# -*- coding: utf-8 -*-
import sys
import json
import zipfile

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

zip_path = r"C:\Users\yedde\Downloads\jam_cy_mocks_and_topic_tests.zip"
with zipfile.ZipFile(zip_path, 'r') as z:
    snip_raw = z.read('jam_cy_mocks_topic_manifest_snippet.json').decode('utf-8')
    items = json.loads(snip_raw)
    print(f"Snippet contains {len(items)} items:")
    for i, it in enumerate(items):
        print(f"[{i+1:02d}] {it.get('testId')} | {it.get('title')} | type={it.get('testType')} | isFree={it.get('isFree')} | Qs={it.get('totalQuestions')}")

    # Inspect Mock 01
    m1 = json.loads(z.read('jam_cy_mock_01.json').decode('utf-8'))
    print("\n=== MOCK 01 ===")
    print("Top keys count:", len(m1))
    print("Top keys:", list(m1.keys()))
    print("Sections:", m1.get('sections'))
    print("Q1 keys:", list(m1['questions'][0].keys()))
    print("Q1 negativeMarks:", m1['questions'][0].get('negativeMarks'))
    print("Q11 (2m MCQ) negativeMarks:", m1['questions'][10].get('negativeMarks'))

    # Inspect Topic Test 01
    t1_name = [n for n in z.namelist() if 'topic' in n and n.endswith('.json') and 'snippet' not in n][0]
    t1 = json.loads(z.read(t1_name).decode('utf-8'))
    print(f"\n=== TOPIC TEST: {t1_name} ===")
    print("Top keys count:", len(t1))
    print("Top keys:", list(t1.keys()))
    print("partId:", t1.get('partId'), "partTitle:", t1.get('partTitle'))
    print("Sections:", t1.get('sections'))
    print("Q1 keys:", list(t1['questions'][0].keys()))
    print("Q1 negativeMarks:", t1['questions'][0].get('negativeMarks'))
