#!/usr/bin/env python3
"""R4 (C-49, rule 0.4.8): bound-concept count per main-course module, from the six parts as they stand.

Usage:  budget.py ROOT [--json OUT.json]

A companion concept card (a heading-defined ID, or a design-patterns bold card label, that is not an exercise, drill, prediction card, key or problem) is *bound* to main-course
module X when
  - its own stitch header names X, outside a segment marked recall or named-only (a recall or a pointer is one line, not teaching load), or
  - a row of its file's §2 stitch table (a table whose first column is the main-course module or anchor; the
    calendar and overlap tables only restate it) names X in the first cell and the card's ID (or a range that holds it) in
    another cell, outside a segment the cell marks as recall or as taught in another module's session, and that cell
    is not a recall-only column (the primer's `Recall` column; the cyber file's
    secondary column still counts, because secondary items are taught in the same session).
The module's own topic lines in the main course count one each. Rule 0.4.8 budgets 3–5 concepts per session and
splits any module over 20 into teaching blocks (C-49). The count is a planning estimate, not a gate on depth.
"""
import json
import os
import re
import sys

COMP = ["system-design-primer-companion.md", "sql-databases-companion.md", "design-patterns-companion.md",
        "cloud-cybersecurity-companion.md", "go-language-companion.md"]
EXER = re.compile(r"^(?:TD|PX|TX|BH|SCH|DT)-|^(?:SQL|SEC)-(?:E|Z0|CAP|SKIP)|^GO-(?:E|P|CAP)|^CR-E|^[EZ]\d|^[POQ]\d{2}$|^C\d\.|^SDP-|^SQL-")
CARD = re.compile(r"^#{3,4} ([A-Z]{1,4}(?:-[A-Z])?-\d{1,2}[a-z]?)\b")
LABEL = re.compile(r"^(?:- )?\*\*([A-Z]{1,4}-\d{1,2})(?: ·| [A-Z][^*]*:\*\*)")   # design-patterns cards: bold labels
MOD = re.compile(r"(?<![\w-])([A-D]\d{1,2})(?![\w-])")
SKIP = re.compile(r"(?i)\brecall|named only|named, not taught")   # a recall or a pointer is one line, not load
RANGE = re.compile(r"(?<![\w-])([A-Z]{1,4}-)(\d+)\s*(?:…|–|\.\.\.)\s*([A-Z]{1,4}-)?(\d+)(?![\w-]|\.\d)")


def expand(cell):
    out = set()
    for p, a, p2, b in RANGE.findall(cell):
        if p2 and p2 != p:
            continue
        w = len(a) if a.startswith("0") else 0
        out |= {f"{p}{i:0{w}d}" if w else f"{p}{i}" for i in range(int(a), int(b) + 1)}
    return out


def count(root):
    cur = open(os.path.join(root, "work", "Curriculum.md"), encoding="utf-8").read().split("\n")
    own, mod = {}, None
    for l in cur:
        m = re.match(r"^### ([A-D]\d{1,2})\. ", l)
        if m:
            mod = m.group(1)
            own[mod] = 0
            continue
        if l.startswith("#"):
            mod = None
        elif mod and l.strip() and not l.startswith(("- [ ]", ">", "|")):
            own[mod] += 1
    bound = {m: {} for m in own}
    for f in COMP:
        L = open(os.path.join(root, "work", f), encoding="utf-8").read().split("\n")
        cards = set()
        for l in L:
            lb = LABEL.match(l)
            if lb and not EXER.search(lb.group(1)):
                cards.add(lb.group(1))
            m = CARD.match(l)
            if m and not EXER.search(m.group(1)):
                cards.add(m.group(1))
                if "— stitch:" in l:
                    st = re.split(r"\brecall:", l.split("— stitch:")[1])[0]
                    st = " · ".join(g for g in st.split(" · ") if not SKIP.search(g))
                    for x in MOD.findall(st):
                        if x in bound:
                            bound[x].setdefault(m.group(1), f)
        t = "\n".join(L)
        s2 = re.search(r"^## 2\. .*?(?=^## 3\.|\Z)", t, re.M | re.S)
        if not s2:
            continue
        head = None
        for l in s2.group(0).split("\n"):
            if not l.startswith("|"):
                head = None
                continue
            cells = [c.strip() for c in l.strip().strip("|").split("|")]
            if head is None:
                head = cells
                continue
            if set(l) <= set("|-: ") or not re.search(r"(?i)module|anchor", head[0]):
                continue   # only the stitch tables bind; the calendar and overlap tables restate them
            mods = [x for x in MOD.findall(cells[0]) if x in bound]
            for i, c in enumerate(cells[1:], 1):
                if i < len(head) and re.search(r"(?i)recall", head[i]):
                    continue
                # a segment the cell itself marks as recall, or as taught in another module's session, adds no load
                segs = [g for g in re.split(r" · |; |\. ", c) if not SKIP.search(g)
                        and not any(o not in mods for o in re.findall(r"taught in the ([A-D]\d{1,2}) session", g))]
                c = " · ".join(segs)
                ids = (set(re.findall(r"(?<![\w-])([A-Z]{1,4}(?:-[A-Z])?-\d{1,2}[a-z]?)(?![\w-])", c)) | expand(c)) & cards
                for x in mods:
                    for i_ in ids:
                        bound[x].setdefault(i_, f)
    return own, bound


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    root = os.path.abspath(args[0] if args else ".")
    own, bound = count(root)
    rows = []
    for m in own:
        n = own[m] + len(bound[m])
        rows.append({"module": m, "own_lines": own[m], "bound_cards": len(bound[m]), "total": n,
                     "sessions_3_to_5": [-(-n // 5), -(-n // 3)], "over_20": n > 20,
                     "cards": sorted(bound[m])})
    for r in rows:
        print(f"{r['module']:4} own {r['own_lines']:3} + bound {r['bound_cards']:3} = {r['total']:3} "
              f"sessions {r['sessions_3_to_5'][0]}–{r['sessions_3_to_5'][1]}" + ("  OVER 20" if r["over_20"] else ""))
    if "--json" in sys.argv:
        out = sys.argv[sys.argv.index("--json") + 1]
        json.dump(rows, open(out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
