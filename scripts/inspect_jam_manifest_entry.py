# -*- coding: utf-8 -*-
import sys
import json

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('manifest.json', 'r', encoding='utf-8') as f:
    m = json.load(f)

for idx, t in enumerate(m['tests']):
    if t.get('categoryId') in ('jam_ph', 'jam_ma', 'jam_cy'):
        print(f"[{idx}] {t.get('categoryId')} | {t.get('testId')}")
        print(json.dumps(t, indent=2, ensure_ascii=False))
