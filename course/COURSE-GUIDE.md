# Course Guide — how to teach the Consolidated Cloud Mastery course

For the tutor. Read this file first, at the start of every session, before any course file. The course has seven parts, one file each. The parts hold the material; this guide holds everything about *how* the course is taught and kept, and holds it once:

- §1 — how every session starts, and where to find things;
- §2 — the seven course files: what each owns, its IDs, and where its keys are;
- §3 — the rules every part follows (rules 0.1–0.5). A reference to "rule 0.x" in any part means a rule in this section;
- §4 — how to manage the course files, so that nothing is taught or written twice;
- §5 — the outline of all seven parts, generated from their headings.

**The aim** is the role, not the certificates; the main course states it at the end of "Why this order" (its §1). Every session serves it through rule 0.4.12.

The learner reads the parts. The tutor reads this guide as well.

## 1. Start of every session

1. **Read this guide** (§1–§4). Use §5 to find a module without opening a whole part.
2. **Find the resume point.** Check, in this order: the resume point named at the last session's close (rule 0.4.8), which the learner may paste in; then the ticked `- [ ]` boxes in the parts; then the phase plan in the main course (§1 of the main course). If nothing is ticked and no ledger is given, the course is a fresh start and begins at A1.
3. **Anchor the session.** Open the main course at the module. In each companion's §2 stitch table, find the rows for that module. Those rows list the companion IDs that are taught in the same session (rule 0.1).
4. **Open only what is bound.** In each part, read its §0, then only the blocks for today's IDs. Search by ID (`SD-10`, `SL-06`, `GO-17`, `AU-03`). Never reload a whole part. Open keys, rubrics and reference solutions only after the learner has attempted the item.
5. **Teach** by the Suite Session Protocol (rule 0.4.2), within the contract (rule 0.4), the learner's preferences (rule 0.2) and Lab Safety (rule 0.5).
6. **Close** by rule 0.4.8: tick the boxes in every part, and emit the ledger delta and the exact resume point.

Where to find things:

| You need | Look in |
|---|---|
| What to teach next, and in what order | Main course §1 (the phase plan) and its Parts I–IV (Tracks A–D); Parts V–VII for the certification tracks |
| The companion IDs that ride with a main-course module | Each companion's §2 stitch table (the SQL companion also has §2.1, the engine-slice pairing, and §2.2, the parallel calendar) |
| Who teaches a shared concept, and who only adds to it | Rule 0.3 (the ownership register) |
| A module's check key, a problem key or a rubric | The keys section of the part that owns the item (§2 below) |
| Whether the learner may skip a block | The part's skip-tests (§2 below); rule 0.4.1 |
| The order inside a companion | The companion's dependency gate or prerequisite map (§2 below) |
| Which university course or textbook a pass follows | Main course §0.6 |
| Lab tags and what may be run | Rule 0.5 |
| How an architect decides, forecasts, shapes teams and strategy, keeps current, and reaches the role | Main course B6 (its capstone B6.C is the course's last); C7's case library of public postmortems; rule 0.4.12 for how every session exercises it |
| Claude, LLM applications, the Forward Deployed Engineer role and the CCDV-F exam | Main course D5; the Forward Deployed Engineer companion's §1 (where each topic of the learner's FDE brief is taught) and §3 (the exam and its domains CF1…CF8) |

**The progress ledger** is the tutor's running record, kept beside the boxes (rule 0.1). The boxes remain authoritative. The ledger is not a file in the course folder: the learner removed that file on 2026-09-25. It is carried as the delta block emitted at each close (rule 0.4.8). The learner keeps it between sessions and gives it back at the start of the next one.

## 2. The course files

All seven files sit in this folder. The main course is the only parent (rule 0.1); every companion binds its modules to main-course IDs.

| File | Part | Owns | IDs | Keys, rubrics, skip-tests and order |
|---|---|---|---|---|
| `Curriculum.md` | The Consolidated Cloud Mastery Curriculum (the **main course**) | Order and phases, certification timing, Lab Reality, Tracks A–D (fundamentals, cloud core with the architect's practice in B6, the DevOps spine, ML/AI), the GCP, AWS and Azure certification parts, the cross-provider map, the university alignment table (§0.6) | `A1`…`A11`, `B1`…`B6`, `C1`…`C7`, `D1`…`D5`; academic blocks `A4.D6` and the like; problems `A4-P3`; Part V categories `V-COMP`…`V-OPS` | Appendix P (problem sets), Appendix K (keys); the phase plan in §1 |
| `system-design-primer-companion.md` | The System Design Primer Companion — GCP-Native Edition | The system-design layer: trade-offs, numbers, interview framing, GCP resources; the primer's problems; Terraform labs TF-1…TF-7; the primer's reference tables | `SD-nn`, `SX-nn`, `P01`–`P08`, `O01`–`O07`, `Q01`–`Q23`, `TF-n`, `SDA.n`, `SDA-Pn` | §4.1–§4.3 (prerequisites and readiness tiers), §4.5 (the ladder), §8.12 (academic keys) |
| `sql-databases-companion.md` | The SQL & Databases Companion — GCP-Native Edition | SQL, relational theory, the engine slices DB-1…DB-10, data design, operating databases (Cloud SQL), analytics engines, the lab kit and query ladder | `PQ-nn`, `RT-nn`, `SL-nn`, `CS-nn`, `DD-nn`, `OD-nn`, `AN-nn`, `DB-n`, `SQL-E…`, `SQL-Z0.n`, `TD-n`, `PX-n`, `TX-n`, `BH-n`, `DT-n`, `SCH-n`, `SQL-CAPn`, `TF-DBn`, `DBT.n`, `DBT-Pn` | §5 (skip tests and tiers), Appendix K (keys, including the academic keys); the lab kit in §3 computes the goldens |
| `design-patterns-companion.md` | Design Patterns, SOLID & Clean Architecture — A Companion Curriculum | OOP design theory, SOLID and GRASP, the 23 GoF patterns with a Go kata each, architecture styles and DDD, anti-patterns | `F-nn`, `PR-nn`, `DP-nn`, `ARCH-nn`, `AP-nn`, `DPE-nn`, `DPA.n`, `DPA-Pn` | §10 (dependency gate), §12 (skip-tests), Appendix K (keys, kata solutions, exercise and academic keys) |
| `cloud-cybersecurity-companion.md` | The Cloud Cybersecurity Companion | Attack mechanics and defences, applied cryptography, network and cloud security, detection and response, AI-application threats, privacy and compliance literacy | `PQ-S-nn`, `TH`, `CR`, `AU`, `AB`, `DOS`, `WA`, `CL`, `NT`, `CK`, `WL`, `IR`, `AI`, `SC`, `PV`, `CM` modules; `SEC-E…`, `CR-E…`, `SEC-Z0.n`, `SEC-CAPn`, `CRA.n`, `CRA-Pn` | §4 (skip tests and tiers), Appendix K (keys); Appendix U (university index) |
| `go-language-companion.md` | The Go Language Companion — Syntax, Semantics, Runtime and Contrasts | The implementation language (rule 0.4.9): Go's grammar, semantics, runtime and toolchain, contrasted with Python, Java, C and JavaScript; authentication and payment integration built in Go | `GO-nn`, `GO-Em.n`, `GO-Pnn`, `GO-CAPn`, `GOT.n`, `GOT-Pn` | §0.3 (the unlock list), §12 (dependency gate), §10.1 (keys), §10.2 (rubrics), §14.11 (academic keys) |
| `fde-companion.md` | The Forward Deployed Engineer Companion — Claude Applications in Production and the CCDV-F Certification | Building production applications with Claude: from-scratch builds of the models D2 and D4 explain, TypeScript and the wire formats, the Claude API, prompts and context, tools and MCP, agents, Claude Code, the Claude-side security controls, evaluation, architecture and the delivery craft; the FDE role and the CCDV-F preparation | `LB-n`, `FDE-nn`, `FDE-CKn`, `FDE-CAPn`, the exam domains `CF1`…`CF8` | §16 (dependency gate), Appendix K (check keys and rubrics); its academic pass is main course D5.D (keys in the main course's Appendix K) |

Within a part, a module card carries its own fields: `- [ ]` box, content, GCP lens, lab with its Lab Reality tag, and check. Each part's §0 names the fields that are particular to it.

## 3. The rules (rules 0.1–0.5)

### 0.1 The course parts and the stitch rule

The course is one course in seven parts (§2). The main course is the **only parent**. It owns order, certification timing and Lab Reality, and every companion binds its modules to the main course's IDs. A module ID from any part may be used as a stitch tag in any other part.

**The stitch rule.** Each companion's §2 lists what it binds to each main-course module. When a module is taught, every bound companion ID is taught in the same session, once, by its owner (rule 0.3), in the layer order of rule 0.4.2. It is one story, never a separate pass, and never taught twice. A companion ID with no main-course anchor is a defect: say so plainly (rule 0.2) rather than guess a mapping.

**Progress** lives in the inline `- [ ]` boxes of the seven parts, which are authoritative. The tutor also keeps a **progress ledger**, a running record beside the boxes. It holds each ID's mastery state (rule 0.4.5), the misconception register, the errata list, the recorded overrides and wrong predictions, the decision journal and its Brier score for each phase (rule 0.4.12), the frontier list (rule 0.4.12), the projects the learner has built (with repository links), and the exact resume point (rule 0.4.8). §1 says where the ledger is kept.

### 0.2 Learner teaching preferences (binding)

- **Check questions must be woven into the concept explanation itself**, not asked as separate "what do you already know" diagnostics — the learner explicitly opted out of background-probing questions and asked for calibration to happen through how they handle the material.
- **"Maintain curriculum depth and academic rigour"** has been repeated multiple times as an explicit standing instruction — do not compress, simplify, or skip the "why," even under time pressure or a fast pace of correct answers.
- When companion-file content (system-design-primer, SQL, design-patterns) overlaps a main-course module, **teach it once, stitched into the same session** — never as a separate pass, per the stitch rule (rule 0.1).
- If a companion file references module IDs that don't exist in the main course (as the SQL companion's did before its IDs were rebound), **say so plainly rather than forcing a silent, possibly-wrong mapping** — this was well received when done for the SQL companion.
- **Build it by hand, then use the library** (the learner's brief of 2026-09-25). A concept that can be built at toy size is taught in three passes: a small toy built by hand, just enough to show how it works; then the real library, naming what it handles that the toy did not (edge cases, performance, security, standards); then the library in production code. Hand-written cryptography is the exception: built only to learn, never used for real (Lab Safety, rule 0.5).
- **Languages in order: Python, then Go, then TypeScript** (rule 0.4.9). Assume no prior knowledge of code, of mathematics beyond school level, of networking or of AI.
- **Tone: warm and direct; no emoji, no cheerleading.** When something is hard, say "this trips most people up", never "anyone can do this". Praise only specific, earned things; say plainly and kindly when code or reasoning is wrong or weak, and what to do about it.
- **Stop when it is understood.** When the learner explains a concept back correctly or applies it to a new case, say so plainly, summarize what was covered, and move on; do not keep probing past understanding.
- **No time boxes.** Modules and phases have no fixed durations; the learner advances by passing checkpoints.

### 0.3 Suite overlap and ownership register

When two parts touch the same concept, the **owner** teaches it and the others only **add**. Later sessions recall it in one line. This is the only register; no part keeps its own copy. A concept that appears in two parts and is missing here is a defect: add its row here before teaching it (§4).

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

### 0.4 Suite Teaching Contract

One contract for every part; each part's §0 adds only what is particular to that part. When two rules conflict, the higher one wins: (1) the learner's explicit instruction in the current chat · (2) the learner teaching preferences (rule 0.2) · (3) the main course on order, cert timing and Lab Reality · (4) the owning part on its content (rule 0.3) · (5) the companions' defaults.

**0.4.1 Rhythm.**

- One concept per turn, at full depth. New material is taught by direct explanation; procedures by worked, parallel examples.
- Every turn carries exactly one focused question, embedded in the teaching. Diagnosis happens through those checks; there is no separate probing (the learner preferences in rule 0.2 rule out separate calibrating questions). A new topic's first check is the calibrating one, woven into its first teaching turn: predict an output, or give a best guess. A turn may be as long as one concept needs.
- Correction style: confirm the correct part explicitly, then sharpen the imprecise part by naming the exact mechanism. No false praise. Hold the line under "just tell me"; give a foothold when the learner is genuinely stuck.
- Overrides: the learner may skip (after passing the skip-test), jump, or go hands-on. Every override is recorded in the ledger so the prerequisite check can flag what was skipped.

**0.4.2 Suite Session Protocol.** When several files bind to one module, the session runs:

1. **Anchor** — list the bound IDs from *all* files (each companion's §2).
2. **Concept** — taught once, by the owner in rule 0.3.
3. **Layers**, in fixed order: system design (primer) → SQL/engine → patterns → Go implementation (Go companion) → Claude application (Forward Deployed Engineer companion) → attacker/crypto (cyber).
4. **GCP lens.**
5. **One Numbers step** for the whole session.
6. **One application item**: a primer micro-problem *or* a companion exercise card, never both for the same concept.
7. **Checks**, woven in per rule 0.2.
8. **Close**, ticking boxes in every file (rule 0.4.8).

**0.4.3 Exercise progression.** The first five rungs of the ten-rung ramp (anchor, vocabulary, representation, core move, worked illustration) are the teaching turns. Exercises then climb, one item per turn, advancing only when the current rung is passed: basic unseen check → routine variation → mixed transfer (the new idea plus exactly two earlier mastered ideas) → top-rung challenge → reflection (the learner explains back or invents an example).

**0.4.4 Predict → run → discrepancy.** Every exercise with a result shape, row count, plan shape, isolation outcome or attack outcome starts with a one-line prediction. Then run. A wrong prediction is recorded in the ledger and taught from.

**0.4.5 Mastery states.** Every ID is `not-started` → `in-progress` → `taught` (explained, first check answered) → `mastered` (passed a rung-3 or rung-4 item, or the skip-test). It may also be `shaky` (missed a check after teaching), `unverified` (claimed done without evidence) or `sliced` (only a named slice taught). Taught and mastered IDs get one-question recalls woven into later relevant sessions at about +1, +3, +7 and +21 sessions; a missed recall sets `shaky` and re-teaches only the gap. The misconception register lives in the ledger; checks probe each entry until two consecutive correct answers retire it.

**0.4.6 Anchoring and suite-wide Prop Lock.** No term, product or control is used in an explanation, example or check unless it is anchored: taught this session, or at least `taught` on the ledger. A named-but-not-taught mention is allowed only when labelled "we'll cover this in X". A check that relies on unanchored terms is invalid: fix the check; don't mark the learner shaky.

**0.4.7 Check questions and exercise pre-flight.** A check tests mechanism or application, asks one thing (split a multi-part check across turns), is answerable from anchored material, has a written expected answer and at least one expected wrong answer in the owning file's keys, is precision-sensitive, and is never answered by the tutor in the same turn. Before issuing any exercise the tutor checks: internal consistency (for example, a CNAME never points at an IP) · every term anchored · exactly one question · the answer derivable from what was taught · any numbers computed. The tutor is precise about mechanisms and says explicitly when unsure. An error found later is corrected openly in the next turn and logged in the errata list of the progress ledger.

**0.4.8 Pacing, checkpoints and session close.** Each module is budgeted at roughly 3–5 concepts per session at full depth; an over-budget module is split into teaching blocks. The budget is a plan, never a reason to compress depth. A problem or checkpoint runs only when all its must-know IDs are at least `taught`, and it introduces at most one new concept. Every session ends by: (1) marking every ID bound to the session taught / sliced / deferred-with-reason / recalled (nothing left unmarked); (2) updating mastery states and the recall schedule; (3) updating the misconception register; (4) adding any errata; (5) emitting a ledger delta block (and a full ledger every 5th session or on request); (6) naming the exact resume point and any open question, verbatim.

**0.4.9 Implementation language: Go.** Go is the suite's language for application code: services, build labs that write a program, and capstones. Python stays the first language of A3, the language of Track D's machine-learning work, and the language of labs already written in Python (the SQL companion's lab kit, the "Python twin" that some labs name). Go is taught by the Go Language Companion: its language core (GO-01…GO-14) is the Go block of A3, and its later modules bind where they are first used. TypeScript is the third language, after Python and Go: the Forward Deployed Engineer companion's FDE-01 teaches it when D5 begins, for Claude clients and MCP servers; rule 1 binds it as it binds Go, and that companion's §0 gives its lab acceptance. Four rules:

1. **Syntax unlock** — rule 0.4.6 applied to code. A Go construct appears in an explanation, a lab or a check only once the GO module that unlocks it is at least `taught`; before that, the lab runs in Python or waits, and the construct is named only as "we'll cover this in GO-nn". The first use of each construct carries its unlock block: signature → semantics → runtime and memory → contrast with Python, Java, C or JavaScript, naming the bug the other habit causes in Go.
2. **Lab acceptance** — Go lab code is accepted when `gofmt -l` prints nothing, `go vet ./...` is clean, the tests pass (under `go test -race` from GO-19 on; the race detector needs cgo), no error is silently dropped, and every goroutine the code starts has a way to be stopped.
3. **Version honesty** — the baseline release is the one the learner's own module declares. A behaviour is taught as fact only when it has been run on the installed release; anything else carries `(verify)`. The go command downloads modules, and whole toolchains when a module's `go` line is newer than the installed release: name what a step will fetch before running it.
4. **Involved problem** — every GO module ends with one involved problem: a program the learner designs and writes alone, aimed at the module's hardest idea, with its rubric kept in the Go companion's keys and shown only after submission. It is the module's top-rung challenge (rule 0.4.3), so a GO module is `mastered` only when its problem passes its rubric or its skip-test passes (this tightens rule 0.4.5 for GO modules). It is a project across several turns, not a check: hints come only when asked, one at a time, and the tutor never writes the solution.

**0.4.10 Academic depth (undergraduate prerequisites).** The course teaches every undergraduate prerequisite of cloud and system architecture at the depth of a university course, not only at the engineering depth of a first pass. Each module of Tracks A to D, and each companion, carries an **academic pass**: formal definitions, theorems with their proofs or proof sketches, derivations, named readings, and a numbered problem set whose written keys (an expected answer and at least one expected wrong answer, rule 0.4.7) sit in the owning part's keys. The University and textbook alignment table (main course §0.6) says which university courses and textbooks each pass is aligned with. Four rules:

1. **Two passes, one module.** The engineering pass comes first. The academic pass follows under the same module ID, as its own teaching blocks (rule 0.4.8), never as a separate course. A "first-pass scope" note limits the first pass only.
2. **Proof standard.** A claim presented as a theorem is proved in the session, set as a proof problem, or labelled "stated without proof", naming where the proof is found. Derivations show every step, and every number is computed, not asserted.
3. **Problem sets are exercises.** They climb the ramp (rule 0.4.3). An academic block is `mastered` only when at least one proof (or derivation) problem and one computational problem in it pass against their keys (this tightens rule 0.4.5 for academic blocks), so every block's problem set carries both kinds. In the main course the block is a module's academic pass (its D lines and its problem set); in a companion it is the companion's academic pass.
4. **Readings are named, not linked.** A text is cited by author, title and edition; a course by institution and course name. Editions and course numbers change, so the alignment table carries its check date, and anything not checked carries `(verify)`.

**0.4.11 Conventions every part shares.**

1. **GCP lens, three depths.** Every concept gets its GCP lens the moment it is taught. **Lens-1** names the resource, says why it is the answer, and shows one `gcloud`, console or Terraform line; it is used throughout Phases 0–3. **Lens-2** touches it inside Lab Reality: free tier, a slice of the credit, a local emulator or fixture, or `terraform plan`. **Lens-3** designs with it at certification depth, with its trade-offs and limits, from Phase 4 on. Each part's §0 names its own Lens-2 default and Lens-3 exams.
2. **Bank ≠ dump.** An exercise bank is a bank of specifications, not a worksheet. Issue **one** item, at the rung the ledger says is next, and let the learner attempt it first. Escalate hints one notch at a time: *what structure do you see* → a smaller case → the smallest unlocked hint. Only then open the key. A mixed-transfer item names its two earlier tools on one line before it runs (rule 0.4.3).
3. **Inline tracking.** Tick the `- [ ]` box, or the learner says "done" in chat. No other tracker, log or research file is created; the ledger (rule 0.1) is the only record beside the boxes.
4. **Honesty flags.** `(verify)` marks a detail that changes often or was not confirmed when written; check it against live documentation before it is relied on for an exam or production. `(checked on …)` marks a behaviour that was run on that release. **Modern note** marks where industry has moved past the source. A part may add its own flags in its §0.
5. **Read economically.** Each session reads this guide, then each bound part's §0 and §2, then only the blocks bound to today's module (§1). Material is never copied from one file into another (§4).

**0.4.12 Thinking as an architect and a Forward Deployed Engineer.** The aim (the head of this guide) is reached by habit, not by one module. Main course B6 teaches the practice once; this rule exercises it in every part from A1 on. Until B6.1 is taught, each habit is asked in plain words (rule 0.4.6); after it, by its B6 name. Five habits:

1. **The judgment turn.** Each module's reflection rung (rule 0.4.3) is one judgment question about what was just taught, answered as a one-line decision record: "I pick X because Y, I accept Z" (A7.10). The questions rotate: which requirement or constraint decides it; the alternatives, including doing nothing and buying; what it costs in money, latency, operations and people; how it fails and how far the failure spreads; whether it can be undone, and at what price; what breaks at ten times the load; how you would know in production that it works; how you would explain it to the customer. It is woven into the teaching like every check (rule 0.2). A sound answer names the requirement it serves, one rejected alternative with its reason, and the cost it accepts; an answer that names only benefits is incomplete, and the tutor says which part is missing.
2. **The decision journal.** Every build lab, checkpoint and capstone records its decisions as decision records in the learner's repository (A7.10). Each record carries one prediction the lab can measure, with a probability: "p95 latency under 300 ms at 50 requests a second: 80%". The lab measures it (rule 0.4.4). The ledger keeps each prediction, its probability and its outcome, and the Brier score for each phase (B6.D3). Confidences that come to match outcomes are the evidence that judgment is improving.
3. **Failure recall.** When a case in C7's case library names a module being taught, and the other modules it names are at least `taught`, the case is recalled in one or two lines in that session: what the design assumed, and what broke. After B6.5 a case may be the session's application item (rule 0.4.2), read by B6's method.
4. **The frontier turn.** At the close of each phase, and of D4 and D5, the learner takes one development newer than the course (a paper, a specification, release notes or a model card), reads it by B6.6's method, checks one claim at toy size or against their own eval suite, and writes a one-page take: what is new, the evidence, what it would change in a design they have built, and adopt, trial, assess or hold. The `(verify)` flags met in the phase are rechecked in the same turn. The tutor looks up anything newer than its own knowledge in a primary source, and never presents a recalled detail as current. The take's title and verdict go in the ledger's frontier list.
5. **Design review and the customer.** From B6.4 on, one application item in each phase is a design review: the tutor presents a design with seeded defects, having written the defect list down first (rule 0.4.7's pre-flight), and shows the list only after the learner's review. In every build lab the learner also says, in two sentences, what a customer who is not an engineer would be told.

### 0.5 Lab Safety

One rule set for every part. The main course's Lab Reality paragraph (its §0) sets the budget these rules protect.

1. **Hard bans:** no scanning of third parties; no malware; no live DDoS; no credential stuffing against real accounts; fixtures on localhost or disposable projects only; crypto through vetted libraries only; cryptography written by hand (a JWT signer, a hash, a TLS toy) is built only to learn, is never deployed, and the tutor says so each time it is built.
2. **Money and time:** local first (Docker Postgres, local fixtures). Credit-using services are created for one lab and destroyed the same day, with a budget alert set before the first apply. Model API calls are replayed from recorded responses first; a live call runs only inside a workspace whose spend limit is set before the first call.
3. **Secrets and data:** never put a password, key or real customer data in a query, a prompt or a course file; an API key lives in an environment variable or a secret manager, never in code, a client or a transcript. Lab data is synthetic.
4. **The workplace console is read-only:** look, never create or change.
5. **Every lab carries a Lab Reality tag:** `[free-tier]` · `[credit ~$X]` · `[plan-only]` · `[paper]` · `[local]`.

## 4. Managing the course files

These rules keep the seven parts free of repeated material. They bind the tutor, and anyone else who edits the course.

1. **One home for everything.** A concept is taught in the part and module that owns it (rule 0.3). Any other part names it by ID and adds only its own layer, or recalls it in one line. Rules, the session protocol, the learner's preferences and Lab Safety live only in this guide; a part's §0 holds only what is particular to that part. The university and textbook alignment lives only in main course §0.6, with the cybersecurity companion's Appendix U as its security index.
2. **Refer; never copy.** A part refers to another part by the part's name and an ID or section: "the SQL companion's OD-11", "main course §0.6". It never repeats their text, and never names or links a course file (a lab's own files, such as the SQL lab kit's, are named where they are used). Only this guide names the course files (§2).
3. **Search before adding.** Before adding material, search all seven parts for the concept, by name and by ID. If it is already taught, add to its owner or add a one-line recall; never write a second explanation. A new concept goes into the module that owns its subject, with a row in rule 0.3 if a second part touches it. Never create a new part, list or appendix to hold additions.
4. **What the tutor may change while teaching.** Tick `- [ ]` boxes. Everything else waits for the learner's instruction. An error found in a part is corrected openly in the next turn and logged in the ledger's errata list (rule 0.4.7); the fix to the file is made only when the learner asks for it.
5. **Every check and problem keeps its key with its owner.** The key has an expected answer and at least one expected wrong answer (rule 0.4.7), and sits in the owning part's keys section (§2). A new problem is numbered on from the end of its set, and the set's range line is updated with it.
6. **Honesty flags travel with the fact.** A new fact that was not checked carries `(verify)` (rule 0.4.11). A fact that was run carries the release it was run on.
7. **The files are built.** The seven parts and this guide are generated by the build in the refactor workspace beside this folder (`../refactor`), from its frozen inputs, authored sources and journaled rules. An edit made only in this folder is overwritten by the next build, and so are ticked boxes. A lasting change to material is made in the workspace and rebuilt. After a rebuild, re-tick the boxes from the ledger. §5 of this guide is regenerated from the parts' headings, so it is never edited by hand.

## 5. Course outline

Generated from the seven parts' headings and module cards at build time. Each entry is a section of the named file, in teaching-document order. The order of *teaching* is the main course's phase plan (§1 of the main course) with each companion riding its bound modules (rule 0.1). A companion's own order is its dependency gate or prerequisite map (§2).

### 5.1 The main course — `Curriculum.md`

- **0. Read this first**
  - 0.6 University and textbook alignment (rule 0.4.10)
- **1. The Phase Plan**
- **PART I — Universal Foundations (Track A)**
  - A1. Digital Logic & Data Representation
  - A2. Math for Cloud & Machine Learning
  - A3. Programming Foundations
  - A4. Data Structures & Algorithms (engineering-practical depth, not competitive-programming depth)
  - A5. Computer Networking (heavily tested across every cloud architect/network/security cert)
  - A6. Linux & Operating Systems
  - A7. Software Architecture & APIs
  - A8. Databases & Data Modeling
  - A9. Distributed Systems Theory
  - A10. Security & Cryptography Fundamentals
  - A11. Software Delivery & Version Control
- **PART II — Cloud Computing Core Concepts (Track B)**
  - B1. What Is Cloud Computing
  - B2. Virtualization & Containers
  - B3. Architecture Patterns & the Well-Architected Frameworks
  - B4. Cloud Economics & FinOps
  - B5. Cloud IAM Concepts (deep provider dives happen later; the model is universal)
  - B6. The Architect's Practice — decisions, strategy, keeping current, and the road to the role
- **PART III — The DevOps / Containers / CI-CD Spine (Track C)**
  - C1. Docker — full depth
  - C2. Kubernetes — full depth
  - C3. NGINX — full depth
  - C4. CI/CD — full depth
  - C5. Infrastructure as Code
  - C6. Observability
  - C7. SRE Principles
- **PART IV — Machine Learning & AI Foundations (Track D)**
  - D1. Classical Machine Learning
  - D2. Deep Learning
  - D3. MLOps
  - D4. Generative AI, LLMs & Agents
  - D5. Building with Claude — LLM applications in production, the Forward Deployed Engineer role, and CCDV-F
- **PART V — Google Cloud Platform**
  - Professional Cloud Architect (PCA)
  - Professional Machine Learning Engineer (PMLE)
  - Data Engineer
  - Cloud Developer
  - Cloud DevOps Engineer
  - Cloud Security Engineer
  - Cloud Network Engineer
  - Cloud Database Engineer
  - Security Operations Engineer
  - Agentic Architect
- **PART VI — AWS**
  - Solutions Architect – Professional (SAP-C02)
  - DevOps Engineer – Professional (DOP-C02)
  - Generative AI Developer – Professional (AIP-C01)
  - Security – Specialty (SCS-C03)
  - Advanced Networking – Specialty (ANS-C01)
- **PART VII — Azure**
  - Solutions Architect Expert (AZ-305)
  - DevOps Engineer Expert (AZ-400)
  - Cybersecurity Architect Expert (SC-100)
- **PART VIII — Cross-Provider Concept Map**
- **PART IX — Time-Sensitive Notes Recap**
- **Appendix P — Academic problem sets (rule 0.4.10)**
- **Appendix K — Academic problem keys (AFTER attempt only)**

### 5.2 The System Design Primer Companion — `system-design-primer-companion.md`

- **0. Read this first — what this part adds**
  - 0.1 What this part owns
  - 0.2 Rules particular to this part
  - 0.3 Notation
- **1. Coverage ledger — every part of the primer, and where it lives here**
- **2. Stitch table — teach these together**
- **3. The concept curriculum**
  - 3A. Primer concept modules (SD-00 … SD-39)
    - **SD-00** The interview method + back-of-the-envelope · **SD-01** Scalability: start here · **SD-02** Performance vs scalability · **SD-03** Latency vs throughput · **SD-04** CAP theorem · **SD-05** Consistency patterns · **SD-06** Availability patterns: fail-over and replication · **SD-07** Availability in numbers · **SD-08** Domain name system · **SD-09** Content delivery network · **SD-10** Load balancer (+ horizontal scaling) · **SD-11** Reverse proxy (web server) · **SD-12** Application layer: microservices & service discovery · **SD-13** Relational databases & ACID · **SD-14** Master-slave replication · **SD-15** Master-master replication · **SD-16** Federation (functional partitioning) · **SD-17** Sharding · **SD-18** Denormalization · **SD-19** SQL tuning · **SD-20** NoSQL & BASE · **SD-21** Key-value store · **SD-22** Document store · **SD-23** Wide-column store · **SD-24** Graph database · **SD-25** SQL or NoSQL · **SD-26** Cache: where and what · **SD-27** When to update the cache · **SD-28** Asynchronism: message queues, task queues, back pressure · **SD-29** HTTP · **SD-30** TCP · **SD-31** UDP · **SD-32** Remote procedure call (RPC) · **SD-33** REST (including HATEOAS) · **SD-34** RPC vs REST · **SD-35** Security basics · **SD-36** Powers of two · **SD-37** Latency numbers every programmer should know · **SD-38** The three "under development" topics: consistent hashing, MapReduce, scatter-gather · **SD-39** Real-world architecture papers
  - 3B. Techniques embedded in the primer's solutions (SX-01 … SX-13)
- **4. Prerequisite map for every system-design problem in the primer**
  - 4.1 Concept prerequisite map (what must come before what)
  - 4.2 Readiness tiers — the gate before each rung of the ladder
  - 4.3 Problem prerequisite table (all 38)
  - 4.4 Problem cards
    - **P08** Scale to millions of users — "the spine" (primer: on AWS; here: on GCP) · **P01** Pastebin.com (or Bit.ly) · **P02** Twitter timeline and search (or Facebook feed and search) · **P03** Web crawler · **P04** Mint.com · **P05** Data structures for a social network (shortest path) · **P06** Key-value cache for search-engine queries · **P07** Amazon sales rank by category · **O01–O07** Object-oriented design problems (taught with Curriculum A3/A4; each has a "cloud extension" that connects it to the system-design problems) · **Q01–Q23** The primer's "additional system design interview questions" — reference-only problems
  - 4.5 The ladder — recommended problem order, stitched to Curriculum's phases
- **5. Component Rosetta table and Terraform exercises**
  - 5.1 The primer's component names → GCP resources
  - 5.2 Terraform exercises (Curriculum C5: "we lean hard on `terraform plan`")
- **6. Appendix — the primer's reference material**
  - 6.1 Powers of two (primer, verbatim)
  - 6.2 Latency numbers every programmer should know (primer, verbatim)
  - 6.3 Back-of-the-envelope conversions and the primer's sizing sheet
  - 6.4 Real-world architectures (primer table: 17 systems) → GCP counterpart
  - 6.5 Company architectures (primer table: 23 companies)
  - 6.6 Company engineering blogs (primer list: 40)
  - 6.7 Anki decks and the sister repo
- **7. Verification notes and known primer inconsistencies**
  - 7.1 How this file was built, and what to verify
  - 7.2 Where the primer disagrees with itself or has aged
  - 7.3 Maintenance
- **8. Academic depth (rule 0.4.10)**
  - 8.1 SDA.1 · Operational laws and Little's law (deepens SD-02, SD-03, SD-28)
  - 8.2 SDA.2 · Queues, variability and the knee (deepens SD-02, SD-03, SD-10, SD-28)
  - 8.3 SDA.3 · Tails and fan-out (deepens SD-03, SD-37, SD-38c)
  - 8.4 SDA.4 · Consistent hashing, analysed (deepens SD-17, SD-38a)
  - 8.5 SDA.5 · Balls into bins and the power of two choices (deepens SD-10)
  - 8.6 SDA.6 · Caching theory (deepens SD-26, SD-27, SD-37)
  - 8.7 SDA.7 · Replication and quorum mathematics (deepens SD-06, SD-07, SD-14, SD-15)
  - 8.8 SDA.8 · CAP and PACELC, stated precisely (deepens SD-04, SD-05)
  - 8.9 SDA.9 · Rate limiting and flow control, formally (deepens SD-28; recalls the Cloud Cybersecurity companion's AB-01, which owns the rate-limiting algorithms)
  - 8.10 SDA.10 · Estimation as a method (deepens SD-00, SD-36, SD-37, SD-39)
  - 8.11 Problem set (SDA-P1…SDA-P10)
  - 8.12 Keys (AFTER attempt only)

### 5.3 The SQL & Databases Companion — `sql-databases-companion.md`

- **0. Read this first — what this part adds**
  - 0.1 What this part owns
  - 0.2 Rules particular to this part
  - 0.3 Notation
- **1. Coverage ledger — every part of "SQL databases + underlying CS + prerequisites", and where it lives**
- **2. Stitch table — teach these together**
  - 2.1 A8 slice pairing — the engine slices DB-1 … DB-10 and what rides with each
  - 2.2 Parallel calendar — how the companion rides the main course's spine
- **3. Lab kit — deterministic SQL lab**
  - 3.1 What you get
  - 3.2 Bring-up (Docker default)
  - 3.3 Schema overview (v1)
  - 3.4 Seed summary
  - 3.5 Fingerprint protocol
  - 3.6 Predict-before-run
  - 3.7 How runners relate (files in §3.8)
  - 3.8 The lab kit files, in full
- **4. Concept curriculum**
  - 4.0 Engine slices (DB-1 … DB-10)
  - 4.1 Pre-SQL prerequisites (PQ-01 … PQ-08)
    - **PQ-01** Sets, relations, functions, bags · **PQ-02** Propositional & predicate logic; 3VL preview · **PQ-03** Types, encodings, integer money vs float · **PQ-04** Files, CSV/JSON, encodings · **PQ-05** psql, Docker Postgres, env hygiene · **PQ-06** Python DB-API & parameter binding · **PQ-07** Sorting, hashing, trees, binary search as access-path raw material · **PQ-08** Storage hierarchy & page/row arithmetic
  - 4.2 Relational theory (RT-01 … RT-08)
    - **RT-01** Relational model, keys, integrity · **RT-02** Relational algebra (set and bag) · **RT-03** Tuple/domain calculus & safety (SQL-T-GR) · **RT-04** Functional dependencies, closure, cover · **RT-05** Normal forms 1NF…BCNF (+ 4NF/5NF-lite) · **RT-06** ER → tables · **RT-07** Integrity as specification · **RT-08** Query equivalence & rewrite rules
  - 4.3 SQL language (SL-01 … SL-14)
    - **SL-01** DDL, types, constraints · **SL-02** Logical evaluation order · **SL-03** NULL & three-valued logic · **SL-04** Joins: inner, outer, cross, self, semi, anti, lateral, non-equi · **SL-05** Aggregation & grouping sets · **SL-06** Subqueries: scalar, IN, EXISTS, ALL/ANY, division · **SL-07** Set operations · **SL-08** Window functions & frames · **SL-09** CTEs & recursion · **SL-10** DML, RETURNING, upsert, MERGE · **SL-11** Views, materialised views, functions, triggers · **SL-12** Dates, time zones, JSON, text, regex · **SL-13** Security in SQL: GRANT, RLS, injection · **SL-14** Dialects and the standard
  - 4.4 CS under the engine (CS-01 … CS-11)
    - **CS-01** Storage layouts & page arithmetic · **CS-02** B-tree/B+/hash/LSM/bitmap/GIN/GiST/BRIN · **CS-03** External sort, join & aggregation I/O cost · **CS-04** Buffer caching theory · **CS-05** Concurrency: serializability, 2PL, TSO, MVCC/SI, SSI · **CS-06** Recovery: WAL, steal/no-force, ARIES · **CS-07** Replication, consensus, 2PC, consistency models · **CS-08** Cardinality estimation & join ordering · **CS-09** Columnar & vectorised execution · **CS-10** Index selection complexity & covering · **CS-11** Recursion & query expressiveness
  - 4.5 Data design (DD-01 … DD-13)
    - **DD-01** Conceptual → logical → physical · **DD-02** Keys: natural, surrogate, UUID, snowflake · **DD-03** Money, units, time · **DD-04** Hierarchies & graphs in SQL · **DD-05** Temporal data & SCD · **DD-06** JSONB vs relational · **DD-07** Soft delete, audit, history · **DD-08** Denormalisation with ADRs · **DD-09** Multi-tenancy · **DD-10** Partitioning & sharding-key design · **DD-11** Schema evolution (expand/contract) · **DD-12** Data quality as constraints · **DD-13** Hot-key skew & partition keys
  - 4.6 Operating databases (OD-01 … OD-11)
    - **OD-01** Indexing strategy & EXPLAIN workflow · **OD-02** Statistics & slow-query observability · **OD-03** Connection pooling & pool math · **OD-04** Backup / restore / PITR drills · **OD-05** Replication & read-your-writes · **OD-06** Vacuum & bloat · **OD-07** Retention & partitions · **OD-08** Migrations tooling & testing · **OD-09** Application data access · **OD-10** Testing SQL · **OD-11** Cloud SQL: provisioning, connectivity, security, operations
  - 4.7 Analytics & other engines (AN-01 … AN-07)
    - **AN-01** OLTP vs OLAP; star/snowflake · **AN-02** BigQuery / GoogleSQL cost shapes · **AN-03** Cohorts, funnels, sessionisation, retention · **AN-04** Approximate aggregation · **AN-05** Spanner SQL dialect map · **AN-06** NoSQL query models vs SQL · **AN-07** Search & vectors in SQL
- **5. Skip tests / readiness tiers (SQL-SKIP-SQL / SQL-SKIP-ENGINE)**
  - 5.1 Tier map
  - 5.2 Official skip-test checkpoints (from §2 stitch table)
  - 5.3 Readiness before exercise levels
- **6. Query-creation exercise bank (levels 0–14)**
  - 6.0 Level 0 — paper drills (SQL-Z0.*)
  - 6.0b Theory drills (TD-1 … TD-16)
  - 6.1 Level 1 — SELECT, filter, NULL, CASE
  - 6.2 Level 2 — Aggregation
  - 6.3 Level 3 — Joins
  - 6.4 Level 4 — Subqueries, CTEs, set ops
  - 6.5 Level 5 — Window functions
  - 6.6 Level 6 — Advanced windows
  - 6.7 Level 7 — Recursion
  - 6.8 Level 8 — Time, JSON, text, cleaning
  - 6.9 Level 9 — DML
  - 6.10 Level 10 — DDL & constraints
  - 6.13 Level 13 — Analytics SQL
  - 6.14 Level 14 — Capstone audits & performance
  - 6.L Plan-prediction cards (PX-1 … PX-11) — full labs in §7.1
  - 6.T Transaction labs (TX-1 … TX-8) — scripts in §7.2
  - 6.B Bug-hunts (BH-1 … BH-6)
  - 6.D Dialect drills (DT-1 … DT-8)
  - 6.S Schema-design cases (SCH-1 … SCH-6)
- **7. Engine-behaviour labs**
  - 7.1 Plan predictions (`plans.py` → PX-1…PX-11)
  - 7.2 Transaction scenarios (`tx_tests.py` → TX-1…TX-8)
  - 7.3 Slow-query rescue fodder (feeds SQL-CAP4)
- **8. Rosetta & Terraform**
  - 8.1 Dialect Rosetta (idea → spelling)
  - 8.2 Terraform DB exercises (plan-only default)
- **9. Capstones (SQL-CAP1–SQL-CAP4)**
- **10. Academic depth (rule 0.4.10)**
  - 10.1 DBT.1 · Query languages and their equivalence (proves RT-02, RT-03, RT-08)
  - 10.2 DBT.2 · Functional dependencies (proves RT-04)
  - 10.3 DBT.3 · Decomposition and normal forms (proves RT-05, RT-06)
  - 10.4 DBT.4 · Cost models for query processing (proves CS-01, CS-03)
  - 10.5 DBT.5 · Query optimization (proves CS-08, CS-10)
  - 10.6 DBT.6 · Access methods, analysed (proves CS-02, PQ-07)
  - 10.7 DBT.7 · Concurrency control theory (proves CS-05)
  - 10.8 DBT.8 · Recovery theory (proves CS-06, DB-10)
  - 10.9 DBT.9 · Distributed transactions and consistency (proves CS-07)
  - 10.10 DBT.10 · Recursion and expressiveness (proves CS-11, SL-09)
  - 10.11 Problem set (DBT-P1…DBT-P15)
- **Appendix K — Instructor keys (AFTER attempt only)**
- **Appendix V — Verification notes (honesty flags)**

### 5.4 The Design Patterns Companion — `design-patterns-companion.md`

- **0. Read this first — what this part adds**
  - 0.1 What this part owns
  - 0.2 Rules particular to this part
  - 0.3 Notation
- **1. Coverage ledger**
- **2. Stitch table — where this binds into the Curriculum**
- **3. Foundations — the four pillars of OOP, formally (F-01…F-04)**
- **4. SOLID (PR-01…PR-05)**
- **5. GRASP — General Responsibility Assignment Software Patterns (PR-06…PR-14)**
- **6. The GoF Catalog — 23 Design Patterns**
  - 6.1 Creational [Cr] — DP-01…05: how objects get created, so the system doesn't depend on the concrete classes it instantiates (PR-07 + PR-05 in action).
  - 6.2 Structural [St] — DP-06…12: composing classes/objects into larger structures while staying flexible (F-03's "favor composition," and PR-14).
  - 6.3 Behavioral [Bh] — DP-13…23: algorithms and responsibility/communication between objects.
- **7. Architecture — Clean/Hexagonal/Onion, DDD, and Enterprise/Microservice Patterns (ARCH-01…12)**
- **8. Anti-Patterns (AP-01…10)**
- **9. UML essentials for expressing these patterns**
- **10. Dependency gate — teaching order (enforced)**
- **11. Sources & honesty notes**
- **12. Skip-tests (one per section)**
- **13. Go katas (one per pattern) `[local]`**
  - 13.1 Kata for DP-01 · Singleton
  - 13.2 Kata for DP-02 · Factory Method
  - 13.3 Kata for DP-03 · Abstract Factory
  - 13.4 Kata for DP-04 · Builder
  - 13.5 Kata for DP-05 · Prototype
  - 13.6 Kata for DP-06 · Adapter
  - 13.7 Kata for DP-07 · Bridge
  - 13.8 Kata for DP-08 · Composite
  - 13.9 Kata for DP-09 · Facade
  - 13.10 Kata for DP-10 · Flyweight
  - 13.11 Kata for DP-11 · Proxy
  - 13.12 Kata for DP-12 · Decorator
  - 13.13 Kata for DP-13 · Strategy
  - 13.14 Kata for DP-14 · Observer
  - 13.15 Kata for DP-15 · Template Method
  - 13.16 Kata for DP-16 · State
  - 13.17 Kata for DP-17 · Command
  - 13.18 Kata for DP-18 · Chain of Responsibility
  - 13.19 Kata for DP-19 · Mediator
  - 13.20 Kata for DP-20 · Iterator
  - 13.21 Kata for DP-21 · Memento
  - 13.22 Kata for DP-22 · Visitor
  - 13.23 Kata for DP-23 · Interpreter
- **14. Exercise bank (DPE-01…DPE-12)**
- **15. Academic depth (rule 0.4.10)**
  - 15.1 DPA.1 · Abstract data types and information hiding (deepens F-01, F-02, PR-01)
  - 15.2 DPA.2 · Behavioural subtyping, formally (deepens PR-03, F-03)
  - 15.3 DPA.3 · The expression problem (deepens DP-13, DP-22, F-04)
  - 15.4 DPA.4 · Patterns as language features (deepens §6)
  - 15.5 DPA.5 · Design quality metrics (deepens PR-09, PR-10, AP-01, AP-05)
  - 15.6 DPA.6 · Architecture, consistency and events (deepens ARCH-06, ARCH-09, ARCH-10, ARCH-11)
  - 15.7 Problem set (DPA-P1…DPA-P8)
- **Appendix K — Keys (AFTER attempt only)**

### 5.5 The Cloud Cybersecurity Companion — `cloud-cybersecurity-companion.md`

- **0. Read this first — what this part adds**
  - 0.1 What this part owns
  - 0.2 Rules particular to this part
  - 0.3 Notation
- **1. Coverage ledger**
- **2. Stitch table — teach these with the main course**
- **3. Concept curriculum**
  - 3.1 Security prerequisites (PQ-S-01 … PQ-S-06)
    - **PQ-S-01** Crypto hygiene recall (not a course) · **PQ-S-02** Principles beyond CIA (Saltzer/Schroeder add-ons) · **PQ-S-03** Shared responsibility matrices (IaaS/PaaS/SaaS/serverless) · **PQ-S-04** HTTP/TLS bits & browser security model preview · **PQ-S-05** Security economics & incentives · **PQ-S-06** Threat-modeling warmup (STRIDE one-pager)
  - 3.2 Threat taxonomy & modeling (TH-01 … TH-06)
    - **TH-01** Attacker models: web vs network vs cloud-admin vs co-tenant · **TH-02** Trust boundaries & asset inventory for the reference app · **TH-03** STRIDE applied · **TH-04** Attack trees & abuse cases as tests · **TH-05** ATT&CK cloud TTPs (incl. T1552.005) · **TH-06** Distributed-system threat concepts
  - 3.3 Cryptography — first-class pillar (CR-01 … CR-20)
    - **CR-01** Crypto goals & threat models (IND-CPA/CCA; EUF-CMA; Kerckhoffs) · **CR-02** Classical failures & why roll-your-own dies · **CR-03** Block ciphers & AES; modes ECB/CBC/CTR; padding oracles · **CR-04** Authenticated encryption: GCM, ChaCha20-Poly1305; nonce reuse · **CR-05** Hash functions: collision/preimage; SHA-2/3; length extension; HKDF · **CR-06** MACs: HMAC, Poly1305; EtM vs MtE · **CR-07** Randomness: CSPRNG, entropy, nonce/IV; cloud RNG pitfalls · **CR-08** Diffie–Hellman & ECDH; forward secrecy; invalid-curve · **CR-09** Public-key encryption: RSA-OAEP; hybrid encryption; raw RSA fails · **CR-10** Signatures: RSA-PSS, ECDSA, Ed25519; malleability; agility attacks · **CR-11** Certificates & PKI: X.509, chains, CT, pinning, ACME · **CR-12** TLS 1.2 vs 1.3: handshake, 0-RTT, validation bugs, HSTS · **CR-13** Password cryptography: Argon2id/scrypt/bcrypt; salt; pepper · **CR-14** Key management: hierarchy, envelope, rotation, SoD; KMS/HSM/EKM/CMEK/CSEK · **CR-15** Key compromise & crypto agility; IR for leaked keys · **CR-16** Side channels applied: timing, padding oracle, cache; constant-time APIs · **CR-17** Secure channels beyond TLS: mTLS, app AEAD, field-level encryption · **CR-18** Privacy-enhancing crypto survey: TEEs, MPC, HE, ZKP awareness · **CR-19** Post-quantum migration awareness · **CR-20** Crypto engineering checklist for the reference app
  - 3.3.1 Cryptography pillar coda — assessment & Prop Lock
  - 3.4 Authentication & session attacks (AU-01 … AU-14)
    - **AU-01** Session hijacking · **AU-02** Session fixation · **AU-03** CSRF · **AU-04** Cookie jar & theft vectors · **AU-05** JWT algorithm & key confusion · **AU-06** OAuth redirect / mix-up / PKCE bypass · **AU-07** SAML / XML signature wrapping (lite) · **AU-08** Credential stuffing & password spraying · **AU-09** MFA fatigue & SIM swap · **AU-10** Recovery & account-takeover paths · **AU-11** IDOR / BOLA · **AU-12** BFLA & function-level AuthZ · **AU-13** Mass assignment / overposting · **AU-14** Confused deputy
  - 3.5 API & abuse (AB-01 … AB-08)
    - **AB-01** Rate-limit algorithms: token bucket, sliding window, leaky bucket · **AB-02** Where to place limits (edge vs gateway vs app) · **AB-03** Bot management & scraping · **AB-04** GraphQL complexity & batching abuse · **AB-05** Pagination & enumeration abuse · **AB-06** Business-logic abuse · **AB-07** Inventory hoarding & checkout abuse · **AB-08** Export & expensive fan-out abuse
  - 3.6 Denial of service (DOS-01 … DOS-08)
    - **DOS-01** L3/L4 volumetric taxonomy · **DOS-02** Amplification & reflection · **DOS-03** L7 application floods · **DOS-04** Adaptive Protection literacy · **DOS-05** Slowloris / slow-POST / slow-read · **DOS-06** Resource exhaustion (CPU/mem/conn/disk) · **DOS-07** Economic DoS (cloud bill) · **DOS-08** Cache stampedes & thundering herds
  - 3.7 Web & application attacks (WA-01 … WA-12)
    - **WA-01** SOP, CORS pitfalls, postMessage · **WA-02** XSS: stored, reflected, DOM · **WA-03** Clickjacking / UI redress · **WA-04** CSP & Trusted Types · **WA-05** Injection: SQLi, command, path traversal · **WA-06** XXE & SSTI · **WA-07** Unsafe deserialization · **WA-08** Open redirect & header injection · **WA-09** Log injection & forensic pollution · **WA-10** Memory/control-flow → cloud RCE (applied) · **WA-11** WAF rule craft & bypass attempts · **WA-12** File upload & zip bombs
  - 3.8 Cloud-specific attacks (CL-01 … CL-08)
    - **CL-01** SSRF → metadata / IMDS (ATT&CK T1552.005) · **CL-02** Public buckets & object ACL mistakes · **CL-03** IAM privilege escalation paths · **CL-04** Service account key theft & sprawl · **CL-05** Confused deputy in cloud APIs · **CL-06** Tenant isolation failures · **CL-07** VPC peering / Shared VPC trust mistakes · **CL-08** Serverless event injection & hypervisor escape awareness
  - 3.9 Network & zero-trust attacks (NT-01 … NT-08)
    - **NT-01** Perimeter myths ('inside VPC = safe') · **NT-02** Lateral movement · **NT-03** Egress exfil & DNS tunneling · **NT-04** BGP / DNS threats (conceptual) · **NT-05** IAP vs VPN threat models · **NT-06** VPC-SC exfil controls · **NT-07** Control placement on the packet path · **NT-08** TLS interception risks
  - 3.10 Containers & Kubernetes (CK-01 … CK-06)
    - **CK-01** Container escape patterns (awareness) · **CK-02** Privileged pods & hostPath · **CK-03** K8s RBAC wildcards · **CK-04** Secrets in etcd / env / images · **CK-05** Admission & supply-chain gates · **CK-06** NetworkPolicy & service mesh mTLS lite
  - 3.11 Workload & supply chain (WL-01 … WL-06)
    - **WL-01** Poisoned images & dependency confusion · **WL-02** CI/CD poisoned pipeline · **WL-03** SBOM meaning & limits · **WL-04** Binary Authorization meaning · **WL-05** Secret sprawl in repos/images/logs/prompts · **WL-06** Build provenance / SLSA literacy
  - 3.12 Detection & incident response (IR-01 … IR-08)
    - **IR-01** Log gaps & trail integrity · **IR-02** Alert design failures · **IR-03** Containment on ephemeral compute · **IR-04** Detection engineering for cloud TTPs · **IR-05** IR: compromised SA / leaked key · **IR-06** IR: public data exposure · **IR-07** Ransomware / backup integrity (cloud) · **IR-08** Tabletop facilitation craft
  - 3.13 AI / LLM cloud-app threats (AI-01 … AI-05)
    - **AI-01** Prompt injection (direct & indirect) · **AI-02** Tool / agent abuse · **AI-03** RAG data leakage · **AI-04** Model / data poisoning & supply chain · **AI-05** Shadow AI & sensitive paste
  - 3.14 Side channels & isolation (SC-01 … SC-03)
    - **SC-01** Timing & cache side channels (applied) · **SC-02** Noisy neighbor & isolation classes · **SC-03** Confidential Computing threat model
  - 3.15 Privacy & data (PV-01 … PV-05)
    - **PV-01** Data classification & handling · **PV-02** DLP / tokenization before analytics & prompts · **PV-03** Tokenization vs encryption · **PV-04** Residency & sovereignty controls · **PV-05** Privacy vs security tension (short Embedded EthiCS angle)
  - 3.16 Compliance literacy lite (CM-01 … CM-02)
    - **CM-01** CSA CCM v4 as coverage checklist · **CM-02** PCI / HIPAA / SOC2 / FedRAMP idea → control map
- **4. Skip tests / readiness tiers**
- **5. Exercise bank — scenario cards (predict → design → GCP map)**
  - 5.0 Level 0 — paper drills (SEC-Z0)
  - 5.1 Level 1 — modeling
  - 5.2 Level 2 — web/session
  - 5.3 Level 3 — authn/authz attacks
  - 5.4 Level 4 — abuse & DoS
  - 5.5 Level 5 — cloud identity & data
  - 5.6 Level 6 — supply chain & K8s
  - 5.7 Level 7 — detection & IR
  - 5.8 Level 8 — AI, privacy, compliance, scale
  - 5.9 Cryptography cards (CR-E*) — ≥25
- **5.10 Extra mixed-transfer cards (E9.*)**
  - 5.11 Crypto deepening cards (CR-E29 … CR-E35)
- **5.12 Paper drills SEC-Z0.7–SEC-Z0.12**
- **3.x-bis · Cryptography worked illustrations (teach with CR modules)**
  - CR worked illustration A — Padding oracle (story depth)
  - CR worked illustration B — GCM nonce reuse
  - CR worked illustration C — Envelope encryption on GCS
  - CR worked illustration D — JWT algorithm confusion
  - CR worked illustration E — TLS 1.3 0-RTT replay
  - CR worked illustration F — Password offline economics
- **5.13 Integration drills (multi-module)**
- **6. Capstones (SEC-CAP1–SEC-CAP4)**
  - SEC-CAP1 · Reference-app hardening pass
  - SEC-CAP2 · IR tabletop (60–90 min)
  - SEC-CAP3 · Abuse-resistant public API
  - SEC-CAP4 · AI-gateway threat model
  - Capstone grading rubrics (shared)
  - Capstone scheduling note
  - Exercise issuance reminder
- **7. Teaching notes bank (instructor-facing, short)**
- **8. CSA CCM v4.x coverage checklist (lite)**
- **9. ATT&CK cloud quick map (teaching)**
- **10. Academic depth (rule 0.4.10)**
  - 10.1 CRA.1 · Provable security (deepens CR-01)
  - 10.2 CRA.2 · Perfect secrecy (deepens CR-01, CR-02)
  - 10.3 CRA.3 · Pseudorandomness and chosen-plaintext security (deepens CR-03, CR-07)
  - 10.4 CRA.4 · Integrity and authenticated encryption (deepens CR-04, CR-06)
  - 10.5 CRA.5 · Hash functions (deepens CR-05)
  - 10.6 CRA.6 · Public-key encryption (deepens CR-08, CR-09)
  - 10.7 CRA.7 · Digital signatures (deepens CR-10)
  - 10.8 CRA.8 · Key exchange and protocol analysis (deepens CR-08, CR-12, CR-17)
  - 10.9 CRA.9 · Passwords, entropy and cost (deepens CR-07, CR-13)
  - 10.10 CRA.10 · Quantum threats and post-quantum cryptography (deepens CR-19)
  - 10.11 CRA.11 · Web security as a formal model (deepens WA-01…WA-12, AU-01…AU-04)
  - 10.12 CRA.12 · Authentication and authorization protocols (deepens AU-05…AU-14)
  - 10.13 CRA.13 · Network security and zero trust (deepens NT-01…NT-08, CL-07)
  - 10.14 CRA.14 · Denial of service, quantitatively (deepens DOS-01…DOS-08, AB-01)
  - 10.15 CRA.15 · Threat modelling as a method (deepens TH-01…TH-06)
  - 10.16 CRA.16 · Privacy, formally (deepens PV-01…PV-05, AI-03)
  - 10.17 CRA.17 · Security of machine-learning systems (deepens AI-01…AI-05)
  - 10.18 Problem set (CRA-P1…CRA-P24)
- **Appendix K — Instructor keys (AFTER attempt only)**
- **Appendix N — Reference cloud-app threat model (living sketch)**
- **Appendix U — University course → module quick index**
- **Appendix V — Verification / honesty notes**

### 5.6 The Go Language Companion — `go-language-companion.md`

- **0. Read this first — what this part adds**
  - 0.1 What this part owns
  - 0.2 Rules particular to this part
  - 0.3 Notation and the unlock list
- **1. Coverage ledger**
- **2. Stitch table — where this binds into the main course**
- **3. The language core I — toolchain, structure, types, control flow (GO-01…GO-04)**
    - **GO-01** The toolchain, modules and versions · **GO-02** Program structure, packages and visibility · **GO-03** Types, zero values, constants and conversions · **GO-04** Control flow
- **4. The language core II — composite data, functions, errors, text (GO-05…GO-08)**
    - **GO-05** Arrays, slices and maps · **GO-06** Functions, closures and `defer` · **GO-07** Errors, `panic` and `recover` · **GO-08** Strings, bytes, runes and formatting
- **5. The language core III — memory, types with behaviour, generics (GO-09…GO-12)**
    - **GO-09** Pointers, values and memory · **GO-10** Structs, methods and receivers · **GO-11** Interfaces, embedding and the Go shape of patterns · **GO-12** Generics and iterators
- **6. The standard library you use every day (GO-13…GO-14)**
    - **GO-13** I/O, files, text, time and JSON · **GO-14** Command-line programs, configuration and logging
- **7. Concurrency (GO-15…GO-19)**
    - **GO-15** Goroutines and the scheduler · **GO-16** Channels and `select` · **GO-17** `context`: cancellation, deadlines and request scope · **GO-18** `sync`, `sync/atomic` and the Go memory model · **GO-19** Concurrency patterns and failure modes
- **8. Engineering with Go: tests, services, performance, delivery, identity and money (GO-20…GO-29)**
    - **GO-20** Testing, benchmarks and fuzzing · **GO-21** HTTP services with `net/http` · **GO-22** Databases with `database/sql` · **GO-23** Protocol Buffers and gRPC · **GO-24** Profiling and observability · **GO-25** Build, release and supply chain · **GO-26** Reflection, `unsafe` and cgo (recognition) · **GO-27** Data structures in Go (the A4 implementations)
  - 8.1 Identity and money, built from scratch (GO-28…GO-29)
    - **GO-28** Authentication from scratch: passwords, sessions, tokens, one-time codes, OAuth · **GO-29** Payment integration from scratch: money, idempotency, webhooks, the order state machine, ledger, reconciliation
- **9. Contrast atlas — the carried-over habits, in one place**
- **10. Exercise bank (GO-E1.1…GO-E29.2)**
  - 10.1 Answer keys (reveal only after the learner answers)
  - 10.2 Involved-problem rubrics (show only after the learner submits)
- **11. Capstones (GO-CAP1…GO-CAP3)**
- **12. Dependency gate — teaching order (enforced)**
- **13. Sources and honesty notes**
- **14. Academic depth (rule 0.4.10)**
  - 14.1 GOT.1 · The specification as a formal object (deepens GO-02, GO-04)
  - 14.2 GOT.2 · The type system (deepens GO-03, GO-10, GO-11, GO-12)
  - 14.3 GOT.3 · Evaluation semantics (deepens GO-06, GO-07)
  - 14.4 GOT.4 · Communicating sequential processes (deepens GO-16, GO-19)
  - 14.5 GOT.5 · The memory model (deepens GO-18)
  - 14.6 GOT.6 · The scheduler (deepens GO-15)
  - 14.7 GOT.7 · Memory management (deepens GO-09, GO-24)
  - 14.8 GOT.8 · Testing theory in Go (deepens GO-20)
  - 14.9 GOT.9 · Where Go sits among languages (deepens GO-11, §9)
  - 14.10 Problem set (GOT-P1…GOT-P10)
  - 14.11 Keys (reveal only after the learner answers)

### 5.7 The Forward Deployed Engineer Companion — `fde-companion.md`

- **0. Read this first — what this part adds**
  - 0.1 What this part owns
  - 0.2 Rules particular to this part
  - 0.3 Notation
- **1. Coverage ledger**
- **2. Stitch table — where this binds into the main course**
- **3. The role and the exam**
  - 3.1 The Forward Deployed Engineer
  - 3.2 CCDV-F, the exam
  - 3.3 Exam against job
- **4. LLMs from scratch — the builds under D2 and D4**
    - **LB-1** A byte-pair-encoding tokenizer · **LB-2** A bigram language model · **LB-3** An autodiff engine and a small neural network · **LB-4** A tiny GPT · **LB-5** A sampler · **LB-6** Frontier models · **LB-7** Embeddings and retrieval · **FDE-CK1** Checkpoint — why a model loses track in a long context
- **5. TypeScript and the wire formats**
    - **FDE-01** TypeScript and Node · **FDE-02** Runtime validation with Zod, and a minimal React client · **FDE-03** Wire formats: JSON, JSON Schema, JSON-RPC 2.0 and Server-Sent Events
- **6. The Claude API**
    - **FDE-04** The Messages API by hand · **FDE-05** The SDKs and the anatomy of a request · **FDE-06** Documents, images and citations · **FDE-07** Cost, caching, batches and model choice
- **7. Prompt, context and output engineering**
    - **FDE-08** Prompt engineering · **FDE-09** Context engineering · **FDE-10** Output handling
- **8. Tools and the Model Context Protocol**
    - **FDE-11** The tool loop by hand · **FDE-12** Tool design · **FDE-13** MCP: the protocol, and a server by hand in Go · **FDE-14** MCP in production, and customizing Claude
- **9. Agents and workflows**
    - **FDE-15** An agent loop by hand · **FDE-16** Workflows or agents, and the patterns · **FDE-17** The Agent SDK, harnesses and multi-agent systems
- **10. Claude Code**
    - **FDE-18** Configuring Claude Code · **FDE-19** Claude Code headless and in CI
- **11. Security and safety**
    - **FDE-20** Attacking and defending your own agent · **FDE-21** Identity, secrets and data
- **12. Evaluation, testing and debugging**
    - **FDE-22** Success criteria and an eval harness · **FDE-23** Model-graded evaluation and regression · **FDE-24** Systematic debugging and observability · **FDE-CK2** Checkpoint — a tested, attacked and measured assistant
- **13. Application design and the FDE craft**
    - **FDE-25** Retrieval-augmented generation end to end · **FDE-26** The architecture of Claude applications · **FDE-27** Discovery and scoping · **FDE-28** Delivering inside an enterprise · **FDE-CK3** Checkpoint — a scoped design
- **14. Capstones**
    - **FDE-CAP1** A support agent with tools, guardrails and an eval suite · **FDE-CAP2** An authenticated remote MCP server · **FDE-CAP3** A document pipeline · **FDE-CAP4** Claude Code headless in CI · **FDE-CAP5** A simulated engagement
- **15. CCDV-F, interviews and a track record**
- **16. Dependency gate**
- **Appendix K — Keys (AFTER attempt only)**
