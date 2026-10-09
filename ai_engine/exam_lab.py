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

    st.markdown("### AI-Powered Practice Lab & Exam Evaluator")
    st.markdown("Practice actual GATE CS, ISRO, and Premier University Master's entrance questions on PostgreSQL Triggers and RBAC. Submissions are evaluated using a hybrid AI engine: **local Sentence-Transformers for deterministic cosine similarity grading** and **Google Gemini for Socratic error diagnosis**.")

    # -------------------------------------------------------------------------
    # 1. Difficulty Level Selector
    # -------------------------------------------------------------------------
    diff_col1, diff_col2 = st.columns([2, 1])
    with diff_col1:
        selected_diff = st.radio(
            "Select Practice Difficulty Level:",
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


    # -------------------------------------------------------------------------
    # 2. Problem Statement Card
    # -------------------------------------------------------------------------
    diff = current_q.get("difficulty", "Medium")
    if diff == "Easy":
        diff_badge = "<span style='background: rgba(134, 197, 160, 0.15); border: 1px solid #86C5A0; color: #86C5A0; padding: 2px 10px; border-radius: 9999px; font-size: 11px; font-weight: 700;'>EASY</span>"
    elif diff == "Medium":
        diff_badge = "<span style='background: rgba(205, 168, 90, 0.15); border: 1px solid #B8975A; color: #E0C27F; padding: 2px 10px; border-radius: 9999px; font-size: 11px; font-weight: 700;'>MEDIUM</span>"
    else:
        diff_badge = "<span style='background: rgba(167, 191, 207, 0.15); border: 1px solid #7FA0B3; color: #A7BFCF; padding: 2px 10px; border-radius: 9999px; font-size: 11px; font-weight: 700;'>HARD</span>"

    st.markdown(f"""
    <div class="exam-question-card">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
            <div>
                <span style="font-size: 11px; font-weight: 700; color: #F0786B; text-transform: none; ">
                    {current_q.get('topic')} &bull; {current_q.get('subtopic')}
                </span>
                <h3 style="margin: 4px 0 0 0; color: #ECEEF2; font-size: 18px;">
                    {current_q.get('title')}
                </h3>
            </div>
            <div style="margin-top: 4px;">
                {diff_badge} &nbsp;
                <span style="background: #171C26; border: 1px solid #353D4B; color: #5BD3AE; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 600;">
                    Source: {current_q.get('source')}
                </span>
            </div>
        </div>
        <div class="exam-prompt-box">
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
        submit_eval = st.button("Submit for AI Evaluation", type="primary", width="stretch", key=f"eval_btn_{q_id}")
    with btn_col2:
        req_hint1 = st.button("Request Hint (Level 1)", width="stretch", key=f"hint1_btn_{q_id}")
    with btn_col3:
        req_hint2 = st.button("Request Hint (Level 2)", width="stretch", key=f"hint2_btn_{q_id}")
    with btn_col4:
        gen_iso = st.button("Generate Practice Variant", width="stretch", key=f"iso_btn_{q_id}")

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
        <div class="exam-hint-box">
            <div style="font-size: 11px; font-weight: 700; color: #F0786B; text-transform: none;">{htitle}</div>
            <div style="color: #AEB5C0; font-size: 13px; margin-top: 4px; line-height: 1.5;">{htext}</div>
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
        <div class="exam-challenge-box">
            <div style="font-size: 11px; font-weight: 700; color: #AEB5C0; text-transform: none;">
                Practice variant (Adapting '{current_q.get('title')}')
            </div>
            <div style="color: #AEB5C0; font-size: 12px; margin-top: 4px;">
                Department: <b style="color: #ECEEF2;">{iso_data.get('domain')}</b> &bull; Scenario: <b style="color: #ECEEF2;">{iso_data.get('scenario_title')}</b> (Variation {current_var_idx + 1} of {total_vars})
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
            cycle_var = st.button("Next variation", key=f"iso_next_var_{q_id}", width="stretch")

        if sel_dept != dept_options[current_dept_idx]:
            new_dept_idx = dept_options.index(sel_dept)
            st.session_state[iso_state_key] = generate_isomorphic_problem(current_q, dept_idx=new_dept_idx, var_idx=0)
            st.rerun()

        if cycle_var:
            st.session_state[iso_state_key] = generate_isomorphic_problem(current_q, dept_idx=current_dept_idx, advance_variation=True)
            st.rerun()

        if iso_data.get("ai_generated_content"):
            st.markdown(f"""
            <div style="background: #171C26; border: 1px solid #353D4B; border-radius: 6px; padding: 14px 18px; margin-bottom: 12px; color: #ECEEF2; font-size: 13px; line-height: 1.5;">
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
        <div style="font-size: 11px; font-weight: 700; color: #AEB5C0; text-transform: none;  margin-top: 14px; margin-bottom: 4px;">
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
                width="stretch",
                key=f"eval_v_btn_{q_id}_{current_dept_idx}_{current_var_idx}"
            )
        with v_btn_col2:
            reset_variant_clicked = st.button(
                "Reset Starter Code",
                width="stretch",
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

            badge_color = "#86C5A0" if v_score >= 80 else ("#CDA85A" if v_score >= 50 else "#E2745C")

            passed_html = "".join([f"<li style='color: #A9D8BC; margin: 2px 0;'>✓ {c}</li>" for c in v_passed]) if v_passed else "<li style='color: #9DB0B0;'>No target invariants matched yet.</li>"
            missing_html = "".join([f"<li style='color: #F1A896; margin: 2px 0;'>✕ {c}</li>" for c in v_missing]) if v_missing else "<li style='color: #A9D8BC;'>All key invariants verified!</li>"

            st.markdown(f"""
            <div style="background: #171C26; border: 1px solid #353D4B; border-left: 4px solid {badge_color}; border-radius: 6px; padding: 12px 16px; margin: 10px 0;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <span style="font-size: 11px; font-weight: 700; color: {badge_color}; text-transform: none;">
                        Variant Evaluation &bull; {v_band}
                    </span>
                    <span style="font-size: 13px; font-weight: 800; color: #ECEEF2; background: rgba(255,255,255,0.06); padding: 2px 8px; border-radius: 4px;">
                        {v_score}% Match
                    </span>
                </div>
                <div style="color: #AEB5C0; font-size: 12.5px; line-height: 1.4; margin-bottom: 8px;">
                    {v_feedback}
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; font-size: 12px;">
                    <div>
                        <div style="font-weight: 700; color: #5BD3AE; margin-bottom: 2px;">Verified Invariants:</div>
                        <ul style="margin: 0 0 0 16px; padding: 0;">{passed_html}</ul>
                    </div>
                    <div>
                        <div style="font-weight: 700; color: #F0786B; margin-bottom: 2px;">Missing Invariants:</div>
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
    # 4. Evaluation Results Dashboard
    # -------------------------------------------------------------------------
    if eval_state_key in st.session_state:
        eval_res = st.session_state[eval_state_key]

        # Socratic Diagnostic Review (compact line spacing)
        diagnosis_text = st.session_state.get(f"diagnosis_{q_id}", eval_res.get("feedback_summary", ""))

        if diagnosis_text.strip().startswith("<div"):
            formatted_diagnosis = diagnosis_text.replace("\n", "")
        else:
            formatted_diagnosis = f"<div style='line-height: 1.35; color: #D9E1DE;'>{diagnosis_text.replace(chr(10), '<br>')}</div>"

        st.markdown(f"""
        <div style="background: #171C26; border: 1px solid #353D4B; border-left: 4px solid #86C5A0; border-radius: 8px; padding: 14px 18px; margin-top: 14px;">
            <div style="font-size: 11px; font-weight: 700; color: #5BD3AE; text-transform: none;  margin-bottom: 6px;">
                Socratic Professor Feedback & Diagnostic Analysis
            </div>
            <div style="color: #AEB5C0; font-size: 13px; line-height: 1.35;">
                {formatted_diagnosis}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Collapsible Official Solution Drawer (duplicate theoretical background removed)
        with st.expander("Inspect Official Solution Key", expanded=False):
            st.markdown("**Official Solution Key:**")
            st.code(current_q.get("solution_key", ""), language="sql")

    # -------------------------------------------------------------------------
    # 5. Continuous PYQ Navigation
    # -------------------------------------------------------------------------
    st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)
    nav_c1, nav_c2 = st.columns([1, 1])
    with nav_c1:
        if st.button("Previous Question", width="stretch", key=f"prev_btn_{selected_diff}_{cur_idx}"):
            st.session_state[cursor_key] = (cur_idx - 1) % len(tier_questions)
            st.rerun()
    with nav_c2:
        if st.button("Next Question", type="primary", width="stretch", key=f"next_btn_{selected_diff}_{cur_idx}"):
            st.session_state[cursor_key] = (cur_idx + 1) % len(tier_questions)
            st.rerun()

