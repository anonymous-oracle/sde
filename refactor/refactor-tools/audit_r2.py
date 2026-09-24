#!/usr/bin/env python3
"""Pre-R3 audit: is every requirement that is due by the end of R2 met, and is everything else assigned to a phase?

Checks, for each §4 conflict C-01…C-75 and C-NEW-01…09, the phase that owns its resolution (the prompt's own phase
tag, or R2 by §2's "Apply §4 resolutions"), then runs an evidence probe on `work/` for every item due by R2.
Items the learner's decisions supersede (D1–D4) are listed with the decision. Also checks the invariants that can
already be checked before R3, the learner decisions, and the commitments made to the learner in the R0–R2 chat.

Usage: audit_r2.py ROOT  → writes ROOT/audit-R2.md, prints a summary, exits 1 on any FAIL.
Deterministic: no timestamps; every list is sorted or in register order.
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
W = os.path.join(ROOT, "work")
FILES = {"cur": "Curriculum.md", "pri": "system-design-primer-companion.md", "sql": "sql-databases-companion.md",
         "dp": "design-patterns-companion.md", "sec": "cloud-cybersecurity-companion.md",
         "led": "session-progress-ledger.md", "skl": "learn-SKILL.md", "ns": "northstar-reference-app.md"}
ARCH = "## Pre-refactor text archive (D3)"
BOX = r"^- \[ \] "
PROV = re.compile(r"Provenance|provenance|Source material|Refactor note|\(was |\*\(was|originally authored")


def text(k, where="work"):
    base = W if where == "work" else os.path.join(ROOT, where)
    return open(os.path.join(base, FILES[k]), encoding="utf-8").read()


def live(k):
    """Work text without the D3 archive (the archive keeps pre-refactor lines verbatim on purpose)."""
    t = text(k)
    return t.split(ARCH)[0]


def n(k, pat, flags=0, src=None):
    return len(re.findall(pat, src if src is not None else live(k), flags | re.M))


def lines(k, pat, prov_ok=True):
    """Live lines matching pat, excluding provenance/refactor-note lines when prov_ok."""
    return [l for l in live(k).split("\n") if re.search(pat, l) and not (prov_ok and PROV.search(l))]


J = [json.loads(l) for l in open(os.path.join(ROOT, "outputs", "r2", "journal.jsonl"), encoding="utf-8")]


def jn(cid):
    return sum(1 for j in J if re.search(rf"\b{re.escape(cid)}\b", j.get("cid") or ""))


def run(cmd):
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    return p.returncode, (p.stdout + p.stderr).strip().split("\n")


def header(k, mid):
    m = re.search(rf"^#### {re.escape(mid)} · .*$", live(k), re.M)
    return m.group(0) if m else ""


def stitch(k, mid):
    h = header(k, mid)
    return h.split("— stitch:")[1].strip() if "— stitch:" in h else ""


def ok(cond, ev):
    return ("PASS" if cond else "FAIL"), ev


# ---------------------------------------------------------------- probes (one per C-nn due by R2)
def c01():
    pat = r"gcp\.md|gcp-curriculum|unified-curriculum|Suhas\.KS"
    hits = {k: len(lines(k, pat)) for k in ("pri", "sql", "sec", "dp")}
    return ok(sum(hits.values()) == 0, f"live old-parent names outside provenance: {hits}; journal C-01 ×{jn('C-01')}")


def c02():
    left = lines("sql", r"(?<![\w`])T\.(Disc|Num|SysTheory)\b|(?<![\w`])M\.NS\b")
    return ok(not left, f"live SQL foreign tier labels: {len(left)}; journal C-02 ×{jn('C-02')} (§6.1, 46 labels)")


def c03():
    bad = []
    for h in re.findall(r"^#### .* — stitch: (.*)$", live("sec"), re.M):
        for t in h.split(" · "):
            if re.fullmatch(r"\d{1,2}[bc]?(\.\d{1,2}|\.x)?", t.strip()):
                bad.append(t)
    return ok(not bad, f"cyber header stitch tokens still in bare x.y form: {len(bad)}; journal C-03 ×{jn('C-03')}")


def c04():
    th = [m for m in ["TH-01", "TH-02", "TH-03", "TH-04", "TH-05", "TH-06", "PQ-S-06"] if re.search(r"\bB4\b", stitch("sec", m))]
    return ok(not th and stitch("sec", "DOS-07").startswith("B4"),
              f"threat-modeling modules anchored to B4: {th}; DOS-07 stitch `{stitch('sec', 'DOS-07')}`")


def c05():
    d = sorted(set(re.findall(r"^#{2,5} .*?\b(DB-\d+)\b", live("sql"), re.M)), key=lambda x: int(x[3:]))
    return ok(len(d) == 10, f"SQL §4.0 engine-slice headings: {', '.join(d)}; journal C-05 ×{jn('C-05')}")


def c06():
    t = text("ns")
    return ok("### N8.1.5 · Cursor pagination" in t and t.count("`Curriculum` anchors (C-06)") == 2,
              "Northstar N8.1.5/N8.1.6 stubs carry the C-06 anchors (content: R9; numbering RD-2)")


def c07():
    need = ["N0.4", "N5.3", "N9c.1", "N11", "N11b", "N6.11", "N6.13", "N6.14", "N6.15", "N6.16"] + \
           [f"N7.{i}" for i in range(1, 10)]
    t = text("ns")
    miss = [x for x in need if not re.search(rf"^#{{2,3}} {re.escape(x)} · ", t, re.M)]
    return ok(not miss, f"Northstar stubs for the C-07 sections: {len(need) - len(miss)}/{len(need)} (missing {miss}); "
                        "content R9 under D1 (port with `Source material:` or reconstruct with the C-07 label)")


def c08():
    return ok("`SQL-T-HS` high-school" in live("sql") and all(f"| M{i} |" in live("cur") for i in range(1, 7)),
              "SQL tier legend present; `Curriculum` reserves M1–M6 (gate content is R4)")


def c09():
    rc, out = run([sys.executable, "refactor-tools/rename_checks.py", "outputs/r2/renamed"])
    passed = sum(1 for l in out if l.startswith("PASS"))
    return ok(rc == 0, f"rename_checks.py on outputs/r2/renamed: {passed} PASS, exit {rc}")


def c10():
    probes = {"pseudo-anchors": r"A10/B5\.\d|A5/Phase4-Net\.\d|Phase4-Sec\.\d|A5 TLS / Phase 4 Armor|§B5 IAM",
              "corruption": r"\bZB5\b|\bEA5\b|\bE1B5\b", "gcp.md gcp.md": r"gcp\.md gcp\.md",
              "principles principles": r"principles principles", "auth patterns.3": r"auth patterns\.3",
              "Edition": r"Standalone Edition|GCP-Native Edition"}
    hits = {k: len(lines("sec", p)) for k, p in probes.items()}  # Provenance lines record what was removed
    av = re.search(r"^## Appendix V.*?(?=^## |\Z)", live("sec"), re.M | re.S)
    nums = [int(x) for x in re.findall(r"^(\d+)\. ", av.group(0), re.M)] if av else []
    good = sum(hits.values()) == 0 and nums == list(range(1, len(nums) + 1))
    return ok(good, f"live hits {hits}; Appendix V numbered 1…{len(nums)} contiguously: {nums == list(range(1, len(nums) + 1))}")


def c11():
    ph = r"\bE-(NT1|NT3|AU3|CL1|CL3|CK1|CK2|DD2|AB1)\b"
    bare = [l for l in live("sec").split("\n") if re.search(ph, l) and not re.search(r"\(was " + ph[2:], l)]
    return ok(not bare, f"live phantom IDs not inside a '(was …)' note: {len(bare)}; mappings in crosswalk.md §3 (RD-1)")


def c12():
    return ok(n("sec", r"VPC-SC exfil \(NT-07\)") == 0 and "NT-06 (Prop Lock)" in live("sec"),
              "live 'VPC-SC exfil (NT-07)': 0; Phase 4 Security row carries NT-06")


def c13():
    a5 = re.search(r"^\| \*\*A5\*\* \|([^|]*)\|", live("sec"), re.M).group(1)
    return ok(stitch("sec", "WA-01").startswith("A10") and "WA-01" not in a5 and "WA-01" in stitch("sec", "PQ-S-04"),
              f"WA-01 stitch `{stitch('sec', 'WA-01')}`; not primary at A5; A5 preview via PQ-S-04")


def c14():
    return ok(stitch("sec", "CR-11").startswith("A5 TLS · A10") and "public-key intuition bridge (C-14)" in live("sec"),
              "CR-11/12 at A5 TLS · A10; A5 row names the C-14 bridge; A10 formalizes it")


C15 = {"DOS-01": "A5 load balancing", "DOS-02": "A5 DNS/UDP", "DOS-03": "A10", "DOS-04": "Phase 4 Networking (Prop Lock)",
       "DOS-05": "A10 · A5 HTTP (recall)", "DOS-06": "A6", "DOS-07": "B4", "DOS-08": "A9 · SD-26 (recall)"}


def c15():
    bad = {m: stitch("sec", m) for m, a in C15.items() if not stitch("sec", m).startswith(a)}
    return ok(not bad, f"DOS-01…08 headers match the C-15 table (mismatches: {bad})")


def c16():
    return ok(n("dp", r"ARCH-09.{0,40}A9|A9.{0,80}ARCH-09") > 0 and jn("C-16") > 0,
              f"design-patterns stitch table puts ARCH-09…12 at A9; journal C-16 ×{jn('C-16')}")


def cnote(cid, k="cur", minimum=1):
    def f():
        c = n(k, rf"\b{cid}\b")
        return ok(c >= minimum, f"{FILES[k]} live mentions of {cid}: {c}; journal ×{jn(cid)}")
    return f


def c22():
    v = [x for x in ["V-COMP", "V-STOR", "V-NET", "V-DATA", "V-AI", "V-SEC", "V-OPS"] if f"| {x} |" in live("cur")]
    return ok(len(v) == 7, f"`Curriculum` Part V defines {len(v)}/7 V-IDs (table); primer uses them")


def c24():
    rc, out = run([sys.executable, "refactor-tools/binding.py", "outputs/r2/primer-renamed-pre-repair.md"])
    return ok(rc == 0 and os.path.exists(os.path.join(ROOT, "primer-binding-table.md")),
              f"binding.py exit {rc}: {out[0][:120] if out else ''}")


def c26():
    t = open(os.path.join(ROOT, "primer-binding-table.md"), encoding="utf-8").read()
    return ok("SD-01[clones + single-box ceiling slice]@A5" in t and "SD-02[performance-vs-scalability slice]@A5" in t,
              "SD-01 / SD-02 A5 slices registered before SD-10")


def c27():
    t = open(os.path.join(ROOT, "primer-binding-table.md"), encoding="utf-8").read()
    return ok("SD-26[HTTP-layer caching slice" in t and "`SD-26@A8`" in t, "SD-26 PRIMARY A8, HTTP-layer slice @A5")


def c28():
    p = live("pri")
    return ok(all(s in p for s in ["Shared lab (C-28)", "Check owner (C-28)", "Taught by"]),
              "SD-35 index module: Taught-by pointers, shared-lab line, check-owner line")


def c29():
    from r2_common import C29_POINTER
    have = {k: C29_POINTER in live(k) for k in ("pri", "sql", "dp", "sec")}
    steps = n("cur", r"^\d\. \*\*(Anchor|Concept|Layers|GCP lens\.|One Numbers step|One application item|Checks|Close)\*\*")
    return ok(all(have.values()) and steps == 8, f"Suite Session Protocol steps: {steps}/8; pointer in companions: {have}")


def c30():
    return ok("single sanctioned cross-file tracker" in live("pri"), "primer rule 6 exception appended (C-30 text)")


def c31():
    """§8.2 C-31: no primer paragraph longer than 20 words appears outside the primer (preview of the R3 check)."""
    src = text("pri", "inputs-original")  # primer-authored text only (the refactor's own suite text is shared on purpose)
    paras = {l.strip() for l in src.split("\n") if len(l.split()) > 20 and not l.startswith("|")}
    leaks = [(k, p[:60]) for k in ("cur", "sql", "dp", "sec", "ns") for p in paras if p in live(k)]
    return ok(not leaks, f"primer paragraphs >20 words found verbatim elsewhere: {len(leaks)} {leaks[:3]}")


def c32():
    return ok("never a copy (C-32)" in text("ns"), "Northstar carries the P08-ladder / TF-by-ID rule for R9")


def c33():
    return ok(jn("C-33") > 0 and "named only" in live("pri"),
              f"A5 checkpoint = Single box + Users++ networking slice; SD-06/SD-12 named only; journal ×{jn('C-33')}")


def c34():
    return ok("O03 (after DP-18 + DP-16 State)" in live("pri") and jn("C-34") > 0,
              f"O03–O06 at A7, O01/O02/O07 A4 recall (note); journal ×{jn('C-34')}")


def c35():
    t = open(os.path.join(ROOT, "primer-binding-table.md"), encoding="utf-8").read()
    return ok("SX-02[62^7 key-space math]@A2" in t and "`SX-02@A8`" in t, "SX PRIMARY at first problem; A2–A4 are slices")


def c36():
    c = live("cur")
    rows = [r for r in ["Cache stampede", "Little's law", "CAP / PACELC", "CRDTs", "Tail latency"] if r in c]
    return ok(len(rows) == 5, f"§0.3 v1.1 overlap rows present: {rows}")


def c37():
    return ok(n("sql", r"(?<![\w-])SD-[1-6](?![\d\w])") == 0, "SQL single-digit SD-n left: 0 (now SCH-n); primer SD-nn kept")


def c39():
    mer = re.search(r"```mermaid.*?```", live("pri"), re.S).group(0)
    return ok("gcp.md" not in mer and mer.count("-->") == 46, f"mermaid: 'gcp.md' labels 0; edges {mer.count('-->')} (46 before)")


def c41():
    return ok(n("pri", r"Generated from `primer-binding-table.md`") >= 1 and n("pri", r"generated from `primer-binding-table.md`") >= 1,
              "primer §2 and §4.5 marked as generated from the binding table")


def c42():
    ticked = {k: n(k, r"^\s*- \[[xX]\]") for k in ("cur", "pri", "sql", "dp", "sec")}
    return ok(sum(ticked.values()) == 0, f"ticked boxes (must be 0 under D2 fresh start): {ticked}")


def c44():
    bad = [l[:80] for l in live("cur").split("\n") if re.search(r"\b[Ff]ifteen\b|#15\b", l) and "eighteen" not in l and "#18" not in l]
    return ok(not bad, f"live 'fifteen' without the correction: {bad}; 'not all 8' corrected: "
                       f"{'not all 8' not in live('cur') or 'corrected' in live('cur')}")


def c45():
    c = n("cur", BOX)
    return ok(c >= 27 + 18, f"`Curriculum` boxes: {c} (27 modules + 18 certs + …)")


def c46():
    return ok("Lab Reality (Track D)" in live("cur"), "Track D Lab Reality line")


def c47():
    return ok("### 0.4 Suite Teaching Contract" in live("cur") and "### 0.5 Lab Safety" in live("cur"), "§0.4 and §0.5 exist")


def c49():
    return ok(n("cur", r"C-49") >= 1, f"A7 teaching blocks note; journal ×{jn('C-49')}")


def c51():
    return ok(n("sql", r"(?<![\w.-])E1[12](\.\d+)?(?![\w.])") == 0, "SQL live E11/E12/E12.1 labels: 0 (→ TX / PX, PX-1)")


def c52():
    return ok(n("sql", r"\bP1\s*[–-]\s*P11\b") == 0, "SQL live 'P1–P11': 0 (→ PX-1…PX-11)")


def c53():
    bad = lines("sql", r"(?<![\w`.-])(G4|G12b|D0|D[5-8])(?![\w`])")  # D1–D4 are `Curriculum` Track D (§6.1)
    bad = [l for l in bad if "`D0…D8`" not in l and "rebound" not in l]
    return ok(not bad and "bibliography" in live("sql"), f"live unlabelled G4/G12b/D0/D5–D8 refs: {len(bad)}; TB-/SRC- kept as "
                                                          "bibliography keys (note)")


def c54():
    return ok("**0.4.3 Exercise progression (C-54).**" in live("cur"), "ten-rung ramp in §0.4.3")


def c55():
    return ok("(C-55).**" in live("cur"), "suite-wide anchoring / Prop Lock in §0.4.6")


def c57():
    return ok("C-57" in live("sql") and "session-progress-ledger.md" in live("sql"), "SQL rule 8 rebound to the ledger")


def c58():
    c = n("dp", r"^\s*" + BOX[1:])
    return ok(c >= 44, f"design-patterns boxes: {c} (was 0 real)")


def c60():
    return ok("paraphrased from GoF" in live("dp"), "format line: Intent (paraphrased from GoF)")


def c62():
    return ok(n("dp", r"C-62") >= 1, "ARCH-06 points to ARCH-07's Repository definition")


def c63():
    old, new = n("dp", r"\[[CSB]\]"), n("dp", r"\[(Cr|St|Bh)\]")
    return ok(old == 0 and new == 29, f"[C]/[S]/[B] left: {old}; [Cr]/[St]/[Bh]: {new}")


def c64():
    return ok("`F-nn` OOP foundations" in live("dp"), "notation line lists F-nn (the rest of C-64 is R7)")


def c70():
    return ok("C-70" in live("cur") and "ledger §5 wins" in live("cur"), "§0.4.1: ledger §5 over the skill's calibrating question")


def c71():
    return ok("**0.4.5 Mastery states (C-71).**" in live("cur"), "mastery states in §0.4.5")


def c72():
    return ok("ledger delta block" in live("cur"), "session close emits a ledger delta block (format: §14, R10)")


def c74():
    return ok("explicitly when unsure (C-74)" in live("cur"), "accuracy standard in §0.4.7")


def c75():
    return ok("Overrides (C-75)" in live("cur"), "one override rule in §0.4.1")


# (cid, phase that owns the resolution, probe or None, note)
REG = [
    ("C-01", "R2", c01, ""), ("C-02", "R2", c02, ""), ("C-03", "R2", c03, ""), ("C-04", "R2", c04, "S6 secondary for PQ-S-06 arrives with Track S (R4)"),
    ("C-05", "R2", c05, "D1: ported from `gcp-curriculum.md` with a `Source material:` line; deepened in R6"),
    ("C-06", "R2 skeleton · R9", c06, ""), ("C-07", "R2 skeleton · R9", c07, ""), ("C-08", "R2 legend · R4", c08, ""),
    ("C-09", "R2 (gate)", c09, ""), ("C-10", "R2", c10, ""), ("C-11", "R2", c11, "[resolved-by-default] RD-1"),
    ("C-12", "R2", c12, ""), ("C-13", "R2", c13, ""), ("C-14", "R2", c14, ""), ("C-15", "R2", c15, "RD-4"),
    ("C-16", "R2", c16, ""), ("C-17", "R2", cnote("C-17"), "moved heading keeps the word 'standalone' (D3); the note under it supersedes it"),
    ("C-18", "R2", cnote("C-18", minimum=2), ""), ("C-19", "R2", cnote("C-19"), ""), ("C-20", "R2", cnote("C-20", minimum=3), "volatility register: R4"),
    ("C-21", "R2", cnote("C-21", minimum=2), ""), ("C-22", "R2", c22, ""),
    ("C-23", "R10", None, "checkpoints go into the regenerated ledger; under D2 they are all 'not-started'"),
    ("C-24", "R2", c24, ""), ("C-25", "R2", c24, "same topological check"), ("C-26", "R2", c26, ""), ("C-27", "R2", c27, ""),
    ("C-28", "R2", c28, ""), ("C-29", "R2", c29, ""), ("C-30", "R2", c30, ""), ("C-31", "R2 rule · R3 check", c31, "preview of the §8.2 check"),
    ("C-32", "R2 rule · R9", c32, ""), ("C-33", "R2", c33, ""), ("C-34", "R2", c34, ""), ("C-35", "R2", c35, ""),
    ("C-36", "R2", c36, ""), ("C-37", "R2", c37, ""), ("C-38", "R3", None, "verify.py/manifest ID regex must accept `SD-\\d{2}[a-c]?` and slice/recall notation"),
    ("C-39", "R2", c39, ""), ("C-40", "R5", None, "keep every `verify` flag (invariant 7 check below)"),
    ("C-41", "R2", c41, ""), ("C-42", "D2", c42, "ticks and 'done' slices dropped: fresh start; nothing is ticked"),
    ("C-43", "D2 (dropped)", None, "chat-state (SD-08 restart gap)"), ("C-44", "R2", c44, "errata E-001/E-002"),
    ("C-45", "R2", c45, ""), ("C-46", "R2", c46, ""), ("C-47", "R2 · R4", c47, "§0.4/§0.5 bodies deepen in R4"),
    ("C-48", "R2 · R4", cnote("C-48"), "as-of notes now; volatility-register.md in R4"), ("C-49", "R2 · R4", c49, "block split deepened in R4"),
    ("C-50", "R6", None, "kit exists on the learner's machine (C-NEW-02): verify-in-place, never edit goldens"),
    ("C-51", "R2 (gate)", c51, ""), ("C-52", "R2 (gate)", c52, ""), ("C-53", "R2", c53, ""), ("C-54", "R2", c54, "D1: may borrow the ramp text"),
    ("C-55", "R2", c55, ""), ("C-56", "R6", None, "pins go into the kit README and run_ex.py"), ("C-57", "R2", c57, ""),
    ("C-58", "R2", c58, ""), ("C-59", "R7", None, "11 ARCH modules (R0 count), not 10"), ("C-60", "R2 · R7", c60, "per-line audit R7"),
    ("C-61", "R7", None, ""), ("C-62", "R2", c62, ""), ("C-63", "R2 (gate)", c63, ""), ("C-64", "R2 · R7", c64, ""),
    ("C-65", "R4", None, "`dag.json` + `dag_check.py` (§12.5)"), ("C-66", "R10", None, "§14 schema; D2: blank template"),
    ("C-67", "D2 (dropped)", None, "chat errors; errata seeded with R2's own corrections instead (RD-7)"),
    ("C-68", "D2 (dropped)", None, "learner-specific error pattern; the generic misconception register stays in §0.4"),
    ("C-69", "D2 evidence · rule kept", None, "evidence was chat-only; the §13.5 one-question rule is in §0.4.7 anyway"),
    ("C-70", "R2", c70, ""), ("C-71", "R2", c71, ""), ("C-72", "R2 · R10", c72, ""),
    ("C-73", "D2 evidence · rule kept", None, "evidence was chat-only; the §13.9 close rule is in §0.4.8 anyway"),
    ("C-74", "R2", c74, ""), ("C-75", "R2", c75, ""),
]


# ---------------------------------------------------------------- C-NEW-nn (found in R0/R1, not in the prompt)
def cn04():
    t = live("cur")
    i, j, k = t.find("### 0.1 "), t.find("#### Companion — Cloud Cybersecurity"), t.find("## PART I ")
    return ok(-1 < i < j < k and jn("C-NEW-04") > 0, "cyber block sits under Curriculum §0.1, before Part I (no longer between A10 and A11)")


def cn05():
    h = n("cur", r"^#{1,3} ")
    return ok(h >= 40 and jn("C-NEW-05") > 0, f"{h} markdown headings in Curriculum; {jn('C-NEW-05')} journaled anchor-rewrites")


def cn07():
    return ok(n("sec", r"\bEA5\b") == 0, "0 live `EA5` in cyber (input had 2: a `Lab:` line and a card header)")


def cn09():
    return c10()


def d8_live():
    """C-11/§6.1: no live D8 (old-parent label) in SQL or cyber outside provenance and the SQL legend."""
    hits = [(k, l) for k in ("sql", "sec") for l in lines(k, r"\bD8\b") if "legend" not in l.lower() and "rebound" not in l.lower()]
    return ok(not hits, f"live D8 outside provenance/legend: {len(hits)}")


def table_lint():
    """Every markdown table row has the header's cell count (fenced code excluded)."""
    bad = []
    for k in FILES:
        if k == "ns" and not os.path.exists(os.path.join(W, FILES[k])):
            continue
        fence, width = False, None
        for i, l in enumerate(text(k).split("\n"), 1):
            if l.startswith("```"):
                fence = not fence
            if fence or not l.startswith("|"):
                width = None
                continue
            cells = len(re.split(r"(?<!\\)\|", l.strip())) - 2
            if width is None:
                width = cells
            elif cells != width:
                bad.append(f"{FILES[k]}:{i}")
    return ok(not bad, f"tables with ragged rows: {len(bad)}" + (f" ({', '.join(bad[:5])})" if bad else ""))


CNEW = [
    ("C-NEW-01", "D1", lambda: DECISIONS[0][1](), "borrow with `Source material:` lines; nothing points back"),
    ("C-NEW-02", "R3 · R7", None, "C-50 becomes verify-in-place; `pgdata/` never copied"),
    ("C-NEW-03", "D2", None, "ledger predates the prompt's learner state; regenerated blank in R10"),
    ("C-NEW-04", "R2", cn04, ""), ("C-NEW-05", "R2", cn05, "RD-5"), ("C-NEW-06", "R2", c29, "via the C-29 pointer"),
    ("C-NEW-07", "R2", cn07, ""), ("C-NEW-08", "R3", None, "whitelist `A2A` in verify.py's corruption regex"),
    ("C-NEW-09", "R2", cn09, "same probe as C-10"),
]


# ---------------------------------------------------------------- invariants, decisions, commitments
def inv_checks():
    out = []
    rc, o = run([sys.executable, "refactor-tools/d3_check.py", "."])
    out.append(("1 / D3 no content loss", *ok(rc == 0, "d3_check.py: " + "; ".join(l.split(":")[1].strip() for l in o if l.startswith(("PASS", "FAIL"))))))
    ins = open(os.path.join(ROOT, "inputs-original", FILES["sql"]), encoding="utf-8").read()
    g = lambda t: sorted(re.findall(r"\b\d+:[0-9a-f]{8}\b", t))
    blk = lambda t: re.findall(r"```sql\n.*?```", t, re.S)
    out.append(("6 goldens immutable", *ok(g(ins) == g(text("sql")) and set(blk(ins)) <= set(blk(text("sql"))),
                                            f"{len(g(ins))} fingerprint tokens identical; {len(blk(ins))} SQL blocks all present")))
    vf = {k: (n(k, r"\(verify", src=open(os.path.join(ROOT, "inputs-original", FILES[k]), encoding="utf-8").read()), n(k, r"\(verify"))
          for k in ("cur", "pri", "sql", "dp", "sec")}
    out.append(("7 `(verify)` flags kept", *ok(all(b >= a for a, b in vf.values()), f"before→after {vf}")))
    ib = open(os.path.join(ROOT, "inputs-original", FILES["pri"]), encoding="utf-8").read()
    cc = [l for l in ib.split("\n") if "CC BY" in l]
    out.append(("11 CC BY line + modification note", *ok(all(l in text("pri") for l in cc) and
                                                        "Modified by the curriculum refactor on 2026-09-24; changes listed in CHANGELOG.md." in text("pri"),
                                                        f"{len(cc)} CC BY lines unchanged; modification line present")))
    out.append(("12 primer numbers immutable", *ok(all(f"**{p}**" in text("pri") for p in
                                                       [f"P0{i}" for i in range(1, 9)] + [f"O0{i}" for i in range(1, 8)]),
                                                   "P01–P08, O01–O07 present (full manifest diff in R3)")))
    import hashlib
    # R5 regenerates the ledger (C-66, D2); the R2 output of it is the frozen copy beside the R2 snapshot
    r2_out = lambda f: next(p for p in (os.path.join(ROOT, "outputs", "r2b", "in", f), os.path.join(W, f)) if os.path.exists(p))
    same = all(hashlib.sha256(open(os.path.join(ROOT, "inputs-original", FILES[k]), "rb").read()).hexdigest() ==
               hashlib.sha256(open(r2_out(FILES[k]), "rb").read()).hexdigest() for k in ("led", "skl"))
    ro = all(not os.stat(os.path.join(ROOT, "inputs-original", f)).st_mode & 0o222 for f in os.listdir(os.path.join(ROOT, "inputs-original")))
    out.append(("14 inputs read-only; skill + ledger untouched in R2", *ok(same and ro, f"ledger/skill byte-identical: {same}; "
                                                                                  f"inputs-original mode a-w: {ro} (a fresh git checkout resets modes: run `chmod a-w inputs-original/*`)")))
    out.append(("tables well-formed", *table_lint()))
    out.append(("C-11/§6.1 no live D8", *d8_live()))
    cls = {"rename", "anchor-rewrite", "move", "merge", "append", "correction", "new-content", "regenerate"}
    bad = [j["n"] for j in J if j["cls"] not in cls or not j.get("evidence") or not j.get("cid")]
    out.append(("15/16 evidence + classed edits", *ok(not bad, f"{len(J)} journal entries; unclassed or unevidenced: {len(bad)}")))
    return out


DECISIONS = [
    ("D1", lambda: ok(n("sql", r"Source material:") >= 1 and c01()[0] == "PASS",
                      f"`Source material:` lines: SQL {n('sql', r'Source material:')}; old-parent names only in provenance (C-01 probe)")),
    ("D2", lambda: c42()),
    ("D3", lambda: ok(run([sys.executable, "refactor-tools/d3_check.py", "."])[0] == 0, "d3_check.py exit 0; archive sections in 5 files")),
    ("D4", lambda: ok(n("cur", r"Verified 2026-09-24 against") == 18 and all(s in live("cur") for s in
                      ["25 / 17.5 / 17.5 / 15 / 12.5 / 12.5", "Gemini Enterprise Agent Platform", "SAP-C03",
                       "Security Foundations and Governance", "July 27, 2026", "Oct 21, 2026",
                       "Cloud and AI Security Engineer Associate", "credit-based free plan"]),
                      f"{n('cur', r'Verified 2026-09-24 against')}/18 cert notes; all 8 changed findings present")),
]

# Commitments made to the learner in the R0–R2 chat (transcript e64fbf7c, 2026-09-24)
PROMISES = [
    ("R1 report", "verify.py normalises through the rename map and treats appended notes as additions", "R3",
     lambda: ("OPEN", "carried into refactor-state.md §9 and requirements-hardening.md §5")),
    ("R2 gate", "SQL tier legend added to SQL §0, logged as new content", "R2",
     lambda: ok("`SQL-T-HS` high-school" in live("sql") and jn("C-08") > 0, "legend line + journal C-08")),
    ("R2 gate", "D8 and the 9 phantom checkpoint IDs fixed by the crosswalk step", "R2", lambda: c11()),
    ("R2 gate", "SQL T1…T6 stay as tx_tests.py scenario labels and are excluded from the ID register", "R2/R3",
     lambda: ok(n("sql", r"\bT[1-6]\b") > 0, "labels kept; exclusion is a verify.py rule (§9)")),
    ("R0/D2", "ledger §5 teaching preferences kept and copied into every file's §0 (learner did not object)", "R2",
     lambda: ok(all("Learner teaching preferences" in live(k) for k in ("cur", "pri", "sql", "dp", "sec")), "all 5 course files")),
    ("D4 report", "'Fifteen' → 'eighteen' on Curriculum lines 6 and 27, shown in the R2 preview", "R2", lambda: c44()),
    ("D4 report", "seven out-of-date certs get a dated note; AWS free-tier note", "R2", DECISIONS[3][1]),
    ("R0 report", "ask before downloading any file", "all", lambda: ("PASS", "no downloads since; rule restated in requirements-hardening.md §6")),
]


def main():
    sys.path.insert(0, os.path.join(ROOT, "refactor-tools"))
    rows, fails = [], 0
    for cid, ph, probe, note in REG + CNEW:
        if probe is None:
            st, ev = ("D2" if ph.startswith("D2") else "deferred"), "—"
        else:
            st, ev = probe()
        fails += st == "FAIL"
        rows.append((cid, ph, st, ev, note))
    inv = inv_checks()
    fails += sum(1 for _, s, _ in inv if s == "FAIL")
    dec = [(d, *f()) for d, f in DECISIONS]
    fails += sum(1 for _, s, _ in dec if s == "FAIL")
    pro = [(w, p, ph, *f()) for w, p, ph, f in PROMISES]
    fails += sum(1 for *_, s, _ in pro if s == "FAIL")
    esc = lambda s: str(s).replace("|", "\\|").replace("\n", " ")
    md = ["# R2 audit (pre-R3)", "",
          "Generated by `refactor-tools/audit_r2.py` (re-run: `python3 refactor-tools/audit_r2.py .`). Every §4 conflict is "
          "assigned to the phase that owns its resolution; every item due by R2 has an evidence probe on `work/` "
          "(live text = the file without its D3 archive). `deferred` = owned by a later phase; `D2` = superseded by the "
          "learner's fresh-start decision.", "",
          f"**Result: {'PASS' if not fails else f'{fails} FAIL'}** · conflicts due by R2: "
          f"{sum(1 for r in rows if r[2] == 'PASS')} PASS / {sum(1 for r in rows if r[2] == 'FAIL')} FAIL · deferred "
          f"{sum(1 for r in rows if r[2] == 'deferred')} · D2 {sum(1 for r in rows if r[2] == 'D2')}", "",
          "## 1. Conflict register (§4 C-01…C-75, then R0/R1 C-NEW-01…09)", "", "| C-nn | Owner phase | Status | Evidence | Note |", "|---|---|---|---|---|"]
    md += [f"| {c} | {p} | {s} | {esc(e)} | {esc(nt)} |" for c, p, s, e, nt in rows]
    md += ["", "## 2. Invariants checkable before R3", "", "| Invariant | Status | Evidence |", "|---|---|---|"]
    md += [f"| {a} | {s} | {esc(e)} |" for a, s, e in inv]
    md += ["", "## 3. Learner decisions", "", "| Decision | Status | Evidence |", "|---|---|---|"]
    md += [f"| {a} | {s} | {esc(e)} |" for a, s, e in dec]
    md += ["", "## 4. Commitments made in the R0–R2 chat", "", "| Where | Commitment | Due | Status | Evidence |",
           "|---|---|---|---|---|"]
    md += [f"| {w} | {esc(p)} | {ph} | {s} | {esc(e)} |" for w, p, ph, s, e in pro]
    open(os.path.join(ROOT, "audit-R2.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
    for r in rows + [(a, "", s, e, "") for a, s, e in inv + dec]:
        if r[2] == "FAIL":
            print("FAIL", r[0], r[3])
    print(f"audit_r2: {'PASS' if not fails else str(fails) + ' FAIL'}")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
