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

ZIP_PATH = r"C:\Users\yedde\Downloads\jam_ma_mocks_and_topic_tests.zip"
BASE_DIR = "tests/jam/jam_ma"
FULL_MOCKS_DIR = os.path.join(BASE_DIR, "full_mocks")
TOPIC_TESTS_DIR = os.path.join(BASE_DIR, "topic_tests")

CDN_BASE = "https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/"
ALT_CDN_BASE = "https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main/"

PARTS_DEF = [
    {
        "partId": "part_01_seq_series",
        "partTitleEn": "Section 1: Sequences & Series of Real Numbers",
        "partTitleHi": "खंड 1: वास्तविक संख्याओं के अनुक्रम एवं श्रेणी",
        "order": 1,
        "topicCount": 2,
        "questionCount": 40
    },
    {
        "partId": "part_02_single_var",
        "partTitleEn": "Section 2: Functions of One Real Variable",
        "partTitleHi": "खंड 2: एक चर के वास्तविक फलन",
        "order": 2,
        "topicCount": 2,
        "questionCount": 40
    },
    {
        "partId": "part_03_multivar",
        "partTitleEn": "Section 3: Multivariable Calculus",
        "partTitleHi": "खंड 3: बहुचर कलन",
        "order": 3,
        "topicCount": 2,
        "questionCount": 40
    },
    {
        "partId": "part_04_integral",
        "partTitleEn": "Section 4: Integral Calculus",
        "partTitleHi": "खंड 4: समाकलन कलन",
        "order": 4,
        "topicCount": 2,
        "questionCount": 40
    },
    {
        "partId": "part_05_ode",
        "partTitleEn": "Section 5: Ordinary Differential Equations",
        "partTitleHi": "खंड 5: साधारण अवकल समीकरण",
        "order": 5,
        "topicCount": 2,
        "questionCount": 40
    },
    {
        "partId": "part_06_matrices",
        "partTitleEn": "Section 6: Matrices, Linear Systems & Eigenvalues",
        "partTitleHi": "खंड 6: आव्यूह, रैखिक निकाय एवं अभिलाक्षणिक मान",
        "order": 6,
        "topicCount": 2,
        "questionCount": 40
    },
    {
        "partId": "part_07_vector_spaces",
        "partTitleEn": "Section 7: Vector Spaces & Linear Transformations",
        "partTitleHi": "खंड 7: सदिश समष्टि एवं रैखिक रूपांतरण",
        "order": 7,
        "topicCount": 2,
        "questionCount": 40
    },
    {
        "partId": "part_08_group_theory",
        "partTitleEn": "Section 8: Group Theory & Abstract Algebra",
        "partTitleHi": "खंड 8: समूह सिद्धांत एवं अमूर्त बीजगणित",
        "order": 8,
        "topicCount": 2,
        "questionCount": 40
    }
]

TOPIC_MAPPING = {
    "jam_ma_topic_sequences_series": {
        "partId": "part_01_seq_series",
        "partTitle": "Sequences & Series of Real Numbers",
        "partTitleEn": "Section 1: Sequences & Series of Real Numbers",
        "partTitleHi": "वास्तविक संख्याओं के अनुक्रम एवं श्रेणी",
        "order": 1
    },
    "jam_ma_topic_single_var_calculus": {
        "partId": "part_02_single_var",
        "partTitle": "Functions of One Real Variable",
        "partTitleEn": "Section 2: Functions of One Real Variable",
        "partTitleHi": "एक चर के वास्तविक फलन",
        "order": 2
    },
    "jam_ma_topic_multivariable_calculus": {
        "partId": "part_03_multivar",
        "partTitle": "Multivariable Calculus",
        "partTitleEn": "Section 3: Multivariable Calculus",
        "partTitleHi": "बहुचर कलन",
        "order": 3
    },
    "jam_ma_topic_integral_calculus": {
        "partId": "part_04_integral",
        "partTitle": "Integral Calculus",
        "partTitleEn": "Section 4: Integral Calculus",
        "partTitleHi": "समाकलन कलन",
        "order": 4
    },
    "jam_ma_topic_differential_equations": {
        "partId": "part_05_ode",
        "partTitle": "Ordinary Differential Equations",
        "partTitleEn": "Section 5: Ordinary Differential Equations",
        "partTitleHi": "साधारण अवकल समीकरण",
        "order": 5
    },
    "jam_ma_topic_linear_algebra_matrices": {
        "partId": "part_06_matrices",
        "partTitle": "Matrices, Linear Systems & Eigenvalues",
        "partTitleEn": "Section 6: Matrices, Linear Systems & Eigenvalues",
        "partTitleHi": "आव्यूह, रैखिक निकाय एवं अभिलाक्षणिक मान",
        "order": 6
    },
    "jam_ma_topic_vector_spaces_transforms": {
        "partId": "part_07_vector_spaces",
        "partTitle": "Vector Spaces & Linear Transformations",
        "partTitleEn": "Section 7: Vector Spaces & Linear Transformations",
        "partTitleHi": "सदिश समष्टि एवं रैखिक रूपांतरण",
        "order": 7
    },
    "jam_ma_topic_group_theory_combinatorics": {
        "partId": "part_08_group_theory",
        "partTitle": "Group Theory & Abstract Algebra",
        "partTitleEn": "Section 8: Group Theory & Abstract Algebra",
        "partTitleHi": "समूह सिद्धांत एवं अमूर्त बीजगणित",
        "order": 8
    }
}

LETTER_TO_IDX = {"A": 0, "B": 1, "C": 2, "D": 3}

def clean_question(q, is_mock, test_num, part_title=None, set_num=None):
    qt = q['questionType']
    pos = float(q.get('positiveMarks', 1.0))
    qnum = int(q['questionNumber'])
    exp_en = (q.get('explanationEn') or q.get('explanation') or '').strip()
    is_mta = "MTA" in (str(q.get("correctOption")) + exp_en)

    # Standardize negative marks to positive value
    if is_mta:
        neg = 0.0
    elif qt == 'MCQ':
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

    # Section ID / Title
    if is_mock:
        if qnum <= 30:
            sec_id, sec_title = "sec_a", "Section A (MCQ)"
        elif qnum <= 40:
            sec_id, sec_title = "sec_b", "Section B (MSQ)"
        else:
            sec_id, sec_title = "sec_c", "Section C (NAT)"
        pyq_tag = f"IIT JAM MA Mock {test_num:02d}"
    else:
        if qt == 'MCQ':
            sec_id, sec_title = "sec_a", "Section A (MCQ)"
        elif qt == 'MSQ':
            sec_id, sec_title = "sec_b", "Section B (MSQ)"
        else:
            sec_id, sec_title = "sec_c", "Section C (NAT)"
        pyq_tag = f"IIT JAM MA Topic • {part_title} (Set {set_num:02d})"

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
        if is_mta:
            co = None
            col = ["A", "B", "C", "D"]
            c_idx = None
            c_indices = [0, 1, 2, 3]
        else:
            co = None
            col = q.get('correctOptionsList') or []
            c_idx = None
            c_indices = q.get('correct_indices') or [LETTER_TO_IDX[x] for x in col if x in LETTER_TO_IDX]
        nmin = None
        nmax = None
    else:  # MCQ
        if is_mta:
            co = q.get('correctOption', 'A')
            col = ["A", "B", "C", "D"]
            c_idx = LETTER_TO_IDX.get(co, 0)
            c_indices = [0, 1, 2, 3]
        else:
            co = q.get('correctOption')
            col = q.get('correctOptionsList') or ([co] if co else [])
            c_idx = q.get('correct_index')
            if c_idx is None and co in LETTER_TO_IDX:
                c_idx = LETTER_TO_IDX[co]
            c_indices = q.get('correct_indices') or ([c_idx] if c_idx is not None else [])
        nmin = None
        nmax = None

    norm_q = OrderedDict()
    norm_q['questionId'] = q.get('questionId') or f"jam_ma_q{qnum:02d}"
    norm_q['questionNumber'] = qnum
    norm_q['sectionId'] = sec_id
    norm_q['sectionTitle'] = sec_title
    norm_q['questionType'] = qt
    norm_q['positiveMarks'] = pos
    norm_q['negativeMarks'] = neg
    norm_q['pyqTag'] = pyq_tag
    norm_q['topicTag'] = q.get('topicTag') or ('Real Analysis' if not part_title else part_title)
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
            if not name.endswith('.json') or 'snippet' in name:
                continue
            raw = json.loads(z.read(name).decode('utf-8'))
            tid = raw['testId']
            is_mock = 'mock' in name.lower()
            questions_raw = raw.get('questions', [])

            if is_mock:
                num = int(tid.split('_')[-1])
                shift_badge = f"IIT JAM MA • Full Mock {num:02d}"
                norm_qs = [clean_question(q, is_mock=True, test_num=num) for q in questions_raw]
            else:
                base = tid.rsplit('_', 1)[0]
                set_num = int(tid.split('_')[-1])
                meta = TOPIC_MAPPING[base]
                part_title = meta['partTitle']
                part_id = meta['partId']
                shift_badge = f"IIT JAM MA • {part_title} • Set {set_num:02d}"
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
            test_obj["categoryId"] = "jam_ma"
            test_obj["test_id"] = tid
            test_obj["category_id"] = "jam_ma"
            test_obj["title"] = raw["title"]
            test_obj["titleEn"] = raw.get("titleEn", raw["title"])
            if is_mock:
                test_obj["testType"] = "FULL_MOCK"
                test_obj["test_type"] = "FULL_MOCK"
            else:
                test_obj["testType"] = "TOPIC"
                test_obj["test_type"] = "TOPIC"
                test_obj["partId"] = meta["partId"]
                test_obj["part_id"] = meta["partId"]
                test_obj["partTitle"] = meta["partTitle"]

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
            test_obj["shiftBadge"] = shift_badge
            test_obj["sections"] = sections
            test_obj["questions"] = norm_qs

            if is_mock:
                out_path = os.path.join(FULL_MOCKS_DIR, f"{tid}.json")
                imported_mocks.append((tid, test_obj, out_path, num))
            else:
                part_dir = os.path.join(TOPIC_TESTS_DIR, meta["partId"])
                os.makedirs(part_dir, exist_ok=True)
                out_path = os.path.join(part_dir, f"{tid}.json")
                imported_topics.append((tid, test_obj, out_path, meta["partId"], set_num, meta))

            with open(out_path, 'w', encoding='utf-8') as f:
                json.dump(test_obj, f, ensure_ascii=False, indent=2)

    imported_mocks.sort(key=lambda x: x[3])
    imported_topics.sort(key=lambda x: (x[5]["order"], x[4]))

    print(f"✓ Imported and wrote {len(imported_mocks)} full mocks.")
    print(f"✓ Imported and wrote {len(imported_topics)} topic tests.")
    return imported_mocks, imported_topics

def update_manifest_and_hashes(imported_mocks, imported_topics):
    with open('manifest.json', 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    # 1. Update Category jam_ma
    for cat in manifest.get('categories', []):
        if cat.get('id') == 'jam_ma':
            cat['title'] = 'IIT JAM Mathematics (MA)'
            cat['titleEn'] = 'IIT JAM Mathematics (MA)'
            cat['titleHi'] = 'आईआईटी जैम गणित (MA)'
            cat['subtitle'] = 'Official Master PYQs (2022–2026) + 10 Full Mocks + 16 Topic Tests'
            cat['subtitleEn'] = 'Official Master PYQs (2022–2026) + 10 Full Mocks + 16 Topic Tests'
            cat['subtitleHi'] = 'आधिकारिक मास्टर PYQs (2022–2026) + 10 संपूर्ण मॉक + 16 टॉपिक टेस्ट'
            cat['descriptionEn'] = 'Official Master PYQs (2022–2026) + 10 Full Mocks + 16 Topic Tests'
            cat['descriptionHi'] = 'आधिकारिक मास्टर PYQs (2022–2026) + 10 संपूर्ण मॉक + 16 टॉपिक टेस्ट'
            cat['totalTests'] = 31
            cat['totalQuestions'] = 1220
            cat['parts'] = PARTS_DEF
            break

    # 2. Existing PYQs in manifest for jam_ma
    existing_pyqs = [t for t in manifest.get('tests', []) if t.get('categoryId') == 'jam_ma' and t.get('testType') == 'PYQ']
    print(f"Preserving {len(existing_pyqs)} existing official PYQs in manifest")

    # 3. Build Mock entries
    new_mock_entries = []
    for tid, t, out_path, num in imported_mocks:
        rel_path = out_path.replace('\\', '/')
        entry = {
            "test_id": tid,
            "testId": tid,
            "category_id": "jam_ma",
            "categoryId": "jam_ma",
            "test_type": "FULL_MOCK",
            "testType": "FULL_MOCK",
            "title": t["title"],
            "titleEn": t["titleEn"],
            "titleHi": f"IIT JAM 2027 गणित (MA) संपूर्ण मॉक टेस्ट {num:02d}",
            "exam_year_tag": "2027",
            "examYearTag": "2027",
            "shiftBadge": t["shiftBadge"],
            "duration_minutes": 180,
            "durationMinutes": 180,
            "total_questions": 60,
            "totalQuestions": 60,
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

    # 4. Build Topic Test entries
    new_topic_entries = []
    for tid, t, out_path, part_id, set_num, meta in imported_topics:
        rel_path = out_path.replace('\\', '/')
        part_hi = meta["partTitleHi"]
        entry = {
            "test_id": tid,
            "testId": tid,
            "category_id": "jam_ma",
            "categoryId": "jam_ma",
            "test_type": "TOPIC",
            "testType": "TOPIC",
            "title": t["title"],
            "titleEn": t["titleEn"],
            "titleHi": f"आईआईटी जैम गणित टॉपिक टेस्ट: {part_hi} — सेट {set_num:02d}",
            "exam_year_tag": "2027",
            "examYearTag": "2027",
            "shiftBadge": t["shiftBadge"],
            "duration_minutes": 45,
            "durationMinutes": 45,
            "total_questions": 20,
            "totalQuestions": 20,
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
            "part_id": part_id,
            "partId": part_id
        }
        new_topic_entries.append(entry)

    # 5. Assemble all 31 jam_ma tests
    all_jam_ma_entries = existing_pyqs + new_mock_entries + new_topic_entries
    print(f"Total jam_ma manifest test entries: {len(all_jam_ma_entries)}")

    # 6. Replace jam_ma block in manifest['tests']
    tests = manifest.get('tests', [])
    first_idx = None
    for i, t in enumerate(tests):
        if t.get('categoryId') == 'jam_ma':
            first_idx = i
            break

    if first_idx is None:
        first_idx = len(tests)

    # Remove all existing jam_ma entries
    tests = [t for t in tests if t.get('categoryId') != 'jam_ma']

    # Insert all 31 tests at first_idx
    for offset, entry in enumerate(all_jam_ma_entries):
        tests.insert(first_idx + offset, entry)

    manifest['tests'] = tests

    with open('manifest.json', 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"✓ Updated manifest.json: 31 jam_ma tests placed starting at index {first_idx}")

    # 7. Refresh seen_question_hashes.json
    with open('seen_question_hashes.json', 'r', encoding='utf-8') as f:
        hashes = json.load(f)

    # Purge existing jam_ma hashes
    old_cnt = len([k for k, v in hashes.items() if v.get('categoryId') == 'jam_ma'])
    hashes = {k: v for k, v in hashes.items() if v.get('categoryId') != 'jam_ma'}
    print(f"Purged {old_cnt} jam_ma hashes from seen_question_hashes.json")

    added = 0
    # PYQs
    for yr in [2026, 2025, 2024, 2023, 2022]:
        p = f"tests/jam/jam_ma/pyq/jam_ma_pyq_{yr}.json"
        with open(p, 'r', encoding='utf-8') as jf:
            d = json.load(jf)
        for q in d['questions']:
            text = q.get('questionTextEn', '')
            norm = re.sub(r'\s+', ' ', text.strip().lower())
            h = hashlib.sha256(norm.encode('utf-8')).hexdigest()[:16]
            hashes[h] = {
                'questionId': q['questionId'],
                'testId': d['testId'],
                'categoryId': 'jam_ma',
                'topicTag': q.get('topicTag', 'Mathematics')
            }
            added += 1

    # Full Mocks
    for tid, t, out_path, num in imported_mocks:
        for q in t['questions']:
            text = q.get('questionTextEn', '')
            norm = re.sub(r'\s+', ' ', text.strip().lower())
            h = hashlib.sha256(norm.encode('utf-8')).hexdigest()[:16]
            hashes[h] = {
                'questionId': q['questionId'],
                'testId': t['testId'],
                'categoryId': 'jam_ma',
                'topicTag': q.get('topicTag', 'Mathematics')
            }
            added += 1

    # Topic Tests
    for tid, t, out_path, part_id, set_num, meta in imported_topics:
        for q in t['questions']:
            text = q.get('questionTextEn', '')
            norm = re.sub(r'\s+', ' ', text.strip().lower())
            h = hashlib.sha256(norm.encode('utf-8')).hexdigest()[:16]
            hashes[h] = {
                'questionId': q['questionId'],
                'testId': t['testId'],
                'categoryId': 'jam_ma',
                'topicTag': q.get('topicTag', 'Mathematics')
            }
            added += 1

    with open('seen_question_hashes.json', 'w', encoding='utf-8') as f:
        json.dump(hashes, f, ensure_ascii=False, indent=2)
    print(f"✓ Refreshed seen_question_hashes.json: processed {added} questions, current total hashes: {len(hashes)}")

if __name__ == '__main__':
    mocks, topics = import_all()
    update_manifest_and_hashes(mocks, topics)
    print("\n✓ IIT JAM Mathematics (MA) Mocks and Topic Tests import complete!")
