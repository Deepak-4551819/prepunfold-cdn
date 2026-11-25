import json

d = json.load(open('scripts/raw_2025_curated.json', encoding='utf-8'))
for q in d[55:]:
    print(f"=== Q{q['qnum']} ({q['qtype']}, {q['marks']}M, ans={q['key']}) ===")
    print("EN:", q['text_en'])
    for i, o in enumerate(q['opts_en']):
        print(f"  ({chr(65+i)}) {o}")
    print()
