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
    for name in sorted(z.namelist()):
        if 'topic' in name.lower() and name.endswith('.json') and 'snippet' not in name.lower():
            d = json.loads(z.read(name).decode('utf-8'))
            print(f"File: {name}")
            print(f"  testId: {d.get('testId')}")
            print(f"  title: {d.get('title')}")
            print(f"  partId: {d.get('partId')}")
            print(f"  partTitle: {d.get('partTitle')}")
            print(f"  isFree: {d.get('isFree')}")
            print(f"  totalQuestions: {d.get('totalQuestions')}")
            print(f"  sections: {d.get('sections')}")
            if d.get('questions'):
                q1 = d['questions'][0]
                print(f"  Q1 topicTag: {q1.get('topicTag')}")
