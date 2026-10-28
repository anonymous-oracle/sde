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
  - Selection, projection, product, union and difference; join, intersection and division; each operator as a set comprehension: σ_p(R) = {t ∈ R : p(t)}, π_A(R) = {t[A] : t ∈ R}, R × S = {(r, s) : r ∈ R, s ∈ S}, R ⋈_θ S = σ_θ(R × S), R ∩ S = R − (R − S), and R ÷ S = π_X(R) − π_X((π_X(R) × S) − R), the X-values paired with every tuple of S
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
- **Joins**: inner, outer, cross, self, semi, anti, lateral, non-equi and range joins; fan-out when joining one-to-many; outer joins keep unmatched rows and NULL-extend the other side, a condition in ON filters before the extension while the same condition in WHERE removes the NULL-extended rows and turns the outer join into an inner join, and FULL keeps unmatched rows from both sides; a semi join returns each left row at most once when a match exists (EXISTS); an anti join returns left rows with no match (NOT EXISTS), which differs from NOT IN, where one NULL in the subquery makes each comparison UNKNOWN and no rows return; a lateral join evaluates a subquery once per left row, as in top-k per group
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
  - Heap pages, line pointers and tuple headers; alignment; TOAST for oversized values; modelled in Go as structs with explicit field widths for the tuple header (`xmin`, `xmax`, `ctid`, the null bitmap), the catalog row and the B-tree node header, with each struct's byte size checked by `unsafe.Sizeof` against the on-disk layout
  - Relation forks, the free-space map and the visibility map; segment files; a heap file as an unordered set of pages, where an insert goes to any page the free-space map shows has room and a sequential scan reads every page in order
  - Slotted pages: insert, delete, compact; line pointers as 4-byte item identifiers packing a 15-bit offset, two flag bits and a 15-bit length; a page header holding the free-space bounds; a page checksum computed over the page with the checksum field zeroed and verified on each read
  - HOT updates and fill factor
  - PostgreSQL system catalogs and system columns: `pg_class`, `pg_attribute`, `pg_type` and `pg_statistic` as ordinary tables describing relations, columns, types and planner statistics; the system columns `ctid`, `xmin` and `xmax` on every heap tuple
- **The buffer pool**
  - Hit ratio versus working set; sequential flooding and scan resistance; cache-hit probability under uniform random access to P pages with a B-page buffer, h ≈ B / P for B < P, so the expected physical reads per lookup are (1 − h) times the page accesses
  - Clock-sweep eviction, pins and reference counts
  - The background writer and the checkpointer
- **Indexes**
  - B+ trees: height ⌈log_F N⌉, splits and merges, leaf chains; Lehman–Yao right links
  - Hash indexes: static, extendible and linear hashing
  - LSM trees: memtables (skip lists), SSTables, leveled versus tiered compaction, Bloom filters per run; read, write and space amplification (the RUM conjecture)
  - Bitmap indexes and bitmap scans; GIN for JSONB, arrays and text; GiST and SP-GiST; BRIN for append-mostly data
  - Composite indexes and the leftmost-prefix rule; partial indexes; covering indexes with `INCLUDE`; index-only scans, which return columns from the index alone when the visibility map marks the heap page all-visible, and otherwise fetch the heap tuple to check visibility
  - Index selection as an NP-hard optimization; write amplification from too many indexes

### Query processing

- **Execution**
  - The Volcano iterator model
  - Nested-loop, block nested-loop, index nested-loop, sort–merge and (Grace) hash joins
  - External merge sort: 2N · (1 + ⌈log_{B−1}⌈N/B⌉⌉) I/Os; two passes when N ≤ B(B − 1)
  - Aggregation by sorting or hashing; `work_mem` and spills to temporary files; top-k by a bounded heap of size k instead of a full sort when `ORDER BY ... LIMIT k` is used, and top-k per group with `ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...)` filtered in an outer query to ranks at most k
  - Columnar and vectorized execution: late materialization, SIMD-friendly operators, run-length and dictionary compression
  - Parallel query: a leader process starts worker processes that scan disjoint page ranges or share a work queue for hash joins and aggregates, a Gather node merges their tuples, and a parallel plan is chosen when the estimated work exceeds a threshold and workers are free
- **Query optimization**
  - The parse, analyse, rewrite and plan pipeline; the parser builds a raw parse tree from the SQL grammar, analysis resolves names and types against the system catalogues, the rewriter expands views and applies rule-based transformations, and the planner picks the cheapest plan by cost estimates before the executor runs it
  - Statistics: histograms, most-common values, correlation; selectivity under uniformity and independence; extended statistics on correlated columns (`CREATE STATISTICS`); compounding estimation error; ANALYZE samples a fixed number of rows (set by the statistics target), refreshes the planner's statistics, and autovacuum re-runs it after a fraction of the rows change; the row estimate as table rows times the product of predicate selectivities, and the factor-of-ten misestimates that correlated predicates produce
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
- Optimistic concurrency control: a row carries a version number (or an ETag hash); a writer reads the version, computes the change without holding locks, and writes with `UPDATE ... WHERE version = expected`, retrying when zero rows change; the validation-based three phases (read, validate, write) over each transaction's read and write sets; optimistic offline locking across user think time, where the version travels to the client and the commit is rejected when it has changed; pessimistic locking (`SELECT ... FOR UPDATE`) when conflicts are frequent, traded against retries versus waiting

### Recovery and replication

- Buffer policies: steal and no-force, and why they require undo and redo
- The write-ahead-logging rule; each WAL record as a header with its total length, transaction ID, the pointer to the previous record and a CRC-32C over the record, followed by the payload, and recovery that stops at the first record whose CRC fails
- ARIES: LSNs, pageLSN, dirty-page and transaction tables, analysis, redo and undo passes, compensation log records
- Checkpoints; full-page writes; synchronous commit
- Physical streaming replication and WAL archiving; point-in-time recovery: a base backup plus archived WAL replayed up to a chosen target (a timestamp, an LSN or a named restore point), with the replay stopping before the bad transaction
- Logical replication: publications, subscriptions, decoding across major versions
- Change data capture through replication slots, and the disk risk of a dead consumer
- Replica lag as an SLI; read-your-writes through sticky sessions or primary reads; failover caveats
- Two-phase commit in databases: prepared transactions holding locks
- External consistency with TrueTime and commit-wait
- Deterministic databases (Calvin)

### Data modelling and design

- Conceptual → logical → physical design; ER diagrams; weak entities; ISA hierarchies; foreign-key placement for 1:N and N:M
- Keys: natural, surrogate, UUID (random versus time-ordered), snowflake IDs; client versus database generation; a Snowflake-style 64-bit integer as a 41-bit millisecond timestamp, a 10-bit worker ID and a 12-bit sequence, with the rule for a clock that moves backwards (wait or refuse)
- Money, units and time: integer minor units with explicit currency; `timestamptz` for instants; `date` for civil dates
- Hierarchies and graphs: adjacency lists, closure tables, path enumeration, nested sets
- Temporal data: valid time versus transaction time; slowly changing dimensions (type 2); as-of joins; preventing label leakage in feature queries
- JSONB versus columns, and the hybrid
- Soft delete, history tables, append-only audit; partial unique indexes
- Denormalization: trading write cost for reads; cache columns, aggregate tables, counters; refresh rules recorded in decision records
- Multi-tenancy: shared tables with `tenant_id`, schema or database per tenant; composite foreign keys; RLS as defence in depth; hot tenants; carrying `tenant_id` into cache keys, job payloads, export files and log fields, so a cache hit, a retried job or a log search cannot return another tenant's data
- Partitioning: range, list and hash; pruning; shard keys as locality keys; hot-key skew and sequential hotspots
- Schema evolution by expand and contract: add nullable, backfill, constrain, switch reads, drop; lock levels; concurrent index creation
- Data quality as constraints; deferral for cyclic foreign keys; EXCLUDE for ranges
- **The entity–relationship model**: entities and attributes (simple, composite, multivalued, derived); relationships with cardinality and participation constraints; weak entities; specialization and generalization; mapping an ER diagram to relations

### Operating databases

- Slow-query observability: `pg_stat_statements`, `auto_explain`, wait events; live triage with `pg_stat_activity`, `pg_blocking_pids`, cancel and terminate; idle-in-transaction sessions; `pgbench` load tests run with `-c` clients, `-j` threads and `-T` seconds, reporting transactions per second and latency, repeated before and after each change
- Connection pooling: session, transaction and statement modes and what transaction mode breaks; pool math (instances × pool ≤ `max_connections` minus reserved slots, with failover headroom)
- Backups: logical (`pg_dump`/`pg_restore`) versus physical with WAL archiving; restore drills to a new instance; RPO and RTO; HA and replicas are not backups
- Retention: dropping partitions versus mass deletes; cold-storage export
- Migrations as jobs: dirty state, advisory locks, expand/contract in CI, rollback plans; online index builds with `CREATE INDEX CONCURRENTLY` and lock timeouts on DDL
- Application data access: N+1 queries, ORM pitfalls, prepared statements, transaction boundaries, keyset pagination with unique tiebreakers and signed cursors, repositories
- Testing SQL: Postgres service containers, seeded fixtures, fingerprint and golden assertions, migration up and down tests
- Managed relational databases: provisioning, private connectivity, connectors and proxies, IAM database authentication, backups and PITR, HA standbys and read replicas, flags
- Database process model: PostgreSQL's postmaster as the supervisor process that forks one backend process per client connection, each with its own private memory for sorts and plans, so an idle connection still costs a process and its memory; shared memory holding the shared buffers, the WAL buffers, the lock table and the process array; background processes (checkpointer, background writer, WAL writer, autovacuum launcher and workers, WAL senders) and how connection count drives memory and context-switch cost, which is why a pool sits in front

### NoSQL and choosing a store

- BASE versus ACID; the modern reality of multi-item transactions in NoSQL stores
- Key-value stores: hash-table abstraction, ordered keys for range scans, caches
- Document stores: collections, flexible fields, queries over structure; joins in application code; MongoDB as the worked example: BSON documents in collections, CRUD with `insertOne`, `find` and `updateOne` taking query and update operators such as `$set`, compound indexes with the `_id` index, and write concern and read concern as the durability and staleness settings
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
- Full-text search with `tsvector` and `tsquery`; vector similarity with `pgvector`; hybrid lexical and vector ranking; isolating search from OLTP; pgvector's distance operators (L2, cosine and inner product) with HNSW and IVFFlat approximate indexes; Qdrant as a dedicated vector store with collections of points, each a vector with a payload, and filters on payload fields applied during the approximate search

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
