import pymupdf
import re

pdf_path = r"C:\Users\yedde\Downloads\Judicial\UP (GS) 9 miner Act Youth PYQ(3).pdf"
doc = pymupdf.open(pdf_path)

acts = [
    ("act_01_persons_with_disabilities", "The Rights of Persons with Disabilities Act, 2016", 3, 11),
    ("act_02_maintenance_parents_senior_citizens", "The Maintenance and Welfare of Parents and Senior Citizens Act, 2007", 12, 19),
    ("act_03_dowry_prohibition", "The Dowry Prohibition Act, 1961", 20, 27),
    ("act_04_domestic_violence", "The Protection of Women from Domestic Violence Act, 2005", 28, 42),
    ("act_05_sexual_harassment_workplace", "The Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013", 43, 52),
    ("act_06_pcpndt_act", "The Pre-Conception and Pre-Natal Diagnostic Techniques (Prohibition of Sex Selection) Act, 1994", 53, 62),
    ("act_07_medical_termination_of_pregnancy", "The Medical Termination of Pregnancy Act, 1971", 63, 64),
    ("act_08_indecent_representation_of_women", "The Indecent Representation of Women (Prohibition) Act, 1986", 65, 67),
    ("act_09_pocso_act", "The Protection of Children from Sexual Offences Act, 2012", 68, 80),
]

def extract_page_text_columns(page):
    blocks = page.get_text("blocks")
    # Header: top < 55, Footer: bottom > 725
    col1 = []
    col2 = []
    for b in blocks:
        x0, y0, x1, y1, text, bno, btype = b
        if btype != 0:
            continue
        # ignore header/footer
        if y0 < 50 or y1 > 730:
            continue
        if x0 < 308:
            col1.append((y0, text))
        else:
            col2.append((y0, text))

    col1.sort(key=lambda x: x[0])
    col2.sort(key=lambda x: x[0])

    full_text = "\n".join([t[1] for t in col1]) + "\n" + "\n".join([t[1] for t in col2])
    return full_text

for tag, title, start_p, end_p in acts:
    # 1. Parse answers from the last page
    last_page = doc[end_p - 1]
    last_text = last_page.get_text()
    ans_dict = {}
    for m in re.finditer(r'(\d+)\.\s*\(([a-e])\)', last_text):
        ans_dict[int(m.group(1))] = m.group(2).lower()

    print(f"\n[{tag}] Expected Qs: {len(ans_dict)}")

    # 2. Extract full text from start_p to end_p
    # Note: On the last page, we stop where the answer table starts!
    act_text = ""
    for p in range(start_p - 1, end_p):
        page = doc[p]
        p_text = extract_page_text_columns(page)
        if p == end_p - 1:
            # find where answer table starts, e.g. "1. (c)" or "1. (d)" or "1. (a)"
            # Usually after the last question options
            # Let's see:
            m_ans = re.search(r'\n\s*1\.\s*\([a-e]\)', p_text)
            if m_ans:
                p_text = p_text[:m_ans.start()]
        act_text += "\n" + p_text

    # Check question number matches
    # Q regex: \n\s*(\d+)\.\s+
    q_matches = list(re.finditer(r'\n\s*(\d+)\.\s+', act_text))
    found_q_nums = [int(m.group(1)) for m in q_matches]

    # Check sequence
    expected_nums = list(range(1, len(ans_dict) + 1))
    missing = set(expected_nums) - set(found_q_nums)
    print(f"   Found Q numbers: {len(found_q_nums)}, min={min(found_q_nums) if found_q_nums else 0}, max={max(found_q_nums) if found_q_nums else 0}")
    if missing:
        print(f"   Missing Q numbers: {sorted(list(missing))[:10]}")
