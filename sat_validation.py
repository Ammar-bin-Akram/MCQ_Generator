"""
Validation Suite for SAT MCQ Generation
- Validates question quality
- Checks SAT format compliance
- Ensures answer correctness
- Scores questions on multiple criteria
"""

import json
from typing import Dict, List, Tuple
from pathlib import Path
import re

class SATQuestionValidator:
    """Validates SAT-style MCQs for quality and format compliance"""
    
    def __init__(self):
        """Initialize validator with SAT standards"""
        self.validation_results = []
        
        # SAT Reading question types
        self.reading_question_types = [
            'main_idea', 'detail', 'inference', 'vocabulary', 
            'purpose', 'tone', 'structure', 'evidence'
        ]
        
        # SAT Writing question types
        self.writing_question_types = [
            'grammar', 'punctuation', 'style', 'organization',
            'transitions', 'precision', 'concision'
        ]
        
        # Minimum quality thresholds
        self.min_question_length = 10  # words
        self.min_option_length = 1     # words
        self.max_option_length = 100   # words
        
    def validate_structure(self, mcq: Dict) -> Tuple[bool, List[str]]:
        """
        Validate basic MCQ structure
        
        Returns:
            (is_valid, list_of_issues)
        """
        issues = []
        
        # Required fields
        required_fields = ['question', 'options', 'correct_answer', 
                          'explanation', 'section']
        for field in required_fields:
            if field not in mcq:
                issues.append(f"Missing required field: '{field}'")
        
        # Check options structure
        if 'options' in mcq:
            if not isinstance(mcq['options'], dict):
                issues.append("'options' must be a dictionary")
            else:
                expected_keys = ['A', 'B', 'C', 'D']
                if set(mcq['options'].keys()) != set(expected_keys):
                    issues.append(f"Options must have exactly keys A, B, C, D. Found: {list(mcq['options'].keys())}")
        
        # Check correct answer
        if 'correct_answer' in mcq and 'options' in mcq:
            if mcq['correct_answer'] not in mcq['options']:
                issues.append(f"Correct answer '{mcq['correct_answer']}' not in options")
        
        # Check section type
        if 'section' in mcq:
            if mcq['section'] not in ['reading', 'writing']:
                issues.append(f"Invalid section: '{mcq['section']}'. Must be 'reading' or 'writing'")
        
        return (len(issues) == 0, issues)
    
    def validate_question_quality(self, mcq: Dict) -> Tuple[int, List[str]]:
        """
        Score question quality (0-100)
        
        Returns:
            (quality_score, feedback_list)
        """
        score = 100
        feedback = []
        
        question = mcq.get('question', '')
        options = mcq.get('options', {})
        
        # 1. Question length check
        question_words = len(question.split())
        if question_words < self.min_question_length:
            score -= 15
            feedback.append(f"Question too short ({question_words} words). Should be at least {self.min_question_length}")
        
        # 2. Question clarity (no vague words)
        vague_words = ['thing', 'stuff', 'very', 'really', 'somewhat']
        if any(word in question.lower() for word in vague_words):
            score -= 10
            feedback.append("Question contains vague language")
        
        # 3. Options quality
        option_lengths = []
        for key, option in options.items():
            opt_words = len(option.split())
            option_lengths.append(opt_words)
            
            if opt_words < self.min_option_length:
                score -= 10
                feedback.append(f"Option {key} too short ({opt_words} words)")
            
            if opt_words > self.max_option_length:
                score -= 5
                feedback.append(f"Option {key} too long ({opt_words} words)")
        
        # 4. Options should have similar lengths (avoid obvious answers)
        if option_lengths:
            avg_length = sum(option_lengths) / len(option_lengths)
            for i, length in enumerate(option_lengths):
                if abs(length - avg_length) > avg_length * 0.5:  # 50% deviation
                    score -= 5
                    feedback.append(f"Option {chr(65+i)} length significantly different from others")
        
        # 5. No duplicate options
        option_values = list(options.values())
        if len(option_values) != len(set(option_values)):
            score -= 20
            feedback.append("Duplicate options found")
        
        # 6. Explanation quality
        explanation = mcq.get('explanation', '')
        if len(explanation.split()) < 15:
            score -= 10
            feedback.append("Explanation too brief (should be detailed)")
        
        # Keep score in range [0, 100]
        score = max(0, min(100, score))
        
        if score == 100:
            feedback.append("✅ Excellent question quality!")
        
        return (score, feedback)
    
    def validate_sat_compliance(self, mcq: Dict) -> Tuple[bool, List[str]]:
        """
        Check SAT-specific format compliance
        
        Returns:
            (is_compliant, list_of_issues)
        """
        issues = []
        section = mcq.get('section', '')
        
        if section == 'reading':
            # Reading-specific checks
            question_type = mcq.get('question_type', '')
            if question_type not in self.reading_question_types:
                issues.append(f"Invalid reading question type: '{question_type}'")
            
            # Should reference passage
            question = mcq.get('question', '').lower()
            if 'passage' not in question and 'author' not in question and 'text' not in question:
                issues.append("Reading question should reference the passage")
            
            # Check if passage is provided
            if 'passage_content' not in mcq and 'passage_id' not in mcq:
                issues.append("Missing passage reference")
        
        elif section == 'writing':
            # Writing-specific checks
            question_type = mcq.get('question_type', '')
            if question_type not in self.writing_question_types:
                issues.append(f"Invalid writing question type: '{question_type}'")
            
            # Option A often "NO CHANGE" in SAT Writing
            options = mcq.get('options', {})
            if 'A' in options and options['A'].upper() != "NO CHANGE":
                issues.append("SAT Writing questions typically have 'NO CHANGE' as option A")
            
            # Should have underlined text
            if 'underlined_text' not in mcq:
                issues.append("Writing question should specify underlined text")
        
        # Difficulty check
        difficulty = mcq.get('difficulty', '')
        if difficulty not in ['easy', 'medium', 'hard']:
            issues.append(f"Invalid difficulty: '{difficulty}'")
        
        return (len(issues) == 0, issues)
    
    def validate_answer_correctness(self, mcq: Dict) -> Tuple[bool, List[str]]:
        """
        Validate that the marked correct answer makes sense
        (This is a heuristic check - manual review still needed)
        
        Returns:
            (seems_correct, warnings)
        """
        warnings = []
        correct = mcq.get('correct_answer', '')
        options = mcq.get('options', {})
        explanation = mcq.get('explanation', '').lower()
        
        # Check if explanation mentions the correct answer
        if correct.lower() not in explanation:
            warnings.append(f"Explanation doesn't mention correct answer '{correct}'")
        
        # Check if correct answer option is substantially different
        if correct in options:
            correct_option = options[correct].lower()
            
            # Heuristic: correct answers in SAT are often more specific
            if len(correct_option.split()) < 3:
                warnings.append("Correct answer seems too brief")
        
        # Warning if multiple similar options
        option_values = [v.lower() for v in options.values()]
        similarities = []
        for i, opt1 in enumerate(option_values):
            for j, opt2 in enumerate(option_values[i+1:], i+1):
                # Simple similarity: common words
                words1 = set(opt1.split())
                words2 = set(opt2.split())
                if len(words1 & words2) / max(len(words1), len(words2)) > 0.7:
                    similarities.append((chr(65+i), chr(65+j)))
        
        if similarities:
            warnings.append(f"Options very similar: {similarities}")
        
        return (len(warnings) == 0, warnings)
    
    def validate_mcq(self, mcq: Dict) -> Dict:
        """
        Full validation of a single MCQ
        
        Returns:
            Validation report
        """
        report = {
            'mcq_id': mcq.get('passage_id', 'unknown'),
            'section': mcq.get('section', 'unknown'),
            'overall_valid': True,
            'checks': {}
        }
        
        # 1. Structure validation
        struct_valid, struct_issues = self.validate_structure(mcq)
        report['checks']['structure'] = {
            'valid': struct_valid,
            'issues': struct_issues
        }
        if not struct_valid:
            report['overall_valid'] = False
        
        # 2. Quality scoring
        quality_score, quality_feedback = self.validate_question_quality(mcq)
        report['checks']['quality'] = {
            'score': quality_score,
            'feedback': quality_feedback,
            'passed': quality_score >= 70  # 70% threshold
        }
        if quality_score < 70:
            report['overall_valid'] = False
        
        # 3. SAT compliance
        sat_compliant, sat_issues = self.validate_sat_compliance(mcq)
        report['checks']['sat_compliance'] = {
            'compliant': sat_compliant,
            'issues': sat_issues
        }
        if not sat_compliant:
            report['overall_valid'] = False
        
        # 4. Answer correctness
        answer_valid, answer_warnings = self.validate_answer_correctness(mcq)
        report['checks']['answer'] = {
            'seems_correct': answer_valid,
            'warnings': answer_warnings
        }
        
        return report
    
    def validate_batch(self, mcqs: List[Dict]) -> Dict:
        """
        Validate multiple MCQs
        
        Returns:
            Batch validation report with statistics
        """
        print(f"\n{'='*70}")
        print("VALIDATING SAT MCQs")
        print(f"{'='*70}")
        
        reports = []
        for i, mcq in enumerate(mcqs, 1):
            print(f"\n📋 Validating MCQ {i}/{len(mcqs)}...")
            report = self.validate_mcq(mcq)
            reports.append(report)
            
            # Print summary
            status = "✅ PASS" if report['overall_valid'] else "❌ FAIL"
            print(f"   {status}")
            print(f"   Quality Score: {report['checks']['quality']['score']}/100")
        
        # Calculate statistics
        valid_count = sum(1 for r in reports if r['overall_valid'])
        avg_quality = sum(r['checks']['quality']['score'] for r in reports) / len(reports)
        
        batch_report = {
            'total_mcqs': len(mcqs),
            'valid_mcqs': valid_count,
            'invalid_mcqs': len(mcqs) - valid_count,
            'pass_rate': (valid_count / len(mcqs)) * 100,
            'average_quality_score': round(avg_quality, 2),
            'individual_reports': reports
        }
        
        # Print summary
        print(f"\n{'='*70}")
        print("VALIDATION SUMMARY")
        print(f"{'='*70}")
        print(f"Total MCQs: {batch_report['total_mcqs']}")
        print(f"Valid: {batch_report['valid_mcqs']} ({batch_report['pass_rate']:.1f}%)")
        print(f"Invalid: {batch_report['invalid_mcqs']}")
        print(f"Average Quality Score: {batch_report['average_quality_score']}/100")
        print(f"{'='*70}")
        
        return batch_report
    
    def save_validation_report(self, report: Dict, output_path: Path):
        """Save validation report to JSON"""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"\n💾 Validation report saved to {output_path}")


def validate_mcq_file(input_file: str, output_file: str = None):
    """
    Validate MCQs from a JSON file
    
    Args:
        input_file: Path to MCQ JSON file
        output_file: Path to save validation report (optional)
    """
    # Load MCQs
    with open(input_file, 'r', encoding='utf-8') as f:
        mcqs = json.load(f)
    
    # Validate
    validator = SATQuestionValidator()
    report = validator.validate_batch(mcqs)
    
    # Save report
    if output_file:
        validator.save_validation_report(report, Path(output_file))
    
    return report


if __name__ == "__main__":
    # Example: Validate existing MCQs
    mcq_file = Path("mcq_output/sat/sample_sat_mcqs.json")
    
    if mcq_file.exists():
        validate_mcq_file(
            str(mcq_file),
            "mcq_output/sat/sat_validation_report.json"
        )
    else:
        print(f"❌ MCQ file not found: {mcq_file}")
        print("Generate MCQs first using generate_sat_mcqs.py")