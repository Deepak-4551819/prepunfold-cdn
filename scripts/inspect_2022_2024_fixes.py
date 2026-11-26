# -*- coding: utf-8 -*-
import json, pdfplumber, re

# 1. Check 2025 & 2026 NAT correctOption & 2m MCQ negativeMarks
for yr in [2025, 2026]:
    d = json.load(open(f"tests/gate/gate_ph/pyq/gate_ph_pyq_{yr}.json", encoding="utf-8"))
    nats = [(q["questionNumber"], q["correctOption"], q["natMin"], q["natMax"]) for q in d["questions"] if q["questionType"] == "NAT"]
    negs = set(q["negativeMarks"] for q in d["questions"] if q["questionType"] == "MCQ" and q["positiveMarks"] == 2.0)
    print(f"{yr} 2m MCQ negMarks: {negs}")
    print(f"{yr} NAT samples: {nats[:6]}")

# 2. Extract 2022 PDF text with pdfplumber (layout=True) for target Qs
print("\n=== EXTRACTING 2022 OFFICIAL PDF FOR Q29, Q31-35, Q59-64 ===")
with pdfplumber.open("temp_gate_pdfs/gate_ph_2022_official.pdf") as pdf:
    txt22 = "\n===PAGE===\n".join(p.extract_text() or "" for p in pdf.pages)
with open("temp_gate_pdfs/gate_ph_2022_official.txt", "w", encoding="utf-8") as f:
    f.write(txt22)

for qn in [29, 31, 32, 33, 34, 35, 59, 60, 61, 62, 63, 64]:
    m = re.search(rf'(Q\.{qn}\b[\s\S]*?)(?=Q\.{qn+1}\b|\Z)', txt22)
    print(f"\n--- 2022 PDF Q.{qn} ---")
    if m:
        print(m.group(1)[:600])
    else:
        print("NOT FOUND with regex")

# 3. Extract 2023 PDF text for Q43, 44, 60, 63
print("\n=== EXTRACTING 2023 OFFICIAL PDF FOR Q43, 44, 60, 63 ===")
with pdfplumber.open("temp_gate_pdfs/gate_ph_2023_official.pdf") as pdf:
    txt23 = "\n===PAGE===\n".join(p.extract_text() or "" for p in pdf.pages)
with open("temp_gate_pdfs/gate_ph_2023_official.txt", "w", encoding="utf-8") as f:
    f.write(txt23)

for qn in [43, 44, 60, 63]:
    m = re.search(rf'(Q\.{qn}\b[\s\S]*?)(?=Q\.{qn+1}\b|\Z)', txt23)
    print(f"\n--- 2023 PDF Q.{qn} ---")
    if m:
        print(m.group(1)[:600])
    else:
        print("NOT FOUND with regex")
