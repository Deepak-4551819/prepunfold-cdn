import json

d = json.load(open('tests/gate/gate_cs/pyq/gate_cs_pyq_2024.json', encoding='utf-8'))
qs = d['questions']

out_lines = [
    "# -*- coding: utf-8 -*-",
    "# GATE 2024 Computer Science (CS) Set 1 Official Questions",
    "",
    "QUESTIONS_2024 = ["
]

for q in qs:
    qnum = q['questionNumber']
    qtype = q['questionType']
    pos = q['positiveMarks']
    if qtype == 'MCQ':
        neg = 0.33 if pos == 1.0 else 0.66
    else:
        neg = 0.0
    corr_opt = q.get('correctOption')
    corr_list = q.get('correctOptionsList', [])
    nat_min = q.get('natMin')
    nat_max = q.get('natMax')
    topic = q.get('topicTag')
    diff = q.get('difficulty')
    en = q.get('questionTextEn')
    opts_en = q.get('optionsEn', [])
    exp_en = q.get('explanationEn')
    hi = q.get('questionTextHi')
    opts_hi = q.get('optionsHi', [])
    exp_hi = q.get('explanationHi')

    tup = (qnum, qtype, pos, neg, corr_opt, corr_list, nat_min, nat_max, topic, diff,
           en, opts_en, exp_en, hi, opts_hi, exp_hi)
    out_lines.append(f"    # Q{qnum}")
    out_lines.append(f"    {repr(tup)},")
    out_lines.append("")

out_lines.append("]")

with open('scripts/gate_cs_2024_data.py', 'w', encoding='utf-8') as f:
    f.write("\n".join(out_lines))

print("Wrote scripts/gate_cs_2024_data.py successfully!")
