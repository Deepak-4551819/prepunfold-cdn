import re
import json

with open('temp_gate_pdfs/gate_ph_2023_text.txt', encoding='utf-8') as f:
    text = f.read()

# Clean up header/footer noise
# Lines like: "GATE Physics Question Paper-2023", "Physics by fiziks", "H.No. 40-D...", "Phone:...", "Website:...", "=== PAGE \d+ ==="
cleaned_lines = []
for line in text.split('\n'):
    l = line.strip()
    if not l:
        continue
    if any(drop in l for drop in [
        'GATE Physics Question Paper-2023',
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
parts = re.split(r'\n(?=Q\d+\.)', cleaned_text)

print(f'Preamble: {parts[0][:150]}')
print(f'Total questions found: {len(parts) - 1}')

for idx in range(1, len(parts)):
    q_text = parts[idx]
    m = re.match(r'Q(\d+)\.', q_text)
    q_num = int(m.group(1)) if m else idx
    print(f'Q{q_num}: lines={len(q_text.splitlines())}, sample={q_text.splitlines()[1][:60]}')
