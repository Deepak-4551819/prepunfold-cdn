import fitz # PyMuPDF

doc = fitz.open("raw_pdfs/gate_cs/gate_cs_2025_q.pdf")
with open("scripts/diagram_questions_text.txt", "w", encoding="utf-8") as f:
    for page_idx in range(len(doc)):
        text = doc[page_idx].get_text()
        for qnum in [40, 50, 53, 55, 57, 59, 60, 62, 64]:
            if f"Q.{qnum}" in text or f"Q.{qnum} " in text:
                f.write(f"\n================ PAGE {page_idx+1} (Q{qnum}) ================\n")
                f.write(text)
