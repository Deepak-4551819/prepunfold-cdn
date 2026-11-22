# -*- coding: utf-8 -*-
import json
import re

with open(r'C:\Users\yedde\Downloads\cpc_pyq.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

ch15 = d['chapters'][14]['questions']

def roman_to_int(s):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
    val = 0
    s = s.upper()
    for i, c in enumerate(s):
        if c not in romans: return 0
        if i + 1 < len(s) and romans[c] < romans[s[i+1]]:
            val -= romans[c]
        else:
            val += romans[c]
    return val

def get_order_num(q):
    txt = (q.get('question_en') or '') + ' ' + (q.get('question_hi') or '') + ' ' + (q.get('explanation_hi') or '')
    ms = re.findall(r'(?:आदेश|Order)\s*([0-9IVXLCDM]+)', txt, re.I)
    for m in ms:
        if m.isdigit():
            n = int(m)
            if 1 <= n <= 55: return n
        else:
            n = roman_to_int(m)
            if 1 <= n <= 55: return n
    return None

last_ord = 1
for i, q in enumerate(ch15):
    ord_n = get_order_num(q)
    if ord_n:
        last_ord = ord_n
    if i in [180, 181, 182, 183, 184, 185, 240, 241, 242, 243, 244, 245, 280, 281, 282, 283, 284, 285, 340, 341, 342, 343, 344, 345]:
        print(f"i={i}: detected Order={last_ord} | {(q.get('question_en') or q.get('question_hi'))[:60]}")
