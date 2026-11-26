# -*- coding: utf-8 -*-
import sys
import json
import zipfile
import re

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

zip_path = r"C:\Users\yedde\Downloads\jam_ph_official_pyqs_2022_2026.zip"

SELF_TALK_PATTERNS = [
    r"\bwait\b", r"\bhold on\b", r"\blet me check\b", r"\bofficial key confirms\b",
    r"\boh wait\b", r"\bscratch that\b", r"\bactually wait\b", r"\bwait,\b", r"\bhold on,\b"
]

with zipfile.ZipFile(zip_path, "r") as z:
    for year in range(2022, 2027):
        fname = f"jam_ph_pyq_{year}.json"
        if fname not in z.namelist():
            print(f"MISSING FILE: {fname}")
            continue

        data = json.loads(z.read(fname).decode("utf-8"))
        print(f"\n==================== {fname} ====================")
        top_keys = list(data.keys())
        print(f"Top-level keys count: {len(top_keys)}")
        print(f"Top-level keys: {top_keys}")

        qs = data.get("questions", [])
        print(f"Total questions: {len(qs)}")

        # Check marks and sections
        total_pos = 0.0
        sec_counts = {}
        qt_counts = {}
        issues = []

        for q in qs:
            qnum = q.get("questionNumber")
            qid = q.get("questionId")
            qt = q.get("questionType")
            pos = q.get("positiveMarks", 0.0)
            neg = q.get("negativeMarks", 0.0)
            sec = q.get("sectionTitle", "")
            qtext = q.get("questionTextEn", "")
            opts = q.get("optionsEn", [])
            exp = q.get("explanationEn", "")
            co = q.get("correctOption")
            col = q.get("correctOptionsList", [])
            nmin = q.get("natMin")
            nmax = q.get("natMax")

            total_pos += pos
            sec_counts[sec] = sec_counts.get(sec, 0) + 1
            qt_counts[qt] = qt_counts.get(qt, 0) + 1

            # Check question keys
            qkeys = list(q.keys())
            if len(qkeys) != 19:
                issues.append(f"Q{qnum}: Key count {len(qkeys)} != 19: {qkeys}")

            # Check questionType matches section
            if qnum <= 30 and qt != "MCQ":
                issues.append(f"Q{qnum}: expected MCQ, got {qt}")
            elif 31 <= qnum <= 40 and qt != "MSQ":
                issues.append(f"Q{qnum}: expected MSQ, got {qt}")
            elif qnum >= 41 and qt != "NAT":
                issues.append(f"Q{qnum}: expected NAT, got {qt}")

            # Check marks
            if qnum in range(1, 11) or qnum in range(41, 51):
                if pos != 1.0:
                    issues.append(f"Q{qnum}: expected 1.0 positive mark, got {pos}")
            else:
                if pos != 2.0:
                    issues.append(f"Q{qnum}: expected 2.0 positive marks, got {pos}")

            # Check negative marks
            if qt == "MCQ":
                if pos == 1.0 and abs(neg - 0.33) > 0.01:
                    issues.append(f"Q{qnum}: 1m MCQ negativeMarks is {neg}, expected 0.33")
                elif pos == 2.0 and abs(neg - 0.67) > 0.01:
                    issues.append(f"Q{qnum}: 2m MCQ negativeMarks is {neg}, expected 0.67")
            else:
                if neg != 0.0:
                    issues.append(f"Q{qnum}: {qt} negativeMarks is {neg}, expected 0.0")

            # Check options
            if qt in ("MCQ", "MSQ"):
                if len(opts) != 4:
                    issues.append(f"Q{qnum}: {qt} options count {len(opts)} != 4")
                if len(set(opts)) != len(opts) and len(opts) > 0:
                    issues.append(f"Q{qnum}: Duplicate options found: {opts}")
            elif qt == "NAT":
                if len(opts) != 0:
                    issues.append(f"Q{qnum}: NAT has non-empty options: {opts}")
                if nmin is None or nmax is None:
                    issues.append(f"Q{qnum}: NAT missing natMin or natMax: min={nmin}, max={nmax}")

            # Check LaTeX balance
            for text_field, field_name in [(qtext, "questionTextEn"), (exp, "explanationEn")] + [(opt, f"opt_{i}") for i, opt in enumerate(opts)]:
                dollar_cnt = text_field.count("$")
                if dollar_cnt % 2 != 0:
                    issues.append(f"Q{qnum} {field_name}: Unbalanced $ count ({dollar_cnt})")

            # Check self-talk
            for pat in SELF_TALK_PATTERNS:
                if re.search(pat, exp, re.IGNORECASE):
                    issues.append(f"Q{qnum}: Self-talk match '{pat}' in explanationEn: {exp[:120]}...")

        print(f"Total positive marks: {total_pos}")
        print(f"Section counts: {sec_counts}")
        print(f"Question type counts: {qt_counts}")
        print(f"Total issues found: {len(issues)}")
        if issues:
            for iss in issues[:15]:
                print(f"  - {iss}")
            if len(issues) > 15:
                print(f"  ... and {len(issues) - 15} more issues")
