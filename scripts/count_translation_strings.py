import os, json

econ_q = set()
econ_opt = set()
for root, dirs, files in os.walk('tests/teaching/tgt_pgt_economics'):
    for f in files:
        if f.endswith('.json'):
            with open(os.path.join(root, f), 'r', encoding='utf-8') as fp:
                for q in json.load(fp).get('questions', []):
                    if q.get('questionTextEn'): econ_q.add(q['questionTextEn'].strip())
                    for o in q.get('optionsEn', []):
                        if o: econ_opt.add(o.strip())

other_q = set()
other_opt = set()
for cat in ['tgt_pgt_civics', 'tgt_pgt_history', 'tgt_pgt_geography']:
    for root, dirs, files in os.walk(os.path.join('tests/teaching', cat)):
        for f in files:
            if f.endswith('.json'):
                with open(os.path.join(root, f), 'r', encoding='utf-8') as fp:
                    for q in json.load(fp).get('questions', []):
                        if q.get('questionTextHi'): other_q.add(q['questionTextHi'].strip())
                        for o in q.get('optionsHi', []):
                            if o: other_opt.add(o.strip())

print(f"Econ (EN->HI): {len(econ_q)} unique Qs, {len(econ_opt)} unique options")
print(f"Civ/Hist/Geo (HI->EN): {len(other_q)} unique Qs, {len(other_opt)} unique options")
