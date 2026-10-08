import psycopg2
import toml
import os

SECRETS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".streamlit", "secrets.toml")

class AssertRaises:
    def __init__(self, exc_type):
        self.exc_type = exc_type
        self.value = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            raise AssertionError(f"Expected exception of type {self.exc_type.__name__} was not raised.")
        if issubclass(exc_type, self.exc_type):
            self.value = exc_val
            return True
        return False

def db_config():
    return toml.load(SECRETS_PATH)



# ============================================================================
# TRIGGER 1: process_transaction (BEFORE INSERT on daily_transactions)
# ============================================================================

def test_process_transaction_pass(db_conn):
    """Test 1A: Passing transfer with KYC approved, active accounts, sufficient balance."""
    with db_conn.cursor() as cur:
        cur.execute("INSERT INTO customer_profiles (profile_id, full_name, phone_number, kyc_status) VALUES (9001, 'Alice Sender', '9876543210', 'APPROVED');")
        cur.execute("INSERT INTO customer_profiles (profile_id, full_name, phone_number, kyc_status) VALUES (9002, 'Bob Receiver', '9876543211', 'APPROVED');")
        cur.execute("INSERT INTO customer_accounts (account_id, profile_id, account_type, balance, account_status) VALUES (9001, 9001, 'SAVINGS', 5000.00, 'ACTIVE');")
        cur.execute("INSERT INTO customer_accounts (account_id, profile_id, account_type, balance, account_status) VALUES (9002, 9002, 'CURRENT', 1000.00, 'ACTIVE');")
        db_conn.commit()

        cur.execute("SET ROLE retail_customer;")
        cur.execute("""
            INSERT INTO daily_transactions (sender_id, receiver_id, amount, transaction_type) 
            VALUES (9001, 9002, 500.00, 'INTERNAL');
        """)
        db_conn.commit()
        cur.execute("RESET ROLE;")

        cur.execute("SELECT balance FROM customer_accounts WHERE account_id = 9001;")
        assert cur.fetchone()[0] == 4500.00
        cur.execute("SELECT balance FROM customer_accounts WHERE account_id = 9002;")
        assert cur.fetchone()[0] == 1500.00
        print("\n[TRIGGER 1 PASS] Transaction succeeded and balances updated (Sender: 5000 -> 4500, Receiver: 1000 -> 1500)")


def test_process_transaction_reject_kyc(db_conn):
    """Test 1B: Rejection when sender KYC is PENDING."""
    with db_conn.cursor() as cur:
        cur.execute("INSERT INTO customer_profiles (profile_id, full_name, phone_number, kyc_status) VALUES (9003, 'Charlie Pending', '9876543212', 'PENDING');")
        cur.execute("INSERT INTO customer_profiles (profile_id, full_name, phone_number, kyc_status) VALUES (9004, 'David Receiver', '9876543213', 'APPROVED');")
        cur.execute("INSERT INTO customer_accounts (account_id, profile_id, account_type, balance, account_status) VALUES (9003, 9003, 'SAVINGS', 5000.00, 'ACTIVE');")
        cur.execute("INSERT INTO customer_accounts (account_id, profile_id, account_type, balance, account_status) VALUES (9004, 9004, 'SAVINGS', 1000.00, 'ACTIVE');")
        db_conn.commit()

        cur.execute("SET ROLE retail_customer;")
        with AssertRaises(psycopg2.Error) as exc_info:
            cur.execute("INSERT INTO daily_transactions (sender_id, receiver_id, amount, transaction_type) VALUES (9003, 9004, 200.00, 'INTERNAL');")
        db_conn.rollback()
        cur.execute("RESET ROLE;")

        raised_text = str(exc_info.value).strip()
        print(f"\n[TRIGGER 1 REJECT - KYC] Expected Exception Caught:\n  >>> {raised_text}")
        assert "KYC_CHECK_FAILED" in raised_text


def test_process_transaction_reject_frozen_account(db_conn):
    """Test 1C: Rejection when sender account is FROZEN."""
    with db_conn.cursor() as cur:
        cur.execute("INSERT INTO customer_profiles (profile_id, full_name, phone_number, kyc_status) VALUES (9005, 'Eve Frozen', '9876543214', 'APPROVED');")
        cur.execute("INSERT INTO customer_profiles (profile_id, full_name, phone_number, kyc_status) VALUES (9006, 'Frank Active', '9876543215', 'APPROVED');")
        cur.execute("INSERT INTO customer_accounts (account_id, profile_id, account_type, balance, account_status) VALUES (9005, 9005, 'SAVINGS', 5000.00, 'FROZEN');")
        cur.execute("INSERT INTO customer_accounts (account_id, profile_id, account_type, balance, account_status) VALUES (9006, 9006, 'SAVINGS', 1000.00, 'ACTIVE');")
        db_conn.commit()

        cur.execute("SET ROLE retail_customer;")
        with AssertRaises(psycopg2.Error) as exc_info:
            cur.execute("INSERT INTO daily_transactions (sender_id, receiver_id, amount, transaction_type) VALUES (9005, 9006, 200.00, 'INTERNAL');")
        db_conn.rollback()
        cur.execute("RESET ROLE;")

        raised_text = str(exc_info.value).strip()
        print(f"\n[TRIGGER 1 REJECT - FROZEN] Expected Exception Caught:\n  >>> {raised_text}")
        assert "ACCOUNT_FROZEN_BLOCKED" in raised_text


def test_process_transaction_reject_fraud_alert(db_conn):
    """Test 1D: Rejection when sender account has an active fraud alert."""
    with db_conn.cursor() as cur:
        cur.execute("INSERT INTO customer_profiles (profile_id, full_name, phone_number, kyc_status) VALUES (9007, 'Grace Alert', '9876543216', 'APPROVED');")
        cur.execute("INSERT INTO customer_profiles (profile_id, full_name, phone_number, kyc_status) VALUES (9008, 'Heidi Receiver', '9876543217', 'APPROVED');")
        cur.execute("INSERT INTO customer_accounts (account_id, profile_id, account_type, balance, account_status) VALUES (9007, 9007, 'SAVINGS', 5000.00, 'ACTIVE');")
        cur.execute("INSERT INTO customer_accounts (account_id, profile_id, account_type, balance, account_status) VALUES (9008, 9008, 'SAVINGS', 1000.00, 'ACTIVE');")
        cur.execute("INSERT INTO fraud_alerts (account_id, risk_reason, alert_status) VALUES (9007, 'Suspicious rapid transfers', 'OPEN');")
        db_conn.commit()

        cur.execute("SET ROLE retail_customer;")
        with AssertRaises(psycopg2.Error) as exc_info:
            cur.execute("INSERT INTO daily_transactions (sender_id, receiver_id, amount, transaction_type) VALUES (9007, 9008, 200.00, 'INTERNAL');")
        db_conn.rollback()
        cur.execute("RESET ROLE;")

        raised_text = str(exc_info.value).strip()
        print(f"\n[TRIGGER 1 REJECT - FRAUD] Expected Exception Caught:\n  >>> {raised_text}")
        assert "FRAUD_CHECK_FAILED" in raised_text


# ============================================================================
# TRIGGER 2: check_loan_eligibility (BEFORE INSERT on loan_applications)
# ============================================================================

def test_check_loan_eligibility_pass(db_conn):
    """Test 2A: Passing loan application for eligible customer with approved KYC."""
    with db_conn.cursor() as cur:
        cur.execute("INSERT INTO customer_profiles (profile_id, full_name, phone_number, kyc_status) VALUES (9010, 'Ivan Borrower', '9876543218', 'APPROVED');")
        cur.execute("INSERT INTO customer_accounts (account_id, profile_id, account_type, balance, account_status) VALUES (9010, 9010, 'SAVINGS', 2000.00, 'ACTIVE');")
        db_conn.commit()

        cur.execute("SET ROLE branch_manager;")
        cur.execute("INSERT INTO loan_applications (profile_id, requested_amount) VALUES (9010, 75000.00);")
        db_conn.commit()
        cur.execute("RESET ROLE;")

        cur.execute("SELECT approval_status FROM loan_applications WHERE profile_id = 9010;")
        status = cur.fetchone()[0]
        assert status == 'SUBMITTED'
        print("\n[TRIGGER 2 PASS] Loan application accepted with initial status: SUBMITTED")


def test_check_loan_eligibility_reject_stacking(db_conn):
    """Test 2B: Rejection when customer already has an active loan application (loan stacking)."""
    with db_conn.cursor() as cur:
        cur.execute("INSERT INTO customer_profiles (profile_id, full_name, phone_number, kyc_status) VALUES (9011, 'Judy Stacking', '9876543219', 'APPROVED');")
        cur.execute("INSERT INTO customer_accounts (account_id, profile_id, account_type, balance, account_status) VALUES (9011, 9011, 'SAVINGS', 2000.00, 'ACTIVE');")
        cur.execute("INSERT INTO loan_applications (profile_id, requested_amount, approval_status) VALUES (9011, 50000.00, 'SUBMITTED');")
        db_conn.commit()

        cur.execute("SET ROLE branch_manager;")
        with AssertRaises(psycopg2.Error) as exc_info:
            cur.execute("INSERT INTO loan_applications (profile_id, requested_amount) VALUES (9011, 25000.00);")
        db_conn.rollback()
        cur.execute("RESET ROLE;")

        raised_text = str(exc_info.value).strip()
        print(f"\n[TRIGGER 2 REJECT - STACKING] Expected Exception Caught:\n  >>> {raised_text}")
        assert "LOAN_STACKING_BLOCKED" in raised_text


def test_check_loan_eligibility_reject_frozen_account(db_conn):
    """Test 2C: Rejection when applicant has a frozen account."""
    with db_conn.cursor() as cur:
        cur.execute("INSERT INTO customer_profiles (profile_id, full_name, phone_number, kyc_status) VALUES (9012, 'Kevin Frozen', '9876543220', 'APPROVED');")
        cur.execute("INSERT INTO customer_accounts (account_id, profile_id, account_type, balance, account_status) VALUES (9012, 9012, 'SAVINGS', 2000.00, 'FROZEN');")
        db_conn.commit()

        cur.execute("SET ROLE branch_manager;")
        with AssertRaises(psycopg2.Error) as exc_info:
            cur.execute("INSERT INTO loan_applications (profile_id, requested_amount) VALUES (9012, 30000.00);")
        db_conn.rollback()
        cur.execute("RESET ROLE;")

        raised_text = str(exc_info.value).strip()
        print(f"\n[TRIGGER 2 REJECT - FROZEN] Expected Exception Caught:\n  >>> {raised_text}")
        assert "LOAN_ACCOUNT_COMPROMISED" in raised_text


# ============================================================================
# TRIGGER 3: enforce_loan_workflow (BEFORE UPDATE on loan_applications)
# ============================================================================

def test_enforce_loan_workflow_pass(db_conn):
    """Test 3A: Passing linear workflow: SUBMITTED -> UNDERWRITE -> APPROVED."""
    with db_conn.cursor() as cur:
        cur.execute("INSERT INTO customer_profiles (profile_id, full_name, phone_number, kyc_status) VALUES (9013, 'Laura Workflow', '9876543221', 'APPROVED');")
        cur.execute("INSERT INTO customer_accounts (account_id, profile_id, account_type, balance, account_status) VALUES (9013, 9013, 'SAVINGS', 5000.00, 'ACTIVE');")
        cur.execute("INSERT INTO loan_applications (profile_id, requested_amount, approval_status) VALUES (9013, 100000.00, 'SUBMITTED');")
        db_conn.commit()

        # Step 1: Senior Underwriter moves SUBMITTED -> UNDERWRITE
        cur.execute("SET ROLE senior_underwriter;")
        cur.execute("UPDATE loan_applications SET approval_status = 'UNDERWRITE' WHERE profile_id = 9013;")
        db_conn.commit()
        cur.execute("RESET ROLE;")

        cur.execute("SELECT approval_status FROM loan_applications WHERE profile_id = 9013;")
        assert cur.fetchone()[0] == 'UNDERWRITE'

        # Step 2: Branch Manager moves UNDERWRITE -> APPROVED
        cur.execute("SET ROLE branch_manager;")
        cur.execute("UPDATE loan_applications SET approval_status = 'APPROVED' WHERE profile_id = 9013;")
        db_conn.commit()
        cur.execute("RESET ROLE;")

        cur.execute("SELECT approval_status FROM loan_applications WHERE profile_id = 9013;")
        assert cur.fetchone()[0] == 'APPROVED'
        print("\n[TRIGGER 3 PASS] Loan workflow succeeded: SUBMITTED -> UNDERWRITE -> APPROVED")


def test_enforce_loan_workflow_reject_skip_stage(db_conn):
    """Test 3B: Rejection when skipping stage (SUBMITTED directly to APPROVED)."""
    with db_conn.cursor() as cur:
        cur.execute("INSERT INTO customer_profiles (profile_id, full_name, phone_number, kyc_status) VALUES (9014, 'Mallory Skip', '9876543222', 'APPROVED');")
        cur.execute("INSERT INTO customer_accounts (account_id, profile_id, account_type, balance, account_status) VALUES (9014, 9014, 'SAVINGS', 5000.00, 'ACTIVE');")
        cur.execute("INSERT INTO loan_applications (profile_id, requested_amount, approval_status) VALUES (9014, 100000.00, 'SUBMITTED');")
        db_conn.commit()

        cur.execute("SET ROLE branch_manager;")
        with AssertRaises(psycopg2.Error) as exc_info:
            cur.execute("UPDATE loan_applications SET approval_status = 'APPROVED' WHERE profile_id = 9014;")
        db_conn.rollback()
        cur.execute("RESET ROLE;")

        raised_text = str(exc_info.value).strip()
        print(f"\n[TRIGGER 3 REJECT - SKIP STAGE] Expected Exception Caught:\n  >>> {raised_text}")
        assert "WORKFLOW_STAGE_SKIPPED" in raised_text


def test_enforce_loan_workflow_reject_backward(db_conn):
    """Test 3C: Rejection when moving backward (UNDERWRITE back to SUBMITTED)."""
    with db_conn.cursor() as cur:
        cur.execute("INSERT INTO customer_profiles (profile_id, full_name, phone_number, kyc_status) VALUES (9015, 'Ned Backward', '9876543223', 'APPROVED');")
        cur.execute("INSERT INTO customer_accounts (account_id, profile_id, account_type, balance, account_status) VALUES (9015, 9015, 'SAVINGS', 5000.00, 'ACTIVE');")
        cur.execute("INSERT INTO loan_applications (profile_id, requested_amount, approval_status) VALUES (9015, 100000.00, 'UNDERWRITE');")
        db_conn.commit()

        cur.execute("SET ROLE senior_underwriter;")
        with AssertRaises(psycopg2.Error) as exc_info:
            cur.execute("UPDATE loan_applications SET approval_status = 'SUBMITTED' WHERE profile_id = 9015;")
        db_conn.rollback()
        cur.execute("RESET ROLE;")

        raised_text = str(exc_info.value).strip()
        print(f"\n[TRIGGER 3 REJECT - BACKWARD] Expected Exception Caught:\n  >>> {raised_text}")
        assert "WORKFLOW_BACKWARD_TRANSITION" in raised_text


# ============================================================================
# TRIGGER 4: log_audit_event (AFTER UPDATE on customer_accounts & loan_applications)
# ============================================================================

def test_log_audit_event_account_status(db_conn):
    """Test 4A: Branch Manager freezes an account, silently logging audit event."""
    with db_conn.cursor() as cur:
        cur.execute("INSERT INTO customer_profiles (profile_id, full_name, phone_number, kyc_status) VALUES (9016, 'Olivia Audit', '9876543224', 'APPROVED');")
        cur.execute("INSERT INTO customer_accounts (account_id, profile_id, account_type, balance, account_status) VALUES (9016, 9016, 'SAVINGS', 3000.00, 'ACTIVE');")
        db_conn.commit()

        # Branch manager updates account status to FROZEN
        cur.execute("SET ROLE branch_manager;")
        cur.execute("UPDATE customer_accounts SET account_status = 'FROZEN' WHERE account_id = 9016;")
        db_conn.commit()
        cur.execute("RESET ROLE;")

        # Verify audit_log entry recorded silently
        cur.execute("""
            SELECT table_name, record_id, action, old_value, new_value, changed_by 
            FROM audit_log 
            WHERE record_id = 9016 AND table_name = 'customer_accounts'
            ORDER BY log_id DESC LIMIT 1;
        """)
        audit_entry = cur.fetchone()
        assert audit_entry is not None
        table_name, record_id, action, old_val, new_val, changed_by = audit_entry
        assert table_name == 'customer_accounts'
        assert record_id == 9016
        assert action == 'UPDATE'
        assert 'ACTIVE' in old_val
        assert 'FROZEN' in new_val
        assert changed_by == 'branch_manager'
        print(f"\n[TRIGGER 4 PASS - ACCOUNT AUDIT] Audit entry created: table={table_name}, record_id={record_id}, old={old_val}, new={new_val}, actor={changed_by}")


def test_log_audit_event_loan_status(db_conn):
    """Test 4B: Senior Underwriter moves loan to UNDERWRITE, silently logging audit event."""
    with db_conn.cursor() as cur:
        cur.execute("INSERT INTO customer_profiles (profile_id, full_name, phone_number, kyc_status) VALUES (9017, 'Paul LoanAudit', '9876543225', 'APPROVED');")
        cur.execute("INSERT INTO customer_accounts (account_id, profile_id, account_type, balance, account_status) VALUES (9017, 9017, 'SAVINGS', 3000.00, 'ACTIVE');")
        cur.execute("INSERT INTO loan_applications (profile_id, requested_amount, approval_status) VALUES (9017, 40000.00, 'SUBMITTED');")
        db_conn.commit()

        cur.execute("SELECT loan_id FROM loan_applications WHERE profile_id = 9017;")
        loan_id = cur.fetchone()[0]

        # Senior Underwriter updates status
        cur.execute("SET ROLE senior_underwriter;")
        cur.execute(f"UPDATE loan_applications SET approval_status = 'UNDERWRITE' WHERE loan_id = {loan_id};")
        db_conn.commit()
        cur.execute("RESET ROLE;")

        # Verify audit_log entry recorded silently
        cur.execute("""
            SELECT table_name, record_id, action, old_value, new_value, changed_by 
            FROM audit_log 
            WHERE record_id = %s AND table_name = 'loan_applications'
            ORDER BY log_id DESC LIMIT 1;
        """, (loan_id,))
        audit_entry = cur.fetchone()
        assert audit_entry is not None
        table_name, record_id, action, old_val, new_val, changed_by = audit_entry
        assert table_name == 'loan_applications'
        assert record_id == loan_id
        assert action == 'UPDATE'
        assert 'SUBMITTED' in old_val
        assert 'UNDERWRITE' in new_val
        assert changed_by == 'senior_underwriter'
        print(f"\n[TRIGGER 4 PASS - LOAN AUDIT] Audit entry created: table={table_name}, record_id={record_id}, old={old_val}, new={new_val}, actor={changed_by}")


if __name__ == "__main__":
    print("=" * 80)
    print("RUNNING DATABASE TRIGGER VERIFICATION TEST HARNESS (PHASE 3)")
    print("=" * 80)

    cfg = db_config()
    conn = psycopg2.connect(
        host=cfg["DB_HOST"], database=cfg["DB_NAME"],
        user=cfg["DB_USER"], password=cfg["DB_PASS"]
    )
    conn.autocommit = False

    test_functions = [
        ("Trigger 1: process_transaction - Valid Transfer (Pass)", test_process_transaction_pass),
        ("Trigger 1: process_transaction - Pending KYC (Reject)", test_process_transaction_reject_kyc),
        ("Trigger 1: process_transaction - Frozen Account (Reject)", test_process_transaction_reject_frozen_account),
        ("Trigger 1: process_transaction - Active Fraud Alert (Reject)", test_process_transaction_reject_fraud_alert),
        ("Trigger 2: check_loan_eligibility - Eligible Customer (Pass)", test_check_loan_eligibility_pass),
        ("Trigger 2: check_loan_eligibility - Loan Stacking (Reject)", test_check_loan_eligibility_reject_stacking),
        ("Trigger 2: check_loan_eligibility - Frozen Account (Reject)", test_check_loan_eligibility_reject_frozen_account),
        ("Trigger 3: enforce_loan_workflow - Linear Progression (Pass)", test_enforce_loan_workflow_pass),
        ("Trigger 3: enforce_loan_workflow - Skip Stage (Reject)", test_enforce_loan_workflow_reject_skip_stage),
        ("Trigger 3: enforce_loan_workflow - Backward Transition (Reject)", test_enforce_loan_workflow_reject_backward),
        ("Trigger 4: log_audit_event - Account Status Audit (Pass)", test_log_audit_event_account_status),
        ("Trigger 4: log_audit_event - Loan Status Audit (Pass)", test_log_audit_event_loan_status),
    ]

    passed = 0
    failed = 0

    for name, func in test_functions:
        print(f"\n--- Running: {name} ---")
        try:
            # Clean before
            with conn.cursor() as cur:
                cur.execute("RESET ROLE;")
                cur.execute("DELETE FROM daily_transactions WHERE sender_id >= 9000 OR receiver_id >= 9000;")
                cur.execute("DELETE FROM fraud_alerts WHERE account_id >= 9000;")
                cur.execute("DELETE FROM loan_applications WHERE profile_id >= 9000;")
                cur.execute("DELETE FROM audit_log WHERE record_id >= 9000 OR account_id >= 9000;")
                cur.execute("DELETE FROM customer_accounts WHERE account_id >= 9000;")
                cur.execute("DELETE FROM customer_profiles WHERE profile_id >= 9000;")
            conn.commit()

            func(conn)
            passed += 1
            print(f"RESULT: [PASS] {name}")
        except Exception as e:
            failed += 1
            print(f"RESULT: [FAIL] {name}: {e}")
        finally:
            # Clean after
            try:
                with conn.cursor() as cur:
                    cur.execute("RESET ROLE;")
                    cur.execute("DELETE FROM daily_transactions WHERE sender_id >= 9000 OR receiver_id >= 9000;")
                    cur.execute("DELETE FROM fraud_alerts WHERE account_id >= 9000;")
                    cur.execute("DELETE FROM loan_applications WHERE profile_id >= 9000;")
                    cur.execute("DELETE FROM audit_log WHERE record_id >= 9000 OR account_id >= 9000;")
                    cur.execute("DELETE FROM customer_accounts WHERE account_id >= 9000;")
                    cur.execute("DELETE FROM customer_profiles WHERE profile_id >= 9000;")
                conn.commit()
            except Exception:
                conn.rollback()

    conn.close()
    print("\n" + "=" * 80)
    print(f"SUMMARY: {passed} PASSED, {failed} FAILED out of {len(test_functions)} tests.")
    print("=" * 80)
    if failed > 0:
        exit(1)

