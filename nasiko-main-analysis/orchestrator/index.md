Orchestrator Analysis
=====================

config.py
---------
- Type: Python config module
- Purpose: Centralizes env-driven configuration for local orchestration.
- Key logic: Docker networks, Redis connection, Kong URL, build paths, delays.
- Inputs/Outputs: Environment variables.

docker_utils.py
---------------
- Type: Python utilities
- Purpose: Docker command helpers and URL construction for agent services.
- Key logic: Shelling out to Docker, network checks, `get_kong_agent_url`.
- Inputs/Outputs: Docker Engine API / CLI.

redis_stream_listener.py
------------------------
- Type: Long-running worker
- Purpose: Consume Redis stream commands and build/deploy agents locally.
- Key logic:
  - `XREADGROUP` on `orchestration:commands`.
  - Build agent Docker image, run container on `agents-net`.
  - Inject tracing (optional) before build.
  - Register agent with backend and auth service.
  - Update upload status via backend API.
- Inputs/Outputs: Redis stream, Docker, backend REST, auth REST.

agent_builder.py
----------------
- Type: Builder and deploy helper
- Purpose: Alternate build/deploy path for agent containers.
- Key logic: Build with Docker/Compose, optional OTEL injection, registry upsert.
- Notes: Not the primary path in the current listener flow.

registry_manager.py
-------------------
- Type: Registry helper
- Purpose: Register agent metadata with backend and auth permissions.
- Key logic: Reads `AgentCard.json`, constructs Kong URL, upserts registry, sets access rules.
- Inputs/Outputs: Backend and auth REST calls.

instrumentation_injector.py
---------------------------
- Type: Code injector
- Purpose: Inject Langtrace/OpenTelemetry instrumentation into agent source before build.
- Key logic: AST-based edits; writes bootstrap module and modifies entrypoints.
- Dependencies: `astor`, `langtrace-python-sdk`, OTEL packages.

superuser_manager.py
--------------------
- Type: Helper class
- Purpose: Create/verify superuser via auth service, persist credentials locally.
- Key logic: Poll auth health, POST create, GET verify, save to `superuser_credentials.json`.

requirements.txt
----------------
- Type: Dependency list
- Purpose: Pin runtime deps for orchestrator worker.
- Key packages: redis, docker, requests, aiohttp, pyyaml, opentelemetry, arize-phoenix, langtrace.
