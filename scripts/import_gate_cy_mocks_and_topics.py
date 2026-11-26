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

ZIP_PATH = r"C:\Users\yedde\Downloads\gate_cy_mocks_and_topic_tests.zip"
BASE_DIR = "tests/gate/gate_cy"
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
        "partId": "part_02_qc",
        "partTitleEn": "Section 2: Quantum Chemistry & Atomic Structure",
        "partTitleHi": "खंड 2: क्वांटम रसायन एवं परमाण्विक संरचना",
        "order": 2,
        "topicCount": 2,
        "questionCount": 40
    },
    {
        "partId": "part_03_gt",
        "partTitleEn": "Section 3: Group Theory & Molecular Spectroscopy",
        "partTitleHi": "खंड 3: समूह सिद्धांत एवं आणविक स्पेक्ट्रोस्कोपी",
        "order": 3,
        "topicCount": 2,
        "questionCount": 40
    },
    {
        "partId": "part_04_thermo",
        "partTitleEn": "Section 4: Chemical Thermodynamics & Phase Equilibria",
        "partTitleHi": "खंड 4: रासायनिक ऊष्मागतिकी एवं प्रावस्था साम्य",
        "order": 4,
        "topicCount": 2,
        "questionCount": 40
    },
    {
        "partId": "part_05_elec",
        "partTitleEn": "Section 5: Statistical Thermodynamics & Electrochemistry",
        "partTitleHi": "खंड 5: सांख्यिकीय ऊष्मागतिकी एवं विद्युत रसायन",
        "order": 5,
        "topicCount": 2,
        "questionCount": 40
    },
    {
        "partId": "part_06_kinetics",
        "partTitleEn": "Section 6: Chemical Kinetics, Surface & Polymer Chemistry",
        "partTitleHi": "खंड 6: रासायनिक बलगतिकी, पृष्ठ एवं बहुलक रसायन",
        "order": 6,
        "topicCount": 2,
        "questionCount": 40
    },
    {
        "partId": "part_07_maingroup",
        "partTitleEn": "Section 7: Main Group & Solid State Chemistry",
        "partTitleHi": "खंड 7: मुख्य समूह एवं ठोस अवस्था रसायन",
        "order": 7,
        "topicCount": 2,
        "questionCount": 40
    },
    {
        "partId": "part_08_coord",
        "partTitleEn": "Section 8: Coordination Chemistry & f-Block Elements",
        "partTitleHi": "खंड 8: उपसहसंयोजन रसायन एवं f-ब्लॉक तत्व",
        "order": 8,
        "topicCount": 2,
        "questionCount": 40
    },
    {
        "partId": "part_09_organo",
        "partTitleEn": "Section 9: Organometallic, Bioinorganic & Nuclear Chemistry",
        "partTitleHi": "खंड 9: कार्बधात्विक, जैव-अकार्बनिक एवं नाभिकीय रसायन",
        "order": 9,
        "topicCount": 2,
        "questionCount": 40
    },
    {
        "partId": "part_10_stereo",
        "partTitleEn": "Section 10: Stereochemistry, Conformations & Reaction Mechanisms",
        "partTitleHi": "खंड 10: त्रिविम रसायन, संरूपण एवं अभिक्रिया क्रियाविधि",
        "order": 10,
        "topicCount": 2,
        "questionCount": 40
    },
    {
        "partId": "part_11_synth",
        "partTitleEn": "Section 11: Organic Synthesis, Reagents, Pericyclic & Photochemistry",
        "partTitleHi": "खंड 11: कार्बनिक संश्लेषण, अभिकर्मक, पेरीसाइक्लिक एवं प्रकाश रसायन",
        "order": 11,
        "topicCount": 2,
        "questionCount": 40
    },
    {
        "partId": "part_12_orgspec",
        "partTitleEn": "Section 12: Organic Spectroscopy, Heterocycles & Biomolecules",
        "partTitleHi": "खंड 12: कार्बनिक स्पेक्ट्रोस्कोपी, विषमचक्रीय यौगिक एवं जैव अणु",
        "order": 12,
        "topicCount": 2,
        "questionCount": 40
    }
]

TOPIC_MAPPING = {
    "gate_cy_topic_general_aptitude": {
        "partId": "part_01_ga",
        "partTitle": "General Aptitude",
        "partTitleEn": "Section 1: General Aptitude",
        "partTitleHi": "सामान्य योग्यता",
        "order": 1
    },
    "gate_cy_topic_quantum_chemistry": {
        "partId": "part_02_qc",
        "partTitle": "Quantum Chemistry & Atomic Structure",
        "partTitleEn": "Section 2: Quantum Chemistry & Atomic Structure",
        "partTitleHi": "क्वांटम रसायन एवं परमाण्विक संरचना",
        "order": 2
    },
    "gate_cy_topic_group_theory_spectroscopy": {
        "partId": "part_03_gt",
        "partTitle": "Group Theory & Molecular Spectroscopy",
        "partTitleEn": "Section 3: Group Theory & Molecular Spectroscopy",
        "partTitleHi": "समूह सिद्धांत एवं आणविक स्पेक्ट्रोस्कोपी",
        "order": 3
    },
    "gate_cy_topic_thermodynamics_phase": {
        "partId": "part_04_thermo",
        "partTitle": "Chemical Thermodynamics & Phase Equilibria",
        "partTitleEn": "Section 4: Chemical Thermodynamics & Phase Equilibria",
        "partTitleHi": "रासायनिक ऊष्मागतिकी एवं प्रावस्था साम्य",
        "order": 4
    },
    "gate_cy_topic_stat_thermo_electrochem": {
        "partId": "part_05_elec",
        "partTitle": "Statistical Thermodynamics & Electrochemistry",
        "partTitleEn": "Section 5: Statistical Thermodynamics & Electrochemistry",
        "partTitleHi": "सांख्यिकीय ऊष्मागतिकी एवं विद्युत रसायन",
        "order": 5
    },
    "gate_cy_topic_kinetics_surface_polymer": {
        "partId": "part_06_kinetics",
        "partTitle": "Chemical Kinetics, Surface & Polymer Chemistry",
        "partTitleEn": "Section 6: Chemical Kinetics, Surface & Polymer Chemistry",
        "partTitleHi": "रासायनिक बलगतिकी, पृष्ठ एवं बहुलक रसायन",
        "order": 6
    },
    "gate_cy_topic_main_group_solid_state": {
        "partId": "part_07_maingroup",
        "partTitle": "Main Group & Solid State Chemistry",
        "partTitleEn": "Section 7: Main Group & Solid State Chemistry",
        "partTitleHi": "मुख्य समूह एवं ठोस अवस्था रसायन",
        "order": 7
    },
    "gate_cy_topic_coordination_f_block": {
        "partId": "part_08_coord",
        "partTitle": "Coordination Chemistry & f-Block Elements",
        "partTitleEn": "Section 8: Coordination Chemistry & f-Block Elements",
        "partTitleHi": "उपसहसंयोजन रसायन एवं f-ब्लॉक तत्व",
        "order": 8
    },
    "gate_cy_topic_organometallics_bioinorganic": {
        "partId": "part_09_organo",
        "partTitle": "Organometallic, Bioinorganic & Nuclear Chemistry",
        "partTitleEn": "Section 9: Organometallic, Bioinorganic & Nuclear Chemistry",
        "partTitleHi": "कार्बधात्विक, जैव-अकार्बनिक एवं नाभिकीय रसायन",
        "order": 9
    },
    "gate_cy_topic_stereo_mechanisms": {
        "partId": "part_10_stereo",
        "partTitle": "Stereochemistry, Conformations & Reaction Mechanisms",
        "partTitleEn": "Section 10: Stereochemistry, Conformations & Reaction Mechanisms",
        "partTitleHi": "त्रिविम रसायन, संरूपण एवं अभिक्रिया क्रियाविधि",
        "order": 10
    },
    "gate_cy_topic_synthesis_pericyclic_photo": {
        "partId": "part_11_synth",
        "partTitle": "Organic Synthesis, Reagents, Pericyclic & Photochemistry",
        "partTitleEn": "Section 11: Organic Synthesis, Reagents, Pericyclic & Photochemistry",
        "partTitleHi": "कार्बनिक संश्लेषण, अभिकर्मक, पेरीसाइक्लिक एवं प्रकाश रसायन",
        "order": 11
    },
    "gate_cy_topic_organic_spec_heterocycles_bio": {
        "partId": "part_12_orgspec",
        "partTitle": "Organic Spectroscopy, Heterocycles & Biomolecules",
        "partTitleEn": "Section 12: Organic Spectroscopy, Heterocycles & Biomolecules",
        "partTitleHi": "कार्बनिक स्पेक्ट्रोस्कोपी, विषमचक्रीय यौगिक एवं जैव अणु",
        "order": 12
    }
}

LETTER_TO_IDX = {"A": 0, "B": 1, "C": 2, "D": 3}

def clean_question(q, is_mock, test_num, part_title=None, set_num=None):
    qt = q['questionType']
    pos = float(q.get('positiveMarks', 1.0))
    qnum = int(q['questionNumber'])
    exp_en = (q.get('explanationEn') or q.get('explanation') or '').strip()
    is_mta = "MTA" in (str(q.get("correctOption")) + exp_en)

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

    if is_mock:
        pyq_tag = f"GATE CY Mock {test_num:02d}"
    else:
        pyq_tag = f"GATE CY Topic • {part_title} (Set {set_num:02d})"

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
    norm_q['questionId'] = q.get('questionId') or f"gate_cy_q{qnum:02d}"
    norm_q['questionNumber'] = qnum
    norm_q['sectionId'] = q.get('sectionId', 'sec_ga' if qnum <= 10 and is_mock else 'sec_cy')
    norm_q['sectionTitle'] = q.get('sectionTitle', 'General Aptitude' if qnum <= 10 and is_mock else 'Chemistry')
    norm_q['questionType'] = qt
    norm_q['positiveMarks'] = pos
    norm_q['negativeMarks'] = neg
    norm_q['pyqTag'] = pyq_tag
    norm_q['topicTag'] = q.get('topicTag') or ('General Aptitude' if norm_q['sectionId'] == 'sec_ga' else 'Chemistry')
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
    # Clean up any legacy empty folders in TOPIC_TESTS_DIR
    if os.path.exists(TOPIC_TESTS_DIR):
        for sub in ["01_physical_chemistry", "02_inorganic_chemistry", "03_organic_chemistry"]:
            p = os.path.join(TOPIC_TESTS_DIR, sub)
            if os.path.exists(p) and not os.listdir(p):
                shutil.rmtree(p)
                print(f"Removed legacy empty dir: {p}")

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
                shift_badge = f"GATE CY • Full Mock {num:02d}"
                norm_qs = [clean_question(q, is_mock=True, test_num=num) for q in questions_raw]
            else:
                base = tid.rsplit('_', 1)[0]
                set_num = int(tid.split('_')[-1])
                meta = TOPIC_MAPPING[base]
                part_title = meta['partTitle']
                part_id = meta['partId']
                shift_badge = f"GATE CY • {part_title} • Set {set_num:02d}"
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
            test_obj["categoryId"] = "gate_cy"
            test_obj["test_id"] = tid
            test_obj["category_id"] = "gate_cy"
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

    # 1. Update Category gate_cy
    for cat in manifest.get('categories', []):
        if cat.get('id') == 'gate_cy':
            cat['title'] = 'GATE Chemistry (CY)'
            cat['titleEn'] = 'GATE Chemistry (CY)'
            cat['titleHi'] = 'गेट रसायन विज्ञान (CY)'
            cat['subtitle'] = 'Official Master PYQs (2022–2026) + 10 Full Mocks + 24 Topic Tests'
            cat['subtitleEn'] = 'Official Master PYQs (2022–2026) + 10 Full Mocks + 24 Topic Tests'
            cat['subtitleHi'] = 'आधिकारिक मास्टर PYQs (2022–2026) + 10 संपूर्ण मॉक + 24 टॉपिक टेस्ट'
            cat['descriptionEn'] = 'Official Master PYQs (2022–2026) + 10 Full Mocks + 24 Topic Tests'
            cat['descriptionHi'] = 'आधिकारिक मास्टर PYQs (2022–2026) + 10 संपूर्ण मॉक + 24 टॉपिक टेस्ट'
            cat['totalTests'] = 39
            cat['totalQuestions'] = 1455
            cat['parts'] = PARTS_DEF
            break

    # 2. Existing PYQs in manifest for gate_cy
    existing_pyqs = [t for t in manifest.get('tests', []) if t.get('categoryId') == 'gate_cy' and t.get('testType') == 'PYQ']
    print(f"Preserving {len(existing_pyqs)} existing official PYQs in manifest")

    # 3. Build Mock entries
    new_mock_entries = []
    for tid, t, out_path, num in imported_mocks:
        rel_path = out_path.replace('\\', '/')
        entry = {
            "test_id": tid,
            "testId": tid,
            "category_id": "gate_cy",
            "categoryId": "gate_cy",
            "test_type": "FULL_MOCK",
            "testType": "FULL_MOCK",
            "title": t["title"],
            "titleEn": t["titleEn"],
            "titleHi": f"GATE 2027 रसायन विज्ञान (CY) संपूर्ण मॉक टेस्ट {num:02d}",
            "exam_year_tag": "2027",
            "examYearTag": "2027",
            "shiftBadge": t["shiftBadge"],
            "duration_minutes": 180,
            "durationMinutes": 180,
            "total_questions": 65,
            "totalQuestions": 65,
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
            "category_id": "gate_cy",
            "categoryId": "gate_cy",
            "test_type": "TOPIC",
            "testType": "TOPIC",
            "title": t["title"],
            "titleEn": t["titleEn"],
            "titleHi": f"गेट रसायन विज्ञान टॉपिक टेस्ट: {part_hi} — सेट {set_num:02d}",
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

    # 5. Assemble all 39 gate_cy tests
    all_cy_entries = existing_pyqs + new_mock_entries + new_topic_entries
    print(f"Total gate_cy manifest test entries: {len(all_cy_entries)}")

    # 6. Replace gate_cy block in manifest['tests']
    tests = manifest.get('tests', [])
    first_cy_idx = None
    for i, t in enumerate(tests):
        if t.get('categoryId') == 'gate_cy':
            first_cy_idx = i
            break

    if first_cy_idx is None:
        first_cy_idx = len(tests)

    # Remove all existing gate_cy entries
    tests = [t for t in tests if t.get('categoryId') != 'gate_cy']

    # Insert all 39 tests at first_cy_idx
    for offset, entry in enumerate(all_cy_entries):
        tests.insert(first_cy_idx + offset, entry)

    manifest['tests'] = tests

    with open('manifest.json', 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"✓ Updated manifest.json: 39 gate_cy tests placed starting at index {first_cy_idx}")

    # 7. Refresh seen_question_hashes.json
    with open('seen_question_hashes.json', 'r', encoding='utf-8') as f:
        hashes = json.load(f)

    # Purge existing gate_cy hashes
    old_cnt = len([k for k, v in hashes.items() if v.get('categoryId') == 'gate_cy'])
    hashes = {k: v for k, v in hashes.items() if v.get('categoryId') != 'gate_cy'}
    print(f"Purged {old_cnt} gate_cy hashes from seen_question_hashes.json")

    added = 0
    # PYQs
    for yr in [2026, 2025, 2024, 2023, 2022]:
        p = f"tests/gate/gate_cy/pyq/gate_cy_pyq_{yr}.json"
        with open(p, 'r', encoding='utf-8') as jf:
            d = json.load(jf)
        for q in d['questions']:
            text = q.get('questionTextEn', '')
            norm = re.sub(r'\s+', ' ', text.strip().lower())
            h = hashlib.sha256(norm.encode('utf-8')).hexdigest()[:16]
            hashes[h] = {
                'questionId': q['questionId'],
                'testId': d['testId'],
                'categoryId': 'gate_cy',
                'topicTag': q.get('topicTag', 'Chemistry')
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
                'categoryId': 'gate_cy',
                'topicTag': q.get('topicTag', 'Chemistry')
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
                'categoryId': 'gate_cy',
                'topicTag': q.get('topicTag', 'Chemistry')
            }
            added += 1

    with open('seen_question_hashes.json', 'w', encoding='utf-8') as f:
        json.dump(hashes, f, ensure_ascii=False, indent=2)
    print(f"✓ Refreshed seen_question_hashes.json: processed {added} questions, current total hashes: {len(hashes)}")

if __name__ == '__main__':
    mocks, topics = import_all()
    update_manifest_and_hashes(mocks, topics)
    print("\n✓ GATE Chemistry (CY) Mocks and Topic Tests import complete!")
