"""
Pilot Metrics for MCQ Quality Assessment
Calculates:
1. P-value (Difficulty Index) - Percentage of students who answer correctly
2. Discrimination Index - How well the question differentiates between high and low performers
3. Coverage - Content coverage across curriculum topics
"""

import json
import numpy as np
from typing import Dict, List, Tuple
from pathlib import Path
from collections import defaultdict, Counter
import statistics


class PilotMetrics:
    """
    Calculate pilot metrics for MCQ quality assessment
    """
    
    def __init__(self):
        """Initialize pilot metrics calculator"""
        self.results = []
        
    # ========================================
    # 1. P-VALUE (DIFFICULTY INDEX)
    # ========================================
    
    def calculate_p_value(self, correct_responses: int, total_responses: int) -> Dict:
        """
        Calculate p-value (difficulty index)
        
        P-value = (Number of correct responses) / (Total number of responses)
        
        Interpretation:
        - P > 0.75: Easy question
        - 0.25 <= P <= 0.75: Moderate difficulty
        - P < 0.25: Hard question
        
        Args:
            correct_responses: Number of students who answered correctly
            total_responses: Total number of students who attempted
            
        Returns:
            Dictionary with p-value and interpretation
        """
        if total_responses == 0:
            return {
                'p_value': None,
                'difficulty_level': 'unknown',
                'interpretation': 'No responses recorded',
                'valid': False
            }
        
        p_value = correct_responses / total_responses
        
        # Determine difficulty level
        if p_value > 0.75:
            difficulty = 'easy'
            interpretation = 'Easy - Most students answered correctly'
        elif p_value >= 0.25:
            difficulty = 'moderate'
            interpretation = 'Moderate - Good difficulty balance'
        else:
            difficulty = 'hard'
            interpretation = 'Hard - Few students answered correctly'
        
        # Ideal range for good MCQs is 0.30 to 0.70
        is_optimal = 0.30 <= p_value <= 0.70
        
        return {
            'p_value': round(p_value, 3),
            'difficulty_level': difficulty,
            'interpretation': interpretation,
            'is_optimal': is_optimal,
            'optimal_range': '0.30 - 0.70',
            'valid': True,
            'correct_responses': correct_responses,
            'total_responses': total_responses
        }
    
    # ========================================
    # 2. DISCRIMINATION INDEX
    # ========================================
    
    def calculate_discrimination_index(self, 
                                       upper_group_correct: int,
                                       upper_group_total: int,
                                       lower_group_correct: int,
                                       lower_group_total: int) -> Dict:
        """
        Calculate discrimination index
        
        Discrimination Index (D) = P_upper - P_lower
        where:
        - P_upper = proportion of upper group answering correctly
        - P_lower = proportion of lower group answering correctly
        
        Upper group: Top 27% of students by total score
        Lower group: Bottom 27% of students by total score
        
        Interpretation:
        - D >= 0.40: Excellent discrimination
        - 0.30 <= D < 0.40: Good discrimination
        - 0.20 <= D < 0.30: Acceptable, needs improvement
        - D < 0.20: Poor discrimination, reject or revise
        - D < 0: Negative discrimination (item is flawed)
        
        Args:
            upper_group_correct: Number in upper group answering correctly
            upper_group_total: Total in upper group
            lower_group_correct: Number in lower group answering correctly
            lower_group_total: Total in lower group
            
        Returns:
            Dictionary with discrimination index and interpretation
        """
        if upper_group_total == 0 or lower_group_total == 0:
            return {
                'discrimination_index': None,
                'quality': 'unknown',
                'interpretation': 'Insufficient data for discrimination analysis',
                'valid': False
            }
        
        p_upper = upper_group_correct / upper_group_total
        p_lower = lower_group_correct / lower_group_total
        
        discrimination = p_upper - p_lower
        
        # Determine quality
        if discrimination >= 0.40:
            quality = 'excellent'
            interpretation = 'Excellent - Strong differentiation between high/low performers'
            action = 'Retain item'
        elif discrimination >= 0.30:
            quality = 'good'
            interpretation = 'Good - Adequate differentiation'
            action = 'Retain item'
        elif discrimination >= 0.20:
            quality = 'acceptable'
            interpretation = 'Acceptable - Marginal differentiation, consider revision'
            action = 'Consider revision'
        elif discrimination >= 0:
            quality = 'poor'
            interpretation = 'Poor - Weak differentiation, needs revision'
            action = 'Revise or reject'
        else:
            quality = 'negative'
            interpretation = 'Negative - Item is flawed (low performers do better)'
            action = 'Reject item immediately'
        
        return {
            'discrimination_index': round(discrimination, 3),
            'p_upper': round(p_upper, 3),
            'p_lower': round(p_lower, 3),
            'quality': quality,
            'interpretation': interpretation,
            'action': action,
            'valid': True,
            'upper_group': {'correct': upper_group_correct, 'total': upper_group_total},
            'lower_group': {'correct': lower_group_correct, 'total': lower_group_total}
        }
    
    def calculate_discrimination_from_responses(self, 
                                               student_scores: List[int],
                                               question_responses: List[bool]) -> Dict:
        """
        Calculate discrimination index from raw student data
        
        Args:
            student_scores: List of total scores for each student
            question_responses: List of True/False for this question (True = correct)
            
        Returns:
            Discrimination index result
        """
        if len(student_scores) != len(question_responses):
            return {
                'discrimination_index': None,
                'quality': 'unknown',
                'interpretation': 'Mismatched data',
                'valid': False
            }
        
        # Combine scores and responses
        data = list(zip(student_scores, question_responses))
        data.sort(reverse=True)  # Sort by score (highest first)
        
        n = len(data)
        # Use top and bottom 27% of students
        group_size = max(1, int(n * 0.27))
        
        # Upper group (high performers)
        upper_group = data[:group_size]
        upper_correct = sum(1 for _, correct in upper_group if correct)
        upper_total = len(upper_group)
        
        # Lower group (low performers)
        lower_group = data[-group_size:]
        lower_correct = sum(1 for _, correct in lower_group if correct)
        lower_total = len(lower_group)
        
        return self.calculate_discrimination_index(
            upper_correct, upper_total,
            lower_correct, lower_total
        )
    
    # ========================================
    # 3. COVERAGE ANALYSIS
    # ========================================
    
    def calculate_coverage(self, 
                          mcqs: List[Dict],
                          curriculum_topics: List[str] = None) -> Dict:
        """
        Calculate content coverage across curriculum
        
        Measures:
        - Topic distribution
        - Difficulty distribution
        - Chapter coverage
        - Coverage completeness
        
        Args:
            mcqs: List of MCQ dictionaries
            curriculum_topics: Expected topics from curriculum (optional)
            
        Returns:
            Coverage analysis results
        """
        if not mcqs:
            return {
                'total_mcqs': 0,
                'coverage_score': 0,
                'valid': False
            }
        
        # Extract topics, difficulties, and chapters
        topics = []
        difficulties = []
        chapters = []
        
        for mcq in mcqs:
            if 'topic' in mcq and mcq['topic']:
                topics.append(mcq['topic'])
            if 'difficulty' in mcq and mcq['difficulty']:
                difficulties.append(mcq['difficulty'])
            if 'chapter' in mcq and mcq['chapter']:
                chapters.append(mcq['chapter'])
        
        # Topic coverage
        topic_counts = Counter(topics)
        unique_topics = len(topic_counts)
        
        # Difficulty distribution
        difficulty_counts = Counter(difficulties)
        difficulty_distribution = {
            'easy': difficulty_counts.get('easy', 0),
            'medium': difficulty_counts.get('medium', 0),
            'hard': difficulty_counts.get('hard', 0)
        }
        
        # Chapter coverage
        chapter_counts = Counter(chapters)
        unique_chapters = len(chapter_counts)
        
        # Calculate coverage score (0-100)
        coverage_score = 0
        
        # 1. Topic diversity (30 points)
        if curriculum_topics:
            topics_covered = len(set(topics) & set(curriculum_topics))
            topic_coverage_pct = (topics_covered / len(curriculum_topics)) * 100
            coverage_score += (topic_coverage_pct / 100) * 30
        else:
            # Without curriculum, reward diversity
            if unique_topics >= 10:
                coverage_score += 30
            elif unique_topics >= 5:
                coverage_score += 20
            else:
                coverage_score += 10
        
        # 2. Difficulty balance (40 points)
        total_mcqs = len(mcqs)
        ideal_distribution = {'easy': 0.3, 'medium': 0.5, 'hard': 0.2}
        
        difficulty_balance_score = 0
        for level, ideal_pct in ideal_distribution.items():
            actual_pct = difficulty_distribution[level] / total_mcqs
            deviation = abs(actual_pct - ideal_pct)
            level_score = max(0, 1 - (deviation / ideal_pct)) if ideal_pct > 0 else 0
            difficulty_balance_score += level_score
        
        coverage_score += (difficulty_balance_score / 3) * 40
        
        # 3. Chapter breadth (30 points)
        if unique_chapters >= 8:
            coverage_score += 30
        elif unique_chapters >= 5:
            coverage_score += 20
        elif unique_chapters >= 3:
            coverage_score += 15
        else:
            coverage_score += 5
        
        # Topic balance (check if any topic is over-represented)
        topic_balance = 'balanced'
        if topic_counts:
            max_topic_count = max(topic_counts.values())
            if max_topic_count > total_mcqs * 0.5:
                topic_balance = 'imbalanced - one topic dominates'
            elif max_topic_count > total_mcqs * 0.3:
                topic_balance = 'moderately balanced'
        
        return {
            'total_mcqs': total_mcqs,
            'coverage_score': round(coverage_score, 2),
            'topic_coverage': {
                'unique_topics': unique_topics,
                'topics': dict(topic_counts.most_common()),
                'balance': topic_balance
            },
            'difficulty_distribution': {
                'counts': difficulty_distribution,
                'percentages': {
                    level: round((count / total_mcqs) * 100, 1)
                    for level, count in difficulty_distribution.items()
                },
                'ideal_distribution': {
                    'easy': '30%',
                    'medium': '50%',
                    'hard': '20%'
                }
            },
            'chapter_coverage': {
                'unique_chapters': unique_chapters,
                'chapters': dict(chapter_counts.most_common())
            },
            'curriculum_coverage': {
                'expected_topics': len(curriculum_topics) if curriculum_topics else None,
                'topics_covered': len(set(topics) & set(curriculum_topics)) if curriculum_topics else None,
                'coverage_percentage': round((len(set(topics) & set(curriculum_topics)) / len(curriculum_topics)) * 100, 1) if curriculum_topics else None
            },
            'valid': True
        }
    
    # ========================================
    # COMPREHENSIVE ANALYSIS
    # ========================================
    
    def analyze_mcq_batch(self,
                         mcqs: List[Dict],
                         student_responses: List[Dict] = None,
                         curriculum_topics: List[str] = None) -> Dict:
        """
        Comprehensive pilot metrics analysis for a batch of MCQs
        
        Args:
            mcqs: List of MCQ dictionaries
            student_responses: Optional list of student response data
                Format: [{'mcq_id': 0, 'student_scores': [80, 75, ...], 'responses': [True, False, ...]}, ...]
            curriculum_topics: Expected curriculum topics
            
        Returns:
            Comprehensive metrics report
        """
        report = {
            'summary': {
                'total_mcqs': len(mcqs),
                'analyzed_date': '2025-11-29'
            },
            'coverage_analysis': None,
            'individual_mcq_metrics': []
        }
        
        # Coverage analysis (always available)
        coverage = self.calculate_coverage(mcqs, curriculum_topics)
        report['coverage_analysis'] = coverage
        
        # Individual MCQ analysis (if student responses available)
        if student_responses:
            for response_data in student_responses:
                mcq_id = response_data.get('mcq_id', 0)
                
                metrics = {
                    'mcq_id': mcq_id,
                    'question': mcqs[mcq_id].get('question', '')[:100] + '...' if len(mcqs[mcq_id].get('question', '')) > 100 else mcqs[mcq_id].get('question', ''),
                    'topic': mcqs[mcq_id].get('topic', 'unknown')
                }
                
                # P-value
                if 'correct_responses' in response_data and 'total_responses' in response_data:
                    p_value_result = self.calculate_p_value(
                        response_data['correct_responses'],
                        response_data['total_responses']
                    )
                    metrics['p_value'] = p_value_result
                
                # Discrimination
                if 'student_scores' in response_data and 'responses' in response_data:
                    discrimination_result = self.calculate_discrimination_from_responses(
                        response_data['student_scores'],
                        response_data['responses']
                    )
                    metrics['discrimination'] = discrimination_result
                
                report['individual_mcq_metrics'].append(metrics)
            
            # Calculate batch statistics
            valid_p_values = [m['p_value']['p_value'] for m in report['individual_mcq_metrics'] 
                            if 'p_value' in m and m['p_value']['valid']]
            valid_discriminations = [m['discrimination']['discrimination_index'] 
                                    for m in report['individual_mcq_metrics'] 
                                    if 'discrimination' in m and m['discrimination']['valid']]
            
            report['summary']['average_p_value'] = round(statistics.mean(valid_p_values), 3) if valid_p_values else None
            report['summary']['average_discrimination'] = round(statistics.mean(valid_discriminations), 3) if valid_discriminations else None
            
            # Quality distribution
            if valid_discriminations:
                excellent = sum(1 for d in valid_discriminations if d >= 0.40)
                good = sum(1 for d in valid_discriminations if 0.30 <= d < 0.40)
                acceptable = sum(1 for d in valid_discriminations if 0.20 <= d < 0.30)
                poor = sum(1 for d in valid_discriminations if 0 <= d < 0.20)
                negative = sum(1 for d in valid_discriminations if d < 0)
                
                report['summary']['quality_distribution'] = {
                    'excellent': excellent,
                    'good': good,
                    'acceptable': acceptable,
                    'poor': poor,
                    'negative': negative
                }
        
        return report
    
    def save_metrics_report(self, report: Dict, output_path: Path):
        """Save metrics report to JSON"""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"\n📊 Pilot metrics report saved to {output_path}")
    
    def print_report(self, report: Dict):
        """Print formatted metrics report"""
        print(f"\n{'='*70}")
        print("PILOT METRICS ANALYSIS REPORT")
        print(f"{'='*70}")
        
        summary = report['summary']
        print(f"\nTotal MCQs: {summary['total_mcqs']}")
        
        if 'average_p_value' in summary and summary['average_p_value']:
            print(f"Average P-value (Difficulty): {summary['average_p_value']}")
        
        if 'average_discrimination' in summary and summary['average_discrimination']:
            print(f"Average Discrimination Index: {summary['average_discrimination']}")
        
        # Coverage
        if report['coverage_analysis']:
            coverage = report['coverage_analysis']
            print(f"\n{'-'*70}")
            print("COVERAGE ANALYSIS")
            print(f"{'-'*70}")
            print(f"Coverage Score: {coverage['coverage_score']}/100")
            print(f"Unique Topics: {coverage['topic_coverage']['unique_topics']}")
            print(f"Unique Chapters: {coverage['chapter_coverage']['unique_chapters']}")
            print(f"\nDifficulty Distribution:")
            for level, pct in coverage['difficulty_distribution']['percentages'].items():
                count = coverage['difficulty_distribution']['counts'][level]
                print(f"  {level.capitalize()}: {count} ({pct}%)")
        
        # Quality distribution
        if 'quality_distribution' in summary:
            print(f"\n{'-'*70}")
            print("DISCRIMINATION QUALITY DISTRIBUTION")
            print(f"{'-'*70}")
            quality_dist = summary['quality_distribution']
            print(f"Excellent (≥0.40): {quality_dist['excellent']}")
            print(f"Good (0.30-0.39): {quality_dist['good']}")
            print(f"Acceptable (0.20-0.29): {quality_dist['acceptable']}")
            print(f"Poor (0.00-0.19): {quality_dist['poor']}")
            print(f"Negative (<0.00): {quality_dist['negative']}")
        
        print(f"\n{'='*70}")


def demo_pilot_metrics():
    """
    Demonstration of pilot metrics calculation
    """
    print("="*70)
    print("PILOT METRICS DEMONSTRATION")
    print("="*70)
    
    calculator = PilotMetrics()
    
    # Demo 1: P-value calculation
    print("\n1. P-VALUE (Difficulty Index)")
    print("-" * 70)
    p_result = calculator.calculate_p_value(correct_responses=45, total_responses=100)
    print(f"Correct responses: 45/100")
    print(f"P-value: {p_result['p_value']}")
    print(f"Difficulty: {p_result['difficulty_level']}")
    print(f"Interpretation: {p_result['interpretation']}")
    print(f"Is Optimal: {p_result['is_optimal']}")
    
    # Demo 2: Discrimination index
    print("\n2. DISCRIMINATION INDEX")
    print("-" * 70)
    disc_result = calculator.calculate_discrimination_index(
        upper_group_correct=24,
        upper_group_total=27,
        lower_group_correct=8,
        lower_group_total=27
    )
    print(f"Upper group (top 27%): 24/27 correct")
    print(f"Lower group (bottom 27%): 8/27 correct")
    print(f"Discrimination Index: {disc_result['discrimination_index']}")
    print(f"Quality: {disc_result['quality']}")
    print(f"Interpretation: {disc_result['interpretation']}")
    print(f"Action: {disc_result['action']}")
    
    # Demo 3: Coverage analysis
    print("\n3. COVERAGE ANALYSIS")
    print("-" * 70)
    
    # Sample MCQs
    sample_mcqs = [
        {'topic': 'Calculus', 'difficulty': 'easy', 'chapter': 'Ch1'},
        {'topic': 'Algebra', 'difficulty': 'medium', 'chapter': 'Ch2'},
        {'topic': 'Calculus', 'difficulty': 'hard', 'chapter': 'Ch1'},
        {'topic': 'Geometry', 'difficulty': 'medium', 'chapter': 'Ch3'},
        {'topic': 'Trigonometry', 'difficulty': 'easy', 'chapter': 'Ch4'},
    ]
    
    coverage_result = calculator.calculate_coverage(sample_mcqs)
    print(f"Total MCQs: {coverage_result['total_mcqs']}")
    print(f"Coverage Score: {coverage_result['coverage_score']}/100")
    print(f"Unique Topics: {coverage_result['topic_coverage']['unique_topics']}")
    print(f"Unique Chapters: {coverage_result['chapter_coverage']['unique_chapters']}")
    print(f"Difficulty Distribution: {coverage_result['difficulty_distribution']['percentages']}")
    
    print("\n" + "="*70)


if __name__ == "__main__":
    demo_pilot_metrics()
