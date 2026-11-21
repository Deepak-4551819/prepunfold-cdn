import pymupdf
import re

doc = pymupdf.open(r'C:\Users\yedde\Downloads\Judicial\Evidence Youth PYQ(2)(1).pdf')

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

def find_4_options_sequential(s):
    m_a = re.search(r'(?:^|\n|\s)\(a\)\s*', s, re.I)
    if not m_a: return None
    m_b = re.search(r'(?:^|\n|\s)\(b\)\s*', s[m_a.end():], re.I)
    if not m_b: return None
    b_start = m_a.end() + m_b.start()
    b_end = m_a.end() + m_b.end()
    m_c = re.search(r'(?:^|\n|\s)\(c\)\s*', s[b_end:], re.I)
    if not m_c: return None
    c_start = b_end + m_c.start()
    c_end = b_end + m_c.end()
    m_d = re.search(r'(?:^|\n|\s)\(d\)\s*', s[c_end:], re.I)
    if not m_d: return None
    d_start = c_end + m_d.start()
    d_end = c_end + m_d.end()
    return [(m_a.start(), m_a.end()), (b_start, b_end), (c_start, c_end), (d_start, d_end)]

evidence_topics = [
    (1, 'evidence_pyq_t01_preliminary', 'Preliminary (Sec 1-4)', 4, 20),
    (2, 'evidence_pyq_t02_relevancy_and_res_gestae', 'Relevancy of Facts & Res Gestae (Sec 5-16)', 21, 43),
    (3, 'evidence_pyq_t03_admissions_and_confessions', 'Admissions and Confessions (Sec 17-31)', 44, 71),
    (4, 'evidence_pyq_t04_dying_declaration_and_statements', 'Dying Declaration & Statements (Sec 32-33)', 72, 88),
    (5, 'evidence_pyq_t05_statements_under_special_circumstances', 'Statements under Special Circumstances & Judgments (Sec 34-44)', 89, 97),
    (6, 'evidence_pyq_t06_expert_opinion_and_character', 'Opinions of Third Persons & Character (Sec 45-55)', 98, 111),
    (7, 'evidence_pyq_t07_facts_need_not_be_proved', 'Facts Which Need Not Be Proved (Sec 56-58)', 112, 116),
    (8, 'evidence_pyq_t08_oral_and_documentary_evidence', 'Oral and Documentary Evidence (Sec 59-73A)', 117, 136),
    (9, 'evidence_pyq_t09_public_documents', 'Public Documents (Sec 74-78)', 137, 141),
    (10, 'evidence_pyq_t10_presumptions_as_to_documents', 'Presumptions as to Documents (Sec 79-90A)', 142, 148),
    (11, 'evidence_pyq_t11_exclusion_of_oral_by_documentary_evidence', 'Exclusion of Oral by Documentary Evidence (Sec 91-100)', 149, 154),
    (12, 'evidence_pyq_t12_burden_of_proof', 'Burden of Proof and Presumptions (Sec 101-114A)', 155, 177),
    (13, 'evidence_pyq_t13_estoppel', 'Estoppel (Sec 115-117)', 178, 183),
    (14, 'evidence_pyq_t14_witnesses_competency_privilege', 'Witnesses, Competency and Privileges (Sec 118-134)', 184, 203),
    (15, 'evidence_pyq_t15_examination_of_witnesses', 'Examination of Witnesses (Sec 135-166)', 204, 226),
    (16, 'evidence_pyq_t16_improper_admission_and_rejection', 'Improper Admission and Rejection of Evidence (Sec 167)', 227, 227),
    (17, 'evidence_pyq_t17_practice_and_revision_questions', 'Practice and Revision Questions (Miscellaneous)', 228, 240)
]

total_q = 0
total_full = 0
for ch_num, test_id, title, p_s, p_e in evidence_topics:
    lines = []
    for p in range(p_s - 1, p_e):
        for l in doc[p].get_text().split('\n'):
            s = l.strip()
            if not s or s.startswith('YCT') or s.startswith('YeejleerÙe mee#Ùe DeefOeefveÙece') or re.match(r'^\d+$', s):
                continue
            lines.append(l)
    text = '\n'.join(lines)

    ans_matches = list(re.finditer(r'\nAns\s*[\.:]\s*\(([a-eA-E\*&, ]+)\)', text))
    ch_q = len(ans_matches)
    ch_full = 0
    for i, ans_m in enumerate(ans_matches):
        ans_start = ans_m.start()
        prev_ans_end = ans_matches[i-1].end() if i > 0 else 0
        window = text[prev_ans_end:ans_start]
        q_num_matches = list(re.finditer(r'(?:^|\n)\s*(\d+)\s*\.\s+', window))
        if q_num_matches:
            q_start_idx = prev_ans_end + q_num_matches[0].start()
        else:
            q_start_idx = prev_ans_end
        pre_ans = text[q_start_idx:ans_start].strip()
        pre_ans = re.sub(r'^\n?\s*\d+\s*\.\s*', '', pre_ans).strip()

        opt_ranges = find_4_options_sequential(pre_ans)
        if opt_ranges:
            ch_full += 1

    total_q += ch_q
    total_full += ch_full
    print(f"Test {ch_num:02d}: {title[:35]:<35} | {ch_full}/{ch_q} full options")

print("="*65)
print(f"Evidence Act Parsing Accuracy: {total_full}/{total_q} ({total_full/total_q*100:.1f}%)")
