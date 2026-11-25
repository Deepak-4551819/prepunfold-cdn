import json

data = json.load(open('scripts/raw_2025_curated.json', encoding='utf-8'))
with open('scripts/raw_part2_out.txt', 'w', encoding='utf-8') as out:
    for q in data:
        if 36 <= q['qnum'] <= 65:
            out.write(f"=== Q{q['qnum']} ({q['qtype']}, Key: {q['key']}) ===\n")
            out.write(q['text_en'] + "\n")
            if q['opts_en']:
                out.write("OPTS:\n")
                for opt in q['opts_en']:
                    out.write(f"  {opt}\n")
            out.write("-" * 50 + "\n")
