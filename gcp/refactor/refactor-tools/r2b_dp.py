"""R2b per-file rules for the design-patterns companion. Learner decisions D6, D10, D11.

Sibling parts are named by title, the shared contract is copied into §0.6, and every remaining backticked
`Curriculum` becomes "the main course".
"""
from r2b_shared import contract_copy, parent_name

EV6 = "D6: no file names, links or file dependencies in course text"
EV11 = "D11: the file-style parent name becomes 'the main course'; IDs stay as stitch tags"


def build(f, files):
    f.rep("DP-1", "anchor-rewrite", 'Companion to `Curriculum` ("The Consolidated Cloud Mastery Curriculum"). Sibling to '
          '`system-design-primer-companion.md` and `sql-databases-companion.md`.',
          'Companion to the main course, "The Consolidated Cloud Mastery Curriculum". Sibling to the System Design '
          'Primer companion and the SQL & Databases companion.', EV6 + "; " + EV11)
    f.rep("DP-1", "anchor-rewrite", "the Suite Session Protocol in `Curriculum` §0.4 governs.",
          "the Suite Session Protocol (rule 0.4.2 in §0.6) governs.", EV6 + " (the contract is copied into §0.6)")
    # the shared contract and Lab Safety, right after the preferences (§0.5)
    h = f.heading("0.5 Learner teaching preferences")
    e = f.section_end(h)
    while f.L[e - 1].strip() in ("", "---"):
        e -= 1
    f.ins("DP-2", e, [""] + contract_copy(files, 5, 6), "D6: each part carries the shared teaching rules in its own "
          "§0 (D7 exemption: rules, not topics)", cls="append")
    parent_name(f, "DP-3")
