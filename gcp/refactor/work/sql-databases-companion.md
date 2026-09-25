# The SQL & Databases Companion — GCP-Native Edition
Companion to the main course, "The Consolidated Cloud Mastery Curriculum".
Sibling of the System Design Primer companion (its SD-13 … SD-27 own the *scale-out and interview* layer of databases; this file owns *SQL semantics, relational and storage theory, schema craft, and a query-writing exercise ladder*).
Sources: PostgreSQL documentation · Silberschatz/Korth/Sudarshan *Database System Concepts* (`TB-DB-001`) · Rogov *PostgreSQL 14 Internals* (`TB-DB-002`) · Kleppmann *Designing Data-Intensive Applications* (`TB-DIST-001`) · CMU 15-445/645 (`SRC-DB-002`) · Google Cloud documentation for Cloud SQL, AlloyDB, Spanner, BigQuery. Built September 21, 2026. **Every reference query and every golden value in §6 and Appendix K was executed on PostgreSQL 15.8 against the deterministic "seed v1" of §3** — nothing in the exercise ladder is typed from memory.
> **Note:** the `TB-…` / `SRC-…` labels in the line above are this file's bibliography keys; the books and courses are named in full beside them.

---

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

### 0.3 Notation

- `PQ-nn` prerequisites · `RT-nn` relational theory · `SL-nn` SQL language · `CS-nn` computer science under the engine · `DD-nn` data design · `OD-nn` operating databases · `AN-nn` analytics & other engines. All are in §4.
- `SQL-E<level>.<n>` query-writing exercises (§6, levels 1–14; **TX** and **PX** are *labs* in §7) · `SQL-Z0.n` level-0 paper drills · `TD-n` theory drills · `PX-n` plan-prediction cards · `TX-n` transaction labs · `BH-n` bug-hunts · `DT-n` dialect-translation drills · `SCH-n` schema-design cases · `SQL-CAP1–SQL-CAP4` capstones · `TF-DBn` Terraform database exercises.
- Main-course IDs (`A1…D4`, `Phase 4`, the Part V category IDs `V-…`) are stitch tags into the main course. `DB-1 … DB-10` are this file's engine slices (§4.0). `SD-…` are primer-companion IDs. `TB-…`/`SRC-…` are this file's bibliography labels (title block).
- Tiers: `SQL-T-HS` high-school · `SQL-T-UG` undergraduate · `SQL-T-GR` graduate — the depth tier of a theory item or gate (§2 rows for A2 and A8 + A9).
- **The lab database** (§3) is a small multi-tenant storefront — tenants, users, categories, products with effective-dated prices, stock, orders and order lines, payments, shipments and reviews — plus a semi-structured event stream and a deliberately messy staging table.


---

## 1. Coverage ledger — every part of "SQL databases + underlying CS + prerequisites", and where it lives

| Area | Content | Covered in |
|---|---|---|
| **Pre-SQL prerequisites** | sets/relations/functions/bags · propositional & predicate logic, three-valued logic · counting & cardinality · data types, encodings, integer vs decimal vs float · time & time zones · files, CSV/JSON · CLI, `psql`, Docker Postgres · Python DB-API and parameter binding · big-O, hashing, trees, sorting, binary search · storage hierarchy and units | PQ-01 … PQ-08, SQL-Z0.1 … SQL-Z0.8 |
| **Relational theory** | relational model, keys, integrity · relational algebra (set and bag) · tuple/domain calculus, safety, Codd equivalence · functional dependencies, closure, cover · 1NF … BCNF, 4NF/5NF-lite, lossless & dependency-preserving decomposition · ER → tables · query equivalence & rewrite rules | RT-01 … RT-08, TD-1 … TD-8 |
| **SQL language** | DDL, types, constraints · logical evaluation order · NULL & 3VL · joins (inner, outer, cross, self, semi, anti, lateral, non-equi) · aggregation, grouping sets · subqueries, EXISTS, ALL/ANY, division · set operations · CTEs, recursion · window functions and frames · DML, RETURNING, upsert, MERGE · views, materialized views, functions, triggers · dates, time zones, JSON, text, regex · security in SQL (GRANT, RLS, injection) · dialects and the standard | SL-01 … SL-14, SQL-E1 … SQL-E10, SQL-E13 |
| **CS under the engine** | storage layouts and page arithmetic · B-tree/B+tree math, hash, LSM, bitmap, GIN/GiST/BRIN · buffer caching theory · external sort, join and aggregation algorithms with I/O cost · cardinality estimation and join ordering · concurrency-control theory (conflict serializability, 2PL, timestamp ordering, MVCC/SI, SSI) · recovery theory (WAL, steal/no-force, ARIES) · replication logs, consensus, 2PC, consistency models · columnar/vectorised execution and compression · complexity of queries, recursion, expressiveness | CS-01 … CS-11, TD-9 … TD-16, TX-1 … TX-8, PX-1 … PX-11 |
| **Data design** | conceptual → logical → physical · keys (natural, surrogate, UUID, snowflake) · money, units, time · hierarchies & graphs in SQL · temporal data & SCD · JSONB vs relational · soft delete, audit, history · denormalisation with ADRs · multi-tenancy · partitioning & sharding-key design · schema evolution (expand/contract) · data quality as constraints | DD-01 … DD-13, SCH-1 … SCH-6, SQL-E10 |
| **Operating databases** | indexing strategy & `EXPLAIN` workflow · statistics & slow-query observability · connection pooling · backup/restore/PITR drills · replication & read-your-writes · vacuum/bloat · retention & partitions · migrations tooling & testing · application data access (N+1, ORMs, prepared statements, injection, pagination) · testing SQL | OD-01 … OD-11, PX-1 … PX-11, BH-1 … BH-6, TF-DB1 … TF-DB6 |
| **Analytics & other engines** | OLTP vs OLAP, star/snowflake · BigQuery/GoogleSQL dialect · cohorts, funnels, sessionisation, retention · approximate aggregation · Spanner SQL · NoSQL query models vs SQL · search & vectors in SQL | AN-01 … AN-07, SQL-E6, SQL-E13, DT-1 … DT-8 |
| **Query-creation exercise bank** | 14 levels, ~120 specified items with traps, goldens and instructor keys | §6, Appendix K |
| **Engine-behaviour labs** | isolation anomalies, deadlock, SKIP LOCKED, oversell under concurrency, EXPLAIN predictions | §7 (TX-1 … TX-8, PX-1 … PX-11) |
| **Capstones** | fault-injected audit, cash-basis revenue, checkout schema + concurrency, slow-query rescue | §9 (SQL-CAP1–SQL-CAP4) |
| **Rosetta & IaC** | Postgres ↔ Cloud SQL ↔ AlloyDB ↔ Spanner ↔ BigQuery ↔ MySQL ↔ SQL Server ↔ SQLite ↔ Oracle · Terraform for Cloud SQL / AlloyDB / Spanner / BigQuery | §8 |

Counts (verified by the generator that produced §6): **Level 0** 8 paper drills · **theory** 16 drills · **query exercises** SQL-E1–SQL-E10, SQL-E13, SQL-CAP1–SQL-CAP2, SQL-CAP4 → 111 items (all with fingerprints) · **plan predictions** 11 · **transaction labs** 8 · **bug-hunts** 6 · **dialect drills** 8 · **schema cases** 6 · **capstones** 4.

---

## 2. Stitch table — teach these together

Each main-course module on the left is taught **with** the companion modules on the right, in the same session (rule 0.1). "Checkpoint" is the exercise (or drill) to run once that module and its stitched concepts are done — issued **one at a time**, per rule 5.

| Main-course module | Companion modules taught in the same session | Checkpoint |
|---|---|---|
| **A2** (math recall; PQ-01/PQ-02 teach the sets, logic and counting SQL needs) — *Tier SQL-T-HS/SQL-T-UG* | PQ-01 sets, relations, functions, **bags** · PQ-02 predicate logic and **3-valued logic (preview)** · counting/cardinality bounds of joins (RT-01) | SQL-Z0.1 … SQL-Z0.6 |
| **A4** (recall: structures, hashing, complexity) | PQ-07 sorting, hashing, trees, binary search *as the raw material of access paths* · CS-02 B-tree fan-out and height arithmetic (formula only — the toy is DB-6) | SQL-Z0.7, TD-10 |
| **A1/A2** (recall: units, orders of magnitude) | PQ-08 storage hierarchy, page/row arithmetic · latency numbers (recall of primer SD-37) | SQL-Z0.8 |
| **A2** (floating point) | PQ-03 `numeric` vs float, rounding modes (half-up vs banker's), integer money — *recall IEEE from A2; add decimal semantics* | SQL-E2.1, SQL-E2.7 |
| **A8 + A9** — DB theory (with the A8 SQL sessions) | RT-02 algebra · RT-03 calculus/safety (SQL-T-GR) · RT-04/05 FDs & normal forms · RT-08 rewrites · CS-05 serializability & SI · CS-06 recovery · CS-08 cardinality. **SQL-T-UG gate items** map to TD-2 (push σ through ⋈), TD-1/2/3 (keys, FDs, 3NF), TD-8 (dirty-read & lost-update schedules), TD-12 (WAL durability). **SQL-T-GR gate items** map to TD-9 (snapshot visibility), TD-13 (selectivity estimate) | TD-1 … TD-16 (as gated) |
| **A3 + A6** (computer, OS, CLI, Git, JSON, HTTP) | PQ-04 files, CSV/JSON/JSONL, encodings (UTF-8, BOM) · PQ-05 `psql`, env vars, Docker basics for a Postgres container | SQL-E0 warm-up: load the lab (§3) |
| **C1** Docker/OCI, container contract | PQ-05 `docker compose` Postgres with a named volume and a healthcheck (the lab in §3.2) | lab loads, fingerprints match |
| **C4** CI | OD-10 SQL tests in CI: a Postgres service container, seed v1, fingerprint assertions, migration up/down | run SQL-E3.2 as a CI test |
| **C4 + C5** CD, IaC | OD-08 migration ordering in deploys · §8.2 Terraform DB exercises | TF-DB1 … TF-DB2 (plan only) |
| **A7** architecture documentation (HLD/LLD contract, ADR template, NFR table) | DD-01 conceptual → logical → physical; **schema ADRs** ("I pick X because Y, I accept Z") · DD-12 constraints as spec | SCH-1 |
| **B5** IAM (+ **OD-11** IAM DB auth) | SL-13 database roles vs IAM principals, `GRANT`/`REVOKE`, least privilege | SQL-E10.6 (RLS) after A10 |
| **C6** observability day one | OD-02 logs, slow-query log, `pg_stat_statements`, Query Insights vocabulary | PX-1 |
| **B3** HA & autoscaling | OD-03 pool arithmetic under autoscaling (instances × pool ≤ `max_connections`), with the OD-03 worksheet | TX-8 |
| **A8 — SQL design track** (concept, then lab; engine slices §4.0) | **The core binding.** SL-01 … SL-12 · RT-01 … RT-07 · DD-01 … DD-06, DD-12 · OD-01 · CS-01 … CS-08 — paired slice by slice with DB-1 … DB-10 (§2.1 table below) | SQL-E1 → SQL-E10 by level (§6 gates); BH-1 after SQL-E3.5 |
| **A8** + **V-STOR** GCP relational offerings (decision table) | AN-01 OLTP/OLAP · DD-08 JSONB vs relational · §8.1 Rosetta table | DT-1 |
| **V-STOR** Cloud SQL setup (required procedure) | **OD-11** provisioning, connectivity, security, operations · OD-03 pooling & pool math · OD-04 backup/restore drills *as runbook (DB-10 owns the toy)* · OD-05 replicas & read-your-writes · SL-13 privileges · §8.2 Terraform | TF-DB1, TX-8, BH-5 |
| **A8** (NoSQL) + **V-STOR** Firestore (primer SD-22) | AN-06 the *same question* in Firestore and SQL — where the document model wins and loses | DT-7 |
| **V-STOR** Cloud Storage | PQ-04 `COPY`/import & export of CSV/JSON through GCS; encoding and NULL-vs-empty pitfalls | SQL-E8.8 – SQL-E8.10 |
| **A8** + **C4** config, migrations, jobs | DD-11 expand/contract with **lock levels** · OD-08 migrations as jobs, tooling & testing (dirty state, advisory lock) | SQL-E9.6, SCH-4, BH-6 |
| **A9** + **V-STOR** Spanner & NoSQL map (primer SD-25) | AN-05 GoogleSQL/Spanner · DD-13 key design & partitioning · CS-07 TrueTime, 2PC, Paxos groups | DT-6, SCH-5 |
| **A7** software design (repositories; design-patterns Repository, Unit of Work) | OD-09 application data access: N+1, ORM pitfalls, prepared statements, transaction boundaries | BH-3 |
| **A7** async (Pub/Sub, Tasks, Scheduler) | SL-10 idempotent writes: `INSERT … ON CONFLICT`, unique keys; `LISTEN`/`NOTIFY` as the worker wake-up | SQL-E9.3 |
| **A9** + design-patterns **ARCH-11** failure design (outbox/inbox, sagas) | CS-07 why 2PC is not the answer; SL-10 `FOR UPDATE SKIP LOCKED` job claim | TX-5, TX-8 |
| **A10 + B5** authorization · **C1** + **Phase 4 Security** secrets & supply chain | SL-13 RLS, injection, parameterisation, least-privilege roles | SQL-E10.6, BH-2 |
| **A8** ledger and consistency | DD-03 money and ledger rules (integer minor units), DD-07 audit/history · SL-08 running balances · CS-05 isolation for money | SQL-E4.5, SQL-CAP2, BH-4 |
| **Phase 4 Security** data protection (cyber CR-14) | SL-13 column-level encryption (`pgcrypto`), masking views, CMEK vocabulary | SCH-6 |
| **A7** architecture documentation + primer building blocks · HLD evidence packs | DD-01 schema ADRs inside HLD packs; DD-10 denormalisation ADR; **recall** primer SD-13 … SD-19 for scale-out | SCH-2, SCH-3 |
| **A9** scale primitives — cursor pagination · hot partition · pool math · RLS · LSM vs B-tree · schema evolution · idempotency | OD-09 keyset SQL and its index (with the from-scratch pager) · DD-13 hot-key skew query · OD-03 · SL-13 · CS-02 arithmetic · DD-11 | PX-9, SQL-E4.7 |
| **V-STOR** Memorystore | OD-09 cache-aside vs DB read path (query-level vs object-level); *no new concept* | — |
| **V-STOR** Spanner, AlloyDB, Bigtable, BigQuery (ops view) | AN-01 · AN-02 · AN-05 · CS-09 columnar & vectorised execution | DT-1 … DT-6, SQL-E13.3 |
| **V-DATA** Big-data services (BigQuery, Dataform) | AN-02 partition/cluster and bytes scanned · AN-03 cohorts/funnels · AN-04 approximate aggregation · SL-11 views & materialised views | SQL-E6.2, SQL-E6.6, SQL-E13.1 – SQL-E13.3 |
| **D3** features, labels, skew | DD-05 leakage and point-in-time correctness · SL-08 / SL-04: the **SQL shape** of a point-in-time join (LATERAL / range join). | SQL-E6.4, SQL-E13.4, SQL-E13.5 |
| **D4** retrieval, RAG | AN-07 full-text search and vector search in Postgres (`tsvector`, `pgvector`) vs dedicated engines | DT-8 |
| **C6** observability, performance | OD-01/02 plan reading & workload observation · CS-08 · PX-1 … PX-11 | PX-1 … PX-11, SQL-CAP4 |
| **C7** SLO / error budget | OD-05 replication lag as an SLI; recovery-point objective from WAL archiving | BH-5 |
| **B4** FinOps + billing-export SQL | AN-03 window analytics on a *billing-export-shaped* table; AN-02 bytes-scanned cost | DT-4, SQL-E13.1 |
| **Phase 4** case-study capstone (the PCA case studies) | SQL-CAP1 – SQL-CAP4 are its database acceptance tests | SQL-CAP1 – SQL-CAP4 |
| **Phase 4** case-study HLDs (a control-plane store) | DD-09 audit/event log design; OD-08 migrations for the control-plane store | SCH-6 |
| **SQL-SKIP-SQL** SQL & relational correctness (`DB-SQL`) | **Skip-test map:** if the A8 sessions confirmed FDs/joins/transactions/pagination/client hygiene, stamp using SQL-E3.2, SQL-E4.5, SQL-E5.4, SQL-E9.3, TX-2. **Else** run the SQL-SKIP-SQL order = RT-01/04/05 → RT-02 → SL-01/02 → SL-03 → SL-04 → SL-05 → SL-06/09 → SL-08 → TX labs → OD-09 (§2.2 table) | see §2.2 |
| **SQL-SKIP-ENGINE** PostgreSQL internals (`DB-ENGINE`) | **Skip-test map:** residual `EXPLAIN` drills = PX-1 … PX-11; crash/recovery evidence = TD-12 + OD-04 drill. **Else** run the SQL-SKIP-ENGINE order = CS-01 → CS-04 → CS-02 → CS-03 → CS-08 → CS-05 → CS-06 → CS-07 (§2.2) | see §2.2 |
| **Part V cert rows 1, 3, 8** (PCA / PDE / PCDE certs) | PCA 2.2 storage systems: §8.1 + DT-1; PDE: AN-01…AN-04, SQL-E13; Professional Cloud Database Engineer: OD-03…OD-05, TF-DB1… (all `verify` against the live exam guide) | §8 |


### 2.1 A8 slice pairing — the engine slices DB-1 … DB-10 and what rides with each

The §4.0 slice supplies *toy spec, SQL, EXPLAIN prediction, Cloud SQL mapping*. The companion supplies the **SQL ladder rung, the theory tier, and the prediction card**. Teach the pair as **one session**.

| Slice (owner) | Companion theory | Companion SQL rung | Prediction / lab cards |
|---|---|---|---|
| **DB-1** algebra & 3VL | RT-01, RT-02, RT-08 · TD-5, TD-6, TD-7 | SQL-E1.x, SQL-E2.x, SQL-E3.x (joins, anti/semi/outer), SQL-E4.3/SQL-E4.4 set ops | — (predict multiplicity & NULL behaviour per exercise) |
| **DB-2** catalog, tuples, constraints | RT-04/05 (FDs → keys), DD-04, DD-12 · TD-1 … TD-4 | SQL-E9.x (DML), SQL-E10.1 – SQL-E10.6 (constraints as specification) | PX-7 (missing FK index) |
| **DB-3** CTEs, windows, lateral | RT-03 (safety), CS-11 (recursion) · TD-16 | SQL-E4.x, SQL-E5.x, SQL-E6.x, SQL-E7.x | PX-10 (sort node for windows) |
| **DB-4** heap pages & TOAST | CS-01 page arithmetic · SQL-Z0.8 | SQL-E8.5 – SQL-E8.7 (JSONB size intuition) | — |
| **DB-5** buffer pool | CS-04 | — | PX-9 (hit vs read) |
| **DB-6** indexes | CS-02, CS-10 · TD-10 | PX-style workflow (§7.1) | PX-1 … PX-6, PX-9 |
| **DB-7** executor & spill | CS-03 · TD-11 | SQL-E13.x aggregation shapes | PX-7, PX-10 |
| **DB-8** planner statistics | CS-08 · TD-13 | — | PX-8 |
| **DB-9** MVCC, locks, vacuum | CS-05 · TD-8, TD-9, TD-15 | SQL-E9.6 (batching), TX labs | TX-1 … TX-7 |
| **DB-10** WAL, replica, PITR (**OD-11**) | CS-06, CS-07 · TD-12, TD-14 | — | BH-5, OD-04 restore drill, TX-8 |

### 2.2 Parallel calendar — how the companion rides the main course's spine

The main course's spine is Phases 0–3 (Tracks A–D, mostly in parallel) → Phase 4 → …. SQL does not first *appear* until A8, so the calendar front-loads only **cheap, unlockable prerequisites** and holds the language until A8 needs it (Prop Lock: no SQL vocabulary before it is anchored).

| Window (main course) | Companion work (parallel, small) | Outcome |
|---|---|---|
| **A1–A4** (SQL-T-HS → SQL-T-UG tiers) | PQ-01, PQ-02, PQ-07, PQ-08 with SQL-Z0.1 – SQL-Z0.8 (≈ 6 short sessions) | paper fluency: sets/bags/3VL/counting/units |
| **A2, A3, A6, A11** | PQ-03 (types, decimals), PQ-04 (files/JSON), PQ-05 (`psql` + Docker Postgres) — the lab loads and fingerprints match (§3) | lab environment ready; no SQL semantics yet |
| **Tracks B and C (B3, C1, C4, C6)** | OD-10 (tests in CI), OD-02 (logs/slow-query vocabulary), OD-03 recall at B3 | vocabulary only; no new SQL |
| **A8 (the main event)** | **The A8 SQL block is stretched over ≥ 3 weeks:** week 1 = RT-01/04/05 + SL-01/02/03 + SQL-E1–SQL-E3 · week 2 = RT-02 + SL-04…SL-09 + SQL-E4–SQL-E7 + DB-1/DB-3 · week 3 = SL-10 + TX labs + CS-05 + DB-9 · then DB-4…DB-8 with CS-01…CS-04, CS-08 and PX cards · then DB-10 with CS-06, OD-04 · the V-STOR, OD-11 and OD-08 rows as bound in §2 | SQL competency through SQL-E9; plan and isolation predictions; the theory tier |
| **A7, A8, A9, A10** | SQL-E9.3 (A7), TX-5 (A9), SQL-E10.6 (A10), SQL-E4.5/SQL-CAP2 (A8 ledger, DD-03) | SQL that makes async/ledger/RLS true |
| **A7 + A9** | PX-9 / DD-13 with the scale primitives; SCH-2/SCH-3 inside packs | scale primitives with SQL evidence |
| **V-STOR, V-DATA, D3/D4** | AN-01 … AN-05, SQL-E6, SQL-E13, DT drills (BigQuery), SQL-E6.4/SQL-E13.4/SQL-E13.5 at D3 (DD-05) | analytics dialect and point-in-time joins |
| **C6, C7, B4** | PX cards and SQL-CAP4 at C6; DT-4 at B4 | performance and cost SQL |
| **Phase 4** (PCA case studies) | SQL-CAP1 – SQL-CAP4 | database acceptance |
| **A8 skip-tests — SQL-SKIP-SQL / SQL-SKIP-ENGINE** | skip-test via the checkpoints in the stitch table; else run the SQL-SKIP-SQL/SQL-SKIP-ENGINE orders below | continuation, only if the skip-test fails |

**SQL-SKIP-SQL order → companion modules (order unchanged):** relations/keys/FDs/normalisation → **RT-01, RT-04, RT-05** · relational algebra → **RT-02** (+ TD-5/6) · DDL/types/constraints → **SL-01, DD-04, DD-12** · SELECT semantics & NULL/3VL → **SL-02, SL-03** · joins incl. semi/anti/outer → **SL-04** · aggregation → **SL-05** · subqueries/CTEs/recursion → **SL-06, SL-07, SL-09** · windows → **SL-08** · transactions/isolation → **CS-05** + TX labs · pagination and application access → **OD-09**. *Predict multiplicity and NULL behaviour before execution.*

**SQL-SKIP-ENGINE order → companion modules:** storage media & layouts → **CS-01, CS-09** · pages/tuples/TOAST/catalogs → **CS-01** · buffer manager → **CS-04** · hash/B-tree/GIN/GiST/BRIN/vector indexes → **CS-02, CS-10** · iterators, sort/aggregate, join algorithms → **CS-03** · statistics/cardinality/cost → **CS-08** · MVCC/isolation/locks/deadlocks/vacuum → **CS-05, OD-06** · WAL/checkpoints/recovery → **CS-06** · replication/PITR → **CS-06, CS-07, OD-04, OD-05** · parallel/distributed trade-offs → **CS-07, CS-09**.

---

---

## 3. Lab kit — deterministic SQL lab

### 3.1 What you get
Local PostgreSQL 15.x database `labdb` with schema `lab` (the storefront OLTP data of §0.3) plus `work` (scratch) and fingerprint functions `lab.chk` / `lab.chk_o`. Every kit file is printed in full in §3.8: the schema `lab_schema.sql`, the seed `lab_seed.sql`, the runners `run_ex.py`, `plans.py`, `tx_tests.py`, and the rest.

> **Note:** Kit check of 2026-09-24: every file in §3.8 was extracted from this companion and run against a fresh local cluster (timezone UTC, C collation, seed v1). All 103 printed fingerprints (the exercise goldens and the trap fingerprints) were reproduced exactly. That server was PostgreSQL 16.13, so the run was a recorded deviation from the 15.x pin, made under `LAB_ALLOW_PG_MAJOR=16`. The pin stays at 15.x until a full run on another major is recorded.

### 3.2 Bring-up (Docker default)
1. Run Postgres 15 with a named volume, port published (lab scripts expect `PGPORT=54329`, user/db `lab`/`labdb` — adjust env to match your compose).
2. `psql -v ON_ERROR_STOP=1 -f lab_schema.sql -f lab_seed.sql`
3. Pin session: `SET TIME ZONE 'UTC';` and use `C` collation (image default `C`/`POSIX` for the lab). **Goldens are invalid if timezone or collation drift.**
4. Smoke: `SELECT lab.chk('SELECT 1');` — non-null `1:…` fingerprint.
5. The pins are checked, not trusted: `run_ex.py` first reads `server_version_num`, `TimeZone`, the database collation and the seed's row counts, and refuses to run if any of them drifts from seed v1 on PostgreSQL 15.x with UTC and C. To run on another major version on purpose, set `LAB_ALLOW_PG_MAJOR` to that major and record the deviation beside the goldens you compare. If the collation check fails on a stock container image whose default locale is not C, create the database with the C collation: `CREATE DATABASE labdb LC_COLLATE 'C' LC_CTYPE 'C' TEMPLATE template0` (or initialise the cluster with `--locale=C`).

Cloud SQL / AlloyDB: same SQL; create an instance only when Lab Reality allows and **destroy the same day** (Lab Safety, rule 0.5). Auth Proxy for IAM DB auth when OD-11 is unlocked — not required for local goldens.

### 3.3 Schema overview (v1)
| Table | Role |
|---|---|
| `tenant` | 5 tenants (free/pro/enterprise) |
| `app_user` | 2000 users; soft delete; referral forest; NULL countries on purpose |
| `category` | per-tenant trees (`parent_id`) |
| `product` | 500 SKUs; `price_minor`; `attrs` JSONB; discontinuations |
| `product_price_history` | effective-dated prices (as-of join fodder) |
| `stock` | on_hand/reserved with CHECK |
| `customer_order` | 20 000 orders; power-law users (user 1 hot; 1801–2000 never order); tenant-safe composite FK |
| `order_line` | 1–4 lines/order; money in minor units |
| `payment` / `shipment` / `review` | charges/refunds; carriers; NULL/'' review bodies |
| `event` | analytics stream with JSONB payload |
| `stg_import` | messy CSV-like rows for cleaning |
| `login_day` | gaps-and-islands fodder |

### 3.4 Seed summary
Deterministic: **no `random()`** — every value is a pure function of ids. Seed tag: **v1**. After load, `ANALYZE;` is part of the seed. Approximate scale: 5 tenants · 2k users · 500 products · 20k orders · matching lines/payments/events.

### 3.5 Fingerprint protocol
```
lab.chk(q)   → '<rowcount>:<8 hex md5>' over order-insensitive row text
lab.chk_o(q) → same but preserves result order (for ORDER BY/LIMIT exercises)
```
Two answers match iff fingerprints match. Regenerating goldens: `python run_ex.py ex_l1_4` (etc.) against a clean seed. Wrong-path fingerprints live in `goldens_wrong.json` (see traps).

### 3.6 Predict-before-run
Every exercise with a result shape, row count, plan shape, or isolation outcome: write the prediction (one line) **before** `psql`. Record discrepancies on the ledger — wrong predictions are the teaching moment.

### 3.7 How runners relate (files in §3.8)
| Runner | Purpose |
|---|---|
| `run_ex.py` | Executes exercise keys inside `BEGIN…ROLLBACK`, prints golden + sample rows |
| `plans.py` | PX plan catalogue (PX-1–PX-11) |
| `tx_tests.py` + `two.py` | Dual-session TX scenarios |
| `wrongs.py` | Canonical wrong queries for trap fingerprints |
| `naive.sql` / `safe.sql` | Oversell RMW vs atomic claim (TX companion) |
| `slow_bad.sql` / `slow_good.sql` | SQL-CAP4 baseline vs rewrite |

### 3.8 The lab kit files, in full

Every file of the kit, in full, under its own name. Copy each block into a file of that name in one directory, bring the database up as in §3.2, and run the runners from that directory. Generated state (the database volume, run logs) is not part of the kit; the goldens files are, because the exercise cards cite them.

#### `lab_schema.sql`

Schemas `lab` and `work`, every table and constraint, and the fingerprint functions.

```sql
-- Storefront SQL Lab — schema v1 (PostgreSQL 15+; runs unchanged on Cloud SQL / AlloyDB for PostgreSQL)
DROP SCHEMA IF EXISTS lab CASCADE;
CREATE SCHEMA lab;
SET search_path = lab;
SET TIME ZONE 'UTC';

CREATE TABLE tenant (
  tenant_id   int         PRIMARY KEY,
  name        text        NOT NULL UNIQUE,
  plan        text        NOT NULL CHECK (plan IN ('free','pro','enterprise')),
  created_at  timestamptz NOT NULL
);

CREATE TABLE app_user (
  user_id      bigint      PRIMARY KEY,
  tenant_id    int         NOT NULL REFERENCES tenant,
  email        text        NOT NULL,
  display_name text        NOT NULL,
  country      char(2),                                   -- NULL on purpose (unknown)
  referred_by  bigint      REFERENCES app_user,           -- forest: recursive-CTE fodder
  created_at   timestamptz NOT NULL,
  deleted_at   timestamptz,                               -- soft delete
  UNIQUE (tenant_id, email),
  UNIQUE (tenant_id, user_id)                             -- target for tenant-safe composite FKs
);

CREATE TABLE category (
  category_id int  PRIMARY KEY,
  tenant_id   int  NOT NULL REFERENCES tenant,
  parent_id   int  REFERENCES category,
  name        text NOT NULL
);

CREATE TABLE product (
  product_id      bigint      PRIMARY KEY,
  tenant_id       int         NOT NULL REFERENCES tenant,
  sku             text        NOT NULL,
  name            text        NOT NULL,
  category_id     int         REFERENCES category,        -- NULL = uncategorised
  price_minor     int         NOT NULL CHECK (price_minor >= 0),   -- current list price, minor units
  currency        char(3)     NOT NULL DEFAULT 'USD',
  attrs           jsonb       NOT NULL DEFAULT '{}',
  created_at      timestamptz NOT NULL,
  discontinued_at timestamptz,
  UNIQUE (tenant_id, sku)
);

CREATE TABLE product_price_history (                      -- effective-dated prices (valid_from inclusive)
  product_id  bigint      NOT NULL REFERENCES product,
  valid_from  timestamptz NOT NULL,
  price_minor int         NOT NULL CHECK (price_minor >= 0),
  PRIMARY KEY (product_id, valid_from)
);

CREATE TABLE stock (
  product_id bigint      PRIMARY KEY REFERENCES product,
  on_hand    int         NOT NULL CHECK (on_hand >= 0),
  reserved   int         NOT NULL DEFAULT 0 CHECK (reserved >= 0),
  updated_at timestamptz NOT NULL,
  CHECK (reserved <= on_hand)
);

CREATE TABLE customer_order (
  order_id        bigint      PRIMARY KEY,
  tenant_id       int         NOT NULL,
  user_id         bigint      NOT NULL,
  status          text        NOT NULL CHECK (status IN ('created','paid','fulfilled','refunded','cancelled')),
  placed_at       timestamptz NOT NULL,
  currency        char(3)     NOT NULL DEFAULT 'USD',
  total_minor     bigint      NOT NULL DEFAULT 0,
  idempotency_key text,
  UNIQUE (tenant_id, idempotency_key),
  FOREIGN KEY (tenant_id, user_id) REFERENCES app_user (tenant_id, user_id)   -- tenant-safe FK
);

CREATE TABLE order_line (
  order_id         bigint NOT NULL REFERENCES customer_order,
  line_no          int    NOT NULL,
  product_id       bigint NOT NULL REFERENCES product,
  qty              int    NOT NULL CHECK (qty > 0),
  unit_price_minor int    NOT NULL CHECK (unit_price_minor >= 0),
  PRIMARY KEY (order_id, line_no)
);

CREATE TABLE payment (
  payment_id   bigint      PRIMARY KEY,
  order_id     bigint      NOT NULL REFERENCES customer_order,
  kind         text        NOT NULL CHECK (kind IN ('charge','refund')),
  amount_minor bigint      NOT NULL CHECK (amount_minor > 0),
  status       text        NOT NULL CHECK (status IN ('pending','succeeded','failed')),
  created_at   timestamptz NOT NULL
);

CREATE TABLE shipment (
  shipment_id  bigint      PRIMARY KEY,
  order_id     bigint      NOT NULL REFERENCES customer_order,
  carrier      text        NOT NULL,
  shipped_at   timestamptz NOT NULL,
  delivered_at timestamptz                                -- NULL = still in transit
);

CREATE TABLE review (
  review_id  bigint      PRIMARY KEY,
  product_id bigint      NOT NULL REFERENCES product,
  user_id    bigint      NOT NULL REFERENCES app_user,
  rating     smallint    NOT NULL CHECK (rating BETWEEN 1 AND 5),
  body       text,                                        -- NULL and '' both occur
  created_at timestamptz NOT NULL
);

CREATE TABLE event (                                      -- analytics stream (semi-structured payload)
  event_id    bigint      PRIMARY KEY,
  tenant_id   int         NOT NULL REFERENCES tenant,
  user_id     bigint,                                     -- NULL = anonymous
  event_type  text        NOT NULL,
  occurred_at timestamptz NOT NULL,
  payload     jsonb       NOT NULL DEFAULT '{}'
);

CREATE TABLE stg_import (                                 -- deliberately messy staging data
  row_id      int  PRIMARY KEY,
  email_text  text,
  signup_text text,
  amount_text text
);
```

#### `lab_seed.sql`

The deterministic seed v1 (no `random()`), ending in `ANALYZE`.

```sql
-- Storefront SQL Lab — deterministic seed v1. No random(): every value is a pure function of its ids.
SET search_path = lab;
SET TIME ZONE 'UTC';

INSERT INTO tenant
SELECT t, 'tenant-' || t,
       (ARRAY['free','pro','enterprise','pro','free'])[t],
       timestamptz '2024-01-01' + t * interval '1 day'
FROM generate_series(1,5) t;

INSERT INTO app_user (user_id, tenant_id, email, display_name, country, referred_by, created_at, deleted_at)
SELECT i,
       (i-1) % 5 + 1,
       'user' || i || '@t' || ((i-1) % 5 + 1) || '.example.com',
       'User ' || i,
       CASE WHEN i % 11 = 0 THEN NULL ELSE (ARRAY['US','GB','DE','IN','BR','JP','FR'])[i % 7 + 1] END,
       CASE WHEN i <= 50 OR i % 4 = 0 THEN NULL ELSE ((i::bigint * 2654435761) % 4294967296) % (i - 1) + 1 END,
       timestamptz '2024-02-01' + (i % 300) * interval '1 day' + (i % 24) * interval '1 hour',
       CASE WHEN i % 97 = 0
            THEN timestamptz '2024-02-01' + (i % 300) * interval '1 day' + interval '100 days' END
FROM generate_series(1,2000) i;

INSERT INTO category (category_id, tenant_id, parent_id, name)
SELECT t*100 + k, t,
       CASE WHEN k = 1 THEN NULL
            WHEN k BETWEEN 2 AND 4 THEN t*100 + 1
            ELSE t*100 + 2 + (k-5)/2 END,
       'cat-' || t || '-' || k
FROM generate_series(1,5) t, generate_series(1,10) k;

INSERT INTO product (product_id, tenant_id, sku, name, category_id, price_minor, currency, attrs, created_at, discontinued_at)
SELECT i,
       (i-1) % 5 + 1,
       'SKU-' || lpad(i::text, 4, '0'),
       'Product ' || i,
       CASE WHEN i % 13 = 0 THEN NULL ELSE ((i-1) % 5 + 1) * 100 + 5 + (i % 6) END,
       500 + (i * 137) % 9500,
       CASE WHEN (i-1) % 5 + 1 = 4 THEN 'EUR' ELSE 'USD' END,
       jsonb_build_object('color', (ARRAY['red','green','blue','black'])[i % 4 + 1],
                          'weight_g', 100 + i % 900)
         || CASE WHEN i % 3 = 0 THEN jsonb_build_object('tags', jsonb_build_array('eco', 'gift')) ELSE '{}'::jsonb END,
       timestamptz '2024-01-15' + (i % 60) * interval '1 day',
       CASE WHEN i % 17 = 0 THEN timestamptz '2025-06-01' END
FROM generate_series(1,500) i;

INSERT INTO product_price_history (product_id, valid_from, price_minor)
SELECT p.product_id, p.created_at + h.d * interval '1 day', p.price_minor + h.delta
FROM product p
CROSS JOIN (VALUES (0, 200), (200, 100), (400, 0)) AS h(d, delta);

INSERT INTO stock (product_id, on_hand, reserved, updated_at)
SELECT i, (i * 31) % 200, ((i * 31) % 200) / 10, timestamptz '2025-12-31 12:00:00'
FROM generate_series(1,500) i;

-- 20,000 orders; user drawn from a skewed (power-law-ish) deterministic hash: user 1 is hot, users 1801-2000 never order;
-- tenant follows the user so the composite FK holds
INSERT INTO customer_order (order_id, tenant_id, user_id, status, placed_at, currency, total_minor, idempotency_key)
SELECT i,
       (u - 1) % 5 + 1,
       u,
       CASE WHEN i % 20 <= 11 THEN 'fulfilled'
            WHEN i % 20 <= 14 THEN 'paid'
            WHEN i % 20 <= 16 THEN 'cancelled'
            WHEN i % 20 = 17  THEN 'created'
            ELSE 'refunded' END,
       timestamptz '2025-01-01' + ((i * 37) % 365) * interval '1 day' + ((i * 7919) % 86400) * interval '1 second',
       CASE WHEN (u - 1) % 5 + 1 = 4 THEN 'EUR' ELSE 'USD' END,
       0,
       CASE WHEN i % 2 = 0 THEN 'idem-' || i END
FROM (SELECT i, 1 + floor(1800 * power(((i * 7919) % 10007)::numeric / 10007, 1.5))::int AS u FROM generate_series(1,20000) i) s;

INSERT INTO order_line (order_id, line_no, product_id, qty, unit_price_minor)
SELECT o.order_id, n, o.tenant_id + 5 * (((o.order_id::bigint * 2654435761 + n * 40503) % 4294967296) % 100), 1 + (o.order_id + n) % 3, 0
FROM customer_order o
JOIN LATERAL generate_series(1, 1 + o.order_id % 4) n ON true;

UPDATE order_line l SET unit_price_minor = p.price_minor FROM product p WHERE p.product_id = l.product_id;

UPDATE customer_order o SET total_minor = s.t
FROM (SELECT order_id, sum(qty::bigint * unit_price_minor) AS t FROM order_line GROUP BY order_id) s
WHERE s.order_id = o.order_id;

INSERT INTO payment (payment_id, order_id, kind, amount_minor, status, created_at)
SELECT row_number() OVER (ORDER BY order_id, created_at, kind), order_id, kind, amount_minor, status, created_at
FROM (
  -- failed first attempt for every 15th paid-ish order
  SELECT order_id, 'charge' AS kind, total_minor AS amount_minor, 'failed' AS status, placed_at + interval '30 seconds' AS created_at
  FROM customer_order WHERE order_id % 15 = 0 AND status IN ('paid','fulfilled','refunded')
  UNION ALL
  SELECT order_id, 'charge', total_minor, 'succeeded', placed_at + interval '1 minute'
  FROM customer_order WHERE status IN ('paid','fulfilled','refunded')
  UNION ALL
  SELECT order_id, 'charge', total_minor, 'pending', placed_at + interval '10 seconds'
  FROM customer_order WHERE status = 'created'
  UNION ALL
  SELECT order_id, 'charge', total_minor, 'failed', placed_at + interval '20 seconds'
  FROM customer_order WHERE status = 'cancelled' AND order_id % 2 = 0
  UNION ALL
  SELECT order_id, 'refund', CASE WHEN order_id % 2 = 0 THEN total_minor ELSE total_minor / 2 END, 'succeeded', placed_at + interval '5 days'
  FROM customer_order WHERE status = 'refunded'
) x;

INSERT INTO shipment (shipment_id, order_id, carrier, shipped_at, delivered_at)
SELECT row_number() OVER (ORDER BY o.order_id, n), o.order_id,
       (ARRAY['UPS','DHL','FedEx'])[(o.order_id + n) % 3 + 1],
       o.placed_at + interval '1 day' + n * interval '2 hours',
       CASE WHEN o.order_id % 7 = 0 THEN NULL
            ELSE o.placed_at + interval '1 day' + n * interval '2 hours' + (2 + o.order_id % 5 + (o.order_id + n) % 3 - 1) * interval '1 day' END
FROM customer_order o
JOIN LATERAL generate_series(1, CASE WHEN o.order_id % 9 = 0 THEN 2 ELSE 1 END) n ON true
WHERE o.status = 'fulfilled';

INSERT INTO review (review_id, product_id, user_id, rating, body, created_at)
SELECT i, p, t + 5 * ((i * 31) % 400),
       CASE (i * 7 + i / 5) % 10 WHEN 0 THEN 1 WHEN 1 THEN 2 WHEN 2 THEN 3 WHEN 3 THEN 3
            WHEN 4 THEN 4 WHEN 5 THEN 4 WHEN 6 THEN 4 ELSE 5 END,
       CASE WHEN i % 5 = 0 THEN NULL WHEN i % 11 = 0 THEN '' ELSE 'Review text ' || i END,
       timestamptz '2025-02-01' + (i % 300) * interval '1 day'
FROM (SELECT i, pp AS p, (pp - 1) % 5 + 1 AS t
      FROM (SELECT i, 1 + floor(500 * power(((i * 7919) % 6007)::numeric / 6007, 1.3))::int AS pp FROM generate_series(1,6000) i) q) s;

-- double-submit bug: every 15th review was posted a second time a day later (400 duplicate (product,user) pairs)
INSERT INTO review (review_id, product_id, user_id, rating, body, created_at)
SELECT review_id + 6000, product_id, user_id, rating, body, created_at + interval '1 day'
FROM review WHERE review_id % 15 = 0;

-- 60,000 events = 7,500 blocks of 8. A block is one visit by one user on one day; every 3rd block has a 40-min gap at k=4.
INSERT INTO event (event_id, tenant_id, user_id, event_type, occurred_at, payload)
SELECT i,
       CASE WHEN b % 6 = 0 THEN b % 5 + 1 ELSE (u - 1) % 5 + 1 END,
       CASE WHEN b % 6 = 0 THEN NULL ELSE u END,
       CASE k WHEN 2 THEN 'search'
              WHEN 4 THEN CASE WHEN b % 2 = 0 THEN 'add_to_cart' ELSE 'page_view' END
              WHEN 5 THEN CASE WHEN b % 4 = 0 THEN 'checkout_start' ELSE 'page_view' END
              WHEN 6 THEN CASE WHEN b % 8 = 0 THEN 'purchase' ELSE 'page_view' END
              ELSE 'page_view' END,
       timestamptz '2025-01-01' + ((b * 37) % 365) * interval '1 day' + ((b * 7919) % 70000) * interval '1 second'
         + (k * 120 + CASE WHEN b % 3 = 0 AND k >= 4 THEN 2400 ELSE 0 END) * interval '1 second',
       jsonb_build_object('path', '/p/' || (1 + (b * 13 + k) % 500), 'ms', (b * k * 53) % 3000)
         || CASE WHEN k = 2 THEN jsonb_build_object('q', (ARRAY['shoe','lamp','desk','mug'])[b % 4 + 1]) ELSE '{}'::jsonb END
FROM (SELECT i, (i - 1) / 8 AS b, (i - 1) % 8 AS k,
             (((i - 1) / 8) * 7919) % 2000 + 1 AS u
      FROM generate_series(1,60000) i) s;

-- messy staging rows for the cleaning ladder
INSERT INTO stg_import VALUES
 (1,  'Ann@Example.com ',   '2025-03-01',   '12.50'),
 (2,  'ann@example.com',    '03/01/2025',   '$1,200.00'),
 (3,  'bob@example.com',    '1 Mar 2025',   '12,50'),
 (4,  '',                   '2025-03-02',   ' 7 '),
 (5,  NULL,                 '2025-03-02',   '0'),
 (6,  'carol@example.com',  'not a date',   'abc'),
 (7,  'CAROL@EXAMPLE.COM',  '2025-03-03',   '3.999'),
 (8,  'dave@example.com',   '',             NULL),
 (9,  'dave@example.com',   '2025-13-40',   '-5.00'),
 (10, ' erin@example.com',  '2025-03-04',   '1e3'),
 (11, 'frank@example',      '2025-03-05',   '15'),
 (12, 'gina@example.com',   '2025-02-29',   '9.99'),
 (13, 'gina@example.com',   '2025-03-06',   '9.99'),
 (14, 'hal@example.com',    '2025-03-06T10:15:00Z', '100'),
 (15, 'ivy@example.com',    '  2025-03-07  ', '1,000.5');

-- gaps-and-islands fodder: which days each of the first 200 users logged in (120 days from 2025-03-01)
CREATE TABLE login_day (
  user_id bigint NOT NULL REFERENCES app_user,
  day     date   NOT NULL,
  PRIMARY KEY (user_id, day)
);
INSERT INTO login_day (user_id, day)
SELECT u, date '2025-03-01' + d
FROM generate_series(1,200) u, generate_series(0,119) d
WHERE (d + u) % 9 < 6 AND d % 23 <> u % 23;

ANALYZE;

-- Lab kit: order-insensitive and order-sensitive result fingerprints (row count : 8 hex chars of md5)
CREATE FUNCTION chk(q text) RETURNS text LANGUAGE plpgsql AS $f$
DECLARE r text;
BEGIN
  EXECUTE format('SELECT count(*) || '':'' || left(md5(coalesce(string_agg(t::text, ''|'' ORDER BY t::text), '''')), 8) FROM (%s) t', q) INTO r;
  RETURN r;
END $f$;

CREATE FUNCTION chk_o(q text) RETURNS text LANGUAGE plpgsql AS $f$
DECLARE r text;
BEGIN
  EXECUTE format('SELECT count(*) || '':'' || left(md5(coalesce(string_agg(t::text, ''|'' ORDER BY rn), '''')), 8) FROM (SELECT row_number() OVER () AS rn, x.* FROM (%s) x) t', q) INTO r;
  RETURN r;
END $f$;

CREATE FUNCTION try(stmt text) RETURNS boolean LANGUAGE plpgsql AS $f$
BEGIN EXECUTE stmt; RETURN true; EXCEPTION WHEN others THEN RETURN false; END $f$;

CREATE SCHEMA IF NOT EXISTS work;
```

#### `run_ex.py`

Runs exercise keys inside `BEGIN…ROLLBACK` and writes the goldens file for the chosen levels.

```python
import subprocess, sys, json, importlib, os
ENV = dict(os.environ, PGHOST="localhost", PGPORT="54329", PGUSER="lab", PGDATABASE="labdb")

def psql(script):
    p = subprocess.run(["psql", "-At", "-v", "ON_ERROR_STOP=1", "-q", "-X"], input=script, capture_output=True, text=True, env=ENV)
    return p.returncode, p.stdout, p.stderr
def pins():
    """The goldens hold only for seed v1 on PostgreSQL 15.x with timezone UTC and the C collation; refuse to run on drift."""
    rc, out, err = psql("SHOW server_version_num;\nSHOW TimeZone;\n"
                        "SELECT datcollate FROM pg_database WHERE datname = current_database();\n"
                        "SELECT count(*) FROM lab.tenant;\nSELECT count(*) FROM lab.app_user;\n"
                        "SELECT count(*) FROM lab.product;\nSELECT count(*) FROM lab.customer_order;\n")
    if rc != 0:
        sys.exit("pins: " + err.strip())
    num, tz, coll, *counts = out.split()
    major = str(int(num) // 10000)
    bad = []
    if major != "15" and major != os.environ.get("LAB_ALLOW_PG_MAJOR"):
        bad.append(f"PostgreSQL {major}.x, not 15.x (set LAB_ALLOW_PG_MAJOR={major} to run anyway, and record the deviation)")
    if tz not in ("UTC", "Etc/UTC"):
        bad.append(f"TimeZone {tz}, not UTC")
    if coll not in ("C", "POSIX"):
        bad.append(f"collation {coll}, not C")
    if counts != ["5", "2000", "500", "20000"]:
        bad.append(f"seed counts {counts}, not seed v1's 5 tenants, 2000 users, 500 products, 20000 orders")
    if bad:
        sys.exit("pins: " + "; ".join(bad))

def run(e):
    probe = e.get("probe", e["key"]).rstrip().rstrip(";")
    fn = "chk_o" if e["ordered"] else "chk"
    setup = e.get("setup", "")
    stmts = e.get("stmts", "")
    show_order = "" if e["ordered"] else " ORDER BY t::text"
    script = f"""BEGIN;
SET LOCAL search_path = public;
{setup}
{stmts}
CREATE TEMP TABLE _p AS {probe};
SELECT 'G|' || lab.{fn}('SELECT * FROM _p');
SELECT 'R|' || t::text FROM _p t{show_order} LIMIT 16;
ROLLBACK;
"""
    rc, out, err = psql(script)
    if rc != 0:
        return None, [], err.strip()
    g = None; rows = []
    for line in out.splitlines():
        if line.startswith("G|"): g = line[2:]
        elif line.startswith("R|"): rows.append(line[2:])
    return g, rows, ""

if __name__ == "__main__":
    pins()
    mods = sys.argv[1].split(",")
    only = set(sys.argv[2].split(",")) if len(sys.argv) > 2 else None
    res = {}
    for m in mods:
        mod = importlib.import_module(m)
        for e in mod.EX:
            if only and e["id"] not in only: continue
            g, rows, err = run(e)
            res[e["id"]] = {"golden": g, "rows": rows, "err": err}
            print(e["id"], g, ("ERR: " + err[:300]) if err else "")
    json.dump(res, open("goldens_" + "_".join(mods) + ".json", "w"), indent=1)
```

#### `ex_l1_4.py`

Exercise keys, levels 1–4.

```python

# Each exercise: id, title, tags, prompt, out, trap, key, ordered, [setup, stmts, probe, show, ext, stitch]
EX = []
def ex(**kw):
    kw.setdefault("ordered", False)
    EX.append(kw)

# ---------------------------------------------------------------- LEVEL 1 : SELECT, filter, NULL, CASE
ex(id="E1.1", level=1, title="Q2-2024 signups from GB or DE", tags="WHERE · half-open ranges",
   prompt="Users whose country is GB or DE and who were created in the second quarter of 2024 (April, May and June, UTC).",
   out="`user_id, email`",
   trap="`BETWEEN '2024-04-01' AND '2024-06-30'` silently drops most of 30 June for a `timestamptz`. Use `>= start AND < next_start`.",
   key="""SELECT user_id, email
FROM lab.app_user
WHERE country IN ('GB','DE')
  AND created_at >= '2024-04-01' AND created_at < '2024-07-01'""")

ex(id="E1.2", level=1, title="Unknown country", tags="NULL · IS NULL",
   prompt="Users whose country is unknown (stored as NULL).",
   out="`user_id`",
   trap="`country = NULL` is never true — it is UNKNOWN. Also note `char(2)` pads; do not compare with `''`.",
   key="SELECT user_id FROM lab.app_user WHERE country IS NULL")

ex(id="E1.3", level=1, title="Everyone not known to be in the US", tags="NULL · 3VL · IS DISTINCT FROM",
   prompt="All users who are not known to be in the US — this **includes** users whose country is unknown.",
   out="`user_id`",
   trap="`country <> 'US'` drops the NULL-country users (UNKNOWN is not TRUE). Use `IS DISTINCT FROM`, or `country <> 'US' OR country IS NULL`. Write the 3VL truth table for `NOT (country = 'US')` first.",
   key="SELECT user_id FROM lab.app_user WHERE country IS DISTINCT FROM 'US'")

ex(id="E1.4", level=1, title="Mid-priced live catalogue, top 20", tags="WHERE · ORDER BY · LIMIT · determinism",
   prompt="Products with `price_minor` from 1000 to 2000 inclusive that are not discontinued, most expensive first, ties broken by lowest `product_id`; first 20 rows only.",
   out="`product_id, price_minor` (ordered)",
   trap="`LIMIT` without a total order is non-deterministic. `discontinued_at IS NULL`, not `= NULL`. Both bounds are inclusive here (integer money, so `BETWEEN` is safe).",
   ordered=True,
   key="""SELECT product_id, price_minor
FROM lab.product
WHERE price_minor BETWEEN 1000 AND 2000 AND discontinued_at IS NULL
ORDER BY price_minor DESC, product_id
LIMIT 20""")

ex(id="E1.5", level=1, title="Reviews with no text", tags="NULL vs empty string · COALESCE",
   prompt="Reviews whose body is missing — treat NULL and the empty string as the same thing.",
   out="`review_id`",
   trap="NULL and `''` are different values; a test for one silently misses the other. In Oracle they collapse into one — a dialect trap (see the Rosetta table).",
   key="SELECT review_id FROM lab.review WHERE coalesce(body, '') = ''")

ex(id="E1.6", level=1, title="Order status buckets", tags="CASE · expressions",
   prompt="Label every order: `open` for created/paid, `done` for fulfilled, `closed` for cancelled/refunded.",
   out="`order_id, bucket`",
   trap="A `CASE` without `ELSE` yields NULL for unmatched values — add a defensive `ELSE 'unknown'` and say why it should never fire (the `CHECK` constraint).",
   key="""SELECT order_id,
       CASE status WHEN 'created' THEN 'open' WHEN 'paid' THEN 'open'
                   WHEN 'fulfilled' THEN 'done'
                   WHEN 'cancelled' THEN 'closed' WHEN 'refunded' THEN 'closed'
                   ELSE 'unknown' END AS bucket
FROM lab.customer_order""")

ex(id="E1.7", level=1, title="Ten priciest live products", tags="ORDER BY · LIMIT · tie-break",
   prompt="The ten most expensive products that are not discontinued (ties → lowest `product_id`).",
   out="`product_id, price_minor` (ordered)",
   trap="Sorting by price alone and hoping. State the tie-break in the spec *before* you write the query.",
   ordered=True,
   key="""SELECT product_id, price_minor FROM lab.product
WHERE discontinued_at IS NULL
ORDER BY price_minor DESC, product_id LIMIT 10""")

ex(id="E1.8", level=1, title="Pattern search", tags="LIKE · ILIKE · escaping",
   prompt="Products whose SKU starts with `SKU-01` and ends with `7`.",
   out="`product_id`",
   trap="`_` and `%` are wildcards — to match a literal underscore you need `ESCAPE`. A leading-wildcard pattern (`'%7'`) cannot use a B-tree index (see the P3 prediction card).",
   key="SELECT product_id FROM lab.product WHERE sku LIKE 'SKU-01%' AND sku LIKE '%7'")

# ---------------------------------------------------------------- LEVEL 2 : aggregation
ex(id="E2.1", level=2, title="Orders and revenue by status", tags="GROUP BY · SUM",
   prompt="For each order status: number of orders and the sum of `total_minor`.",
   out="`status, n_orders, sum_minor`",
   trap="Every non-aggregated SELECT column must be in GROUP BY (or functionally dependent on the PK). Money is an integer of minor units — never `float`.",
   key="SELECT status, count(*) AS n_orders, sum(total_minor) AS sum_minor FROM lab.customer_order GROUP BY status")

ex(id="E2.2", level=2, title="Monthly fulfilled GMV, 2025", tags="date_trunc · GROUP BY · time zones",
   prompt="For fulfilled orders placed in calendar 2025 (UTC): month start, order count, and GMV (`sum(total_minor)`).",
   out="`month, n_orders, gmv_minor`",
   trap="`date_trunc('month', timestamptz)` uses the **session** time zone. The lab pins `UTC`; production rarely does — always state the zone.",
   key="""SELECT date_trunc('month', placed_at) AS month, count(*) AS n_orders, sum(total_minor) AS gmv_minor
FROM lab.customer_order
WHERE status = 'fulfilled' AND placed_at >= '2025-01-01' AND placed_at < '2026-01-01'
GROUP BY 1""")

ex(id="E2.3", level=2, title="Well-reviewed products", tags="HAVING · WHERE vs HAVING · ROUND",
   prompt="Products with at least 10 reviews: review count and average rating rounded to 2 decimals.",
   out="`product_id, n, avg_rating`",
   trap="`WHERE` filters rows *before* grouping, `HAVING` filters groups *after*. `avg(smallint)` is `numeric`, so `round(avg(rating), 2)` works; in engines with integer division check the type.",
   key="""SELECT product_id, count(*) AS n, round(avg(rating), 2) AS avg_rating
FROM lab.review GROUP BY product_id HAVING count(*) >= 10""")

ex(id="E2.4", level=2, title="Buyers per tenant", tags="COUNT(DISTINCT) · count(*) vs count(col)",
   prompt="Per tenant: number of orders and number of *distinct* users who placed at least one order.",
   out="`tenant_id, n_orders, n_buyers`",
   trap="`count(*)` counts rows, `count(col)` skips NULLs, `count(DISTINCT col)` de-duplicates. Say which one each output column needs.",
   key="""SELECT tenant_id, count(*) AS n_orders, count(DISTINCT user_id) AS n_buyers
FROM lab.customer_order GROUP BY tenant_id""")

ex(id="E2.5", level=2, title="Refund rate by tenant", tags="FILTER · conditional aggregation · integer division",
   prompt="Per tenant: total orders, refunded orders, and refund rate = refunded / total rounded to 4 decimals.",
   out="`tenant_id, n_orders, n_refunded, refund_rate`",
   trap="`1/3` in integer arithmetic is 0. Cast one side to `numeric` *before* dividing. `count(*) FILTER (WHERE …)` is the standard-SQL way; `SUM(CASE …)` is the portable way.",
   key="""SELECT tenant_id, count(*) AS n_orders,
       count(*) FILTER (WHERE status = 'refunded') AS n_refunded,
       round(count(*) FILTER (WHERE status = 'refunded')::numeric / count(*), 4) AS refund_rate
FROM lab.customer_order GROUP BY tenant_id""")

ex(id="E2.6", level=2, title="Users by country including unknown", tags="GROUP BY NULL · COALESCE",
   prompt="Number of users per country; label unknown as `'??'`.",
   out="`country, n`",
   trap="GROUP BY puts all NULLs in **one** group (unlike `=`). `country` is `char(2)` so `'US'` and `'US '` compare equal — but `coalesce(country,'??')` must be a valid `char(2)`.",
   key="SELECT coalesce(country, '??') AS country, count(*) AS n FROM lab.app_user GROUP BY 1")

ex(id="E2.7", level=2, title="Median order value per tenant", tags="ordered-set aggregates · percentile_disc",
   prompt="Per tenant, the median `total_minor` of fulfilled orders, defined as `percentile_disc(0.5)` (an actual value from the data).",
   out="`tenant_id, median_minor`",
   trap="`avg` is not the median. `percentile_cont` interpolates and returns `double precision` — a float in a money pipeline. State which definition you use.",
   key="""SELECT tenant_id, percentile_disc(0.5) WITHIN GROUP (ORDER BY total_minor) AS median_minor
FROM lab.customer_order WHERE status = 'fulfilled' GROUP BY tenant_id""")

ex(id="E2.8", level=2, title="Price histogram", tags="bucketing · integer division",
   prompt="Bucket **live** products (not discontinued) into price bands of width 1000 minor units: band start (0, 1000, 2000, …) and product count.",
   out="`band_start, n`",
   trap="`price_minor / 1000 * 1000` relies on integer division truncation — fine in Postgres, wrong in engines that return decimals (dialect trap). `width_bucket` is the explicit alternative.",
   key="""SELECT (price_minor / 1000) * 1000 AS band_start, count(*) AS n
FROM lab.product WHERE discontinued_at IS NULL GROUP BY 1""")

# ---------------------------------------------------------------- LEVEL 3 : joins
ex(id="E3.1", level=3, title="Paid orders with buyer and tenant", tags="INNER JOIN · multi-table",
   prompt="Orders with status `paid` placed in March 2025, tenant 2: order id, buyer email, tenant name, total.",
   out="`order_id, email, tenant_name, total_minor`",
   trap="Filter on the *driving* table in WHERE; join keys go in ON. Three tables, two ON clauses — write the join graph as a picture first.",
   key="""SELECT o.order_id, u.email, t.name AS tenant_name, o.total_minor
FROM lab.customer_order o
JOIN lab.app_user u ON u.user_id = o.user_id
JOIN lab.tenant   t ON t.tenant_id = o.tenant_id
WHERE o.tenant_id = 2 AND o.status = 'paid'
  AND o.placed_at >= '2025-03-01' AND o.placed_at < '2025-04-01'""")

ex(id="E3.2", level=3, title="Users who never referred anyone", tags="anti-join · NOT IN + NULL trap",
   prompt="Users who are not the referrer of any other user.",
   out="`user_id`",
   trap="`WHERE user_id NOT IN (SELECT referred_by FROM app_user)` returns **zero rows** because `referred_by` contains NULLs (`x NOT IN (…, NULL)` is never TRUE). Write it three ways: NOT EXISTS, LEFT JOIN … IS NULL, and NOT IN with a NULL filter — all three must give the same fingerprint.",
   key="""SELECT u.user_id FROM lab.app_user u
WHERE NOT EXISTS (SELECT 1 FROM lab.app_user r WHERE r.referred_by = u.user_id)""")

ex(id="E3.3", level=3, title="Users who never ordered", tags="LEFT JOIN … IS NULL · anti-join",
   prompt="Users with no order at all (any status).",
   out="`user_id`",
   trap="Test the *right-hand primary key* for NULL, not a column that can legitimately be NULL on the right.",
   key="""SELECT u.user_id FROM lab.app_user u
LEFT JOIN lab.customer_order o ON o.user_id = u.user_id
WHERE o.order_id IS NULL""")

ex(id="E3.4", level=3, title="Products not sold in a week", tags="anti-join · date ranges",
   prompt="Products that appear on **no** order line of a fulfilled order placed during 2025-01-01 … 2025-01-07 (inclusive, UTC).",
   out="`product_id`",
   trap="Where does the date filter go? Inside the `NOT EXISTS` subquery (or the `ON` of the LEFT JOIN) — not in the outer WHERE, where it would turn the anti-join into an inner join.",
   key="""SELECT p.product_id FROM lab.product p
WHERE NOT EXISTS (
  SELECT 1 FROM lab.order_line l JOIN lab.customer_order o USING (order_id)
  WHERE l.product_id = p.product_id AND o.status = 'fulfilled'
    AND o.placed_at >= '2025-01-01' AND o.placed_at < '2025-01-08')""")

ex(id="E3.5", level=3, title="Revenue of delivered orders", tags="semi-join · fan-out trap",
   prompt="Total `total_minor` of fulfilled orders that have **at least one** delivered shipment (`delivered_at IS NOT NULL`). One number.",
   out="`revenue_minor`",
   trap="`JOIN shipment` fans out: orders with two shipments are counted twice. Semi-join (`EXISTS`) never multiplies rows. Compute the naive join answer too and explain the difference in one sentence.",
   key="""SELECT sum(o.total_minor) AS revenue_minor FROM lab.customer_order o
WHERE o.status = 'fulfilled'
  AND EXISTS (SELECT 1 FROM lab.shipment s WHERE s.order_id = o.order_id AND s.delivered_at IS NOT NULL)""")

ex(id="E3.6", level=3, title="Cross-tenant referrals", tags="self-join · data-quality find",
   prompt="Users whose referrer belongs to a **different tenant**. This is a multi-tenancy integrity leak, not a feature.",
   out="`user_id, referrer_id`",
   trap="Alias the same table twice (`u`, `r`) and name the join direction aloud. Then: which constraint would have prevented this? (A composite FK `(tenant_id, referred_by) → (tenant_id, user_id)`.)",
   key="""SELECT u.user_id, r.user_id AS referrer_id
FROM lab.app_user u JOIN lab.app_user r ON r.user_id = u.referred_by
WHERE r.tenant_id <> u.tenant_id""")

ex(id="E3.7", level=3, title="One-star counts including zeros", tags="LEFT JOIN · filter in ON · empty groups",
   prompt="For **every** product of tenant 1 (all of them), the number of 1-star reviews it has — 0 where none.",
   out="`product_id, one_star`",
   trap="`LEFT JOIN review r … WHERE r.rating = 1` deletes the zero rows (the WHERE re-filters the NULL-extended rows). Put the predicate in `ON`, or use `count(*) FILTER`. `count(r.review_id)`, not `count(*)`.",
   key="""SELECT p.product_id, count(r.review_id) AS one_star
FROM lab.product p LEFT JOIN lab.review r ON r.product_id = p.product_id AND r.rating = 1
WHERE p.tenant_id = 1 GROUP BY p.product_id""")

ex(id="E3.8", level=3, title="Who ordered vs who reviewed (Q1 2025)", tags="FULL OUTER JOIN · reconciliation",
   prompt="For 2025 Q1 (Jan–Mar UTC): every user who placed **or** reviewed, with two booleans — did they order, did they review.",
   out="`user_id, ordered, reviewed`",
   trap="`COALESCE` the two join keys; a FULL JOIN yields NULL on the missing side. Pre-aggregate each side to one row per user *before* joining.",
   key="""WITH o AS (SELECT DISTINCT user_id FROM lab.customer_order WHERE placed_at >= '2025-01-01' AND placed_at < '2025-04-01'),
     r AS (SELECT DISTINCT user_id FROM lab.review WHERE created_at >= '2025-01-01' AND created_at < '2025-04-01')
SELECT coalesce(o.user_id, r.user_id) AS user_id, o.user_id IS NOT NULL AS ordered, r.user_id IS NOT NULL AS reviewed
FROM o FULL JOIN r ON r.user_id = o.user_id""")

ex(id="E3.9", level=3, title="Deletions per month with zero-fill", tags="calendar spine · generate_series · LEFT JOIN",
   prompt="For every month from 2024-05 through 2025-06 (inclusive, 14 rows), the number of users deleted (`deleted_at`) in that month — including months with zero.",
   out="`month, n_deleted`",
   trap="Group the fact table alone and empty months vanish. Generate the spine first (`generate_series`), then LEFT JOIN facts onto it.",
   key="""SELECT m::date AS month, count(u.user_id) AS n_deleted
FROM generate_series('2024-05-01'::date, '2025-06-01'::date, interval '1 month') m
LEFT JOIN lab.app_user u ON date_trunc('month', u.deleted_at) = m
GROUP BY m""")

ex(id="E3.10", level=3, title="Duplicate-safe reviewers per product", tags="multiplicity · DISTINCT vs GROUP BY",
   prompt="Per product: distinct reviewers and total reviews, only products where those two numbers differ.",
   out="`product_id, n_reviewers, n_reviews`",
   trap="A user may review the same product several times in this seed (see E9.4). `count(*)` ≠ `count(DISTINCT user_id)` exactly there.",
   key="""SELECT product_id, count(DISTINCT user_id) AS n_reviewers, count(*) AS n_reviews
FROM lab.review GROUP BY product_id HAVING count(DISTINCT user_id) <> count(*)""")

# ---------------------------------------------------------------- LEVEL 4 : subqueries, CTEs, set ops
ex(id="E4.1", level=4, title="Above-average spenders", tags="scalar subquery · CTE",
   prompt="Users whose total fulfilled spend is strictly greater than the average spend **across users who spent anything** (exclude users with no fulfilled orders from the average).",
   out="`user_id, spend_minor`",
   trap="What is the denominator? Users with zero orders shift the average if you `LEFT JOIN` them in. Write down which population you average over.",
   key="""WITH s AS (SELECT user_id, sum(total_minor) AS spend_minor FROM lab.customer_order WHERE status = 'fulfilled' GROUP BY user_id)
SELECT user_id, spend_minor FROM s WHERE spend_minor > (SELECT avg(spend_minor) FROM s)""")

ex(id="E4.2", level=4, title="Latest review rating per product", tags="correlated subquery · DISTINCT ON",
   prompt="For each product that has reviews: the rating of its most recent review (newest `created_at`; ties → highest `review_id`).",
   out="`product_id, rating`",
   trap="`max(created_at)` alone does not give you the rating from that row. Use a correlated subquery, `DISTINCT ON`, or a window (E5.4) — then prove they agree.",
   key="""SELECT DISTINCT ON (product_id) product_id, rating
FROM lab.review ORDER BY product_id, created_at DESC, review_id DESC""")

ex(id="E4.3", level=4, title="Both fulfilled and refunded", tags="EXISTS · INTERSECT",
   prompt="Users who have at least one fulfilled order **and** at least one refunded order.",
   out="`user_id`",
   trap="Two `EXISTS` clauses (or `INTERSECT`). A single `JOIN` with `status IN ('fulfilled','refunded')` finds users with *either*.",
   key="""SELECT user_id FROM lab.customer_order WHERE status = 'fulfilled'
INTERSECT
SELECT user_id FROM lab.customer_order WHERE status = 'refunded'""")

ex(id="E4.4", level=4, title="Reviewed but never bought", tags="EXCEPT · NOT EXISTS · set semantics",
   prompt="Distinct `(user_id, product_id)` pairs where the user reviewed the product but has **no** order line for it (in any of their orders, any status).",
   out="`user_id, product_id`",
   trap="`EXCEPT` removes duplicates and needs identical column lists; `EXCEPT ALL` is the bag version. Solve with both `EXCEPT` and `NOT EXISTS`.",
   key="""SELECT user_id, product_id FROM lab.review
EXCEPT
SELECT o.user_id, l.product_id FROM lab.customer_order o JOIN lab.order_line l USING (order_id)""")

ex(id="E4.5", level=4, title="Net revenue per tenant without double counting", tags="CTE · pre-aggregation · fan-out",
   prompt="Per tenant: GMV of fulfilled and refunded orders placed in 2025 (`sum(total_minor)`), sum of **succeeded refund** payments on those orders, and net = gmv − refunds.",
   out="`tenant_id, gmv_minor, refunded_minor, net_minor`",
   trap="orders → payments is 1:N. Joining orders to payments and summing `total_minor` counts each order once per payment row. Aggregate each side **separately in CTEs**, then join on the key.",
   key="""WITH g AS (
  SELECT tenant_id, sum(total_minor) AS gmv_minor FROM lab.customer_order
  WHERE status IN ('fulfilled','refunded') AND placed_at >= '2025-01-01' AND placed_at < '2026-01-01' GROUP BY tenant_id),
r AS (
  SELECT o.tenant_id, sum(p.amount_minor) AS refunded_minor
  FROM lab.payment p JOIN lab.customer_order o USING (order_id)
  WHERE p.kind = 'refund' AND p.status = 'succeeded' AND o.status IN ('fulfilled','refunded')
    AND o.placed_at >= '2025-01-01' AND o.placed_at < '2026-01-01' GROUP BY o.tenant_id)
SELECT g.tenant_id, g.gmv_minor, coalesce(r.refunded_minor, 0) AS refunded_minor,
       g.gmv_minor - coalesce(r.refunded_minor, 0) AS net_minor
FROM g LEFT JOIN r USING (tenant_id)""")

ex(id="E4.6", level=4, title="Strictly the priciest in its category", tags="ALL · empty-set trap",
   prompt="Products strictly more expensive than every *other* product in the same category. Uncategorised products (NULL category) are excluded.",
   out="`product_id`",
   trap="`x > ALL (empty set)` is TRUE. For a NULL category the peer set is empty, so every uncategorised product qualifies unless you exclude them explicitly. Also: ties give no winner.",
   key="""SELECT p.product_id FROM lab.product p
WHERE p.category_id IS NOT NULL
  AND p.price_minor > ALL (SELECT q.price_minor FROM lab.product q
                           WHERE q.category_id = p.category_id AND q.product_id <> p.product_id)""")

ex(id="E4.7", level=4, title="Latest order per user (tenant 3)", tags="LATERAL · top-1 per group",
   prompt="For each user of tenant 3 who has orders: their most recent order (`placed_at DESC`, tie → higher `order_id`).",
   out="`user_id, order_id, placed_at`",
   trap="`LATERAL` runs the subquery once per outer row and can reference it — the SQL for-each loop. Missing index on `(user_id, placed_at)` makes it a seq scan per user (PX-1).",
   key="""SELECT u.user_id, o.order_id, o.placed_at
FROM lab.app_user u
CROSS JOIN LATERAL (SELECT order_id, placed_at FROM lab.customer_order c WHERE c.user_id = u.user_id
                    ORDER BY placed_at DESC, order_id DESC LIMIT 1) o
WHERE u.tenant_id = 3""")

ex(id="E4.8", level=4, title="Relational division: bought all three", tags="division · GROUP BY / HAVING · double NOT EXISTS",
   prompt="Users who have ordered **all** of products 1, 6 and 11 (any status).",
   out="`user_id`",
   trap="Division has two standard forms: `HAVING count(DISTINCT product_id) = 3` (fast, needs the count) and double `NOT EXISTS` (works for a *set stored in a table*). Write both.",
   key="""SELECT o.user_id FROM lab.customer_order o JOIN lab.order_line l USING (order_id)
WHERE l.product_id IN (1, 6, 11)
GROUP BY o.user_id HAVING count(DISTINCT l.product_id) = 3""")
```

#### `ex_l5_8.py`

Exercise keys, levels 5–8.

```python

EX = []
def ex(**kw):
    kw.setdefault("ordered", False)
    EX.append(kw)

# ---------------------------------------------------------------- LEVEL 5 : window functions
ex(id="E5.1", level=5, title="Top-3 price ranks per category", tags="dense_rank · rank vs row_number",
   prompt="For every category (ignore uncategorised products): products whose **dense** price rank (highest price = 1) is 1, 2 or 3 within the category.",
   out="`category_id, product_id, price_minor, rnk`",
   trap="`rank` leaves gaps after ties, `dense_rank` doesn't, `row_number` breaks ties arbitrarily. You cannot filter on a window function in WHERE — wrap in a subquery/CTE.",
   key="""SELECT category_id, product_id, price_minor, rnk FROM (
  SELECT category_id, product_id, price_minor,
         dense_rank() OVER (PARTITION BY category_id ORDER BY price_minor DESC) AS rnk
  FROM lab.product WHERE category_id IS NOT NULL) x
WHERE rnk <= 3""")

ex(id="E5.2", level=5, title="Running GMV, tenant 1, March 2025", tags="running total · frame · aggregate then window",
   prompt="Tenant 1, fulfilled orders placed in March 2025: per UTC day the GMV, plus the cumulative GMV since 1 March.",
   out="`day, gmv_minor, cum_gmv_minor` (ordered by day)",
   trap="Aggregate to days **first** (CTE), then window over the days. The default frame with `ORDER BY` is `RANGE UNBOUNDED PRECEDING … CURRENT ROW` — peers (ties) are included; spell `ROWS` when you mean rows.",
   ordered=True,
   key="""WITH d AS (SELECT placed_at::date AS day, sum(total_minor) AS gmv_minor FROM lab.customer_order
            WHERE tenant_id = 1 AND status = 'fulfilled' AND placed_at >= '2025-03-01' AND placed_at < '2025-04-01' GROUP BY 1)
SELECT day, gmv_minor, sum(gmv_minor) OVER (ORDER BY day ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cum_gmv_minor
FROM d ORDER BY day""")

ex(id="E5.3", level=5, title="Days since the previous order", tags="lag · partitions",
   prompt="For users 1–20: each order with the number of whole days since the same user's previous order (NULL for their first). Use calendar days (`placed_at::date`).",
   out="`user_id, order_id, placed_at, gap_days`",
   trap="`lag` needs a total order inside the partition — add `order_id` as tie-break. `date - date` is an integer in Postgres; timestamp − timestamp is an interval.",
   key="""SELECT user_id, order_id, placed_at,
       placed_at::date - lag(placed_at::date) OVER (PARTITION BY user_id ORDER BY placed_at, order_id) AS gap_days
FROM lab.customer_order WHERE user_id BETWEEN 1 AND 20""")

ex(id="E5.4", level=5, title="Top-2 orders per user", tags="row_number · top-N per group",
   prompt="For users 1–50: their two largest orders by `total_minor` (ties → lower `order_id`), with the position 1 or 2.",
   out="`user_id, order_id, total_minor, rn`",
   trap="`LIMIT 2` gives two rows overall, not per user. The tie-break is part of the spec — without it two correct answers differ.",
   key="""SELECT user_id, order_id, total_minor, rn FROM (
  SELECT user_id, order_id, total_minor,
         row_number() OVER (PARTITION BY user_id ORDER BY total_minor DESC, order_id) AS rn
  FROM lab.customer_order WHERE user_id BETWEEN 1 AND 50) x WHERE rn <= 2""")

ex(id="E5.5", level=5, title="Tenant share of 2025 GMV", tags="sum() OVER () · ratio to total",
   prompt="Per tenant: fulfilled GMV in 2025 and its percentage of the all-tenant total, rounded to 2 decimals.",
   out="`tenant_id, gmv_minor, pct`",
   trap="Window over the *aggregated* result: `sum(sum(x)) OVER ()`. Cast to numeric before dividing.",
   key="""SELECT tenant_id, sum(total_minor) AS gmv_minor,
       round(100.0 * sum(total_minor) / sum(sum(total_minor)) OVER (), 2) AS pct
FROM lab.customer_order
WHERE status = 'fulfilled' AND placed_at >= '2025-01-01' AND placed_at < '2026-01-01'
GROUP BY tenant_id""")

ex(id="E5.6", level=5, title="Price quartiles, tenant 2", tags="ntile · bucket boundaries",
   prompt="Live products of tenant 2 split into 4 price quartiles with `ntile(4)` ordered by price ascending then `product_id`.",
   out="`product_id, price_minor, quartile`",
   trap="`ntile` splits by **row count**, not by value — equal prices can land in different tiles; and if N is not divisible by 4 the first tiles get the extra rows.",
   key="""SELECT product_id, price_minor, ntile(4) OVER (ORDER BY price_minor, product_id) AS quartile
FROM lab.product WHERE tenant_id = 2 AND discontinued_at IS NULL""")

ex(id="E5.7", level=5, title="First and last price", tags="first_value · last_value · frame trap",
   prompt="For products 1–20: the first and last `price_minor` in `product_price_history` (by `valid_from`) and the change (last − first).",
   out="`product_id, first_price, last_price, delta`",
   trap="`last_value(x) OVER (ORDER BY t)` returns the *current* row when the default frame stops at CURRENT ROW. You need `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`, or use `first_value` with a reversed ORDER BY.",
   key="""SELECT DISTINCT product_id,
       first_value(price_minor) OVER w AS first_price,
       last_value(price_minor)  OVER w AS last_price,
       last_value(price_minor) OVER w - first_value(price_minor) OVER w AS delta
FROM lab.product_price_history WHERE product_id BETWEEN 1 AND 20
WINDOW w AS (PARTITION BY product_id ORDER BY valid_from ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)""")

ex(id="E5.8", level=5, title="7-day moving average of daily orders", tags="ROWS frame · moving average · warm-up rows",
   prompt="Tenant 2, orders placed in February 2025: per day the order count and the average of the current and previous 6 days' counts, rounded to 2 decimals. Emit the average only when a full 7-day window exists inside February (from 7 Feb).",
   out="`day, n, avg7` (ordered by day)",
   trap="A `ROWS 6 PRECEDING` frame silently shrinks at the start — you must suppress the warm-up rows yourself. `ROWS` counts rows, so missing days (gaps) would silently stretch the window; here there are no empty days — say why you checked.",
   ordered=True,
   key="""SELECT day, n, avg7 FROM (
  SELECT day, n, row_number() OVER (ORDER BY day) AS rn,
         round(avg(n) OVER (ORDER BY day ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS avg7
  FROM (SELECT placed_at::date AS day, count(*) AS n FROM lab.customer_order
        WHERE tenant_id = 2 AND placed_at >= '2025-02-01' AND placed_at < '2025-03-01' GROUP BY 1) d) x
WHERE rn >= 7 ORDER BY day""")

# ---------------------------------------------------------------- LEVEL 6 : advanced windows
ex(id="E6.1", level=6, title="Longest login streak", tags="gaps and islands · row_number difference",
   prompt="From `login_day` (users 1–200, 120 days): each user's longest run of **consecutive** days and the day it started (earliest start on ties).",
   out="`user_id, streak_len, streak_start`",
   trap="Consecutive days share a constant `day − row_number()`. Do not use `count(*)` per user, and do not forget that the PK already guarantees no duplicate days (if it didn't, dedupe before numbering).",
   key="""WITH g AS (SELECT user_id, day, day - (row_number() OVER (PARTITION BY user_id ORDER BY day))::int AS grp FROM lab.login_day),
runs AS (SELECT user_id, min(day) AS streak_start, count(*) AS streak_len FROM g GROUP BY user_id, grp),
ranked AS (SELECT *, row_number() OVER (PARTITION BY user_id ORDER BY streak_len DESC, streak_start) AS rn FROM runs)
SELECT user_id, streak_len, streak_start FROM ranked WHERE rn = 1""")

ex(id="E6.2", level=6, title="Sessionise the event stream", tags="sessionization · lag · cumulative sum",
   prompt="For identified users (`user_id IS NOT NULL`): a new session starts when the gap to the user's previous event is **> 30 minutes** (or there is no previous event). Return one row per session: user, session number (1-based per user, by time), event count, first and last event time.",
   out="`user_id, session_no, n_events, started_at, ended_at`",
   trap="Three steps: (1) `lag` to get the gap, (2) flag `gap > interval '30 minutes' OR gap IS NULL`, (3) running `sum(flag)` as the session id. Ties on `occurred_at` need an `event_id` tie-break.",
   key="""WITH e AS (SELECT user_id, event_id, occurred_at,
                   occurred_at - lag(occurred_at) OVER (PARTITION BY user_id ORDER BY occurred_at, event_id) AS gap
            FROM lab.event WHERE user_id IS NOT NULL),
f AS (SELECT *, CASE WHEN gap IS NULL OR gap > interval '30 minutes' THEN 1 ELSE 0 END AS is_start FROM e),
s AS (SELECT *, sum(is_start) OVER (PARTITION BY user_id ORDER BY occurred_at, event_id) AS session_no FROM f)
SELECT user_id, session_no, count(*) AS n_events, min(occurred_at) AS started_at, max(occurred_at) AS ended_at
FROM s GROUP BY user_id, session_no""")

ex(id="E6.3", level=6, title="Ordered funnel", tags="conditional aggregation · ordered steps",
   prompt="How many identified users performed `add_to_cart`, later `checkout_start`, later `purchase` — in that order (each step strictly after the previous, using each user's **first** occurrence of the step)? One number, plus the counts that reached step 1 and step 2 as a funnel.",
   out="`n_cart, n_checkout, n_purchase` (one row)",
   trap="`count(DISTINCT user_id) WHERE event_type = …` per step ignores order. Compute each user's first time per step with `min(…) FILTER`, then compare the timestamps.",
   key="""WITH t AS (SELECT user_id,
       min(occurred_at) FILTER (WHERE event_type = 'add_to_cart')    AS t_cart,
       min(occurred_at) FILTER (WHERE event_type = 'checkout_start') AS t_co,
       min(occurred_at) FILTER (WHERE event_type = 'purchase')       AS t_buy
     FROM lab.event WHERE user_id IS NOT NULL GROUP BY user_id)
SELECT count(*) FILTER (WHERE t_cart IS NOT NULL) AS n_cart,
       count(*) FILTER (WHERE t_cart < t_co) AS n_checkout,
       count(*) FILTER (WHERE t_cart < t_co AND t_co < t_buy) AS n_purchase
FROM t""")

ex(id="E6.4", level=6, title="Price in effect at order time (as-of join)", tags="as-of join · LATERAL · temporal correctness",
   prompt="For order lines of orders placed **before 2025-01-04**: the list price that was in effect at `placed_at` (the history row with the greatest `valid_from <= placed_at`), and the lines where the price actually charged (`unit_price_minor`) differs from it.",
   out="`order_id, line_no, unit_price_minor, price_at_order`",
   trap="A plain equi-join on `product_id` returns three rows per line. Use `LATERAL … ORDER BY valid_from DESC LIMIT 1` (or `DISTINCT ON`, or a window). The `<=` boundary is inclusive: an order at exactly `valid_from` sees the *new* price. This is the same shape as the point-in-time joins of DD-05.",
   key="""SELECT l.order_id, l.line_no, l.unit_price_minor, h.price_minor AS price_at_order
FROM lab.order_line l JOIN lab.customer_order o USING (order_id)
CROSS JOIN LATERAL (SELECT price_minor FROM lab.product_price_history h
                    WHERE h.product_id = l.product_id AND h.valid_from <= o.placed_at
                    ORDER BY h.valid_from DESC LIMIT 1) h
WHERE o.placed_at < '2025-01-04' AND l.unit_price_minor <> h.price_minor""")

ex(id="E6.5", level=6, title="Orders in the previous 30 days", tags="RANGE frame with interval · self-window",
   prompt="For users 1–20: each order and how many **other** orders the same user placed in the 30 days before it (`placed_at − 30 days` up to and including this order's time, excluding itself).",
   out="`user_id, order_id, prior_30d`",
   trap="A `RANGE BETWEEN INTERVAL '30 days' PRECEDING AND CURRENT ROW` frame includes the current row *and its peers*; subtract 1 and think about equal timestamps. `ROWS 30 PRECEDING` would count rows, not days.",
   key="""SELECT user_id, order_id,
       (count(*) OVER (PARTITION BY user_id ORDER BY placed_at RANGE BETWEEN INTERVAL '30 days' PRECEDING AND CURRENT ROW) - 1) AS prior_30d
FROM lab.customer_order WHERE user_id BETWEEN 1 AND 20""")

ex(id="E6.6", level=6, title="Signup-cohort activation", tags="cohort analysis · date_trunc · conditional counts",
   prompt="Cohort = signup month (`date_trunc('month', created_at)`). For each cohort: size, and how many of its users placed at least one order in the **calendar month after** their signup month.",
   out="`cohort_month, size, active_next_month`",
   trap="Two grains at once (users, then orders). Compute *per-user* activation first (`EXISTS`), then aggregate by cohort — do not join users to orders and `count(*)`.",
   key="""SELECT date_trunc('month', u.created_at)::date AS cohort_month, count(*) AS size,
       count(*) FILTER (WHERE EXISTS (
          SELECT 1 FROM lab.customer_order o WHERE o.user_id = u.user_id
            AND o.placed_at >= date_trunc('month', u.created_at) + interval '1 month'
            AND o.placed_at <  date_trunc('month', u.created_at) + interval '2 months')) AS active_next_month
FROM lab.app_user u GROUP BY 1""")

ex(id="E6.7", level=6, title="Dedupe events, keep the first", tags="row_number · deduplication · planted test data",
   prompt="Some pipelines deliver twice. Treat two events as the same delivery when `(user_id, event_type, occurred_at)` are equal (NULL users count as equal to each other). Run your query against this **planted** input `e` (the real table plus 6,000 duplicate deliveries with ids +1,000,000): `SELECT * FROM lab.event UNION ALL SELECT event_id + 1000000, tenant_id, user_id, event_type, occurred_at, payload FROM lab.event WHERE event_id % 10 = 0`. Return the `event_id`s that are **not** the lowest id in their duplicate group.",
   out="`event_id`",
   trap="`PARTITION BY` treats NULLs as one group (unlike `=`). Run the query on the *un-planted* table too: it must return 0 rows — an empty result is a valid, testable answer, but only if you have also seen it return the planted rows.",
   key="""SELECT event_id FROM (
  SELECT event_id, row_number() OVER (PARTITION BY user_id, event_type, occurred_at ORDER BY event_id) AS rn
  FROM (SELECT * FROM lab.event UNION ALL
        SELECT event_id + 1000000, tenant_id, user_id, event_type, occurred_at, payload FROM lab.event WHERE event_id % 10 = 0) e) x
WHERE rn > 1""")

# ---------------------------------------------------------------- LEVEL 7 : recursion
ex(id="E7.1", level=7, title="Category paths", tags="recursive CTE · tree · path",
   prompt="For tenant 1's category tree: every category with its depth (root = 0) and the `' > '`-joined path of **names** from the root.",
   out="`category_id, depth, path`",
   trap="A recursive CTE = anchor (roots: `parent_id IS NULL`) `UNION ALL` recursive step joining on `parent_id`. Termination is guaranteed only if the data has no cycles — the seed does, a hostile import might not (E7.5).",
   key="""WITH RECURSIVE t AS (
  SELECT category_id, 0 AS depth, name::text AS path FROM lab.category WHERE tenant_id = 1 AND parent_id IS NULL
  UNION ALL
  SELECT c.category_id, t.depth + 1, t.path || ' > ' || c.name
  FROM lab.category c JOIN t ON c.parent_id = t.category_id)
SELECT category_id, depth, path FROM t""")

ex(id="E7.2", level=7, title="Products in a subtree", tags="recursive CTE · rollup up the tree",
   prompt="For every category of tenant 1: the number of products attached to it **or any descendant**.",
   out="`category_id, subtree_products`",
   trap="Materialise (ancestor, descendant) pairs, then join products to *descendant* and group by *ancestor*. A category with no products still needs a row — LEFT JOIN.",
   key="""WITH RECURSIVE a AS (
  SELECT category_id AS anc, category_id AS des FROM lab.category WHERE tenant_id = 1
  UNION ALL
  SELECT a.anc, c.category_id FROM a JOIN lab.category c ON c.parent_id = a.des)
SELECT a.anc AS category_id, count(p.product_id) AS subtree_products
FROM a LEFT JOIN lab.product p ON p.category_id = a.des GROUP BY a.anc""")

ex(id="E7.3", level=7, title="Referral roots and depth", tags="recursive CTE · forest · depth",
   prompt="Users form a referral forest (`referred_by` → parent). For every user: the root user of their tree and their depth (root = 0).",
   out="`user_id, root_id, depth`",
   trap="Roots are the rows with `referred_by IS NULL`; carry `root_id` through the recursion instead of recomputing it. Prove termination: `referred_by < user_id` holds in this seed, so no cycle — state that invariant, don't assume it.",
   key="""WITH RECURSIVE f AS (
  SELECT user_id, user_id AS root_id, 0 AS depth FROM lab.app_user WHERE referred_by IS NULL
  UNION ALL
  SELECT u.user_id, f.root_id, f.depth + 1 FROM lab.app_user u JOIN f ON u.referred_by = f.user_id)
SELECT user_id, root_id, depth FROM f""")

ex(id="E7.4", level=7, title="Biggest referral tree", tags="recursive CTE · aggregate over recursion",
   prompt="The root user whose tree (including the root) has the most members; ties → lowest `user_id`.",
   out="`root_id, tree_size`",
   trap="Aggregate *after* the recursion. `ORDER BY tree_size DESC, root_id LIMIT 1`.",
   probe="""WITH RECURSIVE f AS (
  SELECT user_id, user_id AS root_id FROM lab.app_user WHERE referred_by IS NULL
  UNION ALL SELECT u.user_id, f.root_id FROM lab.app_user u JOIN f ON u.referred_by = f.user_id)
SELECT root_id, count(*) AS tree_size FROM f GROUP BY root_id ORDER BY tree_size DESC, root_id LIMIT 1""",
   ordered=True, show=3,
   key="""WITH RECURSIVE f AS (
  SELECT user_id, user_id AS root_id FROM lab.app_user WHERE referred_by IS NULL
  UNION ALL SELECT u.user_id, f.root_id FROM lab.app_user u JOIN f ON u.referred_by = f.user_id)
SELECT root_id, count(*) AS tree_size FROM f GROUP BY root_id ORDER BY tree_size DESC, root_id LIMIT 1""")

ex(id="E7.5", level=7, title="Find the cycle", tags="recursive CTE · cycle detection · path array",
   prompt="Directed edges are given inline: `(1,2),(2,3),(3,1),(4,5),(5,6)`. Return every node that lies on a cycle.",
   out="`node`",
   trap="Carry a `path` array and stop when the next node is already in it (`NOT next = ANY(path)`); a node is on a cycle if it can reach itself. PostgreSQL 14+ also has `CYCLE … SET … USING` — write it both ways.",
   show=5,
   key="""WITH RECURSIVE e(a, b) AS (VALUES (1,2),(2,3),(3,1),(4,5),(5,6)),
w AS (
  SELECT a AS start, b AS node, ARRAY[a, b] AS path FROM e
  UNION ALL
  SELECT w.start, e.b, w.path || e.b FROM w JOIN e ON e.a = w.node WHERE e.b <> ALL (w.path[2:]))
SELECT DISTINCT start AS node FROM w WHERE node = start""")

# ---------------------------------------------------------------- LEVEL 8 : time, JSON, text, cleaning
ex(id="E8.1", level=8, title="Average delivery time by carrier", tags="interval arithmetic · extract(epoch)",
   prompt="For delivered shipments: per carrier, the count and the mean transit time in **days** (shipped → delivered) rounded to 2 decimals.",
   out="`carrier, n, avg_days`",
   trap="`avg(interval)` is legal but unreadable; convert with `extract(epoch FROM …) / 86400` — as `numeric`, not float, before rounding. NULL `delivered_at` rows are excluded by the filter, not by luck.",
   key="""SELECT carrier, count(*) AS n,
       round(avg(extract(epoch FROM (delivered_at - shipped_at)) / 86400)::numeric, 2) AS avg_days
FROM lab.shipment WHERE delivered_at IS NOT NULL GROUP BY carrier""")

ex(id="E8.2", level=8, title="Stuck shipments as of a fixed instant", tags="reproducible time · never now()",
   prompt="Shipments not delivered more than 14 days after shipping, **as of `2026-01-01 00:00 UTC`** (undelivered and shipped before 2025-12-18).",
   out="`shipment_id`",
   trap="Never call `now()` in a graded query — the answer changes daily. Parameterise the 'as-of' instant. Same principle as the ledger's determinism rules (DD-03).",
   key="""SELECT shipment_id FROM lab.shipment
WHERE delivered_at IS NULL AND shipped_at < timestamptz '2026-01-01 00:00+00' - interval '14 days'""")

ex(id="E8.3", level=8, title="UTC day vs New York day", tags="AT TIME ZONE · DST",
   prompt="How many orders have a **different calendar date** in `America/New_York` than in UTC? One number.",
   out="`n`",
   trap="`ts AT TIME ZONE 'x'` on a `timestamptz` returns a *timestamp without zone* in that zone; on a plain `timestamp` it does the reverse. Get the direction right and test across the 2025-03-09 DST change.",
   key="""SELECT count(*) AS n FROM lab.customer_order
WHERE (placed_at AT TIME ZONE 'America/New_York')::date <> (placed_at AT TIME ZONE 'UTC')::date""")

ex(id="E8.4", level=8, title="Orders per ISO week", tags="date_trunc('week') · week boundaries",
   prompt="Orders placed in 2025 grouped by ISO week (Monday start): week start date and count.",
   out="`week_start, n`",
   trap="`date_trunc('week')` starts on Monday (ISO); BigQuery's `DATE_TRUNC(d, WEEK)` starts on Sunday. The first/last week straddles the year boundary.",
   key="""SELECT date_trunc('week', placed_at)::date AS week_start, count(*) AS n
FROM lab.customer_order WHERE placed_at >= '2025-01-01' AND placed_at < '2026-01-01' GROUP BY 1""")

ex(id="E8.5", level=8, title="Red eco products", tags="JSONB · @> · ? operator",
   prompt="Products whose `attrs` has `color = 'red'` **and** whose `attrs.tags` array contains `'eco'`.",
   out="`product_id`",
   trap="`attrs->>'color'` returns text; `attrs @> '{\"color\":\"red\"}'` is index-friendly (GIN). `attrs->'tags' ? 'eco'` tests membership in an array of strings. A missing key yields NULL, not false.",
   key="""SELECT product_id FROM lab.product WHERE attrs @> '{"color":"red"}' AND attrs->'tags' ? 'eco'""")

ex(id="E8.6", level=8, title="Search latency by query term", tags="JSONB extraction · casts",
   prompt="For `search` events: per query term (`payload->>'q'`) the number of events and the average `payload->>'ms'` rounded to 1 decimal.",
   out="`q, n, avg_ms`",
   trap="`->>` returns text — cast before averaging: `(payload->>'ms')::int`. A non-numeric value would fail the whole query — in production, validate on write.",
   key="""SELECT payload->>'q' AS q, count(*) AS n, round(avg((payload->>'ms')::int), 1) AS avg_ms
FROM lab.event WHERE event_type = 'search' GROUP BY 1""")

ex(id="E8.7", level=8, title="Products per tag", tags="jsonb_array_elements_text · unnesting",
   prompt="Explode `attrs.tags` and count products per tag.",
   out="`tag, n`",
   trap="A set-returning function in FROM (`CROSS JOIN LATERAL jsonb_array_elements_text(attrs->'tags')`) drops products with no tags — usually what you want; say so. In BigQuery this is `UNNEST`.",
   key="""SELECT tag, count(*) AS n FROM lab.product p
CROSS JOIN LATERAL jsonb_array_elements_text(p.attrs->'tags') AS tag GROUP BY tag""")

ex(id="E8.8", level=8, title="Clean and dedupe emails", tags="trim · lower · regex · dedupe",
   prompt="From `lab.stg_import`: normalise `email_text` with `lower(trim(…))`, keep only values that match `^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$`, and keep the **lowest `row_id`** for each normalised address.",
   out="`row_id, email_norm`",
   trap="Empty string and NULL are both invalid; `frank@example` has no dot. Normalise **before** deduping, or 'Ann@Example.com ' and 'ann@example.com' survive as two people.",
   show=15,
   key="""SELECT row_id, email_norm FROM (
  SELECT row_id, lower(trim(email_text)) AS email_norm,
         row_number() OVER (PARTITION BY lower(trim(email_text)) ORDER BY row_id) AS rn
  FROM lab.stg_import
  WHERE lower(trim(email_text)) ~ '^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$') x
WHERE rn = 1""")

ex(id="E8.9", level=8, title="Parse money text into minor units", tags="regexp · CASE · safe casts",
   prompt="Convert `amount_text` to integer **minor units** (×100, rounded half up). Accept an optional leading `-`, optional `$`, thousands separators `,` (only in groups of exactly three) and an optional decimal part with `.`; surrounding spaces are ignored. Anything else — `12,50`, `abc`, `1e3`, NULL — becomes NULL.",
   out="`row_id, amount_minor`",
   trap="Decide the rule for `12,50` (European decimal comma) explicitly — here it is *invalid*, never guessed. Validate with a regex **before** casting; a bare `::numeric` on bad text aborts the whole statement.",
   show=15,
   key="""SELECT row_id,
  CASE WHEN c ~ '^-?([0-9]{1,3}(,[0-9]{3})+|[0-9]+)(\\.[0-9]+)?$'
       THEN round(replace(c, ',', '')::numeric * 100)::bigint END AS amount_minor
FROM (SELECT row_id, replace(trim(amount_text), '$', '') AS c FROM lab.stg_import) s""")

ex(id="E8.10", level=8, title="Write a total date parser", tags="user-defined function · exception handling · dialect",
   prompt="Create `work.try_date(text) RETURNS date` that returns a date for: ISO `YYYY-MM-DD` (after trimming, and also when followed by a `T…` time), `MM/DD/YYYY`, and `D Mon YYYY` (e.g. `1 Mar 2025`); **NULL** for anything else, including impossible dates like `2025-13-40` and `2025-02-29`. Then `SELECT row_id, work.try_date(signup_text)` over `stg_import`.",
   out="`row_id, d`",
   trap="A cast error aborts the statement; catch it in a `BEGIN … EXCEPTION WHEN others THEN RETURN NULL` block (PL/pgSQL). Postgres 16 adds `pg_input_is_valid()`; BigQuery has `SAFE.PARSE_DATE`, SQL Server `TRY_CONVERT`. `2025-02-29` must fail — 2025 is not a leap year.",
   setup="""CREATE OR REPLACE FUNCTION work.try_date(t text) RETURNS date LANGUAGE plpgsql IMMUTABLE AS $$
DECLARE s text := btrim(t);
BEGIN
  IF s IS NULL OR s = '' THEN RETURN NULL; END IF;
  IF s ~ '^\\d{4}-\\d{2}-\\d{2}(T.*)?$' THEN RETURN to_date(left(s, 10), 'YYYY-MM-DD')::date;
  ELSIF s ~ '^\\d{1,2}/\\d{1,2}/\\d{4}$' THEN RETURN to_date(s, 'MM/DD/YYYY');
  ELSIF s ~ '^\\d{1,2} [A-Za-z]{3} \\d{4}$' THEN RETURN to_date(s, 'DD Mon YYYY');
  END IF;
  RETURN NULL;
EXCEPTION WHEN others THEN RETURN NULL;
END $$;""",
   probe="SELECT row_id, work.try_date(signup_text) AS d FROM lab.stg_import",
   show=15,
   key="""-- function body as in the setup above; then:
SELECT row_id, work.try_date(signup_text) AS d FROM lab.stg_import""")
```

#### `ex_l9_13.py`

Exercise keys, levels 9–13.

```python

EX = []
def ex(**kw):
    kw.setdefault("ordered", False)
    EX.append(kw)

TRY = """CREATE OR REPLACE FUNCTION lab.try(stmt text) RETURNS boolean LANGUAGE plpgsql AS $f$
BEGIN EXECUTE stmt; RETURN true; EXCEPTION WHEN others THEN RETURN false; END $f$;"""

# ---------------------------------------------------------------- LEVEL 9 : DML
ex(id="E9.1", level=9, title="Materialise a daily GMV table", tags="CREATE TABLE · INSERT … SELECT · PK",
   prompt="In schema `work`, create `tenant_daily_gmv(tenant_id int, day date, gmv_minor bigint NOT NULL, PRIMARY KEY (tenant_id, day))` and fill it with fulfilled-order GMV per tenant per UTC day for **January 2025**.",
   out="table contents `tenant_id, day, gmv_minor`",
   trap="Column list on `INSERT` (never rely on positional order across a migration). Create the constraint *with* the table so a re-run fails loudly instead of duplicating. All DML in this level is graded inside a transaction that is rolled back — you can retry freely.",
   stmts="""CREATE TABLE work.tenant_daily_gmv (tenant_id int, day date, gmv_minor bigint NOT NULL, PRIMARY KEY (tenant_id, day));
INSERT INTO work.tenant_daily_gmv (tenant_id, day, gmv_minor)
SELECT tenant_id, placed_at::date, sum(total_minor) FROM lab.customer_order
WHERE status = 'fulfilled' AND placed_at >= '2025-01-01' AND placed_at < '2025-02-01' GROUP BY 1, 2;""",
   probe="SELECT * FROM work.tenant_daily_gmv",
   key="""CREATE TABLE work.tenant_daily_gmv (tenant_id int, day date, gmv_minor bigint NOT NULL, PRIMARY KEY (tenant_id, day));
INSERT INTO work.tenant_daily_gmv (tenant_id, day, gmv_minor)
SELECT tenant_id, placed_at::date, sum(total_minor) FROM lab.customer_order
WHERE status = 'fulfilled' AND placed_at >= '2025-01-01' AND placed_at < '2025-02-01' GROUP BY 1, 2;""")

ex(id="E9.2", level=9, title="Repair corrupted totals", tags="UPDATE … FROM · IS DISTINCT FROM",
   prompt="Setup gives you `work.o`, a copy of `customer_order` in which every 100th order (`order_id % 100 = 0`, 200 rows) has `total_minor = 0`. Repair **only the wrong rows** so that `total_minor` equals the sum of `qty × unit_price_minor` of its lines. The statement must report `UPDATE 200`.",
   out="`work.o` equals `lab.customer_order` on `(order_id, total_minor)`",
   trap="Updating *every* row (no `WHERE … IS DISTINCT FROM`) rewrites 20,000 tuples — table bloat and WAL for no reason. `IS DISTINCT FROM`, not `<>`, so a NULL total would be repaired too.",
   setup="""CREATE TABLE work.o AS SELECT * FROM lab.customer_order;
UPDATE work.o SET total_minor = 0 WHERE order_id % 100 = 0;""",
   stmts="""UPDATE work.o o SET total_minor = s.t
FROM (SELECT order_id, sum(qty::bigint * unit_price_minor) AS t FROM lab.order_line GROUP BY order_id) s
WHERE s.order_id = o.order_id AND o.total_minor IS DISTINCT FROM s.t;""",
   probe="SELECT order_id, total_minor FROM work.o",
   key="""UPDATE work.o o SET total_minor = s.t
FROM (SELECT order_id, sum(qty::bigint * unit_price_minor) AS t FROM lab.order_line GROUP BY order_id) s
WHERE s.order_id = o.order_id AND o.total_minor IS DISTINCT FROM s.t;""")

ex(id="E9.3", level=9, title="Idempotent daily load (upsert)", tags="INSERT … ON CONFLICT DO UPDATE · idempotency",
   prompt="Create `work.daily_orders(day date PRIMARY KEY, n int NOT NULL)`. Write one statement that loads the count of orders per UTC day for all of 2025 and can be **run twice with the same result**.",
   out="`day, n`",
   trap="`SET n = daily_orders.n + EXCLUDED.n` is *not* idempotent (a re-run doubles). `SET n = EXCLUDED.n` is. If your source query returned two rows for one day in a single statement you would get `ON CONFLICT DO UPDATE command cannot affect row a second time` — aggregate first. Idempotent writes are the whole point of at-least-once pipelines (A9).",
   stmts="""CREATE TABLE work.daily_orders (day date PRIMARY KEY, n int NOT NULL);
INSERT INTO work.daily_orders (day, n) SELECT placed_at::date, count(*) FROM lab.customer_order GROUP BY 1
ON CONFLICT (day) DO UPDATE SET n = EXCLUDED.n;
INSERT INTO work.daily_orders (day, n) SELECT placed_at::date, count(*) FROM lab.customer_order GROUP BY 1
ON CONFLICT (day) DO UPDATE SET n = EXCLUDED.n;""",
   probe="SELECT * FROM work.daily_orders",
   key="""INSERT INTO work.daily_orders (day, n)
SELECT placed_at::date, count(*) FROM lab.customer_order GROUP BY 1
ON CONFLICT (day) DO UPDATE SET n = EXCLUDED.n;""")

ex(id="E9.4", level=9, title="Delete the double-submitted reviews", tags="DELETE … USING · self-join delete · RETURNING",
   prompt="Setup gives `work.r`, a copy of `review`. Delete duplicate `(product_id, user_id)` reviews, **keeping the newest** (highest `review_id`). Report how many were deleted (`DELETE 400`).",
   out="`work.r` keeps 6,000 rows",
   trap="Test the *keep* rule on a tiny sample first. `DELETE` on a self-join needs `USING`; without a total order you can delete both copies. Run it inside `BEGIN … ROLLBACK` in real life until the count matches your prediction.",
   setup="CREATE TABLE work.r AS SELECT * FROM lab.review;",
   stmts="""DELETE FROM work.r a USING work.r b
WHERE a.product_id = b.product_id AND a.user_id = b.user_id AND a.review_id < b.review_id;""",
   probe="SELECT review_id FROM work.r",
   key="""DELETE FROM work.r a USING work.r b
WHERE a.product_id = b.product_id AND a.user_id = b.user_id AND a.review_id < b.review_id;""")

ex(id="E9.5", level=9, title="Sync stock with MERGE", tags="MERGE (PG15+) · three-way sync",
   prompt="Setup gives `work.stock_t` (products 1–10 with `on_hand`) and `work.stock_feed` (a partner feed). With **one `MERGE`**: rows in both → update `on_hand`, **except** feed `on_hand = 0` → delete the target row; feed rows not in target → insert.",
   out="`work.stock_t` afterwards (small — check by eye)",
   trap="`MERGE` arrived in PostgreSQL 15; `WHEN NOT MATCHED BY SOURCE` only in 17 — so 'delete rows missing from the feed' cannot be done in one 15/16 MERGE. Many-to-one source rows raise a cardinality error. SQL Server, Oracle, BigQuery all have `MERGE` with dialect differences (Rosetta table).",
   setup="""CREATE TABLE work.stock_t AS SELECT product_id, on_hand FROM lab.stock WHERE product_id <= 10;
CREATE TABLE work.stock_feed (product_id int PRIMARY KEY, on_hand int NOT NULL);
INSERT INTO work.stock_feed VALUES (1, 500), (2, 0), (3, 7), (11, 33), (12, 44);""",
   stmts="""MERGE INTO work.stock_t t USING work.stock_feed f ON t.product_id = f.product_id
WHEN MATCHED AND f.on_hand = 0 THEN DELETE
WHEN MATCHED THEN UPDATE SET on_hand = f.on_hand
WHEN NOT MATCHED THEN INSERT (product_id, on_hand) VALUES (f.product_id, f.on_hand);""",
   probe="SELECT product_id, on_hand FROM work.stock_t ORDER BY product_id",
   ordered=True, show=12,
   key="""MERGE INTO work.stock_t t USING work.stock_feed f ON t.product_id = f.product_id
WHEN MATCHED AND f.on_hand = 0 THEN DELETE
WHEN MATCHED THEN UPDATE SET on_hand = f.on_hand
WHEN NOT MATCHED THEN INSERT (product_id, on_hand) VALUES (f.product_id, f.on_hand);""")

ex(id="E9.6", level=9, title="Chunked backfill", tags="batching · SKIP LOCKED · WAL/bloat awareness",
   prompt="Setup gives `work.o` (copy of `customer_order`) with a new nullable column `total_major numeric(12,2)`. Backfill `total_minor / 100.0` in chunks of **1,000 rows**, looping until no rows are left. (Here one transaction; in production every chunk commits separately — the OD-08 expand/contract pattern.)",
   out="all 20,000 rows have `total_major` set",
   trap="`WHERE total_major IS NULL … LIMIT` inside a CTE + `UPDATE … RETURNING` is the loop body. One giant `UPDATE` holds locks and WAL for minutes on a real table and blocks vacuum. Chunk size is a *tuning knob*, not a constant.",
   setup="""CREATE TABLE work.o AS SELECT * FROM lab.customer_order;
ALTER TABLE work.o ADD COLUMN total_major numeric(12,2);""",
   stmts="""DO $$ DECLARE n int; BEGIN
  LOOP
    WITH c AS (SELECT order_id FROM work.o WHERE total_major IS NULL ORDER BY order_id LIMIT 1000 FOR UPDATE SKIP LOCKED)
    UPDATE work.o o SET total_major = o.total_minor / 100.0 FROM c WHERE o.order_id = c.order_id;
    GET DIAGNOSTICS n = ROW_COUNT;
    EXIT WHEN n = 0;
  END LOOP;
END $$;""",
   probe="SELECT order_id, total_major FROM work.o",
   key="""DO $$ DECLARE n int; BEGIN
  LOOP
    WITH c AS (SELECT order_id FROM work.o WHERE total_major IS NULL ORDER BY order_id LIMIT 1000 FOR UPDATE SKIP LOCKED)
    UPDATE work.o o SET total_major = o.total_minor / 100.0 FROM c WHERE o.order_id = c.order_id;
    GET DIAGNOSTICS n = ROW_COUNT;
    EXIT WHEN n = 0;
  END LOOP;
END $$;""")

ex(id="E9.7", level=9, title="Archive refunded orders atomically", tags="writable CTE · DELETE … RETURNING",
   prompt="Setup gives `work.o` (copy of `customer_order`) and an empty `work.o_archive (LIKE work.o)`. In **one statement**, move every refunded order from `work.o` into `work.o_archive`.",
   out="`live, archived` counts (18000, 2000)",
   trap="`DELETE … RETURNING *` inside a CTE feeding an `INSERT` is atomic — no window where the row is in both or neither. Doing it as two statements needs a transaction; doing it in the application needs an outbox.",
   setup="""CREATE TABLE work.o AS SELECT * FROM lab.customer_order;
CREATE TABLE work.o_archive (LIKE work.o);""",
   stmts="""WITH moved AS (DELETE FROM work.o WHERE status = 'refunded' RETURNING *)
INSERT INTO work.o_archive SELECT * FROM moved;""",
   probe="SELECT (SELECT count(*) FROM work.o) AS live, (SELECT count(*) FROM work.o_archive) AS archived",
   show=2,
   key="""WITH moved AS (DELETE FROM work.o WHERE status = 'refunded' RETURNING *)
INSERT INTO work.o_archive SELECT * FROM moved;""")

# ---------------------------------------------------------------- LEVEL 10 : DDL & constraints (battery = ordered list of pass/fail)
BAT = "SELECT n, lab.try(sql) AS ok FROM (VALUES {rows}) v(n, sql)"

ex(id="E10.1", level=10, title="Coupon table: constraints as a specification", tags="CHECK · UNIQUE · exactly-one-of · citext-free case-insensitive unique",
   prompt="""Create `work.coupon` so that this **battery of 8 inserts gives exactly the pass/fail vector `T T F F F F F T`**:
1. `('SAVE10', percent_off=10, amount_off_minor=NULL, 2025-01-01 → 2025-02-01)` succeeds · 2. a percent coupon with `percent_off=100` succeeds · 3. `percent_off=0` fails · 4. `percent_off=101` fails · 5. **both** `percent_off` and `amount_off_minor` set fails · 6. **neither** set fails · 7. a second code `'save10'` (different case) fails · 8. an amount coupon `amount_off_minor=500` with `valid_until` NULL succeeds.
(Battery statements are in Appendix B.1.)""",
   out="vector of booleans, ordered by test number",
   trap="'Exactly one of' = `num_nonnulls(percent_off, amount_off_minor) = 1`. Case-insensitive uniqueness needs a *functional* unique index on `lower(code)` (or `citext`). CHECK passes when the expression is NULL — write NOT NULL where you mean it.",
   setup=TRY + """
CREATE TABLE work.coupon (
  coupon_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  code text NOT NULL,
  percent_off int CHECK (percent_off BETWEEN 1 AND 100),
  amount_off_minor int CHECK (amount_off_minor > 0),
  valid_from date, valid_until date,
  CHECK (num_nonnulls(percent_off, amount_off_minor) = 1),
  CHECK (valid_until IS NULL OR valid_from IS NULL OR valid_from < valid_until));
CREATE UNIQUE INDEX coupon_code_ci ON work.coupon (lower(code));""",
   probe="""SELECT n, lab.try(sql) AS ok FROM (VALUES
 (1,$$INSERT INTO work.coupon(code,percent_off,valid_from,valid_until) VALUES ('SAVE10',10,'2025-01-01','2025-02-01')$$),
 (2,$$INSERT INTO work.coupon(code,percent_off) VALUES ('FULL',100)$$),
 (3,$$INSERT INTO work.coupon(code,percent_off) VALUES ('ZERO',0)$$),
 (4,$$INSERT INTO work.coupon(code,percent_off) VALUES ('OVER',101)$$),
 (5,$$INSERT INTO work.coupon(code,percent_off,amount_off_minor) VALUES ('BOTH',10,500)$$),
 (6,$$INSERT INTO work.coupon(code) VALUES ('NONE')$$),
 (7,$$INSERT INTO work.coupon(code,percent_off) VALUES ('save10',5)$$),
 (8,$$INSERT INTO work.coupon(code,amount_off_minor) VALUES ('FIVE',500)$$)) v(n, sql) ORDER BY n""",
   ordered=True, show=8,
   key="""CREATE TABLE work.coupon (
  coupon_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  code text NOT NULL,
  percent_off int CHECK (percent_off BETWEEN 1 AND 100),
  amount_off_minor int CHECK (amount_off_minor > 0),
  valid_from date, valid_until date,
  CHECK (num_nonnulls(percent_off, amount_off_minor) = 1),
  CHECK (valid_until IS NULL OR valid_from IS NULL OR valid_from < valid_until));
CREATE UNIQUE INDEX coupon_code_ci ON work.coupon (lower(code));""")

ex(id="E10.2", level=10, title="Tenant-safe foreign key", tags="composite FK · multi-tenancy · integrity at the schema level",
   prompt="""Create `work.note(note_id bigint PK, tenant_id int NOT NULL, user_id bigint NOT NULL, body text)` so that a note can only reference a user **of the same tenant**. Battery (Appendix B.2) must give `T F F F`: (1) tenant 1 / user 1 ok · (2) tenant 2 / user 1 fails (user 1 is tenant 1's) · (3) tenant 1 / user 999999 fails · (4) NULL tenant fails.""",
   out="vector of booleans",
   trap="`user_id REFERENCES app_user` alone only proves the user *exists*. The composite `FOREIGN KEY (tenant_id, user_id) REFERENCES app_user (tenant_id, user_id)` needs a matching unique constraint on the parent — that is why the lab's `app_user` carries `UNIQUE (tenant_id, user_id)`. This is defence in depth beneath RLS (DD-09).",
   setup=TRY + """
CREATE TABLE work.note (note_id bigint PRIMARY KEY, tenant_id int NOT NULL, user_id bigint NOT NULL, body text,
  FOREIGN KEY (tenant_id, user_id) REFERENCES lab.app_user (tenant_id, user_id));""",
   probe="""SELECT n, lab.try(sql) AS ok FROM (VALUES
 (1,$$INSERT INTO work.note VALUES (1,1,1,'x')$$),
 (2,$$INSERT INTO work.note VALUES (2,2,1,'x')$$),
 (3,$$INSERT INTO work.note VALUES (3,1,999999,'x')$$),
 (4,$$INSERT INTO work.note VALUES (4,NULL,1,'x')$$)) v(n, sql) ORDER BY n""",
   ordered=True, show=4,
   key="""CREATE TABLE work.note (note_id bigint PRIMARY KEY, tenant_id int NOT NULL, user_id bigint NOT NULL, body text,
  FOREIGN KEY (tenant_id, user_id) REFERENCES lab.app_user (tenant_id, user_id));""")

ex(id="E10.3", level=10, title="One active subscription per user", tags="partial unique index · state machine invariants",
   prompt="""`work.subscription(sub_id bigint PK, user_id bigint NOT NULL, status text CHECK (status IN ('active','cancelled')))`. Enforce **at most one `active` row per user**, any number of cancelled. Battery (Appendix B.3) expects `T T T F T`: (1) user 1 active · (2) user 1 cancelled · (3) user 1 cancelled again · (4) user 1 second active — fails · (5) user 2 active.""",
   out="vector of booleans",
   trap="A plain `UNIQUE (user_id, status)` would forbid a second *cancelled* row. The invariant is conditional — a **partial unique index** `… (user_id) WHERE status = 'active'`. Race-free by construction, unlike an application-side check.",
   setup=TRY + """
CREATE TABLE work.subscription (sub_id bigint PRIMARY KEY, user_id bigint NOT NULL, status text NOT NULL CHECK (status IN ('active','cancelled')));
CREATE UNIQUE INDEX one_active ON work.subscription (user_id) WHERE status = 'active';""",
   probe="""SELECT n, lab.try(sql) AS ok FROM (VALUES
 (1,$$INSERT INTO work.subscription VALUES (1,1,'active')$$),
 (2,$$INSERT INTO work.subscription VALUES (2,1,'cancelled')$$),
 (3,$$INSERT INTO work.subscription VALUES (3,1,'cancelled')$$),
 (4,$$INSERT INTO work.subscription VALUES (4,1,'active')$$),
 (5,$$INSERT INTO work.subscription VALUES (5,2,'active')$$)) v(n, sql) ORDER BY n""",
   ordered=True, show=5,
   key="""CREATE UNIQUE INDEX one_active ON work.subscription (user_id) WHERE status = 'active';""")

ex(id="E10.4", level=10, title="No overlapping price validity", tags="EXCLUDE constraint · range types · btree_gist",
   prompt="""`work.price_period(product_id bigint, during daterange, price_minor int)`. Forbid two rows of the **same product** whose periods overlap. Battery (Appendix B.4) expects `T T F T F`: (1) p1 `[2025-01-01,2025-02-01)` · (2) p1 `[2025-02-01,2025-03-01)` (touching is fine) · (3) p1 `[2025-01-15,2025-01-20)` overlaps → fails · (4) p2 same dates as (1) fine · (5) p1 `[2025-02-28,2025-04-01)` overlaps (2) → fails.""",
   out="vector of booleans",
   trap="Uniqueness of `(product_id, valid_from)` does **not** stop overlaps. `EXCLUDE USING gist (product_id WITH =, during WITH &&)` needs `btree_gist` for the `=` part. Half-open ranges `[a,b)` make 'touching' legal. Spanner and BigQuery have no exclusion constraints — you'd enforce in a transaction (Rosetta table).",
   setup=TRY + """
CREATE EXTENSION IF NOT EXISTS btree_gist;
CREATE TABLE work.price_period (product_id bigint NOT NULL, during daterange NOT NULL, price_minor int NOT NULL,
  EXCLUDE USING gist (product_id WITH =, during WITH &&));""",
   probe="""SELECT n, lab.try(sql) AS ok FROM (VALUES
 (1,$$INSERT INTO work.price_period VALUES (1,'[2025-01-01,2025-02-01)',100)$$),
 (2,$$INSERT INTO work.price_period VALUES (1,'[2025-02-01,2025-03-01)',110)$$),
 (3,$$INSERT INTO work.price_period VALUES (1,'[2025-01-15,2025-01-20)',120)$$),
 (4,$$INSERT INTO work.price_period VALUES (2,'[2025-01-01,2025-02-01)',100)$$),
 (5,$$INSERT INTO work.price_period VALUES (1,'[2025-02-28,2025-04-01)',130)$$)) v(n, sql) ORDER BY n""",
   ordered=True, show=5,
   key="""CREATE EXTENSION IF NOT EXISTS btree_gist;
CREATE TABLE work.price_period (product_id bigint NOT NULL, during daterange NOT NULL, price_minor int NOT NULL,
  EXCLUDE USING gist (product_id WITH =, during WITH &&));""")

ex(id="E10.5", level=10, title="Circular references with DEFERRABLE", tags="DEFERRABLE INITIALLY DEFERRED · constraint timing",
   prompt="""Two tables reference each other: `work.a(id PK, b_id → b)` and `work.b(id PK, a_id → a)`. Make it possible to insert `a(1, b_id=1)` and `b(1, a_id=1)` **in one transaction** but impossible to commit a dangling reference. Battery (Appendix B.5) is a `DO` block — expected: block succeeds; then a lone `INSERT INTO a VALUES (2, 99)` inside its own transaction **fails at COMMIT** (not at the INSERT).""",
   out="commit-time failure demonstrated",
   trap="Without `DEFERRABLE INITIALLY DEFERRED` the first insert fails immediately. Deferred checks run at `COMMIT` — so the error surfaces *after* your `INSERT` returned success; app code must handle a failed commit. `SET CONSTRAINTS … DEFERRED` scopes it per transaction.",
   setup=TRY + """
CREATE TABLE work.a (id int PRIMARY KEY, b_id int);
CREATE TABLE work.b (id int PRIMARY KEY, a_id int);
ALTER TABLE work.a ADD FOREIGN KEY (b_id) REFERENCES work.b (id) DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE work.b ADD FOREIGN KEY (a_id) REFERENCES work.a (id) DEFERRABLE INITIALLY DEFERRED;
INSERT INTO work.a VALUES (1, 1); INSERT INTO work.b VALUES (1, 1);
SET CONSTRAINTS ALL IMMEDIATE;""",
   probe="SELECT (SELECT count(*) FROM work.a) AS a_rows, (SELECT count(*) FROM work.b) AS b_rows",
   show=1,
   key="""ALTER TABLE work.a ADD FOREIGN KEY (b_id) REFERENCES work.b (id) DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE work.b ADD FOREIGN KEY (a_id) REFERENCES work.a (id) DEFERRABLE INITIALLY DEFERRED;""")

ex(id="E10.6", level=10, title="Row-level security by tenant", tags="RLS · policies · current_setting · roles",
   prompt="""Enable RLS on `work.o` (a copy of `customer_order`) so that a role `app_rls` sees **only rows where `tenant_id = current_setting('app.tenant_id')::int`**. Then, as `app_rls` with `app.tenant_id = '2'`, count rows per tenant. Predict first: how many rows, which tenants? What happens if the setting is unset?""",
   out="`tenant_id, n` (a single row for tenant 2)",
   trap="RLS does **not** apply to the table owner or superusers unless `FORCE ROW LEVEL SECURITY`. `current_setting('x', true)` returns NULL when unset (no rows), without `true` it raises. Connection-pool reuse means the setting must be `SET LOCAL` per transaction — DD-09 RLS.",
   setup="""CREATE TABLE work.o AS SELECT * FROM lab.customer_order;
ALTER TABLE work.o ENABLE ROW LEVEL SECURITY;
CREATE POLICY tenant_iso ON work.o USING (tenant_id = current_setting('app.tenant_id', true)::int);
CREATE ROLE app_rls NOLOGIN;
GRANT USAGE ON SCHEMA work, lab TO app_rls; GRANT SELECT ON work.o TO app_rls;
SET LOCAL ROLE app_rls; SET LOCAL app.tenant_id = '2';""",
   probe="SELECT tenant_id, count(*) AS n FROM work.o GROUP BY tenant_id",
   show=5,
   key="""ALTER TABLE work.o ENABLE ROW LEVEL SECURITY;
CREATE POLICY tenant_iso ON work.o USING (tenant_id = current_setting('app.tenant_id', true)::int);
-- as the app role:  SET LOCAL app.tenant_id = '2';  SELECT tenant_id, count(*) FROM work.o GROUP BY 1;""")

# ---------------------------------------------------------------- LEVEL 13 : analytics SQL
ex(id="E13.1", level=13, title="Subtotals with ROLLUP", tags="GROUP BY ROLLUP · GROUPING() · subtotals",
   prompt="Fulfilled 2025 orders: GMV by `(tenant_id, currency)` with **per-tenant subtotals** and a **grand total** row. Add a column `level` = `'detail'`, `'tenant'` or `'grand'` computed with `GROUPING()`.",
   out="`tenant_id, currency, gmv_minor, level`",
   trap="A subtotal row has NULL in the rolled-up column — indistinguishable from a real NULL. `GROUPING(col)` is 1 for rolled-up NULLs. Adding two currencies into one grand total is only meaningful if you say so (tenant 4 is EUR) — a business-rule trap.",
   key="""SELECT tenant_id, currency, sum(total_minor) AS gmv_minor,
       CASE GROUPING(tenant_id, currency) WHEN 0 THEN 'detail' WHEN 1 THEN 'tenant' ELSE 'grand' END AS level
FROM lab.customer_order
WHERE status = 'fulfilled' AND placed_at >= '2025-01-01' AND placed_at < '2026-01-01'
GROUP BY ROLLUP (tenant_id, currency)""")

ex(id="E13.2", level=13, title="Pivot statuses into columns", tags="conditional aggregation · pivot",
   prompt="One row per tenant with five count columns `created, paid, fulfilled, refunded, cancelled` (orders placed in 2025).",
   out="`tenant_id, created, paid, fulfilled, refunded, cancelled`",
   trap="Standard SQL has no `PIVOT` (SQL Server/Oracle/BigQuery do). The portable idiom is `count(*) FILTER (WHERE …)` or `sum(CASE …)`. The column list is fixed at write time — dynamic pivots need dynamic SQL.",
   key="""SELECT tenant_id,
  count(*) FILTER (WHERE status='created') AS created, count(*) FILTER (WHERE status='paid') AS paid,
  count(*) FILTER (WHERE status='fulfilled') AS fulfilled, count(*) FILTER (WHERE status='refunded') AS refunded,
  count(*) FILTER (WHERE status='cancelled') AS cancelled
FROM lab.customer_order WHERE placed_at >= '2025-01-01' AND placed_at < '2026-01-01' GROUP BY tenant_id""")

ex(id="E13.3", level=13, title="Build a star schema", tags="dimensional modelling · fact/dim · surrogate keys",
   prompt="""In `work`, build `dim_product(product_id, name, category_name)` (category name or `'(none)'`), `dim_date(date_key, year, month)` for 2025 and `fact_sales(order_id, line_no, date_key, product_id, qty, revenue_minor)` from **fulfilled** order lines. Then answer with the star: *revenue by category name and month for 2025*.""",
   out="`category_name, month, revenue_minor`",
   trap="Facts hold measures + foreign keys at one **grain** (an order line); dimensions hold descriptions. Decide grain first, write it in one sentence. In BigQuery you would partition the fact by date and cluster by product (AN-02) and often *denormalise* the dimensions in.",
   stmts="""CREATE TABLE work.dim_product AS SELECT p.product_id, p.name, coalesce(c.name, '(none)') AS category_name FROM lab.product p LEFT JOIN lab.category c USING (category_id);
CREATE TABLE work.dim_date AS SELECT d::date AS date_key, extract(year FROM d)::int AS year, extract(month FROM d)::int AS month FROM generate_series('2025-01-01'::date, '2025-12-31', '1 day') d;
CREATE TABLE work.fact_sales AS SELECT l.order_id, l.line_no, o.placed_at::date AS date_key, l.product_id, l.qty, l.qty::bigint * l.unit_price_minor AS revenue_minor
  FROM lab.order_line l JOIN lab.customer_order o USING (order_id)
  WHERE o.status = 'fulfilled' AND o.placed_at >= '2025-01-01' AND o.placed_at < '2026-01-01';""",
   probe="""SELECT p.category_name, d.month, sum(f.revenue_minor) AS revenue_minor
FROM work.fact_sales f JOIN work.dim_product p USING (product_id) JOIN work.dim_date d USING (date_key) GROUP BY 1, 2""",
   key="""-- DDL as in the setup above, then:
SELECT p.category_name, d.month, sum(f.revenue_minor) AS revenue_minor
FROM work.fact_sales f JOIN work.dim_product p USING (product_id) JOIN work.dim_date d USING (date_key) GROUP BY 1, 2""")

ex(id="E13.4", level=13, title="Price history as a Type-2 dimension", tags="SCD2 · lead() · valid_to",
   prompt="From `product_price_history` build a Type-2 slowly-changing dimension: `product_id, price_minor, valid_from, valid_to, is_current` where `valid_to` is the next row's `valid_from` (NULL for the current row). Products 1–10 only.",
   out="`product_id, price_minor, valid_from, valid_to, is_current`",
   trap="`valid_to` = `lead(valid_from)` — half-open `[from, to)`. Keep `is_current` derived (`valid_to IS NULL`), never hand-set. Overlap is prevented by E10.4's exclusion constraint.",
   key="""SELECT product_id, price_minor, valid_from,
       lead(valid_from) OVER (PARTITION BY product_id ORDER BY valid_from) AS valid_to,
       lead(valid_from) OVER (PARTITION BY product_id ORDER BY valid_from) IS NULL AS is_current
FROM lab.product_price_history WHERE product_id BETWEEN 1 AND 10""")

ex(id="E13.5", level=13, title="Revenue at the price in effect", tags="as-of join · SCD2 join · range join",
   prompt="Using the SCD2 shape of E13.4, re-derive each fulfilled order line of **January 2025** at the *list price in effect at `placed_at`* and return the total difference `sum(qty × (list_price_at_order − unit_price_minor))` per tenant. (Expect a large positive number: the seed charged the *current* price, not the historical one.)",
   out="`tenant_id, price_gap_minor`",
   trap="Join on the *range* `valid_from <= placed_at AND (valid_to IS NULL OR placed_at < valid_to)` — the half-open form makes every order match exactly one row. Check that: `count(*)` of the join must equal `count(*)` of the lines.",
   key="""WITH h AS (SELECT product_id, price_minor, valid_from,
                     lead(valid_from) OVER (PARTITION BY product_id ORDER BY valid_from) AS valid_to
              FROM lab.product_price_history)
SELECT o.tenant_id, sum(l.qty::bigint * (h.price_minor - l.unit_price_minor)) AS price_gap_minor
FROM lab.order_line l JOIN lab.customer_order o USING (order_id)
JOIN h ON h.product_id = l.product_id AND h.valid_from <= o.placed_at AND (h.valid_to IS NULL OR o.placed_at < h.valid_to)
WHERE o.status = 'fulfilled' AND o.placed_at >= '2025-01-01' AND o.placed_at < '2025-02-01'
GROUP BY o.tenant_id""")
```

#### `ex_l14.py`

Exercise keys, level 14 (capstones).

```python
EX = []
def ex(**kw):
    kw.setdefault("ordered", False)
    EX.append(kw)

INJECT = """CREATE SCHEMA audit;
CREATE TABLE audit.o  AS SELECT * FROM lab.customer_order;
CREATE TABLE audit.l  AS SELECT * FROM lab.order_line;
CREATE TABLE audit.p  AS SELECT * FROM lab.payment;
CREATE TABLE audit.st AS SELECT * FROM lab.stock;
CREATE TABLE audit.sh AS SELECT * FROM lab.shipment;
UPDATE audit.o SET total_minor = total_minor + 1 WHERE order_id IN (111, 2222, 3333);
INSERT INTO audit.l VALUES (999999, 1, 1, 1, 500);
DELETE FROM audit.p WHERE kind = 'charge' AND status = 'succeeded' AND order_id IN (12, 13);
UPDATE audit.p SET amount_minor = amount_minor * 3 WHERE kind = 'refund' AND order_id IN (18, 38);
UPDATE audit.st SET reserved = on_hand + 1 WHERE product_id IN (7, 8);
UPDATE audit.o SET idempotency_key = 'idem-DUP' WHERE order_id IN
  (SELECT order_id FROM audit.o WHERE tenant_id = (SELECT tenant_id FROM audit.o WHERE order_id = 2) AND idempotency_key IS NOT NULL ORDER BY order_id LIMIT 2);
UPDATE audit.sh SET delivered_at = shipped_at - interval '1 hour' WHERE shipment_id IN (10, 20);
DELETE FROM audit.sh WHERE order_id IN (SELECT order_id FROM audit.o WHERE status = 'fulfilled' ORDER BY order_id LIMIT 2);"""

AUD = [
 ("C1.1", "Order total ≠ sum of its lines", "`order_id`",
  "SELECT o.order_id FROM {o} o JOIN (SELECT order_id, sum(qty::bigint * unit_price_minor) AS s FROM {l} GROUP BY order_id) x USING (order_id) WHERE o.total_minor <> x.s",
  "Orders **with no lines** would slip through an inner join — is that a separate invariant? (yes: add it if you consider 'empty order' illegal)."),
 ("C1.2", "Order lines with no order (orphans)", "`order_id, line_no`",
  "SELECT l.order_id, l.line_no FROM {l} l WHERE NOT EXISTS (SELECT 1 FROM {o} o WHERE o.order_id = l.order_id)",
  "The real schema has an FK, so this can't happen there — this audit is for *imported* or FK-less (warehouse) data."),
 ("C1.3", "Paid/fulfilled/refunded order with no succeeded charge", "`order_id`",
  "SELECT o.order_id FROM {o} o WHERE o.status IN ('paid','fulfilled','refunded') AND NOT EXISTS (SELECT 1 FROM {p} p WHERE p.order_id = o.order_id AND p.kind = 'charge' AND p.status = 'succeeded')",
  "A *failed* charge followed by a succeeded one is legal (every 15th order). Test the anti-join on `status = 'succeeded'`, not on 'has any charge'."),
 ("C1.4", "Refunds exceed charges", "`order_id`",
  "SELECT order_id FROM {p} GROUP BY order_id HAVING coalesce(sum(amount_minor) FILTER (WHERE kind='refund' AND status='succeeded'),0) > coalesce(sum(amount_minor) FILTER (WHERE kind='charge' AND status='succeeded'),0)",
  "Aggregate the payments table **alone** (one grain), never join it to lines first."),
 ("C1.5", "Reserved stock above on-hand", "`product_id`",
  "SELECT product_id FROM {st} WHERE reserved > on_hand",
  "The real table forbids this with a CHECK; `CREATE TABLE AS` copies data, not constraints — a classic way audit copies lose their guard rails."),
 ("C1.6", "Duplicate idempotency keys within a tenant", "`tenant_id, idempotency_key, n`",
  "SELECT tenant_id, idempotency_key, count(*) AS n FROM {o} WHERE idempotency_key IS NOT NULL GROUP BY 1, 2 HAVING count(*) > 1",
  "NULL keys are legitimately repeated (a UNIQUE index allows many NULLs). Exclude them explicitly."),
 ("C1.7", "Delivered before shipped", "`shipment_id`",
  "SELECT shipment_id FROM {sh} WHERE delivered_at < shipped_at",
  "NULL `delivered_at` compares UNKNOWN → correctly excluded."),
 ("C1.8", "Fulfilled order with no shipment", "`order_id`",
  "SELECT o.order_id FROM {o} o WHERE o.status = 'fulfilled' AND NOT EXISTS (SELECT 1 FROM {sh} s WHERE s.order_id = o.order_id)",
  "Anti-join again. Contrast with E3.5 (semi-join)."),
]
M = dict(o="audit.o", l="audit.l", p="audit.p", st="audit.st", sh="audit.sh")
for i, t, out, q, trap in AUD:
    ex(id=i, level=14, title=t, tags="audit invariant · anti-join / aggregate · data quality",
       prompt=f"On the fault-injected copies in schema `audit` (Appendix B.6): find every violation of the invariant *{t.lower()}*. Also run it against the clean `lab.*` tables — it must return **0 rows** there.",
       out=out, trap=trap, setup=INJECT, key=q.format(**M), baseline=q.format(o="lab.customer_order", l="lab.order_line", p="lab.payment", st="lab.stock", sh="lab.shipment"))

ex(id="C2", level=14, title="Cash-basis monthly revenue report", tags="capstone · payments · accrual vs cash",
   prompt="Per tenant and **payment** month (UTC, by `payment.created_at`): sum of **succeeded charges**, sum of **succeeded refunds**, and net = charges − refunds. Failed and pending payments never count. Then write two sentences reconciling this *cash* report with the *accrual* report of E4.5 (orders by placement date).",
   out="`tenant_id, month, charged_minor, refunded_minor, net_minor`",
   trap="A refund posted five days after an order can land in the next month — cash vs accrual differences are **timing**, not error. Aggregate `payment` on its own (no join to lines/orders except to get `tenant_id`). Money never leaves integer minor units.",
   key="""SELECT o.tenant_id, date_trunc('month', p.created_at)::date AS month,
       coalesce(sum(p.amount_minor) FILTER (WHERE p.kind = 'charge' AND p.status = 'succeeded'), 0) AS charged_minor,
       coalesce(sum(p.amount_minor) FILTER (WHERE p.kind = 'refund' AND p.status = 'succeeded'), 0) AS refunded_minor,
       coalesce(sum(p.amount_minor) FILTER (WHERE p.kind = 'charge' AND p.status = 'succeeded'), 0)
     - coalesce(sum(p.amount_minor) FILTER (WHERE p.kind = 'refund' AND p.status = 'succeeded'), 0) AS net_minor
FROM lab.payment p JOIN lab.customer_order o USING (order_id)
GROUP BY 1, 2""")

ex(id="C4", level=14, title="Explain and fix the slow query", tags="capstone · performance · correlated subquery → join",
   prompt="""For every identified user who ever made a `purchase` event: the number of `page_view` events in the 24 hours **before their first purchase**. The baseline query (Appendix B.7) uses three correlated subqueries per user and takes ~1.5 s on this seed. Deliverable: (1) `EXPLAIN (ANALYZE)` of the baseline with your written diagnosis, (2) a rewrite that returns the **identical fingerprint** in under 50 ms without adding an index, (3) a second fix that keeps the baseline text and adds an index — name it.""",
   out="`user_id, views_24h`",
   trap="Fingerprint first, speed second: a fast wrong answer is worthless. The rewrite computes each user's first-purchase time **once** (CTE, `min … GROUP BY user_id`) and joins; the index alternative is `(user_id, event_type, occurred_at)` or `(user_id, occurred_at)`.",
   key="""WITH fp AS (SELECT user_id, min(occurred_at) AS t FROM lab.event WHERE event_type = 'purchase' AND user_id IS NOT NULL GROUP BY user_id)
SELECT fp.user_id, count(e.event_id) AS views_24h
FROM fp LEFT JOIN lab.event e
  ON e.user_id = fp.user_id AND e.event_type = 'page_view' AND e.occurred_at < fp.t AND e.occurred_at >= fp.t - interval '24 hours'
GROUP BY fp.user_id""")
```

#### `plans.py`

The PX plan catalogue (PX-1…PX-11).

```python
import subprocess, json, os, sys
ENV = dict(os.environ, PGHOST="localhost", PGPORT="54329", PGUSER="lab", PGDATABASE="labdb")
def sql(x, tup=False):
    p=subprocess.run(["psql","-X","-At","-q","-v","ON_ERROR_STOP=1"],input=x,capture_output=True,text=True,env=ENV)
    if p.returncode: print("ERR",p.stderr[:300]); 
    return p.stdout.strip()
def plan(q, pre=""):
    out=sql(pre+"\nEXPLAIN (ANALYZE, BUFFERS OFF, TIMING OFF, SUMMARY OFF, FORMAT JSON) "+q+";")
    j=json.loads(out[out.index("["):])
    res=[]
    def walk(n,d=0):
        res.append("  "*d+f"{n['Node Type']}"+(f" on {n['Relation Name']}" if 'Relation Name' in n else "")+(f" using {n['Index Name']}" if 'Index Name' in n else "")+f"  est={n['Plan Rows']} act={n.get('Actual Rows')}" + (f" sortmethod={n['Sort Method']}" if 'Sort Method' in n else "")+ (f" heapfetches={n['Heap Fetches']}" if 'Heap Fetches' in n else ""))
        for c in n.get('Plans',[]): walk(c,d+1)
    walk(j[0]['Plan']); return "\n".join(res)
def show(t,q,pre=""):
    print("\n### "+t); print(q.strip()); print(plan(q,pre))
sql("""DROP TABLE IF EXISTS work.o; CREATE TABLE work.o AS SELECT * FROM lab.customer_order; ALTER TABLE work.o ADD PRIMARY KEY (order_id); ANALYZE work.o;
DROP TABLE IF EXISTS work.u; CREATE TABLE work.u AS SELECT * FROM lab.app_user; ALTER TABLE work.u ADD PRIMARY KEY (user_id); ANALYZE work.u;""")
show("P1 before index","SELECT * FROM work.o WHERE user_id = 42")
sql("CREATE INDEX o_user_placed ON work.o (user_id, placed_at DESC); ANALYZE work.o;")
show("P1 after index","SELECT * FROM work.o WHERE user_id = 42")
show("P1 user 1 (hot key)","SELECT * FROM work.o WHERE user_id = 1")
show("P1 user 1900 (never ordered)","SELECT * FROM work.o WHERE user_id = 1900")
show("P1 latest 5 for user 42","SELECT * FROM work.o WHERE user_id = 42 ORDER BY placed_at DESC LIMIT 5")
show("P2 sargability: function on column","SELECT count(*) FROM work.o WHERE placed_at::date = '2025-03-01'")
sql("CREATE INDEX o_placed ON work.o (placed_at); ANALYZE work.o;")
show("P2 same, index exists","SELECT count(*) FROM work.o WHERE placed_at::date = '2025-03-01'")
show("P2 rewritten as range","SELECT count(*) FROM work.o WHERE placed_at >= '2025-03-01' AND placed_at < '2025-03-02'")
show("P3 leading wildcard","SELECT * FROM work.u WHERE email LIKE '%@t1.example.com'")
sql("CREATE INDEX u_email ON work.u (email); ANALYZE work.u;")
show("P3 prefix LIKE with default btree","SELECT * FROM work.u WHERE email LIKE 'user1%'")
sql("CREATE INDEX u_email_pat ON work.u (email text_pattern_ops); ANALYZE work.u;")
show("P3 prefix LIKE with text_pattern_ops","SELECT * FROM work.u WHERE email LIKE 'user1%'")
sql("CREATE INDEX o_ts ON work.o (tenant_id, status, placed_at); ANALYZE work.o;")
show("P4 leftmost eq+eq+range","SELECT * FROM work.o WHERE tenant_id = 2 AND status = 'paid' AND placed_at >= '2025-03-01' AND placed_at < '2025-03-08'")
show("P4 skip leading column","SELECT * FROM work.o WHERE status = 'paid' AND placed_at >= '2025-03-01' AND placed_at < '2025-03-08'")
show("P4 OR of two indexed cols","SELECT * FROM work.o WHERE user_id = 42 OR order_id = 7")
sql("DROP INDEX work.o_ts; CREATE INDEX o_cov ON work.o (tenant_id, placed_at) INCLUDE (total_minor); VACUUM ANALYZE work.o;")
show("P5 covering / index-only","SELECT sum(total_minor) FROM work.o WHERE tenant_id = 2 AND placed_at >= '2025-03-01' AND placed_at < '2025-04-01'")
sql("CREATE INDEX o_created ON work.o (order_id) WHERE status = 'created'; ANALYZE work.o;")
show("P6 partial index hit","SELECT order_id FROM work.o WHERE status = 'created' AND order_id > 15000")
show("P7 join large","SELECT count(*) FROM lab.order_line l JOIN lab.product p USING (product_id)")
show("P7 join small side filtered","SELECT * FROM lab.order_line l JOIN lab.product p USING (product_id) WHERE p.product_id = 42")
sql("DROP TABLE IF EXISTS work.p; CREATE TABLE work.p AS SELECT * FROM lab.product; ANALYZE work.p;")
show("P8 correlated columns (before)","SELECT * FROM work.p WHERE tenant_id = 4 AND currency = 'EUR'")
sql("CREATE STATISTICS p_dep (dependencies) ON tenant_id, currency FROM work.p; ANALYZE work.p;")
show("P8 correlated columns (after CREATE STATISTICS)","SELECT * FROM work.p WHERE tenant_id = 4 AND currency = 'EUR'")
show("P9 OFFSET deep","SELECT * FROM work.o ORDER BY order_id OFFSET 19000 LIMIT 20")
show("P9 keyset","SELECT * FROM work.o WHERE order_id > 19000 ORDER BY order_id LIMIT 20")
show("P10 sort default work_mem","SELECT * FROM lab.event ORDER BY occurred_at")
show("P10 sort with 64kB work_mem","SELECT * FROM lab.event ORDER BY occurred_at","SET work_mem='64kB';")
show("P11 hash agg","SELECT user_id, count(*) FROM lab.event GROUP BY user_id")
show("P11 hash agg 64kB","SELECT user_id, count(*) FROM lab.event GROUP BY user_id","SET work_mem='64kB';")
sql("DROP TABLE work.o, work.u, work.p")
```

#### `tx_tests.py`

The TX scenarios, run in two sessions.

```python
from two import *
import subprocess
def sql(x):
    return subprocess.run(["psql","-X","-At","-q","-c",x],capture_output=True,text=True,env=ENV).stdout.strip()
sql("DROP SCHEMA IF EXISTS tx CASCADE; CREATE SCHEMA tx;")
def fresh(ddl):
    sql("DROP SCHEMA IF EXISTS tx CASCADE; CREATE SCHEMA tx;"); 
    for d in ddl.split(";;"): 
        if d.strip(): sql(d)

def scenario(title): print("\n=== "+title)

scenario("T1 lost update READ COMMITTED (app-side read-modify-write)")
fresh("CREATE TABLE tx.acct(id int primary key, bal int); ;; INSERT INTO tx.acct VALUES (1,100)")
a,b=S("S1"),S("S2")
step(a,"BEGIN; SELECT bal FROM tx.acct WHERE id=1;")
step(b,"BEGIN; SELECT bal FROM tx.acct WHERE id=1;")
step(a,"UPDATE tx.acct SET bal=130 WHERE id=1; COMMIT;")
step(b,"UPDATE tx.acct SET bal=80 WHERE id=1; COMMIT;")
print("final:",sql("SELECT bal FROM tx.acct WHERE id=1")); a.close(); b.close()

scenario("T1b atomic UPDATE fixes it")
fresh("CREATE TABLE tx.acct(id int primary key, bal int); ;; INSERT INTO tx.acct VALUES (1,100)")
a,b=S("S1"),S("S2")
step(a,"BEGIN; UPDATE tx.acct SET bal=bal+30 WHERE id=1;")
step(b,"BEGIN; UPDATE tx.acct SET bal=bal-20 WHERE id=1;")   # blocks
step(a,"COMMIT;")
print("S2 after S1 commit:",b.drain())
step(b,"COMMIT;")
print("final:",sql("SELECT bal FROM tx.acct WHERE id=1")); a.close(); b.close()

scenario("T1c REPEATABLE READ: second writer aborts")
fresh("CREATE TABLE tx.acct(id int primary key, bal int); ;; INSERT INTO tx.acct VALUES (1,100)")
a,b=S("S1"),S("S2")
step(a,"BEGIN ISOLATION LEVEL REPEATABLE READ; SELECT bal FROM tx.acct WHERE id=1;")
step(b,"BEGIN ISOLATION LEVEL REPEATABLE READ; SELECT bal FROM tx.acct WHERE id=1;")
step(a,"UPDATE tx.acct SET bal=130 WHERE id=1; COMMIT;")
step(b,"UPDATE tx.acct SET bal=80 WHERE id=1;")
step(b,"ROLLBACK;")
print("final:",sql("SELECT bal FROM tx.acct WHERE id=1")); a.close(); b.close()

scenario("T2 non-repeatable read: RC vs RR")
for lvl in ["READ COMMITTED","REPEATABLE READ"]:
    fresh("CREATE TABLE tx.acct(id int primary key, bal int); ;; INSERT INTO tx.acct VALUES (1,100)")
    a,b=S("S1"),S("S2"); print("--",lvl)
    step(a,f"BEGIN ISOLATION LEVEL {lvl}; SELECT bal FROM tx.acct WHERE id=1;")
    step(b,"UPDATE tx.acct SET bal=999 WHERE id=1;")
    step(a,"SELECT bal FROM tx.acct WHERE id=1; COMMIT;")
    a.close(); b.close()

scenario("T3 write skew (on-call): RR vs SERIALIZABLE")
for lvl in ["REPEATABLE READ","SERIALIZABLE"]:
    fresh("CREATE TABLE tx.oncall(doc int primary key, on_call boolean not null); ;; INSERT INTO tx.oncall VALUES (1,true),(2,true)")
    a,b=S("S1"),S("S2"); print("--",lvl)
    step(a,f"BEGIN ISOLATION LEVEL {lvl}; SELECT count(*) FROM tx.oncall WHERE on_call;")
    step(b,f"BEGIN ISOLATION LEVEL {lvl}; SELECT count(*) FROM tx.oncall WHERE on_call;")
    step(a,"UPDATE tx.oncall SET on_call=false WHERE doc=1;")
    step(b,"UPDATE tx.oncall SET on_call=false WHERE doc=2;")
    step(a,"COMMIT;")
    step(b,"COMMIT;")
    print("on call now:",sql("SELECT count(*) FROM tx.oncall WHERE on_call")); a.close(); b.close()

scenario("T3b phantom: RC vs RR (insert visible?)")
for lvl in ["READ COMMITTED","REPEATABLE READ"]:
    fresh("CREATE TABLE tx.t(id int primary key); ;; INSERT INTO tx.t VALUES (1),(2)")
    a,b=S("S1"),S("S2"); print("--",lvl)
    step(a,f"BEGIN ISOLATION LEVEL {lvl}; SELECT count(*) FROM tx.t;")
    step(b,"INSERT INTO tx.t VALUES (3);")
    step(a,"SELECT count(*) FROM tx.t; COMMIT;")
    a.close(); b.close()

scenario("T4 deadlock")
fresh("CREATE TABLE tx.acct(id int primary key, bal int); ;; INSERT INTO tx.acct VALUES (1,100),(2,100)")
a,b=S("S1"),S("S2")
step(a,"BEGIN; UPDATE tx.acct SET bal=bal-10 WHERE id=1;")
step(b,"BEGIN; UPDATE tx.acct SET bal=bal-10 WHERE id=2;")
step(a,"UPDATE tx.acct SET bal=bal+10 WHERE id=2;", wait=0.5)
step(b,"UPDATE tx.acct SET bal=bal+10 WHERE id=1;", wait=2.5)
print("S1 says:",a.drain(2.0))
a.run("ROLLBACK;",0.5); b.run("ROLLBACK;",0.5); a.close(); b.close()

scenario("T5 SKIP LOCKED queue")
fresh("CREATE TABLE tx.job(id int primary key, state text not null default 'new'); ;; INSERT INTO tx.job SELECT g FROM generate_series(1,6) g")
a,b=S("W1"),S("W2")
step(a,"BEGIN; SELECT id FROM tx.job WHERE state='new' ORDER BY id LIMIT 2 FOR UPDATE SKIP LOCKED;")
step(b,"BEGIN; SELECT id FROM tx.job WHERE state='new' ORDER BY id LIMIT 2 FOR UPDATE SKIP LOCKED;")
step(b,"BEGIN; SELECT id FROM tx.job WHERE state='new' ORDER BY id LIMIT 2 FOR UPDATE;",wait=1)
a.run("ROLLBACK;",0.5); b.run("ROLLBACK;",0.5); a.close(); b.close()

scenario("T6 SELECT FOR UPDATE fixes lost update")
fresh("CREATE TABLE tx.acct(id int primary key, bal int); ;; INSERT INTO tx.acct VALUES (1,100)")
a,b=S("S1"),S("S2")
step(a,"BEGIN; SELECT bal FROM tx.acct WHERE id=1 FOR UPDATE;")
step(b,"BEGIN; SELECT bal FROM tx.acct WHERE id=1 FOR UPDATE;")
step(a,"UPDATE tx.acct SET bal=130 WHERE id=1; COMMIT;")
print("S2 unblocked:",b.drain(1.0))
step(b,"UPDATE tx.acct SET bal=110-20 WHERE id=1; COMMIT;")
print("final:",sql("SELECT bal FROM tx.acct WHERE id=1")); a.close(); b.close()
sql("DROP SCHEMA IF EXISTS tx CASCADE")
```

#### `two.py`

The two-session psql driver used by the TX scenarios.

```python
import subprocess, os, select, time, sys
ENV = dict(os.environ, PGHOST="localhost", PGPORT="54329", PGUSER="lab", PGDATABASE="labdb")
class S:
    def __init__(self, name):
        self.name=name
        self.p=subprocess.Popen(["psql","-X","-At","-q"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,env=ENV,text=True,bufsize=0)
        self.buf=""
    def run(self, sql, wait=1.0):
        tok=f"__END{time.time_ns()}__"
        self.p.stdin.write(sql.strip()+"\n\\echo "+tok+"\n"); self.p.stdin.flush()
        out=""; t0=time.time()
        while time.time()-t0<wait:
            r,_,_=select.select([self.p.stdout],[],[],0.1)
            if r:
                ch=self.p.stdout.readline()
                if not ch: break
                if tok in ch:
                    return out.strip(), False
                out+=ch
        return out.strip(), True   # True => still blocked
    def drain(self, wait=1.0):
        out=""; t0=time.time()
        while time.time()-t0<wait:
            r,_,_=select.select([self.p.stdout],[],[],0.1)
            if r:
                ch=self.p.stdout.readline()
                if not ch: break
                out+=ch
        return out.strip()
    def close(self):
        try: self.p.stdin.write("\\q\n"); self.p.stdin.flush()
        except Exception: pass
        self.p.wait(timeout=5)
def step(s, sql, wait=1.0):
    out, blocked = s.run(sql, wait)
    print(f"[{s.name}] {sql.strip().splitlines()[0][:90]}" + ("  ... " if len(sql.strip().splitlines())>1 else ""))
    print(f"      -> {'(BLOCKED)' if blocked else out or 'ok'}" if blocked or out else "      -> ok")
    return out, blocked
```

#### `wrongs.py`

Canonical wrong queries (trap fingerprints).

```python
WRONG = {
"E1.1": ("BETWEEN with the last calendar day", """SELECT user_id, email FROM lab.app_user WHERE country IN ('GB','DE') AND created_at BETWEEN '2024-04-01' AND '2024-06-30'"""),
"E1.3": ("`<>` instead of IS DISTINCT FROM", """SELECT user_id FROM lab.app_user WHERE country <> 'US'"""),
"E2.5": ("integer division", """SELECT tenant_id, count(*) AS n_orders, count(*) FILTER (WHERE status='refunded') AS n_refunded,
 round((count(*) FILTER (WHERE status='refunded') / count(*))::numeric, 4) AS refund_rate FROM lab.customer_order GROUP BY tenant_id"""),
"E3.2": ("NOT IN over a column containing NULL", """SELECT user_id FROM lab.app_user WHERE user_id NOT IN (SELECT referred_by FROM lab.app_user)"""),
"E3.5": ("plain JOIN fans out orders with two shipments", """SELECT sum(o.total_minor) AS revenue_minor FROM lab.customer_order o JOIN lab.shipment s USING (order_id) WHERE o.status='fulfilled' AND s.delivered_at IS NOT NULL"""),
"E3.7": ("rating filter in WHERE after the LEFT JOIN", """SELECT p.product_id, count(r.review_id) AS one_star FROM lab.product p LEFT JOIN lab.review r ON r.product_id = p.product_id WHERE p.tenant_id = 1 AND r.rating = 1 GROUP BY p.product_id"""),
"E4.5": ("orders JOIN payments then SUM(total_minor)", """SELECT o.tenant_id, sum(o.total_minor) AS gmv_minor, coalesce(sum(p.amount_minor) FILTER (WHERE p.kind='refund' AND p.status='succeeded'),0) AS refunded_minor,
 sum(o.total_minor) - coalesce(sum(p.amount_minor) FILTER (WHERE p.kind='refund' AND p.status='succeeded'),0) AS net_minor
 FROM lab.customer_order o JOIN lab.payment p USING (order_id) WHERE o.status IN ('fulfilled','refunded') AND o.placed_at >= '2025-01-01' AND o.placed_at < '2026-01-01' GROUP BY o.tenant_id"""),
"E4.6": ("forgetting that ALL over an empty set is TRUE", """SELECT p.product_id FROM lab.product p WHERE p.price_minor > ALL (SELECT q.price_minor FROM lab.product q WHERE q.category_id = p.category_id AND q.product_id <> p.product_id)"""),
"E5.7": ("last_value with the default frame", """SELECT DISTINCT product_id, first_value(price_minor) OVER w AS first_price, last_value(price_minor) OVER w AS last_price, last_value(price_minor) OVER w - first_value(price_minor) OVER w AS delta
 FROM lab.product_price_history WHERE product_id BETWEEN 1 AND 20 WINDOW w AS (PARTITION BY product_id ORDER BY valid_from)"""),
"E6.4": ("plain equi-join returns all three price rows", """SELECT l.order_id, l.line_no, l.unit_price_minor, h.price_minor AS price_at_order FROM lab.order_line l JOIN lab.customer_order o USING (order_id) JOIN lab.product_price_history h ON h.product_id = l.product_id WHERE o.placed_at < '2025-01-04' AND l.unit_price_minor <> h.price_minor"""),
"E8.3": ("comparing UTC to UTC (wrong AT TIME ZONE direction)", """SELECT count(*) AS n FROM lab.customer_order WHERE (placed_at::timestamp AT TIME ZONE 'America/New_York')::date <> placed_at::date"""),
}
```

#### `naive.sql`

Check-then-act oversell (application read-modify-write).

```sql
\set sku 1
BEGIN;
SELECT on_hand AS oh FROM tx.inv WHERE sku = :sku \gset
\if :oh > 0
UPDATE tx.inv SET on_hand = :oh - 1 WHERE sku = :sku;
INSERT INTO tx.sale (sku) VALUES (:sku);
\endif
COMMIT;
```

#### `safe.sql`

Single-statement atomic claim.

```sql
\set sku 1
BEGIN;
WITH d AS (UPDATE tx.inv SET on_hand = on_hand - 1 WHERE sku = :sku AND on_hand > 0 RETURNING sku)
INSERT INTO tx.sale (sku) SELECT sku FROM d;
COMMIT;
```

#### `slow_bad.sql`

SQL-CAP4 baseline.

```sql
SELECT u.user_id,
       (SELECT count(*) FROM lab.event e
         WHERE e.user_id = u.user_id AND e.event_type = 'page_view'
           AND e.occurred_at <  (SELECT min(p.occurred_at) FROM lab.event p WHERE p.user_id = u.user_id AND p.event_type = 'purchase')
           AND e.occurred_at >= (SELECT min(p.occurred_at) FROM lab.event p WHERE p.user_id = u.user_id AND p.event_type = 'purchase') - interval '24 hours') AS views_24h
FROM lab.app_user u
WHERE EXISTS (SELECT 1 FROM lab.event p WHERE p.user_id = u.user_id AND p.event_type = 'purchase')
```

#### `slow_bad_idx.sql`

SQL-CAP4 baseline with an index-assisted path.

```sql
SELECT u.user_id,
       (SELECT count(*) FROM work.ev e
         WHERE e.user_id = u.user_id AND e.event_type = 'page_view'
           AND e.occurred_at <  (SELECT min(p.occurred_at) FROM work.ev p WHERE p.user_id = u.user_id AND p.event_type = 'purchase')
           AND e.occurred_at >= (SELECT min(p.occurred_at) FROM work.ev p WHERE p.user_id = u.user_id AND p.event_type = 'purchase') - interval '24 hours') AS views_24h
FROM lab.app_user u
WHERE EXISTS (SELECT 1 FROM work.ev p WHERE p.user_id = u.user_id AND p.event_type = 'purchase')
```

#### `slow_good.sql`

SQL-CAP4 rewrite.

```sql
WITH fp AS (SELECT user_id, min(occurred_at) AS t FROM lab.event WHERE event_type = 'purchase' AND user_id IS NOT NULL GROUP BY user_id)
SELECT fp.user_id, count(e.event_id) AS views_24h
FROM fp LEFT JOIN lab.event e
  ON e.user_id = fp.user_id AND e.event_type = 'page_view' AND e.occurred_at < fp.t AND e.occurred_at >= fp.t - interval '24 hours'
GROUP BY fp.user_id
```

#### `goldens_ex_l1_4.json`

Goldens, levels 1–4.

```json
{
 "E1.1": {
  "golden": "164:d17041f6",
  "rows": [
   "(100,user100@t5.example.com)",
   "(1002,user1002@t2.example.com)",
   "(1003,user1003@t3.example.com)",
   "(1009,user1009@t4.example.com)",
   "(1010,user1010@t5.example.com)",
   "(1016,user1016@t1.example.com)",
   "(1017,user1017@t2.example.com)",
   "(1024,user1024@t4.example.com)",
   "(1030,user1030@t5.example.com)",
   "(1031,user1031@t1.example.com)",
   "(1037,user1037@t2.example.com)",
   "(1038,user1038@t3.example.com)",
   "(1044,user1044@t4.example.com)",
   "(106,user106@t1.example.com)",
   "(107,user107@t2.example.com)",
   "(113,user113@t3.example.com)"
  ],
  "err": ""
 },
 "E1.2": {
  "golden": "181:ab2f2d8e",
  "rows": [
   "(1001)",
   "(1012)",
   "(1023)",
   "(1034)",
   "(1045)",
   "(1056)",
   "(1067)",
   "(1078)",
   "(1089)",
   "(11)",
   "(110)",
   "(1100)",
   "(1111)",
   "(1122)",
   "(1133)",
   "(1144)"
  ],
  "err": ""
 },
 "E1.3": {
  "golden": "1740:d7106dd7",
  "rows": [
   "(1)",
   "(10)",
   "(100)",
   "(1000)",
   "(1001)",
   "(1002)",
   "(1003)",
   "(1004)",
   "(1005)",
   "(1006)",
   "(1007)",
   "(1009)",
   "(101)",
   "(1010)",
   "(1011)",
   "(1012)"
  ],
  "err": ""
 },
 "E1.4": {
  "golden": "20:1af04ff2",
  "rows": [
   "(427,1999)",
   "(80,1960)",
   "(288,1956)",
   "(496,1952)",
   "(149,1913)",
   "(10,1870)",
   "(218,1866)",
   "(426,1862)",
   "(79,1823)",
   "(287,1819)",
   "(495,1815)",
   "(148,1776)",
   "(356,1772)",
   "(9,1733)",
   "(217,1729)",
   "(78,1686)"
  ],
  "err": ""
 },
 "E1.5": {
  "golden": "2036:aa6dda6b",
  "rows": [
   "(10)",
   "(100)",
   "(1000)",
   "(10005)",
   "(1001)",
   "(10020)",
   "(10035)",
   "(1005)",
   "(10050)",
   "(10065)",
   "(10080)",
   "(10095)",
   "(1010)",
   "(10110)",
   "(1012)",
   "(10125)"
  ],
  "err": ""
 },
 "E1.6": {
  "golden": "20000:a58f4910",
  "rows": [
   "(1,done)",
   "(10,done)",
   "(100,done)",
   "(1000,done)",
   "(10000,done)",
   "(10001,done)",
   "(10002,done)",
   "(10003,done)",
   "(10004,done)",
   "(10005,done)",
   "(10006,done)",
   "(10007,done)",
   "(10008,done)",
   "(10009,done)",
   "(1001,done)",
   "(10010,done)"
  ],
  "err": ""
 },
 "E1.7": {
  "golden": "10:558e94b1",
  "rows": [
   "(208,9996)",
   "(416,9992)",
   "(69,9953)",
   "(277,9949)",
   "(485,9945)",
   "(138,9906)",
   "(346,9902)",
   "(207,9859)",
   "(415,9855)",
   "(276,9812)"
  ],
  "err": ""
 },
 "E1.8": {
  "golden": "10:986cf4ec",
  "rows": [
   "(107)",
   "(117)",
   "(127)",
   "(137)",
   "(147)",
   "(157)",
   "(167)",
   "(177)",
   "(187)",
   "(197)"
  ],
  "err": ""
 },
 "E2.1": {
  "golden": "5:2495a69d",
  "rows": [
   "(cancelled,2000,51826032)",
   "(created,1000,20492746)",
   "(fulfilled,12000,310301174)",
   "(paid,3000,62350316)",
   "(refunded,2000,72607634)"
  ],
  "err": ""
 },
 "E2.2": {
  "golden": "12:c6eb674e",
  "rows": [
   "(\"2025-01-01 00:00:00+00\",1028,26459279)",
   "(\"2025-02-01 00:00:00+00\",920,23598472)",
   "(\"2025-03-01 00:00:00+00\",1017,26613155)",
   "(\"2025-04-01 00:00:00+00\",990,25855902)",
   "(\"2025-05-01 00:00:00+00\",1032,26554302)",
   "(\"2025-06-01 00:00:00+00\",987,25454489)",
   "(\"2025-07-01 00:00:00+00\",1012,26107516)",
   "(\"2025-08-01 00:00:00+00\",1024,26566981)",
   "(\"2025-09-01 00:00:00+00\",984,25153787)",
   "(\"2025-10-01 00:00:00+00\",1010,25879543)",
   "(\"2025-11-01 00:00:00+00\",984,25667929)",
   "(\"2025-12-01 00:00:00+00\",1012,26389819)"
  ],
  "err": ""
 },
 "E2.3": {
  "golden": "467:68a601d1",
  "rows": [
   "(1,53,3.60)",
   "(10,23,3.61)",
   "(100,13,3.54)",
   "(101,15,3.73)",
   "(102,15,3.40)",
   "(103,13,3.38)",
   "(104,15,3.67)",
   "(105,15,3.87)",
   "(106,13,3.54)",
   "(107,13,3.69)",
   "(108,15,3.20)",
   "(109,15,3.60)",
   "(11,25,3.36)",
   "(110,13,3.62)",
   "(111,14,3.64)",
   "(112,15,3.20)"
  ],
  "err": ""
 },
 "E2.4": {
  "golden": "5:0cf3aaa2",
  "rows": [
   "(1,4055,360)",
   "(2,4027,360)",
   "(3,3984,360)",
   "(4,3980,360)",
   "(5,3954,360)"
  ],
  "err": ""
 },
 "E2.5": {
  "golden": "5:9fbfe463",
  "rows": [
   "(1,4055,424,0.1046)",
   "(2,4027,432,0.1073)",
   "(3,3984,415,0.1042)",
   "(4,3980,356,0.0894)",
   "(5,3954,373,0.0943)"
  ],
  "err": ""
 },
 "E2.6": {
  "golden": "8:94127f65",
  "rows": [
   "(??,181)",
   "(BR,260)",
   "(DE,260)",
   "(FR,259)",
   "(GB,260)",
   "(IN,260)",
   "(JP,260)",
   "(US,260)"
  ],
  "err": ""
 },
 "E2.7": {
  "golden": "5:74a001bd",
  "rows": [
   "(1,27381)",
   "(2,25335)",
   "(3,25320)",
   "(4,25227)",
   "(5,25135)"
  ],
  "err": ""
 },
 "E2.8": {
  "golden": "10:dc13b2c1",
  "rows": [
   "(0,28)",
   "(1000,55)",
   "(2000,50)",
   "(3000,51)",
   "(4000,45)",
   "(5000,51)",
   "(6000,47)",
   "(7000,48)",
   "(8000,50)",
   "(9000,46)"
  ],
  "err": ""
 },
 "E3.1": {
  "golden": "50:787a0b9d",
  "rows": [
   "(10232,user22@t2.example.com,tenant-2,4469)",
   "(10834,user532@t2.example.com,tenant-2,21189)",
   "(10853,user597@t2.example.com,tenant-2,23952)",
   "(10893,user87@t2.example.com,tenant-2,23735)",
   "(10932,user1787@t2.example.com,tenant-2,14778)",
   "(10952,user1342@t2.example.com,tenant-2,4469)",
   "(11514,user752@t2.example.com,tenant-2,44229)",
   "(11554,user177@t2.example.com,tenant-2,21189)",
   "(11593,user37@t2.example.com,tenant-2,16831)",
   "(11613,user1542@t2.example.com,tenant-2,23735)",
   "(11692,user487@t2.example.com,tenant-2,12867)",
   "(13093,user52@t2.example.com,tenant-2,29251)",
   "(1373,user672@t2.example.com,tenant-2,19572)",
   "(14454,user72@t2.example.com,tenant-2,20109)",
   "(1452,user12@t2.example.com,tenant-2,11858)",
   "(14572,user627@t2.example.com,tenant-2,4647)"
  ],
  "err": ""
 },
 "E3.2": {
  "golden": "1291:ce8f0411",
  "rows": [
   "(1000)",
   "(1001)",
   "(1003)",
   "(1005)",
   "(1007)",
   "(1008)",
   "(1009)",
   "(101)",
   "(1011)",
   "(1012)",
   "(1013)",
   "(1015)",
   "(1017)",
   "(1019)",
   "(1020)",
   "(1021)"
  ],
  "err": ""
 },
 "E3.3": {
  "golden": "200:e5ab3ae1",
  "rows": [
   "(1801)",
   "(1802)",
   "(1803)",
   "(1804)",
   "(1805)",
   "(1806)",
   "(1807)",
   "(1808)",
   "(1809)",
   "(1810)",
   "(1811)",
   "(1812)",
   "(1813)",
   "(1814)",
   "(1815)",
   "(1816)"
  ],
  "err": ""
 },
 "E3.4": {
  "golden": "180:d18c224e",
  "rows": [
   "(10)",
   "(104)",
   "(107)",
   "(109)",
   "(11)",
   "(110)",
   "(113)",
   "(114)",
   "(119)",
   "(12)",
   "(122)",
   "(124)",
   "(128)",
   "(129)",
   "(13)",
   "(131)"
  ],
  "err": ""
 },
 "E3.5": {
  "golden": "1:6c39466d",
  "rows": [
   "(265817834)"
  ],
  "err": ""
 },
 "E3.6": {
  "golden": "1172:9f8ebbd0",
  "rows": [
   "(1001,834)",
   "(1003,664)",
   "(1005,494)",
   "(1007,666)",
   "(101,10)",
   "(1010,72)",
   "(1011,8)",
   "(1013,642)",
   "(1014,898)",
   "(1017,746)",
   "(1018,102)",
   "(1019,918)",
   "(102,79)",
   "(1025,434)",
   "(1026,923)",
   "(1027,136)"
  ],
  "err": ""
 },
 "E3.7": {
  "golden": "100:1b05fa94",
  "rows": [
   "(1,6)",
   "(101,1)",
   "(106,2)",
   "(11,4)",
   "(111,2)",
   "(116,1)",
   "(121,1)",
   "(126,1)",
   "(131,1)",
   "(136,1)",
   "(141,2)",
   "(146,2)",
   "(151,2)",
   "(156,2)",
   "(16,3)",
   "(161,1)"
  ],
  "err": ""
 },
 "E3.8": {
  "golden": "1845:6f7a9372",
  "rows": [
   "(1,t,t)",
   "(10,t,f)",
   "(100,t,f)",
   "(1000,t,t)",
   "(1001,t,t)",
   "(1002,t,f)",
   "(1003,t,t)",
   "(1004,t,t)",
   "(1005,t,f)",
   "(1006,t,f)",
   "(1007,t,f)",
   "(1008,t,f)",
   "(1009,t,f)",
   "(101,t,f)",
   "(1010,t,f)",
   "(1011,t,f)"
  ],
  "err": ""
 },
 "E3.9": {
  "golden": "14:cb9ff4e8",
  "rows": [
   "(2024-05-01,0)",
   "(2024-06-01,1)",
   "(2024-07-01,4)",
   "(2024-08-01,2)",
   "(2024-09-01,1)",
   "(2024-10-01,3)",
   "(2024-11-01,3)",
   "(2024-12-01,0)",
   "(2025-01-01,3)",
   "(2025-02-01,3)",
   "(2025-03-01,0)",
   "(2025-04-01,0)",
   "(2025-05-01,0)",
   "(2025-06-01,0)"
  ],
  "err": ""
 },
 "E3.10": {
  "golden": "241:47e3b13f",
  "rows": [
   "(1,50,53)",
   "(101,14,15)",
   "(102,13,15)",
   "(104,14,15)",
   "(105,13,15)",
   "(108,13,15)",
   "(109,14,15)",
   "(11,22,25)",
   "(111,13,14)",
   "(112,13,15)",
   "(115,13,15)",
   "(116,13,14)",
   "(118,13,14)",
   "(119,13,15)",
   "(122,13,15)",
   "(123,13,14)"
  ],
  "err": ""
 },
 "E4.1": {
  "golden": "675:19348832",
  "rows": [
   "(1,2065770)",
   "(10,791320)",
   "(100,274665)",
   "(1005,180555)",
   "(1006,187235)",
   "(1007,245306)",
   "(101,520862)",
   "(1011,202002)",
   "(1012,290450)",
   "(1013,377421)",
   "(1019,306345)",
   "(102,355741)",
   "(1020,182285)",
   "(1021,226263)",
   "(103,196046)",
   "(1036,282023)"
  ],
  "err": ""
 },
 "E4.2": {
  "golden": "500:7463fec9",
  "rows": [
   "(1,4)",
   "(10,5)",
   "(100,5)",
   "(101,4)",
   "(102,3)",
   "(103,4)",
   "(104,4)",
   "(105,2)",
   "(106,5)",
   "(107,4)",
   "(108,5)",
   "(109,5)",
   "(11,2)",
   "(110,4)",
   "(111,3)",
   "(112,1)"
  ],
  "err": ""
 },
 "E4.3": {
  "golden": "391:6319def9",
  "rows": [
   "(10)",
   "(101)",
   "(102)",
   "(1020)",
   "(1021)",
   "(1022)",
   "(1023)",
   "(1024)",
   "(1029)",
   "(103)",
   "(1030)",
   "(1031)",
   "(104)",
   "(105)",
   "(106)",
   "(1064)"
  ],
  "err": ""
 },
 "E4.4": {
  "golden": "4559:2e92d1fa",
  "rows": [
   "(1,471)",
   "(10,220)",
   "(100,110)",
   "(100,275)",
   "(100,90)",
   "(1000,300)",
   "(1000,495)",
   "(1000,70)",
   "(1001,191)",
   "(1001,291)",
   "(1001,371)",
   "(1001,46)",
   "(1001,486)",
   "(1003,428)",
   "(1003,83)",
   "(1004,64)"
  ],
  "err": ""
 },
 "E4.5": {
  "golden": "5:77344493",
  "rows": [
   "(1,81502724,11059891,70442833)",
   "(2,77343757,11237996,66105761)",
   "(3,74675494,11017902,63657592)",
   "(4,74482248,9245438,65236810)",
   "(5,74904585,9450817,65453768)"
  ],
  "err": ""
 },
 "E4.6": {
  "golden": "30:d5ca9e54",
  "rows": [
   "(137)",
   "(138)",
   "(206)",
   "(207)",
   "(271)",
   "(276)",
   "(277)",
   "(340)",
   "(341)",
   "(342)",
   "(343)",
   "(344)",
   "(345)",
   "(346)",
   "(409)",
   "(410)"
  ],
  "err": ""
 },
 "E4.7": {
  "golden": "360:3dd4aace",
  "rows": [
   "(1003,8935,\"2025-09-28 22:31:05+00\")",
   "(1008,5029,\"2025-10-16 22:24:11+00\")",
   "(1013,15290,\"2025-12-12 09:45:10+00\")",
   "(1018,11384,\"2025-12-30 09:38:16+00\")",
   "(1023,18525,\"2025-11-17 21:51:15+00\")",
   "(1028,5652,\"2025-12-11 00:49:48+00\")",
   "(103,838,\"2025-12-13 19:22:02+00\")",
   "(1033,1746,\"2025-12-29 00:42:54+00\")",
   "(1038,8887,\"2025-11-16 12:55:53+00\")",
   "(1043,4981,\"2025-12-04 12:48:59+00\")",
   "(1048,1075,\"2025-12-22 12:42:05+00\")",
   "(1053,8216,\"2025-11-09 00:55:04+00\")",
   "(1058,4310,\"2025-11-27 00:48:10+00\")",
   "(1063,404,\"2025-12-15 00:41:16+00\")",
   "(1068,7545,\"2025-11-02 12:54:15+00\")",
   "(1073,17806,\"2025-12-29 00:15:14+00\")"
  ],
  "err": ""
 },
 "E4.8": {
  "golden": "5:286c82f6",
  "rows": [
   "(1)",
   "(171)",
   "(201)",
   "(26)",
   "(86)"
  ],
  "err": ""
 }
}
```

#### `goldens_ex_l5_8.json`

Goldens, levels 5–8.

```json
{
 "E5.1": {
  "golden": "90:0444fd32",
  "rows": [
   "(105,276,9812,1)",
   "(105,336,8532,3)",
   "(105,66,9542,2)",
   "(106,271,9127,1)",
   "(106,331,7847,3)",
   "(106,61,8857,2)",
   "(107,206,9722,1)",
   "(107,266,8442,3)",
   "(107,476,8712,2)",
   "(108,201,9037,2)",
   "(108,411,9307,1)",
   "(108,471,8027,3)",
   "(109,136,9632,2)",
   "(109,346,9902,1)",
   "(109,406,8622,3)",
   "(110,131,8947,2)"
  ],
  "err": ""
 },
 "E5.2": {
  "golden": "31:1c8f130e",
  "rows": [
   "(2025-03-01,120655,120655)",
   "(2025-03-02,138235,258890)",
   "(2025-03-03,137430,396320)",
   "(2025-03-04,248339,644659)",
   "(2025-03-05,45156,689815)",
   "(2025-03-06,242754,932569)",
   "(2025-03-07,295819,1228388)",
   "(2025-03-08,57485,1285873)",
   "(2025-03-09,400065,1685938)",
   "(2025-03-10,73998,1759936)",
   "(2025-03-11,161512,1921448)",
   "(2025-03-12,129392,2050840)",
   "(2025-03-13,162049,2212889)",
   "(2025-03-14,370136,2583025)",
   "(2025-03-15,159917,2742942)",
   "(2025-03-16,244118,2987060)"
  ],
  "err": ""
 },
 "E5.3": {
  "golden": "996:d7137b70",
  "rows": [
   "(1,10007,\"2025-05-30 04:37:13+00\",1)",
   "(1,10122,\"2025-01-25 17:35:18+00\",4)",
   "(1,10261,\"2025-02-27 11:20:59+00\",4)",
   "(1,10376,\"2025-10-25 00:19:04+00\",4)",
   "(1,10515,\"2025-11-27 18:04:45+00\",4)",
   "(1,10654,\"2025-12-30 11:50:26+00\",4)",
   "(1,10769,\"2025-08-27 00:48:31+00\",4)",
   "(1,10908,\"2025-09-29 18:34:12+00\",4)",
   "(1,11162,\"2025-06-29 01:17:58+00\",4)",
   "(1,11301,\"2025-08-01 19:03:39+00\",4)",
   "(1,11416,\"2025-03-29 08:01:44+00\",4)",
   "(1,115,\"2025-08-29 12:58:05+00\",2)",
   "(1,1155,\"2025-01-31 20:40:45+00\",2)",
   "(1,11555,\"2025-05-01 01:47:25+00\",4)",
   "(1,11694,\"2025-06-03 19:33:06+00\",4)",
   "(1,11809,\"2025-01-29 08:31:11+00\",4)"
  ],
  "err": ""
 },
 "E5.4": {
  "golden": "100:8a1679d3",
  "rows": [
   "(1,1155,54001,2)",
   "(1,7927,61593,1)",
   "(10,10951,56625,1)",
   "(10,13031,50170,2)",
   "(11,1591,51693,1)",
   "(11,551,49394,2)",
   "(12,12499,51506,1)",
   "(12,17306,51474,2)",
   "(13,1059,52533,1)",
   "(13,19,45459,2)",
   "(14,17167,55992,2)",
   "(14,7807,55992,1)",
   "(15,1567,51165,1)",
   "(15,8454,48115,2)",
   "(16,18715,55533,2)",
   "(16,9355,55533,1)"
  ],
  "err": ""
 },
 "E5.5": {
  "golden": "5:4bec02c5",
  "rows": [
   "(1,65737398,21.19)",
   "(2,61608441,19.85)",
   "(3,59768245,19.26)",
   "(4,61784155,19.91)",
   "(5,61402935,19.79)"
  ],
  "err": ""
 },
 "E5.6": {
  "golden": "94:71892706",
  "rows": [
   "(107,5659,3)",
   "(112,6344,3)",
   "(117,7029,3)",
   "(12,2144,1)",
   "(122,7714,4)",
   "(127,8399,4)",
   "(132,9084,4)",
   "(137,9769,4)",
   "(142,954,1)",
   "(147,1639,1)",
   "(152,2324,1)",
   "(157,3009,2)",
   "(162,3694,2)",
   "(167,4379,2)",
   "(172,5064,2)",
   "(177,5749,3)"
  ],
  "err": ""
 },
 "E5.7": {
  "golden": "20:7ddcb09e",
  "rows": [
   "(1,837,637,-200)",
   "(10,2070,1870,-200)",
   "(11,2207,2007,-200)",
   "(12,2344,2144,-200)",
   "(13,2481,2281,-200)",
   "(14,2618,2418,-200)",
   "(15,2755,2555,-200)",
   "(16,2892,2692,-200)",
   "(17,3029,2829,-200)",
   "(18,3166,2966,-200)",
   "(19,3303,3103,-200)",
   "(2,974,774,-200)",
   "(20,3440,3240,-200)",
   "(3,1111,911,-200)",
   "(4,1248,1048,-200)",
   "(5,1385,1185,-200)"
  ],
  "err": ""
 },
 "E5.8": {
  "golden": "22:55be0551",
  "rows": [
   "(2025-02-07,7,10.86)",
   "(2025-02-08,10,10.86)",
   "(2025-02-09,15,11.71)",
   "(2025-02-10,8,11.43)",
   "(2025-02-11,6,10.86)",
   "(2025-02-12,16,11.29)",
   "(2025-02-13,9,10.14)",
   "(2025-02-14,9,10.43)",
   "(2025-02-15,11,10.57)",
   "(2025-02-16,11,10.00)",
   "(2025-02-17,12,10.57)",
   "(2025-02-18,15,11.86)",
   "(2025-02-19,10,11.00)",
   "(2025-02-20,13,11.57)",
   "(2025-02-21,8,11.43)",
   "(2025-02-22,8,11.00)"
  ],
  "err": ""
 },
 "E6.1": {
  "golden": "200:3d4d4f51",
  "rows": [
   "(1,6,2025-03-09)",
   "(10,6,2025-03-18)",
   "(100,6,2025-03-18)",
   "(101,6,2025-03-17)",
   "(102,6,2025-03-16)",
   "(103,6,2025-03-06)",
   "(104,6,2025-03-05)",
   "(105,6,2025-03-04)",
   "(106,6,2025-03-03)",
   "(107,6,2025-03-02)",
   "(108,6,2025-03-01)",
   "(109,6,2025-03-09)",
   "(11,6,2025-03-17)",
   "(110,6,2025-03-08)",
   "(111,6,2025-03-07)",
   "(112,6,2025-03-06)"
  ],
  "err": ""
 },
 "E6.2": {
  "golden": "7500:311fb683",
  "rows": [
   "(1,1,8,\"2025-06-25 10:00:00+00\",\"2025-06-25 10:14:00+00\")",
   "(1,2,8,\"2025-09-28 05:00:00+00\",\"2025-09-28 05:14:00+00\")",
   "(10,1,8,\"2025-02-07 03:53:29+00\",\"2025-02-07 04:07:29+00\")",
   "(10,2,4,\"2025-05-13 18:20:09+00\",\"2025-05-13 18:26:09+00\")",
   "(10,3,4,\"2025-05-13 19:08:09+00\",\"2025-05-13 19:14:09+00\")",
   "(10,4,8,\"2025-08-16 13:20:09+00\",\"2025-08-16 13:34:09+00\")",
   "(10,5,8,\"2025-11-04 08:53:29+00\",\"2025-11-04 09:07:29+00\")",
   "(100,1,8,\"2025-02-22 05:01:39+00\",\"2025-02-22 05:15:39+00\")",
   "(100,2,8,\"2025-05-28 00:01:39+00\",\"2025-05-28 00:15:39+00\")",
   "(100,3,8,\"2025-08-16 15:01:39+00\",\"2025-08-16 15:15:39+00\")",
   "(100,4,4,\"2025-11-19 10:01:39+00\",\"2025-11-19 10:07:39+00\")",
   "(100,5,4,\"2025-11-19 10:49:39+00\",\"2025-11-19 10:55:39+00\")",
   "(1000,1,8,\"2025-02-17 04:09:59+00\",\"2025-02-17 04:23:59+00\")",
   "(1000,2,8,\"2025-05-23 18:36:39+00\",\"2025-05-23 18:50:39+00\")",
   "(1000,3,4,\"2025-08-26 13:36:39+00\",\"2025-08-26 13:42:39+00\")",
   "(1000,4,4,\"2025-08-26 14:24:39+00\",\"2025-08-26 14:30:39+00\")"
  ],
  "err": ""
 },
 "E6.3": {
  "golden": "1:2f3673b3",
  "rows": [
   "(1000,500,250)"
  ],
  "err": ""
 },
 "E6.4": {
  "golden": "404:4f5a2a10",
  "rows": [
   "(10003,1,1001,1101)",
   "(10003,2,3056,3156)",
   "(10003,3,5111,5211)",
   "(10003,4,7166,7266)",
   "(10151,1,4884,4984)",
   "(10151,2,6939,7039)",
   "(10151,3,8994,9094)",
   "(10151,4,1549,1649)",
   "(10220,1,3506,3606)",
   "(1026,1,8399,8499)",
   "(1026,2,954,1054)",
   "(1026,3,3009,3109)",
   "(10368,1,7252,7352)",
   "(10516,1,4649,4749)",
   "(10585,1,7894,7994)",
   "(10585,2,9949,10049)"
  ],
  "err": ""
 },
 "E6.5": {
  "golden": "996:7e7490f1",
  "rows": [
   "(1,10007,11)",
   "(1,10122,10)",
   "(1,10261,10)",
   "(1,10376,12)",
   "(1,10515,10)",
   "(1,10654,10)",
   "(1,10769,13)",
   "(1,10908,10)",
   "(1,11162,11)",
   "(1,11301,9)",
   "(1,11416,12)",
   "(1,115,13)",
   "(1,1155,12)",
   "(1,11555,9)",
   "(1,11694,10)",
   "(1,11809,11)"
  ],
  "err": ""
 },
 "E6.6": {
  "golden": "10:79a8b3a1",
  "rows": [
   "(2024-02-01,202,0)",
   "(2024-03-01,217,0)",
   "(2024-04-01,210,0)",
   "(2024-05-01,217,0)",
   "(2024-06-01,210,0)",
   "(2024-07-01,217,0)",
   "(2024-08-01,205,0)",
   "(2024-09-01,180,0)",
   "(2024-10-01,186,0)",
   "(2024-11-01,156,0)"
  ],
  "err": ""
 },
 "E6.7": {
  "golden": "6000:a46392ec",
  "rows": [
   "(1000010)",
   "(1000020)",
   "(1000030)",
   "(1000040)",
   "(1000050)",
   "(1000060)",
   "(1000070)",
   "(1000080)",
   "(1000090)",
   "(1000100)",
   "(1000110)",
   "(1000120)",
   "(1000130)",
   "(1000140)",
   "(1000150)",
   "(1000160)"
  ],
  "err": ""
 },
 "E7.1": {
  "golden": "10:82a25fd0",
  "rows": [
   "(101,0,cat-1-1)",
   "(102,1,\"cat-1-1 > cat-1-2\")",
   "(103,1,\"cat-1-1 > cat-1-3\")",
   "(104,1,\"cat-1-1 > cat-1-4\")",
   "(105,2,\"cat-1-1 > cat-1-2 > cat-1-5\")",
   "(106,2,\"cat-1-1 > cat-1-2 > cat-1-6\")",
   "(107,2,\"cat-1-1 > cat-1-3 > cat-1-7\")",
   "(108,2,\"cat-1-1 > cat-1-3 > cat-1-8\")",
   "(109,2,\"cat-1-1 > cat-1-4 > cat-1-9\")",
   "(110,2,\"cat-1-1 > cat-1-4 > cat-1-10\")"
  ],
  "err": ""
 },
 "E7.2": {
  "golden": "10:13320b85",
  "rows": [
   "(101,92)",
   "(102,31)",
   "(103,29)",
   "(104,32)",
   "(105,16)",
   "(106,15)",
   "(107,14)",
   "(108,15)",
   "(109,16)",
   "(110,16)"
  ],
  "err": ""
 },
 "E7.3": {
  "golden": "2000:97e6e0a2",
  "rows": [
   "(1,1,0)",
   "(10,10,0)",
   "(100,100,0)",
   "(1000,1000,0)",
   "(1001,38,3)",
   "(1002,240,3)",
   "(1003,664,1)",
   "(1004,1004,0)",
   "(1005,156,2)",
   "(1006,12,3)",
   "(1007,3,5)",
   "(1008,1008,0)",
   "(1009,240,3)",
   "(101,10,1)",
   "(1010,72,1)",
   "(1011,8,1)"
  ],
  "err": ""
 },
 "E7.4": {
  "golden": "1:36a7110f",
  "rows": [
   "(52,80)"
  ],
  "err": ""
 },
 "E7.5": {
  "golden": "3:62171a21",
  "rows": [
   "(1)",
   "(2)",
   "(3)"
  ],
  "err": ""
 },
 "E8.1": {
  "golden": "3:72b2a44b",
  "rows": [
   "(DHL,3424,3.75)",
   "(FedEx,4573,4.75)",
   "(UPS,3431,2.75)"
  ],
  "err": ""
 },
 "E8.2": {
  "golden": "1825:dc65c0f1",
  "rows": [
   "(100)",
   "(10000)",
   "(10008)",
   "(10015)",
   "(10022)",
   "(10029)",
   "(10037)",
   "(10043)",
   "(1005)",
   "(10051)",
   "(10058)",
   "(10072)",
   "(10079)",
   "(10080)",
   "(10087)",
   "(10094)"
  ],
  "err": ""
 },
 "E8.3": {
  "golden": "1:f10d5c9a",
  "rows": [
   "(3628)"
  ],
  "err": ""
 },
 "E8.4": {
  "golden": "53:15bc9aa0",
  "rows": [
   "(2024-12-30,273)",
   "(2025-01-06,384)",
   "(2025-01-13,383)",
   "(2025-01-20,384)",
   "(2025-01-27,383)",
   "(2025-02-03,384)",
   "(2025-02-10,384)",
   "(2025-02-17,384)",
   "(2025-02-24,383)",
   "(2025-03-03,384)",
   "(2025-03-10,384)",
   "(2025-03-17,383)",
   "(2025-03-24,384)",
   "(2025-03-31,384)",
   "(2025-04-07,383)",
   "(2025-04-14,384)"
  ],
  "err": ""
 },
 "E8.5": {
  "golden": "41:a5be7c78",
  "rows": [
   "(108)",
   "(12)",
   "(120)",
   "(132)",
   "(144)",
   "(156)",
   "(168)",
   "(180)",
   "(192)",
   "(204)",
   "(216)",
   "(228)",
   "(24)",
   "(240)",
   "(252)",
   "(264)"
  ],
  "err": ""
 },
 "E8.6": {
  "golden": "4:eaf94d2b",
  "rows": [
   "(desk,1875,1500.0)",
   "(lamp,1875,1498.0)",
   "(mug,1875,1502.0)",
   "(shoe,1875,1496.0)"
  ],
  "err": ""
 },
 "E8.7": {
  "golden": "2:71943e30",
  "rows": [
   "(eco,166)",
   "(gift,166)"
  ],
  "err": ""
 },
 "E8.8": {
  "golden": "8:4fc20676",
  "rows": [
   "(1,ann@example.com)",
   "(10,erin@example.com)",
   "(12,gina@example.com)",
   "(14,hal@example.com)",
   "(15,ivy@example.com)",
   "(3,bob@example.com)",
   "(6,carol@example.com)",
   "(8,dave@example.com)"
  ],
  "err": ""
 },
 "E8.9": {
  "golden": "15:bafc9e47",
  "rows": [
   "(1,1250)",
   "(10,)",
   "(11,1500)",
   "(12,999)",
   "(13,999)",
   "(14,10000)",
   "(15,100050)",
   "(2,120000)",
   "(3,)",
   "(4,700)",
   "(5,0)",
   "(6,)",
   "(7,400)",
   "(8,)",
   "(9,-500)"
  ],
  "err": ""
 },
 "E8.10": {
  "golden": "15:3eed39e7",
  "rows": [
   "(1,2025-03-01)",
   "(10,2025-03-04)",
   "(11,2025-03-05)",
   "(12,)",
   "(13,2025-03-06)",
   "(14,2025-03-06)",
   "(15,2025-03-07)",
   "(2,2025-03-01)",
   "(3,2025-03-01)",
   "(4,2025-03-02)",
   "(5,2025-03-02)",
   "(6,)",
   "(7,2025-03-03)",
   "(8,)",
   "(9,)"
  ],
  "err": ""
 }
}
```

#### `goldens_ex_l9_13.json`

Goldens, levels 9–13.

```json
{
 "E9.1": {
  "golden": "155:9a2d7927",
  "rows": [
   "(1,2025-01-01,204703)",
   "(1,2025-01-02,190895)",
   "(1,2025-01-03,256619)",
   "(1,2025-01-04,34531)",
   "(1,2025-01-05,173909)",
   "(1,2025-01-06,225307)",
   "(1,2025-01-07,258627)",
   "(1,2025-01-08,262359)",
   "(1,2025-01-09,108464)",
   "(1,2025-01-10,280176)",
   "(1,2025-01-11,251993)",
   "(1,2025-01-12,108194)",
   "(1,2025-01-13,373082)",
   "(1,2025-01-14,189363)",
   "(1,2025-01-15,264988)",
   "(1,2025-01-16,92290)"
  ],
  "err": ""
 },
 "E9.2": {
  "golden": "20000:12518931",
  "rows": [
   "(1,29059)",
   "(10,33989)",
   "(100,14229)",
   "(1000,13947)",
   "(10000,21498)",
   "(10001,8463)",
   "(10002,45309)",
   "(10003,37779)",
   "(10004,4649)",
   "(10005,22850)",
   "(10006,35469)",
   "(10007,39534)",
   "(10008,6292)",
   "(10009,28683)",
   "(1001,23412)",
   "(10010,27354)"
  ],
  "err": ""
 },
 "E9.3": {
  "golden": "365:60b9c8d0",
  "rows": [
   "(2025-01-01,54)",
   "(2025-01-02,55)",
   "(2025-01-03,54)",
   "(2025-01-04,55)",
   "(2025-01-05,55)",
   "(2025-01-06,55)",
   "(2025-01-07,55)",
   "(2025-01-08,54)",
   "(2025-01-09,55)",
   "(2025-01-10,55)",
   "(2025-01-11,55)",
   "(2025-01-12,55)",
   "(2025-01-13,54)",
   "(2025-01-14,55)",
   "(2025-01-15,55)",
   "(2025-01-16,55)"
  ],
  "err": ""
 },
 "E9.4": {
  "golden": "6000:bc58a9d4",
  "rows": [
   "(1)",
   "(10)",
   "(100)",
   "(1000)",
   "(10005)",
   "(1001)",
   "(1002)",
   "(10020)",
   "(1003)",
   "(10035)",
   "(1004)",
   "(10050)",
   "(1006)",
   "(10065)",
   "(1007)",
   "(1008)"
  ],
  "err": ""
 },
 "E9.5": {
  "golden": "11:61ddd589",
  "rows": [
   "(1,500)",
   "(3,7)",
   "(4,124)",
   "(5,155)",
   "(6,186)",
   "(7,17)",
   "(8,48)",
   "(9,79)",
   "(10,110)",
   "(11,33)",
   "(12,44)"
  ],
  "err": ""
 },
 "E9.6": {
  "golden": "20000:f913007e",
  "rows": [
   "(1,290.59)",
   "(10,339.89)",
   "(100,142.29)",
   "(1000,139.47)",
   "(10000,214.98)",
   "(10001,84.63)",
   "(10002,453.09)",
   "(10003,377.79)",
   "(10004,46.49)",
   "(10005,228.50)",
   "(10006,354.69)",
   "(10007,395.34)",
   "(10008,62.92)",
   "(10009,286.83)",
   "(1001,234.12)",
   "(10010,273.54)"
  ],
  "err": ""
 },
 "E9.7": {
  "golden": "1:06897331",
  "rows": [
   "(18000,2000)"
  ],
  "err": ""
 },
 "E10.1": {
  "golden": "8:e5c729de",
  "rows": [
   "(1,t)",
   "(2,t)",
   "(3,f)",
   "(4,f)",
   "(5,f)",
   "(6,f)",
   "(7,f)",
   "(8,t)"
  ],
  "err": ""
 },
 "E10.2": {
  "golden": "4:8c4ee581",
  "rows": [
   "(1,t)",
   "(2,f)",
   "(3,f)",
   "(4,f)"
  ],
  "err": ""
 },
 "E10.3": {
  "golden": "5:7a0a9605",
  "rows": [
   "(1,t)",
   "(2,t)",
   "(3,t)",
   "(4,f)",
   "(5,t)"
  ],
  "err": ""
 },
 "E10.4": {
  "golden": "5:a6c6c4a9",
  "rows": [
   "(1,t)",
   "(2,t)",
   "(3,f)",
   "(4,t)",
   "(5,f)"
  ],
  "err": ""
 },
 "E10.5": {
  "golden": "1:fb0ce7c2",
  "rows": [
   "(1,1)"
  ],
  "err": ""
 },
 "E10.6": {
  "golden": "1:86599c11",
  "rows": [
   "(2,4027)"
  ],
  "err": ""
 },
 "E13.1": {
  "golden": "11:bbcd158f",
  "rows": [
   "(,,310301174,grand)",
   "(1,,65737398,tenant)",
   "(1,USD,65737398,detail)",
   "(2,,61608441,tenant)",
   "(2,USD,61608441,detail)",
   "(3,,59768245,tenant)",
   "(3,USD,59768245,detail)",
   "(4,,61784155,tenant)",
   "(4,EUR,61784155,detail)",
   "(5,,61402935,tenant)",
   "(5,USD,61402935,detail)"
  ],
  "err": ""
 },
 "E13.2": {
  "golden": "5:f64390e3",
  "rows": [
   "(1,169,616,2464,424,382)",
   "(2,226,570,2382,432,417)",
   "(3,198,592,2337,415,442)",
   "(4,223,589,2421,356,391)",
   "(5,184,633,2396,373,368)"
  ],
  "err": ""
 },
 "E13.3": {
  "golden": "372:22383318",
  "rows": [
   "(\"(none)\",1,1772496)",
   "(\"(none)\",10,2077526)",
   "(\"(none)\",11,2219493)",
   "(\"(none)\",12,2155874)",
   "(\"(none)\",2,1885579)",
   "(\"(none)\",3,1909134)",
   "(\"(none)\",4,1816978)",
   "(\"(none)\",5,2115814)",
   "(\"(none)\",6,2165296)",
   "(\"(none)\",7,2238784)",
   "(\"(none)\",8,1980628)",
   "(\"(none)\",9,2117406)",
   "(cat-1-10,1,635073)",
   "(cat-1-10,10,593755)",
   "(cat-1-10,11,626300)",
   "(cat-1-10,12,615245)"
  ],
  "err": ""
 },
 "E13.4": {
  "golden": "30:12ca6f21",
  "rows": [
   "(1,637,\"2025-02-19 00:00:00+00\",,t)",
   "(1,737,\"2024-08-03 00:00:00+00\",\"2025-02-19 00:00:00+00\",f)",
   "(1,837,\"2024-01-16 00:00:00+00\",\"2024-08-03 00:00:00+00\",f)",
   "(10,1870,\"2025-02-28 00:00:00+00\",,t)",
   "(10,1970,\"2024-08-12 00:00:00+00\",\"2025-02-28 00:00:00+00\",f)",
   "(10,2070,\"2024-01-25 00:00:00+00\",\"2024-08-12 00:00:00+00\",f)",
   "(2,774,\"2025-02-20 00:00:00+00\",,t)",
   "(2,874,\"2024-08-04 00:00:00+00\",\"2025-02-20 00:00:00+00\",f)",
   "(2,974,\"2024-01-17 00:00:00+00\",\"2024-08-04 00:00:00+00\",f)",
   "(3,1011,\"2024-08-05 00:00:00+00\",\"2025-02-21 00:00:00+00\",f)",
   "(3,1111,\"2024-01-18 00:00:00+00\",\"2024-08-05 00:00:00+00\",f)",
   "(3,911,\"2025-02-21 00:00:00+00\",,t)",
   "(4,1048,\"2025-02-22 00:00:00+00\",,t)",
   "(4,1148,\"2024-08-06 00:00:00+00\",\"2025-02-22 00:00:00+00\",f)",
   "(4,1248,\"2024-01-19 00:00:00+00\",\"2024-08-06 00:00:00+00\",f)",
   "(5,1185,\"2025-02-23 00:00:00+00\",,t)"
  ],
  "err": ""
 },
 "E13.5": {
  "golden": "5:7656600a",
  "rows": [
   "(1,124800)",
   "(2,96500)",
   "(3,101300)",
   "(4,93000)",
   "(5,93400)"
  ],
  "err": ""
 }
}
```

#### `goldens_ex_l14.json`

Goldens, level 14.

```json
{
 "C1.1": {
  "golden": "3:7cc530bb",
  "rows": [
   "(111)",
   "(2222)",
   "(3333)"
  ],
  "err": ""
 },
 "C1.2": {
  "golden": "1:ec2bf809",
  "rows": [
   "(999999,1)"
  ],
  "err": ""
 },
 "C1.3": {
  "golden": "2:addb7d1b",
  "rows": [
   "(12)",
   "(13)"
  ],
  "err": ""
 },
 "C1.4": {
  "golden": "2:23dae8cd",
  "rows": [
   "(18)",
   "(38)"
  ],
  "err": ""
 },
 "C1.5": {
  "golden": "2:cc6c5a8d",
  "rows": [
   "(7)",
   "(8)"
  ],
  "err": ""
 },
 "C1.6": {
  "golden": "1:3402ab9a",
  "rows": [
   "(1,idem-DUP,2)"
  ],
  "err": ""
 },
 "C1.7": {
  "golden": "2:b713c027",
  "rows": [
   "(10)",
   "(20)"
  ],
  "err": ""
 },
 "C1.8": {
  "golden": "2:7bd384d1",
  "rows": [
   "(1)",
   "(2)"
  ],
  "err": ""
 },
 "C2": {
  "golden": "65:b63b5f6f",
  "rows": [
   "(1,2025-01-01,9402514,874021,8528493)",
   "(1,2025-02-01,6809875,1083505,5726370)",
   "(1,2025-03-01,7912695,909734,7002961)",
   "(1,2025-04-01,7504048,863021,6641027)",
   "(1,2025-05-01,7344646,723179,6621467)",
   "(1,2025-06-01,8808884,1105547,7703337)",
   "(1,2025-07-01,7762675,1021458,6741217)",
   "(1,2025-08-01,9147558,963955,8183603)",
   "(1,2025-09-01,7270675,760315,6510360)",
   "(1,2025-10-01,7299596,705160,6594436)",
   "(1,2025-11-01,8277019,956314,7320705)",
   "(1,2025-12-01,7403926,867854,6536072)",
   "(1,2026-01-01,0,225828,-225828)",
   "(2,2025-01-01,7084573,708153,6376420)",
   "(2,2025-02-01,6623457,734509,5888948)",
   "(2,2025-03-01,7928689,984166,6944523)"
  ],
  "err": ""
 },
 "C4": {
  "golden": "250:eb4c8d2a",
  "rows": [
   "(1,3)",
   "(1001,3)",
   "(1009,3)",
   "(1017,3)",
   "(1025,3)",
   "(1033,3)",
   "(1041,3)",
   "(1049,3)",
   "(105,3)",
   "(1057,3)",
   "(1065,3)",
   "(1073,3)",
   "(1081,3)",
   "(1089,3)",
   "(1097,3)",
   "(1105,3)"
  ],
  "err": ""
 }
}
```

#### `goldens_wrong.json`

Wrong-path fingerprints.

```json
{
 "E1.1": {
  "why": "BETWEEN with the last calendar day",
  "golden": "162:c85bda05",
  "err": ""
 },
 "E1.3": {
  "why": "`<>` instead of IS DISTINCT FROM",
  "golden": "1559:c2797d13",
  "err": ""
 },
 "E2.5": {
  "why": "integer division",
  "golden": "5:b83b6ee2",
  "err": ""
 },
 "E3.2": {
  "why": "NOT IN over a column containing NULL",
  "golden": "0:d41d8cd9",
  "err": ""
 },
 "E3.5": {
  "why": "plain JOIN fans out orders with two shipments",
  "golden": "1:20e027c7",
  "err": ""
 },
 "E3.7": {
  "why": "rating filter in WHERE after the LEFT JOIN",
  "golden": "98:43c02740",
  "err": ""
 },
 "E4.5": {
  "why": "orders JOIN payments then SUM(total_minor)",
  "golden": "5:45fe10e3",
  "err": ""
 },
 "E4.6": {
  "why": "forgetting that ALL over an empty set is TRUE",
  "golden": "68:6cff1edf",
  "err": ""
 },
 "E5.7": {
  "why": "last_value with the default frame",
  "golden": "60:99a2d437",
  "err": ""
 },
 "E6.4": {
  "why": "plain equi-join returns all three price rows",
  "golden": "808:97a9c21a",
  "err": ""
 },
 "E8.3": {
  "why": "comparing UTC to UTC (wrong AT TIME ZONE direction)",
  "golden": "1:c06c9654",
  "err": ""
 }
}
```

## 4. Concept curriculum

Format per module (same contract as the primer companion): **Core** · **Theory** · **GCP lens** (Lens-1 always) · **Lab** · **Check** (answer before explanation). Tick `- [ ]` when taught *and* checks answered. Ownership: where a §4.0 slice toy exists, the concept modules add analysis only.

### 4.0 Engine slices (DB-1 … DB-10)

*The engine slices.* This file **owns** the slices DB-1 … DB-10; main course A8 points here, and each slice is taught as one session with the companion theory paired to it in §2.1. The Cloud SQL procedure they map onto is OD-11.

Each slice: toy spec, SQL, EXPLAIN prediction, Cloud SQL mapping.


#### DB-1 — Relational algebra & 3VL
- **Toy spec:** In-memory bag relations; implement select/project/join/semi/anti/outer; NULL 3VL truth table tests.
- **SQL:** `SELECT … FROM order_line ol LEFT JOIN product p ON … WHERE p.id IS NULL` (anti-join shape); `EXCEPT` vs `NOT EXISTS`.
- **EXPLAIN prediction:** Nested loop vs hash join for small vs large build side — write prediction, then `EXPLAIN`.
- **Cloud SQL mapping:** Same planner; Query Insights shows top queries; no algebra change because managed.

#### DB-2 — Catalog, tuples, constraints
- **Toy spec:** Schema registry struct; enforce PK/FK/CHECK in a toy before SQL; deferred constraint flag.
- **SQL:** `UUID` PKs; `JSONB` attrs; `CHECK (qty > 0)`; `FOREIGN KEY … DEFERRABLE`; inspect `ctid`/`xmin`/`xmax` in learning DB.
- **EXPLAIN prediction:** PK lookup = index only; missing FK index on child → seq scan on delete-parent check.
- **Cloud SQL mapping:** Flags for constraints; migrations via Job (OD-08); IAM DB users still have catalogs.

#### DB-3 — CTEs, windows, lateral
- **Toy spec:** Window functions as framed iterators over sorted partitions (unit-test ranking).
- **SQL:** Order GMV by day with `SUM() OVER (PARTITION BY day)`; recursive CTE category tree; `LATERAL` top-N per tenant.
- **EXPLAIN prediction:** Window sorts; recursive CTE worktable; predict `Sort` / `CTE Scan` nodes.
- **Cloud SQL mapping:** Same SQL; watch `work_mem` for sorts on small tiers (`db-f1-micro` spills early).

#### DB-4 — Heap pages & TOAST
- **Toy spec:** Slotted page: insert/delete/compact line pointers; overflow TOAST-like external blob store.
- **SQL:** Wide `TEXT`/`JSONB` row; compare `pg_column_size` in-row vs toasted; `VACUUM` effects later (DB-9).
- **EXPLAIN prediction:** Seq scan cost rises with toast fetch — predict heap blocks vs toast blocks in `BUFFERS`.
- **Cloud SQL mapping:** Storage autogrow; you still pay GB-month; Insights won’t replace page literacy.

#### DB-5 — Buffer pool
- **Toy spec:** Clock-sweep buffer pool with pins; hit-ratio benchmark under sequential vs random read.
- **SQL:** Warm cache vs cold (`EXPLAIN (ANALYZE, BUFFERS)` shared hit vs read).
- **EXPLAIN prediction:** Second run of same query → higher shared hit%; predict before measure.
- **Cloud SQL mapping:** Instance memory tier ≈ shared_buffers headroom; scaling tier is how you “buy” cache.

#### DB-6 — Indexes
- **Toy spec:** Userspace B-tree (insert/search/range) + inverted index for tokens (GIN-shaped).
- **SQL:** Composite `(tenant_id, created_at)`; partial `WHERE status = 'open'`; covering `INCLUDE`; `JSONB` GIN.
- **EXPLAIN prediction:** Equality on leftmost → index scan; leading-wildcard `LIKE` → seq; bitmap for OR of two indexes.
- **Cloud SQL mapping:** Create indexes concurrently in expand migrations; monitor bloat; AlloyDB/columnar later if HTAP.

#### DB-7 — Executor & spill
- **Toy spec:** Iterator nodes nested-loop / hash / merge; force spill when “work_mem” exceeded.
- **SQL:** Join order_line↔product; `SET work_mem = '64kB'` in session to force spill; compare.
- **EXPLAIN prediction:** Hash join with low `work_mem` → temp written; predict before `ANALYZE`.
- **Cloud SQL mapping:** Flags `work_mem`/`temp_file` monitoring; do not raise blindly — memory × connections.

#### DB-8 — Planner statistics
- **Toy spec:** Histogram + MCV sketch; estimate selectivity; pick join algorithm from estimates.
- **SQL:** `ANALYZE`; inspect `pg_stats`; compare predicted rows vs `EXPLAIN` rows; create skewed tenant data.
- **EXPLAIN prediction:** Write row estimates for skewed tenant vs uniform; then explain misestimates.
- **Cloud SQL mapping:** Autovacuum/analyze; Query Insights; extend statistics when needed.

#### DB-9 — MVCC, locks, vacuum
- **Toy spec:** Visibility simulator (xmin/xmax snapshots); deadlock graph detector; HOT update sketch.
- **SQL:** Isolation labs (RC vs RR vs Serializable); deliberate deadlock; observe `VACUUM`/bloat.
- **EXPLAIN prediction:** Under RR, predict anomaly prevented; under RC, predict nonrepeatable — confirm.
- **Cloud SQL mapping:** HA does not remove need for vacuum; long txns hurt; set statement timeouts.

#### DB-10 — WAL, replica, PITR (WAL codec; the Cloud SQL side is OD-11)
- **Toy spec:** Mini WAL append/CRC/replay; checkpoint; streaming replica mock; backup/restore drill.
- **SQL:** `pg_switch_wal()` in learning PG; base backup story; promote replica (local compose).
- **EXPLAIN prediction:** N/A for WAL — instead **predict** recovery: crash after commit → row present; after uncommitted → absent.
- **Cloud SQL mapping:** Automated backups, PITR window, HA regional standby, replica flags — name each Cloud SQL knob against the toy.

Do not reimplement PostgreSQL. Do not skip a slice because Cloud SQL hides it.

### 4.1 Pre-SQL prerequisites (PQ-01 … PQ-08)

#### PQ-01 · Sets, relations, functions, bags — stitch: A2
- [ ] done
- **Core:** A relation is a set of tuples over a heading; SQL tables are *bags* (multisets). Functions map each domain element to at most one value — keys are the database word for that.
- **Theory:** Cartesian product size = |R|·|S|; projection can shrink or (with bags) keep duplicates. Bag union vs set union.
- **GCP lens:** Lens-1: BigQuery and Postgres both default to bag semantics (`UNION ALL` preserves). Lens-2: lab seed has deliberate duplicate-risk columns (`idempotency_key` NULL repeats).
- **Lab:** SQL-Z0.1–SQL-Z0.3 on paper: draw R⋈S multiplicities for 2×3 bags.
- **Check:** Why does `SELECT a FROM t UNION SELECT a FROM t` drop duplicates but `UNION ALL` does not? Give multiplicities.

#### PQ-02 · Propositional & predicate logic; 3VL preview — stitch: A2 · DB-1
- [ ] done
- **Core:** Predicates evaluate to TRUE / FALSE / UNKNOWN. Filters keep only TRUE. `NOT UNKNOWN = UNKNOWN`.
- **Theory:** Truth tables for AND/OR/NOT with UNKNOWN; why `WHERE col = NULL` never matches.
- **GCP lens:** Lens-1: Cloud SQL Postgres 3VL matches the standard. Lens-3: BigQuery `IS DISTINCT FROM` exists (verify).
- **Lab:** SQL-Z0.4: fill the 3VL table for `country <> 'US'` when country is NULL.
- **Check:** Does `NOT (x = 1)` include rows where x IS NULL? Prove with a truth table.

#### PQ-03 · Types, encodings, integer money vs float — stitch: A2
- [ ] done
- **Core:** Prefer `numeric`/`bigint` minor units for money; never `float`/`double` for currency. UTF-8; beware BOM and `char(n)` padding.
- **Theory:** Half-up vs banker rounding; IEEE recall from A2 then add decimal semantics.
- **GCP lens:** Lens-1: Cloud SQL flags for `extra_float_digits`; Spanner NUMERIC. Lens-2: lab stores `price_minor int`.
- **Lab:** SQL-E2.1 / SQL-E2.7: predict aggregates stay integer/numeric.
- **Check:** Why is `0.1 + 0.2` unsafe for money in float but fine as integer cents?

#### PQ-04 · Files, CSV/JSON, encodings — stitch: A3 + A6 · V-STOR
- [ ] done
- **Core:** CSV NULL vs empty string; JSON vs JSONL; COPY options; UTF-8.
- **Theory:** Encoding traps that flip fingerprints (BOM, CRLF).
- **GCP lens:** Lens-1: GCS → Cloud SQL import; BigQuery load jobs. Lens-2: `stg_import` messy rows in seed.
- **Lab:** SQL-E8.8–SQL-E8.10 cleaning ladder.
- **Check:** Name two ways a CSV import silently changes row count.

#### PQ-05 · psql, Docker Postgres, env hygiene — stitch: A3 + A6 · C1
- [ ] done
- **Core:** `psql` meta-commands, `ON_ERROR_STOP`, connection env vars, Docker volume + healthcheck.
- **Theory:** Session `TimeZone` and `lc_collate` affect fingerprints.
- **GCP lens:** Lens-1: Cloud SQL Auth Proxy as the remote twin of local Docker. Lens-2: §3 compose file.
- **Lab:** Bring lab up; `lab.chk` of `SELECT 1` returns `1:…`.
- **Check:** Which two session settings invalidate every golden in this file?

#### PQ-06 · Python DB-API & parameter binding — stitch: A3 + A6 · C1 + Phase 4 Security
- [ ] done
- **Core:** Placeholders, never string format for SQL; transactions at the connection; cursor hygiene.
- **Theory:** Injection is a binding failure, not a clever-escape problem.
- **GCP lens:** Lens-1: Cloud SQL Connector for Python. Lens-2: `run_ex.py` pattern.
- **Lab:** BH-2 injection hunt.
- **Check:** Rewrite a f-string query into a parameterised call.

#### PQ-07 · Sorting, hashing, trees, binary search as access-path raw material — stitch: A4 · DB-6
- [ ] done
- **Core:** These are the primitives behind indexes and joins — not a second CS course.
- **Theory:** Binary search → B-tree leaf walk; hash → hash join / hash index.
- **GCP lens:** Lens-1: recall only; formula depth in CS-02. Lens-2: none beyond paper.
- **Lab:** SQL-Z0.7, TD-10 fan-out arithmetic.
- **Check:** Given fan-out 100 and 1e6 leaves, about how many levels?

#### PQ-08 · Storage hierarchy & page/row arithmetic — stitch: A1/A2 recall · DB-4
- [ ] done
- **Core:** L1/L2/RAM/SSD/HDD orders of magnitude; 8 KiB pages; rows per page ≈ usable/avg_row.
- **Theory:** Fill-factor and HOT-update intuition (analytic, not a second slotted-page toy).
- **GCP lens:** Lens-1: Cloud SQL machine memory vs dataset working set. Lens-2: SQL-Z0.8 napkin.
- **Lab:** SQL-Z0.8: estimate pages for 20k orders.
- **Check:** If avg row is 200 B on 8 KiB pages at 90% fill, rows/page ≈ ?

### 4.2 Relational theory (RT-01 … RT-08)

#### RT-01 · Relational model, keys, integrity — stitch: A8 / DB-2 · SQL-SKIP-SQL
- [ ] done
- **Core:** Heading, body, candidate/primary/foreign keys, entity & referential integrity.
- **Theory:** Superkey vs candidate key; NULLs and uniqueness (UNIQUE allows multiple NULLs in Postgres).
- **GCP lens:** Lens-1: Cloud SQL constraints enforce the same rules; Spanner interleaved parents are a physical clustering choice on top of keys.
- **Lab:** TD-1; lab composite FK `(tenant_id, user_id)`.
- **Check:** Why does UNIQUE allow two NULLs in Postgres but PRIMARY KEY does not?

#### RT-02 · Relational algebra (set and bag) — stitch: A8 / DB-1
- [ ] done
- **Core:** σ π ⋈ ∪ ∩ − ×; bag variants; rewrite laws (push σ through ⋈).
- **Theory:** Equivalence of expressions; why bag projection is not idempotent.
- **GCP lens:** Lens-1: EXPLAIN nodes are physical cousins of algebra ops. Lens-2: DB-1 toy owns the executable; here we rewrite on paper.
- **Lab:** TD-5, TD-6, TD-7.
- **Check:** Push `σ_{a=1}` through an equijoin on `a`; show both plans.

#### RT-03 · Tuple/domain calculus & safety (SQL-T-GR) — stitch: A8 + A9 · DB-3
- [ ] done
- **Core:** Declarative `{t | P(t)}`; domain calculus; safety (finite results); Codd equivalence.
- **Theory:** Unsafe query examples; how SQL WITH RECURSIVE can leave the safe fragment.
- **GCP lens:** Lens-1: Spanner GoogleSQL stays in a practical safe fragment; recursion limits differ (verify).
- **Lab:** TD-16 recursion termination.
- **Check:** Give one unsafe calculus query and its SQL temptation.

#### RT-04 · Functional dependencies, closure, cover — stitch: A8 / DB-2 · SQL-SKIP-SQL
- [ ] done
- **Core:** X → Y; attribute closure; candidate keys from FDs; canonical cover.
- **Theory:** Armstrong axioms; why transitive FDs matter for 3NF.
- **GCP lens:** Lens-1: schema ADRs cite FDs explicitly. Lens-2: TD-2/3.
- **Lab:** TD-1…TD-4.
- **Check:** Compute closure of `{tenant_id, sku}` on the product heading.

#### RT-05 · Normal forms 1NF…BCNF (+ 4NF/5NF-lite) — stitch: A8 · SQL-SKIP-SQL
- [ ] done
- **Core:** 1NF atomicity; 2NF full FD to key; 3NF no transitive; BCNF; lossless & dependency-preserving decompositions.
- **Theory:** When BCNF loses dependency preservation; MVDs lite.
- **GCP lens:** Lens-1: the lab's OLTP schema stays ≥3NF; analytics star schemas deliberately denormalise (AN-01).
- **Lab:** TD-3, TD-4; SCH-1.
- **Check:** Is `product(tenant_id, sku, price, currency)` in BCNF if `tenant_id → currency`?

#### RT-06 · ER → tables — stitch: A7 · DD-01
- [ ] done
- **Core:** Entities, relationships, cardinality, weak entities, ISA → table patterns.
- **Theory:** Foreign-key placement for 1:N vs N:M.
- **GCP lens:** Lens-1: schema ADR in HLD pack. Lens-2: the lab ER diagram (the storefront OLTP schema, §3).
- **Lab:** SCH-1 draw-and-map.
- **Check:** Map a ternary relationship to tables without inventing a hidden FD.

#### RT-07 · Integrity as specification — stitch: DD-12 · SQL-E10
- [ ] done
- **Core:** CHECK, UNIQUE, FK, EXCLUDE, deferrable constraints — constraints are the executable spec.
- **Theory:** NOT VALID + VALIDATE; constraint exclusion vs RLS.
- **GCP lens:** Lens-1: Cloud SQL supports the Postgres catalogue; Spanner interleaved deletes cascade by design (verify).
- **Lab:** SQL-E10.1–SQL-E10.5.
- **Check:** Name a business rule that needs EXCLUDE rather than UNIQUE.

#### RT-08 · Query equivalence & rewrite rules — stitch: DB-1 · CS-08
- [ ] done
- **Core:** Predicate pushdown, join reordering under constraints, outer-join rewrites that are *not* always legal.
- **Theory:** Why `WHERE` after `LEFT JOIN` can nullify the outer join.
- **GCP lens:** Lens-1: planner rewrites; you must still predict multiplicity. Lens-2: SQL-E3.7 trap.
- **Lab:** TD-7; SQL-E3.7.
- **Check:** When is `σ (R ⟕ S)` ≠ `(σ R) ⟕ S`?

### 4.3 SQL language (SL-01 … SL-14)

#### SL-01 · DDL, types, constraints — stitch: A8 / DB-2
- [ ] done
- **Core:** CREATE TABLE, types (`int`, `bigint`, `numeric`, `text`, `timestamptz`, `jsonb`, ranges), PRIMARY/UNIQUE/CHECK/FK.
- **Theory:** Identity vs serial; domains; collations.
- **GCP lens:** Lens-1: Cloud SQL Postgres DDL; AlloyDB same dialect family. Lens-2: `lab_schema.sql`.
- **Lab:** SQL-E10 battery; read schema end-to-end once.
- **Check:** Why is `timestamptz` preferred over `timestamp` for event time?

#### SL-02 · Logical evaluation order — stitch: SQL-SKIP-SQL
- [ ] done
- **Core:** FROM → WHERE → GROUP BY → HAVING → WINDOW → SELECT → DISTINCT → ORDER BY → LIMIT. Aliases in SELECT are not visible in WHERE.
- **Theory:** Lateral and APPLY as left-to-right correlation.
- **GCP lens:** Lens-1: BigQuery and Postgres share the logical model with dialect wrinkles (DT-1).
- **Lab:** SQL-E1 warm-ups: predict column visibility errors before running.
- **Check:** Why can you `ORDER BY` a SELECT alias but not `WHERE` it?

#### SL-03 · NULL & three-valued logic — stitch: DB-1 · PQ-02
- [ ] done
- **Core:** `IS NULL` / `IS DISTINCT FROM` / `COALESCE` / `NULLIF`; aggregate skip-NULL rules; UNIQUE+NULL.
- **Theory:** Primary keys forbid NULL; CHECK treats UNKNOWN as pass.
- **GCP lens:** Lens-1: same 3VL on Cloud SQL; Oracle NULL-empty-string collapse is the Rosetta trap.
- **Lab:** SQL-E1.2, SQL-E1.3, SQL-E1.5.
- **Check:** Write the 3VL table for `NOT (country = 'US')`.

#### SL-04 · Joins: inner, outer, cross, self, semi, anti, lateral, non-equi — stitch: DB-1 · SQL-SKIP-SQL
- [ ] done
- **Core:** Join types as filters on the product; semi/anti via EXISTS/NOT EXISTS; LATERAL for dependent subqueries; range joins.
- **Theory:** Fan-out: joining a 1:N table multiplies rows — sum after join is a classic bug.
- **GCP lens:** Lens-1: Spanner interleaving physicalises parent-child joins; SQL shape still matters. Lens-2: SQL-E3 ladder.
- **Lab:** SQL-E3.1–SQL-E3.10; SQL-E6.4 as-of shape (leakage owner is DD-05).
- **Check:** Why does `NOT IN (subquery with NULL)` return empty?

#### SL-05 · Aggregation & grouping sets — stitch: SQL-SKIP-SQL · AN-01
- [ ] done
- **Core:** `COUNT(*)` vs `COUNT(col)` vs `COUNT(DISTINCT)`; `FILTER`; `GROUPING SETS`/`ROLLUP`/`CUBE`; ordered-set aggregates.
- **Theory:** Functional dependency relaxation in Postgres when grouping by PK.
- **GCP lens:** Lens-1: BigQuery `GROUP BY ROLLUP` cost = bytes scanned. Lens-2: SQL-E2, SQL-E13.1.
- **Lab:** SQL-E2.1–SQL-E2.8; SQL-E13.1–SQL-E13.2.
- **Check:** When is `avg(x)` not equal to `sum(x)/count(*)`?

#### SL-06 · Subqueries: scalar, IN, EXISTS, ALL/ANY, division — stitch: SQL-SKIP-SQL
- [ ] done
- **Core:** Correlated vs uncorrelated; `= ALL` over empty is TRUE; relational division patterns.
- **Theory:** Unnesting mentally before asking the planner.
- **GCP lens:** Lens-1: same shapes on Cloud SQL; Spanner subquery limits (verify).
- **Lab:** SQL-E4.1–SQL-E4.8.
- **Check:** Predict `> ALL (empty)` and `> ANY (empty)`.

#### SL-07 · Set operations — stitch: DB-1
- [ ] done
- **Core:** `UNION`/`INTERSECT`/`EXCEPT` (± ALL); column type matching; ORDER BY scope.
- **Theory:** Bag vs set cardinality.
- **GCP lens:** Lens-1: BigQuery `EXCEPT DISTINCT` naming. Lens-2: SQL-E4.3/SQL-E4.4.
- **Lab:** SQL-E4.3, SQL-E4.4.
- **Check:** Does `UNION` ever keep two identical rows?

#### SL-08 · Window functions & frames — stitch: DB-3 · SQL-SKIP-SQL
- [ ] done
- **Core:** `RANK`/`DENSE_RANK`/`ROW_NUMBER`; `SUM/AVG` over frames; `ROWS` vs `RANGE`; `EXCLUDE`; running balances; gaps-and-islands.
- **Theory:** Default frame for ordered windows is `RANGE UNBOUNDED PRECEDING` — surprises `last_value`.
- **GCP lens:** Lens-1: BigQuery windows; billing-export patterns at 10.3 reuse these shapes. Lens-2: SQL-E5–E6.
- **Lab:** SQL-E5.1–SQL-E5.8, SQL-E6.1–SQL-E6.7.
- **Check:** Why is `last_value` wrong with the default frame for 'latest price'?

#### SL-09 · CTEs & recursion — stitch: DB-3 · CS-11
- [ ] done
- **Core:** `WITH`, `WITH RECURSIVE`, working table, termination, cycle detection via path arrays; searchable vs cycle options (PG14+).
- **Theory:** Recursion expressiveness vs SQL without recursion.
- **GCP lens:** Lens-1: Spanner has statement timeouts; depth limits differ (verify). Lens-2: E7.
- **Lab:** SQL-E7.1–SQL-E7.5.
- **Check:** How do you detect a cycle without hanging?

#### SL-10 · DML, RETURNING, upsert, MERGE — stitch: A7 · A9 + ARCH-11
- [ ] done
- **Core:** `INSERT…ON CONFLICT`, `UPDATE…FROM`, writable CTEs, `MERGE` (PG15+), `DELETE…RETURNING`. `SAVEPOINT name` / `ROLLBACK TO SAVEPOINT name` / `RELEASE SAVEPOINT name` undo part of a transaction without abandoning it (one failed row in a batch, retried or skipped); in PostgreSQL any error aborts the whole transaction until you roll back to a savepoint (psql's `\set ON_ERROR_ROLLBACK on` sets an implicit savepoint before each statement to do exactly that). `LISTEN channel` / `NOTIFY channel, 'payload'` (or `pg_notify(channel, payload)`) as the wake-up beside a `FOR UPDATE SKIP LOCKED` queue table or an outbox: the notification is sent when the transaction commits, and never if it rolls back.
- **Theory:** Idempotency keys; batching to bound WAL/bloat. A notification is a hint, not a message: it reaches only sessions listening at commit time and is never stored, so a worker drains the table after every wake-up and every reconnect (DBT.9, DBT-P15). A listener needs its own long-lived session, so it cannot sit behind a transaction-mode connection pooler.
- **GCP lens:** Lens-1: Cloud SQL PG15 MERGE; Spanner mutations API vs SQL DML. Lens-2: E9.
- **Lab:** SQL-E9.1–SQL-E9.7; TX-5.
- **Check:** What uniqueness constraint makes an upsert actually idempotent?

#### SL-11 · Views, materialised views, functions, triggers — stitch: V-DATA
- [ ] done
- **Core:** Updatability limits; matview refresh; `SECURITY DEFINER` hazards; triggers as integrity amplifiers (use sparingly).
- **Theory:** Where business logic should *not* hide.
- **GCP lens:** Lens-1: BigQuery authorised views; AlloyDB matviews. Lens-2: SQL-E9.1 materialise daily GMV.
- **Lab:** SQL-E9.1; SCH-6 masking view sketch.
- **Check:** Name one reason a trigger is worse than a constraint for the same rule.

#### SL-12 · Dates, time zones, JSON, text, regex — stitch: V-STOR · D3
- [ ] done
- **Core:** `timestamptz`, `AT TIME ZONE`, `date_trunc`, JSONB operators `@>`/`->`/`JSONB_PATH`, `LIKE`/`regex`.
- **Theory:** Never `now()` in reproducible labs; DST pitfalls.
- **GCP lens:** Lens-1: BigQuery `TIMESTAMP` vs `DATETIME`; Postgres JSONB vs Spanner JSON. Lens-2: E8.
- **Lab:** SQL-E8.1–SQL-E8.10.
- **Check:** Which direction of `AT TIME ZONE` converts *stored UTC* to a New York *civil* date?

#### SL-13 · Security in SQL: GRANT, RLS, injection — stitch: B5 · A10 · A9
- [ ] done
- **Core:** Roles vs IAM principals; least privilege; RLS policies + `FORCE`; parameter binding; owner bypass.
- **Theory:** Column encryption vocabulary (`pgcrypto`) — product rules stay in gcp 7.3.
- **GCP lens:** Lens-1: Cloud SQL IAM DB auth; RLS with `current_setting`. Lens-2: SQL-E10.6.
- **Lab:** SQL-E10.6, BH-2.
- **Check:** Why does table owner bypass RLS unless `FORCE ROW LEVEL SECURITY`?

#### SL-14 · Dialects and the standard — stitch: A8 + V-STOR · §8
- [ ] done
- **Core:** What is ISO SQL vs vendor; common deltas (LIMIT/TOP/FETCH, UPSERT shapes, NULL=empty).
- **Theory:** Rosetta discipline: translate the *idea*, then the spelling.
- **GCP lens:** Lens-1: DT drills across Postgres/MySQL/SQL Server/BigQuery/Spanner. Lens-2: DT-1…DT-8.
- **Lab:** DT-1 start.
- **Check:** Name three features that are Postgres-native and one portable rewrite.

### 4.4 CS under the engine (CS-01 … CS-11)

#### CS-01 · Storage layouts & page arithmetic — stitch: DB-4
- [ ] done
- **Core:** Heap pages, item identifiers, alignment, TOAST for oversized values — *analytic layer only* (toy is DB-4).
- **Theory:** Rows/page, fill-factor, update HOT vs non-HOT intuition.
- **GCP lens:** Lens-1: Cloud SQL storage autosize; AlloyDB columnar extension is separate (CS-09). Lens-2: SQL-Z0.8.
- **Lab:** SQL-Z0.8 napkin with lab row widths.
- **Check:** Estimate pages for 20k orders at 150 B/row on 8 KiB pages.

#### CS-02 · B-tree/B+/hash/LSM/bitmap/GIN/GiST/BRIN — stitch: DB-6 · A9
- [ ] done
- **Core:** Height ≈ log_fanout(n); leftmost prefix rule; LSM write amp vs B-tree read amp; GIN for JSONB/arrays; BRIN for append-mostly. An LSM memtable is usually a skip list (A4.D6): ordered, cheap concurrent inserts, flushed in key order as an SSTable.
- **Theory:** Partial and covering indexes.
- **GCP lens:** Lens-1: Cloud SQL and AlloyDB (B-tree pages) vs Bigtable (LSM write path); here formulas + PX cards and the build lab below. Lens-2: PX-1…PX-6.
- **Build lab `[paper]`:** a written LSM-vs-B-tree comparison with one flush diagram (memtable → immutable memtable → SSTable flush → compaction). Count the writes one update costs in each design, and explain why Bigtable's write path differs from Cloud SQL's B-tree pages. No full engine.
- **Lab:** PX-1…PX-6; TD-10.
- **Check:** Why does `LIKE '%x'` refuse a default B-tree?

#### CS-03 · External sort, join & aggregation I/O cost — stitch: DB-7
- [ ] done
- **Core:** Block nested-loop, hash join (Grace), sort-merge; temp files when work_mem is tight.
- **Theory:** Cost ≈ pages read/written; selectivity changes the winner.
- **GCP lens:** Lens-1: Cloud SQL `work_mem` flag; observe temp files. Lens-2: PX-7, PX-10, TD-11.
- **Lab:** PX-7, PX-10.
- **Check:** When does nested-loop beat hash on a selective probe?

#### CS-04 · Buffer caching theory — stitch: DB-5
- [ ] done
- **Core:** Hit ratio vs working set; sequential flooding; scan resistance; clock sweep recall (toy is DB-5).
- **Theory:** Why `EXPLAIN` shared hit vs read matters.
- **GCP lens:** Lens-1: Cloud SQL memory sizing. Lens-2: PX-9 hit vs read.
- **Lab:** PX-9.
- **Check:** What workload tanks a clock cache if it is not scan-resistant?

#### CS-05 · Concurrency: serializability, 2PL, TSO, MVCC/SI, SSI — stitch: DB-9 · SQL-SKIP-ENGINE
- [ ] done
- **Core:** Conflict serializability & precedence graphs; 2PL; snapshot isolation anomalies (write skew); SSI in Postgres SERIALIZABLE.
- **Theory:** Lost update under RC read-modify-write.
- **GCP lens:** Lens-1: Cloud SQL isolation defaults; Spanner external consistency is a different mechanism (TrueTime) — do not smuggle as a Postgres prop. Lens-2: TX labs.
- **Lab:** TX-1…TX-8; TD-8, TD-9.
- **Check:** Draw the precedence graph for a dirty-write attempt.

#### CS-06 · Recovery: WAL, steal/no-force, ARIES — stitch: DB-10
- [ ] done
- **Core:** Steal/no-force ⇒ redo + undo; checkpoints; ARIES three passes — analytic layer (toy is DB-10 mini-WAL).
- **Theory:** RPO as how far back is the last archived segment.
- **GCP lens:** Lens-1: Cloud SQL PITR; discards are gcp-owned runbooks. Lens-2: TD-12; OD-04 drill outline.
- **Lab:** TD-12.
- **Check:** Why does no-force still need redo after a crash?

#### CS-07 · Replication, consensus, 2PC, consistency models — stitch: DB-10 · A9 + V-STOR · ARCH-11
- [ ] done
- **Core:** Physical vs logical replication (a publication on the source, a subscription on the target, row changes decoded from the WAL, across major versions); change data capture as the same logical decoding read by another system (Debezium, Datastream) through a replication slot, which keeps WAL on the primary until the consumer confirms it, so a dead consumer fills the disk; CDC is the log-based alternative to the outbox's polling reader; failover; why 2PC is not the default answer (outbox owns the product pattern).
- **Theory:** TrueTime/Paxos *vocabulary* when A9 and primer SD-25 are unlocked — no second Spanner toy.
- **GCP lens:** Lens-1: Cloud SQL replicas; Spanner; recall primer SD-14…17 for scale-out *interview* layer (do not re-teach).
- **Lab:** TD-14; BH-5 lag SLI.
- **Check:** Name one failure mode 2PC does not solve that outbox does.

#### CS-08 · Cardinality estimation & join ordering — stitch: DB-8
- [ ] done
- **Core:** Histograms, MCV, independence assumption failure; Selinger DP sketch; correlated stats.
- **Theory:** Estimation error compounds through join trees.
- **GCP lens:** Lens-1: `CREATE STATISTICS`; Query Insights. Lens-2: PX-8; TD-13.
- **Lab:** PX-8.
- **Check:** Why can a 10× estimate error flip hash join to nested loop?

#### CS-09 · Columnar & vectorised execution — stitch: V-STOR · AN-02
- [ ] done
- **Core:** Late materialisation, SIMD-friendly operators, compression (RLE/dict).
- **Theory:** OLTP row store vs OLAP column store trade-off.
- **GCP lens:** Lens-1: BigQuery; AlloyDB columnar. Lens-2: SQL-E13 cost reading.
- **Lab:** DT-2 bytes-scanned napkin.
- **Check:** Why is `SELECT *` punitive on a column store?

#### CS-10 · Index selection complexity & covering — stitch: DB-6 · OD-01
- [ ] done
- **Core:** Which queries an index can answer alone (index-only); INCLUDE columns; trade-offs of write amplification.
- **Theory:** Too many indexes = slower upserts.
- **GCP lens:** Lens-1: Cloud SQL Advisor suggestions are hypotheses, not orders. Lens-2: PX-5.
- **Lab:** PX-5 covering.
- **Check:** When does a covering index still heap-fetch?

#### CS-11 · Recursion & query expressiveness — stitch: DB-3 · SL-09
- [ ] done
- **Core:** Linear recursion; what SQL cannot express without recursion/windows; termination metrics.
- **Theory:** Complexity of transitive closure.
- **GCP lens:** Lens-1: graph patterns sometimes leave SQL (AN-06/07). Lens-2: SQL-E7.5 cycle.
- **Lab:** SQL-E7.5; TD-16.
- **Check:** Is graph reachability expressible in relational algebra without recursion/fixpoint?

### 4.5 Data design (DD-01 … DD-13)

#### DD-01 · Conceptual → logical → physical — stitch: A7
- [ ] done
- **Core:** ER/concepts → normalised tables → indexes/partitioning/storage params; schema ADRs.
- **Theory:** Every physical shortcut needs an ADR ('I pick X because Y, accept Z').
- **GCP lens:** Lens-1: HLD pack schema section. Lens-2: SCH-1.
- **Lab:** SCH-1.
- **Check:** Write one ADR sentence for choosing surrogate keys in `customer_order`.

#### DD-02 · Keys: natural, surrogate, UUID, snowflake — stitch: DB-2
- [ ] done
- **Core:** Stability, width, index locality, client generation vs DB generation.
- **Theory:** UUID v4 random I/O vs time-ordered IDs.
- **GCP lens:** Lens-1: Spanner bit-reversed sequences for hotspots (verify). Lens-2: lab uses bigint surrogates.
- **Lab:** SCH-2.
- **Check:** Name one operational pain of random UUIDs as PKs on B-trees.

#### DD-03 · Money, units, time — stitch: A8 · A2
- [ ] done
- **Core:** Integer minor units; explicit currency; `timestamptz` for instants; civil dates as `date`.
- **Theory:** Never float money; never implicit TZ.
- **GCP lens:** Lens-1: the ledger rules below, on Cloud SQL Postgres. Lens-2: SQL-E4.5, SQL-CAP2.
- **Lab:** SQL-E4.5, SQL-CAP2.
- **Check:** Why store both `currency` and `total_minor` rather than a float USD conversion?
- **Ledger rules (owned here):** amounts in integer minor units (`bigint`) with an explicit currency, never `float`. The payment provider is the system of record for money movement: the database stores provider tokens, payment and session IDs, amounts, currency and status — never card numbers (cyber PV-03). An order moves `created → requires_action → paid → fulfilled | refunded | failed`, and every arrow has a written guard (who, or what evidence). Illegal: `fulfilled` without `paid`; `paid` without a verified provider event (a browser redirect is not proof of payment); skipping `requires_action` when the provider demands it. A refund (`paid | fulfilled → refunded`) tracks the remaining minor units for partial refunds. A replayed provider event must not fulfil twice: idempotency key plus `ON CONFLICT` (SL-10).
- **Build lab `[local]`:** the lab's `customer_order.status` uses a smaller set (`created`, `paid`, `fulfilled`, `refunded`, `cancelled`). Write the transition table for it, a check that rejects illegal arrows (a trigger or one guarded `UPDATE … WHERE status = …`), and table tests for every legal and every illegal transition.

#### DD-04 · Hierarchies & graphs in SQL — stitch: SL-09
- [ ] done
- **Core:** Adjacency list, closure table, path enumeration, nested sets — trade-offs.
- **Theory:** Lab uses adjacency lists (`category.parent_id`, `app_user.referred_by`).
- **GCP lens:** Lens-1: when to leave for a graph DB (AN-06). Lens-2: E7.
- **Lab:** SQL-E7.1–SQL-E7.4; SCH-3.
- **Check:** Which hierarchy pattern makes 'subtree products' cheap?

#### DD-05 · Temporal data & SCD — stitch: D3 · A8
- [ ] done
- **Core:** Valid-time vs transaction-time; SCD2 `valid_from`/`valid_to`; as-of join shapes.
- **Theory:** This module owns leakage prevention as well as the SQL shapes. **Leakage** is a feature built from information that did not exist at prediction time — most often a label or a later row pulled in by a plain equi-join. Train/serving skew (online features computed differently from training features) is a different failure, taught with D3.
- **Build lab `[local]`:** build a feature table keyed by `event_time`; join labels with a plain join and measure the inflated metric; rewrite it as an as-of join (`LATERAL … WHERE valid_from <= t ORDER BY valid_from DESC LIMIT 1`) and show the metric fall back. Keep the failing test and the passing test.
- **GCP lens:** Lens-1: feature stores / as-of joins. Lens-2: SQL-E6.4, SQL-E13.4, SQL-E13.5.
- **Lab:** SQL-E13.4–SQL-E13.5.
- **Check:** Write the predicate for 'price in effect at `placed_at`'.

#### DD-06 · JSONB vs relational — stitch: A8 + V-STOR
- [ ] done
- **Core:** Stable queryable attributes → columns; open-ended attrs → JSONB with GIN; hybrid.
- **Theory:** Constraints are weaker inside JSON.
- **GCP lens:** Lens-1: Firestore when document model wins (AN-06). Lens-2: `product.attrs`.
- **Lab:** SQL-E8.5–SQL-E8.7; DT-7.
- **Check:** When does JSONB become a schema smell?

#### DD-07 · Soft delete, audit, history — stitch: A8
- [ ] done
- **Core:** `deleted_at`; history tables; append-only audit; who-can-see-deleted policies.
- **Theory:** Unique constraints must consider soft delete (`UNIQUE … WHERE deleted_at IS NULL`).
- **GCP lens:** Lens-1: control-plane audit in 11b. Lens-2: SQL-CAP1 invariants.
- **Lab:** SQL-E10.3 partial unique; SQL-CAP1.
- **Check:** How do you keep email unique among *live* users only?

#### DD-08 · Denormalisation with ADRs — stitch: A7 · primer SD-18
- [ ] done
- **Core:** Cache columns, aggregate tables, counter fields — only with refresh rules and ADR.
- **Theory:** Do not re-teach primer SD-18; add SQL maintenance patterns.
- **GCP lens:** Lens-1: materialised views / nightly jobs. Lens-2: SQL-E9.1 daily GMV.
- **Lab:** SCH-2, SQL-E9.1.
- **Check:** Write the refresh invariant for a cached `total_minor`.

#### DD-09 · Multi-tenancy — stitch: A9 · SL-13
- [ ] done
- **Core:** Shared tables + `tenant_id` vs separate DBs/schemas; composite FKs; RLS defence in depth.
- **Theory:** Hot-tenant skew; a noisy tenant is capped by a per-tenant limit (cyber AB-01 owns the limiter).
- **GCP lens:** Lens-1: RLS on Cloud SQL Postgres with the tenant set per transaction (`SET LOCAL`; SL-13 owns the syntax); here the design — policies + composite FKs. Lens-2: SQL-E10.2, SQL-E10.6.
- **Lab:** SQL-E10.2, SQL-E10.6, PX-1 hot key.
- **Check:** Why is a single-column FK to `user_id` unsafe in a multi-tenant DB?

#### DD-10 · Partitioning & sharding-key design — stitch: primer SD-17 · A9 + V-STOR
- [ ] done
- **Core:** Range/list/hash partitioning; prune-friendly predicates; shard key = join/locality key.
- **Theory:** Interview scale-out stays in primer SD-17; here SQL partition pruning.
- **GCP lens:** Lens-1: Cloud SQL declarative partitioning; Spanner parent keys. Lens-2: SCH-5.
- **Lab:** SCH-5; PX prune thought-experiment.
- **Check:** What predicate prevents partition pruning?

#### DD-11 · Schema evolution (expand/contract) — stitch: A8 + C4
- [ ] done
- **Core:** Add nullable → backfill → constrain → switch reads → drop old; lock levels; `CREATE INDEX CONCURRENTLY`; `NOT VALID`.
- **Theory:** OD-08 owns running migrations as jobs; here lock/SQL craft.
- **GCP lens:** Lens-1: Cloud SQL maintenance windows. Lens-2: SQL-E9.6 chunked backfill.
- **Lab:** SQL-E9.6, SCH-4.
- **Check:** Which lock does `ALTER … SET NOT NULL` take on a big table without a rewrite strategy?

#### DD-12 · Data quality as constraints — stitch: RT-07 · SQL-E10
- [ ] done
- **Core:** If it can be expressed as a constraint, it should be — before app code.
- **Theory:** Deferral for cyclic FKs; EXCLUDE for ranges.
- **GCP lens:** Lens-1: same on Cloud SQL. Lens-2: SQL-E10.1–SQL-E10.5.
- **Lab:** SQL-E10 battery.
- **Check:** Encode 'no overlapping price intervals' as a constraint type.

#### DD-13 · Hot-key skew & partition keys — stitch: A9
- [ ] done
- **Core:** Measure skew with SQL; design keys that spread writes; avoid sequential hotspots.
- **Theory:** Lab: user 1 is hot (~135 orders) — see PX-1.
- **GCP lens:** Lens-1: Spanner and Bigtable key design (primer SD-23 owns row keys); build lab below. Lens-2: skew query on lab.
- **Lab:** PX-1; SCH-5.
- **Check:** Write a query that ranks users by order count and spot the hotspot.
- **Build lab `[local]`:** a key histogram. Count writes per key on the lab data (user 1 ≈ 135 orders), then compare three keys for a `(tenant, sku, ts)` event log — timestamp first, a hash prefix, a reversed timestamp — by simulating the partition each write lands in. Unit-test that the chosen partitioner keeps every partition within a stated bound of the mean.

### 4.6 Operating databases (OD-01 … OD-11)

#### OD-01 · Indexing strategy & EXPLAIN workflow — stitch: C6 · DB-6
- [ ] done
- **Core:** Hypothesis → `EXPLAIN (ANALYZE, BUFFERS)` → change one thing → re-measure; sargability.
- **Theory:** Never index every column.
- **GCP lens:** Lens-1: Query Insights. Lens-2: PX-1…PX-11, SQL-CAP4.
- **Lab:** §7.1 PX cards.
- **Check:** What four EXPLAIN fields do you read before changing an index?

#### OD-02 · Statistics & slow-query observability — stitch: C6
- [ ] done
- **Core:** `pg_stat_statements`, auto_explain, wait events; stale analyze symptoms. Live triage from `pg_stat_activity` (state, `wait_event_type`, `xact_start`, `query`): an `idle in transaction` session holds its locks and its snapshot, so it blocks DDL and stops vacuum; `pg_blocking_pids(pid)` names who blocks whom; `pg_cancel_backend` stops a query and `pg_terminate_backend` ends the session; `lock_timeout`, `statement_timeout` and `idle_in_transaction_session_timeout` bound all three.
- **Theory:** Logs are evidence packs, not vibes.
- **GCP lens:** Lens-1: Cloud Logging + Query Insights. Lens-2: PX-8 before/after ANALYZE.
- **Lab:** PX-8.
- **Check:** Name two symptoms of stale statistics.

#### OD-03 · Connection pooling & pool math — stitch: B3 · A9 · V-STOR
- [ ] done
- **Core:** instances × pool ≤ `max_connections`; session vs transaction vs statement pooler modes; what breaks in transaction mode (session locals, prepared statements, advisory locks).
- **Theory:** the pool-math worksheet, built here: one row per workload that connects (each Cloud Run service, each job, admin tools), with columns max instances, pool size per instance and their product. The sum must stay at or below `max_connections` minus the reserved superuser slots, with headroom for the reconnect storm after a failover. Add a test that fails when a configuration change breaks the inequality.
- **GCP lens:** Lens-1: Cloud SQL + managed pooler / Auth Proxy. Lens-2: TX-8 thought-lab.
- **Lab:** TX-8.
- **Check:** Which pooler mode breaks `SET LOCAL` lasting across statements?

#### OD-04 · Backup / restore / PITR drills — stitch: DB-10 · V-STOR + DB-10
- [ ] done
- **Core:** Runbook literacy: schedule, retain, test restore to a *new* instance, measure RPO/RTO. Logical backup (`pg_dump -Fc` / `pg_restore`, one database, portable across major versions, restores to the moment of the dump) versus physical backup with continuous WAL archiving (`pg_basebackup` plus archived WAL, the whole cluster, point-in-time recovery to any moment covered by the archive); the second is what managed services such as Cloud SQL run for you.
- **Theory:** Toy WAL is DB-10; this is the operator checklist.
- **GCP lens:** Lens-1: Cloud SQL backups & PITR (verify UI/flags). Lens-2: paper drill + BH-5.
- **Lab:** BH-5.
- **Check:** What evidence proves a backup is not just green in the console?

#### OD-05 · Replication & read-your-writes — stitch: DB-10 · primer SD-14
- [ ] done
- **Core:** Lag as SLI; sticky sessions / primary reads for RYW; failover caveats.
- **Theory:** Do not re-teach primer replication interviews — add SQL session consequences.
- **GCP lens:** Lens-1: Cloud SQL replicas. Lens-2: BH-5.
- **Lab:** BH-5.
- **Check:** Give one client pattern that restores read-your-writes with a stale replica.

#### OD-06 · Vacuum & bloat — stitch: DB-9
- [ ] done
- **Core:** MVCC leaves dead tuples; vacuum / autovacuum; bloat detection; xid wraparound vocabulary.
- **Theory:** Long transactions are vacuum poison.
- **GCP lens:** Lens-1: Cloud SQL metrics for deadlocks/vacuum. Lens-2: observe after SQL-E9.6 batching.
- **Lab:** TD-15.
- **Check:** Why does an open idle-in-transaction session block cleanup?

#### OD-07 · Retention & partitions — stitch: DD-10
- [ ] done
- **Core:** Drop old partitions vs mass DELETE; retention jobs; cold storage export.
- **Theory:** Partition pruning requires the partition key in the predicate; mass DELETE still writes WAL.
- **GCP lens:** Lens-1: BQ partition expiration as the analytics cousin. Lens-2: SCH-5 retention sketch.
- **Lab:** SCH-5.
- **Check:** Why is `DROP TABLE …_2024_01` preferable to `DELETE WHERE month=…`?

#### OD-08 · Migrations tooling & testing — stitch: A8 + C4 · C5
- [ ] done
- **Core:** Dirty state, advisory lock, expand/contract in CI, rollback story.
- **Theory:** Migrations and backfills are **jobs**: never part of a user request, never run on every container start. A **Cloud Run Job** (run to completion, one service account, bounded retries, a task timeout) runs `migrate up`; **Cloud Scheduler** can trigger a nightly job (its retry setting is not handler idempotency — both are needed); an advisory lock stops two executions racing; there is no public migrate URL. The job's service account cannot act as the API's service account, and the checkout path never opens a DDL connection.
- **Build lab `[local]`:** a local migrator. Ordered files (`001_init.sql`, `002_add_column.sql`, …), a `schema_migrations (version, dirty)` table, `up` and `down`, and a refusal to run while a version is dirty. Tests: running `up` twice is a no-op; a file that fails midway leaves its version dirty and blocks the next run; two concurrent runs serialise on the advisory lock. Then package the same migrations as a Cloud Run Job manifest (`[plan-only]` unless credits allow).
- **GCP lens:** Lens-1: Cloud Build job applying migrations. Lens-2: OD-10 CI fingerprint test.
- **Lab:** SQL-E9.6, SCH-4.
- **Check:** What does a migration advisory lock prevent?

#### OD-09 · Application data access — stitch: A7
- [ ] done
- **Core:** N+1, ORM dirty pages, prepared statements, transaction boundaries, keyset pagination SQL.
- **Theory:** the seek predicate, its index, and a from-scratch pager. Failure modes: an unstable sort (always end the key with a unique tiebreaker), internal IDs leaked without an authorisation check, and cursors that neither expire nor carry a signature. The seek is binary-search-shaped: state the invariant (every row before the cursor is already returned, every row after it is not) before writing it.
- **Build lab `[local]`:** a `cursorpage` package (Python, then Go once the Go Language Companion's GO-22 is taught, rule 0.4.9). Encode and decode an opaque, signed cursor over `(placed_at, order_id)`; run it against a fake ordered store searched by binary search, then against the lab's `customer_order`. Tests: forward pages; the empty result; a row deleted between two pages; a tampered cursor rejected. API shape: `GET /items?cursor=&limit=`.
- **GCP lens:** Lens-1: Cloud SQL + app connectors. Lens-2: PX-9 OFFSET vs keyset; BH-3.
- **Lab:** PX-9, BH-3, SQL-E4.7.
- **Check:** Write the keyset `WHERE` for `(placed_at, order_id)` descending.

#### OD-10 · Testing SQL — stitch: C4
- [ ] done
- **Core:** Postgres service container, seed v1, fingerprint assertions, migration up/down.
- **Theory:** Golden tests beat screenshot tests.
- **GCP lens:** Lens-1: Cloud Build running `lab.chk`. Lens-2: wire SQL-E3.2 as a CI test.
- **Lab:** SQL-E3.2 in CI.
- **Check:** What three lab pins must CI freeze for goldens to mean anything?

#### OD-11 · Cloud SQL: provisioning, connectivity, security, operations — stitch: V-STOR · B5 · B3 · C5
- [ ] done
- **Core (provisioning):** engine and major version; region and zone; machine tier (the smallest shared-core tier is the cheapest credits demo and is not HA `(verify)`); SSD vs HDD storage and automatic storage increase; automated backups, point-in-time recovery and the retained-backup count; maintenance window; database flags (`max_connections`, `work_mem`); deletion protection. **HA (regional):** a primary and a standby in a second zone; failover moves the instance to the standby; cost ≈ 2×. Read replicas are separate and asynchronous (OD-05).
- **Core (connectivity — the part people get wrong):** public IP with authorized networks is rejected for production. Use **private IP** in a VPC through private services access, reached from Cloud Run through Direct VPC egress (or the older Serverless VPC Access connector) and from GCE or GKE directly. The **Cloud SQL Auth Proxy** or a **language connector** (Python, Go, Java) wraps the connection in TLS and authorises it with IAM, so no database password has to sit in an environment variable. **IAM database authentication** makes IAM principals database users (SL-13 grants their privileges); built-in users remain for tools that cannot use IAM. Require TLS (`sslmode=require` or `verify-ca`).
- **Core (security):** one dedicated service account per workload; Secret Manager for any built-in password; authorized networks empty — never `0.0.0.0/0`; CMEK optional (cyber CR-14 owns the key hierarchy); Cloud SQL Admin audit logs for control-plane actions plus `pgAudit` for statement auditing.
- **Core (operations):** import and export through Cloud Storage (PQ-04 formats); the major-version upgrade path; Query Insights and the slow-query log (OD-02); connection pooling with an application pool or PgBouncer, sized with the OD-03 worksheet (Cloud Run max instances × pool size per instance against `max_connections`).
- **Theory:** RPO and RTO arithmetic for automated backups vs PITR vs HA (OD-04). HA is not a backup and a replica is not a backup: both copy a bad `DELETE` within seconds.
- **GCP lens:** Lens-1: `gcloud sql instances create` with no public IP and a VPC network `(verify flags)`. Lens-2: the labs below. Lens-3: Cloud SQL editions, and the exits to AlloyDB or Spanner (primer SD-25).
- **Lab `[local]` (required):** simulate the connector flow. The application reads only an instance connection name and asks one small factory function for a connection; in the lab the factory returns a connection to the Docker Postgres of §3, in production it calls the Cloud SQL connector with IAM authentication. The application code does not change between the two. Then fill the OD-03 worksheet for the check below.
- **Lab `[credit ~$X]` (optional; destroy the same day):** with Terraform (TF-DB1), a PostgreSQL instance on private IP; connect from a Cloud Run service or an e2-micro VM through the connector with IAM database authentication; run the OD-08 migration job; take an on-demand backup; if the instance is HA, trigger a failover and time it; `terraform destroy`.
- **Terraform LLD (deliverable):** `google_sql_database_instance` (private IP, deletion protection, backup configuration, insights configuration), `google_sql_database`, `google_sql_user` (IAM type), and `google_service_networking_connection` for private services access. TF-DB1 (§8.2) is the exercise; primer TF-2 draws the same private-IP pattern at system level.
- **Check:** A Cloud Run service with max 20 instances and a pool of 10 connections per instance points at an instance with `max_connections = 100`. What fails first as traffic grows, and name two fixes.

### 4.7 Analytics & other engines (AN-01 … AN-07)

#### AN-01 · OLTP vs OLAP; star/snowflake — stitch: A8 + V-STOR
- [ ] done
- **Core:** Workload shapes; fact/dim; grain; conformed dimensions.
- **Theory:** the OLTP lab schema vs analytics copies.
- **GCP lens:** Lens-1: Cloud SQL vs BigQuery decision table (A8 + V-STOR). Lens-2: SQL-E13.3 star build.
- **Lab:** SQL-E13.3; DT-1.
- **Check:** What is the grain of `order_line` vs `customer_order`?

#### AN-02 · BigQuery / GoogleSQL cost shapes — stitch: V-STOR · V-DATA
- [ ] done
- **Core:** Partition + cluster; selective column projection; bytes scanned as cost.
- **Theory:** BigQuery operations as well as SQL-level reading: datasets; partition by date and cluster by `tenant_id`; require a partition filter; on-demand bytes vs slot reservations; an authorized view for an analyst service account. The free tier (1 TiB of queries and 10 GiB of storage per month `(verify)`) is the primary free analytics lab. BigQuery never serves the checkout path.
- **Build lab `[free-tier]`:** first run the query locally on the lab data: daily GMV by tenant from `customer_order`. Then batch-load the same rows into a date-partitioned, tenant-clustered BigQuery table, run the query with and without the partition filter, and record the dry-run bytes for each.
- **GCP lens:** Lens-1: dry-run bytes. Lens-2: DT-2, SQL-E13.1.
- **Lab:** DT-2–DT-4.
- **Check:** Name two SQL mistakes that explode bytes scanned.

#### AN-03 · Cohorts, funnels, sessionisation, retention — stitch: V-DATA · B4
- [ ] done
- **Core:** Windowed event math; billing-export-shaped windows reuse.
- **Theory:** Cohort month = trunc(signup); activation window is a half-open interval — same trap as SQL-E1.1.
- **GCP lens:** Lens-1: BQ SQL. Lens-2: SQL-E6.2, SQL-E6.6.
- **Lab:** SQL-E6.2, SQL-E6.6, DT-4.
- **Check:** Define activation as 'purchase within 7 days of signup' in SQL words.

#### AN-04 · Approximate aggregation — stitch: V-DATA
- [ ] done
- **Core:** `HLL`, t-digest / quantile sketches — error bars are part of the answer.
- **Theory:** Bias/variance trade-off; never mix approx and exact in one KPI without labelling.
- **GCP lens:** Lens-1: BQ `APPROX_COUNT_DISTINCT`. Lens-2: DT-5.
- **Lab:** DT-5.
- **Check:** When is a 2% count error unacceptable?

#### AN-05 · Spanner SQL dialect map — stitch: A9 + V-STOR
- [ ] done
- **Core:** GoogleSQL in Spanner: types, interleaved joins, no arbitrary cross-DB features.
- **Theory:** Same *question* as Postgres — different spelling and limits.
- **GCP lens:** Lens-1: Spanner emulator when Lab Reality allows. Lens-2: DT-6.
- **Lab:** DT-6.
- **Check:** Name two Postgres features you must rewrite for Spanner.

#### AN-06 · NoSQL query models vs SQL — stitch: A8 + V-STOR
- [ ] done
- **Core:** Document / KV access patterns; what joins become application fan-out.
- **Theory:** Firestore when it wins/loses — primer SD-22 owns the product; here the same-question drill, with the two rules it depends on: a server using the Admin SDK bypasses security rules, so tenant and role checks live in server code; and while carts live in Firestore and orders in SQL, the handoff goes through an outbox (SL-10), never a dual write.
- **GCP lens:** Lens-1: Firestore. Lens-2: DT-7.
- **Lab:** DT-7.
- **Check:** Express 'top 10 products by GMV for tenant 2' as a document access plan and as SQL.

#### AN-07 · Search & vectors in SQL — stitch: D4
- [ ] done
- **Core:** `tsvector`/`tsquery`; `pgvector` similarity — vs dedicated search engines.
- **Theory:** Ranking quality, hybrid lexical+vector, and operational isolation from OLTP.
- **GCP lens:** Lens-1: Vertex matching vs in-DB vectors (trade-offs). Lens-2: DT-8 sketch.
- **Lab:** DT-8.
- **Check:** When does in-DB vector search stop being enough?
## 5. Skip tests / readiness tiers (SQL-SKIP-SQL / SQL-SKIP-ENGINE)

Mapped to the A8 skip-tests **SQL-SKIP-SQL** / **SQL-SKIP-ENGINE**. If the A8 sessions already confirmed the skill, **stamp and skip**; else run the order in §2.2.

### 5.1 Tier map

| Tier | Ready for… | Evidence to stamp | If missing, run |
|---|---|---|---|
| **SQL-SKIP-SQL-A** Foundations | FDs, keys, 3NF talk-through | TD-1, TD-3 | RT-01, RT-04, RT-05 |
| **SQL-SKIP-SQL-B** Algebra ↔ SQL | Multiplicity + NULL predictions | SQL-E1.3, SQL-E3.2, SQL-E3.5 | RT-02, SL-03, SL-04 |
| **SQL-SKIP-SQL-C** Aggregation & subqueries | Clean GROUP BY + EXISTS | SQL-E2.5, SQL-E4.5 | SL-05, SL-06 |
| **SQL-SKIP-SQL-D** Windows & recursion | Frame + termination | SQL-E5.4, SQL-E7.3 | SL-08, SL-09 |
| **SQL-SKIP-SQL-E** Transactions & app access | Isolation + upsert + keyset | TX-2, SQL-E9.3, SQL-E4.7 | CS-05, SL-10, OD-09 |
| **SQL-SKIP-ENGINE-A** Storage/index math | Page napkin + height | SQL-Z0.8, TD-10 | CS-01, CS-02 |
| **SQL-SKIP-ENGINE-B** Executor/planner | Join/spill/stats predictions | PX-7, PX-8, PX-10 | CS-03, CS-08 |
| **SQL-SKIP-ENGINE-C** MVCC/WAL | Schedule + durability paragraph | TD-9, TD-12 + OD-04 outline | CS-05, CS-06, OD-06 |

### 5.2 Official skip-test checkpoints (from §2 stitch table)
- **SQL-SKIP-SQL:** SQL-E3.2, SQL-E4.5, SQL-E5.4, SQL-E9.3, TX-2 (if the A8 sessions confirmed FDs/joins/transactions/pagination/client hygiene).
- **SQL-SKIP-ENGINE:** PX-1…PX-11 residual EXPLAIN drills; TD-12 + OD-04 for crash/recovery evidence.

### 5.3 Readiness before exercise levels
Use §6 prereq gates. Never issue E_n if the gate names unanchored vocabulary — postpone or teach first (Prop Lock).

## 6. Query-creation exercise bank (levels 0–14)

**Gates** are stated once per level, under its heading; a card's stitch partners are the §2 rows its tags name. **Bank ≠ dump** (rule 0.4.11): issue **one** item at the ledger rung; learner attempts; escalate hints; only then Appendix K. Every read-only golden below is from `goldens_ex_*.json` executed on PostgreSQL 15.8 / seed v1 / UTC / C collation.

### 6.0 Level 0 — paper drills (SQL-Z0.*)

No database. Predict on paper; then optionally confirm later. Gate: PQ modules as tagged.

#### SQL-Z0.1 · Bag vs set multiplicity
- **Tags:** PQ-01
- **Prompt:** On paper: relation R={1,1,2} as a bag. Compute R ∪ R, R ∪_set R, π(R).
- **Output shape:** multiplicity table
- **Trap:** Calling SQL UNION without noticing it is set-union.
- **Golden fingerprint:** _(paper — no `lab.chk`)_

#### SQL-Z0.2 · Join cardinality bound
- **Tags:** PQ-01·RT-01
- **Prompt:** R has 4 rows, S has 6, join key has 2 distinct values with skew 3/1 on R and 4/2 on S. Bound |R⋈S|.
- **Output shape:** integer bound + sketch
- **Trap:** Using |R|·|S| as the *answer* rather than the upper bound.
- **Golden fingerprint:** _(paper — no `lab.chk`)_

#### SQL-Z0.3 · Function vs relation
- **Tags:** PQ-01
- **Prompt:** Is `email → user_id` a function on lab UNIQUE(tenant_id,email)? Explain.
- **Output shape:** one paragraph
- **Trap:** Forgetting the tenant is part of the key.
- **Golden fingerprint:** _(paper — no `lab.chk`)_

#### SQL-Z0.4 · 3VL truth table
- **Tags:** PQ-02·SL-03
- **Prompt:** Fill TRUE/FALSE/UNKNOWN for `country = 'US'`, `country <> 'US'`, `NOT (country = 'US')` when country is NULL.
- **Output shape:** 3×3 table
- **Trap:** Treating UNKNOWN as FALSE.
- **Golden fingerprint:** _(paper — no `lab.chk`)_

#### SQL-Z0.5 · Counting distinct pairs
- **Tags:** PQ-01
- **Prompt:** How many ordered pairs (user, product) if 2000 users and 500 products? How many if each user orders ≤4 products (lab-ish)?
- **Output shape:** two integers
- **Trap:** Confusing domain product with observed fact table size.
- **Golden fingerprint:** _(paper — no `lab.chk`)_

#### SQL-Z0.6 · Predicate safety
- **Tags:** PQ-02
- **Prompt:** Which of `{x | x=x}`, `{x | ∃y R(x,y)}` are safe? Why?
- **Output shape:** safe/unsafe labels
- **Trap:** Equating 'true of everything' with a finite SQL result.
- **Golden fingerprint:** _(paper — no `lab.chk`)_

#### SQL-Z0.7 · Binary search steps
- **Tags:** PQ-07
- **Prompt:** Sorted 1e6 keys, fan-out 1 (binary search). Approx comparisons? Then fan-out 100 B-tree height?
- **Output shape:** two numbers
- **Trap:** Using ln vs log2 casually without stating base.
- **Golden fingerprint:** _(paper — no `lab.chk`)_

#### SQL-Z0.8 · Pages napkin
- **Tags:** PQ-08·CS-01
- **Prompt:** 20k orders × 150 B/row, 8 KiB pages, 90% fill. Approx pages? Compare to 1 RAM GB.
- **Output shape:** pages + fit/not
- **Trap:** Forgetting fill-factor.
- **Golden fingerprint:** _(paper — no `lab.chk`)_

### 6.0b Theory drills (TD-1 … TD-16)

Issued one at a time with the A8 + A9 theory and the §4.0 slices. Keys in Appendix K (sketches).

#### TD-1 · Keys from FDs
- **Tags:** RT-04
- **Prompt:** Given FDs on Orders: order_id→tenant_id,user_id,placed_at; tenant_id,idem→order_id (when idem not null). List candidate keys.
- **Output shape:** key list
- **Trap:** answering with product lore instead of the formal object
- **Golden fingerprint:** _(paper)_
- **Prereq gate:** stitch partners in §2 unlocked

#### TD-2 · Push σ through ⋈
- **Tags:** RT-02·RT-08
- **Prompt:** Rewrite σ_{tenant=2}(Orders⋈Users) two ways; state when they differ with outer joins.
- **Output shape:** two algebra trees
- **Trap:** answering with product lore instead of the formal object
- **Golden fingerprint:** _(paper)_
- **Prereq gate:** stitch partners in §2 unlocked

#### TD-3 · 3NF decomposition
- **Tags:** RT-05
- **Prompt:** Decompose Product(tenant,sku,price,currency) with tenant→currency into 3NF; check lossless.
- **Output shape:** tables + proof sketch
- **Trap:** answering with product lore instead of the formal object
- **Golden fingerprint:** _(paper)_
- **Prereq gate:** stitch partners in §2 unlocked

#### TD-4 · BCNF violation
- **Tags:** RT-05
- **Prompt:** Exhibit a BCNF violation that is still 3NF; say what breaks if you decompose.
- **Output shape:** example
- **Trap:** answering with product lore instead of the formal object
- **Golden fingerprint:** _(paper)_
- **Prereq gate:** stitch partners in §2 unlocked

#### TD-5 · Bag projection
- **Tags:** RT-02
- **Prompt:** Show π_A on a bag with duplicates; contrast set projection.
- **Output shape:** counts
- **Trap:** answering with product lore instead of the formal object
- **Golden fingerprint:** _(paper)_
- **Prereq gate:** stitch partners in §2 unlocked

#### TD-6 · Equivalence laws
- **Tags:** RT-02
- **Prompt:** Prove or refute: σ_p(R∪S)=σ_p(R)∪σ_p(S) for bags.
- **Output shape:** proof/counterexample
- **Trap:** answering with product lore instead of the formal object
- **Golden fingerprint:** _(paper)_
- **Prereq gate:** stitch partners in §2 unlocked

#### TD-7 · Outer-join rewrite illegality
- **Tags:** RT-08
- **Prompt:** Give a counterexample where placing a right-side filter in WHERE vs ON changes meaning.
- **Output shape:** instance + two results
- **Trap:** answering with product lore instead of the formal object
- **Golden fingerprint:** _(paper)_
- **Prereq gate:** stitch partners in §2 unlocked

#### TD-8 · Dirty read & lost update schedules
- **Tags:** CS-05
- **Prompt:** Draw two schedules; mark anomalies; say which Postgres isolation levels forbid them.
- **Output shape:** schedules
- **Trap:** answering with product lore instead of the formal object
- **Golden fingerprint:** _(paper)_
- **Prereq gate:** stitch partners in §2 unlocked

#### TD-9 · Snapshot visibility
- **Tags:** CS-05
- **Prompt:** Given begin/commit timestamps of writers W1,W2 and reader R, which version does R see under SI?
- **Output shape:** version id + reason
- **Trap:** answering with product lore instead of the formal object
- **Golden fingerprint:** _(paper)_
- **Prereq gate:** stitch partners in §2 unlocked

#### TD-10 · B-tree height
- **Tags:** CS-02
- **Prompt:** Fan-out 200, 40e6 leaf entries. Height? Compare to hash probe cost qualitatively.
- **Output shape:** height
- **Trap:** answering with product lore instead of the formal object
- **Golden fingerprint:** _(paper)_
- **Prereq gate:** stitch partners in §2 unlocked

#### TD-11 · Hash join I/O
- **Tags:** CS-03
- **Prompt:** Build side 8 GB, work_mem 256 MB, probe 40 GB. Sketch partitions and I/O order-of-magnitude.
- **Output shape:** napkin
- **Trap:** answering with product lore instead of the formal object
- **Golden fingerprint:** _(paper)_
- **Prereq gate:** stitch partners in §2 unlocked

#### TD-12 · WAL durability
- **Tags:** CS-06
- **Prompt:** Steal/no-force: after crash mid-checkpoint, what must redo vs undo? One paragraph.
- **Output shape:** paragraph
- **Trap:** answering with product lore instead of the formal object
- **Golden fingerprint:** _(paper)_
- **Prereq gate:** stitch partners in §2 unlocked

#### TD-13 · Selectivity estimate
- **Tags:** CS-08
- **Prompt:** Histogram bucket for status='created' is 5% but real is 1%. How might join order flip?
- **Output shape:** scenario
- **Trap:** answering with product lore instead of the formal object
- **Golden fingerprint:** _(paper)_
- **Prereq gate:** stitch partners in §2 unlocked

#### TD-14 · 2PC vs outbox
- **Tags:** CS-07
- **Prompt:** List one availability failure of 2PC that outbox+pubsub survives.
- **Output shape:** bullet
- **Trap:** answering with product lore instead of the formal object
- **Golden fingerprint:** _(paper)_
- **Prereq gate:** stitch partners in §2 unlocked

#### TD-15 · Vacuum vs long tx
- **Tags:** OD-06·CS-05
- **Prompt:** Explain why a 2h idle-in-transaction session causes table bloat under churn.
- **Output shape:** causal chain
- **Trap:** answering with product lore instead of the formal object
- **Golden fingerprint:** _(paper)_
- **Prereq gate:** stitch partners in §2 unlocked

#### TD-16 · Recursion termination
- **Tags:** CS-11·SL-09
- **Prompt:** Write a recursive CTE pattern that detects cycles with a path array; state the stop condition.
- **Output shape:** SQL sketch
- **Trap:** answering with product lore instead of the formal object
- **Golden fingerprint:** _(paper)_
- **Prereq gate:** stitch partners in §2 unlocked


### 6.1 Level 1 — SELECT, filter, NULL, CASE

**Prereq gate:** SL-01, SL-02, SL-03 unlocked; lab fingerprints match (§3)

#### SQL-E1.1 · Q2-2024 signups from GB or DE
- **Tags:** WHERE · half-open ranges
- **Prompt:** Users whose country is GB or DE and who were created in the second quarter of 2024 (April, May and June, UTC).
- **Output shape:** `user_id, email` (order-insensitive — `lab.chk`)
- **Trap:** `BETWEEN '2024-04-01' AND '2024-06-30'` silently drops most of 30 June for a `timestamptz`. Use `>= start AND < next_start`. Wrong-path fingerprint (do not chase): `162:c85bda05` — BETWEEN with the last calendar day.
- **Golden fingerprint:** `164:d17041f6`

#### SQL-E1.2 · Unknown country
- **Tags:** NULL · IS NULL
- **Prompt:** Users whose country is unknown (stored as NULL).
- **Output shape:** `user_id` (order-insensitive — `lab.chk`)
- **Trap:** `country = NULL` is never true — it is UNKNOWN. Also note `char(2)` pads; do not compare with `''`.
- **Golden fingerprint:** `181:ab2f2d8e`

#### SQL-E1.3 · Everyone not known to be in the US
- **Tags:** NULL · 3VL · IS DISTINCT FROM
- **Prompt:** All users who are not known to be in the US — this **includes** users whose country is unknown.
- **Output shape:** `user_id` (order-insensitive — `lab.chk`)
- **Trap:** `country <> 'US'` drops the NULL-country users (UNKNOWN is not TRUE). Use `IS DISTINCT FROM`, or `country <> 'US' OR country IS NULL`. Write the 3VL truth table for `NOT (country = 'US')` first. Wrong-path fingerprint (do not chase): `1559:c2797d13` — `<>` instead of IS DISTINCT FROM.
- **Golden fingerprint:** `1740:d7106dd7`

#### SQL-E1.4 · Mid-priced live catalogue, top 20
- **Tags:** WHERE · ORDER BY · LIMIT · determinism
- **Prompt:** Products with `price_minor` from 1000 to 2000 inclusive that are not discontinued, most expensive first, ties broken by lowest `product_id`; first 20 rows only.
- **Output shape:** `product_id, price_minor` (ordered) (ordered — use `lab.chk_o`)
- **Trap:** `LIMIT` without a total order is non-deterministic. `discontinued_at IS NULL`, not `= NULL`. Both bounds are inclusive here (integer money, so `BETWEEN` is safe).
- **Golden fingerprint:** `20:1af04ff2`

#### SQL-E1.5 · Reviews with no text
- **Tags:** NULL vs empty string · COALESCE
- **Prompt:** Reviews whose body is missing — treat NULL and the empty string as the same thing.
- **Output shape:** `review_id` (order-insensitive — `lab.chk`)
- **Trap:** NULL and `''` are different values; a test for one silently misses the other. In Oracle they collapse into one — a dialect trap (see the Rosetta table).
- **Golden fingerprint:** `2036:aa6dda6b`

#### SQL-E1.6 · Order status buckets
- **Tags:** CASE · expressions
- **Prompt:** Label every order: `open` for created/paid, `done` for fulfilled, `closed` for cancelled/refunded.
- **Output shape:** `order_id, bucket` (order-insensitive — `lab.chk`)
- **Trap:** A `CASE` without `ELSE` yields NULL for unmatched values — add a defensive `ELSE 'unknown'` and say why it should never fire (the `CHECK` constraint).
- **Golden fingerprint:** `20000:a58f4910`

#### SQL-E1.7 · Ten priciest live products
- **Tags:** ORDER BY · LIMIT · tie-break
- **Prompt:** The ten most expensive products that are not discontinued (ties → lowest `product_id`).
- **Output shape:** `product_id, price_minor` (ordered) (ordered — use `lab.chk_o`)
- **Trap:** Sorting by price alone and hoping. State the tie-break in the spec *before* you write the query.
- **Golden fingerprint:** `10:558e94b1`

#### SQL-E1.8 · Pattern search
- **Tags:** LIKE · ILIKE · escaping
- **Prompt:** Products whose SKU starts with `SKU-01` and ends with `7`.
- **Output shape:** `product_id` (order-insensitive — `lab.chk`)
- **Trap:** `_` and `%` are wildcards — to match a literal underscore you need `ESCAPE`. A leading-wildcard pattern (`'%7'`) cannot use a B-tree index (see the PX-3 prediction card).
- **Golden fingerprint:** `10:986cf4ec`

### 6.2 Level 2 — Aggregation

**Prereq gate:** SQL-E1 gate passed; SL-05

#### SQL-E2.1 · Orders and revenue by status
- **Tags:** GROUP BY · SUM
- **Prompt:** For each order status: number of orders and the sum of `total_minor`.
- **Output shape:** `status, n_orders, sum_minor` (order-insensitive — `lab.chk`)
- **Trap:** Every non-aggregated SELECT column must be in GROUP BY (or functionally dependent on the PK). Money is an integer of minor units — never `float`.
- **Golden fingerprint:** `5:2495a69d`

#### SQL-E2.2 · Monthly fulfilled GMV, 2025
- **Tags:** date_trunc · GROUP BY · time zones
- **Prompt:** For fulfilled orders placed in calendar 2025 (UTC): month start, order count, and GMV (`sum(total_minor)`).
- **Output shape:** `month, n_orders, gmv_minor` (order-insensitive — `lab.chk`)
- **Trap:** `date_trunc('month', timestamptz)` uses the **session** time zone. The lab pins `UTC`; production rarely does — always state the zone.
- **Golden fingerprint:** `12:c6eb674e`

#### SQL-E2.3 · Well-reviewed products
- **Tags:** HAVING · WHERE vs HAVING · ROUND
- **Prompt:** Products with at least 10 reviews: review count and average rating rounded to 2 decimals.
- **Output shape:** `product_id, n, avg_rating` (order-insensitive — `lab.chk`)
- **Trap:** `WHERE` filters rows *before* grouping, `HAVING` filters groups *after*. `avg(smallint)` is `numeric`, so `round(avg(rating), 2)` works; in engines with integer division check the type.
- **Golden fingerprint:** `467:68a601d1`

#### SQL-E2.4 · Buyers per tenant
- **Tags:** COUNT(DISTINCT) · count(*) vs count(col)
- **Prompt:** Per tenant: number of orders and number of *distinct* users who placed at least one order.
- **Output shape:** `tenant_id, n_orders, n_buyers` (order-insensitive — `lab.chk`)
- **Trap:** `count(*)` counts rows, `count(col)` skips NULLs, `count(DISTINCT col)` de-duplicates. Say which one each output column needs.
- **Golden fingerprint:** `5:0cf3aaa2`

#### SQL-E2.5 · Refund rate by tenant
- **Tags:** FILTER · conditional aggregation · integer division
- **Prompt:** Per tenant: total orders, refunded orders, and refund rate = refunded / total rounded to 4 decimals.
- **Output shape:** `tenant_id, n_orders, n_refunded, refund_rate` (order-insensitive — `lab.chk`)
- **Trap:** `1/3` in integer arithmetic is 0. Cast one side to `numeric` *before* dividing. `count(*) FILTER (WHERE …)` is the standard-SQL way; `SUM(CASE …)` is the portable way. Wrong-path fingerprint (do not chase): `5:b83b6ee2` — integer division.
- **Golden fingerprint:** `5:9fbfe463`

#### SQL-E2.6 · Users by country including unknown
- **Tags:** GROUP BY NULL · COALESCE
- **Prompt:** Number of users per country; label unknown as `'??'`.
- **Output shape:** `country, n` (order-insensitive — `lab.chk`)
- **Trap:** GROUP BY puts all NULLs in **one** group (unlike `=`). `country` is `char(2)` so `'US'` and `'US '` compare equal — but `coalesce(country,'??')` must be a valid `char(2)`.
- **Golden fingerprint:** `8:94127f65`

#### SQL-E2.7 · Median order value per tenant
- **Tags:** ordered-set aggregates · percentile_disc
- **Prompt:** Per tenant, the median `total_minor` of fulfilled orders, defined as `percentile_disc(0.5)` (an actual value from the data).
- **Output shape:** `tenant_id, median_minor` (order-insensitive — `lab.chk`)
- **Trap:** `avg` is not the median. `percentile_cont` interpolates and returns `double precision` — a float in a money pipeline. State which definition you use.
- **Golden fingerprint:** `5:74a001bd`

#### SQL-E2.8 · Price histogram
- **Tags:** bucketing · integer division
- **Prompt:** Bucket **live** products (not discontinued) into price bands of width 1000 minor units: band start (0, 1000, 2000, …) and product count.
- **Output shape:** `band_start, n` (order-insensitive — `lab.chk`)
- **Trap:** `price_minor / 1000 * 1000` relies on integer division truncation — fine in Postgres, wrong in engines that return decimals (dialect trap). `width_bucket` is the explicit alternative.
- **Golden fingerprint:** `10:dc13b2c1`

### 6.3 Level 3 — Joins

**Prereq gate:** SQL-E2 gate; SL-04

#### SQL-E3.1 · Paid orders with buyer and tenant
- **Tags:** INNER JOIN · multi-table
- **Prompt:** Orders with status `paid` placed in March 2025, tenant 2: order id, buyer email, tenant name, total.
- **Output shape:** `order_id, email, tenant_name, total_minor` (order-insensitive — `lab.chk`)
- **Trap:** Filter on the *driving* table in WHERE; join keys go in ON. Three tables, two ON clauses — write the join graph as a picture first.
- **Golden fingerprint:** `50:787a0b9d`

#### SQL-E3.2 · Users who never referred anyone
- **Tags:** anti-join · NOT IN + NULL trap
- **Prompt:** Users who are not the referrer of any other user.
- **Output shape:** `user_id` (order-insensitive — `lab.chk`)
- **Trap:** `WHERE user_id NOT IN (SELECT referred_by FROM app_user)` returns **zero rows** because `referred_by` contains NULLs (`x NOT IN (…, NULL)` is never TRUE). Write it three ways: NOT EXISTS, LEFT JOIN … IS NULL, and NOT IN with a NULL filter — all three must give the same fingerprint. Wrong-path fingerprint (do not chase): `0:d41d8cd9` — NOT IN over a column containing NULL.
- **Golden fingerprint:** `1291:ce8f0411`

#### SQL-E3.3 · Users who never ordered
- **Tags:** LEFT JOIN … IS NULL · anti-join
- **Prompt:** Users with no order at all (any status).
- **Output shape:** `user_id` (order-insensitive — `lab.chk`)
- **Trap:** Test the *right-hand primary key* for NULL, not a column that can legitimately be NULL on the right.
- **Golden fingerprint:** `200:e5ab3ae1`

#### SQL-E3.4 · Products not sold in a week
- **Tags:** anti-join · date ranges
- **Prompt:** Products that appear on **no** order line of a fulfilled order placed during 2025-01-01 … 2025-01-07 (inclusive, UTC).
- **Output shape:** `product_id` (order-insensitive — `lab.chk`)
- **Trap:** Where does the date filter go? Inside the `NOT EXISTS` subquery (or the `ON` of the LEFT JOIN) — not in the outer WHERE, where it would turn the anti-join into an inner join.
- **Golden fingerprint:** `180:d18c224e`

#### SQL-E3.5 · Revenue of delivered orders
- **Tags:** semi-join · fan-out trap
- **Prompt:** Total `total_minor` of fulfilled orders that have **at least one** delivered shipment (`delivered_at IS NOT NULL`). One number.
- **Output shape:** `revenue_minor` (order-insensitive — `lab.chk`)
- **Trap:** `JOIN shipment` fans out: orders with two shipments are counted twice. Semi-join (`EXISTS`) never multiplies rows. Compute the naive join answer too and explain the difference in one sentence. Wrong-path fingerprint (do not chase): `1:20e027c7` — plain JOIN fans out orders with two shipments.
- **Golden fingerprint:** `1:6c39466d`

#### SQL-E3.6 · Cross-tenant referrals
- **Tags:** self-join · data-quality find
- **Prompt:** Users whose referrer belongs to a **different tenant**. This is a multi-tenancy integrity leak, not a feature.
- **Output shape:** `user_id, referrer_id` (order-insensitive — `lab.chk`)
- **Trap:** Alias the same table twice (`u`, `r`) and name the join direction aloud. Then: which constraint would have prevented this? (A composite FK `(tenant_id, referred_by) → (tenant_id, user_id)`.)
- **Golden fingerprint:** `1172:9f8ebbd0`

#### SQL-E3.7 · One-star counts including zeros
- **Tags:** LEFT JOIN · filter in ON · empty groups
- **Prompt:** For **every** product of tenant 1 (all of them), the number of 1-star reviews it has — 0 where none.
- **Output shape:** `product_id, one_star` (order-insensitive — `lab.chk`)
- **Trap:** `LEFT JOIN review r … WHERE r.rating = 1` deletes the zero rows (the WHERE re-filters the NULL-extended rows). Put the predicate in `ON`, or use `count(*) FILTER`. `count(r.review_id)`, not `count(*)`. Wrong-path fingerprint (do not chase): `98:43c02740` — rating filter in WHERE after the LEFT JOIN.
- **Golden fingerprint:** `100:1b05fa94`

#### SQL-E3.8 · Who ordered vs who reviewed (Q1 2025)
- **Tags:** FULL OUTER JOIN · reconciliation
- **Prompt:** For 2025 Q1 (Jan–Mar UTC): every user who placed **or** reviewed, with two booleans — did they order, did they review.
- **Output shape:** `user_id, ordered, reviewed` (order-insensitive — `lab.chk`)
- **Trap:** `COALESCE` the two join keys; a FULL JOIN yields NULL on the missing side. Pre-aggregate each side to one row per user *before* joining.
- **Golden fingerprint:** `1845:6f7a9372`

#### SQL-E3.9 · Deletions per month with zero-fill
- **Tags:** calendar spine · generate_series · LEFT JOIN
- **Prompt:** For every month from 2024-05 through 2025-06 (inclusive, 14 rows), the number of users deleted (`deleted_at`) in that month — including months with zero.
- **Output shape:** `month, n_deleted` (order-insensitive — `lab.chk`)
- **Trap:** Group the fact table alone and empty months vanish. Generate the spine first (`generate_series`), then LEFT JOIN facts onto it.
- **Golden fingerprint:** `14:cb9ff4e8`

#### SQL-E3.10 · Duplicate-safe reviewers per product
- **Tags:** multiplicity · DISTINCT vs GROUP BY
- **Prompt:** Per product: distinct reviewers and total reviews, only products where those two numbers differ.
- **Output shape:** `product_id, n_reviewers, n_reviews` (order-insensitive — `lab.chk`)
- **Trap:** A user may review the same product several times in this seed (see SQL-E9.4). `count(*)` ≠ `count(DISTINCT user_id)` exactly there.
- **Golden fingerprint:** `241:47e3b13f`

### 6.4 Level 4 — Subqueries, CTEs, set ops

**Prereq gate:** SQL-E3 gate; SL-06, SL-07

#### SQL-E4.1 · Above-average spenders
- **Tags:** scalar subquery · CTE
- **Prompt:** Users whose total fulfilled spend is strictly greater than the average spend **across users who spent anything** (exclude users with no fulfilled orders from the average).
- **Output shape:** `user_id, spend_minor` (order-insensitive — `lab.chk`)
- **Trap:** What is the denominator? Users with zero orders shift the average if you `LEFT JOIN` them in. Write down which population you average over.
- **Golden fingerprint:** `675:19348832`

#### SQL-E4.2 · Latest review rating per product
- **Tags:** correlated subquery · DISTINCT ON
- **Prompt:** For each product that has reviews: the rating of its most recent review (newest `created_at`; ties → highest `review_id`).
- **Output shape:** `product_id, rating` (order-insensitive — `lab.chk`)
- **Trap:** `max(created_at)` alone does not give you the rating from that row. Use a correlated subquery, `DISTINCT ON`, or a window (SQL-E5.4) — then prove they agree.
- **Golden fingerprint:** `500:7463fec9`

#### SQL-E4.3 · Both fulfilled and refunded
- **Tags:** EXISTS · INTERSECT
- **Prompt:** Users who have at least one fulfilled order **and** at least one refunded order.
- **Output shape:** `user_id` (order-insensitive — `lab.chk`)
- **Trap:** Two `EXISTS` clauses (or `INTERSECT`). A single `JOIN` with `status IN ('fulfilled','refunded')` finds users with *either*.
- **Golden fingerprint:** `391:6319def9`

#### SQL-E4.4 · Reviewed but never bought
- **Tags:** EXCEPT · NOT EXISTS · set semantics
- **Prompt:** Distinct `(user_id, product_id)` pairs where the user reviewed the product but has **no** order line for it (in any of their orders, any status).
- **Output shape:** `user_id, product_id` (order-insensitive — `lab.chk`)
- **Trap:** `EXCEPT` removes duplicates and needs identical column lists; `EXCEPT ALL` is the bag version. Solve with both `EXCEPT` and `NOT EXISTS`.
- **Golden fingerprint:** `4559:2e92d1fa`

#### SQL-E4.5 · Net revenue per tenant without double counting
- **Tags:** CTE · pre-aggregation · fan-out
- **Prompt:** Per tenant: GMV of fulfilled and refunded orders placed in 2025 (`sum(total_minor)`), sum of **succeeded refund** payments on those orders, and net = gmv − refunds.
- **Output shape:** `tenant_id, gmv_minor, refunded_minor, net_minor` (order-insensitive — `lab.chk`)
- **Trap:** orders → payments is 1:N. Joining orders to payments and summing `total_minor` counts each order once per payment row. Aggregate each side **separately in CTEs**, then join on the key. Wrong-path fingerprint (do not chase): `5:45fe10e3` — orders JOIN payments then SUM(total_minor).
- **Golden fingerprint:** `5:77344493`

#### SQL-E4.6 · Strictly the priciest in its category
- **Tags:** ALL · empty-set trap
- **Prompt:** Products strictly more expensive than every *other* product in the same category. Uncategorised products (NULL category) are excluded.
- **Output shape:** `product_id` (order-insensitive — `lab.chk`)
- **Trap:** `x > ALL (empty set)` is TRUE. For a NULL category the peer set is empty, so every uncategorised product qualifies unless you exclude them explicitly. Also: ties give no winner. Wrong-path fingerprint (do not chase): `68:6cff1edf` — forgetting that ALL over an empty set is TRUE.
- **Golden fingerprint:** `30:d5ca9e54`

#### SQL-E4.7 · Latest order per user (tenant 3)
- **Tags:** LATERAL · top-1 per group
- **Prompt:** For each user of tenant 3 who has orders: their most recent order (`placed_at DESC`, tie → higher `order_id`).
- **Output shape:** `user_id, order_id, placed_at` (order-insensitive — `lab.chk`)
- **Trap:** `LATERAL` runs the subquery once per outer row and can reference it — the SQL for-each loop. Missing index on `(user_id, placed_at)` makes it a seq scan per user (PX-1).
- **Golden fingerprint:** `360:3dd4aace`

#### SQL-E4.8 · Relational division: bought all three
- **Tags:** division · GROUP BY / HAVING · double NOT EXISTS
- **Prompt:** Users who have ordered **all** of products 1, 6 and 11 (any status).
- **Output shape:** `user_id` (order-insensitive — `lab.chk`)
- **Trap:** Division has two standard forms: `HAVING count(DISTINCT product_id) = 3` (fast, needs the count) and double `NOT EXISTS` (works for a *set stored in a table*). Write both.
- **Golden fingerprint:** `5:286c82f6`

### 6.5 Level 5 — Window functions

**Prereq gate:** SQL-E4 gate; SL-08

#### SQL-E5.1 · Top-3 price ranks per category
- **Tags:** dense_rank · rank vs row_number
- **Prompt:** For every category (ignore uncategorised products): products whose **dense** price rank (highest price = 1) is 1, 2 or 3 within the category.
- **Output shape:** `category_id, product_id, price_minor, rnk` (order-insensitive — `lab.chk`)
- **Trap:** `rank` leaves gaps after ties, `dense_rank` doesn't, `row_number` breaks ties arbitrarily. You cannot filter on a window function in WHERE — wrap in a subquery/CTE.
- **Golden fingerprint:** `90:0444fd32`

#### SQL-E5.2 · Running GMV, tenant 1, March 2025
- **Tags:** running total · frame · aggregate then window
- **Prompt:** Tenant 1, fulfilled orders placed in March 2025: per UTC day the GMV, plus the cumulative GMV since 1 March.
- **Output shape:** `day, gmv_minor, cum_gmv_minor` (ordered by day) (ordered — use `lab.chk_o`)
- **Trap:** Aggregate to days **first** (CTE), then window over the days. The default frame with `ORDER BY` is `RANGE UNBOUNDED PRECEDING … CURRENT ROW` — peers (ties) are included; spell `ROWS` when you mean rows.
- **Golden fingerprint:** `31:1c8f130e`

#### SQL-E5.3 · Days since the previous order
- **Tags:** lag · partitions
- **Prompt:** For users 1–20: each order with the number of whole days since the same user's previous order (NULL for their first). Use calendar days (`placed_at::date`).
- **Output shape:** `user_id, order_id, placed_at, gap_days` (order-insensitive — `lab.chk`)
- **Trap:** `lag` needs a total order inside the partition — add `order_id` as tie-break. `date - date` is an integer in Postgres; timestamp − timestamp is an interval.
- **Golden fingerprint:** `996:d7137b70`

#### SQL-E5.4 · Top-2 orders per user
- **Tags:** row_number · top-N per group
- **Prompt:** For users 1–50: their two largest orders by `total_minor` (ties → lower `order_id`), with the position 1 or 2.
- **Output shape:** `user_id, order_id, total_minor, rn` (order-insensitive — `lab.chk`)
- **Trap:** `LIMIT 2` gives two rows overall, not per user. The tie-break is part of the spec — without it two correct answers differ.
- **Golden fingerprint:** `100:8a1679d3`

#### SQL-E5.5 · Tenant share of 2025 GMV
- **Tags:** sum() OVER () · ratio to total
- **Prompt:** Per tenant: fulfilled GMV in 2025 and its percentage of the all-tenant total, rounded to 2 decimals.
- **Output shape:** `tenant_id, gmv_minor, pct` (order-insensitive — `lab.chk`)
- **Trap:** Window over the *aggregated* result: `sum(sum(x)) OVER ()`. Cast to numeric before dividing.
- **Golden fingerprint:** `5:4bec02c5`

#### SQL-E5.6 · Price quartiles, tenant 2
- **Tags:** ntile · bucket boundaries
- **Prompt:** Live products of tenant 2 split into 4 price quartiles with `ntile(4)` ordered by price ascending then `product_id`.
- **Output shape:** `product_id, price_minor, quartile` (order-insensitive — `lab.chk`)
- **Trap:** `ntile` splits by **row count**, not by value — equal prices can land in different tiles; and if N is not divisible by 4 the first tiles get the extra rows.
- **Golden fingerprint:** `94:71892706`

#### SQL-E5.7 · First and last price
- **Tags:** first_value · last_value · frame trap
- **Prompt:** For products 1–20: the first and last `price_minor` in `product_price_history` (by `valid_from`) and the change (last − first).
- **Output shape:** `product_id, first_price, last_price, delta` (order-insensitive — `lab.chk`)
- **Trap:** `last_value(x) OVER (ORDER BY t)` returns the *current* row when the default frame stops at CURRENT ROW. You need `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`, or use `first_value` with a reversed ORDER BY. Wrong-path fingerprint (do not chase): `60:99a2d437` — last_value with the default frame.
- **Golden fingerprint:** `20:7ddcb09e`

#### SQL-E5.8 · 7-day moving average of daily orders
- **Tags:** ROWS frame · moving average · warm-up rows
- **Prompt:** Tenant 2, orders placed in February 2025: per day the order count and the average of the current and previous 6 days' counts, rounded to 2 decimals. Emit the average only when a full 7-day window exists inside February (from 7 Feb).
- **Output shape:** `day, n, avg7` (ordered by day) (ordered — use `lab.chk_o`)
- **Trap:** A `ROWS 6 PRECEDING` frame silently shrinks at the start — you must suppress the warm-up rows yourself. `ROWS` counts rows, so missing days (gaps) would silently stretch the window; here there are no empty days — say why you checked.
- **Golden fingerprint:** `22:55be0551`

### 6.6 Level 6 — Advanced windows

**Prereq gate:** SQL-E5 gate; SL-08 frames

#### SQL-E6.1 · Longest login streak
- **Tags:** gaps and islands · row_number difference
- **Prompt:** From `login_day` (users 1–200, 120 days): each user's longest run of **consecutive** days and the day it started (earliest start on ties).
- **Output shape:** `user_id, streak_len, streak_start` (order-insensitive — `lab.chk`)
- **Trap:** Consecutive days share a constant `day − row_number()`. Do not use `count(*)` per user, and do not forget that the PK already guarantees no duplicate days (if it didn't, dedupe before numbering).
- **Golden fingerprint:** `200:3d4d4f51`

#### SQL-E6.2 · Sessionise the event stream
- **Tags:** sessionization · lag · cumulative sum
- **Prompt:** For identified users (`user_id IS NOT NULL`): a new session starts when the gap to the user's previous event is **> 30 minutes** (or there is no previous event). Return one row per session: user, session number (1-based per user, by time), event count, first and last event time.
- **Output shape:** `user_id, session_no, n_events, started_at, ended_at` (order-insensitive — `lab.chk`)
- **Trap:** Three steps: (1) `lag` to get the gap, (2) flag `gap > interval '30 minutes' OR gap IS NULL`, (3) running `sum(flag)` as the session id. Ties on `occurred_at` need an `event_id` tie-break.
- **Golden fingerprint:** `7500:311fb683`

#### SQL-E6.3 · Ordered funnel
- **Tags:** conditional aggregation · ordered steps
- **Prompt:** How many identified users performed `add_to_cart`, later `checkout_start`, later `purchase` — in that order (each step strictly after the previous, using each user's **first** occurrence of the step)? One number, plus the counts that reached step 1 and step 2 as a funnel.
- **Output shape:** `n_cart, n_checkout, n_purchase` (one row) (order-insensitive — `lab.chk`)
- **Trap:** `count(DISTINCT user_id) WHERE event_type = …` per step ignores order. Compute each user's first time per step with `min(…) FILTER`, then compare the timestamps.
- **Golden fingerprint:** `1:2f3673b3`

#### SQL-E6.4 · Price in effect at order time (as-of join)
- **Tags:** as-of join · LATERAL · temporal correctness
- **Prompt:** For order lines of orders placed **before 2025-01-04**: the list price that was in effect at `placed_at` (the history row with the greatest `valid_from <= placed_at`), and the lines where the price actually charged (`unit_price_minor`) differs from it.
- **Output shape:** `order_id, line_no, unit_price_minor, price_at_order` (order-insensitive — `lab.chk`)
- **Trap:** A plain equi-join on `product_id` returns three rows per line. Use `LATERAL … ORDER BY valid_from DESC LIMIT 1` (or `DISTINCT ON`, or a window). The `<=` boundary is inclusive: an order at exactly `valid_from` sees the *new* price. This is the same shape as the DD-05 (D3) point-in-time joins. Wrong-path fingerprint (do not chase): `808:97a9c21a` — plain equi-join returns all three price rows.
- **Golden fingerprint:** `404:4f5a2a10`

#### SQL-E6.5 · Orders in the previous 30 days
- **Tags:** RANGE frame with interval · self-window
- **Prompt:** For users 1–20: each order and how many **other** orders the same user placed in the 30 days before it (`placed_at − 30 days` up to and including this order's time, excluding itself).
- **Output shape:** `user_id, order_id, prior_30d` (order-insensitive — `lab.chk`)
- **Trap:** A `RANGE BETWEEN INTERVAL '30 days' PRECEDING AND CURRENT ROW` frame includes the current row *and its peers*; subtract 1 and think about equal timestamps. `ROWS 30 PRECEDING` would count rows, not days.
- **Golden fingerprint:** `996:7e7490f1`

#### SQL-E6.6 · Signup-cohort activation
- **Tags:** cohort analysis · date_trunc · conditional counts
- **Prompt:** Cohort = signup month (`date_trunc('month', created_at)`). For each cohort: size, and how many of its users placed at least one order in the **calendar month after** their signup month.
- **Output shape:** `cohort_month, size, active_next_month` (order-insensitive — `lab.chk`)
- **Trap:** Two grains at once (users, then orders). Compute *per-user* activation first (`EXISTS`), then aggregate by cohort — do not join users to orders and `count(*)`.
- **Golden fingerprint:** `10:79a8b3a1`

#### SQL-E6.7 · Dedupe events, keep the first
- **Tags:** row_number · deduplication · planted test data
- **Prompt:** Some pipelines deliver twice. Treat two events as the same delivery when `(user_id, event_type, occurred_at)` are equal (NULL users count as equal to each other). Run your query against this **planted** input `e` (the real table plus 6,000 duplicate deliveries with ids +1,000,000): `SELECT * FROM lab.event UNION ALL SELECT event_id + 1000000, tenant_id, user_id, event_type, occurred_at, payload FROM lab.event WHERE event_id % 10 = 0`. Return the `event_id`s that are **not** the lowest id in their duplicate group.
- **Output shape:** `event_id` (order-insensitive — `lab.chk`)
- **Trap:** `PARTITION BY` treats NULLs as one group (unlike `=`). Run the query on the *un-planted* table too: it must return 0 rows — an empty result is a valid, testable answer, but only if you have also seen it return the planted rows.
- **Golden fingerprint:** `6000:a46392ec`

### 6.7 Level 7 — Recursion

**Prereq gate:** SQL-E6 gate; SL-09

#### SQL-E7.1 · Category paths
- **Tags:** recursive CTE · tree · path
- **Prompt:** For tenant 1's category tree: every category with its depth (root = 0) and the `' > '`-joined path of **names** from the root.
- **Output shape:** `category_id, depth, path` (order-insensitive — `lab.chk`)
- **Trap:** A recursive CTE = anchor (roots: `parent_id IS NULL`) `UNION ALL` recursive step joining on `parent_id`. Termination is guaranteed only if the data has no cycles — the seed does, a hostile import might not (SQL-E7.5).
- **Golden fingerprint:** `10:82a25fd0`

#### SQL-E7.2 · Products in a subtree
- **Tags:** recursive CTE · rollup up the tree
- **Prompt:** For every category of tenant 1: the number of products attached to it **or any descendant**.
- **Output shape:** `category_id, subtree_products` (order-insensitive — `lab.chk`)
- **Trap:** Materialise (ancestor, descendant) pairs, then join products to *descendant* and group by *ancestor*. A category with no products still needs a row — LEFT JOIN.
- **Golden fingerprint:** `10:13320b85`

#### SQL-E7.3 · Referral roots and depth
- **Tags:** recursive CTE · forest · depth
- **Prompt:** Users form a referral forest (`referred_by` → parent). For every user: the root user of their tree and their depth (root = 0).
- **Output shape:** `user_id, root_id, depth` (order-insensitive — `lab.chk`)
- **Trap:** Roots are the rows with `referred_by IS NULL`; carry `root_id` through the recursion instead of recomputing it. Prove termination: `referred_by < user_id` holds in this seed, so no cycle — state that invariant, don't assume it.
- **Golden fingerprint:** `2000:97e6e0a2`

#### SQL-E7.4 · Biggest referral tree
- **Tags:** recursive CTE · aggregate over recursion
- **Prompt:** The root user whose tree (including the root) has the most members; ties → lowest `user_id`.
- **Output shape:** `root_id, tree_size` (ordered — use `lab.chk_o`)
- **Trap:** Aggregate *after* the recursion. `ORDER BY tree_size DESC, root_id LIMIT 1`.
- **Golden fingerprint:** `1:36a7110f`

#### SQL-E7.5 · Find the cycle
- **Tags:** recursive CTE · cycle detection · path array
- **Prompt:** Directed edges are given inline: `(1,2),(2,3),(3,1),(4,5),(5,6)`. Return every node that lies on a cycle.
- **Output shape:** `node` (order-insensitive — `lab.chk`)
- **Trap:** Carry a `path` array and stop when the next node is already in it (`NOT next = ANY(path)`); a node is on a cycle if it can reach itself. PostgreSQL 14+ also has `CYCLE … SET … USING` — write it both ways.
- **Golden fingerprint:** `3:62171a21`

### 6.8 Level 8 — Time, JSON, text, cleaning

**Prereq gate:** SQL-E7 gate; SL-12

#### SQL-E8.1 · Average delivery time by carrier
- **Tags:** interval arithmetic · extract(epoch)
- **Prompt:** For delivered shipments: per carrier, the count and the mean transit time in **days** (shipped → delivered) rounded to 2 decimals.
- **Output shape:** `carrier, n, avg_days` (order-insensitive — `lab.chk`)
- **Trap:** `avg(interval)` is legal but unreadable; convert with `extract(epoch FROM …) / 86400` — as `numeric`, not float, before rounding. NULL `delivered_at` rows are excluded by the filter, not by luck.
- **Golden fingerprint:** `3:72b2a44b`

#### SQL-E8.2 · Stuck shipments as of a fixed instant
- **Tags:** reproducible time · never now()
- **Prompt:** Shipments not delivered more than 14 days after shipping, **as of `2026-01-01 00:00 UTC`** (undelivered and shipped before 2025-12-18).
- **Output shape:** `shipment_id` (order-insensitive — `lab.chk`)
- **Trap:** Never call `now()` in a graded query — the answer changes daily. Parameterise the 'as-of' instant. Same principle as the ledger's determinism rules (DD-03).
- **Golden fingerprint:** `1825:dc65c0f1`

#### SQL-E8.3 · UTC day vs New York day
- **Tags:** AT TIME ZONE · DST
- **Prompt:** How many orders have a **different calendar date** in `America/New_York` than in UTC? One number.
- **Output shape:** `n` (order-insensitive — `lab.chk`)
- **Trap:** `ts AT TIME ZONE 'x'` on a `timestamptz` returns a *timestamp without zone* in that zone; on a plain `timestamp` it does the reverse. Get the direction right and test across the 2025-03-09 DST change. Wrong-path fingerprint (do not chase): `1:c06c9654` — comparing UTC to UTC (wrong AT TIME ZONE direction).
- **Golden fingerprint:** `1:f10d5c9a`

#### SQL-E8.4 · Orders per ISO week
- **Tags:** date_trunc('week') · week boundaries
- **Prompt:** Orders placed in 2025 grouped by ISO week (Monday start): week start date and count.
- **Output shape:** `week_start, n` (order-insensitive — `lab.chk`)
- **Trap:** `date_trunc('week')` starts on Monday (ISO); BigQuery's `DATE_TRUNC(d, WEEK)` starts on Sunday. The first/last week straddles the year boundary.
- **Golden fingerprint:** `53:15bc9aa0`

#### SQL-E8.5 · Red eco products
- **Tags:** JSONB · @> · ? operator
- **Prompt:** Products whose `attrs` has `color = 'red'` **and** whose `attrs.tags` array contains `'eco'`.
- **Output shape:** `product_id` (order-insensitive — `lab.chk`)
- **Trap:** `attrs->>'color'` returns text; `attrs @> '{"color":"red"}'` is index-friendly (GIN). `attrs->'tags' ? 'eco'` tests membership in an array of strings. A missing key yields NULL, not false.
- **Golden fingerprint:** `41:a5be7c78`

#### SQL-E8.6 · Search latency by query term
- **Tags:** JSONB extraction · casts
- **Prompt:** For `search` events: per query term (`payload->>'q'`) the number of events and the average `payload->>'ms'` rounded to 1 decimal.
- **Output shape:** `q, n, avg_ms` (order-insensitive — `lab.chk`)
- **Trap:** `->>` returns text — cast before averaging: `(payload->>'ms')::int`. A non-numeric value would fail the whole query — in production, validate on write.
- **Golden fingerprint:** `4:eaf94d2b`

#### SQL-E8.7 · Products per tag
- **Tags:** jsonb_array_elements_text · unnesting
- **Prompt:** Explode `attrs.tags` and count products per tag.
- **Output shape:** `tag, n` (order-insensitive — `lab.chk`)
- **Trap:** A set-returning function in FROM (`CROSS JOIN LATERAL jsonb_array_elements_text(attrs->'tags')`) drops products with no tags — usually what you want; say so. In BigQuery this is `UNNEST`.
- **Golden fingerprint:** `2:71943e30`

#### SQL-E8.8 · Clean and dedupe emails
- **Tags:** trim · lower · regex · dedupe
- **Prompt:** From `lab.stg_import`: normalise `email_text` with `lower(trim(…))`, keep only values that match `^[^@\s]+@[^@\s]+\.[^@\s]+$`, and keep the **lowest `row_id`** for each normalised address.
- **Output shape:** `row_id, email_norm` (order-insensitive — `lab.chk`)
- **Trap:** Empty string and NULL are both invalid; `frank@example` has no dot. Normalise **before** deduping, or 'Ann@Example.com ' and 'ann@example.com' survive as two people.
- **Golden fingerprint:** `8:4fc20676`

#### SQL-E8.9 · Parse money text into minor units
- **Tags:** regexp · CASE · safe casts
- **Prompt:** Convert `amount_text` to integer **minor units** (×100, rounded half up). Accept an optional leading `-`, optional `$`, thousands separators `,` (only in groups of exactly three) and an optional decimal part with `.`; surrounding spaces are ignored. Anything else — `12,50`, `abc`, `1e3`, NULL — becomes NULL.
- **Output shape:** `row_id, amount_minor` (order-insensitive — `lab.chk`)
- **Trap:** Decide the rule for `12,50` (European decimal comma) explicitly — here it is *invalid*, never guessed. Validate with a regex **before** casting; a bare `::numeric` on bad text aborts the whole statement.
- **Golden fingerprint:** `15:bafc9e47`

#### SQL-E8.10 · Write a total date parser
- **Tags:** user-defined function · exception handling · dialect
- **Prompt:** Create `work.try_date(text) RETURNS date` that returns a date for: ISO `YYYY-MM-DD` (after trimming, and also when followed by a `T…` time), `MM/DD/YYYY`, and `D Mon YYYY` (e.g. `1 Mar 2025`); **NULL** for anything else, including impossible dates like `2025-13-40` and `2025-02-29`. Then `SELECT row_id, work.try_date(signup_text)` over `stg_import`.
- **Output shape:** `row_id, d` (order-insensitive — `lab.chk`)
- **Trap:** A cast error aborts the statement; catch it in a `BEGIN … EXCEPTION WHEN others THEN RETURN NULL` block (PL/pgSQL). Postgres 16 adds `pg_input_is_valid()`; BigQuery has `SAFE.PARSE_DATE`, SQL Server `TRY_CONVERT`. `2025-02-29` must fail — 2025 is not a leap year.
- **Golden fingerprint:** `15:3eed39e7`

### 6.9 Level 9 — DML

**Prereq gate:** SQL-E8 gate; SL-10

#### SQL-E9.1 · Materialise a daily GMV table
- **Tags:** CREATE TABLE · INSERT … SELECT · PK
- **Prompt:** In schema `work`, create `tenant_daily_gmv(tenant_id int, day date, gmv_minor bigint NOT NULL, PRIMARY KEY (tenant_id, day))` and fill it with fulfilled-order GMV per tenant per UTC day for **January 2025**.
- **Output shape:** table contents `tenant_id, day, gmv_minor` (order-insensitive — `lab.chk`)
- **Trap:** Column list on `INSERT` (never rely on positional order across a migration). Create the constraint *with* the table so a re-run fails loudly instead of duplicating. All DML in this level is graded inside a transaction that is rolled back — you can retry freely.
- **Golden fingerprint:** `155:9a2d7927`

#### SQL-E9.2 · Repair corrupted totals
- **Tags:** UPDATE … FROM · IS DISTINCT FROM
- **Prompt:** Setup gives you `work.o`, a copy of `customer_order` in which every 100th order (`order_id % 100 = 0`, 200 rows) has `total_minor = 0`. Repair **only the wrong rows** so that `total_minor` equals the sum of `qty × unit_price_minor` of its lines. The statement must report `UPDATE 200`.
- **Output shape:** `work.o` equals `lab.customer_order` on `(order_id, total_minor)` (order-insensitive — `lab.chk`)
- **Trap:** Updating *every* row (no `WHERE … IS DISTINCT FROM`) rewrites 20,000 tuples — table bloat and WAL for no reason. `IS DISTINCT FROM`, not `<>`, so a NULL total would be repaired too.
- **Golden fingerprint:** `20000:12518931`

#### SQL-E9.3 · Idempotent daily load (upsert)
- **Tags:** INSERT … ON CONFLICT DO UPDATE · idempotency
- **Prompt:** Create `work.daily_orders(day date PRIMARY KEY, n int NOT NULL)`. Write one statement that loads the count of orders per UTC day for all of 2025 and can be **run twice with the same result**.
- **Output shape:** `day, n` (order-insensitive — `lab.chk`)
- **Trap:** `SET n = daily_orders.n + EXCLUDED.n` is *not* idempotent (a re-run doubles). `SET n = EXCLUDED.n` is. If your source query returned two rows for one day in a single statement you would get `ON CONFLICT DO UPDATE command cannot affect row a second time` — aggregate first. Idempotent writes are the whole point of A7/A9.
- **Golden fingerprint:** `365:60b9c8d0`

#### SQL-E9.4 · Delete the double-submitted reviews
- **Tags:** DELETE … USING · self-join delete · RETURNING
- **Prompt:** Setup gives `work.r`, a copy of `review`. Delete duplicate `(product_id, user_id)` reviews, **keeping the newest** (highest `review_id`). Report how many were deleted (`DELETE 400`).
- **Output shape:** `work.r` keeps 6,000 rows (order-insensitive — `lab.chk`)
- **Trap:** Test the *keep* rule on a tiny sample first. `DELETE` on a self-join needs `USING`; without a total order you can delete both copies. Run it inside `BEGIN … ROLLBACK` in real life until the count matches your prediction.
- **Golden fingerprint:** `6000:bc58a9d4`

#### SQL-E9.5 · Sync stock with MERGE
- **Tags:** MERGE (PG15+) · three-way sync
- **Prompt:** Setup gives `work.stock_t` (products 1–10 with `on_hand`) and `work.stock_feed` (a partner feed). With **one `MERGE`**: rows in both → update `on_hand`, **except** feed `on_hand = 0` → delete the target row; feed rows not in target → insert.
- **Output shape:** `work.stock_t` afterwards (small — check by eye) (ordered — use `lab.chk_o`)
- **Trap:** `MERGE` arrived in PostgreSQL 15; `WHEN NOT MATCHED BY SOURCE` only in 17 — so 'delete rows missing from the feed' cannot be done in one 15/16 MERGE. Many-to-one source rows raise a cardinality error. SQL Server, Oracle, BigQuery all have `MERGE` with dialect differences (Rosetta table).
- **Golden fingerprint:** `11:61ddd589`

#### SQL-E9.6 · Chunked backfill
- **Tags:** batching · SKIP LOCKED · WAL/bloat awareness
- **Prompt:** Setup gives `work.o` (copy of `customer_order`) with a new nullable column `total_major numeric(12,2)`. Backfill `total_minor / 100.0` in chunks of **1,000 rows**, looping until no rows are left. (Here one transaction; in production every chunk commits separately — DD-11 expand/contract, run as an OD-08 job.)
- **Output shape:** all 20,000 rows have `total_major` set (order-insensitive — `lab.chk`)
- **Trap:** `WHERE total_major IS NULL … LIMIT` inside a CTE + `UPDATE … RETURNING` is the loop body. One giant `UPDATE` holds locks and WAL for minutes on a real table and blocks vacuum. Chunk size is a *tuning knob*, not a constant.
- **Golden fingerprint:** `20000:f913007e`

#### SQL-E9.7 · Archive refunded orders atomically
- **Tags:** writable CTE · DELETE … RETURNING
- **Prompt:** Setup gives `work.o` (copy of `customer_order`) and an empty `work.o_archive (LIKE work.o)`. In **one statement**, move every refunded order from `work.o` into `work.o_archive`.
- **Output shape:** `live, archived` counts (18000, 2000) (order-insensitive — `lab.chk`)
- **Trap:** `DELETE … RETURNING *` inside a CTE feeding an `INSERT` is atomic — no window where the row is in both or neither. Doing it as two statements needs a transaction; doing it in the application needs an outbox.
- **Golden fingerprint:** `1:06897331`

### 6.10 Level 10 — DDL & constraints

**Prereq gate:** SQL-E9 gate; SL-01, DD-12, SL-13

#### SQL-E10.1 · Coupon table: constraints as a specification
- **Tags:** CHECK · UNIQUE · exactly-one-of · citext-free case-insensitive unique
- **Prompt:** Create `work.coupon` so that this **battery of 8 inserts gives exactly the pass/fail vector `T T F F F F F T`**:
1. `('SAVE10', percent_off=10, amount_off_minor=NULL, 2025-01-01 → 2025-02-01)` succeeds · 2. a percent coupon with `percent_off=100` succeeds · 3. `percent_off=0` fails · 4. `percent_off=101` fails · 5. **both** `percent_off` and `amount_off_minor` set fails · 6. **neither** set fails · 7. a second code `'save10'` (different case) fails · 8. an amount coupon `amount_off_minor=500` with `valid_until` NULL succeeds.
(Battery statements are in Appendix B.1.)
- **Output shape:** vector of booleans, ordered by test number (ordered — use `lab.chk_o`)
- **Trap:** 'Exactly one of' = `num_nonnulls(percent_off, amount_off_minor) = 1`. Case-insensitive uniqueness needs a *functional* unique index on `lower(code)` (or `citext`). CHECK passes when the expression is NULL — write NOT NULL where you mean it.
- **Golden fingerprint:** `8:e5c729de`

#### SQL-E10.2 · Tenant-safe foreign key
- **Tags:** composite FK · multi-tenancy · integrity at the schema level
- **Prompt:** Create `work.note(note_id bigint PK, tenant_id int NOT NULL, user_id bigint NOT NULL, body text)` so that a note can only reference a user **of the same tenant**. Battery (Appendix B.2) must give `T F F F`: (1) tenant 1 / user 1 ok · (2) tenant 2 / user 1 fails (user 1 is tenant 1's) · (3) tenant 1 / user 999999 fails · (4) NULL tenant fails.
- **Output shape:** vector of booleans (ordered — use `lab.chk_o`)
- **Trap:** `user_id REFERENCES app_user` alone only proves the user *exists*. The composite `FOREIGN KEY (tenant_id, user_id) REFERENCES app_user (tenant_id, user_id)` needs a matching unique constraint on the parent — that is why the lab's `app_user` carries `UNIQUE (tenant_id, user_id)`. This is defence in depth beneath RLS (DD-09).
- **Golden fingerprint:** `4:8c4ee581`

#### SQL-E10.3 · One active subscription per user
- **Tags:** partial unique index · state machine invariants
- **Prompt:** `work.subscription(sub_id bigint PK, user_id bigint NOT NULL, status text CHECK (status IN ('active','cancelled')))`. Enforce **at most one `active` row per user**, any number of cancelled. Battery (Appendix B.3) expects `T T T F T`: (1) user 1 active · (2) user 1 cancelled · (3) user 1 cancelled again · (4) user 1 second active — fails · (5) user 2 active.
- **Output shape:** vector of booleans (ordered — use `lab.chk_o`)
- **Trap:** A plain `UNIQUE (user_id, status)` would forbid a second *cancelled* row. The invariant is conditional — a **partial unique index** `… (user_id) WHERE status = 'active'`. Race-free by construction, unlike an application-side check.
- **Golden fingerprint:** `5:7a0a9605`

#### SQL-E10.4 · No overlapping price validity
- **Tags:** EXCLUDE constraint · range types · btree_gist
- **Prompt:** `work.price_period(product_id bigint, during daterange, price_minor int)`. Forbid two rows of the **same product** whose periods overlap. Battery (Appendix B.4) expects `T T F T F`: (1) p1 `[2025-01-01,2025-02-01)` · (2) p1 `[2025-02-01,2025-03-01)` (touching is fine) · (3) p1 `[2025-01-15,2025-01-20)` overlaps → fails · (4) p2 same dates as (1) fine · (5) p1 `[2025-02-28,2025-04-01)` overlaps (2) → fails.
- **Output shape:** vector of booleans (ordered — use `lab.chk_o`)
- **Trap:** Uniqueness of `(product_id, valid_from)` does **not** stop overlaps. `EXCLUDE USING gist (product_id WITH =, during WITH &&)` needs `btree_gist` for the `=` part. Half-open ranges `[a,b)` make 'touching' legal. Spanner and BigQuery have no exclusion constraints — you'd enforce in a transaction (Rosetta table).
- **Golden fingerprint:** `5:a6c6c4a9`

#### SQL-E10.5 · Circular references with DEFERRABLE
- **Tags:** DEFERRABLE INITIALLY DEFERRED · constraint timing
- **Prompt:** Two tables reference each other: `work.a(id PK, b_id → b)` and `work.b(id PK, a_id → a)`. Make it possible to insert `a(1, b_id=1)` and `b(1, a_id=1)` **in one transaction** but impossible to commit a dangling reference. Battery (Appendix B.5) is a `DO` block — expected: block succeeds; then a lone `INSERT INTO a VALUES (2, 99)` inside its own transaction **fails at COMMIT** (not at the INSERT).
- **Output shape:** commit-time failure demonstrated (order-insensitive — `lab.chk`)
- **Trap:** Without `DEFERRABLE INITIALLY DEFERRED` the first insert fails immediately. Deferred checks run at `COMMIT` — so the error surfaces *after* your `INSERT` returned success; app code must handle a failed commit. `SET CONSTRAINTS … DEFERRED` scopes it per transaction.
- **Golden fingerprint:** `1:fb0ce7c2`

#### SQL-E10.6 · Row-level security by tenant
- **Tags:** RLS · policies · current_setting · roles
- **Prompt:** Enable RLS on `work.o` (a copy of `customer_order`) so that a role `app_rls` sees **only rows where `tenant_id = current_setting('app.tenant_id')::int`**. Then, as `app_rls` with `app.tenant_id = '2'`, count rows per tenant. Predict first: how many rows, which tenants? What happens if the setting is unset?
- **Output shape:** `tenant_id, n` (a single row for tenant 2) (order-insensitive — `lab.chk`)
- **Trap:** RLS does **not** apply to the table owner or superusers unless `FORCE ROW LEVEL SECURITY`. `current_setting('x', true)` returns NULL when unset (no rows), without `true` it raises. Connection-pool reuse means the setting must be `SET LOCAL` per transaction — DD-09 RLS.
- **Golden fingerprint:** `1:86599c11`

### 6.13 Level 13 — Analytics SQL

**Prereq gate:** SQL-E10 gate; AN-01…AN-03, SL-05/08

#### SQL-E13.1 · Subtotals with ROLLUP
- **Tags:** GROUP BY ROLLUP · GROUPING() · subtotals
- **Prompt:** Fulfilled 2025 orders: GMV by `(tenant_id, currency)` with **per-tenant subtotals** and a **grand total** row. Add a column `level` = `'detail'`, `'tenant'` or `'grand'` computed with `GROUPING()`.
- **Output shape:** `tenant_id, currency, gmv_minor, level` (order-insensitive — `lab.chk`)
- **Trap:** A subtotal row has NULL in the rolled-up column — indistinguishable from a real NULL. `GROUPING(col)` is 1 for rolled-up NULLs. Adding two currencies into one grand total is only meaningful if you say so (tenant 4 is EUR) — a business-rule trap.
- **Golden fingerprint:** `11:bbcd158f`

#### SQL-E13.2 · Pivot statuses into columns
- **Tags:** conditional aggregation · pivot
- **Prompt:** One row per tenant with five count columns `created, paid, fulfilled, refunded, cancelled` (orders placed in 2025).
- **Output shape:** `tenant_id, created, paid, fulfilled, refunded, cancelled` (order-insensitive — `lab.chk`)
- **Trap:** Standard SQL has no `PIVOT` (SQL Server/Oracle/BigQuery do). The portable idiom is `count(*) FILTER (WHERE …)` or `sum(CASE …)`. The column list is fixed at write time — dynamic pivots need dynamic SQL.
- **Golden fingerprint:** `5:f64390e3`

#### SQL-E13.3 · Build a star schema
- **Tags:** dimensional modelling · fact/dim · surrogate keys
- **Prompt:** In `work`, build `dim_product(product_id, name, category_name)` (category name or `'(none)'`), `dim_date(date_key, year, month)` for 2025 and `fact_sales(order_id, line_no, date_key, product_id, qty, revenue_minor)` from **fulfilled** order lines. Then answer with the star: *revenue by category name and month for 2025*.
- **Output shape:** `category_name, month, revenue_minor` (order-insensitive — `lab.chk`)
- **Trap:** Facts hold measures + foreign keys at one **grain** (an order line); dimensions hold descriptions. Decide grain first, write it in one sentence. In BigQuery you would partition the fact by date and cluster by product (V-DATA, AN-02) and often *denormalise* the dimensions in.
- **Golden fingerprint:** `372:22383318`

#### SQL-E13.4 · Price history as a Type-2 dimension
- **Tags:** SCD2 · lead() · valid_to
- **Prompt:** From `product_price_history` build a Type-2 slowly-changing dimension: `product_id, price_minor, valid_from, valid_to, is_current` where `valid_to` is the next row's `valid_from` (NULL for the current row). Products 1–10 only.
- **Output shape:** `product_id, price_minor, valid_from, valid_to, is_current` (order-insensitive — `lab.chk`)
- **Trap:** `valid_to` = `lead(valid_from)` — half-open `[from, to)`. Keep `is_current` derived (`valid_to IS NULL`), never hand-set. Overlap is prevented by SQL-E10.4's exclusion constraint.
- **Golden fingerprint:** `30:12ca6f21`

#### SQL-E13.5 · Revenue at the price in effect
- **Tags:** as-of join · SCD2 join · range join
- **Prompt:** Using the SCD2 shape of SQL-E13.4, re-derive each fulfilled order line of **January 2025** at the *list price in effect at `placed_at`* and return the total difference `sum(qty × (list_price_at_order − unit_price_minor))` per tenant. (Expect a large positive number: the seed charged the *current* price, not the historical one.)
- **Output shape:** `tenant_id, price_gap_minor` (order-insensitive — `lab.chk`)
- **Trap:** Join on the *range* `valid_from <= placed_at AND (valid_to IS NULL OR placed_at < valid_to)` — the half-open form makes every order match exactly one row. Check that: `count(*)` of the join must equal `count(*)` of the lines.
- **Golden fingerprint:** `5:7656600a`

### 6.14 Level 14 — Capstone audits & performance

**Prereq gate:** SQL-E13 gate; SQL-CAP1 after SQL-E3+SQL-E4; SQL-CAP2 after SQL-E4.5; SQL-CAP4 after PX cards

#### SQL-CAP1.1 · Order total ≠ sum of its lines
- **Tags:** audit invariant · anti-join / aggregate · data quality
- **Prompt:** On the fault-injected copies in schema `audit` (Appendix B.6): find every violation of the invariant *order total ≠ sum of its lines*. Also run it against the clean `lab.*` tables — it must return **0 rows** there.
- **Output shape:** `order_id` (order-insensitive — `lab.chk`)
- **Trap:** Orders **with no lines** would slip through an inner join — is that a separate invariant? (yes: add it if you consider 'empty order' illegal).
- **Golden fingerprint:** `3:7cc530bb`

#### SQL-CAP1.2 · Order lines with no order (orphans)
- **Tags:** audit invariant · anti-join / aggregate · data quality
- **Prompt:** On the fault-injected copies in schema `audit` (Appendix B.6): find every violation of the invariant *order lines with no order (orphans)*. Also run it against the clean `lab.*` tables — it must return **0 rows** there.
- **Output shape:** `order_id, line_no` (order-insensitive — `lab.chk`)
- **Trap:** The real schema has an FK, so this can't happen there — this audit is for *imported* or FK-less (warehouse) data.
- **Golden fingerprint:** `1:ec2bf809`

#### SQL-CAP1.3 · Paid/fulfilled/refunded order with no succeeded charge
- **Tags:** audit invariant · anti-join / aggregate · data quality
- **Prompt:** On the fault-injected copies in schema `audit` (Appendix B.6): find every violation of the invariant *paid/fulfilled/refunded order with no succeeded charge*. Also run it against the clean `lab.*` tables — it must return **0 rows** there.
- **Output shape:** `order_id` (order-insensitive — `lab.chk`)
- **Trap:** A *failed* charge followed by a succeeded one is legal (every 15th order). Test the anti-join on `status = 'succeeded'`, not on 'has any charge'.
- **Golden fingerprint:** `2:addb7d1b`

#### SQL-CAP1.4 · Refunds exceed charges
- **Tags:** audit invariant · anti-join / aggregate · data quality
- **Prompt:** On the fault-injected copies in schema `audit` (Appendix B.6): find every violation of the invariant *refunds exceed charges*. Also run it against the clean `lab.*` tables — it must return **0 rows** there.
- **Output shape:** `order_id` (order-insensitive — `lab.chk`)
- **Trap:** Aggregate the payments table **alone** (one grain), never join it to lines first.
- **Golden fingerprint:** `2:23dae8cd`

#### SQL-CAP1.5 · Reserved stock above on-hand
- **Tags:** audit invariant · anti-join / aggregate · data quality
- **Prompt:** On the fault-injected copies in schema `audit` (Appendix B.6): find every violation of the invariant *reserved stock above on-hand*. Also run it against the clean `lab.*` tables — it must return **0 rows** there.
- **Output shape:** `product_id` (order-insensitive — `lab.chk`)
- **Trap:** The real table forbids this with a CHECK; `CREATE TABLE AS` copies data, not constraints — a classic way audit copies lose their guard rails.
- **Golden fingerprint:** `2:cc6c5a8d`

#### SQL-CAP1.6 · Duplicate idempotency keys within a tenant
- **Tags:** audit invariant · anti-join / aggregate · data quality
- **Prompt:** On the fault-injected copies in schema `audit` (Appendix B.6): find every violation of the invariant *duplicate idempotency keys within a tenant*. Also run it against the clean `lab.*` tables — it must return **0 rows** there.
- **Output shape:** `tenant_id, idempotency_key, n` (order-insensitive — `lab.chk`)
- **Trap:** NULL keys are legitimately repeated (a UNIQUE index allows many NULLs). Exclude them explicitly.
- **Golden fingerprint:** `1:3402ab9a`

#### SQL-CAP1.7 · Delivered before shipped
- **Tags:** audit invariant · anti-join / aggregate · data quality
- **Prompt:** On the fault-injected copies in schema `audit` (Appendix B.6): find every violation of the invariant *delivered before shipped*. Also run it against the clean `lab.*` tables — it must return **0 rows** there.
- **Output shape:** `shipment_id` (order-insensitive — `lab.chk`)
- **Trap:** NULL `delivered_at` compares UNKNOWN → correctly excluded.
- **Golden fingerprint:** `2:b713c027`

#### SQL-CAP1.8 · Fulfilled order with no shipment
- **Tags:** audit invariant · anti-join / aggregate · data quality
- **Prompt:** On the fault-injected copies in schema `audit` (Appendix B.6): find every violation of the invariant *fulfilled order with no shipment*. Also run it against the clean `lab.*` tables — it must return **0 rows** there.
- **Output shape:** `order_id` (order-insensitive — `lab.chk`)
- **Trap:** Anti-join again. Contrast with SQL-E3.5 (semi-join).
- **Golden fingerprint:** `2:7bd384d1`

#### SQL-CAP2 · Cash-basis monthly revenue report
- **Tags:** capstone · payments · accrual vs cash
- **Prompt:** Per tenant and **payment** month (UTC, by `payment.created_at`): sum of **succeeded charges**, sum of **succeeded refunds**, and net = charges − refunds. Failed and pending payments never count. Then write two sentences reconciling this *cash* report with the *accrual* report of SQL-E4.5 (orders by placement date).
- **Output shape:** `tenant_id, month, charged_minor, refunded_minor, net_minor` (order-insensitive — `lab.chk`)
- **Trap:** A refund posted five days after an order can land in the next month — cash vs accrual differences are **timing**, not error. Aggregate `payment` on its own (no join to lines/orders except to get `tenant_id`). Money never leaves integer minor units.
- **Golden fingerprint:** `65:b63b5f6f`

#### SQL-CAP4 · Explain and fix the slow query
- **Tags:** capstone · performance · correlated subquery → join
- **Prompt:** For every identified user who ever made a `purchase` event: the number of `page_view` events in the 24 hours **before their first purchase**. The baseline query (Appendix B.7) uses three correlated subqueries per user and takes ~1.5 s on this seed. Deliverable: (1) `EXPLAIN (ANALYZE)` of the baseline with your written diagnosis, (2) a rewrite that returns the **identical fingerprint** in under 50 ms without adding an index, (3) a second fix that keeps the baseline text and adds an index — name it.
- **Output shape:** `user_id, views_24h` (order-insensitive — `lab.chk`)
- **Trap:** Fingerprint first, speed second: a fast wrong answer is worthless. The rewrite computes each user's first-purchase time **once** (CTE, `min … GROUP BY user_id`) and joins; the index alternative is `(user_id, event_type, occurred_at)` or `(user_id, occurred_at)`.
- **Golden fingerprint:** `250:eb4c8d2a`

### 6.L Plan-prediction cards (PX-1 … PX-11) — full labs in §7.1

#### PX-1 · Hot key vs cold key plans
- **Tags:** plans.py PX-1
- **Prompt:** Predict Seq Scan vs Index Scan for `user_id=1` (hot), `=42`, `=1900` (never ordered) on `customer_order`. Then run §7.1.
- **Output shape:** plan shape + row est
- **Trap:** reading EXPLAIN after changing three things at once
- **Golden fingerprint:** _(plan shape — see §7.1)_
- **Prereq gate:** OD-01, CS-02/03/08 as relevant

#### PX-2 · Sargability of `::date`
- **Tags:** PX-2
- **Prompt:** Predict whether `placed_at::date = '2025-03-01'` uses `o_placed` B-tree; rewrite as range.
- **Output shape:** used/not + rewrite
- **Trap:** reading EXPLAIN after changing three things at once
- **Golden fingerprint:** _(plan shape — see §7.1)_
- **Prereq gate:** OD-01, CS-02/03/08 as relevant

#### PX-3 · Leading wildcard vs pattern_ops
- **Tags:** PX-3
- **Prompt:** Predict `LIKE '%@t1…'` vs `LIKE 'user1%'` with btree vs `text_pattern_ops`.
- **Output shape:** three plan shapes
- **Trap:** reading EXPLAIN after changing three things at once
- **Golden fingerprint:** _(plan shape — see §7.1)_
- **Prereq gate:** OD-01, CS-02/03/08 as relevant

#### PX-4 · Leftmost prefix
- **Tags:** PX-4
- **Prompt:** Index `(tenant_id,status,placed_at)`: which of eq+eq+range / skip-leading / OR two cols uses it?
- **Output shape:** per-query yes/no
- **Trap:** reading EXPLAIN after changing three things at once
- **Golden fingerprint:** _(plan shape — see §7.1)_
- **Prereq gate:** OD-01, CS-02/03/08 as relevant

#### PX-5 · Covering INCLUDE
- **Tags:** PX-5
- **Prompt:** Predict index-only sum of `total_minor` with `(tenant_id,placed_at) INCLUDE (total_minor)` after VACUUM.
- **Output shape:** heap fetches 0/≠0
- **Trap:** reading EXPLAIN after changing three things at once
- **Golden fingerprint:** _(plan shape — see §7.1)_
- **Prereq gate:** OD-01, CS-02/03/08 as relevant

#### PX-6 · Partial index
- **Tags:** PX-6
- **Prompt:** Index `(order_id) WHERE status='created'`: hit vs miss when filter differs.
- **Output shape:** hit/miss
- **Trap:** reading EXPLAIN after changing three things at once
- **Golden fingerprint:** _(plan shape — see §7.1)_
- **Prereq gate:** OD-01, CS-02/03/08 as relevant

#### PX-7 · Join large vs selective
- **Tags:** PX-7
- **Prompt:** Predict hash/merge/nested for `order_line⋈product` full vs `product_id=42`.
- **Output shape:** node types
- **Trap:** reading EXPLAIN after changing three things at once
- **Golden fingerprint:** _(plan shape — see §7.1)_
- **Prereq gate:** OD-01, CS-02/03/08 as relevant

#### PX-8 · Correlated stats
- **Tags:** PX-8
- **Prompt:** Before/after `CREATE STATISTICS … (dependencies)` on `(tenant_id,currency)` — predict est rows move.
- **Output shape:** est before/after
- **Trap:** reading EXPLAIN after changing three things at once
- **Golden fingerprint:** _(plan shape — see §7.1)_
- **Prereq gate:** OD-01, CS-02/03/08 as relevant

#### PX-9 · OFFSET vs keyset
- **Tags:** PX-9 · OD-09
- **Prompt:** Predict cost of `OFFSET 19000` vs `WHERE order_id>19000 LIMIT 20`.
- **Output shape:** relative cost
- **Trap:** reading EXPLAIN after changing three things at once
- **Golden fingerprint:** _(plan shape — see §7.1)_
- **Prereq gate:** OD-01, CS-02/03/08 as relevant

#### PX-10 · Sort / window memory
- **Tags:** PX-10
- **Prompt:** Predict external sort when `work_mem='64kB'` on `event ORDER BY occurred_at`.
- **Output shape:** in-memory vs disk
- **Trap:** reading EXPLAIN after changing three things at once
- **Golden fingerprint:** _(plan shape — see §7.1)_
- **Prereq gate:** OD-01, CS-02/03/08 as relevant

#### PX-11 · Hash agg spill
- **Tags:** PX-11
- **Prompt:** Predict hash aggregate spill under tiny `work_mem` for `GROUP BY user_id` on events.
- **Output shape:** spill yes/no
- **Trap:** reading EXPLAIN after changing three things at once
- **Golden fingerprint:** _(plan shape — see §7.1)_
- **Prereq gate:** OD-01, CS-02/03/08 as relevant

### 6.T Transaction labs (TX-1 … TX-8) — scripts in §7.2

#### TX-1 · Lost update under RC RMW
- **Tags:** tx_tests T1
- **Prompt:** Two sessions read bal=100, write 130 and 80. Predict final under READ COMMITTED.
- **Output shape:** final bal
- **Trap:** predicting SERIALIZABLE behaviour under RR
- **Expected (post-attempt):** 80 (last writer wins)
- **Prereq gate:** CS-05

#### TX-2 · Atomic UPDATE fix
- **Tags:** T1b
- **Prompt:** Same intent with `bal=bal+30` / `bal=bal-20`. Predict final.
- **Output shape:** final bal
- **Trap:** predicting SERIALIZABLE behaviour under RR
- **Expected (post-attempt):** 110
- **Prereq gate:** CS-05

#### TX-3 · RR second writer aborts
- **Tags:** T1c
- **Prompt:** Both RR; first commits 130; second sets 80. Predict error + final.
- **Output shape:** error class + bal
- **Trap:** predicting SERIALIZABLE behaviour under RR
- **Expected (post-attempt):** serialization/RR conflict; 130
- **Prereq gate:** CS-05

#### TX-4 · Non-repeatable read RC vs RR
- **Tags:** T2
- **Prompt:** Reader re-SELECTs after writer commits 999. Predict RC vs RR second read.
- **Output shape:** two values
- **Trap:** predicting SERIALIZABLE behaviour under RR
- **Expected (post-attempt):** RC sees 999; RR sees 100
- **Prereq gate:** CS-05

#### TX-5 · Write skew on-call RR vs SSI
- **Tags:** T3
- **Prompt:** Two doctors both go off-call under RR vs SERIALIZABLE. Predict on_call count.
- **Output shape:** counts
- **Trap:** predicting SERIALIZABLE behaviour under RR
- **Expected (post-attempt):** RR→0; SSI→one aborts, count≥1
- **Prereq gate:** CS-05

#### TX-6 · Phantom insert RC vs RR
- **Tags:** T3b
- **Prompt:** Reader counts rows; other inserts. Predict second count.
- **Output shape:** two counts
- **Trap:** predicting SERIALIZABLE behaviour under RR
- **Expected (post-attempt):** RC sees +1; RR stable
- **Prereq gate:** CS-05

#### TX-7 · Deadlock
- **Tags:** T4
- **Prompt:** Classic crossed updates. Predict one session errors.
- **Output shape:** error
- **Trap:** predicting SERIALIZABLE behaviour under RR
- **Expected (post-attempt):** 40P01 deadlock detected
- **Prereq gate:** CS-05

#### TX-8 · SKIP LOCKED queue + FOR UPDATE RMW
- **Tags:** T5+T6 · A9
- **Prompt:** Two workers SKIP LOCKED claim distinct jobs; then FOR UPDATE fixes lost update. Predict claimed ids + final bal.
- **Output shape:** ids + bal
- **Trap:** predicting SERIALIZABLE behaviour under RR
- **Expected (post-attempt):** workers get disjoint ids; final bal 110
- **Prereq gate:** CS-05

### 6.B Bug-hunts (BH-1 … BH-6)

#### BH-1 · Fan-out double count
- **Tags:** SQL-E3.5 wrong
- **Prompt:** Find why summing orders joined to shipments inflates revenue.
- **Output shape:** diagnosis
- **Trap:** fixing symptoms without naming the invariant
- **Golden / ref:** goldens_wrong SQL-E3.5
- **Prereq gate:** matching SL/OD modules

#### BH-2 · Injection / string format
- **Tags:** SL-13·PQ-06
- **Prompt:** Locate a query built with f-strings; rewrite with binds.
- **Output shape:** patch
- **Trap:** fixing symptoms without naming the invariant
- **Golden / ref:** n/a
- **Prereq gate:** matching SL/OD modules

#### BH-3 · ORM N+1
- **Tags:** OD-09
- **Prompt:** Given a loop of per-user order fetches, rewrite as one join/window.
- **Output shape:** SQL
- **Trap:** fixing symptoms without naming the invariant
- **Golden / ref:** n/a
- **Prereq gate:** matching SL/OD modules

#### BH-4 · Ledger money float
- **Tags:** DD-03·DD-05
- **Prompt:** Spot a `double precision` balance; propose minor-unit int migration.
- **Output shape:** ADR+DDL
- **Trap:** fixing symptoms without naming the invariant
- **Golden / ref:** n/a
- **Prereq gate:** matching SL/OD modules

#### BH-5 · Replica lag denial
- **Tags:** OD-05·10.1
- **Prompt:** Symptom: read-your-writes fail after write on primary. Checklist.
- **Output shape:** runbook steps
- **Trap:** fixing symptoms without naming the invariant
- **Golden / ref:** n/a
- **Prereq gate:** matching SL/OD modules

#### BH-6 · Migration lockout
- **Tags:** DD-11
- **Prompt:** A `SET NOT NULL` stalls checkout. Identify lock + expand/contract fix.
- **Output shape:** diagnosis
- **Trap:** fixing symptoms without naming the invariant
- **Golden / ref:** n/a
- **Prereq gate:** matching SL/OD modules

### 6.D Dialect drills (DT-1 … DT-8)

#### DT-1 · Postgres → BigQuery SELECT
- **Tags:** AN-02
- **Prompt:** Translate SQL-E2.2 monthly GMV to GoogleSQL; note `date_trunc` vs `DATE_TRUNC`.
- **Output shape:** SQL
- **Trap:** translating tokens without translating semantics (NULL=empty, time zones)
- **Golden fingerprint:** _(dialect — instructor compares meaning)_
- **Prereq gate:** SL-14, AN-* as tagged

#### DT-2 · Bytes-scanned napkin
- **Tags:** AN-02
- **Prompt:** Same query with/without partition filter — estimate bytes.
- **Output shape:** two estimates
- **Trap:** translating tokens without translating semantics (NULL=empty, time zones)
- **Golden fingerprint:** _(dialect — instructor compares meaning)_
- **Prereq gate:** SL-14, AN-* as tagged

#### DT-3 · Postgres → MySQL LIMIT/upsert
- **Tags:** SL-14
- **Prompt:** Translate SQL-E1.7 and SQL-E9.3 upsert shapes.
- **Output shape:** SQL
- **Trap:** translating tokens without translating semantics (NULL=empty, time zones)
- **Golden fingerprint:** _(dialect — instructor compares meaning)_
- **Prereq gate:** SL-14, AN-* as tagged

#### DT-4 · Billing-export windows
- **Tags:** 10.3·AN-03
- **Prompt:** Sketch a window query on a billing-export-shaped table (reuse SQL-E5.2 idea).
- **Output shape:** SQL
- **Trap:** translating tokens without translating semantics (NULL=empty, time zones)
- **Golden fingerprint:** _(dialect — instructor compares meaning)_
- **Prereq gate:** SL-14, AN-* as tagged

#### DT-5 · Approx distinct
- **Tags:** AN-04
- **Prompt:** Rewrite `count(DISTINCT user_id)` with APPROX_COUNT_DISTINCT; state error bar.
- **Output shape:** SQL+note
- **Trap:** translating tokens without translating semantics (NULL=empty, time zones)
- **Golden fingerprint:** _(dialect — instructor compares meaning)_
- **Prereq gate:** SL-14, AN-* as tagged

#### DT-6 · Postgres → Spanner
- **Tags:** AN-05
- **Prompt:** Translate SQL-E3.1 join; note interleaved alternative as comment only.
- **Output shape:** SQL
- **Trap:** translating tokens without translating semantics (NULL=empty, time zones)
- **Golden fingerprint:** _(dialect — instructor compares meaning)_
- **Prereq gate:** SL-14, AN-* as tagged

#### DT-7 · Same question in Firestore
- **Tags:** AN-06·SD-22
- **Prompt:** Top products by GMV for tenant 2 as documents + as SQL (SQL-E2 style).
- **Output shape:** two plans
- **Trap:** translating tokens without translating semantics (NULL=empty, time zones)
- **Golden fingerprint:** _(dialect — instructor compares meaning)_
- **Prereq gate:** SL-14, AN-* as tagged

#### DT-8 · tsvector vs Vertex search
- **Tags:** AN-07
- **Prompt:** Sketch `to_tsvector` query on `product.name` and name when to leave for Vertex.
- **Output shape:** SQL+criterion
- **Trap:** translating tokens without translating semantics (NULL=empty, time zones)
- **Golden fingerprint:** _(dialect — instructor compares meaning)_
- **Prereq gate:** SL-14, AN-* as tagged

### 6.S Schema-design cases (SCH-1 … SCH-6)

#### SCH-1 · Checkout ER → tables
- **Tags:** DD-01·0.4
- **Prompt:** Model cart→order→line→payment with cardinalities; map to DDL sketch matching lab names.
- **Output shape:** ER+DDL
- **Trap:** jumping to physical indexes before logical keys
- **Golden fingerprint:** _(design review)_
- **Prereq gate:** DD-* as tagged

#### SCH-2 · Surrogate vs natural ADR
- **Tags:** DD-02·A7
- **Prompt:** ADR for `product_id` bigint vs SKU-as-PK.
- **Output shape:** ADR
- **Trap:** jumping to physical indexes before logical keys
- **Golden fingerprint:** _(design review)_
- **Prereq gate:** DD-* as tagged

#### SCH-3 · Category hierarchy pick
- **Tags:** DD-04
- **Prompt:** Choose adjacency vs closure for lab-scale categories; justify.
- **Output shape:** ADR
- **Trap:** jumping to physical indexes before logical keys
- **Golden fingerprint:** _(design review)_
- **Prereq gate:** DD-* as tagged

#### SCH-4 · Expand/contract email verify
- **Tags:** DD-11·OD-08
- **Prompt:** Add `email_verified_at` without downtime; list steps + locks.
- **Output shape:** step list
- **Trap:** jumping to physical indexes before logical keys
- **Golden fingerprint:** _(design review)_
- **Prereq gate:** DD-* as tagged

#### SCH-5 · Shard key for multi-tenant
- **Tags:** DD-13·SD-25
- **Prompt:** Propose partition/shard key for orders; address user-1 hotspot.
- **Output shape:** design note
- **Trap:** jumping to physical indexes before logical keys
- **Golden fingerprint:** _(design review)_
- **Prereq gate:** DD-* as tagged

#### SCH-6 · Audit log + masking view
- **Tags:** DD-07·CR-14
- **Prompt:** Design append-only audit and a masking view for support roles.
- **Output shape:** DDL sketch
- **Trap:** jumping to physical indexes before logical keys
- **Golden fingerprint:** _(design review)_
- **Prereq gate:** DD-* as tagged
## 7. Engine-behaviour labs

### 7.1 Plan predictions (`plans.py` → PX-1…PX-11)
Setup copies `lab.customer_order` / `app_user` into `work.*`, builds indexes step-wise, and prints `EXPLAIN (ANALYZE, … FORMAT JSON)` walks. **Protocol:** for each PX card in §6.L, write the predicted node types and row estimates, then run the matching `show("PX-…")` block. Change **one** variable between predictions (index present, `work_mem`, statistics).

Catalogue (labels in script):
- **PX-1** — index on `(user_id, placed_at DESC)`; hot user 1 vs 42 vs 1900; latest-5 limit.
- **PX-2** — `placed_at::date` non-sargable vs half-open range.
- **PX-3** — leading-wildcard `LIKE`; `text_pattern_ops` for prefix.
- **PX-4** — leftmost prefix on `(tenant_id, status, placed_at)`; OR across cols.
- **PX-5** — covering `INCLUDE (total_minor)` + `VACUUM` for index-only.
- **PX-6** — partial index `WHERE status='created'`.
- **PX-7** — large join vs selective product_id probe.
- **PX-8** — `CREATE STATISTICS (dependencies)` on `(tenant_id, currency)`.
- **PX-9** — deep `OFFSET` vs keyset seek.
- **PX-10** — sort under default vs `work_mem='64kB'`.
- **PX-11** — hash agg under tiny `work_mem`.

### 7.2 Transaction scenarios (`tx_tests.py` → TX-1…TX-8)
Dual sessions via `two.py`. Always predict commit/abort/blocking **before** running. Scenarios: lost update RMW (T1), atomic UPDATE (T1b), RR conflict (T1c), non-repeatable RC vs RR (T2), write skew RR vs SERIALIZABLE (T3), phantom (T3b), deadlock (T4), `SKIP LOCKED` queue (T5), `SELECT FOR UPDATE` (T6).

Companion SQL files:
- `naive.sql` — classic check-then-act oversell (app-side RMW).
- `safe.sql` — single-statement `UPDATE…RETURNING` claim.

### 7.3 Slow-query rescue fodder (feeds SQL-CAP4)
- `slow_bad.sql` — three correlated subqueries per user (~1.5 s on seed).
- `slow_good.sql` — CTE of first purchase + join (`SQL-CAP4` key).
- `slow_bad_idx.sql` — index-assisted path keeping baseline text shape.

## 8. Rosetta & Terraform

### 8.1 Dialect Rosetta (idea → spelling)

| Idea | Postgres / Cloud SQL / AlloyDB | Spanner (GoogleSQL) | BigQuery | MySQL 8 | SQL Server |
|---|---|---|---|---|---|
| Half-open day filter | `ts >= a AND ts < b` | same | same | same | same |
| NULL-safe ≠ | `IS DISTINCT FROM` | `IS DISTINCT FROM` | `IS DISTINCT FROM` | `<=>` / `NOT <=>` | `IS DISTINCT FROM` (2022+) `(verify)` |
| Limit | `LIMIT n` | `LIMIT` | `LIMIT` | `LIMIT` | `FETCH NEXT` / `TOP` |
| Upsert | `ON CONFLICT` | mutations / SQL upsert `(verify)` | merge / scripting | `ON DUPLICATE KEY` | `MERGE` |
| Upsert (SQL MERGE) | `MERGE` (PG15+) | limited | scripting | — | `MERGE` |
| Window frames | `ROWS/RANGE`, `EXCLUDE` | subset `(verify)` | `ROWS/RANGE` | similar | similar |
| JSON | `jsonb` `@>` `->` | `JSON` functions | `JSON` functions | `JSON_*` | `OPENJSON` |
| Identity | `GENERATED…AS IDENTITY` | `GENERATE_UUID` / bit-reversed `(verify)` | — | `AUTO_INCREMENT` | `IDENTITY` |
| RLS | native policies | app + IAM | authorised views / row policies `(verify)` | — | RLS policies |
| Money | `bigint` minor / `numeric` | `NUMERIC` | `NUMERIC` | `DECIMAL` | `DECIMAL` |
| Time zone | `timestamptz` | `TIMESTAMP` semantics `(verify)` | `TIMESTAMP` vs `DATETIME` | careful with `TIMESTAMP` | `datetimeoffset` |
| Recursion | `WITH RECURSIVE` | restricted | recursive CTEs `(verify)` | recursive CTE | recursive CTE |
| Soft dialect traps | `char(n)` pads | interleaved DDL | bytes scanned = $$$ | `utf8mb4` | NUL padding / `NOCOUNT` |

SQLite / Oracle: Rosetta footnotes only (Oracle NULL-empty collapse; SQLite type affinity) — not lab targets.

**AlloyDB:** Postgres-compatible dialect + columnar extension for analytics-ish scans (CS-09). Treat SQL as Postgres unless a lab explicitly opens columnar.

### 8.2 Terraform DB exercises (plan-only default)

Mirror the C5 posture: **`terraform plan` reads the graph; apply only if Lab Reality + credits allow, destroy same day.**

| ID | Goal | Notes |
|---|---|---|
| **TF-DB1** | Cloud SQL Postgres instance + private IP + flags sketch | Ties OD-03/04; the Auth Proxy side is OD-11 |
| **TF-DB2** | Cloud SQL read replica + failover knobs (plan) | OD-05 lag SLI discussion |
| **TF-DB3** | AlloyDB cluster + instance (plan) | Compare cost line to Cloud SQL |
| **TF-DB4** | Spanner instance + database + DDL job (plan) | Interleave as comment; no production data |
| **TF-DB5** | BigQuery dataset + partitioned table + clustering | AN-02 bytes napkin |
| **TF-DB6** | IAM bindings for DB roles / BQ dataset access | SL-13 least privilege |

**What each plan must show** (resource and attribute names from the Google provider; `(verify)` them against the provider version you pin). The exercise is done when `terraform plan` lists these and nothing public:

- **TF-DB1:** `google_compute_global_address` (purpose `VPC_PEERING`) + `google_service_networking_connection` for private services access; `google_sql_database_instance` with `database_version = "POSTGRES_16"`, `settings.ip_configuration.ipv4_enabled = false` and `private_network` set, `backup_configuration` with `point_in_time_recovery_enabled = true`, one `database_flags` block (e.g. `log_min_duration_statement`), `deletion_protection = true`. Fail: any `authorized_networks` entry or a public IP.
- **TF-DB2:** the TF-DB1 primary with `availability_type = "REGIONAL"` (HA, same-region standby) plus a second `google_sql_database_instance` with `master_instance_name` pointing at it (read replica). Explain in one line why the replica is not the failover target for HA and which OD-05 lag SLI you would alert on.
- **TF-DB3:** `google_alloydb_cluster` (network config on the same VPC) + `google_alloydb_instance` with `instance_type = "PRIMARY"` and a `machine_config` CPU count. Write the monthly cost line next to TF-DB1's at the same vCPU count.
- **TF-DB4:** `google_spanner_instance` (a regional `config`, `processing_units = 100`, the smallest paid size) + `google_spanner_database` whose `ddl` list creates a parent table and an interleaved child (`INTERLEAVE IN PARENT … ON DELETE CASCADE`); `deletion_protection = true`.
- **TF-DB5:** `google_bigquery_dataset` (location, default table expiration for the sandbox) + `google_bigquery_table` with `time_partitioning` (`type = "DAY"`, `field` = the event timestamp), `clustering` on the filter columns and a required partition filter. Pair it with the AN-02 bytes napkin: bytes scanned by one day's query vs the whole table.
- **TF-DB6:** `google_project_iam_member` giving the app's service account `roles/cloudsql.client` and `roles/cloudsql.instanceUser`; `google_sql_user` of type `CLOUD_IAM_SERVICE_ACCOUNT`; `google_bigquery_dataset_iam_member` giving an analyst group `roles/bigquery.dataViewer` on one dataset. Fail: any primitive role (`roles/owner`, `roles/editor`) or a project-wide BigQuery grant.

## 9. Capstones (SQL-CAP1–SQL-CAP4)

Database acceptance tests for the Phase 4 case-study capstone (the PCA case studies). Issue after the §6 level-14 gate. **Predict; run; reconcile.**

| ID | Title | Soft gate | Fingerprint source |
|---|---|---|---|
| **SQL-CAP1.1–SQL-CAP1.8** | Fault-injected audit invariants | SQL-E3 + SQL-E4 anti/semi-join fluency | `goldens_ex_l14.json` |
| **SQL-CAP2** | Cash-basis monthly revenue | SQL-E4.5 accrual report done | same |
| **SQL-CAP3** | Checkout schema + concurrency | SCH-1 + TX-2/TX-8 | design + TX evidence (no single chk) |
| **SQL-CAP4** | Slow-query rescue | PX cards; `slow_*.sql` | `SQL-CAP4` golden in l14 JSON |

**SQL-CAP3 spec (consistent with lab):** design checkout that cannot oversell `stock` under concurrency (`safe.sql` pattern), uses idempotency keys (`UNIQUE (tenant_id, idempotency_key)`), and records payments as ledger-friendly minor units. Deliver: DDL delta, TX evidence transcript, ADR for isolation level.

**SQL-CAP3 acceptance** (all four must hold; run on the local lab Postgres):

1. **No oversell.** Set one product's `stock.on_hand` to 1. Run the checkout from 10 concurrent sessions (`pgbench -n -c 10 -t 1 -f` with your checkout transaction as the script, or two `psql` sessions as in TX-1). Pass: exactly one new `customer_order`, `on_hand = 0`, and the other nine end cleanly ("sold out", not an error trace). The claim is one conditional `UPDATE … WHERE on_hand >= qty RETURNING` (the `safe.sql` shape), or a `SELECT … FOR UPDATE` then update (TX-8); a read-then-write without either fails.
2. **Idempotent.** Submit the same `(tenant_id, idempotency_key)` twice. Pass: one order row, and both calls return the same `order_id` (`INSERT … ON CONFLICT (tenant_id, idempotency_key) DO NOTHING RETURNING order_id`, then read the existing row when nothing returns). Stock moves once.
3. **Money in minor units.** `total_minor` equals `sum(qty * unit_price_minor)` over the order's lines (prove it with a query that returns zero mismatched orders); no `float`/`real` column anywhere in the delta.
4. **ADR.** One page naming the isolation level and why: READ COMMITTED is enough when the claim is a single conditional `UPDATE`; a check that reads several rows before writing needs SERIALIZABLE (or explicit row locks) plus a retry loop on SQLSTATE `40001`. Name the retry limit and what the customer sees when it is hit.

Evidence: the DDL delta, the transcript of tests 1–3 (commands and final `SELECT`s) and the ADR. Tutor key (after attempt): the lab schema already holds `CHECK (on_hand >= 0)` and `UNIQUE (tenant_id, idempotency_key)`, so the minimal correct delta is often just the checkout transaction itself; a submission that adds a second uniqueness table or an application-side lock has missed that.

Cards for SQL-CAP1.*, SQL-CAP2, SQL-CAP4 are in §6.14; keys in Appendix K.

## 10. Academic depth (rule 0.4.10)

The academic pass of this companion: database theory at the depth of a university databases course (CMU 15-445/645, Berkeley CS 186; main course §0.6). It is the proof layer of the cards named in each block, taught after that card's engineering pass and in the same A8 teaching block (main course A8.D1). The engine slices DB-1…DB-10 stay the build layer; this section proves why they work. Problems DBT-P1…DBT-P15 are in §10.11, with keys in Appendix K under "K-DBT" (after the attempt only). A block is `mastered` by rule 0.4.10.3. Transactions are written T₁, T₂ and operations r₁(A), w₂(B), c₁ (read, write, commit, with the transaction as subscript).

### 10.1 DBT.1 · Query languages and their equivalence (proves RT-02, RT-03, RT-08)

- The relational algebra's five basic operators (selection, projection, product, union, difference) and the derived ones (join, intersection, division), over sets and over bags (PQ-01, DB-1).
- The tuple and domain relational calculi. Safety: a calculus query is safe when its answer can be computed from the values in the database and the query (the active domain); `{t | ¬R(t)}` is unsafe.
- Codd's theorem (1972), stated with a proof sketch: the relational algebra and the safe relational calculus express exactly the same queries. Algebra to calculus is by induction on the expression; calculus to algebra builds the active domain as a union of projections and translates each connective. SQL without recursion or aggregation is "relationally complete" in this sense.
- Equivalence rules that the planner may use (RT-08), each justified from the definitions: selection pushdown σ_p(R ⋈ S) = σ_p(R) ⋈ S when p mentions only R's attributes; join commutativity and associativity; projection pushdown. Under bag semantics, some set identities fail (R ∪ R ≠ R), which is why `UNION` and `UNION ALL` differ.
- Readings: Abiteboul, Hull and Vianu, *Foundations of Databases* (1995), chapters 3–5; Silberschatz, Korth and Sudarshan, *Database System Concepts*, 7th ed. (2019), chapters 2 and 27 `(verify)`.

### 10.2 DBT.2 · Functional dependencies (proves RT-04)

- Armstrong's axioms: reflexivity (Y ⊆ X ⇒ X → Y), augmentation (X → Y ⇒ XZ → YZ), transitivity (X → Y, Y → Z ⇒ X → Z); the derived union, decomposition and pseudo-transitivity rules.
- Soundness: each axiom preserves truth in every relation instance (proved directly from the definition of an FD).
- Completeness: if F does not derive X → Y, a two-tuple instance that agrees exactly on X⁺ satisfies F and violates X → Y (proved as DBT-P3).
- The attribute-closure algorithm, its correctness (it computes exactly X⁺) and its polynomial running time. Membership (does F imply X → Y?) is tested by Y ⊆ X⁺. Candidate keys: an attribute that appears on no right-hand side is in every key.
- Canonical (minimal) cover: singleton right-hand sides, no extraneous left-hand attributes, no redundant dependency.

### 10.3 DBT.3 · Decomposition and normal forms (proves RT-05, RT-06)

- A decomposition of R into R₁ and R₂ is lossless-join if and only if R₁ ∩ R₂ → R₁ or R₁ ∩ R₂ → R₂ is in F⁺ (proof: the natural join returns exactly R in every instance satisfying F). For more than two parts, the chase test decides losslessness.
- Dependency preservation: the union of the projected dependency sets implies F.
- BCNF decomposition always terminates with a lossless decomposition but may lose a dependency; the example R(city, street, zip) with {city, street} → zip and zip → city has no dependency-preserving BCNF decomposition.
- 3NF synthesis from a canonical cover (one relation per dependency, plus a key if none contains one) is always lossless and dependency-preserving.
- Multivalued dependencies and 4NF (a relation with independent multi-valued facts about one key); join dependencies and 5NF named.
- Readings: Garcia-Molina, Ullman and Widom, *Database Systems: The Complete Book*, 2nd ed. (2008), chapter 3; Abiteboul, Hull and Vianu, chapters 8–11.

### 10.4 DBT.4 · Cost models for query processing (proves CS-01, CS-03)

- The I/O cost model: cost counted in page transfers, with B buffer pages available; CPU work named, not counted.
- External merge sort: pass 0 writes ⌈N/B⌉ sorted runs; each later pass merges B − 1 runs. Total cost 2N · (1 + ⌈log_{B−1}⌈N/B⌉⌉) I/Os, so two passes sort N pages whenever N ≤ B(B − 1).
- Joins of R (M pages) and S (N pages): simple nested loops M + (tuples of R) · N; block nested loops M + ⌈M/(B − 2)⌉ · N; index nested loops M + (tuples of R) · (cost of one probe); sort–merge about the sort costs plus M + N; Grace hash join 3(M + N) when B > √(the smaller relation's pages), with recursive partitioning otherwise.
- Aggregation by sorting or by hashing, and the same cost bounds.
- Readings: Ramakrishnan and Gehrke, *Database Management Systems*, 3rd ed. (2003), chapters 13–14; Graefe, "Query Evaluation Techniques for Large Databases", *ACM Computing Surveys* 25(2), 1993.

### 10.5 DBT.5 · Query optimization (proves CS-08, CS-10)

- The Selinger optimizer (System R, 1979): dynamic programming over subsets of relations; left-deep plans; "interesting orders" kept alongside the cheapest plan because a sorted output can make a later merge join or `ORDER BY` free.
- Cardinality estimation: selectivity of `col = const` as 1/NDV under the uniformity assumption; conjunctions multiplied under the independence assumption; histograms and most-common-value lists (DB-8). Errors compound multiplicatively through a join tree, which is why plans go wrong on correlated columns.
- Complexity: choosing the optimal join order is NP-hard in general (Ibaraki and Kameda, 1984), so optimizers use dynamic programming up to a limit and heuristics or genetic search beyond it (PostgreSQL's GEQO past `geqo_threshold`).
- Index selection as an optimization problem (CS-10): choosing a set of indexes under a storage budget to minimize workload cost is NP-hard; advisors use greedy search with the optimizer's own cost estimates.
- Reading: Selinger et al., "Access Path Selection in a Relational Database Management System" (SIGMOD 1979).

### 10.6 DBT.6 · Access methods, analysed (proves CS-02, PQ-07)

- B+ tree: with fanout F and N keys the height is ⌈log_F N⌉, so a lookup costs that many page reads (fewer with the upper levels cached). Split and merge keep every node at least half full; range scans follow the leaf chain.
- Hash indexes: static hashing and overflow chains; extendible hashing (directory doubling) and linear hashing (split one bucket at a time); expected O(1) probes when the load factor is bounded.
- LSM trees: write amplification, read amplification and space amplification trade against each other (the RUM conjecture, Athanassoulis et al., 2016); leveled versus tiered compaction; Bloom filters per run (main course A4.D6) to skip runs on point lookups.
- Readings: Comer, "The Ubiquitous B-Tree", *ACM Computing Surveys* 11(2), 1979; O'Neil, Cheng, Gawlick and O'Neil, "The Log-Structured Merge-Tree", *Acta Informatica* 33, 1996.

### 10.7 DBT.7 · Concurrency control theory (proves CS-05)

- Schedules, conflicts (two operations on the same item, from different transactions, at least one a write) and conflict equivalence. The precedence-graph theorem: a schedule is conflict-serializable if and only if its precedence graph is acyclic (DBT-P8). View serializability is broader, and testing it is NP-complete.
- Two-phase locking: every 2PL schedule is conflict-serializable, ordered by lock points (DBT-P9). Strict 2PL also gives recoverable, cascadeless schedules. Deadlock handling: detection on the waits-for graph (DB-9), or prevention by wait-die and wound-wait.
- Timestamp ordering, and the Thomas write rule (an obsolete write is ignored rather than aborting), which admits some view-serializable schedules that are not conflict-serializable.
- Multiversion concurrency and snapshot isolation: SI prevents dirty reads, non-repeatable reads and lost updates but allows write skew. Serializable snapshot isolation (Cahill, Röhm and Fekete, 2008; PostgreSQL's `SERIALIZABLE`) aborts one transaction of any "dangerous structure": two consecutive read–write antidependencies between concurrent transactions.
- The anomaly-based definitions of isolation levels and their critique: Berenson et al., "A Critique of ANSI SQL Isolation Levels" (SIGMOD 1995); Adya's graph-based definitions (PhD thesis, MIT, 1999).

### 10.8 DBT.8 · Recovery theory (proves CS-06, DB-10)

- Buffer policies: steal (a dirty page of an uncommitted transaction may be written) needs undo; no-force (committed pages need not be written at commit) needs redo. Steal/no-force is the fastest and needs both.
- The write-ahead-logging rule: a log record must be durable before the page it describes, and all of a transaction's log records must be durable before it commits.
- ARIES (Mohan et al., 1992): log sequence numbers; each page's pageLSN; the dirty-page table and transaction table in checkpoints. Recovery runs three passes. **Analysis** rebuilds both tables. **Redo** repeats history from the smallest recLSN, applying a record only when its LSN is greater than the page's pageLSN, which makes redo idempotent. **Undo** rolls back the losers, writing a compensation log record (CLR) for each step so that a crash during recovery never undoes the same step twice.
- Reading: Mohan, Haderle, Lindsay, Pirahesh and Schwarz, "ARIES: A Transaction Recovery Method…", *ACM Transactions on Database Systems* 17(1), 1992.

### 10.9 DBT.9 · Distributed transactions and consistency (proves CS-07)

- Two-phase commit, its correctness (all-or-nothing when participants follow the protocol) and its blocking window, recalled from main course A9.D8 with the database-side detail: prepared transactions hold locks until the decision arrives.
- Spanner's external consistency: commit timestamps chosen within TrueTime's uncertainty interval, and commit-wait until that interval has passed, so timestamp order matches real-time order (Corbett et al., OSDI 2012).
- Deterministic databases (Calvin, 2012) as the alternative that orders transactions before executing them, named only.
- Transactional notification (SL-10). PostgreSQL's `NOTIFY` is queued by the transaction and delivered only if it commits, so a listener never hears about a row it cannot yet see. Delivery is at most once and not durable: a session that is not listening at commit time never receives the message. The notification is therefore a hint and the queue table is the record; this is the lost-wakeup problem of condition variables (main course A6.D4), and the cure is the same: after every wake-up, and after every reconnect, re-check the state (DBT-P15).

### 10.10 DBT.10 · Recursion and expressiveness (proves CS-11, SL-09)

- First-order queries (the relational algebra) cannot express transitive closure (a consequence of the locality of first-order logic, stated without proof; Libkin, *Elements of Finite Model Theory*, 2004).
- Datalog: rules, the least fixpoint semantics, naive and semi-naive evaluation (each round joins only the new facts), and stratified negation. SQL's `WITH RECURSIVE` is linear Datalog with a union; a monotone query reaches its fixpoint in at most as many rounds as the longest shortest path.
- Readings for the whole pass: the CMU 15-445/645 and Berkeley CS 186 lecture notes; Hellerstein, Stonebraker and Hamilton, "Architecture of a Database System", *Foundations and Trends in Databases* 1(2), 2007.

### 10.11 Problem set (DBT-P1…DBT-P15)

- **DBT-P1** · proof · From Armstrong's three axioms, derive the union rule: X → Y and X → Z imply X → YZ.
- **DBT-P2** · compute · R(A, B, C, D, E) with F = {A → B, BC → D, D → E, E → A}. Compute {A, C}⁺ and list every candidate key.
- **DBT-P3** · proof · Prove completeness: if Y ⊄ X⁺ (closure under F), build a two-row instance that satisfies every dependency in F and violates X → Y.
- **DBT-P4** · compute · R(A, B, C) with F = {A → B}. Is the decomposition into (A, B) and (A, C) lossless? Is the decomposition into (A, B) and (B, C)? For the lossy one, give an instance whose join has a spurious row.
- **DBT-P5** · compute · Decompose R(A, B, C, D) with F = {A → B, B → C} into BCNF. Is the result dependency-preserving?
- **DBT-P6** · compute · Sort a file of 10,000 pages with 101 buffer pages. How many runs does pass 0 produce, how many passes are there in total, and what is the I/O cost?
- **DBT-P7** · compute · R has 1,000 pages and S has 500 pages; 102 buffer pages. Give the cost of block nested loops with S as the outer relation, and of Grace hash join. Is the buffer large enough for a two-pass hash join?
- **DBT-P8** · proof · Prove that a schedule is conflict-serializable if its precedence graph is acyclic, and not conflict-serializable if the graph has a cycle.
- **DBT-P9** · proof · Prove that every schedule produced under two-phase locking is conflict-serializable.
- **DBT-P10** · compute · Is the schedule r₁(A) w₂(A) w₂(B) c₂ r₁(B) w₁(B) c₁ conflict-serializable? Draw the precedence graph.
- **DBT-P11** · proof · Two on-call doctors each run: "if at least two doctors are on call, set my own row to off-call". Show that snapshot isolation lets both commit, leaving nobody on call, and name the structure that serializable snapshot isolation detects.
- **DBT-P12** · compute · A page on disk has pageLSN 30. During redo, ARIES meets log records for that page with LSNs 25 and 40. Which does it apply, and why is redo safe to repeat after a second crash?
- **DBT-P13** · compute · A B+ tree has fanout 200 and leaves holding 100 entries each; the table has 100,000,000 rows, one entry per row. How many levels does the tree have, and how many page reads does a lookup cost when only the root is cached?
- **DBT-P14** · compute · A table has 1,000,000 rows. Column a has 50 distinct values and column b has 10, both uniform. Estimate the rows matching `a = 1 AND b = 2` under the independence assumption, and say when the estimate fails.
- **DBT-P15** · design · Workers run `LISTEN job_ready` and, on each notification, claim one job with `SELECT … FOR UPDATE SKIP LOCKED LIMIT 1`. The producer inserts a job and runs `NOTIFY job_ready` in the same transaction. A worker's connection drops for 30 seconds while three jobs are inserted, then reconnects and runs `LISTEN` again. Which jobs does that worker learn about, and what two changes make the design correct without polling every second?

## Appendix K — Instructor keys (AFTER attempt only)

Do **not** open until the learner has attempted the item. Keys are the reference SQL from `ex_*.py` `key=` fields; fingerprints from `goldens_ex_*.json`.

### SQL-E1.1 — Q2-2024 signups from GB or DE
- **Fingerprint:** `164:d17041f6`
```sql
SELECT user_id, email
FROM lab.app_user
WHERE country IN ('GB','DE')
  AND created_at >= '2024-04-01' AND created_at < '2024-07-01'
```

### SQL-E1.2 — Unknown country
- **Fingerprint:** `181:ab2f2d8e`
```sql
SELECT user_id FROM lab.app_user WHERE country IS NULL
```

### SQL-E1.3 — Everyone not known to be in the US
- **Fingerprint:** `1740:d7106dd7`
```sql
SELECT user_id FROM lab.app_user WHERE country IS DISTINCT FROM 'US'
```

### SQL-E1.4 — Mid-priced live catalogue, top 20
- **Fingerprint:** `20:1af04ff2`
```sql
SELECT product_id, price_minor
FROM lab.product
WHERE price_minor BETWEEN 1000 AND 2000 AND discontinued_at IS NULL
ORDER BY price_minor DESC, product_id
LIMIT 20
```

### SQL-E1.5 — Reviews with no text
- **Fingerprint:** `2036:aa6dda6b`
```sql
SELECT review_id FROM lab.review WHERE coalesce(body, '') = ''
```

### SQL-E1.6 — Order status buckets
- **Fingerprint:** `20000:a58f4910`
```sql
SELECT order_id,
       CASE status WHEN 'created' THEN 'open' WHEN 'paid' THEN 'open'
                   WHEN 'fulfilled' THEN 'done'
                   WHEN 'cancelled' THEN 'closed' WHEN 'refunded' THEN 'closed'
                   ELSE 'unknown' END AS bucket
FROM lab.customer_order
```

### SQL-E1.7 — Ten priciest live products
- **Fingerprint:** `10:558e94b1`
```sql
SELECT product_id, price_minor FROM lab.product
WHERE discontinued_at IS NULL
ORDER BY price_minor DESC, product_id LIMIT 10
```

### SQL-E1.8 — Pattern search
- **Fingerprint:** `10:986cf4ec`
```sql
SELECT product_id FROM lab.product WHERE sku LIKE 'SKU-01%' AND sku LIKE '%7'
```

### SQL-E2.1 — Orders and revenue by status
- **Fingerprint:** `5:2495a69d`
```sql
SELECT status, count(*) AS n_orders, sum(total_minor) AS sum_minor FROM lab.customer_order GROUP BY status
```

### SQL-E2.2 — Monthly fulfilled GMV, 2025
- **Fingerprint:** `12:c6eb674e`
```sql
SELECT date_trunc('month', placed_at) AS month, count(*) AS n_orders, sum(total_minor) AS gmv_minor
FROM lab.customer_order
WHERE status = 'fulfilled' AND placed_at >= '2025-01-01' AND placed_at < '2026-01-01'
GROUP BY 1
```

### SQL-E2.3 — Well-reviewed products
- **Fingerprint:** `467:68a601d1`
```sql
SELECT product_id, count(*) AS n, round(avg(rating), 2) AS avg_rating
FROM lab.review GROUP BY product_id HAVING count(*) >= 10
```

### SQL-E2.4 — Buyers per tenant
- **Fingerprint:** `5:0cf3aaa2`
```sql
SELECT tenant_id, count(*) AS n_orders, count(DISTINCT user_id) AS n_buyers
FROM lab.customer_order GROUP BY tenant_id
```

### SQL-E2.5 — Refund rate by tenant
- **Fingerprint:** `5:9fbfe463`
```sql
SELECT tenant_id, count(*) AS n_orders,
       count(*) FILTER (WHERE status = 'refunded') AS n_refunded,
       round(count(*) FILTER (WHERE status = 'refunded')::numeric / count(*), 4) AS refund_rate
FROM lab.customer_order GROUP BY tenant_id
```

### SQL-E2.6 — Users by country including unknown
- **Fingerprint:** `8:94127f65`
```sql
SELECT coalesce(country, '??') AS country, count(*) AS n FROM lab.app_user GROUP BY 1
```

### SQL-E2.7 — Median order value per tenant
- **Fingerprint:** `5:74a001bd`
```sql
SELECT tenant_id, percentile_disc(0.5) WITHIN GROUP (ORDER BY total_minor) AS median_minor
FROM lab.customer_order WHERE status = 'fulfilled' GROUP BY tenant_id
```

### SQL-E2.8 — Price histogram
- **Fingerprint:** `10:dc13b2c1`
```sql
SELECT (price_minor / 1000) * 1000 AS band_start, count(*) AS n
FROM lab.product WHERE discontinued_at IS NULL GROUP BY 1
```

### SQL-E3.1 — Paid orders with buyer and tenant
- **Fingerprint:** `50:787a0b9d`
```sql
SELECT o.order_id, u.email, t.name AS tenant_name, o.total_minor
FROM lab.customer_order o
JOIN lab.app_user u ON u.user_id = o.user_id
JOIN lab.tenant   t ON t.tenant_id = o.tenant_id
WHERE o.tenant_id = 2 AND o.status = 'paid'
  AND o.placed_at >= '2025-03-01' AND o.placed_at < '2025-04-01'
```

### SQL-E3.2 — Users who never referred anyone
- **Fingerprint:** `1291:ce8f0411`
```sql
SELECT u.user_id FROM lab.app_user u
WHERE NOT EXISTS (SELECT 1 FROM lab.app_user r WHERE r.referred_by = u.user_id)
```

### SQL-E3.3 — Users who never ordered
- **Fingerprint:** `200:e5ab3ae1`
```sql
SELECT u.user_id FROM lab.app_user u
LEFT JOIN lab.customer_order o ON o.user_id = u.user_id
WHERE o.order_id IS NULL
```

### SQL-E3.4 — Products not sold in a week
- **Fingerprint:** `180:d18c224e`
```sql
SELECT p.product_id FROM lab.product p
WHERE NOT EXISTS (
  SELECT 1 FROM lab.order_line l JOIN lab.customer_order o USING (order_id)
  WHERE l.product_id = p.product_id AND o.status = 'fulfilled'
    AND o.placed_at >= '2025-01-01' AND o.placed_at < '2025-01-08')
```

### SQL-E3.5 — Revenue of delivered orders
- **Fingerprint:** `1:6c39466d`
```sql
SELECT sum(o.total_minor) AS revenue_minor FROM lab.customer_order o
WHERE o.status = 'fulfilled'
  AND EXISTS (SELECT 1 FROM lab.shipment s WHERE s.order_id = o.order_id AND s.delivered_at IS NOT NULL)
```

### SQL-E3.6 — Cross-tenant referrals
- **Fingerprint:** `1172:9f8ebbd0`
```sql
SELECT u.user_id, r.user_id AS referrer_id
FROM lab.app_user u JOIN lab.app_user r ON r.user_id = u.referred_by
WHERE r.tenant_id <> u.tenant_id
```

### SQL-E3.7 — One-star counts including zeros
- **Fingerprint:** `100:1b05fa94`
```sql
SELECT p.product_id, count(r.review_id) AS one_star
FROM lab.product p LEFT JOIN lab.review r ON r.product_id = p.product_id AND r.rating = 1
WHERE p.tenant_id = 1 GROUP BY p.product_id
```

### SQL-E3.8 — Who ordered vs who reviewed (Q1 2025)
- **Fingerprint:** `1845:6f7a9372`
```sql
WITH o AS (SELECT DISTINCT user_id FROM lab.customer_order WHERE placed_at >= '2025-01-01' AND placed_at < '2025-04-01'),
     r AS (SELECT DISTINCT user_id FROM lab.review WHERE created_at >= '2025-01-01' AND created_at < '2025-04-01')
SELECT coalesce(o.user_id, r.user_id) AS user_id, o.user_id IS NOT NULL AS ordered, r.user_id IS NOT NULL AS reviewed
FROM o FULL JOIN r ON r.user_id = o.user_id
```

### SQL-E3.9 — Deletions per month with zero-fill
- **Fingerprint:** `14:cb9ff4e8`
```sql
SELECT m::date AS month, count(u.user_id) AS n_deleted
FROM generate_series('2024-05-01'::date, '2025-06-01'::date, interval '1 month') m
LEFT JOIN lab.app_user u ON date_trunc('month', u.deleted_at) = m
GROUP BY m
```

### SQL-E3.10 — Duplicate-safe reviewers per product
- **Fingerprint:** `241:47e3b13f`
```sql
SELECT product_id, count(DISTINCT user_id) AS n_reviewers, count(*) AS n_reviews
FROM lab.review GROUP BY product_id HAVING count(DISTINCT user_id) <> count(*)
```

### SQL-E4.1 — Above-average spenders
- **Fingerprint:** `675:19348832`
```sql
WITH s AS (SELECT user_id, sum(total_minor) AS spend_minor FROM lab.customer_order WHERE status = 'fulfilled' GROUP BY user_id)
SELECT user_id, spend_minor FROM s WHERE spend_minor > (SELECT avg(spend_minor) FROM s)
```

### SQL-E4.2 — Latest review rating per product
- **Fingerprint:** `500:7463fec9`
```sql
SELECT DISTINCT ON (product_id) product_id, rating
FROM lab.review ORDER BY product_id, created_at DESC, review_id DESC
```

### SQL-E4.3 — Both fulfilled and refunded
- **Fingerprint:** `391:6319def9`
```sql
SELECT user_id FROM lab.customer_order WHERE status = 'fulfilled'
INTERSECT
SELECT user_id FROM lab.customer_order WHERE status = 'refunded'
```

### SQL-E4.4 — Reviewed but never bought
- **Fingerprint:** `4559:2e92d1fa`
```sql
SELECT user_id, product_id FROM lab.review
EXCEPT
SELECT o.user_id, l.product_id FROM lab.customer_order o JOIN lab.order_line l USING (order_id)
```

### SQL-E4.5 — Net revenue per tenant without double counting
- **Fingerprint:** `5:77344493`
```sql
WITH g AS (
  SELECT tenant_id, sum(total_minor) AS gmv_minor FROM lab.customer_order
  WHERE status IN ('fulfilled','refunded') AND placed_at >= '2025-01-01' AND placed_at < '2026-01-01' GROUP BY tenant_id),
r AS (
  SELECT o.tenant_id, sum(p.amount_minor) AS refunded_minor
  FROM lab.payment p JOIN lab.customer_order o USING (order_id)
  WHERE p.kind = 'refund' AND p.status = 'succeeded' AND o.status IN ('fulfilled','refunded')
    AND o.placed_at >= '2025-01-01' AND o.placed_at < '2026-01-01' GROUP BY o.tenant_id)
SELECT g.tenant_id, g.gmv_minor, coalesce(r.refunded_minor, 0) AS refunded_minor,
       g.gmv_minor - coalesce(r.refunded_minor, 0) AS net_minor
FROM g LEFT JOIN r USING (tenant_id)
```

### SQL-E4.6 — Strictly the priciest in its category
- **Fingerprint:** `30:d5ca9e54`
```sql
SELECT p.product_id FROM lab.product p
WHERE p.category_id IS NOT NULL
  AND p.price_minor > ALL (SELECT q.price_minor FROM lab.product q
                           WHERE q.category_id = p.category_id AND q.product_id <> p.product_id)
```

### SQL-E4.7 — Latest order per user (tenant 3)
- **Fingerprint:** `360:3dd4aace`
```sql
SELECT u.user_id, o.order_id, o.placed_at
FROM lab.app_user u
CROSS JOIN LATERAL (SELECT order_id, placed_at FROM lab.customer_order c WHERE c.user_id = u.user_id
                    ORDER BY placed_at DESC, order_id DESC LIMIT 1) o
WHERE u.tenant_id = 3
```

### SQL-E4.8 — Relational division: bought all three
- **Fingerprint:** `5:286c82f6`
```sql
SELECT o.user_id FROM lab.customer_order o JOIN lab.order_line l USING (order_id)
WHERE l.product_id IN (1, 6, 11)
GROUP BY o.user_id HAVING count(DISTINCT l.product_id) = 3
```

### SQL-E5.1 — Top-3 price ranks per category
- **Fingerprint:** `90:0444fd32`
```sql
SELECT category_id, product_id, price_minor, rnk FROM (
  SELECT category_id, product_id, price_minor,
         dense_rank() OVER (PARTITION BY category_id ORDER BY price_minor DESC) AS rnk
  FROM lab.product WHERE category_id IS NOT NULL) x
WHERE rnk <= 3
```

### SQL-E5.2 — Running GMV, tenant 1, March 2025
- **Fingerprint:** `31:1c8f130e`
```sql
WITH d AS (SELECT placed_at::date AS day, sum(total_minor) AS gmv_minor FROM lab.customer_order
            WHERE tenant_id = 1 AND status = 'fulfilled' AND placed_at >= '2025-03-01' AND placed_at < '2025-04-01' GROUP BY 1)
SELECT day, gmv_minor, sum(gmv_minor) OVER (ORDER BY day ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cum_gmv_minor
FROM d ORDER BY day
```

### SQL-E5.3 — Days since the previous order
- **Fingerprint:** `996:d7137b70`
```sql
SELECT user_id, order_id, placed_at,
       placed_at::date - lag(placed_at::date) OVER (PARTITION BY user_id ORDER BY placed_at, order_id) AS gap_days
FROM lab.customer_order WHERE user_id BETWEEN 1 AND 20
```

### SQL-E5.4 — Top-2 orders per user
- **Fingerprint:** `100:8a1679d3`
```sql
SELECT user_id, order_id, total_minor, rn FROM (
  SELECT user_id, order_id, total_minor,
         row_number() OVER (PARTITION BY user_id ORDER BY total_minor DESC, order_id) AS rn
  FROM lab.customer_order WHERE user_id BETWEEN 1 AND 50) x WHERE rn <= 2
```

### SQL-E5.5 — Tenant share of 2025 GMV
- **Fingerprint:** `5:4bec02c5`
```sql
SELECT tenant_id, sum(total_minor) AS gmv_minor,
       round(100.0 * sum(total_minor) / sum(sum(total_minor)) OVER (), 2) AS pct
FROM lab.customer_order
WHERE status = 'fulfilled' AND placed_at >= '2025-01-01' AND placed_at < '2026-01-01'
GROUP BY tenant_id
```

### SQL-E5.6 — Price quartiles, tenant 2
- **Fingerprint:** `94:71892706`
```sql
SELECT product_id, price_minor, ntile(4) OVER (ORDER BY price_minor, product_id) AS quartile
FROM lab.product WHERE tenant_id = 2 AND discontinued_at IS NULL
```

### SQL-E5.7 — First and last price
- **Fingerprint:** `20:7ddcb09e`
```sql
SELECT DISTINCT product_id,
       first_value(price_minor) OVER w AS first_price,
       last_value(price_minor)  OVER w AS last_price,
       last_value(price_minor) OVER w - first_value(price_minor) OVER w AS delta
FROM lab.product_price_history WHERE product_id BETWEEN 1 AND 20
WINDOW w AS (PARTITION BY product_id ORDER BY valid_from ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
```

### SQL-E5.8 — 7-day moving average of daily orders
- **Fingerprint:** `22:55be0551`
```sql
SELECT day, n, avg7 FROM (
  SELECT day, n, row_number() OVER (ORDER BY day) AS rn,
         round(avg(n) OVER (ORDER BY day ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS avg7
  FROM (SELECT placed_at::date AS day, count(*) AS n FROM lab.customer_order
        WHERE tenant_id = 2 AND placed_at >= '2025-02-01' AND placed_at < '2025-03-01' GROUP BY 1) d) x
WHERE rn >= 7 ORDER BY day
```

### SQL-E6.1 — Longest login streak
- **Fingerprint:** `200:3d4d4f51`
```sql
WITH g AS (SELECT user_id, day, day - (row_number() OVER (PARTITION BY user_id ORDER BY day))::int AS grp FROM lab.login_day),
runs AS (SELECT user_id, min(day) AS streak_start, count(*) AS streak_len FROM g GROUP BY user_id, grp),
ranked AS (SELECT *, row_number() OVER (PARTITION BY user_id ORDER BY streak_len DESC, streak_start) AS rn FROM runs)
SELECT user_id, streak_len, streak_start FROM ranked WHERE rn = 1
```

### SQL-E6.2 — Sessionise the event stream
- **Fingerprint:** `7500:311fb683`
```sql
WITH e AS (SELECT user_id, event_id, occurred_at,
                   occurred_at - lag(occurred_at) OVER (PARTITION BY user_id ORDER BY occurred_at, event_id) AS gap
            FROM lab.event WHERE user_id IS NOT NULL),
f AS (SELECT *, CASE WHEN gap IS NULL OR gap > interval '30 minutes' THEN 1 ELSE 0 END AS is_start FROM e),
s AS (SELECT *, sum(is_start) OVER (PARTITION BY user_id ORDER BY occurred_at, event_id) AS session_no FROM f)
SELECT user_id, session_no, count(*) AS n_events, min(occurred_at) AS started_at, max(occurred_at) AS ended_at
FROM s GROUP BY user_id, session_no
```

### SQL-E6.3 — Ordered funnel
- **Fingerprint:** `1:2f3673b3`
```sql
WITH t AS (SELECT user_id,
       min(occurred_at) FILTER (WHERE event_type = 'add_to_cart')    AS t_cart,
       min(occurred_at) FILTER (WHERE event_type = 'checkout_start') AS t_co,
       min(occurred_at) FILTER (WHERE event_type = 'purchase')       AS t_buy
     FROM lab.event WHERE user_id IS NOT NULL GROUP BY user_id)
SELECT count(*) FILTER (WHERE t_cart IS NOT NULL) AS n_cart,
       count(*) FILTER (WHERE t_cart < t_co) AS n_checkout,
       count(*) FILTER (WHERE t_cart < t_co AND t_co < t_buy) AS n_purchase
FROM t
```

### SQL-E6.4 — Price in effect at order time (as-of join)
- **Fingerprint:** `404:4f5a2a10`
```sql
SELECT l.order_id, l.line_no, l.unit_price_minor, h.price_minor AS price_at_order
FROM lab.order_line l JOIN lab.customer_order o USING (order_id)
CROSS JOIN LATERAL (SELECT price_minor FROM lab.product_price_history h
                    WHERE h.product_id = l.product_id AND h.valid_from <= o.placed_at
                    ORDER BY h.valid_from DESC LIMIT 1) h
WHERE o.placed_at < '2025-01-04' AND l.unit_price_minor <> h.price_minor
```

### SQL-E6.5 — Orders in the previous 30 days
- **Fingerprint:** `996:7e7490f1`
```sql
SELECT user_id, order_id,
       (count(*) OVER (PARTITION BY user_id ORDER BY placed_at RANGE BETWEEN INTERVAL '30 days' PRECEDING AND CURRENT ROW) - 1) AS prior_30d
FROM lab.customer_order WHERE user_id BETWEEN 1 AND 20
```

### SQL-E6.6 — Signup-cohort activation
- **Fingerprint:** `10:79a8b3a1`
```sql
SELECT date_trunc('month', u.created_at)::date AS cohort_month, count(*) AS size,
       count(*) FILTER (WHERE EXISTS (
          SELECT 1 FROM lab.customer_order o WHERE o.user_id = u.user_id
            AND o.placed_at >= date_trunc('month', u.created_at) + interval '1 month'
            AND o.placed_at <  date_trunc('month', u.created_at) + interval '2 months')) AS active_next_month
FROM lab.app_user u GROUP BY 1
```

### SQL-E6.7 — Dedupe events, keep the first
- **Fingerprint:** `6000:a46392ec`
```sql
SELECT event_id FROM (
  SELECT event_id, row_number() OVER (PARTITION BY user_id, event_type, occurred_at ORDER BY event_id) AS rn
  FROM (SELECT * FROM lab.event UNION ALL
        SELECT event_id + 1000000, tenant_id, user_id, event_type, occurred_at, payload FROM lab.event WHERE event_id % 10 = 0) e) x
WHERE rn > 1
```

### SQL-E7.1 — Category paths
- **Fingerprint:** `10:82a25fd0`
```sql
WITH RECURSIVE t AS (
  SELECT category_id, 0 AS depth, name::text AS path FROM lab.category WHERE tenant_id = 1 AND parent_id IS NULL
  UNION ALL
  SELECT c.category_id, t.depth + 1, t.path || ' > ' || c.name
  FROM lab.category c JOIN t ON c.parent_id = t.category_id)
SELECT category_id, depth, path FROM t
```

### SQL-E7.2 — Products in a subtree
- **Fingerprint:** `10:13320b85`
```sql
WITH RECURSIVE a AS (
  SELECT category_id AS anc, category_id AS des FROM lab.category WHERE tenant_id = 1
  UNION ALL
  SELECT a.anc, c.category_id FROM a JOIN lab.category c ON c.parent_id = a.des)
SELECT a.anc AS category_id, count(p.product_id) AS subtree_products
FROM a LEFT JOIN lab.product p ON p.category_id = a.des GROUP BY a.anc
```

### SQL-E7.3 — Referral roots and depth
- **Fingerprint:** `2000:97e6e0a2`
```sql
WITH RECURSIVE f AS (
  SELECT user_id, user_id AS root_id, 0 AS depth FROM lab.app_user WHERE referred_by IS NULL
  UNION ALL
  SELECT u.user_id, f.root_id, f.depth + 1 FROM lab.app_user u JOIN f ON u.referred_by = f.user_id)
SELECT user_id, root_id, depth FROM f
```

### SQL-E7.4 — Biggest referral tree
- **Fingerprint:** `1:36a7110f`
```sql
WITH RECURSIVE f AS (
  SELECT user_id, user_id AS root_id FROM lab.app_user WHERE referred_by IS NULL
  UNION ALL SELECT u.user_id, f.root_id FROM lab.app_user u JOIN f ON u.referred_by = f.user_id)
SELECT root_id, count(*) AS tree_size FROM f GROUP BY root_id ORDER BY tree_size DESC, root_id LIMIT 1
```

### SQL-E7.5 — Find the cycle
- **Fingerprint:** `3:62171a21`
```sql
WITH RECURSIVE e(a, b) AS (VALUES (1,2),(2,3),(3,1),(4,5),(5,6)),
w AS (
  SELECT a AS start, b AS node, ARRAY[a, b] AS path FROM e
  UNION ALL
  SELECT w.start, e.b, w.path || e.b FROM w JOIN e ON e.a = w.node WHERE e.b <> ALL (w.path[2:]))
SELECT DISTINCT start AS node FROM w WHERE node = start
```

### SQL-E8.1 — Average delivery time by carrier
- **Fingerprint:** `3:72b2a44b`
```sql
SELECT carrier, count(*) AS n,
       round(avg(extract(epoch FROM (delivered_at - shipped_at)) / 86400)::numeric, 2) AS avg_days
FROM lab.shipment WHERE delivered_at IS NOT NULL GROUP BY carrier
```

### SQL-E8.2 — Stuck shipments as of a fixed instant
- **Fingerprint:** `1825:dc65c0f1`
```sql
SELECT shipment_id FROM lab.shipment
WHERE delivered_at IS NULL AND shipped_at < timestamptz '2026-01-01 00:00+00' - interval '14 days'
```

### SQL-E8.3 — UTC day vs New York day
- **Fingerprint:** `1:f10d5c9a`
```sql
SELECT count(*) AS n FROM lab.customer_order
WHERE (placed_at AT TIME ZONE 'America/New_York')::date <> (placed_at AT TIME ZONE 'UTC')::date
```

### SQL-E8.4 — Orders per ISO week
- **Fingerprint:** `53:15bc9aa0`
```sql
SELECT date_trunc('week', placed_at)::date AS week_start, count(*) AS n
FROM lab.customer_order WHERE placed_at >= '2025-01-01' AND placed_at < '2026-01-01' GROUP BY 1
```

### SQL-E8.5 — Red eco products
- **Fingerprint:** `41:a5be7c78`
```sql
SELECT product_id FROM lab.product WHERE attrs @> '{"color":"red"}' AND attrs->'tags' ? 'eco'
```

### SQL-E8.6 — Search latency by query term
- **Fingerprint:** `4:eaf94d2b`
```sql
SELECT payload->>'q' AS q, count(*) AS n, round(avg((payload->>'ms')::int), 1) AS avg_ms
FROM lab.event WHERE event_type = 'search' GROUP BY 1
```

### SQL-E8.7 — Products per tag
- **Fingerprint:** `2:71943e30`
```sql
SELECT tag, count(*) AS n FROM lab.product p
CROSS JOIN LATERAL jsonb_array_elements_text(p.attrs->'tags') AS tag GROUP BY tag
```

### SQL-E8.8 — Clean and dedupe emails
- **Fingerprint:** `8:4fc20676`
```sql
SELECT row_id, email_norm FROM (
  SELECT row_id, lower(trim(email_text)) AS email_norm,
         row_number() OVER (PARTITION BY lower(trim(email_text)) ORDER BY row_id) AS rn
  FROM lab.stg_import
  WHERE lower(trim(email_text)) ~ '^[^@\s]+@[^@\s]+\.[^@\s]+$') x
WHERE rn = 1
```

### SQL-E8.9 — Parse money text into minor units
- **Fingerprint:** `15:bafc9e47`
```sql
SELECT row_id,
  CASE WHEN c ~ '^-?([0-9]{1,3}(,[0-9]{3})+|[0-9]+)(\.[0-9]+)?$'
       THEN round(replace(c, ',', '')::numeric * 100)::bigint END AS amount_minor
FROM (SELECT row_id, replace(trim(amount_text), '$', '') AS c FROM lab.stg_import) s
```

### SQL-E8.10 — Write a total date parser
- **Fingerprint:** `15:3eed39e7`
```sql
-- function body as in the setup above; then:
SELECT row_id, work.try_date(signup_text) AS d FROM lab.stg_import
```

### SQL-E9.1 — Materialise a daily GMV table
- **Fingerprint:** `155:9a2d7927`
```sql
CREATE TABLE work.tenant_daily_gmv (tenant_id int, day date, gmv_minor bigint NOT NULL, PRIMARY KEY (tenant_id, day));
INSERT INTO work.tenant_daily_gmv (tenant_id, day, gmv_minor)
SELECT tenant_id, placed_at::date, sum(total_minor) FROM lab.customer_order
WHERE status = 'fulfilled' AND placed_at >= '2025-01-01' AND placed_at < '2025-02-01' GROUP BY 1, 2;
```

### SQL-E9.2 — Repair corrupted totals
- **Fingerprint:** `20000:12518931`
```sql
UPDATE work.o o SET total_minor = s.t
FROM (SELECT order_id, sum(qty::bigint * unit_price_minor) AS t FROM lab.order_line GROUP BY order_id) s
WHERE s.order_id = o.order_id AND o.total_minor IS DISTINCT FROM s.t;
```

### SQL-E9.3 — Idempotent daily load (upsert)
- **Fingerprint:** `365:60b9c8d0`
```sql
INSERT INTO work.daily_orders (day, n)
SELECT placed_at::date, count(*) FROM lab.customer_order GROUP BY 1
ON CONFLICT (day) DO UPDATE SET n = EXCLUDED.n;
```

### SQL-E9.4 — Delete the double-submitted reviews
- **Fingerprint:** `6000:bc58a9d4`
```sql
DELETE FROM work.r a USING work.r b
WHERE a.product_id = b.product_id AND a.user_id = b.user_id AND a.review_id < b.review_id;
```

### SQL-E9.5 — Sync stock with MERGE
- **Fingerprint:** `11:61ddd589`
```sql
MERGE INTO work.stock_t t USING work.stock_feed f ON t.product_id = f.product_id
WHEN MATCHED AND f.on_hand = 0 THEN DELETE
WHEN MATCHED THEN UPDATE SET on_hand = f.on_hand
WHEN NOT MATCHED THEN INSERT (product_id, on_hand) VALUES (f.product_id, f.on_hand);
```

### SQL-E9.6 — Chunked backfill
- **Fingerprint:** `20000:f913007e`
```sql
DO $$ DECLARE n int; BEGIN
  LOOP
    WITH c AS (SELECT order_id FROM work.o WHERE total_major IS NULL ORDER BY order_id LIMIT 1000 FOR UPDATE SKIP LOCKED)
    UPDATE work.o o SET total_major = o.total_minor / 100.0 FROM c WHERE o.order_id = c.order_id;
    GET DIAGNOSTICS n = ROW_COUNT;
    EXIT WHEN n = 0;
  END LOOP;
END $$;
```

### SQL-E9.7 — Archive refunded orders atomically
- **Fingerprint:** `1:06897331`
```sql
WITH moved AS (DELETE FROM work.o WHERE status = 'refunded' RETURNING *)
INSERT INTO work.o_archive SELECT * FROM moved;
```

### SQL-E10.1 — Coupon table: constraints as a specification
- **Fingerprint:** `8:e5c729de`
```sql
CREATE TABLE work.coupon (
  coupon_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  code text NOT NULL,
  percent_off int CHECK (percent_off BETWEEN 1 AND 100),
  amount_off_minor int CHECK (amount_off_minor > 0),
  valid_from date, valid_until date,
  CHECK (num_nonnulls(percent_off, amount_off_minor) = 1),
  CHECK (valid_until IS NULL OR valid_from IS NULL OR valid_from < valid_until));
CREATE UNIQUE INDEX coupon_code_ci ON work.coupon (lower(code));
```

### SQL-E10.2 — Tenant-safe foreign key
- **Fingerprint:** `4:8c4ee581`
```sql
CREATE TABLE work.note (note_id bigint PRIMARY KEY, tenant_id int NOT NULL, user_id bigint NOT NULL, body text,
  FOREIGN KEY (tenant_id, user_id) REFERENCES lab.app_user (tenant_id, user_id));
```

### SQL-E10.3 — One active subscription per user
- **Fingerprint:** `5:7a0a9605`
```sql
CREATE UNIQUE INDEX one_active ON work.subscription (user_id) WHERE status = 'active';
```

### SQL-E10.4 — No overlapping price validity
- **Fingerprint:** `5:a6c6c4a9`
```sql
CREATE EXTENSION IF NOT EXISTS btree_gist;
CREATE TABLE work.price_period (product_id bigint NOT NULL, during daterange NOT NULL, price_minor int NOT NULL,
  EXCLUDE USING gist (product_id WITH =, during WITH &&));
```

### SQL-E10.5 — Circular references with DEFERRABLE
- **Fingerprint:** `1:fb0ce7c2`
```sql
ALTER TABLE work.a ADD FOREIGN KEY (b_id) REFERENCES work.b (id) DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE work.b ADD FOREIGN KEY (a_id) REFERENCES work.a (id) DEFERRABLE INITIALLY DEFERRED;
```

### SQL-E10.6 — Row-level security by tenant
- **Fingerprint:** `1:86599c11`
```sql
ALTER TABLE work.o ENABLE ROW LEVEL SECURITY;
CREATE POLICY tenant_iso ON work.o USING (tenant_id = current_setting('app.tenant_id', true)::int);
-- as the app role:  SET LOCAL app.tenant_id = '2';  SELECT tenant_id, count(*) FROM work.o GROUP BY 1;
```

### SQL-E13.1 — Subtotals with ROLLUP
- **Fingerprint:** `11:bbcd158f`
```sql
SELECT tenant_id, currency, sum(total_minor) AS gmv_minor,
       CASE GROUPING(tenant_id, currency) WHEN 0 THEN 'detail' WHEN 1 THEN 'tenant' ELSE 'grand' END AS level
FROM lab.customer_order
WHERE status = 'fulfilled' AND placed_at >= '2025-01-01' AND placed_at < '2026-01-01'
GROUP BY ROLLUP (tenant_id, currency)
```

### SQL-E13.2 — Pivot statuses into columns
- **Fingerprint:** `5:f64390e3`
```sql
SELECT tenant_id,
  count(*) FILTER (WHERE status='created') AS created, count(*) FILTER (WHERE status='paid') AS paid,
  count(*) FILTER (WHERE status='fulfilled') AS fulfilled, count(*) FILTER (WHERE status='refunded') AS refunded,
  count(*) FILTER (WHERE status='cancelled') AS cancelled
FROM lab.customer_order WHERE placed_at >= '2025-01-01' AND placed_at < '2026-01-01' GROUP BY tenant_id
```

### SQL-E13.3 — Build a star schema
- **Fingerprint:** `372:22383318`
```sql
-- DDL as in the setup above, then:
SELECT p.category_name, d.month, sum(f.revenue_minor) AS revenue_minor
FROM work.fact_sales f JOIN work.dim_product p USING (product_id) JOIN work.dim_date d USING (date_key) GROUP BY 1, 2
```

### SQL-E13.4 — Price history as a Type-2 dimension
- **Fingerprint:** `30:12ca6f21`
```sql
SELECT product_id, price_minor, valid_from,
       lead(valid_from) OVER (PARTITION BY product_id ORDER BY valid_from) AS valid_to,
       lead(valid_from) OVER (PARTITION BY product_id ORDER BY valid_from) IS NULL AS is_current
FROM lab.product_price_history WHERE product_id BETWEEN 1 AND 10
```

### SQL-E13.5 — Revenue at the price in effect
- **Fingerprint:** `5:7656600a`
```sql
WITH h AS (SELECT product_id, price_minor, valid_from,
                     lead(valid_from) OVER (PARTITION BY product_id ORDER BY valid_from) AS valid_to
              FROM lab.product_price_history)
SELECT o.tenant_id, sum(l.qty::bigint * (h.price_minor - l.unit_price_minor)) AS price_gap_minor
FROM lab.order_line l JOIN lab.customer_order o USING (order_id)
JOIN h ON h.product_id = l.product_id AND h.valid_from <= o.placed_at AND (h.valid_to IS NULL OR o.placed_at < h.valid_to)
WHERE o.status = 'fulfilled' AND o.placed_at >= '2025-01-01' AND o.placed_at < '2025-02-01'
GROUP BY o.tenant_id
```

### SQL-CAP1.1 — Order total ≠ sum of its lines
- **Fingerprint:** `3:7cc530bb`
```sql
SELECT o.order_id FROM audit.o o JOIN (SELECT order_id, sum(qty::bigint * unit_price_minor) AS s FROM audit.l GROUP BY order_id) x USING (order_id) WHERE o.total_minor <> x.s
```

### SQL-CAP1.2 — Order lines with no order (orphans)
- **Fingerprint:** `1:ec2bf809`
```sql
SELECT l.order_id, l.line_no FROM audit.l l WHERE NOT EXISTS (SELECT 1 FROM audit.o o WHERE o.order_id = l.order_id)
```

### SQL-CAP1.3 — Paid/fulfilled/refunded order with no succeeded charge
- **Fingerprint:** `2:addb7d1b`
```sql
SELECT o.order_id FROM audit.o o WHERE o.status IN ('paid','fulfilled','refunded') AND NOT EXISTS (SELECT 1 FROM audit.p p WHERE p.order_id = o.order_id AND p.kind = 'charge' AND p.status = 'succeeded')
```

### SQL-CAP1.4 — Refunds exceed charges
- **Fingerprint:** `2:23dae8cd`
```sql
SELECT order_id FROM audit.p GROUP BY order_id HAVING coalesce(sum(amount_minor) FILTER (WHERE kind='refund' AND status='succeeded'),0) > coalesce(sum(amount_minor) FILTER (WHERE kind='charge' AND status='succeeded'),0)
```

### SQL-CAP1.5 — Reserved stock above on-hand
- **Fingerprint:** `2:cc6c5a8d`
```sql
SELECT product_id FROM audit.st WHERE reserved > on_hand
```

### SQL-CAP1.6 — Duplicate idempotency keys within a tenant
- **Fingerprint:** `1:3402ab9a`
```sql
SELECT tenant_id, idempotency_key, count(*) AS n FROM audit.o WHERE idempotency_key IS NOT NULL GROUP BY 1, 2 HAVING count(*) > 1
```

### SQL-CAP1.7 — Delivered before shipped
- **Fingerprint:** `2:b713c027`
```sql
SELECT shipment_id FROM audit.sh WHERE delivered_at < shipped_at
```

### SQL-CAP1.8 — Fulfilled order with no shipment
- **Fingerprint:** `2:7bd384d1`
```sql
SELECT o.order_id FROM audit.o o WHERE o.status = 'fulfilled' AND NOT EXISTS (SELECT 1 FROM audit.sh s WHERE s.order_id = o.order_id)
```

### SQL-CAP2 — Cash-basis monthly revenue report
- **Fingerprint:** `65:b63b5f6f`
```sql
SELECT o.tenant_id, date_trunc('month', p.created_at)::date AS month,
       coalesce(sum(p.amount_minor) FILTER (WHERE p.kind = 'charge' AND p.status = 'succeeded'), 0) AS charged_minor,
       coalesce(sum(p.amount_minor) FILTER (WHERE p.kind = 'refund' AND p.status = 'succeeded'), 0) AS refunded_minor,
       coalesce(sum(p.amount_minor) FILTER (WHERE p.kind = 'charge' AND p.status = 'succeeded'), 0)
     - coalesce(sum(p.amount_minor) FILTER (WHERE p.kind = 'refund' AND p.status = 'succeeded'), 0) AS net_minor
FROM lab.payment p JOIN lab.customer_order o USING (order_id)
GROUP BY 1, 2
```

### SQL-CAP4 — Explain and fix the slow query
- **Fingerprint:** `250:eb4c8d2a`
```sql
WITH fp AS (SELECT user_id, min(occurred_at) AS t FROM lab.event WHERE event_type = 'purchase' AND user_id IS NOT NULL GROUP BY user_id)
SELECT fp.user_id, count(e.event_id) AS views_24h
FROM fp LEFT JOIN lab.event e
  ON e.user_id = fp.user_id AND e.event_type = 'page_view' AND e.occurred_at < fp.t AND e.occurred_at >= fp.t - interval '24 hours'
GROUP BY fp.user_id
```

### SQL-Z0 / TD sketch keys

- **SQL-Z0.4:** `country<>'US'` is UNKNOWN when country IS NULL; include NULLs via `IS DISTINCT FROM`.

- **TD-8:** dirty read = read uncommitted write; lost update = two RMW; forbidden by RR/SI for the latter with atomic update or FOR UPDATE.

- **TD-12:** no-force ⇒ dirty pages may be unwritten ⇒ redo from last checkpoint; steal ⇒ loser tx may have written ⇒ undo.

- **TX expected finals:** see §6.T `Expected` lines.
### K-DBT — academic problem keys (§10.11)

- **DBT-P1** — Expected: augment X → Y by X to get X → XY; augment X → Z by Y to get XY → YZ; transitivity gives X → YZ. · Wrong: "union is an axiom" — it is derived, and the exercise is the derivation.
- **DBT-P2** — Expected: {A, C}⁺ = {A, C, B, D, E} (A → B, then BC → D, then D → E). C is on no right-hand side, so every key contains C, and {C}⁺ = {C}. Adding any one of A, B, D or E to C reaches all five attributes, so the candidate keys are AC, BC, CD and CE. · Wrong: "A is a key" — A⁺ = {A, B} never reaches C.
- **DBT-P3** — Expected: take two rows that agree on every attribute of X⁺ and differ on all others. For any V → W in F: if V ⊆ X⁺ then W ⊆ X⁺ (X⁺ is closed under F), so the rows agree on W; if V ⊄ X⁺ they disagree on V, and the dependency holds vacuously. Y has an attribute outside X⁺, so the rows agree on X but differ on Y: X → Y fails. · Wrong: using a one-row instance — every FD holds on one row.
- **DBT-P4** — Expected: (A, B) and (A, C): the common attribute A determines AB, so the decomposition is lossless. (A, B) and (B, C): B determines neither side, so it is lossy; the instance {(1, x, 2), (3, x, 4)} joins back to include (1, x, 4) and (3, x, 2). · Wrong: "every decomposition that keeps all attributes is lossless" — the join can add rows.
- **DBT-P5** — Expected: the only key is AD. A → B violates BCNF; split on A⁺ = {A, B, C} into R₁(A, B, C) and R₂(A, D). In R₁, B → C violates BCNF (B is not a key of R₁); split into (B, C) and (A, B). Result: (A, B), (B, C), (A, D). Both dependencies are inside one relation, so it is dependency-preserving. · Wrong: stopping at (A, B, C) and (A, D) — R₁ still has the transitive B → C.
- **DBT-P6** — Expected: pass 0 gives ⌈10,000 / 101⌉ = 100 runs; one merge pass with fan-in 100 finishes, so 2 passes; cost 2 × 10,000 × 2 = 40,000 I/Os. · Wrong: 1 + ⌈log₂ 100⌉ = 8 passes — that is a two-way merge, which ignores the 100-way fan-in the buffer allows.
- **DBT-P7** — Expected: block nested loops with S outer: 500 + ⌈500 / 100⌉ × 1,000 = 500 + 5,000 = 5,500 I/Os. Grace hash join: 3 × (1,000 + 500) = 4,500 I/Os; it needs B > √500 ≈ 22.4, and 102 pages suffice. · Wrong: 500 × 1,000 = 500,000 — that is page-at-a-time nested loops, ignoring the buffer.
- **DBT-P8** — Expected: acyclic ⇒ take a topological order of the graph; every conflicting pair already appears in that order, so swapping adjacent non-conflicting operations turns the schedule into that serial schedule without changing any conflict's order. Cycle T₁ → T₂ → … → T₁ ⇒ an equivalent serial schedule must put each transaction before the next along the cycle, including T₁ before itself: impossible. · Wrong: "acyclic means no conflicts" — the graph's edges are the conflicts.
- **DBT-P9** — Expected: each transaction's lock point is the moment it takes its last lock. An edge Tᵢ → Tⱼ means Tᵢ released a lock that Tⱼ later acquired, so lp(Tᵢ) < lp(Tⱼ). A cycle would give lp(T₁) < … < lp(T₁), a contradiction, so the graph is acyclic and the precedence-graph theorem applies. · Wrong: "2PL prevents deadlock" — it does not; it guarantees serializability.
- **DBT-P10** — Expected: r₁(A) before w₂(A) gives T₁ → T₂; w₂(B) before r₁(B) gives T₂ → T₁. The graph has a cycle, so the schedule is not conflict-serializable. · Wrong: "serializable, since T₂ commits first" — commit order is not conflict order.
- **DBT-P11** — Expected: each transaction reads the snapshot with two doctors on call, sees the condition true, and updates only its own row; the write sets are disjoint, so first-committer-wins does not fire, and both commit, leaving zero on call. Each read a row the other then wrote: two read–write antidependencies T₁ → T₂ → T₁ between concurrent transactions, the dangerous structure that SSI aborts. · Wrong: "SI prevents this because it prevents lost updates" — there is no lost update; the two writes touch different rows.
- **DBT-P12** — Expected: skip LSN 25 (25 ≤ pageLSN 30, so its effect is already on the page); apply LSN 40 and set pageLSN to 40. A repeat after a second crash meets pageLSN ≥ LSN for everything already applied and skips it, so redo is idempotent. · Wrong: "apply both, redo repeats history" — history is repeated only for changes the page lacks.
- **DBT-P13** — Expected: leaves = 100,000,000 / 100 = 1,000,000; next level ⌈1,000,000 / 200⌉ = 5,000; next 25; then the root. Four levels; with the root cached a lookup reads 3 pages. · Wrong: log₂(10⁸) ≈ 27 reads — that is a binary tree, not a fanout-200 B+ tree.
- **DBT-P14** — Expected: 1,000,000 × (1/50) × (1/10) = 2,000 rows. It fails when a and b are correlated: if every row with a = 1 has b = 2, the true count is 20,000; if none does, it is 0. Extended statistics on (a, b) fix it. · Wrong: 1,000,000 × (1/50 + 1/10) — adding selectivities models OR, not AND.
- **DBT-P15** — Expected: none of the three: notifications are sent only to sessions listening at commit time and are not stored, so the jobs stay in the table unannounced (another worker may take them, but if every worker was cut off, nobody does). Fixes: (1) after `LISTEN` on every (re)connect, drain the queue with the `SKIP LOCKED` claim until it returns no row, and after each notification claim until empty rather than one job per notification (several `NOTIFY` calls with the same channel and payload in one transaction are folded into one); (2) a slow safety poll (say once a minute) covers anything else missed. · Wrong: "`NOTIFY` is a durable queue, so the worker receives the backlog on reconnect" — the table is the queue; the notification is only a wake-up.

## Appendix V — Verification notes (honesty flags)

- **Goldens:** 92/92 exercise cards carry fingerprints from local JSON artefacts (`goldens_ex_l1_4.json`, `goldens_ex_l5_8.json`, `goldens_ex_l9_13.json`, `goldens_ex_l14.json`). They were produced by `run_ex.py` against seed v1; this build **wires those values verbatim** and does not re-execute Postgres when this file is assembled. The goldens files are printed in full in §3.8.
- **Wrong-path set:** 11 entries from `goldens_wrong.json` referenced in traps where IDs overlap.
- **`(verify)` markers:** Cloud SQL/AlloyDB/Spanner/BigQuery UI labels, exam-guide domain lists, and version-specific syntax (MERGE on older PG, Spanner JSON functions, SQL Server `IS DISTINCT FROM` availability) — check live docs before exams or production.
- **SQL-E3.7 note:** the run log of levels 1–4 contained a duplicate run line with a divergent hash; **JSON golden `100:1b05fa94` is authoritative**.
- **SQL-CAP3:** design/TX evidence capstone — no single `lab.chk` fingerprint; acceptance is the four tests in §9 (transcript + ADR).
- **TF-DB*:** plan-only by default; the learner writes the `.tf`, and §8.2 lists what each plan must show. Provider attribute names are `(verify)`.
- **Primer SD-13…SD-19:** intentionally not re-taught; cross-links only.
- **Engine-slice toys DB-1…DB-10 (§4.0):** not duplicated; the concept modules add the analytic layer only.
- **Modern notes:** SSI write-skew behaviour, `MERGE` in PG15+, `EXCLUDE` with `btree_gist`, recursive cycle clause PG14+ — confirm on your minor version.
- **Built:** 2026-09-21 from on-box sources only.