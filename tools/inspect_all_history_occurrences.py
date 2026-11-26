import json

with open('manifest.json', 'r', encoding='utf-8') as f:
    m = json.load(f)

print("Categories with 'history':")
for c in m.get('categories', []):
    if 'history' in str(c).lower():
        print(" ", c.get('categoryId'), "|", c.get('title'))

hist_cat_tests = [t for t in m.get('tests', []) if 'history' in str(t.get('categoryId', '')).lower()]
print(f"\nTests with category containing 'history': {len(hist_cat_tests)}")
by_cat = {}
for t in hist_cat_tests:
    cat = t.get('categoryId')
    by_cat[cat] = by_cat.get(cat, 0) + 1
for k, v in by_cat.items():
    print(f"  {k}: {v} tests")
