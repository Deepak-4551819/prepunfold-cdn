import urllib.request
import re

url = "https://www.physicsbyfiziks.com/previous-year-gate-question-paper-with-solutions/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        links = re.findall(r'href=[\"\']([^\"\']+)[\"\']', html, re.I)
        print("Total links:", len(links))
        for l in links:
            if '2021' in l or 'pdf' in l.lower():
                print("  ", l)
except Exception as e:
    print("Error:", e)
