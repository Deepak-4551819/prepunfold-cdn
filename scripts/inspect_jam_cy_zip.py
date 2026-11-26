# -*- coding: utf-8 -*-
import os
import sys
import json
import zipfile

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

zip_path = r"C:\Users\yedde\Downloads\jam_cy_official_pyqs_2022_2026.zip"
print(f"Inspecting zip: {zip_path}")

if not os.path.exists(zip_path):
    print("Zip file does not exist!")
    sys.exit(1)

with zipfile.ZipFile(zip_path, 'r') as z:
    for info in z.infolist():
        print(f"  {info.filename} ({info.file_size} bytes)")

extract_py = r"C:\Users\yedde\Downloads\extract_jam_cy_pyqs.py"
if os.path.exists(extract_py):
    print(f"\nextract_jam_cy_pyqs.py exists ({os.path.getsize(extract_py)} bytes)")
else:
    print(f"\nextract_jam_cy_pyqs.py does NOT exist")

print("\nCurrent status of tests/jam/jam_cy/:")
for root, dirs, files in os.walk("tests/jam/jam_cy"):
    for f in files:
        print(f"  {os.path.join(root, f)}")

with open("manifest.json", "r", encoding="utf-8") as f:
    mf = json.load(f)

for c in mf.get("categories", []):
    if c.get("id") == "jam_cy":
        print("\njam_cy category in manifest.json:")
        print(json.dumps(c, indent=2))

jam_cy_tests = [t for t in mf.get("tests", []) if t.get("categoryId") == "jam_cy"]
print(f"\njam_cy tests in manifest: {len(jam_cy_tests)}")
for t in jam_cy_tests:
    print(f"  [{t.get('testId')}] {t.get('title')} ({t.get('testType')}) -> {t.get('path')}")
