# -*- coding: utf-8 -*-
import sys
import os
import json

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

print("=== Scanning tests/jam/jam_ma ===")
for root, dirs, files in os.walk('tests/jam/jam_ma'):
    for f in files:
        p = os.path.join(root, f)
        print(p, os.path.getsize(p))

print("\n=== Manifest Category jam_ma ===")
with open('manifest.json', 'r', encoding='utf-8') as f:
    m = json.load(f)

for c in m.get('categories', []):
    if 'jam' in c.get('id', ''):
        print(f"Cat {c.get('id')}: title={c.get('title')} | totalTests={c.get('totalTests')} | totalQs={c.get('totalQuestions')}")
        print("  Details:", {k: v for k, v in c.items() if k not in ('parts', 'tags')})

print("\n=== Manifest Tests for jam_ma ===")
jam_tests = [(i, t.get('categoryId'), t.get('testId'), t.get('filePath'), t.get('totalQuestions')) for i, t in enumerate(m.get('tests', [])) if 'jam' in t.get('categoryId', '')]
for idx, cat, tid, fp, tq in jam_tests:
    print(f"  [{idx}] cat={cat} id={tid} Qs={tq} path={fp}")
