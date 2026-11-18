#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import glob
import json

def verify():
    files = sorted(glob.glob('tests/state_psc/uppcs_pre/pyq/*.json'))
    print(f"Total PYQ files found: {len(files)}")
    global_stems = {}
    total_q_count = 0

    for f in files:
        with open(f, 'r', encoding='utf-8') as fp:
            d = json.load(fp)
        qs = d.get('questions', [])
        tot = d.get('totalQuestions') or d.get('total_questions')
        tid = d.get('testId')
        stems = set()
        dups = 0
        missing = 0
        for q in qs:
            total_q_count += 1
            en = (q.get('questionTextEn') or q.get('question_en') or '').strip()
            hi = (q.get('questionTextHi') or q.get('question_hi') or '').strip()
            corr = q.get('correctOption') or q.get('correct_index')
            if not en or not hi or corr is None:
                missing += 1
            low = en.lower()
            if low in stems:
                dups += 1
            stems.add(low)
            global_stems.setdefault(low, []).append(tid)

        print(f"{tid:<26} | Qs: {len(qs):>3}/{tot} | Unique: {len(stems):>3} | Dups: {dups} | Missing: {missing}")

    print("-" * 65)
    print(f"Total Questions Verified across all 10 papers: {total_q_count}")

if __name__ == '__main__':
    verify()
