"""R2b per-file rules for the main course (Curriculum.md). Learner decisions D5, D6, D9, D10, D11.

Each rule removes a pointer to an outside file, a Northstar pointer, the file-style parent name or refactor
bookkeeping, and keeps the material it pointed to inside the course (the text it pointed to is already inline, or
is written here).
"""
from r2b_common import F  # noqa: F401

EV6 = "D6: no file names, links or file dependencies in course text"
EV5 = "D5: Northstar and every N pointer are deleted"
EV11 = "D11: the file-style parent name becomes 'the main course'; IDs stay as stitch tags"

TITLE_PRI = "The System Design Primer Companion — GCP-Native Edition"
TITLE_SQL = "The SQL & Databases Companion — GCP-Native Edition"
TITLE_DP = "Design Patterns, SOLID & Clean Architecture — A Companion Curriculum"
TITLE_SEC = "The Cloud Cybersecurity Companion"

S01 = [
    "### 0.1 The course parts and the companion stitch rule",
    "",
    "This course is one course in five parts. This roadmap, the **main course**, is the **only parent**: every "
    "companion binds its modules to the IDs below, and a module ID from any part may be used as a stitch tag in any "
    "other part. The parts:",
    "",
    "- **The Consolidated Cloud Mastery Curriculum** (this part, the main course) — order, cert timing, Lab Reality "
    "and track structure.",
    f"- **{TITLE_PRI}** — the system-design layer (SD, SX, P, O, Q, TF). Its §2 stitch table binds its IDs to the "
    "modules here.",
    f"- **{TITLE_SQL}** — SQL, relational theory and engine internals. It owns the engine slices DB-1…DB-10.",
    f"- **{TITLE_DP}** — OOP design theory, patterns and architecture styles (A7, A9).",
    f"- **{TITLE_SEC}** — security, attacks and cryptography.",
    "",
    "Progress lives in the inline `- [ ]` boxes of the five parts, which are authoritative. The tutor also keeps a "
    "**progress ledger**, a running record beside the boxes: each ID's mastery state (§0.4.5), the misconception "
    "register, the errata list, the recorded overrides and wrong predictions, and the exact resume point (§0.4.8).",
    "",
    "Each companion's §2 lists what it binds to each module. When a module is taught, every bound companion ID is "
    "taught in the same session, once, by its owner (§0.3), in the order §0.4 gives. The cybersecurity stitch rule, "
    "first added to this roadmap on 2026-09-22 between A10 and A11:",
    "",
    "---",
    "",
    "#### Companion — Cloud Cybersecurity",
    "",
    f"**Standing stitch rule.** Teach security-relevant sections of this roadmap with **{TITLE_SEC}**. Whenever "
    "**A5**, **A7 (auth patterns)**, **A10**, **B1 (shared responsibility)**, **B5**, **C1/C2 hardening**, "
    "**Phase 4 Networking/Security**, or the **Cloud Security / Network / SecOps** cert tracks are taught, also "
    "teach every companion module bound in companion **§2** in the **same session** — one story, never twice.",
    "",
    "That companion owns attack mechanics, network/cloud cybersecurity, cryptography (`CR-*`), and the exercise "
    "bank; where a concept is shared with another part, the overlap register (§0.3) names the owner. This roadmap "
    "still owns order, cert mapping, and service vocabulary.",
    "",
    "**Lab safety:** local vulnerable-by-design fixtures only; no live DDoS, third-party scanning, malware, or "
    "credential stuffing against real accounts. The full rule set is §0.5.",
    "",
    "---",
]


def build(f, files):
    # cert notes: the verification text is already inline; only the pointer to the outside record goes
    f.rep("CUR-1", "anchor-rewrite", " (D4; `cert-verification.md`)", "", EV6, n=18)

    # §0.1: the part list names each part by title; Northstar and the ledger file leave (D5, D6)
    s = f.heading("0.1 The course files and the companion stitch rule")
    e = f.heading("0.2 Learner teaching preferences")
    while f.L[e - 1].strip() == "":
        e -= 1
    f.block("CUR-2", "anchor-rewrite", s, e, S01, EV6 + "; " + EV5 + "; " + EV11,
            what="§0.1 part list and cyber stitch block (file names, link, Northstar, superseded notes)")

    # §0.3 register: the parent's owner cells carry the bare module ID
    s = f.heading("0.3 Suite overlap and ownership register")
    e = f.section_end(s)
    f.rx("CUR-3", "anchor-rewrite", r"`Curriculum` (?=[A-Z])", "", EV11, lo=s, hi=e, mn=13, mx=13)
    f.rep("CUR-3", "anchor-rewrite", "| SQL OD-04 (runbook) + N2.3 |",
          "| SQL OD-04 (runbook) + OD-11 (Cloud SQL backups and PITR) |", EV5 + "; the Cloud SQL operations "
          "material the N-pointer named is written into the SQL companion as OD-11 (D9)")
    f.rep("CUR-3", "anchor-rewrite", "; the A2 slice (`primer-binding-table.md`) |",
          "; the A2 slice (primer §2 stitch table) |", EV6)
    f.rep("CUR-3", "anchor-rewrite", "| Northstar milestones cite P08 steps; Track S4/S9 recall |",
          "| Track S4/S9 recall |", EV5)
    f.rep("CUR-3", "anchor-rewrite", "| SQL TF-DB*; Northstar reuses TF IDs rather than duplicating |",
          "| SQL TF-DB1…TF-DB6 |", EV5)

    # §0.4 contract: no outside files in the precedence list or the rules
    f.rep("CUR-4", "anchor-rewrite",
          "One contract for every file. Each companion keeps its own §0.3 session text and points here. When two rules "
          "conflict, the higher one wins: (1) the learner's explicit instruction in the current chat · (2) the ledger "
          "§5 preferences (§0.2) · (3) the refactor invariants · (4) this file on order, cert timing and Lab Reality "
          "· (5) the owning companion on its content (§0.3) · (6) the companions' defaults · (7) `learn-SKILL.md` "
          "defaults.",
          "One contract for every part; each companion carries the same contract in its own §0 and adds its session "
          "detail. When two rules conflict, the higher one wins: (1) the learner's explicit instruction in the "
          "current chat · (2) the learner teaching preferences (§0.2) · (3) this main course on order, cert timing "
          "and Lab Reality · (4) the owning part on its content (§0.3) · (5) the companions' defaults.",
          EV6 + "; D10: no rule comes from an outside file")
    f.rep("CUR-4", "anchor-rewrite", "(ledger §5 wins over the skill's calibrating question)",
          "(the learner preferences in §0.2 rule out separate calibrating questions)", EV6)
    f.rep("CUR-4", "anchor-rewrite", "(each companion's §2; the primer's from `primer-binding-table.md`)",
          "(each companion's §2)", EV6)
    f.rep("CUR-4", "anchor-rewrite", "woven in per ledger §5.", "woven in per §0.2.", EV6)
    f.rep("CUR-4", "anchor-rewrite", "logged in `errata.md`.", "logged in the errata list of the progress ledger.",
          EV6)

    # status notes: the fresh-start fact stays, the ledger-file pointer goes
    f.rep("CUR-5", "anchor-rewrite",
          "> **Note:** Status as of 2026-09-24 (C-20, D2): the course is a fresh start, so this sentence is still "
          "true. The live position is kept in `session-progress-ledger.md`.",
          "> **Note:** Status as of 2026-09-24: the course is a fresh start, so this sentence is still true.",
          EV6, n=2)

    # A7 teaching blocks: the Northstar block leaves; no phase names in course text
    f.rep("CUR-6", "anchor-rewrite",
          " · A7.10 S1–S2 · A7.11 N0 · A7.12 checkpoints. A5, A8 and A10 get the same split in R4, from the §0.4.8 "
          "pacing budget.",
          " · A7.10 S1–S2 · A7.11 checkpoints. A5, A8 and A10 get the same split, from the §0.4.8 pacing budget, "
          "when they are taught.", EV5 + "; " + EV6)
    f.rep("CUR-6", "anchor-rewrite", "owned and taught by `sql-databases-companion.md` §4.0 inside the A8 sessions",
          "owned and taught by the SQL companion (§4.0) inside the A8 sessions", EV6)

    # reserved tracks: Track N leaves (D5); the stubs say plainly that they hold scope, not material (D11)
    f.line("CUR-7", "anchor-rewrite", "### Reserved tracks M, U, S and N (stubs; authored in R4 and R9)",
           "### Reserved tracks M, U and S (stubs)", EV5)
    f.line("CUR-7", "anchor-rewrite", "The companions' foreign anchors were rebound to these IDs by the §6 crosswalks",
           "The companions anchor to these IDs. Each ID is reserved here with its scope; the modules themselves are "
           "not written yet, so nothing here is teaching content yet. Until a module is written, a pointer to it "
           "names its scope only: say so plainly (§0.2) and teach the concept from the part that owns it in §0.3.",
           EV6 + "; D11: a pointer to a place lacking the material is disclosed, not hidden")
    f.line("CUR-7", "move", "| N0…N12 | Northstar reference application |", [], EV5)

    f.rep("CUR-8", "anchor-rewrite", "*Category IDs (C-22, 2026-09-24).* Other files anchor to these IDs",
          "*Category IDs.* The companions anchor to these IDs", EV6)
    f.rep("CUR-8", "anchor-rewrite",
          "the three notes below were re-checked that day (`cert-verification.md`). New dated items are in the Part "
          "V–VII verification notes. R4 moves every date-bearing line into `volatility-register.md` with a "
          "last-checked date.",
          "the three notes below were re-checked that day against the vendors' live pages. New dated items are in "
          "the Part V–VII verification notes.", EV6)
