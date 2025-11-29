"""
Pilot Metrics Analysis for Generated MCQs
Analyzes existing MCQ outputs with pilot metrics
"""

import json
from pathlib import Path
from pilot_metrics import PilotMetrics
import random


def simulate_student_responses(mcqs: list, num_students: int = 100) -> list:
    """
    Simulate student responses for demonstration
    In production, replace with actual student test data
    
    Args:
        mcqs: List of MCQ dictionaries
        num_students: Number of students to simulate
        
    Returns:
        List of response data for each MCQ
    """
    responses = []
    
    for mcq_idx, mcq in enumerate(mcqs):
        # Simulate student total scores (normal distribution around 70%)
        student_scores = [
            max(0, min(100, int(random.gauss(70, 15))))
            for _ in range(num_students)
        ]
        
        # Simulate responses based on difficulty and student ability
        difficulty = mcq.get('difficulty', 'medium')
        base_probability = {
            'easy': 0.75,
            'medium': 0.50,
            'hard': 0.25
        }.get(difficulty, 0.50)
        
        # Higher scoring students more likely to answer correctly
        responses_for_mcq = []
        for score in student_scores:
            # Probability increases with student score
            adjusted_probability = base_probability * (0.5 + (score / 200))
            is_correct = random.random() < adjusted_probability
            responses_for_mcq.append(is_correct)
        
        # Count correct responses
        correct_count = sum(responses_for_mcq)
        
        response_data = {
            'mcq_id': mcq_idx,
            'correct_responses': correct_count,
            'total_responses': num_students,
            'student_scores': student_scores,
            'responses': responses_for_mcq
        }
        
        responses.append(response_data)
    
    return responses


def analyze_math_mcqs():
    """Analyze Math MCQs with pilot metrics"""
    print("\n" + "="*70)
    print("ANALYZING MATH MCQs")
    print("="*70)
    
    # Load Math MCQs
    mcq_file = Path("mcq_output/math_mcqs.json")
    if not mcq_file.exists():
        print(f"❌ File not found: {mcq_file}")
        return
    
    with open(mcq_file, 'r', encoding='utf-8') as f:
        mcqs = json.load(f)
    
    print(f"Loaded {len(mcqs)} Math MCQs")
    
    # Define curriculum topics for Math
    math_curriculum_topics = [
        'Matrices and Determinants',
        'Partial Fractions',
        'Functions and Graphs',
        'Limits and Continuity',
        'Differentiation',
        'Integration',
        'Sequences and Series',
        'Vectors',
        'Trigonometry',
        'Complex Numbers',
        'Permutations and Combinations',
        'Probability'
    ]
    
    # Simulate student responses (replace with actual data in production)
    print("\nSimulating student responses for demonstration...")
    student_responses = simulate_student_responses(mcqs, num_students=100)
    
    # Calculate pilot metrics
    print("\nCalculating pilot metrics...")
    calculator = PilotMetrics()
    report = calculator.analyze_mcq_batch(
        mcqs=mcqs,
        student_responses=student_responses,
        curriculum_topics=math_curriculum_topics
    )
    
    # Print report
    calculator.print_report(report)
    
    # Save report
    output_path = Path("mcq_output/math_pilot_metrics_report.json")
    calculator.save_metrics_report(report, output_path)
    
    return report


def analyze_physics_mcqs():
    """Analyze Physics MCQs with pilot metrics"""
    print("\n" + "="*70)
    print("ANALYZING PHYSICS MCQs")
    print("="*70)
    
    # Load Physics MCQs
    mcq_file = Path("mcq_output/physics_mcqs.json")
    if not mcq_file.exists():
        print(f"❌ File not found: {mcq_file}")
        return
    
    with open(mcq_file, 'r', encoding='utf-8') as f:
        mcqs = json.load(f)
    
    print(f"Loaded {len(mcqs)} Physics MCQs")
    
    # Define curriculum topics for Physics
    physics_curriculum_topics = [
        'Current Electricity',
        'Electrostatics',
        'Magnetism',
        'Electromagnetic Induction',
        'Force and Motion',
        'Work and Energy',
        'Circular Motion',
        'Waves',
        'Optics',
        'Modern Physics',
        'Nuclear Physics',
        'Thermodynamics'
    ]
    
    # Simulate student responses
    print("\nSimulating student responses for demonstration...")
    student_responses = simulate_student_responses(mcqs, num_students=100)
    
    # Calculate pilot metrics
    print("\nCalculating pilot metrics...")
    calculator = PilotMetrics()
    report = calculator.analyze_mcq_batch(
        mcqs=mcqs,
        student_responses=student_responses,
        curriculum_topics=physics_curriculum_topics
    )
    
    # Print report
    calculator.print_report(report)
    
    # Save report
    output_path = Path("mcq_output/physics_pilot_metrics_report.json")
    calculator.save_metrics_report(report, output_path)
    
    return report


def analyze_sat_mcqs():
    """Analyze SAT MCQs with pilot metrics"""
    print("\n" + "="*70)
    print("ANALYZING SAT MCQs")
    print("="*70)
    
    # Load SAT MCQs
    mcq_file = Path("mcq_output/sat/sample_sat_mcqs.json")
    if not mcq_file.exists():
        print(f"❌ File not found: {mcq_file}")
        return
    
    with open(mcq_file, 'r', encoding='utf-8') as f:
        mcqs = json.load(f)
    
    print(f"Loaded {len(mcqs)} SAT MCQs")
    
    # SAT topics
    sat_topics = [
        'Reading Comprehension',
        'Main Idea',
        'Detail Questions',
        'Inference',
        'Vocabulary in Context',
        'Grammar',
        'Punctuation',
        'Style and Tone',
        'Organization',
        'Transitions'
    ]
    
    # Simulate student responses
    print("\nSimulating student responses for demonstration...")
    student_responses = simulate_student_responses(mcqs, num_students=150)
    
    # Calculate pilot metrics
    print("\nCalculating pilot metrics...")
    calculator = PilotMetrics()
    report = calculator.analyze_mcq_batch(
        mcqs=mcqs,
        student_responses=student_responses,
        curriculum_topics=sat_topics
    )
    
    # Print report
    calculator.print_report(report)
    
    # Save report
    output_path = Path("mcq_output/sat/sat_pilot_metrics_report.json")
    calculator.save_metrics_report(report, output_path)
    
    return report


def analyze_single_mcq_example():
    """
    Example of analyzing a single MCQ with custom student data
    """
    print("\n" + "="*70)
    print("SINGLE MCQ ANALYSIS EXAMPLE")
    print("="*70)
    
    calculator = PilotMetrics()
    
    # Example: 100 students, sorted by total test score
    # Top 27 students (upper group): 24 answered correctly
    # Bottom 27 students (lower group): 8 answered correctly
    # Total correct: 45 students
    
    print("\nScenario: Physics question on Ohm's Law")
    print("Total students: 100")
    print("Students answering correctly: 45")
    
    # P-value
    p_result = calculator.calculate_p_value(
        correct_responses=45,
        total_responses=100
    )
    
    print(f"\n1. P-VALUE ANALYSIS:")
    print(f"   P-value: {p_result['p_value']}")
    print(f"   Difficulty: {p_result['difficulty_level']}")
    print(f"   Optimal: {p_result['is_optimal']}")
    print(f"   {p_result['interpretation']}")
    
    # Discrimination
    disc_result = calculator.calculate_discrimination_index(
        upper_group_correct=24,
        upper_group_total=27,
        lower_group_correct=8,
        lower_group_total=27
    )
    
    print(f"\n2. DISCRIMINATION ANALYSIS:")
    print(f"   Discrimination Index: {disc_result['discrimination_index']}")
    print(f"   Upper group (top 27%): {disc_result['p_upper']} answered correctly")
    print(f"   Lower group (bottom 27%): {disc_result['p_lower']} answered correctly")
    print(f"   Quality: {disc_result['quality']}")
    print(f"   Action: {disc_result['action']}")
    print(f"   {disc_result['interpretation']}")
    
    print("\n" + "="*70)


def compare_all_subjects():
    """
    Compare pilot metrics across all subjects
    """
    print("\n" + "="*70)
    print("CROSS-SUBJECT COMPARISON")
    print("="*70)
    
    results = {}
    
    # Analyze each subject
    subjects = [
        ('Math', 'mcq_output/math_mcqs.json'),
        ('Physics', 'mcq_output/physics_mcqs.json'),
        ('SAT', 'mcq_output/sat/sample_sat_mcqs.json')
    ]
    
    for subject_name, file_path in subjects:
        mcq_file = Path(file_path)
        if mcq_file.exists():
            with open(mcq_file, 'r', encoding='utf-8') as f:
                mcqs = json.load(f)
            
            calculator = PilotMetrics()
            
            # Coverage only (no student data)
            report = calculator.analyze_mcq_batch(mcqs=mcqs)
            
            results[subject_name] = {
                'total_mcqs': len(mcqs),
                'coverage_score': report['coverage_analysis']['coverage_score'],
                'unique_topics': report['coverage_analysis']['topic_coverage']['unique_topics'],
                'unique_chapters': report['coverage_analysis']['chapter_coverage']['unique_chapters']
            }
    
    # Print comparison
    print(f"\n{'Subject':<15} {'MCQs':<10} {'Coverage':<12} {'Topics':<10} {'Chapters':<10}")
    print("-" * 70)
    for subject, data in results.items():
        print(f"{subject:<15} {data['total_mcqs']:<10} {data['coverage_score']:<12.1f} {data['unique_topics']:<10} {data['unique_chapters']:<10}")
    
    print("\n" + "="*70)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        subject = sys.argv[1].lower()
        if subject == 'math':
            analyze_math_mcqs()
        elif subject == 'physics':
            analyze_physics_mcqs()
        elif subject == 'sat':
            analyze_sat_mcqs()
        elif subject == 'example':
            analyze_single_mcq_example()
        elif subject == 'compare':
            compare_all_subjects()
        else:
            print(f"Unknown subject: {subject}")
            print("Usage: python analyze_pilot_metrics.py [math|physics|sat|example|compare]")
    else:
        # Run all analyses
        print("Running comprehensive pilot metrics analysis...")
        analyze_single_mcq_example()
        compare_all_subjects()
        
        # Try to analyze each subject if files exist
        for analysis_func in [analyze_math_mcqs, analyze_physics_mcqs, analyze_sat_mcqs]:
            try:
                analysis_func()
            except Exception as e:
                print(f"⚠️  Error in analysis: {e}")
