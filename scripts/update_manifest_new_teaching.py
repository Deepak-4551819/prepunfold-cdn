# -*- coding: utf-8 -*-
import json
import os

def update_manifest():
    with open("manifest.json", "r", encoding="utf-8") as f:
        manifest = json.load(f)

    with open("scripts/ctet_tests_meta.json", "r", encoding="utf-8") as f:
        ctet_meta = json.load(f)

    with open("scripts/emrs_tests_meta.json", "r", encoding="utf-8") as f:
        emrs_meta = json.load(f)

    # 1. Define the 2 new categories
    ctet_cat = {
        "id": "ctet_state_tet_hindi",
        "categoryId": "ctet_state_tet_hindi",
        "title": "CTET & State TET (Hindi)",
        "titleEn": "CTET & All State TET Hindi (Class I-V & VI-VIII)",
        "titleHi": "सीटीईटी एवं सभी राज्य टीईटी हिन्दी भाषा एवं शिक्षाशास्त्र (कक्षा 1-5 व 6-8)",
        "subtitle": "21 Chapter Solved Papers • 3,353 Solved Questions • CTET, UPTET, REET, MPTET, HTET, BTET",
        "descriptionEn": "Complete CTET & All State TET Hindi: 21 Chapter-Wise Solved Topic Tests covering Hindi Grammar, Literature, Language Pedagogy & Reading Comprehension • 3,353 Solved Questions with authentic explanations.",
        "descriptionHi": "सीटीईटी एवं राज्य टीईटी हिन्दी: 21 अध्यायवार टॉपिक टेस्ट (हिन्दी व्याकरण, साहित्य, भाषा शिक्षणशास्त्र एवं अपठित गद्यांश) • 3,353 व्याख्या सहित हल प्रश्न।",
        "is_active": True,
        "pass_6m_product_id": "pass_ctet_tet_hindi_6m_49",
        "pass_6m_price": "₹49",
        "pass_6m_strike_price": "₹149",
        "pass_6m_days": 180,
        "pass_1y_product_id": "pass_ctet_tet_hindi_1y_89",
        "pass_1y_price": "₹89",
        "pass_1y_strike_price": "₹249",
        "pass_1y_days": 365,
        "totalTests": len(ctet_meta),
        "totalQuestions": sum(t["totalQuestions"] for t in ctet_meta),
        "exam_group": "teaching",
        "examGroup": "teaching",
        "unlocks_categories": [
            "ctet_state_tet_hindi"
        ],
        "pass_6m_sku": "tier_49",
        "pass_1y_sku": "tier_89",
        "parts": [
            {
                "partId": "hindi_grammar_literature",
                "partTitleEn": "Unit 1: Hindi Grammar & Literature",
                "partTitleHi": "इकाई 1: हिन्दी व्याकरण एवं साहित्य",
                "order": 1,
                "topicCount": 11,
                "questionCount": 888
            },
            {
                "partId": "hindi_pedagogy",
                "partTitleEn": "Unit 2: Hindi Pedagogy & Teaching Methodology",
                "partTitleHi": "इकाई 2: भाषा शिक्षणशास्त्र एवं शिक्षाशास्त्र",
                "order": 2,
                "topicCount": 9,
                "questionCount": 1765
            },
            {
                "partId": "reading_comprehension",
                "partTitleEn": "Unit 3: Reading Comprehension & Passages",
                "partTitleHi": "इकाई 3: अपठित अनुच्छेद एवं गद्यांश",
                "order": 3,
                "topicCount": 1,
                "questionCount": 700
            }
        ]
    }

    emrs_cat = {
        "id": "emrs_general_hindi",
        "categoryId": "emrs_general_hindi",
        "title": "EMRS Special General Hindi",
        "titleEn": "EMRS Special General Hindi (Teaching & Non-Teaching)",
        "titleHi": "ईएमआरएस विशेष सामान्य हिन्दी (शिक्षक एवं गैर-शिक्षक भर्ती)",
        "subtitle": "25 Chapter Solved Papers • 2,175 Solved Questions • EMRS, KVS, NVS, DSSSB",
        "descriptionEn": "EMRS Special General Hindi: 25 Chapter-Wise Solved Topic Tests covering Hindi Grammar, Vocabulary, Poetics, Literature & Comprehension for EMRS, KVS, NVS & DSSSB exams • 2,175 Solved Questions.",
        "descriptionHi": "ईएमआरएस विशेष सामान्य हिन्दी: 25 अध्यायवार टॉपिक टेस्ट (व्याकरण, शब्द विचार, काव्यशास्त्र, साहित्य व अपठित गद्यांश) • 2,175 व्याख्या सहित हल प्रश्न।",
        "is_active": True,
        "pass_6m_product_id": "pass_emrs_hindi_6m_49",
        "pass_6m_price": "₹49",
        "pass_6m_strike_price": "₹149",
        "pass_6m_days": 180,
        "pass_1y_product_id": "pass_emrs_hindi_1y_89",
        "pass_1y_price": "₹89",
        "pass_1y_strike_price": "₹249",
        "pass_1y_days": 365,
        "totalTests": len(emrs_meta),
        "totalQuestions": sum(t["totalQuestions"] for t in emrs_meta),
        "exam_group": "teaching",
        "examGroup": "teaching",
        "unlocks_categories": [
            "emrs_general_hindi"
        ],
        "pass_6m_sku": "tier_49",
        "pass_1y_sku": "tier_89",
        "parts": [
            {
                "partId": "emrs_grammar",
                "partTitleEn": "Unit 1: Hindi Grammar & Sentence Structure",
                "partTitleHi": "इकाई 1: हिन्दी व्याकरण एवं वाक्य विचार",
                "order": 1,
                "topicCount": 13,
                "questionCount": 757
            },
            {
                "partId": "emrs_vocab",
                "partTitleEn": "Unit 2: Vocabulary & Word Power",
                "partTitleHi": "इकाई 2: शब्द संपदा एवं शब्दावली",
                "order": 2,
                "topicCount": 7,
                "questionCount": 815
            },
            {
                "partId": "emrs_literature_comprehension",
                "partTitleEn": "Unit 3: Literature, Poetics & Comprehension",
                "partTitleHi": "इकाई 3: काव्यशास्त्र, साहित्य एवं अपठित गद्यांश",
                "order": 3,
                "topicCount": 5,
                "questionCount": 603
            }
        ]
    }

    # Remove existing if any
    manifest["categories"] = [c for c in manifest["categories"] if c["id"] not in ["ctet_state_tet_hindi", "emrs_general_hindi"]]
    manifest["categories"].append(ctet_cat)
    manifest["categories"].append(emrs_cat)

    # Filter out existing test ids from manifest["tests"]
    new_test_ids = {t["test_id"] for t in ctet_meta} | {t["test_id"] for t in emrs_meta}
    existing_tests = [t for t in manifest.get("tests", []) if t.get("test_id") not in new_test_ids and t.get("testId") not in new_test_ids]

    # Append new tests
    updated_tests = existing_tests + ctet_meta + emrs_meta
    manifest["tests"] = updated_tests

    # Update metadata totals
    new_version = 33
    manifest["manifest_version"] = new_version
    manifest["manifestVersion"] = new_version
    manifest["version"] = new_version
    manifest["schemaVersion"] = new_version
    manifest["totalCategories"] = len(manifest["categories"])
    manifest["totalTests"] = len(manifest["tests"])
    manifest["total_tests"] = len(manifest["tests"])
    manifest["totalQuestions"] = sum(t.get("totalQuestions", 0) for t in manifest["tests"])

    with open("manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"Manifest successfully updated to v{new_version}!")
    print(f"Total categories: {len(manifest['categories'])}")
    print(f"Total tests: {len(manifest['tests'])}")
    print(f"Total questions: {manifest['totalQuestions']}")

if __name__ == "__main__":
    update_manifest()
