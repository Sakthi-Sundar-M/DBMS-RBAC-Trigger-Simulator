-- Trigger 4: log_audit_event (AFTER UPDATE on customer_accounts, loan_applications & fraud_alerts)
CREATE OR REPLACE FUNCTION log_audit_event()
RETURNS TRIGGER SECURITY DEFINER SET search_path = public, pg_temp AS $$
DECLARE
    resolved_acc_id INT;
BEGIN
    IF TG_TABLE_NAME = 'customer_accounts' THEN
        resolved_acc_id := NEW.account_id;
        INSERT INTO audit_log (table_name, record_id, account_id, action, old_value, new_value, changed_by)
        VALUES ('customer_accounts', NEW.account_id, resolved_acc_id, 'UPDATE',
                format('balance=%s, status=%s', OLD.balance, OLD.account_status),
                format('balance=%s, status=%s', NEW.balance, NEW.account_status),
                COALESCE(NULLIF(current_setting('role', true), 'none'), CURRENT_USER));
    ELSIF TG_TABLE_NAME = 'fraud_alerts' THEN
        INSERT INTO audit_log (table_name, record_id, account_id, action, old_value, new_value, changed_by)
        VALUES ('fraud_alerts', NEW.alert_id, NEW.account_id, 'UPDATE',
                format('alert_status=%s', OLD.alert_status),
                format('alert_status=%s', NEW.alert_status),
                COALESCE(NULLIF(current_setting('role', true), 'none'), CURRENT_USER));
    ELSIF TG_TABLE_NAME = 'loan_applications' THEN
        SELECT account_id INTO resolved_acc_id FROM customer_accounts WHERE profile_id = NEW.profile_id LIMIT 1;
        INSERT INTO audit_log (table_name, record_id, account_id, action, old_value, new_value, changed_by)
        VALUES ('loan_applications', NEW.loan_id, resolved_acc_id, 'UPDATE',
                format('approval=%s, amount=%s', OLD.approval_status, OLD.requested_amount),
                format('approval=%s, amount=%s', NEW.approval_status, NEW.requested_amount),
                COALESCE(NULLIF(current_setting('role', true), 'none'), CURRENT_USER));
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
