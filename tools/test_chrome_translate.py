import requests, urllib.parse

text = "किसने व्यपगत के सिद्धन्त की रचना की?"
url = f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=hi&tl=en&q={urllib.parse.quote(text)}"
r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}, timeout=10)
print("Status code:", r.status_code)
print("Response:", r.json())
