# Creating a valid_chunk_ids json file to validate citations

import json

output_path = "index/valid_chunk_ids.json"

with open("index/fsc_chunk_topic_mapping.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract all chunk IDs
valid_chunk_ids = set()
for chapter_id, chapter_info in data.items():
    topics = chapter_info.get("topics", {})
    for topic_name, chunks in topics.items():
        for chunk_id in chunks:
            valid_chunk_ids.add(chunk_id)

valid_chunk_ids_list = list(valid_chunk_ids)

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(valid_chunk_ids_list, f, indent=2, ensure_ascii=False)

print(f"Saved {len(valid_chunk_ids_list)} valid chunk IDs to {output_path}")