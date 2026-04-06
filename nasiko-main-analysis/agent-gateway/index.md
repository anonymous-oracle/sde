Agent Gateway Analysis
======================

agent-gateway/README.md
-----------------------
- Type: Documentation
- Purpose: Gateway service overview and local run instructions.

agent-gateway/docker-compose.yml
--------------------------------
- Type: Docker Compose
- Purpose: Standalone stack for Kong, registry, router, chat history.
- Key logic: Postgres for Kong, custom plugin mount, networks.

agent-gateway/start.sh
----------------------
- Type: Shell script
- Purpose: Wrapper to start gateway stack locally.
- Key logic: docker compose up / health waits (see file for exact commands).

plugins/chat-logger/handler.lua
-------------------------------
- Type: Kong Lua plugin
- Purpose: Log JSON-RPC `message/send` traffic to chat history service.
- Key logic: capture request/response, post to `/log-chat` asynchronously.
- Inputs/Outputs: Kong request/response bodies; HTTP POST to chat history.

plugins/chat-logger/schema.lua
------------------------------
- Type: Kong plugin schema
- Purpose: Define plugin config (chat service URL, timeout).

chat-history-service/Dockerfile
-------------------------------
- Type: Container build file
- Purpose: Build chat-history microservice image.

chat-history-service/pyproject.toml
-----------------------------------
- Type: Packaging config
- Purpose: Declares FastAPI + Mongo dependencies.

chat-history-service/main.py
----------------------------
- Type: FastAPI service
- Purpose: Ingest chat logs, query chat history by session.
- Key logic: Parses JSON-RPC messages, inserts into Mongo, health check.

registry/requirements.txt
-------------------------
- Type: Dependency list
- Purpose: FastAPI + requests + docker + kubernetes + pydantic.

registry/Dockerfile
-------------------
- Type: Container build file
- Purpose: Build Kong registry service image.

registry/registry.py
--------------------
- Type: FastAPI service + scheduler
- Purpose: Discover agents (Docker/K8s), register Kong services/routes/plugins.
- Key logic: Periodic `sync_services`, static proxy registration, stale cleanup.

router/Dockerfile
-----------------
- Type: Container build file
- Purpose: Build router service image.

router/pyproject.toml
---------------------
- Type: Poetry config
- Purpose: Router dependencies (FastAPI, LangChain, FAISS, OpenAI).

router/README.md
----------------
- Type: Documentation
- Purpose: Router usage and API examples.

router/.gitignore
-----------------
- Type: VCS ignore rules (router-specific).

router/__init__.py
------------------
- Type: Package marker.

router/src/__init__.py
----------------------
- Type: Package marker.

router/src/main.py
------------------
- Type: FastAPI app
- Purpose: Router entrypoint; `/router` streaming endpoint.
- Key logic: Validates inputs, calls `RouterOrchestrator`.

router/src/config/__init__.py
-----------------------------
- Type: Package marker.

router/src/config/settings.py
-----------------------------
- Type: Config module
- Purpose: Router settings and env vars (LLM provider, model, keys).

router/src/core/__init__.py
---------------------------
- Type: Package marker.

router/src/core/agent_client.py
-------------------------------
- Type: HTTP client
- Purpose: Send JSON-RPC `message/send` to agent via Kong.
- Key logic: Rewrites localhost to internal service host in Docker.

router/src/core/agent_registry.py
---------------------------------
- Type: Client + cache
- Purpose: Fetch agent cards from backend registry and cache.

router/src/core/vector_store.py
-------------------------------
- Type: Vector index builder
- Purpose: Build and cache FAISS index from agent descriptions.
- Key logic: OpenAI embeddings, MD5 cache.

router/src/core/routing_engine.py
---------------------------------
- Type: Routing logic
- Purpose: Shortlist via embeddings, rerank, LLM select final agent.
- Key logic: Structured output via Pydantic; fallbacks when similarity low.

router/src/core/session_history.py
----------------------------------
- Type: Client
- Purpose: Fetch chat session history from backend.

router/src/entities/__init__.py
-------------------------------
- Type: Package marker.

router/src/entities/router_entities.py
--------------------------------------
- Type: Pydantic models
- Purpose: Router request/response schemas and LLM structured output.

router/src/services/__init__.py
-------------------------------
- Type: Package marker.

router/src/services/router_orchestrator.py
------------------------------------------
- Type: Orchestration layer
- Purpose: Glue registry, history, routing engine, agent client.
- Key logic: Streaming progress + final response, agent URL selection.

router/src/utils/__init__.py
----------------------------
- Type: Package marker.

router/src/utils/agent_utils.py
-------------------------------
- Type: Helper
- Purpose: Truncate/normalize AgentCards for routing.

router/src/utils/message_utils.py
---------------------------------
- Type: Helper
- Purpose: Build response stream messages and status updates.

router/src/utils/payload_utils.py
---------------------------------
- Type: Helper
- Purpose: Construct JSON-RPC payload for agent calls.

router/src/utils/file_utils.py
------------------------------
- Type: Helper
- Purpose: Parse/format multipart file uploads for router inputs.

router/tests/__init__.py
------------------------
- Type: Test package marker.

router/tests/router_tests.py
----------------------------
- Type: Tests
- Purpose: Router behavior and selection logic tests.

router/tests/router_quality_tests.py
------------------------------------
- Type: Tests
- Purpose: Quality checks and metrics for routing (LLM selection).

router/tests/semantic_search_exps.py
------------------------------------
- Type: Experimental tests
- Purpose: Explore semantic search behavior and thresholds.

router/tests/maf_tests.py
-------------------------
- Type: Tests
- Purpose: Misc router tests (MAF indicates a specific eval variant).

router/tests/test_minimax_provider.py
-------------------------------------
- Type: Tests
- Purpose: MiniMax provider config and routing tests.
