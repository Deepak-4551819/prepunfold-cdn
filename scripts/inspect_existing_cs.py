import json

d = json.load(open('tests/gate/gate_cs/pyq/gate_cs_pyq_2024.json', encoding='utf-8'))
print(f"Total questions in existing: {len(d['questions'])}")
for q in d['questions']:
    print(f"Q{q['questionNumber']:02d}: type={q.get('questionType')} marks={q.get('positiveMarks')} corr={q.get('correctOption')} list={q.get('correctOptionsList')} nat={q.get('natMin')} text={q.get('questionTextEn')[:50]}")
