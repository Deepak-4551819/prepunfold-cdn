# -*- coding: utf-8 -*-
import json, re, zipfile

# 1. Check 2022 Q35 in official PDF text
txt22 = open("temp_gate_pdfs/gate_ph_2022_official.txt", encoding="utf-8").read()
idx = txt22.find("plasma oscillations")
if idx != -1:
    print("=== 2022 Q35 in PDF ===")
    print(txt22[max(0, idx-100):idx+600])

# 2. Check 2022 Q22, Q56, Q58 in repo vs PDF
r22 = json.load(open("tests/gate/gate_ph/pyq/gate_ph_pyq_2022.json", encoding="utf-8"))
print("\n=== 2022 Q22, Q56, Q58 opts ===")
for qn in [22, 56, 58]:
    print(f"Q{qn} opts:", r22["questions"][qn-1]["optionsEn"])

# 3. Check 2021 key PDF vs 2021 json
import pdfplumber
with pdfplumber.open("temp_gate_pdfs/gate_ph_2021_key.pdf") as pdf:
    k21 = "\n".join(p.extract_text() or "" for p in pdf.pages)
print("\n=== 2021 KEY SAMPLE ===")
print(k21[:600])

# 4. Check 2023 and 2024 keys vs repo
print("\n=== 2023 KEY TEXT ===")
print(open("temp_gate_pdfs/gate_ph_2023_key.txt", encoding="utf-8").read())
print("\n=== 2024 KEY TEXT ===")
print(open("temp_gate_pdfs/gate_ph_2024_key.txt", encoding="utf-8").read())
