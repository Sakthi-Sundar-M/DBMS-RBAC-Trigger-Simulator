import psycopg2
import psycopg2.errors
import psycopg2.pool
from psycopg2 import sql
from contextlib import contextmanager
import streamlit as st

def _get_secret(key, default=""):
    try:
        return st.secrets.get(key, default)
    except Exception:
        import os
        return os.environ.get(key, default)

DB_HOST = _get_secret("DB_HOST", "ep-example-pooler.us-east-2.aws.neon.tech")
DB_NAME = _get_secret("DB_NAME", "neondb")
DB_USER = _get_secret("DB_USER", "neondb_owner")
DB_PASS = _get_secret("DB_PASS", "your_secure_password_here")
DB_PORT = _get_secret("DB_PORT", 5432)
DB_SSLMODE = _get_secret("DB_SSLMODE", "require")

POOL_MIN_CONN = 1
POOL_MAX_CONN = 10

# ---------------------------------------------------------------------------
# Connection pool
#
# Every query checks out its own connection and returns it afterwards, so no
# session-level state (role, time zone) can leak between Streamlit sessions.
# Role switching uses SET LOCAL, which lasts only for the current transaction.
# ---------------------------------------------------------------------------

@st.cache_resource
def _create_pool():
    """Builds the shared pool. Raises if the database is unreachable, so a failure is never cached."""
    if not DB_HOST or (DB_HOST == "ep-example-pooler.us-east-2.aws.neon.tech" and DB_PASS == "your_secure_password_here"):
        return None
    return psycopg2.pool.ThreadedConnectionPool(
        POOL_MIN_CONN,
        POOL_MAX_CONN,
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT,
        sslmode=DB_SSLMODE
    )

def _get_pool():
    try:
        return _create_pool()
    except Exception:
        return None

def _acquire(pool):
    """Checks out a connection and verifies it is alive. Returns None if it is stale."""
    conn = pool.getconn()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT 1;")
        conn.rollback()
        return conn
    except Exception:
        pool.putconn(conn, close=True)
        return None

def _release(pool, conn):
    """Ends any open transaction (which also discards SET LOCAL role state) and returns the connection."""
    healthy = False
    if not conn.closed:
        try:
            conn.rollback()
            healthy = True
        except Exception:
            healthy = False
    pool.putconn(conn, close=not healthy)

@contextmanager
def _checkout():
    """Yields a pooled connection, or None if the database is unavailable."""
    pool = _get_pool()
    conn = None
    if pool is not None:
        for _ in range(2):  # one retry in case a pooled connection went stale
            try:
                conn = _acquire(pool)
            except Exception:
                conn = None
            if conn is not None:
                break
    try:
        yield conn
    finally:
        if pool is not None and conn is not None:
            _release(pool, conn)

def is_db_connected():
    """Returns True if a pooled PostgreSQL connection answers SELECT 1, False otherwise."""
    try:
        with _checkout() as conn:
            if conn is None:
                return False
            with conn.cursor() as cur:
                cur.execute("SELECT 1;")
            return True
    except Exception:
        return False

def execute_query_as_role(role_name, query, params=None):
    if params:
        for param in params:
            if isinstance(param, (int, float)) and param < 0:
                return {"status": "error", "message": "Input Error: Negative values are strictly prohibited in this system."}

    offline = {
        "status": "error",
        "message": "Database Offline: Unable to connect to PostgreSQL. Please configure valid Neon credentials in .streamlit/secrets.toml."
    }

    try:
        with _checkout() as conn:
            if conn is None:
                return offline
            with conn.cursor() as cur:
                cur.execute(sql.SQL("SET LOCAL ROLE {};").format(sql.Identifier(role_name)))
                cur.execute("SET LOCAL TIME ZONE 'Asia/Kolkata';")
                cur.execute(query, params)
                data = None
                columns = None
                if cur.description:
                    columns = [desc[0] for desc in cur.description]
                    data = cur.fetchall()
                else:
                    if cur.rowcount == 0:
                        raise Exception("No matching records found in the database. Please check the ID.")
                conn.commit()
                return {"status": "success", "data": data, "columns": columns}
    except psycopg2.errors.InsufficientPrivilege:
        return {"status": "denied", "message": "Access Denied by PostgreSQL."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@st.cache_data(ttl=3600)
def check_table_permission(role, table, privilege, columns=None):
    try:
        with _checkout() as conn:
            if conn is None:
                return False
            with conn.cursor() as cur:
                if columns and len(columns) > 0:
                    for col in columns:
                        cur.execute(
                            "SELECT has_column_privilege(%s, %s, %s, %s);",
                            (role, table, col, privilege)
                        )
                        if not cur.fetchone()[0]:
                            return False
                    return True
                else:
                    cur.execute(
                        "SELECT has_table_privilege(%s, %s, %s);",
                        (role, table, privilege)
                    )
                    return cur.fetchone()[0]
    except Exception:
        return False


@st.cache_data(ttl=3600)
def get_all_permissions_cache(department_name="Banking Department"):
    """
    Evaluates and caches all RBAC permissions for all roles and operations
    in a single round-trip batch SQL query (<250ms).
    Subsequent role switching is instantaneous (0ms in-memory cache lookup).
    Returns: dict mapping (role, job_name) -> bool
    """
    try:
        from config import DEPARTMENTS
    except Exception:
        return {}

    dept = DEPARTMENTS.get(department_name, {})
    roles = dept.get("roles", [])
    queries = dept.get("queries", {})

    if not roles or not queries:
        return {}

    sql_parts = []
    for role in roles:
        escaped_role = role.replace("'", "''")
        for job_name, job_meta in queries.items():
            escaped_job = job_name.replace("'", "''")
            table = job_meta.get("table", "").replace("'", "''")
            priv = job_meta.get("privilege", "").replace("'", "''")
            cols = job_meta.get("columns", [])

            if cols:
                col_clauses = []
                for c in cols:
                    escaped_col = str(c).replace("'", "''")
                    col_clauses.append(f"has_column_privilege('{escaped_role}', '{table}', '{escaped_col}', '{priv}')")
                expr = f"({' AND '.join(col_clauses)})"
            else:
                expr = f"has_table_privilege('{escaped_role}', '{table}', '{priv}')"
            sql_parts.append(f"SELECT '{escaped_role}' AS role, '{escaped_job}' AS job, {expr} AS allowed")

    full_sql = " UNION ALL ".join(sql_parts)

    try:
        with _checkout() as conn:
            if conn is None:
                return {}
            with conn.cursor() as cur:
                cur.execute(full_sql)
                rows = cur.fetchall()
                return {(r[0], r[1]): bool(r[2]) for r in rows}
    except Exception:
        return {}

KNOWN_TRIGGER_CODES = [
    "ACCOUNT_FROZEN_BLOCKED",
    "FRAUD_CHECK_FAILED",
    "INSUFFICIENT_FUNDS",
    "KYC_CHECK_FAILED",
    "LOAN_ACCOUNT_COMPROMISED",
    "LOAN_KYC_FAILED",
    "LOAN_STACKING_BLOCKED",
    "TRANSACTION_SELF_BLOCKED",
    "WORKFLOW_BACKWARD_TRANSITION",
    "WORKFLOW_STAGE_SKIPPED",
    "WORKFLOW_TERMINAL_STATE",
    "WORKFLOW_UNAUTHORIZED_ACTOR"
]

def parse_trigger_error(error_str):
    """Extracts trigger error code and clean description from PostgreSQL exception message."""
    if not error_str:
        return None, ""

    first_line = error_str.split("\n")[0]
    if "CONTEXT:" in first_line:
        first_line = first_line.split("CONTEXT:")[0]
    first_line = first_line.strip()

    detected_code = None
    for code in KNOWN_TRIGGER_CODES:
        if code in first_line:
            detected_code = code
            break

    clean_msg = first_line
    if detected_code and f"{detected_code}:" in first_line:
        clean_msg = first_line.split(f"{detected_code}:", 1)[1].strip()

    return detected_code, clean_msg

def get_snapshot_for_action(job_key, params):
    """Snapshots relevant accounts or loan records before and after execution for diff viewing."""
    if not params:
        return {}

    snapshot = {}
    try:
        with _checkout() as conn:
            if conn is None:
                return {}
            with conn.cursor() as cur:
                # 1. Transaction creation -> snapshot sender and receiver accounts
                if "Transaction" in job_key and "INSERT" in job_key and len(params) >= 2:
                    sender_id, receiver_id = params[0], params[1]
                    cur.execute("""
                        SELECT account_id, profile_id, balance, account_status::text, account_type
                        FROM customer_accounts
                        WHERE account_id IN (%s, %s);
                    """, (sender_id, receiver_id))
                    rows = cur.fetchall()
                    if rows:
                        snapshot["accounts"] = {
                            r[0]: {"account_id": r[0], "profile_id": r[1], "balance": float(r[2]), "status": r[3], "type": r[4]}
                            for r in rows
                        }

                # 2. Account balance or status update -> snapshot single account
                elif "Account" in job_key and ("UPDATE" in job_key or "Freeze" in job_key or "Close" in job_key):
                    # account_id is typically the last param
                    acc_id = params[-1]
                    cur.execute("""
                        SELECT account_id, profile_id, balance, account_status::text, account_type
                        FROM customer_accounts
                        WHERE account_id = %s;
                    """, (acc_id,))
                    row = cur.fetchone()
                    if row:
                        snapshot["accounts"] = {
                            row[0]: {"account_id": row[0], "profile_id": row[1], "balance": float(row[2]), "status": row[3], "type": row[4]}
                        }

                # 3. Loan status update or creation
                elif "Loan" in job_key:
                    # INSERT params are (profile_id, amount); UPDATE params are (status, profile_id)
                    profile_id = params[0] if "INSERT" in job_key else params[-1]
                    cur.execute("""
                        SELECT loan_id, profile_id, requested_amount, approval_status::text
                        FROM loan_applications
                        WHERE profile_id = %s
                        ORDER BY loan_id DESC LIMIT 1;
                    """, (profile_id,))
                    row = cur.fetchone()
                    if row:
                        snapshot["loans"] = {
                            row[0]: {"loan_id": row[0], "profile_id": row[1], "requested_amount": float(row[2]), "approval_status": row[3]}
                        }
    except Exception:
        pass
    return snapshot

def execute_action_with_snapshot(role_name, job_key, query, params=None):
    """
    Executes a query as a role while capturing before/after state snapshots
    and parsing trigger exception codes for the Live Trace UI.
    """
    # Capture PRE-execution snapshot
    before_snap = get_snapshot_for_action(job_key, params)

    # Execute query
    result = execute_query_as_role(role_name, query, params)

    # Parse errors if any
    error_code = None
    clean_msg = result.get("message", "")
    if result["status"] == "error":
        error_code, clean_msg = parse_trigger_error(result.get("message", ""))
    elif result["status"] == "denied":
        error_code = "RBAC_DENIED"

    # Capture POST-execution snapshot if successful
    if result["status"] == "success":
        after_snap = get_snapshot_for_action(job_key, params)
    else:
        after_snap = before_snap

    return {
        "status": result["status"],
        "data": result.get("data"),
        "columns": result.get("columns"),
        "message": result.get("message"),
        "error_code": error_code,
        "clean_message": clean_msg,
        "before_snapshot": before_snap,
        "after_snapshot": after_snap
    }
