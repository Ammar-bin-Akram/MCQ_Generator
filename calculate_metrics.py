"""
Automatic Metrics Calculator
Reads test responses and calculates all pilot metrics
"""

import json
from pathlib import Path
from pilot_metrics import PilotMetrics


def load_test_data(response_file: str = 'student_responses.json') -> dict:
    """Load student response data"""
    with open(response_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_mcqs(mcq_file: str) -> list:
    """Load MCQ data"""
    with open(mcq_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_curriculum_topics(mcq_file: str) -> list:
    """Get curriculum topics based on file path"""
    path_str = str(mcq_file).lower()
    
    if 'math' in path_str:
        return [
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
    elif 'physics' in path_str:
        return [
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
    elif 'sat' in path_str:
        return [
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
    
    return []


def calculate_metrics(response_file: str = 'student_responses.json', 
                     output_file: str = None):
    """
    Calculate all pilot metrics from test responses
    
    Args:
        response_file: Path to student responses JSON
        output_file: Path to save metrics report (auto-generated if None)
    """
    print("\n" + "="*80)
    print("PILOT METRICS CALCULATOR")
    print("="*80)
    
    # Load test data
    print(f"\nLoading test data from {response_file}...")
    test_data = load_test_data(response_file)
    
    metadata = test_data['test_metadata']
    student_scores = test_data['student_scores']
    responses = test_data['responses']
    
    print(f"\n📊 Test Information:")
    print(f"  Date: {metadata['test_date']}")
    print(f"  Students: {metadata['num_students']}")
    print(f"  MCQs: {metadata['num_mcqs']}")
    print(f"  MCQ Source: {metadata['mcq_source']}")
    
    # Load MCQs
    mcq_file = metadata['mcq_source']
    print(f"\nLoading MCQs from {mcq_file}...")
    mcqs = load_mcqs(mcq_file)
    
    # Get curriculum topics
    curriculum_topics = get_curriculum_topics(mcq_file)
    
    # Convert responses to format expected by PilotMetrics
    formatted_responses = []
    for resp_data in responses:
        mcq_id = resp_data['mcq_id']
        responses_list = resp_data['responses']
        
        correct_count = sum(1 for r in responses_list if r)
        
        formatted_responses.append({
            'mcq_id': mcq_id,
            'correct_responses': correct_count,
            'total_responses': len(responses_list),
            'student_scores': student_scores,
            'responses': responses_list
        })
    
    # Calculate metrics
    print("\nCalculating pilot metrics...")
    calculator = PilotMetrics()
    
    report = calculator.analyze_mcq_batch(
        mcqs=mcqs,
        student_responses=formatted_responses,
        curriculum_topics=curriculum_topics
    )
    
    # Print report
    calculator.print_report(report)
    
    # Print individual MCQ details
    print(f"\n{'='*80}")
    print("INDIVIDUAL MCQ ANALYSIS")
    print(f"{'='*80}")
    
    for idx, metrics in enumerate(report['individual_mcq_metrics']):
        print(f"\n{'─'*80}")
        print(f"MCQ {idx + 1}: {mcqs[idx].get('topic', 'Unknown Topic')}")
        print(f"{'─'*80}")
        
        # Question preview
        question = mcqs[idx].get('question', '')
        preview = question[:100] + '...' if len(question) > 100 else question
        print(f"Q: {preview}")
        
        # P-value
        if 'p_value' in metrics and metrics['p_value']['valid']:
            p = metrics['p_value']
            status = '✅' if p['is_optimal'] else '⚠️'
            print(f"\n  {status} P-VALUE: {p['p_value']} ({p['difficulty_level']})")
            print(f"     {p['correct_responses']}/{p['total_responses']} students answered correctly")
            print(f"     {p['interpretation']}")
        
        # Discrimination
        if 'discrimination' in metrics and metrics['discrimination']['valid']:
            d = metrics['discrimination']
            quality_icon = {
                'excellent': '🌟',
                'good': '✅',
                'acceptable': '⚠️',
                'poor': '❌',
                'negative': '🚫'
            }.get(d['quality'], '?')
            
            print(f"\n  {quality_icon} DISCRIMINATION: {d['discrimination_index']} ({d['quality']})")
            print(f"     Top students: {d['upper_group']['correct']}/{d['upper_group']['total']} correct")
            print(f"     Bottom students: {d['lower_group']['correct']}/{d['lower_group']['total']} correct")
            print(f"     Action: {d['action']}")
    
    # Determine output file
    if output_file is None:
        # Auto-generate filename based on MCQ source
        source_path = Path(mcq_file)
        subject = source_path.stem  # e.g., 'physics_mcqs' -> 'physics_mcqs'
        output_file = f"mcq_output/{subject}_metrics_report.json"
    
    # Save report
    calculator.save_metrics_report(report, output_file)
    
    # Recommendations
    print(f"\n{'='*80}")
    print("RECOMMENDATIONS")
    print(f"{'='*80}")
    
    num_students = metadata['num_students']
    
    if num_students < 20:
        print(f"\n⚠️  Sample Size: {num_students} students")
        print("   - Small sample size may affect reliability")
        print("   - Discrimination index less stable with <20 students")
        print("   - P-value still informative")
        print("   - Recommend testing with 20-30+ students for robust metrics")
    
    if 'quality_distribution' in report['summary']:
        qd = report['summary']['quality_distribution']
        
        excellent = qd['excellent']
        good = qd['good']
        poor = qd['poor']
        negative = qd['negative']
        
        print(f"\n📊 Question Quality:")
        if excellent + good >= metadata['num_mcqs'] * 0.7:
            print("   ✅ Most questions have good discrimination")
        
        if poor + negative > metadata['num_mcqs'] * 0.3:
            print(f"   ⚠️  {poor + negative} questions have poor discrimination")
            print("      → Review these questions")
            print("      → Check if distractors are too similar/obvious")
            print("      → Ensure questions test key concepts")
    
    if 'average_p_value' in report['summary']:
        avg_p = report['summary']['average_p_value']
        
        print(f"\n📈 Overall Difficulty:")
        if avg_p > 0.75:
            print(f"   ⚠️  Average P-value: {avg_p} (Questions may be too easy)")
            print("      → Consider adding more challenging questions")
        elif avg_p < 0.25:
            print(f"   ⚠️  Average P-value: {avg_p} (Questions may be too hard)")
            print("      → Consider adding easier questions or reviewing content coverage")
        else:
            print(f"   ✅ Average P-value: {avg_p} (Good difficulty balance)")
    
    # Coverage analysis
    coverage_score = report['coverage_analysis']['coverage_score']
    print(f"\n📚 Content Coverage:")
    print(f"   Coverage Score: {coverage_score}/100")
    
    if coverage_score < 60:
        print("   ⚠️  Low coverage - consider generating more diverse MCQs")
    elif coverage_score < 80:
        print("   ✅ Moderate coverage - could add more topic variety")
    else:
        print("   ✅ Good coverage across curriculum")
    
    print(f"\n{'='*80}")
    print("ANALYSIS COMPLETE!")
    print(f"{'='*80}")
    print(f"\n📄 Full report saved to: {output_file}")
    print(f"\n💡 Use these insights to:")
    print("   1. Identify questions that need revision")
    print("   2. Balance difficulty distribution")
    print("   3. Improve content coverage")
    print("   4. Enhance discriminatory power of questions")
    print(f"\n{'='*80}\n")
    
    return report


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        response_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        calculate_metrics(response_file, output_file)
    else:
        # Use default file
        response_file = 'student_responses.json'
        
        if not Path(response_file).exists():
            print(f"\n❌ Response file not found: {response_file}")
            print("\nPlease run 'python conduct_test.py' first to conduct a test")
            print("and generate student responses.\n")
            sys.exit(1)
        
        calculate_metrics(response_file)
