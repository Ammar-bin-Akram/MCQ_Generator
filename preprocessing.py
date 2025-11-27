# Preprocessig & Corpus building


import os
import re
from pathlib import Path
import json

# requried diirectories
CORPUS_DIR = Path("corpus")
BLUEPRINT_DIR = Path("blueprint")
INDEX_DIR = Path("index")
MCQ_OUTPUT_DIR = Path("mcq_output")

def create_directory_structure():
    # function to create the requried directories
    directories = [
        CORPUS_DIR / "physics",
        CORPUS_DIR / "math",
        BLUEPRINT_DIR,
        INDEX_DIR,
        MCQ_OUTPUT_DIR,
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
    
    print(" Directory structure created")


def extract_chapters_math_style(content: str, subject: str) -> dict:
    """
    Extract chapters from Math files with structure:
    # 1
    ## Complex Numbers
    ## INTRODUCTION
    ## 1.1 Complex Numbers
    etc.
    """
    chapters = {}
    lines = content.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Look for main chapter number: # 1, # 2, etc.
        chapter_num_match = re.match(r'^#\s*(\d+)\s*$', line)
        
        if chapter_num_match:
            chapter_num = chapter_num_match.group(1)
            
            # Skip empty lines and find the chapter title (## Title)
            j = i + 1
            chapter_title = None
            
            while j < len(lines) and j < i + 5:  # Look ahead max 5 lines
                next_line = lines[j].strip()
                
                # Skip empty lines
                if not next_line:
                    j += 1
                    continue
                
                # Check if it's a chapter title (## Title)
                title_match = re.match(r'^##\s*(.+)$', next_line)
                if title_match:
                    chapter_title = title_match.group(1).strip()
                    break
                
                j += 1
            
            if chapter_title:
                # Collect content until next chapter number
                chapter_content = []
                k = j + 1  # Start after the title line
                
                while k < len(lines):
                    next_line = lines[k].strip()
                    # Stop at next chapter number
                    if re.match(r'^#\s*\d+\s*$', next_line):
                        break
                    chapter_content.append(lines[k])
                    k += 1
                
                # Create chapter
                clean_title = re.sub(r'[^\w\s-]', '', chapter_title)
                clean_title = re.sub(r'\s+', '_', clean_title).lower()
                clean_title = clean_title[:30]
                
                chapter_id = f"{subject.lower()}_ch{chapter_num}_{clean_title}"
                
                chapters[chapter_id] = {
                    'number': chapter_num,
                    'title': chapter_title,
                    'content': f"# Chapter {chapter_num}: {chapter_title}\n\n" + '\n'.join(chapter_content).strip()
                }
                
                print(f"    ✓ Extracted Chapter {chapter_num}: {chapter_title}")
                i = k - 1  # Move to the line before next chapter
        
        i += 1
    
    return chapters
    

def extract_chapters(content: str, subject: str) -> dict:
    # function that extracts single chapters from the cleaned content
    chapters = {}
    
    # trying math style to extract chapters
    chapters = extract_chapters_math_style(content, subject)
    
    if chapters:
        print(f"  ✓ Found {len(chapters)} chapters using Math-style extraction")
        return chapters
    
    # physics style chapter extraction
    pattern1 = r'#{1,2}\s*(Chapter|CHAPTER)\s+(\d+)\s*\n+#{1,3}\s*([^\n]+)'
    
    # math style chapter extraction if the upper one misses any
    pattern2 = r'#\s*(CHAPTER|Chapter)\s*\n+#{1,3}\s*(\d+)\s*\n+#{1,3}\s*([^\n]+)'
    
    matches = list(re.finditer(pattern1, content))
    
    if matches:
        print(f"  ✓ Found {len(matches)} chapters using Pattern 1 (Physics-style)")
    
    if not matches:
        matches = list(re.finditer(pattern2, content))
        if matches:
            print(f"  ✓ Found {len(matches)} chapters using Pattern 2")
    
    # If still no matches, try more flexible pattern
    if not matches:
        pattern3 = r'#{1,3}\s*(?:Chapter|CHAPTER)\s*[:\-]?\s*(\d+)'
        matches = list(re.finditer(pattern3, content))
        if matches:
            print(f"  ✓ Found {len(matches)} chapters using Pattern 3 (flexible)")
    
    for i, match in enumerate(matches):
        # Extract chapter number and title based on which pattern matched
        if len(match.groups()) >= 3:
            chapter_num = match.group(2)
            chapter_title = match.group(3).strip()
        elif len(match.groups()) >= 1:
            chapter_num = match.group(1)
            # Find next line as title
            remaining = content[match.end():].lstrip()
            title_match = re.match(r'#{0,3}\s*([^\n]+)', remaining)
            chapter_title = title_match.group(1).strip() if title_match else f"Chapter {chapter_num}"
        else:
            continue
        
        # Get content from this chapter to the next (or end)
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        chapter_content = content[start:end].strip()
        
        # Clean chapter title for filename
        clean_title = re.sub(r'[^\w\s-]', '', chapter_title)
        clean_title = re.sub(r'\s+', '_', clean_title).lower()
        clean_title = clean_title[:30]  # Limit length
        
        chapter_id = f"{subject.lower()}_ch{chapter_num}_{clean_title}"
        
        chapters[chapter_id] = {
            'number': chapter_num,
            'title': chapter_title,
            'content': f"# Chapter {chapter_num}: {chapter_title}\n\n{chapter_content}"
        }
    
    return chapters

def clean_markdown_content(content: str, subject_hint: str = "") -> str:
    # removing unwanted content like authors, heaers and footers
    
    # Remove everything before first chapter
    # Different patterns for Math vs Physics
    if "math" in subject_hint.lower():
        # Math style: # 1 or # 2
        chapter_pattern = r'(^#\s*\d+\s*$)'
        match = re.search(chapter_pattern, content, re.MULTILINE)
    else:
        # Physics style: # Chapter 1 or ## CHAPTER 1
        chapter_pattern = r'(#{1,2}\s*(?:Chapter|CHAPTER)\s+\d+)'
        match = re.search(chapter_pattern, content)
    
    if match:
        content = content[match.start():]
    
    # Remove author sections
    content = re.sub(r'#\s*Authors?\s*\n.*?(?=\n#|\Z)', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove reviewer sections
    content = re.sub(r'#\s*Reviewers?\s*\n.*?(?=\n#|\Z)', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove editor sections
    content = re.sub(r'#\s*Editors?\s*\n.*?(?=\n#|\Z)', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove table of contents
    content = re.sub(r'#\s*(?:CONTENTS|Contents|Table of Contents|TABLE OF CONTENTS)\s*\n.*?(?=\n#|\Z)', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove copyright and authority sections
    content = re.sub(r'.*?(?:PUNJAB EDUCATION|All rights are reserved|copyright).*?\n', '', content, flags=re.IGNORECASE)
    
    # Remove "In the Name of Allah" sections
    content = re.sub(r'#\s*\(In the Name of.*?\)\s*\n', '', content, flags=re.IGNORECASE)
    
    # Remove bibliography sections at the end
    content = re.sub(r'#\s*Bibliography.*', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove [Image removed] placeholders (multiple variations)
    content = re.sub(r'\[Image removed\]\s*', '', content, flags=re.IGNORECASE)
    content = re.sub(r'\[image removed\]\s*', '', content)
    
    # Remove common noise patterns
    noise_patterns = [
        r'Do you know\?\s*\n',
        r'For [Yy]our [Ii]nformation\s*\n',
        r'For [Yy]our intonation\s*\n',
        r'Interesting Information\s*\n',
        r'Point to [Pp]onder\s*\n',
        r'Challenge:\s*\n',
        r'Try yourself!\s*\n',
        r'Remember!\s*\n',
        r'Note:\s*\n',
        r'Note\s*\n\s*\n',
        r'Solution:\s*\n\s*\n',
        r'Solution\s*\n\s*\n',
        r'Procedure\s*\n\s*\n',
    ]
    
    for pattern in noise_patterns:
        content = re.sub(pattern, '', content, flags=re.IGNORECASE)
    
    # Remove page numbers (standalone numbers on a line)
    content = re.sub(r'^\s*\d{1,3}\s*$', '', content, flags=re.MULTILINE)
    
    # Remove multiple blank lines
    for _ in range(3):
        content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Clean up spaces before newlines
    content = re.sub(r' +\n', '\n', content)
    
    return content.strip()


def process_physics_files():
    # function to process physics books
    print("\n🔬 Processing Physics files...")
    
    source_dir = Path("markdown DS")
    physics_files = ["Physics 11.md", "Physics 12.md"]
    
    all_chapters = {}
    
    for phy_file in physics_files:
        file_path = source_dir / phy_file
        if not file_path.exists():
            print(f"[WARNING] ⚠ {phy_file} not found")
            continue
        
        print(f"  Processing {phy_file}...")
        content = file_path.read_text(encoding='utf-8')
        
        cleaned_content = clean_markdown_content(content, subject_hint="physics")
        
        # Extract chapters
        grade = "11" if "11" in phy_file else "12"
        chapters = extract_chapters(cleaned_content, f"phy{grade}")
        
        # saving each chapter
        for chapter_id, chapter_data in chapters.items():
            output_path = CORPUS_DIR / "physics" / f"{chapter_id}.md"
            output_path.write_text(chapter_data['content'], encoding='utf-8')
            all_chapters[chapter_id] = {
                'subject': 'Physics',
                'grade': grade,
                **chapter_data
            }
            print(f"    ✓ Created {chapter_id}.md")
    
    return all_chapters


def process_math_files():
    # fucntion to process math files
    print("\n📚 Processing Math files...")
    
    source_dir = Path("markdown DS")
    math_files = ["Math 11.md", "Math 12.md"] 
    all_chapters = {}
    
    for math_file in math_files:
        file_path = source_dir / math_file
        if not file_path.exists():
            print(f"[WARNING] ⚠ {math_file} not found")
            continue
        
        print(f"  Processing {math_file}...")
        content = file_path.read_text(encoding='utf-8')

        cleaned_content = clean_markdown_content(content, subject_hint="math")
        
        grade = "11" if "11" in math_file else "12"
        chapters = extract_chapters(cleaned_content, f"math{grade}")
        
        # saving each chapter
        for chapter_id, chapter_data in chapters.items():
            output_path = CORPUS_DIR / "math" / f"{chapter_id}.md"
            output_path.write_text(chapter_data['content'], encoding='utf-8')
            all_chapters[chapter_id] = {
                'subject': 'Mathematics',
                'grade': grade,
                **chapter_data
            }
            print(f"    ✓ Created {chapter_id}.md")
    
    return all_chapters

def extract_topics_from_chapter(content: str) -> list:
    # function extract each topic from the chapter
    topics = []
    
    section_pattern = r'^#{2,3}\s+(.+?)$'
    
    # skipping unwanted words
    skip_keywords = [
        'learning objective', 'introduction', 'summary', 'exercise', 'questions',
        'note', 'solution', 'try yourself', 'remember', 'for your information',
        'interesting information', 'point to ponder', 'challenge', 'do you know',
        'example', 'method', 'proof', 'corollary', 'theorem', 'definition',
        'procedure', 'outline', 'now (', 'general form', 'examples:',
        'salation', 'inspectors', 'fish and other', 'wilson cloud',
        'alpha-proton', 'cunich oude', 'your hair acts', 'a voltmeter',
        'kirchhoff', 'if the wire', 'the moving charge', 'fig.', 'out of page',
        'the current loop', 'a cooper ring', 'the speed of light', 'both xenon',
        'alpha - decay', 'beta-decay', 'emission of', 'an alpha', 'an op amplifier'
    ]
    
    for match in re.finditer(section_pattern, content, re.MULTILINE):
        topic = match.group(1).strip()
        
        if len(topic) < 5 or len(topic) > 100:
            continue
            
        # Skip meta content
        topic_lower = topic.lower()
        if any(skip in topic_lower for skip in skip_keywords):
            continue
        
        if re.match(r'^\d+$', topic):
            continue
        
        if re.match(r'^[A-Z]\s+[A-Z]\s+[A-Z]', topic):
            continue
        
        # Skip if it's mostly special characters or math symbols
        if len(re.findall(r'[^\w\s\-\']', topic)) > len(topic) * 0.3:
            continue
        
        # Skip obvious example/solution markers
        if re.match(r'^\**\s*(solution|example|note|remember|for your).*', topic, re.IGNORECASE):
            continue
        
        topics.append(topic)
    
    return topics



def create_blueprint(all_chapters: dict):
    # function creae blueprint
    print("\n Creating blueprint...")
    
    blueprint = {
        "project_info": {
            "name": "Physics & Mathematics MCQ Generator",
            "grades": ["11", "12"],
            "subjects": ["Physics", "Mathematics"]
        },
        "structure": {
            "physics": {},
            "mathematics": {}
        }
    }
    
    # Organize chapters by subject
    for chapter_id, chapter_info in all_chapters.items():
        subject_key = "physics" if chapter_info['subject'] == 'Physics' else "mathematics"
        grade = f"Grade {chapter_info['grade']}"
        
        if grade not in blueprint['structure'][subject_key]:
            blueprint['structure'][subject_key][grade] = {}
        
        # Extract topics from chapter content
        topics = extract_topics_from_chapter(chapter_info['content'])
        
        blueprint['structure'][subject_key][grade][f"Chapter {chapter_info['number']}"] = {
            "title": chapter_info['title'],
            "file": f"{chapter_id}.md",
            "topics": topics[:15] if len(topics) > 15 else topics  # Limit topics
        }
    
    # Save blueprint as JSON
    json_path = BLUEPRINT_DIR / "blueprint_fsc.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(blueprint, f, indent=2, ensure_ascii=False)
    
    # Create markdown version for easy reading
    md_path = BLUEPRINT_DIR / "blueprint.md"
    markdown_content = generate_blueprint_markdown(blueprint)
    md_path.write_text(markdown_content, encoding='utf-8')
    
    print(f"  ✓ Blueprint saved to {json_path}")
    print(f"  ✓ Blueprint saved to {md_path}")

def generate_blueprint_markdown(blueprint: dict) -> str:
    # function to create markdown of the blueprint
    
    md = "# MCQ Generation Blueprint\n\n"
    md += "## Project Information\n\n"
    md += f"**Name:** {blueprint['project_info']['name']}\n\n"
    md += f"**Grades:** {', '.join(blueprint['project_info']['grades'])}\n\n"
    md += f"**Subjects:** {', '.join(blueprint['project_info']['subjects'])}\n\n"
    md += "---\n\n"
    
    for subject, grades in blueprint['structure'].items():
        md += f"# {subject.upper()}\n\n"
        
        for grade, chapters in grades.items():
            md += f"## {grade}\n\n"
            
            for chapter_name, chapter_info in chapters.items():
                md += f"### {chapter_name}: {chapter_info['title']}\n\n"
                md += f"**File:** `{chapter_info['file']}`\n\n"
                md += "**Topics:**\n\n"
                
                for topic in chapter_info['topics']:
                    md += f"- {topic}\n"
                
                md += "\n"
        
        md += "---\n\n"
    
    return md


def main():
    """Main execution function"""
    print("="*60)
    print("STEP 1: PREPROCESSING & CORPUS BUILDING")
    print("="*60)
    
    create_directory_structure()
    
    physics_chapters = process_physics_files()
    math_chapters = process_math_files()
    
    all_chapters = {**physics_chapters, **math_chapters}
    
    create_blueprint(all_chapters)
    


if __name__ == "__main__":
    main()
