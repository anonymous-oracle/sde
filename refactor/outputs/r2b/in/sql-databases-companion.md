# The SQL & Databases Companion — GCP-Native Edition
Companion to `Curriculum` ("The Consolidated Cloud Mastery Curriculum") and to its reference application `northstar-reference-app.md` (Track N).
*Provenance (C-01, 2026-09-24):* originally authored against `gcp-curriculum.md` and the `unified-curriculum.md` nodes `DB-SQL` / `DB-ENGINE`; rebound to `Curriculum` + `northstar-reference-app.md` on 2026-09-24. Every foreign label and its new anchor is listed in `crosswalk.md` §1.
Sibling of `system-design-primer-companion.md` (its SD-13 … SD-27 own the *scale-out and interview* layer of databases; this file owns *SQL semantics, relational and storage theory, schema craft, and a query-writing exercise ladder*).
Sources: PostgreSQL documentation · Silberschatz/Korth/Sudarshan *Database System Concepts* (`TB-DB-001`) · Rogov *PostgreSQL 14 Internals* (`TB-DB-002`) · Kleppmann *Designing Data-Intensive Applications* (`TB-DIST-001`) · CMU 15-445/645 (`SRC-DB-002`) · Google Cloud documentation for Cloud SQL, AlloyDB, Spanner, BigQuery. Built September 21, 2026. **Every reference query and every golden value in §6 and Appendix K was executed on PostgreSQL 15.8 against the deterministic "seed v1" of §3** — nothing in the exercise ladder is typed from memory.
> **Refactor note (2026-09-24, C-53):** the `TB-…` / `SRC-…` labels in the line above are this file's bibliography keys. They were first assigned in `unified-curriculum.md`; the labels are kept, the books and courses are named in full beside them.

---

## 0. Read this first — how this file complements `Curriculum`

### 0.1 Standing instruction (for Claude, every session)

**This file is a complement to `Curriculum`, not a second curriculum. Read both. Whenever a `Curriculum` module is taught, also teach every companion concept bound to it (§2) in the same session, as one story. Similar, related, and overlapping concepts are stitched together and taught in parallel — never in separate sessions, never twice.**

Why: `Curriculum` owns the order and the module spine; `northstar-reference-app.md` owns the *product spine* (Northstar on GCP) and the Cloud SQL procedure (N2.3). Since the refactor this file also owns the engine slices DB-1 … DB-10 (§4.0, C-05). `Curriculum` deliberately does not own the SQL *language* end to end, the pre-SQL mathematics a learner may lack, the theory tier behind the slices (serializability, ARIES, join-cost formulas, Selinger-style planning), modelling method, analytics dialects, or a large body of query-writing practice. This file supplies exactly those, and hangs each piece on the `Curriculum` module that needs it, **at the moment that module needs it**.

### 0.2 Stitching rules

1. **One concept, one teaching.** If both files teach an idea, it is taught once, in the module that owns it (§2.1 overlap register), and the other file only *adds*. Later sessions recall in one line; they do not re-teach. Ideas already unlocked-and-confirmed on the ledger are recalled, never re-taught.
2. **Ownership split (memorise).** *`Curriculum` and Northstar own:* Cloud SQL setup (N2.3), Firestore (N2.4), migrations-as-jobs (N2.6), the Spanner/NoSQL map (N2.7), the primitives of N8.1 (cursor pager, hot partition, pool math, RLS, LSM-vs-B-tree comparison), outbox/inbox (A9 theory; design-patterns ARCH-11 shape), the ledger (N5.3), BigQuery ops (N9.4/N9b.1), as-of joins as *leakage prevention* (D3, N9c.1), billing-export SQL (B4). *This file owns:* SQL-language mastery (SL), relational theory (RT), the CS theory tier under the slices (CS), data-design method (DD), operating-a-database craft (OD), analytics and dialect craft (AN), pre-SQL prerequisites (PQ), the exercise ladder (§6), and — since the refactor (C-05) — the engine slices DB-1 … DB-10 and their toys (§4.0). **Where a §4.0 slice toy exists (WAL codec, slotted page, B-tree, iterator executor, visibility simulator) this file never asks for a second toy — it adds the analytic layer (formulas, schedules, cost models) that the toy's tests do not reach.**
3. **Same ten-rung ramp, same locks.** Companion concepts are taught through the suite's ten-rung sequence (`Curriculum` §0.4.3) (anchor → vocabulary → representation → core move → worked illustration → basic unseen check → routine variation → mixed transfer → top-rung challenge → reflection + ledger). The **dependency gate**, **rung-2 vocabulary audit** and **Prop Lock** apply unchanged: never use a later system as a prop (no Spanner interleaving in the first Postgres transcript; no full PITR runbook before its owner; no Cloud SQL HA as a "known" prop before its N2.3 session). If an exercise needs machinery not yet unlocked, **postpone the exercise** — or teach the machinery first. A smuggled prop is an *instructor process failure*, never "shaky", exactly as in `Curriculum` §0.4.6.
4. **Every concept gets a GCP lens the moment it is taught**, at three depths (same definitions as the primer companion): **Lens-1** name the GCP resource and show one `gcloud`/console/Terraform line; **Lens-2** touch it (local Docker Postgres is the default lab; Cloud SQL / AlloyDB / Spanner emulator / BigQuery sandbox only when Lab Reality allows); **Lens-3** cert-depth trade-offs and limits (PCA storage systems; Professional Data Engineer / Database Engineer overlap).
5. **Bank ≠ dump.** The exercise ladder in §6 is a **bank of specifications**, not a worksheet. At teach time issue **one** item at the rung the ledger says is next (never the whole list), let the learner attempt first, escalate hints one notch at a time (*what structure do you see → smaller case → smallest unlocked hint*), and only then open the instructor key (Appendix K). **Never paste a key before an attempt.** Mixed-transfer items name their two earlier tools on one line before executing.
6. **Predict before you run; explain the discrepancy after.** Every exercise that has a *result shape*, a *row count*, a *plan shape*, or an *isolation outcome* starts with the learner writing the prediction (one line). Then run. A wrong prediction is the best teaching moment in this file — record the discrepancy on the ledger, do not skip it. (`Curriculum` §0.4.4, predict → run → discrepancy; C-53.)
7. **Fingerprints, not eyeballs.** Each read-only exercise has a *golden*: `rows:hash` computed by the lab kit (`lab.chk`). Two queries are the same answer iff their fingerprints match. **Goldens are valid only for seed v1 on PostgreSQL 15.x with `timezone = UTC` and the `C` collation** — if any of those change, regenerate; do not "fix" a learner's query to match a stale golden.
8. **Tracking is inline.** Tick `- [ ]` boxes in this file or say "done" in chat. Do **not** create a separate tracker; the learner ledger `session-progress-ledger.md` (C-57; it replaces the old parent's "Teaching contract → Learner state") records unlocked / shaky / postponed for companion modules under their IDs (`SL-08`, `SQL-E6.2`…).
9. **Honesty flags.** `(verify)` = a GCP or PostgreSQL-version detail that changes often or that I could not confirm here — check live docs before relying on it for an exam or production. **Modern note** marks where industry has moved past a textbook.
10. **Time, money and secrets.** Labs are free-tier/credits-safe: local Postgres in Docker is the default; Cloud SQL / AlloyDB / Memorystore are credits-optional and *destroyed the same day* (`Curriculum` §0.5 Lab Safety). Never put a password, key or real customer data in a query, a prompt or this file; the lab data is synthetic.
11. **User can override anything:** skip a concept already known (run its skip-test; §5 tiers), jump to an exercise, or go hands-on — same rights as `Curriculum` §0.4.1. **On a conflict:** `Curriculum` wins on order, Lab Reality, exam time-sensitivity and the ledger; this file wins on SQL/DB content and exercise specs.
12. **Read economically.** Each session read §0 and §2, then only the blocks bound to today's `Curriculum` module (search by ID: `SL-06`, `CS-05`, `SQL-E4.5`…). Do not reload the whole file. Appendix K (keys) is opened *only after* an attempt.

### 0.3 How one stitched session runs

1. **Anchor** — announce the `Curriculum` module and list the companion modules bound to it (§2). Run the one-line pre-rung-2 self-check: every term to be used is anchored this session or on the ledger; no unanchored sibling; no new product; every noun in the picture unlocked.
2. **Concept** — teach the shared idea once (`Curriculum` depth), then layer this file's SQL / theory / craft on top. Derive before you name.
3. **GCP lens** — the resource(s): Lens-1 always, Lens-2 when Lab Reality allows.
4. **Numbers** — one back-of-the-envelope estimate (rows per page, index height, pool arithmetic, bytes scanned).
5. **Exercise** — issue **one** item from §6/§7 at the current rung (prediction first). For a mixed-transfer item, name the new idea plus exactly two earlier unlocked ideas.
6. **Check** — the module's check questions; the learner answers before you explain. An unseen check that uses unanchored terms is invalid — fix the check, don't mark the learner shaky.
7. **Close** — tick boxes in both files' sense; ledger line: what unlocked, what is shaky, what is postponed.

When other companions bind to the same session, the Suite Session Protocol in `Curriculum` §0.4 governs.

### 0.4 Notation

- `PQ-nn` prerequisites · `RT-nn` relational theory · `SL-nn` SQL language · `CS-nn` computer science under the engine · `DD-nn` data design · `OD-nn` operating databases · `AN-nn` analytics & other engines. All are in §4.
- `SQL-E<level>.<n>` query-writing exercises (§6, levels 1–14; **TX** and **PX** are *labs* in §7) · `SQL-Z0.n` level-0 paper drills · `TD-n` theory drills · `PX-n` plan-prediction cards · `TX-n` transaction labs · `BH-n` bug-hunts · `DT-n` dialect-translation drills · `SCH-n` schema-design cases · `SQL-CAP1–SQL-CAP4` capstones · `TF-DBn` Terraform database exercises.
- The old parent's labels (`T.*`, `F1…F4`, `M.*`, `0.x`, `1.x`, `D0…D8`, `2.x` … `11b`, `12.Sxx`, `G4`, `G12b`) were rebound on 2026-09-24 to `Curriculum` IDs (`A1…D4`, `M1…M6`, `U1…U7`, `S1…S11`, the Part V category IDs `V-…`) and Northstar sections (`Nx.y`); `crosswalk.md` §1 has every mapping. `DB-1 … DB-10` are this file's engine slices (§4.0). `SD-13 … SD-27` are primer-companion IDs. `TB-…`/`SRC-…` are this file's bibliography labels (title block).
- Tiers: `SQL-T-HS` high-school · `SQL-T-UG` undergraduate · `SQL-T-GR` graduate — the depth tier of a theory item or gate (§2 rows for M1 and A8 + A9; renamed from `HS` / `UG` / `grad` in §5 of the refactor). *(Legend added by the refactor, C-08.)*
- `Northstar` = the running reference application (`northstar-reference-app.md`, Track N); the lab database is its OLTP slice plus an event stream.

### 0.5 Learner teaching preferences (binding; copied unchanged from session-progress-ledger.md §5, invariant 4)

- **Check questions must be woven into the concept explanation itself**, not asked as separate "what do you already know" diagnostics — the learner explicitly opted out of background-probing questions and asked for calibration to happen through how they handle the material.
- **"Maintain curriculum depth and academic rigour"** has been repeated multiple times as an explicit standing instruction — do not compress, simplify, or skip the "why," even under time pressure or a fast pace of correct answers.
- When companion-file content (system-design-primer, SQL, design-patterns) overlaps a `Curriculum` module, **teach it once, stitched into the same session** — never as a separate pass, per each companion's own §0.2 stitching rules.
- If a companion file references module IDs that don't exist in `Curriculum` (as `sql-databases-companion.md` does), **say so plainly rather than forcing a silent, possibly-wrong mapping** — this was well received when done for the SQL companion.

---

## 1. Coverage ledger — every part of "SQL databases + underlying CS + prerequisites", and where it lives

| Area | Content | Covered in |
|---|---|---|
| **Pre-SQL prerequisites** | sets/relations/functions/bags · propositional & predicate logic, three-valued logic · counting & cardinality · data types, encodings, integer vs decimal vs float · time & time zones · files, CSV/JSON · CLI, `psql`, Docker Postgres · Python DB-API and parameter binding · big-O, hashing, trees, sorting, binary search · storage hierarchy and units | PQ-01 … PQ-08, SQL-Z0.1 … SQL-Z0.8 |
| **Relational theory** | relational model, keys, integrity · relational algebra (set and bag) · tuple/domain calculus, safety, Codd equivalence · functional dependencies, closure, cover · 1NF … BCNF, 4NF/5NF-lite, lossless & dependency-preserving decomposition · ER → tables · query equivalence & rewrite rules | RT-01 … RT-08, TD-1 … TD-8 |
| **SQL language** | DDL, types, constraints · logical evaluation order · NULL & 3VL · joins (inner, outer, cross, self, semi, anti, lateral, non-equi) · aggregation, grouping sets · subqueries, EXISTS, ALL/ANY, division · set operations · CTEs, recursion · window functions and frames · DML, RETURNING, upsert, MERGE · views, materialized views, functions, triggers · dates, time zones, JSON, text, regex · security in SQL (GRANT, RLS, injection) · dialects and the standard | SL-01 … SL-14, SQL-E1 … SQL-E10, SQL-E13 |
| **CS under the engine** | storage layouts and page arithmetic · B-tree/B+tree math, hash, LSM, bitmap, GIN/GiST/BRIN · buffer caching theory · external sort, join and aggregation algorithms with I/O cost · cardinality estimation and join ordering · concurrency-control theory (conflict serializability, 2PL, timestamp ordering, MVCC/SI, SSI) · recovery theory (WAL, steal/no-force, ARIES) · replication logs, consensus, 2PC, consistency models · columnar/vectorised execution and compression · complexity of queries, recursion, expressiveness | CS-01 … CS-11, TD-9 … TD-16, TX-1 … TX-8, PX-1 … PX-11 |
| **Data design** | conceptual → logical → physical · keys (natural, surrogate, UUID, snowflake) · money, units, time · hierarchies & graphs in SQL · temporal data & SCD · JSONB vs relational · soft delete, audit, history · denormalisation with ADRs · multi-tenancy · partitioning & sharding-key design · schema evolution (expand/contract) · data quality as constraints | DD-01 … DD-13, SCH-1 … SCH-6, SQL-E10 |
| **Operating databases** | indexing strategy & `EXPLAIN` workflow · statistics & slow-query observability · connection pooling · backup/restore/PITR drills · replication & read-your-writes · vacuum/bloat · retention & partitions · migrations tooling & testing · application data access (N+1, ORMs, prepared statements, injection, pagination) · testing SQL | OD-01 … OD-10, PX-1 … PX-11, BH-1 … BH-6, TF-DB1 … TF-DB6 |
| **Analytics & other engines** | OLTP vs OLAP, star/snowflake · BigQuery/GoogleSQL dialect · cohorts, funnels, sessionisation, retention · approximate aggregation · Spanner SQL · NoSQL query models vs SQL · search & vectors in SQL | AN-01 … AN-07, SQL-E6, SQL-E13, DT-1 … DT-8 |
| **Query-creation exercise bank** | 14 levels, ~120 specified items with traps, goldens and instructor keys | §6, Appendix K |
| **Engine-behaviour labs** | isolation anomalies, deadlock, SKIP LOCKED, oversell under concurrency, EXPLAIN predictions | §7 (TX-1 … TX-8, PX-1 … PX-11) |
| **Capstones** | fault-injected audit, cash-basis revenue, checkout schema + concurrency, slow-query rescue | §9 (SQL-CAP1–SQL-CAP4) |
| **Rosetta & IaC** | Postgres ↔ Cloud SQL ↔ AlloyDB ↔ Spanner ↔ BigQuery ↔ MySQL ↔ SQL Server ↔ SQLite ↔ Oracle · Terraform for Cloud SQL / AlloyDB / Spanner / BigQuery | §8 |

Counts (verified by the generator that produced §6): **Level 0** 8 paper drills · **theory** 16 drills · **query exercises** SQL-E1–SQL-E10, SQL-E13, SQL-CAP1–SQL-CAP2, SQL-CAP4 → 111 items (all with fingerprints) · **plan predictions** 11 · **transaction labs** 8 · **bug-hunts** 6 · **dialect drills** 8 · **schema cases** 6 · **capstones** 4.

---

## 2. Stitch table — teach these together

Each `Curriculum` module on the left is taught **with** the companion modules on the right, in the same session (§0.2 rule 1). "Checkpoint" is the exercise (or drill) to run once that module and its stitched concepts are done — issued **one at a time**, per rule 5.

| `Curriculum` module (was: old-parent label) | Companion modules taught in the same session | Checkpoint |
|---|---|---|
| **M1** (logic, sets, proofs, counting, graphs) — *Tier SQL-T-HS/SQL-T-UG* *(was `T.Disc`)* | PQ-01 sets, relations, functions, **bags** · PQ-02 predicate logic and **3-valued logic (preview)** · counting/cardinality bounds of joins (RT-01) | SQL-Z0.1 … SQL-Z0.6 |
| **A4** (recall) + **U2** (structures, hashing theory, complexity) *(was `T.Algo`)* | PQ-07 sorting, hashing, trees, binary search *as the raw material of access paths* · CS-02 B-tree fan-out and height arithmetic (formula only — the toy is DB-6) | SQL-Z0.7, TD-10 |
| **A1/A2** (recall) + **M6** (units, orders of magnitude) *(was `T.Quant`)* | PQ-08 storage hierarchy, page/row arithmetic · latency numbers (recall of primer SD-37) | SQL-Z0.8 |
| **M5** (numerical stability) *(was `M.NS`)* | PQ-03 `numeric` vs float, rounding modes (half-up vs banker's), integer money — *recall IEEE from M5; add decimal semantics* | SQL-E2.1, SQL-E2.7 |
| **A8 + A9** (+ U5) — DB theory (with the A8 SQL sessions) *(was `T.SysTheory`, Part 2)* | RT-02 algebra · RT-03 calculus/safety (SQL-T-GR) · RT-04/05 FDs & normal forms · RT-08 rewrites · CS-05 serializability & SI · CS-06 recovery · CS-08 cardinality. **SQL-T-UG gate items** map to TD-2 (push σ through ⋈), TD-1/2/3 (keys, FDs, 3NF), TD-8 (dirty-read & lost-update schedules), TD-12 (WAL durability). **SQL-T-GR gate items** map to TD-9 (snapshot visibility), TD-13 (selectivity estimate) | TD-1 … TD-16 (as gated) |
| **A3 + A6** (computer, OS, CLI, Git, JSON, HTTP) *(was `F1`)* | PQ-04 files, CSV/JSON/JSONL, encodings (UTF-8, BOM) · PQ-05 `psql`, env vars, Docker basics for a Postgres container | SQL-E0 warm-up: load the lab (§3) |
| **C1** Docker/OCI, container contract *(was `D1`, `1.2`)* | PQ-05 `docker compose` Postgres with a named volume and a healthcheck (the lab in §3.2) | lab loads, fingerprints match |
| **C4** CI *(was `D2`)* | OD-10 SQL tests in CI: a Postgres service container, seed v1, fingerprint assertions, migration up/down | run SQL-E3.2 as a CI test |
| **C4 + C5** CD, IaC *(was `D3/D7`)* | OD-08 migration ordering in deploys · §8.2 Terraform DB exercises | TF-DB1 … TF-DB2 (plan only) |
| **S2** + **N0.4** HLD/LLD contract, ADR template, NFR table *(was `0.4`)* | DD-01 conceptual → logical → physical; **schema ADRs** ("I pick X because Y, I accept Z") · DD-12 constraints as spec | SCH-1 |
| **B5** IAM (+ **N2.3** IAM DB auth) *(was `0.5`, `2.3`)* | SL-13 database roles vs IAM principals, `GRANT`/`REVOKE`, least privilege | SQL-E10.6 (RLS) after A10 |
| **C6** observability day one *(was `1.7`)* | OD-02 logs, slow-query log, `pg_stat_statements`, Query Insights vocabulary | PX-1 |
| **B3** HA & autoscaling *(was `1.12`)* | OD-03 pool arithmetic under autoscaling (instances × pool ≤ `max_connections`); *N8.1 owns the spreadsheet — recall it* | TX-8 |
| **A8 — SQL design track** (concept, then lab; engine slices §4.0) *(was `2.1`)* | **The core binding.** SL-01 … SL-12 · RT-01 … RT-07 · DD-01 … DD-06, DD-12 · OD-01 · CS-01 … CS-08 — paired slice by slice with DB-1 … DB-10 (§2.2 table below) | SQL-E1 → SQL-E10 by level (§6 gates) |
| **A8** + **V-STOR** GCP relational offerings (decision table) *(was `2.2`)* | AN-01 OLTP/OLAP · DD-08 JSONB vs relational · §8.1 Rosetta table | DT-1 |
| **N2.3** Cloud SQL setup (required procedure) *(was `2.3`)* | OD-03 pooling & pool math · OD-04 backup/restore drills *as runbook (DB-10 owns the toy)* · OD-05 replicas & read-your-writes · SL-13 privileges · §8.2 Terraform | TF-DB1, TX-8, BH-5 |
| **A8** (NoSQL) + **N2.4** Firestore *(was `2.4`)* | AN-06 the *same question* in Firestore and SQL — where the document model wins and loses | DT-7 |
| **N2.5** Cloud Storage *(was `2.5`)* | PQ-04 `COPY`/import & export of CSV/JSON through GCS; encoding and NULL-vs-empty pitfalls | SQL-E8.8 – SQL-E8.10 |
| **A8** + **C4** + **N2.6** config, migrations, jobs *(was `2.6`)* | DD-11 expand/contract with **lock levels** · OD-08 migration tooling & testing (dirty state, advisory lock) | SQL-E9.6, SCH-4 |
| **A9** + **V-STOR** + **N2.7** Spanner & NoSQL map *(was `2.7`)* | AN-05 GoogleSQL/Spanner · DD-13 key design & partitioning · CS-07 TrueTime, 2PC, Paxos groups | DT-6, SCH-5 |
| **A7** software design (repositories; design-patterns Repository, Unit of Work) *(was `3.0`)* | OD-09 application data access: N+1, ORM pitfalls, prepared statements, transaction boundaries | BH-3 |
| **A7** async (Pub/Sub, Tasks, Scheduler) *(was `3.4`)* | SL-10 idempotent writes: `INSERT … ON CONFLICT`, unique keys | SQL-E9.3 |
| **A9** + design-patterns **ARCH-11** failure design (outbox/inbox, sagas) *(was `3.5`)* | CS-07 why 2PC is not the answer; SL-10 `FOR UPDATE SKIP LOCKED` job claim | TX-5, TX-8 |
| **A10 + B5** authorization · **C1** + **Phase 4 Security** secrets & supply chain *(was `4.7`, `4.9`)* | SL-13 RLS, injection, parameterisation, least-privilege roles | SQL-E10.6, BH-2 |
| **A8** + **N5.3** ledger and consistency *(was `5.3`)* | DD-05 money (integer minor units), DD-09 audit/history · SL-08 running balances · CS-05 isolation for money | SQL-E4.5, SQL-CAP2, BH-4 |
| **Phase 4 Security** + **N7.3** data protection *(was `7.3`)* | SL-13 column-level encryption (`pgcrypto`), masking views, CMEK vocabulary | SCH-6 |
| **S2** + **N8.0** Donne-Martin building blocks · **N8.C** evidence packs *(was `8.0`, `8.C`)* | DD-01 schema ADRs inside HLD packs; DD-10 denormalisation ADR; **recall** primer SD-13 … SD-19 for scale-out | SCH-2, SCH-3 |
| **N8.1** primitives — cursor pagination · hot partition · pool math · RLS · LSM vs B-tree · schema evolution · idempotency *(was `8.1`)* | OD-09 keyset SQL and its index (**N8.1.5 owns the from-scratch pager**) · DD-13 hot-key skew query · OD-03 · SL-13 · CS-02 arithmetic · DD-11 | PX-9, SQL-E4.7 |
| **V-STOR** + **N9.1** Memorystore *(was `9.1`)* | OD-09 cache-aside vs DB read path (query-level vs object-level); *no new concept* | — |
| **V-STOR** + **N9.4** Spanner, AlloyDB, Bigtable, BigQuery (ops view) *(was `9.4`)* | AN-01 · AN-02 · AN-05 · CS-09 columnar & vectorised execution | DT-1 … DT-6, SQL-E13.3 |
| **V-DATA** + **N9b.1** Big-data services (BigQuery, Dataform) *(was `9b.1`)* | AN-02 partition/cluster and bytes scanned · AN-03 cohorts/funnels · AN-04 approximate aggregation · SL-11 views & materialised views | SQL-E6.2, SQL-E6.6, SQL-E13.1 – SQL-E13.3 |
| **D3** + **N9c.1** features, labels, skew (**as-of join** owner) *(was `9c.1`)* | SL-08 / SL-04: the **SQL shape** of a point-in-time join (LATERAL / range join). *N9c.1 owns leakage; this file owns the join* | SQL-E6.4, SQL-E13.4, SQL-E13.5 |
| **D4** + **N9c.2 / N9c.5** retrieval, RAG *(was `9c.2 / 9c.5`)* | AN-07 full-text search and vector search in Postgres (`tsvector`, `pgvector`) vs dedicated engines | DT-8 |
| **C6** observability, performance *(was `10.0`, `10.5`)* | OD-01/02 plan reading & workload observation · CS-08 · PX-1 … PX-11 | PX-1 … PX-11, SQL-CAP4 |
| **C7** SLO / error budget *(was `10.1`)* | OD-05 replication lag as an SLI; recovery-point objective from WAL archiving | BH-5 |
| **B4** FinOps + billing-export SQL *(was `10.3`)* | AN-03 window analytics on a *billing-export-shaped* table; AN-02 bytes-scanned cost | DT-4, SQL-E13.1 |
| **N11** capstone (Northstar v1) *(was `11`)* | SQL-CAP1 – SQL-CAP4 are the database acceptance tests of the capstone | SQL-CAP1 – SQL-CAP4 |
| **N11b** control-plane capstone *(was `11b`)* | DD-09 audit/event log design; OD-08 migrations for the control-plane store | SCH-6 |
| **SQL-SKIP-SQL** SQL & relational correctness (`DB-SQL`) | **Skip-test map:** if the A8 sessions confirmed FDs/joins/transactions/pagination/client hygiene, stamp using SQL-E3.2, SQL-E4.5, SQL-E5.4, SQL-E9.3, TX-2. **Else** run the SQL-SKIP-SQL order = RT-01/04/05 → RT-02 → SL-01/02 → SL-03 → SL-04 → SL-05 → SL-06/09 → SL-08 → TX labs → OD-09 (§2.3 table) | see §2.3 |
| **SQL-SKIP-ENGINE** PostgreSQL internals (`DB-ENGINE`) | **Skip-test map:** residual `EXPLAIN` drills = PX-1 … PX-11; crash/recovery evidence = TD-12 + OD-04 drill. **Else** run the SQL-SKIP-ENGINE order = CS-01 → CS-04 → CS-02 → CS-03 → CS-08 → CS-05 → CS-06 → CS-07 (§2.3) | see §2.3 |
| **Part V cert rows 1, 3, 8** (PCA / PDE / PCDE certs) | PCA 2.2 storage systems: §8.1 + DT-1; PDE: AN-01…AN-04, SQL-E13; Professional Cloud Database Engineer: OD-03…OD-05, TF-DB1… (all `verify` against the live exam guide) | §8 |

### 2.1 Overlap register — concepts that appear in both files (teach once, in the owner)

> **Refactor note (2026-09-24, §7):** the suite-wide register is `Curriculum` §0.3; this table is the SQL slice of it, and on a conflict §0.3 wins. DB-1 … DB-10 are owned by this file since C-05 (§4.0).

| Concept | Owner (teach here) | This file adds |
|---|---|---|
| Relational algebra, 3VL (DB-1) | **§4.0 DB-1** (this file since C-05; A8) (toy: bag relations + truth-table tests) | RT-02 set-vs-bag laws and rewrite equivalences; RT-03 calculus/safety; SL-03 NULL semantics across every clause; SQL-Z0.4, TD-5/6 |
| Catalog, tuples, constraints (DB-2) | **§4.0 DB-2** | SL-01 type system & constraint catalogue; DD-04 key strategies; DD-12; SQL-E10 constraint batteries |
| CTEs, windows, lateral (DB-3) | **§4.0 DB-3** | SL-06/08/09 full semantics (frames, EXCLUDE, RANGE with intervals, recursion termination); SQL-E4–SQL-E7 ladder |
| Heap pages & TOAST (DB-4) | **§4.0 DB-4** (toy: slotted page) | CS-01 page/row arithmetic and fill-factor maths (no second toy) |
| Buffer pool (DB-5) | **§4.0 DB-5** (toy: clock sweep) | CS-04 hit-ratio and working-set reasoning, why sequential flooding needs scan-resistance |
| Indexes (DB-6) | **§4.0 DB-6** (toy: B-tree + inverted index) | CS-02 height/fan-out/cost formulas; OD-01 index-design workflow; PX-1 … PX-6 |
| Executor & spill (DB-7) | **§4.0 DB-7** (toy: iterators, forced spill) | CS-03 I/O cost formulas (block-NL, Grace hash, sort-merge), TD-11; PX-7, PX-10 |
| Planner statistics (DB-8) | **§4.0 DB-8** (toy: histogram + MCV) | CS-08 Selinger DP, estimation error propagation, TD-13; PX-8 |
| MVCC, locks, vacuum (DB-9) | **§4.0 DB-9** (toy: visibility simulator, deadlock detector) | CS-05 schedule theory (precedence graphs, 2PL, SSI); TD-8/9; TX-1 … TX-8 |
| WAL, replica, PITR (DB-10; foreign `G4` → N2.3) | **§4.0 DB-10** (toy: mini-WAL) | CS-06 ARIES and steal/no-force reasoning; TD-12; OD-04 restore-drill runbook |
| Cloud SQL provisioning, Auth Proxy, private IP, HA, flags | **N2.3** | OD-03/04/05 SQL-side consequences (session state vs pooler modes, RPO/RTO arithmetic, replica lag); §8.2 Terraform |
| Migrations as jobs, expand/contract | **N2.6** | DD-11 *lock levels*, `NOT VALID` + `VALIDATE`, `CREATE INDEX CONCURRENTLY`, backfill batching (SQL-E9.6) |
| Spanner, Bigtable, Firestore map | **N2.7 / N2.4** | AN-05, AN-06 same-question comparisons; DD-13 key design as SQL |
| Cursor pagination | **N8.1.5** (from-scratch pager) | OD-09 the SQL seek predicate & its supporting index; PX-9 measured against OFFSET |
| Hot partition, key histogram | **N8.1** | DD-13 the skew query on lab data (user 1 = 135 orders; see PX-1) |
| Connection-pool math | **N8.1 / N2.3** | OD-03 pooler modes (session/transaction/statement) and what breaks in transaction mode |
| RLS multi-tenancy | **N8.1 / A8** | SL-13 policy syntax, `FORCE`, owner bypass; SQL-E10.2 composite FK as defence in depth; SQL-E10.6 |
| Outbox / inbox, idempotency | **A9 / A7** (`Curriculum` §0.3: 2PC/Saga/outbox) | SL-10 the SQL that makes them true (unique index, `ON CONFLICT`, `SKIP LOCKED`); TX-5, SQL-E9.3 |
| Ledger, minor-unit ints | **N5.3** | DD-05 modelling; SQL-E4.5/SQL-CAP2 revenue reconciliation; SQL-CAP1 invariants |
| BigQuery partition/cluster/cost | **N9.4 / N9b.1** | AN-02 SQL-level cost reading; DT drills |
| As-of / point-in-time join | **N9c.1** (D3) | SQL-E6.4 / SQL-E13.4 / SQL-E13.5 the SQL shapes (lateral, range join, SCD2) |
| Billing-export SQL patterns | **B4** | AN-03 reused windows; no new concept |
| SQL scale-out (replication, federation, sharding, denormalisation, SQL tuning) | **primer companion SD-13 … SD-19** | *this file never re-teaches them*; CS-07/DD-13/OD-05/OD-07 add engine-level and SQL-level detail only |
| ACID, CAP, consistency, big-O, hashing | `Curriculum` **M1 / A4 + U2 / A8 + A9 / A8** *(was T.Disc / T.Algo / T.SysTheory / 2.x)* | CS-05/CS-07 formal treatment of isolation and consistency models; PQ-07 recall only |

### 2.2 A8 slice pairing — the engine slices DB-1 … DB-10 and what rides with each

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
| **DB-10** WAL, replica, PITR (**N2.3**) | CS-06, CS-07 · TD-12, TD-14 | — | BH-5, OD-04 restore drill, TX-8 |

### 2.3 Parallel calendar — how the companion rides `Curriculum`'s spine

`Curriculum`'s spine is Phases 0–3 (Tracks A–D, mostly in parallel) → Phase 4 → …, with the reserved M/U/S tracks placed by R4. SQL does not first *appear* until A8, so the calendar front-loads only **cheap, unlockable prerequisites** and holds the language until A8 needs it (Prop Lock: no SQL vocabulary before it is anchored).

| Window (`Curriculum`) | Companion work (parallel, small) | Outcome |
|---|---|---|
| **A1–A4 + M1** (SQL-T-HS → SQL-T-UG tiers) *(was Block T)* | PQ-01, PQ-02, PQ-07, PQ-08 with SQL-Z0.1 – SQL-Z0.8 (≈ 6 short sessions) | paper fluency: sets/bags/3VL/counting/units |
| **A3, A6, A11 + M5** *(was F1 – F4, M.NS)* | PQ-03 (types, decimals), PQ-04 (files/JSON), PQ-05 (`psql` + Docker Postgres) — the lab loads and fingerprints match (§3) | lab environment ready; no SQL semantics yet |
| **Tracks B and C (B3, C1, C4, C6)** *(was Parts 0 – 1, D)* | OD-10 (tests in CI), OD-02 (logs/slow-query vocabulary), OD-03 recall at B3 | vocabulary only; no new SQL |
| **A8 (the main event)** *(was Part 2)* | **The A8 SQL block is stretched over ≥ 3 weeks:** week 1 = RT-01/04/05 + SL-01/02/03 + SQL-E1–SQL-E3 · week 2 = RT-02 + SL-04…SL-09 + SQL-E4–SQL-E7 + DB-1/DB-3 · week 3 = SL-10 + TX labs + CS-05 + DB-9 · then DB-4…DB-8 with CS-01…CS-04, CS-08 and PX cards · then DB-10 with CS-06, OD-04 · the V-STOR and N2.3…N2.7 rows as bound in §2 | SQL competency through SQL-E9; plan and isolation predictions; the theory tier |
| **A7, A9, A10 + N5.3** *(was Parts 3 – 5)* | SQL-E9.3 (A7), TX-5 (A9), SQL-E10.6 (A10), SQL-E4.5/SQL-CAP2 (N5.3) | SQL that makes async/ledger/RLS true |
| **N8.0/N8.1/N8.C + S2** *(was Part 8)* | PX-9 / DD-13 with N8.1; SCH-2/SCH-3 inside packs | scale primitives with SQL evidence |
| **V-STOR, V-DATA, D3/D4 + N9.1/N9.4/N9b.1/N9c.1** *(was Parts 9, 9b, 9c)* | AN-01 … AN-05, SQL-E6, SQL-E13, DT drills (BigQuery), SQL-E6.4/SQL-E13.4/SQL-E13.5 at D3 (N9c.1) | analytics dialect and point-in-time joins |
| **C6, C7, B4** *(was Part 10)* | PX cards and SQL-CAP4 at C6; DT-4 at B4 | performance and cost SQL |
| **N11 / N11b** *(was Part 11 / 11b)* | SQL-CAP1 – SQL-CAP4 | database acceptance |
| **A8 skip-tests — SQL-SKIP-SQL / SQL-SKIP-ENGINE** *(was Part 12)* | skip-test via the checkpoints in the stitch table; else run the SQL-SKIP-SQL/SQL-SKIP-ENGINE orders below | continuation, only if the skip-test fails |

**SQL-SKIP-SQL order → companion modules (order unchanged; provenance: `unified-curriculum.md` §5.4):** relations/keys/FDs/normalisation → **RT-01, RT-04, RT-05** · relational algebra → **RT-02** (+ TD-5/6) · DDL/types/constraints → **SL-01, DD-04, DD-12** · SELECT semantics & NULL/3VL → **SL-02, SL-03** · joins incl. semi/anti/outer → **SL-04** · aggregation → **SL-05** · subqueries/CTEs/recursion → **SL-06, SL-07, SL-09** · windows → **SL-08** · transactions/isolation → **CS-05** + TX labs · pagination and application access → **OD-09**. *Predict multiplicity and NULL behaviour before execution.*

**SQL-SKIP-ENGINE order → companion modules:** storage media & layouts → **CS-01, CS-09** · pages/tuples/TOAST/catalogs → **CS-01** · buffer manager → **CS-04** · hash/B-tree/GIN/GiST/BRIN/vector indexes → **CS-02, CS-10** · iterators, sort/aggregate, join algorithms → **CS-03** · statistics/cardinality/cost → **CS-08** · MVCC/isolation/locks/deadlocks/vacuum → **CS-05, OD-06** · WAL/checkpoints/recovery → **CS-06** · replication/PITR → **CS-06, CS-07, OD-04, OD-05** · parallel/distributed trade-offs → **CS-07, CS-09**.

---

---

## 3. Lab kit — deterministic Northstar SQL lab

### 3.1 What you get
Local PostgreSQL 15.x database `labdb` with schema `lab` (OLTP slice of Northstar) plus `work` (scratch) and fingerprint functions `lab.chk` / `lab.chk_o`. Sources on this box: `sql-companion-work/lab_schema.sql`, `lab_seed.sql`, runners `run_ex.py`, `plans.py`, `tx_tests.py`.

### 3.2 Bring-up (Docker default)
1. Run Postgres 15 with a named volume, port published (lab scripts expect `PGPORT=54329`, user/db `lab`/`labdb` — adjust env to match your compose).
2. `psql -v ON_ERROR_STOP=1 -f lab_schema.sql -f lab_seed.sql`
3. Pin session: `SET TIME ZONE 'UTC';` and use `C` collation (image default `C`/`POSIX` for the lab). **Goldens are invalid if timezone or collation drift.**
4. Smoke: `SELECT lab.chk('SELECT 1');` — non-null `1:…` fingerprint.

Cloud SQL / AlloyDB: same SQL; create an instance only when Lab Reality allows and **destroy the same day** (`Curriculum` §0.5). Auth Proxy for IAM DB auth when N2.3 is unlocked — not required for local goldens.

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
Every exercise with a result shape, row count, plan shape, or isolation outcome: write the prediction (one line) **before** `psql`. Record discrepancies on the ledger — wrong predictions are the teaching moment (gcp "Database protocol").

### 3.7 How runners relate
| Runner | Purpose |
|---|---|
| `run_ex.py` | Executes exercise keys inside `BEGIN…ROLLBACK`, prints golden + sample rows |
| `plans.py` | PX plan catalogue (PX-1–PX-11) |
| `tx_tests.py` + `two.py` | Dual-session TX scenarios |
| `wrongs.py` | Canonical wrong queries for trap fingerprints |
| `naive.sql` / `safe.sql` | Oversell RMW vs atomic claim (TX companion) |
| `slow_bad.sql` / `slow_good.sql` | SQL-CAP4 baseline vs rewrite |

## 4. Concept curriculum

Format per module (same contract as `system-design-primer-companion.md`): **Core** · **Theory** · **GCP lens** (Lens-1 always) · **Lab** · **Check** (answer before explanation). Tick `- [ ]` when taught *and* checks answered. Ownership: where a §4.0 slice toy exists, the concept modules add analysis only.

### 4.0 Engine slices (DB-1 … DB-10)

*Ported by the refactor (2026-09-24, C-05; decision D1).* **Source material:** `gcp-curriculum.md` lines 3118–3179 ("Engine slices DB-1–DB-10"), copied verbatim except for the ID rebinding marked in `crosswalk.md`. Since the refactor this file **owns** the slices; `Curriculum` A8 points here, and each slice is taught as one session with the companion theory paired to it in §2.2. The Cloud SQL procedure they map onto is N2.3.

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
- **Cloud SQL mapping:** Flags for constraints; migrations via Job (N2.6); IAM DB users still have catalogs.

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

#### DB-10 — WAL, replica, PITR (foreign `G4` WAL codec → N2.3)
- **Toy spec:** Mini WAL append/CRC/replay; checkpoint; streaming replica mock; backup/restore drill.
- **SQL:** `pg_switch_wal()` in learning PG; base backup story; promote replica (local compose).
- **EXPLAIN prediction:** N/A for WAL — instead **predict** recovery: crash after commit → row present; after uncommitted → absent.
- **Cloud SQL mapping:** Automated backups, PITR window, HA regional standby, replica flags — name each Cloud SQL knob against the toy.

Do not reimplement PostgreSQL. Do not skip a slice because Cloud SQL hides it.

### 4.1 Pre-SQL prerequisites (PQ-01 … PQ-08)

#### PQ-01 · Sets, relations, functions, bags — stitch: M1
- [ ] done
- **Core:** A relation is a set of tuples over a heading; SQL tables are *bags* (multisets). Functions map each domain element to at most one value — keys are the database word for that.
- **Theory:** Cartesian product size = |R|·|S|; projection can shrink or (with bags) keep duplicates. Bag union vs set union.
- **GCP lens:** Lens-1: BigQuery and Postgres both default to bag semantics (`UNION ALL` preserves). Lens-2: lab seed has deliberate duplicate-risk columns (`idempotency_key` NULL repeats).
- **Lab:** SQL-Z0.1–SQL-Z0.3 on paper: draw R⋈S multiplicities for 2×3 bags.
- **Check:** Why does `SELECT a FROM t UNION SELECT a FROM t` drop duplicates but `UNION ALL` does not? Give multiplicities.

#### PQ-02 · Propositional & predicate logic; 3VL preview — stitch: M1 · DB-1
- [ ] done
- **Core:** Predicates evaluate to TRUE / FALSE / UNKNOWN. Filters keep only TRUE. `NOT UNKNOWN = UNKNOWN`.
- **Theory:** Truth tables for AND/OR/NOT with UNKNOWN; why `WHERE col = NULL` never matches.
- **GCP lens:** Lens-1: Cloud SQL Postgres 3VL matches the standard. Lens-3: BigQuery `IS DISTINCT FROM` exists (verify).
- **Lab:** SQL-Z0.4: fill the 3VL table for `country <> 'US'` when country is NULL.
- **Check:** Does `NOT (x = 1)` include rows where x IS NULL? Prove with a truth table.

#### PQ-03 · Types, encodings, integer money vs float — stitch: M5
- [ ] done
- **Core:** Prefer `numeric`/`bigint` minor units for money; never `float`/`double` for currency. UTF-8; beware BOM and `char(n)` padding.
- **Theory:** Half-up vs banker rounding; IEEE recall from M5 then add decimal semantics.
- **GCP lens:** Lens-1: Cloud SQL flags for `extra_float_digits`; Spanner NUMERIC. Lens-2: lab stores `price_minor int`.
- **Lab:** SQL-E2.1 / SQL-E2.7: predict aggregates stay integer/numeric.
- **Check:** Why is `0.1 + 0.2` unsafe for money in float but fine as integer cents?

#### PQ-04 · Files, CSV/JSON, encodings — stitch: A3 + A6 · N2.5
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

#### PQ-07 · Sorting, hashing, trees, binary search as access-path raw material — stitch: A4 + U2 · DB-6
- [ ] done
- **Core:** These are the primitives behind indexes and joins — not a second CS course.
- **Theory:** Binary search → B-tree leaf walk; hash → hash join / hash index.
- **GCP lens:** Lens-1: recall only; formula depth in CS-02. Lens-2: none beyond paper.
- **Lab:** SQL-Z0.7, TD-10 fan-out arithmetic.
- **Check:** Given fan-out 100 and 1e6 leaves, about how many levels?

#### PQ-08 · Storage hierarchy & page/row arithmetic — stitch: A1/A2 recall + M6 · DB-4
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

#### RT-03 · Tuple/domain calculus & safety (SQL-T-GR) — stitch: A8 + A9 + U5 · DB-3
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
- **GCP lens:** Lens-1: Northstar OLTP stays ≥3NF; analytics star schemas deliberately denormalise (AN-01).
- **Lab:** TD-3, TD-4; SCH-1.
- **Check:** Is `product(tenant_id, sku, price, currency)` in BCNF if `tenant_id → currency`?

#### RT-06 · ER → tables — stitch: S2 + N0.4 · DD-01
- [ ] done
- **Core:** Entities, relationships, cardinality, weak entities, ISA → table patterns.
- **Theory:** Foreign-key placement for 1:N vs N:M.
- **GCP lens:** Lens-1: schema ADR in HLD pack. Lens-2: lab ER is Northstar OLTP slice.
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
- **Lab:** SQL-E3.1–SQL-E3.10; SQL-E6.4 as-of shape (leakage owner is N9c.1).
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
- **Core:** `INSERT…ON CONFLICT`, `UPDATE…FROM`, writable CTEs, `MERGE` (PG15+), `DELETE…RETURNING`.
- **Theory:** Idempotency keys; batching to bound WAL/bloat.
- **GCP lens:** Lens-1: Cloud SQL PG15 MERGE; Spanner mutations API vs SQL DML. Lens-2: E9.
- **Lab:** SQL-E9.1–SQL-E9.7; TX-5.
- **Check:** What uniqueness constraint makes an upsert actually idempotent?

#### SL-11 · Views, materialised views, functions, triggers — stitch: V-DATA + N9b.1
- [ ] done
- **Core:** Updatability limits; matview refresh; `SECURITY DEFINER` hazards; triggers as integrity amplifiers (use sparingly).
- **Theory:** Where business logic should *not* hide.
- **GCP lens:** Lens-1: BigQuery authorised views; AlloyDB matviews. Lens-2: SQL-E9.1 materialise daily GMV.
- **Lab:** SQL-E9.1; SCH-6 masking view sketch.
- **Check:** Name one reason a trigger is worse than a constraint for the same rule.

#### SL-12 · Dates, time zones, JSON, text, regex — stitch: N2.5 · D3 + N9c.1
- [ ] done
- **Core:** `timestamptz`, `AT TIME ZONE`, `date_trunc`, JSONB operators `@>`/`->`/`JSONB_PATH`, `LIKE`/`regex`.
- **Theory:** Never `now()` in reproducible labs; DST pitfalls.
- **GCP lens:** Lens-1: BigQuery `TIMESTAMP` vs `DATETIME`; Postgres JSONB vs Spanner JSON. Lens-2: E8.
- **Lab:** SQL-E8.1–SQL-E8.10.
- **Check:** Which direction of `AT TIME ZONE` converts *stored UTC* to a New York *civil* date?

#### SL-13 · Security in SQL: GRANT, RLS, injection — stitch: B5 · A10 · N8.1
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

#### CS-02 · B-tree/B+/hash/LSM/bitmap/GIN/GiST/BRIN — stitch: DB-6 · N8.1
- [ ] done
- **Core:** Height ≈ log_fanout(n); leftmost prefix rule; LSM write amp vs B-tree read amp; GIN for JSONB/arrays; BRIN for append-mostly.
- **Theory:** Partial and covering indexes.
- **GCP lens:** Lens-1: N8.1 owns LSM-vs-B-tree comparison toy; here formulas + PX cards. Lens-2: PX-1…PX-6.
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

#### CS-07 · Replication, consensus, 2PC, consistency models — stitch: DB-10 · A9 + V-STOR + N2.7 · ARCH-11
- [ ] done
- **Core:** Physical vs logical replication; failover; why 2PC is not the default answer (outbox owns the product pattern).
- **Theory:** TrueTime/Paxos *vocabulary* when A9 / N2.7 is unlocked — no second Spanner toy.
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

#### CS-09 · Columnar & vectorised execution — stitch: V-STOR + N9.4 · AN-02
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

#### DD-01 · Conceptual → logical → physical — stitch: S2 + N0.4 · N8.0
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

#### DD-03 · Money, units, time — stitch: A8 + N5.3 · M5
- [ ] done
- **Core:** Integer minor units; explicit currency; `timestamptz` for instants; civil dates as `date`.
- **Theory:** Never float money; never implicit TZ.
- **GCP lens:** Lens-1: ledger rules in N5.3 — this file models them. Lens-2: SQL-E4.5, SQL-CAP2.
- **Lab:** SQL-E4.5, SQL-CAP2.
- **Check:** Why store both `currency` and `total_minor` rather than a float USD conversion?

#### DD-04 · Hierarchies & graphs in SQL — stitch: SL-09
- [ ] done
- **Core:** Adjacency list, closure table, path enumeration, nested sets — trade-offs.
- **Theory:** Lab uses adjacency lists (`category.parent_id`, `app_user.referred_by`).
- **GCP lens:** Lens-1: when to leave for a graph DB (AN-06). Lens-2: E7.
- **Lab:** SQL-E7.1–SQL-E7.4; SCH-3.
- **Check:** Which hierarchy pattern makes 'subtree products' cheap?

#### DD-05 · Temporal data & SCD — stitch: D3 + N9c.1 · A8 + N5.3
- [ ] done
- **Core:** Valid-time vs transaction-time; SCD2 `valid_from`/`valid_to`; as-of join shapes.
- **Theory:** Leakage prevention is owned by N9c.1; SQL shapes live here.
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

#### DD-07 · Soft delete, audit, history — stitch: A8 + N5.3 · N11b
- [ ] done
- **Core:** `deleted_at`; history tables; append-only audit; who-can-see-deleted policies.
- **Theory:** Unique constraints must consider soft delete (`UNIQUE … WHERE deleted_at IS NULL`).
- **GCP lens:** Lens-1: control-plane audit in 11b. Lens-2: SQL-CAP1 invariants.
- **Lab:** SQL-E10.3 partial unique; SQL-CAP1.
- **Check:** How do you keep email unique among *live* users only?

#### DD-08 · Denormalisation with ADRs — stitch: S2 + N8.0 · primer SD-18
- [ ] done
- **Core:** Cache columns, aggregate tables, counter fields — only with refresh rules and ADR.
- **Theory:** Do not re-teach primer SD-18; add SQL maintenance patterns.
- **GCP lens:** Lens-1: materialised views / nightly jobs. Lens-2: SQL-E9.1 daily GMV.
- **Lab:** SCH-2, SQL-E9.1.
- **Check:** Write the refresh invariant for a cached `total_minor`.

#### DD-09 · Multi-tenancy — stitch: N8.1 · SL-13
- [ ] done
- **Core:** Shared tables + `tenant_id` vs separate DBs/schemas; composite FKs; RLS defence in depth.
- **Theory:** Hot-tenant skew.
- **GCP lens:** Lens-1: N8.1 owns RLS primitive; here SQL policies + composite FKs. Lens-2: SQL-E10.2, SQL-E10.6.
- **Lab:** SQL-E10.2, SQL-E10.6, PX-1 hot key.
- **Check:** Why is a single-column FK to `user_id` unsafe in a multi-tenant DB?

#### DD-10 · Partitioning & sharding-key design — stitch: primer SD-17 · A9 + V-STOR + N2.7
- [ ] done
- **Core:** Range/list/hash partitioning; prune-friendly predicates; shard key = join/locality key.
- **Theory:** Interview scale-out stays in primer SD-17; here SQL partition pruning.
- **GCP lens:** Lens-1: Cloud SQL declarative partitioning; Spanner parent keys. Lens-2: SCH-5.
- **Lab:** SCH-5; PX prune thought-experiment.
- **Check:** What predicate prevents partition pruning?

#### DD-11 · Schema evolution (expand/contract) — stitch: A8 + C4 + N2.6
- [ ] done
- **Core:** Add nullable → backfill → constrain → switch reads → drop old; lock levels; `CREATE INDEX CONCURRENTLY`; `NOT VALID`.
- **Theory:** N2.6 owns migrations-as-jobs; here lock/SQL craft.
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

#### DD-13 · Hot-key skew & partition keys — stitch: N8.1
- [ ] done
- **Core:** Measure skew with SQL; design keys that spread writes; avoid sequential hotspots.
- **Theory:** Lab: user 1 is hot (~135 orders) — see PX-1.
- **GCP lens:** Lens-1: N8.1 owns the hot-partition primitive. Lens-2: skew query on lab.
- **Lab:** PX-1; SCH-5.
- **Check:** Write a query that ranks users by order count and spot the hotspot.

### 4.6 Operating databases (OD-01 … OD-10)

#### OD-01 · Indexing strategy & EXPLAIN workflow — stitch: C6 · DB-6
- [ ] done
- **Core:** Hypothesis → `EXPLAIN (ANALYZE, BUFFERS)` → change one thing → re-measure; sargability.
- **Theory:** Never index every column.
- **GCP lens:** Lens-1: Query Insights. Lens-2: PX-1…PX-11, SQL-CAP4.
- **Lab:** §7.1 PX cards.
- **Check:** What four EXPLAIN fields do you read before changing an index?

#### OD-02 · Statistics & slow-query observability — stitch: C6
- [ ] done
- **Core:** `pg_stat_statements`, auto_explain, wait events; stale analyze symptoms.
- **Theory:** Logs are evidence packs, not vibes.
- **GCP lens:** Lens-1: Cloud Logging + Query Insights. Lens-2: PX-8 before/after ANALYZE.
- **Lab:** PX-8.
- **Check:** Name two symptoms of stale statistics.

#### OD-03 · Connection pooling & pool math — stitch: B3 · N8.1 · N2.3
- [ ] done
- **Core:** instances × pool ≤ `max_connections`; session vs transaction vs statement pooler modes; what breaks in transaction mode (session locals, prepared statements, advisory locks).
- **Theory:** N8.1 owns the spreadsheet — recall it.
- **GCP lens:** Lens-1: Cloud SQL + managed pooler / Auth Proxy. Lens-2: TX-8 thought-lab.
- **Lab:** TX-8.
- **Check:** Which pooler mode breaks `SET LOCAL` lasting across statements?

#### OD-04 · Backup / restore / PITR drills — stitch: DB-10 · N2.3 + DB-10
- [ ] done
- **Core:** Runbook literacy: schedule, retain, test restore to a *new* instance, measure RPO/RTO.
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

#### OD-08 · Migrations tooling & testing — stitch: A8 + C4 + N2.6 · C5
- [ ] done
- **Core:** Dirty state, advisory lock, expand/contract in CI, rollback story.
- **Theory:** gcp owns migrations-as-jobs; here SQL test discipline.
- **GCP lens:** Lens-1: Cloud Build job applying migrations. Lens-2: OD-10 CI fingerprint test.
- **Lab:** SQL-E9.6, SCH-4.
- **Check:** What does a migration advisory lock prevent?

#### OD-09 · Application data access — stitch: A7 · N8.1.5
- [ ] done
- **Core:** N+1, ORM dirty pages, prepared statements, transaction boundaries, keyset pagination SQL.
- **Theory:** N8.1.5 owns the from-scratch pager — here the seek predicate & index.
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

### 4.7 Analytics & other engines (AN-01 … AN-07)

#### AN-01 · OLTP vs OLAP; star/snowflake — stitch: A8 + V-STOR · N9.4
- [ ] done
- **Core:** Workload shapes; fact/dim; grain; conformed dimensions.
- **Theory:** Northstar OLTP lab vs analytics copies.
- **GCP lens:** Lens-1: Cloud SQL vs BigQuery decision table (A8 + V-STOR). Lens-2: SQL-E13.3 star build.
- **Lab:** SQL-E13.3; DT-1.
- **Check:** What is the grain of `order_line` vs `customer_order`?

#### AN-02 · BigQuery / GoogleSQL cost shapes — stitch: V-STOR + N9.4 · V-DATA + N9b.1
- [ ] done
- **Core:** Partition + cluster; selective column projection; bytes scanned as cost.
- **Theory:** gcp owns ops; here SQL-level reading.
- **GCP lens:** Lens-1: dry-run bytes. Lens-2: DT-2, SQL-E13.1.
- **Lab:** DT-2–DT-4.
- **Check:** Name two SQL mistakes that explode bytes scanned.

#### AN-03 · Cohorts, funnels, sessionisation, retention — stitch: V-DATA + N9b.1 · B4
- [ ] done
- **Core:** Windowed event math; billing-export-shaped windows reuse.
- **Theory:** Cohort month = trunc(signup); activation window is a half-open interval — same trap as SQL-E1.1.
- **GCP lens:** Lens-1: BQ SQL. Lens-2: SQL-E6.2, SQL-E6.6.
- **Lab:** SQL-E6.2, SQL-E6.6, DT-4.
- **Check:** Define activation as 'purchase within 7 days of signup' in SQL words.

#### AN-04 · Approximate aggregation — stitch: V-DATA + N9b.1
- [ ] done
- **Core:** `HLL`, t-digest / quantile sketches — error bars are part of the answer.
- **Theory:** Bias/variance trade-off; never mix approx and exact in one KPI without labelling.
- **GCP lens:** Lens-1: BQ `APPROX_COUNT_DISTINCT`. Lens-2: DT-5.
- **Lab:** DT-5.
- **Check:** When is a 2% count error unacceptable?

#### AN-05 · Spanner SQL dialect map — stitch: A9 + V-STOR + N2.7 · N9.4
- [ ] done
- **Core:** GoogleSQL in Spanner: types, interleaved joins, no arbitrary cross-DB features.
- **Theory:** Same *question* as Postgres — different spelling and limits.
- **GCP lens:** Lens-1: Spanner emulator when Lab Reality allows. Lens-2: DT-6.
- **Lab:** DT-6.
- **Check:** Name two Postgres features you must rewrite for Spanner.

#### AN-06 · NoSQL query models vs SQL — stitch: A8 + N2.4
- [ ] done
- **Core:** Document / KV access patterns; what joins become application fan-out.
- **Theory:** Firestore when it wins/loses — gcp owns product; here same-question drill.
- **GCP lens:** Lens-1: Firestore. Lens-2: DT-7.
- **Lab:** DT-7.
- **Check:** Express 'top 10 products by GMV for tenant 2' as a document access plan and as SQL.

#### AN-07 · Search & vectors in SQL — stitch: D4 + N9c.2 / N9c.5
- [ ] done
- **Core:** `tsvector`/`tsquery`; `pgvector` similarity — vs dedicated search engines.
- **Theory:** Ranking quality, hybrid lexical+vector, and operational isolation from OLTP.
- **GCP lens:** Lens-1: Vertex matching vs in-DB vectors (trade-offs). Lens-2: DT-8 sketch.
- **Lab:** DT-8.
- **Check:** When does in-DB vector search stop being enough?
## 5. Skip tests / readiness tiers (SQL-SKIP-SQL / SQL-SKIP-ENGINE)

Mapped to the A8 skip-tests **SQL-SKIP-SQL** / **SQL-SKIP-ENGINE** (provenance: `unified-curriculum.md` nodes `DB-SQL` / `DB-ENGINE`). If the A8 sessions already confirmed the skill, **stamp and skip**; else run the order in §2.3.

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

**Bank ≠ dump** (§0.2 rule 5): issue **one** item at the ledger rung; learner attempts; escalate hints; only then Appendix K. Every read-only golden below is from `goldens_ex_*.json` executed on PostgreSQL 15.8 / seed v1 / UTC / C collation.

### 6.0 Level 0 — paper drills (SQL-Z0.*)

No database. Predict on paper; then optionally confirm later. Gate: PQ modules as tagged.

#### SQL-Z0.1 · Bag vs set multiplicity
- **Tags:** PQ-01
- **Prompt:** On paper: relation R={1,1,2} as a bag. Compute R ∪ R, R ∪_set R, π(R).
- **Output shape:** multiplicity table
- **Trap:** Calling SQL UNION without noticing it is set-union.
- **Golden fingerprint:** _(paper — no `lab.chk`)_
- **Prereq gate:** matching PQ unlocked

#### SQL-Z0.2 · Join cardinality bound
- **Tags:** PQ-01·RT-01
- **Prompt:** R has 4 rows, S has 6, join key has 2 distinct values with skew 3/1 on R and 4/2 on S. Bound |R⋈S|.
- **Output shape:** integer bound + sketch
- **Trap:** Using |R|·|S| as the *answer* rather than the upper bound.
- **Golden fingerprint:** _(paper — no `lab.chk`)_
- **Prereq gate:** matching PQ unlocked

#### SQL-Z0.3 · Function vs relation
- **Tags:** PQ-01
- **Prompt:** Is `email → user_id` a function on lab UNIQUE(tenant_id,email)? Explain.
- **Output shape:** one paragraph
- **Trap:** Forgetting the tenant is part of the key.
- **Golden fingerprint:** _(paper — no `lab.chk`)_
- **Prereq gate:** matching PQ unlocked

#### SQL-Z0.4 · 3VL truth table
- **Tags:** PQ-02·SL-03
- **Prompt:** Fill TRUE/FALSE/UNKNOWN for `country = 'US'`, `country <> 'US'`, `NOT (country = 'US')` when country is NULL.
- **Output shape:** 3×3 table
- **Trap:** Treating UNKNOWN as FALSE.
- **Golden fingerprint:** _(paper — no `lab.chk`)_
- **Prereq gate:** matching PQ unlocked

#### SQL-Z0.5 · Counting distinct pairs
- **Tags:** PQ-01
- **Prompt:** How many ordered pairs (user, product) if 2000 users and 500 products? How many if each user orders ≤4 products (lab-ish)?
- **Output shape:** two integers
- **Trap:** Confusing domain product with observed fact table size.
- **Golden fingerprint:** _(paper — no `lab.chk`)_
- **Prereq gate:** matching PQ unlocked

#### SQL-Z0.6 · Predicate safety
- **Tags:** PQ-02
- **Prompt:** Which of `{x | x=x}`, `{x | ∃y R(x,y)}` are safe? Why?
- **Output shape:** safe/unsafe labels
- **Trap:** Equating 'true of everything' with a finite SQL result.
- **Golden fingerprint:** _(paper — no `lab.chk`)_
- **Prereq gate:** matching PQ unlocked

#### SQL-Z0.7 · Binary search steps
- **Tags:** PQ-07
- **Prompt:** Sorted 1e6 keys, fan-out 1 (binary search). Approx comparisons? Then fan-out 100 B-tree height?
- **Output shape:** two numbers
- **Trap:** Using ln vs log2 casually without stating base.
- **Golden fingerprint:** _(paper — no `lab.chk`)_
- **Prereq gate:** matching PQ unlocked

#### SQL-Z0.8 · Pages napkin
- **Tags:** PQ-08·CS-01
- **Prompt:** 20k orders × 150 B/row, 8 KiB pages, 90% fill. Approx pages? Compare to 1 RAM GB.
- **Output shape:** pages + fit/not
- **Trap:** Forgetting fill-factor.
- **Golden fingerprint:** _(paper — no `lab.chk`)_
- **Prereq gate:** matching PQ unlocked

### 6.0b Theory drills (TD-1 … TD-16)

Issued one at a time with the A8 + A9 (+ U5) theory and the §4.0 slices. Keys in Appendix K (sketches).

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
- **Prereq gate:** Level 1 gate above; stitch partners from §2 as tagged

#### SQL-E1.2 · Unknown country
- **Tags:** NULL · IS NULL
- **Prompt:** Users whose country is unknown (stored as NULL).
- **Output shape:** `user_id` (order-insensitive — `lab.chk`)
- **Trap:** `country = NULL` is never true — it is UNKNOWN. Also note `char(2)` pads; do not compare with `''`.
- **Golden fingerprint:** `181:ab2f2d8e`
- **Prereq gate:** Level 1 gate above; stitch partners from §2 as tagged

#### SQL-E1.3 · Everyone not known to be in the US
- **Tags:** NULL · 3VL · IS DISTINCT FROM
- **Prompt:** All users who are not known to be in the US — this **includes** users whose country is unknown.
- **Output shape:** `user_id` (order-insensitive — `lab.chk`)
- **Trap:** `country <> 'US'` drops the NULL-country users (UNKNOWN is not TRUE). Use `IS DISTINCT FROM`, or `country <> 'US' OR country IS NULL`. Write the 3VL truth table for `NOT (country = 'US')` first. Wrong-path fingerprint (do not chase): `1559:c2797d13` — `<>` instead of IS DISTINCT FROM.
- **Golden fingerprint:** `1740:d7106dd7`
- **Prereq gate:** Level 1 gate above; stitch partners from §2 as tagged

#### SQL-E1.4 · Mid-priced live catalogue, top 20
- **Tags:** WHERE · ORDER BY · LIMIT · determinism
- **Prompt:** Products with `price_minor` from 1000 to 2000 inclusive that are not discontinued, most expensive first, ties broken by lowest `product_id`; first 20 rows only.
- **Output shape:** `product_id, price_minor` (ordered) (ordered — use `lab.chk_o`)
- **Trap:** `LIMIT` without a total order is non-deterministic. `discontinued_at IS NULL`, not `= NULL`. Both bounds are inclusive here (integer money, so `BETWEEN` is safe).
- **Golden fingerprint:** `20:1af04ff2`
- **Prereq gate:** Level 1 gate above; stitch partners from §2 as tagged

#### SQL-E1.5 · Reviews with no text
- **Tags:** NULL vs empty string · COALESCE
- **Prompt:** Reviews whose body is missing — treat NULL and the empty string as the same thing.
- **Output shape:** `review_id` (order-insensitive — `lab.chk`)
- **Trap:** NULL and `''` are different values; a test for one silently misses the other. In Oracle they collapse into one — a dialect trap (see the Rosetta table).
- **Golden fingerprint:** `2036:aa6dda6b`
- **Prereq gate:** Level 1 gate above; stitch partners from §2 as tagged

#### SQL-E1.6 · Order status buckets
- **Tags:** CASE · expressions
- **Prompt:** Label every order: `open` for created/paid, `done` for fulfilled, `closed` for cancelled/refunded.
- **Output shape:** `order_id, bucket` (order-insensitive — `lab.chk`)
- **Trap:** A `CASE` without `ELSE` yields NULL for unmatched values — add a defensive `ELSE 'unknown'` and say why it should never fire (the `CHECK` constraint).
- **Golden fingerprint:** `20000:a58f4910`
- **Prereq gate:** Level 1 gate above; stitch partners from §2 as tagged

#### SQL-E1.7 · Ten priciest live products
- **Tags:** ORDER BY · LIMIT · tie-break
- **Prompt:** The ten most expensive products that are not discontinued (ties → lowest `product_id`).
- **Output shape:** `product_id, price_minor` (ordered) (ordered — use `lab.chk_o`)
- **Trap:** Sorting by price alone and hoping. State the tie-break in the spec *before* you write the query.
- **Golden fingerprint:** `10:558e94b1`
- **Prereq gate:** Level 1 gate above; stitch partners from §2 as tagged

#### SQL-E1.8 · Pattern search
- **Tags:** LIKE · ILIKE · escaping
- **Prompt:** Products whose SKU starts with `SKU-01` and ends with `7`.
- **Output shape:** `product_id` (order-insensitive — `lab.chk`)
- **Trap:** `_` and `%` are wildcards — to match a literal underscore you need `ESCAPE`. A leading-wildcard pattern (`'%7'`) cannot use a B-tree index (see the PX-3 prediction card).
- **Golden fingerprint:** `10:986cf4ec`
- **Prereq gate:** Level 1 gate above; stitch partners from §2 as tagged

### 6.2 Level 2 — Aggregation

**Prereq gate:** SQL-E1 gate passed; SL-05

#### SQL-E2.1 · Orders and revenue by status
- **Tags:** GROUP BY · SUM
- **Prompt:** For each order status: number of orders and the sum of `total_minor`.
- **Output shape:** `status, n_orders, sum_minor` (order-insensitive — `lab.chk`)
- **Trap:** Every non-aggregated SELECT column must be in GROUP BY (or functionally dependent on the PK). Money is an integer of minor units — never `float`.
- **Golden fingerprint:** `5:2495a69d`
- **Prereq gate:** Level 2 gate above; stitch partners from §2 as tagged

#### SQL-E2.2 · Monthly fulfilled GMV, 2025
- **Tags:** date_trunc · GROUP BY · time zones
- **Prompt:** For fulfilled orders placed in calendar 2025 (UTC): month start, order count, and GMV (`sum(total_minor)`).
- **Output shape:** `month, n_orders, gmv_minor` (order-insensitive — `lab.chk`)
- **Trap:** `date_trunc('month', timestamptz)` uses the **session** time zone. The lab pins `UTC`; production rarely does — always state the zone.
- **Golden fingerprint:** `12:c6eb674e`
- **Prereq gate:** Level 2 gate above; stitch partners from §2 as tagged

#### SQL-E2.3 · Well-reviewed products
- **Tags:** HAVING · WHERE vs HAVING · ROUND
- **Prompt:** Products with at least 10 reviews: review count and average rating rounded to 2 decimals.
- **Output shape:** `product_id, n, avg_rating` (order-insensitive — `lab.chk`)
- **Trap:** `WHERE` filters rows *before* grouping, `HAVING` filters groups *after*. `avg(smallint)` is `numeric`, so `round(avg(rating), 2)` works; in engines with integer division check the type.
- **Golden fingerprint:** `467:68a601d1`
- **Prereq gate:** Level 2 gate above; stitch partners from §2 as tagged

#### SQL-E2.4 · Buyers per tenant
- **Tags:** COUNT(DISTINCT) · count(*) vs count(col)
- **Prompt:** Per tenant: number of orders and number of *distinct* users who placed at least one order.
- **Output shape:** `tenant_id, n_orders, n_buyers` (order-insensitive — `lab.chk`)
- **Trap:** `count(*)` counts rows, `count(col)` skips NULLs, `count(DISTINCT col)` de-duplicates. Say which one each output column needs.
- **Golden fingerprint:** `5:0cf3aaa2`
- **Prereq gate:** Level 2 gate above; stitch partners from §2 as tagged

#### SQL-E2.5 · Refund rate by tenant
- **Tags:** FILTER · conditional aggregation · integer division
- **Prompt:** Per tenant: total orders, refunded orders, and refund rate = refunded / total rounded to 4 decimals.
- **Output shape:** `tenant_id, n_orders, n_refunded, refund_rate` (order-insensitive — `lab.chk`)
- **Trap:** `1/3` in integer arithmetic is 0. Cast one side to `numeric` *before* dividing. `count(*) FILTER (WHERE …)` is the standard-SQL way; `SUM(CASE …)` is the portable way. Wrong-path fingerprint (do not chase): `5:b83b6ee2` — integer division.
- **Golden fingerprint:** `5:9fbfe463`
- **Prereq gate:** Level 2 gate above; stitch partners from §2 as tagged

#### SQL-E2.6 · Users by country including unknown
- **Tags:** GROUP BY NULL · COALESCE
- **Prompt:** Number of users per country; label unknown as `'??'`.
- **Output shape:** `country, n` (order-insensitive — `lab.chk`)
- **Trap:** GROUP BY puts all NULLs in **one** group (unlike `=`). `country` is `char(2)` so `'US'` and `'US '` compare equal — but `coalesce(country,'??')` must be a valid `char(2)`.
- **Golden fingerprint:** `8:94127f65`
- **Prereq gate:** Level 2 gate above; stitch partners from §2 as tagged

#### SQL-E2.7 · Median order value per tenant
- **Tags:** ordered-set aggregates · percentile_disc
- **Prompt:** Per tenant, the median `total_minor` of fulfilled orders, defined as `percentile_disc(0.5)` (an actual value from the data).
- **Output shape:** `tenant_id, median_minor` (order-insensitive — `lab.chk`)
- **Trap:** `avg` is not the median. `percentile_cont` interpolates and returns `double precision` — a float in a money pipeline. State which definition you use.
- **Golden fingerprint:** `5:74a001bd`
- **Prereq gate:** Level 2 gate above; stitch partners from §2 as tagged

#### SQL-E2.8 · Price histogram
- **Tags:** bucketing · integer division
- **Prompt:** Bucket **live** products (not discontinued) into price bands of width 1000 minor units: band start (0, 1000, 2000, …) and product count.
- **Output shape:** `band_start, n` (order-insensitive — `lab.chk`)
- **Trap:** `price_minor / 1000 * 1000` relies on integer division truncation — fine in Postgres, wrong in engines that return decimals (dialect trap). `width_bucket` is the explicit alternative.
- **Golden fingerprint:** `10:dc13b2c1`
- **Prereq gate:** Level 2 gate above; stitch partners from §2 as tagged

### 6.3 Level 3 — Joins

**Prereq gate:** SQL-E2 gate; SL-04

#### SQL-E3.1 · Paid orders with buyer and tenant
- **Tags:** INNER JOIN · multi-table
- **Prompt:** Orders with status `paid` placed in March 2025, tenant 2: order id, buyer email, tenant name, total.
- **Output shape:** `order_id, email, tenant_name, total_minor` (order-insensitive — `lab.chk`)
- **Trap:** Filter on the *driving* table in WHERE; join keys go in ON. Three tables, two ON clauses — write the join graph as a picture first.
- **Golden fingerprint:** `50:787a0b9d`
- **Prereq gate:** Level 3 gate above; stitch partners from §2 as tagged

#### SQL-E3.2 · Users who never referred anyone
- **Tags:** anti-join · NOT IN + NULL trap
- **Prompt:** Users who are not the referrer of any other user.
- **Output shape:** `user_id` (order-insensitive — `lab.chk`)
- **Trap:** `WHERE user_id NOT IN (SELECT referred_by FROM app_user)` returns **zero rows** because `referred_by` contains NULLs (`x NOT IN (…, NULL)` is never TRUE). Write it three ways: NOT EXISTS, LEFT JOIN … IS NULL, and NOT IN with a NULL filter — all three must give the same fingerprint. Wrong-path fingerprint (do not chase): `0:d41d8cd9` — NOT IN over a column containing NULL.
- **Golden fingerprint:** `1291:ce8f0411`
- **Prereq gate:** Level 3 gate above; stitch partners from §2 as tagged

#### SQL-E3.3 · Users who never ordered
- **Tags:** LEFT JOIN … IS NULL · anti-join
- **Prompt:** Users with no order at all (any status).
- **Output shape:** `user_id` (order-insensitive — `lab.chk`)
- **Trap:** Test the *right-hand primary key* for NULL, not a column that can legitimately be NULL on the right.
- **Golden fingerprint:** `200:e5ab3ae1`
- **Prereq gate:** Level 3 gate above; stitch partners from §2 as tagged

#### SQL-E3.4 · Products not sold in a week
- **Tags:** anti-join · date ranges
- **Prompt:** Products that appear on **no** order line of a fulfilled order placed during 2025-01-01 … 2025-01-07 (inclusive, UTC).
- **Output shape:** `product_id` (order-insensitive — `lab.chk`)
- **Trap:** Where does the date filter go? Inside the `NOT EXISTS` subquery (or the `ON` of the LEFT JOIN) — not in the outer WHERE, where it would turn the anti-join into an inner join.
- **Golden fingerprint:** `180:d18c224e`
- **Prereq gate:** Level 3 gate above; stitch partners from §2 as tagged

#### SQL-E3.5 · Revenue of delivered orders
- **Tags:** semi-join · fan-out trap
- **Prompt:** Total `total_minor` of fulfilled orders that have **at least one** delivered shipment (`delivered_at IS NOT NULL`). One number.
- **Output shape:** `revenue_minor` (order-insensitive — `lab.chk`)
- **Trap:** `JOIN shipment` fans out: orders with two shipments are counted twice. Semi-join (`EXISTS`) never multiplies rows. Compute the naive join answer too and explain the difference in one sentence. Wrong-path fingerprint (do not chase): `1:20e027c7` — plain JOIN fans out orders with two shipments.
- **Golden fingerprint:** `1:6c39466d`
- **Prereq gate:** Level 3 gate above; stitch partners from §2 as tagged

#### SQL-E3.6 · Cross-tenant referrals
- **Tags:** self-join · data-quality find
- **Prompt:** Users whose referrer belongs to a **different tenant**. This is a multi-tenancy integrity leak, not a feature.
- **Output shape:** `user_id, referrer_id` (order-insensitive — `lab.chk`)
- **Trap:** Alias the same table twice (`u`, `r`) and name the join direction aloud. Then: which constraint would have prevented this? (A composite FK `(tenant_id, referred_by) → (tenant_id, user_id)`.)
- **Golden fingerprint:** `1172:9f8ebbd0`
- **Prereq gate:** Level 3 gate above; stitch partners from §2 as tagged

#### SQL-E3.7 · One-star counts including zeros
- **Tags:** LEFT JOIN · filter in ON · empty groups
- **Prompt:** For **every** product of tenant 1 (all of them), the number of 1-star reviews it has — 0 where none.
- **Output shape:** `product_id, one_star` (order-insensitive — `lab.chk`)
- **Trap:** `LEFT JOIN review r … WHERE r.rating = 1` deletes the zero rows (the WHERE re-filters the NULL-extended rows). Put the predicate in `ON`, or use `count(*) FILTER`. `count(r.review_id)`, not `count(*)`. Wrong-path fingerprint (do not chase): `98:43c02740` — rating filter in WHERE after the LEFT JOIN.
- **Golden fingerprint:** `100:1b05fa94`
- **Prereq gate:** Level 3 gate above; stitch partners from §2 as tagged

#### SQL-E3.8 · Who ordered vs who reviewed (Q1 2025)
- **Tags:** FULL OUTER JOIN · reconciliation
- **Prompt:** For 2025 Q1 (Jan–Mar UTC): every user who placed **or** reviewed, with two booleans — did they order, did they review.
- **Output shape:** `user_id, ordered, reviewed` (order-insensitive — `lab.chk`)
- **Trap:** `COALESCE` the two join keys; a FULL JOIN yields NULL on the missing side. Pre-aggregate each side to one row per user *before* joining.
- **Golden fingerprint:** `1845:6f7a9372`
- **Prereq gate:** Level 3 gate above; stitch partners from §2 as tagged

#### SQL-E3.9 · Deletions per month with zero-fill
- **Tags:** calendar spine · generate_series · LEFT JOIN
- **Prompt:** For every month from 2024-05 through 2025-06 (inclusive, 14 rows), the number of users deleted (`deleted_at`) in that month — including months with zero.
- **Output shape:** `month, n_deleted` (order-insensitive — `lab.chk`)
- **Trap:** Group the fact table alone and empty months vanish. Generate the spine first (`generate_series`), then LEFT JOIN facts onto it.
- **Golden fingerprint:** `14:cb9ff4e8`
- **Prereq gate:** Level 3 gate above; stitch partners from §2 as tagged

#### SQL-E3.10 · Duplicate-safe reviewers per product
- **Tags:** multiplicity · DISTINCT vs GROUP BY
- **Prompt:** Per product: distinct reviewers and total reviews, only products where those two numbers differ.
- **Output shape:** `product_id, n_reviewers, n_reviews` (order-insensitive — `lab.chk`)
- **Trap:** A user may review the same product several times in this seed (see SQL-E9.4). `count(*)` ≠ `count(DISTINCT user_id)` exactly there.
- **Golden fingerprint:** `241:47e3b13f`
- **Prereq gate:** Level 3 gate above; stitch partners from §2 as tagged

### 6.4 Level 4 — Subqueries, CTEs, set ops

**Prereq gate:** SQL-E3 gate; SL-06, SL-07

#### SQL-E4.1 · Above-average spenders
- **Tags:** scalar subquery · CTE
- **Prompt:** Users whose total fulfilled spend is strictly greater than the average spend **across users who spent anything** (exclude users with no fulfilled orders from the average).
- **Output shape:** `user_id, spend_minor` (order-insensitive — `lab.chk`)
- **Trap:** What is the denominator? Users with zero orders shift the average if you `LEFT JOIN` them in. Write down which population you average over.
- **Golden fingerprint:** `675:19348832`
- **Prereq gate:** Level 4 gate above; stitch partners from §2 as tagged

#### SQL-E4.2 · Latest review rating per product
- **Tags:** correlated subquery · DISTINCT ON
- **Prompt:** For each product that has reviews: the rating of its most recent review (newest `created_at`; ties → highest `review_id`).
- **Output shape:** `product_id, rating` (order-insensitive — `lab.chk`)
- **Trap:** `max(created_at)` alone does not give you the rating from that row. Use a correlated subquery, `DISTINCT ON`, or a window (SQL-E5.4) — then prove they agree.
- **Golden fingerprint:** `500:7463fec9`
- **Prereq gate:** Level 4 gate above; stitch partners from §2 as tagged

#### SQL-E4.3 · Both fulfilled and refunded
- **Tags:** EXISTS · INTERSECT
- **Prompt:** Users who have at least one fulfilled order **and** at least one refunded order.
- **Output shape:** `user_id` (order-insensitive — `lab.chk`)
- **Trap:** Two `EXISTS` clauses (or `INTERSECT`). A single `JOIN` with `status IN ('fulfilled','refunded')` finds users with *either*.
- **Golden fingerprint:** `391:6319def9`
- **Prereq gate:** Level 4 gate above; stitch partners from §2 as tagged

#### SQL-E4.4 · Reviewed but never bought
- **Tags:** EXCEPT · NOT EXISTS · set semantics
- **Prompt:** Distinct `(user_id, product_id)` pairs where the user reviewed the product but has **no** order line for it (in any of their orders, any status).
- **Output shape:** `user_id, product_id` (order-insensitive — `lab.chk`)
- **Trap:** `EXCEPT` removes duplicates and needs identical column lists; `EXCEPT ALL` is the bag version. Solve with both `EXCEPT` and `NOT EXISTS`.
- **Golden fingerprint:** `4559:2e92d1fa`
- **Prereq gate:** Level 4 gate above; stitch partners from §2 as tagged

#### SQL-E4.5 · Net revenue per tenant without double counting
- **Tags:** CTE · pre-aggregation · fan-out
- **Prompt:** Per tenant: GMV of fulfilled and refunded orders placed in 2025 (`sum(total_minor)`), sum of **succeeded refund** payments on those orders, and net = gmv − refunds.
- **Output shape:** `tenant_id, gmv_minor, refunded_minor, net_minor` (order-insensitive — `lab.chk`)
- **Trap:** orders → payments is 1:N. Joining orders to payments and summing `total_minor` counts each order once per payment row. Aggregate each side **separately in CTEs**, then join on the key. Wrong-path fingerprint (do not chase): `5:45fe10e3` — orders JOIN payments then SUM(total_minor).
- **Golden fingerprint:** `5:77344493`
- **Prereq gate:** Level 4 gate above; stitch partners from §2 as tagged

#### SQL-E4.6 · Strictly the priciest in its category
- **Tags:** ALL · empty-set trap
- **Prompt:** Products strictly more expensive than every *other* product in the same category. Uncategorised products (NULL category) are excluded.
- **Output shape:** `product_id` (order-insensitive — `lab.chk`)
- **Trap:** `x > ALL (empty set)` is TRUE. For a NULL category the peer set is empty, so every uncategorised product qualifies unless you exclude them explicitly. Also: ties give no winner. Wrong-path fingerprint (do not chase): `68:6cff1edf` — forgetting that ALL over an empty set is TRUE.
- **Golden fingerprint:** `30:d5ca9e54`
- **Prereq gate:** Level 4 gate above; stitch partners from §2 as tagged

#### SQL-E4.7 · Latest order per user (tenant 3)
- **Tags:** LATERAL · top-1 per group
- **Prompt:** For each user of tenant 3 who has orders: their most recent order (`placed_at DESC`, tie → higher `order_id`).
- **Output shape:** `user_id, order_id, placed_at` (order-insensitive — `lab.chk`)
- **Trap:** `LATERAL` runs the subquery once per outer row and can reference it — the SQL for-each loop. Missing index on `(user_id, placed_at)` makes it a seq scan per user (PX-1).
- **Golden fingerprint:** `360:3dd4aace`
- **Prereq gate:** Level 4 gate above; stitch partners from §2 as tagged

#### SQL-E4.8 · Relational division: bought all three
- **Tags:** division · GROUP BY / HAVING · double NOT EXISTS
- **Prompt:** Users who have ordered **all** of products 1, 6 and 11 (any status).
- **Output shape:** `user_id` (order-insensitive — `lab.chk`)
- **Trap:** Division has two standard forms: `HAVING count(DISTINCT product_id) = 3` (fast, needs the count) and double `NOT EXISTS` (works for a *set stored in a table*). Write both.
- **Golden fingerprint:** `5:286c82f6`
- **Prereq gate:** Level 4 gate above; stitch partners from §2 as tagged

### 6.5 Level 5 — Window functions

**Prereq gate:** SQL-E4 gate; SL-08

#### SQL-E5.1 · Top-3 price ranks per category
- **Tags:** dense_rank · rank vs row_number
- **Prompt:** For every category (ignore uncategorised products): products whose **dense** price rank (highest price = 1) is 1, 2 or 3 within the category.
- **Output shape:** `category_id, product_id, price_minor, rnk` (order-insensitive — `lab.chk`)
- **Trap:** `rank` leaves gaps after ties, `dense_rank` doesn't, `row_number` breaks ties arbitrarily. You cannot filter on a window function in WHERE — wrap in a subquery/CTE.
- **Golden fingerprint:** `90:0444fd32`
- **Prereq gate:** Level 5 gate above; stitch partners from §2 as tagged

#### SQL-E5.2 · Running GMV, tenant 1, March 2025
- **Tags:** running total · frame · aggregate then window
- **Prompt:** Tenant 1, fulfilled orders placed in March 2025: per UTC day the GMV, plus the cumulative GMV since 1 March.
- **Output shape:** `day, gmv_minor, cum_gmv_minor` (ordered by day) (ordered — use `lab.chk_o`)
- **Trap:** Aggregate to days **first** (CTE), then window over the days. The default frame with `ORDER BY` is `RANGE UNBOUNDED PRECEDING … CURRENT ROW` — peers (ties) are included; spell `ROWS` when you mean rows.
- **Golden fingerprint:** `31:1c8f130e`
- **Prereq gate:** Level 5 gate above; stitch partners from §2 as tagged

#### SQL-E5.3 · Days since the previous order
- **Tags:** lag · partitions
- **Prompt:** For users 1–20: each order with the number of whole days since the same user's previous order (NULL for their first). Use calendar days (`placed_at::date`).
- **Output shape:** `user_id, order_id, placed_at, gap_days` (order-insensitive — `lab.chk`)
- **Trap:** `lag` needs a total order inside the partition — add `order_id` as tie-break. `date - date` is an integer in Postgres; timestamp − timestamp is an interval.
- **Golden fingerprint:** `996:d7137b70`
- **Prereq gate:** Level 5 gate above; stitch partners from §2 as tagged

#### SQL-E5.4 · Top-2 orders per user
- **Tags:** row_number · top-N per group
- **Prompt:** For users 1–50: their two largest orders by `total_minor` (ties → lower `order_id`), with the position 1 or 2.
- **Output shape:** `user_id, order_id, total_minor, rn` (order-insensitive — `lab.chk`)
- **Trap:** `LIMIT 2` gives two rows overall, not per user. The tie-break is part of the spec — without it two correct answers differ.
- **Golden fingerprint:** `100:8a1679d3`
- **Prereq gate:** Level 5 gate above; stitch partners from §2 as tagged

#### SQL-E5.5 · Tenant share of 2025 GMV
- **Tags:** sum() OVER () · ratio to total
- **Prompt:** Per tenant: fulfilled GMV in 2025 and its percentage of the all-tenant total, rounded to 2 decimals.
- **Output shape:** `tenant_id, gmv_minor, pct` (order-insensitive — `lab.chk`)
- **Trap:** Window over the *aggregated* result: `sum(sum(x)) OVER ()`. Cast to numeric before dividing.
- **Golden fingerprint:** `5:4bec02c5`
- **Prereq gate:** Level 5 gate above; stitch partners from §2 as tagged

#### SQL-E5.6 · Price quartiles, tenant 2
- **Tags:** ntile · bucket boundaries
- **Prompt:** Live products of tenant 2 split into 4 price quartiles with `ntile(4)` ordered by price ascending then `product_id`.
- **Output shape:** `product_id, price_minor, quartile` (order-insensitive — `lab.chk`)
- **Trap:** `ntile` splits by **row count**, not by value — equal prices can land in different tiles; and if N is not divisible by 4 the first tiles get the extra rows.
- **Golden fingerprint:** `94:71892706`
- **Prereq gate:** Level 5 gate above; stitch partners from §2 as tagged

#### SQL-E5.7 · First and last price
- **Tags:** first_value · last_value · frame trap
- **Prompt:** For products 1–20: the first and last `price_minor` in `product_price_history` (by `valid_from`) and the change (last − first).
- **Output shape:** `product_id, first_price, last_price, delta` (order-insensitive — `lab.chk`)
- **Trap:** `last_value(x) OVER (ORDER BY t)` returns the *current* row when the default frame stops at CURRENT ROW. You need `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`, or use `first_value` with a reversed ORDER BY. Wrong-path fingerprint (do not chase): `60:99a2d437` — last_value with the default frame.
- **Golden fingerprint:** `20:7ddcb09e`
- **Prereq gate:** Level 5 gate above; stitch partners from §2 as tagged

#### SQL-E5.8 · 7-day moving average of daily orders
- **Tags:** ROWS frame · moving average · warm-up rows
- **Prompt:** Tenant 2, orders placed in February 2025: per day the order count and the average of the current and previous 6 days' counts, rounded to 2 decimals. Emit the average only when a full 7-day window exists inside February (from 7 Feb).
- **Output shape:** `day, n, avg7` (ordered by day) (ordered — use `lab.chk_o`)
- **Trap:** A `ROWS 6 PRECEDING` frame silently shrinks at the start — you must suppress the warm-up rows yourself. `ROWS` counts rows, so missing days (gaps) would silently stretch the window; here there are no empty days — say why you checked.
- **Golden fingerprint:** `22:55be0551`
- **Prereq gate:** Level 5 gate above; stitch partners from §2 as tagged

### 6.6 Level 6 — Advanced windows

**Prereq gate:** SQL-E5 gate; SL-08 frames

#### SQL-E6.1 · Longest login streak
- **Tags:** gaps and islands · row_number difference
- **Prompt:** From `login_day` (users 1–200, 120 days): each user's longest run of **consecutive** days and the day it started (earliest start on ties).
- **Output shape:** `user_id, streak_len, streak_start` (order-insensitive — `lab.chk`)
- **Trap:** Consecutive days share a constant `day − row_number()`. Do not use `count(*)` per user, and do not forget that the PK already guarantees no duplicate days (if it didn't, dedupe before numbering).
- **Golden fingerprint:** `200:3d4d4f51`
- **Prereq gate:** Level 6 gate above; stitch partners from §2 as tagged

#### SQL-E6.2 · Sessionise the event stream
- **Tags:** sessionization · lag · cumulative sum
- **Prompt:** For identified users (`user_id IS NOT NULL`): a new session starts when the gap to the user's previous event is **> 30 minutes** (or there is no previous event). Return one row per session: user, session number (1-based per user, by time), event count, first and last event time.
- **Output shape:** `user_id, session_no, n_events, started_at, ended_at` (order-insensitive — `lab.chk`)
- **Trap:** Three steps: (1) `lag` to get the gap, (2) flag `gap > interval '30 minutes' OR gap IS NULL`, (3) running `sum(flag)` as the session id. Ties on `occurred_at` need an `event_id` tie-break.
- **Golden fingerprint:** `7500:311fb683`
- **Prereq gate:** Level 6 gate above; stitch partners from §2 as tagged

#### SQL-E6.3 · Ordered funnel
- **Tags:** conditional aggregation · ordered steps
- **Prompt:** How many identified users performed `add_to_cart`, later `checkout_start`, later `purchase` — in that order (each step strictly after the previous, using each user's **first** occurrence of the step)? One number, plus the counts that reached step 1 and step 2 as a funnel.
- **Output shape:** `n_cart, n_checkout, n_purchase` (one row) (order-insensitive — `lab.chk`)
- **Trap:** `count(DISTINCT user_id) WHERE event_type = …` per step ignores order. Compute each user's first time per step with `min(…) FILTER`, then compare the timestamps.
- **Golden fingerprint:** `1:2f3673b3`
- **Prereq gate:** Level 6 gate above; stitch partners from §2 as tagged

#### SQL-E6.4 · Price in effect at order time (as-of join)
- **Tags:** as-of join · LATERAL · temporal correctness
- **Prompt:** For order lines of orders placed **before 2025-01-04**: the list price that was in effect at `placed_at` (the history row with the greatest `valid_from <= placed_at`), and the lines where the price actually charged (`unit_price_minor`) differs from it.
- **Output shape:** `order_id, line_no, unit_price_minor, price_at_order` (order-insensitive — `lab.chk`)
- **Trap:** A plain equi-join on `product_id` returns three rows per line. Use `LATERAL … ORDER BY valid_from DESC LIMIT 1` (or `DISTINCT ON`, or a window). The `<=` boundary is inclusive: an order at exactly `valid_from` sees the *new* price. This is the same shape as **N9c.1** (D3) point-in-time joins. Wrong-path fingerprint (do not chase): `808:97a9c21a` — plain equi-join returns all three price rows.
- **Golden fingerprint:** `404:4f5a2a10`
- **Prereq gate:** Level 6 gate above; stitch partners from §2 as tagged

#### SQL-E6.5 · Orders in the previous 30 days
- **Tags:** RANGE frame with interval · self-window
- **Prompt:** For users 1–20: each order and how many **other** orders the same user placed in the 30 days before it (`placed_at − 30 days` up to and including this order's time, excluding itself).
- **Output shape:** `user_id, order_id, prior_30d` (order-insensitive — `lab.chk`)
- **Trap:** A `RANGE BETWEEN INTERVAL '30 days' PRECEDING AND CURRENT ROW` frame includes the current row *and its peers*; subtract 1 and think about equal timestamps. `ROWS 30 PRECEDING` would count rows, not days.
- **Golden fingerprint:** `996:7e7490f1`
- **Prereq gate:** Level 6 gate above; stitch partners from §2 as tagged

#### SQL-E6.6 · Signup-cohort activation
- **Tags:** cohort analysis · date_trunc · conditional counts
- **Prompt:** Cohort = signup month (`date_trunc('month', created_at)`). For each cohort: size, and how many of its users placed at least one order in the **calendar month after** their signup month.
- **Output shape:** `cohort_month, size, active_next_month` (order-insensitive — `lab.chk`)
- **Trap:** Two grains at once (users, then orders). Compute *per-user* activation first (`EXISTS`), then aggregate by cohort — do not join users to orders and `count(*)`.
- **Golden fingerprint:** `10:79a8b3a1`
- **Prereq gate:** Level 6 gate above; stitch partners from §2 as tagged

#### SQL-E6.7 · Dedupe events, keep the first
- **Tags:** row_number · deduplication · planted test data
- **Prompt:** Some pipelines deliver twice. Treat two events as the same delivery when `(user_id, event_type, occurred_at)` are equal (NULL users count as equal to each other). Run your query against this **planted** input `e` (the real table plus 6,000 duplicate deliveries with ids +1,000,000): `SELECT * FROM lab.event UNION ALL SELECT event_id + 1000000, tenant_id, user_id, event_type, occurred_at, payload FROM lab.event WHERE event_id % 10 = 0`. Return the `event_id`s that are **not** the lowest id in their duplicate group.
- **Output shape:** `event_id` (order-insensitive — `lab.chk`)
- **Trap:** `PARTITION BY` treats NULLs as one group (unlike `=`). Run the query on the *un-planted* table too: it must return 0 rows — an empty result is a valid, testable answer, but only if you have also seen it return the planted rows.
- **Golden fingerprint:** `6000:a46392ec`
- **Prereq gate:** Level 6 gate above; stitch partners from §2 as tagged

### 6.7 Level 7 — Recursion

**Prereq gate:** SQL-E6 gate; SL-09

#### SQL-E7.1 · Category paths
- **Tags:** recursive CTE · tree · path
- **Prompt:** For tenant 1's category tree: every category with its depth (root = 0) and the `' > '`-joined path of **names** from the root.
- **Output shape:** `category_id, depth, path` (order-insensitive — `lab.chk`)
- **Trap:** A recursive CTE = anchor (roots: `parent_id IS NULL`) `UNION ALL` recursive step joining on `parent_id`. Termination is guaranteed only if the data has no cycles — the seed does, a hostile import might not (SQL-E7.5).
- **Golden fingerprint:** `10:82a25fd0`
- **Prereq gate:** Level 7 gate above; stitch partners from §2 as tagged

#### SQL-E7.2 · Products in a subtree
- **Tags:** recursive CTE · rollup up the tree
- **Prompt:** For every category of tenant 1: the number of products attached to it **or any descendant**.
- **Output shape:** `category_id, subtree_products` (order-insensitive — `lab.chk`)
- **Trap:** Materialise (ancestor, descendant) pairs, then join products to *descendant* and group by *ancestor*. A category with no products still needs a row — LEFT JOIN.
- **Golden fingerprint:** `10:13320b85`
- **Prereq gate:** Level 7 gate above; stitch partners from §2 as tagged

#### SQL-E7.3 · Referral roots and depth
- **Tags:** recursive CTE · forest · depth
- **Prompt:** Users form a referral forest (`referred_by` → parent). For every user: the root user of their tree and their depth (root = 0).
- **Output shape:** `user_id, root_id, depth` (order-insensitive — `lab.chk`)
- **Trap:** Roots are the rows with `referred_by IS NULL`; carry `root_id` through the recursion instead of recomputing it. Prove termination: `referred_by < user_id` holds in this seed, so no cycle — state that invariant, don't assume it.
- **Golden fingerprint:** `2000:97e6e0a2`
- **Prereq gate:** Level 7 gate above; stitch partners from §2 as tagged

#### SQL-E7.4 · Biggest referral tree
- **Tags:** recursive CTE · aggregate over recursion
- **Prompt:** The root user whose tree (including the root) has the most members; ties → lowest `user_id`.
- **Output shape:** `root_id, tree_size` (ordered — use `lab.chk_o`)
- **Trap:** Aggregate *after* the recursion. `ORDER BY tree_size DESC, root_id LIMIT 1`.
- **Golden fingerprint:** `1:36a7110f`
- **Prereq gate:** Level 7 gate above; stitch partners from §2 as tagged

#### SQL-E7.5 · Find the cycle
- **Tags:** recursive CTE · cycle detection · path array
- **Prompt:** Directed edges are given inline: `(1,2),(2,3),(3,1),(4,5),(5,6)`. Return every node that lies on a cycle.
- **Output shape:** `node` (order-insensitive — `lab.chk`)
- **Trap:** Carry a `path` array and stop when the next node is already in it (`NOT next = ANY(path)`); a node is on a cycle if it can reach itself. PostgreSQL 14+ also has `CYCLE … SET … USING` — write it both ways.
- **Golden fingerprint:** `3:62171a21`
- **Prereq gate:** Level 7 gate above; stitch partners from §2 as tagged

### 6.8 Level 8 — Time, JSON, text, cleaning

**Prereq gate:** SQL-E7 gate; SL-12

#### SQL-E8.1 · Average delivery time by carrier
- **Tags:** interval arithmetic · extract(epoch)
- **Prompt:** For delivered shipments: per carrier, the count and the mean transit time in **days** (shipped → delivered) rounded to 2 decimals.
- **Output shape:** `carrier, n, avg_days` (order-insensitive — `lab.chk`)
- **Trap:** `avg(interval)` is legal but unreadable; convert with `extract(epoch FROM …) / 86400` — as `numeric`, not float, before rounding. NULL `delivered_at` rows are excluded by the filter, not by luck.
- **Golden fingerprint:** `3:72b2a44b`
- **Prereq gate:** Level 8 gate above; stitch partners from §2 as tagged

#### SQL-E8.2 · Stuck shipments as of a fixed instant
- **Tags:** reproducible time · never now()
- **Prompt:** Shipments not delivered more than 14 days after shipping, **as of `2026-01-01 00:00 UTC`** (undelivered and shipped before 2025-12-18).
- **Output shape:** `shipment_id` (order-insensitive — `lab.chk`)
- **Trap:** Never call `now()` in a graded query — the answer changes daily. Parameterise the 'as-of' instant. Same principle as the Northstar ledger's (N5.3) determinism rules.
- **Golden fingerprint:** `1825:dc65c0f1`
- **Prereq gate:** Level 8 gate above; stitch partners from §2 as tagged

#### SQL-E8.3 · UTC day vs New York day
- **Tags:** AT TIME ZONE · DST
- **Prompt:** How many orders have a **different calendar date** in `America/New_York` than in UTC? One number.
- **Output shape:** `n` (order-insensitive — `lab.chk`)
- **Trap:** `ts AT TIME ZONE 'x'` on a `timestamptz` returns a *timestamp without zone* in that zone; on a plain `timestamp` it does the reverse. Get the direction right and test across the 2025-03-09 DST change. Wrong-path fingerprint (do not chase): `1:c06c9654` — comparing UTC to UTC (wrong AT TIME ZONE direction).
- **Golden fingerprint:** `1:f10d5c9a`
- **Prereq gate:** Level 8 gate above; stitch partners from §2 as tagged

#### SQL-E8.4 · Orders per ISO week
- **Tags:** date_trunc('week') · week boundaries
- **Prompt:** Orders placed in 2025 grouped by ISO week (Monday start): week start date and count.
- **Output shape:** `week_start, n` (order-insensitive — `lab.chk`)
- **Trap:** `date_trunc('week')` starts on Monday (ISO); BigQuery's `DATE_TRUNC(d, WEEK)` starts on Sunday. The first/last week straddles the year boundary.
- **Golden fingerprint:** `53:15bc9aa0`
- **Prereq gate:** Level 8 gate above; stitch partners from §2 as tagged

#### SQL-E8.5 · Red eco products
- **Tags:** JSONB · @> · ? operator
- **Prompt:** Products whose `attrs` has `color = 'red'` **and** whose `attrs.tags` array contains `'eco'`.
- **Output shape:** `product_id` (order-insensitive — `lab.chk`)
- **Trap:** `attrs->>'color'` returns text; `attrs @> '{"color":"red"}'` is index-friendly (GIN). `attrs->'tags' ? 'eco'` tests membership in an array of strings. A missing key yields NULL, not false.
- **Golden fingerprint:** `41:a5be7c78`
- **Prereq gate:** Level 8 gate above; stitch partners from §2 as tagged

#### SQL-E8.6 · Search latency by query term
- **Tags:** JSONB extraction · casts
- **Prompt:** For `search` events: per query term (`payload->>'q'`) the number of events and the average `payload->>'ms'` rounded to 1 decimal.
- **Output shape:** `q, n, avg_ms` (order-insensitive — `lab.chk`)
- **Trap:** `->>` returns text — cast before averaging: `(payload->>'ms')::int`. A non-numeric value would fail the whole query — in production, validate on write.
- **Golden fingerprint:** `4:eaf94d2b`
- **Prereq gate:** Level 8 gate above; stitch partners from §2 as tagged

#### SQL-E8.7 · Products per tag
- **Tags:** jsonb_array_elements_text · unnesting
- **Prompt:** Explode `attrs.tags` and count products per tag.
- **Output shape:** `tag, n` (order-insensitive — `lab.chk`)
- **Trap:** A set-returning function in FROM (`CROSS JOIN LATERAL jsonb_array_elements_text(attrs->'tags')`) drops products with no tags — usually what you want; say so. In BigQuery this is `UNNEST`.
- **Golden fingerprint:** `2:71943e30`
- **Prereq gate:** Level 8 gate above; stitch partners from §2 as tagged

#### SQL-E8.8 · Clean and dedupe emails
- **Tags:** trim · lower · regex · dedupe
- **Prompt:** From `lab.stg_import`: normalise `email_text` with `lower(trim(…))`, keep only values that match `^[^@\s]+@[^@\s]+\.[^@\s]+$`, and keep the **lowest `row_id`** for each normalised address.
- **Output shape:** `row_id, email_norm` (order-insensitive — `lab.chk`)
- **Trap:** Empty string and NULL are both invalid; `frank@example` has no dot. Normalise **before** deduping, or 'Ann@Example.com ' and 'ann@example.com' survive as two people.
- **Golden fingerprint:** `8:4fc20676`
- **Prereq gate:** Level 8 gate above; stitch partners from §2 as tagged

#### SQL-E8.9 · Parse money text into minor units
- **Tags:** regexp · CASE · safe casts
- **Prompt:** Convert `amount_text` to integer **minor units** (×100, rounded half up). Accept an optional leading `-`, optional `$`, thousands separators `,` (only in groups of exactly three) and an optional decimal part with `.`; surrounding spaces are ignored. Anything else — `12,50`, `abc`, `1e3`, NULL — becomes NULL.
- **Output shape:** `row_id, amount_minor` (order-insensitive — `lab.chk`)
- **Trap:** Decide the rule for `12,50` (European decimal comma) explicitly — here it is *invalid*, never guessed. Validate with a regex **before** casting; a bare `::numeric` on bad text aborts the whole statement.
- **Golden fingerprint:** `15:bafc9e47`
- **Prereq gate:** Level 8 gate above; stitch partners from §2 as tagged

#### SQL-E8.10 · Write a total date parser
- **Tags:** user-defined function · exception handling · dialect
- **Prompt:** Create `work.try_date(text) RETURNS date` that returns a date for: ISO `YYYY-MM-DD` (after trimming, and also when followed by a `T…` time), `MM/DD/YYYY`, and `D Mon YYYY` (e.g. `1 Mar 2025`); **NULL** for anything else, including impossible dates like `2025-13-40` and `2025-02-29`. Then `SELECT row_id, work.try_date(signup_text)` over `stg_import`.
- **Output shape:** `row_id, d` (order-insensitive — `lab.chk`)
- **Trap:** A cast error aborts the statement; catch it in a `BEGIN … EXCEPTION WHEN others THEN RETURN NULL` block (PL/pgSQL). Postgres 16 adds `pg_input_is_valid()`; BigQuery has `SAFE.PARSE_DATE`, SQL Server `TRY_CONVERT`. `2025-02-29` must fail — 2025 is not a leap year.
- **Golden fingerprint:** `15:3eed39e7`
- **Prereq gate:** Level 8 gate above; stitch partners from §2 as tagged

### 6.9 Level 9 — DML

**Prereq gate:** SQL-E8 gate; SL-10

#### SQL-E9.1 · Materialise a daily GMV table
- **Tags:** CREATE TABLE · INSERT … SELECT · PK
- **Prompt:** In schema `work`, create `tenant_daily_gmv(tenant_id int, day date, gmv_minor bigint NOT NULL, PRIMARY KEY (tenant_id, day))` and fill it with fulfilled-order GMV per tenant per UTC day for **January 2025**.
- **Output shape:** table contents `tenant_id, day, gmv_minor` (order-insensitive — `lab.chk`)
- **Trap:** Column list on `INSERT` (never rely on positional order across a migration). Create the constraint *with* the table so a re-run fails loudly instead of duplicating. All DML in this level is graded inside a transaction that is rolled back — you can retry freely.
- **Golden fingerprint:** `155:9a2d7927`
- **Prereq gate:** Level 9 gate above; stitch partners from §2 as tagged

#### SQL-E9.2 · Repair corrupted totals
- **Tags:** UPDATE … FROM · IS DISTINCT FROM
- **Prompt:** Setup gives you `work.o`, a copy of `customer_order` in which every 100th order (`order_id % 100 = 0`, 200 rows) has `total_minor = 0`. Repair **only the wrong rows** so that `total_minor` equals the sum of `qty × unit_price_minor` of its lines. The statement must report `UPDATE 200`.
- **Output shape:** `work.o` equals `lab.customer_order` on `(order_id, total_minor)` (order-insensitive — `lab.chk`)
- **Trap:** Updating *every* row (no `WHERE … IS DISTINCT FROM`) rewrites 20,000 tuples — table bloat and WAL for no reason. `IS DISTINCT FROM`, not `<>`, so a NULL total would be repaired too.
- **Golden fingerprint:** `20000:12518931`
- **Prereq gate:** Level 9 gate above; stitch partners from §2 as tagged

#### SQL-E9.3 · Idempotent daily load (upsert)
- **Tags:** INSERT … ON CONFLICT DO UPDATE · idempotency
- **Prompt:** Create `work.daily_orders(day date PRIMARY KEY, n int NOT NULL)`. Write one statement that loads the count of orders per UTC day for all of 2025 and can be **run twice with the same result**.
- **Output shape:** `day, n` (order-insensitive — `lab.chk`)
- **Trap:** `SET n = daily_orders.n + EXCLUDED.n` is *not* idempotent (a re-run doubles). `SET n = EXCLUDED.n` is. If your source query returned two rows for one day in a single statement you would get `ON CONFLICT DO UPDATE command cannot affect row a second time` — aggregate first. Idempotent writes are the whole point of A7/A9.
- **Golden fingerprint:** `365:60b9c8d0`
- **Prereq gate:** Level 9 gate above; stitch partners from §2 as tagged

#### SQL-E9.4 · Delete the double-submitted reviews
- **Tags:** DELETE … USING · self-join delete · RETURNING
- **Prompt:** Setup gives `work.r`, a copy of `review`. Delete duplicate `(product_id, user_id)` reviews, **keeping the newest** (highest `review_id`). Report how many were deleted (`DELETE 400`).
- **Output shape:** `work.r` keeps 6,000 rows (order-insensitive — `lab.chk`)
- **Trap:** Test the *keep* rule on a tiny sample first. `DELETE` on a self-join needs `USING`; without a total order you can delete both copies. Run it inside `BEGIN … ROLLBACK` in real life until the count matches your prediction.
- **Golden fingerprint:** `6000:bc58a9d4`
- **Prereq gate:** Level 9 gate above; stitch partners from §2 as tagged

#### SQL-E9.5 · Sync stock with MERGE
- **Tags:** MERGE (PG15+) · three-way sync
- **Prompt:** Setup gives `work.stock_t` (products 1–10 with `on_hand`) and `work.stock_feed` (a partner feed). With **one `MERGE`**: rows in both → update `on_hand`, **except** feed `on_hand = 0` → delete the target row; feed rows not in target → insert.
- **Output shape:** `work.stock_t` afterwards (small — check by eye) (ordered — use `lab.chk_o`)
- **Trap:** `MERGE` arrived in PostgreSQL 15; `WHEN NOT MATCHED BY SOURCE` only in 17 — so 'delete rows missing from the feed' cannot be done in one 15/16 MERGE. Many-to-one source rows raise a cardinality error. SQL Server, Oracle, BigQuery all have `MERGE` with dialect differences (Rosetta table).
- **Golden fingerprint:** `11:61ddd589`
- **Prereq gate:** Level 9 gate above; stitch partners from §2 as tagged

#### SQL-E9.6 · Chunked backfill
- **Tags:** batching · SKIP LOCKED · WAL/bloat awareness
- **Prompt:** Setup gives `work.o` (copy of `customer_order`) with a new nullable column `total_major numeric(12,2)`. Backfill `total_minor / 100.0` in chunks of **1,000 rows**, looping until no rows are left. (Here one transaction; in production every chunk commits separately — N2.6 expand/contract.)
- **Output shape:** all 20,000 rows have `total_major` set (order-insensitive — `lab.chk`)
- **Trap:** `WHERE total_major IS NULL … LIMIT` inside a CTE + `UPDATE … RETURNING` is the loop body. One giant `UPDATE` holds locks and WAL for minutes on a real table and blocks vacuum. Chunk size is a *tuning knob*, not a constant.
- **Golden fingerprint:** `20000:f913007e`
- **Prereq gate:** Level 9 gate above; stitch partners from §2 as tagged

#### SQL-E9.7 · Archive refunded orders atomically
- **Tags:** writable CTE · DELETE … RETURNING
- **Prompt:** Setup gives `work.o` (copy of `customer_order`) and an empty `work.o_archive (LIKE work.o)`. In **one statement**, move every refunded order from `work.o` into `work.o_archive`.
- **Output shape:** `live, archived` counts (18000, 2000) (order-insensitive — `lab.chk`)
- **Trap:** `DELETE … RETURNING *` inside a CTE feeding an `INSERT` is atomic — no window where the row is in both or neither. Doing it as two statements needs a transaction; doing it in the application needs an outbox.
- **Golden fingerprint:** `1:06897331`
- **Prereq gate:** Level 9 gate above; stitch partners from §2 as tagged

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
- **Prereq gate:** Level 10 gate above; stitch partners from §2 as tagged

#### SQL-E10.2 · Tenant-safe foreign key
- **Tags:** composite FK · multi-tenancy · integrity at the schema level
- **Prompt:** Create `work.note(note_id bigint PK, tenant_id int NOT NULL, user_id bigint NOT NULL, body text)` so that a note can only reference a user **of the same tenant**. Battery (Appendix B.2) must give `T F F F`: (1) tenant 1 / user 1 ok · (2) tenant 2 / user 1 fails (user 1 is tenant 1's) · (3) tenant 1 / user 999999 fails · (4) NULL tenant fails.
- **Output shape:** vector of booleans (ordered — use `lab.chk_o`)
- **Trap:** `user_id REFERENCES app_user` alone only proves the user *exists*. The composite `FOREIGN KEY (tenant_id, user_id) REFERENCES app_user (tenant_id, user_id)` needs a matching unique constraint on the parent — that is why the lab's `app_user` carries `UNIQUE (tenant_id, user_id)`. This is defence in depth beneath RLS (N8.1).
- **Golden fingerprint:** `4:8c4ee581`
- **Prereq gate:** Level 10 gate above; stitch partners from §2 as tagged

#### SQL-E10.3 · One active subscription per user
- **Tags:** partial unique index · state machine invariants
- **Prompt:** `work.subscription(sub_id bigint PK, user_id bigint NOT NULL, status text CHECK (status IN ('active','cancelled')))`. Enforce **at most one `active` row per user**, any number of cancelled. Battery (Appendix B.3) expects `T T T F T`: (1) user 1 active · (2) user 1 cancelled · (3) user 1 cancelled again · (4) user 1 second active — fails · (5) user 2 active.
- **Output shape:** vector of booleans (ordered — use `lab.chk_o`)
- **Trap:** A plain `UNIQUE (user_id, status)` would forbid a second *cancelled* row. The invariant is conditional — a **partial unique index** `… (user_id) WHERE status = 'active'`. Race-free by construction, unlike an application-side check.
- **Golden fingerprint:** `5:7a0a9605`
- **Prereq gate:** Level 10 gate above; stitch partners from §2 as tagged

#### SQL-E10.4 · No overlapping price validity
- **Tags:** EXCLUDE constraint · range types · btree_gist
- **Prompt:** `work.price_period(product_id bigint, during daterange, price_minor int)`. Forbid two rows of the **same product** whose periods overlap. Battery (Appendix B.4) expects `T T F T F`: (1) p1 `[2025-01-01,2025-02-01)` · (2) p1 `[2025-02-01,2025-03-01)` (touching is fine) · (3) p1 `[2025-01-15,2025-01-20)` overlaps → fails · (4) p2 same dates as (1) fine · (5) p1 `[2025-02-28,2025-04-01)` overlaps (2) → fails.
- **Output shape:** vector of booleans (ordered — use `lab.chk_o`)
- **Trap:** Uniqueness of `(product_id, valid_from)` does **not** stop overlaps. `EXCLUDE USING gist (product_id WITH =, during WITH &&)` needs `btree_gist` for the `=` part. Half-open ranges `[a,b)` make 'touching' legal. Spanner and BigQuery have no exclusion constraints — you'd enforce in a transaction (Rosetta table).
- **Golden fingerprint:** `5:a6c6c4a9`
- **Prereq gate:** Level 10 gate above; stitch partners from §2 as tagged

#### SQL-E10.5 · Circular references with DEFERRABLE
- **Tags:** DEFERRABLE INITIALLY DEFERRED · constraint timing
- **Prompt:** Two tables reference each other: `work.a(id PK, b_id → b)` and `work.b(id PK, a_id → a)`. Make it possible to insert `a(1, b_id=1)` and `b(1, a_id=1)` **in one transaction** but impossible to commit a dangling reference. Battery (Appendix B.5) is a `DO` block — expected: block succeeds; then a lone `INSERT INTO a VALUES (2, 99)` inside its own transaction **fails at COMMIT** (not at the INSERT).
- **Output shape:** commit-time failure demonstrated (order-insensitive — `lab.chk`)
- **Trap:** Without `DEFERRABLE INITIALLY DEFERRED` the first insert fails immediately. Deferred checks run at `COMMIT` — so the error surfaces *after* your `INSERT` returned success; app code must handle a failed commit. `SET CONSTRAINTS … DEFERRED` scopes it per transaction.
- **Golden fingerprint:** `1:fb0ce7c2`
- **Prereq gate:** Level 10 gate above; stitch partners from §2 as tagged

#### SQL-E10.6 · Row-level security by tenant
- **Tags:** RLS · policies · current_setting · roles
- **Prompt:** Enable RLS on `work.o` (a copy of `customer_order`) so that a role `app_rls` sees **only rows where `tenant_id = current_setting('app.tenant_id')::int`**. Then, as `app_rls` with `app.tenant_id = '2'`, count rows per tenant. Predict first: how many rows, which tenants? What happens if the setting is unset?
- **Output shape:** `tenant_id, n` (a single row for tenant 2) (order-insensitive — `lab.chk`)
- **Trap:** RLS does **not** apply to the table owner or superusers unless `FORCE ROW LEVEL SECURITY`. `current_setting('x', true)` returns NULL when unset (no rows), without `true` it raises. Connection-pool reuse means the setting must be `SET LOCAL` per transaction — N8.1 RLS.
- **Golden fingerprint:** `1:86599c11`
- **Prereq gate:** Level 10 gate above; stitch partners from §2 as tagged

### 6.13 Level 13 — Analytics SQL

**Prereq gate:** SQL-E10 gate; AN-01…AN-03, SL-05/08

#### SQL-E13.1 · Subtotals with ROLLUP
- **Tags:** GROUP BY ROLLUP · GROUPING() · subtotals
- **Prompt:** Fulfilled 2025 orders: GMV by `(tenant_id, currency)` with **per-tenant subtotals** and a **grand total** row. Add a column `level` = `'detail'`, `'tenant'` or `'grand'` computed with `GROUPING()`.
- **Output shape:** `tenant_id, currency, gmv_minor, level` (order-insensitive — `lab.chk`)
- **Trap:** A subtotal row has NULL in the rolled-up column — indistinguishable from a real NULL. `GROUPING(col)` is 1 for rolled-up NULLs. Adding two currencies into one grand total is only meaningful if you say so (tenant 4 is EUR) — a business-rule trap.
- **Golden fingerprint:** `11:bbcd158f`
- **Prereq gate:** Level 13 gate above; stitch partners from §2 as tagged

#### SQL-E13.2 · Pivot statuses into columns
- **Tags:** conditional aggregation · pivot
- **Prompt:** One row per tenant with five count columns `created, paid, fulfilled, refunded, cancelled` (orders placed in 2025).
- **Output shape:** `tenant_id, created, paid, fulfilled, refunded, cancelled` (order-insensitive — `lab.chk`)
- **Trap:** Standard SQL has no `PIVOT` (SQL Server/Oracle/BigQuery do). The portable idiom is `count(*) FILTER (WHERE …)` or `sum(CASE …)`. The column list is fixed at write time — dynamic pivots need dynamic SQL.
- **Golden fingerprint:** `5:f64390e3`
- **Prereq gate:** Level 13 gate above; stitch partners from §2 as tagged

#### SQL-E13.3 · Build a star schema
- **Tags:** dimensional modelling · fact/dim · surrogate keys
- **Prompt:** In `work`, build `dim_product(product_id, name, category_name)` (category name or `'(none)'`), `dim_date(date_key, year, month)` for 2025 and `fact_sales(order_id, line_no, date_key, product_id, qty, revenue_minor)` from **fulfilled** order lines. Then answer with the star: *revenue by category name and month for 2025*.
- **Output shape:** `category_name, month, revenue_minor` (order-insensitive — `lab.chk`)
- **Trap:** Facts hold measures + foreign keys at one **grain** (an order line); dimensions hold descriptions. Decide grain first, write it in one sentence. In BigQuery you would partition the fact by date and cluster by product (V-DATA, N9b.1) and often *denormalise* the dimensions in.
- **Golden fingerprint:** `372:22383318`
- **Prereq gate:** Level 13 gate above; stitch partners from §2 as tagged

#### SQL-E13.4 · Price history as a Type-2 dimension
- **Tags:** SCD2 · lead() · valid_to
- **Prompt:** From `product_price_history` build a Type-2 slowly-changing dimension: `product_id, price_minor, valid_from, valid_to, is_current` where `valid_to` is the next row's `valid_from` (NULL for the current row). Products 1–10 only.
- **Output shape:** `product_id, price_minor, valid_from, valid_to, is_current` (order-insensitive — `lab.chk`)
- **Trap:** `valid_to` = `lead(valid_from)` — half-open `[from, to)`. Keep `is_current` derived (`valid_to IS NULL`), never hand-set. Overlap is prevented by SQL-E10.4's exclusion constraint.
- **Golden fingerprint:** `30:12ca6f21`
- **Prereq gate:** Level 13 gate above; stitch partners from §2 as tagged

#### SQL-E13.5 · Revenue at the price in effect
- **Tags:** as-of join · SCD2 join · range join
- **Prompt:** Using the SCD2 shape of SQL-E13.4, re-derive each fulfilled order line of **January 2025** at the *list price in effect at `placed_at`* and return the total difference `sum(qty × (list_price_at_order − unit_price_minor))` per tenant. (Expect a large positive number: the seed charged the *current* price, not the historical one.)
- **Output shape:** `tenant_id, price_gap_minor` (order-insensitive — `lab.chk`)
- **Trap:** Join on the *range* `valid_from <= placed_at AND (valid_to IS NULL OR placed_at < valid_to)` — the half-open form makes every order match exactly one row. Check that: `count(*)` of the join must equal `count(*)` of the lines.
- **Golden fingerprint:** `5:7656600a`
- **Prereq gate:** Level 13 gate above; stitch partners from §2 as tagged

### 6.14 Level 14 — Capstone audits & performance

**Prereq gate:** SQL-E13 gate; SQL-CAP1 after SQL-E3+SQL-E4; SQL-CAP2 after SQL-E4.5; SQL-CAP4 after PX cards

#### SQL-CAP1.1 · Order total ≠ sum of its lines
- **Tags:** audit invariant · anti-join / aggregate · data quality
- **Prompt:** On the fault-injected copies in schema `audit` (Appendix B.6): find every violation of the invariant *order total ≠ sum of its lines*. Also run it against the clean `lab.*` tables — it must return **0 rows** there.
- **Output shape:** `order_id` (order-insensitive — `lab.chk`)
- **Trap:** Orders **with no lines** would slip through an inner join — is that a separate invariant? (yes: add it if you consider 'empty order' illegal).
- **Golden fingerprint:** `3:7cc530bb`
- **Prereq gate:** Level 14 gate above; stitch partners from §2 as tagged

#### SQL-CAP1.2 · Order lines with no order (orphans)
- **Tags:** audit invariant · anti-join / aggregate · data quality
- **Prompt:** On the fault-injected copies in schema `audit` (Appendix B.6): find every violation of the invariant *order lines with no order (orphans)*. Also run it against the clean `lab.*` tables — it must return **0 rows** there.
- **Output shape:** `order_id, line_no` (order-insensitive — `lab.chk`)
- **Trap:** The real schema has an FK, so this can't happen there — this audit is for *imported* or FK-less (warehouse) data.
- **Golden fingerprint:** `1:ec2bf809`
- **Prereq gate:** Level 14 gate above; stitch partners from §2 as tagged

#### SQL-CAP1.3 · Paid/fulfilled/refunded order with no succeeded charge
- **Tags:** audit invariant · anti-join / aggregate · data quality
- **Prompt:** On the fault-injected copies in schema `audit` (Appendix B.6): find every violation of the invariant *paid/fulfilled/refunded order with no succeeded charge*. Also run it against the clean `lab.*` tables — it must return **0 rows** there.
- **Output shape:** `order_id` (order-insensitive — `lab.chk`)
- **Trap:** A *failed* charge followed by a succeeded one is legal (every 15th order). Test the anti-join on `status = 'succeeded'`, not on 'has any charge'.
- **Golden fingerprint:** `2:addb7d1b`
- **Prereq gate:** Level 14 gate above; stitch partners from §2 as tagged

#### SQL-CAP1.4 · Refunds exceed charges
- **Tags:** audit invariant · anti-join / aggregate · data quality
- **Prompt:** On the fault-injected copies in schema `audit` (Appendix B.6): find every violation of the invariant *refunds exceed charges*. Also run it against the clean `lab.*` tables — it must return **0 rows** there.
- **Output shape:** `order_id` (order-insensitive — `lab.chk`)
- **Trap:** Aggregate the payments table **alone** (one grain), never join it to lines first.
- **Golden fingerprint:** `2:23dae8cd`
- **Prereq gate:** Level 14 gate above; stitch partners from §2 as tagged

#### SQL-CAP1.5 · Reserved stock above on-hand
- **Tags:** audit invariant · anti-join / aggregate · data quality
- **Prompt:** On the fault-injected copies in schema `audit` (Appendix B.6): find every violation of the invariant *reserved stock above on-hand*. Also run it against the clean `lab.*` tables — it must return **0 rows** there.
- **Output shape:** `product_id` (order-insensitive — `lab.chk`)
- **Trap:** The real table forbids this with a CHECK; `CREATE TABLE AS` copies data, not constraints — a classic way audit copies lose their guard rails.
- **Golden fingerprint:** `2:cc6c5a8d`
- **Prereq gate:** Level 14 gate above; stitch partners from §2 as tagged

#### SQL-CAP1.6 · Duplicate idempotency keys within a tenant
- **Tags:** audit invariant · anti-join / aggregate · data quality
- **Prompt:** On the fault-injected copies in schema `audit` (Appendix B.6): find every violation of the invariant *duplicate idempotency keys within a tenant*. Also run it against the clean `lab.*` tables — it must return **0 rows** there.
- **Output shape:** `tenant_id, idempotency_key, n` (order-insensitive — `lab.chk`)
- **Trap:** NULL keys are legitimately repeated (a UNIQUE index allows many NULLs). Exclude them explicitly.
- **Golden fingerprint:** `1:3402ab9a`
- **Prereq gate:** Level 14 gate above; stitch partners from §2 as tagged

#### SQL-CAP1.7 · Delivered before shipped
- **Tags:** audit invariant · anti-join / aggregate · data quality
- **Prompt:** On the fault-injected copies in schema `audit` (Appendix B.6): find every violation of the invariant *delivered before shipped*. Also run it against the clean `lab.*` tables — it must return **0 rows** there.
- **Output shape:** `shipment_id` (order-insensitive — `lab.chk`)
- **Trap:** NULL `delivered_at` compares UNKNOWN → correctly excluded.
- **Golden fingerprint:** `2:b713c027`
- **Prereq gate:** Level 14 gate above; stitch partners from §2 as tagged

#### SQL-CAP1.8 · Fulfilled order with no shipment
- **Tags:** audit invariant · anti-join / aggregate · data quality
- **Prompt:** On the fault-injected copies in schema `audit` (Appendix B.6): find every violation of the invariant *fulfilled order with no shipment*. Also run it against the clean `lab.*` tables — it must return **0 rows** there.
- **Output shape:** `order_id` (order-insensitive — `lab.chk`)
- **Trap:** Anti-join again. Contrast with SQL-E3.5 (semi-join).
- **Golden fingerprint:** `2:7bd384d1`
- **Prereq gate:** Level 14 gate above; stitch partners from §2 as tagged

#### SQL-CAP2 · Cash-basis monthly revenue report
- **Tags:** capstone · payments · accrual vs cash
- **Prompt:** Per tenant and **payment** month (UTC, by `payment.created_at`): sum of **succeeded charges**, sum of **succeeded refunds**, and net = charges − refunds. Failed and pending payments never count. Then write two sentences reconciling this *cash* report with the *accrual* report of SQL-E4.5 (orders by placement date).
- **Output shape:** `tenant_id, month, charged_minor, refunded_minor, net_minor` (order-insensitive — `lab.chk`)
- **Trap:** A refund posted five days after an order can land in the next month — cash vs accrual differences are **timing**, not error. Aggregate `payment` on its own (no join to lines/orders except to get `tenant_id`). Money never leaves integer minor units.
- **Golden fingerprint:** `65:b63b5f6f`
- **Prereq gate:** Level 14 gate above; stitch partners from §2 as tagged

#### SQL-CAP4 · Explain and fix the slow query
- **Tags:** capstone · performance · correlated subquery → join
- **Prompt:** For every identified user who ever made a `purchase` event: the number of `page_view` events in the 24 hours **before their first purchase**. The baseline query (Appendix B.7) uses three correlated subqueries per user and takes ~1.5 s on this seed. Deliverable: (1) `EXPLAIN (ANALYZE)` of the baseline with your written diagnosis, (2) a rewrite that returns the **identical fingerprint** in under 50 ms without adding an index, (3) a second fix that keeps the baseline text and adds an index — name it.
- **Output shape:** `user_id, views_24h` (order-insensitive — `lab.chk`)
- **Trap:** Fingerprint first, speed second: a fast wrong answer is worthless. The rewrite computes each user's first-purchase time **once** (CTE, `min … GROUP BY user_id`) and joins; the index alternative is `(user_id, event_type, occurred_at)` or `(user_id, occurred_at)`.
- **Golden fingerprint:** `250:eb4c8d2a`
- **Prereq gate:** Level 14 gate above; stitch partners from §2 as tagged

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
- **Tags:** PX-9 · OD-09 · N8.1.5
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
- **Tags:** N5.3·DD-05
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
- **Tags:** AN-06·N2.4
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
- **Tags:** DD-02·N8.0
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
- **Tags:** DD-11·N2.6
- **Prompt:** Add `email_verified_at` without downtime; list steps + locks.
- **Output shape:** step list
- **Trap:** jumping to physical indexes before logical keys
- **Golden fingerprint:** _(design review)_
- **Prereq gate:** DD-* as tagged

#### SCH-5 · Shard key for multi-tenant
- **Tags:** DD-13·N2.7
- **Prompt:** Propose partition/shard key for orders; address user-1 hotspot.
- **Output shape:** design note
- **Trap:** jumping to physical indexes before logical keys
- **Golden fingerprint:** _(design review)_
- **Prereq gate:** DD-* as tagged

#### SCH-6 · Audit log + masking view
- **Tags:** DD-07·N7.3
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

Mirror `Curriculum` C5 posture: **`terraform plan` reads the graph; apply only if Lab Reality + credits allow, destroy same day.**

| ID | Goal | Notes |
|---|---|---|
| **TF-DB1** | Cloud SQL Postgres instance + private IP + flags sketch | Ties OD-03/04; Auth Proxy as separate module |
| **TF-DB2** | Cloud SQL read replica + failover knobs (plan) | OD-05 lag SLI discussion |
| **TF-DB3** | AlloyDB cluster + instance (plan) | Compare cost line to Cloud SQL |
| **TF-DB4** | Spanner instance + database + DDL job (plan) | Interleave as comment; no production data |
| **TF-DB5** | BigQuery dataset + partitioned table + clustering | AN-02 bytes napkin |
| **TF-DB6** | IAM bindings for DB roles / BQ dataset access | SL-13 least privilege |

## 9. Capstones (SQL-CAP1–SQL-CAP4)

Database acceptance tests for N11 (Northstar). Issue after the §6 level-14 gate. **Predict; run; reconcile.**

| ID | Title | Soft gate | Fingerprint source |
|---|---|---|---|
| **SQL-CAP1.1–SQL-CAP1.8** | Fault-injected audit invariants | SQL-E3 + SQL-E4 anti/semi-join fluency | `goldens_ex_l14.json` |
| **SQL-CAP2** | Cash-basis monthly revenue | SQL-E4.5 accrual report done | same |
| **SQL-CAP3** | Checkout schema + concurrency | SCH-1 + TX-2/TX-8 | design + TX evidence (no single chk) |
| **SQL-CAP4** | Slow-query rescue | PX cards; `slow_*.sql` | `SQL-CAP4` golden in l14 JSON |

**SQL-CAP3 spec (consistent with lab):** design checkout that cannot oversell `stock` under concurrency (`safe.sql` pattern), uses idempotency keys (`UNIQUE (tenant_id, idempotency_key)`), and records payments as ledger-friendly minor units. Deliver: DDL delta, TX evidence transcript, ADR for isolation level.

Cards for SQL-CAP1.*, SQL-CAP2, SQL-CAP4 are in §6.14; keys in Appendix K.

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
## Appendix V — Verification notes (honesty flags)

- **Goldens:** 92/92 exercise cards carry fingerprints from local JSON artefacts (`goldens_ex_l1_4.json`, `goldens_ex_l5_8.json`, `goldens_ex_l9_13.json`, `goldens_ex_l14.json`). They were produced by `run_ex.py` against seed v1; this build **wires those values verbatim** and does not re-execute Postgres in the markdown generator.
- **Wrong-path set:** 11 entries from `goldens_wrong.json` referenced in traps where IDs overlap.
- **`(verify)` markers:** Cloud SQL/AlloyDB/Spanner/BigQuery UI labels, exam-guide domain lists, and version-specific syntax (MERGE on older PG, Spanner JSON functions, SQL Server `IS DISTINCT FROM` availability) — check live docs before exams or production.
- **SQL-E3.7 note:** `out_ex_l1_4.txt` contains a duplicate run line with a divergent hash; **JSON golden `100:1b05fa94` is authoritative**.
- **SQL-CAP3:** design/TX evidence capstone — no single `lab.chk` fingerprint (stub: acceptance via transcript + ADR).
- **TF-DB*:** plan-only stubs; no checked-in `.tf` in this companion (owned by learner under Lab Reality).
- **Primer SD-13…SD-19:** intentionally not re-taught; cross-links only.
- **gcp toys DB-1…DB-10:** not duplicated; analytic layer only.
- **Modern notes:** SSI write-skew behaviour, `MERGE` in PG15+, `EXCLUDE` with `btree_gist`, recursive cycle clause PG14+ — confirm on your minor version.
- **Built:** 2026-09-21 from on-box sources only.



---

## Pre-refactor text archive (D3)

*Refactor-authored section (2026-09-24).* Decision D3 says content may be re-arranged but never removed. Each block below is the exact pre-refactor text (after the §5 ID renames) of a line that R2 corrected or regenerated. It is kept for provenance only and is **not authoritative**; the live text above wins. Tooling excludes this section from ID and anchor checks.

**D3-01** · C-01 · title block, parent line

```text
Companion to `gcp-curriculum.md` ("The Consolidated Cloud Mastery Curriculum", initial course T–11b + Part 12 continuation) and to the owner nodes `DB-SQL` and `DB-ENGINE` of `unified-curriculum.md`.
```

**D3-02** · C-05 · §0.1 "Why" line

```text
Why: gcp-curriculum owns the *product spine* (Northstar on GCP) and, in Part 2, the engine slices DB-1 … DB-10 and the Cloud SQL procedure. It deliberately does not own the SQL *language* end to end, the pre-SQL mathematics a learner may lack, the theory tier behind the slices (serializability, ARIES, join-cost formulas, Selinger-style planning), modelling method, analytics dialects, or a large body of query-writing practice. This file supplies exactly those, and hangs each piece on the gcp-curriculum module that needs it, **at the moment that module needs it**.
```

**D3-03** · C-05 · §0.2 rule 2

```text
2. **Ownership split (memorise).** *gcp-curriculum owns:* Cloud SQL setup (2.3), the ten engine slices DB-1 … DB-10 and their toys, Firestore (2.4), migrations-as-jobs (2.6), the Spanner/NoSQL map (2.7), the primitives of 8.1 (cursor pager, hot partition, pool math, RLS, LSM-vs-B-tree comparison), outbox/inbox (3.5), the ledger (5.3), BigQuery ops (9.4/9b.1), as-of joins as *leakage prevention* (9c.1), billing-export SQL (10.3). *This file owns:* SQL-language mastery (SL), relational theory (RT), the CS theory tier under the slices (CS), data-design method (DD), operating-a-database craft (OD), analytics and dialect craft (AN), pre-SQL prerequisites (PQ), and the exercise ladder (§6). **Where a gcp-curriculum toy exists (WAL codec, slotted page, B-tree, iterator executor, visibility simulator) this file never asks for a second toy — it adds the analytic layer (formulas, schedules, cost models) that the toy's tests do not reach.**
```

**D3-04** · C-37 · replaced line

```text
- `SQL-E<level>.<n>` query-writing exercises (§6, levels 1–14; **TX** and **PX** are *labs* in §7) · `SQL-Z0.n` level-0 paper drills · `TD-n` theory drills · `PX-n` plan-prediction cards · `TX-n` transaction labs · `BH-n` bug-hunts · `DT-n` dialect-translation drills · `SD-n` schema-design cases · `SQL-CAP1–SQL-CAP4` capstones · `TF-DBn` Terraform database exercises.
```

**D3-05** · C-53 · §0.4 notation, ID legend

```text
- `T.*`, `F1…F4`, `M.*`, `0.x`, `1.x`, `D0…D8`, `2.x` … `11b`, `12.Sxx`, `DB-1 … DB-10`, `G4`, `G12b` are **gcp-curriculum** IDs. `SD-13 … SD-27` are **primer-companion** IDs. `TB-…`/`SRC-…` are unified-curriculum source IDs.
```

**D3-06** · C-02 · §2.3 intro

```text
gcp-curriculum's spine is `T → F → M → 0 → 1 → D → 2 → 3 → …`. SQL does not first *appear* until Part 2, so the calendar front-loads only **cheap, unlockable prerequisites** and holds the language until Part 2 needs it (Prop Lock: no SQL vocabulary before it is anchored).
```
