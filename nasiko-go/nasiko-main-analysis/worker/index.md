Worker Analysis
===============

worker/__init__.py
-----------------
- Type: Python package marker
- Purpose: Declares `worker` as a module for `python -m worker.k8s_build_worker`.

worker/k8s_build_worker.py
--------------------------
- Type: Python service
- Purpose: Kubernetes BuildKit worker consuming Redis streams to build, deploy, update, rollback agents.
- Key logic:
  - Connects to Redis stream `orchestration:commands` with consumer group `k8s-orchestrator`.
  - Branches on `action` (`update_agent`, `rollback_agent`, `rebuild_agent`) or `command` (`deploy_agent`).
  - Uses `K8sService` to build images via BuildKit, push to registry, deploy workloads.
  - Updates backend registry and status via API calls.
- Inputs/Outputs: Redis streams, Kubernetes API, registry endpoints, backend API.
- Dependencies: Redis, Kubernetes client, requests/aiohttp, BuildKit env config.
