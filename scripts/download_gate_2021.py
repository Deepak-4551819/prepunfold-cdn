import urllib.request
import re
import os
import ssl

ctx = ssl._create_unverified_context()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

url = "https://gate2025.iitr.ac.in/download.html"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

links = re.findall(r'href=[\"\']([^\"\']+)[\"\']', html, re.I)
ph_links = [l for l in links if 'ph' in l.lower() or 'physics' in l.lower()]
print("All PH links:")
for l in ph_links:
    print("  ", l)

# Download 2021 PH
os.makedirs("temp_gate_pdfs", exist_ok=True)
for l in ph_links:
    if '2021' in l:
        full_url = "https://gate2025.iitr.ac.in/" + l if not l.startswith('http') else l
        fname = os.path.basename(l)
        print(f"Downloading {full_url} -> temp_gate_pdfs/{fname}...")
        try:
            req_pdf = urllib.request.Request(full_url, headers=headers)
            with urllib.request.urlopen(req_pdf, context=ctx, timeout=15) as r:
                data = r.read()
                with open(f"temp_gate_pdfs/{fname}", "wb") as f_out:
                    f_out.write(data)
                print(f"Downloaded {fname}, size: {len(data)} bytes")
        except Exception as e:
            print(f"Failed {full_url}: {e}")
