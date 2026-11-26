import json

with open('manifest.json', 'r', encoding='utf-8') as f:
    m = json.load(f)

print("manifest_version:", m.get('manifest_version'))
print("manifestVersion:", m.get('manifestVersion'))
print("version:", m.get('version'))
print("totalTests:", m.get('totalTests'))
print("totalQuestions:", m.get('totalQuestions'))
