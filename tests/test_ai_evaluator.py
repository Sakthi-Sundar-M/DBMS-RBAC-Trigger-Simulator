import json
import os
import unittest
from ai_engine.evaluator import evaluate_submission, compute_cosine_similarity
import numpy as np

class TestAIEvaluator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "exam_questions.json")
        with open(data_path, "r", encoding="utf-8") as f:
            cls.questions = json.load(f)

    def test_cosine_similarity_math(self):
        vec_a = np.array([1.0, 0.0, 0.0])
        vec_b = np.array([1.0, 0.0, 0.0])
        vec_c = np.array([0.0, 1.0, 0.0])

        self.assertAlmostEqual(compute_cosine_similarity(vec_a, vec_b), 1.0, places=4)
        self.assertAlmostEqual(compute_cosine_similarity(vec_a, vec_c), 0.0, places=4)

    def test_evaluate_perfect_answer(self):
        q = self.questions[0]
        # Evaluating the exact solution key
        result = evaluate_submission(q["solution_key"], q)
        self.assertGreaterEqual(result["similarity_pct"], 80.0)
        self.assertIn("Mastery", result["grade_band"])

    def test_evaluate_empty_submission(self):
        q = self.questions[0]
        result = evaluate_submission("", q)
        self.assertEqual(result["similarity_pct"], 0.0)
        self.assertEqual(result["grade_band"], "Not Submitted")

    def test_evaluate_imperfect_answer(self):
        q = self.questions[3]  # BEFORE vs AFTER question
        perfect_result = evaluate_submission(q["solution_key"], q)
        wrong_answer = "Triggers do not exist in relational databases. Use MongoDB collections and JSON documents instead."
        wrong_result = evaluate_submission(wrong_answer, q)
        # Should be penalized significantly compared to perfect answer
        self.assertLess(wrong_result["similarity_pct"], perfect_result["similarity_pct"])
        self.assertLess(wrong_result["similarity_pct"], 50.0)

if __name__ == "__main__":
    unittest.main()
