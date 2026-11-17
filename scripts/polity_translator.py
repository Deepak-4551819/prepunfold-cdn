import pymupdf
import re
import json
import os
import requests
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

CACHE_FILE = r'D:\Android Project\prepunfold-cdn\scripts\translation_cache.json'
if os.path.exists(CACHE_FILE):
    try:
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            trans_cache = json.load(f)
    except:
        trans_cache = {}
else:
    trans_cache = {}

# Seed dictionary with standard recurring phrases
standard_terms = {
    "None of the above": "उपर्युक्त में से कोई नहीं",
    "None of these": "इनमें से कोई नहीं",
    "All of the above": "उपर्युक्त सभी",
    "All of these": "ये सभी",
    "Both 1 and 2": "1 और 2 दोनों",
    "Neither 1 nor 2": "न तो 1 और न ही 2",
    "1 only": "केवल 1",
    "2 only": "केवल 2",
    "3 only": "केवल 3",
    "1, 2 and 3": "1, 2 और 3",
    "1 and 2 only": "केवल 1 और 2",
    "1 and 3 only": "केवल 1 और 3",
    "2 and 3 only": "केवल 2 और 3",
    "See the explanation of above question.": "उपर्युक्त प्रश्न की व्याख्या देखें।",
    "See the explanation of previous question.": "पिछले प्रश्न की व्याख्या देखें।",
    "The Constitution of India": "भारत का संविधान",
    "Supreme Court of India": "भारत का सर्वोच्च न्यायालय",
    "High Court": "उच्च न्यायालय",
    "President of India": "भारत के राष्ट्रपति",
    "Prime Minister": "प्रधानमंत्री",
    "Parliament of India": "भारत की संसद",
    "Lok Sabha": "लोकसभा",
    "Rajya Sabha": "राज्यसभा",
    "Fundamental Rights": "मूल अधिकार",
    "Directive Principles of State Policy": "राज्य के नीति निदेशक तत्व",
    "Fundamental Duties": "मूल कर्तव्य",
    "Preamble": "प्रस्तावना"
}
trans_cache.update(standard_terms)

def save_cache():
    try:
        with open(CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump(trans_cache, f, ensure_ascii=False, indent=2)
    except:
        pass

def translate_text(text):
    text = text.strip()
    if not text:
        return ""
    if text in trans_cache:
        return trans_cache[text]

    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=hi&dt=t&q={urllib.parse.quote(text)}"
    try:
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=8)
        if r.status_code == 200:
            res = ''.join([item[0] for item in r.json()[0]])
            trans_cache[text] = res
            return res
    except:
        pass
    return text

print(f"Loaded {len(trans_cache)} cached translations.")
