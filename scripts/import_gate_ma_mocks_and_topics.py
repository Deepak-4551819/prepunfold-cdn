# -*- coding: utf-8 -*-
import os
import sys
import json
import shutil
import zipfile
import hashlib
import re
from collections import OrderedDict

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ZIP_PATH = r"C:\Users\yedde\Downloads\gate_ma_mocks_and_topic_tests.zip"
BASE_DIR = "tests/gate/gate_ma"
FULL_MOCKS_DIR = os.path.join(BASE_DIR, "full_mocks")
TOPIC_TESTS_DIR = os.path.join(BASE_DIR, "topic_tests")

CDN_BASE = "https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/"
ALT_CDN_BASE = "https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main/"

PARTS_DEF = [
    {
        "partId": "part_01_ga",
        "partTitleEn": "Section 1: General Aptitude",
        "partTitleHi": "खंड 1: सामान्य योग्यता",
        "order": 1,
        "topicCount": 2,
        "questionCount": 40
    },
    {
        "partId": "part_02_cal",
        "partTitleEn": "Section 2: Calculus",
        "partTitleHi": "खंड 2: कलन",
        "order": 2,
        "topicCount": 2,
        "questionCount": 40
    },
    {
        "partId": "part_03_la",
        "partTitleEn": "Section 3: Linear Algebra",
        "partTitleHi": "खंड 3: रैखिक बीजगणित",
        "order": 3,
        "topicCount": 2,
        "questionCount": 40
    },
    {
        "partId": "part_04_ra",
        "partTitleEn": "Section 4: Real Analysis",
        "partTitleHi": "खंड 4: वास्तविक विश्लेषण",
        "order": 4,
        "topicCount": 2,
        "questionCount": 40
    },
    {
        "partId": "part_05_ca",
        "partTitleEn": "Section 5: Complex Analysis",
        "partTitleHi": "खंड 5: सम्मिश्र विश्लेषण",
        "order": 5,
        "topicCount": 2,
        "questionCount": 40
    },
    {
        "partId": "part_06_ode",
        "partTitleEn": "Section 6: Ordinary Differential Equations",
        "partTitleHi": "खंड 6: साधारण अवकल समीकरण",
        "order": 6,
        "topicCount": 2,
        "questionCount": 40
    },
    {
        "partId": "part_07_alg",
        "partTitleEn": "Section 7: Algebra",
        "partTitleHi": "खंड 7: बीजगणित",
        "order": 7,
        "topicCount": 2,
        "questionCount": 40
    },
    {
        "partId": "part_08_fa",
        "partTitleEn": "Section 8: Functional Analysis",
        "partTitleHi": "खंड 8: फलनिक विश्लेषण",
        "order": 8,
        "topicCount": 2,
        "questionCount": 40
    },
    {
        "partId": "part_09_na",
        "partTitleEn": "Section 9: Numerical Analysis",
        "partTitleHi": "खंड 9: संख्यात्मक विश्लेषण",
        "order": 9,
        "topicCount": 2,
        "questionCount": 40
    },
    {
        "partId": "part_10_pde",
        "partTitleEn": "Section 10: Partial Differential Equations",
        "partTitleHi": "खंड 10: आंशिक अवकल समीकरण",
        "order": 10,
        "topicCount": 2,
        "questionCount": 40
    },
    {
        "partId": "part_11_top",
        "partTitleEn": "Section 11: Topology",
        "partTitleHi": "खंड 11: संस्थिति विज्ञान (टोपोलॉजी)",
        "order": 11,
        "topicCount": 2,
        "questionCount": 40
    },
    {
        "partId": "part_12_lp",
        "partTitleEn": "Section 12: Linear Programming",
        "partTitleHi": "खंड 12: रैखिक प्रोग्रामन",
        "order": 12,
        "topicCount": 2,
        "questionCount": 40
    }
]

PART_HI_MAP = {
    "part_01_ga": "सामान्य योग्यता",
    "part_02_cal": "कलन",
    "part_03_la": "रैखिक बीजगणित",
    "part_04_ra": "वास्तविक विश्लेषण",
    "part_05_ca": "सम्मिश्र विश्लेषण",
    "part_06_ode": "साधारण अवकल समीकरण",
    "part_07_alg": "बीजगणित",
    "part_08_fa": "फलनिक विश्लेषण",
    "part_09_na": "संख्यात्मक विश्लेषण",
    "part_10_pde": "आंशिक अवकल समीकरण",
    "part_11_top": "संस्थिति विज्ञान (टोपोलॉजी)",
    "part_12_lp": "रैखिक प्रोग्रामन"
}

EXPECTED_19_KEYS = [
    'questionId', 'questionNumber', 'sectionId', 'sectionTitle', 'questionType',
    'positiveMarks', 'negativeMarks', 'pyqTag', 'topicTag', 'difficulty',
    'correctOption', 'correctOptionsList', 'correct_index', 'correct_indices',
    'natMin', 'natMax', 'questionTextEn', 'optionsEn', 'explanationEn'
]

def clean_question(q, is_mock, test_num, part_title=None, set_num=None):
    qt = q['questionType']
    pos = float(q.get('positiveMarks', 1.0))
    qnum = int(q['questionNumber'])

    if qt == 'MCQ':
        if pos == 2.0:
            neg = 0.67
        elif pos == 1.0:
            neg = 0.33
        else:
            neg = round(pos / 3.0, 2)
    else:
        neg = 0.0

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

    if is_mock:
        pyq_tag = f"GATE MA Mock {test_num:02d}"
    else:
        pyq_tag = f"GATE MA Topic • {part_title} (Set {set_num})"

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
    norm_q['questionId'] = q.get('questionId') or f"gate_ma_q{qnum:02d}"
    norm_q['questionNumber'] = qnum
    norm_q['sectionId'] = q.get('sectionId', 'sec_ga' if qnum <= 10 else 'sec_ma')
    norm_q['sectionTitle'] = q.get('sectionTitle', 'General Aptitude' if qnum <= 10 else 'Mathematics')
    norm_q['questionType'] = qt
    norm_q['positiveMarks'] = pos
    norm_q['negativeMarks'] = neg
    norm_q['pyqTag'] = pyq_tag
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

def import_all():
    os.makedirs(FULL_MOCKS_DIR, exist_ok=True)
    os.makedirs(TOPIC_TESTS_DIR, exist_ok=True)

    imported_mocks = []
    imported_topics = []

    with zipfile.ZipFile(ZIP_PATH, 'r') as z:
        for name in sorted(z.namelist()):
            if not name.endswith('.json'):
                continue
            raw = json.loads(z.read(name).decode('utf-8'))
            tid = raw['testId']
            is_mock = name.startswith('full_mocks/')
            questions_raw = raw.get('questions', [])

            if is_mock:
                num = int(tid.split('_')[-1])
                shift_badge = raw.get('shiftBadge') or f"GATE MA • Full Mock {num:02d}"
                norm_qs = [clean_question(q, is_mock=True, test_num=num) for q in questions_raw]
            else:
                part_title = raw['partTitle']
                part_id = raw['partId']
                set_num = int(tid.split('_')[-1])
                shift_badge = raw.get('shiftBadge') or f"GATE MA • {part_title} • Set {set_num}"
                norm_qs = [clean_question(q, is_mock=False, test_num=0, part_title=part_title, set_num=set_num) for q in questions_raw]

            # Build sections dynamically
            sec_map = OrderedDict()
            for q in norm_qs:
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
            test_obj["title"] = raw["title"]
            test_obj["titleEn"] = raw.get("titleEn", raw["title"])
            if is_mock:
                test_obj["titleHi"] = f"GATE 2027 गणित (MA) संपूर्ण मॉक टेस्ट {num:02d}"
                test_obj["testType"] = "FULL_MOCK"
                test_obj["test_type"] = "FULL_MOCK"
            else:
                test_obj["partId"] = raw["partId"]
                test_obj["part_id"] = raw["partId"]
                test_obj["partTitle"] = raw["partTitle"]
                part_hi = PART_HI_MAP.get(raw["partId"], raw["partTitle"])
                test_obj["titleHi"] = f"गेट गणित टॉपिक टेस्ट: {part_hi} — सेट {set_num}"
                test_obj["testType"] = "TOPIC"
                test_obj["test_type"] = "TOPIC"

            is_free = bool(raw.get("isFree", False))
            test_obj["isFree"] = is_free
            test_obj["is_free"] = is_free
            test_obj["durationMinutes"] = int(raw.get("durationMinutes", 180 if is_mock else 45))
            test_obj["duration_minutes"] = int(raw.get("durationMinutes", 180 if is_mock else 45))
            test_obj["totalQuestions"] = len(norm_qs)
            test_obj["total_questions"] = len(norm_qs)
            test_obj["maxMarks"] = float(raw.get("maxMarks", 100.0 if is_mock else 30.0))
            test_obj["positiveMarks"] = 2.0
            test_obj["negativeMarks"] = 0.33
            test_obj["examYear"] = 2027
            test_obj["exam_year_tag"] = "2027"
            test_obj["examYearTag"] = "2027"
            test_obj["shiftBadge"] = shift_badge
            test_obj["sections"] = sections
            test_obj["questions"] = norm_qs

            if is_mock:
                out_path = os.path.join(FULL_MOCKS_DIR, f"{tid}.json")
                imported_mocks.append((tid, test_obj, out_path))
            else:
                part_dir = os.path.join(TOPIC_TESTS_DIR, raw["partId"])
                os.makedirs(part_dir, exist_ok=True)
                out_path = os.path.join(part_dir, f"{tid}.json")
                imported_topics.append((tid, test_obj, out_path, raw["partId"], set_num))

            with open(out_path, 'w', encoding='utf-8') as f:
                json.dump(test_obj, f, ensure_ascii=False, indent=2)

    print(f"✓ Imported and wrote {len(imported_mocks)} full mocks.")
    print(f"✓ Imported and wrote {len(imported_topics)} topic tests.")
    return imported_mocks, imported_topics

def update_manifest_and_hashes(imported_mocks, imported_topics):
    with open('manifest.json', 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    # 1. Update Category gate_ma
    for cat in manifest.get('categories', []):
        if cat.get('id') == 'gate_ma':
            cat['title'] = 'GATE Mathematics (MA)'
            cat['titleEn'] = 'GATE Mathematics (MA)'
            cat['titleHi'] = 'गेट गणित (MA)'
            cat['subtitle'] = 'Official Master PYQs (2022–2026) + 10 Full Mocks + 24 Topic Tests'
            cat['subtitleEn'] = 'Official Master PYQs (2022–2026) + 10 Full Mocks + 24 Topic Tests'
            cat['subtitleHi'] = 'आधिकारिक मास्टर PYQs (2022–2026) + 10 संपूर्ण मॉक + 24 टॉपिक टेस्ट'
            cat['descriptionEn'] = 'Official Master PYQs (2022–2026) + 10 Full Mocks + 24 Topic Tests'
            cat['descriptionHi'] = 'आधिकारिक मास्टर PYQs (2022–2026) + 10 संपूर्ण मॉक + 24 टॉपिक टेस्ट'
            cat['totalTests'] = 39
            cat['totalQuestions'] = 1455
            cat['parts'] = PARTS_DEF
            break

    # 2. Existing PYQs in manifest for gate_ma
    existing_pyqs = [t for t in manifest.get('tests', []) if t.get('categoryId') == 'gate_ma' and t.get('testType') == 'PYQ']

    # 3. Build Mock entries
    new_mock_entries = []
    for tid, t, out_path in imported_mocks:
        rel_path = out_path.replace('\\', '/')
        entry = {
            "test_id": tid,
            "testId": tid,
            "category_id": "gate_ma",
            "categoryId": "gate_ma",
            "test_type": "FULL_MOCK",
            "testType": "FULL_MOCK",
            "title": t["title"],
            "titleEn": t["titleEn"],
            "titleHi": t["titleHi"],
            "exam_year_tag": "2027",
            "examYearTag": "2027",
            "shiftBadge": t["shiftBadge"],
            "duration_minutes": t["durationMinutes"],
            "durationMinutes": t["durationMinutes"],
            "total_questions": t["totalQuestions"],
            "totalQuestions": t["totalQuestions"],
            "positive_marks": 2.0,
            "positiveMarks": 2.0,
            "negative_marks": 0.33,
            "negativeMarks": 0.33,
            "is_free": t["isFree"],
            "isFree": t["isFree"],
            "version": 1,
            "path": rel_path,
            "filePath": rel_path,
            "file_path": rel_path,
            "json_url": f"{CDN_BASE}{rel_path}",
            "cdnUrl": f"{CDN_BASE}{rel_path}",
            "altCdnUrl": f"{ALT_CDN_BASE}{rel_path}"
        }
        new_mock_entries.append(entry)

    # 4. Build Topic entries
    new_topic_entries = []
    # Sort topics by part order (part_01_ga .. part_12_lp) and set_num
    part_order = {p["partId"]: p["order"] for p in PARTS_DEF}
    sorted_topics = sorted(imported_topics, key=lambda x: (part_order.get(x[3], 99), x[4]))

    for tid, t, out_path, pid, set_num in sorted_topics:
        rel_path = out_path.replace('\\', '/')
        entry = {
            "test_id": tid,
            "testId": tid,
            "category_id": "gate_ma",
            "categoryId": "gate_ma",
            "test_type": "TOPIC",
            "testType": "TOPIC",
            "title": t["title"],
            "titleEn": t["titleEn"],
            "titleHi": t["titleHi"],
            "exam_year_tag": "2027",
            "examYearTag": "2027",
            "shiftBadge": t["shiftBadge"],
            "duration_minutes": t["durationMinutes"],
            "durationMinutes": t["durationMinutes"],
            "total_questions": t["totalQuestions"],
            "totalQuestions": t["totalQuestions"],
            "positive_marks": 2.0,
            "positiveMarks": 2.0,
            "negative_marks": 0.33,
            "negativeMarks": 0.33,
            "is_free": t["isFree"],
            "isFree": t["isFree"],
            "version": 1,
            "path": rel_path,
            "filePath": rel_path,
            "file_path": rel_path,
            "json_url": f"{CDN_BASE}{rel_path}",
            "cdnUrl": f"{CDN_BASE}{rel_path}",
            "altCdnUrl": f"{ALT_CDN_BASE}{rel_path}",
            "part_id": pid,
            "partId": pid
        }
        new_topic_entries.append(entry)

    # Total 39 test entries: 5 PYQs + 10 Mocks + 24 Topics
    all_39_ma_tests = existing_pyqs + new_mock_entries + new_topic_entries

    # Replace in manifest['tests']
    tests_list = manifest.get('tests', [])
    first_idx = None
    last_idx = None
    for idx, t in enumerate(tests_list):
        if t.get('categoryId') == 'gate_ma':
            if first_idx is None:
                first_idx = idx
            last_idx = idx

    print(f"Replacing gate_ma tests from index {first_idx} to {last_idx} ({last_idx - first_idx + 1} old tests) with {len(all_39_ma_tests)} new tests.")
    manifest['tests'] = tests_list[:first_idx] + all_39_ma_tests + tests_list[last_idx + 1:]

    with open('manifest.json', 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print("✓ manifest.json updated with 39 gate_ma tests!")

    # 5. Refresh seen_question_hashes.json
    with open('seen_question_hashes.json', 'r', encoding='utf-8') as f:
        hashes = json.load(f)

    # Purge gate_ma
    hashes = {k: v for k, v in hashes.items() if v.get('categoryId') != 'gate_ma'}

    # Add all 39 tests
    added = 0
    # PYQs
    for y in [2026, 2025, 2024, 2023, 2022]:
        p = f"tests/gate/gate_ma/pyq/gate_ma_pyq_{y}.json"
        with open(p, 'r', encoding='utf-8') as jf:
            d = json.load(jf)
        for q in d['questions']:
            text = q.get('questionTextEn', '')
            norm = re.sub(r'\s+', ' ', text.strip().lower())
            h = hashlib.sha256(norm.encode('utf-8')).hexdigest()[:16]
            hashes[h] = {
                'questionId': q['questionId'],
                'testId': d['testId'],
                'categoryId': 'gate_ma',
                'topicTag': q.get('topicTag', 'Mathematics')
            }
            added += 1

    # Mocks
    for tid, t, out_path in imported_mocks:
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

    # Topics
    for tid, t, out_path, pid, set_num in sorted_topics:
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
    print(f"✓ Added {added} gate_ma question hashes to seen_question_hashes.json (Total: {len(hashes)})")

if __name__ == '__main__':
    mocks, topics = import_all()
    update_manifest_and_hashes(mocks, topics)
    print("ALL GATE MA IMPORT & MANIFEST UPDATE TASKS COMPLETED!")
