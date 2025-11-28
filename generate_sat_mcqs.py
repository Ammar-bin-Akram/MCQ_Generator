"""
Generate SAT-style MCQs using RAG with Google Gemini
- Loads SAT passages and embeddings
- Retrieves relevant passages
- Generates SAT Reading/Writing questions
- Saves to mcq_output/sat/
"""

import json
import faiss
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer
import google.generativeai as genai
import os
from typing import List, Dict

# Directories
INDEX_DIR = Path("index")
MCQ_OUTPUT_DIR = Path("mcq_output") / "sat"
MCQ_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Configuration
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
GEMINI_MODEL = "gemini-2.0-flash"

class SATMCQGenerator:
    """Generate SAT-style MCQs using passages and RAG"""
    
    def __init__(self):
        """Initialize SAT RAG system"""
        print("🚀 Initializing SAT MCQ Generator...")
        
        # Load embedding model
        print(f"📦 Loading embedding model: {EMBEDDING_MODEL}...")
        self.encoder = SentenceTransformer(EMBEDDING_MODEL)
        
        # Load SAT FAISS index
        print("🔍 Loading SAT FAISS index...")
        index_path = INDEX_DIR / "sat_embeddings.faiss"
        if not index_path.exists():
            raise FileNotFoundError(
                "SAT embeddings not found! Run 'create_sat_embeddings.py' first."
            )
        self.index = faiss.read_index(str(index_path))
        print(f"   ✓ Loaded index with {self.index.ntotal} vectors")
        
        # Load SAT passages
        print("📚 Loading SAT passages...")
        passages_path = INDEX_DIR / "sat_passages.json"
        with open(passages_path, 'r', encoding='utf-8') as f:
            self.passages = json.load(f)
        print(f"   ✓ Loaded {len(self.passages)} SAT passages")
        
        # Initialize Google Gemini
        api_key = "" # your api key
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(GEMINI_MODEL)
        print(f"   ✓ Google Gemini API initialized ({GEMINI_MODEL})")
        
        print("✅ SAT RAG system ready!\n")
    
    def retrieve_passage(self, topic: str = None, section_type: str = "reading") -> Dict:
        """
        Retrieve a relevant SAT passage
        
        Args:
            topic: Topic to search for (optional)
            section_type: 'reading' or 'writing'
            
        Returns:
            Selected passage
        """
        if topic:
            # Use semantic search
            query_embedding = self.encoder.encode([topic], normalize_embeddings=True)
            distances, indices = self.index.search(query_embedding, 1)
            passage = self.passages[indices[0][0]]
        else:
            # Random selection from matching section type
            matching = [p for p in self.passages 
                       if p['metadata'].get('section_type') == section_type]
            if not matching:
                matching = self.passages
            import random
            passage = random.choice(matching)
        
        return passage
    
    def generate_reading_mcq_prompt(self, passage: Dict, difficulty: str = "medium") -> str:
        """Create prompt for SAT Reading question"""
        
        prompt = f"""You are an expert SAT test creator. Generate ONE SAT Reading question based on the passage below.

**Passage:**
{passage['content']}

**Passage Topic:** {passage['metadata'].get('topic', 'General')}
**Difficulty Level:** {difficulty}

**Requirements for SAT Reading Question:**
1. Question should test:
   - Main idea/purpose
   - Supporting details
   - Inference
   - Vocabulary in context
   - Author's tone/purpose
   - Text structure/function

2. Provide 4 options (A, B, C, D)
3. Only ONE correct answer
4. Wrong answers should be plausible but clearly incorrect
5. Question should be college-level appropriate
6. Follow SAT question format exactly

**Output Format (JSON only):**
{{
    "question": "The question text (can reference line numbers if needed)",
    "options": {{
        "A": "Option A text",
        "B": "Option B text",
        "C": "Option C text",
        "D": "Option D text"
    }},
    "correct_answer": "A",
    "explanation": "Detailed explanation with evidence from passage",
    "difficulty": "{difficulty}",
    "question_type": "main_idea|detail|inference|vocabulary|purpose",
    "section": "reading"
}}

Generate the SAT Reading question now (JSON only):"""
        
        return prompt
    
    def generate_writing_mcq_prompt(self, passage: Dict, difficulty: str = "medium") -> str:
        """Create prompt for SAT Writing question"""
        
        prompt = f"""You are an expert SAT test creator. Generate ONE SAT Writing and Language question based on the passage below.

**Passage:**
{passage['content']}

**Difficulty Level:** {difficulty}

**Requirements for SAT Writing Question:**
1. Question should test:
   - Grammar and usage
   - Sentence structure
   - Punctuation
   - Rhetorical skills
   - Expression of ideas
   - Standard English conventions

2. Underline a portion of the passage that needs improvement
3. Provide 4 options (A through D)
4. Option A is often "NO CHANGE"
5. Follow SAT Writing format exactly

**Output Format (JSON only):**
{{
    "question": "Which choice most effectively combines the sentences at the underlined portion?",
    "underlined_text": "The exact text from passage that's being questioned",
    "options": {{
        "A": "NO CHANGE",
        "B": "Alternative wording",
        "C": "Another alternative",
        "D": "Third alternative"
    }},
    "correct_answer": "B",
    "explanation": "Why this choice is correct and others are wrong",
    "difficulty": "{difficulty}",
    "question_type": "grammar|punctuation|style|organization",
    "section": "writing"
}}

Generate the SAT Writing question now (JSON only):"""
        
        return prompt
    
    def generate_sat_mcq(self, section_type: str = "reading", 
                         difficulty: str = "medium",
                         topic: str = None) -> Dict:
        """
        Generate a single SAT MCQ
        
        Args:
            section_type: 'reading' or 'writing'
            difficulty: 'easy', 'medium', or 'hard'
            topic: Optional topic to search for
            
        Returns:
            Generated SAT MCQ
        """
        print(f"\n📝 Generating SAT {section_type.upper()} question ({difficulty})")
        
        # Retrieve passage
        print(f"   🔍 Selecting passage...")
        passage = self.retrieve_passage(topic, section_type)
        print(f"   ✓ Selected: {passage['passage_id']}")
        print(f"      Topic: {passage['metadata'].get('topic', 'N/A')}")
        
        # Generate appropriate prompt
        if section_type == "reading":
            prompt = self.generate_reading_mcq_prompt(passage, difficulty)
        else:  # writing
            prompt = self.generate_writing_mcq_prompt(passage, difficulty)
        
        # Call Gemini API
        print(f"   🤖 Generating question with Gemini...")
        try:
            generation_config = {
                "temperature": 0.7,
                "top_p": 0.95,
                "top_k": 40,
                "max_output_tokens": 2048,
            }
            
            response = self.model.generate_content(
                prompt,
                generation_config=generation_config
            )
            
            response_text = response.text
            
            # Extract JSON
            if "```json" in response_text:
                response_text = response_text.split("```json")[1].split("```")[0].strip()
            elif "```" in response_text:
                response_text = response_text.split("```")[1].split("```")[0].strip()
            
            mcq = json.loads(response_text)
            
            # Add metadata
            mcq['passage_id'] = passage['passage_id']
            mcq['passage_content'] = passage['content']
            mcq['generated_with'] = 'RAG-Gemini-SAT'
            
            print(f"   ✅ SAT question generated successfully!")
            return mcq
            
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
            return None
    
    def generate_batch_sat_mcqs(self, num_reading: int = 5, 
                                num_writing: int = 5,
                                difficulty_mix: bool = True) -> List[Dict]:
        """
        Generate multiple SAT questions
        
        Args:
            num_reading: Number of reading questions
            num_writing: Number of writing questions
            difficulty_mix: Mix of difficulties
            
        Returns:
            List of generated SAT MCQs
        """
        all_mcqs = []
        difficulties = ['easy', 'medium', 'hard'] if difficulty_mix else ['medium']
        
        # Generate Reading questions
        print(f"\n{'='*70}")
        print("GENERATING SAT READING QUESTIONS")
        print(f"{'='*70}")
        
        for i in range(num_reading):
            difficulty = difficulties[i % len(difficulties)]
            mcq = self.generate_sat_mcq('reading', difficulty)
            if mcq:
                all_mcqs.append(mcq)
        
        # Generate Writing questions
        print(f"\n{'='*70}")
        print("GENERATING SAT WRITING QUESTIONS")
        print(f"{'='*70}")
        
        for i in range(num_writing):
            difficulty = difficulties[i % len(difficulties)]
            mcq = self.generate_sat_mcq('writing', difficulty)
            if mcq:
                all_mcqs.append(mcq)
        
        return all_mcqs
    
    def save_mcqs(self, mcqs: List[Dict], filename: str = "sat_mcqs.json"):
        """Save SAT MCQs to file"""
        output_path = MCQ_OUTPUT_DIR / filename
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(mcqs, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Saved {len(mcqs)} SAT MCQs to {output_path}")


def main():
    """Main execution"""
    print("="*70)
    print("SAT MCQ GENERATION USING RAG (Google Gemini)")
    print("="*70)
    
    # Initialize SAT generator
    generator = SATMCQGenerator()
    
    # Generate SAT questions
    mcqs = generator.generate_batch_sat_mcqs(
        num_reading=5,      # 3 reading questions
        num_writing=5,      # 3 writing questions
        difficulty_mix=True  # Mix of easy/medium/hard
    )
    
    # Save results
    generator.save_mcqs(mcqs, "sample_sat_mcqs.json")
    
    # Summary
    reading_count = sum(1 for m in mcqs if m.get('section') == 'reading')
    writing_count = sum(1 for m in mcqs if m.get('section') == 'writing')
    
    print(f"\n{'='*70}")
    print("GENERATION COMPLETE")
    print(f"{'='*70}")
    print(f"✅ Total SAT MCQs generated: {len(mcqs)}")
    print(f"   📖 Reading questions: {reading_count}")
    print(f"   ✍️  Writing questions: {writing_count}")
    print(f"📁 Saved to: mcq_output/sat/sample_sat_mcqs.json")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()