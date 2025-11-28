import json
from typing import Dict, List
from pathlib import Path
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import re


class MCQValidator:
    def __init__(self, valid_chunk_ids, similarity_threshold=0.80):
      self.mcqs = set()
      self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
      self.similarity_threshold = similarity_threshold
      self.valid_chunk_ids = set(valid_chunk_ids)

    # -------------------------
    # 1. Uniqueness Check
    # -------------------------
    def is_unique(self, mcq):
        normalized = mcq.strip().lower()
        if normalized in self.mcqs:
            return False
        self.mcqs.add(normalized)
        return True

    # -------------------------
    # 2. Distractor Validation
    # -------------------------
    def validate_distractor(self, correct_answer, distractors):
        correct_emb = self.model.encode(correct_answer)

        for dist in distractors:
            if dist.strip().lower() == correct_answer.strip().lower():
                return False
            
            dist_emb = self.model.encode(dist)
            sim = cosine_similarity([correct_emb], [dist_emb])[0][0]

            if sim > self.similarity_threshold:
                return False

        return True

    # -------------------------
    # 3. Math Question Validation
    # -------------------------
    def safe_solve(self, expr):
        if not re.match(r"^[0-9+\-*/(). ]+$", expr):
            return None
        try:
            return eval(expr)
        except:
            return None

    def validate_math_question(self, question, user_answer):
        correct = self.safe_solve(question)
        return correct == user_answer

    # -------------------------
    # 4. Citation Check
    # -------------------------
    def check_citation(self, mcq_chunk_ids):
        """
        Citation validation using only chunk IDs:
        - Each MCQ must reference at least one valid chunk ID
        """
        for cid in mcq_chunk_ids:
            if cid in self.valid_chunk_ids:
                return True
        return False

    # -------------------------
    # 5. Unified Validation
    # -------------------------
    def validate_mcq(self, question: str, correct_answer: str,
                    distractors: List[str], mcq_chunk_ids: List[str],
                    math_question: str = None, user_answer = None) -> dict:

      unique_result = self.is_unique(question)
      distractor_result = self.validate_distractor(correct_answer, distractors)
      math_result = self.validate_math_question(math_question, user_answer) if math_question else None
      citation_result = self.check_citation(mcq_chunk_ids)

      # Overall validity
      overall_valid = all([unique_result, distractor_result, citation_result])
      if math_result is False:
          overall_valid = False

      return {
          "question": question,
          "unique": unique_result,
          "distractor_valid": distractor_result,
          "math_valid": math_result,
          "citation_valid": citation_result,
          "overall_valid": overall_valid
      }

    # -------------------------
    # Save Validation Report
    # -------------------------
    def save_validation_report(self, report: dict, output_path: Path):
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"\nSaved validation report to {output_path}")
