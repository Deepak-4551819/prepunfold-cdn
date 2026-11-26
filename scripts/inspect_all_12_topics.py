# -*- coding: utf-8 -*-
import sys
import json
import zipfile

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ZIP_PATH = r"C:\Users\yedde\Downloads\gate_cy_mocks_and_topic_tests.zip"

topics_seen = {}
with zipfile.ZipFile(ZIP_PATH, 'r') as z:
    for name in sorted(z.namelist()):
        if 'topic' in name and name.endswith('.json') and 'snippet' not in name:
            d = json.loads(z.read(name).decode('utf-8'))
            tid = d.get('testId')
            base = tid.rsplit('_', 1)[0]
            if base not in topics_seen:
                topics_seen[base] = []
            topics_seen[base].append(d)

print(f"Found {len(topics_seen)} distinct topics:")
for idx, (base, tests) in enumerate(topics_seen.items(), 1):
    t1 = tests[0]
    print(f"{idx:02d}. base: {base}")
    print(f"    title: {t1.get('title')}")
    print(f"    shiftBadge: {t1.get('shiftBadge')}")
    print(f"    questions: {len(t1.get('questions', []))}, marks: {t1.get('maxMarks')}")
