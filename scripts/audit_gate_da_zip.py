import zipfile
import json
import re

zip_path = r"C:\Users\yedde\Downloads\gate_da_official_pyqs_2024_2026.zip"

with zipfile.ZipFile(zip_path, "r") as z:
    for yr in [2024, 2025, 2026]:
        fname = f"gate_da_pyq_{yr}.json"
        data = json.loads(z.read(fname).decode("utf-8"))
        qs = data.get("questions", [])
        total_marks = sum(q.get("positiveMarks", 0) for q in qs)
        qtypes = {}
        for q in qs:
            qt = q.get("questionType")
            qtypes[qt] = qtypes.get(qt, 0) + 1

        # Check anomalies
        short_stem = [q["questionNumber"] for q in qs if len(q.get("questionTextEn", "").strip()) < 15]
        empty_opts = [q["questionNumber"] for q in qs if q.get("questionType") in ("MCQ", "MSQ") and (len(q.get("optionsEn", [])) != 4 or any(not o.strip() for o in q.get("optionsEn", [])))]
        cid_artifacts = [q["questionNumber"] for q in qs if "(cid:" in q.get("questionTextEn", "") or any("(cid:" in o for o in q.get("optionsEn", []))]
        mta_qs = [q["questionNumber"] for q in qs if q.get("is_mta") or "MTA" in q.get("explanationEn", "")]

        print(f"\n==============================")
        print(f"Year {yr} ({fname}):")
        print(f"  Total Qs: {len(qs)}, Total Marks: {total_marks}")
        print(f"  Question Types: {qtypes}")
        print(f"  Short stems (<15 chars): {short_stem}")
        print(f"  Empty options: {empty_opts}")
        print(f"  CID artifacts: {cid_artifacts}")
        print(f"  MTA questions: {mta_qs}")

        # Check sections
        sec_counts = {}
        for q in qs:
            s = q.get("sectionId")
            sec_counts[s] = sec_counts.get(s, 0) + 1
        print(f"  Section counts: {sec_counts}")
