#!/usr/bin/env bash
set -euo pipefail

# Canonical Python LLD/Clean Architecture project bootstrap (macOS)

PROJECT_NAME="${1:-cleanarch_project}"

# Check dependencies
command -v python3 >/dev/null 2>&1 || { echo "python3 not installed"; exit 1; }
command -v pipx >/dev/null 2>&1 || { echo "pipx required: brew install pipx"; exit 1; }

# Create project directory
mkdir -p "${PROJECT_NAME}"
cd "${PROJECT_NAME}"

# Create project structure
mkdir -p src/app/{domain,application,adapters,entrypoints}
mkdir -p tests/{unit,integration,e2e}
mkdir -p scripts

# pyproject.toml baseline
cat > pyproject.toml << 'EOF'
[project]
name = "cleanarch-app"
version = "0.1.0"
requires-python = ">=3.12"

[tool.ruff]
line-length = 88

[tool.pytest.ini_options]
addopts = "--strict-markers --disable-warnings"

EOF

# Makefile baseline
cat > Makefile << 'EOF'
.PHONY: install lint test type run

install:
	uv sync || poetry install || pip install -r requirements.txt

lint:
	ruff check .

format:
	ruff check . --fix

test:
	pytest -q

type:
	mypy src

run:
	python -m app.entrypoints.main
EOF

# Install global tools via pipx
pipx install ruff || true
pipx install mypy || true
pipx install uv || true

# Local virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Optional: prepare local requirements
cat > requirements.txt << 'EOF'
pytest
pytest-cov
mypy
EOF

echo "Project initialized in ${PROJECT_NAME}"
