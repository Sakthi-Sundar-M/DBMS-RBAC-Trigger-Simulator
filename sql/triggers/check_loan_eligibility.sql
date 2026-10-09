-- Trigger 2: check_loan_eligibility (BEFORE INSERT on loan_applications)
CREATE OR REPLACE FUNCTION check_loan_eligibility()
RETURNS TRIGGER SECURITY DEFINER SET search_path = public, pg_temp AS $$
DECLARE
    customer_kyc VARCHAR(20);
    existing_loan_id INT;
    bad_account_id INT;
BEGIN
    -- 1. Applicant KYC Verification
    SELECT kyc_status INTO customer_kyc FROM customer_profiles WHERE profile_id = NEW.profile_id;
    IF customer_kyc IS NULL OR customer_kyc <> 'APPROVED' THEN
        RAISE EXCEPTION 'LOAN_KYC_FAILED: Loan applicant KYC not approved (status: %).', COALESCE(customer_kyc, 'NOT_FOUND');
    END IF;

    -- 2. Anti-Loan Stacking Rule
    SELECT loan_id INTO existing_loan_id FROM loan_applications
    WHERE profile_id = NEW.profile_id AND approval_status IN ('SUBMITTED', 'UNDERWRITE') LIMIT 1;
    IF FOUND THEN
        RAISE EXCEPTION 'LOAN_STACKING_BLOCKED: Customer already has an active loan application under review (Loan ID: %).', existing_loan_id;
    END IF;

    -- 3. Account Operational Health Check
    SELECT account_id INTO bad_account_id FROM customer_accounts
    WHERE profile_id = NEW.profile_id AND account_status IN ('FROZEN', 'CLOSED') LIMIT 1;
    IF FOUND THEN
        RAISE EXCEPTION 'LOAN_ACCOUNT_COMPROMISED: Loan application blocked. Customer holds a FROZEN/CLOSED account (Account ID: %).', bad_account_id;
    END IF;

    NEW.approval_status := COALESCE(NEW.approval_status, 'SUBMITTED');
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
