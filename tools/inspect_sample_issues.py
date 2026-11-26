import json

with open('tests/tgt_pgt_history/tgt_pgt_hist_ch03_vedic_period.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for q in d['questions']:
    if q['questionNumber'] in [1, 34, 38]:
        print(f"=== Q{q['questionNumber']} ===")
        print("  qHi:", q.get('questionTextHi'))
        print("  qEn:", q.get('questionTextEn'))
        print("  optsHi:", q.get('optionsHi'))
        print("  optsEn:", q.get('optionsEn'))
        print("  expHi:", q.get('explanationHi')[:120] if q.get('explanationHi') else '')

with open('tests/tgt_pgt_history/tgt_pgt_hist_ch01_prehistoric_cultures.json', 'r', encoding='utf-8') as f:
    d1 = json.load(f)

for q in d1['questions']:
    if q['questionNumber'] in [16, 20]:
        print(f"=== Ch1 Q{q['questionNumber']} ===")
        print("  qHi:", q.get('questionTextHi'))
        print("  optsHi:", q.get('optionsHi'))
        print("  optsEn:", q.get('optionsEn'))
