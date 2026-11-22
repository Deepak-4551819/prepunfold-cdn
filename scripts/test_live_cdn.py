# -*- coding: utf-8 -*-
import  urllib.request
import json

url = 'https://raw.githubusercontent.com/Deepak-4551819/prepunfold-cdn/main/tests/judiciary_pyq/cpc/cpc_pyq_t06_execution.json'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        d = json.loads(resp.read().decode('utf-8'))
        q1 = d['questions'][0]
        print("Live Q1 English:", q1.get('questionTextEn'))
        print("Live Q1 Hindi:", q1.get('questionTextHi'))
except Exception as e:
    print("Fetch info:", e)
