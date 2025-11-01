# {REPO_NAME}

**Backend → Systems Architect (2-Year) + System Design (26 modules)**

- **Track A**: Weeks 0A–0B, 1–112
- **Track B**: SD-00–SD-26

## Getting Started
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
make format && make lint && make test
```

## Scaffolding

Generate all week/module directories and boilerplates:

```bash
python scripts/scaffold.py --path "{TARGET_PATH}" --repo "{REPO_NAME}"
```

Re-running is idempotent (safe).
