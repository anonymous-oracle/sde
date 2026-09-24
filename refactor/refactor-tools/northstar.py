"""R2: build the `northstar-reference-app.md` skeleton (C-03, C-05…C-07, §6.3).

Every `Nx.y` referenced by a work/ file gets a section whose meaning is the heading of the same-numbered section in
the old parent `gcp-curriculum.md` (cited by line). Nothing is authored here: each section is a stub for R9, which
may port the original (decision D1) or reconstruct it (C-07 label). Deterministic: sections and "referenced by"
lists are sorted.
"""
import os
import re
import sys

N_RE = re.compile(r"(?<![\w.-])(N\d{1,2}[bc]?(?:\.(?:\d{1,2}|C|x))*)(?![\w])")
SCAN = ["Curriculum.md", "system-design-primer-companion.md", "sql-databases-companion.md",
        "design-patterns-companion.md", "cloud-cybersecurity-companion.md"]
SHORT = {"Curriculum.md": "Curriculum", "system-design-primer-companion.md": "primer",
         "sql-databases-companion.md": "SQL", "design-patterns-companion.md": "patterns",
         "cloud-cybersecurity-companion.md": "cyber"}
PARTS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "9b", "9c", "10", "11", "11b", "12"]
HEAD_ID = re.compile(r"^#{2,4} (?:[A-Z]{2,4}(?:-S)?-\d{2}|SEC-E[\d.]+|SQL-E[\d.]+|SEC-Z0\.\d+|SQL-Z0\.\d+|SCH-\d|"
                     r"TX-\d|PX-\d+|BH-\d|DT-\d|DB-\d+|SEC-CAP\d|SQL-CAP\d|CR-E\d+)\b")


def refs(work):
    out = {}
    for f in SCAN:
        L = open(os.path.join(work, f), encoding="utf-8").read().split("\n")
        cut = next((i for i, l in enumerate(L) if l.startswith("## Pre-refactor text archive")), len(L))
        cur = "§0–§2"
        for l in L[:cut]:
            m = HEAD_ID.match(l)
            if m:
                cur = m.group(0).lstrip("# ").strip()
            elif re.match(r"^#{2,3} ", l):
                cur = re.sub(r"^#+ ", "", l).split(" — ")[0].split(" · ")[0].split(" (")[0][:48]
            for t in N_RE.findall(l):
                out.setdefault(t, set()).add(f"{SHORT[f]} {cur}")
    return out


def parent_headings(parent):
    """parts: '## Part k — title' (or '### Part 11b — …'); sections: '### x.y title' with a dot in the number"""
    L = open(parent, encoding="utf-8").read().split("\n")
    h = {}
    for i, l in enumerate(L, 1):
        m = (re.match(r"^#{2,3} Part (\d{1,2}[bc]?) — (.*)$", l)
             or re.match(r"^#{3,5} (\d{1,2}[bc]?(?:\.(?:\d{1,2}|C))+) (.*)$", l))
        if m and m.group(1) not in h:
            h[m.group(1)] = (m.group(2).strip(" —"), i)
    return h


def skey(s):
    return [(0, int(x), "") if x.isdigit() else (1, 0, x) for x in re.findall(r"\d+|[a-zA-Z]+", s)]


def build(root):
    work = os.path.join(root, "work")
    parent = os.path.join(root, "..", "gcp-curriculum.md")
    R = refs(work)
    H = parent_headings(parent)
    ids = {k for k in R if not k.endswith(".x")}
    ids |= {"N" + p for p in PARTS} | {f"N8.1.{k}" for k in range(1, 7)}
    out = [
        "# Northstar Reference Application (Track N)", "",
        "*Skeleton created by the curriculum refactor on 2026-09-24 (R2; C-03, C-05, C-06, C-07, §6.3). R9 authors "
        "it.* Northstar is the one running reference application every file builds on: storefront, customer API, "
        "admin, service-to-service, data, CI/CD and AI-gateway planes (the cybersecurity companion's Appendix N "
        "sketches its threat model). `Curriculum` owns order and cert timing; this file will own the concrete build, "
        "milestone by milestone.", "",
        "**How the sections were numbered.** The companions were written against an older parent, "
        "`gcp-curriculum.md`, and cite its numbered sections. Each such section `x.y` becomes `Nx.y` here, with the "
        "same meaning (C-03, §6.3). The meaning line quotes that section's heading and line in `gcp-curriculum.md`. "
        "Under decision D1, R9 may port the original text with a `Source material:` line, or reconstruct it; a "
        "reconstructed section is labelled `[reconstructed from companion references]` (C-07). Every section below is "
        "still a **stub**: nothing in this file is teaching content yet.", "",
        "**Rules carried into R9.** Each milestone that changes the deployed architecture cites the primer P08 ladder "
        "step it realizes and reuses the primer's Terraform exercise by ID (TF-1…TF-7), never a copy (C-32). Each "
        "milestone lists its companion stitches, its Lab Reality budget, its acceptance evidence and the S2-format "
        "documents it produces (§9.4).", "",
        "Wildcard references (`N2.x`, `N3.x`, `N5.x`, `N6.x`) resolve to the milestone of the same number.", ""]
    parts = sorted({i for i in ids if re.fullmatch(r"N\d{1,2}[bc]?", i)}, key=skey)
    for p in parts:
        key = p[1:]
        title, line = H.get(key, (None, None))
        out.append(f"## {p} · {title or '[stub — meaning unknown]'}")
        out.append("")
        src = f"`gcp-curriculum.md`:{line} (Part {key})" if line else "no same-numbered part in `gcp-curriculum.md`"
        out.append(f"- **Meaning:** {src}.")
        rb = sorted(R.get(p, set()) | R.get(p + ".x", set()))
        out.append("- **Referenced by:** " + ("; ".join(rb) if rb else "— (milestone container)"))
        out.append("- **Status:** [stub — authored in R9]")
        out.append("")
        subs = sorted([i for i in ids if i.startswith(p + ".") and re.fullmatch(re.escape(p) + r"\.[\dC]+(?:\.\d+)?", i)],
                      key=skey)
        for s in subs:
            key = s[1:]
            t, ln = H.get(key, (None, None))
            out.append(f"### {s} · {t or '[stub — meaning unknown; referenced by the IDs below]'}")
            out.append("")
            out.append(f"- **Meaning:** " + (f"`gcp-curriculum.md`:{ln} (§{key})." if ln else
                                             "not found in `gcp-curriculum.md`; listed as an open question."))
            rb = sorted(R.get(s, set()))
            out.append("- **Referenced by:** " + ("; ".join(rb) if rb else "— (named by C-06)"))
            out.append("- **Status:** [stub — authored in R9]")
            out.append("")
    missing = sorted(i for i in ids if not any(l.startswith(f"## {i} · ") or l.startswith(f"### {i} · ") for l in out))
    assert not missing, missing
    open(os.path.join(work, "northstar-reference-app.md"), "w", encoding="utf-8").write("\n".join(out))
    return sorted(ids, key=skey)


if __name__ == "__main__":
    print(len(build(os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else "."))))
