#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build self-contained copies of the full-build pack (v2).

Fix vs v1: compact meta has no evidence-files section, so that rewrite
is skipped when the heading is absent. Writes only NEW files under
builds/full/selfcontained/. Never modifies or deletes existing pack files.
"""
from __future__ import print_function

import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

FULL = Path("/Users/suhas/sde/nptel/builds/full")
CURRICULUM = Path("/Users/suhas/sde/nptel/unified_cloud_curriculum.md")
OUT = FULL / "selfcontained"

ORIGINAL_NAMES = [
    "topics.md",
    "meta_rules_and_index.md",
    "topics_sorted.md",
    "meta_rules_and_index_sorted.md",
    "topics_sorted_compact.md",
    "meta_rules_and_index_sorted_compact.md",
]

TOPIC_RE = re.compile(r"^- (.+) \[([^\]]+)\] —")
T_PTR_RE = re.compile(r"T@L(\d+)-(\d+)")
A_PTR_RE = re.compile(r"A:([A-Za-z0-9.]+)@L(\d+)-(\d+)")
COMPACT_ID_RE = re.compile(r"^([0-9a-z]+) (.+)$")
LEVEL_LETTER = {
    "HS": "H",
    "UG": "U",
    "UG+PG": "J",
    "PG-only": "P",
    "industry": "I",
    "level-unknown": "?",
}
FILEISH_RE = re.compile(r"\.md|\.json|\.tsv|/Users/")
ALLOWED_META_NOTE = (
    "Self-contained: this pair needs no other files except "
    "Master_Rules.md and learn-SKILL.md."
)

LINE18 = (
    "- T/A pointers in topics.md refer to existing source lines, not embedded "
    "lessons. These two pack files do not contain the original questions, keys "
    "or proofs. A local Mac path is not automatically readable inside Claude: "
    "obtain the unchanged source/map upload before claiming to inspect or reuse "
    "it. If unavailable, say so; never pretend it was read."
)
LINE17 = (
    "- Look up the topic/unit in teaching_assignments_map.md/.json. Reuse "
    "existing Topics, Results, Build, Gap-fills, proof-tagged items and "
    "assignments from their exact source references; preserve proof status, "
    "uncertainty and ownership. Do not redo complete content. A lexical link "
    "is not proof of full teaching or assessment scope."
)


def sha256_file(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_lines(path):
    data = path.read_bytes()
    if b"\r\n" in data:
        raise SystemExit("unexpected CRLF in %s" % path)
    text = data.decode("utf-8")
    if not text.endswith("\n"):
        raise SystemExit("expected trailing newline in %s" % path)
    return text.splitlines()


def join_lines(lines):
    return "\n".join(lines) + "\n"


def must_replace(s, old, new, where):
    if old not in s:
        raise SystemExit("expected string not found in %s:\n%s" % (where, old[:200]))
    return s.replace(old, new)


def extract_detailed_topics(lines):
    out = []
    for i, line in enumerate(lines, 1):
        if line.startswith("# Embedded curriculum text"):
            break
        m = TOPIC_RE.match(line)
        if m:
            out.append((i, m.group(1), m.group(2), line))
    return out


def extract_compact_topics(lines):
    out = []
    level = None
    in_appendix = False
    for i, line in enumerate(lines, 1):
        if line.startswith("# Embedded curriculum text"):
            in_appendix = True
            break
        if line.startswith("## Level:"):
            level = line.split(":", 1)[1].strip()
            continue
        if i <= 6 or line.startswith("#") or line.startswith("Level legend") or not line.strip():
            continue
        m = COMPACT_ID_RE.match(line)
        if not m:
            raise SystemExit("unparsed compact topic line %d: %s" % (i, line[:200]))
        out.append((i, m.group(1), m.group(2), level, line))
    return out


def block_lines(curr, start, end):
    if start < 1 or end > len(curr) or start > end:
        raise SystemExit("invalid curriculum range L%s-%s (file has %d lines)" % (start, end, len(curr)))
    return curr[start - 1:end]


def build_t_labels(ranges):
    labels = {}
    inv = {}
    for i, rng in enumerate(sorted(ranges, key=lambda x: (x[0], x[1])), 1):
        lab = "T%04d" % i
        labels[rng] = lab
        inv[lab] = rng
    return labels, inv


def rewrite_topics_header_original(lines):
    lines = list(lines)
    if lines[0] != "# Prerequisite-ordered topics by unit":
        raise SystemExit("unexpected topics.md title: %r" % lines[0])
    lines[2] = (
        "Full pack. Topic names/IDs come only from installed graph nodes. "
        "Source-derived levels remain level-unknown where unsupported. "
        "Within-unit topic order follows the checked DAG; unresolved "
        "cross-unit conflicts are disclosed in the pack-specific order audit."
    )
    lines[4] = (
        "Evidence: g = exact graph node ID; c = observed course count; src = existing "
        "graph source key; SDP/CBSE identify the downloaded source line. T: and A: "
        "labels point to curriculum text embedded at the end of this file. They are "
        "not guarantees of complete teaching/assessment scope."
    )
    return lines


def rewrite_topics_header_sorted(lines):
    lines = list(lines)
    if lines[0] != "# Full graph topics: domain → level → DAG":
        raise SystemExit("unexpected topics_sorted.md title: %r" % lines[0])
    lines[2] = (
        "36,628 graph topics, each exactly once. Every topic line below keeps its "
        "graph ID, level and source pointers. T: and A: labels point to curriculum "
        "text embedded at the end of this file. The active order and every "
        "reversed-edge audit record are in this pack's meta-rules."
    )
    lines[4] = (
        "T: and A: labels identify teaching and assignment text embedded below in "
        "this file. Original units split into .pN segments only when required to "
        "preserve DAG order within a domain/level band; original titles and IDs "
        "remain traceable."
    )
    # line 6 (index 6) noise paragraph stays verbatim
    return lines


def rewrite_topics_header_compact(lines):
    lines = list(lines)
    if lines[0] != "# Full topics: compact domain → level → DAG":
        raise SystemExit("unexpected topics_sorted_compact.md title: %r" % lines[0])
    lines[2] = (
        "36,628 topics, exact names/levels/order retained. Each base-36 short ID is "
        "its 1-based position, not a graph ID. Level is inherited from the enclosing "
        "header. Teaching and assignment text used by these topics is embedded at "
        "the end of this file, keyed by short ID. Noise IDs in this pack's "
        "meta-rules remain reconciliation-only."
    )
    return lines


def replace_pointers(line, t_labels):
    def t_sub(m):
        rng = (int(m.group(1)), int(m.group(2)))
        if rng not in t_labels:
            raise SystemExit("unmapped T range %s" % (rng,))
        return "T:" + t_labels[rng]

    def a_sub(m):
        return "A:" + m.group(1)

    line = T_PTR_RE.sub(t_sub, line)
    line = A_PTR_RE.sub(a_sub, line)
    return line


def appendix_header():
    return [
        "# Embedded curriculum text",
        "",
        "Each block below is copied verbatim from the original teaching source. "
        "A T: or A: label on a topic line in this file refers to the block with "
        "the same heading here. A lexical link is not a guarantee of complete "
        "teaching or assessment scope.",
        "",
    ]


def appendix_header_compact():
    return [
        "# Embedded curriculum text",
        "",
        "Each block below is copied verbatim from the original teaching source. "
        "The short IDs listed after Used by: are the compact topic IDs in this "
        "file that use the block. A lexical link is not a guarantee of complete "
        "teaching or assessment scope.",
        "",
    ]


def emit_blocks(section_title, items, used_by=None):
    """items: list of (label, source_lines). used_by: optional label -> [short ids]."""
    out = [section_title, ""]
    for label, src_lines in items:
        out.append("### " + label)
        out.append("")
        if used_by is not None:
            ids = used_by.get(label, [])
            out.append("Used by: " + (", ".join(ids) if ids else "(none)"))
            out.append("")
        out.extend(src_lines)
        if not src_lines or src_lines[-1] != "":
            out.append("")
    return out


def line17_for(kind, sibling):
    if kind == "compact":
        return (
            "- Look up the topic's short ID in the embedded curriculum appendix of "
            "%s. Reuse existing Topics, Results, Build, Gap-fills, proof-tagged "
            "items and assignments from the blocks listed for that short ID; "
            "preserve proof status, uncertainty and ownership. Do not redo complete "
            "content. A lexical link is not proof of full teaching or assessment scope."
            % sibling
        )
    return (
        "- Look up the topic in %s. Reuse existing Topics, Results, Build, "
        "Gap-fills, proof-tagged items and assignments from the embedded curriculum "
        "text in that file (T: and A: labels); preserve proof status, uncertainty "
        "and ownership. Do not redo complete content. A lexical link is not proof "
        "of full teaching or assessment scope."
        % sibling
    )


def line18_for(kind, sibling):
    if kind == "compact":
        return (
            "- Teaching and assignment excerpts are embedded in the appendix of "
            "%s, keyed by the topic's compact short ID. Reuse that verbatim text "
            "(questions, keys and proofs included where present). If a short ID is "
            "not listed on any appendix block, no extracted teaching or assignment "
            "text is present for it. Never pretend to have read text that is not in "
            "this pair."
            % sibling
        )
    return (
        "- T: and A: labels in %s refer to curriculum text embedded in that same "
        "file, not to an external source. Reuse that verbatim text (questions, keys "
        "and proofs included where present). If a topic has no T: or A: label, no "
        "extracted teaching or assignment text is present for it. Never pretend to "
        "have read text that is not in this pair."
        % sibling
    )


def rewrite_evidence_lines(lines):
    """Rewrite the evidence-files registry in place; may change line count."""
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line == "### Evidence files and source registry":
            out.append(line)
            i += 1
            # consume original registry bullets until a blank line followed by
            # something that is not a continuation, or until unit-index heading.
            # We rebuild the registry from the original bullets we see.
            seen_graph = False
            while i < len(lines):
                L = lines[i]
                if L.startswith("# ") or L.startswith("# Unit"):
                    break
                if L.startswith("- `/Users/suhas/sde/ocw-courses/uglists/graph/unified_graph.json`"):
                    if not seen_graph:
                        out.append(
                            "- Derived from the project's topic graph. Graph-file "
                            "paths are not required to use this pack."
                        )
                        out.append(
                            "- Teaching and assignment excerpts used here are "
                            "embedded verbatim in the sibling topics file of this pair."
                        )
                        seen_graph = True
                    i += 1
                    continue
                if L.startswith("- `/Users/suhas/sde/ocw-courses/uglists/graph/topic_levels_expanded.tsv`"):
                    i += 1
                    continue
                if L.startswith("- `/Users/suhas/sde/ocw-courses/recovery/curriculum/rebuild_full/teaching_assignments_map.md`"):
                    i += 1
                    continue
                if L.startswith("- `/Users/suhas/sde/ocw-courses/recovery/curriculum/rebuild_full/teaching_assignments_map.json`"):
                    i += 1
                    continue
                if L.startswith("- `/Users/suhas/sde/nptel/unified_cloud_curriculum.md`"):
                    i += 1
                    continue
                if L.startswith("- Teaching-source SHA256:"):
                    out.append(
                        "- Teaching-source SHA256: `0a81c35c21c3a8343764ccd8f443933fc0db88aab51c6282318751cd5318e6a9`; "
                        "the embedded curriculum text was copied verbatim from that unchanged source."
                    )
                    i += 1
                    continue
                if L.startswith("- Rules input `/Users/suhas/sde/Master_Rules.md`"):
                    out.append(
                        "- Rules input Master_Rules.md; SHA256 `1d5d63e06317a7c35ca6e050595f16a7670a72979c2773d68b00145eb1372865`."
                    )
                    i += 1
                    continue
                if L.startswith("- Rules input `/Users/suhas/sde/learn-SKILL.md`"):
                    out.append(
                        "- Rules input learn-SKILL.md; SHA256 `d794cc09183d2e0a25904a03ee24b4ce14db30ef609fbc9a123d192b8f91c83c`."
                    )
                    i += 1
                    continue
                if L == "- https://github.com/donnemartin/system-design-primer/blob/master/README.md":
                    # Drop the README.md path segment so this pack has no extra .md file name.
                    out.append("- https://github.com/donnemartin/system-design-primer")
                    i += 1
                    continue
                if L.startswith("- Sorted-build graph copy actually read:"):
                    out.append(
                        "- The sorted build was derived from the project's topic graph; "
                        "no graph file was changed."
                    )
                    i += 1
                    continue
                # CBSE URLs, blank lines, or anything else in the registry
                out.append(L)
                i += 1
                if L == "" and i < len(lines) and lines[i].startswith("#"):
                    break
            continue
        out.append(line)
        i += 1
    if not any(L.startswith("- Derived from the project's topic graph.") for L in out):
        raise SystemExit("evidence-section rewrite did not emit the generic graph line")
    return out


def rewrite_meta(lines, sibling, kind):
    text_lines = list(lines)
    joined = join_lines(text_lines)

    # required exact originals must be present
    joined = must_replace(
        joined,
        "Tags come from the graph's topic_levels_expanded.tsv;",
        "Tags come from the project's topic graph;",
        "rule 1",
    )
    joined = must_replace(joined, LINE17, line17_for(kind, sibling), "rule 3 lookup")
    joined = must_replace(joined, LINE18, line18_for(kind, sibling), "rule 3 pointers")

    if kind in ("sorted", "compact"):
        if kind == "sorted":
            new_use = sibling
        else:
            new_use = sibling
        joined = must_replace(
            joined,
            "For this sorted edition use topics_sorted.md and this regenerated index:",
            "For this sorted edition use %s and this regenerated index:" % new_use,
            "rule 9",
        )
        joined = must_replace(
            joined,
            "Original topic-line T/A pointers retain their original source meaning.",
            "Original topic-line T: and A: labels refer to embedded curriculum text in the sibling topics file.",
            "rule 9 T/A",
        )
        joined = must_replace(
            joined,
            "Update learner_record.md:",
            "Update the learner's progress record, if provided:",
            "rule 10",
        )

    if kind == "sorted":
        joined = must_replace(
            joined,
            "the existing topological_node_order.json rank is used",
            "the existing graph topological rank is used",
            "topo rank",
        )
        joined = must_replace(
            joined,
            "# Unit index (same order as topics_sorted.md)",
            "# Unit index (same order as %s)" % sibling,
            "unit index heading",
        )
        joined = must_replace(
            joined,
            "topics_sorted.md:L",
            "%s:L" % sibling,
            "unit index line refs",
        )
        old_audit = (
            "Every record below is a reversed typed graph relation: the "
            "prerequisite/source (later line) → dependent/target (earlier line). "
            "L means the exact topic line in topics_sorted.md, which contains its "
            "unchanged g: graph ID. Dn is 1-based edges[n-1] in graph/dag_view.json; "
            "Gn is edges[n-1] in graph/unified_graph.json (explicit ext_prereq only). "
            "Shared D/G records are one relation, with both original edge positions. "
            "Domain/level is found in the topic line and enclosing headers. Reasons: "
            "domain, level, or same-band/non-DAG. Source/lecture order, taxonomy and "
            "containment edges are audited for ordering but are not automatically "
            "academic prerequisites. Validate before invoking the just-in-time teaching bridge."
        )
        new_audit = (
            "Every record below is a reversed typed graph relation: the "
            "prerequisite/source (later line) → dependent/target (earlier line). "
            "L means the exact topic line in %s, which contains its unchanged g: "
            "graph ID. Dn and Gn are 1-based edge registry indices from the project's "
            "topic graph (Gn: explicit ext_prereq only). Shared D/G records are one "
            "relation, with both original edge positions. Domain/level is found in the "
            "topic line and enclosing headers. Reasons: domain, level, or "
            "same-band/non-DAG. Source/lecture order, taxonomy and containment edges "
            "are audited for ordering but are not automatically academic prerequisites. "
            "Validate before invoking the just-in-time teaching bridge."
            % sibling
        )
        joined = must_replace(joined, old_audit, new_audit, "audit intro")

    if kind == "compact":
        old_bind = (
            "- In this edition rule 9 selects topics_sorted_compact.md and the index "
            "below. Short IDs are base-36 1-based topic positions, not graph IDs or "
            "source line numbers. Original T/A/source evidence is omitted, not moved; "
            "rules 3 and 7 still forbid claiming inaccessible sources were read."
        )
        new_bind = (
            "- In this edition rule 9 selects %s and the index below. Short IDs are "
            "base-36 1-based topic positions, not graph IDs or source line numbers. "
            "Teaching and assignment text is embedded in the appendix of that sibling "
            "topics file, keyed by short ID; rules 3 and 7 still forbid claiming text "
            "that is not present was read."
            % sibling
        )
        joined = must_replace(joined, old_bind, new_bind, "compact binding")

    if kind == "original":
        joined = must_replace(
            joined,
            "# Unit index (same order as topics.md)",
            "# Unit index (same order as %s)" % sibling,
            "original unit index heading",
        )

    out_lines = joined.splitlines()
    if any(L == "### Evidence files and source registry" for L in out_lines):
        out_lines = rewrite_evidence_lines(out_lines)
    # one-line note at top
    if out_lines[0] != "# Meta-rules for teaching from the topic list":
        raise SystemExit("unexpected meta title after rewrite: %r" % out_lines[0][:120])
    out_lines = [ALLOWED_META_NOTE, ""] + out_lines
    return out_lines


def parse_appendix(lines):
    """Return dict label -> list of source lines (verbatim block)."""
    blocks = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("### ") and (line.startswith("### T") or line.startswith("### A")):
            label = line[4:].strip()
            i += 1
            if i < len(lines) and lines[i] == "":
                i += 1
            # optional Used by line
            if i < len(lines) and lines[i].startswith("Used by:"):
                i += 1
                if i < len(lines) and lines[i] == "":
                    i += 1
            start = i
            while i < len(lines) and not (lines[i].startswith("### ") or lines[i].startswith("## ") or lines[i].startswith("# ")):
                i += 1
            blk = lines[start:i]
            # drop one trailing separator blank if present AND the next thing is a heading
            # We will compare against known expected length later; keep raw here.
            blocks[label] = blk
            continue
        i += 1
    return blocks


def trim_trailing_blank(blk):
    if blk and blk[-1] == "":
        return blk[:-1]
    return blk


def fileish_hits(text, allowed):
    hits = []
    for i, line in enumerate(text.splitlines(), 1):
        if not FILEISH_RE.search(line):
            continue
        # report leftover mentions that are not an allowed filename context
        # Allowed if every match is one of the allowed names, and no /Users/
        leftover = line
        if "/Users/" in leftover:
            hits.append((i, line))
            continue
        cleaned = leftover
        for name in allowed:
            cleaned = cleaned.replace(name, "")
        if FILEISH_RE.search(cleaned):
            hits.append((i, line))
    return hits


def write_new(path, text):
    if path.exists():
        raise SystemExit("refusing to overwrite existing file: %s" % path)
    path.write_text(text, encoding="utf-8")
    if sha256_file(path) != hashlib.sha256(text.encode("utf-8")).hexdigest():
        raise SystemExit("write mismatch: %s" % path)


def main():
    report = {
        "issues": [],
        "checks": {},
    }
    original_sha_before = {name: sha256_file(FULL / name) for name in ORIGINAL_NAMES}
    report["original_sha256_before"] = original_sha_before

    curr = read_lines(CURRICULUM)
    topics_md = read_lines(FULL / "topics.md")
    topics_sorted = read_lines(FULL / "topics_sorted.md")
    topics_compact = read_lines(FULL / "topics_sorted_compact.md")
    meta_orig = read_lines(FULL / "meta_rules_and_index.md")
    meta_sorted = read_lines(FULL / "meta_rules_and_index_sorted.md")
    meta_compact = read_lines(FULL / "meta_rules_and_index_sorted_compact.md")

    # Collect pointers from topics.md (same set as topics_sorted.md)
    t_ranges = set()
    a_map = {}
    for line in topics_md:
        for a, b in T_PTR_RE.findall(line):
            t_ranges.add((int(a), int(b)))
        for aid, a, b in A_PTR_RE.findall(line):
            rng = (int(a), int(b))
            if aid in a_map and a_map[aid] != rng:
                raise SystemExit("assignment %s has multiple ranges" % aid)
            a_map[aid] = rng
    t_ranges_sorted = set()
    a_map_sorted = {}
    for line in topics_sorted:
        for a, b in T_PTR_RE.findall(line):
            t_ranges_sorted.add((int(a), int(b)))
        for aid, a, b in A_PTR_RE.findall(line):
            rng = (int(a), int(b))
            if aid in a_map_sorted and a_map_sorted[aid] != rng:
                raise SystemExit("sorted assignment %s has multiple ranges" % aid)
            a_map_sorted[aid] = rng
    if t_ranges != t_ranges_sorted or a_map != a_map_sorted:
        raise SystemExit("topics.md and topics_sorted.md pointer sets differ")
    if T_PTR_RE.search(join_lines(topics_compact)) or A_PTR_RE.search(join_lines(topics_compact)):
        raise SystemExit("unexpected T/A pointers in compact topics")

    t_labels, t_inv = build_t_labels(t_ranges)
    t_items = [(t_labels[rng], block_lines(curr, rng[0], rng[1])) for rng in sorted(t_ranges)]
    a_items = [(aid, block_lines(curr, a_map[aid][0], a_map[aid][1])) for aid in sorted(a_map, key=lambda x: tuple(int(p) if p.isdigit() else p for p in re.split(r"(\d+)", x)))]
    expected_block = {lab: src for lab, src in t_items}
    expected_block.update({lab: src for lab, src in a_items})

    # --- detailed topics files ---
    def transform_detailed(src_lines, header_fn):
        lines = header_fn(list(src_lines))
        if len(lines) != len(src_lines):
            raise SystemExit("header rewrite changed line count")
        out = []
        for i, line in enumerate(lines):
            if TOPIC_RE.match(line):
                out.append(replace_pointers(line, t_labels))
            else:
                # headers / unit headings / comments unchanged except the rewritten header lines
                out.append(line)
        # append appendix after original last line (plus the file's trailing newline already handled)
        if out[-1] != "":
            out.append("")
        out.extend(appendix_header())
        out.extend(emit_blocks("## Teaching blocks", t_items))
        out.extend(emit_blocks("## Assignment blocks", a_items))
        # drop a trailing extra blank if emit_blocks left one and we already end with blank
        while len(out) >= 2 and out[-1] == "" and out[-2] == "":
            out.pop()
        return out

    topics_sc = transform_detailed(topics_md, rewrite_topics_header_original)
    topics_sorted_sc = transform_detailed(topics_sorted, rewrite_topics_header_sorted)

    # --- compact: map by name/level equality ---
    src_sorted_topics = extract_detailed_topics(topics_sorted)
    src_compact_topics = extract_compact_topics(topics_compact)
    if len(src_sorted_topics) != 36628 or len(src_compact_topics) != 36628:
        raise SystemExit("source topic counts: sorted %d compact %d" % (len(src_sorted_topics), len(src_compact_topics)))
    used_by = defaultdict(list)
    for (sln, sname, slevel, sline), (cln, cid, cname, clevel, cline) in zip(src_sorted_topics, src_compact_topics):
        expect_letter = LEVEL_LETTER[slevel]
        if sname != cname or expect_letter != clevel:
            raise SystemExit(
                "compact/sorted mismatch at sorted L%d / compact L%d: %r [%s] vs %s %r [%s]"
                % (sln, cln, sname, slevel, cid, cname, clevel)
            )
        for a, b in T_PTR_RE.findall(sline):
            used_by[t_labels[(int(a), int(b))]].append(cid)
        for aid, a, b in A_PTR_RE.findall(sline):
            used_by[aid].append(cid)
    report["checks"]["compact_name_level_order_vs_sorted"] = True

    topics_compact_sc = rewrite_topics_header_compact(list(topics_compact))
    if len(topics_compact_sc) != len(topics_compact):
        raise SystemExit("compact header rewrite changed line count")
    # keep all topic lines verbatim
    if topics_compact_sc[-1] != "":
        topics_compact_sc.append("")
    topics_compact_sc.extend(appendix_header_compact())
    topics_compact_sc.extend(emit_blocks("## Teaching blocks", t_items, used_by=used_by))
    topics_compact_sc.extend(emit_blocks("## Assignment blocks", a_items, used_by=used_by))
    while len(topics_compact_sc) >= 2 and topics_compact_sc[-1] == "" and topics_compact_sc[-2] == "":
        topics_compact_sc.pop()

    meta_sc = rewrite_meta(meta_orig, "topics_sc.md", "original")
    meta_sorted_sc = rewrite_meta(meta_sorted, "topics_sorted_sc.md", "sorted")
    meta_compact_sc = rewrite_meta(meta_compact, "topics_sorted_compact_sc.md", "compact")

    outputs = {
        "topics_sc.md": join_lines(topics_sc),
        "meta_rules_and_index_sc.md": join_lines(meta_sc),
        "topics_sorted_sc.md": join_lines(topics_sorted_sc),
        "meta_rules_and_index_sorted_sc.md": join_lines(meta_sorted_sc),
        "topics_sorted_compact_sc.md": join_lines(topics_compact_sc),
        "meta_rules_and_index_sorted_compact_sc.md": join_lines(meta_compact_sc),
    }

    # ---------- verification (in memory, before write) ----------
    def check(name, ok, detail=None):
        report["checks"][name] = {"ok": bool(ok), "detail": detail}
        if not ok:
            report["issues"].append("%s: %s" % (name, detail))

    # topic counts and name/level/order
    pairs = [
        ("topics_sc.md", topics_md, "detailed"),
        ("topics_sorted_sc.md", topics_sorted, "detailed"),
        ("topics_sorted_compact_sc.md", topics_compact, "compact"),
    ]
    for out_name, src_lines, kind in pairs:
        out_lines = outputs[out_name].splitlines()
        if kind == "detailed":
            src_topics = extract_detailed_topics(src_lines)
            new_topics = extract_detailed_topics(out_lines)
            same = (
                len(new_topics) == 36628
                and len(src_topics) == 36628
                and all(
                    (a[1], a[2]) == (b[1], b[2])
                    for a, b in zip(src_topics, new_topics)
                )
            )
            # line numbers of topic rows should be unchanged (header line count preserved)
            same_lines = all(a[0] == b[0] for a, b in zip(src_topics, new_topics))
            check(
                out_name + ".topics_identical",
                same and same_lines,
                {
                    "count": len(new_topics),
                    "src_count": len(src_topics),
                    "names_levels_order": same,
                    "same_line_numbers": same_lines,
                },
            )
        else:
            src_topics = extract_compact_topics(src_lines)
            new_topics = extract_compact_topics(out_lines)
            same = (
                len(new_topics) == 36628
                and all(
                    (a[1], a[2], a[3], a[4]) == (b[1], b[2], b[3], b[4])
                    for a, b in zip(src_topics, new_topics)
                )
            )
            check(
                out_name + ".topics_identical",
                same,
                {"count": len(new_topics), "lines_and_text_unchanged": same},
            )

    # zero @L pointers in the pre-appendix portion; also scan whole file
    atL = re.compile(r"@L\d+")
    for out_name in outputs:
        text = outputs[out_name]
        # split at appendix if any
        if "\n# Embedded curriculum text\n" in text:
            pre, post = text.split("\n# Embedded curriculum text\n", 1)
        else:
            pre, post = text, ""
        pre_hits = atL.findall(pre)
        post_hits = atL.findall(post)
        check(
            out_name + ".zero_atL_pre_appendix",
            len(pre_hits) == 0,
            {"pre": len(pre_hits), "in_appendix_or_rest": len(post_hits)},
        )
        if post_hits:
            report["issues"].append(
                "%s has @L in appendix/rest (verbatim source?): %d"
                % (out_name, len(post_hits))
            )

    # every embedded block byte-identical; every used label resolves uniquely
    for out_name, kind in (
        ("topics_sc.md", "detailed"),
        ("topics_sorted_sc.md", "detailed"),
        ("topics_sorted_compact_sc.md", "compact"),
    ):
        out_lines = outputs[out_name].splitlines()
        blocks = parse_appendix(out_lines)
        # compare, allowing a single trailing separator blank
        ident = True
        mismatches = []
        for lab, expected in expected_block.items():
            if lab not in blocks:
                ident = False
                mismatches.append("missing " + lab)
                continue
            got = blocks[lab]
            if got != expected and trim_trailing_blank(got) != expected:
                ident = False
                if len(mismatches) < 8:
                    mismatches.append(
                        "%s expected %d lines got %d first=%r"
                        % (lab, len(expected), len(got), (got[0] if got else ""))
                    )
        extra = [lab for lab in blocks if lab not in expected_block]
        if extra:
            ident = False
            mismatches.append("extra labels: %s" % extra[:8])
        check(out_name + ".blocks_byte_identical", ident and not extra, mismatches or None)

        # labels used in the topic body must resolve
        used = set()
        if kind == "detailed":
            body = outputs[out_name].split("\n# Embedded curriculum text\n", 1)[0]
            used.update(re.findall(r"(?:(?<=\s)|(?<=;))T:(T\d{4})(?=\s|;|$)", body))
            used.update(re.findall(r"(?:(?<=\s)|(?<=;))A:(A\d+\.\d+)(?=\s|;|$)", body))
            # also simpler
            used = set(re.findall(r"T:(T\d{4})", body) + re.findall(r"A:(A\d+\.\d+)", body))
        else:
            # compact uses Used by lists; every expected label should be present
            used = set(expected_block)
        unresolved = sorted(u for u in used if u not in blocks)
        # uniqueness of headings already implied by parse overwrite; detect dup headings
        headings = [ln[4:].strip() for ln in out_lines if ln.startswith("### T") or ln.startswith("### A")]
        dup = sorted({h for h in headings if headings.count(h) > 1})
        check(
            out_name + ".labels_resolve",
            not unresolved and not dup and set(expected_block) <= set(blocks),
            {"unresolved": unresolved[:10], "duplicate_headings": dup, "used": len(used), "blocks": len(blocks)},
        )

    # filename-like mentions
    allowed_map = {
        "topics_sc.md": [],
        "topics_sorted_sc.md": [],
        "topics_sorted_compact_sc.md": [],
        "meta_rules_and_index_sc.md": ["Master_Rules.md", "learn-SKILL.md", "topics_sc.md"],
        "meta_rules_and_index_sorted_sc.md": ["Master_Rules.md", "learn-SKILL.md", "topics_sorted_sc.md"],
        "meta_rules_and_index_sorted_compact_sc.md": [
            "Master_Rules.md",
            "learn-SKILL.md",
            "topics_sorted_compact_sc.md",
        ],
    }
    mention_report = {}
    mentions_ok = True
    for out_name, allowed in allowed_map.items():
        hits = fileish_hits(outputs[out_name], allowed)
        mention_report[out_name] = [{"line": i, "text": t[:240]} for i, t in hits]
        if hits:
            mentions_ok = False
    check("filename_mentions_allowed_only", mentions_ok, mention_report if not mentions_ok else "clean")
    report["filename_mentions"] = mention_report

    critical_failed = [
        k for k, v in report["checks"].items()
        if isinstance(v, dict) and not v.get("ok", True)
    ]
    report["critical_failed"] = critical_failed

    # Filename-mention leftovers are recorded but do not block the write;
    # identity, pointer, and block checks do.
    hard = [k for k in critical_failed if k != "filename_mentions_allowed_only"]
    if hard:
        report["status"] = "aborted_before_write"
        ver_path = OUT / "verification.json"
        write_new(ver_path, json.dumps(report, indent=2, ensure_ascii=False) + "\n")
        print("ABORT, hard failures:", hard)
        sys.exit(2)

    output_meta = {}
    for name, text in outputs.items():
        path = OUT / name
        write_new(path, text)
        output_meta[name] = {
            "path": str(path),
            "bytes": path.stat().st_size,
            "chars": len(text),
            "lines": text.count("\n"),
            "sha256": sha256_file(path),
        }
    report["outputs"] = output_meta

    original_sha_after = {name: sha256_file(FULL / name) for name in ORIGINAL_NAMES}
    report["original_sha256_after"] = original_sha_after
    unchanged = original_sha_before == original_sha_after
    report["originals_unchanged"] = unchanged
    if not unchanged:
        report["issues"].append("ORIGINAL FILE HASH CHANGED")
        report["status"] = "wrote_but_originals_changed"
    else:
        report["status"] = "ok" if not report["issues"] else "ok_with_notes"

    # also record sizes of sources for the report
    report["source_sizes"] = {
        name: (FULL / name).stat().st_size for name in ORIGINAL_NAMES
    }
    report["pointer_stats"] = {
        "unique_teaching_ranges": len(t_ranges),
        "teaching_pointers_in_topics_md": sum(len(T_PTR_RE.findall(L)) for L in topics_md),
        "unique_assignments": len(a_map),
        "assignment_pointers_in_topics_md": sum(len(A_PTR_RE.findall(L)) for L in topics_md),
        "teaching_labels": [t_labels[r] for r in sorted(t_ranges)][:3] + ["..."] + [t_labels[sorted(t_ranges)[-1]]],
    }

    ver_path = OUT / "verification.json"
    write_new(ver_path, json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print("STATUS", report["status"])
    print("ISSUES", len(report["issues"]))
    for issue in report["issues"]:
        print(" -", issue)
    for name, meta in output_meta.items():
        print("WROTE", name, meta["bytes"], "bytes", meta["lines"], "lines")
    print("WROTE verification.json")
    if report["status"] not in ("ok", "ok_with_notes"):
        sys.exit(1)


if __name__ == "__main__":
    main()
