# -*- coding: utf-8 -*-
import zipfile
import json
from collections import Counter

ZIP_PATH = r"C:\Users\yedde\Downloads\gate_ph_mocks_and_topic_tests.zip"

with zipfile.ZipFile(ZIP_PATH, "r") as z:
    names = sorted(z.namelist())
    print(f"Total entries in zip: {len(names)}")
    for n in names:
        print(" ", n)
    print("\n--- Inspecting sample files ---")
    json_names = [n for n in names if n.endswith(".json")]
    print(f"Total JSON files: {len(json_names)}")
    for n in json_names[:3] + json_names[-2:]:
        d = json.loads(z.read(n).decode("utf-8"))
        print(f"\nFile: {n}")
        print("  Top keys:", list(d.keys()))
        print("  testId:", d.get("testId"), "testType:", d.get("testType"), "totalQuestions:", d.get("totalQuestions"), "maxMarks:", d.get("maxMarks"))
        print("  partId:", d.get("partId"), "part_id:", d.get("part_id"))
        qs = d.get("questions", [])
        if qs:
            print("  Q1 keys:", list(qs[0].keys()))
            print("  Q1:", json.dumps(qs[0], ensure_ascii=False)[:400])
