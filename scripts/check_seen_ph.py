import json

with open("seen_question_hashes.json", "r", encoding="utf-8") as f:
    hashes = json.load(f)

ph_pyqs = {}
for h, info in hashes.items():
    tid = info.get("testId", "")
    if "gate_ph_pyq" in tid:
        ph_pyqs[tid] = ph_pyqs.get(tid, 0) + 1

print("Current gate_ph_pyq counts in seen_question_hashes.json:")
for tid, cnt in sorted(ph_pyqs.items()):
    print(f"  {tid}: {cnt}")
