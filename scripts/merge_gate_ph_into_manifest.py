#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
One-Command Merger & Validator for `prepunfold-cdn` (GATE Physics Complete Upgrade)
Usage inside your local `prepunfold-cdn` repo root:
    python3 scripts/merge_gate_ph_into_manifest.py
"""
import json, os, shutil, glob

def main():
    with open("manifest_gate_ph_section.json", "r", encoding="utf-8") as f:
        gate_data = json.load(f)

    manifest_path = "manifest.json"
    if os.path.exists(manifest_path):
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)
    else:
        manifest = {"manifest_version": 2, "categories": [], "tests": []}

    # Update or insert gate_ph category
    cats = manifest.get("categories", [])
    cats = [c for c in cats if (c.get("id") or c.get("categoryId")) != "gate_ph"]
    cats.append(gate_data["category"])
    manifest["categories"] = cats

    # Replace old repeating gate_ph tests with the 67 verified unique GATE PH papers
    tests = manifest.get("tests", [])
    tests = [t for t in tests if (t.get("category_id") or t.get("categoryId")) != "gate_ph"]
    tests.extend(gate_data["tests"])
    manifest["tests"] = tests
    manifest["manifest_version"] = manifest.get("manifest_version", 1) + 1

    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    # Also copy tests/gate_ph/*.json into tests/*.json if flat path is used by any client
    os.makedirs("tests", exist_ok=True)
    for src in glob.glob(os.path.join("tests", "gate_ph", "*.json")):
        shutil.copy2(src, os.path.join("tests", os.path.basename(src)))

    print(f"Successfully merged {len(gate_data['tests'])} GATE Physics papers ({gate_data['total_gate_ph_questions']} unique bilingual questions) into manifest.json!")

if __name__ == "__main__":
    main()
