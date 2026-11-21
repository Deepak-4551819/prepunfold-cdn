import json

with open("manifest.json", "r", encoding="utf-8") as f:
    manifest = json.load(f)

for cat in manifest.get("categories", []):
    if cat.get("id") in ["history_pyq_1990_2024", "polity_pyq_1990_2022"]:
        print(f"=== Category {cat.get('id')} ===")
        print(json.dumps(cat, ensure_ascii=False, indent=2)[:600])

print("\n=== Sample tests in manifest['tests'] ===")
for t in manifest.get("tests", [])[:3]:
    print(json.dumps(t, ensure_ascii=False, indent=2))
