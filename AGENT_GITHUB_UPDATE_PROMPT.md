# Local Coding Agent Handoff — Update `prepunfold-cdn` on GitHub (`Geography PYQ 1993–2026`)

Copy and paste the prompt block below directly into your local coding agent (**Cursor**, **Windsurf**, **VS Code GitHub Copilot Agent**, **Claude Code**, or **Android Studio Gemini Agent**) after downloading `prepunfold_cdn_geography_1993_2026_complete.zip`.

---

## Copy-Paste Prompt for Your Local Agent

```markdown
You are updating the PrepUnfold CDN repository (`https://github.com/Deepak-4551819/prepunfold-cdn`) for the PrepUnfold Android app (`com.justunfold.prepunfold`).

### 1. Context & Credentials
- **GitHub Repository**: `https://github.com/Deepak-4551819/prepunfold-cdn`
- **Branch**: `main`
- **GitHub Fine-Grained PAT**: `YOUR_GITHUB_PAT`
- **Source Bundle**: `prepunfold_cdn_geography_1993_2026_complete.zip`

### 2. What Has Been Added in This Release (`v2026.11.13.2`)
1. **New Exam Section — `geography_pyq_1993_2026`**:
   - **Title (EN)**: `Geography PYQ (1993-2026) — All State PSC / UPSC`
   - **Title (HI)**: `भूगोल विगत वर्ष प्रश्न (1993-2026) — सभी राज्य पीएससी / यूपीएससी (Topic & Sub-Topic Wise)`
   - **Total Questions**: `3,495` real PYQs (1993–2026) across **83 Topic-Wise Mock Tests** and **167 Sub-Topics**:
     - **Part I: Indian Geography (`part1_indian_geography`)**: Topics 1–31 (`geo_pyq_ind_t01_general_introduction.json` to `geo_pyq_ind_t31_miscellaneous.json`) • 89 Sub-Topics • 2,099 PYQs.
     - **Part II: World Geography (`part2_world_geography`)**: Topics 1–52 (`geo_pyq_wld_t01_the_universe.json` to `geo_pyq_wld_t52_miscellaneous.json`) • 78 Sub-Topics • 1,396 PYQs.
2. **Sub-Topic Hierarchy & Short Clear Explanations**:
   - Every topic test file (`tests/geography_pyq_1993_2026/<testId>.json`) contains a top-level `subtopics` array listing every sub-topic (`subtopicId`, `subtopicTitleEn`, `subtopicTitleHi`, `questionCount`) and tags every question with `sectionId`, `sectionTitleEn`, `subtopicId`, `subtopicTitleEn`, `pyqTag` (exact exam & year, e.g. `U.P.P.C.S. (Pre) 2022`, `I.A.S. (Pre) 2010`), and a concise 1–3 sentence bilingual explanation (`explanationEn` & `explanationHi`).
3. **Complete Multi-Exam Catalog (`12 Categories • 112 Tests • 4,915 Questions`)**:
   - `geography_pyq_1993_2026` (83 Topic-Wise Mock Tests, 3,495 Qs)
   - `upsc_cse` (4 Tests, 300 Qs)
   - `uppcs_pre` (3 Tests, 230 Qs)
   - `tgt_pgt_econ_geo` (3 Tests, 150 Qs)
   - `ssc_gd` (3 Tests, 240 Qs)
   - `gate_cy`, `gate_ma`, `gate_ph`, `gate_cs` (8 Tests, 290 Qs)
   - `jam_ma`, `jam_cy`, `jam_ph` (8 Tests, 210 Qs)

### 3. Exact Commands to Execute Locally
Run the following commands in the terminal where `prepunfold_cdn_geography_1993_2026_complete.zip` is located:

```bash
# Option A: One-command Python API Atomic Upload (No git clone required)
unzip -q -o prepunfold_cdn_geography_1993_2026_complete.zip -d ./prepunfold_cdn_bundle
cd ./prepunfold_cdn_bundle
export GITHUB_TOKEN="YOUR_GITHUB_PAT"
python3 push_to_github.py
```

Or using standard `git` CLI:

```bash
# Option B: Standard Git Clone, Copy, Commit & Push
git clone https://x-access-token:YOUR_GITHUB_PAT@github.com/Deepak-4551819/prepunfold-cdn.git
unzip -q -o prepunfold_cdn_geography_1993_2026_complete.zip -d ./prepunfold-cdn
cd ./prepunfold-cdn
git add manifest.json README.md AGENT_GITHUB_UPDATE_PROMPT.md push_to_github.py scripts/ tests/
git commit -m "feat(cdn): add Geography PYQ (1993-2026) exam section (83 Topic-Wise Mock Tests, 167 Sub-Topics, 3,495 PYQs with explanations)"
git push origin main
curl -s "https://purge.jsdelivr.net/gh/Deepak-4551819/prepunfold-cdn@main/manifest.json"
```
```

---

## Topic & Sub-Topic Directory Overview (`geography_pyq_1993_2026`)

| Part | Topics Covered | Sub-Topics | Total PYQs | Test ID Range |
| :--- | :--- | :---: | :---: | :--- |
| **Part I: Indian Geography** | Topics 1–31 (`1. General Introduction` to `31. Miscellaneous`) | 89 Sub-Topics | 2,099 | `geo_pyq_ind_t01_general_introduction` – `geo_pyq_ind_t31_miscellaneous` |
| **Part II: World Geography** | Topics 1–52 (`1. The Universe` to `52. Miscellaneous`) | 78 Sub-Topics | 1,396 | `geo_pyq_wld_t01_the_universe` – `geo_pyq_wld_t52_miscellaneous` |
| **Total (`geography_pyq_1993_2026`)** | **83 Main Topics** | **167 Sub-Topics** | **3,495 PYQs** | `tests/geography_pyq_1993_2026/*.json` |
