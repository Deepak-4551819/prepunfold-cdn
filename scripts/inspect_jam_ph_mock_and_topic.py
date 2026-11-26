# -*- coding: utf-8 -*-
import sys
import json
import zipfile

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

zip_path = r"C:\Users\yedde\Downloads\jam_ph_mocks_and_topic_tests.zip"
with zipfile.ZipFile(zip_path, 'r') as z:
    # 1. Inspect Mock 01
    m1 = json.loads(z.read('jam_ph_mock_01.json').decode('utf-8'))
    print("=== MOCK 01 ===")
    print("Top-level keys count:", len(m1))
    print("Top-level keys:", list(m1.keys()))
    print("Questions count:", len(m1.get('questions', [])))
    print("Sections:", json.dumps(m1.get('sections', []), indent=2))
    print("Q1 sample keys:", list(m1['questions'][0].keys()))
    print("Q1 negativeMarks:", m1['questions'][0].get('negativeMarks'))
    print("Q11 (2m MCQ) negativeMarks:", m1['questions'][10].get('negativeMarks'))

    # 2. Inspect a Topic Test
    t1 = json.loads(z.read('jam_ph_topic_mathematical_methods_01.json').decode('utf-8'))
    print("\n=== TOPIC TEST 01 ===")
    print("Top-level keys count:", len(t1))
    print("Top-level keys:", list(t1.keys()))
    print("Questions count:", len(t1.get('questions', [])))
    print("Sections:", json.dumps(t1.get('sections', []), indent=2))
    print("Q1 sample keys:", list(t1['questions'][0].keys()))
    print("Q1 negativeMarks:", t1['questions'][0].get('negativeMarks'))
