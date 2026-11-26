import os, requests

os.makedirs("temp_gate_pdfs", exist_ok=True)
urls = {
    "2022_qp": ("https://gate2027.iitm.ac.in/static/doc/download/2022/ph_2022.pdf", "temp_gate_pdfs/gate_ph_2022_official.pdf"),
    "2022_key": ("https://gate2027.iitm.ac.in/static/doc/download/2022/ph_key_2022.pdf", "temp_gate_pdfs/gate_ph_2022_key.pdf"),
    "2023_qp": ("https://gate2027.iitm.ac.in/static/doc/download/2023/ph_2023.pdf", "temp_gate_pdfs/gate_ph_2023_official.pdf"),
    "2023_key": ("https://gate2027.iitm.ac.in/static/doc/download/Answer_keys2023/PH_ANS_GATE2023.pdf", "temp_gate_pdfs/gate_ph_2023_key.pdf"),
    "2024_qp": ("https://gate2027.iitm.ac.in/static/doc/download/2024/PH24S5.pdf", "temp_gate_pdfs/gate_ph_2024_official.pdf"),
    "2024_key": ("https://gate2027.iitm.ac.in/static/doc/download/2024/PHFinalAnswerKey.pdf", "temp_gate_pdfs/gate_ph_2024_key.pdf"),
}
for k, (u, p) in urls.items():
    try:
        r = requests.get(u, timeout=20)
        print(f"{k}: {r.status_code} ({len(r.content)} bytes)")
        if r.status_code == 200 and len(r.content) > 5000:
            with open(p, "wb") as f:
                f.write(r.content)
    except Exception as e:
        print(f"{k}: error {e}")
