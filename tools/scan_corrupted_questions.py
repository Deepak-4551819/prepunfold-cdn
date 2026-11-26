import os
import json
import re

TESTS_DIR = "tests/tgt_pgt_history"

ARTIFACT_PATTERNS = [
    r'uee@', r'kewâ', r'cesÙ', r'fह्',
    r'[™०åäø§°\^@æ®]'
]
ARTIFACT_REGEX = re.compile('|'.join(ARTIFACT_PATTERNS))

def detect_artifacts(text):
    if not text:
        return []
    return ARTIFACT_REGEX.findall(str(text))

def scan_all_30_chapters():
    files = sorted([f for f in os.listdir(TESTS_DIR) if f.startswith('tgt_pgt_hist_ch') and f.endswith('.json')])
    summary = []

    for fname in files:
        fpath = os.path.join(TESTS_DIR, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        questions = data.get('questions', [])
        total_q = len(questions)
        flagged_count = 0
        reasons_breakdown = {
            'legacy_artifacts': 0,
            'empty_options': 0,
            'untranslated_q': 0,
            'untranslated_opts': 0,
            'spillover': 0
        }

        for idx, q in enumerate(questions, 1):
            q_num = q.get('questionNumber', idx)
            is_flagged = False

            # Check Hindi fields
            q_hi = str(q.get('questionTextHi') or q.get('question_hi') or '')
            opts_hi = q.get('optionsHi') or q.get('options_hi') or []
            exp_hi = str(q.get('explanationHi') or q.get('explanation_hi') or '')

            # Check English fields
            q_en = str(q.get('questionTextEn') or q.get('question_en') or '')
            opts_en = q.get('optionsEn') or q.get('options_en') or []

            # 1. Legacy artifacts
            art_q = detect_artifacts(q_hi)
            art_exp = detect_artifacts(exp_hi)
            art_opts = []
            for o in opts_hi:
                art_opts.extend(detect_artifacts(str(o)))

            if art_q or art_exp or art_opts:
                reasons_breakdown['legacy_artifacts'] += 1
                is_flagged = True

            # 2. Empty options
            if len(opts_hi) < 4 or any(not str(o).strip() for o in opts_hi) or len(opts_en) < 4 or any(not str(o).strip() for o in opts_en):
                reasons_breakdown['empty_options'] += 1
                is_flagged = True

            # 3. Untranslated English fields
            if q_hi and q_en and q_hi.strip() == q_en.strip():
                reasons_breakdown['untranslated_q'] += 1
                is_flagged = True

            if opts_hi and opts_en:
                if [str(o).strip() for o in opts_hi] == [str(o).strip() for o in opts_en]:
                    reasons_breakdown['untranslated_opts'] += 1
                    is_flagged = True

            # 4. Spillover
            if 'ch25' in fname and q_num in [1, 2]:
                if 'बांडुंग' in q_hi or 'द्वितीय संशोधन' in q_hi:
                    reasons_breakdown['spillover'] += 1
                    is_flagged = True

            if is_flagged:
                flagged_count += 1

        clean_count = total_q - flagged_count
        summary.append({
            'file': fname,
            'total': total_q,
            'clean': clean_count,
            'flagged': flagged_count,
            'reasons': reasons_breakdown
        })

    return summary

def main():
    results = scan_all_30_chapters()
    header = f"{'Ch':<4} | {'Chapter File':<48} | {'Total':<6} | {'Clean':<6} | {'Corrupted':<10} | {'Status'}"
    sep = "-" * len(header)
    print(sep)
    print(header)
    print(sep)
    total_q = 0
    clean_q = 0
    flagged_q = 0
    for idx, r in enumerate(results, 1):
        st = "CLEAN" if r['flagged'] == 0 else f"FLAGGED ({r['flagged']})"
        line = f"Ch{idx:02d} | {r['file']:<48} | {r['total']:<6} | {r['clean']:<6} | {r['flagged']:<10} | {st}"
        print(line)
        total_q += r['total']
        clean_q += r['clean']
        flagged_q += r['flagged']
    print(sep)
    print(f"{'TOTAL':<4} | {'ALL 30 CHAPTERS':<48} | {total_q:<6} | {clean_q:<6} | {flagged_q:<10} | {'ALL CLEAN' if flagged_q == 0 else 'NEEDS REMEDIATION'}")
    print(sep)

if __name__ == '__main__':
    main()
