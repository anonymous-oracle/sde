.PHONY: setup format lint test ci

setup:
	python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements-dev.txt

format:
	. .venv/bin/activate && black .

lint:
	. .venv/bin/activate && ruff check .

test:
	. .venv/bin/activate && pytest

ci: format lint test


