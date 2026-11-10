#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build a lean self-contained compact pair (no embedded teaching appendix).

Writes only NEW files under builds/full/selfcontained/:
  topics_sorted_compact_lean.md
  meta_rules_and_index_sorted_compact_lean.md
  verification_lean.json

Never modifies or deletes existing pack, curriculum, or *_sc.md files.
"""
from __future__ import print_function

import hashlib
import json
import re
import sys
from pathlib import Path

FULL = Path("/Users/suhas/sde/nptel/builds/full")
SC = FULL / "selfcontained"
SRC_TOPICS = FULL / "topics_sorted_compact.md"
SRC_META = SC / "meta_rules_and_index_sorted_compact_sc.md"

OUT_TOPICS = SC / "topics_sorted_compact_lean.md"
OUT_META = SC / "meta_rules_and_index_sorted_compact_lean.md"
OUT_VER = SC / "verification_lean.json"

WATCH = [
    FULL / "topics.md",
    FULL / "meta_rules_and_index.md",
    FULL / "topics_sorted.md",
    FULL / "meta_rules_and_index_sorted.md",
    FULL / "topics_sorted_compact.md",
    FULL / "meta_rules_and_index_sorted_compact.md",
    SC / "topics_sc.md",
    SC / "meta_rules_and_index_sc.md",
    SC / "topics_sorted_sc.md",
    SC / "meta_rules_and_index_sorted_sc.md",
    SC / "topics_sorted_compact_sc.md",
    SC / "meta_rules_and_index_sorted_compact_sc.md",
]

COMPACT_ID_RE = re.compile(r"^([0-9a-z]+) (.+)$")
FILEISH_RE = re.compile(r"\.md|\.json|\.tsv|/Users/")
FORBIDDEN_META_RE = re.compile(
    r"appendix|T:T0|A:A|embedded|teaching_assignments", re.I
)
SIBLING = "topics_sorted_compact_lean.md"
ALLOWED_META = ["Master_Rules.md", "learn-SKILL.md", SIBLING]

NEW_HEADER_LINE3 = (
    "36,628 topics, exact names/levels/order retained. Each base-36 short ID is "
    "its 1-based position, not a graph ID. Level is inherited from the enclosing "
    "header. The teaching method for every topic is in this pack's sibling "
    "meta-rules. Noise IDs listed there remain reconciliation-only."
)

LEVEL_UNKNOWN_BULLET = (
    "- Teach level-unknown (?) topics at graduate depth: undergraduate core then "
    "graduate extension, like UG+PG, unless the learner says otherwise. Do not "
    "relabel the tag; keep it level-unknown in the record until actual course or "
    "syllabus evidence supports a classification."
)

OLD_CEILING = (
    "- A level sets the starting benchmark/depth emphasis, not a ceiling. "
    "Master Rules L0 foundations → L1 intuition → L2 core → L3 rigorous academic "
    "pass → L4 expert/research evidence still applies. A one-line name is a whole "
    "topic, never permission to teach shallowly. Unknown level is a provenance gap, "
    "not a reason to skip the topic or falsely claim graduate-only evidence."
)
NEW_CEILING = (
    "- A level is a floor, not a ceiling: it sets the starting benchmark/depth "
    "emphasis, not a maximum. Master Rules L0 foundations → L1 intuition → L2 core "
    "→ L3 rigorous academic pass → L4 expert/research evidence still applies. A "
    "one-line name is a whole topic, never permission to teach shallowly. Unknown "
    "level is a provenance gap, not a reason to skip the topic or falsely claim "
    "graduate-only evidence."
)

OLD_NOISE11 = (
    "- Keep every listed item in the coverage record. A noise:true appendix is "
    "retained for reconciliation, not endorsed as sound teaching. Unreviewed graph "
    "extraction strings require scope validation against their actual source; do "
    "not invent a lesson from a fragment or quietly remove it."
)
NEW_NOISE11 = (
    "- Keep every listed item in the coverage record. A noise:true reconciliation "
    "list is retained for reconciliation, not endorsed as sound teaching. "
    "Unreviewed graph extraction strings require scope validation against their "
    "actual source; do not invent a lesson from a fragment or quietly remove it."
)

OLD_NOISE15 = (
    "Noise-appendix boundaries are audited separately from the normal learning path."
)
NEW_NOISE15 = (
    "Noise-flagged boundaries are audited separately from the normal learning path."
)

OLD_S3_HEAD = "## 3. Reuse existing teaching and assignments first"
NEW_S3_HEAD = "## 3. Author tutor-generated teaching and assignments"
NEW_S3_BODY = [
    NEW_S3_HEAD,
    "- This pack contains no existing lessons, assignments or extracted source "
    "excerpts. For every listed topic, author all teaching, checks, assignments "
    "and capstones fresh, following sections 4, 6, 10 and 11, and label that work "
    "tutor-generated self-study.",
    "- Do not invent topics, source titles, citations, course codes, editions, "
    "quotations, page numbers or empirical results. Never present tutor-generated "
    "material as a source excerpt. Log genuine scope gaps and obtain learner "
    "agreement before adding a new topic.",
    "- Keep the honesty rules in section 7: never claim a script ran, a key was "
    "computed or an experiment passed unless it actually did; never claim unrun "
    "tests passed.",
]

OLD_R6 = (
    "- Reuse a suitable existing assignment; never invent its questions/key. "
    "Otherwise label the new check tutor-generated self-study: (1) conceptual "
    "choice with reason, (2) multiple-select/conditions or counterexample, "
    "(3) numerical/computational/subject-equivalent application, "
    "(4) proof/derivation/rigorous argument, (5) build/programming/design/"
    "subject-equivalent transfer. Teach every prerequisite first. Use the actual "
    "course profile's marking rules; do not invent a universal pass mark."
)
NEW_R6 = (
    "- Author each five-question unit check as clearly labelled tutor-generated "
    "self-study (this pack has no existing assignments to reuse): (1) conceptual "
    "choice with reason, (2) multiple-select/conditions or counterexample, "
    "(3) numerical/computational/subject-equivalent application, "
    "(4) proof/derivation/rigorous argument, (5) build/programming/design/"
    "subject-equivalent transfer. Teach every prerequisite first. Write and verify "
    "the hidden key before issuing the check; never invent sources, citations or "
    "topics. Use the actual course profile's marking rules; do not invent a "
    "universal pass mark."
)

OLD_R9_USE = (
    "For this sorted edition use topics_sorted_compact_sc.md and this regenerated index:"
)
NEW_R9_USE = (
    "For this sorted edition use topics_sorted_compact_lean.md and this regenerated index:"
)
OLD_R9_TA = (
    "Original topic-line T: and A: labels refer to embedded curriculum text in the "
    "sibling topics file. "
)
# delete that sentence entirely
NEW_R9_TA = ""

OLD_S10_INTRO = (
    "Modelled on the observed curriculum, not official NPTEL/university policy. "
    "Extends rule 6; reuse suitable sources only when actually available, otherwise "
    "label work tutor-generated self-study."
)
NEW_S10_INTRO = (
    "Modelled on the observed curriculum, not official NPTEL/university policy. "
    "Extends rule 6; author all assignments and capstones as tutor-generated "
    "self-study per sections 4, 6, 10 and 11."
)

OLD_BIND = (
    "- In this edition rule 9 selects topics_sorted_compact_sc.md and the index "
    "below. Short IDs are base-36 1-based topic positions, not graph IDs or "
    "source line numbers. Teaching and assignment text is embedded in the appendix "
    "of that sibling topics file, keyed by short ID; rules 3 and 7 still forbid "
    "claiming text that is not present was read."
)
NEW_BIND = (
    "- In this edition rule 9 selects topics_sorted_compact_lean.md and the index "
    "below. Short IDs are base-36 1-based topic positions, not graph IDs or source "
    "line numbers. The sibling topics file is a topic list only. Author all lessons, "
    "checks, assignments and capstones fresh per sections 3, 4, 6, 10 and 11, "
    "labelled tutor-generated self-study. Rules 3 and 7 still forbid inventing "
    "sources or claiming work was read or run when it was not."
)


def sha256_file(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


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
        raise SystemExit("expected string not found in %s:\n%r" % (where, old[:240]))
    return s.replace(old, new)


def extract_compact_topics(lines):
    out = []
    level = None
    for i, line in enumerate(lines, 1):
        if line.startswith("# Embedded curriculum text"):
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


def fileish_hits(text, allowed):
    hits = []
    for i, line in enumerate(text.splitlines(), 1):
        if not FILEISH_RE.search(line):
            continue
        if "/Users/" in line:
            hits.append((i, line))
            continue
        cleaned = line
        for name in allowed:
            cleaned = cleaned.replace(name, "")
        if FILEISH_RE.search(cleaned):
            hits.append((i, line))
    return hits


def write_new(path, text):
    if path.exists():
        raise SystemExit("refusing to overwrite existing file: %s" % path)
    path.write_text(text, encoding="utf-8")
    if sha256_file(path) != sha256_text(text):
        raise SystemExit("write mismatch: %s" % path)


def build_topics(src_lines):
    if src_lines[0] != "# Full topics: compact domain → level → DAG":
        raise SystemExit("unexpected compact topics title: %r" % src_lines[0])
    if "meta_rules_and_index_sorted_compact.md" not in src_lines[2]:
        raise SystemExit("unexpected compact topics header line 3")
    out = list(src_lines)
    out[2] = NEW_HEADER_LINE3
    if len(out) != len(src_lines):
        raise SystemExit("topics header rewrite changed line count")
    return out


def build_meta(src_lines):
    lines = list(src_lines)

    # floor/ceiling wording
    if lines.count(OLD_CEILING) != 1:
        raise SystemExit("expected exactly one ceiling bullet")
    for i, L in enumerate(lines):
        if L == OLD_CEILING:
            lines[i] = NEW_CEILING
            # insert level-unknown teaching-depth rule immediately after
            lines[i + 1:i + 1] = [LEVEL_UNKNOWN_BULLET]
            break

    text = join_lines(lines)
    text = must_replace(text, OLD_NOISE11, NEW_NOISE11, "noise list bullet")
    text = must_replace(text, OLD_NOISE15, NEW_NOISE15, "noise-flagged boundaries")

    # section 3: replace heading + three bullets as a block
    old_s3 = "\n".join([OLD_S3_HEAD] + src_lines[18:21])  # lines 18-21 are heading+3 bullets (1-based 18-21)
    # After inserting one bullet in section 1, those line numbers shifted.
    # Use exact original strings from src, not shifted indices.
    old_s3 = "\n".join(src_lines[17:21])  # original 0-based 17..20 = lines 18-21
    if old_s3 not in text:
        raise SystemExit("section 3 block not found after earlier edits")
    new_s3 = "\n".join(NEW_S3_BODY)
    text = must_replace(text, old_s3, new_s3, "section 3")

    text = must_replace(text, OLD_R6, NEW_R6, "rule 6")
    text = must_replace(text, OLD_R9_USE, NEW_R9_USE, "rule 9 sibling")
    text = must_replace(text, OLD_R9_TA, NEW_R9_TA, "rule 9 T/A sentence")
    text = must_replace(text, OLD_S10_INTRO, NEW_S10_INTRO, "section 10 intro")
    text = must_replace(text, OLD_BIND, NEW_BIND, "compact binding")

    out = text.splitlines()
    # section 11 and most of §10 must still be present
    if not any(L.startswith("## 11.") for L in out):
        raise SystemExit("section 11 missing")
    if not any(L.startswith("## 10.") for L in out):
        raise SystemExit("section 10 missing")
    if not any("Cadence override: see section 11 (one coding capstone per collection of related units)." in L for L in out):
        raise SystemExit("section 10 override sentence missing")
    if not any(L.startswith("- One coding capstone per collection of related units:") for L in out):
        raise SystemExit("section 11 collection-capstone bullet missing")
    if LEVEL_UNKNOWN_BULLET not in out:
        raise SystemExit("level-unknown teaching rule missing")
    if NEW_CEILING not in out:
        raise SystemExit("floor/ceiling bullet missing")
    return out


def main():
    for p in (OUT_TOPICS, OUT_META, OUT_VER):
        if p.exists():
            raise SystemExit("refusing to overwrite existing file: %s" % p)

    before = {str(p): sha256_file(p) for p in WATCH}
    src_topics = read_lines(SRC_TOPICS)
    src_meta = read_lines(SRC_META)

    topics = build_topics(src_topics)
    meta = build_meta(src_meta)
    topics_text = join_lines(topics)
    meta_text = join_lines(meta)

    report = {"issues": [], "checks": {}, "changed_rules": {}}
    report["original_and_sc_sha256_before"] = before

    def check(name, ok, detail=None):
        report["checks"][name] = {"ok": bool(ok), "detail": detail}
        if not ok:
            report["issues"].append("%s: %s" % (name, detail))

    # topics: 36628 lines identical; header only changed; no appendix
    src_tops = extract_compact_topics(src_topics)
    new_tops = extract_compact_topics(topics)
    same = (
        len(src_tops) == 36628
        and len(new_tops) == 36628
        and all(a == b for a, b in zip(src_tops, new_tops))
    )
    check("topic_lines_identical_to_original_compact", same, {
        "src": len(src_tops), "out": len(new_tops),
        "same_line_numbers_and_bytes": same,
    })
    # body after 6-line header byte-identical
    body_same = topics[6:] == src_topics[6:]
    check("topics_body_after_header_identical", body_same, None)
    check("topics_header_line_count_unchanged", len(topics) == len(src_topics), {
        "src_lines": len(src_topics), "out_lines": len(topics)
    })
    has_appendix = any(L.startswith("# Embedded curriculum text") for L in topics)
    check("topics_has_no_appendix", not has_appendix, None)
    t_hits = fileish_hits(topics_text, allowed=[])
    check("topics_no_file_mentions", t_hits == [], [{"line": i, "text": t[:240]} for i, t in t_hits])

    # meta forbidden words
    forb = []
    for i, L in enumerate(meta, 1):
        if FORBIDDEN_META_RE.search(L):
            forb.append({"line": i, "text": L[:300]})
    check("meta_no_appendix_embedded_or_TA_labels", forb == [], forb)

    m_hits = fileish_hits(meta_text, ALLOWED_META)
    check("meta_filename_mentions_allowed_only", m_hits == [], [{"line": i, "text": t[:240]} for i, t in m_hits])

    # sibling name present; sc name gone
    check(
        "meta_points_at_lean_sibling",
        SIBLING in meta_text and "topics_sorted_compact_sc.md" not in meta_text,
        {
            "lean_mentions": meta_text.count(SIBLING),
            "sc_mentions": meta_text.count("topics_sorted_compact_sc.md"),
        },
    )

    # index/audit/noise IDs/domain order verbatim:
    # compare from "# Compact unit index" through EOF
    def from_heading(lines, heading):
        for i, L in enumerate(lines):
            if L == heading:
                return lines[i:]
        return None

    src_index = from_heading(src_meta, "# Compact unit index")
    out_index = from_heading(meta, "# Compact unit index")
    check("unit_index_and_audit_verbatim", src_index is not None and src_index == out_index, {
        "src_tail_lines": None if src_index is None else len(src_index),
        "out_tail_lines": None if out_index is None else len(out_index),
    })
    # noise ID line verbatim
    noise_src = [L for L in src_meta if L.startswith("- Noise:true reconciliation-only topic IDs:")]
    noise_out = [L for L in meta if L.startswith("- Noise:true reconciliation-only topic IDs:")]
    check("noise_ids_verbatim", noise_src == noise_out and len(noise_src) == 1, None)
    domain_src = [L for L in src_meta if L.startswith("- Domain order is unchanged")]
    domain_out = [L for L in meta if L.startswith("- Domain order is unchanged")]
    check("domain_order_verbatim", domain_src == domain_out and len(domain_src) == 1, None)

    # section 11 present and collection wording
    check("section_11_present", any(L.startswith("## 11.") for L in meta), None)

    report["changed_rules"] = {
        "rule_3_heading": NEW_S3_HEAD,
        "rule_3": NEW_S3_BODY[1:],
        "rule_6": NEW_R6,
        "level_unknown_rule": LEVEL_UNKNOWN_BULLET,
        "floor_not_ceiling": NEW_CEILING,
        "section_10_intro": NEW_S10_INTRO,
        "rule_9_and_binding": "sibling renamed to topics_sorted_compact_lean.md; T:/A: and appendix sentences removed; binding says the topics file is a topic list only and all lessons are authored fresh",
        "noise_wording": "replaced the word 'appendix' in the two noise-reconciliation sentences so the lean meta has no 'appendix' mention; meaning retained",
    }

    hard = [k for k, v in report["checks"].items() if isinstance(v, dict) and not v.get("ok", True)]
    report["critical_failed"] = hard
    if hard:
        report["status"] = "aborted_before_write"
        write_new(OUT_VER, json.dumps(report, indent=2, ensure_ascii=False) + "\n")
        print("ABORT", hard)
        sys.exit(2)

    write_new(OUT_TOPICS, topics_text)
    write_new(OUT_META, meta_text)

    after = {str(p): sha256_file(p) for p in WATCH}
    report["original_and_sc_sha256_after"] = after
    unchanged = before == after
    report["originals_and_sc_unchanged"] = unchanged
    if not unchanged:
        report["issues"].append("WATCHED FILE HASH CHANGED")
        changed = {k: {"before": before[k], "after": after[k]} for k in before if before[k] != after[k]}
        report["changed_watched_files"] = changed

    report["outputs"] = {
        "topics_sorted_compact_lean.md": {
            "path": str(OUT_TOPICS),
            "bytes": OUT_TOPICS.stat().st_size,
            "lines": topics_text.count("\n"),
            "sha256": sha256_file(OUT_TOPICS),
        },
        "meta_rules_and_index_sorted_compact_lean.md": {
            "path": str(OUT_META),
            "bytes": OUT_META.stat().st_size,
            "lines": meta_text.count("\n"),
            "sha256": sha256_file(OUT_META),
        },
    }
    report["status"] = "ok" if not report["issues"] else "wrote_with_issues"
    write_new(OUT_VER, json.dumps(report, indent=2, ensure_ascii=False) + "\n")

    print("STATUS", report["status"])
    print("ISSUES", report["issues"])
    for name, meta_info in report["outputs"].items():
        print("WROTE", name, meta_info["bytes"], "bytes", meta_info["lines"], "lines")
    print("WATCHED_UNCHANGED", unchanged)


if __name__ == "__main__":
    main()
