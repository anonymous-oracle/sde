# The SQL & Databases Companion — GCP-Native Edition
Companion to `gcp-curriculum.md` ("The Consolidated Cloud Mastery Curriculum", initial course T–11b + Part 12 continuation) and to the owner nodes `DB-SQL` and `DB-ENGINE` of `unified-curriculum.md`.
Sibling of `system-design-primer-companion.md` (its SD-13 … SD-27 own the *scale-out and interview* layer of databases; this file owns *SQL semantics, relational and storage theory, schema craft, and a query-writing exercise ladder*).
Sources: PostgreSQL documentation · Silberschatz/Korth/Sudarshan *Database System Concepts* (`TB-DB-001`) · Rogov *PostgreSQL 14 Internals* (`TB-DB-002`) · Kleppmann *Designing Data-Intensive Applications* (`TB-DIST-001`) · CMU 15-445/645 (`SRC-DB-002`) · Google Cloud documentation for Cloud SQL, AlloyDB, Spanner, BigQuery. Built September 21, 2026. **Every reference query and every golden value in §6 and Appendix K was executed on PostgreSQL 15.8 against the deterministic "seed v1" of §3** — nothing in the exercise ladder is typed from memory.

---

## 0. Read this first — how this file complements gcp-curriculum.md

### 0.1 Standing instruction (for Claude, every session)

**This file is a complement to `gcp-curriculum.md`, not a second curriculum. Read both. Whenever a gcp-curriculum module is taught, also teach every companion concept bound to it (§2) in the same session, as one story. Similar, related, and overlapping concepts are stitched together and taught in parallel — never in separate sessions, never twice.**

Why: gcp-curriculum owns the *product spine* (Northstar on GCP) and, in Part 2, the engine slices DB-1 … DB-10 and the Cloud SQL procedure. It deliberately does not own the SQL *language* end to end, the pre-SQL mathematics a learner may lack, the theory tier behind the slices (serializability, ARIES, join-cost formulas, Selinger-style planning), modelling method, analytics dialects, or a large body of query-writing practice. This file supplies exactly those, and hangs each piece on the gcp-curriculum module that needs it, **at the moment that module needs it**.

### 0.2 Stitching rules

1. **One concept, one teaching.** If both files teach an idea, it is taught once, in the module that owns it (§2.1 overlap register), and the other file only *adds*. Later sessions recall in one line; they do not re-teach. Ideas already unlocked-and-confirmed on the ledger are recalled, never re-taught.
2. **Ownership split (memorise).** *gcp-curriculum owns:* Cloud SQL setup (2.3), the ten engine slices DB-1 … DB-10 and their toys, Firestore (2.4), migrations-as-jobs (2.6), the Spanner/NoSQL map (2.7), the primitives of 8.1 (cursor pager, hot partition, pool math, RLS, LSM-vs-B-tree comparison), outbox/inbox (3.5), the ledger (5.3), BigQuery ops (9.4/9b.1), as-of joins as *leakage prevention* (9c.1), billing-export SQL (10.3). *This file owns:* SQL-language mastery (SL), relational theory (RT), the CS theory tier under the slices (CS), data-design method (DD), operating-a-database craft (OD), analytics and dialect craft (AN), pre-SQL prerequisites (PQ), and the exercise ladder (§6). **Where a gcp-curriculum toy exists (WAL codec, slotted page, B-tree, iterator executor, visibility simulator) this file never asks for a second toy — it adds the analytic layer (formulas, schedules, cost models) that the toy's tests do not reach.**
3. **Same ten-rung ramp, same locks.** Companion concepts are taught through gcp-curriculum's universal ten-rung sequence (anchor → vocabulary → representation → core move → worked illustration → basic unseen check → routine variation → mixed transfer → top-rung challenge → reflection + ledger). The **dependency gate**, **rung-2 vocabulary audit** and **Prop Lock** apply unchanged: never use a later system as a prop (no Spanner interleaving in the first Postgres transcript; no full PITR runbook before its owner; no Cloud SQL HA as a "known" prop before Part 2). If an exercise needs machinery not yet unlocked, **postpone the exercise** — or teach the machinery first. A smuggled prop is an *instructor process failure*, never "shaky", exactly as in gcp-curriculum.
4. **Every concept gets a GCP lens the moment it is taught**, at three depths (same definitions as the primer companion): **Lens-1** name the GCP resource and show one `gcloud`/console/Terraform line; **Lens-2** touch it (local Docker Postgres is the default lab; Cloud SQL / AlloyDB / Spanner emulator / BigQuery sandbox only when Lab Reality allows); **Lens-3** cert-depth trade-offs and limits (PCA storage systems; Professional Data Engineer / Database Engineer overlap).
5. **Bank ≠ dump.** The exercise ladder in §6 is a **bank of specifications**, not a worksheet. At teach time issue **one** item at the rung the ledger says is next (never the whole list), let the learner attempt first, escalate hints one notch at a time (*what structure do you see → smaller case → smallest unlocked hint*), and only then open the instructor key (Appendix K). **Never paste a key before an attempt.** Mixed-transfer items name their two earlier tools on one line before executing.
6. **Predict before you run; explain the discrepancy after.** Every exercise that has a *result shape*, a *row count*, a *plan shape*, or an *isolation outcome* starts with the learner writing the prediction (one line). Then run. A wrong prediction is the best teaching moment in this file — record the discrepancy on the ledger, do not skip it. (gcp-curriculum "Database protocol".)
7. **Fingerprints, not eyeballs.** Each read-only exercise has a *golden*: `rows:hash` computed by the lab kit (`lab.chk`). Two queries are the same answer iff their fingerprints match. **Goldens are valid only for seed v1 on PostgreSQL 15.x with `timezone = UTC` and the `C` collation** — if any of those change, regenerate; do not "fix" a learner's query to match a stale golden.
8. **Tracking is inline.** Tick `- [ ]` boxes in this file or say "done" in chat. Do **not** create a separate tracker; the learner ledger of gcp-curriculum ("Teaching contract → Learner state") records unlocked / shaky / postponed for companion modules under their IDs (`SL-08`, `E6.2`…).
9. **Honesty flags.** `(verify)` = a GCP or PostgreSQL-version detail that changes often or that I could not confirm here — check live docs before relying on it for an exam or production. **Modern note** marks where industry has moved past a textbook.
10. **Time, money and secrets.** Labs are free-tier/credits-safe: local Postgres in Docker is the default; Cloud SQL / AlloyDB / Memorystore are credits-optional and *destroyed the same day* (gcp-curriculum Lab safety). Never put a password, key or real customer data in a query, a prompt or this file; the lab data is synthetic.
11. **User can override anything:** skip a concept already known (run its skip-test; §5 tiers), jump to an exercise, or go hands-on — same rights as gcp-curriculum. **On a conflict:** gcp-curriculum wins on order, Lab Reality, exam time-sensitivity and the ledger; this file wins on SQL/DB content and exercise specs.
12. **Read economically.** Each session read §0 and §2, then only the blocks bound to today's gcp-curriculum module (search by ID: `SL-06`, `CS-05`, `E4.5`…). Do not reload the whole file. Appendix K (keys) is opened *only after* an attempt.

### 0.3 How one stitched session runs

1. **Anchor** — announce the gcp-curriculum module and list the companion modules bound to it (§2). Run the one-line pre-rung-2 self-check: every term to be used is anchored this session or on the ledger; no unanchored sibling; no new product; every noun in the picture unlocked.
2. **Concept** — teach the shared idea once (gcp-curriculum depth), then layer this file's SQL / theory / craft on top. Derive before you name.
3. **GCP lens** — the resource(s): Lens-1 always, Lens-2 when Lab Reality allows.
4. **Numbers** — one back-of-the-envelope estimate (rows per page, index height, pool arithmetic, bytes scanned).
5. **Exercise** — issue **one** item from §6/§7 at the current rung (prediction first). For a mixed-transfer item, name the new idea plus exactly two earlier unlocked ideas.
6. **Check** — the module's check questions; the learner answers before you explain. An unseen check that uses unanchored terms is invalid — fix the check, don't mark the learner shaky.
7. **Close** — tick boxes in both files' sense; ledger line: what unlocked, what is shaky, what is postponed.

### 0.4 Notation

- `PQ-nn` prerequisites · `RT-nn` relational theory · `SL-nn` SQL language · `CS-nn` computer science under the engine · `DD-nn` data design · `OD-nn` operating databases · `AN-nn` analytics & other engines. All are in §4.
- `E<level>.<n>` query-writing exercises (§6, levels 1–14; **E11** and **E12** are *labs* in §7) · `Z0.n` level-0 paper drills · `TD-n` theory drills · `PX-n` plan-prediction cards · `TX-n` transaction labs · `BH-n` bug-hunts · `DT-n` dialect-translation drills · `SD-n` schema-design cases · `C1–C4` capstones · `TF-DBn` Terraform database exercises.
- `T.*`, `F1…F4`, `M.*`, `0.x`, `1.x`, `D0…D8`, `2.x` … `11b`, `12.Sxx`, `DB-1 … DB-10`, `G4`, `G12b` are **gcp-curriculum** IDs. `SD-13 … SD-27` are **primer-companion** IDs. `TB-…`/`SRC-…` are unified-curriculum source IDs.
- `Northstar` = the running product of gcp-curriculum; the lab database is its OLTP slice plus an event stream.

---

## 1. Coverage ledger — every part of "SQL databases + underlying CS + prerequisites", and where it lives

| Area | Content | Covered in |
|---|---|---|
| **Pre-SQL prerequisites** | sets/relations/functions/bags · propositional & predicate logic, three-valued logic · counting & cardinality · data types, encodings, integer vs decimal vs float · time & time zones · files, CSV/JSON · CLI, `psql`, Docker Postgres · Python DB-API and parameter binding · big-O, hashing, trees, sorting, binary search · storage hierarchy and units | PQ-01 … PQ-08, Z0.1 … Z0.8 |
| **Relational theory** | relational model, keys, integrity · relational algebra (set and bag) · tuple/domain calculus, safety, Codd equivalence · functional dependencies, closure, cover · 1NF … BCNF, 4NF/5NF-lite, lossless & dependency-preserving decomposition · ER → tables · query equivalence & rewrite rules | RT-01 … RT-08, TD-1 … TD-8 |
| **SQL language** | DDL, types, constraints · logical evaluation order · NULL & 3VL · joins (inner, outer, cross, self, semi, anti, lateral, non-equi) · aggregation, grouping sets · subqueries, EXISTS, ALL/ANY, division · set operations · CTEs, recursion · window functions and frames · DML, RETURNING, upsert, MERGE · views, materialized views, functions, triggers · dates, time zones, JSON, text, regex · security in SQL (GRANT, RLS, injection) · dialects and the standard | SL-01 … SL-14, E1 … E10, E13 |
| **CS under the engine** | storage layouts and page arithmetic · B-tree/B+tree math, hash, LSM, bitmap, GIN/GiST/BRIN · buffer caching theory · external sort, join and aggregation algorithms with I/O cost · cardinality estimation and join ordering · concurrency-control theory (conflict serializability, 2PL, timestamp ordering, MVCC/SI, SSI) · recovery theory (WAL, steal/no-force, ARIES) · replication logs, consensus, 2PC, consistency models · columnar/vectorised execution and compression · complexity of queries, recursion, expressiveness | CS-01 … CS-11, TD-9 … TD-16, TX-1 … TX-8, PX-1 … PX-11 |
| **Data design** | conceptual → logical → physical · keys (natural, surrogate, UUID, snowflake) · money, units, time · hierarchies & graphs in SQL · temporal data & SCD · JSONB vs relational · soft delete, audit, history · denormalisation with ADRs · multi-tenancy · partitioning & sharding-key design · schema evolution (expand/contract) · data quality as constraints | DD-01 … DD-13, SD-1 … SD-6, E10 |
| **Operating databases** | indexing strategy & `EXPLAIN` workflow · statistics & slow-query observability · connection pooling · backup/restore/PITR drills · replication & read-your-writes · vacuum/bloat · retention & partitions · migrations tooling & testing · application data access (N+1, ORMs, prepared statements, injection, pagination) · testing SQL | OD-01 … OD-10, PX-1 … PX-11, BH-1 … BH-6, TF-DB1 … TF-DB6 |
| **Analytics & other engines** | OLTP vs OLAP, star/snowflake · BigQuery/GoogleSQL dialect · cohorts, funnels, sessionisation, retention · approximate aggregation · Spanner SQL · NoSQL query models vs SQL · search & vectors in SQL | AN-01 … AN-07, E6, E13, DT-1 … DT-8 |
| **Query-creation exercise bank** | 14 levels, ~120 specified items with traps, goldens and instructor keys | §6, Appendix K |
| **Engine-behaviour labs** | isolation anomalies, deadlock, SKIP LOCKED, oversell under concurrency, EXPLAIN predictions | §7 (TX-1 … TX-8, PX-1 … PX-11) |
| **Capstones** | fault-injected audit, cash-basis revenue, checkout schema + concurrency, slow-query rescue | §9 (C1–C4) |
| **Rosetta & IaC** | Postgres ↔ Cloud SQL ↔ AlloyDB ↔ Spanner ↔ BigQuery ↔ MySQL ↔ SQL Server ↔ SQLite ↔ Oracle · Terraform for Cloud SQL / AlloyDB / Spanner / BigQuery | §8 |

Counts (verified by the generator that produced §6): **Level 0** 8 paper drills · **theory** 16 drills · **query exercises** E1–E10, E13, C1–C2, C4 → 111 items (all with fingerprints) · **plan predictions** 11 · **transaction labs** 8 · **bug-hunts** 6 · **dialect drills** 8 · **schema cases** 6 · **capstones** 4.

---

## 2. Stitch table — teach these together

Each gcp-curriculum module on the left is taught **with** the companion modules on the right, in the same session (§0.2 rule 1). "Checkpoint" is the exercise (or drill) to run once that module and its stitched concepts are done — issued **one at a time**, per rule 5.

| gcp-curriculum module | Companion modules taught in the same session | Checkpoint |
|---|---|---|
| **T.Disc** (logic, sets, proofs, counting, graphs) — *Tier HS/UG* | PQ-01 sets, relations, functions, **bags** · PQ-02 predicate logic and **3-valued logic (preview)** · counting/cardinality bounds of joins (RT-01) | Z0.1 … Z0.6 |
| **T.Algo** (structures, hashing theory, complexity) | PQ-07 sorting, hashing, trees, binary search *as the raw material of access paths* · CS-02 B-tree fan-out and height arithmetic (formula only — the toy is DB-6) | Z0.7, TD-10 |
| **T.Quant** (units, orders of magnitude) | PQ-08 storage hierarchy, page/row arithmetic · latency numbers (recall of primer SD-37) | Z0.8 |
| **M.NS** (numerical stability) | PQ-03 `numeric` vs float, rounding modes (half-up vs banker's), integer money — *recall IEEE from M.NS; add decimal semantics* | E2.1, E2.7 |
| **T.SysTheory — DB theory** (with Part 2) | RT-02 algebra · RT-03 calculus/safety (grad) · RT-04/05 FDs & normal forms · RT-08 rewrites · CS-05 serializability & SI · CS-06 recovery · CS-08 cardinality. **UG gate items** map to TD-2 (push σ through ⋈), TD-1/2/3 (keys, FDs, 3NF), TD-8 (dirty-read & lost-update schedules), TD-12 (WAL durability). **Grad gate items** map to TD-9 (snapshot visibility), TD-13 (selectivity estimate) | TD-1 … TD-16 (as gated) |
| **F1** (computer, OS, CLI, Git, JSON, HTTP) | PQ-04 files, CSV/JSON/JSONL, encodings (UTF-8, BOM) · PQ-05 `psql`, env vars, Docker basics for a Postgres container | E0 warm-up: load the lab (§3) |
| **D1** Docker/OCI · **1.2** container contract | PQ-05 `docker compose` Postgres with a named volume and a healthcheck (the lab in §3.2) | lab loads, fingerprints match |
| **D2** CI | OD-10 SQL tests in CI: a Postgres service container, seed v1, fingerprint assertions, migration up/down | run E3.2 as a CI test |
| **D3/D7** CD, IaC | OD-08 migration ordering in deploys · §8.2 Terraform DB exercises | TF-DB1 … TF-DB2 (plan only) |
| **0.4** HLD/LLD contract, ADR template, NFR table | DD-01 conceptual → logical → physical; **schema ADRs** ("I pick X because Y, I accept Z") · DD-12 constraints as spec | SD-1 |
| **0.5** IAM (+ **2.3** IAM DB auth) | SL-13 database roles vs IAM principals, `GRANT`/`REVOKE`, least privilege | E10.6 (RLS) after 4.7 |
| **1.7** observability day one | OD-02 logs, slow-query log, `pg_stat_statements`, Query Insights vocabulary | PX-1 |
| **1.12** HA & autoscaling | OD-03 pool arithmetic under autoscaling (instances × pool ≤ `max_connections`); *8.1 owns the spreadsheet — recall it* | TX-8 |
| **2.1 — SQL design track** (concept, then lab) | **The core binding.** SL-01 … SL-12 · RT-01 … RT-07 · DD-01 … DD-06, DD-12 · OD-01 · CS-01 … CS-08 — paired slice by slice with DB-1 … DB-10 (§2.2 table below) | E1 → E10 by level (§6 gates) |
| **2.2** GCP relational offerings (decision table) | AN-01 OLTP/OLAP · DD-08 JSONB vs relational · §8.1 Rosetta table | DT-1 |
| **2.3** Cloud SQL setup (required procedure) | OD-03 pooling & pool math · OD-04 backup/restore drills *as runbook (DB-10 owns the toy)* · OD-05 replicas & read-your-writes · SL-13 privileges · §8.2 Terraform | TF-DB1, TX-8, BH-5 |
| **2.4** Firestore | AN-06 the *same question* in Firestore and SQL — where the document model wins and loses | DT-7 |
| **2.5** Cloud Storage | PQ-04 `COPY`/import & export of CSV/JSON through GCS; encoding and NULL-vs-empty pitfalls | E8.8 – E8.10 |
| **2.6** config, migrations, jobs | DD-11 expand/contract with **lock levels** · OD-08 migration tooling & testing (dirty state, advisory lock) | E9.6, SD-4 |
| **2.7** Spanner & NoSQL map | AN-05 GoogleSQL/Spanner · DD-13 key design & partitioning · CS-07 TrueTime, 2PC, Paxos groups | DT-6, SD-5 |
| **3.0** software design (repositories) | OD-09 application data access: N+1, ORM pitfalls, prepared statements, transaction boundaries | BH-3 |
| **3.4** async (Pub/Sub, Tasks, Scheduler) | SL-10 idempotent writes: `INSERT … ON CONFLICT`, unique keys | E9.3 |
| **3.5** failure design (outbox/inbox, sagas) | CS-07 why 2PC is not the answer; SL-10 `FOR UPDATE SKIP LOCKED` job claim | TX-5, TX-8 |
| **4.7** authorization · **4.9** secrets & supply chain | SL-13 RLS, injection, parameterisation, least-privilege roles | E10.6, BH-2 |
| **5.3** ledger and consistency | DD-05 money (integer minor units), DD-09 audit/history · SL-08 running balances · CS-05 isolation for money | E4.5, C2, BH-4 |
| **7.3** data protection | SL-13 column-level encryption (`pgcrypto`), masking views, CMEK vocabulary | SD-6 |
| **8.0** Donne-Martin building blocks · **8.C** evidence packs | DD-01 schema ADRs inside HLD packs; DD-10 denormalisation ADR; **recall** primer SD-13 … SD-19 for scale-out | SD-2, SD-3 |
| **8.1** primitives — cursor pagination · hot partition · pool math · RLS · LSM vs B-tree · schema evolution · idempotency | OD-09 keyset SQL and its index (**8.1.5 owns the from-scratch pager**) · DD-13 hot-key skew query · OD-03 · SL-13 · CS-02 arithmetic · DD-11 | PX-9, E4.7 |
| **9.1** Memorystore | OD-09 cache-aside vs DB read path (query-level vs object-level); *no new concept* | — |
| **9.4** Spanner, AlloyDB, Bigtable, BigQuery (ops view) | AN-01 · AN-02 · AN-05 · CS-09 columnar & vectorised execution | DT-1 … DT-6, E13.3 |
| **9b.1** Big-data services (BigQuery, Dataform) | AN-02 partition/cluster and bytes scanned · AN-03 cohorts/funnels · AN-04 approximate aggregation · SL-11 views & materialised views | E6.2, E6.6, E13.1 – E13.3 |
| **9c.1** features, labels, skew (**as-of join** owner) | SL-08 / SL-04: the **SQL shape** of a point-in-time join (LATERAL / range join). *9c.1 owns leakage; this file owns the join* | E6.4, E13.4, E13.5 |
| **9c.2 / 9c.5** retrieval, RAG | AN-07 full-text search and vector search in Postgres (`tsvector`, `pgvector`) vs dedicated engines | DT-8 |
| **10.0** observability · **10.5** performance | OD-01/02 plan reading & workload observation · CS-08 · PX-1 … PX-11 | PX-1 … PX-11, C4 |
| **10.1** SLO / error budget | OD-05 replication lag as an SLI; recovery-point objective from WAL archiving | BH-5 |
| **10.3** FinOps + billing-export SQL | AN-03 window analytics on a *billing-export-shaped* table; AN-02 bytes-scanned cost | DT-4, E13.1 |
| **11** capstone (Northstar v1) | C1 – C4 are the database acceptance tests of the capstone | C1 – C4 |
| **11b** control-plane capstone | DD-09 audit/event log design; OD-08 migrations for the control-plane store | SD-6 |
| **12.S12** SQL & relational correctness (`DB-SQL`) | **Skip-test map:** if Part 2 confirmed FDs/joins/transactions/pagination/client hygiene, stamp using E3.2, E4.5, E5.4, E9.3, TX-2. **Else** run the S12 order = RT-01/04/05 → RT-02 → SL-01/02 → SL-03 → SL-04 → SL-05 → SL-06/09 → SL-08 → TX labs → OD-09 (§2.3 table) | see §2.3 |
| **12.S13** PostgreSQL internals (`DB-ENGINE`) | **Skip-test map:** residual `EXPLAIN` drills = PX-1 … PX-11; crash/recovery evidence = TD-12 + OD-04 drill. **Else** run the S13 order = CS-01 → CS-04 → CS-02 → CS-03 → CS-08 → CS-05 → CS-06 → CS-07 (§2.3) | see §2.3 |
| **PCA / PDE / PCDE certs** | PCA 2.2 storage systems: §8.1 + DT-1; PDE: AN-01…AN-04, E13; Professional Cloud Database Engineer: OD-03…OD-05, TF-DB1… (all `verify` against the live exam guide) | §8 |

### 2.1 Overlap register — concepts that appear in both files (teach once, in the owner)

| Concept | Owner (teach here) | This file adds |
|---|---|---|
| Relational algebra, 3VL (DB-1) | gcp-curriculum **2.1 / DB-1** (toy: bag relations + truth-table tests) | RT-02 set-vs-bag laws and rewrite equivalences; RT-03 calculus/safety; SL-03 NULL semantics across every clause; Z0.4, TD-5/6 |
| Catalog, tuples, constraints (DB-2) | **2.1 / DB-2** | SL-01 type system & constraint catalogue; DD-04 key strategies; DD-12; E10 constraint batteries |
| CTEs, windows, lateral (DB-3) | **2.1 / DB-3** | SL-06/08/09 full semantics (frames, EXCLUDE, RANGE with intervals, recursion termination); E4–E7 ladder |
| Heap pages & TOAST (DB-4) | **2.1 / DB-4** (toy: slotted page) | CS-01 page/row arithmetic and fill-factor maths (no second toy) |
| Buffer pool (DB-5) | **2.1 / DB-5** (toy: clock sweep) | CS-04 hit-ratio and working-set reasoning, why sequential flooding needs scan-resistance |
| Indexes (DB-6) | **2.1 / DB-6** (toy: B-tree + inverted index) | CS-02 height/fan-out/cost formulas; OD-01 index-design workflow; PX-1 … PX-6 |
| Executor & spill (DB-7) | **2.1 / DB-7** (toy: iterators, forced spill) | CS-03 I/O cost formulas (block-NL, Grace hash, sort-merge), TD-11; PX-7, PX-10 |
| Planner statistics (DB-8) | **2.1 / DB-8** (toy: histogram + MCV) | CS-08 Selinger DP, estimation error propagation, TD-13; PX-8 |
| MVCC, locks, vacuum (DB-9) | **2.1 / DB-9** (toy: visibility simulator, deadlock detector) | CS-05 schedule theory (precedence graphs, 2PL, SSI); TD-8/9; TX-1 … TX-8 |
| WAL, replica, PITR (DB-10 / G4) | **2.1 / DB-10** (toy: mini-WAL) | CS-06 ARIES and steal/no-force reasoning; TD-12; OD-04 restore-drill runbook |
| Cloud SQL provisioning, Auth Proxy, private IP, HA, flags | **2.3** | OD-03/04/05 SQL-side consequences (session state vs pooler modes, RPO/RTO arithmetic, replica lag); §8.2 Terraform |
| Migrations as jobs, expand/contract | **2.6** | DD-11 *lock levels*, `NOT VALID` + `VALIDATE`, `CREATE INDEX CONCURRENTLY`, backfill batching (E9.6) |
| Spanner, Bigtable, Firestore map | **2.7 / 2.4** | AN-05, AN-06 same-question comparisons; DD-13 key design as SQL |
| Cursor pagination | **8.1.5** (from-scratch pager) | OD-09 the SQL seek predicate & its supporting index; PX-9 measured against OFFSET |
| Hot partition, key histogram | **8.1** | DD-13 the skew query on lab data (user 1 = 135 orders; see PX-1) |
| Connection-pool math | **8.1 / 2.3** | OD-03 pooler modes (session/transaction/statement) and what breaks in transaction mode |
| RLS multi-tenancy | **8.1 / 2.1** | SL-13 policy syntax, `FORCE`, owner bypass; E10.2 composite FK as defence in depth; E10.6 |
| Outbox / inbox, idempotency | **3.5 / 3.4** | SL-10 the SQL that makes them true (unique index, `ON CONFLICT`, `SKIP LOCKED`); TX-5, E9.3 |
| Ledger, minor-unit ints | **5.3** | DD-05 modelling; E4.5/C2 revenue reconciliation; C1 invariants |
| BigQuery partition/cluster/cost | **9.4 / 9b.1** | AN-02 SQL-level cost reading; DT drills |
| As-of / point-in-time join | **9c.1** | E6.4 / E13.4 / E13.5 the SQL shapes (lateral, range join, SCD2) |
| Billing-export SQL patterns | **10.3** | AN-03 reused windows; no new concept |
| SQL scale-out (replication, federation, sharding, denormalisation, SQL tuning) | **primer companion SD-13 … SD-19** | *this file never re-teaches them*; CS-07/DD-13/OD-05/OD-07 add engine-level and SQL-level detail only |
| ACID, CAP, consistency, big-O, hashing | gcp-curriculum **T.Disc / T.Algo / T.SysTheory / 2.x** | CS-05/CS-07 formal treatment of isolation and consistency models; PQ-07 recall only |

### 2.2 Part 2.1 slice pairing — the engine slices DB-1 … DB-10 and what rides with each

The gcp-curriculum slice supplies *toy spec, SQL, EXPLAIN prediction, Cloud SQL mapping*. The companion supplies the **SQL ladder rung, the theory tier, and the prediction card**. Teach the pair as **one session**.

| Slice (owner) | Companion theory | Companion SQL rung | Prediction / lab cards |
|---|---|---|---|
| **DB-1** algebra & 3VL | RT-01, RT-02, RT-08 · TD-5, TD-6, TD-7 | E1.x, E2.x, E3.x (joins, anti/semi/outer), E4.3/E4.4 set ops | — (predict multiplicity & NULL behaviour per exercise) |
| **DB-2** catalog, tuples, constraints | RT-04/05 (FDs → keys), DD-04, DD-12 · TD-1 … TD-4 | E9.x (DML), E10.1 – E10.6 (constraints as specification) | PX-7 (missing FK index) |
| **DB-3** CTEs, windows, lateral | RT-03 (safety), CS-11 (recursion) · TD-16 | E4.x, E5.x, E6.x, E7.x | PX-10 (sort node for windows) |
| **DB-4** heap pages & TOAST | CS-01 page arithmetic · Z0.8 | E8.5 – E8.7 (JSONB size intuition) | — |
| **DB-5** buffer pool | CS-04 | — | PX-9 (hit vs read) |
| **DB-6** indexes | CS-02, CS-10 · TD-10 | E12-style workflow (§7.1) | PX-1 … PX-6, PX-9 |
| **DB-7** executor & spill | CS-03 · TD-11 | E13.x aggregation shapes | PX-7, PX-10 |
| **DB-8** planner statistics | CS-08 · TD-13 | — | PX-8 |
| **DB-9** MVCC, locks, vacuum | CS-05 · TD-8, TD-9, TD-15 | E9.6 (batching), E11 labs | TX-1 … TX-7 |
| **DB-10** WAL, replica, PITR (**G4**) | CS-06, CS-07 · TD-12, TD-14 | — | BH-5, OD-04 restore drill, TX-8 |

### 2.3 Parallel calendar — how the companion rides gcp-curriculum's spine

gcp-curriculum's spine is `T → F → M → 0 → 1 → D → 2 → 3 → …`. SQL does not first *appear* until Part 2, so the calendar front-loads only **cheap, unlockable prerequisites** and holds the language until Part 2 needs it (Prop Lock: no SQL vocabulary before it is anchored).

| Window (gcp-curriculum) | Companion work (parallel, small) | Outcome |
|---|---|---|
| **Block T** (HS → UG tiers) | PQ-01, PQ-02, PQ-07, PQ-08 with Z0.1 – Z0.8 (≈ 6 short sessions) | paper fluency: sets/bags/3VL/counting/units |
| **F1 – F4, M.NS** | PQ-03 (types, decimals), PQ-04 (files/JSON), PQ-05 (`psql` + Docker Postgres) — the lab loads and fingerprints match (§3) | lab environment ready; no SQL semantics yet |
| **Parts 0 – 1, D** | OD-10 (tests in CI), OD-02 (logs/slow-query vocabulary), OD-03 recall at 1.12 | vocabulary only; no new SQL |
| **Part 2 (the main event)** | **2.1 is stretched over ≥ 3 weeks:** week 1 = RT-01/04/05 + SL-01/02/03 + E1–E3 · week 2 = RT-02 + SL-04…SL-09 + E4–E7 + DB-1/DB-3 · week 3 = SL-10 + TX labs + CS-05 + DB-9 · then DB-4…DB-8 with CS-01…CS-04, CS-08 and PX cards · then DB-10 with CS-06, OD-04 · 2.2 – 2.7 as bound in §2 | SQL competency through E9; plan and isolation predictions; the theory tier |
| **Parts 3 – 5** | E9.3 (3.4), TX-5 (3.5), E10.6 (4.7), E4.5/C2 (5.3) | SQL that makes async/ledger/RLS true |
| **Part 8** | PX-9 / DD-13 with 8.1; SD-2/SD-3 inside packs | scale primitives with SQL evidence |
| **Parts 9, 9b, 9c** | AN-01 … AN-05, E6, E13, DT drills (BigQuery), E6.4/E13.4/E13.5 at 9c.1 | analytics dialect and point-in-time joins |
| **Part 10** | PX cards and C4 at 10.5; DT-4 at 10.3 | performance and cost SQL |
| **Part 11 / 11b** | C1 – C4 | database acceptance |
| **Part 12 — S12 / S13** | skip-test via the checkpoints in the stitch table; else run the S12/S13 orders below | continuation, only if the skip-test fails |

**12.S12 order → companion modules (unified-curriculum §5.4 order, unchanged):** relations/keys/FDs/normalisation → **RT-01, RT-04, RT-05** · relational algebra → **RT-02** (+ TD-5/6) · DDL/types/constraints → **SL-01, DD-04, DD-12** · SELECT semantics & NULL/3VL → **SL-02, SL-03** · joins incl. semi/anti/outer → **SL-04** · aggregation → **SL-05** · subqueries/CTEs/recursion → **SL-06, SL-07, SL-09** · windows → **SL-08** · transactions/isolation → **CS-05** + TX labs · pagination and application access → **OD-09**. *Predict multiplicity and NULL behaviour before execution.*

**12.S13 order → companion modules:** storage media & layouts → **CS-01, CS-09** · pages/tuples/TOAST/catalogs → **CS-01** · buffer manager → **CS-04** · hash/B-tree/GIN/GiST/BRIN/vector indexes → **CS-02, CS-10** · iterators, sort/aggregate, join algorithms → **CS-03** · statistics/cardinality/cost → **CS-08** · MVCC/isolation/locks/deadlocks/vacuum → **CS-05, OD-06** · WAL/checkpoints/recovery → **CS-06** · replication/PITR → **CS-06, CS-07, OD-04, OD-05** · parallel/distributed trade-offs → **CS-07, CS-09**.

---
