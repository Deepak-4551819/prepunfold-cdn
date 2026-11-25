import json

d = json.load(open('scripts/raw_2025_curated.json', encoding='utf-8'))
for q in d[35:]:
    print(f"=== Q{q['qnum']} ({q['qtype']}, {q['marks']}M, ans={q['key']}) ===")
    print("Text:", q['text_en'][:200])
    if q['opts_en']:
        for idx, o in enumerate(q['opts_en']):
            print(f"  ({chr(65+idx)}) {o[:80]}")
    print()
