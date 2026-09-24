# Refactor state

Meta prompt: `curriculum-refactor-meta-prompt.md` v1.2 (repo root) · Workspace: `refactor/` (the repo's `refactor/` folder; R0–R1 ran at `/Users/suhas/sde/refactor/`, R2 was finished in a cloud checkout of the same repo, branch `gcp`). Outputs go to `refactor/outputs/` and the workspace root.

**Resume point:** R2 is **done** and waiting for "continue". Next: **R3 Verify** (§8.2). Write `refactor-tools/verify.py` (it must fold in `d3_check.py` and `rename_checks.py`; see §9 for what it must know), run it on `work/` to produce `manifest-after.json` and `verification-report-R3.md`. Hard gate: zero orphans, zero undefined references, zero lost items. Rebuild everything first with `python3 refactor-tools/r2_build.py .`; it is idempotent, so the output must be byte-identical to what is committed.

| Phase | Status | Date | Deliverables |
|---|---|---|---|
| R0 Ingest | **done** | 2026-09-24 | `refactor-state.md`, `r0-reproduction.md`, `cert-verification.md`, `refactor-tools/r0_reproduce.py`, `refactor-tools/primer_bindings.py`, `inputs-original/` |
| R1 Manifest | **done** | 2026-09-24 | `manifest-before.json`, `manifest-before-summary.md`, `refactor-tools/manifest.py`, `refactor-tools/count_boxes.py` |
| R2 Repair | **done** | 2026-09-24 | `work/*` (5 repaired files + new `northstar-reference-app.md`), `id-rename-map.csv`, `crosswalk.md`, `primer-binding-table.md`, `CHANGELOG.md`, `errata.md`, `diffs/<file>.diff`, `outputs/r2/journal.jsonl`, `outputs/r2-gate/*`, tools listed in §7 |
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
| D2 | Fresh start: no progress carried over. | Invariant 3 does not apply. Ledger regenerated in R10 as a clean §14 template. C-43, C-67, C-68, C-69, C-73 dropped. All boxes unticked (NT-04 too). Ledger §5 preferences **kept** and copied into every file's §0. |
| D3 | `gcp.md` is the primary Curriculum; content may be rearranged, never removed. | Stale text gets dated notes. Every line changed by a correction or regeneration keeps its pre-refactor text in the file's closing "Pre-refactor text archive (D3)". Checked by `d3_check.py`. Applied to all companions too. |
| D4 | Verify and keep all 18 certifications. | `cert-verification.md`; R2 annotated each cert (box, Lab Reality, D4 note) and corrected "fifteen" → "eighteen". |

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
| Northstar (new) | — → 417 | skeleton: 16 milestones + 52 sections, all stubs for R9 |
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
- `manifest.py work` preview: 0 primary collisions. Its 32 "unresolved" references are all expected and must be handled by verify.py, not by edits (§9).

## 7. Tools (`refactor-tools/`)

`r0_reproduce.py`, `primer_bindings.py` (R0) · `manifest.py`, `count_boxes.py` (R1) · `rename.py`, `rename_checks.py` (R2 gate) · `binding.py` (C-24/C-25 binding table + topological check) · `r2_build.py` (pipeline + primer builder) · `r2_common.py` (Doc/journal framework, constants, ledger preferences) · `r2_cur.py`, `r2_sql.py`, `r2_sec.py`, `r2_dp.py` (per-file builders) · `northstar.py` (Northstar skeleton) · `reports.py` (crosswalk, CHANGELOG, errata seed, id-rename-map copy, diffs) · `d3_check.py` (D3 no-removal).

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

## 9. What R3's verify.py must know

- File set: the 5 course files **plus `northstar-reference-app.md`**. `manifest.py` does not scan Northstar yet, so every `Nx` shows as unresolved.
- Not references: `- **Provenance**` lines, `*(was …)*` / `(was E-…)` notes, `Source material:` lines, the D3 archive section, and SQL §0 legend lines that list rebound labels (`D8`, `G12b`).
- Definitions: the SQL tier legend (`SQL-T-HS/UG/GR`, SQL §0) defines those tiers. SQL `T\d` are script labels (RD-6). Whitelist `A2A` (C-NEW-08).
- Current unresolved list from the preview: Curriculum `N12`; SQL `D8`, `N5/N7/N9`, `SQL-T-*`, `T1–T6`; cyber `D8`, the 9 `E-XX` (all in `(was …)` or archive), `N1/N3–N7/N9/N10`. Every one of them is covered by the rules above.
- Compare after the rename map (§8.2). The anchor-rewrite and regenerate originals are in `outputs/r2/journal.jsonl`; `d3_check.py` shows how to chain them.
- Primer §8.2 checks: CC BY line identical + modification note; mermaid edge superset (after C-39 label rewrite); binding-table topo check (`binding.py`); §2/§4.5/headers derive from the table; "my addition" labels present; verbatim-table hashes.

## 10. Open questions (for the learner)

1. **N6.16 meaning** (RD-3): keep "DNS and DDoS (security view)" from the old parent, or use §6.3's "Edge/DNS teardown"?
2. **C-11 mappings** (RD-1): accept the nine phantom → card mappings?
3. **"the reference cloud app"** (×36 in the cyber input): rename to "Northstar" in R9 (the plan), or earlier? One corrupted cookie example (`Domain=.the reference cloud app.example`) is left untouched until then.

## 11. Deferred (not R2 by the prompt's phase rules)

- A5/A8/A10 teaching-block splits → R4. C-59 checks / C-61 examples / the C-60 per-line audit → R7. Northstar content → R9. Ledger regeneration → R10. Volatility register, coverage matrix, DAG → R4+.
