import json

with open(r'C:/Users/yedde/.gemini/antigravity-acp/brain/d5dd1b15-4b68-43bb-a5bc-d83e186816f7/.system_generated/logs/transcript.jsonl', 'r', encoding='utf-8') as f:
    lines = f.readlines()

d = json.loads(lines[2082])
print(d.get('content'))
