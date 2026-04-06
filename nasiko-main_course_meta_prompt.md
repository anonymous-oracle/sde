# Nasiko Go Control Plane Course Meta Prompt

## Role
You are a senior staff engineer and curriculum designer. You will produce a complete, detailed course that teaches how to build an AI agent control plane similar to the Nasiko project, but implemented in Go.

## Objective
Create a comprehensive course plan that explains architecture, data flows, and implementation details for a Go-based AI agent control plane with:
- API gateway and service discovery
- Agent registry and upload pipeline
- LLM-based routing and vector search
- Observability and tracing
- Orchestration for Docker and Kubernetes
- CLI for operators
- Sample agents following an Agent-to-Agent protocol

## Audience
Intermediate backend engineers who know Go basics, HTTP APIs, and Docker, but are new to agent orchestration platforms and LLM routing.

## Output requirements
Produce a course in Markdown that includes:
- A short course overview and outcomes
- Prerequisites and setup requirements
- A module-by-module syllabus (12 to 18 modules)
- For each module: goals, concepts, design decisions, key APIs, labs, and deliverables
- Progressive capstone project checkpoints
- A final capstone description and acceptance criteria
- A testing and evaluation plan
- A glossary of required concepts and tools
- Reading and reference links (generic references, no proprietary or secret data)

## Scope to cover (must include)
### Architecture and data flows
- Multi-service control plane layout (gateway, backend, router, auth, chat logging)
- Agent lifecycle flows: upload -> build -> deploy -> registry -> routing
- Event-driven orchestration via Redis streams (or equivalent)
- Chat logging and observability flows

### Core services to implement in Go
- **Gateway**: Kong or Nginx as API gateway, plugin integration, routing rules
- **Backend API**: FastAPI equivalent in Go (Gin/Fiber/Chi), Pydantic equivalent (Go structs + validation)
- **Router**: LLM-based selection using embeddings + reranking + structured output
- **Registry**: Persistent agent metadata in MongoDB (or PostgreSQL if you justify the change)
- **Chat history service**: JSON-RPC log ingestion and query endpoints
- **Orchestrator/Worker**: Redis stream consumer, docker build/run, BuildKit, K8s deploy
- **CLI**: Go-based CLI using Cobra/Viper

### Agent protocol and sample agents
- JSON-RPC 2.0 message/send semantics
- AgentCard schema variations and validation
- A2A-style task tracking, artifacts, and streaming responses
- Tool calling patterns and function schema generation

### Observability and security
- OpenTelemetry tracing across services
- LLM tracing concepts (Phoenix or OpenTelemetry exporters)
- Auth service integration (JWT validation)
- GitHub OAuth flow integration (optional)
- Secret management and config layering

### Infra and deployment
- Docker Compose for local dev
- Kubernetes manifests or Helm chart templates
- Terraform bootstrap for cloud clusters
- BuildKit image builds and registry integration

## Implementation constraints
- Use ASCII-only text and code examples unless strictly necessary
- Be explicit about trade-offs and alternatives
- Explain data contracts between services
- Provide realistic testing strategies for each module

## Suggested technology mapping (Go)
- HTTP: Gin/Fiber/Chi, net/http
- Config: Viper + envconfig
- MongoDB: mongo-go-driver
- Redis streams: go-redis
- Vector search: FAISS via CGO, Qdrant, or pgvector
- LLM: OpenAI Go SDK or HTTP client; structured output using JSON schema
- JSON-RPC: custom handler or existing Go libs
- Docker: Docker Engine API client
- Kubernetes: client-go
- Observability: OpenTelemetry Go SDK
- CLI: Cobra + Viper

## Course structure guidelines
1. Start with a system-level overview and the end-to-end flow.
2. Build the API gateway and backend first.
3. Add registry and storage.
4. Add router and vector store.
5. Add orchestration worker.
6. Add observability and tracing.
7. Add CLI and infra automation.
8. Finish with sample agents and end-to-end tests.

## Deliverables per module
Each module should specify:
- Source files created or modified
- Key structs, interfaces, and data contracts
- Tests to write and how to run them
- Expected runtime behavior and observability signals

## Capstone project
Design a capstone where the learner builds a minimal but complete control plane:
- Uploads an agent, builds it, deploys it, registers with gateway
- Routes a user query to the correct agent with confidence
- Logs chat history and shows traces in an observability UI
- Provides CLI commands for status, upload, and routing tests

## Evaluation rubric
Define pass/fail criteria for:
- API correctness and auth
- Orchestrator reliability and idempotency
- Routing accuracy and fallback behavior
- Observability completeness
- Infrastructure automation reproducibility

## Finish with a glossary
Include definitions for Redis Streams, Kong plugins, AgentCard, JSON-RPC, OpenTelemetry, vector search, BuildKit, and LLM routing.
