import subprocess

# Check commits where teaching was mentioned with tgt
cmd = ['git', 'log', '--grep=teaching', '--oneline', '-n', '15']
res = subprocess.run(cmd, capture_output=True, text=True)
print("Commits with 'teaching':\n", res.stdout)

# Check commit 2557237 message and diff summary
cmd = ['git', 'show', '--stat', '2557237']
res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='ignore')
print("Commit 2557237:\n", res.stdout[:1000])
