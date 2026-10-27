# Topic diff: Go G0-G20, math-ML and ML-system spines, computing baseline

Source: gcp/unified-curriculum.md lines 4068-4327. Compared against: gcp-lite/index/*.topics.md (parts 01–29).

Counts: 407 rows — covered 353, partial 26, missing 18, out of scope 10.

## G0 Orientation and tooling (Udemy 1–2)

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Git, GitHub and SSH basics | covered | part15_software_delivery.topics.md › Git | - |
| Editor setup and extensions (VS Code) | missing | → suggest part05 | - |
| Installing Go on Linux, Windows and macOS | missing | → suggest part06 | - |
| Go Playground | missing | → suggest part06 | - |
| GOROOT, GOPATH and module environment variables | partial | part06_programming_languages_go.topics.md › Go — toolchain and program structure | GOMOD, GOSUMDB and GOPROXY covered; GOROOT and GOPATH not named |
| go env and go version | covered | part06_programming_languages_go.topics.md › Go — toolchain and program structure | - |
| Formatting for vertical openness and density | partial | part06_programming_languages_go.topics.md › Go — toolchain and program structure | gofmt covered as the layout tool; the vertical layout rules are not taught |

## G1 Foundations I (Udemy 3)

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Program layout with package main and func main | covered | part06_programming_languages_go.topics.md › Go — toolchain and program structure | - |
| Data types, variables, constants and arithmetic | covered | part06_programming_languages_go.topics.md › Go — toolchain and program structure | - |
| Naming conventions | partial | part06_programming_languages_go.topics.md › Go — toolchain and program structure | Package naming covered; identifier conventions not taught |
| Control flow: for, if/else, switch, break and continue | covered | part06_programming_languages_go.topics.md › Go — toolchain and program structure | - |
| Arrays as fixed-length values | covered | part06_programming_languages_go.topics.md › Go — composite data, functions, errors and text | - |
| Blank identifier | missing | → suggest part06 | - |
| Two pointers, prefix sums and sliding windows | covered | part08_data_structures_algorithms.topics.md › Linear structures and techniques | - |
| Discrete math: indexed sequences | partial | part03_mathematics.topics.md › Proof and discrete mathematics | Functions covered; indexed sequences not taught as a concept |
| Nasiko byte buffers | out of scope | - | Nasiko project mapping |

## G2 Foundations II (Udemy 3–4)

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Slices, maps and range loops | covered | part06_programming_languages_go.topics.md › Go — composite data, functions, errors and text | - |
| Functions: multiple returns, variadic parameters and closures | covered | part06_programming_languages_go.topics.md › Go — composite data, functions, errors and text | - |
| defer, panic and recover | covered | part06_programming_languages_go.topics.md › Go — composite data, functions, errors and text | - |
| init functions | covered | part06_programming_languages_go.topics.md › Go — toolchain and program structure | Initialisation order in Packages and visibility |
| Errors and custom error types | covered | part06_programming_languages_go.topics.md › Go — composite data, functions, errors and text | - |
| Strings, runes and fmt formatting verbs | covered | part06_programming_languages_go.topics.md › Go — composite data, functions, errors and text | - |
| Built-ins: len, cap, make, append, copy, delete, new | covered | part06_programming_languages_go.topics.md › Go — composite data, functions, errors and text | - |
| Stacks, queues and deques on slices | covered | part06_programming_languages_go.topics.md › Go — engineering | Data structures in Go; also part08 Linear structures |
| Recursion and backtracking | covered | part08_data_structures_algorithms.topics.md › Linear structures and techniques | - |
| Hash table as a map client | covered | part08_data_structures_algorithms.topics.md › Hashing | - |
| Induction on list length | covered | part03_mathematics.topics.md › Proof and discrete mathematics | - |
| Nasiko request buffers | out of scope | - | Nasiko project mapping |

## G3 Types, interfaces, generics (Udemy 4–5)

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Pointers and the & and * operators | covered | part06_programming_languages_go.topics.md › Go — memory, types with behaviour and generics | - |
| Structs, methods and struct tags | covered | part06_programming_languages_go.topics.md › Go — memory, types with behaviour and generics | - |
| Interfaces and struct embedding | covered | part06_programming_languages_go.topics.md › Go — memory, types with behaviour and generics | - |
| Generics | covered | part06_programming_languages_go.topics.md › Go — memory, types with behaviour and generics | - |
| Type conversions | covered | part06_programming_languages_go.topics.md › Go — toolchain and program structure | - |
| Singly and doubly linked lists | covered | part08_data_structures_algorithms.topics.md › Linear structures and techniques | - |
| Binary search trees and balanced trees | covered | part08_data_structures_algorithms.topics.md › Trees and heaps | Red-black or AVL balancing |
| Binary heap and priority queue | covered | part08_data_structures_algorithms.topics.md › Trees and heaps | - |
| Union-find with union by rank and path compression | covered | part08_data_structures_algorithms.topics.md › Trees and heaps | Weighted union is union by rank |
| Hash table with chaining and open addressing | covered | part08_data_structures_algorithms.topics.md › Hashing | - |
| Trees as acyclic connected graphs | covered | part03_mathematics.topics.md › Proof and discrete mathematics | - |
| Amortized analysis of union-find | partial | part08_data_structures_algorithms.topics.md › Analysis | Amortized cost named in general; union-find potential argument not taught |
| Database tuple, catalog and B-tree node structs | partial | part12_databases.topics.md › Storage and access methods | Heap tuples and B+ trees covered; the Go modelling lab is not taught |
| Nasiko registry lookup and timeout heaps | out of scope | - | Nasiko project mapping |

## G4 Files, IO, text, time

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| bufio readers and scanners | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library | - |
| Reading and writing files, paths and directories | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library | - |
| embed for bundled files | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library | - |
| io.Reader and io.Writer composition | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library | - |
| Text templates | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library | - |
| Regular expressions | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library | RE2 semantics |
| Time, epoch and format/parse | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library | Epoch not named explicitly |
| Tries | covered | part08_data_structures_algorithms.topics.md › Trees and heaps | - |
| KMP string matching | covered | part08_data_structures_algorithms.topics.md › Sorting, searching and strings | - |
| Rabin–Karp rolling hash | covered | part08_data_structures_algorithms.topics.md › Sorting, searching and strings | - |
| Binary file layout, slotted-page encoding and checksums | partial | part12_databases.topics.md › Storage and access methods | Slotted pages named; byte encoding and page checksums not taught |
| WAL-record serialization | partial | part12_databases.topics.md › Recovery and replication | WAL rule named; record format not taught |
| Nasiko AgentCard and query tokens | out of scope | - | Nasiko project mapping |

## G5 CLI, env, config, logging

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Command-line flags and subcommands | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library | - |
| Environment variables | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library | - |
| Logging with log/slog | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library | - |
| JSON encoding and decoding | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library | - |
| XML encoding | missing | → suggest part07 | - |

## G6 Concurrency I (Udemy 5)

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Goroutines | covered | part06_programming_languages_go.topics.md › Go — concurrency | - |
| Channels: unbuffered, buffered, directions and closing | covered | part06_programming_languages_go.topics.md › Go — concurrency | - |
| select and non-blocking channel operations | covered | part06_programming_languages_go.topics.md › Go — concurrency | - |
| context package | covered | part06_programming_languages_go.topics.md › Go — concurrency | - |
| Channel as a concurrent queue and bounded buffer | covered | part06_programming_languages_go.topics.md › Go — concurrency | - |
| Nasiko worker handoff | out of scope | - | Nasiko project mapping |

## G7 Concurrency II (Udemy 6)

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Worker pools | covered | part06_programming_languages_go.topics.md › Go — concurrency | - |
| WaitGroup, Mutex, RWMutex, Once, Cond and Pool | covered | part06_programming_languages_go.topics.md › Go — concurrency | - |
| Atomic counters | covered | part06_programming_languages_go.topics.md › Go — concurrency | - |
| for-select loops | covered | part06_programming_languages_go.topics.md › Go — concurrency | - |

## G8 Rate limiting and performance

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Token bucket rate limiting | covered | part06_programming_languages_go.topics.md › Go — concurrency | golang.org/x/time/rate |
| Leaky bucket and fixed-window limiters | partial | part14_security.topics.md › API abuse | Named in a list of rate-limit algorithms only |
| Sorting algorithms: insertion, merge, quick and heap | covered | part08_data_structures_algorithms.topics.md › Sorting, searching and strings | - |
| Binary search and binary search on a predicate | covered | part08_data_structures_algorithms.topics.md › Sorting, searching and strings | - |
| Master theorem and recurrences | covered | part08_data_structures_algorithms.topics.md › Analysis | - |
| External merge sort with a loser tree | covered | part08_data_structures_algorithms.topics.md › Sorting, searching and strings | - |
| Greedy algorithms: Huffman coding and interval scheduling | covered | part08_data_structures_algorithms.topics.md › Greedy algorithms and dynamic programming | - |
| Minimum spanning trees: Kruskal and Prim | covered | part08_data_structures_algorithms.topics.md › Graph algorithms | - |
| Nasiko gateway limiter and job scheduling | out of scope | - | Nasiko project mapping |

## G9 Testing, benchmarking, OS, signals, reflection

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Tests, benchmarks and table-driven tests | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| OS processes | covered | part10_operating_systems.topics.md › Processes and threads | - |
| Signals | covered | part10_operating_systems.topics.md › Processes and threads | - |
| Reflection | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Asymptotic notation: big-O, Omega and Theta | covered | part08_data_structures_algorithms.topics.md › Analysis | - |
| Loop invariants and correctness proofs | covered | part08_data_structures_algorithms.topics.md › Analysis | - |
| Empirical timing and crossover measurement | covered | part08_data_structures_algorithms.topics.md › Exercises | Reasoning drill: predict the crossover, then measure |
| Dynamic programming: knapsack, LCS, LIS and alignment | covered | part08_data_structures_algorithms.topics.md › Greedy algorithms and dynamic programming | - |
| Birthday bound and hash collision probability | covered | part03_mathematics.topics.md › Probability | - |
| Selectivity estimates and cache-hit reasoning | partial | part12_databases.topics.md › Query processing | Selectivity under uniformity covered; cache-hit probability not taught |

## G10 Advanced concurrency (Udemy 6)

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Concurrency versus parallelism | covered | part06_programming_languages_go.topics.md › Go — concurrency | - |
| Race detector | covered | part06_programming_languages_go.topics.md › Go — concurrency | - |
| Deadlocks | covered | part10_operating_systems.topics.md › Concurrency | - |

## G11 Internet and HTTP/TLS (Udemy 7)

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| URL and URI structure | missing | → suggest part09 | - |
| HTTP request/response cycle | covered | part09_networking.topics.md › HTTP and the web | - |
| Frontend client versus backend API roles | partial | part07_programming_languages_typescript_wire_theory_exercises.topics.md › TypeScript, Node and the web client | Web client covered; the client and server role split is not taught |
| HTTP/1.1, HTTP/2 and HTTP/3 | covered | part09_networking.topics.md › HTTP and the web | - |
| HTTPS and the TLS handshake | covered | part09_networking.topics.md › TLS mechanics | - |
| Mutual TLS (mTLS) | covered | part14_security.topics.md › Cryptography | - |
| Graph definitions (vertices, edges, degrees) | covered | part03_mathematics.topics.md › Proof and discrete mathematics | - |
| Graph adjacency lists, BFS, DFS and topological sort | covered | part08_data_structures_algorithms.topics.md › Graph algorithms | - |
| Dijkstra and Bellman–Ford | covered | part08_data_structures_algorithms.topics.md › Graph algorithms | - |
| 0-1 BFS | covered | part08_data_structures_algorithms.topics.md › Graph algorithms | - |
| All-pairs shortest paths (Floyd–Warshall) | missing | → suggest part08 | - |
| Nasiko service discovery graph | out of scope | - | Nasiko project mapping |

## G12 REST API project (Udemy 8)

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Routing, ServeMux and path parameters | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Middleware chain ordering | covered | part06_programming_languages_go.topics.md › Go — engineering | Includes logging and recover middleware |
| Rate-limiter middleware | covered | part14_security.topics.md › API abuse | 429 with Retry-After; token bucket also in part06 |
| CORS middleware | partial | part14_security.topics.md › Web application security | Same-origin policy and CORS named; no middleware configuration taught |
| Security response headers | partial | part14_security.topics.md › Cryptography | HSTS named only |
| HTTP compression middleware | partial | part09_networking.topics.md › Middleboxes, proxies and load balancing | Compression named as a proxy role; gzip appears only in an exercise |
| HTTP parameter pollution (HPP) | missing | → suggest part14 | - |
| SQL CRUD, DDL and DML | covered | part12_databases.topics.md › The SQL language | - |
| Constraints as an executable specification | covered | part12_databases.topics.md › Relational theory | - |
| Three-valued logic and NULL semantics | covered | part12_databases.topics.md › Pre-SQL foundations | NULL handling also in The SQL language |
| Joins, grouping and subqueries | covered | part12_databases.topics.md › The SQL language | - |
| Common table expressions | covered | part12_databases.topics.md › The SQL language | - |
| Transactions and isolation levels | covered | part12_databases.topics.md › Transactions and concurrency control | - |
| Indexes and access paths | covered | part12_databases.topics.md › Storage and access methods | - |
| Modular arithmetic for hashing | covered | part03_mathematics.topics.md › Proof and discrete mathematics | Number theory group |
| Data modelling for an API | covered | part12_databases.topics.md › Data modelling and design | - |
| Environment configuration | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library | - |
| Request input validation | partial | part06_programming_languages_go.topics.md › Go — engineering | MaxBytesReader covered; validation rules not taught |
| Keyset pagination | covered | part12_databases.topics.md › Operating databases | - |
| Argon2id password hashing | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| JWT, cookies and sessions | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Password change and forgot/reset flows | missing | → suggest part14 | - |
| CSRF tokens | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| XSS sanitization and output encoding | covered | part14_security.topics.md › Web application security | - |
| Code obfuscation | missing | → suggest part14 | - |
| Shipping an API binary | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Nasiko HTTP cache and session store | out of scope | - | Nasiko project mapping |

## G12b SQL and PostgreSQL internals braid

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Relational algebra: selection, projection and joins | covered | part12_databases.topics.md › Relational theory | - |
| Semi-joins and anti-joins | covered | part12_databases.topics.md › The SQL language | - |
| Bag versus set semantics | covered | part12_databases.topics.md › Pre-SQL foundations | - |
| IS DISTINCT FROM | covered | part12_databases.topics.md › The SQL language | - |
| PostgreSQL system catalogs (pg_class, pg_attribute, pg_type, pg_statistic) | missing | → suggest part12 | - |
| System columns ctid, xmin and xmax | partial | part12_databases.topics.md › Transactions and concurrency control | Tuple versioning covered; the system columns are not named |
| Primitive, extended and JSONB types | covered | part12_databases.topics.md › The SQL language | - |
| Range types and UUIDs | covered | part12_databases.topics.md › The SQL language | - |
| Deferred constraints | covered | part12_databases.topics.md › Relational theory | - |
| Migrations and constraint-violation tests | covered | part12_databases.topics.md › Operating databases | - |
| Inlined versus materialized CTEs | covered | part12_databases.topics.md › The SQL language | - |
| Recursive CTE working table | covered | part12_databases.topics.md › The SQL language | - |
| Window frames | covered | part12_databases.topics.md › The SQL language | - |
| Lateral joins | covered | part12_databases.topics.md › The SQL language | - |
| EXPLAIN (ANALYZE, BUFFERS) | covered | part12_databases.topics.md › Query processing | - |
| Heap pages, line pointers and tuple headers | covered | part12_databases.topics.md › Storage and access methods | - |
| TOAST for oversized values | covered | part12_databases.topics.md › Storage and access methods | - |
| Relation forks, free-space and visibility maps, segment files | covered | part12_databases.topics.md › Storage and access methods | - |
| 8 KB page arithmetic | covered | part12_databases.topics.md › Pre-SQL foundations | - |
| Buffer pool with clock-sweep eviction | covered | part12_databases.topics.md › Storage and access methods | Pins, reference counts, bgwriter and checkpointer included |
| Scan resistance and hit-ratio measurement | covered | part12_databases.topics.md › Storage and access methods | - |
| B+ trees and Lehman–Yao right links | covered | part12_databases.topics.md › Storage and access methods | - |
| Hash indexes | covered | part12_databases.topics.md › Storage and access methods | - |
| GIN, GiST, SP-GiST and BRIN indexes | covered | part12_databases.topics.md › Storage and access methods | - |
| Bitmap scans and index-only scans | covered | part12_databases.topics.md › Storage and access methods | - |
| Nasiko AgentCard inverted index | out of scope | - | Nasiko project mapping |
| Volcano iterator model | covered | part12_databases.topics.md › Query processing | - |
| work_mem and external sort spills | covered | part12_databases.topics.md › Query processing | - |
| Nested-loop, hash and merge joins | covered | part12_databases.topics.md › Query processing | - |
| Hash aggregation and set operators | covered | part12_databases.topics.md › Query processing | - |
| Parse, analyze, rewrite and plan pipeline | covered | part12_databases.topics.md › Query processing | - |
| Histograms, most-common values and correlation statistics | covered | part12_databases.topics.md › Query processing | - |
| Selinger dynamic programming and interesting orders | covered | part12_databases.topics.md › Query processing | - |
| Genetic query optimization (GEQO) | covered | part12_databases.topics.md › Query processing | - |
| Parallel query | covered | part12_databases.topics.md › Query processing | - |
| Cost variables such as random_page_cost | covered | part12_databases.topics.md › Query processing | - |
| MVCC tuple versioning and snapshots | covered | part12_databases.topics.md › Transactions and concurrency control | - |
| Isolation levels and anomalies | covered | part12_databases.topics.md › Transactions and concurrency control | - |
| Serializable snapshot isolation | covered | part12_databases.topics.md › Transactions and concurrency control | - |
| Lightweight versus heavyweight locks | covered | part12_databases.topics.md › Transactions and concurrency control | - |
| Deadlock detection with a waits-for graph | covered | part12_databases.topics.md › Transactions and concurrency control | - |
| HOT updates | covered | part12_databases.topics.md › Storage and access methods | - |
| Autovacuum and transaction-ID wraparound | covered | part12_databases.topics.md › Transactions and concurrency control | - |
| WAL rule (write-ahead logging) | covered | part12_databases.topics.md › Recovery and replication | - |
| Steal and no-force buffer policies | covered | part12_databases.topics.md › Recovery and replication | - |
| ARIES redo and undo passes | covered | part12_databases.topics.md › Recovery and replication | - |
| Checkpoints, full-page writes and synchronous commit | covered | part12_databases.topics.md › Recovery and replication | - |
| Physical streaming replication and WAL archiving | covered | part12_databases.topics.md › Recovery and replication | - |
| Point-in-time recovery | covered | part12_databases.topics.md › Recovery and replication | - |
| Replica lag as a service-level indicator | covered | part12_databases.topics.md › Recovery and replication | - |

## G13 Protocol Buffers (Udemy 9)

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| proto3 messages, packages, field numbers and enums | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Protobuf wire format and serialization | covered | part07_programming_languages_typescript_wire_theory_exercises.topics.md › Wire formats | - |
| Protobuf schema evolution and backward compatibility | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| protoc code generation | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| RPC as a call abstraction | covered | part11_software_architecture.topics.md › API design | - |

## G14 gRPC core (Udemy 10)

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Service stubs and service definitions | covered | part11_software_architecture.topics.md › API design | - |
| REST versus gRPC | covered | part11_software_architecture.topics.md › API design | - |
| gRPC unary and streaming RPCs | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| gRPC metadata, headers and trailers | partial | part06_programming_languages_go.topics.md › Go — engineering | Metadata covered; headers and trailers not taught separately |
| gRPC over TLS | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| grpcurl and ghz tools | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Postman for gRPC testing | missing | → suggest part06 | - |
| protoc-gen-validate | missing | → suggest part06 | - |

## G15 gRPC API project (Udemy 11)

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| MongoDB CRUD and document relationships | covered | part12_databases.topics.md › NoSQL and choosing a store | Go driver in part06 Go — the everyday standard library |
| gRPC interceptors for logging, rate limits and auth | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Combined REST and gRPC API | covered | part11_software_architecture.topics.md › API design | Transcoding one .proto to both |
| Generics helper functions | covered | part06_programming_languages_go.topics.md › Go — memory, types with behaviour and generics | - |

## G16 Observability and profiling

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| OpenTelemetry instrumentation in Go | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| pprof profiling | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Distributed tracing | covered | part18_devops_sre.topics.md › Observability | - |

## G17 Security and hardening

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| govulncheck | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Secrets management | covered | part14_security.topics.md › Cryptography | - |
| Least privilege | covered | part14_security.topics.md › Principles and economics | - |
| Audit logs | partial | part19_machine_learning.topics.md › MLOps | Named in ML governance only; general audit logging not taught in part14 |
| SLOs | covered | part18_devops_sre.topics.md › Site reliability engineering | - |
| Webhook failure budgets | covered | part06_programming_languages_go.topics.md › Go — engineering | Payments section |

## G18 Deployment and releases

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Docker images and containers | covered | part18_devops_sre.topics.md › Docker | - |
| Cross-compilation | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| GoReleaser | covered | part06_programming_languages_go.topics.md › Go — engineering | - |

## G19 Interview prep (Udemy 13)

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Udemy sections 12, 14 and 15 (archived resources) | out of scope | - | Tagged ARCHIVE in the source: not taught |

## G20 Payments addendum

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Payment rails versus wallets and UPI | covered | part06_programming_languages_go.topics.md › Go — engineering | Implementing payments section |
| Authorization, capture and settlement | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Test versus live mode | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| PCI DSS compliance | partial | part14_security.topics.md › Privacy | PCI scope named only in the tokenization line |
| Idempotency-Key handling | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Webhook signatures and replay windows | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Double-entry ledger | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Rounding and largest-remainder allocation | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Property-based tests of ledger invariants | covered | part11_software_architecture.topics.md › Software testing at depth | Generic technique; payments example in part06 |
| Refunds, disputes and reversals | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Reconciliation | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Regional payment methods (UPI, QR, netbanking) | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Provider swap behind an interface with contract tests | covered | part06_programming_languages_go.topics.md › Go — engineering | - |

## §2b Contest and theory remainder

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| NP-completeness and P versus NP | covered | part08_data_structures_algorithms.topics.md › Computability and complexity | - |
| Polynomial-time reductions | covered | part08_data_structures_algorithms.topics.md › Computability and complexity | - |
| Approximation and heuristics for hard problems | covered | part08_data_structures_algorithms.topics.md › Computability and complexity | - |
| Max flow and min cut | covered | part08_data_structures_algorithms.topics.md › Graph algorithms | Ford–Fulkerson and Edmonds–Karp |
| Fenwick trees, segment trees and sparse tables | covered | part08_data_structures_algorithms.topics.md › Trees and heaps | - |
| Suffix arrays and suffix automata | covered | part08_data_structures_algorithms.topics.md › Sorting, searching and strings | - |
| Finite automata and weighted finite-state transducers | covered | part08_data_structures_algorithms.topics.md › Computability and complexity | - |
| Peak finding | covered | part08_data_structures_algorithms.topics.md › Sorting, searching and strings | - |
| Fibonacci heaps and van Emde Boas trees | covered | part08_data_structures_algorithms.topics.md › Trees and heaps | As ideas only |
| Integer linear programming | covered | part19_machine_learning.topics.md › Specialised learning areas | Operations research bullet |

## §2c Mathematics, ML algorithms, and ML-system foundations

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Go numerical packages (Gonum, Gorgonia, GoMLX, ONNX Runtime) | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library | - |
| Qdrant client | partial | part20_generative_ai_1of3.topics.md › Embeddings and retrieval | Named as a vector store option only; no Go client taught |
| pgvector client | covered | part12_databases.topics.md › Analytics and other engines | - |
| Kafka and Redpanda clients | partial | part18_devops_sre.topics.md › Site reliability engineering | Named as open-source specimens only |

## MATH-ML ladder: arithmetic to graduate-level readiness

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Integers, fractions, decimals, percentages and ratios | covered | part01_school_foundations.topics.md › Arithmetic and number sense | - |
| Number bases and base conversion | covered | part02_computer_organization.topics.md › Data representation | - |
| GCD, LCM and prime factors | covered | part01_school_foundations.topics.md › Arithmetic and number sense | - |
| Units, rates and unit conversion | covered | part01_school_foundations.topics.md › Units and dimensional reasoning | - |
| Scientific notation and significant figures | covered | part01_school_foundations.topics.md › Arithmetic and number sense | - |
| Expressions, equations and inequalities | covered | part01_school_foundations.topics.md › Algebra | - |
| Polynomials, remainder and factor theorems | covered | part01_school_foundations.topics.md › Algebra | - |
| Exponentials and logarithms | covered | part01_school_foundations.topics.md › Exponents, roots and logarithms | - |
| Relations, functions, domain, range, composition and inverses | covered | part01_school_foundations.topics.md › Functions and graphs | - |
| Cartesian coordinates and distance metrics | covered | part01_school_foundations.topics.md › Geometry, trigonometry and vectors | Manhattan and cosine distances in part03 Linear algebra |
| Lines, slope, intersections and similarity | covered | part01_school_foundations.topics.md › Geometry, trigonometry and vectors | - |
| Trigonometry and the unit circle | covered | part01_school_foundations.topics.md › Geometry, trigonometry and vectors | - |
| Intersection over union and bounding boxes | missing | → suggest part19 | - |
| Conic sections | missing | → suggest part01 | - |
| Vectors, matrices, determinants and row operations | covered | part03_mathematics.topics.md › Linear algebra | - |
| Rank, projections and orthogonality | covered | part03_mathematics.topics.md › Linear algebra | - |
| Gram–Schmidt and least squares | covered | part03_mathematics.topics.md › Linear algebra | - |
| Eigenvectors, eigenvalues and power iteration | covered | part03_mathematics.topics.md › Linear algebra | - |
| SVD, PCA and low-rank approximation | covered | part03_mathematics.topics.md › Linear algebra | - |
| Brute-force nearest neighbours | covered | part19_machine_learning.topics.md › Classical machine learning | k-NN bullet |
| Limits, continuity and derivatives | covered | part03_mathematics.topics.md › Calculus and optimization | - |
| Chain, product and quotient rules | covered | part03_mathematics.topics.md › Calculus and optimization | - |
| Partial derivatives, gradients and Jacobians | covered | part03_mathematics.topics.md › Calculus and optimization | - |
| Hessian | covered | part03_mathematics.topics.md › Calculus and optimization | - |
| Integrals as accumulated area | covered | part03_mathematics.topics.md › Calculus and optimization | - |
| Euler and Runge–Kutta solvers | covered | part03_mathematics.topics.md › Calculus and optimization | - |
| Finite-difference gradient checks | covered | part03_mathematics.topics.md › Numerical computing | - |
| Events, conditional probability and Bayes theorem | covered | part03_mathematics.topics.md › Probability | - |
| Random variables, expectation and variance | covered | part03_mathematics.topics.md › Probability | - |
| Common distributions (Bernoulli, binomial, Poisson, normal, exponential) | covered | part03_mathematics.topics.md › Probability | - |
| Sampling and Monte Carlo estimation | covered | part03_mathematics.topics.md › Probability | - |
| Law of large numbers and central limit theorem | covered | part03_mathematics.topics.md › Probability | - |
| Estimators, bias, variance and maximum likelihood | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| Fisher information | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| Confidence intervals and hypothesis tests | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| Bootstrap and jackknife | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| Power, sample size and multiple testing | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| Sequential testing and CUPED | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| Bayesian prior and posterior updates | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| Convexity and global minima | covered | part03_mathematics.topics.md › Calculus and optimization | - |
| Lagrange multipliers and KKT conditions | covered | part03_mathematics.topics.md › Calculus and optimization | - |
| Gradient descent and SGD | covered | part03_mathematics.topics.md › Calculus and optimization | - |
| Momentum and adaptive optimizers | covered | part03_mathematics.topics.md › Calculus and optimization | - |
| L1 and L2 regularization with coordinate descent | covered | part03_mathematics.topics.md › Calculus and optimization | - |
| Linear programming and the Hungarian method | covered | part03_mathematics.topics.md › Calculus and optimization | - |
| Entropy, cross-entropy and KL divergence | covered | part03_mathematics.topics.md › Information theory | - |
| Mutual information | covered | part03_mathematics.topics.md › Information theory | - |
| Perplexity, log loss and calibration | covered | part03_mathematics.topics.md › Information theory | - |
| Shannon source coding and channel capacity | covered | part03_mathematics.topics.md › Information theory | - |
| DAGs, confounding and propensity scores | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| Difference-in-differences and uplift modelling | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| Markov decision processes | covered | part03_mathematics.topics.md › Decision mathematics | - |
| Contextual bandits, UCB and Thompson sampling | covered | part03_mathematics.topics.md › Decision mathematics | - |
| Floating-point error and catastrophic cancellation | covered | part03_mathematics.topics.md › Numerical computing | - |
| Stable softmax and log-sum-exp | covered | part03_mathematics.topics.md › Numerical computing | - |
| PRNG seeding and deterministic tests | covered | part03_mathematics.topics.md › Numerical computing | - |
| Interpolation and curve fitting | covered | part03_mathematics.topics.md › Numerical computing | - |
| Numerical integration and error propagation | covered | part03_mathematics.topics.md › Numerical computing | - |
| Convolution and correlation | covered | part03_mathematics.topics.md › Signals and sequences | - |
| Sampling and aliasing | covered | part03_mathematics.topics.md › Signals and sequences | - |
| DFT, FFT, windowing and STFT | covered | part03_mathematics.topics.md › Signals and sequences | - |
| Spectrograms and MFCC features | covered | part03_mathematics.topics.md › Signals and sequences | - |
| Sobel filters and morphology | covered | part03_mathematics.topics.md › Signals and sequences | - |
| n-gram perplexity and finite-state tokenizers | covered | part03_mathematics.topics.md › Signals and sequences | - |
| Proof habits and counterexamples | covered | part01_school_foundations.topics.md › Proof habits | Also part03 Proof and discrete mathematics |
| Metric spaces, compactness and convergence | missing | → suggest part03 | - |
| Generalization versus optimization | covered | part03_mathematics.topics.md › Calculus and optimization | - |
| Conditioning and stability of algorithms | covered | part03_mathematics.topics.md › Numerical computing | - |

## ML-CORE algorithm spine

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Prediction, ranking, retrieval and generation framing | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Leakage and delayed labels | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Class imbalance and the accuracy paradox | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Cold start and feedback loops | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Feature engineering and the hashing trick | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Train/serve parity and point-in-time features | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Confusion matrix, precision, recall and F1 | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| ROC and PR curves | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Calibration and reliability bins | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Ranking metrics (MAP, MRR, nDCG) | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Forecast error metrics | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Cross-validation | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| k-NN, linear regression and logistic regression | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Naive Bayes and discriminant analysis | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Support vector machines and margins | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Generalized linear models | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Regularization and class weights | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Decision trees, impurity and CART | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Random forests and gradient boosting | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Monotonic constraints | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| k-means, DBSCAN and Gaussian mixtures with EM | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Isolation forests and reconstruction-error anomaly scores | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Robust z-score and median absolute deviation | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Inverted indexes and BM25 | covered | part19_machine_learning.topics.md › Applied problem families | Search, learning to rank and ads |
| Collaborative filtering and matrix factorization | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Two-stage retrieval and reranking | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Learning to rank | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Diversity and coverage in result sets | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Tokenization, Unicode normalization and edit distance | covered | part19_machine_learning.topics.md › Natural language processing foundations | - |
| TF-IDF weighting | covered | part19_machine_learning.topics.md › Natural language processing foundations | - |
| Transformer blocks and self-attention | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Prompt and context-window design | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | - |
| Structured outputs and constrained decoding | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | - |
| RAG evaluation | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | - |
| Prompt injection and safety filters | covered | part22_generative_ai_3of3.topics.md › Security and safety of LLM applications | - |
| Image convolution and spatial filters | covered | part19_machine_learning.topics.md › Classical computer vision and geometry | - |
| Image embeddings and document extraction | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Audio spectrograms and MFCC features | covered | part19_machine_learning.topics.md › Specialised learning areas | - |
| Perceptual hashing | covered | part19_machine_learning.topics.md › Specialised learning areas | - |
| Multimodal retrieval | covered | part19_machine_learning.topics.md › Specialised learning areas | - |
| PageRank and random-walk embeddings | covered | part19_machine_learning.topics.md › Specialised learning areas | - |
| Label propagation and bipartite anomaly scores | covered | part19_machine_learning.topics.md › Specialised learning areas | - |
| Entity-resolution blocking | covered | part19_machine_learning.topics.md › Specialised learning areas | - |
| Moving averages, exponential smoothing and backtests | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Quantile loss and prediction intervals | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Assignment and constrained scheduling | covered | part19_machine_learning.topics.md › Specialised learning areas | - |
| Off-policy evaluation | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Causal graphs and observational bias | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Value iteration and temporal-difference learning | covered | part19_machine_learning.topics.md › Specialised learning areas | - |
| Privacy, PII minimization and retention checks | covered | part19_machine_learning.topics.md › MLOps | - |
| Human-in-the-loop review and human override | covered | part19_machine_learning.topics.md › MLOps | - |
| Model bias and fairness checks | covered | part19_machine_learning.topics.md › MLOps | - |
| Model cards | covered | part19_machine_learning.topics.md › MLOps | - |
| Tensors and computational graphs | covered | part19_machine_learning.topics.md › Deep learning | - |
| MLP forward and backward pass | covered | part19_machine_learning.topics.md › Deep learning | Backpropagation bullet |
| Optimizers: SGD, momentum, RMSProp and Adam | covered | part19_machine_learning.topics.md › Deep learning | - |
| Dropout and normalization layers | covered | part19_machine_learning.topics.md › Deep learning | - |
| Residual connections | covered | part19_machine_learning.topics.md › Deep learning | - |
| Multi-head attention and positional encodings | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Causal masking for decoders | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |

## ML-SYS production spine from the case-study corpus

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Product spec, north-star metric and launch criteria | partial | part19_machine_learning.topics.md › Classical machine learning | Guardrail metrics covered; north-star tree and launch criteria not taught |
| Event contracts, freshness and backfills | covered | part19_machine_learning.topics.md › MLOps | - |
| Feature store with online and offline parity | covered | part19_machine_learning.topics.md › MLOps | - |
| Dataset snapshots and experiment tracking | covered | part19_machine_learning.topics.md › MLOps | - |
| Model registry and lineage | covered | part19_machine_learning.topics.md › MLOps | - |
| Online, batch, async and sidecar serving | covered | part19_machine_learning.topics.md › MLOps | - |
| Caches, fallbacks and timeout budgets | covered | part19_machine_learning.topics.md › MLOps | - |
| A/B tests, holdouts and canary or shadow rollout | covered | part19_machine_learning.topics.md › MLOps | - |
| Rollback gates | covered | part19_machine_learning.topics.md › MLOps | - |
| Covariate, label and concept drift | covered | part19_machine_learning.topics.md › MLOps | - |
| Kolmogorov–Smirnov statistic and population stability index | covered | part19_machine_learning.topics.md › MLOps | - |
| Drift and freshness alerting with OpenTelemetry | covered | part18_devops_sre.topics.md › Observability | General OpenTelemetry; ML-specific metrics not separate |
| Privacy, abuse and governance controls | covered | part19_machine_learning.topics.md › MLOps | - |
| Hot keys, batching and approximate retrieval | covered | part19_machine_learning.topics.md › MLOps | - |
| Cost per successful decision | covered | part19_machine_learning.topics.md › MLOps | - |
| Shared ML platforms | covered | part19_machine_learning.topics.md › MLOps | - |
| Case-study method: metric, data, serving and monitoring | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Published case-study rotation (named companies) | partial | part25_ml_case_studies_1of5.topics.md › Recommend / personalize / feed | Netflix, LinkedIn, Etsy, Airbnb, Spotify, Instacart, DoorDash, GitHub, Uber, Grab and Honeycomb present in parts 25–29; Stripe Radar not found |

## 3. Computing baseline

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Process, file and computer basics | covered | part10_operating_systems.topics.md › Processes and threads | - |
| Binary, hexadecimal and bytes | covered | part02_computer_organization.topics.md › Data representation | - |
| UTF-8 encoding | covered | part02_computer_organization.topics.md › Data representation | - |
| Filesystem paths, permissions and environment | covered | part10_operating_systems.topics.md › Linux practice | - |
| Working directory, pipes and exit codes | covered | part05_programming_languages_python_and_shell.topics.md › Shell and working with APIs from code | - |
| Git add, commit, branch, diff and pull requests | covered | part15_software_delivery.topics.md › Git | - |
| HTTP verbs, status codes, headers and JSON | covered | part09_networking.topics.md › HTTP and the web | - |
| Debugger use with Delve | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Print-debugging | missing | → suggest part05 | - |
| Programming ideas: variable, sequence, branch, loop, function, error, test | covered | part05_programming_languages_python_and_shell.topics.md › Python | - |
| Arrays, lists, stacks, queues, maps, trees and graphs as vocabulary | covered | part08_data_structures_algorithms.topics.md › Linear structures and techniques | - |
| Sets, functions and relations | covered | part03_mathematics.topics.md › Proof and discrete mathematics | - |
| Counting and permutations | covered | part03_mathematics.topics.md › Proof and discrete mathematics | - |
| Process versus thread versus goroutine | covered | part10_operating_systems.topics.md › Processes and threads | Goroutines in part06 Go — concurrency |
| IP addressing and ports | partial | part09_networking.topics.md › Architecture principles | IPv4 covered; port numbers appear only as NAT source-port exhaustion |
| DNS | covered | part09_networking.topics.md › DNS | - |
| AIOps: trace, alert and incident note | missing | → suggest part18 | - |
| Orchestration with job queues and schedulers | covered | part18_devops_sre.topics.md › Kubernetes | - |
| Distributed resilience: backpressure, retries and failover | covered | part13_distributed_systems.topics.md › Asynchronism and flow control | - |
| High-level system design method | covered | part13_distributed_systems.topics.md › System design method | - |
| Low-level design of service contracts | covered | part11_software_architecture.topics.md › API design | - |
| Design patterns: adapter and repository | partial | part11_software_architecture.topics.md › Gang of Four patterns | Adapter covered; repository named only as an architecture style |
| Software development: pull requests, test pyramid and CI | partial | part15_software_delivery.topics.md › Git | Pull requests and CI covered; the test pyramid is not named |

## Missing in this range

- Editor setup and extensions (VS Code) (→ suggest part05) — from: G0 Orientation and tooling
- Installing Go on Linux, Windows and macOS (→ suggest part06) — from: G0 Orientation and tooling
- Go Playground (→ suggest part06) — from: G0 Orientation and tooling
- Blank identifier (→ suggest part06) — from: G1 Foundations I
- XML encoding (→ suggest part07) — from: G5 CLI, env, config, logging
- URL and URI structure (→ suggest part09) — from: G11 Internet and HTTP/TLS
- All-pairs shortest paths, Floyd–Warshall (→ suggest part08) — from: G11 Internet and HTTP/TLS
- HTTP parameter pollution (HPP) (→ suggest part14) — from: G12 REST API project
- Password change and forgot/reset flows (→ suggest part14) — from: G12 REST API project
- Code obfuscation (→ suggest part14) — from: G12 REST API project
- PostgreSQL system catalogs: pg_class, pg_attribute, pg_type, pg_statistic (→ suggest part12) — from: G12b SQL and PostgreSQL internals braid
- Postman for gRPC testing (→ suggest part06) — from: G14 gRPC core
- protoc-gen-validate (→ suggest part06) — from: G14 gRPC core
- Intersection over union and bounding boxes (→ suggest part19) — from: §2c MATH-ML ladder
- Conic sections (→ suggest part01) — from: §2c MATH-ML ladder
- Metric spaces, compactness and convergence (→ suggest part03) — from: §2c MATH-ML ladder
- Print-debugging (→ suggest part05) — from: §3 Computing baseline
- AIOps: trace, alert and incident note (→ suggest part18) — from: §3 Computing baseline

## Partial in this range

- GOROOT, GOPATH and module environment variables — GOMOD, GOSUMDB and GOPROXY covered; GOROOT and GOPATH not named — part06_programming_languages_go.topics.md
- Formatting for vertical openness and density — gofmt covered; vertical layout rules not taught — part06_programming_languages_go.topics.md
- Naming conventions — package naming covered; identifier conventions not taught — part06_programming_languages_go.topics.md
- Discrete math: indexed sequences — functions covered; indexed sequences not taught as a concept — part03_mathematics.topics.md
- Amortized analysis of union-find — amortized cost covered in general; union-find potential argument not taught — part08_data_structures_algorithms.topics.md
- Database tuple, catalog and B-tree node structs — heap tuples and B+ trees covered; Go modelling lab not taught — part12_databases.topics.md
- Binary file layout, slotted-page encoding and checksums — slotted pages named; byte encoding and page checksums not taught — part12_databases.topics.md
- WAL-record serialization — WAL rule named; record format not taught — part12_databases.topics.md
- Leaky bucket and fixed-window limiters — named in a list of rate-limit algorithms only — part14_security.topics.md
- Selectivity estimates and cache-hit reasoning — selectivity under uniformity covered; cache-hit probability not taught — part12_databases.topics.md
- Frontend client versus backend API roles — web client covered; client and server role split not taught — part07_programming_languages_typescript_wire_theory_exercises.topics.md
- CORS middleware — same-origin policy and CORS named; no middleware configuration taught — part14_security.topics.md
- Security response headers — HSTS named only — part14_security.topics.md
- HTTP compression middleware — compression named as a proxy role; gzip appears only in an exercise — part09_networking.topics.md
- Request input validation — MaxBytesReader covered; validation rules not taught — part06_programming_languages_go.topics.md
- System columns ctid, xmin and xmax — tuple versioning covered; system columns not named — part12_databases.topics.md
- gRPC metadata, headers and trailers — metadata covered; headers and trailers not taught separately — part06_programming_languages_go.topics.md
- Audit logs — named in ML governance only; general audit logging not taught in part14 — part19_machine_learning.topics.md
- PCI DSS compliance — PCI scope named only in the tokenization line — part14_security.topics.md
- Qdrant client — named as a vector store option only; no Go client taught — part20_generative_ai_1of3.topics.md
- Kafka and Redpanda clients — named as open-source specimens only — part18_devops_sre.topics.md
- Product spec, north-star metric and launch criteria — guardrail metrics covered; north-star tree and launch criteria not taught — part19_machine_learning.topics.md
- Published case-study rotation (named companies) — Stripe Radar not found in parts 25–29 — part25_ml_case_studies_1of5.topics.md
- IP addressing and ports — IPv4 covered; port numbers appear only as NAT source-port exhaustion — part09_networking.topics.md
- Design patterns: adapter and repository — adapter covered; repository named only as an architecture style — part11_software_architecture.topics.md
- Software development: pull requests, test pyramid and CI — pull requests and CI covered; test pyramid not named — part15_software_delivery.topics.md
