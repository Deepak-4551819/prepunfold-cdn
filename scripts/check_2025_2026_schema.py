import zipfile
import json

zip_path = r"C:\Users\yedde\Downloads\gate_ph_official_pyqs_2022_2026.zip"

with zipfile.ZipFile(zip_path, 'r') as z:
    for name in ["pyqs/gate_ph_pyq_2025.json", "pyqs/gate_ph_pyq_2026.json"]:
        data = json.loads(z.read(name).decode('utf-8'))
        print(f"\n=== Checking schema of {name} ===")
        all_keys = set()
        for q in data["questions"]:
            all_keys.update(q.keys())
        print("Union of question keys:", sorted(list(all_keys)))
        sample_q = data["questions"][0]
        print("Sample Q1:")
        print(json.dumps(sample_q, indent=2))
