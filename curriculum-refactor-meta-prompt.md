# META PROMPT — Curriculum Suite Refactor, Conflict Resolution & Academic Enhancement

**Version:** 1.2 · **Written:** September 24, 2026 · **For:** a Claude session with a code-execution container.

**What changed in v1.2:**

- **The pending audits are closed.** `Curriculum`, the SQL companion, the design-patterns companion, the ledger, and the teaching method (`learn-SKILL.md`) were each script-audited line by line, as the primer and cyber companions already had been. The findings are §4.I–§4.L, C-44 to C-75.
- **Hardening.** Four new parts:
  - **§1 invariants 13–16:** a precedence ladder, read-only inputs, an evidence rule, and a no-silent-change rule;
  - **a hardened execution protocol in §2:** integrity checks, an approval gate, self-review, stop rules, and context management;
  - **§12 Content hardening:** execution-verified exercises, a volatility register, a coverage matrix, a global prerequisite DAG, and an errata log;
  - **§13 Teaching hardening:** a single Suite Teaching Contract, mastery states, spaced retrieval, a misconception register, check-question quality rules, an exercise pre-flight, suite-wide Prop Lock, pacing budgets, and a session-close protocol.
- **§14:** a machine-checkable ledger schema.
- **Acceptance criteria:** §11 gains matching checks.

**What changed from v1.0:** v1.0 covered the system-design-primer companion only in passing: its parent reference, its Part V anchors, a rename of its tiers, and a short enhancement list. v1.1 adds a dedicated audit of that file:

- **§4.H**, conflicts C-24 to C-43, each found by script against the actual file;
- primer-specific rename and regex rules in **§5**;
- primer ownership rows in **§7**;
- primer manifest items in **§8**;
- a rewritten **§9.3.1**. The v1.0 instruction to "remove content duplicated from Track S" broke the no-content-loss invariant and has been withdrawn;
- primer ledger reconciliation in **§10**;
- primer acceptance checks in **§11**;
- a fix to the reference to a non-existent §8.3 in the R10 row of §2.
**Target files (7 inputs: six to refactor, plus one read-only method reference):**

1. `Curriculum` — the primary syllabus.
2. `system-design-primer-companion.md`
3. `sql-databases-companion.md`
4. `design-patterns-companion.md`
5. `cloud-cybersecurity-companion.md`
6. `session-progress-ledger.md` — the learner's progress.
7. `learn-SKILL.md` — the tutoring method. It is **read-only** and is not refactored, but §13 reconciles it with the ledger and the companions. It is identical to the installed `learn` skill apart from trailing whitespace.

**How to use:** upload this file together with all six input files into a new chat. Then say:
"Execute the meta prompt, starting at Phase R0."

---

## 0. Role, mission, and what "done" means

You are acting as a **curriculum architect and technical editor**. You have two jobs, and you do them in this order.

**Job 1 — Repair.** Make the five syllabus files one internally consistent course. That means:

- one parent file;
- one ID namespace;
- every stitch reference resolving to a real section;
- no corrupted tokens;
- no phantom IDs;
- **zero content lost**.

Repair changes structure and references only. It never changes teaching content.

**Job 2 — Enhance.** Only after Job 1 has passed verification (Phase R3), expand the suite into a **complete practical cloud and system-architecture design course**. Every undergraduate prerequisite must be taught at academic depth: definitions, theorems, proofs or proof sketches where an undergraduate course would include them, worked examples, and graded exercises. All of it must stay tied to real cloud practice.

"Done" means every acceptance check in §11 passes. You also deliver:

- the refactored files;
- an ID rename map;
- a crosswalk;
- a changelog;
- a verification report;
- an updated session ledger.

---

## 1. Invariants — never violate these

1. **No content loss.** Every heading, module, bullet, table row, check question, lab, exercise card, instructor key, golden value, and honesty/verify note in the inputs must still exist in the outputs. It may be renamed, moved, or merged. When merged, the merged text must contain everything its sources contained. Section 8 of this prompt proves this mechanically.
2. **Repair before enhancement.** Phases R1–R3 add no new teaching content. Phases R4 onward add content and delete none.
3. **Learner progress is sacred.**
   - Everything marked done in `session-progress-ledger.md` §3 and §4 stays done under whatever ID it ends up with.
   - Completed modules are never re-scheduled for re-teaching.
   - New material that deepens a completed module becomes an **extension pass**: it recalls the earlier material in one line, then builds on it.
   - The learner is currently in **A5**. DNS is finished, including the security companion's NT-04. One exercise is still open: the HttpOnly + `Domain=.example.com` cookie question.
4. **The teaching preferences in ledger §5 are binding** and must be copied, unchanged, into every file's §0 standing instructions. They are:
   - Check questions are woven into the explanation itself, never asked as separate diagnostics.
   - Maintain curriculum depth and academic rigour.
   - Teach overlapping companion content once, stitched into the same session.
   - Flag ID mismatches plainly.
5. **Owner rules survive.** "Teach once in the owner, others only add" stays the core rule. Where two companions both claim a concept, §7 of this prompt decides the owner.
6. **Golden values are immutable.** The SQL companion's §6 goldens and Appendix K values were executed on PostgreSQL 15.8. Never edit, recompute, or invent them. When exercise IDs are renamed, the keys move with them unchanged.
7. **Honesty.**
   - Keep every `(verify)` flag.
   - Add `(verify)` to any new version-sensitive product detail, exam-domain weight, or date.
   - Never state an exam date, product feature, or price as fact without either a live check or a verify flag.
8. **Copyright.**
   - Textbooks and courses are cited at chapter or lecture level and paraphrased.
   - Never reproduce passages, problem sets, or exam questions from any source.
   - Every new exercise is original.
9. **Lab safety** follows the cyber companion's §0.2 rule 10 and applies to every file:
   - no scanning of third parties;
   - no malware;
   - no live DDoS;
   - no credential stuffing;
   - crypto only through vetted libraries;
   - loopback fixtures or disposable projects only.
10. **Lab Reality** follows `Curriculum` §0. Every new lab gets a tag:
    - `[free-tier]`
    - `[credit ~$X]`
    - `[plan-only]`
    - `[paper]`
    - `[local]`
11. **CC BY 4.0 compliance (primer companion).** The primer is licensed CC BY 4.0 (Copyright 2017 Donne Martin). Two consequences:
    - The attribution line at the top of `system-design-primer-companion.md` must survive every phase unchanged.
    - Because the refactor modifies the file, add a line directly under the attribution: "Modified by the curriculum refactor on <date>; changes listed in CHANGELOG.md", as CC BY 4.0 §3(a)(1)(B) requires.
    
    The primer material that the file itself labels *verbatim* is §6.1 (powers of two) and §6.2 (latency numbers). It is licensed and attributed, so it stays verbatim: it is **not** subject to invariant 8's paraphrase rule, and it must not be paraphrased away. Nothing new is ever copied from the primer repository beyond what is already in the file.
12. **Primer numbers are immutable, like SQL goldens.** This covers:
    - every figure labelled "primer:" or "Primer numbers", such as P08's 10 M users, 400 writes/s, and 40,000 reads/s;
    - the §6.1 and §6.2 tables;
    - the §1 coverage counts: 8 + 6 solved problems, 23 questions, 17 architectures, 23 companies, 40 blogs, and 42 + 8 + 6 Anki notes.
    
    Items labelled "my addition" / "my math" (see primer §7.1) may be extended, but never silently merged into primer-attributed text. The primer-vs-addition provenance boundary must stay visible.
13. **Precedence ladder.** When two rules conflict, the higher rule wins. Record every use of this ladder in `CHANGELOG.md → Precedence decisions`.
    1. The learner's explicit instruction in the current chat.
    2. Ledger §5 standing preferences.
    3. The invariants in this §1.
    4. `Curriculum` on order, cert timing, and Lab Reality.
    5. The owning companion on its content (§7).
    6. This prompt's defaults.
    7. `learn-SKILL.md` defaults.
    
    Example: the skill's "ask one calibrating question" yields to ledger §5's "no diagnostic probing" (C-70).
14. **Inputs are read-only.** In R0, copy all inputs to `inputs-original/`, record their SHA-256 hashes, and never modify those copies. All work happens on copies in `work/`. Every delivered file comes with a unified diff against its original (`diffs/<file>.diff`), so the learner can review exactly what changed.
15. **Evidence rule.** Any statement in a phase report about what a file contains must cite `file:line` or the grep/script that produced it. "I believe the file says…" is not allowed. Reconstructed or authored content is always labelled as such.
16. **No silent change.** Every edit falls into exactly one of these classes: rename, anchor rewrite, move, merge, append, correction, or new content. Each is logged in `CHANGELOG.md` with its class, and each **correction** of existing teaching text needs an evidence line explaining why the original was wrong. Corrections to technical claims need a citation (docs, textbook section, or an executed check).

---

## 2. Execution protocol (phased — do not compress)

The job is too large for one response. Run these phases in order. **End each phase by delivering its files and a short phase report, then stop and wait for "continue".** Carry state forward in `refactor-state.md`, which you create in R0 and update every phase, so that a fresh chat can resume from it.

| Phase | Name | Delivers |
|---|---|---|
| **R0** | Ingest | Read all six files fully (use `view` and `grep`; don't skim). Create `refactor-state.md`. Confirm that every conflict in §4 reproduces in the actual files. Log any new conflicts you find as C-NEW-nn. |
| **R1** | Manifest | Run the §8.1 scripts to produce `manifest-before.json`: every ID, heading, table row, checkbox, Check/Lab line, and key, with counts per file. |
| **R2** | Repair | Apply §4 resolutions (including §4.H for the primer), the §5 rename map, the §6 crosswalks, and the §7 ownership rulings. Rebuild the primer's §2, §2.1, and §4.5 as primer §7.3 requires (C-41). Deliver the repaired files, `id-rename-map.csv`, `crosswalk.md`, `primer-binding-table.md` (C-24), and `CHANGELOG.md`. |
| **R3** | Verify repair | Run §8.2 to produce `manifest-after.json` and `verification-report-R3.md`. **Hard gate:** zero orphans, zero undefined references, zero lost items. If anything fails, fix it and re-run. Do not proceed until it passes. |
| **R4** | Enhance `Curriculum` | §9.2: new tracks, deepened modules, the revised phase plan, and a revised scope estimate. |
| **R5** | Enhance primer companion | §9.3.1 (rewritten in v1.1) |
| **R6** | Enhance SQL companion | §9.3.2, including porting the engine slices. |
| **R7** | Enhance design-patterns companion | §9.3.3 |
| **R8** | Enhance cyber companion | §9.3.4 |
| **R9** | Northstar reference application | §9.4. Author the N-track milestone file. |
| **R10** | Final verification and ledger | §8.2 re-run, §10 new ledger, §11 acceptance checklist. |

**Within each phase:**

- Use Python or bash in the container for every mechanical operation (ID renames, reference rewrites, manifests). Never hand-edit a rename across 2,700 lines.
- Build long files section by section, reviewing as you go.
- Save outputs to `/mnt/user-data/outputs/` and deliver them as downloadable files.

**If you are unsure of a mapping:**

- Do not guess silently.
- Record it in `refactor-state.md → Open questions`.
- Apply the §6 default rule ("bind by content, not by number").
- Mark the item `[resolved-by-default]` so the learner can overrule it.

**Hardening rules for every phase (v1.2):**

1. **R0 integrity checks.**
   - Every input decodes as UTF-8.
   - Line counts match those recorded in `refactor-state.md`.
   - SHA-256 hashes are recorded.
   - Reproduce **every** C-nn in §4 with the exact command used, and record it as `reproduced` / `not reproduced` / `different`. If a conflict does not reproduce (for example, because the learner edited a file), do **not** apply its resolution blindly. Log it and ask.
2. **Tools are saved and re-runnable.** Every script (`manifest.py`, `rename.py`, `binding.py`, `dag_check.py`, `verify.py`, …) is saved under `refactor-tools/`. Each is idempotent: running it twice yields the same output. Each is delivered with the phase outputs, so any phase can be re-run in a fresh chat.
3. **Approval gate at R2.** Before writing any renamed file, deliver `id-rename-map.csv`, a dry-run diff summary (counts per file per rename), and 20 sampled before/after lines. Then **stop and wait for "approve"**. Renames are the single highest-risk operation in this refactor.
4. **Adversarial self-review at the end of every phase.** Before reporting, answer these five questions in writing, each backed by a script result:
   1. What could have been lost?
   2. Which references could now dangle?
   3. What did I author that could be mistaken for source text?
   4. What claim did I make without evidence?
   5. Which invariant is closest to being violated?
   
   Include the answers in the phase report.
5. **Stop rules.**
   - If a verification gate fails twice after fixes, stop. Report the failing items and the hypotheses, and wait. Do not weaken a check to make it pass.
   - If context is running low mid-phase, finish the current file section, update `refactor-state.md` with an exact resume point (file, section, next step), deliver what exists, and stop.
6. **Context economy.**
   - After R0, never load a whole large file again. Use `grep`/`sed` ranges and the manifest.
   - Write long outputs section by section.
   - Keep `refactor-state.md` under about 300 lines by summarising closed items.
7. **Resume protocol.** A new chat resumes from `refactor-state.md` + `refactor-tools/` + `work/` (uploaded). It first re-runs `verify.py` on `work/` to confirm the state before continuing.
8. **Tool-availability honesty.** The container's network allowlist may block tooling downloads, for example the Terraform provider registry, HashiCorp releases, the Chromium download used by mermaid-cli, and newer PostgreSQL builds. Check first. Where a tool can't be obtained, use the documented fallback (§12.2) and say so in the report. Never claim a check ran when it did not.

---

## 3. Target architecture after repair

### 3.1 File set and naming

| Canonical name | Role | Replaces references to |
|---|---|---|
| `Curriculum` (saved as `Curriculum.md`) | The only parent and roadmap spine. It owns order, cert timing, Lab Reality, and track structure. | `gcp.md`, `/Users/Suhas.KS/gcp.md`, `gcp-curriculum.md`, `unified-curriculum.md` |
| `northstar-reference-app.md` *(new, R9)* | Track N: the one running reference application, used by every file. Hosts all product-spine sections that the companions reference but no current file contains. | `gcp-curriculum.md` parts 0.4 … 11b; the cyber companion's "the reference cloud app" (36 occurrences) |
| `system-design-primer-companion.md` | System-design layer (SD/SX/P/O/Q) | — |
| `sql-databases-companion.md` | SQL, relational theory, and engine internals. Takes ownership of the DB-1…DB-10 engine slices (§4, C-05). | — |
| `design-patterns-companion.md` | OOP design theory, patterns, and architecture styles | — |
| `cloud-cybersecurity-companion.md` | Security, attacks, and cryptography | — |
| `session-progress-ledger.md` | Learner state | Regenerated in R10, following the §14 schema |
| `volatility-register.md` *(new, R4)* | Every time-sensitive claim (exam dates, product names/GA status, prices, domain weights), with the date it was last checked | — |
| `coverage-matrix.md` *(new, R4)* | Maps CS2023 knowledge areas and every cert's exam-guide domains to module IDs; the proof of completeness (§12.4) | — |
| `errata.md` *(new, R2; permanent)* | A running log of technical errors found in teaching or content, with their corrections (§12.6) | — |
| `refactor-tools/`, `inputs-original/`, `work/`, `diffs/` | Build tooling and provenance (§2) | — |

### 3.2 Track structure in `Curriculum` after R4

Existing IDs **never change**:

- A1–A11
- B1–B5
- C1–C7
- D1–D4
- Phases 0–8
- Parts I–X

New tracks get fresh letters that collide with nothing:

| Track | Content | IDs |
|---|---|---|
| **A, B, C, D** | Existing tracks, deepened in place (§9.2.2) | unchanged |
| **M** — Mathematical Foundations (undergraduate depth) | Discrete math & proof; linear algebra; calculus; probability & statistics; numerical methods; information & queueing theory | M1–M6 |
| **U** — Undergraduate CS Core | Computer architecture & systems programming; algorithms (rigorous); theory of computation; programming languages; concurrency & parallelism; software engineering & testing; professional practice & ethics | U1–U7 |
| **S** — System Architecture Design Studio | Requirements & quality attributes → documentation/ADRs → capacity → reliability → data → security → integration → migration → cost → evaluation → case studies | S1–S11 |
| **N** — Northstar reference application | Running build, milestone by milestone (file: `northstar-reference-app.md`) | N0 … N12 |

---

## 4. Conflict register — every known conflict, its evidence, and its resolution

Each entry follows the same shape:

- **Evidence:** what the files actually say.
- **Resolution:** what to change.
- **Test:** how R3 proves it is fixed.

Reproduce each one in R0 before fixing it.

### 4.A Parent-reference conflicts

**C-01 — Four different parent names.**

- **Evidence:**

  | File | Names its parent as | Occurrences |
  |---|---|---|
  | Primer companion | `gcp.md`, plus the absolute path `/Users/Suhas.KS/gcp.md` | 58 |
  | SQL companion | `gcp-curriculum.md` | 3 |
  | SQL companion | `unified-curriculum.md` (nodes `DB-SQL`, `DB-ENGINE`) | 1 |
  | Cyber companion | `gcp.md` | 32 |
  | Design-patterns companion | `Curriculum` (correct) | — |

- **Resolution:**
  - Rewrite every parent reference to `Curriculum`.
  - Delete the absolute path.
  - In the SQL companion, keep a one-line provenance note: "originally authored against `gcp-curriculum.md`; rebound to `Curriculum` + `northstar-reference-app.md` on 2026-09-xx."
- **Test:** `grep -c 'gcp\.md\|gcp-curriculum\|unified-curriculum\|/Users/'` returns 0 outside provenance notes.

**C-02 — The SQL companion is built on a different, more granular parent.**

- **Evidence:** The SQL companion's §2 stitch table, §2.1, §2.2, §2.3, and its module headers reference sections that do not exist in `Curriculum`:
  - `T.Disc`, `T.Algo`, `T.Quant`, `M.NS`, `T.SysTheory`
  - `F1`, `D1`, `D2`, `D3/D7`
  - `0.4`, `0.5`, `1.2`, `1.7`, `1.12`
  - `2.1`–`2.7`, `3.0`, `3.4`, `3.5`, `4.7`, `4.9`, `5.3`, `7.3`
  - `8.0`, `8.1`, `8.1.5`, `8.C`
  - `9.1`, `9.4`, `9b.1`, `9c.1`, `9c.2`, `9c.5`
  - `10.0`, `10.1`, `10.3`, `10.5`, `11`, `11b`, `12.S12`, `12.S13`
  - "Part 2"
  - Note that `D1`/`D2` mean *Docker/CI* there, but *Classical ML/Deep Learning* in `Curriculum`. Same ID, different meaning.
- **Resolution:** Rebind using crosswalk §6.1.
- **Test:** Every SQL stitch target resolves to an ID that exists in `Curriculum` or `northstar-reference-app.md`.

**C-03 — The cyber companion uses the same foreign numbering.**

- **Evidence:** It references numbered sections of the foreign parent, and those numbers mean the same things as in the SQL companion. For example:
  - 7.3 = data protection
  - 8.1 = primitives, tenancy, and pagination
  - 9.1 = Memorystore
  - 10.3 = FinOps
  - 2.3 = Cloud SQL backups
  
  The full list of foreign numbers it uses: 0.4, 1.2, 2.3, 3.0, 3.4, 3.x, 4.2, 4.5, 4.7, 4.8, 4.9, 4.10, 5, 5.x, 6.11, 6.13–6.16, 7.1–7.9, 8, 8.1, 9.1, 9.2, 9b, 9c, 9c.2, 10, 10.0, 10.3, "Part 2", `F1`, `D2`, `D8`, `T.SysTheory`.
- **Resolution:**
  - Numbered sections become N-track anchors: `x.y` → `Nx.y` (§6.3). The meanings stay the same.
  - Each concept module additionally gets a primary `Curriculum` anchor from crosswalk §6.2.
- **Test:** Same as C-02.

**C-04 — The cyber companion stitches "B4" for threat modeling.**

- **Evidence:** TH-02, TH-03, and PQ-S-06 stitch to `B4`. In `Curriculum`, B4 is **Cloud Economics & FinOps**. B4 was a different section in the foreign parent.
- **Resolution:** Rebind TH-* and PQ-S-06 to **A10**, plus S6 after R4. Only DOS-07 (economic DoS) stays on B4.
- **Test:** No threat-modeling module anchors to B4.

### 4.B Owner content that no file contains — must be ported so nothing is lost

**C-05 — The engine slices DB-1…DB-10 are "owned by the parent" but exist nowhere.**

- **Evidence:** The SQL companion's §2.1 and §2.2 say the parent owns these toys:

  | Slice | Toy |
  |---|---|
  | DB-1 | bag relations + truth tables |
  | DB-4 | slotted page |
  | DB-5 | clock sweep |
  | DB-6 | B-tree + inverted index |
  | DB-7 | iterators + forced spill |
  | DB-8 | histogram + MCV |
  | DB-9 | visibility simulator + deadlock detector |
  | DB-10 | mini-WAL |

  The parent also owns the Cloud SQL procedure (2.3). None of these exist in any file.
- **Resolution:**
  - Transfer ownership of DB-1…DB-10 to the SQL companion as a new §4.0 "Engine slices". Author each slice from the companion's own description (toy spec, SQL, EXPLAIN prediction, Cloud SQL mapping).
  - Put the Cloud SQL procedure in N2.3.
  - `Curriculum` A8 gets one outline bullet that points to them.
- **Test:** Every DB-n referenced anywhere is defined exactly once.

**C-06 — "8.1 primitives" are owned by the parent but missing.**

- **Evidence:** The primitives are:
  - cursor pagination (8.1.5 "owns the from-scratch pager");
  - hot partition / key histogram;
  - connection-pool math spreadsheet;
  - RLS multi-tenancy;
  - LSM vs B-tree comparison toy;
  - schema evolution;
  - idempotency.
- **Resolution:** Author these as N8.1.1–N8.1.7 in `northstar-reference-app.md`. Each primitive gets a `Curriculum` anchor:
  - A8 for pagination, RLS, schema evolution, and LSM vs B-tree;
  - A9 for hot partitions and idempotency;
  - A5/A8 recall for pool math, since SD-30 already covered the connection budget.
- **Test:** Every "8.1" and "8.1.x" reference resolves.

**C-07 — Other parent-owned sections referenced but absent.**

- **Evidence:**
  - 0.4 — HLD/LLD contract, ADR template, NFR table
  - 5.3 — ledger & consistency
  - 8.0 — building blocks
  - 8.C — evidence packs
  - 9c.1 — feature/label/leakage ownership, as-of join
  - 11 / 11b — capstones
  - 6.11 — packet-path map
  - 6.13 — edge/TLS hardening
  - 6.14 — IAP lab
  - 6.15 — VPC-SC
  - 6.16 — destroy-order checklist
  - 7.1–7.9 — security labs
- **Resolution:**
  - Recreate each one as an N-track section, reconstructed **only from what the companions say it owns**. Label it `[reconstructed from companion references — replace with original if gcp-curriculum.md / gcp.md is supplied]`.
  - 0.4's HLD/ADR/NFR contract is additionally taught conceptually in S2.
- **Test:** No dangling numbered references remain.

**C-08 — Discrete-math, numerical-stability, and systems-theory gates referenced but absent.**

- **Evidence:** The SQL companion depends on `T.Disc` (logic, sets, proofs, counting, graphs), `M.NS` (IEEE floating point), and `T.SysTheory`'s "UG gate / grad gate" items.
- **Resolution:**
  - `T.Disc` → M1
  - `M.NS` → M5
  - `T.Quant` → A1/A2 recall plus M6
  - `T.Algo` → A4 + U2
  - `T.SysTheory` → A8 + A9 (+ U5 for concurrency theory)
  
  The UG and grad gate items are kept verbatim in the SQL companion's §5, re-anchored to these modules.
- **Test:** The gate tables resolve.

### 4.C ID collisions across files

**C-09 — Same prefix, different meaning.**

- **Evidence:**

  | Prefix | Meaning in one file | Meaning in another |
  |---|---|---|
  | `DD-` | SQL: data design (DD-01…13) | Cyber: denial of service (DD-01…08) |
  | `DT-` | SQL: dialect drills (DT-1…8) | Cyber: detection/IR (DT-01…08) |
  | `PR-` | Design patterns: SOLID/GRASP (PR-01…14) | Cyber: privacy (PR-01…05) |
  | `SD-n` | SQL: schema-design cases (SD-1…6) | Primer: concepts (SD-00…39) |
  | `C1–C4` | SQL capstones | Cyber capstones — and both collide with `Curriculum` Track C modules C1–C7 |
  | `Z0.*` | SQL paper drills | Cyber paper drills |
  | `E1.1…` | SQL exercise ladder | Cyber exercise bank |
  | `T0…` tiers | Primer T0–T5 | Cyber T0–T9, and SQL uses HS/UG/grad tiers |
  | `D1`/`D2` | SQL's foreign parent: Docker/CI | `Curriculum`: Classical ML / Deep Learning |

- **Resolution:** Apply the §5 rename map.
- **Test:** A global ID registry built in R3 shows every ID defined exactly once across the suite.

### 4.D Corruption from a previous automated find-and-replace (cyber companion)

**C-10 — Tokens were mangled.**

- **Evidence:** It looks like literal substrings were replaced without word boundaries, e.g. "0.5" → "B5 IAM" and "1.4" → "A5 TLS / Phase 4 Armor". The damage:

  | Corrupted text | Location | Original |
  |---|---|---|
  | `ZB5 IAM` | heading at approx. line 1361 | `Z0.5` |
  | `E1B5 IAM` | approx. line 2453 | `E10.5`, confirmed by its E10.1…E10.8 neighbours |
  | `EA5 TLS / Phase 4 Armor` | approx. line 1398 | `E1.4`, confirmed by the E1.1–E1.3 / E2.1 sequence |
  | `gcp.md gcp.md` | doubled word | — |
  | `A10 / B5 / API auth patterns.3` | bundle 2 of §3.3.1 | — |
  | "see §B5 IAM" | §3.3 intro | — |
  | "principles principles" | Appendix V item 8 | — |
  | Appendix V numbering | skips 9 and 12 | — |
  | Edition title | line 1 says "Standalone Edition"; closing lines say "GCP-Native Edition" | — |
  | Two "End of" footers | end of file | — |

  The pseudo-anchors `A10/B5.2` … `A10/B5.10`, `A5/Phase4-Net.11…16`, `Phase4-Sec.1…9`, and `A5 TLS / Phase 4 Armor` are also partly corrupted.
- **Resolution:**
  - Restore `Z0.5`, `E1.4`, and `E10.5`, then apply the §5 renames to them.
  - Fix the prose.
  - Renumber Appendix V.
  - Use one title: **"The Cloud Cybersecurity Companion"**.
  - Keep one footer.
  - Replace every pseudo-anchor using crosswalk §6.2. **Do not** try to reverse-engineer the original numbers.
  - Then scan all five files for the same corruption signature: a digit-dot pattern glued to letters, as in `[A-Z][0-9]+[A-Z]` inside IDs.
- **Test:** A regex scan for mangled IDs returns 0.

**C-11 — Nine checkpoint IDs don't exist.**

- **Evidence:** The cyber §2 stitch table uses `E-NT1`, `E-NT3`, `E-AU3`, `E-CL1`, `E-CL3`, `E-CK1`, `E-CK2`, `E-DD2`, and `E-AB1`. None is defined anywhere.
- **Resolution:** Map each one to an existing card whose subject matches the named family.
  - Candidates: `E-NT1` → the card behind NT-03/NT-04 (E4.20 / E4.21). `E-CL1` → the shared-responsibility card (old Z0.5 / Z0.8).
  - Use the card's content to decide. Record every mapping in the crosswalk.
  - Only if no card fits, author a new one (in R8, not R2) and mark the row `[pending R8]`.
- **Test:** 0 undefined references.

**C-12 — Wrong module cited for VPC-SC.**

- **Evidence:** The cyber §2 row for Phase 4 Security says "VPC-SC exfil (NT-07)". NT-07 is control placement; VPC-SC is **NT-06**.
- **Resolution:** Change it to NT-06.

### 4.E Internal contradictions about ordering and ownership

**C-13 — WA-01 (SOP/CORS) is bound to two different places.**

- **Evidence:** The cyber §2 table binds it to A5. Its own header binds it to A10.
- **Resolution:** Primary anchor A10. The A5 HTTP session gets a one-line preview through PQ-S-04. Already applied in the live session.

**C-14 — Cryptography placement contradicts itself.**

- **Evidence:** The cyber §2 table binds CR-01…13 to A10 and CR-11/12 to A5. But the §3.3.1 "recommended bundles" put CR-01…04 and CR-08…12 on "A5 TLS day".
- **Resolution:**
  - **A5 TLS session:** CR-11 and CR-12 taught at mechanism level, plus a *minimal public-key intuition bridge*: what a key pair does, what a signature proves, why DH gives a shared secret. Do not formalize.
  - **A10:** CR-01…CR-10 and CR-13 at full depth. They formalize the A5 bridge and recall it in one line.
  - Rewrite the bundle list to match.
  - Add the same rule to the primer companion's SD-35 split: transit slice at A5, the rest at A10.

**C-15 — DoS modules are bound inconsistently.**

- **Evidence:** DD-03 (L7 floods) appears in both the A5 row and an A10 header. DD-05 and DD-06 carry foreign anchors.
- **Resolution** (after the rename to `DOS-`):

  | Module | Anchor |
  |---|---|
  | DOS-01 | A5 load balancing |
  | DOS-02 | A5 DNS/UDP |
  | DOS-03 | A10 |
  | DOS-04 | Phase 4 Networking (Prop Lock) |
  | DOS-05 | A10, recalling A5 HTTP |
  | DOS-06 | A6 |
  | DOS-07 | B4 |
  | DOS-08 | A9, recalling SD-26 |

**C-16 — The design-patterns companion binds "everything" to A7 while gating ARCH-09…12 behind A9.**

- **Resolution:**
  - Split the stitch table: ARCH-01…08 → A7; ARCH-09…12 → **A9** session.
  - The C4 recall of Strangler Fig becomes valid only after A9, which is always true because C4 comes after A9.

**C-17 — "Standalone" claim vs real overlaps.**

- **Evidence:** The cyber companion says it depends on no other companion. It actually overlaps:
  - primer SD-35, SD-08, SD-10/11, SD-26, SD-29, Q22;
  - SQL SL-13, OD-04, CS-07.
- **Resolution:** Replace the claim with "self-contained content; ownership shared per the suite overlap register (`Curriculum` §0.3)". The overlap register itself is §7.

**C-18 — `Curriculum`'s own pedagogical stance conflicts with the learner's standing instruction.**

- **Evidence:**
  - A2 says "no need for proof-level rigor".
  - A4 says "not competitive-programming depth … not to implement red-black trees".
  - The ledger's standing instruction is "maintain curriculum depth and academic rigour", and the new goal is undergraduate completeness.
- **Resolution:**
  - Keep the engineering-intuition pass as **first pass**. A2 and A4 are already complete and stay complete.
  - Rewrite those caveats to say that rigorous passes follow in M1–M4 and U2.
  - Do not delete the original caveat text. Move it into a "First-pass scope" note.

### 4.F Internal defects inside `Curriculum`

**C-19 — "Track G" doesn't exist.** Part VII says AZ-104 knowledge folds into "Track G". Fix: fold it into Phase 7, via B5/C-track recall plus a named "AZ-104-equivalent" sub-block in Part VII.

**C-20 — Stale and time-bound text.**

- **Evidence:**
  - "We start with A1 … below, right now" — the course is now mid-A5.
  - ANS-C01: "once we see how our timeline looks by mid-2026".
  - The Agentic Architect beta window closes on Sept 30, 2026.
  - ANS-C01's last exam date is Dec 31, 2026.
- **Resolution:**
  - Update the progress sentence.
  - Mark every date `(verify live)`.
  - Add a dated "status as of" line.
  - **Do not assert new dates** without checking.

**C-21 — TLS is split across A5 and A10 without a rule.** Apply the C-14 split in `Curriculum`'s own text:

- A5: handshake mechanics, certificates, CAs.
- A10: cryptographic primitives underneath, formally.

**C-22 — Part V categories are used as anchors.** The primer uses "Part V Networking", "Part V Storage/DB", and so on. Part V has category labels but no IDs. Fix: give Part V's service-map categories stable IDs (V-COMP, V-STOR, V-NET, V-DATA, V-AI, V-SEC, V-OPS) and rewrite the primer anchors to use them.

### 4.G Pending items the ledger missed

**C-23 — A5 has checkpoints that the ledger doesn't list.**

- The primer's §2 lists the A5 checkpoint "P08 steps single box → DNS → Users++", plus the P08 first pass once A5 and A6 are done.
- The cyber companion's A5 checkpoints are E-NT1 → (C-11 mapping) and CR-E12.

Add all of these to the regenerated ledger (§10). C-33 narrows the P08 checkpoint to what A5 can actually support.

### 4.H System-design-primer companion — dedicated audit (v1.1)

The following findings come from a scripted comparison of the primer's §2 stitch table, its 40 SD-module headers, its §4.1 prerequisite map, its §4.3 problem gates, and its §4.5 ladder. The primer is 1,042 lines, with 77 checkboxes, **all currently unticked**. Re-run the same scripts in R0 to reproduce every finding.

**C-24 — The primer states its own bindings in three places, and they disagree.**

- **Evidence:** For **26 of the 40** SD modules, the module header's stitch list disagrees with the §2 table. For example:

  | Module | Header says | §2 table says |
  |---|---|---|
  | SD-26 (caching) | A5 | not in the A5 row |
  | SD-14 (master-slave) | A9 | A8 (via "SD-13 … SD-25") |
  | SD-02 | A2, B3 | A7 |
  | SD-29 | A7, C3 | A5 only |
  | SD-35 | A10 | A5 and C3 |
  | SD-37 | C6 | not in the C6 row |

  The §4.5 ladder is a third, different version. For example, it places SD-02 at B3 only, and it omits SD-26 and SD-35 from A5.
- **Resolution:** Build `primer-binding-table.md`. For each SD and SX ID, give exactly **one PRIMARY anchor** (the session that teaches it in full) plus any number of **SLICE** anchors (the session teaches one named ingredient) and **RECALL** anchors (a one-line reference).
  - Use the union of header, table, and ladder as the candidate set. Nothing gets dropped.
  - Choose PRIMARY so that it satisfies the §4.1 prerequisite map (C-25).
  - Then regenerate the header stitch lines, the §2 table, and §4.5 from this one table, so the three can never drift apart again.
  - Write slice notation as `SD-21[hash-table slice]@A4`, `SD-21@A8` (primary), `SD-21~C2` (recall).
- **Test:** A script confirms that the header, §2, and §4.5 all derive from the binding table and agree.

**C-25 — Many stitches place a concept earlier than the primer's own hard prerequisites allow.**

- **Evidence:** Taking each module's earliest binding and checking it against the §4.1 "must know first" column produces 23 violations. For example:
  - SD-02 at A2, although SD-01 (its hard prerequisite) is bound at A6;
  - SD-07 at A2, although SD-06 is at A9;
  - SD-14, SD-20 at A8, although SD-05/SD-06 are at A9;
  - SD-16 at A7, although SD-13 is at A8;
  - SD-19, SD-21, SD-24, SD-38 at A4, although SD-13, SD-20, SD-17, SD-23 are at A8;
  - SD-27, SD-32, SD-33 at A3;
  - SD-28 at A2;
  - SD-35 at A5, although A10 and SD-13 are prerequisites.
- **Resolution:** Most of these early bindings are really *slices*: A4 teaches the hash table *inside* SD-21, not the key-value store itself. Reclassify each early binding as SLICE, and put PRIMARY at the earliest session where the hard prerequisites are met. Where a genuine ordering gap remains, fix it by adding a named slice earlier; do not move the concept later than the learner can use it. Specific cases:
  - **C-26** covers SD-10.
  - **SD-14, SD-15, SD-17**: PRIMARY at A9. A8 gives a forward pointer only. This matches the headers and `Curriculum`'s A9 bullet "Partitioning/sharding".
  - **SD-04**: CAP is taught at A8, because `Curriculum` A8 lists "CAP theorem". The primer's hard prerequisite "A9" becomes: A8 gives the statement and intuition; A9 gives the formal limits (§9.2.2) and PACELC.
- **Test:** Topological check of the rebuilt binding table against §4.1 finds zero PRIMARY-before-prerequisite violations. Run it in R3 and R10.

**C-26 — Directly affects the live session: SD-10 (load balancer) is bound to A5, but its prerequisite chain runs through A6.**

- **Evidence:** SD-10 requires SD-02, which requires SD-01, which is bound at A6. The A5 load-balancing session is still ahead for this learner.
- **Resolution:** Add `SD-01[clones + single-box ceiling slice]@A5` and `SD-02[performance-vs-scalability slice]@A5`, taught immediately before load balancing. SD-01 and SD-02 stay PRIMARY at A6/B3; those later sessions recall the slice and complete it.
- **Test:** Ledger §4's remaining-A5 list shows both slices before SD-10.

**C-27 — SD-26 (caching) is bound to A5 by its header, but needs SD-21 (A8).**

- **Resolution:** `SD-26[HTTP-layer caching slice: client/browser cache, Cache-Control/ETag, CDN-as-cache, reverse-proxy cache]@A5`, placed inside the HTTP and CDN sessions. Application- and database-level caching, query-level vs object-level caching, and SD-27 update strategies go PRIMARY at A8/A9, after SD-21. C3 recalls the NGINX/Varnish cache.

**C-28 — SD-35 (security basics) overlaps about eight cyber modules and uses Prop-Locked controls as props.**

- **Evidence:**
  - SD-35's GCP lens names VPC Service Controls, CMEK, Cloud Armor WAF rules, mTLS, and Web Security Scanner. These are the territory of cyber NT-06, CR-14, WA-11, CR-17, and WA-02.
  - Its lab (Python + SQLite string-concatenated vs parameterized login query) duplicates cyber WA-05 and SQL SL-13.
  - Cyber's Prop Lock forbids treating VPC-SC or CMEK as known props before Phase 4 Security.
- **Resolution:** SD-35 becomes an **index module**. Keep every one of its bullets verbatim, and append a "Taught by" pointer to each clause:

  | SD-35 clause | Taught by |
  |---|---|
  | in transit | A5 TLS, CR-11/12 |
  | at rest | CR-14 @ Phase 4 |
  | XSS | WA-02 @ A10 |
  | SQLi / parameterized queries | SL-13 (mechanics) + WA-05 (attacker model) |
  | least privilege | B5 + CL-03 |
  | network hardening from P08 | NT-01, NT-05, NT-07 @ A5 |

  - Mark its lab as **"shared lab — run once as WA-05/SL-13; SD-35 recalls it"**. Keep the lab text; do not delete it.
  - Put a Prop Lock note on the GCP-lens sentence: Lens-1 naming only before Phase 4.
  - Its Check question (credential *replay* in P04) is owned by cyber CR-17/PV-03 as mechanism, and SD-35 keeps the question.

**C-29 — Three "Numbers"/session protocols collide when several companions bind to one module.**

- **Evidence:** The primer §0.3, SQL §0.3, and cyber §0.3 each define a 7-step session and each requires "one numbers step" and "one micro-problem/exercise". A5 alone binds primer and cyber modules, and A8 binds primer, SQL, and cyber.
- **Resolution:** `Curriculum` §0.4 gets a **Suite Session Protocol**:
  1. **Anchor** — list the bound IDs from *all* companions.
  2. **Concept** — taught once, by the owner in §7.
  3. **Layers**, in fixed order: system design (primer) → SQL/engine → patterns → attacker/crypto (cyber).
  4. **GCP lens.**
  5. **One Numbers step**, for the whole session.
  6. **One application item**: either a primer micro-problem or a companion exercise card, never both for the same concept. This honours primer rule 5 and cyber "one card at a time".
  7. **Checks**, woven in per ledger §5.
  8. **Close**, ticking boxes in every file.
  
  Each companion keeps its own §0.3 text, with an added pointer: "When other companions bind to the same session, the Suite Session Protocol in `Curriculum` §0.4 governs."

**C-30 — Primer rule 6 ("Do **not** create a separate tracker, log, or research file") conflicts with the ledger and with this refactor's working files.**

- **Resolution:** Amend rule 6, keeping its original text and adding: "Exception: `session-progress-ledger.md` is the single sanctioned cross-file tracker; inline `- [ ]` ticks remain authoritative and the ledger mirrors them. Refactor artifacts (`refactor-state.md`, manifests, reports) are build tooling, not trackers, and are not uploaded to teaching sessions."

**C-31 — Primer rule 9 ("do not copy its contents into other files") conflicts with Tracks S and N, which reuse primer material.**

- **Resolution:** Keep the rule and enforce it. Track S, Track N, and `Curriculum` **reference primer IDs** (SD-00, SX-12, P08, TF-1…TF-7). They never paste primer text. The §8.2 diff adds a check: no primer paragraph longer than 20 words appears outside the primer file.

**C-32 — Two "spines": primer P08 ("the spine") and Northstar (the product spine).**

- **Resolution:** They do different jobs, and both are kept:
  - **P08** is the *scaling-evolution script*: a problem card, run in two passes.
  - **Northstar** is the *concrete running build*.
  
  In `northstar-reference-app.md`, every N-milestone that changes the deployed architecture must cite the P08 ladder step it realizes (Single box, Users+, …, Users+++++). It reuses the matching Terraform exercise, TF-1…TF-7, by ID rather than writing a new one. P08's Phase 6–7 re-runs (AWS/Azure) stay primer-owned.

**C-33 — Three different timings for P08's first pass.**

- **Evidence:**
  - §2 puts the A5 checkpoint at "P08 steps single box → DNS → Users++".
  - §2 also puts "P08 step 0" at A6.
  - §4.5 says "P08 first pass (outline, once A5/A6 are done)".
  - Primer rule 5 says a problem introduces at most one new concept, yet Users++ introduces SD-10, SD-06, SD-12, SD-09, and SD-11, and SD-06 and SD-12 are not available until A9/A7.
- **Resolution:**
  - **A5 checkpoint** = P08 *Single box* step (SD-08 plus the P08 network hardening, now pointing to NT-01/NT-05), plus the *networking slice* of Users++ (SD-09, SD-10, SD-11). SD-06 and SD-12 are **named but not taught**, and marked "→ A9 / A7".
  - **A6** = P08 step 0 (the single-box OS view).
  - **Full first pass (outline)** comes after A6.
  - **Second pass** comes after Phase 3.
  
  Update the §2 table, §4.3, §4.5, and the P08 card's checkbox labels to match.

**C-34 — O-problems have conflicting gates, and now overlap the design-patterns companion.**

- **Evidence:**
  - §2 puts the A7 checkpoint at O03.
  - §4.3 and §4.5 gate O03, O04, and O05 at A3/A4.
  - O03's stated patterns (chain of responsibility, state) are design-patterns DP-18 and the State pattern, which are taught at A7.
  - A3 and A4 are complete, and no O-problem is ticked.
- **Resolution:**
  - O01, O02, O07 become **A4 recall checkpoints (pending)**. They exercise A4 data structures the learner already has, so they are run as practice, not re-teaching.
  - O03, O04, O05, O06 move to **A7 checkpoints**, after the relevant design-patterns modules. O03 comes after DP-18 and State. O04 and O05 come after F-01…04 and SOLID.
  - Record the primer's "defects to find" lists as design-patterns AP-* (anti-pattern) practice via cross-reference only.

**C-35 — SX techniques: "taught with the first problem that needs them" (§4.1) vs early stitches in §2.**

- **Evidence:** §2 stitches SX-02 at A2/A3, and SX-07, SX-09, SX-10, and SX-11 at A4.
- **Resolution:** Apply the same PRIMARY/SLICE split as C-24. The SX technique is PRIMARY at its first problem. The A2/A3/A4 bindings are slices of the underlying math or data structure, e.g. `SX-02[62^7 key-space math]@A2`.

**C-36 — Overlaps between the primer's own additions and the new tracks and other companions.**

- **Evidence:** Primer §7.1 labels PACELC, cache stampede, tail latency/hedging, CRDTs, and top-k sketches as "my addition". Little's law lives in SD-03/SD-28. Q-cards overlap U2 (sketches, approximate counting), U4 (Q21 garbage collection), A9 deepening (Q04 CRDTs, Q05 vector clocks), ARCH-10 (Q23 event sourcing), cyber AB-01 (Q22), and cyber CR-13/CR-17 (P04 credential storage).
- **Resolution:** Add the §7 rows marked "(v1.1)". The primer keeps its text; its additions become the *design-decision layer*, and the new owners hold the theory.

**C-37 — SQL uses "SD-1 … SD-6" for schema-design cases *and* cites primer IDs ("recall primer SD-13 … SD-19", SD-27, SD-37) in the same file.**

- **Evidence:** The SQL file contains single-digit schema cases SD-1 to SD-6 (35 occurrences), one bare "SD-" from a range, and two-digit primer references SD-13, SD-14, SD-17, SD-18, SD-19, SD-27, SD-37.
- **Resolution:** The §5 rename of SQL `SD-n` → `SCH-n` must use the disambiguating regex in §5. A naive `SD-1` replacement would corrupt `SD-13`. Also fix the bare `SD-` range token.
- **Test:** After the rename, every remaining `SD-` in the SQL file is two-digit and resolves to a primer module.

**C-38 — Sub-IDs `SD-38a`, `SD-38b`, `SD-38c` and slice notation.**

- **Resolution:** The ID regexes in §5 and §8 must accept a lowercase suffix: `SD-\d{2}[a-c]?`. `SD-38a/b/c` are registered as defined *within* SD-38; they are not orphans.

**C-39 — `gcp.md`-labelled nodes in the §4.1 mermaid diagram and in the tier tables.**

- **Evidence:**
  - Node labels "gcp A1", "gcp A5", "gcp A8", "gcp A9".
  - §4.2 column "gcp.md modules complete".
  - §4.3 column "gcp.md gate".
  - SD-25's anchor "gcp.md Cloud Database Engineer domain".
  - The §0.4 notation line.
  - `Part V` categories used as anchors.
- **Resolution:**
  - Relabel to "Curriculum A1" and so on.
  - Rename the columns to "Curriculum gate".
  - SD-25 → Part V cert row 8 (Cloud Database Engineer).
  - `Part V — X` → the V-IDs from C-22: V-COMP, V-STOR, V-NET, V-DATA, V-AI, V-SEC, V-OPS.
  - Keep the diagram rendering. After editing, validate the mermaid syntax with a parser: `npx @mermaid-js/mermaid-cli`, or at minimum a bracket/arrow lint.

**C-40 — The primer's GCP details come from a January 2026 knowledge cutoff (primer §7.1), not from live docs.**

- **Resolution:** Keep every `verify` flag. In R5, any product name the primer flags as uncertain gets a dated "status to verify" line; do not assert changes without a live check. The list includes Spanner Graph, Memorystore for Valkey, Managed Service for Apache Kafka, Firestore MongoDB compatibility, managed connection pooling, and Vertex AI Search for commerce.

**C-41 — Primer §7.3 is a maintenance rule this refactor triggers: "When gcp.md changes … update §2 stitch table and §4.5 ladder first."**

- **Resolution:** Honour it. The C-24 binding table regenerates §2 and §4.5. The concept modules and problem cards change only through ID renames, anchor rewrites, and appended "Taught by" / "Prop Lock" notes. Their primer text is untouched.

**C-42 — Primer ticks vs the ledger.**

- **Evidence:** All 77 primer boxes are unticked. The ledger nevertheless records that primer content was taught:
  - §4: "SD-30/SD-31 … SD-08" folded into A5;
  - A1 covered KiB vs KB, which is SD-36's core;
  - A4 covered hash maps, BSTs, and graphs, which are slices of SD-21, SD-19, and SX-10.
  
  Other A1–A4 primer stitches have no evidence either way: SD-37, SD-00, SD-03, SD-07, SX-02, Little's law, SX-11, SD-38a ring, and the O01/O02/O07 checkpoints.
- **Resolution:**
  - Tick SD-08, SD-30, and SD-31 (ledger-confirmed).
  - Record the slices SD-36[prefix slice]@A1, SD-21[hash-table slice]@A4, SD-19[B-tree slice]@A4, and SX-10[BFS slice]@A4 as done.
  - List everything else as **"unverified — run the module's Check question as a recall check at the next natural point; tick on a correct answer, teach only the gap on a miss."** Never re-teach completed material wholesale; ledger §3 invariant.

**C-43 — The SD-08 restart gap in the current chat.**

- **Evidence:** On the learner's request, DNS was restarted in this chat. The restart re-covered hierarchy, resolution, TTL/caching, record types, and DNS-as-SPOF. It did **not** re-cover SD-08's GCP lens: Cloud DNS routing policies (weighted round robin, geolocation, failover), anycast global LB replacing DNS latency routing, Service Directory, and the `dig +trace` lab. The earlier session did cover them, per ledger §4.
- **Resolution:** Keep SD-08 ticked on the ledger's evidence. Add a one-line recall item, "SD-08 GCP lens + `dig +trace` lab", to the start of the HTTP session.

### 4.I `Curriculum` — line-level audit (v1.2)

**C-44 — The certification count contradicts itself.**

- **Evidence:** §0 says "Fifteen professional-tier certifications", and "fifteen certs" appears again under "Why this order". But Parts V–VII list **18**: 10 GCP, 5 AWS, and 3 Azure. Phase 5 also says "pick 2–4 … not all 8": after PCA and PMLE, 8 GCP certs remain only if Agentic Architect is counted, yet Agentic Architect is scheduled separately in Phase 8.
- **Resolution:** Do not guess which count the learner intended. Log it as an **Open question** for the learner, with both numbers shown. Until they answer, change the prose to "the certifications listed in Parts V–VII (18 as currently listed)" and correct "not all 8" to "not all 7; Agentic Architect is Phase 8". Record both edits in CHANGELOG as corrections, with the counting evidence.

**C-45 — There are no inline tracking boxes, but every companion tracks inline.**

- **Resolution:** Add one `- [ ]` per module (A1–A11, B1–B5, C1–C7, D1–D4, M/U/S/N modules, and Part V cert rows). Tick them from ledger evidence: A1–A4 ticked, A5 in progress. The ledger (§14) mirrors the boxes; the boxes are authoritative.

**C-46 — No Lab Reality for Track D, and none for most per-cert entries.**

- **Resolution:** Append Lab Reality notes for D1–D4 (local notebooks, free-tier Vertex AI where available `(verify)`, `[plan-only]` for large training) and for each cert row. This is append-only.

**C-47 — `Curriculum` has no teaching protocol beyond Part X.**

- **Evidence:** The companions each assume a parent teaching protocol:
  - SQL's "universal ten-rung sequence", "pre-rung-2 self-check", "Teaching contract → Learner state", "Lab safety", and "Database protocol";
  - the cyber companion's "Predict → attempt → discrepancy → ledger".
  
  None of these exist in `Curriculum`.
- **Resolution:** Add the **Suite Teaching Contract** (§13) as `Curriculum` §0.4, absorbing the C-29 Suite Session Protocol. Add **Lab Safety** as `Curriculum` §0.5, unifying cyber rule 10, SQL rule 10, and `Curriculum` §0's Lab Reality.

**C-48 — Stale framing in Part IX and the phase plan.** Beyond C-20: add an "as of" date to Part IX, and move every date-bearing line into `volatility-register.md` with a last-checked date.

**C-49 — A7 is overloaded.**

- **Evidence:** After the refactor, A7 binds:
  - `Curriculum` A7 itself;
  - all 63 design-patterns items (minus ARCH-09…12);
  - primer SD-12, SD-28, SD-32–SD-34, and O03–O06 checkpoints;
  - cyber TH-04, AU-05…07, AU-11…13, and AB-01…08;
  - Track S1 and S2;
  - Northstar N0.
  
  That is several dozen concepts in one module.
- **Resolution:** Split A7 into ordered **teaching blocks** A7.1…A7.n. These are sessions, not new modules, and the module ID A7 stays unchanged. Suggested order:
  1. Client-server and API styles (+ SD-32…34)
  2. Async and queues (+ SD-28)
  3. OOP foundations + SOLID
  4. GRASP + creational patterns
  5. Structural patterns
  6. Behavioral patterns
  7. Architecture styles + DDD
  8. API authentication/authorization + attacks
  9. Abuse and rate limits
  10. S1–S2
  11. N0
  12. Checkpoints
  
  Apply the same splitting rule to any module whose bound-concept count exceeds 20 (A5, A8, and A10 are likely), using the §13.7 pacing budget.

### 4.J SQL companion — line-level audit (v1.2)

**C-50 — The lab kit that produces the goldens is not in any file.**

- **Evidence:** SQL §3.1 says the sources live "on this box" at `sql-companion-work/`: `lab_schema.sql`, `lab_seed.sql`, `run_ex.py`, `plans.py`, `tx_tests.py`, `two.py`, `wrongs.py`, `goldens_wrong.json`, `naive.sql`/`safe.sql`, and `slow_bad.sql`/`slow_good.sql`. None of these is present. The file has 186 code-fence lines, but these are exercise keys, not the kit. **The goldens therefore cannot currently be reproduced.**
- **Resolution (R6):**
  1. Rebuild the kit as a new appendix plus files in `work/sql-lab-kit/`, from §3.3 (schema), §3.4 (the deterministic seed rule: "every value a pure function of ids", no `random()`), and the documented distributions (5 tenants, 2,000 users, 500 SKUs, 20,000 orders, user 1 hot, users 1801–2000 never order, and so on).
  2. Execute every Appendix K key against the rebuilt seed and compare fingerprints with the recorded goldens.
  3. **If they match:** mark the kit `verified`.
  4. **If they don't:** do **not** edit the goldens (invariant 6). Mark each mismatch `golden-unreproduced`. Record both values and a diagnosis (seed drift, PostgreSQL version, collation, timezone), and list it in `errata.md`. The learner is told that the kit is reconstructed.
  5. Install PostgreSQL 15.x if the environment permits. If only another major version is available, run there, record the version, and treat plan-shape (PX) differences as expected rather than as errors.
- **Test:** Kit files exist; `run_ex.py` executes every key; a match/mismatch report is delivered.

**C-51 — "E11" and "E12" are declared as labs in §7, and E12.1 is referenced, but E12.1 is never defined.**

- **Evidence:** §0.4 says E11 and E12 are labs in §7. §7 defines PX-n and TX-n, not E11.x or E12.x. Line ~1331 references E12.1 (a missing-index seq scan per user), which reads like a PX card.
- **Resolution:** Map E11 → the PX family and E12 → the TX family (or the reverse) according to their content. Rewrite E12.1 to the specific PX/TX card it describes. If no card fits, author one in R6 and mark it `[pending R6]`. Record everything in the crosswalk.

**C-52 — The runner table calls the plan catalogue "P1–P11".**

- **Evidence:** Everywhere else the plan cards are PX-1…PX-11. "P1–P11" is also confusable with primer P01–P08.
- **Resolution:** Rename it to `PX-1…PX-11`.

**C-53 — More parent-owned references that are not covered by §6.1.**

- **Evidence:** `G4`, `G12b`, `F1…F4`, `D0…D8`, `TB-…`/`SRC-…` source IDs (from `unified-curriculum.md`), "gcp-curriculum Lab safety", "Database protocol", and "Teaching contract → Learner state".
- **Resolution:**

  | Reference | New anchor |
  |---|---|
  | `G4` (WAL/replica/PITR) | N2.3 + DB-10 |
  | `G12b` | N-stub, or by content if it can be determined |
  | `F1…F4` | A3/A6/A11 by content |
  | `D0…D8` | C1–C5 by content |
  | `TB-`/`SRC-` IDs | an explicit bibliography in SQL §Sources, keeping the IDs as labels |
  | Lab safety | `Curriculum` §0.5 |
  | Database protocol | the predict→run→discrepancy rule in §13 |
  | Teaching contract → Learner state | the §14 ledger |

**C-54 — The "ten-rung ramp" is a parent-owned pedagogy that is referenced but absent.**

- **Evidence:** SQL rule 3 names the rungs: anchor → vocabulary → representation → core move → worked illustration → basic unseen check → routine variation → mixed transfer → top-rung challenge → reflect.
- **Resolution:** Import it into the Suite Teaching Contract (§13.2) as the canonical progression for **exercises**, reconciled with the one-concept-per-turn rhythm.

**C-55 — Anchoring rules exist in SQL only.**

- **Evidence:** SQL has a "pre-rung-2 self-check" (every term used must already be anchored; no unanchored sibling; no new product). It also has the rule that "an unseen check that uses unanchored terms is invalid — fix the check, don't mark the learner shaky".
- **Resolution:** Promote both suite-wide (§13.4). This generalises the cyber companion's Prop Lock.

**C-56 — Goldens depend on environment pins stated only in SQL rule 7:** seed v1, PostgreSQL 15.x, `timezone = UTC`, and `C` collation. Copy these pins into the kit's README and into `run_ex.py` as asserted preconditions. The runner must refuse to fingerprint if a pin is violated.

**C-57 — SQL rule 8 names the parent's ledger ("Teaching contract → Learner state") as the tracker.** Rebind it to `session-progress-ledger.md` per §14, keeping the rule text plus a pointer.

### 4.K Design-patterns companion — line-level audit (v1.2)

**C-58 — Almost no inline tracking.** The file has only **one** `- [ ]` box for 63 items, even though its rule 6 says tracking is inline. Add one box per item (F, PR, DP, ARCH, AP).

**C-59 — Ten architecture modules have no Check question.**

- **Evidence:** ARCH-01, 02, 03, 05, 06, 07, 08, 09, 10, and 11 have none. The nine GRASP items share one Check, and the ten anti-patterns share one.
- **Resolution (R7):** Author one Check per item, following §13.5's rules. Keep the existing shared Checks as "integration checks".

**C-60 — The file contradicts itself about quoting GoF.**

- **Evidence:** §6's format line says "**Intent** (GoF's own line)". §11 says the Intent lines are "close paraphrases". Rule 7 says `(GoF)` marks text "quoted/adapted directly", but the tag is used only twice.
- **Resolution:** Correct §6's format line to "Intent (paraphrased from GoF)". Audit all 23 Intent lines: any line that reproduces the book's wording beyond a short phrase is re-paraphrased (invariant 8). Keep `(GoF)` only where a short attributed quote is actually retained.

**C-61 — Rule 4 requires a *real* industry example for every pattern, but some examples are toy classes.**

- **Evidence:** DP-02's "real-world example" is `DocumentCreator`/`PDFCreator`, a textbook illustration rather than a named library or SDK.
- **Resolution:** In R7, audit all 23 patterns. Any toy example gets an additional **named** real example (a standard-library API, cloud SDK, or framework the suite uses), marked `(verify)` if version-specific. The toy stays as a teaching illustration.

**C-62 — Repository is defined twice.** ARCH-06 (DDD) and ARCH-07 (PoEAA) both define Repository, and PR-12 mentions it as well. The owner is ARCH-07's definition (Fowler); ARCH-06 recalls it in one line plus its DDD-specific constraint (one repository per aggregate root). Keep both texts and add the pointer.

**C-63 — The GoF category tags `[C]`, `[S]`, `[B]` collide with Track C, the new Track S, and Track B.** Rename them to `[Cr]`, `[St]`, `[Bh]` within this file only.

**C-64 — Notation (§0.4) omits `F-nn`, and the file lacks everything the suite standard requires:** GCP lens, labs, exercise bank, keys, and skip-tests.

- **Resolution:** Fix the notation line. In R7, bring the file to parity (§9.3.3 plus §9.1):
  - Lens-1 per pattern, naming a GCP SDK or service where the pattern appears;
  - one `[local]` Python kata per pattern, with an executable test;
  - an exercise bank with an after-attempt-only Appendix K;
  - a skip-test per section.

**C-65 — The dependency gate is local to this file.** Merge §10's order into the global prerequisite DAG (§12.5) so that cross-file gates are checked by script. Examples: ARCH-09…12 need A9; ARCH-11 relates to SQL CS-07; DP-14 relates to SD-28.

### 4.L Ledger, pedagogy, and teaching-method audit (v1.2)

**C-66 — The ledger is free text.** It cannot be diffed or checked mechanically. Adopt the §14 schema.

**C-67 — Teaching errors in this chat that any hardening must prevent from recurring.** Log both in `errata.md` as the first entries.

1. An exercise said a load-balancer **IP** sat behind a **CNAME**. CNAMEs point to names, and IPs sit behind A records. Discovered and corrected in the same chat.
2. The DNS restart omitted SD-08's GCP lens (C-43).

These motivate the exercise pre-flight (§13.6) and the stitch-completeness check at session close (§13.9).

**C-68 — Known learner error pattern not yet operationalised.** The ledger records it: errors sit at the terminology/precision layer, not the logic layer. For example: "call stack" misnamed, "centered" instead of the actual variance mechanism, "power of 9" (host-bit count confused with prefix length), and "returned to the OS by the authoritative server" (resolver role).

- **Resolution:** Seed the **misconception register** (§13.3) with these items, and have checks deliberately probe the precision layer.

**C-69 — The "one question per turn" rhythm conflicts with multi-part checks used in practice.** Some checks in this chat asked two things at once (e.g., "which record type … and why would a CNAME at the apex …").

- **Resolution:** §13.5 rule: one focused question per turn. A multi-part check is split across turns, or reduced to its single most diagnostic part.

**C-70 — `learn-SKILL.md` conflicts with ledger §5.**

- **Evidence:** The skill says to diagnose before teaching with one calibrating question, and to keep turns to "a few sentences". Ledger §5 says there is to be no background probing, and depth is not to be compressed.
- **Resolution:** Ledger §5 wins, by invariant 13 rung 2. Diagnosis happens *through* the embedded check. Turns may be as long as one concept needs at full depth, but still carry exactly one question. The skill's other rules stand, including holding the line under pushback, no false praise, and "know when you're done". Record this in §13.1.

**C-71 — No mastery model.** "Done" currently means "taught and answered once". There is no state for shaky, unverified, or needs-spaced-recall.

- **Resolution:** §13.3 mastery states.

**C-72 — No session-close protocol for carrying state.** The tutor cannot edit project files between chats; the learner has to re-upload.

- **Resolution:** §13.9. Every session ends with a ledger **delta block** (§14 format) that the learner can paste or merge, and every Nth session (N = 5, or when asked) with a full regenerated ledger file.

**C-73 — Stitch completeness isn't checked when a session closes.** This is how C-43 happened.

- **Resolution:** §13.9 requires listing every ID bound to the session (from the binding tables) and marking each one taught, sliced, deferred-with-reason, or recalled. An ID left unmarked blocks the close.

**C-74 — No accuracy standard for the tutor's own explanations.**

- **Resolution:** §12.1 and §13.6. The tutor must be precise about mechanisms, flag uncertainty explicitly, and log errors in `errata.md` when found.

**C-75 — The companions' own "user can override" rules are uncoordinated.** Unify them into one rule in the Suite Teaching Contract (§13.1): the learner may skip (after passing the skip-test), jump, or go hands-on. Overrides are recorded in the ledger so the DAG check can flag any prerequisite that was skipped.

---

## 5. ID rename map (apply mechanically in R2, emit `id-rename-map.csv`)

**Principle:** Concept families keep short codes but must be unique across the suite. Exercises, drills, tiers, and capstones get file-qualified prefixes. When a collision occurs, rename the side with fewer external references. Never renumber within a family.

| Old | File | New | Reason |
|---|---|---|---|
| `DD-01…08` (denial of service) | cyber | `DOS-01…08` | Collides with SQL data design |
| `DT-01…08` (detection/IR) | cyber | `IR-01…08` | Collides with SQL dialect drills |
| `PR-01…05` (privacy) | cyber | `PV-01…05` | Collides with design-patterns SOLID/GRASP |
| `SD-1…6` (schema-design cases) | SQL | `SCH-1…6` | Collides with primer SD-nn |
| `C1–C4` (capstones) | SQL | `SQL-CAP1…4` | Collides with cyber capstones and `Curriculum` C-track |
| `C1–C4` (capstones) | cyber | `SEC-CAP1…4` | Same |
| `Z0.*` | SQL | `SQL-Z0.*` | Collides with cyber |
| `Z0.*` | cyber | `SEC-Z0.*` | Collides with SQL |
| `E<level>.<n>` | SQL | `SQL-E<level>.<n>` | Collides with cyber |
| `E<level>.<n>` | cyber | `SEC-E<level>.<n>` | Collides with SQL |
| `CR-E*` | cyber | unchanged | Unique |
| Tiers `T0–T5` | primer | `SDP-T0…T5` | Tier collision |
| Tiers `T0–T9` | cyber | `SEC-T0…T9` | Same |
| Tiers HS/UG/grad and `12.S12` / `12.S13` | SQL | `SQL-T-HS`, `SQL-T-UG`, `SQL-T-GR`; skip-tests `SQL-SKIP-SQL`, `SQL-SKIP-ENGINE` | Removes the foreign parent numbering |
| `F-01…04`, `PR-01…14`, `DP-01…23`, `ARCH-01…12`, `AP-01…10` | design patterns | unchanged | Unique once cyber PR → PV |
| SD, SX, P, O, Q, TF-1…7 | primer | unchanged | Unique |
| PQ, RT, SL, CS, DD (data design), OD, AN, TD, PX, TX, BH, DT (dialect), TF-DB | SQL | unchanged | Unique once the cyber side is renamed |

**Rules for applying the renames:**

- Rewrite references everywhere they appear: text, tables, Appendix K, bundle lists, and the ledger.
- Use word-boundary regexes.
- Process longest IDs first, so that `DD-01` never clobbers `DD-010`.
- Run the rename in a dry-run mode first and diff it before writing.

**Additional renames (v1.2):**

| Old | File | New | Reason |
|---|---|---|---|
| `[C]`, `[S]`, `[B]` (GoF categories) | design patterns | `[Cr]`, `[St]`, `[Bh]` | Collides with Tracks C, S, B (C-63) |
| "P1–P11" (runner table) | SQL | `PX-1…PX-11` | Inconsistent with PX cards; confusable with primer P01–P08 (C-52) |
| `E11.x` / `E12.x` | SQL | the PX/TX IDs per C-51 | Undefined IDs |

**Primer-specific rename rules (v1.1):**

- **SQL `SD-n` → `SCH-n` (C-37).** Apply **only inside `sql-databases-companion.md`**, with the pattern `(?<![\w-])SD-([1-6])(?![\d\w])`. It matches single-digit SD-1 … SD-6 and never touches two-digit primer references such as SD-13 or SD-37.
  - Fix the bare range token (`SD-1…SD-6` / `SD-` fragments) by hand-reviewed diff.
  - Then assert that every remaining `SD-` in that file matches `SD-\d{2}[a-c]?` and is defined in the primer.
- **Primer tier references.** Rewrite `T0`–`T5` to `SDP-T0`–`SDP-T5` **only** in:
  - primer §4.2 (tier definitions);
  - primer §4.3 (the "Tier" column);
  - the P08 card ("T1 outline; T5 capstone");
  - any cross-file reference to primer tiers.
  
  Do not touch `T` tokens that are not tiers. Examples: `TF-1`, `TX-`, `TD-`, `TH-`, and the SQL foreign labels `T.Disc` and `T.Algo`, which are crosswalked, not renamed. Use the pattern `(?<![\w.-])T([0-5])(?![\w.])` restricted to those line ranges, and review the diff.
- **ID regex must include:**
  - SD sub-IDs `SD-\d{2}[a-c]?`;
  - slice notation `ID[...]@Anchor` and recall notation `ID~Anchor`, introduced in C-24;
  - O, P, and Q IDs as `\b[OPQ]\d{2}\b`. Guard these against false positives such as the cert name "PCA" and phase names.
- **Primer IDs that stay unchanged:** SD-00…SD-39 (+a/b/c), SX-01…SX-13, P01…P08, O01…O07, Q01…Q23, and TF-1…TF-7. Track S's `S1…S11` does not collide with `SX-nn`: always write S-modules without a hyphen and SX with a hyphen, and assert this in R3.

---

## 6. Crosswalks

**Default rule for anything not listed below: bind by content, not by number.** Read the module's title and body, find the `Curriculum` section whose topic list contains that concept, and anchor it there.

### 6.1 SQL companion: foreign label → new anchor

| Foreign label | New anchor |
|---|---|
| T.Disc | **M1** |
| T.Algo | A4 (recall) + **U2** |
| T.Quant | A1/A2 recall + **M6** |
| M.NS | **M5** |
| T.SysTheory (DB theory) | **A8** + **A9** (+ U5) |
| F1 | A3 + A6 |
| D1 / "1.2 container contract" | **C1** |
| D2 | **C4** |
| D3/D7 | C4 + **C5** |
| 0.4 (HLD/LLD, ADR, NFR) | **S2** + N0.4 |
| 0.5 IAM | **B5** |
| 2.3 IAM DB auth | N2.3 |
| 1.7 | **C6** |
| 1.12 | **B3** |
| 2.1 SQL design track | **A8** + SQL §4.0 engine slices (C-05) |
| 2.2 | A8 + V-STOR |
| 2.3 | N2.3 |
| 2.4 | A8 (NoSQL) + N2.4 |
| 2.5 | N2.5 |
| 2.6 | A8 + C4 + N2.6 |
| 2.7 | A9 + V-STOR + N2.7 |
| 3.0 | **A7** + design-patterns companion (Repository, Unit of Work) |
| 3.4 | A7 |
| 3.5 | **A9** + design-patterns ARCH-11 |
| 4.7 | A10 + B5 |
| 4.9 | C1 + Phase 4 Security |
| 5.3 | A8 + N5.3 |
| 7.3 | Phase 4 Security + N7.3 |
| 8.0 / 8.C | S-track + N8.0 / N8.C |
| 8.1 / 8.1.5 | N8.1.x (C-06) |
| 9.1 | V-STOR + N9.1 |
| 9.4 | V-STOR + N9.4 |
| 9b.1 | V-DATA + N9b.1 |
| 9c.1 | **D3** + N9c.1 |
| 9c.2 / 9c.5 | **D4** + N9c.2 / N9c.5 |
| 10.0 / 10.5 | C6 |
| 10.1 | C7 |
| 10.3 | B4 |
| 11 | N11 |
| 11b | N11b |
| 12.S12 / 12.S13 | A8 skip-tests (§5 renames) |
| PCA / PDE / PCDE rows | Part V cert rows |

### 6.2 Cyber companion concept modules → primary `Curriculum` anchor (secondary anchors after the ·)

For each module, keep the original foreign anchor in a `Provenance:` field translated to N-form. Delete the corrupted pseudo-anchors.

| Modules | Primary anchor · secondary |
|---|---|
| PQ-S-01 | A10 (gate for CR-01) · A1 recall |
| PQ-S-02 | A10 |
| PQ-S-05 | A10 |
| PQ-S-03 | B1 |
| PQ-S-04 | A5 HTTP/TLS (preview) · A10 |
| PQ-S-06 | A10 |
| TH-01…03 | A10 · S6 |
| TH-04 | A7 · A10 |
| TH-05 | Phase 4 Security (SecOps) |
| TH-06 | A9 |
| CR-01…10, CR-13 | A10 (the CR-11/12 bridge per C-14) |
| CR-11, CR-12 | A5 TLS · A10 |
| CR-19 | A10, after CR-11/12 |
| CR-14, CR-15, CR-17, CR-18, CR-20 | Phase 4 Security · N7.x |
| CR-16 | A10 · SC-01 |
| AU-01…04 | A10 · A5 HTTP cookie mechanics (recall) |
| AU-05…07 | A7 · A10 federation/SSO |
| AU-08…10 | A10 (MFA) |
| AU-11…13 | A7 (API AuthZ) · A10 |
| AU-14 | B5 |
| AB-01…05 | A7 · V-NET (Armor, Lens-3) |
| AB-06…08 | A7 · B4 |
| DOS-01…08 | per C-15 |
| WA-01…04, WA-06…08, WA-12 | A10 |
| WA-05 | A10 · A8 (SQL SL-13 owns the SQL mechanics, §7) |
| WA-09 | C6 |
| WA-10 | A6 + U1 · A10 |
| WA-11 | V-NET (Armor) |
| CL-01…05 | B5 · Phase 4 Security (Lens-3) |
| CL-06 | A9 · B5 · N8.1 |
| CL-07 | V-NET |
| CL-08 | B2 · A7 |
| NT-01, NT-02, NT-07 | A5 NAT/firewalls/proxies |
| NT-03, NT-04 | A5 DNS (**NT-04 is already taught** — mark done) |
| NT-05 | A5 VPN |
| NT-06 | Phase 4 Security (Prop Lock) |
| NT-08 | A5 TLS |
| CK-01, CK-02, CK-04 | C1 · B2 |
| CK-03, CK-05, CK-06 | C2 |
| WL-01 | C1 |
| WL-02, WL-03, WL-05, WL-06 | C4 · A11 |
| WL-04 | Phase 4 Security |
| IR-01, IR-02, IR-04 | C6 · Phase 4 Security (SecOps) |
| IR-03, IR-05…08 | C7 · Phase 4 Security |
| AI-01…05 | D4 |
| SC-01 | A10 |
| SC-02 | B2 |
| SC-03 | Phase 4 Security |
| PV-01…04 | Phase 4 Security · B1 |
| PV-05 | U7 · A10 |
| CM-01, CM-02 | Phase 4 Security · B1 |

### 6.3 N-track numbering

Foreign section `x.y`, as used in both the SQL and cyber companions, becomes `Nx.y` with the same meaning. The meanings can be inferred from the companions' own context:

| Section | Meaning |
|---|---|
| 2.3 | Cloud SQL |
| 5.3 | Ledger |
| 6.11 | Packet-path map |
| 6.14 | IAP |
| 6.15 | VPC-SC |
| 6.16 | Edge/DNS teardown |
| 7.3 | Data protection |
| 7.5 | Binary Authorization |
| 7.6 | Security Command Center |
| 7.8 | Key/SA incident response |
| 7.9 | Governance |
| 8.1 | Primitives |
| 9.1 | Memorystore |
| 9c | AI |
| 10.x | Operations |

Record the inferred meaning next to every N-section. Where the meaning cannot be inferred, create the section as `[stub — meaning unknown; referenced by <IDs>]` and list it under Open questions.

---

## 7. Suite-wide overlap and ownership register (goes into `Curriculum` §0.3)

When two companions touch the same concept, the **owner** teaches it and the other only **adds**. Later sessions recall it in one line.

| Concept | Owner | Adds |
|---|---|---|
| DNS mechanics | `Curriculum` A5 | Primer SD-08 adds routing policies/TTL discipline; cyber NT-03/04 and DOS-02 add attacks |
| HTTP | `Curriculum` A5 | Primer SD-29 adds idempotency/HTTP/2/3; cyber PQ-S-04 adds the browser security preview |
| Cookie attributes (`Domain`, `Secure`, `HttpOnly`, `SameSite`, `__Host-`) | `Curriculum` A5 HTTP | Cyber AU-01…04 adds attacks at A10 |
| TLS | `Curriculum` A5 (mechanics) / A10 (formal) | Primer SD-35 transit slice; cyber CR-11/12, NT-08 |
| Load balancing, reverse proxy | `Curriculum` A5 / C3 | Primer SD-10/11; cyber NT-07, DOS-01 |
| Rate limiting | Cyber AB-01 (algorithms + abuse) | Primer Q22 is the design exercise and recalls AB-01 |
| Caching | Primer SD-26/27 | Cyber DOS-08 (stampede as an attack); SQL OD-09 (read path) |
| SQL injection / parameterisation | SQL SL-13 (the SQL mechanics) | Cyber WA-05 (attacker model across the whole injection family) |
| Field / column encryption | Cyber CR-17 (the cryptography) | SQL SL-13 `pgcrypto` syntax |
| Backup/restore | SQL OD-04 (runbook) + N2.3 | Cyber IR-07 (ransomware integrity) |
| 2PC / Saga / outbox | `Curriculum` A9 (theory) | SQL CS-07 + SL-10 (SQL); design-patterns ARCH-11 (shape) |
| Pub/Sub | `Curriculum` A7 | Primer SD-28; design-patterns DP-14 (Observer) |
| Shared responsibility | `Curriculum` B1 | Cyber PQ-S-03, CM-01 |
| Least privilege / IAM | `Curriculum` B5 | Primer SD-35; cyber CL-03…05, AU-14 |
| Floating point | M5 | SQL PQ-03 (decimal semantics) |
| Discrete-math foundations of relations | M1 | SQL PQ-01/02, RT-01 |
| Number theory for cryptography | M1 | Cyber CR-01…10 |
| **(v1.1)** Security checklist (encrypt in transit/at rest, XSS, SQLi, least privilege) | Distributed per C-28: `Curriculum` A5/A10/B5 + cyber modules | Primer SD-35 is an index module that points to each owner; its lab is shared with WA-05/SL-13 |
| **(v1.1)** Cache stampede / thundering herd | Primer SD-27 (mechanics: locking, request coalescing, TTL jitter; primer "my addition") | Cyber DOS-08 (adversarially triggered stampede) |
| **(v1.1)** Tail latency, percentiles, hedged requests | M6 (the math: order statistics, fan-out amplification) | Primer SD-03/SD-38c (design levers: timeouts, hedging, replicas); `Curriculum` C6/C7 (alerting/SLOs) |
| **(v1.1)** Little's law | M6 (statement + proof sketch) | Primer SD-03/SD-28 (sizing checks, e.g. 400 rps × 250 ms); A2 slice already taught if C-42 confirms it |
| **(v1.1)** CAP / PACELC | `Curriculum` A8 (CAP statement) → A9 (formal limits, PACELC) | Primer SD-04/SD-05 (per-dataset choice, GCP store mapping) |
| **(v1.1)** Consistent hashing | U2 (analysis: expected movement 1/N, virtual nodes, load bounds) | Primer SD-38a (sharding/rebalancing design); A4 ring slice |
| **(v1.1)** MapReduce / scatter-gather | A9 (distributed computation model) | Primer SD-38b/c, SX-08 (job patterns); `Curriculum` V-DATA (Dataflow/Dataproc) |
| **(v1.1)** CRDTs, operational transform | A9 deepening | Primer Q04 (Google Docs design problem) |
| **(v1.1)** Vector clocks, quorums, gossip | A9 deepening | Primer Q05 (Redis-like KV design problem), SD-39 papers |
| **(v1.1)** Heavy hitters / sketches / approximate counting | U2 (randomized algorithms) | Primer Q16/Q18 (design); SQL AN-04 (SQL approximation) |
| **(v1.1)** Unique ID generation (Base62, Snowflake) | Primer SX-02/Q17 | M1 (counting, birthday bound for collisions); A1 recall (bit layout) |
| **(v1.1)** Garbage collection | U4 (memory management) | Primer Q21 (design problem); SX-04 (data GC/TTL) |
| **(v1.1)** Event sourcing | Design-patterns ARCH-10 (shape) + A9 (theory) | Primer Q23 (stock exchange design); SQL IR/audit designs |
| **(v1.1)** Credential storage & replay | Cyber CR-13 (password KDFs) + CR-17/PV-03 (tokenization/encryption for replayable secrets) | Primer P04 (design context) + SD-35 check question |
| **(v1.1)** OOD problems O01–O07 | Primer (problems) | Design-patterns (principles and patterns they exercise, C-34); A4 recall |
| **(v1.1)** Interview/design method, back-of-the-envelope | Primer SD-00 | Track S1–S3 recall it; they never restate it (C-31) |
| **(v1.1)** Scaling evolution (single box → millions) | Primer P08 + SX-12 | Northstar milestones cite P08 steps (C-32); Track S4/S9 recall |
| **(v1.1)** Terraform labs | Primer TF-1…TF-7 (P08/P01/P07 infra) | SQL TF-DB*; Northstar reuses TF IDs rather than duplicating |
| **(v1.1)** Real-world architecture papers (Dynamo, Bigtable, Spanner, GFS, Chubby, MapReduce, Dapper, Kafka, ZooKeeper…) | Primer SD-39 / §6.4 (index) | A9 deepening and §9.5 cite the same papers; the reading list lives once, in the primer |

---

## 8. Verification protocol — proving that nothing was lost

### 8.1 Manifest (R1)

Write `manifest.py`. For each file, extract:

1. every markdown heading (level + text);
2. every ID that matches the union of the family regexes in §5, recording where each is **defined** (heading or bold lead) and where it is **referenced**;
3. every table row (normalized whitespace), with a hash;
4. every `- [ ]` / `- [x]` item;
5. every line starting with `- **Check:**`, `- **Lab:**`, `- **GCP lens:**`, `- **Attack:**`, `- **Defense pattern:**`, `- **Primer:**`, `- **Trade-offs:**`, or `- **Core:**` — and in general any `- **Label:**` line;
6. every Appendix K key entry;
7. every `(verify)` / `verify` flag;
8. every golden value in the SQL companion's §6 and Appendix K. Hash these separately; they must match byte-for-byte after the rename is applied to the IDs.
9. **Primer items (v1.1):**
   - the 77 checkboxes;
   - the verbatim §6.1/§6.2 tables (hashed like goldens);
   - every "Primer numbers"/"primer:" figure;
   - the §1 coverage counts;
   - the P08 ladder table rows;
   - the §5.1 Rosetta rows;
   - the TF-1…TF-7 items;
   - the §6.4/§6.5/§6.6 lists (17 architectures, 23 companies, 40 blogs; count the items);
   - the §6.7 Anki counts;
   - the §7.2 numbered inconsistencies;
   - every "Modern note" (6) and "my addition"/"my math" label;
   - the mermaid block (node and edge list, extracted as data).

Emit counts per category per file, plus content hashes (with the IDs normalized through the rename map).

### 8.2 Diff (R3 and R10)

The run passes only if all of the following hold:

- For every before-item there is an after-item with an equal content hash (after the ID rename). Otherwise the item must be listed in `CHANGELOG.md → Merges` with a justification that names the item containing it.
- `defined-count(ID) == 1` for every ID in the suite registry.
- Every referenced ID is defined.
- Zero occurrences of the foreign parent names and pseudo-anchors, outside provenance notes.
- Zero mangled IDs (C-10 regex).
- Golden-value hashes are identical.
- All ledger-done items exist and are still marked done.
- In R10 only: each count is greater than or equal to its R1 count. Enhancement only adds.
- **Primer (v1.1):**
  - verbatim-table hashes identical;
  - the CC BY attribution line identical, and the modification note present;
  - the mermaid edge set is a superset of the before-set (after the ID rename);
  - the binding table passes the C-25 topological check;
  - header, §2, and §4.5 all derive from the binding table (C-24);
  - no primer paragraph longer than 20 words appears outside the primer file (C-31);
  - every "my addition" label is still present.

Output `verification-report-R3.md` / `-R10.md`, containing a pass/fail table and every failing item listed.

---

## 9. Enhancement specification (R4–R9)

### 9.1 The academic module standard — apply to every new module and every deepened one

Every module must contain these parts, in this order:

1. **ID · title · Prerequisites.** Split into *hard* (must be done first) and *soft* (helps first), using the dependency style the primer companion already uses.
2. **Learning objectives.** Three to seven, each measurable and phrased with Bloom verbs (define, derive, prove, compute, design, evaluate). Include at least one at the analyze/evaluate/create level.
3. **Core theory.** Definitions stated precisely. Theorems and results stated, with **proofs or proof sketches wherever the matching undergraduate course would prove them**. Examples: correctness of binary search via a loop invariant; the master theorem; Armstrong's axioms; the pumping lemma; Bayes; CAP's formal statement and its limits; FLP at the level of its statement and intuition.
4. **Mechanism walkthroughs.** Concrete, traced, step by step, in the style that has worked in the live sessions.
5. **Worked examples.** At least two. They must be *parallel* problems, never the exercises themselves.
6. **Common misconceptions.** Each one gets the precise correction. This is the learner's known error layer: terminology and precision.
7. **Cloud tie-in.** GCP Lens-1/2/3 as defined in the companions, plus AWS/Azure names via Part VIII. For pure-math and theory modules, state the concrete cloud or architecture decision the theory powers (e.g., M6 → autoscaling targets and tail-latency SLOs; U3 → why static analysis/policy engines can't decide everything).
8. **Lab** with its Lab Reality tag. `[paper]` and `[local]` labs are required for every theory module.
9. **Check questions.** These are *answer-before-explain* and are woven into the teaching sequence (ledger §5).
10. **Exercise set**, graded L0 paper → L1 compute → L2 prove/derive → L3 design/evaluate. Keys go in an appendix, following "Bank ≠ dump" and "after attempt only".
11. **Stitched companion IDs.**
12. **Certification mapping** (verify flags).
13. **References.** Textbook chapter-level plus university course alignment (§9.5). Paraphrased; never transcribed.

**What "undergraduate depth" means here.** A learner who finishes the module could pass the final exam of the aligned university course's corresponding unit. Every module ends with a **skip-test**: 3–6 unaided tasks that demonstrate this.

### 9.2 `Curriculum` enhancements (R4)

#### 9.2.1 New tracks

Author each module to the §9.1 standard, at outline-plus depth in `Curriculum`. `Curriculum` stays the roadmap. If depth there would exceed about 150 lines per module, create `math-foundations-companion.md` and `cs-core-companion.md` with the full treatment, and keep outlines plus stitch rows in `Curriculum`. That mirrors the existing companion pattern.

**Track M — Mathematical Foundations**

| Module | Content |
|---|---|
| **M1 Discrete Mathematics & Proof** | Propositional & predicate logic; proof techniques (direct, contrapositive, contradiction, induction, strong induction, structural induction); sets, relations, functions, and equivalence & partial orders (→ relational algebra, lattices in IAM policy); combinatorics & counting (→ key spaces, birthday bound); recurrences; graph theory (paths, trees, connectivity, matchings, planarity awareness); elementary number theory (divisibility, gcd/Euclid, modular arithmetic, Fermat/Euler, the Chinese Remainder Theorem → RSA/DH in A10); asymptotics made rigorous. |
| **M2 Linear Algebra** (rigorous pass on A2) | Vector spaces, span, basis, dimension; linear maps & matrices; rank-nullity; systems & elimination; orthogonality, projections, least squares; determinants; eigenvalues/eigenvectors, diagonalization; SVD & PCA (→ D1, embeddings in D4). |
| **M3 Calculus** (single + multivariable, rigorous pass on A2) | Limits & continuity; derivatives & the chain rule; integrals & the FTC; series & Taylor approximation; partial derivatives, gradients, Jacobians, Hessians; multivariable chain rule (→ backprop in D2); constrained optimization & Lagrange multipliers; convexity basics (→ gradient descent convergence). |
| **M4 Probability & Statistics** (rigorous pass on A2) | Axioms; random variables; discrete & continuous distributions; expectation, variance, covariance; joint & conditional distributions; LLN & CLT; estimation (MLE/MAP); confidence intervals; hypothesis testing & p-values (→ A/B tests, canaries in C4/D3); regression; Bayesian inference; basic Markov chains (→ M6). |
| **M5 Numerical Methods & Floating Point** (absorbs M.NS) | IEEE 754 representation (recall of A1 binary); rounding, ulp, cancellation; conditioning vs stability; decimal vs binary & money (→ SQL PQ-03, DM-05); numerical issues in ML training (overflow, underflow, mixed precision). |
| **M6 Information Theory & Performance Modeling** | Entropy, cross-entropy, KL (→ D2 losses, compression); coding & compression basics; queueing theory — Little's law proof sketch, M/M/1, M/M/c, utilization-latency curves, tail latency & percentiles; Amdahl's law & the Universal Scalability Law (→ S3, autoscaling, SLOs). |

**Track U — Undergraduate CS Core**

| Module | Content |
|---|---|
| **U1 Computer Architecture & Systems Programming** | Data representation at machine level (recall A1); ISA & assembly basics; C and memory (pointers, stack/heap, memory safety → WA-10); the memory hierarchy & caches (→ SD-37 latency numbers, CS-04 buffer pools); pipelining & branch prediction awareness (→ SC-01 side channels); linking/loading; virtual memory (hardware side, → A6). |
| **U2 Algorithms: Design & Analysis** (rigorous pass on A4) | Correctness via loop invariants; recurrences & the master theorem; divide & conquer; sorting lower bound; hashing theory (universal hashing, load factor → A4 recall); balanced search trees (implement one — lifts A4's caveat); heaps & priority queues; graph algorithms (BFS/DFS, topological sort, Dijkstra, Bellman-Ford, MST, max-flow/min-cut awareness → network design); greedy & dynamic programming with proofs; amortized analysis; randomized algorithms (→ consistent hashing, Bloom filters, HyperLogLog → SQL AN-04); NP-completeness & reductions. |
| **U3 Theory of Computation** | DFAs/NFAs & regular expressions (→ log parsing, WAF regex, ReDoS); context-free grammars (→ parsers, SQL, injection); Turing machines; decidability & the halting problem (→ limits of static analysis / policy verification); complexity classes P, NP, NP-complete. |
| **U4 Programming Languages & Paradigms** | Paradigms (imperative, OO — recall A3; functional: immutability, higher-order functions, closures, map/reduce → Dataflow/Beam); type systems (static/dynamic, soundness intuition, generics); memory management (GC vs ownership); evaluation strategies; interpreters & compilers overview (lexing, parsing, ASTs, IR); DSLs you already use (HCL, YAML, SQL, Rego/CEL). |
| **U5 Concurrency & Parallel Computing** | Threads, races, critical sections; locks, semaphores, monitors, condition variables; deadlock (conditions, detection → SQL DB-9); memory models & atomics awareness; lock-free intuition; async/event loops (→ Cloud Run concurrency); parallel patterns (map-reduce, fork-join, pipelines); GPU/data parallelism awareness (→ D2 training). |
| **U6 Software Engineering & Testing** | Requirements (functional vs quality attributes → S1); design documentation; testing theory (unit/integration/contract/E2E, coverage limits, property-based testing, test doubles); TDD; refactoring; code review; formal specification lite (TLA+ intuition for distributed protocols → A9); reliability of software (defects, static analysis). Stitches with A11. |
| **U7 Professional Practice, Ethics & Law** | ACM Code of Ethics; privacy frameworks (GDPR/CCPA literacy → PV-*); intellectual property & licensing (OSS licenses → supply chain WL-*); accessibility; responsible AI (recall D4); professional communication of architecture decisions. |

#### 9.2.2 Deepen existing modules in place

Add bullets; never delete. Completed modules get extension passes; they are not rewritten.

| Module | Additions |
|---|---|
| **A5** | Congestion control (AIMD, slow start, BBR awareness); flow control & windows; IPv6 in depth (addressing, SLAAC, NDP, dual-stack in VPCs); BGP & inter-domain routing (→ ANS-C01, Interconnect, RPKI via NT-04); QUIC/HTTP/3 internals; anycast (→ Google global LB); MTU/fragmentation; ARP/NDP. |
| **A6** | OSTEP-depth virtualization of CPU (scheduling algorithms, context switches), memory (paging, TLBs, page replacement), and persistence (file systems, journaling → WAL analogy); I/O models (blocking, epoll); file-descriptor and connection limits (→ SD-30). |
| **A7** | API design rigor (resource modeling, versioning, pagination, idempotency keys, error models); gRPC/Protobuf schema evolution; AsyncAPI/event contracts; API gateways. |
| **A8** | Relational algebra & calculus formally (stitched to SQL RT-*); normalization theory with proofs (Armstrong's axioms, closure, lossless-join and dependency-preservation tests); the engine slices (C-05). |
| **A9** | Time & order (Lamport clocks, vector clocks, hybrid logical clocks → Spanner TrueTime contrast); linearizability vs serializability vs sequential consistency; FLP impossibility (statement + intuition); Raft in full (leader election, log replication, safety argument); Paxos at a conceptual level; quorums; CRDTs; failure detectors; the 8 fallacies (already listed). |
| **A10** | Formal security definitions via the cyber CR track; access-control models (DAC/MAC/RBAC/ABAC, capabilities); Saltzer-Schroeder principles in full. |
| **A11** | Stitch with U6; release engineering; semantic versioning; monorepo vs polyrepo. |
| **B-track** | B3 adds S4 reliability architecture; B4 adds unit economics & cost modeling (S9). |
| **C-track** | C2 adds scheduler & controller theory (control loops ↔ reconciliation); C6 adds statistics for alerting (percentiles, burn-rate math from M4/M6); C7 adds SLO math proofs. |
| **D-track** | D1 bias-variance derivation, regularization as a prior (M4), and ESL/ISLR depth; D2 backprop as the multivariable chain rule (M3), optimization (SGD, momentum, Adam), and attention math; D3 statistical rigor for drift detection; D4 transformer internals, evaluation methodology, and RAG evaluation. |

#### 9.2.3 New Phase Plan sequence

Insert it without disturbing completed work. The learner is mid-A5.

1. Finish A5, with every stitch listed in ledger §4 plus C-23.
2. **M1**
3. **U1**
4. A6 (deepened)
5. **U5**
6. **U2**
7. **U4**
8. A7 + design-patterns companion (ARCH-01…08) + **S1, S2**. **N0 starts here.**
9. **M4**
10. A8 + SQL companion + engine slices (N2.x)
11. **M6**
12. A9 + ARCH-09…12 + **S3**
13. A10 + cyber core
14. **U3**
15. A11 + **U6** + **U7**
16. Track B (+ S4–S9 as they bind)
17. Track C
18. **M2, M3, M5**
19. Track D
20. Phase 4 onward (+ S10, S11)

N milestones run alongside from step 8 to the end. `Curriculum`'s statement that Phases 0–3 run "mostly in parallel" is preserved: M and U modules may interleave with B and C when the learner requests it.

#### 9.2.4 Honest scope revision

Rewrite §0's time estimate to account for Tracks M, U, and S, plus Northstar. Say plainly that this is roughly an extra undergraduate year of material. Cert timelines slip accordingly. Offer an explicit "cert-first fast path" that marks which M/U modules are prerequisites for which cert and which are enrichment. The learner can then choose, and ledger preference §5 (depth) remains the default.

#### 9.2.5 Track S — System Architecture Design Studio

`Curriculum` currently has no end-to-end architecture-design method. Add:

| Module | Content |
|---|---|
| **S1** | Requirements, stakeholders, quality attributes & scenarios |
| **S2** | Architecture documentation: views & viewpoints, the C4 model, ADRs, the HLD/LLD contract and NFR tables (absorbs foreign 0.4) |
| **S3** | Capacity & performance engineering: back-of-the-envelope (recall SD-00) + M6 queueing models + load-test design |
| **S4** | Reliability architecture: failure-mode analysis (FMEA), redundancy math (recall SD-07), DR tiers & RTO/RPO, chaos engineering |
| **S5** | Data architecture: OLTP/OLAP/lakehouse, data contracts, lineage |
| **S6** | Security architecture: threat-model-driven design, zero-trust reference architectures (stitches TH-*, NT-*) |
| **S7** | Integration & event-driven architecture (enterprise integration patterns, sagas recall) |
| **S8** | Migration & modernization: 6 R's, strangler fig recall, cut-over planning (the DNS TTL discipline returns here) |
| **S9** | Cost architecture & unit economics |
| **S10** | Architecture evaluation: ATAM-style trade-off analysis, fitness functions, architecture reviews |
| **S11** | Case-study studio: PCA published case studies (verify the current set), AWS SAP-C02 and Azure AZ-305 style scenarios. Each is done as a full design document, reviewed against the S10 rubric. |

### 9.3 Companion enhancements

#### 9.3.1 Primer companion (R5) — rewritten in v1.1

**Scope rule.** The primer file stays the *system-design layer*. Enhancements are **appended** under clearly labelled headings: `**Academic backing:**`, `**Quantitative drill:**`, `**Rubric:**`, `**Lens-3:**`, `**Twin (AWS/Azure):**`. They are never interleaved into primer-attributed text, which keeps the CC BY provenance boundary (invariant 11) intact. Nothing is removed. The v1.0 instruction to remove content duplicated from Track S is **withdrawn**: the primer owns SD-00 and P08, and Track S points to them (C-31).

1. **Academic backing per SD module.** Two to four sentences naming the theory the module rests on and where the suite teaches it formally, plus one proof-level fact the learner should be able to reproduce. Examples:

   | Module | Theory | Where taught formally | Proof-level fact |
   |---|---|---|---|
   | SD-04 | CAP formal statement and its limits | A9 | Gilbert & Lynch framing, paraphrased |
   | SD-07 | Independence assumption behind series/parallel availability | M4 | Why correlated failures break the formula |
   | SD-26/SX-11 | Hit ratio vs working set; LRU optimality limits | U1, U2 | Competitive-analysis intuition |
   | SD-38a | Expected key movement 1/N; virtual nodes | U2 | Load variance argument |
   | SD-28 | Queueing | M6 | Utilization → latency blow-up (M/M/1) |
   | SD-03 | Percentile math; fan-out tail amplification | M6 | 1 − (1 − p)^n |

2. **Quantitative drill per SD module**, using M6/M4 where relevant. Original problems only. The answers are computed and checked in the container, not written from memory, and go into a new primer Appendix K ("after attempt only").
3. **Close the primer's own gaps** without editing primer text:
   - Add a *Modern note* wherever §7.2 lists an aged claim that has no note yet (80× vs 120×, MySQL query cache, NoSQL transactions, Elasticsearch classification, GraphQL conflation).
   - Add a solution sketch plus rubric for O07 (the primer placeholder).
4. **Q01–Q23 rubrics.** The primer asks for five lines per Q (requirements, numbers, design, bottleneck, trade-off). Turn that into a scored rubric per Q, aligned with the S10 architecture-evaluation rubric. It must include the Q's "twist" as a mandatory element.
5. **Lens-3 for every P-problem.** Cert-depth trade-offs and limits, `(verify)`-flagged, cross-referenced to the PCA domains in `Curriculum` Part V.
6. **AWS/Azure twin designs for P01–P08** via Part VIII names. P08's AWS version is the primer's own wording, so it is referenced, not rewritten.
7. **Terraform.** Keep TF-1…TF-7. Add `terraform validate` + `plan` acceptance criteria per item, and cross-reference the Northstar milestones that reuse them (C-32).
8. **Anki integration.** Keep primer §6.7. Add the rule "one card per Check question" for *all* suite files, pointing to the primer's method as the owner.
9. **Nothing from the primer repository is newly copied.** Additions are original, or cite the primer by section.

#### 9.3.2 SQL companion (R6)

- Port the engine slices DB-1…DB-10 (C-05).
- Add proofs to RT-04/05: Armstrong soundness & completeness sketch, the lossless-join test, BCNF vs 3NF trade-off.
- Add query optimization theory: equivalence rules, cost-based join ordering (Selinger DP).
- Add distributed SQL internals at conceptual depth: Spanner, AlloyDB architecture (verify).
- Re-anchor the UG/grad gates.
- **Keep every golden value untouched.** Any *new* exercise with a numeric answer must either be executed against the seed in the container (PostgreSQL) or keyed qualitatively. Never type goldens from memory.

#### 9.3.3 Design-patterns companion (R7)

- Add refactoring (catalog-level, cross-referenced to AP-*).
- Add testing patterns (test doubles, xUnit patterns).
- Add concurrency patterns (thread pool, producer-consumer, reactor, active object, monitor object → U5).
- Add functional design patterns (→ U4).
- Add a **cloud design patterns** catalog: retry with backoff & jitter, circuit breaker (recall ARCH-12), bulkhead, cache-aside, queue-based load leveling, competing consumers, priority queue, throttling, claim check, valet key, sidecar, ambassador, anti-corruption layer, gateway aggregation/offloading/routing, leader election, sharding, compensating transaction, health endpoint monitoring, and backends-for-frontends. Each entry gets GCP resources and, where relevant, overlap rows pointing to the primer/SQL/cyber owners.
- Add a UML depth pass (sequence/state/component/deployment diagrams, used in S2).
- Add exercises with keys at each level.

#### 9.3.4 Cyber companion (R8)

- Add an explicit M1 dependency to CR-01…10 (modular arithmetic, groups for DH/ECC intuition, probability for IND-CPA advantage).
- Add formal definitions and security-reduction sketches where CS255 would present them (paraphrased).
- Add access-control formal models (Bell-LaPadula, Biba awareness) to A10 stitches.
- Author any checkpoint cards left `[pending R8]` from C-11.
- Add network-security depth matching the A5 deepening (BGP/RPKI, IPv6 attack surface, QUIC).
- Keep every Prop Lock.

### 9.4 Northstar reference application (R9)

Create `northstar-reference-app.md`:

- a one-page product definition (the storefront / customer API / admin / service-to-service / data / CI-CD / AI-gateway planes already sketched in cyber Appendix N);
- an architecture baseline;
- milestone sections N0…N12, including every reconstructed section from C-05 to C-07;
- each milestone's companion stitches, its Lab Reality budget, its acceptance evidence, and the architecture documents it produces (S2 format).

Rewrite all 36 occurrences of "the reference cloud app" to "Northstar (`northstar-reference-app.md`)".

### 9.5 University and textbook alignment table

Add this as `Curriculum` Appendix. Cite at chapter/lecture level and paraphrase. Course numbers change; mark them `(verify current numbering)`.

| Area | Primary texts | Aligned courses |
|---|---|---|
| M1 | Lehman, Leighton & Meyer, *Mathematics for Computer Science*; Rosen, *Discrete Mathematics and Its Applications*; Velleman, *How to Prove It* | MIT 6.1200 (formerly 6.042); Stanford CS103 |
| M2 | Strang, *Introduction to Linear Algebra*; Axler, *Linear Algebra Done Right* | MIT 18.06 |
| M3 | Stewart, *Calculus*; Boyd & Vandenberghe, *Convex Optimization* (intro chapters) | MIT 18.01/18.02 |
| M4 | Blitzstein & Hwang, *Introduction to Probability*; Wasserman, *All of Statistics* | Harvard Stat 110 |
| M5 | Goldberg, "What Every Computer Scientist Should Know About Floating-Point Arithmetic"; Heath, *Scientific Computing* | — |
| M6 | Cover & Thomas, *Elements of Information Theory*; Harchol-Balter, *Performance Modeling and Design of Computer Systems* | — |
| U1 | Bryant & O'Hallaron, *Computer Systems: A Programmer's Perspective*; Patterson & Hennessy, *Computer Organization and Design* | CMU 15-213; Berkeley CS61C |
| U2 | Cormen et al., *Introduction to Algorithms*; Kleinberg & Tardos, *Algorithm Design* | MIT 6.006/6.046; Stanford CS161 |
| U3 | Sipser, *Introduction to the Theory of Computation* | Stanford CS103/CS154 |
| U4 | Abelson & Sussman, *SICP*; Nystrom, *Crafting Interpreters*; Pierce, *Types and Programming Languages* (intro) | — |
| U5 | Arpaci-Dusseau, *OSTEP* (concurrency); Herlihy & Shavit, *The Art of Multiprocessor Programming* | — |
| U6 | Sommerville, *Software Engineering*; Fowler, *Refactoring*; Lamport, *Specifying Systems* | — |
| U7 | ACM Code of Ethics; Baase, *A Gift of Fire* | — |
| A5 | Kurose & Ross, *Computer Networking*; Peterson & Davie, *Computer Networks* | Stanford CS144; Berkeley CS168 |
| A6 | Arpaci-Dusseau, *OSTEP*; Kerrisk, *The Linux Programming Interface* | Berkeley CS162 |
| A8 | Silberschatz, Korth & Sudarshan, *Database System Concepts* | CMU 15-445 |
| A9 | Kleppmann, *Designing Data-Intensive Applications*; van Steen & Tanenbaum, *Distributed Systems*; the Lamport clocks paper, the Raft paper, the FLP paper | MIT 6.5840 (formerly 6.824) |
| A10 | Boneh & Shoup, *A Graduate Course in Applied Cryptography*; Katz & Lindell, *Introduction to Modern Cryptography*; Anderson, *Security Engineering* | Stanford CS255/CS155 |
| S-track | Bass, Clements & Kazman, *Software Architecture in Practice*; Richards & Ford, *Fundamentals of Software Architecture*; Ford et al., *Building Evolutionary Architectures*; Hohpe & Woolf, *Enterprise Integration Patterns*; Newman, *Building Microservices*; Google *SRE* book & *Workbook*; the C4 model; Nygard on ADRs; GCP Architecture Framework, AWS and Azure Well-Architected frameworks | — |
| D-track | Hastie, Tibshirani & Friedman, *The Elements of Statistical Learning* (and *ISLR*); Goodfellow, Bengio & Courville, *Deep Learning*; Bishop, *Pattern Recognition and Machine Learning*; Huyen, *Designing Machine Learning Systems*; Jurafsky & Martin, *Speech and Language Processing* | — |

---

## 10. Regenerate `session-progress-ledger.md` (R10)

Keep the ledger's structure and apply these changes:

- Add the new files to §1 and remove the SQL mismatch flag, since C-02 is resolved.
- Keep §2 and §5 verbatim.
- In §3, apply renamed IDs and add "extension passes pending" pointers: A2 → M2/M3/M4; A4 → U2.
- Rewrite §4 (A5) to show:
  - done: OSI, IP, subnetting, routing, TCP/UDP, DNS (full), and NT-04;
  - open: the HttpOnly/`Domain=.example.com` cookie question, verbatim;
  - remaining in order:
    1. NT-03 + DOS-02
    2. HTTP (SD-29, PQ-S-04, cookie mechanics, WA-08 preview)
    3. TLS (SD-35 transit slice, CR-11, CR-12 with the C-14 bridge, NT-08)
    4. NAT/firewalls/proxies (SD-11, NT-01, NT-02, NT-07)
    5. Load balancing (SD-10, SD-09, DOS-01)
    6. VPN (NT-05)
    7. A5 deepening bullets (§9.2.2)
    8. A5 checkpoints (P08 steps, the C-11-mapped NT card, CR-E12)
    
    Items 1–8 above are also amended by the v1.1 primer rules below.
  - postponed with Prop Lock: NT-06, DOS-03 → A10, DOS-04 → Phase 4.
- In §6, replace the open items with the next sequence from §9.2.3 and any `refactor-state.md` open questions.
- **Primer reconciliation (v1.1):**
  - Add a ledger subsection **"System-design-primer status"**. It lists the ticked IDs (SD-08, SD-30, SD-31), the done slices (C-42), and the **unverified** IDs, each paired with the Check question to use as its recall check.
  - Amend the remaining-A5 order so that:
    - the HTTP session opens with the SD-08 GCP-lens recall (C-43);
    - HTTP includes `SD-26[HTTP-layer caching slice]` (C-27) and SD-29;
    - load balancing is preceded by `SD-01[slice]` and `SD-02[slice]` (C-26) and includes SD-10, SD-09, and SD-11;
    - the A5 checkpoint is the narrowed P08 step set (C-33).
  - Add O01, O02, and O07 as pending A4 recall checkpoints, and O03–O06 as A7 checkpoints (C-34).

---

## 11. Final acceptance checklist (all must be ✅ in `verification-report-R10.md`)

- [ ] Zero references to `gcp.md`, `gcp-curriculum.md`, `unified-curriculum.md`, or `/Users/` outside provenance notes
- [ ] Every ID defined exactly once suite-wide; every reference resolves
- [ ] Zero mangled or corrupted tokens (C-10 scan)
- [ ] Nine phantom checkpoints resolved (C-11)
- [ ] Every manifest-before item accounted for (kept, moved, renamed, or merged with justification)
- [ ] Golden-value hashes identical
- [ ] Ledger-done items still done; the open cookie question preserved
- [ ] Every new or deepened module has all 13 parts of §9.1 and a skip-test
- [ ] Tracks M, U, and S sequenced (§9.2.3) with prerequisite edges and no cycles (verify with a script: topological sort of the prerequisite graph)
- [ ] Northstar file exists; all N-anchors resolve; reconstructed sections labelled
- [ ] Suite overlap register (§7) is present in `Curriculum` §0.3, and each companion's §0 points to it
- [ ] Ledger §5 preferences copied into every file's §0
- [ ] Every new version-sensitive claim carries `(verify)`
- [ ] Scope estimate revised honestly (§9.2.4)
- [ ] **Hardening (v1.2):**
  - [ ] inputs preserved in `inputs-original/` with hashes; a diff delivered per file (invariant 14)
  - [ ] every C-nn marked reproduced / not / different in `refactor-state.md` (§2 hardening 1)
  - [ ] R2 approval gate honoured (the "approve" message is recorded)
  - [ ] a self-review block is present in every phase report
  - [ ] `refactor-tools/` delivered; each script idempotent (run twice, identical output)
  - [ ] C-44 certification count logged as an open question; interim wording applied
  - [ ] inline boxes present in `Curriculum` (C-45) and design patterns (C-58)
  - [ ] SQL lab kit rebuilt; match/mismatch report delivered; zero goldens edited (C-50, C-56)
  - [ ] E11/E12/"P1–P11" resolved (C-51, C-52)
  - [ ] every design-patterns item has its own Check; GoF quoting audited; named real examples added (C-59–C-61)
  - [ ] A7 (and any module with more than 20 bound concepts) split into teaching blocks (C-49)
  - [ ] the Suite Teaching Contract is present as `Curriculum` §0.4 and Lab Safety as §0.5, and each companion's §0 points to them (C-47)
  - [ ] `errata.md` seeded (C-67); misconception register seeded (C-68)
  - [ ] `volatility-register.md` and `coverage-matrix.md` exist; gaps are explicit (§12.3, §12.4)
  - [ ] `dag_check.py` passes: no cycles, no PRIMARY-before-prerequisite, no unknown IDs (§12.5)
  - [ ] consistency lints pass (§12.7)
  - [ ] the ledger YAML block validates against the registry and the DAG (§14)
- [ ] **Primer (v1.1):**
  - [ ] `primer-binding-table.md` exists; every SD/SX ID has exactly one PRIMARY anchor; header, §2, and §4.5 regenerated from it (C-24, C-41)
  - [ ] zero PRIMARY-before-prerequisite violations (C-25)
  - [ ] SD-01/SD-02 slices placed before SD-10 at A5 (C-26)
  - [ ] SD-26 split into an HTTP-layer slice (A5) and PRIMARY at A8/A9 (C-27)
  - [ ] SD-35 is an index module with "Taught by" pointers and a Prop-Lock note; its lab is marked shared, not deleted (C-28)
  - [ ] Suite Session Protocol present in `Curriculum` §0.4 and referenced from all companion §0.3 sections (C-29)
  - [ ] primer rules 6 and 9 amended as specified (C-30, C-31)
  - [ ] every Northstar milestone that changes the architecture cites a P08 step and TF-n (C-32)
  - [ ] P08 checkpoint timings consistent across §2, §4.3, §4.5, and the card (C-33)
  - [ ] O-problem gates consistent (C-34)
  - [ ] SQL `SD-n` → `SCH-n` done without touching two-digit primer references (C-37)
  - [ ] mermaid diagram relabelled and syntax-valid (C-39)
  - [ ] CC BY attribution and modification note present; verbatim-table and primer-number hashes identical (invariants 11, 12)
  - [ ] ledger primer-status subsection present (C-42, C-43)
- [ ] Deliverables presented:
  - refactored files ×5
  - `northstar-reference-app.md`
  - any `*-companion.md` split out per §9.2.1
  - `id-rename-map.csv`
  - `crosswalk.md`
  - `primer-binding-table.md`
  - `errata.md`, `volatility-register.md`, `coverage-matrix.md`, `dag.json`
  - `work/sql-lab-kit/` plus its verification report
  - `refactor-tools/`, `diffs/`, `inputs-original/` hashes
  - `CHANGELOG.md`
  - `verification-report-R3.md`
  - `verification-report-R10.md`
  - `refactor-state.md`
  - new `session-progress-ledger.md`

---

## 12. Content hardening (applies from R2 onward)

### 12.1 Technical accuracy

Every technical claim that is new or corrected must meet one of these standards:

- **(a)** it was executed in the container (code, SQL, arithmetic);
- **(b)** it cites a textbook section or a primary paper;
- **(c)** it cites official documentation checked live, with the date;
- **(d)** it carries `(verify)`.

Product and exam claims require (c) or (d). Nothing is asserted from memory as current fact.

### 12.2 Execution-verified exercises

Every exercise with a computable answer is checked by execution before its key is written:

| Exercise type | How it is checked |
|---|---|
| Python katas | unit tests |
| SQL | the rebuilt kit (C-50) |
| Subnetting / CIDR / BoE / queueing arithmetic | a Python checker |
| Proofs | peer-checked by a second read-through against the textbook statement |
| Terraform | `terraform fmt` + `validate` if the binary and providers can be obtained; otherwise an HCL parse (e.g., `python-hcl2`) plus a resource-reference lint, labelled "parse-checked, not validated" |
| Mermaid | `mermaid-cli` if it can be obtained; otherwise a structural lint (balanced brackets, known arrow tokens, every node defined), labelled accordingly |

Keys record the method used ("executed", "parse-checked", "hand-derived").

### 12.3 Volatility register

`volatility-register.md` lists every time-sensitive claim across all files. Each row has: claim · file:line · category (exam date / domain weight / product name / GA status / price / quota) · last-checked date · source · status.

- Claims older than 90 days at teaching time are re-verified, or read out with their date.
- Four to six weeks before any exam, the whole register for that cert is re-checked, as `Curriculum` Part IX already requires.

### 12.4 Coverage matrix

`coverage-matrix.md` proves completeness in both directions:

- **(a) CS2023 knowledge areas → modules.** This is the undergraduate-completeness claim. Each knowledge area is marked covered / partial / out of scope with a reason. `(verify)` the current CS2023 area list.
- **(b) Every exam guide domain, for each cert in Parts V–VII → modules.**

Gaps become explicit rows in `refactor-state.md → Gaps`, never silent omissions.

### 12.5 Global prerequisite DAG

Merge every prerequisite statement in the suite into one graph, `dag.json`, including:

- the primer's §4.1;
- SQL's gates and tiers;
- the design-patterns §10 gate;
- the cyber companion's Prop Lock and tiers;
- the M/U/S tracks;
- the ledger's done-set.

`dag_check.py` asserts three things:

- the graph has no cycles;
- no PRIMARY binding comes before its hard prerequisites;
- every ID in the graph exists in the registry.

The script runs at R3, R10, and at every session close (§13.9).

### 12.6 Errata log

`errata.md` is permanent and append-only. Each entry records: date · where the error was (file:line or chat session) · what was wrong · the correct statement · evidence · what was done (content corrected / learner re-told / check added).

Seed it with C-67's two entries. The tutor adds to it whenever an error is found, including its own mistakes in explanations.

### 12.7 Consistency lints (run in R3, R10, and whenever a file changes)

- An ID used in prose has the same title everywhere.
- Every numeric fact appearing in two places has the same value. Examples: the 13 root-server addresses; the 2.5 M seconds/month conversion; the latency table.
- Every "see §x" cross-reference resolves.
- No table has a ragged column count.

## 13. Teaching hardening — the Suite Teaching Contract (becomes `Curriculum` §0.4)

### 13.1 Authority and rhythm

The contract applies the precedence ladder of invariant 13. Its rhythm, taken from the ledger and the skill as reconciled in C-70:

- **One concept per turn**, at full depth.
- New material is taught by **direct explanation**; procedures are taught with **worked, parallel examples**.
- Every turn carries **exactly one** focused question, embedded in the teaching.
- Diagnosis happens through those embedded checks. No separate probing.
- **Correction style**, from the ledger: confirm the correct part explicitly, then sharpen the imprecise part by stating the exact mechanism.
- **No false praise.** Hold the line under "just tell me" when the learner is impatient. Give a foothold when the learner is genuinely stuck.
- **Overrides** (C-75): skip after passing the skip-test, jump, or go hands-on. Every override is recorded.

### 13.2 Exercise progression (from SQL's ten-rung ramp, C-54)

Concepts are taught through the rhythm in 13.1. **Exercises** for a concept climb these rungs, one item per turn, and do not advance until the current rung is passed:

1. basic unseen check
2. routine variation
3. mixed transfer (the new idea plus exactly two earlier mastered ideas)
4. top-rung challenge
5. reflection (the learner explains back, or invents an example)

The first five rungs of the SQL ramp (anchor, vocabulary, representation, core move, worked illustration) are the teaching turns themselves.

### 13.3 Mastery states and spaced retrieval

Every ID carries one of these states:

`not-started` → `in-progress` → `taught` (explained and first check answered) → `mastered` (passed the rung-3 or rung-4 item, or passed the skip-test).

It can also be marked, alongside or instead:

- `shaky` — missed a check after teaching;
- `unverified` — claimed done without evidence, like the C-42 primer items;
- `sliced` — only a named slice has been taught.

**Spaced recall.** Every `taught` or `mastered` ID gets recall checks at roughly +1, +3, +7, and +21 sessions after it was mastered. Each recall is one question, woven into a later session where the concept is relevant (interleaving), never as a quiz dump. A missed recall sets the ID to `shaky` and schedules a targeted re-teach of **only the gap**.

**Misconception register.** Stored in the ledger. Each entry records: the misconception, its layer (terminology / mechanism / arithmetic / model), the correction, and the date it was last probed. It is seeded from C-68. Checks deliberately probe registered misconceptions until two consecutive correct answers retire the entry.

### 13.4 Anchoring and suite-wide Prop Lock (C-55)

- No term, product, or control is used in an explanation, example, or check unless it is anchored: taught this session, or at least `taught` on the ledger.
- A **named-but-not-taught** mention is allowed only when it is explicitly labelled "we'll cover this in X". C-33's P08 treatment is the model.
- A check that relies on unanchored terms is invalid. Fix the check; don't mark the learner shaky.

### 13.5 Check-question quality rules

1. It tests **mechanism or application**, not recall of wording.
2. It asks **one thing** (C-69).
3. It is answerable from anchored material only (13.4).
4. It has a written expected answer and at least one expected wrong answer, tied to the misconception register, in the owning file's keys.
5. It is **precision-sensitive** where the learner's pattern calls for it (C-68). The expected answer names the exact mechanism, so a vague-but-right answer earns the "confirm then sharpen" treatment.
6. It is never answered by the tutor in the same turn.

### 13.6 Exercise pre-flight (C-67)

Before issuing any exercise or scenario, the tutor silently checks it against five conditions:

1. **Internal consistency** — record types, protocols, and addresses match (for example, a CNAME never "points at an IP").
2. **Every term is anchored.**
3. **Exactly one question** is asked.
4. **The answer is derivable** from what has been taught.
5. **Any numbers have been computed.**

Failing any condition means the tutor fixes the exercise before sending it. If an error is still discovered later, the tutor corrects it openly in the next turn and logs it in `errata.md`.

### 13.7 Pacing budgets

Each module gets an estimated session count in `Curriculum`, computed from its bound-concept count at roughly 3–5 concepts per session at full depth. Modules over budget are split into teaching blocks (C-49). The estimate feeds the honest scope revision (§9.2.4). It is a plan, not a pressure: ledger §5 forbids compressing depth to hit it.

### 13.8 Checkpoints and capstones

A problem or checkpoint runs only when every one of its must-know IDs is at least `taught`, as checked against the DAG. A problem introduces at most one new concept (primer rule 5, now suite-wide). Checkpoint results are recorded in the ledger with the rubric score where a rubric exists (S10, Q-rubrics).

### 13.9 Session close protocol (C-72, C-73)

At the end of every session, the tutor:

1. **Runs the stitch-completeness list.** Every ID bound to the session is marked taught / sliced / deferred-with-reason / recalled. Nothing may be left unmarked.
2. **Updates mastery states** and the spaced-recall schedule.
3. **Updates the misconception register.**
4. **Adds any errata.**
5. **Emits a ledger delta block** (§14 format) for the learner to merge or paste, and a full regenerated ledger every 5th session or when asked.
6. **Names the exact resume point:** the next concept and any open question, written verbatim.

## 14. Ledger schema (machine-checkable; the regenerated ledger follows it)

The ledger keeps its human-readable sections. It adds one fenced YAML block, which is the source of truth for scripts:

```yaml
ledger_version: 2
as_of: 2026-09-24
learner:
  preferences:        # ledger §5, verbatim strings
    - "..."
  error_pattern: "terminology/precision layer, not logic"
position:
  module: A5
  block: A5.x         # teaching block per C-49
  resume_concept: "HTTP request/response cycle"
  open_question: "HttpOnly + Domain=.example.com cookie — would HttpOnly have saved the user? why/why not"
ids:                  # one entry per ID touched so far
  SD-08: {state: mastered, evidence: "ledger §4 + chat 2026-09-24", recall_due: [..]}
  SD-21: {state: sliced, slice: "hash-table", at: A4}
  NT-04: {state: taught, evidence: "chat 2026-09-24"}
misconceptions:
  - {text: "authoritative server returns IP directly to OS", layer: mechanism, corrected: 2026-09-24, probes_correct: 0}
overrides: []
errata_refs: [E-001, E-002]
```

`verify.py` validates this block against the ID registry and the DAG.

---

*End of meta prompt (v1.2). Execute phase by phase; stop after each phase and wait for "continue" (and for "approve" at the R2 gate).*
