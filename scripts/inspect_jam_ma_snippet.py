# -*- coding: utf-8 -*-
import sys
import json
import zipfile

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

z = zipfile.ZipFile(r"C:\Users\yedde\Downloads\jam_ma_official_pyqs_2022_2026.zip")
raw = z.read("jam_ma_pyq_manifest_snippet.json").decode('utf-8')
data = json.loads(raw)
print(json.dumps(data, indent=2, ensure_ascii=False))
