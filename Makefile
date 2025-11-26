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
