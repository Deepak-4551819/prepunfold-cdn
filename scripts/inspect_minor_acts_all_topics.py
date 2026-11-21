import pymupdf
import re

pdf_path = r"C:\Users\yedde\Downloads\Judicial\UP (GS) 9 miner Act Youth PYQ(3).pdf"
doc = pymupdf.open(pdf_path)

# 9 Acts according to TOC:
# 1. The Rights of Persons with Disabilities Act, 2016: 3-11
# 2. The Maintenance and Welfare of Parents and Senior Citizens Act, 2007: 12-19
# 3. The Dowry Prohibition Act, 1961: 20-27
# 4. The Protection of Women from Domestic Violence Act, 2005: 28-42
# 5. The Sexual Harassment of Women at Workplace Act, 2013: 43-52
# 6. The Pre-Conception and Pre-Natal Diagnostic Techniques Act, 1994: 53-62
# 7. The Medical Termination of Pregnancy Act, 1971: 63-64
# 8. The Indecent Representation of Women (Prohibition) Act, 1986: 65-67
# 9. The Protection of Children from Sexual Offence Act, 2012: 68-80

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

for tag, title, start_p, end_p in acts:
    # Let's inspect the last page text for answers
    last_page_text = doc[end_p - 1].get_text()
    ans_matches = re.findall(r'(\d+)\.\s*\(([a-d])\)', last_page_text)
    print(f"[{tag}] {title}")
    print(f"   Pages: {start_p}-{end_p} (total {end_p-start_p+1} pages)")
    print(f"   Answers on page {end_p}: found {len(ans_matches)} answers (from {ans_matches[0] if ans_matches else 'none'} to {ans_matches[-1] if ans_matches else 'none'})")
