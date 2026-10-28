# Topic diff: Tool subcourses, system design track, production and glossary

Source: gcp/unified-curriculum.md lines 4328-4518 and 4806-4837. Compared against: gcp-lite/index/*.topics.md and gcp-lite/Rust_Track_AI_Infrastructure.md.

Counts: 204 topics; 153 covered, 41 partial, 7 missing, 3 out of scope.

## 4. Tool and platform subcourses

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Git and GitHub workflow | covered | part15_software_delivery.topics.md › Git | - |
| Docker and Docker Compose | covered | part18_devops_sre.topics.md › Docker | - |
| BuildKit image builds | partial | part18_devops_sre.topics.md › Docker | named in one bullet; no build-backend depth |
| Kubernetes deployments | covered | part18_devops_sre.topics.md › Kubernetes | - |
| Helm charts | covered | part18_devops_sre.topics.md › Kubernetes | - |
| Terraform | covered | part18_devops_sre.topics.md › Infrastructure as code | - |
| Kong gateway and Lua plugins | partial | part18_devops_sre.topics.md › NGINX and API gateways | Kong routes, plugins and admin covered; Lua basics not taught |
| NGINX | covered | part18_devops_sre.topics.md › NGINX and API gateways | - |
| MongoDB | partial | part12_databases.topics.md › NoSQL and choosing a store | document-store model taught; MongoDB itself, indexes and CRUD not |
| Redis data store and cache | partial | part23_cloud_providers_1of2.topics.md › Google Cloud — storage and databases | Redis named only via Memorystore; no Redis commands or cache setup |
| Redis Streams and consumer groups | covered | part18_devops_sre.topics.md › Observability | - |
| PostgreSQL with pgvector and psql | covered | part12_databases.topics.md › Pre-SQL foundations | pgvector also in Analytics and other engines |
| PostgreSQL ops tools (pg_stat_statements, pgbench, pg_dump, PITR) | partial | part12_databases.topics.md › Operating databases | pgbench benchmarking not named; the rest covered |
| OpenTelemetry tracing | covered | part18_devops_sre.topics.md › Observability | - |
| Phoenix LLM tracing UI | partial | part18_devops_sre.topics.md › Observability | named in one list only |
| Cobra and Viper CLIs | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library | - |
| Service client libraries (mongo-go-driver, go-redis, client-go, Docker Engine API) | partial | part06_programming_languages_go.topics.md › Go — the everyday standard library | named in one list with learning tests; not taught |
| Vector stores and k-NN search (Qdrant, pgvector, FAISS) | covered | part20_generative_ai_1of3.topics.md › Embeddings and retrieval | - |
| Gonum numerical stack | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library | - |
| Go ML runtime adapters (Gorgonia, GoMLX, ONNX Runtime) | partial | part06_programming_languages_go.topics.md › Go — the everyday standard library | named in one lab bullet only |
| Feature store (point-in-time, freshness) | covered | part19_machine_learning.topics.md › MLOps | - |
| Model registry | covered | part19_machine_learning.topics.md › MLOps | - |
| Drift detection | covered | part19_machine_learning.topics.md › MLOps | - |
| Evaluator CLI and rollback gate | partial | part19_machine_learning.topics.md › Exercises | taught only as exercise items; no evaluation-gate topic |
| OpenAI-compatible HTTP API and Go SDKs | covered | part21_generative_ai_2of3.topics.md › Model APIs | - |
| Structured output (JSON Schema) | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | - |
| JSON-RPC 2.0 | covered | part07_programming_languages_typescript_wire_theory_exercises.topics.md › Wire formats | - |
| LLM tool calling, token limits, rate limits and safety | partial | part21_generative_ai_2of3.topics.md › Tools and the Model Context Protocol | tool loop and safety covered; LLM rate limits and token budgets not taught |
| Ollama local models | covered | part21_generative_ai_2of3.topics.md › Model APIs | - |
| Go HTTP frameworks and net/http | covered | part06_programming_languages_go.topics.md › Go — engineering | - |

## HLD, LLD, and clean architecture

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| High-level design (service boundaries, data flows, capacity) | covered | part11_software_architecture.topics.md › Architecture documentation | - |
| Mermaid diagram notation | missing | → suggest part11 | no Mermaid in gcp-lite |
| Low-level design (APIs, state, transaction scopes) | partial | part11_software_architecture.topics.md › API design | pieces covered across parts 06 and 11; no LLD method taught |
| Clean architecture and DDD | covered | part11_software_architecture.topics.md › Application architecture | - |
| Repository pattern | covered | part11_software_architecture.topics.md › Application architecture | - |
| Unit of work | partial | part11_software_architecture.topics.md › Application architecture | named in one list only |
| Adapter pattern | covered | part11_software_architecture.topics.md › Gang of Four patterns | - |
| Strategy pattern | covered | part11_software_architecture.topics.md › Gang of Four patterns | - |
| Factory and builder patterns | covered | part11_software_architecture.topics.md › Gang of Four patterns | - |
| Decorator and middleware | covered | part11_software_architecture.topics.md › Gang of Four patterns | - |
| Chain of responsibility | covered | part11_software_architecture.topics.md › Gang of Four patterns | - |
| Observer and pub-sub | covered | part11_software_architecture.topics.md › Gang of Four patterns | - |
| Mediator | covered | part11_software_architecture.topics.md › Gang of Four patterns | - |
| Command pattern | covered | part11_software_architecture.topics.md › Gang of Four patterns | - |
| State pattern | covered | part11_software_architecture.topics.md › Gang of Four patterns | - |
| Circuit breaker | covered | part11_software_architecture.topics.md › Distributed application patterns | - |
| Bulkhead | covered | part11_software_architecture.topics.md › Distributed application patterns | - |
| Retry with exponential backoff and jitter | covered | part06_programming_languages_go.topics.md › Go — concurrency | - |
| Timeouts and deadlines | covered | part06_programming_languages_go.topics.md › Go — concurrency | - |
| Idempotency keys and idempotent consumers | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Transactional outbox | covered | part13_distributed_systems.topics.md › Distributed transactions | - |
| Saga pattern | covered | part13_distributed_systems.topics.md › Distributed transactions | - |
| CQRS and read models | covered | part11_software_architecture.topics.md › Distributed application patterns | - |
| Strangler fig migration | covered | part11_software_architecture.topics.md › Distributed application patterns | - |

## 5. System design track

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Six-step system design approach (FR/NFR, capacity, HLD, LLD, trade-offs, SLOs) | partial | part13_distributed_systems.topics.md › System design method | a four-step interview method is taught; the six-step write-up with trade-off table is not |
| Functional and non-functional requirements | partial | part11_software_architecture.topics.md › Architecture documentation | NFR tables named; requirement elicitation not taught |
| Capacity estimation | covered | part13_distributed_systems.topics.md › Performance at scale | - |
| Service-level objectives (SLOs) | covered | part18_devops_sre.topics.md › Site reliability engineering | - |
| Rollback and rollout paths | partial | part18_devops_sre.topics.md › CI/CD | canary and blue-green covered; rollback plans named only for migrations |
| Case-study analysis method (ADR and tiny model) | partial | part13_distributed_systems.topics.md › System design method | case studies in parts 25–29; the ADR-plus-tiny-model step is not taught |
| Backpressure and bounded queues | covered | part13_distributed_systems.topics.md › Asynchronism and flow control | - |
| Load shedding | covered | part13_distributed_systems.topics.md › Asynchronism and flow control | - |
| Dead-letter queue and redrive | partial | part06_programming_languages_go.topics.md › Go — engineering | named in webhook retries and Pub/Sub; not taught as a pattern |
| Request coalescing | covered | part06_programming_languages_go.topics.md › Go — concurrency | single-flight loading |
| Hot partitions and hot keys | covered | part13_distributed_systems.topics.md › Partitioning | - |
| Consistent hashing | covered | part13_distributed_systems.topics.md › Partitioning | - |
| Zero-downtime migrations (expand and contract) | covered | part12_databases.topics.md › Operating databases | - |
| Graceful degradation | covered | part11_software_architecture.topics.md › Distributed application patterns | - |
| Throttling and rate limiting | covered | part06_programming_languages_go.topics.md › Go — concurrency | token-bucket rate limiting |
| Ranking diversity and NDCG | partial | part19_machine_learning.topics.md › Applied problem families | NDCG covered; diversity reranking named only |
| Bipartite graph anomaly features | covered | part19_machine_learning.topics.md › Specialised learning areas | - |
| Context packing and window budgeting | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | - |

## 5a Primer topic index

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Performance vs scalability | covered | part13_distributed_systems.topics.md › Performance at scale | - |
| Latency vs throughput | covered | part13_distributed_systems.topics.md › Performance at scale | - |
| CAP theorem (CP vs AP) | covered | part13_distributed_systems.topics.md › Foundations | - |
| Weak, eventual and strong consistency | covered | part13_distributed_systems.topics.md › Foundations | - |
| Active-passive and active-active failover | covered | part09_networking.topics.md › Middleboxes, proxies and load balancing | - |
| Nines and series vs parallel availability | covered | part16_cloud_core.topics.md › Cloud economics and FinOps | serial composition covered |
| DNS record types (NS, MX, A, CNAME) | covered | part09_networking.topics.md › DNS | - |
| DNS TTL and weighted, latency and geo routing | covered | part09_networking.topics.md › DNS | - |
| CDN push vs pull | covered | part09_networking.topics.md › Middleboxes, proxies and load balancing | - |
| L4 vs L7 load balancing | covered | part09_networking.topics.md › Middleboxes, proxies and load balancing | - |
| Session persistence and SSL termination | covered | part09_networking.topics.md › Middleboxes, proxies and load balancing | - |
| Horizontal vs vertical scaling | covered | part13_distributed_systems.topics.md › Performance at scale | - |
| Reverse proxy vs load balancer | covered | part09_networking.topics.md › Middleboxes, proxies and load balancing | - |
| Microservices and monolith styles | covered | part11_software_architecture.topics.md › Architecture fundamentals | - |
| Service discovery | covered | part11_software_architecture.topics.md › Architecture fundamentals | - |
| Relational algebra | covered | part12_databases.topics.md › Relational theory | - |
| ACID transactions | covered | part12_databases.topics.md › Transactions and concurrency control | - |
| MVCC | covered | part12_databases.topics.md › Transactions and concurrency control | - |
| Database indexes (B-tree, hash, GIN, BRIN) | covered | part12_databases.topics.md › Storage and access methods | - |
| Query planning and EXPLAIN | covered | part12_databases.topics.md › Query processing | - |
| Master-slave and master-master replication | covered | part13_distributed_systems.topics.md › Replication | - |
| Federation (functional partitioning) | covered | part13_distributed_systems.topics.md › Partitioning | - |
| Sharding | covered | part13_distributed_systems.topics.md › Partitioning | - |
| Denormalization | covered | part12_databases.topics.md › Data modelling and design | - |
| SQL tuning | covered | part12_databases.topics.md › Query processing | - |
| Write-ahead log (WAL) | covered | part12_databases.topics.md › Recovery and replication | - |
| Backup and restore | covered | part12_databases.topics.md › Operating databases | - |
| Replication lag and read/write routing | covered | part12_databases.topics.md › Recovery and replication | - |
| BASE vs ACID | covered | part12_databases.topics.md › NoSQL and choosing a store | - |
| NoSQL data models (key-value, document, wide-column, graph) | covered | part12_databases.topics.md › NoSQL and choosing a store | - |
| SQL vs NoSQL choice | covered | part12_databases.topics.md › NoSQL and choosing a store | - |
| Cache layers and query vs object caching | covered | part13_distributed_systems.topics.md › Caching at scale | - |
| Cache-aside | partial | part13_distributed_systems.topics.md › Caching at scale | named in one list; no mechanics |
| Write-through and write-behind caching | partial | part13_distributed_systems.topics.md › Caching at scale | named in one list; no mechanics |
| Refresh-ahead caching | partial | part13_distributed_systems.topics.md › Caching at scale | named in one list; no mechanics |
| Message queues vs task queues | covered | part13_distributed_systems.topics.md › Asynchronism and flow control | - |
| At-least-once vs exactly-once delivery | covered | part13_distributed_systems.topics.md › Distributed transactions | - |
| TCP vs UDP | covered | part09_networking.topics.md › Transport | - |
| RPC vs REST | covered | part11_software_architecture.topics.md › API design | - |
| Security (primer section) | partial | part14_security.topics.md › Principles and economics | name only; security covered broadly |
| Powers of two | covered | part02_computer_organization.topics.md › Data representation | - |
| Latency numbers every programmer should know | covered | part02_computer_organization.topics.md › Machine organization | - |

## 5a-SQL PostgreSQL and database-systems application matrix

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Bag vs set semantics | covered | part12_databases.topics.md › Relational theory | - |
| Three-valued logic (NULLs) | covered | part12_databases.topics.md › Pre-SQL foundations | - |
| Table constraints (PK, FK, CHECK, deferrable) | covered | part12_databases.topics.md › Relational theory | - |
| JSONB, range and UUID types | covered | part12_databases.topics.md › The SQL language | - |
| System catalogs and system columns | missing | → suggest part12 | not in gcp-lite |
| Slotted pages and TOAST | covered | part12_databases.topics.md › Storage and access methods | - |
| External merge sort | covered | part08_data_structures_algorithms.topics.md › Sorting, searching and strings | - |
| Bitmap and index-only scans | covered | part12_databases.topics.md › Storage and access methods | - |
| Isolation levels | covered | part12_databases.topics.md › Transactions and concurrency control | - |
| Tuple versions, HOT, vacuum and freezing | covered | part12_databases.topics.md › Transactions and concurrency control | - |
| Locks and deadlocks | covered | part12_databases.topics.md › Transactions and concurrency control | - |
| Shared buffers, background writer and checkpointer | covered | part12_databases.topics.md › Storage and access methods | - |
| Full-page writes and crash recovery | covered | part12_databases.topics.md › Recovery and replication | - |
| Streaming replication and point-in-time recovery | covered | part12_databases.topics.md › Recovery and replication | - |
| Selectivity and top-k queries | partial | part12_databases.topics.md › Query processing | selectivity covered; top-k queries not named |

## 5a-ML Production ML-system case-study atlas

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| BM25 ranking | covered | part19_machine_learning.topics.md › Applied problem families | - |
| TF-IDF | covered | part19_machine_learning.topics.md › Natural language processing foundations | - |
| Tokenizers (byte-pair encoding) | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Learning to rank (pairwise) | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Recall@k ranking metric | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Cold-start problem | partial | part19_machine_learning.topics.md › Applied problem families | named in problem framing only |
| Time-series forecasting baselines | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Quantile forecasting | partial | part19_machine_learning.topics.md › Applied problem families | pinball loss and prediction intervals taught; quantile forecasting as a method not named |
| Feature freshness checks | covered | part19_machine_learning.topics.md › MLOps | - |
| Assignment and linear-programming scheduling | covered | part03_mathematics.topics.md › Calculus and optimization | - |
| Streaming windows (tumbling, sliding, session) | covered | part13_distributed_systems.topics.md › Stream and batch processing | - |
| Anomaly detection | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| PageRank and random-walk embeddings | covered | part19_machine_learning.topics.md › Specialised learning areas | - |
| Entity resolution and blocking | covered | part19_machine_learning.topics.md › Specialised learning areas | - |
| Threshold selection and review queues | partial | part19_machine_learning.topics.md › Applied problem families | cost-weighted thresholds covered; review queues not |
| Audit trail | covered | part19_machine_learning.topics.md › MLOps | - |
| Adversarial test sets | partial | part19_machine_learning.topics.md › Applied problem families | adversarial drift named; test-set method not taught |
| RAG evaluation | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | - |
| Prompt-injection tests | covered | part14_security.topics.md › AI and LLM application threats | - |
| Perceptual hashing | covered | part19_machine_learning.topics.md › Specialised learning areas | - |
| Spectrograms and audio features | covered | part19_machine_learning.topics.md › Specialised learning areas | - |
| Convolution | covered | part19_machine_learning.topics.md › Deep learning | - |
| Embedding adapters | partial | part20_generative_ai_1of3.topics.md › Multimodal models | adapter idea covered for multimodal; embedding-level adapters not taught |
| Multimodal retrieval evaluation | covered | part19_machine_learning.topics.md › Specialised learning areas | - |
| Dataset snapshot manifest | covered | part19_machine_learning.topics.md › MLOps | - |
| Training-serving skew and batch/stream parity | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Shadow and canary model rollout | covered | part19_machine_learning.topics.md › MLOps | - |
| Distributed training | missing | → suggest part19 | only named in case studies |
| Epsilon-greedy, UCB and Thompson sampling | covered | part03_mathematics.topics.md › Decision mathematics | - |
| Contextual bandits | covered | part03_mathematics.topics.md › Decision mathematics | - |
| Off-policy replay | partial | part19_machine_learning.topics.md › Applied problem families | inverse-propensity scoring named; replay not taught |
| A/B assignment and exposure logging | covered | part19_machine_learning.topics.md › MLOps | - |
| Bootstrap intervals | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| CUPED variance reduction | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| Propensity weighting and uplift modelling | covered | part03_mathematics.topics.md › Statistics and experimental design | - |

## 5e HLD/LLD/microservices/design-pattern implementation ladder

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Service mesh basics | partial | part23_cloud_providers_1of2.topics.md › Google Cloud — networking | Cloud Service Mesh named; mesh concepts not taught |
| Synchronous vs asynchronous service calls | covered | part11_software_architecture.topics.md › Architecture fundamentals | - |
| Orchestration vs choreography | covered | part13_distributed_systems.topics.md › Distributed transactions | - |
| Schema ownership per service | missing | → suggest part11 | not in gcp-lite |
| Blast radius | partial | part17_architects_practice.topics.md › Learning from failure | named in one postmortem bullet |
| Sequence diagrams | missing | → suggest part11 | not in gcp-lite |
| Contract tests | partial | part11_software_architecture.topics.md › API design | contracts generate contract tests; test method not taught |
| Health checks | covered | part09_networking.topics.md › Middleboxes, proxies and load balancing | - |
| Architecture decision records (ADR) | covered | part11_software_architecture.topics.md › Architecture documentation | - |
| etcd-style watch and config model | partial | part13_distributed_systems.topics.md › Consensus and coordination | etcd named; watch semantics not taught |
| Temporal-style durable workflow retry state | missing | → suggest part13 | not in gcp-lite |

## 9. Production and release

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Multi-environment config layering | partial | part06_programming_languages_go.topics.md › Go — the everyday standard library | config precedence taught; local/dev/staging/prod layering not |
| Feature flags | partial | part22_generative_ai_3of3.topics.md › Security and safety of LLM applications | flags named in LLM release safety; no release-flag practice |
| API versioning and deprecation | partial | part11_software_architecture.topics.md › API design | versioning named; deprecation not taught (model deprecation in part21) |
| Schema migrations and backward compatibility | covered | part12_databases.topics.md › Operating databases | - |
| Data retention and PII handling | covered | part14_security.topics.md › Principles and economics | - |
| RBAC and least privilege | covered | part14_security.topics.md › Principles and economics | - |
| Secret rotation | covered | part23_cloud_providers_1of2.topics.md › Google Cloud — security | Secret Manager versions and rotation; part14 Cryptography has rotation with dual-key overlap |
| TLS in transit | covered | part09_networking.topics.md › TLS mechanics | - |
| Audit logging | covered | part12_databases.topics.md › Data modelling and design | append-only audit tables |
| Software bill of materials (SBOM) | covered | part14_security.topics.md › Supply chain | - |
| Image signing and build provenance | covered | part14_security.topics.md › Supply chain | - |
| Container image scanning | covered | part18_devops_sre.topics.md › Docker | - |
| Logs, metrics and traces | covered | part18_devops_sre.topics.md › Observability | - |
| Alerts, dashboards and runbooks | partial | part18_devops_sre.topics.md › Site reliability engineering | alerting covered; runbooks and dashboards not named |
| Incident management and postmortems | covered | part18_devops_sre.topics.md › Site reliability engineering | - |
| Load and stress testing | covered | part13_distributed_systems.topics.md › Performance at scale | - |
| pprof profiling | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Inference latency and batch throughput | partial | part19_machine_learning.topics.md › MLOps | batching named; latency and throughput measurement not taught |
| LLM token budgets | partial | part22_generative_ai_3of3.topics.md › Agents and workflows | token budget appears only as an agent-loop bound |
| Cost attribution and cost per decision | covered | part16_cloud_core.topics.md › Cloud economics and FinOps | unit economics per request or transaction |
| CI/CD pipelines | covered | part18_devops_sre.topics.md › CI/CD | - |
| Staging promotion | partial | part07_programming_languages_typescript_wire_theory_exercises.topics.md › Exercises | named in one exercise only |
| Operational readiness review (ORR) | missing | → suggest part18 | not in gcp-lite |
| Threat modelling public endpoints | covered | part14_security.topics.md › Threat modelling | - |
| Model-evaluation dashboards | partial | part19_machine_learning.topics.md › MLOps | monitoring and drift covered; evaluation dashboards not named |
| Evaluation rubric (API auth, orchestrator idempotency, routing, SLOs) | out of scope | - | Nasiko project rubric |

## 10. Glossary

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| A2A protocol | covered | part22_generative_ai_3of3.topics.md › Agents and workflows | - |
| AgentCard | out of scope | - | Nasiko project schema (SCHEMA-REG-001) |
| NADT, SUGL and SYNTAX UNLOCK | out of scope | - | course-internal labels |

## Missing in this range

- Distributed training (→ suggest part19) — from: 5a-ML Production ML-system case-study atlas
- System catalogs and system columns (→ suggest part12) — from: 5a-SQL PostgreSQL and database-systems application matrix
- Mermaid diagram notation (→ suggest part11) — from: HLD, LLD, and clean architecture
- Schema ownership per service (→ suggest part11) — from: 5e HLD/LLD/microservices/design-pattern implementation ladder
- Sequence diagrams (→ suggest part11) — from: 5e HLD/LLD/microservices/design-pattern implementation ladder
- Temporal-style durable workflow retry state (→ suggest part13) — from: 5e HLD/LLD/microservices/design-pattern implementation ladder
- Operational readiness review (ORR) (→ suggest part18) — from: 9. Production and release

## Partial in this range

- BuildKit image builds — named in one bullet; no build-backend depth — part18_devops_sre.topics.md
- Kong gateway and Lua plugins — Kong covered; Lua basics not taught — part18_devops_sre.topics.md
- MongoDB — document-store model taught; MongoDB itself, indexes and CRUD not — part12_databases.topics.md
- Redis data store and cache — Redis named only via Memorystore — part23_cloud_providers_1of2.topics.md
- PostgreSQL ops tools — pgbench benchmarking not named — part12_databases.topics.md
- Phoenix LLM tracing UI — named in one list only — part18_devops_sre.topics.md
- Service client libraries — named in one list with learning tests; not taught — part06_programming_languages_go.topics.md
- Go ML runtime adapters — named in one lab bullet only — part06_programming_languages_go.topics.md
- Evaluator CLI and rollback gate — taught only as exercise items — part19_machine_learning.topics.md
- LLM tool calling, token limits, rate limits and safety — LLM rate limits and token budgets not taught — part21_generative_ai_2of3.topics.md
- Low-level design — pieces covered across parts 06 and 11; no LLD method taught — part11_software_architecture.topics.md
- Unit of work — named in one list only — part11_software_architecture.topics.md
- Six-step system design approach — four-step method taught; six-step write-up with trade-off table not — part13_distributed_systems.topics.md
- Functional and non-functional requirements — NFR tables named; elicitation not taught — part11_software_architecture.topics.md
- Rollback and rollout paths — canary and blue-green covered; rollback plans only for migrations — part18_devops_sre.topics.md
- Case-study analysis method — ADR-plus-tiny-model step not taught — part13_distributed_systems.topics.md
- Dead-letter queue and redrive — named in webhook retries and Pub/Sub; not taught as a pattern — part06_programming_languages_go.topics.md
- Ranking diversity and NDCG — diversity reranking named only — part19_machine_learning.topics.md
- Cache-aside — named in one list; no mechanics — part13_distributed_systems.topics.md
- Write-through and write-behind caching — named in one list; no mechanics — part13_distributed_systems.topics.md
- Refresh-ahead caching — named in one list; no mechanics — part13_distributed_systems.topics.md
- Security (primer section) — name only — part14_security.topics.md
- Selectivity and top-k queries — top-k queries not named — part12_databases.topics.md
- Cold-start problem — named in problem framing only — part19_machine_learning.topics.md
- Quantile forecasting — pinball loss and prediction intervals taught; quantile forecasting not named — part19_machine_learning.topics.md
- Threshold selection and review queues — review queues not covered — part19_machine_learning.topics.md
- Adversarial test sets — test-set method not taught — part19_machine_learning.topics.md
- Embedding adapters — embedding-level adapters not taught — part20_generative_ai_1of3.topics.md
- Off-policy replay — replay not taught — part19_machine_learning.topics.md
- Service mesh basics — mesh concepts not taught — part23_cloud_providers_1of2.topics.md
- Blast radius — named in one postmortem bullet — part17_architects_practice.topics.md
- Contract tests — test method not taught — part11_software_architecture.topics.md
- etcd-style watch and config model — watch semantics not taught — part13_distributed_systems.topics.md
- Multi-environment config layering — local/dev/staging/prod layering not taught — part06_programming_languages_go.topics.md
- Feature flags — no release-flag practice — part22_generative_ai_3of3.topics.md
- API versioning and deprecation — deprecation not taught — part11_software_architecture.topics.md
- Alerts, dashboards and runbooks — runbooks and dashboards not named — part18_devops_sre.topics.md
- Inference latency and batch throughput — latency and throughput measurement not taught — part19_machine_learning.topics.md
- LLM token budgets — token budget appears only as an agent-loop bound — part22_generative_ai_3of3.topics.md
- Staging promotion — named in one exercise only — part07_programming_languages_typescript_wire_theory_exercises.topics.md
- Model-evaluation dashboards — evaluation dashboards not named — part19_machine_learning.topics.md
