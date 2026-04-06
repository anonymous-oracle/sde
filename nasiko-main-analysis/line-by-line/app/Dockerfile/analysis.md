# app/Dockerfile — line-by-line analysis

## Lines 1-8
- Base image `python:3.12-slim`; sets workdir.
- Installs `git` and cleans apt cache.

## Lines 9-16
- Copies `uv` binary from official image.
- Copies `pyproject.toml` and `uv.lock` for dependencies.

## Lines 17-24
- Copies `app/` source into image.
- Exposes port 8000.

## Lines 25-27
- Runs Uvicorn via `uv run`, binding to 0.0.0.0:8000.
