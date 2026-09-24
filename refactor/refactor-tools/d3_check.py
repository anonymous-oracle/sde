#!/usr/bin/env python3
"""D3 no-removal check (learner decision D3; invariant 1). R3 folds this into verify.py.

For every file, every non-blank line of the renamed, pre-repair snapshot (outputs/r2/renamed/) must survive in work/:
  - verbatim as a substring of some work/ line (unchanged, moved, prefixed with a heading marker, or archived in the
    file's "Pre-refactor text archive (D3)"), or
  - as the `before` of a journaled anchor-rewrite / rename / unarchived regenerate, where the logged `after` is
    itself present in work/ (anchor metadata keeps its original in the journal, the diff and crosswalk.md).
Lines changed by rename.py are compared after the rename (§8.2: "after the ID rename").

Usage: d3_check.py ROOT   → prints per-file counts, exits 1 on any lost line.
"""
import json
import os
import sys

FILES = ["Curriculum.md", "system-design-primer-companion.md", "sql-databases-companion.md",
         "design-patterns-companion.md", "cloud-cybersecurity-companion.md", "session-progress-ledger.md",
         "learn-SKILL.md"]


def main():
    root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
    J = [json.loads(l) for l in open(os.path.join(root, "outputs", "r2", "journal.jsonl"), encoding="utf-8")]
    lost_all = 0
    for f in FILES:
        before = open(os.path.join(root, "outputs", "r2", "renamed", f), encoding="utf-8").read().split("\n")
        work = open(os.path.join(root, "work", f), encoding="utf-8").read()
        wl = set(work.split("\n"))
        # chain journal rewrites: an original line may be rewritten several times before its final form
        succ = {}
        for j in J:
            if j["file"] == f and len(j["before"]) == len(j["after"]) and j["before"]:
                for b, a in zip(j["before"], j["after"]):
                    succ.setdefault(b, []).append(a)

        def survives(line, depth=0):
            if line.strip() in work:
                return "verbatim"
            if depth > 8:
                return None
            for a in succ.get(line, []):
                if a in wl or survives(a, depth + 1):
                    return "journaled"
            return None
        c = {"verbatim": 0, "journaled": 0}
        lost = []
        for n, l in enumerate(before, 1):
            if not l.strip():
                continue
            s = survives(l)
            if s:
                c[s] += 1
            else:
                lost.append((n, l[:120]))
        lost_all += len(lost)
        print(f"{'PASS' if not lost else 'FAIL'} {f}: {c['verbatim']} verbatim, {c['journaled']} via journal, "
              f"{len(lost)} lost")
        for n, l in lost[:20]:
            print(f"    L{n}: {l}")
    sys.exit(1 if lost_all else 0)


if __name__ == "__main__":
    main()
