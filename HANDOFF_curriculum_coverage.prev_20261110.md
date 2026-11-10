# Handoff — Curriculum coverage, graph expansion & Claude learning packs
Updated: 2026-11-10 09:45 IST · Machine: Suhas's MacBook Air · All work runs on the Mac (stdlib Python, no pip).

## Standing rules (still in force)
- Ask Suhas before deleting ANY file (incl. temp). Ask before any git commit — nothing committed so far.
- Never invent topics, sources, course codes, assignments or capstones. Public legal sources only. No OCR.
- Originals in `~/sde/nptel/` (`unified_cloud_curriculum.md`, `index_cloud.md`, `learner_record.md`) are untouched — keep them so.
- Do not restore `unified_cloud_curriculum_index.md`.
- Level tags: HS, UG, UG+PG, PG-only, industry, level-unknown (from graph `topic_levels*.tsv`); never guess a level.

## Decisions made (2026-11-10)
1. Main graph expanded with System Design Primer (donnemartin README) + CBSE high-school bridge (cbseacademic.nic.in 2026-27 Maths/Physics/CS). Copy → expand → verify → swap; old main graph deleted, `backup_pre_recovery/` kept.
   - `~/sde/ocw-courses/uglists/graph/`: 37,503 nodes / 487,223 edges (+131 nodes, +515 edges; provenance expand:sdp / expand:hs). Evidence: `recovery/graph_expansion_20261110/`.
2. Three builds produced and compared: staged enhance, hybrid rebuild, full rebuild (full = ALL 36,628 graph topics, per Suhas).
3. Claude cowork format = 2 files per build: `topics.md` + `meta_rules_and_index.md` (meta rules make Claude teach to level, follow prereq order, generate content where none exists).
4. Recommendation given: hybrid as primary pack, full as reference.
5. Full build re-sorted domain → level (HS→UG→UG+PG→PG-only→industry→unknown) → DAG. Level switches 19,646 → 63; trade-off: ~49k prereq reversals across blocks, all listed in the audit for just-in-time bridging (0 reversals within a domain/level band).
6. Literal assignment/capstone pointers REMOVED from the index; replaced by §10 "Assignment doctrine" (NPTEL/university-style, generated on the go), modelled on analysis of the 433 existing assignments (5 Qs, 10 marks: 1/2/2/2/3, pass 7/10 + proof & build accepted) and 18 capstones. Explicitly not official NPTEL policy.
7. Compact versions created (all topics, levels, order and the full prereq audit retained; per-line evidence tags and T/A pointers dropped — still available in the non-compact files).
8. Full graph copy embedded in the full build (`full/graph/`, ~230 MB) per Suhas.

## Where things are
`~/sde/nptel/builds/`
- `staged/` — topics.md (2.0 MB), meta_rules_and_index.md
- `hybrid/` — topics.md (2.0 MB), meta_rules_and_index.md  ← recommended primary
- `full/`
  - `topics_sorted_compact.md` (801 KB) + `meta_rules_and_index_sorted_compact.md` (523 KB)  ← recommended for upload
  - `topics_sorted.md` (5.2 MB) + `meta_rules_and_index_sorted.md` (4.6 MB) — non-compact, with evidence tags
  - `meta_rules_and_index_sorted.with_pointers.bak.md` — backup before pointer removal
  - `topics.md` + `meta_rules_and_index.md` — original DAG-ordered full pack
  - `graph/` — unified_graph.json (197 MB), dag_view.json, topological_node_order.json, topic_levels_expanded.tsv
  - `sort_verification.json`, `assignment_doctrine_analysis_20261110.json`

`~/sde/ocw-courses/recovery/curriculum/`
- `assignments/assignments.md` (+ .json) — all 433 existing assignments + keys, verbatim, by unit (2,380 topics)
- `assignments/capstones.md` — 18 verbatim capstones (17 D13 + 1 D21 remedial)
- `out/` (staged build sources, teaching_assignments_map), `rebuild_hybrid/`, `rebuild_full/` (sources, manifests)
- `COMPARISON.md`, `claude_pack_COMPARISON.md`, `FINAL_VERIFICATION.json`, `EXPANSION_RUN_REPORT.md`
- Scripts: `propose.py`, `insert.py`, `sort_full_domain_level_20261110.py`

## Cleanup done
Deleted (approved): `recovery/recov.tgz`, 6 `__pycache__` dirs, `uglists/prev/ucc/._index_cloud.md` (~11.6 MB). Old handoff replaced by this file.

## Open items / next steps
- Git: nothing committed. `nptel/builds/full/graph/` (~230 MB) is NOT gitignored — exclude it before any commit (ask Suhas).
- CS2023 fold-in blocked (0/60 inserted: 54 lacked level data, 5 unsafe aliases, 1 already covered).
- ~17,210 full-build topics remain level-unknown (provenance gap, not guessed).
- Possibly clean old drafts in recovery/ — only with Suhas's approval.
- Upload to Claude cowork: hybrid pack, or full compact pair, plus `nptel/learner_record.md`.
