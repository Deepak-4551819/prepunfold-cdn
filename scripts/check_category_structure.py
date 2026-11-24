import json

with open('manifest.json', 'r', encoding='utf-8') as f:
    m = json.load(f)

for cat in m.get('categories', []):
    if 'tgt_pgt' in cat['id']:
        print("Category:", json.dumps({k: v for k, v in cat.items() if k != 'tests'}, ensure_ascii=False, indent=2))
        break

for t in m.get('tests', []):
    if 'tgt_pgt' in t.get('categoryId', ''):
        print("Sample Test:", json.dumps(t, ensure_ascii=False, indent=2))
        break
