# Part 13 · Distributed Systems & Large-Scale System Design · TOPIC LIST

Rules and directives for this part: `index/part13_distributed_systems.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Distributed Systems & Large-Scale System Design

### Foundations

- **System models**
  - Synchronous, partially synchronous and asynchronous timing
  - Crash-stop, crash-recovery, omission and Byzantine failures
  - Fair-loss versus reliable links
  - Failure detectors: perfect versus eventually perfect; a timeout means only "suspected"
  - The eight fallacies of distributed computing
- **Time and order**
  - Happens-before as a partial order
  - Lamport clocks; vector clocks capture causality exactly
  - Physical clock synchronization (NTP); bounded uncertainty with TrueTime and commit-wait
  - Consistent snapshots (Chandy–Lamport)
- **Consistency**
  - Weak, eventual and strong consistency
  - Linearizability versus sequential, causal and eventual consistency
  - Serializability versus strict serializability
  - Session guarantees: read-your-writes, monotonic reads
  - CAP as proved by Gilbert and Lynch, with what it does not say; PACELC; choosing CP or AP
- **Impossibility results**
  - The Two Generals problem
  - FLP: no deterministic asynchronous consensus with one crash; bivalence; escapes via partial synchrony, randomization and failure detectors

### Consensus and coordination

- The consensus problem: agreement, validity, termination
- Single-decree Paxos (prepare/promise, accept/accepted) and Multi-Paxos
- Raft: terms and leader election, log replication, log matching and leader completeness, the commit rule, membership change
- State-machine replication
- Coordination services built on consensus: Chubby, ZooKeeper, etcd; leader election and distributed locks; fencing
- Byzantine fault tolerance: n ≥ 3f + 1; PBFT's three phases; why cloud control planes use crash-fault consensus

### Replication

- Primary–replica replication; read replicas; promotion on primary failure
- Multi-primary replication and write conflicts
- Chain replication
- Leaderless, Dynamo-style replication: read repair, hinted handoff, Merkle-tree anti-entropy, sloppy quorums
- Quorums: R + W > N by pigeonhole; W > N/2 against conflicting writes; majority-quorum availability Σ C(N,k)pᵏ(1 − p)^(N−k)
- CRDTs as join-semilattices: G-Counter, PN-Counter, OR-Set; operational transformation
- Durability: probability of losing all r copies within a repair window; re-replication speed

### Availability

- Active-passive (hot and cold standby) and active-active fail-over
- Availability in nines: downtime per year, month, week and day for 99.9% and 99.99%
- Series availability (multiply availabilities) and parallel availability (multiply unavailabilities)
- Correlated failures and failure domains (zones, regions, releases)

### Partitioning

- Federation (functional partitioning) by domain
- Sharding: shard keys, hot keys, rebalancing, cross-shard queries, replication per shard
- Denormalization to avoid distributed joins
- Consistent hashing: expected 1/(n + 1) key movement; Θ(log n / n) arcs and virtual nodes; rendezvous hashing; jump consistent hash
- Scatter-gather queries

### Distributed transactions

- Two-phase commit and its blocking window; why three-phase commit fails under partitions
- Two-phase commit over Paxos groups
- Sagas: local transactions with compensating transactions; choreography versus orchestration; no isolation between steps
- Exactly-once delivery as effectively-once: idempotence plus deduplication
- The transactional outbox and inbox; idempotent consumers

### Caching at scale

- Where to cache: client, CDN, reverse proxy, web server, database, application
- What to cache: rows, query results, serialized objects, rendered HTML; query-level versus object-level invalidation
- Update strategies: cache-aside, write-through, write-behind, refresh-ahead
- Cache internals: TTLs, sampled LRU approximation; sharded caches by consistent hashing
- Caching theory: effective latency T = h·t_hit + (1 − h)·t_miss; Belady's optimum; LRU's k-competitiveness; Zipf popularity; working sets
- Consistency: TTLs bound staleness; leases against thundering herds and stale sets

### Asynchronism and flow control

- Message queues versus task queues; workers; scheduled tasks
- Back-pressure with bounded queues and 503s
- Load shedding versus queueing; Little's law for queue bounds
- Token-bucket arrival curves (at most b + r·t over any interval) and network-calculus delay bounds
- When not to queue: cheap or real-time work

### Stream and batch processing

- MapReduce and dataflow; lineage-based recovery
- MapReduce job patterns: count by key, dedup, group-and-filter, sort by moving the count into the key
- Event time versus processing time
- Windows: tumbling, sliding, session
- Watermarks and late data
- Exactly-once processing
- Heavy hitters and approximate counting with bounded memory

### Performance at scale

- Performance versus scalability; latency versus throughput
- Vertical versus horizontal scaling; stateless clones with external session stores
- The tail at scale: fan-out amplification; hedged and tied requests
- The iterative scaling loop: load test → profile → fix the bottleneck → repeat
- Back-of-the-envelope estimation: users, requests per second, read:write ratio, storage per year

### Testing and verification

- Fault injection in the Jepsen style
- Deterministic simulation testing
- Linearizability checking of recorded histories (NP-complete in general; per-key partitioning)

### System design method

- The four-step interview method: use cases and constraints, high-level design, core components, scaling
- Scaling a web service from one box to millions of users: single box; static content to object storage and a managed database on private networking; load balancer, multi-zone web tier and database fail-over; read caches, stateless sessions and read replicas; autoscaling, configuration management and monitoring; warehousing, NoSQL, sharding and asynchronous workers
- Real-world systems and their lessons: MapReduce, Spark, Storm, Bigtable, HBase, Cassandra, Dynamo, MongoDB, Spanner, Memcached, Redis, GFS, HDFS, Chubby, Dapper, Kafka, ZooKeeper
- Company architectures as case studies: Amazon (service-oriented decomposition), Dropbox (metadata versus block storage), Facebook (memcached at scale, TAO, photo storage, live fan-out), Flickr and Pinterest (sharded MySQL and caching), Instagram (sharded PostgreSQL and Redis), Netflix (CDN and resilient microservices), Twitter (timelines and the firehose), Tumblr (dashboard fan-out), WhatsApp (persistent connections), YouTube (video storage and sharding), Uber (microservice sprawl), Stack Overflow (few large machines plus caching), PlentyOfFish (vertical database scaling), Salesforce (multi-tenant relational scale), TripAdvisor (read-heavy caching), DataSift (stream filtering), ESPN (spiky traffic), Justin.tv (live video ingest), Mailbox (queues under sudden growth), Cinchcast (media pipelines), Playfish (social-gaming load)

### Design techniques

- Blob storage with only locations in the database
- Short links and unique IDs: Base62 encodings, collision probability, counters and range allocators, Snowflake-style IDs and clock skew
- Log analytics into a warehouse
- Expiry and cleanup with native TTLs or sweepers
- Fan-out on write versus on read; the celebrity problem; active-user timelines
- Search: tokenization, inverted indexes, ranking, in-memory hot indexes
- Crawler frontiers, URL and content dedup with signatures, freshness, politeness
- Categorization dictionaries and budget alerts
- Graph traversal at scale: sharded adjacency, bidirectional BFS, precomputation
- Notification services through queues

### Exercises

- From scratch in Go: MapReduce; a linearizable key/value server; Raft (election, log replication, persistence, snapshots); a fault-tolerant key/value service on Raft; a sharded key/value service
- From scratch: Lamport and vector clocks; consistent hashing with virtual nodes and measured key movement; a quorum-replicated register with read repair; a Merkle-tree anti-entropy sync
- From scratch: a distributed rate limiter; an outbox relay with idempotent consumers; a Snowflake-style ID generator
- Designs: Pastebin or a URL shortener; a Twitter timeline and search; a web crawler; a personal-finance aggregator; social-network shortest paths; a key-value cache for search queries; sales rank by category; a service scaled from one box to millions of users
- Designs: file sync (chunking, content-hash dedup, delta sync), a search engine, collaborative documents (OT and CRDTs), a Redis-like store, a Memcached-like cache, a recommendation system, a chat app with presence, photo sharing, a news feed, graph search, a CDN, trending topics, random-ID generation, top-k requests in an interval, multi-datacentre serving, an online multiplayer card game, a garbage-collection service, an API rate limiter, a stock-exchange matching engine
- Proofs: quorum intersection, CAP's two-node argument, consistent-hashing movement
- **Reasoning drills**
  - Back-of-the-envelope capacity for every design before drawing it
  - Prove safety properties (quorum intersection, log matching) and build failure schedules that break weakened variants
  - Predict behaviour under partitions, clock skew and message loss, then inject the faults and compare
  - Find the assumption each design leans on most and show what breaks without it
