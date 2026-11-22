# -*- coding: utf-8 -*-
import json
import glob
import os

with open(r'C:\Users\yedde\Downloads\ipc_pyq (1).json', 'r', encoding='utf-8') as f:
    ipc_data = json.load(f)

print(f"Total chapters in IPC json: {len(ipc_data['chapters'])}")
for i, ch in enumerate(ipc_data['chapters']):
    print(f"Ch {i+1}: Qs={len(ch['questions'])}, EN='{ch['chapter_name_en']}'")

tests = sorted(glob.glob(r'D:\Android Project\prepunfold-cdn\tests\judiciary_pyq\ipc\*.json'))
print(f"\nTotal test files in IPC repo: {len(tests)}")
for t in tests:
    with open(t, 'r', encoding='utf-8') as f:
        d = json.load(f)
    print(f"  {os.path.basename(t)}: {len(d.get('questions', []))} Qs, titleEn='{d.get('titleEn')}'")
