import subprocess

cmd = ['git', 'show', '--stat', '9a2a79c']
res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='ignore')
print("Commit 9a2a79c:\n", res.stdout[:1500])
