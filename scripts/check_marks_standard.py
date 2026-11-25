import json

d = json.load(open('tests/gate/gate_ph/pyq/gate_ph_pyq_2024.json', encoding='utf-8'))
for q in d['questions']:
    if q['questionType'] == 'MCQ' and q['positiveMarks'] == 2.0:
        print(f"2M MCQ Q{q['questionNumber']}: pos={q['positiveMarks']} neg={q['negativeMarks']}")
        break

for q in d['questions']:
    if q['questionType'] == 'MSQ':
        print(f"MSQ Q{q['questionNumber']}: pos={q['positiveMarks']} neg={q['negativeMarks']}")
        break

for q in d['questions']:
    if q['questionType'] == 'NAT':
        print(f"NAT Q{q['questionNumber']}: pos={q['positiveMarks']} neg={q['negativeMarks']}")
        break
