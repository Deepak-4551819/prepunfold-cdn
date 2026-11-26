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
    data = json.loads(snippet_raw)
    print("Snippet type:", type(data))
    if isinstance(data, dict):
        print("Snippet keys:", list(data.keys()))
        for k in data:
            if isinstance(data[k], list):
                print(f"  {k}: list of length {len(data[k])}")
                if len(data[k]) > 0:
                    print(f"    sample item {k}[0]:", json.dumps(data[k][0], indent=2)[:300])
            elif isinstance(data[k], dict):
                print(f"  {k}: dict with keys {list(data[k].keys())}")
            else:
                print(f"  {k}: {data[k]}")
    elif isinstance(data, list):
        print(f"Snippet list of length {len(data)}")
        if len(data) > 0:
            print("Sample item[0]:", json.dumps(data[0], indent=2))
