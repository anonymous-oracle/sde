# Session Progress Ledger — the main course and its five companions
Regenerated on 2026-09-24 as a clean template. The learner chose a fresh start (decision D2), so nothing from the earlier ledger counts as done: every module and card begins `not-started`. The earlier ledger's standing teaching preferences are kept word for word (§5). Upload this file alongside the six parts of the course: the main course (The Consolidated Cloud Mastery Curriculum) and its five companions (System Design Primer, SQL & Databases, Design Patterns, Cloud Cybersecurity, Go Language).

---

## 0. How to use this file (read first, in the new chat)

1. This is a **status file, not a transcript.** It records what is done, what is shaky and exactly where to pick up. Re-derive explanations fresh.
2. Continue in **`/learn` mode**, following the main course's §0.4 teaching contract, which every companion copies.
3. **The resume point is §4.** Start there.
4. **The teaching preferences in §5 are binding.** Follow them without re-asking.
5. **The fenced YAML block in §8 is the source of truth for scripts.** The prose sections restate it for a human reader. At each session close, emit a ledger delta block in the same YAML shape (main course rule 0.4.8), and regenerate the whole file every fifth session or when asked.

---

## 1. The six parts this ledger tracks

| Part | Role |
|---|---|
| The Consolidated Cloud Mastery Curriculum (the main course) | The spine: Track A (A1–A11) → Track B → Track C → Track D → certifications. Authoritative on order and scope. |
| The System Design Primer Companion | SD, SX, P, O and Q cards, stitched into the main-course modules its §2 names. |
| The SQL & Databases Companion | Relational theory and SQL depth, stitched into the main-course modules its §2 names; carries its own lab kit. |
| Design Patterns, SOLID & Clean Architecture | F, PR, GRASP, DP, ARCH and AP cards, stitched into A7 and later modules as its §2 names. |
| The Cloud Cybersecurity Companion | Security cards and labs, stitched into the modules its §2 names. |
| The Go Language Companion | GO cards, taught beside the modules its §2 names. |

---

## 2. Learner profile

- Blank under the fresh start. Fill it at session close from what the sessions show, never from the earlier ledger.

---

## 3. Done (recall only, do not re-teach)

- None yet.

---

## 4. Resume point ← start here

- **Module:** A1 — Digital Logic & Data Representation.
- **First concept:** "Bits, bytes, binary and hexadecimal number systems; why computers use base-2"
- **Open question carried over:** none.

---

## 5. Standing teaching preferences confirmed this session (binding — don't re-ask)

- **Check questions must be woven into the concept explanation itself**, not asked as separate "what do you already know" diagnostics — the learner explicitly opted out of background-probing questions and asked for calibration to happen through how they handle the material.
- **"Maintain curriculum depth and academic rigour"** has been repeated multiple times as an explicit standing instruction — do not compress, simplify, or skip the "why," even under time pressure or a fast pace of correct answers.
- When companion-file content (system-design-primer, SQL, design-patterns) overlaps a `Curriculum` module, **teach it once, stitched into the same session** — never as a separate pass, per each companion's own §0.2 stitching rules.
- If a companion file references module IDs that don't exist in `Curriculum` (as `sql-databases-companion.md` does), **say so plainly rather than forcing a silent, possibly-wrong mapping** — this was well received when done for the SQL companion.

---

## 6. Checkpoints waiting (all not-started)

Each checkpoint is taught where its part's §2 places it. They are listed here so none is missed.

- **At A4:** O01, O02 and O07, the primer's recall checkpoints.
- **At A5:** the primer's P08 checkpoint, limited to the single box and the Users++ networking slice; the cybersecurity companion's A5 labs SEC-E4.21 and CR-E12.
- **After A6:** the P08 first pass, the full outline.
- **At A7:** O03 (after DP-18 and DP-16), O04, O05 (after F-01…F-04 and PR-01…PR-05), O06.
- **After A7 and A8:** P01.

---

## 7. Open items

- None. Record new ones at session close.

---

## 8. Machine-readable block

```yaml
ledger_version: 2
as_of: 2026-09-24
learner:
  preferences:        # §5, verbatim strings
    - '**Check questions must be woven into the concept explanation itself**, not asked as separate "what do you already know" diagnostics — the learner explicitly opted out of background-probing questions and asked for calibration to happen through how they handle the material.'
    - '**"Maintain curriculum depth and academic rigour"** has been repeated multiple times as an explicit standing instruction — do not compress, simplify, or skip the "why," even under time pressure or a fast pace of correct answers.'
    - 'When companion-file content (system-design-primer, SQL, design-patterns) overlaps a `Curriculum` module, **teach it once, stitched into the same session** — never as a separate pass, per each companion''s own §0.2 stitching rules.'
    - 'If a companion file references module IDs that don''t exist in `Curriculum` (as `sql-databases-companion.md` does), **say so plainly rather than forcing a silent, possibly-wrong mapping** — this was well received when done for the SQL companion.'
  error_pattern: null # fresh start: the earlier pattern is not carried over
position:
  module: A1
  block: null         # A1 has no teaching-block split; its academic pass (A1.D) follows the engineering lines
  resume_concept: "Bits, bytes, binary and hexadecimal number systems; why computers use base-2"
  open_question: null
ids:                  # the checkpoints of §6; every other ID is not-started by default
  O01: {state: not-started, at: A4}
  O02: {state: not-started, at: A4}
  O07: {state: not-started, at: A4}
  P08: {state: not-started, at: A5, slice: "single box + Users++ networking slice; first pass after A6"}
  SEC-E4.21: {state: not-started, at: A5}
  CR-E12: {state: not-started, at: A5}
  O03: {state: not-started, at: A7, after: [DP-18, DP-16]}
  O04: {state: not-started, at: A7}
  O05: {state: not-started, at: A7, after: [F-01, F-02, F-03, F-04, PR-01, PR-02, PR-03, PR-04, PR-05]}
  O06: {state: not-started, at: A7}
  P01: {state: not-started, at: A8}
misconceptions: []
overrides: []
errata_refs: []
```
