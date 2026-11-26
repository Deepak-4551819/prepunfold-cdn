# -*- coding: utf-8 -*-
import sys
import json
import zipfile
import re
import hashlib

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ZIP_PATH = r"C:\Users\yedde\Downloads\jam_ma_mocks_and_topic_tests.zip"

hashes = {}
collisions = []
total_q = 0

# 5 PYQs from disk
for yr in [2026, 2025, 2024, 2023, 2022]:
    p = f"tests/jam/jam_ma/pyq/jam_ma_pyq_{yr}.json"
    with open(p, 'r', encoding='utf-8') as f:
        d = json.load(f)
    for q in d['questions']:
        total_q += 1
        text = q.get('questionTextEn', '')
        norm = re.sub(r'\s+', ' ', text.strip().lower())
        h = hashlib.sha256(norm.encode('utf-8')).hexdigest()[:16]
        if h in hashes:
            collisions.append((hashes[h], q['questionId'], text[:60]))
        else:
            hashes[h] = q['questionId']

print(f"PYQ questions: {total_q}, unique hashes: {len(hashes)}")

# Mocks and Topic tests from zip
zip_q = 0
with zipfile.ZipFile(ZIP_PATH, 'r') as z:
    for name in sorted(z.namelist()):
        if not name.endswith('.json') or 'snippet' in name:
            continue
        d = json.loads(z.read(name).decode('utf-8'))
        for q in d['questions']:
            zip_q += 1
            text = q.get('questionTextEn', '')
            norm = re.sub(r'\s+', ' ', text.strip().lower())
            h = hashlib.sha256(norm.encode('utf-8')).hexdigest()[:16]
            if h in hashes:
                collisions.append((hashes[h], q['questionId'], text[:60]))
            else:
                hashes[h] = q['questionId']

print(f"Zip questions: {zip_q}")
print(f"Grand total questions: {total_q + zip_q}")
print(f"Grand total unique hashes: {len(hashes)}")
print(f"Collisions: {len(collisions)}")
if collisions:
    print("\nCollisions found:")
    for c in collisions:
        print(f"  {c[0]} <-> {c[1]}: '{c[2]}'")
