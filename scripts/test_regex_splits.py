import pymupdf, re

def extract_all_questions(pdf_path):
    doc = pymupdf.open(pdf_path)
    clean_lines = []
    for page in doc:
        for line in page.get_text().splitlines():
            # Filter page header/footer
            if "Organizing Institute" in line or "Organising Institute" in line:
                continue
            if "Computer Science and Information Technology" in line:
                continue
            if re.match(r'^\s*Page\s+\d+\s+of\s+\d+\s*$', line, re.I):
                continue
            clean_lines.append(line)

    full_text = "\n".join(clean_lines)

    # Replace range headers like "Q.1 – Q.5 Carry ONE mark Each"
    full_text = re.sub(r'Q\s*\.\s*\d+\s*[-–]\s*Q\s*\.\s*\d+\s+Carry\s+[A-Z]+\s+mark[s]?\s+Each', '', full_text, flags=re.I)

    # Find all Q.<num>
    pattern = r'(?:^|\n)\s*Q\s*\.\s*(\d+)\b'
    matches = list(re.finditer(pattern, full_text))

    # Keep only matches where the number matches 1, 2, ..., 65 in order
    qs = {}
    for i in range(len(matches)):
        m = matches[i]
        num = int(m.group(1))
        start_idx = m.end()
        end_idx = matches[i+1].start() if i + 1 < len(matches) else len(full_text)
        chunk = full_text[start_idx:end_idx].strip()
        qs[num] = chunk

    print(f"File: {pdf_path}")
    print(f"Total extracted: {len(qs)}")
    missing = [i for i in range(1, 66) if i not in qs]
    print(f"Missing (1-65): {missing}")
    return qs

qs24 = extract_all_questions('raw_pdfs/gate_cs/gate_cs_2024_q.pdf')
qs25 = extract_all_questions('raw_pdfs/gate_cs/gate_cs_2025_q.pdf')
