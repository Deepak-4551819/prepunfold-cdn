import pymupdf
import re

pdf_path = r'C:\Users\yedde\Downloads\Ghatnachakra_Polity_2022_English.pdf'
doc = pymupdf.open(pdf_path)

chapters = [
    (1, 'The Constitutional Development of India', 'constitutional_development', 9, 26),
    (2, 'Constituent Assembly and Making of the Constitution', 'constituent_assembly', 27, 33),
    (3, 'Articles of the Constitution', 'articles_of_constitution', 33, 53),
    (4, 'The Preamble', 'the_preamble', 53, 61),
    (5, 'The Governance System', 'the_governance_system', 61, 73),
    (6, 'National Symbols', 'national_symbols', 73, 75),
    (7, 'State and the Union Territories', 'state_and_union_territories', 75, 84),
    (8, 'The Citizenship', 'the_citizenship', 84, 87),
    (9, 'Fundamental Rights', 'fundamental_rights', 87, 113),
    (10, 'Directive Principles of State Policy', 'directive_principles', 113, 123),
    (11, 'Fundamental Duties', 'fundamental_duties', 123, 129),
    (12, 'The President', 'the_president', 129, 150),
    (13, 'The Vice-President', 'the_vice_president', 150, 153),
    (14, 'The Council of Ministers', 'the_council_of_ministers', 153, 166),
    (15, 'The Attorney General and the C.A.G.', 'attorney_general_and_cag', 166, 174),
    (16, 'Order of Precedence', 'order_of_precedence', 174, 175),
    (17, 'The Parliament (1)', 'the_parliament_1', 175, 191),
    (18, 'The Parliament (2)', 'the_parliament_2', 192, 200),
    (19, 'The Parliament (3)', 'the_parliament_3', 201, 231),
    (20, 'The Parliament (4)', 'the_parliament_4', 231, 241),
    (21, 'The Supreme Court', 'the_supreme_court', 241, 259),
    (22, 'The Governor', 'the_governor', 259, 267),
    (23, 'The State Legislature', 'the_state_legislature', 268, 278),
    (24, 'The High Court', 'the_high_court', 278, 287),
    (25, 'The Centre-State Relations', 'centre_state_relations', 287, 295),
    (26, 'Emergency Provisions', 'emergency_provisions', 295, 301),
    (27, 'The Finance Commission', 'the_finance_commission', 301, 306),
    (28, 'The Planning Commission/Niti Aayog', 'planning_commission_niti_aayog', 306, 311),
    (29, 'Lokpal and Important Commissions', 'lokpal_and_important_commissions', 311, 324),
    (30, 'Temporary Special Provisions', 'temporary_special_provisions', 324, 326),
    (31, 'Election Commission', 'election_commission', 326, 335),
    (32, 'Political Parties', 'political_parties', 336, 344),
    (33, 'Constitutional Amendments', 'constitutional_amendments', 345, 356),
    (34, 'Official Language', 'official_language', 356, 360),
    (35, 'Panchayati Raj and Community Development', 'panchayati_raj', 360, 389),
    (36, 'Special Provision for Certain Classes', 'special_provisions_certain_classes', 389, 395),
    (37, 'Miscellaneous', 'miscellaneous', 396, 424)
]

total_qs = 0
for ch_num, title, slug, start_d, end_d in chapters:
    p_start = start_d - 5
    p_end = min(len(doc), end_d - 4)
    ch_text = []
    for p in range(p_start, p_end):
        for line in doc[p].get_text().split('\n'):
            s = line.strip()
            if s.startswith('Join− https://t.me') or s.startswith('D–') or s == 'General Studies' or s == 'Indian Polity and Governance':
                continue
            ch_text.append(line)
    full_text = '\n'.join(ch_text)

    expected = 1
    pos = 0
    while True:
        m = re.search(r'\n\s*' + str(expected) + r'\s*\.\s+', full_text[pos:])
        if not m:
            break
        pos = pos + m.start() + len(m.group())
        expected += 1
    count = expected - 1
    total_qs += count
    print(f"Ch {ch_num:02d}: {title:45s} -> {count:3d} questions")

print("="*60)
print(f"Grand Total Questions: {total_qs}")
