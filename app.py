import streamlit as st
import pandas as pd
from db_connection import execute_action_with_snapshot, check_table_permission, get_all_permissions_cache
from visualizer import (
    render_live_trace, 
    render_diff_viewer,
    render_graphviz_flowchart, 
    render_eca_trigger_dissector,
    TRIGGER_SOURCE_CODES
)
from config import DEPARTMENTS
from ai_engine.exam_lab import render_exam_lab_tab

ACRONYMS = {"it", "csr", "dba", "hipaa", "aml", "ta", "bi", "rbac", "kyc", "vit", "cse"}
st.set_page_config(page_title="RBAC & Trigger Visualizer", layout="wide")

# =============================================================================
# MODERN FINTECH DESIGN SYSTEM (CSS)
# =============================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Poppins:wght@500;600;700;800&display=swap');
    
    html, body, [class*="css"], .stMarkdown p { font-family: 'Inter', sans-serif !important; }
    h1, h2, h3, h4 { font-family: 'Poppins', sans-serif !important; }

    /* Main Branding Header */
    .brand-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.95) 100%);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 14px;
        padding: 20px 24px;
        margin-bottom: 20px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
    }
    .brand-title {
        background: linear-gradient(135deg, #38BDF8 0%, #818CF8 50%, #C084FC 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
        font-size: 2rem !important;
        letter-spacing: -0.5px;
        margin-bottom: 4px;
    }
    .brand-subtitle {
        color: #94A3B8 !important;
        font-size: 13px !important;
        font-weight: 500;
    }

    /* KPI Metric Cards */
    .kpi-card {
        background: #111827;
        border: 1px solid #1F2937;
        border-radius: 10px;
        padding: 12px 16px;
        transition: all 0.2s ease;
    }
    .kpi-card:hover {
        border-color: #38BDF8;
        transform: translateY(-2px);
    }
    .kpi-title {
        font-size: 11px;
        color: #64748B;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .kpi-value {
        font-size: 15px;
        color: #F8FAFC;
        font-weight: 700;
        margin-top: 4px;
    }

    /* Modern Primary Action Button */
    button[kind="primary"] {
        background: linear-gradient(90deg, #0284C7 0%, #2563EB 100%) !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(2, 132, 199, 0.4) !important;
        transition: all 0.3s ease !important;
        border-radius: 8px !important;
        padding: 0.5rem 1.5rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.5px !important;
    }
    button[kind="primary"]:hover {
        box-shadow: 0 6px 20px rgba(2, 132, 199, 0.6) !important;
        transform: translateY(-1px) !important;
    }

    /* Bio Card */
    .bio-container {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
        border: 1px solid #3730a3;
        border-radius: 16px;
        padding: 28px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
    }
    .bio-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 12px;
    }
    .social-btn {
        display: inline-flex;
        align-items: center;
        padding: 10px 18px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        font-size: 13px;
        transition: all 0.2s ease;
        margin-right: 10px;
    }
</style>
""", unsafe_allow_html=True)

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
st.markdown("""
<div class="brand-container">
    <div>
        <div class="brand-title">Database RBAC Simulator & Trigger Visualizer</div>
    </div>
    <div>
        <span style="background: rgba(16, 185, 129, 0.15); border: 1px solid #10b981; color: #10b981; padding: 6px 14px; border-radius: 9999px; font-size: 12px; font-weight: 700; letter-spacing: 0.5px;">
            POSTGRESQL ONLINE (SSL)
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

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
st.sidebar.markdown(f"""
<div style="background: #1e293b; border: 1px solid #334155; border-radius: 8px; padding: 12px 14px; margin-top: 10px; margin-bottom: 12px;">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
        <span style="color: #38bdf8; font-weight: 700; font-size: 13px;">{format_role_name(active_role)}</span>
        <span style="background: rgba(56, 189, 248, 0.15); color: #38bdf8; padding: 2px 8px; border-radius: 9999px; font-size: 10px; font-weight: 700;">ACTIVE</span>
    </div>
    <div style="color: #94a3b8; font-size: 12px; line-height: 1.4;">{role_desc}</div>
</div>
""", unsafe_allow_html=True)

with st.sidebar.expander("Demo Test Cheatsheet", expanded=False):
    st.markdown("""
    **Pre-seeded Demo Accounts:**
    - **101 (Alice Smith)**: Active, KYC Approved ($10,000)
    - **102 (Bob Jones)**: Active, KYC Approved ($5,000)
    - **103 (Charlie)**: Active, KYC **PENDING** ($3,000)
    - **104 (Diana)**: **FROZEN** Account ($7,500)
    - **105 (Edward)**: Active, with **FRAUD ALERT** ($4,200)
    - **106 (Fiona)**: Active, Loan already in **SUBMITTED**
    
    **Trigger Test Scenarios:**
    - **Pass Transfer**: 101 -> 102 ($500) as `retail_customer`
    - **Block KYC**: 103 -> 102 ($200) as `retail_customer`
    - **Block Frozen**: 104 -> 102 ($200) as `retail_customer`
    - **Block Fraud**: 105 -> 102 ($200) as `retail_customer`
    - **Block Loan Stacking**: Profile 106 ($25,000)
    - **Loan Workflow**: Profile 106 as `senior_underwriter` -> `UNDERWRITE`, then `branch_manager` -> `APPROVED`
    """)

# -----------------------------------------------------------------------------
# SIDEBAR DEVELOPER BIO & TEAM PROFILE
# -----------------------------------------------------------------------------
st.sidebar.markdown("---")
st.sidebar.markdown("### Developer & Team Profile")
st.sidebar.markdown("""
<div style="background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); border: 1px solid #3730a3; border-radius: 12px; padding: 14px; margin-bottom: 12px;">
    <div style="display: inline-block; padding: 2px 8px; border-radius: 9999px; font-size: 10px; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase; background: rgba(56, 189, 248, 0.2); color: #38bdf8; border: 1px solid #0284c7; margin-bottom: 8px;">
        DBMS PROJECT
    </div>
    <div style="color: #f8fafc; font-size: 16px; font-weight: 800;">M. Sakthi Sundar</div>
    <div style="color: #a5b4fc; font-size: 12px; font-weight: 600; margin-top: 2px;">Reg No: 25BCE1244 &bull; Team MICHAEL</div>
    <div style="color: #94a3b8; font-size: 12px;">B.Tech CSE &bull; <b>VIT Chennai</b></div>
    <div style="margin-top: 8px; padding-top: 8px; border-top: 1px solid rgba(255, 255, 255, 0.1); color: #cbd5e1; font-size: 11px;">
        Project Guide: <b style="color: #f8fafc;">Dr. Swaminathan A</b> <span style="color: #38bdf8;"></span>
    </div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<div style="display: flex; gap: 8px; margin-bottom: 8px;">
    <a href="https://github.com/Sakthi-Sundar-M" target="_blank" style="flex: 1; display: inline-flex; align-items: center; justify-content: center; background: #24292e; color: #ffffff; padding: 8px 6px; border-radius: 6px; text-decoration: none; font-size: 11px; font-weight: 600; border: 1px solid #444d56;">
        <svg height="14" width="14" viewBox="0 0 16 16" fill="#ffffff" style="margin-right: 6px;">
            <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
        </svg>
        GitHub
    </a>
    <a href="https://www.linkedin.com/in/sakthi-sundar-m-34345a267" target="_blank" style="flex: 1; display: inline-flex; align-items: center; justify-content: center; background: #0a66c2; color: #ffffff; padding: 8px 6px; border-radius: 6px; text-decoration: none; font-size: 11px; font-weight: 600; border: 1px solid #004182;">
        <svg height="14" width="14" viewBox="0 0 24 24" fill="#ffffff" style="margin-right: 6px;">
            <path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 10.9v8.37H9.2V10.9H6.46M7.83 6.45a1.64 1.64 0 1 0 0 3.28 1.64 1.64 0 0 0 0-3.28z"></path>
        </svg>
        LinkedIn
    </a>
</div>
<div style="margin-bottom: 12px;">
    <a href="https://github.com/Sakthi-Sundar-M/workout" target="_blank" style="display: flex; align-items: center; justify-content: center; background: #1e293b; color: #38bdf8; padding: 7px 10px; border-radius: 6px; text-decoration: none; font-size: 11px; font-weight: 600; border: 1px solid #38bdf8;">
        <svg height="13" width="13" viewBox="0 0 16 16" fill="#38bdf8" style="margin-right: 6px;">
            <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5v-9zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8V1.5z"></path>
        </svg>
        GitHub Repository
    </a>
</div>
""", unsafe_allow_html=True)

with st.sidebar.expander("Project Architecture & Tech Stack", expanded=False):
    st.markdown("""
    **Core Architecture Contributions:**
    - **Schema Design:** 6 interconnected core banking tables on Neon Serverless PostgreSQL.
    - **RBAC Matrix:** Surgical table & column-level GRANT privileges across 6 roles.
    - **Trigger Engine:** 4 PL/pgSQL triggers with deterministic exception signatures.
    - **Observability:** Live Trace & Before/After State Diff Viewer.
    - **Test Automation:** 12-scenario automated test suite (100% pass rate).

    **Core Tech Stack:**
    `PostgreSQL 16` &bull; `Neon Serverless` &bull; `PL/pgSQL` &bull; `Python 3.13` &bull; `Streamlit` &bull; `Graphviz` &bull; `psycopg2`
    """)

# =============================================================================
# TOP NAVIGATION TABS (MULTI-PAGE FINTECH EXPERIENCE)
# =============================================================================
main_tabs = st.tabs([
    "Banking Operations & Simulator",
    "Trigger Code for Selected Operation",
    "In-Engine Trigger Theory & Buffers",
    "Role-Specific Execution Flowchart",
    "Exam Lab & AI Evaluator"
])

tab_simulator, tab_trigger_code, tab_eca_theory, tab_flowchart, tab_exam_lab = main_tabs

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
    job_display_map[job_name] = f"{'✔️' if has_access else '❌'} {job_name}"

# -----------------------------------------------------------------------------
# TAB 1: BANKING OPERATIONS & SIMULATOR
# -----------------------------------------------------------------------------
with tab_simulator:
    # Top KPI Metric Ribbon
    kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)
    with kpi_col1:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Active Security Role</div>
            <div class="kpi-value" style="color: #38bdf8;">{format_role_name(active_role)}</div>
        </div>
        """, unsafe_allow_html=True)
    with kpi_col2:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">PostgreSQL Catalogs</div>
            <div class="kpi-value" style="color: #c084fc;">information_schema</div>
        </div>
        """, unsafe_allow_html=True)
    with kpi_col3:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">PL/pgSQL Triggers</div>
            <div class="kpi-value" style="color: #f59e0b;">4 In-Engine Firewalls</div>
        </div>
        """, unsafe_allow_html=True)
    with kpi_col4:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">Verification Harness</div>
            <div class="kpi-value" style="color: #10b981;">12/12 Tests Passing</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)
    st.subheader("Simulate Database Operation")

    selected_job_key = st.selectbox(
        "Select a Banking Operation to Test:", 
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
            st.success(f"✅ **RBAC Authorization Granted**: Role `{format_role_name(active_role)}` holds `{selected_job_details['privilege']}` privilege on `{selected_job_details['table']}`.")    
            
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
                run_clicked = st.button("Run Operation", type="primary", use_container_width=True)
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
                            st.success("✅ Query executed successfully.")
                        else:
                            st.success("✅ Transaction committed to PostgreSQL.")
                        
                        if result.get("data") is not None:
                            if len(result["data"]) == 0:
                                st.info("No records found in this table yet.")
                                df = pd.DataFrame(columns=result.get("columns", []))
                                st.dataframe(df, use_container_width=True)
                            else:
                                df = pd.DataFrame(result["data"], columns=result.get("columns", []))
                                st.dataframe(df, use_container_width=True)

                    elif result["status"] == "denied":
                        st.error("Access Denied by PostgreSQL RBAC Engine")
                        st.error(result.get("message", "Insufficient privileges."))

                    else:
                        st.error(f"Execution Blocked by Trigger: {result.get('clean_message', 'Trigger exception raised.')}")
                        with st.expander("Show Full PostgreSQL Engine Exception"):
                            st.code(result.get("message", ""), language="text")

        else:
            st.error(f"**Access Denied**: Active role `{format_role_name(active_role)}` does not hold `{selected_job_details['privilege']}` privilege on `{selected_job_details['table']}`.")
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
            sync_bg = "#064e3b"
            sync_color = "#a7f3d0"
            sync_border = "#10b981"
        else:
            sync_badge = "Free Inspection"
            sync_bg = "#1e293b"
            sync_color = "#94a3b8"
            sync_border = "#334155"

        role_badge = "<span style='color: #10b981; font-weight: 700;'>✔️ Authorized</span>" if inspect_has_access else "<span style='color: #ef4444; font-weight: 700;'>❌ RBAC Denied</span>"
        st.markdown(f"""
        <div style='background: {sync_bg}; color: {sync_color}; border: 1px solid {sync_border}; border-radius: 6px; padding: 6px 10px; font-size: 11px; font-weight: 600; text-align: center;'>
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
            "cascades": "Initializes candidate row state with approval_status := 'SUBMITTED'."
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
        <div style="background: #111827; border: 1px solid #1f2937; border-left: 4px solid #38bdf8; border-radius: 8px; padding: 14px 18px; margin-bottom: 14px;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                <div>
                    <span style="font-size: 11px; font-weight: 700; color: #38bdf8; text-transform: uppercase; letter-spacing: 1px;">Directly Backing Selected Operation</span>
                    <h3 style="margin: 4px 0 0 0; color: #f8fafc; font-size: 18px;"><code>{trigger_title}</code></h3>
                </div>
                <div style="margin-top: 6px;">
                    <span style="background: rgba(56, 189, 248, 0.15); border: 1px solid #0284c7; color: #38bdf8; padding: 4px 10px; border-radius: 9999px; font-size: 11px; font-weight: 700;">
                        {trigger_timing}
                    </span>
                </div>
            </div>
            <div style="color: #cbd5e1; font-size: 13px; line-height: 1.5; margin-top: 8px;">
                {trigger_summary}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # 2. Role Context Banner
        role_hint = get_role_context_hint(active_role, active_trigger_key, inspect_job)
        st.markdown(f"""
        <div style="background: rgba(56, 189, 248, 0.08); border-left: 3px solid #38bdf8; border-radius: 6px; padding: 10px 14px; margin-bottom: 16px;">
            <span style="font-size: 11px; font-weight: 700; color: #38bdf8; text-transform: uppercase; letter-spacing: 0.5px;">
                Relevance to Active Role ({format_role_name(active_role)})
            </span>
            <div style="font-size: 12px; color: #e2e8f0; margin-top: 3px; line-height: 1.4;">
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
                    <div style="background: #1e293b; border: 1px solid #334155; border-radius: 8px; padding: 12px 14px; height: 100%;">
                        <div style="font-size: 13px; font-weight: 700; color: #f8fafc;">{flabel}</div>
                        <div style="margin-top: 4px;">
                            <span style="font-size: 10px; font-weight: 700; color: #f87171; font-family: monospace; background: rgba(239, 68, 68, 0.15); padding: 2px 6px; border-radius: 4px; border: 1px solid rgba(239, 68, 68, 0.3);">
                                {ecode}
                            </span>
                        </div>
                        <div style="font-size: 11px; color: #cbd5e1; margin-top: 8px; line-height: 1.4;">
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
            st.info("**Try it in the Simulator (Tab 1):** Submit a loan for Profile **104** (Frozen Account) or Profile **106** (Already has a pending loan) to see anti-stacking block the insertion!")
        elif active_trigger_key == "enforce_loan_workflow":
            st.info("**Try it in the Simulator (Tab 1):** Switch between `senior_underwriter` and `branch_manager` to test workflow role authority and stage progression rules!")
    else:
        st.markdown(f"""
        <div style="background: #111827; border: 1px solid #334155; border-left: 4px solid #f59e0b; border-radius: 8px; padding: 16px 20px; margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                <div>
                    <span style="font-size: 11px; font-weight: 700; color: #f59e0b; text-transform: uppercase; letter-spacing: 1px;">
                        Architectural Classification: Tier-1 RBAC Governed
                    </span>
                    <h3 style="margin: 4px 0 0 0; color: #f8fafc; font-size: 18px;">
                        No Procedural Trigger Attached to <code>{inspect_job}</code>
                    </h3>
                </div>
                <div style="margin-top: 6px;">
                    <span style="background: rgba(245, 158, 11, 0.15); border: 1px solid #d97706; color: #fbbf24; padding: 4px 10px; border-radius: 9999px; font-size: 11px; font-weight: 700;">
                        DIRECT POSTGRESQL ENGINE QUERY
                    </span>
                </div>
            </div>
            <div style="color: #cbd5e1; font-size: 13px; line-height: 1.6; margin-top: 12px;">
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
    all_job_keys = list(QUERIES.keys())
    current_sim_job = st.session_state.get("current_selected_operation", all_job_keys[3] if len(all_job_keys) > 3 else all_job_keys[0])
    default_tab3_idx = all_job_keys.index(current_sim_job) if current_sim_job in all_job_keys else 0

    st.markdown("### In-Engine Trigger Theory & Memory Buffers (ECA Model)")

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
            sync_bg = "#064e3b"
            sync_color = "#a7f3d0"
            sync_border = "#10b981"
        else:
            sync_badge = "Free Inspection"
            sync_bg = "#1e293b"
            sync_color = "#94a3b8"
            sync_border = "#334155"

        role_badge = "<span style='color: #10b981; font-weight: 700;'>✔️ Authorized</span>" if dissect_has_access else "<span style='color: #ef4444; font-weight: 700;'>❌ RBAC Denied</span>"
        st.markdown(f"""
        <div style='background: {sync_bg}; color: {sync_color}; border: 1px solid {sync_border}; border-radius: 6px; padding: 6px 10px; font-size: 11px; font-weight: 600; text-align: center;'>
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
            sync_bg = "#064e3b"
            sync_color = "#a7f3d0"
            sync_border = "#10b981"
        else:
            sync_badge = "Free Inspection"
            sync_bg = "#1e293b"
            sync_color = "#94a3b8"
            sync_border = "#334155"

        role_badge = "<span style='color: #10b981; font-weight: 700;'>✔️ Authorized</span>" if flow_has_access else "<span style='color: #ef4444; font-weight: 700;'>❌ RBAC Denied</span>"
        st.markdown(f"""
        <div style='background: {sync_bg}; color: {sync_color}; border: 1px solid {sync_border}; border-radius: 6px; padding: 6px 10px; font-size: 11px; font-weight: 600; text-align: center;'>
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
    st.markdown("""
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px; margin-top: 8px;">
        <div style="background: #111827; border: 1px solid #1f2937; border-top: 3px solid #c084fc; border-radius: 8px; padding: 14px 16px;">
            <div style="font-size: 11px; font-weight: 700; color: #c084fc; text-transform: uppercase; letter-spacing: 0.5px;">Tier 1: Access Check</div>
            <div style="font-size: 14px; font-weight: 700; color: #f8fafc; margin-top: 3px;">PostgreSQL RBAC Catalog</div>
            <div style="font-size: 12px; color: #94a3b8; margin-top: 6px; line-height: 1.4;">
                Checks role privileges in <code>information_schema</code>. Unauthorized queries are halted immediately with 403 <code>InsufficientPrivilege</code> without reading or writing disk rows.
            </div>
        </div>
        <div style="background: #111827; border: 1px solid #1f2937; border-top: 3px solid #38bdf8; border-radius: 8px; padding: 14px 16px;">
            <div style="font-size: 11px; font-weight: 700; color: #38bdf8; text-transform: uppercase; letter-spacing: 0.5px;">Tier 2: Business Firewalls</div>
            <div style="font-size: 14px; font-weight: 700; color: #f8fafc; margin-top: 3px;">In-Engine PL/pgSQL Triggers</div>
            <div style="font-size: 12px; color: #94a3b8; margin-top: 6px; line-height: 1.4;">
                Intercepts writes in memory before commitment (<code>NEW</code> buffer). Checks KYC, account freeze status, fraud alerts, anti-stacking, and workflow permissions.
            </div>
        </div>
        <div style="background: #111827; border: 1px solid #1f2937; border-top: 3px solid #10b981; border-radius: 8px; padding: 14px 16px;">
            <div style="font-size: 11px; font-weight: 700; color: #10b981; text-transform: uppercase; letter-spacing: 0.5px;">Tier 3: Guarantee</div>
            <div style="font-size: 14px; font-weight: 700; color: #f8fafc; margin-top: 3px;">ACID Atomicity & Audit</div>
            <div style="font-size: 12px; color: #94a3b8; margin-top: 6px; line-height: 1.4;">
                Rule violation calls <code>RAISE EXCEPTION</code> triggering an automatic <code>ROLLBACK</code> (zero corrupted balances). Success commits to disk and cascades to tamper-proof <code>audit_log</code>.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# TAB 5: AI-POWERED PRACTICE LAB & EXAM EVALUATOR
# -----------------------------------------------------------------------------
with tab_exam_lab:
    render_exam_lab_tab(active_role=active_role)

