#!/usr/bin/env python3
"""R2 repair pipeline: inputs-original → rename.py (§5) → journaled repair edits (§4, §6, §7) → work/ + new files.

Usage:
  r2_build.py ROOT          # ROOT = the refactor workspace (holds inputs-original/, work/, refactor-tools/)

Deterministic and idempotent: it always starts again from inputs-original/, so running it twice gives
byte-identical outputs. Every edit is journaled (outputs/r2/journal.jsonl) with its class (§1 invariant 16),
conflict ID, evidence, and before/after lines; CHANGELOG.md is generated from the journal.

Edit classes: rename (rename.py) · anchor-rewrite · move · append · correction · new-content · regenerate.
Decision D3 (no removal): a line changed by anything other than an anchor-rewrite keeps its pre-refactor text
verbatim in the file's closing "Pre-refactor text archive (D3)" section. Anchor-rewrites keep their originals
in the journal, diffs/, crosswalk.md, and (cyber) the per-module Provenance lines.
"""
import difflib, hashlib, json, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rename  # noqa: E402
import binding  # noqa: E402
import r2_cur  # noqa: E402
import r2_sql  # noqa: E402
import r2_sec  # noqa: E402
import r2_dp  # noqa: E402
import northstar  # noqa: E402
import reports  # noqa: E402

from r2_common import JOURNAL, Doc, note, ledger_prefs, PREFS_HEAD, C29_POINTER, DATE, CUR, PRI, SQL, DPC, SEC, LED, SKL  # noqa: E402


# ------------------------------------------------------------------------------------------------ primer
def build_primer(d, prefs, primer_src_path):
    E = "primer file; C-01/C-39 parent rename; Curriculum is the only parent (§3.1)"
    # ---------- C-01 / C-39 parent-name rewrites (anchor-rewrite) ----------
    d.sub("C-01", "anchor-rewrite", r"`/Users/Suhas\.KS/gcp\.md`", "`Curriculum`", E, expect_min=2, expect_max=2)
    d.sub("C-39", "anchor-rewrite", r"\bgcp (A\d+)\b", r"Curriculum \1", "primer §4.1 mermaid node labels; C-39",
          expect_min=4, expect_max=4, skip_fence=False)
    # Part V categories used as anchors → V-IDs (C-22/C-39); only outside the regenerated §2 and headers
    vrules = [(r"Part V Compute/Networking", "V-COMP/V-NET"), (r"Part V Storage/Data\b", "V-STOR/V-DATA"),
              (r"Part V Storage/DB", "V-STOR"), (r"Part V Storage\b", "V-STOR"),
              (r"Part V Networking", "V-NET"), (r"Part V Data/Analytics", "V-DATA")]
    s2 = d.heading("2. Stitch table")
    hdr = lambda l: not re.match(r"#### SD-\d{2} · ", l)
    for pat, rep in vrules:
        d.sub("C-39", "anchor-rewrite", pat, rep, "C-22/C-39: Part V categories get V-IDs", start=s2 + 1,
              only=lambda l: hdr(l) and not l.startswith("| **Part V"), expect_min=0)
    d.sub("C-39", "anchor-rewrite", r"gcp\.md C2 / Part V\b", "Curriculum C2 / V-COMP",
          "C-22/C-39: autoscaling (MIG) lives in the Compute category", expect_min=1, expect_max=1)
    d.sub("C-01", "anchor-rewrite", r"gcp\.md's", "Curriculum's", E, expect_min=1)
    d.sub("C-01", "anchor-rewrite", r"\bgcp\.md\b", "Curriculum", E, expect_min=40)

    # ---------- invariant 11: CC BY modification line directly under the attribution ----------
    i = d.one("(CC BY 4.0)")
    d.insert_after("INV-11", "new-content", i,
                   [f"Modified by the curriculum refactor on {DATE}; changes listed in CHANGELOG.md."],
                   "invariant 11 (CC BY 4.0 §3(a)(1)(B): indicate modifications)")

    # ---------- §0.2 rule 6 amendment (C-30) ----------
    i = d.one("6. **Tracking is inline.**")
    d.insert_after("C-30", "append", i, [
        "   *Exception (added by the refactor, C-30):* `session-progress-ledger.md` is the single sanctioned "
        "cross-file tracker; inline `- [ ]` ticks remain authoritative and the ledger mirrors them. Refactor "
        "artifacts (`refactor-state.md`, manifests, reports) are build tooling, not trackers, and are not uploaded "
        "to teaching sessions."], "C-30 resolution text, verbatim from the refactor prompt")

    # ---------- §0.3 Suite Session Protocol pointer (C-29) ----------
    i = d.one("7. **Close** — tick the boxes in both files' sense")
    d.insert_after("C-29", "append", i, ["", C29_POINTER], "C-29: each companion keeps its §0.3 plus this pointer")

    # ---------- §0.4 notation additions (C-22, C-24, §3.2) ----------
    i = d.one("`Part V` = Curriculum's GCP service map.")
    d.insert_after("C-22", "append", i, [
        "- `V-COMP, V-STOR, V-NET, V-DATA, V-AI, V-SEC, V-OPS` — `Curriculum` Part V service-map categories (C-22). "
        "`M1…M6`, `U1…U7`, `S1…S11` — new `Curriculum` tracks (stubs until R4). `Nx.y` — sections of "
        "`northstar-reference-app.md`.",
        "- Binding notation (C-24): `SD-21@A8` primary · `SD-21[hash-table slice]@A4` slice · `SD-21~C2` recall. "
        "The single source is `primer-binding-table.md`; the header stitches, §2 and §4.5 are generated from it."],
        "C-22 V-IDs; C-24 notation; §3.2 track IDs")

    # ---------- invariant 4: ledger §5 preferences in §0 ----------
    i = d.one("- Primer numbers (\"primer:\") are quoted from the primer")
    d.insert_after("INV-4", "new-content", i, ["", "### 0.5 " + PREFS_HEAD, ""] + prefs,
                   "invariant 4: ledger §5 preferences copied unchanged into every file's §0")

    # ---------- C-24: regenerate module-header stitches from the binding table ----------
    for i, l in enumerate(list(d.L)):
        m = re.match(r"^(#### (SD-\d{2}) · .*? — stitch: )(.*)$", l)
        if m:
            new = m.group(1) + binding.header_stitch(m.group(2))
            if new != l:
                d.replace_line("C-24", "regenerate", i, new, "primer-binding-table.md (C-24/C-25/C-26/C-27)",
                               archive=False)
    # header stitches are anchor metadata: originals stay in the journal, the diff and primer-binding-table.md's
    # candidate column, so they are not duplicated into the archive (anchor-rewrite rule)

    # ---------- C-24/C-33/C-34: regenerate §2 stitch table ----------
    _, _, _, hard = binding.pb.parse(primer_src_path)
    hard = binding.hard_prereqs(hard)
    s2 = d.heading("2. Stitch table")
    t0 = d.one("| Curriculum module | Companion concepts taught in the same session | Checkpoint |", start=s2)
    t1 = next(j for j in range(t0, len(d.L)) if not d.L[j].startswith("|"))
    old_rows = d.L[t0:t1]
    title = {}
    checkpoint = {}
    for r in old_rows[2:]:
        cells = [c.strip() for c in r.strip("|").split("|")]
        m = re.match(r"\*\*([ABCD]\d+)\*\* (.*)", cells[0])
        if m:
            title[m.group(1)] = m.group(2)
            checkpoint[m.group(1)] = cells[-1]
    cp_new = {
        "A3": "— (O01, O02 move to the A4 recall checkpoints, C-34)",
        "A4": "O01, O02, O07 — recall checkpoints, run as practice, not re-teaching (C-34)",
        "A5": "P08 *Single box* step (SD-08 + the P08 network hardening → NT-01, NT-05) and the *Users++* networking "
              "slice (SD-09, SD-10, SD-11); SD-06 → A9 and SD-12 → A7 are named, not taught (C-33)",
        "A6": "P08 step 0 (the single-box OS view), then the full P08 first pass (outline) (C-33)",
        "A7": "P01, O03 (after DP-18 + DP-16 State), O04, O05 (after F-01…F-04 + PR-01…PR-05 SOLID), O06 (C-34)",
    }
    # problem-level stitches that the pre-refactor rows carried besides SD/SX IDs (kept in the live table)
    probs = {"A2": "SD-00 back-of-envelope drills", "A3": "all O-problems' Python",
             "A11": "P08 \"automate DevOps\" step", "B1": "P08 (why managed services beat self-run at each step)",
             "B3": "P08 walk-through", "B4": "autoscaling savings (P08 \"Users++++\")",
             "C2": "P08 autoscaling (HPA)",
             "C5": "every P-problem's reference architecture (Section 5) as a `terraform plan` exercise",
             "C6": "P08 monitoring list (host, aggregate, logs, external, alerts, errors)",
             "D1": "Q07 recommendation system · Q16 trending topics (score models)",
             "D3": "Q07 feature store, batch vs online serving",
             "D4": "SX-06 reverse index ↔ embeddings/vector index · Q02 search engine · Q14 graph search",
             }
    anchors = [a for a in binding.ORDER if re.match(r"[ABCD]\d+$", a)]
    rows = ["| Curriculum module | Taught in full here (PRIMARY) | Slices and forward pointers | Recalls | "
            "Also in this session | Checkpoint |", "|---|---|---|---|---|---|"]
    for a in anchors:
        c_pri, c_sl, c_rc = binding.row_cells(a, hard)
        if a not in title and c_pri == c_sl == c_rc == "—":
            continue
        name = title.get(a, {"D2": "Deep learning"}.get(a, ""))
        cp = cp_new.get(a, checkpoint.get(a, "—"))
        rows.append(f"| **{a}** {name} | {c_pri} | {c_sl} | {c_rc} | {probs.get(a, '—')} | {cp} |")
    vname = {"V-COMP": "Compute", "V-STOR": "Storage/DB", "V-NET": "Networking", "V-DATA": "Data/Analytics",
             "V-AI": "AI/ML", "V-SEC": "Security", "V-OPS": "Ops/DevOps"}
    vrow = {}
    for r in old_rows[2:]:
        m = re.match(r"\| \*\*Part V — ([^*]+)\*\*([^|]*)\|", r)
        if m:
            c = [x.strip() for x in r.strip("|").split("|")]
            vrow[m.group(1)] = (m.group(2).strip(), c[1], c[2])   # (service list, Lens-3 wording verbatim, checkpoint)
    for v, nm in vname.items():
        _, _, c_rc = binding.row_cells(v, hard)
        svc, lens3, cp = vrow.get(nm, ("", "—", "—"))
        rows.append(f"| **{v}** Part V — {nm}{' ' + svc if svc else ''} (Lens-3 in Phase 4) | — | — | {c_rc} | "
                    f"{lens3} | {cp} |")
    for r in old_rows[2:]:
        if r.startswith("| **PCA") or r.startswith("| **Part VI"):
            c = [x.strip() for x in r.strip("|").split("|")]
            rows.append(f"| {c[0]} | — | — | — | {c[1]} | {c[2]} |")
    intro = [f"*Generated from `primer-binding-table.md` ({DATE}, C-24).* Columns: PRIMARY = the session that "
             "teaches the concept in full; slices = one named ingredient taught earlier (or a continuation after); "
             "recalls = a one-line reference back; also in this session = the problem-level work (and, for V rows, the Lens-3 service wording) the pre-refactor row named, kept verbatim. "
             "The full pre-refactor table is kept verbatim in the D3 archive at the end of this file.", ""]
    d.replace_block("C-24", "regenerate", t0, t1, intro + rows,
                    "primer-binding-table.md; C-24 (one source), C-33 (P08 timing), C-34 (O-problem gates)",
                    what="§2 stitch table (pre-refactor)")

    # ---------- §2.1: pointer to the suite register (C-36, §7) ----------
    i = d.heading("2.1 Overlap register")
    d.insert_after("C-36", "append", i, ["", "Suite-wide ownership lives in the register in `Curriculum` §0.3 "
                   "(which also carries the v1.1 rows for PACELC, cache stampede, tail latency, Little's law, "
                   "consistent hashing, CRDTs, sketches, unique IDs, GC, event sourcing and credential storage). "
                   "This table is the primer's slice of it; on a conflict §0.3 wins."],
                   "C-36 + §7: the §7 register goes into Curriculum §0.3; companions point to it")

    # ---------- SD-35 index module (C-28, C-14) ----------
    s = d.heading("SD-35 · Security basics")
    e = d.section_end(s)
    ip = d.one("- **Primer:** encrypt in transit and at rest", start=s, end=e)
    d.insert_after("C-28", "append", ip, [
        "- **Taught by (index module, C-28):** in transit → `Curriculum` A5 TLS + cyber CR-11/CR-12 (the A5 "
        "transit slice; C-14) · at rest → CR-14 @ Phase 4 · XSS → WA-02 @ A10 · SQL injection / parameterized "
        "queries → SQL SL-13 (mechanics) + cyber WA-05 (attacker model) · least privilege → B5 + CL-03 · the P08 "
        "network hardening → NT-01, NT-05, NT-07 @ A5."], "C-28 table, C-14 split")
    ig = d.one("- **GCP lens:** in transit → TLS at the LB", start=s, end=d.section_end(s))
    d.insert_after("C-28", "append", ig, [
        "- **Prop Lock (C-28):** before Phase 4 the controls named above (VPC Service Controls, CMEK, Cloud Armor "
        "WAF rules, mTLS, Web Security Scanner) are Lens-1 names only; their mechanisms are taught in cyber NT-06, "
        "CR-14, WA-11, CR-17 and WA-02."], "C-28 Prop Lock note")
    il = d.one("- **Lab:** Python + SQLite: string-concatenated vs parameterized", start=s, end=d.section_end(s))
    d.insert_after("C-28", "append", il, [
        "- **Shared lab (C-28):** run once as cyber WA-05 / SQL SL-13; SD-35 recalls it. The lab text above is kept."],
        "C-28 shared-lab note")
    ic = d.one("\"hash the bank password\" a valid way", start=s, end=d.section_end(s))
    d.insert_after("C-28", "append", ic, [
        "- **Check owner (C-28):** the replay mechanism is taught by cyber CR-17 / PV-03; SD-35 keeps the question."],
        "C-28 check ownership")

    # ---------- §4.1 note on the SD-04 amendment (C-25) ----------
    i = d.one("| SX-01…SX-13 | taught with the first problem that needs them (see §4.3) | — |")
    d.insert_after("C-25", "append", i, ["", note("C-25", "SD-04's prerequisite `A9` reads as: `Curriculum` A8 "
                   "gives the CAP statement and intuition; A9 gives the formal limits and PACELC (A8 lists \"CAP "
                   "theorem\"). SD-14, SD-15 and SD-17 are PRIMARY at A9 with an A8 forward pointer. The checked "
                   "order is in `primer-binding-table.md` §2.")],
                   "C-25 resolution; Curriculum A8 line \"CAP theorem and its real engineering trade-offs\"")

    # ---------- §4.3 gates (C-33, C-34) ----------
    s43 = d.heading("4.3 Problem prerequisite table")
    fixes = {
        "| **P08** |": ("| A5, A6, B3 (first pass); C2, C6, V-COMP/V-NET (second) |",
                        "| A5 checkpoint: *Single box* + *Users++* networking slice; A6: step 0, then the full "
                        "first-pass outline; B3: second-pass framing (first pass); C2, C6, V-COMP/V-NET (second, "
                        "after Phase 3) |", "C-33"),
        "| **O01** |": ("| A3, A4 | — | O02, P06, Q05 |", "| A4 (recall checkpoint) | — | O02, P06, Q05 |", "C-34"),
        "| **O02** |": ("| A3, A4 | O01 |", "| A4 (recall checkpoint) | O01 |", "C-34"),
        "| **O03** |": ("| A3, A4 | — | (queue", "| A7 (after DP-18 + DP-16 State) | — | (queue", "C-34"),
        "| **O04** |": ("| A3 | — | Q20 |", "| A7 (after F-01…F-04 + PR-01…PR-05 SOLID) | — | Q20 |", "C-34"),
        "| **O05** |": ("| A3 | — | (concurrency", "| A7 (after F-01…F-04 + PR-01…PR-05 SOLID) | — | (concurrency",
                        "C-34"),
        "| **O06** |": ("| A3, A7 | O03", "| A7 | O03", "C-34"),
        "| **O07** |": ("| A3, A4 | O01 |", "| A4 (recall checkpoint) | O01 |", "C-34"),
    }
    for key, (old, new, cid) in fixes.items():
        i = d.one(key, start=s43)
        assert d.L[i].count(old) == 1, (key, d.L[i])
        d.replace_line(cid, "correction", i, d.L[i].replace(old, new),
                       f"{cid} resolution (gate column only); O03 patterns = DP-18 Chain of Responsibility + DP-16 "
                       "State (design-patterns-companion.md §6.3)", what=f"§4.3 row {key.strip('| *')}")

    # ---------- P08 checkbox labels (C-33) ----------
    i = d.one("- [ ] first pass (outline, during A5/A6/B3) · [ ] second pass (capstone, after Phase 3)")
    d.replace_line("C-33", "correction", i,
                   "- [ ] A5 checkpoint (*Single box* + *Users++* networking slice) · [ ] A6 step 0 · [ ] first pass "
                   "(full outline, after A6) · [ ] second pass (capstone, after Phase 3)",
                   "C-33: A5 = Single box + networking slice; A6 = step 0; full first pass after A6; second pass after "
                   "Phase 3", what="P08 checkbox line")

    # ---------- O-problems: timing + AP cross-reference (C-34) ----------
    i = d.one("The primer's OOD code is **interview-sketch quality**.")
    d.insert_after("C-34", "append", i, ["", note("C-34", "O01, O02 and O07 are A4 recall checkpoints (practice, "
                   "not re-teaching). O03–O06 are A7 checkpoints: O03 after DP-18 Chain of Responsibility and DP-16 "
                   "State; O04 and O05 after F-01…F-04 and SOLID (PR-01…PR-05); O06 after SD-12. The \"defects to "
                   "find\" lists double as anti-pattern practice: cross-reference design-patterns AP-01…AP-10 "
                   "(`design-patterns-companion.md` §8). Card text unchanged.")], "C-34 resolution")

    # ---------- §4.5 ladder regeneration (C-24/C-33/C-34) ----------
    s45 = d.heading("4.5 The ladder")
    ph = {"**Phase 0": [a for a in binding.ORDER if a.startswith("A")],
          "**Phase 1": [a for a in binding.ORDER if a.startswith("B")],
          "**Phase 2": [a for a in binding.ORDER if a.startswith("C")],
          "**Phase 3": [a for a in binding.ORDER if a.startswith("D")],
          "**Phase 4": ["Phase 4"]}
    for key, anchors_ in ph.items():
        i = d.one("| " + key, start=s45)
        cells = [c.strip() for c in d.L[i].strip("|").split("|")]
        cell = binding.ladder_cell(anchors_, hard)
        rc = []
        for a in anchors_:
            _, _, _, r = binding.bindings_at(a, hard)
            if r:
                rc.append(f"{a}: " + ", ".join(f"{x}~" for _, x, _ in r))
        if key == "**Phase 4":
            cell = (cell + " · " if cell else "") + "V-STOR, V-NET, V-DATA at Lens-3"
        elif rc:
            cell = (cell + " · " if cell else "") + "recall — " + " · ".join(rc)
        probs = cells[2]
        if key == "**Phase 0":
            probs = ("**O01, O02, O07** (A4 recall checkpoints, C-34), **Q21**; **P08** A5 checkpoint (*Single box* "
                     "+ *Users++* networking slice) and A6 step 0, then **P08 first pass** (full outline, after A6; "
                     "C-33); **O03, O04, O05, O06** (A7, after the design-patterns modules they exercise; C-34); "
                     "**P01** (after A7/A8); **Q17** (after A1 + SX-02); **Q08** (= P01)")
        if key == "**Phase 1":
            probs = probs + "; P08 second-pass framing (B3)"
        new = f"| {cells[0]} | {cell} | {probs} |"
        d.replace_line("C-24", "regenerate", i, new, "primer-binding-table.md; C-33; C-34",
                       what=f"§4.5 ladder row {cells[0]}")
    i = d.one("The order follows the prerequisite table (§4.3)", start=s45)
    d.insert_after("C-24", "append", i, ["", f"*Column 2 of the Phase 0–4 rows is generated from "
                   f"`primer-binding-table.md` ({DATE}, C-24): `ID[slice]` = a named ingredient taught before the "
                   "concept's full session; `ID~` = recall. The pre-refactor rows are in the D3 archive.*"],
                   "C-24 derivation note")
    return d


# ------------------------------------------------------------------------------------------------ main
def main():
    root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
    src = os.path.join(root, "inputs-original")
    work = os.path.join(root, "work")
    outd = os.path.join(root, "outputs", "r2")
    os.makedirs(outd, exist_ok=True)
    renamed = {}
    for f in [CUR, PRI, SQL, DPC, SEC, LED, SKL]:
        orig, cur, events, code_hits = rename.process(os.path.join(src, f), f)
        assert not code_hits or f in (SQL,), (f, code_hits[:3])
        renamed[f] = cur
    # binding.py parses the renamed, pre-repair primer
    tmp_primer = os.path.join(outd, "primer-renamed-pre-repair.md")
    open(tmp_primer, "w", encoding="utf-8").write("\n".join(renamed[PRI]))
    errors, notes, topo, hard, cand = binding.check(tmp_primer)
    if errors:
        raise SystemExit(f"binding.py errors: {errors}")
    open(os.path.join(root, "primer-binding-table.md"), "w", encoding="utf-8").write(
        binding.table_md(errors, notes, topo, hard, cand))

    # renamed-only snapshot: rename_checks.py runs here (the repairs below add Curriculum C-track anchors on purpose)
    snap = os.path.join(outd, "renamed")
    os.makedirs(snap, exist_ok=True)
    for f, cur in renamed.items():
        open(os.path.join(snap, f), "w", encoding="utf-8").write("\n".join(cur))
    prefs = ledger_prefs(renamed[LED])
    docs = {f: Doc(f, renamed[f]) for f in renamed}
    build_primer(docs[PRI], prefs, tmp_primer)
    r2_cur.build_curriculum(docs[CUR], prefs)
    r2_sql.build_sql(docs[SQL], prefs, root)
    r2_sec.build_sec(docs[SEC], prefs)
    r2_dp.build_dp(docs[DPC], prefs)

    for f, d in docs.items():
        out = d.finish()
        open(os.path.join(work, f), "w", encoding="utf-8").write("\n".join(out))
    northstar.build(root)
    with open(os.path.join(outd, "journal.jsonl"), "w", encoding="utf-8") as fh:
        for k, j in enumerate(JOURNAL, 1):
            fh.write(json.dumps({"n": k, **j}, ensure_ascii=False, sort_keys=True) + "\n")
    stats = reports.build(root, [{"n": k, **j} for k, j in enumerate(JOURNAL, 1)])
    print(f"r2_build: {len(JOURNAL)} journaled edits; diff +/- lines: "
          + ", ".join(f"{f.split('-')[0].split('.')[0]} +{a}/-{b}" for f, (a, b) in stats.items()))


if __name__ == "__main__":
    main()
