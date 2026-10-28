# Topic diff: Tool subcourses, system design, phases and glossary

Source: gcp/unified-curriculum.md lines 4328-4894. Compared against: gcp-lite/index/*.topics.md and gcp-lite/Rust_Track_AI_Infrastructure.md.

Counts: 265 topics; 237 covered, 19 partial, 0 missing, 9 out of scope.

## 4. Tool and platform subcourses
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Git commits, branches, merges and pull requests | covered | part15_software_delivery.topics.md › Git | - |
| GitHub OAuth login and token handling | covered | part14_security.topics.md › Authentication and sessions | - |
| Docker images and Docker Compose | covered | part18_devops_sre.topics.md › Docker | - |
| BuildKit image builds | covered | part18_devops_sre.topics.md › Docker | - |
| Kubernetes deployments and pods | covered | part18_devops_sre.topics.md › Kubernetes | - |
| Helm charts and releases | covered | part18_devops_sre.topics.md › Kubernetes | - |
| Terraform plan, state and modules | covered | part18_devops_sre.topics.md › Infrastructure as code | - |
| Kong gateway, routes and plugins (with Lua) | covered | part18_devops_sre.topics.md › NGINX and API gateways | - |
| NGINX reverse proxy and load balancing | covered | part18_devops_sre.topics.md › NGINX and API gateways | - |
| MongoDB document store | covered | part12_databases.topics.md › NoSQL and choosing a store | - |
| Service clients (mongo-go-driver, go-redis, client-go, Docker Engine API) | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library | - |
| Redis Streams and consumer groups | covered | part18_devops_sre.topics.md › Observability | - |
| Redis as a cache | covered | part13_distributed_systems.topics.md › Caching at scale | - |
| PostgreSQL and psql | covered | part12_databases.topics.md › The SQL language | - |
| pgvector vector search | covered | part12_databases.topics.md › Analytics and other engines | - |
| pg_stat_statements and slow-query triage | covered | part12_databases.topics.md › Operating databases | - |
| pgbench benchmarking | partial | part12_databases.topics.md › Operating databases | pgbench is not named; slow-query tools and restore drills are taught |
| Logical and physical backups (pg_dump, WAL archiving) | covered | part12_databases.topics.md › Operating databases | - |
| Point-in-time recovery | covered | part12_databases.topics.md › Recovery and replication | - |
| OpenTelemetry tracing | covered | part18_devops_sre.topics.md › Observability | - |
| Phoenix LLM trace UI | covered | part18_devops_sre.topics.md › Observability | - |
| Cobra and Viper CLIs | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library | - |
| Vector stores (Qdrant, pgvector, FAISS) | covered | part20_generative_ai_1of3.topics.md › Embeddings and retrieval | - |
| Gonum numerical library | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library | - |
| Go ML runtimes (Gorgonia, GoMLX, ONNX Runtime) | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library | - |
| Feature store (online and offline features) | partial | part19_machine_learning.topics.md › MLOps | Feature platforms and point-in-time joins are taught; no feature-store facade or online/offline serving build |
| Model registry (versions, approval, rollback pointer) | partial | part19_machine_learning.topics.md › MLOps | MLflow tracking and a shared registry are named; approval state and rollback pointer are not taught |
| Drift monitoring and alerts | covered | part19_machine_learning.topics.md › MLOps | - |
| OpenAI-compatible chat APIs | covered | part21_generative_ai_2of3.topics.md › Model APIs | - |
| Structured JSON output | covered | part21_generative_ai_2of3.topics.md › Model APIs | - |
| JSON-RPC 2.0 | covered | part07_programming_languages_typescript_wire_theory_exercises.topics.md › Wire formats | - |
| LLM tool calling | covered | part21_generative_ai_2of3.topics.md › Tools and the Model Context Protocol | - |
| LLM rate limits and API errors | covered | part21_generative_ai_2of3.topics.md › Model APIs | - |
| LLM token budgets and cost control | partial | part21_generative_ai_2of3.topics.md › Model APIs | Model choice on price and latency is taught; per-request token budgets are not |
| Ollama local models | covered | part21_generative_ai_2of3.topics.md › Model APIs | - |
| Gin, Fiber and Chi HTTP frameworks | covered | part06_programming_languages_go.topics.md › Go — engineering | - |

## HLD, LLD, and clean architecture
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| High-level design (HLD) | covered | part13_distributed_systems.topics.md › System design method | - |
| Low-level design (LLD) and design contracts | covered | part11_software_architecture.topics.md › Architecture documentation | - |
| C4 model and Mermaid diagrams | covered | part11_software_architecture.topics.md › Architecture documentation | - |
| Capacity estimation | covered | part03_mathematics.topics.md › Queueing and performance modelling | - |
| API contracts and pagination | covered | part11_software_architecture.topics.md › API design | - |
| State machines (design level) | covered | part11_software_architecture.topics.md › Gang of Four patterns | - |
| Idempotency keys | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Concurrency model and transaction boundaries | covered | part12_databases.topics.md › Transactions and concurrency control | - |
| Error model and error taxonomy | partial | part09_networking.topics.md › HTTP and the web | HTTP status codes and Retry-After are taught; a designed API error taxonomy and error envelope are not |
| Clean architecture (dependency rule, ports and adapters) | covered | part11_software_architecture.topics.md › Application architecture | - |
| Domain-driven design | covered | part11_software_architecture.topics.md › Domain-driven design | - |
| Repository pattern | covered | part11_software_architecture.topics.md › Application architecture | - |
| Unit of Work pattern | covered | part11_software_architecture.topics.md › Application architecture | - |
| Gang of Four patterns (creational, structural, behavioural) | covered | part11_software_architecture.topics.md › Gang of Four patterns | - |
| Chain of Responsibility | covered | part11_software_architecture.topics.md › Gang of Four patterns | - |
| Middleware and decorator chains | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Transactional outbox | covered | part13_distributed_systems.topics.md › Distributed transactions | - |
| Saga pattern | covered | part13_distributed_systems.topics.md › Distributed transactions | - |
| CQRS and read models | covered | part11_software_architecture.topics.md › Distributed application patterns | - |
| Idempotent consumer | covered | part13_distributed_systems.topics.md › Distributed transactions | - |
| Circuit breaker | covered | part11_software_architecture.topics.md › Distributed application patterns | - |
| Bulkhead | covered | part11_software_architecture.topics.md › Distributed application patterns | - |
| Retry with exponential backoff and jitter | covered | part06_programming_languages_go.topics.md › Go — concurrency | - |
| Timeouts and deadlines | covered | part06_programming_languages_go.topics.md › Go — concurrency | - |
| Strangler fig migration | covered | part11_software_architecture.topics.md › Distributed application patterns | - |

## 5. System design track
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Six-step system design write-up | covered | part13_distributed_systems.topics.md › System design method | - |
| Case-study analysis with a tiny model | covered | part13_distributed_systems.topics.md › System design method | - |
| Request coalescing | partial | part06_programming_languages_go.topics.md › Go — concurrency | Single-flight loading is named; coalescing reads by routing key is not taught |
| Zero-downtime schema migration (expand and contract) | covered | part12_databases.topics.md › Data modelling and design | - |
| Load shedding and bounded queues | covered | part13_distributed_systems.topics.md › Asynchronism and flow control | - |
| Dead-letter queue and redrive | partial | part06_programming_languages_go.topics.md › Go — engineering | Dead-letter queues are taught for webhooks and Pub/Sub; redrive of dead letters is not |
| Diversity-aware reranking | covered | part19_machine_learning.topics.md › Applied problem families | - |

## 5a Primer topic index
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Performance versus scalability | covered | part13_distributed_systems.topics.md › Performance at scale | - |
| Latency versus throughput | covered | part13_distributed_systems.topics.md › Performance at scale | - |
| CAP theorem, CP and AP systems | covered | part13_distributed_systems.topics.md › Foundations | - |
| Weak, eventual and strong consistency | covered | part13_distributed_systems.topics.md › Foundations | - |
| Active-passive and active-active failover | covered | part09_networking.topics.md › Middleboxes, proxies and load balancing | - |
| Availability in nines | covered | part13_distributed_systems.topics.md › Availability | - |
| Series versus parallel availability | covered | part18_devops_sre.topics.md › Site reliability engineering | - |
| DNS record types and TTL | covered | part09_networking.topics.md › DNS | - |
| DNS weighted, latency and geo routing | covered | part09_networking.topics.md › DNS | - |
| CDN push versus pull | covered | part09_networking.topics.md › Middleboxes, proxies and load balancing | - |
| Layer 4 versus layer 7 load balancing | covered | part09_networking.topics.md › Middleboxes, proxies and load balancing | - |
| Session persistence and SSL termination | covered | part09_networking.topics.md › Middleboxes, proxies and load balancing | - |
| Horizontal versus vertical scaling | covered | part13_distributed_systems.topics.md › Performance at scale | - |
| Reverse proxy versus load balancer | covered | part09_networking.topics.md › Middleboxes, proxies and load balancing | - |
| Service discovery and registries (Consul, etcd, ZooKeeper) | covered | part11_software_architecture.topics.md › Architecture fundamentals | - |
| Monolith, modular monolith, SOA and microservices | covered | part11_software_architecture.topics.md › Architecture fundamentals | - |
| Synchronous versus asynchronous communication | covered | part11_software_architecture.topics.md › Architecture fundamentals | - |
| API gateway concerns | covered | part11_software_architecture.topics.md › Architecture fundamentals | - |
| Relational algebra | covered | part12_databases.topics.md › Relational theory | - |
| ACID transactions | covered | part12_databases.topics.md › Transactions and concurrency control | - |
| MVCC snapshots and tuple versioning | covered | part12_databases.topics.md › Transactions and concurrency control | - |
| Isolation levels | covered | part12_databases.topics.md › Transactions and concurrency control | - |
| Locks and deadlocks | covered | part12_databases.topics.md › Transactions and concurrency control | - |
| B-tree indexes | covered | part12_databases.topics.md › Storage and access methods | - |
| Hash, GIN, BRIN and bitmap indexes | covered | part12_databases.topics.md › Storage and access methods | - |
| Query planning and EXPLAIN | covered | part12_databases.topics.md › Query processing | - |
| Leader-follower (primary-replica) replication | covered | part13_distributed_systems.topics.md › Replication | - |
| Multi-leader replication and write conflicts | covered | part13_distributed_systems.topics.md › Replication | - |
| Federation by functional partitioning | covered | part13_distributed_systems.topics.md › Partitioning | - |
| Sharding and hot keys | covered | part13_distributed_systems.topics.md › Partitioning | - |
| Consistent hashing with virtual nodes | covered | part13_distributed_systems.topics.md › Caching at scale | - |
| Denormalization | covered | part12_databases.topics.md › Data modelling and design | - |
| SQL tuning workflow | covered | part12_databases.topics.md › Query processing | - |
| Write-ahead logging | covered | part12_databases.topics.md › Recovery and replication | - |
| Backup and restore | covered | part12_databases.topics.md › Operating databases | - |
| Replication lag | covered | part12_databases.topics.md › Recovery and replication | - |
| Read/write routing | partial | part13_distributed_systems.topics.md › Replication | Read replicas and promotion are taught; application-level read/write routing and proxies are not |
| BASE versus ACID | covered | part12_databases.topics.md › NoSQL and choosing a store | - |
| Key-value, document, wide-column and graph stores | covered | part12_databases.topics.md › NoSQL and choosing a store | - |
| SQL versus NoSQL choice | covered | part12_databases.topics.md › NoSQL and choosing a store | - |
| Cache layers (client, CDN, web, database, application) | covered | part13_distributed_systems.topics.md › Caching at scale | - |
| Query cache versus object cache | partial | part13_distributed_systems.topics.md › Caching at scale | Cache layers are named; query-level and object-level caching are not distinguished |
| Cache-aside, write-through, write-behind and refresh-ahead | covered | part13_distributed_systems.topics.md › Caching at scale | - |
| Cache TTLs and LRU approximation | covered | part13_distributed_systems.topics.md › Caching at scale | - |
| Message queues and event-driven architecture | covered | part11_software_architecture.topics.md › Architecture fundamentals | - |
| Task queues and job claims in SQL | covered | part12_databases.topics.md › The SQL language | - |
| Back pressure | covered | part13_distributed_systems.topics.md › Asynchronism and flow control | - |
| At-least-once versus exactly-once delivery | covered | part13_distributed_systems.topics.md › Distributed transactions | - |
| TCP and UDP | covered | part09_networking.topics.md › Transport | - |
| RPC | covered | part05_programming_languages_python_and_shell.topics.md › Shell and working with APIs from code | - |
| REST | covered | part11_software_architecture.topics.md › API design | - |
| Powers of two | covered | part02_computer_organization.topics.md › Data representation | - |
| Latency numbers every programmer should know | covered | part02_computer_organization.topics.md › Machine organization | - |

## 5a-SQL PostgreSQL and database-systems application matrix
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Bag versus set semantics | covered | part12_databases.topics.md › Relational theory | - |
| Three-valued logic and NULL handling | covered | part12_databases.topics.md › Pre-SQL foundations | - |
| Constraints (PK, FK, CHECK, UNIQUE, EXCLUDE, deferrable) | covered | part12_databases.topics.md › Relational theory | - |
| System catalogs and system columns | covered | part12_databases.topics.md › Storage and access methods | - |
| JSONB, range and UUID types | covered | part12_databases.topics.md › The SQL language | - |
| Slotted pages, line pointers and TOAST | covered | part12_databases.topics.md › Storage and access methods | - |
| External merge sort | covered | part12_databases.topics.md › Query processing | - |
| Index-only and bitmap scans | covered | part12_databases.topics.md › Storage and access methods | - |
| Tuple version chains and HOT updates | covered | part12_databases.topics.md › Storage and access methods | - |
| Vacuum, bloat and transaction-ID freezing | covered | part12_databases.topics.md › Transactions and concurrency control | - |
| Shared buffers, background writer and checkpointer | covered | part12_databases.topics.md › Storage and access methods | - |
| Full-page writes and crash recovery | covered | part12_databases.topics.md › Recovery and replication | - |
| Streaming replication and PITR | covered | part12_databases.topics.md › Recovery and replication | - |
| Selectivity and planner statistics | covered | part12_databases.topics.md › Query processing | - |
| Approximate versus exact k-NN (ANN, HNSW, IVF) | covered | part20_generative_ai_1of3.topics.md › Embeddings and retrieval | - |
| Vector store trade-offs (pgvector versus Qdrant) | covered | part20_generative_ai_1of3.topics.md › Embeddings and retrieval | - |

## 5a-ML Production ML-system case-study atlas
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| BM25 and TF-IDF retrieval | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Pairwise and listwise learning to rank | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Ranking metrics (NDCG, precision@k, recall@k) | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Cold-start handling | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Time-series forecasting baselines | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Quantile forecasting and pinball loss | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Linear and integer programming for scheduling | covered | part03_mathematics.topics.md › Calculus and optimization | - |
| Streaming features and freshness checks | covered | part19_machine_learning.topics.md › MLOps | - |
| Anomaly detection | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Graph risk and fraud rings | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Review thresholds and fail-open versus fail-closed | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Append-only audit trail | covered | part12_databases.topics.md › Data modelling and design | - |
| Adversarial test sets | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Tokenizers | covered | part19_machine_learning.topics.md › Machine learning in Python | - |
| Prompt packing and context-window budgeting | partial | part20_generative_ai_1of3.topics.md › How LLMs work | The context window is taught as a position-table limit; prompt packing and budgeting are not |
| RAG evaluation and faithfulness | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | - |
| Structured-output validation | covered | part21_generative_ai_2of3.topics.md › Model APIs | - |
| Prompt injection | covered | part14_security.topics.md › AI and LLM application threats | - |
| Perceptual hashing for near-duplicate images | partial | part29_ml_case_studies_5of5.topics.md › Other (pricing, classification, routing, dimensions and more) | Near-duplicate image detection is taught only as the OLX case (triplet-loss embeddings); perceptual hashing itself is not |
| Spectrograms and MFCC features | covered | part19_machine_learning.topics.md › Specialised learning areas | - |
| Multimodal retrieval | covered | part19_machine_learning.topics.md › Specialised learning areas | - |
| Dataset snapshots and versioning | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Computer vision: images, motion and multi-view geometry | Image dataset versions are recorded; training-data snapshot manifests are not taught |
| Training-serving skew and point-in-time correctness | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Drift monitoring | covered | part19_machine_learning.topics.md › MLOps | - |
| Shadow and canary rollout | covered | part19_machine_learning.topics.md › MLOps | - |
| PageRank and random-walk embeddings | covered | part19_machine_learning.topics.md › Specialised learning areas | - |
| Bipartite graphs | covered | part03_mathematics.topics.md › Proof and discrete mathematics | - |
| Blocking and candidate generation | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Entity resolution (record linkage) | partial | part29_ml_case_studies_5of5.topics.md › Other (pricing, classification, routing, dimensions and more) | Record linkage is named in passing in the Wayfair case; matching and clustering methods are not taught |
| Epsilon-greedy, UCB and Thompson sampling | covered | part03_mathematics.topics.md › Decision mathematics | - |
| Contextual bandits and offline replay | covered | part19_machine_learning.topics.md › Applied problem families | - |
| A/B assignment and exposure logging | covered | part19_machine_learning.topics.md › MLOps | - |
| CUPED variance reduction | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| Propensity weighting and uplift modelling | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| Causal DAG adjustment | covered | part03_mathematics.topics.md › Statistics and experimental design | - |

## 5b Official system-design problems — design + implement in Go
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| URL shortener design (Pastebin, Bit.ly, TinyURL) | covered | part13_distributed_systems.topics.md › Exercises | - |
| Twitter timeline and search design | covered | part13_distributed_systems.topics.md › Exercises | - |
| Web crawler design | covered | part13_distributed_systems.topics.md › Exercises | - |
| Personal-finance aggregator design (Mint.com) | covered | part13_distributed_systems.topics.md › Exercises | - |
| Social-network data structures and graph traversal | covered | part13_distributed_systems.topics.md › Exercises | - |
| Key-value cache for search queries | covered | part13_distributed_systems.topics.md › Exercises | - |
| Sales rank by category | covered | part13_distributed_systems.topics.md › Exercises | - |
| Scaling a service from one box to millions of users | covered | part13_distributed_systems.topics.md › System design method | - |

## 5c Official object-oriented design problems — implement in Go
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Hash map design | covered | part08_data_structures_algorithms.topics.md › Hashing | - |
| LRU cache design | covered | part11_software_architecture.topics.md › Exercises | - |
| Call center with escalation | covered | part11_software_architecture.topics.md › Exercises | - |
| Deck of cards and blackjack | covered | part11_software_architecture.topics.md › Exercises | - |
| Parking lot design | covered | part11_software_architecture.topics.md › Exercises | - |
| Chat server with group chats | covered | part11_software_architecture.topics.md › Exercises | - |
| Circular array (ring buffer) | covered | part08_data_structures_algorithms.topics.md › Linear structures and techniques | - |

## 5d Additional primer questions — same bar
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| File sync design (Dropbox) | covered | part13_distributed_systems.topics.md › Exercises | - |
| Search engine design | covered | part13_distributed_systems.topics.md › Exercises | - |
| Collaborative documents (OT and CRDTs) | covered | part13_distributed_systems.topics.md › Replication | - |
| Redis-like key-value store with expiry and eviction | covered | part13_distributed_systems.topics.md › Exercises | - |
| Memcached-like cache | covered | part13_distributed_systems.topics.md › Exercises | - |
| Recommendation system design (Amazon) | covered | part13_distributed_systems.topics.md › Exercises | - |
| Chat app with presence (WhatsApp) | covered | part13_distributed_systems.topics.md › Exercises | - |
| Photo sharing design (Instagram) | covered | part13_distributed_systems.topics.md › Exercises | - |
| News feed design | covered | part13_distributed_systems.topics.md › Exercises | - |
| Graph search design (Facebook) | covered | part13_distributed_systems.topics.md › Exercises | - |
| CDN design | covered | part13_distributed_systems.topics.md › Exercises | - |
| Trending topics | covered | part13_distributed_systems.topics.md › Exercises | - |
| Random ID generation (Snowflake) | covered | part13_distributed_systems.topics.md › Exercises | - |
| Top-k requests in a time window | covered | part13_distributed_systems.topics.md › Exercises | - |
| Multi-datacentre serving | covered | part13_distributed_systems.topics.md › Exercises | - |
| Online multiplayer card game | covered | part13_distributed_systems.topics.md › Exercises | - |
| Garbage-collection service design | covered | part13_distributed_systems.topics.md › Exercises | - |
| API rate limiter design | covered | part13_distributed_systems.topics.md › Exercises | - |
| Stock-exchange matching engine | covered | part13_distributed_systems.topics.md › Exercises | - |

## 5e HLD/LLD/microservices/design-pattern implementation ladder
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Service mesh basics (sidecars, mTLS, traffic control) | partial | part23_cloud_providers_1of2.topics.md › Google Cloud — networking | A managed mesh is named and mesh mTLS is mentioned; sidecar proxies and the mesh control plane are not taught |
| Orchestration versus choreography | covered | part13_distributed_systems.topics.md › Distributed transactions | - |
| Durable workflow retry state (Temporal-style) | covered | part13_distributed_systems.topics.md › Distributed transactions | - |
| etcd-style watch and config model | partial | part13_distributed_systems.topics.md › Consensus and coordination | etcd is named as a coordination service; watch-based config distribution is not taught |
| Fraud decision thresholds (Stripe Radar case) | covered | part27_ml_case_studies_3of5.topics.md › Fraud / trust & safety | - |

## 6. Reconstruction phases
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Keyset pagination | partial | part12_databases.topics.md › Exercises | Named only in a lab line; no teaching bullet |
| N+1 query detection | covered | part12_databases.topics.md › Operating databases | - |
| Union-find connected components | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Heap-based top-k selection | covered | part12_databases.topics.md › Query processing | - |
| Tries for token prefixes | covered | part08_data_structures_algorithms.topics.md › Trees and heaps | - |
| Derived read-model consistency | partial | part11_software_architecture.topics.md › Distributed application patterns | CQRS read models are taught; projection lag and rebuilds are not |
| Layered configuration (flags, environment, file, defaults) | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library | - |
| Profiling with pprof | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Recovery time and recovery point objectives (RTO, RPO) | partial | part16_cloud_core.topics.md › Architecture patterns and well-architected frameworks | DR patterns are taught; RTO, RPO and data-loss budgets are not defined |
| Cost per successful decision (unit economics) | covered | part16_cloud_core.topics.md › Cloud economics and FinOps | Cost per request is taught |
| Load and stress testing | covered | part18_devops_sre.topics.md › Site reliability engineering | - |
| Operational readiness review (ORR) | covered | part18_devops_sre.topics.md › Site reliability engineering | - |
| Disaster recovery drills | covered | part16_cloud_core.topics.md › Architecture patterns and well-architected frameworks | - |
| SLOs and error budgets | covered | part18_devops_sre.topics.md › Site reliability engineering | - |
| On-call, incident triage and postmortems | covered | part18_devops_sre.topics.md › Site reliability engineering | - |
| Feature flags and staged rollouts | covered | part22_generative_ai_3of3.topics.md › Security and safety of LLM applications | - |
| Chaos experiments | covered | part18_devops_sre.topics.md › Site reliability engineering | - |
| Contract tests | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| State machines for order and job lifecycles | covered | part11_software_architecture.topics.md › Gang of Four patterns | - |

## 7.1 HTTP API
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Nasiko HTTP endpoints (API-*) | out of scope | - | - |

## 7.2 Chat-history service
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Nasiko chat-history endpoints | out of scope | - | - |

## 7.3 Router
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Router pipeline (embed, ANN shortlist, rerank, LLM pick) | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Fail-closed behaviour when the registry is down | covered | part19_machine_learning.topics.md › Applied problem families | - |

## 7.3b Auth service
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| JWT issuing and validation | covered | part14_security.topics.md › Authentication and sessions | - |

## 7.3c Agent protocol
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| A2A task states (submitted, working, terminal) | covered | part22_generative_ai_3of3.topics.md › Agents and workflows | - |
| AgentCard validation and versioning | covered | part22_generative_ai_3of3.topics.md › Agents and workflows | - |

## 7.4 Registry / Kong sync
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Periodic service sync, health checks and stale cleanup | covered | part11_software_architecture.topics.md › Architecture fundamentals | - |

## 7.5 Jobs (Redis)
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Nasiko Redis job names (JOB-*) | out of scope | - | - |

## 7.6 Data models
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Registry and session schema fields | out of scope | - | - |
| Postgres teaching schema with constraints | covered | part12_databases.topics.md › Relational theory | - |
| Query-performance fixture with partial and covering indexes | covered | part12_databases.topics.md › Storage and access methods | - |
| Transaction fixture for isolation and deadlock drills | covered | part12_databases.topics.md › Transactions and concurrency control | - |

## 7.7 Config matrix
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Nasiko config variable names | out of scope | - | - |

## 7.8 CLI
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Nasiko CLI command groups | out of scope | - | - |

## 7.9 Infra
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| CI format, type and lint checks | covered | part06_programming_languages_go.topics.md › Go — toolchain and program structure | - |

## 7.10 Ops and tests
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Runbooks for build failure, rollback and drift | covered | part14_security.topics.md › Detection and incident response | - |

## 7.11 Agents
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Sample agent implementations and NANDA adapter | out of scope | - | - |

## 9. Production and release
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Non-functional requirements (reliability, scalability, latency, cost) | covered | part11_software_architecture.topics.md › Architecture documentation | - |
| Multi-environment promotion (local, dev, staging, prod) | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| API versioning and deprecation | covered | part11_software_architecture.topics.md › API design | - |
| Backups, restore and retention | covered | part12_databases.topics.md › Operating databases | - |
| PII handling and privacy | covered | part14_security.topics.md › Privacy | - |
| RBAC and least privilege | covered | part14_security.topics.md › Principles and economics | - |
| Secret rotation | covered | part14_security.topics.md › Cryptography | - |
| TLS | covered | part09_networking.topics.md › TLS mechanics | - |
| Audit logging | covered | part12_databases.topics.md › Data modelling and design | - |
| Prompt-injection and model-abuse checks | covered | part14_security.topics.md › AI and LLM application threats | - |
| Supply chain: SBOM, image signing and provenance | covered | part14_security.topics.md › Supply chain | - |
| Model artifact lineage | partial | part19_machine_learning.topics.md › MLOps | MLflow runs and artifacts are taught; lineage from data to deployed model is not |
| Logs, metrics, traces and dashboards | covered | part18_devops_sre.topics.md › Observability | - |
| CI/CD and rollback | covered | part18_devops_sre.topics.md › CI/CD | - |
| Threat modelling of public endpoints | covered | part14_security.topics.md › Threat modelling | - |

## 11. ARCHIVE
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Python-only frameworks as implementation (FastAPI, Typer, Pydantic, LangChain) | out of scope | - | ARCHIVE |
| Java clean-code exception and null wording | out of scope | - | ARCHIVE |

## Missing in this range

## Partial in this range
- Perceptual hashing for near-duplicate images — near-duplicate image detection is taught only as the OLX case; perceptual hashing itself is not — part29_ml_case_studies_5of5.topics.md
- Entity resolution (record linkage) — record linkage is named in passing in the Wayfair case; matching and clustering methods are not taught — part29_ml_case_studies_5of5.topics.md
- pgbench benchmarking — pgbench is not named; slow-query tools and restore drills are taught — part12_databases.topics.md
- Feature store (online and offline features) — no feature-store facade or online/offline serving build — part19_machine_learning.topics.md
- Model registry (versions, approval, rollback pointer) — approval state and rollback pointer are not taught — part19_machine_learning.topics.md
- LLM token budgets and cost control — per-request token budgets are not taught — part21_generative_ai_2of3.topics.md
- Error model and error taxonomy — a designed API error taxonomy and error envelope are not taught — part09_networking.topics.md
- Request coalescing — coalescing reads by routing key is not taught — part06_programming_languages_go.topics.md
- Dead-letter queue and redrive — redrive of dead letters is not taught — part06_programming_languages_go.topics.md
- Service mesh basics — sidecar proxies and the mesh control plane are not taught — part23_cloud_providers_1of2.topics.md
- etcd-style watch and config model — watch-based config distribution is not taught — part13_distributed_systems.topics.md
- Read/write routing — application-level read/write routing and proxies are not taught — part13_distributed_systems.topics.md
- Query cache versus object cache — query-level and object-level caching are not distinguished — part13_distributed_systems.topics.md
- Prompt packing and context-window budgeting — prompt packing and budgeting are not taught — part20_generative_ai_1of3.topics.md
- Dataset snapshots and versioning — training-data snapshot manifests are not taught — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md
- Keyset pagination — named only in a lab line, with no teaching bullet — part12_databases.topics.md
- Derived read-model consistency — projection lag and rebuilds are not taught — part11_software_architecture.topics.md
- Recovery time and recovery point objectives — RTO, RPO and data-loss budgets are not defined — part16_cloud_core.topics.md
- Model artifact lineage — lineage from data to deployed model is not taught — part19_machine_learning.topics.md
