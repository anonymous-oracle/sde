# HANDOFF — Curriculum coverage, graph expansion & Claude learning packs (context spine)
Last updated: 2026-11-10 ~10:15 IST · Owner: Suhas · Machine: Suhas's MacBook Air (all work runs on the Mac; stdlib Python only)

---
## START HERE (read this first in any new chat)
**What this is:** A learning-curriculum project. A unified topic graph built from NPTEL/OCW/university course lists (+ System Design Primer + CBSE high-school bridge) drives curriculum "packs" that Suhas uploads to a Claude cowork project to learn in a structured, prerequisite-ordered way. Claude teaches from a topic list + a meta-rules/index file and generates teaching content and assignments on the go.

**State in 5 lines**
1. Main graph expanded and swapped in: 37,503 nodes / 487,223 edges (`/Users/suhas/sde/ocw-courses/uglists/graph/`).
2. Three builds exist: staged, hybrid, full — in `/Users/suhas/sde/nptel/builds/{staged,hybrid,full}/`.
3. Full build is re-sorted domain → level → DAG, with a compact upload pair (1.32 MB) and an Assignment Doctrine (§10) in its meta file.
4. All 433 existing assignments and 18 capstones extracted verbatim into `/Users/suhas/sde/ocw-courses/recovery/curriculum/assignments/`.
5. Nothing committed to git. Originals in `/Users/suhas/sde/nptel/` untouched.

**Canonical files (upload candidates)**
- Recommended full upload: `/Users/suhas/sde/nptel/builds/full/topics_sorted_compact.md` + `/Users/suhas/sde/nptel/builds/full/meta_rules_and_index_sorted_compact.md` (+ `/Users/suhas/sde/nptel/learner_record.md`).
- Alternative (preserves written teaching text pointers): `/Users/suhas/sde/nptel/builds/hybrid/topics.md` + `meta_rules_and_index.md` (+ original curriculum for pointers to resolve).

**First commands to re-verify (read-only)**
```
ls -la ~/sde/nptel ~/sde/nptel/builds/*
du -sh ~/sde/nptel/builds/*
git -C ~/sde status --short
python3 -c "import json;print(json.load(open('/Users/suhas/sde/nptel/builds/full/sort_verification.json')).keys())"
grep -c '' ~/sde/nptel/builds/full/topics_sorted_compact.md
grep -n '^## 10' ~/sde/nptel/builds/full/meta_rules_and_index_sorted_compact.md
```

---
## 1. Purpose, starting brief & evidence boundaries
- The task started from the original `~/sde/HANDOFF_curriculum_coverage.md` (deleted 2026-11-10 at Suhas's request; **not recoverable** — never in git). From the conversation and run reports, it asked:
  - **Part 1:** raise topic coverage of `~/sde/nptel/unified_cloud_curriculum.md` and `~/sde/nptel/index_cloud.md` from the main topic graph via additive gap-fill insertions (insertions-only diff), tagging topics UG / UG+PG / PG-only from `topic_levels.tsv`.
  - **Part 2:** clean up `~/sde/ocw-courses` (propose; delete only with approval).
- The original rules are carried forward in §7.
- Evidence boundary: exact early wording/timestamps of the first requests and the deleted handoff's transfer-archive checksum note are not recoverable. Everything else below is verified against files on the Mac.

## 2. Request & decision log (with rationale) — do not reverse without asking Suhas
1. **Execute the handoff on the Mac, not the assistant's computer.** All scripts and outputs live on the Mac.
2. **Gap-fill proposals:**
   - The first run proposed 1,847 noisy topics. Filters were tightened (allowlist plus a level-lookup fix), bringing it to 304 proposals. The staged output is in `recovery/curriculum/out/`.
   - The CS2023 fold-in is blocked: 0/60 inserted (54 had no usable level evidence, 5 unsafe aliases, 1 already covered).
3. **Graph lacked System Design Primer (donnemartin) + high-school bridge.**
   - Decision: copy the main graph, expand it, verify it's intact, swap it in, and delete the old one.
   - Done: +131 nodes, +515 edges, with provenance `expand:sdp` / `expand:hs`.
   - Sources: the SDP GitHub README; cbseacademic.nic.in curriculum 2026-27 (Maths, Physics, Computer Science).
   - `backup_pre_recovery/` kept. Evidence in `recovery/graph_expansion_20261110/`.
4. **Enhance vs rebuild.** Suhas needs an index plus a curriculum file for Claude cowork. Decision: build a hybrid and a full rebuild separately, compare them, and recommend.
   - Hybrid: 480 units; keeps all 450 original unit bodies, 433 assignments and 435 details blocks verbatim.
   - Full: initially 2,816 topics (strict filter). Suhas: "All graph topics are needed", so it was rebuilt with all 36,628 topics (14,022 main units plus 24 noise-appendix units holding 43 noise topics).
5. **Cleanup approved and done** (~11.6 MB):
   - Deleted `recovery/recov.tgz`, 6 `__pycache__` dirs and `uglists/prev/ucc/._index_cloud.md`.
   - Audit: `cleanup_audit.log`, `cleanup_approved_result.json`.
6. **Teaching and assignments map** built for each build: `teaching_assignments_map.md/.json`.
7. **Claude pack format.** Topic lists suffice for Claude, so each pack has two files, `topics.md` and `meta_rules_and_index.md`.
   - The meta rules cover: teach to the level tag, follow prerequisite order, use existing content via pointers, otherwise generate (definitions, results with proof tags, a build, and a 5-question check with a hidden key).
   - Made for all 3 builds and compared (`claude_pack_COMPARISON.md`).
8. **Recommendation given:** Hybrid for preserved written teaching. Full for the complete inventory and on-demand authoring; it is not completed teaching.
9. **"Make the full rebuild smaller / an index"** was started, then **stopped** by Suhas. The `claude_pack_compact/` folder doesn't exist.
10. **Extract existing assignments to a separate file:** 433 verbatim, with answer keys.
11. **Move packs into `~/sde/nptel`, each build in its own folder.**
    - Final location: `~/sde/nptel/builds/{staged,hybrid,full}/`. (A detour moving them to `~/sde/` was a misread and has been corrected.)
12. **Record the entire graph in the full build.** A ~231 MB copy went into `full/graph/`. Suhas: "stick with this."
13. **Level order was not maintained** (19,646 level switches). Decision: re-sort the full build by domain → level (HS → UG → UG+PG → PG-only → industry → level-unknown) → DAG.
    - Level switches dropped to 63.
    - Units were split into 24,828 contiguous `.pN` segments.
    - Domain order was derived by exactly minimising backward cross-domain prerequisite counts, with HS fixed first.
14. **Assignment and capstone pointers** were first added to the sorted index, then **reverted** at Suhas's request.
    - They were replaced by **§10 Assignment Doctrine**, which generates NPTEL- and university-style assignments and capstones on the go.
    - The doctrine is modelled on an analysis of the 433 assignments and 18 capstones. It is explicitly not official NPTEL policy.
    - A backup with the pointers is kept.
15. **Prune size while keeping all topics:** compact pair created (1,324,483 bytes, down from 9,803,953 bytes for the detailed sorted pair).
16. **Old handoff deleted; this context-spine handoff written.**

## 3. Requirements checklist
| Requirement | Status | Evidence |
|---|---|---|
| Work on Mac only | Met | all outputs under /Users/suhas |
| Additive-only curriculum changes, originals untouched | Met | hash checks; `~/sde/nptel/*.md` unchanged |
| Never invent topics/sources/codes/assignments | Met | graph-node-only topics; verbatim extraction; doctrine marked "modelled" |
| SDP + HS in main graph, verify before swap, delete old | Met | `recovery/graph_expansion_20261110/` |
| Hybrid vs full comparison + recommendation | Met | `recovery/curriculum/COMPARISON.md` |
| Cleanup | Met (approved items only) | `cleanup_approved_result.json` |
| Teaching/assignment map per build | Met | `teaching_assignments_map.*` |
| 2-file Claude pack ×3 + comparison | Met | `nptel/builds/*`, `claude_pack_COMPARISON.md` |
| Full build = all graph topics | Met | 36,628 topics |
| Domain → level → DAG order | Met (with trade-off, §5) | `sort_verification.json` |
| Assignments/capstones as doctrine, not literal | Met (sorted full meta files only) | §10 in `*_sorted*.md` |
| Smaller file, all topics kept | Met | compact pair 1.32 MB |
| CS2023 gap-fill | **Not met** (blocked) | `cs2023_review.json` |
| Level tags for every topic | **Partial**: 17,210 level-unknown in full | graph level data |
| Git commit | **Not done** (needs Suhas's yes) | `git status` |
| Install a build into the live curriculum files | **Not requested/not done** | — |

## 4. Methods & semantic contracts
- **Graph:**
  - `unified_graph.json` has node types topic, curriculum_unit, course and external_course.
  - Edge types include covers, ext_prereq, cooccurrence and more.
  - `dag_view.json` is the DAG view.
  - Only `ext_prereq` and DAG edges count as prerequisite claims. Containment, taxonomy, cooccurrence and lecture sequence are not automatically prerequisites.
- **Levels:**
  - Tags come from `topic_levels.tsv` / `topic_levels_expanded.tsv`.
  - Joint UG/PG is written as UG+PG; practitioner topics are tagged industry.
  - Unknown stays unknown and is never guessed.
- **Staged build:** the original curriculum plus filtered additive insertions.
- **Hybrid build:** the unit skeleton is regenerated from the graph, and existing content is carried over verbatim.
- **Full build:** every graph topic in DAG order, with placeholders and no fabricated teaching.
- **Sort:** domain → level band → DAG.
  - Every prerequisite that ends up after its dependent is listed in the audit, so Claude bridges it just in time.
- **Compaction:**
  - Drops per-line provenance (g:, c:, src:, SDP/CBSE line refs), T@/A: pointers, repeated headings and source-edge registry indices.
  - Levels are inherited from headers. Topic IDs are short, and the audit is stored as adjacency lists.
  - It is not lossless archival compression. The detailed files keep the metadata.
- **Assignment doctrine:**
  - Five questions worth 10 marks: single-choice 1, multiple-select 2, numerical 2, proof/derivation 2, build/programming 3.
  - The default pass is 7/10 with the proof and build accepted, but only if the learner profile has no rule of its own.
  - Write and verify the key first, and reveal it only after an attempt.
  - Distractors target misconceptions, and correct-answer positions vary. The originals show bias: single-choice A/B/C/D = 158/224/46/5, and multiple-select ABC = 330.
  - Capstones come after domain exit. Each has fixed criteria, tests, predict-then-measure, an injected failure, a threat model, cost, teardown and an oral defence. There is also a remedial variant.
  - Results are logged in `learner_record.md`.

## 5. Verification results
- **Graph:** all 12 installed graph payload hashes are OK, and the 4 copied graph files match the originals.
- **Compact full topics:** all 36,628 names, levels and their order are identical to `topics_sorted.md`, and the detailed graph IDs are unique.
- **Assignments:** all 433 assignments and keys match the staged and original curriculum byte for byte (spot checks: A1.1, A26.1, A14.22).
- **Capstones:** all 18 match their source ranges and hashes.
- **Sorted-order trade-off:**
  - 49,159 reversed typed relations (these are relations, not topics): 49,056 DAG and 761 explicit ext_prereq. The two sets overlap, so don't add them.
  - By cause: domain grouping 31,863, level grouping 17,258, same-band non-DAG 38.
  - Within a band there are **0 DAG reversals**, but **38 explicit non-DAG exceptions**.
  - Before the sort: 318 DAG and 157 ext_prereq reversals.
  - 1,526 DAG edges and 61 explicit edges have non-topic endpoints, so they can't be placed in a topic-only list (disclosed).
- **Pack comparison** (before the sort):

  | Pack | Topics | SDP / HS coverage | Prereq violations | Size |
  |---|---:|---:|---:|---:|
  | Staged | 14,574 | 46% / 23% | 456 | 2.05 MB |
  | Hybrid | 14,704 | 100% / 100% | 461 | 2.07 MB |
  | Full | 36,628 | — | 0 (main DAG) | 4.7 MB |

  Teaching and assignment pointer coverage: staged and hybrid 66% / 15%, full 26% / 6%.
- **HS and SDP in the full sorted build:** the HS-source domain has 101 distinct topics (79 tagged HS level), and the SDP domain has 95.
- **Assignment metadata discrepancy:** status records show 423 direct plus 10 context-only, while the header count says 425 direct (two context-only records have topic lists). The sources were not altered.

## 6. File map (absolute paths)
`/Users/suhas/sde/nptel/` — originals (DO NOT MODIFY): `unified_cloud_curriculum.md` (2.13 MB), `index_cloud.md`, `learner_record.md`
`/Users/suhas/sde/nptel/builds/`
- `staged/` — `topics.md` (2.0 MB), `meta_rules_and_index.md` (53 KB)
- `hybrid/` — `topics.md` (2.0 MB), `meta_rules_and_index.md` (54 KB)
- `full/` (251,373,448 bytes total)
  - `topics_sorted_compact.md` (801 KB) + `meta_rules_and_index_sorted_compact.md` (523 KB): **upload pair**
  - `topics_sorted.md` (5.2 MB) + `meta_rules_and_index_sorted.md` (4.6 MB): detailed, with metadata and §10
  - `meta_rules_and_index_sorted.with_pointers.bak.md`: backup taken before the pointer revert
  - `topics.md` (3.9 MB) + `meta_rules_and_index.md` (765 KB): original DAG-ordered full pack (no §10)
  - `graph/` (230,848,757 bytes): `unified_graph.json`, `dag_view.json`, `topological_node_order.json`, `topic_levels_expanded.tsv`
  - `sort_verification.json`, `assignment_doctrine_analysis_20261110.json`

`/Users/suhas/sde/ocw-courses/recovery/curriculum/`
- `assignments/`:
  - `assignments.md` (1.2 MB) and `.json`: 433 verbatim assignments
  - `capstones.md` (44 KB): 18 verbatim capstones (17 from D13, 1 remedial from D21)
- `out/`: staged sources, `teaching_assignments_map.*`, `RUN_REPORT.md`, `FILTER_NOTES.md`, `cleanup_proposal.md`, `cs2023_review.json`
- `rebuild_hybrid/` (includes `unit_manifest.json`) and `rebuild_full/` (includes `full_scope.json`): build sources
- Reports: `COMPARISON.md`, `claude_pack_COMPARISON.md`, `FINAL_VERIFICATION.json`, `EXPANSION_RUN_REPORT.md`, `*_CHECKS.json`, `filter_audit.json`
- Scripts: `propose.py`, `insert.py`, `inspect_graph.py`, `cleanup_audit.py`, `sort_full_domain_level_20261110.py`

`/Users/suhas/sde/ocw-courses/uglists/graph/`: main graph (1.3 GB folder) and `backup_pre_recovery/`
`/Users/suhas/sde/ocw-courses/recovery/graph_expansion_20261110/`: expansion evidence

## 7. Standing rules & preferences
- Ask Suhas before deleting ANY file on the Mac, even temporary ones. Ask before any git commit.
- Work on the Mac, not the assistant's computer. Use stdlib Python only: no pip, no OCR. Use public, legal sources only.
- Never invent topics, sources, course codes, levels, assignments or capstones.
- Curriculum changes are additive only. Never modify the originals in `~/sde/nptel/`.
- Do not restore `unified_cloud_curriculum_index.md`.
- Each build stays in its own folder under `~/sde/nptel/builds/`.
- Write new versions as new files rather than overwriting, and back up before replacing anything.

## 8. Known issues & open work
- **Git:**
  - Nothing is committed. `git status` shows `nptel/builds/`, `nptel/unified_cloud_curriculum.md` and `ocw-courses/` as untracked.
  - `nptel/builds/full/graph/` (~231 MB) is **not gitignored**. Exclude it before any commit.
- **CS2023:** blocked, 0 of 60 inserted.
- **Levels:** 17,210 level-unknown topics in the full build.
- **Doctrine scope:** §10 exists only in the two sorted full meta files, not in staged, hybrid or the original full pack.
- **Stale scripts:**
  - `sort_full_domain_level_20261110.py` targets the old `/Users/suhas/sde/nptel/full/`.
  - The pack generator recreates the historical `claude_pack/` folders.
  - `final_verify.py` expects the historical pack locations.
  - No standalone script exists for assignment extraction, compaction or doctrine insertion.
- **Leftovers:** possible old drafts in `recovery/`. Clean them only with approval.

## 9. Safe resumption & reproduction
1. Run the Start Here checks.
2. Read `sort_verification.json` and `FINAL_VERIFICATION.json`.
3. Before rerunning any script:
   - update its paths to `/Users/suhas/sde/nptel/builds/...`;
   - redirect its output to a new dated folder;
   - never write into `~/sde/nptel/*.md`.
4. Verify after any change: topic count is 36,628, the name/level/order equality check passes, and the originals' hashes are unchanged.

## 10. Enhancement backlog (proposals — not done; confirm with Suhas)
- **Resolve level-unknown topics** using real syllabus or course evidence. This needs sources. The risk is guessed levels.
- **Unblock CS2023:** find level evidence and safe alias mappings for the 54 + 5 topics.
- **Reduce cross-block reversals:** for example, a "bridge-first" variant that pulls needed prerequisites into earlier bands. The trade-off is more level switching.
- **Per-domain pack split,** so Claude gets smaller uploads one domain at a time.
- **Add §10 to the hybrid and staged meta files** for consistency.
- **Git hygiene:** add `nptel/builds/full/graph/` to `.gitignore`, then commit (with Suhas's yes).
- **Consolidated script:** one reproducible end-to-end script covering extraction, sort, compaction and doctrine.
- **Learner progress tracking** in `learner_record.md` (mastery per domain and level band).

## 11. Claude cowork upload guidance
- **Option A (complete scope):** upload `full/topics_sorted_compact.md`, `full/meta_rules_and_index_sorted_compact.md` and `nptel/learner_record.md`. Claude generates teaching and assignments using §10.
- **Option B (preserved teaching text):**
  - Upload `hybrid/topics.md`, `hybrid/meta_rules_and_index.md`, `nptel/unified_cloud_curriculum.md` (so the T/A pointers resolve) and `learner_record.md`.
  - Optionally add `assignments/assignments.md`.
- Don't upload `full/graph/` (too large). The packs contain pointers and rules, not teaching text.
