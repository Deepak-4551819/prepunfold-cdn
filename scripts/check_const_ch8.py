# -*- coding: utf-8 -*-
import json

with open(r'C:\Users\yedde\Downloads\indian_constitution_pyq (1).json', 'r', encoding='utf-8') as f:
    d = json.load(f)

ch8 = d['chapters'][7]['questions']
print(f"Total questions in Ch 8: {len(ch8)}")

slices = [
    (0, 103, "t11 (President & VP)"),
    (103, 179, "t12 (Parliament)"),
    (179, 286, "t13 (Union Judiciary & CAG)")
]

for s, e, name in slices:
    q_start = ch8[s]
    q_end = ch8[e-1]
    print(f"\n{name} ({e-s} Qs):")
    print(f"  Start [idx {s}]: {(q_start.get('question_en') or q_start.get('question_hi'))[:70]}")
    print(f"  End   [idx {e-1}]: {(q_end.get('question_en') or q_end.get('question_hi'))[:70]}")
