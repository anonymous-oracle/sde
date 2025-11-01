#!/usr/bin/env python3
import argparse, os, sys
from pathlib import Path

TRACK_A_WEEKS = ["week-00A", "week-00B"] + [f"week-{i:03d}" for i in range(1, 113)]
TRACK_B_MODULES = [
    "sd-00-orientation",
    "sd-01-rfcs-adrs",
    "sd-02-scale-zero-to-millions",
    "sd-03-estimation",
    "sd-04-system-design-framework",
    "sd-05-rate-limiter",
    "sd-06-consistent-hashing",
    "sd-07-kv-lsm",
    "sd-08-unique-id-generator",
    "sd-09-url-shortener",
    "sd-10-web-crawler",
    "sd-11-notification-system",
    "sd-12-news-feed",
    "sd-13-chat-system",
    "sd-14-search-autocomplete",
    "sd-15-video-streaming",
    "sd-16-cloud-storage-cas",
    "sd-17-proximity-service",
    "sd-18-nearby-friends",
    "sd-19-maps-tiles",
    "sd-20-distributed-mq",
    "sd-21-metrics-monitoring-alerting",
    "sd-22-hotel-reservation",
    "sd-23-payment-system",
    "sd-24-digital-wallet",
    "sd-25-stock-exchange",
    "sd-26-capstone",
]

README_WEEK = """\
# {title}

## Objectives
- See meta prompt for detailed weekly objectives.

## Folders
- `src/` — illustrative snippets only
- `tests/` — tiny tests
- `exercise/` — requirements + hints (no full solutions)
"""

README_SD = """\
# {title} (System Design)

## Objective
See meta prompt for SD module details.

## Folders
- `src/` — demo code/diagrams
- `tests/` — tiny tests
- `exercise/` — requirements + hints
"""

GITKEEP = ""

def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)

def write_file(path: Path, content: str, overwrite=False):
    if path.exists() and not overwrite:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def create_track_a(root: Path):
    base = root / "track-a"
    ensure_dir(base)
    for w in TRACK_A_WEEKS:
        wk = base / w
        ensure_dir(wk / "src")
        ensure_dir(wk / "tests")
        ensure_dir(wk / "exercise")
        write_file(wk / "README.md", README_WEEK.format(title=w.replace('-', ' ').title()))
        write_file(wk / ".gitkeep", GITKEEP)

def create_track_b(root: Path):
    base = root / "track-b"
    ensure_dir(base)
    for m in TRACK_B_MODULES:
        md = base / m
        ensure_dir(md / "src")
        ensure_dir(md / "tests")
        ensure_dir(md / "exercise")
        title = m.replace('-', ' ').title()
        write_file(md / "README.md", README_SD.format(title=title))
        write_file(md / ".gitkeep", GITKEEP)

def create_shared(root: Path):
    ensure_dir(root / "shared" / "python")
    ensure_dir(root / "docs" / "adr")
    ensure_dir(root / "docs" / "rfc")
    ensure_dir(root / ".github" / "ISSUE_TEMPLATE")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", required=True, help="Absolute path to parent directory")
    ap.add_argument("--repo", required=True, help="Repository folder name to create")
    args = ap.parse_args()

    target = Path(args.path).expanduser().resolve()
    repo = target / args.repo
    ensure_dir(repo)

    create_shared(repo)
    create_track_a(repo)
    create_track_b(repo)

    print(f"Scaffold complete at: {repo}")

if __name__ == "__main__":
    main()
