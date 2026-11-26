# -*- coding: utf-8 -*-
import json, zipfile, requests, pymupdf

# 1. Try finding 2024 official PDF URL on gate2027.iitm.ac.in
for cand in ["PH24S1.pdf", "PH24S2.pdf", "PH24S3.pdf", "PH24S4.pdf", "PH24S6.pdf", "PH24S7.pdf", "PH24S8.pdf", "PH.pdf", "PH_2024.pdf", "PH2024.pdf"]:
    url = f"https://gate2027.iitm.ac.in/static/doc/download/2024/{cand}"
    try:
        r = requests.head(url, timeout=5)
        if r.status_code == 200:
            print("FOUND 2024 PDF:", url)
            resp = requests.get(url, timeout=20)
            with open("temp_gate_pdfs/gate_ph_2024_official.pdf", "wb") as f:
                f.write(resp.content)
            break
    except Exception:
        pass

# 2. Check 2024 Q47 and Q61 in repo vs zip
r24 = json.load(open("tests/gate/gate_ph/pyq/gate_ph_pyq_2024.json", encoding="utf-8"))
for qn in [47, 61]:
    print(f"\n=== REPO 2024 Q{qn} ===")
    print(json.dumps({k: r24["questions"][qn-1][k] for k in ["questionType", "correctOption", "correctOptionsList", "correct_indices", "natMin", "natMax", "questionTextEn", "optionsEn", "explanationEn"]}, ensure_ascii=False, indent=2))

# 3. Dump 2025 and 2026 questions from current JSON + PDF text side-by-side
for yr in [2025, 2026]:
    d = json.load(open(f"tests/gate/gate_ph/pyq/gate_ph_pyq_{yr}.json", encoding="utf-8"))
    with open(f"temp_gate_pdfs/dump_{yr}_qs.txt", "w", encoding="utf-8") as f:
        for q in d["questions"]:
            f.write(f"=== Q{q['questionNumber']} ({q['questionType']}, {q['positiveMarks']}m/{q['negativeMarks']}m, ans={q['correctOption']}, list={q['correctOptionsList']}, min={q['natMin']}, max={q['natMax']}, topic={q['topicTag']}) ===\n")
            f.write(f"STEM: {q['questionTextEn']}\n")
            f.write(f"OPTS: {q['optionsEn']}\n")
            f.write(f"EXP:  {q['explanationEn']}\n\n")
    print(f"Dumped {yr} questions to temp_gate_pdfs/dump_{yr}_qs.txt")
