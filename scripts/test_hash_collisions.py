# -*- coding: utf-8 -*-
import json
import re
import hashlib
from gate_cs_2024_data import QUESTIONS_2024
from build_2025_part1 import QUESTIONS_2025_PART1
from gate_cs_2025_part2 import QUESTIONS_2025_PART2

def compute_hash(text):
    norm = re.sub(r'\s+', ' ', text.strip().lower())
    return hashlib.sha256(norm.encode('utf-8')).hexdigest()[:16]

seen_data = json.load(open('seen_question_hashes.json', encoding='utf-8'))
other_hashes = {k: v for k, v in seen_data.items() if v.get('testId') != 'gate_cs_pyq_2024'}

# Check 2024
hashes_2024 = {}
for q in QUESTIONS_2024:
    q_num = q[0]
    text = q[10]
    h = compute_hash(text)
    assert h not in hashes_2024, f"Self collision in 2024 Q{q_num} hash {h}"
    if h in other_hashes:
        print(f"Collision in 2024 Q{q_num} with {other_hashes[h]}")
    hashes_2024[h] = f"gate_cs_2024_s1_q{q_num:02d}"

# Check 2025
all_2025 = QUESTIONS_2025_PART1 + QUESTIONS_2025_PART2
hashes_2025 = {}
for q in all_2025:
    q_num = q[0]
    text = q[10]
    h = compute_hash(text)
    assert h not in hashes_2025, f"Self collision in 2025 Q{q_num} hash {h}"
    if h in other_hashes:
        print(f"Collision in 2025 Q{q_num} with {other_hashes[h]}")
    if h in hashes_2024:
        print(f"Cross collision between 2025 Q{q_num} and 2024: {hashes_2024[h]}")
    hashes_2025[h] = f"gate_cs_2025_s1_q{q_num:02d}"

print(f"Total 2024 unique hashes: {len(hashes_2024)}")
print(f"Total 2025 unique hashes: {len(hashes_2025)}")
print("Hash collision check finished!")
