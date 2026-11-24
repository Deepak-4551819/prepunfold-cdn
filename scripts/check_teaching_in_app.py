import os

APP_DIR = r"D:\MyApp\PrepUnfold"

drawer_path = os.path.join(APP_DIR, r"app\src\main\java\com\justunfold\abhyasdesk\ui\components\ExamNavigationDrawer.kt")
with open(drawer_path, "r", encoding="utf-8") as f:
    dc = f.read()
print("=== ExamNavigationDrawer.kt teaching snippet ===")
for line in dc.split("\n"):
    if any(k in line for k in ["teaching", "Teaching", "tgt_pgt", "DrawerExamFamily"]):
        print(line)

goal_picker_path = os.path.join(APP_DIR, r"app\src\main\java\com\justunfold\abhyasdesk\ui\screens\goalpicker\ExamGoalPickerScreen.kt")
with open(goal_picker_path, "r", encoding="utf-8") as f:
    gc = f.read()
print("\n=== ExamGoalPickerScreen.kt teaching snippet ===")
for line in gc.split("\n"):
    if any(k in line for k in ["tgt_pgt", "teaching", "Teaching", "CTET", "ctet"]):
        print(line)
