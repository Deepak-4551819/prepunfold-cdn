# -*- coding: utf-8 -*-
import os
import glob
import json

base_dir = r'D:\Android Project\prepunfold-cdn\tests\judiciary_pyq'
subjects = os.listdir(base_dir)

for s in sorted(subjects):
    s_path = os.path.join(base_dir, s)
    if not os.path.isdir(s_path):
        continue
    files = sorted(glob.glob(os.path.join(s_path, '*.json')))
    print(f"Subject: {s} ({len(files)} files)")
    for f in files[:5]:
        with open(f, 'r', encoding='utf-8') as jf:
            d = json.load(jf)
        print(f"   {os.path.basename(f)}: id={d.get('testId')}, titleEn={d.get('titleEn')}, Qs={len(d.get('questions', []))}")
    if len(files) > 5:
        print(f"   ... and {len(files)-5} more")
