# -*- coding: utf-8 -*-
import sys
import json
import glob

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

for pattern in ['tests/jam/jam_ma/pyq/*.json', 'tests/gate/gate_ph/pyq/*.json', 'tests/gate/gate_ma/pyq/*.json', 'tests/gate/gate_cy/pyq/*.json']:
    for fpath in glob.glob(pattern):
        with open(fpath, 'r', encoding='utf-8') as f:
            d = json.load(f)
            for q in d.get('questions', []):
                exp = q.get('explanationEn', '')
                co = str(q.get('correctOption', ''))
                if 'MTA' in exp or 'Marks to All' in exp or 'MTA' in co:
                    print(f"{fpath} Q{q.get('questionNumber')}: type={q.get('questionType')}, neg={q.get('negativeMarks')}, co={q.get('correctOption')}, col={q.get('correctOptionsList')}, natMin={q.get('natMin')}, natMax={q.get('natMax')}")
