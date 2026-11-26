# -*- coding: utf-8 -*-
import json, zipfile, pdfplumber, re

# Check if fitz (PyMuPDF) is available
try:
    import fitz
    print("PyMuPDF (fitz) is available!")
except ImportError:
    print("PyMuPDF (fitz) NOT available")

# Check zip mocks/topics metadata
ZIP_MOCKS = r"C:\Users\yedde\Downloads\gate_ph_mocks_and_topic_tests.zip"
with zipfile.ZipFile(ZIP_MOCKS, "r") as z:
    print("\n=== ZIP MOCKS & TOPICS METADATA ===")
    for n in sorted(z.namelist()):
        if not n.endswith(".json"):
            continue
        d = json.loads(z.read(n).decode("utf-8"))
        qs = d["questions"]
        tot_m = sum(q["positiveMarks"] for q in qs)
        print(f"{n:42s} | id={d['testId']:24s} | free={str(d['isFree']):5s} | Qs={len(qs)} | Marks={tot_m} | part={d.get('partId')}")

# Check 2021-2024 negativeMarks, key mismatches, and 2024 zip Q47, Q61
ZIP_PYQ = r"C:\Users\yedde\Downloads\gate_ph_official_pyqs_2022_2026.zip"
with zipfile.ZipFile(ZIP_PYQ, "r") as z:
    z24 = json.loads(z.read("pyqs/gate_ph_pyq_2024.json").decode("utf-8"))
    for qn in [47, 61]:
        print(f"\n=== ZIP 2024 Q{qn} FULL ===")
        print(json.dumps(z24["questions"][qn-1], ensure_ascii=False, indent=2))
