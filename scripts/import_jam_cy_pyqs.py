# -*- coding: utf-8 -*-
import os
import sys
import json
import shutil
import zipfile
import re
import hashlib
from collections import OrderedDict

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ZIP_PATH = r"C:\Users\yedde\Downloads\jam_cy_official_pyqs_2022_2026.zip"
TARGET_DIR = "tests/jam/jam_cy/pyq"
OLD_MOCK_DIR = "tests/jam/jam_cy/full_mocks"

CDN_BASE = "https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/"
ALT_CDN_BASE = "https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main/"

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

HINDI_YEAR_TITLES = {
    2022: "IIT JAM 2022 रसायन विज्ञान (CY) आधिकारिक हल प्रश्न पत्र",
    2023: "IIT JAM 2023 रसायन विज्ञान (CY) आधिकारिक हल प्रश्न पत्र",
    2024: "IIT JAM 2024 रसायन विज्ञान (CY) आधिकारिक हल प्रश्न पत्र",
    2025: "IIT JAM 2025 रसायन विज्ञान (CY) आधिकारिक हल प्रश्न पत्र",
    2026: "IIT JAM 2026 रसायन विज्ञान (CY) आधिकारिक हल प्रश्न पत्र",
}

def compute_question_hash(text):
    norm = re.sub(r'\s+', ' ', text.strip().lower())
    return hashlib.sha256(norm.encode('utf-8')).hexdigest()[:16]

def clean_question(q, year):
    clean_q = OrderedDict()
    for k in EXPECTED_19_KEYS:
        clean_q[k] = q.get(k)
    return clean_q

def main():
    print("=== STARTING IMPORT OF IIT JAM CHEMISTRY (CY) OFFICIAL PYQS (2022-2026) ===")
    os.makedirs(TARGET_DIR, exist_ok=True)

    # 1. Read and clean test files from zip
    imported_tests = []
    all_new_hashes = {}

    with zipfile.ZipFile(ZIP_PATH, 'r') as z:
        for year in range(2022, 2027):
            fname = f"jam_cy_pyq_{year}.json"
            raw_data = json.loads(z.read(fname).decode('utf-8'))

            clean_test = OrderedDict()
            for k in TOP_LEVEL_21_KEYS:
                if k == 'questions':
                    clean_test['questions'] = [clean_question(q, year) for q in raw_data.get('questions', [])]
                else:
                    clean_test[k] = raw_data.get(k)

            target_path = os.path.join(TARGET_DIR, fname)
            with open(target_path, 'w', encoding='utf-8') as out_f:
                json.dump(clean_test, out_f, indent=2, ensure_ascii=False)
            print(f"[OK] Wrote {target_path} (60 questions, 100.0 marks)")

            for q in clean_test['questions']:
                h = compute_question_hash(q['questionTextEn'])
                all_new_hashes[h] = {
                    "questionId": q["questionId"],
                    "testId": clean_test["testId"],
                    "categoryId": "jam_cy",
                    "topicTag": q.get("topicTag", "Chemistry")
                }

            imported_tests.append(clean_test)

    # 2. Remove old placeholder file if exists
    old_file = os.path.join(OLD_MOCK_DIR, "jam_cy_pyq_2024.json")
    if os.path.exists(old_file):
        os.remove(old_file)
        print(f"[OK] Removed old placeholder file: {old_file}")
    if os.path.exists(OLD_MOCK_DIR) and not os.listdir(OLD_MOCK_DIR):
        os.rmdir(OLD_MOCK_DIR)
        print(f"[OK] Removed empty directory: {OLD_MOCK_DIR}")

    # 3. Update manifest.json
    with open('manifest.json', 'r', encoding='utf-8') as f:
        mf = json.load(f)

    # Update category metadata
    for cat in mf.get('categories', []):
        if cat.get('id') == 'jam_cy':
            cat['title'] = "IIT JAM Chemistry (CY)"
            cat['titleEn'] = "IIT JAM Chemistry (CY)"
            cat['titleHi'] = "आईआईटी जैम रसायन विज्ञान (CY)"
            cat['subtitle'] = "Official Master PYQs (2022–2026)"
            cat['subtitleEn'] = "Official Master PYQs (2022–2026)"
            cat['subtitleHi'] = "आधिकारिक मास्टर PYQs (2022–2026)"
            cat['descriptionEn'] = "Official Master PYQs (2022–2026)"
            cat['descriptionHi'] = "आधिकारिक मास्टर PYQs (2022–2026)"
            cat['totalTests'] = 5
            cat['totalQuestions'] = 300
            print("[OK] Updated category 'jam_cy' in manifest.json")
            break

    # Remove old test entries for jam_cy
    old_test_count = len(mf.get('tests', []))
    mf['tests'] = [t for t in mf.get('tests', []) if t.get('categoryId') != 'jam_cy' and not t.get('testId', '').startswith('jam_cy')]
    removed_cnt = old_test_count - len(mf['tests'])
    print(f"[OK] Filtered out {removed_cnt} old jam_cy test entries from manifest.json")

    # Add 5 official PYQs
    for test in imported_tests:
        tid = test['testId']
        year = test['examYear']
        rel_path = f"tests/jam/jam_cy/pyq/{tid}.json"

        manifest_entry = {
            "test_id": tid,
            "testId": tid,
            "category_id": "jam_cy",
            "categoryId": "jam_cy",
            "test_type": "PYQ",
            "testType": "PYQ",
            "title": test['title'],
            "titleEn": test['titleEn'],
            "titleHi": HINDI_YEAR_TITLES.get(year, f"IIT JAM {year} रसायन विज्ञान (CY) आधिकारिक हल प्रश्न पत्र"),
            "exam_year_tag": str(year),
            "examYearTag": str(year),
            "shiftBadge": test['shiftBadge'],
            "duration_minutes": test['durationMinutes'],
            "durationMinutes": test['durationMinutes'],
            "total_questions": test['totalQuestions'],
            "totalQuestions": test['totalQuestions'],
            "positive_marks": 2.0,
            "positiveMarks": 2.0,
            "negative_marks": 0.33,
            "negativeMarks": 0.33,
            "is_free": test['isFree'],
            "isFree": test['isFree'],
            "version": 1,
            "path": rel_path,
            "filePath": rel_path,
            "file_path": rel_path,
            "json_url": CDN_BASE + rel_path,
            "cdnUrl": CDN_BASE + rel_path,
            "altCdnUrl": ALT_CDN_BASE + rel_path
        }
        mf['tests'].append(manifest_entry)
        print(f"[OK] Added manifest entry for {tid}")

    with open('manifest.json', 'w', encoding='utf-8') as f:
        json.dump(mf, f, indent=2, ensure_ascii=False)
    print("[OK] Saved manifest.json")

    # 4. Refresh seen_question_hashes.json
    with open('seen_question_hashes.json', 'r', encoding='utf-8') as f:
        seen = json.load(f)

    # Remove old hashes associated with jam_cy
    old_hash_cnt = len(seen)
    cleaned_seen = {k: v for k, v in seen.items() if not (isinstance(v, dict) and v.get('categoryId') == 'jam_cy')}
    removed_hashes = old_hash_cnt - len(cleaned_seen)
    print(f"[OK] Removed {removed_hashes} old jam_cy hashes from seen_question_hashes.json")

    # Add all 300 new hashes
    cleaned_seen.update(all_new_hashes)
    with open('seen_question_hashes.json', 'w', encoding='utf-8') as f:
        json.dump(cleaned_seen, f, indent=2, ensure_ascii=False)
    print(f"[OK] Added {len(all_new_hashes)} new jam_cy question hashes to seen_question_hashes.json (Total repo hashes: {len(cleaned_seen)})")

    print("\n=== IMPORT COMPLETED SUCCESSFULLY! ===")

if __name__ == '__main__':
    main()
