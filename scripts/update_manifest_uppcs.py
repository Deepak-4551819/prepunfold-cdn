#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scripts/update_manifest_uppcs.py — Registers all 14 official UPPCS PYQs (2018-2024) in manifest.json."""
import datetime
import json
import os

PAPERS_INFO = [
    {
        "year": 2024,
        "is_gs": True,
        "tid": "uppcs_pre_pyq_2024_gs1",
        "title_en": "UPPSC PCS Prelims 2024 — General Studies Paper 1 (Full 150 Qs)",
        "title_hi": "UPPSC PCS प्रारंभिक परीक्षा 2024 — सामान्य अध्ययन प्रश्नपत्र-1 (पूर्ण 150 प्रश्न)",
        "badge": "UPPCS Prelims 2024 • GS-1 (Full 150 Qs)",
        "total": 150,
        "pos": 1.33,
        "neg": 0.44
    },
    {
        "year": 2024,
        "is_gs": False,
        "tid": "uppcs_pre_pyq_2024_csat",
        "title_en": "UPPSC PCS Prelims 2024 — CSAT Paper 2 (Full 100 Qs)",
        "title_hi": "UPPSC PCS प्रारंभिक परीक्षा 2024 — CSAT प्रश्नपत्र-2 (पूर्ण 100 प्रश्न)",
        "badge": "UPPCS Prelims 2024 • CSAT Paper-2 (Full 100 Qs)",
        "total": 100,
        "pos": 2.0,
        "neg": 0.66
    },
    {
        "year": 2023,
        "is_gs": True,
        "tid": "uppcs_pre_pyq_2023_gs1",
        "title_en": "UPPSC PCS Prelims 2023 — General Studies Paper 1 (Full 150 Qs)",
        "title_hi": "UPPSC PCS प्रारंभिक परीक्षा 2023 — सामान्य अध्ययन प्रश्नपत्र-1 (पूर्ण 150 प्रश्न)",
        "badge": "UPPCS Prelims 2023 • GS-1 (Full 150 Qs)",
        "total": 150,
        "pos": 1.33,
        "neg": 0.44
    },
    {
        "year": 2023,
        "is_gs": False,
        "tid": "uppcs_pre_pyq_2023_csat",
        "title_en": "UPPSC PCS Prelims 2023 — CSAT Paper 2 (Full 100 Qs)",
        "title_hi": "UPPSC PCS प्रारंभिक परीक्षा 2023 — CSAT प्रश्नपत्र-2 (पूर्ण 100 प्रश्न)",
        "badge": "UPPCS Prelims 2023 • CSAT Paper-2 (Full 100 Qs)",
        "total": 100,
        "pos": 2.0,
        "neg": 0.66
    },
    {
        "year": 2022,
        "is_gs": True,
        "tid": "uppcs_pre_pyq_2022_gs1",
        "title_en": "UPPSC PCS Prelims 2022 — General Studies Paper 1 (Full 150 Qs)",
        "title_hi": "UPPSC PCS प्रारंभिक परीक्षा 2022 — सामान्य अध्ययन प्रश्नपत्र-1 (पूर्ण 150 प्रश्न)",
        "badge": "UPPCS Prelims 2022 • GS-1 (Full 150 Qs)",
        "total": 150,
        "pos": 1.33,
        "neg": 0.44
    },
    {
        "year": 2022,
        "is_gs": False,
        "tid": "uppcs_pre_pyq_2022_csat",
        "title_en": "UPPSC PCS Prelims 2022 — CSAT Paper 2 (Full 100 Qs)",
        "title_hi": "UPPSC PCS प्रारंभिक परीक्षा 2022 — CSAT प्रश्नपत्र-2 (पूर्ण 100 प्रश्न)",
        "badge": "UPPCS Prelims 2022 • CSAT Paper-2 (Full 100 Qs)",
        "total": 100,
        "pos": 2.0,
        "neg": 0.66
    },
    {
        "year": 2021,
        "is_gs": True,
        "tid": "uppcs_pre_pyq_2021_gs1",
        "title_en": "UPPSC PCS Prelims 2021 — General Studies Paper 1 (Full 150 Qs)",
        "title_hi": "UPPSC PCS प्रारंभिक परीक्षा 2021 — सामान्य अध्ययन प्रश्नपत्र-1 (पूर्ण 150 प्रश्न)",
        "badge": "UPPCS Prelims 2021 • GS-1 (Full 150 Qs)",
        "total": 150,
        "pos": 1.33,
        "neg": 0.44
    },
    {
        "year": 2021,
        "is_gs": False,
        "tid": "uppcs_pre_pyq_2021_csat",
        "title_en": "UPPSC PCS Prelims 2021 — CSAT Paper 2 (Full 100 Qs)",
        "title_hi": "UPPSC PCS प्रारंभिक परीक्षा 2021 — CSAT प्रश्नपत्र-2 (पूर्ण 100 प्रश्न)",
        "badge": "UPPCS Prelims 2021 • CSAT Paper-2 (Full 100 Qs)",
        "total": 100,
        "pos": 2.0,
        "neg": 0.66
    },
    {
        "year": 2020,
        "is_gs": True,
        "tid": "uppcs_pre_pyq_2020_gs1",
        "title_en": "UPPSC PCS Prelims 2020 — General Studies Paper 1 (Full 150 Qs)",
        "title_hi": "UPPSC PCS प्रारंभिक परीक्षा 2020 — सामान्य अध्ययन प्रश्नपत्र-1 (पूर्ण 150 प्रश्न)",
        "badge": "UPPCS Prelims 2020 • GS-1 (Full 150 Qs)",
        "total": 150,
        "pos": 1.33,
        "neg": 0.44
    },
    {
        "year": 2020,
        "is_gs": False,
        "tid": "uppcs_pre_pyq_2020_csat",
        "title_en": "UPPSC PCS Prelims 2020 — CSAT Paper 2 (Full 100 Qs)",
        "title_hi": "UPPSC PCS प्रारंभिक परीक्षा 2020 — CSAT प्रश्नपत्र-2 (पूर्ण 100 प्रश्न)",
        "badge": "UPPCS Prelims 2020 • CSAT Paper-2 (Full 100 Qs)",
        "total": 100,
        "pos": 2.0,
        "neg": 0.66
    },
    {
        "year": 2019,
        "is_gs": True,
        "tid": "uppcs_pre_pyq_2019_gs1",
        "title_en": "UPPSC PCS Prelims 2019 — General Studies Paper 1 (Full 150 Qs)",
        "title_hi": "UPPSC PCS प्रारंभिक परीक्षा 2019 — सामान्य अध्ययन प्रश्नपत्र-1 (पूर्ण 150 प्रश्न)",
        "badge": "UPPCS Prelims 2019 • GS-1 (Full 150 Qs)",
        "total": 150,
        "pos": 1.33,
        "neg": 0.44
    },
    {
        "year": 2019,
        "is_gs": False,
        "tid": "uppcs_pre_pyq_2019_csat",
        "title_en": "UPPSC PCS Prelims 2019 — CSAT Paper 2 (Full 100 Qs)",
        "title_hi": "UPPSC PCS प्रारंभिक परीक्षा 2019 — CSAT प्रश्नपत्र-2 (पूर्ण 100 प्रश्न)",
        "badge": "UPPCS Prelims 2019 • CSAT Paper-2 (Full 100 Qs)",
        "total": 100,
        "pos": 2.0,
        "neg": 0.66
    },
    {
        "year": 2018,
        "is_gs": True,
        "tid": "uppcs_pre_pyq_2018_gs1",
        "title_en": "UPPSC PCS Prelims 2018 — General Studies Paper 1 (Full 150 Qs)",
        "title_hi": "UPPSC PCS प्रारंभिक परीक्षा 2018 — सामान्य अध्ययन प्रश्नपत्र-1 (पूर्ण 150 प्रश्न)",
        "badge": "UPPCS Prelims 2018 • GS-1 (Full 150 Qs)",
        "total": 150,
        "pos": 1.33,
        "neg": 0.44
    },
    {
        "year": 2018,
        "is_gs": False,
        "tid": "uppcs_pre_pyq_2018_csat",
        "title_en": "UPPSC PCS Prelims 2018 — CSAT Paper 2 (Full 100 Qs)",
        "title_hi": "UPPSC PCS प्रारंभिक परीक्षा 2018 — CSAT प्रश्नपत्र-2 (पूर्ण 100 प्रश्न)",
        "badge": "UPPSC Prelims 2018 • CSAT Paper-2 (Full 100 Qs)",
        "total": 100,
        "pos": 2.0,
        "neg": 0.66
    }
]

def update_manifest():
    manifest_path = "manifest.json"
    with open(manifest_path, "r", encoding="utf-8") as fp:
        manifest = json.load(fp)

    tests = manifest.get("tests", [])

    flawed_ids = {"uppcs_csat_pyq_2022", "uppcs_pre_pyq_2020"}
    target_ids = {p["tid"] for p in PAPERS_INFO}
    remove_ids = flawed_ids | target_ids

    kept_tests = [t for t in tests if (t.get("testId") or t.get("test_id")) not in remove_ids]

    new_uppcs_entries = []
    for info in PAPERS_INFO:
        tid = info["tid"]
        rel_path = f"tests/state_psc/uppcs_pre/pyq/{tid}.json"
        cdn_url = f"https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/{rel_path}"
        alt_cdn_url = f"https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main/{rel_path}"

        entry = {
            "test_id": tid,
            "testId": tid,
            "category_id": "uppcs_pre",
            "categoryId": "uppcs_pre",
            "test_type": "PYQ",
            "testType": "PYQ",
            "title": info["title_en"],
            "titleEn": info["title_en"],
            "titleHi": info["title_hi"],
            "exam_year_tag": info["badge"],
            "examYearTag": info["badge"],
            "duration_minutes": 120,
            "durationMinutes": 120,
            "total_questions": info["total"],
            "totalQuestions": info["total"],
            "positive_marks": info["pos"],
            "positiveMarks": info["pos"],
            "negative_marks": info["neg"],
            "negativeMarks": info["neg"],
            "is_free": True,
            "isFree": True,
            "version": 1,
            "path": rel_path,
            "json_url": cdn_url,
            "cdnUrl": cdn_url,
            "altCdnUrl": alt_cdn_url
        }
        new_uppcs_entries.append(entry)

    updated_tests = new_uppcs_entries + kept_tests
    manifest["tests"] = updated_tests

    for cat in manifest.get("categories", []):
        if (cat.get("categoryId") or cat.get("category_id") or cat.get("id")) == "uppcs_pre":
            cat["subtitle"] = "14 Official Full Shift PYQs (2018-2024 GS1 & CSAT) + Special Mock Tests"

    total_q = sum((t.get("total_questions") or t.get("totalQuestions") or 0) for t in updated_tests)
    manifest["totalTests"] = len(updated_tests)
    manifest["totalQuestions"] = total_q
    now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()
    manifest["updatedAt"] = now_iso
    manifest["lastUpdated"] = now_iso

    with open(manifest_path, "w", encoding="utf-8") as fp:
        json.dump(manifest, fp, ensure_ascii=False, indent=2)

    print(f"Manifest successfully updated: {len(updated_tests)} total tests, {total_q} total questions.")
    print(f"Registered all {len(new_uppcs_entries)} official UPPCS PYQs (2018-2024).")

if __name__ == "__main__":
    update_manifest()
