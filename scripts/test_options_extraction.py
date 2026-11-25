import pymupdf, re

def parse_answer_key(key_pdf):
    doc = pymupdf.open(key_pdf)
    text = "\n".join([page.get_text() for page in doc])
    lines = [l.strip() for l in text.splitlines() if l.strip()]

    # Let's inspect answer key format
    # Columns: Q. No., Session, Question Type (or Q. Type), Section, Key/Range, Mark(s)
    # Looking at earlier output:
    # 1
    # 5
    # MCQ
    # GA
    # A
    # 1
    key_data = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.isdigit() and 1 <= int(line) <= 65:
            qnum = int(line)
            # Check if next lines match session, type, section, key, mark
            if i + 5 < len(lines):
                sess = lines[i+1]
                qtype = lines[i+2]
                sec = lines[i+3]
                ans_key = lines[i+4]
                mark = lines[i+5]
                if qtype in ['MCQ', 'MSQ', 'NAT'] and mark in ['1', '2']:
                    key_data[qnum] = {
                        'qtype': qtype,
                        'sec': sec,
                        'key': ans_key,
                        'mark': float(mark)
                    }
                    i += 6
                    continue
        i += 1
    return key_data

k24 = parse_answer_key('raw_pdfs/gate_cs/gate_cs_2024_k.pdf')
k25 = parse_answer_key('raw_pdfs/gate_cs/gate_cs_2025_k.pdf')
print(f"Key 2024 parsed: {len(k24)}/65")
print(f"Key 2025 parsed: {len(k25)}/65")

# Test extracting options from question text
from test_regex_splits import extract_all_questions

qs24 = extract_all_questions('raw_pdfs/gate_cs/gate_cs_2024_q.pdf')
qs25 = extract_all_questions('raw_pdfs/gate_cs/gate_cs_2025_q.pdf')

def test_split_options(qs, key_data, year):
    opt_pattern = r'(?:^|\n)\s*\(([A-D])\)\s*'
    issues = []
    for qnum in range(1, 66):
        chunk = qs[qnum]
        meta = key_data[qnum]
        qtype = meta['qtype']
        if qtype in ['MCQ', 'MSQ']:
            matches = list(re.finditer(opt_pattern, chunk))
            labels = [m.group(1) for m in matches]
            if labels != ['A', 'B', 'C', 'D']:
                issues.append((qnum, qtype, labels, chunk[:150]))
    print(f"Year {year} option split issues: {len(issues)}")
    for issue in issues[:10]:
        print(f"  Q{issue[0]} ({issue[1]}): labels={issue[2]}")
        print(f"    snippet: {issue[3]!r}")

test_split_options(qs24, k24, 2024)
test_split_options(qs25, k25, 2025)
