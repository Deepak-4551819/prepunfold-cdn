# -*- coding: utf-8 -*-
"""
Master Generator for GATE PH Full Length Mock Tests 03 to 12.
Generates 10 complete mock tests (Mock 03 to Mock 12), each with:
- Exactly 65 questions
- Exactly 100.0 marks (Q1-Q5: 1m, Q6-Q10: 2m, Q11-Q35: 1m, Q36-Q65: 2m)
- Sections: General Aptitude (10 Qs, 15 marks), Physics (55 Qs, 85 marks)
- Full bilingual English and Hindi for all questions, options, and explanations
- Complete step-by-step mathematical derivations with proper LaTeX
- Diverse question types: MCQ (with negative marking), MSQ (no negative), NAT (no negative)
- Full syllabus coverage across all 9 GATE Physics domains with zero question repetition.
"""

import json
import os
import sys

from mock_modules.ga_generator import get_ga_questions
from mock_modules.physics_1m_generator import get_physics_1m_questions
from mock_modules.physics_2m_generator import get_physics_2m_questions

def build_mock_suite():
    out_dir = os.path.join("tests", "gate", "gate_ph", "mock_tests")
    os.makedirs(out_dir, exist_ok=True)

    print("Building GATE PH Mock Suite (Mock 03 to Mock 12)...")
    generated_files = []

    for t in range(3, 13):
        ga = get_ga_questions(t)
        p1 = get_physics_1m_questions(t)
        p2 = get_physics_2m_questions(t)

        all_q = ga + p1 + p2
        assert len(all_q) == 65, f"Test {t} must have 65 questions, got {len(all_q)}"

        total_marks = 0.0
        for idx, q in enumerate(all_q, 1):
            assert q["questionNumber"] == idx, f"Test {t} Q{idx} number mismatch"
            assert q["questionTextEn"], f"Missing questionTextEn in Mock {t} Q{idx}"
            assert q["questionTextHi"], f"Missing questionTextHi in Mock {t} Q{idx}"
            assert q["explanationEn"], f"Missing explanationEn in Mock {t} Q{idx}"
            assert q["explanationHi"], f"Missing explanationHi in Mock {t} Q{idx}"
            total_marks += q["positiveMarks"]

        assert abs(total_marks - 100.0) < 1e-4, f"Test {t} total marks must be 100.0, got {total_marks}"

        tid = f"gate_ph_mock_{t:02d}"
        title_en = f"GATE Physics (PH) Full Length Mock Test {t:02d}"
        title_hi = f"GATE भौतिकी (PH) संपूर्ण मॉक टेस्ट {t:02d}"

        test_data = {
            "testId": tid,
            "categoryId": "gate_ph",
            "test_id": tid,
            "category_id": "gate_ph",
            "title": title_en,
            "titleEn": title_en,
            "titleHi": title_hi,
            "testType": "MOCK",
            "test_type": "MOCK",
            "isFree": True,
            "is_free": True,
            "durationMinutes": 180,
            "duration_minutes": 180,
            "totalQuestions": 65,
            "total_questions": 65,
            "maxMarks": 100.0,
            "positiveMarks": 2.0,
            "negativeMarks": 0.33,
            "examYear": 2025,
            "shiftBadge": f"GATE PH • Full Mock Test {t:02d}",
            "sections": [
                {
                    "sectionId": "sec_ga",
                    "sectionTitle": "General Aptitude",
                    "sectionTitleEn": "General Aptitude",
                    "sectionTitleHi": "सामान्य अभिरुचि",
                    "questionCount": 10,
                    "totalMarks": 15.0
                },
                {
                    "sectionId": "sec_ph",
                    "sectionTitle": "Physics",
                    "sectionTitleEn": "Physics",
                    "sectionTitleHi": "भौतिकी",
                    "questionCount": 55,
                    "totalMarks": 85.0
                }
            ],
            "questions": all_q
        }

        out_file = os.path.join(out_dir, f"{tid}.json")
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(test_data, f, ensure_ascii=False, indent=2)

        file_size = os.path.getsize(out_file)
        print(f"Generated {out_file} ({file_size} bytes, 65 Qs, 100.0 marks)")
        generated_files.append(out_file)

    print(f"\nSuccessfully generated all {len(generated_files)} mock tests (Mock 03 to 12)!")

if __name__ == "__main__":
    build_mock_suite()
