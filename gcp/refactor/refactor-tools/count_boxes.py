#!/usr/bin/env python3
"""Count real checkboxes in markdown files: '[ ]'/'[x]' outside inline code spans. Usage: count_boxes.py FILE..."""
import re, sys
for f in sys.argv[1:]:
    L = open(f, encoding="utf-8").read().split("\n")
    real, men = [], 0
    for i, l in enumerate(L):
        s = re.sub(r"`[^`]*`", "", l)
        real += [(i + 1, m.group(1)) for m in re.finditer(r"\[( |x|X)\]", s)]
        men += len(re.findall(r"\[( |x|X)\]", l)) - len(re.findall(r"\[( |x|X)\]", s))
    lines = sorted({n for n, _ in real})
    multi = sorted({n for n, _ in real if sum(1 for m, _ in real if m == n) > 1})
    print(f"{f}: boxes {len(real)} on {len(lines)} lines; ticked {sum(1 for _, c in real if c != ' ')}; code-span mentions {men}; multi-box lines {multi}")
