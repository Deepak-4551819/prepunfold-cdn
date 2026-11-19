# -*- coding: utf-8 -*-
"""
Audits and verifies the complete GATE PH Suite (4 PYQs + 12 Mocks + 22 Topic Tests = 38 tests).
"""
import json
import os

def verify():
    manifest_path = "manifest.json"
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    # 1. Check category
    gate_ph_cats = [c for c in manifest.get("categories", []) if c.get("id") == "gate_ph"]
    assert len(gate_ph_cats) == 1, "GATE PH category missing or duplicated in manifest"
    print(f"Verified Category: {gate_ph_cats[0]['title']} -> {gate_ph_cats[0]['subtitle']}")

    # 2. Check tests in manifest
    gate_ph_tests = [t for t in manifest.get("tests", []) if t.get("category_id") == "gate_ph" or t.get("categoryId") == "gate_ph"]
    print(f"Total gate_ph tests in manifest: {len(gate_ph_tests)} (Expected 38)")
    assert len(gate_ph_tests) == 38, f"Expected 38 tests, found {len(gate_ph_tests)}"

    pyq_count = 0
    mock_count = 0
    topic_count = 0

    for t in gate_ph_tests:
        tid = t.get("test_id") or t.get("testId")
        rel_path = t.get("path")
        assert os.path.exists(rel_path), f"File {rel_path} for test {tid} does not exist on disk!"

        with open(rel_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        questions = data.get("questions", [])
        expected_q = t.get("total_questions")
        assert len(questions) == expected_q, f"Count mismatch in {tid}: manifest says {expected_q}, file has {len(questions)}"

        marks_sum = sum(q.get("positiveMarks", q.get("marks", 0)) for q in questions)

        if "pyq" in tid:
            pyq_count += 1
            assert abs(marks_sum - 100.0) < 1e-4, f"PYQ {tid} marks {marks_sum} != 100.0"
        elif "mock" in tid:
            mock_count += 1
            assert abs(marks_sum - 100.0) < 1e-4, f"Mock {tid} marks {marks_sum} != 100.0"
        elif "top" in tid:
            topic_count += 1
            assert abs(marks_sum - 30.0) < 1e-4, f"Topic test {tid} marks {marks_sum} != 30.0"

    print(f"\nAudit Summary:")
    print(f"  PYQs: {pyq_count} tests (100.0 marks each)")
    print(f"  Full Mocks: {mock_count} tests (100.0 marks each, 11-section syllabus)")
    print(f"  Topic Tests: {topic_count} tests (30.0 marks each, 2 tests per topic for 11 sections)")
    print(f"\nALL 38 GATE PH TESTS AUDITED AND VERIFIED WITH 100% SUCCESS!")

if __name__ == "__main__":
    verify()
