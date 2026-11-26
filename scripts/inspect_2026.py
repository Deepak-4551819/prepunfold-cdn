# -*- coding: utf-8 -*-
import json

d = json.load(open('tests/gate/gate_ph/pyq/gate_ph_pyq_2026.json', encoding='utf-8'))
qs = {q['questionNumber']: q for q in d['questions']}

print('=== 2026 Option D inspection ===')
for qn in [10, 11, 14, 16, 19, 21, 24, 25, 27, 36, 38, 39, 40, 41]:
    q = qs[qn]
    opts = q.get('optionsEn', [])
    optD = opts[3] if len(opts) > 3 else 'NO_OPT_D'
    print(f'Q{qn} Opt D: {optD}')

print('\n=== 2026 NAT inspection ===')
for qn in range(1, 66):
    q = qs[qn]
    if q['questionType'] == 'NAT':
        txt = q['questionTextEn']
        lines = [line.strip() for line in txt.splitlines() if line.strip()]
        last_line = lines[-1] if lines else ''
        first_line = lines[0] if lines else ''
        print(f"Q{qn} NAT ({q.get('natMin')}..{q.get('natMax')}):")
        print(f"   First: {first_line[:80]}")
        print(f"   Last : {last_line}")
