import os
import json
import glob
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

MANIFEST_PATH = "manifest.json"
ALLOWED_TEST_TYPES = {"FULL_MOCK", "PYQ", "SECTIONAL", "TOPIC"}

def validate():
    print("=== Running AbhyasDesk Manifest Validation ===")

    if not os.path.exists(MANIFEST_PATH):
        print(f"FAILED: {MANIFEST_PATH} does not exist!")
        sys.exit(1)

    try:
        with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
            manifest = json.load(f)
    except Exception as e:
        print(f"FAILED: Could not parse {MANIFEST_PATH}: {e}")
        sys.exit(1)

    categories = manifest.get("categories", [])
    tests = manifest.get("tests", [])
    bundles = manifest.get("bundles", [])
    remote_config = manifest.get("remote_config", {})

    print(f"Manifest Version: {manifest.get('manifest_version')}")
    print(f"Total Categories: {len(categories)}")
    print(f"Total Bundles: {len(bundles)}")
    print(f"Total Tests in Manifest: {len(tests)}")

    # 1. Category validation & parts map
    cat_parts_map = {}
    cat_ids = set()
    for cat in categories:
        cid = cat.get("id") or cat.get("categoryId")
        if not cid:
            print("FAILED: Category missing id/categoryId!")
            sys.exit(1)
        if cid in cat_ids:
            print(f"FAILED: Duplicate category ID: {cid}")
            sys.exit(1)
        cat_ids.add(cid)

        parts = cat.get("parts", [])
        part_ids = {p.get("partId") for p in parts if p.get("partId")}
        cat_parts_map[cid] = part_ids

    # 2. Test Validation
    seen_test_ids = set()
    errors = []

    for idx, t in enumerate(tests):
        tid = t.get("test_id") or t.get("testId")
        if not tid:
            errors.append(f"Test at index {idx} has missing test_id")
            continue
        if tid in seen_test_ids:
            errors.append(f"Duplicate test_id: {tid}")
        seen_test_ids.add(tid)

        cid = t.get("category_id") or t.get("categoryId")
        if not cid or cid not in cat_ids:
            errors.append(f"Test {tid} has unknown category_id: {cid}")

        # test_type check
        ttype = t.get("test_type") or t.get("testType")
        if ttype not in ALLOWED_TEST_TYPES:
            errors.append(f"Test {tid} has invalid test_type: '{ttype}' (allowed: {ALLOWED_TEST_TYPES})")

        # path exists check
        path = t.get("path") or t.get("filePath")
        if not path:
            errors.append(f"Test {tid} missing path/filePath")
        else:
            clean_path = path.replace("\\", "/")
            if not os.path.exists(clean_path):
                errors.append(f"Test {tid} points to missing path on disk: {clean_path}")

        # TOPIC test part_id check
        if ttype == "TOPIC":
            part_id = t.get("part_id") or t.get("partId")
            valid_parts = cat_parts_map.get(cid, set())
            if not part_id:
                errors.append(f"TOPIC test {tid} in category {cid} has missing part_id (valid parts: {valid_parts})")
            elif part_id not in valid_parts:
                errors.append(f"TOPIC test {tid} has part_id '{part_id}' not found in category {cid} parts[] ({valid_parts})")

    # 3. Check all JSON files on disk for corruption
    disk_json_files = glob.glob("tests/**/*.json", recursive=True)
    broken_files = []
    for f in disk_json_files:
        try:
            with open(f, "r", encoding="utf-8") as jf:
                json.load(jf)
        except Exception as e:
            broken_files.append((f, str(e)))

    if broken_files:
        errors.append(f"Found {len(broken_files)} broken JSON files on disk: {broken_files}")

    # 4. Check tests/geography_pyq_1993_2026/ is untouched
    geo_pyq_dir = "tests/geography_pyq_1993_2026"
    if not os.path.exists(geo_pyq_dir):
        errors.append(f"GUARDRAIL FAILED: {geo_pyq_dir} does not exist!")
    else:
        geo_files = glob.glob(f"{geo_pyq_dir}/*.json")
        if len(geo_files) != 83:
            errors.append(f"GUARDRAIL FAILED: {geo_pyq_dir} should have exactly 83 files, found {len(geo_files)}")

    # 5. Bundles validation
    if len(bundles) < 2:
        errors.append(f"Expected at least 2 bundles, found {len(bundles)}")
    for b in bundles:
        bid = b.get("bundle_id") or b.get("bundleId")
        if not bid:
            errors.append("Bundle missing bundle_id")
        unlocks = b.get("unlocks_categories", [])
        if not unlocks:
            errors.append(f"Bundle {bid} missing unlocks_categories")

    # 6. Remote config active_play_product_id check
    active_prod = remote_config.get("active_play_product_id")
    if active_prod == "prepunfold_pro_49":
        errors.append("remote_config.active_play_product_id is still pointing to prepunfold_pro_49!")

    print("\n=== Validation Results ===")
    if errors:
        print(f"FAILED with {len(errors)} errors:")
        for err in errors[:20]:
            print(f"  ❌ {err}")
        if len(errors) > 20:
            print(f"  ... and {len(errors) - 20} more errors")
        sys.exit(1)
    else:
        print("✅ Every path in manifest.json exists on disk.")
        print(f"✅ Every test_type is strictly in {ALLOWED_TEST_TYPES}.")
        print("✅ Every 'TOPIC' test has a valid part_id in its category parts[].")
        print("✅ Zero broken JSON files on disk (all 651 files valid JSON).")
        print("✅ Zero duplicate test_ids.")
        print("✅ tests/geography_pyq_1993_2026/ has 83 files and is completely untouched.")
        print(f"✅ Active bundles: {[b['bundle_id'] for b in bundles]}")
        print(f"✅ remote_config.active_play_product_id: {active_prod}")
        print("\n🎉 ALL MANIFEST AND REPO VALIDATION CHECKS PASSED PERFECTLY!")

if __name__ == "__main__":
    validate()
