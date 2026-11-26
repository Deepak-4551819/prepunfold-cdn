# -*- coding: utf-8 -*-
import json
import zipfile
import glob
import os
import sys
from collections import Counter

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ZIP_PATH = r"C:\Users\yedde\Downloads\gate_ph_official_pyqs_2022_2026.zip"
EXISTING_DIR = r"tests/gate/gate_ph/pyq"

print("========================================")
print("  EXISTING GATE PH PYQS IN REPO")
print("========================================")
existing_stems = {}
for p in sorted(glob.glob(os.path.join(EXISTING_DIR, "*.json"))):
    fname = os.path.basename(p)
    d = json.load(open(p, "r", encoding="utf-8"))
    qs = d.get("questions", [])
    stems = [q.get("questionTextEn", "").strip() for q in qs]
    counter = Counter(stems)
    internal_dups = {k: v for k, v in counter.items() if v > 1}

    # check Hindi
    has_hi = any(q.get("questionTextHi") for q in qs)

    print(f"\n{fname}:")
    print(f"  testId: {d.get('testId')}")
    print(f"  title: {d.get('title')}")
    print(f"  totalQuestions: {d.get('totalQuestions')}, len(qs): {len(qs)}, maxMarks: {d.get('maxMarks')}")
    print(f"  has_hindi: {has_hi}")
    print(f"  internal dups: {len(internal_dups)}")
    if internal_dups:
        for k, v in list(internal_dups.items())[:5]:
            print(f"    DUP ({v}x): {k[:70]}")

    existing_stems[fname] = stems

print("\n========================================")
print("  ZIP GATE PH PYQS")
print("========================================")
zip_stems = {}
with zipfile.ZipFile(ZIP_PATH, "r") as z:
    for name in sorted(z.namelist()):
        if not name.endswith(".json"):
            continue
        d = json.loads(z.read(name).decode("utf-8"))
        qs = d.get("questions", [])
        stems = [q.get("questionTextEn", "").strip() for q in qs]
        counter = Counter(stems)
        internal_dups = {k: v for k, v in counter.items() if v > 1}
        has_hi = any(q.get("questionTextHi") for q in qs)

        print(f"\n{name}:")
        print(f"  testId: {d.get('testId')}")
        print(f"  title: {d.get('title')}")
        print(f"  totalQuestions: {d.get('totalQuestions')}, len(qs): {len(qs)}, maxMarks: {d.get('maxMarks')}")
        print(f"  has_hindi: {has_hi}")
        print(f"  internal dups: {len(internal_dups)}")
        print(f"  top-level keys: {list(d.keys())}")
        if qs:
            print(f"  q[0] keys: {list(qs[0].keys())}")
            print(f"  Q1 stem: {qs[0].get('questionTextEn', '')[:80]}")
            print(f"  Q11 stem: {qs[10].get('questionTextEn', '')[:80] if len(qs) > 10 else ''}")

        zip_stems[name] = stems

# Compare existing vs zip
print("\n========================================")
print("  COMPARING EXISTING VS ZIP")
print("========================================")
for fname, ex_s in existing_stems.items():
    zip_match = f"pyqs/{fname}"
    if zip_match in zip_stems:
        z_s = zip_stems[zip_match]
        same_count = sum(1 for a, b in zip(ex_s, z_s) if a == b)
        print(f"{fname} vs {zip_match}: {same_count}/65 identical question stems")
        if same_count < 65:
            for idx, (a, b) in enumerate(zip(ex_s, z_s)):
                if a != b:
                    print(f"  Diff at Q{idx+1}:")
                    print(f"    Existing: {a[:70]}")
                    print(f"    Zip:      {b[:70]}")
                    break
