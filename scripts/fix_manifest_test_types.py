# -*- coding: utf-8 -*-
import json

MANIFEST_PATH = r'D:\Android Project\prepunfold-cdn\manifest.json'

with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
    manifest = json.load(f)

fixed = 0
for t in manifest.get('tests', []):
    if t.get('category_id') == 'judiciary_pyq' or t.get('categoryId') == 'judiciary_pyq':
        t['test_type'] = 'TOPIC'
        t['testType'] = 'TOPIC'
        fixed += 1

print(f"Fixed {fixed} tests to test_type='TOPIC'.")

with open(MANIFEST_PATH, 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

print("Saved manifest.json.")
