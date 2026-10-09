-- Trigger 3: enforce_loan_workflow (BEFORE UPDATE on loan_applications)
CREATE OR REPLACE FUNCTION enforce_loan_workflow()
RETURNS TRIGGER SECURITY DEFINER SET search_path = public, pg_temp AS $$
BEGIN
    IF OLD.approval_status = NEW.approval_status THEN
        RETURN NEW;
    END IF;

    -- 1. Stage-Skipping Guard
    IF OLD.approval_status = 'SUBMITTED' AND NEW.approval_status = 'APPROVED' THEN
        RAISE EXCEPTION 'WORKFLOW_STAGE_SKIPPED: A loan in SUBMITTED state must move to UNDERWRITE before final approval.';
    END IF;

    -- 1b. Linear State Machine: SUBMITTED -> REJECTED must pass through UNDERWRITE
    IF OLD.approval_status = 'SUBMITTED' AND NEW.approval_status = 'REJECTED' THEN
        RAISE EXCEPTION 'WORKFLOW_STAGE_SKIPPED: A loan in SUBMITTED state must move to UNDERWRITE before rejection (SUBMITTED -> REJECTED is not a permitted transition).';
    END IF;

    -- 2. Backward Transition Guard
    IF OLD.approval_status = 'UNDERWRITE' AND NEW.approval_status = 'SUBMITTED' THEN
        RAISE EXCEPTION 'WORKFLOW_BACKWARD_TRANSITION: Backward workflow transitions are prohibited (Cannot revert UNDERWRITE -> SUBMITTED).';
    END IF;
    IF OLD.approval_status IN ('APPROVED', 'REJECTED') THEN
        RAISE EXCEPTION 'WORKFLOW_TERMINAL_STATE: Loan application is already % and cannot be modified further.', OLD.approval_status;
    END IF;

    -- 3. Role-Based Underwriting Enforcement
    IF NEW.approval_status = 'UNDERWRITE' AND COALESCE(NULLIF(current_setting('role', true), 'none'), CURRENT_USER) NOT IN ('senior_underwriter', 'neondb_owner') THEN
        RAISE EXCEPTION 'WORKFLOW_UNAUTHORIZED_ACTOR: Only Senior Underwriters can transition a loan to UNDERWRITE (Current user: %).', COALESCE(NULLIF(current_setting('role', true), 'none'), CURRENT_USER);
    END IF;
    IF NEW.approval_status = 'APPROVED' AND COALESCE(NULLIF(current_setting('role', true), 'none'), CURRENT_USER) NOT IN ('branch_manager', 'neondb_owner') THEN
        RAISE EXCEPTION 'WORKFLOW_UNAUTHORIZED_ACTOR: Only Branch Managers can grant final loan approval (Current user: %).', COALESCE(NULLIF(current_setting('role', true), 'none'), CURRENT_USER);
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
