# -*- coding: utf-8 -*-
import json, re

YEARS = [2021, 2022, 2023, 2024, 2025, 2026]

for y in YEARS:
    path = f"tests/gate/gate_ph/pyq/gate_ph_pyq_{y}.json"
    d = json.load(open(path, encoding="utf-8"))
    qs = d["questions"]
    print(f"\n==================== {y} ({len(qs)} Qs) ====================")
    unwrapped_opts = []
    dup_opts = []
    neg_066 = []
    bad_qid = []
    nat_null_co = []
    placeholder_exp = []
    fig_refs = []
    bleed_suspects = []
    bad_chars = []

    for q in qs:
        qn = q["questionNumber"]
        qt = q["questionType"]
        qid = q["questionId"]
        pm = q["positiveMarks"]
        nm = q["negativeMarks"]
        opts = q.get("optionsEn") or []
        txt = q.get("questionTextEn") or ""
        exp = q.get("explanationEn") or ""

        expected_qid = f"gate_ph_{y}_q{qn:02d}"
        if qid != expected_qid:
            bad_qid.append((qn, qid, expected_qid))

        if qt == "MCQ" and pm == 2.0 and nm != 0.67:
            neg_066.append((qn, nm))

        if qt == "NAT" and q.get("correctOption") is None:
            nat_null_co.append(qn)

        if qt in ("MCQ", "MSQ"):
            if len(set(o.strip() for o in opts)) < len(opts):
                dup_opts.append((qn, opts))
            for idx, o in enumerate(opts):
                # check unwrapped latex
                if ("\\" in o or "^" in o or "_" in o) and "$" not in o:
                    unwrapped_opts.append((qn, idx, o[:60]))
                # bleed into option D
                if idx == 3 and ("\n" in o or len(o) > 120):
                    bleed_suspects.append((qn, "optD", o[:80]))

        if "Official GATE" in exp and "Answer Key:" in exp:
            placeholder_exp.append(qn)

        if re.search(r"\b(figure|shown|schematic|diagram|circuit|graph|below)\b", txt, re.I):
            fig_refs.append(qn)

        if "\ufffd" in txt + exp + "".join(opts) or "(cid:" in txt + exp + "".join(opts):
            bad_chars.append(qn)

    print(f"  bad_qid ({len(bad_qid)}): {bad_qid[:5]}")
    print(f"  neg_066 ({len(neg_066)}): {neg_066[:5]}")
    print(f"  nat_null_co ({len(nat_null_co)}): {nat_null_co[:5]}")
    print(f"  dup_opts ({len(dup_opts)}): {dup_opts}")
    print(f"  unwrapped_opts ({len(unwrapped_opts)}): {unwrapped_opts[:8]}")
    print(f"  placeholder_exp ({len(placeholder_exp)}): {placeholder_exp[:10]}")
    print(f"  fig_refs ({len(fig_refs)}): {fig_refs}")
    print(f"  bleed_suspects ({len(bleed_suspects)}): {bleed_suspects[:8]}")
    print(f"  bad_chars ({len(bad_chars)}): {bad_chars}")
