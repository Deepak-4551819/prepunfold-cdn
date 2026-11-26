# -*- coding: utf-8 -*-
import sys
import json
import zipfile

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ZIP_PATH = r"C:\Users\yedde\Downloads\jam_ma_mocks_and_topic_tests.zip"

with zipfile.ZipFile(ZIP_PATH, 'r') as z:
    raw = z.read("jam_ma_mocks_topic_manifest_snippet.json").decode('utf-8')
    data = json.loads(raw)
    print("Total snippet items:", len(data))
    for idx, item in enumerate(data):
        print(f"{idx:02d}: {item.get('testId')} | type={item.get('testType')} | Qs={item.get('totalQuestions')} | marks={item.get('maxMarks')} | isFree={item.get('isFree')} | title={item.get('title')}")
