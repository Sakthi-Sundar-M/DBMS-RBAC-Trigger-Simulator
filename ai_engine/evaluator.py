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
    # Clamp between 0.0 and 1.0
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


def check_concept_invariants(student_text: str, key_concepts: List[str]) -> Tuple[List[str], List[str]]:
    """
    Checks whether key DBMS architectural invariants were mentioned or utilized in the student's answer.
    Returns (present_concepts, missing_concepts).
    """
    student_lower = student_text.lower()
    present = []
    missing = []
    for concept in key_concepts:
        # Check either whole phrase or key keywords in the concept
        words = [w for w in re.split(r"[^a-zA-Z0-9_]+", concept.lower()) if len(w) > 2]
        if any(w in student_lower for w in words):
            present.append(concept)
        else:
            missing.append(concept)
    return present, missing


def evaluate_submission(student_text: str, question: Dict[str, Any]) -> Dict[str, Any]:
    """
    Evaluates a student's answer against the verified solution key and rubric.
    Combines:
      1. Dense vector embedding cosine similarity (Sentence-Transformers)
      2. Key architectural concept verification
      3. Rubric performance categorization
    """
    if not student_text or not student_text.strip():
        return {
            "score": 0.0,
            "similarity_pct": 0.0,
            "grade_band": "Not Submitted",
            "grade_color": "#94a3b8",
            "present_concepts": [],
            "missing_concepts": question.get("evaluation_rubric", {}).get("key_concepts", []),
            "feedback_summary": "Please write your SQL solution or conceptual explanation above to evaluate."
        }

    solution_key = question.get("solution_key", "")
    ground_truth = question.get("ground_truth_explanation", "")
    target_reference = f"{solution_key}\n\n{ground_truth}".strip()

    model = get_embedding_model()
    if model is not None:
        try:
            embeddings = model.encode([student_text, target_reference], normalize_embeddings=True)
            cos_sim = compute_cosine_similarity(embeddings[0], embeddings[1])
        except Exception:
            cos_sim = fallback_token_similarity(student_text, target_reference)
    else:
        cos_sim = fallback_token_similarity(student_text, target_reference)

    # Concept verification
    key_concepts = question.get("evaluation_rubric", {}).get("key_concepts", [])
    present, missing = check_concept_invariants(student_text, key_concepts)

    # Concept coverage modifier
    concept_ratio = len(present) / len(key_concepts) if key_concepts else 1.0

    # Composite weighted score (70% embedding similarity, 30% specific concept keywords)
    final_score = float(np.clip((0.70 * cos_sim) + (0.30 * concept_ratio), 0.0, 1.0))
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
        "raw_cosine_sim": round(cos_sim * 100, 1),
        "concept_coverage_pct": round(concept_ratio * 100, 1),
        "grade_band": grade_band,
        "grade_color": grade_color,
        "present_concepts": present,
        "missing_concepts": missing,
        "feedback_summary": summary
    }
