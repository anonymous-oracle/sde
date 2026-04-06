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
Absolute beginners with **zero programming knowledge** (assume they do not know basic programming concepts). The course must teach them from the ground up until they can implement this project in Go.

## Output requirements
Produce a course in Markdown that includes:
- A short course overview and outcomes
- **Zero-knowledge baseline** assumptions (no programming literacy)
- Prerequisites and setup requirements (hardware, OS, editor, CLI)
- A **core course syllabus** (12 to 18 modules) focused on building the control plane
- **Subcourses** for each tool/package/Go language topic used in the project
- For each module/subcourse: goals, concepts, design decisions, key APIs, labs, and deliverables
- Progressive capstone project checkpoints
- A final capstone description and acceptance criteria
- A testing and evaluation plan
- A glossary of required concepts and tools
- Reading and reference links (generic references, no proprietary or secret data)

## Zero-to-mastery constraint
- Explain every term before use.
- Include a foundations track that teaches: basic computing, file system, CLI, Git, HTTP, JSON, IDE usage, debugging, and core programming concepts (variables, control flow, functions, data structures).
- Include a **full Go language subcourse** from zero to mastery (syntax, types, errors, interfaces, concurrency, testing, modules, build/release).

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

## Subcourse requirements (mandatory)
For **each tool, package, framework, and platform** used in the project, create a **dedicated subcourse** with exhaustive curriculum depth based on how sophisticated its usage is in this repo. Each subcourse must include:
- Prerequisites (from zero)
- Concepts and mental models
- Hands-on labs and mini-projects
- Common pitfalls and debugging strategies
- Assessments and mastery checks

Minimum subcourses (expand as needed):
- Go language (full stack fundamentals)
- Git + GitHub
- Docker + Docker Compose
- Kubernetes + Helm
- Terraform (AWS EKS + DigitalOcean DOKS)
- Kong API Gateway + plugins (Lua basics)
- MongoDB (data modeling, indexing)
- Redis (streams, caching)
- OpenTelemetry + Phoenix tracing
- LLM API usage and structured output
- JSON-RPC 2.0 and A2A protocol
- CLI tooling (Cobra, Viper)

## Design and architecture mastery
Include dedicated tracks for:
- **HLD (High-Level Design)** from zero to mastery
- **LLD (Low-Level Design)** from zero to mastery
- **Design patterns** mapped to project components (factory, adapter, repository, mediator, observer, etc.)

Every design topic must include:
- Concept explanation
- UML diagrams
- Mapping to this project’s components
- Exercises that implement the pattern in Go

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

## Deliverable structure
- One **main course** (core control plane build).
- One **subcourse per tool/package/language** with exhaustive depth.
- A **dependency map** showing which subcourses must be completed before each core module.

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
