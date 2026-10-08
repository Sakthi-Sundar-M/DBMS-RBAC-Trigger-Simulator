import os
from typing import Dict, Any, Optional

def get_gemini_client():
    """
    Attempts to initialize Google GenAI SDK client using API key from:
    1. Streamlit secrets ([gemini] api_key or GEMINI_API_KEY)
    2. Environment variable GEMINI_API_KEY
    Returns client instance or None if not configured.
    """
    api_key = None
    try:
        import streamlit as st
        if hasattr(st, "secrets"):
            if "gemini" in st.secrets and "api_key" in st.secrets["gemini"]:
                api_key = st.secrets["gemini"]["api_key"]
            elif "GEMINI_API_KEY" in st.secrets:
                api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass

    if not api_key:
        api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        return None

    try:
        from google import genai
        return genai.Client(api_key=api_key)
    except Exception:
        return None


def diagnose_student_submission(question: Dict[str, Any], student_text: str, eval_result: Dict[str, Any]) -> str:
    """
    Generates a personalized, Socratic diagnostic critique of the student's submission.
    Explains the exact DBMS concept and why certain logic works or fails.
    Falls back to rubric-based diagnosis if Gemini API is offline.
    """
    client = get_gemini_client()
    if not client:
        # High-yield offline fallback diagnosis
        rubric = question.get("evaluation_rubric", {})
        common_mistakes = rubric.get("common_mistakes", [])
        missing = eval_result.get("missing_concepts", [])
        present_str = ", ".join(eval_result.get("present_concepts", [])) or "None yet identified"
        missing_str = ", ".join(missing) if missing else "All key concepts detected!"

        traps_html = "".join([f"<li style='margin: 1px 0;'><i>Trap:</i> {cm}</li>" for cm in common_mistakes])

        return f"""<div style="font-size: 13px; line-height: 1.35; color: #cbd5e1;">
<div style="margin-bottom: 5px; font-weight: 700; color: #f8fafc;">Diagnostic Review (Match: {eval_result.get('similarity_pct', 0)}% &bull; {eval_result.get('grade_band', 'Needs Review')}):</div>
<div style="margin-bottom: 2px;">&bull; <b>Target Concept:</b> {question.get('title')} ({question.get('subtopic')})</div>
<div style="margin-bottom: 2px;">&bull; <b>Concepts Verified:</b> {present_str}</div>
<div style="margin-bottom: 7px;">&bull; <b>Concepts Needing Attention:</b> {missing_str}</div>
<div style="margin-bottom: 2px; font-weight: 700; color: #f8fafc;">Relational Engine Ground Truth:</div>
<div style="margin-bottom: 7px; color: #cbd5e1;">{question.get('ground_truth_explanation', '')}</div>
<div style="margin-bottom: 2px; font-weight: 700; color: #f8fafc;">Common Exam Traps for this Problem:</div>
<ul style="margin: 2px 0 0 16px; padding: 0; color: #cbd5e1;">
{traps_html}
</ul>
</div>"""

    # Online diagnosis via Gemini 3.8 Flash
    prompt = f"""
You are an expert Database Management Systems (DBMS) professor evaluating a student's answer for an exam question on SQL Triggers & RBAC.

EXAM QUESTION:
Title: {question.get('title')}
Difficulty: {question.get('difficulty')}
Source: {question.get('source')}
Prompt: {question.get('prompt')}

OFFICIAL SOLUTION KEY:
{question.get('solution_key')}

ENGINE REASONING & GROUND TRUTH:
{question.get('ground_truth_explanation')}

EVALUATION RUBRIC:
Key Concepts: {question.get('evaluation_rubric', {}).get('key_concepts')}
Common Traps: {question.get('evaluation_rubric', {}).get('common_mistakes')}

STUDENT'S SUBMISSION:
\"\"\"{student_text}\"\"\"

EMBEDDING SIMILARITY METRIC:
Similarity Score: {eval_result.get('similarity_pct')}%
Missing Invariants: {eval_result.get('missing_concepts')}

INSTRUCTIONS:
1. Provide a concise, highly instructive Socratic critique (3-4 short paragraphs).
2. Point out what the student got right.
3. If they made a mistake (e.g. wrong trigger timing, missing transition variables, flawed RBAC grant), explain the physical relational database mechanism behind why that fails in PostgreSQL.
4. Do NOT just give the code answer away; guide their thinking.
5. Use clean markdown formatting without excessive symbols.
"""
    try:
        from google.genai import types
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction="You are a rigorous DBMS professor specializing in relational engines, PL/pgSQL procedural triggers, and database security.",
                temperature=0.3
            )
        )
        return response.text.strip()
    except Exception as e:
        return f"Offline Diagnostic fallback (API error: {str(e)}):\n\n{question.get('ground_truth_explanation', '')}"


def generate_socratic_hint(question: Dict[str, Any], student_text: str, hint_level: int = 1) -> str:
    """
    Generates a progressive Socratic hint (Level 1: General architectural direction,
    Level 2: Concrete hint targeting specific transition variables or syntax).
    """
    static_hints = question.get("hints", [])
    if hint_level <= len(static_hints):
        static_hint = static_hints[hint_level - 1]
    else:
        static_hint = static_hints[-1] if static_hints else "Review the relation schema and trigger lifecycle."

    client = get_gemini_client()
    if not client or not student_text.strip():
        return static_hint

    prompt = f"""
The student is solving this DBMS question:
{question.get('prompt')}

Student's current draft:
\"\"\"{student_text}\"\"\"

The verified solution is:
{question.get('solution_key')}

TASK:
Provide a progressive Socratic Hint (Level {hint_level} of 2).
- Level 1 should be a conceptual conceptual nudge without code.
- Level 2 can reference specific PostgreSQL variables (like NEW, OLD, BEFORE, or GRANT) without providing the final code solution.
- Keep it under 3 sentences.
"""
    try:
        from google.genai import types
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction="You are a Socratic DBMS tutor providing hints without revealing the full solution.",
                temperature=0.4
            )
        )
        return response.text.strip()
    except Exception:
        return static_hint


_DEPARTMENTS = [
    {
        "id": "fintech",
        "name": "FinTech & Digital Banking",
        "variations": [
            {
                "title": "Peer-to-Peer (P2P) Micro-Transfers & Wallets",
                "schema": "wallets(wallet_id INT PRIMARY KEY, user_id INT, balance NUMERIC, daily_limit NUMERIC, status TEXT);\ntransfers(transfer_id SERIAL PRIMARY KEY, sender_wallet INT REFERENCES wallets, receiver_wallet INT REFERENCES wallets, amount NUMERIC, fee NUMERIC, status TEXT, created_at TIMESTAMPTZ, approved_by TEXT);",
                "primary_table": "wallets",
                "event_table": "transfers",
                "audit_table": "transfer_audit_log(audit_id SERIAL PRIMARY KEY, transfer_id INT, old_status TEXT, new_status TEXT, changed_by TEXT, modified_at TIMESTAMPTZ)",
                "view_name": "v_user_transfer_summary",
                "primary_metric": "daily_limit",
                "metric_desc": "daily accumulated transfer limit",
                "roles": {"operator": "payment_processor", "officer": "compliance_auditor", "admin": "fintech_secadmin"}
            },
            {
                "title": "High-Frequency Forex & Algorithmic Trading",
                "schema": "trading_accounts(account_id INT PRIMARY KEY, trader_id INT, equity NUMERIC, margin_available NUMERIC, risk_tier TEXT, is_active BOOLEAN);\nlimit_orders(order_id SERIAL PRIMARY KEY, account_id INT REFERENCES trading_accounts, currency_pair VARCHAR(10), order_type VARCHAR(10), units NUMERIC, limit_price NUMERIC, status VARCHAR(20), placed_at TIMESTAMPTZ);",
                "primary_table": "trading_accounts",
                "event_table": "limit_orders",
                "audit_table": "margin_liquidation_log(log_id SERIAL PRIMARY KEY, account_id INT, order_id INT, margin_deficit NUMERIC, triggered_at TIMESTAMPTZ, authorized_by TEXT)",
                "view_name": "v_active_order_exposures",
                "primary_metric": "margin_available",
                "metric_desc": "maintenance margin buffer",
                "roles": {"operator": "day_trader", "officer": "risk_officer", "admin": "trading_secadmin"}
            },
            {
                "title": "Merchant Escrow & Payment Gateway Processing",
                "schema": "merchants(merchant_id INT PRIMARY KEY, business_name TEXT, reserve_balance NUMERIC, payout_schedule TEXT, risk_hold BOOLEAN);\ncard_settlements(txn_id SERIAL PRIMARY KEY, merchant_id INT REFERENCES merchants, card_hash VARCHAR(64), amount NUMERIC, dispute_status TEXT, settled_at TIMESTAMPTZ, processed_by TEXT);",
                "primary_table": "merchants",
                "event_table": "card_settlements",
                "audit_table": "escrow_dispute_audit(audit_id SERIAL PRIMARY KEY, txn_id INT, old_dispute_status TEXT, new_dispute_status TEXT, reviewed_by TEXT, changed_at TIMESTAMPTZ)",
                "view_name": "v_merchant_payout_ledger",
                "primary_metric": "reserve_balance",
                "metric_desc": "dispute collateral reserve balance",
                "roles": {"operator": "gateway_client", "officer": "fraud_investigator", "admin": "gateway_secadmin"}
            },
            {
                "title": "Corporate Syndicated Lending & Credit Line Facilities",
                "schema": "credit_facilities(facility_id INT PRIMARY KEY, borrower_org TEXT, credit_limit NUMERIC, drawn_amount NUMERIC, credit_rating VARCHAR(10), is_frozen BOOLEAN);\ndrawdown_requests(drawdown_id SERIAL PRIMARY KEY, facility_id INT REFERENCES credit_facilities, principal_req NUMERIC, term_months INT, approval_stage TEXT, requested_by TEXT, approved_by TEXT);",
                "primary_table": "credit_facilities",
                "event_table": "drawdown_requests",
                "audit_table": "credit_committee_audit(audit_id SERIAL PRIMARY KEY, facility_id INT, action_type TEXT, changed_by TEXT, timestamp TIMESTAMPTZ)",
                "view_name": "v_syndicated_facility_utilization",
                "primary_metric": "credit_limit",
                "metric_desc": "authorized facility credit ceiling",
                "roles": {"operator": "borrower_agent", "officer": "credit_risk_analyst", "admin": "syndicate_secadmin"}
            }
        ]
    },
    {
        "id": "aviation",
        "name": "Commercial Aviation & Flight Operations",
        "variations": [
            {
                "title": "Passenger Airline Seat Reservation & Overbooking Control",
                "schema": "flights(flight_no VARCHAR(10) PRIMARY KEY, origin VARCHAR(3), destination VARCHAR(3), max_capacity INT, booked_seats INT, base_fare NUMERIC, flight_status TEXT);\nseat_bookings(booking_id SERIAL PRIMARY KEY, flight_no VARCHAR(10) REFERENCES flights, passenger_id INT, seat_class VARCHAR(20), booking_status TEXT, booked_at TIMESTAMPTZ, agent_id TEXT);",
                "primary_table": "flights",
                "event_table": "seat_bookings",
                "audit_table": "flight_manifest_audit(log_id SERIAL PRIMARY KEY, booking_id INT, flight_no VARCHAR(10), action_type TEXT, changed_by TEXT, logged_at TIMESTAMPTZ)",
                "view_name": "v_flight_manifest_summary",
                "primary_metric": "booked_seats",
                "metric_desc": "maximum cabin seat capacity",
                "roles": {"operator": "passenger_portal", "officer": "flight_dispatcher", "admin": "airline_sysadmin"}
            },
            {
                "title": "Pilot & Cabin Crew FAA Duty Hours Flight Dispatch",
                "schema": "crew_members(crew_id INT PRIMARY KEY, full_name TEXT, crew_role VARCHAR(20), max_monthly_duty_hours NUMERIC, total_hours_flown NUMERIC, medical_cleared BOOLEAN);\nduty_rosters(roster_id SERIAL PRIMARY KEY, flight_no VARCHAR(10), crew_id INT REFERENCES crew_members, departure_time TIMESTAMPTZ, block_hours NUMERIC, validation_status TEXT, assigned_by TEXT);",
                "primary_table": "crew_members",
                "event_table": "duty_rosters",
                "audit_table": "faa_duty_audit_log(audit_id SERIAL PRIMARY KEY, crew_id INT, flight_no VARCHAR(10), violation_flag BOOLEAN, recorded_by TEXT, timestamp TIMESTAMPTZ)",
                "view_name": "v_crew_readiness_schedule",
                "primary_metric": "max_monthly_duty_hours",
                "metric_desc": "statutory flight duty safety hours",
                "roles": {"operator": "rostering_scheduler", "officer": "faa_compliance_auditor", "admin": "crew_ops_secadmin"}
            },
            {
                "title": "Air Freight Cargo Hold Weight & Dangerous Goods Manifest",
                "schema": "cargo_holds(hold_id INT PRIMARY KEY, flight_no VARCHAR(10), max_payload_kg NUMERIC, current_payload_kg NUMERIC, hazmat_certified BOOLEAN);\ncargo_pallets(pallet_id SERIAL PRIMARY KEY, hold_id INT REFERENCES cargo_holds, weight_kg NUMERIC, hazmat_class VARCHAR(10), manifest_status TEXT, loaded_at TIMESTAMPTZ, verified_by TEXT);",
                "primary_table": "cargo_holds",
                "event_table": "cargo_pallets",
                "audit_table": "cargo_weight_audit(log_id SERIAL PRIMARY KEY, hold_id INT, pallet_id INT, old_weight NUMERIC, new_weight NUMERIC, logged_at TIMESTAMPTZ)",
                "view_name": "v_aircraft_weight_distribution",
                "primary_metric": "current_payload_kg",
                "metric_desc": "gross airframe payload limit",
                "roles": {"operator": "ramp_agent", "officer": "cargo_loadmaster", "admin": "freight_secadmin"}
            },
            {
                "title": "Frequent Flyer Mileage Accruals & Tier Expirations",
                "schema": "loyalty_accounts(account_id INT PRIMARY KEY, member_id INT, tier_level VARCHAR(20), point_balance NUMERIC, tier_expiry DATE, is_locked BOOLEAN);\nmileage_accruals(txn_id SERIAL PRIMARY KEY, account_id INT REFERENCES loyalty_accounts, flight_no VARCHAR(10), points_earned NUMERIC, redemption_flag BOOLEAN, processed_by TEXT, processed_at TIMESTAMPTZ);",
                "primary_table": "loyalty_accounts",
                "event_table": "mileage_accruals",
                "audit_table": "points_ledger_audit(audit_id SERIAL PRIMARY KEY, account_id INT, txn_id INT, points_delta NUMERIC, actor_id TEXT, recorded_at TIMESTAMPTZ)",
                "view_name": "v_tier_status_accruals",
                "primary_metric": "point_balance",
                "metric_desc": "mileage reward points balance",
                "roles": {"operator": "rewards_partner", "officer": "loyalty_fraud_analyst", "admin": "rewards_secadmin"}
            }
        ]
    },
    {
        "id": "healthcare",
        "name": "Healthcare & Hospital Administration",
        "variations": [
            {
                "title": "Emergency Room & ICU Critical Bed Allocation",
                "schema": "icu_wards(ward_id INT PRIMARY KEY, ward_name TEXT, total_critical_beds INT, occupied_beds INT, nurse_ratio NUMERIC, is_quarantined BOOLEAN);\nbed_assignments(assignment_id SERIAL PRIMARY KEY, ward_id INT REFERENCES icu_wards, patient_mrn VARCHAR(20), acuity_score INT, status TEXT, assigned_at TIMESTAMPTZ, admitting_doctor TEXT);",
                "primary_table": "icu_wards",
                "event_table": "bed_assignments",
                "audit_table": "icu_triage_audit(audit_id SERIAL PRIMARY KEY, assignment_id INT, ward_id INT, triage_decision TEXT, doctor_id TEXT, timestamp TIMESTAMPTZ)",
                "view_name": "v_icu_occupancy_overview",
                "primary_metric": "occupied_beds",
                "metric_desc": "available critical care bed count",
                "roles": {"operator": "triage_nurse", "officer": "chief_medical_officer", "admin": "hospital_secadmin"}
            },
            {
                "title": "Hospital Pharmacy Controlled Substance Vault Dispensing",
                "schema": "narcotic_vault(drug_code VARCHAR(20) PRIMARY KEY, drug_name TEXT, schedule_class VARCHAR(5), on_hand_units NUMERIC, safe_threshold NUMERIC, is_controlled BOOLEAN);\ndispensation_logs(log_id SERIAL PRIMARY KEY, drug_code VARCHAR(20) REFERENCES narcotic_vault, doctor_dea_license VARCHAR(30), patient_mrn VARCHAR(20), dosage_mg NUMERIC, dispensed_at TIMESTAMPTZ, dispensing_pharmacist TEXT);",
                "primary_table": "narcotic_vault",
                "event_table": "dispensation_logs",
                "audit_table": "dea_substance_audit(audit_id SERIAL PRIMARY KEY, log_id INT, drug_code VARCHAR(20), units_dispensed NUMERIC, inspector_id TEXT, audited_at TIMESTAMPTZ)",
                "view_name": "v_pharmacy_narcotic_inventory",
                "primary_metric": "safe_threshold",
                "metric_desc": "statutory DEA vault floor threshold",
                "roles": {"operator": "dispensing_pharmacist", "officer": "pharmacy_director", "admin": "hipaa_secadmin"}
            },
            {
                "title": "Operating Theater Surgical Suite Scheduling & Preemption",
                "schema": "operating_theaters(theater_id INT PRIMARY KEY, suite_name TEXT, is_active BOOLEAN, scheduled_surgeries INT, max_daily_procedures INT);\nsurgical_bookings(booking_id SERIAL PRIMARY KEY, theater_id INT REFERENCES operating_theaters, lead_surgeon_id INT, procedure_code VARCHAR(20), priority_level INT, scheduled_start TIMESTAMPTZ, booked_by TEXT);",
                "primary_table": "operating_theaters",
                "event_table": "surgical_bookings",
                "audit_table": "theater_reschedule_audit(audit_id SERIAL PRIMARY KEY, booking_id INT, old_time TIMESTAMPTZ, new_time TIMESTAMPTZ, reason TEXT, logged_at TIMESTAMPTZ)",
                "view_name": "v_surgical_theater_utilization",
                "primary_metric": "scheduled_surgeries",
                "metric_desc": "daily theater procedural allocation",
                "roles": {"operator": "surgical_coordinator", "officer": "clinical_director", "admin": "theater_secadmin"}
            },
            {
                "title": "Pathology Diagnostic Reports & HIPAA Access Audit",
                "schema": "patient_records(record_id INT PRIMARY KEY, patient_mrn VARCHAR(20), confidentiality_level VARCHAR(20), attending_physician_id INT, is_sealed BOOLEAN);\nlab_diagnostics(test_id SERIAL PRIMARY KEY, record_id INT REFERENCES patient_records, pathologist_id INT, lab_result_data TEXT, approval_status TEXT, verified_at TIMESTAMPTZ, entered_by TEXT);",
                "primary_table": "patient_records",
                "event_table": "lab_diagnostics",
                "audit_table": "hipaa_phi_access_log(audit_id SERIAL PRIMARY KEY, record_id INT, viewer_role TEXT, query_context TEXT, access_granted BOOLEAN, accessed_at TIMESTAMPTZ)",
                "view_name": "v_pathology_verified_results",
                "primary_metric": "confidentiality_level",
                "metric_desc": "protected health privacy classification",
                "roles": {"operator": "lab_technician", "officer": "privacy_officer", "admin": "ehr_secadmin"}
            }
        ]
    },
    {
        "id": "cloud",
        "name": "Cloud Infrastructure & Cybersecurity",
        "variations": [
            {
                "title": "Multi-Tenant Virtual Compute & Hypervisor Quota Engine",
                "schema": "tenant_quotas(tenant_id INT PRIMARY KEY, org_name TEXT, max_vcpus INT, allocated_vcpus INT, max_ram_gb INT, is_suspended BOOLEAN);\nvirtual_machines(vm_id SERIAL PRIMARY KEY, tenant_id INT REFERENCES tenant_quotas, vcpu_count INT, ram_gb INT, power_state TEXT, launched_at TIMESTAMPTZ, launched_by TEXT);",
                "primary_table": "tenant_quotas",
                "event_table": "virtual_machines",
                "audit_table": "hypervisor_quota_audit(audit_id SERIAL PRIMARY KEY, tenant_id INT, event_type TEXT, old_vcpus INT, new_vcpus INT, logged_at TIMESTAMPTZ)",
                "view_name": "v_tenant_resource_consumption",
                "primary_metric": "allocated_vcpus",
                "metric_desc": "tenant hardware vCPU core quota",
                "roles": {"operator": "devops_engineer", "officer": "cloud_finops_auditor", "admin": "cloud_iam_admin"}
            },
            {
                "title": "Distributed API Gateway Rate-Limiting & Token Buckets",
                "schema": "api_consumers(api_key_id VARCHAR(64) PRIMARY KEY, tenant_id INT, plan_tier VARCHAR(20), burst_limit INT, current_window_tokens INT, is_throttled BOOLEAN);\ntraffic_requests(req_id SERIAL PRIMARY KEY, api_key_id VARCHAR(64) REFERENCES api_consumers, endpoint_path TEXT, http_status INT, latency_ms INT, req_timestamp TIMESTAMPTZ);",
                "primary_table": "api_consumers",
                "event_table": "traffic_requests",
                "audit_table": "rate_limit_throttle_log(log_id SERIAL PRIMARY KEY, api_key_id VARCHAR(64), throttled_count INT, violation_window TIMESTAMPTZ, logged_at TIMESTAMPTZ)",
                "view_name": "v_api_gateway_metrics",
                "primary_metric": "current_window_tokens",
                "metric_desc": "token bucket burst limit",
                "roles": {"operator": "api_consumer_app", "officer": "api_platform_lead", "admin": "gateway_secadmin"}
            },
            {
                "title": "Object Storage Encrypted Buckets & Immutable WORM Retention",
                "schema": "storage_buckets(bucket_id INT PRIMARY KEY, bucket_name TEXT, retention_days INT, worm_locked BOOLEAN, current_storage_bytes BIGINT);\nstored_objects(object_id SERIAL PRIMARY KEY, bucket_id INT REFERENCES storage_buckets, object_key TEXT, size_bytes BIGINT, retention_until TIMESTAMPTZ, is_deleted BOOLEAN, uploaded_by TEXT);",
                "primary_table": "storage_buckets",
                "event_table": "stored_objects",
                "audit_table": "bucket_compliance_audit(audit_id SERIAL PRIMARY KEY, bucket_id INT, object_id INT, attempted_op TEXT, blocked BOOLEAN, timestamp TIMESTAMPTZ)",
                "view_name": "v_immutable_bucket_contents",
                "primary_metric": "retention_days",
                "metric_desc": "regulatory immutable WORM retention window",
                "roles": {"operator": "backup_agent", "officer": "compliance_auditor", "admin": "storage_secadmin"}
            },
            {
                "title": "IAM Cloud Roles & Ephemeral Identity Access Management",
                "schema": "iam_roles(role_id INT PRIMARY KEY, role_name TEXT, trust_policy JSONB, max_session_minutes INT, is_privileged BOOLEAN);\nsession_grants(session_id SERIAL PRIMARY KEY, role_id INT REFERENCES iam_roles, assumed_by_arn TEXT, ip_cidr CIDR, session_expires_at TIMESTAMPTZ, revoked_at TIMESTAMPTZ, granted_by TEXT);",
                "primary_table": "iam_roles",
                "event_table": "session_grants",
                "audit_table": "iam_privilege_audit(audit_id SERIAL PRIMARY KEY, session_id INT, action_name TEXT, caller_arn TEXT, status TEXT, logged_at TIMESTAMPTZ)",
                "view_name": "v_active_role_sessions",
                "primary_metric": "max_session_minutes",
                "metric_desc": "ephemeral session lease timeout",
                "roles": {"operator": "workload_service", "officer": "security_analyst", "admin": "root_iam_admin"}
            }
        ]
    },
    {
        "id": "logistics",
        "name": "Global Logistics & Supply Chain",
        "variations": [
            {
                "title": "Automated Fulfillment Center Bin Replenishment & Stockouts",
                "schema": "warehouse_bins(bin_id INT PRIMARY KEY, sku VARCHAR(30), aisle_zone VARCHAR(10), current_stock_qty INT, min_reorder_qty INT, is_active BOOLEAN);\npick_tasks(task_id SERIAL PRIMARY KEY, bin_id INT REFERENCES warehouse_bins, picker_id INT, requested_qty INT, status TEXT, picked_at TIMESTAMPTZ, supervisor_id TEXT);",
                "primary_table": "warehouse_bins",
                "event_table": "pick_tasks",
                "audit_table": "stock_reconciliation_audit(audit_id SERIAL PRIMARY KEY, bin_id INT, old_stock INT, new_stock INT, delta_reason TEXT, timestamp TIMESTAMPTZ)",
                "view_name": "v_warehouse_inventory_status",
                "primary_metric": "current_stock_qty",
                "metric_desc": "minimum inventory safety buffer",
                "roles": {"operator": "picker_robot", "officer": "inventory_controller", "admin": "wms_sysadmin"}
            },
            {
                "title": "E-Commerce Flash-Sale Concurrency & Order Allocation",
                "schema": "flash_events(sale_id INT PRIMARY KEY, sku VARCHAR(30), event_capacity INT, reserved_units INT, max_per_customer INT, is_live BOOLEAN);\norder_reservations(reservation_id SERIAL PRIMARY KEY, sale_id INT REFERENCES flash_events, customer_id INT, quantity INT, expires_at TIMESTAMPTZ, checkout_state TEXT, reserved_by TEXT);",
                "primary_table": "flash_events",
                "event_table": "order_reservations",
                "audit_table": "flash_reservation_audit(audit_id SERIAL PRIMARY KEY, reservation_id INT, sale_id INT, state_change TEXT, logged_at TIMESTAMPTZ)",
                "view_name": "v_flash_sale_active_reservations",
                "primary_metric": "reserved_units",
                "metric_desc": "flash sale promotional quota",
                "roles": {"operator": "customer_checkout_svc", "officer": "merchandise_lead", "admin": "ecomm_secadmin"}
            },
            {
                "title": "Cold-Chain Pharmaceutical Logistics & Temperature Monitoring",
                "schema": "cold_containers(container_id INT PRIMARY KEY, consignment_code VARCHAR(30), target_temp_c NUMERIC, min_temp_c NUMERIC, max_temp_c NUMERIC, is_spoiled BOOLEAN);\ntelemetry_logs(telemetry_id SERIAL PRIMARY KEY, container_id INT REFERENCES cold_containers, recorded_temp_c NUMERIC, battery_pct NUMERIC, recorded_at TIMESTAMPTZ, sensor_status TEXT);",
                "primary_table": "cold_containers",
                "event_table": "telemetry_logs",
                "audit_table": "cold_chain_breach_audit(audit_id SERIAL PRIMARY KEY, container_id INT, excursion_temp NUMERIC, duration_mins INT, logged_at TIMESTAMPTZ)",
                "view_name": "v_active_cold_chain_monitors",
                "primary_metric": "target_temp_c",
                "metric_desc": "cold chain safe thermal excursion limits",
                "roles": {"operator": "iot_sensor_gateway", "officer": "gdp_quality_inspector", "admin": "logistics_sysadmin"}
            },
            {
                "title": "Intermodal Port Terminal Drayage & Container Berths",
                "schema": "berth_slots(berth_id INT PRIMARY KEY, terminal_name VARCHAR(30), max_teu_capacity INT, current_teu INT, quay_crane_count INT, status VARCHAR(20));\nvessel_calls(call_id SERIAL PRIMARY KEY, berth_id INT REFERENCES berth_slots, vessel_imo VARCHAR(20), scheduled_dock_time TIMESTAMPTZ, discharged_teu INT, call_status VARCHAR(20), harbor_pilot_id TEXT);",
                "primary_table": "berth_slots",
                "event_table": "vessel_calls",
                "audit_table": "port_berth_manifest_audit(audit_id SERIAL PRIMARY KEY, call_id INT, berth_id INT, old_teu INT, new_teu INT, timestamp TIMESTAMPTZ)",
                "view_name": "v_terminal_berth_occupancy",
                "primary_metric": "current_teu",
                "metric_desc": "intermodal berth TEU intake limit",
                "roles": {"operator": "stevedore_operator", "officer": "harbor_master", "admin": "port_secadmin"}
            }
        ]
    }
]

_question_variation_counters: Dict[str, int] = {}
_question_department_indices: Dict[str, int] = {}


def get_all_departments():
    """Returns metadata for all 5 enterprise departments."""
    return [{"id": d["id"], "name": d["name"], "variation_count": len(d["variations"])} for d in _DEPARTMENTS]


def _build_solution_and_rubric(
    concept_key: str,
    sec_title: str,
    prim: str,
    evt: str,
    aud: str,
    vw: str,
    metric: str,
    metric_desc: str,
    roles: Dict[str, str],
    key_invariant: str,
    question: Dict[str, Any]
) -> tuple:
    aud_tbl = aud.split('(')[0].strip()

    if concept_key == "eca":
        starter = (
            f"-- ECA Model Breakdown for {sec_title}:\n"
            f"-- 1. Event (DML Operation & Timing on {evt}):\n"
            f"-- 2. Condition (Transient Buffer Predicate on NEW/OLD):\n"
            f"-- 3. Action (PL/pgSQL Procedural Execution on {prim}):\n"
            f"-- Gatekeeper Primitive (Which component controls execution):\n"
        )
        solution = (
            f"-- 1. Event: BEFORE or AFTER INSERT/UPDATE ON {evt} (initiates the active rule engine).\n"
            f"-- 2. Condition: A boolean predicate (e.g. WHEN clause or IF check on NEW.{metric}) evaluated against transition records.\n"
            f"-- 3. Action: Procedural PL/pgSQL block (e.g. UPDATE {prim} ... or RAISE EXCEPTION) executed when condition is TRUE.\n"
            f"-- Gatekeeper Primitive: The Condition gates whether the Action executes or is bypassed."
        )
        checks = [
            {"label": "Defines Event operation and timing", "pattern": ["event", "insert", "update", "delete", "before", "after"]},
            {"label": "Defines Condition predicate on NEW/OLD", "pattern": ["condition", "when", "predicate", "boolean", "new", "old"]},
            {"label": "Defines Action procedural logic", "pattern": ["action", "procedure", "pl/pgsql", "raise", "update"]},
            {"label": "Identifies Condition as the gatekeeper primitive", "pattern": ["condition"]}
        ]

    elif concept_key == "insert_transition":
        starter = (
            f"-- Analyze Transition Variables during INSERT into {evt}:\n"
            f"-- 1. State & Accessibility of NEW:\n"
            f"-- 2. State & Accessibility of OLD:\n"
            f"-- 3. Storage Engine Reason why OLD is invalid during INSERT:\n"
        )
        solution = (
            f"-- 1. NEW: Fully populated with candidate tuple proposed for {evt}. Modifiable in BEFORE INSERT triggers.\n"
            f"-- 2. OLD: Unassigned / NULL (undefined). Attempting to read or mutate OLD raises a runtime exception or yields NULL.\n"
            f"-- 3. Storage Engine Reason: An INSERT introduces a brand-new tuple where no pre-existing disk state exists on the relation heap."
        )
        checks = [
            {"label": "Explains NEW holds candidate tuple", "pattern": ["new", "candidate", "proposed", "inserted"]},
            {"label": "Explains OLD is NULL / undefined", "pattern": ["old", "null", "undefined"]},
            {"label": "Identifies absence of pre-existing disk state", "pattern": ["disk", "heap", "prior", "exist", "initial"]}
        ]

    elif concept_key == "delete_transition":
        starter = (
            f"-- Analyze Transition Variables during DELETE on {evt}:\n"
            f"-- 1. State of OLD during DELETE:\n"
            f"-- 2. State of NEW during DELETE:\n"
            f"-- 3. Archival trigger function into {aud_tbl}:\n"
            f"CREATE OR REPLACE FUNCTION fn_archive_{evt}() RETURNS TRIGGER AS $$\n"
            f"BEGIN\n"
            f"    -- Archive departing row:\n"
            f"    RETURN OLD;\n"
            f"END;\n"
            f"$$ LANGUAGE plpgsql;\n"
        )
        solution = (
            f"-- 1. OLD: Fully populated with the row scheduled for deletion from {evt}.\n"
            f"-- 2. NEW: Unassigned / NULL because no replacement tuple exists during deletion.\n"
            f"-- 3. Archival trigger function:\n"
            f"CREATE OR REPLACE FUNCTION fn_archive_{evt}() RETURNS TRIGGER AS $$\n"
            f"BEGIN\n"
            f"    INSERT INTO {aud_tbl} VALUES (DEFAULT, OLD.id, 'DELETED', session_user, clock_timestamp());\n"
            f"    RETURN OLD;\n"
            f"END;\n"
            f"$$ LANGUAGE plpgsql;\n\n"
            f"CREATE TRIGGER trg_archive_{evt}\n"
            f"BEFORE DELETE ON {evt}\n"
            f"FOR EACH ROW\n"
            f"EXECUTE FUNCTION fn_archive_{evt}();"
        )
        checks = [
            {"label": "Identifies OLD holds departing row", "pattern": ["old"]},
            {"label": "Identifies NEW is undefined/NULL", "pattern": ["new", "null", "undefined"]},
            {"label": f"Archives to audit log {aud_tbl}", "pattern": [aud_tbl, "archive", "insert into"]}
        ]

    elif concept_key == "grant_revoke":
        starter = (
            f"-- 1. Create role {roles['officer']} with login:\n\n"
            f"-- 2. Grant SELECT on {prim} and {evt} to {roles['officer']}:\n\n"
            f"-- 3. Grant INSERT, UPDATE on {evt} to {roles['operator']}:\n\n"
            f"-- 4. Revoke privileges on {aud_tbl} from {roles['operator']}:\n"
        )
        solution = (
            f"CREATE ROLE {roles['officer']} WITH LOGIN PASSWORD 'secure_pass';\n\n"
            f"GRANT SELECT ON {prim}, {evt} TO {roles['officer']};\n\n"
            f"GRANT INSERT, UPDATE ON {evt} TO {roles['operator']};\n\n"
            f"REVOKE ALL PRIVILEGES ON {aud_tbl} FROM {roles['operator']};"
        )
        checks = [
            {"label": f"Creates role {roles['officer']} with LOGIN", "pattern": ["create role", "login"]},
            {"label": f"Grants SELECT on {prim} or {evt}", "pattern": ["grant select", roles['officer']]},
            {"label": f"Grants INSERT/UPDATE on {evt}", "pattern": ["grant insert", roles['operator']]},
            {"label": f"Revokes privileges from {roles['operator']}", "pattern": ["revoke", roles['operator']]}
        ]

    elif concept_key == "before_after":
        starter = (
            f"-- 1. Which timing mutates candidate NEW values before heap write:\n"
            f"-- 2. Which timing records audit entries in {aud_tbl} with generated keys:\n"
            f"-- 3. Transaction rollback behavior when exception occurs in AFTER vs BEFORE:\n"
        )
        solution = (
            f"-- 1. BEFORE triggers: Can sanitize, normalize, and modify candidate values in NEW before disk write.\n"
            f"-- 2. AFTER triggers: Executed after tuple insertion when serial primary keys are generated, ideal for audit logs.\n"
            f"-- 3. Atomicity: An unhandled exception in either timing aborts the entire transaction and rolls back all writes."
        )
        checks = [
            {"label": "Identifies BEFORE modifies in-flight tuples", "pattern": ["before", "modify", "sanitize", "in-flight"]},
            {"label": "Identifies AFTER logs generated keys", "pattern": ["after", "serial", "key", "audit", "committed"]},
            {"label": "Explains atomic rollback on exception", "pattern": ["rollback", "atomicity", "abort", "transaction"]}
        ]

    elif concept_key == "value_guard":
        starter = (
            f"CREATE OR REPLACE FUNCTION fn_guard_{metric}()\n"
            f"RETURNS TRIGGER AS $$\n"
            f"BEGIN\n"
            f"    -- Validate NEW.{metric} against OLD.{metric}:\n"
            f"    \n"
            f"    RETURN NEW;\n"
            f"END;\n"
            f"$$ LANGUAGE plpgsql;\n\n"
            f"CREATE TRIGGER trg_guard_{metric}\n"
            f"BEFORE UPDATE ON {prim}\n"
            f"FOR EACH ROW\n"
            f"EXECUTE FUNCTION fn_guard_{metric}();"
        )
        solution = (
            f"CREATE OR REPLACE FUNCTION fn_guard_{metric}()\n"
            f"RETURNS TRIGGER AS $$\n"
            f"BEGIN\n"
            f"    IF NEW.{metric} < OLD.{metric} THEN\n"
            f"        RAISE EXCEPTION 'Monotonic integrity violation: % cannot be reduced from % to %',\n"
            f"            '{metric}', OLD.{metric}, NEW.{metric};\n"
            f"    END IF;\n"
            f"    RETURN NEW;\n"
            f"END;\n"
            f"$$ LANGUAGE plpgsql;\n\n"
            f"CREATE TRIGGER trg_guard_{metric}\n"
            f"BEFORE UPDATE ON {prim}\n"
            f"FOR EACH ROW\n"
            f"EXECUTE FUNCTION fn_guard_{metric}();"
        )
        checks = [
            {"label": f"Compares NEW.{metric} with OLD.{metric}", "pattern": ["new." + metric, "old." + metric, "new", "old"]},
            {"label": "Uses RAISE EXCEPTION on illegal decrease", "pattern": ["raise exception"]},
            {"label": "Returns NEW on valid modification", "pattern": ["return new"]},
            {"label": f"Defines BEFORE UPDATE ON {prim}", "pattern": ["before update on " + prim, "before update"]}
        ]

    elif concept_key == "cascading":
        starter = (
            f"-- 1. ACID Transaction Atomicity across Trigger Cascade:\n"
            f"-- 2. Rollback Scope when Secondary Trigger on {aud_tbl} Fails:\n"
            f"-- 3. Independent Commit Capability of Triggers:\n"
        )
        solution = (
            f"-- 1. All cascading triggers execute within the single top-level ACID transaction boundary.\n"
            f"-- 2. If the secondary trigger on {aud_tbl} raises an exception, all modifications to {prim} and {evt} roll back atomically.\n"
            f"-- 3. Triggers cannot commit independently; they are strictly bound to the enclosing transaction."
        )
        checks = [
            {"label": "Explains single ACID transaction boundary", "pattern": ["acid", "boundary", "transaction", "same"]},
            {"label": "Explains atomic rollback of all preceding writes", "pattern": ["rollback", "abort", "atomically", "all"]},
            {"label": "Explains triggers cannot commit independently", "pattern": ["commit", "independent", "cannot"]}
        ]

    elif concept_key == "mutating_table":
        starter = (
            f"CREATE OR REPLACE FUNCTION fn_prevent_recursion()\n"
            f"RETURNS TRIGGER AS $$\n"
            f"BEGIN\n"
            f"    -- Terminate recursive loop if depth > 1:\n"
            f"    \n"
            f"    RETURN NEW;\n"
            f"END;\n"
            f"$$ LANGUAGE plpgsql;"
        )
        solution = (
            f"CREATE OR REPLACE FUNCTION fn_prevent_recursion()\n"
            f"RETURNS TRIGGER AS $$\n"
            f"BEGIN\n"
            f"    -- Break infinite recursion if nesting depth exceeds 1\n"
            f"    IF pg_trigger_depth() > 1 THEN\n"
            f"        RETURN NEW;\n"
            f"    END IF;\n\n"
            f"    UPDATE {prim} SET ... WHERE ...;\n"
            f"    RETURN NEW;\n"
            f"END;\n"
            f"$$ LANGUAGE plpgsql;\n\n"
            f"CREATE TRIGGER trg_recursion_guard\n"
            f"AFTER UPDATE ON {prim}\n"
            f"FOR EACH ROW\n"
            f"EXECUTE FUNCTION fn_prevent_recursion();"
        )
        checks = [
            {"label": "Uses pg_trigger_depth() inspection", "pattern": ["pg_trigger_depth"]},
            {"label": "Returns early when depth > 1", "pattern": ["return new", "return"]},
            {"label": f"Defines trigger on {prim}", "pattern": [prim]}
        ]

    elif concept_key == "state_machine":
        starter = (
            f"CREATE OR REPLACE FUNCTION fn_validate_lifecycle()\n"
            f"RETURNS TRIGGER AS $$\n"
            f"BEGIN\n"
            f"    -- Validate (OLD.status, NEW.status) transitions:\n"
            f"    \n"
            f"    RETURN NEW;\n"
            f"END;\n"
            f"$$ LANGUAGE plpgsql;"
        )
        solution = (
            f"CREATE OR REPLACE FUNCTION fn_validate_lifecycle()\n"
            f"RETURNS TRIGGER AS $$\n"
            f"BEGIN\n"
            f"    IF OLD.status = 'SETTLED' THEN\n"
            f"        RAISE EXCEPTION 'Cannot modify record in terminal state';\n"
            f"    END IF;\n\n"
            f"    IF NOT (\n"
            f"        (OLD.status = 'DRAFT' AND NEW.status = 'SUBMITTED') OR\n"
            f"        (OLD.status = 'SUBMITTED' AND NEW.status = 'UNDER_REVIEW') OR\n"
            f"        (OLD.status = 'UNDER_REVIEW' AND NEW.status IN ('APPROVED', 'REJECTED')) OR\n"
            f"        (OLD.status = 'APPROVED' AND NEW.status = 'SETTLED')\n"
            f"    ) THEN\n"
            f"        RAISE EXCEPTION 'Illegal state transition from % to %', OLD.status, NEW.status;\n"
            f"    END IF;\n"
            f"    RETURN NEW;\n"
            f"END;\n"
            f"$$ LANGUAGE plpgsql;\n\n"
            f"CREATE TRIGGER trg_state_lifecycle\n"
            f"BEFORE UPDATE ON {evt}\n"
            f"FOR EACH ROW\n"
            f"WHEN (OLD.status IS DISTINCT FROM NEW.status)\n"
            f"EXECUTE FUNCTION fn_validate_lifecycle();"
        )
        checks = [
            {"label": "Validates OLD.status and NEW.status", "pattern": ["old.status", "new.status", "status"]},
            {"label": "Raises exception on illegal jump", "pattern": ["raise exception"]},
            {"label": f"Defines BEFORE UPDATE trigger on {evt}", "pattern": ["before update on " + evt, "before update"]}
        ]

    elif concept_key == "instead_of":
        starter = (
            f"CREATE OR REPLACE FUNCTION fn_{vw}_router()\n"
            f"RETURNS TRIGGER AS $$\n"
            f"BEGIN\n"
            f"    -- Decompose INSERT to base tables {prim} and {evt}:\n"
            f"    \n"
            f"    RETURN NEW;\n"
            f"END;\n"
            f"$$ LANGUAGE plpgsql;\n\n"
            f"CREATE TRIGGER trg_{vw}_insert\n"
            f"INSTEAD OF INSERT ON {vw}\n"
            f"FOR EACH ROW\n"
            f"EXECUTE FUNCTION fn_{vw}_router();"
        )
        solution = (
            f"CREATE OR REPLACE FUNCTION fn_{vw}_router()\n"
            f"RETURNS TRIGGER AS $$\n"
            f"BEGIN\n"
            f"    INSERT INTO {prim} VALUES (NEW.id, ...)\n"
            f"    ON CONFLICT (id) DO NOTHING;\n\n"
            f"    INSERT INTO {evt} VALUES (DEFAULT, NEW.id, ...);\n\n"
            f"    RETURN NEW;\n"
            f"END;\n"
            f"$$ LANGUAGE plpgsql;\n\n"
            f"CREATE TRIGGER trg_{vw}_insert\n"
            f"INSTEAD OF INSERT ON {vw}\n"
            f"FOR EACH ROW\n"
            f"EXECUTE FUNCTION fn_{vw}_router();"
        )
        checks = [
            {"label": f"Defines INSTEAD OF INSERT ON {vw}", "pattern": ["instead of insert", vw]},
            {"label": f"Decomposes write to base table {prim}", "pattern": [prim]},
            {"label": f"Decomposes write to base table {evt}", "pattern": [evt]},
            {"label": "Returns NEW in trigger function", "pattern": ["return new"]}
        ]

    elif concept_key == "append_only":
        starter = (
            f"CREATE OR REPLACE FUNCTION fn_immutable_{aud_tbl}()\n"
            f"RETURNS TRIGGER AS $$\n"
            f"BEGIN\n"
            f"    -- Forbid all UPDATE and DELETE mutations:\n"
            f"    \n"
            f"    RETURN NULL;\n"
            f"END;\n"
            f"$$ LANGUAGE plpgsql;"
        )
        solution = (
            f"CREATE OR REPLACE FUNCTION fn_immutable_{aud_tbl}()\n"
            f"RETURNS TRIGGER AS $$\n"
            f"BEGIN\n"
            f"    RAISE EXCEPTION 'Append-only ledger violation: UPDATE and DELETE are prohibited on %', TG_TABLE_NAME;\n"
            f"    RETURN NULL;\n"
            f"END;\n"
            f"$$ LANGUAGE plpgsql;\n\n"
            f"CREATE TRIGGER trg_append_only\n"
            f"BEFORE UPDATE OR DELETE ON {aud_tbl}\n"
            f"FOR EACH ROW\n"
            f"EXECUTE FUNCTION fn_immutable_{aud_tbl}();"
        )
        checks = [
            {"label": "Unconditionally raises exception on mutation", "pattern": ["raise exception"]},
            {"label": "Intercepts BEFORE UPDATE OR DELETE", "pattern": ["before update or delete", "before update", "before delete"]},
            {"label": f"Attached to audit relation {aud_tbl}", "pattern": [aud_tbl]}
        ]

    elif concept_key == "tg_op":
        starter = (
            f"CREATE OR REPLACE FUNCTION fn_multi_event_audit()\n"
            f"RETURNS TRIGGER AS $$\n"
            f"BEGIN\n"
            f"    -- Branch logic using TG_OP ('INSERT', 'UPDATE', 'DELETE'):\n"
            f"    \n"
            f"    RETURN NULL;\n"
            f"END;\n"
            f"$$ LANGUAGE plpgsql;"
        )
        solution = (
            f"CREATE OR REPLACE FUNCTION fn_multi_event_audit()\n"
            f"RETURNS TRIGGER AS $$\n"
            f"BEGIN\n"
            f"    IF (TG_OP = 'INSERT') THEN\n"
            f"        INSERT INTO {aud_tbl} VALUES (DEFAULT, NEW.id, 'INSERT', session_user, clock_timestamp());\n"
            f"        RETURN NEW;\n"
            f"    ELSIF (TG_OP = 'UPDATE') THEN\n"
            f"        INSERT INTO {aud_tbl} VALUES (DEFAULT, NEW.id, 'UPDATE', session_user, clock_timestamp());\n"
            f"        RETURN NEW;\n"
            f"    ELSIF (TG_OP = 'DELETE') THEN\n"
            f"        INSERT INTO {aud_tbl} VALUES (DEFAULT, OLD.id, 'DELETE', session_user, clock_timestamp());\n"
            f"        RETURN OLD;\n"
            f"    END IF;\n"
            f"    RETURN NULL;\n"
            f"END;\n"
            f"$$ LANGUAGE plpgsql;\n\n"
            f"CREATE TRIGGER trg_audit_{evt}\n"
            f"AFTER INSERT OR UPDATE OR DELETE ON {evt}\n"
            f"FOR EACH ROW\n"
            f"EXECUTE FUNCTION fn_multi_event_audit();"
        )
        checks = [
            {"label": "Branches on TG_OP = 'INSERT'", "pattern": ["tg_op", "insert"]},
            {"label": "Branches on TG_OP = 'UPDATE'", "pattern": ["update"]},
            {"label": "Branches on TG_OP = 'DELETE'", "pattern": ["delete"]},
            {"label": f"Logs into {aud_tbl}", "pattern": [aud_tbl]}
        ]

    elif concept_key == "maker_checker":
        starter = (
            f"CREATE OR REPLACE FUNCTION fn_enforce_sod()\n"
            f"RETURNS TRIGGER AS $$\n"
            f"BEGIN\n"
            f"    -- Validate creator != approver:\n"
            f"    \n"
            f"    RETURN NEW;\n"
            f"END;\n"
            f"$$ LANGUAGE plpgsql;"
        )
        solution = (
            f"CREATE OR REPLACE FUNCTION fn_enforce_sod()\n"
            f"RETURNS TRIGGER AS $$\n"
            f"BEGIN\n"
            f"    IF NEW.status = 'APPROVED' THEN\n"
            f"        IF session_user = OLD.created_by OR NEW.approved_by = OLD.created_by THEN\n"
            f"            RAISE EXCEPTION 'Segregation of duties violation: Maker cannot approve their own record';\n"
            f"        END IF;\n"
            f"    END IF;\n"
            f"    RETURN NEW;\n"
            f"END;\n"
            f"$$ LANGUAGE plpgsql;\n\n"
            f"CREATE TRIGGER trg_sod_{evt}\n"
            f"BEFORE UPDATE ON {evt}\n"
            f"FOR EACH ROW\n"
            f"EXECUTE FUNCTION fn_enforce_sod();"
        )
        checks = [
            {"label": "Compares approver with record creator", "pattern": ["session_user", "approved_by", "created_by"]},
            {"label": "Raises exception on match", "pattern": ["raise exception"]},
            {"label": "Returns NEW on valid dual approval", "pattern": ["return new"]}
        ]

    elif concept_key == "security_definer":
        starter = (
            f"CREATE OR REPLACE FUNCTION fn_secure_exec()\n"
            f"RETURNS VOID AS $$\n"
            f"BEGIN\n"
            f"    -- Privileged operations:\n"
            f"END;\n"
            f"$$ LANGUAGE plpgsql\n"
            f"SECURITY DEFINER\n"
            f"SET search_path = ...;"
        )
        solution = (
            f"CREATE OR REPLACE FUNCTION fn_secure_exec()\n"
            f"RETURNS VOID AS $$\n"
            f"BEGIN\n"
            f"    UPDATE {prim} SET ... WHERE ...;\n"
            f"END;\n"
            f"$$ LANGUAGE plpgsql\n"
            f"SECURITY DEFINER\n"
            f"SET search_path = pg_catalog, pg_temp;\n\n"
            f"REVOKE ALL ON FUNCTION fn_secure_exec() FROM PUBLIC;\n"
            f"GRANT EXECUTE ON FUNCTION fn_secure_exec() TO {roles['operator']};"
        )
        checks = [
            {"label": "Specifies SECURITY DEFINER", "pattern": ["security definer"]},
            {"label": "Secures search_path against trojan horses", "pattern": ["search_path", "pg_catalog"]},
            {"label": f"Grants EXECUTE to {roles['operator']}", "pattern": ["grant execute", roles['operator']]}
        ]

    elif concept_key == "when_clause":
        starter = (
            f"CREATE TRIGGER trg_conditional_{evt}\n"
            f"BEFORE UPDATE ON {evt}\n"
            f"FOR EACH ROW\n"
            f"WHEN (...)\n"
            f"EXECUTE FUNCTION fn_audit_change();"
        )
        solution = (
            f"CREATE TRIGGER trg_conditional_{evt}\n"
            f"BEFORE UPDATE ON {evt}\n"
            f"FOR EACH ROW\n"
            f"WHEN (OLD.{metric} IS DISTINCT FROM NEW.{metric})\n"
            f"EXECUTE FUNCTION fn_audit_change();"
        )
        checks = [
            {"label": "Defines WHEN clause on trigger", "pattern": ["when (", "when"]},
            {"label": "Uses IS DISTINCT FROM or comparison on NEW/OLD", "pattern": ["distinct from", "is distinct", "!=", "<>"]},
            {"label": f"Attached to event table {evt}", "pattern": [evt]}
        ]

    elif concept_key == "transition_tables":
        starter = (
            f"CREATE TRIGGER trg_batch_{evt}\n"
            f"AFTER INSERT ON {evt}\n"
            f"REFERENCING NEW TABLE AS ...\n"
            f"FOR EACH STATEMENT\n"
            f"EXECUTE FUNCTION fn_process_batch();"
        )
        solution = (
            f"CREATE TRIGGER trg_batch_{evt}\n"
            f"AFTER INSERT ON {evt}\n"
            f"REFERENCING NEW TABLE AS inserted_batch\n"
            f"FOR EACH STATEMENT\n"
            f"EXECUTE FUNCTION fn_process_batch();"
        )
        checks = [
            {"label": "Uses REFERENCING NEW TABLE AS", "pattern": ["referencing new table as", "referencing"]},
            {"label": "Defines FOR EACH STATEMENT granularity", "pattern": ["for each statement"]},
            {"label": f"Attached to event table {evt}", "pattern": [evt]}
        ]

    elif concept_key == "granularity":
        starter = (
            f"-- 1. FOR EACH ROW vs FOR EACH STATEMENT execution counts on batch insert:\n"
            f"-- 2. Statement-level trigger behavior when 0 rows match WHERE clause:\n"
            f"-- 3. Optimal trigger granularity for batch logging into {aud_tbl}:\n"
        )
        solution = (
            f"-- 1. FOR EACH ROW executes once per mutated tuple (e.g. 5,000 times for 5,000 inserted rows).\n"
            f"--    FOR EACH STATEMENT executes exactly once per statement regardless of row count.\n"
            f"-- 2. A statement-level trigger fires even when zero rows match the WHERE predicate;\n"
            f"--    a row-level trigger executes zero times when no tuples are mutated.\n"
            f"-- 3. FOR EACH STATEMENT is optimal for writing a single consolidated execution summary to {aud_tbl}."
        )
        checks = [
            {"label": "Contrasts FOR EACH ROW and FOR EACH STATEMENT invocation counts", "pattern": ["for each row", "for each statement", "statement", "row"]},
            {"label": "Explains statement trigger fires even on zero qualifying rows", "pattern": ["zero", "0", "fires", "once"]},
            {"label": f"Identifies statement-level granularity for batch logging into {aud_tbl}", "pattern": ["statement", aud_tbl, "batch"]}
        ]

    elif concept_key == "truncate":
        starter = (
            f"-- 1. Reason why row-level triggers do not fire on TRUNCATE {evt}:\n"
            f"-- 2. Statement-level trigger syntax intercepting TRUNCATE:\n"
            f"CREATE TRIGGER trg_truncate_{evt}\n"
            f"-- Timing & Granularity ON {evt}:\n"
            f"-- 3. Performance & lock differences between TRUNCATE and DELETE:\n"
        )
        solution = (
            f"-- 1. TRUNCATE is a DDL-like bulk extent deallocation that does not scan individual rows on the heap,\n"
            f"--    so row-level triggers (which require tuple buffers) never fire.\n"
            f"-- 2. Statement trigger syntax:\n"
            f"CREATE TRIGGER trg_truncate_{evt}\n"
            f"BEFORE TRUNCATE ON {evt}\n"
            f"FOR EACH STATEMENT\n"
            f"EXECUTE FUNCTION fn_log_truncate();\n"
            f"-- 3. TRUNCATE acquires an ACCESS EXCLUSIVE lock but completes in O(1) time without vacuum overhead."
        )
        checks = [
            {"label": "Explains row-level triggers cannot intercept TRUNCATE", "pattern": ["truncate", "row-level", "extent", "deallocat", "scan"]},
            {"label": "Defines statement trigger ON TRUNCATE", "pattern": ["truncate", "for each statement"]},
            {"label": "Contrasts locking or performance vs DELETE", "pattern": ["lock", "delete", "performance", "exclusive", "vacuum"]}
        ]

    elif concept_key == "drop_trigger":
        starter = (
            f"-- 1. Contrast DROP TRIGGER ... RESTRICT vs DROP TRIGGER ... CASCADE on {evt}:\n"
            f"-- 2. Handling of dependent constraints/views:\n"
            f"-- 3. Fate of underlying PL/pgSQL function when trigger is dropped:\n"
        )
        solution = (
            f"-- 1. DROP TRIGGER trg_name ON {evt} RESTRICT halts if dependent objects exist.\n"
            f"--    DROP TRIGGER trg_name ON {evt} CASCADE automatically drops all dependent objects.\n"
            f"-- 2. RESTRICT prevents unintended cascade failures; CASCADE prunes dependencies.\n"
            f"-- 3. Dropping a trigger does NOT drop its underlying trigger function; the function remains intact."
        )
        checks = [
            {"label": "Contrasts CASCADE vs RESTRICT on DROP TRIGGER", "pattern": ["cascade", "restrict", "drop trigger"]},
            {"label": "Explains RESTRICT halts if dependent objects exist", "pattern": ["halt", "abort", "fail", "depend", "restrict"]},
            {"label": "Explains underlying function remains intact", "pattern": ["function", "preserv", "intact", "not drop"]}
        ]

    elif concept_key == "savepoint":
        starter = (
            f"CREATE OR REPLACE FUNCTION fn_audit_with_savepoint()\n"
            f"RETURNS TRIGGER AS $$\n"
            f"BEGIN\n"
            f"    -- Catch audit failure without aborting parent transaction:\n"
            f"    BEGIN\n"
            f"        INSERT INTO {aud_tbl} VALUES (DEFAULT, NEW.id, 'LOG', clock_timestamp());\n"
            f"    EXCEPTION WHEN OTHERS THEN\n"
            f"        -- Graceful handling:\n"
            f"    END;\n"
            f"    RETURN NEW;\n"
            f"END;\n"
            f"$$ LANGUAGE plpgsql;\n"
        )
        solution = (
            f"CREATE OR REPLACE FUNCTION fn_audit_with_savepoint()\n"
            f"RETURNS TRIGGER AS $$\n"
            f"BEGIN\n"
            f"    -- An internal BEGIN ... EXCEPTION block establishes an internal subtransaction savepoint\n"
            f"    BEGIN\n"
            f"        INSERT INTO {aud_tbl} VALUES (DEFAULT, NEW.id, 'LOG', clock_timestamp());\n"
            f"    EXCEPTION WHEN OTHERS THEN\n"
            f"        RAISE WARNING 'Audit logging failed but proceeding: %', SQLERRM;\n"
            f"    END;\n"
            f"    RETURN NEW;\n"
            f"END;\n"
            f"$$ LANGUAGE plpgsql;\n"
        )
        checks = [
            {"label": "Uses BEGIN ... EXCEPTION block for internal savepoint", "pattern": ["begin", "exception"]},
            {"label": f"Attempts write to {aud_tbl}", "pattern": [aud_tbl, "insert into"]},
            {"label": "Returns NEW to allow parent transaction to proceed", "pattern": ["return new", "return"]}
        ]

    else:
        # Generic fallback
        starter = (
            f"-- PL/pgSQL & SQL Execution Buffer for {sec_title}\n"
            f"-- Implement your solution applying {question.get('title')} to {prim} / {evt}:\n\n"
            f"CREATE OR REPLACE FUNCTION fn_process_{prim[:10]}()\n"
            f"RETURNS TRIGGER AS $$\n"
            f"BEGIN\n"
            f"    -- Implement invariant checks:\n\n"
            f"    RETURN NEW;\n"
            f"END;\n"
            f"$$ LANGUAGE plpgsql;\n"
        )
        solution = (
            f"-- Official Model Solution for {sec_title}\n"
            f"-- Key Invariant: {key_invariant}\n\n"
            f"{question.get('solution_key', '')}"
        )
        checks = [
            {"label": f"Interacts with target relations '{prim}' or '{evt}'", "pattern": [prim, evt, "relation", "table", "view", "role", "function"]},
            {"label": "Defines valid SQL / PL/pgSQL procedural statements", "pattern": ["create", "select", "insert", "update", "grant", "revoke", "begin", "function", "trigger", "return", "view"]}
        ]

    return starter, solution, checks


def synthesize_isomorphic_scenario(question: Dict[str, Any], dept: Dict[str, Any], scenario: Dict[str, Any]) -> Dict[str, Any]:
    """
    Synthesizes a concept-faithful isomorphic problem by binding the active question's
    exact relational database invariant into the chosen enterprise domain scenario.
    """
    title = question.get("title", "").strip()
    subtopic = question.get("subtopic", "").strip()
    q_lower = (title + " " + subtopic).lower()

    dept_name = dept["name"]
    sec_title = scenario["title"]
    schema_def = scenario["schema"]
    prim = scenario["primary_table"]
    evt = scenario["event_table"]
    aud = scenario["audit_table"]
    vw = scenario["view_name"]
    metric = scenario["primary_metric"]
    metric_desc = scenario["metric_desc"]
    roles = scenario["roles"]

    # Resolve Concept Key
    if "eca" in q_lower or "formal trigger architecture" in q_lower:
        concept_key = "eca"
    elif "insert" in q_lower and ("transition" in q_lower or "new vs old" in q_lower or "memory buffer" in q_lower):
        concept_key = "insert_transition"
    elif "delete" in q_lower and ("transition" in q_lower or "delete trigger" in q_lower):
        concept_key = "delete_transition"
    elif "grant & revoke" in q_lower or "discretionary access" in q_lower or "basic role" in q_lower:
        concept_key = "grant_revoke"
    elif "before vs after" in q_lower or "timing" in q_lower:
        concept_key = "before_after"
    elif "granularity" in q_lower or "row-level vs statement-level" in q_lower or "zero rows" in q_lower:
        concept_key = "granularity"
    elif "truncate" in q_lower:
        concept_key = "truncate"
    elif "dac" in q_lower or "mac" in q_lower or "mandatory access" in q_lower:
        concept_key = "dac_mac"
    elif "return null" in q_lower or "return new" in q_lower or "return semantics" in q_lower:
        concept_key = "return_null"
    elif "grant option" in q_lower or "delegation" in q_lower or "graph cycles" in q_lower:
        concept_key = "grant_option"
    elif "column-level" in q_lower or "fine-grained" in q_lower:
        concept_key = "column_level"
    elif "dropping triggers" in q_lower or "drop trigger" in q_lower:
        concept_key = "drop_trigger"
    elif "tg_op" in q_lower or "introspection" in q_lower:
        concept_key = "tg_op"
    elif "cascading" in q_lower or "rollback boundar" in q_lower or "acid atomicity" in q_lower:
        concept_key = "cascading"
    elif "reduction guard" in q_lower or "salary reduction" in q_lower or "monotonic" in q_lower:
        concept_key = "value_guard"
    elif "security definer" in q_lower or "privilege elevation" in q_lower:
        concept_key = "security_definer"
    elif "when clause" in q_lower or "conditional trigger" in q_lower:
        concept_key = "when_clause"
    elif "transition tables" in q_lower or "referencing new table" in q_lower:
        concept_key = "transition_tables"
    elif "execution order" in q_lower or "trigger order" in q_lower:
        concept_key = "execution_order"
    elif "set role" in q_lower or "reset role" in q_lower or "session context" in q_lower:
        concept_key = "set_role"
    elif "cross-relation" in q_lower or "referential integrity" in q_lower:
        concept_key = "cross_relation"
    elif "timestamp" in q_lower or "metadata enrichment" in q_lower:
        concept_key = "timestamp"
    elif "maker-checker" in q_lower or "segregation of duties" in q_lower:
        concept_key = "maker_checker"
    elif "mutating table" in q_lower or "recursion" in q_lower or "re-entrancy" in q_lower or "pg_trigger_depth" in q_lower:
        concept_key = "mutating_table"
    elif "state machine" in q_lower or "anti-loan" in q_lower or "dual-key" in q_lower:
        concept_key = "state_machine"
    elif "instead of" in q_lower or "view updatability" in q_lower:
        concept_key = "instead_of"
    elif "tamper-proof" in q_lower or "immutable" in q_lower or "append-only" in q_lower:
        concept_key = "append_only"
    elif "deferred" in q_lower or "deferrable" in q_lower:
        concept_key = "deferred"
    elif "multi-tenant" in q_lower or "tenant boundary" in q_lower or "rls" in q_lower:
        concept_key = "multi_tenant"
    elif "ddl event" in q_lower or "ddl_command" in q_lower:
        concept_key = "ddl_event"
    elif "savepoint" in q_lower or "subtransaction" in q_lower or "exception handling" in q_lower:
        concept_key = "savepoint"
    else:
        concept_key = "generic"

    # 1. ECA Model Primitives & Architecture (EASY-01, EASY-11)
    if "eca" in q_lower or "formal trigger architecture" in q_lower:
        prompt = (
            f"In `{sec_title}` ({dept_name}) with relations `{prim}` and `{evt}`, explain how the "
            f"Event-Condition-Action (ECA) rule model applies to automated `{metric}` governance. "
            f"Formulate the active rule components for `{evt}` and state which primitive acts as the execution gatekeeper."
        )
        hint = f"Identify the triggering DML on '{evt}', the validation check on candidate values in NEW, and the procedural update on '{prim}'."
        key_invariant = "Event initiates the trigger; Condition evaluates the boolean gatekeeper; Action executes procedural side-effects."

    # 2. Transition Variables in INSERT (NEW vs OLD) (EASY-02)
    elif "insert" in q_lower and ("transition" in q_lower or "new vs old" in q_lower or "memory buffer" in q_lower):
        prompt = (
            f"For an INSERT operation on `{evt}` in `{sec_title}`, evaluate the states and accessibility of transition "
            f"variables `NEW` and `OLD` inside a row-level PL/pgSQL trigger. Explain from a storage engine perspective "
            f"why referencing `OLD` is invalid during tuple insertion."
        )
        hint = f"Does a newly proposed tuple for '{evt}' exist on disk prior to insertion? In relational engines, what is the pre-state of a non-existent row?"
        key_invariant = "NEW contains the proposed tuple in memory; OLD is unassigned/NULL because no prior disk tuple exists for an INSERT operation."

    # 3. Transition Variables in DELETE (EASY-13)
    elif "delete" in q_lower and ("transition" in q_lower or "delete trigger" in q_lower):
        prompt = (
            f"When executing a DELETE operation on `{evt}` in `{sec_title}`, evaluate the states of transition variables "
            f"`NEW` and `OLD`. Construct a row-level trigger that leverages the departing tuple buffer to archive records into `{aud}`."
        )
        hint = f"During a DELETE from '{evt}', only the pre-existing state exists. Transition variable NEW has no replacement tuple."
        key_invariant = "OLD references the row being pruned; NEW is undefined/NULL in DELETE triggers."

    # 4. Basic Role Privileges (GRANT & REVOKE) (EASY-03, EASY-08, EASY-15)
    elif "grant & revoke" in q_lower or "discretionary access" in q_lower or "basic role" in q_lower:
        prompt = (
            f"Configure Discretionary Access Control (DAC) for `{sec_title}` in {dept_name}. Establish login role `{roles['officer']}` "
            f"with read permissions on `{prim}` and `{evt}`, grant operational write access on `{evt}` to `{roles['operator']}` without delete rights, "
            f"and revoke all access on `{aud}` from `{roles['operator']}`."
        )
        hint = f"Use standard SQL DCL syntax: `CREATE ROLE ... WITH LOGIN`, `GRANT ... ON {prim} TO ...`, and `REVOKE ... FROM ...`."
        key_invariant = "Enforce least privilege via role separation, granting distinct DML capabilities and denying destructive permissions."

    # 5. BEFORE vs AFTER Timing (EASY-04)
    elif "before vs after" in q_lower or "timing" in q_lower:
        prompt = (
            f"In `{sec_title}` with relations `{prim}` and `{evt}`, contrast `BEFORE` and `AFTER` trigger timings when sanitizing in-flight `NEW` tuples "
            f"versus recording generated keys in `{aud}`. Detail the transactional rollback behavior if an exception arises post-disk allocation."
        )
        hint = f"BEFORE triggers can alter NEW fields in-flight; AFTER triggers execute after disk allocation when serial IDs are finalized."
        key_invariant = "BEFORE triggers sanitize/validate tuples in-flight; AFTER triggers execute downstream audit side-effects; exceptions in either timing roll back the entire transaction."

    # 6. Row-Level vs Statement-Level Granularity (EASY-05, MED-04, HARD-15)
    elif "granularity" in q_lower or "row-level vs statement-level" in q_lower or "zero rows" in q_lower:
        prompt = (
            f"In `{sec_title}`, contrast `FOR EACH ROW` and `FOR EACH STATEMENT` granularity on `{evt}` regarding invocation frequency, zero-row DML behavior, "
            f"and optimal efficiency when recording batch audit entries into `{aud}`."
        )
        hint = f"Statement-level triggers fire exactly once per DML statement regardless of qualifying tuples; row-level triggers fire once per affected tuple."
        key_invariant = "Statement-level triggers fire once per statement (even if 0 rows matched); row-level triggers execute once per mutated tuple."

    # 7. TRUNCATE Operations (EASY-06)
    elif "truncate" in q_lower:
        prompt = (
            f"Explain why row-level `DELETE` triggers fail to intercept a `TRUNCATE {evt}` command in `{sec_title}`, and define a statement-level trigger "
            f"to audit truncations into `{aud}` while evaluating table lock implications."
        )
        hint = f"TRUNCATE deallocates storage extents directly without scanning tuples, completely bypassing row-level triggers."
        key_invariant = "TRUNCATE bypasses row-level triggers; only statement-level triggers defined FOR EACH STATEMENT ON TRUNCATE can intercept it."

    # 8. DAC vs MAC (EASY-07)
    elif "dac" in q_lower or "mac" in q_lower or "mandatory access" in q_lower:
        prompt = (
            f"Compare Discretionary Access Control (DAC) and Mandatory Access Control (MAC) models for `{sec_title}`. Explain how object ownership affects "
            f"privilege delegation to `{roles['operator']}`, and how security labels mitigate Trojan horse data leakage."
        )
        hint = "In DAC, the object owner decides permissions; in MAC, central administrative policies and security labels govern access regardless of ownership."
        key_invariant = "DAC grants discretionary rights to object owners; MAC enforces strict, system-wide clearance rules preventing unauthorized propagation."

    # 9. RETURN NULL vs RETURN NEW in BEFORE INSERT (EASY-09)
    elif "return null" in q_lower or "return new" in q_lower or "return semantics" in q_lower:
        prompt = (
            f"In `{sec_title}`, analyze the operational divergence between `RETURN NEW` and `RETURN NULL` inside a BEFORE INSERT trigger on `{evt}`. "
            f"Explain when silent tuple suppression is preferable to raising an exception."
        )
        hint = f"In a BEFORE row trigger, RETURN NEW proceeds with heap storage; RETURN NULL silently discards the tuple without aborting the transaction."
        key_invariant = "RETURN NULL silently suppresses row insertion without raising an error; RETURN NEW approves the tuple for storage."

    # 10. WITH GRANT OPTION Fundamentals (EASY-10, MED-07, HARD-14)
    elif "grant option" in q_lower or "delegation" in q_lower or "graph cycles" in q_lower:
        prompt = (
            f"In `{sec_title}`, illustrate privilege delegation using `WITH GRANT OPTION` from `{roles['admin']}` to `{roles['officer']}` on `{prim}`. "
            f"Analyze the cascade revocation dynamics if delegated permissions to `{roles['operator']}` are pruned."
        )
        hint = f"Use `WITH GRANT OPTION`. Under CASCADE, downstream grants delegated by that user are revoked; under RESTRICT, the revoke fails if dependencies exist."
        key_invariant = "WITH GRANT OPTION authorizes role delegation; CASCADE prunes downstream authorization branches."

    # 11. Column-Level Privileges & Views (EASY-12, MED-05)
    elif "column-level" in q_lower or "fine-grained" in q_lower:
        prompt = (
            f"In `{sec_title}`, design column-restricted access to relation `{prim}` for `{roles['operator']}` that shields sensitive attribute `{metric}`. "
            f"Construct security view `{vw}` and evaluate the architectural advantages of view encapsulation over raw column grants."
        )
        hint = f"Syntax: `GRANT SELECT (col1, col2) ON {prim} TO {roles['operator']};` Views provide an alternate security boundary with clean query planning."
        key_invariant = "Column-level permissions restrict specific attributes; views abstract projections with granular privilege management."

    # 12. Dropping Triggers CASCADE vs RESTRICT (EASY-14)
    elif "dropping triggers" in q_lower or "drop trigger" in q_lower:
        prompt = (
            f"In `{sec_title}`, contrast `DROP TRIGGER ... RESTRICT` with `CASCADE` on relation `{evt}` when dependent constraints exist, "
            f"and explain the lifecycle fate of the underlying PL/pgSQL function."
        )
        hint = "In PostgreSQL, dropping a trigger does NOT drop the underlying function. RESTRICT fails if dependencies exist; CASCADE removes dependent items."
        key_invariant = "RESTRICT halts if dependent objects exist; CASCADE drops dependent objects; dropping a trigger preserves the underlying function."

    # 13. TG_OP Introspection Variable (EASY-16)
    elif "tg_op" in q_lower or "introspection" in q_lower:
        prompt = (
            f"Develop a unified multi-event audit trigger on `{evt}` for `{sec_title}`. Utilize `TG_OP` introspection to dispatch "
            f"INSERT, UPDATE, and DELETE telemetry into `{aud}` using transition variables appropriately."
        )
        hint = f"Branch using: `IF (TG_OP = 'INSERT') THEN ... ELSIF (TG_OP = 'UPDATE') THEN ... ELSIF (TG_OP = 'DELETE') THEN ...`"
        key_invariant = "TG_OP introspects the triggering DML event at runtime, enabling unified multi-event auditing in a single trigger."

    # 14. Cascading Triggers and Rollback Boundaries (MED-01)
    elif "cascading" in q_lower or "rollback boundar" in q_lower or "acid atomicity" in q_lower:
        prompt = (
            f"In `{sec_title}`, an insertion into `{evt}` cascades updates to `{prim}` and secondary logs in `{aud}`. "
            f"Examine the ACID transaction atomicity and rollback boundary if the secondary trigger fails."
        )
        hint = f"All cascading triggers execute within the exact same transaction boundary. An exception anywhere aborts and rolls back all modifications."
        key_invariant = "Cascading triggers share the same transaction boundary; an unhandled exception at any tier rolls back all preceding and nested writes."

    # 15. Value Reduction Guard / Monotonic Guard (MED-02)
    elif "reduction guard" in q_lower or "salary reduction" in q_lower or "monotonic" in q_lower:
        prompt = (
            f"Implement a PL/pgSQL BEFORE UPDATE trigger on `{prim}` for `{sec_title}` enforcing monotonic integrity on `{metric}` ({metric_desc}). "
            f"Reject unauthorized decreases by raising an exception, otherwise allowing valid updates."
        )
        hint = f"In a BEFORE UPDATE trigger: compare NEW.{metric} with OLD.{metric}. Return NEW if valid; raise an exception if decreased."
        key_invariant = "BEFORE UPDATE triggers inspect proposed mutations (NEW vs OLD) to guard against unauthorized state decreases."

    # 16. SECURITY DEFINER vs SECURITY INVOKER (MED-03, HARD-09)
    elif "security definer" in q_lower or "privilege elevation" in q_lower:
        prompt = (
            f"Configure a `SECURITY DEFINER` routine on `{prim}` enabling `{roles['operator']}` to perform authorized updates in `{sec_title}`. "
            f"Detail search_path hardening necessary to prevent privilege escalation."
        )
        hint = "SECURITY DEFINER runs with the permissions of the function creator. Securing search_path prevents malicious schema hijacking."
        key_invariant = "SECURITY DEFINER executes with owner privileges; search_path must be locked down to prevent privilege escalation."

    # 17. Conditional WHEN Clause (MED-06)
    elif "when clause" in q_lower or "conditional trigger" in q_lower:
        prompt = (
            f"Formulate a high-throughput update trigger on `{evt}` in `{sec_title}` using an engine-level `WHEN` clause that only fires "
            f"when `{metric}` changes, explaining why this outperforms PL/pgSQL function-level checks."
        )
        hint = f"The SQL WHEN clause evaluates inside the engine core before invoking the procedural runtime, eliminating context-switch overhead."
        key_invariant = "Engine-level WHEN clause filters trigger execution before procedural context switching."

    # 18. Transition Tables (REFERENCING NEW TABLE AS) (MED-08)
    elif "transition tables" in q_lower or "referencing new table" in q_lower:
        prompt = (
            f"Construct a statement-level trigger on `{evt}` in `{sec_title}` utilizing transition tables (`REFERENCING NEW TABLE`) "
            f"to perform set-based validation across batch inserts."
        )
        hint = f"PostgreSQL transition tables allow SQL queries like `SELECT SUM(amount) FROM inserted_batch` inside statement-level triggers."
        key_invariant = "Transition tables give statement-level triggers set-based access to the complete delta batch."

    # 19. Trigger Execution Order (MED-09)
    elif "execution order" in q_lower or "trigger order" in q_lower:
        prompt = (
            f"In `{sec_title}`, analyze the execution sequence when multiple BEFORE triggers exist on `{evt}`. Explain how PostgreSQL determines "
            f"order and how mutations in earlier triggers affect subsequent triggers."
        )
        hint = "In PostgreSQL, triggers on the same event and timing execute in alphabetical order by trigger name."
        key_invariant = "Triggers execute in alphabetical order by name; mutations made to NEW by earlier triggers are visible to subsequent triggers."

    # 20. Dynamic Role Switching (SET ROLE & RESET ROLE) (MED-10)
    elif "set role" in q_lower or "reset role" in q_lower or "session context" in q_lower:
        prompt = (
            f"In `{sec_title}`, demonstrate how `{roles['admin']}` temporarily assumes `{roles['officer']}` using `SET ROLE` and reverts via `RESET ROLE`. "
            f"Contrast `current_user` and `session_user` resolution during this session."
        )
        hint = "SET ROLE alters current_user for permission checks; session_user remains the authenticated identity; RESET ROLE restores the session."
        key_invariant = "SET ROLE changes current_user for authorization; session_user retains authenticated identity; RESET ROLE restores baseline."

    # 21. Cross-Relation Referential Integrity (MED-11)
    elif "cross-relation" in q_lower or "referential integrity" in q_lower:
        prompt = (
            f"Design a BEFORE INSERT trigger on `{evt}` in `{sec_title}` to maintain aggregate synchrony with `{prim}.{metric}`. "
            f"Validate capacity atomically and abort over-allocation within the transaction boundary."
        )
        hint = f"Use a BEFORE INSERT trigger on '{evt}' that checks and updates parent '{prim}' atomically within the transaction."
        key_invariant = "Triggers enforce cross-table aggregate invariants and relational consistency that foreign keys alone cannot express."

    # 22. Automatic Timestamp Auditing (MED-13)
    elif "timestamp" in q_lower or "metadata enrichment" in q_lower:
        prompt = (
            f"Implement a BEFORE UPDATE metadata trigger on `{prim}` in `{sec_title}` recording timestamp and session identity. "
            f"Explain why `clock_timestamp()` is preferred over `CURRENT_TIMESTAMP` for precise physical execution timing."
        )
        hint = "NOW() returns transaction start time; clock_timestamp() reflects actual physical wall-clock execution time."
        key_invariant = "BEFORE UPDATE triggers automate metadata enrichment; clock_timestamp() records real-time execution moments."

    # 23. Maker-Checker Segregation of Duties (MED-15)
    elif "maker-checker" in q_lower or "segregation of duties" in q_lower:
        prompt = (
            f"Enforce Maker-Checker dual control on `{evt}` in `{sec_title}` via a BEFORE UPDATE trigger. Prevent self-approval "
            f"by ensuring the approving user differs from the record creator."
        )
        hint = f"Compare creator identity with approving officer identity. Raise an exception if they match."
        key_invariant = "Procedural triggers enforce dual-control authorization and Segregation of Duties (SoD) at the database layer."

    # 24. Mutating Table & Infinite Recursion Guard (HARD-01, HARD-07)
    elif "mutating table" in q_lower or "recursion" in q_lower or "re-entrancy" in q_lower or "pg_trigger_depth" in q_lower:
        prompt = (
            f"In `{sec_title}`, protect `{prim}` against self-triggering recursion loops during cascade updates. "
            f"Implement an execution depth guard using `pg_trigger_depth()` to break circular invocation."
        )
        hint = "`pg_trigger_depth()` inspects current nesting level. Returning early when depth > 1 terminates recursive cascade loops."
        key_invariant = "pg_trigger_depth() halts infinite trigger recursion and re-entrant cascade loops."

    # 25. Linear State Machine Enforcement (HARD-02, HARD-16)
    elif "state machine" in q_lower or "anti-loan" in q_lower or "dual-key" in q_lower:
        prompt = (
            f"Implement a state machine validation trigger on `{evt}` in `{sec_title}` governing status transitions (`DRAFT` -> `SUBMITTED` -> `UNDER_REVIEW` -> `APPROVED` -> `SETTLED`). "
            f"Block invalid jumps and modifications to finalized records."
        )
        hint = "Use conditional checks or a lookup table validating allowable (OLD.status, NEW.status) pairs. Abort on invalid jumps."
        key_invariant = "Relational triggers act as strict state machine verifiers, preventing illegal lifecycle bypasses."

    # 26. INSTEAD OF Triggers on Views (HARD-04, HARD-08)
    elif "instead of" in q_lower or "view updatability" in q_lower:
        prompt = (
            f"Create an `INSTEAD OF INSERT` trigger on joined view `{vw}` in `{sec_title}` that decomposes submitted tuples and routes "
            f"atomic writes to underlying base tables `{prim}` and `{evt}`."
        )
        hint = f"INSTEAD OF triggers intercept DML on complex views and route underlying mutations to base relations '{prim}' and '{evt}'."
        key_invariant = "INSTEAD OF triggers provide write abstraction over complex non-updatable joined or aggregated views."

    # 27. Immutable Append-Only Ledger (HARD-05)
    elif "tamper-proof" in q_lower or "immutable" in q_lower or "append-only" in q_lower:
        prompt = (
            f"Enforce strict append-only immutability on `{aud}` in `{sec_title}` via a PL/pgSQL trigger that unconditionally blocks "
            f"all `UPDATE` and `DELETE` statements at the database level."
        )
        hint = f"In the trigger function on '{aud}': `RAISE EXCEPTION 'Immutable ledger: UPDATE and DELETE operations are forbidden on this relation';`"
        key_invariant = "Append-only triggers enforce absolute immutability by intercepting and rejecting all UPDATE/DELETE attempts."

    # 28. Deferred Constraint Triggers (HARD-06)
    elif "deferred" in q_lower or "deferrable" in q_lower:
        prompt = (
            f"In `{sec_title}`, explain the mechanics of `CONSTRAINT TRIGGER ... DEFERRABLE INITIALLY DEFERRED` across relations `{prim}` and `{evt}`, "
            f"contrasting statement-level evaluation with commit-time integrity verification."
        )
        hint = "Deferred constraint triggers evaluate at transaction COMMIT time rather than immediately after each statement."
        key_invariant = "DEFERRABLE INITIALLY DEFERRED evaluates integrity invariants at COMMIT time rather than statement time."

    # 29. Pre-RLS Multi-Tenant Isolation (HARD-10, HARD-13)
    elif "multi-tenant" in q_lower or "tenant boundary" in q_lower or "rls" in q_lower:
        prompt = (
            f"Design a BEFORE INSERT tenant-isolation trigger on `{prim}` and `{evt}` in `{sec_title}` that extracts session tenant "
            f"context and blocks cross-tenant spoofing."
        )
        hint = "Use `current_setting('app.current_tenant_id', true)` to stamp the verified tenant into NEW.tenant_id."
        key_invariant = "Triggers enforce multi-tenant isolation by overriding and validating tenant identity attributes from session variables."

    # 30. DDL Event Triggers (HARD-11)
    elif "ddl event" in q_lower or "ddl_command" in q_lower:
        prompt = (
            f"Develop a PostgreSQL Event Trigger in `{sec_title}` to intercept DDL commands (`DROP TABLE`, `ALTER TABLE`) targeting mission-critical "
            f"relations `{prim}` and `{aud}`, contrasting DDL event triggers with table DML triggers."
        )
        hint = "Event Triggers capture DDL lifecycle events across the entire database rather than table DML events."
        key_invariant = "DDL Event Triggers monitor and abort schema alterations at the database level."

    # 31. ACID Savepoints and Exception Handling (HARD-12)
    elif "savepoint" in q_lower or "subtransaction" in q_lower or "exception handling" in q_lower:
        prompt = (
            f"In `{sec_title}`, formulate a trigger on `{evt}` with a `BEGIN ... EXCEPTION` subtransaction block to record audit data to `{aud}` "
            f"without aborting the primary transaction if logging encounters an error."
        )
        hint = "A `BEGIN ... EXCEPTION` block in PL/pgSQL creates an internal savepoint that catches runtime errors without terminating the outer transaction."
        key_invariant = "PL/pgSQL exception blocks establish internal subtransactions/savepoints for graceful error recovery."

    # Fallback: Dynamic Synthesis tailored to Question
    else:
        orig_prompt = question.get("prompt", "")
        prompt = (
            f"In `{sec_title}` ({dept_name}) with relations `{prim}` and `{evt}`, apply the principles of "
            f"{subtopic} ({title}) to enforce `{metric_desc}` while auditing state in `{aud}`.\n\n"
            f"{orig_prompt}"
        )
        hints_list = question.get("hints", [])
        hint = hints_list[0] if hints_list else f"Review how {title} applies to {prim} and {evt}."
        key_invariant = f"Apply {title} ({subtopic}) in the context of {dept_name}."

    starter_code, model_solution, rubric_checks = _build_solution_and_rubric(
        concept_key, sec_title, prim, evt, aud, vw, metric, metric_desc, roles, key_invariant, question
    )

    return {
        "title": f"Isomorphic Practice: {sec_title}",
        "domain": dept_name,
        "dept_id": dept["id"],
        "scenario_title": sec_title,
        "schema": schema_def,
        "primary_table": prim,
        "event_table": evt,
        "audit_table": aud,
        "view_name": vw,
        "prompt": prompt,
        "hint": hint,
        "key_invariant": key_invariant,
        "concept_key": concept_key,
        "starter_code": starter_code,
        "model_solution": model_solution,
        "rubric_checks": rubric_checks
    }


def generate_isomorphic_problem(
    question: Dict[str, Any],
    dept_idx: Optional[int] = None,
    var_idx: Optional[int] = None,
    advance_variation: bool = False
) -> Dict[str, Any]:
    """
    Generates a fresh, concept-faithful isomorphic practice problem.
    Offline mode: Procedurally binds the question's relational concept into 5 enterprise departments
    with 4 distinct scenario variations per department (20 schemas total).
    Online mode: Injects the active scenario schema into Gemini 3.8 Flash for AI synthesis.
    """
    global _question_variation_counters, _question_department_indices

    q_id = str(question.get("id", "q"))

    # Resolve Department Index
    if dept_idx is not None:
        d_idx = dept_idx % len(_DEPARTMENTS)
        _question_department_indices[q_id] = d_idx
    else:
        d_idx = _question_department_indices.get(q_id, 0)

    dept = _DEPARTMENTS[d_idx]
    variations = dept["variations"]

    # Resolve Variation Index
    var_key = f"{q_id}_{d_idx}"
    if advance_variation:
        current_v = _question_variation_counters.get(var_key, 0)
        v_idx = (current_v + 1) % len(variations)
        _question_variation_counters[var_key] = v_idx
    elif var_idx is not None:
        v_idx = var_idx % len(variations)
        _question_variation_counters[var_key] = v_idx
    else:
        v_idx = _question_variation_counters.get(var_key, 0) % len(variations)

    scenario = variations[v_idx]

    # Offline synthesis first
    offline_res = synthesize_isomorphic_scenario(question, dept, scenario)
    offline_res["dept_idx"] = d_idx
    offline_res["var_idx"] = v_idx
    offline_res["total_variations"] = len(variations)

    # Check for Online Gemini synthesis
    client = get_gemini_client()
    if client:
        online_prompt = f"""
You are an expert DBMS professor creating an isomorphic exam problem.
The student is studying: {question.get('title')} ({question.get('subtopic')}).
Original Concept Invariant: {offline_res['key_invariant']}

DOMAIN: {dept['name']}
SCENARIO: {scenario['title']}
RELATION SCHEMAS:
{scenario['schema']}

TASK:
Create a rigorous exam practice problem that tests the EXACT SAME database invariant ({offline_res['key_invariant']}),
using the tables, columns, and business rules of this scenario.

Return clean markdown with:
1. Scenario Context & Table Schema
2. A concise, challenging exam problem statement (2-3 sentences, do NOT spoon-feed or list out step-by-step tasks)
3. A Socratic Hint (1 sentence)
"""
        try:
            from google.genai import types
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=online_prompt,
                config=types.GenerateContentConfig(
                    system_instruction="You are a DBMS question generator for GATE and university competitive exams.",
                    temperature=0.6
                )
            )
            offline_res["ai_generated_content"] = response.text.strip()
        except Exception:
            pass

    return offline_res


def evaluate_isomorphic_submission(student_code: str, iso_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Evaluates a student's submission for an isomorphic variant against its target
    relational schema, transition variables, and key invariants.
    """
    clean_code = student_code.strip()
    rubric = iso_data.get("rubric_checks", [])

    if not clean_code or len(clean_code) < 15:
        return {
            "score": 0,
            "grade_band": "No Submission",
            "passed_checks": [],
            "missing_checks": [c["label"] for c in rubric],
            "feedback": "Please write your SQL or PL/pgSQL solution in the buffer before submitting for evaluation."
        }

    passed = []
    missing = []
    code_lower = clean_code.lower()

    for item in rubric:
        pattern = item.get("pattern", "")
        label = item.get("label", "")
        if isinstance(pattern, list):
            match = any(p.lower() in code_lower for p in pattern)
        elif isinstance(pattern, str) and pattern.startswith("regex:"):
            import re
            match = bool(re.search(pattern[6:], clean_code, re.IGNORECASE))
        else:
            match = str(pattern).lower() in code_lower

        if match:
            passed.append(label)
        else:
            missing.append(label)

    total = len(rubric) if rubric else 1
    score = int((len(passed) / total) * 100)

    if score >= 85:
        grade_band = "Mastery (Production Grade)"
        feedback = "Exceptional submission! All target relational engine invariants and schema entities are correctly implemented."
    elif score >= 60:
        grade_band = "Proficient (Minor Gaps)"
        feedback = f"Good solution! {len(passed)} of {total} invariants satisfied. Review the missing checks below to tighten your constraints."
    elif score >= 35:
        grade_band = "Developing"
        feedback = f"Partial match ({score}%). Several key invariants or schema entities were not detected."
    else:
        grade_band = "Needs Revision"
        feedback = "The submission does not yet address the core relational invariants for this scenario. Review the hint and schema."

    return {
        "score": score,
        "grade_band": grade_band,
        "passed_checks": passed,
        "missing_checks": missing,
        "feedback": feedback
    }

