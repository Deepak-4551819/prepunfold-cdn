import json

with open('manifest.json', 'r', encoding='utf-8') as f:
    m = json.load(f)

print("Bundles:")
for b in m.get('bundles', []):
    print(json.dumps(b, ensure_ascii=False, indent=2))
