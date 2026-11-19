import subprocess, sys

print("Executing: git push origin main")
p = subprocess.Popen(["git", "push", "origin", "main"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
for line in p.stdout:
    print(line, end='', flush=True)
p.wait()
print(f"\nExited with code {p.returncode}")
sys.exit(p.returncode)
