import glob
import json
import os
import re

DIR = "tests/teaching/tgt_pgt_history"

PASS2_HINDI_REPLACEMENTS = [
    # Top KrutiDev words & frequent terms
    ("काँ«ोस", "काँग्रेस"),
    ("काँग्रेेस", "काँग्रेस"),
    ("ब्रÿणों", "ब्राह्मणों"),
    ("ब्रÿण", "ब्राह्मण"),
    ("ब्रÿाr", "ब्राह्मी"),
    ("ब्रÿगुप्त", "ब्रह्मगुप्त"),
    ("ब्रÿा", "ब्रह्मा"),
    ("ब्रÿ", "ब्रह्म"),
    ("नेह्¤", "नेहरू"),
    ("Âस्थिकोण", "दृष्टिकोण"),
    ("Âस्थि", "दृष्टि"),
    ("Âषि्ट", "दृष्टि"),
    ("सुÂढ़", "सुदृढ़"),
    ("Âढ़", "दृढ़"),
    ("Âश्य", "दृश्य"),
    ("Âश्यों", "दृश्यों"),
    ("क्ुतुबुöीन", "कुतुबुद्दीन"),
    ("निजामुöीन", "निजामुद्दीन"),
    ("गियासुöीन", "गियासुद्दीन"),
    ("जलालुöीन", "जलालुद्दीन"),
    ("जियाउöीन", "जियाउद्दीन"),
    ("बहउöीन", "बहाउद्दीन"),
    ("गयासुöीन", "गयासुद्दीन"),
    ("नासिरुöीन", "नासिरुद्दीन"),
    ("नासिरूöीन", "नासिरुद्दीन"),
    ("बद्रुöीन", "बद्रुद्दीन"),
    ("मुईनुöीन", "मुईनुद्दीन"),
    ("मुइनुöीन", "मुईनुद्दीन"),
    ("शिहबुöीन", "शहाबुद्दीन"),
    ("उöेश्य", "उद्देश्य"),
    ("गöी", "गद्दी"),
    ("रö", "रद्द"),
    ("मुöे", "मुद्दे"),
    ("विÅासागर", "विद्यासागर"),
    ("विÅापीठ", "विद्यापीठ"),
    ("विÅा", "विद्या"),
    ("विÅमान", "विद्यमान"),
    ("औÅोगिक", "औद्योगिक"),
    ("उÅोगों", "उद्योगों"),
    ("उÅोग", "उद्योग"),
    ("उÅान", "उद्यान"),
    ("प्रौÅोगिकी", "प्रौद्योगिकी"),
    ("यÅपि", "यद्यपि"),
    ("Åोतक", "द्योतक"),
    ("वाÅ", "वाद्य"),
    ("ngceeÙetB", "हुमायूँ"),
    ("Ûeesue", "चोल"),
    ("Ûeešj", "चार्टर"),
    ("Ûeej", "चार"),
    ("Ûeš&", "चर्ट"),
    ("Ûeeboer", "चांदी"),
    ("ÛeeBoer", "चांदी"),
    ("Ûeewकाsj", "चौकोर"),
    ("Ûevntoड़es", "चन्हुदड़ो"),
    ("Ûebntoड़eW", "चन्हुदड़ों"),
    ("DeefOeefveÙece", "अधिनियम"),
    ("njoÙeeue", "हरदयाल"),
    ("JeuueYeeÛeeÙe", "वल्लभाचार्य"),
    ("विलिÙece", "विलियम"),
    ("oòe", "दत्त"),
    ("सैÙयद", "सैयद"),
    ("रैÙयतवाड़ी", "रैयतवाड़ी"),
    ("अÙयर", "अय्यर"),
    ("jजिÙee", "रजिया"),
    ("Ùegद्ध", "युद्ध"),
    ("काbmÙe", "कांस्य"),
    ("ßeeruebका", "श्रीलंका"),
    ("ÙeJe", "यव"),
    ("kegâuueer", "कुल्ली"),
    ("काÙeथा", "कायथा"),
    ("cetति&ÙeeW", "मूर्तियों"),
    ("ह्र्ष", "हर्ष"),
    ("क््रष्ण", "कृष्ण"),
    ("क््रषक", "कृषक"),
    ("क््रषकों", "कृषकों"),
    ("त्र+ग्वेद", "ऋग्वेद"),
    ("त्र+चाएं", "ऋचाएं"),
    ("त्र+चाआें", "ऋचाओं"),
    ("«ाrक", "ग्रीक"),
    ("«ाrस", "ग्रीस"),
    ("«ांट", "ग्रांट"),
    ("«ोट", "ग्रेट"),
    ("«ोन", "ग्रेन"),
    ("साम«ाr", "सामग्री"),
    ("अ«णी", "अग्रणी"),
    ("अ«द्ूत", "अग्रदूत"),
    ("अधि«ह्ण", "अधिग्रहण"),
    ("आ«ह", "आग्रह"),
    ("सं«हलय", "संग्रहालय"),
    ("सं«ह्ण", "संग्रहण"),
    ("सं«ह", "संग्रह"),
    ("सत्या«ह", "सत्याग्रह"),
    ("«ह्ण", "ग्रहण"),
    ("उ«वादी", "उग्रवादी"),
    ("उ«", "उग्र"),
    ("परिणामस्व¤प", "परिणामस्वरूप"),
    ("फलस्व¤प", "फलस्वरूप"),
    ("स्व¤प", "स्वरूप"),
    ("प्रा¤प", "प्रारूप"),
    ("हेम¤ल", "होमरूल"),
    ("शु¤", "शुरू"),
    ("¤स", "रूस"),
    ("¤प", "रूप"),
    ("£ेनसांग", "ह्वेनसांग"),
    ("£ीलर", "ह्वीलर"),
    ("ùद्य", "हृदय"),
    ("प¢ान", "पठान"),
    ("बा¢", "बाह्य"),
    ("गÅ", "गद्य"),
    ("केjue", "केरल"),
    ("kjue", "केरल"),
    ("दिuueer", "दिल्ली"),
    ("Fšueer", "इटली"),
    ("Fbiueै[", "इंग्लैण्ड"),
]

PASS2_ENGLISH_REPLACEMENTS = [
    ("kjue", "Kerala"),
    ("jsiÙeguesEšie ekš of 1773", "Regulating Act of 1773"),
    ("ceewÙe&", "Maurya"),
    ("ceewÙe", "Maurya"),
    ("Ûeesue", "Chola"),
    ("mJeosMeer Deevoesueve Gandhi peer ves was ØeejcYe efkeâÙee in 1905", "Swadeshi Movement was started in 1905"),
    ("In the ÛecheejCe melÙee«en of 1917", "In the Champaran Satyagraha of 1917"),
    ("Buddhism – Jain «nth", "Buddhism – Jain text"),
    ("Chola – Jain «nth", "Chola – Jain text"),
    ("Medicine's «Th", "Medical text"),
    ("«nthas", "texts"),
    ("«nth", "text"),
    ("«Th", "text"),
    ("diuuuer", "Delhi"),
    ("Fshueer", "Italy"),
    ("Vajaaniya", "Virginia"),
    ("connectioncuttack", "Connecticut"),
]

def clean_h(text):
    if not isinstance(text, str):
        return text
    for old, new in PASS2_HINDI_REPLACEMENTS:
        text = text.replace(old, new)
    return text

def clean_e(text):
    if not isinstance(text, str):
        return text
    for old, new in PASS2_ENGLISH_REPLACEMENTS:
        text = text.replace(old, new)
    return text

def run():
    files = sorted(glob.glob(f"{DIR}/tgt_pgt_hist_ch*.json"))
    print(f"Running Pass 2 clean on {len(files)} files...")

    total_q = 0
    for fpath in files:
        with open(fpath, "r", encoding="utf-8") as fp:
            data = json.load(fp)

        questions = data.get("questions", [])
        total_q += len(questions)

        for q in questions:
            q["questionTextHi"] = clean_h(q.get("questionTextHi", ""))
            q["optionsHi"] = [clean_h(opt) for opt in q.get("optionsHi", [])]
            q["explanationHi"] = clean_h(q.get("explanationHi", ""))

            q["questionTextEn"] = clean_e(q.get("questionTextEn", ""))
            q["optionsEn"] = [clean_e(opt) for opt in q.get("optionsEn", [])]
            q["explanationEn"] = clean_e(q.get("explanationEn", ""))

            # Sync snake_case
            q["question_hi"] = q["questionTextHi"]
            q["options_hi"] = q["optionsHi"]
            q["explanation_hi"] = q["explanationHi"]
            q["question_en"] = q["questionTextEn"]
            q["options_en"] = q["optionsEn"]
            q["explanation_en"] = q["explanationEn"]

        with open(fpath, "w", encoding="utf-8") as fp:
            json.dump(data, fp, ensure_ascii=False, indent=2)

    print(f"Pass 2 completed across {total_q} questions!")

if __name__ == "__main__":
    run()
