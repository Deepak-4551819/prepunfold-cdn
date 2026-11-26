import requests, urllib.parse, time

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

t0 = time.time()
joined = "\n".join(texts)
url = f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=hi&tl=en&q={urllib.parse.quote(joined)}"
r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
if r.status_code == 200:
    res = r.json()
    lines = res[0].split("\n")
    print(f"Batch translated {len(lines)} items in a SINGLE request in {time.time() - t0:.2f}s:")
    for src, tr in zip(texts, lines):
        print(f"  {src:<35} -> {tr}")
else:
    print("Failed with status:", r.status_code)
