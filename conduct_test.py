"""
Interactive MCQ Test Conductor
Administers MCQs to students and records responses
"""

import json
from pathlib import Path
from datetime import datetime


def load_mcqs(mcq_file: str) -> list:
    """Load MCQs from JSON file"""
    with open(mcq_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def display_mcq(mcq: dict, mcq_number: int, total_mcqs: int):
    """Display a single MCQ to the student"""
    print("\n" + "="*80)
    print(f"Question {mcq_number}/{total_mcqs}")
    print("="*80)
    
    # Display question
    print(f"\n{mcq.get('question', 'No question text')}\n")
    
    # Display options
    options = mcq.get('options', {})
    for key in ['A', 'B', 'C', 'D']:
        if key in options:
            print(f"  {key}. {options[key]}")
    
    print()


def get_student_answer() -> str:
    """Get student's answer (A, B, C, or D)"""
    while True:
        answer = input("Enter answer (A/B/C/D): ").strip().upper()
        if answer in ['A', 'B', 'C', 'D']:
            return answer
        print("❌ Invalid input. Please enter A, B, C, or D.")


def conduct_student_test(mcqs: list, student_num: int, total_students: int) -> tuple:
    """
    Conduct test for a single student
    
    Returns:
        (total_score, responses_list)
    """
    print("\n" + "="*80)
    print(f"STUDENT {student_num}/{total_students}")
    print("="*80)
    
    responses = []
    correct_count = 0
    
    for idx, mcq in enumerate(mcqs, 1):
        display_mcq(mcq, idx, len(mcqs))
        
        student_answer = get_student_answer()
        correct_answer = mcq.get('correct_answer', '').upper()
        
        is_correct = (student_answer == correct_answer)
        responses.append(is_correct)
        
        if is_correct:
            correct_count += 1
            print("✅ Correct!")
        else:
            print(f"❌ Incorrect. Correct answer: {correct_answer}")
    
    # Calculate total score (percentage)
    total_score = int((correct_count / len(mcqs)) * 100) if mcqs else 0
    
    print("\n" + "="*80)
    print(f"Student {student_num} Results:")
    print(f"  Score: {correct_count}/{len(mcqs)} ({total_score}%)")
    print("="*80)
    
    return total_score, responses


def conduct_test(mcq_file: str, num_students: int, output_file: str = None):
    """
    Main test conductor - administers test to all students
    
    Args:
        mcq_file: Path to MCQ JSON file
        num_students: Number of students taking the test
        output_file: Path to save responses (default: student_responses.json)
    """
    # Load MCQs
    print(f"\n{'='*80}")
    print("MCQ TEST CONDUCTOR")
    print(f"{'='*80}")
    
    mcqs = load_mcqs(mcq_file)
    print(f"\nLoaded {len(mcqs)} MCQs from {mcq_file}")
    print(f"Number of students: {num_students}")
    
    input("\n📋 Press Enter to start the test...")
    
    # Collect data
    student_scores = []
    all_responses = []
    
    # Conduct test for each student
    for student_num in range(1, num_students + 1):
        total_score, responses = conduct_student_test(mcqs, student_num, num_students)
        student_scores.append(total_score)
        
        # Store responses in format needed for metrics
        for mcq_idx, is_correct in enumerate(responses):
            if student_num == 1:
                # Initialize response tracking for each MCQ
                all_responses.append({
                    'mcq_id': mcq_idx,
                    'responses': [is_correct]
                })
            else:
                # Add this student's response to existing MCQ
                all_responses[mcq_idx]['responses'].append(is_correct)
        
        # Pause between students (except after last student)
        if student_num < num_students:
            input(f"\n⏸️  Press Enter when Student {student_num + 1} is ready...")
    
    # Prepare final data structure
    test_data = {
        'test_metadata': {
            'num_students': num_students,
            'num_mcqs': len(mcqs),
            'test_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'mcq_source': str(mcq_file)
        },
        'student_scores': student_scores,
        'responses': all_responses
    }
    
    # Save to file
    if output_file is None:
        output_file = 'student_responses.json'
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(test_data, f, indent=2, ensure_ascii=False)
    
    # Summary
    print("\n" + "="*80)
    print("TEST COMPLETED!")
    print("="*80)
    print(f"\n📊 Summary:")
    print(f"  Students tested: {num_students}")
    print(f"  MCQs administered: {len(mcqs)}")
    print(f"  Average score: {sum(student_scores)/len(student_scores):.1f}%")
    print(f"  Highest score: {max(student_scores)}%")
    print(f"  Lowest score: {min(student_scores)}%")
    print(f"\n💾 Responses saved to: {output_file}")
    print(f"\nNext step: Run 'python calculate_metrics.py' to analyze results")
    print("="*80 + "\n")
    
    return test_data


def quick_test_mode(mcq_file: str, num_students: int):
    """
    Quick test mode with auto-responses (for testing the system)
    """
    import random
    
    print(f"\n{'='*80}")
    print("QUICK TEST MODE (Auto-Generated Responses)")
    print(f"{'='*80}")
    
    mcqs = load_mcqs(mcq_file)
    print(f"\nLoaded {len(mcqs)} MCQs")
    print(f"Generating responses for {num_students} students...")
    
    student_scores = []
    all_responses = []
    
    for student_num in range(1, num_students + 1):
        # Simulate student ability (random score distribution)
        ability = random.gauss(0.6, 0.15)  # Average 60% correct
        ability = max(0.2, min(0.9, ability))  # Clamp between 20-90%
        
        responses = []
        for mcq_idx, mcq in enumerate(mcqs):
            # Higher ability students more likely to answer correctly
            difficulty = {'easy': 0.8, 'medium': 0.5, 'hard': 0.3}.get(
                mcq.get('difficulty', 'medium'), 0.5
            )
            prob_correct = (ability + difficulty) / 2
            is_correct = random.random() < prob_correct
            responses.append(is_correct)
            
            if student_num == 1:
                all_responses.append({
                    'mcq_id': mcq_idx,
                    'responses': [is_correct]
                })
            else:
                all_responses[mcq_idx]['responses'].append(is_correct)
        
        score = int((sum(responses) / len(mcqs)) * 100)
        student_scores.append(score)
        print(f"  Student {student_num}: {score}%")
    
    test_data = {
        'test_metadata': {
            'num_students': num_students,
            'num_mcqs': len(mcqs),
            'test_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'mcq_source': str(mcq_file),
            'mode': 'quick_test'
        },
        'student_scores': student_scores,
        'responses': all_responses
    }
    
    output_file = 'student_responses.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(test_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Quick test complete! Responses saved to {output_file}")
    print(f"Average score: {sum(student_scores)/len(student_scores):.1f}%")
    print(f"\nRun 'python calculate_metrics.py' to analyze results")
    
    return test_data


if __name__ == "__main__":
    import sys
    
    # Check command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == 'quick':
            # Quick test mode
            mcq_file = sys.argv[2] if len(sys.argv) > 2 else 'mcq_output/physics_mcqs.json'
            num_students = int(sys.argv[3]) if len(sys.argv) > 3 else 5
            quick_test_mode(mcq_file, num_students)
        else:
            print("Usage:")
            print("  python conduct_test.py              # Interactive mode")
            print("  python conduct_test.py quick [file] [num]  # Quick test mode")
    else:
        # Interactive mode
        print("\n" + "="*80)
        print("MCQ TEST CONDUCTOR - INTERACTIVE MODE")
        print("="*80)
        
        # Get MCQ file
        print("\nAvailable MCQ files:")
        print("  1. mcq_output/physics_mcqs.json")
        print("  2. mcq_output/math_mcqs.json")
        print("  3. mcq_output/sat/sample_sat_mcqs.json")
        print("  4. Custom path")
        
        choice = input("\nSelect MCQ file (1-4): ").strip()
        
        mcq_files = {
            '1': 'mcq_output/physics_mcqs.json',
            '2': 'mcq_output/math_mcqs.json',
            '3': 'mcq_output/sat/sample_sat_mcqs.json'
        }
        
        if choice in mcq_files:
            mcq_file = mcq_files[choice]
        elif choice == '4':
            mcq_file = input("Enter MCQ file path: ").strip()
        else:
            print("Invalid choice. Using default: mcq_output/physics_mcqs.json")
            mcq_file = 'mcq_output/physics_mcqs.json'
        
        # Check file exists
        if not Path(mcq_file).exists():
            print(f"File not found: {mcq_file}")
            sys.exit(1)
        
        # Get number of students
        num_students = int(input("\nHow many students will take the test? ").strip())
        
        if num_students < 1:
            print("Number of students must be at least 1")
            sys.exit(1)
        
        # Conduct the test
        conduct_test(mcq_file, num_students)
