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

new_pass_plans = """        CoursePassPlan(
            productId = "pass_ctet_tet_hindi_6m_49",
            categoryId = "ctet_state_tet_hindi",
            title = "CTET & State TET Hindi 6-Month Pass",
            subtitle = "Unlocks all 21 Chapter Tests (3,353 Solved Questions) for 180 Days",
            duration = PassDuration.SIX_MONTHS,
            defaultPriceInr = 49,
            isRecommended = false
        ),
        CoursePassPlan(
            productId = "pass_ctet_tet_hindi_1y_89",
            categoryId = "ctet_state_tet_hindi",
            title = "CTET & State TET Hindi 1-Year Pass",
            subtitle = "Full 365-Day access to all 21 Chapter Tests (Grammar, Literature & Pedagogy)",
            duration = PassDuration.ONE_YEAR,
            defaultPriceInr = 89,
            isRecommended = true
        ),

        CoursePassPlan(
            productId = "pass_emrs_hindi_6m_49",
            categoryId = "emrs_general_hindi",
            title = "EMRS Special General Hindi 6-Month Pass",
            subtitle = "Unlocks all 25 Chapter Tests (2,175 Solved Questions) for 180 Days",
            duration = PassDuration.SIX_MONTHS,
            defaultPriceInr = 49,
            isRecommended = false
        ),
        CoursePassPlan(
            productId = "pass_emrs_hindi_1y_89",
            categoryId = "emrs_general_hindi",
            title = "EMRS Special General Hindi 1-Year Pass",
            subtitle = "Full 365-Day access to all 25 Chapter Tests (EMRS, KVS, NVS, DSSSB)",
            duration = PassDuration.ONE_YEAR,
            defaultPriceInr = 89,
            isRecommended = true
        ),
"""

if 'pass_ctet_tet_hindi_6m_49' not in pass_content:
    print("2. Adding CTET and EMRS Pass plans to CoursePassModels.kt...")
    marker = 'CoursePassPlan(\n            productId = "pass_all_exams_7d_20",'
    if marker in pass_content:
        pass_content = pass_content.replace(marker, new_pass_plans + "\n        " + marker)
        with open(pass_models_path, "w", encoding="utf-8") as f:
            f.write(pass_content)
        print("   CoursePassModels.kt updated successfully.")
    else:
        print("   Warning: marker not found in CoursePassModels.kt")
else:
    print("2. CoursePassModels.kt already contains CTET/EMRS pass plans.")

# 3. Update ExamGoalPickerScreen.kt
goal_picker_path = os.path.join(APP_DIR, r"app\src\main\java\com\justunfold\abhyasdesk\ui\screens\goalpicker\ExamGoalPickerScreen.kt")
with open(goal_picker_path, "r", encoding="utf-8") as f:
    goal_content = f.read()

new_goals = """    CompactGoalItem(
        id = "ctet_state_tet_hindi",
        titleEn = "CTET & State TET (Hindi & Pedagogy)",
        titleHi = "सीटीईटी एवं राज्य टीईटी (हिन्दी भाषा व शिक्षाशास्त्र)",
        group = "Teaching",
        metadataEn = "Teaching • 21 Tests • 3,353 Solved Qs",
        metadataHi = "शिक्षक पात्रता • 21 टेस्ट • 3,353 हल प्रश्न",
        icon = Icons.AutoMirrored.Filled.MenuBook
    ),
    CompactGoalItem(
        id = "emrs_general_hindi",
        titleEn = "EMRS Special General Hindi",
        titleHi = "ईएमआरएस विशेष सामान्य हिन्दी",
        group = "Teaching",
        metadataEn = "Teaching • 25 Tests • 2,175 Solved Qs",
        metadataHi = "शिक्षक भर्ती • 25 टेस्ट • 2,175 हल प्रश्न",
        icon = Icons.AutoMirrored.Filled.MenuBook
    ),
"""

if 'ctet_state_tet_hindi' not in goal_content:
    print("3. Adding CTET and EMRS goals to ExamGoalPickerScreen.kt...")
    marker = 'CompactGoalItem(\n        id = "judiciary_pyq",'
    if marker in goal_content:
        goal_content = goal_content.replace(marker, new_goals + "    " + marker)
        with open(goal_picker_path, "w", encoding="utf-8") as f:
            f.write(goal_content)
        print("   ExamGoalPickerScreen.kt updated successfully.")
    else:
        print("   Warning: marker not found in ExamGoalPickerScreen.kt")
else:
    print("3. ExamGoalPickerScreen.kt already contains ctet_state_tet_hindi.")

# 4. Update ExamNavigationDrawer.kt
drawer_path = os.path.join(APP_DIR, r"app\src\main\java\com\justunfold\abhyasdesk\ui\components\ExamNavigationDrawer.kt")
with open(drawer_path, "r", encoding="utf-8") as f:
    drawer_content = f.read()

if 'ctet_' not in drawer_content:
    print("4. Updating resolveFallbackGroup in ExamNavigationDrawer.kt...")
    old_line = 'categoryId.startsWith("tgt_pgt") -> "teaching"'
    new_line = 'categoryId.startsWith("tgt_pgt") || categoryId.startsWith("ctet_") || categoryId.startsWith("emrs_") -> "teaching"'
    if old_line in drawer_content:
        drawer_content = drawer_content.replace(old_line, new_line)
        with open(drawer_path, "w", encoding="utf-8") as f:
            f.write(drawer_content)
        print("   ExamNavigationDrawer.kt updated successfully.")
    else:
        print("   Warning: marker not found in ExamNavigationDrawer.kt")
else:
    print("4. ExamNavigationDrawer.kt already handles ctet_.")

print("\nAll app sync tasks completed successfully!")
