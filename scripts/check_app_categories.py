import os

app_path = r'D:\MyApp\PrepUnfold\app\src\main\java\com\justunfold\abhyasdesk'
for root, dirs, files in os.walk(app_path):
    for f in files:
        if f in ['CoursePassModels.kt', 'ExamGoalPickerScreen.kt', 'ExamBundle.kt', 'ExamCategory.kt']:
            p = os.path.join(root, f)
            print(f"=== {f} ===")
            with open(p, 'r', encoding='utf-8') as fp:
                print(fp.read()[:1500])
