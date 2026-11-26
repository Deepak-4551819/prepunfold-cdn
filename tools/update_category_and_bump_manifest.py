import json
import time

MANIFEST_FILE = "manifest.json"
MASTER_MANIFEST = "manifest_tgt_pgt_history_master.json"

PARTS = [
    {
        "partId": "part1_ancient_history",
        "partTitleEn": "Part I: Ancient Indian History (9 Chapters • 2,153 PYQs)",
        "partTitleHi": "भाग I: प्राचीन भारत का इतिहास (9 अध्याय • 2,153 प्रश्न)",
        "order": 1,
        "topicCount": 9,
        "questionCount": 2153
    },
    {
        "partId": "part2_medieval_history",
        "partTitleEn": "Part II: Medieval Indian History (6 Chapters • 2,025 PYQs)",
        "partTitleHi": "भाग II: मध्यकालीन भारत का इतिहास (6 अध्याय • 2,025 प्रश्न)",
        "order": 2,
        "topicCount": 6,
        "questionCount": 2025
    },
    {
        "partId": "part3_modern_history",
        "partTitleEn": "Part III: Modern Indian History (13 Chapters • 2,149 PYQs)",
        "partTitleHi": "भाग III: आधुनिक भारत का इतिहास (13 अध्याय • 2,149 प्रश्न)",
        "order": 3,
        "topicCount": 13,
        "questionCount": 2149
    },
    {
        "partId": "part4_research_world",
        "partTitleEn": "Part IV: Historiography & World History (2 Chapters • 447 PYQs)",
        "partTitleHi": "भाग IV: इतिहास दर्शन, शोध एवं विश्व इतिहास (2 अध्याय • 447 प्रश्न)",
        "order": 4,
        "topicCount": 2,
        "questionCount": 447
    },
    {
        "partId": "part0_full_length_mocks",
        "partTitleEn": "Part V: Full-Length Practice Mock Tests",
        "partTitleHi": "भाग V: सम्पूर्ण अभ्यास मॉक टेस्ट",
        "order": 5,
        "topicCount": 1,
        "questionCount": 63
    }
]

def update_manifest():
    with open(MANIFEST_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. Update tgt_pgt_history category
    for c in data.get('categories', []):
        cid = c.get('categoryId') or c.get('id')
        if cid == 'tgt_pgt_history':
            c['totalTests'] = 31
            c['total_tests'] = 31
            c['totalQuestions'] = 6837
            c['total_questions'] = 6837
            c['subtitle'] = "30 Chapter Topic Tests + Full-Length Mocks (6,837 Solved PYQs • Bilingual)"
            c['descriptionEn'] = "Complete TGT/PGT History: 30 Chapter-Wise Solved Topic Tests across Ancient, Medieval, Modern & World History + Full-Length Mocks • 6,837 Authentic Solved PYQs with Detailed Bilingual Explanations"
            c['descriptionHi'] = "टीजीटी/पीजीटी इतिहास: 30 अध्यायवार टॉपिक टेस्ट (प्राचीन, मध्यकालीन, आधुनिक एवं विश्व इतिहास) + फुल-लेंथ मॉक • 6,837 प्रमाणिक हल प्रश्न विस्तृत द्विभाषी व्याख्या सहित"
            c['parts'] = PARTS
            print("Updated tgt_pgt_history category in manifest.json")

    # 2. Bump version
    cur_v = data.get('version') or data.get('manifest_version', 38)
    new_v = cur_v + 1
    data['version'] = new_v
    data['manifest_version'] = new_v
    data['manifestVersion'] = new_v

    # 3. Recount total tests and questions
    tests = data.get('tests', [])
    data['totalTests'] = len(tests)
    data['total_tests'] = len(tests)
    data['totalQuestions'] = sum(t.get('totalQuestions', 0) for t in tests)
    data['total_questions'] = data['totalQuestions']
    data['lastUpdated'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    data['updatedAt'] = data['lastUpdated']
    data['updated_at'] = data['lastUpdated']

    with open(MANIFEST_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Bumped manifest.json to v{new_v}. Total tests: {data['totalTests']}, Total Qs: {data['totalQuestions']}")

    # 4. Master manifest
    with open(MASTER_MANIFEST, 'r', encoding='utf-8') as f:
        master = json.load(f)

    for c in master.get('categories', []):
        cid = c.get('categoryId') or c.get('id')
        if cid == 'tgt_pgt_history':
            c['totalTests'] = 31
            c['total_tests'] = 31
            c['totalQuestions'] = 6837
            c['total_questions'] = 6837
            c['subtitle'] = "30 Chapter Topic Tests + Full-Length Mocks (6,837 Solved PYQs • Bilingual)"
            c['descriptionEn'] = "Complete TGT/PGT History: 30 Chapter-Wise Solved Topic Tests across Ancient, Medieval, Modern & World History + Full-Length Mocks • 6,837 Authentic Solved PYQs with Detailed Bilingual Explanations"
            c['descriptionHi'] = "टीजीटी/पीजीटी इतिहास: 30 अध्यायवार टॉपिक टेस्ट (प्राचीन, मध्यकालीन, आधुनिक एवं विश्व इतिहास) + फुल-लेंथ मॉक • 6,837 प्रमाणिक हल प्रश्न विस्तृत द्विभाषी व्याख्या सहित"
            c['parts'] = PARTS

    master['version'] = new_v
    master['manifest_version'] = new_v
    master['manifestVersion'] = new_v
    master['totalTests'] = len(master.get('tests', []))
    master['total_tests'] = master['totalTests']
    master['totalQuestions'] = sum(t.get('totalQuestions', 0) for t in master.get('tests', []))
    master['total_questions'] = master['totalQuestions']
    master['lastUpdated'] = data['lastUpdated']
    master['updatedAt'] = data['lastUpdated']
    master['updated_at'] = data['lastUpdated']

    with open(MASTER_MANIFEST, 'w', encoding='utf-8') as f:
        json.dump(master, f, ensure_ascii=False, indent=2)
    print(f"Bumped master manifest to v{new_v}.")

if __name__ == '__main__':
    update_manifest()
