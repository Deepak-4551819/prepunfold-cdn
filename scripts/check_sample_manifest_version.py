import json

path = r"D:\MyApp\PrepUnfold\app\src\main\assets\sample_manifest.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Sample manifest keys: {list(data.keys())}")
print(f"manifestVersion: {data.get('manifestVersion') or data.get('manifest_version')}")
print(f"Categories count: {len(data.get('categories', []))}")
print(f"Tests count: {len(data.get('tests', []))}")
