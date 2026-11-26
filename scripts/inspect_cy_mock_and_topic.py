# -*- coding: utf-8 -*-
import sys
import json
import zipfile

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ZIP_PATH = r"C:\Users\yedde\Downloads\gate_cy_mocks_and_topic_tests.zip"

with zipfile.ZipFile(ZIP_PATH, 'r') as z:
    for name in ["gate_cy_mock_01.json", "gate_cy_topic_quantum_chemistry_01.json", "gate_cy_topic_general_aptitude_01.json"]:
        raw = z.read(name).decode('utf-8')
        d = json.loads(raw)
        print(f"\n--- {name} ---")
        print("Top keys:", list(d.keys()))
        print("testId:", d.get("testId"))
        print("testType:", d.get("testType"))
        print("title:", d.get("title"))
        print("totalQuestions:", d.get("totalQuestions"), len(d.get("questions", [])))
        print("maxMarks:", d.get("maxMarks"))
        print("isFree:", d.get("isFree"))
        print("partId:", d.get("partId"))
        print("partTitle:", d.get("partTitle"))
        print("sections:", d.get("sections"))
        qs = d.get("questions", [])
        if qs:
            print("Q1 keys:", list(qs[0].keys()))
            print("Q1 sample:", json.dumps(qs[0], indent=2, ensure_ascii=False)[:300])
