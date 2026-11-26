import json

with open('tests/tgt_pgt_history/tgt_pgt_hist_ch25_governors_viceroys.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print(f"Total questions: {len(d['questions'])}, durationMinutes: {d['durationMinutes']}")
for i, q in enumerate(d['questions'][:5], 1):
    print(f"\n--- Question {i} ---")
    print(f"PYQ: {q['pyqTag']}")
    print(f"Hi : {q['questionTextHi']}")
    print(f"En : {q['questionTextEn']}")
    print(f"Ans: {q['correctOption']}")
    print(f"OptHi: {q['optionsHi']}")
    print(f"OptEn: {q['optionsEn']}")
    print(f"ExpHi: {q['explanationHi'][:80]}...")
    print(f"ExpEn: {q['explanationEn'][:80]}...")

# Also check last question
last_q = d['questions'][-1]
print(f"\n--- Last Question ({last_q['questionNumber']}) ---")
print(f"Hi : {last_q['questionTextHi']}")
print(f"En : {last_q['questionTextEn']}")
print(f"OptHi: {last_q['optionsHi']}")
print(f"OptEn: {last_q['optionsEn']}")
