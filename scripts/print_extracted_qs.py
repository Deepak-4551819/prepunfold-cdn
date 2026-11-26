import re

print("==================== 2026 Q.16 to Q.19 ====================")
with open("temp_gate_pdfs/gate_ph_2026_extracted.txt", "r", encoding="utf-8") as f:
    text_2026 = f.read()

for match in re.finditer(r'(Q\.(?:16|17|18|19|44|45|46|2)[\s\S]*?)(?=Q\.\d+|\Z)', text_2026):
    print("--------------------------------------------------")
    print(match.group(1).strip()[:800])

print("\n==================== 2025 Q.5, 8, 10, 41 ====================")
with open("temp_gate_pdfs/gate_ph_2025_extracted.txt", "r", encoding="utf-8") as f:
    text_2025 = f.read()

for match in re.finditer(r'(Q\.(?:5|8|10|41)[\s\S]*?)(?=Q\.\d+|\Z)', text_2025):
    print("--------------------------------------------------")
    print(match.group(1).strip()[:800])
