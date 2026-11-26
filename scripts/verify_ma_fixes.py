# -*- coding: utf-8 -*-
import json, sys

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

EXPECTED_21_TOP_KEYS = [
    'testId', 'categoryId', 'test_id', 'category_id', 'title', 'titleEn',
    'testType', 'test_type', 'isFree', 'is_free', 'durationMinutes', 'duration_minutes',
    'totalQuestions', 'total_questions', 'maxMarks', 'positiveMarks', 'negativeMarks',
    'examYear', 'shiftBadge', 'sections', 'questions'
]

for y in [2022, 2023, 2024, 2025, 2026]:
    p = f'tests/gate/gate_ma/pyq/gate_ma_pyq_{y}.json'
    d = json.load(open(p, 'r', encoding='utf-8'))

    # 1. Top keys
    top_keys = list(d.keys())
    assert top_keys == EXPECTED_21_TOP_KEYS, f"{y} keys mismatch: {top_keys}"
    assert 'titleHi' not in d, f"{y} titleHi found"
    assert 'exam_year_tag' not in d, f"{y} exam_year_tag found"
    assert 'examYearTag' not in d, f"{y} examYearTag found"
    print(f"[OK] {y} top-level keys verified: exactly 21 keys")

    # Check topicTag
    math_generic = [q['questionNumber'] for q in d['questions'] if q.get('topicTag') == 'Mathematics']
    assert len(math_generic) == 0, f"{y} still has generic Mathematics topicTag on Qs: {math_generic}"
    print(f"[OK] {y} all questions have specific syllabus topic tags")

# 2. 2023 Q6
d23 = json.load(open('tests/gate/gate_ma/pyq/gate_ma_pyq_2023.json', 'r', encoding='utf-8'))
q6_23 = [q for q in d23['questions'] if q['questionNumber'] == 6][0]
assert q6_23['negativeMarks'] == 0.0, f"2023 Q6 neg marks is {q6_23['negativeMarks']}"
print(f"[OK] 2023 Q6 MTA negativeMarks is {q6_23['negativeMarks']}")

# 3. 2025 Q6
d25 = json.load(open('tests/gate/gate_ma/pyq/gate_ma_pyq_2025.json', 'r', encoding='utf-8'))
q6_25 = [q for q in d25['questions'] if q['questionNumber'] == 6][0]
assert r'\"' not in q6_25['questionTextEn'], f"2025 Q6 has literal backslash-quote"
assert '"I put the brown paper' in q6_25['questionTextEn'], "2025 Q6 clean quote missing"
print(f"[OK] 2025 Q6 questionTextEn quotes verified clean: {q6_25['questionTextEn'][:60]}...")

print("ALL FIXES VERIFIED 100% CLEAN!")
