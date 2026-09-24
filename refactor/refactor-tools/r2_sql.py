"""R2 repairs for `sql-databases-companion.md` (C-01, C-02, C-05, C-08, C-29, C-37, C-53, C-57, §6.1, invariant 4).

Foreign-parent labels (`gcp-curriculum.md` numbering, `T.*`, `F1`, `D1`…) are rebound through the §6.1 crosswalk in
FOREIGN below. Anchor rewrites keep their originals in the journal and in `crosswalk.md`; lines whose *meaning* changes
(ownership statements) are corrections and keep their pre-refactor text in the D3 archive.
"""
import os
import re

from r2_common import C29_POINTER, DATE, PREFS_HEAD, note

SRC_PARENT = "gcp-curriculum.md"

# §6.1 crosswalk (+ C-53, §6.3). Value: the new anchors, in order.
FOREIGN = {
    "T.Disc": ["M1"], "T.Algo": ["A4", "U2"], "T.Quant": ["A1/A2 recall", "M6"], "M.NS": ["M5"],
    "T.SysTheory": ["A8", "A9", "U5"], "F1": ["A3", "A6"], "D1": ["C1"], "1.2": ["C1"], "D2": ["C4"],
    "D3": ["C4", "C5"], "D7": ["C5"], "0.4": ["S2", "N0.4"], "0.5": ["B5"], "1.7": ["C6"], "1.12": ["B3"],
    "2.1": ["A8"], "2.2": ["A8", "V-STOR"], "2.3": ["N2.3"], "2.4": ["A8", "N2.4"], "2.5": ["N2.5"],
    "2.6": ["A8", "C4", "N2.6"], "2.7": ["A9", "V-STOR", "N2.7"], "3.0": ["A7"], "3.4": ["A7"],
    "3.5": ["A9", "ARCH-11"], "4.7": ["A10", "B5"], "4.9": ["C1", "Phase 4 Security"], "5.3": ["A8", "N5.3"],
    "7.3": ["Phase 4 Security", "N7.3"], "8.0": ["S2", "N8.0"], "8.C": ["S2", "N8.C"], "8.1": ["N8.1"],
    "8.1.5": ["N8.1.5"], "9.1": ["V-STOR", "N9.1"], "9.4": ["V-STOR", "N9.4"], "9b.1": ["V-DATA", "N9b.1"],
    "9c.1": ["D3", "N9c.1"], "9c.2": ["D4", "N9c.2"], "9c.5": ["D4", "N9c.5"], "10.0": ["C6"], "10.5": ["C6"],
    "10.1": ["C7"], "10.3": ["B4"], "11": ["N11"], "11b": ["N11b"], "G4": ["N2.3", "DB-10"],
}
_TOK = sorted(FOREIGN, key=len, reverse=True)
TOK_RE = re.compile(r"(?<![\w.§-])(" + "|".join(re.escape(t) for t in _TOK) + r")(?![\w.])")
PROV = (f"*Provenance (C-01, {DATE}):* originally authored against `gcp-curriculum.md` and the `unified-curriculum.md` "
        "nodes `DB-SQL` / `DB-ENGINE`; rebound to `Curriculum` + `northstar-reference-app.md` on 2026-09-24. Every "
        "foreign label and its new anchor is listed in `crosswalk.md` §1.")


def remap(text, seen=None):
    """rewrite a ' · '-separated stitch list: foreign tokens → new anchors, deduplicated, others unchanged"""
    seen = set() if seen is None else seen
    out = []
    for part in text.split(" · "):
        toks = []
        for tok in part.split(" / "):
            t = tok.strip()
            if t in FOREIGN:
                new = [a for a in FOREIGN[t] if a not in seen]
                seen.update(new)
                if new:
                    toks.append(" + ".join(new))
            else:
                toks.append(tok)
        if toks:
            out.append(" / ".join(toks))
    return " · ".join(out)


def pairs(d, cid, needle, reps, evidence, cls="anchor-rewrite", what="", **kw):
    i = d.one(needle, **kw)
    new = d.L[i]
    for old, rep in reps:
        assert new.count(old) >= 1, (cid, old, new[:120])
        new = new.replace(old, rep)
    if cls == "anchor-rewrite":
        d.replace_line(cid, cls, i, new, evidence, archive=False)
    else:
        d.replace_line(cid, cls, i, new, evidence, what=what)


def port_slices(root):
    """C-05: DB-1…DB-10 ported from the foreign parent (D1 allows borrowing), edited only for ID rebinding"""
    p = os.path.join(root, "..", SRC_PARENT)
    L = open(p, encoding="utf-8").read().split("\n")
    s = L.index("#### Engine slices DB-1–DB-10 (each: toy spec, SQL, EXPLAIN prediction, Cloud SQL mapping)")
    e = next(i for i in range(s, len(L)) if "Do not skip a slice because Cloud SQL hides it." in L[i])
    body = L[s + 1:e + 1]
    out = []
    for l in body:
        l = l.replace("##### DB-", "#### DB-")
        l = l.replace("(**G4**)", "(foreign `G4` WAL codec → N2.3)")
        l = l.replace("migrations via Job (2.6)", "migrations via Job (N2.6)")
        out.append(l)
    assert sum(1 for l in out if l.startswith("#### DB-")) == 10
    head = [
        "### 4.0 Engine slices (DB-1 … DB-10)", "",
        f"*Ported by the refactor ({DATE}, C-05; decision D1).* **Source material:** `gcp-curriculum.md` lines "
        f"{s + 2}–{e + 1} (\"Engine slices DB-1–DB-10\"), copied verbatim except for the ID rebinding marked in "
        "`crosswalk.md`. Since the refactor this file **owns** the slices; `Curriculum` A8 points here, and each "
        "slice is taught as one session with the companion theory paired to it in §2.2. The Cloud SQL procedure "
        "they map onto is N2.3.", "",
        "Each slice: toy spec, SQL, EXPLAIN prediction, Cloud SQL mapping.", ""]
    return head + out + [""]


def build_sql(d, prefs, root):
    E1 = "C-01: `Curriculum` is the only parent (§3.1)"
    E61 = "C-02/C-53: §6.1 crosswalk (crosswalk.md §1)"

    # ---------- title block ----------
    i = d.one("Companion to `gcp-curriculum.md` (\"The Consolidated Cloud Mastery Curriculum\"")
    d.replace_line("C-01", "correction", i,
                   "Companion to `Curriculum` (\"The Consolidated Cloud Mastery Curriculum\") and to its reference "
                   "application `northstar-reference-app.md` (Track N).", E1 + "; the old parent names are in the "
                   "provenance line below", what="title block, parent line")
    d.insert_after("C-01", "append", i, [PROV], "C-01: keep a one-line provenance note")
    i = d.one("Sources: PostgreSQL documentation · Silberschatz")
    d.insert_after("C-53", "append", i, [
        note("C-53", "the `TB-…` / `SRC-…` labels in the line above are this file's bibliography keys. They "
             "were first assigned in `unified-curriculum.md`; the labels are kept, the books and courses are named "
             "in full beside them.")], "C-53: TB-/SRC- IDs become an explicit bibliography, labels kept")

    # ---------- §0 ----------
    pairs(d, "C-01", "## 0. Read this first — how this file complements gcp-curriculum.md",
          [("gcp-curriculum.md", "`Curriculum`")], E1)
    pairs(d, "C-01", "**This file is a complement to `gcp-curriculum.md`",
          [("`gcp-curriculum.md`", "`Curriculum`"), ("a gcp-curriculum module", "a `Curriculum` module")], E1)
    pairs(d, "C-05", "Why: gcp-curriculum owns the *product spine*",
          [("Why: gcp-curriculum owns the *product spine* (Northstar on GCP) and, in Part 2, the engine slices DB-1 … "
            "DB-10 and the Cloud SQL procedure. It deliberately",
            "Why: `Curriculum` owns the order and the module spine; `northstar-reference-app.md` owns the *product "
            "spine* (Northstar on GCP) and the Cloud SQL procedure (N2.3). Since the refactor this file also owns the "
            "engine slices DB-1 … DB-10 (§4.0, C-05). `Curriculum` deliberately"),
           ("hangs each piece on the gcp-curriculum module", "hangs each piece on the `Curriculum` module")],
          "C-05: ownership of DB-1…DB-10 moved to this file; C-01", cls="correction", what="§0.1 \"Why\" line")
    pairs(d, "C-05", "2. **Ownership split (memorise).** *gcp-curriculum owns:*",
          [("*gcp-curriculum owns:* Cloud SQL setup (2.3), the ten engine slices DB-1 … DB-10 and their toys, Firestore "
            "(2.4), migrations-as-jobs (2.6), the Spanner/NoSQL map (2.7), the primitives of 8.1 (cursor pager, hot "
            "partition, pool math, RLS, LSM-vs-B-tree comparison), outbox/inbox (3.5), the ledger (5.3), BigQuery ops "
            "(9.4/9b.1), as-of joins as *leakage prevention* (9c.1), billing-export SQL (10.3).",
            "*`Curriculum` and Northstar own:* Cloud SQL setup (N2.3), Firestore (N2.4), migrations-as-jobs (N2.6), "
            "the Spanner/NoSQL map (N2.7), the primitives of N8.1 (cursor pager, hot partition, pool math, RLS, "
            "LSM-vs-B-tree comparison), outbox/inbox (A9 theory; design-patterns ARCH-11 shape), the ledger (N5.3), "
            "BigQuery ops (N9.4/N9b.1), as-of joins as *leakage prevention* (D3, N9c.1), billing-export SQL (B4)."),
           ("and the exercise ladder (§6).", "the exercise ladder (§6), and — since the refactor (C-05) — the engine "
            "slices DB-1 … DB-10 and their toys (§4.0)."),
           ("Where a gcp-curriculum toy exists", "Where a §4.0 slice toy exists")],
          "C-05: slices owned here; §6.1 rebinds the rest", cls="correction", what="§0.2 rule 2")
    pairs(d, "C-54", "3. **Same ten-rung ramp, same locks.**",
          [("taught through gcp-curriculum's universal ten-rung sequence",
            "taught through the suite's ten-rung sequence (`Curriculum` §0.4.3)"),
           ("before Part 2)", "before its N2.3 session)"),
           ("exactly as in gcp-curriculum.", "exactly as in `Curriculum` §0.4.6.")], "C-54/C-55 + C-01")
    pairs(d, "C-53", "6. **Predict before you run; explain the discrepancy after.**",
          [("(gcp-curriculum \"Database protocol\".)", "(`Curriculum` §0.4.4, predict → run → discrepancy; C-53.)")],
          "C-53: Database protocol → §13 rule")
    pairs(d, "C-57", "8. **Tracking is inline.** Tick `- [ ]` boxes in this file",
          [("the learner ledger of gcp-curriculum (\"Teaching contract → Learner state\") records",
            "the learner ledger `session-progress-ledger.md` (C-57; it replaces the old parent's \"Teaching contract "
            "→ Learner state\") records")], "C-57: rule kept, pointer rebound")
    pairs(d, "C-53", "10. **Time, money and secrets.**",
          [("(gcp-curriculum Lab safety)", "(`Curriculum` §0.5 Lab Safety)")], "C-53: Lab safety → Curriculum §0.5")
    pairs(d, "C-01", "11. **User can override anything:**",
          [("same rights as gcp-curriculum", "same rights as `Curriculum` §0.4.1"),
           ("**On a conflict:** gcp-curriculum wins", "**On a conflict:** `Curriculum` wins")], E1)
    pairs(d, "C-01", "12. **Read economically.**", [("today's gcp-curriculum module", "today's `Curriculum` module")],
          E1)
    pairs(d, "C-01", "1. **Anchor** — announce the gcp-curriculum module",
          [("the gcp-curriculum module", "the `Curriculum` module")], E1)
    pairs(d, "C-01", "2. **Concept** — teach the shared idea once (gcp-curriculum depth)",
          [("(gcp-curriculum depth)", "(`Curriculum` depth)")], E1)
    i = d.one("7. **Close** — tick boxes in both files' sense; ledger line")
    d.insert_after("C-29", "append", i, ["", C29_POINTER], "C-29 pointer")

    # notation
    pairs(d, "C-37", "`SD-n` schema-design cases", [("`SD-n` schema-design cases", "`SCH-n` schema-design cases")],
          "C-37: the bare `SD-n` legend token (hand-reviewed; §5 primer-specific rule)", cls="rename")
    i = d.one("- `T.*`, `F1…F4`, `M.*`, `0.x`, `1.x`, `D0…D8`")
    d.replace_line("C-53", "correction", i,
                   "- The old parent's labels (`T.*`, `F1…F4`, `M.*`, `0.x`, `1.x`, `D0…D8`, `2.x` … `11b`, `12.Sxx`, "
                   "`G4`, `G12b`) were rebound on 2026-09-24 to `Curriculum` IDs (`A1…D4`, `M1…M6`, `U1…U7`, "
                   "`S1…S11`, the Part V category IDs `V-…`) and Northstar sections (`Nx.y`); `crosswalk.md` §1 has "
                   "every mapping. `DB-1 … DB-10` are this file's engine slices (§4.0). `SD-13 … SD-27` are "
                   "primer-companion IDs. `TB-…`/`SRC-…` are this file's bibliography labels (title block).",
                   "C-53 + §6.1: the legend described foreign IDs that no longer appear", what="§0.4 notation, ID legend")
    d.insert_after("C-08", "append", i, [
        "- Tiers: `SQL-T-HS` high-school · `SQL-T-UG` undergraduate · `SQL-T-GR` graduate — the depth tier of a theory "
        "item or gate (§2 rows for M1 and A8 + A9; renamed from `HS` / `UG` / `grad` in §5 of the refactor). "
        "*(Legend added by the refactor, C-08.)*"], "C-08: the tier IDs had no legend line")
    pairs(d, "C-01", "- `Northstar` = the running product of gcp-curriculum",
          [("the running product of gcp-curriculum", "the running reference application "
            "(`northstar-reference-app.md`, Track N)")], E1)
    i = d.one("- `Northstar` = the running reference application")
    d.insert_after("INV-4", "new-content", i, ["", "### 0.5 " + PREFS_HEAD, ""] + prefs,
                   "invariant 4: ledger §5 preferences copied unchanged")

    # ---------- §2 stitch table ----------
    pairs(d, "C-01", "Each gcp-curriculum module on the left", [("Each gcp-curriculum module", "Each `Curriculum` module")],
          E1)
    pairs(d, "C-02", "| gcp-curriculum module | Companion modules taught in the same session | Checkpoint |",
          [("gcp-curriculum module", "`Curriculum` module (was: old-parent label)")], E61)
    s2 = d.heading("2. Stitch table")
    e2 = d.heading("2.1 Overlap register")
    first = {  # old first cell → new first cell (C-02, §6.1)
        "**T.Disc** (logic, sets, proofs, counting, graphs) — *Tier SQL-T-HS/SQL-T-UG*":
            "**M1** (logic, sets, proofs, counting, graphs) — *Tier SQL-T-HS/SQL-T-UG* *(was `T.Disc`)*",
        "**T.Algo** (structures, hashing theory, complexity)":
            "**A4** (recall) + **U2** (structures, hashing theory, complexity) *(was `T.Algo`)*",
        "**T.Quant** (units, orders of magnitude)":
            "**A1/A2** (recall) + **M6** (units, orders of magnitude) *(was `T.Quant`)*",
        "**M.NS** (numerical stability)": "**M5** (numerical stability) *(was `M.NS`)*",
        "**T.SysTheory — DB theory** (with Part 2)":
            "**A8 + A9** (+ U5) — DB theory (with the A8 SQL sessions) *(was `T.SysTheory`, Part 2)*",
        "**F1** (computer, OS, CLI, Git, JSON, HTTP)": "**A3 + A6** (computer, OS, CLI, Git, JSON, HTTP) *(was `F1`)*",
        "**D1** Docker/OCI · **1.2** container contract": "**C1** Docker/OCI, container contract *(was `D1`, `1.2`)*",
        "**D2** CI": "**C4** CI *(was `D2`)*",
        "**D3/D7** CD, IaC": "**C4 + C5** CD, IaC *(was `D3/D7`)*",
        "**0.4** HLD/LLD contract, ADR template, NFR table":
            "**S2** + **N0.4** HLD/LLD contract, ADR template, NFR table *(was `0.4`)*",
        "**0.5** IAM (+ **2.3** IAM DB auth)": "**B5** IAM (+ **N2.3** IAM DB auth) *(was `0.5`, `2.3`)*",
        "**1.7** observability day one": "**C6** observability day one *(was `1.7`)*",
        "**1.12** HA & autoscaling": "**B3** HA & autoscaling *(was `1.12`)*",
        "**2.1 — SQL design track** (concept, then lab)":
            "**A8 — SQL design track** (concept, then lab; engine slices §4.0) *(was `2.1`)*",
        "**2.2** GCP relational offerings (decision table)":
            "**A8** + **V-STOR** GCP relational offerings (decision table) *(was `2.2`)*",
        "**2.3** Cloud SQL setup (required procedure)": "**N2.3** Cloud SQL setup (required procedure) *(was `2.3`)*",
        "**2.4** Firestore": "**A8** (NoSQL) + **N2.4** Firestore *(was `2.4`)*",
        "**2.5** Cloud Storage": "**N2.5** Cloud Storage *(was `2.5`)*",
        "**2.6** config, migrations, jobs": "**A8** + **C4** + **N2.6** config, migrations, jobs *(was `2.6`)*",
        "**2.7** Spanner & NoSQL map": "**A9** + **V-STOR** + **N2.7** Spanner & NoSQL map *(was `2.7`)*",
        "**3.0** software design (repositories)":
            "**A7** software design (repositories; design-patterns Repository, Unit of Work) *(was `3.0`)*",
        "**3.4** async (Pub/Sub, Tasks, Scheduler)": "**A7** async (Pub/Sub, Tasks, Scheduler) *(was `3.4`)*",
        "**3.5** failure design (outbox/inbox, sagas)":
            "**A9** + design-patterns **ARCH-11** failure design (outbox/inbox, sagas) *(was `3.5`)*",
        "**4.7** authorization · **4.9** secrets & supply chain":
            "**A10 + B5** authorization · **C1** + **Phase 4 Security** secrets & supply chain *(was `4.7`, `4.9`)*",
        "**5.3** ledger and consistency": "**A8** + **N5.3** ledger and consistency *(was `5.3`)*",
        "**7.3** data protection": "**Phase 4 Security** + **N7.3** data protection *(was `7.3`)*",
        "**8.0** Donne-Martin building blocks · **8.C** evidence packs":
            "**S2** + **N8.0** Donne-Martin building blocks · **N8.C** evidence packs *(was `8.0`, `8.C`)*",
        "**8.1** primitives — cursor pagination · hot partition · pool math · RLS · LSM vs B-tree · schema evolution · "
        "idempotency":
            "**N8.1** primitives — cursor pagination · hot partition · pool math · RLS · LSM vs B-tree · schema "
            "evolution · idempotency *(was `8.1`)*",
        "**9.1** Memorystore": "**V-STOR** + **N9.1** Memorystore *(was `9.1`)*",
        "**9.4** Spanner, AlloyDB, Bigtable, BigQuery (ops view)":
            "**V-STOR** + **N9.4** Spanner, AlloyDB, Bigtable, BigQuery (ops view) *(was `9.4`)*",
        "**9b.1** Big-data services (BigQuery, Dataform)":
            "**V-DATA** + **N9b.1** Big-data services (BigQuery, Dataform) *(was `9b.1`)*",
        "**9c.1** features, labels, skew (**as-of join** owner)":
            "**D3** + **N9c.1** features, labels, skew (**as-of join** owner) *(was `9c.1`)*",
        "**9c.2 / 9c.5** retrieval, RAG": "**D4** + **N9c.2 / N9c.5** retrieval, RAG *(was `9c.2 / 9c.5`)*",
        "**10.0** observability · **10.5** performance": "**C6** observability, performance *(was `10.0`, `10.5`)*",
        "**10.1** SLO / error budget": "**C7** SLO / error budget *(was `10.1`)*",
        "**10.3** FinOps + billing-export SQL": "**B4** FinOps + billing-export SQL *(was `10.3`)*",
        "**11** capstone (Northstar v1)": "**N11** capstone (Northstar v1) *(was `11`)*",
        "**11b** control-plane capstone": "**N11b** control-plane capstone *(was `11b`)*",
        "**PCA / PDE / PCDE certs**": "**Part V cert rows 1, 3, 8** (PCA / PDE / PCDE certs)",
    }
    cells = {  # other cells of the same rows
        "(**8.1.5 owns the from-scratch pager**)": "(**N8.1.5 owns the from-scratch pager**)",
        "*8.1 owns the spreadsheet — recall it*": "*N8.1 owns the spreadsheet — recall it*",
        "| SQL-E10.6 (RLS) after 4.7 |": "| SQL-E10.6 (RLS) after A10 |",
        "*9c.1 owns leakage; this file owns the join*": "*N9c.1 owns leakage; this file owns the join*",
        "if Part 2 confirmed": "if the A8 sessions confirmed",
        "*recall IEEE from M.NS;": "*recall IEEE from M5;",
    }
    used = set()
    for i in range(s2, e2):
        l = d.L[i]
        if not l.startswith("| **"):
            continue
        c0 = l[2:].split(" |", 1)[0]
        new = l
        if c0 in first:
            new = new.replace(c0, first[c0], 1)
            used.add(c0)
        for o, r in cells.items():
            if o in new:
                new = new.replace(o, r)
                used.add(o)
        if new != l:
            d.replace_line("C-02", "anchor-rewrite", i, new, E61, archive=False)
    missing = (set(first) | set(cells)) - used
    assert not missing, missing

    # ---------- §2.1 overlap register ----------
    s = d.heading("2.1 Overlap register")
    e = d.heading("2.2 ")
    owner = [
        ("| gcp-curriculum **2.1 / DB-1** (toy:", "| **§4.0 DB-1** (this file since C-05; A8) (toy:"),
        ("| **2.1 / DB-", "| **§4.0 DB-"), ("(DB-10 / G4)", "(DB-10; foreign `G4` → N2.3)"),
        ("| **2.3** |", "| **N2.3** |"), ("| **2.6** |", "| **N2.6** |"), ("| **2.7 / 2.4** |", "| **N2.7 / N2.4** |"),
        ("| **8.1.5** (from-scratch pager) |", "| **N8.1.5** (from-scratch pager) |"), ("| **8.1** |", "| **N8.1** |"),
        ("| **8.1 / 2.3** |", "| **N8.1 / N2.3** |"), ("| **8.1 / 2.1** |", "| **N8.1 / A8** |"),
        ("| **3.5 / 3.4** |", "| **A9 / A7** (`Curriculum` §0.3: 2PC/Saga/outbox) |"), ("| **5.3** |", "| **N5.3** |"),
        ("| **9.4 / 9b.1** |", "| **N9.4 / N9b.1** |"), ("| **9c.1** |", "| **N9c.1** (D3) |"),
        ("| **10.3** |", "| **B4** |"),
        ("| gcp-curriculum **T.Disc / T.Algo / T.SysTheory / 2.x** |",
         "| `Curriculum` **M1 / A4 + U2 / A8 + A9 / A8** *(was T.Disc / T.Algo / T.SysTheory / 2.x)* |"),
    ]
    for i in range(s, e):
        l = d.L[i]
        new = l
        for o, r in owner:
            new = new.replace(o, r)
        if new != l:
            d.replace_line("C-02", "anchor-rewrite", i, new, E61 + "; C-05 (DB-n owned here)", archive=False)
    assert not any("gcp-curriculum" in d.L[k] for k in range(s, e))
    i = d.one("| Concept | Owner (teach here) | This file adds |", start=s)
    d.insert("§7", "append", i, [note("§7", "the suite-wide register is `Curriculum` §0.3; this table is the SQL slice "
             "of it, and on a conflict §0.3 wins. DB-1 … DB-10 are owned by this file since C-05 (§4.0)."), ""],
             "§7 register → Curriculum §0.3")

    # ---------- §2.2 / §2.3 ----------
    pairs(d, "C-02", "### 2.2 Part 2.1 slice pairing", [("### 2.2 Part 2.1 slice pairing", "### 2.2 A8 slice pairing")],
          E61)
    pairs(d, "C-05", "The gcp-curriculum slice supplies *toy spec, SQL, EXPLAIN prediction, Cloud SQL mapping*.",
          [("The gcp-curriculum slice supplies", "The §4.0 slice supplies")], "C-05")
    pairs(d, "C-53", "| **DB-10** WAL, replica, PITR (**G4**) |", [("(**G4**)", "(**N2.3**)")], "C-53: G4 → N2.3 + DB-10")
    pairs(d, "C-01", "### 2.3 Parallel calendar — how the companion rides gcp-curriculum's spine",
          [("gcp-curriculum's spine", "`Curriculum`'s spine")], E1)
    pairs(d, "C-02", "gcp-curriculum's spine is `T → F → M → 0 → 1 → D → 2 → 3 → …`.",
          [("gcp-curriculum's spine is `T → F → M → 0 → 1 → D → 2 → 3 → …`. SQL does not first *appear* until Part 2,",
            "`Curriculum`'s spine is Phases 0–3 (Tracks A–D, mostly in parallel) → Phase 4 → …, with the reserved "
            "M/U/S tracks placed by R4. SQL does not first *appear* until A8,"),
           ("holds the language until Part 2 needs it", "holds the language until A8 needs it")],
          E61, cls="correction", what="§2.3 intro")
    pairs(d, "C-01", "| Window (gcp-curriculum) | Companion work", [("| Window (gcp-curriculum) |", "| Window (`Curriculum`) |")],
          E1)
    cal = [
        ("| **Block T** (SQL-T-HS → SQL-T-UG tiers) |", [("**Block T** (SQL-T-HS → SQL-T-UG tiers)",
                                                         "**A1–A4 + M1** (SQL-T-HS → SQL-T-UG tiers) *(was Block T)*")]),
        ("| **F1 – F4, M.NS** |", [("**F1 – F4, M.NS**", "**A3, A6, A11 + M5** *(was F1 – F4, M.NS)*")]),
        ("| **Parts 0 – 1, D** |", [("**Parts 0 – 1, D**", "**Tracks B and C (B3, C1, C4, C6)** *(was Parts 0 – 1, D)*"),
                                    ("OD-03 recall at 1.12", "OD-03 recall at B3")]),
        ("| **Part 2 (the main event)** |", [("**Part 2 (the main event)**", "**A8 (the main event)** *(was Part 2)*"),
                                             ("**2.1 is stretched over ≥ 3 weeks:**",
                                              "**The A8 SQL block is stretched over ≥ 3 weeks:**"),
                                             ("2.2 – 2.7 as bound in §2", "the V-STOR and N2.3…N2.7 rows as bound in §2")]),
        ("| **Parts 3 – 5** |", [("**Parts 3 – 5**", "**A7, A9, A10 + N5.3** *(was Parts 3 – 5)*"),
                                 ("SQL-E9.3 (3.4), TX-5 (3.5), SQL-E10.6 (4.7), SQL-E4.5/SQL-CAP2 (5.3)",
                                  "SQL-E9.3 (A7), TX-5 (A9), SQL-E10.6 (A10), SQL-E4.5/SQL-CAP2 (N5.3)")]),
        ("| **Part 8** |", [("**Part 8**", "**N8.0/N8.1/N8.C + S2** *(was Part 8)*"), ("with 8.1", "with N8.1")]),
        ("| **Parts 9, 9b, 9c** |", [("**Parts 9, 9b, 9c**", "**V-STOR, V-DATA, D3/D4 + N9.1/N9.4/N9b.1/N9c.1** *(was Parts 9, 9b, 9c)*"),
                                     ("at 9c.1", "at D3 (N9c.1)")]),
        ("| **Part 10** |", [("**Part 10**", "**C6, C7, B4** *(was Part 10)*"),
                             ("at 10.5; DT-4 at 10.3", "at C6; DT-4 at B4")]),
        ("| **Part 11 / 11b** |", [("**Part 11 / 11b**", "**N11 / N11b** *(was Part 11 / 11b)*")]),
        ("| **Part 12 — SQL-SKIP-SQL / SQL-SKIP-ENGINE** |",
         [("**Part 12 — SQL-SKIP-SQL / SQL-SKIP-ENGINE**", "**A8 skip-tests — SQL-SKIP-SQL / SQL-SKIP-ENGINE** "
           "*(was Part 12)*")]),
    ]
    for needle, reps in cal:
        pairs(d, "C-02", needle, reps, E61)
    pairs(d, "C-01", "**SQL-SKIP-SQL order → companion modules (unified-curriculum §5.4 order, unchanged):**",
          [("(unified-curriculum §5.4 order, unchanged)", "(order unchanged; provenance: `unified-curriculum.md` §5.4)")],
          E1)

    # ---------- §3, §4 headers and prose ----------
    pairs(d, "C-01", "Cloud SQL / AlloyDB: same SQL; create an instance only when Lab Reality allows",
          [("(gcp-curriculum Lab safety)", "(`Curriculum` §0.5)"), ("when 2.3 is unlocked", "when N2.3 is unlocked")], E1)
    pairs(d, "C-05", "Ownership: where a gcp toy exists, this file adds analysis only.",
          [("where a gcp toy exists, this file adds analysis only.",
            "where a §4.0 slice toy exists, the concept modules add analysis only.")], "C-05: toys now live in §4.0")
    n = 0
    for i, l in enumerate(d.L):
        m = re.match(r"^(#### [A-Z]{2}-\d{2} · .*? — stitch: )(.*)$", l)
        if m:
            new = m.group(1) + remap(m.group(2))
            if new != l:
                d.replace_line("C-02", "anchor-rewrite", i, new, E61, archive=False)
                n += 1
    assert n >= 40, n
    prose = [
        ("- **Theory:** Half-up vs banker rounding; IEEE recall from M.NS", [("from M.NS", "from M5")]),
        ("- **Lab:** SQL-E3.1–SQL-E3.10; SQL-E6.4 as-of shape (leakage owner is 9c.1).", [("is 9c.1", "is N9c.1")]),
        ("- **GCP lens:** Lens-1: 8.1 owns LSM-vs-B-tree comparison toy", [("Lens-1: 8.1 owns", "Lens-1: N8.1 owns")]),
        ("- **Theory:** TrueTime/Paxos *vocabulary* when 2.7 is unlocked", [("when 2.7 is", "when A9 / N2.7 is")]),
        ("- **GCP lens:** Lens-1: ledger rules in gcp 5.3", [("in gcp 5.3", "in N5.3")]),
        ("- **Theory:** Leakage prevention is owned by 9c.1;", [("owned by 9c.1", "owned by N9c.1")]),
        ("- **GCP lens:** Lens-1: 8.1 owns RLS primitive", [("Lens-1: 8.1 owns", "Lens-1: N8.1 owns")]),
        ("- **Theory:** gcp 2.6 owns migrations-as-jobs", [("gcp 2.6 owns", "N2.6 owns")]),
        ("- **GCP lens:** Lens-1: 8.1 owns the hot-partition primitive", [("Lens-1: 8.1 owns", "Lens-1: N8.1 owns")]),
        ("- **Theory:** 8.1 owns the spreadsheet — recall it.", [("8.1 owns", "N8.1 owns")]),
        ("- **Theory:** 8.1.5 owns the from-scratch pager", [("8.1.5 owns", "N8.1.5 owns")]),
        ("Lens-1: Cloud SQL vs BigQuery decision table (gcp 2.2)", [("(gcp 2.2)", "(A8 + V-STOR)")]),
        ("Mapped to unified-curriculum `DB-SQL` / `DB-ENGINE` and gcp-curriculum continuation modules",
         [("Mapped to unified-curriculum `DB-SQL` / `DB-ENGINE` and gcp-curriculum continuation modules "
           "**SQL-SKIP-SQL** / **SQL-SKIP-ENGINE**. If Part 2 already confirmed",
           "Mapped to the A8 skip-tests **SQL-SKIP-SQL** / **SQL-SKIP-ENGINE** (provenance: `unified-curriculum.md` "
           "nodes `DB-SQL` / `DB-ENGINE`). If the A8 sessions already confirmed")]),
        ("- **SQL-SKIP-SQL:** SQL-E3.2, SQL-E4.5, SQL-E5.4, SQL-E9.3, TX-2 (if Part 2 confirmed",
         [("(if Part 2 confirmed", "(if the A8 sessions confirmed")]),
        ("Issued one at a time with T.SysTheory / Part 2 slices.",
         [("with T.SysTheory / Part 2 slices", "with the A8 + A9 (+ U5) theory and the §4.0 slices")]),
        ("This is the same shape as gcp-curriculum **9c.1** point-in-time joins.",
         [("gcp-curriculum **9c.1**", "**N9c.1** (D3)")]),
        ("Same principle as the gcp-curriculum ledger's determinism rules.",
         [("the gcp-curriculum ledger's", "the Northstar ledger's (N5.3)")]),
        ("Idempotent writes are the whole point of gcp-curriculum 3.4/3.5.", [("gcp-curriculum 3.4/3.5", "A7/A9")]),
        ("in production every chunk commits separately — gcp-curriculum 2.6 expand/contract.)",
         [("gcp-curriculum 2.6", "N2.6")]),
        ("This is defence in depth beneath RLS (gcp-curriculum 8.1).", [("(gcp-curriculum 8.1)", "(N8.1)")]),
        ("must be `SET LOCAL` per transaction — gcp-curriculum 8.1 RLS.", [("gcp-curriculum 8.1 RLS", "N8.1 RLS")]),
        ("In BigQuery you would partition the fact by date and cluster by product (gcp-curriculum 9b.1)",
         [("(gcp-curriculum 9b.1)", "(V-DATA, N9b.1)")]),
        ("- **Tags:** PX-9 · OD-09 · 8.1.5", [("8.1.5", "N8.1.5")]),
        ("- **Tags:** T5+T6 · 3.5", [("· 3.5", "· A9")]),
        ("- **Tags:** 5.3·DD-05", [("5.3·", "N5.3·")]),
        ("- **Tags:** AN-06·2.4", [("·2.4", "·N2.4")]),
        ("- **Tags:** DD-02·8.0", [("·8.0", "·N8.0")]),
        ("- **Tags:** DD-11·2.6", [("·2.6", "·N2.6")]),
        ("- **Tags:** DD-13·2.7", [("·2.7", "·N2.7")]),
        ("- **Tags:** DD-07·7.3", [("·7.3", "·N7.3")]),
        ("Mirror gcp-curriculum C5 posture", [("gcp-curriculum C5", "`Curriculum` C5")]),
        ("Database acceptance tests for gcp Part 11 / Northstar.", [("gcp Part 11 / Northstar", "N11 (Northstar)")]),
    ]
    for needle, reps in prose:
        pairs(d, "C-02", needle, reps, E61)
    d.sub("C-09", "rename", r"(?<![\w.-])E(\d{1,2})\.x\b", r"SQL-E\1.x",
          "§5 rename: `E<level>.x` level wildcards were missed by the dry run's `E<l>.<n>` rule", expect_min=9,
          expect_max=9)

    # ---------- C-05: §4.0 engine slices ----------
    i = d.heading("4.1 Pre-SQL prerequisites")
    d.insert("C-05", "new-content", i, port_slices(root),
             "C-05 + D1: slices ported with a Source-material line (gcp-curriculum.md)")
    assert not [l for l in d.L if "gcp-curriculum" in l and "rovenance" not in l and "Source material" not in l
                and "crosswalk" not in l and "was:" not in l], \
        [l[:80] for l in d.L if "gcp-curriculum" in l and "rovenance" not in l][:5]
    return d
