import os
import json
import streamlit as st
from ai_engine.evaluator import evaluate_submission
from ai_engine.tutor import diagnose_student_submission, generate_socratic_hint, generate_isomorphic_problem, evaluate_isomorphic_submission

@st.cache_data
def load_exam_questions():
    """
    Loads and caches the curated benchmark practice questions.
    Prioritizes data/exam_questions.json if present, otherwise uses built-in questions_data.
    """
    dataset_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "exam_questions.json")
    if os.path.exists(dataset_path):
        try:
            with open(dataset_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    try:
        from ai_engine.questions_data import BENCHMARK_QUESTIONS
        return BENCHMARK_QUESTIONS
    except Exception:
        return []


def render_exam_lab_tab(active_role="retail_customer"):
    """
    Renders Tab 5: AI-Powered Practice Lab & Exam Evaluator.
    Evaluates student trigger & RBAC solutions using:
      1. Dense vector cosine similarity (Sentence-Transformers)
      2. Generative Socratic error diagnosis (Gemini 3.8 Flash via google-genai)
    """
    questions = load_exam_questions()
    if not questions:
        st.error("Question bank could not be loaded. Please ensure data/exam_questions.json exists.")
        return

    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.95) 100%); border: 1px solid rgba(168, 85, 247, 0.3); border-radius: 8px; padding: 10px 16px; margin-bottom: 12px; box-shadow: 0 4px 14px rgba(0,0,0,0.25);">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
            <div>
                <div style="font-size: 15px; font-weight: 800; color: #f8fafc; letter-spacing: -0.3px;">AI Practice Lab & Exam Evaluator</div>
                <div style="font-size: 11.5px; color: #94a3b8; margin-top: 1px;">Curated GATE CS, ISRO & Premier University benchmark challenges on PostgreSQL Triggers and RBAC</div>
            </div>
            <div style="display: flex; gap: 6px; flex-wrap: wrap;">
                <span style="background: rgba(56, 189, 248, 0.12); border: 1px solid #0284c7; color: #38bdf8; padding: 2px 8px; border-radius: 4px; font-size: 10px; font-weight: 700;">models/dbms-trigger-evaluator</span>
                <span style="background: rgba(16, 185, 129, 0.12); border: 1px solid #10b981; color: #10b981; padding: 2px 8px; border-radius: 4px; font-size: 10px; font-weight: 700;">384-DIM DENSE EMBEDDINGS</span>
                <span style="background: rgba(168, 85, 247, 0.12); border: 1px solid #9333ea; color: #c084fc; padding: 2px 8px; border-radius: 4px; font-size: 10px; font-weight: 700;">~14ms CPU LATENCY</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # -------------------------------------------------------------------------
    # 1. Difficulty Level Selector & Counter
    # -------------------------------------------------------------------------
    diff_col1, diff_col2 = st.columns([2.5, 1.5])
    with diff_col1:
        selected_diff = st.radio(
            "Practice Difficulty Level:",
            options=["Easy", "Medium", "Hard"],
            index=0,
            horizontal=True,
            key="exam_diff_level"
        )

    tier_questions = [q for q in questions if q.get("difficulty") == selected_diff]
    if not tier_questions:
        tier_questions = questions

    cursor_key = f"exam_cursor_{selected_diff}"
    if cursor_key not in st.session_state:
        st.session_state[cursor_key] = 0

    cur_idx = st.session_state[cursor_key] % len(tier_questions)
    current_q = tier_questions[cur_idx]
    q_id = current_q["id"]

    with diff_col2:
        st.markdown(f"""
        <div style="display: flex; justify-content: flex-end; align-items: center; height: 100%; padding-top: 18px;">
            <span style="background: #1e293b; border: 1px solid #334155; color: #94a3b8; padding: 4px 10px; border-radius: 6px; font-size: 11px; font-weight: 700;">
                Question {cur_idx + 1} of {len(tier_questions)}
            </span>
        </div>
        """, unsafe_allow_html=True)

    # -------------------------------------------------------------------------
    # 2. Problem Statement Card
    # -------------------------------------------------------------------------
    diff = current_q.get("difficulty", "Medium")
    if diff == "Easy":
        diff_badge = "<span style='background: rgba(16, 185, 129, 0.15); border: 1px solid #10b981; color: #10b981; padding: 2px 10px; border-radius: 9999px; font-size: 11px; font-weight: 700;'>EASY</span>"
    elif diff == "Medium":
        diff_badge = "<span style='background: rgba(56, 189, 248, 0.15); border: 1px solid #0284c7; color: #38bdf8; padding: 2px 10px; border-radius: 9999px; font-size: 11px; font-weight: 700;'>MEDIUM</span>"
    else:
        diff_badge = "<span style='background: rgba(192, 132, 252, 0.15); border: 1px solid #9333ea; color: #c084fc; padding: 2px 10px; border-radius: 9999px; font-size: 11px; font-weight: 700;'>HARD</span>"

    st.markdown(f"""
    <div style="background: #111827; border: 1px solid #1f2937; border-left: 4px solid #38bdf8; border-radius: 8px; padding: 16px 20px; margin-bottom: 18px;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
            <div>
                <span style="font-size: 11px; font-weight: 700; color: #38bdf8; text-transform: uppercase; letter-spacing: 1px;">
                    {current_q.get('topic')} &bull; {current_q.get('subtopic')}
                </span>
                <h3 style="margin: 4px 0 0 0; color: #f8fafc; font-size: 18px; font-weight: 700;">
                    {current_q.get('title')}
                </h3>
            </div>
            <div style="margin-top: 4px;">
                {diff_badge} &nbsp;
                <span style="background: #1e293b; border: 1px solid #334155; color: #94a3b8; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 600;">
                    Source: {current_q.get('source')}
                </span>
            </div>
        </div>
        <div style="color: #e2e8f0; font-size: 13.5px; line-height: 1.6; margin-top: 12px; background: rgba(15, 23, 42, 0.6); padding: 12px 16px; border-radius: 6px; border: 1px solid #1e293b;">
            {current_q.get('prompt')}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # -------------------------------------------------------------------------
    # 3. Student Code & Solution Workbench
    # -------------------------------------------------------------------------
    ans_key = f"student_ans_{q_id}"
    default_code = current_q.get("starter_code", "-- Enter your solution here")
    if ans_key not in st.session_state:
        st.session_state[ans_key] = default_code

    student_code = st.text_area(
        "Your PL/pgSQL Code or Conceptual Solution:",
        value=st.session_state[ans_key],
        height=190,
        key=f"text_area_{q_id}"
    )
    st.session_state[ans_key] = student_code

    # Action buttons
    btn_col1, btn_col2, btn_col3, btn_col4 = st.columns([2, 1.5, 1.5, 2])
    with btn_col1:
        submit_eval = st.button("Submit for AI Evaluation", type="primary", use_container_width=True, key=f"eval_btn_{q_id}")
    with btn_col2:
        req_hint1 = st.button("Request Hint (Level 1)", use_container_width=True, key=f"hint1_btn_{q_id}")
    with btn_col3:
        req_hint2 = st.button("Request Hint (Level 2)", use_container_width=True, key=f"hint2_btn_{q_id}")
    with btn_col4:
        gen_iso = st.button("Generate Practice Variant", use_container_width=True, key=f"iso_btn_{q_id}")

    # Handle evaluation submission
    eval_state_key = f"eval_result_{q_id}"
    if submit_eval:
        with st.spinner("Analyzing semantic embeddings and DBMS relational invariants..."):
            eval_res = evaluate_submission(student_code, current_q)
            st.session_state[eval_state_key] = eval_res
            # Also fetch Socratic diagnosis
            diagnosis = diagnose_student_submission(current_q, student_code, eval_res)
            st.session_state[f"diagnosis_{q_id}"] = diagnosis

    # Handle Socratic hints
    hint_state_key = f"hint_{q_id}"
    if req_hint1:
        with st.spinner("Synthesizing Level 1 Socratic hint..."):
            h1 = generate_socratic_hint(current_q, student_code, hint_level=1)
            st.session_state[hint_state_key] = ("Level 1 Hint", h1)
    elif req_hint2:
        with st.spinner("Synthesizing Level 2 Socratic hint..."):
            h2 = generate_socratic_hint(current_q, student_code, hint_level=2)
            st.session_state[hint_state_key] = ("Level 2 Hint", h2)

    # Handle Isomorphic Question Generation
    iso_state_key = f"iso_problem_{q_id}"
    if gen_iso:
        with st.spinner("Synthesizing isomorphic problem variant..."):
            iso_res = generate_isomorphic_problem(current_q)
            st.session_state[iso_state_key] = iso_res

    # Display active Hint if requested
    if hint_state_key in st.session_state:
        htitle, htext = st.session_state[hint_state_key]
        st.markdown(f"""
        <div style="background: rgba(245, 158, 11, 0.08); border-left: 3px solid #f59e0b; border-radius: 6px; padding: 12px 16px; margin: 12px 0;">
            <div style="font-size: 11px; font-weight: 700; color: #f59e0b; text-transform: uppercase;">{htitle}</div>
            <div style="color: #cbd5e1; font-size: 13px; margin-top: 4px; line-height: 1.5;">{htext}</div>
        </div>
        """, unsafe_allow_html=True)

    # Display active Isomorphic Question if requested
    if iso_state_key in st.session_state:
        iso_data = st.session_state[iso_state_key]
        dept_options = [
            "FinTech & Digital Banking",
            "Commercial Aviation & Flight Operations",
            "Healthcare & Hospital Administration",
            "Cloud Infrastructure & Cybersecurity",
            "Global Logistics & Supply Chain"
        ]
        current_dept_idx = iso_data.get("dept_idx", 0)
        current_var_idx = iso_data.get("var_idx", 0)
        total_vars = iso_data.get("total_variations", 4)

        st.markdown(f"""
        <div style="background: rgba(192, 132, 252, 0.08); border-left: 3px solid #c084fc; border-radius: 6px; padding: 12px 16px; margin: 12px 0 8px 0;">
            <div style="font-size: 11px; font-weight: 700; color: #c084fc; text-transform: uppercase;">
                🔄 Isomorphic Practice Problem (Adapting '{current_q.get('title')}')
            </div>
            <div style="color: #cbd5e1; font-size: 12px; margin-top: 4px;">
                Department: <b style="color: #f8fafc;">{iso_data.get('domain')}</b> &bull; Scenario: <b style="color: #f8fafc;">{iso_data.get('scenario_title')}</b> (Variation {current_var_idx + 1} of {total_vars})
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Department switcher and Variation cycler controls
        iso_nav_col1, iso_nav_col2 = st.columns([3, 2])
        with iso_nav_col1:
            sel_dept = st.selectbox(
                "Select Department Domain:",
                dept_options,
                index=current_dept_idx,
                key=f"iso_dept_sel_{q_id}",
                label_visibility="collapsed"
            )
        with iso_nav_col2:
            cycle_var = st.button("🔄 Next Variation", key=f"iso_next_var_{q_id}", use_container_width=True)

        if sel_dept != dept_options[current_dept_idx]:
            new_dept_idx = dept_options.index(sel_dept)
            st.session_state[iso_state_key] = generate_isomorphic_problem(current_q, dept_idx=new_dept_idx, var_idx=0)
            st.rerun()

        if cycle_var:
            st.session_state[iso_state_key] = generate_isomorphic_problem(current_q, dept_idx=current_dept_idx, advance_variation=True)
            st.rerun()

        if iso_data.get("ai_generated_content"):
            st.markdown(f"""
            <div style="background: #0f172a; border: 1px solid #1e293b; border-radius: 6px; padding: 14px 18px; margin-bottom: 12px; color: #e2e8f0; font-size: 13px; line-height: 1.5;">
{iso_data['ai_generated_content']}
            </div>
            """, unsafe_allow_html=True)
        else:
            schema_txt = iso_data.get("schema", "")
            prompt_txt = iso_data.get("prompt", "")
            invariant_txt = iso_data.get("key_invariant", "")
            hint_txt = iso_data.get("hint", "")

            st.markdown(f"""
**Relation Schema:**
```sql
{schema_txt}
```

**Task Description:**
{prompt_txt}

**Key Relational Invariant Tested:**
`{invariant_txt}`

**Socratic Hint:**
*{hint_txt}*
""")

        # Dedicated Interactive Workspace for Isomorphic Variant (Option A)
        st.markdown("""
        <div style="font-size: 11px; font-weight: 700; color: #c084fc; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 14px; margin-bottom: 4px;">
            Variant PL/pgSQL & SQL Execution Buffer
        </div>
        """, unsafe_allow_html=True)

        v_buf_key = f"iso_buf_{q_id}_{current_dept_idx}_{current_var_idx}"
        v_eval_key = f"iso_eval_{q_id}_{current_dept_idx}_{current_var_idx}"

        if v_buf_key not in st.session_state:
            st.session_state[v_buf_key] = iso_data.get("starter_code", "")

        v_code = st.text_area(
            label="Variant submission code buffer:",
            value=st.session_state[v_buf_key],
            height=160,
            key=f"iso_text_area_{q_id}_{current_dept_idx}_{current_var_idx}",
            label_visibility="collapsed",
            help="Implement your PL/pgSQL function or SQL commands for this specific variant."
        )

        v_btn_col1, v_btn_col2 = st.columns([2.5, 1.5])
        with v_btn_col1:
            eval_variant_clicked = st.button(
                "Evaluate Variant Submission",
                type="primary",
                use_container_width=True,
                key=f"eval_v_btn_{q_id}_{current_dept_idx}_{current_var_idx}"
            )
        with v_btn_col2:
            reset_variant_clicked = st.button(
                "Reset Starter Code",
                use_container_width=True,
                key=f"reset_v_btn_{q_id}_{current_dept_idx}_{current_var_idx}"
            )

        if eval_variant_clicked:
            st.session_state[v_buf_key] = v_code
            v_res = evaluate_isomorphic_submission(v_code, iso_data)
            st.session_state[v_eval_key] = v_res
            st.rerun()

        if reset_variant_clicked:
            st.session_state[v_buf_key] = iso_data.get("starter_code", "")
            st.session_state.pop(v_eval_key, None)
            st.rerun()

        # Display Variant Evaluation Results
        if v_eval_key in st.session_state:
            v_res = st.session_state[v_eval_key]
            v_score = v_res.get("score", 0)
            v_band = v_res.get("grade_band", "Evaluated")
            v_feedback = v_res.get("feedback", "")
            v_passed = v_res.get("passed_checks", [])
            v_missing = v_res.get("missing_checks", [])

            badge_color = "#10b981" if v_score >= 80 else ("#f59e0b" if v_score >= 50 else "#ef4444")

            passed_html = "".join([f"<li style='color: #86efac; margin: 2px 0;'>✓ {c}</li>" for c in v_passed]) if v_passed else "<li style='color: #94a3b8;'>No target invariants matched yet.</li>"
            missing_html = "".join([f"<li style='color: #fca5a5; margin: 2px 0;'>✕ {c}</li>" for c in v_missing]) if v_missing else "<li style='color: #86efac;'>All key invariants verified!</li>"

            st.markdown(f"""
            <div style="background: #111827; border: 1px solid #1f2937; border-left: 4px solid {badge_color}; border-radius: 6px; padding: 12px 16px; margin: 10px 0;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <span style="font-size: 11px; font-weight: 700; color: {badge_color}; text-transform: uppercase;">
                        Variant Evaluation &bull; {v_band}
                    </span>
                    <span style="font-size: 13px; font-weight: 800; color: #f8fafc; background: rgba(255,255,255,0.06); padding: 2px 8px; border-radius: 4px;">
                        {v_score}% Match
                    </span>
                </div>
                <div style="color: #cbd5e1; font-size: 12.5px; line-height: 1.4; margin-bottom: 8px;">
                    {v_feedback}
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; font-size: 12px;">
                    <div>
                        <div style="font-weight: 700; color: #86efac; margin-bottom: 2px;">Verified Invariants:</div>
                        <ul style="margin: 0 0 0 16px; padding: 0;">{passed_html}</ul>
                    </div>
                    <div>
                        <div style="font-weight: 700; color: #fca5a5; margin-bottom: 2px;">Missing Invariants:</div>
                        <ul style="margin: 0 0 0 16px; padding: 0;">{missing_html}</ul>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Collapsible Model Solution & Self-Check Rubric
        with st.expander("Official Model Solution & Self-Check Rubric"):
            checklist_items = "\n".join([f"- [✓] {c['label']}" for c in iso_data.get('rubric_checks', [])])
            st.markdown(f"""
```sql
{iso_data.get('model_solution', '')}
```

**Self-Check Invariant Checklist:**
{checklist_items}
""")

    # -------------------------------------------------------------------------
    # 4. Evaluation Results Dashboard & AI Rubric Cockpit
    # -------------------------------------------------------------------------
    if eval_state_key in st.session_state:
        eval_res = st.session_state[eval_state_key]

        score_pct = eval_res.get("similarity_pct", 0.0)
        raw_cos = eval_res.get("raw_cosine_sim", 0.0)
        coverage_pct = eval_res.get("concept_coverage_pct", 0.0)
        grade_band = eval_res.get("grade_band", "Evaluated")
        grade_color = eval_res.get("grade_color", "#38bdf8")
        present = eval_res.get("present_concepts", [])
        missing = eval_res.get("missing_concepts", [])
        summary_text = eval_res.get("feedback_summary", "")

        # Chips for Verified and Missing Invariants
        if present:
            present_chips = "".join([
                f"<span style='display: inline-block; background: rgba(16, 185, 129, 0.12); border: 1px solid #10b981; color: #86efac; padding: 3px 8px; border-radius: 4px; font-size: 11px; margin: 2px 4px 2px 0;'>✓ {c}</span>"
                for c in present
            ])
        else:
            present_chips = "<span style='color: #94a3b8; font-size: 11px;'>No target invariants verified yet.</span>"

        if missing:
            missing_chips = "".join([
                f"<span style='display: inline-block; background: rgba(239, 68, 68, 0.12); border: 1px solid #ef4444; color: #fca5a5; padding: 3px 8px; border-radius: 4px; font-size: 11px; margin: 2px 4px 2px 0;'>✕ {c}</span>"
                for c in missing
            ])
        else:
            missing_chips = "<span style='color: #86efac; font-size: 11px; font-weight: 600;'>All key invariants verified! ✓</span>"

        # Dynamic Gradient Progress Bar
        bar_gradient = f"linear-gradient(90deg, {grade_color}88 0%, {grade_color} 100%)"

        st.markdown(f"""
        <div style="background: #111827; border: 1px solid #1f2937; border-left: 4px solid {grade_color}; border-radius: 10px; padding: 18px 22px; margin-top: 18px; margin-bottom: 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.25);">
            <!-- Cockpit Header -->
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; margin-bottom: 12px;">
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 12px; font-weight: 700; color: {grade_color}; text-transform: uppercase; letter-spacing: 0.8px;">
                        AI Evaluation Report
                    </span>
                    <span style="background: {grade_color}22; border: 1px solid {grade_color}; color: {grade_color}; padding: 3px 10px; border-radius: 9999px; font-size: 11px; font-weight: 700;">
                        {grade_band}
                    </span>
                </div>
                <div>
                    <span style="font-size: 24px; font-weight: 800; color: {grade_color}; letter-spacing: -0.5px;">{score_pct}%</span>
                    <span style="font-size: 12px; font-weight: 700; color: #94a3b8; text-transform: uppercase; margin-left: 4px;">Match</span>
                </div>
            </div>

            <!-- Dynamic Progress Meter -->
            <div style="background: #1e293b; border-radius: 9999px; height: 10px; overflow: hidden; margin-bottom: 16px; border: 1px solid #334155;">
                <div style="background: {bar_gradient}; width: {score_pct}%; height: 100%; border-radius: 9999px; transition: width 0.6s ease;"></div>
            </div>

            <!-- 3 Telemetry Metrics Grid -->
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-bottom: 16px;">
                <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid #1e293b; border-radius: 8px; padding: 10px 14px;">
                    <div style="font-size: 10.5px; color: #94a3b8; font-weight: 600; text-transform: uppercase;">Composite Score</div>
                    <div style="font-size: 15px; font-weight: 800; color: #f8fafc; margin-top: 2px;">{score_pct}%</div>
                </div>
                <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid #1e293b; border-radius: 8px; padding: 10px 14px;">
                    <div style="font-size: 10.5px; color: #94a3b8; font-weight: 600; text-transform: uppercase;">Vector Cosine Sim</div>
                    <div style="font-size: 15px; font-weight: 800; color: #38bdf8; margin-top: 2px;">{raw_cos}%</div>
                </div>
                <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid #1e293b; border-radius: 8px; padding: 10px 14px;">
                    <div style="font-size: 10.5px; color: #94a3b8; font-weight: 600; text-transform: uppercase;">Invariant Coverage</div>
                    <div style="font-size: 15px; font-weight: 800; color: #10b981; margin-top: 2px;">{coverage_pct}%</div>
                </div>
            </div>

            <!-- Invariants Chips -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 10px; font-size: 12px;">
                <div>
                    <div style="font-weight: 700; color: #86efac; margin-bottom: 6px; font-size: 11.5px; text-transform: uppercase; letter-spacing: 0.5px;">
                        Verified Invariants:
                    </div>
                    <div>{present_chips}</div>
                </div>
                <div>
                    <div style="font-weight: 700; color: #fca5a5; margin-bottom: 6px; font-size: 11.5px; text-transform: uppercase; letter-spacing: 0.5px;">
                        Missing Invariants:
                    </div>
                    <div>{missing_chips}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Socratic Diagnostic Review (comfortable spacing)
        diagnosis_text = st.session_state.get(f"diagnosis_{q_id}", summary_text)

        if diagnosis_text.strip().startswith("<div"):
            formatted_diagnosis = diagnosis_text.replace("\n", "")
        else:
            formatted_diagnosis = f"<div style='line-height: 1.55; color: #cbd5e1;'>{diagnosis_text.replace(chr(10), '<br>')}</div>"

        st.markdown(f"""
        <div style="background: #111827; border: 1px solid #1f2937; border-left: 4px solid #10b981; border-radius: 10px; padding: 16px 20px; margin-top: 14px; margin-bottom: 14px;">
            <div style="font-size: 11.5px; font-weight: 700; color: #10b981; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px;">
                Socratic Professor Feedback & Diagnostic Analysis
            </div>
            <div style="color: #cbd5e1; font-size: 13.5px; line-height: 1.55;">
                {formatted_diagnosis}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Collapsible Official Solution Drawer
        with st.expander("Inspect Official Solution Key", expanded=False):
            st.markdown("**Official Solution Key:**")
            st.code(current_q.get("solution_key", ""), language="sql")

    # -------------------------------------------------------------------------
    # 5. Continuous PYQ Navigation
    # -------------------------------------------------------------------------
    st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)
    nav_c1, nav_c2 = st.columns([1, 1])
    with nav_c1:
        if st.button("Previous Question", use_container_width=True, key=f"prev_btn_{selected_diff}_{cur_idx}"):
            st.session_state[cursor_key] = (cur_idx - 1) % len(tier_questions)
            st.rerun()
    with nav_c2:
        if st.button("Next Question", type="primary", use_container_width=True, key=f"next_btn_{selected_diff}_{cur_idx}"):
            st.session_state[cursor_key] = (cur_idx + 1) % len(tier_questions)
            st.rerun()

