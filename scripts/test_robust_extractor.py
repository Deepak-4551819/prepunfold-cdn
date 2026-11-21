import pymupdf
import re

doc = pymupdf.open(r'C:\Users\yedde\Downloads\Judicial\CPC Youth PYQ.pdf')

chapters_info = [
    (1, "Preliminary (Sec 1-8)", "Preliminary (Sec 1-8)", 4, 15),
    (2, "Jurisdiction and Res Judicata (Sec 9-14)", "Jurisdiction & Res Judicata", 16, 29),
    (3, "Place of Suing and Institution of Suits (Sec 15-26)", "Place of Suing & Institution of Suits", 30, 38),
    (4, "Summons and Discovery (Sec 27-32)", "Summons & Discovery", 39, 40),
    (5, "Judgment, Decree and Costs (Sec 33-35B)", "Judgment, Decree & Costs", 41, 42),
    (6, "Execution (Sec 36-74)", "Execution of Decrees", 43, 53),
    (7, "Incidental Proceedings (Sec 75-78)", "Incidental Proceedings", 54, 54),
    (8, "Suits in Particular Cases (Sec 79-88)", "Suits in Particular Cases", 55, 59),
    (9, "Special Proceedings (Sec 89-93)", "Special Proceedings (ADR)", 60, 64),
    (10, "Supplemental Proceedings (Sec 94-95)", "Supplemental Proceedings", 65, 65),
    (11, "Appeals (Sec 96-112)", "Appeals", 66, 71),
    (12, "Reference, Review and Revision (Sec 113-115)", "Reference, Review & Revision", 72, 75),
    (13, "High Court Rules and Special Provisions (Sec 116-131)", "High Court Special Provisions", 76, 76),
    (14, "Miscellaneous (Sec 132-158)", "Miscellaneous Provisions", 76, 82),
    (15, "First Schedule: Orders 1-10 (Parties, Pleadings & Issues)", "Orders 1 to 10", 83, 114),
    (16, "First Schedule: Orders 11-20 (Discovery, Admissions & Trial)", "Orders 11 to 20", 115, 124),
    (17, "First Schedule: Order 21 (Execution of Decrees and Orders)", "Order 21 (Execution)", 125, 132),
    (18, "First Schedule: Orders 22-32 (Incidental & Special Suits)", "Orders 22 to 32", 133, 142),
    (19, "First Schedule: Orders 33-51 (Indigent, Injunctions & Appeals)", "Orders 33 to 51", 143, 159),
    (20, "Miscellaneous & Practice Questions", "Practice & Revision", 160, 168)
]

def split_en_hi(text_block):
    if '/' in text_block:
        return text_block.split('/')[0].strip()
    lines = [l.strip() for l in text_block.split('\n') if l.strip()]
    if not lines:
        return text_block.strip()
    en_lines = []
    for line in lines:
        has_akruti = any(ord(c) > 127 for c in line) or bool(re.search(r'(keâ|ef|me|ue|Je|Ce|Øe|›eâ|ne|le|Le|oe|Oe|ve|he|ye|Ye|ce|Ùe|Me|<e)', line))
        words = re.findall(r'[a-zA-Z]+', line)
        if len(words) > 0 and not has_akruti:
            en_lines.append(line)
        elif not en_lines:
            en_lines.append(line)
        else:
            break
    return ' '.join(en_lines).strip()

def parse_chapter_questions(p_start, p_end):
    lines = []
    for p in range(p_start - 1, p_end):
        for l in doc[p].get_text().split('\n'):
            s = l.strip()
            if not s or s.startswith('YCT') or s == 'efmeefJeue Øeef›eâÙee mebefnlee, 1908' or re.match(r'^\d+$', s):
                continue
            lines.append(l)
    text = '\n'.join(lines)

    # Find all Ans positions
    ans_matches = list(re.finditer(r'\nAns\.\s*\(([a-eA-E\*&, ]+)\)\s*:?', text))
    if not ans_matches:
        return []

    questions = []
    for i, ans_m in enumerate(ans_matches):
        ans_start = ans_m.start()
        ans_end = ans_m.end()
        ans_str = ans_m.group(1).upper()
        m_let = re.search(r'[A-E]', ans_str)
        corr_letter = m_let.group(0) if m_let else 'A'

        # Determine the start of this question:
        # Search backwards from ans_start for the question number pattern
        prev_ans_end = ans_matches[i-1].end() if i > 0 else 0
        window = text[prev_ans_end:ans_start]

        # Look for question number at start of line in window
        q_num_matches = list(re.finditer(r'(?:^|\n)\s*(\d+)\s*\.\s+', window))
        if q_num_matches:
            # The question number is the last one in this window before the options
            # Usually the first in window if clean, but let's take the first valid q_num
            q_num = int(q_num_matches[0].group(1))
            q_start_idx = prev_ans_end + q_num_matches[0].start()
        else:
            q_num = i + 1
            q_start_idx = prev_ans_end

        pre_ans = text[q_start_idx:ans_start].strip()
        # strip leading question number
        pre_ans = re.sub(r'^\n?\s*\d+\s*\.\s*', '', pre_ans).strip()

        # Determine end of explanation: up to next question start
        if i + 1 < len(ans_matches):
            next_window = text[ans_end:ans_matches[i+1].start()]
            next_q_matches = list(re.finditer(r'(?:^|\n)\s*(\d+)\s*\.\s+', next_window))
            if next_q_matches:
                exp_end = ans_end + next_q_matches[0].start()
            else:
                exp_end = ans_matches[i+1].start()
        else:
            exp_end = len(text)

        explanation = text[ans_end:exp_end].strip()

        # Parse options
        opt_matches = list(re.finditer(r'(?:^|\n)\s*\(([a-d])\)\s*', pre_ans))
        filtered_opts = []
        expected_letter = 'a'
        for m in opt_matches:
            if m.group(1).lower() == expected_letter:
                filtered_opts.append(m)
                expected_letter = chr(ord(expected_letter) + 1)
                if expected_letter > 'd':
                    break

        if len(filtered_opts) == 4:
            raw_stem = pre_ans[:filtered_opts[0].start()].strip()
            raw_options = []
            for j in range(4):
                opt_s = filtered_opts[j].end()
                opt_e = filtered_opts[j+1].start() if j + 1 < 4 else len(pre_ans)
                raw_options.append(pre_ans[opt_s:opt_e].strip())

            d_lines = raw_options[3].split('\n')
            exam_tag = ""
            actual_d_lines = []
            for l in d_lines:
                ls = l.strip()
                if re.search(r'(P\.C\.S|I\.A\.S|U\.P|M\.P|R\.O|A\.R\.O|B\.P|R\.A\.S|Uttarakhand|Jharkhand|Chhattisgarh|Bihar|Rajasthan|Haryana|MPHC|UPPCS|BPSC|RJS|JS|CJ|Pre|Mains|\b\d{4}\b)', ls, re.I) and len(actual_d_lines) > 0:
                    exam_tag = (exam_tag + " " + ls).strip()
                else:
                    actual_d_lines.append(l)
            raw_options[3] = '\n'.join(actual_d_lines).strip()
        else:
            raw_stem = pre_ans
            raw_options = ["", "", "", ""]
            exam_tag = ""

        q_en = split_en_hi(raw_stem)
        opts_en = [split_en_hi(o) for o in raw_options]

        q_en = re.sub(r'\s+', ' ', q_en).strip()
        opts_en = [re.sub(r'\s+', ' ', o).strip() for o in opts_en]

        # Fallback for options if empty
        for idx_o in range(4):
            if not opts_en[idx_o]:
                opts_en[idx_o] = f"Option {chr(ord('A') + idx_o)}"

        questions.append({
            "num": i + 1,
            "orig_num": q_num,
            "q_en": q_en if q_en else f"Question {i+1}",
            "opts_en": opts_en,
            "correct_opt": corr_letter,
            "exam_tag": exam_tag if exam_tag else "State Judiciary & PCS (J) PYQ",
            "explanation": explanation
        })

    return questions

total = 0
all_4_opts = 0
for ch_num, title, short_title, p_start, p_end in chapters_info:
    qs = parse_chapter_questions(p_start, p_end)
    with_opts = sum(1 for q in qs if all(not o.startswith('Option ') for o in q['opts_en']))
    total += len(qs)
    all_4_opts += with_opts
    print(f"Test {ch_num:02d}: {short_title:<40} | Qs: {len(qs):3d} | Full Opts: {with_opts:3d}")

print("="*75)
print(f"Total Parsed: {total} | Full Options: {all_4_opts}/{total} ({all_4_opts/total*100:.1f}%)")
