import pymupdf, re, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from aps_decoder import decode_aps

PDF_PATH = r"C:\Users\yedde\Downloads\GEOGRAPHY CHAPTER-WISE SOLVED PAPERS.pdf"

GEO_CHAPTERS = [
    (9, 14, "Geographical Thought & Nature of Geography", "भूगोल-अर्थ एवं विषय क्षेत्र"),
    (15, 70, "Physical Geography & Solar System", "भौतिक भूगोल एवं सौर मण्डल"),
    (71, 176, "Geomorphology & Lithosphere", "स्थलमण्डल एवं भू-आकृति विज्ञान"),
    (177, 269, "Climatology & Atmosphere", "वायुमण्डल एवं जलवायु विज्ञान"),
    (270, 325, "Oceanography & Hydrosphere", "जलमण्डल एवं समुद्र विज्ञान"),
    (326, 367, "Biogeography & Ecosystem", "जैवमण्डल एवं पारिस्थितिकी"),
    (368, 497, "Human Geography, Population & Settlement", "मानव भूगोल, जनसंख्या एवं अधिवास"),
    (498, 606, "Economic Geography & Resources", "आर्थिक भूगोल एवं संसाधन"),
    (607, 835, "Geography of India", "भारत का भूगोल"),
    (836, 864, "Miscellaneous Geography & Cartography", "विविध भूगोल एवं मानचित्रकला")
]

def clean_page(doc, p_idx):
    lines = doc[p_idx].get_text().splitlines()
    cleaned = []
    for l in lines:
        s = l.strip()
        if not s:
            continue
        if s.isdigit() and len(s) <= 4:
            continue
        if 'TGT/PGT Geography Planner' in s or s == 'YCT':
            continue
        if '@Apnapdfs' in s or 'CLICK HERE' in s:
            continue
        cleaned.append(s)
    return '\n'.join(cleaned)

def parse_options_and_tags(opt_part_raw):
    opt_matches = list(re.finditer(r'(?:^|\s)(?:\(([a-eA-E])\)|([a-eA-E])\))\s*', opt_part_raw))
    if not opt_matches:
        return [], ""

    options_raw = {}
    for idx, om in enumerate(opt_matches):
        letter = (om.group(1) or om.group(2)).upper()
        start = om.end()
        end = opt_matches[idx+1].start() if idx + 1 < len(opt_matches) else len(opt_part_raw)
        options_raw[letter] = opt_part_raw[start:end].strip()

    last_letter = list(options_raw.keys())[-1]
    last_val = options_raw[last_letter]
    last_lines = [l.strip() for l in last_val.splitlines() if l.strip()]

    opt_d_lines = []
    tag_lines = []
    exam_kw = [
        'PGT', 'TGT', 'GIC', 'GDC', 'LT', 'NET', 'JRF', 'SET', 'Asst', 'Prof',
        'Lect', 'UPPCS', 'PSC', 'KVS', 'NVS', 'DSSSB', 'RPSC', 'JSSC', 'UKPSC',
        'BPSC', 'Exam', 'Shift', 'Paper'
    ]

    is_tag = True
    for l in reversed(last_lines):
        if is_tag and (any(kw in l for kw in exam_kw) or re.search(r'\b(19\d\d|20\d\d)\b', l)):
            tag_lines.insert(0, l)
        else:
            is_tag = False
            opt_d_lines.insert(0, l)

    options_raw[last_letter] = ' '.join(opt_d_lines).strip()
    exam_tag = ' | '.join(tag_lines).strip()

    opt_list = []
    for l in ['A', 'B', 'C', 'D']:
        if l in options_raw and len(options_raw[l].strip()) > 0:
            decoded_opt = decode_aps(options_raw[l])
            decoded_opt = re.sub(r'\s+', ' ', decoded_opt).strip()
            if decoded_opt:
                opt_list.append(decoded_opt)

    return opt_list, exam_tag

def parse_geo_chapter(doc, start_p, end_p, ch_en, ch_hi):
    pages_text = []
    for p in range(start_p - 1, min(end_p, len(doc))):
        pages_text.append(clean_page(doc, p))
    full_text = '\n'.join(pages_text)

    ans_pattern = re.compile(r'(?:^|\n)\s*Ans\s*[\.:-]*\s*(?:\n\s*)?\(?([a-eA-E\*])\)?\s*[:\.-]?', re.MULTILINE)
    matches = list(ans_pattern.finditer(full_text))

    questions = []
    for i, m in enumerate(matches):
        prev_boundary = matches[i-1].end() if i > 0 else 0
        between_prev_and_ans = full_text[prev_boundary:m.start()].strip()

        q_matches = list(re.finditer(r'(?:^|\n)\s*(\d{1,4})\.\s+', between_prev_and_ans))
        if not q_matches:
            continue
        last_q = q_matches[-1]

        if questions:
            raw_exp = between_prev_and_ans[:last_q.start()].strip()
            dec_exp = decode_aps(raw_exp)
            questions[-1]['explanation'] = re.sub(r'\s+', ' ', dec_exp).strip()
            questions[-1]['explanationHi'] = questions[-1]['explanation']

        q_and_opt = between_prev_and_ans[last_q.start():].strip()
        ans_letter = m.group(1).upper()

        opt_m = re.search(r'(?:^|\n)\s*(?:\([a-eA-E]\)|[a-eA-E]\))\s*', q_and_opt)
        if not opt_m:
            continue

        q_text_raw = re.sub(r'^\d+\.\s*', '', q_and_opt[:opt_m.start()]).strip()
        opt_part_raw = q_and_opt[opt_m.start():].strip()

        opts, exam_tag = parse_options_and_tags(opt_part_raw)
        if len(opts) != 4 or any(len(o) == 0 for o in opts):
            continue
        if ans_letter not in ['A', 'B', 'C', 'D']:
            continue

        dec_q = decode_aps(q_text_raw)
        dec_q = re.sub(r'\s+', ' ', dec_q).strip()
        if len(dec_q) < 5:
            continue

        questions.append({
            'q_num_book': int(last_q.group(1)),
            'chapterEn': ch_en,
            'chapterHi': ch_hi,
            'questionText': dec_q,
            'questionTextHi': dec_q,
            'questionTextEn': "",
            'options': opts,
            'optionsHi': opts,
            'optionsEn': [],
            'correctOption': ans_letter,
            'examTag': exam_tag if exam_tag else "TGT/PGT Geography Solved Papers",
            'explanation': "",
            'explanationHi': "",
            'explanationEn': ""
        })

    if questions and matches:
        last_exp = full_text[matches[-1].end():matches[-1].end()+1000].strip()
        next_q = re.search(r'(?:^|\n)\s*\d{1,4}\.\s+', last_exp)
        if next_q:
            last_exp = last_exp[:next_q.start()]
        dec_last = decode_aps(last_exp.strip())
        questions[-1]['explanation'] = re.sub(r'\s+', ' ', dec_last).strip()
        questions[-1]['explanationHi'] = questions[-1]['explanation']

    final_qs = []
    for q in questions:
        if len(q['explanation'].strip()) >= 5:
            final_qs.append(q)

    return final_qs

def main():
    print(f"Opening {PDF_PATH}...")
    doc = pymupdf.open(PDF_PATH)
    print(f"Loaded Geography PDF with {len(doc)} pages.")

    all_questions = []
    for start_p, end_p, ch_en, ch_hi in GEO_CHAPTERS:
        ch_qs = parse_geo_chapter(doc, start_p, end_p, ch_en, ch_hi)
        print(f"Chapter '{ch_en}' (pp. {start_p}-{end_p}): {len(ch_qs)} valid questions extracted.")
        all_questions.extend(ch_qs)

    print(f"\nTOTAL VALID GEOGRAPHY QUESTIONS EXTRACTED: {len(all_questions)}")
    out_file = "scripts/extracted_tgt_pgt_geography_master.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, ensure_ascii=False, indent=2)
    print(f"Saved master questions cache to {out_file} ({os.path.getsize(out_file) / 1024 / 1024:.2f} MB)")

if __name__ == "__main__":
    main()
