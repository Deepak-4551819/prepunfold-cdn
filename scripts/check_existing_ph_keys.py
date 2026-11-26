import json

for year in [2022, 2023, 2024]:
    path = f"tests/gate/gate_ph/pyq/gate_ph_pyq_{year}.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    all_keys = set()
    for q in data["questions"]:
        all_keys.update(q.keys())
    print(f"=== Existing {year} ===")
    print("Top level keys:", list(data.keys()))
    print("Question keys:", sorted(list(all_keys)))
