import requests, urllib.parse, time
from concurrent.futures import ThreadPoolExecutor

texts = [
    "किसने व्यपगत के सिद्धान्त की रचना की?",
    "लॉर्ड कैनिंग",
    "लॉर्ड डलहौजी",
    "लॉर्ड कर्जन",
    "लॉर्ड एलनबरो",
    "निम्नलिखित में से फ्रेंच ईस्ट इण्डिया कम्पनी का संस्थापक कौन था?",
    "डूप्ले",
    "फ्रांसिस मार्टिन",
    "काउंट डी लैली",
    "कॉलबर्ट"
]

def translate_single(text):
    url = f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=hi&tl=en&q={urllib.parse.quote(text)}"
    try:
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=8)
        if r.status_code == 200:
            res = r.json()
            if isinstance(res, list) and res and isinstance(res[0], str):
                return text, res[0]
    except Exception as e:
        pass
    return text, text

t0 = time.time()
with ThreadPoolExecutor(max_workers=5) as ex:
    results = list(ex.map(translate_single, texts))

print(f"Translated {len(texts)} texts in {time.time() - t0:.2f}s:")
for src, tr in results:
    print(f"  {src:<35} -> {tr}")
