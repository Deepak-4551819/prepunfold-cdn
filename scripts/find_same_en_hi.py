import os, json

cats = ['tgt_pgt_economics', 'tgt_pgt_civics']
base = 'tests/teaching'

for cat in cats:
    for root, dirs, files in os.walk(os.path.join(base, cat)):
        for f in files:
            if not f.endswith('.json'):
                continue
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as fp:
                d = json.load(fp)
                for q in d.get('questions', []):
                    q_en = q.get('questionTextEn', '').strip()
                    q_hi = q.get('questionTextHi', '').strip()
                    if q_en and q_hi and q_en == q_hi:
                        print(f"File: {f} | QID: {q.get('questionId')} | Text: {q_en}")
