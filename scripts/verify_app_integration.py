import json

asset_manifest_path = r"D:\MyApp\PrepUnfold\app\src\main\assets\sample_manifest.json"
with open(asset_manifest_path, "r", encoding="utf-8") as f:
    m = json.load(f)

print(f"Manifest Version: {m.get('manifest_version') or m.get('manifestVersion')}")
print(f"Total Categories: {len(m.get('categories', []))}")
print(f"Total Tests: {len(m.get('tests', []))}")

jud_cat = [c for c in m.get('categories', []) if c.get('id') == 'judiciary_pyq']
print(f"Found judiciary_pyq category: {bool(jud_cat)}")
if jud_cat:
    cat = jud_cat[0]
    print(f"  Title: {cat.get('titleEn')}")
    print(f"  Parts: {len(cat.get('parts', []))}")
    print(f"  Total tests reported: {cat.get('totalTests')}")
    print(f"  Total Qs reported: {cat.get('totalQuestions')}")

jud_tests = [t for t in m.get('tests', []) if t.get('categoryId') == 'judiciary_pyq']
print(f"Judiciary tests in manifest: {len(jud_tests)}")
sample_test = jud_tests[0] if jud_tests else None
if sample_test:
    print(f"Sample test cdnUrl: {sample_test.get('cdnUrl')}")
    print(f"Sample test title: {sample_test.get('titleEn')}")
