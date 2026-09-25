"""R2 reports: `crosswalk.md`, `CHANGELOG.md`, `errata.md`, `id-rename-map.csv` (copy) and `diffs/<file>.diff`.

Everything here is derived from the build's own data (the journal, the crosswalk tables in r2_sql / r2_sec, rename.py's
events, inputs-original/ vs work/), so the reports cannot drift from the files. Deterministic: sorted, no timestamps
beyond DATE.
"""
import collections
import difflib
import json
import os
import re
import shutil

import rename
import r2_sec
import r2_sql
from r2_common import DATE, CUR, PRI, SQL, DPC, SEC, LED, SKL

FILES = [CUR, PRI, SQL, DPC, SEC]
SHORT = {CUR: "Curriculum", PRI: "primer", SQL: "SQL", DPC: "patterns", SEC: "cyber"}
CLASSES = ["rename", "anchor-rewrite", "move", "merge", "append", "correction", "new-content", "regenerate"]
NEW_FILES = ["northstar-reference-app.md"]
HDR = re.compile(r"^#### ([A-Z]{2,3}(?:-S)?-\d{2}) · (.*?) — stitch: (.*)$")

# §6.3 meanings as the prompt states them (compared against the old parent's headings in §4 of crosswalk.md)
PROMPT_N = {"N2.3": "Cloud SQL", "N5.3": "Ledger", "N6.11": "Packet-path map", "N6.14": "IAP", "N6.15": "VPC-SC",
            "N6.16": "Edge/DNS teardown", "N7.3": "Data protection", "N7.5": "Binary Authorization",
            "N7.6": "Security Command Center", "N7.8": "Key/SA incident response", "N7.9": "Governance",
            "N8.1": "Primitives", "N9.1": "Memorystore", "N9c": "AI", "N10": "Operations (10.x)"}

C53 = [("`G4` (WAL/replica/PITR)", "N2.3 + DB-10", "SQL §4.0 DB-10 row: `(foreign G4 WAL codec → N2.3)`"),
       ("`G12b`", "N-stub / by content", "appears only in the SQL §0 legend of rebound labels; no live reference"),
       ("`F1…F4`", "A3/A6/A11 by content", "`F1` → A3 + A6 (§6.1); F2–F4 appear only in the legend"),
       ("`D0…D8`", "C1–C5 by content", "D1 → C1, D2 → C4, D3/D7 → C4 + C5 (§6.1); cyber `D8` → C1–C5 by content"),
       ("`TB-…` / `SRC-…`", "explicit bibliography, labels kept", "SQL title block + C-53 note"),
       ("\"gcp-curriculum Lab safety\"", "`Curriculum` §0.5", "SQL rule 10 and §2.3"),
       ("\"Database protocol\"", "`Curriculum` §0.4.4 (predict → run → discrepancy)", "SQL rule 6"),
       ("\"Teaching contract → Learner state\"", "the §14 ledger (`session-progress-ledger.md`)", "SQL rule 8 (C-57)")]

V_IDS = [("V-COMP", "Compute"), ("V-STOR", "Storage/DB"), ("V-NET", "Networking"), ("V-DATA", "Data/Analytics"),
         ("V-AI", "AI/ML"), ("V-SEC", "Security"), ("V-OPS", "Ops/DevOps")]

PRECEDENCE = [
    ("P-1", "D1 (learner, rung 1)", "C-05/C-06/C-07/C-47/C-54 \"reconstruct\" defaults (rung 6)",
     "`gcp-curriculum.md` is not part of the course; missing owner content is written into the suite and may borrow "
     "from it with a `Source material:` line (SQL §4.0 DB-1…DB-10). Nothing points back at the old parent."),
    ("P-2", "D2 (learner, rung 1)", "invariant 3 (rung 3); C-43, C-67, C-68, C-69, C-73 and §6.2's \"NT-04 is "
     "already taught — mark done\" (rung 6)", "fresh start: no progress carried over, NT-04 stays unticked, errata "
     "and ledger start empty (the ledger is regenerated in R10)."),
    ("P-3", "D3 (learner, rung 1)", "C-18/C-19/C-20/C-48 rewrite resolutions (rung 6)",
     "nothing is removed: stale or time-bound lines get dated notes; every line changed by a correction or "
     "regeneration keeps its pre-refactor text in the file's D3 archive."),
    ("P-4", "D4 (learner, rung 1)", "C-44 \"do not guess the count; log an open question\" (rung 6)",
     "the count is 18 (all 18 certifications verified, `cert-verification.md`); the open question is closed."),
    ("P-5", "ledger §5 (rung 2)", "`learn-SKILL.md` \"ask one calibrating question\" (rung 7)",
     "`Curriculum` §0.4 uses woven checks and no separate diagnostic probing (C-70)."),
    ("P-6", "`Curriculum` on order (rung 4)", "design-patterns §2 A7 row (rung 5)",
     "ARCH-09…12 are taught in the A9 session, as the companion's own §10 gate and `Curriculum` order require (C-16)."),
]


def journal(root):
    return [json.loads(l) for l in open(os.path.join(root, "outputs", "r2", "journal.jsonl"), encoding="utf-8")]


def rename_events(root):
    ev = {}
    for f in FILES:
        _, _, events, _ = rename.process(os.path.join(root, "inputs-original", f), f)
        ev[f] = events
    return ev


def md_cell(s, n=None):
    s = s.replace("|", "\\|")
    return s if n is None or len(s) <= n else s[:n - 1] + "…"


def clip(s, n=220):
    return s if len(s) <= n else s[:n - 1] + "…"


def code(s):
    return "``" + (" " + s + " " if s.startswith("`") or s.endswith("`") else s) + "``" if s else "*(blank line)*"


def window(b, a, ctx=60, n=220):
    """the changed span of a one-line edit, with context, so long lines are not truncated before the change"""
    if len(b) <= n and len(a) <= n:
        return b, a
    p = 0
    while p < min(len(a), len(b)) and a[p] == b[p]:
        p += 1
    q = 0
    while q < min(len(a), len(b)) - p and a[-1 - q] == b[-1 - q]:
        q += 1
    lo = max(0, p - ctx)

    def cut(x):
        hi = min(len(x), len(x) - q + ctx)
        body = x[lo:hi]
        return ("…" if lo else "") + (clip(body, n) if len(body) > n else body + ("…" if hi < len(x) else ""))
    return cut(b), cut(a)


# ------------------------------------------------------------------------------------------------ crosswalk.md
def crosswalk(root, J):
    out = ["# Crosswalk (R2)", "",
           f"*Generated by `refactor-tools/reports.py` on {DATE} from the build's own tables and journal.* It lists "
           "every foreign label, anchor and ID that R2 rebound, and where it went. The ID renames of §5 are in "
           "`id-rename-map.csv`; the primer bindings are in `primer-binding-table.md`.", ""]

    # §0 parent names
    out += ["## 0. Parent-name rewrites (C-01)", "",
            "`gcp.md`, `/Users/Suhas.KS/gcp.md`, `gcp-curriculum.md` and `unified-curriculum.md` all become "
            "`Curriculum` or are rebound through §1–§4 below. Old-parent names that remain are provenance only "
            "(provenance lines, `Source material:` lines, `*(was …)*` notes and the D3 archives).", "",
            "| File | Journaled edits citing C-01 | Old-parent names left in live text |", "|---|---:|---:|"]
    for f in FILES:
        n = sum(1 for j in J if j["file"] == f and j["cid"] == "C-01")
        L = open(os.path.join(root, "work", f), encoding="utf-8").read().split("\n")
        cut = next((i for i, l in enumerate(L) if l.startswith("## Pre-refactor text archive")), len(L))
        left = sum(1 for l in L[:cut] if re.search(r"gcp\.md|gcp-curriculum|unified-curriculum", l)
                   and not re.search(r"[Pp]rovenance|Source material|Refactor note|\(was |\*was ", l))
        out.append(f"| {SHORT[f]} | {n} | {left} |")
    out.append("")

    # §1 SQL
    out += ["## 1. SQL companion: foreign label → new anchor (§6.1, C-53)", "",
            "Source: `r2_sql.FOREIGN`. Header stitches are deduplicated after the rewrite; `Nx.y` sections are "
            "stubs in `northstar-reference-app.md`.", "", "| Foreign label | New anchor(s) |", "|---|---|"]
    for k in sorted(r2_sql.FOREIGN, key=lambda s: [(0, int(x), "") if x.isdigit() else (1, 0, x)
                                                    for x in re.findall(r"\d+|[A-Za-z]+", s)]):
        out.append(f"| `{k}` | {' + '.join(r2_sql.FOREIGN[k])} |")
    out += ["| `12.S12` / `12.S13` | A8 skip-tests (renamed by §5; see `id-rename-map.csv`) |",
            "| PCA / PDE / PCDE rows | `Curriculum` Part V cert rows |", "",
            "**C-53 references not covered by §6.1:**", "", "| Reference | New anchor | Where |", "|---|---|---|"]
    out += [f"| {a} | {b} | {c} |" for a, b, c in C53]
    sql_cids = collections.Counter(j["cid"] for j in J if j["file"] == SQL and j["cls"] == "anchor-rewrite")
    out += ["", "Anchor-rewrite edits in the SQL file by conflict: " +
            ", ".join(f"{k} ×{v}" for k, v in sorted(sql_cids.items())) + ".", ""]

    # §2 cyber
    old = {}
    for l in open(os.path.join(root, "outputs", "r2", "renamed", SEC), encoding="utf-8").read().split("\n"):
        m = HDR.match(l)
        if m:
            old[m.group(1)] = m.group(3)
    new = {}
    for l in open(os.path.join(root, "work", SEC), encoding="utf-8").read().split("\n"):
        m = HDR.match(l)
        if m and m.group(1) not in new:
            new[m.group(1)] = m.group(3)
    missing = sorted(set(r2_sec.BIND) - set(new))
    assert not missing, missing
    out += ["## 2. Cyber companion: module → `Curriculum` anchor (§6.2, C-03, C-10)", "",
            f"Source: `r2_sec.BIND` ({len(r2_sec.BIND)} modules). *Old stitch* is the header after the §5 renames "
            "and before repair; *new stitch* is the live header. Each module's `Provenance` line in the file says "
            "what was kept in N-form, rebound or removed.", "",
            "| Module | Primary | Secondary | Old stitch | New stitch |", "|---|---|---|---|---|"]
    for mid in sorted(r2_sec.BIND, key=lambda s: (s.split("-")[0], s)):
        p, s = r2_sec.BIND[mid]
        out.append(f"| {mid} | {md_cell(p)} | {md_cell(' · '.join(s)) or '—'} | {md_cell(old.get(mid, '—'))} | "
                   f"{md_cell(new[mid])} |")
    out.append("")

    # §3 C-11
    out += ["## 3. Phantom checkpoints → existing cards (C-11, `[resolved-by-default]`)", "",
            "The nine `E-XX` IDs were referenced but never defined. Each maps to the existing card whose content "
            "matches; the learner may overrule any row.", "", "| Phantom | Card | Why |", "|---|---|---|"]
    out += [f"| {k} | {v} | {md_cell(w)} |" for k, (v, w) in sorted(r2_sec.PHANTOM.items())]
    out.append("")

    # §4 N-numbering
    ns = open(os.path.join(root, "work", "northstar-reference-app.md"), encoding="utf-8").read().split("\n")
    rows = []
    for k, l in enumerate(ns):
        m = re.match(r"^#{2,3} (N[\w.]+) · (.*)$", l)
        if m:
            nid, title = m.group(1), m.group(2)
            rb = next((x for x in ns[k + 1:k + 5] if x.startswith("- **Referenced by:**")), "")
            rb = rb.replace("- **Referenced by:** ", "")
            rows.append((nid, title, PROMPT_N.get(nid, ""), rb))
    out += ["## 4. N-track numbering (C-03, §6.3)", "",
            "Old-parent section `x.y` → `Nx.y`, same meaning. *Old-parent heading* is the same-numbered heading in "
            "`gcp-curriculum.md` (cited by line in `northstar-reference-app.md`); *§6.3* is the prompt's inferred "
            "meaning where it gives one. Where the two differ, the old heading is used and the row is an open "
            "question (`refactor-state.md`).", "",
            "| N-ID | Old-parent heading | §6.3 meaning | Referenced by |", "|---|---|---|---|"]
    out += [f"| {a} | {md_cell(b)} | {c or '—'} | {md_cell(d, 160)} |" for a, b, c, d in rows]
    out.append("")

    # §5 V-IDs
    out += ["## 5. Part V service-map categories → V-IDs (C-22)", "", "| V-ID | `Curriculum` Part V category |",
            "|---|---|"] + [f"| {a} | {b} |" for a, b in V_IDS] + [""]

    # §6 pseudo-anchors
    before = open(os.path.join(root, "outputs", "r2", "renamed", SEC), encoding="utf-8").read()
    after = open(os.path.join(root, "work", SEC), encoding="utf-8").read().split("\n")
    cut = next((i for i, l in enumerate(after) if l.startswith("## Pre-refactor text archive")), len(after))
    live = "\n".join(l for l in after[:cut] if not l.startswith("- **Provenance**"))
    def forms(text):  # "B5 IAM model" (cyber intro, `Curriculum` B5 is IAM) is prose, not a pseudo-anchor
        return collections.Counter(re.sub(r"\d+", "n", m.group(0)) for m in r2_sec.PSEUDO_RE.finditer(text)
                                   if not text.startswith(" model", m.end()))
    cb, ca = forms(before), forms(live)
    out += ["## 6. Corrupted pseudo-anchors removed (C-10, C-NEW-09)", "",
            "Deleted, not reverse-engineered: each module is rebound by content (§2) and its `Provenance` line names "
            "the removed token. Counted with `r2_sec.PSEUDO_RE` (digits folded to `n`).", "",
            "| Form | Before repair | Live after (excluding Provenance lines and the D3 archive) |", "|---|---:|---:|"]
    for k in sorted(cb):
        out.append(f"| `{k}` | {cb[k]} | {ca.get(k, 0)} |")
    out += [f"| **total** | **{sum(cb.values())}** | **{sum(ca.values())}** |", ""]
    assert sum(ca.values()) == 0, ca
    return out


# ------------------------------------------------------------------------------------------------ CHANGELOG.md
def changelog(root, J, ev):
    out = ["# CHANGELOG", "",
           f"*Generated by `refactor-tools/reports.py` from `outputs/r2/journal.jsonl` and `rename.py` ({DATE}).* "
           "Every edit has exactly one class (invariant 16). Each correction carries its evidence and its "
           "pre-refactor text; that text is also kept verbatim in the file's closing *Pre-refactor text archive (D3)*. "
           "Line-level detail for every edit: `outputs/r2/journal.jsonl` and `diffs/<file>.diff`.", "",
           "## R2 Repair — 2026-09-24", "", "### Summary", "",
           "| File | " + " | ".join(CLASSES) + " | total |", "|---|" + "---:|" * (len(CLASSES) + 1)]
    tot = collections.Counter()
    for f in FILES:
        c = collections.Counter(j["cls"] for j in J if j["file"] == f)
        c["rename"] += len(ev[f])
        tot.update(c)
        out.append(f"| {SHORT[f]} | " + " | ".join(str(c.get(k, 0)) for k in CLASSES) + f" | {sum(c.values())} |")
    out.append("| **all** | " + " | ".join(f"**{tot.get(k, 0)}**" for k in CLASSES) + f" | **{sum(tot.values())}** |")
    out += ["", "*rename* counts are replacements: §5 renames by `rename.py` (per-rule detail in "
            "`id-rename-map.csv`) plus the journaled C-09/C-37 follow-ups. `session-progress-ledger.md` and "
            "`learn-SKILL.md` are unchanged (the ledger is regenerated in R10, D2). New file: "
            "`northstar-reference-app.md` (skeleton; every section a stub for R9).", ""]

    out += ["### Precedence decisions (invariant 13)", "", "| # | Winner | Yields | Effect |", "|---|---|---|---|"]
    out += [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in PRECEDENCE]
    out += ["", "### Merges", "", "None. R2 merged no items; every before-item still exists (R3 checks this, §8.2).",
            ""]

    out += ["### Corrections (with evidence)", ""]
    for f in FILES:
        C = [j for j in J if j["file"] == f and j["cls"] == "correction"]
        if not C:
            continue
        out += [f"#### {SHORT[f]}", ""]
        for j in C:
            out.append(f"- **#{j['n']} {j['cid']}** — {j['evidence']}")
            if len(j["before"]) == len(j["after"]) == 1:
                b, a = window(j["before"][0], j["after"][0])
                out += [f"  - before: {code(b)}", f"  - after: {code(a)}"]
            else:
                out += [f"  - before: {code(clip(b))}" for b in j["before"]]
                out += [f"  - after: {code(clip(a))}" for a in j["after"]]
        out.append("")

    out += ["### Moves, new content, regenerated blocks", ""]
    for j in J:
        if j["cls"] in ("move", "new-content", "regenerate"):
            what = j["note"] or (j["before"][0][:80] if j["before"] else "")
            out.append(f"- #{j['n']} {SHORT[j['file']]} · {j['cls']} · {j['cid']} — {j['evidence']}"
                       + (f" ({md_cell(what, 100)})" if what else ""))
    out.append("")

    out += ["### Appends (annotations, notes, boxes, pointers)", "",
            "Grouped by file and conflict; each append adds lines and changes none.", "",
            "| File | Conflict | Count | Evidence (first) |", "|---|---|---:|---|"]
    g = collections.OrderedDict()
    for j in J:
        if j["cls"] == "append":
            g.setdefault((j["file"], j["cid"]), []).append(j)
    for (f, cid), js in g.items():
        out.append(f"| {SHORT[f]} | {cid} | {len(js)} | {md_cell(js[0]['evidence'], 140)} |")
    out.append("")

    out += ["### Anchor rewrites", "", "Old anchor → new anchor inside a line; meaning unchanged. The mapping is in "
            "`crosswalk.md`; each original line is in the journal and the diff.", "",
            "| File | Conflict | Lines |", "|---|---|---:|"]
    g = collections.Counter((j["file"], j["cid"]) for j in J if j["cls"] == "anchor-rewrite")
    for (f, cid), n in sorted(g.items(), key=lambda x: (FILES.index(x[0][0]), x[0][1])):
        out.append(f"| {SHORT[f]} | {cid} | {n} |")
    out.append("")

    out += ["### Renames (§5, `rename.py`)", "", "| File | Rule | Replacements |", "|---|---|---:|"]
    for f in FILES:
        c = collections.Counter(e[0] for e in ev[f])
        for r, n in sorted(c.items()):
            out.append(f"| {SHORT[f]} | {r} | {n} |")
    out.append("")
    return out


# ------------------------------------------------------------------------------------------------ errata.md
ERRATA = [
    ("E-001", "`Curriculum` line 6 (pre-refactor)", "\"Fifteen professional-tier certifications\"; Parts V–VII list 18 "
     "(10 GCP + 5 AWS + 3 Azure)", "eighteen (D4: all 18 kept and verified)", "count of the Parts V–VII rows; "
     "`cert-verification.md`", "content corrected (CHANGELOG C-44); the pre-refactor line is in the D3 archive"),
    ("E-002", "`Curriculum` Phase 5 line (pre-refactor)", "\"not all 8\" remaining GCP Professional certs; Agentic "
     "Architect is scheduled separately in Phase 8, so 7 remain", "\"not all 7; Agentic Architect is Phase 8\"",
     "`Curriculum` Phase 8 line", "content corrected (CHANGELOG C-44)"),
    ("E-003", "`design-patterns-companion.md` §6 format line (pre-refactor)", "each pattern's Intent was described as "
     "\"GoF's own line\"; the file's §11 says the Intent lines are close paraphrases", "\"(paraphrased from GoF)\"",
     "the file's own §11", "content corrected (CHANGELOG C-60); per-line audit scheduled for R7"),
]


def errata():
    out = ["# Errata", "",
           "Permanent, append-only log of technical errors found in teaching or content (§12.6). Created in R2 "
           f"({DATE}). Each entry: date · where · what was wrong · correct statement · evidence · what was done.", "",
           "The two chat-session errors the refactor prompt seeds here (C-67) are not carried over: decision D2 "
           "(fresh start) drops chat and progress history. Entries below are content errors found and corrected by "
           "the refactor.", "",
           "| ID | Date | Where | What was wrong | Correct statement | Evidence | Done |", "|---|---|---|---|---|---|---|"]
    out += [f"| {e[0]} | {DATE} | " + " | ".join(e[1:]) + " |" for e in ERRATA]
    out.append("")
    return out


# ------------------------------------------------------------------------------------------------ diffs
def diffs(root):
    dd = os.path.join(root, "diffs")
    os.makedirs(dd, exist_ok=True)
    stats = {}
    for f in FILES + [LED, SKL]:
        a = open(os.path.join(root, "inputs-original", f), encoding="utf-8").read().split("\n")
        b = open(os.path.join(root, "work", f), encoding="utf-8").read().split("\n")
        d = list(difflib.unified_diff(a, b, f"inputs-original/{f}", f"work/{f}", lineterm=""))
        if d:
            open(os.path.join(dd, f + ".diff"), "w", encoding="utf-8").write("\n".join(d) + "\n")
        stats[f] = (sum(1 for l in d if l.startswith("+") and not l.startswith("+++")),
                    sum(1 for l in d if l.startswith("-") and not l.startswith("---")))
    for f in NEW_FILES:
        b = open(os.path.join(root, "work", f), encoding="utf-8").read().split("\n")
        d = list(difflib.unified_diff([], b, "/dev/null", f"work/{f}", lineterm=""))
        open(os.path.join(dd, f + ".diff"), "w", encoding="utf-8").write("\n".join(d) + "\n")
        stats[f] = (len(b), 0)
    return stats


def build(root, J):
    ev = rename_events(root)
    open(os.path.join(root, "crosswalk.md"), "w", encoding="utf-8").write("\n".join(crosswalk(root, J)))
    open(os.path.join(root, "CHANGELOG.md"), "w", encoding="utf-8").write("\n".join(changelog(root, J, ev)))
    p = os.path.join(root, "errata.md")
    if not os.path.exists(p):  # permanent and append-only: seeded once, never regenerated
        open(p, "w", encoding="utf-8").write("\n".join(errata()))
    shutil.copyfile(os.path.join(root, "outputs", "r2-gate", "id-rename-map.csv"),
                    os.path.join(root, "id-rename-map.csv"))
    return diffs(root)
