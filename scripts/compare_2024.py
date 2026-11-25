import json, pymupdf, re
from test_regex_splits import extract_all_questions

existing = json.load(open('tests/gate/gate_cs/pyq/gate_cs_pyq_2024.json', encoding='utf-8'))
pdf_qs = extract_all_questions('raw_pdfs/gate_cs/gate_cs_2024_q.pdf')

key_data = {}
doc_k = pymupdf.open('raw_pdfs/gate_cs/gate_cs_2024_k.pdf')
k_text = "\n".join([p.get_text() for p in doc_k])
lines = [l.strip() for l in k_text.splitlines() if l.strip()]
i = 0
while i < len(lines):
    line = lines[i]
    if line.isdigit() and 1 <= int(line) <= 65:
        qnum = int(line)
        if i + 5 < len(lines) and lines[i+2] in ['MCQ', 'MSQ', 'NAT']:
            key_data[qnum] = {
                'type': lines[i+2],
                'key': lines[i+4],
                'mark': float(lines[i+5])
            }
            i += 6
            continue
    i += 1

print(f"{'Q#':<4} | {'Ex Type':<7} | {'PDF Key Type':<12} | {'Ex Key':<10} | {'PDF Key':<10} | {'Match?'}")
print("-" * 65)

mismatches = 0
for q in existing['questions']:
    qnum = q['questionNumber']
    ex_type = q.get('questionType')
    ex_key = q.get('correctOption') if ex_type == 'MCQ' else (";".join(q.get('correctOptionsList', [])) if ex_type == 'MSQ' else f"{q.get('natMin')} to {q.get('natMax')}")
    pdf_info = key_data.get(qnum, {})
    pdf_type = pdf_info.get('type')
    pdf_key = pdf_info.get('key')

    match = (ex_type == pdf_type)
    if not match:
        mismatches += 1
    print(f"Q{qnum:<3} | {ex_type:<7} | {pdf_type:<12} | {str(ex_key):<10} | {str(pdf_key):<10} | {'OK' if match else 'MISMATCH'}")

print(f"Total type mismatches: {mismatches}")
