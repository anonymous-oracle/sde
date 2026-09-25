Authored §0 text for the six parts under decision D18 (2026-09-25): the rules, the session protocol, the learner's
preferences, Lab Safety and the ownership register now live once, in the course guide, so each part's §0 keeps only
what is particular to that part. r7_guide.py puts each section in place of the lines it replaces (they go to records/).
Text above the first key is not used.

@@@ cur-note
> **Note:** the rules every part follows are kept once, in the course guide. They are the parts and the stitch rule (rule 0.1), the learner's teaching preferences (rule 0.2), the ownership register (rule 0.3), the Suite Teaching Contract (rule 0.4) and Lab Safety (rule 0.5). This part keeps the scope, the certification notes, the university and textbook alignment (§0.6) and the plan.

@@@ pri-s0
## 0. Read this first — what this part adds

This part follows the rules of the course guide (rules 0.1–0.5). This section holds only what is particular to it.

### 0.1 What this part owns

The primer teaches *what* scalable systems are made of, in vendor-neutral words: load balancer, cache, queue, shard. The main course teaches *which cloud resources* those words become, and the exam-grade judgment around them. This part owns the system-design layer of every shared idea: trade-offs and disadvantages, numbers, interview framing, and the GCP resource. It also owns the primer's problems (P01–P08, O01–O07, Q01–Q23), the Terraform labs TF-1…TF-7 and the primer's reference tables (§6). Every primer concept arrives with its GCP resource attached, and every GCP resource with the primer's trade-off reasoning.

### 0.2 Rules particular to this part

1. **Other clouds come from main course Part VIII.** The primer's own examples are AWS-flavoured (S3, RDS, ELB, CloudFront, ElastiCache, SQS, Route 53, DynamoDB, Redshift, CloudWatch). Each concept below translates them to GCP, and Part VIII gives the Azure side, so no service is taught three times.
2. **Problems are checkpoints, not detours.** A problem from the ladder (§4.5) runs only when its readiness gate (§4.2, §4.3) is met, and it introduces at most one new concept (rule 0.4.8).
3. **Numbers and application.** In this part's layer of a session (rule 0.4.2), the Numbers step uses §6.1–§6.3, and the application item is a ladder problem or the "Users+" step of P08 that introduces the concept.
4. **Primer vintage.** The primer is 2017-vintage. Where industry has moved on, the concept block says so under **Modern note** (rule 0.4.11). Primer numbers ("primer:") are quoted from the primer; GCP details are this part's own and carry `(verify)` where needed.

@@@ sql-s0
## 0. Read this first — what this part adds

This part follows the rules of the course guide (rules 0.1–0.5). This section holds only what is particular to it.

### 0.1 What this part owns

The main course owns the order and the module spine. It deliberately does not own the SQL *language* end to end, the pre-SQL mathematics a learner may lack, the theory tier behind the engine slices (serializability, ARIES, join-cost formulas, Selinger-style planning), modelling method, analytics dialects, or a large body of query-writing practice. This part supplies exactly those, and hangs each piece on the main-course module that needs it, **at the moment that module needs it**.

It owns SQL-language mastery (SL), relational theory (RT), the CS theory tier under the slices (CS), data-design method (DD) including the ledger rules (DD-03) and point-in-time correctness and leakage (DD-05), operating-a-database craft (OD) including Cloud SQL (OD-11), migrations as jobs (OD-08), the cursor pager (OD-09) and pool arithmetic (OD-03), analytics and dialect craft (AN) including BigQuery operations (AN-02), pre-SQL prerequisites (PQ), the exercise ladder (§6), and the engine slices DB-1…DB-10 and their toys (§4.0). Other parts own the Firestore, Bigtable and store-choice material (primer SD-22, SD-23, SD-25), outbox and inbox (A9 theory; design-patterns ARCH-11 shape), payment-flow abuse (cyber AB-06) and billing-export SQL (B4); rule 0.3 has the full register.

### 0.2 Rules particular to this part

1. **No second toy.** Where a §4.0 slice toy exists (WAL codec, slotted page, B-tree, iterator executor, visibility simulator), this part never asks for a second toy. It adds the analytic layer (formulas, schedules, cost models) that the toy's tests do not reach.
2. **No later system as a prop** (rule 0.4.6): no Spanner interleaving in the first Postgres transcript, no full PITR runbook before its owner, no Cloud SQL HA as a "known" prop before its OD-11 session. If an exercise needs machinery not yet unlocked, postpone the exercise or teach the machinery first.
3. **Lens defaults** (rule 0.4.11): Lens-2 is local Docker Postgres. Cloud SQL, AlloyDB, the Spanner emulator and the BigQuery sandbox are used only when Lab Reality allows, and are destroyed the same day (rule 0.5). Lens-3 is PCA storage design and the Professional Data Engineer and Database Engineer overlap.
4. **Fingerprints, not eyeballs.** Each read-only exercise has a *golden*: `rows:hash`, computed by the lab kit (`lab.chk`). Two queries give the same answer if and only if their fingerprints match. **Goldens are valid only for seed v1 on PostgreSQL 15.x with `timezone = UTC` and the `C` collation.** If any of those change, regenerate the goldens; do not "fix" a learner's query to match a stale golden.
5. **Predictions to make** (rule 0.4.4): the result shape, the row count, the plan shape or the isolation outcome, one line, before the run.
6. **Numbers and application.** In this part's layer of a session (rule 0.4.2), the Numbers step is one estimate (rows per page, index height, pool arithmetic, bytes scanned), and the application item is one item from §6 or §7 at the current rung. Skip-tests and tiers are in §5. The ledger records companion items under their IDs (`SL-08`, `SQL-E6.2`).

@@@ dp-s0
## 0. Read this first — what this part adds

This part follows the rules of the course guide (rules 0.1–0.5). This section holds only what is particular to it.

### 0.1 What this part owns

This part supplies one thing that main-course module **A7 (Software Architecture & APIs)** names but does not detail: formal OOP design theory. That is SOLID, GRASP, the GoF catalogue, Clean, Hexagonal and Onion architecture, DDD building blocks, and the enterprise and microservice patterns layered on top. Its modules are taught when A7 is reached, and the items gated behind A9 when A9 is reached (§2).

### 0.2 Rules particular to this part

1. **A3 already taught operational OOP** (class, object, `self`, constructor, inheritance mechanics through the `Dog` example). This part never re-derives it; every module below assumes it and recalls it in one clause.
2. **System-level twins are cross-referenced, not re-taught.** Where a pattern's core idea overlaps a primer concept (Observer and Pub/Sub's fan-out; Strategy and SD-10's load-balancer algorithms), this part teaches the OOP-level mechanism and names the primer's system-level version.
3. **Order is enforced** (§10): Foundations (§3) → SOLID (§4) → GRASP (§5) → GoF catalogue (§6) → Architecture (§7) → Anti-patterns (§8). A pattern is never taught before the principle it embodies: Strategy is not taught before Open/Closed, because Strategy *is* Open/Closed made concrete.
4. **Every pattern gets four things, always:** the problem it solves, stated before the solution (a pattern without its pain is cargo-cult programming, AP-06, in the making); its formal structure, with GoF's own participant names; its trade-offs, named rather than sold; and at least one real industry example, from a cloud SDK, a popular library, or a framework the course touches elsewhere.
5. **Distinguish pattern from principle from architecture**, explicitly, whenever one could be mistaken for another. A *principle* (SOLID, GRASP) is a rule for arranging responsibility. A *pattern* (GoF) is a named, reusable solution shape to a recurring problem, usually at class or object level. An *architecture* (Clean, Hexagonal, the microservice patterns) is a system-level arrangement, often built from several patterns and principles at once. Conflating the three is the most common shallow-learning failure in this material; call it out on sight.
6. **Flags** (rule 0.4.11): `(debated)` marks where the industry itself disagrees, for example whether Singleton is a pattern or an anti-pattern in modern practice. `(GoF)` marks a definition quoted or adapted directly from the 1994 book, since its precise wording is often what is tested.

@@@ sec-s0
## 0. Read this first — what this part adds

This part follows the rules of the course guide (rules 0.1–0.5). This section holds only what is particular to it.

### 0.1 What this part owns

The main course owns the roadmap spine: what to learn, in what order, tied to the certifications (PCA, Cloud Security Engineer, Network Engineer, SecOps, SCS-C03 and the rest), and the provider service maps. It lists security topics at outline depth (A5 networking, A10 security and cryptography fundamentals, B1 shared responsibility, B5 the IAM model, Track C container and Kubernetes hardening, the Phase 4 GCP security services), and owns their service vocabulary (IAM, Armor, VPC-SC, KMS, SCC, SecOps). This part owns what the title block lists, and hangs each piece on the main-course section that needs it, **when that section is taught**.

### 0.2 Rules particular to this part

1. **When this part rides along** (rule 0.1): whenever **A5**, **A7 (auth patterns)**, **A10**, **B1 (shared responsibility)**, **B5**, **C1/C2 hardening**, **Phase 4 Networking/Security**, or the **Cloud Security / Network / SecOps** certification tracks are taught, every module bound to them in §2 is taught in the same session.
2. **No later control as a prop** (rule 0.4.6): do not use a later control (VPC-SC, Confidential VM, Binary Authorization) as a "known" prop before its main-course section has been covered. Postpone the exercise or teach the prerequisite first.
3. **Predictions to make** (rule 0.4.4): the blast radius or the control placement, before the answer is revealed.
4. **Lens defaults** (rule 0.4.11): Lens-1 names the GCP resource and its AWS and Azure twins from the main course's mapping tables (Part VIII). Lens-2 touches it through a local vulnerable-by-design fixture or a credits-safe lab (rule 0.5). Lens-3 is Cloud Security Engineer, PCA security and SCS-C03 depth.
5. **Keys are qualitative.** No invented lab-database goldens.
6. **Numbers and application.** In this part's layer of a session (rule 0.4.2), the Numbers step is one estimate (the QPS to throttle, a key size, a blast radius, an incident's RTO or RPO), and the application item is one card from §5. Skip tests and tiers are in §4.

@@@ go-s0
## 0. Read this first — what this part adds

This part follows the rules of the course guide (rules 0.1–0.5). Rule 0.4.9 (the implementation language) is the rule this part serves. This section holds only what is particular to it.

### 0.1 What this part owns

This part supplies one thing the main course needs everywhere but teaches nowhere: **the implementation language**. It teaches Go as a language — its grammar, its semantics, its runtime and its toolchain — and, at every construct, what it does *differently* from Python, Java, C and JavaScript, because the bugs a newcomer writes in Go are almost all habits carried across from another language. Its last two modules, GO-28 and GO-29, apply the language to the two things most services must get right, authentication and payment integration. Each piece is built from scratch against its published test vectors, so the mechanism is visible. The attacks, the cryptography and the ledger rules stay with their owners (rule 0.3); this part owns only the Go rendering of each: the syntax, the semantics, the runtime behaviour and the idiom.

### 0.2 Rules particular to this part

1. **Binding.** The language core (GO-01…GO-14) is the Go block of A3. Every later module binds where its first real use is (§2).
2. **The unlock list is §0.3.** A construct is usable only from its module on (rule 0.4.9). The first use of each construct carries its **unlock block**: the grammar or function signature, exactly; the semantics, including the zero value and what is copied and what is shared; the runtime and memory behaviour — where the value lives (stack, heap, inside a header), what can block, what can panic, what it costs; and one precise contrast with Python, Java, C or JavaScript, with the bug that habit causes here.
3. **Predict → run** (rule 0.4.4): after the unlock block, a four-to-ten-line program whose output the learner predicts before running it. Then the idiom, as the standard library actually uses it.
4. **Every module carries a contrast.** Each module's **Contrast** line names what Python, Java, C and JavaScript do instead, and the exact bug the other habit produces in Go. §9 collects them into one atlas for revision; the atlas never replaces the teaching. A carried-over habit the learner shows goes into the misconception register (rule 0.4.5).
5. **Mechanism before idiom.** An idiom ("accept interfaces, return structs", "don't communicate by sharing memory") is taught only after the mechanism that justifies it, and always with the case where it is wrong.
6. **Version baseline.** The baseline is Go 1.27, the version the learner's own module declares (rule 0.4.9). A construct newer than Go 1.21 names the release that introduced it, because a `go` line older than that release in `go.mod` turns the construct off (the compiler says so). `(checked on 1.27.1)` marks a behaviour run on Go 1.27.1 (linux/amd64) on 2026-09-24, while this part was written.
7. **Involved problems** (rule 0.4.9): each is `GO-Pnn`, the card's last line, with its rubric in §10.2. Before GO-20 is taught, its checks are a self-checking `main` that prints one PASS or FAIL line per case; from GO-20 on, they are `go test` tests. It uses only constructs already unlocked, and names any download first. Two problems wait for a later module: GO-01's, GO-02's and GO-03's are set at the close of A3.G1 (they need GO-04's loops), and GO-15's after GO-16 (a leak needs a channel).
