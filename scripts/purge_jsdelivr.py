# -*- coding: utf-8 -*-
import urllib.request
import json

urls_to_purge = [
    "https://purge.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/manifest.json",
    "https://purge.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/tests/judiciary_pyq/cpc/cpc_pyq_t01_preliminary.json",
    "https://purge.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/tests/judiciary_pyq/cpc/cpc_pyq_t06_execution.json"
]

for url in urls_to_purge:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read().decode('utf-8')
            print(f"Purged {url}: {data}")
    except Exception as e:
        print(f"Purge error for {url}: {e}")
