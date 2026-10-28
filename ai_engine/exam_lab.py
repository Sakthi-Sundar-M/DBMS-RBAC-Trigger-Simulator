import os
import json
import streamlit as st
from ai_engine.evaluator import evaluate_submission
from ai_engine.tutor import (
    diagnose_student_submission,
    generate_socratic_hint,
    generate_isomorphic_problem,
    evaluate_isomorphic_submission
)

@st.cache_data
def load_exam_questions():
    """
    Loads and caches the curated benchmark practice questions for descriptive/code mode.
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


@st.cache_data
def load_mcq_questions():
    """
    Loads and caches the 77 curated Indian entrance exam MCQs with 231 pre-computed domain variants.
    """
    dataset_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "mcq_exam_questions.json")
    if os.path.exists(dataset_path):
        try:
            with open(dataset_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    try:
        from ai_engine.mcq_data import MCQ_BENCHMARK_QUESTIONS
        return MCQ_BENCHMARK_QUESTIONS
    except Exception:
        return []


def render_exam_lab_tab(active_role="retail_customer"):
    """
    Renders Tab 5: Practice Lab & Exam Evaluator with dual modes:
      1. Competitive Exam MCQs (178 Authentic + Practice Variants)
      2. Descriptive & PL/pgSQL Code Lab (48 Practice Problems)
    """
    st.markdown("### AI-Powered Practice Lab & Exam Evaluator")

    # Mode Selector
    mode_options = [
        "Competitive Exam MCQs (178 Authentic + Practice Variants)",
        "Descriptive & Code Lab (48 Practice Problems)"
    ]
    selected_mode = st.radio(
        "Choose Practice Mode:",
        options=mode_options,
        index=0,
        horizontal=True,
        key="exam_lab_mode_selector"
    )

    st.markdown("<hr style='margin: 12px 0 18px 0; border: none; border-top: 1px solid #1e293b;'>", unsafe_allow_html=True)

    if selected_mode.startswith("Competitive"):
        render_mcq_lab(active_role)
    else:
        render_descriptive_lab(active_role)


def render_mcq_lab(active_role="retail_customer"):
    """
    Renders the Multiple-Choice Exam Lab featuring 178 authentic questions from GATE (50), ISRO (21), NIELIT (29), and UGC-NET (78).
    Provides immediate answer feedback, in-depth conceptual explanations, and 3 variants per question.
    """
    all_mcqs = load_mcq_questions()
    if not all_mcqs:
        st.error("MCQ dataset could not be loaded. Please ensure data/mcq_exam_questions.json exists.")
        return

    # Count statistics
    gate_count = sum(1 for q in all_mcqs if "GATE" in q.get("source", ""))
    isro_count = sum(1 for q in all_mcqs if "ISRO" in q.get("source", ""))
    nielit_count = sum(1 for q in all_mcqs if "NIELIT" in q.get("source", ""))
    ugc_count = sum(1 for q in all_mcqs if "UGC" in q.get("source", ""))
    total_variants = sum(len(q.get("variants", [])) for q in all_mcqs)

    st.markdown(f"""
    <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid #1e293b; border-radius: 8px; padding: 12px 18px; margin-bottom: 16px;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
            <div style="font-size: 13px; color: #cbd5e1;">
                Official Indian Competitive Entrance Exam Bank: <b style="color:#f8fafc;">{len(all_mcqs)} MCQs</b> with <b style="color:#38bdf8;">{total_variants} Pre-defined Practice Variants</b>
            </div>
            <div style="display: flex; gap: 6px; font-size: 11px;">
                <span style="background: rgba(56, 189, 248, 0.15); border: 1px solid #0284c7; color: #38bdf8; padding: 2px 8px; border-radius: 4px; font-weight: 700;">GATE: {gate_count}</span>
                <span style="background: rgba(16, 185, 129, 0.15); border: 1px solid #10b981; color: #10b981; padding: 2px 8px; border-radius: 4px; font-weight: 700;">ISRO: {isro_count}</span>
                <span style="background: rgba(245, 158, 11, 0.15); border: 1px solid #f59e0b; color: #f59e0b; padding: 2px 8px; border-radius: 4px; font-weight: 700;">NIELIT: {nielit_count}</span>
                <span style="background: rgba(192, 132, 252, 0.15); border: 1px solid #9333ea; color: #c084fc; padding: 2px 8px; border-radius: 4px; font-weight: 700;">UGC-NET: {ugc_count}</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # -------------------------------------------------------------------------
    # 1. Filter Controls
    # -------------------------------------------------------------------------
    f_col1, f_col2, f_col3 = st.columns([1.2, 1.4, 2])
    with f_col1:
        diff_filter = st.selectbox(
            "Difficulty Filter:",
            options=["All Difficulties", "Easy", "Medium", "Hard"],
            index=0,
            key="mcq_diff_filter"
        )
    with f_col2:
        source_filter = st.selectbox(
            "Exam Source Filter:",
            options=["All Exam Sources", "GATE CS/IT", "ISRO Scientist/Engineer", "NIELIT Scientist B", "UGC-NET CS"],
            index=0,
            key="mcq_source_filter"
        )
    with f_col3:
        all_topics = sorted(list(set(q.get("topic", "General") for q in all_mcqs)))
        topic_filter = st.selectbox(
            "DBMS Topic Filter:",
            options=["All Topics"] + all_topics,
            index=0,
            key="mcq_topic_filter"
        )

    # Apply filters
    filtered_mcqs = all_mcqs
    if diff_filter != "All Difficulties":
        filtered_mcqs = [q for q in filtered_mcqs if q.get("difficulty") == diff_filter]

    if source_filter == "GATE CS/IT":
        filtered_mcqs = [q for q in filtered_mcqs if "GATE" in q.get("source", "")]
    elif source_filter == "ISRO Scientist/Engineer":
        filtered_mcqs = [q for q in filtered_mcqs if "ISRO" in q.get("source", "")]
    elif source_filter == "NIELIT Scientist B":
        filtered_mcqs = [q for q in filtered_mcqs if "NIELIT" in q.get("source", "")]
    elif source_filter == "UGC-NET CS":
        filtered_mcqs = [q for q in filtered_mcqs if "UGC" in q.get("source", "")]


    if topic_filter != "All Topics":
        filtered_mcqs = [q for q in filtered_mcqs if q.get("topic") == topic_filter]

    if not filtered_mcqs:
        st.warning("No questions match the selected combination of filters. Reverting to all questions.")
        filtered_mcqs = all_mcqs

    # Session State Cursor
    if "mcq_cursor_idx" not in st.session_state:
        st.session_state["mcq_cursor_idx"] = 0

    if st.session_state["mcq_cursor_idx"] >= len(filtered_mcqs):
        st.session_state["mcq_cursor_idx"] = 0

    cur_idx = st.session_state["mcq_cursor_idx"]
    current_q = filtered_mcqs[cur_idx]
    qid = current_q["id"]

    # Jump-to selector
    jump_options = [f"{i+1}. [{q['id']}] {q['title']} ({q['source'][:25]}...)" for i, q in enumerate(filtered_mcqs)]
    jump_ver = st.session_state.get("mcq_nav_ver", 0)
    jump_key = f"mcq_jump_sel_{jump_ver}"

    def _sync_mcq_jump_to_cursor():
        picked = st.session_state.get(jump_key)
        if picked in jump_options:
            st.session_state["mcq_cursor_idx"] = jump_options.index(picked)

    nav_col1, nav_col2 = st.columns([3, 1])
    with nav_col1:
        st.selectbox(
            "Quick Navigate Question:",
            options=jump_options,
            index=cur_idx,
            key=jump_key,
            on_change=_sync_mcq_jump_to_cursor,
            label_visibility="collapsed"
        )

    with nav_col2:
        st.markdown(f"""
        <div style="display: flex; justify-content: flex-end; align-items: center; height: 100%;">
            <span style="background: #1e293b; border: 1px solid #334155; color: #94a3b8; padding: 6px 12px; border-radius: 6px; font-size: 12px; font-weight: 700;">
                Question {cur_idx + 1} of {len(filtered_mcqs)}
            </span>
        </div>
        """, unsafe_allow_html=True)

    # -------------------------------------------------------------------------
    # 2. Question Statement Card
    # -------------------------------------------------------------------------
    diff = current_q.get("difficulty", "Medium")
    if diff == "Easy":
        diff_pill = "<span style='background: rgba(16, 185, 129, 0.15); border: 1px solid #10b981; color: #10b981; padding: 2px 10px; border-radius: 9999px; font-size: 11px; font-weight: 700;'>EASY</span>"
    elif diff == "Medium":
        diff_pill = "<span style='background: rgba(56, 189, 248, 0.15); border: 1px solid #0284c7; color: #38bdf8; padding: 2px 10px; border-radius: 9999px; font-size: 11px; font-weight: 700;'>MEDIUM</span>"
    else:
        diff_pill = "<span style='background: rgba(192, 132, 252, 0.15); border: 1px solid #9333ea; color: #c084fc; padding: 2px 10px; border-radius: 9999px; font-size: 11px; font-weight: 700;'>HARD</span>"

    st.markdown(f"""<div style="background: #111827; border: 1px solid #1f2937; border-left: 4px solid #38bdf8; border-radius: 8px; padding: 18px 22px; margin-top: 10px; margin-bottom: 14px;">
<div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
<div>
<span style="font-size: 11px; font-weight: 700; color: #38bdf8; text-transform: uppercase; letter-spacing: 0.5px;">
{current_q.get('topic')} &bull; {current_q.get('subtopic')}
</span>
<h3 style="margin: 4px 0 0 0; color: #f8fafc; font-size: 18px; font-weight: 700;">
[{qid}] {current_q.get('title')}
</h3>
</div>
<div style="margin-top: 4px;">
{diff_pill} &nbsp;
<span style="background: #1e293b; border: 1px solid #334155; color: #94a3b8; padding: 3px 8px; border-radius: 4px; font-size: 11px; font-weight: 600;">
Source: {current_q.get('source')}
</span>
</div>
</div>
<div style="color: #f1f5f9; font-size: 14px; line-height: 1.6; margin-top: 14px; background: rgba(15, 23, 42, 0.65); padding: 14px 18px; border-radius: 6px; border: 1px solid #1e293b;">
{current_q.get('prompt')}
</div>
</div>""", unsafe_allow_html=True)

    # -------------------------------------------------------------------------
    # 3. Question & Isomorphic Variant Tabs
    # -------------------------------------------------------------------------
    variants = current_q.get("variants", [])
    tab_labels = ["Original Question"]
    for i, v in enumerate(variants):
        dom = v.get("domain", f"Variant {i+1}")
        short_dom = dom.split('&')[0].strip() if '&' in dom else dom[:22]
        tab_labels.append(f"Variant {i+1}: {short_dom}")

    created_tabs = st.tabs(tab_labels)
    tab_orig = created_tabs[0]
    var_tabs = created_tabs[1:]

    # ----------------- TAB: ORIGINAL QUESTION -----------------
    with tab_orig:
        ans_state_key = f"mcq_ans_selected_{qid}"
        submitted_key = f"mcq_submitted_{qid}"

        selected_opt = st.radio(
            "Select Your Option:",
            options=current_q["options"],
            key=ans_state_key
        )

        col_btn1, col_btn2 = st.columns([1.5, 3])
        with col_btn1:
            submit_btn = st.button("Submit & Verify Answer", type="primary", use_container_width=True, key=f"btn_sub_{qid}")

        if submit_btn or st.session_state.get(submitted_key, False):
            st.session_state[submitted_key] = True
            chosen_letter = selected_opt.strip()[0].upper()
            correct_letter = current_q.get("correct_option", "A").strip()[0].upper()

            if chosen_letter == correct_letter:
                st.success(f"✅ Correct! Option {correct_letter} is the right answer.")
            else:
                st.error(f"❌ Incorrect. You selected Option {chosen_letter}, but the correct answer is Option {correct_letter}.")

            # In-depth Explanation Card
            st.markdown(f"""<div style="background: #0f172a; border: 1px solid #1e293b; border-left: 4px solid #10b981; border-radius: 6px; padding: 14px 18px; margin-top: 10px;">
<div style="font-size: 11.5px; font-weight: 700; color: #10b981; text-transform: uppercase; margin-bottom: 6px;">
💡 Conceptual Rationale & Database Invariants:
</div>
<div style="color: #cbd5e1; font-size: 13px; line-height: 1.55;">
{current_q.get('explanation')}
</div>
</div>""", unsafe_allow_html=True)

    # ----------------- TABS: PRE-COMPUTED PRACTICE VARIANTS -----------------
    for v_idx, v_tab in enumerate(var_tabs):
        with v_tab:
            render_variant_card(variants[v_idx], qid, f"var_{v_idx+1}")

    # -------------------------------------------------------------------------
    # 4. Question Navigation Buttons (Bottom)
    # -------------------------------------------------------------------------
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    c_prev, c_next = st.columns([1, 1])
    with c_prev:
        if st.button("Previous Question", use_container_width=True, key=f"mcq_prev_btn_{cur_idx}"):
            st.session_state["mcq_cursor_idx"] = (cur_idx - 1) % len(filtered_mcqs)
            st.session_state["mcq_nav_ver"] = jump_ver + 1
            st.rerun()
    with c_next:
        if st.button("Next Question", type="primary", use_container_width=True, key=f"mcq_next_btn_{cur_idx}"):
            st.session_state["mcq_cursor_idx"] = (cur_idx + 1) % len(filtered_mcqs)
            st.session_state["mcq_nav_ver"] = jump_ver + 1
            st.rerun()


def render_variant_card(variant_data, qid, var_tag):
    """
    Renders an interactive variant card with radio selection, answer checker, and explanation.
    """
    domain = variant_data.get("domain", "Enterprise Scenario")
    st.markdown(f"""<div style="background: rgba(192, 132, 252, 0.08); border-left: 3px solid #c084fc; border-radius: 6px; padding: 12px 16px; margin-bottom: 12px;">
<span style="font-size: 11px; font-weight: 700; color: #c084fc; text-transform: uppercase;">
🔄 Adapted Domain: {domain}
</span>
<div style="color: #f1f5f9; font-size: 13.5px; line-height: 1.5; margin-top: 6px;">
{variant_data.get('prompt')}
</div>
</div>""", unsafe_allow_html=True)

    v_opts = variant_data.get("options", [])
    if not v_opts:
        st.warning("No options in variant.")
        return

    # Use hash of current options to isolate radio widget and avoid StreamlitAPIException on option mutations
    opt_hash = abs(hash(tuple(v_opts))) % 100000
    v_ans_key = f"v_radio_{qid}_{var_tag}_{opt_hash}"
    v_sub_key = f"v_sub_{qid}_{var_tag}_{opt_hash}"

    chosen_v_opt = st.radio(
        "Select Variant Answer:",
        options=v_opts,
        key=v_ans_key
    )

    if st.button("Verify Variant Response", key=f"v_btn_{qid}_{var_tag}_{opt_hash}", use_container_width=True):
        st.session_state[v_sub_key] = True

    if st.session_state.get(v_sub_key, False):
        chosen_l = chosen_v_opt.strip()[0].upper()
        corr_l = variant_data.get("correct_option", "A").strip()[0].upper()

        if chosen_l == corr_l:
            st.success(f"✅ Correct! Option {corr_l} matches the domain relational invariant.")
        else:
            st.error(f"❌ Incorrect. You selected Option {chosen_l}, but the correct answer is Option {corr_l}.")

        st.markdown(f"""<div style="background: #0f172a; border: 1px solid #1e293b; border-left: 4px solid #c084fc; border-radius: 6px; padding: 12px 16px; margin-top: 10px;">
<div style="font-size: 11px; font-weight: 700; color: #c084fc; text-transform: uppercase; margin-bottom: 4px;">
💡 Variant Rationale & Domain Analysis:
</div>
<div style="color: #cbd5e1; font-size: 12.5px; line-height: 1.5;">
{variant_data.get('explanation')}
</div>
</div>""", unsafe_allow_html=True)


def render_descriptive_lab(active_role="retail_customer"):
    """
    Renders the Descriptive & Code Workbench (48 benchmark questions) evaluated using Sentence-Transformers and Gemini.
    """
    questions = load_exam_questions()
    if not questions:
        st.error("Question bank could not be loaded. Please ensure data/exam_questions.json exists.")
        return

    st.markdown("Practice actual GATE CS, ISRO, and Premier University Master's entrance questions on PostgreSQL Triggers and RBAC. Submissions are evaluated using a hybrid AI engine: **local Sentence-Transformers for deterministic cosine similarity grading** and **Google Gemini for Socratic error diagnosis**.")

    diff_col1, diff_col2, diff_col3 = st.columns([1.5, 2, 1])
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

    desc_jump_opts = [f"{i+1}. [{q['id']}] {q['title']}" for i, q in enumerate(tier_questions)]
    desc_ver_key = f"desc_nav_ver_{selected_diff}"
    desc_ver = st.session_state.get(desc_ver_key, 0)
    desc_jump_key = f"desc_jump_{selected_diff}_{desc_ver}"

    def _sync_desc_jump():
        picked = st.session_state.get(desc_jump_key)
        if picked in desc_jump_opts:
            st.session_state[cursor_key] = desc_jump_opts.index(picked)

    with diff_col2:
        st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)
        st.selectbox(
            "Quick Navigate Question:",
            options=desc_jump_opts,
            index=cur_idx,
            key=desc_jump_key,
            on_change=_sync_desc_jump,
            label_visibility="collapsed"
        )

    with diff_col3:
        st.markdown(f"""
        <div style="display: flex; justify-content: flex-end; align-items: center; height: 100%; padding-top: 24px;">
            <span style="background: #1e293b; border: 1px solid #334155; color: #94a3b8; padding: 6px 12px; border-radius: 6px; font-size: 11px; font-weight: 700;">
                Question {cur_idx + 1} of {len(tier_questions)}
            </span>
        </div>
        """, unsafe_allow_html=True)

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

    btn_col1, btn_col2, btn_col3, btn_col4 = st.columns([2, 1.5, 1.5, 2])
    with btn_col1:
        submit_eval = st.button("Submit for AI Evaluation", type="primary", use_container_width=True, key=f"eval_btn_{q_id}")
    with btn_col2:
        req_hint1 = st.button("Request Hint (Level 1)", use_container_width=True, key=f"hint1_btn_{q_id}")
    with btn_col3:
        req_hint2 = st.button("Request Hint (Level 2)", use_container_width=True, key=f"hint2_btn_{q_id}")
    with btn_col4:
        gen_iso = st.button("Generate Practice Variant", use_container_width=True, key=f"iso_btn_{q_id}")

    eval_state_key = f"eval_result_{q_id}"
    if submit_eval:
        with st.spinner("Analyzing semantic embeddings and DBMS relational invariants..."):
            eval_res = evaluate_submission(student_code, current_q)
            st.session_state[eval_state_key] = eval_res
            diagnosis = diagnose_student_submission(current_q, student_code, eval_res)
            st.session_state[f"diagnosis_{q_id}"] = diagnosis

    hint_state_key = f"hint_{q_id}"
    if req_hint1:
        with st.spinner("Synthesizing Level 1 Socratic hint..."):
            h1 = generate_socratic_hint(current_q, student_code, hint_level=1)
            st.session_state[hint_state_key] = ("Level 1 Hint", h1)
    elif req_hint2:
        with st.spinner("Synthesizing Level 2 Socratic hint..."):
            h2 = generate_socratic_hint(current_q, student_code, hint_level=2)
            st.session_state[hint_state_key] = ("Level 2 Hint", h2)

    iso_state_key = f"iso_problem_{q_id}"
    if gen_iso:
        with st.spinner("Synthesizing isomorphic problem variant..."):
            iso_res = generate_isomorphic_problem(current_q)
            st.session_state[iso_state_key] = iso_res

    if hint_state_key in st.session_state:
        htitle, htext = st.session_state[hint_state_key]
        st.markdown(f"""
        <div style="background: rgba(245, 158, 11, 0.08); border-left: 3px solid #f59e0b; border-radius: 6px; padding: 12px 16px; margin: 12px 0;">
            <div style="font-size: 11px; font-weight: 700; color: #f59e0b; text-transform: uppercase;">{htitle}</div>
            <div style="color: #cbd5e1; font-size: 13px; margin-top: 4px; line-height: 1.5;">{htext}</div>
        </div>
        """, unsafe_allow_html=True)

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

        v_ans_key = f"iso_student_ans_{q_id}_{current_dept_idx}_{current_var_idx}"
        v_default_code = iso_data.get("starter_code", "-- Write your SQL solution here")
        if v_ans_key not in st.session_state:
            st.session_state[v_ans_key] = v_default_code

        v_student_code = st.text_area(
            f"Solve Isomorphic Variation ({iso_data.get('scenario_title')}):",
            value=st.session_state[v_ans_key],
            height=160,
            key=f"iso_text_area_{q_id}_{current_dept_idx}_{current_var_idx}"
        )
        st.session_state[v_ans_key] = v_student_code

        v_eval_key = f"iso_eval_result_{q_id}_{current_dept_idx}_{current_var_idx}"
        v_col1, v_col2 = st.columns([2, 3])
        with v_col1:
            if st.button("Evaluate Isomorphic Solution", type="primary", use_container_width=True, key=f"iso_eval_btn_{q_id}_{current_dept_idx}_{current_var_idx}"):
                with st.spinner("Analyzing isomorphic invariants and schema compliance..."):
                    iso_eval_res = evaluate_isomorphic_submission(v_student_code, iso_data)
                    st.session_state[v_eval_key] = iso_eval_res

        if v_eval_key in st.session_state:
            v_res = st.session_state[v_eval_key]
            v_score = v_res.get("score", 0)
            v_band = v_res.get("grade_band", "Evaluated")
            v_feedback = v_res.get("feedback", "")
            v_passed = v_res.get("passed_checks", [])
            v_missing = v_res.get("missing_checks", [])

            if v_band == "Not Submitted" or v_score == 0:
                badge_color = "#94a3b8"
            elif v_score >= 80:
                badge_color = "#10b981"
            elif v_score >= 50:
                badge_color = "#f59e0b"
            else:
                badge_color = "#ef4444"

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

        with st.expander("Official Model Solution & Self-Check Rubric"):
            checklist_items = "\n".join([f"- [✓] {c['label']}" for c in iso_data.get('rubric_checks', [])])
            st.markdown(f"""
```sql
{iso_data.get('model_solution', '')}
```

**Self-Check Invariant Checklist:**
{checklist_items}
""")

    if eval_state_key in st.session_state:
        eval_res = st.session_state[eval_state_key]
        diagnosis_text = st.session_state.get(f"diagnosis_{q_id}", eval_res.get("feedback_summary", ""))

        if diagnosis_text.strip().startswith("<div"):
            formatted_diagnosis = diagnosis_text.replace("\n", "")
        else:
            formatted_diagnosis = f"<div style='line-height: 1.5; color: #cbd5e1;'>{diagnosis_text.replace(chr(10), '<br>')}</div>"

        st.markdown(f"""
        <div style="background: #111827; border: 1px solid #1f2937; border-left: 4px solid #10b981; border-radius: 8px; padding: 16px 20px; margin-top: 14px; margin-bottom: 14px;">
            <div style="font-size: 11.5px; font-weight: 700; color: #10b981; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px;">
                Socratic Professor Feedback & Diagnostic Analysis
            </div>
            <div style="color: #cbd5e1; font-size: 13.5px; line-height: 1.5;">
                {formatted_diagnosis}
            </div>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("Inspect Official Solution Key", expanded=False):
            st.markdown("**Official Solution Key:**")
            st.code(current_q.get("solution_key", ""), language="sql")

    st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)
    nav_c1, nav_c2 = st.columns([1, 1])
    with nav_c1:
        if st.button("Previous Question", use_container_width=True, key=f"prev_btn_{selected_diff}_{cur_idx}"):
            st.session_state[cursor_key] = (cur_idx - 1) % len(tier_questions)
            st.session_state[desc_ver_key] = desc_ver + 1
            st.rerun()
    with nav_c2:
        if st.button("Next Question", type="primary", use_container_width=True, key=f"next_btn_{selected_diff}_{cur_idx}"):
            st.session_state[cursor_key] = (cur_idx + 1) % len(tier_questions)
            st.session_state[desc_ver_key] = desc_ver + 1
            st.rerun()
