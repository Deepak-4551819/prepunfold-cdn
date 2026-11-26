import json

with open('manifest_tgt_pgt_history_master.json', 'r', encoding='utf-8') as f:
    m = json.load(f)

part_counts = {}
for t in m.get('tests', []):
    pid = t.get('partId') or t.get('part_id')
    part_counts[pid] = part_counts.get(pid, 0) + 1

print("Parts in manifest_tgt_pgt_history_master.json:")
for pid, c in part_counts.items():
    print(f"  {pid}: {c} tests")
