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

with zipfile.ZipFile(ZIP_PATH, 'r') as z:
    raw = z.read("gate_cy_mocks_topic_manifest_snippet.json").decode('utf-8')
    data = json.loads(raw)
    print("Snippet type:", type(data))
    if isinstance(data, dict):
        print("Keys:", list(data.keys()))
        if "category" in data:
            print("\nCategory config:")
            print(json.dumps(data["category"], indent=2, ensure_ascii=False))
        if "parts" in data:
            print("\nParts count:", len(data["parts"]))
            print(json.dumps(data["parts"], indent=2, ensure_ascii=False))
        if "tests" in data:
            print("\nTests count:", len(data["tests"]))
            print("First test sample:")
            print(json.dumps(data["tests"][0], indent=2, ensure_ascii=False))
    elif isinstance(data, list):
        print(f"List with {len(data)} items")
        print("Sample 0:", json.dumps(data[0], indent=2, ensure_ascii=False))
        print("Sample -1:", json.dumps(data[-1], indent=2, ensure_ascii=False))
