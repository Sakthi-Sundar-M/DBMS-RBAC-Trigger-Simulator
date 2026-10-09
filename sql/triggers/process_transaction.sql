-- Trigger 1: process_transaction (BEFORE INSERT on daily_transactions)
CREATE OR REPLACE FUNCTION process_transaction()
RETURNS TRIGGER SECURITY DEFINER SET search_path = public, pg_temp AS $$
DECLARE
    sender_kyc VARCHAR(20);
    receiver_kyc VARCHAR(20);
    sender_status VARCHAR(20);
    receiver_status VARCHAR(20);
    sender_balance NUMERIC(15, 2);
    alert_account INT;
    alert_reason TEXT;
BEGIN
    -- 0. Self-Transfer Guard (sender and receiver must differ)
    IF NEW.sender_id = NEW.receiver_id THEN
        RAISE EXCEPTION 'TRANSACTION_SELF_BLOCKED: Sender and receiver account cannot be the same (Account ID: %).', NEW.sender_id;
    END IF;

    -- 1. Identity & KYC Verification Check
    SELECT kyc_status INTO sender_kyc FROM customer_profiles cp
    JOIN customer_accounts ca ON ca.profile_id = cp.profile_id WHERE ca.account_id = NEW.sender_id;
    SELECT kyc_status INTO receiver_kyc FROM customer_profiles cp
    JOIN customer_accounts ca ON ca.profile_id = cp.profile_id WHERE ca.account_id = NEW.receiver_id;

    IF sender_kyc IS NULL OR sender_kyc <> 'APPROVED' THEN
        RAISE EXCEPTION 'KYC_CHECK_FAILED: Sender KYC verification not approved (status: %).', COALESCE(sender_kyc, 'NOT_FOUND');
    END IF;
    IF receiver_kyc IS NULL OR receiver_kyc <> 'APPROVED' THEN
        RAISE EXCEPTION 'KYC_CHECK_FAILED: Receiver KYC verification not approved (status: %).', COALESCE(receiver_kyc, 'NOT_FOUND');
    END IF;

    -- 2. Operational Health Check (Frozen / Closed)
    SELECT account_status, balance INTO sender_status, sender_balance FROM customer_accounts WHERE account_id = NEW.sender_id;
    SELECT account_status INTO receiver_status FROM customer_accounts WHERE account_id = NEW.receiver_id;

    IF sender_status IN ('FROZEN', 'CLOSED') THEN
        RAISE EXCEPTION 'ACCOUNT_FROZEN_BLOCKED: Sender account % is currently %.', NEW.sender_id, sender_status;
    END IF;
    IF receiver_status IN ('FROZEN', 'CLOSED') THEN
        RAISE EXCEPTION 'ACCOUNT_FROZEN_BLOCKED: Receiver account % is currently %.', NEW.receiver_id, receiver_status;
    END IF;

    -- 3. Risk Intelligence & Fraud Alerts Check
    SELECT account_id, risk_reason INTO alert_account, alert_reason FROM fraud_alerts
    WHERE account_id IN (NEW.sender_id, NEW.receiver_id) AND alert_status IN ('OPEN', 'UNDER_INVESTIGATION') LIMIT 1;
    IF FOUND THEN
        RAISE EXCEPTION 'FRAUD_CHECK_FAILED: Active fraud alert on file for account % (Reason: %).', alert_account, alert_reason;
    END IF;

    -- 4. Balance Sufficiency & In-Engine Atomic Mutation
    IF sender_balance < NEW.amount THEN
        RAISE EXCEPTION 'INSUFFICIENT_FUNDS: Sender balance ($%) insufficient for transfer amount ($%).', sender_balance, NEW.amount;
    END IF;

    UPDATE customer_accounts SET balance = balance - NEW.amount WHERE account_id = NEW.sender_id;
    UPDATE customer_accounts SET balance = balance + NEW.amount WHERE account_id = NEW.receiver_id;

    RETURN NEW; -- Proceeds to commit transaction row
END;
$$ LANGUAGE plpgsql;
