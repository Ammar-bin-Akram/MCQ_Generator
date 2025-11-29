# MCQ_Generator
A RAG-based system that generates high-quality MCQs from HSSC Physics, Math and SAT English syllabus.

## Features

- **RAG-based MCQ Generation**: Uses Retrieval-Augmented Generation for accurate, curriculum-aligned questions
- **Multi-subject Support**: Physics, Mathematics (FSc), and SAT Reading/Writing
- **Quality Validation**: Comprehensive validation suite for structure, quality, and compliance
- **Pilot Metrics**: Advanced psychometric analysis including:
  - **P-value (Difficulty Index)**: Measures question difficulty
  - **Discrimination Index**: Evaluates how well questions differentiate between high/low performers
  - **Coverage Analysis**: Assesses content coverage across curriculum

## Project Structure

### Core Files
- `generate_mcqs.py` - Generate FSc Math & Physics MCQs
- `generate_sat_mcqs.py` - Generate SAT Reading/Writing MCQs
- `validation.py` - Validate curriculum MCQs
- `sat_validation.py` - Validate SAT MCQs
- `pilot_metrics.py` - Calculate pilot metrics (p-value, discrimination, coverage)
- `analyze_pilot_metrics.py` - Analyze MCQs with pilot metrics

### Supporting Files
- `chunking.py` - Text chunking for RAG
- `preprocessing.py` / `preprocessing_sat.py` - Data preprocessing
- `filtering.py` - Content filtering
- `extract_text.py` - Text extraction utilities

## Quick Start

### 1. Generate MCQs
```bash
# Generate Physics/Math MCQs
python generate_mcqs.py

# Generate SAT MCQs
python generate_sat_mcqs.py
```

### 2. Validate MCQs
```bash
# Validate curriculum MCQs
python validation.py

# Validate SAT MCQs
python sat_validation.py
```

### 3. Analyze Pilot Metrics
```bash
# Compare all subjects
python analyze_pilot_metrics.py compare

# Analyze specific subject
python analyze_pilot_metrics.py physics
python analyze_pilot_metrics.py math
python analyze_pilot_metrics.py sat

# See single MCQ example
python analyze_pilot_metrics.py example
```

## Pilot Metrics

The system implements three key psychometric metrics:

### 1. P-value (Difficulty Index)
- Measures the proportion of students answering correctly
- Range: 0.0 to 1.0
- Optimal: 0.30 - 0.70
- Interpretation:
  - > 0.75: Easy
  - 0.25-0.75: Moderate
  - < 0.25: Hard

### 2. Discrimination Index
- Measures how well a question differentiates ability levels
- Range: -1.0 to 1.0
- Optimal: ≥ 0.30
- Quality levels:
  - ≥ 0.40: Excellent
  - 0.30-0.39: Good
  - 0.20-0.29: Acceptable
  - < 0.20: Poor (needs revision)
  - < 0.00: Negative (reject item)

### 3. Coverage Analysis
- Evaluates content distribution across:
  - Topics
  - Difficulty levels
  - Chapters
- Provides coverage score (0-100)
- Identifies gaps and imbalances

For detailed documentation, see [PILOT_METRICS_GUIDE.md](PILOT_METRICS_GUIDE.md)

## Output Structure

```
mcq_output/
├── math_mcqs.json                      # Generated Math MCQs
├── physics_mcqs.json                   # Generated Physics MCQs
├── math_validation_report.json         # Math validation results
├── physics_validation_report.json      # Physics validation results
├── math_pilot_metrics_report.json      # Math pilot metrics
├── physics_pilot_metrics_report.json   # Physics pilot metrics
└── sat/
    ├── sample_sat_mcqs.json           # Generated SAT MCQs
    ├── validation_report.json         # SAT validation results
    └── sat_pilot_metrics_report.json  # SAT pilot metrics
```

## Documentation

- **[PILOT_METRICS_GUIDE.md](PILOT_METRICS_GUIDE.md)** - Comprehensive guide to pilot metrics (formulas, examples, integration)
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Quick command reference and metric interpretation cheat sheet
- **[VISUAL_GUIDE.md](VISUAL_GUIDE.md)** - Visual diagrams and decision trees for all metrics
- **[IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)** - Complete implementation summary

## Testing

Run the demo to see all metrics in action:
```bash
python pilot_metrics.py
python test_metrics.py
```
