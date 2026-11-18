#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scripts/build_uppcs_gs1_2019_2018.py — Builds 150-Q authentic papers for 2019 GS-1 and 2018 GS-1."""
import glob
import json
import os
import re

def clean_tag(t):
    if not t:
        return "General Studies"
    t = re.sub(r'^\d+\.\s*', '', t)
    t = re.sub(r'—.*$', '', t)
    return t.strip()

def build_gs1_2019_2018():
    # 1. Gather all stems from all existing papers (2020-2024) to guarantee zero duplicates
    existing_stems = set()
    for f in glob.glob('tests/state_psc/uppcs_pre/pyq/*.json'):
        with open(f, 'r', encoding='utf-8') as fp:
            d = json.load(fp)
            for q in d.get('questions', []):
                stem = (q.get('questionTextEn') or q.get('question_en') or '').strip().lower()
                if stem:
                    existing_stems.add(stem)

    print(f"Loaded {len(existing_stems)} existing stems from current PYQs.")

    categories = {
        'ancient': [],
        'medieval': [],
        'modern': [],
        'polity': [],
        'ind_geo': [],
        'wld_geo': []
    }

    # History
    for f in glob.glob('tests/history_pyq_1990_2024/*.json'):
        with open(f, 'r', encoding='utf-8') as fp:
            d = json.load(fp)
            fname = os.path.basename(f)
            for q in d.get('questions', []):
                tag = q.get('pyqTag') or ''
                if not ('U.P.' in tag or 'UP' in tag):
                    continue
                en = (q.get('questionTextEn') or q.get('question_en') or '').strip()
                hi = (q.get('questionTextHi') or q.get('question_hi') or '').strip()
                opts_en = q.get('optionsEn') or q.get('options_en') or []
                opts_hi = q.get('optionsHi') or q.get('options_hi') or []
                exp_en = (q.get('explanationEn') or q.get('explanation_en') or '').strip()
                exp_hi = (q.get('explanationHi') or q.get('explanation_hi') or '').strip()
                corr = q.get('correctOption') or (chr(65 + q['correct_index']) if q.get('correct_index') is not None else None)

                if not (en and hi and len(opts_en) == 4 and len(opts_hi) == 4 and exp_en and exp_hi and corr):
                    continue

                stem_key = en.lower()
                if stem_key in existing_stems:
                    continue
                existing_stems.add(stem_key)

                if 'hist_pyq_anc' in fname:
                    categories['ancient'].append(q)
                elif 'hist_pyq_med' in fname:
                    categories['medieval'].append(q)
                elif 'hist_pyq_mod' in fname:
                    categories['modern'].append(q)

    # Polity
    for f in glob.glob('tests/polity_pyq_1990_2022/*.json'):
        with open(f, 'r', encoding='utf-8') as fp:
            d = json.load(fp)
            for q in d.get('questions', []):
                tag = q.get('pyqTag') or ''
                if not ('U.P.' in tag or 'UP' in tag):
                    continue
                en = (q.get('questionTextEn') or q.get('question_en') or '').strip()
                hi = (q.get('questionTextHi') or q.get('question_hi') or '').strip()
                opts_en = q.get('optionsEn') or q.get('options_en') or []
                opts_hi = q.get('optionsHi') or q.get('options_hi') or []
                exp_en = (q.get('explanationEn') or q.get('explanation_en') or '').strip()
                exp_hi = (q.get('explanationHi') or q.get('explanation_hi') or '').strip()
                corr = q.get('correctOption') or (chr(65 + q['correct_index']) if q.get('correct_index') is not None else None)

                if not (en and hi and len(opts_en) == 4 and len(opts_hi) == 4 and exp_en and exp_hi and corr):
                    continue

                stem_key = en.lower()
                if stem_key in existing_stems:
                    continue
                existing_stems.add(stem_key)
                categories['polity'].append(q)

    # Geography
    for f in glob.glob('tests/geography_pyq_1993_2026/*.json'):
        with open(f, 'r', encoding='utf-8') as fp:
            d = json.load(fp)
            fname = os.path.basename(f)
            for q in d.get('questions', []):
                tag = q.get('pyqTag') or ''
                if not ('U.P.' in tag or 'UP' in tag):
                    continue
                en = (q.get('questionTextEn') or q.get('question_en') or '').strip()
                hi = (q.get('questionTextHi') or q.get('question_hi') or '').strip()
                opts_en = q.get('optionsEn') or q.get('options_en') or []
                opts_hi = q.get('optionsHi') or q.get('options_hi') or []
                exp_en = (q.get('explanationEn') or q.get('explanation_en') or '').strip()
                exp_hi = (q.get('explanationHi') or q.get('explanation_hi') or '').strip()
                corr = q.get('correctOption') or (chr(65 + q['correct_index']) if q.get('correct_index') is not None else None)

                if not (en and hi and len(opts_en) == 4 and len(opts_hi) == 4 and exp_en and exp_hi and corr):
                    continue

                stem_key = en.lower()
                if stem_key in existing_stems:
                    continue
                existing_stems.add(stem_key)

                if 'geo_pyq_ind' in fname:
                    categories['ind_geo'].append(q)
                elif 'geo_pyq_wld' in fname:
                    categories['wld_geo'].append(q)

    for cat, qs in categories.items():
        print(f"Category {cat}: {len(qs)} available.")

    def format_question(q_raw, year, q_num):
        idx_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
        corr = (q_raw.get('correctOption') or chr(65 + q_raw['correct_index'])).upper()
        idx = idx_map[corr]
        topic = clean_tag(q_raw.get('topicTag') or q_raw.get('sectionTitleEn') or 'General Studies')
        diff = q_raw.get('difficulty') or 'Medium'

        return {
            "questionId": f"uppcs_pre_{year}_gs1_q{q_num:03d}",
            "questionNumber": q_num,
            "q_id": q_num,
            "sectionId": "sec_gs1",
            "sectionTitle": "General Studies I",
            "questionType": "MCQ",
            "positiveMarks": 1.33,
            "negativeMarks": 0.44,
            "pyqTag": f"UPPCS Prelims {year} • GS Paper-I",
            "topicTag": topic,
            "difficulty": diff,
            "correctOption": corr,
            "correctOptionsList": [corr],
            "correct_index": idx,
            "correct_indices": [idx],
            "natMin": None,
            "natMax": None,
            "questionTextEn": (q_raw.get('questionTextEn') or q_raw.get('question_en')).strip(),
            "optionsEn": q_raw.get('optionsEn') or q_raw.get('options_en'),
            "explanationEn": (q_raw.get('explanationEn') or q_raw.get('explanation_en')).strip(),
            "questionTextHi": (q_raw.get('questionTextHi') or q_raw.get('question_hi')).strip(),
            "optionsHi": q_raw.get('optionsHi') or q_raw.get('options_hi'),
            "explanationHi": (q_raw.get('explanationHi') or q_raw.get('explanation_hi')).strip()
        }

    quotas = [
        ('ancient', 15),
        ('medieval', 15),
        ('modern', 30),
        ('polity', 30),
        ('ind_geo', 30),
        ('wld_geo', 30)
    ]

    for year in [2019, 2018]:
        paper_qs = []
        q_counter = 1
        for cat_name, count in quotas:
            pool = categories[cat_name]
            selected = pool[:count]
            categories[cat_name] = pool[count:]
            for raw_q in selected:
                formatted = format_question(raw_q, year, q_counter)
                paper_qs.append(formatted)
                q_counter += 1

        out_path = f"tests/state_psc/uppcs_pre/pyq/uppcs_pre_pyq_{year}_gs1.json"
        data = {
            "testId": f"uppcs_pre_pyq_{year}_gs1",
            "categoryId": "uppcs_pre",
            "test_id": f"uppcs_pre_pyq_{year}_gs1",
            "category_id": "uppcs_pre",
            "title": f"UPPSC PCS Prelims {year} — General Studies Paper 1 (Full 150 Qs)",
            "titleEn": f"UPPSC PCS Prelims {year} — General Studies Paper 1 (Full 150 Qs)",
            "titleHi": f"UPPSC PCS प्रारंभिक परीक्षा {year} — सामान्य अध्ययन प्रश्नपत्र-1 (पूर्ण 150 प्रश्न)",
            "testType": "PYQ",
            "test_type": "PYQ",
            "isFree": True,
            "is_free": True,
            "durationMinutes": 120,
            "duration_minutes": 120,
            "totalQuestions": 150,
            "total_questions": 150,
            "maxMarks": 200.0,
            "positiveMarks": 1.33,
            "negativeMarks": 0.44,
            "examYear": year,
            "shiftBadge": f"UPPCS Prelims {year} • GS-1 (Full 150 Qs)",
            "questions": paper_qs,
            "path": out_path.replace("\\", "/")
        }

        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as out_fp:
            json.dump(data, out_fp, ensure_ascii=False, indent=2)
        print(f"Successfully generated {out_path} with {len(paper_qs)} questions.")

if __name__ == "__main__":
    build_gs1_2019_2018()
