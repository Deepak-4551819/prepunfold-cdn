import json
import os
import re

TESTS_DIR = "tests/tgt_pgt_history"
KRUTI_PAT = re.compile(r'uee@|kewâ|cesÙ|fह्|[™०åäø§°\^@æ®]')

def dump():
    files = sorted([f for f in os.listdir(TESTS_DIR) if f.startswith('tgt_pgt_hist_ch') and f.endswith('.json')])
    words_found = {}

    for fname in files:
        fpath = os.path.join(TESTS_DIR, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for q in data.get('questions', []):
            texts = [str(q.get('questionTextHi') or ''), str(q.get('explanationHi') or '')]
            texts.extend([str(o) for o in q.get('optionsHi', [])])

            for text in texts:
                for match in KRUTI_PAT.finditer(text):
                    m = re.search(r'[^\s,।.:;?!()\'"\[\]{}]+(' + KRUTI_PAT.pattern + r')[^\s,।.:;?!()\'"\[\]{}]*', text[max(0, match.start()-25):min(len(text), match.end()+25)])
                    tok = m.group(0) if m else match.group(0)
                    words_found[tok] = words_found.get(tok, 0) + 1

    sorted_words = sorted(words_found.items(), key=lambda x: -x[1])
    with open('tools/all_artifact_tokens.json', 'w', encoding='utf-8') as f:
        json.dump(sorted_words, f, ensure_ascii=False, indent=2)
    print(f"Dumped {len(sorted_words)} distinct tokens to tools/all_artifact_tokens.json")

if __name__ == '__main__':
    dump()
