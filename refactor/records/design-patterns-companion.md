# Records for design-patterns-companion.md (R2b, 2026-09-24)

Refactor bookkeeping only, not course material. Decision D6 keeps provenance, the D3 archive and every line R2b changed or removed out of the course files; decision D3 keeps them here, verbatim. Each entry names the R2b journal number (outputs/r2b/journal.jsonl), the rule and the class.

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

**J624** · DP-1 · anchor-rewrite

````text
Companion to `Curriculum` ("The Consolidated Cloud Mastery Curriculum"). Sibling to `system-design-primer-companion.md` and `sql-databases-companion.md`.
````

**J625** · DP-1 · anchor-rewrite

````text
When other companions bind to the same session, the Suite Session Protocol in `Curriculum` §0.4 governs.
````

**J627** · DP-3 · anchor-rewrite

````text
| **A7 — Software Architecture & APIs** | **Everything in this file**, in order: F-01…04, then PR-01…14, then DP-01…23, then ARCH-01…08, then AP-01…10. ARCH-09…12 are taught in the A9 session (next row). `Curriculum` A7 splits this into teaching blocks A7.3–A7.7 | Primary landing module — flagged as a curriculum gap during the A5 networking session, filled here |
````

**J628** · DP-3 · anchor-rewrite

````text
> **Note:** the suite-wide register is `Curriculum` §0.3; this table is the patterns slice of it, and on a conflict the main course's register wins.
````
