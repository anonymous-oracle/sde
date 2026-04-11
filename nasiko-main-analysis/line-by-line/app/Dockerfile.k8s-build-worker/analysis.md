# app/Dockerfile.k8s-build-worker — line-by-line analysis

## Lines 1-8
- Base image `python:3.12-slim`; sets workdir.
- Installs `git` and cleans apt cache.

## Lines 9-16
- Copies `uv` binary.
- Copies dependency files and runs `uv sync --no-dev`.
- Notes intent to avoid startup dependency downloads.

## Lines 17-24
- Installs Phoenix/OTEL-related deps explicitly for observability.
- Validates imports with a Python one-liner.
- Copies `app` and `worker` sources.

## Lines 25-28
- Prepends venv to PATH.
- Runs `worker.k8s_build_worker` as module entrypoint.
