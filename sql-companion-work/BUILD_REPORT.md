# BUILD_REPORT — sql-databases-companion.md

- **Output:** `/workspace/sde/out/sql-databases-companion.md`
- **Line count:** 3056
- **Major `##` sections (12):**
  - ## 0. Read this first — how this file complements gcp-curriculum.md
  - ## 1. Coverage ledger — every part of "SQL databases + underlying CS + prerequisites", and where it lives
  - ## 2. Stitch table — teach these together
  - ## 3. Lab kit — deterministic Northstar SQL lab
  - ## 4. Concept curriculum
  - ## 5. Skip tests / readiness tiers (12.S12 / 12.S13)
  - ## 6. Query-creation exercise bank (levels 0–14)
  - ## 7. Engine-behaviour labs
  - ## 8. Rosetta & Terraform
  - ## 9. Capstones (C1–C4)
  - ## Appendix K — Instructor keys (AFTER attempt only)
  - ## Appendix V — Verification notes (honesty flags)

## Exercise counts
- Query cards from py (E*/C1*/C2/C4): **92** — by level: {1: 8, 2: 8, 3: 10, 4: 8, 5: 8, 6: 7, 7: 5, 8: 10, 9: 7, 10: 6, 13: 5, 14: 10}
- Level-0 Z0: **8**
- Theory TD: **16**
- Plan PX: **11**
- Transaction TX: **8**
- Bug-hunts BH: **6**
- Dialect DT: **8**
- Schema SD: **6**
- Capstones: C1.1–C1.8 + C2 + C3 + C4 (C1/C2/C4 in py goldens; C3 spec-only)
- Concept modules: PQ 8 · RT 8 · SL 14 · CS 11 · DD 13 · OD 10 · AN 7 = **71**

## Golden wiring
- **All py exercise goldens wired:** YES
- Wrong-path fingerprints referenced: 11

## Stubs / honesty
- C3 (no single fingerprint)
- TF-DB1…TF-DB6 (plan-only, no .tf checked in)
- Z0/TD paper drills (no lab.chk)
- PX/TX expected shapes (behavioural)

## §§0–2
- Preserved from `part_a.md` (stitch table, overlap register, DB pairing, parallel calendar).
