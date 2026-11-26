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
    return hashlib.sha256(norm.encode('utf-8')).hexdigest()

with open('seen_question_hashes.json', 'r', encoding='utf-8') as f:
    seen = json.load(f)

print(f"Total existing hashes in seen_question_hashes.json: {len(seen)}")

zip_path = r"C:\Users\yedde\Downloads\jam_ph_mocks_and_topic_tests.zip"

zip_hashes = {}
collisions_with_existing = []
internal_duplicates = []

with zipfile.ZipFile(zip_path, 'r') as z:
    for fname in sorted(z.namelist()):
        if fname.endswith('.json') and 'snippet' not in fname.lower():
            data = json.loads(z.read(fname).decode('utf-8'))
            for q in data['questions']:
                qid = q['questionId']
                qtext = q.get('questionTextEn', '')
                h = compute_question_hash(qtext)

                if h in zip_hashes:
                    internal_duplicates.append((qid, zip_hashes[h], qtext[:80]))
                else:
                    zip_hashes[h] = qid

                if h in seen:
                    collisions_with_existing.append((qid, seen[h], qtext[:80]))

print(f"Total questions in 24 JAM PH mock/topic files: 880")
print(f"Unique hashes among JAM PH mock/topic tests: {len(zip_hashes)}")
print(f"Internal duplicate question stems: {len(internal_duplicates)}")
for dup in internal_duplicates:
    print(f"  {dup[0]} matches {dup[1]}: {dup[2]}")

print(f"Collisions with existing repo hashes: {len(collisions_with_existing)}")
for col in collisions_with_existing:
    print(f"  {col[0]} collided with existing {col[1]}: {col[2]}")
