import urllib.request
import ssl
import sys

ctx = ssl._create_unverified_context()
url = 'https://www.physicsbyfiziks.com/freedownload/previous_year_question_paper/gate/GATE%20Physics-2022_Question%20Paper.pdf'
out = 'temp_gate_pdfs/gate_ph_2022.pdf'

print('Starting download of 2022 PDF...')
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp, open(out, 'wb') as f:
    total = int(resp.headers.get('Content-Length', 0))
    downloaded = 0
    chunk_size = 1024 * 512
    while True:
        chunk = resp.read(chunk_size)
        if not chunk:
            break
        f.write(chunk)
        downloaded += len(chunk)
        percent = (downloaded / total * 100) if total else 0
        sys.stdout.write(f'\rDownloaded {downloaded}/{total} bytes ({percent:.1f}%)')
        sys.stdout.flush()

print('\nDone!')
