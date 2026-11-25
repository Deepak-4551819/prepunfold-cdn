import json

d = json.load(open('tests/gate/gate_cs/pyq/gate_cs_pyq_2024.json', encoding='utf-8'))
qs = d['questions']
print(f"Total questions: {len(qs)}")
short_exp = []
for q in qs:
    en_exp = q.get('explanationEn', '')
    hi_exp = q.get('explanationHi', '')
    if len(en_exp) < 50 or len(hi_exp) < 50:
        short_exp.append((q['questionNumber'], len(en_exp), len(hi_exp)))

print(f"Questions with short explanations (<50 chars): {len(short_exp)}")
if short_exp:
    print(short_exp)
