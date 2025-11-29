"""
Generate MCQs using RAG with Google Gemini
- Loads FAISS index and chunks
- Retrieves relevant content based on topic
- Uses Google Gemini API to generate MCQs
- Saves to mcq_output/
"""

import json
import faiss
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer
import google.generativeai as genai
import os
from dotenv import load_dotenv
from typing import List, Dict
import re
import random

from validation import CurriculumMCQValidator
from adaptive_module import AdaptiveEngine
from phy_validation import MCQValidator

load_dotenv()

# Directories
INDEX_DIR = Path("index")
MCQ_OUTPUT_DIR = Path("mcq_output")
MCQ_OUTPUT_DIR.mkdir(exist_ok=True)

# Configuration
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
TOP_K = 3  # Number of chunks to retrieve
GEMINI_MODEL = "gemini-2.0-flash"  # or "gemini-1.5-flash" for faster responses


DIFFICULTY_MAP = {
        "easy": -1.0,
        "medium": 0.0,
        "hard": +1.0
    }

class RAGMCQGenerator:
    """Generate MCQs using Retrieval-Augmented Generation with Google Gemini"""
    
    def __init__(self):
        """Initialize RAG system"""
        print("🚀 Initializing RAG MCQ Generator...")
        
        # Load embedding model
        print(f"📦 Loading embedding model: {EMBEDDING_MODEL}...")
        self.encoder = SentenceTransformer(EMBEDDING_MODEL)
        
        # Load FAISS index
        print("🔍 Loading FAISS index...")
        index_path = INDEX_DIR / "fsc_embeddings.faiss"
        self.index = faiss.read_index(str(index_path))
        print(f"   ✓ Loaded index with {self.index.ntotal} vectors")
        
        # Load chunks
        print("📚 Loading chunks...")
        chunks_path = INDEX_DIR / "fsc_chunks.json"
        with open(chunks_path, 'r', encoding='utf-8') as f:
            self.chunks = json.load(f)
        print(f"   ✓ Loaded {len(self.chunks)} chunks")
        
        # Initialize Google Gemini
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(GEMINI_MODEL)
        print(f"   ✓ Google Gemini API initialized ({GEMINI_MODEL})")
        
        print("✅ RAG system ready!\n")


    def estimate_difficulty(self, mcq: Dict) -> str:
        """
        Estimate MCQ difficulty based ONLY on question content (no topic bias)
        
        Args:
            mcq: Generated MCQ
            
        Returns:
            'easy', 'medium', or 'hard'
        """
        score = 0
        
        question = mcq.get('question', '')
        options = mcq.get('options', {})
        
        # Combine all text for analysis
        all_text = question + ' '.join(options.values())
        question_lower = question.lower()
        
        # ========================================
        # 1. COGNITIVE COMPLEXITY INDICATORS
        # ========================================
        
        # Bloom's Taxonomy - Higher order thinking
        high_order_verbs = [
            'analyze', 'evaluate', 'synthesize', 'derive', 'prove', 
            'compare', 'contrast', 'justify', 'critique', 'design',
            'formulate', 'hypothesize', 'deduce', 'infer'
        ]
        mid_order_verbs = [
            'apply', 'calculate', 'demonstrate', 'solve', 'determine',
            'classify', 'explain', 'interpret', 'relate', 'use'
        ]
        low_order_verbs = [
            'define', 'list', 'name', 'state', 'identify', 'recall',
            'recognize', 'select', 'what is', 'which of the following'
        ]
        
        if any(verb in question_lower for verb in high_order_verbs):
            score += 3
        elif any(verb in question_lower for verb in mid_order_verbs):
            score += 1
        elif any(verb in question_lower for verb in low_order_verbs):
            score -= 2
        
        # ========================================
        # 2. MULTI-STEP REASONING
        # ========================================
        
        multi_step_indicators = [
            'first', 'then', 'next', 'subsequently', 'finally',
            'step 1', 'step 2', 'given that', 'if.*then',
            'assuming', 'suppose', 'consider the case'
        ]
        
        multi_step_count = sum(1 for indicator in multi_step_indicators 
                            if re.search(indicator, question_lower))
        
        if multi_step_count >= 3:
            score += 3
        elif multi_step_count == 2:
            score += 2
        elif multi_step_count == 1:
            score += 1
        
        # ========================================
        # 3. MATHEMATICAL/COMPUTATIONAL COMPLEXITY
        # ========================================
        
        math_symbols = {
            'advanced': ['∫', '∑', '∏', '∂', '∇', 'lim', 'log', 'ln', '∞', '\\int', '\\sum', '\\lim'],
            'intermediate': ['²', '³', '√', 'π', 'sin', 'cos', 'tan', '\\sqrt', '\\frac']
        }
        
        advanced_math_count = sum(1 for symbol in math_symbols['advanced'] 
                                if symbol in all_text)
        intermediate_math_count = sum(1 for symbol in math_symbols['intermediate'] 
                                    if symbol in all_text)
        
        score += min(advanced_math_count * 2, 4)  # Cap at +4
        score += min(intermediate_math_count, 2)   # Cap at +2
        
        # LaTeX complexity
        latex_patterns = [
            r'\\frac{.*?}{.*?}',      # Fractions
            r'\\int.*?d[x-z]',        # Integrals
            r'\\sum',                  # Summations
            r'\\sqrt\[.*?\]',          # Roots
            r'\^{.*?}',                # Exponents
        ]
        
        latex_complexity = sum(1 for pattern in latex_patterns 
                            if re.search(pattern, all_text))
        score += min(latex_complexity, 3)
        
        # ========================================
        # 4. NUMERICAL COMPLEXITY
        # ========================================
        
        numbers = re.findall(r'\d+\.?\d*', all_text)
        
        # Scientific notation or large numbers
        try:
            if any(float(n) > 1000 or float(n) < 0.001 for n in numbers if n and float(n) != 0):
                score += 1
        except:
            pass
        
        # Decimal operations
        decimals = [n for n in numbers if '.' in n]
        if len(decimals) > 2:
            score += 1
        
        # Multiple numerical values
        if len(numbers) > 5:
            score += 2
        elif len(numbers) > 3:
            score += 1
        
        # ========================================
        # 5. QUESTION LENGTH & COMPLEXITY
        # ========================================
        
        question_words = len(question.split())
        
        if question_words > 40:
            score += 2
        elif question_words > 25:
            score += 1
        elif question_words < 10:
            score -= 1
        
        # Sentence complexity
        clauses = question.count(',') + question.count(';') + question.count(':')
        if clauses > 3:
            score += 1
        
        # ========================================
        # 6. OPTIONS COMPLEXITY
        # ========================================
        
        option_lengths = [len(opt.split()) for opt in options.values()]
        avg_option_length = sum(option_lengths) / len(option_lengths) if option_lengths else 0
        
        if avg_option_length > 20:
            score += 2
        elif avg_option_length > 12:
            score += 1
        elif avg_option_length < 3:
            score -= 1
        
        # Options similarity (harder if very similar)
        option_texts = list(options.values())
        similar_pairs = 0
        
        for i in range(len(option_texts)):
            for j in range(i+1, len(option_texts)):
                words_i = set(option_texts[i].lower().split())
                words_j = set(option_texts[j].lower().split())
                
                if len(words_i) > 0 and len(words_j) > 0:
                    overlap = len(words_i & words_j) / max(len(words_i), len(words_j))
                    if overlap > 0.5:
                        similar_pairs += 1
        
        if similar_pairs >= 2:
            score += 2
        elif similar_pairs == 1:
            score += 1
        
        # ========================================
        # 7. CONCEPTUAL DEPTH INDICATORS
        # ========================================
        
        abstract_indicators = [
            'relationship', 'principle', 'theory', 'concept', 'implication',
            'consequence', 'effect', 'cause', 'mechanism', 'process'
        ]
        
        abstract_count = sum(1 for indicator in abstract_indicators 
                            if indicator in question_lower)
        score += min(abstract_count, 2)
        
        # Conditional/hypothetical reasoning
        conditional_indicators = ['if', 'when', 'suppose', 'assume', 'given', 'provided']
        conditional_count = sum(1 for indicator in conditional_indicators 
                            if indicator in question_lower)
        
        if conditional_count >= 2:
            score += 1
        
        # ========================================
        # 8. PENALTY FOR SIMPLICITY
        # ========================================
        
        direct_patterns = [
            r'^what is the',
            r'^which of the following is',
            r'^select the',
            r'^identify the',
            r'^name the'
        ]
        
        if any(re.search(pattern, question_lower) for pattern in direct_patterns):
            score -= 1
        
        # True/False embedded
        if 'true' in question_lower and 'false' in question_lower:
            score -= 1
        
        # ========================================
        # FINAL DIFFICULTY MAPPING
        # ========================================
        
        if score <= 1:
            return 'easy'
        elif score <= 5:
            return 'medium'
        else:
            return 'hard'
    
    def retrieve_relevant_chunks(self, query: str, top_k: int = TOP_K) -> List[Dict]:
        """
        Retrieve most relevant chunks using FAISS
        
        Args:
            query: Search query (e.g., "Newton's laws of motion")
            top_k: Number of chunks to retrieve
            
        Returns:
            List of relevant chunks with metadata
        """
        # Encode query
        query_embedding = self.encoder.encode([query], normalize_embeddings=True)
        
        # Search FAISS index
        distances, indices = self.index.search(query_embedding, top_k)
        
        # Retrieve chunks
        relevant_chunks = []
        for idx, distance in zip(indices[0], distances[0]):
            if idx < len(self.chunks):  # Validate index
                chunk = self.chunks[idx].copy()
                chunk['similarity_score'] = float(1 - distance)  # Convert distance to similarity
                relevant_chunks.append(chunk)
        
        return relevant_chunks
    
    def generate_mcq_prompt(self, chunks: List[Dict], topic: str, difficulty: str = "medium") -> str:
        """
        Create prompt for Gemini to generate MCQ
        
        Args:
            chunks: Retrieved relevant chunks
            topic: Topic name
            difficulty: easy/medium/hard
            
        Returns:
            Formatted prompt for Gemini
        """
        # Combine chunk content
        context = "\n\n---\n\n".join([
            f"**Source {i+1}:** {chunk['metadata']['chapter_title']} - {chunk['metadata'].get('topic', 'N/A')}\n{chunk['content']}"
            for i, chunk in enumerate(chunks)
        ])
        
        prompt = f"""You are an expert educational content creator for FSc (Grade 11-12) Physics and Mathematics in Pakistan.

**Task:** Generate ONE high-quality Multiple Choice Question (MCQ) based on the provided content.

**Topic:** {topic}
**Difficulty Level:** {difficulty}

**Content to use:**
{context}

**Requirements:**
1. Create a clear, unambiguous question
2. Provide 4 options (A, B, C, D)
3. Mark the correct answer
4. Provide a detailed explanation
5. Ensure the question tests understanding, not just memorization
6. Use proper mathematical notation where needed
7. Make distractors (wrong answers) plausible but clearly incorrect
8. Add one or multiple distractors that are meant to confuse students

**Output Format (JSON only, no markdown):**
{{
    "question": "The question text here",
    "options": {{
        "A": "Option A text",
        "B": "Option B text",
        "C": "Option C text",
        "D": "Option D text"
    }},
    "correct_answer": "A",
    "distractors": ["B", "C"],
    "explanation": "Detailed explanation of why the answer is correct",
    "difficulty": "{difficulty}",
    "topic": "{topic}",
    "chapter": "Chapter name from context"
}}

Generate the MCQ now (respond with only the JSON, no additional text):"""
        
        return prompt
    
    def generate_mcq(self, topic: str, difficulty: str = None, subject: str = None) -> Dict:
        """
        Generate a single MCQ for a given topic
        
        Args:
            topic: Topic to generate MCQ for
            difficulty: Requested difficulty (used for prompt, not final label)
            subject: physics/math (optional, for filtering)
            
        Returns:
            Generated MCQ as dictionary
        """
        # Use medium as default for generation prompt
        requested_difficulty = difficulty if difficulty else "medium"
        
        print(f"\n📝 Generating MCQ for: {topic}")
        
        # Create search query
        query = topic
        if subject:
            query = f"{subject} {topic}"
        
        # Retrieve relevant chunks
        print(f"   🔍 Searching for relevant content...")
        chunks = self.retrieve_relevant_chunks(query)
        
        if not chunks:
            print(f"   ⚠️  No relevant content found for '{topic}'")
            return None
        
        print(f"   ✓ Retrieved {len(chunks)} relevant chunks")
        for i, chunk in enumerate(chunks[:3]):
            print(f"      {i+1}. {chunk['metadata']['chapter_title']} - Score: {chunk['similarity_score']:.3f}")
        
        # Generate prompt (using requested difficulty as hint)
        prompt = self.generate_mcq_prompt(chunks, topic, requested_difficulty)
        
        # Call Gemini API
        print(f"   🤖 Generating MCQ with Gemini...")
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
            
            # Parse response
            response_text = response.text
            print(response_text)
            
            if "```json" in response_text:
                response_text = response_text.split("```json")[1].split("```")[0].strip()
            elif "```" in response_text:
                response_text = response_text.split("```")[1].split("```")[0].strip()
            
            mcq = json.loads(response_text)
            
            # ✅ CALCULATE ACTUAL DIFFICULTY BASED ON CONTENT
            calculated_difficulty = self.estimate_difficulty(mcq)
            
            # Add metadata
            mcq['source_chunks'] = [chunk['chunk_id'] for chunk in chunks[:3]]
            mcq['generated_with'] = 'RAG-Gemini'
            mcq['requested_difficulty'] = requested_difficulty  # What we asked for
            mcq['difficulty'] = calculated_difficulty  # What it actually is
            
            # Show if there's a mismatch
            if calculated_difficulty != requested_difficulty:
                print(f"   i  Difficulty adjusted: {requested_difficulty} → {calculated_difficulty}")
            
            print(f"   ✅ MCQ generated - Difficulty: {calculated_difficulty}")
            return mcq
            
        except Exception as e:
            print(f"   ❌ Error generating MCQ: {str(e)}")
            return None
    
    def generate_batch_mcqs(self, topics: List[str], num_per_topic: int = 3, 
                           difficulty_mix: bool = True) -> List[Dict]:
        """
        Generate multiple MCQs for multiple topics
        
        Args:
            topics: List of topics
            num_per_topic: Number of MCQs per topic
            difficulty_mix: If True, generate mix of difficulties
            
        Returns:
            List of generated MCQs
        """
        all_mcqs = []
        difficulties = ['easy', 'medium', 'hard'] if difficulty_mix else ['medium']
        
        for topic in topics:
            print(f"\n{'='*70}")
            print(f"Topic: {topic}")
            print(f"{'='*70}")
            
            for i in range(num_per_topic):
                difficulty = difficulties[i % len(difficulties)] if difficulty_mix else 'medium'
                
                mcq = self.generate_mcq(topic, difficulty)
                if mcq:
                    all_mcqs.append(mcq)
        
        return all_mcqs
    
    def save_mcqs(self, mcqs: List[Dict], filename: str = "generated_mcqs.json"):
        """Save generated MCQs to file"""
        output_path = MCQ_OUTPUT_DIR / filename
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(mcqs, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Saved {len(mcqs)} MCQs to {output_path}")


    def load_all_topics_from_blueprint(self) -> List[str]:
        """Load all topics from the blueprint"""
        blueprint_path = Path("blueprint") / "blueprint_fsc.json"
        
        if not blueprint_path.exists():
            print(f"   ⚠️  Blueprint not found at {blueprint_path}")
            return []
        
        with open(blueprint_path, 'r', encoding='utf-8') as f:
            blueprint = json.load(f)
        
        all_topics = []
        
        # Navigate to the 'structure' key first
        if 'structure' not in blueprint:
            print(f"   ⚠️  'structure' key not found in blueprint")
            return []
        
        structure = blueprint['structure']
        
        # Iterate through subjects (physics, mathematics)
        for subject_name, subject_data in structure.items():
            print(f"   📖 Processing {subject_name}...")
            
            # Iterate through grades (Grade 11, Grade 12)
            for grade_name, grade_data in subject_data.items():
                print(f"      📚 {grade_name}...")
                
                # Iterate through chapters
                for chapter_num, chapter_data in grade_data.items():
                    
                    # Get topics list
                    topics_list = chapter_data.get('topics', [])
                    
                    # Add all topics from this chapter
                    for topic in topics_list:
                        if topic and isinstance(topic, str):
                            # Clean up topic names (remove markdown, special chars)
                            cleaned_topic = topic.strip()
                            # Remove numbering like "12.1", "3.1.1", etc.
                            cleaned_topic = ' '.join(cleaned_topic.split()[1:]) if cleaned_topic.split()[0].replace('.', '').isdigit() else cleaned_topic
                            # Remove markdown bold/italic
                            cleaned_topic = cleaned_topic.replace('**', '').replace('*', '')
                            # Remove parentheses indicators like (i), (ii), etc.
                            if cleaned_topic and not cleaned_topic.startswith('('):
                                all_topics.append(cleaned_topic)
        
        # Remove duplicates and empty strings
        all_topics = [t for t in set(all_topics) if t.strip()]
        
        return all_topics

    
    def generate_random_mcqs(self, num_questions: int = 20, 
                        difficulty_mix: bool = True,
                        subject_filter: str = None) -> List[Dict]:
        """
        Generate MCQs from randomly selected topics
        
        Args:
            num_questions: Number of MCQs to generate
            difficulty_mix: If True, mix easy/medium/hard
            subject_filter: 'physics' or 'math' to filter by subject (optional)
            
        Returns:
            List of generated MCQs
        """
        print(f"\n🎲 Generating {num_questions} random MCQs...")
        
        # Load all topics from blueprint
        print("📚 Loading topics from blueprint...")
        all_topics = self.load_all_topics_from_blueprint()
        
        if not all_topics:
            print("   ❌ No topics found in blueprint!")
            return []
        
        print(f"   ✓ Found {len(all_topics)} unique topics")
        
        # Filter by subject if specified
        if subject_filter:
            # Filter chunks by subject to get relevant topics
            subject_chunks = [c for c in self.chunks 
                            if c['metadata'].get('subject', '').lower() == subject_filter.lower()]
            subject_topics = set()
            for chunk in subject_chunks:
                topic = chunk['metadata'].get('topic', '')
                if topic:
                    subject_topics.add(topic)
            
            # Filter all_topics to only include those from the subject
            all_topics = [t for t in all_topics if any(st in t.lower() for st in 
                        [topic.lower() for topic in subject_topics])]
            
            print(f"   ✓ Filtered to {len(all_topics)} {subject_filter} topics")
        
        # Randomly select topics
        
        num_to_select = min(num_questions, len(all_topics))
        selected_topics = random.sample(all_topics, num_to_select)
        
        print(f"   🎯 Selected {num_to_select} random topics")
        
        # Generate MCQs
        mcqs = []
        difficulties = ['easy', 'medium', 'hard'] if difficulty_mix else ['medium']
        
        for i, topic in enumerate(selected_topics):
            difficulty = difficulties[i % len(difficulties)] if difficulty_mix else 'medium'
            
            print(f"\n{'='*70}")
            print(f"[{i+1}/{num_to_select}] Topic: {topic}")
            print(f"{'='*70}")
            
            mcq = self.generate_mcq(topic, difficulty)
            if mcq:
                mcqs.append(mcq)


        if mcqs:
            difficulty_counts = {'easy': 0, 'medium': 0, 'hard': 0}
            for mcq in mcqs:
                diff = mcq.get('difficulty', 'medium')
                difficulty_counts[diff] = difficulty_counts.get(diff, 0) + 1
            
            print(f"\n{'='*70}")
            print("📊 ACTUAL DIFFICULTY DISTRIBUTION")
            print(f"{'='*70}")
            for diff in ['easy', 'medium', 'hard']:
                count = difficulty_counts[diff]
                percentage = (count / len(mcqs)) * 100 if mcqs else 0
                bar = '█' * int(percentage / 5)  # Visual bar
                print(f"   {diff.capitalize():8} : {count:2} ({percentage:5.1f}%) {bar}")
        print(f"{'='*70}")
        
        return mcqs


    def run_adaptive_session(
        self,
        rag_generator,             # your existing MCQ generator class/function
        num_questions=5,
        initial_theta=0.0
    ):
        """
        Runs a full adaptive MCQ session using:
            - theta updates
            - difficulty control
            - topic balancing

        rag_generator(topic, difficulty) MUST return dict:
            {
                "question": str,
                "options": { "A": "...", "B": "...", "C": "...", "D": "..." },
                "correct_answer": "A",
                "difficulty": "medium",
                "topic": "...",
                ... other fields ...
            }
        """

        engine = AdaptiveEngine()
        history = []
        available_topics = self.load_all_topics_from_blueprint()

        for i in range(num_questions):

            # ------------------------------------------
            # 1) Decide difficulty + topic using adaptive engine
            # ------------------------------------------
            spec = engine.get_next_question_spec(available_topics)
            topic = spec["topic"]
            difficulty = spec["difficulty"]

            print(f"\n===============================")
            print(f" Question {i+1}/{num_questions}")
            print(f" Topic: {topic}")
            print(f" Difficulty: {difficulty}")
            print(f" θ (before): {round(engine.theta, 3)}")
            print(f"===============================")

            # ------------------------------------------
            # 2) Generate the MCQ using RAG
            # ------------------------------------------
            mcq = rag_generator.generate_mcq(topic, difficulty)

            question_text = mcq["question"]
            options = mcq["options"]          # dict {"A": "...", "B": "..."}
            correct_letter = mcq["correct_answer"]
            correct_text = options[correct_letter]

            # ------------------------------------------
            # 3) Display question
            # ------------------------------------------
            print("\n" + question_text)
            for key, val in options.items():
                print(f"{key}. {val}")

            # ------------------------------------------
            # 4) Take student input
            # ------------------------------------------
            user_input = input("\nYour answer (A, B, C, D): ").strip().upper()

            if user_input not in options:
                print("Invalid answer. Marked incorrect.")
                user_input = None

            result = 1 if user_input == correct_letter else 0

            if result == 1:
                print("Correct!")
            else:
                print(f"Incorrect. Correct answer: {correct_letter}. {correct_text}")

            # ------------------------------------------
            # 5) Update θ based on result
            # ------------------------------------------
            difficulty_value = DIFFICULTY_MAP[difficulty]
            new_theta = engine.update_theta(difficulty_value, result)

            print(f"Updated θ = {round(new_theta, 3)}")

            # ------------------------------------------
            # 6) Save all details to history
            # ------------------------------------------
            history.append({
                "question": question_text,
                "options": options,
                "correct_answer": correct_letter,
                "chosen_answer": user_input,
                "result": result,
                "difficulty_requested": difficulty,
                "topic": topic,
                "theta_after": new_theta,
                "mcq_metadata": mcq  # keeps chapter, source_chunks, etc.
            })

        return history
    

def main():
    """Main execution with validation for Math and Physics"""
    print("="*70)
    print("MCQ GENERATION & VALIDATION (Math + Physics)")
    print("="*70)

    # Initialize RAG system
    generator = RAGMCQGenerator()
    
    # ✅ Import CURRICULUM validator (not SAT validator)

    # Load source chunks JSON
    with open("index/valid_chunk_ids.json", "r", encoding="utf-8") as f:
        valid_chunk_ids = json.load(f)
    
    # validator = CurriculumMCQValidator()
    validator = MCQValidator(valid_chunk_ids)

    # adaptive_engine = AdaptiveMCQEngine()
    results = generator.run_adaptive_session(generator)

    # Save adaptive session results
    adaptive_output_path = MCQ_OUTPUT_DIR / "adaptive_session_results.json"

    with open(adaptive_output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\n💾 Saved adaptive session results to {adaptive_output_path}")
    
    # ========== GENERATE PHYSICS MCQs ==========
    
    print("\n" + "="*70)
    print("PHASE 1: GENERATING PHYSICS MCQs")
    print("="*70)
    
    # physics_mcqs = generator.generate_random_mcqs(             *
    #     num_questions=15,
    #     difficulty_mix=True,
    #     subject_filter='physics'
    # )
    
    # Save physics MCQs
    # generator.save_mcqs(physics_mcqs, "physics_mcqs.json")                            *
    
    # Validate physics MCQs
    # if physics_mcqs:
    #     print("\n" + "="*70)
    #     print("VALIDATING PHYSICS MCQs")
    #     print("="*70)
    #     physics_report = validator.validate_batch(physics_mcqs)
    #     validator.save_validation_report(
    #         physics_report, 
    #         MCQ_OUTPUT_DIR / "physics_validation_report_test.json"
    #     )

    # Build mapping: chunk_id -> content

    # batch_report = []
    # for mcq in physics_mcqs:
    #     mcq_chunk_ids = mcq.get("source_chunks", [])

    #     report = validator.validate_mcq(
    #         question=mcq["question"],
    #         correct_answer=mcq["correct_answer"],
    #         distractors=mcq["distractors"],
    #         mcq_chunk_ids=mcq_chunk_ids,
    #         math_question=mcq.get("math_question"),
    #         user_answer=mcq.get("user_answer")
    #     )
    #     batch_report.append({
    #         "question": mcq["question"],
    #         "validation": report
    #     })                                                                                *
    
    # output_path = Path(MCQ_OUTPUT_DIR / "physics_validation_report_test.json")
    # validator.save_validation_report(batch_report, output_path)                               *

    # if math_mcqs:
        # print(f"\nMath Validation:")
        # print(f"   Pass Rate: {math_report['pass_rate']:.1f}%")
        # print(f"   Avg Quality: {math_report['average_quality_score']}/100")
    
    print(f"\nFiles Created:")
    print(f"   - mcq_output/physics_mcqs.json")
    print(f"   - mcq_output/physics_validation_report.json")
    print(f"   - mcq_output/math_mcqs.json")
    print(f"   - mcq_output/math_validation_report.json")
    
    print("\n" + "="*70)
    print("PROCESS COMPLETE!")
    print("="*70)


if __name__ == "__main__":
    main()