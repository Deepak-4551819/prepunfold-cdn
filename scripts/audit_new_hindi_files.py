import json
import re

files = [
    (r'C:\Users\yedde\Downloads\ctet_all_state_tet_hindi_chapterwise.json', 'CTET & State TET'),
    (r'C:\Users\yedde\Downloads\emrs_special_general_hindi_chapterwise.json', 'EMRS General Hindi')
]

akruti_keywords = ['efmeef', 'Deeef', 'Jeeo', 'kesâ', 'ceW', 'efveÙece', 'mebefnlee', 'Oeeje', 'Deveglees', 'Heâ', 'he$e', '«', 'æ', 'ö', 'ø', 'Ç', 'Ì', '¤']

for path, label in files:
    print("=" * 60)
    print(f"Auditing: {label}")
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    total_q = 0
    missing_ans = 0
    missing_options = 0
    found_keywords = {k: 0 for k in akruti_keywords}

    for ch in data.get('chapters', []):
        for q in ch.get('questions', []):
            total_q += 1
            opts = q.get('options', {})
            if len(opts) < 4:
                missing_options += 1
            ans = q.get('answer', '')
            if not ans:
                missing_ans += 1

            full_str = q.get('question', '') + " " + str(opts) + " " + str(q.get('explanation', ''))
            for kw in akruti_keywords:
                if kw in full_str:
                    found_keywords[kw] += 1

    print(f"  Total Questions: {total_q}")
    print(f"  Missing / < 4 Options: {missing_options}")
    print(f"  Missing Answers: {missing_ans}")
    print(f"  Corrupt Keyword Hits: {found_keywords}")
