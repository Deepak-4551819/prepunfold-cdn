import json
import re

with open("manifest.json", "r", encoding="utf-8") as f:
    text = f.read()

urls = re.findall(r'https://cdn\.jsdelivr\.net/gh/[^/]+/[^/]+@[^/]+/', text)
print("CDN URLs in manifest:")
for u in set(urls):
    print(" ", u)
