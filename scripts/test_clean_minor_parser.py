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

def is_ans_block(text):
    lines = [l.strip() for l in text.strip().split('\n') if l.strip()]
    if not lines:
        return False
    ans_lines = sum(1 for l in lines if re.match(r'^\d+\.\s*\([a-e]\)', l))
    return ans_lines >= 1 and (ans_lines / len(lines) > 0.5)

def parse_act(tag, title, start_p, end_p):
    # Collect answer key
    ans_dict = {}
    for p in range(start_p - 1, end_p):
        page = doc[p]
        for b in page.get_text("blocks"):
            if b[6] != 0:
                continue
            for m in re.finditer(r'(\d+)\.\s*\(([a-e])\)', b[4]):
                ans_dict[int(m.group(1))] = m.group(2).lower()

    # Collect text blocks (excluding headers, footers, and answer key blocks)
    act_text = ""
    for p in range(start_p - 1, end_p):
        page = doc[p]
        col1 = []
        col2 = []
        for b in page.get_text("blocks"):
            x0, y0, x1, y1, text, bno, btype = b
            if btype != 0:
                continue
            if y0 < 50 or y1 > 730:
                continue
            if is_ans_block(text):
                continue
            if x0 < 308:
                col1.append((y0, text))
            else:
                col2.append((y0, text))
        col1.sort(key=lambda x: x[0])
        col2.sort(key=lambda x: x[0])
        p_text = "\n".join([t[1] for t in col1]) + "\n" + "\n".join([t[1] for t in col2])
        act_text += "\n" + p_text

    return ans_dict, act_text

for tag, title, start_p, end_p in acts:
    ans_dict, act_text = parse_act(tag, title, start_p, end_p)
    q_matches = list(re.finditer(r'\n\s*(\d+)\.\s+', act_text))
    found_nums = set()
    for m in q_matches:
        num = int(m.group(1))
        if num in ans_dict:
            found_nums.add(num)

    expected_nums = set(ans_dict.keys())
    missing = expected_nums - found_nums
    print(f"[{tag}] Total Ans: {len(ans_dict)} | Matched Qs: {len(found_nums)} | Missing: {len(missing)}")
    if missing:
        print(f"   Missing nums: {sorted(list(missing))}")
