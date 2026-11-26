# -*- coding: utf-8 -*-
import sys
import os
import json
import zipfile
import re

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ZIP_PATH = r"C:\Users\yedde\Downloads\gate_cy_official_pyqs_2022_2026.zip"

print(f"Inspecting zip: {ZIP_PATH}")
with zipfile.ZipFile(ZIP_PATH, 'r') as z:
    for name in sorted(z.namelist()):
        info = z.getinfo(name)
        print(f"\nFile: {name} ({info.file_size} bytes)")
        if name.endswith('.json') and 'snippet' not in name:
            data = json.loads(z.read(name).decode('utf-8'))
            print("  Top-level keys:", list(data.keys()))
            qs = data.get("questions", [])
            print(f"  Total questions: {len(qs)}")
            print(f"  Max marks: {data.get('maxMarks')}")

            # Check question counts by type
            qtypes = {}
            for q in qs:
                qt = q.get("questionType")
                qtypes[qt] = qtypes.get(qt, 0) + 1
            print(f"  Question types: {qtypes}")

            # Check sections
            secs = {}
            for q in qs:
                sid = q.get("sectionId")
                secs[sid] = secs.get(sid, 0) + 1
            print(f"  Sections: {secs}")

            # Check marks sum
            marks_sum = sum(q.get("positiveMarks", 0) for q in qs)
            print(f"  Positive marks sum: {marks_sum}")

            # Check negative marks
            bad_neg = []
            for q in qs:
                qt = q.get("questionType")
                pos = q.get("positiveMarks")
                neg = q.get("negativeMarks")
                qnum = q.get("questionNumber")
                is_mta = "MTA" in (str(q.get("correctOption")) + str(q.get("explanationEn")))
                if is_mta:
                    if neg != 0.0:
                        bad_neg.append((qnum, qt, pos, neg, "MTA not 0.0"))
                elif qt == "MCQ":
                    if pos == 1.0 and abs(neg - 0.33) > 0.01:
                        bad_neg.append((qnum, qt, pos, neg, "1m MCQ not 0.33"))
                    elif pos == 2.0 and abs(neg - 0.67) > 0.01:
                        bad_neg.append((qnum, qt, pos, neg, "2m MCQ not 0.67"))
                elif qt in ("MSQ", "NAT"):
                    if neg != 0.0:
                        bad_neg.append((qnum, qt, pos, neg, f"{qt} not 0.0"))
            if bad_neg:
                print(f"  Bad negative marks: {bad_neg[:5]} (total {len(bad_neg)})")
            else:
                print("  Negative marks: All standardized correctly.")

            # Check question keys
            q_key_sets = set(tuple(sorted(q.keys())) for q in qs)
            print(f"  Question key variations: {len(q_key_sets)}")
            for ks in q_key_sets:
                print(f"    Sample question keys ({len(ks)}): {ks}")

            # Check placeholder explanations or self-talk
            self_talk = []
            placeholders = []
            for q in qs:
                exp = q.get("explanationEn", "")
                qnum = q.get("questionNumber")
                if any(w in exp.lower() for w in ["wait,", "hold on", "let me re-read", "re-calculate"]):
                    self_talk.append(qnum)
                if exp.startswith("Official GATE") and len(exp.splitlines()) <= 2:
                    placeholders.append(qnum)
            if self_talk:
                print(f"  Self-talk found in questions: {self_talk}")
            print(f"  Placeholder-only explanations count: {len(placeholders)}")

            # Check empty options or short questions
            empty_opts = [q.get("questionNumber") for q in qs if q.get("questionType") in ("MCQ", "MSQ") and (len(q.get("optionsEn", [])) != 4 or any(not o for o in q.get("optionsEn", [])))]
            if empty_opts:
                print(f"  Empty/incomplete options in: {empty_opts}")
            else:
                print("  Options: All 4 options present for MCQs/MSQs.")
