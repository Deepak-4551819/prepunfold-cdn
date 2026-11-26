# -*- coding: utf-8 -*-
import sys
import json
import zipfile
import re

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

z = zipfile.ZipFile(r"C:\Users\yedde\Downloads\jam_ma_mocks_and_topic_tests.zip")
found = 0
for name in sorted(z.namelist()):
    if not name.endswith('.json') or 'snippet' in name:
        continue
    d = json.loads(z.read(name).decode('utf-8'))
    for q in d['questions']:
        exp = q.get('explanationEn', '')
        if re.search(r'\b(wait|hold on|let me rethink|let me re-read)\b\s*[:\-,]', exp, re.I):
            print(f"{name} Q{q['questionNumber']}: {exp[:120]}")
            found += 1
print(f"Total true self-talk found: {found}")
