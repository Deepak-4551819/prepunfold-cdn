# -*- coding: utf-8 -*-
import json, sys

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

for y in [2022, 2023, 2024, 2025, 2026]:
    p = f'tests/gate/gate_ma/pyq/gate_ma_pyq_{y}.json'
    d = json.load(open(p, 'r', encoding='utf-8'))
    print(f"=== {y} ===")
    for q in d['questions']:
        if q.get('topicTag') == 'Mathematics':
            num = q['questionNumber']
            qtext = q['questionTextEn'].replace('\n', ' ')[:100]
            exp = q['explanationEn'].replace('\n', ' ')[:100]
            print(f"Q{num:02d} | text: {qtext} | exp: {exp}")
