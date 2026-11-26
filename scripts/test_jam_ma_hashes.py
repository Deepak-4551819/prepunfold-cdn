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

ZIP_PATH = r"C:\Users\yedde\Downloads\jam_ma_official_pyqs_2022_2026.zip"

hashes = {}
collisions = []
total_q = 0

with zipfile.ZipFile(ZIP_PATH, 'r') as z:
    for name in sorted(z.namelist()):
        if not name.endswith('.json') or 'snippet' in name:
            continue
        d = json.loads(z.read(name).decode('utf-8'))
        for q in d['questions']:
            total_q += 1
            text = q.get('questionTextEn', '')
            norm = re.sub(r'\s+', ' ', text.strip().lower())
            h = hashlib.sha256(norm.encode('utf-8')).hexdigest()[:16]
            if h in hashes:
                collisions.append((hashes[h], q['questionId'], text[:60]))
            else:
                hashes[h] = q['questionId']

print(f"Total JAM MA questions: {total_q}")
print(f"Total unique hashes: {len(hashes)}")
print(f"Collisions: {len(collisions)}")
if collisions:
    for c in collisions:
        print(f"  {c[0]} <-> {c[1]}: '{c[2]}'")
