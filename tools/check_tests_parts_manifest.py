import json

with open('manifest.json', 'r', encoding='utf-8') as f:
    m = json.load(f)

hist_tests = [t for t in m.get('tests', []) if t.get('categoryId') == 'tgt_pgt_history']
print(f"Total tgt_pgt_history tests in manifest.json: {len(hist_tests)}")
for t in hist_tests:
    print(f"  {t.get('testId'):<45} | part: {t.get('partId'):<24} | Qs: {t.get('totalQuestions'):<4} | Dur: {t.get('durationMinutes')}")
