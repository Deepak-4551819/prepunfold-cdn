import json

with open('manifest.json', 'r', encoding='utf-8') as f:
    m = json.load(f)

print(f"Total categories: {len(m.get('categories', []))}")
for c in m.get('categories', []):
    print(f"ID: {c.get('id'):<30} | Title: {c.get('title'):<35} | TitleHi: {c.get('titleHi')}")
