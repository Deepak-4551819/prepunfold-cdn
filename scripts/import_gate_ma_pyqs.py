# -*- coding: utf-8 -*-
import os
import sys
import json
import shutil
import zipfile
from collections import OrderedDict

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ZIP_PATH = r"C:\Users\yedde\Downloads\gate_ma_official_pyqs_2022_2026.zip"
TARGET_DIR = "tests/gate/gate_ma/pyq"
OLD_MOCK_DIR = "tests/gate/gate_ma/full_mocks"

CDN_BASE = "https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/"
ALT_CDN_BASE = "https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main/"

EXPECTED_19_KEYS = [
    'questionId', 'questionNumber', 'sectionId', 'sectionTitle', 'questionType',
    'positiveMarks', 'negativeMarks', 'pyqTag', 'topicTag', 'difficulty',
    'correctOption', 'correctOptionsList', 'correct_index', 'correct_indices',
    'natMin', 'natMax', 'questionTextEn', 'optionsEn', 'explanationEn'
]

def clean_question(q, year):
    qt = q['questionType']
    pos = float(q.get('positiveMarks', 1.0))
    qnum = int(q['questionNumber'])

    # Standardize negativeMarks
    if qt == 'MCQ':
        if pos == 2.0:
            neg = 0.67
        elif pos == 1.0:
            neg = 0.33
        else:
            neg = round(pos / 3.0, 2)
    else:
        neg = 0.0

    # Ensure difficulty is clean Title case
    diff = q.get('difficulty', 'Medium')
    if diff.upper() in ('EASY', 'E'):
        diff = 'Easy'
    elif diff.upper() in ('HARD', 'H'):
        diff = 'Hard'
    else:
        diff = 'Medium'

    qtext_en = (q.get('questionTextEn') or q.get('questionText') or '').strip()
    options_en = q.get('optionsEn') or q.get('options') or []
    exp_en = (q.get('explanationEn') or q.get('explanation') or '').strip()

    # NAT handling
    if qt == 'NAT':
        options_en = []
        col = []
        c_idx = None
        c_indices = []
        nmin = q.get('natMin')
        nmax = q.get('natMax')
        if nmin is not None and nmax is not None:
            nmin = float(nmin)
            nmax = float(nmax)
            if nmin == nmax:
                co = f"{nmin:g}"
            else:
                co = f"{nmin:g} to {nmax:g}"
        else:
            co = str(q.get('correctOption', ''))
    elif qt == 'MSQ':
        co = None
        col = q.get('correctOptionsList') or []
        c_idx = None
        c_indices = q.get('correct_indices') or []
        nmin = None
        nmax = None
    else:  # MCQ
        co = q.get('correctOption')
        col = q.get('correctOptionsList') or ([co] if co else [])
        c_idx = q.get('correct_index')
        c_indices = q.get('correct_indices') or ([c_idx] if c_idx is not None else [])
        nmin = None
        nmax = None

    norm_q = OrderedDict()
    norm_q['questionId'] = f"gate_ma_{year}_q{qnum:02d}"
    norm_q['questionNumber'] = qnum
    norm_q['sectionId'] = q.get('sectionId', 'sec_ga' if qnum <= 10 else 'sec_ma')
    norm_q['sectionTitle'] = q.get('sectionTitle', 'General Aptitude' if qnum <= 10 else 'Mathematics')
    norm_q['questionType'] = qt
    norm_q['positiveMarks'] = pos
    norm_q['negativeMarks'] = neg
    norm_q['pyqTag'] = q.get('pyqTag') or f"GATE MA {year}"
    norm_q['topicTag'] = q.get('topicTag') or ('General Aptitude' if qnum <= 10 else 'Mathematics')
    norm_q['difficulty'] = diff
    norm_q['correctOption'] = co
    norm_q['correctOptionsList'] = col
    norm_q['correct_index'] = c_idx
    norm_q['correct_indices'] = c_indices
    norm_q['natMin'] = nmin
    norm_q['natMax'] = nmax
    norm_q['questionTextEn'] = qtext_en
    norm_q['optionsEn'] = options_en
    norm_q['explanationEn'] = exp_en

    return norm_q

def import_and_normalize():
    if os.path.exists(OLD_MOCK_DIR):
        shutil.rmtree(OLD_MOCK_DIR)
        print(f"Removed legacy stub dir: {OLD_MOCK_DIR}")

    os.makedirs(TARGET_DIR, exist_ok=True)

    imported_tests = {}

    with zipfile.ZipFile(ZIP_PATH, 'r') as z:
        for name in sorted(z.namelist()):
            if not name.endswith('.json'):
                continue
            raw = json.loads(z.read(name).decode('utf-8'))
            tid = raw['testId']
            year = int(raw.get('examYear') or tid.split('_')[-1])
            is_free = bool(raw.get('isFree', year == 2022))

            questions_raw = raw.get('questions', [])
            norm_questions = [clean_question(q, year) for q in questions_raw]

            # Build sections dynamically
            sec_map = OrderedDict()
            for q in norm_questions:
                sid = q['sectionId']
                stitle = q['sectionTitle']
                if sid not in sec_map:
                    sec_map[sid] = {
                        "sectionId": sid,
                        "sectionTitle": stitle,
                        "sectionTitleEn": stitle,
                        "questionCount": 0,
                        "totalMarks": 0.0
                    }
                sec_map[sid]["questionCount"] += 1
                sec_map[sid]["totalMarks"] = round(sec_map[sid]["totalMarks"] + float(q["positiveMarks"]), 2)
            sections = list(sec_map.values())

            test_obj = OrderedDict()
            test_obj["testId"] = tid
            test_obj["categoryId"] = "gate_ma"
            test_obj["test_id"] = tid
            test_obj["category_id"] = "gate_ma"
            test_obj["title"] = f"GATE {year} Mathematics (MA) Official Solved Paper (All Core Subjects & GA)"
            test_obj["titleEn"] = f"GATE {year} Mathematics (MA) Official Solved Paper (All Core Subjects & GA)"
            test_obj["titleHi"] = f"GATE {year} गणित (MA) आधिकारिक हल प्रश्न पत्र (सभी मुख्य विषय एवं GA)"
            test_obj["testType"] = "PYQ"
            test_obj["test_type"] = "PYQ"
            test_obj["isFree"] = is_free
            test_obj["is_free"] = is_free
            test_obj["durationMinutes"] = 180
            test_obj["duration_minutes"] = 180
            test_obj["totalQuestions"] = len(norm_questions)
            test_obj["total_questions"] = len(norm_questions)
            test_obj["maxMarks"] = 100.0
            test_obj["positiveMarks"] = 2.0
            test_obj["negativeMarks"] = 0.33
            test_obj["examYear"] = year
            test_obj["exam_year_tag"] = str(year)
            test_obj["examYearTag"] = str(year)
            test_obj["shiftBadge"] = f"GATE MA • {year} Official Paper"
            test_obj["sections"] = sections
            test_obj["questions"] = norm_questions

            out_path = os.path.join(TARGET_DIR, f"{tid}.json")
            with open(out_path, 'w', encoding='utf-8') as out_f:
                json.dump(test_obj, out_f, ensure_ascii=False, indent=2)

            print(f"✓ Wrote {out_path} ({len(norm_questions)} Qs, 100.0 marks, isFree={is_free})")
            imported_tests[year] = test_obj

    return imported_tests

def update_manifest_and_hashes(imported_tests):
    with open('manifest.json', 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    # 1. Update Category gate_ma
    for cat in manifest.get('categories', []):
        if cat.get('id') == 'gate_ma':
            cat['title'] = 'GATE Mathematics (MA)'
            cat['titleEn'] = 'GATE Mathematics (MA)'
            cat['titleHi'] = 'गेट गणित (MA)'
            cat['subtitle'] = 'Official Master PYQs (2022–2026)'
            cat['subtitleEn'] = 'Official Master PYQs (2022–2026)'
            cat['subtitleHi'] = 'आधिकारिक मास्टर PYQs (2022–2026)'
            cat['descriptionEn'] = 'Official Master PYQs (2022–2026)'
            cat['descriptionHi'] = 'आधिकारिक मास्टर PYQs (2022–2026)'
            cat['totalTests'] = 5
            cat['totalQuestions'] = 325
            break

    # 2. Build test entries (2026 down to 2022)
    new_ma_test_entries = []
    for y in [2026, 2025, 2024, 2023, 2022]:
        t = imported_tests[y]
        tid = t['testId']
        rel_path = f"tests/gate/gate_ma/pyq/{tid}.json"
        is_free = t['isFree']
        entry = {
            "test_id": tid,
            "testId": tid,
            "category_id": "gate_ma",
            "categoryId": "gate_ma",
            "test_type": "PYQ",
            "testType": "PYQ",
            "title": t["title"],
            "titleEn": t["titleEn"],
            "titleHi": t["titleHi"],
            "exam_year_tag": str(y),
            "examYearTag": str(y),
            "shiftBadge": f"GATE MA • {y} Official Paper",
            "duration_minutes": 180,
            "durationMinutes": 180,
            "total_questions": 65,
            "totalQuestions": 65,
            "positive_marks": 2.0,
            "positiveMarks": 2.0,
            "negative_marks": 0.33,
            "negativeMarks": 0.33,
            "is_free": is_free,
            "isFree": is_free,
            "version": 1,
            "path": rel_path,
            "filePath": rel_path,
            "file_path": rel_path,
            "json_url": f"{CDN_BASE}{rel_path}",
            "cdnUrl": f"{CDN_BASE}{rel_path}",
            "altCdnUrl": f"{ALT_CDN_BASE}{rel_path}"
        }
        new_ma_test_entries.append(entry)

    # 3. Replace old gate_ma tests in manifest['tests']
    tests_list = manifest.get('tests', [])
    first_idx = None
    last_idx = None
    for idx, t in enumerate(tests_list):
        if t.get('categoryId') == 'gate_ma':
            if first_idx is None:
                first_idx = idx
            last_idx = idx

    if first_idx is not None:
        print(f"Replacing gate_ma test(s) at indices [{first_idx}:{last_idx+1}] with 5 new official PYQs.")
        manifest['tests'] = tests_list[:first_idx] + new_ma_test_entries + tests_list[last_idx+1:]
    else:
        print("Appending 5 new gate_ma official PYQs to manifest.tests.")
        manifest['tests'].extend(new_ma_test_entries)

    with open('manifest.json', 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print("✓ manifest.json updated successfully!")

    # 4. Refresh seen_question_hashes.json
    import hashlib, re
    with open('seen_question_hashes.json', 'r', encoding='utf-8') as f:
        hashes = json.load(f)

    old_ma_count = sum(1 for v in hashes.values() if v.get('categoryId') == 'gate_ma')
    print(f"Removing {old_ma_count} old gate_ma hashes from seen_question_hashes...")
    hashes = {k: v for k, v in hashes.items() if v.get('categoryId') != 'gate_ma'}

    added = 0
    for y in [2026, 2025, 2024, 2023, 2022]:
        t = imported_tests[y]
        tid = t['testId']
        for q in t['questions']:
            text = q.get('questionTextEn', '')
            norm = re.sub(r'\s+', ' ', text.strip().lower())
            h = hashlib.sha256(norm.encode('utf-8')).hexdigest()[:16]
            hashes[h] = {
                'questionId': q['questionId'],
                'testId': tid,
                'categoryId': 'gate_ma',
                'topicTag': q.get('topicTag', 'Mathematics')
            }
            added += 1

    with open('seen_question_hashes.json', 'w', encoding='utf-8') as f:
        json.dump(hashes, f, ensure_ascii=False, indent=2)
    print(f"✓ Added {added} fresh gate_ma question hashes to seen_question_hashes.json (Total: {len(hashes)})")

if __name__ == '__main__':
    imported = import_and_normalize()
    update_manifest_and_hashes(imported)
    print("ALL GATE MA IMPORT & UPDATE STEPS COMPLETED!")
