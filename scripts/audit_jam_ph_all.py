# -*- coding: utf-8 -*-
import os
import sys
import json
import re
import hashlib

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def compute_question_hash(text):
    norm = re.sub(r'\s+', ' ', text.strip().lower())
    return hashlib.sha256(norm.encode('utf-8')).hexdigest()[:16]

EXPECTED_19_KEYS = [
    'questionId', 'questionNumber', 'sectionId', 'sectionTitle', 'questionType',
    'positiveMarks', 'negativeMarks', 'pyqTag', 'topicTag', 'difficulty',
    'correctOption', 'correctOptionsList', 'correct_index', 'correct_indices',
    'natMin', 'natMax', 'questionTextEn', 'optionsEn', 'explanationEn'
]

TOP_LEVEL_21_KEYS = [
    'testId', 'categoryId', 'test_id', 'category_id', 'title', 'titleEn',
    'testType', 'test_type', 'isFree', 'is_free', 'durationMinutes', 'duration_minutes',
    'totalQuestions', 'total_questions', 'maxMarks', 'positiveMarks', 'negativeMarks',
    'examYear', 'shiftBadge', 'sections', 'questions'
]

TOP_LEVEL_24_KEYS = [
    'testId', 'categoryId', 'test_id', 'category_id', 'title', 'titleEn',
    'testType', 'test_type', 'partId', 'part_id', 'partTitle', 'isFree', 'is_free',
    'durationMinutes', 'duration_minutes', 'totalQuestions', 'total_questions',
    'maxMarks', 'positiveMarks', 'negativeMarks', 'examYear', 'shiftBadge',
    'sections', 'questions'
]

def main():
    errors = []
    print("=== 1. AUDITING MANIFEST.JSON FOR IIT JAM PH SUITE ===")
    with open('manifest.json', 'r', encoding='utf-8') as f:
        mf = json.load(f)

    # 1. Check category
    cat = next((c for c in mf.get('categories', []) if c.get('id') == 'jam_ph'), None)
    if not cat:
        errors.append("Category 'jam_ph' not found in manifest.json")
    else:
        print(f"[OK] Category jam_ph metadata: {len(cat.get('parts', []))} parts, {cat.get('totalTests')} tests, {cat.get('totalQuestions')} questions")
        if cat.get('totalTests') != 29:
            errors.append(f"Category totalTests is {cat.get('totalTests')}, expected 29")
        if cat.get('totalQuestions') != 1180:
            errors.append(f"Category totalQuestions is {cat.get('totalQuestions')}, expected 1180")
        if len(cat.get('parts', [])) != 7:
            errors.append(f"Category parts count is {len(cat.get('parts', []))}, expected 7")

    # 2. Check test entries
    tests = [t for t in mf.get('tests', []) if t.get('categoryId') == 'jam_ph']
    print(f"[OK] Manifest contains exactly {len(tests)} jam_ph test entries")
    if len(tests) != 29:
        errors.append(f"Expected 29 tests in manifest, found {len(tests)}")

    pyq_cnt = len([t for t in tests if t.get('testType') == 'PYQ'])
    mock_cnt = len([t for t in tests if t.get('testType') == 'FULL_MOCK'])
    topic_cnt = len([t for t in tests if t.get('testType') == 'TOPIC'])
    print(f"[OK] Test type breakdown: {pyq_cnt} PYQs, {mock_cnt} Full Mocks, {topic_cnt} Topic Tests")
    if pyq_cnt != 5 or mock_cnt != 10 or topic_cnt != 14:
        errors.append(f"Test type breakdown mismatch: {pyq_cnt} PYQs, {mock_cnt} Full Mocks, {topic_cnt} Topic Tests")

    for t in tests:
        p = t.get('path')
        if not os.path.exists(p):
            errors.append(f"Manifest path missing on disk: {p}")

    print("=== 2. AUDITING ALL 29 IIT JAM PH TEST FILES ON DISK ===")
    total_q_count = 0
    file_hashes = {}

    for t in tests:
        fpath = t.get('path')
        if not os.path.exists(fpath):
            continue

        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        is_topic = t.get('testType') == 'TOPIC'
        is_mock = t.get('testType') == 'FULL_MOCK'
        is_pyq = t.get('testType') == 'PYQ'

        # Check top keys
        expected_top_keys = TOP_LEVEL_24_KEYS if is_topic else TOP_LEVEL_21_KEYS
        if list(data.keys()) != expected_top_keys:
            errors.append(f"{fpath}: Top keys mismatch")

        qs = data.get('questions', [])
        total_q_count += len(qs)
        expected_qc = 20 if is_topic else 60
        expected_marks = 30.0 if is_topic else 100.0

        if len(qs) != expected_qc:
            errors.append(f"{fpath}: Question count {len(qs)} != {expected_qc}")

        calc_marks = 0.0
        sec_marks = {}
        sec_qcounts = {}

        for q in qs:
            qnum = q.get('questionNumber')
            qt = q.get('questionType')
            pos = float(q.get('positiveMarks', 0.0))
            neg = float(q.get('negativeMarks', 0.0))
            calc_marks += pos
            sec = q.get('sectionTitle', '')
            qtext = q.get('questionTextEn', '')
            opts = q.get('optionsEn', [])
            exp = q.get('explanationEn', '')
            co = q.get('correctOption')
            col = q.get('correctOptionsList')
            nmin = q.get('natMin')
            nmax = q.get('natMax')

            # Check question keys
            if list(q.keys()) != EXPECTED_19_KEYS:
                errors.append(f"{fpath} Q{qnum}: Question keys mismatch: {list(q.keys())}")

            sec_marks[sec] = round(sec_marks.get(sec, 0.0) + pos, 2)
            sec_qcounts[sec] = sec_qcounts.get(sec, 0) + 1

            # Check negative marks
            is_mta = "MTA" in (str(co) + exp)
            if is_mta:
                if neg != 0.0:
                    errors.append(f"{fpath} Q{qnum}: MTA negativeMarks {neg} != 0.0")
            elif qt == 'MCQ':
                if pos == 1.0 and abs(neg - 0.33) > 0.01:
                    errors.append(f"{fpath} Q{qnum}: 1m MCQ negativeMarks {neg} != 0.33")
                elif pos == 2.0 and abs(neg - 0.67) > 0.01:
                    errors.append(f"{fpath} Q{qnum}: 2m MCQ negativeMarks {neg} != 0.67")
            else:
                if neg != 0.0:
                    errors.append(f"{fpath} Q{qnum}: {qt} negativeMarks {neg} != 0.0")

            # Check options
            if qt in ('MCQ', 'MSQ'):
                if len(opts) != 4:
                    errors.append(f"{fpath} Q{qnum}: {qt} options count {len(opts)} != 4")
            elif qt == 'NAT':
                if len(opts) != 0:
                    errors.append(f"{fpath} Q{qnum}: NAT has options: {opts}")
                if not is_mta and (nmin is None or nmax is None):
                    errors.append(f"{fpath} Q{qnum}: Non-MTA NAT missing natMin/natMax")

            # Check LaTeX balance
            for text_f, fld in [(qtext, 'questionTextEn'), (exp, 'explanationEn')] + [(opt, f'opt_{i}') for i, opt in enumerate(opts)]:
                if text_f and text_f.count('$') % 2 != 0:
                    errors.append(f"{fpath} Q{qnum} {fld}: Unbalanced $")

            h = compute_question_hash(qtext)
            file_hashes[h] = q.get('questionId')

        if abs(calc_marks - expected_marks) > 0.01:
            errors.append(f"{fpath}: Total marks {calc_marks} != expected {expected_marks}")

        if is_topic:
            expected_sec_qc = {'Section A (MCQ)': 10, 'Section B (MSQ)': 4, 'Section C (NAT)': 6}
            expected_sec_marks = {'Section A (MCQ)': 15.0, 'Section B (MSQ)': 8.0, 'Section C (NAT)': 7.0}
        else:
            expected_sec_qc = {'Section A (MCQ)': 30, 'Section B (MSQ)': 10, 'Section C (NAT)': 20}
            expected_sec_marks = {'Section A (MCQ)': 50.0, 'Section B (MSQ)': 20.0, 'Section C (NAT)': 30.0}

        if sec_qcounts != expected_sec_qc:
            errors.append(f"{fpath}: Section question counts mismatch: {sec_qcounts} vs {expected_sec_qc}")
        if sec_marks != expected_sec_marks:
            errors.append(f"{fpath}: Section marks mismatch: {sec_marks} vs {expected_sec_marks}")

    print(f"[OK] Scanned {len(tests)} files, total questions: {total_q_count}")

    print("=== 3. AUDITING SEEN_QUESTION_HASHES.JSON ===")
    with open('seen_question_hashes.json', 'r', encoding='utf-8') as f:
        seen = json.load(f)

    jam_ph_hashes = {k: v for k, v in seen.items() if isinstance(v, dict) and v.get('categoryId') == 'jam_ph'}
    print(f"[OK] Exactly {len(jam_ph_hashes)} hashes indexed for jam_ph in seen_question_hashes.json (1180 questions processed)")
    if len(jam_ph_hashes) != 1180:
        errors.append(f"Expected 1180 hashes for jam_ph, found {len(jam_ph_hashes)}")

    for h, qid in file_hashes.items():
        if h not in seen:
            errors.append(f"Hash for {qid} not found in seen_question_hashes.json")

    print("=== SUMMARY ===")
    if errors:
        print(f"FAILED WITH {len(errors)} ERRORS:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("ALL 29 IIT JAM PH AUDIT CHECKS PASSED PERFECTLY! 100% READY!")

if __name__ == '__main__':
    main()
