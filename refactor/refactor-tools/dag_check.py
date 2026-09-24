#!/usr/bin/env python3
"""R4 (C-65, meta prompt §12.5): the global prerequisite DAG, built from the six parts' own prerequisite statements.

Usage:  dag_check.py ROOT [--json OUT.json] [--ledger]      (verify.py writes ROOT/dag.json through this module)

Sources merged into one graph (edge kinds: hard = must come first; soft = helps first; lab = a build lab in one part
needs a card of another part, which orders the lab, not the concept):
  primer    §4.1 text table: "Must know first" → hard, "Helps first" → soft (the mermaid spine is a subset of it,
            which verify.py already checks).
  patterns  §10 dependency gate: each numbered step after the one before it; "requires A9" → hard.
  go        §2 primary-landing row "GO-01…GO-14, in order" → a chain; §12 dependency gate: "A → B", "X needs Y", "X after Y", "not before Y", "owners … for X" → hard;
            step 12 (other parts' labs written in Go) → lab.
  sql       §6 exercise-level gates: level n needs level n-1 and the IDs its gate names → hard.
  cyber     "(gate for X)" and "after X" in stitch headers → hard; §6's capstone line → hard.
  ledger    the done-set: the modules marked done, the module in progress and the cards it lists as folded in. Under
            D2 (fresh start) that set is empty and the old ticks are only recorded; --ledger merges them (for the
            session-close run of §13.9, once a real ledger exists).
Not merged, with the reason: the SQL and cyber readiness tiers and skip-test tables (they name what to re-run
after a failed skip-test, not what must come first); Prop Lock lines naming products or controls (no ID on one
side); the M/U/S tracks (withdrawn by D16).

Checks (§12.5):
  1. the graph has no cycles;
  2. no PRIMARY binding comes before its hard prerequisites: for a hard edge p → s, the module that teaches p in
     full (or p itself, when p is a module) comes no later than the module that teaches s in full, in the suite
     order the primer binding table uses (A1…A11, B, C, D, Phase 4, Part V). A primer prerequisite also passes
     when it has a slice at or before that module (the C-25 rule binding.py applies);
  3. every ID in the graph exists: a heading-defined ID, a design-patterns card label, a main-course module, or a
     gate node its source defines (an SQL exercise level).
Plus the ledger: every done card's hard card prerequisites are done, and its module prerequisites are done or in
progress. Deterministic; no timestamps.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import binding  # noqa: E402
import budget   # noqa: E402

ORDER = ([f"A{i}" for i in range(1, 12)] + [f"B{i}" for i in range(1, 6)] + [f"C{i}" for i in range(1, 8)]
         + [f"D{i}" for i in range(1, 5)] + ["Phase 4"])          # binding.py's order, without the Part V rows
RANK = {m: i for i, m in enumerate(ORDER)}
ID = r"(?<![\w-])((?:[A-Z]{1,4}(?:-[A-Z])?-(?:CAP|P)?\d{1,2}[a-z]?)|[A-D]\d{1,2})(?![\w-])"
MODRX = re.compile(r"(?<![\w-])([A-D]\d{1,2}|Phase 4)(?![\w-])")


def ids(s):
    """IDs and modules named in s, ranges expanded; parentheticals dropped."""
    s = re.sub(r"\([^)]*\)", "", s)
    out = set(re.findall(ID, s)) | budget.expand(s)
    return {x for x in out if not re.fullmatch(r"[A-D]\d{1,2}", x) or x in RANK}


def section(text, start, stop=r"^## "):
    m = re.search(start + r".*?(?=" + stop + r"|\Z)", text, re.M | re.S)
    return m.group(0) if m else ""


def build(root, honour_ledger=False):
    rd = lambda f: open(os.path.join(root, "work", f), encoding="utf-8").read()
    pri, dp, sql, sec, go, cur, led = (rd(f) for f in (
        "system-design-primer-companion.md", "design-patterns-companion.md", "sql-databases-companion.md",
        "cloud-cybersecurity-companion.md", "go-language-companion.md", "Curriculum.md", "session-progress-ledger.md"))
    E = []   # (from, to, kind, source)

    def add(ps, s, kind, src):
        for p in sorted(ps):
            if p != s:
                E.append((p, s, kind, src))

    # primer §4.1 text table
    for l in section(pri, r"^### 4\.1 ", r"^### 4\.2 ").split("\n"):
        c = [x.strip() for x in l.strip().strip("|").split("|")] if l.startswith("|") else []
        if len(c) == 3 and re.match(r"SD-\d", c[0]):
            s = re.match(r"(SD-\d+)", c[0]).group(1)
            hard = ids(c[1])
            am = binding.PREREQ_AMEND.get(s)
            if am:   # C-25: the primer's own note under §4.1 reads SD-04's `A9` as `A8`
                hard = (hard - am["drop_mod"]) | am["add_mod"]
            add(hard, s, "hard", "primer §4.1")
            add(ids(c[2]), s, "soft", "primer §4.1")
    # patterns §10: each step after the previous one
    prev = set()
    for l in section(dp, r"^## 10\. ").split("\n"):
        m = re.match(r"^\d+\. (.*)", l)
        if not m:
            continue
        body = m.group(1)
        side = "hold back" in body     # a held-back step is a side branch: the next step follows the one before it
        before = prev
        groups = [ids(g) - set(RANK) for g in re.split(r" → ", re.split(r" — | \(", body)[0])]
        for g in groups:
            for s in g:
                add(prev, s, "hard", "patterns §10")
            prev = g
        for s in prev:
            add({x for x in MODRX.findall(body.split(" — ", 1)[-1]) if x in RANK}, s, "hard", "patterns §10")
        if side:
            prev = before
    # go §12
    for l in section(go, r"^## 12\. ").split("\n"):
        m = re.match(r"^(\d+)\. (.*)", l)
        if not m:
            continue
        n, body = int(m.group(1)), m.group(2)
        kind = "lab" if n == 12 else "hard"
        for cl in re.split(r"; |\. |: |, and ", body):
            chain = re.findall(r"(GO-\d+)(?= →)|(?<=→ )(GO-\d+)", cl)
            chain = [a or b for a, b in chain]
            for a, b in zip(chain, chain[1:]):
                add({a}, b, kind, "go §12")
            nb = re.search(r"not before (GO-\d+)", cl)
            if nb and chain:
                add({nb.group(1)}, chain[0], kind, "go §12")
            # "X needs Y", "X after Y", "X's needs Y", "X build lab needs Y" (no other ID between X and the verb)
            for x in re.finditer(r"([A-Z]{2,4}-(?:CAP|P)?\d+)(?:(?![A-Z]{2,4}-(?:CAP|P)?\d)[^,;])*? (?:needs|after) (.*)", cl):
                add(ids(x.group(2)), x.group(1), kind, "go §12")
            for x in re.finditer(r"owners at least `taught`[:,] (.*)", body):
                for part in re.split(r", and |; ", x.group(1)):
                    for y in re.finditer(r"(.*?) for (GO-\d+)", part):
                        add(ids(y.group(1)), y.group(2), "hard", "go §12")
    # go §2: the primary-landing row teaches its range "in order"
    for x in re.finditer(r"\*\*(GO-\d+…GO-\d+)\*\*, in order", section(go, r"^## 2\. ")):
        seq = sorted(budget.expand(x.group(1)))
        for a, b in zip(seq, seq[1:]):
            add({a}, b, "hard", "go §2")
    # sql §6 level gates ("X after Y" inside a gate orders X; an exercise SQL-En.m stands for its level SQL-En)
    for x in re.finditer(r"^### 6\.(\d+) Level \d+ .*?\n\n\*\*Prereq gate:\*\* (.*)$", sql, re.M):
        lvl = f"SQL-E{x.group(1)}"
        for seg in x.group(2).split("; "):
            seg = re.sub(r"([A-Z]{2}-)(\d+)/(\d+)", r"\1\2, \g<1>\3", seg)          # SL-05/08 → SL-05, SL-08
            lv = {f"SQL-E{n}" for n in re.findall(r"SQL-E(\d+)", seg)}
            seg = re.sub(r"SQL-E\d+(?:\.\d+)?", " ", seg)
            a = re.match(r"\s*(SQL-CAP\d) after(.*)", seg)
            if a:
                add(lv | (ids(a.group(2)) - {a.group(1)}), a.group(1), "hard", "sql §6")
            else:
                add(lv | ids(seg), lvl, "hard", "sql §6")
    # cyber: stitch-header gates and the capstone line
    for l in sec.split("\n"):
        h = re.match(r"^#### ([A-Z]{2,4}(?:-[A-Z])?-\d+) · .*— stitch: (.*)", l)
        if h:
            for g in re.findall(r"gate for ([A-Z]{2,4}-\d+)", h.group(2)):
                add({h.group(1)}, g, "hard", "cyber stitch")
            for g in re.findall(r"after ([A-Z0-9/-]+)", h.group(2)):
                add(ids(g.replace("/", " ")), h.group(1), "hard", "cyber stitch")
        if l.startswith("Run **SEC-CAP1**"):
            for x in re.finditer(r"\*\*(SEC-CAP\d)\*\* after ([^;.]*)", l):
                add(ids(x.group(2).replace("/", " ").replace("+", " ")), x.group(1), "hard", "cyber §6")
    # ledger done-set
    done_mods = set(re.findall(r"^- \[x\] \*\*([A-D]\d{1,2})\b", led, re.M))
    prog = re.search(r"in progress: \*\*([A-D]\d{1,2})\b", led)
    folded = re.search(r"\*\*Stitched-in companion content already folded.*", led)
    done_cards = set(re.findall(r"(?<![\w-])(SD-\d+)", folded.group(0))) if folded else set()
    for a, b in re.findall(r"(SD-\d+)/(SD-\d+)", folded.group(0) if folded else ""):
        done_cards |= {a, b}
    found = {"done_modules": sorted(done_mods), "in_progress": prog.group(1) if prog else None,
             "done_cards": sorted(done_cards)}
    # D2: the revamp starts fresh, so nothing on the old ledger counts as done; its ticks are recorded, not merged
    ledger = found if honour_ledger else {"done_modules": [], "in_progress": None, "done_cards": [],
                                          "ignored_under_D2": found}

    # PRIMARY: primer §2 PRIMARY column, cyber §2 primary column, patterns §2, else the first module of the header
    primary, pslice = {}, {}
    for f, t, col in (("pri", pri, 1), ("sec", sec, 1), ("dp", dp, 1), ("sql", sql, 1), ("go", go, 1)):
        for l in section(t, r"^## 2\. ").split("\n"):
            if not l.startswith("|") or set(l) <= set("|-: "):
                continue
            c = [x.strip() for x in l.strip().strip("|").split("|")]
            mods = [m for m in MODRX.findall(c[0]) if m in RANK] or (["Phase 4"] if "Phase 4" in c[0] else [])
            if not mods:
                continue
            m0 = min(mods, key=RANK.get)
            cell = c[col]
            if f == "go" and "Primary landing" not in l:
                continue   # the other Go rows are renderings taught "once the Go companion reaches them" (§12 order)
            if f == "sql":
                cell = " · ".join(g for g in re.split(r" · |; |\. ", cell) if not budget.SKIP.search(g))
            if f == "dp":
                cell = " · ".join(s for s in re.split(r"\. ", cell)
                                  if not re.search(r"taught in the ([A-D]\d{1,2}) session", s)
                                  or m0 in re.findall(r"taught in the ([A-D]\d{1,2}) session", s))
                cell = re.sub(r"\(recall[^)]*\)", "", cell)
            for i in ids(cell) - set(RANK):
                if i not in primary or RANK[m0] < RANK[primary[i]]:
                    primary[i] = m0
            if f == "pri" and len(c) > 2:
                for i in re.findall(r"(SD-\d+)\[", c[2]):
                    pslice.setdefault(i, set()).add(m0)
    for t in (sql, sec):
        for l in t.split("\n"):
            h = re.match(r"^#{3,4} ([A-Z]{2,4}(?:-[A-Z])?-\d{1,2}) · .*— stitch: (.*)", l)
            if h and h.group(1) not in primary:
                ms = MODRX.findall(h.group(2))
                if ms and ms[0] in RANK:
                    primary[h.group(1)] = ms[0]
                elif "Phase 4" in h.group(2).split(" · ")[0]:
                    primary[h.group(1)] = "Phase 4"

    # registry
    reg = set(RANK)
    for f in budget.COMP + ["Curriculum.md"]:
        for l in rd(f).split("\n"):
            m = re.match(r"^#{2,5} (?:\[[ x]\] )?([A-Z]{1,4}(?:-[A-Z])?-(?:CAP|P)?\d{1,2}[a-z]?)\b", l)
            if m:
                reg.add(m.group(1))
            lb = budget.LABEL.match(l)
            if lb:
                reg.add(lb.group(1))
            for d in re.findall(r"^- (?:\[[ x]\] )?\*\*(GO-CAP\d+) · |\*\*Involved problem (GO-P\d+):\*\*", l):
                reg |= {x for x in d if x}
    reg |= {f"SQL-E{n}" for n in re.findall(r"^### 6\.(\d+) Level", sql, re.M)}   # gate nodes: exercise levels
    E = sorted(set(E))
    return {"schema": "dag/1", "edges": [{"from": a, "to": b, "kind": k, "source": s} for a, b, k, s in E],
            "primary": dict(sorted(primary.items())), "primer_slices": {k: sorted(v) for k, v in sorted(pslice.items())},
            "ledger": ledger}, reg


def check(dag, reg):
    E = [(e["from"], e["to"], e["kind"]) for e in dag["edges"]]
    nodes = sorted({x for a, b, _ in E for x in (a, b)})
    # 1. cycles over the must-come-first edges (hard + lab). A soft ("helps first") edge is advice; one that runs
    #    against a must-come-first path cannot be followed and is reported, not failed
    adj = {}
    for a, b, k in E:
        if k != "soft":
            adj.setdefault(a, []).append(b)
    colour, cycles = {}, []

    def dfs(u, stack):
        colour[u] = 1
        stack.append(u)
        for v in sorted(adj.get(u, [])):
            if colour.get(v) == 1:
                cycles.append(stack[stack.index(v):] + [v])
            elif not colour.get(v):
                dfs(v, stack)
        stack.pop()
        colour[u] = 2
    sys.setrecursionlimit(10000)
    for u in nodes:
        if not colour.get(u):
            dfs(u, [])
    reach = {}

    def down(u):
        if u not in reach:
            reach[u] = set()
            for v in adj.get(u, []):
                reach[u] |= {v} | down(v)
        return reach[u]
    soft_back = sorted(f"{a} ⇢ {b} (but {b} must come before {a})" for a, b, k in E if k == "soft" and a in down(b))
    # 2. PRIMARY order
    P = dag["primary"]
    home = lambda x: x if x in RANK else P.get(x)
    bad, checked, unplaced = [], 0, set()
    for a, b, k in E:
        if k != "hard" or b in RANK:
            continue
        hb, ha = home(b), home(a)
        if hb is None or ha is None:
            unplaced |= {x for x, h in ((a, ha), (b, hb)) if h is None}
            continue
        checked += 1
        if RANK[ha] > RANK[hb] and not any(RANK[m] <= RANK[hb] for m in dag["primer_slices"].get(a, ())):
            bad.append(f"{a}@{ha} → {b}@{hb}")
    # 3. unknown IDs
    base = lambda x: re.sub(r"(-\d+)[a-z]$", r"\1", x)
    unknown = sorted(x for x in nodes if x not in reg and base(x) not in reg)
    # ledger
    L = dag["ledger"]
    ok_mod = set(L["done_modules"]) | ({L["in_progress"]} if L["in_progress"] else set())
    lbad = []
    for c in L["done_cards"]:
        for a, b, k in E:
            if b == c and k == "hard" and not (a in L["done_cards"] or a in ok_mod):
                lbad.append(f"{c} needs {a}")
    return {"nodes": len(nodes), "edges": len(E), "by_kind": {k: sum(e[2] == k for e in E) for k in ("hard", "soft", "lab")},
            "cycles": cycles, "soft_against_hard": soft_back, "order_checked": checked, "order_bad": bad, "unplaced": sorted(unplaced),
            "unknown": unknown, "ledger_bad": lbad}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    root = os.path.abspath(args[0] if args else ".")
    dag, reg = build(root, honour_ledger="--ledger" in sys.argv)
    r = check(dag, reg)
    if "--json" in sys.argv:
        json.dump(dag, open(sys.argv[sys.argv.index("--json") + 1], "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(json.dumps(r, indent=1, ensure_ascii=False))
    sys.exit(1 if r["cycles"] or r["order_bad"] or r["unknown"] or r["ledger_bad"] else 0)


if __name__ == "__main__":
    main()
