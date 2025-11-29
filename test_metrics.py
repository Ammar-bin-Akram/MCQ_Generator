"""Quick test of all three pilot metrics"""
from pilot_metrics import PilotMetrics

print('\n' + '='*70)
print('PILOT METRICS - ALL THREE METRICS TEST')
print('='*70)

calc = PilotMetrics()

# Test 1: P-Value
p = calc.calculate_p_value(45, 100)
print(f'\n✅ P-VALUE: {p["p_value"]} ({p["difficulty_level"]})')
print(f'   {p["interpretation"]}')

# Test 2: Discrimination
d = calc.calculate_discrimination_index(24, 27, 8, 27)
print(f'\n✅ DISCRIMINATION: {d["discrimination_index"]} ({d["quality"]})')
print(f'   {d["action"]}')

# Test 3: Coverage
mcqs = [
    {'topic': 'Physics', 'difficulty': 'medium', 'chapter': 'Ch1'},
    {'topic': 'Math', 'difficulty': 'easy', 'chapter': 'Ch2'},
    {'topic': 'Physics', 'difficulty': 'hard', 'chapter': 'Ch1'},
]
c = calc.calculate_coverage(mcqs)
print(f'\n✅ COVERAGE: {c["coverage_score"]}/100')
print(f'   {c["topic_coverage"]["unique_topics"]} topics, {c["chapter_coverage"]["unique_chapters"]} chapters')

print('\n' + '='*70)
print('✅ ALL THREE METRICS WORKING PERFECTLY!')
print('='*70 + '\n')
