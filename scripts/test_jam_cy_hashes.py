# -*- coding: utf-8 -*-
import sys
import json
import zipfile
import hashlib
import re

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def compute_question_hash(text):
    norm = re.sub(r'\s+', ' ', text.strip().lower())
    return hashlib.sha256(norm.encode('utf-8')).hexdigest()[:16]

with open('seen_question_hashes.json', 'r', encoding='utf-8') as f:
    seen = json.load(f)

print(f"Total existing hashes in seen_question_hashes.json: {len(seen)}")

# Check old jam_cy hashes in seen
old_jam_cy = {k: v for k, v in seen.items() if isinstance(v, dict) and v.get('categoryId') == 'jam_cy'}
print(f"Existing jam_cy hashes in seen_question_hashes.json: {len(old_jam_cy)}")

zip_path = r"C:\Users\yedde\Downloads\jam_cy_official_pyqs_2022_2026.zip"

zip_hashes = {}
collisions_with_existing = []
internal_duplicates = []

with zipfile.ZipFile(zip_path, "r") as z:
    for year in range(2022, 2027):
        fname = f"jam_cy_pyq_{year}.json"
        data = json.loads(z.read(fname).decode("utf-8"))
        for q in data["questions"]:
            qnum = q["questionNumber"]
            qid = q.get("questionId", f"jam_cy_{year}_q{qnum:02d}")
            qtext = q.get("questionTextEn", "")
            h = compute_question_hash(qtext)

            if h in zip_hashes:
                internal_duplicates.append((qid, zip_hashes[h], qtext[:80]))
            else:
                zip_hashes[h] = qid

            if h in seen and seen[h].get('categoryId') != 'jam_cy':
                collisions_with_existing.append((qid, seen[h], qtext[:80]))

print(f"Total questions in 5 JAM CY PYQs: 300")
print(f"Unique hashes among JAM CY PYQs: {len(zip_hashes)}")
print(f"Internal duplicate question stems: {len(internal_duplicates)}")
for dup in internal_duplicates:
    print(f"  {dup[0]} matches {dup[1]}: {dup[2]}")

print(f"Collisions with other categories in repo: {len(collisions_with_existing)}")
for col in collisions_with_existing:
    print(f"  {col[0]} collided with existing {col[1]}: {col[2]}")
