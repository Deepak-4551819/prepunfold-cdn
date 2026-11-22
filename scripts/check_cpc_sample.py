# -*- coding: utf-8 -*-
import json

with open(r'C:\Users\yedde\Downloads\cpc_pyq.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

ch1 = d['chapters'][0]
for q in ch1['questions']:
    if q.get('question_number') in (14, 29):
        print(f"=== Q{q['question_number']} ===")
        print("EN:", q.get('question_en'))
        print("HI:", q.get('question_hi'))
        print("Options EN:", q.get('options_en'))
        print("Options HI:", q.get('options_hi'))
        print("Answer:", q.get('answer'))
        print("Expl HI:", (q.get('explanation_hi') or '')[:150])
        print("Expl EN:", (q.get('explanation_en') or '')[:150])
