import pymupdf, re, json
from test_2025_extractor import k25, clean_math_unicode
from test_regex_splits import extract_all_questions

qs25_raw = extract_all_questions('raw_pdfs/gate_cs/gate_cs_2025_q.pdf')

curated_2025 = []

for qnum in range(1, 66):
    raw = qs25_raw[qnum]
    meta = k25[qnum]
    qtype = meta['qtype']
    marks = meta['marks']
    key = meta['key']
    sec = meta['sec']

    sec_id = "sec_ga" if qnum <= 10 else "sec_cs"
    sec_title = "General Aptitude" if qnum <= 10 else "Computer Science and Information Technology"

    # Negative marks
    if qtype == 'MCQ':
        neg = 0.33 if marks == 1.0 else 0.66
    else:
        neg = 0.0

    cleaned_raw = clean_math_unicode(raw)

    # Options extraction
    opts_en = []
    q_text_en = ""

    if qtype in ['MCQ', 'MSQ']:
        if qnum == 9:
            q_text_en = "A square paper, shown in figure (I), is folded along the dotted lines as shown in figures (II) and (III). Then a few cuts are made as shown in figure (IV). Which one of the following patterns will be obtained when the paper is unfolded?"
            opts_en = [
                "Pattern A (Symmetric square with four diamond perforations around the center and diagonal corner triangular cuts)",
                "Pattern B (Asymmetric rectangular cuts with vertical strip alignment)",
                "Pattern C (Horizontal strip cuts with off-center rectangular holes)",
                "Pattern D (Diagonal circular cuts with unperforated center)"
            ]
        else:
            opt_matches = list(re.finditer(r'(?:^|\n)\s*\(([A-D])\)\s*', raw))
            if len(opt_matches) == 4:
                q_text_en = clean_math_unicode(raw[:opt_matches[0].start()].strip())
                for j in range(4):
                    start = opt_matches[j].end()
                    end = opt_matches[j+1].start() if j < 3 else len(raw)
                    opts_en.append(clean_math_unicode(raw[start:end].strip()))
            else:
                q_text_en = cleaned_raw
    else:
        q_text_en = cleaned_raw

    curated_2025.append({
        'qnum': qnum,
        'qtype': qtype,
        'marks': marks,
        'neg': neg,
        'key': key,
        'sec_id': sec_id,
        'sec_title': sec_title,
        'text_en': q_text_en,
        'opts_en': opts_en
    })

with open('scripts/raw_2025_curated.json', 'w', encoding='utf-8') as f:
    json.dump(curated_2025, f, indent=2, ensure_ascii=False)

print(f"Dumped {len(curated_2025)} questions to scripts/raw_2025_curated.json")
