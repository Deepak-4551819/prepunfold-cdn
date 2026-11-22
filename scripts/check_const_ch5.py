# -*- coding: utf-8 -*-
import json
import re

with open(r'C:\Users\yedde\Downloads\indian_constitution_pyq (1).json', 'r', encoding='utf-8') as f:
    d = json.load(f)

ch5 = d['chapters'][4]['questions']
print(f"Total questions in Ch 5: {len(ch5)}")

# Check slices
# t04 had 63 Qs, t05 had 91 Qs, t06 had 130 Qs, t07 had 40 Qs, t08 had 63 Qs
# 63, 63+91=154, 154+130=284, 284+40=324, 324+63=387
slices = [
    (0, 63, "t04 (Art 12-13)"),
    (63, 154, "t05 (Art 14-18)"),
    (154, 284, "t06 (Art 19-22)"),
    (284, 324, "t07 (Art 23-31)"),
    (324, 387, "t08 (Art 32-35)")
]

for s, e, name in slices:
    q_start = ch5[s]
    q_end = ch5[e-1]
    print(f"\n{name} ({e-s} Qs):")
    print(f"  Start [idx {s}]: {(q_start.get('question_en') or q_start.get('question_hi'))[:70]}")
    print(f"  End   [idx {e-1}]: {(q_end.get('question_en') or q_end.get('question_hi'))[:70]}")
