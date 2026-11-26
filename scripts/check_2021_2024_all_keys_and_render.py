# -*- coding: utf-8 -*-
import os, json, re, pymupdf

os.makedirs("temp_gate_pdfs/renders", exist_ok=True)

# 1. Extract 2024 official PDF text & render Q47, Q61 pages
doc24 = pymupdf.open("temp_gate_pdfs/gate_ph_2024_official.pdf")
for i, page in enumerate(doc24):
    t = page.get_text()
    if "Q.47" in t or "Q.61" in t:
        pix = page.get_pixmap(dpi=150)
        out = f"temp_gate_pdfs/renders/2024_p{i+1}.png"
        pix.save(out)
        print(f"Rendered 2024 page {i+1} -> {out}")

# 2. Render 2022 Q34, Q59, Q60, Q63
doc22 = pymupdf.open("temp_gate_pdfs/gate_ph_2022_official.pdf")
for i, page in enumerate(doc22):
    t = page.get_text()
    if any(q in t for q in ["Q.34", "Q.59", "Q.60", "Q.63"]):
        pix = page.get_pixmap(dpi=150)
        out = f"temp_gate_pdfs/renders/2022_p{i+1}.png"
        pix.save(out)
        print(f"Rendered 2022 page {i+1} -> {out}")

# 3. Render 2023 Q63
doc23 = pymupdf.open("temp_gate_pdfs/gate_ph_2023_official.pdf")
for i, page in enumerate(doc23):
    t = page.get_text()
    if "Q.63" in t:
        pix = page.get_pixmap(dpi=150)
        out = f"temp_gate_pdfs/renders/2023_p{i+1}.png"
        pix.save(out)
        print(f"Rendered 2023 page {i+1} -> {out}")

# 4. Check 2021-2024 explanations for contradiction with keys
for yr in [2021, 2022, 2023, 2024]:
    d = json.load(open(f"tests/gate/gate_ph/pyq/gate_ph_pyq_{yr}.json", encoding="utf-8"))
    print(f"\n=== Auditing {yr} explanations vs keys ===")
    for q in d["questions"]:
        qn = q["questionNumber"]
        qt = q["questionType"]
        exp = q["explanationEn"]
        if qt == "MCQ":
            co = q["correctOption"]
            # Check if explanation explicitly says another Option (X) is correct at the end
            m = re.findall(r'Option\s*\(?([ABCD])\)?\s*is\s*correct|correct\s*option\s*is\s*\(?([ABCD])\)?|\(([ABCD])\)\s*$', exp[-100:], re.I)
            if m:
                letters = [x for tup in m for x in tup if x]
                if letters and letters[-1].upper() != co:
                    print(f"  {yr} Q{qn} MCQ mismatch? key={co}, exp_mentions={letters}")
        elif qt == "NAT":
            nmin, nmax = q["natMin"], q["natMax"]
            # Check if last 150 chars contain nmin or int(nmin)
            tail = exp[-180:]
            s_min = str(int(nmin)) if nmin == int(nmin) else str(nmin)
            if s_min not in tail and str(nmin) not in tail and str(nmax) not in tail:
                print(f"  {yr} Q{qn} NAT tail doesn't mention {nmin}-{nmax}: {tail!r}")
