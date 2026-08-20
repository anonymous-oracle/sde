# Nasiko Go Control Plane — Master Curriculum

Single syllabus of record for this course. Every unique topic from the eight source files lives here once.

Teaching brief: `nasiko-instructions.md`.

This is not the ML/LLM/DSP course (`curriculum.md`).

## How to read this file

| Tag | Meaning |
|---|---|
| `CORE` | Destination topics |
| `PREREQ` | Taught first, because CORE depends on them |
| `TOOL` | Platforms and libraries, taught with the matching slice |
| `ARCHIVE` | Kept so nothing is lost; not taught unless a real CORE dependency appears |

Source keys: `GO` go-topics, `SD` sdesign + donnemartin primer, `BP` reconstruction blueprint, `META` course meta prompt, `AN` packed analysis, `PAY` payments addendum, `RULE` nasigo-rules / engine / exercise-rule.

A lesson cites a Go module from §2. Reconstruction work cites a phase from §6 and spec IDs from §7. Algorithms/DS cite §2 blend notes, §2b, or the Nasiko bibliography below.

## Nasiko bibliography `CORE`

Ivy-league / OCW spines for algorithms, data structures, and discrete math. Teach from these; do not invent extra chapter numbers.

- *Algorithms*, 4th ed. — Sedgewick & Wayne (Princeton COS 226 / [algs4.cs.princeton.edu](https://algs4.cs.princeton.edu/)): Ch. 1 fundamentals (union-find, bags/stacks/queues, analysis); Ch. 2 sorting; Ch. 3 searching (BST, red-black, hash ST); Ch. 4 graphs (undirected/directed, MST, shortest paths); Ch. 5 strings (sorts, tries, substring, compression); Ch. 6 context (reductions, maxflow as residual).
- MIT 6.042J / 6.1200J *Mathematics for Computer Science* (OCW): proofs, sets, relations, induction, recurrences, graphs, counting, discrete probability, modular arithmetic, state machines, asymptotics.
- MIT 6.006 *Introduction to Algorithms* (OCW): peak finding, sorting, heaps, BST, hashing, BFS/DFS, Dijkstra, Bellman-Ford, DP (knapsack, alignment), complexity.
- MIT 6.046 *Design and Analysis of Algorithms*: amortized analysis, max flow, NP and what to do — residual §2b unless a Nasiko/contest item needs it.
- Stanford CS161 / Tim Roughgarden *Algorithms Illuminated* I–III (IV for NP): divide-and-conquer, Master theorem, randomized; graphs and DS; greedy, MST, Huffman, DP; APSP and NP.
- Harvard CS124; CLRS (*Introduction to Algorithms*, Cormen et al.) as the reference encyclopedia (cite chapters; do not duplicate a second full ToC here).
- Contest practice: LeetCode / HackerRank / HackerEarth **hard** — implement the DS/algo in Go first, then the platform problem, using only unlocked syntax.

---

# 1. Outcome and inventory

**Outcome.** From zero programming knowledge to implementing and operating a Go control plane (gateway, backend, LLM router + vector search, registry, chat-history, orchestrator/worker, CLI, sample A2A agents) **and** implementing standard algorithms and data structures in Go well enough to solve **hard** problems on LeetCode, HackerRank, HackerEarth, and similar. DS/algo labs are coursework, not the Nasiko capstone.

**Setup (`META`, not assumed)** — a computer that can run Docker; a Unix-like shell or WSL; 16 GB RAM recommended for Compose + a small cluster; disk for images; VS Code or equivalent; Git; a browser. Cloud accounts (AWS and/or DigitalOcean) only when Terraform labs start.

**Target services (`BP`, `META`)**

- API gateway (Kong or Nginx) with custom plugins
- Backend API (Go HTTP: handlers, services, repositories)
- Auth service (JWT issue/validate, users, access rules; backend and CLI call it)
- Router (embeddings, shortlist/rerank, LLM structured selection)
- Registry (Docker/K8s discovery + Kong config)
- Chat history (JSON-RPC ingest + query)
- Orchestrator + build worker (Redis streams, BuildKit, deploy)
- CLI (Cobra/Viper)
- Sample agents (JSON-RPC 2.0 / A2A, AgentCard, tool calling)
- Web UI (compose service only — talks HTTP to the backend; no frontend course; `ARCHIVE` as implementation)

**Stores and infra:** MongoDB; Redis streams/cache; Postgres (Kong); object storage + container registry (ECR/DOCR); BuildKit, Docker, Kubernetes, Terraform.

**Go module mapping**

| Go tree | Legacy Python |
|---|---|
| `go-backend/` | `app/` |
| `go-auth/` | auth service used by `app/pkg/auth` + CLI + superuser |
| `go-router/` | `agent-gateway/router/` |
| `go-registry/` | `agent-gateway/registry/` |
| `go-chat-history/` | `agent-gateway/chat-history-service/` |
| `go-orchestrator/` | `orchestrator/` + `worker/` |
| `go-cli/` | `cli/` |
| `go-agents/` | `agents/` + templates |
| `infra/` | compose, `k8s/`, `terraform/`, Kong |

**End-to-end flow**

1. Upload agent (CLI or API) → registry → build request on Redis stream
2. Orchestrator consumes stream → image build → Docker/K8s deploy
3. Registry discovers the agent → Kong services/routes/plugins
4. Router: query → embeddings → shortlist → LLM picks agent
5. Gateway routes to agent → chat logged → traces emitted

---

# 2. Go language spine `CORE`

Source: `go-topics.md`. Udemy map in parentheses. Named syntax under each module is the unlock list. Do not use an item before its module.

### G0 Orientation and tooling `PREREQ` (Udemy 1–2)

Git, GitHub, SSH. VS Code / editor, extensions. Install Go (Linux/Windows/Mac). Go Playground. `GOROOT`/`GOPATH`/`GOMOD`. `go env`, `go version`. Formatting: vertical openness between distinct ideas, vertical density for related lines, hierarchical indentation.

### G1 Foundations I `CORE` (Udemy 3)

Program layout (`main` package, `func main`). Data types, variables, naming conventions, constants, arithmetic. Control flow: for loops (`for`), `break`/`continue`, `if`/`else`, `switch`. Arrays, blank identifier.

**DS/algo (COS 226 / 6.006 / contest).** 1D arrays, two pointers, prefix sums. Implement in Go; then hard array problems (unlocked syntax only). Discrete math: indexed sequences. Nasiko: byte buffers.

### G2 Foundations II `CORE` (Udemy 3–4)

Slices, maps, `range`. Functions: multiple return, variadic, `defer`, `panic`, `recover`, `init`, closures, recursion. Errors, custom errors. Strings, runes, `fmt`, formatting verbs, string functions, string formatting.

Built-ins that unlock here or in G1: `len`, `cap`, `make`, `append`, `copy`, `delete`, `new`, `panic`, `recover`. Operators `:=`, `*`, `&` unlock with pointers in G3 if not already needed for `make`/`new`.

**DS/algo.** Stacks, queues, deques, bags (algs4 1.3) on slices; sliding window; recursion/backtracking. Hash table as `map` client first. Discrete math: induction on list length. Nasiko: request buffers. Contest: stack/queue/window **hard**.

### G3 Types, interfaces, generics `CORE` (Udemy 4–5)

Pointers. Structs, methods, interfaces, struct embedding, struct tags. Generics. Type conversions.

**DS/algo.** Singly/doubly linked lists; binary trees; BST and balanced BST (red-black, algs4 3.3); binary heap / priority queue; union-find (algs4 1.5; weighted + path compression); hash ST from scratch (chaining and open addressing) — feeds OOD-1. Discrete math: trees as acyclic connected graphs; amortized analysis of union-find (undergraduate depth). Nasiko: registry lookup, timeout heaps. Contest: LL/tree/heap/UF **hard**.

### G4 Files, IO, text, time `CORE`

`bufio`; read/write files; line filters; paths; directories; temp files; `embed`; `io`. Text templates. Regular expressions. Time, epoch, format/parse.

**DS/algo.** Tries; KMP; rolling hash / Rabin–Karp (algs4 Ch. 5; 6.006 strings). Nasiko: AgentCard / query tokens (P5). Contest: string **hard**. Suffix arrays wait for §2b.

### G5 CLI, env, config, logging `CORE`

Command line flags, subcommands. Environment variables. Logging. JSON, XML.

### G6 Concurrency I `CORE` (Udemy 5)

Goroutines. Channels: intro, unbuffered, buffered, synchronization, directions, `select`, non-blocking ops, closing. `context`.

**DS/algo.** Channel as concurrent queue; bounded buffer. Nasiko: worker handoff.

### G7 Concurrency II `CORE` (Udemy 6)

Worker pools. Wait groups, mutexes, atomic counters, `RWMutex`, `sync.NewCond`, `sync.Once`, `sync.Pool`. for-select.

### G8 Rate limiting and performance `CORE`

Token bucket, fixed window, leaky bucket. Sorting. Maps to SDP additional: API rate limiter.

**DS/algo.** Insertion, mergesort, quicksort (randomized — CS161), heapsort; binary search and binary search on a predicate; Master theorem / recurrences with mergesort (6.042 + CS161). Greedy, Huffman, interval scheduling, MST (Kruskal with UF, Prim with heap) — algs4 Ch. 2/4, CS161 part 3. Nasiko: gateway limiter, job scheduling. Contest: sort/search/greedy **hard**.

### G9 Testing, benchmarking, OS, signals, reflection `CORE`

Tests, benchmarks, table tests. OS processes. Signals. Reflection.

**DS/algo.** Asymptotics (big-O, Ω, Θ); loop invariants; proving correctness; empirical timing (algs4 analysis). Dynamic programming: 1D/2D, knapsack, LCS, LIS, alignment (6.006 / CS161 part 3). Discrete probability: hash collisions, randomized quicksort. Contest: DP **hard** only after this unlock.

### G10 Advanced concurrency `CORE` (Udemy 6)

Concurrency vs parallelism. Race detector. Deadlocks.

### G11 Internet and HTTP/TLS `CORE` (Udemy 7)

URL/URI. Request/response cycle. Frontend/client vs backend/API. HTTP 1/2/3. HTTPS, TLS handshake, mTLS.

**DS/algo.** Graphs: adjacency list, BFS, DFS, topological sort, Dijkstra, Bellman-Ford (algs4 Ch. 4; 6.006). Discrete math: graph definitions before code. Nasiko: service discovery graph (P4). Contest: graph **hard**. 0-1 BFS / APSP wait until here or §2b as needed.

### G12 REST API project `CORE` (Udemy 8)

Routing/mux, methods, path/query params. Middleware: security headers, CORS, response time, compression, rate limiter, HPP, ordering. MariaDB/MySQL, SQL CRUD. Env, modeling, validation, pagination. Argon2 hashing. JWT, cookies, sessions. Password update, forgot/reset. CSRF, XSS sanitization. Code obfuscation. API binary. Benchmarking.

Maps to backend capstone service (Chi/Gin/Fiber + `net/http`).

**DS/algo.** LRU/LFU as cache (OOD-2); consistent hashing (5a); modular arithmetic for hashing (6.042). Nasiko: HTTP cache, session store. Contest: design **hard**.

### G13 Protocol Buffers `CORE` (Udemy 9)

Protocol Buffers (protobuf) proto3: packages, messages, field types and field numbers, enums. Serialize/deserialize. RPC. Versioning and backward compatibility. `protoc`. Best practices.

### G14 gRPC core `CORE` (Udemy 10)

Stubs, services. REST vs gRPC. Server/client. TLS. Streaming (server-side, client-side, bidirectional). Metadata, headers, trailers. Postman / gRPCurl. Protoc Gen Validate.

### G15 gRPC API project `CORE` (Udemy 11)

MongoDB/NoSQL CRUD and relationships. Interceptors: response time, rate limiting, authentication, authorization. TLS. GHZ benchmarking. Combo API (REST + gRPC). Generics helpers.

### G16 Observability and profiling `CORE`

OpenTelemetry. pprof. Tracing. Maps to Phoenix / OTEL exporters in the control plane.

### G17 Security and hardening `CORE`

Argon2, JWT, CSRF, XSS, `govulncheck`. Secrets, least privilege, audit logs, rate limits, SLOs, webhook failure budgets.

### G18 Deployment and releases `CORE`

Docker. Cross-compile. GoReleaser.

### G19 Interview prep `CORE` (Udemy 13)

Concurrency, API design, distributed systems. Uses §5 primer problems **and** hard platform DS/algo problems (unlocked set only) as the interview set.

Udemy sections 12 (Resources), 14 (Course Summary), 15 (Best Wishes) are `ARCHIVE` — not taught.

### G20 Payments addendum `CORE` if the capstone charges money

- PG-1 Domain and compliance (rails vs wallets/UPI; auth/capture/settlement; test vs live; PCI DSS; PII; secrets)
- PG-2 Idempotent charges (`Idempotency-Key`; retries; conflict; request-hash store)
- PG-3 Webhooks (signatures Stripe/Razorpay/PayPal; replay windows; skew; nonces; backoff; DLQ)
- PG-4 Ledger (double-entry; conservation; rounding; property tests; idempotent writes)
- PG-5 Refunds, disputes, reversals (full/partial refunds; chargeback life cycle; evidence; ledger adjustments; state machine)
- PG-6 Reconciliation (nightly compare; mismatch classes; alerts)
- PG-7 Security and operations (SLOs; webhook failure budgets)
- PG-8 Regional notes (UPI/QR, netbanking, wallets; payout timelines; sandbox seeding; provider swap by interface and contract tests)

### §2b Contest and theory remainder `CORE`

Only what has no honest home in a G-module or Nasiko phase. Unlock after G9/G11. Hard platform problems that need these wait here.

- NP-completeness, polynomial reductions, P vs NP; what to do (approximation, heuristic, ILP) — Stanford CS161 part 4 / 6.046 / CLRS NP chapters.
- Max flow / min cut, Ford–Fulkerson / Edmonds–Karp — algs4 Ch. 6; 6.046; Harvard CS124. Use if a primer/contest item needs it.
- Fenwick (BIT), segment tree, sparse table — contest range queries.
- Suffix arrays / suffix automata — algs4 Ch. 6 context; beyond G4 tries/KMP.
- Peak finding (6.006) if not already used as a binary-search lab in G8.
- Heavy 6.046 (Fibonacci heaps, van Emde Boas): implement the **idea** only if a hard problem needs it; not a second graduate course.

Each item: invariant + complexity, Go implementation with tests, then one hard platform problem.

---

# 3. Computing baseline `PREREQ`

Zero-knowledge track (`META`). Thin.

- What a computer, process, and file are. Binary/hex at the level needed for bytes and UTF-8.
- Filesystem paths, permissions, environment.
- Terminal: cwd, pipes, exit codes.
- Git add/commit/branch/diff/PR (deepen in G0 / GitHub `TOOL`).
- HTTP verbs, status codes, headers, JSON.
- Editor, debugger, print-debugging.
- Programming ideas before Go syntax: variable, sequence, branch, loop, function, error, test.
- Data structures: array, list, stack, queue, map, tree, graph — vocabulary here; **implement** in G1–G3 (see blend notes).
- Discrete math (6.042 / 6.1200), same slice as the algorithm that needs it: proofs and induction (before recurrences); sets, functions, relations; counting / permutations for hashing; recurrences and Master theorem with mergesort (G8); discrete probability (hash collisions, randomized quicksort, G9); modular arithmetic (hashing, G12); graph definitions before G11 BFS.
- Complexity (big-O, Ω, Θ) at first analysis (G8–G9), not delayed until SDP.
- OS: process vs thread vs goroutine (with G6).
- Networking: IP, port, DNS (with primer DNS topic and G11).

Mathematics for the router only: vectors, dot product, cosine similarity. Supervised vs unsupervised, embeddings, evaluation: thin slices or `curriculum.md`. Tokens, prompts, tool calling, structured output, rate limits, safety: with the router phase.

### 3b Zero-to-hero domain map (`META`)

Folded tracks, not a second spine. Each domain: intro in the cited block, intermediate on the first project use, advanced in the matching P-phase or primer lab.

| Domain | Lives in | Project lab |
|---|---|---|
| Computer science fundamentals | §3, G6, G11 | Process vs goroutine; HTTP request |
| Programming fundamentals | §3, G1–G2, G9 | First tested function |
| Data structures | G1–G4, G8, OOD-1, OOD-2 | From-scratch Go + hard LC/HR/HE |
| Algorithms | G8–G9, G11, P4–P5, §2b | Sort, graph, DP, then residual NP/flow/segtree |
| Discrete mathematics | §3, G3, G8–G9, G11–G12 | Proofs, recurrences, graphs, counting, mod, probability |
| Mathematics | §3 router math | Cosine similarity on two embedding vectors |
| Machine learning | §3 + `curriculum.md` | Embed + evaluate a shortlist |
| LLMs | §4 LLM row, ALG-ROUTE, P5/P9 | Structured pick; tool call |
| MLOps | P5, P10, §9 | Deploy a model-backed router; watch drift as “bad shortlist rate” |
| AIOps | G16, P10, §9 | Trace + alert + incident note |
| Orchestration | G6–G8, P7, JOB-* | Stream consumer, idempotent deploy |
| System design | §5a | Every SDP |
| HLD | §4 HLD, P0–P10 Deep-Dives | Mermaid for the control plane |
| LLD | §7 `API-*` / `SCHEMA-*` | One service contract |
| Design patterns | §4, §5a | Repository and adapter on backend |
| Software development | G0, G9, G18, §9 | PR, test pyramid, CI |

---

# 4. Tool and platform subcourses `TOOL`

Each row is a subcourse. Teach prereqs from zero, concepts, a lab tied to this project, pitfalls, then a mastery check. Depth = how sophisticated the repo’s use is.

**Branched quests:** when a new tool or pattern appears (Redis Streams, a Kong plugin, a vector index), pause the main track, finish that row’s lab, then return.

| Subcourse | Project use | Lab / mastery |
|---|---|---|
| Git + GitHub | Repo, PRs, optional GitHub OAuth (`API-GH-*`) | Commit, branch, PR; OAuth login works |
| Docker + Compose + BuildKit | Local stack; agent images; `JOB-ORCH-001` | Compose up; one agent image builds |
| Kubernetes + Helm + client-go | Deploy agents; registry discovery; worker | Apply a chart; list pods via client-go |
| Terraform | EKS and DOKS bootstrap (`META`) | Plan a cluster; no need to apply until P10 |
| Kong + Lua basics + plugins | Gateway routes; `chat-logger` → `/log-chat` | Route + plugin posts a log |
| Nginx | Allowed alternative to Kong (`BP`, flag) | Same route table if Kong is not used |
| MongoDB | Registry, chat, creds, builds, uploads | Indexes exist; CRUD on SCHEMA-REG-001 |
| Redis | Stream `orchestration:commands`; cache | XADD/XREADGROUP round-trip |
| Postgres | Kong config DB | Kong admin persists a service |
| OpenTelemetry + Phoenix | Cross-service traces; optional agent inject | One request shows a trace |
| Cobra + Viper | Operator CLI | One group with env overlay |
| mongo-go-driver, go-redis, client-go, Docker Engine API | Service clients | Learning tests at each boundary |
| Vector store: Qdrant or pgvector (prefer); FAISS via CGO only if justified | Router | k-NN shortlist returns seeded cards |
| OpenAI-compatible HTTP / official Go SDK | Router + agents; JSON schema structured output | Structured pick parses |
| JSON-RPC 2.0 | Agent protocol + chat logger | `message/send` accepted |
| LLM API usage | Tokens, prompts, tool calling, rate limits, safety | Maps to ALG-ROUTE and agents |
| Ollama | Optional local LLM (`models/`) | 11434 answers when enabled |

Gin / Fiber / Chi + `net/http` for HTTP services. Pydantic equivalent = structs + validation.

### HLD, LLD, and clean architecture `CORE`

Named tracks (`META`). Running example is this control plane. Not a second spine.

- **HLD** — service boundaries, C4/Mermaid, data flows, capacity. Teach with primer 5a and every P0–P10 Deep-Dive.
- **LLD** — API contracts (`API-*`), schemas (`SCHEMA-*`), module interfaces (handler → service → repository), error model.
- **Clean architecture** — dependencies point inward; adapters at Kong, Mongo, Redis, LLM, Docker, K8s; patterns named when they appear (repository, adapter, factory, strategy, observer, mediator).

Resilience (teach with 5a + P10, use in every service): retries, timeouts, circuit breakers, bulkheads, idempotency.

---

# 5. System design track `CORE`

Sources (`SD`): [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) is the mastery set. Support: Alex Xu Vol 1–2, Kleppmann DDIA, Grokking the System Design Interview, official docs for tools in §4.

**Approach (always):** (1) FR/NFR (2) capacity (3) HLD + Mermaid (4) LLD, bottlenecks, failures (5) trade-off table (6) SLOs, observability, security, rollback.

Entry: Harvard scalability lecture; lecloud “Scalability for dummies” (clones, databases, caches, asynchronism). Primer study-guide “long timeline”: all topics, most questions.

These labs are coursework. They are not the Nasiko capstone. Unlock after the cited Go modules.

### 5a Primer topic index `CORE`

Teach every heading, in order. Each is a sub-topic.

1. Performance vs scalability
2. Latency vs throughput
3. Availability vs consistency — CAP; CP; AP
4. Consistency patterns — weak consistency, eventual consistency, strong consistency
5. Availability patterns — active-passive / active-active failover; replication; nines; series vs parallel availability
6. DNS — NS/MX/A/CNAME; TTL; weighted / latency / geo
7. CDN — push vs pull
8. Load balancer — L4 vs L7; session persistence; SSL termination; horizontal vs vertical scaling
9. Reverse proxy — vs load balancer
10. Application layer — microservices; service discovery (Consul/etcd/ZooKeeper ideas; Kong/registry is the project mapping)
11. Database — ACID; master-slave; master-master; federation; sharding; consistent hashing; denormalization; SQL tuning (schema, indexes, joins, partitions, query cache)
12. NoSQL — BASE; key-value; document; wide-column; graph; SQL vs NoSQL
13. Cache — client/CDN/web/DB/app; query vs object; cache-aside; write-through; write-behind; refresh-ahead
14. Asynchronism — message queues; task queues; back pressure; at-least-once vs exactly-once (exactly-once is the design contrast; Redis jobs are at-least-once plus idempotent keys)
15. Communication — TCP; UDP; RPC; REST
16. Security (primer section)
17. Appendix — powers of two; latency numbers every programmer should know

**Phase mapping:** P1 shared libs ↔ communication/errors; P2 data ↔ DB/cache; P3 backend ↔ app layer/REST; P4 registry/gateway ↔ discovery + reverse proxy + LB; P5 router ↔ cache + search; P6 chat ↔ append-only store; P7 orchestrator ↔ queues/back pressure; P8 CLI ↔ API clients; P9 agents ↔ RPC; P10 ↔ nines, failover, SLOs.

Patterns to name when they appear in Nasiko: repository, adapter, factory, strategy, observer, mediator. Clean architecture: handlers → services → repositories; dependencies point inward.

### 5b Official system-design problems — design + implement in Go `CORE`

| ID | Problem | Primer | Unlock after |
|---|---|---|---|
| SDP-1 | Pastebin.com / Bit.ly | `solutions/system_design/pastebin` | G11–G12 |
| SDP-2 | Twitter timeline and search (Facebook feed/search) | `solutions/system_design/twitter` | G12, 5a cache/fan-out |
| SDP-3 | Web crawler | `solutions/system_design/web_crawler` | G6–G7, G11 |
| SDP-4 | Mint.com | `solutions/system_design/mint` | G12, 5a queues |
| SDP-5 | Data structures for a social network | `solutions/system_design/social_graph` | G3, G12 |
| SDP-6 | Key-value store for a search engine | `solutions/system_design/query_cache` | G3, G8 |
| SDP-7 | Amazon sales ranking by category | `solutions/system_design/sales_rank` | G12, 5a cache |
| SDP-8 | Scale to millions of users on AWS | `solutions/system_design/scaling_aws` | G18, §4 K8s/Terraform |

Pass: six-step write-up; Go implementation with tests of the core path; can rebuild from notes; can state every primer trade-off for that problem.

### 5c Official object-oriented design problems — implement in Go `CORE`

| ID | Problem | Unlock after |
|---|---|---|
| OOD-1 | Hash map | G2–G3; from-scratch ST then hard hash problems |
| OOD-2 | LRU cache | G3; feeds 5a cache-aside; LFU variant; design-hard |
| OOD-3 | Call center | G3 interfaces |
| OOD-4 | Deck of cards | G3 |
| OOD-5 | Parking lot | G3 |
| OOD-6 | Chat server | G6, G11–G12; feeds P6 |
| OOD-7 | Circular array (no official primer solution; still implement) | G2 |

### 5d Additional primer questions — same bar `CORE`

One lab when two names are the same system.

| ID | Problem | Notes |
|---|---|---|
| SDP-A1 | File sync (Dropbox) | |
| SDP-A2 | Search engine (Google) | |
| SDP-A3 | Scalable crawler | Same lab as SDP-3; second design write-up if constraints differ |
| SDP-A4 | Google Docs | |
| SDP-A5 | Redis-like key-value store | Related to SDP-6; include expiration + eviction |
| SDP-A6 | Memcached-like cache | Related to OOD-2 |
| SDP-A7 | Amazon recommendations | Thin ML: point at `curriculum.md` for similarity math |
| SDP-A8 | TinyURL / Bitly | Same implementation as SDP-1; design write-up if needed |
| SDP-A9 | Chat (WhatsApp) | Builds on OOD-6 |
| SDP-A10 | Picture sharing (Instagram) | |
| SDP-A11 | Facebook news feed | Related to SDP-2 |
| SDP-A12 | Facebook timeline | |
| SDP-A13 | Facebook chat | Related to OOD-6 / SDP-A9 |
| SDP-A14 | Facebook graph search | Related to SDP-5 |
| SDP-A15 | CDN (CloudFlare-like) | After 5a CDN |
| SDP-A16 | Twitter trending topics | |
| SDP-A17 | Random ID generation (Snowflake) | After G7 atomics |
| SDP-A18 | Top-k requests in a time window | After G8 |
| SDP-A19 | Multi-datacenter serving | After SDP-8 |
| SDP-A20 | Online multiplayer card game | After OOD-4, G6 |
| SDP-A21 | Garbage collector | After G2–G3; industry-competence model, not a production GC |
| SDP-A22 | API rate limiter | After G8; maps to gateway/backend middleware |
| SDP-A23 | Stock exchange | After G7, G12 |

Do not add primer problems that are not on the README.

---

# 6. Reconstruction phases `CORE`

Source: blueprint + packed `plan.phases`. Isolated until §2–§5 (as needed) and §4 tools for that phase are done.

### P0 Foundations

Inputs: workstation, Go toolchain, Docker, kubectl, terraform.  
Steps: monorepo + Go modules; lint/format; Makefile; local dev loop.  
Outputs: repo skeleton.  
Acceptance: `go test ./...` on scaffolding; dev loop documented.  
Deep-dive: what is a system; latency numbers.

### P1 Core platform skeleton

Shared config (env, file, defaults); logging; tracing; error model and HTTP helpers.  
Acceptance: a service boots with config + logs + traces.  
Deep-dive: communication, SLIs.

### P2 Data stores and contracts

Mongo schemas (registry, chat, creds, builds, uploads). Redis stream names, payloads, consumer groups. Kong DB, service/route specs. Migrations, indexes, invariants.  
Acceptance: data-model review.  
Deep-dive: SQL vs document; indexes.

### P3 Backend API

HTTP router, middleware, handlers, services, repositories. JWT validation. Endpoints §7 `API-*`.  
Acceptance: contract tests; auth works.  
Deep-dive: REST, pagination, idempotency.

### P4 Registry and gateway

Discover Docker/K8s agents. Program Kong services, routes, plugins. Health checks; stale cleanup.  
Acceptance: agents appear on the gateway and are routable.  
Deep-dive: service discovery, reverse proxy, L7 routing. **DS/algo:** model agents as a graph; BFS/DFS from G11; union-find for connected components if useful.

### P5 Router

Embeddings; vector store; shortlist; rerank; LLM structured pick.  
Acceptance: routing tests match expected agent.  
Deep-dive: cache, ANN vs exact k-NN, fallbacks. **DS/algo:** heap-select / top-k (SDP-A18); tries for token prefixes (G4).

### P6 Chat history

JSON-RPC ingest; Mongo persist; query + pagination. Kong `chat-logger` → `/log-chat`.  
Acceptance: logs persist and retrieve.  
Deep-dive: append-only, TTL/retention.

### P7 Orchestrator + worker

`XREADGROUP` on `orchestration:commands`. BuildKit/Docker build; push; deploy; registry/status updates. Actions: deploy, update, rebuild, rollback.  
Acceptance: e2e build/deploy completes.  
Deep-dive: queues, at-least-once vs exactly-once, idempotency, back pressure.

### P8 CLI

Command groups §7 `CLI-*`. Local/K8s setup automation.  
Acceptance: operator workflows covered.  
Deep-dive: client retries, config layering.

### P9 Sample agents

A2A JSON-RPC; AgentCard; tool calling; streaming/artifacts. Templates.  
Acceptance: agents accept JSON-RPC and complete a routed turn.  
Deep-dive: RPC vs REST; schema evolution.

### P10 Production hardening

SLOs, dashboards, alerts, runbooks. Load tests, pprof, scaling. Security and supply chain. ORR, rollback, DR drill.  
Acceptance: ORR signed; rollback proven.  
Deep-dive: nines, failover, cost. Retries, timeouts, circuit breakers, bulkheads, idempotency on every public path.

**Capstone acceptance (`META`):** upload → build → deploy → register → route a query with confidence → chat + traces visible → CLI status/upload/route-test → staging and prod with promotion → load test → backup/restore drill → security review + incident plan.

---

# 7. Normalized specs `CORE`

Atomic. Source: packed analysis + module indexes. Ambiguity is flagged.

## 7.1 HTTP API (`go-backend`)

Prefix conventions from `app/api/routes/*`. Auth unless noted.

| ID | Method / path | Behavior |
|---|---|---|
| API-HLTH-001 | GET `/healthcheck` | Liveness; no auth |
| API-UP-001 | POST `/agents/upload` | Zip file; optional `agent_name`; `user_id`; enqueue build |
| API-UP-002 | POST `/agents/upload-directory` | Directory path + `user_id` |
| API-UP-003 | GET upload status | Track `UploadStatus` lifecycle (exact path in handlers; preserve status enum) |
| API-UP-004 | List uploaded | Named by CLI `agent list-uploaded`; keep handler parity |
| API-ACC-001 | Grant user access | CLI `access grant-user` (agent_id, user_ids) |
| API-ACC-002 | Grant agent access | CLI `access grant-agent` (target_agent_ids) |
| API-ACC-003 | List agent access | CLI `access list` |
| API-N8N-003 | N8N credentials get/update | Named by CLI `n8n credentials` / `update`; keep handler parity |
| API-OPS-001 | POST `/agents/build` | Create build record |
| API-OPS-002 | POST `/agents/deploy` | Create deployment record |
| API-OPS-003 | PUT `/agents/build/{build_id}/status` | Worker updates `BuildStatus` + logs |
| API-OPS-004 | PUT `/agents/deployment/{deployment_id}/status` | Worker updates `DeploymentStatus` + `service_url` |
| API-UPD-001 | PUT `/agents/{agent_id}/update` | Optional upload; `version_strategy`; `update_strategy`; `cleanup_old`; `user_id` |
| API-UPD-002 | Rollback / version | Same router family; preserve both if present in handlers |
| API-REG-001 | POST `/registry` | Create registry document (AgentCard-shaped) |
| API-REG-002 | GET `/registry/user/agents` | List agents for user |
| API-CHAT-001 | POST `/chat/session` | Create session (`agent_id`, `agent_url`) |
| API-CHAT-002 | DELETE `/chat/session/{session_id}` | Delete session |
| API-CHAT-003 | GET `/chat/session/list` | Paginate: `limit`, `cursor`, `direction` |
| API-CHAT-004 | GET `/chat/session/{session_id}` | Message history |
| API-GH-001 | GET `/auth/github/login` | OAuth URL |
| API-GH-002 | GET callback | `code`, `state` |
| API-GH-003 | GET `/auth/github/token` | Stored token status |
| API-GH-004 | POST `/auth/github/logout` | Drop token |
| API-N8N-001 | POST `/agents/n8n/register` | Workflow → agent |
| API-N8N-002 | POST `/agents/n8n/connect` | Test then save credentials |
| API-NANDA-001 | GET `/nanda/health` | Adapter health |
| API-NANDA-002 | GET `/nanda/agents` | Filtered list |
| API-SRCH-001 | GET `/search/users` | Prefix / case-insensitive / fuzzy; `q`, `limit` |
| API-OBS-001 | GET session list (observability) | `start_time`; `user_id` |
| API-SU-001 | POST `/user/register` | Superuser-only; proxies auth service `/auth/users/register` |

**Assumption (flagged):** exact remaining sub-routes (list builds, get one agent) exist in handlers; implement from handler names. Do not invent paths that no CLI or route file names.

## 7.2 Chat-history service

| ID | Method / path | Behavior |
|---|---|---|
| API-CH-001 | POST `/log-chat` | Kong plugin; extract user + assistant JSON-RPC parts; insert Mongo |
| API-CH-002 | GET `/chat-history` | By session; ObjectId → string |
| API-CH-003 | GET `/health` | DB ping; 503 if down |

Indexes: `session_id`, `timestamp`. Port in analysis: 8002.

## 7.3 Router

**ALG-ROUTE-001** (meta algorithm spec)

1. Load live AgentCards from registry (fail closed if registry down).
2. Embed the user query with the configured provider (OpenAI-compatible, Minimax, or Ollama).
3. k-NN / ANN shortlist against the vector store (Qdrant or pgvector; FAISS/CGO only if justified).
4. Optional rerank of the shortlist.
5. LLM structured output: agent id + confidence + reason (JSON schema).
6. Fallback if confidence < threshold or LLM errors: return ranked shortlist, or a configured default agent. **Both variants are in the analysis — make policy configurable; default = ranked list, no silent pick. Flag.**
7. Edge cases: empty registry; embed timeout; all scores near zero; agent in index but not on Kong; oversized query.

Config: backend URL, API keys, Minimax/Ollama URLs, provider/model, vector settings, request limits, host/port, CORS, log level.

## 7.3b Auth service `CORE`

First-class service (`META`). Not only middleware.

- Issue and validate JWT. Users and access rules (user↔agent, agent↔agent).
- Backend `pkg/auth` client; CLI login/refresh; orchestrator `superuser_manager` (create/verify superuser, persist `superuser_credentials.json` locally — gitignored).
- Superuser routes proxy `/auth/users/register`.
- **Assumption:** auth may stay a small Go service or sit behind the backend; do not invent a third OAuth provider beyond GitHub optional.

## 7.3c Agent protocol

**PROTO-A2A-001** — JSON-RPC 2.0 `message/send`: jsonrpc, id, method, params (message parts, session/context ids). Errors: parse, invalid request, method not found, invalid params, internal.

**PROTO-A2A-002** — A2A task tracking: submit, working, artifact parts, streaming responses, terminal states.

**PROTO-A2A-003** — AgentCard validation against SCHEMA-REG-001; reject unknown required fields; version the card.

**PROTO-A2A-004** — Tool calling: tools → JSON schema; executor loop; map tool errors to task failure, not a hang.

## 7.4 Registry / Kong sync

Periodic `sync_services`. Discover Docker and/or K8s (`K8S_ENABLED`, `AGENTS_NAMESPACE`). Upsert Kong service + route + plugins. Static proxy registration. Remove stale. Interval: `REGISTRY_INTERVAL`. Admin: `KONG_ADMIN_URL`.

Lua plugin `chat-logger`: on `message/send`, async POST API-CH-001. Config: chat service URL, timeout.

## 7.5 Jobs (Redis)

Stream: `orchestration:commands`.

| ID | Consumer | Fields / actions |
|---|---|---|
| JOB-ORCH-001 | Local listener group | Build image; run on `agents-net`; optional OTEL inject; register backend + auth; update upload status |
| JOB-K8S-001 | Group `k8s-orchestrator` | `command=deploy_agent` or `action` in {`update_agent`, `rollback_agent`, `rebuild_agent`}; BuildKit; push; deploy; status APIs |

At-least-once: idempotent on `(agent_id, version, action)`. ACK after status write succeeds.

## 7.6 Data models

**SCHEMA-REG-001 Registry** — `protocolVersion`, `id`, `name`, `description`, `url`, preferred transport, `Provider` (org, url), `iconUrl`, `version`, `documentationUrl`, `Capabilities`, `securitySchemes`, `security`, `defaultInputModes`, `defaultOutputModes`, `skills[]` (id, name, description, tags, examples), `supportsAuthenticatedExtendedCard`, `signatures`, `additionalInterfaces`, `tags`, owner id, timestamps. DB wrapper adds `_id`.

**SCHEMA-SKILL-001** — skill subdocument as above.

**SCHEMA-UP-001 UploadStatus** — enum lifecycle (queued / building / ready / failed — exact symbols from entity; do not invent extras).

**SCHEMA-BLD-001 AgentBuild** — agent id, status (`BuildStatus`), job name, logs, timestamps, `_id`.

**SCHEMA-DEP-001 AgentDeployment** — id, `agent_id`, `build_id`, namespace, replicas, `DeploymentStatus`, `service_url`, `created_at`.

**SCHEMA-SES-001 Session** — `session_id`, `created_at`, title, `agent_id`, `agent_url`.

**SCHEMA-MSG-001 Message** — role, content, timestamps, metadata (chat service + backend).

**SCHEMA-N8N-001** — n8n credentials and workflows (`entity/n8n_entity.py`).

**SCHEMA-GH-001** — user GitHub credentials.

**Invariants:** registry `id` unique per owner; session belongs to user; build belongs to agent; deployment points at an existing build; chat lines immutable after insert.

## 7.7 Config matrix (non-secret names)

From `app/pkg/config` and orchestrator config. Secrets never stored in git (`.env*` ignored; `*.env.example` allowed; `superuser_credentials.json` ignored).

Mongo user/pass/host/port/db → `MONGO_URI`. Redis host/port/db. Phoenix. OpenAI / Minimax keys + Minimax base URL. BuildKit address. Registry and gateway URLs. DigitalOcean token. `K8S_ENABLED`. `NASIKO_API_URL`. GitHub OAuth client + redirect. Encryption key. Orchestrator: Docker network, Kong URL, agent registry URL/tag, startup delays, agent directory, health timeout.

**Assumption:** `.nasiko-local.env.example` was not read in analysis; treat as the local template and list keys from code references only.

## 7.8 CLI (`go-cli`)

Typer → Cobra groups. Env load order as in `cli/main.py`.

| ID | Group / command | Maps to |
|---|---|---|
| CLI-AGT-001 | `agent upload-zip` | API-UP-001 |
| CLI-AGT-002 | `agent upload-directory` | API-UP-002 |
| CLI-AGT-003 | `agent list-uploaded` | upload list |
| CLI-REG-001 | `registry` list/get | API-REG-* |
| CLI-CHAT-001 | `chat create-session` | API-CHAT-001 |
| CLI-CHAT-002 | `chat list-sessions` | API-CHAT-003 |
| CLI-CHAT-003 | `chat history` | API-CHAT-004 |
| CLI-CHAT-004 | `chat send` | JSON-RPC `message/send` via gateway |
| CLI-GH-001–005 | `github` login/logout/status/repos/clone | API-GH-* |
| CLI-N8N-001–004 | `n8n` register/connect/credentials/update | API-N8N-* |
| CLI-ACC-001–003 | `access` grant-user, grant-agent, list | access APIs |
| CLI-OBS-001 | `observability` session/trace helpers | API-OBS-* |
| CLI-IMG-001 | `images` build/push service images (router, registry, chat-history, auth) | Docker |
| CLI-LOC-001 | `local` compose up/down/ps (requires daemon) | `docker-compose.local.yml` |

## 7.9 Infra

- `docker-compose.local.yml`: Mongo, Redis, Kong+Postgres, backend, router, web, chat-history, registry, worker, superuser job; healthchecks; `agents-net`.
- App-only compose: `docker-compose.app.yaml`.
- Gateway compose: Kong, registry, router, chat-history.
- `Dockerfile.worker` / `app/Dockerfile.k8s-build-worker`.
- Makefile: clean, backend, router, orchestrator, redis-listener. (References `orchestrator/orchestrator.py` — **not in tree**; listener is the real entry. Flag.)
- CI: format + types on `main` and PRs (Go equivalent: `gofmt`/`go vet`/`staticcheck`).
- License: Apache 2.0.
- Models: optional Ollama on 11434; Modelfile `arch-function` from GGUF; `num_ctx 8096`.
- Terraform: AWS EKS + DigitalOcean DOKS (`META`).
- Helm/manifests: agent workloads + control-plane services (P4, P7, P10).

## 7.10 Ops and tests

SLIs (at least): gateway latency, error rate, stream lag, build latency, route confidence/fallback rate, chat ingest success. SLOs set in P10 with numbers from capacity work (5a appendix). Alerts on SLO burn. Runbooks: build fail, registry drift, router fallback storm, Redis lag, Mongo disk. Rollback: JOB-K8S-001 `rollback_agent`. DR: Mongo+Redis backup/restore drill.

Tests: unit (handlers/services with fakes); contract tests per `API-*`; stream integration; e2e upload→route→chat; load (gateway + router); chaos (kill worker, dual consume).

## 7.11 Agents

Sample trees: `a2a-compliance-checker`, `a2a-github-agent`, `a2a-translator` (zips are copies of dirs — ARCHIVE as zip). AgentCard.json; executor; tool schema; JSON-RPC task/artifact/stream. Alternate LangChain path in compliance agent — implement one Go executor; keep LangChain path as ARCHIVE. `policy_agent.py` imported `BaseAgent` missing in tree — **flag**; do not depend on a missing type.

Webhook agent template under `app/utils/templates/a2a-webhook-agent/`. AgentCard generator under `app/utils/agentcard_generator/`.

NANDA adapter: wrap external NANDA HTTP (`adapters/nanda_adapter.py`).

---

# 8. Traceability

302 analyzed files, rolled up. Raw line notes stay in `nasiko-main_reconstruction_blueprint.md` Appendix A and the packed JSON. Do not teach Python line-by-line.

| Legacy tree | Count | Go home | Responsibility |
|---|---|---|---|
| `app/` | 91 | `go-backend/` | HTTP API, entities, repos, services, adapters, OTEL, templates |
| `cli/` | 102 | `go-cli/` | Commands, groups, local/k8s setup, image builds |
| `agents/` | 42 | `go-agents/` | A2A samples + cards + tools |
| `agent-gateway/` | 41 | `go-router/`, `go-registry/`, `go-chat-history/`, `infra/kong` | Router, registry sync, chat service, Lua plugin |
| `orchestrator/` | 8 | `go-orchestrator/` | Local stream consumer, docker build, inject, registry upsert |
| `worker/` | 2 | `go-orchestrator/` (k8s worker cmd) | BuildKit + deploy/rollback |
| `models/` | 3 | `infra/ollama` | Optional local LLM |
| root + `.github` | 12 | `infra/` + CI | Compose, Makefile, license, CI |
| `docs/` | 1 | docs | Indexes |

---

# 9. Production and release `CORE`

Fold into P10; teach ideas when the matching service appears.

NFRs: reliability, scalability, availability, latency, cost. Multi-env: local / dev / staging / prod; config layering; feature flags. Change management: versioning, migrations, compatibility, deprecation (APIs + AgentCard). Data lifecycle: backups, restore, retention, PII. Security: RBAC, least privilege, secret rotation, TLS, audit. Supply chain: scan, SBOM, image sign, provenance. Observability: logs, metrics, traces, dashboards, alerts, runbooks. Incidents: on-call, triage, postmortem. Performance: load, stress, pprof. Cost: LLM token budgets, cache, attribution.

Release: CI/CD, staging promotion, rollback. ORR checklist and go-live criteria. Threat model public endpoints. Evaluation rubric (`META`): API+auth; orchestrator idempotency; routing accuracy + fallback; observability; infra reproducibility; SLOs/alerts/runbooks; RBAC/audit/secrets; latency and token budgets.

---

# 10. Glossary

- **NADT** — dependency tree for a lesson (Go module + phase + locked roots).
- **SUGL** — set of unlocked Go/syntax/concept assets.
- **SYNTAX UNLOCK** — signature, memory model, contrast to Python/Java/C.
- **AgentCard** — agent capability document (SCHEMA-REG-001 shape).
- **JSON-RPC 2.0** — `message/send` and related A2A methods.
- **A2A** — agent-to-agent task/artifact/stream protocol.
- **Redis Streams** — append log; `XREADGROUP`; `orchestration:commands`.
- **Kong plugin** — Lua (or Go) middleware on the gateway; chat-logger is the project example.
- **BuildKit** — image build backend used by the worker.
- **Vector search** — embed query, nearest AgentCards, then LLM rerank/select.
- **LLM routing** — choose an agent from a shortlist with structured output.
- **OpenTelemetry** — traces/metrics/logs; Phoenix is an LLM-trace UI.
- **ORR** — operational readiness review.

---

# 10b. Readings (academic sources)

- donnemartin/system-design-primer (topics + `solutions/` for SDP/OOD)
- Alex Xu, *System Design Interview* Vol 1 and 2
- Martin Kleppmann, *Designing Data-Intensive Applications*
- Grokking the System Design Interview (Educative)
- Official docs: Go, Gin/Fiber/Chi, mongo-go-driver, go-redis, client-go, Kong, Docker, Kubernetes, Terraform, OpenTelemetry, Cobra, Viper
- JSON-RPC 2.0 spec; A2A/AgentCard notes in the analysis indexes
- `nasiko-main_reconstruction_blueprint.md` Appendix A and the packed JSON — lookup only, not a teaching spine
- Sedgewick & Wayne *Algorithms* 4e; Princeton COS 226
- MIT 6.042J / 6.1200J; MIT 6.006; MIT 6.046 (residual)
- Roughgarden *Algorithms Illuminated* I–IV; Stanford CS161
- Harvard CS124; CLRS as encyclopedia
- LeetCode / HackerRank / HackerEarth hard (practice, not a textbook)

# 11. ARCHIVE

Inventory only.

- Appendix A line-by-line Python (“Lines 1–8 …”) and packed `analysis.line_by_line` chunks.
- `uv.lock` full pin lists; use module `pyproject.toml` intent instead.
- Agent `.zip` archives (duplicates of directories).
- `.nasiko-local.env.example` contents (unread by analysis policy).
- Python-only paths: FastAPI/Typer/Pydantic/LangChain/Poetry/PyOxidizer/black/mypy as implementation, not concepts.
- Missing-tree references: `orchestrator/orchestrator.py`; `BaseAgent` import.
- Web UI if present only as a compose service name without Go rewrite requirement — keep as “existing UI talks HTTP to backend”; do not invent a frontend course.
- Udemy sections 12, 14, 15 (resources, summary, best wishes).
- Clean-code Java exception/null wording (intent kept in the brief).
- Engine “5–6 micro-assignments / infinite CS expansion” (superseded by the brief).

---

# 12. Source map

| Source | Where it lives |
|---|---|
| `go-topics.md` 0–20 + named syntax | §2 |
| `sdesign.md` 6-step + books | §5 intro |
| donnemartin primer topics + all listed problems | §5a–5d |
| Meta services, subcourses, production, capstone rubric | §1, §4, §6, §9 |
| Blueprint P0–P10, inventory, flow | §1, §6 |
| Packed JSON / Appendix A facts | §7, §8; raw text ARCHIVE |
| COS 226 / 6.006 / CS161 / 6.042 DS–algo–discrete | §2 blend notes, §2b, §3, Nasiko bibliography |
| `nasigo-rules` / engine / exercise-rule | `nasiko-instructions.md` |
