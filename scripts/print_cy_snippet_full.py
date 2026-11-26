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
raw = z.read("gate_cy_mocks_topic_manifest_snippet.json").decode('utf-8')
data = json.loads(raw)
print(json.dumps(data, indent=2, ensure_ascii=False))
