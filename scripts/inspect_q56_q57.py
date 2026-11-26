# -*- coding: utf-8 -*-
import sys
import json

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('tests/gate/gate_cy/pyq/gate_cy_pyq_2024.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for q in d['questions']:
    if q['questionNumber'] in (56, 57):
        print(f"Q{q['questionNumber']}:")
        print("  questionTextEn:", q['questionTextEn'])
        print("  optionsEn:", json.dumps(q['optionsEn'], ensure_ascii=False, indent=4))
        print("  correctOptionsList:", q['correctOptionsList'])
        print("  explanationEn:", q['explanationEn'][:150])
