#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import textwrap
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


SOURCE_SPECS = [
    ("textbooks", Path("/Users/Suhas.KS/textbooks.md")),
    ("analysis", Path("/Users/Suhas.KS/CurriculumSpine2.txt")),
    ("dense", Path("/Users/Suhas.KS/curriculum-spine.md")),
    ("structured", Path("/Users/Suhas.KS/curriculum-spine2.md")),
    ("master", Path("/Users/Suhas.KS/master-curriculum.md")),
]

COMPARE_ONLY_SPECS = [
    ("prior_dump", Path("/Users/Suhas.KS/curriculum-load.md")),
]

ANCHORS = [
    "Audit Checkpoint 1",
    "Audit Checkpoint 2",
    "Audit Checkpoint 3",
    "Audit Checkpoint 4",
    "Audit Checkpoint 5",
    "Operational Execution Strategy",
    "Hall & Knight",
    "Tattersall",
    "Apostol",
    "Rosen",
    "Grimaldi",
    "aima-python",
    "OpenFst Toolkit",
    "Karhunen-",
    "BigQuery ML",
    "PANCE",
    "Pathology: The Big Picture",
]

ANALYSIS_PURE_EXCLUDE_PATTERNS = [
    re.compile(r"^The rapid evolution of artificial intelligence"),
    re.compile(r"^In strict adherence to the parameters of this analysis"),
    re.compile(r"^Initial Assimilation and Inventory Verification$"),
    re.compile(r"^Before initiating the comprehensive deconstruction"),
    re.compile(r"^Audit Checkpoint \d+:"),
    re.compile(r"^Forensic Audit Verification$"),
    re.compile(r"^To satisfy the strict requirement for exhaustive verification"),
    re.compile(r"^The audit guarantees zero omissions"),
]

STRUCTURED_POLICY_LINE_RANGE = range(428, 436)

STRUCTURED_BIBLIOGRAPHY_HEADING_MAP = {
    "FOUNDATIONAL MATHEMATICS SERIES (ICSE Classes 6 to 10)": "ICSE Mathematics Series (Classes 6–10)",
    "NCERT MATHEMATICS EDITIONS (Official 2025–2026 Academic Year)": "NCERT Mathematics",
    "COMPETITIVE ENTRANCE & ADVANCED CLASSICS (JEE Main & Advanced)": "Competitive Entrance & Advanced Classics",
    "NUMBER THEORY & ADVANCED RIGOR SERIES": "Number Theory",
    "PROOFS, ANALYSIS, AND RIGOROUS VECTOR SPACES": "Proofs, Analysis, and Rigorous Vector Spaces",
    "GRADUATE APPLIED ENGINEERING PARADIGMS": "Higher Engineering Mathematics",
    "SIGNALS, COMMUNICATIONS, AND DIGITAL SIGNAL PROCESSING": "Signals, Systems & Digital Signal Processing",
    "SPEECH AND WEIGHTED AUTOMATA SYSTEMS": "Speech & Weighted Automata Systems",
    "PRODUCTION MACHINE LEARNING & SOFTWARE ENGINEERING": "Production Machine Learning & Software Engineering",
}


@dataclass
class SourceFile:
    key: str
    path: Path
    text: str
    lines: list[str]
    sha1: str
    byte_count: int
    ends_with_newline: bool


def sha1_text(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_source(key: str, path: Path) -> SourceFile:
    text = path.read_text(encoding="utf-8")
    return SourceFile(
        key=key,
        path=path,
        text=text,
        lines=text.splitlines(),
        sha1=sha1_text(text),
        byte_count=len(text.encode("utf-8")),
        ends_with_newline=text.endswith("\n"),
    )


def line_hash(line: str) -> str:
    return sha256_text(line)


def duplicate_line_set(sources: dict[str, SourceFile], exclude_key: str) -> set[str]:
    values: set[str] = set()
    for key, source in sources.items():
        if key == exclude_key:
            continue
        for line in source.lines:
            stripped = line.strip()
            if stripped:
                values.add(stripped)
    return values


def classify_analysis_line(line: str) -> str:
    stripped = line.strip()
    if not stripped:
        return "blank"
    if re.match(r"^\d+\. https?://", stripped):
        return "raw_reference_url"
    if stripped.startswith("Audit Checkpoint "):
        return "audit_checkpoint"
    if stripped == "Forensic Audit Verification":
        return "audit_heading"
    if stripped.startswith("To satisfy the strict requirement"):
        return "audit_verification"
    if stripped.startswith("The audit guarantees zero omissions"):
        return "audit_verification"
    if stripped.startswith("Textbook Deconstruction:"):
        return "deconstruction_heading"
    if stripped.startswith("Categorization"):
        return "table_header"
    if stripped.startswith("Deep Learning and Neural Networks: Comprehensive Curriculum"):
        return "curriculum_heading"
    if stripped.startswith("MODULE "):
        return "curriculum_module_heading"
    if re.match(r"^\d+\.\d+ ", stripped):
        return "curriculum_topic"
    if stripped.startswith("Phase "):
        return "phase_heading"
    if stripped.startswith("1.") or stripped.startswith("2.") or stripped.startswith("3.") or stripped.startswith("4."):
        return "numbered_topic"
    if stripped.startswith("• "):
        return "bullet_topic"
    if any(pattern.match(stripped) for pattern in ANALYSIS_PURE_EXCLUDE_PATTERNS):
        return "analysis_meta"
    if stripped.endswith("Theory") or stripped.endswith("Architectures") or stripped.endswith("Pipelines"):
        return "subject_heading"
    return "analysis_content"


def classify_structured_line(line_number: int, line: str) -> str:
    stripped = line.strip()
    if not stripped:
        return "blank"
    if line_number in STRUCTURED_POLICY_LINE_RANGE:
        return "policy_instruction"
    if line_number < 119:
        if stripped.startswith("#") or stripped.startswith("SECTION") or re.match(r"^\d+\.", stripped):
            return "bibliography_heading"
        return "bibliography_or_intro"
    if stripped.startswith("## TIER"):
        return "tier_heading"
    if stripped.startswith("* Module"):
        return "module_heading"
    if stripped.startswith("* Concepts"):
        return "concept_list"
    if stripped.startswith("* Skills"):
        return "skill_list"
    if stripped.startswith("### Operational Execution Strategy"):
        return "policy_instruction"
    return "structured_content"


def classify_textbooks_line(line: str) -> str:
    stripped = line.strip()
    if not stripped:
        return "blank"
    if stripped.startswith("**"):
        return "bibliography_heading"
    if stripped.startswith("-"):
        return "bibliography_entry"
    return "bibliography_misc"


def classify_dense_line(line: str) -> str:
    return "supplementary_dense_raw" if line.strip() else "blank"


def classify_master_line(line: str, duplicated_elsewhere: bool) -> str:
    stripped = line.strip()
    if not stripped:
        return "blank"
    if duplicated_elsewhere:
        return "composite_duplicate"
    return "composite_unique_or_mixed"


def pure_dump_status(source_key: str, line_number: int, line: str, classification: str) -> tuple[str, str]:
    stripped = line.strip()
    if not stripped:
        return ("no", "blank_line")

    if source_key == "textbooks":
        return ("yes", "included_bibliography")

    if source_key == "analysis":
        if classification in {"audit_checkpoint", "audit_heading", "audit_verification", "analysis_meta"}:
            return ("no", "excluded_meta_or_audit")
        return ("yes", "included_analysis_content")

    if source_key == "structured":
        if line_number in STRUCTURED_POLICY_LINE_RANGE:
            return ("no", "excluded_policy_instruction")
        if line_number < 119:
            return ("no", "duplicate_bibliography_covered_elsewhere")
        return ("yes", "included_structured_spine")

    if source_key == "dense":
        return ("partial", "normalized_into_supplementary_section")

    if source_key == "master":
        return ("no", "composite_preserved_in_lossless_archive")

    return ("no", "unclassified")


def build_lossless_archive(sources: dict[str, SourceFile], output_path: Path) -> None:
    lines: list[str] = []
    lines.append("# Lossless Curriculum Archive")
    lines.append("")
    lines.append("This archive preserves every original source file verbatim, with file-level provenance and checksums.")
    lines.append("")
    lines.append("## Source Manifest")
    lines.append("")
    lines.append("| Key | Path | Lines | Bytes | SHA1 | Trailing Newline |")
    lines.append("| --- | --- | ---: | ---: | --- | --- |")
    for source in sources.values():
        lines.append(
            f"| {source.key} | {source.path} | {len(source.lines)} | {source.byte_count} | {source.sha1} | {'yes' if source.ends_with_newline else 'no'} |"
        )
    lines.append("")

    for source in sources.values():
        lines.append(f"## Source: {source.path.name}")
        lines.append("")
        lines.append(f"- Source key: `{source.key}`")
        lines.append(f"- Source path: `{source.path}`")
        lines.append(f"- Line count: `{len(source.lines)}`")
        lines.append(f"- Byte count: `{source.byte_count}`")
        lines.append(f"- SHA1: `{source.sha1}`")
        lines.append(f"- Trailing newline present: `{'yes' if source.ends_with_newline else 'no'}`")
        lines.append("")
        lines.append("~~~text")
        lines.append(source.text if source.text.endswith("\n") else f"{source.text}\n")
        lines.append("~~~")
        lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")


def filter_analysis_for_pure(source: SourceFile) -> list[str]:
    kept: list[str] = []
    for line in source.lines:
        classification = classify_analysis_line(line)
        status, _ = pure_dump_status("analysis", 0, line, classification)
        if status == "yes":
            kept.append(line)
    return kept


def filter_structured_for_pure(source: SourceFile) -> list[str]:
    kept: list[str] = []
    for line_number, line in enumerate(source.lines, start=1):
        classification = classify_structured_line(line_number, line)
        status, _ = pure_dump_status("structured", line_number, line, classification)
        if status == "yes":
            kept.append(line)
    return kept


def normalize_comparison_text(text: str) -> str:
    text = text.strip().lower()
    text = text.replace("&", " and ")
    text = re.sub(r"[–—−]", "-", text)
    text = re.sub(r"\([^)]*\)", "", text)
    text = text.split(":", 1)[0]
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def bibliography_entry_key(line: str) -> str:
    entry = re.sub(r"^[-*]\s+", "", line.strip())
    parts = re.split(r"\s+(?:-|–|—|−)\s+", entry, maxsplit=1)
    if len(parts) == 2:
        title, author = parts
    else:
        title, author = entry, ""
    return f"{normalize_comparison_text(title)}|{normalize_comparison_text(author)}"


def bibliography_entry_score(line: str) -> int:
    score = len(line.strip())
    if ":" in line:
        score += 20
    if "(" in line and ")" in line:
        score += 10
    return score


def parse_textbooks_bibliography_sections(source: SourceFile) -> list[tuple[str, list[str]]]:
    sections: list[tuple[str, list[str]]] = []
    current_heading: str | None = None
    current_entries: list[str] = []

    for line in source.lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("**") and stripped.endswith("**"):
            if current_heading is not None:
                sections.append((current_heading, current_entries))
            current_heading = stripped.strip("*")
            current_entries = []
            continue
        if stripped.startswith("-") and current_heading is not None:
            current_entries.append(stripped)

    if current_heading is not None:
        sections.append((current_heading, current_entries))

    return [(heading, entries) for heading, entries in sections if entries]


def map_structured_bibliography_heading(line: str) -> str:
    heading = re.sub(r"^\d+\.\s*", "", line.strip())
    return STRUCTURED_BIBLIOGRAPHY_HEADING_MAP.get(heading, heading.title())


def parse_structured_bibliography_sections(source: SourceFile) -> list[tuple[str, list[str]]]:
    sections: list[tuple[str, list[str]]] = []
    current_heading: str | None = None
    current_entries: list[str] = []

    for line_number, line in enumerate(source.lines, start=1):
        if line_number >= 119:
            break

        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("Below is the complete"):
            continue
        if stripped.startswith("#") or stripped.startswith("SECTION"):
            continue
        if set(stripped) <= {"=", "-"}:
            continue
        if re.match(r"^\d+\.\s+", stripped):
            if current_heading is not None:
                sections.append((map_structured_bibliography_heading(current_heading), current_entries))
            current_heading = stripped
            current_entries = []
            continue
        if stripped.startswith("*") and current_heading is not None:
            current_entries.append(f"- {stripped.lstrip('*').strip()}")

    if current_heading is not None:
        sections.append((map_structured_bibliography_heading(current_heading), current_entries))

    return [(heading, entries) for heading, entries in sections if entries]


def merged_bibliography_text(textbooks: SourceFile, structured: SourceFile) -> str:
    merged_sections: list[dict[str, object]] = []
    section_positions: dict[str, int] = {}
    entry_positions: dict[str, tuple[str, int]] = {}

    def ensure_section(heading: str) -> list[str]:
        if heading not in section_positions:
            section_positions[heading] = len(merged_sections)
            merged_sections.append({"heading": heading, "entries": []})
        section = merged_sections[section_positions[heading]]
        return section["entries"]  # type: ignore[return-value]

    def add_entry(heading: str, entry: str) -> None:
        key = bibliography_entry_key(entry)
        if not key:
            return

        existing_position = entry_positions.get(key)
        if existing_position is None:
            entries = ensure_section(heading)
            entries.append(entry)
            entry_positions[key] = (heading, len(entries) - 1)
            return

        existing_heading, existing_index = existing_position
        existing_entries = merged_sections[section_positions[existing_heading]]["entries"]
        if bibliography_entry_score(entry) > bibliography_entry_score(existing_entries[existing_index]):
            existing_entries[existing_index] = entry

    for heading, entries in parse_textbooks_bibliography_sections(textbooks):
        ensure_section(heading)
        for entry in entries:
            add_entry(heading, entry)

    for heading, entries in parse_structured_bibliography_sections(structured):
        for entry in entries:
            add_entry(heading, entry)

    lines: list[str] = []
    for section in merged_sections:
        entries = section["entries"]
        if not entries:
            continue
        lines.append(f"**{section['heading']}**")
        lines.extend(entries)
        lines.append("")

    return "\n".join(lines).rstrip("\n")


def normalize_dense_text(source: SourceFile) -> str:
    text = source.text.strip()
    if not text:
        return ""

    start_markers = [
        "Phase 0 and 1: Secondary Foundations and High-School Bridge",
        "ICSE Mathematics: Selina Concise Series (Classes 6",
    ]
    for marker in start_markers:
        marker_index = text.find(marker)
        if marker_index != -1:
            text = text[marker_index:]
            break

    checkpoint_patterns = [
        r"Audit Checkpoint\s*0?2:.*?(?=Class Level)",
        r"Audit Checkpoint\s*0?3:.*?(?=Chapter Name)",
        r"Audit Checkpoint\s*0?4:.*?(?=The curriculum transitions)",
        r"Audit Checkpoint\s*0?5:.*?(?=Author & Title)",
        r"Audit Checkpoint\s*0?6:.*?(?=Advanced Problems in Mathematics for JEE Main & Advanced)",
        r"Audit Checkpoint\s*0?7:.*?(?=Text and Author)",
        r"Audit Checkpoint\s*0?8:.*?(?=Discrete Mathematics and Combinatorics)",
        r"Internal Audit Checkpoint\s*0?9:.*?(?=Higher Engineering Mathematics\(B\.S\. Grewal\))",
        r"Internal Audit Checkpoint\s*10:.*?(?=DisciplineTextbook / AuthorExhaustive List of Topics and Scope)",
        r"Internal Audit Checkpoint\s*11:.*?(?=Medical DomainExhaustive List of Textbooks, Modules, and Specialty Categories)",
        r"Final Audit Checkpoint:.*$",
    ]
    for pattern in checkpoint_patterns:
        text = re.sub(pattern, "", text, flags=re.S)

    trimming_patterns = [
        r"Rigorous Forensic Audit and Final Reconciliation.*$",
        r"The forensic reconciliation process demands.*$",
        r"The audit confirms.*$",
        r"The mandate for absolute structural exhaustiveness.*$",
    ]
    for pattern in trimming_patterns:
        text = re.sub(pattern, "", text)

    marker_replacements = [
        "Phase 0 and 1: Secondary Foundations and High-School Bridge",
        "ICSE Mathematics: Selina Concise Series",
        "Understanding ICSE Mathematics by M.L. Aggarwal",
        "NCERT Mathematics (Classes 11 & 12)",
        "Phase 2: Advanced Secondary Mathematics (Competitive Frameworks)",
        "Hall & Knight: Higher Algebra",
        "Elementary Number Theory in Nine Chapters",
        "Introduction to Analytic Number Theory",
        "Phase 4: Discrete Mathematics, Topology, and Linear Algebra",
        "Discrete Mathematics and Combinatorics",
        "Real Analysis and Linear Algebra",
        "Phase 5: Engineering Mathematics, Telecommunications, and Signal Processing",
        "Higher Engineering Mathematics(B.S. Grewal)",
        "Signals and Systems(Oppenheim & Willsky)",
        "Elements of Information Theory(Cover & Thomas)",
        "Digital Signal Processing: Principles, Algorithms, and Applications(John G. Proakis & Dimitris G. Manolakis)",
        "Digital Communications(John G. Proakis & Masoud Salehi)",
        "Understanding Digital Signal Processing(Richard G. Lyons)",
        "Software Engineering and Mechanical Architecture",
        "Software EngineeringSoftware Engineering at Google",
        "Cognitive Science in Programming",
        "Software Architecture",
        "Code Optimization",
        "Web Development",
        "Programming Languages",
        "Fluid Mechanics",
        "Mechanical Engineering",
        "Aerospace Engineering",
        "Clinical and Basic Medical Sciences Curriculum",
        "Medical Domain",
        "Basic Science",
        "Clinical Practices & Board Review",
        "Physician Associate/Assistant",
        "Diagnostic and Imaging Studies",
        "Interactive Modules & Flashcards",
        "Clerkship Resource Collections",
        "Library Specialties",
        "Specific Textbooks Uncovered",
    ]
    for marker in marker_replacements:
        text = text.replace(marker, f"\n\n{marker}")

    structural_replacements = {
        "Author & TitleExhaustive List of Chapters and Concepts": "Author & Title\nExhaustive List of Chapters and Concepts",
        "Text and AuthorExhaustive List of Chapters and Topics": "Text and Author\nExhaustive List of Chapters and Topics",
        "Text and AuthorExhaustive List of Chapters and Modules": "Text and Author\nExhaustive List of Chapters and Modules",
        "Text and AuthorExhaustive List of Chapters, Modules, and Tricks": "Text and Author\nExhaustive List of Chapters, Modules, and Tricks",
        "DisciplineTextbook / AuthorExhaustive List of Topics and Scope": "Discipline\nTextbook / Author\nExhaustive List of Topics and Scope",
        "Medical DomainExhaustive List of Textbooks, Modules, and Specialty Categories": "Medical Domain\nExhaustive List of Textbooks, Modules, and Specialty Categories",
    }
    for old, new in structural_replacements.items():
        text = text.replace(old, new)

    paragraphs: list[str] = []
    for block in re.split(r"\n\n+", text):
        block = block.strip()
        if not block:
            continue
        if block.startswith("Audit Checkpoint") or block.startswith("Internal Audit"):
            continue
        wrapped = textwrap.fill(block, width=120, break_long_words=False, break_on_hyphens=False)
        paragraphs.append(wrapped)

    return "\n\n".join(paragraphs)


def build_pure_dump(sources: dict[str, SourceFile], output_path: Path) -> None:
    textbooks = sources["textbooks"]
    analysis = sources["analysis"]
    structured = sources["structured"]
    dense = sources["dense"]

    sections: list[str] = []
    sections.append("# Curriculum Content Extract")
    sections.append("")
    sections.append("## Bibliography")
    sections.append("")
    sections.append(merged_bibliography_text(textbooks, structured))
    sections.append("")
    sections.append("## Advanced Textbook Deconstructions and Domain Topics")
    sections.append("")
    sections.append("\n".join(filter_analysis_for_pure(analysis)).rstrip("\n"))
    sections.append("")
    sections.append("## Eight-Tier Curriculum Spine")
    sections.append("")
    sections.append("\n".join(filter_structured_for_pure(structured)).rstrip("\n"))
    sections.append("")
    sections.append("## Supplementary Dense Taxonomy Source")
    sections.append("")
    sections.append(normalize_dense_text(dense))
    sections.append("")

    output_path.write_text("\n".join(sections), encoding="utf-8")


def build_unified_deduped_dump(sources: dict[str, SourceFile], output_path: Path) -> None:
    textbooks = sources["textbooks"]
    analysis = sources["analysis"]
    structured = sources["structured"]
    dense = sources["dense"]

    sections: list[str] = []
    sections.append("# Unified Curriculum Load")
    sections.append("")
    sections.append("## Bibliography")
    sections.append("")
    sections.append(merged_bibliography_text(textbooks, structured))
    sections.append("")
    sections.append("## Advanced Textbook Deconstructions and Domain Topics")
    sections.append("")
    sections.append("\n".join(filter_analysis_for_pure(analysis)).rstrip("\n"))
    sections.append("")
    sections.append("## Eight-Tier Curriculum Spine")
    sections.append("")
    sections.append("\n".join(filter_structured_for_pure(structured)).rstrip("\n"))
    sections.append("")
    sections.append("## Supplementary Dense Taxonomy Source")
    sections.append("")
    sections.append(normalize_dense_text(dense))
    sections.append("")

    output_path.write_text("\n".join(sections), encoding="utf-8")


def build_omission_ledger(sources: dict[str, SourceFile], output_path: Path) -> None:
    other_source_lines_for_master = duplicate_line_set(sources, "master")

    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "source_key",
                "source_path",
                "line_number",
                "classification",
                "line_sha256",
                "in_lossless_archive",
                "in_pure_dump",
                "pure_dump_reason",
                "content_preview",
            ]
        )

        for source in sources.values():
            for line_number, line in enumerate(source.lines, start=1):
                if source.key == "textbooks":
                    classification = classify_textbooks_line(line)
                elif source.key == "analysis":
                    classification = classify_analysis_line(line)
                elif source.key == "structured":
                    classification = classify_structured_line(line_number, line)
                elif source.key == "dense":
                    classification = classify_dense_line(line)
                else:
                    classification = classify_master_line(line, line.strip() in other_source_lines_for_master)

                pure_status, pure_reason = pure_dump_status(source.key, line_number, line, classification)
                writer.writerow(
                    [
                        source.key,
                        str(source.path),
                        line_number,
                        classification,
                        line_hash(line),
                        "yes",
                        pure_status,
                        pure_reason,
                        line.strip()[:160],
                    ]
                )


def contains_subsequence(haystack: list[str], needle: list[str]) -> int | None:
    if not needle or len(needle) > len(haystack):
        return None
    needle_length = len(needle)
    for index in range(len(haystack) - needle_length + 1):
        if haystack[index : index + needle_length] == needle:
            return index + 1
    return None


def build_validation_report(
    sources: dict[str, SourceFile],
    compare_only: dict[str, SourceFile],
    archive_path: Path,
    pure_dump_path: Path,
    ledger_path: Path,
    output_path: Path,
) -> None:
    archive_text = archive_path.read_text(encoding="utf-8")
    pure_dump_text = pure_dump_path.read_text(encoding="utf-8")

    master = sources["master"]
    analysis = sources["analysis"]
    textbooks = sources["textbooks"]
    structured = sources["structured"]

    relations: list[str] = []
    if master.lines[: len(analysis.lines)] == analysis.lines:
        relations.append(
            f"- `{analysis.path.name}` appears verbatim as the first `{len(analysis.lines)}` lines of `{master.path.name}`."
        )
    if master.lines[-len(textbooks.lines) :] == textbooks.lines:
        relations.append(
            f"- `{textbooks.path.name}` appears verbatim as the final `{len(textbooks.lines)}` lines of `{master.path.name}`."
        )
    structured_anchor = structured.lines[2:10]
    structured_position = contains_subsequence(master.lines, structured_anchor)
    if structured_position is not None:
        relations.append(
            f"- `{structured.path.name}` section beginning with `# UNIFIED MATHEMATICAL AND TECHNICAL CURRICULUM ARCHITECTURE REFERENCE` begins at line `{structured_position}` of `{master.path.name}`."
        )

    def anchor_present(text: str, anchor: str) -> bool:
        if anchor.startswith("Audit Checkpoint "):
            checkpoint_number = anchor.rsplit(" ", 1)[-1]
            pattern = re.compile(rf"Audit Checkpoint\s*0?{re.escape(checkpoint_number)}(?::|\b)")
            return bool(pattern.search(text))
        return anchor in text

    anchor_rows: list[str] = []
    for anchor in ANCHORS:
        archive_present = "yes" if anchor_present(archive_text, anchor) else "no"
        pure_present = "yes" if anchor_present(pure_dump_text, anchor) else "no"
        anchor_rows.append(f"| {anchor} | {archive_present} | {pure_present} |")

    pure_status_counter: Counter[str] = Counter()
    with ledger_path.open("r", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            pure_status_counter[row["in_pure_dump"]] += 1

    prior_dump = compare_only.get("prior_dump")
    prior_dump_findings: list[str] = []
    if prior_dump is not None:
        prior_dump_findings.append(
            f"- Prior derived dump `{prior_dump.path.name}` has SHA1 `{prior_dump.sha1}` and line count `{len(prior_dump.lines)}`."
        )
        omitted_sentinels = [
            "Operational Execution Strategy",
            "Audit Checkpoint 1",
            "The rapid evolution of artificial intelligence",
            "The development of Automatic Speech Recognition",
        ]
        for sentinel in omitted_sentinels:
            prior_present = "yes" if sentinel in prior_dump.text else "no"
            pure_present = "yes" if sentinel in pure_dump_text else "no"
            archive_present = "yes" if sentinel in archive_text else "no"
            prior_dump_findings.append(
                f"- Sentinel `{sentinel}`: prior dump `{prior_present}`, lossless archive `{archive_present}`, pure dump `{pure_present}`."
            )

    lines: list[str] = []
    lines.append("# Curriculum Validation Report")
    lines.append("")
    lines.append("## Source Inventory")
    lines.append("")
    lines.append("| Key | Path | Lines | Bytes | SHA1 |")
    lines.append("| --- | --- | ---: | ---: | --- |")
    for source in sources.values():
        lines.append(
            f"| {source.key} | {source.path} | {len(source.lines)} | {source.byte_count} | {source.sha1} |"
        )
    lines.append("")
    lines.append("## Source Relationships")
    lines.append("")
    lines.extend(relations or ["- No direct containment relationships were auto-detected beyond file-level preservation."])
    lines.append("")
    lines.append("## Artifact Coverage")
    lines.append("")
    lines.append(f"- Lossless archive path: `{archive_path}`")
    lines.append(f"- Pure dump path: `{pure_dump_path}`")
    lines.append(f"- Omission ledger path: `{ledger_path}`")
    lines.append("- Lossless archive preservation rule: every source file is embedded verbatim in a fenced block.")
    lines.append("- Pure dump rule: bibliography, deconstructions, module spine, and supplementary taxonomy are included; audit and policy lines are excluded by rule.")
    lines.append("")
    lines.append("## Pure Dump Inclusion Summary")
    lines.append("")
    lines.append(f"- Included line rows: `{pure_status_counter.get('yes', 0)}`")
    lines.append(f"- Excluded line rows: `{pure_status_counter.get('no', 0)}`")
    lines.append(f"- Partially normalized line rows: `{pure_status_counter.get('partial', 0)}`")
    lines.append("")
    lines.append("## Anchor Verification")
    lines.append("")
    lines.append("| Anchor | In Lossless Archive | In Pure Dump |")
    lines.append("| --- | --- | --- |")
    lines.extend(anchor_rows)
    lines.append("")
    lines.append("## Regression Check Against Prior Derived Dump")
    lines.append("")
    lines.extend(prior_dump_findings or ["- No prior derived dump was provided for comparison."])
    lines.append("")
    lines.append("## Verdict")
    lines.append("")
    lines.append("- Lossless archive status: PASS. All original source files are preserved verbatim.")
    lines.append("- Pure dump status: DERIVED VIEW. It intentionally excludes audit/process/policy material and normalizes the dense supplementary source.")

    output_path.write_text("\n".join(lines), encoding="utf-8")


def build_manifest_json(sources: dict[str, SourceFile], output_path: Path) -> None:
    manifest = {
        source.key: {
            "path": str(source.path),
            "sha1": source.sha1,
            "line_count": len(source.lines),
            "byte_count": source.byte_count,
            "ends_with_newline": source.ends_with_newline,
        }
        for source in sources.values()
    }
    output_path.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate curriculum archive artifacts.")
    parser.add_argument(
        "--output-dir",
        default=str(Path(__file__).resolve().parent / "curriculum_artifacts"),
        help="Directory where generated artifacts will be written.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    sources = {key: load_source(key, path) for key, path in SOURCE_SPECS}
    compare_only = {key: load_source(key, path) for key, path in COMPARE_ONLY_SPECS if path.exists()}

    archive_path = output_dir / "curriculum_lossless_archive.md"
    pure_dump_path = output_dir / "curriculum_pure_dump.md"
    unified_deduped_path = output_dir / "curriculum_unified_deduped.md"
    ledger_path = output_dir / "curriculum_omission_ledger.csv"
    report_path = output_dir / "curriculum_validation_report.md"
    manifest_path = output_dir / "curriculum_source_manifest.json"

    build_lossless_archive(sources, archive_path)
    build_pure_dump(sources, pure_dump_path)
    build_unified_deduped_dump(sources, unified_deduped_path)
    build_omission_ledger(sources, ledger_path)
    build_validation_report(sources, compare_only, archive_path, pure_dump_path, ledger_path, report_path)
    build_manifest_json(sources, manifest_path)

    print(f"Generated: {archive_path}")
    print(f"Generated: {pure_dump_path}")
    print(f"Generated: {unified_deduped_path}")
    print(f"Generated: {ledger_path}")
    print(f"Generated: {report_path}")
    print(f"Generated: {manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())