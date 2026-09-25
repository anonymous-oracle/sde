@@@ section
## 8. Academic depth (rule 0.4.10)

The academic pass of this companion: the mathematics and the classic results under the SD cards, taught after the engineering pass of each card it names and before the problem cards of §4.4 that lean on it. Each block names the SD cards it deepens and the main-course blocks it builds on (A2.D5–A2.D8 probability and queueing, A9.D1–A9.D9 distributed-systems theory). Aligned with the queueing and distributed-systems rows of the main course's §0.6. Problems SDA-P1…SDA-P10 follow in §8.11, keys in §8.12 (after the attempt only). A block is `mastered` by rule 0.4.10.3.

### 8.1 SDA.1 · Operational laws and Little's law (deepens SD-02, SD-03, SD-28)

- The operational laws hold for any system observed over an interval, with no distributional assumption: the utilization law U = X·S (throughput × mean service time per completion), the forced-flow law Xₖ = Vₖ·X (a resource visited Vₖ times per request), and Little's law L = λW.
- Little's law, sample-path proof sketch: draw each request as a horizontal bar from its arrival to its departure. The area under the curve "number in system over time" equals the sum of the bars' lengths. Divide that area by the interval length T to get L; divide it by the number of arrivals to get W; the number of arrivals divided by T is λ. So L = λW whenever the system empties, or the leftover area is negligible as T grows.
- The bottleneck law: the maximum throughput of a request path is 1 / max(Vₖ·Sₖ); adding capacity anywhere else raises no ceiling.
- Readings: Harchol-Balter, *Performance Modeling and Design of Computer Systems*, chapters 2–7; Lazowska, Zahorjan, Graham and Sevcik, *Quantitative System Performance* (1984), chapters 1–5 `(verify)`.

### 8.2 SDA.2 · Queues, variability and the knee (deepens SD-02, SD-03, SD-10, SD-28)

- M/M/1 derived from its birth–death chain: balance gives πₙ = (1 − ρ)ρⁿ, so the mean number in system is ρ/(1 − ρ) and, by Little's law, the mean time in system is 1/(μ − λ). At ρ = 0.5 a request spends 2 service times in the system; at ρ = 0.9, 10; at ρ = 0.99, 100 — the "knee" that makes 70–80% a planning ceiling.
- M/M/k and the Erlang C formula (stated; the probability that an arrival waits). One shared queue for k servers beats k separate queues at the same total load, because no server idles while work waits elsewhere — the reason a load balancer with a shared queue beats random assignment.
- Variability: the Pollaczek–Khinchine formula for M/G/1, E[W_q] = ρ·E[S]·(1 + C²)/(2(1 − ρ)), where C² is the squared coefficient of variation of the service time. Doubling the variance of service time raises the waiting time as much as a load increase does; this is the case for hedging and for keeping slow requests off the fast path.
- Closed systems: with N users and think time Z, the interactive response-time law R = N/X − Z; adding users to a saturated closed system adds latency, not throughput.

### 8.3 SDA.3 · Tails and fan-out (deepens SD-03, SD-37, SD-38c)

- For a request that waits on n independent sub-requests, P(all under t) = F(t)ⁿ. With n = 100 and each sub-request over its own p99 with probability 0.01, the whole request is slow with probability 1 − 0.99¹⁰⁰ ≈ 0.634.
- Hedged requests: sending a second copy after the p95 delay turns the tail of one request into the minimum of two, P(min > t) = P(X > t)², at a cost of about 5% extra load. Tied requests cancel the loser. Reading: Dean and Barroso, "The Tail at Scale", *Communications of the ACM* 56(2), 2013.
- Why averages hide tails: the mean of a heavy-tailed distribution is dominated by rare values, and a p99 cannot be averaged across hosts (main course A2.D7).

### 8.4 SDA.4 · Consistent hashing, analysed (deepens SD-17, SD-38a)

- Modulo hashing moves about (n − 1)/n of all keys when an n-th node is added, because a key keeps its node only when h mod n = h mod (n + 1).
- Consistent hashing (Karger et al., 1997): nodes and keys hash onto a ring and each key goes to the next node clockwise. Adding one node moves only the keys of one arc, an expected 1/(n + 1) of all keys.
- Balance: with one point per node, the largest arc is Θ(log n / n) of the ring with high probability, so one node can own about log n times its fair share. With v virtual points per node, where v = Θ(log n), every node's share is within a constant factor of 1/n with high probability. Rendezvous (highest-random-weight) hashing reaches the same balance with no ring, at O(n) cost per lookup; jump consistent hash (Lamping and Veach, 2014) uses O(1) memory but supports only numbered buckets.
- Readings: Karger, Lehman, Leighton, Panigrahy, Levine and Lewin, "Consistent Hashing and Random Trees" (STOC 1997); Thaler and Ravishankar, "Using Name-Based Mappings to Increase Hit Rates" (1998) `(verify)`.

### 8.5 SDA.5 · Balls into bins and the power of two choices (deepens SD-10)

- Throwing n requests at random onto n servers gives a maximum load of Θ(log n / log log n) with high probability.
- Sending each request to the less loaded of d ≥ 2 randomly chosen servers drops the maximum load to ln ln n / ln d + O(1): an exponential improvement from one extra probe (Azar, Broder, Karlin and Upfal, 1999; Mitzenmacher, 2001).
- Why "least connections" over all servers can herd: with stale load reports every balancer picks the same idle server. Two random choices tolerate staleness far better.
- Reading: Mitzenmacher, "The Power of Two Choices in Randomized Load Balancing", *IEEE Transactions on Parallel and Distributed Systems* 12(10), 2001; Mitzenmacher and Upfal, *Probability and Computing*, 2nd ed. (2017), chapter 5.

### 8.6 SDA.6 · Caching theory (deepens SD-26, SD-27, SD-37)

- Hit ratio and effective latency: T = h·t_hit + (1 − h)·t_miss (main course A1.D6's AMAT, applied to a service).
- Belady's optimal policy (evict the item used furthest in the future) is the offline optimum; LRU is k-competitive against it with a cache of size k (Sleator and Tarjan, 1985), and no deterministic online policy does better.
- Zipf-distributed popularity (the frequency of the i-th most popular key ∝ 1/iˢ) is why a small cache catches most requests: with s near 1, the top 1% of keys can carry a large share of traffic. The working set (Denning, 1968) is the set of keys referenced in the last τ requests.
- Caches and consistency: a TTL bounds staleness; invalidation plus a lease prevents a thundering herd and stale sets (Nishtala et al., "Scaling Memcache at Facebook", NSDI 2013).

### 8.7 SDA.7 · Replication and quorum mathematics (deepens SD-06, SD-07, SD-14, SD-15)

- Quorum intersection: with N replicas, read quorum R and write quorum W, R + W > N guarantees every read quorum meets every write quorum, by the pigeonhole principle: R + W elements drawn from N positions must repeat at least one position. W > N/2 also stops two conflicting writes from both succeeding.
- Availability of a majority quorum of N independent replicas, each up with probability p: A = Σ_{k=⌈(N+1)/2⌉}^{N} C(N,k) pᵏ(1 − p)^(N−k). For p = 0.99 and N = 3, A = 3p²(1 − p) + p³ ≈ 0.999702.
- Series and parallel availability: components in series multiply availabilities, and redundant components in parallel multiply unavailabilities. Correlated failures (one zone, one bad release) break the independence assumption, which is why the design places replicas across failure domains.
- Durability: with replication factor r and independent loss, P(loss) is roughly the chance that all r copies fail inside one repair window. Faster re-replication therefore buys as much durability as another copy does.

### 8.8 SDA.8 · CAP and PACELC, stated precisely (deepens SD-04, SD-05)

- Gilbert and Lynch (2002) proved Brewer's conjecture: in an asynchronous network that may lose messages, no read/write register can be both linearizable and available (every request to a non-failed node answered). Proof sketch: split the nodes into two sides and drop every message between them; a write on one side followed by a read on the other must either wait (losing availability) or return the old value (losing linearizability).
- What the theorem does not say: nothing about latency when the network is healthy, and nothing about weaker consistency models. PACELC (Abadi, 2012) adds that without a partition, a system still trades latency against consistency.
- Readings: Gilbert and Lynch, "Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services", *SIGACT News* 33(2), 2002; Abadi, "Consistency Tradeoffs in Modern Distributed Database System Design", *IEEE Computer* 45(2), 2012.

### 8.9 SDA.9 · Rate limiting and flow control, formally (deepens SD-28; recalls the Cloud Cybersecurity companion's AB-01, which owns the rate-limiting algorithms)

- The token bucket is AB-01's algorithm (recalled, not re-taught). What this block adds: a token bucket of rate r and depth b admits, over any interval of length t, at most b + r·t units. This arrival curve is the basis of network calculus (Le Boudec and Thiran), where a server offering rate R ≥ r bounds the delay at b/R.
- Back-pressure versus load shedding: a bounded queue converts overload into rejections, not unbounded delay; Little's law gives the queue bound for a target latency (L = λW).
- Retries with exponential backoff and jitter: without jitter, synchronized retries form waves; with full jitter the expected load spreads across the window.

### 8.10 SDA.10 · Estimation as a method (deepens SD-00, SD-36, SD-37, SD-39)

- Fermi estimation: decompose, estimate each factor to within a factor of 3, and multiply; errors in log space partly cancel, so the product is usually within an order of magnitude.
- Sensitivity: the factor with the widest range dominates the uncertainty of the product; estimate it twice by two methods.
- Readings for the whole pass: Kleppmann and Riccomini, *Designing Data-Intensive Applications*, 2nd ed. (2026), parts I–II; DeCandia et al., "Dynamo: Amazon's Highly Available Key-value Store" (SOSP 2007); Harchol-Balter, cited above.

### 8.11 Problem set (SDA-P1…SDA-P10)

- **SDA-P1** · proof · Prove Little's law for a single-server queue observed over [0, T] that starts and ends empty, using the area argument of SDA.1.
- **SDA-P2** · compute · A service handles λ = 800 requests per second with mean service time 1 ms on one worker. Treat it as M/M/1. What are ρ, the mean number in system and the mean response time? What happens to the response time at λ = 950?
- **SDA-P3** · derive · From the M/M/1 balance equations λπₙ = μπₙ₊₁, derive πₙ = (1 − ρ)ρⁿ and the mean number in system.
- **SDA-P4** · compute · A page fans out to 40 back ends, each slower than 50 ms with probability 0.02, independently. What is the probability that the page waits longer than 50 ms?
- **SDA-P5** · compute · A cluster of 10 cache nodes uses modulo hashing. One node is added. What fraction of keys move? What fraction moves under consistent hashing?
- **SDA-P6** · proof · Prove that R + W > N guarantees that every read quorum intersects every write quorum.
- **SDA-P7** · compute · Five replicas, each up with probability 0.99 independently. What is the availability of a majority quorum (at least 3 up)? Give the answer to six decimal places.
- **SDA-P8** · design · A load balancer reads server load from reports refreshed every 2 s. Argue from SDA.5 why "pick the less loaded of two random servers" is safer than "pick the least loaded server".
- **SDA-P9** · compute · A token bucket has rate 100 requests per second and depth 50. What is the largest number of requests it admits in any 2-second window?
- **SDA-P10** · derive · Use the Pollaczek–Khinchine formula to compare the mean queueing delay of an M/D/1 queue (deterministic service, C² = 0) and an M/M/1 queue (C² = 1) at the same ρ.

### 8.12 Keys (AFTER attempt only)

- **SDA-P1** — Expected: let N(t) be the number in system; ∫₀ᵀ N(t) dt = Σᵢ (dᵢ − aᵢ), because each request contributes 1 for exactly the length of its stay. Divide by T: L = (A/T)·(1/A)Σ(dᵢ − aᵢ) = λW, with A arrivals. · Wrong: "Little's law needs Poisson arrivals" — the argument uses no distribution.
- **SDA-P2** — Expected: μ = 1000/s, ρ = 0.8, L = 0.8/0.2 = 4, W = 1/(1000 − 800) s = 5 ms. At λ = 950: W = 1/50 s = 20 ms — 19% more load, four times the latency. · Wrong: "response time = service time = 1 ms at any load below capacity" — ignores queueing.
- **SDA-P3** — Expected: iterate πₙ₊₁ = ρπₙ, so πₙ = ρⁿπ₀; Σπₙ = 1 gives π₀ = 1 − ρ (for ρ < 1). E[N] = Σ n(1 − ρ)ρⁿ = ρ/(1 − ρ). · Wrong: π₀ = ρ — confuses the idle probability with the utilization.
- **SDA-P4** — Expected: 1 − 0.98⁴⁰ ≈ 1 − 0.4457 = 0.5543, about 55%. · Wrong: 40 × 0.02 = 0.8 — the union bound, which overestimates here.
- **SDA-P5** — Expected: under modulo hashing, a key keeps its node only if h mod 10 = h mod 11, which happens for 10 of every 110 residues (h mod 110 < 10), so about 10/11 ≈ 91% move. Under consistent hashing about 1/11 ≈ 9% move. · Wrong: "1/11 move under modulo hashing too" — that is consistent hashing's number.
- **SDA-P6** — Expected: suppose a read quorum Q_R and a write quorum Q_W are disjoint; then |Q_R ∪ Q_W| = R + W > N, but both are subsets of the N replicas, a contradiction. · Wrong: "it works because replicas gossip" — intersection is a counting fact, not a protocol.
- **SDA-P7** — Expected: A = C(5,3)p³q² + C(5,4)p⁴q + p⁵ with p = 0.99, q = 0.01: 10 × 0.970299 × 0.0001 + 5 × 0.96059601 × 0.01 + 0.9509900499 = 0.000970299 + 0.048029801 + 0.950990050 = 0.9999901494, which is 0.999990 to six places. · Wrong: 0.99⁵ ≈ 0.951 — that is the chance all five are up, which the quorum does not need.
- **SDA-P8** — Expected: every balancer reading the same stale report sends its traffic to the same "least loaded" server, which overloads before the next report (herding); two random choices spread requests across servers while still avoiding the worst ones, and its ln ln n bound degrades gracefully with stale data. · Wrong: "least loaded is always optimal" — it is optimal only with fresh, exact load.
- **SDA-P9** — Expected: at most b + r·t = 50 + 100 × 2 = 250. · Wrong: 200 — forgets the burst the full bucket allows.
- **SDA-P10** — Expected: E[W_q] ∝ (1 + C²)/2; M/D/1 gives ρE[S]/(2(1 − ρ)), exactly half the M/M/1 value ρE[S]/(1 − ρ). · Wrong: "the same, because ρ is the same" — waiting depends on variability as well as load.
@@@ c40-note
  - **Web check of 2026-09-24** (by web search against Google's own product pages, release notes and blogs; the `verify` flags stay, because these details keep changing):
    - Firestore with MongoDB compatibility: generally available since 26 August 2025, on the Firestore Enterprise edition.
    - Spanner Graph: generally available since 30 January 2025, queried in ISO GQL and interoperable with SQL.
    - Memorystore: the engines are Valkey, Redis Cluster, Redis and Memcached. Memorystore for Valkey is generally available with a 99.99% SLA and is the recommended default for new caches. Memorystore for Memcached is deprecated: from 1 February 2027 no new instances in new projects, and shutdown on 31 January 2029.
    - Pub/Sub: topic and subscription retention up to 31 days (subscriptions default to 7 days); exactly-once delivery is an opt-in setting for pull subscriptions, within one region.
    - The always-free `e2-micro`: one instance-month in us-west1, us-central1 or us-east1, with 30 GB-months of standard persistent disk.
    - Managed Service for Apache Kafka: the search found Kafka Connect, VPC Service Controls and mTLS announced as GA, but did not settle the status of the service as a whole. It stays `verify`.
    - Not checked that day: SLA percentages other than those above, HTTP/3 on the load balancers, Cloud Armor rule names, TTL support per store, LB timeouts, managed connection pooling, and Vertex AI Search for commerce.
@@@ c40-memcached
  - *Checked 2026-09-24:* Memorystore for Memcached is deprecated (no new instances in new projects from 1 February 2027; shutdown on 31 January 2029). Choose Valkey for a new cache-grade KV store.
