# -*- coding: utf-8 -*-
import json
import re

with open(r'C:\Users\yedde\Downloads\cpc_pyq.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

ch15 = d['chapters'][14] # Ch 15
print("Ch15 questions count:", len(ch15['questions']))

# Look at how orders appear in stems or explanations
order_counts = {}
for q in ch15['questions']:
    txt = (q.get('question_en') or '') + ' ' + (q.get('question_hi') or '') + ' ' + (q.get('explanation_hi') or '')
    m = re.search(r'(?:आदेश|Order)\s*[-:]?\s*([0-9IVXLCDM]+)', txt, re.I)
    ord_str = m.group(1).upper() if m else 'UNKNOWN'
    order_counts[ord_str] = order_counts.get(ord_str, 0) + 1

print("Sample order detections:", sorted(order_counts.items(), key=lambda x: -x[1])[:20])
