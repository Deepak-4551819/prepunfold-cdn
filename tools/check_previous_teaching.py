import subprocess
import json

cmd = ['git', 'show', '2557237:manifest.json']
res = subprocess.run(cmd, capture_output=True)
manifest = json.loads(res.stdout.decode('utf-8', errors='ignore'))

# Look at category for history
for c in manifest.get('categories', []):
    if 'history' in str(c).lower() and 'tgt' in str(c).lower():
        print("Category in 2557237:", json.dumps(c, ensure_ascii=False, indent=2))

tests = manifest.get('tests', [])
hist_tests = [t for t in tests if 'tgt_pgt_history' in t.get('categoryId', '') or 'history' in t.get('path', '')]
print(f"Total history tests in 2557237: {len(hist_tests)}")
for t in hist_tests[:5]:
    print(t.get('testId'), '|', t.get('categoryId'), '|', t.get('path'), '|', t.get('totalQuestions'))
