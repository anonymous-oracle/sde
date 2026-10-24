# Part 13 · Distributed Systems & Large-Scale System Design · RULES AND DIRECTIVES

Companion topic list: `index/part13_distributed_systems.topics.md`. Ingest `index/00_learning_method.md` once per session, then this file, then the topic list. Mark the part done in `index/00_ingest_progress.md` before opening the next part.

Groups in this part: Foundations; Consensus and coordination; Replication; Availability; Partitioning; Distributed transactions; Caching at scale; Asynchronism and flow control; Stream and batch processing; Performance at scale; Testing and verification; System design method; Design techniques; Exercises.

---

# A. Standing rules: the Learning method

The full Learning method is kept **once**, in `index/00_learning_method.md`, and applies unchanged to every part. Read it at the start of a session and again after any compaction; it governs how every topic in this part is taught. It is not repeated here.

---

# B. Directives for this domain

## Distributed Systems & Large-Scale System Design

**Prerequisites:** networking (TCP, DNS, load balancing, latency numbers); databases (transactions, isolation, replication, indexes); concurrency (locks, happens-before, memory models); probability (order statistics, balls into bins, the birthday bound); queueing (Little's law, utilization); partial orders; hashing and consistent hashing basics.

**Depth bar:** a graduate distributed-systems course with replication and consensus labs plus staff-level system-design interviews: impossibility results proved, protocols implemented and tested under injected faults, designs sized with numbers.

**Capstone:** a replicated, partitioned key-value store with consensus and a client library, tested under partitions, crashes and clock skew with a linearizability checker, and its design written up and defended with capacity numbers.
