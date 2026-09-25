Diagrams and Callgraphs
=======================

Overall Architecture
--------------------
```mermaid
flowchart TB
  UI[Web UI / CLI / Desktop] --> Kong[Kong API Gateway]
  Kong --> Backend[FastAPI Backend /api/v1]
  Kong --> Router[Router Service /router]
  Kong --> Auth[Auth Service /auth]
  Kong --> Agents[Agent Containers /agents/*]
  Kong --> N8N[N8N Workflows /n8n]
  Kong --> Web[Web UI /app]

  Backend --> Mongo[(MongoDB)]
  Backend --> Redis[(Redis)]
  Backend --> Auth
  Backend --> Phoenix[Phoenix / OTLP]

  Router --> Backend
  Router --> Agents
  Router --> Vector[(FAISS in-memory)]
  Router --> LLMs[LLM Providers]

  Kong --> ChatSvc[Chat History Service]
  ChatSvc --> Mongo

  Orchestrator[Redis Stream Worker] --> Redis
  Orchestrator --> Docker[Docker / BuildKit]
  Orchestrator --> K8s[Kubernetes]
  Orchestrator --> Backend
  Orchestrator --> Kong
```

Agent Upload and Deployment Flow
--------------------------------
```mermaid
sequenceDiagram
  participant User
  participant CLI
  participant Backend
  participant Redis
  participant Worker
  participant DockerOrK8s
  participant Kong

  User->>CLI: upload agent (zip/dir)
  CLI->>Backend: POST /api/v1/agents/upload
  Backend->>Mongo: write upload status
  Backend->>Redis: XADD orchestration:commands
  Worker->>Redis: XREADGROUP
  Worker->>DockerOrK8s: build + deploy agent
  Worker->>Backend: PUT /api/v1/registry/agent/{name}
  Backend->>Mongo: update registry + versions
  Worker->>Kong: register service + routes
```

Routing Flow (Router Service)
-----------------------------
```mermaid
sequenceDiagram
  participant Client
  participant Kong
  participant Router
  participant Backend
  participant LLM
  participant Agent

  Client->>Kong: /router (query)
  Kong->>Router: forward request
  Router->>Backend: GET /registry/user/agents/info
  Router->>Router: build FAISS + shortlist
  Router->>LLM: structured output (agent_name)
  Router->>Agent: JSON-RPC message/send
  Agent-->>Router: JSON-RPC response
  Router-->>Kong: stream response
```

Chat Logging Flow (Kong Plugin)
-------------------------------
```mermaid
sequenceDiagram
  participant Client
  participant Kong
  participant Agent
  participant Plugin
  participant ChatSvc
  participant Mongo

  Client->>Kong: JSON-RPC message/send
  Kong->>Agent: proxy request
  Agent-->>Kong: response
  Plugin->>ChatSvc: POST /log-chat
  ChatSvc->>Mongo: insert chat records
```

Router Callgraph (Core)
-----------------------
```mermaid
flowchart LR
  main[router/src/main.py] --> orchestrator[router/services/router_orchestrator.py]
  orchestrator --> registry[core/agent_registry.py]
  orchestrator --> session[core/session_history.py]
  orchestrator --> router[core/routing_engine.py]
  router --> vector[core/vector_store.py]
  router --> llm[LangChain ChatOpenAI]
  orchestrator --> client[core/agent_client.py]
```

Orchestrator Flow (Local)
-------------------------
```mermaid
flowchart TD
  A[Redis Stream: orchestration:commands] --> B[redis_stream_listener.py]
  B --> C[copy agent to /tmp/agent-builds]
  C --> D[inject tracing (optional)]
  D --> E[docker build]
  E --> F[docker run on agents-net]
  F --> G[PUT /api/v1/registry/agent/{name}]
  G --> H[register agent permissions with auth]
```
