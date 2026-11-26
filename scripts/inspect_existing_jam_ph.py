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

print("Files in tests/jam/jam_ph:")
for root, dirs, files in os.walk("tests/jam/jam_ph"):
    for f in files:
        print(f"  {os.path.join(root, f)}")

with open("manifest.json", "r", encoding="utf-8") as f:
    mf = json.load(f)

for c in mf.get("categories", []):
    if c.get("id") == "jam_ph":
        print("\njam_ph Category metadata in manifest.json:")
        print(json.dumps(c, indent=2))

for t in mf.get("tests", []):
    if t.get("categoryId") == "jam_ph" or "jam_ph" in t.get("testId", ""):
        print("\njam_ph test in manifest.json:")
        print(json.dumps(t, indent=2))

zip_path = r"C:\Users\yedde\Downloads\jam_ph_official_pyqs_2022_2026.zip"
with zipfile.ZipFile(zip_path, "r") as z:
    snip = json.loads(z.read("jam_ph_pyq_manifest_snippet.json").decode("utf-8"))
    print("\nManifest snippet in zip:")
    print(json.dumps(snip, indent=2))
