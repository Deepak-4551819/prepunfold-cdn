# -*- coding: utf-8 -*-
import sys
import json
import zipfile

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

zip_path = r"C:\Users\yedde\Downloads\jam_ph_official_pyqs_2022_2026.zip"
with zipfile.ZipFile(zip_path, "r") as z:
    for year in range(2022, 2027):
        data = json.loads(z.read(f"jam_ph_pyq_{year}.json").decode("utf-8"))
        print(f"\n{year} top keys ({len(data)}): {list(data.keys())}")
        print(f"  title: {data.get('title')}")
        print(f"  titleEn: {data.get('titleEn')}")
        print(f"  testType: {data.get('testType')}")
        print(f"  isFree: {data.get('isFree')}")
        print(f"  maxMarks: {data.get('maxMarks')}")
        print(f"  positiveMarks: {data.get('positiveMarks')}")
        print(f"  negativeMarks: {data.get('negativeMarks')}")
        print(f"  totalQuestions: {data.get('totalQuestions')}")
        print(f"  shiftBadge: {data.get('shiftBadge')}")
        print(f"  sections: {json.dumps(data.get('sections'))}")
