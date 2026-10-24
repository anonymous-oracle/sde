# Part 12 · Databases, SQL, Relational Theory & Data Modelling · RULES AND DIRECTIVES

Companion topic list: `index/part12_databases.topics.md`. Ingest `index/00_learning_method.md` once per session, then this file, then the topic list. Mark the part done in `index/00_ingest_progress.md` before opening the next part.

Groups in this part: Pre-SQL foundations; Relational theory; The SQL language; Storage and access methods; Query processing; Transactions and concurrency control; Recovery and replication; Data modelling and design; Operating databases; NoSQL and choosing a store; Analytics and other engines; Exercises.

---

# A. Standing rules: the Learning method

The full Learning method is kept **once**, in `index/00_learning_method.md`, and applies unchanged to every part. Read it at the start of a session and again after any compaction; it governs how every topic in this part is taught. It is not repeated here.

---

# B. Directives for this domain

## Databases, SQL, Relational Theory & Data Modelling

**Prerequisites:** sets, relations, functions and bags; propositional and predicate logic; binary search, sorting, hashing and trees; the storage hierarchy with page and row arithmetic; integer versus floating-point arithmetic and encodings; files, CSV and JSON; a programming language with a database driver; operating-system virtual memory and `fsync`; concurrency (locks, deadlock).

**Depth bar:** a top-university database-systems course with its internals labs plus production PostgreSQL practice: each theorem proved, each plan predicted before `EXPLAIN`, each operational procedure rehearsed.

**Capstone:** a production schema for a transactional product taken from requirements through normalization, migrations, indexing and an isolation-anomaly test suite to backups with a timed restore, deployed on Cloud SQL with a connection budget.
