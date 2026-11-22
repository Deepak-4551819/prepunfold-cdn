# -*- coding: utf-8 -*-
import json
import re

with open(r'C:\Users\yedde\Downloads\cpc_pyq.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

ch15 = d['chapters'][14]['questions']

for i in range(180, 205):
    q = ch15[i]
    txt = (q.get('question_en') or '') + ' ' + (q.get('question_hi') or '') + ' ' + (q.get('explanation_hi') or '')
    print(f"i={i}: {(q.get('question_en') or q.get('question_hi'))[:60]}")

print("--- 240..255 ---")
for i in range(240, 255):
    q = ch15[i]
    print(f"i={i}: {(q.get('question_en') or q.get('question_hi'))[:60]}")

print("--- 280..295 ---")
for i in range(280, 295):
    q = ch15[i]
    print(f"i={i}: {(q.get('question_en') or q.get('question_hi'))[:60]}")

print("--- 345..360 ---")
for i in range(345, 360):
    q = ch15[i]
    print(f"i={i}: {(q.get('question_en') or q.get('question_hi'))[:60]}")
