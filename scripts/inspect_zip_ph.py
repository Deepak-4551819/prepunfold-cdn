import zipfile
import json

zip_path = r"C:\Users\yedde\Downloads\gate_ph_official_pyqs_2022_2026.zip"

with zipfile.ZipFile(zip_path, 'r') as z:
    for name in ["pyqs/gate_ph_pyq_2025.json", "pyqs/gate_ph_pyq_2026.json"]:
        data = json.loads(z.read(name).decode('utf-8'))
        print(f"=== {name} ===")
        print("Keys:", list(data.keys()))
        print("Total questions:", len(data.get("questions", [])))
        for q in data.get("questions", []):
            qnum = q.get("questionNumber") or q.get("q_num")
            qtype = q.get("questionType") or q.get("type")
            opts = q.get("optionsEn") or q.get("opts") or q.get("options") or []
            qtext = q.get("questionTextEn") or q.get("stem") or q.get("questionText") or ""
            if qtype in ["MCQ", "MSQ"] and len(opts) < 4:
                print(f"  Q{qnum} ({qtype}) opts count={len(opts)}: {opts} | Stem: {qtext[:80]}...")
            if "– Q." in qtext or "Carry" in qtext:
                print(f"  Q{qnum} header in text: {qtext[:80]}...")
