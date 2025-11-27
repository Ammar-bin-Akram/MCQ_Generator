import os
import re
from pathlib import Path

# --- Configuration ---
# You can adjust these markers if your other SAT files have slightly different section headers
START_MARKER = r'^#\s*Reading and Writing'  # Starts after the main R&W header
END_MARKER = r'^#\s*Math'                  # Stops before the main Math header
INPUT_DIR = Path(".")                      # Assumes your .md files are in the same folder as this script
OUTPUT_DIR = Path("filtered_sat_english_only")

def filter_english_content(file_path: Path) -> str:
    """Reads an SAT file and extracts only the Reading and Writing section."""
    print(f"Processing: {file_path.name}")
    content = file_path.read_text(encoding="utf-8")
    lines = content.split('\n')
    
    start_index = -1
    end_index = -1
    
    # 1. Find the start marker
    for i, line in enumerate(lines):
        if re.search(START_MARKER, line):
            start_index = i
            break
            
    # 2. Find the end marker
    # Search starts from the found R&W header to ensure we don't accidentally pick up a math header from previous tests
    for i in range(start_index + 1, len(lines)):
        if re.search(END_MARKER, lines[i]):
            end_index = i
            break

    if start_index == -1:
        print(f"Warning: Start marker not found in {file_path.name}. Skipping.")
        return ""
        
    # If end marker isn't found, assume English content runs to the end (unlikely for a complete test, but safer)
    if end_index == -1:
        print(f"Warning: End marker not found in {file_path.name}. Extracting until EOF.")
        return "\n".join(lines[start_index:])
        
    # 3. Extract the slice and clean up the list
    english_content = lines[start_index:end_index]
    
    # Optional: Prepend a clear header to the final content
    return f"# Reading and Writing (English Section Only)\n\n" + "\n".join(english_content).strip()

def process_all_files():
    """Finds all .md files and processes them."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    markdown_files = list(INPUT_DIR.glob("sat-practice-test-*-digital.md"))
    
    if not markdown_files:
        print(f"No files matching 'sat-practice-test-*-digital.md' found in {INPUT_DIR}")
        return

    print(f"Found {len(markdown_files)} SAT files to process.")
    print("-" * 30)

    for file_path in markdown_files:
        filtered_content = filter_english_content(file_path)
        
        if filtered_content:
            output_file_path = OUTPUT_DIR / file_path.name
            output_file_path.write_text(filtered_content, encoding="utf-8")
            print(f"Successfully filtered and saved to: {output_file_path}")

    print("-" * 30)
    print("Filtering complete. Use the files in the 'filtered_sat_english_only' folder for your RAG pipeline.")

if __name__ == "__main__":
    process_all_files()