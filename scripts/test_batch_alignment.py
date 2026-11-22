import requests, urllib.parse

items = [
    "Adam Smith",
    "J.K. Mehta",
    "Marshall",
    "Robbins",
    "Who said, \"The problem of getting freedom from wants is regarded as an economic problem\"?",
    "Perfect competition",
    "Monopolistic competition",
    "Monopoly",
    "Oligopoly",
    "Law of diminishing marginal utility",
    "Indifference curve",
    "Consumer surplus",
    "Inflation",
    "Deflation",
    "Fiscal policy",
    "Monetary policy",
    "Gross Domestic Product",
    "Net National Product",
    "Balance of Payments",
    "Foreign Direct Investment"
]

def translate_batch(batch, sl="en", tl="hi"):
    cleaned_batch = [b.replace("\n", " ").strip() for b in batch]
    joined = "\n".join(cleaned_batch)
    url = f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl={sl}&tl={tl}&q={urllib.parse.quote(joined)}"
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=12)
    if r.status_code == 200:
        res = r.json()
        lines = res[0].split("\n")
        if len(lines) == len(batch):
            return dict(zip(batch, lines))
    return None

res = translate_batch(items)
print("Success:", res is not None)
if res:
    for k, v in list(res.items())[:6]:
        print(f"  {k} -> {v}")
