# The Consolidated Cloud Mastery Curriculum
Fundamentals → GCP + AWS + Azure Professional/Expert Certifications → DevOps/Docker/K8s/NGINX/CI-CD
Built September 16, 2026. This is our shared syllabus — I'll teach from it session by session.
 
## 0. Read this first
Scope, honestly. Eighteen professional-tier certifications, three providers, plus the full engineering stack underneath them, is not a weekend, a month, or even a semester. Treated seriously — with real understanding, not memorized dumps — this is 18–30 months of consistent study for someone starting from true fundamentals. I'm telling you this not to discourage you but so we plan like adults: we go in phases, we build real skill that transfers across providers (so cert #2 through #18 get progressively faster), and we don't burn your $300 GCP credit or your motivation in week one.
 
Two time-sensitive corrections to your list, found while researching today:
 
Agentic Architect (Beta) — registration is open now and the beta window closes September 30, 2026 — about two weeks from today. Realistically, you cannot go from zero to exam-ready in two weeks while also learning fundamentals. My recommendation: let the beta window pass. The certification will reach General Availability afterward and you'll sit it properly, later, once you have the ADK/agent-building foundation (Track D4) and general GCP experience. Chasing the beta discount now would mean skipping comprehension for speed — exactly what you told me not to do.
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** the beta is still open until Sept 30, 2026. The GA date is not announced; recheck after the window closes. (verify live before scheduling)
AWS Security Specialty — your list says SCS-C02. That exam was decommissioned December 1, 2025; it's been replaced by SCS-C03 (restructured domains, new question types, added GenAI-security content). I've planned around SCS-C03.
One item on your list is confirmed accurate as stated: AWS Advanced Networking Specialty (ANS-C01) — official AWS page confirms last exam day is December 31, 2026. That's tight (3.5 months) and it's a five-year-experience-recommended exam with no announced successor. We'll revisit whether to chase it or let it lapse once you see how the rest of the pace goes — I'd rather you have real distributed-networking skill than a rushed cert for an exam being retired anyway.
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** ANS-C01's last exam day is still Dec 31, 2026, with no successor. (verify live before scheduling)
 
Your hands-on reality (given $300 GCP credit, permanent free tier, a workplace GCP account you can look in but not touch, and AWS/Azure free tier only) is threaded through every module below as an explicit "Lab Reality" note. Short version: we'll do real hands-on work for anything that fits free tier or a small slice of the $300; for expensive/enterprise-only services (Spanner multi-region, BigQuery at scale, multi-region GKE, Anthos, etc.) we'll write real Terraform/gcloud/kubectl that we validate with plan/dry-run but don't apply, and use your workplace console read-only, as a museum, never to create or change anything there. That combination genuinely builds real, defensible skill — architects are hired for judgment about services they've read deeply and reasoned about, not just ones they've clicked.
 
### 0.1 The course files and the companion stitch rule

*Refactor-authored (2026-09-24, C-01, C-NEW-04).* This roadmap is the **only parent**. Every companion names it `Curriculum` and binds its modules to the IDs below. The files:

- `Curriculum` (this file) — order, cert timing, Lab Reality and track structure.
- `system-design-primer-companion.md` — the system-design layer (SD, SX, P, O, Q, TF). Its bindings are generated from `primer-binding-table.md`.
- `sql-databases-companion.md` — SQL, relational theory and engine internals. It owns the engine slices DB-1…DB-10 (C-05).
- `design-patterns-companion.md` — OOP design theory, patterns and architecture styles (A7, A9).
- `cloud-cybersecurity-companion.md` — security, attacks and cryptography.
- `northstar-reference-app.md` — Track N, the one running reference application (sections `Nx.y`). R2 creates its skeleton; R9 authors it.
- `session-progress-ledger.md` — the learner's state; it mirrors the inline boxes, which are authoritative.

Each companion's §2 lists what it binds to each module. When a module is taught, every bound companion ID is taught in the same session, once, by its owner (§0.3), in the order §0.4 gives. The cybersecurity companion's original stitch block, first added to this file on 2026-09-22 between A10 and A11, now sits here unchanged:

---

#### Companion — Cloud Cybersecurity (standalone)

**Standing stitch rule.** Teach security-relevant sections of this roadmap with [`cloud-cybersecurity-companion.md`](./cloud-cybersecurity-companion.md). Whenever **A5**, **A7 (auth patterns)**, **A10**, **B1 (shared responsibility)**, **B5**, **C1/C2 hardening**, **Phase 4 Networking/Security**, or the **Cloud Security / Network / SecOps** cert tracks are taught, also teach every companion module bound in companion **§2** in the **same session** — one story, never twice.

That companion is **standalone** (no other companion files). It owns attack mechanics, network/cloud cybersecurity, cryptography (`CR-*`), and the exercise bank. This roadmap still owns order, cert mapping, and service vocabulary.

> **Refactor note (2026-09-24, C-17):** "Standalone" is superseded: the companion has self-contained content, and ownership is shared per the suite overlap register (§0.3). Its §2 bindings now use this file's IDs (§6.2 crosswalk).

**Lab safety:** local vulnerable-by-design fixtures only; no live DDoS, third-party scanning, malware, or credential stuffing against real accounts.

> **Refactor note (2026-09-24, C-47):** the suite-wide rule set is §0.5.

---

### 0.2 Learner teaching preferences (binding; copied unchanged from session-progress-ledger.md §5, invariant 4)

- **Check questions must be woven into the concept explanation itself**, not asked as separate "what do you already know" diagnostics — the learner explicitly opted out of background-probing questions and asked for calibration to happen through how they handle the material.
- **"Maintain curriculum depth and academic rigour"** has been repeated multiple times as an explicit standing instruction — do not compress, simplify, or skip the "why," even under time pressure or a fast pace of correct answers.
- When companion-file content (system-design-primer, SQL, design-patterns) overlaps a `Curriculum` module, **teach it once, stitched into the same session** — never as a separate pass, per each companion's own §0.2 stitching rules.
- If a companion file references module IDs that don't exist in `Curriculum` (as `sql-databases-companion.md` does), **say so plainly rather than forcing a silent, possibly-wrong mapping** — this was well received when done for the SQL companion.

### 0.3 Suite overlap and ownership register

*Refactor-authored (2026-09-24, §7 of the refactor prompt; C-17, C-36).* When two files touch the same concept, the **owner** teaches it and the others only **add**. Later sessions recall it in one line. Each companion's own overlap table is its slice of this register; on a conflict this register wins.

| Concept | Owner | Adds |
|---|---|---|
| DNS mechanics | `Curriculum` A5 | Primer SD-08 adds routing policies/TTL discipline; cyber NT-03/04 and DOS-02 add attacks |
| HTTP | `Curriculum` A5 | Primer SD-29 adds idempotency/HTTP/2/3; cyber PQ-S-04 adds the browser security preview |
| Cookie attributes (`Domain`, `Secure`, `HttpOnly`, `SameSite`, `__Host-`) | `Curriculum` A5 HTTP | Cyber AU-01…04 adds attacks at A10 |
| TLS | `Curriculum` A5 (mechanics) / A10 (formal) | Primer SD-35 transit slice; cyber CR-11/12, NT-08 |
| Load balancing, reverse proxy | `Curriculum` A5 / C3 | Primer SD-10/11; cyber NT-07, DOS-01 |
| Rate limiting | Cyber AB-01 (algorithms + abuse) | Primer Q22 is the design exercise and recalls AB-01 |
| Caching | Primer SD-26/27 | Cyber DOS-08 (stampede as an attack); SQL OD-09 (read path) |
| SQL injection / parameterisation | SQL SL-13 (the SQL mechanics) | Cyber WA-05 (attacker model across the whole injection family) |
| Field / column encryption | Cyber CR-17 (the cryptography) | SQL SL-13 `pgcrypto` syntax |
| Backup/restore | SQL OD-04 (runbook) + N2.3 | Cyber IR-07 (ransomware integrity) |
| 2PC / Saga / outbox | `Curriculum` A9 (theory) | SQL CS-07 + SL-10 (SQL); design-patterns ARCH-11 (shape) |
| Pub/Sub | `Curriculum` A7 | Primer SD-28; design-patterns DP-14 (Observer) |
| Shared responsibility | `Curriculum` B1 | Cyber PQ-S-03, CM-01 |
| Least privilege / IAM | `Curriculum` B5 | Primer SD-35; cyber CL-03…05, AU-14 |
| Floating point | M5 | SQL PQ-03 (decimal semantics) |
| Discrete-math foundations of relations | M1 | SQL PQ-01/02, RT-01 |
| Number theory for cryptography | M1 | Cyber CR-01…10 |
| Security checklist (encrypt in transit/at rest, XSS, SQLi, least privilege) | Distributed per C-28: `Curriculum` A5/A10/B5 + cyber modules | Primer SD-35 is an index module that points to each owner; its lab is shared with WA-05/SL-13 |
| Cache stampede / thundering herd | Primer SD-27 (mechanics: locking, request coalescing, TTL jitter; primer "my addition") | Cyber DOS-08 (adversarially triggered stampede) |
| Tail latency, percentiles, hedged requests | M6 (the math: order statistics, fan-out amplification) | Primer SD-03/SD-38c (design levers: timeouts, hedging, replicas); `Curriculum` C6/C7 (alerting/SLOs) |
| Little's law | M6 (statement + proof sketch) | Primer SD-03/SD-28 (sizing checks, e.g. 400 rps × 250 ms); the A2 slice (`primer-binding-table.md`) |
| CAP / PACELC | `Curriculum` A8 (CAP statement) → A9 (formal limits, PACELC) | Primer SD-04/SD-05 (per-dataset choice, GCP store mapping) |
| Consistent hashing | U2 (analysis: expected movement 1/N, virtual nodes, load bounds) | Primer SD-38a (sharding/rebalancing design); A4 ring slice |
| MapReduce / scatter-gather | A9 (distributed computation model) | Primer SD-38b/c, SX-08 (job patterns); `Curriculum` V-DATA (Dataflow/Dataproc) |
| CRDTs, operational transform | A9 deepening | Primer Q04 (Google Docs design problem) |
| Vector clocks, quorums, gossip | A9 deepening | Primer Q05 (Redis-like KV design problem), SD-39 papers |
| Heavy hitters / sketches / approximate counting | U2 (randomized algorithms) | Primer Q16/Q18 (design); SQL AN-04 (SQL approximation) |
| Unique ID generation (Base62, Snowflake) | Primer SX-02/Q17 | M1 (counting, birthday bound for collisions); A1 recall (bit layout) |
| Garbage collection | U4 (memory management) | Primer Q21 (design problem); SX-04 (data GC/TTL) |
| Event sourcing | Design-patterns ARCH-10 (shape) + A9 (theory) | Primer Q23 (stock exchange design); SQL IR/audit designs |
| Credential storage & replay | Cyber CR-13 (password KDFs) + CR-17/PV-03 (tokenization/encryption for replayable secrets) | Primer P04 (design context) + SD-35 check question |
| OOD problems O01–O07 | Primer (problems) | Design-patterns (principles and patterns they exercise, C-34); A4 recall |
| Interview/design method, back-of-the-envelope | Primer SD-00 | Track S1–S3 recall it; they never restate it (C-31) |
| Scaling evolution (single box → millions) | Primer P08 + SX-12 | Northstar milestones cite P08 steps (C-32); Track S4/S9 recall |
| Terraform labs | Primer TF-1…TF-7 (P08/P01/P07 infra) | SQL TF-DB*; Northstar reuses TF IDs rather than duplicating |
| Real-world architecture papers (Dynamo, Bigtable, Spanner, GFS, Chubby, MapReduce, Dapper, Kafka, ZooKeeper…) | Primer SD-39 / §6.4 (index) | A9 deepening and the university alignment appendix cite the same papers; the reading list lives once, in the primer |

### 0.4 Suite Teaching Contract

*Refactor-authored (2026-09-24, C-29, C-47, C-53, C-54, C-55, C-69, C-70, C-72, C-73, C-75).* One contract for every file. Each companion keeps its own §0.3 session text and points here. When two rules conflict, the higher one wins: (1) the learner's explicit instruction in the current chat · (2) the ledger §5 preferences (§0.2) · (3) the refactor invariants · (4) this file on order, cert timing and Lab Reality · (5) the owning companion on its content (§0.3) · (6) the companions' defaults · (7) `learn-SKILL.md` defaults.

**0.4.1 Rhythm.**

- One concept per turn, at full depth. New material is taught by direct explanation; procedures by worked, parallel examples.
- Every turn carries exactly one focused question, embedded in the teaching. Diagnosis happens through those checks; there is no separate probing (ledger §5 wins over the skill's calibrating question, C-70). A turn may be as long as one concept needs.
- Correction style: confirm the correct part explicitly, then sharpen the imprecise part by naming the exact mechanism. No false praise. Hold the line under "just tell me"; give a foothold when the learner is genuinely stuck.
- Overrides (C-75): the learner may skip (after passing the skip-test), jump, or go hands-on. Every override is recorded in the ledger so the prerequisite check can flag what was skipped.

**0.4.2 Suite Session Protocol (C-29).** When several files bind to one module, the session runs:

1. **Anchor** — list the bound IDs from *all* files (each companion's §2; the primer's from `primer-binding-table.md`).
2. **Concept** — taught once, by the owner in §0.3.
3. **Layers**, in fixed order: system design (primer) → SQL/engine → patterns → attacker/crypto (cyber).
4. **GCP lens.**
5. **One Numbers step** for the whole session.
6. **One application item**: a primer micro-problem *or* a companion exercise card, never both for the same concept.
7. **Checks**, woven in per ledger §5.
8. **Close**, ticking boxes in every file (§0.4.8).

**0.4.3 Exercise progression (C-54).** The first five rungs of the ten-rung ramp (anchor, vocabulary, representation, core move, worked illustration) are the teaching turns. Exercises then climb, one item per turn, advancing only when the current rung is passed: basic unseen check → routine variation → mixed transfer (the new idea plus exactly two earlier mastered ideas) → top-rung challenge → reflection (the learner explains back or invents an example).

**0.4.4 Predict → run → discrepancy (C-53).** Every exercise with a result shape, row count, plan shape, isolation outcome or attack outcome starts with a one-line prediction. Then run. A wrong prediction is recorded in the ledger and taught from.

**0.4.5 Mastery states.** Every ID is `not-started` → `in-progress` → `taught` (explained, first check answered) → `mastered` (passed a rung-3 or rung-4 item, or the skip-test). It may also be `shaky` (missed a check after teaching), `unverified` (claimed done without evidence) or `sliced` (only a named slice taught). Taught and mastered IDs get one-question recalls woven into later relevant sessions at about +1, +3, +7 and +21 sessions; a missed recall sets `shaky` and re-teaches only the gap. The misconception register lives in the ledger; checks probe each entry until two consecutive correct answers retire it.

**0.4.6 Anchoring and suite-wide Prop Lock (C-55).** No term, product or control is used in an explanation, example or check unless it is anchored: taught this session, or at least `taught` on the ledger. A named-but-not-taught mention is allowed only when labelled "we'll cover this in X". A check that relies on unanchored terms is invalid: fix the check; don't mark the learner shaky.

**0.4.7 Check questions and exercise pre-flight.** A check tests mechanism or application, asks one thing (C-69: split a multi-part check across turns), is answerable from anchored material, has a written expected answer and at least one expected wrong answer in the owning file's keys, is precision-sensitive, and is never answered by the tutor in the same turn. Before issuing any exercise the tutor checks: internal consistency (for example, a CNAME never points at an IP) · every term anchored · exactly one question · the answer derivable from what was taught · any numbers computed. An error found later is corrected openly in the next turn and logged in `errata.md`.

**0.4.8 Pacing, checkpoints and session close (C-72, C-73).** Each module is budgeted at roughly 3–5 concepts per session at full depth; an over-budget module is split into teaching blocks (C-49). The budget is a plan, never a reason to compress depth. A problem or checkpoint runs only when all its must-know IDs are at least `taught`, and it introduces at most one new concept. Every session ends by: (1) marking every ID bound to the session taught / sliced / deferred-with-reason / recalled (nothing left unmarked); (2) updating mastery states and the recall schedule; (3) updating the misconception register; (4) adding any errata; (5) emitting a ledger delta block (and a full ledger every 5th session or on request); (6) naming the exact resume point and any open question, verbatim.

### 0.5 Lab Safety

*Refactor-authored (2026-09-24, C-47, C-53).* One rule set for every file; it unifies the cybersecurity companion's rule 10, the SQL companion's rule 10 and the Lab Reality paragraph above.

1. **Hard bans:** no scanning of third parties; no malware; no live DDoS; no credential stuffing against real accounts; fixtures on localhost or disposable projects only; crypto through vetted libraries only.
2. **Money and time:** local first (Docker Postgres, local fixtures). Credit-using services are created for one lab and destroyed the same day, with a budget alert set before the first apply.
3. **Secrets and data:** never put a password, key or real customer data in a query, a prompt or a course file. Lab data is synthetic.
4. **The workplace console is read-only:** look, never create or change.
5. **Every lab carries a Lab Reality tag:** `[free-tier]` · `[credit ~$X]` · `[plan-only]` · `[paper]` · `[local]`.

## 1. The Phase Plan
```text
Phase 0  Universal Fundamentals (Track A)              ─┐
Phase 1  Cloud Core Concepts (Track B)                   ├─ run mostly in parallel,
Phase 2  DevOps/Containers/K8s/NGINX/CI-CD spine (Track C)│  woven together — this is
Phase 3  ML/AI Foundations (Track D)                    ─┘  the "consolidate common concepts" layer
 
Phase 4  GCP deep dive  →  sit PCA, then PMLE first (your named priorities)
Phase 5  Remaining GCP Professional certs (pick 2–4 that match your goals, not all 7; Agentic Architect is Phase 8)
Phase 6  AWS deep dive  →  SAP-C02, DOP-C02, AIP-C01, (SCS-C03, ANS-C01 if time allows)
Phase 7  Azure deep dive → AZ-305, AZ-400, SC-100
Phase 8  Agentic Architect (GA) once ADK/agent material is solid
```text
Why this order: everything in Phases 0–3 is provider-agnostic and is tested, in some form, on every single one of your eighteen certs. Front-loading it means each subsequent cert is 60–70% "same concepts, new console." GCP goes first because you named PCA/PMLE explicitly and have a workplace GCP account to look around in. AWS and Azure then go faster because you already know what a load balancer, an IAM policy, and a Kubernetes pod are — you're just learning new names and new console layouts for concepts you already own.
 
## PART I — Universal Foundations (Track A)
High-school-accessible, zero assumed background. This is what makes everything downstream make sense instead of feeling like memorized trivia.
 
### A1. Digital Logic & Data Representation
- [ ] A1 done
Bits, bytes, binary and hexadecimal number systems; why computers use base-2
Boolean logic (AND/OR/NOT/XOR) and truth tables — the literal basis of IAM policy evaluation, firewall rules, and CPU design
Binary vs. decimal storage prefixes (KiB/MiB/GiB vs KB/MB/GB) — directly relevant to cloud storage billing
Character encoding (ASCII, UTF-8) and why it matters for data pipelines
→ We start here, today, below.
> **Refactor note (2026-09-24, C-20):** Status as of 2026-09-24 (C-20, D2): the course is a fresh start, so this sentence is still true. The live position is kept in `session-progress-ledger.md`.
### A2. Math for Cloud & Machine Learning
- [ ] A2 done
Algebra refresher: functions, exponents, logarithms (logs matter for scaling, entropy, and Big-O)
Linear algebra essentials: vectors, matrices, dot products, matrix multiplication (the literal computation inside every neural network)
Probability & statistics: distributions, mean/variance/std-dev, conditional probability, Bayes' theorem, correlation vs causation
Calculus intuition: derivatives as "rate of change," gradients, why gradient descent trains ML models (no need for proof-level rigor — engineering intuition is the target)
> **Refactor note (2026-09-24, C-18):** First-pass scope: this intuition pass is the first pass and is complete as written. The rigorous passes follow in M2 (linear algebra), M3 (calculus) and M4 (probability & statistics).
Big-O notation for algorithm/cost reasoning
### A3. Programming Foundations
- [ ] A3 done
Python: variables, control flow, functions, data structures (list/dict/set/tuple), OOP basics, virtual environments, package management (pip)
Bash/shell scripting: variables, loops, conditionals, pipes, redirection, exit codes — essential for CI/CD scripts and automation everywhere
Working with APIs from code: HTTP clients, JSON parsing, SDKs (google-cloud-*, boto3, azure-sdk)
Git fundamentals (deep dive lives in A11)
### A4. Data Structures & Algorithms (engineering-practical depth, not competitive-programming depth)
- [ ] A4 done
Arrays, linked lists, hash maps, stacks/queues, trees, graphs
Big-O in practice: why a hash lookup beats a linear scan, why indexes matter in databases
Sorting/searching intuition (enough to reason about algorithmic choices, not to implement red-black trees from memory)
> **Refactor note (2026-09-24, C-18):** First-pass scope: A4 stays at engineering-practical depth. The rigorous pass (proofs, recurrences, and implementing a balanced search tree) is U2.
### A5. Computer Networking (heavily tested across every cloud architect/network/security cert)
- [ ] A5 done
The OSI model and TCP/IP model — what actually lives at each layer
IP addressing: IPv4 structure, subnetting and CIDR notation (binary math from A1 comes back here), IPv6 basics
Routing fundamentals: how packets find their way, default gateways, routing tables
TCP vs UDP: three-way handshake, reliability vs speed trade-offs
DNS: how domain resolution works, record types (A, AAAA, CNAME, MX, TXT, NS)
HTTP/HTTPS: request/response cycle, methods, status codes, headers, cookies
TLS/SSL: the handshake, certificates, certificate authorities (ties into A10 security)
> **Refactor note (2026-09-24, C-21):** TLS split: A5 teaches the handshake mechanics, certificates and CAs, plus a minimal public-key intuition bridge (what a key pair does, what a signature proves, why DH gives a shared secret). A10 formalizes the cryptographic primitives underneath and recalls A5 in one line.
NAT, firewalls, proxies vs reverse proxies (sets up NGINX in Track C)
Load balancing concepts: L4 vs L7, algorithms (round robin, least connections, consistent hashing)
VPNs and private connectivity concepts
### A6. Linux & Operating Systems
- [ ] A6 done
Processes, threads, memory management, the filesystem hierarchy
Linux shell essentials: navigation, permissions (chmod/chown), package managers, systemd/services
Containers vs VMs at the OS level: namespaces and cgroups (sets up Docker)
SSH and remote access
### A7. Software Architecture & APIs
- [ ] A7 done
Client-server model, monoliths vs microservices, trade-offs of each
REST principles, gRPC, GraphQL (awareness-level)
Synchronous vs asynchronous communication; message queues and event-driven architecture (sets up Pub/Sub, SQS/SNS, Service Bus)
API authentication patterns: API keys, OAuth 2.0, JWTs, service accounts

> **Refactor note (2026-09-24, C-49):** A7 binds several dozen suite concepts, so it is taught as ordered teaching blocks. These are sessions, not new modules; the module ID stays A7. A7.1 client-server and API styles (+ SD-32…SD-34) · A7.2 async and queues (+ SD-28) · A7.3 OOP foundations + SOLID · A7.4 GRASP + creational patterns · A7.5 structural patterns · A7.6 behavioral patterns · A7.7 architecture styles + DDD (ARCH-01…ARCH-08) · A7.8 API authentication/authorization + attacks · A7.9 abuse and rate limits · A7.10 S1–S2 · A7.11 N0 · A7.12 checkpoints. A5, A8 and A10 get the same split in R4, from the §0.4.8 pacing budget.
### A8. Databases & Data Modeling
- [ ] A8 done
Relational model, SQL fundamentals (SELECT/JOIN/GROUP BY, normalization)
ACID properties and transactions
NoSQL families: key-value, document, wide-column, graph — and when each fits
CAP theorem and its real engineering trade-offs
Data warehousing basics: OLTP vs OLAP, star schemas
Engine slices DB-1…DB-10 (bag relations, slotted page, buffer clock sweep, B-tree + inverted index, iterators + spill, histograms, MVCC visibility + deadlock detection, mini-WAL): owned and taught by `sql-databases-companion.md` §4.0 inside the A8 sessions *(added by the refactor, C-05)*
### A9. Distributed Systems Theory
- [ ] A9 done
Consistency models (strong, eventual), replication strategies
Partitioning/sharding, consensus (Raft/Paxos at a conceptual level — Spanner, etcd, and Kubernetes all depend on this)
Availability vs durability, failure modes, idempotency
Why "the network is reliable" is the first fallacy of distributed computing (and the other seven)
### A10. Security & Cryptography Fundamentals
- [ ] A10 done
Symmetric vs asymmetric encryption, hashing vs encryption, digital signatures
The TLS handshake in detail, PKI and certificate chains
> **Refactor note (2026-09-24, C-21):** A10 formalizes what A5 taught at mechanism level (see the A5 note); it does not re-teach the handshake.
Authentication vs authorization; identity federation, SSO, MFA
Common attack classes: injection, XSS, CSRF, DDoS, privilege escalation
Principle of least privilege, defense in depth, zero trust — the conceptual spine of every cloud IAM system



### A11. Software Delivery & Version Control
- [ ] A11 done
Git deep dive: branches, merges, rebases, conflict resolution, tagging
SDLC models, Agile/Scrum basics
Code review culture, trunk-based development vs GitFlow (relevant to CI/CD design choices later)
## PART II — Cloud Computing Core Concepts (Track B)
### B1. What Is Cloud Computing
- [ ] B1 done
Service models: IaaS, PaaS, SaaS, FaaS — and where each provider's services sit
Deployment models: public, private, hybrid, multi-cloud
The shared responsibility model (security "of" the cloud vs "in" the cloud) — appears on nearly every security-adjacent exam
### B2. Virtualization & Containers
- [ ] B2 done
Hypervisors (Type 1 vs Type 2), how a VM actually works
Containers: why they're lighter than VMs, the namespace/cgroup mechanics from A6
Image layering and immutability as a concept
### B3. Architecture Patterns & the Well-Architected Frameworks
- [ ] B3 done
High availability, fault tolerance, horizontal vs vertical scaling
Disaster recovery patterns: backup/restore, pilot light, warm standby, multi-site active-active — and RTO/RPO math
Provider-specific framework nuance: GCP's Architecture Framework (Operational Excellence, Security, Reliability, Performance/Cost) vs AWS's Well-Architected Framework (6 pillars incl. Sustainability) vs Azure's Well-Architected Framework (5 pillars). Same ideas, different names — we'll map them directly.
### B4. Cloud Economics & FinOps
- [ ] B4 done
Pay-as-you-go vs reserved/committed-use pricing, spot/preemptible instances
Cost visibility and optimization tooling per provider
Budget alerts, tagging/labeling for cost allocation
### B5. Cloud IAM Concepts (deep provider dives happen later; the model is universal)
- [ ] B5 done
Principals, roles/policies, resource hierarchies (org → folder/OU → project/account)
RBAC vs ABAC, policy inheritance, least-privilege design
Service accounts / managed identities and workload identity federation
## PART III — The DevOps / Containers / CI-CD Spine (Track C)
This is the cross-cutting engineering core you asked to be taught "in parallel" and "exhaustively." It underlies the DevOps Engineer, Cloud Developer, Cloud Architect, and DOP-C02/AZ-400 certs directly, and shows up as scenario content everywhere else.
 
### C1. Docker — full depth
- [ ] C1 done
Images vs containers, the union filesystem and layer caching
Writing Dockerfiles: FROM, RUN, COPY, ENTRYPOINT vs CMD, multi-stage builds for small production images
Container networking modes (bridge, host, none), volumes vs bind mounts vs tmpfs
Docker Compose for multi-container local dev
Registries: pushing/pulling, tagging strategy, image scanning for vulnerabilities
Security: running as non-root, minimal base images (distroless/alpine), secrets handling anti-patterns
### C2. Kubernetes — full depth
- [ ] C2 done
Architecture: control plane (API server, etcd, scheduler, controller manager) vs worker nodes (kubelet, kube-proxy, container runtime)
Core objects: Pods, ReplicaSets, Deployments, StatefulSets, DaemonSets, Jobs/CronJobs
Networking: Services (ClusterIP/NodePort/LoadBalancer), Ingress and Ingress controllers (NGINX Ingress lands here), Network Policies, the CNI model
Configuration: ConfigMaps, Secrets, environment injection
Storage: PersistentVolumes, PersistentVolumeClaims, StorageClasses, dynamic provisioning
Scheduling & scaling: node affinity/taints/tolerations, Horizontal Pod Autoscaler, Vertical Pod Autoscaler, Cluster Autoscaler
RBAC in Kubernetes, Pod Security Standards, admission controllers
Helm: charts, templating, releases
Operators and the Operator pattern (brief — enough for exam recognition)
Managed Kubernetes nuance: GKE (Autopilot vs Standard, node auto-provisioning, Workload Identity) vs EKS (Fargate vs managed node groups, IRSA) vs AKS (virtual nodes, Azure AD pod identity) — same primitives, different managed-service ergonomics
### C3. NGINX — full depth
- [ ] C3 done
Reverse proxy and forward proxy concepts (ties back to A5)
Core config syntax: server blocks, location matching, directives
Load balancing algorithms in NGINX (round robin, least_conn, ip_hash) and upstream blocks
TLS termination, HTTP→HTTPS redirects, HTTP/2
Caching and static content serving
NGINX as a Kubernetes Ingress Controller — how it fits into the C2 picture concretely
### C4. CI/CD — full depth
- [ ] C4 done
Concepts: build → test → package → deploy pipeline stages, artifact repositories
Deployment strategies: rolling, blue-green, canary — and how to pick one from a scenario
GitOps as a philosophy (declarative, git-as-source-of-truth, reconciliation loops) — ArgoCD/Flux at a working level
Provider-native tooling, mapped side by side:
Build: Cloud Build (GCP) ↔ CodeBuild (AWS) ↔ Azure Pipelines (build stage)
Deploy: Cloud Deploy (GCP) ↔ CodePipeline/CodeDeploy (AWS) ↔ Azure Pipelines/Release (Azure)
Universal/cross-cloud: GitHub Actions, Jenkins, GitLab CI
### C5. Infrastructure as Code
- [ ] C5 done
Declarative vs imperative provisioning, state management, drift detection
Terraform as our primary cross-cloud tool: providers, resources, modules, plan/apply/destroy, remote state, workspaces — this is what lets us build real GCP/AWS/Azure architectures without necessarily paying for them (we lean hard on terraform plan)
Native IaC per provider (recognize, don't need mastery of all): Deployment Manager / Config Connector / Infrastructure Manager (GCP), CloudFormation / CDK (AWS), ARM templates / Bicep (Azure)
### C6. Observability
- [ ] C6 done
The three pillars: metrics, logs, traces
Provider-native stacks: Cloud Monitoring/Logging/Trace (GCP) ↔ CloudWatch/X-Ray (AWS) ↔ Azure Monitor/Application Insights (Azure)
Open standards: Prometheus + Grafana, OpenTelemetry — increasingly tested because they're the multi-cloud-portable answer
### C7. SRE Principles
- [ ] C7 done
SLIs, SLOs, SLAs and how they relate; error budgets and burn-rate alerting
Toil and why eliminating it is an SRE's actual job
Incident management, on-call, postmortem culture (blameless postmortems)
This shows up explicitly and heavily on the PCA exam's Reliability domain and on DOP-C02/AZ-400 — it is not optional reading.
## PART IV — Machine Learning & AI Foundations (Track D)
Required for PMLE, AIP-C01, and Agentic Architect specifically — but every architect-level cert now touches "how do I put AI in this design" too.
 
### D1. Classical Machine Learning
- [ ] D1 done
Supervised vs unsupervised vs reinforcement learning
Regression, classification, clustering — core algorithms and when to use which
Train/validation/test splits, cross-validation
Evaluation metrics: accuracy, precision, recall, F1, ROC/AUC, confusion matrices — and why accuracy alone lies to you on imbalanced data
Overfitting/underfitting, the bias-variance tradeoff, regularization
Feature engineering: scaling, encoding categoricals, handling missing data, imbalanced datasets (SMOTE, class weighting)
### D2. Deep Learning
- [ ] D2 done
Neural network basics: neurons, layers, activation functions, forward pass
Backpropagation intuition (built on the calculus from A2)
CNNs (images), RNNs/LSTMs (sequences, mostly historical context now)
Transformers and attention — the architecture behind every modern LLM; this is a must-understand-deeply topic, not a footnote
### D3. MLOps
- [ ] D3 done
The end-to-end ML lifecycle: data → features → train → evaluate → deploy → monitor → retrain
Feature stores, model registries, experiment tracking
CI/CD/CT (continuous training) for ML pipelines
Model monitoring: drift, training-serving skew, performance decay
A/B testing and canary rollouts for models specifically
### D4. Generative AI, LLMs & Agents
- [ ] D4 done
How LLMs actually generate text (autoregressive next-token prediction, sampling, temperature)
Prompting techniques, few-shot vs zero-shot, system prompts
Embeddings and vector databases; Retrieval-Augmented Generation (RAG) architecture end to end
Fine-tuning vs prompt engineering vs RAG — when each is the right tool
Agentic patterns: tool use, planning/reasoning loops, multi-agent orchestration, agent-to-agent protocols (A2A) — directly relevant to the Agentic Architect cert
Responsible AI: bias, fairness, explainability, safety evaluation
Lab Reality (Track D) *(added by the refactor, C-46)*: D1 `[local]` notebooks (scikit-learn) · D2 `[local]` small models on CPU, `[plan-only]` for large training · D3 `[local]` tracking and pipelines, `[free-tier]` Vertex AI pieces where a free tier exists `(verify)` · D4 `[local]` RAG and agent prototypes, `[credit ~$X]` timeboxed model API calls `(verify)`.

### Reserved tracks M, U, S and N (stubs; authored in R4 and R9)

*Refactor-authored (2026-09-24).* The companions' foreign anchors were rebound to these IDs by the §6 crosswalks (`crosswalk.md`). Each ID is reserved here with its scope; the modules themselves are written in R4 (M, U, S) and R9 (N). Nothing here is teaching content yet.

| ID | Title | Scope (what the rebound references need) |
|---|---|---|
| M1 | Discrete Mathematics & Proof | logic, proof techniques, sets and relations, counting, graphs, elementary number theory |
| M2 | Linear Algebra | rigorous pass on A2 |
| M3 | Calculus | rigorous pass on A2 |
| M4 | Probability & Statistics | rigorous pass on A2 |
| M5 | Numerical Methods & Floating Point | IEEE 754, rounding, decimal vs binary |
| M6 | Information Theory & Performance Modeling | queueing, Little's law, tail latency |
| U1 | Computer Architecture & Systems Programming | machine-level representation, memory hierarchy |
| U2 | Algorithms: Design & Analysis | rigorous pass on A4 |
| U3 | Theory of Computation | automata, grammars, decidability |
| U4 | Programming Languages & Paradigms | paradigms, types, memory management |
| U5 | Concurrency & Parallel Computing | races, locks, deadlock, memory models |
| U6 | Software Engineering & Testing | requirements, testing theory, specification |
| U7 | Professional Practice, Ethics & Law | ethics, privacy law literacy, licensing |
| S1 | Requirements & quality attributes | Track S — System Architecture Design Studio |
| S2 | Architecture documentation | views, C4, ADRs, the HLD/LLD contract and NFR tables |
| S3 | Capacity & performance engineering | |
| S4 | Reliability architecture | |
| S5 | Data architecture | |
| S6 | Security architecture | threat-model-driven design |
| S7 | Integration & event-driven architecture | |
| S8 | Migration & modernization | |
| S9 | Cost architecture & unit economics | |
| S10 | Architecture evaluation | |
| S11 | Case-study studio | |
| N0…N12 | Northstar reference application | milestones and sections `Nx.y` in `northstar-reference-app.md` |

## PART V — Google Cloud Platform
Service map by category (the vocabulary we'll build fluency in)

*Category IDs (C-22, 2026-09-24).* Other files anchor to these IDs instead of the category names:

| V-ID | Category (line below) |
|---|---|
| V-COMP | Compute |
| V-STOR | Storage/DB |
| V-NET | Networking |
| V-DATA | Data/Analytics |
| V-AI | AI/ML |
| V-SEC | Security |
| V-OPS | Ops/DevOps |

Compute: Compute Engine, GKE, Cloud Run, App Engine, Cloud Functions
Storage/DB: Cloud Storage, Cloud SQL, Spanner, Bigtable, Firestore, Memorystore, AlloyDB
Networking: VPC, Cloud Load Balancing, Cloud CDN, Cloud Interconnect/VPN, Cloud DNS, Cloud Armor
Data/Analytics: BigQuery, Pub/Sub, Dataflow, Dataproc, Cloud Composer, Looker
AI/ML: Vertex AI (full suite: Workbench, Training, Pipelines, Feature Store, Model Registry, Endpoints, Vizier), Model Garden, Gemini Enterprise/Agent Platform, AutoML, BigQuery ML
Security: IAM, Cloud KMS, VPC Service Controls, Binary Authorization, Security Command Center, Google SecOps (Chronicle)
Ops/DevOps: Cloud Build, Cloud Deploy, Artifact Registry, Cloud Monitoring/Logging
Certification-by-certification breakdown
(Domain weights below are from the current official exam guides where I verified them directly; where I didn't verify exact percentages, I've given you the topic structure and flagged it — always cross-check the live guide a few weeks before you actually schedule.)
 
1. Professional Cloud Architect (PCA) — your named priority #1
- [ ] PCA passed
- **Lab Reality** *(added by the refactor, C-46)*: `[free-tier]` Compute Engine / Cloud Run / Cloud Storage builds · `[plan-only]` multi-region and hybrid designs · `[paper]` the published case studies.
 
Format: 50 scenario-based questions, 2 hours, includes 4 published case studies you study in advance
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** 50–60 questions; 4 case studies are published and 2 appear per exam. (verify live before scheduling)
Domains (verified): Designing (24%) · Provisioning (15%) · Security & Securing AI (20%) · Optimization (18%) · Implementation (11%) · Reliability & Well-Architected Framework (12%)
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** the live guide's weights are 25 / 17.5 / 17.5 / 15 / 12.5 / 12.5, under different section names. The line above keeps the 2026-09-16 reading. (verify live before scheduling)
What makes it hard: it's not "what does this service do," it's "given these constraints, which trade-off is correct" — architectural judgment, tested through the case studies
2. Professional Machine Learning Engineer (PMLE) — your named priority #2
- [ ] PMLE passed
- **Lab Reality** *(added by the refactor, C-46)*: `[local]` notebooks · `[credit ~$X]` timeboxed Vertex AI training/prediction (Part V note) · `[plan-only]` large training runs.
 
6 domains covering the full ML lifecycle: framing business problems as ML problems · architecting low-code/AutoML/BigQuery ML solutions · building with Google's AI APIs and foundation models (Gemini, Model Garden) · developing/scaling custom models (Vertex AI Training, distributed training, hyperparameter tuning) · automating MLOps pipelines (Vertex AI Pipelines, CI/CD/CT) · monitoring, responsible AI, and maintaining solutions in production
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** still 6 sections, renamed: low-code AI 13, data & models 16, scaling prototypes 21, serving 20, pipelines 18, monitoring 13. The exam moved from Vertex AI to the **Gemini Enterprise Agent Platform**. (verify live before scheduling)
Heavy 2026 emphasis on GenAI: Vertex AI Studio, Model Garden, RAG architectures
3. Data Engineer
- [ ] Professional Data Engineer passed
- **Lab Reality** *(added by the refactor, C-46)*: `[free-tier]` Pub/Sub and the BigQuery sandbox `(verify)` · `[credit ~$X]` short Dataflow runs · `[plan-only]` Dataproc/Composer at scale.
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** Active; a branding update is pending. (verify live before scheduling)
 
Designing data processing systems · building/operationalizing data pipelines (Dataflow, Dataproc, Pub/Sub, BigQuery, Composer) · operationalizing ML models · ensuring reliability, security, and compliance of data solutions
4. Cloud Developer
- [ ] Professional Cloud Developer passed
- **Lab Reality** *(added by the refactor, C-46)*: `[free-tier]` Cloud Run, Cloud Functions, Firestore · `[credit ~$X]` Cloud Build / Cloud Deploy beyond the free quota `(verify)`.
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** Active; its own page is live and registration is open, although it is missing from the certification index page's rendered list. (verify live before scheduling)
 
Designing highly scalable/available cloud-native apps · building and testing applications · deploying (Cloud Build, Cloud Deploy, Cloud Run/GKE/App Engine) · integrating with GCP managed services and APIs · monitoring application performance
5. Cloud DevOps Engineer
- [ ] Professional Cloud DevOps Engineer passed
- **Lab Reality** *(added by the refactor, C-46)*: `[free-tier]` Cloud Build, Cloud Monitoring/Logging · `[credit ~$X]` a short-lived GKE cluster.
 
Applying SRE principles to service design and operations (Track C7 directly) · building CI/CD pipelines · implementing observability · optimizing performance · managing releases and incidents
6. Cloud Security Engineer
- [ ] Professional Cloud Security Engineer passed
- **Lab Reality** *(added by the refactor, C-46)*: `[free-tier]` IAM and firewall rules · `[credit ~$X]` Cloud KMS keys `(verify)` · `[plan-only]` VPC Service Controls perimeters and organization policies (they need an organization).
 
Configuring access (IAM design) · configuring network security (VPC-SC, firewall, Cloud Armor) · ensuring data protection (KMS, DLP) · managing security operations · ensuring regulatory compliance
7. Cloud Network Engineer
- [ ] Professional Cloud Network Engineer passed
- **Lab Reality** *(added by the refactor, C-46)*: `[local]` packet labs · `[credit ~$X]` small VPC + load-balancer labs destroyed the same day · `[plan-only]` Interconnect / HA VPN designs.
 
Designing/planning GCP network architecture · implementing VPC · configuring network services (load balancing, DNS, CDN) · implementing hybrid connectivity (Interconnect/VPN) · implementing network security · managing/monitoring networks
8. Cloud Database Engineer
- [ ] Professional Cloud Database Engineer passed
- **Lab Reality** *(added by the refactor, C-46)*: `[local]` Postgres (SQL companion lab kit) · `[credit ~$X]` Cloud SQL destroyed the same day · `[plan-only]` Spanner and AlloyDB.
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** Active; a branding update is pending. Guide weights: design ~32%, manage ~25%, migrate ~23%, deploy ~20%. (verify live before scheduling)
 
Designing scalable/secure database solutions (choosing the right DB from the whole storage list) · managing solutions (migration, provisioning) · designing for security/compliance · optimizing performance and monitoring
9. Security Operations Engineer (newer cert — verify current exam guide closer to study time)
- [ ] Professional Security Operations Engineer passed
- **Lab Reality** *(added by the refactor, C-46)*: `[paper]` detection engineering · `[local]` log fixtures · `[plan-only]` Google SecOps, an enterprise product `(verify)` trial availability.
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** Active. Six sections: platform operations 14, data management 14, threat hunting 19, detection engineering 22, incident response 21, observability 10. (verify live before scheduling)
 
Threat detection and hunting · SIEM/SOAR configuration and use (Google SecOps/Chronicle) · incident response · threat intelligence · using Gemini-assisted security operations tooling
10. Agentic Architect (Beta → GA) — we're deliberately doing this last, per the plan above
- [ ] Agentic Architect passed
- **Lab Reality** *(added by the refactor, C-46)*: `[local]` ADK agents · `[credit ~$X]` model API calls beyond the free quota `(verify)`.
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** Still in beta, open until Sept 30, 2026. The exam is 3 hours: about 80 multiple-choice questions, then labs in Google Skills. Five sections, with custom agents at about 33%. The guide names ADK, A2A and **MCP**; it does **not** name "Agent Registry" or "Agent Gateway". (verify live before scheduling)
 
Two-part exam: proctored multiple-choice (conceptual/design) plus hands-on coding labs on Google Skills
~5 sections; roughly a third of the exam is writing actual agent code
Built around: Agent Development Kit (ADK), Agent Registry, Agent Gateway, the A2A (agent-to-agent) protocol, LLM/agent design patterns, reliability/cost/security/scalability of agentic systems
Lab Reality (GCP): Compute Engine (e2-micro), Cloud Run, Cloud Functions, Cloud Storage, Firestore, and Pub/Sub all have genuine always-free tiers — we'll build real projects on these at zero cost. Your $300 credit is the right budget for: a short-lived GKE cluster, a small BigQuery dataset, and Vertex AI training/prediction experiments — we'll timebox these deliberately. Spanner, multi-region deployments, and Anthos we'll study via architecture + Terraform-plan only, and via read-only tours of your workplace console (never creating/modifying resources there).
 
## PART VI — AWS
Service map by category (cross-referenced to GCP — see Part VIII for the full table)
Compute: EC2, Lambda, ECS/EKS, Fargate, App Runner · Storage/DB: S3, EBS, RDS, DynamoDB, Aurora · Networking: VPC, ELB (ALB/NLB), Route 53, CloudFront, Direct Connect · Data: Kinesis, Glue, Redshift, EMR · AI/ML: SageMaker, Bedrock · Security: IAM, KMS, GuardDuty, Security Hub, Macie · DevOps: CodeBuild/CodePipeline/CodeDeploy, CloudFormation/CDK
 
1. Solutions Architect – Professional (SAP-C02)
- [ ] AWS SAP passed
- **Lab Reality** *(added by the refactor, C-46)*: `[free-tier]` single-account labs · `[plan-only]` Organizations / multi-account Terraform.
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** Domain weights 26/29/25/20 confirmed. **SAP-C02 is being replaced:** SAP-C03 registration opens Oct 27, 2026, and the last day for SAP-C02 is Nov 17, 2026. (verify live before scheduling)
 
4 domains: Design for Organizational Complexity (~26%) · Design for New Solutions (~29%) · Continuous Improvement for Existing Solutions (~25%) · Accelerate Workload Migration and Modernization (~20%) (check current guide for exact figures)
Heavy on multi-account strategy (AWS Organizations, SCPs), the 6 R's of migration, and cost/resilience trade-offs at enterprise scale
2. DevOps Engineer – Professional (DOP-C02)
- [ ] AWS DOP passed
- **Lab Reality** *(added by the refactor, C-46)*: `[free-tier]` CodeBuild/CodePipeline within the free quota `(verify)` · `[plan-only]` the rest.
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** Active. Six domains, 22/17/15/15/14/17. The Korean-language exam retires after Dec 31, 2026. (verify live before scheduling)
 
~6 domains: SDLC Automation · Configuration Management & IaC · Resilient Cloud Solutions · Monitoring & Logging · Incident & Event Response · Security & Compliance
Direct extension of Track C — you'll recognize nearly everything, just under AWS-native tool names
3. Generative AI Developer – Professional (AIP-C01) — genuinely new (2025/2026), one of AWS's hardest exams by reputation
- [ ] AWS AIP passed
- **Lab Reality** *(added by the refactor, C-46)*: `[local]` RAG prototypes · `[credit ~$X]` Bedrock calls (no free tier assumed; `(verify)`).
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** Active. Five domains: FM integration & data 31, implementation 26, AI safety/governance 20, efficiency 12, testing 11. (verify live before scheduling)
 
Domains cover: selecting/architecting with foundation models (Bedrock) · building resilient, provider-flexible GenAI architectures · RAG, vector stores, and knowledge base design · data security, privacy, and responsible-AI governance for GenAI systems · cost/latency/performance optimization
Recommendation candidates already hold AWS ML/Data Engineer associate-level knowledge — we'll build that via Track D first
4. Security – Specialty (SCS-C03) (corrected from your SCS-C02 — that version retired Dec 1, 2025)
- [ ] AWS SCS passed
- **Lab Reality** *(added by the refactor, C-46)*: `[free-tier]` IAM and KMS basics · `[plan-only]` organization-level controls.
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** Weights confirmed. The last domain is named **"Security Foundations and Governance" (14%)**, not "Management & Security Governance". (verify live before scheduling)
 
Current domains (Dec 2025 refresh): Identity & Access Management (~20%) · Data Protection (~18%) · Infrastructure Security (~18%) · Detection (~16%, now its own domain) · Incident Response (~14%) · Management & Security Governance
New emphasis on GenAI-application security guardrails
5. Advanced Networking – Specialty (ANS-C01) — last exam day Dec 31, 2026 per AWS, no announced successor
- [ ] AWS ANS passed
- **Lab Reality** *(added by the refactor, C-46)*: `[local]` BGP labs in containers · `[plan-only]` Direct Connect and Transit Gateway.
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** Retiring: last exam day Dec 31, 2026; no new certifications are issued after retirement. Domains 30/26/20/24. (verify live before scheduling)
 
Hybrid IT network architecture at scale: BGP, Direct Connect, Transit Gateway, multi-region networking, network security (WAF/Shield/Network Firewall), automation
Five-year-networking-experience recommended candidate; we'll fold the concepts into Track A5/C naturally either way — the cert itself is optional depending on how our timeline looks by mid-2026
> **Refactor note (2026-09-24, C-20):** mid-2026 has passed. The ANS-C01 decision is due before its last exam day, Dec 31, 2026 (verified 2026-09-24; verify live).
Lab Reality (AWS): Free tier covers EC2 t2/t3.micro (750 hrs/mo for 12 months on new accounts — check current status of your account), Lambda (1M requests/mo, always-free), S3 (5GB), DynamoDB (25GB, always-free). For VPC/networking/multi-account work we'll build with Terraform and validate via plan, since Organizations/Transit Gateway/multi-account labs cost real money fast.
> **Refactor note (2026-09-24, D4):** new AWS accounts since July 2025 get a credit-based free plan instead of the 12-month free tier described above (verify).
 
## PART VII — Azure
Service map by category
Compute: Virtual Machines, AKS, Container Apps, Functions, App Service · Storage/DB: Blob Storage, Azure SQL Database, Cosmos DB, Managed Disks · Networking: VNet, Azure Load Balancer, Application Gateway, Front Door, Azure DNS, ExpressRoute · Data: Synapse Analytics, Data Factory, Stream Analytics · AI/ML: Azure Machine Learning, Azure AI Foundry (OpenAI Service) · Security: Microsoft Entra ID, Key Vault, Microsoft Defender, Microsoft Sentinel · DevOps: Azure Pipelines, Azure Repos, ARM/Bicep
 
Provider-specific nuance to know up front: unlike GCP and AWS, Azure's Expert-tier exams have real prerequisites — AZ-305 requires an active AZ-104; AZ-400 requires AZ-104 or AZ-204; SC-100 requires one of AZ-500/SC-200/SC-300. This means your Azure path structurally requires associate-level certs first even though you only named the Expert ones — we'll fold AZ-104-equivalent knowledge into Track G teaching either way, whether or not you sit that exact exam.

> **Refactor note (2026-09-24, C-19):** there is no Track G. AZ-104-equivalent knowledge folds into Phase 7 through B5 and C-track recall, taught as the sub-block below.

**AZ-104-equivalent sub-block** *(added by the refactor, C-19; Phase 7, before AZ-305)*: Entra ID and Azure RBAC (recall B5) · VNet, NSGs, Load Balancer and Azure DNS (recall A5 and Part VIII) · virtual machines and storage (recall B2, C1 and Part VIII) · Azure Monitor (recall C6) · governance with Azure Policy (recall B5, Part VIII). Check the topic list against the live AZ-104 guide `(verify)`.
 
1. Solutions Architect Expert (AZ-305) (English version last updated April 17, 2026 — current)
- [ ] Azure AZ-305 passed
- **Lab Reality** *(added by the refactor, C-46)*: `[paper]` design documents · `[free-tier]` small always-free services.
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** Confirmed: skills as of Apr 17, 2026; the prerequisite is Azure Administrator Associate. (verify live before scheduling)
 
Scenario-heavy, spans identity, data, infrastructure, and governance design decisions
No live labs (unlike AZ-104); rewards architectural judgment over recall — closest Azure analog to the GCP PCA
2. DevOps Engineer Expert (AZ-400)
- [ ] Azure AZ-400 passed
- **Lab Reality** *(added by the refactor, C-46)*: `[free-tier]` Azure DevOps / GitHub Actions minutes `(verify)`.
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** Skills revised as of **July 27, 2026**; build/release pipelines is 50–55%. (verify live before scheduling)
 
Source control strategy, CI/CD pipeline design (Azure Pipelines + GitHub Actions), IaC (ARM/Bicep/Terraform), release/deployment strategies, security & compliance in the pipeline, monitoring feedback loops
The direct Track C capstone for Azure
3. Cybersecurity Architect Expert (SC-100) (English version updated July 28, 2026 — current)
- [ ] Azure SC-100 passed
- **Lab Reality** *(added by the refactor, C-46)*: `[paper]` Zero Trust designs · `[free-tier]` Entra ID basics.
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** The study guide now shows skills measured **as of Oct 21, 2026** (an upcoming revision). The AZ-500 prerequisite is now listed as **"Cloud and AI Security Engineer Associate"**. (verify live before scheduling)
 
Designing Zero Trust strategy, security operations/identity/compliance architecture across hybrid environments
Growing AI-governance content share (10–12%+ by mid-2026 per Microsoft's own roadmap signals)
Lab Reality (Azure): Free account gives $200 credit for 30 days plus always-free services (small VM instances, limited Functions executions, Cosmos DB free tier). Because that initial credit window is short, we'll time our Azure phase deliberately and lean on Terraform-plan + architecture design work for anything beyond the always-free slice.
 
## PART VIII — Cross-Provider Concept Map
The "don't learn it three times" table. Same underlying idea, three names.
 
Concept	GCP	AWS	Azure
Virtual machines	Compute Engine	EC2	Virtual Machines
Managed Kubernetes	GKE	EKS	AKS
Serverless containers	Cloud Run	App Runner / Fargate	Container Apps
Functions-as-a-service	Cloud Functions	Lambda	Azure Functions
PaaS app hosting	App Engine	Elastic Beanstalk	App Service
Object storage	Cloud Storage	S3	Blob Storage
Block storage	Persistent Disk	EBS	Managed Disks
Managed relational DB	Cloud SQL	RDS	Azure SQL Database
Globally distributed DB	Spanner	Aurora Global/DynamoDB	Cosmos DB
Wide-column NoSQL	Bigtable	DynamoDB / Keyspaces	Cosmos DB (Cassandra API)
Document NoSQL	Firestore	DynamoDB	Cosmos DB
In-memory cache	Memorystore	ElastiCache	Azure Cache for Redis
Data warehouse	BigQuery	Redshift	Synapse Analytics
Pub/Sub messaging	Pub/Sub	SNS + SQS	Service Bus / Event Grid
Stream/batch data processing	Dataflow (Apache Beam)	Kinesis / Glue	Stream Analytics
Managed Spark/Hadoop	Dataproc	EMR	HDInsight
Data pipeline orchestration	Cloud Composer (Airflow)	MWAA (Airflow)	Data Factory
BI/visualization	Looker / Looker Studio	QuickSight	Power BI
Virtual network	VPC	VPC	VNet
Load balancing	Cloud Load Balancing	ELB (ALB/NLB/GLB)	Load Balancer / App Gateway
CDN	Cloud CDN	CloudFront	Azure CDN / Front Door
DNS	Cloud DNS	Route 53	Azure DNS
Hybrid connectivity	Cloud Interconnect/VPN	Direct Connect/VPN	ExpressRoute/VPN Gateway
Identity & access	Cloud IAM	AWS IAM	Microsoft Entra ID + Azure RBAC
Key management	Cloud KMS	AWS KMS	Key Vault
Secrets management	Secret Manager	Secrets Manager	Key Vault
WAF / DDoS protection	Cloud Armor	AWS WAF / Shield	Azure WAF / DDoS Protection
Container registry	Artifact Registry	ECR	Azure Container Registry
CI build service	Cloud Build	CodeBuild	Azure Pipelines
CD/release service	Cloud Deploy	CodePipeline/CodeDeploy	Azure Pipelines/Release
Native IaC	Deployment Manager / Config Connector	CloudFormation / CDK	ARM / Bicep
Metrics/monitoring	Cloud Monitoring	CloudWatch	Azure Monitor
Logging	Cloud Logging	CloudWatch Logs	Azure Monitor Logs
Distributed tracing	Cloud Trace	X-Ray	Application Insights
ML platform	Vertex AI	SageMaker	Azure Machine Learning
GenAI/foundation models	Model Garden / Gemini	Bedrock	Azure AI Foundry (OpenAI Service)
Org hierarchy	Org → Folder → Project	Organization → OU → Account	Management Group → Subscription
Org-wide policy	Organization Policy	Service Control Policies	Azure Policy
SIEM/SecOps	Google SecOps (Chronicle)	Security Hub / GuardDuty	Microsoft Sentinel / Defender
## PART IX — Time-Sensitive Notes Recap
> **Refactor note (2026-09-24, C-48):** status as of 2026-09-24: the three notes below were re-checked that day (`cert-verification.md`). New dated items are in the Part V–VII verification notes. R4 moves every date-bearing line into `volatility-register.md` with a last-checked date.
Agentic Architect beta closes Sept 30, 2026 — we're intentionally skipping the beta window and targeting GA later.
AWS ANS-C01 last exam Dec 31, 2026 — decide later, once we see real progress against the plan; no shame either way.
AWS Security Specialty is now SCS-C03, not SCS-C02 — already corrected in this plan.
Check every exam guide's live PDF ~4–6 weeks before you actually schedule — Google, AWS, and Microsoft all revise domain weights and content periodically (several did so earlier this year), and I'll flag anything relevant I notice as we go, but I can't watch it continuously between our sessions.
## PART X — How We'll Actually Work
Each session, we take one module from the plan above, I teach it properly (explanations, worked examples, real config/code where it applies, checks for understanding), and we mark it done. Tell me any time you want to:
 
Skip ahead on something you already know (say so — no need to sit through material you've got)
Jump to a specific cert's material directly instead of following the phase order
Go hands-on on something — I'll tell you honestly whether it fits free tier, needs a slice of your $300, or should stay as a Terraform-plan/console-read exercise

> **Refactor note (2026-09-24, C-75):** these overrides are the suite-wide rule in §0.4.1; the session shape is §0.4.2.
We start with A1: Digital Logic & Data Representation below, right now.

> **Refactor note (2026-09-24, C-20):** Status as of 2026-09-24 (C-20, D2): the course is a fresh start, so this sentence is still true. The live position is kept in `session-progress-ledger.md`.


---

## Pre-refactor text archive (D3)

*Refactor-authored section (2026-09-24).* Decision D3 says content may be re-arranged but never removed. Each block below is the exact pre-refactor text (after the §5 ID renames) of a line that R2 corrected or regenerated. It is kept for provenance only and is **not authoritative**; the live text above wins. Tooling excludes this section from ID and anchor checks.

**D3-01** · C-44 · §0 scope paragraph

```text
Scope, honestly. Fifteen professional-tier certifications, three providers, plus the full engineering stack underneath them, is not a weekend, a month, or even a semester. Treated seriously — with real understanding, not memorized dumps — this is 18–30 months of consistent study for someone starting from true fundamentals. I'm telling you this not to discourage you but so we plan like adults: we go in phases, we build real skill that transfers across providers (so cert #2 through #15 get progressively faster), and we don't burn your $300 GCP credit or your motivation in week one.
```

**D3-02** · C-44 · "Why this order" paragraph

```text
Why this order: everything in Phases 0–3 is provider-agnostic and is tested, in some form, on every single one of your fifteen certs. Front-loading it means each subsequent cert is 60–70% "same concepts, new console." GCP goes first because you named PCA/PMLE explicitly and have a workplace GCP account to look around in. AWS and Azure then go faster because you already know what a load balancer, an IAM policy, and a Kubernetes pod are — you're just learning new names and new console layouts for concepts you already own.
```

**D3-03** · C-44 · Phase 5 line

```text
Phase 5  Remaining GCP Professional certs (pick 2–4 that match your goals, not all 8)
```
