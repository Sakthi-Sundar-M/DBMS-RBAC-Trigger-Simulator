/**
 * DBMS RBAC & TRIGGER SIMULATOR - INTERACTIVE FRONTEND APP
 * Pure client-side logic providing dynamic role switching, tab navigation,
 * and live pipeline trace simulations without needing Streamlit.
 */

// Role metadata matching config.py
const ROLES_DATA = {
    "it_security_admin": {
        name: "IT Security Admin",
        desc: "Security & compliance: strictly read-only inspection of the audit trail.",
        permissions: {
            "create_transaction": false,
            "create_account": false,
            "update_balance": false,
            "log_fraud": false,
            "freeze_account": false,
            "approve_loan": false,
            "view_audit": true
        }
    },
    "internal_auditor": {
        name: "Internal Auditor",
        desc: "Independent oversight: full read-only visibility across all core banking tables.",
        permissions: {
            "create_transaction": false,
            "create_account": false,
            "update_balance": false,
            "log_fraud": false,
            "freeze_account": false,
            "approve_loan": false,
            "view_audit": true
        }
    },
    "fraud_analyst": {
        name: "Fraud Analyst",
        desc: "Financial intelligence: inspects suspicious activity and logs fraud alerts.",
        permissions: {
            "create_transaction": false,
            "create_account": false,
            "update_balance": false,
            "log_fraud": true,
            "freeze_account": false,
            "approve_loan": false,
            "view_audit": false
        }
    },
    "branch_manager": {
        name: "Branch Manager",
        desc: "Branch oversight: approves loans, updates alert statuses, freezes/closes accounts.",
        permissions: {
            "create_transaction": false,
            "create_account": false,
            "update_balance": false,
            "log_fraud": false,
            "freeze_account": true,
            "approve_loan": true,
            "view_audit": false
        }
    },
    "senior_underwriter": {
        name: "Senior Underwriter",
        desc: "Credit risk assessment: advances loan applications to UNDERWRITE stage.",
        permissions: {
            "create_transaction": false,
            "create_account": false,
            "update_balance": false,
            "log_fraud": false,
            "freeze_account": false,
            "approve_loan": false,
            "view_audit": false
        }
    },
    "loan_officer": {
        name: "Loan Officer",
        desc: "Loan intake: captures client requirements and coordinates credit files.",
        permissions: {
            "create_transaction": false,
            "create_account": false,
            "update_balance": false,
            "log_fraud": false,
            "freeze_account": false,
            "approve_loan": false,
            "view_audit": false
        }
    },
    "bank_teller": {
        name: "Bank Teller",
        desc: "Counter cashier: creates accounts and processes cash deposits/withdrawals.",
        permissions: {
            "create_transaction": true,
            "create_account": true,
            "update_balance": true,
            "log_fraud": false,
            "freeze_account": false,
            "approve_loan": false,
            "view_audit": false
        }
    },
    "csr": {
        name: "CSR",
        desc: "Customer service: resolves account inquiries with read-only account data.",
        permissions: {
            "create_transaction": false,
            "create_account": false,
            "update_balance": false,
            "log_fraud": false,
            "freeze_account": false,
            "approve_loan": false,
            "view_audit": false
        }
    },
    "retail_customer": {
        name: "Retail Customer",
        desc: "Self-service customer: initiates peer transfers and daily transactions.",
        permissions: {
            "create_transaction": true,
            "create_account": false,
            "update_balance": false,
            "log_fraud": false,
            "freeze_account": false,
            "approve_loan": false,
            "view_audit": false
        }
    }
};

const OPERATION_SQL = {
    "create_transaction": "INSERT INTO daily_transactions (sender_id, receiver_id, amount, transaction_type) VALUES (101, 102, 500.00, 'INTERNAL');",
    "create_account": "INSERT INTO customer_accounts (account_id, profile_id, balance, account_type) VALUES (106, 1, 1000.00, 'SAVINGS');",
    "update_balance": "UPDATE customer_accounts SET balance = 15500.00 WHERE account_id = 101;",
    "log_fraud": "INSERT INTO fraud_alerts (account_id, risk_reason) VALUES (101, 'Suspicious anomalous velocity');",
    "freeze_account": "UPDATE customer_accounts SET account_status = 'FROZEN' WHERE account_id = 101;",
    "approve_loan": "UPDATE loan_applications SET approval_status = 'APPROVED' WHERE profile_id = 1;",
    "view_audit": "SELECT log_id, changed_at, changed_by AS actor_role, table_name, record_id, account_id, action, old_value, new_value FROM audit_log ORDER BY changed_at DESC LIMIT 50;"
};

const OPERATION_PRIVILEGE_INFO = {
    "create_transaction": { priv: "INSERT", table: "daily_transactions" },
    "create_account": { priv: "INSERT", table: "customer_accounts" },
    "update_balance": { priv: "UPDATE", table: "customer_accounts.balance" },
    "log_fraud": { priv: "INSERT", table: "fraud_alerts" },
    "freeze_account": { priv: "UPDATE", table: "customer_accounts.account_status" },
    "approve_loan": { priv: "UPDATE", table: "loan_applications.approval_status" },
    "view_audit": { priv: "SELECT", table: "audit_log" }
};

let currentRole = "it_security_admin";
let currentOperation = "view_audit"; // Default to View Audit Logs to match Image 1

document.addEventListener("DOMContentLoaded", () => {
    initTabs();
    initRoleRadios();
    initOperationSelector();
    initCollapsible();
    initTriggerCodeTabs();
    initSqlToggle();
    initRunButton();
    updateUI();
});

// Tab navigation handler
function initTabs() {
    const tabButtons = document.querySelectorAll(".tab-btn");
    const tabPanes = document.querySelectorAll(".tab-pane");

    tabButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            tabButtons.forEach(b => b.classList.remove("active"));
            tabPanes.forEach(p => p.classList.remove("active"));

            btn.classList.add("active");
            const targetId = btn.getAttribute("data-tab");
            const targetPane = document.getElementById(targetId);
            if (targetPane) targetPane.classList.add("active");
        });
    });
}

// Role radio buttons handler
function initRoleRadios() {
    const radios = document.querySelectorAll("input[name='role_radio']");
    radios.forEach(radio => {
        radio.addEventListener("change", (e) => {
            currentRole = e.target.value;
            document.querySelectorAll(".radio-option").forEach(opt => opt.classList.remove("active"));
            e.target.closest(".radio-option").classList.add("active");
            updateUI();
        });
    });
}

// Operation dropdown handler
function initOperationSelector() {
    const opSelect = document.getElementById("operationSelect");
    if (opSelect) {
        opSelect.value = currentOperation;
        opSelect.addEventListener("change", (e) => {
            currentOperation = e.target.value;
            updateUI();
        });
    }
}

// Show Raw SQL toggle handler
function initSqlToggle() {
    const cb = document.getElementById("showSqlCheckbox");
    const preview = document.getElementById("sqlPreviewCard");
    if (cb && preview) {
        cb.addEventListener("change", (e) => {
            preview.classList.toggle("open", e.target.checked);
        });
    }
}

// Run Operation button handler
function initRunButton() {
    const btn = document.getElementById("runOpBtn");
    if (btn) {
        btn.addEventListener("click", () => {
            btn.textContent = "Executing...";
            btn.style.opacity = "0.7";
            setTimeout(() => {
                btn.textContent = "Run Operation";
                btn.style.opacity = "1";
                updateUI(true);
            }, 300);
        });
    }
}

// Cheatsheet collapsible handler
function initCollapsible() {
    const header = document.querySelector(".collapsible-header");
    const content = document.querySelector(".collapsible-content");
    if (header && content) {
        header.addEventListener("click", () => {
            content.classList.toggle("open");
            const icon = header.querySelector(".collapsible-icon");
            if (icon) {
                icon.textContent = content.classList.contains("open") ? "▼" : "▶";
            }
        });
    }
}

// Sub-tabs in Trigger Code Viewer (Tab 2)
function initTriggerCodeTabs() {
    const codeBtns = document.querySelectorAll(".code-tab-btn");
    const codeBlocks = document.querySelectorAll(".trigger-code-block");

    codeBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            codeBtns.forEach(b => b.classList.remove("active"));
            codeBlocks.forEach(cb => cb.style.display = "none");

            btn.classList.add("active");
            const targetId = btn.getAttribute("data-code");
            const targetBlock = document.getElementById(targetId);
            if (targetBlock) targetBlock.style.display = "block";
        });
    });
}

// Core UI updater based on current role and operation
function updateUI(flashAnimation = false) {
    const roleMeta = ROLES_DATA[currentRole] || ROLES_DATA["it_security_admin"];

    // Update Sidebar Role Card
    const roleTitleEl = document.getElementById("sidebarRoleTitle");
    const roleDescEl = document.getElementById("sidebarRoleDesc");
    if (roleTitleEl) roleTitleEl.textContent = roleMeta.name;
    if (roleDescEl) roleDescEl.textContent = roleMeta.desc;

    // Update KPI Card
    const kpiRoleVal = document.getElementById("kpiRoleValue");
    if (kpiRoleVal) kpiRoleVal.textContent = roleMeta.name;

    // Evaluate Access Permission
    const hasAccess = !!roleMeta.permissions[currentOperation];
    const targetInfo = OPERATION_PRIVILEGE_INFO[currentOperation] || { priv: "EXECUTE", table: "target_table" };

    // Update Raw SQL Preview Text
    const sqlText = document.getElementById("sqlPreviewText");
    if (sqlText) {
        sqlText.textContent = OPERATION_SQL[currentOperation] || "SELECT 1;";
    }

    // Update Operation Selectbox status icons
    const opSelect = document.getElementById("operationSelect");
    if (opSelect) {
        Array.from(opSelect.options).forEach(opt => {
            const opKey = opt.value;
            const optAllowed = !!roleMeta.permissions[opKey];
            const cleanText = opt.text.replace(/^[✔️❌]\s*/, "");
            opt.text = `${optAllowed ? "✔️" : "❌"} ${cleanText}`;
        });
    }

    // Update Alert Banner & Stepper Pipeline
    const alertBox = document.getElementById("simulationAlert");
    const stepperContainer = document.getElementById("stepperList");

    if (hasAccess) {
        // Allowed State (exact phrasing matching Streamlit Image 1)
        if (alertBox) {
            alertBox.className = "alert-box alert-success";
            alertBox.innerHTML = `<span>✔️</span><span><b>RBAC Authorization Granted</b>: Role <b>${roleMeta.name}</b> holds <code>${targetInfo.priv}</code> privilege on <code>${targetInfo.table}</code>.</span>`;
        }
        if (stepperContainer) {
            stepperContainer.innerHTML = `
                <div class="step-card passed">
                    <div>✓ RBAC Authorization Check: Role holds required table & column privilege</div>
                    <span class="step-badge passed">PASSED</span>
                </div>
                <div class="step-card passed">
                    <div>✓ Identity & KYC Verification: Account holder status is APPROVED</div>
                    <span class="step-badge passed">PASSED</span>
                </div>
                <div class="step-card passed">
                    <div>✓ Account Health Check: Sender & Receiver accounts are ACTIVE</div>
                    <span class="step-badge passed">PASSED</span>
                </div>
                <div class="step-card passed">
                    <div>✓ In-Engine Execution: Balances updated & transaction committed</div>
                    <span class="step-badge passed">COMMITTED</span>
                </div>
            `;
        }
    } else {
        // Denied State
        if (alertBox) {
            alertBox.className = "alert-box alert-danger";
            alertBox.innerHTML = `<span>❌</span><span><b>Access Denied</b>: Active role <b>${roleMeta.name}</b> does not hold <code>${targetInfo.priv}</code> privilege on <code>${targetInfo.table}</code>.</span>`;
        }
        if (stepperContainer) {
            stepperContainer.innerHTML = `
                <div class="step-card failed">
                    <div>✕ RBAC Authorization Denied: Role lacks ${targetInfo.priv} privilege</div>
                    <span class="step-badge failed">FAILED</span>
                </div>
                <div class="step-card blocked">
                    <div>— Account status check skipped</div>
                    <span class="step-badge blocked">BLOCKED</span>
                </div>
                <div class="step-card blocked">
                    <div>— Fraud check skipped</div>
                    <span class="step-badge blocked">BLOCKED</span>
                </div>
                <div class="step-card blocked">
                    <div>— Transfer execution skipped</div>
                    <span class="step-badge blocked">BLOCKED</span>
                </div>
            `;
        }
    }
}
