# Dockerfile.worker — line-by-line analysis

## Lines 1-8
- Describes worker image purpose, uses Python 3.12 slim, sets workdir.

## Lines 9-16
- Installs system packages for Docker CLI and cleans apt cache.

## Lines 17-24
- Adds Docker repo key, installs docker CLI/plugins, cleans apt cache.

## Lines 25-32
- Copies orchestrator and observability code plus pyproject.

## Lines 33-40
- Creates __init__ files and installs Python deps via uv/pip.

## Lines 41-48
- Installs observability libs and astor, prepares runtime environment.

## Lines 49-56
- Creates worker user and defines healthcheck to import orchestrator.

## Lines 57-60
- Sets ENTRYPOINT to run Redis stream listener.
