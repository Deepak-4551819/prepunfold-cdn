import json, datetime

MANIFEST_PATH = "manifest.json"

with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
    manifest = json.load(f)

categories = manifest.get("categories", [])
for c in categories:
    cid = c.get("categoryId") or c.get("id") or c.get("category_id")
    if cid == "tgt_pgt_civics":
        c.update({
            "id": "tgt_pgt_civics",
            "categoryId": "tgt_pgt_civics",
            "category_id": "tgt_pgt_civics",
            "categoryName": "TGT/PGT Civics & Political Science",
            "category_name": "TGT/PGT Civics & Political Science",
            "categoryNameHi": "टीजीटी/पीजीटी नागरिक शास्त्र एवं राजनीति विज्ञान",
            "title": "TGT / PGT Civics (नागरिक शास्त्र)",
            "titleEn": "TGT / PGT Civics & Political Science (UPSESSB, KVS, NVS, DSSSB, RPSC)",
            "titleHi": "टीजीटी / पीजीटी नागरिक शास्त्र एवं राजनीति विज्ञान",
            "subtitle": "20 Official Full PYQ Papers + 10 Subject Mock Tests (2,847 Solved Questions)",
            "descriptionEn": "20 Official Full PYQ Papers (UP PGT/TGT, UKPSC, DSSSB, RPSC, MPPSC) + 10 Subject Mock Tests • 2,847 Solved Questions with Detailed Explanations",
            "descriptionHi": "20 आधिकारिक विगत वर्ष प्रश्न-पत्र (UP PGT/TGT, UKPSC, DSSSB, RPSC, MPPSC) + 10 विषयवार मॉक टेस्ट • 2,847 हल प्रश्न विस्तृत व्याख्या सहित",
            "iconName": "account_balance",
            "is_active": True,
            "pass_6m_product_id": "pass_tgt_pgt_civics_6m_49",
            "pass_6m_price": "₹49",
            "pass_6m_strike_price": "₹149",
            "pass_6m_days": 180,
            "pass_1y_product_id": "pass_tgt_pgt_civics_1y_89",
            "pass_1y_price": "₹89",
            "pass_1y_strike_price": "₹249",
            "pass_1y_days": 365,
            "totalTests": 30,
            "totalQuestions": 2847,
            "order": 19
        })
    elif cid == "tgt_pgt_history":
        c.update({
            "id": "tgt_pgt_history",
            "categoryId": "tgt_pgt_history",
            "category_id": "tgt_pgt_history",
            "categoryName": "TGT/PGT History",
            "category_name": "TGT/PGT History",
            "categoryNameHi": "टीजीटी/पीजीटी इतिहास",
            "title": "TGT / PGT History (इतिहास)",
            "titleEn": "TGT / PGT History (UPSESSB, KVS, NVS, DSSSB, RPSC, UKPSC)",
            "titleHi": "टीजीटी / पीजीटी इतिहास",
            "subtitle": "20 Official Full PYQ Papers + 10 Subject Mock Tests (3,000 Solved Questions)",
            "descriptionEn": "20 Official Full PYQ Papers (UP PGT/TGT, UKPSC, DSSSB, RPSC, MPPSC, KVS) + 10 Subject Mock Tests • 3,000 Solved Questions with Detailed Explanations",
            "descriptionHi": "20 आधिकारिक विगत वर्ष प्रश्न-पत्र (UP PGT/TGT, UKPSC, DSSSB, RPSC, MPPSC, KVS) + 10 विषयवार मॉक टेस्ट • 3,000 हल प्रश्न विस्तृत व्याख्या सहित",
            "iconName": "menu_book",
            "is_active": True,
            "pass_6m_product_id": "pass_tgt_pgt_hist_6m_49",
            "pass_6m_price": "₹49",
            "pass_6m_strike_price": "₹149",
            "pass_6m_days": 180,
            "pass_1y_product_id": "pass_tgt_pgt_hist_1y_89",
            "pass_1y_price": "₹89",
            "pass_1y_strike_price": "₹249",
            "pass_1y_days": 365,
            "totalTests": 30,
            "totalQuestions": 3000,
            "order": 20
        })

manifest["manifest_version"] = manifest.get("manifest_version", 21) + 1
manifest["updated_at"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

with open(MANIFEST_PATH, 'w', encoding='utf-8') as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"Categories standardized in manifest.json! New manifest_version: {manifest['manifest_version']}")
