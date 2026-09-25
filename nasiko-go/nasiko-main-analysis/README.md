Nasiko Main Analysis
====================

Purpose
-------
This directory contains file-level analysis for `nasiko-main`, structured to mirror
the codebase and capture:
- file purpose
- implemented logic
- data flows and interfaces
- dependencies and external services
- design and architecture notes

Structure
---------
- `index.md`: master index of file list and analysis map
- `diagrams.md`: architecture, flow charts, and callgraphs
- `root/`: top-level files (build, CI, compose, repo metadata)
- `app/`: backend API service (FastAPI)
- `agent-gateway/`: Kong registry, router, chat history service, plugins
- `agents/`: sample A2A agents and templates
- `cli/`: CLI and infra automation
- `orchestrator/`: local Docker orchestration and Redis stream consumer
- `worker/`: K8s BuildKit worker
- `models/`: Ollama model stack
- `docs/`: documentation

Conventions
-----------
Each module index lists per-file notes in a consistent mini-template:
- Type
- Purpose
- Key logic
- Inputs/Outputs
- Dependencies
- Notes

Limitations and safety rules
----------------------------
- `.nasiko-local.env.example` is not read (env/credential file).
- `.zip` archives are not expanded; they are documented as packaged copies of
  existing agent directories.
- Large lock files (`uv.lock`) are summarized by intent and not exhaustively parsed.
  Dependencies are documented from `pyproject.toml` files instead.

Status
------
This analysis is derived from the file list at `nasiko-main-list.txt` and the
codebase contents. If new files are added, update `index.md` and the relevant
module index.
