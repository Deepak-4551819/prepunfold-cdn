# -*- coding: utf-8 -*-
import sys
import json

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('manifest.json', 'r', encoding='utf-8') as f:
    mf = json.load(f)

types = set()
for t in mf.get('tests', []):
    types.add((t.get('testType'), t.get('test_type')))
print('Unique (testType, test_type) pairs in manifest:', types)

for cat in ['gate_ph', 'gate_ma', 'gate_cy', 'jam_ma', 'jam_ph']:
    mocks = [t for t in mf.get('tests', []) if t.get('categoryId') == cat and 'mock' in t.get('testId', '').lower()]
    print(f"{cat} mocks count: {len(mocks)}")
    if mocks:
        m = mocks[0]
        print(f"  sample {m.get('testId')}: testType={m.get('testType')}, test_type={m.get('test_type')}, isFree={m.get('isFree')}, shiftBadge={m.get('shiftBadge')}, path={m.get('path')}")
