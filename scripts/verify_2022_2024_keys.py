# -*- coding: utf-8 -*-
import json, re

def parse_keys_from_text(txt):
    keys = {}
    for line in txt.splitlines():
        m = re.match(r'^(\d+)\s+\d+\s+(MCQ|MSQ|NAT)\s+(?:GA|PH)\s+(.+?)\s+(\d+)\s*$', line.strip())
        if m:
            qn = int(m.group(1))
            qt = m.group(2)
            ky = m.group(3).strip()
            mk = float(m.group(4))
            keys[qn] = (qt, ky, mk)
    return keys

txt22 = open("temp_gate_pdfs/gate_ph_2022_official.txt", encoding="utf-8").read()
txt23 = open("temp_gate_pdfs/gate_ph_2023_key.txt", encoding="utf-8").read()
txt24 = open("temp_gate_pdfs/gate_ph_2024_key.txt", encoding="utf-8").read()

for yr, txt in [(2022, txt22), (2023, txt23), (2024, txt24)]:
    keys = parse_keys_from_text(txt)
    d = json.load(open(f"tests/gate/gate_ph/pyq/gate_ph_pyq_{yr}.json", encoding="utf-8"))
    print(f"=== {yr} Key Comparison (parsed {len(keys)}/65) ===")
    for q in d["questions"]:
        qn = q["questionNumber"]
        if qn not in keys:
            print(f"  Q{qn}: NOT IN PARSED KEY")
            continue
        qt, ky, mk = keys[qn]
        if q["questionType"] != qt or q["positiveMarks"] != mk:
            print(f"  Q{qn} TYPE/MARKS MISMATCH: json=({q['questionType']},{q['positiveMarks']}) vs off=({qt},{mk})")
        if qt == "MCQ":
            if ky == "MTA":
                print(f"  Q{qn} MTA: json_list={q['correctOptionsList']} neg={q['negativeMarks']}")
            elif q["correctOption"] != ky:
                print(f"  Q{qn} MCQ KEY MISMATCH: json={q['correctOption']} vs off={ky}")
        elif qt == "MSQ":
            exp_list = [x.strip() for x in re.split(r"[,;]", ky)]
            if q["correctOptionsList"] != exp_list:
                print(f"  Q{qn} MSQ KEY MISMATCH: json={q['correctOptionsList']} vs off={exp_list}")
        elif qt == "NAT":
            if ky == "MTA":
                print(f"  Q{qn} NAT MTA: json=({q['natMin']},{q['natMax']})")
            else:
                parts = ky.split(" to ")
                omin, omax = float(parts[0]), float(parts[1])
                if q["natMin"] != omin or q["natMax"] != omax:
                    print(f"  Q{qn} NAT RANGE MISMATCH: json=({q['natMin']},{q['natMax']}) vs off=({omin},{omax})")

print("\n=== 2023 OFFICIAL PDF Q33-35, Q61-65 ===")
txt23_off = open("temp_gate_pdfs/gate_ph_2023_official.txt", encoding="utf-8").read()
for qn in [33, 34, 35, 61, 62, 64, 65]:
    m = re.search(rf'(Q\.{qn}\b[\s\S]*?)(?=Q\.{qn+1}\b|Q\.36|\Z)', txt23_off)
    if m:
        print(f"--- 2023 PDF Q.{qn} ---")
        print(m.group(1)[:400])
