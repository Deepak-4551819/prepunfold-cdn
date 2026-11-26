# -*- coding: utf-8 -*-
import json
import zipfile
import sys
from collections import Counter

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ZIP_PATH = r"C:\Users\yedde\Downloads\gate_ph_official_pyqs_2022_2026.zip"

with zipfile.ZipFile(ZIP_PATH, "r") as z:
    for name in sorted(z.namelist()):
        if not name.endswith(".json"):
            continue
        print("=" * 60)
        print(f"FILE: {name}")
        print("=" * 60)
        d = json.loads(z.read(name).decode("utf-8"))
        qs = d.get("questions", [])

        # Check sections
        sec_counts = Counter(q.get("sectionId") for q in qs)
        sec_title_counts = Counter(q.get("sectionTitle") for q in qs)
        print("sectionId counts:", dict(sec_counts))
        print("sectionTitle counts:", dict(sec_title_counts))

        # Check question numbers
        qnums = [q.get("questionNumber") for q in qs]
        print(f"qnum range: min={min(qnums)}, max={max(qnums)}, len={len(qnums)}, unique={len(set(qnums))}")

        # Check marks breakdown
        marks_dist = Counter((q.get("sectionId"), q.get("positiveMarks"), q.get("questionType")) for q in qs)
        print("Marks breakdown:")
        for k, v in sorted(marks_dist.items()):
            print(f"  {k}: {v}")

        # Check duplicates
        stems = [q.get("questionTextEn", "").strip() for q in qs]
        c = Counter(stems)
        dups = {k: v for k, v in c.items() if v > 1}
        print(f"Duplicate stems count: {len(dups)}")
        if dups:
            for k, v in dups.items():
                print(f"  DUP ({v}x): {k[:60]}")

        # Print sample questions
        for idx in [0, 9, 10, 15, 34, 35, 64]:
            if idx < len(qs):
                q = qs[idx]
                print(f"  Q{q.get('questionNumber')} [sec={q.get('sectionId')}, {q.get('positiveMarks')}M, {q.get('questionType')}]: {q.get('questionTextEn')[:80]}")
