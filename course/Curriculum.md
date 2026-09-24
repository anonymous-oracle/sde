# The Consolidated Cloud Mastery Curriculum
Fundamentals → GCP + AWS + Azure Professional/Expert Certifications → DevOps/Docker/K8s/NGINX/CI-CD
Built September 16, 2026. This is our shared syllabus — I'll teach from it session by session.
 
## 0. Read this first
Scope, honestly. Eighteen professional-tier certifications, three providers, plus the full engineering stack underneath them, is not a weekend, a month, or even a semester. Treated seriously — with real understanding, not memorized dumps — this is 18–30 months of consistent study for someone starting from true fundamentals. I'm telling you this not to discourage you but so we plan like adults: we go in phases, we build real skill that transfers across providers (so cert #2 through #18 get progressively faster), and we don't burn your $300 GCP credit or your motivation in week one.
 
Two time-sensitive corrections to your list, found while researching today:
 
Agentic Architect (Beta) — registration is open now and the beta window closes September 30, 2026 — about two weeks from today. Realistically, you cannot go from zero to exam-ready in two weeks while also learning fundamentals. My recommendation: let the beta window pass. The certification will reach General Availability afterward and you'll sit it properly, later, once you have the ADK/agent-building foundation (Track D4) and general GCP experience. Chasing the beta discount now would mean skipping comprehension for speed — exactly what you told me not to do.
> **Verified 2026-09-24 against the vendor's live page:** the beta is still open until Sept 30, 2026. The GA date is not announced; recheck after the window closes. (verify live before scheduling)
AWS Security Specialty — your list says SCS-C02. That exam was decommissioned December 1, 2025; it's been replaced by SCS-C03 (restructured domains, new question types, added GenAI-security content). I've planned around SCS-C03.
One item on your list is confirmed accurate as stated: AWS Advanced Networking Specialty (ANS-C01) — official AWS page confirms last exam day is December 31, 2026. That's tight (3.5 months) and it's a five-year-experience-recommended exam with no announced successor. We'll revisit whether to chase it or let it lapse once you see how the rest of the pace goes — I'd rather you have real distributed-networking skill than a rushed cert for an exam being retired anyway.
> **Verified 2026-09-24 against the vendor's live page:** ANS-C01's last exam day is still Dec 31, 2026, with no successor. (verify live before scheduling)
 
Your hands-on reality (given $300 GCP credit, permanent free tier, a workplace GCP account you can look in but not touch, and AWS/Azure free tier only) is threaded through every module below as an explicit "Lab Reality" note. Short version: we'll do real hands-on work for anything that fits free tier or a small slice of the $300; for expensive/enterprise-only services (Spanner multi-region, BigQuery at scale, multi-region GKE, Anthos, etc.) we'll write real Terraform/gcloud/kubectl that we validate with plan/dry-run but don't apply, and use your workplace console read-only, as a museum, never to create or change anything there. That combination genuinely builds real, defensible skill — architects are hired for judgment about services they've read deeply and reasoned about, not just ones they've clicked.
 
### 0.1 The course parts and the companion stitch rule

This course is one course in six parts. This roadmap, the **main course**, is the **only parent**: every companion binds its modules to the IDs below, and a module ID from any part may be used as a stitch tag in any other part. The parts:

- **The Consolidated Cloud Mastery Curriculum** (this part, the main course) — order, cert timing, Lab Reality and track structure.
- **The System Design Primer Companion — GCP-Native Edition** — the system-design layer (SD, SX, P, O, Q, TF). Its §2 stitch table binds its IDs to the modules here.
- **The SQL & Databases Companion — GCP-Native Edition** — SQL, relational theory and engine internals. It owns the engine slices DB-1…DB-10.
- **Design Patterns, SOLID & Clean Architecture — A Companion Curriculum** — OOP design theory, patterns and architecture styles (A7, A9).
- **The Cloud Cybersecurity Companion** — security, attacks and cryptography.
- **The Go Language Companion — Syntax, Semantics, Runtime and Contrasts** — the implementation language: Go's grammar, semantics, runtime and toolchain, each construct contrasted with Python, Java, C and JavaScript, and authentication and payment integration built from scratch in Go. Its language core is the Go block of A3; its later modules bind where they are first used (rule 0.4.9).

Progress lives in the inline `- [ ]` boxes of the six parts, which are authoritative. The tutor also keeps a **progress ledger**, a running record beside the boxes: each ID's mastery state (§0.4.5), the misconception register, the errata list, the recorded overrides and wrong predictions, and the exact resume point (§0.4.8).

Each companion's §2 lists what it binds to each module. When a module is taught, every bound companion ID is taught in the same session, once, by its owner (§0.3), in the order §0.4 gives. The cybersecurity stitch rule, first added to this roadmap on 2026-09-22 between A10 and A11:

---

#### Companion — Cloud Cybersecurity

**Standing stitch rule.** Teach security-relevant sections of this roadmap with **The Cloud Cybersecurity Companion**. Whenever **A5**, **A7 (auth patterns)**, **A10**, **B1 (shared responsibility)**, **B5**, **C1/C2 hardening**, **Phase 4 Networking/Security**, or the **Cloud Security / Network / SecOps** cert tracks are taught, also teach every companion module bound in companion **§2** in the **same session** — one story, never twice.

That companion owns attack mechanics, network/cloud cybersecurity, cryptography (`CR-*`), and the exercise bank; where a concept is shared with another part, the overlap register (§0.3) names the owner. This roadmap still owns order, cert mapping, and service vocabulary.

**Lab safety:** local vulnerable-by-design fixtures only; no live DDoS, third-party scanning, malware, or credential stuffing against real accounts. The full rule set is §0.5.

---

### 0.2 Learner teaching preferences (binding)

- **Check questions must be woven into the concept explanation itself**, not asked as separate "what do you already know" diagnostics — the learner explicitly opted out of background-probing questions and asked for calibration to happen through how they handle the material.
- **"Maintain curriculum depth and academic rigour"** has been repeated multiple times as an explicit standing instruction — do not compress, simplify, or skip the "why," even under time pressure or a fast pace of correct answers.
- When companion-file content (system-design-primer, SQL, design-patterns) overlaps a main-course module, **teach it once, stitched into the same session** — never as a separate pass, per each companion's own §0.2 stitching rules.
- If a companion file references module IDs that don't exist in the main course (as the SQL companion's did before its IDs were rebound), **say so plainly rather than forcing a silent, possibly-wrong mapping** — this was well received when done for the SQL companion.

### 0.3 Suite overlap and ownership register

When two files touch the same concept, the **owner** teaches it and the others only **add**. Later sessions recall it in one line. Each companion's own overlap table is its slice of this register; on a conflict this register wins.

| Concept | Owner | Adds |
|---|---|---|
| DNS mechanics | A5 | Primer SD-08 adds routing policies/TTL discipline; cyber NT-03/04 and DOS-02 add attacks |
| HTTP | A5 | Primer SD-29 adds idempotency/HTTP/2/3; cyber PQ-S-04 adds the browser security preview |
| Cookie attributes (`Domain`, `Secure`, `HttpOnly`, `SameSite`, `__Host-`) | A5 HTTP | Cyber AU-01…04 adds attacks at A10 |
| TLS | A5 (mechanics) / A10 (formal) | Primer SD-35 transit slice; cyber CR-11/12, NT-08 |
| Load balancing, reverse proxy | A5 / C3 | Primer SD-10/11; cyber NT-07, DOS-01 |
| Rate limiting | Cyber AB-01 (algorithms + abuse) | Primer Q22 is the design exercise and recalls AB-01; Go companion GO-19 (`golang.org/x/time/rate`) |
| Caching | Primer SD-26/27 | Cyber DOS-08 (stampede as an attack); SQL OD-09 (read path) |
| SQL injection / parameterisation | SQL SL-13 (the SQL mechanics) | Cyber WA-05 (attacker model across the whole injection family); Go companion GO-22 (placeholders in `database/sql`) |
| Field / column encryption | Cyber CR-17 (the cryptography) | SQL SL-13 `pgcrypto` syntax |
| Backup/restore | SQL OD-04 (runbook) + OD-11 (Cloud SQL backups and PITR) | Cyber IR-07 (ransomware integrity) |
| 2PC / Saga / outbox | A9 (theory) | SQL CS-07 + SL-10 (SQL); design-patterns ARCH-11 (shape) |
| Pub/Sub | A7 | Primer SD-28; design-patterns DP-14 (Observer) |
| Shared responsibility | B1 | Cyber PQ-S-03, CM-01 |
| Least privilege / IAM | B5 | Primer SD-35; cyber CL-03…05, AU-14 |
| Floating point | A2 | SQL PQ-03 (decimal semantics); Go companion GO-03 (no implicit conversions) |
| Discrete-math foundations of relations | SQL PQ-01/02 | SQL RT-01 |
| Security checklist (encrypt in transit/at rest, XSS, SQLi, least privilege) | Distributed per A5/A10/B5 + cyber modules | Primer SD-35 is an index module that points to each owner; its lab is shared with WA-05/SL-13 |
| Cache stampede / thundering herd | Primer SD-27 (mechanics: locking, request coalescing, TTL jitter; primer "my addition") | Cyber DOS-08 (adversarially triggered stampede) |
| Tail latency, percentiles, hedged requests | Primer SD-03/SD-38c (percentiles; design levers: timeouts, hedging, replicas) | C6/C7 (alerting/SLOs) |
| Little's law | Primer SD-03/SD-28 (L = λW; sizing checks, e.g. 400 rps × 250 ms) | the A2 slice (primer §2 stitch table) |
| CAP / PACELC | A8 (CAP statement) → A9 (formal limits, PACELC) | Primer SD-04/SD-05 (per-dataset choice, GCP store mapping) |
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
| Authentication built in code: sessions, signed tokens, one-time codes, OAuth client | Cyber AU-01…AU-10 and CR-05…CR-07, CR-13, CR-16 (the attacks and the primitives) | Go companion GO-28 (each piece built from scratch in Go against its RFC test vectors, then with a vetted library) |
| Payment-provider integration: idempotent create, signed webhooks, ledger writes, reconciliation | Go companion GO-29 (the integration code) | SQL DD-03 (the ledger rules it follows); Cyber PV-03 (tokenization, PCI DSS scope) and AB-06/AB-07 (checkout abuse); Primer SD-28 (queues, back-pressure) |

### 0.4 Suite Teaching Contract

One contract for every part; each companion carries the same contract in its own §0 and adds its session detail. When two rules conflict, the higher one wins: (1) the learner's explicit instruction in the current chat · (2) the learner teaching preferences (§0.2) · (3) this main course on order, cert timing and Lab Reality · (4) the owning part on its content (§0.3) · (5) the companions' defaults.

**0.4.1 Rhythm.**

- One concept per turn, at full depth. New material is taught by direct explanation; procedures by worked, parallel examples.
- Every turn carries exactly one focused question, embedded in the teaching. Diagnosis happens through those checks; there is no separate probing (the learner preferences in §0.2 rule out separate calibrating questions). A turn may be as long as one concept needs.
- Correction style: confirm the correct part explicitly, then sharpen the imprecise part by naming the exact mechanism. No false praise. Hold the line under "just tell me"; give a foothold when the learner is genuinely stuck.
- Overrides: the learner may skip (after passing the skip-test), jump, or go hands-on. Every override is recorded in the ledger so the prerequisite check can flag what was skipped.

**0.4.2 Suite Session Protocol.** When several files bind to one module, the session runs:

1. **Anchor** — list the bound IDs from *all* files (each companion's §2).
2. **Concept** — taught once, by the owner in §0.3.
3. **Layers**, in fixed order: system design (primer) → SQL/engine → patterns → Go implementation (Go companion) → attacker/crypto (cyber).
4. **GCP lens.**
5. **One Numbers step** for the whole session.
6. **One application item**: a primer micro-problem *or* a companion exercise card, never both for the same concept.
7. **Checks**, woven in per §0.2.
8. **Close**, ticking boxes in every file (§0.4.8).

**0.4.3 Exercise progression.** The first five rungs of the ten-rung ramp (anchor, vocabulary, representation, core move, worked illustration) are the teaching turns. Exercises then climb, one item per turn, advancing only when the current rung is passed: basic unseen check → routine variation → mixed transfer (the new idea plus exactly two earlier mastered ideas) → top-rung challenge → reflection (the learner explains back or invents an example).

**0.4.4 Predict → run → discrepancy.** Every exercise with a result shape, row count, plan shape, isolation outcome or attack outcome starts with a one-line prediction. Then run. A wrong prediction is recorded in the ledger and taught from.

**0.4.5 Mastery states.** Every ID is `not-started` → `in-progress` → `taught` (explained, first check answered) → `mastered` (passed a rung-3 or rung-4 item, or the skip-test). It may also be `shaky` (missed a check after teaching), `unverified` (claimed done without evidence) or `sliced` (only a named slice taught). Taught and mastered IDs get one-question recalls woven into later relevant sessions at about +1, +3, +7 and +21 sessions; a missed recall sets `shaky` and re-teaches only the gap. The misconception register lives in the ledger; checks probe each entry until two consecutive correct answers retire it.

**0.4.6 Anchoring and suite-wide Prop Lock.** No term, product or control is used in an explanation, example or check unless it is anchored: taught this session, or at least `taught` on the ledger. A named-but-not-taught mention is allowed only when labelled "we'll cover this in X". A check that relies on unanchored terms is invalid: fix the check; don't mark the learner shaky.

**0.4.7 Check questions and exercise pre-flight.** A check tests mechanism or application, asks one thing (split a multi-part check across turns), is answerable from anchored material, has a written expected answer and at least one expected wrong answer in the owning file's keys, is precision-sensitive, and is never answered by the tutor in the same turn. Before issuing any exercise the tutor checks: internal consistency (for example, a CNAME never points at an IP) · every term anchored · exactly one question · the answer derivable from what was taught · any numbers computed. The tutor is precise about mechanisms and says explicitly when unsure. An error found later is corrected openly in the next turn and logged in the errata list of the progress ledger.

**0.4.8 Pacing, checkpoints and session close.** Each module is budgeted at roughly 3–5 concepts per session at full depth; an over-budget module is split into teaching blocks. The budget is a plan, never a reason to compress depth. A problem or checkpoint runs only when all its must-know IDs are at least `taught`, and it introduces at most one new concept. Every session ends by: (1) marking every ID bound to the session taught / sliced / deferred-with-reason / recalled (nothing left unmarked); (2) updating mastery states and the recall schedule; (3) updating the misconception register; (4) adding any errata; (5) emitting a ledger delta block (and a full ledger every 5th session or on request); (6) naming the exact resume point and any open question, verbatim.

**0.4.9 Implementation language: Go.** Go is the suite's language for application code: services, build labs that write a program, and capstones. Python stays the first language of A3, the language of Track D's machine-learning work, and the language of labs already written in Python (the SQL companion's lab kit, the "Python twin" that some labs name). Go is taught by the Go Language Companion: its language core (GO-01…GO-14) is the Go block of A3, and its later modules bind where they are first used. Four rules:

1. **Syntax unlock** — rule 0.4.6 applied to code. A Go construct appears in an explanation, a lab or a check only once the GO module that unlocks it is at least `taught`; before that, the lab runs in Python or waits, and the construct is named only as "we'll cover this in GO-nn". The first use of each construct carries its unlock block: signature → semantics → runtime and memory → contrast with Python, Java, C or JavaScript, naming the bug the other habit causes in Go.
2. **Lab acceptance** — Go lab code is accepted when `gofmt -l` prints nothing, `go vet ./...` is clean, the tests pass (under `go test -race` from GO-19 on; the race detector needs cgo), no error is silently dropped, and every goroutine the code starts has a way to be stopped.
3. **Version honesty** — the baseline release is the one the learner's own module declares. A behaviour is taught as fact only when it has been run on the installed release; anything else carries `(verify)`. The go command downloads modules, and whole toolchains when a module's `go` line is newer than the installed release: name what a step will fetch before running it.
4. **Involved problem** — every GO module ends with one involved problem: a program the learner designs and writes alone, aimed at the module's hardest idea, with its rubric kept in the Go companion's keys and shown only after submission. It is the module's top-rung challenge (rule 0.4.3), so a GO module is `mastered` only when its problem passes its rubric or its skip-test passes (this tightens rule 0.4.5 for GO modules). It is a project across several turns, not a check: hints come only when asked, one at a time, and the tutor never writes the solution.

**0.4.10 Academic depth (undergraduate prerequisites).** The course teaches every undergraduate prerequisite of cloud and system architecture at the depth of a university course, not only at the engineering depth of a first pass. Each Track A module, and each companion, carries an **academic pass**: formal definitions, theorems with their proofs or proof sketches, derivations, named readings, and a numbered problem set whose written keys (an expected answer and at least one expected wrong answer, rule 0.4.7) sit in the owning part's keys. The University and textbook alignment table (main course §0.6) says which university courses and textbooks each pass is aligned with. Four rules:

1. **Two passes, one module.** The engineering pass comes first. The academic pass follows under the same module ID, as its own teaching blocks (rule 0.4.8), never as a separate course. A "first-pass scope" note limits the first pass only.
2. **Proof standard.** A claim presented as a theorem is proved in the session, set as a proof problem, or labelled "stated without proof", naming where the proof is found. Derivations show every step, and every number is computed, not asserted.
3. **Problem sets are exercises.** They climb the ramp (rule 0.4.3). An academic block is `mastered` only when at least one proof problem and one computational problem in it pass against their keys (this tightens rule 0.4.5 for academic blocks).
4. **Readings are named, not linked.** A text is cited by author, title and edition; a course by institution and course name. Editions and course numbers change, so the alignment table carries its check date, and anything not checked carries `(verify)`.

### 0.5 Lab Safety

One rule set for every file; it unifies the cybersecurity companion's rule 10, the SQL companion's rule 10 and the Lab Reality paragraph above.

1. **Hard bans:** no scanning of third parties; no malware; no live DDoS; no credential stuffing against real accounts; fixtures on localhost or disposable projects only; crypto through vetted libraries only.
2. **Money and time:** local first (Docker Postgres, local fixtures). Credit-using services are created for one lab and destroyed the same day, with a budget alert set before the first apply.
3. **Secrets and data:** never put a password, key or real customer data in a query, a prompt or a course file. Lab data is synthetic.
4. **The workplace console is read-only:** look, never create or change.
5. **Every lab carries a Lab Reality tag:** `[free-tier]` · `[credit ~$X]` · `[plan-only]` · `[paper]` · `[local]`.

### 0.6 University and textbook alignment (rule 0.4.10)

This table maps the course onto the undergraduate computer-science core. It uses the knowledge areas of CS2023, the joint ACM, IEEE Computer Society and AAAI curricular guideline, and names reference university courses and textbooks. Course numbers and editions were checked on 2026-09-24 by web search of the universities' course pages and the publishers' listings. A row or item marked `(verify)` was not confirmed that day. Where the course teaches each subject is given by module ID; the academic pass of each module is its "D" teaching blocks (for example A2.D5), and the problem sets are in Appendix P, with keys in Appendix K.

| Subject | CS2023 knowledge area | Reference university courses | Core textbooks | Where it is taught here |
|---|---|---|---|---|
| Computer organization and architecture | Architecture and Organization (AR) | MIT 6.1910 Computation Structures · Berkeley CS 61C Great Ideas of Computer Architecture · CMU 15-213 Introduction to Computer Systems | Patterson and Hennessy, *Computer Organization and Design: RISC-V Edition*, 2nd ed. (2020) · Bryant and O'Hallaron, *Computer Systems: A Programmer's Perspective*, 3rd ed. (2016) | A1 (A1.D1–A1.D8) |
| Discrete mathematics and proof | Mathematical and Statistical Foundations (MSF) | MIT 6.1200 Mathematics for Computer Science · Berkeley CS 70 Discrete Mathematics and Probability Theory · Stanford CS 103 Mathematical Foundations of Computing | Lehman, Leighton and Meyer, *Mathematics for Computer Science* (2018 revision) | A2 (A2.D1–A2.D4); the SQL companion's PQ-01 and PQ-02 own sets, relations and logic |
| Probability and statistics | MSF | Stanford CS 109 Probability for Computer Scientists · Harvard Stat 110 Probability · Berkeley CS 70 (second half) | Blitzstein and Hwang, *Introduction to Probability*, 2nd ed. (2019) | A2 (A2.D5–A2.D7) |
| Queueing and performance modelling | MSF; Parallel and Distributed Computing (PDC) | CMU performance-modelling course taught by Harchol-Balter `(verify)` | Harchol-Balter, *Performance Modeling and Design of Computer Systems: Queueing Theory in Action* (2013) | A2 (A2.D8); the System Design Primer companion's academic pass |
| Linear algebra, calculus and information theory | MSF | MIT 18.06 Linear Algebra `(verify)` | Strang, *Introduction to Linear Algebra*, 6th ed. (2023) | A2 (A2.D9–A2.D11); Track D uses it |
| Algorithms, complexity and computability | Algorithmic Foundations (AL) | MIT 6.1210 Introduction to Algorithms · Stanford CS 161 Design and Analysis of Algorithms `(verify)` · Berkeley CS 170 Efficient Algorithms and Intractable Problems `(verify)` | Cormen, Leiserson, Rivest and Stein, *Introduction to Algorithms*, 4th ed. (2022) · Kleinberg and Tardos, *Algorithm Design* (2005) · Sipser, *Introduction to the Theory of Computation*, 3rd ed. (2012) `(verify)` | A4 (A4.D1–A4.D8) |
| Programming, types and language semantics | Software Development Fundamentals (SDF); Foundations of Programming Languages (FPL) | Berkeley CS 61A and CS 61B `(verify)` | Abelson and Sussman, *Structure and Interpretation of Computer Programs*, 2nd ed. (1996) · Donovan and Kernighan, *The Go Programming Language* (2015) | A3 (A3.D1–A3.D4); the Go Language Companion's academic pass |
| Operating systems | Operating Systems (OS) | MIT 6.1810 Operating System Engineering (xv6 on RISC-V) · Berkeley CS 162 Operating Systems and System Programming · Stanford CS 111 Operating Systems Principles | Arpaci-Dusseau and Arpaci-Dusseau, *Operating Systems: Three Easy Pieces*, version 1.10 (2023) | A6 (A6.D1–A6.D7); B2 (B2.D1) |
| Computer networks | Networking and Communication (NC) | Stanford CS 144 Introduction to Computer Networking · Berkeley CS 168 Introduction to the Internet | Kurose and Ross, *Computer Networking: A Top-Down Approach*, 9th ed. (2025) | A5 (A5.D1–A5.D7) |
| Databases | Data Management (DM) | CMU 15-445/645 Database Systems · Berkeley CS 186 Introduction to Database Systems | Silberschatz, Korth and Sudarshan, *Database System Concepts*, 7th ed. (2019) | A8 (A8.D1); the SQL companion's academic pass |
| Distributed systems | PDC | MIT 6.5840 Distributed Systems | van Steen and Tanenbaum, *Distributed Systems*, 4th ed. (2023) · Kleppmann and Riccomini, *Designing Data-Intensive Applications*, 2nd ed. (2026) | A9 (A9.D1–A9.D9); the System Design Primer companion's academic pass |
| Security and cryptography | Security (SEC) | MIT 6.1600 Foundations of Computer Security · Stanford CS 255 Introduction to Cryptography · Berkeley CS 161 Computer Security | Boneh and Shoup, *A Graduate Course in Applied Cryptography*, version 0.6 (2023) · Anderson, *Security Engineering*, 3rd ed. (2020) `(verify)` | A10 (A10.D1–A10.D5); the Cloud Cybersecurity companion's academic pass |
| Software engineering and architecture | Software Engineering (SE) | MIT 6.1800 Computer Systems Engineering | Bass, Clements and Kazman, *Software Architecture in Practice*, 4th ed. (2021) · Gamma, Helm, Johnson and Vlissides, *Design Patterns* (1994) | A7 (A7.D1–A7.D6); the Design Patterns companion's academic pass |
| Systems engineering, reliability and delivery | Systems Fundamentals (SF); SE | MIT 6.1800 Computer Systems Engineering | Barroso, Hölzle and Ranganathan, *The Datacenter as a Computer*, 3rd ed. (2018) `(verify)` · Beyer, Jones, Petoff and Murphy (eds.), *Site Reliability Engineering* (2016) · Forsgren, Humble and Kim, *Accelerate* (2018) | A11 (A11.D1–A11.D3); B3 (B3.D1); C2 (C2.D1); C6 (C6.D1); C7 (C7.D1) |
| Machine learning | Artificial Intelligence (AI) | Stanford CS 229 Machine Learning `(verify)` | Hastie, Tibshirani and Friedman, *The Elements of Statistical Learning*, 2nd ed. (2009) `(verify)` | D1 (D1.D1); D2 (D2.D1) |
| Society, ethics and the profession | Society, Ethics and the Profession (SEP) | taught inside each university's core `(verify)` | ACM Code of Ethics and Professional Conduct (2018) | A11 (A11.D3); the Cloud Cybersecurity companion's privacy and compliance modules |

> **Note:** out of scope on purpose: CS2023's Graphics and Interactive Techniques (GIT) and Human-Computer Interaction (HCI) areas are not prerequisites of cloud and system architecture. Specialized Platform Development (SPD) is covered only where Tracks B and C need it (mobile and web platforms are named, not taught). The table names reference courses so that the depth of each academic pass can be compared with a known standard; it does not claim equivalence to any university credit.

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
> **Note:** Status as of 2026-09-24: the course is a fresh start, so this sentence is still true.

> **Academic depth (rule 0.4.10) — A1.D, the academic pass, taught after the engineering lines above.** Aligned with MIT 6.1910, Berkeley CS 61C and CMU 15-213 (§0.6).
A1.D1 Number systems, formally: positional notation (a numeral dₖ…d₀ in base b is Σ dᵢ·bⁱ); base conversion by repeated division and why it terminates; two's complement as arithmetic modulo 2ⁿ (one adder serves signed and unsigned values; the range −2ⁿ⁻¹ … 2ⁿ⁻¹−1; signed overflow happens exactly when the carry into the sign bit differs from the carry out of it); sign extension; bit identities (`x & (x−1)` clears the lowest set bit, so a nonzero x is a power of two exactly when `x & (x−1) == 0`)
A1.D2 Boolean algebra and combinational logic: the laws (identity, complement, distributive, De Morgan), sum-of-products and product-of-sums canonical forms, the functional completeness of NAND alone and of NOR alone, Karnaugh-map minimization up to four variables; half and full adders, the n-bit ripple-carry adder with its O(n) delay, carry-lookahead with O(log n) delay; multiplexers and decoders
A1.D3 Sequential logic: the SR latch, the D flip-flop, registers, the clock and the setup and hold constraints; finite-state machines, Moore versus Mealy — the same state-machine idea that TCP's state diagram (A5) and the State pattern (the Design Patterns companion's DP-16) reuse
A1.D4 Instruction set architecture: the RISC-V RV32I base (32 registers, load/store, arithmetic, branches, `jal`/`jalr`); how a C or Go function becomes instructions — the calling convention, the stack frame, caller-saved and callee-saved registers; the fetch–decode–execute cycle and a single-cycle datapath
A1.D5 Performance laws: the iron law (CPU time = instruction count × cycles per instruction × clock period); Amdahl's law (speedup = 1 / ((1 − p) + p/s), bounded by 1/(1 − p) however large s is); the five-stage pipeline, its structural, data and control hazards, forwarding and branch prediction
A1.D6 The memory hierarchy: SRAM, DRAM, flash and disk; temporal and spatial locality; cache organization (direct-mapped, set-associative, fully associative; the tag / index / offset split of an address), write-through versus write-back, the three Cs of misses (compulsory, capacity, conflict); average memory access time (AMAT = hit time + miss rate × miss penalty, applied level by level); virtual memory and the TLB from the hardware side (A6.D3 owns the OS side)
A1.D7 Parallel hardware: multicore, cache coherence (the MSI and MESI protocols) and false sharing; memory consistency models — sequential consistency versus x86-TSO and the weaker RISC-V and ARM models — and why every language therefore defines a memory model (Go's is the Go companion's GO-18); SIMD and GPUs as data parallelism (the matrix multiply of Track D)
A1.D8 Data layout and error detection: endianness and network byte order; alignment and padding; UTF-8 as a variable-length prefix code (why it is ASCII-compatible and self-synchronizing); parity and the cyclic redundancy check (CRC as polynomial division over GF(2)), what each detects and why neither authenticates (cyber CR-05 owns MACs)
> **Readings:** Patterson and Hennessy, RISC-V edition, chapters 1–6; Bryant and O'Hallaron, chapters 2–6. **Problem set:** A1-P1…A1-P7 (Appendix P; keys in Appendix K, after the attempt only).
### A2. Math for Cloud & Machine Learning
- [ ] A2 done
Algebra refresher: functions, exponents, logarithms (logs matter for scaling, entropy, and Big-O)
Linear algebra essentials: vectors, matrices, dot products, matrix multiplication (the literal computation inside every neural network)
Probability & statistics: distributions, mean/variance/std-dev, conditional probability, Bayes' theorem, correlation vs causation
Calculus intuition: derivatives as "rate of change," gradients, why gradient descent trains ML models (no need for proof-level rigor — engineering intuition is the target)
> **Note:** First-pass scope: this intuition pass is the first pass and is complete as written.
> **Note:** learner decision of 2026-09-24: the learner asked for every undergraduate prerequisite at academic depth. The intuition pass above stays the first pass and is still complete as a first pass; the academic pass A2.D1…A2.D11 below adds the rigour, in the same module (rule 0.4.10).
Big-O notation for algorithm/cost reasoning
Floating point: IEEE 754, rounding, decimal vs binary; catastrophic cancellation, compensated (Kahan) summation, stable reformulations (`log1p`, log-sum-exp)

> **Academic depth (rule 0.4.10) — A2.D, the academic pass.** Aligned with MIT 6.1200, Berkeley CS 70, Stanford CS 103 and CS 109, Harvard Stat 110, and MIT 18.06 (§0.6).
A2.D1 Proof: direct proof, proof by contraposition, by contradiction and by cases; mathematical induction (ordinary and strong) and structural induction over lists and trees; the well-ordering principle; invariants as the proof tool for algorithms (A4.D1 reuses them). Propositional and predicate logic are the SQL companion's PQ-02 (recalled, not re-taught)
A2.D2 Relations, functions and counting: the SQL companion's PQ-01 owns sets, relations and bags (recalled); this block adds equivalence relations and partitions, partial orders (A9.D2's happens-before is one), injections, surjections and bijections and what they say about cardinality, the pigeonhole principle, the sum and product rules, permutations and combinations, the binomial theorem, inclusion–exclusion, and linear recurrences solved by the characteristic equation
A2.D3 Number theory for cryptography: divisibility; gcd and the Euclidean algorithm with its O(log n) step bound; Bézout's identity and the extended Euclidean algorithm; modular arithmetic and modular inverses; primes and the fundamental theorem of arithmetic; Fermat's little theorem and Euler's theorem; the Chinese remainder theorem; fast modular exponentiation by repeated squaring; the correctness proof of RSA (used by cyber CR-09) and the discrete-logarithm problem (used by cyber CR-08)
A2.D4 Graph theory: vertices, edges and degrees, the handshake lemma; paths, cycles and connectivity; trees (a tree on n vertices has n − 1 edges and a unique path between any two vertices); bipartite graphs and 2-colouring; directed acyclic graphs and topological order (the prerequisite gate of this course is one); Euler tours. A4.D4 owns the algorithms
A2.D5 Probability, rigorously: sample spaces, events and the axioms; conditional probability and independence; Bayes' theorem derived from the definition; random variables, expectation and the linearity of expectation (which needs no independence), variance and covariance; the Bernoulli, binomial, geometric, Poisson, uniform, exponential and normal distributions with their means and variances; the memoryless property; indicator variables; the birthday bound — for n values drawn uniformly from N, P(some collision) ≈ 1 − e^(−n(n−1)/2N), so collisions become likely near n ≈ √N (why a random 64-bit ID collides after about 2³² draws)
A2.D6 Tail bounds and order statistics: the Markov, Chebyshev and Chernoff bounds (Chernoff stated without proof; the proof is in Blitzstein and Hwang, and in Mathematics for Computer Science); the union bound; the law of large numbers and the central limit theorem (stated and used); the maximum of n independent samples, P(max ≤ t) = F(t)ⁿ — why a request fanned out to 100 servers, each over its own p99 with probability 1%, is slow with probability 1 − 0.99¹⁰⁰ ≈ 63% (the mathematics under the primer's SD-03 and SD-38c)
A2.D7 Statistics for engineers: estimators, bias and variance; the sample mean, its standard error σ/√n and confidence intervals; hypothesis tests and p-values, and their common misreadings; the sample size of an A/B test; quantiles and their estimation from histograms (why averaging per-host p99 values does not give the fleet p99); correlation versus causation and confounders
A2.D8 Queueing theory: arrival and service processes; Little's law L = λW (the primer's SD-03 and SD-28 use it) with a sample-path proof sketch; the M/M/1 queue — utilization ρ = λ/μ, mean number in system ρ/(1 − ρ), mean time in system 1/(μ − λ), so waiting grows without bound as ρ → 1; M/M/k and why one shared queue for k servers beats k separate queues; the effect of service-time variability (the Pollaczek–Khinchine formula for M/G/1, stated); utilization targets in capacity planning
A2.D9 Linear algebra, rigorously: vector spaces, span, linear independence, basis and dimension; matrices as linear maps; rank and the rank–nullity theorem; solving Ax = b by Gaussian elimination and LU factorization; determinants; orthogonality, projections and least squares (the normal equations AᵀAx = Aᵀb are linear regression, D1); eigenvalues and eigenvectors; the singular value decomposition and principal component analysis (D1); the O(n³) cost of naive matrix multiplication and why it parallelizes
A2.D10 Calculus and optimization, rigorously: limits and continuity; the derivative as a limit; the chain rule (all of backpropagation, D2); partial derivatives and the gradient; the first-order Taylor approximation and why a small enough gradient step decreases a smooth function; convexity (for a convex function every local minimum is global); the integral as accumulated area (probability densities, A2.D5)
A2.D11 Information theory: entropy H(X) = −Σ p·log₂ p; cross-entropy and KL divergence (the loss functions of D1 and D2); Shannon's source-coding bound and Huffman codes, which come within one bit per symbol of it; why compressed or well-encrypted data looks uniformly random (the Cloud Cybersecurity companion's CR-02); channel capacity named only
> **Readings:** Lehman, Leighton and Meyer, parts I–IV; Blitzstein and Hwang, chapters 1–10; Strang, chapters 1–7; Harchol-Balter, chapters 1–6 and 13–14. **Problem set:** A2-P1…A2-P12 (Appendix P; keys in Appendix K).

> **Note:** A2 binds more than twenty suite concepts once its academic pass is counted (rule 0.4.8), so it is taught as ordered teaching blocks. These are sessions, not new modules; the module ID stays A2. A2.1 algebra, logarithms and Big-O (+ primer SD-00 [the back-of-the-envelope method], SD-02 [proportional-scaling arithmetic]) · A2.2 floating point and number formats (+ SQL PQ-03, DD-03 [money, units, time], PQ-08 [page and row arithmetic]; Go companion GO-03) · A2.3 linear algebra and calculus intuition · A2.4 probability and statistics intuition (+ primer SD-03 [percentiles; Little's law sizing], SD-07 [availability math], SD-28 [Little's law]) · A2.5 sets, relations and logic (+ SQL PQ-01, PQ-02, RT-01) with A2.D1 proof and A2.D2 counting · A2.D3 number theory · A2.D4 graphs · A2.D5–A2.D7 probability, tails and statistics · A2.D8 queueing · A2.D9–A2.D10 linear algebra and calculus, rigorously · A2.D11 information theory · A2.C checkpoints.
### A3. Programming Foundations
- [ ] A3 done
Python: variables, control flow, functions, data structures (list/dict/set/tuple), OOP basics, virtual environments, package management (pip)
Bash/shell scripting: variables, loops, conditionals, pipes, redirection, exit codes — essential for CI/CD scripts and automation everywhere
Working with APIs from code: HTTP clients, JSON parsing, SDKs (google-cloud-*, boto3, azure-sdk)
Git fundamentals (deep dive lives in A11)
Go, the implementation language of the suite's labs and services: the Go companion's GO-01…GO-14, after the Python block, in four teaching blocks — A3.G1 toolchain, packages, types and control flow · A3.G2 slices and maps, functions, errors, strings · A3.G3 pointers and memory, structs and methods, interfaces, generics · A3.G4 I/O, JSON, command-line programs and logging — every construct contrasted with Python (rule 0.4.9)

> **Note:** A3 binds more than twenty suite concepts (rule 0.4.8), so it is taught as ordered teaching blocks. These are sessions, not new modules; the module ID stays A3. A3.P1 Python (+ primer SD-21 [dict as a hash table], SD-27 [cache-aside code]) · A3.P2 Bash, APIs from code and Git (+ primer SD-32…SD-34 [RPC and REST calls in Python and curl]; SQL PQ-04 files and encodings, PQ-05 `psql` and a Docker Postgres, PQ-06 DB-API parameter binding) · A3.G1…A3.G4 the Go blocks above (GO-01…GO-14) · A3.C checkpoints.

> **Academic depth (rule 0.4.10) — A3.D, the academic pass, after A3.G4 and before A3.C.** Aligned with Berkeley CS 61A and CS 61B (§0.6); the Go Language Companion's academic pass owns the theory behind Go.
A3.D1 Semantics of programs: values versus references, mutability and aliasing, scope and closures (lexical environments), evaluation order; Python's call by sharing versus Go's call by value with explicit pointers — the model behind every "why did my list change" bug
A3.D2 Recursion and its correctness: base case and a decreasing measure; proving a recursive function correct and terminating by induction (A2.D1); recursion versus iteration, tail calls, and the call stack's depth limit
A3.D3 Types: static versus dynamic checking, strong versus weak typing, nominal versus structural typing (Go's interfaces are structural, GO-11), parametric polymorphism (generics, GO-12) versus subtype polymorphism (the Design Patterns companion's F-04); type soundness as "well-typed programs do not go wrong" (progress and preservation, stated without proof; the proof is in Pierce, *Types and Programming Languages* (2002))
A3.D4 Specification and testing: preconditions, postconditions and loop invariants; Hoare triples {P} C {Q} and the assignment rule, stated; assertions; example-based versus property-based tests; why 100% line coverage proves nothing about correctness
> **Problem set:** A3-P1…A3-P4 (Appendix P; keys in Appendix K).
### A4. Data Structures & Algorithms (engineering-practical depth, not competitive-programming depth)
- [ ] A4 done
Arrays, linked lists, hash maps, stacks/queues, trees, graphs
Big-O in practice: why a hash lookup beats a linear scan, why indexes matter in databases
Sorting/searching intuition (enough to reason about algorithmic choices, not to implement red-black trees from memory)
Probabilistic structures: Bloom filters with their false-positive rate (1 − e^(−kn/m))^k, count-min sketch, HyperLogLog
> **Note:** First-pass scope: A4 stays at engineering-practical depth.
> **Note:** learner decision of 2026-09-24: the learner asked for every undergraduate prerequisite at academic depth. The engineering pass above stays the first pass; A4.D1…A4.D8 below are the university-algorithms pass, in the same module (rule 0.4.10). The first-pass note limits the first pass only.

> **Academic depth (rule 0.4.10) — A4.D, the academic pass.** Aligned with MIT 6.1210, Stanford CS 161 and Berkeley CS 170 (§0.6).
A4.D1 Correctness and analysis: loop invariants (initialization, maintenance, termination) proved for insertion sort and binary search; the RAM model of computation; O, Ω, Θ and o defined with quantifiers and proved from the definitions; worst-case, average-case and amortized cost
A4.D2 Recurrences and divide and conquer: merge sort and T(n) = 2T(n/2) + Θ(n); solving recurrences by recursion tree, by substitution (induction) and by the master theorem; Karatsuba multiplication; the Ω(n log n) lower bound for comparison sorting (the decision-tree proof) and why counting sort and radix sort escape it
A4.D3 Data structures with proofs: dynamic arrays and amortized O(1) append (aggregate, accounting and potential methods); binary heaps and heapsort; hash tables with chaining — expected O(1 + α) per operation under simple uniform hashing, universal hashing, open addressing and the load factor; binary search trees and one balanced tree (red-black or AVL) with its O(log n) height proof; B-trees as the disk-oriented balanced tree (the SQL companion's CS-02 and DB-6 own the engine side); union–find with union by rank and path compression (near-constant amortized cost, stated)
A4.D4 Graph algorithms: adjacency lists versus matrices and their costs; breadth-first search and its shortest-path proof for unweighted graphs; depth-first search, edge classification, topological sort and cycle detection; strongly connected components; Dijkstra's algorithm with its correctness proof and its failure on negative edges; Bellman–Ford and negative cycles (the distance-vector routing of A5.D4); minimum spanning trees by the cut property (Kruskal and Prim); maximum flow and minimum cut (Ford–Fulkerson; the max-flow min-cut theorem, stated)
A4.D5 Greedy algorithms and dynamic programming: the greedy-choice property and exchange arguments (interval scheduling; Huffman coding from A2.D11); dynamic programming as optimal substructure plus overlapping subproblems (edit distance, 0/1 knapsack, longest common subsequence, shortest paths in a DAG); the SQL planner's join-order search is dynamic programming (the SQL companion's CS-08)
A4.D6 Randomized algorithms and probabilistic data structures: quicksort's expected O(n log n) by indicator variables; randomized selection; the Bloom filter's false-positive rate derived from A2.D5, the count-min sketch's ε–δ guarantee, HyperLogLog's standard error of about 1.04/√m (stated); consistent hashing's expected 1/N key movement derived (the primer's SD-38a); reservoir sampling
A4.D7 Computability and complexity: decision problems, P and NP, polynomial-time reductions and NP-completeness (SAT, 3-SAT, vertex cover, subset sum, bin packing); what "NP-hard" means to an engineer (use approximations or heuristics — first-fit bin packing is the shape of the Kubernetes scheduler, C2.D1); undecidability of the halting problem by diagonalization; finite automata and regular expressions (the regex engines of C3 and GO-08) and context-free grammars (parsers; the Design Patterns companion's DP-23)
A4.D8 Algorithms at scale: the external-memory model (cost counted in block transfers; the SQL companion's CS-03 owns the engine's sort and join costs); the streaming model; parallel algorithms by work and span (Brent's bound, stated); MapReduce as a parallel model (A9 owns its distributed side)
> **Readings:** Cormen, Leiserson, Rivest and Stein, 4th ed., parts I–VI and chapter 34; Kleinberg and Tardos, chapters 4–8; Sipser, chapters 1–5 and 7. **Problem set:** A4-P1…A4-P9 (Appendix P; keys in Appendix K).

> **Note:** A4 binds more than twenty suite concepts once its academic pass is counted (rule 0.4.8), so it is taught as ordered teaching blocks. These are sessions, not new modules; the module ID stays A4. A4.1 arrays, lists, hash maps, stacks and queues (+ primer SD-21 [hash-table slice]; SQL PQ-07; Go companion GO-05) · A4.2 trees, graphs and search (+ primer SD-19 [B-tree index slice], SD-24 [graph representation slice]; SQL CS-02, DB-6) · A4.3 sorting, searching and probabilistic structures (+ primer SD-38 [consistent-hash ring slice]) · A4.4 the Go renderings, once the Go companion reaches them (GO-12, GO-27) · A4.D1–A4.D3 analysis and data structures with proofs · A4.D4 graph algorithms · A4.D5–A4.D6 greedy, dynamic programming and randomized algorithms · A4.D7–A4.D8 complexity, computability and scale · A4.C checkpoints (primer O01, O02, O07).
### A5. Computer Networking (heavily tested across every cloud architect/network/security cert)
- [ ] A5 done
The OSI model and TCP/IP model — what actually lives at each layer
IP addressing: IPv4 structure, subnetting and CIDR notation (binary math from A1 comes back here), IPv6 basics
Routing fundamentals: how packets find their way, default gateways, routing tables
TCP vs UDP: three-way handshake, reliability vs speed trade-offs
DNS: how domain resolution works, record types (A, AAAA, CNAME, MX, TXT, NS)
HTTP/HTTPS: request/response cycle, methods, status codes, headers, cookies
TLS/SSL: the handshake, certificates, certificate authorities (ties into A10 security)
> **Note:** TLS split: A5 teaches the handshake mechanics, certificates and CAs, plus a minimal public-key intuition bridge (what a key pair does, what a signature proves, why DH gives a shared secret). A10 formalizes the cryptographic primitives underneath and recalls A5 in one line.
NAT, firewalls, proxies vs reverse proxies (sets up NGINX in Track C)
Load balancing concepts: L4 vs L7, algorithms (round robin, least connections, consistent hashing)
VPNs and private connectivity concepts

> **Note:** A5 binds more than twenty suite concepts (rule 0.4.8), so it is taught as ordered teaching blocks. These are sessions, not new modules; the module ID stays A5. A5.1 layers, addressing, routing, TCP and UDP (+ primer SD-30, SD-31, SD-01 [clones + single-box ceiling], SD-02 [performance vs scalability]) · A5.2 DNS (+ primer SD-08; cyber DOS-02, NT-03, NT-04) · A5.3 HTTP and HTTP-layer caching (+ primer SD-29, SD-09, SD-26 [HTTP-layer caching]; cyber PQ-S-04) · A5.4 TLS mechanics (+ cyber CR-11, CR-12, NT-08; primer SD-35 [TLS in transit]) · A5.5 NAT, firewalls and proxies (+ primer SD-11; cyber NT-01, NT-02, NT-07) · A5.6 load balancing (+ primer SD-10; cyber DOS-01) · A5.7 VPNs and private connectivity (+ cyber NT-05) · A5.8 the Go renderings, once the Go companion reaches them (GO-21 `net/http`, GO-28 cookies, GO-17 deadlines, GO-23 gRPC) · A5.9 checkpoints.

> **Academic depth (rule 0.4.10) — A5.D, the academic pass, after A5.7 and before the A5.9 checkpoints.** Aligned with Stanford CS 144 and Berkeley CS 168 (§0.6).
A5.D1 Architecture principles: layering and encapsulation; the end-to-end argument (Saltzer, Reed and Clark, 1984); packet versus circuit switching and statistical multiplexing; the four delays — transmission L/R, propagation d/s, queueing (A2.D8) and processing; the bandwidth–delay product as the data "in flight"
A5.D2 Reliable transfer, formally: building a reliable channel from checksums, acknowledgements, sequence numbers and timeouts; stop-and-wait utilization U = (L/R) / (RTT + L/R); Go-Back-N versus selective repeat and the window-size limit for selective repeat (at most half the sequence space); TCP's cumulative ACKs, RTT estimation (exponentially weighted moving averages of the sample RTT and its deviation; RTO = estimated RTT + 4 × deviation), fast retransmit, and flow control by the receive window
A5.D3 Congestion control: additive-increase multiplicative-decrease and why it converges toward fairness (the Chiu–Jain argument); slow start; Reno, CUBIC and the model-based BBR; the Mathis approximation, throughput ≈ (MSS/RTT) × 1.22/√p for loss rate p (stated); bufferbloat; explicit congestion notification
A5.D4 Routing algorithms: link state (Dijkstra; OSPF) versus distance vector (Bellman–Ford; RIP; count-to-infinity and poisoned reverse); hierarchical routing and autonomous systems; BGP as path-vector policy routing (eBGP and iBGP, route selection, slow convergence, and why a false route announcement can hijack traffic — the Cloud Cybersecurity companion's network modules own the attack); longest-prefix match in forwarding tables, implemented with tries
A5.D5 The link layer and data-centre networks: Ethernet framing, self-learning switches, ARP and VLANs; Clos and fat-tree data-centre topologies, equal-cost multipath (ECMP) and oversubscription — the fabric every cloud VPC runs on (Google's Jupiter fabric, described in its 2015 paper)
A5.D6 Modern transport and the socket interface: QUIC over UDP (independent streams without head-of-line blocking, combined transport and TLS 1.3 handshake, 0-RTT resumption and its replay risk, connection migration by connection ID); HTTP/2 multiplexing versus HTTP/3; the socket API (`socket`, `bind`, `listen`, `accept`, `connect`) as the operating system's interface to all of it (the Go companion's GO-21 renders it)
A5.D7 Naming and measurement: DNS as a distributed, hierarchical, cached database whose consistency is bounded by TTLs (A9's eventual consistency); anycast; measurement as experiment — `ping`, `traceroute` (TTL expiry), `dig +trace`, and packet capture with `tcpdump` on your own host only (§0.5)
> **Readings:** Kurose and Ross, 9th ed., chapters 1–6; Saltzer, Reed and Clark, "End-to-End Arguments in System Design" (1984). **Problem set:** A5-P1…A5-P7 (Appendix P; keys in Appendix K).
### A6. Linux & Operating Systems
- [ ] A6 done
Processes, threads, memory management, the filesystem hierarchy
Linux shell essentials: navigation, permissions (chmod/chown), package managers, systemd/services
Containers vs VMs at the OS level: namespaces and cgroups (sets up Docker)
SSH and remote access
Observing a live system: `/proc`, `ps`, `ss`, the OOM killer and cgroup memory limits (why a Cloud Run instance is killed), predicted before they are observed, on your own VM only

> **Academic depth (rule 0.4.10) — A6.D, the academic pass.** Aligned with MIT 6.1810 (xv6 on RISC-V), Berkeley CS 162 and Stanford CS 111 (§0.6).
A6.D1 The process abstraction: user and kernel mode, system calls, traps and interrupts; `fork`, `exec` and `wait`; process states and the cost of a context switch; threads versus processes; the address-space layout (code, data, heap, stack)
A6.D2 CPU scheduling: FIFO, shortest-job-first and shortest-time-to-completion-first (optimal for mean turnaround time, by an exchange argument), round robin and response time, the multi-level feedback queue, proportional share (lottery and stride scheduling), and Linux's fair schedulers (CFS, replaced by EEVDF in Linux 6.6); cgroup CPU shares and quotas — the throttling behind Kubernetes CPU limits (C2)
A6.D3 Virtual memory: address translation, paging and multi-level page tables (with the page-table size arithmetic), the TLB and its reach, page faults and demand paging, copy-on-write (why `fork` is cheap), replacement policies (optimal, LRU, CLOCK — the same clock sweep as the SQL companion's DB-5), thrashing and working sets, memory-mapped files; the OOM killer (recalled)
A6.D4 Concurrency: race conditions and critical sections; mutual exclusion built from atomic instructions (test-and-set, compare-and-swap); spinlocks versus blocking locks; condition variables and the producer–consumer problem; semaphores; readers–writers locks; the four Coffman conditions for deadlock and prevention by a global lock order; livelock and priority inversion
A6.D5 Persistence: the device interface and I/O scheduling; the file-system abstraction (inodes, directories, hard and symbolic links, file descriptors); the on-disk layout of a very simple file system; crash consistency — `fsck` versus journaling (data versus metadata journaling, ordered mode) versus copy-on-write file systems; what `fsync` promises and what a database relies on (the SQL companion's CS-06); flash translation layers and write amplification; RAID 0, 1 and 5 and their failure arithmetic
A6.D6 Isolation at the OS level: what each Linux namespace isolates and what cgroups limit, seccomp filters and capabilities; why a container shares the kernel and is therefore a weaker boundary than a VM (the Cloud Cybersecurity companion's CK-01 owns the attacks; B2.D1 owns hypervisors)
A6.D7 I/O models and performance: the cost of system calls and copies; thread-per-connection versus event-driven I/O (`epoll`, `io_uring`) and the C10k problem; zero-copy transfer (`sendfile`) — why NGINX (C3) and Go's network poller (the Go companion's GO-15) are built as they are
> **Readings:** Arpaci-Dusseau and Arpaci-Dusseau, *Operating Systems: Three Easy Pieces*, version 1.10 — virtualization, concurrency and persistence parts; the xv6 book used by MIT 6.1810. **Problem set:** A6-P1…A6-P7 (Appendix P; keys in Appendix K).

> **Note:** A6 binds more than twenty suite concepts once its academic pass is counted (rule 0.4.8), so it is taught as ordered teaching blocks. These are sessions, not new modules; the module ID stays A6. A6.1 processes, threads, memory and the filesystem (+ primer SD-01 [clones; the single-box ceiling], SD-19 [profiling tools]; Go companion GO-09, GO-15) · A6.2 the shell, permissions, packages and services (+ SQL PQ-04, PQ-05, PQ-06; Go companion GO-14; cyber WA-10) · A6.3 namespaces, cgroups, SSH and observing a live system (+ primer SD-30 [connection and file-descriptor limits]; cyber DOS-06) · A6.D1–A6.D3 processes, scheduling and virtual memory · A6.D4 concurrency · A6.D5 persistence · A6.D6–A6.D7 isolation and I/O models · A6.C checkpoints.
### A7. Software Architecture & APIs
- [ ] A7 done
Client-server model, monoliths vs microservices, trade-offs of each
REST principles, gRPC, GraphQL (awareness-level)
Synchronous vs asynchronous communication; message queues and event-driven architecture (sets up Pub/Sub, SQS/SNS, Service Bus)
API authentication patterns: API keys, OAuth 2.0, JWTs, service accounts
Architecture documentation: views, C4, ADRs ("I pick X because Y, I accept Z"), the HLD/LLD contract and NFR tables

> **Note:** A7 binds several dozen suite concepts, so it is taught as ordered teaching blocks. These are sessions, not new modules; the module ID stays A7. A7.1 client-server and API styles (+ primer SD-12, SD-32…SD-34) · A7.2 async and queues (+ primer SD-28; SQL SL-10 idempotent writes) · A7.3 OOP foundations + SOLID (patterns F-01…F-04, PR-01…PR-05) · A7.4 GRASP + creational patterns (PR-06…PR-14, DP-01…DP-05) · A7.5 structural patterns (DP-06…DP-12) · A7.6 behavioral patterns (DP-13…DP-23) · A7.7 architecture styles + DDD (ARCH-01…ARCH-08, anti-patterns AP-01…AP-10; primer SD-16 [functional partitioning as service design]; SQL OD-09 data access through repositories) · A7.8 API authentication/authorization + attacks (cyber AU-05…AU-08, AU-11…AU-13, CR-10, TH-04, CL-08) · A7.9 abuse and rate limits (cyber AB-01…AB-08) · A7.10 architecture documentation (views, C4, ADRs, HLD/LLD, NFR tables; SQL DD-01, RT-06, DD-08, DD-10, DD-12 as schema ADRs) · A7.11 the Go renderings, once the Go companion reaches them (GO-10, GO-11, GO-21, GO-22, GO-23, GO-28, GO-29) · A7.12 checkpoints. A3, A5, A8, A9 and A10 are split the same way (their notes).

> **Academic depth (rule 0.4.10) — A7.D, the academic pass, after A7.10 and before A7.11.** Aligned with MIT 6.1800 and the software-architecture texts in §0.6.
A7.D1 Modularity: information hiding (Parnas, 1972 — decompose by the design decisions likely to change, not by processing steps); coupling and cohesion as measurable properties (afferent and efferent coupling, instability I = Ce/(Ca + Ce), the stable-dependencies principle); interfaces as contracts; Conway's law
A7.D2 Design by contract and substitutability: preconditions, postconditions and class invariants (Meyer); behavioural subtyping by the Liskov–Wing rule (1994) — a subtype may not strengthen preconditions or weaken postconditions, must preserve invariants, and must respect the history constraint — the formal basis of the Design Patterns companion's PR-03
A7.D3 Specification and model checking: state machines as specifications; safety versus liveness properties; TLA+ as used at Amazon Web Services to find design bugs before code (Newcombe et al., 2015); model-checking a small protocol (a lock, or two-phase commit) by exhaustive state enumeration
A7.D4 Quality attributes and architecture evaluation: quality-attribute scenarios (source, stimulus, artifact, environment, response, response measure); tactics for availability, performance, modifiability, security and testability; the Architecture Tradeoff Analysis Method (utility tree, sensitivity and trade-off points, risks) — how the ADRs of A7.10 are evaluated
A7.D5 API design theory: REST as an architectural style defined by constraints (Fielding, 2000: client–server, stateless, cacheable, uniform interface, layered system, optional code on demand); safety and idempotency of methods as algebraic properties (f(f(x)) = f(x)); compatibility rules for evolving an API and a schema (protobuf field-number rules); Hyrum's law
A7.D6 Software quality and measurement: testing theory (test oracles, equivalence partitioning, boundary values, mutation testing), static analysis, the evidence on code review; estimation error; technical debt as a metaphor and its limits
> **Readings:** Bass, Clements and Kazman, 4th ed., parts I–III; Parnas, "On the Criteria To Be Used in Decomposing Systems into Modules" (1972); Liskov and Wing, "A Behavioral Notion of Subtyping" (1994); Fielding's dissertation, chapter 5 (2000). **Problem set:** A7-P1…A7-P5 (Appendix P; keys in Appendix K). The Design Patterns companion's academic pass continues this block for patterns.
### A8. Databases & Data Modeling
- [ ] A8 done
Relational model, SQL fundamentals (SELECT/JOIN/GROUP BY, normalization)
ACID properties and transactions
NoSQL families: key-value, document, wide-column, graph — and when each fits
CAP theorem and its real engineering trade-offs
Data warehousing basics: OLTP vs OLAP, star schemas
Engine slices DB-1…DB-10 (bag relations, slotted page, buffer clock sweep, B-tree + inverted index, iterators + spill, histograms, MVCC visibility + deadlock detection, mini-WAL): owned and taught by the SQL companion (§4.0) inside the A8 sessions

> **Note:** A8 binds more than twenty suite concepts (rule 0.4.8), so it is taught as ordered teaching blocks. These are sessions, not new modules; the module ID stays A8. A8.1 relational model, keys, dependencies and normal forms; DDL, evaluation order, NULL (SQL RT-01, RT-04, RT-05, RT-07, SL-01…SL-03, DD-12; slice DB-2; primer SD-13) · A8.2 relational algebra and the query language (SQL RT-02, RT-03, RT-08, SL-04…SL-09, SL-14; slices DB-1, DB-3) · A8.3 transactions and isolation (SQL SL-10, CS-05; slice DB-9; primer SD-04 [the CAP statement], SD-05 [strong vs eventual as the C in CAP]) · A8.4 storage, indexes and the executor (SQL CS-01…CS-04, CS-08, OD-01; slices DB-4…DB-8; primer SD-19) · A8.5 recovery and replication in the engine (SQL CS-06, CS-07; slice DB-10) · A8.6 data modeling (SQL RT-06, DD-01…DD-08, DD-11, OD-08, SL-11, SL-12; primer SD-16 [schema view], SD-18 [denormalization as the inverse of normalization]; cyber PV-03, CM-02) · A8.7 NoSQL families and the choice (primer SD-20…SD-25, SD-26; SQL AN-06) · A8.8 warehousing: OLTP vs OLAP (SQL AN-01) · A8.9 attacks on the data layer (cyber WA-05, AB-06, AB-07) · A8.10 the Go renderings, once the Go companion reaches them (GO-22, GO-29) · A8.11 checkpoints.

> **Academic depth (rule 0.4.10) — A8.D.** Aligned with CMU 15-445/645 and Berkeley CS 186 (§0.6).
A8.D1 Database theory at university depth is the SQL companion's academic pass (its one owner), taught as the proof layer of the cards in A8.1–A8.5: Armstrong's axioms with soundness and completeness, attribute closure and minimal covers, the lossless-join and dependency-preservation tests, BCNF decomposition and 3NF synthesis, relational algebra versus safe calculus (Codd's theorem), the conflict-serializability theorem and the two-phase-locking theorem, ARIES recovery, the I/O cost formulas, and dynamic-programming join ordering
### A9. Distributed Systems Theory
- [ ] A9 done
Consistency models (strong, eventual), replication strategies
Partitioning/sharding, consensus (Raft/Paxos at a conceptual level — Spanner, etcd, and Kubernetes all depend on this)
Availability vs durability, failure modes, idempotency
Why "the network is reliable" is the first fallacy of distributed computing (and the other seven)

> **Note:** A9 binds more than twenty suite concepts (rule 0.4.8), so it is taught as ordered teaching blocks. These are sessions, not new modules; the module ID stays A9. A9.1 consistency models and CAP in full (primer SD-04 [formal limits + PACELC], SD-05) · A9.2 replication, availability and durability (primer SD-06, SD-07, SD-14, SD-15; SQL CS-06) · A9.3 partitioning and sharding (primer SD-16, SD-17, SD-18, SD-25, SD-38; SQL DD-10, DD-13, AN-05) · A9.4 consensus, distributed transactions and failure design (SQL CS-07, SL-10; patterns ARCH-09…ARCH-12) · A9.5 caching at scale (primer SD-27; cyber DOS-08) · A9.6 scale primitives with SQL evidence (SQL OD-03, OD-09, DD-11; multi-tenancy: SQL DD-09, SL-13, cyber CL-06; cyber AB-05) · A9.7 the database theory tier, taught with the A8 sessions (SQL RT-02, RT-03, RT-04, RT-08, CS-02, CS-05, CS-08) · A9.8 the fallacies and distributed threats (cyber TH-06); the papers (primer SD-39) · A9.9 the Go renderings, once the Go companion reaches them (GO-15…GO-19, GO-29) · A9.10 checkpoints.

> **Academic depth (rule 0.4.10) — A9.D, the academic pass, after A9.8 and before A9.9.** Aligned with MIT 6.5840 Distributed Systems (§0.6).
A9.D1 System models: synchronous, partially synchronous and asynchronous timing; crash-stop, crash-recovery, omission and Byzantine failures; fair-loss versus reliable links; failure detectors (perfect versus eventually perfect) — why "timed out" means only "suspected"
A9.D2 Time and order: happens-before (Lamport, 1978) as a partial order (A2.D2); Lamport clocks (if a → b then C(a) < C(b), not conversely); vector clocks capture causality exactly (proof sketch); physical clock synchronization (NTP) and bounded uncertainty (Spanner's TrueTime interval and commit wait); consistent snapshots (Chandy–Lamport)
A9.D3 Consistency, formally: linearizability (Herlihy and Wing, 1990) versus sequential, causal and eventual consistency; serializability versus strict serializability; session guarantees (read-your-writes, monotonic reads); the CAP theorem as proved by Gilbert and Lynch (2002), with the two-node proof sketch, and PACELC; quorums — R + W > N forces every read quorum to meet every write quorum (proof by pigeonhole), and why sloppy quorums give that up
A9.D4 Impossibility results: the Two Generals problem (no deterministic agreement over a lossy channel); the FLP result (Fischer, Lynch and Paterson, 1985) — no deterministic protocol solves consensus in an asynchronous system if even one process may crash — with the bivalence intuition; how real systems escape it (partial synchrony, randomization, failure detectors)
A9.D5 Consensus: the problem (agreement, validity, termination); single-decree Paxos (prepare/promise, accept/accepted; why majority quorums make a chosen value stick) and Multi-Paxos; Raft (terms and leader election, log replication, the log-matching and leader-completeness properties, the commit rule, membership change); state-machine replication as the use; Chubby, ZooKeeper and etcd as products built on it
A9.D6 Byzantine fault tolerance: why tolerating f Byzantine faults needs n ≥ 3f + 1 replicas (the three-node argument); the three phases of PBFT, named; why cloud control planes use crash-fault consensus instead
A9.D7 Replication and convergence: primary–backup and chain replication; leaderless, Dynamo-style replication with read repair, hinted handoff and Merkle-tree anti-entropy; CRDTs — a state-based CRDT's merge is commutative, associative and idempotent (a join-semilattice), which is why replicas converge (G-Counter, PN-Counter, OR-Set); operational transformation, named (the primer's Q04)
A9.D8 Distributed transactions: two-phase commit and its blocking window when the coordinator fails after "prepared" (shown by scenario); why three-phase commit fails under partitions; Sagas with compensations (the Design Patterns companion's ARCH-11 owns the shape); two-phase commit over Paxos groups in Spanner; exactly-once delivery as effectively-once (idempotence plus deduplication)
A9.D9 Computation, the tail and verification: MapReduce and dataflow, and lineage-based recovery; the tail at scale (Dean and Barroso, 2013) — hedged and tied requests analysed with A2.D6's order statistics; testing distributed systems — fault injection in the Jepsen style and deterministic simulation; the MIT 6.5840 lab sequence (MapReduce, a linearizable key/value server, Raft, a fault-tolerant key/value service on Raft, a sharded key/value service) as the A9 build path in Go, after the Go companion's GO-15…GO-19
> **Readings:** van Steen and Tanenbaum, 4th ed., chapters 5–8; Kleppmann and Riccomini, 2nd ed., the distributed-data part; Lamport, "Time, Clocks, and the Ordering of Events in a Distributed System" (1978); Fischer, Lynch and Paterson (1985); Gilbert and Lynch (2002); Ongaro and Ousterhout, "In Search of an Understandable Consensus Algorithm" (2014). **Problem set:** A9-P1…A9-P9 (Appendix P; keys in Appendix K). The primer's academic pass adds the design-level derivations.
### A10. Security & Cryptography Fundamentals
- [ ] A10 done
Symmetric vs asymmetric encryption, hashing vs encryption, digital signatures
The TLS handshake in detail, PKI and certificate chains
> **Note:** A10 formalizes what A5 taught at mechanism level (see the A5 note); it does not re-teach the handshake.
Authentication vs authorization; identity federation, SSO, MFA
Common attack classes: injection, XSS, CSRF, DDoS, privilege escalation
Principle of least privilege, defense in depth, zero trust — the conceptual spine of every cloud IAM system

> **Note:** A10 binds more than twenty suite concepts (rule 0.4.8), so it is taught as ordered teaching blocks. These are sessions, not new modules; the module ID stays A10. A10.1 principles, economics and threat modeling (cyber PQ-S-02, PQ-S-05, PQ-S-06, TH-01…TH-04) · A10.2 cryptographic primitives (cyber PQ-S-01, CR-01…CR-10, CR-13, CR-16, CR-17, CR-19, SC-01) · A10.3 TLS and PKI, formally (cyber CR-11, CR-12; primer SD-35) · A10.4 authentication, sessions, federation and MFA (cyber AU-01…AU-13) · A10.5 web attack classes (cyber PQ-S-04, WA-01…WA-08, WA-10, WA-12; SQL SL-13) · A10.6 denial of service and resource exhaustion (cyber DOS-03, DOS-05, DOS-06) · A10.7 least privilege, defense in depth, zero trust (cyber CL-05, CK-04, PV-05) · A10.8 the Go renderings, once the Go companion reaches them (GO-07, GO-13, GO-21, GO-25, GO-26, GO-28) · A10.9 checkpoints.

> **Academic depth (rule 0.4.10) — A10.D, the academic pass, after A10.7 and before A10.8.** Aligned with MIT 6.1600, Stanford CS 255 and Berkeley CS 161 (§0.6).
A10.D1 Security design principles: Saltzer and Schroeder's eight principles (1975 — economy of mechanism, fail-safe defaults, complete mediation, open design, separation of privilege, least privilege, least common mechanism, psychological acceptability); the reference monitor (tamper-proof, always invoked, small enough to verify) and the trusted computing base
A10.D2 Access-control models: the access-control matrix, ACLs versus capabilities; discretionary versus mandatory access control; Bell–LaPadula for confidentiality (no read up, no write down) and Biba for integrity (its dual); Clark–Wilson (well-formed transactions, separation of duty); the NIST RBAC model (users, roles, permissions, sessions, role hierarchies) and ABAC — the theory under B5's IAM
A10.D3 Cryptography, formally, is the Cloud Cybersecurity companion's academic pass (its owner): security definitions as games (IND-CPA, IND-CCA, EUF-CMA), negligible functions, reductions, and the random-oracle model; it runs inside A10.2
A10.D4 Protocol reasoning: the Dolev–Yao attacker; nonces and freshness; classic protocol failures (replay, reflection, Lowe's 1995 attack on the Needham–Schroeder public-key protocol); formal protocol verification, named (Tamarin, ProVerif), and TLS 1.3 as a protocol designed together with formal analysis
A10.D5 Systems security: memory-safety bugs (buffer overflows, use-after-free) and their mitigations (stack canaries, ASLR, non-executable memory, control-flow integrity); why a memory-safe language such as Go removes a class of them; privilege separation and sandboxing (the OpenSSH design); hardware side channels (the Cloud Cybersecurity companion's SC-01…SC-03 own them)
> **Readings:** Saltzer and Schroeder, "The Protection of Information in Computer Systems" (1975); Anderson, *Security Engineering*, 3rd ed., chapters 2–6; Boneh and Shoup, version 0.6, part I. **Problem set:** A10-P1…A10-P5 (Appendix P; keys in Appendix K).



### A11. Software Delivery & Version Control
- [ ] A11 done
Git deep dive: branches, merges, rebases, conflict resolution, tagging
SDLC models, Agile/Scrum basics
Code review culture, trunk-based development vs GitFlow (relevant to CI/CD design choices later)

> **Academic depth (rule 0.4.10) — A11.D.**
A11.D1 Git's data model: content-addressed objects (blob, tree, commit, tag) named by their hash; the commit graph as a DAG and a Merkle structure (why one commit hash authenticates its whole history); refs; a merge as a three-way merge against the merge base (a lowest common ancestor in the DAG); a rebase as a replay that creates new commits with new hashes
A11.D2 Delivery as a measurable system: the four DORA key metrics (deployment frequency, lead time for changes, change failure rate, time to restore service) and their evidence base (Forsgren, Humble and Kim, *Accelerate*, 2018); small batches and trunk-based development read as queueing (A2.D8 — smaller batches wait less)
A11.D3 The profession: the ACM Code of Ethics and Professional Conduct (2018); permissive versus copyleft licences and why a dependency's licence matters; responsibility for privacy in system design (the Cloud Cybersecurity companion's PV modules own the technical side)
> **Problem set:** A11-P1…A11-P3 (Appendix P; keys in Appendix K).
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

> **Academic depth (rule 0.4.10) — B2.D.** Aligned with the OS courses in §0.6.
B2.D1 Virtualization theory: Popek and Goldberg's requirements (equivalence, resource control, efficiency) and their theorem — an instruction set can be virtualized by trap-and-emulate if its sensitive instructions are a subset of its privileged ones; why classic x86 failed the condition and was virtualized by binary translation, then paravirtualization, then hardware support (VT-x and AMD-V, nested page tables); microVMs and user-space kernels (Firecracker, gVisor) as the middle ground between containers and VMs
> **Problem set:** B2-P1 (Appendix P; key in Appendix K).
### B3. Architecture Patterns & the Well-Architected Frameworks
- [ ] B3 done
High availability, fault tolerance, horizontal vs vertical scaling
Disaster recovery patterns: backup/restore, pilot light, warm standby, multi-site active-active — and RTO/RPO math
Provider-specific framework nuance: GCP's Architecture Framework (Operational Excellence, Security, Reliability, Performance/Cost) vs AWS's Well-Architected Framework (6 pillars incl. Sustainability) vs Azure's Well-Architected Framework (5 pillars). Same ideas, different names — we'll map them directly.

> **Academic depth (rule 0.4.10) — B3.D.**
B3.D1 Reliability mathematics: MTBF, MTTR and steady-state availability A = MTBF / (MTBF + MTTR); the exponential failure model (A2.D5) and its memorylessness; the durability of r replicas as the probability that all fail within one repair window; RTO and RPO as specified bounds that a design must be shown to meet
> **Problem set:** B3-P1, B3-P2 (Appendix P; keys in Appendix K).
### B4. Cloud Economics & FinOps
- [ ] B4 done
Pay-as-you-go vs reserved/committed-use pricing, spot/preemptible instances
Cost visibility and optimization tooling per provider
Budget alerts, tagging/labeling for cost allocation
Three budgets per system: money (billing account → project link, budgets, the billing export for analysis), errors (the C7 error budget) and quota (per-project API and resource quotas, raised before launch). GCP's discount forms: sustained-use, committed-use, Spot. Carbon as a cost-adjacent signal (region choice, the provider's footprint report)

> **Academic depth (rule 0.4.10) — B4.D.**
B4.D1 Cost modelling: total cost of ownership; the break-even of a commitment against on-demand pricing (a commitment at discount d pays off when expected utilization exceeds 1 − d); marginal versus average cost; forecasting spend with confidence intervals (A2.D7)
> **Problem set:** B4-P1 (Appendix P; key in Appendix K).
### B5. Cloud IAM Concepts (deep provider dives happen later; the model is universal)
- [ ] B5 done
Principals, roles/policies, resource hierarchies (org → folder/OU → project/account)
RBAC vs ABAC, policy inheritance, least-privilege design
Service accounts / managed identities and workload identity federation
Role types (basic, predefined, custom), conditional bindings (IAM Conditions), deny policies, and workforce federation for people beside workload federation for machines

> **Academic depth (rule 0.4.10) — B5.D.**
B5.D1 Policy evaluation as logic: an IAM decision as a function of principal, action, resource and context; default deny, explicit deny overriding allow, and inheritance down the resource hierarchy as a union of grants; least privilege as a minimization problem; automated policy reasoning with SMT solvers, as in AWS's Zelkova (2018) `(verify)`; A10.D2 owns the access-control models
> **Problem set:** B5-P1 (Appendix P; key in Appendix K).
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

> **Academic depth (rule 0.4.10) — C2.D.**
C2.D1 The theory under Kubernetes: level-triggered reconciliation (observe, diff, act) and why it tolerates missed events that an edge-triggered handler would lose; scheduling as bin packing (NP-hard, A4.D7) solved by filter-and-score heuristics; the lineage Borg, Omega, Kubernetes (Burns et al., 2016)
> **Problem set:** C2-P1 (Appendix P; key in Appendix K).
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
Delivery performance: the four DORA metrics (deployment frequency, lead time for changes, change failure rate, failed-deployment recovery time), and platform engineering — a golden-path service template and preview environments destroyed on merge
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

> **Academic depth (rule 0.4.10) — C6.D.**
C6.D1 Measurement theory for observability: counters, gauges and histograms; why percentiles cannot be averaged but histograms with shared bucket boundaries can be merged (A2.D7); head versus tail sampling in tracing and the bias each introduces; the cost of label cardinality
> **Problem set:** C6-P1 (Appendix P; key in Appendix K).
### C7. SRE Principles
- [ ] C7 done
SLIs, SLOs, SLAs and how they relate; error budgets and burn-rate alerting
Toil and why eliminating it is an SRE's actual job
Incident management, on-call, postmortem culture (blameless postmortems)
Proving reliability: load tests against the SLO, and chaos experiments (kill a revision, fail a push subscription, stall a queue) in non-production first, each with its error-budget cost written down
This shows up explicitly and heavily on the PCA exam's Reliability domain and on DOP-C02/AZ-400 — it is not optional reading.

> **Academic depth (rule 0.4.10) — C7.D.**
C7.D1 SLO mathematics: error budget = (1 − SLO) × window; burn rate = observed error ratio ÷ (1 − SLO); multi-window, multi-burn-rate alerts derived from it (for a 30-day window, a burn rate of 14.4 sustained for 1 hour spends 14.4 × 1/720 = 2% of the budget); the availability of composed services (series multiply; redundant parallel copies give 1 − Π(1 − aᵢ); the primer's SD-07 owns the arithmetic, recalled here)
> **Problem set:** C7-P1, C7-P2 (Appendix P; keys in Appendix K).
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
Applied problem families, as literacy: retrieve-then-rank recommenders (two-tower retrieval, learning to rank), bandits for exploration, time-series forecasting (seasonality, backtesting), fraud and anomaly detection with human review, and uplift measurement (why a lift claim needs a control group)

> **Academic depth (rule 0.4.10) — D1.D.**
D1.D1 Learning theory: empirical risk minimization; the bias–variance decomposition of squared error; regularization as a constraint (ridge and lasso); maximum likelihood, and why minimizing cross-entropy (A2.D11) is maximum likelihood for a classifier; cross-validation as an estimator with its own variance
> **Problem set:** D1-P1 (Appendix P; key in Appendix K).
### D2. Deep Learning
- [ ] D2 done
Neural network basics: neurons, layers, activation functions, forward pass
Backpropagation intuition (built on the calculus from A2)
CNNs (images), RNNs/LSTMs (sequences, mostly historical context now)
Transformers and attention — the architecture behind every modern LLM; this is a must-understand-deeply topic, not a footnote

> **Academic depth (rule 0.4.10) — D2.D.**
D2.D1 Backpropagation as reverse-mode automatic differentiation: the chain rule (A2.D10) applied over the computation graph, whose cost is a small constant multiple of the forward pass; vanishing and exploding gradients as products of many factors; attention as a softmax-weighted sum and its O(n²) cost in sequence length
> **Problem set:** D2-P1 (Appendix P; key in Appendix K).
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
Lab Reality (Track D): D1 `[local]` notebooks (scikit-learn) · D2 `[local]` small models on CPU, `[plan-only]` for large training · D3 `[local]` tracking and pipelines, `[free-tier]` Vertex AI pieces where a free tier exists `(verify)` · D4 `[local]` RAG and agent prototypes, `[credit ~$X]` timeboxed model API calls `(verify)`.

## PART V — Google Cloud Platform
Service map by category (the vocabulary we'll build fluency in)

*Category IDs.* The companions anchor to these IDs instead of the category names:

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
Storage/DB: Cloud Storage, Cloud SQL, Spanner, Bigtable, Firestore, Memorystore, AlloyDB, Filestore, Persistent Disk / Hyperdisk, Backup and DR Service
Networking: VPC, Cloud Load Balancing, Cloud CDN, Cloud Interconnect/VPN, Cloud DNS, Cloud Armor, Cloud Router, Cloud NAT, Private Service Connect, Network Connectivity Center, Cloud NGFW
Data/Analytics: BigQuery, Pub/Sub, Dataflow, Dataproc, Cloud Composer, Looker, Datastream, Data Fusion, Dataplex, BigLake, Analytics Hub
AI/ML: Vertex AI (full suite: Workbench, Training, Pipelines, Feature Store, Model Registry, Endpoints, Vizier), Model Garden, Gemini Enterprise/Agent Platform, AutoML, BigQuery ML, the pre-built AI APIs (Vision, Video Intelligence, Speech-to-Text, Natural Language, Translation, Document AI)
Security: IAM, Cloud KMS, VPC Service Controls, Binary Authorization, Security Command Center, Google SecOps (Chronicle), Identity-Aware Proxy, Identity Platform, Secret Manager, Certificate Manager, Sensitive Data Protection, Organization Policy Service, Cloud Asset Inventory, Assured Workloads
Ops/DevOps: Cloud Build, Cloud Deploy, Artifact Registry, Cloud Monitoring/Logging, Cloud Trace, Cloud Profiler, Error Reporting, Managed Service for Prometheus, Service Health, Cloud Billing reports and the billing export to BigQuery, Recommender (Active Assist), Cloud Quotas, Carbon Footprint
Certification-by-certification breakdown
(Domain weights below are from the current official exam guides where I verified them directly; where I didn't verify exact percentages, I've given you the topic structure and flagged it — always cross-check the live guide a few weeks before you actually schedule.)
 
1. Professional Cloud Architect (PCA) — your named priority #1
- [ ] PCA passed
- **Lab Reality**: `[free-tier]` Compute Engine / Cloud Run / Cloud Storage builds · `[plan-only]` multi-region and hybrid designs · `[paper]` the published case studies.
 
Format: 50 scenario-based questions, 2 hours, includes 4 published case studies you study in advance
> **Verified 2026-09-24 against the vendor's live page:** 50–60 questions; 4 case studies are published and 2 appear per exam. (verify live before scheduling)
Domains (verified): Designing (24%) · Provisioning (15%) · Security & Securing AI (20%) · Optimization (18%) · Implementation (11%) · Reliability & Well-Architected Framework (12%)
> **Verified 2026-09-24 against the vendor's live page:** the live guide's weights are 25 / 17.5 / 17.5 / 15 / 12.5 / 12.5, under different section names. The line above keeps the 2026-09-16 reading. (verify live before scheduling)
What makes it hard: it's not "what does this service do," it's "given these constraints, which trade-off is correct" — architectural judgment, tested through the case studies
The published case studies (exam guide v6.1): Altostrat Media, Cymbal Retail, EHR Healthcare, KnightMotives Automotive `(verify)` against the live guide. Each gets a written HLD and one "I pick X because Y, I accept Z" answer per requirement.
Migration and modernization (PCA 1.4): the six Rs mapped to landings (rehost with Migrate to Virtual Machines, replatform, re-architect for GKE or Cloud Run, retire, retain, repurchase); Migration Center discovery, dependency mapping and wave planning; licence impact (bring-your-own vs included) before wave 1; data movement (Database Migration Service, Datastream, Storage Transfer Service, Transfer Appliance); wave-0 connectivity; cutover checklist with a written rollback
2. Professional Machine Learning Engineer (PMLE) — your named priority #2
- [ ] PMLE passed
- **Lab Reality**: `[local]` notebooks · `[credit ~$X]` timeboxed Vertex AI training/prediction (Part V note) · `[plan-only]` large training runs.
 
6 domains covering the full ML lifecycle: framing business problems as ML problems · architecting low-code/AutoML/BigQuery ML solutions · building with Google's AI APIs and foundation models (Gemini, Model Garden) · developing/scaling custom models (Vertex AI Training, distributed training, hyperparameter tuning) · automating MLOps pipelines (Vertex AI Pipelines, CI/CD/CT) · monitoring, responsible AI, and maintaining solutions in production
> **Verified 2026-09-24 against the vendor's live page:** still 6 sections, renamed: low-code AI 13, data & models 16, scaling prototypes 21, serving 20, pipelines 18, monitoring 13. The exam moved from Vertex AI to the **Gemini Enterprise Agent Platform**. (verify live before scheduling)
Heavy 2026 emphasis on GenAI: Vertex AI Studio, Model Garden, RAG architectures
3. Data Engineer
- [ ] Professional Data Engineer passed
- **Lab Reality**: `[free-tier]` Pub/Sub and the BigQuery sandbox `(verify)` · `[credit ~$X]` short Dataflow runs · `[plan-only]` Dataproc/Composer at scale.
> **Verified 2026-09-24 against the vendor's live page:** Active; a branding update is pending. (verify live before scheduling)
 
Designing data processing systems · building/operationalizing data pipelines (Dataflow, Dataproc, Pub/Sub, BigQuery, Composer) · operationalizing ML models · ensuring reliability, security, and compliance of data solutions
4. Cloud Developer
- [ ] Professional Cloud Developer passed
- **Lab Reality**: `[free-tier]` Cloud Run, Cloud Functions, Firestore · `[credit ~$X]` Cloud Build / Cloud Deploy beyond the free quota `(verify)`.
> **Verified 2026-09-24 against the vendor's live page:** Active; its own page is live and registration is open, although it is missing from the certification index page's rendered list. (verify live before scheduling)
 
Designing highly scalable/available cloud-native apps · building and testing applications · deploying (Cloud Build, Cloud Deploy, Cloud Run/GKE/App Engine) · integrating with GCP managed services and APIs · monitoring application performance
5. Cloud DevOps Engineer
- [ ] Professional Cloud DevOps Engineer passed
- **Lab Reality**: `[free-tier]` Cloud Build, Cloud Monitoring/Logging · `[credit ~$X]` a short-lived GKE cluster.
 
Applying SRE principles to service design and operations (Track C7 directly) · building CI/CD pipelines · implementing observability · optimizing performance · managing releases and incidents
6. Cloud Security Engineer
- [ ] Professional Cloud Security Engineer passed
- **Lab Reality**: `[free-tier]` IAM and firewall rules · `[credit ~$X]` Cloud KMS keys `(verify)` · `[plan-only]` VPC Service Controls perimeters and organization policies (they need an organization).
 
Configuring access (IAM design) · configuring network security (VPC-SC, firewall, Cloud Armor) · ensuring data protection (KMS, DLP) · managing security operations · ensuring regulatory compliance
7. Cloud Network Engineer
- [ ] Professional Cloud Network Engineer passed
- **Lab Reality**: `[local]` packet labs · `[credit ~$X]` small VPC + load-balancer labs destroyed the same day · `[plan-only]` Interconnect / HA VPN designs.
 
Designing/planning GCP network architecture · implementing VPC · configuring network services (load balancing, DNS, CDN) · implementing hybrid connectivity (Interconnect/VPN) · implementing network security · managing/monitoring networks
8. Cloud Database Engineer
- [ ] Professional Cloud Database Engineer passed
- **Lab Reality**: `[local]` Postgres (SQL companion lab kit) · `[credit ~$X]` Cloud SQL destroyed the same day · `[plan-only]` Spanner and AlloyDB.
> **Verified 2026-09-24 against the vendor's live page:** Active; a branding update is pending. Guide weights: design ~32%, manage ~25%, migrate ~23%, deploy ~20%. (verify live before scheduling)
 
Designing scalable/secure database solutions (choosing the right DB from the whole storage list) · managing solutions (migration, provisioning) · designing for security/compliance · optimizing performance and monitoring
9. Security Operations Engineer (newer cert — verify current exam guide closer to study time)
- [ ] Professional Security Operations Engineer passed
- **Lab Reality**: `[paper]` detection engineering · `[local]` log fixtures · `[plan-only]` Google SecOps, an enterprise product `(verify)` trial availability.
> **Verified 2026-09-24 against the vendor's live page:** Active. Six sections: platform operations 14, data management 14, threat hunting 19, detection engineering 22, incident response 21, observability 10. (verify live before scheduling)
 
Threat detection and hunting · SIEM/SOAR configuration and use (Google SecOps/Chronicle) · incident response · threat intelligence · using Gemini-assisted security operations tooling
10. Agentic Architect (Beta → GA) — we're deliberately doing this last, per the plan above
- [ ] Agentic Architect passed
- **Lab Reality**: `[local]` ADK agents · `[credit ~$X]` model API calls beyond the free quota `(verify)`.
> **Verified 2026-09-24 against the vendor's live page:** Still in beta, open until Sept 30, 2026. The exam is 3 hours: about 80 multiple-choice questions, then labs in Google Skills. Five sections, with custom agents at about 33%. The guide names ADK, A2A and **MCP**; it does **not** name "Agent Registry" or "Agent Gateway". (verify live before scheduling)
 
Two-part exam: proctored multiple-choice (conceptual/design) plus hands-on coding labs on Google Skills
~5 sections; roughly a third of the exam is writing actual agent code
Built around: Agent Development Kit (ADK), Agent Registry, Agent Gateway, the A2A (agent-to-agent) protocol, LLM/agent design patterns, reliability/cost/security/scalability of agentic systems
Lab Reality (GCP): Compute Engine (e2-micro), Cloud Run, Cloud Functions, Cloud Storage, Firestore, and Pub/Sub all have genuine always-free tiers — we'll build real projects on these at zero cost. Your $300 credit is the right budget for: a short-lived GKE cluster, a small BigQuery dataset, and Vertex AI training/prediction experiments — we'll timebox these deliberately. Spanner, multi-region deployments, and Anthos we'll study via architecture + Terraform-plan only, and via read-only tours of your workplace console (never creating/modifying resources there).
 
## PART VI — AWS
Service map by category (cross-referenced to GCP — see Part VIII for the full table)
Compute: EC2, Lambda, ECS/EKS, Fargate, App Runner · Storage/DB: S3, EBS, RDS, DynamoDB, Aurora · Networking: VPC, ELB (ALB/NLB), Route 53, CloudFront, Direct Connect · Data: Kinesis, Glue, Redshift, EMR · AI/ML: SageMaker, Bedrock · Security: IAM, KMS, GuardDuty, Security Hub, Macie · DevOps: CodeBuild/CodePipeline/CodeDeploy, CloudFormation/CDK
 
1. Solutions Architect – Professional (SAP-C02)
- [ ] AWS SAP passed
- **Lab Reality**: `[free-tier]` single-account labs · `[plan-only]` Organizations / multi-account Terraform.
> **Verified 2026-09-24 against the vendor's live page:** Domain weights 26/29/25/20 confirmed. **SAP-C02 is being replaced:** SAP-C03 registration opens Oct 27, 2026, and the last day for SAP-C02 is Nov 17, 2026. (verify live before scheduling)
 
4 domains: Design for Organizational Complexity (~26%) · Design for New Solutions (~29%) · Continuous Improvement for Existing Solutions (~25%) · Accelerate Workload Migration and Modernization (~20%) (check current guide for exact figures)
Heavy on multi-account strategy (AWS Organizations, SCPs), the 6 R's of migration, and cost/resilience trade-offs at enterprise scale
2. DevOps Engineer – Professional (DOP-C02)
- [ ] AWS DOP passed
- **Lab Reality**: `[free-tier]` CodeBuild/CodePipeline within the free quota `(verify)` · `[plan-only]` the rest.
> **Verified 2026-09-24 against the vendor's live page:** Active. Six domains, 22/17/15/15/14/17. The Korean-language exam retires after Dec 31, 2026. (verify live before scheduling)
 
~6 domains: SDLC Automation · Configuration Management & IaC · Resilient Cloud Solutions · Monitoring & Logging · Incident & Event Response · Security & Compliance
Direct extension of Track C — you'll recognize nearly everything, just under AWS-native tool names
3. Generative AI Developer – Professional (AIP-C01) — genuinely new (2025/2026), one of AWS's hardest exams by reputation
- [ ] AWS AIP passed
- **Lab Reality**: `[local]` RAG prototypes · `[credit ~$X]` Bedrock calls (no free tier assumed; `(verify)`).
> **Verified 2026-09-24 against the vendor's live page:** Active. Five domains: FM integration & data 31, implementation 26, AI safety/governance 20, efficiency 12, testing 11. (verify live before scheduling)
 
Domains cover: selecting/architecting with foundation models (Bedrock) · building resilient, provider-flexible GenAI architectures · RAG, vector stores, and knowledge base design · data security, privacy, and responsible-AI governance for GenAI systems · cost/latency/performance optimization
Recommendation candidates already hold AWS ML/Data Engineer associate-level knowledge — we'll build that via Track D first
4. Security – Specialty (SCS-C03) (corrected from your SCS-C02 — that version retired Dec 1, 2025)
- [ ] AWS SCS passed
- **Lab Reality**: `[free-tier]` IAM and KMS basics · `[plan-only]` organization-level controls.
> **Verified 2026-09-24 against the vendor's live page:** Weights confirmed. The last domain is named **"Security Foundations and Governance" (14%)**, not "Management & Security Governance". (verify live before scheduling)
 
Current domains (Dec 2025 refresh): Identity & Access Management (~20%) · Data Protection (~18%) · Infrastructure Security (~18%) · Detection (~16%, now its own domain) · Incident Response (~14%) · Management & Security Governance
New emphasis on GenAI-application security guardrails
5. Advanced Networking – Specialty (ANS-C01) — last exam day Dec 31, 2026 per AWS, no announced successor
- [ ] AWS ANS passed
- **Lab Reality**: `[local]` BGP labs in containers · `[plan-only]` Direct Connect and Transit Gateway.
> **Verified 2026-09-24 against the vendor's live page:** Retiring: last exam day Dec 31, 2026; no new certifications are issued after retirement. Domains 30/26/20/24. (verify live before scheduling)
 
Hybrid IT network architecture at scale: BGP, Direct Connect, Transit Gateway, multi-region networking, network security (WAF/Shield/Network Firewall), automation
Five-year-networking-experience recommended candidate; we'll fold the concepts into Track A5/C naturally either way — the cert itself is optional depending on how our timeline looks by mid-2026
> **Note:** mid-2026 has passed. The ANS-C01 decision is due before its last exam day, Dec 31, 2026 (verified 2026-09-24; verify live).
Lab Reality (AWS): Free tier covers EC2 t2/t3.micro (750 hrs/mo for 12 months on new accounts — check current status of your account), Lambda (1M requests/mo, always-free), S3 (5GB), DynamoDB (25GB, always-free). For VPC/networking/multi-account work we'll build with Terraform and validate via plan, since Organizations/Transit Gateway/multi-account labs cost real money fast.
> **Note:** new AWS accounts since July 2025 get a credit-based free plan instead of the 12-month free tier described above (verify).
 
## PART VII — Azure
Service map by category
Compute: Virtual Machines, AKS, Container Apps, Functions, App Service · Storage/DB: Blob Storage, Azure SQL Database, Cosmos DB, Managed Disks · Networking: VNet, Azure Load Balancer, Application Gateway, Front Door, Azure DNS, ExpressRoute · Data: Synapse Analytics, Data Factory, Stream Analytics · AI/ML: Azure Machine Learning, Azure AI Foundry (OpenAI Service) · Security: Microsoft Entra ID, Key Vault, Microsoft Defender, Microsoft Sentinel · DevOps: Azure Pipelines, Azure Repos, ARM/Bicep
 
Provider-specific nuance to know up front: unlike GCP and AWS, Azure's Expert-tier exams have real prerequisites — AZ-305 requires an active AZ-104; AZ-400 requires AZ-104 or AZ-204; SC-100 requires one of AZ-500/SC-200/SC-300. This means your Azure path structurally requires associate-level certs first even though you only named the Expert ones — we'll fold AZ-104-equivalent knowledge into Track G teaching either way, whether or not you sit that exact exam.

> **Note:** there is no Track G. AZ-104-equivalent knowledge folds into Phase 7 through B5 and C-track recall, taught as the sub-block below.

**AZ-104-equivalent sub-block**: Entra ID and Azure RBAC (recall B5) · VNet, NSGs, Load Balancer and Azure DNS (recall A5 and Part VIII) · virtual machines and storage (recall B2, C1 and Part VIII) · Azure Monitor (recall C6) · governance with Azure Policy (recall B5, Part VIII). Check the topic list against the live AZ-104 guide `(verify)`.
 
1. Solutions Architect Expert (AZ-305) (English version last updated April 17, 2026 — current)
- [ ] Azure AZ-305 passed
- **Lab Reality**: `[paper]` design documents · `[free-tier]` small always-free services.
> **Verified 2026-09-24 against the vendor's live page:** Confirmed: skills as of Apr 17, 2026; the prerequisite is Azure Administrator Associate. (verify live before scheduling)
 
Scenario-heavy, spans identity, data, infrastructure, and governance design decisions
No live labs (unlike AZ-104); rewards architectural judgment over recall — closest Azure analog to the GCP PCA
2. DevOps Engineer Expert (AZ-400)
- [ ] Azure AZ-400 passed
- **Lab Reality**: `[free-tier]` Azure DevOps / GitHub Actions minutes `(verify)`.
> **Verified 2026-09-24 against the vendor's live page:** Skills revised as of **July 27, 2026**; build/release pipelines is 50–55%. (verify live before scheduling)
 
Source control strategy, CI/CD pipeline design (Azure Pipelines + GitHub Actions), IaC (ARM/Bicep/Terraform), release/deployment strategies, security & compliance in the pipeline, monitoring feedback loops
The direct Track C capstone for Azure
3. Cybersecurity Architect Expert (SC-100) (English version updated July 28, 2026 — current)
- [ ] Azure SC-100 passed
- **Lab Reality**: `[paper]` Zero Trust designs · `[free-tier]` Entra ID basics.
> **Verified 2026-09-24 against the vendor's live page:** The study guide now shows skills measured **as of Oct 21, 2026** (an upcoming revision). The AZ-500 prerequisite is now listed as **"Cloud and AI Security Engineer Associate"**. (verify live before scheduling)
 
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
> **Note:** status as of 2026-09-24: the three notes below were re-checked that day against the vendors' live pages. New dated items are in the Part V–VII verification notes.
Agentic Architect beta closes Sept 30, 2026 — we're intentionally skipping the beta window and targeting GA later.
AWS ANS-C01 last exam Dec 31, 2026 — decide later, once we see real progress against the plan; no shame either way.
AWS Security Specialty is now SCS-C03, not SCS-C02 — already corrected in this plan.
Check every exam guide's live PDF ~4–6 weeks before you actually schedule — Google, AWS, and Microsoft all revise domain weights and content periodically (several did so earlier this year), and I'll flag anything relevant I notice as we go, but I can't watch it continuously between our sessions.
## PART X — How We'll Actually Work
Each session, we take one module from the plan above, I teach it properly (explanations, worked examples, real config/code where it applies, checks for understanding), and we mark it done. Tell me any time you want to:
 
Skip ahead on something you already know (say so — no need to sit through material you've got)
Jump to a specific cert's material directly instead of following the phase order
Go hands-on on something — I'll tell you honestly whether it fits free tier, needs a slice of your $300, or should stay as a Terraform-plan/console-read exercise

> **Note:** these overrides are the suite-wide rule in §0.4.1; the session shape is §0.4.2.
We start with A1: Digital Logic & Data Representation below, right now.

> **Note:** Status as of 2026-09-24: the course is a fresh start, so this sentence is still true.

## Appendix P — Academic problem sets (rule 0.4.10)

Each problem belongs to the academic pass of the module in its label. The type says what is assessed: **proof** (a written argument), **derive** (a formula from first principles), **compute** (a number, with the steps shown) or **design** (a short argued choice). Keys are in Appendix K, shown only after the attempt (rule 0.4.7). Problems are issued one per turn, on the ramp of rule 0.4.3.

**A1 — computer organization**
- **A1-P1** · proof · Prove that in n-bit two's complement the bit pattern of −x is `~x + 1` (mod 2ⁿ).
- **A1-P2** · compute · In 8-bit two's complement, compute 100 + 50. Give the bit pattern, its signed value, and whether the overflow condition fires.
- **A1-P3** · proof · Prove that NAND alone is functionally complete.
- **A1-P4** · compute · 80% of a program's run time parallelizes perfectly. What speedup do 16 cores give, and what is the limit as the core count grows?
- **A1-P5** · compute · A 32 KiB, 4-way set-associative cache has 64-byte lines and 32-bit addresses. How many offset, index and tag bits?
- **A1-P6** · compute · L1: hit time 1 ns, miss rate 5%. L2: hit time 10 ns, local miss rate 20%. Memory: 100 ns. Compute the AMAT.
- **A1-P7** · design · Two goroutines on two cores each increment their own `int64` counter; the counters sit next to each other in one struct. Why is this slower than with each counter padded to 64 bytes?

**A2 — mathematics**
- **A2-P1** · proof · Prove by induction that 1 + 2 + … + n = n(n + 1)/2.
- **A2-P2** · proof · Prove that √2 is irrational.
- **A2-P3** · compute · Use the extended Euclidean algorithm to find 17⁻¹ mod 3120.
- **A2-P4** · proof · Let n = pq for distinct primes p and q, and ed ≡ 1 (mod φ(n)). Prove that (mᵉ)ᵈ ≡ m (mod n) for every m coprime to n.
- **A2-P5** · compute · A diagnostic has 99% sensitivity and 95% specificity; the condition's prevalence is 1%. What is P(condition | positive)?
- **A2-P6** · derive · Derive the birthday bound: for n values drawn uniformly from N, show P(no collision) ≈ e^(−n(n−1)/2N), then give the n at which P(collision) ≈ 1/2 for N = 2⁶⁴.
- **A2-P7** · compute · A request fans out to 100 servers in parallel and waits for all of them. Each server independently exceeds 10 ms with probability 1%. What is P(the request exceeds 10 ms)? With 1,000 servers?
- **A2-P8** · compute · Use Markov's inequality to bound P(X ≥ 10) for a non-negative X with mean 2. Then use Chebyshev's with variance 4 to bound P(|X − 2| ≥ 8). Which bound is tighter here, and why?
- **A2-P9** · derive · For an M/M/1 queue with λ = 80 requests/s and μ = 100 requests/s, compute ρ, the mean number in the system and the mean time in the system, and check your answer with Little's law. What happens to the mean time in the system at λ = 95?
- **A2-P10** · proof · Prove that the least-squares solution of Ax = b satisfies AᵀAx = Aᵀb.
- **A2-P11** · compute · Compute the entropy of a source emitting A, B, C, D with probabilities 1/2, 1/4, 1/8, 1/8, and give a prefix code that achieves it.
- **A2-P12** · compute · How many 3-replica quorums can be chosen from 5 replicas? Then use complement counting (the one-set case of inclusion–exclusion) to count the 4-digit PINs that contain at least one 7.

**A3 — programming**
- **A3-P1** · compute · Predict the output of the Python code `a = [1, 2]; b = a; b.append(3); print(a)`, and of the Go code `a := []int{1, 2}; b := a; b[0] = 9; fmt.Println(a)`. Explain each by the value/reference model.
- **A3-P2** · proof · Prove by induction that a recursive `pow(x, n)` that returns 1 for n = 0 and `x * pow(x, n-1)` otherwise returns xⁿ for every n ≥ 0, and that it terminates.
- **A3-P3** · design · Is Go's `io.Reader` an example of nominal or structural typing? What does a type have to do to be an `io.Reader`, and what would it have to do in Java?
- **A3-P4** · proof · State a loop invariant for a loop that sums an array, and show initialization, maintenance and termination.

**A4 — algorithms**
- **A4-P1** · proof · Prove from the definition that 3n² + 10n = O(n²), giving explicit constants.
- **A4-P2** · proof · State a loop invariant for binary search over a sorted array and use it to prove correctness.
- **A4-P3** · derive · Solve T(n) = 2T(n/2) + n with T(1) = 1 by the recursion tree, and confirm with the master theorem.
- **A4-P4** · proof · Prove that every comparison sort needs Ω(n log n) comparisons in the worst case.
- **A4-P5** · derive · Show that appending to a dynamic array that doubles its capacity when full costs O(1) amortized per append.
- **A4-P6** · proof · Prove that Dijkstra's algorithm is correct when all edge weights are non-negative, and give a three-vertex graph with one negative edge on which it fails.
- **A4-P7** · compute · Fill the dynamic-programming table for the edit distance between "kitten" and "sitting", and give the distance.
- **A4-P8** · derive · A Bloom filter has m bits, k hash functions and n inserted keys. Derive the false-positive rate, then compute it for m = 10n and k = 7.
- **A4-P9** · proof · Show that the decision version of bin packing is in NP, and explain what NP-completeness implies for a cluster scheduler.

**A5 — networking**
- **A5-P1** · compute · A 1,500-byte packet crosses a 10 Mb/s link 2,000 km long (propagation 2 × 10⁸ m/s). Compute the transmission and propagation delays.
- **A5-P2** · compute · Stop-and-wait over a 1 Gb/s link with RTT 30 ms and 1,500-byte packets: compute the sender utilization, then the window (in packets) needed to fill the pipe.
- **A5-P3** · proof · Show that with selective repeat and a sequence-number space of size k, a window larger than k/2 lets the receiver accept a retransmitted old packet as new data.
- **A5-P4** · compute · EstimatedRTT = 100 ms, DevRTT = 10 ms, α = 1/8, β = 1/4. A SampleRTT of 140 ms arrives. Compute the new EstimatedRTT, the new DevRTT and the new timeout.
- **A5-P5** · design · Why does AIMD converge toward a fair share between two flows while additive-increase additive-decrease does not?
- **A5-P6** · compute · Run distance-vector updates on a three-router line A–B–C (link costs 1) until convergence, then break link B–C and show the first two rounds of count-to-infinity.
- **A5-P7** · design · Why can QUIC deliver stream 2's data while stream 1 waits for a lost packet, when HTTP/2 over TCP cannot?

**A6 — operating systems**
- **A6-P1** · compute · Jobs of lengths 10, 1 and 2 arrive at time 0. Compute the mean turnaround time under FIFO (in that order) and under SJF.
- **A6-P2** · proof · Prove that SJF minimizes mean turnaround time when all jobs arrive together.
- **A6-P3** · compute · A 32-bit address space with 4 KiB pages and 4-byte page-table entries: how large is a single-level page table? With a two-level table, how much is needed for a process that touches only one page?
- **A6-P4** · compute · Run FIFO, LRU and OPT on the reference string 1 2 3 4 1 2 5 1 2 3 4 5 with 3 frames, and count the faults of each.
- **A6-P5** · design · Two threads lock mutexes A and B in opposite orders. Show the deadlock, name the Coffman condition you remove, and give the fix.
- **A6-P6** · design · A write returns successfully and the machine loses power before `fsync`. What may the file contain after reboot on a journaling file system in ordered mode, and why?
- **A6-P7** · compute · RAID 5 over 5 disks of 4 TB each: usable capacity, and how many disk failures it survives.

**A7 — software architecture**
- **A7-P1** · compute · A package has 3 incoming and 9 outgoing dependencies. Compute its instability and say whether other packages should depend on it.
- **A7-P2** · proof · A base method accepts any integer and promises a non-negative result. A subclass accepts only positive integers and returns any integer. Which Liskov–Wing conditions does it break?
- **A7-P3** · design · Write a quality-attribute scenario for "the checkout must stay available when the payment provider is down".
- **A7-P4** · design · Model a two-process mutex as a state machine, state the safety property and the liveness property, and say which one a timeout-based lock can violate.
- **A7-P5** · proof · Show that `PUT /items/42 {...}` is idempotent and `POST /items {...}` is not, as properties of functions on server state.

**A9 — distributed systems**
- **A9-P1** · compute · Three processes exchange messages; assign Lamport timestamps to a given trace (process p sends m1 at local event 2; process q receives m1 after its local event 1, then sends m2; process r receives m2 after its local events 1–3), and name two events that are concurrent.
- **A9-P2** · proof · Show with a counterexample that C(a) < C(b) for Lamport clocks does not imply a → b, and say what vector clocks add.
- **A9-P3** · proof · Prove that R + W > N guarantees that every read quorum intersects every write quorum. Does N = 5, W = 3, R = 2 guarantee reading the latest write?
- **A9-P4** · proof · Give the Gilbert–Lynch proof sketch that no system can provide linearizability and availability during a network partition.
- **A9-P5** · design · A two-phase-commit coordinator crashes after every participant voted yes but before any learned the decision. What can the participants do, and why?
- **A9-P6** · proof · Explain why a Raft leader may not commit an entry from an earlier term just by counting replicas, and what rule fixes it.
- **A9-P7** · proof · Prove that the merge of a G-Counter (element-wise max of per-replica counts) is commutative, associative and idempotent.
- **A9-P8** · compute · How many replicas are needed to tolerate 2 Byzantine faults, and how many for 2 crash faults under majority consensus?
- **A9-P9** · compute · A service calls 50 backends in parallel; each has p99 = 20 ms. With hedging after the p95 (send a second copy if no reply by then), what problem does hedging solve, and what load does it add?

**A10 — security**
- **A10-P1** · design · Name the Saltzer–Schroeder principle violated by each: a default admin password; a cache that skips the permission check on a hit; a secret encryption algorithm.
- **A10-P2** · design · Under Bell–LaPadula, may a Secret-cleared subject read a Top-Secret file? Write to a Confidential file? Under Biba with the same levels read as integrity levels?
- **A10-P3** · design · Describe Lowe's attack on the Needham–Schroeder public-key protocol and the one-field fix.
- **A10-P4** · design · Map each of these mitigations to the bug class it addresses: stack canary, ASLR, non-executable stack.
- **A10-P5** · design · An RBAC system has roles Viewer ⊂ Editor ⊂ Owner. Write the permission-assignment and user-assignment relations for a user who needs to edit, and show the least-privilege choice.

**A11 — delivery**
- **A11-P1** · design · Why does changing one byte of a file three commits ago change the hash of the current commit?
- **A11-P2** · compute · A team deployed 40 times in a month; 6 deployments caused incidents. Compute the change failure rate.
- **A11-P3** · design · A dependency changes from a permissive licence to a copyleft one. What must you check before upgrading?

**B–D tracks**
- **B2-P1** · design · Classic x86 had instructions such as `POPF` that behave differently in user and kernel mode without trapping. Which Popek–Goldberg condition does that break, and how did hardware support fix it?
- **B3-P1** · compute · A server has MTBF 1,000 hours and MTTR 2 hours. What is its availability? Two independent such servers in active–active?
- **B3-P2** · compute · Each replica fails independently with probability 0.001 during one repair window. What is the probability of losing data with three replicas?
- **B4-P1** · compute · A one-year commitment gives a 37% discount. Above what average utilization does it beat on-demand?
- **B5-P1** · design · A user has an allow on a folder and an explicit deny on one project in it. What is the decision for a resource in that project, and in a sibling project?
- **C2-P1** · design · Why does a level-triggered controller recover after it was down while three events happened, when an edge-triggered handler would not?
- **C6-P1** · design · Three hosts report p99 latencies of 10, 12 and 200 ms. Why is 74 ms not the fleet p99, and what data would give it?
- **C7-P1** · compute · A 99.9% SLO over 30 days: how many minutes of full outage is the error budget?
- **C7-P2** · compute · Over 1 hour the error ratio is 1.44% against a 99.9% SLO. Compute the burn rate and the fraction of a 30-day budget spent.
- **D1-P1** · derive · Show that minimizing the mean cross-entropy of a binary classifier maximizes the likelihood of the labels.
- **D2-P1** · compute · For y = (w·x + b)², compute ∂y/∂w by the chain rule at w = 2, x = 3, b = 1.

## Appendix K — Academic problem keys (AFTER attempt only)

Each key gives the expected answer and at least one expected wrong answer with the reason it is wrong (rule 0.4.7). Numbers were computed, not estimated.

**A1**
- **A1-P1** — Expected: ~x = (2ⁿ − 1) − x, so ~x + 1 = 2ⁿ − x ≡ −x (mod 2ⁿ). · Wrong: "flipping the bits gives −x" — that is one's complement, off by one.
- **A1-P2** — Expected: 150 = `1001 0110` = 0x96, read as signed −106; the overflow condition fires (carry into the sign bit 1, carry out 0; two positives gave a negative). · Wrong: "no overflow because there is no carry out" — the carry out detects unsigned overflow, not signed.
- **A1-P3** — Expected: NOT a = a NAND a; a AND b = NOT(a NAND b) = (a NAND b) NAND (a NAND b); a OR b = (NOT a) NAND (NOT b) by De Morgan. {AND, OR, NOT} is complete (every truth table has a sum-of-products form), so NAND is. · Wrong: building AND and NOT from NAND but not arguing that {AND, NOT} or {AND, OR, NOT} is complete.
- **A1-P4** — Expected: 1 / (0.2 + 0.8/16) = 1 / 0.25 = 4×; limit 1/0.2 = 5×. · Wrong: 16× or 12.8× (0.8 × 16) — ignores the serial 20%.
- **A1-P5** — Expected: offset 6 bits (64 B); sets = 32,768 / (64 × 4) = 128, so index 7 bits; tag 32 − 13 = 19 bits. · Wrong: index 9 bits — counts 512 lines, forgetting that 4 lines share a set.
- **A1-P6** — Expected: 1 + 0.05 × (10 + 0.2 × 100) = 1 + 0.05 × 30 = 2.5 ns. · Wrong: 21.5 ns — applies the L2 miss rate globally instead of to L1 misses only.
- **A1-P7** — Expected: both counters are in one 64-byte cache line; each write takes the line exclusive (MESI), invalidating the other core's copy, so the line ping-pongs between cores; padding puts them in separate lines. · Wrong: "a data race" or "lock contention" — each goroutine writes only its own counter and there is no lock.

**A2**
- **A2-P1** — Expected: base n = 1: 1 = 1·2/2. Step: if the sum to k is k(k+1)/2, the sum to k+1 is k(k+1)/2 + (k+1) = (k+1)(k+2)/2. · Wrong: checking n = 1, 2, 3 and concluding — examples are not a proof.
- **A2-P2** — Expected: suppose √2 = p/q in lowest terms; then p² = 2q², so p is even, p = 2r, so q² = 2r² and q is even — contradicting lowest terms. · Wrong: "√2 = 1.41421… never repeats" — asserts the conclusion.
- **A2-P3** — Expected: 3120 = 17·183 + 9; 17 = 9·1 + 8; 9 = 8·1 + 1. Back-substituting: 1 = 9 − 8 = 9 − (17 − 9) = 2·9 − 17 = 2·(3120 − 17·183) − 17 = 2·3120 − 367·17, so 17⁻¹ ≡ −367 ≡ 2753 (mod 3120). Check: 17 × 2753 = 46,801 = 15 × 3120 + 1. · Wrong: 3120/17 or any non-integer — a modular inverse is an integer class.
- **A2-P4** — Expected: ed = 1 + kφ(n) with φ(n) = (p − 1)(q − 1). By Euler's theorem m^φ(n) ≡ 1 (mod n) for gcd(m, n) = 1, so m^(ed) = m·(m^φ(n))ᵏ ≡ m (mod n). (The result also holds for m not coprime to n, by the Chinese remainder theorem applied mod p and mod q.) · Wrong: using Fermat's little theorem mod n directly — n is not prime.
- **A2-P5** — Expected: P(+) = 0.99 × 0.01 + 0.05 × 0.99 = 0.0099 + 0.0495 = 0.0594; P(C | +) = 0.0099 / 0.0594 ≈ 0.167 (about 17%). · Wrong: 99% — confuses P(+ | C) with P(C | +) (base-rate neglect).
- **A2-P6** — Expected: P(no collision) = Π_{i=0}^{n−1}(1 − i/N) ≈ Π e^(−i/N) = e^(−n(n−1)/2N), using 1 − x ≈ e^(−x) for small x. Setting it to 1/2 gives n ≈ √(2N ln 2) ≈ 1.1774·√N; for N = 2⁶⁴, n ≈ 1.18 × 2³² ≈ 5.1 × 10⁹. · Wrong: n ≈ N/2 — that is the count for a collision with one fixed value, not among all pairs.
- **A2-P7** — Expected: 1 − 0.99¹⁰⁰ ≈ 1 − 0.366 = 0.634; with 1,000: 1 − 0.99¹⁰⁰⁰ ≈ 1 − 4.3 × 10⁻⁵ ≈ 0.99996. · Wrong: 1% — the p99 of one server is not the p99 of a fan-out that waits for all.
- **A2-P8** — Expected: Markov: P(X ≥ 10) ≤ 2/10 = 0.2. Chebyshev: P(|X − 2| ≥ 8) ≤ 4/64 = 0.0625. Chebyshev is tighter because it uses the variance; Markov uses only the mean. (P(X ≥ 10) ⊆ P(|X − 2| ≥ 8), so 0.0625 also bounds it.) · Wrong: "Markov is always tighter because it is simpler".
- **A2-P9** — Expected: ρ = 0.8; L = ρ/(1 − ρ) = 4; W = 1/(μ − λ) = 1/20 s = 50 ms; Little: L = λW = 80 × 0.05 = 4 ✓. At λ = 95: W = 1/5 s = 200 ms (four times longer for 19% more load). · Wrong: W = 1/μ = 10 ms — that is the service time only, with no queueing.
- **A2-P10** — Expected: minimize f(x) = ‖Ax − b‖² = xᵀAᵀAx − 2bᵀAx + bᵀb; the gradient 2AᵀAx − 2Aᵀb = 0 gives AᵀAx = Aᵀb. (Geometrically, the residual b − Ax is orthogonal to the column space of A.) · Wrong: "x = A⁻¹b" — A is usually not square or not invertible.
- **A2-P11** — Expected: H = ½·1 + ¼·2 + ⅛·3 + ⅛·3 = 1.75 bits; code A = 0, B = 10, C = 110, D = 111 has mean length 1.75. · Wrong: 2 bits — that is the fixed-length code, not the entropy.
- **A2-P12** — Expected: C(5,3) = 10. PINs with at least one 7 = 10⁴ − 9⁴ = 10,000 − 6,561 = 3,439 (complement counting, the one-set case of inclusion–exclusion). · Wrong: 4 × 1,000 = 4,000 — counts PINs with several 7s more than once.

**A3**
- **A3-P1** — Expected: Python prints `[1, 2, 3]` (b names the same list object). Go prints `[9 2]` (the slice header is copied, but both headers point at the same backing array). · Wrong: Go prints `[1 2]` "because Go is pass by value" — the value copied is the header, not the array.
- **A3-P2** — Expected: base n = 0 returns 1 = x⁰; step: if pow(x, k) = xᵏ then pow(x, k+1) = x·xᵏ = xᵏ⁺¹. Termination: n decreases by 1 each call and stops at 0. · Wrong: proving only termination, or only for n ≥ 1.
- **A3-P3** — Expected: structural — any type with a method `Read(p []byte) (n int, err error)` is an `io.Reader`, with no declaration. In Java the class must name the interface (`implements`), which is nominal. · Wrong: "nominal, because `io.Reader` has a name" — the interface has a name, but satisfaction is decided by the method set.
- **A3-P4** — Expected: invariant "after i iterations, s = a[0] + … + a[i−1]"; initialization i = 0, s = 0 (the empty sum); maintenance adds a[i]; at termination i = n, so s is the whole sum. · Wrong: an invariant that mentions only i (for example "i ≤ n") — true but too weak to prove the result.

**A4**
- **A4-P1** — Expected: for n ≥ 10, 10n ≤ n², so 3n² + 10n ≤ 4n²; take c = 4, n₀ = 10. · Wrong: "drop lower-order terms" with no constants — a rule of thumb, not a proof from the definition.
- **A4-P2** — Expected: invariant "if the target is in the array, it is in a[lo..hi]"; it holds initially, each step discards only a half that cannot contain the target (sortedness), and when lo > hi the range is empty, so the target is absent; the range shrinks every step, so the loop ends. · Wrong: an invariant that is not preserved when mid is excluded (off-by-one on `hi = mid` versus `hi = mid − 1`).
- **A4-P3** — Expected: each of the log₂ n levels costs n, plus n leaves: T(n) = n log₂ n + n = Θ(n log n); master theorem case 2 (a = 2, b = 2, f(n) = Θ(n) = Θ(n^(log_b a))). · Wrong: Θ(n) — counts only the top level.
- **A4-P4** — Expected: a comparison sort is a binary decision tree whose leaves must include all n! orderings; a binary tree of height h has at most 2ʰ leaves, so h ≥ log₂(n!) = Θ(n log n) (Stirling, or n! ≥ (n/2)^(n/2)). · Wrong: "because merge sort is n log n" — an upper bound for one algorithm is not a lower bound for all.
- **A4-P5** — Expected: n appends copy at most 1 + 2 + 4 + … + n < 2n elements in total, plus n writes, so under 3n work: O(1) amortized (aggregate method). · Wrong: "O(n) per append because resizing copies everything" — true for the resizing append, not averaged over the sequence.
- **A4-P6** — Expected: invariant "when a vertex is extracted, its distance is final": if a shorter path existed, it would leave the extracted set at some vertex y with d(y) ≤ that path's length < d(u), so y would have been extracted first — contradiction, which needs non-negative weights. Counterexample: s→a (2), s→b (3), b→a (−2): Dijkstra fixes a at 2, but s→b→a costs 1. · Wrong: "it fails because of cycles" — this counterexample has no cycle.
- **A4-P7** — Expected: distance 3 (k→s substitution, e→i substitution, insert g). · Wrong: 2 — misses the final insertion (the strings have lengths 6 and 7).
- **A4-P8** — Expected: a given bit stays 0 after kn insertions with probability (1 − 1/m)^(kn) ≈ e^(−kn/m); a false positive needs all k bits set: (1 − e^(−kn/m))ᵏ. With m/n = 10, k = 7: (1 − e^(−0.7))⁷ = (1 − 0.4966)⁷ = 0.5034⁷ ≈ 0.0082 (about 0.8%). · Wrong: "no false negatives, so no false positives" — Bloom filters have false positives only.
- **A4-P9** — Expected: a certificate (an assignment of items to k bins) is checked in polynomial time by summing each bin, so the problem is in NP; it is NP-complete (reduction from partition), so no polynomial exact algorithm is known, and schedulers use heuristics such as first-fit or scoring with bounded quality. · Wrong: "NP means not polynomial" — NP is nondeterministic polynomial time; P ⊆ NP.

**A5**
- **A5-P1** — Expected: transmission 12,000 bits / 10⁷ b/s = 1.2 ms; propagation 2 × 10⁶ m / 2 × 10⁸ m/s = 10 ms. · Wrong: adding them as "bandwidth delay" — they are different quantities; one depends on the link rate, the other on distance.
- **A5-P2** — Expected: L/R = 12,000 / 10⁹ = 12 µs; U = 0.012 / (30 + 0.012) ≈ 0.0004 (0.04%). Pipe = R × RTT = 10⁹ × 0.03 = 3 × 10⁷ bits = 2,500 packets, so a window of about 2,501 packets (the sender needs (RTT + L/R)/(L/R) packets in flight). · Wrong: "1 Gb/s link, so 1 Gb/s throughput" — stop-and-wait idles for a whole RTT per packet.
- **A5-P3** — Expected: with k = 4 and window 3, the sender sends 0,1,2; the receiver ACKs all and moves its window to 3,0,1; all ACKs are lost; the sender retransmits packet 0, which the receiver accepts as the new packet 0. With window ≤ k/2 the old and new windows never overlap. · Wrong: "any window below k is fine" — that is the Go-Back-N bound (k − 1), not selective repeat.
- **A5-P4** — Expected: Estimated = 0.875 × 100 + 0.125 × 140 = 105 ms; Dev = 0.75 × 10 + 0.25 × |140 − 100| = 7.5 + 10 = 17.5 ms; timeout = 105 + 4 × 17.5 = 175 ms. (RFC 6298 updates the deviation with the old estimate, as here.) · Wrong: timeout = 140 ms — using the last sample alone.
- **A5-P5** — Expected: on the two-flow phase plot, additive increase moves both rates along a 45° line (equal gains) and multiplicative decrease moves them toward the origin (proportional cuts), shrinking the gap; repeated, the operating point converges to the fairness line. Additive decrease subtracts equal amounts, so the gap never shrinks. · Wrong: "AIMD is fair because TCP is fair" — circular.
- **A5-P6** — Expected: converged: A→C cost 2 via B. When B–C breaks, B's direct route to C is gone; B hears A advertise C at cost 2 and sets C at 3 via A; A then updates to 4 via B; they count up by 2 each exchange until the "infinity" limit (16 in RIP). Poisoned reverse (A advertises C at infinity to B) stops this two-node loop. · Wrong: "B learns C is unreachable immediately" — B has no way to know A's route goes through B.
- **A5-P7** — Expected: TCP delivers one ordered byte stream, so a lost segment blocks every later byte, whatever HTTP/2 stream it carries; QUIC orders data per stream, so loss on stream 1 blocks only stream 1. · Wrong: "QUIC is faster because it uses UDP" — UDP gives no ordering at all; QUIC adds per-stream ordering itself.

**A6**
- **A6-P1** — Expected: FIFO completes at 10, 11, 13 → mean 34/3 ≈ 11.33; SJF (1, 2, 10) completes at 1, 3, 13 → mean 17/3 ≈ 5.67. · Wrong: using response time (first run) instead of turnaround (completion − arrival).
- **A6-P2** — Expected: exchange argument — if a longer job runs directly before a shorter one, swapping them lowers the shorter one's completion time by the longer one's length and raises the longer one's by the shorter one's length, a net decrease; so any order that is not shortest-first can be improved. · Wrong: "SJF is fastest" without an argument — and it is optimal for mean turnaround only, not for response time or fairness.
- **A6-P3** — Expected: 2³² / 2¹² = 2²⁰ entries × 4 B = 4 MiB. Two-level (10 + 10 + 12 bits): one 4 KiB directory + one 4 KiB second-level table = 8 KiB. · Wrong: 4 KiB — forgets the directory page.
- **A6-P4** — Expected: FIFO 9 faults, LRU 10 faults, OPT 7 faults (this is Belady's string; with 4 frames FIFO gives 10, showing Belady's anomaly). · Wrong: LRU < FIFO "always" — on this string LRU does worse.
- **A6-P5** — Expected: thread s holds A and waits for B; thread t holds B and waits for A — circular wait. Remove circular wait by a global lock order (always A before B). · Wrong: "add a timeout" as the fix — it breaks the deadlock only by failing, and can livelock.
- **A6-P6** — Expected: in ordered mode data blocks are written before the metadata that points to them is committed; if the commit was not reached, the file shows the old size and old contents (the new data is lost), never metadata pointing at garbage. Only `fsync` returning promises durability. · Wrong: "journaling means no data loss" — journaling protects consistency, not un-synced data.
- **A6-P7** — Expected: (5 − 1) × 4 TB = 16 TB usable; survives one disk failure. · Wrong: 20 TB or two failures — parity costs one disk and protects against one.

**A7**
- **A7-P1** — Expected: I = Ce / (Ca + Ce) = 9 / 12 = 0.75 — unstable; stable packages should not depend on it (the stable-dependencies principle). · Wrong: I = 3/12 = 0.25 — swaps incoming and outgoing.
- **A7-P2** — Expected: it strengthens the precondition (rejects 0 and negatives the base accepted) and weakens the postcondition (may return negatives); both break the rule. · Wrong: "only the precondition" — callers relying on a non-negative result also break.
- **A7-P3** — Expected: source: the payment provider; stimulus: it stops responding; artifact: the checkout service; environment: normal operation, peak load; response: accept the order, queue the payment for retry, tell the user it is pending; measure: 99.9% of checkouts complete in under 2 s while the provider is down, and 100% of queued payments are retried within 1 hour of recovery. · Wrong: "the system should be highly available" — not measurable, so not a scenario.
- **A7-P4** — Expected: states per process {idle, waiting, critical}; safety: never both critical; liveness: a waiting process eventually enters. A timeout-based lock (a lease) can violate safety if a paused holder resumes after its lease expired while another holder entered — hence fencing tokens. · Wrong: "a timeout violates liveness" — timeouts help liveness; they endanger safety.
- **A7-P5** — Expected: PUT sets state s ↦ s[42 := v]; applying it twice gives the same state as once (f(f(s)) = f(s)). POST s ↦ s ∪ {new item with a fresh id}; twice adds two items. · Wrong: "PUT is idempotent because it returns the same response" — idempotency is about the effect on state, not the response.

**A9**
- **A9-P1** — Expected: p: events 1, 2 (send m1, timestamp 2); q: event 1 (ts 1), receive m1 → max(1, 2) + 1 = 3, send m2 → 4; r: events 1–3 (ts 1–3), receive m2 → max(3, 4) + 1 = 5. Concurrent: p's event 1 and r's event 1 (no path of messages or local order links them). · Wrong: naming q's receive and p's send as concurrent — the message orders them.
- **A9-P2** — Expected: two processes with no messages: p's event with C = 1 and q's event with C = 2 have C(a) < C(b) but are concurrent. Vector clocks give V(a) < V(b) if and only if a → b. · Wrong: "Lamport clocks capture causality both ways".
- **A9-P3** — Expected: a read quorum and a write quorum are subsets of N replicas with |R| + |W| > N; if they were disjoint they would hold R + W > N distinct replicas — impossible (pigeonhole). N = 5, W = 3, R = 2: 5 = 5, not greater, so a read of 2 may miss all 3 written replicas — no guarantee. · Wrong: "W is a majority, so reads see it" — the read quorum must also intersect it.
- **A9-P4** — Expected: two replicas G1 and G2, partitioned. A write of v1 goes to G1 and must complete (availability); a later read at G2 must also return (availability) but cannot learn v1 (the partition drops all messages), so it returns the old value, and the execution is not linearizable. · Wrong: "CAP means pick two of three at all times" — the choice is forced only during a partition.
- **A9-P5** — Expected: participants that voted yes are "prepared" — they may neither commit nor abort on their own, because the coordinator may have decided either way; they block holding locks until the coordinator recovers (or, with a cooperative termination protocol, until some participant knows the outcome). · Wrong: "abort after a timeout" — safe only for a participant that has not yet voted yes.
- **A9-P6** — Expected: an entry from an old term stored on a majority can still be overwritten by a later leader that never had it (the Figure 8 scenario in the Raft paper); Raft therefore commits by counting replicas only for entries of the leader's current term — earlier entries become committed indirectly by the log-matching property. · Wrong: "majority replication always means committed".
- **A9-P7** — Expected: merge(a, b)[i] = max(a[i], b[i]); max is commutative, associative and idempotent element-wise, so the merge is too; the value is Σ merged[i]. · Wrong: merging by summing counts — not idempotent, so a re-delivered state double-counts.
- **A9-P8** — Expected: Byzantine: 3f + 1 = 7. Crash with majority quorums: 2f + 1 = 5. · Wrong: 5 for Byzantine — a majority is not enough when faulty nodes can lie.
- **A9-P9** — Expected: with 50 parallel calls, P(at least one over p99) = 1 − 0.99⁵⁰ ≈ 39.5%, so the tail of one call sets the typical latency of the whole request. Hedging after the p95 duplicates about 5% of calls (the extra load) and cuts the tail because the slow copy is usually a transient delay. · Wrong: "hedging doubles the load" — only calls still pending at the hedge point are duplicated.

**A10**
- **A10-P1** — Expected: fail-safe defaults (a shipped default grants access); complete mediation (every access must be checked, cached or not); open design (security must not depend on a secret design). · Wrong: least privilege for the cache — the flaw is the missing check, not the size of a privilege.
- **A10-P2** — Expected: BLP: read up Top-Secret — no (no read up); write down to Confidential — no (no write down). Biba: read down (lower integrity) — no; write up — no; Biba allows reading up and writing down. · Wrong: "Secret can read Confidential and also write it" — writing down leaks under BLP.
- **A10-P3** — Expected: A starts a session with the intruder I; I re-encrypts A's nonce and identity for B, posing as A; B's reply goes to A through I; A decrypts B's nonce and returns it to I, who completes the run with B as "A". Lowe's fix puts B's identity in message 2, so A sees the reply is from B, not I. · Wrong: "the attacker breaks the encryption" — no cryptography is broken; the protocol logic is.
- **A10-P4** — Expected: canary — detects overwrites of the return address by a stack buffer overflow; ASLR — makes code and data addresses unpredictable, defeating hard-coded jump targets; non-executable stack — stops injected shellcode from running (which pushed attackers to code-reuse attacks). · Wrong: "ASLR prevents buffer overflows" — it makes exploiting them harder; the overflow still happens.
- **A10-P5** — Expected: PA: Viewer→{read}; Editor→{read, write}; Owner→{read, write, set-policy}; UA: user→Editor. Assigning Owner would add set-policy, which the need does not include. · Wrong: assigning Owner "to be safe" — violates least privilege.

**A11**
- **A11-P1** — Expected: the file's blob hash changes, so its tree's hash changes, so that commit's hash changes; every later commit names its parent's hash, so each of their hashes changes up to the current one (a Merkle chain). · Wrong: "Git recomputes hashes on push" — the hashes are content-derived, not recomputed by a server.
- **A11-P2** — Expected: 6 / 40 = 15%. · Wrong: counting incidents per day, or dividing by total incidents.
- **A11-P3** — Expected: whether you distribute the software (copyleft obligations are usually triggered by distribution, and for some licences by network use); whether the licence is compatible with your own and your other dependencies' licences; what the change requires you to publish. · Wrong: "licences only matter for open-source projects".

**B–D tracks**
- **B2-P1** — Expected: sensitive instructions that are not privileged break the trap-and-emulate condition (sensitive ⊄ privileged); VT-x and AMD-V added a guest mode in which those instructions trap to the hypervisor. · Wrong: "x86 was too slow to virtualize" — the obstacle was correctness, not speed.
- **B3-P1** — Expected: 1000 / 1002 ≈ 0.998004 (99.80%); two independent in parallel: 1 − (1 − 0.998004)² = 1 − 0.001996² ≈ 1 − 3.98 × 10⁻⁶ ≈ 0.999996. · Wrong: 0.998² — that is two in series, where both must be up.
- **B3-P2** — Expected: all three must fail in the window: 0.001³ = 10⁻⁹. · Wrong: 3 × 0.001 — that is the chance that at least one fails.
- **B4-P1** — Expected: the commitment costs 0.63 of the full-time on-demand price; on-demand costs u × full price; it wins when u > 0.63 (63%). · Wrong: 37% — confuses the discount with the break-even utilization.
- **B5-P1** — Expected: in the denied project: deny (explicit deny overrides the inherited allow); in the sibling project: allow (inherited from the folder). · Wrong: "the folder allow wins because it is higher in the hierarchy".
- **C2-P1** — Expected: a level-triggered controller compares desired with observed state on every pass, so after restarting it sees the net difference and acts on it; an edge-triggered handler acts on each event and misses the three that arrived while it was down. · Wrong: "the events are queued for it" — watches can expire; the design must not depend on seeing every event.
- **C6-P1** — Expected: percentiles are not linear, so their mean is not the pooled percentile; the fleet p99 needs the pooled distribution — the raw samples or histograms with the same bucket boundaries, merged by adding counts. · Wrong: "take the max, 200 ms" — the max of per-host p99s is not the fleet p99 either.
- **C7-P1** — Expected: 0.001 × 30 × 24 × 60 = 43.2 minutes. · Wrong: 4.32 minutes — a factor of ten, from reading 99.9% as 0.01% allowed.
- **C7-P2** — Expected: burn rate = 0.0144 / 0.001 = 14.4; budget spent = 14.4 × (1/720) = 0.02 = 2%. · Wrong: 1.44% spent — confuses the error ratio with the budget fraction.
- **D1-P1** — Expected: the likelihood of labels yᵢ ∈ {0, 1} under predictions pᵢ is Π pᵢ^yᵢ (1 − pᵢ)^(1 − yᵢ); its negative log divided by n is −(1/n) Σ [yᵢ log pᵢ + (1 − yᵢ) log(1 − pᵢ)], the mean cross-entropy; the log is monotone, so minimizing one maximizes the other. · Wrong: "cross-entropy is used because it is convex" — convexity is a separate property (it holds for logistic regression, not for deep networks).
- **D2-P1** — Expected: u = wx + b = 7; y = u²; ∂y/∂w = 2u × x = 2 × 7 × 3 = 42. · Wrong: 2wx = 12 — drops b and the chain through u.