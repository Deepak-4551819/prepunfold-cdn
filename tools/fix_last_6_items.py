import json

# 1. Ch 3 Q256
with open('tests/tgt_pgt_history/tgt_pgt_hist_ch03_vedic_period.json', 'r', encoding='utf-8') as f:
    d = json.load(f)
for q in d['questions']:
    if q['questionNumber'] == 256:
        q['optionsEn'] = ["Kaikeya", "Madra", "Panchala", "Ushinara"]
        q['options_en'] = q['optionsEn']
with open('tests/tgt_pgt_history/tgt_pgt_hist_ch03_vedic_period.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

# 2. Ch 6 Q43
with open('tests/tgt_pgt_history/tgt_pgt_hist_ch06_gupta_post_gupta.json', 'r', encoding='utf-8') as f:
    d = json.load(f)
for q in d['questions']:
    if q['questionNumber'] == 43:
        q['optionsEn'] = ["Bhukta", "Uparika", "Commissioner", "District Officer"]
        q['options_en'] = q['optionsEn']
with open('tests/tgt_pgt_history/tgt_pgt_hist_ch06_gupta_post_gupta.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

# 3. Ch 9 Q34
with open('tests/tgt_pgt_history/tgt_pgt_hist_ch09_ancient_misc.json', 'r', encoding='utf-8') as f:
    d = json.load(f)
for q in d['questions']:
    if q['questionNumber'] == 34:
        q['optionsEn'] = ["Capillarity", "Anga Samhita", "Matriarch", "Nashat"]
        q['options_en'] = q['optionsEn']
with open('tests/tgt_pgt_history/tgt_pgt_hist_ch09_ancient_misc.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

# 4. Ch 30 Q7, Q153, Q220
with open('tests/tgt_pgt_history/tgt_pgt_hist_ch30_world_history.json', 'r', encoding='utf-8') as f:
    d = json.load(f)
for q in d['questions']:
    if q['questionNumber'] == 7:
        q['explanationEn'] = q['explanationEn'].replace("Camões", "Camoes")
        q['explanation_en'] = q['explanationEn']
    elif q['questionNumber'] == 153:
        q['optionsEn'] = [
            "The Aborigines Act (1934)",
            "The Native Administration Act (1936)",
            "The Aboriginals Ordinance Act (1918)",
            "The Aborigines Protection Act (1909)"
        ]
        q['options_en'] = q['optionsEn']
    elif q['questionNumber'] == 220:
        q['explanationEn'] = q['explanationEn'].replace("Müntzer", "Muntzer")
        q['explanation_en'] = q['explanationEn']
        q['optionsEn'] = [o.replace("Müntzer", "Muntzer") for o in q['optionsEn']]
        q['options_en'] = q['optionsEn']
with open('tests/tgt_pgt_history/tgt_pgt_hist_ch30_world_history.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print("Applied precision fixes to the last 6 items!")
