# -*- coding: utf-8 -*-
import sys
import json

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('manifest.json', 'r', encoding='utf-8') as f:
    mf = json.load(f)

tests = [t for t in mf.get('tests', []) if t.get('categoryId') == 'jam_ph']
print(f"=== TOTAL JAM PH TESTS IN MANIFEST: {len(tests)} ===\n")

print("--- 10 FULL LENGTH MOCKS ---")
for t in tests:
    if t.get('testType') == 'FULL_MOCK':
        print(f"  [{t.get('testId')}] {t.get('title')} | isFree={t.get('isFree')} | Qs={t.get('totalQuestions')} | Path={t.get('path')}")

print("\n--- 5 OFFICIAL PYQS ---")
for t in tests:
    if t.get('testType') == 'PYQ':
        print(f"  [{t.get('testId')}] {t.get('title')} | isFree={t.get('isFree')} | Qs={t.get('totalQuestions')} | Path={t.get('path')}")

print("\n--- 14 TOPIC TESTS ---")
for t in tests:
    if t.get('testType') == 'TOPIC':
        print(f"  [{t.get('testId')}] {t.get('title')} | isFree={t.get('isFree')} | Part={t.get('partId')} | Path={t.get('path')}")
