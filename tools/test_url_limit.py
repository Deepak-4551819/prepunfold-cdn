import requests, urllib.parse

# Test with POST or smaller batches
text_list = ["यह एक परीक्षण वाक्य है जो इतिहास के बारे में बताता है।" for _ in range(30)]
joined = "\n".join(text_list)
print("Joined length in chars:", len(joined))

url = f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=hi&tl=en&q={urllib.parse.quote(joined)}"
print("URL length:", len(url))

r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
print("GET status code:", r.status_code)

# Try POST to clients5 or translate.googleapis.com
post_url = "https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=hi&tl=en"
r_post = requests.post(post_url, data={'q': joined}, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
print("POST status code:", r_post.status_code)
if r_post.status_code == 200:
    print("POST success! Lines:", len(r_post.json()[0].split('\n')))
