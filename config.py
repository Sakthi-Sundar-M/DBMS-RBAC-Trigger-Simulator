DEPARTMENTS = {
    "Banking Department": {
        "roles": [
            "it_security_admin", "internal_auditor", "fraud_analyst",
            "branch_manager", "senior_underwriter", "loan_officer",
            "bank_teller", "csr", "retail_customer"
        ],
        "queries": {
            "Create New Account (INSERT)": {
                "table": "customer_accounts",
                "privilege": "INSERT",
                "sql": "INSERT INTO customer_accounts (account_id, profile_id, balance, account_type) VALUES (%s, %s, %s, %s);",
                "inputs": [
                    {"label": "Account ID", "type": "number"},
                    {"label": "Profile ID", "type": "number"},
                    {"label": "Initial Deposit Amount", "type": "number"},
                    {"label": "Account Type", "type": "selectbox", "options": ["SAVINGS", "CURRENT", "DEPOSITS"]}
                ]
            },
            "Update Customer Profile (UPDATE)": {
                "table": "customer_profiles",
                "privilege": "UPDATE",
                "columns": ["full_name", "phone_number"],
                "sql": """
                    UPDATE customer_profiles 
                    SET 
                        full_name = COALESCE(NULLIF(%s, ''), full_name), 
                        phone_number = COALESCE(NULLIF(%s, ''), phone_number) 
                    WHERE profile_id = %s;
                """,
                "inputs": [
                    {"label": "Full Name", "type": "text"},
                    {"label": "Phone Number", "type": "text"},
                    {"label": "Profile ID", "type": "number"}
                ]
            },
            "Update Account Balance (UPDATE)": {
                "table": "customer_accounts",
                "privilege": "UPDATE",
                "columns": ["balance"],
                "sql": "UPDATE customer_accounts SET balance = %s WHERE account_id = %s;",
                "inputs": [
                    {"label": "New Balance", "type": "number"},
                    {"label": "Account ID", "type": "number"}
                ]
            },
            "Create New Transaction (INSERT)": {
                "table": "daily_transactions",
                "privilege": "INSERT",
                "sql": "INSERT INTO daily_transactions (sender_id, receiver_id, amount, transaction_type) VALUES (%s, %s, %s, %s);",
                "inputs": [
                    {"label": "Sender Account ID", "type": "number"},
                    {"label": "Receiver Account ID", "type": "number"},
                    {"label": "Transfer Amount", "type": "number"},
                    {"label": "Transaction Type", "type": "selectbox", "options": ["INTERNAL", "ACH", "WIRE"]}
                ]
            },
            "Log Fraud Alert (INSERT)": {
                "table": "fraud_alerts",
                "privilege": "INSERT",
                "sql": "INSERT INTO fraud_alerts (account_id, risk_reason) VALUES (%s, %s);",
                "inputs": [
                    {"label": "Account ID", "type": "number"},
                    {"label": "Risk Reason", "type": "text"}
                ]
            },
            "Update Account Status (Freeze/Unfreeze)": {
                "table": "customer_accounts",
                "privilege": "UPDATE",
                "columns": ["account_status"],
                "sql": "UPDATE customer_accounts SET account_status = %s WHERE account_id = %s;",
                "inputs": [
                    {"label": "New Account Status", "type": "selectbox", "options": ["FROZEN", "ACTIVE"]},
                    {"label": "Account ID", "type": "number"}
                ]
            },
            "Update Fraud Status (UPDATE)": {
                "table": "fraud_alerts",
                "privilege": "UPDATE",
                "columns": ["alert_status"],
                "sql": "UPDATE fraud_alerts SET alert_status = %s WHERE account_id = %s;",
                "inputs": [
                    {"label": "New Alert Status", "type": "selectbox", "options": ["UNDER_INVESTIGATION", "FALSE_POSITIVE", "RESOLVED"]},
                    {"label": "Account ID", "type": "number"}
                ]
            }
            ,
            "Close Customer Account (UPDATE)": {
                "table": "customer_accounts",
                "privilege": "UPDATE",
                "columns": ["account_status"],
                "sql": "UPDATE customer_accounts SET account_status = 'CLOSED' WHERE account_id = %s;",
                "inputs": [
                    {"label": "Account ID to Close", "type": "number"}
                ]
            }
            ,
            "Create New Loan (INSERT)": {
                "table": "loan_applications",
                "privilege": "INSERT",
                "sql": "INSERT INTO loan_applications (profile_id, requested_amount) VALUES (%s, %s);",
                "inputs": [
                    {"label": "Profile ID", "type": "number"},
                    {"label": "Requested Amount", "type": "number"}
                ]
            },
            "Update Loan Status (UPDATE)": {
                "table": "loan_applications",
                "privilege": "UPDATE",
                "columns": ["approval_status"],
                "sql": "UPDATE loan_applications SET approval_status = %s WHERE profile_id = %s;",
                "inputs": [
                    {"label": "Approval Status", "type": "selectbox", "options": ["UNDERWRITE", "APPROVED", "REJECTED"]},
                    {"label": "Profile ID", "type": "number"}
                ]
            },
            "View Audit Logs (SELECT)": {
                "table": "audit_log",
                "privilege": "SELECT",
                "sql": "SELECT log_id, changed_at, changed_by AS actor_role, table_name, record_id, account_id, action, old_value, new_value FROM audit_log ORDER BY changed_at DESC LIMIT 50;",
                "inputs": []
            },
            "View Customer Accounts (SELECT)": {
                "table": "customer_accounts",
                "privilege": "SELECT",
                "sql": "SELECT * FROM secure_account_viewer(%s, %s, %s);",
                "inputs": [
                    {"label": "Account ID (Staff: Enter 0 for all)", "type": "number"},
                    {"label": "Profile ID (Staff: Enter 0)", "type": "number"},
                    {"label": "Full Name (Staff: Type NA)", "type": "text"}
                ]
            }
            ,
            "View Loan Applications (SELECT)": {
                "table": "loan_applications",
                "privilege": "SELECT",
                "sql": "SELECT * FROM loan_applications LIMIT 50;",
                "inputs": []
            },
            "View Transactions (SELECT)": {
                "table": "daily_transactions",
                "privilege": "SELECT",
                "sql": "SELECT * FROM secure_transaction_viewer(%s, %s, %s);",
                "inputs": [
                    {"label": "Account ID (Staff: Enter 0 for all)", "type": "number"},
                    {"label": "Profile ID (Staff: Enter 0)", "type": "number"},
                    {"label": "Full Name (Staff: Type NA)", "type": "text"}
                ]
            }
        }
    }
}
