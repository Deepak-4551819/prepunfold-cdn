# -*- coding: utf-8 -*-
import zipfile, json, re

ZIP_MOCKS = r"C:\Users\yedde\Downloads\gate_ph_mocks_and_topic_tests.zip"
with zipfile.ZipFile(ZIP_MOCKS, "r") as z:
    m1 = json.loads(z.read("full_mocks/gate_ph_mock_01.json").decode("utf-8"))
    print("Mock 01 sections:", set((q["sectionId"], q["sectionTitle"]) for q in m1["questions"]))

# Check unwrapped latex in 2021-2026 options
for yr in [2021, 2022, 2023, 2024, 2025, 2026]:
    d = json.load(open(f"tests/gate/gate_ph/pyq/gate_ph_pyq_{yr}.json", encoding="utf-8"))
    print(f"\n=== {yr} Unwrapped Options ===")
    for q in d["questions"]:
        qn = q["questionNumber"]
        for i, o in enumerate(q.get("optionsEn") or []):
            if ("\\" in o or "^" in o or "_" in o) and "$" not in o:
                print(f"  Q{qn} opt{i}: {repr(o)}")
