#!/usr/bin/env python3
"""R2 ID renames (meta prompt §5, plus C-10 restores, C-51, C-52, C-63).

Usage:
  rename.py WORKDIR --dry-run --out-dir DIR   # writes id-rename-map.csv, rename-dryrun-summary.md,
                                              # rename-samples.md, rename-dryrun.diff; touches nothing in WORKDIR
  rename.py WORKDIR --apply --out-dir DIR     # same reports, then rewrites the files in WORKDIR

Rules run in list order, line by line, outside fenced code blocks (SQL goldens and keys are immutable,
invariant 6). Every replacement is in-line, so line counts never change. The script is idempotent:
qualified outputs (SEC-…, SQL-…, SDP-…, DOS-…) fail every rule's lookbehind, so a second run changes nothing.
"""
import argparse, csv, difflib, hashlib, os, re, sys
from collections import Counter, defaultdict

CUR = "Curriculum.md"
PRI = "system-design-primer-companion.md"
SQL = "sql-databases-companion.md"
DPC = "design-patterns-companion.md"
SEC = "cloud-cybersecurity-companion.md"

# text immediately before a bare E<n> that marks it as CR-E shorthand ("CR-E1…E8", "CR-E9/E10/E34")
CR_CHAIN = re.compile(r"CR-E\d+(?:[/…–-]E\d+)*[/…–-]$")


def R(rid, files, pat, repl, cls, src, note="", lines=None, skip=(), only=None, ctx=None):
    return dict(id=rid, files=files, pat=re.compile(pat), repl=repl, cls=cls, src=src, note=note,
                lines=lines, skip=set(skip), only=set(only) if only else None, ctx=ctx)


RULES = [
    # ---- cyber: C-10 corruption restores (restore + §5 rename in one step) ----
    R("SEC-00a", [SEC], r"(?<!\w)E1B5 IAM", "SEC-E10.5", "correction+rename", "C-10, §5",
      "mangled E10.5 (neighbours E10.1…E10.8)"),
    R("SEC-00b", [SEC], r"(?<!\w)ZB5 IAM", "SEC-Z0.5", "correction+rename", "C-10, §5", "mangled Z0.5"),
    R("SEC-00c", [SEC], r"(?<!\w)EA5 TLS / Phase 4 Armor", "SEC-E1.4", "correction+rename", "C-10, §5",
      "mangled E1.4 (sequence E1.1–E1.3 / E2.1; TH-01 lab = attacker-model picker)"),
    # ---- cyber: concept families ----
    R("SEC-01", [SEC], r"(?<![\w-])DD-(\d{2}|\*)", r"DOS-\1", "rename", "§5", "denial of service"),
    R("SEC-02", [SEC], r"(?<![\w-])DD(?![\w-])", "DOS", "rename", "§5", "bare family code (source tables, bundles)"),
    R("SEC-03", [SEC], r"(?<![\w-])DT-(\d{2}|\*)", r"IR-\1", "rename", "§5", "detection / IR"),
    R("SEC-04", [SEC], r"(?<![\w-])DT(?![\w-])", "IR", "rename", "§5", "bare family code"),
    R("SEC-05", [SEC], r"(?<![\w-])PR-(\d{2}|\*)", r"PV-\1", "rename", "§5", "privacy"),
    R("SEC-06", [SEC], r"(?<![\w-])PR(?![\w-])", "PV", "rename", "§5",
      "bare family code; only line 1201 (other bare 'PR' = pull request)", only=[1201]),
    # ---- cyber: exercises, drills, capstones, tiers ----
    R("SEC-07", [SEC], r"(?<![\w.-])E(\d+\.\d+[a-z]?)(?![\w])", r"SEC-E\1", "rename", "§5", "exercise bank"),
    R("SEC-08", [SEC], r"(?<![\w.-])E(\d{1,2})(?![\w.])", r"SEC-E\1", "rename", "§5 [resolved-by-default]",
      "bare level form; CR-E shorthand ('CR-E1…E8') excluded", ctx=CR_CHAIN),
    R("SEC-09", [SEC], r"(?<![\w.-])E\*(?!\*)", "SEC-E*", "rename", "§5", "wildcard in notation"),
    R("SEC-10", [SEC], r"(?<![\w.-])Z0(?=\.(?:\d|\*|n\b)|[^\w.]|$)", "SEC-Z0", "rename", "§5", "paper drills"),
    R("SEC-11", [SEC], r"(?<![\w-])C([1-4])(?![\w-])", r"SEC-CAP\1", "rename", "§5",
      "capstones; lines 52/101/102/120 are Curriculum Track C (Docker/K8s) and stay", skip=[52, 101, 102, 120]),
    R("SEC-12", [SEC], r"(?<![\w.-])T(\d)(?![\w.])", r"SEC-T\1", "rename", "§5", "tiers T0–T9 (ATT&CK T1552.005 untouched)"),
    # ---- SQL ----
    R("SQL-01", [SQL], r"(?<![\w.-])E12\.1(?![\w.])", "PX-1", "rename", "C-51",
      "undefined E12.1 = missing (user_id, placed_at) index seq scan = PX-1 hot/cold key plans"),
    R("SQL-02", [SQL], r"(?<![\w.-])E11(?![\w.])", "TX", "rename", "C-51", "E11 labs = transaction labs (§7.2)"),
    R("SQL-03", [SQL], r"(?<![\w.-])E12(?![\w.])", "PX", "rename", "C-51", "E12 labs = plan predictions (§7.1)"),
    R("SQL-04", [SQL], r"(?<![\w-])SD-([1-6])(?![\d\w])", r"SCH-\1", "rename", "§5, C-37", "schema-design cases"),
    R("SQL-05", [SQL], r"`E<level>\.<n>`", "`SQL-E<level>.<n>`", "rename", "§5", "notation line"),
    R("SQL-06", [SQL], r"(?<![\w.-])E(\d+\.\d+[a-z]?)(?![\w])", r"SQL-E\1", "rename", "§5", "exercise ladder"),
    R("SQL-07", [SQL], r"(?<![\w.-])E(\d{1,2})(?![\w.])", r"SQL-E\1", "rename", "§5 [resolved-by-default]",
      "bare level form ('E3 gate', 'E1–E10')"),
    R("SQL-08", [SQL], r"(?<![\w.-])Z0(?=\.(?:\d|\*|n\b)|[^\w.]|$)", "SQL-Z0", "rename", "§5", "paper drills"),
    R("SQL-09", [SQL], r"(?<![\w-])C([1-4])(?![\w-])", r"SQL-CAP\1", "rename", "§5", "capstones (incl. C1.1…C1.8)"),
    R("SQL-10", [SQL], r"(?<![\w.-])12\.S12(?![\w])", "SQL-SKIP-SQL", "rename", "§5", "skip-test"),
    R("SQL-11", [SQL], r"(?<![\w.-])12\.S13(?![\w])", "SQL-SKIP-ENGINE", "rename", "§5", "skip-test"),
    R("SQL-12", [SQL], r"(?<![\w.-])S12(?![\w])", "SQL-SKIP-SQL", "rename", "§5", "bare form and S12-A…E rows"),
    R("SQL-13", [SQL], r"(?<![\w.-])S13(?![\w])", "SQL-SKIP-ENGINE", "rename", "§5", "bare form and S13-A…C rows"),
    R("SQL-14", [SQL], r"(?<![\w-])HS(?![\w-])", "SQL-T-HS", "rename", "§5", "tier"),
    R("SQL-15", [SQL], r"(?<![\w-])UG(?![\w-])", "SQL-T-UG", "rename", "§5", "tier"),
    R("SQL-16", [SQL], r"(?<![\w-])[Gg]rad(?![\w-])", "SQL-T-GR", "rename", "§5", "tier"),
    R("SQL-17", [SQL], r"(?<![\w-])P(\d{1,2})(?![\w])", r"PX-\1", "rename", "C-52 [resolved-by-default]",
      "runner table + script labels + card tags (all 1:1 with PX-n)"),
    R("SQL-18", [SQL], r'show\("P…"\)', 'show("PX-…")', "rename", "C-52", "script-label placeholder"),
    # ---- design patterns ----
    R("DP-01", [DPC], r"\[C\]", "[Cr]", "rename", "C-63", "GoF creational"),
    R("DP-02", [DPC], r"\[S\]", "[St]", "rename", "C-63", "GoF structural"),
    R("DP-03", [DPC], r"\[B\]", "[Bh]", "rename", "C-63", "GoF behavioral"),
    # ---- primer tiers: only §4.2 + §4.3 (includes the P08 row) ----
    R("SDP-01", [PRI], r"(?<![\w.-])T([0-5])(?![\w.])", r"SDP-T\1", "rename", "§5 primer rules",
      "tiers; lines 625–680 only", lines=(625, 680)),
]


# judgment-based rules are sampled first (context exclusions, restores, family-code guesses, scoped rules)
RISKY = ["SEC-00a", "SEC-00b", "SEC-00c", "SEC-11", "SEC-06", "SEC-08", "SEC-12", "SEC-02", "SQL-01", "SQL-02",
         "SQL-07", "SQL-09", "SQL-12", "SQL-16", "SQL-17", "SQL-18", "SQL-04", "SDP-01", "DP-01", "SEC-10"]


def fence_mask(lines):
    inside, mask = False, []
    for l in lines:
        s = l.lstrip()
        if s.startswith("```") or s.startswith("~~~"):
            mask.append(True)
            inside = not inside
        else:
            mask.append(inside)
    return mask


def apply_rule_line(rule, text):
    """returns (new_text, [(old, new)])"""
    hits = []

    def sub(m):
        if rule["ctx"] is not None and rule["ctx"].search(text[: m.start()]):
            return m.group(0)
        new = m.expand(rule["repl"])
        hits.append((m.group(0), new))
        return new

    return rule["pat"].sub(sub, text), hits


def process(path, fname):
    orig = open(path, encoding="utf-8").read().split("\n")
    cur = list(orig)
    mask = fence_mask(orig)
    events = []  # (rule_id, line, old, new)
    code_hits = []
    for rule in RULES:
        if fname not in rule["files"]:
            continue
        for i, l in enumerate(cur):
            n = i + 1
            if rule["lines"] and not (rule["lines"][0] <= n <= rule["lines"][1]):
                continue
            if n in rule["skip"] or (rule["only"] is not None and n not in rule["only"]):
                continue
            if mask[i]:
                if rule["pat"].search(l):
                    code_hits.append((rule["id"], n, l.strip()[:120]))
                continue
            new, hits = apply_rule_line(rule, l)
            if hits:
                cur[i] = new
                events += [(rule["id"], n, o, w) for o, w in hits]
    return orig, cur, events, code_hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("workdir")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true")
    g.add_argument("--apply", action="store_true")
    ap.add_argument("--out-dir", required=True)
    a = ap.parse_args()
    os.makedirs(a.out_dir, exist_ok=True)
    rules_by_id = {r["id"]: r for r in RULES}
    files = [CUR, PRI, SQL, DPC, SEC, "session-progress-ledger.md", "learn-SKILL.md"]
    results = {}
    for f in files:
        results[f] = process(os.path.join(a.workdir, f), f)

    # ---- id-rename-map.csv: one row per (file, old token, new token) ----
    pairs = defaultdict(lambda: {"n": 0, "lines": []})
    for f in files:
        for rid, n, o, w in results[f][2]:
            k = (f, o, w, rid)
            pairs[k]["n"] += 1
            if n not in pairs[k]["lines"]:
                pairs[k]["lines"].append(n)

    def tok_key(k):
        f, o, w, rid = k
        return (files.index(f), [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", o)], rid)

    with open(os.path.join(a.out_dir, "id-rename-map.csv"), "w", newline="", encoding="utf-8") as fh:
        wr = csv.writer(fh)
        wr.writerow(["file", "old", "new", "rule", "source", "class", "occurrences", "lines", "note"])
        for k in sorted(pairs, key=tok_key):
            f, o, w, rid = k
            r = rules_by_id[rid]
            ls = pairs[k]["lines"]
            wr.writerow([f, o, w, rid, r["src"], r["cls"], pairs[k]["n"],
                         " ".join(map(str, ls[:12])) + (" …" if len(ls) > 12 else ""), r["note"]])

    # ---- summary: counts per file per rule ----
    S = ["# R2 rename dry run — counts per file per rule", "",
         "Generated by `refactor-tools/rename.py`. Nothing in `work/` is modified by a dry run.", "",
         "| Rule | File | Pattern → replacement | Source | Occurrences | Lines touched |", "|---|---|---|---|---:|---:|"]
    tot = Counter()
    for r in RULES:
        for f in r["files"]:
            ev = [e for e in results[f][2] if e[0] == r["id"]]
            tot[f] += len(ev)
            pat, rep = r["pat"].pattern.replace("|", "\\|"), r["repl"].replace("|", "\\|")
            S.append(f"| {r['id']} | {f} | `{pat}` → `{rep}` | {r['src']} | {len(ev)} | {len({e[1] for e in ev})} |")
    S += ["", "| File | Replacements | Lines changed | Line count before → after |", "|---|---:|---:|---|"]
    for f in files:
        orig, cur, ev, _ = results[f]
        ch = sum(1 for x, y in zip(orig, cur) if x != y)
        S.append(f"| {f} | {len(ev)} | {ch} | {len(orig)} → {len(cur)} |")
    S += ["", "## Matches inside fenced code (left untouched — invariant 6)", ""]
    anyc = False
    for f in files:
        for rid, n, t in results[f][3]:
            anyc = True
            S.append(f"- {f}:{n} [{rid}] `{t}`")
    if not anyc:
        S.append("- none")
    S += ["", "## Unmatched rules", ""]
    un = [r["id"] for r in RULES if not any(e[0] == r["id"] for f in r["files"] for e in results[f][2])]
    S.append("- " + (", ".join(un) if un else "none"))
    open(os.path.join(a.out_dir, "rename-dryrun-summary.md"), "w", encoding="utf-8").write("\n".join(S) + "\n")

    # ---- unified diff ----
    D = []
    for f in files:
        orig, cur, _, _ = results[f]
        D += difflib.unified_diff(orig, cur, f"a/{f}", f"b/{f}", lineterm="", n=0)
    open(os.path.join(a.out_dir, "rename-dryrun.diff"), "w", encoding="utf-8").write("\n".join(D) + "\n")

    # ---- 20 samples: one per rule first (deterministic), then fill by hash order ----
    changed = []
    for f in files:
        orig, cur, ev, _ = results[f]
        by_line = defaultdict(list)
        for rid, n, o, w in ev:
            by_line[n].append(rid)
        for n, rids in by_line.items():
            changed.append((f, n, sorted(set(rids)), orig[n - 1], cur[n - 1]))
    picked, seen, covered = [], set(), set()
    hashed = sorted(changed, key=lambda c: hashlib.sha256(f"{c[0]}:{c[1]}".encode()).hexdigest())
    per_file = [[r for r in RULES if f in r["files"]] for f in files]
    rr = [q[i] for i in range(max(map(len, per_file))) for q in per_file if i < len(q)]  # round-robin by file
    order = [rules_by_id[x] for x in RISKY] + [r for r in rr if r["id"] not in RISKY]
    for r in order:
        if r["id"] in covered or len(picked) >= 20:
            continue
        for c in hashed:
            if r["id"] in c[2] and (c[0], c[1]) not in seen:
                picked.append(c); seen.add((c[0], c[1])); covered.update(c[2])
                break
    for c in sorted(changed, key=lambda c: hashlib.sha256(f"{c[0]}:{c[1]}".encode()).hexdigest()):
        if len(picked) >= 20:
            break
        if (c[0], c[1]) not in seen:
            picked.append(c); seen.add((c[0], c[1]))
    picked.sort(key=lambda c: (files.index(c[0]), c[1]))
    M = ["# R2 rename dry run — 20 sampled before/after lines", "",
         "Judgment-based rules (RISKY list) are sampled first, then the rest round-robin across files (deterministic hash order); a line that exercises several rules covers them all. Long lines are cut to the changed region.", ""]

    def clip(b, a_):
        # show the window around the first/last differing chars
        i = 0
        while i < min(len(b), len(a_)) and b[i] == a_[i]:
            i += 1
        j = 0
        while j < min(len(b), len(a_)) - i and b[-1 - j] == a_[-1 - j]:
            j += 1
        lo = max(0, i - 60)
        return ("…" if lo else "") + b[lo: len(b) - j + 60] + ("…" if len(b) - j + 60 < len(b) else ""), \
               ("…" if lo else "") + a_[lo: len(a_) - j + 60] + ("…" if len(a_) - j + 60 < len(a_) else "")

    for k, (f, n, rids, b, a_) in enumerate(picked, 1):
        cb, ca = clip(b, a_)
        M += [f"**{k}. {f}:{n}** ({', '.join(rids)})", "", "```text", "- " + cb, "+ " + ca, "```", ""]
    open(os.path.join(a.out_dir, "rename-samples.md"), "w", encoding="utf-8").write("\n".join(M))

    if a.apply:
        for f in files:
            orig, cur, ev, _ = results[f]
            if ev:
                open(os.path.join(a.workdir, f), "w", encoding="utf-8").write("\n".join(cur))
    print("replacements:", {f: len(results[f][2]) for f in files})


if __name__ == "__main__":
    main()
