import pymupdf
import re
import json
import os
import requests
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

PDF_PATH = r'C:\Users\yedde\Downloads\Ghatnachakra_Polity_2022_English.pdf'
OUTPUT_DIR = r'D:\Android Project\prepunfold-cdn\tests\polity_pyq_1990_2022'
CACHE_FILE = r'D:\Android Project\prepunfold-cdn\scripts\translation_cache.json'

os.makedirs(OUTPUT_DIR, exist_ok=True)

trans_cache = {}
if os.path.exists(CACHE_FILE):
    try:
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            trans_cache = json.load(f)
    except:
        trans_cache = {}

def translate_batch(texts, max_workers=10):
    to_fetch = [t for t in texts if t and t not in trans_cache]

    def fetch_one(text):
        if not text:
            return text, ""
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=hi&dt=t&q={urllib.parse.quote(text)}"
        try:
            r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=8)
            if r.status_code == 200:
                res = ''.join([item[0] for item in r.json()[0]])
                return text, res
        except:
            pass
        return text, text

    if to_fetch:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            for orig, trans in executor.map(fetch_one, to_fetch):
                trans_cache[orig] = trans
        try:
            with open(CACHE_FILE, 'w', encoding='utf-8') as f:
                json.dump(trans_cache, f, ensure_ascii=False)
        except:
            pass

    return [trans_cache.get(t, t) for t in texts]

CHAPTER_CONFIGS = [
    {
        "ch_num": 1,
        "slug": "polity_pyq_t01_constitutional_development",
        "titleEn": "1. The Constitutional Development of India",
        "titleHi": "1. भारत का संवैधानिक विकास (The Constitutional Development of India)",
        "start_d": 9, "end_d": 26,
        "subtopics": [
            {"subtopicId": "sub_01_company_rule", "subtopicTitleEn": "(i) Acts Passed under East India Company Rule (1773–1853)", "subtopicTitleHi": "(i) ईस्ट इंडिया कंपनी शासन के अधिनियम (1773–1853)"},
            {"subtopicId": "sub_02_crown_rule", "subtopicTitleEn": "(ii) Acts Passed under the British Crown (1858–1947)", "subtopicTitleHi": "(ii) ब्रिटिश क्राउन के अधीन अधिनियम (1858–1947)"}
        ]
    },
    {
        "ch_num": 2,
        "slug": "polity_pyq_t02_constituent_assembly",
        "titleEn": "2. Constituent Assembly and Making of the Constitution",
        "titleHi": "2. संविधान सभा एवं संविधान निर्माण प्रक्रिया (Constituent Assembly & Making of the Constitution)",
        "start_d": 27, "end_d": 33,
        "subtopics": [
            {"subtopicId": "sub_01_formation_interim_govt", "subtopicTitleEn": "(i) Formation & Interim Government (1946)", "subtopicTitleHi": "(i) संविधान सभा का गठन एवं अंतरिम सरकार (1946)"},
            {"subtopicId": "sub_02_drafting_enactment", "subtopicTitleEn": "(ii) Drafting Committee & Enactment", "subtopicTitleHi": "(ii) प्रारूप समिति एवं संविधान का अधिनियमन"}
        ]
    },
    {
        "ch_num": 3,
        "slug": "polity_pyq_t03_articles_schedules",
        "titleEn": "3. Articles, Schedules and Parts of the Constitution",
        "titleHi": "3. संविधान के अनुच्छेद, अनुसूचियां एवं भाग (Articles, Schedules and Parts of the Constitution)",
        "start_d": 33, "end_d": 53,
        "subtopics": [
            {"subtopicId": "sub_01_important_articles", "subtopicTitleEn": "(i) Important Articles of the Constitution", "subtopicTitleHi": "(i) संविधान के महत्वपूर्ण अनुच्छेद"},
            {"subtopicId": "sub_02_schedules_of_constitution", "subtopicTitleEn": "(ii) Schedules of the Constitution", "subtopicTitleHi": "(ii) संविधान की अनुसूचियां"},
            {"subtopicId": "sub_03_parts_sources", "subtopicTitleEn": "(iii) Parts and Sources of the Constitution", "subtopicTitleHi": "(iii) संविधान के भाग एवं स्रोत"}
        ]
    },
    {
        "ch_num": 4,
        "slug": "polity_pyq_t04_the_preamble",
        "titleEn": "4. The Preamble",
        "titleHi": "4. उद्देशिका / प्रस्तावना (The Preamble)",
        "start_d": 53, "end_d": 61,
        "subtopics": [
            {"subtopicId": "sub_01_preamble_philosophy", "subtopicTitleEn": "(i) Philosophy & Key Terms of Preamble", "subtopicTitleHi": "(i) उद्देशिका के आदर्श एवं प्रमुख शब्दावली"},
            {"subtopicId": "sub_02_preamble_cases_amendments", "subtopicTitleEn": "(ii) Landmark Judgments & 42nd Amendment", "subtopicTitleHi": "(ii) प्रमुख वाद एवं 42वां संविधान संशोधन"}
        ]
    },
    {
        "ch_num": 5,
        "slug": "polity_pyq_t05_the_governance_system",
        "titleEn": "5. The Governance System",
        "titleHi": "5. शासन प्रणाली (The Governance System)",
        "start_d": 61, "end_d": 73,
        "subtopics": [
            {"subtopicId": "sub_01_nature_of_state", "subtopicTitleEn": "(i) Nature of State & Federal Features", "subtopicTitleHi": "(i) शासन प्रणाली की प्रकृति एवं संघीय लक्षण"},
            {"subtopicId": "sub_02_parliamentary_democracy", "subtopicTitleEn": "(ii) Parliamentary System & Separation of Powers", "subtopicTitleHi": "(ii) संसदीय व्यवस्था एवं शक्ति पृथक्करण"}
        ]
    },
    {
        "ch_num": 6,
        "slug": "polity_pyq_t06_national_symbols",
        "titleEn": "6. National Symbols",
        "titleHi": "6. राष्ट्रीय प्रतीक (National Symbols)",
        "start_d": 73, "end_d": 75,
        "subtopics": [
            {"subtopicId": "sub_01_national_symbols", "subtopicTitleEn": "(i) National Flag, Emblem, Anthem & Song", "subtopicTitleHi": "(i) राष्ट्रीय ध्वज, प्रतीक, गान एवं गीत"}
        ]
    },
    {
        "ch_num": 7,
        "slug": "polity_pyq_t07_state_and_union_territories",
        "titleEn": "7. State and the Union Territories",
        "titleHi": "7. राज्य एवं संघ राज्य क्षेत्र (State and the Union Territories)",
        "start_d": 75, "end_d": 84,
        "subtopics": [
            {"subtopicId": "sub_01_reorganization_art1_4", "subtopicTitleEn": "(i) Formation & Reorganization of States (Art. 1–4)", "subtopicTitleHi": "(i) नए राज्यों का प्रवेश, गठन एवं पुनर्गठन (अनुच्छेद 1–4)"},
            {"subtopicId": "sub_02_ut_administration", "subtopicTitleEn": "(ii) Union Territories Administration", "subtopicTitleHi": "(ii) संघ राज्य क्षेत्रों का प्रशासन"}
        ]
    },
    {
        "ch_num": 8,
        "slug": "polity_pyq_t08_the_citizenship",
        "titleEn": "8. The Citizenship",
        "titleHi": "8. नागरिकता (The Citizenship)",
        "start_d": 84, "end_d": 87,
        "subtopics": [
            {"subtopicId": "sub_01_citizenship_articles_act", "subtopicTitleEn": "(i) Constitutional Provisions & Citizenship Act", "subtopicTitleHi": "(i) संवैधानिक प्रावधान एवं नागरिकता अधिनियम"}
        ]
    },
    {
        "ch_num": 9,
        "slug": "polity_pyq_t09_fundamental_rights",
        "titleEn": "9. Fundamental Rights",
        "titleHi": "9. मूल अधिकार (Fundamental Rights)",
        "start_d": 87, "end_d": 113,
        "subtopics": [
            {"subtopicId": "sub_01_equality_freedom", "subtopicTitleEn": "(i) Right to Equality & Freedom (Art. 14–22)", "subtopicTitleHi": "(i) समानता एवं स्वतंत्रता का अधिकार (अनुच्छेद 14–22)"},
            {"subtopicId": "sub_02_exploitation_religion", "subtopicTitleEn": "(ii) Right against Exploitation & Religious Freedom (Art. 23–28)", "subtopicTitleHi": "(ii) शोषण के विरुद्ध एवं धार्मिक स्वतंत्रता का अधिकार (अनुच्छेद 23–28)"},
            {"subtopicId": "sub_03_cultural_remedies_writs", "subtopicTitleEn": "(iii) Cultural Rights, Remedies & Writs (Art. 29–32)", "subtopicTitleHi": "(iii) संस्कृति, शिक्षा एवं संवैधानिक उपचारों का अधिकार (अनुच्छेद 29–32)"}
        ]
    },
    {
        "ch_num": 10,
        "slug": "polity_pyq_t10_directive_principles",
        "titleEn": "10. Directive Principles of State Policy",
        "titleHi": "10. राज्य के नीति निदेशक तत्व (Directive Principles of State Policy)",
        "start_d": 113, "end_d": 123,
        "subtopics": [
            {"subtopicId": "sub_01_dpsp_articles_principles", "subtopicTitleEn": "(i) Social, Economic & Gandhian Principles (Art. 36–51)", "subtopicTitleHi": "(i) सामाजिक, आर्थिक एवं गांधीवादी सिद्धांत (अनुच्छेद 36–51)"},
            {"subtopicId": "sub_02_dpsp_implementation_fr", "subtopicTitleEn": "(ii) Implementation & Interrelation with Fundamental Rights", "subtopicTitleHi": "(ii) क्रियान्वयन एवं मूल अधिकारों से अंतर्संबंध"}
        ]
    },
    {
        "ch_num": 11,
        "slug": "polity_pyq_t11_fundamental_duties",
        "titleEn": "11. Fundamental Duties",
        "titleHi": "11. मूल कर्तव्य (Fundamental Duties)",
        "start_d": 123, "end_d": 129,
        "subtopics": [
            {"subtopicId": "sub_01_swaran_singh_art51a", "subtopicTitleEn": "(i) Article 51A & Swaran Singh Committee", "subtopicTitleHi": "(i) अनुच्छेद 51A एवं स्वर्ण सिंह समिति"}
        ]
    },
    {
        "ch_num": 12,
        "slug": "polity_pyq_t12_the_president",
        "titleEn": "12. The President",
        "titleHi": "12. राष्ट्रपति (The President)",
        "start_d": 129, "end_d": 150,
        "subtopics": [
            {"subtopicId": "sub_01_election_qualifications", "subtopicTitleEn": "(i) Election, Qualifications, Oath & Impeachment", "subtopicTitleHi": "(i) निर्वाचन, अर्हताएं, शपथ एवं महाभियोग"},
            {"subtopicId": "sub_02_powers_ordinance_pardon", "subtopicTitleEn": "(ii) Powers, Ordinance & Pardoning Prerogatives", "subtopicTitleHi": "(ii) शक्तियां, अध्यादेश एवं क्षमादान की शक्तियां"}
        ]
    },
    {
        "ch_num": 13,
        "slug": "polity_pyq_t13_the_vice_president",
        "titleEn": "13. The Vice-President",
        "titleHi": "13. उपराष्ट्रपति (The Vice-President)",
        "start_d": 150, "end_d": 153,
        "subtopics": [
            {"subtopicId": "sub_01_vp_election_powers", "subtopicTitleEn": "(i) Election, Removal & Chairman of Rajya Sabha", "subtopicTitleHi": "(i) निर्वाचन, पदमुक्ति एवं राज्यसभा सभापति के रूप में कार्य"}
        ]
    },
    {
        "ch_num": 14,
        "slug": "polity_pyq_t14_the_council_of_ministers",
        "titleEn": "14. The Council of Ministers",
        "titleHi": "14. केंद्रीय मंत्रिपरिषद (The Council of Ministers)",
        "start_d": 153, "end_d": 166,
        "subtopics": [
            {"subtopicId": "sub_01_pm_appointment_role", "subtopicTitleEn": "(i) Prime Minister Appointment & Executive Powers", "subtopicTitleHi": "(i) प्रधानमंत्री की नियुक्ति एवं कार्यकारी शक्तियां"},
            {"subtopicId": "sub_02_collective_responsibility", "subtopicTitleEn": "(ii) Collective Responsibility & Cabinet Functioning", "subtopicTitleHi": "(ii) सामूहिक उत्तरदायित्व एवं मंत्रिमंडल कार्यप्रणाली"}
        ]
    },
    {
        "ch_num": 15,
        "slug": "polity_pyq_t15_attorney_general_and_cag",
        "titleEn": "15. The Attorney General and the C.A.G.",
        "titleHi": "15. महान्यायवादी एवं नियंत्रक-महालेखापरीक्षक (The Attorney General and the C.A.G.)",
        "start_d": 166, "end_d": 174,
        "subtopics": [
            {"subtopicId": "sub_01_attorney_general_solicitor", "subtopicTitleEn": "(i) Attorney General & Solicitor General of India", "subtopicTitleHi": "(i) भारत का महान्यायवादी एवं सॉलिसिटर जनरल"},
            {"subtopicId": "sub_02_cag_audit_duties", "subtopicTitleEn": "(ii) Comptroller & Auditor General (CAG) Duties", "subtopicTitleHi": "(ii) नियंत्रक एवं महालेखापरीक्षक (CAG) के कर्तव्य एवं अधिकार"}
        ]
    },
    {
        "ch_num": 16,
        "slug": "polity_pyq_t16_order_of_precedence",
        "titleEn": "16. Order of Precedence",
        "titleHi": "16. वरीयता अनुक्रम (Order of Precedence)",
        "start_d": 174, "end_d": 175,
        "subtopics": [
            {"subtopicId": "sub_01_precedence_hierarchy", "subtopicTitleEn": "(i) Official Warrant of Precedence", "subtopicTitleHi": "(i) भारत का आधिकारिक वरीयता अनुक्रम"}
        ]
    },
    {
        "ch_num": 17,
        "slug": "polity_pyq_t17_the_parliament_1",
        "titleEn": "17. The Parliament (1) — Lok Sabha",
        "titleHi": "17. संसद (भाग 1 - लोकसभा) (The Parliament 1 — Lok Sabha)",
        "start_d": 175, "end_d": 191,
        "subtopics": [
            {"subtopicId": "sub_01_lok_sabha_composition", "subtopicTitleEn": "(i) Lok Sabha Composition & Delimitation", "subtopicTitleHi": "(i) लोकसभा संरचना एवं परिसीमन"},
            {"subtopicId": "sub_02_speaker_officers", "subtopicTitleEn": "(ii) Speaker, Deputy Speaker & Presiding Officers", "subtopicTitleHi": "(ii) अध्यक्ष, उपाध्यक्ष एवं पीठासीन अधिकारी"}
        ]
    },
    {
        "ch_num": 18,
        "slug": "polity_pyq_t18_the_parliament_2",
        "titleEn": "18. The Parliament (2) — Rajya Sabha",
        "titleHi": "18. संसद (भाग 2 - राज्यसभा) (The Parliament 2 — Rajya Sabha)",
        "start_d": 192, "end_d": 200,
        "subtopics": [
            {"subtopicId": "sub_01_rajya_sabha_composition", "subtopicTitleEn": "(i) Rajya Sabha Composition & Duration", "subtopicTitleHi": "(i) राज्यसभा संरचना एवं कार्यकाल"},
            {"subtopicId": "sub_02_rajya_sabha_special_powers", "subtopicTitleEn": "(ii) Exclusive Powers of Rajya Sabha (Art. 249, 312)", "subtopicTitleHi": "(ii) राज्यसभा की अनन्य शक्तियां (अनुच्छेद 249, 312)"}
        ]
    },
    {
        "ch_num": 19,
        "slug": "polity_pyq_t19_the_parliament_3",
        "titleEn": "19. The Parliament (3) — Legislative Procedures & Budget",
        "titleHi": "19. संसद (भाग 3 - विधायी प्रक्रिया एवं बजट) (The Parliament 3 — Legislative Procedures & Budget)",
        "start_d": 201, "end_d": 231,
        "subtopics": [
            {"subtopicId": "sub_01_bills_joint_sitting", "subtopicTitleEn": "(i) Ordinary Bills, Joint Sittings & Privileges", "subtopicTitleHi": "(i) साधारण विधेयक, संयुक्त बैठक एवं विशेषाधिकार"},
            {"subtopicId": "sub_02_money_bills_budget", "subtopicTitleEn": "(ii) Money Bills, Financial Bills & Annual Budget", "subtopicTitleHi": "(ii) धन विधेयक, वित्त विधेयक एवं वार्षिक बजट"},
            {"subtopicId": "sub_03_parliamentary_motions", "subtopicTitleEn": "(iii) Parliamentary Devices, Motions & Hours", "subtopicTitleHi": "(iii) संसदीय साधन, प्रस्ताव, प्रश्नकाल एवं शून्यकाल"}
        ]
    },
    {
        "ch_num": 20,
        "slug": "polity_pyq_t20_the_parliament_4",
        "titleEn": "20. The Parliament (4) — Parliamentary Committees",
        "titleHi": "20. संसद (भाग 4 - संसदीय समितियां) (The Parliament 4 — Parliamentary Committees)",
        "start_d": 231, "end_d": 241,
        "subtopics": [
            {"subtopicId": "sub_01_financial_committees", "subtopicTitleEn": "(i) Public Accounts Committee & Estimates Committee", "subtopicTitleHi": "(i) लोक लेखा समिति एवं प्राक्कलन समिति"},
            {"subtopicId": "sub_02_departmental_committees", "subtopicTitleEn": "(ii) Departmental Standing Committees & Ad-hoc Bodies", "subtopicTitleHi": "(ii) विभागीय स्थायी समितियां एवं तदर्थ समितियां"}
        ]
    },
    {
        "ch_num": 21,
        "slug": "polity_pyq_t21_the_supreme_court",
        "titleEn": "21. The Supreme Court",
        "titleHi": "21. सर्वोच्च न्यायालय (The Supreme Court)",
        "start_d": 241, "end_d": 259,
        "subtopics": [
            {"subtopicId": "sub_01_appointment_collegium", "subtopicTitleEn": "(i) Judges Appointment, Qualifications & Collegium", "subtopicTitleHi": "(i) न्यायाधीशों की नियुक्ति, योग्यताएं एवं कॉलेजियम प्रणाली"},
            {"subtopicId": "sub_02_jurisdiction_judicial_review", "subtopicTitleEn": "(ii) Original, Appellate Jurisdiction & Judicial Review", "subtopicTitleHi": "(ii) मूल, अपीलीय क्षेत्राधिकार एवं न्यायिक पुनर्विलोकन"}
        ]
    },
    {
        "ch_num": 22,
        "slug": "polity_pyq_t22_the_governor",
        "titleEn": "22. The Governor",
        "titleHi": "22. राज्यपाल (The Governor)",
        "start_d": 259, "end_d": 267,
        "subtopics": [
            {"subtopicId": "sub_01_appointment_qualifications", "subtopicTitleEn": "(i) Appointment, Term & Executive Authority", "subtopicTitleHi": "(i) नियुक्ति, कार्यकाल एवं कार्यकारी शक्तियां"},
            {"subtopicId": "sub_02_discretionary_powers", "subtopicTitleEn": "(ii) Discretionary, Legislative & Ordinance Powers", "subtopicTitleHi": "(ii) विवेकाधीन शक्तियां, विधायी एवं अध्यादेश शक्ति"}
        ]
    },
    {
        "ch_num": 23,
        "slug": "polity_pyq_t23_the_state_legislature",
        "titleEn": "23. The State Legislature",
        "titleHi": "23. राज्य विधानमंडल (The State Legislature)",
        "start_d": 268, "end_d": 278,
        "subtopics": [
            {"subtopicId": "sub_01_vidhan_sabha_parishad", "subtopicTitleEn": "(i) Legislative Assembly (Vidhan Sabha) & Council (Vidhan Parishad)", "subtopicTitleHi": "(i) विधानसभा एवं विधान परिषद की संरचना व कार्य"},
            {"subtopicId": "sub_02_legislative_powers_privileges", "subtopicTitleEn": "(ii) Legislative Powers, Procedures & Privileges", "subtopicTitleHi": "(ii) विधायी प्रक्रियाएं, शक्तियां एवं विशेषाधिकार"}
        ]
    },
    {
        "ch_num": 24,
        "slug": "polity_pyq_t24_the_high_court",
        "titleEn": "24. The High Court",
        "titleHi": "24. उच्च न्यायालय एवं अधीनस्थ न्यायालय (The High Court)",
        "start_d": 278, "end_d": 287,
        "subtopics": [
            {"subtopicId": "sub_01_high_court_jurisdiction", "subtopicTitleEn": "(i) High Court Organization & Writ Jurisdiction (Art. 226)", "subtopicTitleHi": "(i) उच्च न्यायालय का गठन एवं रिट क्षेत्राधिकार (अनुच्छेद 226)"},
            {"subtopicId": "sub_02_subordinate_courts_tribunals", "subtopicTitleEn": "(ii) Subordinate Courts, Lok Adalats & Gram Nyayalayas", "subtopicTitleHi": "(ii) अधीनस्थ न्यायालय, लोक अदालत एवं ग्राम न्यायालय"}
        ]
    },
    {
        "ch_num": 25,
        "slug": "polity_pyq_t25_the_centre_state_relations",
        "titleEn": "25. The Centre-State Relations",
        "titleHi": "25. केंद्र-राज्य संबंध (The Centre-State Relations)",
        "start_d": 287, "end_d": 295,
        "subtopics": [
            {"subtopicId": "sub_01_legislative_admin_relations", "subtopicTitleEn": "(i) 7th Schedule & Administrative Distribution of Powers", "subtopicTitleHi": "(i) सातवीं अनुसूची एवं शक्तियों का प्रशासनिक वितरण"},
            {"subtopicId": "sub_02_interstate_commissions", "subtopicTitleEn": "(ii) Sarkaria Commission & Inter-State Council", "subtopicTitleHi": "(ii) सरकारिया आयोग एवं अंतर-राज्य परिषद"}
        ]
    },
    {
        "ch_num": 26,
        "slug": "polity_pyq_t26_emergency_provisions",
        "titleEn": "26. Emergency Provisions",
        "titleHi": "26. आपात उपबंध (Emergency Provisions)",
        "start_d": 295, "end_d": 301,
        "subtopics": [
            {"subtopicId": "sub_01_national_emergency", "subtopicTitleEn": "(i) National Emergency (Art. 352)", "subtopicTitleHi": "(i) राष्ट्रीय आपातकाल (अनुच्छेद 352)"},
            {"subtopicId": "sub_02_state_financial_emergency", "subtopicTitleEn": "(ii) President's Rule & Financial Emergency (Art. 356, 360)", "subtopicTitleHi": "(ii) राष्ट्रपति शासन एवं वित्तीय आपातकाल (अनुच्छेद 356, 360)"}
        ]
    },
    {
        "ch_num": 27,
        "slug": "polity_pyq_t27_the_finance_commission",
        "titleEn": "27. The Finance Commission",
        "titleHi": "27. वित्त आयोग (The Finance Commission)",
        "start_d": 301, "end_d": 306,
        "subtopics": [
            {"subtopicId": "sub_01_finance_commission_role", "subtopicTitleEn": "(i) Composition, Functions & Fiscal Devolution (Art. 280)", "subtopicTitleHi": "(i) वित्त आयोग की संरचना, कार्य एवं वित्तीय वितरण (अनुच्छेद 280)"}
        ]
    },
    {
        "ch_num": 28,
        "slug": "polity_pyq_t28_planning_commission_niti_aayog",
        "titleEn": "28. The Planning Commission / NITI Aayog",
        "titleHi": "28. योजना आयोग / नीति आयोग (The Planning Commission / NITI Aayog)",
        "start_d": 306, "end_d": 311,
        "subtopics": [
            {"subtopicId": "sub_01_niti_aayog_evolution", "subtopicTitleEn": "(i) Planning Commission to NITI Aayog & NDC", "subtopicTitleHi": "(i) योजना आयोग से नीति आयोग एवं राष्ट्रीय विकास परिषद"}
        ]
    },
    {
        "ch_num": 29,
        "slug": "polity_pyq_t29_lokpal_and_important_commissions",
        "titleEn": "29. Lokpal and Important Commissions",
        "titleHi": "29. लोकपाल एवं महत्वपूर्ण आयोग (Lokpal and Important Commissions)",
        "start_d": 311, "end_d": 324,
        "subtopics": [
            {"subtopicId": "sub_01_lokpal_lokayukta", "subtopicTitleEn": "(i) Lokpal & Lokayukta Institutions", "subtopicTitleHi": "(i) लोकपाल एवं लोकायुक्त संस्थाएं"},
            {"subtopicId": "sub_02_human_rights_commissions", "subtopicTitleEn": "(ii) NHRC, State Human Rights Commissions & CVC", "subtopicTitleHi": "(ii) राष्ट्रीय मानवाधिकार आयोग, राज्य मानवाधिकार आयोग व CVC"}
        ]
    },
    {
        "ch_num": 30,
        "slug": "polity_pyq_t30_temporary_special_provisions",
        "titleEn": "30. Temporary Special Provisions",
        "titleHi": "30. अस्थायी विशेष उपबंध (Temporary Special Provisions)",
        "start_d": 324, "end_d": 326,
        "subtopics": [
            {"subtopicId": "sub_01_article_370_371", "subtopicTitleEn": "(i) Articles 370, 371 & State Specific Provisions", "subtopicTitleHi": "(i) अनुच्छेद 370, 371 एवं राज्यों के लिए विशेष उपबंध"}
        ]
    },
    {
        "ch_num": 31,
        "slug": "polity_pyq_t31_election_commission",
        "titleEn": "31. Election Commission",
        "titleHi": "31. निर्वाचन आयोग (Election Commission)",
        "start_d": 326, "end_d": 335,
        "subtopics": [
            {"subtopicId": "sub_01_ec_powers_composition", "subtopicTitleEn": "(i) Election Commission Composition & Powers (Art. 324)", "subtopicTitleHi": "(i) निर्वाचन आयोग की संरचना एवं अधिकार (अनुच्छेद 324)"},
            {"subtopicId": "sub_02_electoral_reforms_voting", "subtopicTitleEn": "(ii) Electoral Reforms, Model Code of Conduct & EVMs", "subtopicTitleHi": "(ii) चुनाव सुधार, आदर्श आचार संहिता एवं ईवीएम"}
        ]
    },
    {
        "ch_num": 32,
        "slug": "polity_pyq_t32_political_parties",
        "titleEn": "32. Political Parties",
        "titleHi": "32. राजनीतिक दल (Political Parties)",
        "start_d": 336, "end_d": 344,
        "subtopics": [
            {"subtopicId": "sub_01_party_system_recognition", "subtopicTitleEn": "(i) National & State Party Recognition Criteria", "subtopicTitleHi": "(i) राष्ट्रीय एवं राज्य स्तरीय राजनीतिक दलों की मान्यता"},
            {"subtopicId": "sub_02_anti_defection_law", "subtopicTitleEn": "(ii) Anti-Defection Law (10th Schedule)", "subtopicTitleHi": "(ii) दलबदल विरोधी कानून (10वीं अनुसूची)"}
        ]
    },
    {
        "ch_num": 33,
        "slug": "polity_pyq_t33_constitutional_amendments",
        "titleEn": "33. Constitutional Amendments",
        "titleHi": "33. संविधान संशोधन (Constitutional Amendments)",
        "start_d": 345, "end_d": 356,
        "subtopics": [
            {"subtopicId": "sub_01_amendment_procedure_art368", "subtopicTitleEn": "(i) Amendment Procedure under Article 368", "subtopicTitleHi": "(i) अनुच्छेद 368 के तहत संविधान संशोधन प्रक्रिया"},
            {"subtopicId": "sub_02_landmark_amendments", "subtopicTitleEn": "(ii) Historic & Significant Constitutional Amendments", "subtopicTitleHi": "(ii) ऐतिहासिक एवं महत्वपूर्ण संविधान संशोधन"}
        ]
    },
    {
        "ch_num": 34,
        "slug": "polity_pyq_t34_official_language",
        "titleEn": "34. Official Language",
        "titleHi": "34. राजभाषा (Official Language)",
        "start_d": 356, "end_d": 360,
        "subtopics": [
            {"subtopicId": "sub_01_official_language_provisions", "subtopicTitleEn": "(i) Part XVII, 8th Schedule & Classical Languages", "subtopicTitleHi": "(i) भाग XVII, 8वीं अनुसूची एवं शास्त्रीय भाषाएं"}
        ]
    },
    {
        "ch_num": 35,
        "slug": "polity_pyq_t35_panchayati_raj",
        "titleEn": "35. Panchayati Raj and Community Development",
        "titleHi": "35. पंचायती राज एवं सामुदायिक विकास (Panchayati Raj and Community Development)",
        "start_d": 360, "end_d": 389,
        "subtopics": [
            {"subtopicId": "sub_01_evolution_committees", "subtopicTitleEn": "(i) Balwant Rai Mehta & Panchayati Raj Committees", "subtopicTitleHi": "(i) बलवंत राय मेहता एवं पंचायती राज समितियां"},
            {"subtopicId": "sub_02_73rd_amendment", "subtopicTitleEn": "(ii) 73rd Constitutional Amendment Act (Rural Governance)", "subtopicTitleHi": "(ii) 73वां संविधान संशोधन अधिनियम (ग्रामीण स्वशासन)"},
            {"subtopicId": "sub_03_74th_amendment", "subtopicTitleEn": "(iii) 74th Constitutional Amendment Act (Urban Governance)", "subtopicTitleHi": "(iii) 74वां संविधान संशोधन अधिनियम (शहरी स्वशासन)"}
        ]
    },
    {
        "ch_num": 36,
        "slug": "polity_pyq_t36_special_provisions_certain_classes",
        "titleEn": "36. Special Provision for Certain Classes",
        "titleHi": "36. कुछ वर्गों के लिए विशेष उपबंध (Special Provision for Certain Classes)",
        "start_d": 389, "end_d": 395,
        "subtopics": [
            {"subtopicId": "sub_01_sc_st_obc_commissions", "subtopicTitleEn": "(i) SC/ST/OBC Commissions & Anglo-Indian Safeguards", "subtopicTitleHi": "(i) अनुसूचित जाति/जनजाति/पिछड़ा वर्ग आयोग एवं विशेष प्रावधान"}
        ]
    },
    {
        "ch_num": 37,
        "slug": "polity_pyq_t37_miscellaneous",
        "titleEn": "37. Miscellaneous",
        "titleHi": "37. विविध (Miscellaneous)",
        "start_d": 396, "end_d": 424,
        "subtopics": [
            {"subtopicId": "sub_01_constitutional_doctrines", "subtopicTitleEn": "(i) Constitutional Doctrines, Conventions & Practices", "subtopicTitleHi": "(i) संवैधानिक सिद्धांत, परंपराएं एवं कार्यप्रणालियां"},
            {"subtopicId": "sub_02_pil_tribunals_governance", "subtopicTitleEn": "(ii) Public Interest Litigation (PIL), Tribunals & Governance", "subtopicTitleHi": "(ii) जनहित याचिका (PIL), अधिकरण एवं सुशासन"}
        ]
    }
]

def process_all_chapters():
    doc = pymupdf.open(PDF_PATH)
    total_chapters = len(CHAPTER_CONFIGS)
    manifest_items = []

    print(f"=== Starting extraction of all {total_chapters} Polity chapters ===")

    for cfg in CHAPTER_CONFIGS:
        ch_num = cfg["ch_num"]
        slug = cfg["slug"]
        title_en = cfg["titleEn"]
        title_hi = cfg["titleHi"]
        start_d = cfg["start_d"]
        end_d = cfg["end_d"]
        subtopics = cfg["subtopics"]

        out_file = os.path.join(OUTPUT_DIR, f"{slug}.json")
        if os.path.exists(out_file) and ch_num == 1:
            print(f"Ch {ch_num:02d} ({slug}) already exists. Reading metadata...")
            with open(out_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            manifest_items.append({
                "test_id": slug, "testId": slug,
                "category_id": "polity_pyq_1990_2022", "categoryId": "polity_pyq_1990_2022",
                "test_type": "TOPIC_TEST", "testType": "TOPIC_TEST",
                "title": data["titleEn"], "titleEn": data["titleEn"], "titleHi": data["titleHi"],
                "exam_year_tag": "State PSC & UPSC PYQ (1990–2021)",
                "duration_minutes": data["durationMinutes"], "durationMinutes": data["durationMinutes"],
                "total_questions": data["totalQuestions"], "totalQuestions": data["totalQuestions"],
                "positive_marks": 2.0, "positiveMarks": 2.0,
                "negative_marks": 0.66, "negativeMarks": 0.66,
                "is_free": True, "isFree": True, "version": 1,
                "path": f"tests/polity_pyq_1990_2022/{slug}.json",
                "json_url": f"https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/tests/polity_pyq_1990_2022/{slug}.json",
                "cdnUrl": f"https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/tests/polity_pyq_1990_2022/{slug}.json",
                "altCdnUrl": f"https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main/tests/polity_pyq_1990_2022/{slug}.json"
            })
            continue

        p_start = start_d - 5
        p_end = min(len(doc), end_d - 4)

        lines = []
        for p in range(p_start, p_end):
            for line in doc[p].get_text().split('\n'):
                s = line.strip()
                if s.startswith('Join− https://t.me') or s.startswith('D–') or s == 'General Studies' or s == 'Indian Polity and Governance':
                    continue
                lines.append(line)
        full_text = '\n'.join(lines)

        expected = 1
        pos = 0
        found_qs = []
        while True:
            m = re.search(r'\n\s*' + str(expected) + r'\s*\.\s+', full_text[pos:])
            if not m:
                break
            q_start = pos + m.start()
            found_qs.append((expected, q_start))
            pos = q_start + len(m.group())
            expected += 1

        raw_questions = []
        for i in range(len(found_qs)):
            num, start = found_qs[i]
            end = found_qs[i+1][1] if i + 1 < len(found_qs) else len(full_text)
            block = full_text[start:end]
            clean = re.sub(r'^\n?\s*' + str(num) + r'\s*\.\s*', '', block).strip()

            m_ans = re.search(r'\nAns\.\s*\(([a-eA-E\*])\)', clean)
            if not m_ans:
                continue
            correct_opt = m_ans.group(1).upper()
            if correct_opt == '*':
                correct_opt = 'A'
            pre_ans = clean[:m_ans.start()].strip()
            explanation = clean[m_ans.end():].strip()

            opt_matches = list(re.finditer(r'(?:^|\n|\s)\(([a-dA-D])\)\s*', pre_ans))
            filtered_opts = []
            expected_letter = 'a'
            for m in opt_matches:
                if m.group(1).lower() == expected_letter:
                    filtered_opts.append(m)
                    expected_letter = chr(ord(expected_letter) + 1)
                    if expected_letter > 'd':
                        break

            if len(filtered_opts) == 4:
                q_text = pre_ans[:filtered_opts[0].start()].strip()
                options = []
                for j in range(4):
                    opt_s = filtered_opts[j].end()
                    opt_e = filtered_opts[j+1].start() if j + 1 < 4 else len(pre_ans)
                    options.append(pre_ans[opt_s:opt_e].strip())

                d_lines = options[3].split('\n')
                exam_tag = ""
                actual_d_lines = []
                for l in d_lines:
                    ls = l.strip()
                    if re.search(r'(P\.C\.S|I\.A\.S|U\.P|M\.P|R\.O|A\.R\.O|B\.P|R\.A\.S|Uttarakhand|Jharkhand|Chhattisgarh|PSC|Pre|Mains|\b\d{4}\b)', ls) and len(actual_d_lines) > 0:
                        exam_tag = (exam_tag + " " + ls).strip()
                    else:
                        actual_d_lines.append(l)
                options[3] = '\n'.join(actual_d_lines).strip()
                options = [re.sub(r'\s+', ' ', o).strip() for o in options]
            else:
                q_text = pre_ans
                options = ["Option A", "Option B", "Option C", "Option D"]
                exam_tag = ""

            q_text = re.sub(r'\s+', ' ', q_text).strip()
            explanation = re.sub(r'\s+', ' ', explanation).strip()
            m_yr = re.search(r'\b(19\d\d|20\d\d)\b', exam_tag)
            exam_year = int(m_yr.group(1)) if m_yr else 2022

            raw_questions.append({
                "num": num,
                "q_text": q_text,
                "options": options,
                "correct_opt": correct_opt,
                "exam_tag": exam_tag if exam_tag else "State PSC & UPSC PYQ",
                "exam_year": exam_year,
                "explanation": explanation
            })

        print(f"Extracted {len(raw_questions)} questions for Ch {ch_num:02d}: {title_en}")

        # Batch translation
        all_q_texts = [q["q_text"] for q in raw_questions]
        all_explanations = [q["explanation"] for q in raw_questions]
        all_opt_texts = []
        for q in raw_questions:
            all_opt_texts.extend(q["options"])

        trans_q_texts = translate_batch(all_q_texts)
        trans_explanations = translate_batch(all_explanations)
        trans_opt_texts = translate_batch(all_opt_texts)

        subtopic_counts = {s["subtopicId"]: 0 for s in subtopics}
        formatted_questions = []
        opt_idx_map = {"A": 0, "B": 1, "C": 2, "D": 3}

        for i, q in enumerate(raw_questions):
            q_num = q["num"]
            if len(subtopics) > 1:
                sub_idx = min(len(subtopics) - 1, int(i / len(raw_questions) * len(subtopics)))
                sub = subtopics[sub_idx]
            else:
                sub = subtopics[0]

            subtopic_counts[sub["subtopicId"]] += 1

            opts_en = q["options"]
            opts_hi = trans_opt_texts[i*4 : (i+1)*4]
            corr_letter = q["correct_opt"]
            corr_idx = opt_idx_map.get(corr_letter, 0)

            q_obj = {
                "questionId": f"{slug}_q{q_num:03d}",
                "questionNumber": q_num,
                "sectionId": sub["subtopicId"],
                "sectionTitleEn": f"{title_en} — {sub['subtopicTitleEn']}",
                "sectionTitleHi": f"{title_hi} — {sub['subtopicTitleHi']}",
                "subtopicId": sub["subtopicId"],
                "subtopicTitleEn": sub["subtopicTitleEn"],
                "subtopicTitleHi": sub["subtopicTitleHi"],
                "questionType": "MCQ",
                "positiveMarks": 2.0,
                "negativeMarks": 0.66,
                "pyqTag": q["exam_tag"],
                "examYear": q["exam_year"],
                "topicTag": f"Indian Polity: {title_en} — {sub['subtopicTitleEn']}",
                "difficulty": "MEDIUM",
                "questionTextEn": q["q_text"],
                "questionTextHi": trans_q_texts[i],
                "optionsEn": opts_en,
                "optionsHi": opts_hi,
                "correctOption": corr_letter,
                "correctOptionsList": None,
                "natMin": None,
                "natMax": None,
                "explanationEn": f"Correct Answer: ({corr_letter}). {q['explanation']}",
                "explanationHi": f"सही उत्तर: ({corr_letter}) {trans_explanations[i]}",
                "q_id": 800000 + ch_num * 1000 + q_num,
                "q_number": q_num,
                "section": f"{title_en} — {sub['subtopicTitleEn']}",
                "exam_year_tag": q["exam_tag"],
                "question_en": q["q_text"],
                "question_hi": trans_q_texts[i],
                "options_en": opts_en,
                "options_hi": opts_hi,
                "correct_index": corr_idx,
                "correct_indices": [corr_idx],
                "explanation_en": f"Correct Answer: ({corr_letter}). {q['explanation']}",
                "explanation_hi": f"सही उत्तर: ({corr_letter}) {trans_explanations[i]}"
            }
            formatted_questions.append(q_obj)

        for s in subtopics:
            s["questionCount"] = subtopic_counts[s["subtopicId"]]

        total_q = len(formatted_questions)
        doc_json = {
            "testId": slug,
            "categoryId": "polity_pyq_1990_2022",
            "partId": "part1_indian_polity_and_governance",
            "partTitleEn": "Part I: Indian Polity & Governance",
            "partTitleHi": "भाग I: भारतीय राजव्यवस्था एवं शासन",
            "topicNumber": ch_num,
            "topicTitleEn": title_en,
            "topicTitleHi": title_hi,
            "subtopics": subtopics,
            "titleEn": f"Indian Polity Topic {ch_num}: {title_en} ({total_q} PYQs | {len(subtopics)} Sub-Topics)",
            "titleHi": f"भारतीय राजव्यवस्था अध्याय {ch_num}: {title_hi} ({total_q} PYQs | {len(subtopics)} उप-विषय)",
            "subtitleEn": "Sub-Topics: " + ", ".join([s["subtopicTitleEn"] for s in subtopics]),
            "testType": "TOPIC",
            "isFree": True,
            "durationMinutes": total_q,
            "totalQuestions": total_q,
            "maxMarks": total_q * 2.0,
            "positiveMarks": 2.0,
            "negativeMarks": 0.66,
            "examYear": 2022,
            "shiftBadge": f"PYQ (1990–2021) • {len(subtopics)} Sub-Topics",
            "questions": formatted_questions
        }

        with open(out_file, 'w', encoding='utf-8') as f:
            json.dump(doc_json, f, ensure_ascii=False, indent=2)

        print(f"Generated Ch {ch_num:02d}: {out_file} ({total_q} Qs, {os.path.getsize(out_file)} bytes)")

        manifest_items.append({
            "test_id": slug, "testId": slug,
            "category_id": "polity_pyq_1990_2022", "categoryId": "polity_pyq_1990_2022",
            "test_type": "TOPIC_TEST", "testType": "TOPIC_TEST",
            "title": doc_json["titleEn"], "titleEn": doc_json["titleEn"], "titleHi": doc_json["titleHi"],
            "exam_year_tag": "State PSC & UPSC PYQ (1990–2021)",
            "duration_minutes": total_q, "durationMinutes": total_q,
            "total_questions": total_q, "totalQuestions": total_q,
            "positive_marks": 2.0, "positiveMarks": 2.0,
            "negative_marks": 0.66, "negativeMarks": 0.66,
            "is_free": True, "isFree": True, "version": 1,
            "path": f"tests/polity_pyq_1990_2022/{slug}.json",
            "json_url": f"https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/tests/polity_pyq_1990_2022/{slug}.json",
            "cdnUrl": f"https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/tests/polity_pyq_1990_2022/{slug}.json",
            "altCdnUrl": f"https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main/tests/polity_pyq_1990_2022/{slug}.json"
        })

    # Save manifest items helper
    with open(r'D:\Android Project\prepunfold-cdn\scripts\polity_manifest_entries.json', 'w', encoding='utf-8') as f:
        json.dump(manifest_items, f, ensure_ascii=False, indent=2)
    print(f"=== Complete! Generated all {len(manifest_items)} topic test files! ===")

if __name__ == "__main__":
    process_all_chapters()
