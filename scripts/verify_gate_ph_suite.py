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
    print(f"Total gate_ph tests in manifest: {len(gate_ph_tests)}")

    assert not any((t.get("test_id") == "gate_ph_pyq_2025" or t.get("testId") == "gate_ph_pyq_2025") for t in gate_ph_tests), "Fake 2025 paper still present in manifest!"

    for t in gate_ph_tests:
        tid = t.get("test_id") or t.get("testId")
        rel_path = t.get("path")
        assert os.path.exists(rel_path), f"File {rel_path} for test {tid} does not exist on disk!"

        with open(rel_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        questions = data.get("questions", [])
        assert len(questions) == t.get("total_questions"), f"Count mismatch in {tid}: manifest says {t.get('total_questions')}, file has {len(questions)}"
        print(f"  [OK] {tid}: {len(questions)} questions in {rel_path}")

        if "pyq" in tid:
            marks = sum(q.get("marks", q.get("positiveMarks", 0)) for q in questions)
            print(f"       Marks sum: {marks}")
            assert abs(marks - 100.0) < 1e-4, f"Marks sum for {tid} is {marks}, expected 100.0"

    # 3. Assert fake file deleted from disk
    assert not os.path.exists("tests/gate/gate_ph/pyq/gate_ph_pyq_2025.json"), "gate_ph_pyq_2025.json still exists on disk!"

    print("\nALL GATE PH TESTS AND MANIFEST AUDIT PASSED WITH 100% SUCCESS!")

if __name__ == "__main__":
    verify()
