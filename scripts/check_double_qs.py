# -*- coding: utf-8 -*-
import json
import glob
import os
import re
from collections import Counter

def norm(text):
    text = text.lower().strip()
    text = re.sub(r'\s+', ' ', text)
    return text

files = sorted(glob.glob('tests/gate/gate_ph/pyq/*.json'))
for f in files:
    d = json.load(open(f, encoding='utf-8'))
    qs = d.get('questions', [])
    stems = [norm(q.get('questionTextEn', '')) for q in qs]
    counts = Counter(stems)
    dups = {k: v for k, v in counts.items() if v > 1}
    print(f"{os.path.basename(f)}: {len(qs)} questions, {len(dups)} duplicates")
    if dups:
        for k, v in list(dups.items()):
            print(f"  {v}x: {k[:80]}")

print("\n--- Cross-file duplicates among existing pyqs ---")
all_stems = {}
for f in files:
    d = json.load(open(f, encoding='utf-8'))
    for q in d.get('questions', []):
        s = norm(q.get('questionTextEn', ''))
        all_stems.setdefault(s, []).append((os.path.basename(f), q.get('questionNumber')))

cross = {k: v for k, v in all_stems.items() if len(v) > 1}
print(f"Total cross-file duplicates: {len(cross)}")
for k, v in list(cross.items())[:10]:
    print(f"  Appears in {v}: {k[:80]}")

print("\n--- Check 2021 specifically ---")
d21 = json.load(open('tests/gate/gate_ph/pyq/gate_ph_pyq_2021.json', encoding='utf-8'))
for q in d21['questions'][:15]:
    print(f"Q{q['questionNumber']} ({q['questionType']}): {q['questionTextEn'][:60]}")
    if q.get('optionsEn'):
        print(f"   opts: {q['optionsEn']}")
