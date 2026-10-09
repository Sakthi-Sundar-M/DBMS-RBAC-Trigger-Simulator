import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os

ROLES = [
    "bank_teller",
    "branch_manager",
    "fraud_analyst",
    "senior_underwriter",
    "it_security_admin",
    "internal_auditor",
    "retail_customer",
    "loan_officer",
    "csr"
]

def setup_database():
    print("1. Connecting to PostgreSQL server...")
    conn = psycopg2.connect(host="localhost", port=5432, user="postgres", dbname="postgres")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()

    # Create neondb database if not exists
    cur.execute("SELECT 1 FROM pg_database WHERE datname = 'neondb';")
    if not cur.fetchone():
        cur.execute("CREATE DATABASE neondb;")
        print("Created database: neondb")
    else:
        print("Database neondb already exists.")

    # Create or update neondb_owner role
    cur.execute("SELECT 1 FROM pg_roles WHERE rolname = 'neondb_owner';")
    if not cur.fetchone():
        cur.execute("CREATE ROLE neondb_owner WITH SUPERUSER LOGIN PASSWORD 'neondb_password';")
        print("Created role: neondb_owner")
    else:
        cur.execute("ALTER ROLE neondb_owner WITH SUPERUSER LOGIN PASSWORD 'neondb_password';")
        print("Updated role: neondb_owner")

    cur.close()
    conn.close()

    print("2. Connecting to neondb as neondb_owner...")
    db_conn = psycopg2.connect(host="localhost", port=5432, user="neondb_owner", password="neondb_password", dbname="neondb")
    db_conn.autocommit = True
    db_cur = db_conn.cursor()

    # Create RBAC roles
    print("3. Creating simulator RBAC roles...")
    for role in ROLES:
        db_cur.execute(f"SELECT 1 FROM pg_roles WHERE rolname = '{role}';")
        if not db_cur.fetchone():
            db_cur.execute(f"CREATE ROLE {role};")
            print(f"Created role: {role}")
        db_cur.execute(f"GRANT {role} TO neondb_owner;")

    # Create tables
    print("4. Creating tables...")
    db_cur.execute("""
    CREATE TABLE IF NOT EXISTS customer_profiles (
        profile_id INT PRIMARY KEY,
        full_name VARCHAR(100) NOT NULL,
        phone_number VARCHAR(20) NOT NULL,
        kyc_status VARCHAR(20) DEFAULT 'PENDING'
    );

    CREATE TABLE IF NOT EXISTS customer_accounts (
        account_id INT PRIMARY KEY,
        profile_id INT REFERENCES customer_profiles(profile_id) ON DELETE CASCADE,
        account_type VARCHAR(20) NOT NULL,
        balance NUMERIC(15, 2) NOT NULL DEFAULT 0.00,
        account_status VARCHAR(20) NOT NULL DEFAULT 'ACTIVE'
    );

    CREATE TABLE IF NOT EXISTS daily_transactions (
        transaction_id SERIAL PRIMARY KEY,
        sender_id INT REFERENCES customer_accounts(account_id),
        receiver_id INT REFERENCES customer_accounts(account_id),
        amount NUMERIC(15, 2) NOT NULL,
        transaction_type VARCHAR(20) DEFAULT 'INTERNAL',
        created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS fraud_alerts (
        alert_id SERIAL PRIMARY KEY,
        account_id INT REFERENCES customer_accounts(account_id),
        risk_reason TEXT NOT NULL,
        alert_status VARCHAR(30) DEFAULT 'OPEN',
        created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS loan_applications (
        loan_id SERIAL PRIMARY KEY,
        profile_id INT REFERENCES customer_profiles(profile_id) ON DELETE CASCADE,
        requested_amount NUMERIC(15, 2) NOT NULL,
        approval_status VARCHAR(30) DEFAULT 'SUBMITTED',
        applied_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS audit_log (
        log_id SERIAL PRIMARY KEY,
        changed_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
        changed_by VARCHAR(50) NOT NULL,
        table_name VARCHAR(50) NOT NULL,
        record_id INT NOT NULL,
        account_id INT,
        action VARCHAR(20) NOT NULL,
        old_value TEXT,
        new_value TEXT
    );
    """)

    # Create Functions and Triggers
    print("5. Installing PL/pgSQL triggers and procedures...")
    trigger_files = [
        "process_transaction.sql",
        "check_loan_eligibility.sql",
        "enforce_loan_workflow.sql",
        "log_audit_event.sql"
    ]
    base_sql_dir = os.path.join(os.path.dirname(__file__), "sql", "triggers")
    for tf in trigger_files:
        path = os.path.join(base_sql_dir, tf)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                db_cur.execute(f.read())
            print(f"Installed trigger function: {tf}")

    db_cur.execute("""
    DROP TRIGGER IF EXISTS trg_process_transaction ON daily_transactions;
    CREATE TRIGGER trg_process_transaction
    BEFORE INSERT ON daily_transactions
    FOR EACH ROW
    EXECUTE FUNCTION process_transaction();

    DROP TRIGGER IF EXISTS trg_check_loan_eligibility ON loan_applications;
    CREATE TRIGGER trg_check_loan_eligibility
    BEFORE INSERT ON loan_applications
    FOR EACH ROW
    EXECUTE FUNCTION check_loan_eligibility();

    DROP TRIGGER IF EXISTS trg_enforce_loan_workflow ON loan_applications;
    CREATE TRIGGER trg_enforce_loan_workflow
    BEFORE UPDATE ON loan_applications
    FOR EACH ROW
    EXECUTE FUNCTION enforce_loan_workflow();

    DROP TRIGGER IF EXISTS trg_log_audit_customer_accounts ON customer_accounts;
    CREATE TRIGGER trg_log_audit_customer_accounts
    AFTER UPDATE ON customer_accounts
    FOR EACH ROW
    EXECUTE FUNCTION log_audit_event();

    DROP TRIGGER IF EXISTS trg_log_audit_loan_applications ON loan_applications;
    CREATE TRIGGER trg_log_audit_loan_applications
    AFTER UPDATE ON loan_applications
    FOR EACH ROW
    EXECUTE FUNCTION log_audit_event();
    """)

    # Install helper functions for viewers
    print("6. Creating helper functions secure_account_viewer & secure_transaction_viewer...")
    db_cur.execute("""
    CREATE OR REPLACE FUNCTION secure_account_viewer(
        p_acc_id INT DEFAULT 0,
        p_prof_id INT DEFAULT 0,
        p_name TEXT DEFAULT 'NA'
    )
    RETURNS TABLE (
        account_id INT,
        profile_id INT,
        full_name VARCHAR,
        account_type VARCHAR,
        balance NUMERIC,
        account_status VARCHAR
    ) AS $$
    BEGIN
        RETURN QUERY
        SELECT 
            ca.account_id,
            ca.profile_id,
            cp.full_name,
            ca.account_type,
            ca.balance,
            ca.account_status
        FROM customer_accounts ca
        JOIN customer_profiles cp ON cp.profile_id = ca.profile_id
        WHERE (p_acc_id = 0 OR ca.account_id = p_acc_id)
          AND (p_prof_id = 0 OR ca.profile_id = p_prof_id)
          AND (p_name = 'NA' OR cp.full_name ILIKE '%' || p_name || '%')
        ORDER BY ca.account_id;
    END;
    $$ LANGUAGE plpgsql SECURITY DEFINER SET search_path = public, pg_temp;

    CREATE OR REPLACE FUNCTION secure_transaction_viewer(
        p_acc_id INT DEFAULT 0,
        p_prof_id INT DEFAULT 0,
        p_name TEXT DEFAULT 'NA'
    )
    RETURNS TABLE (
        transaction_id INT,
        sender_id INT,
        receiver_id INT,
        amount NUMERIC,
        transaction_type VARCHAR,
        created_at TIMESTAMPTZ
    ) AS $$
    BEGIN
        RETURN QUERY
        SELECT 
            dt.transaction_id,
            dt.sender_id,
            dt.receiver_id,
            dt.amount,
            dt.transaction_type,
            dt.created_at
        FROM daily_transactions dt
        WHERE (p_acc_id = 0 OR dt.sender_id = p_acc_id OR dt.receiver_id = p_acc_id)
        ORDER BY dt.created_at DESC;
    END;
    $$ LANGUAGE plpgsql SECURITY DEFINER SET search_path = public, pg_temp;
    """)

    # Grant RBAC permissions
    print("7. Configuring RBAC security permissions matrix...")
    db_cur.execute("""
    -- Allow usage on schema and sequences
    GRANT USAGE ON SCHEMA public TO PUBLIC;
    GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO PUBLIC;
    GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO PUBLIC;

    -- Bank Teller
    GRANT SELECT, INSERT ON customer_accounts TO bank_teller;
    GRANT UPDATE (balance) ON customer_accounts TO bank_teller;
    GRANT SELECT, INSERT ON daily_transactions TO bank_teller;
    GRANT SELECT ON customer_profiles TO bank_teller;

    -- Branch Manager
    GRANT SELECT ON ALL TABLES IN SCHEMA public TO branch_manager;
    GRANT UPDATE (account_status) ON customer_accounts TO branch_manager;
    GRANT UPDATE (alert_status) ON fraud_alerts TO branch_manager;
    GRANT UPDATE (approval_status) ON loan_applications TO branch_manager;
    GRANT INSERT ON loan_applications TO branch_manager;

    -- Fraud Analyst
    GRANT SELECT, INSERT ON fraud_alerts TO fraud_analyst;
    GRANT UPDATE (alert_status) ON fraud_alerts TO fraud_analyst;
    GRANT SELECT ON customer_accounts, daily_transactions TO fraud_analyst;

    -- Senior Underwriter
    GRANT SELECT ON loan_applications, customer_accounts, customer_profiles TO senior_underwriter;
    GRANT UPDATE (approval_status) ON loan_applications TO senior_underwriter;

    -- IT Security Admin
    GRANT SELECT ON audit_log TO it_security_admin;

    -- Internal Auditor
    GRANT SELECT ON customer_profiles, customer_accounts, daily_transactions, fraud_alerts, loan_applications, audit_log TO internal_auditor;

    -- Retail Customer
    GRANT SELECT ON customer_accounts, daily_transactions TO retail_customer;
    GRANT INSERT ON daily_transactions TO retail_customer;

    -- Loan Officer
    GRANT SELECT ON loan_applications, customer_profiles, customer_accounts TO loan_officer;
    GRANT INSERT ON loan_applications TO loan_officer;

    -- CSR
    GRANT SELECT ON customer_accounts, customer_profiles, daily_transactions TO csr;
    GRANT UPDATE (full_name, phone_number) ON customer_profiles TO csr;
    """)

    # Seed initial test data
    print("8. Seeding core sample data...")
    db_cur.execute("""
    INSERT INTO customer_profiles (profile_id, full_name, phone_number, kyc_status)
    VALUES 
        (1, 'Alice Walker', '+1-555-0101', 'APPROVED'),
        (2, 'Bob Vance', '+1-555-0102', 'APPROVED'),
        (3, 'Charlie Pending', '+1-555-0103', 'PENDING'),
        (4, 'David Miller', '+1-555-0104', 'APPROVED'),
        (5, 'Eve Risk', '+1-555-0105', 'APPROVED')
    ON CONFLICT (profile_id) DO NOTHING;

    INSERT INTO customer_accounts (account_id, profile_id, account_type, balance, account_status)
    VALUES 
        (101, 1, 'SAVINGS', 15000.00, 'ACTIVE'),
        (102, 2, 'CURRENT', 8500.00, 'ACTIVE'),
        (103, 3, 'SAVINGS', 2500.00, 'ACTIVE'),
        (104, 4, 'SAVINGS', 12000.00, 'FROZEN'),
        (105, 5, 'CURRENT', 400.00, 'ACTIVE')
    ON CONFLICT (account_id) DO NOTHING;

    INSERT INTO fraud_alerts (account_id, risk_reason, alert_status)
    SELECT 105, 'High velocity anomalous IP transaction pattern', 'OPEN'
    WHERE NOT EXISTS (SELECT 1 FROM fraud_alerts WHERE account_id = 105);

    INSERT INTO loan_applications (profile_id, requested_amount, approval_status)
    SELECT 1, 35000.00, 'SUBMITTED'
    WHERE NOT EXISTS (SELECT 1 FROM loan_applications WHERE profile_id = 1);
    """)

    db_cur.close()
    db_conn.close()
    print("[OK] Database setup complete successfully!")

if __name__ == "__main__":
    setup_database()
