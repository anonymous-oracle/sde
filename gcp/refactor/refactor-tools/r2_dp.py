"""R2 repairs for `design-patterns-companion.md` (C-16, C-29, C-58, C-60, C-62, C-64, §7, invariant 4).

C-59 (per-item Checks), C-61 (named real examples) and the rest of C-64's parity work are R7 content, not R2.
"""
import re

from r2_common import C29_POINTER, PREFS_HEAD, note


def build_dp(d, prefs):
    # ---------- §0 ----------
    i = d.one("7. **Close** — tick the box; note anything shaky for a later recall.")
    d.insert_after("C-29", "append", i, ["", C29_POINTER], "C-29 pointer")
    i = d.one("`PR-nn` SOLID/GRASP principles · `DP-nn` GoF design patterns")
    d.replace_line("C-64", "correction", i, "`F-nn` OOP foundations · " + d.L[i],
                   "C-64: the notation line omitted F-01…F-04, which §1 and §3 define", what="§0.4 notation")
    d.insert_after("INV-4", "new-content", i, ["", "### 0.5 " + PREFS_HEAD, ""] + prefs,
                   "invariant 4: ledger §5 preferences copied unchanged")

    # ---------- §2 (C-16) + §2.1 pointer ----------
    i = d.one("| **A7 — Software Architecture & APIs** | **Everything in this file**, in order:")
    old = "then ARCH-01…12 (minus ARCH-09…12 if A9 isn't done yet), then AP-01…10"
    assert old in d.L[i]
    d.replace_line("C-16", "correction", i, d.L[i].replace(
        old, "then ARCH-01…08, then AP-01…10. ARCH-09…12 are taught in the A9 session (next row; C-16). `Curriculum` "
             "A7 splits this into teaching blocks A7.3–A7.7 (C-49)"),
        "C-16: the table bound everything to A7 while §10 gates ARCH-09…12 behind A9", what="§2 A7 row")
    i = d.one("| Concept | Already owned by | What this file adds instead |")
    d.insert("§7", "append", i, [note("§7", "the suite-wide register is `Curriculum` §0.3; this table is the "
             "patterns slice of it, and on a conflict §0.3 wins."), ""], "§7 register → Curriculum §0.3")

    # ---------- C-60 ----------
    i = d.one("Format per pattern: **Intent** (GoF's own line)")
    d.replace_line("C-60", "correction", i, d.L[i].replace("**Intent** (GoF's own line)",
                   "**Intent** (paraphrased from GoF)"),
                   "C-60: §11 says the Intent lines are close paraphrases; the per-line audit is R7",
                   what="§6 format line")

    # ---------- C-62 ----------
    i = d.one("- **Repository:** collection-like access to Aggregates, hiding persistence (PR-12 in action).")
    d.insert_after("C-62", "append", i, [
        "  - *Owner pointer (C-62):* Repository's definition is owned by ARCH-07 (Fowler, PoEAA). Here, recall it in "
        "one line and add the DDD constraint: one repository per aggregate root."], "C-62 resolution")

    # ---------- C-58: inline boxes ----------
    n = 0
    k = 0
    while k < len(d.L):
        l = d.L[k]
        m = (re.match(r"^#### ((?:F|PR)-\d{2}) · ", l) or re.match(r"^\*\*(DP-\d{2}) · ", l)
             or re.match(r"^\*\*(ARCH-\d{2}) · ", l))
        if m:
            d.insert_after("C-58", "append", k, [f"- [ ] {m.group(1)}"], "C-58: one inline box per item")
            n += 1
            k += 1
        k += 1
    i = d.one("- **PR-14 Protected Variations:**")
    d.insert_after("C-58", "append", i, ["", "- [ ] " + " · [ ] ".join(f"PR-{x:02d}" for x in range(6, 15))],
                   "C-58: one inline box per GRASP item")
    i = d.one("- **AP-10 Interface Bloat:**")
    d.insert_after("C-58", "append", i, ["", "- [ ] " + " · [ ] ".join(f"AP-{x:02d}" for x in range(1, 11))],
                   "C-58: one inline box per anti-pattern")
    assert n == 4 + 5 + 23 + 12, n
    return d
