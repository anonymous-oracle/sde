# Refactor state

Meta prompt: `curriculum-refactor-meta-prompt.md` v1.2 (repo root) · Workspace: `refactor/` (the repo's `refactor/` folder; R0–R1 ran at `/Users/suhas/sde/refactor/`, R2 was finished in a cloud checkout of the same repo, branch `gcp`). Outputs go to `refactor/outputs/` and the workspace root.

**Resume point:** R2b, R2c and R2c-bis are **done**. R2c (D12) added the sixth part, the Go Language Companion, plus rule 0.4.9 and the tie-ins; see §6c. R2c-bis (D13) made the final gap check of the legacy GCP notes (17 small additions, `refactor-tools/r2c_gcp.py`), added GO-28 (authentication from scratch) and GO-29 (payment integration from scratch), and gave every GO module an involved problem with a rubric (rule 0.4.9's fourth rule); see §6d. `audit-R2b.md` has **one FAIL, D8**: the learner put `gcp-curriculum.md` back for the D13 check, and it is not deleted again without the learner's say-so (§10 question 2). No build step opens it (checked with an audit hook on every `open`, §6d). The six course files in `work/` are self-contained (D6), Northstar is gone (D5), each topic has one home (D7), and the gaps are filled (D9). Read `requirements-hardening.md` §1 first. Next: **R3 Verify** (§8.2). Write `refactor-tools/verify.py` (fold in `d3_check.py`, `selfcontained.py`, `audit_r2b.py`, `rename_checks.py` and the R2 probes of `audit_r2.py` that still apply after R2b; see §9), run it on `work/` to produce `manifest-after.json` and `verification-report-R3.md`. Hard gate: zero orphans, zero undefined references, zero lost items, zero file names or links. After a fresh checkout run `chmod a-w inputs-original/*`. Rebuild first with `python3 refactor-tools/r2b_build.py .`: it starts from the frozen R2 snapshot (`outputs/r2b/in/`, checked against `outputs/r2b/in.sha256`) and must reproduce the committed `work/`, `records/` and journal byte for byte. The R2 pipeline (`r2_build.py`, `northstar.py`, `r2_sql.py`'s slice port) and `r0_reproduce.py` read the deleted legacy file, so they no longer run; their outputs are frozen in `outputs/r2/` and `outputs/r2b/in/`.

| Phase | Status | Date | Deliverables |
|---|---|---|---|
| R0 Ingest | **done** | 2026-09-24 | `refactor-state.md`, `r0-reproduction.md`, `cert-verification.md`, `refactor-tools/r0_reproduce.py`, `refactor-tools/primer_bindings.py`, `inputs-original/` |
| R1 Manifest | **done** | 2026-09-24 | `manifest-before.json`, `manifest-before-summary.md`, `refactor-tools/manifest.py`, `refactor-tools/count_boxes.py` |
| R2 Repair | **done** | 2026-09-24 | `work/*` (5 repaired files + new `northstar-reference-app.md`), `id-rename-map.csv`, `crosswalk.md`, `primer-binding-table.md`, `CHANGELOG.md`, `errata.md`, `diffs/<file>.diff`, `outputs/r2/journal.jsonl`, `outputs/r2-gate/*`, tools listed in §7; pre-R3 audit `audit-R2.md` + `requirements-hardening.md` |
| R2b Self-contained rework (D5–D11) | **done** | 2026-09-24 | `work/*` (5 self-contained files; Northstar deleted), `records/<file>`, `outputs/r2b/journal.jsonl`, `outputs/r2b/in/` + `in.sha256`, `audit-R2b.md`; tools listed in §7; `gcp-curriculum.md` deleted |
| R2c Go Language Companion (D12) | **done** | 2026-09-24 | `authored/go-language-companion.md` (source) → `work/go-language-companion.md`; `refactor-tools/r2c_go.py` (run inside `r2b_build.py`); rule 0.4.9 in the main course and every contract copy; tie-ins in the primer, SQL, patterns and cyber companions; D12 check in `audit_r2b.py` |
| R2c-bis Final legacy check, GO-28/GO-29, involved problems (D13) | **done** | 2026-09-24 | `refactor-tools/r2c_gcp.py` (GAP-1…GAP-17, run inside `r2b_build.py`); GO-28, GO-29, GO-P01…GO-P29 and §10.2 rubrics in `authored/go-language-companion.md`; rule 0.4.9's fourth rule and two §0.3 rows in `r2c_go.py`; D12 audit extended |
| R3 Verify | **next** | | `refactor-tools/verify.py`, `manifest-after.json`, `verification-report-R3.md` |
| R4–R9 Enhance | pending | | |
| R10 Final | pending | | |

---

## 1. Inputs (read-only copies in `inputs-original/`)

| Logical name | Source on disk | Lines | SHA-256 |
|---|---|---|---|
| `Curriculum` | `/Users/suhas/sde/gcp.md` | 356 | `9fdc183aa9cecff18fb64b0fff5c3062cd1c5d1a59cea324ac298fb2dd95a907` |
| `system-design-primer-companion.md` | `/Users/suhas/sde/` | 1042 | `03adee11642228b984b500fe63b23d96891a3a1f8a7025e5bf1fe3e4bae19f5b` |
| `sql-databases-companion.md` | `/Users/suhas/sde/` | 3056 | `567579e55987ea2baaa5a3b5b06cbec4de1e535c6c58ab108a2a2330507f915f` |
| `design-patterns-companion.md` | `/Users/suhas/sde/` | 439 | `a0044a2c11f59eeb437bf34d20f1c95972e68bd4832e9dd55fd2d857a8474790` |
| `cloud-cybersecurity-companion.md` | `/Users/suhas/sde/` | 2715 | `48f2cc6f2df66eb156f24db59b65a21701ec5dce066ac154ca6f542b7020e27f` |
| `session-progress-ledger.md` | `/Users/suhas/session-progress-ledger.md` | 82 | `ffd20c5bb8905b65802635ad9f6ed18180a91116ead5d1e9d447563df631e418` |
| `learn-SKILL.md` (reference only, never edited) | `/Users/suhas/sde/` | 77 | `d794cc09183d2e0a25904a03ee24b4ce14db30ef609fbc9a123d192b8f91c83c` |

Not inputs, but used as source material under D1: `gcp-curriculum.md` (repo root, 8,120 lines; the old foreign parent) and `unified-curriculum.md`. The SQL lab kit `sql-companion-work/` (goldens) exists on the learner's machine (C-NEW-02).

## 2. Conflict reproduction (R0)

Full table and commands: `r0-reproduction.md` (regenerate with `python3 refactor-tools/r0_reproduce.py .`). **75 checked: 59 reproduced · 12 different · 4 chat-only · 0 not reproduced.** Differences that shaped the plan: C-05/06/07/47/54 owner content exists in `gcp-curriculum.md` (ported or borrowed under D1); C-01 counts are larger; C-10 has a second `EA5` corruption (C-NEW-07); C-25 is 15 modules / 24 pairs; C-29 has four 7-step protocols; C-31's resolution is new content; C-59 is 11 ARCH modules; C-68 3 of 4 in the ledger.

**R2 correction to R0:** R0 recorded C-10's "see §B5 IAM" as 0 hits. It occurs (cyber §3.3 intro, input line 244). R2 restored it to "see §0.5" (the University alignment table, whose CS255 row it points to). CHANGELOG, cyber, C-10.

## 3. New conflicts (C-NEW-nn)

| ID | Finding | Handling (status) |
|---|---|---|
| C-NEW-01 | `gcp-curriculum.md` / `unified-curriculum.md` on disk | closed by D1: borrow with `Source material:` lines; nothing points back |
| C-NEW-02 | SQL lab kit with goldens exists | C-50 becomes verify-in-place (R3/R7); `pgdata/` not copied |
| C-NEW-03 | ledger on disk predates the prompt's learner state | closed by D2 |
| C-NEW-04 | the cyber-pointer block splits Curriculum Part I | **done**: moved into `Curriculum` §0.1 (journal class move) |
| C-NEW-05 | Curriculum had no markdown headings for modules | **done**: `#`/`##`/`###` headings added; phase-plan diagram fenced |
| C-NEW-06 | design-patterns §0.3 is a fourth 7-step protocol | **done** via C-29 pointer |
| C-NEW-07 | `EA5` corruption also in a cyber `Lab:` line | **done** (rename.py C-10 restore) |
| C-NEW-08 | corruption regex false-positive on `A2A` | R3: whitelist `A2A` in verify.py |
| C-NEW-09 | 95 pseudo-anchor tokens, 10 forms (digits folded) in the cyber file | **done**: all removed from live text (`crosswalk.md` §6) |

## 4. Learner decisions (2026-09-24, binding, rung 1)

| # | Decision | Effect |
|---|---|---|
| D1 | `gcp-curriculum.md` is not part of the course. Any `.md` on disk may be borrowed from. | Foreign references rebound via §6 crosswalks. Missing owner content is written into the suite, with `Source material:` lines (SQL §4.0 DB-1…DB-10 ported in R2; Northstar sections in R9). |
| D2 | Fresh start: no progress carried over. | Invariant 3 does not apply. Ledger regenerated in R10 as a clean §14 template. C-43, C-67, C-68 dropped; C-69/C-73 evidence was chat-only and is dropped, but their §13.5/§13.9 rules are kept (`Curriculum` §0.4.7/§0.4.8). All boxes unticked (NT-04 too). Ledger §5 preferences **kept** and copied into every file's §0. |
| D3 | `gcp.md` is the primary Curriculum; content may be rearranged, never removed. | Stale text gets dated notes. Every line changed by a correction or regeneration keeps its pre-refactor text in the file's closing "Pre-refactor text archive (D3)". Checked by `d3_check.py`. Applied to all companions too. |
| D4 | Verify and keep all 18 certifications. | `cert-verification.md`; R2 annotated each cert (box, Lab Reality, D4 note) and corrected "fifteen" → "eighteen". |

| D5–D11 | Later the same day: course-wide IDs stay as stitch/mapping tags, material dependencies go (D11); companions serve only the Curriculum course; `gcp-curriculum.md` is a content reference with no rules taken from it (D10); drop Northstar and the cookie question (D5); 5 self-contained files, no file names or links, lab kit embedded, bookkeeping moved to `refactor/` (D6); one topic, one home (D7); delete `gcp-curriculum.md` once no longer needed (D8); expand the nine checkpoints and every other gap (D9). | Full text and readings in `requirements-hardening.md` §1. Supersedes the prompt's Track N (§9.4), §7 overlap register and "companion §0 points to `Curriculum`" rules. |
| D13 | Before R3: a final check of the restored `gcp-curriculum.md` for anything still missing ("not to unnecessarily add curriculum"); Go modules on payment and authentication integration, built from scratch; one involved problem per Go topic; a robustness review. | Full text and reading in `requirements-hardening.md` §1. Results in §6d. |
| D12 | Before R3: add a rule for teaching Go (language rules, contrasts with other languages) and a new Go companion built from `nasiko-curriculum.md`, tied into the other files. | Full text and reading in `requirements-hardening.md` §1. The sixth part is the Go Language Companion; the rule is 0.4.9. |

R0 questions Q1–Q4 are all superseded by D1–D4.

## 5. R1 baseline (manifest-before)

Regenerate with `python3 refactor-tools/manifest.py work --out manifest-before.json --summary manifest-before-summary.md` **on `inputs-original/`** (idempotent across runs and hash seeds). Non-blank lines / IDs: Curriculum 311/27 · primer 890/136 · SQL 2621/275 · DP 347/75 · cyber 2303/278 · ledger 58/19 · skill 46/0. Primer: 77 checkboxes, 46 mermaid edges / 41 nodes, §6.4–§6.7 counts as in the prompt. DP: 63 items. Before renames there were 95 primary collisions (E-levels, Z0.x, DD, PR, C1–C4, tiers) and 14 unresolved references.

## 6. R2 results

**Pipeline.** `python3 refactor-tools/r2_build.py .` rebuilds everything from `inputs-original/`: `rename.py` (§5, 37 rules; 1,108 replacements incl. journaled follow-ups) → renamed snapshot `outputs/r2/renamed/` → `binding.py` → per-file builders (`build_primer` in r2_build, `r2_cur`, `r2_sql`, `r2_sec`, `r2_dp`) → `work/` → `northstar.py` → journal → `reports.py`. **897 journaled edits.** Idempotent: three runs (two hash seeds) give identical hashes over `work/`, `outputs/r2/`, `diffs/` and all reports.

| File | Lines in → out | Classes (from CHANGELOG summary) |
|---|---|---|
| Curriculum | 356 → 643 | anchor-rewrite 41 (headings), move 1, append 69, correction 3, new-content 1 |
| primer | 1042 → 1202 | rename 46, anchor-rewrite 72, append 11, correction 9, new-content 2, regenerate 46 |
| SQL | 3056 → 3182 | rename 572, anchor-rewrite 173, append 5, correction 5, new-content 2 |
| patterns | 439 → 524 | rename 29, append 49, correction 3, new-content 1 |
| cyber | 2715 → 2936 | rename 461, anchor-rewrite 258, append 127, correction 5, new-content 1, regenerate 1 |
| Northstar (new) | — → 419 | skeleton: 16 milestones + 52 sections, all stubs for R9 |
| ledger, skill | unchanged | — |

**What R2 did, by file.**
- **Curriculum:** §0.1 files + stitch rule (cyber block moved here), §0.2 ledger preferences, §0.3 suite register (§7 rows), §0.4 Suite Teaching Contract (0.4.1–0.4.8), §0.5 Lab Safety; headings (C-NEW-05); C-18/C-19/C-20/C-21/C-48/C-75 dated notes; C-44 corrections; C-45 boxes (27 modules); C-46 Track D Lab Reality; C-49 A7 teaching blocks; C-05 A8 slice pointer; C-22 V-ID table; reserved M/U/S/N stub table; per-cert box + Lab Reality + D4 note (18).
- **Primer:** C-01/C-39 parent rewrites; CC BY modification line; C-24 header stitches, §2 and §4.5 regenerated from `primer-binding-table.md`; C-25, C-28, C-30, C-33, C-34 resolutions; §0.5 preferences; §2.1 → §0.3 pointer.
- **SQL:** §6.1 crosswalk (FOREIGN, 46 labels) incl. header stitches and §2 first cells; C-05 DB-1…DB-10 ported as §4.0 (Source material line); C-08 tier legend; C-09 `SQL-E<n>.x`; C-37; C-53 bibliography, Lab safety, Database protocol; C-57; provenance line.
- **Cyber:** §6.2 BIND for 125 modules with a Provenance line each; §2 regenerated; C-03 x.y → Nx.y; C-10 pseudo-anchors removed (95 → 0) and title/footers/Appendix V fixed; C-11 phantoms mapped; C-14 six CR bundles; C-17 intro; `gcp.md` → `Curriculum`.
- **Patterns:** C-16 A7 row; C-29 pointer; C-58 boxes (44 items + GRASP + AP lines); C-60; C-62; C-64 notation; §0.5 preferences.
- **Northstar:** every referenced `Nx.y` gets a section whose meaning is the same-numbered heading in `gcp-curriculum.md` (cited by line); 0 sections with unknown meaning.

**Checks run at the end of R2.**
- `rename_checks.py outputs/r2/renamed` → 23/23 PASS. (Runs on the renamed snapshot; `work/` adds Curriculum C-track anchors on purpose.)
- `d3_check.py .` → 0 lost lines in all 7 files. Every original non-blank line is verbatim in `work/` or reachable through the journal. A mutation test (one deleted primer line) makes it fail.
- `crosswalk.md` §0: 0 old-parent names left in live text outside provenance; §6: 0 live pseudo-anchors.
- `audit_r2.py .` → PASS (pre-R3 audit, `audit-R2.md`): C-01…C-75 + C-NEW-01…09 each assigned an owner phase; 67 R2-due probes PASS, 11 deferred, 6 D2; invariants 1/6/7/11/12/14/15-16, table lint, no live D8, D1–D4 and chat commitments checked. Only OPEN item: the R1 promise that verify.py normalises through the rename map (R3).
- Audit fixes (2026-09-24): cyber cert-row cells re-padded to 4 columns; duplicate CR-16 in a header stitch; §6.2 qualifiers (`A10 (gate for CR-01)`, `A10 (MFA)`); C-06 `Curriculum` anchors on N8.1.5/N8.1.6; C-71/C-74 tags in §0.4.
- `manifest.py work` preview: 0 primary collisions. Its 32 "unresolved" references are all expected and must be handled by verify.py, not by edits (§9).

## 6b. R2b results (D5–D11)

**Pipeline.** `python3 refactor-tools/r2b_build.py .` reads the frozen R2 output (`outputs/r2b/in/`, hash-checked), applies the generic rules G0–G5, G8–G10 to all five files, then the per-file rules in `r2b_cur.py`, `r2b_pri.py`, `r2b_sql.py`, `r2b_dp.py`, `r2b_sec.py`, and writes `work/`, `records/<file>` and `outputs/r2b/journal.jsonl`. **811 journaled edits.** Two runs give byte-identical `work/`, `records/` and journal.

| File | Lines R2 → R2b | Records entries | Journal classes |
|---|---|---|---|
| Curriculum | 643 → 612 | 109 | anchor-rewrite 107, move 2 |
| primer | 1202 → 1117 | 35 | anchor-rewrite 34, move 1, append 1, new-content 2 |
| SQL | 3182 → 6555 | 221 | anchor-rewrite 165, move 51, append 1, new-content 12 |
| patterns | 524 → 546 | 13 | anchor-rewrite 12, move 1, append 1 |
| cyber | 2936 → 2812 | 397 | anchor-rewrite 262, move 135, append 1, new-content 23 |
| Northstar | 419 → deleted | — | D5 |

**What R2b did.**
- **All files:** the D3 archive, provenance / `Source material:` lines and `(was …)` notes moved to `records/<file>` (D6; D3 still holds there, verbatim). File names, links and the backticked `Curriculum` are gone ("the main course"); course IDs stay as stitch tags (D11). Each companion carries a copy of the main course's §0.4 teaching contract and §0.5 Lab Safety in its own §0 (primer, SQL, patterns §0.6; cyber §0.7). "On a conflict §0.3 wins" now names the main course's register (G10).
- **Northstar (D5, D10):** every `N…` pointer is mapped to the course module that teaches the topic (cyber `NMAP`, 34 N-IDs; stitch headers via G8). Where the legacy text handed a lab to Northstar, the owning module now holds the lab: cyber CR-06, CR-13, CR-14, AU-03, AU-11, DOS-05, CL-01, WL-04 build labs and an IR-05 runbook. "The reference app" is defined once, in cyber §0.4 (the shop at `shop.example`).
- **SQL:** the whole lab kit (seed, scripts, goldens JSON, `run_ex.py` family) is printed in §3.8 from `sql-companion-work/`; only its two header comments and seven notes that named the legacy course were reworded (comments only, so no fingerprint changed). §8.2 now lists what each TF-DB plan must show; §9 gives SQL-CAP3 four acceptance tests and a tutor key.
- **Cyber (D9):** the nine checkpoints (RD-1) are full cards with a check question and key: SEC-Z0.5, SEC-E3.1, SEC-E3.5, SEC-E4.3, SEC-E4.16, SEC-E4.21, SEC-E6.5, SEC-E6.8, SEC-E10.7. Bare legacy section numbers (6.16, 7.2, …) rebound (SEC-13).
- **Primer (D7, D9):** SD-25 is the one home of the store-choice map; it gained the Filestore row and the anti-choices.
- **One home per topic (D7):** store choice, Firestore, Bigtable → primer SD-22/23/25; Cloud SQL → SQL OD-11; migrations OD-08; cursor pager OD-09; pool math OD-03; ledger DD-03; point-in-time joins DD-05; tenant RLS DD-09; key design DD-13; LSM vs B-tree CS-02; BigQuery ops AN-02; tokenization cyber PV-03; KMS/CMEK CR-14. Other files recall these by ID in one line.

**Checks run at the end of R2b.** `selfcontained.py .` → 5/5 PASS (V1 file names, with an allow-list of names whose full content is printed in the same file; V2 links; V3 Northstar and `N…` pointers; V4 backticked `Curriculum`; V5 legacy parent names; V6 legacy section numbers; V3/V4/V6 also inside code fences). `d3_check.py . --stage all` → 12/12 PASS (0 lost lines, R2 and R2b stages). `audit_r2b.py .` → PASS (`audit-R2b.md`): probe, D3, reproducibility from the snapshot, invariants 6/7/11/12, D2, D5, D7, D8, D9, D11. A Python audit hook confirmed the build opens no legacy file.

**Known limits (disclosed).** The reserved tracks M1–M6, U1–U7, S1–S11 are scope stubs in the main course and are authored in R4. Invariant 4 deviation: the ledger preferences copied into each file's §0 changed only in file-name tokens (D6). `audit_r2.py` probes the R2 state (provenance lines, the in-file D3 archive, Northstar in `work/`): run on the R2b `work/` it stops with a missing-file error on `northstar-reference-app.md`, so it is kept only as the record of R2; verify.py keeps only its probes that still apply.

## 6c. R2c results (D12, the Go Language Companion)

**Pipeline.** `refactor-tools/r2c_go.py` runs inside `r2b_build.py`, which is why the rebuild still starts from the frozen R2 snapshot and reproduces byte for byte. `r2c_go.cur` runs right after `r2b_cur.build`, so every companion's contract copy (made later) already carries rule 0.4.9. `r2c_go.build` runs last. It turns the authored source `authored/go-language-companion.md` into `work/go-language-companion.md`: the markers `@@PREFS@@` and `@@CONTRACT@@` become the main course's §0.2 (as §0.5) and `contract_copy(files, 5, 6)` (as §0.6). It also writes the tie-ins. Journal: 16 new entries, rule IDs GO-0…GO-8 and GO-10…GO-14. The new file is one new-content insert with no records entry, because nothing was replaced.

**What R2c did.**
- **Main course:**
  - §0.1 lists six parts and adds a sixth bullet.
  - §0.3 has three owner rows extended (rate limiting, SQL injection, GC) and six new rows (Go language; concurrency; data-structure code; patterns in Go; HTTP server timeouts; password hashing in a service).
  - Rule 0.4.2's layers are now: primer → SQL → patterns → **Go** → cyber.
  - New **rule 0.4.9**.
  - A3 gains the Go line (teaching blocks A3.G1–G4).
  - The shared contract intro now reads 0.4.1…0.4.9.
- **Go companion (663 lines):**
  - §0 (standing instruction, stitching rules, session shape with the unlock block, an unlock list per module, the preferences and contract copies).
  - Coverage ledger; stitch table (A3 primary; A4, A5, A6, A7, A8, A9, A10, A11, C1, C4, C6, U4, U5); overlap register.
  - 27 module cards, each with a Contrast line.
  - §9 contrast atlas; §10 54 exercises with keys (expected answer + expected wrong answer); §11 GO-CAP1–3 on `shop.example`; §12 dependency gate; §13 sources and honesty notes.
- **Tie-ins:**
  - Primer: an O-checkpoints note (Go after GO-27 / GO-11).
  - SQL OD-09: `cursorpage` in Go after GO-22.
  - Patterns: a §2 stitch-table row (the Go shape of PR-04/05, F-03, DP-01/04/12/13/14/18/20; DP-15 cannot be built by overriding).
  - Cyber: DOS-05 names GO-21; CR-13's Go library waits for GO-07 + GO-21.
- **Evidence behind the Go claims:**
  - Every `(checked on 1.27.1)` claim and every exercise-key output was run on Go 1.27.1 (linux/amd64) in a scratch module, with `GOTOOLCHAIN=go1.27.1 GOPROXY=off`.
  - The 1.27.1 toolchain itself was auto-downloaded once, when `go version` ran in the repo root under `GOTOOLCHAIN=auto` (the root `go.mod` says `go 1.27.1`). The download was not asked for first, and GO-01 and §13 of the companion say so.
  - Claims that were not run carry `(verify)`.

**Tool changes.**
- `selfcontained.py`:
  - covers six files;
  - allow-lists `_test.go` (the Go test-file suffix);
  - V2 now ignores code spans, which never render as links. Go generics such as `Map[T any](s []T)` had matched the link pattern.
- `audit_r2b.py`:
  - covers six files (invariant 7 only on the five with inputs);
  - gains **D12**: rule 0.4.9 is identical in all six parts; every contract intro reads 0.4.9; §0.1 lists six parts; GO-01…GO-27 are in order and only in the Go file; every GO / GO-E / GO-CAP reference resolves; every exercise has a key; every stitch tag is a main-course module (heading or reserved row); the four tie-ins are present.
  - Mutation-tested: removing a key and a tie-in made D12 fail with both named.

**Checks run at the end of R2c.**
- `selfcontained.py .` → 6/6 PASS.
- `d3_check.py . --stage all` → 12/12 PASS.
- `audit_r2b.py .` → PASS, 15 rows including D12 and the byte-identical rebuild.
- The 34 cross-part IDs the Go file cites (SD-, DP-, WA-, WL-, OD- and others) were checked against the headings of their owning files.

## 6d. R2c-bis results (D13)

**Legacy check (`refactor-tools/r2c_gcp.py`, GAP-1…GAP-17, all journaled into the main course).** The notes were read as material only (D10); the build never opens them. Added, each at its one home and only where no part taught it:
- Part V service map: Cloud Router, Cloud NAT, Private Service Connect, Network Connectivity Center, Cloud NGFW (GAP-1); Filestore, Persistent Disk / Hyperdisk, Backup and DR (GAP-2); Datastream, Data Fusion, Dataplex, BigLake, Analytics Hub (GAP-3); the pre-built AI APIs (GAP-4); IAP, Identity Platform, Secret Manager, Certificate Manager, Sensitive Data Protection, Organization Policy, Cloud Asset Inventory, Assured Workloads (GAP-5); Cloud Trace, Profiler, Error Reporting, Managed Prometheus, Service Health, billing reports and export, Recommender, Cloud Quotas, Carbon Footprint (GAP-6).
- PCA case studies named, `(verify)` against the live guide (GAP-7); the S8 migration scope (GAP-8) and the S11 case-study scope (GAP-9) filled; M5 numerical stability (GAP-10); the sketch formulas on the U2 register row, where the register already puts sketches (GAP-11).
- Track lines: observing a live Linux system (GAP-12); three budgets and GCP discount forms (GAP-13); IAM role types, conditions, deny policies, workforce federation (GAP-14); DORA metrics and platform engineering (GAP-15); load tests and chaos experiments against the SLO (GAP-16); applied ML problem families as literacy (GAP-17).

Checked and **not** added: Cloud Run tuning details (min instances, concurrency, cold starts; product detail under V-COMP); Northstar, the Part 12 continuation and Appendix M's case catalogue (D5, or already covered as families); the notes' pedagogy and session rules (D10); items already present under other names (double entry in SQL DD-03, budget alerts, org policy); a new migration module (the S8 scope holds it without a new ID); payments and authentication (taught instead by GO-28/GO-29).

**Go companion.** New §8.1 with GO-28 (authentication from scratch: `crypto/rand`, Argon2id record with rehash, hashed server-side sessions, `__Host-` cookies, CSRF, HS256 JWS from scratch then EdDSA, HOTP/TOTP, OAuth code + PKCE client) and GO-29 (payment integration from scratch: minor-unit money and largest-remainder splits, the transition table, idempotency keys, webhook verification on the raw body, inbox, double-entry ledger, partial refunds, CSV reconciliation, a fake PSP). Every GO module now ends with `Involved problem GO-Pnn` right after its Check, with its rubric in the new §10.2; §0.2 rule 8, §0.3 step 6, the unlock list, ledger (29), stitch table, overlap register, atlas (2 rows), exercises GO-E28.1…GO-E29.2 with keys, gate items 10–11 and §13 honesty notes are updated. Main course: rule 0.4.9 has a fourth rule (involved problem; it tightens rule 0.4.5 for GO modules), §0.1's Go bullet names the new scope, and §0.3 has two new rows (authentication built in code; payment-provider integration) and one extended row (password hashing).

**Evidence.** RFC 4226/6238/7636 vectors, the from-scratch HS256 token, cookie serialisation, constant-time comparison, Luhn and the float-money results were run on Go 1.27.1 with `GOTOOLCHAIN=go1.27.1 GOPROXY=off` in a scratch module; nothing was downloaded. `golang.org/x/crypto` was not in the module cache, so Argon2id is `(verify)`; so are all provider webhook formats. The involved problems were written, not solved; §13 says so.

**Checks at the end of R2c-bis.** `selfcontained.py` 6/6 PASS; `d3_check.py --stage all` 12/12 PASS; `audit_r2b.py` all rows PASS except D8 (the restored legacy file). D12 now derives the module count from the ledger total, and requires one involved problem per card right after its Check and one rubric per problem; mutation-tested (a deleted problem and a renamed rubric each made D12 fail, naming the fault). A Python audit hook on `open` during a full rebuild saw 88 files opened and none of them `gcp-curriculum.md` or the Nasiko notes.

## 7. Tools (`refactor-tools/`)

`r0_reproduce.py`, `primer_bindings.py` (R0) · `manifest.py`, `count_boxes.py` (R1) · `rename.py`, `rename_checks.py` (R2 gate) · `binding.py` (C-24/C-25 binding table + topological check) · `r2_build.py` (pipeline + primer builder) · `r2_common.py` (Doc/journal framework, constants, ledger preferences) · `r2_cur.py`, `r2_sql.py`, `r2_sec.py`, `r2_dp.py` (per-file builders) · `northstar.py` (Northstar skeleton) · `reports.py` (crosswalk, CHANGELOG, errata seed, id-rename-map copy, diffs) · `d3_check.py` (D3 no-removal) · `audit_r2.py` (pre-R3 audit → `audit-R2.md`; R2 state only) · **R2b:** `r2b_build.py` (pipeline, generic rules), `r2b_common.py` (`F` edit framework, journal, records), `r2b_shared.py` (contract copy, parent-name rewrite), `r2b_cur.py`, `r2b_pri.py`, `r2b_sql.py`, `r2b_dp.py`, `r2b_sec.py` (per-file rules), `selfcontained.py` (D6 probe V1–V6), `audit_r2b.py` (→ `audit-R2b.md`). No longer runnable after D8 (they read `gcp-curriculum.md`): `r0_reproduce.py`, `r2_build.py`, `r2_sql.py`, `northstar.py`. `requirements-hardening.md` pins how the prompt applies (decisions, gate rulings, corrected facts, per-phase acceptance checks).

`errata.md` is permanent and append-only: `reports.py` writes it only if it does not exist. `diffs/R2-01-renames.diff` is the approved gate diff (renames only); `diffs/<file>.diff` are full input-vs-work diffs.

## 8. `[resolved-by-default]` items (the learner may overrule any of them)

| # | Item | Default taken |
|---|---|---|
| RD-1 | C-11: nine phantom checkpoints | Mapped by content to SEC-E4.21, SEC-E10.7, SEC-E3.5, SEC-Z0.5, SEC-E3.1, SEC-E6.5, SEC-E6.8, SEC-E4.16, SEC-E4.3 (`crosswalk.md` §3). |
| RD-2 | C-06: numbering of N8.1.x | Follows the old parent (8.1.1 Bloom filter … 8.1.5 cursor pagination, 8.1.6 other primitives), not C-06's list order. |
| RD-3 | §6.3 meanings vs old-parent headings | Northstar uses the old parent's heading. Where §6.3 names a narrower subtopic (N6.11 packet-path map, N7.5 Binary Authorization, N7.8 key/SA IR, N7.9 governance) it is a part of that section. **N6.16 differs:** old heading "DNS and DDoS (security view)" vs §6.3 "Edge/DNS teardown". |
| RD-4 | C-15: DOS-01 / DOS-02 primaries | "A5 load balancing" / "A5 DNS/UDP". |
| RD-5 | C-NEW-05 heading markers | Logged as anchor-rewrite (line text unchanged; `###` prefix added). |
| RD-6 | Gate defaults R2-Q1, SQL-07/SEC-08, SQL-17, SQL-02/03, SEC-06, SEC-11 | As applied at the rename gate (`outputs/r2-gate/rename-dryrun-summary.md`). SQL `T1…T6` stay as `tx_tests.py` scenario labels. |
| RD-7 | `errata.md` seed | C-67's two chat errors dropped (D2). Seeded with the 3 content errors R2 corrected (C-44 ×2, C-60). |
| RD-8 | §6.2 "NT-04 already taught — mark done" | Not ticked (D2 fresh start). |
| RD-10 | Complementing without links (D6/D7) | Superseded by D11: IDs stay as tags; each companion keeps its stitch table; shared rules copied into each companion §0. |

## 9. What R3's verify.py must know

- Fold in `d3_check.py --stage all`, `selfcontained.py`, `audit_r2b.py`, `rename_checks.py`, `binding.py`'s topo check, and the probes of `audit_r2.py` that still apply after R2b (not those that look for provenance lines, the in-file D3 archive or Northstar). Report D2-vacuous §8.2/§11 items as `N/A (D2)`.
- File set: the 6 course files (the 5 originals plus the Go Language Companion, D12). Northstar is deleted (D5); no `N…` ID is defined or referenced. The Go companion has no input in `inputs-original/`: its source is `authored/go-language-companion.md`, and its D3 baseline is that source.
- Not references: SQL §0 legend lines that list rebound labels, and the kit file names that `selfcontained.py` allow-lists (each is printed in full in the same file; `audit.sh` is a table name in a query).
- Definitions: the SQL tier legend (`SQL-T-HS/UG/GR`, SQL §0) defines those tiers. SQL `T\d` are script labels (RD-6). Whitelist `A2A` (C-NEW-08).
- Compare after the rename map (§8.2), chaining `outputs/r2/journal.jsonl` and then `outputs/r2b/journal.jsonl`; lines R2b changed or moved are verbatim in `records/<file>` (`d3_check.py` shows how).
- Goldens: compare the *set* of fingerprints; §3.8 prints the goldens JSON, so each fingerprint now appears once more.
- Primer §8.2 checks: CC BY line identical + the change notice (now in words: "Modified on 2026-09-24, when this companion was fitted into the five-part course."); mermaid edge superset; binding-table topo check; "my addition" labels present; verbatim-table hashes.

## 10. Open questions (for the learner)

1. RD-1: accept the nine checkpoint mappings (expanded into full cards under D9 either way)?
2. D8 after D13: `gcp-curriculum.md` is back in the repo. The D13 check is done and no build reads it. Delete it again now (audit D8 then passes), or keep it until R3? R3's hard gate cannot pass D8 while it is present.

## 11. Deferred (not R2 by the prompt's phase rules)

- A5/A8/A10 teaching-block splits → R4. C-59 checks / C-61 examples / the C-60 per-line audit → R7. Northstar content: dropped (D5). Ledger regeneration → R10. Volatility register, coverage matrix, DAG → R4+.
