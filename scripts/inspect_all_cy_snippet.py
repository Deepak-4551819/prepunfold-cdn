# -*- coding: utf-8 -*-
import sys
import json
import zipfile

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

z = zipfile.ZipFile(r'C:\Users\yedde\Downloads\gate_cy_mocks_and_topic_tests.zip')
data = json.loads(z.read('gate_cy_mocks_topic_manifest_snippet.json').decode('utf-8'))
print(f"Total snippet items: {len(data)}")
for idx, item in enumerate(data):
    print(f"{idx:02d}: {item.get('testId')} | type={item.get('testType')} | Qs={item.get('totalQuestions')} | marks={item.get('maxMarks')} | isFree={item.get('isFree')} | title={item.get('title')}")
