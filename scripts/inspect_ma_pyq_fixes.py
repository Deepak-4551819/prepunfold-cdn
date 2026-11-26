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
    generic_topics = []
    for q in d['questions']:
        if q.get('topicTag') == 'Mathematics':
            generic_topics.append((q['questionNumber'], q['questionTextEn'][:60]))
    print(f"{y}: {len(generic_topics)} questions with topicTag == 'Mathematics'")
    if generic_topics:
        for num, snippet in generic_topics[:5]:
            print(f"   Q{num:02d}: {snippet}...")
