import zipfile, json

ZIP_MOCKS = r"C:\Users\yedde\Downloads\gate_ph_mocks_and_topic_tests.zip"
with zipfile.ZipFile(ZIP_MOCKS, "r") as z:
    m1 = json.loads(z.read("full_mocks/gate_ph_mock_01.json").decode("utf-8"))
    t1 = json.loads(z.read("topic_tests/gate_ph_topic_ga_01.json").decode("utf-8"))
    print("Mock 01 header:", {k: v for k, v in m1.items() if k != "questions"})
    print("Topic GA 01 header:", {k: v for k, v in t1.items() if k != "questions"})
    # Check unique sectionIds/sectionTitles in mocks and topics
    secs = set()
    for n in z.namelist():
        if n.endswith(".json"):
            d = json.loads(z.read(n).decode("utf-8"))
            for q in d["questions"]:
                secs.add((q["sectionId"], q["sectionTitle"]))
    print("Unique sections:", sorted(list(secs)))
