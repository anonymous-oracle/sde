# HANDOFF — Curriculum coverage, graph expansion & Claude learning packs (context spine)
Last updated: 2026-11-10 ~11:25 IST (see §12 for 10:15–11:25 changes) · Owner: Suhas · Machine: Suhas's MacBook Air (all work runs on the Mac; stdlib Python only)

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
- **Current self-contained pair (supersedes the two bullets below; see §12):** `/Users/suhas/sde/nptel/builds/full/selfcontained/topics_compact.md` + `meta_rules_compact.md` (+ `Master_Rules.md`, `learn-SKILL.md`). 36,640 topics.
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

---
## 12. Update 2026-11-10 10:15–11:05 IST — self-contained compact Claude pack (supersedes §11 upload guidance)
**Suhas's rules added this session (standing):**
- Pack files must be self-contained. Topics files reference NO other file. Meta-rules files may reference ONLY `Master_Rules.md` and `learn-SKILL.md` (plus their sibling topics file).
- The compact meta-rules file must capture the overall teaching method for ALL topics, and describe how the course is structured as a domain → level map only — no per-unit index, audit lists, noise IDs or other tags. Topics file: no tags (no short IDs).
- Assessment cadence (meta §11): weekly assignments (§10 five-question format); one meaningful coding capstone per **collection of related units** (not per tiny unit; Claude forms collections from consecutive related topics in a domain/level band and announces scope first); plus from-scratch implementation exercises during teaching (no libraries, toy size, then compare with a real tool).
- Level-unknown (?) topics are taught at graduate depth (UG core + graduate extension, like UG+PG) unless the learner says otherwise; the tag stays unknown. A level is a floor, not a ceiling.
- Lean pack: Claude authors all lessons/checks/assignments/capstones fresh (labelled tutor-generated); no embedded original teaching text or assignments (Suhas rejected the 2.18 MB version with embedded text).

**Done:**
- Built self-contained versions of all three full-build pairs (`*_sc.md`, with 960 teaching blocks + 415 assignments embedded verbatim as an in-file appendix). Then built the lean compact pair. At Suhas's request **everything in `selfcontained/` except the lean pair was deleted** (the `_sc` files, scripts, logs, verification JSONs, `__pycache__`).
- `/Users/suhas/sde/nptel/builds/full/selfcontained/` now holds:
  - `topics_sorted_compact_lean.md` (801,037 B, ~165k tokens): original compact list, 36,628 topic lines byte-identical, header rewritten to name no file. Still has base-36 short IDs.
  - `meta_rules_and_index_sorted_compact_lean.md` (525,252 B, ~158k tokens): rules 1–8, §10, §11, level-unknown rule; rules 3/6/§10 rewritten to "author fresh". Still contains the full unit index, reversed-edge audit and noise IDs (the bulk of its size).
- Token estimate for lean pair + Master_Rules.md (~15k) + learn-SKILL.md (~3k): ~340k total (estimate, not tokenizer-exact).
- Confirmed all full-build topics files (and the lean one) contain 101 HS-bridge topics and 95 SDP topics; hybrid has both fully; staged only partial (~46% SDP / 23% HS).
- `/Users/suhas/nptel-ocw.zip` (3.7 GB unpacked, a backup of ~/sde) was only listed, not used, copied or deleted. The iCloud copy was unreadable (macOS privacy block). An empty folder `ocw-courses/recovery/zipcopy/` was created and left in place.
- Originals in `builds/full/` and `~/sde/nptel/*.md` unchanged. Nothing committed.

**In progress at time of writing (new files, written alongside; existing two lean files not modified):**
- `selfcontained/meta_rules_compact.md`: rules 1–8, 10, 11 only (references to unit index/IDs/audit/noise/graph removed; rule 2 → follow domain → level → topic order, check prerequisites and bridge just in time), plus a "Course structure: domain → level map" table (domain order, per-level topic counts, totals). Target: a few thousand tokens.
- `selfcontained/topics_compact.md`: same domain/level headings and order, plain topic names only, no short IDs.
- Builder scripts/logs go to /tmp or `ocw-courses/recovery/curriculum/`, not `selfcontained/`.

**Next steps:**
1. Verify the two new files (36,628 topics; counts match; only allowed filenames; no tags).
2. Show Suhas; on his yes, delete the two older lean files so `selfcontained/` holds only `topics_compact.md` + `meta_rules_compact.md`.
3. Upload set for Claude cowork: `topics_compact.md`, `meta_rules_compact.md`, `Master_Rules.md`, `learn-SKILL.md` (+ progress record if any).

**Update ~11:09 IST:** both new files built and verified. `topics_compact.md` 655,741 B (~164k tokens; 36,628 plain names, no IDs). `meta_rules_compact.md` 16,235 B (~4k tokens; rules 1-8, 10, 11 + domain → level count table; level totals H 79, U 6,046, J 4,785, P 8,429, I 79, ? 17,210). Old lean pair still present, awaiting Suhas's yes to delete. Builder/log in /tmp.

**Update ~11:25 IST — old lean pair deleted; IIT GenAI gap-fill (supersedes the "Next steps" list above):**
- Suhas said yes: `topics_sorted_compact_lean.md` and `meta_rules_and_index_sorted_compact_lean.md` are deleted. `selfcontained/` now holds only `topics_compact.md` and `meta_rules_compact.md`.
- Noise tags: gone from the new pair (no IDs, no `noise:true` flag, no audit lists). They remain in the older full-build files (`topics*.md`, `meta_rules_and_index*.md`), which were not modified. The 43 former noise topics are still listed in `topics_compact.md` as ordinary topics with no caution flag; their IDs were stripped, so which lines they are has not been mapped. Open choice for Suhas: keep, drop, or add a one-line caution to the meta file.
- Checked `/Users/suhas/sde/iit-genai.md` (12 chapters, ~500 lines) against `topics_compact.md`, concept-level (~130 terms, not line-by-line). Nearly all present; most already exist as `Curriculum-only` level-`?` topics (this curriculum appears to be ingested already). Not found by name: word2vec, InstructGPT, RLHF, BM25, HNSW, hard negative mining, GPT-1/2/3, T5, METEOR (NLP metric), tool calling, AI winter. PAIR, TechHazardQA and Chain-of-RAG were found.
- **Added those 12 topics** (at Suhas's request) to `topics_compact.md`: `word2vec`, `hard negative mining`, `bm25`, `gpt-1 and gpt-2`, `gpt-3`, `t5`, `instructgpt`, `rlhf`, `hnsw`, `meteor metric`, `tool calling`, `ai winter`.
  - Placement: domain **Curriculum-only**, level **?** (no level evidence, so level not guessed; taught at graduate depth per the level-unknown rule). Each is inserted next to its nearest related existing topic in that band (for example `hnsw` before `efsearch candidate list`, `rlhf` before `aligning model with human preference`), not at a computed DAG position.
  - Naming: `meteor metric` rather than `meteor`, because `meteor` already exists as an unrelated Mathematics topic. The topic names come from the headings and bullets of `iit-genai.md`.
- **New counts:** 36,640 topics (was 36,628). Level-unknown 17,222 (was 17,210). Curriculum-only 8,545 (was 8,533). The header line of `topics_compact.md` and the domain → level table plus totals in `meta_rules_compact.md` were updated; a recount of the topics file matches the table exactly. Diff versus the pre-change files shows only the 12 added lines, the header count and those three meta lines. Other level totals unchanged (H 79, U 6,046, J 4,785, P 8,429, I 79).
- Backups of the pre-change files (and of this handoff): `/private/tmp/claude-501/-Users-suhas-sde/0a62790a-4998-4621-8c44-aa0780fa5101/scratchpad/backup_pre_genai/` (session scratchpad, may not persist). Insert script: `.../scratchpad/add_genai.py`.
- The earlier counts in this handoff (36,628 etc.) still describe the detailed and compact-sorted full builds, which were not changed. `iit-genai.md` itself is untouched and uncommitted.
- Still open: git commit (needs yes; exclude `nptel/builds/full/graph/`), CS2023 gap-fill, level-unknown resolution, §10 doctrine only in the full sorted meta files, and the stale-script list in §8. Upload set for Claude cowork: `topics_compact.md`, `meta_rules_compact.md`, `Master_Rules.md`, `learn-SKILL.md`.
