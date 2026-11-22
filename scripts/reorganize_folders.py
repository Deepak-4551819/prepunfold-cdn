import os
import shutil
import json
import glob

BASE_CDN_URL = "https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main"
ALT_CDN_URL = "https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main"

def update_json_file(file_path, new_rel_path, new_test_type=None, part_id=None):
    # Guardrail 1: Never touch tests/geography_pyq_1993_2026/
    if "geography_pyq_1993_2026" in file_path.replace("\\", "/"):
        raise RuntimeError(f"GUARDRAIL VIOLATION: Tried to touch {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    clean_path = new_rel_path.replace("\\", "/")

    # Update paths and URLs if they exist or update them standardly
    if "path" in data or "filePath" in data or "file_path" in data:
        data["path"] = clean_path
        data["filePath"] = clean_path
        data["file_path"] = clean_path

    if "json_url" in data or "cdnUrl" in data or "altCdnUrl" in data:
        data["json_url"] = f"{BASE_CDN_URL}/{clean_path}"
        data["cdnUrl"] = f"{BASE_CDN_URL}/{clean_path}"
        data["altCdnUrl"] = f"{ALT_CDN_URL}/{clean_path}"

    if new_test_type:
        data["test_type"] = new_test_type
        data["testType"] = new_test_type

    if part_id:
        data["part_id"] = part_id
        data["partId"] = part_id

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def move_file_and_update(src_path, dst_path, new_test_type=None, part_id=None):
    src_clean = src_path.replace("\\", "/")
    dst_clean = dst_path.replace("\\", "/")

    if "geography_pyq_1993_2026" in src_clean or "geography_pyq_1993_2026" in dst_clean:
        raise RuntimeError("GUARDRAIL VIOLATION: Touched geography_pyq_1993_2026")

    os.makedirs(os.path.dirname(dst_clean), exist_ok=True)
    if os.path.abspath(src_clean) != os.path.abspath(dst_clean):
        shutil.move(src_clean, dst_clean)

    update_json_file(dst_clean, dst_clean, new_test_type, part_id)

def main():
    print("=== Step 1: Reorganizing folders and test files ===")

    # 1. tgt_pgt_economics
    econ_base = "tests/teaching/tgt_pgt_economics"

    # 1a. chapter_tests -> topic_tests
    old_econ_ch = f"{econ_base}/chapter_tests"
    new_econ_top = f"{econ_base}/topic_tests"
    if os.path.exists(old_econ_ch):
        os.makedirs(new_econ_top, exist_ok=True)
        for f in glob.glob(f"{old_econ_ch}/*.json"):
            dst = os.path.join(new_econ_top, os.path.basename(f)).replace("\\", "/")
            # assign part_id
            fname = os.path.basename(f)
            # ch01-ch06: microeconomics
            # ch07-ch08: macroeconomics
            # ch09-ch13: public_finance
            # ch14-ch18: money_banking
            # ch19-ch22: international_trade
            # ch23-ch31: indian_economy
            ch_num = int(fname.split("_ch")[1][:2])
            if ch_num <= 6:
                part = "microeconomics"
            elif ch_num <= 8:
                part = "macroeconomics"
            elif ch_num <= 13:
                part = "public_finance"
            elif ch_num <= 18:
                part = "money_banking"
            elif ch_num <= 22:
                part = "international_trade"
            else:
                part = "indian_economy"
            move_file_and_update(f, dst, "TOPIC", part)
        shutil.rmtree(old_econ_ch, ignore_errors=True)
        print(f"Moved Economics chapter tests to topic_tests.")

    # 1b. mock_tests -> full_mocks and sectional_tests
    econ_mock_dir = f"{econ_base}/mock_tests"
    if os.path.exists(econ_mock_dir):
        for f in glob.glob(f"{econ_mock_dir}/*.json"):
            fname = os.path.basename(f)
            if "full_length" in fname:
                dst = f"{econ_base}/full_mocks/{fname}"
                move_file_and_update(f, dst, "FULL_MOCK")
            else:
                dst = f"{econ_base}/sectional_tests/{fname}"
                move_file_and_update(f, dst, "SECTIONAL")
        shutil.rmtree(econ_mock_dir, ignore_errors=True)
        print(f"Split Economics mock_tests into full_mocks and sectional_tests.")

    # 1c. update economics pyq files test_type
    for f in glob.glob(f"{econ_base}/pyq/*.json"):
        f_clean = f.replace("\\", "/")
        update_json_file(f_clean, f_clean, "PYQ")

    # 2. tgt_pgt_geography
    geo_base = "tests/teaching/tgt_pgt_geography"

    # 2a. chapter_tests -> topic_tests
    old_geo_ch = f"{geo_base}/chapter_tests"
    new_geo_top = f"{geo_base}/topic_tests"
    if os.path.exists(old_geo_ch):
        os.makedirs(new_geo_top, exist_ok=True)
        for f in glob.glob(f"{old_geo_ch}/*.json"):
            dst = os.path.join(new_geo_top, os.path.basename(f)).replace("\\", "/")
            fname = os.path.basename(f)
            # ch01: geographical_thought
            # ch02-ch08: physical_geography
            # ch09-ch12: human_economic_geography
            # ch13-ch14: indian_geography
            # ch15: practical_cartography
            ch_num = int(fname.split("_ch")[1][:2])
            if ch_num == 1:
                part = "geographical_thought"
            elif ch_num <= 8:
                part = "physical_geography"
            elif ch_num <= 12:
                part = "human_economic_geography"
            elif ch_num <= 14:
                part = "indian_geography"
            else:
                part = "practical_cartography"
            move_file_and_update(f, dst, "TOPIC", part)
        shutil.rmtree(old_geo_ch, ignore_errors=True)
        print(f"Moved Geography chapter tests to topic_tests.")

    # 2b. mock_tests -> full_mocks and sectional_tests
    geo_mock_dir = f"{geo_base}/mock_tests"
    if os.path.exists(geo_mock_dir):
        for f in glob.glob(f"{geo_mock_dir}/*.json"):
            fname = os.path.basename(f)
            if "full_length" in fname:
                dst = f"{geo_base}/full_mocks/{fname}"
                move_file_and_update(f, dst, "FULL_MOCK")
            else:
                dst = f"{geo_base}/sectional_tests/{fname}"
                move_file_and_update(f, dst, "SECTIONAL")
        shutil.rmtree(geo_mock_dir, ignore_errors=True)
        print(f"Split Geography mock_tests into full_mocks and sectional_tests.")

    # 2c. update geography pyq files test_type
    for f in glob.glob(f"{geo_base}/pyq/*.json"):
        f_clean = f.replace("\\", "/")
        update_json_file(f_clean, f_clean, "PYQ")

    # 3. tgt_pgt_civics
    civics_base = "tests/teaching/tgt_pgt_civics"
    civ_mock_dir = f"{civics_base}/mock_tests"
    if os.path.exists(civ_mock_dir):
        for f in glob.glob(f"{civ_mock_dir}/*.json"):
            fname = os.path.basename(f)
            dst = f"{civics_base}/sectional_tests/{fname}"
            move_file_and_update(f, dst, "SECTIONAL")
        shutil.rmtree(civ_mock_dir, ignore_errors=True)
        print(f"Moved Civics mock_tests to sectional_tests.")
    for f in glob.glob(f"{civics_base}/pyq/*.json"):
        f_clean = f.replace("\\", "/")
        update_json_file(f_clean, f_clean, "PYQ")

    # 4. tgt_pgt_history
    history_base = "tests/teaching/tgt_pgt_history"
    hist_mock_dir = f"{history_base}/mock_tests"
    if os.path.exists(hist_mock_dir):
        for f in glob.glob(f"{hist_mock_dir}/*.json"):
            fname = os.path.basename(f)
            dst = f"{history_base}/sectional_tests/{fname}"
            move_file_and_update(f, dst, "SECTIONAL")
        shutil.rmtree(hist_mock_dir, ignore_errors=True)
        print(f"Moved Teaching History mock_tests to sectional_tests.")
    for f in glob.glob(f"{history_base}/pyq/*.json"):
        f_clean = f.replace("\\", "/")
        update_json_file(f_clean, f_clean, "PYQ")

    # 5. Remove legacy tests/teaching/tgt_pgt_econ_geo/
    legacy_dir = "tests/teaching/tgt_pgt_econ_geo"
    if os.path.exists(legacy_dir):
        shutil.rmtree(legacy_dir, ignore_errors=True)
        print(f"Removed legacy unused {legacy_dir}.")

    # 6. gate_ph
    gate_ph_base = "tests/gate/gate_ph"
    # mock_tests -> full_mocks
    if os.path.exists(f"{gate_ph_base}/mock_tests"):
        os.makedirs(f"{gate_ph_base}/full_mocks", exist_ok=True)
        for f in glob.glob(f"{gate_ph_base}/mock_tests/*.json"):
            fname = os.path.basename(f)
            dst = f"{gate_ph_base}/full_mocks/{fname}"
            move_file_and_update(f, dst, "FULL_MOCK")
        shutil.rmtree(f"{gate_ph_base}/mock_tests", ignore_errors=True)
        print(f"Moved GATE PH mock_tests to full_mocks.")
    # update pyqs
    for f in glob.glob(f"{gate_ph_base}/pyq/*.json"):
        f_clean = f.replace("\\", "/")
        update_json_file(f_clean, f_clean, "PYQ")
    # update topic_tests with part_id
    for f in glob.glob(f"{gate_ph_base}/topic_tests/**/*.json", recursive=True):
        f_clean = f.replace("\\", "/")
        # folder is e.g. 01_measurements_error_analysis
        part_name = f_clean.split("/topic_tests/")[1].split("/")[0]
        update_json_file(f_clean, f_clean, "TOPIC", part_name)
    print(f"Updated GATE PH topic tests and PYQs.")

    # 7. gate_ma, gate_cy
    for s in ["gate_ma", "gate_cy"]:
        b = f"tests/gate/{s}"
        if os.path.exists(f"{b}/mock_tests"):
            os.makedirs(f"{b}/full_mocks", exist_ok=True)
            for f in glob.glob(f"{b}/mock_tests/*.json"):
                fname = os.path.basename(f)
                dst = f"{b}/full_mocks/{fname}"
                move_file_and_update(f, dst, "FULL_MOCK")
            shutil.rmtree(f"{b}/mock_tests", ignore_errors=True)
            print(f"Moved {s} mock_tests to full_mocks.")

    # 8. jam_ph, jam_ma, jam_cy
    for s in ["jam_ph", "jam_ma", "jam_cy"]:
        b = f"tests/jam/{s}"
        if os.path.exists(f"{b}/mock_tests"):
            os.makedirs(f"{b}/full_mocks", exist_ok=True)
            for f in glob.glob(f"{b}/mock_tests/*.json"):
                fname = os.path.basename(f)
                dst = f"{b}/full_mocks/{fname}"
                move_file_and_update(f, dst, "FULL_MOCK")
            shutil.rmtree(f"{b}/mock_tests", ignore_errors=True)
            print(f"Moved {s} mock_tests to full_mocks.")

    # 9. ssc_gd, ssc_chsl
    for s in ["ssc_gd", "ssc_chsl"]:
        b = f"tests/ssc/{s}"
        if os.path.exists(f"{b}/mock_tests"):
            os.makedirs(f"{b}/full_mocks", exist_ok=True)
            for f in glob.glob(f"{b}/mock_tests/*.json"):
                fname = os.path.basename(f)
                dst = f"{b}/full_mocks/{fname}"
                move_file_and_update(f, dst, "FULL_MOCK")
            shutil.rmtree(f"{b}/mock_tests", ignore_errors=True)
            print(f"Moved {s} mock_tests to full_mocks.")

    # 10. rrb_ntpc
    b = "tests/railway/rrb_ntpc"
    if os.path.exists(f"{b}/mock_tests"):
        os.makedirs(f"{b}/full_mocks", exist_ok=True)
        for f in glob.glob(f"{b}/mock_tests/*.json"):
            fname = os.path.basename(f)
            dst = f"{b}/full_mocks/{fname}"
            move_file_and_update(f, dst, "FULL_MOCK")
        shutil.rmtree(f"{b}/mock_tests", ignore_errors=True)
        print("Moved rrb_ntpc mock_tests to full_mocks.")

    # 11. uppcs_pre
    uppcs_b = "tests/state_psc/uppcs_pre"
    if os.path.exists(f"{uppcs_b}/mock_tests"):
        os.makedirs(f"{uppcs_b}/sectional_tests", exist_ok=True)
        for f in glob.glob(f"{uppcs_b}/mock_tests/*.json"):
            fname = os.path.basename(f)
            dst = f"{uppcs_b}/sectional_tests/{fname}"
            move_file_and_update(f, dst, "SECTIONAL")
        shutil.rmtree(f"{uppcs_b}/mock_tests", ignore_errors=True)
        print("Moved uppcs_pre mock_tests to sectional_tests.")
    for f in glob.glob(f"{uppcs_b}/pyq/*.json"):
        f_clean = f.replace("\\", "/")
        update_json_file(f_clean, f_clean, "PYQ")

    # 12. upsc_cse
    upsc_b = "tests/upsc/upsc_cse"
    if os.path.exists(f"{upsc_b}/mock_tests"):
        os.makedirs(f"{upsc_b}/sectional_tests", exist_ok=True)
        for f in glob.glob(f"{upsc_b}/mock_tests/*.json"):
            fname = os.path.basename(f)
            dst = f"{upsc_b}/sectional_tests/{fname}"
            move_file_and_update(f, dst, "SECTIONAL")
        shutil.rmtree(f"{upsc_b}/mock_tests", ignore_errors=True)
        print("Moved upsc_cse mock_tests to sectional_tests.")
    # check upsc_cse_geo_pyq_ias_special_1.json in topic_tests
    sp1 = f"{upsc_b}/topic_tests/ind_01_intro_frontiers/upsc_cse_geo_pyq_ias_special_1.json"
    if os.path.exists(sp1):
        dst = f"{upsc_b}/sectional_tests/upsc_cse_geo_pyq_ias_special_1.json"
        move_file_and_update(sp1, dst, "SECTIONAL")
        print("Moved upsc_cse_geo_pyq_ias_special_1 to sectional_tests.")
    # update upsc_cse topic tests
    for f in glob.glob(f"{upsc_b}/topic_tests/**/*.json", recursive=True):
        f_clean = f.replace("\\", "/")
        part = "part1_indian_geography" if "ind_" in f_clean else "part2_world_geography"
        update_json_file(f_clean, f_clean, "TOPIC", part)

    # 13. current_affairs
    ca_b = "tests/current_affairs"
    ca_files = glob.glob(f"{ca_b}/*.json")
    if ca_files:
        os.makedirs(f"{ca_b}/full_mocks", exist_ok=True)
        os.makedirs(f"{ca_b}/sectional_tests", exist_ok=True)
        for f in ca_files:
            fname = os.path.basename(f)
            if "grand_mock" in fname:
                dst = f"{ca_b}/full_mocks/{fname}"
                move_file_and_update(f, dst, "FULL_MOCK")
            else:
                dst = f"{ca_b}/sectional_tests/{fname}"
                move_file_and_update(f, dst, "SECTIONAL")
        print("Organized current_affairs into full_mocks and sectional_tests.")

    # 14. Update polity, history, judiciary tests on disk
    for f in glob.glob("tests/polity_pyq_1990_2022/*.json"):
        f_clean = f.replace("\\", "/")
        update_json_file(f_clean, f_clean, "TOPIC", "part1_indian_polity_and_governance")

    for f in glob.glob("tests/history_pyq_1990_2024/*.json"):
        f_clean = f.replace("\\", "/")
        fname = os.path.basename(f)
        if "anc_" in fname:
            part = "part1_ancient_history"
        elif "med_" in fname:
            part = "part2_medieval_history"
        else:
            part = "part3_modern_history"
        update_json_file(f_clean, f_clean, "TOPIC", part)

    part_map_judiciary = {
        "cpc": "part1_cpc_1908",
        "crpc": "part2_crpc_1973",
        "evidence": "part3_evidence_1872",
        "ipc": "part4_ipc_1860",
        "constitution": "part5_constitution_of_india",
        "tpa": "part6_transfer_of_property_1882",
        "contract": "part7_indian_contract_act_1872",
        "tort": "part8_law_of_torts",
        "limitation": "part9_limitation_act_1963",
        "sra": "part10_specific_relief_act_1963",
        "trust_equity": "part11_law_of_trust_and_equity",
        "jurisprudence": "part12_jurisprudence",
        "international_org": "part13_international_organisations",
        "minor_acts": "part14_minor_acts"
    }
    for sub, pid in part_map_judiciary.items():
        for f in glob.glob(f"tests/judiciary_pyq/{sub}/*.json"):
            f_clean = f.replace("\\", "/")
            update_json_file(f_clean, f_clean, "TOPIC", pid)

    print("Reorganization complete!")

if __name__ == "__main__":
    main()
