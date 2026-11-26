import json
import os
import re

TESTS_DIR = "tests/tgt_pgt_history"
ARTIFACT_CHAR_SET = set("uee@ kewâ cesÙ fह् ™ ० å ä ø § ° ^ @ æ ®".split())
ARTIFACT_CHARS = set("™०åäø§°^@æ®")
# Also KrutiDev patterns
KRUTI_PAT = re.compile(r'uee@|kewâ|cesÙ|fह्|[™०åäø§°\^@æ®]')

def get_artifact_words():
    files = sorted([f for f in os.listdir(TESTS_DIR) if f.startswith('tgt_pgt_hist_ch') and f.endswith('.json')])
    words_found = {}

    for fname in files:
        fpath = os.path.join(TESTS_DIR, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for q in data.get('questions', []):
            qn = q.get('questionNumber')
            texts = [str(q.get('questionTextHi') or ''), str(q.get('explanationHi') or '')]
            texts.extend([str(o) for o in q.get('optionsHi', [])])

            for text in texts:
                for match in KRUTI_PAT.finditer(text):
                    # extract the surrounding word
                    start = max(0, match.start() - 15)
                    end = min(len(text), match.end() + 15)
                    full_token = text[start:end]
                    # Also get whitespace delimited token
                    token_m = re.search(r'\S*(' + KRUTI_PAT.pattern + r')\S*', text[max(0, match.start()-20):min(len(text), match.end()+20)])
                    tok = token_m.group(0) if token_m else match.group(0)
                    words_found[tok] = words_found.get(tok, 0) + 1

    print(f"Total distinct artifact word contexts found: {len(words_found)}")
    sorted_words = sorted(words_found.items(), key=lambda x: -x[1])
    for w, count in sorted_words[:80]:
        print(f"  {w!r:<30}: {count}")

if __name__ == '__main__':
    get_artifact_words()
