import glob
import json
import os

judiciary_dir = "tests/judiciary_pyq"
subdirs = sorted([d for d in os.listdir(judiciary_dir) if os.path.isdir(os.path.join(judiciary_dir, d))])

for sub in subdirs:
    sub_path = os.path.join(judiciary_dir, sub)
    json_files = sorted(glob.glob(os.path.join(sub_path, "*.json")))
    if json_files:
        with open(json_files[0], 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"[{sub:<18}] testId: {data.get('testId')} | categoryId: {data.get('categoryId')} | partId: {data.get('partId')}")
