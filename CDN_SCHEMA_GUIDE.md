# AbhyasDesk CDN & Manifest Architecture Guide (`prepunfold-cdn`)

This document defines the unified, production-standard directory structure, manifest schema, and payment contract for the **AbhyasDesk** Android application and CDN repository (`prepunfold-cdn`).

---

## 1. Directory Layout Standard

Every exam stream must follow this exact 4-folder structure under `tests/<exam_group>/<exam_stream>/`:

```text
tests/<exam_group>/<exam_stream>/
  ├── full_mocks/                 # Full-length exam-pattern mocks (e.g., 125 Qs TGT/PGT, 65 Qs GATE)
  ├── sectional_tests/            # Single-unit / subject mini-mocks (e.g., Microeconomics Mock)
  ├── pyq/                        # Official Previous Year Question papers (tagged by board & year)
  └── topic_tests/                # Chapter/subtopic tests (flat or in <unit_slug>/ folders)
```

### Stream Hierarchy
| Exam Group (`<exam_group>`) | Exam Stream (`<exam_stream>`) | Content Folders Active |
|---|---|---|
| `teaching` | `tgt_pgt_economics` | `full_mocks/`, `sectional_tests/`, `pyq/`, `topic_tests/` |
| `teaching` | `tgt_pgt_geography` | `full_mocks/`, `sectional_tests/`, `pyq/`, `topic_tests/` |
| `teaching` | `tgt_pgt_civics` | `sectional_tests/`, `pyq/` |
| `teaching` | `tgt_pgt_history` | `sectional_tests/`, `pyq/` |
| `gate` | `gate_ph` | `full_mocks/`, `pyq/`, `topic_tests/<01_unit_slug>/` |
| `gate` | `gate_cs`, `gate_ma`, `gate_cy` | `full_mocks/` or `pyq/` |
| `jam` | `jam_ph`, `jam_ma`, `jam_cy` | `full_mocks/` |
| `state_psc` | `uppcs_pre` | `pyq/`, `sectional_tests/` |
| `upsc` | `upsc_cse` | `sectional_tests/`, `topic_tests/<unit_slug>/` |
| `ssc` | `ssc_gd`, `ssc_chsl` | `full_mocks/` |
| `railway` | `rrb_ntpc` | `full_mocks/` |
| `general` | `current_affairs` | `full_mocks/`, `sectional_tests/` |

> [!CAUTION]
> **Protected Path**: `tests/geography_pyq_1993_2026/` is a legacy compendium root. Do NOT move, rename, or alter files inside this folder.

---

## 2. Bilingual File Standard (Never Split en/ and hi/)

**Rule**: Keep English and Hindi together in the same test JSON file. **Never** split into `en/` and `hi/` subfolders.

Every question object contains:
```json
{
  "questionNumber": 1,
  "questionText": "English Question Text",
  "questionTextEn": "English Question Text",
  "questionTextHi": "हिन्दी प्रश्न पाठ",
  "options": ["Option A", "Option B", "Option C", "Option D"],
  "optionsEn": ["Option A", "Option B", "Option C", "Option D"],
  "optionsHi": ["विकल्प क", "विकल्प ख", "विकल्प ग", "विकल्प घ"],
  "correctAnswerIndex": 1,
  "explanation": "Detailed explanation in English",
  "explanationEn": "Detailed explanation in English",
  "explanationHi": "विस्तृत व्याख्या हिन्दी में"
}
```

---

## 3. Standardized Test Types (`test_type` / `testType`)

All tests inside `manifest.json` and in individual test files must strictly use one of these four values:

1. **`"FULL_MOCK"`**: Full-length exam-pattern mock tests covering the entire exam syllabus (e.g., 65 questions for GATE, 100/125 questions for TGT/PGT, 100 questions for CSAT/Annual CA).
2. **`"PYQ"`**: Official Previous Year Question papers. Must include `exam_year_tag` / `examYearTag` and `shiftBadge` (e.g. `"UP PGT 2021"`, `"GATE PH 2024"`).
3. **`"SECTIONAL"`**: Unit-level or subject-level mini-mocks (e.g., Microeconomics Mock, Geomorphology Mock, Indian Constitution Mock).
4. **`"TOPIC"`**: Chapter-wise or subtopic-wise practice tests. Must have `part_id` / `partId` mapping to a valid part in the category's `parts[]`.

### Sorting Order in Categories
Tests within any category in `manifest.json` are sorted strictly in this order:
$$\text{FULL\_MOCK} \longrightarrow \text{PYQ} \longrightarrow \text{SECTIONAL} \longrightarrow \text{TOPIC}$$
Within `"TOPIC"`, tests are ordered by the category's `parts[].order`, then by chapter/test order.

---

## 4. 2-Level Unit Grouping (`parts[]` and `part_id`)

For any category containing `"TOPIC"` tests, `parts[]` must be defined on the category in `manifest.json`, and every `"TOPIC"` test must have a matching `part_id` / `partId`:

### Example: `gate_ph` Parts
11 revised GATE Physics syllabus sections:
- `01_measurements_error_analysis`
- `02_mathematical_physics`
- `03_classical_mechanics`
- `04_electromagnetic_theory`
- `05_quantum_mechanics`
- `06_optical_physics`
- `07_thermodynamics_stat_physics`
- `08_atomic_molecular_physics`
- `09_solid_state_physics`
- `10_electronics`
- `11_nuclear_particle_physics`

### Example: `tgt_pgt_economics` Parts
6 syllabus units:
1. `microeconomics` (Chapters 01–06)
2. `macroeconomics` (Chapters 07–08)
3. `public_finance` (Chapters 09–13)
4. `money_banking` (Chapters 14–18)
5. `international_trade` (Chapters 19–22)
6. `indian_economy` (Chapters 23–31)

### Example: `tgt_pgt_geography` Parts
5 syllabus units:
1. `geographical_thought` (Chapter 01)
2. `physical_geography` (Chapters 02–08)
3. `human_economic_geography` (Chapters 09–12)
4. `indian_geography` (Chapters 13–14)
5. `practical_cartography` (Chapter 15)

---

## 5. Payment, Bundles & Price-Tier SKU Schema

To avoid Play Store SKU explosion and maintain clean pricing tiers, AbhyasDesk uses reusable price-tier product IDs:

### Standard SKUs
| SKU | Price | Strike Price | Validity | Primary Use Case |
|---|---|---|---|---|
| `tier_49` | ₹49 | ₹149 | 180 Days | Single Teaching / SSC / Railway Subject (6M) |
| `tier_89` | ₹89 | ₹249 | 365 Days | Single Teaching / SSC / Railway Subject (1Y) |
| `tier_99` | ₹99 | ₹249 | 180 Days | Single GATE / State PSC / Combo 6M |
| `tier_179` | ₹179 | ₹399 | 365 Days | Single GATE / State PSC (1Y) & Combo 1Y / All-Access 6M |
| `tier_399` | ₹399 | ₹999 | 365 Days | All-Access Pass (1Y) |

### Category Fields
Every category in `manifest.json` includes:
```json
{
  "id": "tgt_pgt_economics",
  "exam_group": "teaching",
  "examGroup": "teaching",
  "unlocks_categories": ["tgt_pgt_economics"],
  "pass_6m_sku": "tier_49",
  "pass_6m_product_id": "pass_tgt_pgt_econ_6m_49",
  "pass_6m_price": "₹49",
  "pass_6m_strike_price": "₹149",
  "pass_6m_days": 180,
  "pass_1y_sku": "tier_89",
  "pass_1y_product_id": "pass_tgt_pgt_econ_1y_89",
  "pass_1y_price": "₹89",
  "pass_1y_strike_price": "₹249",
  "pass_1y_days": 365
}
```

### Top-Level Bundles
`manifest.json` provides a `bundles` array:
```json
"bundles": [
  {
    "bundle_id": "bundle_tgt_pgt_sst",
    "bundleId": "bundle_tgt_pgt_sst",
    "title": "TGT/PGT Social Science Combo (सामाजिक विज्ञान कॉम्बो)",
    "titleEn": "TGT/PGT Social Science Combo (Economics, Geography, History, Civics)",
    "titleHi": "टीजीटी/पीजीटी सामाजिक विज्ञान कॉम्बो (अर्थशास्त्र, भूगोल, इतिहास, नागरिक शास्त्र)",
    "exam_group": "teaching",
    "unlocks_categories": [
      "tgt_pgt_geography",
      "tgt_pgt_economics",
      "tgt_pgt_history",
      "tgt_pgt_civics"
    ],
    "pass_6m_sku": "tier_99",
    "pass_6m_price": "₹99",
    "pass_6m_strike_price": "₹249",
    "pass_6m_days": 180,
    "pass_1y_sku": "tier_179",
    "pass_1y_price": "₹179",
    "pass_1y_strike_price": "₹399",
    "pass_1y_days": 365,
    "is_active": true
  },
  {
    "bundle_id": "bundle_all_access",
    "bundleId": "bundle_all_access",
    "title": "AbhyasDesk All-Access Pass (संपूर्ण एक्सेस पास)",
    "titleEn": "AbhyasDesk All-Access Pass (All Exams & Streams)",
    "titleHi": "अभ्यासडेस्क संपूर्ण एक्सेस पास (सभी परीक्षाएं एवं विषय)",
    "exam_group": "all",
    "unlocks_categories": ["*"],
    "pass_6m_sku": "tier_179",
    "pass_6m_price": "₹179",
    "pass_6m_strike_price": "₹499",
    "pass_6m_days": 180,
    "pass_1y_sku": "tier_399",
    "pass_1y_price": "₹399",
    "pass_1y_strike_price": "₹999",
    "pass_1y_days": 365,
    "is_active": true
  }
]
```

### Remote Config Protection
`remote_config.active_play_product_id` must point to `"tier_179"` (All-Access Pass tier), ensuring global Pro passes do not undercut individual single-subject passes.

---

## 6. Backward Compatibility Key Mapping

To support existing and upcoming app releases without breaking, the following keys are duplicated in both `snake_case` and `camelCase`:
- `test_id` / `testId`
- `category_id` / `categoryId`
- `test_type` / `testType`
- `exam_year_tag` / `examYearTag`
- `duration_minutes` / `durationMinutes`
- `total_questions` / `totalQuestions`
- `positive_marks` / `positiveMarks`
- `negative_marks` / `negativeMarks`
- `is_free` / `isFree`
- `part_id` / `partId`
- `filePath` / `path` / `file_path`
- `json_url` / `cdnUrl` / `altCdnUrl`

---

## 7. Automated Validation

Run the validator anytime changes are made to files or manifest:
```bash
python scripts/validate_manifest.py
```

The script verifies:
1. Every path in `manifest.json` exists on disk.
2. Every `test_type` is in `{"FULL_MOCK", "PYQ", "SECTIONAL", "TOPIC"}`.
3. Every `"TOPIC"` test has a valid `part_id` defined in its category `parts[]`.
4. Zero broken JSON files on disk.
5. Zero duplicate `test_id`s.
6. `tests/geography_pyq_1993_2026/` remains untouched with all 83 files intact.
