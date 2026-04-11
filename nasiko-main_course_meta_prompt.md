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

## Production-level requirements (mandatory)
Treat the course as if the learner is building a real production system. Include:
- Non-functional requirements (NFRs): reliability, scalability, availability, latency, and cost budgets.
- Explicit SLIs and SLOs per service (API latency, error rates, queue lag, build latency).
- Capacity planning and autoscaling strategy (requests per second, worker pools, rate limits).
- Failure modes and resilience patterns: retries, timeouts, circuit breakers, bulkheads, idempotency.
- Multi-environment workflow: local, dev, staging, prod with config layering and feature flags.
- Change management: versioning, migrations, backward compatibility, and deprecation policy.
- Data lifecycle: schema migrations, indexing, backups, restores, retention, and PII handling.
- Security hardening: RBAC, least privilege, secret rotation, TLS, and audit logging.
- Supply chain security: dependency scanning, SBOMs, image signing, and provenance checks.
- Observability operations: logs, metrics, traces, dashboards, alerting, and runbooks.
- Incident response: on-call procedures, triage flow, and postmortem templates.
- Performance testing: load tests, stress tests, and profiling requirements.
- Cost management: LLM token budgets, caching strategies, and cost attribution by service.

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

## Zero-to-hero topic domains (mandatory)
Include **full zero-to-hero subcourses** for **every domain below**, explicitly mapped to this project’s features:
- **Computer Science Fundamentals**: binary/hex, filesystems, OS/processes, networking basics, concurrency primitives.
- **Programming Fundamentals**: variables, control flow, functions, error handling, testing, debugging.
- **Data Structures**: arrays, lists, stacks, queues, hash maps, trees, graphs.
- **Algorithms**: complexity, searching, sorting, hashing, graph traversal, caching strategies.
- **Mathematics**: basic algebra, probability, linear algebra fundamentals for embeddings.
- **Machine Learning**: supervised/unsupervised, evaluation, embeddings, vector similarity.
- **LLMs**: tokens, prompts, tool calling, structured output, rate limits, safety.
- **MLOps**: model lifecycle, deployment patterns, monitoring, data drift.
- **AIOps**: observability signals, anomaly detection, incident response basics.
- **Orchestration**: queues/streams, schedulers, workflows, idempotency.
- **System Design**: scalability, reliability, fault tolerance, CAP tradeoffs.
- **HLD**: architecture diagrams, service boundaries, data flows.
- **LLD**: API design, data contracts, schemas, module interfaces.
- **Design Patterns**: repository, adapter, factory, strategy, observer, mediator; map each to project components.
- **Software Development**: Git workflows, CI/CD, code review, documentation, testing pyramid.

Each domain subcourse must include:
- Prerequisites (from zero)
- Concept progression (intro → intermediate → advanced)
- Hands-on labs tied to this project
- Assessments and mastery checkpoints

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
- Include operational readiness review (ORR) checklists and go-live criteria
- Require threat modeling and abuse prevention for public endpoints
- Include backward compatibility plans for APIs and AgentCard schema changes

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
9. Add production hardening: security, performance, and disaster recovery.
10. Add operational readiness and release management.

## Deliverable structure
- One **main course** (core control plane build).
- One **subcourse per tool/package/language** with exhaustive depth.
- A **dependency map** showing which subcourses must be completed before each core module.
- A **production operations track** covering runbooks, alerting, incident response, and SRE practices.
- A **release engineering track** covering CI/CD pipelines, staging promotion, and rollback plans.

## Deliverables per module
Each module should specify:
- Source files created or modified
- Key structs, interfaces, and data contracts
- Tests to write and how to run them
- Expected runtime behavior and observability signals
- Dashboards, alerts, and runbooks relevant to the module
- Risk register entries and mitigation steps
- Rollback and recovery steps

## Capstone project
Design a capstone where the learner builds a minimal but complete control plane:
- Uploads an agent, builds it, deploys it, registers with gateway
- Routes a user query to the correct agent with confidence
- Logs chat history and shows traces in an observability UI
- Provides CLI commands for status, upload, and routing tests
- Deploys a staging and production environment with promotion rules
- Runs load tests and demonstrates scalability under traffic
- Demonstrates backup/restore and disaster recovery drill
- Performs a security review and produces an incident response plan

## Evaluation rubric
Define pass/fail criteria for:
- API correctness and auth
- Orchestrator reliability and idempotency
- Routing accuracy and fallback behavior
- Observability completeness
- Infrastructure automation reproducibility
- Production readiness (SLOs met, alerts, runbooks, rollback)
- Security and compliance (RBAC, audit logs, secret handling)
- Performance and cost controls (latency targets, token budgets)

## Finish with a glossary
Include definitions for Redis Streams, Kong plugins, AgentCard, JSON-RPC, OpenTelemetry, vector search, BuildKit, and LLM routing.
