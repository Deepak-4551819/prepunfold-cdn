import os

teaching_dir = "tests/teaching"
if os.path.exists(teaching_dir):
    print("Folders in tests/teaching:")
    for f in os.listdir(teaching_dir):
        p = os.path.join(teaching_dir, f)
        if os.path.isdir(p):
            print(f"  {f}/ -> {len(os.listdir(p))} items")
            for sub in os.listdir(p):
                sub_p = os.path.join(p, sub)
                if os.path.isdir(sub_p):
                    print(f"     {sub}/ -> {len(os.listdir(sub_p))} items")
