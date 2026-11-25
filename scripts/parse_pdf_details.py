import pymupdf, re

def parse_pdf(pdf_path):
    doc = pymupdf.open(pdf_path)
    # Remove header/footer
    full_text = ""
    for page_num in range(len(doc)):
        page = doc[page_num]
        lines = page.get_text().split("\n")
        filtered = []
        for line in lines:
            # Filter headers & footers
            if "Organizing Institute" in line or "Organising Institute" in line:
                continue
            if "Computer Science and Information Technology" in line:
                continue
            if re.match(r'^\s*Page\s+\d+\s+of\s+\d+\s*$', line, re.I):
                continue
            filtered.append(line)
        full_text += "\n" + "\n".join(filtered)

    # Split by Q.1, Q.2, ... Q.65
    # Be careful not to match Q.1 - Q.5 Carry ONE mark Each
    # Regex for question start: newline followed by Q.<num> and newline (or space and newline)
    pattern = r'\n\s*Q\s*\.\s*(\d+)\s*\n'
    splits = list(re.finditer(pattern, full_text))
    print(f"Total regex splits for {pdf_path}: {len(splits)}")

    questions = {}
    for i in range(len(splits)):
        m = splits[i]
        qnum = int(m.group(1))
        start = m.end()
        end = splits[i+1].start() if i+1 < len(splits) else len(full_text)
        chunk = full_text[start:end].strip()
        questions[qnum] = chunk

    print(f"Parsed {len(questions)} questions")
    return questions

q24 = parse_pdf('raw_pdfs/gate_cs/gate_cs_2024_q.pdf')
q25 = parse_pdf('raw_pdfs/gate_cs/gate_cs_2025_q.pdf')

for q in [1, 2, 11, 22, 32, 36, 44, 54]:
    print(f"--- 2024 Q.{q} ---")
    print(q24.get(q, "MISSING")[:250])
    print()

for q in [1, 2, 11, 21, 29, 36, 46, 51]:
    print(f"--- 2025 Q.{q} ---")
    print(q25.get(q, "MISSING")[:250])
    print()
