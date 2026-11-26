# -*- coding: utf-8 -*-
import json, re, zipfile

print("=== GATE PH 2021 AUDIT ===")
d21 = json.load(open("tests/gate/gate_ph/pyq/gate_ph_pyq_2021.json", encoding="utf-8"))
print("2021 top keys:", list(d21.keys()))
print("2021 total Qs:", len(d21["questions"]), "total marks:", sum(q["positiveMarks"] for q in d21["questions"]))
for q in d21["questions"]:
    qn = q["questionNumber"]
    qt = q["questionType"]
    opts = q.get("optionsEn") or []
    if qt in ("MCQ", "MSQ") and (len(opts) != 4 or len(set(o.strip() for o in opts)) < 4):
        print(f"  2021 Q{qn} ({qt}) bad/dup opts:", opts)
    if qt == "NAT" and (q.get("natMin") is None or q.get("natMax") is None):
        print(f"  2021 Q{qn} (NAT) missing min/max:", q.get("natMin"), q.get("natMax"))
    if q.get("positiveMarks") == 2.0 and qt == "MCQ" and q.get("negativeMarks") != 0.67:
        pass # we'll count below
print("2021 2m MCQ negMarks:", set(q.get("negativeMarks") for q in d21["questions"] if q["questionType"] == "MCQ" and q["positiveMarks"] == 2.0))
print("2021 NAT correctOption sample:", [(q["questionNumber"], q.get("correctOption"), q.get("natMin"), q.get("natMax")) for q in d21["questions"] if q["questionType"] == "NAT"][:5])

print("\n=== ZIP MOCKS/TOPICS NAT & SCHEMA CHECK ===")
ZIP_PATH = r"C:\Users\yedde\Downloads\gate_ph_mocks_and_topic_tests.zip"
with zipfile.ZipFile(ZIP_PATH, "r") as z:
    d_m1 = json.loads(z.read("full_mocks/gate_ph_mock_01.json").decode("utf-8"))
    nats = [q for q in d_m1["questions"] if q["questionType"] == "NAT"]
    print("Mock 01 NAT samples:", [(q["questionNumber"], q.get("correctOption"), q.get("natMin"), q.get("natMax")) for q in nats[:5]])
    # Check unwrapped latex or other issues in zip
    unwrapped = 0
    for n in z.namelist():
        if n.endswith(".json"):
            d = json.loads(z.read(n).decode("utf-8"))
            for q in d["questions"]:
                for o in q.get("optionsEn") or []:
                    if ("\\" in o) and "$" not in o:
                        unwrapped += 1
    print("Zip options with backslash but no $:", unwrapped)

print("\n=== CHECKING 2022, 2023, 2024 REPORTED ISSUES ===")
d22 = json.load(open("tests/gate/gate_ph/pyq/gate_ph_pyq_2022.json", encoding="utf-8"))
print("--- 2022 NATs (Q29, Q31-35, Q59-64) ---")
for q in d22["questions"]:
    if q["questionNumber"] in [29, 31, 32, 33, 34, 35, 59, 60, 61, 62, 63, 64]:
        print(f"Q{q['questionNumber']}: natMin={q['natMin']} natMax={q['natMax']} | exp={q['explanationEn'][-120:]}")

d23 = json.load(open("tests/gate/gate_ph/pyq/gate_ph_pyq_2023.json", encoding="utf-8"))
print("\n--- 2023 Q43, Q44, Q60, Q63 ---")
for q in d23["questions"]:
    if q["questionNumber"] in [43, 44, 60, 63]:
        print(f"Q{q['questionNumber']} ({q['questionType']}): opts={q.get('optionsEn')} | correct={q.get('correctOption')} | min/max={q.get('natMin')}/{q.get('natMax')}")
        print(f"  text={q['questionTextEn'][:200]}")
        print(f"  exp={q['explanationEn']}")

d24 = json.load(open("tests/gate/gate_ph/pyq/gate_ph_pyq_2024.json", encoding="utf-8"))
print("\n--- 2024 Q47, Q61, and questionIds ---")
for q in d24["questions"]:
    if q["questionNumber"] in [47, 61]:
        print(f"Q{q['questionNumber']} ({q['questionType']}): correct={q.get('correctOption')} min/max={q.get('natMin')}/{q.get('natMax')}")
        print(f"  text={q['questionTextEn'][:200]}")
        print(f"  exp={q['explanationEn']}")
print("2024 Q1, Q10, Q65 IDs:", [d24["questions"][i]["questionId"] for i in [0, 9, 64]])
