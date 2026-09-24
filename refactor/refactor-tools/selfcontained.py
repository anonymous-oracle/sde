#!/usr/bin/env python3
"""Self-containment probe for the five course files (learner decisions D5, D6, D10, D11; R2b gate, R3 hard gate).

A course file passes when its text (the whole file; after R2b there is no archive section) has:
  V1 no file names — `name.ext` tokens for course, tooling or data files. Allowed only: a name that the same file
     defines itself (a heading or bold "File `name`" line above an embedded code block, one intro line allowed), and the
     learner-created artefact names in ALLOWED_NAMES (concept names such as robots.txt, or files a lab step tells
     the learner to create). The allow-list is printed in the report so it stays visible.
  V2 no links to files — markdown links whose target is not an in-page anchor. The CC BY 4.0 attribution link in
     the primer is the one exception (license requirement).
  V3 no Northstar / Track N / `N…` section IDs (D5).
  V4 no file-style parent name (`Curriculum` in backticks, "Curriculum.md") (D11).
  V5 no refactor bookkeeping in course text: provenance lines, "(was …)" notes, refactor notes, conflict IDs
     (C-nn), the D3 archive, names of refactor artefacts (crosswalk, errata, binding table, ledger file, skill file).
  V6 no pointers to the legacy course or other outside files by name (gcp-curriculum, unified-curriculum, …),
     including the legacy course named in prose ("gcp owns …", gcp "Section", "the old parent") and its bare
     section numbers after a pointing word ("from 7.2", "before 6.15", "lab 6.14").
  V3 (Northstar), V4 and V6 also apply inside code blocks: an embedded lab kit is course material too.

Usage: selfcontained.py ROOT [--verbose]   → exit 1 on any violation.
"""
import os
import re
import sys

FILES = ["Curriculum.md", "system-design-primer-companion.md", "sql-databases-companion.md",
         "design-patterns-companion.md", "cloud-cybersecurity-companion.md"]

EXT = r"(?:md|py|sql|json|jsonl|txt|sh|tgz|csv|ya?ml|tf|go|pdf|proto|ipynb|toml|ini|cfg|log|out)"
FILE_RE = re.compile(r"(?<![\w@])((?:[\w-]+/)*[\w.-]*[A-Za-z0-9_]\." + EXT + r")\b")

# learner-created artefacts and concept names (not references to outside material); reason in the value
ALLOWED_NAMES = {
    "robots.txt": "web crawling concept (the robots exclusion file), not a course file",
    "main.tf": "the Terraform file a lab tells the learner to write",
    "variables.tf": "the Terraform file a lab tells the learner to write",
    "outputs.tf": "the Terraform file a lab tells the learner to write",
    "go.mod": "Go module file the learner creates",
    "requirements.txt": "Python dependency file the learner creates",
    "docker-compose.yml": "Compose file the learner creates",
    "docker-compose.yaml": "Compose file the learner creates",
    "Dockerfile": "container build file the learner creates",
    "attestation.json": "the file the learner's attestation toy writes (WL-04 build lab)",
    "001_init.sql": "example migration file name the learner writes (DD-11 / OD-08 build lab)",
    "002_add_column.sql": "example migration file name the learner writes (OD-08 build lab)",
    "service.proto": "example protobuf file name the learner writes",
    "user.proto": "example protobuf file name the learner writes",
    "schema.proto": "example protobuf file name the learner writes",
    "audit.sh": "SQL table reference (schema audit, table sh) in a query, not a file",
}

LEGACY = re.compile(r"gcp-curriculum|unified-curriculum|northstar-reference|learn-SKILL|session-progress-ledger|"
                    r"cert-verification|primer-binding-table|crosswalk|errata\.md|volatility-register|"
                    r"requirements-hardening|refactor-state|semantic-unified|appendix-r-build|CHANGELOG|"
                    r"\bgcp owns\b|old parent|\bgcp \"|"
                    r"\b(?:from|before|per|lab|checklist) [3-9]\.(?:\d{1,2}|x)\b(?!\.\d|\d| ?(?:s|ms|%|GB|MB)\b)|"
                    r"\| [3-9]\.[0-9x]/[3-9]\.[0-9x]",
                    re.I)
NREF = re.compile(r"(?<![\w-])N(?:\d+(?:\.\d+)*[a-z]?|\d+\.[A-Z]|\d+[a-c])(?![\w-])")
NORTH = re.compile(r"northstar|Track N\b", re.I)
CURBT = re.compile(r"`Curriculum`|Curriculum\.md")
BOOK = [("provenance line", re.compile(r"\*\*Provenance\*\*|\*Provenance[ (]|^\s*-?\s*\*?Provenance")),
        ("(was …) note", re.compile(r"\*?\(was [`'\"A-Za-z0-9]")),
        ("refactor note", re.compile(r"Refactor note|Refactor-authored|refactor-authored|Ported by the refactor|"
                                     r"Added by the refactor|added by the refactor|Source material:")),
        ("conflict ID", re.compile(r"(?<![\w-])C-(?:\d{2}|NEW-\d{2})(?![\w-])")),
        ("D3 archive", re.compile(r"Pre-refactor text archive|D3 archive|\bD3-\d{2}\b")),
        ("refactor word", re.compile(r"\brefactor(?:ed|ing)?\b", re.I))]
MDLINK = re.compile(r"\[[^\]]*\]\((?!#)([^)]+)\)")
LINK_OK = {"https://github.com/donnemartin/system-design-primer"}


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


def defined_names(lines):
    """names the file defines itself: a heading or a bold File line naming it, followed by a code fence (at most one
    intro line between them)"""
    out = set()
    for i, l in enumerate(lines):
        m = re.match(r"^(?:#{3,6} .*?|\*\*File\*?\*? )`([^`]+)`", l)
        if m:
            nxt = [x for x in lines[i + 1:i + 6] if x.strip()][:2]   # at most one intro line before the fence
            if any(x.lstrip().startswith("```") for x in nxt) and not any(x.startswith("#") for x in nxt):
                out.add(m.group(1).split("/")[-1])
                out.add(m.group(1))
    return out


def probe(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    mask = fence_mask(lines)
    own = defined_names(lines)
    v = []
    for n, l in enumerate(lines, 1):
        fenced = mask[n - 1]
        for m in FILE_RE.finditer(l):
            name = m.group(1)
            base = name.split("/")[-1]
            if base in own or name in own or base in ALLOWED_NAMES:
                continue
            if re.match(r"^\d+(\.\d+)+$", name.rsplit(".", 1)[0]):  # version-like numbers, e.g. 1.2.md never
                continue
            v.append(("V1 file name", n, name, l))
        for m in MDLINK.finditer(l):
            if m.group(1) not in LINK_OK and not fenced:
                v.append(("V2 link", n, m.group(1), l))
        for m in NORTH.finditer(l):          # V3 Northstar, V4, V6 also inside code blocks: embedded kit text is
            v.append(("V3 Northstar", n, m.group(0), l))          # course material too
        for m in CURBT.finditer(l):
            v.append(("V4 file-style parent name", n, m.group(0), l))
        for m in LEGACY.finditer(l):
            v.append(("V6 outside file", n, m.group(0), l))
        if fenced:
            continue
        for m in NREF.finditer(l):
            v.append(("V3 N-section ID", n, m.group(0), l))
        for name, rx in BOOK:
            for m in rx.finditer(l):
                v.append(("V5 " + name, n, m.group(0), l))
    return v


def main():
    root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else ".")
    verbose = "--verbose" in sys.argv
    total = 0
    for f in FILES:
        v = probe(os.path.join(root, "work", f))
        total += len(v)
        kinds = {}
        for k, *_ in v:
            kinds[k] = kinds.get(k, 0) + 1
        print(f"{'PASS' if not v else 'FAIL'} {f}: {len(v)} violation(s)"
              + (" — " + ", ".join(f"{k} ×{c}" for k, c in sorted(kinds.items())) if v else ""))
        if verbose:
            for k, n, tok, l in v:
                print(f"    L{n} [{k}] {tok!r}: {l[:160]}")
    print("allow-listed names (V1):", ", ".join(sorted(ALLOWED_NAMES)))
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
