import zipfile
import json
import re

zip_path = r"C:\Users\yedde\Downloads\gate_ph_official_pyqs_2022_2026.zip"

with zipfile.ZipFile(zip_path, 'r') as z:
    for year in [2025, 2026]:
        data = json.loads(z.read(f"pyqs/gate_ph_pyq_{year}.json").decode('utf-8'))
        qs = data["questions"]
        print(f"\n=================== DEEP AUDIT {year} ({len(qs)} questions) ===================")
        tot_marks = 0
        for q in qs:
            qn = q["questionNumber"]
            qt = q["questionType"]
            pos = q["positiveMarks"]
            neg = q["negativeMarks"]
            tot_marks += pos
            opts = q.get("optionsEn") or []
            stem = q.get("questionTextEn", "")
            ans = q.get("correctOption")
            ans_list = q.get("correctOptionsList")
            c_idx = q.get("correct_index")
            c_idxs = q.get("correct_indices")
            nat_min = q.get("natMin")
            nat_max = q.get("natMax")

            # Check opts
            if qt in ["MCQ", "MSQ"]:
                if len(opts) != 4 or any(len(o.strip()) == 0 for o in opts):
                    print(f"  Q{qn} ({qt}): bad options: {opts}")
                if qt == "MCQ" and (c_idx is None or c_idx < 0 or c_idx >= len(opts)):
                    print(f"  Q{qn} (MCQ): invalid c_idx={c_idx} for correctOption={ans}")
                if qt == "MSQ" and (not c_idxs or any(i < 0 or i >= len(opts) for i in c_idxs)):
                    print(f"  Q{qn} (MSQ): invalid c_idxs={c_idxs} for ans_list={ans_list}")
            elif qt == "NAT":
                if nat_min is None or nat_max is None:
                    print(f"  Q{qn} (NAT): missing natMin/natMax! min={nat_min}, max={nat_max}, ans={ans}")

            if len(stem.strip()) < 15:
                print(f"  Q{qn}: very short stem: {stem}")

            # check weird patterns
            if "– Q." in stem or "Carry" in stem:
                print(f"  Q{qn}: header in stem: {stem[:60]}")

        print(f"Total positive marks: {tot_marks}")
