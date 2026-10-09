import os
import re
import numpy as np
from typing import Dict, Any, List, Tuple

# Global cached embedding model instance to avoid reloading overhead
_MODEL_CACHE = None

def get_embedding_model():
    """
    Lazy-loads the lightweight sentence-transformers model on CPU.
    Prioritizes fine-tuned weights from models/dbms-trigger-evaluator if available,
    otherwise falls back to sentence-transformers/all-MiniLM-L6-v2.
    Takes ~80 MB RAM and caches in memory across Streamlit re-runs.
    """
    global _MODEL_CACHE
    if _MODEL_CACHE is None:
        try:
            from sentence_transformers import SentenceTransformer
            custom_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "models", "dbms-trigger-evaluator")
            if os.path.exists(custom_dir) and os.path.isdir(custom_dir):
                _MODEL_CACHE = SentenceTransformer(custom_dir, device="cpu")
            else:
                _MODEL_CACHE = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu")
        except Exception:
            _MODEL_CACHE = None
    return _MODEL_CACHE


def compute_cosine_similarity(vec_a: np.ndarray, vec_b: np.ndarray) -> float:
    """
    Calculates exact Cosine Similarity between two dense embedding vectors:
    cos_sim = (A . B) / (||A|| * ||B||)
    """
    dot_product = np.dot(vec_a, vec_b)
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    sim = dot_product / (norm_a * norm_b)
    return float(np.clip(sim, 0.0, 1.0))


def fallback_token_similarity(text_a: str, text_b: str) -> float:
    """
    Lightweight fallback token Jaccard + N-gram overlap similarity
    used if transformer model is loading or offline.
    """
    tokens_a = set(re.findall(r"\b[A-Za-z0-9_]+\b", text_a.lower()))
    tokens_b = set(re.findall(r"\b[A-Za-z0-9_]+\b", text_b.lower()))
    if not tokens_a or not tokens_b:
        return 0.0
    intersection = tokens_a.intersection(tokens_b)
    union = tokens_a.union(tokens_b)
    return float(len(intersection) / len(union))


def is_unanswered_template(student_text: str, starter_code: str) -> bool:
    """
    Detects if the student submission is empty or contains only the unedited starter template
    without any actual student answer content.
    """
    if not student_text or not student_text.strip():
        return True

    s_clean = re.sub(r"\s+", " ", student_text.strip().lower())
    st_clean = re.sub(r"\s+", " ", (starter_code or "").strip().lower())
    if s_clean == st_clean:
        return True

    starter_lines = set(re.sub(r"\s+", " ", l.strip().lower()) for l in (starter_code or "").splitlines() if l.strip())
    student_lines = [l.strip() for l in student_text.splitlines() if l.strip()]

    novel_content_lines = []
    for l in student_lines:
        norm_l = re.sub(r"\s+", " ", l.lower())
        if norm_l in starter_lines:
            continue
        # Ignore empty comment lines / prompt prefixes (e.g. "-- 1. Event:" or "-- Event:")
        if re.match(r"^--\s*(\d+\.?\s*[a-zA-Z_]+:?)?\s*$", l):
            continue
        # Ignore stripped instruction lines
        uncom = re.sub(r"^--\s*", "", norm_l).strip()
        if any(uncom == re.sub(r"^--\s*", "", sl).strip() for sl in starter_lines):
            continue
        novel_content_lines.append(l)

    if not novel_content_lines:
        return True

    # Count meaningful answer tokens added by the student
    added_tokens = re.findall(r"\b[a-zA-Z0-9_]{2,}\b", " ".join(novel_content_lines))
    return len(added_tokens) < 3


def clean_answer_text(student_text: str, starter_code: str = "") -> str:
    """
    Normalizes student answer by removing SQL comment markers and instructional boilerplate,
    isolating the actual conceptual or code answer regardless of formatting.
    """
    starter_lines = set(re.sub(r"\s+", " ", l.strip().lower()) for l in (starter_code or "").splitlines() if l.strip())
    cleaned = []
    for line in student_text.splitlines():
        l_str = line.strip()
        if not l_str:
            continue
        # Strip leading comment prefixes (-- , # , // , /* )
        uncom = re.sub(r"^(?:--|#|//|\*+)\s*", "", l_str).strip()
        norm_raw = re.sub(r"\s+", " ", l_str.lower())
        norm_uncom = re.sub(r"\s+", " ", uncom.lower())

        # Omit lines that are purely prompt instructions without answers
        if (norm_raw in starter_lines or norm_uncom in starter_lines) and re.match(r"^(which|explain|describe|write|implement|please)\b", norm_uncom, re.I):
            continue
        cleaned.append(uncom if uncom else l_str)
    return "\n".join(cleaned) if cleaned else student_text.strip()


def evaluate_concept_scores(student_text: str, key_concepts: List[str], model=None) -> Tuple[List[str], List[str], List[float]]:
    """
    Evaluates student answer against each key concept invariant in the rubric using
    dense semantic embeddings and domain technical keyword verification.
    Returns (present_concepts, missing_concepts, concept_scores).
    """
    if not key_concepts:
        return [], [], []

    cleaned_lower = student_text.lower()
    chunks = [c.strip() for c in re.split(r"[\n;\.]+", student_text) if len(c.strip()) > 3]
    if not chunks:
        chunks = [student_text.strip()]

    if model is not None:
        try:
            emb_chunks = model.encode(chunks, normalize_embeddings=True)
            emb_full = model.encode(student_text, normalize_embeddings=True)
            emb_concepts = model.encode(key_concepts, normalize_embeddings=True)
            sim_matrix = np.dot(emb_concepts, emb_chunks.T)
            sim_full = np.dot(emb_concepts, emb_full)
        except Exception:
            sim_matrix, sim_full = None, None
    else:
        sim_matrix, sim_full = None, None

    concept_scores = []
    present = []
    missing = []

    for i, concept in enumerate(key_concepts):
        if sim_matrix is not None and sim_full is not None:
            max_chunk_sim = float(sim_matrix[i].max()) if sim_matrix.shape[1] > 0 else 0.0
            sem_sim = max(max_chunk_sim, float(sim_full[i]))
        else:
            sem_sim = 0.0

        concept_terms = [
            w for w in re.split(r"[^a-zA-Z0-9_]+", concept.lower())
            if len(w) > 2 and w not in {"the", "and", "for", "with", "that", "this", "are", "can", "when"}
        ]
        matched_terms = [w for w in concept_terms if re.search(r"\b" + re.escape(w) + r"\b", cleaned_lower)]
        kw_ratio = len(matched_terms) / len(concept_terms) if concept_terms else 0.0

        is_present = (sem_sim >= 0.60) or (sem_sim >= 0.50 and kw_ratio >= 0.40) or (kw_ratio >= 0.50 and len(matched_terms) >= 2)

        if is_present:
            if sem_sim >= 0.75:
                c_score = 1.0
            elif sem_sim >= 0.60:
                c_score = 0.90 + (sem_sim - 0.60) * 0.66
            elif sem_sim >= 0.50:
                c_score = 0.75 + (sem_sim - 0.50) * 1.50
            else:
                c_score = max(0.85, kw_ratio)
            present.append(concept)
        else:
            if sem_sim >= 0.40:
                c_score = 0.35 + (sem_sim - 0.40) * 1.50
            elif kw_ratio >= 0.30:
                c_score = kw_ratio * 0.60
            else:
                c_score = 0.0
            missing.append(concept)

        concept_scores.append(float(np.clip(c_score, 0.0, 1.0)))

    return present, missing, concept_scores


def check_concept_invariants(student_text: str, key_concepts: List[str]) -> Tuple[List[str], List[str]]:
    """
    Checks whether key DBMS architectural invariants were accurately expressed.
    Returns (present_concepts, missing_concepts) for backward compatibility.
    """
    model = get_embedding_model()
    present, missing, _ = evaluate_concept_scores(student_text, key_concepts, model=model)
    return present, missing


def evaluate_submission(student_text: str, question: Dict[str, Any]) -> Dict[str, Any]:
    """
    Evaluates a student's answer against the verified solution key and rubric.
    Focuses on substantive answer content regardless of formatting.
    Correctly recognizes untouched starter templates as 0.0%.
    """
    starter_code = question.get("starter_code", "")
    key_concepts = question.get("evaluation_rubric", {}).get("key_concepts", [])

    if not student_text or not student_text.strip() or is_unanswered_template(student_text, starter_code):
        return {
            "score": 0.0,
            "similarity_pct": 0.0,
            "raw_cosine_sim": 0.0,
            "concept_coverage_pct": 0.0,
            "grade_band": "Not Submitted",
            "grade_color": "#94a3b8",
            "present_concepts": [],
            "missing_concepts": key_concepts,
            "feedback_summary": "Please write your SQL solution or conceptual explanation above to evaluate."
        }

    clean_ans = clean_answer_text(student_text, starter_code)
    model = get_embedding_model()
    present, missing, concept_scores = evaluate_concept_scores(clean_ans, key_concepts, model=model)

    concept_ratio = len(present) / len(key_concepts) if key_concepts else 1.0
    avg_concept_score = float(np.mean(concept_scores)) if concept_scores else 1.0

    solution_key = question.get("solution_key", "")
    ground_truth = question.get("ground_truth_explanation", "")

    if model is not None:
        try:
            emb_student = model.encode(clean_ans, normalize_embeddings=True)
            emb_sol = model.encode(solution_key, normalize_embeddings=True)
            sim_sol = compute_cosine_similarity(emb_student, emb_sol)
            if ground_truth:
                emb_gt = model.encode(ground_truth, normalize_embeddings=True)
                sim_gt = compute_cosine_similarity(emb_student, emb_gt)
            else:
                sim_gt = 0.0
            raw_cos_sim = max(sim_sol, sim_gt)
        except Exception:
            raw_cos_sim = fallback_token_similarity(clean_ans, solution_key)
    else:
        raw_cos_sim = fallback_token_similarity(clean_ans, solution_key)

    if key_concepts:
        # Effective solution similarity: format-independent weighting ensures full marks for concise correct answers
        effective_sol_sim = max(raw_cos_sim, avg_concept_score)
        final_score = float(np.clip(0.80 * avg_concept_score + 0.20 * effective_sol_sim, 0.0, 1.0))
    else:
        final_score = raw_cos_sim

    similarity_pct = round(final_score * 100, 1)

    # Determine Grade Band
    if similarity_pct >= 85.0:
        grade_band = "Mastery (Excellent)"
        grade_color = "#10b981"  # Emerald
        summary = "Your answer closely aligns with the standard relational DBMS solution and captures the key architectural invariants."
    elif similarity_pct >= 68.0:
        grade_band = "Proficient (Good)"
        grade_color = "#38bdf8"  # Sky blue
        summary = "Your answer captures the core logic well, but minor edge cases or technical precision could be refined."
    elif similarity_pct >= 45.0:
        grade_band = "Developing (Partial Credit)"
        grade_color = "#f59e0b"  # Amber
        summary = "You identified some relevant concepts, but key architectural rules (such as execution timing or transition variable states) are missing or reversed."
    else:
        grade_band = "Needs Review"
        grade_color = "#ef4444"  # Red
        summary = "Your submission diverges significantly from the verified solution. Review the recommended concepts and request a hint."

    return {
        "score": final_score,
        "similarity_pct": similarity_pct,
        "raw_cosine_sim": round(raw_cos_sim * 100, 1),
        "concept_coverage_pct": round(concept_ratio * 100, 1),
        "grade_band": grade_band,
        "grade_color": grade_color,
        "present_concepts": present,
        "missing_concepts": missing,
        "feedback_summary": summary
    }
