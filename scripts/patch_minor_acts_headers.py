import os
import glob
import json

minor_dir = "tests/judiciary_pyq/minor_acts"
for f in glob.glob(os.path.join(minor_dir, "*.json")):
    with open(f, "r", encoding="utf-8") as fp:
        data = json.load(fp)

    data["categoryId"] = "judiciary_pyq"
    data["category_id"] = "judiciary_pyq"
    data["partId"] = "part14_minor_acts"
    data["partTitleEn"] = "Part XIV: Minor Acts (9 in 1 Special)"
    data["partTitleHi"] = "भाग XIV: लघु अधिनियम (Minor Acts)"
    data["testType"] = "TOPIC_TEST"
    data["test_type"] = "TOPIC_TEST"
    data["isFree"] = True
    data["is_free"] = True
    data["positiveMarks"] = 1.0
    data["positive_marks"] = 1.0
    data["negativeMarks"] = 0.33
    data["negative_marks"] = 0.33
    data["exam_year_tag"] = "Judiciary PYQ • Minor Acts Special"
    data["examYearTag"] = "Judiciary PYQ • Minor Acts Special"

    with open(f, "w", encoding="utf-8") as fp:
        json.dump(data, fp, ensure_ascii=False, indent=2)

print("Patched all minor acts headers successfully!")
