# Topic diff: Nasiko master curriculum, Go and ML spines

Source: gcp/unified-curriculum.md lines 3848-4327. Compared against: gcp-lite/index/*.topics.md and gcp-lite/Rust_Track_AI_Infrastructure.md.

Counts: 331 topics; 280 covered, 28 partial, 0 missing, 23 out of scope.

## Nasiko bibliography `CORE`

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Union-find, bags, stacks, queues and analysis (algs4 Ch. 1) | covered | part08_data_structures_algorithms.topics.md › Trees and heaps | - |
| Sorting (algs4 Ch. 2) | covered | part08_data_structures_algorithms.topics.md › Sorting, searching and strings | - |
| BST, red-black and hash symbol tables (algs4 Ch. 3) | covered | part08_data_structures_algorithms.topics.md › Trees and heaps | Balanced search tree in the from-scratch exercises. |
| Graphs, MST and shortest paths (algs4 Ch. 4) | covered | part08_data_structures_algorithms.topics.md › Graph algorithms | - |
| Strings, tries, substring search and compression (algs4 Ch. 5) | covered | part08_data_structures_algorithms.topics.md › Sorting, searching and strings | Trie in the from-scratch exercises; Huffman under Greedy algorithms. |
| Reductions and max flow as residual (algs4 Ch. 6) | covered | part08_data_structures_algorithms.topics.md › Graph algorithms | - |
| Proofs, sets, relations, induction, recurrences, counting, discrete probability, modular arithmetic (6.042) | covered | part03_mathematics.topics.md › Proof and discrete mathematics | - |
| Peak finding, heaps, BFS/DFS, Dijkstra, Bellman-Ford and DP (6.006) | covered | part08_data_structures_algorithms.topics.md › Graph algorithms | - |
| Amortized analysis and NP (6.046) | covered | part08_data_structures_algorithms.topics.md › Analysis | NP reductions under Computability and complexity. |
| Divide-and-conquer and Master theorem (CS161) | covered | part08_data_structures_algorithms.topics.md › Computability and complexity | Master theorem is on a long line, not visible in the grep preview. |
| Greedy, MST, Huffman and APSP (Roughgarden) | covered | part08_data_structures_algorithms.topics.md › Greedy algorithms and dynamic programming | - |
| Contest practice on LeetCode, HackerRank and HackerEarth hard | partial | part04_problem_solving.topics.md › Contest mathematics toolkit | Timed problem families in part08 Exercises; no platform practice. |
| Database systems reading spine (PostgreSQL docs, CMU 15-445, Berkeley CS186) | out of scope | - | Reading list; the topics it teaches are covered in the database rows below. |
| Industry architecture spine (roadmap.sh, Stripe, AWS Builders' Library, OSS repos) | out of scope | - | Reading list and architecture specimens, not topics. |
| ML-system spine references (CS229, CS189, CS224N, CS231n, MIT 18.06/18.01) | out of scope | - | Reading list. |
| Production ML case-study atlas (`MLCASE`) | covered | part27_ml_case_studies_3of5.topics.md › (case-study entries) | Case studies across part25-part29; Slack and Wayfair fraud shown as examples. |

## 0. Knowledge graph and graph-ordered curriculum `CORE`

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Edge types: requires, strengthens, implements, contrasts, revises | out of scope | - | Course-design structure for ordering the course, not a subject topic. |
| Canonical node owners and anti-repetition ledger | out of scope | - | Course-design bookkeeping. |
| Graph theory to graph anomaly detection to fraud pipelines | covered | part19_machine_learning.topics.md › Specialised learning areas | Fraud rings and graph anomaly in Applied problem families. |
| Gradient descent to constrained scheduling to cost-aware serving | covered | part03_mathematics.topics.md › Calculus and optimization | Operations research in part19 Specialised learning areas. |
| Probability and statistics to offline evaluation to A/B tests | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| WAL and replay to outbox and event sourcing to rollback | covered | part13_distributed_systems.topics.md › Distributed transactions | Transactional outbox and inbox; WAL in part12 Recovery and replication. |
| Queues and streams to feature freshness to online inference | covered | part19_machine_learning.topics.md › MLOps | Data and feature platforms cover freshness and streamed features. |
| Stage table S0-S14 (teaching schedule) | out of scope | - | Course schedule, not a subject topic. |

## 1. Outcome and inventory

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Course outcome statement | out of scope | - | Goal statement. |
| Setup: Docker-capable machine, Unix shell or WSL, Git, editor, browser | out of scope | - | Environment setup. |
| API gateway (Kong or NGINX) with custom plugins | covered | part18_devops_sre.topics.md › NGINX and API gateways | - |
| Backend API in Go HTTP (handlers, services, repositories) | covered | part06_programming_languages_go.topics.md › Go — engineering | Frameworks and net/http; repository pattern in part11. |
| Auth service (JWT issue and validate, users, access rules) | covered | part14_security.topics.md › Authentication and sessions | - |
| Router (embeddings, shortlist, rerank, LLM structured selection) | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | Two-stage retrieval; structured output in Prompt, context and output engineering. |
| Registry (Docker and Kubernetes discovery, Kong config) | out of scope | - | Nasiko control-plane service list. |
| Chat history (JSON-RPC ingest and query) | covered | part06_programming_languages_go.topics.md › Go — engineering | JSON-RPC 2.0 served from net/http. |
| Orchestrator and build worker (Redis streams, BuildKit, deploy) | partial | part13_distributed_systems.topics.md › Asynchronism and flow control | Queues and workers covered; Redis streams is a separate missing row. |
| CLI (Cobra and Viper) | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library | - |
| Sample agents (JSON-RPC 2.0, A2A, AgentCard, tool calling) | covered | part22_generative_ai_3of3.topics.md › Agent-to-agent protocol (A2A) | AgentCard fields and validation covered. |
| Web UI (compose service) | out of scope | - | ARCHIVE in the curriculum. |
| Store: MongoDB | covered | part12_databases.topics.md › NoSQL and choosing a store | Go driver in part06 line 129. |
| Store: Redis cache | partial | part06_programming_languages_go.topics.md › Go — the everyday standard library | go-redis client only. |
| Redis streams and consumer groups (orchestrator queue) | partial | part18_devops_sre.topics.md › Observability | Named as a stream-infrastructure bullet with consumer groups and acknowledgement at line 104; not taught as an orchestrator queue. |
| Store: Postgres (Kong plus SQL labs) | covered | part12_databases.topics.md › The SQL language | - |
| Store: object storage and container registry (ECR, DOCR) | partial | part13_distributed_systems.topics.md › System design method | Object storage as an example at line 117; registries named in part24 only. |
| Docker | covered | part18_devops_sre.topics.md › Docker | - |
| BuildKit | covered | part18_devops_sre.topics.md › Docker | Solver DAG and secret mounts. |
| Kubernetes | covered | part18_devops_sre.topics.md › Kubernetes | - |
| Terraform | covered | part18_devops_sre.topics.md › Infrastructure as code | - |
| Go module mapping table | out of scope | - | Nasiko repository layout. |
| End-to-end flow (upload, build, deploy, route, chat) | out of scope | - | Nasiko product flow. |
| TOOLS: Compose | covered | part18_devops_sre.topics.md › Docker | docker compose commands and profiles. |
| TOOLS: Helm | covered | part18_devops_sre.topics.md › Kubernetes | Helm charts under Extending. |
| TOOLS: Kong and NGINX | covered | part18_devops_sre.topics.md › NGINX and API gateways | - |
| TOOLS: OpenTelemetry | covered | part18_devops_sre.topics.md › Observability | Go tracing in part06 line 217. |
| TOOLS: Cobra and Viper | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library | - |
| TOOLS: Gonum | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library | Compared with hand-built primitives. |
| TOOLS: Go ML and runtime adapters (Gorgonia, GoMLX, ONNX Runtime) | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library | - |
| TOOLS: pgvector and Qdrant | covered | part20_generative_ai_1of3.topics.md › Embeddings and retrieval | Qdrant with its Go client. |
| TOOLS: LLM APIs | covered | part21_generative_ai_2of3.topics.md › Model APIs | - |
| TOOLS: Ollama | covered | part21_generative_ai_2of3.topics.md › Model APIs | Modelfiles and GGUF. |

## 2. Concept node details: Go, DS/algo, database internals, and ML systems `CORE`

### G0 Orientation and tooling `PREREQ`

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Git, GitHub and SSH | covered | part15_software_delivery.topics.md › Git | SSH keys and remote access in part10 line 13. |
| Editor and extensions | out of scope | - | Personal tooling preference. |
| Install Go on Linux, Windows and Mac | covered | part06_programming_languages_go.topics.md › Go — toolchain and program structure | - |
| Go Playground | covered | part06_programming_languages_go.topics.md › Go — toolchain and program structure | - |
| GOROOT, GOPATH and GOMOD | covered | part06_programming_languages_go.topics.md › Go — toolchain and program structure | - |
| go env and go version | covered | part06_programming_languages_go.topics.md › Go — toolchain and program structure | - |
| Formatting: vertical openness and density | covered | part06_programming_languages_go.topics.md › Go — toolchain and program structure | gofmt and the vertical density rule. |

### G1 Foundations I `CORE`

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Program layout (main package, func main) | covered | part06_programming_languages_go.topics.md › Go — toolchain and program structure | - |
| Data types, variables, naming conventions, constants and arithmetic | covered | part06_programming_languages_go.topics.md › Go — toolchain and program structure | - |
| Control flow: for, break, continue, if, switch | covered | part06_programming_languages_go.topics.md › Go — toolchain and program structure | - |
| Arrays and blank identifier | covered | part06_programming_languages_go.topics.md › Go — toolchain and program structure | Blank identifier at line 30. |
| 1D arrays, two pointers and prefix sums | covered | part08_data_structures_algorithms.topics.md › Linear structures and techniques | Two pointers, prefix sums and sliding windows named at line 27. |
| Discrete math: indexed sequences | partial | part01_school_foundations.topics.md › Sequences, series and notation | School-level sequences only. |
| Nasiko byte buffers | out of scope | - | Nasiko implementation detail. |

### G2 Foundations II `CORE`

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Slices, maps and range | covered | part06_programming_languages_go.topics.md › Go — composite data, functions, errors and text | - |
| Functions: multiple return, variadic, defer, panic, recover, init, closures, recursion | covered | part06_programming_languages_go.topics.md › Go — composite data, functions, errors and text | init functions at line 24; closures and defer at line 53. |
| Errors and custom errors | covered | part06_programming_languages_go.topics.md › Go — composite data, functions, errors and text | - |
| Strings, runes, fmt, formatting verbs and string functions | covered | part06_programming_languages_go.topics.md › Go — composite data, functions, errors and text | - |
| Built-ins: len, cap, make, append, copy, delete, new | covered | part06_programming_languages_go.topics.md › Go — composite data, functions, errors and text | - |
| Operators := and & | covered | part06_programming_languages_go.topics.md › Go — composite data, functions, errors and text | Short declaration and address-of in the same groups. |
| Stacks, queues, deques, bags on slices | covered | part08_data_structures_algorithms.topics.md › Linear structures and techniques | Stack, queue and deque from scratch. |
| Sliding window and recursion/backtracking | covered | part08_data_structures_algorithms.topics.md › Linear structures and techniques | Recursion and backtracking at line 31. |
| Hash table as a map client | covered | part08_data_structures_algorithms.topics.md › Hashing | - |
| Discrete math: induction on list length | covered | part03_mathematics.topics.md › Proof and discrete mathematics | - |
| Nasiko request buffers | out of scope | - | Nasiko implementation detail. |
| Contest: stack, queue and window hard problems | partial | part08_data_structures_algorithms.topics.md › Linear structures and techniques | Timed family practice only; no platform problem set. |

### G3 Types, interfaces, generics `CORE`

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Pointers | covered | part06_programming_languages_go.topics.md › Go — memory, types with behaviour and generics | - |
| Structs, methods, interfaces, struct embedding and struct tags | covered | part06_programming_languages_go.topics.md › Go — memory, types with behaviour and generics | Embedding and tags at lines 85 and 91. |
| Generics | covered | part06_programming_languages_go.topics.md › Go — memory, types with behaviour and generics | - |
| Type conversions | covered | part06_programming_languages_go.topics.md › Go — toolchain and program structure | Types, constants and conversions group at line 27. |
| Singly and doubly linked lists | covered | part08_data_structures_algorithms.topics.md › Linear structures and techniques | From-scratch exercise. |
| Binary trees, BST and balanced BST (red-black) | covered | part08_data_structures_algorithms.topics.md › Trees and heaps | - |
| Binary heap and priority queue | covered | part08_data_structures_algorithms.topics.md › Trees and heaps | - |
| Union-find with weighted union and path compression | covered | part08_data_structures_algorithms.topics.md › Trees and heaps | - |
| Hash symbol table from scratch (chaining and open addressing) | covered | part08_data_structures_algorithms.topics.md › Hashing | - |
| Trees as acyclic connected graphs; amortized union-find | covered | part08_data_structures_algorithms.topics.md › Trees and heaps | Amortized bound at line 48. |
| Database bridge: tuples, catalog rows and B-tree node structs | covered | part12_databases.topics.md › Storage and access methods | Structs with explicit field widths at line 67. |
| Nasiko registry lookup and timeout heaps | out of scope | - | Nasiko implementation detail. |
| Contest: linked list, tree, heap and union-find hard | partial | part04_problem_solving.topics.md › Contest mathematics toolkit | Same contest-practice gap as the bibliography row. |

### G4 Files, IO, text, time `CORE`

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| bufio, read and write files, line filters | covered | part06_programming_languages_go.topics.md › I/O, files, text, time and JSON | bufio.Scanner and bufio.Writer at line 112; temp-file writes at line 119. |
| Paths, directories, temp files, io, embed | covered | part06_programming_languages_go.topics.md › I/O, files, text, time and JSON | os files, filepath and embed at line 113. Temp files not named. |
| Text templates | covered | part06_programming_languages_go.topics.md › I/O, files, text, time and JSON | text/template versus html/template at line 114. |
| Regular expressions | covered | part06_programming_languages_go.topics.md › I/O, files, text, time and JSON | Named on long line 115. |
| Time, epoch and format/parse | covered | part06_programming_languages_go.topics.md › I/O, files, text, time and JSON | time package at line 116. Epoch not named. |
| Tries | covered | part08_data_structures_algorithms.topics.md › Exercises | Trie from scratch. |
| KMP | covered | part08_data_structures_algorithms.topics.md › Sorting, searching and strings | - |
| Rolling hash and Rabin-Karp | covered | part08_data_structures_algorithms.topics.md › Sorting, searching and strings | - |
| Binary file layout, slotted-page encoding, checksums | covered | part12_databases.topics.md › Storage and access methods | Slotted pages and checksum at line 69. |
| WAL-record serialization | covered | part12_databases.topics.md › Recovery and replication | WAL record header and CRC at line 122. |
| Nasiko AgentCard and query tokens | out of scope | - | Nasiko implementation detail. |
| Contest: string problems hard | partial | part04_problem_solving.topics.md › Contest mathematics toolkit | Same contest-practice gap. |
| Suffix arrays (wait for §2b) | covered | part08_data_structures_algorithms.topics.md › Sorting, searching and strings | Suffix arrays at line 62. |

### G5 CLI, env, config, logging `CORE`

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Command-line flags and subcommands | covered | part06_programming_languages_go.topics.md › Command-line programs, configuration and logging | - |
| Environment variables | covered | part06_programming_languages_go.topics.md › Command-line programs, configuration and logging | PORT variable on Cloud Run. |
| Logging | covered | part06_programming_languages_go.topics.md › Command-line programs, configuration and logging | log/slog at line 125. |
| JSON and XML | covered | part06_programming_languages_go.topics.md › I/O, files, text, time and JSON | XML and SOAP concepts in part11 API design. |

### G6 Concurrency I `CORE`

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Goroutines and channels (unbuffered, buffered, directions, closing) | covered | part06_programming_languages_go.topics.md › Go — concurrency | - |
| select, non-blocking operations | covered | part06_programming_languages_go.topics.md › Go — concurrency | Channels and select group. |
| context | covered | part06_programming_languages_go.topics.md › Go — concurrency | - |
| Channel as concurrent queue; bounded buffer | covered | part08_data_structures_algorithms.topics.md › Exercises | Ring buffer with back-pressure. |
| Nasiko worker handoff | out of scope | - | Nasiko implementation detail. |

### G7 Concurrency II `CORE`

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Worker pools | covered | part06_programming_languages_go.topics.md › Go — concurrency | Worker pools, pipelines, fan-out and fan-in at line 164. |
| Wait groups, mutexes, atomic counters, RWMutex | covered | part06_programming_languages_go.topics.md › Go — concurrency | sync group at line 157. |
| sync.NewCond | covered | part06_programming_languages_go.topics.md › Go — concurrency | Cond listed at line 157. |
| sync.Once | covered | part06_programming_languages_go.topics.md › Go — concurrency | Once and OnceFunc at line 157. |
| sync.Pool | covered | part06_programming_languages_go.topics.md › Go — concurrency | When appropriate, line 160. |
| for-select | covered | part06_programming_languages_go.topics.md › Go — concurrency | select group at line 142. |

### G8 Rate limiting and performance `CORE`

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Token bucket, fixed window and leaky bucket | covered | part14_security.topics.md › API abuse | Token bucket also in part06 line 166. |
| Sorting (insertion, mergesort, quicksort, heapsort) | covered | part08_data_structures_algorithms.topics.md › Sorting, searching and strings | - |
| Randomized quicksort analysis (CS161) | covered | part08_data_structures_algorithms.topics.md › Sorting, searching and strings | Expected O(n log n) by indicator variables. |
| Binary search and binary search on a predicate | covered | part08_data_structures_algorithms.topics.md › Sorting, searching and strings | Predicate form at line 57. |
| Master theorem and recurrences with mergesort | covered | part08_data_structures_algorithms.topics.md › Computability and complexity | Long line; see the bibliography row. |
| External merge sort and loser-tree merge | covered | part08_data_structures_algorithms.topics.md › Sorting, searching and strings | Loser tree at line 59. |
| Greedy, Huffman, interval scheduling | covered | part08_data_structures_algorithms.topics.md › Greedy algorithms and dynamic programming | - |
| MST with Kruskal and Prim | covered | part08_data_structures_algorithms.topics.md › Graph algorithms | - |
| Nasiko gateway limiter and job scheduling | out of scope | - | Nasiko implementation detail. |
| Contest: sort, search and greedy hard | partial | part04_problem_solving.topics.md › Contest mathematics toolkit | Same contest-practice gap. |
| SDP additional: API rate limiter | covered | part14_security.topics.md › API abuse | - |

### G9 Testing, benchmarking, OS, signals, reflection `CORE`

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Tests, benchmarks and table tests | covered | part06_programming_languages_go.topics.md › Go — engineering | Testing and benchmarks group. |
| OS processes | covered | part10_operating_systems.topics.md | File-level match; processes covered in the OS part. |
| Signals | covered | part10_operating_systems.topics.md | Signal delivery, SIGTERM then SIGKILL and graceful shutdown at line 26; signal.NotifyContext at part06 line 126. |
| Reflection | covered | part06_programming_languages_go.topics.md › Go — engineering | reflect at line 226. |
| Asymptotics, loop invariants and correctness proofs | covered | part08_data_structures_algorithms.topics.md › Analysis | - |
| Dynamic programming: 1D, 2D, knapsack, LCS, LIS, alignment | covered | part08_data_structures_algorithms.topics.md › Greedy algorithms and dynamic programming | - |
| Discrete probability: hash collisions, randomized quicksort, cache hits | covered | part03_mathematics.topics.md › Probability | Cache-hit reasoning in part12 Storage and access methods. |
| Contest: DP hard | partial | part04_problem_solving.topics.md › Contest mathematics toolkit | Same contest-practice gap. |

### G10 Advanced concurrency `CORE`

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Concurrency versus parallelism | covered | part06_programming_languages_go.topics.md › Go — concurrency | Named at line 138. |
| Race detector | covered | part06_programming_languages_go.topics.md › Go — concurrency | Race detector at line 168. |
| Deadlocks | covered | part06_programming_languages_go.topics.md › Go — concurrency | Global and silent partial deadlocks at line 147. |

### G11 Internet and HTTP/TLS `CORE`

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| URL and URI, request and response cycle, frontend versus backend | covered | part09_networking.topics.md | File-level match. |
| HTTP 1, 2 and 3 | covered | part06_programming_languages_go.topics.md › Go — engineering | h2c and HTTP/2 on Cloud Run; HTTP/3 in part09. |
| HTTPS, TLS handshake, mTLS | covered | part14_security.topics.md › Cryptography | TLS 1.2 versus 1.3 at line 75. |
| Graphs: adjacency list, BFS, DFS, topological sort, Dijkstra, Bellman-Ford | covered | part08_data_structures_algorithms.topics.md › Graph algorithms | - |
| Discrete math: graph definitions before code | covered | part03_mathematics.topics.md › Proof and discrete mathematics | - |
| Nasiko service discovery graph | out of scope | - | Nasiko implementation detail. |
| Contest: graph hard | partial | part04_problem_solving.topics.md › Contest mathematics toolkit | Same contest-practice gap. |
| 0-1 BFS and APSP | partial | part08_data_structures_algorithms.topics.md › Graph algorithms | Floyd-Warshall covered; 0-1 BFS not named. |

### G12 REST API project `CORE`

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Routing, mux, methods, path and query parameters | covered | part06_programming_languages_go.topics.md › Go — engineering | Frameworks and net/http routing. |
| Middleware: security headers, CORS, response time, compression, rate limiter, HPP, ordering | partial | part14_security.topics.md › Web application security | Security headers at line 155 and CORS covered; compression, response time and HPP not named. |
| Postgres-first SQL CRUD, DDL and DML, constraints, NULL and 3VL, joins, grouping, subqueries, CTEs, transactions, indexes, EXPLAIN | covered | part12_databases.topics.md › The SQL language | - |
| Env, modeling, validation, pagination | covered | part06_programming_languages_go.topics.md › Go — engineering | Request validation at line 187; keyset pagination in part12. |
| Argon2 hashing | covered | part06_programming_languages_go.topics.md › Go — engineering | Argon2id at line 239. |
| JWT, cookies and sessions | covered | part14_security.topics.md › Authentication and sessions | - |
| Password update and forgot or reset flows | partial | part14_security.topics.md › Authentication and sessions | Authentication covered; reset flow not checked. |
| CSRF and XSS sanitization | covered | part14_security.topics.md › Web application security | Session-bound CSRF tokens at part06 line 242. |
| Code obfuscation | out of scope | - | Not taught; not a defensible teaching target for the course. |
| API binary | partial | part06_programming_languages_go.topics.md › Go — engineering | Build flags and distroless images covered; the API-binary framing is not named. |
| Benchmarking | covered | part06_programming_languages_go.topics.md › Go — engineering | Benchmarks with b.Loop at line 177. |
| LRU and LFU as cache (OOD-2) | covered | part08_data_structures_algorithms.topics.md › Hashing | - |
| Consistent hashing | covered | part13_distributed_systems.topics.md › Caching at scale | Sharded caches by consistent hashing. |
| Modular arithmetic for hashing | covered | part03_mathematics.topics.md › Proof and discrete mathematics | Fermat and Euler theorems. |
| Keyset pagination, covering indexes and N+1 detection | covered | part12_databases.topics.md › Operating databases | - |
| Nasiko HTTP cache and session store | out of scope | - | Nasiko implementation detail. |
| Contest: design hard | partial | part04_problem_solving.topics.md › Contest mathematics toolkit | Same contest-practice gap. |

### G12b SQL and PostgreSQL internals braid `CORE`

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| DB-1 Relational algebra and SQL semantics (joins, semi and anti joins, bag versus set, NULL and 3VL) | covered | part12_databases.topics.md › Relational theory | Semi and anti joins at line 51. |
| DB-1 Tiny relational algebra evaluator in Go | covered | part12_databases.topics.md › Exercises | Bag relations with NULL logic. |
| DB-2 Catalogs, system columns, types, PK, FK, CHECK and deferred constraints | covered | part12_databases.topics.md › Storage and access methods | Catalog tables and system columns at line 71. |
| DB-2 Schema registry lab and migrations | covered | part12_databases.topics.md › Exercises | Schema registry with constraints. |
| DB-3 Inlined versus materialized CTEs and recursive CTEs | covered | part12_databases.topics.md › The SQL language | Inlined and materialized CTEs at line 56; recursive CTEs at line 56. |
| DB-3 Window frames and LATERAL joins | covered | part12_databases.topics.md › The SQL language | LATERAL at line 49. |
| DB-4 Storage: data directory, forks, FSM, visibility map, page header, line pointers, TOAST | covered | part12_databases.topics.md › Storage and access methods | Relation forks, free-space map and visibility map at line 68; heap pages and TOAST at lines 67-69. |
| DB-4 Slotted-page package with checksums | covered | part12_databases.topics.md › Exercises | Slotted pages with out-of-line storage. |
| DB-5 Buffer pool, pins and refcounts, clock-sweep | covered | part12_databases.topics.md › Storage and access methods | Buffer pool at line 72; clock-sweep lab in Exercises. |
| DB-5 Background writer and checkpointer | covered | part12_databases.topics.md › Storage and access methods | Background writer and checkpointer at line 75. |
| DB-6 B-tree, Lehman-Yao, hash, GIN, GiST and SP-GiST, BRIN, bitmap, index-only, visibility map | covered | part12_databases.topics.md › Storage and access methods | Lehman-Yao at line 77; GIN, GiST, BRIN at line 80. |
| DB-7 Volcano iterator, work_mem, external sort, nested-loop, index, hash and merge joins, aggregation | covered | part12_databases.topics.md › Query processing | Lines 87-90. |
| DB-8 Parser, analyser, rewriter, planner pipeline; pg_statistic; MCV and histograms | covered | part12_databases.topics.md › Query processing | Pipeline at line 94; statistics at line 95. |
| DB-8 Interesting orders | covered | part12_databases.topics.md › Query processing | Selinger optimizer at line 96. |
| DB-8 GEQO and parallel query | partial | part12_databases.topics.md › Query processing | Neither term found in the read text. |
| DB-9 MVCC, snapshots, isolation levels, SSI | covered | part12_databases.topics.md › Transactions and concurrency control | Lines 112-114. |
| DB-9 Locks, deadlocks, HOT, vacuum and XID wraparound | covered | part12_databases.topics.md › Transactions and concurrency control | HOT at line 70; vacuum and wraparound at line 117. |
| DB-9 Wait-for graph deadlock detector | covered | part12_databases.topics.md › Exercises | MVCC simulator with a deadlock detector. |
| DB-10 WAL records, checkpoints, redo and recovery | covered | part12_databases.topics.md › Recovery and replication | Lines 122-123. |
| DB-10 Streaming replication, archiving and PITR | covered | part12_databases.topics.md › Recovery and replication | Lines 124-125. |
| Mastery check per DB slice | out of scope | - | Teaching assessment design. |

### G13 Protocol Buffers `CORE`

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Protobuf proto3: packages, messages, field numbers, enums | covered | part06_programming_languages_go.topics.md › Go — engineering | Field numbers at line 204. |
| Serialize and deserialize; RPC | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Versioning and backward compatibility | covered | part06_programming_languages_go.topics.md › Go — engineering | Reserved fields and compatibility matrix at line 204. |
| protoc and code generation | covered | part06_programming_languages_go.topics.md › Go — engineering | protoc plugins and buf at line 205. |

### G14 gRPC core `CORE`

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Stubs and services; REST versus gRPC | covered | part06_programming_languages_go.topics.md › Go — engineering | Unary and streaming RPCs at line 206. |
| Server-side, client-side and bidirectional streaming | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Metadata, headers and trailers | covered | part06_programming_languages_go.topics.md › Go — engineering | Line 206. |
| TLS for gRPC | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Postman and gRPCurl | covered | part06_programming_languages_go.topics.md › Go — engineering | Line 208. |
| Protoc Gen Validate | covered | part06_programming_languages_go.topics.md › Go — engineering | Line 205. |

### G15 gRPC API project `CORE`

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| MongoDB and NoSQL CRUD and relationships | covered | part12_databases.topics.md › NoSQL and choosing a store | Mongo driver in part06 line 129. |
| Interceptors: response time, rate limiting, authentication, authorization | covered | part06_programming_languages_go.topics.md › Go — engineering | Interceptors at line 206. |
| TLS | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| GHZ benchmarking | covered | part06_programming_languages_go.topics.md › Go — engineering | ghz at line 208. |
| Combo API (REST and gRPC) | partial | part11_software_architecture.topics.md › Exercises | Only the REST and gRPC pair named; no combo service described. |
| Generics helpers | covered | part06_programming_languages_go.topics.md › Go — memory, types with behaviour and generics | - |

### G16 Observability and profiling `CORE`

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| OpenTelemetry | covered | part06_programming_languages_go.topics.md › Go — engineering | OpenTelemetry for Go at line 217. |
| pprof | covered | part06_programming_languages_go.topics.md › Go — engineering | Line 211. |
| Tracing | covered | part06_programming_languages_go.topics.md › Go — engineering | Trace context through context.Context at line 217. |
| Phoenix and OTEL exporters | covered | part18_devops_sre.topics.md › Observability | Observability group. |

### G17 Security and hardening `CORE`

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Argon2, JWT, CSRF, XSS | covered | part14_security.topics.md › Authentication and sessions | Go-specific Argon2 and CSRF in part06 lines 239-242. |
| govulncheck | covered | part06_programming_languages_go.topics.md › Go — engineering | Line 223. |
| Secrets, least privilege and audit logs | covered | part14_security.topics.md › Security management, risk and governance | - |
| Rate limits and SLOs | covered | part18_devops_sre.topics.md › Site reliability engineering | - |
| Webhook failure budgets | partial | part06_programming_languages_go.topics.md › Go — engineering | Webhook signature verification covered (line 252); failure budgets not named. |

### G18 Deployment and releases `CORE`

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Docker | covered | part18_devops_sre.topics.md › Docker | - |
| Cross-compile | covered | part06_programming_languages_go.topics.md › Go — engineering | Build flags and cross-compilation at lines 220-222. |
| GoReleaser | covered | part06_programming_languages_go.topics.md › Go — engineering | Line 224. |

### G19 Interview prep `CORE`

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Concurrency, API design and distributed systems interview questions | partial | part13_distributed_systems.topics.md › System design method | System-design method only; no question bank. |
| Hard platform DS/algo problems (unlocked set) | partial | part04_problem_solving.topics.md › Contest mathematics toolkit | Same contest-practice gap. |

### G20 Payments addendum `CORE` if the capstone charges money

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| PG-1 Payment domain and compliance (rails, wallets and UPI, auth, capture, settlement, test versus live) | covered | part06_programming_languages_go.topics.md › Go — engineering | Payment domain at line 256. |
| PG-2 Idempotent charges and the Idempotency-Key | covered | part06_programming_languages_go.topics.md › Go — engineering | Idempotency named in the payments group. |
| PG-3 Webhooks: signatures, replay windows, skew, DLQ | partial | part06_programming_languages_go.topics.md › Go — engineering | Signature verification and timestamp tolerance at line 252; DLQ not named. |
| PG-4 Ledger: double-entry, conservation, rounding, property tests | covered | part06_programming_languages_go.topics.md › Go — engineering | Double-entry ledger at line 253. |
| PG-5 Refunds, disputes and reversals | covered | part06_programming_languages_go.topics.md › Go — engineering | Bounded partial refunds at line 253; chargeback life cycle and ledger adjustments at line 258. |
| PG-6 Reconciliation | covered | part06_programming_languages_go.topics.md › Go — engineering | Daily reconciliation against settlement reports at line 253. |
| PG-7 Security and operations (SLOs, webhook failure budgets) | partial | part14_security.topics.md › Security management, risk and governance | - |
| PG-8 Regional notes (UPI, netbanking, wallets, provider swap) | covered | part06_programming_languages_go.topics.md › Go — engineering | Line 256 and provider swap behind an interface at line 260. |

### §2b Contest and theory remainder `CORE`

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| NP-completeness, polynomial reductions, P versus NP | covered | part08_data_structures_algorithms.topics.md › Computability and complexity | Lines 95-96. |
| Max flow, min cut, Ford-Fulkerson and Edmonds-Karp | covered | part08_data_structures_algorithms.topics.md › Graph algorithms | Line 75. |
| Fenwick tree, segment tree and sparse table | covered | part08_data_structures_algorithms.topics.md › Trees and heaps | Line 50. |
| Suffix arrays and suffix automata | covered | part08_data_structures_algorithms.topics.md › Sorting, searching and strings | Line 62. |
| Finite automata and weighted finite-state transducers | covered | part08_data_structures_algorithms.topics.md › Computability and complexity | Finite automata at line 100; WFST decoding at line 101. |
| Peak finding | covered | part08_data_structures_algorithms.topics.md › Sorting, searching and strings | Line 58. |
| Fibonacci heaps and van Emde Boas trees (ideas only) | covered | part08_data_structures_algorithms.topics.md › Trees and heaps | Named as ideas at line 51. |

### §2c Mathematics, ML algorithms, and ML-system foundations `CORE`

#### MATH-ML ladder: arithmetic to graduate-level readiness

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| MML-0 Integers, GCD, fractions, ratios, percentages, units | covered | part01_school_foundations.topics.md › Arithmetic and number sense | Units at Units and dimensional reasoning. |
| MML-1 Algebra, polynomials, exponentials, logarithms, relations, functions | covered | part01_school_foundations.topics.md › Algebra | Functions and graphs and Exponents, roots and logarithms. |
| MML-2 Coordinate geometry, distances, slopes and intersections | covered | part01_school_foundations.topics.md › Coordinate geometry of lines, circles and conics | - |
| MML-2 Bounding boxes and IoU | covered | part20_generative_ai_1of3.topics.md › Multimodal models | IoU defined at line 135. |
| MML-3 Vectors, matrices, determinants, rank, eigenvalues | covered | part03_mathematics.topics.md › Linear algebra | - |
| MML-3 Gram-Schmidt, SVD, PCA, low-rank approximation | covered | part03_mathematics.topics.md › Linear algebra | Gram-Schmidt at line 146; power iteration and PCA at lines 147 and 231. |
| MML-4 Limits, derivatives, partial derivatives, gradients, Jacobians, Hessian | covered | part03_mathematics.topics.md › Calculus and optimization | Jacobian at line 168; Hessian at line 169. |
| MML-4 Integrals and first-order ODE intuition, Euler and RK4 | covered | part03_mathematics.topics.md › Calculus and optimization | Euler and RK4 at line 165. |
| MML-5 Conditional probability, Bayes, random variables, distributions | covered | part03_mathematics.topics.md › Probability | - |
| MML-5 Sampling, Monte Carlo, convergence | covered | part03_mathematics.topics.md › Probability | Monte Carlo at line 56. |
| MML-6 Estimators, MLE, confidence intervals, hypothesis tests | covered | part03_mathematics.topics.md › Statistics and experimental design | Fisher information and MLE at line 86. |
| MML-6 Bootstrap, jackknife, power, A/B tests, CUPED | covered | part03_mathematics.topics.md › Statistics and experimental design | Bootstrap and jackknife at line 89; CUPED at line 94. |
| MML-7 Convexity, Lagrange multipliers, KKT, linear programming | covered | part03_mathematics.topics.md › Calculus and optimization | KKT at line 175; LP at line 176. |
| MML-7 SGD, momentum, adaptive optimizers, regularization, coordinate descent | covered | part19_machine_learning.topics.md › Deep learning | Optimizers at line 98; coordinate descent in part03 line 174. |
| MML-7 Hungarian and min-cost assignment | covered | part03_mathematics.topics.md › Calculus and optimization | Hungarian method at line 176. |
| MML-8 Entropy, cross-entropy, KL divergence, mutual information | covered | part03_mathematics.topics.md › Information theory | - |
| MML-8 Perplexity and calibration | covered | part03_mathematics.topics.md › Information theory | Log loss, perplexity and calibration at line 202. |
| MML-9 DAGs, confounding, propensity scores, difference-in-differences, uplift | covered | part19_machine_learning.topics.md › Applied problem families | Causal inference at line 224; uplift at part03 line 101. |
| MML-9 MDPs, contextual bandits, UCB and Thompson sampling | covered | part03_mathematics.topics.md › Decision mathematics | UCB and Thompson at line 225. |
| MML-10 Floating-point error, stable softmax and logsumexp | covered | part03_mathematics.topics.md › Numerical computing | Overflow, log-sum-exp at lines 191. |
| MML-10 PRNG seeding and reproducible tests | covered | part03_mathematics.topics.md › Numerical computing | Seeding at line 195. |
| MML-10 Interpolation, curve fitting, finite differences, integration | covered | part03_mathematics.topics.md › Numerical computing | Lines 193 and 240. |
| MML-11 Convolution, correlation, DFT and FFT | covered | part03_mathematics.topics.md › Signals and sequences | - |
| MML-11 Spectrogram and MFCC; 2D convolution; morphology | partial | part03_mathematics.topics.md › Signals and sequences | Morphology and n-gram perplexity at lines 219-220; 2D convolution at line 241; MFCC and spectrogram not verified. |
| MML-12 Proof habits, convergence, generalization versus optimization | covered | part03_mathematics.topics.md › Proof and discrete mathematics | - |
| MML-12 Conditioning and stability of numerical methods | covered | part03_mathematics.topics.md › Calculus and optimization | Condition number in conjugate gradient at line 179; overflow and stability at line 191. |

#### ML-CORE algorithm spine

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| ML-1 Problem framing, prediction versus ranking versus retrieval, labels, leakage, class imbalance, cold start | covered | part19_machine_learning.topics.md › Applied problem families | Leakage at line 181; cold start at line 184; delayed labels at line 263. |
| ML-1 Feedback loops | covered | part19_machine_learning.topics.md › Applied problem families | Popularity feedback loops at line 185; hidden feedback loops at part19 MLOps line 230. |
| ML-2 Feature engineering: normalization, hashing trick, missing values, train and serve parity | covered | part19_machine_learning.topics.md › Classical machine learning | Hashing trick and encoding at line 70; parity at line 181. |
| ML-3 Evaluation: confusion matrix, precision, recall, F1, ROC and PR-AUC, calibration, MAP, NDCG, MRR | covered | part19_machine_learning.topics.md › Classical machine learning | Lines 62-66. |
| ML-3 Forecast error metrics | covered | part19_machine_learning.topics.md › Applied problem families | Pinball loss and interval coverage at line 203. |
| ML-4 kNN, linear and logistic regression, naive Bayes, LDA and QDA, SVM, GLM, class weights | covered | part19_machine_learning.topics.md › Classical machine learning | Lines 49-57. |
| ML-5 Decision trees, impurity, random forests, boosting, feature importance, monotonic constraints | covered | part19_machine_learning.topics.md › Classical machine learning | Line 58. |
| ML-6 k-means, DBSCAN, GMM and EM, isolation forest, reconstruction-error anomaly scores | covered | part19_machine_learning.topics.md › Classical machine learning | Line 59. |
| ML-6 Robust z-score and MAD detector | covered | part19_machine_learning.topics.md › Classical machine learning | Line 59. |
| ML-7 BM25, embeddings, ANN, collaborative filtering, matrix factorization, two-stage retrieval, learning to rank | covered | part19_machine_learning.topics.md › Applied problem families | Lines 183-188. |
| ML-7 Diversity and fairness in result sets | covered | part19_machine_learning.topics.md › Applied problem families | Diversity and MMR re-ranking at line 185; fairness in Ethics of AI at part19 line 40. |
| ML-8 Unicode, tokenization, edit distance, n-grams, TF-IDF, BM25 | covered | part19_machine_learning.topics.md › Natural language processing foundations | Lines 119-120; edit distance at line 124. |
| ML-8 LLMs, RAG, prompt injection, structured outputs | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | Prompt injection in part14 AI and LLM application threats. |
| ML-8 Grammar and automata constraints for decoding | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech recognition: from HMMs to Kaldi | WFST decoding graph. |
| ML-9 Pixels, 2D convolution, image filters, image embeddings, perceptual hashing, OCR | covered | part19_machine_learning.topics.md › Specialised learning areas | Perceptual hashing at line 151. |
| ML-9 Audio frames, spectrogram and MFCC features, multimodal retrieval | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech science and analysis | - |
| ML-10 Graph features, PageRank, random walks, bipartite graphs, label propagation | covered | part19_machine_learning.topics.md › Specialised learning areas | Line 149. |
| ML-10 Entity resolution: blocking and candidate generation | covered | part19_machine_learning.topics.md › Specialised learning areas | Line 150. |
| ML-11 Moving averages, exponential smoothing, seasonality, quantiles | covered | part19_machine_learning.topics.md › Applied problem families | Trend, seasonality, smoothing and quantile forecasting at lines 201-203. |
| ML-11 Linear programming and assignment scheduling | covered | part19_machine_learning.topics.md › Specialised learning areas | Operations research at line 155. |
| ML-12 Bandits, reinforcement learning and causal inference | covered | part19_machine_learning.topics.md › Specialised learning areas | Lines 160-162; bandits at lines 194-197. |
| ML-12 Off-policy evaluation and propensity weighting | covered | part19_machine_learning.topics.md › Applied problem families | Lines 190 and 196. |
| ML-13 Privacy, abuse resistance, bias and fairness, explanation, human-in-loop review | covered | part19_machine_learning.topics.md › Applied problem families | Responsible AI and fraud review queues; explanation via part20 line 55. |
| ML-14 Tensors, computational graphs, MLP, activations, backprop, optimizers | covered | part19_machine_learning.topics.md › Deep learning | Lines 93-98. |
| ML-14 Attention heads, positional encodings, residual connections, decoder masking | covered | part20_generative_ai_1of3.topics.md › How LLMs work | Residuals and normalization in part19 Deep learning line 97. |

#### ML-SYS production spine from the case-study corpus

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| MLSYS-1 Product and metric framing, north-star metric, guardrails | covered | part19_machine_learning.topics.md › Applied problem families | Case-study method at line 180. |
| MLSYS-2 Data and feature platform: event contracts, batch versus streaming features, point-in-time correctness, feature store | covered | part19_machine_learning.topics.md › MLOps | Lines 231 and 181. |
| MLSYS-3 Training and evaluation pipelines, dataset snapshots, experiment tracking, model registry | covered | part19_machine_learning.topics.md › MLOps | MLflow and ML platforms at lines 244-248. |
| MLSYS-4 Serving: online, batch, cache, fallback, timeout budgets, cost | covered | part19_machine_learning.topics.md › Exercises | Serving with cache and fallback; multi-model endpoints at line 252. |
| MLSYS-5 Experimentation and rollout: A/B tests, holdouts, canary, shadow, rollback | covered | part19_machine_learning.topics.md › MLOps | Traffic split at line 252. |
| MLSYS-6 Monitoring and drift: input and output drift, calibration drift, data quality, freshness | covered | part19_machine_learning.topics.md › MLOps | Monitoring and drift at lines 237-241. |
| MLSYS-6 Bad-shortlist rate monitoring | partial | part19_machine_learning.topics.md › MLOps | Drift and calibration monitored; shortlist-quality monitoring not named. |
| MLSYS-7 Governance and safety: privacy, compliance, threat modeling, prompt injection, audit | covered | part14_security.topics.md › Privacy | Compliance at line 278; AI threats at line 238. |
| MLSYS-8 Scale and cost: hot keys, fan-out, batching, GPUs as remote services, cost per successful decision | covered | part19_machine_learning.topics.md › MLOps | Scale and cost at line 243. |
| MLSYS-9 Case-study synthesis (Stripe Radar, DoorDash, Airbnb, Grab graph anomaly, LinkedIn causal, Uber, Instacart) | covered | part27_ml_case_studies_3of5.topics.md | Case studies across part25-part29. |
| Explanations: SHAP and LIME | partial | part20_generative_ai_1of3.topics.md › How LLMs work | Named as explainability at line 55; case studies use them; no method taught. |

## 3. Computing baseline `PREREQ`

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| What a computer, process and file are | covered | part02_computer_organization.topics.md | File-level match. |
| Binary, hex and UTF-8 | covered | part06_programming_languages_go.topics.md › Go — composite data, functions, errors and text | UTF-8 decoding in range at line 68. |
| Filesystem paths, permissions and environment | covered | part10_operating_systems.topics.md | File-level match. |
| Terminal: cwd, pipes and exit codes | covered | part05_programming_languages_python_and_shell.topics.md › Shell and working with APIs from code | Pipes, redirection and exit codes at line 51. |
| Git add, commit, branch, diff and PR | covered | part15_software_delivery.topics.md › Git | - |
| HTTP verbs, status codes, headers and JSON | covered | part09_networking.topics.md | File-level match; JSON at part06 line 187. |
| Editor, debugger and print-debugging | covered | part05_programming_languages_python_and_shell.topics.md › Python | Debugger run configuration at line 24; Delve at part06 line 215. |
| Programming ideas before syntax (variable, sequence, branch, loop, function, error, test) | covered | part05_programming_languages_python_and_shell.topics.md › Python | Variables and control flow at line 10. |
| Data-structure vocabulary: array, list, stack, queue, map, tree, graph | covered | part08_data_structures_algorithms.topics.md › Analysis | - |
| Discrete math: proofs, induction, sets, functions, relations, counting, recurrences | covered | part03_mathematics.topics.md › Proof and discrete mathematics | - |
| Complexity: big-O, big-Omega and big-Theta | covered | part08_data_structures_algorithms.topics.md › Analysis | - |
| Process versus thread versus goroutine | covered | part10_operating_systems.topics.md | File-level match; goroutines in part06 Go — concurrency. |
| Networking: IP, port, DNS | covered | part09_networking.topics.md | File-level match. |

### 3b Zero-to-hero domain map `META`

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Computer science fundamentals | covered | part02_computer_organization.topics.md | File-level match. |
| Programming fundamentals | covered | part05_programming_languages_python_and_shell.topics.md › Python | - |
| Data structures | covered | part08_data_structures_algorithms.topics.md › Linear structures and techniques | - |
| Algorithms | covered | part08_data_structures_algorithms.topics.md › Graph algorithms | - |
| Discrete mathematics | covered | part03_mathematics.topics.md › Proof and discrete mathematics | - |
| ML mathematics | covered | part03_mathematics.topics.md › Linear algebra | - |
| Database systems | covered | part12_databases.topics.md › The SQL language | - |
| Machine learning | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| LLMs | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Conditional NLP, CV and audio math | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech science and analysis | - |
| MLOps | covered | part19_machine_learning.topics.md › MLOps | - |
| AIOps | partial | part18_devops_sre.topics.md › Observability | Trace, alert and incident practice covered; the term AIOps not named. |
| Orchestration | covered | part13_distributed_systems.topics.md › Distributed transactions | Durable workflow retry state (Temporal-style) at line 69. |
| Distributed systems and resilience | covered | part11_software_architecture.topics.md › Distributed application patterns | Circuit breaker and bulkhead at line 140. |
| System design | covered | part13_distributed_systems.topics.md › System design method | - |
| HLD | covered | part11_software_architecture.topics.md › Architecture documentation | C4 and Mermaid at lines 164-165. |
| LLD | covered | part11_software_architecture.topics.md › API design | - |
| Design patterns | covered | part11_software_architecture.topics.md › Gang of Four patterns | Adapter and Repository at lines 94 and 126. |
| Software development: PR, test pyramid, CI | covered | part15_software_delivery.topics.md › Git | Test pyramid at part15 line 32; CI at part18 CI/CD. |

---

## Missing in this range

None.

## Partial in this range

- Contest practice on LeetCode, HackerRank and HackerEarth hard → part04_problem_solving.topics.md › Contest mathematics toolkit
- Orchestrator and build worker (Redis streams, BuildKit, deploy) → part13_distributed_systems.topics.md › Asynchronism and flow control
- Store: Redis cache → part06_programming_languages_go.topics.md › Go — the everyday standard library
- Redis streams and consumer groups (orchestrator queue) → part18_devops_sre.topics.md › Observability
- Store: object storage and container registry (ECR, DOCR) → part13_distributed_systems.topics.md › System design method
- Discrete math: indexed sequences → part01_school_foundations.topics.md › Sequences, series and notation
- Contest: stack, queue and window hard problems → part08_data_structures_algorithms.topics.md › Linear structures and techniques
- Contest: linked list, tree, heap and union-find hard → part04_problem_solving.topics.md › Contest mathematics toolkit
- Contest: string problems hard → part04_problem_solving.topics.md › Contest mathematics toolkit
- Contest: sort, search and greedy hard → part04_problem_solving.topics.md › Contest mathematics toolkit
- Contest: DP hard → part04_problem_solving.topics.md › Contest mathematics toolkit
- Contest: graph hard → part04_problem_solving.topics.md › Contest mathematics toolkit
- 0-1 BFS and APSP → part08_data_structures_algorithms.topics.md › Graph algorithms
- Middleware: security headers, CORS, response time, compression, rate limiter, HPP, ordering → part14_security.topics.md › Web application security
- Password update and forgot or reset flows → part14_security.topics.md › Authentication and sessions
- API binary → part06_programming_languages_go.topics.md › Go — engineering
- Contest: design hard → part04_problem_solving.topics.md › Contest mathematics toolkit
- DB-8 GEQO and parallel query → part12_databases.topics.md › Query processing
- Combo API (REST and gRPC) → part11_software_architecture.topics.md › Exercises
- Webhook failure budgets → part06_programming_languages_go.topics.md › Go — engineering
- Concurrency, API design and distributed systems interview questions → part13_distributed_systems.topics.md › System design method
- Hard platform DS/algo problems (unlocked set) → part04_problem_solving.topics.md › Contest mathematics toolkit
- PG-3 Webhooks: signatures, replay windows, skew, DLQ → part06_programming_languages_go.topics.md › Go — engineering
- PG-7 Security and operations (SLOs, webhook failure budgets) → part14_security.topics.md › Security management, risk and governance
- MML-11 Spectrogram and MFCC; 2D convolution; morphology → part03_mathematics.topics.md › Signals and sequences
- MLSYS-6 Bad-shortlist rate monitoring → part19_machine_learning.topics.md › MLOps
- Explanations: SHAP and LIME → part20_generative_ai_1of3.topics.md › How LLMs work
- AIOps → part18_devops_sre.topics.md › Observability
