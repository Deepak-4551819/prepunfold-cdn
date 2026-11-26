import json
import os
import re

with open('manifest.json', 'r', encoding='utf-8') as f:
    mf = json.load(f)

teaching_items = [
    t for t in mf.get('tests', [])
    if 'history' in t.get('testId', '').lower()
    or 'history' in t.get('categoryId', '').lower()
    or 'tgt_pgt' in t.get('categoryId', '').lower()
]

print(f"Total history / tgt_pgt items in manifest.json: {len(teaching_items)}")
for t in teaching_items:
    tid = t.get('testId')
    cid = t.get('categoryId')
    tq = t.get('totalQuestions')
    fp = t.get('filePath')
    print(f"  {tid} | cat={cid} | Qs={tq} | {fp}")

# Check Chapter 25 questions 1, 2, 3
print("\n--- Inspect Chapter 25 initial questions ---")
with open('tests/tgt_pgt_history/tgt_pgt_hist_ch25_governors_viceroys.json', 'r', encoding='utf-8') as f:
    ch25 = json.load(f)

for q in ch25['questions'][:5]:
    print(f"Q{q['questionNumber']}: {q['pyqTag']}")
    print(f"   Hi: {q['questionTextHi'][:100]}")
    print(f"   En: {q['questionTextEn'][:100]}")
    print(f"   OptsHi: {q['optionsHi']}")

# Check chapters 1 to 5 status of English vs Hindi
print("\n--- Check bilingual status across sample chapters ---")
for ch_idx in [1, 5, 10, 15, 20, 25]:
    files = [f for f in os.listdir('tests/tgt_pgt_history') if f.startswith(f'tgt_pgt_hist_ch{ch_idx:02d}')]
    if files:
        with open(os.path.join('tests/tgt_pgt_history', files[0]), 'r', encoding='utf-8') as f:
            data = json.load(f)
        qs = data['questions']
        same_count = sum(1 for q in qs if q.get('questionTextEn') == q.get('questionTextHi'))
        empty_opts = sum(1 for q in qs if any(opt == "" for opt in q.get('optionsHi', [])))
        print(f"Ch {ch_idx:02d} ({files[0]}): Total Qs={len(qs)}, Q_En==Q_Hi: {same_count}/{len(qs)}, Empty Opts: {empty_opts}")
