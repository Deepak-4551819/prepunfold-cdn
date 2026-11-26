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

targets = [
    (2022, 16),
    (2022, 20),
    (2022, 57),
    (2023, 22),
    (2024, 42)
]

with zipfile.ZipFile(zip_path, "r") as z:
    for year, qnum in targets:
        fname = f"jam_ph_pyq_{year}.json"
        data = json.loads(z.read(fname).decode("utf-8"))
        q = next(item for item in data["questions"] if item["questionNumber"] == qnum)
        print(f"\n==================== {year} Q{qnum} ====================")
        print("questionType:", q.get("questionType"))
        print("positiveMarks:", q.get("positiveMarks"))
        print("negativeMarks:", q.get("negativeMarks"))
        print("correctOption:", q.get("correctOption"))
        print("correctOptionsList:", q.get("correctOptionsList"))
        print("natMin:", q.get("natMin"))
        print("natMax:", q.get("natMax"))
        print("questionTextEn:", q.get("questionTextEn")[:150])
        print("explanationEn:", q.get("explanationEn"))
