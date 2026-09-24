"""R2b per-file rules for the System Design Primer companion. Learner decisions D5, D6, D10, D11.

The CC BY 4.0 source line and its link stay (license requirement); the change notice stays in words, because the
license asks that changes be indicated, but it no longer names an outside file.
"""
from r2b_shared import contract_copy

EV6 = "D6: no file names, links or file dependencies in course text"
EV5 = "D5: Northstar and every N pointer are deleted"
EV11 = "D11: the file-style parent name becomes 'the main course'; IDs stay as stitch tags"


def build(f, files):
    f.rep("PRI-1", "anchor-rewrite", 'Companion to `Curriculum` ("The Consolidated Cloud Mastery Curriculum")',
          'Companion to the main course, "The Consolidated Cloud Mastery Curriculum"', EV11)
    f.line("PRI-1", "anchor-rewrite", "Modified by the curriculum refactor on 2026-09-24; changes listed in CHANGELOG.md.",
           "Modified on 2026-09-24, when this companion was fitted into the five-part course.",
           EV6 + "; CC BY 4.0 asks that changes be indicated, so the notice stays in words")
    f.rep("PRI-2", "anchor-rewrite", "**This file is a complement to `Curriculum`, not a second curriculum.",
          "**This file is a complement to the main course, not a second curriculum.", EV11)
    f.line("PRI-2", "anchor-rewrite", "   *Exception (added by the refactor):* `session-progress-ledger.md` is the single",
           "   *Exception:* the tutor's progress ledger (main course §0.1) is a running record beside these boxes, not "
           "a separate tracker; the inline `- [ ]` ticks remain authoritative.", EV6)
    f.rep("PRI-2", "anchor-rewrite", "the Suite Session Protocol in `Curriculum` §0.4 governs.",
          "the Suite Session Protocol (rule 0.4.2 in §0.6) governs.", EV6 + " (the contract is copied into §0.6)")
    f.line("PRI-3", "anchor-rewrite", "- `V-COMP, V-STOR, V-NET, V-DATA, V-AI, V-SEC, V-OPS` — `Curriculum` Part V",
           "- `V-COMP, V-STOR, V-NET, V-DATA, V-AI, V-SEC, V-OPS` — the main course's Part V service-map categories. "
           "`M1…M6`, `U1…U7`, `S1…S11` — the main course's reserved tracks (scope stubs; its reserved-tracks table "
           "says what each covers).", EV5 + "; " + EV6 + "; " + EV11)
    f.rep("PRI-3", "anchor-rewrite", "The single source is `primer-binding-table.md`; the header stitches, §2 and §4.5 "
          "are generated from it.", "§2 is the single source; the header stitches and §4.5 agree with it.", EV6)
    f.line("PRI-4", "anchor-rewrite", "*Generated from `primer-binding-table.md` (2026-09-24).* Columns:",
           "Columns: PRIMARY = the session that teaches the concept in full; slices = one named ingredient taught "
           "earlier (or a continuation after); recalls = a one-line reference back; also in this session = the "
           "problem-level work (and, for V rows, the Lens-3 service wording) that rides in the same session.", EV6)
    f.rep("PRI-4", "anchor-rewrite", "Suite-wide ownership lives in the register in `Curriculum` §0.3",
          "Suite-wide ownership lives in the register in the main course §0.3", EV11)
    f.rep("PRI-4", "anchor-rewrite", "in transit → `Curriculum` A5 TLS", "in transit → A5 TLS", EV11)
    f.rep("PRI-4", "anchor-rewrite", "reads as: `Curriculum` A8 gives the CAP statement", "reads as: A8 gives the CAP "
          "statement", EV11)
    f.rep("PRI-4", "anchor-rewrite", " The checked order is in `primer-binding-table.md` §2.", " The checked order is "
          "§2 of this file.", EV6)
    f.rep("PRI-4", "anchor-rewrite", "cross-reference design-patterns AP-01…AP-10 (`design-patterns-companion.md` §8)",
          "cross-reference design-patterns AP-01…AP-10 (the design-patterns companion, §8)", EV6)
    f.line("PRI-4", "anchor-rewrite", "*Column 2 of the Phase 0–4 rows is generated from `primer-binding-table.md`",
           "*Column 2 of the Phase 0–4 rows: `ID[slice]` = a named ingredient taught before the concept's full "
           "session; `ID~` = recall.*", EV6)
    # the shared contract and Lab Safety, right after the preferences (§0.5)
    h = f.heading("0.5 Learner teaching preferences")
    e = f.section_end(h)
    while f.L[e - 1].strip() in ("", "---"):
        e -= 1
    f.ins("PRI-5", e, [""] + contract_copy(files, 5, 6), "D6: each part carries the shared teaching rules in its own "
          "§0 (D7 exemption: rules, not topics)", cls="append")

    # SD-25 is the one home of the store-choice map (D7); the legacy storage map's remaining facts fill it (D9, D10)
    ev = "D9 + D7: SD-25 is the store-choice home; a missing store row and the anti-choices are added (facts only)"
    f.ins_after("PRI-6", "| Blobs | Cloud Storage |", ["| Shared POSIX files (NFS) for GKE pods or VMs | Filestore |"], ev)
    f.ins_after("PRI-6", "  Primer examples → GCP: clickstream/logs", [
        "  Anti-choices (each is a common wrong answer): Memorystore is never the system of record for money or "
        "orders (a cache can lose writes on failover); BigQuery is never on the checkout path (an analytics warehouse, "
        "not an OLTP store); Filestore and Cloud Storage are never a database (no transactions, no queries); Bigtable "
        "is never chosen for ad-hoc joins (single-row lookups and range scans only)."], ev)
