import json, os, datetime

OUT_DIR = "tests/current_affairs"
os.makedirs(OUT_DIR, exist_ok=True)

def make_test_json(test_id, title_en, title_hi, duration, total_q, badge, questions):
    max_m = round(total_q * 2.0, 2)
    doc = {
        "testId": test_id,
        "categoryId": "current_affairs",
        "test_id": test_id,
        "category_id": "current_affairs",
        "title": title_en,
        "titleEn": title_en,
        "titleHi": title_hi,
        "testType": "MOCK",
        "test_type": "MOCK",
        "isFree": True,
        "is_free": True,
        "durationMinutes": duration,
        "duration_minutes": duration,
        "totalQuestions": total_q,
        "total_questions": total_q,
        "maxMarks": max_m,
        "positiveMarks": 2.0,
        "negativeMarks": 0.66,
        "examYear": 2024,
        "shiftBadge": badge,
        "questions": questions
    }
    return doc

print("Current Affairs builder helper loaded.")
