import zipfile
import json

zip_path = r"C:\Users\yedde\Downloads\gate_ph_official_pyqs_2022_2026.zip"

with zipfile.ZipFile(zip_path, 'r') as z:
    for name in ["pyqs/gate_ph_pyq_2025.json", "pyqs/gate_ph_pyq_2026.json"]:
        data = json.loads(z.read(name).decode('utf-8'))
        print(f"\n=================== {name} ===================")
        bad_chars = []
        for q in data["questions"]:
            qnum = q["questionNumber"]
            s = json.dumps(q)
            if "\ufffd" in s or "(cid:" in s:
                bad_chars.append(qnum)
        print(f"Questions with \\ufffd or (cid: in {name}: {bad_chars}")

        # Check 2026 Q17, Q45
        if "2026" in name:
            for q in data["questions"]:
                if q["questionNumber"] in [2, 17, 18, 45, 46]:
                    print(f"\n--- 2026 Q{q['questionNumber']} ---")
                    print("questionTextEn:", q.get("questionTextEn"))
                    print("optionsEn:", q.get("optionsEn"))
                    print("correctOption:", q.get("correctOption"), "correct_index:", q.get("correct_index"))
                    print("explanationEn:", q.get("explanationEn"))

        if "2025" in name:
            for q in data["questions"]:
                if q["questionNumber"] in [5, 8, 10, 41]:
                    print(f"\n--- 2025 Q{q['questionNumber']} ---")
                    print("questionTextEn:", q.get("questionTextEn"))
                    print("correctOption:", q.get("correctOption"), "correct_index:", q.get("correct_index"))
                    print("explanationEn:", q.get("explanationEn"))
