import json

with open("manifest.json", "r", encoding="utf-8") as f:
    manifest = json.load(f)

print(f"Manifest keys: {list(manifest.keys())}")
if "categories" in manifest:
    print(f"Total categories: {len(manifest['categories'])}")
    for cat in manifest['categories']:
        print(f"  - Category: {cat.get('id')} | Name: {cat.get('nameEn')} | Tests/Items: {len(cat.get('tests', [])) if 'tests' in cat else len(cat.get('subcategories', [])) if 'subcategories' in cat else len(cat.get('parts', []))}")
elif "tests" in manifest:
    print(f"Total root tests: {len(manifest['tests'])}")
    # Sample test
    print(f"Sample test: {manifest['tests'][0] if manifest['tests'] else None}")
