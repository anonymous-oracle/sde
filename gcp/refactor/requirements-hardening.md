# Revamp requirements — hardened (as of the end of R2b, 2026-09-24; D5–D13 added the same day; D14–D16 at R4)

This file pins down how the meta-prompt (`curriculum-refactor-meta-prompt.md`, "the prompt") applies to this repo. It merges the prompt with the learner's decisions, the rulings made at the R2 gate, and the defaults taken during R0–R2. It also records what each later phase has to prove. When it disagrees with the prompt, it wins only where it cites a higher rung of the precedence ladder: a learner decision (rung 1), or a gate ruling the learner approved.

Evidence for R2 is in `audit-R2.md` (a record of the R2 state; `audit_r2.py` no longer runs on `work/`, see `refactor-state.md` §6b). Evidence for R2b is in `audit-R2b.md`; re-run it with `python3 refactor-tools/audit_r2b.py .`.

## 1. Learner decisions (rung 1, verbatim from the 2026-09-24 chat)

| # | Learner's words | Binding reading |
|---|---|---|
| D1 | "gcp-curriculum.md is unrelated to this. But if any .md file provides you helpful material, you are free to use it. For this course, the main curriculum and the 4 curriculum files are the main requirement files." | The course is `Curriculum` (from `gcp.md`) plus the four companions. `gcp-curriculum.md` / `unified-curriculum.md` are source material only: text may be borrowed with a `Source material:` line, but no live text may point back to them. |
| D2 | "You may forget about any progress related refactoring, consider this revamp task as something we are doing fresh." | Nothing counts as done. Every box stays unticked. Chat-only learner state is dropped (C-43, C-67, C-68 evidence; C-69/C-73 evidence). The R10 ledger is a blank §14 template. Ledger §5 **teaching preferences** are course content, not progress, so they are kept. |
| D3 | "Yes, gcp.md is the primary curriculum. But do not remove any curriculum content, you are only allowed to re-arrange, not remove." | Applies to all 7 files. Content may be moved, renamed, annotated or corrected, never deleted. A corrected or regenerated line keeps its pre-refactor text in the file's closing `## Pre-refactor text archive (D3)` section. |
| D4 | "Verify all 18 and retain them." | 18 certifications, each verified on 2026-09-24 (`cert-verification.md`) and kept, with a dated note. "Fifteen" became "eighteen". |
| D5 | "Northstar was a gcp-curriculum.md thing. Not relevant. I hope you did not simply copy @gcp-curriculum.md into this course. That is not required, only use it's content or material if it helps." · "Forget the open question, we are tackling this as if it is a new fresh course." | Track N and `northstar-reference-app.md` are out of scope and are deleted. Every `N…` pointer and every "the reference cloud app" is rebound to the course module that teaches the topic, and missing material is written into that file. Nothing is copied wholesale; material is borrowed only where it fills a gap. The prompt's open cookie question is dropped: the course has no carried-over open items. |
| D6 | "Make the main curriculum file and the 4 companion files self contained but complementing to each other for the sake of the course. No filename references should exist in any of them. Add the material directly instead of referencing." · "1 primary file and 4 companion files, all self contained and no reference links. Ensure that you have all the material added within the files, no file dependencies are tolerated." | Each of the 5 files can be studied with nothing else open. **Zero** file names (`*.md`, `*.py`, `*.sql`, `*.json`, paths) and zero "see file X §y" links in live text. Shared rules (teaching contract, lab safety, session protocol, learner preferences) are written out in each file that needs them. The SQL lab kit is embedded as code blocks, and the golden answers are embedded verbatim, so goldens stay byte-identical. Refactor bookkeeping (provenance lines, the D3 archive, `Source material:` lines) moves out of the course files into `refactor/` records, so D3 still holds and nothing is deleted. |
| D7 | "you free to collect required material from files, just make sure topics do not overlap." | One topic, one home. Every topic is taught in exactly one of the 5 files. Where two files teach the same topic today, the fuller treatment is kept in the owning file and the other file's unique lines are moved into it (D3: moved, never dropped). This replaces the prompt's "owner teaches, others add" overlap register (§7). |
| D8 | "gcp curriculum file is a legacy course, keep that file only until it's useful and then delete it, otherwise that will only confuse you." | `gcp-curriculum.md` (repo root) is source material only. It is deleted in the phase that finishes borrowing from it, once a check shows no course file still needs it. Git history keeps it. **Done in R2b:** the R2b build opens no legacy file (checked with a Python audit hook), and `audit_r2b.py` checks it is absent. **Superseded by D14 (keep the file).** |
| D9 | "expand the nine mappings and any other such missing gaps so that we have a proper, robust self contained curriculum." | The nine checkpoint IDs (C-11) each become a full checkpoint card with a scenario, a prediction step, a check question and an answer key, inside the file that owns the topic. The same applies to every other thin or missing item a gap scan finds (stub sections, pointer-only modules, empty Lab/Check lines). |
| D10 | "the companion files are strictly for the gcp.md course or the Curriculum course. Both have same content. @gcp-curriculum.md is strictly a helper or content reference file. for curriculum material and nothing else. No rule, instruction, should be used from it." | The 4 companions exist only to serve the Curriculum course (`gcp.md` = `Curriculum`). `gcp-curriculum.md` may be consulted for facts and material only. No rule, instruction, structure, numbering, ownership split, milestone or "N" section from it enters the course. A companion line that hands part of a topic to the legacy course ("N4.3 owns the lab; here we add…") is resolved by the companion teaching the whole topic itself. Only the missing piece is written, in the companion's own style. |
| D11 | Asked whether companions may keep the course's module numbers (A5, C3, V-NET…) as tags: "if they help in mapping and stitching the curriculum material as a one single course, keep them." | Course-wide IDs (all unique across the 5 files since the R2 renames) stay as mapping and stitching tags: stitch tables, prerequisite maps, "study with A5", and "recall CR-17" all stay. What must go: file names, links, the backticked file-style name `Curriculum` (it becomes "the main course"), Northstar and every `N…` section, and every **material dependency**. A material dependency is a line that sends the learner outside the 5 files, or to a file that does not actually contain the material ("A10 owns the password lab" when A10 has no such lab). Within the 5 files, each topic has one home (D7). Other files tag it by ID and recall it; they do not re-teach it. |
| D13 | Before R3: "i have added back the gcp-curriculum file. See if you can include anything else from that file and add to the relevant main curriculum file or any of the companion files. This is just a final verification not to unnecessarily add curriculum. After verifying, add a module appropriately in the golang companion to teach me about integrating payment systems, authentication systems (also from the scratch implementations to understand the concepts well), golang implementations from the scratch wherever necessary. When teaching a golang topic, provide one good involved exercise problem that I must solve. It will help cement the concept. Now, after all these checks and changes, see if everything is lining up so far with respect to hardening and ensuring curriculum robustness before moving to R3." | (a) One last read of the restored legacy notes, as material only (D10): add a topic only if no part teaches it, at its one home (D7), in the owner's style; list what was checked and not added (`refactor-state.md` §6d). (b) Two Go modules, GO-28 (authentication) and GO-29 (payment integration), each built from scratch against published test vectors before a vetted library is used; the attacks, cryptography and ledger rules stay with their owners (Cyber AU/CR/PV-03/AB-06/AB-07, SQL DD-03, Primer SD-28). (c) Every GO module ends with one involved problem the learner solves alone, with a rubric shown after submission; rule 0.4.9 gains it as a fourth rule, and it gates `mastered` for GO modules. (d) A robustness review before R3. The legacy file stays until the learner says otherwise (D8 is on hold, not overruled). |
| D12 | Before R3: "add a new rule to teach golang and it's required basic language rules, nuances compared to other languages. Create a new companion course file using nasiko-curriculum.md. Complete this task first and ensure it ties in with the other files." | The course gains a sixth part, **the Go Language Companion** (built as `work/go-language-companion.md` by `refactor-tools/r2c_go.py` from `authored/go-language-companion.md`). It has 27 modules GO-01…GO-27, 54 exercises GO-E*m.n* with keys, 3 capstones and a contrast atlas (Python / Java / C / JavaScript). The new rule is **rule 0.4.9 (Implementation language: Go)** in the main course §0.4, so every part's contract copy carries it. It covers: syntax unlock (rule 0.4.6 applied to code); lab acceptance (`gofmt`, `go vet`, `-race`, no dropped errors, a stop path for every goroutine); version honesty. Python stays the first language of A3 and of Track D. `nasiko-curriculum.md` is **material only**, read the same way D10 reads helper files: its Go nodes set the module list; no rule, phase, spec or ML track is taken from it. Everything else is unchanged: D6 (self-contained), D7 (one home), D11 (IDs as tags) apply to the sixth file as to the others. |

| D14 | Asked whether to delete `gcp-curriculum.md` again or keep it: "keep it" | Supersedes D8's deletion. The file stays as a content reference (D10). The audit row is now "D14 legacy file kept; no build reads it": a full rebuild runs under a Python audit hook and must open the file 0 times. |
| D15 | On the 68 bare "Curriculum" names: "using the bare word is fine, but it should not be a substitute for any curriculum material" | No rename pass. The bare word may name the parent. It may never stand in for material: no "see Curriculum" without a target, and every "Curriculum <module / Part>" pointer must land on a real main-course module or Part, where the material is. `verify.py` gates this. |
| D16 | On R4's tracks M, U and S: "No do not include any of them" · "are you picking these from gcp-curriculum? If yes, skip them. Work with what we already have. I never wanted to copy more bloat from gcp curriculum file." | No track M, U or S, and no new module, §9.2.2 deepening or scope rewrite taken from that scope. The stubs go to `records/`. Every M/U/S anchor is rebound to the module that already teaches the topic. A stub topic that no module teaches gets one line in its natural owner only when the course otherwise lacks it (A2 floating point, A4 sketches, A7 architecture documentation, PCA migration). Everything else goes to `records/` only. `verify.py` gates that no M/U/S token remains. |
### What the decisions change in the prompt

- **§8.2 "All ledger-done items exist and are still marked done"** and **§11 "Ledger-done items still done; the open cookie question preserved"**: D2 makes these vacuous (there are no done items). R3/R10 report them as `N/A (D2)`, not as PASS.
- **§11 "C-44 certification count logged as an open question"**: D4 closes it. The count is 18 and verified. Report it as `closed by D4`.
- **§11 "errata.md seeded (C-67); misconception register seeded (C-68)"**: `errata.md` is seeded with R2's own corrections (RD-7). The misconception register is the generic one in `Curriculum` §0.4. The chat-derived entries are dropped under D2.
- **§11 "ledger primer-status subsection present (C-42, C-43)"**: present in R10, all `not-started`.
- **§8.2 "each count ≥ its R1 count" (R10)**: checkbox *ticks* are excluded (D2). Checkbox *lines* are still counted and may only grow.
- **Invariant 3 (progress preserved)**: does not apply (D2).
- **D3 is stricter than the prompt**: `CHANGELOG.md → Merges` may not drop text. A merged item's original lines must still be findable verbatim or through the journal (`d3_check.py`).

## 2. Rulings at the R2 gate (the learner replied "approve")

1. SQL `T1…T6` stay as `tx_tests.py` scenario labels. They are not IDs.
2. Bare level references get the file prefix (e.g. `E3` → `SQL-E3`).
3. SQL `P1…P11` become `PX-1…PX-11`.
4. SQL `E11` → `TX`, `E12` → `PX`, `E12.1` → `PX-1`.
5. Cyber `PR` becomes `PV` only at the one appendix use (input line 1201).
6. Cyber `C1`/`C2` at input lines 52, 101, 102 and 120 stay: they are `Curriculum` Track C modules.
7. A SQL tier legend (`SQL-T-HS/UG/GR`) is added to SQL §0 (done; journaled as new content under C-08).

## 3. Defaults taken (`[resolved-by-default]`; the learner may overrule any)

RD-1…RD-8 are in `refactor-state.md` §8. RD-2 and RD-3 lapse under D5 (there is no N-track). RD-9 (the cookie question) is withdrawn under D5. One interpretation default follows from D6/D7:

| # | Item | Default taken |
|---|---|---|
| RD-10 | How the files complement each other with no links | Superseded by D11: course-wide IDs stay as tags. Each companion keeps its own stitch table. The main course's §0.1 names the companions by title, with no file names. Shared rules (teaching contract, lab safety) are written into each companion's §0 so none depends on another file for them. |

## 4. Facts corrected against the prompt (the files win)

| Prompt says | Actual (command) |
|---|---|
| C-10: "see §B5 IAM" has 0 hits | 1 hit (cyber input line 244). Restored to "see §0.5" in R2. |
| C-25: 23 PRIMARY-before-prerequisite violations | 15 modules / 24 module–prerequisite pairs by a direct earliest-binding check (`binding.py`; `r0-reproduction.md` C-25) |
| C-42: 77 primer boxes, all unticked | Reproduced. R0's own first count (76+2) was wrong and was corrected in R1: 77 boxes on 76 lines (`count_boxes.py`) |
| C-59: ten ARCH modules lack a Check | 11: ARCH-01…03 and 05…12. The prompt omits ARCH-12 (`r0-reproduction.md` C-59) |
| C-10 `EA5` corruption, 1 place | 2 places (C-NEW-07) |
| "fifteen certifications" | eighteen (D4) |

## 5. Acceptance checks for the remaining phases

Each phase ends with its report and the 5-question self-review (§2 hardening 4), then **stops for "continue"**.

**R3 (hard gate).** `verify.py` produces `manifest-after.json` and `verification-report-R3.md`. It must:

- **Fold in the existing checks:** `d3_check.py --stage all`, `selfcontained.py`, `audit_r2b.py`, `rename_checks.py`, `binding.py`'s topological check, and every R2-due probe in `audit_r2.py` that still applies after R2b. Re-running R3 therefore re-proves R2 and R2b.
- **Normalise before-items through `id-rename-map.csv` and the journal** (anchor-rewrite, rename and regenerate chains) before hashing. Appended notes count as additions, never as changes to the item they follow. This was promised in the R1 report and is the only OPEN item in `audit-R2.md` §4.
- **The ID registry is the 5 course files.** Northstar is deleted (D5).
- **Treat these as non-references:** the SQL legend lines that list rebound labels, and the kit file names `selfcontained.py` allow-lists. (Provenance lines, `(was …)` notes and the D3 archive now live in `records/<file>`, outside the course files.)
- **Treat these as definitions or labels:**
  - the SQL tier legend defines `SQL-T-*`;
  - `T1…T6` are script labels;
  - `A2A` is whitelisted in the corruption regex (C-NEW-08);
  - the ID regex accepts `SD-\d{2}[a-c]?` and slice/recall notation (C-38).
- **Pass with:** zero orphans, zero undefined references, zero lost items, and zero live foreign-parent names or pseudo-anchors. It must also pass all primer §8.2 checks: the CC BY line, the mermaid edge superset, verbatim-table hashes, "my addition" 9/9, and C-31's 20-word rule (primer-authored paragraphs only).
- **Stop rule:** if the gate fails twice after fixes, stop and report. Never weaken a check.
- **Done (2026-09-24):** PASS on the first run after fixes; 42 of 42 GATE rows pass, D8 is HOLD. Results, fixes and tool corrections are in `refactor-state.md` §6e.

**R4 (`Curriculum`).** As the prompt planned it:
- New tracks M/U/S follow the §9.1 13-part standard, with a skip-test.
- `dag.json` + `dag_check.py` (C-65, §12.5): no cycles, no PRIMARY-before-prerequisite, no unknown IDs.
- `volatility-register.md` and `coverage-matrix.md`.
- A5/A8/A10 teaching-block splits (C-49 pattern).
- S6 secondary for PQ-S-06 (C-04).
- Revised scope estimate.
- New version-sensitive claims carry `(verify)`.
- D3: deepening only adds.

**Done (2026-09-24), with the D16 substitutions** (details in `refactor-state.md` §6f):
- **M/U/S:** withdrawn (D16). The stubs are in `records/`, the anchors are rebound, and a GATE confirms no token remains.
- **DAG:** `dag_check.py` passes. 213 nodes, 651 edges, no cycles, 0 of 537 hard edges out of PRIMARY order, 0 unknown IDs. Folded into `verify.py`.
- **Volatility register:** built, 183 rows. Nothing re-verified.
- **Coverage matrix:** not built. Part (a) needs the CS2023 list, which is not in the repo, and downloading needs permission.
- **Teaching blocks:** all six modules over 20 (A3, A5, A7, A8, A9, A10) have block notes, not only A5/A8/A10. A GATE checks that each note places every bound card.
- **C-04 S6 secondary:** moot under D16; PQ-S-06 is taught at A10.
- **Scope estimate:** Phases 0–3 total 599 concept units, 130–211 sessions.
- **`(verify)`:** R4 added no version-sensitive claim.
- **D3:** every rewritten line is in `records/`, and `d3_check.py --stage all` passes.
- **Verify:** `verify.py --stage R4`: 47/47 GATE PASS.

**R5 (primer).**
- §9.3.1 enhancements.
- Every `(verify)` flag is kept (C-40).
- P01–P08 / O01–O07 numbers and verbatim tables stay hash-identical.

**R6 (SQL).**
- Port the engine slices.
- The lab kit is verified **in place** from the repo-root `sql-companion-work/`: `run_ex.py` produces a match/mismatch report against the `goldens_*.json` files, and goldens are never edited (C-50, C-NEW-02).
- Pins go in the kit README and `run_ex.py` (C-56).
- `pgdata/` is never copied.
- The tool-availability rule (§2 hardening 8) applies: if PostgreSQL cannot be installed, say so and use the §12.2 fallback.

**R7 (patterns).**
- C-59: all 11 ARCH modules get their own Check.
- C-61: named real examples.
- C-60: per-line GoF quoting audit.

**R8 (cyber).**
- §9.3.4 enhancements.
- RD-9 cookie exercise.
- Decide on "the reference cloud app" → "Northstar" (open question 3). The corrupted cookie domain is fixed then.

**R9 (Northstar).**
- Fill the 16 milestones / 52 sections now stubbed.
- Architecture-changing milestones cite a P08 step and TF-n (C-32).
- The C-06 `Curriculum` anchors for N8.1.5/N8.1.6 are already listed.
- Reconstructed sections are labelled.

**R10.**
- Run §8.2 again, with counts ≥ R1 (ticks excluded, D2).
- Blank §14 ledger with C-23 checkpoints, all `not-started`.
- The §11 checklist, with the D2/D4 substitutions from §1 above.

## 6. Process rules (confirmed in the R0–R2 chat)

- **Phase stops.** Stop after every phase and wait for "continue". R2's gate needed "approve", which was received.
- **Files.** `inputs-original/` is read-only (`chmod a-w`; a fresh git checkout resets the mode, and `audit_r2.py` checks it). Invariant 14 is a separate check: the skill file and ledger stay byte-identical until R10.
- **Journal and evidence.** Every edit goes through the journal (`outputs/r2/journal.jsonl`, then `outputs/r2b/journal.jsonl` with a rule ID and the decision as evidence) with a class and evidence. No hand edits to a rename.
- **Idempotent tools.** Every tool is idempotent. Check: two runs under two `PYTHONHASHSEED`s give identical hashes over `work/`, `outputs/`, `diffs/` and the reports. From R2b on, the pipeline starts from the frozen R2 snapshot (`outputs/r2b/in/`, hash-checked), because the R2 pipeline read the deleted legacy file.
- **No downloads without asking.** Downloading any file needs the learner's explicit permission first. This was committed to in R0, after two PDFs were fetched without asking.
- **Deliverables go to the repo.** The prompt says `/mnt/user-data/outputs/`. Here, deliverables are committed under `refactor/` and pushed to branch `gcp`.
- **Honesty.** No check is reported as run unless it ran. Unsure mappings go to `refactor-state.md` §10 and are marked `[resolved-by-default]`.

## 7. Open questions for the learner

1. **RD-1, the nine checkpoint mappings:** do you accept them? They are expanded into full cards under D9 either way.

2. **D12 scope:** the Go companion takes only Nasiko's Go language and engineering nodes. Payments are now taught by GO-29 (D13), written from the standards and the owner modules rather than from the payments addendum. Do you also want the control-plane reconstruction phases (P0–P10), the service specifications, or the mathematics / ML tracks brought in? Each would need its own home under D7.

3. *(closed by D14: keep it)* **D8 after D13:** R3 passed with D8 as HOLD. Delete the restored `gcp-curriculum.md` now (`audit_r2b.py` then passes D8 too), or keep it?

4. *(closed by D15)* **Bare "Curriculum":** 68 places still use it as the parent's name (primer 59, patterns 6, main course 3). Rename them to "the main course" in R4?

5. **D16 restore offer:** R4 moved to `records/` the stub scope no module taught: number theory, the birthday bound, order statistics, proof sketches and the "rigorous pass" plans. Say if any of it should come back into an existing module.

6. **Coverage matrix (§12.4):** build part (b), exam-guide domains → modules, from Parts V–VII as they stand? Part (a), CS2023 → modules, needs the current CS2023 area list, and fetching it needs your permission.

Closed by D5: N6.16 meaning, the Northstar rename timing, and the cookie question.
