import json

with open('tests/tgt_pgt_history/tgt_pgt_hist_ch25_governors_viceroys.json', 'r', encoding='utf-8') as f:
    ch25 = json.load(f)

qs = ch25['questions']
print(f"Total Qs currently in Ch 25: {len(qs)}")
print("Q1 (to be trimmed):", qs[0]['questionTextHi'][:60])
print("Q2 (to be trimmed):", qs[1]['questionTextHi'][:60])
print("Q3 (to become new Q1):", qs[2]['questionTextHi'][:60])
print("Last Q (Q58):", qs[-1]['questionTextHi'][:60])
print(f"New count after trimming Q1 and Q2: {len(qs) - 2} Qs (Q1 to Q{len(qs)-2})")
