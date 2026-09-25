| Concept | Owner | Adds |
|---|---|---|
| DNS mechanics | A5 | Primer SD-08 adds routing policies (weighted, latency, geo), TTL staleness and DNS as a single point of failure; cyber NT-03/04 and DOS-02 add attacks |
| HTTP | A5 | Primer SD-29 adds idempotency/HTTP/2/3; cyber PQ-S-04 adds the browser security preview; Go companion GO-21 (`net/http`) |
| Cookie attributes (`Domain`, `Secure`, `HttpOnly`, `SameSite`, `__Host-`) | A5 HTTP | Cyber AU-01…04 adds attacks at A10 |
| TLS | A5 (mechanics) / A10 (formal) | Primer SD-35 transit slice; cyber CR-11/12 (attacks, 0-RTT, validation bugs), NT-08; Go companion GO-21 (`crypto/tls` configuration) |
| Load balancing, reverse proxy | A5 / C3 | Primer SD-10 (SSL termination, session persistence, load-balancer failover, disadvantages) and SD-11 (the load-balancer-versus-reverse-proxy rule); cyber NT-07, DOS-01 |
| Rate limiting | Cyber AB-01 (algorithms + abuse) | Primer Q22 is the design exercise and recalls AB-01; Go companion GO-19 (`golang.org/x/time/rate`) |
| Caching | Primer SD-26/27 | Cyber DOS-08 (stampede as an attack); SQL OD-09 (read path) |
| SQL injection / parameterisation | SQL SL-13 (the SQL mechanics) | Cyber WA-05 (attacker model across the whole injection family); Go companion GO-22 (placeholders and pools in `database/sql`) |
| Field / column encryption | Cyber CR-17 (the cryptography) | SQL SL-13 `pgcrypto` syntax |
| Backup/restore | SQL OD-04 (runbook) + OD-11 (Cloud SQL backups and PITR) | Cyber IR-07 (ransomware integrity) |
| 2PC / Saga / outbox | A9 (theory) | SQL CS-07 + SL-10 (the SQL that makes them true: unique index, `ON CONFLICT`, `SKIP LOCKED`; TX-5, SQL-E9.3); design-patterns ARCH-11 (shape) |
| Pub/Sub | A7 | Primer SD-28 (task queues, back pressure, delivery semantics); design-patterns DP-14 (Observer, the in-process ancestor) |
| Shared responsibility | B1 | Cyber PQ-S-03 (matrices by service model), CM-01 |
| Least privilege / IAM | B5 | Primer SD-35 (checklist); cyber CL-03…05 (IAM privilege escalation, key sprawl), AU-14 |
| Floating point | A2 | SQL PQ-03 (decimal semantics); Go companion GO-03 (no implicit conversions) |
| Discrete-math foundations of relations | SQL PQ-01/02 | SQL RT-01 |
| Security checklist (encrypt in transit/at rest, XSS, SQLi, least privilege) | Distributed per A5/A10/B5 + cyber modules | Primer SD-35 is an index module that points to each owner; its lab is shared with WA-05/SL-13 |
| Cache stampede / thundering herd | Primer SD-27 (mechanics: locking, request coalescing, TTL jitter; primer "my addition") | Cyber DOS-08 (adversarially triggered stampede) |
| Tail latency, percentiles, hedged requests | Primer SD-03/SD-38c (percentiles; design levers: timeouts, hedging, replicas) | C6/C7 (alerting/SLOs) |
| Little's law | Primer SD-03/SD-28 (L = λW; sizing checks, e.g. 400 rps × 250 ms) | the A2 slice (primer §2 stitch table) |
| CAP / PACELC | A8 (CAP statement) → A9 (formal limits, PACELC) | Primer SD-04/SD-05 (per-dataset choice, GCP store mapping) and SD-13…SD-25 (scaling techniques, SQL-versus-NoSQL decision lists); SQL CS-05/CS-07 (isolation and consistency models, formally) |
| Consistent hashing | Primer SD-38a (the ring: ~1/N of keys move, virtual nodes; sharding/rebalancing) | A4 ring slice |
| MapReduce / scatter-gather | A9 (distributed computation model) | Primer SD-38b/c, SX-08 (job patterns); V-DATA (Dataflow/Dataproc) |
| CRDTs, operational transform | A9 deepening | Primer Q04 (Google Docs design problem) |
| Vector clocks, quorums, gossip | A9 deepening | Primer Q05 (Redis-like KV design problem), SD-39 papers |
| Heavy hitters / sketches / approximate counting | A4 (probabilistic structures) | Primer Q16/Q18 (design); SQL AN-04 (SQL approximation) |
| Unique ID generation (Base62, Snowflake) | Primer SX-02/Q17 | A1 recall (bit layout) |
| Garbage collection | Go companion GO-09 (Go's collector, escape analysis, `GOGC`, `GOMEMLIMIT`) | Primer Q21 (design problem); SX-04 (data GC/TTL) |
| Event sourcing | Design-patterns ARCH-10 (shape) + A9 (theory) | Primer Q23 (stock exchange design); SQL IR/audit designs |
| Credential storage & replay | Cyber CR-13 (password KDFs) + CR-17/PV-03 (tokenization/encryption for replayable secrets) | Primer P04 (design context) + SD-35 check question |
| OOD problems O01–O07 | Primer (problems) | Design-patterns (principles and patterns they exercise); A4 recall |
| Interview/design method, back-of-the-envelope | Primer SD-00 | every later design exercise recalls it; none restates it |
| Scaling evolution (single box → millions) | Primer P08 + SX-12 | recalled wherever scale comes up; never restated |
| Terraform labs | Primer TF-1…TF-7 (P08/P01/P07 infra) | SQL TF-DB1…TF-DB6 |
| Real-world architecture papers (Dynamo, Bigtable, Spanner, GFS, Chubby, MapReduce, Dapper, Kafka, ZooKeeper…) | Primer SD-39 / §6.4 (index) | A9's academic pass (A9.D) and the university and textbook alignment table (§0.6) cite the same papers; the reading list lives once, in the primer |
| Go: language, toolchain, runtime | Go companion GO-01…GO-14 (the Go block of A3) | every Go lab in every part recalls it (rule 0.4.9); A3's Python block stays the first language |
| Concurrency | Go companion GO-15…GO-19 (goroutines, channels, `context`, `sync`, the Go memory model, data races, deadlock, the race detector) | SQL CS-05 (serializability, 2PL, snapshot isolation); A9 (distributed theory) |
| Data-structure implementations in code | A4 (concepts and costs) | Go companion GO-27 (the Go code); Primer O01, O02, O07 (the checkpoints) |
| Design patterns in Go | Design-patterns companion (the patterns) | Go companion GO-11 (the Go shape: implicit interfaces, embedding, functional options, middleware, iterators) |
| HTTP server timeouts against slow clients | Cyber DOS-05 (the attack and the values) | Go companion GO-21 (which `http.Server` field does what) |
| Password hashing in a service | Cyber CR-13 (the KDFs) | Go companion GO-07 + GO-21 (CR-13's build lab written in Go); GO-28 (a versioned record with rehash on login) |
| Authentication built in code: sessions, signed tokens, one-time codes, OAuth client | Cyber AU-01…AU-10 and CR-05…CR-07, CR-13, CR-16 (the attacks and the primitives) | Go companion GO-28 (each piece built from scratch in Go against its RFC test vectors, then with a vetted library, each with a test that replays the attack) |
| Payment-provider integration: idempotent create, signed webhooks, ledger writes, reconciliation | Go companion GO-29 (the integration code) | SQL DD-03 (the ledger rules it follows); Cyber PV-03 (tokenization, PCI DSS scope) and AB-06/AB-07 (checkout abuse); Primer SD-28 (queues, back-pressure) |
| TCP vs UDP | A5 | Primer SD-30/31 (when-to-use rules, connection pooling) |
| REST / gRPC | A7 | Primer SD-32/33/34 (RPC-versus-REST decision, HATEOAS) |
| OAuth and JWT, as named in A7 | A7 (mention) | Cyber AU and CR failure modes (algorithm confusion, mix-up) |
| Microservices, service discovery | A7; Primer SD-12 | Design-patterns: the class-level patterns (Strategy, Observer) that compose into them |
| Classes, objects, constructors, inheritance mechanics | A3 (operational OOP, the `Dog` example) | Design-patterns F-01…F-04 (formal theory) and F-03, PR-03 (the is-a contract and its limits) |
| Big-O, hash lookup, indexes | A2 / A4 | Primer SD-19 (index trade-offs), SX-11; SQL PQ-07 (recall only) |
| Replication, sharding, consensus | A9 | Primer SD-06, SD-14, SD-15, SD-17, SD-38 |
| SQL scale-out (replication, federation, sharding, denormalisation, SQL tuning) | Primer SD-13 … SD-19 | SQL CS-07, DD-13, OD-05, OD-07 (engine-level and SQL-level detail only) |
| Spanner, Bigtable, Firestore and the store choice | Primer SD-22 / SD-23 / SD-25 | SQL AN-05, AN-06 (same-question comparisons); DD-13 (key design in SQL) |
| Hot partitions, key histograms | SQL DD-13 (key histogram) + Primer SD-23 (row keys) | SQL DD-13 (the skew query on the lab data; PX-1) |
| Availability vs durability, nines | A9 / C7 | Primer SD-07 (tables, series and parallel formulas) |
| HA, horizontal vs vertical scaling, DR | B3 | Primer SD-06, SD-10 and the P08 walk-through; design-patterns treats HA/DR as infrastructure, not code architecture |
| Autoscaling (HPA, MIG) | C2 / V-COMP | Primer P08 "Users++++" |
| Observability, SRE | C6 / C7 | Primer P08 (monitoring list, back pressure) |
| Container non-root, Pod Security Standards | C1 / C2 | Cyber CK (escape and supply-chain attacker paths) |
| KMS and CMEK | Phase 4 Security | Cyber CR-14 (envelope hierarchy, compromise response) |
| Cloud Armor and DDoS product names | V-NET / Phase 4 Networking | Cyber DOS taxonomy, rate-limit and bot design |
| Row-level security for multi-tenancy | A8 + SQL DD-09 (design) | SQL SL-13 (policy syntax, `FORCE`, owner bypass); SQL-E10.2 (composite foreign key as defence in depth), SQL-E10.6 |
| Billing-export SQL | B4 | SQL AN-03 (the same windows reused; no new concept) |
| Cloud SQL provisioning, Auth Proxy, private IP, HA, flags | SQL OD-11 | SQL OD-03/04/05 (session state versus pooler modes, RPO/RTO arithmetic, replica lag); SQL §8.2 Terraform |
| Migrations as jobs, expand/contract | SQL OD-08 (jobs) + DD-11 (expand/contract) | SQL DD-11 (lock levels, `NOT VALID` + `VALIDATE`, `CREATE INDEX CONCURRENTLY`), SQL-E9.6 (backfill batching) |
| Cursor pagination | SQL OD-09 (seek predicate, index, from-scratch pager) | SQL PX-9 (measured against `OFFSET`) |
| Connection-pool arithmetic | SQL OD-03 (worksheet) | SQL OD-03 (pooler modes, and what breaks in transaction mode) |
| Ledgers, integer minor units | SQL DD-03 (ledger rules) | SQL DD-05 (modelling); SQL-E4.5, SQL-CAP2 (revenue reconciliation); SQL-CAP1 (invariants) |
| BigQuery partitioning, clustering, cost | SQL AN-02 | SQL DT drills |
| As-of (point-in-time) joins | SQL DD-05 (leakage) | SQL-E6.4, SQL-E13.4, SQL-E13.5 (lateral, range join, SCD2) |
| The SQL engine slices DB-1…DB-10 | SQL §4.0 (each slice and its toy) | the pairing table in SQL §2.1 names the theory, rung and cards that ride with each; no slice gets a second toy |
| LLM mechanics: tokenization, next-token prediction, attention, decoding, alignment | D4 (D4.D1–D4.D5); D2 (backpropagation) | Forward Deployed Engineer companion LB-1…LB-6 (the from-scratch builds; they recall the theory, never re-teach it) |
| Prompt engineering | D4 (zero-shot, few-shot and system prompts as concepts) | Forward Deployed Engineer companion FDE-08 (the craft, templates, versioning) |
| Embeddings, retrieval-augmented generation, hybrid search | D4 (the concept; D4.D5); D5.D1 (ranking theory) | Forward Deployed Engineer companion LB-7 (the rankers built) and FDE-25 (the production pipeline); SQL AN-07 (search and vectors in Postgres); cyber AI-03 (leakage through retrieval) |
| Prompt injection; tool and agent abuse | Cyber AI-01, AI-02 (the attacks; labs SEC-E8.3, SEC-E8.4) | Forward Deployed Engineer companion FDE-20 (the learner's own agent attacked; the Claude-side controls, hooks, the lethal trifecta) |
| Agentic patterns and agents | D4 (named as concepts) | Forward Deployed Engineer companion FDE-15…FDE-17 (built, with the Agent SDK); the Agentic Architect certification (ADK, A2A) |
| Evaluating LLM applications | Forward Deployed Engineer companion FDE-22, FDE-23 | D1 (metrics), D3.D4 (online experiments) and D5.D2 (the statistics) are recalled |
| Retries, backoff and overload handling for model APIs | Design-patterns ARCH-12 (retry, backoff, jitter, degradation) | Forward Deployed Engineer companion FDE-04 (429 and 529), FDE-24 (retry storms); Go companion GO-19 |
| TypeScript and Node | Forward Deployed Engineer companion FDE-01, FDE-02 | rule 0.4.9 (the third language) |
| JSON Schema, JSON-RPC 2.0, Server-Sent Events | Forward Deployed Engineer companion FDE-03 | FDE-04 (the Messages API stream), FDE-13 (MCP's envelope) |
| Model Context Protocol (MCP) | Forward Deployed Engineer companion FDE-13, FDE-14 | the Agentic Architect certification's notes name it |
| OAuth for remote tool servers | Cyber AU modules (OAuth, tokens, the attacks); Go companion GO-28 (PKCE built) | Forward Deployed Engineer companion FDE-14 (MCP authorization: protected-resource metadata, audience checks) |
| Architecture decisions and decision records | A7.10 (the record, its form and the documentation around it); A7.D4 (evaluating an architecture against quality-attribute scenarios) | Main course B6 (how a decision is made: options, premortem, reversibility, review date; B6.D1–B6.D3 its mathematics); rule 0.4.12 (the decision journal) |
| Estimation | System Design Primer companion SD-00 and SDA.10 (sizing a system: back-of-the-envelope numbers) | Main course A7.D6 (estimation error); B6.D3 (forecasting work and outcomes: calibration, the Brier score, reference classes) |
| Migrating a running system | Design-patterns ARCH-12 (the strangler fig); C4 (canaries and progressive delivery); SQL companion DD-11 (expand/contract) | Main course B6 (the migration as a sequence of reversible steps: parallel runs, shadow traffic, dark launches, the point of no return); the PCA part's migration line (the six Rs mapped to landings) |
| Incidents and postmortems | C7 (incident management, the blameless postmortem, C7.D3; the case library of public postmortems) | Main course B6.5 (reading a postmortem as a design review in hindsight); Forward Deployed Engineer companion FDE-24 (debugging a Claude application) |
| Conway's law and team design | A7.D1 (Conway's law) | Main course B6 (the inverse Conway manoeuvre, team types and interaction modes, cognitive load) |
| Track record and portfolio | Forward Deployed Engineer companion §15 (the FDE track record and interviews) | Main course B6 (the architect's portfolio and interview, which extend it) |
| Build or buy, and total cost of ownership | B4.D1 (total cost of ownership, break-even) | Main course B6 (build, buy, rent or adopt; lock-in priced as a switching cost) |
| Recommenders, learning to rank and ads ranking | D6 (D6.F1, D6.F2, the ranker D6.B1; position bias in D6.D1) | D1 (named as literacy); D5.D1 (BM25, fusion and the ranking measures); Forward Deployed Engineer companion LB-7 (retrieval rankers built) |
| Bandits and exploration | D6.D2 (regret, UCB1, Thompson sampling, contextual bandits) | D1 (named as literacy); D3.D4 (the A/B test a bandit is contrasted with) |
| Uplift, incrementality and holdouts | D6.D4 (potential outcomes, uplift) and D6.F8 (the holdout in a campaign) | D1 (why a lift claim needs a control group); D3.D4 (sample size) |
| Time-series forecasting and ETAs | D6.F3 and D6.B2; D6.D3 (quantile loss, coverage against width) | D1 (seasonality and backtesting, as literacy) |
| Fraud scoring on payment tokens | D6.F4 and D6.B3 (the model, the threshold, the review queue) | Go companion GO-29 (the payment path built); cyber PV-03 (tokenization against encryption) |
| Training–serving skew and drift in production | D3 (D3.D2, the tests) | D6.1 (kept apart from leakage per family) and the monitors of D6.F1…D6.F10 |
| Model canaries and shadow deployments | D3 (A/B testing and canary rollouts for models) | D6.F10 (a different dial from C4's application canary) |
