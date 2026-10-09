import streamlit as st
import html
import pandas as pd
from db_connection import (
    execute_action_with_snapshot, 
    check_table_permission, 
    get_all_permissions_cache,
    is_db_connected
)
from visualizer import (
    render_live_trace, 
    render_diff_viewer,
    render_graphviz_flowchart, 
    render_eca_trigger_dissector,
    TRIGGER_SOURCE_CODES
)
from config import DEPARTMENTS
from ai_engine.exam_lab import render_exam_lab_tab
from frontend_utils import (
    load_css, 
    render_brand_header, 
    render_sidebar_role_card, 
    render_sidebar_bio,
    render_defense_depth_grid
)

ACRONYMS = {"it", "csr", "dba", "hipaa", "aml", "ta", "bi", "rbac", "kyc", "vit", "cse"}
st.set_page_config(page_title="RBAC & Trigger Visualizer", layout="wide")

# =============================================================================
# LOAD SEPARATED FRONTEND STYLESHEET
# =============================================================================
load_css()


def format_role_name(role_key):
    words = role_key.split('_') 
    formatted_words = [word.upper() if word.lower() in ACRONYMS else word.title() for word in words]
    return " ".join(formatted_words)

# Role descriptions for intuitive UI
ROLE_DESCRIPTIONS = {
    "bank_teller": "Counter cashier: creates accounts and processes cash deposits/withdrawals.",
    "branch_manager": "Branch oversight: approves loans, updates alert statuses, freezes/closes accounts.",
    "fraud_analyst": "Financial intelligence: inspects suspicious activity and logs fraud alerts.",
    "senior_underwriter": "Credit risk assessment: advances loan applications to UNDERWRITE stage.",
    "it_security_admin": "Security & compliance: strictly read-only inspection of the audit trail.",
    "internal_auditor": "Independent oversight: full read-only visibility across all core banking tables.",
    "retail_customer": "Self-service customer: initiates peer transfers and daily transactions.",
    "loan_officer": "Loan intake: captures client requirements and coordinates credit files.",
    "csr": "Customer service: resolves account inquiries with read-only account data."
}

# =============================================================================
# BRANDING HEADER
# =============================================================================
db_online = is_db_connected()
render_brand_header(is_connected=db_online)
if not db_online:
    st.info(
        "**Offline simulator mode.** PostgreSQL database connection is offline. "
        "You can explore all architectural features (**Trigger Code Viewer**, **ECA Dissector**, "
        "**Flowcharts**, and **AI Exam Lab**) without a database. "
        "To execute live SQL transactions against Neon, configure your credentials in `.streamlit/secrets.toml`."
    )

# -----------------------------------------------------------------------------
# SIDEBAR CONTROLS
# -----------------------------------------------------------------------------
st.sidebar.header("Active Security")
selected_dept = st.sidebar.selectbox("Department", list(DEPARTMENTS.keys()))
active_role = st.sidebar.radio(
    "Simulated PostgreSQL Role", 
    DEPARTMENTS[selected_dept]["roles"], 
    format_func=format_role_name
)

role_desc = ROLE_DESCRIPTIONS.get(active_role, "Authenticated database user role.")
render_sidebar_role_card(format_role_name(active_role), role_desc)

with st.sidebar.expander("Demo Test Cheatsheet", expanded=False):
    st.markdown("""
    **Pre-seeded Demo Accounts:**
    - **101 (Alice Walker, profile 1)**: ACTIVE, KYC approved, balance 15,000.00. Holds the seeded loan (35,000.00) in **SUBMITTED**
    - **102 (Bob Vance, profile 2)**: ACTIVE, KYC approved, balance 8,500.00
    - **103 (Charlie Pending, profile 3)**: ACTIVE, KYC **PENDING**, balance 2,500.00
    - **104 (David Miller, profile 4)**: **FROZEN**, balance 12,000.00
    - **105 (Eve Risk, profile 5)**: ACTIVE, KYC approved, balance 400.00, with an **OPEN** fraud alert
    
    **Trigger Test Scenarios:**
    - **Pass Transfer**: 101 -> 102 ($500) as `retail_customer`
    - **Block KYC**: 103 -> 102 ($200) as `retail_customer`
    - **Block Frozen**: 104 -> 102 ($200) as `retail_customer`
    - **Block Fraud**: 105 -> 102 ($200) as `retail_customer`
    - **Block Loan Stacking**: Profile 1 ($25,000), which already has a SUBMITTED loan
    - **Loan Workflow**: The seeded loan for profile 1 as `senior_underwriter` -> `UNDERWRITE`, then `branch_manager` -> `APPROVED`
    """)

# -----------------------------------------------------------------------------
# SIDEBAR DEVELOPER BIO & TEAM PROFILE
# -----------------------------------------------------------------------------
render_sidebar_bio()

with st.sidebar.expander("Project Architecture & Tech Stack", expanded=False):
    st.markdown("""
    **Core Architecture Contributions:**
    - **Schema Design:** 6 interconnected core banking tables on Neon Serverless PostgreSQL.
    - **RBAC Matrix:** Surgical table & column-level GRANT privileges across 6 roles.
    - **Trigger Engine:** 4 PL/pgSQL triggers with deterministic exception signatures.
    - **Observability:** Live Trace & Before/After State Diff Viewer.

    **Core Tech Stack:**
    `PostgreSQL 16` &bull; `Neon Serverless` &bull; `PL/pgSQL` &bull; `Python 3.13` &bull; `Streamlit` &bull; `Graphviz` &bull; `psycopg2`
    """)

# =============================================================================
# TOP NAVIGATION TABS (MULTI-PAGE FINTECH EXPERIENCE)
# =============================================================================
main_tabs = st.tabs([
    "Run an operation",
    "Access matrix",
    "Trigger source",
    "How triggers work",
    "Execution flow",
    "Exam lab"
])

tab_simulator, tab_access, tab_trigger_code, tab_eca_theory, tab_flowchart, tab_exam_lab = main_tabs

# -----------------------------------------------------------------------------
# REFERENCE TABLES (facts taken from sql/triggers/*.sql and sql/schema.sql)
# -----------------------------------------------------------------------------
TRIGGER_OVERVIEW = [
    ("process_transaction", "BEFORE INSERT", "daily_transactions",
     "Self-transfer, sender and receiver KYC, account status (frozen or closed), open fraud alerts, and sender balance. Then it updates both balances.",
     ["TRANSACTION_SELF_BLOCKED", "KYC_CHECK_FAILED", "ACCOUNT_FROZEN_BLOCKED", "FRAUD_CHECK_FAILED", "INSUFFICIENT_FUNDS"]),
    ("check_loan_eligibility", "BEFORE INSERT", "loan_applications",
     "Applicant KYC, one active application at a time, and frozen or closed accounts. A new application starts as SUBMITTED.",
     ["LOAN_KYC_FAILED", "LOAN_STACKING_BLOCKED", "LOAN_ACCOUNT_COMPROMISED"]),
    ("enforce_loan_workflow", "BEFORE UPDATE", "loan_applications",
     "Stage order (SUBMITTED, then UNDERWRITE, then APPROVED or REJECTED), no moving backwards, final states locked, and role checks for UNDERWRITE and APPROVED.",
     ["WORKFLOW_STAGE_SKIPPED", "WORKFLOW_BACKWARD_TRANSITION", "WORKFLOW_TERMINAL_STATE", "WORKFLOW_UNAUTHORIZED_ACTOR"]),
    ("log_audit_event", "AFTER UPDATE", "customer_accounts, loan_applications, fraud_alerts",
     "Records the old and new values in audit_log. It never blocks a change.",
     []),
]

def build_trigger_table_html(rows):
    head = "<tr><th>Trigger</th><th>Runs</th><th>On table</th><th>What it checks</th><th>Error codes</th></tr>"
    body = []
    for name, when, table, checks, codes in rows:
        code_html = " ".join(f"<code>{html.escape(c)}</code>" for c in codes) if codes else "None"
        body.append(
            f"<tr><td><code>{html.escape(name)}</code></td><td>{html.escape(when)}</td>"
            f"<td>{html.escape(table)}</td><td>{html.escape(checks)}</td>"
            f"<td class=\"tt-codes\">{code_html}</td></tr>"
        )
    return ('<div class="table-scroll"><table class="trigger-table"><thead>' + head +
            '</thead><tbody>' + "".join(body) + '</tbody></table></div>')

def build_access_matrix_html(queries, roles, permissions):
    head_cells = "".join(f'<th scope="col">{html.escape(format_role_name(r))}</th>' for r in roles)
    rows = []
    for job, meta in queries.items():
        cells = []
        for r in roles:
            allowed = permissions.get((r, job))
            if allowed is None:
                cells.append('<td class="am-unknown">Not loaded</td>')
            elif allowed:
                cells.append('<td class="am-yes">Allowed</td>')
            else:
                cells.append('<td class="am-no">Denied</td>')
        detail = f"{meta.get('table', '')}, {meta.get('privilege', '')}"
        rows.append(f'<tr><th scope="row">{html.escape(job)}<span class="am-table">{html.escape(detail)}</span></th>' + "".join(cells) + '</tr>')
    return ('<div class="table-scroll"><table class="access-table"><thead><tr><th scope="col">Operation</th>' +
            head_cells + '</tr></thead><tbody>' + "".join(rows) + '</tbody></table></div>')

# Track active_role transitions to immediately invalidate stale results and synchronize widgets
if st.session_state.get("previous_active_role") != active_role:
    st.session_state["previous_active_role"] = active_role
    st.session_state["last_result"] = None

# Initialize session state for cross-tab inspection
if "last_result" not in st.session_state:
    st.session_state["last_result"] = None
if "last_job_key" not in st.session_state:
    st.session_state["last_job_key"] = "Create New Transaction (INSERT)"
if "current_selected_operation" not in st.session_state:
    st.session_state["current_selected_operation"] = "Create New Transaction (INSERT)"
if "last_inputs" not in st.session_state:
    st.session_state["last_inputs"] = (101, 102, 500.0, "INTERNAL")

QUERIES = DEPARTMENTS[selected_dept]["queries"]
all_permissions = get_all_permissions_cache(selected_dept)
job_display_map = {}
for job_name, job_details in QUERIES.items():
    has_access = all_permissions.get((active_role, job_name))
    if has_access is None:
        has_access = check_table_permission(
            active_role, 
            job_details["table"], 
            job_details["privilege"], 
            tuple(job_details.get("columns", []))
        )
    job_display_map[job_name] = job_name if has_access else f"{job_name}  (not permitted for this role)"

# -----------------------------------------------------------------------------
# TAB 1: BANKING OPERATIONS & SIMULATOR
# -----------------------------------------------------------------------------
with tab_simulator:
    st.markdown(
        '<header class="section-head"><p class="eyebrow">Explore by yourself</p>'
        '<h2>Run a database operation</h2>'
        '<p class="section-lede">Pick an operation, fill in its inputs, and run it as the selected role. '
        'The result shows which check decided the outcome.</p></header>',
        unsafe_allow_html=True,
    )

    st.markdown(f"""
    <dl class="context-strip">
        <div><dt>Active role</dt><dd>{format_role_name(active_role)}</dd></div>
        <div><dt>Tables in schema</dt><dd>6 core tables</dd></div>
        <div><dt>Trigger functions</dt><dd>4 PL/pgSQL functions</dd></div>
        <div><dt>Where rules run</dt><dd>Inside PostgreSQL</dd></div>
    </dl>
    """, unsafe_allow_html=True)

    selected_job_key = st.selectbox(
        "Choose an operation to run", 
        options=list(QUERIES.keys()), 
        index=3 if len(QUERIES) > 3 else 0, 
        placeholder="-- Select a database action to test --", 
        format_func=lambda job: job_display_map[job],
        key=f"tab1_sim_selector_{active_role}"
    )

    if selected_job_key is not None:
        st.session_state["current_selected_operation"] = selected_job_key
        if st.session_state.get("last_result") is None:
            st.session_state["last_job_key"] = selected_job_key

        selected_job_details = QUERIES[selected_job_key]
        final_access_check = all_permissions.get((active_role, selected_job_key))
        if final_access_check is None:
            final_access_check = check_table_permission(
                active_role, 
                selected_job_details["table"], 
                selected_job_details["privilege"], 
                tuple(selected_job_details.get("columns", []))
            )

        if final_access_check:
            st.success(f"**Permission granted.** Role `{format_role_name(active_role)}` can {selected_job_details['privilege']} `{selected_job_details['table']}`.")    
            
            user_inputs = []
            if "inputs" in selected_job_details: 
                input_cols = st.columns(min(len(selected_job_details["inputs"]), 3) or 1)
                for i, inp in enumerate(selected_job_details.get("inputs", [])):
                    col = input_cols[i % len(input_cols)]
                    with col:
                        if inp["type"] == "text":
                            val = st.text_input(inp["label"], key=f"sim_inp_{i}")
                            user_inputs.append(val)
                        elif inp["type"] == "number":
                            default_val = 101 if "Sender" in inp["label"] or "Account ID" in inp["label"] else (102 if "Receiver" in inp["label"] else (500 if "Amount" in inp["label"] else 101))
                            val = st.number_input(inp["label"], step=1, value=default_val, key=f"sim_inp_{i}")
                            user_inputs.append(val)
                        elif inp["type"] == "selectbox":
                            val = st.selectbox(inp["label"], inp["options"], key=f"sim_inp_{i}")
                            user_inputs.append(val)

            col_btn1, col_btn2 = st.columns([1, 4])
            with col_btn1:
                run_clicked = st.button("Run Operation", type="primary", width="stretch")
            with col_btn2:
                show_query = st.checkbox("Show Raw SQL Query", value=False)
                if show_query:
                    st.code(selected_job_details["sql"], language="sql")

            if run_clicked:
                with st.spinner("Dispatching query to PostgreSQL on Neon..."):
                    result = execute_action_with_snapshot(
                        active_role, 
                        selected_job_key, 
                        selected_job_details["sql"], 
                        tuple(user_inputs)
                    )
                    # Persist in session state for Tabs 2, 3, 4
                    st.session_state["last_result"] = result
                    st.session_state["last_job_key"] = selected_job_key
                    st.session_state["current_selected_operation"] = selected_job_key
                    st.session_state["last_inputs"] = tuple(user_inputs)

                    st.markdown("---")

                    # Live Trace & Diff Viewer
                    render_live_trace(selected_job_key, result)
                    if result.get("before_snapshot") or result.get("after_snapshot"):
                        render_diff_viewer(
                            result.get("before_snapshot"), 
                            result.get("after_snapshot"), 
                            selected_job_key, 
                            result
                        )

                    # Database Output Table
                    st.markdown("### Database Output & Response")
                    if result["status"] == "success":
                        if selected_job_details["privilege"] == "SELECT":
                            st.success("Query ran successfully.")
                        else:
                            st.success("Change committed to PostgreSQL.")
                        
                        if result.get("data") is not None:
                            if len(result["data"]) == 0:
                                st.info("No records found in this table yet.")
                                df = pd.DataFrame(columns=result.get("columns", []))
                                st.dataframe(df, width="stretch")
                            else:
                                df = pd.DataFrame(result["data"], columns=result.get("columns", []))
                                st.dataframe(df, width="stretch")

                    elif result["status"] == "denied":
                        st.error("Blocked by permissions")
                        st.error(result.get("message", "Insufficient privileges."))

                    else:
                        st.error(f"Execution Blocked by Trigger: {result.get('clean_message', 'Trigger exception raised.')}")
                        with st.expander("Show Full PostgreSQL Engine Exception"):
                            st.code(result.get("message", ""), language="text")

        else:
            st.error(f"**Blocked by permissions.** Role `{format_role_name(active_role)}` does not have {selected_job_details['privilege']} on `{selected_job_details['table']}`, so PostgreSQL rejected the statement before reading any rows.")
            fake_denied = {
                "status": "denied",
                "message": f"Role {active_role} lacks {selected_job_details['privilege']} on {selected_job_details['table']}."
            }
            render_live_trace(selected_job_key, fake_denied)


def get_role_context_hint(role, trigger_key, operation_name):
    if trigger_key == "process_transaction":
        if role == "retail_customer":
            return "As a Customer sending money, PostgreSQL evaluates your transfer against these 4 firewalls in real time. If any check fails, your balance is never touched and the transfer aborts."
        elif role == "branch_manager":
            return "As a Branch Manager, when you freeze an account, the database's ACCOUNT_FROZEN_BLOCKED rule immediately halts all money movement out of that account."
        elif role == "fraud_analyst":
            return "As a Fraud Analyst, logging a fraud alert directly activates the FRAUD_CHECK_FAILED firewall, automatically blocking transactions without waiting for manual intervention."
        elif role in ("bank_teller", "csr"):
            return f"As a {format_role_name(role)}, these deterministic error signatures explain to you exactly why a customer's transaction was rejected by the database."
        else:
            return f"Active role {format_role_name(role)} is protected by these 4 database kernel firewalls to prevent fraud and maintain solvency."
    elif trigger_key == "check_loan_eligibility":
        if role in ("loan_officer", "bank_teller"):
            return "As loan intake staff, the database automatically stops you from submitting duplicate active loans (anti-stacking) or loans for customers with frozen accounts."
        else:
            return f"Active role {format_role_name(role)}: Enforces loan qualification, verified KYC, and anti-stacking rules before accepting new loan applications."
    elif trigger_key == "enforce_loan_workflow":
        if role == "senior_underwriter":
            return "As Senior Underwriter, you have authority to advance loans to UNDERWRITE, but the database blocks you from granting final approval or skipping stages."
        elif role == "branch_manager":
            return "As Branch Manager, you hold exclusive authority to APPROVE loans. Anyone else attempting approval is blocked with WORKFLOW_UNAUTHORIZED_ACTOR."
        else:
            return f"Active role {format_role_name(role)} lacks underwriting privileges; database workflow guards prevent unauthorized loan state changes."
    elif trigger_key == "log_audit_event":
        return f"Whenever {format_role_name(role)} modifies accounts or loans, this silent trigger automatically records the old value, new value, and your role stamp into the immutable audit_log."
    return f"Active role {format_role_name(role)} executes this operation under PostgreSQL RBAC authorization."


# -----------------------------------------------------------------------------
# TAB 2 (TAB C): TRIGGER CODE FOR SELECTED OPERATION
# -----------------------------------------------------------------------------
with tab_trigger_code:
    all_job_keys = list(QUERIES.keys())
    current_sim_job = st.session_state.get("current_selected_operation", all_job_keys[3] if len(all_job_keys) > 3 else all_job_keys[0])
    default_tab2_idx = all_job_keys.index(current_sim_job) if current_sim_job in all_job_keys else 0

    st.markdown("### In-Action Trigger Source Code")
    st.markdown(f"Inspect the compiled PL/pgSQL procedural trigger backing database operations for active role `{format_role_name(active_role)}`.")

    t2_col1, t2_col2 = st.columns([3, 1])
    with t2_col1:
        inspect_job = st.selectbox(
            "Select a Banking Operation to Inspect Its In-Engine Trigger:",
            options=all_job_keys,
            index=default_tab2_idx,
            format_func=lambda job: job_display_map.get(job, job),
            key=f"tab2_inspect_selector_{active_role}"
        )
    with t2_col2:
        st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
        inspect_has_access = all_permissions.get((active_role, inspect_job), False)
        if inspect_job == st.session_state.get("current_selected_operation"):
            sync_badge = "🔄 Synced with Simulator\n"
            sync_class = "is-synced"
        else:
            sync_badge = "Free Inspection"
            sync_class = "is-free"

        role_badge = "<span class='rbac-ok'>Authorized</span>" if inspect_has_access else "<span class='rbac-deny'>RBAC Denied</span>"
        st.markdown(f"""
        <div class='sync-pill {sync_class}'>
            {sync_badge} &bull; {role_badge}
        </div>
        """, unsafe_allow_html=True)

    OPERATION_TRIGGER_MAP = {
        "Create New Transaction (INSERT)": {
            "trigger_key": "process_transaction",
            "title": "process_transaction()",
            "timing": "BEFORE INSERT ON daily_transactions (FOR EACH ROW)",
            "summary": "Enforces a sequential 4-tier financial firewall: 1) Sender & receiver KYC verification, 2) Operational account status (not FROZEN or CLOSED), 3) Financial crime clearance (zero open FRAUD_ALERT), and 4) Solvency check with atomic in-engine sender debit and receiver credit.",
            "exceptions": [
                ("Identity Verification", "KYC_CHECK_FAILED", "Sender or receiver KYC profile status is not APPROVED."),
                ("Account Freeze Hold", "ACCOUNT_FROZEN_BLOCKED", "Sender or receiver account is currently FROZEN by compliance or management."),
                ("Fraud Flag Alert", "FRAUD_CHECK_FAILED", "Account has an open fraud investigation ticket on record."),
                ("Balance & Solvency", "INSUFFICIENT_FUNDS", "Sender account balance is less than the proposed transfer amount.")
            ],
            "cascades": "Cascades AFTER trigger to log_audit_event() upon atomic balance modification."
        },
        "Create New Loan (INSERT)": {
            "trigger_key": "check_loan_eligibility",
            "title": "check_loan_eligibility()",
            "timing": "BEFORE INSERT ON loan_applications (FOR EACH ROW)",
            "summary": "Verifies applicant KYC approval, blocks compromised profiles holding FROZEN/CLOSED accounts, and enforces the anti-loan-stacking rule (blocks duplicate active loans in SUBMITTED/UNDERWRITE).",
            "exceptions": [
                ("Applicant KYC", "LOAN_KYC_FAILED", "Loan applicant KYC is not APPROVED."),
                ("Anti-Loan Stacking", "LOAN_STACKING_BLOCKED", "Customer already has an active loan application under review."),
                ("Compromised Account", "LOAN_ACCOUNT_COMPROMISED", "Applicant holds at least one FROZEN or CLOSED account.")
            ],
            "cascades": "Initializes applicant status to SUBMITTED."
        },
        "Update Loan Status (UPDATE)": {
            "trigger_key": "enforce_loan_workflow",
            "title": "enforce_loan_workflow()",
            "timing": "BEFORE UPDATE ON loan_applications (FOR EACH ROW, SECURITY DEFINER)",
            "summary": "Linear workflow state machine (SUBMITTED -> UNDERWRITE -> APPROVED/REJECTED). Enforces strict role-based underwriting (Senior Underwriter & Branch Manager) and blocks backward transitions, stage skips, or mutations of terminal states.",
            "exceptions": [
                ("Stage-Skip Guard", "WORKFLOW_STAGE_SKIPPED", "Attempted to skip from SUBMITTED directly to APPROVED without underwrite review."),
                ("Reversion Prohibited", "WORKFLOW_BACKWARD_TRANSITION", "Prohibits reverting a loan backwards (e.g., UNDERWRITE to SUBMITTED)."),
                ("Unauthorized Actor", "WORKFLOW_UNAUTHORIZED_ACTOR", "Only Senior Underwriters can advance to UNDERWRITE; only Branch Managers can APPROVE."),
                ("Closed Loan Lock", "WORKFLOW_TERMINAL_STATE", "Attempted to mutate a loan that is already APPROVED or REJECTED.")
            ],
            "cascades": "Cascades AFTER trigger to log_audit_event() to record the state transition in audit_log."
        },
        "Update Account Balance (UPDATE)": {
            "trigger_key": "log_audit_event",
            "title": "log_audit_event()",
            "timing": "AFTER UPDATE ON customer_accounts (FOR EACH ROW, SECURITY DEFINER)",
            "summary": "Silent forensic event recorder executing with SECURITY DEFINER privilege elevation. Automatically logs actor role, table name, record ID, account ID, old values, and new values into the append-only audit_log.",
            "exceptions": [
                ("Append-Only Audit", "AUDIT_APPEND_ONLY", "audit_log is append-only; direct mutations and deletions are strictly revoked from all non-admin roles.")
            ],
            "cascades": "None (Terminal audit recording step)."
        },
        "Update Account Status (Freeze/Unfreeze)": {
            "trigger_key": "log_audit_event",
            "title": "log_audit_event()",
            "timing": "AFTER UPDATE ON customer_accounts (FOR EACH ROW, SECURITY DEFINER)",
            "summary": "Silent forensic audit recorder capturing administrative account status transitions (ACTIVE <-> FROZEN) and recording actor role, timestamp, and before/after states.",
            "exceptions": [
                ("Append-Only Audit", "AUDIT_APPEND_ONLY", "audit_log is append-only; direct mutations and deletions are strictly revoked from all non-admin roles.")
            ],
            "cascades": "None (Terminal audit recording step)."
        },
        "Close Customer Account (UPDATE)": {
            "trigger_key": "log_audit_event",
            "title": "log_audit_event()",
            "timing": "AFTER UPDATE ON customer_accounts (FOR EACH ROW, SECURITY DEFINER)",
            "summary": "Silent forensic audit recorder capturing final account decommission (CLOSED) in the immutable audit trail.",
            "exceptions": [
                ("Append-Only Audit", "AUDIT_APPEND_ONLY", "audit_log is append-only; direct mutations and deletions are strictly revoked from all non-admin roles.")
            ],
            "cascades": "None (Terminal audit recording step)."
        },
        "Update Fraud Status (UPDATE)": {
            "trigger_key": "log_audit_event",
            "title": "log_audit_event()",
            "timing": "AFTER UPDATE ON fraud_alerts (FOR EACH ROW, SECURITY DEFINER)",
            "summary": "Auditing trigger capturing fraud alert status updates and risk assessments into audit_log.",
            "exceptions": [],
            "cascades": "None (Terminal audit recording step)."
        }
    }

    trigger_meta = OPERATION_TRIGGER_MAP.get(inspect_job)

    if trigger_meta:
        active_trigger_key = trigger_meta["trigger_key"]
        trigger_title = trigger_meta["title"]
        trigger_timing = trigger_meta["timing"]
        trigger_summary = trigger_meta["summary"]
        trigger_exceptions = trigger_meta["exceptions"]

        # 1. Visual Summary Card
        st.markdown(f"""
        <div class="trigger-hero-card">
            <div class="trigger-hero-header">
                <div>
                    <span class="trigger-hero-label">Directly Backing Selected Operation</span>
                    <h3 class="trigger-hero-title"><code>{trigger_title}</code></h3>
                </div>
                <div style="margin-top: 6px;">
                    <span class="trigger-timing-badge">
                        {trigger_timing}
                    </span>
                </div>
            </div>
            <div class="trigger-hero-summary">
                {trigger_summary}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # 2. Role Context Banner
        role_hint = get_role_context_hint(active_role, active_trigger_key, inspect_job)
        st.markdown(f"""
        <div class="role-context-banner">
            <span class="role-context-title">
                Relevance to Active Role ({format_role_name(active_role)})
            </span>
            <div class="role-context-desc">
                {role_hint}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # 3. Rejection Firewalls Cards
        if trigger_exceptions:
            st.markdown("#### Database Rejection Firewalls (Why PostgreSQL Blocks This Action)")
            st.caption("If any of these conditions are violated, PostgreSQL immediately halts execution and triggers an automatic ACID Rollback (zero partial writes).")
            ex_cols = st.columns(len(trigger_exceptions))
            for idx, (flabel, ecode, edesc) in enumerate(trigger_exceptions):
                with ex_cols[idx]:
                    st.markdown(f"""
                    <div class="firewall-card">
                        <div class="firewall-title">{flabel}</div>
                        <div>
                            <span class="firewall-badge">
                                {ecode}
                            </span>
                        </div>
                        <div class="firewall-desc">
                            {edesc}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

        st.markdown("<div style='height: 14px;'></div>", unsafe_allow_html=True)

        # 4. Collapsible Code Drawer
        with st.expander("View Raw PL/pgSQL Kernel Source Code (Compiled in PostgreSQL)", expanded=False):
            st.markdown(f"**Function:** `{trigger_title}` &bull; **Mode:** `{trigger_timing}`")
            st.code(TRIGGER_SOURCE_CODES[active_trigger_key], language="sql")

        # 5. Interactive Testing Hint
        if active_trigger_key == "process_transaction":
            st.info("**Try it in the Simulator (Tab 1):** Select Demo Account **103** (Pending KYC) or **104** (Frozen) to watch PostgreSQL reject the transfer in real-time with these exact error codes!")
        elif active_trigger_key == "check_loan_eligibility":
            st.info("**Try it in the Simulator (Tab 1):** Submit a loan for Profile **1** (already has a SUBMITTED loan) to see the anti-stacking block, or Profile **4** (frozen account) to see the account-health block.")
        elif active_trigger_key == "enforce_loan_workflow":
            st.info("**Try it in the Simulator (Tab 1):** Switch between `senior_underwriter` and `branch_manager` to test workflow role authority and stage progression rules!")
    else:
        st.markdown(f"""
        <div class="tier1-notice-card">
            <div class="tier1-notice-header">
                <div>
                    <span class="tier1-notice-pretitle">
                        Architectural Classification: Tier-1 RBAC Governed
                    </span>
                    <h3 class="tier1-notice-title">
                        No Procedural Trigger Attached to <code>{inspect_job}</code>
                    </h3>
                </div>
                <div style="margin-top: 6px;">
                    <span class="tier1-badge">
                        DIRECT POSTGRESQL ENGINE QUERY
                    </span>
                </div>
            </div>
            <div class="tier1-notice-content">
                <b>Why doesn't this operation attach a procedural trigger?</b><br>
                In PostgreSQL and ANSI SQL relational database standards, <b>procedural triggers execute exclusively on row modification events (<code>INSERT</code>, <code>UPDATE</code>, <code>DELETE</code>)</b>.
                <ul style="margin: 8px 0 4px 0; padding-left: 20px;">
                    <li><b>Read-Only Queries (<code>SELECT</code>):</b> Executed directly by PostgreSQL's cost-based query optimizer. Access is authorized at <b>Tier 1 (RBAC Catalog)</b> via <code>GRANT SELECT</code> without incurring procedural trigger interpreter overhead.</li>
                    <li><b>Standard Schema DML:</b> Basic inserts/updates without business state machines rely on database constraints (foreign keys, uniqueness) and column-level RBAC rather than procedural trigger hooks.</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### Inspect Any of the 4 Core Banking Triggers:")
        chosen_trigger_pill = st.radio(
            "Select Core Trigger to View:",
            options=[
                "1. Transaction Firewall (process_transaction)",
                "2. Loan Eligibility Guard (check_loan_eligibility)",
                "3. Loan Workflow State Machine (enforce_loan_workflow)",
                "4. Silent Forensic Auditor (log_audit_event)"
            ],
            horizontal=True,
            label_visibility="collapsed",
            key="tab2_trigger_pill_selector"
        )
        pill_map = {
            "1. Transaction Firewall (process_transaction)": "process_transaction",
            "2. Loan Eligibility Guard (check_loan_eligibility)": "check_loan_eligibility",
            "3. Loan Workflow State Machine (enforce_loan_workflow)": "enforce_loan_workflow",
            "4. Silent Forensic Auditor (log_audit_event)": "log_audit_event"
        }
        manual_key = pill_map[chosen_trigger_pill]
        st.code(TRIGGER_SOURCE_CODES[manual_key], language="sql")

    st.markdown("---")
    with st.expander("Browse All 4 Core Banking Triggers Side-by-Side in Library", expanded=False):
        t_tab1, t_tab2, t_tab3, t_tab4 = st.tabs([
            "1. Transaction Firewall", 
            "2. Loan Eligibility", 
            "3. Loan Workflow State Machine", 
            "4. Silent Audit Logger"
        ])
        with t_tab1:
            st.markdown("**`process_transaction()`** &bull; `BEFORE INSERT ON daily_transactions`")
            st.code(TRIGGER_SOURCE_CODES["process_transaction"], language="sql")
        with t_tab2:
            st.markdown("**`check_loan_eligibility()`** &bull; `BEFORE INSERT ON loan_applications`")
            st.code(TRIGGER_SOURCE_CODES["check_loan_eligibility"], language="sql")
        with t_tab3:
            st.markdown("**`enforce_loan_workflow()`** &bull; `BEFORE UPDATE ON loan_applications (SECURITY DEFINER)`")
            st.code(TRIGGER_SOURCE_CODES["enforce_loan_workflow"], language="sql")
        with t_tab4:
            st.markdown("**`log_audit_event()`** &bull; `AFTER UPDATE ON customer_accounts, loan_applications (SECURITY DEFINER)`")
            st.code(TRIGGER_SOURCE_CODES["log_audit_event"], language="sql")


# -----------------------------------------------------------------------------
# TAB 3 (TAB A): IN-ENGINE TRIGGER THEORY & BUFFERS (ECA MODEL)
# -----------------------------------------------------------------------------
with tab_eca_theory:
    st.markdown("### The four triggers")
    st.markdown("Triggers run inside PostgreSQL. A check that fails raises its error code, which stops the statement and rolls back its changes.")
    st.markdown(build_trigger_table_html(TRIGGER_OVERVIEW), unsafe_allow_html=True)
    st.markdown("### Defense in depth")
    render_defense_depth_grid()

    all_job_keys = list(QUERIES.keys())
    current_sim_job = st.session_state.get("current_selected_operation", all_job_keys[3] if len(all_job_keys) > 3 else all_job_keys[0])
    default_tab3_idx = all_job_keys.index(current_sim_job) if current_sim_job in all_job_keys else 0

    st.markdown("### Inspect one operation: triggers and memory buffers")

    t3_col1, t3_col2 = st.columns([3, 1])
    with t3_col1:
        dissect_job = st.selectbox(
            "Select Banking Operation to Dissect ECA Model & Memory Buffers:",
            options=all_job_keys,
            index=default_tab3_idx,
            format_func=lambda job: job_display_map.get(job, job),
            key=f"tab3_dissect_selector_{active_role}"
        )
    with t3_col2:
        st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
        dissect_has_access = all_permissions.get((active_role, dissect_job), False)
        if dissect_job == st.session_state.get("current_selected_operation"):
            sync_badge = "🔄 Synced with Simulator"
            sync_class = "is-synced"
        else:
            sync_badge = "Free Inspection"
            sync_class = "is-free"

        role_badge = "<span class='rbac-ok'>Authorized</span>" if dissect_has_access else "<span class='rbac-deny'>RBAC Denied</span>"
        st.markdown(f"""
        <div class='sync-pill {sync_class}'>
            {sync_badge} &bull; {role_badge}
        </div>
        """, unsafe_allow_html=True)

    dissect_has_access = all_permissions.get((active_role, dissect_job), False)
    inspect_inputs = st.session_state.get("last_inputs") if st.session_state.get("last_job_key") == dissect_job else None
    inspect_result = st.session_state.get("last_result") if st.session_state.get("last_job_key") == dissect_job else None

    render_eca_trigger_dissector(
        dissect_job, 
        inspect_inputs, 
        inspect_result, 
        active_role=active_role, 
        has_access=dissect_has_access
    )


# -----------------------------------------------------------------------------
# TAB 4 (TAB B): ROLE-SPECIFIC EXECUTION FLOWCHART
# -----------------------------------------------------------------------------
with tab_flowchart:
    all_job_keys = list(QUERIES.keys())
    current_sim_job = st.session_state.get("current_selected_operation", all_job_keys[3] if len(all_job_keys) > 3 else all_job_keys[0])
    default_tab4_idx = all_job_keys.index(current_sim_job) if current_sim_job in all_job_keys else 0

    st.markdown("### Role-Specific PostgreSQL Execution Flowchart")

    t4_col1, t4_col2 = st.columns([3, 1])
    with t4_col1:
        flow_job = st.selectbox(
            "Select Banking Operation for Flowchart Execution Path:",
            options=all_job_keys,
            index=default_tab4_idx,
            format_func=lambda job: job_display_map.get(job, job),
            key=f"tab4_flow_selector_{active_role}"
        )
    with t4_col2:
        st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
        flow_has_access = all_permissions.get((active_role, flow_job), False)
        if flow_job == st.session_state.get("current_selected_operation"):
            sync_badge = "🔄 Synced with Simulator"
            sync_class = "is-synced"
        else:
            sync_badge = "Free Inspection"
            sync_class = "is-free"

        role_badge = "<span class='rbac-ok'>Authorized</span>" if flow_has_access else "<span class='rbac-deny'>RBAC Denied</span>"
        st.markdown(f"""
        <div class='sync-pill {sync_class}'>
            {sync_badge} &bull; {role_badge}
        </div>
        """, unsafe_allow_html=True)

    if not flow_has_access:
        current_status = "denied"
    else:
        inspect_result = st.session_state.get("last_result") if st.session_state.get("last_job_key") == flow_job else None
        current_status = inspect_result.get("status", "success") if inspect_result else "success"

    st.markdown(f"Vector SVG compiled natively by Streamlit Graphviz in a compact Left-to-Right layout. Demonstrates how PostgreSQL routes requests for active role `{format_role_name(active_role)}` through the RBAC System Catalog, uncommitted memory buffers, trigger interception, and atomic commits/rollbacks.")

    # Compact centered container
    flow_col1, flow_col2, flow_col3 = st.columns([1, 10, 1])
    with flow_col2:
        render_graphviz_flowchart(active_role, flow_job, current_status)

    st.markdown("---")
    st.markdown("#### How PostgreSQL Executes This Operation (3-Tier Defense-in-Depth)")


# -----------------------------------------------------------------------------
# TAB 5: AI-POWERED PRACTICE LAB & EXAM EVALUATOR
# -----------------------------------------------------------------------------
with tab_access:
    st.markdown("### Access matrix")
    st.markdown("Each cell is read from the connected PostgreSQL database with `has_table_privilege` or `has_column_privilege`, so it shows the grants that are actually in place.")
    if all_permissions:
        st.markdown(build_access_matrix_html(QUERIES, DEPARTMENTS[selected_dept]["roles"], all_permissions), unsafe_allow_html=True)
    else:
        st.info("Connect to PostgreSQL to load the grid. Without a connection there are no grants to read.")

with tab_exam_lab:
    render_exam_lab_tab(active_role=active_role)

st.markdown('<p class="site-footer">Six core tables, four PL/pgSQL trigger functions. Schema and triggers live in the sql/ folder.</p>', unsafe_allow_html=True)
