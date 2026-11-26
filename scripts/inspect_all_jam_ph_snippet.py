# -*- coding: utf-8 -*-
import sys
import json
import zipfile

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

zip_path = r"C:\Users\yedde\Downloads\jam_ph_mocks_and_topic_tests.zip"
with zipfile.ZipFile(zip_path, 'r') as z:
    snippet_raw = z.read('jam_ph_mocks_topic_manifest_snippet.json').decode('utf-8')
    items = json.loads(snippet_raw)
    for i, it in enumerate(items):
        print(f"[{i+1:02d}] testId={it.get('testId')}, testType={it.get('testType')}, isFree={it.get('isFree')}, totalQ={it.get('totalQuestions')}, maxMarks={it.get('maxMarks')}, file={it.get('file')}")
        if 'partId' in it or 'syllabusPart' in it:
            print(f"     part: {it.get('partId') or it.get('syllabusPart')}")
