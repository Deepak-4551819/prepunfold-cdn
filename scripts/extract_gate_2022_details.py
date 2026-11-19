import re
import json

with open('temp_gate_pdfs/gate_ph_2022_text.txt', encoding='utf-8') as f:
    text = f.read()

cleaned_lines = []
for line in text.split('\n'):
    l = line.strip()
    if not l:
        continue
    if any(drop in l for drop in [
        'GATE 2022: Question Paper',
        'Physics by fiziks',
        'Learn Physics in Right Way',
        'H.No. 40-D',
        'Phone: 011-',
        'Website: www.physicsbyfiziks.com',
        'Be Part of Disciplined Learning',
        '=== PAGE '
    ]):
        continue
    cleaned_lines.append(line)

cleaned_text = '\n'.join(cleaned_lines)
parts = re.split(r'\n(?=Q\d+[\.:\s])', cleaned_text)

extracted = {}
for idx in range(1, len(parts)):
    q_body = parts[idx]
    m = re.match(r'Q(\d+)[\.:\s]\s*(.*)', q_body, re.DOTALL)
    if not m:
        continue
    q_num = int(m.group(1))
    body = m.group(2).strip()

    ans_split = re.split(r'\nAns\.?\s*\d*\s*:\s*', body)
    q_and_opts = ans_split[0]
    ans_text = ans_split[1] if len(ans_split) > 1 else ""

    extracted[q_num] = {
        "raw_body": q_and_opts,
        "ans_text": ans_text.strip()
    }

print(f"Extracted {len(extracted)} questions for 2022.")
with open('temp_gate_pdfs/extracted_2022_raw.json', 'w', encoding='utf-8') as f:
    json.dump(extracted, f, indent=2, ensure_ascii=False)
