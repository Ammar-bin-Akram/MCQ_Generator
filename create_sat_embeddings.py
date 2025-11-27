# File to creating SAT embeddings

import json
import re
from pathlib import Path
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

def load_sat_passages():
    # function load all the content for SAT
    passages = []
    
    chunks_file = INDEX_DIR / "fsc_chunks.json"
    if not chunks_file.exists():
        print(f"[ERROR] chunks.json not found. Please run 'Chunk & Index Corpus' (Option 3) first.")
        return passages
    
    print(f"Files: Loading SAT passages from chunks.json...")
    
    with open(chunks_file, 'r', encoding='utf-8') as f:
        all_chunks = json.load(f)
    
    # filtering only SAT passages
    sat_passages = [c for c in all_chunks if c['metadata'].get('is_sat_passage', False)]
    
    if not sat_passages:
        print(f"[ERROR] No SAT passages found in chunks. Please run SAT preprocessing (Option 5) and chunking (Option 3) first.")
        return passages
    
    print(f"[OK] Found {len(sat_passages)} SAT passages")
    
    # making passage format
    for chunk in sat_passages:
        meta = chunk['metadata']
        passages.append({
            'passage_id': chunk['chunk_id'],
            'content': chunk['content'],
            'metadata': meta
        })
    
    print(f"Loaded {len(passages)} SAT passages")
    return passages

def create_sat_embeddings():
    # function for creating embeddings for SAT passages
    print("\n" + "="*70)
    print("CREATING SAT EMBEDDINGS FOR RAG")
    print("="*70 + "\n")
    
    passages = load_sat_passages()
    
    if not passages:
        print("No SAT passages found. Please run SAT preprocessing first.")
        return
    
    print(f"[SETUP] Loading embedding model: {EMBEDDING_MODEL}")
    model = SentenceTransformer(EMBEDDING_MODEL)
    
    # creating embeddings
    print(f"Loading: Creating embeddings for {len(passages)} passages...")
    passage_texts = [p['content'] for p in passages]
    embeddings = model.encode(passage_texts, show_progress_bar=True, batch_size=32)
    
    # normalizing embeddings
    print("Normalizing embeddings...")
    faiss.normalize_L2(embeddings)
    
    # creating FAISS index
    print("Building FAISS index...")
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings.astype('float32'))

    print("Saving: Saving SAT embeddings and index...")
    
    sat_passages_file = INDEX_DIR / "sat_passages.json"
    with open(sat_passages_file, 'w', encoding='utf-8') as f:
        json.dump(passages, f, indent=2, ensure_ascii=False)
    
    sat_embeddings_file = INDEX_DIR / "sat_embeddings.npy"
    np.save(sat_embeddings_file, embeddings)

    sat_index_file = INDEX_DIR / "sat_embeddings.faiss"
    faiss.write_index(index, str(sat_index_file))
    
    
    # Breakdown by section
    reading_count = sum(1 for p in passages if p['metadata'].get('section_type') == 'reading')
    writing_count = sum(1 for p in passages if p['metadata'].get('section_type') == 'writing')
    
    print(f" Type Breakdown:")
    print(f"   * Reading passages: {reading_count}")
    print(f"   * Writing passages: {writing_count}")
    
    print(f"Output Files:")
    print(f"   * {sat_passages_file}")
    print(f"   * {sat_embeddings_file}")
    print(f"   * {sat_index_file}")

if __name__ == "__main__":
    # Directories
    CORPUS_DIR = Path("corpus")
    INDEX_DIR = Path("index")

    # Configuration
    EMBEDDING_MODEL = "all-MiniLM-L6-v2"
    create_sat_embeddings()
