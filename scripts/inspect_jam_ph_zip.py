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

print("Folders under tests/jam:")
if os.path.exists("tests/jam"):
    print(os.listdir("tests/jam"))
else:
    print("tests/jam does not exist!")

with open("manifest.json", "r", encoding="utf-8") as f:
    mf = json.load(f)

cats = mf.get("categories", [])
print("\nCategories in manifest matching jam:")
for cdata in cats:
    cid = cdata.get("id") or cdata.get("categoryId")
    if "jam" in str(cid).lower():
        print(f"  {cid}: {cdata.get('nameEn')} (testsCount={cdata.get('testsCount')}, totalQuestions={cdata.get('totalQuestions')})")

tests_jam = [t for t in mf.get("tests", []) if "jam" in t.get("categoryId", "").lower() or "jam" in t.get("testId", "").lower()]
print(f"\nTotal tests in manifest matching jam: {len(tests_jam)}")
by_cat = {}
for t in tests_jam:
    cat = t.get("categoryId", "unknown")
    by_cat[cat] = by_cat.get(cat, 0) + 1
for cat, cnt in by_cat.items():
    print(f"  {cat}: {cnt} tests")

zip_path = r"C:\Users\yedde\Downloads\jam_ph_official_pyqs_2022_2026.zip"
print(f"\nAnalyzing zip: {zip_path}")
with zipfile.ZipFile(zip_path, "r") as z:
    for name in z.namelist():
        data = z.read(name)
        print(f"  {name}: {len(data)} bytes")
