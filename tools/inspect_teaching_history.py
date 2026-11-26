import subprocess

cmd = ['git', 'log', '-n', '10', '--oneline', 'manifest.json']
res = subprocess.run(cmd, capture_output=True, text=True)
print("Git log for manifest.json:\n", res.stdout)

cmd2 = ['git', 'log', '-S', 'teaching', '-n', '5', '--oneline', 'manifest.json']
res2 = subprocess.run(cmd2, capture_output=True, text=True)
print("Git log searching 'teaching' in manifest.json:\n", res2.stdout)
