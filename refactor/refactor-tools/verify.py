#!/usr/bin/env python3
"""R3 / R10 verification (meta prompt §8.2 diff, §12.7 lints, R3 hard gate), folded over every earlier check.

It runs, in order:
  1. inputs      the read-only inputs match the SHA-256 table in refactor-state.md §1; the frozen R2 snapshot and the
                 frozen R2c Go source match their recorded hashes.
  2. rebuild     audit_r2b.py (rebuilds work/ from the frozen snapshot, byte-identical; D-decision and invariant rows).
  3. folded      selfcontained.py (D6), d3_check.py --stage all (D3), rename_checks.py on the renamed snapshot,
                 binding.py on the current primer (C-24/C-25 topological check).
  4. manifest    manifest.py over work/ → manifest-after.json (+ manifest-after-summary.md).
  5. §8.2        every R1 manifest item survives (through the rename map and both journals, or kept in records/);
                 defined-count(ID) == 1; every referenced ID is defined; no orphan companion module; no foreign parent
                 names or pseudo-anchors; no mangled IDs; goldens; D2 ledger items; the primer checks (verbatim tables,
                 CC BY, mermaid edge superset, binding topology, generated sections unchanged, C-31, labels).
  6. Go D3       every line of the R2c Go source survives in the current source or in records/; the source is in work/.
  7. conflicts   every audit_r2.py probe for C-01…C-75 / C-NEW-nn, re-run on work/; a probe that looked for text R2b
                 removed on purpose (conflict tags, file names, Northstar) is replaced by a probe of the substance, and
                 every R2 journal edit of that conflict is traced to live text through the R2b journal.
  8. lints       §12.7: tables not ragged; every "§x" resolves; repeated numeric facts agree; ID titles (heuristic,
                 informational); the parent named as a file-style name.
  9. holds       items that are not §8.2 gate items but are open with the learner (D8).

Hard gate (R3): zero lost items, zero undefined references, zero orphans, zero file names or links; every other GATE
row must pass. Rows marked INFO or HOLD are reported, never counted as passes.

Usage: verify.py ROOT [--stage R3|R10] [--no-rebuild]
  → writes ROOT/manifest-after.json, ROOT/manifest-after-summary.md, ROOT/verification-report-<stage>.md; exit 1 on
    any GATE failure. Deterministic: no timestamps; every list is sorted or in a fixed order.
"""
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(next((a for a in sys.argv[1:] if not a.startswith("--") and a not in ("R3", "R10")), "."))
STAGE = sys.argv[sys.argv.index("--stage") + 1] if "--stage" in sys.argv else "R3"
TOOLS = os.path.join(ROOT, "refactor-tools")
sys.path.insert(0, TOOLS)

COURSE = ["Curriculum.md", "system-design-primer-companion.md", "sql-databases-companion.md",
          "design-patterns-companion.md", "cloud-cybersecurity-companion.md", "go-language-companion.md"]
ORIG5 = COURSE[:5]                                   # the five course files that have an input in inputs-original/
OTHER = ["session-progress-ledger.md", "learn-SKILL.md"]
SHORT = dict(zip(COURSE + OTHER, ["cur", "pri", "sql", "dp", "sec", "go", "led", "skl"]))
GO_R2C = os.path.join("outputs", "r2c", "go-language-companion.r2c.md")

ROWS = []   # (section, check, kind, status, evidence); kind GATE | INFO | HOLD


def row(section, check, status, evidence, kind="GATE"):
    ROWS.append((section, check, kind, status, str(evidence)))


def rd(*p):
    return open(os.path.join(ROOT, *p), encoding="utf-8").read()


def run(cmd):
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    return p.returncode, (p.stdout + p.stderr).strip().split("\n")


def sha(path):
    return hashlib.sha256(open(os.path.join(ROOT, path), "rb").read()).hexdigest()


def code_mask(lines):
    on, out = False, []
    for l in lines:
        if l.lstrip().startswith("```") or l.lstrip().startswith("~~~"):
            out.append(True)
            on = not on
        else:
            out.append(on)
    return out


# ---------------------------------------------------------------- 1. inputs
def inputs():
    st = rd("refactor-state.md")
    want = dict(re.findall(r"^\| `?([\w.-]+?)`?(?: \(reference only, never edited\))? \| .*? \| \d+ \| `([0-9a-f]{64})` \|$",
                           st, re.M))
    want = {("Curriculum.md" if k == "Curriculum" else k): v for k, v in want.items()}
    got = {f: sha(os.path.join("inputs-original", f)) for f in sorted(os.listdir(os.path.join(ROOT, "inputs-original")))}
    bad = sorted(f for f in got if want.get(f) != got[f])
    row("1 inputs", "inputs-original/ matches refactor-state.md §1 hashes", "PASS" if not bad and len(want) == 7 else "FAIL",
        f"{len(got)} files, {len(want)} recorded hashes; mismatched: {bad}")
    rec = dict(l.split()[::-1] for l in rd("outputs", "r2b", "in.sha256").split("\n") if l.strip())
    badr = sorted(p for p, h in rec.items() if sha(p if os.path.isabs(p) else os.path.join("outputs", "r2b", "in",
                                                                                            os.path.basename(p))) != h)
    row("1 inputs", "frozen R2 snapshot outputs/r2b/in/ matches in.sha256", "PASS" if not badr else "FAIL",
        f"{len(rec)} files; mismatched {badr}")
    h, p = rd(GO_R2C + ".sha256").split()
    row("1 inputs", "frozen R2c Go source matches its hash", "PASS" if sha(GO_R2C) == h else "FAIL", f"{GO_R2C}")
    ro = all(not os.stat(os.path.join(ROOT, "inputs-original", f)).st_mode & 0o222 for f in got)
    row("1 inputs", "inputs-original/ is read-only (invariant 14)", "PASS" if ro else "FAIL",
        "mode a-w on every file" if ro else "a fresh checkout resets modes: run `chmod a-w inputs-original/*`")


# ---------------------------------------------------------------- 2. rebuild + audit_r2b
def rebuild():
    rc, out = run([sys.executable, os.path.join(TOOLS, "audit_r2b.py"), "."])
    for l in out:
        m = re.match(r"^(PASS|FAIL) (.+?) — (.*)$", l)
        if not m:
            continue
        st, name, ev = m.groups()
        if name.startswith("D8 "):
            row("9 holds", "D8 legacy file deleted (audit_r2b)", "HOLD" if st == "FAIL" else "PASS",
                ev + " — kept on purpose until the learner answers refactor-state.md §10 question 2", "HOLD")
        else:
            row("2 rebuild + decisions", name, st, ev[:300])


# ---------------------------------------------------------------- 3. folded tools
def folded():
    rc, out = run([sys.executable, os.path.join(TOOLS, "selfcontained.py"), "."])
    ps = [l for l in out if l.startswith(("PASS", "FAIL"))]
    row("3 folded", "D6 self-contained: no file names, links, Northstar, file-style parent, bookkeeping, legacy "
        "pointers (selfcontained.py)", "PASS" if rc == 0 else "FAIL", f"{sum(l.startswith('PASS') for l in ps)}/"
        f"{len(ps)} files PASS")
    rc, out = run([sys.executable, os.path.join(TOOLS, "d3_check.py"), ".", "--stage", "all"])
    ps = [l for l in out if l.startswith(("PASS", "FAIL"))]
    row("3 folded", "D3 no lost line: renamed input → R2 → R2b (d3_check.py --stage all)", "PASS" if rc == 0 else "FAIL",
        f"{sum(l.startswith('PASS') for l in ps)}/{len(ps)} stage-file rows PASS")
    rc, out = run([sys.executable, os.path.join(TOOLS, "rename_checks.py"), "outputs/r2/renamed"])
    ps = [l for l in out if l.startswith(("PASS", "FAIL"))]
    row("3 folded", "rename post-conditions on the renamed snapshot (rename_checks.py)", "PASS" if rc == 0 else "FAIL",
        f"{sum(l.startswith('PASS') for l in ps)}/{len(ps)} PASS")
    rc, out = run([sys.executable, os.path.join(TOOLS, "binding.py"), "work/system-design-primer-companion.md"])
    row("3 folded", "C-24/C-25 primer binding table: one PRIMARY each, no PRIMARY before a hard prerequisite "
        "(binding.py on the current primer)", "PASS" if rc == 0 else "FAIL", out[0] if out else "")


# ---------------------------------------------------------------- 4. manifest
def manifest():
    rc, out = run([sys.executable, os.path.join(TOOLS, "manifest.py"), "work", "--out", "manifest-after.json",
                   "--summary", "manifest-after-summary.md"])
    row("4 manifest", "manifest-after.json written from work/", "PASS" if rc == 0 else "FAIL", out[-1][:300] if out else "")
    return json.load(open(os.path.join(ROOT, "manifest-after.json"))), json.load(open(os.path.join(ROOT, "manifest-before.json")))


# ---------------------------------------------------------------- 5. §8.2
def chain():
    """the R2 journal (renamed line → R2-output line), for tracing R1 items"""
    J = [json.loads(l) for l in open(os.path.join(ROOT, "outputs", "r2", "journal.jsonl"), encoding="utf-8")]
    succ = {}
    for j in J:
        if len(j["before"]) == len(j["after"]) and j["before"]:
            for b, a in zip(j["before"], j["after"]):
                succ.setdefault((j["file"], b), []).append(a)
    return succ


def item_survival(before):
    """§8.2 first bullet: every R1 item has an after-item, through the rename map (outputs/r2/renamed keeps line
    numbers), the R2 journal, and R2b (work/ or records/)."""
    succ = chain()
    per, lost_all = {}, []
    for f in ORIG5 + OTHER:
        renamed = open(os.path.join(ROOT, "outputs", "r2", "renamed", f), encoding="utf-8").read().split("\n")
        r2out_p = os.path.join(ROOT, "outputs", "r2b", "in", f)
        r2out = open(r2out_p if os.path.exists(r2out_p) else os.path.join(ROOT, "work", f), encoding="utf-8").read()
        work = rd("work", f)
        recp = os.path.join(ROOT, "records", f)
        rec = open(recp, encoding="utf-8").read() if os.path.exists(recp) else ""

        def r2_final(line, depth=0):
            if line.strip() in r2out:
                return line.strip()
            if depth > 8:
                return None
            for a in succ.get((f, line), []):
                x = r2_final(a, depth + 1)
                if x is not None:
                    return x
            return None
        counts = {}
        items = before["files"][f]["items"]
        cats = [(k, v) for k, v in items.items() if isinstance(v, list) and k not in ("ids",)]
        if "primer" in items:
            cats += [("primer." + k, v) for k, v in items["primer"].items() if isinstance(v, list) and v and
                     isinstance(v[0], dict) and "line" in v[0]]
        for cat, lst in cats:
            c = {"work": 0, "records": 0, "lost": 0}
            for it in lst:
                if "line" not in it:
                    continue
                src = renamed[it["line"] - 1]
                fin = r2_final(src)
                if fin is None:
                    c["lost"] += 1
                    lost_all.append((f, cat, it["line"], src[:100]))
                elif fin in work:
                    c["work"] += 1
                elif fin in rec:
                    c["records"] += 1
                else:
                    c["lost"] += 1
                    lost_all.append((f, cat, it["line"], src[:100]))
            counts[cat] = c
        per[f] = counts
    return per, lost_all


REG_ID = re.compile(r"(?<![\w.-])(?:E\d+\.\d+|C\d\.\d+|P\d{1,2}|T\d)(?![\w-])")


def references(after):
    """§8.2: every referenced ID is defined. Exemptions are rules, each with its evidence; nothing is waved through."""
    su = after["suite"]
    sql = rd("work", "sql-databases-companion.md").split("\n")
    mask = code_mask(sql)
    sql_ids = after["files"]["sql-databases-companion.md"]["items"]["ids"]
    defined = set(su["defined_in"])
    ex, bad = {}, []
    for f, u in sorted(su["unresolved_refs"].items()):
        for tok, lines in sorted(u.items()):
            allrefs = after["files"][f]["items"]["ids"][tok]["referenced"]
            only_code = all(mask[n - 1] for n in allrefs) if f == "sql-databases-companion.md" else False
            if f == "sql-databases-companion.md" and re.fullmatch(r"E\d+\.\d+", tok) and only_code:
                if "SQL-" + tok in defined:
                    ex.setdefault("SQL kit data label E<l>.<n> = card SQL-E<l>.<n> (code only)", []).append(tok)
                    continue
            if f == "sql-databases-companion.md" and re.fullmatch(r"C\d\.\d+", tok) and only_code:
                if "SQL-CAP" + tok[1:] in defined:
                    ex.setdefault("SQL kit data label C<n>.<m> = capstone step SQL-CAP<n>.<m> (code only)", []).append(tok)
                    continue
            if f == "sql-databases-companion.md" and re.fullmatch(r"P\d{1,2}", tok) and only_code:
                ex.setdefault("SQL kit runner label P<n> inside the kit code; the course text names them PX-<n> "
                              "(RD-6, C-52)", []).append(tok)
                continue
            if f == "sql-databases-companion.md" and re.fullmatch(r"T[1-6]", tok) and \
                    any(mask[i] and re.search(rf"\b{tok}\b", l) for i, l in enumerate(sql)):
                ex.setdefault("SQL tx_tests scenario label T<n>, defined in the kit's tx_tests code (RD-6)", []).append(tok)
                continue
            if f == "sql-databases-companion.md" and tok in ("SQL-T-HS", "SQL-T-UG", "SQL-T-GR") and \
                    any(l.startswith("- Tiers:") and f"`{tok}`" in l for l in sql):
                ex.setdefault("SQL tier legend (§0 'Tiers:' line) defines the tier tags", []).append(tok)
                continue
            if f == "go-language-companion.md":
                g = rd("work", f).split("\n")
                occ = [g[n - 1] for n in allrefs]
                # each rule demands the context on every occurrence, so a real reference with the same token still fails
                if tok == "C11" and all(re.search(r"\bC11 (atomics|and modern JavaScript)", l) and "Java" in l for l in occ):
                    ex.setdefault("Go: C11 is the ISO C standard in a language contrast (every occurrence names Java too)",
                                  []).append(tok)
                    continue
                if tok == "T0" and all(re.search(r"\bT0 = 0\b", l) and "TOTP" in l for l in occ):
                    ex.setdefault("Go: T0 is the RFC 6238 TOTP epoch parameter (`T0 = 0` in a TOTP exercise)", []).append(tok)
                    continue
                if all(re.search(rf"`[^`]*\b{re.escape(tok)}\b[^`]*`", l) and
                       not re.sub(r"`[^`]*`", "", l).count(tok) for l in occ):
                    ex.setdefault("Go: sample input data inside an inline code span (every occurrence), e.g. `sku=A12;qty=3`",
                                  []).append(tok)
                    continue
            bad.append(f"{SHORT[f]}:{tok} (L{','.join(map(str, lines[:4]))})")
    return bad, ex


def orphans(after):
    """R3 gate: zero orphans. An orphan is a companion module card (a heading-defined module ID, not an exercise or
    key) that is bound nowhere: no main-course anchor in its own stitch header and no row in its file's §2 stitch
    table. Every stitch anchor that looks like a main-course module ID must exist in the main course."""
    cur = rd("work", "Curriculum.md")
    mods = set(re.findall(r"^#{1,6} ([A-D]\d{1,2})\b", cur, re.M)) | set(re.findall(r"^\| ([MUS]\d{1,2}) \|", cur, re.M))
    EXER = re.compile(r"^(?:SQL|SEC)-(?:E|Z0|CAP|SKIP)|^GO-(?:E|P|CAP)|^[EZ]\d|^[POQ]\d{2}$|^C\d\.|^SDP-")
    orph, undefined_anchor, n_mod = [], [], 0
    for f in COURSE[1:]:
        t = rd("work", f)
        lines = t.split("\n")
        s2 = re.search(r"^## 2\. .*?(?=^## 3\.|\Z)", t, re.M | re.S)
        table = s2.group(0) if s2 else ""
        ids = after["files"][f]["items"]["ids"]
        # a §2 range binds every member: "PX-1 … PX-11", "F-01…04", "TX-1 – TX-7" (same prefix, same zero-padding)
        ranged = set()
        for p, a, p2, b in re.findall(r"(?<![\w-])([A-Z]{1,4}-)(\d+)\s*(?:…|–|\.\.\.)\s*([A-Z]{1,4}-)?(\d+)(?![\w.-])", table):
            if p2 and p2 != p:
                continue
            w = len(a) if a.startswith("0") else 0
            ranged |= {f"{p}{i:0{w}d}" if w else f"{p}{i}" for i in range(int(a), int(b) + 1)}
        for tok, r in ids.items():
            heads = [d for d in r["defined"] if d["kind"] == "heading"]
            if not heads or EXER.search(tok):
                continue
            n_mod += 1
            h = lines[heads[0]["line"] - 1]
            anchors = re.findall(r"(?<![\w-])([A-DMUS]\d{1,2})(?![\w-])", h.split("— stitch:")[1]) if "— stitch:" in h else []
            undefined_anchor += [f"{SHORT[f]}:{tok}→{a}" for a in anchors if a not in mods]
            in_table = re.search(rf"(?<![\w-]){re.escape(tok)}(?![\w-])", table) is not None or tok in ranged
            stitched = "— stitch:" in h
            if not (stitched or in_table):
                # a group heading (e.g. "O01–O07 · …", "AP-01…AP-10") is bound through its members
                orph.append(f"{SHORT[f]}:{tok}")
    return orph, undefined_anchor, n_mod


def section_82(after, before):
    per, lost = item_survival(before)
    tot = {"work": 0, "records": 0, "lost": 0}
    for f, cats in per.items():
        for c in cats.values():
            for k in tot:
                tot[k] += c[k]
    row("5 §8.2", "every R1 manifest item survives after the rename (lines, headings, table rows, checkboxes, labels, "
        "verify flags, goldens, K entries, primer sets)", "PASS" if not lost else "FAIL",
        f"{tot['work']} in the course text · {tot['records']} kept verbatim in records/ (each with its journal entry "
        f"and reason; the §8.2 'Merges' list) · {tot['lost']} lost" + (f"; first: {lost[:3]}" if lost else ""))
    su = after["suite"]
    row("5 §8.2", "defined-count(ID) == 1 across the six parts (primary definitions)",
        "PASS" if su["counts"]["collisions_primary"] == 0 else "FAIL",
        f"{su['counts']['tokens_defined']} defined tokens; primary collisions {su['counts']['collisions_primary']} "
        f"{list(su['collisions_primary'])[:5]}")
    bad, ex = references(after)
    row("5 §8.2", "every referenced ID is defined (R3 hard gate: zero undefined references)", "PASS" if not bad else "FAIL",
        f"{len(bad)} undefined {bad[:8]}; exempt by rule: " + "; ".join(f"{k}: {len(v)}" for k, v in sorted(ex.items())))
    orph, und, n = orphans(after)
    row("5 §8.2", "zero orphans: every companion module card is bound (stitch header or §2 row), and every stitch anchor "
        "is a main-course module", "PASS" if not orph and not und else "FAIL",
        f"{n} module cards; unbound {len(orph)} {orph[:10]}; undefined anchors {len(und)} {und[:10]}")
    PSEUDO = re.compile(r"A10/B5\.\d|A5/Phase4-Net\.\d|Phase4-Sec\.\d|A5 TLS / Phase 4 Armor|§B5 IAM|gcp\.md")
    # the Edition probe is the cyber file's own title defect (meta-prompt C-10 table; audit_r2 c10 runs it on "sec"
    # only); the primer and SQL companions are titled "… — GCP-Native Edition" on purpose
    EDITION = re.compile(r"Standalone Edition|GCP-Native Edition")
    hits = [(f, i) for f in COURSE for i, l in enumerate(rd("work", f).split("\n"), 1)
            if PSEUDO.search(l) or (f == "cloud-cybersecurity-companion.md" and EDITION.search(l))]
    row("5 §8.2", "zero foreign parent names and pseudo-anchors (C-01, C-10, C-NEW-09)", "PASS" if not hits else "FAIL",
        f"hits {hits[:6]}")
    MANGLED = re.compile(r"(?<![\w-])(?:[EZ]\d*[AB]5 (?:IAM|TLS)|[EZ][A-Z]\d)(?<!EC2)(?![\w-])")
    mg = []
    for f in COURSE:
        L = rd("work", f).split("\n")
        m = code_mask(L)
        mg += [(SHORT[f], i + 1, x.group(0)) for i, l in enumerate(L) if not m[i]
               for x in MANGLED.finditer(l) if x.group(0) not in ("A2A",)]
    row("5 §8.2", "zero mangled IDs (C-10 corruption signature; `A2A` whitelisted, C-NEW-08)", "PASS" if not mg else "FAIL",
        f"{len(mg)} {mg[:6]}")
    # unqualified legacy labels outside the kit code (rename_checks.py's work/ form; the kit keeps its own labels)
    uq = []
    for f in ("sql-databases-companion.md", "cloud-cybersecurity-companion.md"):
        L = rd("work", f).split("\n")
        m = code_mask(L)
        for i, l in enumerate(L):
            if m[i]:
                continue
            for pat in (r"(?<![\w.-])E\d+\.\d+(?![\w])", r"(?<![\w.-])Z0(?![\w])", r"(?<![\w.-])E1[12](?![\w.])"):
                uq += [(SHORT[f], i + 1, x.group(0)) for x in re.finditer(pat, l)]
            if f.startswith("sql"):
                uq += [(SHORT[f], i + 1, x.group(0)) for x in re.finditer(r"(?<![\w-])P\d{1,2}(?![\w])", l)]
    row("5 §8.2", "no unqualified pre-rename labels in course text (E<l>.<n>, Z0, E11/E12, SQL P<n>) outside the kit "
        "code", "PASS" if not uq else "FAIL", f"{len(uq)} {uq[:6]}")
    ticked = {SHORT[f]: len(re.findall(r"^\s*- \[[xX]\]", rd("work", f), re.M)) for f in COURSE}
    row("5 §8.2", "ledger-done items exist and are still done", "N/A (D2)",
        f"fresh start: nothing is done; ticked boxes {ticked}", "INFO")
    row("5 §8.2", "each count ≥ its R1 count", "N/A (R10 only)", "checked at R10; R3 lists the counts in "
        "manifest-after-summary.md", "INFO")
    primer_checks(after, before)


def primer_checks(after, before):
    f = "system-design-primer-companion.md"
    pa, pb = after["files"][f]["items"]["primer"], before["files"][f]["items"]["primer"]
    same = pa["verbatim_6_1_hash"] == pb["verbatim_6_1_hash"] and pa["verbatim_6_2_hash"] == pb["verbatim_6_2_hash"]
    row("5 §8.2 primer", "verbatim §6.1/§6.2 table hashes identical", "PASS" if same else "FAIL",
        f"6.1 {pb['verbatim_6_1_hash']}→{pa['verbatim_6_1_hash']} · 6.2 {pb['verbatim_6_2_hash']}→{pa['verbatim_6_2_hash']}")
    cc = [l for l in rd("inputs-original", f).split("\n") if "CC BY" in l]
    note = "Modified on 2026-09-24, when this companion was fitted into"
    w = rd("work", f)
    row("5 §8.2 primer", "CC BY attribution line identical + the modification note", "PASS" if all(
        l in w for l in cc) and note in w else "FAIL", f"{len(cc)} CC BY lines verbatim; note present: {note in w}")
    # mermaid: compare edges after mapping the pre-rename node names (labels changed with the renames)
    eb, ea = set(pb["mermaid_edges"]), set(pa["mermaid_edges"])
    row("5 §8.2 primer", "mermaid edge set ⊇ the R1 edge set", "PASS" if eb <= ea else "FAIL",
        f"before {len(eb)} · after {len(ea)} · missing {sorted(eb - ea)[:6]}")
    # C-24/C-41: header stitches, §2 and §4.5 were generated from the binding table in R2; R2b may reword cells but
    # must not change a binding token
    TOK = re.compile(r"(?<![\w-])(?:SD|SX)-\d{2}[a-c]?(?:\[[^\]]*\])?(?:@[\w ./+-]+?(?=[ ,;·|)]|$))?~?")

    def gen(t):
        L = t.split("\n")
        out = [l for l in L if re.match(r"^#### (SD|SX)-\d\d", l)]
        for pat in (r"^## 2\. ", r"^### 4\.5"):
            on = False
            for l in L:
                if re.match(pat, l):
                    on = True
                    continue
                if on and re.match(r"^##", l):
                    break
                if on and l.startswith("|"):
                    out.append(l)
        return [sorted(TOK.findall(l)) for l in out]
    g_b, g_a = gen(rd("outputs", "r2b", "in", f)), gen(w)
    row("5 §8.2 primer", "header stitches, §2 and §4.5 still carry exactly the binding-table tokens generated in R2 "
        "(C-24, C-41)", "PASS" if g_b == g_a else "FAIL",
        f"{len(g_a)} generated lines, {sum(map(len, g_a))} binding tokens; differing lines "
        f"{sum(1 for x, y in zip(g_b, g_a) if x != y) + abs(len(g_a) - len(g_b))}")
    # C-31: no primer paragraph longer than 20 words appears outside the primer
    src = rd("inputs-original", f)
    cur_in = rd("inputs-original", "Curriculum.md")
    paras = {l.strip() for l in src.split("\n") if len(l.split()) > 20 and not l.lstrip().startswith("|")
             and l.strip() not in cur_in}
    leaks = sorted((SHORT[g], p[:50]) for g in COURSE if g != f for p in paras if p in rd("work", g))

    def grams(t, n=21):
        ws = re.findall(r"\S+", t)
        return {" ".join(ws[i:i + n]) for i in range(max(0, len(ws) - n + 1))}
    pg = set()
    for p in paras:
        pg |= grams(p)
    # a run is exempt only when the line is the file's OWN input text: traced back through the R2b journal and the
    # R2 journal (same file, rewrites only — a move from the primer never traces) to its own renamed input line.
    # Shared suite boilerplate (the companion contract) converged once D11 gave every copy the same parent name.
    back = {}
    for jf in (("outputs", "r2b", "journal.jsonl"), ("outputs", "r2", "journal.jsonl")):
        for l in open(os.path.join(ROOT, *jf), encoding="utf-8"):
            j = json.loads(l)
            if j.get("cls", "") != "move" and len(j["before"]) == len(j["after"]):
                for b_, a_ in zip(j["before"], j["after"]):
                    back.setdefault((j["file"], a_), set()).add(b_)

    def own_input(g, line):
        seen, todo = set(), {line}
        own = set(rd("outputs", "r2", "renamed", g).split("\n"))
        while todo:
            x = todo.pop()
            if x in own:
                return True
            seen.add(x)
            todo |= back.get((g, x), set()) - seen
        return False
    runs, own_runs = set(), []
    for g in COURSE:
        if g == f:
            continue
        for i, l in enumerate(rd("work", g).split("\n"), 1):
            if len(l.split()) > 20 and grams(l) & pg:
                if own_input(g, l):
                    own_runs.append(f"{SHORT[g]}:L{i}")
                else:
                    runs.add(SHORT[g])
    runs = sorted(runs)
    row("5 §8.2 primer", "no primer paragraph longer than 20 words outside the primer (C-31; whole paragraphs and any "
        "21-word run)", "PASS" if not leaks and not runs else "FAIL",
        f"{len(paras)} primer paragraphs checked; whole-paragraph leaks {leaks[:3]}; files with a 21-word run {runs}; "
        f"runs in a file's own input text (traced through both journals, not primer material) {own_runs}")
    a, b = len(pa["my_addition_labels"]), len(pb["my_addition_labels"])
    row("5 §8.2 primer", "every 'my addition' / 'my math' label still present", "PASS" if a >= b else "FAIL", f"{b} → {a}")
    mn = (len(pb["modern_notes"]), len(pa["modern_notes"]))
    row("5 §8.2 primer", "every 'Modern note' still present", "PASS" if mn[1] >= mn[0] else "FAIL", f"{mn[0]} → {mn[1]}")


# ---------------------------------------------------------------- 6. Go companion D3
def go_d3():
    old = rd(GO_R2C).split("\n")
    src = rd("authored", "go-language-companion.md")
    rec = rd("records", "go-language-companion.md")
    lost = [(n, l[:80]) for n, l in enumerate(old, 1) if l.strip() and l.strip() not in src and l.strip() not in rec]
    kept = sum(1 for l in old if l.strip() and l.strip() not in src and l.strip() in rec)
    row("6 Go D3", "every line of the R2c Go source survives in the current source or in records/", "PASS" if not lost
        else "FAIL", f"{sum(1 for l in old if l.strip())} lines; {kept} extended in R2c-bis and kept in records/; "
        f"lost {len(lost)} {lost[:3]}")
    work = rd("work", "go-language-companion.md")
    miss = [l[:80] for l in src.split("\n") if l.strip() and not l.startswith("@@") and l.strip() not in work]
    row("6 Go D3", "every line of the authored Go source is in work/ (markers replaced)", "PASS" if not miss else "FAIL",
        f"missing {len(miss)} {miss[:3]}")


# ---------------------------------------------------------------- 7. conflict register (audit_r2 probes)
def load_audit_r2():
    argv = sys.argv
    sys.argv = [argv[0], ROOT]
    spec = importlib.util.spec_from_file_location("audit_r2", os.path.join(TOOLS, "audit_r2.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    sys.argv = argv
    return m


def lineage(cid):
    """every non-blank line an R2 journal entry wrote for cid reaches live course text (verbatim, or through the
    R2b journal's rewrites), or was removed by a named R2b rule and is kept in records/"""
    J2 = [json.loads(l) for l in open(os.path.join(ROOT, "outputs", "r2", "journal.jsonl"), encoding="utf-8")]
    J3 = [json.loads(l) for l in open(os.path.join(ROOT, "outputs", "r2b", "journal.jsonl"), encoding="utf-8")]
    succ = {}
    for j in J3:
        pairs = zip(j["before"], j["after"]) if len(j["before"]) == len(j["after"]) else ((b, None) for b in j["before"])
        for b, a in pairs:
            succ.setdefault((j["file"], b), []).append((a, j["rule"]))
    work = {f: rd("work", f) for f in ORIG5}
    rec = {f: rd("records", f) for f in ORIG5}
    res = {}

    def fate(f, l, d=0):
        if l.strip() in work[f]:
            return "live"
        for a, r in succ.get((f, l), []):
            if a is None:
                return "records" if l.strip() in rec[f] else "lost"
            if d < 8:
                x = fate(f, a, d + 1)
                if x != "lost":
                    return x
        return "records" if l.strip() in rec[f] else "lost"
    for j in J2:
        if j["file"] in work and re.search(rf"\b{re.escape(cid)}\b", j.get("cid") or ""):
            for l in j["after"]:
                if l.strip():
                    k = fate(j["file"], l)
                    res[k] = res.get(k, 0) + 1
    return res


def conflicts():
    a = load_audit_r2()
    cur, pri, sql, dp, sec = (rd("work", f) for f in ORIG5)
    stitch = lambda t, mid: (re.search(rf"^#### {re.escape(mid)} · .*— stitch: (.*)$", t, re.M) or [None, ""])[1]
    # substance probes for conflicts whose R2 probe looked for text that R2b removed on purpose (D5, D6, D11)
    SUB = {
        "C-06": (lambda: "northstar-reference-app.md" not in os.listdir(os.path.join(ROOT, "work")),
                 "D5: Northstar deleted; the N8.1.5/N8.1.6 material is taught by SQL OD-09 and the primer's sketches"),
        "C-07": (lambda: "northstar-reference-app.md" not in os.listdir(os.path.join(ROOT, "work")),
                 "D5: Northstar deleted; each pointed-to lab now lives in its owning module (R2b, cyber build labs)"),
        "C-32": (lambda: "northstar-reference-app.md" not in os.listdir(os.path.join(ROOT, "work")),
                 "D5: Northstar deleted, so the Northstar-only P08/TF rule has no file to live in"),
        "C-31": (lambda: True, "re-implemented in §8.2 primer rows (whole paragraphs and 21-word runs)"),
        "C-14": (lambda: stitch(sec, "CR-11").startswith("A5 TLS · A10") and "public-key intuition bridge" in sec,
                 "CR-11 stitch starts 'A5 TLS · A10'; the A5 row names the public-key intuition bridge"),
        "C-28": (lambda: all(s in pri for s in ("Taught by (index module)", "Shared lab", "Check owner")),
                 "SD-35 index module: Taught-by pointers, shared-lab line, check-owner line (conflict tags dropped, D6)"),
        "C-29": (lambda: all("**0.4.2 Suite Session Protocol" in t for t in (pri, sql, dp, sec)),
                 "the pointer became the copied contract: rule 0.4.2 Suite Session Protocol is in every companion §0"),
        "C-30": (lambda: "progress ledger (main course §0.1) is a running record beside these boxes" in pri,
                 "primer rule 6 exception reworded without file names (R2b PRI-2)"),
        "C-41": (lambda: True, "the 'generated from' markers named a file (D6); the generated content is checked token "
                              "by token in the §8.2 primer rows"),
        "C-49": (lambda: "A7.1 client-server and API styles" in cur and "A7.4 GRASP + creational patterns" in cur,
                 "A7 teaching blocks A7.1…A7.4 present"),
        "C-51": (lambda: not re.search(r"(?<![\w.-])E1[12](\.\d+)?(?![\w.])", "\n".join(
            l for l, m in zip(sql.split("\n"), code_mask(sql.split("\n"))) if not m)),
                 "no E11/E12 labels in SQL course text; the kit code keeps its own data labels"),
        "C-54": (lambda: "**0.4.3 Exercise progression.**" in cur and "ten-rung ramp" in cur, "rule 0.4.3 ten-rung ramp"),
        "C-55": (lambda: "**0.4.6 Anchoring and suite-wide Prop Lock.**" in cur, "rule 0.4.6"),
        "C-57": (lambda: "progress ledger" in sql, "SQL rule 8 names the progress ledger (no file name, D6)"),
        "C-62": (lambda: "Repository's definition is owned by ARCH-07" in dp, "ARCH-06 points to ARCH-07's definition"),
        "C-70": (lambda: "calibrating question" in cur, "rule 0.4.1 puts the learner preferences over the calibrating "
                                                       "questions"),
        "C-71": (lambda: "**0.4.5 Mastery states.**" in cur and "`not-started` → `in-progress` → `taught`" in cur,
                 "rule 0.4.5 mastery states"),
        "C-74": (lambda: "says explicitly when unsure" in cur, "rule 0.4.7 accuracy standard"),
        "C-75": (lambda: "- Overrides: the learner may skip" in cur, "rule 0.4.1 overrides"),
        "C-NEW-01": (lambda: "Source material:" not in sql and "Source material:" in rd("records", "sql-databases-companion.md"),
                     "D6 moved the `Source material:` lines to records/ (D1 borrowing is recorded there)"),
        "C-NEW-06": (lambda: all("**0.4.2 Suite Session Protocol" in t for t in (pri, sql, dp, sec)), "as C-29"),
    }
    NOTE = {c: "conflict tag dropped from course text (D6 V5); the note itself is traced below" for c in
            ("C-17", "C-18", "C-19", "C-20", "C-21", "C-48")}
    rows = []
    for cid, ph, probe, note in a.REG + a.CNEW:
        if probe is None:
            rows.append((cid, ph, "deferred" if not ph.startswith("D2") else "D2", note or "—"))
            continue
        try:
            st, ev = probe()
        except Exception as e:           # a probe that reads the deleted Northstar file
            st, ev = "ERROR", type(e).__name__
        if st == "PASS":
            rows.append((cid, ph, "PASS", ev))
            continue
        lin = lineage(cid)
        if cid in SUB:
            ok = SUB[cid][0]()
            rows.append((cid, ph, "PASS (substance)" if ok else "FAIL", f"R2 probe: {st}; substance: {SUB[cid][1]}; "
                                                                        f"R2 edits traced: {lin or 'none'}"))
        elif cid in NOTE:
            ok = lin and not lin.get("lost") and lin.get("live")
            rows.append((cid, ph, "PASS (lineage)" if ok else "FAIL", f"R2 probe: {st}; {NOTE[cid]}; R2 edits traced: {lin}"))
        else:
            rows.append((cid, ph, "FAIL", f"R2 probe: {st} {ev}; no substance probe"))
    fails = [r for r in rows if r[2] == "FAIL"]
    row("7 conflicts", "C-01…C-75 and C-NEW-01…09 still resolved in the current files", "PASS" if not fails else "FAIL",
        f"{sum(r[2] == 'PASS' for r in rows)} PASS · {sum(r[2].startswith('PASS (') for r in rows)} PASS by substance or "
        f"lineage · {sum(r[2] == 'deferred' for r in rows)} deferred to their owner phase · {sum(r[2] == 'D2' for r in rows)} "
        f"D2 · {len(fails)} FAIL {[r[0] for r in fails]}")
    return rows


# ---------------------------------------------------------------- 8. §12.7 lints
PART = [(r"main course", COURSE[0]), (r"[Pp]rimer|System Design", COURSE[1]), (r"\bSQL\b", COURSE[2]),
        (r"[Dd]esign[- ][Pp]atterns|patterns companion", COURSE[3]), (r"[Cc]ybersecurity|\bcyber\b", COURSE[4]),
        (r"\bGo\b", COURSE[5]), (r"[Cc]ompanion", None)]


def sec_refs():
    T = {f: rd("work", f) for f in COURSE}

    def secs(t):
        s = set(m.group(1).rstrip(".") for m in re.finditer(r"^#{1,6}\s+(?:Appendix\s+)?([0-9A-Z]+(?:\.[0-9a-z]+)*)[.\s]",
                                                             t, re.M))
        return s | set(re.findall(r"\*\*(\d+\.\d+\.\d+)\b", t))
    S = {f: secs(T[f]) for f in COURSE}

    def has(f, ref):
        if ref in S[f] or any(x.startswith(ref + ".") for x in S[f]):
            return True
        p = ref.rsplit(".", 1)
        return len(p) == 2 and p[1].isdigit() and "." in p[0] and p[0] in S[f]   # §0.2.10 = rule 10 of §0.2
    bad, n = [], 0
    for f in COURSE:
        L = T[f].split("\n")
        m = code_mask(L)
        for i, l in enumerate(L, 1):
            if m[i - 1]:
                continue
            for x in re.finditer(r"§\s?([0-9A-Z]+(?:\.[0-9a-z]+)*)", l):
                n += 1
                ref, pre = x.group(1).rstrip("."), l[max(0, x.start() - 60):x.start()]
                if not re.search(r"main course|[Pp]rimer|SQL|[Pp]atterns|[Cc]yber|\bGo\b|[Cc]ompanion", pre):
                    pre = l[:x.start()]          # "Its §2" in a bullet that names the part at its start
                last = max(((mm.end(), t) for rx, t in PART for mm in re.finditer(rx, pre)), default=None,
                           key=lambda z: z[0])
                if last is None:
                    ok = has(f, ref)
                elif last[1] is None:
                    ok = any(has(t, ref) for t in COURSE[1:])
                else:
                    ok = has(last[1], ref) or has(f, ref)
                if not ok:
                    bad.append(f"{SHORT[f]}:{i} §{ref}")
    return bad, n


def lints():
    bad = []
    for f in COURSE:
        L = rd("work", f).split("\n")
        m = code_mask(L)
        width = None
        for i, l in enumerate(L, 1):
            if m[i - 1] or not l.startswith("|"):
                width = None
                continue
            cells = len(re.split(r"(?<!\\)\|", re.sub(r"`[^`]*`", "``", l.strip()))) - 2
            if width is None:
                width = cells
            elif cells != width:
                bad.append(f"{SHORT[f]}:{i}")
    row("8 lints", "no table has a ragged column count (six parts, code excluded)", "PASS" if not bad else "FAIL",
        f"{len(bad)} {bad[:8]}")
    sb, n = sec_refs()
    row("8 lints", "every '§x' cross-reference resolves (in its own part, or in the part the sentence names)",
        "PASS" if not sb else "FAIL", f"{n} references; unresolved {len(sb)} {sb[:8]}")
    T = {f: rd("work", f) for f in COURSE}
    FACTS = [("99.9% monthly downtime", r"99\.9% .{0,40}?(43m ?49\.7s|43\.8 min)", {"43m49.7s", "43m 49.7s", "43.8 min"}),
             ("seconds per month", r"(2\.5 ?M(?:illion)? seconds|2\.5 million seconds)", None)]
    fr = []
    for name, rx, allowed in FACTS:
        vals = sorted({x.group(1) for t in T.values() for x in re.finditer(rx, t)})
        ok = allowed is None or set(vals) <= allowed
        fr.append(f"{name}: {vals} {'agree' if ok else 'DISAGREE'}")
    row("8 lints", "numeric facts stated in two places agree", "PASS" if all("DISAGREE" not in x for x in fr) else "FAIL",
        "; ".join(fr) + " (the other example facts in §12.7 do not occur twice in the course)")
    # ID titles: heuristic; '·' is also a list separator, so hits are reported, not gated
    ID = (r"((?:GO|SD|SX|DP|PR|AP|ARCH|CR|AU|AB|CL|WA|WL|NT|DOS|IR|PV|TH|SC|CM|CK|AI|DD|OD|SL|CS|RT|AN|DT|PQ|TX|BH|PX|TD|"
          r"SCH|F)-\d{1,2}[a-c]?)")
    title = {}
    for f in COURSE:
        for x in re.finditer(r"^#{2,5} (?:\[[ x]\] )?" + ID + r" · ([^—\n]+)", T[f], re.M):
            title[x.group(1)] = x.group(2).strip()
    wds = lambda s: re.findall(r"[a-z0-9]+", s.lower())
    hits = 0
    for f in COURSE:
        for l in T[f].split("\n"):
            if l.startswith("#"):
                continue
            for x in re.finditer(ID + r"(?:\*\*)? (?:·|—) ([^|;·—\n]{4,})", l):
                t = title.get(x.group(1))
                if t and wds(x.group(2))[:2] and wds(x.group(2))[:2] != wds(t)[:2] and wds(x.group(2))[0] not in wds(t):
                    hits += 1
    row("8 lints", "an ID has the same title everywhere (heuristic: 'ID · Title' / 'ID — Title' forms)", "INFO",
        f"{len(title)} titled IDs; {hits} candidate mismatches. " + (
            "The R3 run's 49 were read one by one: all use '·' or '—' as a separator or a description, none renames "
            "a module" if hits == 49 else "The count differs from the 49 read at R3: the new candidates are unread"),
        "INFO")
    bare = {SHORT[f]: len(re.findall(r"(?<![\"\w])Curriculum(?![\"\w])", T[f])) for f in COURSE}
    row("8 lints", "the parent is named one way ('the main course'); bare 'Curriculum' left from R2's gcp.md rewrite",
        "INFO", f"bare 'Curriculum' (not the quoted title): {bare}. D11's binding reading removes only the backticked "
                "file-style name, so this is a naming inconsistency, not a D11 failure; proposed for R4", "INFO")
    row("8 lints", "global prerequisite DAG (§12.5, dag_check.py)", "NOT RUN",
        "dag.json does not exist yet: the audit assigns C-65 (the DAG) to R4. Not claimed as a pass", "INFO")


# ---------------------------------------------------------------- report
def main():
    no_rebuild = "--no-rebuild" in sys.argv
    inputs()
    if not no_rebuild:
        rebuild()
    folded()
    after, before = manifest()
    section_82(after, before)
    go_d3()
    crows = conflicts()
    lints()
    gate = [r for r in ROWS if r[2] == "GATE"]
    fails = [r for r in gate if not r[3].startswith("PASS")]
    esc = lambda s: str(s).replace("|", "\\|").replace("\n", " ")
    md = [f"# Verification report {STAGE}", "",
          f"Generated by `refactor-tools/verify.py` (re-run: `python3 refactor-tools/verify.py . --stage {STAGE}`). "
          "Deterministic: no timestamps. GATE rows decide the result; INFO rows are reported and never counted as "
          "passes; HOLD rows wait on the learner.", "",
          f"**Result: {'PASS' if not fails else f'{len(fails)} GATE FAIL'}** · GATE rows {len(gate)} "
          f"({len(gate) - len(fails)} PASS) · INFO {sum(r[2] == 'INFO' for r in ROWS)} · HOLD "
          f"{sum(r[2] == 'HOLD' for r in ROWS)}", "",
          "R3 hard gate: zero lost items · zero undefined references · zero orphans · zero file names or links — "
          "the rows '§8.2 every R1 manifest item survives', 'every referenced ID is defined', 'zero orphans' and "
          "'D6 self-contained'.", "",
          "| Section | Check | Kind | Status | Evidence |", "|---|---|---|---|---|"]
    md += [f"| {a} | {esc(b)} | {k} | {s} | {esc(e)} |" for a, b, k, s, e in ROWS]
    md += ["", "## Conflict register re-run (audit_r2.py probes on the current files)", "",
           "`PASS (substance)` = the R2 probe looked for text that R2b removed on purpose (a conflict tag, a file name, "
           "Northstar); a probe of the resolution itself passes. `PASS (lineage)` = every line R2 wrote for the "
           "conflict is traced through the R2b journal to live text.", "",
           "| C-nn | Owner phase | Status | Evidence |", "|---|---|---|---|"]
    md += [f"| {c} | {p} | {s} | {esc(e)} |" for c, p, s, e in crows]
    open(os.path.join(ROOT, f"verification-report-{STAGE}.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
    for r in ROWS:
        print(f"{r[3]:<16} {r[2]:<4} {r[0]} · {r[1][:90]} — {r[4][:160]}")
    print(f"verify {STAGE}: {'PASS' if not fails else str(len(fails)) + ' GATE FAIL'}")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
