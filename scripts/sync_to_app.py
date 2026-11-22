import shutil
import os
import re

APP_DIR = r"D:\MyApp\PrepUnfold"
MANIFEST_SRC = r"D:\Android Project\prepunfold-cdn\manifest.json"
MANIFEST_DEST = os.path.join(APP_DIR, r"app\src\main\assets\sample_manifest.json")

print("1. Copying manifest.json to app assets...")
shutil.copyfile(MANIFEST_SRC, MANIFEST_DEST)
print(f"   Copied {MANIFEST_SRC} -> {MANIFEST_DEST}")

# 2. Update CoursePassModels.kt
pass_models_path = os.path.join(APP_DIR, r"app\src\main\java\com\justunfold\abhyasdesk\domain\model\CoursePassModels.kt")
with open(pass_models_path, "r", encoding="utf-8") as f:
    pass_content = f.read()

judiciary_plans = """        CoursePassPlan(
            productId = "pass_judiciary_pyq_6m_149",
            categoryId = "judiciary_pyq",
            title = "Judiciary PYQ 6-Month Target Pass",
            subtitle = "Unlocks all 181 Topic-Wise Tests (14 Law Subjects • 9,927 PYQs) for 180 Days",
            duration = PassDuration.SIX_MONTHS,
            defaultPriceInr = 149,
            isRecommended = false
        ),
        CoursePassPlan(
            productId = "pass_judiciary_pyq_1y_249",
            categoryId = "judiciary_pyq",
            title = "Judiciary PYQ 1-Year Complete Pass",
            subtitle = "Full 365-Day access to all 181 Tests, 14 Subjects & 9,927 PYQs (MPSC JMFC, UPPCS-J, Bihar-J)",
            duration = PassDuration.ONE_YEAR,
            defaultPriceInr = 249,
            isRecommended = true
        ),
"""

if 'pass_judiciary_pyq_6m_149' not in pass_content:
    print("2. Adding Judiciary Pass plans to CoursePassModels.kt...")
    # Insert right before pass_all_exams_7d_20
    marker = 'CoursePassPlan(\n            productId = "pass_all_exams_7d_20",'
    if marker in pass_content:
        pass_content = pass_content.replace(marker, judiciary_plans + "\n        " + marker)
        with open(pass_models_path, "w", encoding="utf-8") as f:
            f.write(pass_content)
        print("   CoursePassModels.kt updated successfully.")
    else:
        print("   Warning: marker not found in CoursePassModels.kt")
else:
    print("2. CoursePassModels.kt already contains judiciary pass plans.")

# 3. Update ExamGoalPickerScreen.kt
goal_picker_path = os.path.join(APP_DIR, r"app\src\main\java\com\justunfold\abhyasdesk\ui\screens\goalpicker\ExamGoalPickerScreen.kt")
with open(goal_picker_path, "r", encoding="utf-8") as f:
    goal_content = f.read()

judiciary_goal = """    ExamGoalItem(
        id = "judiciary_pyq",
        titleEn = "Judiciary (Civil Judge & JMFC) PYQ (1990-2024)",
        titleHi = "न्यायिक सेवा परीक्षा (सिविल जज एवं जेएमएफसी) विगत वर्ष प्रश्न",
        testCountBadge = "181 Tests • 14 Law Subjects • 9,927 PYQs",
        subtitleEn = "Civil Judge Jr Div & JMFC • CPC, CrPC, Evidence, IPC, Constitution, Contract, TPA, Torts, SRA, Limitation, Jurisprudence, Int. Org & Minor Acts",
        subtitleHi = "एमपीएससी जेएमएफसी, यूपी, बिहार, एमपी, राजस्थान, दिल्ली • 14 विधि विषय एवं 9,927 वास्तविक विगत वर्ष प्रश्न द्विभाषी समाधान सहित",
        icon = Icons.Default.School,
        chips = listOf("9,927 Real PYQs", "MPSC JMFC & State PSC", "Bilingual Solutions")
    ),
"""

if 'judiciary_pyq' not in goal_content:
    print("3. Adding Judiciary goal to ExamGoalPickerScreen.kt...")
    marker = 'ExamGoalItem(\n        id = "history_pyq_1990_2024",'
    if marker in goal_content:
        goal_content = goal_content.replace(marker, judiciary_goal + "    " + marker)
        with open(goal_picker_path, "w", encoding="utf-8") as f:
            f.write(goal_content)
        print("   ExamGoalPickerScreen.kt updated successfully.")
    else:
        print("   Warning: marker not found in ExamGoalPickerScreen.kt")
else:
    print("3. ExamGoalPickerScreen.kt already contains judiciary_pyq.")

# 4. Update ExamNavigationDrawer.kt
drawer_path = os.path.join(APP_DIR, r"app\src\main\java\com\justunfold\abhyasdesk\ui\components\ExamNavigationDrawer.kt")
with open(drawer_path, "r", encoding="utf-8") as f:
    drawer_content = f.read()

judiciary_drawer = """    DrawerExamFamily(
        title = "Judiciary (Civil Judge & JMFC)",
        isEnglishOnly = false,
        categoryIds = listOf("judiciary_pyq")
    ),
"""

if 'judiciary_pyq' not in drawer_content:
    print("4. Adding Judiciary to ExamNavigationDrawer.kt...")
    marker = 'DrawerExamFamily(\n        title = "UPSC & State PSC",'
    if marker in drawer_content:
        drawer_content = drawer_content.replace(marker, judiciary_drawer + "    " + marker)
        with open(drawer_path, "w", encoding="utf-8") as f:
            f.write(drawer_content)
        print("   ExamNavigationDrawer.kt updated successfully.")
    else:
        print("   Warning: marker not found in ExamNavigationDrawer.kt")
else:
    print("4. ExamNavigationDrawer.kt already contains judiciary_pyq.")

print("All app sync tasks completed!")
