import pymupdf, re, json, os, sys, time
sys.path.insert(0, os.path.dirname(__file__))
from aps_decoder import decode_aps

PDF_PATH = r"C:\Users\yedde\Downloads\HISTORY CHAPTER-WISE SOLVED PAPERS.pdf"
OUT_MASTER = os.path.join(os.path.dirname(__file__), "extracted_tgt_pgt_history_master.json")

HISTORY_CHAPTERS = [
    (9, 32, "Prehistoric Cultures of India", "भारतीय प्रागैतिहासिक संस्कृतियाँ"),
    (33, 59, "Indus Valley Civilization", "सिन्धु घाटी सभ्यता एवं नगर नियोजन"),
    (60, 90, "Vedic Period", "वैदिक काल एवं उत्तर वैदिक काल"),
    (91, 134, "Jainism, Buddhism & Mahajanapadas", "जैन धर्म, बौद्ध धर्म एवं महाजनपद"),
    (135, 182, "Mauryan & Post-Mauryan Empire", "मौर्यकाल एवं मौर्योत्तर काल"),
    (183, 212, "Gupta & Post-Gupta Era", "गुप्त एवं गुप्तोत्तर काल"),
    (213, 224, "Chola Dynasty & South India", "चोल काल एवं दक्षिण भारत"),
    (225, 232, "Foreign Invasions", "विदेशी आक्रमण (अरब, गजनवी, गोरी)"),
    (233, 284, "Ancient Indian Culture & Historiography", "विविध: प्राचीन भारतीय इतिहास एवं संस्कृति"),
    (285, 348, "Delhi Sultanate", "दिल्ली सल्तनत (राजनीतिक, प्रशासनिक व सांस्कृतिक)"),
    (349, 419, "Mughal Empire", "मुगल साम्राज्य एवं प्रशासन"),
    (420, 449, "Vijayanagara, Bahmani & Marathas", "विजयनगर, बहमनी एवं मराठा साम्राज्य"),
    (450, 521, "Medieval Culture, Bhakti & Sufism", "मध्यकालीन संस्कृति, भक्ति एवं सूफी आन्दोलन"),
    (522, 544, "Medieval Economy & Society", "मध्यकालीन समाज एवं अर्थव्यवस्था"),
    (545, 562, "Miscellaneous Medieval History", "विविध: मध्यकालीन इतिहास"),
    (563, 593, "British Expansion & East India Company", "ईस्ट इण्डिया कम्पनी एवं ब्रिटिश विस्तार"),
    (594, 611, "Modern Indian Economy & Agriculture", "आधुनिक भारत में अर्थव्यवस्था व व्यापार"),
    (612, 636, "Education & Constitutional Development", "आधुनिक शिक्षा एवं संवैधानिक विकास"),
    (637, 650, "Revolt of 1857", "1857 ई. का विद्रोह"),
    (651, 687, "Socio-Religious Reform Movements", "सामाजिक-धार्मिक सुधार आन्दोलन"),
    (688, 762, "Indian National Movement & Freedom Struggle", "भारतीय राष्ट्रीय आन्दोलन"),
    (763, 780, "Prominent Leaders in National Movement", "गाँधी, तिलक, गोखले, सुभाष बोस"),
    (781, 803, "Independence & Partition of India", "स्वतंत्रता प्राप्ति एवं विभाजन"),
    (804, 811, "Governors & Viceroys", "गवर्नर-जनरल एवं वायसराय"),
    (812, 822, "Peasant, Tribal & Revolutionary Movements", "कृषक, जनजातीय एवं क्रान्तिकारी आन्दोलन"),
    (823, 861, "Miscellaneous Modern India", "विविध: आधुनिक भारत"),
    (862, 884, "Historical Methodology & Historiography", "इतिहास दर्शन एवं शोध प्रविधि"),
    (885, 928, "World History", "विश्व इतिहास (पुनर्जागरण, क्रांतियाँ, विश्व युद्ध)")
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
        if 'TGT PGT History Planner' in s or s == 'YCT':
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
        'BPSC', 'Exam', 'Shift', 'Paper', 'HPSC', 'MPPSC', 'CGPSC'
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

def parse_history_chapter(doc, start_p, end_p, ch_en, ch_hi):
    pages_text = []
    for p in range(start_p - 1, min(end_p, len(doc))):
        pages_text.append(clean_page(doc, p))
    full_text = '\n'.join(pages_text)

    ans_pattern = re.compile(r'(?:^|\n)\s*(Ans|Gòej)\s*[\.:-]*\s*(?:\n\s*)?\(?([a-eA-E\*])\)?\s*[:\.-]?', re.MULTILINE)
    matches = list(ans_pattern.finditer(full_text))

    questions = []
    for i, ans_m in enumerate(matches):
        marker_type = ans_m.group(1)
        correct_opt = ans_m.group(2).upper()
        if correct_opt == '*':
            correct_opt = 'A'

        next_boundary = matches[i+1].start() if i + 1 < len(matches) else len(full_text)
        post_ans = full_text[ans_m.end():next_boundary]

        extra_tag = ""
        if marker_type.lower() == 'gòej':
            vyakhya_m = re.search(r'JÙeeKÙee\s*[:–-]*\s*', post_ans)
            if vyakhya_m:
                extra_tag = post_ans[:vyakhya_m.start()].strip()
                explanation_raw = post_ans[vyakhya_m.end():]
            else:
                explanation_raw = post_ans
        else:
            explanation_raw = post_ans

        prev_boundary = matches[i-1].end() if i > 0 else 0
        pre_text = full_text[prev_boundary:ans_m.start()]

        q_num_match = list(re.finditer(r'(?:^|\n)\s*(\d{1,4})\.\s*', pre_text))
        if not q_num_match:
            continue

        last_q = q_num_match[-1]
        book_q_num = int(last_q.group(1))
        q_body = pre_text[last_q.end():]

        first_opt = re.search(r'(?:^|\s)(?:\([aA]\)|[aA]\))\s*', q_body)
        if not first_opt:
            continue

        q_text_raw = q_body[:first_opt.start()]
        opt_part_raw = q_body[first_opt.start():]

        options, exam_tag = parse_options_and_tags(opt_part_raw)
        if extra_tag:
            clean_extra = decode_aps(extra_tag).strip()
            exam_tag = f"{exam_tag} | {clean_extra}".strip(" |")

        if len(options) < 2:
            continue

        while len(options) < 4:
            options.append(f"इनमें से कोई नहीं ({len(options)+1})")

        next_q_num_m = re.search(r'(?:^|\n)\s*\d{1,4}\.\s*', explanation_raw)
        if next_q_num_m:
            explanation_raw = explanation_raw[:next_q_num_m.start()]

        q_text_hi = decode_aps(q_text_raw).strip()
        q_text_hi = re.sub(r'\s+', ' ', q_text_hi)

        exp_hi = decode_aps(explanation_raw).strip()
        exp_hi = re.sub(r'\s+', ' ', exp_hi)

        if not q_text_hi:
            continue

        questions.append({
            "bookQuestionNumber": book_q_num,
            "questionTextHi": q_text_hi,
            "optionsHi": options,
            "correctOption": correct_opt,
            "explanationHi": exp_hi,
            "examTag": exam_tag,
            "chapterEn": ch_en,
            "chapterHi": ch_hi
        })

    return questions

def main():
    t0 = time.time()
    print(f"Opening {PDF_PATH}...")
    doc = pymupdf.open(PDF_PATH)
    all_questions = []

    for idx, (sp, ep, ch_en, ch_hi) in enumerate(HISTORY_CHAPTERS, 1):
        print(f"Parsing Ch {idx}: {ch_en} (pp. {sp}-{ep})...")
        qs = parse_history_chapter(doc, sp, ep, ch_en, ch_hi)
        print(f" -> Found {len(qs)} valid questions")
        all_questions.extend(qs)

    print(f"\nTotal questions parsed: {len(all_questions)} in {time.time()-t0:.2f}s")

    with open(OUT_MASTER, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, ensure_ascii=False, indent=2)

    print(f"Saved master questions to {OUT_MASTER} ({os.path.getsize(OUT_MASTER)/(1024*1024):.2f} MB)")

if __name__ == "__main__":
    main()
