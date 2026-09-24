#!/usr/bin/env python3
"""R0/C-24/C-25 audit: compare the primer's three binding sources and check them against §4.1 hard prerequisites.
Read-only; idempotent. Usage: primer_bindings.py <primer.md> [--json out.json]"""
import re, sys, json

ORDER = [f"A{i}" for i in range(1, 12)] + [f"B{i}" for i in range(1, 6)] + [f"C{i}" for i in range(1, 8)] + [f"D{i}" for i in range(1, 5)]
RANK = {m: i for i, m in enumerate(ORDER)}
MOD = re.compile(r"\b([ABCD](?:1[01]|[1-9]))\b")
SDRANGE = re.compile(r"SD-(\d{2})\s*(?:…|\.\.\.|–|-)\s*SD-(\d{2})")
SDID = re.compile(r"\b(S[DX]-\d{2})[a-c]?\b")


def ids_in(text):
    out = set()
    for a, b in SDRANGE.findall(text):
        out |= {f"SD-{i:02d}" for i in range(int(a), int(b) + 1)}
    text = SDRANGE.sub(" ", text)
    out |= set(SDID.findall(text))
    # "SD-33/34" and "SD-30/31" shorthand
    for a, b in re.findall(r"SD-(\d{2})/(\d{2})", text):
        out.add(f"SD-{b}")
    return out


def parse(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    header, table, ladder, hard = {}, {}, {}, {}
    sec = None
    for n, ln in enumerate(lines, 1):
        if ln.startswith("## 2. Stitch table"): sec = "s2"
        elif ln.startswith("### 2.1"): sec = None
        elif ln.startswith("### 4.1"): sec = "s41"
        elif ln.startswith("### 4.2"): sec = None
        elif ln.startswith("### 4.5"): sec = "s45"
        elif ln.startswith("## 5."): sec = None
        m = re.match(r"#### (S[DX]-\d{2}) · .*? — stitch: (.*)$", ln)
        if m:
            header[m.group(1)] = {x for x in MOD.findall(m.group(2))}
            continue
        if sec == "s2" and ln.startswith("| **") and not ln.startswith("| **Part") and not ln.startswith("| **PCA"):
            cells = [c.strip() for c in ln.strip("|").split("|")]
            mm = re.match(r"\*\*([ABCD]\d+)\*\*", cells[0])
            if mm:
                for i in ids_in(cells[1]):
                    table.setdefault(i, set()).add(mm.group(1))
        if sec == "s45" and ln.startswith("| **Phase 0"):
            cell = [c.strip() for c in ln.strip("|").split("|")][1]
            for part in cell.split(" · "):
                mm = re.match(r"((?:[ABCD]\d+)(?:/[ABCD]\d+)*):\s*(.*)", part.strip())
                if mm:
                    mods = mm.group(1).split("/")
                    for i in ids_in(mm.group(2)):
                        for mo in mods:
                            ladder.setdefault(i, set()).add(mo)
        if sec == "s45" and re.match(r"\| \*\*Phase [123]", ln):
            cell = [c.strip() for c in ln.strip("|").split("|")][1]
            for part in cell.split(" · "):
                mm = re.match(r"((?:[ABCD]\d+)(?:/[ABCD]\d+)*):\s*(.*)", part.strip())
                if mm:
                    for i in ids_in(mm.group(2)):
                        for mo in mm.group(1).split("/"):
                            ladder.setdefault(i, set()).add(mo)
        if sec == "s41" and re.match(r"\| SD-\d{2} ", ln):
            cells = [c.strip() for c in ln.strip("|").split("|")]
            sid = cells[0].split()[0]
            hard[sid] = {"sd": ids_in(cells[1]), "mod": set(MOD.findall(cells[1]))}
    return header, table, ladder, hard


def earliest(mods):
    ms = [m for m in mods if m in RANK]
    return min(ms, key=RANK.get) if ms else None


def main():
    path = sys.argv[1]
    header, table, ladder, hard = parse(path)
    sds = sorted(k for k in header if k.startswith("SD-"))
    disagree = []
    for s in sds:
        h, t, l = header.get(s, set()), table.get(s, set()), ladder.get(s, set())
        if h != t:
            disagree.append((s, sorted(h, key=RANK.get), sorted(t, key=RANK.get), sorted(l, key=RANK.get)))
    # C-25: earliest binding (union of sources) vs earliest binding of each hard prerequisite
    union = {s: header.get(s, set()) | table.get(s, set()) | ladder.get(s, set()) for s in header}
    viol = []
    for s, pre in sorted(hard.items()):
        e = earliest(union.get(s, set()))
        if e is None:
            continue
        reasons = []
        for m in sorted(pre["mod"], key=lambda x: RANK.get(x, 99)):
            if m in RANK and RANK[m] > RANK[e]:
                reasons.append(m)
        for p in sorted(pre["sd"]):
            pe = earliest(union.get(p, set()))
            if pe and RANK[pe] > RANK[e]:
                reasons.append(f"{p}@{pe}")
        if reasons:
            viol.append((s, e, reasons))
    res = {"sd_modules": len(sds), "header_vs_table_disagree": len(disagree), "disagreements": disagree,
           "prereq_violations": len(viol), "violations": viol}
    print(f"SD modules parsed: {len(sds)} · header≠§2 table: {len(disagree)} · earliest-binding-before-hard-prereq: {len(viol)}")
    for d in disagree:
        print("  DIS", d[0], "header", d[1], "§2", d[2], "§4.5", d[3])
    for v in viol:
        print("  VIOL", v[0], "earliest", v[1], "needs", v[2])
    if "--json" in sys.argv:
        json.dump(res, open(sys.argv[sys.argv.index("--json") + 1], "w"), indent=1, default=sorted)


if __name__ == "__main__":
    main()
