# AbhyasDesk (`prepunfold-cdn`) — Modular Language & Topic-Wise Folder Architecture + Agent Migration Prompt

This guide defines the **new modular, language-isolated, topic-wise directory structure** for `prepunfold-cdn` and gives you the **exact copy-paste prompt** for your agent to reorganize the existing repository, prune all cloned/fake legacy files identified in your audit, and set up dedicated folders for **PYQs, Mock Tests, Topic-Wise Tests, Short Notes, and Videos** under each language (`en/` and `hi/`).

---

## 1. Visual Blueprint of the New `prepunfold-cdn` Folder Structure

By grouping exams under their **Exam Family (`gate/`, `jam/`, `upsc/`, `state_psc/`, `teaching/`, `ssc/`, `railway/`)**, splitting each exam into **Language Folders (`en/` and `hi/`)**, and organizing content into **`pyq/`**, **`mock_tests/`**, **`topic_tests/<topic_slug>/`**, **`short_notes/`**, and **`videos/`**, you get three major benefits:
1. **Update One Language Without Touching the Other:** If you want to fix or add Hindi translations for `gate_ph` or `upsc_cse`, you only edit files inside `.../hi/`—the English `.../en/` files are never touched or broken.
2. **Topic-Wise Scalability:** Every subject/topic has its own subfolder inside `topic_tests/<topic_slug>/`, `short_notes/<topic_slug>/`, and `videos/<topic_slug>/`, so you can add Topic Test 1, Topic Test 2, PDF/Markdown Short Notes, Formula Sheets, and YouTube/Video Lecture JSONs per topic anytime.
3. **Zero Clutter:** All 12 exam categories follow the exact same predictable path convention.

```text
prepunfold-cdn/
├── manifest.json                                  # Master CDN index (links en/, hi/, notes & videos)
├── exams/
│   ├── gate/                                      # 1. ALL GATE EXAMS IN ONE FAMILY FOLDER
│   │   ├── gate_ph/                               # GATE Physics (PH)
│   │   │   ├── exam_config.json                   # Syllabus tree, marking scheme, topic list
│   │   │   ├── en/                                # ENGLISH LANGUAGE FOLDER
│   │   │   │   ├── pyq/
│   │   │   │   │   ├── gate_ph_pyq_2025.json
│   │   │   │   │   └── gate_ph_pyq_2024.json
│   │   │   │   ├── mock_tests/
│   │   │   │   │   ├── gate_ph_mock_01.json
│   │   │   │   │   └── gate_ph_mock_02.json
│   │   │   │   ├── topic_tests/
│   │   │   │   │   ├── 01_mathematical_physics/
│   │   │   │   │   │   ├── sub_01_linear_algebra_vector_calc.json
│   │   │   │   │   │   ├── sub_02_complex_analysis.json
│   │   │   │   │   │   └── sub_03_differential_equations.json
│   │   │   │   │   ├── 02_classical_mechanics/
│   │   │   │   │   ├── 03_electromagnetic_theory/
│   │   │   │   │   ├── 04_quantum_mechanics/
│   │   │   │   │   ├── 05_thermodynamics_stat_physics/
│   │   │   │   │   ├── 06_atomic_molecular_physics/
│   │   │   │   │   ├── 07_solid_state_physics/
│   │   │   │   │   ├── 08_electronics/
│   │   │   │   │   └── 09_nuclear_particle_physics/
│   │   │   │   ├── short_notes/
│   │   │   │   │   ├── 01_mathematical_physics/
│   │   │   │   │   │   └── formula_revision_notes.json
│   │   │   │   │   └── ...
│   │   │   │   └── videos/
│   │   │   │       ├── 01_mathematical_physics/
│   │   │   │       │   └── video_playlist.json
│   │   │   │       └── ...
│   │   │   └── hi/                                # HINDI LANGUAGE FOLDER (Mirrors en/ 1:1)
│   │   │       ├── pyq/
│   │   │       │   ├── gate_ph_pyq_2025.json
│   │   │       │   └── gate_ph_pyq_2024.json
│   │   │       ├── mock_tests/
│   │   │       ├── topic_tests/
│   │   │       │   ├── 01_mathematical_physics/
│   │   │       │   │   └── sub_01_linear_algebra_vector_calc.json
│   │   │       │   └── ...
│   │   │       ├── short_notes/
│   │   │       └── videos/
│   │   ├── gate_cs/                               # GATE Computer Science (CS) -> en/ & hi/
│   │   ├── gate_cy/                               # GATE Chemistry (CY) -> en/ & hi/
│   │   └── gate_ma/                               # GATE Mathematics (MA) -> en/ & hi/
│   │
│   ├── jam/                                       # 2. ALL IIT JAM EXAMS
│   │   ├── jam_ph/                                # en/ & hi/ -> pyq/, mock_tests/, topic_tests/, short_notes/, videos/
│   │   ├── jam_cy/
│   │   └── jam_ma/
│   │
│   ├── upsc/                                      # 3. UPSC CIVIL SERVICES
│   │   └── upsc_cse/
│   │       ├── en/
│   │       │   ├── pyq/
│   │       │   │   ├── upsc_cse_geo_pyq_ias_special_1.json
│   │       │   │   └── upsc_cse_geo_pyq_ias_special_2.json
│   │       │   ├── mock_tests/
│   │       │   ├── topic_tests/
│   │       │   │   ├── ind_01_intro_frontiers/
│   │       │   │   ├── ind_02_physiography/
│   │       │   │   ├── ...
│   │       │   │   └── world_06_economic_resources/
│   │       │   ├── short_notes/
│   │       │   └── videos/
│   │       └── hi/
│   │
│   ├── state_psc/                                 # 4. STATE PSC EXAMS (UPPCS, BPSC, MPPSC)
│   │   └── uppcs_pre/                             # en/ & hi/ -> pyq/, csat_pyq/, mock_tests/, topic_tests/, short_notes/, videos/
│   │
│   ├── teaching/                                  # 5. TEACHING & UGC NET EXAMS
│   │   └── tgt_pgt_econ_geo/                      # en/ & hi/ -> pyq/, mock_tests/, topic_tests/, short_notes/, videos/
│   │
│   ├── ssc/                                       # 6. SSC EXAMS
│   │   ├── ssc_gd/                                # en/ & hi/ -> pyq/, mock_tests/, topic_tests/, short_notes/, videos/
│   │   └── ssc_chsl/
│   │
│   └── railway/                                   # 7. RAILWAY (RRB) EXAMS
│       └── rrb_ntpc/                              # en/ & hi/ -> pyq/, mock_tests/, topic_tests/, short_notes/, videos/
│
└── tests/
    └── geography_pyq_1993_2026/                   # UNTOUCHED GHATNA CHAKRA COMPENDIUM (83 Papers, 3,495 Qs)
```

---

## 2. Copy-Paste Prompt for Your Agent to Rearrange the Repository & Clean Up Clones

Copy and paste the block below into your agent so it restructures `prepunfold-cdn` into the new modular architecture, splits existing bilingual files into `en/` and `hi/` folders, creates the `pyq/`, `mock_tests/`, `topic_tests/<topic_slug>/`, `short_notes/`, and `videos/` directories, and deletes all fake cloned papers found in the audit:

```markdown
# ROLE & MISSION: RESTRUCTURE `prepunfold-cdn` INTO MODULAR LANGUAGE & TOPIC-WISE ARCHITECTURE

You are a Senior Data & Repository Architect working on `prepunfold-cdn` for the **AbhyasDesk** (`com.justunfold.prepunfold`) app.

Your task is to **reorganize the repository into a clean, modular, language-isolated (`en/` and `hi/`), topic-wise directory structure** so that:
1. All exams are grouped under `exams/<exam_family>/<exam_id>/` (e.g., `exams/gate/gate_ph/`, `exams/gate/gate_cs/`, `exams/gate/gate_cy/`, `exams/gate/gate_ma/`, `exams/jam/jam_ph/`, `exams/upsc/upsc_cse/`, `exams/state_psc/uppcs_pre/`, `exams/teaching/tgt_pgt_econ_geo/`, `exams/ssc/ssc_gd/`, `exams/ssc/ssc_chsl/`, `exams/railway/rrb_ntpc/`).
2. Inside every `<exam_id>/` folder, there are separate **language folders (`en/` and `hi/`)** so that updating English or Hindi in the future only touches that specific language folder.
3. Inside each language folder (`en/` and `hi/`), content is organized into 5 clean sub-folders:
   - `pyq/` — Official Previous Year Question papers
   - `mock_tests/` — Full-Length Mock Test papers
   - `topic_tests/<topic_slug>/` — Separate folder per subject/topic so multiple tests can be added per topic
   - `short_notes/<topic_slug>/` — For topic-wise short notes, formula sheets, and revision cards (`notes_index.json`)
   - `videos/<topic_slug>/` — For topic-wise video lectures and solution playlists (`videos_index.json`)

---

## CRITICAL RULES FOR THIS MIGRATION

### Rule 1: Keep `tests/geography_pyq_1993_2026/` 100% Untouched
- Do **NOT** move, rename, edit, or delete `tests/geography_pyq_1993_2026/` (the 83 Ghatna Chakra Geography topic papers, 3,495 Qs) or its entries in `manifest.json`.

### Rule 2: Purge the Cloned Synthetic Pools During Migration (Keep Only Real / Unique Papers)
Based on our audit report, **do NOT migrate the fake cloned duplicate files** into the new structure—delete them so we start clean and build authentic papers one by one:
1. **`gate_ph`:**
   - **KEEP & MIGRATE:** `gate_ph_pyq_2025.json` (65 Qs), `gate_ph_pyq_2024.json` (35 Qs — to be expanded to 65 Qs next), and `gate_ph_sub_01.json` (30 Qs -> place in `topic_tests/01_mathematical_physics/sub_01_linear_algebra_vector_calc.json`).
   - **DELETE CLONES:** Delete the 10 cloned legacy PYQs (`gate_ph_pyq_01..10`), the 12 cloned mocks (`gate_ph_mock_01..12`), and the 18 cloned legacy subtopics (`sub_cm_01..02`, `sub_emt_01..02`, etc.) that repeated the same 65-question synthetic pool.
2. **`gate_cs`, `gate_cy`, `gate_ma` & `jam_ph`, `jam_cy`, `jam_ma`:**
   - **KEEP & MIGRATE:** Migrate `gate_cs_pyq_2024.json` (65 Qs), `gate_cy_pyq_2024.json` (40 Qs), `gate_ma_pyq_2024.json` (30 Qs), `jam_ph_pyq_2024.json` (30 Qs), `jam_cy_pyq_2024.json` (30 Qs), and `jam_ma_pyq_2024.json` (30 Qs) into their respective `en/pyq/` and `hi/pyq/` folders.
3. **`upsc_cse`:**
   - **KEEP & MIGRATE:** Migrate `upsc_cse_geo_pyq_ias_special_1.json` and `upsc_cse_geo_pyq_ias_special_2.json` into `exams/upsc/upsc_cse/{en,hi}/pyq/`, and migrate the 15 topic papers (`upsc_geo_ind_01..09` and `upsc_geo_world_01..06`) into their own dedicated topic folders under `exams/upsc/upsc_cse/{en,hi}/topic_tests/<topic_slug>/`.
4. **`uppcs_pre`, `tgt_pgt_econ_geo`, `ssc_gd`:**
   - **KEEP & MIGRATE:** Keep `uppcs_pre_pyq_2023_gs1.json`, `uppcs_pre_geo_pyq_special.json`, `tgt_pgt_econ_geo_models_mock_1.json`, `tgt_pgt_econ_geo_pyq_compendium.json`, and **only 1 copy** of the unique pool (`ssc_gd_pyq_2024_s1.json` / `ssc_gd_pyq_01.json`, `tgt_pgt_geo_pyq_01.json`, `uppcs_pre_pyq_2020.json`).
   - **DELETE CLONES:** Delete `ssc_gd_pyq_02..10` and `ssc_gd_mock_01..10` (which cloned `ssc_gd_pyq_01`), delete `tgt_pgt_geo_pyq_02..10`, `mock_01..10`, and `sub_*` (which cloned `tgt_pgt_geo_pyq_01`), and delete `uppcs_pre_pyq_2021..2024`, `mock_01..05`, `uppcs_csat_pyq_2023` (clone of 2022), and cloned `sub_*` files.

### Rule 3: Schema for Language-Specific JSON Files (`en/` vs `hi/`)
When splitting a paper into `en/<type>/<testId>.json` and `hi/<type>/<testId>.json`:
- **In `en/.../<testId>.json`:**
  - Include `"language": "en"` at the root.
  - Each question contains `"questionId"`, `"questionNumber"`, `"sectionId"`, `"sectionTitle"`, `"questionType"`, `"positiveMarks"`, `"negativeMarks"`, `"pyqTag"`, `"topicTag"`, `"difficulty"`, `"questionText"` (from `questionTextEn`), `"options"` (from `optionsEn`), `"correctOption"`, `"correctOptionsList"`, `"natMin"`, `"natMax"`, `"explanation"` (from `explanationEn`), AND retains `"questionTextEn"`, `"optionsEn"`, `"explanationEn"` for backward compatibility with older app builds.
- **In `hi/.../<testId>.json`:**
  - Include `"language": "hi"` at the root.
  - Each question has the **exact same `"questionId"` and `"questionNumber"`** so the app can toggle `EN ⇄ हिं` mid-test by matching `questionNumber` / `questionId`, with `"questionText"` (from `questionTextHi`), `"options"` (from `optionsHi`), and `"explanation"` (from `explanationHi`), plus `"questionTextHi"`, `"optionsHi"`, `"explanationHi"`.

### Rule 4: Create Topic Scaffolds for `topic_tests/`, `short_notes/`, and `videos/`
For every exam, create an `exam_config.json` and initialize empty topic folders under `en/topic_tests/`, `hi/topic_tests/`, `en/short_notes/`, `hi/short_notes/`, `en/videos/`, and `hi/videos/` with a starter `index.json` schema:
- **Short Notes Schema (`short_notes/<topic_slug>/notes_01.json`):**
  ```json
  {
    "noteId": "gate_ph_mp_notes_01",
    "examId": "gate_ph",
    "topicId": "01_mathematical_physics",
    "language": "en",
    "title": "Linear Algebra & Vector Calculus — Quick Revision & Formula Sheet",
    "readTimeMinutes": 10,
    "sections": [
      {
        "heading": "1. Eigenvalues, Trace & Cayley-Hamilton Theorem",
        "markdownContent": "...",
        "keyFormulas": ["Tr(A) = Σ λ_i", "det(A) = Π λ_i"]
      }
    ]
  }
  ```
- **Video Playlist Schema (`videos/<topic_slug>/videos_01.json`):**
  ```json
  {
    "playlistId": "gate_ph_mp_videos_01",
    "examId": "gate_ph",
    "topicId": "01_mathematical_physics",
    "language": "en",
    "title": "Mathematical Physics — Concept & PYQ Video Lectures",
    "videos": []
  }
  ```

### Rule 5: Update `manifest.json` & Delete All Temporary Migration Scripts
1. Update `manifest.json` so every test entry includes both:
   - `"pathEn": "exams/<family>/<examId>/en/<type>/<file>.json"` and `"cdnUrlEn": "https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/..."`
   - `"pathHi": "exams/<family>/<examId>/hi/<type>/<file>.json"` and `"cdnUrlHi": "https://cdn.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/..."`
   - `"path"` and `"cdnUrl"` pointing to the default (`en/`) path for backward compatibility.
   - Plus `"shortNotesIndexUrl"` and `"videosIndexUrl"` on each category/topic.
2. Delete the old flat folders (except `tests/geography_pyq_1993_2026/`) once migrated.
3. **MANDATORY CLEANUP:** Delete (`rm -f`) any temporary `.py` migration script you created before finishing so `git status` shows only the clean `exams/`, `tests/geography_pyq_1993_2026/`, and `manifest.json` files.
```
