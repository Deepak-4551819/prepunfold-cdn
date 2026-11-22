import requests, urllib.parse

lines = [
    "Who said, \"The problem of getting freedom from wants is regarded as an economic problem\"?",
    "Adam Smith",
    "J.K. Mehta",
    "Marshall",
    "Robbins",
    "This definition is given by J.K. Mehta who is called Indian philosopher and ascetic economist."
]

joined = "\n".join(lines)
url = f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=en&tl=hi&q={urllib.parse.quote(joined)}"
r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
print('Status:', r.status_code)
res = r.json()
print('Result:\n' + res[0])
split_res = res[0].split('\n')
print('Split count:', len(split_res))
