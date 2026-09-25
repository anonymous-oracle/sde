@@@ section
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
@@@ run-ex-pins

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
@@@ run-ex-call
    pins()
@@@ s3.1-note
> **Note:** Kit check of 2026-09-24: every file in §3.8 was extracted from this companion and run against a fresh local cluster (timezone UTC, C collation, seed v1). All 103 printed fingerprints (the exercise goldens and the trap fingerprints) were reproduced exactly. That server was PostgreSQL 16.13, so the run was a recorded deviation from the 15.x pin, made under `LAB_ALLOW_PG_MAJOR=16`. The pin stays at 15.x until a full run on another major is recorded.
@@@ s3.2-note
5. The pins are checked, not trusted: `run_ex.py` first reads `server_version_num`, `TimeZone`, the database collation and the seed's row counts, and refuses to run if any of them drifts from seed v1 on PostgreSQL 15.x with UTC and C. To run on another major version on purpose, set `LAB_ALLOW_PG_MAJOR` to that major and record the deviation beside the goldens you compare. If the collation check fails on a stock container image whose default locale is not C, create the database with the C collation: `CREATE DATABASE labdb LC_COLLATE 'C' LC_CTYPE 'C' TEMPLATE template0` (or initialise the cluster with `--locale=C`).
