import urllib.request
import os

os.makedirs("temp_gate_pdfs", exist_ok=True)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

urls = [
    ("https://www.physicsbyfiziks.com/pdf/gate/GATE%202021_Solution.pdf", "fiziks_gate_2021.pdf"),
    ("https://pravegaa.com/wp-content/uploads/2021/04/GATE-2021.pdf", "pravegaa_gate_2021.pdf")
]

for url, fname in urls:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            outpath = os.path.join("temp_gate_pdfs", fname)
            with open(outpath, "wb") as f:
                f.write(data)
            print(f"Downloaded {fname}: {len(data)} bytes")
    except Exception as e:
        print(f"Failed {url}: {e}")
