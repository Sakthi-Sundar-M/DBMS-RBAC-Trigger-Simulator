import os
import streamlit as st
import html
import pandas as pd

def parse_trigger_steps(job_name, result):
    """
    Builds the sequential pipeline of trigger verification steps based on the job type
    and evaluates each step as 'passed', 'failed', or 'blocked'.
    """
    status = result.get("status", "error")
    error_code = result.get("error_code")
    raw_msg = result.get("message", "")

    # =========================================================================
    # 1. DAILY TRANSACTIONS PIPELINE (Trigger: process_transaction)
    # =========================================================================
    if "Transaction" in job_name and "INSERT" in job_name:
        steps = [
            {
                "id": "kyc",
                "title": "KYC Verification",
                "passed_text": "KYC verification passed",
                "failed_text": "KYC verification failed: unverified profile",
                "blocked_text": "KYC verification pending",
            },
            {
                "id": "account_status",
                "title": "Account Status Check",
                "passed_text": "Account status: active (not frozen)",
                "failed_text": "Account status check failed: account is frozen or closed",
                "blocked_text": "Account status: not checked",
            },
            {
                "id": "fraud_check",
                "title": "Fraud Investigation Check",
                "passed_text": "Fraud check passed: no alerts on file",
                "failed_text": "Fraud check failed: alert on file",
                "blocked_text": "Fraud alerts: not checked",
            },
            {
                "id": "execution",
                "title": "Transfer Execution",
                "passed_text": "Transaction committed: Funds transferred",
                "failed_text": "Transaction blocked: insufficient funds or transfer error",
                "blocked_text": "Insert stopped before any row was written",
            }
        ]

        if status == "success":
            for s in steps:
                s["state"] = "passed"
                s["display_text"] = s["passed_text"]
        elif status == "denied":
            steps[0]["state"] = "failed"
            steps[0]["display_text"] = "Permission check: this role cannot INSERT into the table"
            for s in steps[1:]:
                s["state"] = "blocked"
                s["display_text"] = s["blocked_text"]
        else:
            if error_code == "KYC_CHECK_FAILED":
                steps[0]["state"] = "failed"
                steps[0]["display_text"] = f"KYC check failed: {result.get('clean_message', 'unverified profile')}"
                steps[1]["state"] = "blocked"
                steps[1]["display_text"] = steps[1]["blocked_text"]
                steps[2]["state"] = "blocked"
                steps[2]["display_text"] = steps[2]["blocked_text"]
                steps[3]["state"] = "blocked"
                steps[3]["display_text"] = steps[3]["blocked_text"]
            elif error_code == "ACCOUNT_FROZEN_BLOCKED":
                steps[0]["state"] = "passed"
                steps[0]["display_text"] = steps[0]["passed_text"]
                steps[1]["state"] = "failed"
                steps[1]["display_text"] = f"Account status check failed: {result.get('clean_message', 'frozen/closed account')}"
                steps[2]["state"] = "blocked"
                steps[2]["display_text"] = steps[2]["blocked_text"]
                steps[3]["state"] = "blocked"
                steps[3]["display_text"] = steps[3]["blocked_text"]
            elif error_code == "FRAUD_CHECK_FAILED":
                steps[0]["state"] = "passed"
                steps[0]["display_text"] = steps[0]["passed_text"]
                steps[1]["state"] = "passed"
                steps[1]["display_text"] = steps[1]["passed_text"]
                steps[2]["state"] = "failed"
                steps[2]["display_text"] = "Fraud check failed: alert on file"
                steps[3]["state"] = "blocked"
                steps[3]["display_text"] = steps[3]["blocked_text"]
            elif error_code == "INSUFFICIENT_FUNDS":
                steps[0]["state"] = "passed"
                steps[0]["display_text"] = steps[0]["passed_text"]
                steps[1]["state"] = "passed"
                steps[1]["display_text"] = steps[1]["passed_text"]
                steps[2]["state"] = "passed"
                steps[2]["display_text"] = steps[2]["passed_text"]
                steps[3]["state"] = "failed"
                steps[3]["display_text"] = f"Transfer blocked: {result.get('clean_message', 'insufficient balance')}"
            else:
                steps[0]["state"] = "failed"
                steps[0]["display_text"] = f"Validation rejected: {result.get('clean_message', raw_msg[:60])}"
                for s in steps[1:]:
                    s["state"] = "blocked"
                    s["display_text"] = s["blocked_text"]
        return steps

    # =========================================================================
    # 2. LOAN APPLICATIONS PIPELINE (Trigger: check_loan_eligibility)
    # =========================================================================
    elif "Loan" in job_name and "INSERT" in job_name:
        steps = [
            {
                "id": "kyc",
                "title": "Customer KYC Status",
                "passed_text": "Customer KYC verified (APPROVED)",
                "failed_text": "KYC check failed: KYC status not approved",
                "blocked_text": "KYC verification pending",
            },
            {
                "id": "account_integrity",
                "title": "Account Operational Health",
                "passed_text": "Account status clean: no frozen or closed accounts",
                "failed_text": "Account compromised: customer has a frozen/closed account",
                "blocked_text": "Account status: not checked",
            },
            {
                "id": "fraud_check",
                "title": "Fraud Risk Assessment",
                "passed_text": "Fraud assessment clean: no active fraud investigations",
                "failed_text": "Fraud alert detected on customer account",
                "blocked_text": "Fraud alerts: not checked",
            },
            {
                "id": "stacking",
                "title": "Loan Stacking Prevention",
                "passed_text": "No concurrent loans under review",
                "failed_text": "Loan stacking blocked: customer already has a pending application",
                "blocked_text": "Loan stacking: not checked",
            },
            {
                "id": "creation",
                "title": "Loan Application Created",
                "passed_text": "Application registered in SUBMITTED status",
                "failed_text": "Application rejected before insert",
                "blocked_text": "Application creation blocked",
            }
        ]

        if status == "success":
            for s in steps:
                s["state"] = "passed"
                s["display_text"] = s["passed_text"]
        elif status == "denied":
            steps[0]["state"] = "failed"
            steps[0]["display_text"] = "Permission check: this role cannot INSERT into the table"
            for s in steps[1:]:
                s["state"] = "blocked"
                s["display_text"] = s["blocked_text"]
        else:
            if error_code == "LOAN_KYC_FAILED":
                steps[0]["state"] = "failed"
                steps[0]["display_text"] = steps[0]["failed_text"]
                for s in steps[1:]:
                    s["state"] = "blocked"
                    s["display_text"] = s["blocked_text"]
            elif error_code == "LOAN_ACCOUNT_COMPROMISED":
                steps[0]["state"] = "passed"
                steps[0]["display_text"] = steps[0]["passed_text"]
                steps[1]["state"] = "failed"
                steps[1]["display_text"] = steps[1]["failed_text"]
                for s in steps[2:]:
                    s["state"] = "blocked"
                    s["display_text"] = s["blocked_text"]
            elif error_code == "LOAN_STACKING_BLOCKED":
                steps[0]["state"] = "passed"
                steps[0]["display_text"] = steps[0]["passed_text"]
                steps[1]["state"] = "passed"
                steps[1]["display_text"] = steps[1]["passed_text"]
                steps[2]["state"] = "passed"
                steps[2]["display_text"] = steps[2]["passed_text"]
                steps[3]["state"] = "failed"
                steps[3]["display_text"] = steps[3]["failed_text"]
                steps[4]["state"] = "blocked"
                steps[4]["display_text"] = steps[4]["blocked_text"]
            else:
                steps[0]["state"] = "failed"
                steps[0]["display_text"] = f"Validation Error: {result.get('clean_message', raw_msg[:60])}"
                for s in steps[1:]:
                    s["state"] = "blocked"
                    s["display_text"] = s["blocked_text"]
        return steps

    # =========================================================================
    # 3. LOAN WORKFLOW PIPELINE (Trigger: enforce_loan_workflow)
    # =========================================================================
    elif "Loan Status" in job_name and "UPDATE" in job_name:
        steps = [
            {
                "id": "auth",
                "title": "Role Stage Authorization",
                "passed_text": "Role authorized for state transition",
                "failed_text": "Unauthorized role for requested stage",
                "blocked_text": "Role authorization pending",
            },
            {
                "id": "linear_state",
                "title": "Linear State Machine Validation",
                "passed_text": "Strict linear transition validated (SUBMITTED -> UNDERWRITE -> APPROVED)",
                "failed_text": "Status change not allowed: a stage was skipped or moved backwards",
                "blocked_text": "Status change: not checked",
            },
            {
                "id": "risk_check",
                "title": "Underwriting Risk & Fraud Assessment",
                "passed_text": "Account & fraud risk clean at underwriting",
                "failed_text": "Approval blocked: active fraud alert or frozen account",
                "blocked_text": "Risk checks: not checked",
            },
            {
                "id": "audit_commit",
                "title": "Workflow Update & Audit Log",
                "passed_text": "Workflow status committed & audit event logged",
                "failed_text": "Workflow update blocked before commit",
                "blocked_text": "Audit entry: not written",
            }
        ]

        if status == "success":
            for s in steps:
                s["state"] = "passed"
                s["display_text"] = s["passed_text"]
        elif status == "denied":
            steps[0]["state"] = "failed"
            steps[0]["display_text"] = "Permission check: this role cannot UPDATE approval_status"
            for s in steps[1:]:
                s["state"] = "blocked"
                s["display_text"] = s["blocked_text"]
        else:
            if error_code == "WORKFLOW_ROLE_DENIED":
                steps[0]["state"] = "failed"
                steps[0]["display_text"] = f"Permission check: {result.get('clean_message', 'unauthorized role')}"
                for s in steps[1:]:
                    s["state"] = "blocked"
                    s["display_text"] = s["blocked_text"]
            elif error_code in ("WORKFLOW_STAGE_SKIPPED", "WORKFLOW_BACKWARD_TRANSITION", "WORKFLOW_INVALID_STATE"):
                steps[0]["state"] = "passed"
                steps[0]["display_text"] = steps[0]["passed_text"]
                steps[1]["state"] = "failed"
                steps[1]["display_text"] = f"Workflow Error: {result.get('clean_message', 'illegal transition')}"
                steps[2]["state"] = "blocked"
                steps[2]["display_text"] = steps[2]["blocked_text"]
                steps[3]["state"] = "blocked"
                steps[3]["display_text"] = steps[3]["blocked_text"]
            elif error_code == "WORKFLOW_RISK_BLOCKED":
                steps[0]["state"] = "passed"
                steps[0]["display_text"] = steps[0]["passed_text"]
                steps[1]["state"] = "passed"
                steps[1]["display_text"] = steps[1]["passed_text"]
                steps[2]["state"] = "failed"
                steps[2]["display_text"] = f"Risk Block: {result.get('clean_message', 'frozen/fraud accounts')}"
                steps[3]["state"] = "blocked"
                steps[3]["display_text"] = steps[3]["blocked_text"]
            elif error_code == "WORKFLOW_TERMINAL_STATE":
                steps[0]["state"] = "passed"
                steps[0]["display_text"] = steps[0]["passed_text"]
                steps[1]["state"] = "failed"
                steps[1]["display_text"] = "Terminal State Error: Final decision already reached"
                steps[2]["state"] = "blocked"
                steps[2]["display_text"] = steps[2]["blocked_text"]
                steps[3]["state"] = "blocked"
                steps[3]["display_text"] = steps[3]["blocked_text"]
            else:
                steps[0]["state"] = "failed"
                steps[0]["display_text"] = f"Error: {result.get('clean_message', raw_msg[:60])}"
                for s in steps[1:]:
                    s["state"] = "blocked"
                    s["display_text"] = s["blocked_text"]
        return steps

    # =========================================================================
    # 4. DEFAULT MUTATION PIPELINE (Account status, balance, etc.)
    # =========================================================================
    else:
        steps = [
            {
                "id": "rbac",
                "title": "Permission check",
                "passed_text": "Role authorization verified via information_schema",
                "failed_text": "Permission check by PostgreSQL",
                "blocked_text": "Authorization pending",
            },
            {
                "id": "mutation",
                "title": "Table Constraint & State Update",
                "passed_text": "Data constraints verified & state updated",
                "failed_text": "Data validation or constraint failure",
                "blocked_text": "Update: not run",
            },
            {
                "id": "audit",
                "title": "Audit Log Trigger (log_audit_event)",
                "passed_text": "Audit event captured silently via SECURITY DEFINER",
                "failed_text": "Audit logging failed",
                "blocked_text": "Audit entry: not written",
            }
        ]

        if status == "success":
            for s in steps:
                s["state"] = "passed"
                s["display_text"] = s["passed_text"]
        elif status == "denied":
            steps[0]["state"] = "failed"
            steps[0]["display_text"] = "Permission check: insufficient role privileges"
            steps[1]["state"] = "blocked"
            steps[1]["display_text"] = steps[1]["blocked_text"]
            steps[2]["state"] = "blocked"
            steps[2]["display_text"] = steps[2]["blocked_text"]
        else:
            steps[0]["state"] = "passed"
            steps[0]["display_text"] = steps[0]["passed_text"]
            steps[1]["state"] = "failed"
            steps[1]["display_text"] = f"Execution Error: {result.get('clean_message', raw_msg[:60])}"
            steps[2]["state"] = "blocked"
            steps[2]["display_text"] = steps[2]["blocked_text"]
        return steps


def render_live_trace(job_name, result):
    """
    Renders the Live Trace UI card using separated static CSS classes.
    """
    steps = parse_trigger_steps(job_name, result)

    # Only the first step that stops the statement is "failed"; everything after it is "not reached".
    stop_idx = next((i for i, s in enumerate(steps) if s["state"] in ("failed", "blocked")), None)

    html_cards = []
    for idx, step in enumerate(steps):
        text = html.escape(step["display_text"])

        if stop_idx is not None and idx == stop_idx:
            state, icon, badge_text = "failed", "✕", "Stopped here"
        elif step["state"] == "passed":
            state, icon, badge_text = "passed", "✓", "Passed"
        else:
            state, icon, badge_text = "skipped", "–", "Not reached"

        card_html = (
            f'<div class="trace-step {state}">'
            f'<div class="trace-step-content">'
            f'<span class="trace-icon">{icon}</span>'
            f'<span class="trace-step-text">{text}</span>'
            f'</div>'
            f'<span class="trace-badge">{badge_text}</span>'
            f'</div>'
        )
        html_cards.append(card_html)

        # Connector arrow between steps
        if idx < len(steps) - 1:
            arrow_class = "passed" if state == "passed" else "skipped"
            arrow_html = (
                f'<div class="trace-arrow {arrow_class}">'
                f'<span>|</span>'
                f'</div>'
            )
            html_cards.append(arrow_html)

    all_cards_html = "".join(html_cards)

    full_component = (
        f'<div class="trace-container">'
        f'<div class="trace-header">'
        f'<div class="trace-title">Trigger pipeline trace</div>'
        f'<div class="trace-subtitle">Checks run inside PostgreSQL, in order, until one stops the statement</div>'
        f'</div>'
        f'{all_cards_html}'
        f'</div>'
    )
    st.html(full_component)


def render_diff_viewer(before_snapshot, after_snapshot, job_name, result):
    """
    Renders an interactive Before/After Diff Viewer showing database row state
    snapshots side-by-side using separated static CSS classes.
    """
    if not before_snapshot and not after_snapshot:
        return
    before_snapshot = before_snapshot or {}
    after_snapshot = after_snapshot or {}

    status = result.get("status")
    is_success = (status == "success")

    st.markdown('<div class="diff-section-title">Row state before and after</div>', unsafe_allow_html=True)

    col_before, col_after = st.columns(2)

    # -------------------------------------------------------------------------
    # BEFORE COLUMN
    # -------------------------------------------------------------------------
    with col_before:
        before_header = (
            '<div class="diff-column-header pre">'
            '<span>Before the statement</span>'
            '</div>'
        )
        st.html(before_header)

        if "accounts" in before_snapshot:
            for acc_id, acc in before_snapshot["accounts"].items():
                card = (
                    f'<div class="diff-card">'
                    f'<div class="diff-card-header">'
                    f'<span class="diff-card-title">Account #{acc_id}</span>'
                    f'<span class="diff-card-type">Type: {acc.get("type", "N/A")}</span>'
                    f'</div>'
                    f'<div class="diff-card-body">'
                    f'<div><span class="diff-card-type">Balance: </span>'
                    f'<span class="diff-card-balance">${acc.get("balance", 0.0):,.2f}</span></div>'
                    f'<span class="diff-status-badge">{acc.get("status", "ACTIVE")}</span>'
                    f'</div></div>'
                )
                st.html(card)

        elif "loans" in before_snapshot:
            for loan_id, loan in before_snapshot["loans"].items():
                card = (
                    f'<div class="diff-card">'
                    f'<div class="diff-card-header">'
                    f'<span class="diff-card-title">Loan #{loan_id} (Profile #{loan.get("profile_id")})</span>'
                    f'</div>'
                    f'<div class="diff-card-body">'
                    f'<div><span class="diff-card-type">Amount: </span>'
                    f'<span class="diff-card-balance" style="color: #16191D; font-size: 15px;">${loan.get("requested_amount", 0.0):,.2f}</span></div>'
                    f'<span class="diff-status-badge" style="background: #F4ECDD; color: #A8322A;">{loan.get("approval_status")}</span>'
                    f'</div></div>'
                )
                st.html(card)

    # -------------------------------------------------------------------------
    # AFTER COLUMN
    # -------------------------------------------------------------------------
    with col_after:
        if is_success:
            after_header = (
                '<div class="diff-column-header post">'
                '<span>After commit</span>'
                '</div>'
            )
            st.html(after_header)

            if "accounts" in after_snapshot:
                for acc_id, acc in after_snapshot["accounts"].items():
                    old_acc = before_snapshot.get("accounts", {}).get(acc_id, {})
                    old_bal = old_acc.get("balance", acc.get("balance", 0.0))
                    new_bal = acc.get("balance", 0.0)
                    diff = new_bal - old_bal

                    diff_html = ""
                    if abs(diff) > 0.001:
                        if diff > 0:
                            diff_html = f'<span style="color: #2E6B5E; font-size: 13px; font-weight: 700; margin-left: 6px;">(+${diff:,.2f})</span>'
                        else:
                            diff_html = f'<span style="color: #A8322A; font-size: 13px; font-weight: 700; margin-left: 6px;">(-${abs(diff):,.2f})</span>'

                    status_diff = ""
                    if old_acc.get("status") != acc.get("status"):
                        status_diff = f'<span class="diff-status-badge" style="color: #A8322A; background: #F4ECDD;">{acc.get("status")}</span>'
                    else:
                        status_diff = f'<span class="diff-status-badge">{acc.get("status")}</span>'

                    card = (
                        f'<div class="diff-card updated">'
                        f'<div class="diff-card-header">'
                        f'<span class="diff-card-title">Account #{acc_id}</span>'
                        f'<span style="color: #2E6B5E; font-size: 12px; font-weight: 600;">Updated</span>'
                        f'</div>'
                        f'<div class="diff-card-body">'
                        f'<div><span class="diff-card-type">Balance: </span>'
                        f'<span class="diff-card-balance">${new_bal:,.2f}</span>'
                        f'{diff_html}</div>'
                        f'{status_diff}'
                        f'</div></div>'
                    )
                    st.html(card)

            elif "loans" in after_snapshot:
                for loan_id, loan in after_snapshot["loans"].items():
                    old_loan = before_snapshot.get("loans", {}).get(loan_id, {})
                    old_status = old_loan.get("approval_status", "")
                    new_status = loan.get("approval_status", "")

                    card = (
                        f'<div class="diff-card updated">'
                        f'<div class="diff-card-header">'
                        f'<span class="diff-card-title">Loan #{loan_id} (Profile #{loan.get("profile_id")})</span>'
                        f'<span style="color: #2E6B5E; font-size: 12px; font-weight: 600;">State Advanced</span>'
                        f'</div>'
                        f'<div class="diff-card-body">'
                        f'<div><span class="diff-card-type">Amount: </span>'
                        f'<span class="diff-card-balance" style="color: #16191D; font-size: 15px;">${loan.get("requested_amount", 0.0):,.2f}</span></div>'
                        f'<div><span style="color: #2E6B5E; font-size: 11px; text-decoration: line-through; margin-right: 4px;">{old_status}</span>'
                        f'<span class="diff-status-badge" style="background: #E4EFEB;">{new_status}</span></div>'
                        f'</div></div>'
                    )
                    st.html(card)

        else:
            # Rejection / Rollback state
            after_header = (
                '<div class="diff-column-header rollback">'
                '<span>After rollback</span>'
                '</div>'
            )
            st.html(after_header)

            card = (
                '<div class="diff-card rollback">'
                '<div class="diff-rollback-title">Transaction aborted</div>'
                '<div class="diff-rollback-desc">'
                'PostgreSQL triggered an automatic <strong>ROLLBACK</strong>.<br>'
                '<strong>0 rows modified</strong>: database state remains completely intact.'
                '</div></div>'
            )
            st.html(card)



def load_trigger_sources():
    """Loads trigger SQL source definitions from separated .sql files."""
    triggers = {}
    trigger_names = [
        "process_transaction", 
        "check_loan_eligibility", 
        "enforce_loan_workflow", 
        "log_audit_event"
    ]
    base_dir = os.path.dirname(__file__)
    for name in trigger_names:
        file_path = os.path.join(base_dir, "sql", "triggers", f"{name}.sql")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                triggers[name] = f.read().strip()
    return triggers

TRIGGER_SOURCE_CODES = load_trigger_sources()


def render_graphviz_flowchart(role, action_name, status):
    """
    Renders a compact, vector SVG Architecture Flowchart using Streamlit's native
    st.graphviz_chart engine. Optimized with Left-to-Right layout and compact dimensions.
    """
    verb = action_name.split(' ')[0].strip() if action_name else "SQL"
    safe_role = role.replace('"', '').replace("'", "")
    clean_role = safe_role.replace("_", " ").title()

    common_graph_attr = 'graph [rankdir=LR, bgcolor="transparent", margin="0.04,0.04", nodesep=0.18, ranksep=0.22];'
    common_node_attr = 'node [fontname="Helvetica,Arial,sans-serif", style="filled,rounded", shape=box, fontsize=9, height=0.3, margin="0.08,0.04", penwidth=1.2];'
    common_edge_attr = 'edge [fontname="Helvetica,Arial,sans-serif", fontsize=8, arrowsize=0.6];'

    if status == "denied":
        dot_code = f"""
        digraph {{
            {common_graph_attr}
            {common_node_attr}
            {common_edge_attr}
            edge [color="#A8322A", fontcolor="#A8322A"]

            role [label="Role: {clean_role}", shape=ellipse, fillcolor="#F5E6E4", fontcolor="#A8322A", color="#B8975A"]
            rbac [label="RBAC Engine\\n(System Catalog)", shape=diamond, fillcolor="#FBFAF7", fontcolor="#16191D", color="#8B9097"]
            blocked [label="Access denied\\n(SQLSTATE 42501)", shape=box, fillcolor="#F5E6E4", fontcolor="#A8322A", color="#A8322A"]
            abort [label="Transaction Aborted\\nZero DB Mutation", shape=box, fillcolor="#FBFAF7", fontcolor="#16191D", color="#7C9393"]

            role -> rbac [label="Dispatches {verb}"]
            rbac -> blocked [label="No GRANT"]
            blocked -> abort [label="Aborted"]
        }}
        """
    elif status == "success" and "transaction" in action_name.lower():
        dot_code = f"""
        digraph {{
            {common_graph_attr}
            {common_node_attr}
            {common_edge_attr}
            edge [color="#2E6B5E", fontcolor="#2E6B5E"]

            role [label="Role: {clean_role}", shape=ellipse, fillcolor="#F5E6E4", fontcolor="#A8322A", color="#B8975A"]
            rbac [label="RBAC Check\\n(Granted)", shape=diamond, fillcolor="#E4EFEB", fontcolor="#2E6B5E", color="#2E6B5E"]
            tbl [label="daily_transactions\\n(Memory Buffer)", shape=cylinder, fillcolor="#FBFAF7", fontcolor="#16191D", color="#5F8799"]
            trigger [label="BEFORE Trigger:\\nprocess_transaction()", shape=box, fillcolor="#FBFAF7", fontcolor="#16191D", color="#6F94A6"]
            checks [label="In-Engine Verification:\\nKYC | Health | Fraud | Balance", shape=box, fillcolor="#FBFAF7", fontcolor="#16191D", color="#A8322A"]
            mutation [label="Atomic In-Engine Mutation:\\nDebit Sender & Credit Receiver", shape=cylinder, fillcolor="#E4EFEB", fontcolor="#2E6B5E", color="#2E6B5E"]
            audit [label="AFTER Trigger:\\nlog_audit_event()", shape=box, fillcolor="#FBFAF7", fontcolor="#16191D", color="#8B9097"]
            commit [label="ACID Commit\\n(Synced to Disk)", shape=ellipse, fillcolor="#E4EFEB", fontcolor="#2E6B5E", color="#2E6B5E"]

            role -> rbac [label="Dispatches INSERT"]
            rbac -> tbl [label="Allowed"]
            tbl -> trigger [label="Intercepted"]
            trigger -> checks [label="Evaluates Constraints"]
            checks -> mutation [label="Passed"]
            mutation -> audit [label="Cascades"]
            audit -> commit [label="Committed"]
        }}
        """
    elif status == "success" and "loan" in action_name.lower() and "insert" in action_name.lower():
        dot_code = f"""
        digraph {{
            {common_graph_attr}
            {common_node_attr}
            {common_edge_attr}
            edge [color="#2E6B5E", fontcolor="#2E6B5E"]

            role [label="Role: {clean_role}", shape=ellipse, fillcolor="#F5E6E4", fontcolor="#A8322A", color="#B8975A"]
            rbac [label="RBAC Check\\n(Granted)", shape=diamond, fillcolor="#E4EFEB", fontcolor="#2E6B5E", color="#2E6B5E"]
            tbl [label="loan_applications\\n(Memory Buffer)", shape=cylinder, fillcolor="#FBFAF7", fontcolor="#16191D", color="#5F8799"]
            trigger [label="BEFORE Trigger:\\ncheck_loan_eligibility()", shape=box, fillcolor="#FBFAF7", fontcolor="#16191D", color="#6F94A6"]
            checks [label="Eligibility Rules:\\nKYC | Anti-Stacking | Health", shape=box, fillcolor="#FBFAF7", fontcolor="#16191D", color="#A8322A"]
            registered [label="Registered State:\\napproval_status := SUBMITTED", shape=cylinder, fillcolor="#E4EFEB", fontcolor="#2E6B5E", color="#2E6B5E"]
            commit [label="ACID Commit", shape=ellipse, fillcolor="#E4EFEB", fontcolor="#2E6B5E", color="#2E6B5E"]

            role -> rbac [label="Dispatches INSERT"]
            rbac -> tbl [label="Allowed"]
            tbl -> trigger [label="Intercepted"]
            trigger -> checks [label="Evaluates Applicant"]
            checks -> registered [label="Eligible"]
            registered -> commit [label="Row Inserted"]
        }}
        """
    elif status == "success" and "loan" in action_name.lower() and "update" in action_name.lower():
        dot_code = f"""
        digraph {{
            {common_graph_attr}
            {common_node_attr}
            {common_edge_attr}
            edge [color="#2E6B5E", fontcolor="#2E6B5E"]

            role [label="Role: {clean_role}", shape=ellipse, fillcolor="#F5E6E4", fontcolor="#A8322A", color="#B8975A"]
            rbac [label="RBAC Check\\n(Granted)", shape=diamond, fillcolor="#E4EFEB", fontcolor="#2E6B5E", color="#2E6B5E"]
            tbl [label="loan_applications\\n(Memory Buffer)", shape=cylinder, fillcolor="#FBFAF7", fontcolor="#16191D", color="#5F8799"]
            trigger [label="BEFORE Trigger:\\nenforce_loan_workflow()", shape=box, fillcolor="#FBFAF7", fontcolor="#16191D", color="#6F94A6"]
            state [label="State Machine Guard:\\nSUBMITTED -> UNDERWRITE -> APPROVED", shape=box, fillcolor="#FBFAF7", fontcolor="#16191D", color="#A8322A"]
            audit [label="AFTER Trigger:\\nlog_audit_event()", shape=box, fillcolor="#FBFAF7", fontcolor="#16191D", color="#8B9097"]
            commit [label="ACID Commit", shape=ellipse, fillcolor="#E4EFEB", fontcolor="#2E6B5E", color="#2E6B5E"]

            role -> rbac [label="Dispatches UPDATE"]
            rbac -> tbl [label="Allowed"]
            tbl -> trigger [label="Intercepted"]
            trigger -> state [label="Validates Role & Transition"]
            state -> audit [label="State Advanced"]
            audit -> commit [label="Committed"]
        }}
        """
    elif status == "success" and ("select" in action_name.lower() or "view" in action_name.lower()):
        dot_code = f"""
        digraph {{
            {common_graph_attr}
            {common_node_attr}
            {common_edge_attr}
            edge [color="#2E6B5E", fontcolor="#2E6B5E"]

            role [label="Role: {clean_role}", shape=ellipse, fillcolor="#F5E6E4", fontcolor="#A8322A", color="#B8975A"]
            rbac [label="RBAC Engine\\n(System Catalog)", shape=diamond, fillcolor="#E4EFEB", fontcolor="#2E6B5E", color="#2E6B5E"]
            engine [label="PostgreSQL Query Engine\\n(Cost-Based Optimizer)", shape=box, fillcolor="#FBFAF7", fontcolor="#16191D", color="#6F94A6"]
            pool [label="Shared Buffer Pool\\n(Direct Tuple Scan)", shape=cylinder, fillcolor="#FBFAF7", fontcolor="#16191D", color="#5F8799"]
            client [label="Client Result Set\\n(Zero Trigger Mutation)", shape=ellipse, fillcolor="#E4EFEB", fontcolor="#2E6B5E", color="#2E6B5E"]

            role -> rbac [label="Dispatches SELECT"]
            rbac -> engine [label="GRANT SELECT Verified"]
            engine -> pool [label="Executes Plan"]
            pool -> client [label="Streams Tuples"]
        }}
        """
    elif status == "success":
        dot_code = f"""
        digraph {{
            {common_graph_attr}
            {common_node_attr}
            {common_edge_attr}
            edge [color="#2E6B5E", fontcolor="#2E6B5E"]

            role [label="Role: {clean_role}", shape=ellipse, fillcolor="#F5E6E4", fontcolor="#A8322A", color="#B8975A"]
            rbac [label="RBAC Engine\\n(System Catalog)", shape=diamond, fillcolor="#E4EFEB", fontcolor="#2E6B5E", color="#2E6B5E"]
            tbl [label="Target Table\\n(Disk/Buffer)", shape=cylinder, fillcolor="#FBFAF7", fontcolor="#16191D", color="#5F8799"]
            audit [label="AFTER Trigger:\\nlog_audit_event() [If Mutation]", shape=box, fillcolor="#FBFAF7", fontcolor="#16191D", color="#8B9097"]
            commit [label="ACID Complete", shape=ellipse, fillcolor="#E4EFEB", fontcolor="#2E6B5E", color="#2E6B5E"]

            role -> rbac [label="Dispatches {verb}"]
            rbac -> tbl [label="Granted"]
            tbl -> audit [label="Executes Operation"]
            audit -> commit [label="Committed"]
        }}
        """
    else:  # Error / Trigger violation
        dot_code = f"""
        digraph {{
            {common_graph_attr}
            {common_node_attr}
            {common_edge_attr}

            role [label="Role: {clean_role}", shape=ellipse, fillcolor="#F5E6E4", fontcolor="#A8322A", color="#B8975A"]
            rbac [label="RBAC Engine", shape=diamond, fillcolor="#E4EFEB", fontcolor="#2E6B5E", color="#2E6B5E"]
            tbl [label="Target Table\\n(Uncommitted Buffer)", shape=cylinder, fillcolor="#FBFAF7", fontcolor="#16191D", color="#5F8799"]
            trigger [label="BEFORE Trigger\\nExecution", shape=box, fillcolor="#FBFAF7", fontcolor="#16191D", color="#6F94A6"]
            violate [label="RAISE EXCEPTION\\n(Constraint Violated)", shape=box, fillcolor="#F5E6E4", fontcolor="#A8322A", color="#A8322A"]
            rollback [label="Kernel ROLLBACK\\nZero DB Mutation", shape=box, fillcolor="#F5E6E4", fontcolor="#A8322A", color="#A8322A"]

            role -> rbac [label="Allowed", color="#2E6B5E", fontcolor="#2E6B5E"]
            rbac -> tbl [label="Dispatched", color="#2E6B5E", fontcolor="#2E6B5E"]
            tbl -> trigger [label="Intercepted", color="#2E6B5E", fontcolor="#2E6B5E"]
            trigger -> violate [label="Check Failed", color="#A8322A", fontcolor="#A8322A"]
            violate -> rollback [label="Automatic Rollback", color="#A8322A", fontcolor="#A8322A"]
        }}
        """
    st.graphviz_chart(dot_code, width="stretch")


def render_flowchart(role, action_name, status):
    """Bridge function routing directly to native vector Graphviz engine."""
    render_graphviz_flowchart(role, action_name, status)


def render_eca_trigger_dissector(job_key, user_inputs, result=None, active_role="retail_customer", has_access=True):
    """
    Renders an advanced DBMS Event-Condition-Action (ECA) trigger dissector,
    exposing trigger timing, NEW/OLD memory buffers, condition hierarchy, and PL/pgSQL code.
    Dynamically reflects role authorization (allowed vs. disallowed) and ANSI SQL buffer allocation.
    """
    # Determine relation table and operation type from job_key
    if "Profile" in job_key:
        target_table = "customer_profiles"
    elif "Account" in job_key:
        target_table = "customer_accounts"
    elif "Transaction" in job_key:
        target_table = "daily_transactions"
    elif "Loan" in job_key:
        target_table = "loan_applications"
    elif "Fraud" in job_key:
        target_table = "fraud_alerts"
    elif "Audit" in job_key:
        target_table = "audit_log"
    else:
        target_table = "Core Banking Engine"

    if not has_access:
        status = "denied"
    elif result and isinstance(result, dict):
        status = result.get("status", "ready")
    else:
        status = "ready"

    is_success = (status == "success")
    is_denied = (status == "denied")

    # =========================================================================
    # 1. Identify active trigger and architectural properties
    # =========================================================================
    if not has_access:
        active_trigger_key = None
        event_timing = "PRE-PARSING CHECK"
        event_type = "DISPATCH ABORTED"
        sec_mode = "CATALOG RBAC"
        timing_desc = f"PostgreSQL catalog halted query dispatch for role `{active_role}` before execution."
        cond_title = "Tier-1 PostgreSQL RBAC Catalog Check"
        conditions = [
            ("1. Table Privilege Check", f"has_table_privilege('{active_role}', '{target_table}', ...) = FALSE"),
            ("2. Column Grant Bitmask", "Required column privileges revoked or not granted in catalog"),
            ("3. Defense Boundary", "Execution stopped at Tier 1 before triggers or memory buffers are created")
        ]
        action_desc = f"PostgreSQL kernel raised exception 42501 (insufficient_privilege). 0 bytes allocated in RAM, 0 disk I/O, zero state mutations."
        action_badge = "<span style='color: #A8322A; font-weight: 700;'>Access denied</span>"

    elif "Transaction" in job_key and "INSERT" in job_key:
        active_trigger_key = "process_transaction"
        event_timing = "BEFORE"
        event_type = "INSERT"
        target_table = "daily_transactions"
        sec_mode = "SECURITY INVOKER"
        timing_desc = "Fires automatically in PostgreSQL kernel immediately prior to row commitment."
        cond_title = "4-Tier Financial Firewall"
        conditions = [
            ("1. KYC Check", "Sender & receiver kyc_status = 'APPROVED'"),
            ("2. Health Check", "account_status NOT IN ('FROZEN', 'CLOSED')"),
            ("3. Fraud Intelligence", "Zero active fraud_alerts on either account"),
            ("4. Solvency Check", "sender.balance >= NEW.amount")
        ]
        if is_success:
            action_desc = "Atomic balance adjustment committed (Debit sender, Credit receiver); cascaded AFTER trigger to audit_log."
            action_badge = "<span style='color: #2E6B5E; font-weight: 700;'>Transaction committed</span>"
        elif status == "error":
            clean_err = result.get("clean_message", "Constraint Violated") if result else "Constraint Violated"
            action_desc = f"RAISE EXCEPTION executed ({clean_err}); entire transfer aborted via automatic ROLLBACK."
            action_badge = "<span style='color: #A8322A; font-weight: 700;'>Transaction aborted</span>"
        else:
            action_desc = "Ready for execution dispatch to PostgreSQL."
            action_badge = "<span style='color: #9DB0B0; font-weight: 700;'>Not run yet</span>"

    elif "Loan" in job_key and "INSERT" in job_key:
        active_trigger_key = "check_loan_eligibility"
        event_timing = "BEFORE"
        event_type = "INSERT"
        target_table = "loan_applications"
        sec_mode = "SECURITY INVOKER"
        timing_desc = "Fires automatically prior to inserting candidate loan row."
        cond_title = "Credit Qualification & Anti-Stacking"
        conditions = [
            ("1. Applicant KYC", "Applicant kyc_status = 'APPROVED'"),
            ("2. Anti-Stacking Rule", "Zero existing loans in SUBMITTED or UNDERWRITE"),
            ("3. Account Health", "Applicant holds zero FROZEN or CLOSED accounts"),
            ("4. Initial Status", "Initializes applicant status to SUBMITTED")
        ]
        if is_success:
            action_desc = "Loan application inserted in SUBMITTED state for underwriter review."
            action_badge = "<span style='color: #2E6B5E; font-weight: 700;'>Loan registered</span>"
        elif status == "error":
            clean_err = result.get("clean_message", "Eligibility Failed") if result else "Eligibility Failed"
            action_desc = f"RAISE EXCEPTION ({clean_err}); loan creation aborted via ROLLBACK."
            action_badge = "<span style='color: #A8322A; font-weight: 700;'>Application rejected</span>"
        else:
            action_desc = "Ready for loan application dispatch."
            action_badge = "<span style='color: #9DB0B0; font-weight: 700;'>Not run yet</span>"

    elif "Loan" in job_key and "UPDATE" in job_key:
        active_trigger_key = "enforce_loan_workflow"
        event_timing = "BEFORE"
        event_type = "UPDATE"
        target_table = "loan_applications"
        sec_mode = "SECURITY DEFINER"
        timing_desc = "Fires with elevated schema privileges on loan state mutation."
        cond_title = "Workflow State Machine & Role Authority"
        conditions = [
            ("1. Linear Progression", "SUBMITTED -> UNDERWRITE -> APPROVED/REJECTED"),
            ("2. Stage-Skip Block", "Prohibits direct jump from SUBMITTED to APPROVED"),
            ("3. Role Segregation", "Only senior_underwriter to UNDERWRITE; only branch_manager to APPROVE"),
            ("4. Terminal Lock", "APPROVED and REJECTED states are strictly immutable")
        ]
        if is_success:
            action_desc = "State transition committed; cascaded AFTER trigger to audit_log."
            action_badge = "<span style='color: #2E6B5E; font-weight: 700;'>Workflow advanced</span>"
        elif status == "error":
            clean_err = result.get("clean_message", "Workflow Violated") if result else "Workflow Violated"
            action_desc = f"RAISE EXCEPTION ({clean_err}); update aborted via ROLLBACK."
            action_badge = "<span style='color: #A8322A; font-weight: 700;'>Transition rejected</span>"
        else:
            action_desc = "Ready for workflow state transition dispatch."
            action_badge = "<span style='color: #9DB0B0; font-weight: 700;'>Not run yet</span>"

    elif "Account" in job_key and ("UPDATE" in job_key or "Freeze" in job_key or "Close" in job_key or "Balance" in job_key):
        active_trigger_key = "log_audit_event"
        event_timing = "AFTER"
        event_type = "UPDATE"
        target_table = "customer_accounts"
        sec_mode = "SECURITY DEFINER"
        timing_desc = "Fires after account mutation has passed all checks and committed."
        cond_title = "Forensic Change Detection"
        conditions = [
            ("1. Change Detection", "OLD.balance != NEW.balance OR OLD.status != NEW.status"),
            ("2. Context Capture", "Captures CURRENT_USER, timestamp, and account_id"),
            ("3. Privilege Elevation", "SECURITY DEFINER executes as table owner (postgres)"),
            ("4. Append-Only Store", "Writes to tamper-evident audit_log")
        ]
        if is_success:
            action_desc = "Immutable audit entry appended to audit_log table with actor, timestamp, and diff."
            action_badge = "<span style='color: #2E6B5E; font-weight: 700;'>Audit entry written</span>"
        elif status == "error":
            clean_err = result.get("clean_message", "Write Failed") if result else "Write Failed"
            action_desc = f"Database mutation failed ({clean_err}); ROLLBACK issued."
            action_badge = "<span style='color: #A8322A; font-weight: 700;'>Mutation failed</span>"
        else:
            action_desc = "Awaiting account mutation to generate forensic trace."
            action_badge = "<span style='color: #9DB0B0; font-weight: 700;'>Not run yet</span>"

    elif "Fraud" in job_key and "UPDATE" in job_key:
        active_trigger_key = "log_audit_event"
        event_timing = "AFTER"
        event_type = "UPDATE"
        target_table = "fraud_alerts"
        sec_mode = "SECURITY DEFINER"
        timing_desc = "Fires after fraud status change to append forensic record."
        cond_title = "Risk Status Audit Detection"
        conditions = [
            ("1. Status Mutation", "OLD.alert_status != NEW.alert_status"),
            ("2. Actor Verification", "Captures authenticated analyst role"),
            ("3. Privilege Elevation", "SECURITY DEFINER elevation to record audit row"),
            ("4. Tamper Resistance", "Append-only storage in audit_log")
        ]
        if is_success:
            action_desc = "Fraud status update committed and recorded to audit_log."
            action_badge = "<span style='color: #2E6B5E; font-weight: 700;'>Alert change audited</span>"
        elif status == "error":
            action_desc = "Update aborted via ROLLBACK."
            action_badge = "<span style='color: #A8322A; font-weight: 700;'>Update failed</span>"
        else:
            action_desc = "Awaiting fraud status update."
            action_badge = "<span style='color: #9DB0B0; font-weight: 700;'>Not run yet</span>"

    elif "Account" in job_key and "INSERT" in job_key:
        active_trigger_key = None
        event_timing = "BEFORE INSERT"
        event_type = "INSERT"
        target_table = "customer_accounts"
        sec_mode = "SECURITY INVOKER"
        timing_desc = "Direct PostgreSQL schema validation and relation insertion."
        cond_title = "Relational Integrity & Primary Key Constraints"
        conditions = [
            ("1. Profile FK Check", "profile_id exists in customer_profiles"),
            ("2. Primary Key Uniqueness", "account_id is unique across customer_accounts"),
            ("3. Positive Balance", "balance >= 0 (CHECK constraint)"),
            ("4. Initial Status", "Default account_status set to 'ACTIVE'")
        ]
        if is_success:
            action_desc = "Account created and committed to storage heap."
            action_badge = "<span style='color: #2E6B5E; font-weight: 700;'>Account created</span>"
        elif status == "error":
            clean_err = result.get("clean_message", "Insert Failed") if result else "Insert Failed"
            action_desc = f"Account creation aborted ({clean_err})."
            action_badge = "<span style='color: #A8322A; font-weight: 700;'>Insert failed</span>"
        else:
            action_desc = "Ready for new account insertion dispatch."
            action_badge = "<span style='color: #9DB0B0; font-weight: 700;'>Not run yet</span>"

    elif "Profile" in job_key and "UPDATE" in job_key:
        active_trigger_key = None
        event_timing = "ON UPDATE"
        event_type = "UPDATE"
        target_table = "customer_profiles"
        sec_mode = "SECURITY INVOKER"
        timing_desc = "Column-level granular UPDATE on non-sensitive contact fields."
        cond_title = "Column-Level RBAC & Profile Verification"
        conditions = [
            ("1. Column RBAC", f"has_column_privilege('{active_role}', 'customer_profiles', 'full_name', 'UPDATE') = TRUE"),
            ("2. Target Profile", "profile_id exists in customer_profiles"),
            ("3. Identity Freeze", "kyc_status remains immutable to staff")
        ]
        if is_success:
            action_desc = "Profile contact fields updated on disk."
            action_badge = "<span style='color: #2E6B5E; font-weight: 700;'>Profile updated</span>"
        elif status == "error":
            clean_err = result.get("clean_message", "Update Failed") if result else "Update Failed"
            action_desc = f"Profile update aborted ({clean_err})."
            action_badge = "<span style='color: #A8322A; font-weight: 700;'>Update failed</span>"
        else:
            action_desc = "Ready for profile update dispatch."
            action_badge = "<span style='color: #9DB0B0; font-weight: 700;'>Not run yet</span>"

    elif "Fraud" in job_key and "INSERT" in job_key:
        active_trigger_key = None
        event_timing = "ON INSERT"
        event_type = "INSERT"
        target_table = "fraud_alerts"
        sec_mode = "SECURITY INVOKER"
        timing_desc = "Financial crime intelligence ingestion into compliance records."
        cond_title = "Fraud Alert Logging Rules"
        conditions = [
            ("1. Table Privilege", f"has_table_privilege('{active_role}', 'fraud_alerts', 'INSERT') = TRUE"),
            ("2. Account Verification", "account_id exists in customer_accounts"),
            ("3. Auto-Flagging", "Initial alert_status initialized to 'OPEN'")
        ]
        if is_success:
            action_desc = "Fraud alert registered; initiates automated transfer freeze check."
            action_badge = "<span style='color: #2E6B5E; font-weight: 700;'>Alert logged</span>"
        elif status == "error":
            clean_err = result.get("clean_message", "Logging Failed") if result else "Logging Failed"
            action_desc = f"Alert insertion aborted ({clean_err})."
            action_badge = "<span style='color: #A8322A; font-weight: 700;'>Logging failed</span>"
        else:
            action_desc = "Ready to log fraud alert."
            action_badge = "<span style='color: #9DB0B0; font-weight: 700;'>Not run yet</span>"

    else:
        # Read-only operation (SELECT)
        active_trigger_key = None
        event_timing = "ON DISPATCH"
        event_type = "SELECT"
        sec_mode = "SECURITY INVOKER"
        timing_desc = "Direct execution via PostgreSQL query engine (Shared Buffer Pool Scan)."
        cond_title = "Tier-1 RBAC Authorization Catalog"
        conditions = [
            ("1. Catalog Check", f"has_table_privilege('{active_role}', '{target_table}', 'SELECT') = TRUE"),
            ("2. MVCC Snapshot", "Consistent Read Snapshot (Committed transaction isolation)"),
            ("3. Shared Buffer Cache", "Tuples streamed from PostgreSQL memory cache to client cursor"),
            ("4. Zero Trigger Overhead", "Bypasses PL/pgSQL procedural interpreter entirely")
        ]
        if is_success:
            action_desc = "Query executed directly; tuples streamed from buffer pool without mutation."
            action_badge = "<span style='color: #2E6B5E; font-weight: 700;'>Query executed</span>"
        elif status == "error":
            clean_err = result.get("clean_message", "Query Error") if result else "Query Error"
            action_desc = f"Execution failed: {clean_err}"
            action_badge = "<span style='color: #A8322A; font-weight: 700;'>Execution failed</span>"
        else:
            action_desc = "Ready for direct SQL dispatch."
            action_badge = "<span style='color: #9DB0B0; font-weight: 700;'>Not run yet</span>"

    st.markdown("""
    <div class="eca-hero-container">
        <div class="eca-hero-pretitle">
            Event, Condition, Action
        </div>
        <div class="eca-hero-title">
            How a trigger fires
        </div>
        <div class="eca-hero-desc">
            In formal database theory, a trigger is an active database rule structured into three formal primitives:
            an <b>Event</b> that invokes execution, <b>Conditions</b> evaluated against memory buffers, and an atomic <b>Action</b>.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ECA 3-Column Visual
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"""
        <div class="eca-col-card">
            <div class="eca-col-header event">
                1. Event
            </div>
            <div class="eca-col-title">
                {event_timing} {event_type}
            </div>
            <div class="eca-col-content">
                <div><b>Target Table:</b> <code style="color: #A8322A;">{target_table}</code></div>
                <div><b>Granularity:</b> <code>FOR EACH ROW</code></div>
                <div><b>Execution Mode:</b> <code style="color: #4B525B;">{sec_mode}</code></div>
            </div>
            <div class="eca-col-footer">
                {timing_desc}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        cond_status_badge = "Verified" if is_success else ("Violated" if status == "error" else ("Denied" if is_denied else "Awaiting run"))
        cond_items_html = "".join([f"<div><b>{cname}:</b> <code>{cdesc}</code></div>" for cname, cdesc in conditions])
        st.markdown(f"""
        <div class="eca-col-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div class="eca-col-header conditions">
                    2. Condition
                </div>
                <span style="font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 10px; background: #ECEBE5; color: #2E6B5E;">{cond_status_badge}</span>
            </div>
            <div class="eca-col-title">
                {cond_title}
            </div>
            <div class="eca-col-content">
                {cond_items_html}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="eca-col-card">
            <div class="eca-col-header action">
                3. Action
            </div>
            <div style="font-size: 14px; margin-top: 6px;">
                {action_badge}
            </div>
            <div class="eca-col-content">
                {action_desc}
            </div>
            <div class="eca-col-footer">
                ACID Atomicity: Zero partial writes guaranteed on error.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # =========================================================================
    # 2. Memory Buffer Inspector (NEW vs OLD transition variables)
    # =========================================================================
    if not has_access:
        st.markdown("#### In-Memory Buffer Inspector: Transition Variables (`NEW` vs `OLD`)")
        st.markdown(f"""
        <div class="buffer-inspector-box denied">
            <div class="buffer-inspector-title">
                RBAC authorization denied. In-memory transition buffers were never allocated.
            </div>
            <div class="buffer-inspector-desc">
                PostgreSQL evaluates role privileges at <b>Tier 1 (Parser & System Catalog Stage)</b>. 
                Because active role <code style="color: #A8322A;">{active_role}</code> does not hold the required privilege on <code style="color: #4B525B;">{target_table}</code>, 
                PostgreSQL halts execution immediately with error <code>42501 (insufficient_privilege)</code>.
                <br><br>
                <b>Memory Allocation Abort:</b> In PostgreSQL engine internals, memory for <code>NEW</code> and <code>OLD</code> pseudo-record variables is only allocated <i>after</i> Tier-1 RBAC authorization succeeds. 
                Because authorization was denied, zero heap pages were retrieved into the Shared Buffer Pool, and no backend tuple buffers were created.
            </div>
        </div>
        """, unsafe_allow_html=True)

        denied_rows = [
            {"Attribute": "Execution Stage", "Memory Buffer State": "Halted at Tier 1 (PostgreSQL System Catalog)", "Role": "Access Verification Firewall", "Status": "Aborted (42501)"},
            {"Attribute": "OLD Buffer (Heap Disk)", "Memory Buffer State": "NULL (Read access blocked: Disk page not loaded into RAM)", "Role": "Pre-Mutation Heap State", "Status": "Unallocated"},
            {"Attribute": "NEW Buffer (Candidate Row)", "Memory Buffer State": "NULL (Memory allocation aborted before backend slot creation)", "Role": "Proposed Row State", "Status": "Unallocated"},
            {"Attribute": "Procedural Trigger Engine", "Memory Buffer State": "BYPASSED (Short-circuited at catalog level)", "Role": "Business Rule Enforcement", "Status": "Not reached"},
            {"Attribute": "WAL / Disk I/O", "Memory Buffer State": "0 bytes written (Zero side effects)", "Role": "ACID Durability", "Status": "Protected"}
        ]
        st.dataframe(pd.DataFrame(denied_rows), width="stretch", hide_index=True)

    elif "SELECT" in job_key:
        st.markdown("#### In-Memory Buffer Inspector: Shared Buffer Pool & Read-Cursor Stream")
        st.markdown(f"""
        <div class="buffer-inspector-box select">
            <div class="buffer-inspector-title">
                Read-Only (SELECT) Query Memory Architecture
            </div>
            <div class="buffer-inspector-desc">
                In ANSI SQL and PostgreSQL storage architecture, transition variables (<code>NEW</code> and <code>OLD</code>) exist <b>solely during row-mutating operations (<code>INSERT</code>, <code>UPDATE</code>, <code>DELETE</code>)</b>.
                <br><br>
                For read queries, PostgreSQL's executor allocates a <b>TupleTableSlot (Virtual Heap Slot)</b> in private backend memory. 
                Committed table pages are retrieved from the <b>PostgreSQL Shared Buffer Pool (Disk Cache)</b> under a non-blocking <code>AccessShareLock</code>, 
                and rows are streamed directly to the client cursor without allocating transition record buffers or invoking procedural triggers.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if "Audit" in job_key:
            select_rows = [
                {"Column Name": "log_id", "Data Type": "BIGINT", "Buffer Allocation": "Shared Buffer Pool -> Client Cursor", "Mutation Mode": "Read-Only (OLD/NEW: NULL)", "Description": "Forensic audit sequence primary key"},
                {"Column Name": "changed_at", "Data Type": "TIMESTAMPTZ", "Buffer Allocation": "Shared Buffer Pool -> Client Cursor", "Mutation Mode": "Read-Only (OLD/NEW: NULL)", "Description": "Exact timestamp of database mutation"},
                {"Column Name": "changed_by", "Data Type": "VARCHAR(50)", "Buffer Allocation": "Shared Buffer Pool -> Client Cursor", "Mutation Mode": "Read-Only (OLD/NEW: NULL)", "Description": "Authenticated database actor role stamp"},
                {"Column Name": "table_name", "Data Type": "VARCHAR(50)", "Buffer Allocation": "Shared Buffer Pool -> Client Cursor", "Mutation Mode": "Read-Only (OLD/NEW: NULL)", "Description": "Target relation mutated"},
                {"Column Name": "record_id", "Data Type": "BIGINT", "Buffer Allocation": "Shared Buffer Pool -> Client Cursor", "Mutation Mode": "Read-Only (OLD/NEW: NULL)", "Description": "Mutated row identifier"},
                {"Column Name": "account_id", "Data Type": "BIGINT", "Buffer Allocation": "Shared Buffer Pool -> Client Cursor", "Mutation Mode": "Read-Only (OLD/NEW: NULL)", "Description": "Associated customer account"},
                {"Column Name": "action", "Data Type": "VARCHAR(20)", "Buffer Allocation": "Shared Buffer Pool -> Client Cursor", "Mutation Mode": "Read-Only (OLD/NEW: NULL)", "Description": "DML operation type (INSERT/UPDATE)"},
                {"Column Name": "old_value", "Data Type": "TEXT", "Buffer Allocation": "Shared Buffer Pool -> Client Cursor", "Mutation Mode": "Read-Only (OLD/NEW: NULL)", "Description": "Pre-mutation serialized state snapshot"},
                {"Column Name": "new_value", "Data Type": "TEXT", "Buffer Allocation": "Shared Buffer Pool -> Client Cursor", "Mutation Mode": "Read-Only (OLD/NEW: NULL)", "Description": "Post-mutation serialized state snapshot"}
            ]
        elif "Account" in job_key:
            select_rows = [
                {"Column Name": "account_id", "Data Type": "BIGINT", "Buffer Allocation": "Shared Buffer Pool -> Client Cursor", "Mutation Mode": "Read-Only (OLD/NEW: NULL)", "Description": "Unique account primary key"},
                {"Column Name": "profile_id", "Data Type": "BIGINT", "Buffer Allocation": "Shared Buffer Pool -> Client Cursor", "Mutation Mode": "Read-Only (OLD/NEW: NULL)", "Description": "Foreign key to customer profile"},
                {"Column Name": "balance", "Data Type": "NUMERIC(15,2)", "Buffer Allocation": "Shared Buffer Pool -> Client Cursor", "Mutation Mode": "Read-Only (OLD/NEW: NULL)", "Description": "Current ledger balance on disk"},
                {"Column Name": "account_status", "Data Type": "VARCHAR(20)", "Buffer Allocation": "Shared Buffer Pool -> Client Cursor", "Mutation Mode": "Read-Only (OLD/NEW: NULL)", "Description": "Operational state (ACTIVE/FROZEN/CLOSED)"},
                {"Column Name": "account_type", "Data Type": "VARCHAR(20)", "Buffer Allocation": "Shared Buffer Pool -> Client Cursor", "Mutation Mode": "Read-Only (OLD/NEW: NULL)", "Description": "Product type (SAVINGS/CURRENT/DEPOSITS)"},
                {"Column Name": "created_at", "Data Type": "TIMESTAMPTZ", "Buffer Allocation": "Shared Buffer Pool -> Client Cursor", "Mutation Mode": "Read-Only (OLD/NEW: NULL)", "Description": "Account origination timestamp"}
            ]
        elif "Loan" in job_key:
            select_rows = [
                {"Column Name": "application_id", "Data Type": "BIGINT", "Buffer Allocation": "Shared Buffer Pool -> Client Cursor", "Mutation Mode": "Read-Only (OLD/NEW: NULL)", "Description": "Loan file primary key"},
                {"Column Name": "profile_id", "Data Type": "BIGINT", "Buffer Allocation": "Shared Buffer Pool -> Client Cursor", "Mutation Mode": "Read-Only (OLD/NEW: NULL)", "Description": "Borrower profile foreign key"},
                {"Column Name": "requested_amount", "Data Type": "NUMERIC(15,2)", "Buffer Allocation": "Shared Buffer Pool -> Client Cursor", "Mutation Mode": "Read-Only (OLD/NEW: NULL)", "Description": "Principal loan amount requested"},
                {"Column Name": "approval_status", "Data Type": "VARCHAR(20)", "Buffer Allocation": "Shared Buffer Pool -> Client Cursor", "Mutation Mode": "Read-Only (OLD/NEW: NULL)", "Description": "Workflow state (SUBMITTED/UNDERWRITE/APPROVED/REJECTED)"},
                {"Column Name": "application_date", "Data Type": "TIMESTAMPTZ", "Buffer Allocation": "Shared Buffer Pool -> Client Cursor", "Mutation Mode": "Read-Only (OLD/NEW: NULL)", "Description": "Intake timestamp"}
            ]
        else: # Transactions SELECT
            select_rows = [
                {"Column Name": "transaction_id", "Data Type": "BIGINT", "Buffer Allocation": "Shared Buffer Pool -> Client Cursor", "Mutation Mode": "Read-Only (OLD/NEW: NULL)", "Description": "Transaction ledger primary key"},
                {"Column Name": "sender_id", "Data Type": "BIGINT", "Buffer Allocation": "Shared Buffer Pool -> Client Cursor", "Mutation Mode": "Read-Only (OLD/NEW: NULL)", "Description": "Originating debtor account"},
                {"Column Name": "receiver_id", "Data Type": "BIGINT", "Buffer Allocation": "Shared Buffer Pool -> Client Cursor", "Mutation Mode": "Read-Only (OLD/NEW: NULL)", "Description": "Receiving creditor account"},
                {"Column Name": "amount", "Data Type": "NUMERIC(15,2)", "Buffer Allocation": "Shared Buffer Pool -> Client Cursor", "Mutation Mode": "Read-Only (OLD/NEW: NULL)", "Description": "Transfer amount debited/credited"},
                {"Column Name": "transaction_type", "Data Type": "VARCHAR(20)", "Buffer Allocation": "Shared Buffer Pool -> Client Cursor", "Mutation Mode": "Read-Only (OLD/NEW: NULL)", "Description": "Payment clearing rail (INTERNAL/ACH/WIRE)"},
                {"Column Name": "transaction_date", "Data Type": "TIMESTAMPTZ", "Buffer Allocation": "Shared Buffer Pool -> Client Cursor", "Mutation Mode": "Read-Only (OLD/NEW: NULL)", "Description": "Transfer timestamp"}
            ]
        st.dataframe(pd.DataFrame(select_rows), width="stretch", hide_index=True)

    else:
        # Row mutation (INSERT / UPDATE)
        st.markdown("#### In-Memory Buffer Inspector: Transition Variables (`NEW` vs `OLD`)")
        st.markdown("""
        In PostgreSQL PL/pgSQL, row triggers receive two special pseudo-record variables in memory:
        - **`NEW`**: Holds the candidate row being inserted or the proposed post-update state.
        - **`OLD`**: Holds the pre-existing database row (or `NULL` during `INSERT` operations).
        """)

        buffer_rows = []
        if "Transaction" in job_key and "INSERT" in job_key:
            s_id = user_inputs[0] if user_inputs and len(user_inputs) > 0 and str(user_inputs[0]).isdigit() else "101"
            r_id = user_inputs[1] if user_inputs and len(user_inputs) > 1 and str(user_inputs[1]).isdigit() else "102"
            amt = f"${float(user_inputs[2]):,.2f}" if user_inputs and len(user_inputs) > 2 and str(user_inputs[2]).replace('.', '', 1).isdigit() else "$500.00"
            tx_type = user_inputs[3] if user_inputs and len(user_inputs) > 3 and isinstance(user_inputs[3], str) else "INTERNAL"

            buffer_rows = [
                {"Attribute": "sender_id", "OLD Buffer (Pre-Mutation)": "NULL (Does not exist yet)", "NEW Buffer (Candidate Row)": f"{s_id}", "Role": "Sender Account ID"},
                {"Attribute": "receiver_id", "OLD Buffer (Pre-Mutation)": "NULL (Does not exist yet)", "NEW Buffer (Candidate Row)": f"{r_id}", "Role": "Receiver Account ID"},
                {"Attribute": "amount", "OLD Buffer (Pre-Mutation)": "NULL (Does not exist yet)", "NEW Buffer (Candidate Row)": f"{amt}", "Role": "Transfer Amount"},
                {"Attribute": "transaction_type", "OLD Buffer (Pre-Mutation)": "NULL (Does not exist yet)", "NEW Buffer (Candidate Row)": f"{tx_type}", "Role": "Transfer Protocol"},
                {"Attribute": "transaction_date", "OLD Buffer (Pre-Mutation)": "NULL (Does not exist yet)", "NEW Buffer (Candidate Row)": "CURRENT_TIMESTAMP", "Role": "System Clock"}
            ]
        elif "Loan" in job_key and "INSERT" in job_key:
            prof_val = user_inputs[0] if user_inputs and len(user_inputs) > 0 and str(user_inputs[0]).isdigit() else "101"
            amt_val = f"${float(user_inputs[1]):,.2f}" if user_inputs and len(user_inputs) > 1 and str(user_inputs[1]).replace('.', '', 1).isdigit() else "$25,000.00"
            buffer_rows = [
                {"Attribute": "profile_id", "OLD Buffer (Pre-Mutation)": "NULL (Does not exist yet)", "NEW Buffer (Candidate Row)": f"{prof_val}", "Role": "Applicant Profile Foreign Key"},
                {"Attribute": "requested_amount", "OLD Buffer (Pre-Mutation)": "NULL (Does not exist yet)", "NEW Buffer (Candidate Row)": f"{amt_val}", "Role": "Principal Amount Requested"},
                {"Attribute": "approval_status", "OLD Buffer (Pre-Mutation)": "NULL (Does not exist yet)", "NEW Buffer (Candidate Row)": "'SUBMITTED' (Initialized by Trigger)", "Role": "Initial Workflow State"},
                {"Attribute": "application_date", "OLD Buffer (Pre-Mutation)": "NULL (Does not exist yet)", "NEW Buffer (Candidate Row)": "CURRENT_TIMESTAMP", "Role": "Intake System Clock"}
            ]
        elif "Loan" in job_key and "UPDATE" in job_key:
            valid_loan_statuses = {"UNDERWRITE", "APPROVED", "REJECTED", "SUBMITTED"}
            new_status = "UNDERWRITE"
            prof_id = "101"

            if user_inputs and len(user_inputs) > 0:
                val0 = str(user_inputs[0]).strip().upper()
                if val0 in valid_loan_statuses:
                    new_status = val0
                    prof_id = str(user_inputs[1]) if len(user_inputs) > 1 and str(user_inputs[1]).isdigit() else "101"
                elif len(user_inputs) > 1 and str(user_inputs[1]).strip().upper() in valid_loan_statuses:
                    new_status = str(user_inputs[1]).strip().upper()
                    prof_id = str(user_inputs[0]) if str(user_inputs[0]).isdigit() else "101"
                else:
                    prof_id = str(user_inputs[0]) if str(user_inputs[0]).isdigit() else "101"
                    new_status = "UNDERWRITE"

            buffer_rows = [
                {"Attribute": "profile_id", "OLD Buffer (Pre-Mutation)": f"{prof_id}", "NEW Buffer (Candidate Row)": f"{prof_id}", "Role": "Applicant Profile Identifier"},
                {"Attribute": "approval_status", "OLD Buffer (Pre-Mutation)": "SUBMITTED", "NEW Buffer (Candidate Row)": f"{new_status}", "Role": "Workflow State Transition"},
                {"Attribute": "updated_at", "OLD Buffer (Pre-Mutation)": "(Timestamp on disk)", "NEW Buffer (Candidate Row)": "CURRENT_TIMESTAMP", "Role": "Mutation Timestamp"}
            ]
        elif "Account" in job_key and "INSERT" in job_key:
            acc_id = str(user_inputs[0]) if user_inputs and len(user_inputs) > 0 and str(user_inputs[0]).isdigit() else "107"
            prof_id = str(user_inputs[1]) if user_inputs and len(user_inputs) > 1 and str(user_inputs[1]).isdigit() else "101"
            init_bal = f"${float(user_inputs[2]):,.2f}" if user_inputs and len(user_inputs) > 2 and str(user_inputs[2]).replace('.', '', 1).isdigit() else "$1,000.00"
            acc_type = str(user_inputs[3]) if user_inputs and len(user_inputs) > 3 and isinstance(user_inputs[3], str) else "SAVINGS"
            buffer_rows = [
                {"Attribute": "account_id", "OLD Buffer (Pre-Mutation)": "NULL (Does not exist yet)", "NEW Buffer (Candidate Row)": f"{acc_id}", "Role": "Primary Key"},
                {"Attribute": "profile_id", "OLD Buffer (Pre-Mutation)": "NULL (Does not exist yet)", "NEW Buffer (Candidate Row)": f"{prof_id}", "Role": "Foreign Key (Profile)"},
                {"Attribute": "balance", "OLD Buffer (Pre-Mutation)": "NULL (Does not exist yet)", "NEW Buffer (Candidate Row)": f"{init_bal}", "Role": "Initial Opening Deposit"},
                {"Attribute": "account_type", "OLD Buffer (Pre-Mutation)": "NULL (Does not exist yet)", "NEW Buffer (Candidate Row)": f"{acc_type}", "Role": "Product Tier"},
                {"Attribute": "account_status", "OLD Buffer (Pre-Mutation)": "NULL (Does not exist yet)", "NEW Buffer (Candidate Row)": "'ACTIVE' (Default)", "Role": "Account Status"},
                {"Attribute": "created_at", "OLD Buffer (Pre-Mutation)": "NULL (Does not exist yet)", "NEW Buffer (Candidate Row)": "CURRENT_TIMESTAMP", "Role": "Origination Timestamp"}
            ]
        elif "Profile" in job_key and "UPDATE" in job_key:
            is_text_name = user_inputs and len(user_inputs) > 0 and not str(user_inputs[0]).isdigit()
            new_name = str(user_inputs[0]) if is_text_name else "Alice Walker Updated"
            is_phone = user_inputs and len(user_inputs) > 1 and ("+" in str(user_inputs[1]) or "-" in str(user_inputs[1]))
            new_phone = str(user_inputs[1]) if is_phone else "+1-555-0199"
            prof_id = str(user_inputs[2]) if user_inputs and len(user_inputs) > 2 and str(user_inputs[2]).isdigit() else "101"
            buffer_rows = [
                {"Attribute": "profile_id", "OLD Buffer (Pre-Mutation)": f"{prof_id}", "NEW Buffer (Candidate Row)": f"{prof_id}", "Role": "Target Profile Key"},
                {"Attribute": "full_name", "OLD Buffer (Pre-Mutation)": "(Current name on disk)", "NEW Buffer (Candidate Row)": f"{new_name}", "Role": "Contact Field (Column RBAC)"},
                {"Attribute": "phone_number", "OLD Buffer (Pre-Mutation)": "(Current phone on disk)", "NEW Buffer (Candidate Row)": f"{new_phone}", "Role": "Contact Field (Column RBAC)"},
                {"Attribute": "kyc_status", "OLD Buffer (Pre-Mutation)": "APPROVED", "NEW Buffer (Candidate Row)": "APPROVED (Immutable to Staff)", "Role": "Protected Identity Status"}
            ]
        elif "Fraud" in job_key and "INSERT" in job_key:
            acc_id = str(user_inputs[0]) if user_inputs and len(user_inputs) > 0 and str(user_inputs[0]).isdigit() else "105"
            risk_reason = str(user_inputs[1]) if user_inputs and len(user_inputs) > 1 and str(user_inputs[1]).strip() else "Rapid multi-jurisdiction IP velocity"
            buffer_rows = [
                {"Attribute": "alert_id", "OLD Buffer (Pre-Mutation)": "NULL (Does not exist yet)", "NEW Buffer (Candidate Row)": "NEXTVAL('fraud_alerts_alert_id_seq')", "Role": "Sequence Primary Key"},
                {"Attribute": "account_id", "OLD Buffer (Pre-Mutation)": "NULL (Does not exist yet)", "NEW Buffer (Candidate Row)": f"{acc_id}", "Role": "Foreign Key (Account)"},
                {"Attribute": "risk_reason", "OLD Buffer (Pre-Mutation)": "NULL (Does not exist yet)", "NEW Buffer (Candidate Row)": f"{risk_reason}", "Role": "Risk Indicator Reason"},
                {"Attribute": "alert_status", "OLD Buffer (Pre-Mutation)": "NULL (Does not exist yet)", "NEW Buffer (Candidate Row)": "'OPEN'", "Role": "Investigation Status"},
                {"Attribute": "created_at", "OLD Buffer (Pre-Mutation)": "NULL (Does not exist yet)", "NEW Buffer (Candidate Row)": "CURRENT_TIMESTAMP", "Role": "Detection Timestamp"}
            ]
        elif "Account" in job_key and ("Balance" in job_key or "UPDATE" in job_key or "Freeze" in job_key or "Close" in job_key):
            acc_id = "101"
            new_val = "5000.00"
            target_field = "balance"

            if "Close" in job_key:
                target_field = "account_status"
                new_val = "CLOSED"
                acc_id = str(user_inputs[0]) if user_inputs and len(user_inputs) > 0 and str(user_inputs[0]).isdigit() else "101"
            elif "Freeze" in job_key:
                target_field = "account_status"
                new_val = str(user_inputs[0]) if user_inputs and len(user_inputs) > 0 and str(user_inputs[0]) in ("FROZEN", "ACTIVE") else "FROZEN"
                acc_id = str(user_inputs[1]) if user_inputs and len(user_inputs) > 1 and str(user_inputs[1]).isdigit() else "101"
            else:
                # Balance update
                target_field = "balance"
                new_val = f"${float(user_inputs[0]):,.2f}" if user_inputs and len(user_inputs) > 0 and str(user_inputs[0]).replace('.', '', 1).isdigit() else "$7,500.00"
                acc_id = str(user_inputs[1]) if user_inputs and len(user_inputs) > 1 and str(user_inputs[1]).isdigit() else "101"

            old_display = "ACTIVE" if target_field == "account_status" else "(Current balance on disk)"
            buffer_rows = [
                {"Attribute": "account_id", "OLD Buffer (Pre-Mutation)": f"{acc_id}", "NEW Buffer (Candidate Row)": f"{acc_id}", "Role": "Primary Key"},
                {"Attribute": target_field, "OLD Buffer (Pre-Mutation)": old_display, "NEW Buffer (Candidate Row)": f"{new_val}", "Role": "Target Mutation Field"}
            ]
        elif "Fraud" in job_key and "UPDATE" in job_key:
            valid_fraud_statuses = {"UNDER_INVESTIGATION", "FALSE_POSITIVE", "OPEN", "RESOLVED"}
            new_status = str(user_inputs[0]) if user_inputs and len(user_inputs) > 0 and str(user_inputs[0]) in valid_fraud_statuses else "UNDER_INVESTIGATION"
            acc_id = str(user_inputs[1]) if user_inputs and len(user_inputs) > 1 and str(user_inputs[1]).isdigit() else "105"
            buffer_rows = [
                {"Attribute": "account_id", "OLD Buffer (Pre-Mutation)": f"{acc_id}", "NEW Buffer (Candidate Row)": f"{acc_id}", "Role": "Foreign Key"},
                {"Attribute": "alert_status", "OLD Buffer (Pre-Mutation)": "OPEN", "NEW Buffer (Candidate Row)": f"{new_status}", "Role": "Fraud Case Status"}
            ]

        if buffer_rows:
            df_buffer = pd.DataFrame(buffer_rows)
            st.dataframe(df_buffer, width="stretch", hide_index=True)



