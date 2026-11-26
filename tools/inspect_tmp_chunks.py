import os

chunks_dir = "_tmp_chunks"
if os.path.exists(chunks_dir):
    files = sorted(os.listdir(chunks_dir))
    print(f"Total files in {chunks_dir}: {len(files)}")
    print("First 10:", files[:10])
    print("Last 10:", files[-10:])
else:
    print(f"{chunks_dir} does not exist!")
