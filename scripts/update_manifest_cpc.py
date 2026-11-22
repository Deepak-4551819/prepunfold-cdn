# -*- coding: utf-8 -*-
import json
import os
import shutil

MANIFEST_PATH = 'manifest.json'
with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
    m = json.load(f)

updated = 0
for t in m.get('tests', []):
    if 'cpc_pyq' in t.get('testId', ''):
        fn = os.path.join('tests/judiciary_pyq/cpc', f"{t['testId']}.json")
        if os.path.exists(fn):
            with open(fn, 'r', encoding='utf-8') as fp:
                d = json.load(fp)
            cnt = len(d['questions'])
            if t.get('totalQuestions') != cnt:
                t['totalQuestions'] = cnt
                updated += 1

m['manifest_version'] = m.get('manifest_version', 28) + 1
print(f"Updated {updated} CPC tests in manifest. Bumped manifest_version to {m['manifest_version']}.")

with open(MANIFEST_PATH, 'w', encoding='utf-8') as f:
    json.dump(m, f, ensure_ascii=False, indent=2)

print("Saved manifest.json successfully.")

# Sync to app
app_dest = r"D:\MyApp\PrepUnfold\app\src\main\assets\sample_manifest.json"
if os.path.exists(os.path.dirname(app_dest)):
    shutil.copyfile(MANIFEST_PATH, app_dest)
    print(f"Synced manifest to {app_dest}")
