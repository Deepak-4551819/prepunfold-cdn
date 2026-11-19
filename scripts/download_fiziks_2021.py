import urllib.request
import re
import os

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

urls = [
    "https://www.physicsbyfiziks.com/wp-content/uploads/2021/04/GATE-2021-Solution.pdf",
    "https://www.physicsbyfiziks.com/wp-content/uploads/2021/02/GATE-2021-PH-Solution.pdf",
    "https://www.physicsbyfiziks.com/wp-content/uploads/2021/03/GATE_2021_Solution.pdf",
    "https://www.physicsbyfiziks.com/download/GATE-2021-Solution.pdf",
    "https://www.physicsbyfiziks.com/download/gate-physics-previous-year-questions-with-solutions/"
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            content_type = resp.headers.get('Content-Type', '')
            length = resp.headers.get('Content-Length', 0)
            print(f"200: {u} ({content_type}, {length})")
            if 'pdf' in content_type:
                with open("temp_gate_pdfs/fiziks_gate_2021.pdf", "wb") as f_out:
                    f_out.write(resp.read())
                print("Saved fiziks_gate_2021.pdf!")
                break
            elif 'html' in content_type:
                html = resp.read().decode('utf-8', errors='ignore')
                links = re.findall(r'href=[\"\']([^\"\']+\.pdf)[\"\']', html, re.I)
                print(f"Found {len(links)} pdf links in page:")
                for l in links:
                    if '2021' in l:
                        print("  2021 PDF link:", l)
    except Exception as e:
        print(f"Failed {u}: {e}")
