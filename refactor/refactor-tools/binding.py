#!/usr/bin/env python3
"""C-24/C-25/C-35 primer binding table: the single source for the primer's header stitches, §2 table and §4.5 ladder.

Usage:
  binding.py PRIMER_SOURCE.md [--table OUT.md] [--json OUT.json]
    PRIMER_SOURCE is the renamed, pre-repair primer (r2_build passes it in memory; R3 re-derives it
    from inputs-original + rename.py). Exits 1 if any check fails.

Kinds (C-24 notation):
  PRIMARY  `ID@X`          the session that teaches the concept in full (exactly one per ID)
  SLICE    `ID[label]@X`   the session teaches one named ingredient (before or after PRIMARY)
  FWD      `ID[forward pointer]@X`  named, not taught (C-25 "A8 gives a forward pointer only"; C-33)
  RECALL   `ID~X`          a one-line reference back after PRIMARY

Checks:
  1. exactly one PRIMARY per SD-00…SD-39 and SX-01…SX-13
  2. nothing dropped: every anchor the primer used for an ID (header ∪ §2 ∪ §4.5, Part V categories mapped
     to V-IDs) appears in that ID's bindings (§4.5 "A3/A4" group cells count as satisfied by either module)
  3. C-25 topological check: for every hard prerequisite p of s (§4.1 "must know first", with the C-25 SD-04
     amendment), PRIMARY(p) ≤ PRIMARY(s), or p has a SLICE at ≤ PRIMARY(s) that declares it serves s;
     every module prerequisite m satisfies m ≤ PRIMARY(s)
  4. same-anchor order: PRIMARY items within one anchor are emitted in a topological order of §4.1
Idempotent; no randomness; output sorted.
"""
import json, re, sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import primer_bindings as pb  # noqa: E402

ORDER = ([f"A{i}" for i in range(1, 12)] + [f"B{i}" for i in range(1, 6)] + [f"C{i}" for i in range(1, 8)]
         + [f"D{i}" for i in range(1, 5)] + ["Phase 4"]
         + ["V-COMP", "V-STOR", "V-NET", "V-DATA", "V-AI", "V-SEC", "V-OPS", "Part V cert 8"])
RANK = {m: i for i, m in enumerate(ORDER)}
VMAP = {"Compute": "V-COMP", "Storage/DB": "V-STOR", "Storage": "V-STOR", "Networking": "V-NET",
        "Data/Analytics": "V-DATA", "AI/ML": "V-AI", "Security": "V-SEC", "Ops": "V-OPS", "Ops/DevOps": "V-OPS"}
V_ALL = ["V-COMP", "V-STOR", "V-NET", "V-DATA", "V-AI", "V-SEC", "V-OPS"]


def P(a):
    return ("PRIMARY", a, "", ())


def S(a, label, serves=()):
    return ("SLICE", a, label, tuple(serves))


def F(a, label="forward pointer"):
    return ("FWD", a, label, ())


def Rc(a, note=""):
    return ("RECALL", a, note, ())


# Refactor-authored binding decisions (R2, 2026-09-24). Slice labels quote the primer's own §2 wording where it
# had one; otherwise they name the ingredient in a few words. Evidence per row: primer header / §2 / §4.5 / §4.1,
# plus C-25, C-26, C-27, C-33, C-35, C-42 of the refactor prompt.
B = {
    "SD-00": [P("A2"), Rc("A11", "iterative loop: benchmark → profile → fix → repeat"), Rc("B3"),
              Rc("C4", "iterative delivery"), Rc("V-OPS", "the SD-00 loop")],
    "SD-01": [S("A5", "clones + single-box ceiling slice", ["SD-10"]), P("A6"), Rc("B2", "clones"),
              Rc("C1", "clones"), Rc("V-COMP")],
    "SD-02": [S("A2", "proportional-scaling arithmetic"),
              S("A5", "performance-vs-scalability slice", ["SD-10", "SD-04"]), Rc("A7"), P("B3")],
    "SD-03": [S("A2", "throughput/latency arithmetic; Little's law sizing"), P("B3"),
              Rc("C6", "tail latency"), Rc("C7", "percentiles")],
    "SD-04": [P("A8"), S("A9", "formal limits + PACELC")],
    "SD-05": [S("A8", "strong vs eventual consistency as the C in CAP", ["SD-20"]), P("A9")],
    "SD-06": [F("A5", "P08 Users++ networking slice"), P("A9"),
              Rc("B3", "active-passive ≈ warm standby/pilot light; active-active ≈ multi-site"),
              Rc("C4", "blue-green/canary ↔ active-active/passive"), Rc("C7", "fail-over")],
    "SD-07": [S("A2", "availability math: series vs parallel, nines"), P("A9"), Rc("B3"),
              Rc("C7", "nines ↔ SLO/error budget")],
    "SD-08": [P("A5"), Rc("V-NET")],
    "SD-09": [P("A5"), Rc("B4", "CDN cost vs origin cost"), Rc("V-NET")],
    "SD-10": [P("A5"), Rc("B2", "horizontal scaling from identical images"), Rc("B3", "vertical vs horizontal"),
              Rc("C1", "stateless servers"), Rc("C2", "Service/Ingress = L4/L7; HPA"), Rc("C3"),
              Rc("V-COMP", "MIG + autoscaling"), Rc("V-NET")],
    "SD-11": [P("A5"), Rc("C2"), Rc("C3", "reverse proxy in NGINX"), Rc("V-NET")],
    "SD-12": [F("A5", "P08 Users++ networking slice"), P("A7"),
              Rc("B5", "service-to-service auth"), Rc("C2", "Services, CoreDNS"), Rc("C3"), Rc("V-COMP")],
    "SD-13": [P("A8"), Rc("V-STOR")],
    "SD-14": [F("A8"), P("A9"), Rc("C2", "StatefulSet ↔ stateful tier"), Rc("V-STOR")],
    "SD-15": [F("A8"), P("A9"), Rc("V-STOR")],
    "SD-16": [S("A7", "functional partitioning as service decomposition"),
              S("A8", "split databases by function: schema view"), P("A9"), Rc("V-STOR")],
    "SD-17": [F("A8"), P("A9"), Rc("V-STOR")],
    "SD-18": [S("A8", "denormalization as the inverse of normalization"), P("A9"), Rc("V-STOR")],
    "SD-19": [S("A4", "B-tree index slice"), S("A6", "profiling tools"), P("A8"),
              Rc("C6", "benchmark/profile"), Rc("V-OPS"), Rc("V-STOR")],
    "SD-20": [P("A8"), Rc("A9", "BASE ↔ eventual consistency"), Rc("V-STOR")],
    "SD-21": [S("A3", "dict as a hash table"), S("A4", "hash-table slice"), P("A8"),
              Rc("C2", "StatefulSet ↔ stateful tier"), Rc("V-STOR")],
    "SD-22": [P("A8"), Rc("V-STOR")],
    "SD-23": [P("A8"), Rc("A9"), Rc("V-STOR")],
    "SD-24": [S("A4", "graph representation slice"), P("A8"), Rc("V-STOR")],
    "SD-25": [S("A8", "SQL-vs-NoSQL decision lists, family level"), P("A9"), Rc("V-STOR"),
              Rc("Part V cert 8", "Cloud Database Engineer")],
    "SD-26": [S("A5", "HTTP-layer caching slice: client/browser cache, Cache-Control/ETag, CDN-as-cache, "
                      "reverse-proxy cache"), P("A8"), Rc("B4", "cache vs DB cost"),
              Rc("C3", "NGINX/Varnish web-server cache"), Rc("V-STOR")],
    "SD-27": [S("A3", "cache-aside code"), P("A9"), Rc("V-STOR")],
    "SD-28": [S("A2", "Little's law"), P("A7"), Rc("C7", "back pressure/retries"), Rc("V-COMP", "workers"),
              Rc("V-DATA", "Pub/Sub")],
    "SD-29": [P("A5"), Rc("A7"), Rc("C3")],
    "SD-30": [P("A5"), S("A6", "connection and file-descriptor limits"), Rc("V-NET")],
    "SD-31": [P("A5"), Rc("V-NET")],
    "SD-32": [S("A3", "RPC calls in Python"), P("A7")],
    "SD-33": [S("A3", "REST calls in Python + curl"), P("A7")],
    "SD-34": [S("A3", "REST vs RPC calls in Python + curl"), P("A7")],
    "SD-35": [S("A5", "transit-encryption slice (TLS in transit)"), P("A10"), Rc("B5", "least privilege"),
              Rc("C3", "TLS termination"), Rc("V-SEC")],
    "SD-36": [P("A1")],
    "SD-37": [P("A1"), Rc("A6", "memory/disk numbers"), Rc("C6")],
    "SD-38": [S("A4", "consistent-hash ring slice (SD-38a)"), P("A9"), Rc("V-DATA", "MapReduce → Dataflow/Dataproc")],
    "SD-39": [P("A9"), Rc("C6", "Dapper")] + [Rc(v) for v in V_ALL],
    # SX: PRIMARY at the first problem that introduces it (§4.3 "New here"; C-35)
    "SX-01": [P("A8"), Rc("B4", "storage tiering"), Rc("V-STOR")],
    "SX-02": [S("A2", "62^7 key-space math"), S("A3", "Base62 code"), P("A8")],
    "SX-03": [P("A8"), Rc("V-DATA", "log analytics → BigQuery")],
    "SX-04": [P("A8")],
    "SX-05": [P("Phase 4")],
    "SX-06": [P("D4"), Rc("Phase 4")],
    "SX-07": [S("A4", "heaps/sorted sets"), P("Phase 4")],
    "SX-08": [P("Phase 4"), Rc("V-DATA", "log analytics → BigQuery")],
    "SX-09": [S("A4", "heaps"), P("Phase 4")],
    "SX-10": [S("A4", "BFS slice"), P("Phase 4")],
    "SX-11": [P("A4")],
    "SX-12": [P("A6")],
    "SX-13": [P("Phase 4")],
}

# the problem through which each SX is taught (first problem that introduces it, §4.3 "New here")
SX_VIA = {"SX-01": "P01", "SX-02": "P01", "SX-03": "P01", "SX-04": "P01", "SX-05": "P02", "SX-06": "Q02",
          "SX-07": "P03", "SX-08": "P07", "SX-09": "P04", "SX-10": "P05", "SX-11": "O02", "SX-12": "P08",
          "SX-13": "P04"}

# C-25: "The primer's hard prerequisite 'A9' becomes: A8 gives the statement and intuition; A9 gives the
# formal limits (§9.2.2) and PACELC."
PREREQ_AMEND = {"SD-04": {"drop_mod": {"A9"}, "add_mod": {"A8"}}}

ALL_IDS = [f"SD-{i:02d}" for i in range(40)] + [f"SX-{i:02d}" for i in range(1, 14)]


def primary(i):
    return [b for b in B[i] if b[0] == "PRIMARY"][0][1]


def hard_prereqs(hard):
    out = {}
    for s, pre in hard.items():
        mods = set(pre["mod"])
        am = PREREQ_AMEND.get(s)
        if am:
            mods = (mods - am["drop_mod"]) | am["add_mod"]
        out[s] = {"sd": set(pre["sd"]), "mod": mods}
    return out


def candidates(path):
    """union of header, §2 and §4.5 anchors per ID, with Part V categories mapped to V-IDs"""
    header, table, ladder, _ = pb.parse(path)
    lines = open(path, encoding="utf-8").read().split("\n")
    cand = {i: set() for i in ALL_IDS}
    groups = {i: [] for i in ALL_IDS}
    for src in (header, table):
        for i, mods in src.items():
            cand.setdefault(i, set()).update(mods)
    for i, mods in ladder.items():
        groups.setdefault(i, []).append(set(mods))
    sec = None
    for ln in lines:
        m = re.match(r"#### (SD-\d{2}) · .*? — stitch: (.*)$", ln)
        if m:
            st = m.group(2)
            for cat, v in VMAP.items():
                if re.search(r"Part V " + re.escape(cat) + r"(?![\w/])", st):
                    cand[m.group(1)].add(v)
            if "Part V (all)" in st:
                cand[m.group(1)].update(V_ALL)
            if "Cloud Database Engineer" in st:
                cand[m.group(1)].add("Part V cert 8")
        if ln.startswith("## 2. Stitch table"):
            sec = "s2"
        elif ln.startswith("### 2.1"):
            sec = None
        if sec == "s2" and ln.startswith("| **Part V — "):
            cells = [c.strip() for c in ln.strip("|").split("|")]
            cat = re.match(r"\*\*Part V — ([^*(]+?)\*\*", cells[0]).group(1).strip()
            for i in pb.ids_in(cells[1]):
                cand.setdefault(i, set()).add(VMAP[cat])
    # §4.5 cells "A3/A4: …" are one group: satisfied by either module
    return cand, groups


def check(path):
    _, _, _, hard = pb.parse(path)
    hard = hard_prereqs(hard)
    cand, groups = candidates(path)
    errors, notes = [], []
    for i in ALL_IDS:
        ps = [b for b in B[i] if b[0] == "PRIMARY"]
        if len(ps) != 1:
            errors.append(f"{i}: {len(ps)} PRIMARY bindings")
        anchors = {b[1] for b in B[i]}
        for a in sorted(cand.get(i, ()), key=lambda x: RANK.get(x, 99)):
            if a not in anchors:
                errors.append(f"{i}: candidate anchor {a} dropped")
        for g in groups.get(i, []):
            if not (g & anchors):
                errors.append(f"{i}: §4.5 group {sorted(g)} not represented")
        p = primary(i)
        if p not in cand.get(i, set()) and not any(p in g for g in groups.get(i, [])):
            notes.append(f"{i}: PRIMARY {p} is outside the primer's candidate set (C-25 cascade / C-27 / C-35)")
    topo = []
    for s in sorted(hard):
        ps = primary(s)
        for m in sorted(hard[s]["mod"], key=lambda x: RANK.get(x, 99)):
            if RANK[m] > RANK[ps]:
                errors.append(f"C-25 {s}@{ps} before module prerequisite {m}")
        for p in sorted(hard[s]["sd"]):
            pp = primary(p)
            if RANK[pp] <= RANK[ps]:
                topo.append((s, p, f"{p}@{pp}"))
                continue
            sl = [b for b in B[p] if b[0] == "SLICE" and s in b[3] and RANK[b[1]] <= RANK[ps]]
            if sl:
                topo.append((s, p, f"{p}[{sl[0][2]}]@{sl[0][1]}"))
            else:
                errors.append(f"C-25 {s}@{ps} before prerequisite {p}@{pp} (no serving slice)")
    return errors, notes, topo, hard, cand


def anchor_order(hard):
    """PRIMARY items per anchor, topologically sorted by §4.1 hard prerequisites (ties by ID)"""
    per = {}
    for i in ALL_IDS:
        per.setdefault(primary(i), []).append(i)
    out = {}
    for a, ids in per.items():
        ids = sorted(ids)
        done, seq = set(), []
        while len(seq) < len(ids):
            for i in ids:
                if i in done:
                    continue
                deps = hard.get(i, {}).get("sd", set()) & set(ids)
                if deps <= done:
                    seq.append(i)
                    done.add(i)
                    break
            else:
                raise SystemExit(f"cycle in anchor {a}")
        out[a] = seq
    return out


def bindings_at(a, hard):
    """(kind, id, label) for anchor a, in teaching order: slices/forward pointers first, then PRIMARY in topo order,
    then recalls"""
    order = anchor_order(hard)
    pri = order.get(a, [])
    sl = sorted(((b[0], i, b[2]) for i in ALL_IDS for b in B[i] if b[1] == a and b[0] in ("SLICE", "FWD")
                 and RANK[a] < RANK[primary(i)]), key=lambda x: x[1])
    after = sorted(((b[0], i, b[2]) for i in ALL_IDS for b in B[i] if b[1] == a and b[0] == "SLICE"
                    and RANK[a] > RANK[primary(i)]), key=lambda x: x[1])
    rc = sorted(((b[0], i, b[2]) for i in ALL_IDS for b in B[i] if b[1] == a and b[0] == "RECALL"),
                key=lambda x: x[1])
    return sl, [("PRIMARY", i, "") for i in pri], after, rc


def fmt_item(kind, i, label):
    if kind == "PRIMARY":
        return f"{i}@" if False else i
    if kind in ("SLICE", "FWD"):
        return f"{i}[{label}]"
    return f"{i}~" + (f" ({label})" if label else "")


def header_stitch(i):
    """regenerated text after '— stitch: ' in a primer module header"""
    p = primary(i)
    sl = [f"[{b[2]}]@{b[1]}" for b in B[i] if b[0] == "SLICE"]
    fw = [b[1] + ("" if b[2] == "forward pointer" else f" ({b[2]})") for b in B[i] if b[0] == "FWD"]
    rc = [b[1] for b in B[i] if b[0] == "RECALL"]
    out = f"{p} (primary)"
    if sl:
        out += " · slices: " + ", ".join(sl)
    if fw:
        out += " · named only: " + ", ".join(fw)
    if rc:
        out += " · recall: " + ", ".join(rc)
    return out


def row_cells(a, hard):
    sl, pri, after, rc = bindings_at(a, hard)
    c_pri = ", ".join(i + (f" (via {SX_VIA[i]})" if i in SX_VIA else "") for _, i, _ in pri) or "—"
    c_sl = " · ".join((f"{i} *(named only" + ("" if lab == "forward pointer" else f": {lab}") + ")*") if k == "FWD"
                      else f"{i}[{lab}]" for k, i, lab in sl + after) or "—"
    c_rc = " · ".join(f"{i}~" + (f" ({lab})" if lab else "") for _, i, lab in rc) or "—"
    return c_pri, c_sl, c_rc


def ladder_cell(anchors, hard):
    parts = []
    for a in anchors:
        sl, pri, after, rc = bindings_at(a, hard)
        items = [f"{i}[{lab}]" for k, i, lab in sl if k == "SLICE"] + [i for _, i, _ in pri] + \
                [f"{i}[{lab}]" for _, i, lab in after]
        if items:
            parts.append(f"{a}: " + ", ".join(items))
    return " · ".join(parts)


def table_md(errors, notes, topo, hard, cand):
    L = ["# Primer binding table (C-24)", "",
         "Built by `refactor-tools/binding.py` in R2 (2026-09-24). **Refactor-authored**: every row is a binding "
         "decision, not primer text. The primer's module-header stitches, its §2 table and its §4.5 ladder are "
         "generated from this table, so the three cannot drift apart (primer §7.3 maintenance rule, C-41).", "",
         "Notation (C-24): `ID@X` = PRIMARY, the session that teaches the concept in full (exactly one) · "
         "`ID[slice]@X` = SLICE, the session teaches one named ingredient · `ID[forward pointer]@X` = named, not "
         "taught · `ID~X` = RECALL, a one-line reference back.", "",
         "Candidate set: the union of the header stitch, the §2 table and the §4.5 ladder, with `Part V <category>` "
         "mapped to its V-ID (C-22). Nothing is dropped: `binding.py` fails if any candidate anchor is missing. "
         "SX techniques are PRIMARY at the first problem that introduces them (§4.3 \"New here\", C-35).", "",
         f"**Checks (this run):** {len(ALL_IDS)} IDs, one PRIMARY each · candidate anchors dropped: "
         f"{sum('dropped' in e for e in errors)} · C-25 topological violations: "
         f"{sum(e.startswith('C-25') for e in errors)} · total errors: {len(errors)}.", "",
         "## 1. Bindings", "",
         "| ID | PRIMARY | SLICE / forward pointer | RECALL | Primer candidate anchors (header ∪ §2 ∪ §4.5) |",
         "|---|---|---|---|---|"]
    for i in ALL_IDS:
        p = primary(i) + (f" (via {SX_VIA[i]})" if i in SX_VIA else "")
        sl = "; ".join(f"`{i}[{b[2]}]@{b[1]}`" + (" (fwd)" if b[0] == "FWD" else "") for b in B[i]
                       if b[0] in ("SLICE", "FWD")) or "—"
        rc = "; ".join(f"`{i}~{b[1]}`" + (f" ({b[2]})" if b[2] else "") for b in B[i] if b[0] == "RECALL") or "—"
        cd = ", ".join(sorted(cand.get(i, ()), key=lambda x: RANK.get(x, 99))) or "— (SX: §2/§4.5 only)"
        L.append(f"| {i} | `{i}@{primary(i)}`{p[len(primary(i)):]} | {sl} | {rc} | {cd} |")
    L += ["", "## 2. C-25 topological check (hard prerequisites from primer §4.1)", "",
          "Rule: every hard prerequisite `p` of `s` has PRIMARY(p) ≤ PRIMARY(s) in the order A1…A11, B1…B5, C1…C7, "
          "D1…D4, Phase 4, or a SLICE of `p` at or before PRIMARY(s) that is declared to serve `s` (C-25: \"fix it by "
          "adding a named slice earlier\"). Module prerequisites must be ≤ PRIMARY(s). Amendment applied "
          "(C-25): SD-04's module prerequisite `A9` reads as `A8` (statement + intuition), with A9 teaching the formal "
          "limits + PACELC as a slice.", "",
          "| Concept @ PRIMARY | Hard prerequisite | Satisfied by |", "|---|---|---|"]
    for s, p, how in topo:
        L.append(f"| {s} @ {primary(s)} | {p} | `{how}` |")
    L += ["", "Violations: " + ("none." if not any(e.startswith("C-25") for e in errors) else ""), ""]
    for e in errors:
        L.append(f"- ERROR {e}")
    L += ["## 3. Decisions to review (`[resolved-by-default]`)", ""]
    for n in notes:
        L.append(f"- {n} `[resolved-by-default]`")
    L += ["", "## 4. Teaching order inside each session (PRIMARY items, topological by §4.1)", ""]
    for a, seq in sorted(anchor_order(hard).items(), key=lambda x: RANK[x[0]]):
        sl, pri, after, rc = bindings_at(a, hard)
        pre = [f"{i}[{lab}]" for k, i, lab in sl]
        L.append(f"- **{a}:** " + (" → ".join(pre) + " → " if pre else "") + " → ".join(seq))
    return "\n".join(L) + "\n"


def main():
    path = sys.argv[1]
    errors, notes, topo, hard, cand = check(path)
    if "--table" in sys.argv:
        open(sys.argv[sys.argv.index("--table") + 1], "w", encoding="utf-8").write(
            table_md(errors, notes, topo, hard, cand))
    if "--json" in sys.argv:
        json.dump({"bindings": {i: [list(b[:3]) + [list(b[3])] for b in B[i]] for i in ALL_IDS},
                   "errors": errors, "notes": notes}, open(sys.argv[sys.argv.index("--json") + 1], "w"),
                  indent=1, sort_keys=True)
    print(f"binding.py: {len(ALL_IDS)} IDs · errors {len(errors)} · notes {len(notes)} · topo pairs {len(topo)}")
    for e in errors:
        print("  ERROR", e)
    for n in notes:
        print("  NOTE", n)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
