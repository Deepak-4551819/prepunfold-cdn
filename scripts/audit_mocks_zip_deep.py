# -*- coding: utf-8 -*-
import zipfile, json, re

ZIP_MOCKS = r"C:\Users\yedde\Downloads\gate_ph_mocks_and_topic_tests.zip"

with zipfile.ZipFile(ZIP_MOCKS, "r") as z:
    issues = []
    for n in sorted(z.namelist()):
        if not n.endswith(".json"):
            continue
        d = json.loads(z.read(n).decode("utf-8"))
        for q in d["questions"]:
            qn = q["questionNumber"]
            qt = q["questionType"]
            txt = q.get("questionTextEn", "")
            exp = q.get("explanationEn", "")
            opts = q.get("optionsEn", [])
            if len(txt.strip()) < 15:
                issues.append((n, qn, "short stem"))
            if len(exp.strip()) < 15:
                issues.append((n, qn, "short exp"))
            if "placeholder" in exp.lower():
                issues.append((n, qn, "placeholder exp"))
            if qt in ("MCQ", "MSQ"):
                if len(opts) != 4 or len(set(o.strip() for o in opts)) < 4:
                    issues.append((n, qn, f"bad/dup opts: {opts}"))
                for idx, o in enumerate(opts):
                    if ("\\" in o) and "$" not in o:
                        issues.append((n, qn, f"unwrapped latex opt {idx}: {o[:40]}"))
            if qt == "NAT":
                if q.get("natMin") is None or q.get("natMax") is None:
                    issues.append((n, qn, "NAT missing min/max"))
                if not isinstance(q.get("correctOption"), str):
                    issues.append((n, qn, f"NAT non-str correctOption: {q.get('correctOption')}"))
    print(f"Total issues in gate_ph_mocks_and_topic_tests.zip: {len(issues)}")
    for i in issues[:20]:
        print(" ", i)
