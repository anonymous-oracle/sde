# Part 12 · Databases, SQL, Relational Theory & Data Modelling · TOPIC LIST

Rules and directives for this part: `index/part12_databases.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Databases, SQL, Relational Theory & Data Modelling

### Pre-SQL foundations

- Relations as sets of tuples over a heading; SQL tables as bags; Cartesian product sizes; bag versus set union
- Three-valued logic: TRUE, FALSE, UNKNOWN; why `= NULL` never matches
- Types and encodings: minor-unit money, never floats; UTF-8, byte-order marks, `char(n)` padding; half-up versus banker's rounding
- Files for loading: CSV NULL versus empty string, JSON versus JSONL, `COPY` options, CRLF traps
- Tooling: `psql` meta-commands and `ON_ERROR_STOP`, Postgres in Docker with volumes and health checks, session time zone and collation
- Driver hygiene: parameter binding (injection as a binding failure), transactions on the connection, cursor hygiene
- Page arithmetic: 8 KiB pages, rows per page, fill factor

### Relational theory

- **The relational model**
  - Headings, bodies, candidate, primary and foreign keys; superkeys
  - Entity and referential integrity; NULLs and uniqueness
- **Relational algebra**
  - Selection, projection, product, union and difference; join, intersection and division
  - Set and bag semantics; why bag projection is not idempotent
  - Equivalence and rewrite rules: selection and projection pushdown, join commutativity and associativity; outer-join rewrites that are not legal
- **Relational calculus**
  - Tuple and domain calculus; safety and the active domain
  - Codd's theorem: algebra and safe calculus are equally expressive; relational completeness
- **Functional dependencies**
  - X → Y; Armstrong's axioms with soundness and completeness; derived rules
  - Attribute closure and its correctness; membership testing; candidate keys
  - Canonical (minimal) covers
- **Normalization**
  - 1NF, 2NF, 3NF and BCNF
  - Lossless-join decomposition (the binary test and the chase) and dependency preservation
  - BCNF decomposition versus 3NF synthesis; when BCNF loses a dependency
  - Multivalued dependencies and 4NF; join dependencies and 5NF
- **Integrity as specification**
  - CHECK, UNIQUE, FOREIGN KEY, EXCLUDE and deferrable constraints as the executable spec
  - `NOT VALID` then `VALIDATE`
- **Expressiveness**
  - First-order queries cannot express transitive closure
  - Datalog: least fixpoints, naive and semi-naive evaluation, stratified negation
  - `WITH RECURSIVE` as linear Datalog; termination

### The SQL language

- **DDL**: tables; types (`int`, `bigint`, `numeric`, `text`, `timestamptz`, `jsonb`, ranges, UUID); identity versus serial; domains; collations
- **Logical evaluation order**: FROM → WHERE → GROUP BY → HAVING → WINDOW → SELECT → DISTINCT → ORDER BY → LIMIT; alias visibility; LATERAL as left-to-right correlation
- **NULL handling**: `IS NULL`, `IS DISTINCT FROM`, `COALESCE`, `NULLIF`; aggregates skipping NULLs; CHECK treating UNKNOWN as pass
- **Joins**: inner, outer, cross, self, semi, anti, lateral, non-equi and range joins; fan-out when joining one-to-many
- **Aggregation**: `COUNT(*)` versus `COUNT(col)` versus `COUNT(DISTINCT)`; `FILTER`; `GROUPING SETS`, `ROLLUP`, `CUBE`; ordered-set aggregates
- **Subqueries**: scalar, `IN`, `EXISTS`, `ALL`/`ANY` (and `= ALL` over empty); correlated versus uncorrelated; relational division
- **Set operations**: `UNION`, `INTERSECT`, `EXCEPT` with and without `ALL`
- **Window functions**: `ROW_NUMBER`, `RANK`, `DENSE_RANK`; aggregates over frames; `ROWS` versus `RANGE`; default frames and `last_value`; running balances; gaps and islands
- **CTEs and recursion**: `WITH`, `WITH RECURSIVE`, working tables, cycle detection, `SEARCH` and `CYCLE` clauses; inlined versus materialized CTEs
- **DML**: `INSERT … ON CONFLICT`, `UPDATE … FROM`, writable CTEs, `MERGE`, `RETURNING`; savepoints; batching to bound WAL and bloat
- **Job queues in SQL**: `FOR UPDATE SKIP LOCKED` job claims; `LISTEN`/`NOTIFY` as transactional, non-durable hints
- **Views and server-side code**: updatable views; materialized views and refresh; functions; `SECURITY DEFINER` hazards; triggers used sparingly
- **Dates, JSON and text**: `timestamptz`, `AT TIME ZONE`, `date_trunc`, DST pitfalls; JSONB operators and JSON path; `LIKE` and regular expressions
- **Security in SQL**: roles and privileges, least privilege, row-level security with `FORCE`, owner bypass, column encryption with `pgcrypto`
- **Dialects**: ISO SQL versus vendor extensions; `LIMIT`/`TOP`/`FETCH`; upsert shapes; Oracle's NULL-equals-empty-string; GoogleSQL in BigQuery and Spanner

### Storage and access methods

- **Storage layout**
  - Heap pages, line pointers and tuple headers; alignment; TOAST for oversized values
  - Relation forks, the free-space map and the visibility map; segment files
  - Slotted pages: insert, delete, compact
  - HOT updates and fill factor
- **The buffer pool**
  - Hit ratio versus working set; sequential flooding and scan resistance
  - Clock-sweep eviction, pins and reference counts
  - The background writer and the checkpointer
- **Indexes**
  - B+ trees: height ⌈log_F N⌉, splits and merges, leaf chains; Lehman–Yao right links
  - Hash indexes: static, extendible and linear hashing
  - LSM trees: memtables (skip lists), SSTables, leveled versus tiered compaction, Bloom filters per run; read, write and space amplification (the RUM conjecture)
  - Bitmap indexes and bitmap scans; GIN for JSONB, arrays and text; GiST and SP-GiST; BRIN for append-mostly data
  - Composite indexes and the leftmost-prefix rule; partial indexes; covering indexes with `INCLUDE`; index-only scans
  - Index selection as an NP-hard optimization; write amplification from too many indexes

### Query processing

- **Execution**
  - The Volcano iterator model
  - Nested-loop, block nested-loop, index nested-loop, sort–merge and (Grace) hash joins
  - External merge sort: 2N · (1 + ⌈log_{B−1}⌈N/B⌉⌉) I/Os; two passes when N ≤ B(B − 1)
  - Aggregation by sorting or hashing; `work_mem` and spills to temporary files
  - Columnar and vectorized execution: late materialization, SIMD-friendly operators, run-length and dictionary compression
  - Parallel query
- **Query optimization**
  - The parse, analyse, rewrite and plan pipeline
  - Statistics: histograms, most-common values, correlation; selectivity under uniformity and independence; extended statistics on correlated columns (`CREATE STATISTICS`); compounding estimation error
  - The Selinger optimizer: dynamic programming over subsets, left-deep plans, interesting orders
  - NP-hardness of join ordering; genetic search beyond a threshold
  - Cost variables such as `random_page_cost`
- **The tuning workflow**
  - Benchmark and profile before optimizing
  - Hypothesis → `EXPLAIN (ANALYZE, BUFFERS)` → change one thing → re-measure; sargable predicates
  - Predicting plan shapes, row estimates and buffer hits before measuring
  - Schema-level tuning: column types, keeping blobs out of rows, dropping and rebuilding indexes for bulk loads

### Transactions and concurrency control

- ACID: atomicity, consistency, isolation, durability
- Schedules, conflicts and conflict serializability; the precedence-graph theorem; view serializability (NP-complete to test)
- Two-phase locking and strict 2PL; recoverable and cascadeless schedules
- Deadlocks: waits-for graph detection; wait-die and wound-wait prevention
- Timestamp ordering and the Thomas write rule
- MVCC: tuple versioning, snapshots, visibility rules, the commit log
- Isolation levels: read committed, repeatable read, serializable; dirty reads, non-repeatable reads, phantoms, lost updates and write skew
- Snapshot isolation and serializable snapshot isolation (dangerous structures)
- Critiques of the ANSI isolation definitions; Adya's graph-based definitions
- Row and table locks; lightweight versus heavyweight locks
- Vacuum: dead tuples, autovacuum, bloat, transaction-ID wraparound and freezing; long transactions as vacuum poison

### Recovery and replication

- Buffer policies: steal and no-force, and why they require undo and redo
- The write-ahead-logging rule
- ARIES: LSNs, pageLSN, dirty-page and transaction tables, analysis, redo and undo passes, compensation log records
- Checkpoints; full-page writes; synchronous commit
- Physical streaming replication and WAL archiving; point-in-time recovery
- Logical replication: publications, subscriptions, decoding across major versions
- Change data capture through replication slots, and the disk risk of a dead consumer
- Replica lag as an SLI; read-your-writes through sticky sessions or primary reads; failover caveats
- Two-phase commit in databases: prepared transactions holding locks
- External consistency with TrueTime and commit-wait
- Deterministic databases (Calvin)

### Data modelling and design

- Conceptual → logical → physical design; ER diagrams; weak entities; ISA hierarchies; foreign-key placement for 1:N and N:M
- Keys: natural, surrogate, UUID (random versus time-ordered), snowflake IDs; client versus database generation
- Money, units and time: integer minor units with explicit currency; `timestamptz` for instants; `date` for civil dates
- Hierarchies and graphs: adjacency lists, closure tables, path enumeration, nested sets
- Temporal data: valid time versus transaction time; slowly changing dimensions (type 2); as-of joins; preventing label leakage in feature queries
- JSONB versus columns, and the hybrid
- Soft delete, history tables, append-only audit; partial unique indexes
- Denormalization: trading write cost for reads; cache columns, aggregate tables, counters; refresh rules recorded in decision records
- Multi-tenancy: shared tables with `tenant_id`, schema or database per tenant; composite foreign keys; RLS as defence in depth; hot tenants
- Partitioning: range, list and hash; pruning; shard keys as locality keys; hot-key skew and sequential hotspots
- Schema evolution by expand and contract: add nullable, backfill, constrain, switch reads, drop; lock levels; concurrent index creation
- Data quality as constraints; deferral for cyclic foreign keys; EXCLUDE for ranges

### Operating databases

- Slow-query observability: `pg_stat_statements`, `auto_explain`, wait events; live triage with `pg_stat_activity`, `pg_blocking_pids`, cancel and terminate; idle-in-transaction sessions
- Connection pooling: session, transaction and statement modes and what transaction mode breaks; pool math (instances × pool ≤ `max_connections` minus reserved slots, with failover headroom)
- Backups: logical (`pg_dump`/`pg_restore`) versus physical with WAL archiving; restore drills to a new instance; RPO and RTO; HA and replicas are not backups
- Retention: dropping partitions versus mass deletes; cold-storage export
- Migrations as jobs: dirty state, advisory locks, expand/contract in CI, rollback plans; online index builds with `CREATE INDEX CONCURRENTLY` and lock timeouts on DDL
- Application data access: N+1 queries, ORM pitfalls, prepared statements, transaction boundaries, keyset pagination with unique tiebreakers and signed cursors, repositories
- Testing SQL: Postgres service containers, seeded fixtures, fingerprint and golden assertions, migration up and down tests
- Managed relational databases: provisioning, private connectivity, connectors and proxies, IAM database authentication, backups and PITR, HA standbys and read replicas, flags

### NoSQL and choosing a store

- BASE versus ACID; the modern reality of multi-item transactions in NoSQL stores
- Key-value stores: hash-table abstraction, ordered keys for range scans, caches
- Document stores: collections, flexible fields, queries over structure; joins in application code
- Wide-column stores: column families, timestamps and versions, row-key design, salting, garbage-collection policies
- Graph databases: nodes and edges for many-to-many data; sharding difficulty; adjacency lists in other stores
- NoSQL query models versus SQL: access patterns first; joins as application fan-out; outboxes instead of dual writes
- SQL or NoSQL: structured, relational, transactional data versus semi-structured, high-volume, high-IOPS data; polyglot persistence; anti-choices (a cache as the system of record, a warehouse on the checkout path, object or file storage as a database, ad-hoc joins on a wide-column store)

### Analytics and other engines

- OLTP versus OLAP; star and snowflake schemas; facts, dimensions, grain, conformed dimensions
- Warehouse cost shapes: bytes scanned, partitioning and clustering, column projection, required partition filters, on-demand versus reserved capacity, authorized views
- Cohorts, funnels, sessionization and retention with windowed SQL; half-open intervals
- Approximate aggregation: HyperLogLog and quantile sketches with error bars
- Globally distributed SQL dialects: interleaved tables, limits
- Full-text search with `tsvector` and `tsquery`; vector similarity with `pgvector`; hybrid lexical and vector ranking; isolating search from OLTP

### Exercises

- From scratch in Go: bag relations with NULL logic; a schema registry with constraints; window functions as framed iterators; slotted pages with out-of-line storage; a clock-sweep buffer pool; a B-tree and an inverted index; iterator-model executor nodes with spills; histograms and selectivity estimates; an MVCC visibility simulator with a deadlock detector; a mini WAL with replay
- From scratch: an LSM-tree key-value store with a memtable, sorted runs, compaction and a Bloom filter per run
- Plan prediction: predict, then `EXPLAIN`, for joins, indexes, spills, warm and cold caches, skewed statistics and isolation anomalies
- Proofs: Armstrong completeness, the lossless-join test, the precedence-graph theorem, the 2PL theorem
- A checkout schema that cannot oversell under concurrency, with idempotency keys, minor-unit money and an isolation-level decision record
- Audit invariants under fault injection; cash-basis monthly revenue in SQL
- Keyset pagination, covering indexes and N+1 detection; a slow query rescued from its plan
- Primary and standby locally; replica lag; backup, restore and PITR drills
- A connection-pool sizing check with a failing test for over-subscription
- A migration run as a one-off job with an advisory lock
- Store selection for clickstreams, leaderboards, carts and lookup tables
- **Reasoning drills**
  - Predict plan shape, row counts and run time before `EXPLAIN ANALYZE`
  - Prove or refute a schedule's serializability from its precedence graph
  - Estimate table, index and buffer-pool sizes for a billion-row table
  - Choose an isolation level by the anomalies the workload can tolerate, as a decision record
