# -*- coding: utf-8 -*-
import os, json

fixes = {
    "tgt_pgt_civics_pyq_up_tgt_2016_q051": {
        "file": "tests/teaching/tgt_pgt_civics/pyq/tgt_pgt_civics_pyq_up_tgt_2016.json",
        "questionTextEn": "Where is the headquarters of UNESCO located?",
        "questionTextHi": "यूनेस्को का मुख्यालय कहाँ स्थित है?",
        "optionsEn": ["Paris", "New York", "London", "Rome"],
        "optionsHi": ["पेरिस", "न्यूयार्क", "लंदन", "रोम"]
    },
    "tgt_pgt_econ_ch22_international_economic_institutions_q087": {
        "file": "tests/teaching/tgt_pgt_economics/topic_tests/tgt_pgt_econ_ch22_international_economic_institutions.json",
        "questionTextEn": "Match the GATT rounds with their timeline (Tokyo Round 1973-79):",
        "questionTextHi": "गैट वार्ताओं के दौरों को उनकी समय-सीमा (टोक्यो दौर 1973-79) से सुमेलित कीजिए:"
    },
    "tgt_pgt_civics_pyq_dsssb_pgt_2021_s2_q055": {
        "file": "tests/teaching/tgt_pgt_civics/pyq/tgt_pgt_civics_pyq_dsssb_pgt_2021_s2.json",
        "questionTextEn": "Match the political events and constitutional developments (1936):",
        "questionTextHi": "राजनीतिक घटनाओं एवं संवैधानिक विकासों (1936) को सुमेलित कीजिए:",
        "optionsEn": ["A-3, B-2, C-1, D-4", "A-1, B-2, C-3, D-4", "A-4, B-1, C-3, D-2", "A-2, B-4, C-3, D-1"],
        "optionsHi": ["A-3, B-2, C-1, D-4", "A-1, B-2, C-3, D-4", "A-4, B-1, C-3, D-2", "A-2, B-4, C-3, D-1"]
    }
}

for qid, fix in fixes.items():
    p = fix["file"]
    with open(p, 'r', encoding='utf-8') as f:
        d = json.load(f)
    for q in d.get("questions", []):
        if q.get("questionId") == qid:
            for k, v in fix.items():
                if k != "file":
                    q[k] = v
            print(f"Fixed {qid} in {p}")
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)

print("Applied 3 fixes.")
