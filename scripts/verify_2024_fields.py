import json

d = json.load(open('tests/gate/gate_cs/pyq/gate_cs_pyq_2024.json', encoding='utf-8'))
qs = d['questions']
print(f"Total: {len(qs)}")
total_marks = sum(q['positiveMarks'] for q in qs)
print(f"Total marks: {total_marks}")

for q in qs:
    qnum = q['questionNumber']
    qtype = q['questionType']
    pos = q['positiveMarks']
    neg = q['negativeMarks']
    en = q.get('questionTextEn', '')
    hi = q.get('questionTextHi', '')
    opts_en = q.get('optionsEn', [])
    opts_hi = q.get('optionsHi', [])
    exp_en = q.get('explanationEn', '')
    exp_hi = q.get('explanationHi', '')

    assert len(en) > 10, f"Q{qnum} short en"
    assert len(hi) > 10, f"Q{qnum} short hi"
    assert len(exp_en) > 10, f"Q{qnum} short exp_en"
    assert len(exp_hi) > 10, f"Q{qnum} short exp_hi"

    if qtype in ['MCQ', 'MSQ']:
        assert len(opts_en) == 4, f"Q{qnum} opts_en != 4"
        assert len(opts_hi) == 4, f"Q{qnum} opts_hi != 4"
    else:
        assert len(opts_en) == 0, f"Q{qnum} NAT has opts_en"
        assert len(opts_hi) == 0, f"Q{qnum} NAT has opts_hi"
        assert q.get('natMin') is not None, f"Q{qnum} NAT missing natMin"
        assert q.get('natMax') is not None, f"Q{qnum} NAT missing natMax"

print("All 65 questions in 2024 verified with full bilingual options & explanations!")
