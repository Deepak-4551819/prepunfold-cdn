# -*- coding: utf-8 -*-
import json, zipfile, pdfplumber, re

# 1. Extract 2023, 2024, 2025, 2026 official keys
for yr in [2023, 2024, 2025, 2026]:
    kpath = f"temp_gate_pdfs/gate_ph_{yr}_key.pdf"
    with pdfplumber.open(kpath) as pdf:
        txt = "\n".join(p.extract_text() or "" for p in pdf.pages)
    with open(f"temp_gate_pdfs/gate_ph_{yr}_key.txt", "w", encoding="utf-8") as f:
        f.write(txt)
    print(f"Saved {yr} key text ({len(txt)} chars)")

# 2. Check 2022 zip vs repo for Q29, 31-35, 59-64
ZIP_PYQ = r"C:\Users\yedde\Downloads\gate_ph_official_pyqs_2022_2026.zip"
with zipfile.ZipFile(ZIP_PYQ, "r") as z:
    z22 = json.loads(z.read("pyqs/gate_ph_pyq_2022.json").decode("utf-8"))
    z23 = json.loads(z.read("pyqs/gate_ph_pyq_2023.json").decode("utf-8"))
    z24 = json.loads(z.read("pyqs/gate_ph_pyq_2024.json").decode("utf-8"))

r22 = json.load(open("tests/gate/gate_ph/pyq/gate_ph_pyq_2022.json", encoding="utf-8"))
r23 = json.load(open("tests/gate/gate_ph/pyq/gate_ph_pyq_2023.json", encoding="utf-8"))
r24 = json.load(open("tests/gate/gate_ph/pyq/gate_ph_pyq_2024.json", encoding="utf-8"))

print("\n=== 2022 NAT MISMATCHES (Repo vs Zip vs PDF) ===")
pdf22_txt = open("temp_gate_pdfs/gate_ph_2022_text.txt", encoding="utf-8").read()
for qn in [29, 31, 32, 33, 34, 35, 59, 60, 61, 62, 63, 64]:
    rq = r22["questions"][qn-1]
    zq = z22["questions"][qn-1]
    print(f"\n--- 2022 Q{qn} ---")
    print(f"  Repo text: {rq['questionTextEn'][:220]}")
    print(f"  Repo min/max: {rq['natMin']} / {rq['natMax']}")
    print(f"  Zip text:  {zq['questionTextEn'][:220]}")
    print(f"  Zip key:   {zq['correctOption']} ({zq['natMin']} / {zq['natMax']})")

print("\n=== 2023 CHECKS (Q43, Q44, Q60, Q63) ===")
for qn in [43, 44, 60, 63]:
    rq = r23["questions"][qn-1]
    zq = z23["questions"][qn-1]
    print(f"\n--- 2023 Q{qn} ---")
    print(f"  Repo opts: {rq['optionsEn']} | ans: {rq['correctOption']} | min/max: {rq['natMin']}/{rq['natMax']}")
    print(f"  Zip text:  {zq['questionTextEn'][:220]}")
    print(f"  Zip opts:  {zq['optionsEn']} | ans: {zq['correctOption']} | min/max: {zq['natMin']}/{zq['natMax']}")

print("\n=== 2024 CHECKS (Q7, Q10, Q47, Q61) ===")
for qn in [7, 10, 47, 61]:
    rq = r24["questions"][qn-1]
    zq = z24["questions"][qn-1]
    print(f"\n--- 2024 Q{qn} ({rq['questionType']}) ---")
    print(f"  Repo neg={rq['negativeMarks']} ans={rq['correctOption']} list={rq['correctOptionsList']} min/max={rq['natMin']}/{rq['natMax']}")
    print(f"  Repo text: {rq['questionTextEn'][:220]}")
    print(f"  Repo opts: {rq['optionsEn']}")
    print(f"  Zip ans={zq['correctOption']} list={zq['correctOptionsList']} min/max={zq['natMin']}/{zq['natMax']}")
    print(f"  Zip text:  {zq['questionTextEn'][:220]}")
    print(f"  Zip opts:  {zq['optionsEn']}")
