#!/usr/bin/env python3
"""R2b/R2c audit: are the six course files self-contained, loss-free and reproducible (learner decisions D2–D11)?

Runs the self-containment probe, the D3 loss check (both stages), the frozen-snapshot check, an idempotency rebuild,
the invariants that R2b could break, and one probe per learner decision. Writes ROOT/audit-R2b.md; exits 1 on a FAIL.

Usage: audit_r2b.py ROOT
Deterministic: no timestamps; every list is in a fixed order.
"""
import hashlib
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
W = os.path.join(ROOT, "work")
IN = os.path.join(ROOT, "inputs-original")
COURSE = {"cur": "Curriculum.md", "pri": "system-design-primer-companion.md", "sql": "sql-databases-companion.md",
          "dp": "design-patterns-companion.md", "sec": "cloud-cybersecurity-companion.md",
          "go": "go-language-companion.md"}
ORIG = [k for k in COURSE if k != "go"]   # the Go companion (D12) is new in R2c: it has no input to compare with


def text(k, base=W):
    return open(os.path.join(base, COURSE[k]), encoding="utf-8").read()


def ok(cond, ev):
    return ("PASS" if cond else "FAIL"), ev


def run(*args):
    p = subprocess.run([sys.executable, *args], cwd=ROOT, capture_output=True, text=True)
    return p.returncode, [l for l in (p.stdout + p.stderr).strip().split("\n") if l]


def tree_hash():
    h = hashlib.sha256()
    for d in ("work", "records"):
        for fn in sorted(os.listdir(os.path.join(ROOT, d))):
            h.update(fn.encode() + open(os.path.join(ROOT, d, fn), "rb").read())
    h.update(open(os.path.join(ROOT, "outputs", "r2b", "journal.jsonl"), "rb").read())
    return h.hexdigest()


def heading(k, mid):
    return len(re.findall(rf"^#{{3,4}} {re.escape(mid)} ", text(k), re.M))


def checks():
    out = []
    rc, o = run("refactor-tools/selfcontained.py", ".")
    out.append(("D6 self-contained (V1–V6)", *ok(rc == 0, "; ".join(l for l in o if l.startswith(("PASS", "FAIL"))))))
    rc, o = run("refactor-tools/d3_check.py", ".", "--stage", "all")
    out.append(("D3 no content loss (R2 and R2b)", *ok(rc == 0, f"{sum(l.startswith('PASS') for l in o)} PASS, "
                                                                f"{sum(l.startswith('FAIL') for l in o)} FAIL")))
    before = tree_hash()
    rc, o = run("refactor-tools/r2b_build.py", ".")
    after = tree_hash()
    out.append(("Reproducible from the frozen R2 snapshot", *ok(rc == 0 and before == after,
                "rebuild " + ("left work/, records/ and the journal byte-identical" if before == after else "CHANGED output")
                + (f"; {o[-1][:60]}" if o else ""))))

    ins = text("sql", IN)
    g = lambda t: sorted(re.findall(r"\b\d+:[0-9a-f]{8}\b", t))
    blk = lambda t: re.findall(r"```sql\n.*?```", t, re.S)
    # the kit's goldens JSON (printed in full in §3.8) repeats every fingerprint once more, so compare the sets
    out.append(("Invariant 6: goldens immutable", *ok(set(g(ins)) == set(g(text("sql"))) and set(blk(ins)) <= set(blk(text("sql"))),
                f"{len(set(g(ins)))} distinct fingerprints, same set before and after (the §3.8 goldens JSON repeats "
                f"them); {len(blk(ins))} input SQL blocks all present")))
    vf = {k: (text(k, IN).count("(verify"), text(k).count("(verify")) for k in ORIG}
    out.append(("Invariant 7: `(verify)` flags kept", *ok(all(b >= a for a, b in vf.values()), f"before→after {vf}")))
    cc = [l for l in text("pri", IN).split("\n") if "CC BY" in l]
    out.append(("Invariant 11: CC BY line + change notice", *ok(all(l in text("pri") for l in cc) and
                "Modified on 2026-09-24, when this companion was fitted into the five-part course." in text("pri"),
                f"{len(cc)} CC BY lines unchanged; the change notice is in words")))
    out.append(("Invariant 12: primer numbers", *ok(all(f"**{p}**" in text("pri") for p in
                [f"P0{i}" for i in range(1, 9)] + [f"O0{i}" for i in range(1, 8)]), "P01–P08, O01–O07 present")))

    ticked = {k: len(re.findall(r"^\s*- \[[xX]\] ", text(k), re.M)) for k in COURSE}
    out.append(("D2 fresh start", *ok(not any(ticked.values()), f"ticked boxes {ticked}")))
    ns = {k: len(re.findall(r"Northstar|northstar", text(k))) for k in COURSE}
    out.append(("D5 Northstar deleted", *ok(not os.path.exists(os.path.join(W, "northstar-reference-app.md"))
                                           and not any(ns.values()), f"file absent; mentions {ns}")))
    homes = [("pri", "SD-22"), ("pri", "SD-23"), ("pri", "SD-25"), ("sql", "OD-03"), ("sql", "OD-08"),
             ("sql", "OD-09"), ("sql", "OD-11"), ("sql", "DD-03"), ("sql", "DD-05"), ("sql", "DD-09"),
             ("sql", "DD-13"), ("sql", "CS-02"), ("sql", "AN-02"), ("sec", "PV-03"), ("sec", "CR-14")]
    bad = [f"{k}:{m}" for k, m in homes if heading(k, m) != 1 or any(heading(o, m) for o in COURSE if o != k)]
    out.append(("D7 one home per topic", *ok(not bad, f"{len(homes)} home modules, each one heading in its own file "
                                                      f"only" + (f"; wrong: {bad}" if bad else ""))))
    # D14 (2026-09-24) replaces D8: the learner keeps gcp-curriculum.md. What must hold instead is that no build step
    # reads it. A full rebuild runs under an audit hook that records every file the process opens.
    probe = ("import sys, os\n"
             "seen = []\n"
             "sys.addaudithook(lambda ev, a: seen.append(str(a[0])) if ev == 'open' and a and isinstance(a[0], (str, "
             "bytes, os.PathLike)) else None)\n"
             f"sys.argv = ['r2b_build.py', {ROOT!r}]\n"
             f"sys.path.insert(0, {os.path.join(ROOT, 'refactor-tools')!r})\n"
             "import r2b_build\n"
             "r2b_build.main()\n"
             "print('OPENED', len(seen))\n"
             "print('LEGACY', sum(1 for s in seen if 'gcp-curriculum.md' in s))\n")
    res = subprocess.run([sys.executable, "-c", probe], capture_output=True, text=True, cwd=ROOT)
    got = dict(l.split() for l in res.stdout.splitlines() if l.startswith(("OPENED", "LEGACY")))
    legacy = os.path.join(ROOT, "..", "gcp-curriculum.md")
    out.append(("D14 legacy file kept; no build reads it", *ok(
        res.returncode == 0 and got.get("LEGACY") == "0" and int(got.get("OPENED", 0)) > 0,
        f"gcp-curriculum.md {'present' if os.path.exists(legacy) else 'absent'} (kept by D14, which replaces D8); "
        f"full rebuild under an open() audit hook: {got.get('OPENED', '?')} opens, {got.get('LEGACY', '?')} of the "
        f"legacy file; build exit {res.returncode}")))
    sec, sql, pri = text("sec"), text("sql"), text("pri")
    cards = ["SEC-Z0.5", "SEC-E3.1", "SEC-E3.5", "SEC-E4.3", "SEC-E4.16", "SEC-E4.21", "SEC-E6.5", "SEC-E6.8", "SEC-E10.7"]
    miss = [c for c in cards if not re.search(rf"^- \*\*{re.escape(c)}:\*\*", sec, re.M)]
    fills = {"nine checkpoint keys": not miss, "TF-DB plan acceptance": "**What each plan must show**" in sql,
             "SQL-CAP3 acceptance": "**SQL-CAP3 acceptance**" in sql, "SQL lab kit": "Every file of the kit, in full" in sql,
             "SD-25 Filestore row": "| Filestore |" in pri, "reference app defined": "`shop.example`" in sec}
    out.append(("D9 gaps filled", *ok(all(fills.values()), "; ".join(f"{k} {'yes' if v else 'NO'}" for k, v in fills.items())
                                      + (f"; keys missing {miss}" if miss else ""))))
    bt = {k: text(k).count("`Curriculum`") for k in COURSE}
    out.append(("D11 parent named 'the main course'", *ok(not any(bt.values()), f"backticked `Curriculum` {bt}")))
    out.append(("D12 Go companion tied in", *d12()))
    return out


def d12():
    """the sixth part exists, rule 0.4.9 is in every part, and every GO reference and stitch tag resolves"""
    cur, go, bad = text("cur"), text("go"), []
    rule = [l for l in cur.split("\n") if l.startswith("**0.4.9 Implementation language: Go.**")]
    if len(rule) != 1:
        bad.append("main course has no single rule 0.4.9")
    bad += [f"{k} lacks rule 0.4.9" for k in COURSE if k != "cur" and rule and rule[0] not in text(k).split("\n")]
    bad += [f"{k} contract intro not 0.4.10" for k in COURSE if k != "cur" and "(0.4.1…0.4.10, and" not in text(k)]
    if "one course in six parts" not in cur or "- **The Go Language Companion" not in cur:
        bad.append("main §0.1 does not list six parts")
    mods = re.findall(r"^#### (GO-\d\d) ", go, re.M)
    total = re.search(r"^\| \*\*Total\*\* \| \| \*\*(\d+)\*\* \|$", go, re.M)
    n = int(total.group(1)) if total else 0
    if not n or mods != [f"GO-{i:02d}" for i in range(1, n + 1)]:
        bad.append(f"GO-01…GO-{n:02d} headings not in order or the ledger total disagrees ({len(mods)} headings)")
    # D13: one involved problem per module (on its card, after the Check) and one rubric per problem
    cards = re.split(r"^(?=#### GO-\d\d )", go, flags=re.M)[1:]
    for c in cards:
        m = c[5:10]
        body = c.split("\n\n")[0]
        if not re.search(rf"^- \*\*Check:\*\* .*\n- \*\*Involved problem {m.replace('GO-', 'GO-P')}:\*\* ", body, re.M):
            bad.append(f"{m} has no involved problem right after its Check")
    probs = re.findall(r"^- \*\*Involved problem (GO-P\d\d):\*\*", go, re.M)
    rubs = re.findall(r"^- \*\*(GO-P\d\d) rubric:\*\*", go, re.M)
    if probs != [f"GO-P{i:02d}" for i in range(1, n + 1)] or rubs != probs:
        bad.append(f"involved problems/rubrics not one per module ({len(probs)} problems, {len(rubs)} rubrics)")
    if "4. **Involved problem** — every GO module ends with one involved problem" not in cur:
        bad.append("rule 0.4.9 lacks its fourth rule (involved problem)")
    bad += [f"{k} has a GO heading" for k in COURSE if k != "go" and re.search(r"^#{3,4} GO-", text(k), re.M)]
    refs = {r for k in COURSE for r in re.findall(r"\bGO-(?:\d\d|E\d+\.\d+|CAP\d|P\d\d)\b", text(k))}
    ex = set(re.findall(r"^- \[ \] \*\*(GO-E\d+\.\d+)\*\*", go, re.M))
    keys = set(re.findall(r"^- \*\*(GO-E\d+\.\d+):\*\*", go, re.M))
    caps = set(re.findall(r"^- \[ \] \*\*(GO-CAP\d) ·", go, re.M))
    bad += [f"exercise {e} has no key" for e in sorted(ex - keys)] + [f"key {e} has no exercise" for e in sorted(keys - ex)]
    bad += [f"dangling {r}" for r in sorted(refs) if r not in set(mods) | ex | caps | set(probs)]
    tags = {t.strip() for h in re.findall(r"^#### GO-\d\d .*? — stitch: (.*)$", go, re.M) for t in h.split(" · ")}
    bad += [f"stitch tag {t} not a main-course module" for t in sorted(tags)
            if not re.search(rf"^(?:#{{2,4}} {re.escape(t)}[.: ]|\| {re.escape(t)} \|)", cur, re.M)]   # heading or reserved row
    ties = {"pri": "once its GO-11 is (rule 0.4.9)", "sql": "once the Go Language Companion's GO-22 is taught",
            "dp": "| Go Language Companion | GO-11 renders", "sec": "the Go Language Companion's GO-21 teaches"}
    bad += [f"{k} tie-in missing" for k, v in ties.items() if v not in text(k)]
    return ok(not bad, f"{len(mods)} modules, {len(probs)} involved problems with rubrics, {len(ex)} exercises with "
                       f"keys, {len(caps)} capstones, {len(refs)} "
                       f"GO IDs referenced, {len(tags)} stitch tags, rule 0.4.9 in {len(COURSE)} parts"
              + (f"; wrong: {bad[:8]}" if bad else ""))


def main():
    rows = checks()
    fails = sum(1 for _, s, _ in rows if s == "FAIL")
    esc = lambda s: str(s).replace("|", "\\|").replace("\n", " ")
    md = ["# R2b audit", "",
          "Generated by `refactor-tools/audit_r2b.py` (re-run: `python3 refactor-tools/audit_r2b.py .`). It checks the "
          "six course files in `work/` after R2b.", "",
          f"**Result: {'PASS' if not fails else f'{fails} FAIL'}**", "",
          "| Check | Status | Evidence |", "|---|---|---|"]
    md += [f"| {a} | {s} | {esc(e)} |" for a, s, e in rows]
    open(os.path.join(ROOT, "audit-R2b.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
    for a, s, e in rows:
        print(s, a, "—", e[:150])
    print(f"audit_r2b: {'PASS' if not fails else str(fails) + ' FAIL'}")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
