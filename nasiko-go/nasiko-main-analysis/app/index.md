App (Backend) Analysis
======================

Docker and Packaging
--------------------
Dockerfile
- Type: Container build file
- Purpose: Build backend API image.

Dockerfile.k8s-build-worker
- Type: Container build file
- Purpose: Build K8s worker image for cluster deployments.

docker-compose.app.yaml
- Type: Compose stack for backend-only dev.
- Purpose: Run backend + dependencies separately from full stack.

.dockerignore
- Type: Docker ignore patterns for app build context.

pyproject.toml
- Type: Packaging config
- Purpose: Backend dependencies (FastAPI, Mongo, Redis, LangChain, OTEL).

main.py
-------
- Type: FastAPI entrypoint
- Purpose: App initialization, DB setup, router wiring, search init.
- Key logic: Lifespan creates DB client, repository, service, handlers.

pkg/config/config.py
--------------------
- Type: Settings module
- Purpose: Environment configuration (URLs, DBs, K8S flags, OAuth keys).

pkg/auth/__init__.py
pkg/auth/auth_client.py
- Type: Auth integration
- Purpose: Communicate with auth service (JWT validation, access rules).

pkg/redisclient/redisclient.py
- Type: Redis helper
- Purpose: Token storage or shared keys (legacy/simple use).

Adapters
--------
adapters/__init__.py
- Package marker.

adapters/base_adapter.py
- Purpose: Base class for external service adapters.

adapters/nanda_adapter.py
- Purpose: Wrapper for NANDA API endpoints.

Entities and Models
-------------------
entity/entity.py
- Purpose: Core Pydantic models for registry, skills, chat, uploads.

entity/n8n_entity.py
- Purpose: Pydantic models for N8N credentials and workflows.

entity/user_github_credentials_entity.py
- Purpose: Pydantic model for GitHub credentials storage.

Repository Layer (MongoDB)
--------------------------
repository/base_repository.py
- Purpose: Base Mongo repository with common helpers and indexes.

repository/registry_repository.py
- Purpose: Registry CRUD + version history.

repository/agent_operations_repository.py
- Purpose: Agent build and deployment records.

repository/n8n_repository.py
- Purpose: Persist N8N credentials/workflows.

repository/upload_status_repository.py
- Purpose: Track upload states.

repository/chat_repository.py
- Purpose: Chat session and history storage, pagination.

repository/github_repository.py
- Purpose: Store GitHub credential records.

repository/repository.py
- Purpose: Aggregates repositories and ensures indexes.

Service Layer
-------------
service/service.py
- Purpose: Core business logic for registry and user agent operations.

service/agent_operations_service.py
- Purpose: Build/deploy status API operations.

service/agent_update_service.py
- Purpose: Update/rollback agent versions and orchestration triggers.

service/agent_upload_service.py
- Purpose: Validate and process agent upload (zip/dir).

service/agent_upload_tracking_service.py
- Purpose: Track upload progress, trigger orchestration on success.

service/agentcard_service.py
- Purpose: Generate/validate AgentCard data.

service/chat_history_service.py
- Purpose: Manage chat sessions and history retrieval.

service/github_service.py
- Purpose: GitHub OAuth and repo operations.

service/n8n_service.py
- Purpose: N8N API integration.

service/nanda_service.py
- Purpose: Proxy/aggregation over NANDA API.

service/orchestration_service.py
- Purpose: Produce Redis stream events for worker.

service/k8s_service.py
- Purpose: K8s operations for agent deployments.

service/observability_service.py
- Purpose: Phoenix/trace aggregation and stats.

service/redis_search_service.py
- Purpose: Redis-backed search index for users/agents.

API Layer
---------
api/auth.py
- Purpose: JWT validation via auth service.

api/types.py
- Purpose: Shared request/response DTOs for handlers.

api/routes/__init__.py
- Package marker.

api/routes/router.py
- Purpose: Compose FastAPI routers for modules.

api/routes/health_routes.py
- Purpose: Health check endpoints.

api/routes/registry_routes.py
- Purpose: Registry CRUD endpoints.

api/routes/agent_upload_routes.py
- Purpose: Upload and download endpoints.

api/routes/agent_operations_routes.py
- Purpose: Build/deploy status endpoints.

api/routes/agent_update_routes.py
- Purpose: Update/rollback endpoints.

api/routes/github_routes.py
- Purpose: GitHub OAuth and clone endpoints.

api/routes/n8n_routes.py
- Purpose: N8N management endpoints.

api/routes/nanda_routes.py
- Purpose: NANDA proxy endpoints.

api/routes/search_routes.py
- Purpose: Search endpoints for users/agents.

api/routes/chat_history_routes.py
- Purpose: Chat session endpoints.

api/routes/observability_routes.py
- Purpose: Observability endpoints.

api/routes/superuser_routes.py
- Purpose: Superuser creation and management endpoints.

api/handlers/__init__.py
- Purpose: Handler factory wiring.

api/handlers/base_handler.py
- Purpose: Base handler with shared helpers.

api/handlers/health_handler.py
- Purpose: Health logic.

api/handlers/registry_handler.py
- Purpose: Registry orchestration and index updates.

api/handlers/agent_upload_handler.py
- Purpose: Upload logic and orchestration trigger.

api/handlers/agent_operations_handler.py
- Purpose: Build/deploy status logic.

api/handlers/agent_update_handler.py
- Purpose: Update/rollback logic.

api/handlers/github_handler.py
- Purpose: GitHub OAuth operations.

api/handlers/n8n_handler.py
- Purpose: N8N operations.

api/handlers/nanda_handler.py
- Purpose: NANDA proxy handling.

api/handlers/search_handler.py
- Purpose: Search index operations.

api/handlers/chat_history_handler.py
- Purpose: Chat session handling.

api/handlers/observability_handler.py
- Purpose: Observability handler over Phoenix.

api/handlers/traces_handler.py
- Purpose: Trace retrieval support (not wired in factory).

Init Scripts
------------
init-scripts/mongo/01-setup.js
- Type: Mongo init JS
- Purpose: Initialize Mongo DB user/permissions on startup.

Observability Utilities
-----------------------
utils/observability/__init__.py
- Package marker.

utils/observability/config.py
- Purpose: Observability config flags and defaults.

utils/observability/tracing_utils.py
- Purpose: OpenTelemetry / Phoenix tracing helpers.

utils/observability/injector.py
- Purpose: AST-based injection of tracing into agent code.

AgentCard Generator
-------------------
utils/agentcard_generator/README.md
- Purpose: Explain AgentCard generation tooling.

utils/agentcard_generator/ARCHITECTURE.md
- Purpose: Design and internal architecture for generator.

utils/agentcard_generator/requirements.txt
- Purpose: Minimal deps for generator.

utils/agentcard_generator/cli.py
- Purpose: CLI entry for generator.

utils/agentcard_generator/agent.py
- Purpose: Generator core logic.

utils/agentcard_generator/tools.py
- Purpose: Helper utilities for generation.

utils/agentcard_generator/generate_agentcard.sh
- Purpose: Shell wrapper for generator.

utils/agentcard_generator/__init__.py
- Package marker.

Agent Template (Webhook)
------------------------
utils/templates/a2a-webhook-agent/Dockerfile
- Purpose: Build webhook agent image.

utils/templates/a2a-webhook-agent/AgentCard.json
- Purpose: Template AgentCard for webhook agent.

utils/templates/a2a-webhook-agent/pyproject.toml
- Purpose: Template dependencies (a2a-sdk, httpx, uvicorn).

utils/templates/a2a-webhook-agent/README.md
- Purpose: Usage docs for webhook agent template.

utils/templates/a2a-webhook-agent/.gitignore
- Purpose: Template ignore rules.

utils/templates/a2a-webhook-agent/docker-compose.yml
- Purpose: Local run config for webhook agent.

utils/templates/a2a-webhook-agent/src/__init__.py
- Purpose: Package marker.

utils/templates/a2a-webhook-agent/src/__main__.py
- Purpose: Entry point; run A2A app with webhook executor.

utils/templates/a2a-webhook-agent/src/webhook_agent.py
- Purpose: HTTP client to external webhook; parse responses.

utils/templates/a2a-webhook-agent/src/webhook_agent_executor.py
- Purpose: A2A executor; maps A2A requests to webhook calls.
