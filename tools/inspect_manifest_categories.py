import json

with open('manifest.json', 'r', encoding='utf-8') as f:
    m = json.load(f)

print("Top-level keys in manifest.json:", list(m.keys()))
categories = m.get('categories', [])
print(f"Total categories: {len(categories)}")
for c in categories:
    cid = c.get('categoryId') or c.get('id') or c.get('category_id')
    name = c.get('name') or c.get('title')
    print(f"  Category: {cid} | Name: {name}")

tests = m.get('tests', [])
cat_counts = {}
for t in tests:
    cat = t.get('categoryId') or t.get('category_id')
    cat_counts[cat] = cat_counts.get(cat, 0) + 1

print("\nTests per category in manifest.json:")
for cat, count in sorted(cat_counts.items(), key=lambda x: str(x[0])):
    print(f"  {cat}: {count} tests")
