import subprocess

cmd = ['git', 'show', '--stat', 'af01adf']
res = subprocess.run(cmd, capture_output=True, text=True)
print("Commit af01adf stat:\n", res.stdout[:1500])

cmd2 = ['git', 'show', 'af01adf:manifest.json']
res2 = subprocess.run(cmd2, capture_output=True, text=True)
import json
try:
    m = json.loads(res2.stdout)
    for c in m.get('categories', []):
        if 'history' in c.get('categoryId', '') or 'history' in c.get('name', '').lower() or 'tgt' in c.get('categoryId', ''):
            print("Category in af01adf:", c)
    tgt_tests = [t for t in m.get('tests', []) if 'history' in t.get('categoryId', '') or 'history' in t.get('path', '')]
    print(f"Total history tests in af01adf: {len(tgt_tests)}")
    if tgt_tests:
        print("Sample test in af01adf:", tgt_tests[0])
except Exception as e:
    print("Error parsing manifest:", e)
