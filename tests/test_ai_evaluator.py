import os
import unittest
import numpy as np
from ai_engine.evaluator import evaluate_submission, compute_cosine_similarity

class TestAIEvaluator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            from ai_engine.questions_data import BENCHMARK_QUESTIONS
            cls.questions = BENCHMARK_QUESTIONS
        except Exception:
            import json
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
        result = evaluate_submission(q["solution_key"], q)
        self.assertGreaterEqual(result["similarity_pct"], 85.0)
        self.assertIn("Mastery", result["grade_band"])

    def test_evaluate_empty_submission(self):
        q = self.questions[0]
        result = evaluate_submission("", q)
        self.assertEqual(result["similarity_pct"], 0.0)
        self.assertEqual(result["grade_band"], "Not Submitted")

    def test_evaluate_untouched_starter_template(self):
        q = self.questions[0]
        starter = q.get("starter_code", "")
        # Submitting the untouched starter template must yield 0% and Not Submitted
        result = evaluate_submission(starter, q)
        self.assertEqual(result["similarity_pct"], 0.0)
        self.assertEqual(result["grade_band"], "Not Submitted")
        self.assertEqual(len(result["present_concepts"]), 0)

    def test_evaluate_format_independent_accurate_answer(self):
        q = self.questions[0]
        student_ans = """Event is DML operation/timing
Condition is boolean predicate
Action is procedural body
Condition controls whether actions fires"""
        result = evaluate_submission(student_ans, q)
        self.assertGreaterEqual(result["similarity_pct"], 90.0)
        self.assertIn("Mastery", result["grade_band"])
        self.assertEqual(len(result["missing_concepts"]), 0)

    def test_evaluate_kept_format_accurate_answer(self):
        q = self.questions[0]
        ans_kept = """-- Explain the 3 ECA primitives:
-- 1. Event: DML operation (insert, update, delete) and timing
-- 2. Condition: boolean predicate evaluated on transition memory
-- 3. Action: procedural code block
-- Which primitive controls conditional execution?
Condition primitive controls whether action fires"""
        result = evaluate_submission(ans_kept, q)
        self.assertGreaterEqual(result["similarity_pct"], 90.0)
        self.assertIn("Mastery", result["grade_band"])

    def test_evaluate_wrong_answer(self):
        q = self.questions[3]
        wrong_answer = "Triggers do not exist in relational databases. Use MongoDB collections and JSON documents instead."
        wrong_result = evaluate_submission(wrong_answer, q)
        self.assertLess(wrong_result["similarity_pct"], 40.0)

if __name__ == "__main__":
    unittest.main()
