#!/usr/bin/env python3
"""Post-conditions for the R2 renames. Usage: rename_checks.py DIR   (DIR = a renamed copy of work/, or work/ after --apply)
Exit 1 if any check fails. Idempotent, read-only."""
import os, re, sys
W = sys.argv[1]
rd = lambda f: open(os.path.join(W, f), encoding="utf-8").read().split("\n")
S, C, D, P, K = (rd(f) for f in ("sql-databases-companion.md", "cloud-cybersecurity-companion.md",
                                  "design-patterns-companion.md", "system-design-primer-companion.md", "Curriculum.md"))
prim = "\n".join(P)
prim_def = set(re.findall(r"^#### (SD-\d{2}[a-c]?)", prim, re.M)) | set(re.findall(r"\*\*(SD-\d{2}[a-c]?)", prim))
fails = 0


def scan(name, L, pat, allow=lambda n, m: False):
    global fails
    bad = [(i + 1, m.group(0)) for i, l in enumerate(L) for m in re.finditer(pat, l) if not allow(i + 1, m)]
    fails += bool(bad)
    print(f"{'PASS' if not bad else 'FAIL'} {name}: {len(bad)} {bad[:8]}")


scan("SQL: every remaining SD- is two-digit (primer)", S, r"(?<![\w-])SD-\d+[a-c]?",
     lambda n, m: re.fullmatch(r"SD-\d{2}[a-c]?", m.group(0)) is not None)
sd = {m for l in S for m in re.findall(r"(?<![\w-])SD-\d{2}[a-c]?", l)}
ok = sd <= prim_def
fails += not ok
print(f"{'PASS' if ok else 'FAIL'} SQL: remaining SD refs {sorted(sd)} all defined in primer")
scan("cyber: no DD-/DT-/PR- numbered or wildcard", C, r"(?<![\w-])(DD|DT|PR)-(\d|\*)")
scan("cyber: no bare DD/DT family codes", C, r"(?<![\w-])(DD|DT)(?![\w-])")
for nm, L in (("SQL", S), ("cyber", C)):
    scan(f"{nm}: no unqualified E<l>.<n>", L, r"(?<![\w.-])E\d+\.\d+")
    scan(f"{nm}: no unqualified Z0", L, r"(?<![\w.-])Z0(?![\w])")
scan("SQL: no bare C1–C4", S, r"(?<![\w-])C[1-4](?![\w-])")
scan("cyber: bare C1–C4 only on Curriculum Track-C lines 52/101/102/120", C, r"(?<![\w-])C[1-4](?![\w-])",
     lambda n, m: n in (52, 101, 102, 120))
scan("SQL: no 12.S12/12.S13/S12/S13", S, r"12\.S1[23]|(?<![\w.-])S1[23](?![\w])")
scan("SQL: no P1–P11", S, r"(?<![\w-])P\d{1,2}(?![\w])")
scan("SQL: no E11/E12", S, r"(?<![\w.-])E1[12](?![\w])")
scan("SQL: no bare HS/UG/grad", S, r"(?<![\w-])(HS|UG|[Gg]rad)(?![\w-])")
scan("DP: no [C]/[S]/[B]", D, r"\[[CSB]\]")
scan("primer §4.2–§4.3 (625–680): no bare tiers", P[624:680], r"(?<![\w.-])T[0-5](?![\w.])")
scan("cyber: no bare tiers", C, r"(?<![\w.-])T\d(?![\w.\d])")
for nm, L in (("SQL", S), ("cyber", C), ("DP", D), ("primer", P), ("Curriculum", K)):
    scan(f"{nm}: C-10 corruption signature", L, r"(?<![\w-])(?:[EZ]\d*[AB]5 (?:IAM|TLS)|[EZ][A-Z]\d)(?<!EC2)")
scan("all: S-modules never hyphenated (S-n)", S + C + D + P + K, r"(?<![\w-])S-\d")
sys.exit(1 if fails else 0)
