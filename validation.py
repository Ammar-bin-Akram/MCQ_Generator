"""
Validation Suite for Curriculum MCQs (Math & Physics)
"""

import json
from typing import Dict, List, Tuple
from pathlib import Path
import re

class CurriculumMCQValidator:
    """Validates FSc Math & Physics MCQs"""
    
    def __init__(self):
        """Initialize validator"""
        self.validation_results = []
        
        # FSc subjects
        self.valid_subjects = ['physics', 'math', 'mathematics']
        
        # Difficulty levels
        self.valid_difficulties = ['easy', 'medium', 'hard']
        
        # Quality thresholds
        self.min_question_length = 8   # words
        self.min_option_length = 2     # words
        self.max_option_length = 150   # words
    
    def validate_structure(self, mcq: Dict) -> Tuple[bool, List[str]]:
        """Validate basic MCQ structure"""
        issues = []
        
        # Required fields
        required_fields = ['question', 'options', 'correct_answer', 'explanation']
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
                    issues.append(f"Options must have keys A, B, C, D")
        
        # Check correct answer
        if 'correct_answer' in mcq and 'options' in mcq:
            if mcq['correct_answer'] not in mcq['options']:
                issues.append(f"Correct answer '{mcq['correct_answer']}' not in options")
        
        return (len(issues) == 0, issues)
    
    def validate_question_quality(self, mcq: Dict) -> Tuple[int, List[str]]:
        """Score question quality (0-100)"""
        score = 100
        feedback = []
        
        question = mcq.get('question', '')
        options = mcq.get('options', {})
        
        # Question length
        question_words = len(question.split())
        if question_words < self.min_question_length:
            score -= 15
            feedback.append(f"Question too short ({question_words} words)")
        
        # No duplicate options
        option_values = list(options.values())
        if len(option_values) != len(set(option_values)):
            score -= 25
            feedback.append("Duplicate options found")
        
        # Options length consistency
        option_lengths = [len(opt.split()) for opt in options.values()]
        if option_lengths:
            avg_length = sum(option_lengths) / len(option_lengths)
            for i, length in enumerate(option_lengths):
                if length < self.min_option_length:
                    score -= 10
                    feedback.append(f"Option {chr(65+i)} too short")
                
                # Check for length outliers
                if abs(length - avg_length) > avg_length * 0.6:
                    score -= 5
                    feedback.append(f"Option {chr(65+i)} length inconsistent")
        
        # Explanation quality
        explanation = mcq.get('explanation', '')
        if len(explanation.split()) < 10:
            score -= 15
            feedback.append("Explanation too brief")
        
        # Check if explanation mentions correct answer
        correct = mcq.get('correct_answer', '')
        if correct and correct not in explanation:
            score -= 10
            feedback.append("Explanation doesn't reference correct answer")
        
        score = max(0, min(100, score))
        
        if score >= 90:
            feedback.append("Excellent quality!")
        
        return (score, feedback)
    
    def validate_curriculum_compliance(self, mcq: Dict) -> Tuple[bool, List[str]]:
        """Check FSc curriculum compliance"""
        issues = []
        
        # Difficulty check
        difficulty = mcq.get('difficulty', '').lower()
        if difficulty not in self.valid_difficulties:
            issues.append(f"Invalid difficulty: '{difficulty}'")
        
        # Topic should be present
        topic = mcq.get('topic', '')
        if not topic or len(topic.strip()) < 3:
            issues.append("Topic missing or too short")
        
        # Source chunks should exist (for RAG validation)
        source_chunks = mcq.get('source_chunks', [])
        if not source_chunks:
            issues.append("No source chunks referenced (RAG traceability missing)")
        
        return (len(issues) == 0, issues)
    
    def validate_mcq(self, mcq: Dict) -> Dict:
        """Full validation of a single MCQ"""
        report = {
            'topic': mcq.get('topic', 'unknown'),
            'difficulty': mcq.get('difficulty', 'unknown'),
            'overall_valid': True,
            'checks': {}
        }
        
        # Structure validation
        struct_valid, struct_issues = self.validate_structure(mcq)
        report['checks']['structure'] = {
            'valid': struct_valid,
            'issues': struct_issues
        }
        if not struct_valid:
            report['overall_valid'] = False
        
        # Quality scoring
        quality_score, quality_feedback = self.validate_question_quality(mcq)
        report['checks']['quality'] = {
            'score': quality_score,
            'feedback': quality_feedback,
            'passed': quality_score >= 70
        }
        if quality_score < 70:
            report['overall_valid'] = False
        
        # Curriculum compliance
        curriculum_compliant, curriculum_issues = self.validate_curriculum_compliance(mcq)
        report['checks']['curriculum'] = {
            'compliant': curriculum_compliant,
            'issues': curriculum_issues
        }
        if not curriculum_compliant:
            report['overall_valid'] = False
        
        # Difficulty assignment validation
        difficulty_valid, difficulty_issues = self.validate_difficulty_assignment(mcq)
        report['checks']['difficulty_assignment'] = {
            'valid': difficulty_valid,
            'issues': difficulty_issues
        }
        
        return report
    
    def validate_difficulty_assignment(self, mcq: Dict) -> Tuple[bool, List[str]]:
        """
        Validate that difficulty is properly assigned
        
        Returns:
            (is_valid, issues)
        """
        issues = []
        
        difficulty = mcq.get('difficulty', '')
        requested = mcq.get('requested_difficulty', '')
        
        # Check if difficulty exists
        if not difficulty:
            issues.append("Missing 'difficulty' field")
            return (False, issues)
        
        # Check if valid value
        if difficulty not in ['easy', 'medium', 'hard']:
            issues.append(f"Invalid difficulty value: '{difficulty}'")
            return (False, issues)
        
        # If there's a mismatch, it's actually GOOD (means auto-calculation worked)
        if requested and difficulty != requested:
            issues.append(f"ℹ️  Auto-adjusted from '{requested}' to '{difficulty}' based on content")
        
        return (True, issues)
    
    def validate_batch(self, mcqs: List[Dict]) -> Dict:
        """Validate multiple MCQs"""
        print(f"\n{'='*70}")
        print("VALIDATING CURRICULUM MCQs")
        print(f"{'='*70}")
        
        reports = []
        for i, mcq in enumerate(mcqs, 1):
            print(f"\nValidating MCQ {i}/{len(mcqs)}...")
            report = self.validate_mcq(mcq)
            reports.append(report)
            
            status = "PASS" if report['overall_valid'] else "FAIL"
            print(f"   {status} - Quality: {report['checks']['quality']['score']}/100")
        
        # Statistics
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
        
        print(f"\n{'='*70}")
        print("VALIDATION SUMMARY")
        print(f"{'='*70}")
        print(f"Total: {batch_report['total_mcqs']}")
        print(f"Valid: {batch_report['valid_mcqs']} ({batch_report['pass_rate']:.1f}%)")
        print(f"Invalid: {batch_report['invalid_mcqs']}")
        print(f"Avg Quality: {batch_report['average_quality_score']}/100")
        print(f"{'='*70}")
        
        return batch_report
    
    def save_validation_report(self, report: Dict, output_path: Path):
        """Save validation report"""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"\nValidation report saved to {output_path}")