import subprocess
import sys

print("Starting git push...")
try:
    res = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True, timeout=120)
    print("Return code:", res.returncode)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)
except subprocess.TimeoutExpired as e:
    print("Timeout expired after 120s:", e)
except Exception as e:
    print("Exception:", e)
