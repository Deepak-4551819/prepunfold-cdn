import json

with open('manifest.json', 'r', encoding='utf-8') as f:
    m = json.load(f)

for c in m.get('categories', []):
    if 'tgt' in str(c).lower() or 'teach' in str(c).lower() or 'history' in str(c).lower():
        print(json.dumps(c, ensure_ascii=False, indent=2))
