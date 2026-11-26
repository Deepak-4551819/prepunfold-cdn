# -*- coding: utf-8 -*-
import os, sys, json, hashlib, re

CDN_BASE = 'https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/'
ALT_CDN_BASE = 'https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main/'

PARTS_DEF = [
    {
        'partId': 'part_01_ga',
        'partTitleEn': 'Section 1: General Aptitude',
        'partTitleHi': 'खंड 1: सामान्य योग्यता',
        'order': 1,
        'topicCount': 2,
        'questionCount': 40
    },
    {
        'partId': 'part_02_mp',
        'partTitleEn': 'Section 2: Mathematical Physics',
        'partTitleHi': 'खंड 2: गणितीय भौतिकी',
        'order': 2,
        'topicCount': 2,
        'questionCount': 40
    },
    {
        'partId': 'part_03_cm',
        'partTitleEn': 'Section 3: Classical Mechanics',
        'partTitleHi': 'खंड 3: चिरसम्मत यांत्रिकी',
        'order': 3,
        'topicCount': 2,
        'questionCount': 40
    },
    {
        'partId': 'part_04_emt',
        'partTitleEn': 'Section 4: Electromagnetic Theory',
        'partTitleHi': 'खंड 4: विद्युतचुंबकीय सिद्धांत',
        'order': 4,
        'topicCount': 2,
        'questionCount': 40
    },
    {
        'partId': 'part_05_qm',
        'partTitleEn': 'Section 5: Quantum Mechanics',
        'partTitleHi': 'खंड 5: क्वांटम यांत्रिकी',
        'order': 5,
        'topicCount': 2,
        'questionCount': 40
    },
    {
        'partId': 'part_06_tsp',
        'partTitleEn': 'Section 6: Thermodynamics and Statistical Physics',
        'partTitleHi': 'खंड 6: ऊष्मागतिकी एवं सांख्यिकीय भौतिकी',
        'order': 6,
        'topicCount': 2,
        'questionCount': 40
    },
    {
        'partId': 'part_07_amp',
        'partTitleEn': 'Section 7: Atomic and Molecular Physics',
        'partTitleHi': 'खंड 7: परमाण्विक एवं आणविक भौतिकी',
        'order': 7,
        'topicCount': 2,
        'questionCount': 40
    },
    {
        'partId': 'part_08_ssp',
        'partTitleEn': 'Section 8: Solid State Physics',
        'partTitleHi': 'खंड 8: ठोस अवस्था भौतिकी',
        'order': 8,
        'topicCount': 2,
        'questionCount': 40
    },
    {
        'partId': 'part_09_elec',
        'partTitleEn': 'Section 9: Electronics',
        'partTitleHi': 'खंड 9: इलेक्ट्रॉनिकी',
        'order': 9,
        'topicCount': 2,
        'questionCount': 40
    },
    {
        'partId': 'part_10_npp',
        'partTitleEn': 'Section 10: Nuclear and Particle Physics',
        'partTitleHi': 'खंड 10: नाभिकीय एवं कण भौतिकी',
        'order': 10,
        'topicCount': 2,
        'questionCount': 40
    }
]

PART_HI_NAMES = {
    'part_01_ga': 'सामान्य योग्यता',
    'part_02_mp': 'गणितीय भौतिकी',
    'part_03_cm': 'चिरसम्मत यांत्रिकी',
    'part_04_emt': 'विद्युतचुंबकीय सिद्धांत',
    'part_05_qm': 'क्वांटम यांत्रिकी',
    'part_06_tsp': 'ऊष्मागतिकी एवं सांख्यिकीय भौतिकी',
    'part_07_amp': 'परमाण्विक एवं आणविक भौतिकी',
    'part_08_ssp': 'ठोस अवस्था भौतिकी',
    'part_09_elec': 'इलेक्ट्रॉनिकी',
    'part_10_npp': 'नाभिकीय एवं कण भौतिकी'
}

def update_manifest():
    with open('manifest.json', 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    # 1. Update Category gate_ph
    for cat in manifest.get('categories', []):
        if cat.get('id') == 'gate_ph':
            cat['title'] = 'GATE Physics (PH)'
            cat['titleEn'] = 'GATE Physics (PH)'
            cat['titleHi'] = 'गेट भौतिकी (PH)'
            cat['subtitle'] = 'Official Master PYQs (2021–2026) + 10 Full Mocks + 20 Topic Tests'
            cat['subtitleEn'] = 'Official Master PYQs (2021–2026) + 10 Full Mocks + 20 Topic Tests'
            cat['subtitleHi'] = 'आधिकारिक मास्टर PYQs (2021–2026) + 10 संपूर्ण मॉक + 20 टॉपिक टेस्ट'
            cat['totalTests'] = 36
            cat['totalQuestions'] = 1440
            cat['parts'] = PARTS_DEF
            break

    # 2. Build 36 test entries
    new_gate_ph_tests = []

    # A) 6 PYQs: 2026 down to 2021
    pyq_years = [2026, 2025, 2024, 2023, 2022, 2021]
    for y in pyq_years:
        rel_path = f'tests/gate/gate_ph/pyq/gate_ph_pyq_{y}.json'
        with open(rel_path, 'r', encoding='utf-8') as f:
            d = json.load(f)
        
        tid = f'gate_ph_pyq_{y}'
        is_free = bool(d.get('isFree', False))
        entry = {
            'test_id': tid,
            'testId': tid,
            'category_id': 'gate_ph',
            'categoryId': 'gate_ph',
            'test_type': 'PYQ',
            'testType': 'PYQ',
            'title': d['title'],
            'titleEn': d.get('titleEn', d['title']),
            'titleHi': f'GATE {y} भौतिकी (PH) आधिकारिक हल प्रश्न पत्र (सभी 9 मुख्य विषय एवं GA)',
            'exam_year_tag': str(y),
            'examYearTag': str(y),
            'shiftBadge': f'GATE PH • {y} Official Paper',
            'duration_minutes': 180,
            'durationMinutes': 180,
            'total_questions': len(d.get('questions', [])),
            'totalQuestions': len(d.get('questions', [])),
            'positive_marks': 2.0,
            'positiveMarks': 2.0,
            'negative_marks': 0.33,
            'negativeMarks': 0.33,
            'is_free': is_free,
            'isFree': is_free,
            'version': 1,
            'path': rel_path,
            'filePath': rel_path,
            'file_path': rel_path,
            'json_url': f'{CDN_BASE}{rel_path}',
            'cdnUrl': f'{CDN_BASE}{rel_path}',
            'altCdnUrl': f'{ALT_CDN_BASE}{rel_path}'
        }
        new_gate_ph_tests.append(entry)

    # B) 10 Full Mocks: 01 to 10
    for i in range(1, 11):
        rel_path = f'tests/gate/gate_ph/full_mocks/gate_ph_mock_{i:02d}.json'
        with open(rel_path, 'r', encoding='utf-8') as f:
            d = json.load(f)
        
        tid = f'gate_ph_mock_{i:02d}'
        is_free = bool(d.get('isFree', False))
        entry = {
            'test_id': tid,
            'testId': tid,
            'category_id': 'gate_ph',
            'categoryId': 'gate_ph',
            'test_type': 'FULL_MOCK',
            'testType': 'FULL_MOCK',
            'title': d['title'],
            'titleEn': d.get('titleEn', d['title']),
            'titleHi': f'GATE 2027 भौतिकी (PH) संपूर्ण मॉक टेस्ट {i:02d}',
            'exam_year_tag': '2027',
            'examYearTag': '2027',
            'shiftBadge': d.get('shiftBadge', f'GATE PH • Full Mock {i:02d}'),
            'duration_minutes': 180,
            'durationMinutes': 180,
            'total_questions': len(d.get('questions', [])),
            'totalQuestions': len(d.get('questions', [])),
            'positive_marks': 2.0,
            'positiveMarks': 2.0,
            'negative_marks': 0.33,
            'negativeMarks': 0.33,
            'is_free': is_free,
            'isFree': is_free,
            'version': 1,
            'path': rel_path,
            'filePath': rel_path,
            'file_path': rel_path,
            'json_url': f'{CDN_BASE}{rel_path}',
            'cdnUrl': f'{CDN_BASE}{rel_path}',
            'altCdnUrl': f'{ALT_CDN_BASE}{rel_path}'
        }
        new_gate_ph_tests.append(entry)

    # C) 20 Topic Tests
    topic_configs = [
        ('part_01_ga', 'ga', 'General Aptitude'),
        ('part_02_mp', 'mp', 'Mathematical Physics'),
        ('part_03_cm', 'cm', 'Classical Mechanics'),
        ('part_04_emt', 'emt', 'Electromagnetic Theory'),
        ('part_05_qm', 'qm', 'Quantum Mechanics'),
        ('part_06_tsp', 'tsp', 'Thermodynamics and Statistical Physics'),
        ('part_07_amp', 'amp', 'Atomic and Molecular Physics'),
        ('part_08_ssp', 'ssp', 'Solid State Physics'),
        ('part_09_elec', 'elec', 'Electronics'),
        ('part_10_npp', 'npp', 'Nuclear and Particle Physics')
    ]
    for pid, pref, en_name in topic_configs:
        for s in [1, 2]:
            rel_path = f'tests/gate/gate_ph/topic_tests/{pid}/gate_ph_topic_{pref}_{s:02d}.json'
            with open(rel_path, 'r', encoding='utf-8') as f:
                d = json.load(f)
            tid = f'gate_ph_topic_{pref}_{s:02d}'
            is_free = bool(d.get('isFree', False))
            hi_name = PART_HI_NAMES.get(pid, en_name)
            entry = {
                'test_id': tid,
                'testId': tid,
                'category_id': 'gate_ph',
                'categoryId': 'gate_ph',
                'test_type': 'TOPIC',
                'testType': 'TOPIC',
                'title': d['title'],
                'titleEn': d.get('titleEn', d['title']),
                'titleHi': f'गेट भौतिकी टॉपिक टेस्ट: {hi_name} — सेट {s}',
                'exam_year_tag': '2027',
                'examYearTag': '2027',
                'shiftBadge': d.get('shiftBadge', f'Topic Set {s}'),
                'duration_minutes': 45,
                'durationMinutes': 45,
                'total_questions': len(d.get('questions', [])),
                'totalQuestions': len(d.get('questions', [])),
                'positive_marks': 2.0,
                'positiveMarks': 2.0,
                'negative_marks': 0.33,
                'negativeMarks': 0.33,
                'is_free': is_free,
                'isFree': is_free,
                'version': 1,
                'path': rel_path,
                'filePath': rel_path,
                'file_path': rel_path,
                'json_url': f'{CDN_BASE}{rel_path}',
                'cdnUrl': f'{CDN_BASE}{rel_path}',
                'altCdnUrl': f'{ALT_CDN_BASE}{rel_path}',
                'part_id': pid,
                'partId': pid
            }
            new_gate_ph_tests.append(entry)

    # 3. Replace in manifest['tests']
    tests_list = manifest['tests']
    first_idx = None
    last_idx = None
    for idx, t in enumerate(tests_list):
        if t.get('categoryId') == 'gate_ph':
            if first_idx is None:
                first_idx = idx
            last_idx = idx

    print(f'Replacing gate_ph tests from index {first_idx} to {last_idx} ({last_idx - first_idx + 1} old tests) with {len(new_gate_ph_tests)} new tests.')
    manifest['tests'] = tests_list[:first_idx] + new_gate_ph_tests + tests_list[last_idx + 1:]

    with open('manifest.json', 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print('Manifest updated successfully!')

if __name__ == '__main__':
    update_manifest()
