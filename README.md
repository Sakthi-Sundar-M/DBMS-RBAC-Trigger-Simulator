# Database Users & Roles Simulator, Trigger Visualizer, and AI Practice Lab
### Academic Evaluation Repository (Professor Copy)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://dbms-rbac-trigger-simulator-michael.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-red.svg)](https://streamlit.io/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Neon%20Serverless-4169E1.svg)](https://neon.tech/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-EE4C2C.svg)](https://pytorch.org/)
[![License](https://img.shields.io/badge/License-Academic-green.svg)]()

**Course**: Database Management Systems (DBMS) Project  
**Institution**: Vellore Institute of Technology (VIT), Chennai  
**Author**: M. Sakthi Sundar (Reg. No: 25BCE1244)  
**Project Guide**: Dr. Swaminathan A (Faculty ID: 54632)  
**Live Application Deployment**: [https://dbms-rbac-trigger-simulator-michael.streamlit.app/](https://dbms-rbac-trigger-simulator-michael.streamlit.app/)  
**Original Public Repository**: [https://github.com/Sakthi-Sundar-M/DBMS-RBAC-Trigger-Simulator](https://github.com/Sakthi-Sundar-M/DBMS-RBAC-Trigger-Simulator)  
**GitHub Profile**: [Sakthi-Sundar-M](https://github.com/Sakthi-Sundar-M)  
**LinkedIn**: [Sakthi Sundar M](https://www.linkedin.com/in/sakthi-sundar-m)  

---

> [!IMPORTANT]
> ### NOTICE FOR EVALUATOR / PROFESSOR: RUNNING THE APPLICATION
> **Cloning this repository locally will NOT run the application out-of-the-box.**  
> The application is securely connected to a live serverless cloud database (**Neon PostgreSQL**) via protected database connection strings, credentials, and API access keys stored in environment secrets (`.streamlit/secrets.toml`), which are strictly excluded from git tracking for enterprise database security and integrity.
>
> **How to Evaluate the Project:**  
> Please access and evaluate the full interactive application through our live production deployment hosted on Streamlit Cloud:  
> **[Live Interactive App: https://dbms-rbac-trigger-simulator-michael.streamlit.app/](https://dbms-rbac-trigger-simulator-michael.streamlit.app/)**  
>
> All backend tables, PostgreSQL triggers, RBAC permission enforcements, live transaction visualizers, and the AI Practice Lab are pre-configured, live, and fully operational on this deployment link.

---

### Project Reference Files Included in this Repository

| Document | Purpose & Description |
| :--- | :--- |
| **[`competitive_exam_questions_and_answers.md`](./competitive_exam_questions_and_answers.md)** | Complete compilation of all **178 authentic competitive exam questions** (GATE, ISRO, NIELIT, UGC-NET) with verified official answer keys and difficulty categorizations (no spoilers/explanations). |
| **[`competitive_exam_practice_variants.md`](./competitive_exam_practice_variants.md)** | Full library of all **534 isomorphic practice variants** across 3 enterprise domains (FinTech / Core Banking, Healthcare EMR, and E-Commerce Retail) with complete question statements, answer choices, and correct solutions. |
| **[`gate_pyq_evidence_matrix.md`](./gate_pyq_evidence_matrix.md)** | Direct IIT/IISc master question paper provenance matrix linking each GATE question to its official PDF source, page number, and question number. |

---

## 1. Executive Summary & Architecture

The **Database Users & Roles Simulator, Trigger Visualizer, and AI Practice Lab** simulates dynamic Role-Based Access Control (RBAC), autonomous trigger-driven workflows, real-time database state observability, and AI-assisted pedagogy for enterprise core banking systems.

Unlike standard web applications that implement access policies exclusively at the client or application layer, this system establishes a **Defense-in-Depth** paradigm where granular column-level privileges, financial invariants, and multi-step state machine workflows are verified directly inside the **PostgreSQL database engine (Neon Serverless)**.

```
Client Operation (Streamlit Frontend)
                 │
                 ▼
      [PostgreSQL RBAC Layer] ────────── Denied ──► 403 InsufficientPrivilege (Blocked)
                 │ (information_schema / GRANTs)
                 ▼
      [PL/pgSQL Trigger Pipeline]
                 │
   ┌─────────────┴─────────────┐
   │                           │
   ▼                           ▼
[BEFORE Triggers]        [AFTER Triggers]
- process_transaction    - log_audit_event
- check_loan_eligibility   (SECURITY DEFINER silent
- enforce_loan_workflow    audit log recorder)
   │
   ├── 1. KYC Verification ───────── Failed ──► RAISE 'KYC_CHECK_FAILED'
   ├── 2. Frozen/Closed Check ────── Failed ──► RAISE 'ACCOUNT_FROZEN_BLOCKED'
   ├── 3. Fraud Investigation ────── Failed ──► RAISE 'FRAUD_CHECK_FAILED'
   └── 4. Balance Sufficiency ────── Failed ──► RAISE 'INSUFFICIENT_FUNDS'
                 │ Passed
                 ▼
      [Database Mutation Committed]
```

---

## 2. Core Banking Schema

The system operates across six normalized relational tables hosted on **Neon Serverless PostgreSQL**:

1. **`customer_profiles`**: Personal customer identity records and KYC compliance statuses (`APPROVED`, `PENDING`, `REJECTED`).
2. **`customer_accounts`**: Financial ledger accounts tracking operational state (`ACTIVE`, `FROZEN`, `CLOSED`) and current monetary balance.
3. **`daily_transactions`**: Append-only transactional transfer ledger recording sender (`from_account_id`), recipient (`to_account_id`), and transfer amounts.
4. **`fraud_alerts`**: Security incident tracking ledger monitoring account flags and resolution states (`OPEN`, `UNDER_INVESTIGATION`, `RESOLVED`).
5. **`loan_applications`**: Credit request lifecycle table subject to sequential approval stages (`SUBMITTED`, `UNDERWRITE`, `APPROVED`, `REJECTED`).
6. **`audit_log`**: Tamper-evident governance ledger recording modifying user roles, target entities, pre/post-mutation values, and timestamps.

---

## 3. Role-Based Access Control (RBAC) Matrix

Privileges are granted through native SQL `GRANT` directives, ensuring security cannot be bypassed by client-side tampering:

| Role | Operational Scope | Permissions & Column Constraints |
| :--- | :--- | :--- |
| **Bank Teller** | Front-Desk Cashier | `INSERT` on `daily_transactions`, `UPDATE` on `customer_accounts.balance`. Strictly blocked from altering account or loan statuses. |
| **Branch Manager** | Branch Authority | `UPDATE` on `customer_accounts.account_status` (Freeze/Unfreeze), `fraud_alerts.alert_status`, and final loan authorization (`APPROVED`/`REJECTED`). Blocked from direct balance edits. |
| **Fraud Analyst** | Risk & Compliance | `INSERT` and `SELECT` on `fraud_alerts`. Restricted from altering balances or freezing accounts directly. |
| **Senior Underwriter** | Credit Risk Assessor | Surgical `UPDATE` on `loan_applications.approval_status` moving strictly from `SUBMITTED` to `UNDERWRITE`. Blocked from final approval. |
| **IT Security Admin** | System Auditor | Exclusive `SELECT` access to `audit_log` for monitoring personnel activity and regulatory compliance. |
| **Internal Auditor** | Global Inspection | Read-only `SELECT` access across all tables to verify financial integrity without modification privileges. |

---

## 4. In-Engine PL/pgSQL Triggers

Four transactional triggers enforce financial consistency and security within the database runtime:

1. **`process_transaction`** (`BEFORE INSERT` on `daily_transactions`):
   - Confirms KYC compliance for both sender and receiver accounts (`KYC_CHECK_FAILED`).
   - Aborts transactions involving `FROZEN` or `CLOSED` accounts (`ACCOUNT_FROZEN_BLOCKED`).
   - Rejects transfers if unresolved fraud alerts exist on either account (`FRAUD_CHECK_FAILED`).
   - Validates positive balance sufficiency and atomically debits the sender while crediting the receiver (`INSUFFICIENT_FUNDS`).

2. **`check_loan_eligibility`** (`BEFORE INSERT` on `loan_applications`):
   - Prevents loan stacking by rejecting new applications if the customer has an existing pending loan (`PENDING_APPLICATION_EXISTS`).
   - Disallows loan applications from customers possessing frozen or compromised accounts (`BORROWER_ACCOUNT_NOT_ACTIVE`).

3. **`enforce_loan_workflow`** (`BEFORE UPDATE` on `loan_applications`):
   - Enforces a linear state machine: `SUBMITTED` -> `UNDERWRITE` (Senior Underwriter) -> `APPROVED`/`REJECTED` (Branch Manager).
   - Blocks unauthorized transitions, stage skipping, and status regression via `SECURITY DEFINER` runtime validation.

4. **`log_audit_event`** (`AFTER UPDATE` on `customer_accounts` & `loan_applications`):
   - Automatically and silently records mutating role, affected table, primary key, account number, prior state, new state, and current timestamp into `audit_log`.

---

## 5. Observability & Visualizer (Phase 4)

- **Live Trace & Trigger Pipeline**: Visual inspection container displaying validation outcomes with clear status indicators (`✓ passed`, `✕ failed`, `■ blocked`) and workflow transition pointers (`↓`).
- **Before / After Diff Viewer**: Real-time snapshot comparison engine displaying pre- and post-mutation balances (`-$500.00` / `+$500.00`) and operational status changes.
- **Architecture Flowchart (Mermaid)**: Dynamic diagram visualizing the query execution path across RBAC validation, trigger evaluations, and table mutations.

---

## 6. AI Practice Lab & Exam Evaluator (Phase 5)

Tab 5 provides an interactive learning environment for competitive examination mastery, triggers, and access control:

- **178 Curated Competitive Exam Questions**:
  - 50 Authentic GATE CS & DA Questions (2012–2026) verified against organizing IIT/IISc master papers.
  - 28 ISRO Scientist / Engineer Questions.
  - 50 NIELIT Scientist 'B' & Technical Assistant Questions.
  - 50 UGC-NET Computer Science Questions.
- **534 Pre-Defined Enterprise Practice Variants**:
  - 3 isomorphic, distinct domain variants for every single parent question:
    1. **Enterprise FinTech & Banking Ledger**: Focuses on core banking ledger integrity, transaction concurrency, and audit trails.
    2. **Healthcare & Clinical EMR Infrastructure**: Focuses on HIPAA-compliant medical records, HL7 schemas, and physician authorization.
    3. **E-Commerce & Supply Chain Logistics**: Focuses on inventory reserves, cart idempotency, flash sales, and order lifecycle states.
  - **Decoupled Key Alignment**: Variant answer keys are systematically permuted to prevent rote memorization while preserving underlying relational invariants.
- **Fine-Tuned Evaluator Model (`models/dbms-trigger-evaluator`)**:
  - Sentence Transformer model fine-tuned using MultipleNegativesRankingLoss.
  - Generates dense semantic embeddings for automated student answer evaluation on CPU in under 15 milliseconds.
  - Combines cosine similarity (`weight = 0.60`) with AST-extracted SQL concept invariant verification (`weight = 0.40`).

---

## 7. Project Structure

```
RBAC-Simulator-and-Trigger-Visualizer/
├── app.py                                    # Streamlit frontend with 5 integrated modules
├── config.py                                 # Roles, schemas, SQL definitions, and configurations
├── db_connection.py                          # Thread-safe pooled PostgreSQL connection manager
├── visualizer.py                             # Visual pipeline rendering, live trace, and diff viewers
├── requirements.txt                          # Production dependencies
├── README.md                                 # System architecture, RBAC matrix, and deployment guide
├── .gitignore                                # Exclusion rules for secrets, caches, and local files
├── competitive_exam_questions_and_answers.md # 178 Official questions & verified answer keys
├── competitive_exam_practice_variants.md     # 534 Pre-defined variants (FinTech, Healthcare, E-Commerce)
├── gate_pyq_evidence_matrix.md               # Verifiable audit matrix of GATE master papers
├── ai_engine/                                # AI practice and isomorphic problem generation
│   ├── evaluator.py                          # Hybrid AI evaluation engine (Embeddings + Invariants)
│   ├── exam_lab.py                           # Practice lab and question runner
│   ├── mcq_data.py                           # 178 official questions & 534 verified practice variants
│   ├── questions_data.py                     # Curated benchmark practice problems dataset
│   ├── train_embeddings.py                   # Fine-tuning script for sentence transformer model
│   └── tutor.py                              # Socratic tutor and variant scoring engine
├── models/
│   └── dbms-trigger-evaluator/                # Fine-tuned PyTorch / HuggingFace model weights
├── tests/
│   ├── conftest.py                           # Pytest database fixtures and transactional cleanup
│   ├── test_ai_evaluator.py                  # Unit tests for AI evaluation and invariant checks
│   ├── test_mcq_dataset.py                   # Unit tests for the 178 questions & 534 variants
│   └── test_triggers.py                      # Validation suite for Neon PostgreSQL triggers
└── .streamlit/
    ├── config.toml                           # Streamlit theme and server configuration
    └── secrets.toml.example                  # Safe credentials template for deployment
```

---

## 8. Local Setup & Execution Guide (Developer Notice)

### Prerequisites
- Python 3.10+
- Active PostgreSQL database (e.g., [Neon Serverless](https://neon.tech))

### Installation
```bash
# Clone the repository
git clone https://github.com/Sakthi-Sundar-M/RBAC-Simulator-and-Trigger-Visualizer-professor-copy-.git
cd RBAC-Simulator-and-Trigger-Visualizer-professor-copy-

# Set up virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Credentials Configuration
To run locally, you must provide valid Neon PostgreSQL credentials in `.streamlit/secrets.toml`:
```toml
DB_HOST = "your-database-host.neon.tech"
DB_NAME = "neondb"
DB_USER = "your_username"
DB_PASS = "your_secure_password"
DB_PORT = "5432"

# Optional: Gemini API key for dynamic AI assistant features
GEMINI_API_KEY = "your_gemini_api_key_here"
```

### Running Test Suite
```bash
python -m pytest tests/
```

### Launching the Application
```bash
streamlit run app.py
```

---

## 9. Streamlit Cloud Deployment Guide

1. Push your repository to GitHub.
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Select **"New app"**, configure your repository and branch (`main`), and set the main file path to `app.py`.
4. In **Advanced Settings -> Secrets**, paste your Neon PostgreSQL connection credentials:
   ```toml
   DB_HOST = "your-database-host.neon.tech"
   DB_NAME = "neondb"
   DB_USER = "your_username"
   DB_PASS = "your_secure_password"
   DB_PORT = "5432"
   GEMINI_API_KEY = "your_gemini_api_key"
   ```
5. Click **"Deploy"**. The application will automatically configure dependencies and start up.
