# -*- coding: utf-8 -*-
import json
import re

with open(r'C:\Users\yedde\Downloads\cpc_pyq.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

ch15 = d['chapters'][14]
print(f"Total questions in Ch 15: {len(ch15['questions'])}")

# Check order mentions for questions
for i, q in enumerate(ch15['questions']):
    txt = (q.get('question_en') or '') + ' ' + (q.get('question_hi') or '') + ' ' + (q.get('explanation_hi') or '')
    m = re.findall(r'(?:आदेश|Order)\s*([0-9IVXLCDM]+)', txt, re.I)
    if i in [0, 50, 100, 150, 180, 200, 240, 280, 320, 360, 400, 440]:
        print(f"Q{i+1} (num {q.get('question_number')}): matches={m[:3]}, text={(q.get('question_en') or q.get('question_hi'))[:70]}")
