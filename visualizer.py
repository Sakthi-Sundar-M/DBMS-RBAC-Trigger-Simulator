import streamlit as st
import streamlit.components.v1 as components
from streamlit_mermaid import st_mermaid
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
                "failed_text": "KYC verification failed — unverified profile",
                "blocked_text": "KYC verification pending",
            },
            {
                "id": "account_status",
                "title": "Account Status Check",
                "passed_text": "Account status: active (not frozen)",
                "failed_text": "Account status check failed — account is frozen or closed",
                "blocked_text": "Account status check skipped",
            },
            {
                "id": "fraud_check",
                "title": "Fraud Investigation Check",
                "passed_text": "Fraud check passed — no alerts on file",
                "failed_text": "Fraud check failed — alert on file",
                "blocked_text": "Fraud check skipped",
            },
            {
                "id": "execution",
                "title": "Transfer Execution",
                "passed_text": "Transaction committed: Funds transferred",
                "failed_text": "Transaction blocked — insufficient funds or transfer error",
                "blocked_text": "Transaction blocked before insert",
            }
        ]

        if status == "success":
            for s in steps:
                s["state"] = "passed"
                s["display_text"] = s["passed_text"]
        elif status == "denied":
            steps[0]["state"] = "failed"
            steps[0]["display_text"] = "RBAC Authorization Denied: Role lacks INSERT privilege"
            for s in steps[1:]:
                s["state"] = "blocked"
                s["display_text"] = s["blocked_text"]
        else:
            if error_code == "KYC_CHECK_FAILED":
                steps[0]["state"] = "failed"
                steps[0]["display_text"] = f"KYC check failed — {result.get('clean_message', 'unverified profile')}"
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
                steps[1]["display_text"] = f"Account status check failed — {result.get('clean_message', 'frozen/closed account')}"
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
                steps[2]["display_text"] = "Fraud check failed — alert on file"
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
                steps[3]["display_text"] = f"Transfer blocked — {result.get('clean_message', 'insufficient balance')}"
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
                "blocked_text": "Account status check skipped",
            },
            {
                "id": "fraud_check",
                "title": "Fraud Risk Assessment",
                "passed_text": "Fraud assessment clean: no active fraud investigations",
                "failed_text": "Fraud alert detected on customer account",
                "blocked_text": "Fraud assessment skipped",
            },
            {
                "id": "stacking",
                "title": "Loan Stacking Prevention",
                "passed_text": "No concurrent loans under review",
                "failed_text": "Loan stacking blocked — customer already has a pending application",
                "blocked_text": "Loan stacking check skipped",
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
            steps[0]["display_text"] = "RBAC Authorization Denied: Role lacks INSERT privilege"
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
                "failed_text": "State transition violation: skipped stage or backward transition",
                "blocked_text": "State transition skipped",
            },
            {
                "id": "risk_check",
                "title": "Underwriting Risk & Fraud Assessment",
                "passed_text": "Account & fraud risk clean at underwriting",
                "failed_text": "Approval blocked: active fraud alert or frozen account",
                "blocked_text": "Risk assessment skipped",
            },
            {
                "id": "audit_commit",
                "title": "Workflow Update & Audit Log",
                "passed_text": "Workflow status committed & audit event logged",
                "failed_text": "Workflow update blocked before commit",
                "blocked_text": "Audit event skipped",
            }
        ]

        if status == "success":
            for s in steps:
                s["state"] = "passed"
                s["display_text"] = s["passed_text"]
        elif status == "denied":
            steps[0]["state"] = "failed"
            steps[0]["display_text"] = "RBAC Authorization Denied: Role lacks UPDATE privilege on approval_status"
            for s in steps[1:]:
                s["state"] = "blocked"
                s["display_text"] = s["blocked_text"]
        else:
            if error_code == "WORKFLOW_ROLE_DENIED":
                steps[0]["state"] = "failed"
                steps[0]["display_text"] = f"Access Denied — {result.get('clean_message', 'unauthorized role')}"
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
                "title": "PostgreSQL RBAC Authorization",
                "passed_text": "Role authorization verified via information_schema",
                "failed_text": "Access Denied by PostgreSQL RBAC",
                "blocked_text": "Authorization pending",
            },
            {
                "id": "mutation",
                "title": "Table Constraint & State Update",
                "passed_text": "Data constraints verified & state updated",
                "failed_text": "Data validation or constraint failure",
                "blocked_text": "Update skipped",
            },
            {
                "id": "audit",
                "title": "Audit Log Trigger (log_audit_event)",
                "passed_text": "Audit event captured silently via SECURITY DEFINER",
                "failed_text": "Audit logging failed",
                "blocked_text": "Audit logging skipped",
            }
        ]

        if status == "success":
            for s in steps:
                s["state"] = "passed"
                s["display_text"] = s["passed_text"]
        elif status == "denied":
            steps[0]["state"] = "failed"
            steps[0]["display_text"] = "Access Denied: Insufficient role privileges"
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
    Renders the Live Trace UI card styled exactly like the attached reference image:
    Dark navy background, rounded step items with distinct icons (✓, ✕, -),
    and arrow connectors indicating workflow pipeline execution.
    Renders directly via st.html() to avoid markdown code-block conversion.
    """
    steps = parse_trigger_steps(job_name, result)

    html_cards = []
    for idx, step in enumerate(steps):
        state = step["state"]
        text = html.escape(step["display_text"])

        if state == "passed":
            icon = "✓"
            icon_color = "#10b981"
            card_bg = "#1e293b"
            text_color = "#f8fafc"
            badge_text = "PASSED"
            badge_style = "color: #10b981; background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.3);"
            card_border = "border: 1px solid rgba(16, 185, 129, 0.25);"
        elif state == "failed":
            icon = "✕"
            icon_color = "#ef4444"
            card_bg = "#1e293b"
            text_color = "#f8fafc"
            badge_text = "FAILED"
            badge_style = "color: #ef4444; background: rgba(239, 68, 68, 0.18); border: 1px solid rgba(239, 68, 68, 0.4);"
            card_border = "border: 1px solid rgba(239, 68, 68, 0.5); box-shadow: 0 0 12px rgba(239, 68, 68, 0.2);"
        else:  # blocked / skipped
            icon = "-"
            icon_color = "#64748b"
            card_bg = "#192233"
            text_color = "#94a3b8"
            badge_text = "BLOCKED"
            badge_style = "color: #64748b; background: rgba(100, 116, 139, 0.12); border: 1px solid rgba(100, 116, 139, 0.2);"
            card_border = "border: 1px solid rgba(100, 116, 139, 0.15);"

        card_html = (
            f'<div style="background: {card_bg}; {card_border} border-radius: 9px; padding: 14px 18px; '
            f'display: flex; align-items: center; justify-content: space-between; margin-bottom: 2px;">'
            f'<div style="display: flex; align-items: center; gap: 14px;">'
            f'<span style="color: {icon_color}; font-weight: 800; font-size: 17px; min-width: 20px; text-align: center;">{icon}</span>'
            f'<span style="color: {text_color}; font-size: 14.5px; font-weight: 500; letter-spacing: 0.2px;">{text}</span>'
            f'</div>'
            f'<span style="{badge_style} font-size: 11px; font-weight: 700; padding: 3px 8px; border-radius: 4px; letter-spacing: 0.5px;">{badge_text}</span>'
            f'</div>'
        )
        html_cards.append(card_html)

        # Connector arrow between steps
        if idx < len(steps) - 1:
            arrow_color = "#38bdf8" if state == "passed" else "#475569"
            arrow_html = (
                f'<div style="display: flex; justify-content: center; align-items: center; padding: 3px 0; margin: -1px 0;">'
                f'<span style="color: {arrow_color}; font-size: 13px; line-height: 1; opacity: 0.85; font-family: monospace;">|</span>'
                f'</div>'
            )
            html_cards.append(arrow_html)

    all_cards_html = "".join(html_cards)

    full_component = (
        f'<div style="background: #111827; border-radius: 14px; padding: 22px; border: 1px solid #1f2937; '
        f'box-shadow: 0 12px 30px rgba(0, 0, 0, 0.45); margin-bottom: 20px;">'
        f'<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">'
        f'<div style="color: #94a3b8; font-size: 13px; font-weight: 700; letter-spacing: 2px;">LIVE TRACE & TRIGGER PIPELINE</div>'
        f'<div style="font-size: 12px; color: #64748b; font-weight: 500;">In-Engine PostgreSQL PL/pgSQL</div>'
        f'</div>'
        f'{all_cards_html}'
        f'</div>'
    )
    st.html(full_component)


def render_diff_viewer(before_snapshot, after_snapshot, job_name, result):
    """
    Renders an interactive Before/After Diff Viewer showing database row state
    snapshots side-by-side, with highlighted balance and status delta indicators.
    Renders directly via st.html() to avoid markdown code-block conversion.
    """
    if not before_snapshot and not after_snapshot:
        return

    status = result.get("status")
    is_success = (status == "success")

    st.markdown("""
        <div style="color: #94a3b8; font-size: 13px; font-weight: 700; letter-spacing: 2px; margin-top: 15px; margin-bottom: 12px;">
            BEFORE / AFTER STATE DIFF VIEWER
        </div>
    """, unsafe_allow_html=True)

    col_before, col_after = st.columns(2)

    # -------------------------------------------------------------------------
    # BEFORE COLUMN
    # -------------------------------------------------------------------------
    with col_before:
        before_header = (
            '<div style="background: rgba(30, 41, 59, 0.7); border-radius: 8px; padding: 6px 12px; margin-bottom: 10px; border-left: 4px solid #38bdf8;">'
            '<span style="color: #38bdf8; font-weight: 700; font-size: 12px; letter-spacing: 1px;">PRE-TRANSACTION SNAPSHOT</span>'
            '</div>'
        )
        st.html(before_header)

        if "accounts" in before_snapshot:
            for acc_id, acc in before_snapshot["accounts"].items():
                card = (
                    f'<div style="background: #1e293b; border-radius: 8px; padding: 12px 14px; margin-bottom: 8px; border: 1px solid #334155;">'
                    f'<div style="display: flex; justify-content: space-between; margin-bottom: 6px;">'
                    f'<span style="color: #f1f5f9; font-weight: 600; font-size: 14px;">Account #{acc_id}</span>'
                    f'<span style="color: #94a3b8; font-size: 12px;">Type: {acc.get("type", "N/A")}</span>'
                    f'</div>'
                    f'<div style="display: flex; justify-content: space-between; align-items: center;">'
                    f'<div><span style="color: #94a3b8; font-size: 12px;">Balance: </span>'
                    f'<span style="color: #38bdf8; font-size: 16px; font-weight: 700;">${acc.get("balance", 0.0):,.2f}</span></div>'
                    f'<span style="color: #10b981; font-size: 11px; font-weight: 600; background: rgba(16, 185, 129, 0.12); padding: 2px 6px; border-radius: 4px;">{acc.get("status", "ACTIVE")}</span>'
                    f'</div></div>'
                )
                st.html(card)

        elif "loans" in before_snapshot:
            for loan_id, loan in before_snapshot["loans"].items():
                card = (
                    f'<div style="background: #1e293b; border-radius: 8px; padding: 12px 14px; margin-bottom: 8px; border: 1px solid #334155;">'
                    f'<div style="display: flex; justify-content: space-between; margin-bottom: 6px;">'
                    f'<span style="color: #f1f5f9; font-weight: 600; font-size: 14px;">Loan #{loan_id} (Profile #{loan.get("profile_id")})</span>'
                    f'</div>'
                    f'<div style="display: flex; justify-content: space-between; align-items: center;">'
                    f'<div><span style="color: #94a3b8; font-size: 12px;">Amount: </span>'
                    f'<span style="color: #f8fafc; font-size: 15px; font-weight: 600;">${loan.get("requested_amount", 0.0):,.2f}</span></div>'
                    f'<span style="color: #38bdf8; font-size: 11px; font-weight: 600; background: rgba(56, 189, 248, 0.15); padding: 2px 8px; border-radius: 4px;">{loan.get("approval_status")}</span>'
                    f'</div></div>'
                )
                st.html(card)

    # -------------------------------------------------------------------------
    # AFTER COLUMN
    # -------------------------------------------------------------------------
    with col_after:
        if is_success:
            after_header = (
                '<div style="background: rgba(16, 185, 129, 0.1); border-radius: 8px; padding: 6px 12px; margin-bottom: 10px; border-left: 4px solid #10b981;">'
                '<span style="color: #10b981; font-weight: 700; font-size: 12px; letter-spacing: 1px;">POST-TRANSACTION STATE (COMMITTED)</span>'
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
                            diff_html = f'<span style="color: #10b981; font-size: 13px; font-weight: 700; margin-left: 6px;">(+${diff:,.2f})</span>'
                        else:
                            diff_html = f'<span style="color: #ef4444; font-size: 13px; font-weight: 700; margin-left: 6px;">(-${abs(diff):,.2f})</span>'

                    status_diff = ""
                    if old_acc.get("status") != acc.get("status"):
                        status_diff = f'<span style="color: #f59e0b; font-size: 11px; font-weight: 700; background: rgba(245, 158, 11, 0.15); padding: 2px 6px; border-radius: 4px;">{acc.get("status")}</span>'
                    else:
                        status_diff = f'<span style="color: #10b981; font-size: 11px; font-weight: 600; background: rgba(16, 185, 129, 0.12); padding: 2px 6px; border-radius: 4px;">{acc.get("status")}</span>'

                    card = (
                        f'<div style="background: #1e293b; border-radius: 8px; padding: 12px 14px; margin-bottom: 8px; border: 1px solid #10b981;">'
                        f'<div style="display: flex; justify-content: space-between; margin-bottom: 6px;">'
                        f'<span style="color: #f1f5f9; font-weight: 600; font-size: 14px;">Account #{acc_id}</span>'
                        f'<span style="color: #10b981; font-size: 12px; font-weight: 600;">Updated</span>'
                        f'</div>'
                        f'<div style="display: flex; justify-content: space-between; align-items: center;">'
                        f'<div><span style="color: #94a3b8; font-size: 12px;">Balance: </span>'
                        f'<span style="color: #f8fafc; font-size: 16px; font-weight: 700;">${new_bal:,.2f}</span>'
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
                        f'<div style="background: #1e293b; border-radius: 8px; padding: 12px 14px; margin-bottom: 8px; border: 1px solid #10b981;">'
                        f'<div style="display: flex; justify-content: space-between; margin-bottom: 6px;">'
                        f'<span style="color: #f1f5f9; font-weight: 600; font-size: 14px;">Loan #{loan_id} (Profile #{loan.get("profile_id")})</span>'
                        f'<span style="color: #10b981; font-size: 12px; font-weight: 600;">State Advanced</span>'
                        f'</div>'
                        f'<div style="display: flex; justify-content: space-between; align-items: center;">'
                        f'<div><span style="color: #94a3b8; font-size: 12px;">Amount: </span>'
                        f'<span style="color: #f8fafc; font-size: 15px; font-weight: 600;">${loan.get("requested_amount", 0.0):,.2f}</span></div>'
                        f'<div><span style="color: #94a3b8; font-size: 11px; text-decoration: line-through; margin-right: 4px;">{old_status}</span>'
                        f'<span style="color: #10b981; font-size: 11px; font-weight: 700; background: rgba(16, 185, 129, 0.2); padding: 2px 8px; border-radius: 4px;">{new_status}</span></div>'
                        f'</div></div>'
                    )
                    st.html(card)

        else:
            # Rejection / Rollback state
            after_header = (
                '<div style="background: rgba(239, 68, 68, 0.1); border-radius: 8px; padding: 6px 12px; margin-bottom: 10px; border-left: 4px solid #ef4444;">'
                '<span style="color: #ef4444; font-weight: 700; font-size: 12px; letter-spacing: 1px;">POST-TRANSACTION (ROLLED BACK)</span>'
                '</div>'
            )
            st.html(after_header)

            card = (
                '<div style="background: #1e293b; border-radius: 8px; padding: 20px; text-align: center; border: 1px dashed rgba(239, 68, 68, 0.5);">'
                '<div style="color: #ef4444; font-size: 18px; font-weight: bold; margin-bottom: 6px;">❌ TRANSACTION ABORTED</div>'
                '<div style="color: #cbd5e1; font-size: 13px; line-height: 1.5;">'
                'PostgreSQL triggered an automatic <strong>ROLLBACK</strong>.<br>'
                '<strong>0 rows modified</strong> — database state remains completely intact.'
                '</div></div>'
            )
            st.html(card)


TRIGGER_SOURCE_CODES = {
    "process_transaction": """-- Trigger 1: process_transaction (BEFORE INSERT on daily_transactions)
CREATE OR REPLACE FUNCTION process_transaction()
RETURNS TRIGGER AS $$
DECLARE
    sender_kyc VARCHAR(20);
    receiver_kyc VARCHAR(20);
    sender_status VARCHAR(20);
    receiver_status VARCHAR(20);
    sender_balance NUMERIC(15, 2);
    alert_account INT;
    alert_reason TEXT;
BEGIN
    -- 1. Identity & KYC Verification Check
    SELECT kyc_status INTO sender_kyc FROM customer_profiles cp
    JOIN customer_accounts ca ON ca.profile_id = cp.profile_id WHERE ca.account_id = NEW.sender_id;
    SELECT kyc_status INTO receiver_kyc FROM customer_profiles cp
    JOIN customer_accounts ca ON ca.profile_id = cp.profile_id WHERE ca.account_id = NEW.receiver_id;

    IF sender_kyc IS NULL OR sender_kyc <> 'APPROVED' THEN
        RAISE EXCEPTION 'KYC_CHECK_FAILED: Sender KYC verification not approved (status: %).', COALESCE(sender_kyc, 'NOT_FOUND');
    END IF;
    IF receiver_kyc IS NULL OR receiver_kyc <> 'APPROVED' THEN
        RAISE EXCEPTION 'KYC_CHECK_FAILED: Receiver KYC verification not approved (status: %).', COALESCE(receiver_kyc, 'NOT_FOUND');
    END IF;

    -- 2. Operational Health Check (Frozen / Closed)
    SELECT account_status, balance INTO sender_status, sender_balance FROM customer_accounts WHERE account_id = NEW.sender_id;
    SELECT account_status INTO receiver_status FROM customer_accounts WHERE account_id = NEW.receiver_id;

    IF sender_status IN ('FROZEN', 'CLOSED') THEN
        RAISE EXCEPTION 'ACCOUNT_FROZEN_BLOCKED: Sender account % is currently %.', NEW.sender_id, sender_status;
    END IF;
    IF receiver_status IN ('FROZEN', 'CLOSED') THEN
        RAISE EXCEPTION 'ACCOUNT_FROZEN_BLOCKED: Receiver account % is currently %.', NEW.receiver_id, receiver_status;
    END IF;

    -- 3. Risk Intelligence & Fraud Alerts Check
    SELECT account_id, risk_reason INTO alert_account, alert_reason FROM fraud_alerts
    WHERE account_id IN (NEW.sender_id, NEW.receiver_id) AND alert_status IN ('OPEN', 'UNDER_INVESTIGATION') LIMIT 1;
    IF FOUND THEN
        RAISE EXCEPTION 'FRAUD_CHECK_FAILED: Active fraud alert on file for account % (Reason: %).', alert_account, alert_reason;
    END IF;

    -- 4. Balance Sufficiency & In-Engine Atomic Mutation
    IF sender_balance < NEW.amount THEN
        RAISE EXCEPTION 'INSUFFICIENT_FUNDS: Sender balance ($%) insufficient for transfer amount ($%).', sender_balance, NEW.amount;
    END IF;

    UPDATE customer_accounts SET balance = balance - NEW.amount WHERE account_id = NEW.sender_id;
    UPDATE customer_accounts SET balance = balance + NEW.amount WHERE account_id = NEW.receiver_id;

    RETURN NEW; -- Proceeds to commit transaction row
END;
$$ LANGUAGE plpgsql;""",

    "check_loan_eligibility": """-- Trigger 2: check_loan_eligibility (BEFORE INSERT on loan_applications)
CREATE OR REPLACE FUNCTION check_loan_eligibility()
RETURNS TRIGGER AS $$
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

    NEW.approval_status := 'SUBMITTED';
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;""",

    "enforce_loan_workflow": """-- Trigger 3: enforce_loan_workflow (BEFORE UPDATE on loan_applications)
CREATE OR REPLACE FUNCTION enforce_loan_workflow()
RETURNS TRIGGER SECURITY DEFINER AS $$
BEGIN
    IF OLD.approval_status = NEW.approval_status THEN
        RETURN NEW;
    END IF;

    -- 1. Stage-Skipping Guard
    IF OLD.approval_status = 'SUBMITTED' AND NEW.approval_status = 'APPROVED' THEN
        RAISE EXCEPTION 'WORKFLOW_STAGE_SKIPPED: A loan in SUBMITTED state must move to UNDERWRITE before final approval.';
    END IF;

    -- 2. Backward Transition Guard
    IF OLD.approval_status = 'UNDERWRITE' AND NEW.approval_status = 'SUBMITTED' THEN
        RAISE EXCEPTION 'WORKFLOW_BACKWARD_TRANSITION: Backward workflow transitions are prohibited (Cannot revert UNDERWRITE -> SUBMITTED).';
    END IF;
    IF OLD.approval_status IN ('APPROVED', 'REJECTED') THEN
        RAISE EXCEPTION 'WORKFLOW_TERMINAL_STATE: Loan application is already % and cannot be modified further.', OLD.approval_status;
    END IF;

    -- 3. Role-Based Underwriting Enforcement
    IF NEW.approval_status = 'UNDERWRITE' AND CURRENT_USER NOT IN ('senior_underwriter', 'neondb_owner') THEN
        RAISE EXCEPTION 'WORKFLOW_UNAUTHORIZED_ACTOR: Only Senior Underwriters can transition a loan to UNDERWRITE (Current user: %).', CURRENT_USER;
    END IF;
    IF NEW.approval_status = 'APPROVED' AND CURRENT_USER NOT IN ('branch_manager', 'neondb_owner') THEN
        RAISE EXCEPTION 'WORKFLOW_UNAUTHORIZED_ACTOR: Only Branch Managers can grant final loan approval (Current user: %).', CURRENT_USER;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;""",

    "log_audit_event": """-- Trigger 4: log_audit_event (AFTER UPDATE on customer_accounts & loan_applications)
CREATE OR REPLACE FUNCTION log_audit_event()
RETURNS TRIGGER SECURITY DEFINER AS $$
DECLARE
    resolved_acc_id INT;
BEGIN
    IF TG_TABLE_NAME = 'customer_accounts' THEN
        resolved_acc_id := NEW.account_id;
        INSERT INTO audit_log (table_name, record_id, account_id, action, old_value, new_value, changed_by)
        VALUES ('customer_accounts', NEW.account_id, resolved_acc_id, 'UPDATE',
                format('balance=%s, status=%s', OLD.balance, OLD.account_status),
                format('balance=%s, status=%s', NEW.balance, NEW.account_status),
                CURRENT_USER);
    ELSIF TG_TABLE_NAME = 'loan_applications' THEN
        SELECT account_id INTO resolved_acc_id FROM customer_accounts WHERE profile_id = NEW.profile_id LIMIT 1;
        INSERT INTO audit_log (table_name, record_id, account_id, action, old_value, new_value, changed_by)
        VALUES ('loan_applications', NEW.loan_id, resolved_acc_id, 'UPDATE',
                format('approval=%s, amount=%s', OLD.approval_status, OLD.requested_amount),
                format('approval=%s, amount=%s', NEW.approval_status, NEW.requested_amount),
                CURRENT_USER);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;"""
}


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
            edge [color="#ef4444", fontcolor="#f87171"]

            role [label="Role: {clean_role}", shape=ellipse, fillcolor="#1e293b", fontcolor="#38bdf8", color="#0284c7"]
            rbac [label="RBAC Engine\\n(System Catalog)", shape=diamond, fillcolor="#3b0764", fontcolor="#f5d0fe", color="#c084fc"]
            blocked [label="403 Access Denied\\n(InsufficientPrivilege)", shape=box, fillcolor="#450a0a", fontcolor="#fecaca", color="#ef4444"]
            abort [label="Transaction Aborted\\nZero DB Mutation", shape=box, fillcolor="#1e293b", fontcolor="#cbd5e1", color="#64748b"]

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
            edge [color="#10b981", fontcolor="#6ee7b7"]

            role [label="Role: {clean_role}", shape=ellipse, fillcolor="#1e293b", fontcolor="#38bdf8", color="#0284c7"]
            rbac [label="RBAC Check\\n(Granted)", shape=diamond, fillcolor="#064e3b", fontcolor="#a7f3d0", color="#10b981"]
            tbl [label="daily_transactions\\n(Memory Buffer)", shape=cylinder, fillcolor="#1e293b", fontcolor="#93c5fd", color="#3b82f6"]
            trigger [label="BEFORE Trigger:\\nprocess_transaction()", shape=box, fillcolor="#172554", fontcolor="#bfdbfe", color="#60a5fa"]
            checks [label="In-Engine Verification:\\nKYC | Health | Fraud | Balance", shape=box, fillcolor="#1e293b", fontcolor="#e2e8f0", color="#38bdf8"]
            mutation [label="Atomic In-Engine Mutation:\\nDebit Sender & Credit Receiver", shape=cylinder, fillcolor="#064e3b", fontcolor="#a7f3d0", color="#10b981"]
            audit [label="AFTER Trigger:\\nlog_audit_event()", shape=box, fillcolor="#3b0764", fontcolor="#f5d0fe", color="#c084fc"]
            commit [label="ACID Commit\\n(Synced to Disk)", shape=ellipse, fillcolor="#064e3b", fontcolor="#a7f3d0", color="#10b981"]

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
            edge [color="#10b981", fontcolor="#6ee7b7"]

            role [label="Role: {clean_role}", shape=ellipse, fillcolor="#1e293b", fontcolor="#38bdf8", color="#0284c7"]
            rbac [label="RBAC Check\\n(Granted)", shape=diamond, fillcolor="#064e3b", fontcolor="#a7f3d0", color="#10b981"]
            tbl [label="loan_applications\\n(Memory Buffer)", shape=cylinder, fillcolor="#1e293b", fontcolor="#93c5fd", color="#3b82f6"]
            trigger [label="BEFORE Trigger:\\ncheck_loan_eligibility()", shape=box, fillcolor="#172554", fontcolor="#bfdbfe", color="#60a5fa"]
            checks [label="Eligibility Rules:\\nKYC | Anti-Stacking | Health", shape=box, fillcolor="#1e293b", fontcolor="#e2e8f0", color="#38bdf8"]
            registered [label="Registered State:\\napproval_status := SUBMITTED", shape=cylinder, fillcolor="#064e3b", fontcolor="#a7f3d0", color="#10b981"]
            commit [label="ACID Commit", shape=ellipse, fillcolor="#064e3b", fontcolor="#a7f3d0", color="#10b981"]

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
            edge [color="#10b981", fontcolor="#6ee7b7"]

            role [label="Role: {clean_role}", shape=ellipse, fillcolor="#1e293b", fontcolor="#38bdf8", color="#0284c7"]
            rbac [label="RBAC Check\\n(Granted)", shape=diamond, fillcolor="#064e3b", fontcolor="#a7f3d0", color="#10b981"]
            tbl [label="loan_applications\\n(Memory Buffer)", shape=cylinder, fillcolor="#1e293b", fontcolor="#93c5fd", color="#3b82f6"]
            trigger [label="BEFORE Trigger:\\nenforce_loan_workflow()", shape=box, fillcolor="#172554", fontcolor="#bfdbfe", color="#60a5fa"]
            state [label="State Machine Guard:\\nSUBMITTED -> UNDERWRITE -> APPROVED", shape=box, fillcolor="#1e293b", fontcolor="#e2e8f0", color="#38bdf8"]
            audit [label="AFTER Trigger:\\nlog_audit_event()", shape=box, fillcolor="#3b0764", fontcolor="#f5d0fe", color="#c084fc"]
            commit [label="ACID Commit", shape=ellipse, fillcolor="#064e3b", fontcolor="#a7f3d0", color="#10b981"]

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
            edge [color="#10b981", fontcolor="#6ee7b7"]

            role [label="Role: {clean_role}", shape=ellipse, fillcolor="#1e293b", fontcolor="#38bdf8", color="#0284c7"]
            rbac [label="RBAC Engine\\n(System Catalog)", shape=diamond, fillcolor="#064e3b", fontcolor="#a7f3d0", color="#10b981"]
            engine [label="PostgreSQL Query Engine\\n(Cost-Based Optimizer)", shape=box, fillcolor="#172554", fontcolor="#bfdbfe", color="#60a5fa"]
            pool [label="Shared Buffer Pool\\n(Direct Tuple Scan)", shape=cylinder, fillcolor="#1e293b", fontcolor="#93c5fd", color="#3b82f6"]
            client [label="Client Result Set\\n(Zero Trigger Mutation)", shape=ellipse, fillcolor="#064e3b", fontcolor="#a7f3d0", color="#10b981"]

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
            edge [color="#10b981", fontcolor="#6ee7b7"]

            role [label="Role: {clean_role}", shape=ellipse, fillcolor="#1e293b", fontcolor="#38bdf8", color="#0284c7"]
            rbac [label="RBAC Engine\\n(System Catalog)", shape=diamond, fillcolor="#064e3b", fontcolor="#a7f3d0", color="#10b981"]
            tbl [label="Target Table\\n(Disk/Buffer)", shape=cylinder, fillcolor="#1e293b", fontcolor="#93c5fd", color="#3b82f6"]
            audit [label="AFTER Trigger:\\nlog_audit_event() [If Mutation]", shape=box, fillcolor="#3b0764", fontcolor="#f5d0fe", color="#c084fc"]
            commit [label="ACID Complete", shape=ellipse, fillcolor="#064e3b", fontcolor="#a7f3d0", color="#10b981"]

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

            role [label="Role: {clean_role}", shape=ellipse, fillcolor="#1e293b", fontcolor="#38bdf8", color="#0284c7"]
            rbac [label="RBAC Engine", shape=diamond, fillcolor="#064e3b", fontcolor="#a7f3d0", color="#10b981"]
            tbl [label="Target Table\\n(Uncommitted Buffer)", shape=cylinder, fillcolor="#1e293b", fontcolor="#93c5fd", color="#3b82f6"]
            trigger [label="BEFORE Trigger\\nExecution", shape=box, fillcolor="#172554", fontcolor="#bfdbfe", color="#60a5fa"]
            violate [label="RAISE EXCEPTION\\n(Constraint Violated)", shape=box, fillcolor="#450a0a", fontcolor="#fecaca", color="#ef4444"]
            rollback [label="Kernel ROLLBACK\\nZero DB Mutation", shape=box, fillcolor="#1e293b", fontcolor="#f87171", color="#ef4444"]

            role -> rbac [label="Allowed", color="#10b981", fontcolor="#6ee7b7"]
            rbac -> tbl [label="Dispatched", color="#10b981", fontcolor="#6ee7b7"]
            tbl -> trigger [label="Intercepted", color="#10b981", fontcolor="#6ee7b7"]
            trigger -> violate [label="Check Failed", color="#ef4444", fontcolor="#f87171"]
            violate -> rollback [label="Automatic Rollback", color="#ef4444", fontcolor="#f87171"]
        }}
        """
    st.graphviz_chart(dot_code, use_container_width=True)


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
        action_badge = "<span style='color: #ef4444; font-weight: 700;'>❌ ACCESS DENIED (403)</span>"

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
            action_badge = "<span style='color: #10b981; font-weight: 700;'>✓ TRANSACTION COMMITTED</span>"
        elif status == "error":
            clean_err = result.get("clean_message", "Constraint Violated") if result else "Constraint Violated"
            action_desc = f"RAISE EXCEPTION executed ({clean_err}); entire transfer aborted via automatic ROLLBACK."
            action_badge = "<span style='color: #ef4444; font-weight: 700;'>✕ TRANSACTION ABORTED</span>"
        else:
            action_desc = "Ready for execution dispatch to PostgreSQL."
            action_badge = "<span style='color: #94a3b8; font-weight: 700;'>PENDING DISPATCH</span>"

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
            ("4. Initial State Guard", "Enforces NEW.approval_status := 'SUBMITTED'")
        ]
        if is_success:
            action_desc = "Loan application inserted in SUBMITTED state for underwriter review."
            action_badge = "<span style='color: #10b981; font-weight: 700;'>✓ LOAN REGISTERED</span>"
        elif status == "error":
            clean_err = result.get("clean_message", "Eligibility Failed") if result else "Eligibility Failed"
            action_desc = f"RAISE EXCEPTION ({clean_err}); loan creation aborted via ROLLBACK."
            action_badge = "<span style='color: #ef4444; font-weight: 700;'>✕ APPLICATION REJECTED</span>"
        else:
            action_desc = "Ready for loan application dispatch."
            action_badge = "<span style='color: #94a3b8; font-weight: 700;'>PENDING DISPATCH</span>"

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
            action_badge = "<span style='color: #10b981; font-weight: 700;'>✓ WORKFLOW ADVANCED</span>"
        elif status == "error":
            clean_err = result.get("clean_message", "Workflow Violated") if result else "Workflow Violated"
            action_desc = f"RAISE EXCEPTION ({clean_err}); update aborted via ROLLBACK."
            action_badge = "<span style='color: #ef4444; font-weight: 700;'>✕ TRANSITION REJECTED</span>"
        else:
            action_desc = "Ready for workflow state transition dispatch."
            action_badge = "<span style='color: #94a3b8; font-weight: 700;'>PENDING DISPATCH</span>"

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
            action_badge = "<span style='color: #10b981; font-weight: 700;'>✓ AUDIT LOGGED</span>"
        elif status == "error":
            clean_err = result.get("clean_message", "Write Failed") if result else "Write Failed"
            action_desc = f"Database mutation failed ({clean_err}); ROLLBACK issued."
            action_badge = "<span style='color: #ef4444; font-weight: 700;'>✕ MUTATION FAILED</span>"
        else:
            action_desc = "Awaiting account mutation to generate forensic trace."
            action_badge = "<span style='color: #94a3b8; font-weight: 700;'>PENDING DISPATCH</span>"

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
            action_badge = "<span style='color: #10b981; font-weight: 700;'>✓ ALERT AUDITED</span>"
        elif status == "error":
            action_desc = "Update aborted via ROLLBACK."
            action_badge = "<span style='color: #ef4444; font-weight: 700;'>✕ UPDATE FAILED</span>"
        else:
            action_desc = "Awaiting fraud status update."
            action_badge = "<span style='color: #94a3b8; font-weight: 700;'>PENDING DISPATCH</span>"

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
            action_badge = "<span style='color: #10b981; font-weight: 700;'>✓ ACCOUNT CREATED</span>"
        elif status == "error":
            clean_err = result.get("clean_message", "Insert Failed") if result else "Insert Failed"
            action_desc = f"Account creation aborted ({clean_err})."
            action_badge = "<span style='color: #ef4444; font-weight: 700;'>✕ INSERT FAILED</span>"
        else:
            action_desc = "Ready for new account insertion dispatch."
            action_badge = "<span style='color: #94a3b8; font-weight: 700;'>PENDING DISPATCH</span>"

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
            action_badge = "<span style='color: #10b981; font-weight: 700;'>✓ PROFILE UPDATED</span>"
        elif status == "error":
            clean_err = result.get("clean_message", "Update Failed") if result else "Update Failed"
            action_desc = f"Profile update aborted ({clean_err})."
            action_badge = "<span style='color: #ef4444; font-weight: 700;'>✕ UPDATE FAILED</span>"
        else:
            action_desc = "Ready for profile update dispatch."
            action_badge = "<span style='color: #94a3b8; font-weight: 700;'>PENDING DISPATCH</span>"

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
            action_badge = "<span style='color: #10b981; font-weight: 700;'>✓ ALERT LOGGED</span>"
        elif status == "error":
            clean_err = result.get("clean_message", "Logging Failed") if result else "Logging Failed"
            action_desc = f"Alert insertion aborted ({clean_err})."
            action_badge = "<span style='color: #ef4444; font-weight: 700;'>✕ LOGGING FAILED</span>"
        else:
            action_desc = "Ready to log fraud alert."
            action_badge = "<span style='color: #94a3b8; font-weight: 700;'>PENDING DISPATCH</span>"

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
            action_badge = "<span style='color: #10b981; font-weight: 700;'>✓ QUERY EXECUTED</span>"
        elif status == "error":
            clean_err = result.get("clean_message", "Query Error") if result else "Query Error"
            action_desc = f"Execution failed: {clean_err}"
            action_badge = "<span style='color: #ef4444; font-weight: 700;'>✕ EXECUTION FAILED</span>"
        else:
            action_desc = "Ready for direct SQL dispatch."
            action_badge = "<span style='color: #94a3b8; font-weight: 700;'>PENDING DISPATCH</span>"

    st.markdown("""
    <div style="background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); border-radius: 12px; padding: 18px 22px; border: 1px solid #312e81; margin-bottom: 20px;">
        <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 1.5px; color: #38bdf8; font-weight: 700;">
            DBMS Educational Architecture &bull; Event-Condition-Action (ECA) Model
        </div>
        <div style="font-size: 20px; font-weight: 700; color: #f8fafc; margin-top: 4px;">
            In-Engine Trigger Dissector
        </div>
        <div style="color: #94a3b8; font-size: 13px; margin-top: 4px;">
            In formal database theory, a trigger is an active database rule structured into three formal primitives:
            an <b>Event</b> that invokes execution, <b>Conditions</b> evaluated against memory buffers, and an atomic <b>Action</b>.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ECA 3-Column Visual
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"""
        <div style="background: #111827; border-radius: 10px; padding: 16px; border: 1px solid #1f2937; height: 100%;">
            <div style="font-size: 12px; font-weight: 700; color: #60a5fa; letter-spacing: 1px; text-transform: uppercase;">
                1. THE EVENT
            </div>
            <div style="font-size: 16px; font-weight: 700; color: #f8fafc; margin-top: 6px;">
                {event_timing} {event_type}
            </div>
            <div style="margin-top: 10px; font-size: 12px; color: #cbd5e1; line-height: 1.6;">
                <div><b>Target Table:</b> <code style="color: #38bdf8;">{target_table}</code></div>
                <div><b>Granularity:</b> <code>FOR EACH ROW</code></div>
                <div><b>Execution Mode:</b> <code style="color: #c084fc;">{sec_mode}</code></div>
            </div>
            <div style="margin-top: 12px; font-size: 11px; color: #64748b;">
                {timing_desc}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        cond_status_badge = "✓ VERIFIED" if is_success else ("✕ VIOLATED" if status == "error" else ("❌ DENIED" if is_denied else "AWAITING"))
        cond_items_html = "".join([f"<div><b>{cname}:</b> <code>{cdesc}</code></div>" for cname, cdesc in conditions])
        st.markdown(f"""
        <div style="background: #111827; border-radius: 10px; padding: 16px; border: 1px solid #1f2937; height: 100%;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="font-size: 12px; font-weight: 700; color: #f59e0b; letter-spacing: 1px; text-transform: uppercase;">
                    2. CONDITIONS
                </div>
                <span style="font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 10px; background: #1e293b; color: #94a3b8;">{cond_status_badge}</span>
            </div>
            <div style="font-size: 16px; font-weight: 700; color: #f8fafc; margin-top: 6px;">
                {cond_title}
            </div>
            <div style="margin-top: 10px; font-size: 12px; color: #cbd5e1; line-height: 1.6;">
                {cond_items_html}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div style="background: #111827; border-radius: 10px; padding: 16px; border: 1px solid #1f2937; height: 100%;">
            <div style="font-size: 12px; font-weight: 700; color: #10b981; letter-spacing: 1px; text-transform: uppercase;">
                3. THE ACTION
            </div>
            <div style="font-size: 14px; margin-top: 6px;">
                {action_badge}
            </div>
            <div style="margin-top: 10px; font-size: 12px; color: #cbd5e1; line-height: 1.6;">
                {action_desc}
            </div>
            <div style="margin-top: 12px; font-size: 11px; color: #64748b;">
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
        <div style="background: rgba(239, 68, 68, 0.08); border-left: 4px solid #ef4444; border-radius: 8px; padding: 14px 18px; margin-bottom: 16px;">
            <div style="font-size: 13px; font-weight: 700; color: #f87171;">
                ❌ RBAC Authorization Denied — In-Memory Transition Buffers Never Allocated
            </div>
            <div style="font-size: 12px; color: #cbd5e1; margin-top: 6px; line-height: 1.5;">
                PostgreSQL evaluates role privileges at <b>Tier 1 (Parser & System Catalog Stage)</b>. 
                Because active role <code style="color: #38bdf8;">{active_role}</code> does not hold the required privilege on <code style="color: #c084fc;">{target_table}</code>, 
                PostgreSQL halts execution immediately with error <code>42501 (insufficient_privilege)</code>.
                <br><br>
                <b>Memory Allocation Abort:</b> In PostgreSQL engine internals, memory for <code>NEW</code> and <code>OLD</code> pseudo-record variables is only allocated <i>after</i> Tier-1 RBAC authorization succeeds. 
                Because authorization was denied, zero heap pages were retrieved into the Shared Buffer Pool, and no backend tuple buffers were created.
            </div>
        </div>
        """, unsafe_allow_html=True)

        denied_rows = [
            {"Attribute": "Execution Stage", "Memory Buffer State": "Halted at Tier 1 (PostgreSQL System Catalog)", "Role": "Access Verification Firewall", "Status": "❌ Aborted (42501)"},
            {"Attribute": "OLD Buffer (Heap Disk)", "Memory Buffer State": "NULL (Read access blocked — Disk page not loaded into RAM)", "Role": "Pre-Mutation Heap State", "Status": "❌ Unallocated"},
            {"Attribute": "NEW Buffer (Candidate Row)", "Memory Buffer State": "NULL (Memory allocation aborted before backend slot creation)", "Role": "Proposed Row State", "Status": "❌ Unallocated"},
            {"Attribute": "Procedural Trigger Engine", "Memory Buffer State": "BYPASSED (Short-circuited at catalog level)", "Role": "Business Rule Enforcement", "Status": "❌ Not Reached"},
            {"Attribute": "WAL / Disk I/O", "Memory Buffer State": "0 bytes written (Zero side effects)", "Role": "ACID Durability", "Status": "✓ Protected"}
        ]
        st.dataframe(pd.DataFrame(denied_rows), use_container_width=True, hide_index=True)

    elif "SELECT" in job_key:
        st.markdown("#### In-Memory Buffer Inspector: Shared Buffer Pool & Read-Cursor Stream")
        st.markdown(f"""
        <div style="background: rgba(56, 189, 248, 0.08); border-left: 4px solid #38bdf8; border-radius: 8px; padding: 14px 18px; margin-bottom: 16px;">
            <div style="font-size: 13px; font-weight: 700; color: #38bdf8;">
                Read-Only (SELECT) Query Memory Architecture
            </div>
            <div style="font-size: 12px; color: #cbd5e1; margin-top: 6px; line-height: 1.5;">
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
        st.dataframe(pd.DataFrame(select_rows), use_container_width=True, hide_index=True)

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
                {"Attribute": "approval_status", "OLD Buffer (Pre-Mutation)": "NULL (Does not exist yet)", "NEW Buffer (Candidate Row)": "'SUBMITTED' (Enforced by Trigger)", "Role": "Initial Workflow State"},
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
            new_name = str(user_inputs[0]) if is_text_name else "Alice Smith Updated"
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
            st.dataframe(df_buffer, use_container_width=True, hide_index=True)



