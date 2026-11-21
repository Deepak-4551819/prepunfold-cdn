import json
import os
import glob
import re
from datetime import datetime

MANIFEST_PATH = "manifest.json"
BASE_DIR = "tests/judiciary_pyq"

PARTS_DEF = [
    {
        "partId": "part1_cpc_1908",
        "subDir": "cpc",
        "titleEn": "Part I: Code of Civil Procedure, 1908",
        "titleHi": "भाग I: सिविल प्रक्रिया संहिता, 1908"
    },
    {
        "partId": "part2_crpc_1973",
        "subDir": "crpc",
        "titleEn": "Part II: Code of Criminal Procedure, 1973",
        "titleHi": "भाग II: दंड प्रक्रिया संहिता, 1973"
    },
    {
        "partId": "part3_evidence_1872",
        "subDir": "evidence",
        "titleEn": "Part III: Indian Evidence Act, 1872",
        "titleHi": "भाग III: भारतीय साक्ष्य अधिनियम, 1872"
    },
    {
        "partId": "part4_ipc_1860",
        "subDir": "ipc",
        "titleEn": "Part IV: Indian Penal Code, 1860",
        "titleHi": "भाग IV: भारतीय दंड संहिता, 1860"
    },
    {
        "partId": "part5_constitution_of_india",
        "subDir": "constitution",
        "titleEn": "Part V: Constitution of India",
        "titleHi": "भाग V: भारत का संविधान"
    },
    {
        "partId": "part6_transfer_of_property_1882",
        "subDir": "tpa",
        "titleEn": "Part VI: Transfer of Property Act, 1882",
        "titleHi": "भाग VI: संपत्ति अंतरण अधिनियम, 1882"
    },
    {
        "partId": "part7_indian_contract_act_1872",
        "subDir": "contract",
        "titleEn": "Part VII: Indian Contract Act, 1872",
        "titleHi": "भाग VII: भारतीय संविदा अधिनियम, 1872"
    },
    {
        "partId": "part8_law_of_torts",
        "subDir": "tort",
        "titleEn": "Part VIII: Law of Torts",
        "titleHi": "भाग VIII: अपकृत्य विधि (Law of Torts)"
    },
    {
        "partId": "part9_limitation_act_1963",
        "subDir": "limitation",
        "titleEn": "Part IX: Limitation Act, 1963",
        "titleHi": "भाग IX: परिसीमा अधिनियम, 1963"
    },
    {
        "partId": "part10_specific_relief_act_1963",
        "subDir": "sra",
        "titleEn": "Part X: Specific Relief Act, 1963",
        "titleHi": "भाग X: विनिर्दिष्ट अनुतोष अधिनियम, 1963"
    },
    {
        "partId": "part11_law_of_trust_and_equity",
        "subDir": "trust_equity",
        "titleEn": "Part XI: Law of Trust & Equity",
        "titleHi": "भाग XI: साम्या एवं न्यास विधि"
    },
    {
        "partId": "part12_jurisprudence",
        "subDir": "jurisprudence",
        "titleEn": "Part XII: Jurisprudence",
        "titleHi": "भाग XII: विधिशास्त्र (Jurisprudence)"
    },
    {
        "partId": "part13_international_organisations",
        "subDir": "international_org",
        "titleEn": "Part XIII: International Organisations & Current Affairs",
        "titleHi": "भाग XIII: अंतर्राष्ट्रीय संगठन एवं समसामयिक अंतर्राष्ट्रीय प्रकरण"
    },
    {
        "partId": "part14_minor_acts",
        "subDir": "minor_acts",
        "titleEn": "Part XIV: Minor Acts (9 in 1 Special)",
        "titleHi": "भाग XIV: लघु अधिनियम (Minor Acts)"
    }
]

def update_manifest():
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    all_test_entries = []
    parts_summary = []
    total_judiciary_questions = 0

    for part_info in PARTS_DEF:
        p_id = part_info["partId"]
        sub_dir = part_info["subDir"]
        dir_path = os.path.join(BASE_DIR, sub_dir)

        files = sorted(glob.glob(os.path.join(dir_path, "*.json")))

        # Natural sort by topic number
        def sort_by_tnum(path):
            m = re.search(r'_t(\d+)_', os.path.basename(path))
            return int(m.group(1)) if m else 999
        files.sort(key=sort_by_tnum)

        part_qs = 0
        for fpath in files:
            with open(fpath, "r", encoding="utf-8") as fp:
                tdata = json.load(fp)

            t_id = tdata.get("testId") or os.path.splitext(os.path.basename(fpath))[0]
            qs = tdata.get("questions", [])
            q_count = len(qs)
            part_qs += q_count
            total_judiciary_questions += q_count

            dur = tdata.get("durationMinutes", max(15, int(q_count * 0.9)))
            pos_marks = tdata.get("positiveMarks", 2.0)
            neg_marks = tdata.get("negativeMarks", 0.66)
            rel_path = os.path.relpath(fpath, ".").replace("\\", "/")

            entry = {
                "test_id": t_id,
                "testId": t_id,
                "category_id": "judiciary_pyq",
                "categoryId": "judiciary_pyq",
                "partId": p_id,
                "test_type": "TOPIC_TEST",
                "testType": "TOPIC_TEST",
                "title": tdata.get("titleEn", t_id),
                "titleEn": tdata.get("titleEn", t_id),
                "titleHi": tdata.get("titleHi", t_id),
                "exam_year_tag": tdata.get("examYearTag", "Judiciary PYQ (1990–2024)"),
                "examYearTag": tdata.get("examYearTag", "Judiciary PYQ (1990–2024)"),
                "duration_minutes": dur,
                "durationMinutes": dur,
                "total_questions": q_count,
                "totalQuestions": q_count,
                "positive_marks": pos_marks,
                "positiveMarks": pos_marks,
                "negative_marks": neg_marks,
                "negativeMarks": neg_marks,
                "is_free": True,
                "isFree": True,
                "version": 1,
                "path": rel_path,
                "json_url": f"https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/{rel_path}",
                "cdnUrl": f"https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/{rel_path}",
                "altCdnUrl": f"https://cdn.jsdelivr.net/gh/Yeddesh/prepunfold-cdn@main/{rel_path}"
            }
            all_test_entries.append(entry)

        parts_summary.append({
            "partId": p_id,
            "partTitleEn": f"{part_info['titleEn']} ({len(files)} Topics • {part_qs} PYQs)",
            "partTitleHi": f"{part_info['titleHi']} ({len(files)} अध्याय • {part_qs} प्रश्न)",
            "topicCount": len(files),
            "questionCount": part_qs
        })

    judiciary_category = {
        "id": "judiciary_pyq",
        "categoryId": "judiciary_pyq",
        "title": "All-India & State Judiciary (Civil Judge Jr Div & JMFC) PYQ (1990-2024)",
        "titleEn": "All-India & State Judiciary (Civil Judge Jr Div & JMFC) PYQ (1990-2024)",
        "titleHi": "अखिल भारतीय एवं राज्य न्यायिक सेवा परीक्षा (सिविल जज जूनियर डिवीजन एवं जेएमएफसी) विगत वर्ष प्रश्न (1990-2024)",
        "subtitle": f"{len(all_test_entries)} Topic-Wise Mock Tests • 14 Law Subjects • {total_judiciary_questions} Real PYQs (1990–2024) with Detailed Bilingual Solutions",
        "descriptionEn": f"{len(all_test_entries)} Topic-Wise Mock Tests • 14 Law Subjects • {total_judiciary_questions} Real PYQs (1990–2024) with Detailed Bilingual Solutions for Maharashtra MPSC JMFC, UP, Bihar, MP, Rajasthan, Delhi, Uttarakhand, Haryana & All State Judiciary Exams.",
        "descriptionHi": f"{len(all_test_entries)} अध्यायवार मॉक टेस्ट • 14 विधि विषय • {total_judiciary_questions} वास्तविक विगत वर्ष प्रश्न (1990-2024) विस्तृत द्विभाषी व्याख्या सहित (महाराष्ट्र जेएमएफसी, यूपी, बिहार, एमपी, राजस्थान, दिल्ली एवं अन्य सभी राज्य)।",
        "is_active": True,
        "pass_6m_product_id": "pass_judiciary_pyq_6m_149",
        "pass_6m_price": "₹149",
        "pass_6m_strike_price": "₹399",
        "pass_6m_days": 180,
        "pass_1y_product_id": "pass_judiciary_pyq_1y_249",
        "pass_1y_price": "₹249",
        "pass_1y_strike_price": "₹599",
        "pass_1y_days": 365,
        "totalTests": len(all_test_entries),
        "totalQuestions": total_judiciary_questions,
        "parts": parts_summary
    }

    # Update manifest categories
    cat_exists = False
    for i, cat in enumerate(manifest.get("categories", [])):
        if cat.get("id") == "judiciary_pyq" or cat.get("categoryId") == "judiciary_pyq":
            manifest["categories"][i] = judiciary_category
            cat_exists = True
            break
    if not cat_exists:
        manifest["categories"].append(judiciary_category)

    # Update manifest tests
    existing_tests = manifest.get("tests", [])
    filtered_tests = [t for t in existing_tests if t.get("categoryId") != "judiciary_pyq" and t.get("category_id") != "judiciary_pyq"]
    filtered_tests.extend(all_test_entries)

    manifest["tests"] = filtered_tests
    manifest["total_tests"] = len(filtered_tests)
    manifest["totalTests"] = len(filtered_tests)
    manifest["totalCategories"] = len(manifest["categories"])
    manifest["manifest_version"] = manifest.get("manifest_version", 14) + 1
    manifest["lastUpdated"] = datetime.utcnow().isoformat() + "Z"
    manifest["updatedAt"] = manifest["lastUpdated"]

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print("=" * 80)
    print("MANIFEST UPDATE COMPLETE:")
    print(f"Added category 'judiciary_pyq' with {len(parts_summary)} Parts.")
    print(f"Total Judiciary Tests: {len(all_test_entries)}")
    print(f"Total Judiciary Questions: {total_judiciary_questions}")
    print(f"Overall Manifest Tests: {len(filtered_tests)}")
    print("=" * 80)

if __name__ == "__main__":
    update_manifest()
