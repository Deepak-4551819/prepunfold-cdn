import pymupdf
import re

doc = pymupdf.open(r'C:\Users\yedde\Downloads\Judicial\Cr.PC Youth PYQ.pdf')

crpc_chapters = [
    (1, "Preliminary (Sec 1-5)", 4, 17),
    (2, "Constitution of Criminal Courts and Offices (Sec 6-25A)", 18, 25),
    (3, "Power of Courts (Sec 26-35)", 26, 31),
    (4, "Powers of Superior Police Officers & Aid to Magistrates (Sec 36-40)", 32, 33),
    (5, "Arrest of Persons (Sec 41-60A)", 34, 45),
    (6, "Process to Compel Appearance (Sec 61-90)", 46, 51),
    (7, "Process to Compel Production of Things (Sec 91-105)", 52, 55),
    (8, "Reciprocal Arrangements (Sec 105A-105L)", 56, 56),
    (9, "Security for Keeping the Peace and Good Behaviour (Sec 106-124)", 57, 61),
    (10, "Order for Maintenance of Wives, Children and Parents (Sec 125-128)", 62, 73),
    (11, "Maintenance of Public Order and Tranquillity (Sec 129-148)", 74, 81),
    (12, "Preventive Action of the Police (Sec 149-153)", 82, 82),
    (13, "Information to the Police and Powers to Investigate (Sec 154-176)", 83, 112),
    (14, "Jurisdiction of Criminal Courts in Inquiries and Trials (Sec 177-189)", 113, 118),
    (15, "Conditions Requisite for Initiation of Proceedings (Sec 190-199)", 119, 125),
    (16, "Complaints to Magistrates & Commencement of Proceedings (Sec 200-210)", 126, 131),
    (17, "The Charge (Sec 211-224)", 132, 140),
    (18, "Trial before a Court of Session (Sec 225-237)", 141, 144),
    (19, "Trial of Warrant-Cases by Magistrates (Sec 238-250)", 145, 148),
    (20, "Trial of Summons-Cases by Magistrates (Sec 251-259)", 149, 151),
    (21, "Summary Trials (Sec 260-265)", 152, 155),
    (22, "Plea Bargaining (Sec 265A-265L)", 156, 159),
    (23, "Attendance of Persons Confined or Detained in Prisons (Sec 266-271)", 160, 160),
    (24, "Evidence in Inquiries and Trials (Sec 272-299)", 161, 163),
    (25, "General Provisions as to Inquiries and Trials (Sec 300-327)", 164, 187),
    (26, "Provisions as to Accused Persons of Unsound Mind (Sec 328-352)", 188, 188),
    (27, "The Judgment (Sec 353-365)", 189, 197),
    (28, "Submission of Death Sentences for Confirmation (Sec 366-371)", 198, 199),
    (29, "Appeals (Sec 372-394)", 200, 209),
    (30, "Reference and Revision (Sec 395-405)", 210, 212),
    (31, "Transfer of Criminal Cases (Sec 406-412)", 213, 214),
    (32, "Execution, Suspension, Remission and Commutation of Sentences (Sec 413-435)", 215, 218),
    (33, "Provisions as to Bail and Bonds (Sec 436-450)", 219, 228),
    (34, "Disposal of Property (Sec 451-459)", 229, 229),
    (35, "Irregular Proceedings (Sec 460-466)", 230, 235),
    (36, "Limitation for Taking Cognizance of Certain Offences (Sec 467-473)", 236, 240),
    (37, "Miscellaneous (Sec 474-484)", 241, 243),
    (38, "First and Second Schedules", 244, 246),
    (39, "Practice and Revision Questions", 247, 256)
]

grand_total = 0
for ch_num, title, p_s, p_e in crpc_chapters:
    lines = []
    for p in range(p_s - 1, p_e):
        lines.append(doc[p].get_text())
    text = '\n'.join(lines)
    ans = re.findall(r'\nAns\s*[\.:]\s*\(([a-eA-E\*&, ]+)\)', text)
    print(f"Ch {ch_num:02d}: {title:<65} | pp. {p_s:3d}-{p_e:3d} | Ans: {len(ans):3d}")
    grand_total += len(ans)

print("="*85)
print(f"Total counted across CrPC chapters: {grand_total}")
