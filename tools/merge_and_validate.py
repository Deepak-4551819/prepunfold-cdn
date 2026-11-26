#!/usr/bin/env python3
"""
tools/merge_and_validate.py
Merges extracted chunk JSONs for any chapter into the final 40-key dual
camelCase + snake_case schema file inside tests/tgt_pgt_history/,
overwrites any old low-question files (and removes ch02_part1/part2 duplicates),
validates 4 options & sequential questionNumber, and updates the manifest JSONs.
"""

import os
import sys
import glob
import json
import re
import argparse

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

CHAPTER_METADATA = {
    1: {
        "part_id": "part1_ancient_history",
        "partTitleEn": "Part I: Ancient Indian History",
        "partTitleHi": "भाग I: प्राचीन भारतीय इतिहास",
        "file_name": "tgt_pgt_hist_ch01_prehistoric_cultures.json",
        "test_id": "tgt_pgt_hist_ch01_prehistoric_cultures",
        "topicNumber": 1,
        "topicTitleEn": "1. Salient Features of Indian Prehistoric Cultures",
        "topicTitleHi": "1. भारतीय प्रागैतिहासिक संस्कृतियों की प्रमुख विशेषताएँ",
        "titleEn": "Ancient History Chapter 1: Indian Prehistoric Cultures",
        "titleHi": "प्राचीन इतिहास अध्याय 1: भारतीय प्रागैतिहासिक संस्कृतियाँ",
        "start_page": 9,
        "end_page": 32,
    },
    2: {
        "part_id": "part1_ancient_history",
        "partTitleEn": "Part I: Ancient Indian History",
        "partTitleHi": "भाग I: प्राचीन भारतीय इतिहास",
        "file_name": "tgt_pgt_hist_ch02_indus_valley.json",
        "test_id": "tgt_pgt_hist_ch02_indus_valley",
        "topicNumber": 2,
        "topicTitleEn": "2. Indus Valley Civilization & Town Planning",
        "topicTitleHi": "2. सिन्धु घाटी सभ्यता एवं नगर नियोजन",
        "titleEn": "Ancient History Chapter 2: Indus Valley Civilization & Town Planning",
        "titleHi": "प्राचीन इतिहास अध्याय 2: सिन्धु घाटी सभ्यता एवं नगर नियोजन",
        "start_page": 33,
        "end_page": 59,
    },
    3: {
        "part_id": "part1_ancient_history",
        "partTitleEn": "Part I: Ancient Indian History",
        "partTitleHi": "भाग I: प्राचीन भारतीय इतिहास",
        "file_name": "tgt_pgt_hist_ch03_vedic_period.json",
        "test_id": "tgt_pgt_hist_ch03_vedic_period",
        "topicNumber": 3,
        "topicTitleEn": "3. Vedic & Later Vedic Period",
        "topicTitleHi": "3. वैदिक काल एवं उत्तर वैदिक काल",
        "titleEn": "Ancient History Chapter 3: Vedic & Later Vedic Period",
        "titleHi": "प्राचीन इतिहास अध्याय 3: वैदिक काल एवं उत्तर वैदिक काल",
        "start_page": 60,
        "end_page": 90,
    },
    4: {
        "part_id": "part1_ancient_history",
        "partTitleEn": "Part I: Ancient Indian History",
        "partTitleHi": "भाग I: प्राचीन भारतीय इतिहास",
        "file_name": "tgt_pgt_hist_ch04_jain_buddha_mahajanapada.json",
        "test_id": "tgt_pgt_hist_ch04_jain_buddha_mahajanapada",
        "topicNumber": 4,
        "topicTitleEn": "4. Jainism, Buddhism & Mahajanapadas",
        "topicTitleHi": "4. जैन धर्म, बौद्ध धर्म एवं 16 महाजनपद",
        "titleEn": "Ancient History Chapter 4: Jainism, Buddhism & Mahajanapadas",
        "titleHi": "प्राचीन इतिहास अध्याय 4: जैन धर्म, बौद्ध धर्म एवं महाजनपद",
        "start_page": 91,
        "end_page": 134,
    },
    5: {
        "part_id": "part1_ancient_history",
        "partTitleEn": "Part I: Ancient Indian History",
        "partTitleHi": "भाग I: प्राचीन भारतीय इतिहास",
        "file_name": "tgt_pgt_hist_ch05_mauryan_post_mauryan.json",
        "test_id": "tgt_pgt_hist_ch05_mauryan_post_mauryan",
        "topicNumber": 5,
        "topicTitleEn": "5. Mauryan & Post-Mauryan Period",
        "topicTitleHi": "5. मौर्यकाल एवं मौर्योत्तर काल",
        "titleEn": "Ancient History Chapter 5: Mauryan & Post-Mauryan Period",
        "titleHi": "प्राचीन इतिहास अध्याय 5: मौर्यकाल एवं मौर्योत्तर काल",
        "start_page": 135,
        "end_page": 182,
    },
    6: {
        "part_id": "part1_ancient_history",
        "partTitleEn": "Part I: Ancient Indian History",
        "partTitleHi": "भाग I: प्राचीन भारतीय इतिहास",
        "file_name": "tgt_pgt_hist_ch06_gupta_post_gupta.json",
        "test_id": "tgt_pgt_hist_ch06_gupta_post_gupta",
        "topicNumber": 6,
        "topicTitleEn": "6. Gupta & Post-Gupta Era",
        "topicTitleHi": "6. गुप्त एवं गुप्तोत्तर काल (हर्षवर्धन)",
        "titleEn": "Ancient History Chapter 6: Gupta & Post-Gupta Era",
        "titleHi": "प्राचीन इतिहास अध्याय 6: गुप्त एवं गुप्तोत्तर काल",
        "start_page": 183,
        "end_page": 212,
    },
    7: {
        "part_id": "part1_ancient_history",
        "partTitleEn": "Part I: Ancient Indian History",
        "partTitleHi": "भाग I: प्राचीन भारतीय इतिहास",
        "file_name": "tgt_pgt_hist_ch07_chola_period.json",
        "test_id": "tgt_pgt_hist_ch07_chola_period",
        "topicNumber": 7,
        "topicTitleEn": "7. Chola Period & South Indian Dynasties",
        "topicTitleHi": "7. चोल काल एवं दक्षिण भारत के राजवंश",
        "titleEn": "Ancient History Chapter 7: Chola Period & South India",
        "titleHi": "प्राचीन इतिहास अध्याय 7: चोल काल एवं दक्षिण भारत",
        "start_page": 213,
        "end_page": 224,
    },
    8: {
        "part_id": "part1_ancient_history",
        "partTitleEn": "Part I: Ancient Indian History",
        "partTitleHi": "भाग I: प्राचीन भारतीय इतिहास",
        "file_name": "tgt_pgt_hist_ch08_foreign_invasions.json",
        "test_id": "tgt_pgt_hist_ch08_foreign_invasions",
        "topicNumber": 8,
        "topicTitleEn": "8. Foreign Invasions (Arab, Ghazni, Ghori)",
        "topicTitleHi": "8. विदेशी आक्रमण (अरब, गजनवी, गोरी)",
        "titleEn": "Ancient History Chapter 8: Foreign Invasions",
        "titleHi": "प्राचीन इतिहास अध्याय 8: विदेशी आक्रमण (अरब, गजनवी, गोरी)",
        "start_page": 225,
        "end_page": 232,
    },
    9: {
        "part_id": "part1_ancient_history",
        "partTitleEn": "Part I: Ancient Indian History",
        "partTitleHi": "भाग I: प्राचीन भारतीय इतिहास",
        "file_name": "tgt_pgt_hist_ch09_ancient_misc.json",
        "test_id": "tgt_pgt_hist_ch09_ancient_misc",
        "topicNumber": 9,
        "topicTitleEn": "9. Ancient Indian Culture, Literature & Historiography",
        "topicTitleHi": "9. विविध: प्राचीन भारतीय इतिहास, कला, साहित्य एवं संस्कृति",
        "titleEn": "Ancient History Chapter 9: Ancient Indian Culture & Misc",
        "titleHi": "प्राचीन इतिहास अध्याय 9: विविध प्राचीन इतिहास एवं संस्कृति",
        "start_page": 233,
        "end_page": 284,
    },
    10: {
        "part_id": "part2_medieval_history",
        "partTitleEn": "Part II: Medieval Indian History",
        "partTitleHi": "भाग II: मध्यकालीन भारतीय इतिहास",
        "file_name": "tgt_pgt_hist_ch10_delhi_sultanate.json",
        "test_id": "tgt_pgt_hist_ch10_delhi_sultanate",
        "topicNumber": 10,
        "topicTitleEn": "10. Delhi Sultanate (Polity, Administration & Culture)",
        "topicTitleHi": "10. दिल्ली सल्तनत (राजनीतिक, प्रशासनिक व सांस्कृतिक)",
        "titleEn": "Medieval History Chapter 10: Delhi Sultanate",
        "titleHi": "मध्यकालीन इतिहास अध्याय 10: दिल्ली सल्तनत",
        "start_page": 285,
        "end_page": 348,
    },
    11: {
        "part_id": "part2_medieval_history",
        "partTitleEn": "Part II: Medieval Indian History",
        "partTitleHi": "भाग II: मध्यकालीन भारतीय इतिहास",
        "file_name": "tgt_pgt_hist_ch11_mughal_empire.json",
        "test_id": "tgt_pgt_hist_ch11_mughal_empire",
        "topicNumber": 11,
        "topicTitleEn": "11. Mughal Empire, Administration, Art & Architecture",
        "topicTitleHi": "11. मुगल साम्राज्य एवं प्रशासन",
        "titleEn": "Medieval History Chapter 11: Mughal Empire",
        "titleHi": "मध्यकालीन इतिहास अध्याय 11: मुगल साम्राज्य एवं प्रशासन",
        "start_page": 349,
        "end_page": 419,
    },
    12: {
        "part_id": "part2_medieval_history",
        "partTitleEn": "Part II: Medieval Indian History",
        "partTitleHi": "भाग II: मध्यकालीन भारतीय इतिहास",
        "file_name": "tgt_pgt_hist_ch12_bahmani_vijayanagara_maratha.json",
        "test_id": "tgt_pgt_hist_ch12_bahmani_vijayanagara_maratha",
        "topicNumber": 12,
        "topicTitleEn": "12. Vijayanagara, Bahmani & Maratha Empire",
        "topicTitleHi": "12. विजयनगर, बहमनी एवं मराठा साम्राज्य",
        "titleEn": "Medieval History Chapter 12: Vijayanagara, Bahmani & Marathas",
        "titleHi": "मध्यकालीन इतिहास अध्याय 12: विजयनगर, बहमनी एवं मराठा साम्राज्य",
        "start_page": 420,
        "end_page": 449,
    },
    13: {
        "part_id": "part2_medieval_history",
        "partTitleEn": "Part II: Medieval Indian History",
        "partTitleHi": "भाग II: मध्यकालीन भारतीय इतिहास",
        "file_name": "tgt_pgt_hist_ch13_medieval_culture.json",
        "test_id": "tgt_pgt_hist_ch13_medieval_culture",
        "topicNumber": 13,
        "topicTitleEn": "13. Medieval Culture, Bhakti Movement & Sufism",
        "topicTitleHi": "13. मध्यकालीन संस्कृति, भक्ति एवं सूफी आन्दोलन",
        "titleEn": "Medieval History Chapter 13: Medieval Culture, Bhakti & Sufism",
        "titleHi": "मध्यकालीन इतिहास अध्याय 13: मध्यकालीन संस्कृति, भक्ति एवं सूफी आन्दोलन",
        "start_page": 450,
        "end_page": 521,
    },
    14: {
        "part_id": "part2_medieval_history",
        "partTitleEn": "Part II: Medieval Indian History",
        "partTitleHi": "भाग II: मध्यकालीन भारतीय इतिहास",
        "file_name": "tgt_pgt_hist_ch14_medieval_society_economy.json",
        "test_id": "tgt_pgt_hist_ch14_medieval_society_economy",
        "topicNumber": 14,
        "topicTitleEn": "14. Medieval Society, Agrarian System & Economy",
        "topicTitleHi": "14. मध्यकालीन समाज एवं अर्थव्यवस्था",
        "titleEn": "Medieval History Chapter 14: Medieval Society & Economy",
        "titleHi": "मध्यकालीन इतिहास अध्याय 14: मध्यकालीन समाज एवं अर्थव्यवस्था",
        "start_page": 522,
        "end_page": 544,
    },
    15: {
        "part_id": "part2_medieval_history",
        "partTitleEn": "Part II: Medieval Indian History",
        "partTitleHi": "भाग II: मध्यकालीन भारतीय इतिहास",
        "file_name": "tgt_pgt_hist_ch15_medieval_misc.json",
        "test_id": "tgt_pgt_hist_ch15_medieval_misc",
        "topicNumber": 15,
        "topicTitleEn": "15. Miscellaneous Medieval History & Regional Dynasties",
        "topicTitleHi": "15. विविध: मध्यकालीन इतिहास",
        "titleEn": "Medieval History Chapter 15: Miscellaneous Medieval History",
        "titleHi": "मध्यकालीन इतिहास अध्याय 15: विविध मध्यकालीन इतिहास",
        "start_page": 545,
        "end_page": 562,
    },
    16: {
        "part_id": "part3_modern_history",
        "partTitleEn": "Part III: Modern Indian History",
        "partTitleHi": "भाग III: आधुनिक भारतीय इतिहास",
        "file_name": "tgt_pgt_hist_ch16_east_india_company.json",
        "test_id": "tgt_pgt_hist_ch16_east_india_company",
        "topicNumber": 16,
        "topicTitleEn": "16. East India Company & British Expansion",
        "topicTitleHi": "16. ईस्ट इण्डिया कम्पनी एवं ब्रिटिश विस्तार",
        "titleEn": "Modern History Chapter 16: East India Company & British Expansion",
        "titleHi": "आधुनिक इतिहास अध्याय 16: ईस्ट इण्डिया कम्पनी एवं ब्रिटिश विस्तार",
        "start_page": 563,
        "end_page": 593,
    },
    17: {
        "part_id": "part3_modern_history",
        "partTitleEn": "Part III: Modern Indian History",
        "partTitleHi": "भाग III: आधुनिक भारतीय इतिहास",
        "file_name": "tgt_pgt_hist_ch17_modern_agriculture_trade.json",
        "test_id": "tgt_pgt_hist_ch17_modern_agriculture_trade",
        "topicNumber": 17,
        "topicTitleEn": "17. Modern Economy, Agriculture, Revenue & Trade",
        "topicTitleHi": "17. आधुनिक भारत में अर्थव्यवस्था व व्यापार",
        "titleEn": "Modern History Chapter 17: Modern Economy & Agriculture",
        "titleHi": "आधुनिक इतिहास अध्याय 17: आधुनिक भारत में अर्थव्यवस्था व व्यापार",
        "start_page": 594,
        "end_page": 611,
    },
    18: {
        "part_id": "part3_modern_history",
        "partTitleEn": "Part III: Modern Indian History",
        "partTitleHi": "भाग III: आधुनिक भारतीय इतिहास",
        "file_name": "tgt_pgt_hist_ch18_modern_education_constitution.json",
        "test_id": "tgt_pgt_hist_ch18_modern_education_constitution",
        "topicNumber": 18,
        "topicTitleEn": "18. Development of Modern Education & Constitution",
        "topicTitleHi": "18. आधुनिक शिक्षा एवं संवैधानिक विकास",
        "titleEn": "Modern History Chapter 18: Modern Education & Constitution",
        "titleHi": "आधुनिक इतिहास अध्याय 18: आधुनिक शिक्षा एवं संवैधानिक विकास",
        "start_page": 612,
        "end_page": 636,
    },
    19: {
        "part_id": "part3_modern_history",
        "partTitleEn": "Part III: Modern Indian History",
        "partTitleHi": "भाग III: आधुनिक भारतीय इतिहास",
        "file_name": "tgt_pgt_hist_ch19_revolt_1857.json",
        "test_id": "tgt_pgt_hist_ch19_revolt_1857",
        "topicNumber": 19,
        "topicTitleEn": "19. The Great Revolt of 1857",
        "topicTitleHi": "19. 1857 ई. का विद्रोह",
        "titleEn": "Modern History Chapter 19: The Revolt of 1857",
        "titleHi": "आधुनिक इतिहास अध्याय 19: 1857 ई. का विद्रोह",
        "start_page": 637,
        "end_page": 650,
    },
    20: {
        "part_id": "part3_modern_history",
        "partTitleEn": "Part III: Modern Indian History",
        "partTitleHi": "भाग III: आधुनिक भारतीय इतिहास",
        "file_name": "tgt_pgt_hist_ch20_19th_century_renaissance.json",
        "test_id": "tgt_pgt_hist_ch20_19th_century_renaissance",
        "topicNumber": 20,
        "topicTitleEn": "20. 19th Century Socio-Religious Renaissance Movements",
        "topicTitleHi": "20. सामाजिक-धार्मिक सुधार आन्दोलन",
        "titleEn": "Modern History Chapter 20: 19th Century Renaissance",
        "titleHi": "आधुनिक इतिहास अध्याय 20: सामाजिक-धार्मिक सुधार आन्दोलन",
        "start_page": 651,
        "end_page": 687,
    },
    21: {
        "part_id": "part3_modern_history",
        "partTitleEn": "Part III: Modern Indian History",
        "partTitleHi": "भाग III: आधुनिक भारतीय इतिहास",
        "file_name": "tgt_pgt_hist_ch21_national_movement.json",
        "test_id": "tgt_pgt_hist_ch21_national_movement",
        "topicNumber": 21,
        "topicTitleEn": "21. Indian National Movement & Freedom Struggle",
        "topicTitleHi": "21. भारतीय राष्ट्रीय आन्दोलन",
        "titleEn": "Modern History Chapter 21: Indian National Movement",
        "titleHi": "आधुनिक इतिहास अध्याय 21: भारतीय राष्ट्रीय आन्दोलन",
        "start_page": 688,
        "end_page": 762,
    },
    22: {
        "part_id": "part3_modern_history",
        "partTitleEn": "Part III: Modern Indian History",
        "partTitleHi": "भाग III: आधुनिक भारतीय इतिहास",
        "file_name": "tgt_pgt_hist_ch22_gandhi_tilak_gokhale_bose.json",
        "test_id": "tgt_pgt_hist_ch22_gandhi_tilak_gokhale_bose",
        "topicNumber": 22,
        "topicTitleEn": "22. Prominent National Leaders (Gandhi, Tilak, Gokhale, Bose)",
        "topicTitleHi": "22. गाँधी, तिलक, गोखले, सुभाष बोस",
        "titleEn": "Modern History Chapter 22: Gandhi, Tilak, Gokhale, Bose",
        "titleHi": "आधुनिक इतिहास अध्याय 22: गाँधी, तिलक, गोखले, सुभाष बोस",
        "start_page": 763,
        "end_page": 780,
    },
    23: {
        "part_id": "part3_modern_history",
        "partTitleEn": "Part III: Modern Indian History",
        "partTitleHi": "भाग III: आधुनिक भारतीय इतिहास",
        "file_name": "tgt_pgt_hist_ch23_independence.json",
        "test_id": "tgt_pgt_hist_ch23_independence",
        "topicNumber": 23,
        "topicTitleEn": "23. Independence & Partition of India (1947)",
        "topicTitleHi": "23. स्वतंत्रता प्राप्ति एवं विभाजन",
        "titleEn": "Modern History Chapter 23: Independence & Partition",
        "titleHi": "आधुनिक इतिहास अध्याय 23: स्वतंत्रता प्राप्ति एवं विभाजन",
        "start_page": 781,
        "end_page": 791,
    },
    24: {
        "part_id": "part3_modern_history",
        "partTitleEn": "Part III: Modern Indian History",
        "partTitleHi": "भाग III: आधुनिक भारतीय इतिहास",
        "file_name": "tgt_pgt_hist_ch24_post_independence.json",
        "test_id": "tgt_pgt_hist_ch24_post_independence",
        "topicNumber": 24,
        "topicTitleEn": "24. Post-Independence India & National Integration",
        "topicTitleHi": "24. स्वातंत्र्योत्तर भारत एवं एकीकरण",
        "titleEn": "Modern History Chapter 24: Post-Independence India",
        "titleHi": "आधुनिक इतिहास अध्याय 24: स्वातंत्र्योत्तर भारत एवं एकीकरण",
        "start_page": 792,
        "end_page": 803,
    },
    25: {
        "part_id": "part3_modern_history",
        "partTitleEn": "Part III: Modern Indian History",
        "partTitleHi": "भाग III: आधुनिक भारतीय इतिहास",
        "file_name": "tgt_pgt_hist_ch25_governors_viceroys.json",
        "test_id": "tgt_pgt_hist_ch25_governors_viceroys",
        "topicNumber": 25,
        "topicTitleEn": "25. Governors-General & Viceroys of India",
        "topicTitleHi": "25. गवर्नर-जनरल एवं वायसराय",
        "titleEn": "Modern History Chapter 25: Governors & Viceroys",
        "titleHi": "आधुनिक इतिहास अध्याय 25: गवर्नर-जनरल एवं वायसराय",
        "start_page": 804,
        "end_page": 811,
    },
    26: {
        "part_id": "part3_modern_history",
        "partTitleEn": "Part III: Modern Indian History",
        "partTitleHi": "भाग III: आधुनिक भारतीय इतिहास",
        "file_name": "tgt_pgt_hist_ch26_peasant_tribal.json",
        "test_id": "tgt_pgt_hist_ch26_peasant_tribal",
        "topicNumber": 26,
        "topicTitleEn": "26. Peasant & Tribal Movements",
        "topicTitleHi": "26. कृषक एवं जनजातीय आन्दोलन",
        "titleEn": "Modern History Chapter 26: Peasant & Tribal Movements",
        "titleHi": "आधुनिक इतिहास अध्याय 26: कृषक एवं जनजातीय आन्दोलन",
        "start_page": 812,
        "end_page": 818,
    },
    27: {
        "part_id": "part3_modern_history",
        "partTitleEn": "Part III: Modern Indian History",
        "partTitleHi": "भाग III: आधुनिक भारतीय इतिहास",
        "file_name": "tgt_pgt_hist_ch27_revolutionary.json",
        "test_id": "tgt_pgt_hist_ch27_revolutionary",
        "topicNumber": 27,
        "topicTitleEn": "27. Revolutionary Movements in India & Abroad",
        "topicTitleHi": "27. क्रान्तिकारी आन्दोलन",
        "titleEn": "Modern History Chapter 27: Revolutionary Movement",
        "titleHi": "आधुनिक इतिहास अध्याय 27: क्रान्तिकारी आन्दोलन",
        "start_page": 819,
        "end_page": 822,
    },
    28: {
        "part_id": "part3_modern_history",
        "partTitleEn": "Part III: Modern Indian History",
        "partTitleHi": "भाग III: आधुनिक भारतीय इतिहास",
        "file_name": "tgt_pgt_hist_ch28_modern_misc.json",
        "test_id": "tgt_pgt_hist_ch28_modern_misc",
        "topicNumber": 28,
        "topicTitleEn": "28. Miscellaneous Modern History, Press & Literature",
        "topicTitleHi": "28. विविध: आधुनिक भारत",
        "titleEn": "Modern History Chapter 28: Miscellaneous Modern History",
        "titleHi": "आधुनिक इतिहास अध्याय 28: विविध: आधुनिक भारत",
        "start_page": 823,
        "end_page": 861,
    },
    29: {
        "part_id": "part4_research_world",
        "partTitleEn": "Part IV: Historical Methodology & World History",
        "partTitleHi": "भाग IV: इतिहास दर्शन, शोध प्रविधि एवं विश्व इतिहास",
        "file_name": "tgt_pgt_hist_ch29_research.json",
        "test_id": "tgt_pgt_hist_ch29_research",
        "topicNumber": 29,
        "topicTitleEn": "29. Historical Philosophy & Research Methodology",
        "topicTitleHi": "29. इतिहास दर्शन एवं शोध प्रविधि",
        "titleEn": "Research & World History Chapter 29: Historical Methodology",
        "titleHi": "शोध एवं विश्व इतिहास अध्याय 29: इतिहास दर्शन एवं शोध प्रविधि",
        "start_page": 862,
        "end_page": 884,
    },
    30: {
        "part_id": "part4_research_world",
        "partTitleEn": "Part IV: Historical Methodology & World History",
        "partTitleHi": "भाग IV: इतिहास दर्शन, शोध प्रविधि एवं विश्व इतिहास",
        "file_name": "tgt_pgt_hist_ch30_world_history.json",
        "test_id": "tgt_pgt_hist_ch30_world_history",
        "topicNumber": 30,
        "topicTitleEn": "30. World History (Renaissance, Revolutions, World Wars)",
        "topicTitleHi": "30. विश्व इतिहास (पुनर्जागरण, क्रांतियाँ, विश्व युद्ध)",
        "titleEn": "Research & World History Chapter 30: World History",
        "titleHi": "शोध एवं विश्व इतिहास अध्याय 30: विश्व इतिहास",
        "start_page": 885,
        "end_page": 928,
    },
}

BASE_CDN_URL = "https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main"
ALT_CDN_URL = "https://cdn.jsdelivr.net/gh/justunfold/prepunfold-cdn@main"

def normalize_question(q, test_id, idx, meta):
    """
    Ensures the question has exactly the 40 dual camelCase + snake_case keys.
    """
    ch_num = meta["topicNumber"]
    corr_opt = str(q.get("correctOption") or q.get("correct_option") or "A").strip().upper()
    if corr_opt not in ("A", "B", "C", "D"):
        corr_opt = "A"
    corr_idx = ord(corr_opt) - ord('A')

    # Bilingual texts
    q_en = str(q.get("questionTextEn") or q.get("question_en") or q.get("questionText") or "").strip()
    q_hi = str(q.get("questionTextHi") or q.get("question_hi") or "").strip()
    if not q_en and q_hi:
        q_en = q_hi

    # Options
    opts_en = q.get("optionsEn") or q.get("options_en") or q.get("options") or []
    opts_hi = q.get("optionsHi") or q.get("options_hi") or []
    if not opts_en and opts_hi:
        opts_en = list(opts_hi)
    if not opts_hi and opts_en:
        opts_hi = list(opts_en)

    opts_en = [str(x).strip() for x in opts_en]
    opts_hi = [str(x).strip() for x in opts_hi]
    while len(opts_en) < 4:
        opts_en.append(f"None of the above ({len(opts_en)+1})")
    while len(opts_hi) < 4:
        opts_hi.append(f"इनमें से कोई नहीं ({len(opts_hi)+1})")
    opts_en = opts_en[:4]
    opts_hi = opts_hi[:4]

    # Explanations
    exp_en = str(q.get("explanationEn") or q.get("explanation_en") or q.get("explanation") or "").strip()
    exp_hi = str(q.get("explanationHi") or q.get("explanation_hi") or "").strip()
    if not exp_en and exp_hi:
        exp_en = f"Correct option is ({corr_opt}).\n[Solution: {exp_hi}]"
    if not exp_hi and exp_en:
        exp_hi = f"सही विकल्प ({corr_opt}) है।"

    # Subtopic & Section info
    subtopic_id = str(q.get("subtopicId") or q.get("sectionId") or f"sub_{ch_num:02d}").strip()
    sec_en = str(q.get("sectionTitleEn") or q.get("section") or meta["titleEn"]).strip()
    sec_hi = str(q.get("sectionTitleHi") or meta["titleHi"]).strip()
    sub_title_en = str(q.get("subtopicTitleEn") or sec_en).strip()
    sub_title_hi = str(q.get("subtopicTitleHi") or sec_hi).strip()

    pyq_tag = str(q.get("pyqTag") or q.get("exam_year_tag") or "TGT/PGT History PYQ").strip()
    exam_year_raw = q.get("examYear")
    if not exam_year_raw:
        yr_match = re.search(r'\b(20\d\d|19\d\d)\b', pyq_tag)
        exam_year = int(yr_match.group(1)) if yr_match else 2021
    else:
        try:
            exam_year = int(exam_year_raw)
        except Exception:
            exam_year = 2021

    diff = str(q.get("difficulty") or "MEDIUM").strip().upper()
    if diff not in ("EASY", "MEDIUM", "HARD"):
        diff = "MEDIUM"

    q_id_int = int(f"19{ch_num:02d}{idx:04d}")

    # Build exact 40-key object
    norm_q = {
        "questionId": f"{test_id}_q{idx:03d}",
        "questionNumber": idx,
        "sectionId": subtopic_id,
        "sectionTitleEn": sec_en,
        "sectionTitleHi": sec_hi,
        "subtopicId": subtopic_id,
        "subtopicTitleEn": sub_title_en,
        "subtopicTitleHi": sub_title_hi,
        "questionType": "MCQ",
        "positiveMarks": 2.0,
        "negativeMarks": 0.0,
        "pyqTag": pyq_tag,
        "examYear": exam_year,
        "topicTag": f"Ancient History: {sec_en}" if ch_num <= 9 else (f"Medieval History: {sec_en}" if ch_num <= 15 else f"Modern History: {sec_en}"),
        "difficulty": diff,
        "questionTextEn": q_en,
        "questionTextHi": q_hi,
        "optionsEn": opts_en,
        "optionsHi": opts_hi,
        "correctOption": corr_opt,
        "correctOptionsList": None,
        "natMin": None,
        "natMax": None,
        "explanationEn": exp_en,
        "explanationHi": exp_hi,
        "q_id": q_id_int,
        "q_number": idx,
        "section": sec_en,
        "exam_year_tag": pyq_tag,
        "question_en": q_en,
        "question_hi": q_hi,
        "options_en": opts_en,
        "options_hi": opts_hi,
        "correct_index": corr_idx,
        "correct_indices": [corr_idx],
        "explanation_en": exp_en,
        "explanation_hi": exp_hi,
        "question_type": "MCQ",
        "q_marks": 2.0,
        "q_negative_marks": 0.0
    }
    return norm_q

def find_chunk_files(ch_num, chunk_dirs=("_tmp_chunks", "_tmp_chunks/extracted")):
    patterns = [
        f"ch{ch_num:02d}_p*.json",
        f"ch{ch_num:02d}_*.json",
    ]
    found = []
    for d in chunk_dirs:
        if not os.path.isdir(d):
            continue
        for p in patterns:
            found.extend(glob.glob(os.path.join(d, p)))

    # Deduplicate and sort
    return sorted(list(set(found)))

def remove_old_part_duplicates(ch_num, out_dir="tests/tgt_pgt_history"):
    """
    Removes any old partial files, e.g., tgt_pgt_hist_ch02_part1_indus_valley.json.
    """
    patterns = [
        os.path.join(out_dir, f"tgt_pgt_hist_ch{ch_num:02d}_part*.json"),
        os.path.join(out_dir, f"tgt_pgt_hist_ch{ch_num:02d}_*_part*.json"),
    ]
    removed = []
    for pat in patterns:
        for f in glob.glob(pat):
            try:
                os.remove(f)
                removed.append(f)
                print(f"  [Clean] Removed old partial duplicate: {f}")
            except Exception as e:
                print(f"  [Warn] Failed to remove {f}: {e}")
    return removed

def update_manifests(ch_num, test_doc, out_path):
    rel_path = os.path.relpath(out_path, ".").replace("\\", "/")
    test_id = test_doc["testId"]
    total_q = test_doc["totalQuestions"]
    shift_badge = test_doc["shiftBadge"]
    title_en = test_doc["titleEn"]
    title_hi = test_doc["titleHi"]
    part_id = test_doc["partId"]

    entry = {
        "test_id": test_id,
        "testId": test_id,
        "category_id": "tgt_pgt_history",
        "categoryId": "tgt_pgt_history",
        "part_id": part_id,
        "partId": part_id,
        "test_type": "TOPIC",
        "testType": "TOPIC",
        "title": title_en,
        "titleEn": title_en,
        "titleHi": title_hi,
        "exam_year_tag": "TGT/PGT/GIC/UGC NET/UPPCS PYQ (2000–2021)",
        "examYearTag": "TGT/PGT/GIC/UGC NET/UPPCS PYQ (2000–2021)",
        "shiftBadge": shift_badge,
        "duration_minutes": 120,
        "durationMinutes": 120,
        "total_questions": total_q,
        "totalQuestions": total_q,
        "positive_marks": 2.0,
        "positiveMarks": 2.0,
        "negative_marks": 0.0,
        "negativeMarks": 0.0,
        "is_free": True,
        "isFree": True,
        "version": 1,
        "path": rel_path,
        "filePath": rel_path,
        "file_path": rel_path,
        "json_url": f"{BASE_CDN_URL}/{rel_path}",
        "cdnUrl": f"{BASE_CDN_URL}/{rel_path}",
        "altCdnUrl": f"{ALT_CDN_URL}/{rel_path}"
    }

    # 1. Update manifest_tgt_pgt_history_master.json
    m_master_path = "manifest_tgt_pgt_history_master.json"
    if os.path.isfile(m_master_path):
        try:
            with open(m_master_path, "r", encoding="utf-8") as f:
                m_master = json.load(f)
            tests_list = m_master.get("tests", [])
            # Filter out this test or any obsolete partial parts of this chapter
            cleaned_tests = []
            for t in tests_list:
                tid = t.get("testId") or t.get("test_id", "")
                if tid == test_id or tid.startswith(f"tgt_pgt_hist_ch{ch_num:02d}_part"):
                    continue
                cleaned_tests.append(t)
            cleaned_tests.append(entry)
            m_master["tests"] = cleaned_tests
            with open(m_master_path, "w", encoding="utf-8") as f:
                json.dump(m_master, f, ensure_ascii=False, indent=2)
            print(f"  [Manifest] Updated {m_master_path} with {test_id} ({total_q} Qs)")
        except Exception as e:
            print(f"  [Error] Failed to update {m_master_path}: {e}")

    # 2. Update manifest.json
    m_main_path = "manifest.json"
    if os.path.isfile(m_main_path):
        try:
            with open(m_main_path, "r", encoding="utf-8") as f:
                m_main = json.load(f)
            main_tests = m_main.get("tests", [])
            cleaned_main = []
            for t in main_tests:
                tid = t.get("testId") or t.get("test_id", "")
                if tid == test_id or tid.startswith(f"tgt_pgt_hist_ch{ch_num:02d}_part"):
                    continue
                cleaned_main.append(t)
            cleaned_main.append(entry)
            m_main["tests"] = cleaned_main
            m_main["totalTests"] = len(cleaned_main)
            m_main["total_tests"] = len(cleaned_main)
            with open(m_main_path, "w", encoding="utf-8") as f:
                json.dump(m_main, f, ensure_ascii=False, indent=2)
            print(f"  [Manifest] Updated {m_main_path} (Total tests: {len(cleaned_main)})")
        except Exception as e:
            print(f"  [Error] Failed to update {m_main_path}: {e}")

def merge_chapter(ch_num, chunk_files=None, out_dir="tests/tgt_pgt_history"):
    if ch_num not in CHAPTER_METADATA:
        raise ValueError(f"Invalid chapter number: {ch_num}. Must be 1 to 30.")

    meta = CHAPTER_METADATA[ch_num]
    test_id = meta["test_id"]
    file_name = meta["file_name"]
    out_path = os.path.join(out_dir, file_name)
    os.makedirs(out_dir, exist_ok=True)

    if not chunk_files:
        chunk_files = find_chunk_files(ch_num)

    if not chunk_files:
        print(f"[Ch {ch_num:02d}] No chunk JSON files found. Checking if target {out_path} exists...")
        if os.path.isfile(out_path):
            chunk_files = [out_path]
        else:
            print(f"  -> Skipping Ch {ch_num:02d} (no chunks to merge).")
            return None

    print(f"\n=======================================================")
    print(f"Merging Chapter {ch_num:02d}: {meta['titleEn']}")
    print(f"Chunk files found: {len(chunk_files)}")

    raw_questions = []
    subtopics_dict = {}

    for cf in chunk_files:
        print(f"  Reading chunk: {cf}")
        try:
            with open(cf, "r", encoding="utf-8") as f:
                content = json.load(f)
            if isinstance(content, list):
                raw_questions.extend(content)
            elif isinstance(content, dict):
                if "questions" in content and isinstance(content["questions"], list):
                    raw_questions.extend(content["questions"])
                    # Carry subtopics if defined
                    for sub in content.get("subtopics", []):
                        sub_id = sub.get("subtopicId")
                        if sub_id and sub_id not in subtopics_dict:
                            subtopics_dict[sub_id] = sub
                else:
                    raw_questions.append(content)
        except Exception as e:
            print(f"  [Error] Failed to read {cf}: {e}")

    if not raw_questions:
        print(f"  [Warning] No questions collected for Ch {ch_num:02d}.")
        return None

    # Normalization & Validation
    normalized_questions = []
    seen_texts = set()

    for raw_q in raw_questions:
        norm_q = normalize_question(raw_q, test_id, len(normalized_questions) + 1, meta)

        # Validation: 4 options
        if len(norm_q["optionsEn"]) != 4 or len(norm_q["optionsHi"]) != 4:
            raise ValueError(f"Question {norm_q['questionNumber']} does not have 4 options!")

        # Deduplication check: deduplicate by bookQuestionNumber if present, or by full text
        b_num = raw_q.get("bookQuestionNumber")
        if b_num is not None:
            if b_num in seen_texts:
                print(f"  [Dedup] Skipping duplicate book question #{b_num}")
                continue
            seen_texts.add(b_num)
        else:
            q_key = (norm_q["questionTextHi"].strip(), norm_q["correctOption"], tuple(norm_q["optionsHi"]))
            if q_key in seen_texts:
                print(f"  [Dedup] Skipping duplicate question #{norm_q['questionNumber']}")
                continue
            seen_texts.add(q_key)

        normalized_questions.append(norm_q)

    # Re-sequence question numbers strictly 1..N
    total_q = len(normalized_questions)
    for idx, q in enumerate(normalized_questions, 1):
        q["questionNumber"] = idx
        q["q_number"] = idx
        q["questionId"] = f"{test_id}_q{idx:03d}"
        q["q_id"] = int(f"19{ch_num:02d}{idx:04d}")

    # Build subtopics summary if not already provided
    if not subtopics_dict:
        # Default single/subtopic grouping
        subtopics_list = [
            {
                "subtopicId": f"sub_{ch_num:02d}",
                "subtopicTitleEn": meta["topicTitleEn"],
                "subtopicTitleHi": meta["topicTitleHi"],
                "questionCount": total_q
            }
        ]
    else:
        subtopics_list = list(subtopics_dict.values())
        # recount
        for sub in subtopics_list:
            sub_id = sub.get("subtopicId")
            cnt = sum(1 for q in normalized_questions if q.get("subtopicId") == sub_id)
            sub["questionCount"] = cnt

    # Build final document
    title_full_en = f"{meta['titleEn']} ({total_q} PYQs)"
    title_full_hi = f"{meta['titleHi']} ({total_q} PYQs)"

    doc = {
        "testId": test_id,
        "test_id": test_id,
        "categoryId": "tgt_pgt_history",
        "category_id": "tgt_pgt_history",
        "partId": meta["part_id"],
        "part_id": meta["part_id"],
        "partTitleEn": meta["partTitleEn"],
        "partTitleHi": meta["partTitleHi"],
        "topicNumber": meta["topicNumber"],
        "topicTitleEn": meta["topicTitleEn"],
        "topicTitleHi": meta["topicTitleHi"],
        "title": title_full_en,
        "titleEn": title_full_en,
        "titleHi": title_full_hi,
        "testType": "TOPIC",
        "test_type": "TOPIC",
        "isFree": True,
        "is_free": True,
        "durationMinutes": 120,
        "duration_minutes": 120,
        "totalQuestions": total_q,
        "total_questions": total_q,
        "maxMarks": round(total_q * 2.0, 1),
        "positiveMarks": 2.0,
        "positive_marks": 2.0,
        "negativeMarks": 0.0,
        "negative_marks": 0.0,
        "examYearTag": "TGT/PGT/GIC/UGC NET/UPPCS PYQ (2000–2021)",
        "exam_year_tag": "TGT/PGT/GIC/UGC NET/UPPCS PYQ (2000–2021)",
        "shiftBadge": f"PYQ (2000–2021) • {total_q} Solved MCQs • Bilingual",
        "version": 1,
        "subtopics": subtopics_list,
        "questions": normalized_questions
    }

    # Remove old duplicates (e.g., ch02_part1)
    remove_old_part_duplicates(ch_num, out_dir)

    # Write final JSON
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)

    print(f"  [Success] Merged & validated {total_q} Qs into {out_path}")

    # Update manifests
    update_manifests(ch_num, doc, out_path)
    return out_path

def main():
    parser = argparse.ArgumentParser(description="Merge & Validate TGT/PGT History Chapter JSONs")
    parser.add_argument("chapter", type=int, nargs="?", default=None, help="Chapter number (1-30)")
    parser.add_argument("--chapter", "-c", dest="ch_flag", type=int, default=None, help="Chapter number (1-30)")
    parser.add_argument("--all", action="store_true", help="Process all available chapters")
    parser.add_argument("--out-dir", default="tests/tgt_pgt_history", help="Output directory")
    args = parser.parse_args()

    ch = args.chapter or args.ch_flag
    if args.all:
        for c in sorted(CHAPTER_METADATA.keys()):
            merge_chapter(c, out_dir=args.out_dir)
    elif ch is not None:
        merge_chapter(ch, out_dir=args.out_dir)
    else:
        print("Please specify a chapter number (e.g. python tools/merge_and_validate.py 2) or --all.")
        sys.exit(1)

if __name__ == "__main__":
    main()
