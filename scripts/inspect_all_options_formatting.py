# -*- coding: utf-8 -*-
import json, glob

for yr in [2021, 2022, 2023, 2024, 2025, 2026]:
    d = json.load(open(f"tests/gate/gate_ph/pyq/gate_ph_pyq_{yr}.json", encoding="utf-8"))
    unw = []
    for q in d["questions"]:
        for i, o in enumerate(q.get("optionsEn") or []):
            if ("\\" in o or "^" in o or "_" in o) and "$" not in o:
                unw.append((q["questionNumber"], i, o))
    print(f"=== {yr} unwrapped ({len(unw)}) ===")
    for x in unw:
        print(f"  Q{x[0]}[{x[1]}]: {x[2]}")

# Check mocks/topics
mt_unw = 0
for p in glob.glob("tests/gate/gate_ph/full_mocks/*.json") + glob.glob("tests/gate/gate_ph/topic_tests/*/*.json"):
    d = json.load(open(p, encoding="utf-8"))
    for q in d["questions"]:
        for i, o in enumerate(q.get("optionsEn") or []):
            if ("\\" in o or "^" in o or "_" in o) and "$" not in o:
                mt_unw += 1
print(f"\nMocks/Topics unwrapped options count: {mt_unw}")
