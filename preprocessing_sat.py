# Preprocessing SAT

import os
import re
import json
from pathlib import Path

def create_sat_directories():
    # creating necessary directories
    SAT_CORPUS_DIR.mkdir(parents=True, exist_ok=True)
    BLUEPRINT_DIR.mkdir(parents=True, exist_ok=True)
    print("SAT directory structure created")

def extract_sat_structure(content: str, test_num: int) -> dict:
    # Extract all numbered questions from the entire Reading and Writing block.
    
    # 1. Define the overall structure we need to capture
    sections = {'english_questions': {'passages': [], 'topics': set()}}
    
    # 2. Find the full Reading and Writing content (Modules 1 and 2, excluding Math and boilerplates)
    # This regex is broad and matches all content between the first R/W header and the first Math header.
    rw_content_match = re.search(r'(# Reading and Writing.*)(?=# Math|$)', content, re.DOTALL | re.IGNORECASE)
    
    if not rw_content_match:
        print("Warning: Could not find main 'Reading and Writing' section block.")
        return sections
        
    rw_content = rw_content_match.group(1).strip()
    
    # 3. Split the entire block by the standard question header pattern (## 1, ## 2, etc.)
    # The regex splits on the header and includes the header line with the subsequent question content.
    # We use a lookahead to ensure the delimiter is not consumed.
    question_blocks = re.split(r'(?=\n##\s*\d+\s*\n)', rw_content)

    q_id_counter = 1
    
    for block in question_blocks:
        block = block.strip()
        if not block:
            continue
        
        # Check if the block actually starts with a question header (## <num>)
        header_match = re.match(r'##\s*(\d+)\s*\n', block)
        
        if header_match:
            # This is a standard question block (e.g., ## 1, ## 2)
            q_num = int(header_match.group(1))
            
            # Use a simple, safer topic tag
            topic = "General English Item" 
            source = f"Q {q_num}"

            # Simple heuristic for SAT structure: R&W modules typically contain 33 or 27 questions.
            # We'll use question number to assign a basic section ID (optional but good practice)
            section_key = 'R&W_M1' if q_num <= 33 else 'R&W_M2'
            
            # Format the data for the corpus
            sections['english_questions']['topics'].add(topic)
            sections['english_questions']['passages'].append({
                'passage_id': f"test{test_num}_{section_key}_q{q_num}",
                'source': source,
                'topic': topic,
                'content': block
            })
            q_id_counter += 1
        
        else:
            # This handles introductory text, directions, or headers that didn't match the simple question number
            # We skip this boilerplate as it's not material for MCQs
            pass

    return sections

def categorize_passage(passage_text: str, source: str) -> str:
    """Categorize reading passage by topic"""
    text_lower = passage_text.lower()
    
    # Literature
    if any(word in source.lower() for word in ['novel', 'story', 'poem', 'fiction', 'literature']):
        return "Literature and Fiction"
    
    # Science
    if any(word in text_lower[:500] for word in ['experiment', 'study', 'research', 'scientific', 'hypothesis', 'data', 'results']):
        return "Science"
    
    # Social Studies/History
    if any(word in text_lower[:500] for word in ['history', 'political', 'society', 'government', 'economy', 'historical']):
        return "Social Studies and History"
    
    # General non-fiction
    return "General Non-Fiction"

def create_sat_corpus_files(test_num: int, sections: dict):
    # function to create sat corpus files
    
    # Use the combined 'english_questions' data structure
    if 'english_questions' not in sections:
        return
        
    for item in sections['english_questions']['passages']:
        # Use the passage_id (e.g., test10_R&W_M1_q1) as the filename
        filename = f"{item['passage_id']}.md"
        filepath = SAT_CORPUS_DIR / filename
        
        # Format content (using the full block captured in the extraction)
        formatted_content = f"""# SAT Test {test_num} - Question {item['source']}

## Topic: {item['topic']}
## Source: {item['source']}

{item['content']}
"""
        
        filepath.write_text(formatted_content, encoding='utf-8')

def create_sat_blueprint(all_tests_data: dict):
    # function to create sat blueprint
    
    blueprint = {
        "project_info": {
            "sections": ["English R/W Combined"] # Reflect combined structure
        },
        "structure": {
            "english_rw": { 
                "topics": list(set().union(*[
                    test['english_questions']['topics'] for test in all_tests_data.values()
                ])),
                "description": "All Reading and Writing items (Vocabulary, Grammar, Comprehension)"
            }
        },
        "tests": {}
    }
    
    # Add individual test metadata
    for test_num, sections in all_tests_data.items():
        blueprint["tests"][f"Test {test_num}"] = {
            "total_questions": len(sections['english_questions']['passages']),
            "topics": list(sections['english_questions']['topics'])
        }
    
    # Save blueprint
    blueprint_path = BLUEPRINT_DIR / "sat_blueprint.json"
    with open(blueprint_path, 'w', encoding='utf-8') as f:
        json.dump(blueprint, f, indent=2, ensure_ascii=False)
    
    print(f"[OK] SAT blueprint created: {blueprint_path}")
    return blueprint

def process_all_sat_files():
    """Main function to process all SAT files"""
    print("\n" + "="*70)
    print("SAT PREPROCESSING AND CORPUS BUILDING")
    print("="*70 + "\n")
    
    create_sat_directories()
    
    markdown_dir = Path("markdown DS")
    sat_files = sorted(markdown_dir.glob("SAT*.md"))
    
    if not sat_files:
        print("[ERROR] No SAT files found in 'markdown DS' directory!")
        return
    
    print(f"Files: Found {len(sat_files)} SAT test file(s)")
    
    all_tests_data = {}
    
    for sat_file in sat_files:
        # Extract test number from filename
        test_match = re.search(r'test[-_]?(\d+)', sat_file.stem, re.IGNORECASE)
        if not test_match:
            print(f"[WARNING]  Skipping {sat_file.name} - cannot extract test number")
            continue
        
        test_num = int(test_match.group(1))
        
        print(f"\n📚 Processing SAT Test {test_num}...")
        
        # Read content
        content = sat_file.read_text(encoding='utf-8')
        
        # Extract structure
        sections = extract_sat_structure(content, test_num)
        
        all_tests_data[test_num] = sections
        
        # Create corpus files
        create_sat_corpus_files(test_num, sections)
        
        total_extracted_questions = len(sections['english_questions']['passages'])
        print(f"  ✓ Total R/W Questions Extracted: {total_extracted_questions}")
        # Note: We now report the total count, as R/W are combined in the extraction logic.
    
    # Create blueprint
    blueprint = create_sat_blueprint(all_tests_data)
    
    # Summary
    print("\n" + "="*70)
    print("[OK] SAT PREPROCESSING COMPLETE")
    print("="*70)
    print(f"\nSTATUS: Summary:")
    print(f"   * Tests processed: {len(all_tests_data)}")
    print(f"   * Reading topics: {len(blueprint['structure']['reading']['topics'])}")
    print(f"   * Writing topics: {len(blueprint['structure']['writing']['topics'])}")
    print(f"\nOutput: Output:")
    print(f"   * Corpus files: corpus/sat/")
    print(f"   * Blueprint: blueprint/sat_blueprint.json")
    print("="*70)

def main():
    process_all_sat_files()

if __name__ == "__main__":
    CORPUS_DIR = Path("corpus")
    BLUEPRINT_DIR = Path("blueprint")
    SAT_CORPUS_DIR = CORPUS_DIR / "sat"
    main()
