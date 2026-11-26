# -*- coding: utf-8 -*-
import os, json, re, zipfile, glob
from collections import Counter

print("=== 1. CHECKING GATE CS NAT & 2M MCQ CONVENTIONS ===")
cs_nat_correct_opts = Counter()
cs_2m_neg = Counter()
for p in glob.glob("tests/gate/gate_cs/**/*.json", recursive=True):
    d = json.load(open(p, encoding="utf-8"))
    for q in d.get("questions", []):
        if q.get("questionType") == "NAT":
            cs_nat_correct_opts[type(q.get("correctOption")).__name__ + ":" + str(q.get("correctOption"))] += 1
        if q.get("questionType") == "MCQ" and q.get("positiveMarks") == 2.0:
            cs_2m_neg[q.get("negativeMarks")] += 1
print("GATE CS NAT correctOption types/samples:", list(cs_nat_correct_opts.items())[:5])
print("GATE CS 2M MCQ negativeMarks:", dict(cs_2m_neg))

print("\n=== 2. AUDITING gate_ph_mocks_and_topic_tests.zip ===")
ZIP_PATH = r"C:\Users\yedde\Downloads\gate_ph_mocks_and_topic_tests.zip"
with zipfile.ZipFile(ZIP_PATH, "r") as z:
    parts_seen = {}
    neg_marks_2m = Counter()
    nat_co = Counter()
    opt_dist = Counter()
    all_stems = []
    bad_items = []
    for n in sorted(z.namelist()):
        if not n.endswith(".json"):
            continue
        d = json.loads(z.read(n).decode("utf-8"))
        if d.get("partId"):
            parts_seen[d["partId"]] = d.get("partTitle")
        qs = d.get("questions", [])
        tot_m = sum(q.get("positiveMarks", 0) for q in qs)
        for q in qs:
            qt = q.get("questionType")
            pm = q.get("positiveMarks")
            nm = q.get("negativeMarks")
            if qt == "MCQ" and pm == 2.0:
                neg_marks_2m[nm] += 1
            if qt == "NAT":
                nat_co[type(q.get("correctOption")).__name__] += 1
                if q.get("natMin") is None or q.get("natMax") is None:
                    bad_items.append((n, q["questionNumber"], "NAT missing min/max"))
            if qt == "MCQ":
                opt_dist[q.get("correctOption")] += 1
                opts = q.get("optionsEn") or []
                if len(opts) != 4 or len(set(o.strip() for o in opts)) < 4:
                    bad_items.append((n, q["questionNumber"], f"MCQ bad/dup opts: {opts}"))
            if qt == "MSQ":
                opts = q.get("optionsEn") or []
                if len(opts) != 4 or len(set(o.strip() for o in opts)) < 4:
                    bad_items.append((n, q["questionNumber"], f"MSQ bad/dup opts: {opts}"))
            all_stems.append((n, q["questionNumber"], q.get("questionTextEn", "")))
    print("Parts in zip:", json.dumps(parts_seen, indent=2))
    print("2M MCQ negativeMarks in zip:", dict(neg_marks_2m))
    print("NAT correctOption types in zip:", dict(nat_co))
    print("MCQ answer distribution in zip:", dict(opt_dist))
    print("Bad items in zip:", len(bad_items), bad_items[:10])
    # Duplicate stem check within zip
    stem_counts = Counter(re.sub(r"\s+", " ", s[2].strip().lower()) for s in all_stems)
    dups = [(k[:60], v) for k, v in stem_counts.items() if v > 1]
    print("Duplicate stems in zip:", len(dups), dups[:5])
