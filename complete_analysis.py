"""
Complete MCQ Analysis Pipeline
Runs validation + pilot metrics in one workflow
"""

import json
from pathlib import Path
from validation import CurriculumMCQValidator
from sat_validation import SATQuestionValidator
from pilot_metrics import PilotMetrics
from analyze_pilot_metrics import simulate_student_responses


def complete_analysis_curriculum(mcq_file: str, subject: str):
    """
    Complete analysis for curriculum MCQs (Math/Physics)
    
    Args:
        mcq_file: Path to MCQ JSON file
        subject: 'math' or 'physics'
    """
    print(f"\n{'='*80}")
    print(f"COMPLETE ANALYSIS: {subject.upper()} MCQs")
    print(f"{'='*80}")
    
    # Load MCQs
    with open(mcq_file, 'r', encoding='utf-8') as f:
        mcqs = json.load(f)
    
    print(f"\nLoaded {len(mcqs)} MCQs from {mcq_file}")
    
    # ========================================
    # STEP 1: VALIDATION
    # ========================================
    print(f"\n{'='*80}")
    print("STEP 1: VALIDATION")
    print(f"{'='*80}")
    
    validator = CurriculumMCQValidator()
    validation_report = validator.validate_batch(mcqs)
    
    # Save validation report
    validation_output = Path(f"mcq_output/{subject}_validation_report.json")
    validator.save_validation_report(validation_report, validation_output)
    
    # ========================================
    # STEP 2: PILOT METRICS
    # ========================================
    print(f"\n{'='*80}")
    print("STEP 2: PILOT METRICS ANALYSIS")
    print(f"{'='*80}")
    
    # Define curriculum topics
    curriculum_topics = {
        'math': [
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
        ],
        'physics': [
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
    }
    
    # Simulate student responses (replace with real data in production)
    print("\nSimulating student responses for demonstration...")
    print("(Replace with actual pilot test data in production)")
    student_responses = simulate_student_responses(mcqs, num_students=100)
    
    # Calculate metrics
    calculator = PilotMetrics()
    metrics_report = calculator.analyze_mcq_batch(
        mcqs=mcqs,
        student_responses=student_responses,
        curriculum_topics=curriculum_topics.get(subject, [])
    )
    
    # Print metrics report
    calculator.print_report(metrics_report)
    
    # Save metrics report
    metrics_output = Path(f"mcq_output/{subject}_pilot_metrics_report.json")
    calculator.save_metrics_report(metrics_report, metrics_output)
    
    # ========================================
    # STEP 3: COMBINED SUMMARY
    # ========================================
    print(f"\n{'='*80}")
    print("COMBINED ANALYSIS SUMMARY")
    print(f"{'='*80}")
    
    print(f"\n📊 VALIDATION RESULTS:")
    print(f"   Total MCQs: {validation_report['total_mcqs']}")
    print(f"   Valid MCQs: {validation_report['valid_mcqs']} ({validation_report['pass_rate']:.1f}%)")
    print(f"   Average Quality Score: {validation_report['average_quality_score']}/100")
    
    print(f"\n📈 PILOT METRICS:")
    if 'average_p_value' in metrics_report['summary']:
        print(f"   Average P-value: {metrics_report['summary']['average_p_value']} (difficulty)")
    if 'average_discrimination' in metrics_report['summary']:
        print(f"   Average Discrimination: {metrics_report['summary']['average_discrimination']}")
    print(f"   Coverage Score: {metrics_report['coverage_analysis']['coverage_score']}/100")
    
    if 'quality_distribution' in metrics_report['summary']:
        print(f"\n🎯 DISCRIMINATION QUALITY:")
        qd = metrics_report['summary']['quality_distribution']
        print(f"   Excellent (≥0.40): {qd['excellent']}")
        print(f"   Good (0.30-0.39): {qd['good']}")
        print(f"   Acceptable (0.20-0.29): {qd['acceptable']}")
        print(f"   Poor (0.00-0.19): {qd['poor']}")
        print(f"   Negative (<0.00): {qd['negative']}")
    
    # Recommendations
    print(f"\n💡 RECOMMENDATIONS:")
    recommendations = []
    
    if validation_report['pass_rate'] < 80:
        recommendations.append("⚠️  Less than 80% MCQs passed validation - review failed items")
    
    if validation_report['average_quality_score'] < 75:
        recommendations.append("⚠️  Average quality score below 75 - improve question and option quality")
    
    if metrics_report['coverage_analysis']['coverage_score'] < 70:
        recommendations.append("⚠️  Coverage score below 70 - generate more diverse MCQs")
    
    if 'quality_distribution' in metrics_report['summary']:
        qd = metrics_report['summary']['quality_distribution']
        poor_ratio = (qd['poor'] + qd['negative']) / validation_report['total_mcqs']
        if poor_ratio > 0.3:
            recommendations.append("⚠️  More than 30% MCQs have poor discrimination - revise distractors")
    
    if recommendations:
        for rec in recommendations:
            print(f"   {rec}")
    else:
        print("   ✅ All metrics look good!")
    
    print(f"\n{'='*80}")
    print(f"Analysis complete! Reports saved to:")
    print(f"  - {validation_output}")
    print(f"  - {metrics_output}")
    print(f"{'='*80}\n")
    
    return validation_report, metrics_report


def complete_analysis_sat(mcq_file: str):
    """
    Complete analysis for SAT MCQs
    
    Args:
        mcq_file: Path to SAT MCQ JSON file
    """
    print(f"\n{'='*80}")
    print(f"COMPLETE ANALYSIS: SAT MCQs")
    print(f"{'='*80}")
    
    # Load MCQs
    with open(mcq_file, 'r', encoding='utf-8') as f:
        mcqs = json.load(f)
    
    print(f"\nLoaded {len(mcqs)} MCQs from {mcq_file}")
    
    # ========================================
    # STEP 1: VALIDATION
    # ========================================
    print(f"\n{'='*80}")
    print("STEP 1: VALIDATION")
    print(f"{'='*80}")
    
    validator = SATQuestionValidator()
    validation_report = validator.validate_batch(mcqs)
    
    # Save validation report
    validation_output = Path("mcq_output/sat/sat_validation_report.json")
    validator.save_validation_report(validation_report, validation_output)
    
    # ========================================
    # STEP 2: PILOT METRICS
    # ========================================
    print(f"\n{'='*80}")
    print("STEP 2: PILOT METRICS ANALYSIS")
    print(f"{'='*80}")
    
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
    print("(Replace with actual SAT pilot test data in production)")
    student_responses = simulate_student_responses(mcqs, num_students=150)
    
    # Calculate metrics
    calculator = PilotMetrics()
    metrics_report = calculator.analyze_mcq_batch(
        mcqs=mcqs,
        student_responses=student_responses,
        curriculum_topics=sat_topics
    )
    
    # Print metrics report
    calculator.print_report(metrics_report)
    
    # Save metrics report
    metrics_output = Path("mcq_output/sat/sat_pilot_metrics_report.json")
    calculator.save_metrics_report(metrics_report, metrics_output)
    
    # ========================================
    # STEP 3: COMBINED SUMMARY
    # ========================================
    print(f"\n{'='*80}")
    print("COMBINED ANALYSIS SUMMARY")
    print(f"{'='*80}")
    
    print(f"\n📊 VALIDATION RESULTS:")
    print(f"   Total MCQs: {validation_report['total_mcqs']}")
    print(f"   Valid MCQs: {validation_report['valid_mcqs']} ({validation_report['pass_rate']:.1f}%)")
    print(f"   Average Quality Score: {validation_report['average_quality_score']}/100")
    
    print(f"\n📈 PILOT METRICS:")
    if 'average_p_value' in metrics_report['summary']:
        print(f"   Average P-value: {metrics_report['summary']['average_p_value']} (difficulty)")
    if 'average_discrimination' in metrics_report['summary']:
        print(f"   Average Discrimination: {metrics_report['summary']['average_discrimination']}")
    print(f"   Coverage Score: {metrics_report['coverage_analysis']['coverage_score']}/100")
    
    print(f"\n{'='*80}")
    print(f"Analysis complete! Reports saved to:")
    print(f"  - {validation_output}")
    print(f"  - {metrics_output}")
    print(f"{'='*80}\n")
    
    return validation_report, metrics_report


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        subject = sys.argv[1].lower()
        
        if subject == 'math':
            complete_analysis_curriculum('mcq_output/math_mcqs.json', 'math')
        elif subject == 'physics':
            complete_analysis_curriculum('mcq_output/physics_mcqs.json', 'physics')
        elif subject == 'sat':
            complete_analysis_sat('mcq_output/sat/sample_sat_mcqs.json')
        else:
            print(f"Unknown subject: {subject}")
            print("Usage: python complete_analysis.py [math|physics|sat]")
    else:
        print("Complete MCQ Analysis Pipeline")
        print("=" * 80)
        print("\nUsage:")
        print("  python complete_analysis.py math     # Analyze Math MCQs")
        print("  python complete_analysis.py physics  # Analyze Physics MCQs")
        print("  python complete_analysis.py sat      # Analyze SAT MCQs")
        print("\nThis script performs:")
        print("  1. Validation (structure, quality, compliance)")
        print("  2. Pilot metrics (p-value, discrimination, coverage)")
        print("  3. Combined analysis and recommendations")
        print("=" * 80)
