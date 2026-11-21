import json
import glob

files = glob.glob("tests/judiciary_pyq/*/*.json")
five_opt_count = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    for q in data.get("questions", []):
        if len(q.get("optionsEn", [])) > 4:
            five_opt_count += 1

print(f"Total existing questions with >4 options: {five_opt_count}")
