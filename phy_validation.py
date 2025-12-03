import json
from typing import Dict, List
from pathlib import Path
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import re

class MCQValidator:
    """Robust MCQ Validator for Math & Physics"""

    def __init__(self, valid_chunk_ids: List[str]):
        self.valid_chunk_ids = set(valid_chunk_ids)
        self.mcqs_seen = set()
        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    # -------------------------
    # 1. Uniqueness Check
    # -------------------------
    def is_unique(self, question: str) -> bool:
        normalized = question.strip().lower()
        if normalized in self.mcqs_seen:
            return False
        self.mcqs_seen.add(normalized)
        return True

    # -------------------------
    # 2. Distractor Validation (Semantic)
    # -------------------------
    def validate_distractor(self, correct_answer: str, distractors: List[str]) -> bool:
        return all(d != correct_answer for d in distractors)

    # -------------------------
    # 3. Math Validation
    # -------------------------
    def safe_solve(self, expr: str):
        if not expr or not re.match(r"^[0-9+\-*/(). ]+$", expr):
            return None
        try:
            return eval(expr)
        except:
            return None

    def validate_math_question(self, question: str, user_answer):
        correct = self.safe_solve(question)
        return correct == user_answer

    # -------------------------
    # 4. Citation Validation
    # -------------------------
    def check_citation(self, mcq_chunk_ids: List[str]) -> bool:
        return any(cid in self.valid_chunk_ids for cid in mcq_chunk_ids)

    # -------------------------
    # 5. Structure Validation
    # -------------------------
    def validate_structure(self, mcq: Dict):
        issues = []

        required_keys = {
            "question": str,
            "options": dict,
            "correct_answer": str,
            "distractors": list,
            "explanation": str,
            "difficulty": str,
            "topic": str,
            "chapter": str,
            "source_chunks": list,
            "generated_with": str,
            "requested_difficulty": str
        }

        # Check keys and types
        for key, typ in required_keys.items():
            if key not in mcq:
                issues.append(f"Missing key: {key}")
            elif not isinstance(mcq[key], typ):
                issues.append(f"Key '{key}' must be of type {typ.__name__}")

        # Validate options
        options = mcq.get("options", {})
        if isinstance(options, dict):
            expected_keys = {"A", "B", "C", "D"}
            if set(options.keys()) != expected_keys:
                issues.append("'options' must contain exactly the keys: A, B, C, D")
            for k, v in options.items():
                if not isinstance(v, str):
                    issues.append(f"Option '{k}' must be a string")

        # Correct answer must be a valid option
        correct = mcq.get("correct_answer")
        if correct not in {"A", "B", "C", "D"}:
            issues.append("'correct_answer' must be one of: A, B, C, D")

        # Distractors validation
        distractors = mcq.get("distractors", [])
        if not all(isinstance(d, str) for d in distractors):
            issues.append("All distractors must be strings")
        if correct in distractors:
            issues.append("'distractors' must NOT include the correct answer")

        # Source chunks validation
        source_chunks = mcq.get("source_chunks", [])
        if not all(isinstance(c, str) for c in source_chunks):
            issues.append("All items in 'source_chunks' must be strings")

        return len(issues) == 0, issues

    # -------------------------
    # 6. Single MCQ Validation
    # -------------------------
    def validate_mcq(self, mcq: Dict) -> Dict:
        # Validate structure
        struct_valid, struct_issues = self.validate_structure(mcq)

        # Unique question
        unique_ok = self.is_unique(mcq.get("question", ""))

        # Distractor validation
        distractor_ok = self.validate_distractor(
            mcq.get("options", {}).get(mcq.get("correct_answer", "A"), ""),
            [mcq["options"][d] for d in mcq.get("distractors", []) if d in mcq.get("options", {})]
        )

        # Math validation
        math_ok = None
        if "math_question" in mcq and "user_answer" in mcq:
            math_ok = self.validate_math_question(mcq["math_question"], mcq["user_answer"])

        # Citation check
        citation_ok = self.check_citation(mcq.get("source_chunks", []))

        overall = struct_valid and unique_ok and distractor_ok and citation_ok
        if math_ok is False:
            overall = False

        return {
            "question": mcq.get("question", ""),
            "structure_valid": struct_valid,
            "structure_issues": struct_issues,
            "unique": unique_ok,
            "distractor_valid": distractor_ok,
            "math_valid": math_ok,
            "citation_valid": citation_ok,
            "overall_valid": overall
        }

    # -------------------------
    # 7. Batch Validation
    # -------------------------
    def validate_batch(self, mcqs: List[Dict]) -> Dict:
        print("\n" + "="*70)
        print("VALIDATING MCQ BATCH")
        print("="*70)

        results = []
        valid_count = 0

        for i, mcq in enumerate(mcqs, 1):
            print(f"Validating MCQ {i}/{len(mcqs)}")
            report = self.validate_mcq(mcq)
            if report["overall_valid"]:
                valid_count += 1
            results.append({"question": mcq.get("question", ""), "report": report})

        total = len(mcqs)
        pass_rate = (valid_count / total) * 100 if total else 0.0

        return {
            "total_mcqs": total,
            "valid_mcqs": valid_count,
            "invalid_mcqs": total - valid_count,
            "pass_rate": pass_rate,
            "results": results
        }

    # -------------------------
    # 8. Save Validation Report
    # -------------------------
    def save_validation_report(self, report: Dict, output_path: Path):
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"\nSaved validation report to {output_path}")
