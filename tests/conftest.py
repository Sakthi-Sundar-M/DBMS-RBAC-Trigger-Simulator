import pytest
import psycopg2
import toml
import os

SECRETS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".streamlit", "secrets.toml")

@pytest.fixture
def db_conn():
    """Provides a transactional database connection for trigger integration tests."""
    if not os.path.exists(SECRETS_PATH):
        pytest.skip("secrets.toml not found; skipping live database tests.")
    try:
        cfg = toml.load(SECRETS_PATH)
        conn = psycopg2.connect(
            host=cfg["DB_HOST"],
            database=cfg["DB_NAME"],
            user=cfg["DB_USER"],
            password=cfg["DB_PASS"],
            port=cfg.get("DB_PORT", "5432")
        )
        conn.autocommit = False
    except Exception as e:
        pytest.skip(f"Database connection failed: {e}")

    # Pre-test cleanup
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

    yield conn

    # Post-test cleanup
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
    finally:
        conn.close()
