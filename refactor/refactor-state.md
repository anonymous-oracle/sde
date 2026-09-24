# Refactor state

Meta prompt: `curriculum-refactor-meta-prompt.md` v1.2 · Workspace: `/Users/suhas/sde/refactor/` (§1's `/mnt/user-data/outputs/` does not exist on this machine, so outputs go to `refactor/outputs/`).

**Resume point:** R0 is complete and decisions D1–D4 are recorded (§4a). Certification verification is done (`cert-verification.md`). Waiting for "continue". The next phase is **R1, Manifest**.

| Phase | Status | Date | Deliverables |
|---|---|---|---|
| R0 Ingest | **done** | 2026-09-24 | `refactor-state.md`, `r0-reproduction.md`, `refactor-tools/r0_reproduce.py`, `refactor-tools/primer_bindings.py`, `inputs-original/` |
| R1 Manifest | pending | | |
| R2 Repair | pending (approve gate) | | |
| R3 Verify | pending | | |
| R4–R9 Enhance | pending | | |
| R10 Final | pending | | |

---

## 1. Inputs (read-only copies in `inputs-original/`; writable copies in `work/`, currently byte-identical)

| Logical name | Source on disk | Lines | SHA-256 |
|---|---|---|---|
| `Curriculum` | `/Users/suhas/sde/gcp.md` | 356 | `9fdc183aa9cecff18fb64b0fff5c3062cd1c5d1a59cea324ac298fb2dd95a907` |
| `system-design-primer-companion.md` | `/Users/suhas/sde/` | 1042 | `03adee11642228b984b500fe63b23d96891a3a1f8a7025e5bf1fe3e4bae19f5b` |
| `sql-databases-companion.md` | `/Users/suhas/sde/` | 3056 | `567579e55987ea2baaa5a3b5b06cbec4de1e535c6c58ab108a2a2330507f915f` |
| `design-patterns-companion.md` | `/Users/suhas/sde/` | 439 | `a0044a2c11f59eeb437bf34d20f1c95972e68bd4832e9dd55fd2d857a8474790` |
| `cloud-cybersecurity-companion.md` | `/Users/suhas/sde/` | 2715 | `48f2cc6f2df66eb156f24db59b65a21701ec5dce066ac154ca6f542b7020e27f` |
| `session-progress-ledger.md` | `/Users/suhas/session-progress-ledger.md` | 82 | `ffd20c5bb8905b65802635ad9f6ed18180a91116ead5d1e9d447563df631e418` |
| `learn-SKILL.md` (reference only, never edited) | `/Users/suhas/sde/` | 77 | `d794cc09183d2e0a25904a03ee24b4ce14db30ef609fbc9a123d192b8f91c83c` |

All seven files are valid UTF-8 and were read in full.

The following files are not inputs, but R0 found and read them:
- `/Users/suhas/sde/gcp-curriculum.md`: 8,120 lines, 641 KB, modified 2026-09-22. This is the original foreign parent.
- `/Users/suhas/sde/unified-curriculum.md`: 569 KB.
- `/Users/suhas/sde/gcp.md.pre-cyber-pointer`
- `/Users/suhas/sde/sql-companion-work/`: the SQL lab kit.

## 2. Conflict reproduction summary

Full table, commands and captured output: `r0-reproduction.md`. To regenerate it, run `python3 refactor-tools/r0_reproduce.py .`.

**75 checked: 58 reproduced · 13 different · 4 chat-only · 0 not reproduced.**

Differences that change the plan:
- **C-05 / C-06 / C-07 / C-47 / C-54: the owner content is not lost.** DB-1…10 (definitions), 8.1.1–8.1.6, 0.4, 5.3, 9c.1, Part 11/11b, the ten-rung ramp and Prop Lock all exist in `gcp-curriculum.md`. R2 can *port* them with provenance instead of *reconstructing* them (C-07's own clause asks for this).
- **C-50: the SQL lab kit exists.** R2/R3 verify the goldens against it rather than rebuilding them.
- **C-01: bigger counts, same fix.** SQL has 38 `gcp-curriculum` and 4 `unified-curriculum` references.
- **C-10.** "see §B5 IAM" does not occur. There is a second `EA5` corruption in a `Lab:` line (C-NEW-07).
- **C-25.** A direct check finds 15 modules / 24 module-prerequisite pairs, not 23. C-26's SD-10 case is transitive only (SD-10 → SD-02 → SD-01@A6).
- **C-29.** There are four 7-step protocols; the design-patterns companion has one too.
- **C-31.** Primer rule 9 is "Read economically". No "do not copy" rule exists, so the C-31 resolution is new content.
- **C-42.** There are 78 box tokens (76 line-start + 2 inline), not 77. None is ticked.
- **C-59.** 11 ARCH modules lack a Check, not 10. The single §7 Check at line 363 sits after ARCH-04.
- **C-68.** 3 of the 4 error examples are in ledger §2; the "authoritative server/OS" one is chat-only.
- **Chat-only: C-43, C-67, C-69, C-73.** These can't be checked from the files. They are seeded from the prompt's descriptions and labelled "per refactor prompt, not in ledger".

## 3. New conflicts (C-NEW-nn)

| ID | Finding | Proposed handling |
|---|---|---|
| C-NEW-01 | The foreign parent `gcp-curriculum.md` (and `unified-curriculum.md`) is on disk. | Port the owner sections verbatim with a provenance line (Q1). |
| C-NEW-02 | The SQL lab kit (`sql-companion-work/`) exists with its goldens. | C-50 becomes verify-in-place. `pgdata/` (526 MB) is not copied into outputs. |
| C-NEW-03 | The ledger on disk (2026-09-21) predates the state the prompt describes. Its open question is the 24-h TTL migration; it has no NT-04, no cookie question and no cyber companion in §1. | Treat the prompt as the newer learner state (ladder rung 1), but keep **both** open questions in YAML `open_questions` (Q2). |
| C-NEW-04 | `Curriculum` is `gcp.md`. A cyber-pointer section (lines 93–103), added 2026-09-22, splits Part I between A10 and A11. | Use `gcp.md` as the input (it is newer). R2 moves that block into a §0 companion-pointer section (move, not delete) (Q3). |
| C-NEW-05 | `Curriculum`'s only markdown heading is line 95, from the spliced section. Native module lines are plain text. | R1 parses module lines by regex. R2 adds headings (a structural change, logged). |
| C-NEW-06 | The design-patterns §0.3 is also a 7-step protocol. | Handled by C-29: all four protocols are replaced by `Curriculum` §0.4 pointers. |
| C-NEW-07 | The corrupted anchors in the cyber companion also appear in a `Lab:` line (line 194, `EA5`), not only in headings. | The C-10 fix covers references as well as headings. |
| C-NEW-08 | The corruption regex `[A-Z]\d+[A-Z]` false-positives on `A2A` (Agent2Agent protocol, Curriculum). | Whitelist `A2A` in the R3 scan. |
| C-NEW-09 | The cyber companion has 90 pseudo-anchor tokens in 22 distinct forms (`A10/B5.x`, `A5/Phase4-Net.x`, `Phase4-Sec.x`, `A5 TLS / Phase 4 Armor`). | Rebind all of them via the §6.2 crosswalk (R2). |

Also noted, no conflict: "the reference cloud app" appears ×36 in the cyber companion, matching the prompt. SQL `DD-04`/`DD-12` are schema-design IDs that also collide with cyber `DD-` (covered by C-09).

## 4a. Learner decisions (2026-09-24, binding, rung 1 of the precedence ladder)

| # | Decision | Effect on the plan |
|---|---|---|
| D1 | **`gcp-curriculum.md` is not part of this course.** The course is `Curriculum` (gcp.md) plus the 4 companions. Any `.md` on disk may be used as helpful source material. | Foreign references in the SQL and cyber files are rebound to `Curriculum` anchors through the prompt's §6 crosswalks. Missing "owner" content (DB slices, N-track primitives, the teaching protocol) is **written into the new files**. It may borrow from `gcp-curriculum.md` / `unified-curriculum.md`, with a `Source material:` provenance line. Nothing points back at those files. C-NEW-01 is closed: C-05/06/07/47/54 revert to "reconstruct" (borrowing allowed). |
| D2 | **Fresh start: no progress-related refactoring.** | Learner progress is not carried over. Invariant 3 does not apply. The ledger is rebuilt as a clean §14 YAML template: empty progress, no open questions, no error history. Every checkbox is unticked (all already are). C-43, C-67, C-68, C-69 and C-73 are dropped as progress/chat-state items. C-NEW-03 is closed. **Kept:** ledger §5 teaching preferences (woven checks, full depth and rigour, teach-once stitching, flag unmapped IDs). These are how to teach, not progress. See the note in the R0 follow-up report. |
| D3 | **`gcp.md` is the primary Curriculum. Content may be rearranged, never removed.** | This strengthens invariant 1. Every original Curriculum line must survive in the output: moved, or annotated with a note beneath it, never deleted. Stale or time-bound text (C-18, C-19, C-20, C-48) stays and gets dated annotations instead of rewrites. The cyber-pointer block moves into §0 (C-NEW-04). R3 adds a script check: every original line appears in the output after ID renames. The same no-removal rule is applied to the 4 companions. |
| D4 | **Verify all 18 certifications and keep them.** | Done: see `cert-verification.md`. All 18 are real and registrable. Changes to annotate in R2: PCA weights, question count and case studies; the PMLE section rename and Agent Platform move; the Agentic Architect guide not naming "Agent Registry/Gateway"; SAP-C02 → SAP-C03 (last C02 day Nov 17, 2026); the SCS-C03 domain name; the AZ-400 July 27 revision; the SC-100 Oct 21 revision and renamed prerequisite. "Fifteen" becomes "eighteen" at lines 6 and 27. |

## 4. Open questions (R0; superseded by 4a)

| # | Question | Default if no answer |
|---|---|---|
| Q1 | `gcp-curriculum.md` is present. Port its owner sections (DB-1…10, 8.1.x, 0.4, 5.3, 9c.1, Part 11/11b, the ten-rung ramp, Prop Lock) verbatim into the new files with provenance, or reconstruct them as the prompt assumes? | **Port**, edited only for ID renames. Where a reconstruction slot has no original, it is marked `(reconstructed)`. |
| Q2 | The ledger on disk ends at the TTL-migration question. The prompt says DNS is finished including NT-04 and that the HttpOnly/`Domain=.example.com` cookie question is open. Which is current? | Follow the prompt's state, record both questions as open, and set NT-04 to `taught, unverified` (not `mastered`). |
| Q3 | Use `gcp.md` (with the 2026-09-22 cyber-pointer section) as the `Curriculum` input? | **Yes.** The section moves into §0 during R2. |
| Q4 | C-44: Curriculum line 6 says "Fifteen professional-tier certifications", but 18 are listed. Change it to 18 or annotate it? | Change it to **18** with a `(verify)` flag, and log it as a factual correction. |

## 5. Invariant status at end of R0

- No input modified (`work/` = `inputs-original/` by hash).
- No renames performed.
- Golden values untouched.
- Learner progress untouched. Under D2, progress is now out of scope.
- R0 follow-up: I fetched vendor pages and exam guides for certification verification (read-only, public). Two Google guide PDFs sit in the session scratchpad and one in the tool-results cache; none of them are in the workspace.
- No lab or network activity. The PG cluster in `sql-companion-work/pgdata` is stopped.
