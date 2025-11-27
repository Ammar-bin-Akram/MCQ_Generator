import os
import json
import re
from pathlib import Path
from typing import List, Dict, Tuple
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

CHUNK_SIZE = 512  
CHUNK_OVERLAP = 128
EMBEDDING_MODEL = "all-MiniLM-L6-v2" 

BAD_PATTERNS = [
    r'^Example\s*\d*:?\s*',
    r'^Solution\s*:?\s*',
    r'^Example\s+\d+\s+',
    r'^\d+\.\s*Example',
    r'Solution Given',
    r'Example.*:',
    r'^Point to ponder',
    r'^Chastet\s+\d+',
    r'^Proof of',
    r'^\(i\)\s*\$',
    r'^\(a\)\s',
    r'^\(b\)\s',
    r'^\(c\)\s',
    r'^\(d\)\s',
    r'^EXERCISE\s+\d',
]

CONNECTING_PHRASES = [
    "As the", "As $", "Consider", "Let us", "We have", "It has been",
    "Most earthquakes", "Pour some", "The kinetic energy", "Photon must",
    "Maximum uncertainty", "Ozone on", "If there are"
]

class TextChunker:
    
    def __init__(self, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP):
        self.chunk_size = chunk_size
        self.overlap = overlap
        self.blueprint_topics = {}
    
    def load_blueprint_topics(self, blueprint: dict):
        for subject in ["physics", "mathematics"]:
            if subject not in blueprint["structure"]:
                continue
            
            for grade, chapters in blueprint["structure"][subject].items():
                for chapter_key, chapter_data in chapters.items():
                    if isinstance(chapter_data, dict) and "topics" in chapter_data:
                        subject_short = "physics" if subject == "physics" else "math"
                        grade_num = grade.split()[-1]
                        chapter_num = chapter_key.split()[-1]
                        key = f"{subject_short}_{grade_num}_ch{chapter_num}"
                        self.blueprint_topics[key] = set(chapter_data["topics"])
    
    def is_bad_topic(self, topic: str) -> bool:
        for pattern in BAD_PATTERNS:
            if re.search(pattern, topic, re.IGNORECASE):
                return True
        
        if len(topic) > 200:
            return True
        
        bad_keywords = ["todostone", "lodestone", "cosmic rays", "earthquakes are caused"]
        if any(keyword in topic.lower() for keyword in bad_keywords):
            return True
        
        if any(topic.startswith(phrase) for phrase in CONNECTING_PHRASES):
            return True
        
        if topic.endswith("we have") or topic.endswith("we have:"):
            return True
        
        if ". " in topic or topic.endswith("."):
            if not re.match(r'^\d+\.\d+\s+[A-Z]', topic):
                return True
        
        if topic.count(",") > 2:
            return True
        
        if r'\int' in topic or (r'\frac' in topic and len(topic) > 50):
            return True
        
        if topic.startswith('$') and (len(topic) > 80 or topic.count('$') > 4):
            return True
        
        return False
    
    def match_to_blueprint_topic(self, extracted_topic: str, chapter_key: str) -> str:
        if chapter_key not in self.blueprint_topics:
            return "Chapter Content"
        
        valid_topics = self.blueprint_topics[chapter_key]
        
        extracted_clean = re.sub(r'[*_`]', '', extracted_topic).strip()
    
        if extracted_clean in valid_topics:
            return extracted_clean
        
        for valid_topic in valid_topics:
            if extracted_clean.lower() == valid_topic.lower():
                return valid_topic
        
        for valid_topic in valid_topics:
            valid_clean = re.sub(r'[*_`]', '', valid_topic).strip()
            
            if extracted_clean in valid_clean or valid_clean in extracted_clean:
                return valid_topic
            
            if extracted_clean.lower() in valid_clean.lower() or valid_clean.lower() in extracted_clean.lower():
                return valid_topic
        
        for valid_topic in valid_topics:
            extracted_no_num = re.sub(r'^\d+\.?\d*\s*', '', extracted_clean)
            valid_no_num = re.sub(r'^\d+\.?\d*\s*', '', valid_topic)
            
            if extracted_no_num and valid_no_num:
                if extracted_no_num.lower() == valid_no_num.lower():
                    return valid_topic
        
        return "Chapter Content"
    
    def extract_topics_from_content(self, content: str, chapter_key: str) -> List[Tuple[str, int, int]]:
        topics = []
        
        pattern = r'^(#{2,3})\s+(.+?)$'
        
        for match in re.finditer(pattern, content, re.MULTILINE):
            level = len(match.group(1))
            extracted_topic = match.group(2).strip()
            start_pos = match.start()
            
            topic_name = self.match_to_blueprint_topic(extracted_topic, chapter_key)
            
            if topic_name == "Chapter Content" and any(phrase in extracted_topic.lower() for phrase in [
                "tick", "multiple choice", "exercise", "review question", "numerical problem",
                "short question", "long question", "conceptual question"
            ]):
                continue
            
            topics.append((topic_name, level, start_pos))
        
        topics_with_end = []
        for i, (name, level, start) in enumerate(topics):
            if i + 1 < len(topics):
                end = topics[i + 1][2]
            else:
                end = len(content)
            topics_with_end.append((name, level, start, end))
        
        return topics_with_end
    
    def chunk_by_topic(self, content: str, chapter_info: dict) -> List[dict]:
        chapter_key = f"{chapter_info['subject']}_{chapter_info['grade']}_ch{chapter_info['chapter_num']}"
        
        chunks = []
        topics = self.extract_topics_from_content(content, chapter_key)
        
        if not topics:
            return self.chunk_by_sliding_window(content, chapter_info)
        
        chunk_id = 0
        for topic_name, level, start, end in topics:
            topic_content = content[start:end].strip()
            
            if len(topic_content) > self.chunk_size * 4:
                sub_chunks = self.split_large_section(topic_content, topic_name)
                for sub_chunk in sub_chunks:
                    chunks.append({
                        'chunk_id': f"{chapter_info['file_id']}_chunk_{chunk_id}",
                        'content': sub_chunk,
                        'metadata': {
                            'subject': chapter_info['subject'],
                            'grade': chapter_info['grade'],
                            'chapter_num': chapter_info['chapter_num'],
                            'chapter_title': chapter_info['chapter_title'],
                            'topic': topic_name,
                            'topic_level': level,
                            'file': chapter_info['file']
                        }
                    })
                    chunk_id += 1
            else:
                chunks.append({
                    'chunk_id': f"{chapter_info['file_id']}_chunk_{chunk_id}",
                    'content': topic_content,
                    'metadata': {
                        'subject': chapter_info['subject'],
                        'grade': chapter_info['grade'],
                        'chapter_num': chapter_info['chapter_num'],
                        'chapter_title': chapter_info['chapter_title'],
                        'topic': topic_name,
                        'topic_level': level,
                        'file': chapter_info['file']
                    }
                })
                chunk_id += 1
        
        return chunks
    
    def split_large_section(self, text: str, topic_name: str) -> List[str]:
        chunks = []
        words = text.split()
        
        i = 0
        while i < len(words):
            chunk = ' '.join(words[i:i + self.chunk_size])
            chunks.append(chunk)
            i += self.chunk_size - self.overlap
        
        return chunks
    
    def chunk_sat_passage(self, content: str, chapter_info: dict, topic: str, section_type: str) -> List[dict]:
        chunks = []
        
        content_lines = content.split('\n')
        passage_start = 0
        for i, line in enumerate(content_lines):
            if line.startswith('##') and 'Questions' in line:
                passage_start = i
                break
        
        passage_content = '\n'.join(content_lines[passage_start:]) if passage_start > 0 else content
        
        chunk = {
            'chunk_id': f"{chapter_info['file_id']}_full",
            'content': passage_content,
            'metadata': {
                'subject': 'SAT',
                'grade': 'SAT Prep',
                'test_num': chapter_info['chapter_num'],
                'section_type': section_type,
                'topic': topic,
                'file': chapter_info['file'],
                'is_sat_passage': True
            }
        }
        
        chunks.append(chunk)
        return chunks
    
    def chunk_by_sliding_window(self, content: str, chapter_info: dict) -> List[dict]:
        chunks = []
        words = content.split()
        
        chunk_id = 0
        i = 0
        while i < len(words):
            chunk_text = ' '.join(words[i:i + self.chunk_size])
            
            chunks.append({
                'chunk_id': f"{chapter_info['file_id']}_chunk_{chunk_id}",
                'content': chunk_text,
                'metadata': {
                    'subject': chapter_info['subject'],
                    'grade': chapter_info['grade'],
                    'chapter_num': chapter_info['chapter_num'],
                    'chapter_title': chapter_info['chapter_title'],
                    'topic': 'General',
                    'topic_level': 2,
                    'file': chapter_info['file']
                }
            })
            
            chunk_id += 1
            i += self.chunk_size - self.overlap
        
        return chunks

class EmbeddingIndexer:
    
    def __init__(self, model_name: str = EMBEDDING_MODEL):
        print(f"Loading embedding model: {model_name}...")
        self.model = SentenceTransformer(model_name)
        self.dimension = self.model.get_sentence_embedding_dimension()
        print(f"Model loaded (dimension: {self.dimension})")
    
    def create_embeddings(self, chunks: List[dict]) -> np.ndarray:
        print(f"Creating embeddings for {len(chunks)} chunks...")
        
        texts = [chunk['content'] for chunk in chunks]
        embeddings = self.model.encode(texts, show_progress_bar=True, batch_size=32)
        
        return embeddings
    
    def build_faiss_index(self, embeddings: np.ndarray) -> faiss.IndexFlatL2:
        print("Building FAISS index...")
        
        faiss.normalize_L2(embeddings)
        
        index = faiss.IndexFlatL2(self.dimension)
        index.add(embeddings)
        
        print(f"Index built with {index.ntotal} vectors")
        return index

def load_blueprint() -> dict:
    blueprint_path = BLUEPRINT_DIR / "fsc_blueprint.json"
    with open(blueprint_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def process_corpus():
    print("\n" + "="*60)
    print("STEP 2: CHUNKING AND INDEXING")
    print("="*60)
    
    blueprint = load_blueprint()
    chunker = TextChunker()
    
    print("Loading valid topics from blueprint...")
    chunker.load_blueprint_topics(blueprint)
    print(f"Loaded topics for {len(chunker.blueprint_topics)} chapters")
    
    all_chunks = []
    
    print("\nProcessing Physics corpus...")
    physics_dir = CORPUS_DIR / "physics"
    for file_path in sorted(physics_dir.glob("*.md")):
        content = file_path.read_text(encoding='utf-8')
        
        file_id = file_path.stem
        parts = file_id.split('_')
        grade = parts[0].replace('phy', '')
        chapter_num = parts[1].replace('ch', '')
        
        first_line = content.split('\n')[0]
        chapter_title = first_line.replace('#', '').strip()
        if chapter_title.startswith('Chapter'):
            chapter_title = ':'.join(chapter_title.split(':')[1:]).strip()
        
        chapter_info = {
            'file_id': file_id,
            'subject': 'physics',
            'grade': grade,
            'chapter_num': chapter_num,
            'chapter_title': chapter_title,
            'file': file_path.name
        }
        
        chunks = chunker.chunk_by_topic(content, chapter_info)
        all_chunks.extend(chunks)
        print(f"  {file_path.name}: {len(chunks)} chunks")
    
    print("\nProcessing Math corpus...")
    math_dir = CORPUS_DIR / "math"
    for file_path in sorted(math_dir.glob("*.md")):
        content = file_path.read_text(encoding='utf-8')
        
        file_id = file_path.stem
        parts = file_id.split('_')
        grade = parts[0].replace('math', '')
        chapter_num = parts[1].replace('ch', '')
        
        first_line = content.split('\n')[0]
        chapter_title = first_line.replace('#', '').strip()
        if chapter_title.startswith('Chapter'):
            chapter_title = ':'.join(chapter_title.split(':')[1:]).strip()
        
        chapter_info = {
            'file_id': file_id,
            'subject': 'math',
            'grade': grade,
            'chapter_num': chapter_num,
            'chapter_title': chapter_title,
            'file': file_path.name
        }
        
        chunks = chunker.chunk_by_topic(content, chapter_info)
        all_chunks.extend(chunks)
        print(f"  {file_path.name}: {len(chunks)} chunks")
    
    print(f"\nTotal chunks created: {len(all_chunks)}")
    
    sat_dir = CORPUS_DIR / "sat"
    if sat_dir.exists():
        print("\nProcessing SAT corpus...")
        for file_path in sorted(sat_dir.glob("*.md")):
            content = file_path.read_text(encoding='utf-8')
            
            file_id = file_path.stem
            
            parts = file_id.split('_')
            test_num = parts[0].replace('test', '')
            section_type = parts[1] if len(parts) > 1 else 'general'
            
            topic_match = re.search(r'## Topic(?:s)?: (.+)', content)
            topic = topic_match.group(1).strip() if topic_match else "General SAT Content"
            
            chapter_info = {
                'file_id': file_id,
                'subject': 'sat',
                'grade': 'SAT',
                'chapter_num': test_num,
                'chapter_title': f"SAT Test {test_num}",
                'file': file_path.name
            }
            
            chunks = chunker.chunk_sat_passage(content, chapter_info, topic, section_type)
            all_chunks.extend(chunks)
            print(f"  {file_path.name}: {len(chunks)} chunks")
    
    print(f"\nTotal chunks created: {len(all_chunks)}")
    
    return all_chunks

def save_chunks_and_metadata(chunks: List[dict]):
    print("\nSaving chunks and metadata...")
    
    chunks_path = INDEX_DIR / "fsc_chunks.json"
    with open(chunks_path, 'w', encoding='utf-8') as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)
    
    metadata = []
    for chunk in chunks:
        metadata.append({
            'chunk_id': chunk['chunk_id'],
            'metadata': chunk['metadata'],
            'content_preview': chunk['content'][:200] + '...'
        })
    
    metadata_path = INDEX_DIR / "fsc_metadata.json"
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    print(f"  Saved to {chunks_path}")
    print(f"  Saved to {metadata_path}")

def create_chunk_topic_mapping(chunks: List[dict]) -> dict:
    mapping = {}
    
    for chunk in chunks:
        meta = chunk['metadata']
        
        if meta.get('is_sat_passage', False):
            continue
        
        key = f"{meta['subject']}_{meta['grade']}_ch{meta['chapter_num']}"
        
        if key not in mapping:
            mapping[key] = {
                'chapter': meta['chapter_title'],
                'topics': {}
            }
        
        topic = meta['topic']
        if topic not in mapping[key]['topics']:
            mapping[key]['topics'][topic] = []
        
        mapping[key]['topics'][topic].append(chunk['chunk_id'])
    
    return mapping

def update_blueprint_with_chunks(chunks: List[dict]):
    print("\nUpdating blueprint with chunk mappings...")
    
    mapping = create_chunk_topic_mapping(chunks)
    
    mapping_path = INDEX_DIR / "fsc_chunk_topic_mapping.json"
    with open(mapping_path, 'w', encoding='utf-8') as f:
        json.dump(mapping, f, indent=2, ensure_ascii=False)
    
    print(f"  Chunk-topic mapping saved to {mapping_path}")

def main():
    
    chunks = process_corpus()
    
    save_chunks_and_metadata(chunks)
    
    update_blueprint_with_chunks(chunks)
    
    print("\nCreating embeddings and FAISS index (Curriculum only)...")
    curriculum_chunks = [c for c in chunks if not c['metadata'].get('is_sat_passage', False)]
    sat_chunks = [c for c in chunks if c['metadata'].get('is_sat_passage', False)]
    
    print(f"   Curriculum chunks: {len(curriculum_chunks)}")
    print(f"   SAT chunks: {len(sat_chunks)} (will be indexed separately)")
    
    indexer = EmbeddingIndexer()
    embeddings = indexer.create_embeddings(curriculum_chunks)
    
    index = indexer.build_faiss_index(embeddings)
    
    print("\nSaving FAISS index...")
    index_path = INDEX_DIR / "fsc_embeddings.faiss"
    faiss.write_index(index, str(index_path))
    print(f"  Index saved to {index_path}")
    
    embeddings_path = INDEX_DIR / "fsc_embeddings.npy"
    np.save(embeddings_path, embeddings)
    print(f"  Embeddings saved to {embeddings_path}")
    
    print("\n" + "="*60)
    print("INDEXING SUMMARY")
    print("="*60)
    print(f"Total chunks saved: {len(chunks)}")
    print(f"   Curriculum chunks: {len(curriculum_chunks)}")
    print(f"   SAT chunks: {len(sat_chunks)}")
    print(f"Curriculum embeddings: {len(curriculum_chunks)}")
    print(f"Embedding dimension: {indexer.dimension}")
    print(f"Index size: {index.ntotal} vectors")
    print(f"\nFiles created:")
    print(f"   - index/fsc_chunks.json (all chunks)")
    print(f"   - index/fsc_metadata.json (quick lookup)")
    print(f"   - index/fsc_chunk_topic_mapping.json (curriculum topic->chunks)")
    print(f"   - index/fsc_embeddings.faiss (curriculum search index)")
    print(f"   - index/fsc_embeddings.npy (curriculum embeddings)")
    print(f"\nSAT passages saved but not embedded yet.")
    print(f"   Run 'Create SAT Embeddings' (Option 7) to enable SAT question generation.")
    print("="*60)
    print("Chunking & Indexing Complete!")
    print("="*60)


if __name__ == "__main__":
    CORPUS_DIR = Path("corpus")
    BLUEPRINT_DIR = Path("blueprint")
    INDEX_DIR = Path("index")
    main()