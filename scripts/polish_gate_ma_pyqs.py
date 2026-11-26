# -*- coding: utf-8 -*-
import os, sys, json
from collections import OrderedDict

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Topic mappings for previously generic questions
TOPIC_MAP = {
    2022: {
        11: "Linear Algebra",
        14: "Complex Analysis",
        18: "Numerical Analysis",
        29: "Complex Analysis",
        30: "Numerical Analysis",
        31: "Calculus",
        32: "Calculus",
        38: "Real Analysis",
        39: "Real Analysis",
        40: "Real Analysis",
        42: "Functional Analysis",
        44: "Numerical Analysis",
        45: "Calculus",
        50: "Complex Analysis",
        51: "Functional Analysis",
        57: "Linear Programming",
        59: "Calculus",
        60: "Calculus",
    },
    2023: {
        13: "Real Analysis",
        19: "Linear Algebra",
        23: "Functional Analysis",
        26: "Partial Differential Equations",
        28: "Numerical Analysis",
        30: "Calculus",
        31: "Calculus",
        35: "Linear Algebra",
        38: "Functional Analysis",
        49: "Ordinary Differential Equations",
        50: "Numerical Analysis",
        51: "Numerical Analysis",
        53: "Topology",
        55: "Calculus",
    },
    2024: {
        14: "Real Analysis",
        23: "Partial Differential Equations",
        26: "Calculus",
        27: "Algebra",
        32: "Numerical Analysis",
        33: "Numerical Analysis",
        35: "Calculus",
        37: "Complex Analysis",
        46: "Partial Differential Equations",
        47: "Functional Analysis",
        54: "Calculus",
        64: "Calculus",
    },
    2025: {
        17: "Functional Analysis",
        18: "Calculus",
        21: "Complex Analysis",
        25: "Linear Programming",
        26: "Calculus",
        30: "Calculus",
        34: "Numerical Analysis",
        37: "Ordinary Differential Equations",
        38: "Ordinary Differential Equations",
        39: "Calculus",
        40: "Partial Differential Equations",
        46: "Topology",
        65: "Topology",
    },
    2026: {
        12: "Calculus",
        20: "Topology",
        27: "Ordinary Differential Equations",
        30: "Numerical Analysis",
        31: "Real Analysis",
        32: "Functional Analysis",
        34: "Topology",
        56: "Calculus",
        64: "Calculus",
    }
}

EXPECTED_21_TOP_KEYS = [
    'testId', 'categoryId', 'test_id', 'category_id', 'title', 'titleEn',
    'testType', 'test_type', 'isFree', 'is_free', 'durationMinutes', 'duration_minutes',
    'totalQuestions', 'total_questions', 'maxMarks', 'positiveMarks', 'negativeMarks',
    'examYear', 'shiftBadge', 'sections', 'questions'
]

def polish_gate_ma():
    for y in [2022, 2023, 2024, 2025, 2026]:
        p = f'tests/gate/gate_ma/pyq/gate_ma_pyq_{y}.json'
        with open(p, 'r', encoding='utf-8') as f:
            d = json.load(f)

        # 1. Update questions
        for q in d['questions']:
            qnum = q['questionNumber']

            # Fix 2023 Q06 MTA negativeMarks
            if y == 2023 and qnum == 6:
                q['negativeMarks'] = 0.0
                print("✓ 2023 Q6 negativeMarks set to 0.0 (MTA)")

            # Fix 2025 Q06 double-escaped quotes
            if y == 2025 and qnum == 6:
                qtext = q['questionTextEn']
                qtext_clean = qtext.replace(r'\"', '"')
                q['questionTextEn'] = qtext_clean
                print("✓ 2025 Q6 questionTextEn double-escaped quotes cleaned")

            # Update generic topicTag
            if y in TOPIC_MAP and qnum in TOPIC_MAP[y]:
                q['topicTag'] = TOPIC_MAP[y][qnum]

        # 2. Build clean 21 top-level keys
        clean_d = OrderedDict()
        for k in EXPECTED_21_TOP_KEYS:
            if k in d:
                clean_d[k] = d[k]

        assert len(clean_d.keys()) == 21, f"{y} expected 21 keys, got {len(clean_d.keys())}: {list(clean_d.keys())}"

        with open(p, 'w', encoding='utf-8') as f:
            json.dump(clean_d, f, ensure_ascii=False, indent=2)

        print(f"✓ {y}: Saved with strict 21-key top-level schema (stripped titleHi, exam_year_tag, examYearTag)")

    print("All 5 GATE MA PYQ papers polished successfully!")

if __name__ == '__main__':
    polish_gate_ma()
