import copy
import glob
import json
import os
import random

DIR = "tests/teaching/tgt_pgt_history"

def deduplicate_pool(pool, global_seen_stems):
    unique = []
    for q in pool:
        stem = q.get("questionTextHi", "").strip()
        if stem and stem not in global_seen_stems:
            global_seen_stems.add(stem)
            unique.append(q)
    return unique

def run():
    print("Collecting questions from 30 chapters...")
    files = sorted(glob.glob(f"{DIR}/tgt_pgt_hist_ch*.json"))

    ancient_pool = []
    medieval_pool = []
    modern_pool = []
    world_pool = []

    for fpath in files:
        fname = os.path.basename(fpath)
        ch_num = int(fname.split("_ch")[1][:2])
        with open(fpath, "r", encoding="utf-8") as fp:
            data = json.load(fp)

        qs = data.get("questions", [])
        if 1 <= ch_num <= 9:
            ancient_pool.extend(qs)
        elif 10 <= ch_num <= 15:
            medieval_pool.extend(qs)
        elif 16 <= ch_num <= 28:
            modern_pool.extend(qs)
        elif 29 <= ch_num <= 30:
            world_pool.extend(qs)

    # Deduplicate globally across all pools
    global_seen_stems = set()
    anc_unique = deduplicate_pool(ancient_pool, global_seen_stems)
    med_unique = deduplicate_pool(medieval_pool, global_seen_stems)
    mod_unique = deduplicate_pool(modern_pool, global_seen_stems)
    wor_unique = deduplicate_pool(world_pool, global_seen_stems)

    print(f"Ancient unique: {len(anc_unique)}")
    print(f"Medieval unique: {len(med_unique)}")
    print(f"Modern unique: {len(mod_unique)}")
    print(f"World/Historiography unique: {len(wor_unique)}")

    # Deterministic sampling with seed 42
    random.seed(42)

    sampled_ancient = random.sample(anc_unique, 380)
    sampled_medieval = random.sample(med_unique, 380)
    sampled_modern = random.sample(mod_unique, 400)
    sampled_world = random.sample(wor_unique, 90)

    all_sampled = sampled_ancient + sampled_medieval + sampled_modern + sampled_world
    assert len(all_sampled) == 1250, f"Expected 1250 questions, got {len(all_sampled)}"
    unique_texts = set(q["questionTextHi"] for q in all_sampled)
    assert len(unique_texts) == 1250, f"Expected 1250 unique questions, got {len(unique_texts)}"
    print(f"100% Guaranteed: Exactly 1,250 unique questions with ZERO overlap across 10 mocks!")

    SECTIONS_META = [
        {
            "subtopicId": "sec_ancient",
            "sectionId": "sec_ancient",
            "subtopicTitleEn": "Section A: Ancient Indian History",
            "sectionTitleEn": "Section A: Ancient Indian History",
            "subtopicTitleHi": "खण्ड A: प्राचीन भारतीय इतिहास",
            "sectionTitleHi": "खण्ड A: प्राचीन भारतीय इतिहास",
            "questionCount": 38
        },
        {
            "subtopicId": "sec_medieval",
            "sectionId": "sec_medieval",
            "subtopicTitleEn": "Section B: Medieval Indian History",
            "sectionTitleEn": "Section B: Medieval Indian History",
            "subtopicTitleHi": "खण्ड B: मध्यकालीन भारतीय इतिहास",
            "sectionTitleHi": "खण्ड B: मध्यकालीन भारतीय इतिहास",
            "questionCount": 38
        },
        {
            "subtopicId": "sec_modern",
            "sectionId": "sec_modern",
            "subtopicTitleEn": "Section C: Modern Indian History",
            "sectionTitleEn": "Section C: Modern Indian History",
            "subtopicTitleHi": "खण्ड C: आधुनिक भारतीय इतिहास",
            "sectionTitleHi": "खण्ड C: आधुनिक भारतीय इतिहास",
            "questionCount": 40
        },
        {
            "subtopicId": "sec_world_historiography",
            "sectionId": "sec_world_historiography",
            "subtopicTitleEn": "Section D: World History & Historiography",
            "sectionTitleEn": "Section D: World History & Historiography",
            "subtopicTitleHi": "खण्ड D: विश्व इतिहास एवं इतिहास-दर्शन",
            "sectionTitleHi": "खण्ड D: विश्व इतिहास एवं इतिहास-दर्शन",
            "questionCount": 9
        }
    ]

    mock_test_entries = []

    for m in range(1, 11):
        mock_id = f"tgt_pgt_hist_mock_{m:02d}"
        is_free = (m <= 2)

        # Slice per section
        anc_slice = sampled_ancient[(m-1)*38 : m*38]
        med_slice = sampled_medieval[(m-1)*38 : m*38]
        mod_slice = sampled_modern[(m-1)*40 : m*40]
        wor_slice = sampled_world[(m-1)*9 : m*9]

        mock_qs = []
        q_num = 1

        section_batches = [
            (SECTIONS_META[0], anc_slice),
            (SECTIONS_META[1], med_slice),
            (SECTIONS_META[2], mod_slice),
            (SECTIONS_META[3], wor_slice),
        ]

        for sec_meta, batch in section_batches:
            for raw_q in batch:
                q = copy.deepcopy(raw_q)

                # Format question
                q["questionId"] = f"{mock_id}_q{q_num:03d}"
                q["questionNumber"] = q_num
                q["sectionId"] = sec_meta["sectionId"]
                q["sectionTitleEn"] = sec_meta["sectionTitleEn"]
                q["sectionTitleHi"] = sec_meta["sectionTitleHi"]
                q["subtopicId"] = sec_meta["subtopicId"]
                q["subtopicTitleEn"] = sec_meta["subtopicTitleEn"]
                q["subtopicTitleHi"] = sec_meta["subtopicTitleHi"]
                q["questionType"] = "MCQ"
                q["positiveMarks"] = 4.0
                q["negativeMarks"] = 0.0
                q["pyqTag"] = f"UP TGT/PGT Mock {m:02d}"
                q["examYear"] = 2026
                q["topicTag"] = f"TGT/PGT History: {sec_meta['subtopicTitleEn']}"

                # Snake case fields
                q["q_id"] = 19900000 + m * 1000 + q_num
                q["q_number"] = q_num
                q["section"] = sec_meta["sectionTitleEn"]
                q["exam_year_tag"] = f"UP TGT/PGT Mock {m:02d}"
                q["question_en"] = q["questionTextEn"]
                q["question_hi"] = q["questionTextHi"]
                q["options_en"] = q["optionsEn"]
                q["options_hi"] = q["optionsHi"]

                opt_map = {"A": 0, "B": 1, "C": 2, "D": 3}
                c_idx = opt_map.get(q.get("correctOption", "A"), 0)
                q["correct_index"] = c_idx
                q["correct_indices"] = [c_idx]

                q["explanation_en"] = q.get("explanationEn", "")
                q["explanation_hi"] = q.get("explanationHi", "")
                q["question_type"] = "MCQ"
                q["q_marks"] = 4.0
                q["q_negative_marks"] = 0.0
                q["positive_marks"] = 4.0
                q["negative_marks"] = 0.0

                mock_qs.append(q)
                q_num += 1

        assert len(mock_qs) == 125, f"Mock {m} has {len(mock_qs)} questions, expected 125"

        mock_data = {
            "testId": mock_id,
            "test_id": mock_id,
            "categoryId": "tgt_pgt_history",
            "category_id": "tgt_pgt_history",
            "partId": "part0_full_length_mocks",
            "part_id": "part0_full_length_mocks",
            "partTitleEn": "Full-Length TGT/PGT History Mocks",
            "partTitleHi": "पूर्ण लंबाई TGT/PGT इतिहास मॉक टेस्ट",
            "topicNumber": m,
            "topicTitleEn": f"UP TGT/PGT History Full-Length Mock Test {m:02d} (125 Qs | 500 Marks)",
            "topicTitleHi": f"यूपी TGT/PGT इतिहास पूर्ण मॉक टेस्ट {m:02d} (125 प्रश्न | 500 अंक)",
            "title": f"UP TGT/PGT History Full-Length Mock Test {m:02d} (125 Qs | Bilingual)",
            "titleEn": f"UP TGT/PGT History Full-Length Mock Test {m:02d} (125 Qs | Bilingual)",
            "titleHi": f"यूपी TGT/PGT इतिहास पूर्ण मॉक टेस्ट {m:02d} (125 प्रश्न | द्विभाषी)",
            "testType": "MOCK",
            "test_type": "MOCK",
            "isFree": is_free,
            "is_free": is_free,
            "durationMinutes": 120,
            "duration_minutes": 120,
            "totalQuestions": 125,
            "total_questions": 125,
            "maxMarks": 500.0,
            "max_marks": 500.0,
            "positiveMarks": 4.0,
            "positive_marks": 4.0,
            "negativeMarks": 0.0,
            "negative_marks": 0.0,
            "examYearTag": "UP TGT/PGT 2026 Pattern",
            "exam_year_tag": "UP TGT/PGT 2026 Pattern",
            "shiftBadge": "Full-Length Mock • 125 Questions • Bilingual",
            "version": 1,
            "subtopics": [
                {
                    "subtopicId": s["subtopicId"],
                    "subtopicTitleEn": s["subtopicTitleEn"],
                    "subtopicTitleHi": s["subtopicTitleHi"],
                    "questionCount": s["questionCount"]
                }
                for s in SECTIONS_META
            ],
            "questions": mock_qs
        }

        mock_file_path = f"{DIR}/{mock_id}.json"
        with open(mock_file_path, "w", encoding="utf-8") as fp:
            json.dump(mock_data, fp, ensure_ascii=False, indent=2)

        print(f"Generated {mock_file_path} with 125 Qs (isFree={is_free})")

        cdn_url = f"https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/tests/teaching/tgt_pgt_history/{mock_id}.json"
        alt_cdn_url = f"https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main/tests/teaching/tgt_pgt_history/{mock_id}.json"
        rel_path = f"tests/teaching/tgt_pgt_history/{mock_id}.json"

        entry = {
            "test_id": mock_id,
            "testId": mock_id,
            "category_id": "tgt_pgt_history",
            "categoryId": "tgt_pgt_history",
            "part_id": "part0_full_length_mocks",
            "partId": "part0_full_length_mocks",
            "test_type": "MOCK",
            "testType": "MOCK",
            "title": f"UP TGT/PGT History Full-Length Mock Test {m:02d} (125 Qs | Bilingual)",
            "titleEn": f"UP TGT/PGT History Full-Length Mock Test {m:02d} (125 Qs | Bilingual)",
            "titleHi": f"यूपी TGT/PGT इतिहास पूर्ण मॉक टेस्ट {m:02d} (125 प्रश्न | द्विभाषी)",
            "exam_year_tag": "UP TGT/PGT 2026 Pattern",
            "examYearTag": "UP TGT/PGT 2026 Pattern",
            "shiftBadge": "Full-Length Mock • 125 Questions • Bilingual",
            "duration_minutes": 120,
            "durationMinutes": 120,
            "total_questions": 125,
            "totalQuestions": 125,
            "positive_marks": 4.0,
            "positiveMarks": 4.0,
            "negative_marks": 0.0,
            "negativeMarks": 0.0,
            "is_free": is_free,
            "isFree": is_free,
            "version": 1,
            "path": rel_path,
            "filePath": rel_path,
            "file_path": rel_path,
            "json_url": cdn_url,
            "cdnUrl": cdn_url,
            "altCdnUrl": alt_cdn_url
        }
        mock_test_entries.append(entry)

    # Remove obsolete mock01_full_length.json if present
    old_mock_path = f"{DIR}/tgt_pgt_hist_mock01_full_length.json"
    if os.path.exists(old_mock_path):
        os.remove(old_mock_path)
        print(f"Removed obsolete file: {old_mock_path}")

    # Update manifest_tgt_pgt_history_master.json
    master_path = "manifest_tgt_pgt_history_master.json"
    with open(master_path, "r", encoding="utf-8") as fp:
        master_data = json.load(fp)

    chapter_entries = [t for t in master_data.get("tests", []) if not t.get("testId", "").startswith("tgt_pgt_hist_mock")]
    all_master_tests = mock_test_entries + chapter_entries

    total_master_q = sum(t.get("totalQuestions", 0) for t in all_master_tests)
    master_data["tests"] = all_master_tests
    master_data["totalTests"] = len(all_master_tests)
    master_data["total_tests"] = len(all_master_tests)
    master_data["totalQuestions"] = total_master_q
    master_data["total_questions"] = total_master_q
    master_data["version"] = 41
    master_data["manifest_version"] = 41
    master_data["manifestVersion"] = 41

    with open(master_path, "w", encoding="utf-8") as fp:
        json.dump(master_data, fp, ensure_ascii=False, indent=2)
    print(f"Updated {master_path}: totalTests={len(all_master_tests)}, totalQuestions={total_master_q}, v41")

    # Update manifest.json
    manifest_path = "manifest.json"
    with open(manifest_path, "r", encoding="utf-8") as fp:
        manifest_data = json.load(fp)

    non_history_tests = [t for t in manifest_data.get("tests", []) if t.get("categoryId") != "tgt_pgt_history"]
    manifest_data["tests"] = non_history_tests + all_master_tests

    for cat in manifest_data.get("categories", []):
        if cat.get("categoryId") == "tgt_pgt_history":
            cat["totalTests"] = len(all_master_tests)
            cat["total_tests"] = len(all_master_tests)
            cat["totalQuestions"] = total_master_q
            cat["total_questions"] = total_master_q
            cat["subtitle"] = f"30 Chapter Topic Tests + 10 Full-Length Mocks ({total_master_q:,} Solved PYQs • Bilingual)"

    manifest_data["totalTests"] = len(manifest_data["tests"])
    manifest_data["total_tests"] = len(manifest_data["tests"])
    manifest_data["totalQuestions"] = sum(t.get("totalQuestions", 0) for t in manifest_data["tests"])
    manifest_data["total_questions"] = manifest_data["totalQuestions"]
    manifest_data["version"] = 41
    manifest_data["manifest_version"] = 41
    manifest_data["manifestVersion"] = 41

    with open(manifest_path, "w", encoding="utf-8") as fp:
        json.dump(manifest_data, fp, ensure_ascii=False, indent=2)
    print(f"Updated {manifest_path}: totalTests={manifest_data['totalTests']}, totalQuestions={manifest_data['totalQuestions']}, v41")

if __name__ == "__main__":
    run()
