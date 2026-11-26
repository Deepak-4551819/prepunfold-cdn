import os
import requests
import pdfplumber

os.makedirs("temp_gate_pdfs", exist_ok=True)

urls = {
    "ph_2026_qp": ("https://gate2027.iitm.ac.in/static/doc/download/2026/QPs/PH.pdf", "temp_gate_pdfs/gate_ph_2026.pdf"),
    "ph_2026_key": ("https://gate2027.iitm.ac.in/static/doc/download/2026/Keys/PH_Keys.pdf", "temp_gate_pdfs/gate_ph_2026_key.pdf"),
    "ph_2025_qp": ("https://gate2027.iitm.ac.in/static/doc/download/2025/PH2025.pdf", "temp_gate_pdfs/gate_ph_2025.pdf"),
    "ph_2025_key": ("https://gate2027.iitm.ac.in/static/doc/download/2025_Key/PH_Keys.pdf", "temp_gate_pdfs/gate_ph_2025_key.pdf")
}

for name, (url, path) in urls.items():
    if not os.path.exists(path) or os.path.getsize(path) < 1000:
        print(f"Downloading {name} from {url}...")
        try:
            r = requests.get(url, timeout=30)
            if r.status_code == 200:
                with open(path, "wb") as f:
                    f.write(r.content)
                print(f"Downloaded {path} ({len(r.content)} bytes)")
            else:
                print(f"Failed to download {name}: status {r.status_code}")
        except Exception as e:
            print(f"Error downloading {name}: {e}")
    else:
        print(f"Already exists: {path} ({os.path.getsize(path)} bytes)")
