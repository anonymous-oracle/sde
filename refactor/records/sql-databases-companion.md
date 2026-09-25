# Records for sql-databases-companion.md (R2b, R2c and R4 build edits, 2026-09-24)

Refactor bookkeeping only, not course material. Decision D6 keeps provenance, the D3 archive and every line the build changed or removed (R2b; the R2c Go tie-ins; R4, rules R4-*) out of the course files; decision D3 keeps them here, verbatim. Each entry names the build journal number (outputs/r2b/journal.jsonl), the rule and the class.

**J81** · G0 · R2 in-file D3 archive, moved out whole

````text



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

````

**J82** · G1 · line moved out of the course file

````text
*Provenance (C-01, 2026-09-24):* originally authored against `gcp-curriculum.md` and the `unified-curriculum.md` nodes `DB-SQL` / `DB-ENGINE`; rebound to `Curriculum` + `northstar-reference-app.md` on 2026-09-24. Every foreign label and its new anchor is listed in `crosswalk.md` §1.
````

**J83** · G2 · move

````text
| **M1** (logic, sets, proofs, counting, graphs) — *Tier SQL-T-HS/SQL-T-UG* *(was `T.Disc`)* | PQ-01 sets, relations, functions, **bags** · PQ-02 predicate logic and **3-valued logic (preview)** · counting/cardinality bounds of joins (RT-01) | SQL-Z0.1 … SQL-Z0.6 |
````

**J84** · G2 · move

````text
| **A4** (recall) + **U2** (structures, hashing theory, complexity) *(was `T.Algo`)* | PQ-07 sorting, hashing, trees, binary search *as the raw material of access paths* · CS-02 B-tree fan-out and height arithmetic (formula only — the toy is DB-6) | SQL-Z0.7, TD-10 |
````

**J85** · G2 · move

````text
| **A1/A2** (recall) + **M6** (units, orders of magnitude) *(was `T.Quant`)* | PQ-08 storage hierarchy, page/row arithmetic · latency numbers (recall of primer SD-37) | SQL-Z0.8 |
````

**J86** · G2 · move

````text
| **M5** (numerical stability) *(was `M.NS`)* | PQ-03 `numeric` vs float, rounding modes (half-up vs banker's), integer money — *recall IEEE from M5; add decimal semantics* | SQL-E2.1, SQL-E2.7 |
````

**J87** · G2 · move

````text
| **A8 + A9** (+ U5) — DB theory (with the A8 SQL sessions) *(was `T.SysTheory`, Part 2)* | RT-02 algebra · RT-03 calculus/safety (SQL-T-GR) · RT-04/05 FDs & normal forms · RT-08 rewrites · CS-05 serializability & SI · CS-06 recovery · CS-08 cardinality. **SQL-T-UG gate items** map to TD-2 (push σ through ⋈), TD-1/2/3 (keys, FDs, 3NF), TD-8 (dirty-read & lost-update schedules), TD-12 (WAL durability). **SQL-T-GR gate items** map to TD-9 (snapshot visibility), TD-13 (selectivity estimate) | TD-1 … TD-16 (as gated) |
````

**J88** · G2 · move

````text
| **A3 + A6** (computer, OS, CLI, Git, JSON, HTTP) *(was `F1`)* | PQ-04 files, CSV/JSON/JSONL, encodings (UTF-8, BOM) · PQ-05 `psql`, env vars, Docker basics for a Postgres container | SQL-E0 warm-up: load the lab (§3) |
````

**J89** · G2 · move

````text
| **C1** Docker/OCI, container contract *(was `D1`, `1.2`)* | PQ-05 `docker compose` Postgres with a named volume and a healthcheck (the lab in §3.2) | lab loads, fingerprints match |
````

**J90** · G2 · move

````text
| **C4** CI *(was `D2`)* | OD-10 SQL tests in CI: a Postgres service container, seed v1, fingerprint assertions, migration up/down | run SQL-E3.2 as a CI test |
````

**J91** · G2 · move

````text
| **C4 + C5** CD, IaC *(was `D3/D7`)* | OD-08 migration ordering in deploys · §8.2 Terraform DB exercises | TF-DB1 … TF-DB2 (plan only) |
````

**J92** · G2 · move

````text
| **S2** + **N0.4** HLD/LLD contract, ADR template, NFR table *(was `0.4`)* | DD-01 conceptual → logical → physical; **schema ADRs** ("I pick X because Y, I accept Z") · DD-12 constraints as spec | SCH-1 |
````

**J93** · G2 · move

````text
| **B5** IAM (+ **N2.3** IAM DB auth) *(was `0.5`, `2.3`)* | SL-13 database roles vs IAM principals, `GRANT`/`REVOKE`, least privilege | SQL-E10.6 (RLS) after A10 |
````

**J94** · G2 · move

````text
| **C6** observability day one *(was `1.7`)* | OD-02 logs, slow-query log, `pg_stat_statements`, Query Insights vocabulary | PX-1 |
````

**J95** · G2 · move

````text
| **B3** HA & autoscaling *(was `1.12`)* | OD-03 pool arithmetic under autoscaling (instances × pool ≤ `max_connections`); *N8.1 owns the spreadsheet — recall it* | TX-8 |
````

**J96** · G2 · move

````text
| **A8 — SQL design track** (concept, then lab; engine slices §4.0) *(was `2.1`)* | **The core binding.** SL-01 … SL-12 · RT-01 … RT-07 · DD-01 … DD-06, DD-12 · OD-01 · CS-01 … CS-08 — paired slice by slice with DB-1 … DB-10 (§2.2 table below) | SQL-E1 → SQL-E10 by level (§6 gates) |
````

**J97** · G2 · move

````text
| **A8** + **V-STOR** GCP relational offerings (decision table) *(was `2.2`)* | AN-01 OLTP/OLAP · DD-08 JSONB vs relational · §8.1 Rosetta table | DT-1 |
````

**J98** · G2 · move

````text
| **N2.3** Cloud SQL setup (required procedure) *(was `2.3`)* | OD-03 pooling & pool math · OD-04 backup/restore drills *as runbook (DB-10 owns the toy)* · OD-05 replicas & read-your-writes · SL-13 privileges · §8.2 Terraform | TF-DB1, TX-8, BH-5 |
````

**J99** · G2 · move

````text
| **A8** (NoSQL) + **N2.4** Firestore *(was `2.4`)* | AN-06 the *same question* in Firestore and SQL — where the document model wins and loses | DT-7 |
````

**J100** · G2 · move

````text
| **N2.5** Cloud Storage *(was `2.5`)* | PQ-04 `COPY`/import & export of CSV/JSON through GCS; encoding and NULL-vs-empty pitfalls | SQL-E8.8 – SQL-E8.10 |
````

**J101** · G2 · move

````text
| **A8** + **C4** + **N2.6** config, migrations, jobs *(was `2.6`)* | DD-11 expand/contract with **lock levels** · OD-08 migration tooling & testing (dirty state, advisory lock) | SQL-E9.6, SCH-4 |
````

**J102** · G2 · move

````text
| **A9** + **V-STOR** + **N2.7** Spanner & NoSQL map *(was `2.7`)* | AN-05 GoogleSQL/Spanner · DD-13 key design & partitioning · CS-07 TrueTime, 2PC, Paxos groups | DT-6, SCH-5 |
````

**J103** · G2 · move

````text
| **A7** software design (repositories; design-patterns Repository, Unit of Work) *(was `3.0`)* | OD-09 application data access: N+1, ORM pitfalls, prepared statements, transaction boundaries | BH-3 |
````

**J104** · G2 · move

````text
| **A7** async (Pub/Sub, Tasks, Scheduler) *(was `3.4`)* | SL-10 idempotent writes: `INSERT … ON CONFLICT`, unique keys | SQL-E9.3 |
````

**J105** · G2 · move

````text
| **A9** + design-patterns **ARCH-11** failure design (outbox/inbox, sagas) *(was `3.5`)* | CS-07 why 2PC is not the answer; SL-10 `FOR UPDATE SKIP LOCKED` job claim | TX-5, TX-8 |
````

**J106** · G2 · move

````text
| **A10 + B5** authorization · **C1** + **Phase 4 Security** secrets & supply chain *(was `4.7`, `4.9`)* | SL-13 RLS, injection, parameterisation, least-privilege roles | SQL-E10.6, BH-2 |
````

**J107** · G2 · move

````text
| **A8** + **N5.3** ledger and consistency *(was `5.3`)* | DD-05 money (integer minor units), DD-09 audit/history · SL-08 running balances · CS-05 isolation for money | SQL-E4.5, SQL-CAP2, BH-4 |
````

**J108** · G2 · move

````text
| **Phase 4 Security** + **N7.3** data protection *(was `7.3`)* | SL-13 column-level encryption (`pgcrypto`), masking views, CMEK vocabulary | SCH-6 |
````

**J109** · G2 · move

````text
| **S2** + **N8.0** Donne-Martin building blocks · **N8.C** evidence packs *(was `8.0`, `8.C`)* | DD-01 schema ADRs inside HLD packs; DD-10 denormalisation ADR; **recall** primer SD-13 … SD-19 for scale-out | SCH-2, SCH-3 |
````

**J110** · G2 · move

````text
| **N8.1** primitives — cursor pagination · hot partition · pool math · RLS · LSM vs B-tree · schema evolution · idempotency *(was `8.1`)* | OD-09 keyset SQL and its index (**N8.1.5 owns the from-scratch pager**) · DD-13 hot-key skew query · OD-03 · SL-13 · CS-02 arithmetic · DD-11 | PX-9, SQL-E4.7 |
````

**J111** · G2 · move

````text
| **V-STOR** + **N9.1** Memorystore *(was `9.1`)* | OD-09 cache-aside vs DB read path (query-level vs object-level); *no new concept* | — |
````

**J112** · G2 · move

````text
| **V-STOR** + **N9.4** Spanner, AlloyDB, Bigtable, BigQuery (ops view) *(was `9.4`)* | AN-01 · AN-02 · AN-05 · CS-09 columnar & vectorised execution | DT-1 … DT-6, SQL-E13.3 |
````

**J113** · G2 · move

````text
| **V-DATA** + **N9b.1** Big-data services (BigQuery, Dataform) *(was `9b.1`)* | AN-02 partition/cluster and bytes scanned · AN-03 cohorts/funnels · AN-04 approximate aggregation · SL-11 views & materialised views | SQL-E6.2, SQL-E6.6, SQL-E13.1 – SQL-E13.3 |
````

**J114** · G2 · move

````text
| **D3** + **N9c.1** features, labels, skew (**as-of join** owner) *(was `9c.1`)* | SL-08 / SL-04: the **SQL shape** of a point-in-time join (LATERAL / range join). *N9c.1 owns leakage; this file owns the join* | SQL-E6.4, SQL-E13.4, SQL-E13.5 |
````

**J115** · G2 · move

````text
| **D4** + **N9c.2 / N9c.5** retrieval, RAG *(was `9c.2 / 9c.5`)* | AN-07 full-text search and vector search in Postgres (`tsvector`, `pgvector`) vs dedicated engines | DT-8 |
````

**J116** · G2 · move

````text
| **C6** observability, performance *(was `10.0`, `10.5`)* | OD-01/02 plan reading & workload observation · CS-08 · PX-1 … PX-11 | PX-1 … PX-11, SQL-CAP4 |
````

**J117** · G2 · move

````text
| **C7** SLO / error budget *(was `10.1`)* | OD-05 replication lag as an SLI; recovery-point objective from WAL archiving | BH-5 |
````

**J118** · G2 · move

````text
| **B4** FinOps + billing-export SQL *(was `10.3`)* | AN-03 window analytics on a *billing-export-shaped* table; AN-02 bytes-scanned cost | DT-4, SQL-E13.1 |
````

**J119** · G2 · move

````text
| **N11** capstone (Northstar v1) *(was `11`)* | SQL-CAP1 – SQL-CAP4 are the database acceptance tests of the capstone | SQL-CAP1 – SQL-CAP4 |
````

**J120** · G2 · move

````text
| **N11b** control-plane capstone *(was `11b`)* | DD-09 audit/event log design; OD-08 migrations for the control-plane store | SCH-6 |
````

**J121** · G2 · move

````text
| ACID, CAP, consistency, big-O, hashing | `Curriculum` **M1 / A4 + U2 / A8 + A9 / A8** *(was T.Disc / T.Algo / T.SysTheory / 2.x)* | CS-05/CS-07 formal treatment of isolation and consistency models; PQ-07 recall only |
````

**J122** · G2 · move

````text
| **A1–A4 + M1** (SQL-T-HS → SQL-T-UG tiers) *(was Block T)* | PQ-01, PQ-02, PQ-07, PQ-08 with SQL-Z0.1 – SQL-Z0.8 (≈ 6 short sessions) | paper fluency: sets/bags/3VL/counting/units |
````

**J123** · G2 · move

````text
| **A3, A6, A11 + M5** *(was F1 – F4, M.NS)* | PQ-03 (types, decimals), PQ-04 (files/JSON), PQ-05 (`psql` + Docker Postgres) — the lab loads and fingerprints match (§3) | lab environment ready; no SQL semantics yet |
````

**J124** · G2 · move

````text
| **Tracks B and C (B3, C1, C4, C6)** *(was Parts 0 – 1, D)* | OD-10 (tests in CI), OD-02 (logs/slow-query vocabulary), OD-03 recall at B3 | vocabulary only; no new SQL |
````

**J125** · G2 · move

````text
| **A8 (the main event)** *(was Part 2)* | **The A8 SQL block is stretched over ≥ 3 weeks:** week 1 = RT-01/04/05 + SL-01/02/03 + SQL-E1–SQL-E3 · week 2 = RT-02 + SL-04…SL-09 + SQL-E4–SQL-E7 + DB-1/DB-3 · week 3 = SL-10 + TX labs + CS-05 + DB-9 · then DB-4…DB-8 with CS-01…CS-04, CS-08 and PX cards · then DB-10 with CS-06, OD-04 · the V-STOR and N2.3…N2.7 rows as bound in §2 | SQL competency through SQL-E9; plan and isolation predictions; the theory tier |
````

**J126** · G2 · move

````text
| **A7, A9, A10 + N5.3** *(was Parts 3 – 5)* | SQL-E9.3 (A7), TX-5 (A9), SQL-E10.6 (A10), SQL-E4.5/SQL-CAP2 (N5.3) | SQL that makes async/ledger/RLS true |
````

**J127** · G2 · move

````text
| **N8.0/N8.1/N8.C + S2** *(was Part 8)* | PX-9 / DD-13 with N8.1; SCH-2/SCH-3 inside packs | scale primitives with SQL evidence |
````

**J128** · G2 · move

````text
| **V-STOR, V-DATA, D3/D4 + N9.1/N9.4/N9b.1/N9c.1** *(was Parts 9, 9b, 9c)* | AN-01 … AN-05, SQL-E6, SQL-E13, DT drills (BigQuery), SQL-E6.4/SQL-E13.4/SQL-E13.5 at D3 (N9c.1) | analytics dialect and point-in-time joins |
````

**J129** · G2 · move

````text
| **C6, C7, B4** *(was Part 10)* | PX cards and SQL-CAP4 at C6; DT-4 at B4 | performance and cost SQL |
````

**J130** · G2 · move

````text
| **N11 / N11b** *(was Part 11 / 11b)* | SQL-CAP1 – SQL-CAP4 | database acceptance |
````

**J131** · G2 · move

````text
| **A8 skip-tests — SQL-SKIP-SQL / SQL-SKIP-ENGINE** *(was Part 12)* | skip-test via the checkpoints in the stitch table; else run the SQL-SKIP-SQL/SQL-SKIP-ENGINE orders below | continuation, only if the skip-test fails |
````

**J132** · G3 · anchor-rewrite

````text
> **Refactor note (2026-09-24, C-53):** the `TB-…` / `SRC-…` labels in the line above are this file's bibliography keys. They were first assigned in `unified-curriculum.md`; the labels are kept, the books and courses are named in full beside them.
````

**J133** · G3 · anchor-rewrite

````text
> **Refactor note (2026-09-24, §7):** the suite-wide register is `Curriculum` §0.3; this table is the SQL slice of it, and on a conflict §0.3 wins. DB-1 … DB-10 are owned by this file since C-05 (§4.0).
````

**J134** · G4 · anchor-rewrite

````text
- Tiers: `SQL-T-HS` high-school · `SQL-T-UG` undergraduate · `SQL-T-GR` graduate — the depth tier of a theory item or gate (§2 rows for M1 and A8 + A9; renamed from `HS` / `UG` / `grad` in §5 of the refactor). *(Legend added by the refactor, C-08.)*
````

**J135** · G5 · anchor-rewrite

````text
2. **Ownership split (memorise).** *`Curriculum` and Northstar own:* Cloud SQL setup (N2.3), Firestore (N2.4), migrations-as-jobs (N2.6), the Spanner/NoSQL map (N2.7), the primitives of N8.1 (cursor pager, hot partition, pool math, RLS, LSM-vs-B-tree comparison), outbox/inbox (A9 theory; design-patterns ARCH-11 shape), the ledger (N5.3), BigQuery ops (N9.4/N9b.1), as-of joins as *leakage prevention* (D3, N9c.1), billing-export SQL (B4). *This file owns:* SQL-language mastery (SL), relational theory (RT), the CS theory tier under the slices (CS), data-design method (DD), operating-a-database craft (OD), analytics and dialect craft (AN), pre-SQL prerequisites (PQ), the exercise ladder (§6), and — since the refactor (C-05) — the engine slices DB-1 … DB-10 and their toys (§4.0). **Where a §4.0 slice toy exists (WAL codec, slotted page, B-tree, iterator executor, visibility simulator) this file never asks for a second toy — it adds the analytic layer (formulas, schedules, cost models) that the toy's tests do not reach.**
````

**J136** · G5 · anchor-rewrite

````text
Why: `Curriculum` owns the order and the module spine; `northstar-reference-app.md` owns the *product spine* (Northstar on GCP) and the Cloud SQL procedure (N2.3). Since the refactor this file also owns the engine slices DB-1 … DB-10 (§4.0, C-05). `Curriculum` deliberately does not own the SQL *language* end to end, the pre-SQL mathematics a learner may lack, the theory tier behind the slices (serializability, ARIES, join-cost formulas, Selinger-style planning), modelling method, analytics dialects, or a large body of query-writing practice. This file supplies exactly those, and hangs each piece on the `Curriculum` module that needs it, **at the moment that module needs it**.
````

**J137** · G9 · anchor-rewrite

````text
### 0.5 Learner teaching preferences (binding; copied unchanged from session-progress-ledger.md §5, invariant 4)
````

**J138** · G9 · anchor-rewrite

````text
- When companion-file content (system-design-primer, SQL, design-patterns) overlaps a `Curriculum` module, **teach it once, stitched into the same session** — never as a separate pass, per each companion's own §0.2 stitching rules.
````

**J139** · G9 · anchor-rewrite

````text
- If a companion file references module IDs that don't exist in `Curriculum` (as `sql-databases-companion.md` does), **say so plainly rather than forcing a silent, possibly-wrong mapping** — this was well received when done for the SQL companion.
````

**J140** · G10 · anchor-rewrite

````text
> **Note:** the suite-wide register is `Curriculum` §0.3; this table is the SQL slice of it, and on a conflict §0.3 wins. DB-1 … DB-10 are owned by this file since C-05 (§4.0).
````

**J141** · G8 · anchor-rewrite

````text
#### PQ-04 · Files, CSV/JSON, encodings — stitch: A3 + A6 · N2.5
````

**J142** · G8 · anchor-rewrite

````text
#### RT-06 · ER → tables — stitch: S2 + N0.4 · DD-01
````

**J143** · G8 · anchor-rewrite

````text
#### SL-11 · Views, materialised views, functions, triggers — stitch: V-DATA + N9b.1
````

**J144** · G8 · anchor-rewrite

````text
#### SL-12 · Dates, time zones, JSON, text, regex — stitch: N2.5 · D3 + N9c.1
````

**J145** · G8 · anchor-rewrite

````text
#### SL-13 · Security in SQL: GRANT, RLS, injection — stitch: B5 · A10 · N8.1
````

**J146** · G8 · anchor-rewrite

````text
#### CS-02 · B-tree/B+/hash/LSM/bitmap/GIN/GiST/BRIN — stitch: DB-6 · N8.1
````

**J147** · G8 · anchor-rewrite

````text
#### CS-07 · Replication, consensus, 2PC, consistency models — stitch: DB-10 · A9 + V-STOR + N2.7 · ARCH-11
````

**J148** · G8 · anchor-rewrite

````text
#### CS-09 · Columnar & vectorised execution — stitch: V-STOR + N9.4 · AN-02
````

**J149** · G8 · anchor-rewrite

````text
#### DD-01 · Conceptual → logical → physical — stitch: S2 + N0.4 · N8.0
````

**J150** · G8 · anchor-rewrite

````text
#### DD-03 · Money, units, time — stitch: A8 + N5.3 · M5
````

**J151** · G8 · anchor-rewrite

````text
#### DD-05 · Temporal data & SCD — stitch: D3 + N9c.1 · A8 + N5.3
````

**J152** · G8 · anchor-rewrite

````text
#### DD-07 · Soft delete, audit, history — stitch: A8 + N5.3 · N11b
````

**J153** · G8 · anchor-rewrite

````text
#### DD-08 · Denormalisation with ADRs — stitch: S2 + N8.0 · primer SD-18
````

**J154** · G8 · anchor-rewrite

````text
#### DD-09 · Multi-tenancy — stitch: N8.1 · SL-13
````

**J155** · G8 · anchor-rewrite

````text
#### DD-10 · Partitioning & sharding-key design — stitch: primer SD-17 · A9 + V-STOR + N2.7
````

**J156** · G8 · anchor-rewrite

````text
#### DD-11 · Schema evolution (expand/contract) — stitch: A8 + C4 + N2.6
````

**J157** · G8 · anchor-rewrite

````text
#### DD-13 · Hot-key skew & partition keys — stitch: N8.1
````

**J158** · G8 · anchor-rewrite

````text
#### OD-03 · Connection pooling & pool math — stitch: B3 · N8.1 · N2.3
````

**J159** · G8 · anchor-rewrite

````text
#### OD-04 · Backup / restore / PITR drills — stitch: DB-10 · N2.3 + DB-10
````

**J160** · G8 · anchor-rewrite

````text
#### OD-08 · Migrations tooling & testing — stitch: A8 + C4 + N2.6 · C5
````

**J161** · G8 · anchor-rewrite

````text
#### OD-09 · Application data access — stitch: A7 · N8.1.5
````

**J162** · G8 · anchor-rewrite

````text
#### AN-01 · OLTP vs OLAP; star/snowflake — stitch: A8 + V-STOR · N9.4
````

**J163** · G8 · anchor-rewrite

````text
#### AN-02 · BigQuery / GoogleSQL cost shapes — stitch: V-STOR + N9.4 · V-DATA + N9b.1
````

**J164** · G8 · anchor-rewrite

````text
#### AN-03 · Cohorts, funnels, sessionisation, retention — stitch: V-DATA + N9b.1 · B4
````

**J165** · G8 · anchor-rewrite

````text
#### AN-04 · Approximate aggregation — stitch: V-DATA + N9b.1
````

**J166** · G8 · anchor-rewrite

````text
#### AN-05 · Spanner SQL dialect map — stitch: A9 + V-STOR + N2.7 · N9.4
````

**J167** · G8 · anchor-rewrite

````text
#### AN-06 · NoSQL query models vs SQL — stitch: A8 + N2.4
````

**J168** · G8 · anchor-rewrite

````text
#### AN-07 · Search & vectors in SQL — stitch: D4 + N9c.2 / N9c.5
````

**J481** · SQL-1 · anchor-rewrite

````text
Companion to `Curriculum` ("The Consolidated Cloud Mastery Curriculum") and to its reference application `northstar-reference-app.md` (Track N).
````

**J482** · SQL-1 · anchor-rewrite

````text
Sibling of `system-design-primer-companion.md` (its SD-13 … SD-27 own the *scale-out and interview* layer of databases; this file owns *SQL semantics, relational and storage theory, schema craft, and a query-writing exercise ladder*).
````

**J483** · SQL-1 · anchor-rewrite

````text
> **Note:** the `TB-…` / `SRC-…` labels in the line above are this file's bibliography keys. They were first assigned in `unified-curriculum.md`; the labels are kept, the books and courses are named in full beside them.
````

**J484** · SQL-1 · anchor-rewrite

````text
Why: `Curriculum` owns the order and the module spine; `northstar-reference-app.md` owns the *product spine* (Northstar on GCP) and the Cloud SQL procedure (N2.3). Since the refactor this file also owns the engine slices DB-1 … DB-10 (§4.0). `Curriculum` deliberately does not own the SQL *language* end to end, the pre-SQL mathematics a learner may lack, the theory tier behind the slices (serializability, ARIES, join-cost formulas, Selinger-style planning), modelling method, analytics dialects, or a large body of query-writing practice. This file supplies exactly those, and hangs each piece on the `Curriculum` module that needs it, **at the moment that module needs it**.
````

**J485** · SQL-1 · anchor-rewrite

````text
2. **Ownership split (memorise).** *`Curriculum` and Northstar own:* Cloud SQL setup (N2.3), Firestore (N2.4), migrations-as-jobs (N2.6), the Spanner/NoSQL map (N2.7), the primitives of N8.1 (cursor pager, hot partition, pool math, RLS, LSM-vs-B-tree comparison), outbox/inbox (A9 theory; design-patterns ARCH-11 shape), the ledger (N5.3), BigQuery ops (N9.4/N9b.1), as-of joins as *leakage prevention* (D3, N9c.1), billing-export SQL (B4). *This file owns:* SQL-language mastery (SL), relational theory (RT), the CS theory tier under the slices (CS), data-design method (DD), operating-a-database craft (OD), analytics and dialect craft (AN), pre-SQL prerequisites (PQ), the exercise ladder (§6), and — since the refactor — the engine slices DB-1 … DB-10 and their toys (§4.0). **Where a §4.0 slice toy exists (WAL codec, slotted page, B-tree, iterator executor, visibility simulator) this file never asks for a second toy — it adds the analytic layer (formulas, schedules, cost models) that the toy's tests do not reach.**
````

**J486** · SQL-1 · anchor-rewrite

````text
3. **Same ten-rung ramp, same locks.** Companion concepts are taught through the suite's ten-rung sequence (`Curriculum` §0.4.3) (anchor → vocabulary → representation → core move → worked illustration → basic unseen check → routine variation → mixed transfer → top-rung challenge → reflection + ledger). The **dependency gate**, **rung-2 vocabulary audit** and **Prop Lock** apply unchanged: never use a later system as a prop (no Spanner interleaving in the first Postgres transcript; no full PITR runbook before its owner; no Cloud SQL HA as a "known" prop before its N2.3 session). If an exercise needs machinery not yet unlocked, **postpone the exercise** — or teach the machinery first. A smuggled prop is an *instructor process failure*, never "shaky", exactly as in `Curriculum` §0.4.6.
````

**J487** · SQL-1 · anchor-rewrite

````text
3. **Same ten-rung ramp, same locks.** Companion concepts are taught through the suite's ten-rung sequence (rule 0.4.3, §0.6) (anchor → vocabulary → representation → core move → worked illustration → basic unseen check → routine variation → mixed transfer → top-rung challenge → reflection + ledger). The **dependency gate**, **rung-2 vocabulary audit** and **Prop Lock** apply unchanged: never use a later system as a prop (no Spanner interleaving in the first Postgres transcript; no full PITR runbook before its owner; no Cloud SQL HA as a "known" prop before its N2.3 session). If an exercise needs machinery not yet unlocked, **postpone the exercise** — or teach the machinery first. A smuggled prop is an *instructor process failure*, never "shaky", exactly as in `Curriculum` §0.4.6.
````

**J488** · SQL-1 · anchor-rewrite

````text
3. **Same ten-rung ramp, same locks.** Companion concepts are taught through the suite's ten-rung sequence (rule 0.4.3, §0.6) (anchor → vocabulary → representation → core move → worked illustration → basic unseen check → routine variation → mixed transfer → top-rung challenge → reflection + ledger). The **dependency gate**, **rung-2 vocabulary audit** and **Prop Lock** apply unchanged: never use a later system as a prop (no Spanner interleaving in the first Postgres transcript; no full PITR runbook before its owner; no Cloud SQL HA as a "known" prop before its OD-11 session). If an exercise needs machinery not yet unlocked, **postpone the exercise** — or teach the machinery first. A smuggled prop is an *instructor process failure*, never "shaky", exactly as in `Curriculum` §0.4.6.
````

**J489** · SQL-1 · anchor-rewrite

````text
6. **Predict before you run; explain the discrepancy after.** Every exercise that has a *result shape*, a *row count*, a *plan shape*, or an *isolation outcome* starts with the learner writing the prediction (one line). Then run. A wrong prediction is the best teaching moment in this file — record the discrepancy on the ledger, do not skip it. (`Curriculum` §0.4.4, predict → run → discrepancy; C-53.)
````

**J490** · SQL-1 · anchor-rewrite

````text
8. **Tracking is inline.** Tick `- [ ]` boxes in this file or say "done" in chat. Do **not** create a separate tracker; the learner ledger `session-progress-ledger.md` (C-57; it replaces the old parent's "Teaching contract → Learner state") records unlocked / shaky / postponed for companion modules under their IDs (`SL-08`, `SQL-E6.2`…).
````

**J491** · SQL-1 · anchor-rewrite

````text
10. **Time, money and secrets.** Labs are free-tier/credits-safe: local Postgres in Docker is the default; Cloud SQL / AlloyDB / Memorystore are credits-optional and *destroyed the same day* (`Curriculum` §0.5 Lab Safety). Never put a password, key or real customer data in a query, a prompt or this file; the lab data is synthetic.
````

**J492** · SQL-1 · anchor-rewrite

````text
11. **User can override anything:** skip a concept already known (run its skip-test; §5 tiers), jump to an exercise, or go hands-on — same rights as `Curriculum` §0.4.1. **On a conflict:** `Curriculum` wins on order, Lab Reality, exam time-sensitivity and the ledger; this file wins on SQL/DB content and exercise specs.
````

**J493** · SQL-1 · anchor-rewrite

````text
When other companions bind to the same session, the Suite Session Protocol in `Curriculum` §0.4 governs.
````

**J494** · SQL-1 · anchor-rewrite

````text
- The old parent's labels (`T.*`, `F1…F4`, `M.*`, `0.x`, `1.x`, `D0…D8`, `2.x` … `11b`, `12.Sxx`, `G4`, `G12b`) were rebound on 2026-09-24 to `Curriculum` IDs (`A1…D4`, `M1…M6`, `U1…U7`, `S1…S11`, the Part V category IDs `V-…`) and Northstar sections (`Nx.y`); `crosswalk.md` §1 has every mapping. `DB-1 … DB-10` are this file's engine slices (§4.0). `SD-13 … SD-27` are primer-companion IDs. `TB-…`/`SRC-…` are this file's bibliography labels (title block).
````

**J495** · SQL-1 · anchor-rewrite

````text
- Tiers: `SQL-T-HS` high-school · `SQL-T-UG` undergraduate · `SQL-T-GR` graduate — the depth tier of a theory item or gate (§2 rows for M1 and A8 + A9; renamed from `HS` / `UG` / `grad` in §5 of the refactor).
````

**J496** · SQL-1 · anchor-rewrite

````text
- `Northstar` = the running reference application (`northstar-reference-app.md`, Track N); the lab database is its OLTP slice plus an event stream.
````

**J497** · SQL-1 · anchor-rewrite

````text
| `Curriculum` module (was: old-parent label) | Companion modules taught in the same session | Checkpoint |
````

**J498** · SQL-1 · anchor-rewrite

````text
| **S2** + **N0.4** HLD/LLD contract, ADR template, NFR table | DD-01 conceptual → logical → physical; **schema ADRs** ("I pick X because Y, I accept Z") · DD-12 constraints as spec | SCH-1 |
````

**J499** · SQL-1 · anchor-rewrite

````text
| **B5** IAM (+ **N2.3** IAM DB auth) | SL-13 database roles vs IAM principals, `GRANT`/`REVOKE`, least privilege | SQL-E10.6 (RLS) after A10 |
````

**J500** · SQL-1 · anchor-rewrite

````text
| **B3** HA & autoscaling | OD-03 pool arithmetic under autoscaling (instances × pool ≤ `max_connections`); *N8.1 owns the spreadsheet — recall it* | TX-8 |
````

**J501** · SQL-1 · anchor-rewrite

````text
| **N2.3** Cloud SQL setup (required procedure) | OD-03 pooling & pool math · OD-04 backup/restore drills *as runbook (DB-10 owns the toy)* · OD-05 replicas & read-your-writes · SL-13 privileges · §8.2 Terraform | TF-DB1, TX-8, BH-5 |
````

**J502** · SQL-1 · anchor-rewrite

````text
| **A8** (NoSQL) + **N2.4** Firestore | AN-06 the *same question* in Firestore and SQL — where the document model wins and loses | DT-7 |
````

**J503** · SQL-1 · anchor-rewrite

````text
| **N2.5** Cloud Storage | PQ-04 `COPY`/import & export of CSV/JSON through GCS; encoding and NULL-vs-empty pitfalls | SQL-E8.8 – SQL-E8.10 |
````

**J504** · SQL-1 · anchor-rewrite

````text
| **A8** + **C4** + **N2.6** config, migrations, jobs | DD-11 expand/contract with **lock levels** · OD-08 migration tooling & testing (dirty state, advisory lock) | SQL-E9.6, SCH-4 |
````

**J505** · SQL-1 · anchor-rewrite

````text
| **A8** + **C4** config, migrations, jobs | DD-11 expand/contract with **lock levels** · OD-08 migration tooling & testing (dirty state, advisory lock) | SQL-E9.6, SCH-4 |
````

**J506** · SQL-1 · anchor-rewrite

````text
| **A9** + **V-STOR** + **N2.7** Spanner & NoSQL map | AN-05 GoogleSQL/Spanner · DD-13 key design & partitioning · CS-07 TrueTime, 2PC, Paxos groups | DT-6, SCH-5 |
````

**J507** · SQL-1 · anchor-rewrite

````text
| **A8** + **N5.3** ledger and consistency | DD-05 money (integer minor units), DD-09 audit/history · SL-08 running balances · CS-05 isolation for money | SQL-E4.5, SQL-CAP2, BH-4 |
````

**J508** · SQL-1 · anchor-rewrite

````text
| **A8** ledger and consistency | DD-05 money (integer minor units), DD-09 audit/history · SL-08 running balances · CS-05 isolation for money | SQL-E4.5, SQL-CAP2, BH-4 |
````

**J509** · SQL-1 · anchor-rewrite

````text
| **Phase 4 Security** + **N7.3** data protection | SL-13 column-level encryption (`pgcrypto`), masking views, CMEK vocabulary | SCH-6 |
````

**J510** · SQL-1 · anchor-rewrite

````text
| **S2** + **N8.0** Donne-Martin building blocks · **N8.C** evidence packs | DD-01 schema ADRs inside HLD packs; DD-10 denormalisation ADR; **recall** primer SD-13 … SD-19 for scale-out | SCH-2, SCH-3 |
````

**J511** · SQL-1 · anchor-rewrite

````text
| **N8.1** primitives — cursor pagination · hot partition · pool math · RLS · LSM vs B-tree · schema evolution · idempotency | OD-09 keyset SQL and its index (**N8.1.5 owns the from-scratch pager**) · DD-13 hot-key skew query · OD-03 · SL-13 · CS-02 arithmetic · DD-11 | PX-9, SQL-E4.7 |
````

**J512** · SQL-1 · anchor-rewrite

````text
| **A9** scale primitives — cursor pagination · hot partition · pool math · RLS · LSM vs B-tree · schema evolution · idempotency | OD-09 keyset SQL and its index (**N8.1.5 owns the from-scratch pager**) · DD-13 hot-key skew query · OD-03 · SL-13 · CS-02 arithmetic · DD-11 | PX-9, SQL-E4.7 |
````

**J513** · SQL-1 · anchor-rewrite

````text
| **V-STOR** + **N9.1** Memorystore | OD-09 cache-aside vs DB read path (query-level vs object-level); *no new concept* | — |
````

**J514** · SQL-1 · anchor-rewrite

````text
| **V-STOR** + **N9.4** Spanner, AlloyDB, Bigtable, BigQuery (ops view) | AN-01 · AN-02 · AN-05 · CS-09 columnar & vectorised execution | DT-1 … DT-6, SQL-E13.3 |
````

**J515** · SQL-1 · anchor-rewrite

````text
| **V-DATA** + **N9b.1** Big-data services (BigQuery, Dataform) | AN-02 partition/cluster and bytes scanned · AN-03 cohorts/funnels · AN-04 approximate aggregation · SL-11 views & materialised views | SQL-E6.2, SQL-E6.6, SQL-E13.1 – SQL-E13.3 |
````

**J516** · SQL-1 · anchor-rewrite

````text
| **D3** + **N9c.1** features, labels, skew (**as-of join** owner) | SL-08 / SL-04: the **SQL shape** of a point-in-time join (LATERAL / range join). *N9c.1 owns leakage; this file owns the join* | SQL-E6.4, SQL-E13.4, SQL-E13.5 |
````

**J517** · SQL-1 · anchor-rewrite

````text
| **D3** features, labels, skew | DD-05 leakage and point-in-time correctness · SL-08 / SL-04: the **SQL shape** of a point-in-time join (LATERAL / range join). *N9c.1 owns leakage; this file owns the join* | SQL-E6.4, SQL-E13.4, SQL-E13.5 |
````

**J518** · SQL-1 · anchor-rewrite

````text
| **D4** + **N9c.2 / N9c.5** retrieval, RAG | AN-07 full-text search and vector search in Postgres (`tsvector`, `pgvector`) vs dedicated engines | DT-8 |
````

**J519** · SQL-1 · anchor-rewrite

````text
| **N11** capstone (Northstar v1) | SQL-CAP1 – SQL-CAP4 are the database acceptance tests of the capstone | SQL-CAP1 – SQL-CAP4 |
````

**J520** · SQL-1 · anchor-rewrite

````text
| **N11b** control-plane capstone | DD-09 audit/event log design; OD-08 migrations for the control-plane store | SCH-6 |
````

**J521** · SQL-1 · anchor-rewrite

````text
> **Note:** the suite-wide register is `Curriculum` §0.3; this table is the SQL slice of it, and on a conflict the main course's register wins. DB-1 … DB-10 are owned by this file since C-05 (§4.0).
````

**J522** · SQL-1 · anchor-rewrite

````text
> **Note:** the suite-wide register is the main course §0.3; this table is the SQL slice of it, and on a conflict the main course's register wins. DB-1 … DB-10 are owned by this file since C-05 (§4.0).
````

**J523** · SQL-1 · anchor-rewrite

````text
| Relational algebra, 3VL (DB-1) | **§4.0 DB-1** (this file since C-05; A8) (toy: bag relations + truth-table tests) | RT-02 set-vs-bag laws and rewrite equivalences; RT-03 calculus/safety; SL-03 NULL semantics across every clause; SQL-Z0.4, TD-5/6 |
````

**J524** · SQL-1 · anchor-rewrite

````text
| WAL, replica, PITR (DB-10; foreign `G4` → N2.3) | **§4.0 DB-10** (toy: mini-WAL) | CS-06 ARIES and steal/no-force reasoning; TD-12; OD-04 restore-drill runbook |
````

**J525** · SQL-1 · anchor-rewrite

````text
| Cloud SQL provisioning, Auth Proxy, private IP, HA, flags | **N2.3** | OD-03/04/05 SQL-side consequences (session state vs pooler modes, RPO/RTO arithmetic, replica lag); §8.2 Terraform |
````

**J526** · SQL-1 · anchor-rewrite

````text
| Migrations as jobs, expand/contract | **N2.6** | DD-11 *lock levels*, `NOT VALID` + `VALIDATE`, `CREATE INDEX CONCURRENTLY`, backfill batching (SQL-E9.6) |
````

**J527** · SQL-1 · anchor-rewrite

````text
| Spanner, Bigtable, Firestore map | **N2.7 / N2.4** | AN-05, AN-06 same-question comparisons; DD-13 key design as SQL |
````

**J528** · SQL-1 · anchor-rewrite

````text
| Cursor pagination | **N8.1.5** (from-scratch pager) | OD-09 the SQL seek predicate & its supporting index; PX-9 measured against OFFSET |
````

**J529** · SQL-1 · anchor-rewrite

````text
| Hot partition, key histogram | **N8.1** | DD-13 the skew query on lab data (user 1 = 135 orders; see PX-1) |
````

**J530** · SQL-1 · anchor-rewrite

````text
| Connection-pool math | **N8.1 / N2.3** | OD-03 pooler modes (session/transaction/statement) and what breaks in transaction mode |
````

**J531** · SQL-1 · anchor-rewrite

````text
| RLS multi-tenancy | **N8.1 / A8** | SL-13 policy syntax, `FORCE`, owner bypass; SQL-E10.2 composite FK as defence in depth; SQL-E10.6 |
````

**J532** · SQL-1 · anchor-rewrite

````text
| Outbox / inbox, idempotency | **A9 / A7** (`Curriculum` §0.3: 2PC/Saga/outbox) | SL-10 the SQL that makes them true (unique index, `ON CONFLICT`, `SKIP LOCKED`); TX-5, SQL-E9.3 |
````

**J533** · SQL-1 · anchor-rewrite

````text
| Ledger, minor-unit ints | **N5.3** | DD-05 modelling; SQL-E4.5/SQL-CAP2 revenue reconciliation; SQL-CAP1 invariants |
````

**J534** · SQL-1 · anchor-rewrite

````text
| BigQuery partition/cluster/cost | **N9.4 / N9b.1** | AN-02 SQL-level cost reading; DT drills |
````

**J535** · SQL-1 · anchor-rewrite

````text
| As-of / point-in-time join | **N9c.1** (D3) | SQL-E6.4 / SQL-E13.4 / SQL-E13.5 the SQL shapes (lateral, range join, SCD2) |
````

**J536** · SQL-1 · anchor-rewrite

````text
| ACID, CAP, consistency, big-O, hashing | `Curriculum` **M1 / A4 + U2 / A8 + A9 / A8** | CS-05/CS-07 formal treatment of isolation and consistency models; PQ-07 recall only |
````

**J537** · SQL-1 · anchor-rewrite

````text
| **DB-10** WAL, replica, PITR (**N2.3**) | CS-06, CS-07 · TD-12, TD-14 | — | BH-5, OD-04 restore drill, TX-8 |
````

**J538** · SQL-1 · anchor-rewrite

````text
`Curriculum`'s spine is Phases 0–3 (Tracks A–D, mostly in parallel) → Phase 4 → …, with the reserved M/U/S tracks placed by R4. SQL does not first *appear* until A8, so the calendar front-loads only **cheap, unlockable prerequisites** and holds the language until A8 needs it (Prop Lock: no SQL vocabulary before it is anchored).
````

**J539** · SQL-1 · anchor-rewrite

````text
| **A8 (the main event)** | **The A8 SQL block is stretched over ≥ 3 weeks:** week 1 = RT-01/04/05 + SL-01/02/03 + SQL-E1–SQL-E3 · week 2 = RT-02 + SL-04…SL-09 + SQL-E4–SQL-E7 + DB-1/DB-3 · week 3 = SL-10 + TX labs + CS-05 + DB-9 · then DB-4…DB-8 with CS-01…CS-04, CS-08 and PX cards · then DB-10 with CS-06, OD-04 · the V-STOR and N2.3…N2.7 rows as bound in §2 | SQL competency through SQL-E9; plan and isolation predictions; the theory tier |
````

**J540** · SQL-1 · anchor-rewrite

````text
| **A7, A9, A10 + N5.3** | SQL-E9.3 (A7), TX-5 (A9), SQL-E10.6 (A10), SQL-E4.5/SQL-CAP2 (N5.3) | SQL that makes async/ledger/RLS true |
````

**J541** · SQL-1 · anchor-rewrite

````text
| **N8.0/N8.1/N8.C + S2** | PX-9 / DD-13 with N8.1; SCH-2/SCH-3 inside packs | scale primitives with SQL evidence |
````

**J542** · SQL-1 · anchor-rewrite

````text
| **V-STOR, V-DATA, D3/D4 + N9.1/N9.4/N9b.1/N9c.1** | AN-01 … AN-05, SQL-E6, SQL-E13, DT drills (BigQuery), SQL-E6.4/SQL-E13.4/SQL-E13.5 at D3 (N9c.1) | analytics dialect and point-in-time joins |
````

**J543** · SQL-1 · anchor-rewrite

````text
| **V-STOR, V-DATA, D3/D4** | AN-01 … AN-05, SQL-E6, SQL-E13, DT drills (BigQuery), SQL-E6.4/SQL-E13.4/SQL-E13.5 at D3 (N9c.1) | analytics dialect and point-in-time joins |
````

**J544** · SQL-1 · anchor-rewrite

````text
| **N11 / N11b** | SQL-CAP1 – SQL-CAP4 | database acceptance |
````

**J545** · SQL-1 · anchor-rewrite

````text
**SQL-SKIP-SQL order → companion modules (order unchanged; provenance: `unified-curriculum.md` §5.4):** relations/keys/FDs/normalisation → **RT-01, RT-04, RT-05** · relational algebra → **RT-02** (+ TD-5/6) · DDL/types/constraints → **SL-01, DD-04, DD-12** · SELECT semantics & NULL/3VL → **SL-02, SL-03** · joins incl. semi/anti/outer → **SL-04** · aggregation → **SL-05** · subqueries/CTEs/recursion → **SL-06, SL-07, SL-09** · windows → **SL-08** · transactions/isolation → **CS-05** + TX labs · pagination and application access → **OD-09**. *Predict multiplicity and NULL behaviour before execution.*
````

**J546** · SQL-1 · anchor-rewrite

````text
## 3. Lab kit — deterministic Northstar SQL lab
````

**J547** · SQL-1 · anchor-rewrite

````text
Local PostgreSQL 15.x database `labdb` with schema `lab` (OLTP slice of Northstar) plus `work` (scratch) and fingerprint functions `lab.chk` / `lab.chk_o`. Sources on this box: `sql-companion-work/lab_schema.sql`, `lab_seed.sql`, runners `run_ex.py`, `plans.py`, `tx_tests.py`.
````

**J548** · SQL-1 · anchor-rewrite

````text
Cloud SQL / AlloyDB: same SQL; create an instance only when Lab Reality allows and **destroy the same day** (`Curriculum` §0.5). Auth Proxy for IAM DB auth when N2.3 is unlocked — not required for local goldens.
````

**J549** · SQL-1 · anchor-rewrite

````text
Every exercise with a result shape, row count, plan shape, or isolation outcome: write the prediction (one line) **before** `psql`. Record discrepancies on the ledger — wrong predictions are the teaching moment (gcp "Database protocol").
````

**J550** · SQL-1 · anchor-rewrite

````text
### 3.7 How runners relate
````

**J551** · SQL-1 · anchor-rewrite

````text
Format per module (same contract as `system-design-primer-companion.md`): **Core** · **Theory** · **GCP lens** (Lens-1 always) · **Lab** · **Check** (answer before explanation). Tick `- [ ]` when taught *and* checks answered. Ownership: where a §4.0 slice toy exists, the concept modules add analysis only.
````

**J552** · SQL-1 · anchor-rewrite

````text
*Ported by the refactor (2026-09-24, C-05; decision D1).* **Source material:** `gcp-curriculum.md` lines 3118–3179 ("Engine slices DB-1–DB-10"), copied verbatim except for the ID rebinding marked in `crosswalk.md`. Since the refactor this file **owns** the slices; `Curriculum` A8 points here, and each slice is taught as one session with the companion theory paired to it in §2.2. The Cloud SQL procedure they map onto is N2.3.
````

**J553** · SQL-1 · anchor-rewrite

````text
- **Cloud SQL mapping:** Flags for constraints; migrations via Job (N2.6); IAM DB users still have catalogs.
````

**J554** · SQL-1 · anchor-rewrite

````text
#### DB-10 — WAL, replica, PITR (foreign `G4` WAL codec → N2.3)
````

**J555** · SQL-1 · anchor-rewrite

````text
- **GCP lens:** Lens-1: Northstar OLTP stays ≥3NF; analytics star schemas deliberately denormalise (AN-01).
````

**J556** · SQL-1 · anchor-rewrite

````text
- **GCP lens:** Lens-1: schema ADR in HLD pack. Lens-2: lab ER is Northstar OLTP slice.
````

**J557** · SQL-1 · anchor-rewrite

````text
- **Lab:** SQL-E3.1–SQL-E3.10; SQL-E6.4 as-of shape (leakage owner is N9c.1).
````

**J558** · SQL-1 · anchor-rewrite

````text
- **GCP lens:** Lens-1: N8.1 owns LSM-vs-B-tree comparison toy; here formulas + PX cards. Lens-2: PX-1…PX-6.
````

**J560** · SQL-1 · anchor-rewrite

````text
- **Theory:** TrueTime/Paxos *vocabulary* when A9 / N2.7 is unlocked — no second Spanner toy.
````

**J561** · SQL-1 · anchor-rewrite

````text
- **GCP lens:** Lens-1: ledger rules in N5.3 — this file models them. Lens-2: SQL-E4.5, SQL-CAP2.
````

**J563** · SQL-2 · new-content

````text
- **Theory:** Leakage prevention is owned by N9c.1; SQL shapes live here.
````

**J564** · SQL-1 · anchor-rewrite

````text
- **GCP lens:** Lens-1: N8.1 owns RLS primitive; here SQL policies + composite FKs. Lens-2: SQL-E10.2, SQL-E10.6.
````

**J565** · SQL-1 · anchor-rewrite

````text
- **Theory:** Hot-tenant skew.
````

**J566** · SQL-1 · anchor-rewrite

````text
- **Theory:** N2.6 owns migrations-as-jobs; here lock/SQL craft.
````

**J567** · SQL-1 · anchor-rewrite

````text
- **GCP lens:** Lens-1: N8.1 owns the hot-partition primitive. Lens-2: skew query on lab.
````

**J569** · SQL-2 · new-content

````text
- **Theory:** N8.1 owns the spreadsheet — recall it.
````

**J570** · SQL-2 · new-content

````text
- **Theory:** gcp owns migrations-as-jobs; here SQL test discipline.
````

**J571** · SQL-2 · new-content

````text
- **Theory:** N8.1.5 owns the from-scratch pager — here the seek predicate & index.
````

**J572** · SQL-1 · anchor-rewrite

````text
### 4.6 Operating databases (OD-01 … OD-10)
````

**J573** · SQL-1 · anchor-rewrite

````text
| **Operating databases** | indexing strategy & `EXPLAIN` workflow · statistics & slow-query observability · connection pooling · backup/restore/PITR drills · replication & read-your-writes · vacuum/bloat · retention & partitions · migrations tooling & testing · application data access (N+1, ORMs, prepared statements, injection, pagination) · testing SQL | OD-01 … OD-10, PX-1 … PX-11, BH-1 … BH-6, TF-DB1 … TF-DB6 |
````

**J575** · SQL-1 · anchor-rewrite

````text
- **Theory:** Northstar OLTP lab vs analytics copies.
````

**J576** · SQL-2 · new-content

````text
- **Theory:** gcp owns ops; here SQL-level reading.
````

**J577** · SQL-1 · anchor-rewrite

````text
- **Theory:** Firestore when it wins/loses — gcp owns product; here same-question drill.
````

**J578** · SQL-1 · anchor-rewrite

````text
Mapped to the A8 skip-tests **SQL-SKIP-SQL** / **SQL-SKIP-ENGINE** (provenance: `unified-curriculum.md` nodes `DB-SQL` / `DB-ENGINE`). If the A8 sessions already confirmed the skill, **stamp and skip**; else run the order in §2.3.
````

**J579** · SQL-1 · anchor-rewrite

````text
- **Trap:** A plain equi-join on `product_id` returns three rows per line. Use `LATERAL … ORDER BY valid_from DESC LIMIT 1` (or `DISTINCT ON`, or a window). The `<=` boundary is inclusive: an order at exactly `valid_from` sees the *new* price. This is the same shape as **N9c.1** (D3) point-in-time joins. Wrong-path fingerprint (do not chase): `808:97a9c21a` — plain equi-join returns all three price rows.
````

**J580** · SQL-1 · anchor-rewrite

````text
- **Trap:** Never call `now()` in a graded query — the answer changes daily. Parameterise the 'as-of' instant. Same principle as the Northstar ledger's (N5.3) determinism rules.
````

**J581** · SQL-1 · anchor-rewrite

````text
- **Prompt:** Setup gives `work.o` (copy of `customer_order`) with a new nullable column `total_major numeric(12,2)`. Backfill `total_minor / 100.0` in chunks of **1,000 rows**, looping until no rows are left. (Here one transaction; in production every chunk commits separately — N2.6 expand/contract.)
````

**J582** · SQL-1 · anchor-rewrite

````text
- **Trap:** `user_id REFERENCES app_user` alone only proves the user *exists*. The composite `FOREIGN KEY (tenant_id, user_id) REFERENCES app_user (tenant_id, user_id)` needs a matching unique constraint on the parent — that is why the lab's `app_user` carries `UNIQUE (tenant_id, user_id)`. This is defence in depth beneath RLS (N8.1).
````

**J583** · SQL-1 · anchor-rewrite

````text
- **Trap:** RLS does **not** apply to the table owner or superusers unless `FORCE ROW LEVEL SECURITY`. `current_setting('x', true)` returns NULL when unset (no rows), without `true` it raises. Connection-pool reuse means the setting must be `SET LOCAL` per transaction — N8.1 RLS.
````

**J584** · SQL-1 · anchor-rewrite

````text
- **Trap:** Facts hold measures + foreign keys at one **grain** (an order line); dimensions hold descriptions. Decide grain first, write it in one sentence. In BigQuery you would partition the fact by date and cluster by product (V-DATA, N9b.1) and often *denormalise* the dimensions in.
````

**J585** · SQL-1 · anchor-rewrite

````text
- **Tags:** PX-9 · OD-09 · N8.1.5
````

**J586** · SQL-1 · anchor-rewrite

````text
- **Tags:** N5.3·DD-05
````

**J587** · SQL-1 · anchor-rewrite

````text
- **Tags:** AN-06·N2.4
````

**J588** · SQL-1 · anchor-rewrite

````text
- **Tags:** DD-02·N8.0
````

**J589** · SQL-1 · anchor-rewrite

````text
- **Tags:** DD-11·N2.6
````

**J590** · SQL-1 · anchor-rewrite

````text
- **Tags:** DD-13·N2.7
````

**J591** · SQL-1 · anchor-rewrite

````text
- **Tags:** DD-07·N7.3
````

**J592** · SQL-1 · anchor-rewrite

````text
Mirror `Curriculum` C5 posture: **`terraform plan` reads the graph; apply only if Lab Reality + credits allow, destroy same day.**
````

**J593** · SQL-1 · anchor-rewrite

````text
| **TF-DB1** | Cloud SQL Postgres instance + private IP + flags sketch | Ties OD-03/04; Auth Proxy as separate module |
````

**J594** · SQL-1 · anchor-rewrite

````text
Database acceptance tests for N11 (Northstar). Issue after the §6 level-14 gate. **Predict; run; reconcile.**
````

**J595** · SQL-1 · anchor-rewrite

````text
- **Goldens:** 92/92 exercise cards carry fingerprints from local JSON artefacts (`goldens_ex_l1_4.json`, `goldens_ex_l5_8.json`, `goldens_ex_l9_13.json`, `goldens_ex_l14.json`). They were produced by `run_ex.py` against seed v1; this build **wires those values verbatim** and does not re-execute Postgres in the markdown generator.
````

**J596** · SQL-1 · anchor-rewrite

````text
- **SQL-E3.7 note:** `out_ex_l1_4.txt` contains a duplicate run line with a divergent hash; **JSON golden `100:1b05fa94` is authoritative**.
````

**J597** · SQL-1 · anchor-rewrite

````text
- **gcp toys DB-1…DB-10:** not duplicated; analytic layer only.
````

**J599** · SQL-4 · anchor-rewrite

````text
-- Northstar SQL Lab — schema v1 (PostgreSQL 15+; runs unchanged on Cloud SQL / AlloyDB for PostgreSQL)
````

**J600** · SQL-4 · anchor-rewrite

````text
-- Northstar SQL Lab — deterministic seed v1. No random(): every value is a pure function of its ids.
````

**J601** · SQL-4 · anchor-rewrite

````text
   trap="A plain equi-join on `product_id` returns three rows per line. Use `LATERAL … ORDER BY valid_from DESC LIMIT 1` (or `DISTINCT ON`, or a window). The `<=` boundary is inclusive: an order at exactly `valid_from` sees the *new* price. This is the same shape as gcp-curriculum **9c.1** point-in-time joins.",
````

**J602** · SQL-4 · anchor-rewrite

````text
   trap="Never call `now()` in a graded query — the answer changes daily. Parameterise the 'as-of' instant. Same principle as the gcp-curriculum ledger's determinism rules.",
````

**J603** · SQL-4 · anchor-rewrite

````text
   trap="`SET n = daily_orders.n + EXCLUDED.n` is *not* idempotent (a re-run doubles). `SET n = EXCLUDED.n` is. If your source query returned two rows for one day in a single statement you would get `ON CONFLICT DO UPDATE command cannot affect row a second time` — aggregate first. Idempotent writes are the whole point of gcp-curriculum 3.4/3.5.",
````

**J604** · SQL-4 · anchor-rewrite

````text
   prompt="Setup gives `work.o` (copy of `customer_order`) with a new nullable column `total_major numeric(12,2)`. Backfill `total_minor / 100.0` in chunks of **1,000 rows**, looping until no rows are left. (Here one transaction; in production every chunk commits separately — gcp-curriculum 2.6 expand/contract.)",
````

**J605** · SQL-4 · anchor-rewrite

````text
   trap="`user_id REFERENCES app_user` alone only proves the user *exists*. The composite `FOREIGN KEY (tenant_id, user_id) REFERENCES app_user (tenant_id, user_id)` needs a matching unique constraint on the parent — that is why the lab's `app_user` carries `UNIQUE (tenant_id, user_id)`. This is defence in depth beneath RLS (gcp-curriculum 8.1).",
````

**J606** · SQL-4 · anchor-rewrite

````text
   trap="RLS does **not** apply to the table owner or superusers unless `FORCE ROW LEVEL SECURITY`. `current_setting('x', true)` returns NULL when unset (no rows), without `true` it raises. Connection-pool reuse means the setting must be `SET LOCAL` per transaction — gcp-curriculum 8.1 RLS.",
````

**J607** · SQL-4 · anchor-rewrite

````text
   trap="Facts hold measures + foreign keys at one **grain** (an order line); dimensions hold descriptions. Decide grain first, write it in one sentence. In BigQuery you would partition the fact by date and cluster by product (gcp-curriculum 9b.1) and often *denormalise* the dimensions in.",
````

**J608** · SQL-4 · anchor-rewrite

````text
   trap="`LATERAL` runs the subquery once per outer row and can reference it — the SQL for-each loop. Missing index on `(user_id, placed_at)` makes it a seq scan per user (E12.1).",
````

**J609** · SQL-8 · anchor-rewrite

````text
| **A8 — SQL design track** (concept, then lab; engine slices §4.0) | **The core binding.** SL-01 … SL-12 · RT-01 … RT-07 · DD-01 … DD-06, DD-12 · OD-01 · CS-01 … CS-08 — paired slice by slice with DB-1 … DB-10 (§2.2 table below) | SQL-E1 → SQL-E10 by level (§6 gates) |
````

**J610** · SQL-8 · anchor-rewrite

````text
| **A8** + **C4** config, migrations, jobs | DD-11 expand/contract with **lock levels** · OD-08 migrations as jobs, tooling & testing (dirty state, advisory lock) | SQL-E9.6, SCH-4 |
````

**J612** · SQL-6 · anchor-rewrite

````text
## 0. Read this first — how this file complements `Curriculum`
````

**J613** · SQL-6 · anchor-rewrite

````text
**This file is a complement to `Curriculum`, not a second curriculum. Read both. Whenever a `Curriculum` module is taught, also teach every companion concept bound to it (§2) in the same session, as one story. Similar, related, and overlapping concepts are stitched together and taught in parallel — never in separate sessions, never twice.**
````

**J614** · SQL-6 · anchor-rewrite

````text
Why: the main course owns the order and the module spine. This file owns the engine slices DB-1 … DB-10 (§4.0) and the Cloud SQL procedure (OD-11). The main course deliberately does not own the SQL *language* end to end, the pre-SQL mathematics a learner may lack, the theory tier behind the slices (serializability, ARIES, join-cost formulas, Selinger-style planning), modelling method, analytics dialects, or a large body of query-writing practice. This file supplies exactly those, and hangs each piece on the `Curriculum` module that needs it, **at the moment that module needs it**.
````

**J615** · SQL-6 · anchor-rewrite

````text
12. **Read economically.** Each session read §0 and §2, then only the blocks bound to today's `Curriculum` module (search by ID: `SL-06`, `CS-05`, `SQL-E4.5`…). Do not reload the whole file. Appendix K (keys) is opened *only after* an attempt.
````

**J616** · SQL-6 · anchor-rewrite

````text
1. **Anchor** — announce the `Curriculum` module and list the companion modules bound to it (§2). Run the one-line pre-rung-2 self-check: every term to be used is anchored this session or on the ledger; no unanchored sibling; no new product; every noun in the picture unlocked.
````

**J617** · SQL-6 · anchor-rewrite

````text
2. **Concept** — teach the shared idea once (`Curriculum` depth), then layer this file's SQL / theory / craft on top. Derive before you name.
````

**J618** · SQL-6 · anchor-rewrite

````text
Each `Curriculum` module on the left is taught **with** the companion modules on the right, in the same session (§0.2 rule 1). "Checkpoint" is the exercise (or drill) to run once that module and its stitched concepts are done — issued **one at a time**, per rule 5.
````

**J619** · SQL-6 · anchor-rewrite

````text
### 2.3 Parallel calendar — how the companion rides `Curriculum`'s spine
````

**J620** · SQL-6 · anchor-rewrite

````text
| Window (`Curriculum`) | Companion work (parallel, small) | Outcome |
````

**J623** · SQL-7 · anchor-rewrite

````text
- **SQL-CAP3:** design/TX evidence capstone — no single `lab.chk` fingerprint (stub: acceptance via transcript + ADR).
````

**J624** · SQL-7 · anchor-rewrite

````text
- **TF-DB*:** plan-only stubs; no checked-in `.tf` in this companion (owned by learner under Lab Reality).
````

**J845** · GO-11 · anchor-rewrite

````text
- **Build lab `[local]`:** a `cursorpage` package (Python, then Go). Encode and decode an opaque, signed cursor over `(placed_at, order_id)`; run it against a fake ordered store searched by binary search, then against the lab's `customer_order`. Tests: forward pages; the empty result; a row deleted between two pages; a tampered cursor rejected. API shape: `GET /items?cursor=&limit=`.
````

**J879** · R4-9 · anchor-rewrite

````text
- Main-course IDs (`A1…D4`, `M1…M6`, `U1…U7`, `S1…S11`, the Part V category IDs `V-…`) are stitch tags into the main course. `DB-1 … DB-10` are this file's engine slices (§4.0). `SD-…` are primer-companion IDs. `TB-…`/`SRC-…` are this file's bibliography labels (title block).
````

**J880** · R4-9 · anchor-rewrite

````text
- Tiers: `SQL-T-HS` high-school · `SQL-T-UG` undergraduate · `SQL-T-GR` graduate — the depth tier of a theory item or gate (§2 rows for M1 and A8 + A9).
````

**J881** · R4-9 · anchor-rewrite

````text
| **M1** (logic, sets, proofs, counting, graphs) — *Tier SQL-T-HS/SQL-T-UG* | PQ-01 sets, relations, functions, **bags** · PQ-02 predicate logic and **3-valued logic (preview)** · counting/cardinality bounds of joins (RT-01) | SQL-Z0.1 … SQL-Z0.6 |
````

**J882** · R4-9 · anchor-rewrite

````text
| **A4** (recall) + **U2** (structures, hashing theory, complexity) | PQ-07 sorting, hashing, trees, binary search *as the raw material of access paths* · CS-02 B-tree fan-out and height arithmetic (formula only — the toy is DB-6) | SQL-Z0.7, TD-10 |
````

**J883** · R4-9 · anchor-rewrite

````text
| **A1/A2** (recall) + **M6** (units, orders of magnitude) | PQ-08 storage hierarchy, page/row arithmetic · latency numbers (recall of primer SD-37) | SQL-Z0.8 |
````

**J884** · R4-9 · anchor-rewrite

````text
| **M5** (numerical stability) | PQ-03 `numeric` vs float, rounding modes (half-up vs banker's), integer money — *recall IEEE from M5; add decimal semantics* | SQL-E2.1, SQL-E2.7 |
````

**J885** · R4-9 · anchor-rewrite

````text
| **A2** (floating point) | PQ-03 `numeric` vs float, rounding modes (half-up vs banker's), integer money — *recall IEEE from M5; add decimal semantics* | SQL-E2.1, SQL-E2.7 |
````

**J886** · R4-9 · anchor-rewrite

````text
| **A8 + A9** (+ U5) — DB theory (with the A8 SQL sessions) | RT-02 algebra · RT-03 calculus/safety (SQL-T-GR) · RT-04/05 FDs & normal forms · RT-08 rewrites · CS-05 serializability & SI · CS-06 recovery · CS-08 cardinality. **SQL-T-UG gate items** map to TD-2 (push σ through ⋈), TD-1/2/3 (keys, FDs, 3NF), TD-8 (dirty-read & lost-update schedules), TD-12 (WAL durability). **SQL-T-GR gate items** map to TD-9 (snapshot visibility), TD-13 (selectivity estimate) | TD-1 … TD-16 (as gated) |
````

**J887** · R4-9 · anchor-rewrite

````text
| **S2** HLD/LLD contract, ADR template, NFR table | DD-01 conceptual → logical → physical; **schema ADRs** ("I pick X because Y, I accept Z") · DD-12 constraints as spec | SCH-1 |
````

**J888** · R4-9 · anchor-rewrite

````text
| **S2** + primer building blocks · HLD evidence packs | DD-01 schema ADRs inside HLD packs; DD-10 denormalisation ADR; **recall** primer SD-13 … SD-19 for scale-out | SCH-2, SCH-3 |
````

**J889** · R4-9 · anchor-rewrite

````text
| **S11** case-study capstone | SQL-CAP1 – SQL-CAP4 are its database acceptance tests | SQL-CAP1 – SQL-CAP4 |
````

**J890** · R4-9 · anchor-rewrite

````text
| **S11** control-plane case study | DD-09 audit/event log design; OD-08 migrations for the control-plane store | SCH-6 |
````

**J891** · R4-9 · anchor-rewrite

````text
| ACID, CAP, consistency, big-O, hashing | **M1 / A4 + U2 / A8 + A9 / A8** | CS-05/CS-07 formal treatment of isolation and consistency models; PQ-07 recall only |
````

**J892** · R4-9 · anchor-rewrite

````text
The main course's spine is Phases 0–3 (Tracks A–D, mostly in parallel) → Phase 4 → …; the reserved M/U/S tracks are not placed yet. SQL does not first *appear* until A8, so the calendar front-loads only **cheap, unlockable prerequisites** and holds the language until A8 needs it (Prop Lock: no SQL vocabulary before it is anchored).
````

**J893** · R4-9 · anchor-rewrite

````text
| **A1–A4 + M1** (SQL-T-HS → SQL-T-UG tiers) | PQ-01, PQ-02, PQ-07, PQ-08 with SQL-Z0.1 – SQL-Z0.8 (≈ 6 short sessions) | paper fluency: sets/bags/3VL/counting/units |
````

**J894** · R4-9 · anchor-rewrite

````text
| **A3, A6, A11 + M5** | PQ-03 (types, decimals), PQ-04 (files/JSON), PQ-05 (`psql` + Docker Postgres) — the lab loads and fingerprints match (§3) | lab environment ready; no SQL semantics yet |
````

**J895** · R4-9 · anchor-rewrite

````text
| **A9 + S2** | PX-9 / DD-13 with the scale primitives; SCH-2/SCH-3 inside packs | scale primitives with SQL evidence |
````

**J896** · R4-9 · anchor-rewrite

````text
| **S11** | SQL-CAP1 – SQL-CAP4 | database acceptance |
````

**J897** · R4-9 · anchor-rewrite

````text
#### PQ-01 · Sets, relations, functions, bags — stitch: M1
````

**J898** · R4-9 · anchor-rewrite

````text
#### PQ-02 · Propositional & predicate logic; 3VL preview — stitch: M1 · DB-1
````

**J899** · R4-9 · anchor-rewrite

````text
#### PQ-03 · Types, encodings, integer money vs float — stitch: M5
````

**J900** · R4-9 · anchor-rewrite

````text
- **Theory:** Half-up vs banker rounding; IEEE recall from M5 then add decimal semantics.
````

**J901** · R4-9 · anchor-rewrite

````text
#### PQ-07 · Sorting, hashing, trees, binary search as access-path raw material — stitch: A4 + U2 · DB-6
````

**J902** · R4-9 · anchor-rewrite

````text
#### PQ-08 · Storage hierarchy & page/row arithmetic — stitch: A1/A2 recall + M6 · DB-4
````

**J903** · R4-9 · anchor-rewrite

````text
#### RT-03 · Tuple/domain calculus & safety (SQL-T-GR) — stitch: A8 + A9 + U5 · DB-3
````

**J904** · R4-9 · anchor-rewrite

````text
#### RT-06 · ER → tables — stitch: S2 · DD-01
````

**J905** · R4-9 · anchor-rewrite

````text
#### DD-01 · Conceptual → logical → physical — stitch: S2
````

**J906** · R4-9 · anchor-rewrite

````text
#### DD-03 · Money, units, time — stitch: A8 · M5
````

**J907** · R4-9 · anchor-rewrite

````text
#### DD-07 · Soft delete, audit, history — stitch: A8 · S11
````

**J908** · R4-9 · anchor-rewrite

````text
#### DD-08 · Denormalisation with ADRs — stitch: S2 · primer SD-18
````

**J909** · R4-9 · anchor-rewrite

````text
Issued one at a time with the A8 + A9 (+ U5) theory and the §4.0 slices. Keys in Appendix K (sketches).
````

**J910** · R4-9 · anchor-rewrite

````text
- **Tags:** DD-02·S2
````

**J911** · R4-9 · anchor-rewrite

````text
Database acceptance tests for the S11 case-study capstone. Issue after the §6 level-14 gate. **Predict; run; reconcile.**
````

**J1051** · R6-1 · new-content

````text
- **Core:** `INSERT…ON CONFLICT`, `UPDATE…FROM`, writable CTEs, `MERGE` (PG15+), `DELETE…RETURNING`.
````

**J1052** · R6-1 · new-content

````text
- **Theory:** Idempotency keys; batching to bound WAL/bloat.
````

**J1053** · R6-1 · anchor-rewrite

````text
| **A7** async (Pub/Sub, Tasks, Scheduler) | SL-10 idempotent writes: `INSERT … ON CONFLICT`, unique keys | SQL-E9.3 |
````

**J1054** · R6-2 · new-content

````text
- **Core:** `INSERT…ON CONFLICT`, `UPDATE…FROM`, writable CTEs, `MERGE` (PG15+), `DELETE…RETURNING`. `LISTEN channel` / `NOTIFY channel, 'payload'` (or `pg_notify(channel, payload)`) as the wake-up beside a `FOR UPDATE SKIP LOCKED` queue table or an outbox: the notification is sent when the transaction commits, and never if it rolls back.
````

**J1055** · R6-2 · new-content

````text
- **Core:** `pg_stat_statements`, auto_explain, wait events; stale analyze symptoms.
````

**J1056** · R6-2 · new-content

````text
- **Core:** Runbook literacy: schedule, retain, test restore to a *new* instance, measure RPO/RTO.
````

**J1057** · R6-2 · new-content

````text
- **Core:** Physical vs logical replication; failover; why 2PC is not the default answer (outbox owns the product pattern).
````

**J1058** · R6-2 · new-content

````text
- **Core:** Height ≈ log_fanout(n); leftmost prefix rule; LSM write amp vs B-tree read amp; GIN for JSONB/arrays; BRIN for append-mostly.
````

**J1119** · R7-2 · §0.1–§0.3 replaced by the part's own §0 (generic rules are in the course guide)

````text
## 0. Read this first — how this file complements the main course

### 0.1 Standing instruction (for Claude, every session)

**This file is a complement to the main course, not a second curriculum. Read both. Whenever a main-course module is taught, also teach every companion concept bound to it (§2) in the same session, as one story. Similar, related, and overlapping concepts are stitched together and taught in parallel — never in separate sessions, never twice.**

Why: the main course owns the order and the module spine. This file owns the engine slices DB-1 … DB-10 (§4.0) and the Cloud SQL procedure (OD-11). The main course deliberately does not own the SQL *language* end to end, the pre-SQL mathematics a learner may lack, the theory tier behind the slices (serializability, ARIES, join-cost formulas, Selinger-style planning), modelling method, analytics dialects, or a large body of query-writing practice. This file supplies exactly those, and hangs each piece on the main-course module that needs it, **at the moment that module needs it**.

### 0.2 Stitching rules

1. **One concept, one teaching.** If both files teach an idea, it is taught once, in the module that owns it (§2.1 overlap register), and the other file only *adds*. Later sessions recall in one line; they do not re-teach. Ideas already unlocked-and-confirmed on the ledger are recalled, never re-taught.
2. **Ownership split (memorise).** *Other parts own:* the Firestore, Bigtable and store-choice material (primer SD-22, SD-23, SD-25), outbox/inbox (A9 theory; design-patterns ARCH-11 shape), payment-flow abuse (cyber AB-06), billing-export SQL (B4). *This file owns:* SQL-language mastery (SL), relational theory (RT), the CS theory tier under the slices (CS), data-design method (DD) including the ledger rules (DD-03) and point-in-time correctness and leakage (DD-05), operating-a-database craft (OD) including Cloud SQL (OD-11), migrations as jobs (OD-08), the cursor pager (OD-09) and pool math (OD-03), analytics and dialect craft (AN) including BigQuery operations (AN-02), pre-SQL prerequisites (PQ), the exercise ladder (§6), and the engine slices DB-1 … DB-10 and their toys (§4.0). **Where a §4.0 slice toy exists (WAL codec, slotted page, B-tree, iterator executor, visibility simulator) this file never asks for a second toy — it adds the analytic layer (formulas, schedules, cost models) that the toy's tests do not reach.**
3. **Same ten-rung ramp, same locks.** Companion concepts are taught through the suite's ten-rung sequence (rule 0.4.3, §0.6) (anchor → vocabulary → representation → core move → worked illustration → basic unseen check → routine variation → mixed transfer → top-rung challenge → reflection + ledger). The **dependency gate**, **rung-2 vocabulary audit** and **Prop Lock** apply unchanged: never use a later system as a prop (no Spanner interleaving in the first Postgres transcript; no full PITR runbook before its owner; no Cloud SQL HA as a "known" prop before its OD-11 session). If an exercise needs machinery not yet unlocked, **postpone the exercise** — or teach the machinery first. A smuggled prop is an *instructor process failure*, never "shaky", exactly as in rule 0.4.6 (§0.6).
4. **Every concept gets a GCP lens the moment it is taught**, at three depths (same definitions as the primer companion): **Lens-1** name the GCP resource and show one `gcloud`/console/Terraform line; **Lens-2** touch it (local Docker Postgres is the default lab; Cloud SQL / AlloyDB / Spanner emulator / BigQuery sandbox only when Lab Reality allows); **Lens-3** cert-depth trade-offs and limits (PCA storage systems; Professional Data Engineer / Database Engineer overlap).
5. **Bank ≠ dump.** The exercise ladder in §6 is a **bank of specifications**, not a worksheet. At teach time issue **one** item at the rung the ledger says is next (never the whole list), let the learner attempt first, escalate hints one notch at a time (*what structure do you see → smaller case → smallest unlocked hint*), and only then open the instructor key (Appendix K). **Never paste a key before an attempt.** Mixed-transfer items name their two earlier tools on one line before executing.
6. **Predict before you run; explain the discrepancy after.** Every exercise that has a *result shape*, a *row count*, a *plan shape*, or an *isolation outcome* starts with the learner writing the prediction (one line). Then run. A wrong prediction is the best teaching moment in this file — record the discrepancy on the ledger, do not skip it. (Rule 0.4.4 in §0.6: predict → run → discrepancy.)
7. **Fingerprints, not eyeballs.** Each read-only exercise has a *golden*: `rows:hash` computed by the lab kit (`lab.chk`). Two queries are the same answer iff their fingerprints match. **Goldens are valid only for seed v1 on PostgreSQL 15.x with `timezone = UTC` and the `C` collation** — if any of those change, regenerate; do not "fix" a learner's query to match a stale golden.
8. **Tracking is inline.** Tick `- [ ]` boxes in this file or say "done" in chat. Do **not** create a separate tracker; the tutor's progress ledger (§0.6) records unlocked / shaky / postponed for companion modules under their IDs (`SL-08`, `SQL-E6.2`…).
9. **Honesty flags.** `(verify)` = a GCP or PostgreSQL-version detail that changes often or that I could not confirm here — check live docs before relying on it for an exam or production. **Modern note** marks where industry has moved past a textbook.
10. **Time, money and secrets.** Labs are free-tier/credits-safe: local Postgres in Docker is the default; Cloud SQL / AlloyDB / Memorystore are credits-optional and *destroyed the same day* (Lab Safety, §0.6). Never put a password, key or real customer data in a query, a prompt or this file; the lab data is synthetic.
11. **User can override anything:** skip a concept already known (run its skip-test; §5 tiers), jump to an exercise, or go hands-on — same rights as rule 0.4.1 (§0.6). **On a conflict:** the main course wins on order, Lab Reality, exam time-sensitivity and the ledger; this file wins on SQL/DB content and exercise specs.
12. **Read economically.** Each session read §0 and §2, then only the blocks bound to today's main-course module (search by ID: `SL-06`, `CS-05`, `SQL-E4.5`…). Do not reload the whole file. Appendix K (keys) is opened *only after* an attempt.

### 0.3 How one stitched session runs

1. **Anchor** — announce the main-course module and list the companion modules bound to it (§2). Run the one-line pre-rung-2 self-check: every term to be used is anchored this session or on the ledger; no unanchored sibling; no new product; every noun in the picture unlocked.
2. **Concept** — teach the shared idea once (main-course depth), then layer this file's SQL / theory / craft on top. Derive before you name.
3. **GCP lens** — the resource(s): Lens-1 always, Lens-2 when Lab Reality allows.
4. **Numbers** — one back-of-the-envelope estimate (rows per page, index height, pool arithmetic, bytes scanned).
5. **Exercise** — issue **one** item from §6/§7 at the current rung (prediction first). For a mixed-transfer item, name the new idea plus exactly two earlier unlocked ideas.
6. **Check** — the module's check questions; the learner answers before you explain. An unseen check that uses unanchored terms is invalid — fix the check, don't mark the learner shaky.
7. **Close** — tick boxes in both files' sense; ledger line: what unlocked, what is shaky, what is postponed.

When other companions bind to the same session, the Suite Session Protocol (rule 0.4.2 in §0.6) governs.

````

**J1120** · R7-2 · anchor-rewrite

````text
### 0.4 Notation
````

**J1121** · R7-2 · copied preferences, contract and Lab Safety moved out

````text
### 0.5 Learner teaching preferences (binding)

- **Check questions must be woven into the concept explanation itself**, not asked as separate "what do you already know" diagnostics — the learner explicitly opted out of background-probing questions and asked for calibration to happen through how they handle the material.
- **"Maintain curriculum depth and academic rigour"** has been repeated multiple times as an explicit standing instruction — do not compress, simplify, or skip the "why," even under time pressure or a fast pace of correct answers.
- When companion-file content (system-design-primer, SQL, design-patterns) overlaps a main-course module, **teach it once, stitched into the same session** — never as a separate pass, per each companion's own §0.2 stitching rules.
- If a companion file references module IDs that don't exist in the main course (as the SQL companion's did before its IDs were rebound), **say so plainly rather than forcing a silent, possibly-wrong mapping** — this was well received when done for the SQL companion.

### 0.6 Suite Teaching Contract and Lab Safety (same text in every part)

The main course's §0.4 and §0.5, copied whole so that this companion can be taught on its own terms. The rule numbers stay the main course's (0.4.1…0.4.10, and the five Lab Safety rules), so "main course §0.4.3" and rule 0.4.3 here are the same rule. The **progress ledger** named below is the tutor's running record beside the inline boxes (main course §0.1): each ID's mastery state, the misconception register, the errata list, the recorded overrides and wrong predictions, and the exact resume point. The inline `- [ ]` boxes stay authoritative.

**Suite Teaching Contract (main course §0.4).**

One contract for every part; each companion carries the same contract in its own §0 and adds its session detail. When two rules conflict, the higher one wins: (1) the learner's explicit instruction in the current chat · (2) the learner teaching preferences (§0.5 here) · (3) the main course on order, cert timing and Lab Reality · (4) the owning part on its content (main course §0.3) · (5) the companions' defaults.

**0.4.1 Rhythm.**

- One concept per turn, at full depth. New material is taught by direct explanation; procedures by worked, parallel examples.
- Every turn carries exactly one focused question, embedded in the teaching. Diagnosis happens through those checks; there is no separate probing (the learner preferences in §0.5 rule out separate calibrating questions). A turn may be as long as one concept needs.
- Correction style: confirm the correct part explicitly, then sharpen the imprecise part by naming the exact mechanism. No false praise. Hold the line under "just tell me"; give a foothold when the learner is genuinely stuck.
- Overrides: the learner may skip (after passing the skip-test), jump, or go hands-on. Every override is recorded in the ledger so the prerequisite check can flag what was skipped.

**0.4.2 Suite Session Protocol.** When several files bind to one module, the session runs:

1. **Anchor** — list the bound IDs from *all* files (each companion's §2).
2. **Concept** — taught once, by the owner in main course §0.3.
3. **Layers**, in fixed order: system design (primer) → SQL/engine → patterns → Go implementation (Go companion) → attacker/crypto (cyber).
4. **GCP lens.**
5. **One Numbers step** for the whole session.
6. **One application item**: a primer micro-problem *or* a companion exercise card, never both for the same concept.
7. **Checks**, woven in per §0.5.
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

**0.4.10 Academic depth (undergraduate prerequisites).** The course teaches every undergraduate prerequisite of cloud and system architecture at the depth of a university course, not only at the engineering depth of a first pass. Each module of Tracks A to D, and each companion, carries an **academic pass**: formal definitions, theorems with their proofs or proof sketches, derivations, named readings, and a numbered problem set whose written keys (an expected answer and at least one expected wrong answer, rule 0.4.7) sit in the owning part's keys. The University and textbook alignment table (main course §0.6) says which university courses and textbooks each pass is aligned with. Four rules:

1. **Two passes, one module.** The engineering pass comes first. The academic pass follows under the same module ID, as its own teaching blocks (rule 0.4.8), never as a separate course. A "first-pass scope" note limits the first pass only.
2. **Proof standard.** A claim presented as a theorem is proved in the session, set as a proof problem, or labelled "stated without proof", naming where the proof is found. Derivations show every step, and every number is computed, not asserted.
3. **Problem sets are exercises.** They climb the ramp (rule 0.4.3). An academic block is `mastered` only when at least one proof (or derivation) problem and one computational problem in it pass against their keys (this tightens rule 0.4.5 for academic blocks), so every block's problem set carries both kinds. In the main course the block is a module's academic pass (its D lines and its problem set); in a companion it is the companion's academic pass.
4. **Readings are named, not linked.** A text is cited by author, title and edition; a course by institution and course name. Editions and course numbers change, so the alignment table carries its check date, and anything not checked carries `(verify)`.

**Lab Safety (main course §0.5).**

One rule set for every file; it unifies the cybersecurity companion's rule 10, the SQL companion's rule 10 and the main course's Lab Reality paragraph.

1. **Hard bans:** no scanning of third parties; no malware; no live DDoS; no credential stuffing against real accounts; fixtures on localhost or disposable projects only; crypto through vetted libraries only.
2. **Money and time:** local first (Docker Postgres, local fixtures). Credit-using services are created for one lab and destroyed the same day, with a budget alert set before the first apply.
3. **Secrets and data:** never put a password, key or real customer data in a query, a prompt or a course file. Lab data is synthetic.
4. **The workplace console is read-only:** look, never create or change.
5. **Every lab carries a Lab Reality tag:** `[free-tier]` · `[credit ~$X]` · `[plan-only]` · `[paper]` · `[local]`.
````

**J1122** · R7-3 · overlap-register slice moved to rule 0.3

````text
### 2.1 Overlap register — concepts that appear in both files (teach once, in the owner)

> **Note:** the suite-wide register is the main course §0.3; this table is the SQL slice of it, and on a conflict the main course's register wins. DB-1 … DB-10 are owned by this file (§4.0).

| Concept | Owner (teach here) | This file adds |
|---|---|---|
| Relational algebra, 3VL (DB-1) | **§4.0 DB-1** (this file; A8) (toy: bag relations + truth-table tests) | RT-02 set-vs-bag laws and rewrite equivalences; RT-03 calculus/safety; SL-03 NULL semantics across every clause; SQL-Z0.4, TD-5/6 |
| Catalog, tuples, constraints (DB-2) | **§4.0 DB-2** | SL-01 type system & constraint catalogue; DD-04 key strategies; DD-12; SQL-E10 constraint batteries |
| CTEs, windows, lateral (DB-3) | **§4.0 DB-3** | SL-06/08/09 full semantics (frames, EXCLUDE, RANGE with intervals, recursion termination); SQL-E4–SQL-E7 ladder |
| Heap pages & TOAST (DB-4) | **§4.0 DB-4** (toy: slotted page) | CS-01 page/row arithmetic and fill-factor maths (no second toy) |
| Buffer pool (DB-5) | **§4.0 DB-5** (toy: clock sweep) | CS-04 hit-ratio and working-set reasoning, why sequential flooding needs scan-resistance |
| Indexes (DB-6) | **§4.0 DB-6** (toy: B-tree + inverted index) | CS-02 height/fan-out/cost formulas; OD-01 index-design workflow; PX-1 … PX-6 |
| Executor & spill (DB-7) | **§4.0 DB-7** (toy: iterators, forced spill) | CS-03 I/O cost formulas (block-NL, Grace hash, sort-merge), TD-11; PX-7, PX-10 |
| Planner statistics (DB-8) | **§4.0 DB-8** (toy: histogram + MCV) | CS-08 Selinger DP, estimation error propagation, TD-13; PX-8 |
| MVCC, locks, vacuum (DB-9) | **§4.0 DB-9** (toy: visibility simulator, deadlock detector) | CS-05 schedule theory (precedence graphs, 2PL, SSI); TD-8/9; TX-1 … TX-8 |
| WAL, replica, PITR (DB-10) | **§4.0 DB-10** (toy: mini-WAL) | CS-06 ARIES and steal/no-force reasoning; TD-12; OD-04 restore-drill runbook |
| Cloud SQL provisioning, Auth Proxy, private IP, HA, flags | **OD-11** | OD-03/04/05 SQL-side consequences (session state vs pooler modes, RPO/RTO arithmetic, replica lag); §8.2 Terraform |
| Migrations as jobs, expand/contract | **OD-08** (jobs) + **DD-11** (expand/contract) | DD-11 *lock levels*, `NOT VALID` + `VALIDATE`, `CREATE INDEX CONCURRENTLY`, backfill batching (SQL-E9.6) |
| Spanner, Bigtable, Firestore map | **Primer SD-22 / SD-23 / SD-25** | AN-05, AN-06 same-question comparisons; DD-13 key design as SQL |
| Cursor pagination | **OD-09** (seek predicate, index, from-scratch pager) | PX-9 measured against OFFSET |
| Hot partition, key histogram | **DD-13** (key histogram) + primer SD-23 (row keys) | DD-13 the skew query on lab data (user 1 = 135 orders; see PX-1) |
| Connection-pool math | **OD-03** (worksheet) | OD-03 pooler modes (session/transaction/statement) and what breaks in transaction mode |
| RLS multi-tenancy | **A8** + DD-09 (design) | SL-13 policy syntax, `FORCE`, owner bypass; SQL-E10.2 composite FK as defence in depth; SQL-E10.6 |
| Outbox / inbox, idempotency | **A9 / A7** (main course §0.3: 2PC/Saga/outbox) | SL-10 the SQL that makes them true (unique index, `ON CONFLICT`, `SKIP LOCKED`); TX-5, SQL-E9.3 |
| Ledger, minor-unit ints | **DD-03** (ledger rules) | DD-05 modelling; SQL-E4.5/SQL-CAP2 revenue reconciliation; SQL-CAP1 invariants |
| BigQuery partition/cluster/cost | **AN-02** (cost and operations) | DT drills |
| As-of / point-in-time join | **DD-05** (leakage; D3) | SQL-E6.4 / SQL-E13.4 / SQL-E13.5 the SQL shapes (lateral, range join, SCD2) |
| Billing-export SQL patterns | **B4** | AN-03 reused windows; no new concept |
| SQL scale-out (replication, federation, sharding, denormalisation, SQL tuning) | **primer companion SD-13 … SD-19** | *this file never re-teaches them*; CS-07/DD-13/OD-05/OD-07 add engine-level and SQL-level detail only |
| ACID, CAP, consistency, big-O, hashing | **A2 / A4 / A8 + A9 / A8** | CS-05/CS-07 formal treatment of isolation and consistency models; PQ-07 recall only |
````

**J1136** · R7-4 · anchor-rewrite

````text
Each main-course module on the left is taught **with** the companion modules on the right, in the same session (§0.2 rule 1). "Checkpoint" is the exercise (or drill) to run once that module and its stitched concepts are done — issued **one at a time**, per rule 5.
````

**J1137** · R7-4 · anchor-rewrite

````text
Local PostgreSQL 15.x database `labdb` with schema `lab` (the storefront OLTP data of §0.4) plus `work` (scratch) and fingerprint functions `lab.chk` / `lab.chk_o`. Every kit file is printed in full in §3.8: the schema `lab_schema.sql`, the seed `lab_seed.sql`, the runners `run_ex.py`, `plans.py`, `tx_tests.py`, and the rest.
````

**J1138** · R7-4 · anchor-rewrite

````text
Cloud SQL / AlloyDB: same SQL; create an instance only when Lab Reality allows and **destroy the same day** (Lab Safety, §0.6). Auth Proxy for IAM DB auth when OD-11 is unlocked — not required for local goldens.
````

**J1139** · R7-4 · anchor-rewrite

````text
**Bank ≠ dump** (§0.2 rule 5): issue **one** item at the ledger rung; learner attempts; escalate hints; only then Appendix K. Every read-only golden below is from `goldens_ex_*.json` executed on PostgreSQL 15.8 / seed v1 / UTC / C collation.
````

**J1140** · R7-4 · anchor-rewrite

````text
### 2.2 A8 slice pairing — the engine slices DB-1 … DB-10 and what rides with each
````

**J1141** · R7-4 · anchor-rewrite

````text
### 2.3 Parallel calendar — how the companion rides the main course's spine
````

**J1142** · R7-4 · anchor-rewrite

````text
| **A8 — SQL design track** (concept, then lab; engine slices §4.0) | **The core binding.** SL-01 … SL-12 · RT-01 … RT-07 · DD-01 … DD-06, DD-12 · OD-01 · CS-01 … CS-08 — paired slice by slice with DB-1 … DB-10 (§2.2 table below) | SQL-E1 → SQL-E10 by level (§6 gates); BH-1 after SQL-E3.5 |
````

**J1143** · R7-4 · anchor-rewrite

````text
*The engine slices.* This file **owns** the slices DB-1 … DB-10; main course A8 points here, and each slice is taught as one session with the companion theory paired to it in §2.2. The Cloud SQL procedure they map onto is OD-11.
````

**J1144** · R7-4 · anchor-rewrite

````text
| **SQL-SKIP-SQL** SQL & relational correctness (`DB-SQL`) | **Skip-test map:** if the A8 sessions confirmed FDs/joins/transactions/pagination/client hygiene, stamp using SQL-E3.2, SQL-E4.5, SQL-E5.4, SQL-E9.3, TX-2. **Else** run the SQL-SKIP-SQL order = RT-01/04/05 → RT-02 → SL-01/02 → SL-03 → SL-04 → SL-05 → SL-06/09 → SL-08 → TX labs → OD-09 (§2.3 table) | see §2.3 |
````

**J1145** · R7-4 · anchor-rewrite

````text
| **SQL-SKIP-ENGINE** PostgreSQL internals (`DB-ENGINE`) | **Skip-test map:** residual `EXPLAIN` drills = PX-1 … PX-11; crash/recovery evidence = TD-12 + OD-04 drill. **Else** run the SQL-SKIP-ENGINE order = CS-01 → CS-04 → CS-02 → CS-03 → CS-08 → CS-05 → CS-06 → CS-07 (§2.3) | see §2.3 |
````

**J1146** · R7-4 · anchor-rewrite

````text
Mapped to the A8 skip-tests **SQL-SKIP-SQL** / **SQL-SKIP-ENGINE**. If the A8 sessions already confirmed the skill, **stamp and skip**; else run the order in §2.3.
````

**J1155** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** matching PQ unlocked
````

**J1156** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** matching PQ unlocked
````

**J1157** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** matching PQ unlocked
````

**J1158** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** matching PQ unlocked
````

**J1159** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** matching PQ unlocked
````

**J1160** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** matching PQ unlocked
````

**J1161** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** matching PQ unlocked
````

**J1162** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** matching PQ unlocked
````

**J1163** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 1 gate above; stitch partners from §2 as tagged
````

**J1164** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 1 gate above; stitch partners from §2 as tagged
````

**J1165** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 1 gate above; stitch partners from §2 as tagged
````

**J1166** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 1 gate above; stitch partners from §2 as tagged
````

**J1167** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 1 gate above; stitch partners from §2 as tagged
````

**J1168** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 1 gate above; stitch partners from §2 as tagged
````

**J1169** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 1 gate above; stitch partners from §2 as tagged
````

**J1170** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 1 gate above; stitch partners from §2 as tagged
````

**J1171** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 2 gate above; stitch partners from §2 as tagged
````

**J1172** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 2 gate above; stitch partners from §2 as tagged
````

**J1173** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 2 gate above; stitch partners from §2 as tagged
````

**J1174** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 2 gate above; stitch partners from §2 as tagged
````

**J1175** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 2 gate above; stitch partners from §2 as tagged
````

**J1176** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 2 gate above; stitch partners from §2 as tagged
````

**J1177** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 2 gate above; stitch partners from §2 as tagged
````

**J1178** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 2 gate above; stitch partners from §2 as tagged
````

**J1179** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 3 gate above; stitch partners from §2 as tagged
````

**J1180** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 3 gate above; stitch partners from §2 as tagged
````

**J1181** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 3 gate above; stitch partners from §2 as tagged
````

**J1182** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 3 gate above; stitch partners from §2 as tagged
````

**J1183** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 3 gate above; stitch partners from §2 as tagged
````

**J1184** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 3 gate above; stitch partners from §2 as tagged
````

**J1185** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 3 gate above; stitch partners from §2 as tagged
````

**J1186** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 3 gate above; stitch partners from §2 as tagged
````

**J1187** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 3 gate above; stitch partners from §2 as tagged
````

**J1188** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 3 gate above; stitch partners from §2 as tagged
````

**J1189** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 4 gate above; stitch partners from §2 as tagged
````

**J1190** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 4 gate above; stitch partners from §2 as tagged
````

**J1191** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 4 gate above; stitch partners from §2 as tagged
````

**J1192** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 4 gate above; stitch partners from §2 as tagged
````

**J1193** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 4 gate above; stitch partners from §2 as tagged
````

**J1194** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 4 gate above; stitch partners from §2 as tagged
````

**J1195** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 4 gate above; stitch partners from §2 as tagged
````

**J1196** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 4 gate above; stitch partners from §2 as tagged
````

**J1197** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 5 gate above; stitch partners from §2 as tagged
````

**J1198** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 5 gate above; stitch partners from §2 as tagged
````

**J1199** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 5 gate above; stitch partners from §2 as tagged
````

**J1200** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 5 gate above; stitch partners from §2 as tagged
````

**J1201** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 5 gate above; stitch partners from §2 as tagged
````

**J1202** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 5 gate above; stitch partners from §2 as tagged
````

**J1203** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 5 gate above; stitch partners from §2 as tagged
````

**J1204** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 5 gate above; stitch partners from §2 as tagged
````

**J1205** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 6 gate above; stitch partners from §2 as tagged
````

**J1206** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 6 gate above; stitch partners from §2 as tagged
````

**J1207** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 6 gate above; stitch partners from §2 as tagged
````

**J1208** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 6 gate above; stitch partners from §2 as tagged
````

**J1209** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 6 gate above; stitch partners from §2 as tagged
````

**J1210** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 6 gate above; stitch partners from §2 as tagged
````

**J1211** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 6 gate above; stitch partners from §2 as tagged
````

**J1212** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 7 gate above; stitch partners from §2 as tagged
````

**J1213** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 7 gate above; stitch partners from §2 as tagged
````

**J1214** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 7 gate above; stitch partners from §2 as tagged
````

**J1215** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 7 gate above; stitch partners from §2 as tagged
````

**J1216** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 7 gate above; stitch partners from §2 as tagged
````

**J1217** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 8 gate above; stitch partners from §2 as tagged
````

**J1218** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 8 gate above; stitch partners from §2 as tagged
````

**J1219** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 8 gate above; stitch partners from §2 as tagged
````

**J1220** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 8 gate above; stitch partners from §2 as tagged
````

**J1221** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 8 gate above; stitch partners from §2 as tagged
````

**J1222** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 8 gate above; stitch partners from §2 as tagged
````

**J1223** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 8 gate above; stitch partners from §2 as tagged
````

**J1224** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 8 gate above; stitch partners from §2 as tagged
````

**J1225** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 8 gate above; stitch partners from §2 as tagged
````

**J1226** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 8 gate above; stitch partners from §2 as tagged
````

**J1227** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 9 gate above; stitch partners from §2 as tagged
````

**J1228** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 9 gate above; stitch partners from §2 as tagged
````

**J1229** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 9 gate above; stitch partners from §2 as tagged
````

**J1230** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 9 gate above; stitch partners from §2 as tagged
````

**J1231** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 9 gate above; stitch partners from §2 as tagged
````

**J1232** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 9 gate above; stitch partners from §2 as tagged
````

**J1233** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 9 gate above; stitch partners from §2 as tagged
````

**J1234** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 10 gate above; stitch partners from §2 as tagged
````

**J1235** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 10 gate above; stitch partners from §2 as tagged
````

**J1236** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 10 gate above; stitch partners from §2 as tagged
````

**J1237** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 10 gate above; stitch partners from §2 as tagged
````

**J1238** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 10 gate above; stitch partners from §2 as tagged
````

**J1239** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 10 gate above; stitch partners from §2 as tagged
````

**J1240** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 13 gate above; stitch partners from §2 as tagged
````

**J1241** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 13 gate above; stitch partners from §2 as tagged
````

**J1242** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 13 gate above; stitch partners from §2 as tagged
````

**J1243** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 13 gate above; stitch partners from §2 as tagged
````

**J1244** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 13 gate above; stitch partners from §2 as tagged
````

**J1245** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 14 gate above; stitch partners from §2 as tagged
````

**J1246** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 14 gate above; stitch partners from §2 as tagged
````

**J1247** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 14 gate above; stitch partners from §2 as tagged
````

**J1248** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 14 gate above; stitch partners from §2 as tagged
````

**J1249** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 14 gate above; stitch partners from §2 as tagged
````

**J1250** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 14 gate above; stitch partners from §2 as tagged
````

**J1251** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 14 gate above; stitch partners from §2 as tagged
````

**J1252** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 14 gate above; stitch partners from §2 as tagged
````

**J1253** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 14 gate above; stitch partners from §2 as tagged
````

**J1254** · R7-6 · line moved out of the course file

````text
- **Prereq gate:** Level 14 gate above; stitch partners from §2 as tagged
````

**J1255** · R7-6 · new-content

````text
**Bank ≠ dump** (rule 0.4.11): issue **one** item at the ledger rung; learner attempts; escalate hints; only then Appendix K. Every read-only golden below is from `goldens_ex_*.json` executed on PostgreSQL 15.8 / seed v1 / UTC / C collation.
````
