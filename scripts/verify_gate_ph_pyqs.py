# -*- coding: utf-8 -*-
import os
import json

PYQ_DIR = "tests/gate/gate_ph/pyq"
YEARS = [2022, 2023, 2024, 2025, 2026]

EXPECTED_KEYS = [
    "questionId", "questionNumber", "sectionId", "sectionTitle",
    "questionType", "positiveMarks", "negativeMarks", "pyqTag",
    "topicTag", "difficulty", "correctOption", "correctOptionsList",
    "correct_index", "correct_indices", "natMin", "natMax",
    "questionTextEn", "optionsEn", "explanationEn"
]

print("=== VERIFYING GATE PH PYQS (2022–2026) ===")

# Check 2021 deletion
path_2021 = os.path.join(PYQ_DIR, "gate_ph_pyq_2021.json")
if os.path.exists(path_2021):
    print(f"❌ ERROR: {path_2021} still exists on disk!")
else:
    print(f"✅ Verified: gate_ph_pyq_2021.json successfully deleted from disk.")

for y in YEARS:
    path = os.path.join(PYQ_DIR, f"gate_ph_pyq_{y}.json")
    if not os.path.exists(path):
        print(f"❌ ERROR: Missing {path}")
        continue

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    qs = data.get("questions", [])
    if len(qs) != 65:
        print(f"❌ {y}: Expected 65 questions, found {len(qs)}")
        continue

    tot_marks = 0.0
    bad_opts = 0
    bad_keys = 0
    bad_nats = 0

    for q in qs:
        qn = q.get("questionNumber")
        qt = q.get("questionType")
        pos = q.get("positiveMarks", 0.0)
        tot_marks += pos

        # Check keys
        q_keys = list(q.keys())
        if q_keys != EXPECTED_KEYS:
            bad_keys += 1

        opts = q.get("optionsEn") or []
        if qt in ("MCQ", "MSQ"):
            if len(opts) != 4 or any(len(o.strip()) == 0 for o in opts):
                bad_opts += 1
                print(f"   {y} Q{qn} ({qt}) bad options: {opts}")
        elif qt == "NAT":
            if q.get("natMin") is None or q.get("natMax") is None:
                bad_nats += 1
                print(f"   {y} Q{qn} (NAT) missing min/max: min={q.get('natMin')}, max={q.get('natMax')}")

    print(f"✅ {y}: 65 Qs | Total Marks: {tot_marks:.1f} | Bad Keys: {bad_keys} | Bad Opts: {bad_opts} | Bad NATs: {bad_nats}")

# Check manifest
with open("manifest.json", "r", encoding="utf-8") as f:
    manifest = json.load(f)

ph_tests = [t for t in manifest["tests"] if (t.get("category_id") or t.get("categoryId")) == "gate_ph"]
print(f"\nManifest gate_ph total tests: {len(ph_tests)}")

type_counts = {}
for t in ph_tests:
    tt = t.get("test_type") or t.get("testType")
    type_counts[tt] = type_counts.get(tt, 0) + 1

print(f"Breakdown: {type_counts}")

pyq_ids = [t.get("test_id") or t.get("testId") for t in ph_tests if (t.get("test_type") or t.get("testType")) == "PYQ"]
print(f"PYQ test IDs in manifest: {pyq_ids}")

if pyq_ids == ["gate_ph_pyq_2022", "gate_ph_pyq_2023", "gate_ph_pyq_2024", "gate_ph_pyq_2025", "gate_ph_pyq_2026"]:
    print("✅ Perfect! PYQs in manifest are strictly 2022 to 2026 in exact chronological order.")
else:
    print(f"❌ Unexpected PYQs: {pyq_ids}")
