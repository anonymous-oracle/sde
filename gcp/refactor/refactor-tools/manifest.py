#!/usr/bin/env python3
"""R1/R3/R10 manifest (meta prompt §8.1). Read-only, idempotent: no timestamps; output is a pure function of the inputs.

Usage: manifest.py <dir-with-md-files> --out manifest.json [--summary summary.md]

Per file it extracts items, each {line, text, h} where h = sha256(normalized text)[:16]:
  lines         every non-blank line (decision D3: no line may disappear; verify.py matches these after renames)
  headings      markdown headings (level + text); for Curriculum also plain-text structural lines (PART/Phase/A5./N.)
  ids           every family-regex token → {defined:[lines], referenced:[lines]}
  table_rows    every | row | (separator rows skipped)
  checkboxes    every [ ] / [x] (line-start and inline)
  labels        every '- **Label:**' line, grouped by label
  verify        every line containing 'verify' (case-insensitive)
  goldens       SQL §6 'Golden fingerprint' + Appendix K 'Fingerprint' values keyed by exercise ID, and K SQL key blocks
  appendix_k    SQL Appendix K entry headings
  primer        primer §8.1 item 9 sets (checkboxes, verbatim §6.1/§6.2 blocks, primer numbers, §1 counts, P08 ladder,
                §5.1 Rosetta, TF-n, §6.4–6.6 counts, §6.7 Anki, §7.2 items, Modern notes, my-addition labels, mermaid)
"""
import argparse, hashlib, json, os, re, sys

FILES = ["Curriculum.md", "system-design-primer-companion.md", "sql-databases-companion.md",
         "design-patterns-companion.md", "cloud-cybersecurity-companion.md", "session-progress-ledger.md", "learn-SKILL.md",
         "go-language-companion.md", "fde-companion.md"]   # the Go (D12) and FDE (D19) companions exist only in work/

# Union of ID families (meta prompt §5 + R1 survey). Order matters only for readability; matching is non-overlapping left-to-right.
HY = ("PQ-S|CR-E|TF-DB|ARCH|Lens|SD|SX|TF|CS|SL|DB|TD|PX|OD|DD|RT|AN|DT|PQ|TX|BH|DP|PR|AP|F|CR|AU|CL|WA|AB|NT|WL|AI|CK|TH|SC|CM"
      "|DOS|IR|PV|SCH|SQL-CAP|SEC-CAP")          # post-rename families, so the same script serves R3/R10
ID_RE = re.compile(
    r"(?<![\w./-])(?:"
    r"(?:SQL|SEC)-(?:Z0\.\d+|E\d+\.\d+[a-z]?|T-(?:HS|UG|GR)|SKIP-(?:SQL|ENGINE)(?:-[A-E])?|CAP[1-4](?:\.\d+)?|T\d)"   # post-rename qualified
    r"|GO-(?:E\d+\.\d+|P\d{2}|CAP\d|\d{2})"                 # Go companion (D12, D13)
    r"|FDE-(?:CAP\d|CK\d|\d{2})|LB-\d|CF[1-8]"          # FDE companion (D19)
    r"|SDP-T[0-5]"
    r"|E-[A-Z]{2}\d"                               # cyber checkpoint IDs (E-NT1 …)
    r"|CR-E\d{1,2}"                                # cyber crypto exercises (CR-E1 … CR-E35; C-38)
    r"|(?:" + HY + r")-\d{1,2}[a-c]?(?:\.\d+)?"    # hyphenated families
    r"|[EZ]\d+\.\d+[a-z]?"                         # exercise levels / Z0 drills
    r"|C[1-4]\.\d+"                                # capstone sub-items
    r"|12\.S1[23]"                                 # SQL foreign skip tests
    r"|[POQ]\d{2}"                                 # primer P01/O01/Q01
    r"|[ABCDMUNS](?:1[0-9]|[1-9])"                 # Curriculum modules (+ new tracks M/U/N/S); no leading zero (OWASP A01)
    r"|P\d{1,2}|T\d"                               # SQL runner P1–P11, tiers
    r")(?![\w-])"
)
# tokens the bare families catch that are not IDs
ID_STOP = {"S3"}  # AWS S3

HEAD_RE = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")
CURR_STRUCT = re.compile(r"^(PART [IVX]+ —.*|Phase \d+\s.*|[ABCD]\d{1,2}\. .*|\d{1,2}\. [A-Z].*|## .*)$")
LABEL_RE = re.compile(r"^\s*[-*]\s+\*\*([^*:]{1,40}):\*\*")
BOX_RE = re.compile(r"\[( |x|X)\]")
LEAD_RE = re.compile(r"^(?:#{1,6}\s+|\s*[-*]\s+(?:\[[ xX]\]\s+)?|\s*\d+\.\s+|\|\s*)?\**\s*")


def norm(t):
    return re.sub(r"\s+", " ", t.strip())


def h(t):
    return hashlib.sha256(norm(t).encode()).hexdigest()[:16]


def item(n, t):
    return {"line": n, "text": norm(t), "h": h(t)}


def sections(lines):
    """[(start, end, level, title)] for markdown headings; end is exclusive (next heading of same/higher level)."""
    hs = [(i, len(m.group(1)), m.group(2)) for i, l in enumerate(lines) if (m := HEAD_RE.match(l))]
    out = []
    for k, (i, lv, t) in enumerate(hs):
        end = next((j for j, lv2, _ in hs[k + 1:] if lv2 <= lv), len(lines))
        out.append((i, end, lv, t))
    return out


def sec(secs, pattern):
    for s, e, lv, t in secs:
        if re.match(pattern, t):
            return s, e
    return None


def in_code(lines):
    flags, on = [], False
    for l in lines:
        if l.lstrip().startswith("```"):
            flags.append(True); on = not on; continue
        flags.append(on)
    return flags


def extract(path, name):
    raw = open(path, "rb").read()
    lines = raw.decode("utf-8").split("\n")
    code = in_code(lines)
    secs = sections(lines)
    in_key = [False] * len(lines)
    for s_, e_, lv_, t_ in secs:
        if lv_ == 2 and t_.startswith("Appendix K"):
            for j in range(s_ + 1, e_):
                in_key[j] = True
    R = {k: [] for k in ["lines", "headings", "table_rows", "checkboxes", "checkbox_mentions", "labels", "verify"]}
    ids = {}
    for i, l in enumerate(lines):
        n = i + 1
        if not l.strip():
            continue
        R["lines"].append(item(n, l))
        m = HEAD_RE.match(l)
        if m:
            R["headings"].append({**item(n, l), "level": len(m.group(1))})
        elif name == "Curriculum.md" and CURR_STRUCT.match(l.strip()):
            R["headings"].append({**item(n, l), "level": 0})
        if not code[i] and l.lstrip().startswith("|") and not re.match(r"^\s*\|[\s:|-]+\|\s*$", l):
            R["table_rows"].append(item(n, l))
        nocode = re.sub(r"`[^`]*`", "", l)  # a `- [ ]` inside a code span is a mention, not a box
        for k_, bm in enumerate(BOX_RE.finditer(nocode)):
            R["checkboxes"].append({**item(n, l), "checked": bm.group(1) != " ", "line_start": k_ == 0 and bool(re.match(r"^\s*[-*]\s+\[", nocode)), "nth": k_})
        for _ in range(len(BOX_RE.findall(l)) - len(BOX_RE.findall(nocode))):
            R["checkbox_mentions"].append(item(n, l))
        lm = LABEL_RE.match(l)
        if lm:
            R["labels"].append({**item(n, l), "label": lm.group(1).strip()})
        if re.search(r"verify", l, re.I):
            R["verify"].append(item(n, l))
        # IDs: a line defines the ID that leads it (heading, bold lead, first table cell, Curriculum module line)
        lead, kind = None, None
        if not code[i]:
            body = LEAD_RE.sub("", l, count=1)
            lm2 = ID_RE.match(body)
            if lm2 and lm2.group(0) not in ID_STOP:
                if m:
                    kind = "key" if in_key[i] else "heading"
                elif re.match(r"^\s*(?:[-*]\s+)?(?:\[[ xX]\]\s+)?\*\*", l):
                    kind = "key" if in_key[i] else "bold"
                elif re.match(r"^\|", l):
                    kind = "row"
                elif name == "Curriculum.md" and re.match(r"^[ABCD]\d{1,2}\. ", l):
                    kind = "module"
                if kind:
                    lead = lm2.group(0)
        seen_lead = False
        for tm in ID_RE.finditer(l):
            tok = tm.group(0)
            if tok in ID_STOP:
                continue
            rec = ids.setdefault(tok, {"defined": [], "referenced": []})
            if tok == lead and not seen_lead:
                rec["defined"].append({"line": n, "kind": kind}); seen_lead = True
            else:
                rec["referenced"].append(n)
    out = {k: v for k, v in R.items()}
    out["ids"] = dict(sorted(ids.items()))
    if name == "sql-databases-companion.md":
        out.update(sql_items(lines, secs))
    if name == "system-design-primer-companion.md":
        out["primer"] = primer_items(lines, secs, code)
    counts = {k: len(v) for k, v in out.items() if isinstance(v, list)}
    counts["ids_distinct"] = len(out["ids"])
    counts["ids_defined_distinct"] = sum(1 for v in out["ids"].values() if v["defined"])
    prim = lambda v: [d for d in v["defined"] if d["kind"] in ("heading", "module")] or [d for d in v["defined"] if d["kind"] == "bold"]
    counts["ids_multiply_defined_primary"] = sum(1 for v in out["ids"].values() if len(prim(v)) > 1)
    counts["ids_undefined_referenced"] = sum(1 for v in out["ids"].values() if not v["defined"])
    counts["checkboxes_checked"] = sum(1 for c in out["checkboxes"] if c["checked"])
    counts["checkboxes_line_start"] = sum(1 for c in out["checkboxes"] if c["line_start"])
    if "primer" in out:
        for k, v in out["primer"].items():
            counts["primer." + k] = len(v) if isinstance(v, list) else v
    lab = {}
    for x in out["labels"]:
        lab[x["label"]] = lab.get(x["label"], 0) + 1
    counts_by_label = dict(sorted(lab.items()))
    return {"sha256": hashlib.sha256(raw).hexdigest(), "line_count": len(lines) - (1 if lines and lines[-1] == "" else 0),
            "counts": dict(sorted(counts.items())), "labels_by_name": counts_by_label, "items": out}


def owner_id(lines, i):
    """nearest preceding heading that leads with an exercise ID"""
    for j in range(i, -1, -1):
        m = re.match(r"^#{2,6}\s+(\S+)", lines[j])
        if m:
            return m.group(1)
    return None


def sql_items(lines, secs):
    g, keys, kheads = [], [], []
    s6 = sec(secs, r"6\. Query-creation")
    k = sec(secs, r"Appendix K")
    for i, l in enumerate(lines):
        m = re.match(r"^\s*-\s+\*\*(Golden fingerprint|Fingerprint):\*\*\s*(.*)$", l)
        if m:
            where = "s6" if s6 and s6[0] <= i < s6[1] else ("K" if k and k[0] <= i < k[1] else "other")
            g.append({**item(i + 1, l), "id": owner_id(lines, i), "value": m.group(2).strip(), "where": where})
    if k:
        i = k[0]
        while i < k[1]:
            l = lines[i]
            if re.match(r"^#{3,4}\s", l):
                kheads.append({**item(i + 1, l), "id": owner_id(lines, i)})
            if l.lstrip().startswith("```sql"):
                j = i + 1
                while j < k[1] and not lines[j].lstrip().startswith("```"):
                    j += 1
                block = "\n".join(lines[i + 1:j])
                keys.append({"line": i + 1, "id": owner_id(lines, i), "h": hashlib.sha256(block.encode()).hexdigest()[:16], "n_lines": j - i - 1})
                i = j
            i += 1
    return {"goldens": g, "golden_key_blocks": keys, "appendix_k": kheads}


def primer_items(lines, secs, code):
    P = {}

    def rows(rng, kind="table"):
        if not rng:
            return []
        out = []
        for i in range(rng[0] + 1, rng[1]):
            l = lines[i]
            if kind == "table" and l.lstrip().startswith("|") and not re.match(r"^\s*\|[\s:|-]+\|\s*$", l) and not code[i]:
                out.append(item(i + 1, l))
            if kind == "list" and re.match(r"^\s*(?:[-*]|\d+\.)\s+", l) and not code[i]:
                out.append(item(i + 1, l))
        return out

    def block_hash(rng):
        if not rng:
            return None
        return hashlib.sha256("\n".join(lines[rng[0] + 1:rng[1]]).strip().encode()).hexdigest()[:16]

    P["checkboxes"] = [item(i + 1, l) for i, l in enumerate(lines) for _ in BOX_RE.finditer(re.sub(r"`[^`]*`", "", l))]
    for key, pat in [("verbatim_6_1", r"6\.1 "), ("verbatim_6_2", r"6\.2 ")]:
        rng = sec(secs, pat)
        P[key + "_lines"] = [item(i + 1, lines[i]) for i in range(rng[0] + 1, rng[1]) if code[i] and not lines[i].lstrip().startswith("```")] if rng else []
        P[key + "_hash"] = block_hash(rng)
    P["primer_numbers"] = [item(i + 1, l) for i, l in enumerate(lines) if re.search(r"primer numbers|primer:", l, re.I)]
    P["coverage_s1_rows"] = rows(sec(secs, r"1\. Coverage"))
    p08 = next(((s, e) for s, e, lv, t in secs if re.match(r"P08\b", t)), None)
    P["p08_card_rows"] = rows(p08)
    P["p08_card_lines"] = [item(i + 1, lines[i]) for i in range(p08[0], p08[1]) if lines[i].strip()] if p08 else []
    P["rosetta_5_1_rows"] = rows(sec(secs, r"5\.1 "))
    P["tf_items"] = [item(i + 1, l) for i, l in enumerate(lines) if re.search(r"(?<![\w-])TF-[1-7](?![\d\w])", l) and re.match(r"^\s*(?:[-*|]|\*\*|#)", l)]
    P["s6_4_rows"] = rows(sec(secs, r"6\.4 "))
    P["s6_5_rows"] = rows(sec(secs, r"6\.5 "))
    s66 = sec(secs, r"6\.6 ")
    P["s6_6_lines"] = [item(i + 1, lines[i]) for i in range(s66[0] + 1, s66[1]) if lines[i].strip()] if s66 else []
    s66txt = " ".join(lines[s66[0] + 1:s66[1]]) if s66 else ""
    P["s6_6_blog_tokens"] = len([t for t in re.split(r"\s·\s|;\s|,\s(?=[A-Z])", s66txt) if t.strip()])
    s67 = sec(secs, r"6\.7 ")
    P["s6_7_lines"] = [item(i + 1, lines[i]) for i in range(s67[0] + 1, s67[1]) if lines[i].strip()] if s67 else []
    P["s7_2_items"] = rows(sec(secs, r"7\.2 "), "list")
    MN = re.compile(r"(?:^\s*-\s+\*\*Modern note:\*\*|(?<!\*)\*Modern note:\*(?!\*))")  # '- **Modern note:**' lead or inline '*Modern note:*'
    P["modern_notes"] = [item(i + 1, l) for i, l in enumerate(lines) if MN.search(l)]
    P["modern_note_mentions"] = [item(i + 1, l) for i, l in enumerate(lines) if re.search(r"modern note", l, re.I) and not MN.search(l)]
    P["my_addition_labels"] = [item(i + 1, l) for i, l in enumerate(lines) if re.search(r"my addition|my math", l, re.I)]
    P["attribution"] = [item(i + 1, l) for i, l in enumerate(lines[:12]) if re.search(r"CC BY|Donne Martin", l)]
    # mermaid → node + edge sets
    nodes, edges = set(), set()
    i = 0
    while i < len(lines):
        if lines[i].strip().startswith("```mermaid"):
            j = i + 1
            while j < len(lines) and not lines[j].strip().startswith("```"):
                l = lines[j]
                for nm in re.finditer(r"([A-Za-z_][\w]*)\s*(?:\[\"?([^\]\"]*)\"?\]|\(\"?([^)\"]*)\"?\))", l):
                    nodes.add(nm.group(1) + "=" + norm(nm.group(2) or nm.group(3) or ""))
                ids_in = re.findall(r"([A-Za-z_][\w]*)(?:\s*(?:\[[^\]]*\]|\([^)]*\)))?\s*(-->|---|-.->|==>)", l)
                parts = re.split(r"\s*(?:-->|---|-\.->|==>)(?:\|[^|]*\|)?\s*", l.strip())
                heads = [re.match(r"([A-Za-z_][\w]*)", p).group(1) for p in parts if re.match(r"([A-Za-z_][\w]*)", p)]
                if len(heads) > 1 and ids_in:
                    for a, b in zip(heads, heads[1:]):
                        edges.add(a + "->" + b)
                j += 1
            i = j
        i += 1
    P["mermaid_nodes"] = sorted(nodes)
    P["mermaid_edges"] = sorted(edges)
    return P


SUB = re.compile(r"^(.*-\d{2})[a-c]$")


def suite_registry(res):
    """Which file(s) define each token (primary kinds), and which references resolve nowhere in the suite.
    Sub-IDs (SD-38a) resolve through their parent (SD-38); a group ID (SQL-CAP1) resolves through its dotted children in the same file. Ledger/skill are consumers, never definers."""
    defs = {}
    for f, v in res["files"].items():
        if f in ("session-progress-ledger.md", "learn-SKILL.md"):
            continue
        for tok, r in v["items"]["ids"].items():
            for d in r["defined"]:
                defs.setdefault(tok, {}).setdefault(f, []).append(d["kind"])
    unresolved, cross = {}, {}
    for f, v in res["files"].items():
        for tok, r in v["items"]["ids"].items():
            if not r["referenced"] and r["defined"]:
                continue
            local = bool(r["defined"])
            elsewhere = sorted(g for g in defs.get(tok, {}) if g != f)
            parent = SUB.match(tok)
            if not local and not elsewhere and parent and parent.group(1) in defs:
                elsewhere = ["(parent " + parent.group(1) + ")"]
            if not local and not elsewhere and any(k.startswith(tok + ".") and f in defs[k] for k in defs):
                local = True  # group parent (SQL-CAP1 = SQL-CAP1.1…1.8), defined through its children in this file
            if not local and not elsewhere:
                unresolved.setdefault(f, {})[tok] = r["referenced"][:12]
            elif not local:
                cross.setdefault(f, {})[tok] = elsewhere
    PRIMARY = ("heading", "module", "bold")
    multi_file = {t: {g: sorted(set(k)) for g, k in d.items()} for t, d in defs.items()
                  if sum(1 for k in d.values() if any(x in PRIMARY for x in k)) > 1}
    return {"defined_in": dict(sorted(defs.items())), "collisions_primary": dict(sorted(multi_file.items())),
            "unresolved_refs": unresolved, "cross_file_refs": cross,
            "counts": {"tokens_defined": len(defs), "collisions_primary": len(multi_file),
                       "unresolved": sum(len(x) for x in unresolved.values()), "cross_file": sum(len(x) for x in cross.values())}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir")
    ap.add_argument("--out", required=True)
    ap.add_argument("--summary")
    a = ap.parse_args()
    res = {"schema": "manifest/1", "files": {}}
    for f in FILES:
        p = os.path.join(a.dir, f)
        if os.path.exists(p):
            res["files"][f] = extract(p, f)
    res["suite"] = suite_registry(res)
    json.dump(res, open(a.out, "w"), indent=1, sort_keys=True, ensure_ascii=False)
    if a.summary:
        cats = sorted({c for v in res["files"].values() for c in v["counts"]})
        short = {"Curriculum.md": "Curr", "system-design-primer-companion.md": "Primer", "sql-databases-companion.md": "SQL",
                 "design-patterns-companion.md": "DP", "cloud-cybersecurity-companion.md": "Cyber",
                 "session-progress-ledger.md": "Ledger", "learn-SKILL.md": "Skill", "go-language-companion.md": "Go", "fde-companion.md": "FDE"}
        fs = list(res["files"])
        o = ["# Manifest summary", "", f"Generated by `refactor-tools/manifest.py` from `{os.path.basename(os.path.abspath(a.dir))}/`.", "",
             "| Category | " + " | ".join(short[f] for f in fs) + " |", "|---|" + "---:|" * len(fs)]
        for c in cats:
            o.append(f"| {c} | " + " | ".join(str(res['files'][f]['counts'].get(c, '')) for f in fs) + " |")
        o += ["", "## Label lines by label (companions)", ""]
        for f in fs:
            lb = res["files"][f]["labels_by_name"]
            if lb:
                o.append(f"- **{short[f]}**: " + " · ".join(f"{k} {v}" for k, v in lb.items()))
        su = res["suite"]
        o += ["", "## Suite registry", "", "Counts: " + " · ".join(f"{k} {v}" for k, v in su["counts"].items()), "",
              "**Primary-definition collisions** (same token defined as a heading/bold lead/module in more than one file; §5 renames target these):", ""]
        fam = {}
        for t, d in su["collisions_primary"].items():
            key = re.sub(r"\d+(\.\d+)?[a-c]?$", "n", t) + " : " + " + ".join(short[g] for g in sorted(d))
            fam.setdefault(key, []).append(t)
        for k, v in sorted(fam.items()):
            o.append(f"- `{k}` — {len(v)} tokens ({v[0]} … {v[-1]})")
        o += ["", "**Unresolved references** (referenced, defined nowhere in the suite):", ""]
        for f, u in su["unresolved_refs"].items():
            o.append(f"- **{short[f]}**: " + ", ".join(f"`{t}` (L{','.join(map(str, ls[:4]))})" for t, ls in sorted(u.items())))
        o += ["", "## File hashes", "", "| File | Lines | SHA-256 |", "|---|---:|---|"]
        for f in fs:
            o.append(f"| {f} | {res['files'][f]['line_count']} | `{res['files'][f]['sha256']}` |")
        open(a.summary, "w").write("\n".join(o) + "\n")
    print(" ".join(f"{f.split('-')[0].split('.')[0]}:{v['counts']['lines']}L/{v['counts']['ids_distinct']}ids" for f, v in res["files"].items()))


if __name__ == "__main__":
    main()
