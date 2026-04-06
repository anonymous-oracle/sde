Root Files Analysis
===================

README.md
---------
- Type: Documentation
- Purpose: Primary project overview, architecture, setup, agent development, routing, observability.
- Key logic: Describes service topology, ports, supported LLM providers, and workflows.
- Inputs/Outputs: None; user-facing docs.
- Dependencies: N/A

CONTRIBUTING.md
--------------
- Type: Documentation
- Purpose: Contributor workflow, code style, testing, commit conventions.
- Key logic: Defines conventional commit format and dev setup.
- Inputs/Outputs: None.

LICENSE
-------
- Type: License text
- Purpose: Apache 2.0 license for the repo.
- Inputs/Outputs: None.

.gitignore
----------
- Type: VCS ignore rules
- Purpose: Ignore Python artifacts, envs, build outputs, test caches, and secrets.
- Key logic: Explicitly ignores `.env*` and `superuser_credentials.json`.
- Notes: Supports `*.env.example` exceptions.

.github/workflows/ci.yml
------------------------
- Type: CI workflow
- Purpose: Run formatting and type checks on PRs and pushes to main.
- Key logic: `black --check`, `mypy --ignore-missing-imports` on Python 3.12.
- Inputs/Outputs: GitHub Actions environment.

pyproject.toml (repo root)
--------------------------
- Type: Python packaging config
- Purpose: Defines shared dependencies used across backend, router, agents, and tooling.
- Key logic: Lists LLM, observability, DB, vector, and web framework dependencies.
- Dependencies: fastapi, langchain, opentelemetry, arize-phoenix, motor, redis, kubernetes, etc.
- Notes: Also includes dev tools (black, ruff, mypy).

uv.lock
-------
- Type: Dependency lock file (uv)
- Purpose: Fully pinned dependency resolution for Python packages.
- Notes: Large; summarized by `pyproject.toml` instead of exhaustive parsing.

Makefile
--------
- Type: Build/run helpers
- Purpose: Docker lifecycle shortcuts and local worker orchestration.
- Key logic: `clean-all`, `backend-app`, `router`, `orchestrator`, `redis-listener`.
- Notes: References `orchestrator/orchestrator.py` (not present in tree).

docker-compose.local.yml
------------------------
- Type: Compose stack definition
- Purpose: Local dev environment (Mongo, Redis, Kong, backend, router, web, chat history, registry).
- Key logic: Environment variables, healthchecks, networks, volumes, worker + superuser job.
- Outputs: Running containers with mapped ports.

Dockerfile.worker
-----------------
- Type: Container build file
- Purpose: Build image for local Redis stream listener and superuser job.
- Key logic: Installs Docker CLI, copies orchestrator code, installs deps, entrypoint to listener.
- Dependencies: Docker CLI, redis, requests, OpenTelemetry, Phoenix, Langtrace.

superuser_init.py
-----------------
- Type: Python script
- Purpose: One-shot bootstrap to create or verify superuser via auth service.
- Key logic: Uses `SuperuserManager` from `orchestrator/superuser_manager.py`.
- Inputs: `SUPERUSER_*` env vars, `AUTH_SERVICE_URL`.

.nasiko-local.env.example
-------------------------
- Type: Environment template
- Purpose: Example env config for local stack.
- Notes: Not read by policy (env/credentials file). Documented by name and references only.
