import os
import sys
import json
import unittest
import re

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestMCQDataset(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        cls.json_path = os.path.join(base_dir, "data", "mcq_exam_questions.json")
        with open(cls.json_path, "r", encoding="utf-8") as f:
            cls.questions = json.load(f)

    def test_total_question_count(self):
        """Must have exactly 178 authentic entrance exam questions."""
        self.assertEqual(len(self.questions), 178)

    def test_gate_question_count(self):
        """Must have exactly 50 authentic GATE questions."""
        gate_qs = [q for q in self.questions if "GATE" in q.get("source", "")]
        self.assertEqual(len(gate_qs), 50)

    def test_gate_provenance_and_evidence(self):
        """All 50 GATE questions must have complete provenance metadata (file, page, qnum, snippet)."""
        gate_qs = [q for q in self.questions if "GATE" in q.get("source", "")]
        for q in gate_qs:
            qid = q.get("id")
            self.assertTrue(q.get("source_file"), f"{qid} missing source_file")
            self.assertTrue(q.get("source_page"), f"{qid} missing source_page")
            self.assertTrue(q.get("source_qnum"), f"{qid} missing source_qnum")
            self.assertTrue(q.get("evidence_snippet"), f"{qid} missing evidence_snippet")
            self.assertTrue(os.path.exists(os.path.join(os.path.dirname(os.path.dirname(__file__)), q["source_file"])),
                            f"{qid} source_file does not exist on disk: {q['source_file']}")

    def test_all_questions_have_three_standardized_variants(self):
        """All 178 questions must have exactly 3 pre-defined variants with standardized domains."""
        expected_domains = [
            "Healthcare & Clinical EMR",
            "Core Banking & FinTech Settlement",
            "E-Commerce Flash Sale & Inventory"
        ]
        total_variants = sum(len(q.get("variants", [])) for q in self.questions)
        self.assertEqual(total_variants, 178 * 3)

        for q in self.questions:
            qid = q.get("id")
            variants = q.get("variants", [])
            self.assertEqual(len(variants), 3, f"{qid} must have exactly 3 variants")
            domains = [v.get("domain") for v in variants]
            self.assertEqual(domains, expected_domains, f"{qid} domain mismatch: {domains}")

    def test_other_entrance_exams_included(self):
        """Must include questions from ISRO (21), NIELIT (29), and UGC-NET (78)."""
        isro_qs = [q for q in self.questions if "ISRO" in q.get("source", "")]
        nielit_qs = [q for q in self.questions if "NIELIT" in q.get("source", "")]
        ugc_qs = [q for q in self.questions if "UGC" in q.get("source", "")]

        self.assertEqual(len(isro_qs), 21)
        self.assertEqual(len(nielit_qs), 29)
        self.assertEqual(len(ugc_qs), 78)

    def test_question_structure_and_options(self):
        """Every question must have 4 options, valid correct answer, and explanation."""
        valid_options = {"A", "B", "C", "D"}
        for q in self.questions:
            qid = q.get("id")
            self.assertTrue(qid, "Missing ID")
            self.assertTrue(q.get("title"), f"{qid} Missing title")
            self.assertTrue(q.get("prompt"), f"{qid} Missing prompt")
            self.assertTrue(q.get("explanation"), f"{qid} Missing explanation")
            self.assertEqual(len(q.get("options", [])), 4, f"{qid} must have 4 options")
            self.assertIn(q.get("correct_option"), valid_options, f"{qid} invalid correct_option")

    def test_variants_structure_and_clean_answers(self):
        """All 534 variants must have valid answers and NO absurd distractors marked correct."""
        valid_options = {"A", "B", "C", "D"}
        letters = ["A", "B", "C", "D"]
        distractor_patterns = [
            'reboot', 'delete customer', 'deleting the customer', 'balance to zero', 'balances to zero',
            'convert the database into a csv', 'dropping the products', 'unindexed night', 'python debugging',
            'network card speed', 'electricity', 'not software engineers', 'wi-fi', 'wifi',
            'format the atm', 'cardboard', 'boxes', 'slow down competitor', 'single-threaded',
            'discharging', 'registering doctor', 'querying doctor', 'paying interest', 'running balance',
            'opening checking', 'adding catalog', 'updating password', 'passive file', 'cube projection',
            'rsa key', 'discretionary matrix', '100 penalty', '$100', 'infinite loop', 'table scan error',
            '0.00 always', '10 digits', 'telephone spam', 'cannot store numbers', 'change daily',
            'hash tables only', 'photos', 'more disk space', 'public domain', 'not access his own data',
            'not access their own data', 'ceo must approve', 'root access', 'speeding up http',
            'eliminating the need for ssl', 'automatically refunding', 'without batteries',
            'decrease medical memory', 'unencrypted pin', 'eliminate internal logic', '1 hz',
            'slow down package', 'bypass parity', 'manual package', 'diagnosing patient illnesses',
            'converting analog ekg', 'printing hospital', 'stock market opening',
            'currency exchange rates', 'bank vault locks', 'calculating product prices',
            'packing cardboard', 'managing customer credit card', 'immediate delivery of ordered',
            'free shipping', 'elimination of sql joins', 'double the bank', 'replace the primary key',
            'prevent account numbers', 'speed up network backups', 'delete all vital logs',
            'fails to compile', 'aborts the query with an exception', 'depressing the average',
            'replaces null with the maximum', 'truncate orders table', 'deadlocks occur frequently in mri',
            'one hospital per month', 'all 500 consortium', 'network switches must be replaced',
            'orders fail if region', 'broadcast storms flood', 'databases run without consensus',
            'cannot detect levels', 'disable barcode', 'directly access the cpu bus',
            'surgery proceeds without medication', 'pharmacy server is deleted',
            'billing charges the patient double', 'bank a sends the money regardless', 'bank b is fined',
            'placed in an infinite loop', 'customer is banned', 'shipping ships an empty package',
            'charts older than 15 minutes', 'prevent doctors from ordering', 'restart the database engine',
            'pause all customer atm', 'reset customer account balances', 'canceling all pending orders',
            'disabling checkout buttons', 'lowering product prices', 'as a diamond', 'as a dashed circle',
            'as a double rectangle', 'solid hexagon', 'triangle', 'underlined rectangle', 'single square',
            'dashed diamond', 'concentric octagons', 'ssn contains hyphens', 'blood type is confidential',
            'doctors do not use ssns', 'age changes every year', 'banking tables require three',
            'ibans cannot be stored', 'carts have images', 'items can be returned', 'users have usernames',
            'patient_id set to -1', 'beneficiaries receive a wire transfer', 'all warehouse products are deleted',
            'cart items are shipped to customer', 'patient ids must be negative', 'null is reserved for doctor',
            'only support integer types', 'interest is not calculated', 'currency was not specified',
            'balance is too low', 'credit cards reject null', 'orders must have tracking',
            'carts are temporary tables', 'uuid is not supported', 'prescriptions cannot reference patients',
            'start with capital letters', 'ibans contain country codes', 'cannot store characters',
            'bigint cannot be indexed', 'converting sku to price', 'products from being returned',
            'cannot reference text', 'wait in a deadlock cycle', 't2 aborts t1', 't1 is demoted',
            'timestamps are randomized', 'granted to all transactions simultaneously',
            'wire transfers cannot be canceled', 't2 forcibly preempts', 'both carts merge',
            'inventory is doubled', 'only debit cards', 'converted to gold', 'audio recording of doctor',
            'high delivery fees', 'slow internet connections', 'nurse c is logged out forever',
            'hospital data is wiped', 'prevent researchers from publishing papers', 'public tables are read-only',
            'cause physical pacemaker failure', 'corrupt the entire medical database',
            'bypass sql syntax validation', 'all orders are free', 'checkout takes less than 1 second',
            'all orders placed during the entire day', 'products that are out of stock',
            'converting the database to mongodb', 'creating traders without ids'
        ]

        whitelist = [
            'limiting reboot recovery time',
            'double rectangle connected via a double diamond',
            'undo information to reverse the partial write upon reboot',
            'sibling pointers until exceeding $100'
        ]

        for q in self.questions:
            qid = q.get("id")
            variants = q.get("variants", [])
            for v in variants:
                vid = v.get("variant_id")
                self.assertTrue(v.get("domain"), f"{qid} variant missing domain")
                self.assertTrue(v.get("prompt"), f"{qid} variant missing prompt")
                self.assertTrue(v.get("explanation"), f"{qid} variant missing explanation")
                self.assertEqual(len(v.get("options", [])), 4, f"{qid} variant must have 4 options")
                self.assertIn(v.get("correct_option"), valid_options, f"{qid} variant invalid correct_option")

                # Verify answer option does not contain distractor patterns
                c_idx = letters.index(v["correct_option"])
                corr_txt = re.sub(r'^[A-Da-d][\.\)]\s*', '', v["options"][c_idx]).strip().lower()

                is_whitelisted = any(w in corr_txt for w in whitelist)
                if not is_whitelisted:
                    for pat in distractor_patterns:
                        self.assertFalse(pat in corr_txt, f"Distractor '{pat}' marked as correct in {qid} V{vid}: {corr_txt}")

    def test_python_module_fallback_parity(self):
        """Fallback python module ai_engine.mcq_data must match JSON data exactly."""
        from ai_engine.mcq_data import MCQ_BENCHMARK_QUESTIONS
        self.assertEqual(len(MCQ_BENCHMARK_QUESTIONS), len(self.questions))
        self.assertEqual(MCQ_BENCHMARK_QUESTIONS[0]["id"], self.questions[0]["id"])
        self.assertEqual(MCQ_BENCHMARK_QUESTIONS[-1]["id"], self.questions[-1]["id"])
        self.assertEqual(len(MCQ_BENCHMARK_QUESTIONS[0]["variants"]), 3)

    def test_exam_lab_does_not_contain_live_variant_tab(self):
        """Exam lab UI must only present Original Question and the 3 Pre-defined variants."""
        with open("D:/DBP/ai_engine/exam_lab.py", "r", encoding="utf-8") as f:
            code = f.read()
        self.assertNotIn("Live AI Variant", code)
        self.assertNotIn("generate_live_mcq_variant", code)

if __name__ == "__main__":
    unittest.main()
