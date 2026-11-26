# -*- coding: utf-8 -*-
import sys
import json

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

m = json.load(open('manifest.json', encoding='utf-8'))
for i in range(373, 380):
    t = m['tests'][i]
    print(f"[{i}] cat={t.get('categoryId')} id={t.get('testId')}")
