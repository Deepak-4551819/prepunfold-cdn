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

def main():
    errors = []
    print("=== 1. AUDITING MANIFEST.JSON FOR IIT JAM CY SUITE ===")
    with open('manifest.json', 'r', encoding='utf-8') as f:
        mf = json.load(f)

    # Check category
    cat = next((c for c in mf.get('categories', []) if c.get('id') == 'jam_cy'), None)
    if not cat:
        errors.append("Category 'jam_cy' not found in manifest.json")
    else:
        print(f"[OK] Category jam_cy metadata: testsCount={cat.get('totalTests')}, totalQuestions={cat.get('totalQuestions')}")
        if cat.get('totalTests') != 5:
            errors.append(f"Category totalTests is {cat.get('totalTests')}, expected 5")
        if cat.get('totalQuestions') != 300:
            errors.append(f"Category totalQuestions is {cat.get('totalQuestions')}, expected 300")

    # Check test entries
    tests = [t for t in mf.get('tests', []) if t.get('categoryId') == 'jam_cy']
    print(f"[OK] Manifest contains exactly {len(tests)} jam_cy test entries")
    if len(tests) != 5:
        errors.append(f"Expected 5 jam_cy tests in manifest, found {len(tests)}")

    for t in tests:
        fpath = t.get('path')
        if not os.path.exists(fpath):
            errors.append(f"Manifest path does not exist on disk: {fpath}")

    print("=== 2. AUDITING ALL 5 IIT JAM CY TEST FILES ON DISK ===")
    total_q_count = 0
    file_hashes = {}

    for year in range(2022, 2027):
        fpath = f"tests/jam/jam_cy/pyq/jam_cy_pyq_{year}.json"
        if not os.path.exists(fpath):
            errors.append(f"File missing: {fpath}")
            continue

        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Check top-level keys
        top_keys = list(data.keys())
        if top_keys != TOP_LEVEL_21_KEYS:
            errors.append(f"{fpath}: top keys mismatch. Got {top_keys}")

        qs = data.get('questions', [])
        total_q_count += len(qs)
        if len(qs) != 60:
            errors.append(f"{fpath}: Question count is {len(qs)}, expected 60")

        # Check sections
        sec_marks = {"Section A (MCQ)": 0.0, "Section B (MSQ)": 0.0, "Section C (NAT)": 0.0}
        sec_qcounts = {"Section A (MCQ)": 0, "Section B (MSQ)": 0, "Section C (NAT)": 0}

        for q in qs:
            qnum = q.get('questionNumber')
            qt = q.get('questionType')
            pos = float(q.get('positiveMarks', 0.0))
            neg = float(q.get('negativeMarks', 0.0))
            sec = q.get('sectionTitle', '')
            qtext = q.get('questionTextEn', '')
            opts = q.get('optionsEn', [])
            exp = q.get('explanationEn', '')
            co = q.get('correctOption')
            col = q.get('correctOptionsList')
            nmin = q.get('natMin')
            nmax = q.get('natMax')

            # Check question keys
            qkeys = list(q.keys())
            if qkeys != EXPECTED_19_KEYS:
                errors.append(f"{fpath} Q{qnum}: Question keys mismatch: {qkeys}")

            if sec in sec_marks:
                sec_marks[sec] += pos
                sec_qcounts[sec] += 1
            else:
                errors.append(f"{fpath} Q{qnum}: Unknown section {sec}")

            # LaTeX balance
            for text_f, fld in [(qtext, "questionTextEn"), (exp, "explanationEn")] + [(opt, f"opt_{i}") for i, opt in enumerate(opts)]:
                if text_f and text_f.count("$") % 2 != 0:
                    errors.append(f"{fpath} Q{qnum} {fld}: Unbalanced $")

            # Check hash
            h = compute_question_hash(qtext)
            file_hashes[h] = q.get('questionId')

        if sec_qcounts != {"Section A (MCQ)": 30, "Section B (MSQ)": 10, "Section C (NAT)": 20}:
            errors.append(f"{fpath}: Section question counts mismatch: {sec_qcounts}")
        if sec_marks != {"Section A (MCQ)": 50.0, "Section B (MSQ)": 20.0, "Section C (NAT)": 30.0}:
            errors.append(f"{fpath}: Section marks mismatch: {sec_marks}")

    print(f"[OK] Scanned 5 files, total questions: {total_q_count}")

    print("=== 3. AUDITING SEEN_QUESTION_HASHES.JSON ===")
    with open('seen_question_hashes.json', 'r', encoding='utf-8') as f:
        seen = json.load(f)

    jam_cy_hashes = {k: v for k, v in seen.items() if isinstance(v, dict) and v.get('categoryId') == 'jam_cy'}
    print(f"[OK] Exactly {len(jam_cy_hashes)} hashes indexed for jam_cy in seen_question_hashes.json")
    if len(jam_cy_hashes) != 300:
        errors.append(f"Expected 300 hashes for jam_cy, found {len(jam_cy_hashes)}")

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
        print("ALL 5 IIT JAM CY PYQ AUDIT CHECKS PASSED PERFECTLY! 100% READY!")

if __name__ == '__main__':
    main()
