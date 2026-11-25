import json

d = json.load(open('tests/gate/gate_ph/pyq/gate_ph_pyq_2024.json', encoding='utf-8'))
q0 = d['questions'][0]
print("PH Q0 keys:", list(q0.keys()))
print("Does PH have q_id?", 'q_id' in q0)
