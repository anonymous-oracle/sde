# Records for design-patterns-companion.md (R2b, R2c and R4 build edits, 2026-09-24)

Refactor bookkeeping only, not course material. Decision D6 keeps provenance, the D3 archive and every line the build changed or removed (R2b; the R2c Go tie-ins; R4, rules R4-*) out of the course files; decision D3 keeps them here, verbatim. Each entry names the build journal number (outputs/r2b/journal.jsonl), the rule and the class.

**J169** · G0 · R2 in-file D3 archive, moved out whole

````text


---

## Pre-refactor text archive (D3)

*Refactor-authored section (2026-09-24).* Decision D3 says content may be re-arranged but never removed. Each block below is the exact pre-refactor text (after the §5 ID renames) of a line that R2 corrected or regenerated. It is kept for provenance only and is **not authoritative**; the live text above wins. Tooling excludes this section from ID and anchor checks.

**D3-01** · C-64 · §0.4 notation

```text
`PR-nn` SOLID/GRASP principles · `DP-nn` GoF design patterns · `ARCH-nn` architectural styles/DDD/enterprise patterns · `AP-nn` anti-patterns. `[Cr]` = Creational, `[St]` = Structural, `[Bh]` = Behavioral (GoF's own three categories).
```

**D3-02** · C-16 · §2 A7 row

```text
| **A7 — Software Architecture & APIs** | **Everything in this file**, in order: F-01…04, then PR-01…14, then DP-01…23, then ARCH-01…12 (minus ARCH-09…12 if A9 isn't done yet), then AP-01…10 | Primary landing module — flagged as a curriculum gap during the A5 networking session, filled here |
```

**D3-03** · C-60 · §6 format line

```text
Format per pattern: **Intent** (GoF's own line) → **Problem** → **Structure** → **Trade-offs** → **Real-world example**.
```

````

**J170** · G3 · anchor-rewrite

````text
> **Refactor note (2026-09-24, §7):** the suite-wide register is `Curriculum` §0.3; this table is the patterns slice of it, and on a conflict §0.3 wins.
````

**J171** · G5 · anchor-rewrite

````text
| **A7 — Software Architecture & APIs** | **Everything in this file**, in order: F-01…04, then PR-01…14, then DP-01…23, then ARCH-01…08, then AP-01…10. ARCH-09…12 are taught in the A9 session (next row; C-16). `Curriculum` A7 splits this into teaching blocks A7.3–A7.7 (C-49) | Primary landing module — flagged as a curriculum gap during the A5 networking session, filled here |
````

**J172** · G5 · anchor-rewrite

````text
  - *Owner pointer (C-62):* Repository's definition is owned by ARCH-07 (Fowler, PoEAA). Here, recall it in one line and add the DDD constraint: one repository per aggregate root.
````

**J173** · G5 · anchor-rewrite

````text
| **A7 — Software Architecture & APIs** | **Everything in this file**, in order: F-01…04, then PR-01…14, then DP-01…23, then ARCH-01…08, then AP-01…10. ARCH-09…12 are taught in the A9 session (next row; C-16). `Curriculum` A7 splits this into teaching blocks A7.3–A7.7 | Primary landing module — flagged as a curriculum gap during the A5 networking session, filled here |
````

**J174** · G9 · anchor-rewrite

````text
### 0.5 Learner teaching preferences (binding; copied unchanged from session-progress-ledger.md §5, invariant 4)
````

**J175** · G9 · anchor-rewrite

````text
- When companion-file content (system-design-primer, SQL, design-patterns) overlaps a `Curriculum` module, **teach it once, stitched into the same session** — never as a separate pass, per each companion's own §0.2 stitching rules.
````

**J176** · G9 · anchor-rewrite

````text
- If a companion file references module IDs that don't exist in `Curriculum` (as `sql-databases-companion.md` does), **say so plainly rather than forcing a silent, possibly-wrong mapping** — this was well received when done for the SQL companion.
````

**J177** · G10 · anchor-rewrite

````text
> **Note:** the suite-wide register is `Curriculum` §0.3; this table is the patterns slice of it, and on a conflict §0.3 wins.
````

**J625** · DP-1 · anchor-rewrite

````text
Companion to `Curriculum` ("The Consolidated Cloud Mastery Curriculum"). Sibling to `system-design-primer-companion.md` and `sql-databases-companion.md`.
````

**J626** · DP-1 · anchor-rewrite

````text
When other companions bind to the same session, the Suite Session Protocol in `Curriculum` §0.4 governs.
````

**J628** · DP-3 · anchor-rewrite

````text
| **A7 — Software Architecture & APIs** | **Everything in this file**, in order: F-01…04, then PR-01…14, then DP-01…23, then ARCH-01…08, then AP-01…10. ARCH-09…12 are taught in the A9 session (next row). `Curriculum` A7 splits this into teaching blocks A7.3–A7.7 | Primary landing module — flagged as a curriculum gap during the A5 networking session, filled here |
````

**J629** · DP-3 · anchor-rewrite

````text
> **Note:** the suite-wide register is `Curriculum` §0.3; this table is the patterns slice of it, and on a conflict the main course's register wins.
````

**J1046** · R5-11 · relabel

````text
**Check:** a `PaymentValidator` exists purely to check payment rules, representing no real-world "thing." Which GRASP principle justifies it, and which one answers "why isn't this just inside `Payment`?"
````

**J1047** · R5-11 · relabel

````text
**Check:** a `UserManager` has 40 methods covering auth, email, reports, and DB migrations. Name the anti-pattern and the SOLID violation at its root.
````

**J1063** · R6-2 · new-content

````text
- **Bounded Context:** an explicit boundary within which a model is internally consistent — the same word can mean different things in different contexts, deliberately.
````

**J1064** · R6-2 · new-content

````text
- **PR-09 Low Coupling:** minimize how many other classes a class depends on.
````

**J1065** · R6-2 · new-content

````text
**ARCH-12 · Resilience micro-patterns** *(gated behind A9)* — **Circuit Breaker:** wraps a remote call; after enough failures, "opens" and fails fast for a cooldown, protecting the caller. **Strangler Fig:** incrementally migrate a legacy system by routing growing traffic shares to new services via a facade/proxy layer until legacy is retired — the formal pattern behind C4's legacy-migration-via-CI/CD question. **Bulkhead:** isolate resources per downstream dependency so one failing dependency can't exhaust resources needed elsewhere.
````

**J1066** · R6-2 · new-content

````text
- **AP-07 Premature Optimization:** applying a pattern (often Flyweight) for a performance problem that doesn't yet exist.
````

**J1067** · R6-2 · new-content

````text
- **AP-09 Shotgun Surgery:** one logical change requires editing many unrelated classes — the mirror image of SRP done right.
````

**J1113** · R7-2 · §0.1–§0.3 replaced by the part's own §0 (generic rules are in the course guide)

````text
## 0. Read this first

### 0.1 Standing instruction (for Claude, every session)
This file is a complement to the Curriculum, not a second curriculum. It supplies one thing Curriculum module **A7 (Software Architecture & APIs)** names but doesn't detail: formal OOP design theory — SOLID, GRASP, the GoF catalog, Clean/Hexagonal/Onion architecture, DDD building blocks, and the enterprise/microservice patterns layered on top. Teach this file's modules when A7 is reached, in the same session shape already used for the other two companions: one concept at a time, checked before moving on. This file supplies content; it does not relax the core teaching rhythm.

### 0.2 Stitching / no-overlap rules
1. **A3 already taught operational OOP** (class, object, `self`, constructor, inheritance mechanics via the `Dog` example) — this file never re-derives that; every module below assumes it and *recalls* it in one clause, never re-teaches it.
2. **One concept, one teaching**, same convention as the sibling companions. Where a pattern's core idea overlaps a system-design-primer concept (Observer ↔ Pub/Sub's fan-out, Strategy ↔ SD-10's load-balancer algorithms), teach the OOP-level mechanism here and cross-reference the SD companion's system-level version — don't re-teach either.
3. **Order is enforced.** Foundations (§3) → SOLID (§4) → GRASP (§5) → GoF catalog (§6) → Architecture (§7) → Anti-patterns (§8). A pattern is never taught before the principle it embodies — e.g., Strategy is not taught before Open/Closed, because Strategy *is* Open/Closed made concrete.
4. **Every pattern gets three things, always:** the problem it solves (pain before solution, never the reverse), the formal structure using canonical GoF participant names, and at least one real industry example — a cloud SDK, a popular library, or a framework this Curriculum touches elsewhere. Academic rigor and industry grounding are both mandatory, every time, not alternatives.
5. **Distinguish pattern from principle from architecture, explicitly, whenever one could be mistaken for another.** A *principle* (SOLID, GRASP) is a rule for arranging responsibility. A *pattern* (GoF) is a named, reusable solution shape to a recurring problem, usually at class/object level. An *architecture* (Clean, Hexagonal, microservice patterns) is a system-level arrangement, often built from several patterns and principles at once. Conflating these three is the most common shallow-learning failure in this material — call it out on sight.
6. **Tracking is inline**, same as the sibling files: tick `- [ ]` or say "done" in chat.
7. **Honesty flags.** `(debated)` marks where the industry itself disagrees (e.g., whether Singleton is a pattern or an anti-pattern in modern practice); `(GoF)` marks a definition quoted/adapted directly from the 1994 book, since its precise wording is often what's actually tested.

### 0.3 How one stitched session runs
1. **Anchor** — name the module(s) from §1's ledger being taught this session.
2. **Motivate** — state the problem *before* the solution; a pattern introduced without its pain is cargo-cult programming (AP-06) in the making.
3. **Structure** — the formal participants, using GoF's own names.
4. **Trade-offs** — every pattern costs something; name it, don't just sell the benefit.
5. **Real-world anchor** — one concrete industry example.
6. **Check** — the module's check question; the learner answers before being told the answer.
7. **Close** — tick the box; note anything shaky for a later recall.

When other companions bind to the same session, the Suite Session Protocol (rule 0.4.2 in §0.6) governs.

````

**J1114** · R7-2 · anchor-rewrite

````text
### 0.4 Notation
````

**J1115** · R7-2 · copied preferences, contract and Lab Safety moved out

````text
### 0.5 Learner teaching preferences (binding)

- **Check questions must be woven into the concept explanation itself**, not asked as separate "what do you already know" diagnostics — the learner explicitly opted out of background-probing questions and asked for calibration to happen through how they handle the material.
- **"Maintain curriculum depth and academic rigour"** has been repeated multiple times as an explicit standing instruction — do not compress, simplify, or skip the "why," even under time pressure or a fast pace of correct answers.
- When companion-file content (system-design-primer, SQL, design-patterns) overlaps a main-course module, **teach it once, stitched into the same session** — never as a separate pass, per each companion's own §0.2 stitching rules.
- If a companion file references module IDs that don't exist in the main course (as the SQL companion's did before its IDs were rebound), **say so plainly rather than forcing a silent, possibly-wrong mapping** — this was well received when done for the SQL companion.

### 0.6 Suite Teaching Contract and Lab Safety (same text in every part)

The main course's §0.4 and §0.5, copied whole so that this companion can be taught on its own terms. The rule numbers stay the main course's (0.4.1…0.4.10, and the five Lab Safety rules), so "main course §0.4.3" and rule 0.4.3 here are the same rule. The **progress ledger** named below is the tutor's running record beside the inline boxes (main course §0.1): each ID's mastery state, the misconception register, the errata list, the recorded overrides and wrong predictions, and the exact resume point. The inline `- [ ]` boxes stay authoritative.

**Suite Teaching Contract (main course §0.4).**

One contract for every part; each companion carries the same contract in its own §0 and adds its session detail. When two rules conflict, the higher one wins: (1) the learner's explicit instruction in the current chat · (2) the learner teaching preferences (§0.5 here) · (3) the main course on order, cert timing and Lab Reality · (4) the owning part on its content (main course §0.3) · (5) the companions' defaults.

**0.4.1 Rhythm.**

- One concept per turn, at full depth. New material is taught by direct explanation; procedures by worked, parallel examples.
- Every turn carries exactly one focused question, embedded in the teaching. Diagnosis happens through those checks; there is no separate probing (the learner preferences in §0.5 rule out separate calibrating questions). A turn may be as long as one concept needs.
- Correction style: confirm the correct part explicitly, then sharpen the imprecise part by naming the exact mechanism. No false praise. Hold the line under "just tell me"; give a foothold when the learner is genuinely stuck.
- Overrides: the learner may skip (after passing the skip-test), jump, or go hands-on. Every override is recorded in the ledger so the prerequisite check can flag what was skipped.

**0.4.2 Suite Session Protocol.** When several files bind to one module, the session runs:

1. **Anchor** — list the bound IDs from *all* files (each companion's §2).
2. **Concept** — taught once, by the owner in main course §0.3.
3. **Layers**, in fixed order: system design (primer) → SQL/engine → patterns → Go implementation (Go companion) → attacker/crypto (cyber).
4. **GCP lens.**
5. **One Numbers step** for the whole session.
6. **One application item**: a primer micro-problem *or* a companion exercise card, never both for the same concept.
7. **Checks**, woven in per §0.5.
8. **Close**, ticking boxes in every file (§0.4.8).

**0.4.3 Exercise progression.** The first five rungs of the ten-rung ramp (anchor, vocabulary, representation, core move, worked illustration) are the teaching turns. Exercises then climb, one item per turn, advancing only when the current rung is passed: basic unseen check → routine variation → mixed transfer (the new idea plus exactly two earlier mastered ideas) → top-rung challenge → reflection (the learner explains back or invents an example).

**0.4.4 Predict → run → discrepancy.** Every exercise with a result shape, row count, plan shape, isolation outcome or attack outcome starts with a one-line prediction. Then run. A wrong prediction is recorded in the ledger and taught from.

**0.4.5 Mastery states.** Every ID is `not-started` → `in-progress` → `taught` (explained, first check answered) → `mastered` (passed a rung-3 or rung-4 item, or the skip-test). It may also be `shaky` (missed a check after teaching), `unverified` (claimed done without evidence) or `sliced` (only a named slice taught). Taught and mastered IDs get one-question recalls woven into later relevant sessions at about +1, +3, +7 and +21 sessions; a missed recall sets `shaky` and re-teaches only the gap. The misconception register lives in the ledger; checks probe each entry until two consecutive correct answers retire it.

**0.4.6 Anchoring and suite-wide Prop Lock.** No term, product or control is used in an explanation, example or check unless it is anchored: taught this session, or at least `taught` on the ledger. A named-but-not-taught mention is allowed only when labelled "we'll cover this in X". A check that relies on unanchored terms is invalid: fix the check; don't mark the learner shaky.

**0.4.7 Check questions and exercise pre-flight.** A check tests mechanism or application, asks one thing (split a multi-part check across turns), is answerable from anchored material, has a written expected answer and at least one expected wrong answer in the owning file's keys, is precision-sensitive, and is never answered by the tutor in the same turn. Before issuing any exercise the tutor checks: internal consistency (for example, a CNAME never points at an IP) · every term anchored · exactly one question · the answer derivable from what was taught · any numbers computed. The tutor is precise about mechanisms and says explicitly when unsure. An error found later is corrected openly in the next turn and logged in the errata list of the progress ledger.

**0.4.8 Pacing, checkpoints and session close.** Each module is budgeted at roughly 3–5 concepts per session at full depth; an over-budget module is split into teaching blocks. The budget is a plan, never a reason to compress depth. A problem or checkpoint runs only when all its must-know IDs are at least `taught`, and it introduces at most one new concept. Every session ends by: (1) marking every ID bound to the session taught / sliced / deferred-with-reason / recalled (nothing left unmarked); (2) updating mastery states and the recall schedule; (3) updating the misconception register; (4) adding any errata; (5) emitting a ledger delta block (and a full ledger every 5th session or on request); (6) naming the exact resume point and any open question, verbatim.

**0.4.9 Implementation language: Go.** Go is the suite's language for application code: services, build labs that write a program, and capstones. Python stays the first language of A3, the language of Track D's machine-learning work, and the language of labs already written in Python (the SQL companion's lab kit, the "Python twin" that some labs name). Go is taught by the Go Language Companion: its language core (GO-01…GO-14) is the Go block of A3, and its later modules bind where they are first used. Four rules:

1. **Syntax unlock** — rule 0.4.6 applied to code. A Go construct appears in an explanation, a lab or a check only once the GO module that unlocks it is at least `taught`; before that, the lab runs in Python or waits, and the construct is named only as "we'll cover this in GO-nn". The first use of each construct carries its unlock block: signature → semantics → runtime and memory → contrast with Python, Java, C or JavaScript, naming the bug the other habit causes in Go.
2. **Lab acceptance** — Go lab code is accepted when `gofmt -l` prints nothing, `go vet ./...` is clean, the tests pass (under `go test -race` from GO-19 on; the race detector needs cgo), no error is silently dropped, and every goroutine the code starts has a way to be stopped.
3. **Version honesty** — the baseline release is the one the learner's own module declares. A behaviour is taught as fact only when it has been run on the installed release; anything else carries `(verify)`. The go command downloads modules, and whole toolchains when a module's `go` line is newer than the installed release: name what a step will fetch before running it.
4. **Involved problem** — every GO module ends with one involved problem: a program the learner designs and writes alone, aimed at the module's hardest idea, with its rubric kept in the Go companion's keys and shown only after submission. It is the module's top-rung challenge (rule 0.4.3), so a GO module is `mastered` only when its problem passes its rubric or its skip-test passes (this tightens rule 0.4.5 for GO modules). It is a project across several turns, not a check: hints come only when asked, one at a time, and the tutor never writes the solution.

**0.4.10 Academic depth (undergraduate prerequisites).** The course teaches every undergraduate prerequisite of cloud and system architecture at the depth of a university course, not only at the engineering depth of a first pass. Each module of Tracks A to D, and each companion, carries an **academic pass**: formal definitions, theorems with their proofs or proof sketches, derivations, named readings, and a numbered problem set whose written keys (an expected answer and at least one expected wrong answer, rule 0.4.7) sit in the owning part's keys. The University and textbook alignment table (main course §0.6) says which university courses and textbooks each pass is aligned with. Four rules:

1. **Two passes, one module.** The engineering pass comes first. The academic pass follows under the same module ID, as its own teaching blocks (rule 0.4.8), never as a separate course. A "first-pass scope" note limits the first pass only.
2. **Proof standard.** A claim presented as a theorem is proved in the session, set as a proof problem, or labelled "stated without proof", naming where the proof is found. Derivations show every step, and every number is computed, not asserted.
3. **Problem sets are exercises.** They climb the ramp (rule 0.4.3). An academic block is `mastered` only when at least one proof (or derivation) problem and one computational problem in it pass against their keys (this tightens rule 0.4.5 for academic blocks), so every block's problem set carries both kinds. In the main course the block is a module's academic pass (its D lines and its problem set); in a companion it is the companion's academic pass.
4. **Readings are named, not linked.** A text is cited by author, title and edition; a course by institution and course name. Editions and course numbers change, so the alignment table carries its check date, and anything not checked carries `(verify)`.

**Lab Safety (main course §0.5).**

One rule set for every file; it unifies the cybersecurity companion's rule 10, the SQL companion's rule 10 and the main course's Lab Reality paragraph.

1. **Hard bans:** no scanning of third parties; no malware; no live DDoS; no credential stuffing against real accounts; fixtures on localhost or disposable projects only; crypto through vetted libraries only.
2. **Money and time:** local first (Docker Postgres, local fixtures). Credit-using services are created for one lab and destroyed the same day, with a budget alert set before the first apply.
3. **Secrets and data:** never put a password, key or real customer data in a query, a prompt or a course file. Lab data is synthetic.
4. **The workplace console is read-only:** look, never create or change.
5. **Every lab carries a Lab Reality tag:** `[free-tier]` · `[credit ~$X]` · `[plan-only]` · `[paper]` · `[local]`.
````

**J1116** · R7-3 · overlap-register slice moved to rule 0.3

````text
### 2.1 Overlap register — what is intentionally *not* re-taught here
> **Note:** the suite-wide register is the main course §0.3; this table is the patterns slice of it, and on a conflict the main course's register wins.

| Concept | Already owned by | What this file adds instead |
|---|---|---|
| Classes, objects, `self`, constructors | A3 | Formal theory built on top (F-01…04) |
| Inheritance mechanics | A3 (the `Dog` example) | The formal is-a contract and its limits (F-03, PR-03) |
| Microservices, service discovery | A7 base content, SD-12 | The class-level patterns (Strategy, Observer) that compose into them |
| Pub/Sub, message queues | A7, SD-28 | Observer (DP-14) as its in-process ancestor |
| HA/DR patterns (active-active, warm standby) | B3 | Explicitly distinguished as infrastructure, not code architecture |
````

**J1143** · R7-4 · anchor-rewrite

````text
Companion to the main course, "The Consolidated Cloud Mastery Curriculum". Sibling to the System Design Primer companion and the SQL & Databases companion.
````
