# Records for system-design-primer-companion.md (R2b, R2c and R4 build edits, 2026-09-24)

Refactor bookkeeping only, not course material. Decision D6 keeps provenance, the D3 archive and every line the build changed or removed (R2b; the R2c Go tie-ins; R4, rules R4-*) out of the course files; decision D3 keeps them here, verbatim. Each entry names the build journal number (outputs/r2b/journal.jsonl), the rule and the class.

**J60** · G0 · R2 in-file D3 archive, moved out whole

````text



---

## Pre-refactor text archive (D3)

*Refactor-authored section (2026-09-24).* Decision D3 says content may be re-arranged but never removed. Each block below is the exact pre-refactor text (after the §5 ID renames) of a line that R2 corrected or regenerated. It is kept for provenance only and is **not authoritative**; the live text above wins. Tooling excludes this section from ID and anchor checks.

**D3-01** · C-24 · §2 stitch table (pre-refactor)

```text
| Curriculum module | Companion concepts taught in the same session | Checkpoint |
|---|---|---|
| **A1** Digital logic & data representation | SD-36 powers of two (exact vs approximate; KiB vs KB), SD-37 units (ns/µs/ms) | — |
| **A2** Math for cloud & ML | SD-03 throughput/latency arithmetic · SD-07 availability math (series vs parallel, nines) · SX-02 key-space math (62^7) · Little's law (SD-28) · SD-00 back-of-envelope | BoE drills on P01 |
| **A3** Programming foundations | SD-33/34 REST vs RPC calls in Python + curl · SD-27 cache-aside code · SX-02 Base62 code · all O-problems' Python | O01, O02 |
| **A4** Data structures & algorithms | SD-21 hash table · SD-19 B-tree index · SX-11 LRU (hash map + doubly linked list) · SX-10 BFS · SD-38 consistent-hash ring · heaps/sorted sets (SX-07, SX-09) | O01, O02, O07 |
| **A5** Computer networking | SD-08 DNS · SD-09 CDN · SD-10 load balancer (L4/L7) · SD-11 reverse proxy · SD-29 HTTP · SD-30 TCP · SD-31 UDP · SD-35 (TLS in transit) | P08 steps "single box → DNS → Users++" |
| **A6** Linux & OS | SD-01 single-box baseline · SD-19 profiling tools · SD-37 memory/disk numbers · connection & file-descriptor limits (feeds SD-30) | P08 step 0 |
| **A7** Software architecture & APIs | SD-12 app layer/microservices/service discovery · SD-28 queues · SD-32 RPC · SD-33 REST · SD-34 · SD-02 | P01, O03 |
| **A8** Databases & data modeling | SD-13 … SD-25 (all of SQL, NoSQL, SQL-vs-NoSQL) | P01, P04 |
| **A9** Distributed systems theory | SD-04 CAP · SD-05 consistency · SD-06 fail-over/replication · SD-07 nines · SD-15 multi-master · SD-17 sharding · SD-38 consistent hashing/scatter-gather · SD-39 papers (Dynamo, Bigtable, Spanner, Chubby, GFS) | P05, P06 |
| **A10** Security & crypto | SD-35 (encrypt in transit/at rest, XSS, SQL injection, parameterized queries, least privilege) | P04 (credential storage) |
| **A11** Software delivery | SD-00 iterative loop (benchmark → profile → fix → repeat) · P08 "automate DevOps" step | — |
| **B1** What is cloud computing | P08 (why managed services beat self-run at each step) | P08 |
| **B2** Virtualization & containers | SD-01 "clones" · SD-10 horizontal scaling (identical images) | — |
| **B3** Architecture patterns & Well-Architected | SD-02 · SD-03 · SD-06 (active-passive ≈ warm standby/pilot light; active-active ≈ multi-site) · SD-07 · vertical vs horizontal (SD-10) | P08 |
| **B4** Cloud economics & FinOps | CDN cost vs origin cost (SD-09) · cache vs DB cost (SD-26) · autoscaling savings (P08 "Users++++") · storage tiering (SX-01) | P07 |
| **B5** Cloud IAM concepts | SD-35 least privilege · service-to-service auth for SD-12 | — |
| **C1** Docker | SD-01 clones · stateless servers (SD-10 horizontal-scaling disadvantages) | — |
| **C2** Kubernetes | SD-12 microservices & service discovery (Services, CoreDNS) · SD-10 (Service/Ingress = L4/L7) · P08 autoscaling (HPA) · StatefulSet ↔ stateful tier (SD-14, SD-21) | P08, P06 |
| **C3** NGINX | SD-11 reverse proxy · SD-10 · SD-26 web-server caching (Varnish/NGINX cache) · TLS termination (SD-10, SD-35) | P01 |
| **C4** CI/CD | SD-00 iterative delivery · blue-green/canary ↔ SD-06 active-active/passive | — |
| **C5** IaC (Terraform) | every P-problem's reference architecture (Section 5) as a `terraform plan` exercise | P01, P08 |
| **C6** Observability | SD-19 benchmark/profile · P08 monitoring list (host, aggregate, logs, external, alerts, errors) · SD-03 tail latency · Dapper (SD-39) | P08 |
| **C7** SRE principles | SD-07 nines ↔ SLO/error budget · SD-06 fail-over · SD-28 back pressure/retries · SD-03 percentiles | P08, Q19 |
| **D1** Classical ML | Q07 recommendation system · Q16 trending topics (score models) | Q07 |
| **D3** MLOps | Q07 feature store, batch vs online serving | Q07 |
| **D4** GenAI, embeddings, RAG | SX-06 reverse index ↔ embeddings/vector index · Q02 search engine · Q14 graph search | Q02, Q14 |
| **Part V — Compute** (GCE, GKE, Cloud Run, App Engine, Functions) | SD-01, SD-10 (MIG + autoscaling), SD-12 microservices, SD-28 workers | P08 |
| **Part V — Storage/DB** | SD-13 … SD-27, SX-01 | P01, P04, P06 |
| **Part V — Networking** | SD-08, SD-09, SD-10, SD-11, SD-30/31 | P08 |
| **Part V — Data/Analytics** | SD-28 (Pub/Sub) · SD-38 MapReduce → Dataflow/Dataproc · SX-03/08 log analytics → BigQuery | P07, P04 |
| **Part V — AI/ML** | Q07, Q02 | Q07 |
| **Part V — Security** | SD-35 | — |
| **Part V — Ops/DevOps** | SD-19, SD-00 loop, P08 | — |
| **PCA / Data Eng / Network Eng / Database Eng / DevOps / Developer certs** | PCA: all P-problems are constraint→trade-off drills (matches "which trade-off is correct"). Data Eng: SD-28, SD-38, P04, P07, Q16, Q18. Network Eng: SD-08–SD-11, SD-30/31, Q15. Database Eng: SD-13–SD-25, P05, Q05, Q17, Q19. DevOps: SD-07, SD-19, SD-28, P08. Developer: SD-26–SD-28, SD-32–SD-34 | Phase 4 |
| **Part VI AWS / Part VII Azure** | The primer's own AWS wording is the AWS-track reference: P08 is literally the AWS build. When Phase 6/7 arrives, re-run P08 with Part VIII names — no new concepts needed | P08 (AWS), P08 (Azure) |
```

**D3-02** · C-33 · §4.3 row P08

```text
| **P08** | Scale to millions of users (AWS in primer → GCP here) | SDP-T1 outline; SDP-T5 capstone | first pass: SD-00 … SD-03; second pass: everything through SDP-T4 | SX-12 (the loop) — each "Users+" step introduces one concept | A5, A6, B3 (first pass); C2, C6, V-COMP/V-NET (second) | — | every problem below; also the AWS/Azure re-runs (Parts VI/VII) |
```

**D3-03** · C-34 · §4.3 row O01

```text
| **O01** | Hash map | SDP-T0 | A3, A4 | — (SD-21 in miniature) | A3, A4 | — | O02, P06, Q05 |
```

**D3-04** · C-34 · §4.3 row O02

```text
| **O02** | LRU cache | SDP-T0 | O01, A4 (doubly linked list) | SX-11 | A3, A4 | O01 | P06, Q06 |
```

**D3-05** · C-34 · §4.3 row O03

```text
| **O03** | Call center | SDP-T0 | A3 (abstract classes, enums), A4 (queue) | — | A3, A4 | — | (queue/escalation patterns: SD-28) |
```

**D3-06** · C-34 · §4.3 row O04

```text
| **O04** | Deck of cards (+ blackjack) | SDP-T0 | A3 (inheritance, properties) | — | A3 | — | Q20 |
```

**D3-07** · C-34 · §4.3 row O05

```text
| **O05** | Parking lot | SDP-T0 | A3 (composition, polymorphism) | — | A3 | — | (concurrency extension: SD-13 transactions) |
```

**D3-08** · C-34 · §4.3 row O06

```text
| **O06** | Online chat (users, friends, private/group chat) | SDP-T2 | A3, SD-12, SD-13 | — | A3, A7 | O03 (state/roles) | Q09, Q13 |
```

**D3-09** · C-34 · §4.3 row O07

```text
| **O07** | Circular array (primer placeholder, no solution) | SDP-T0 | A3, A4 (arrays, modulo) | ring buffer | A3, A4 | O01 | (bounded buffers: SD-28 back pressure) |
```

**D3-10** · C-33 · P08 checkbox line

```text
- [ ] first pass (outline, during A5/A6/B3) · [ ] second pass (capstone, after Phase 3)
```

**D3-11** · C-24 · §4.5 ladder row **Phase 0 — Track A** (A1–A11)

```text
| **Phase 0 — Track A** (A1–A11) | A1: SD-36, SD-37 · A2: SD-00 (BoE), SD-03, SD-07 · A3/A4: SX-02 (Base62), SX-11 (LRU), SD-21 hash table · A5: SD-08, SD-29, SD-30, SD-31, SD-09, SD-10, SD-11 · A6: SD-01 · A7: SD-12, SD-28, SD-32, SD-33, SD-34 · A8: SD-13 … SD-25 · A9: SD-04 … SD-07, SD-38 · A10: SD-35 | **O01, O02, O07** (with A3/A4), **O03, O04, O05** (OOP), **Q21**; **P08 first pass** (outline, once A5/A6 are done); **P01** and **O06** (after A7/A8); **Q17** (after A1 + SX-02); **Q08** (= P01) |
```

**D3-12** · C-24 · §4.5 ladder row **Phase 1 — Track B** (B1–B5)

```text
| **Phase 1 — Track B** (B1–B5) | B3: SD-02, SD-06, P08 second-pass framing · B4: CDN/cache/autoscaling cost trade-offs · B5: least privilege in SD-35 | P08 cost discussion; P01 priced in the Pricing Calculator |
```

**D3-13** · C-24 · §4.5 ladder row **Phase 2 — Track C** (C1–C7)

```text
| **Phase 2 — Track C** (C1–C7) | C2/C3: SD-10, SD-11, SD-12 in Kubernetes/NGINX · C5: Terraform plans TF-1…TF-7 (§5.2) · C6: SD-19, P08 monitoring list · C7: SD-07 ↔ SLOs, SD-28 back pressure | **P06** and **Q06** (caches), **Q22** (rate limiter) |
```

**D3-14** · C-24 · §4.5 ladder row **Phase 3 — Track D** (D1–D4)

```text
| **Phase 3 — Track D** (D1–D4) | D1/D3: recommendation features · D4: embeddings ↔ SX-06 reverse index | **Q07**, **Q02** (semantic angle), **Q14** |
```

**D3-15** · C-24 · §4.5 ladder row **Phase 4 — GCP deep dive (PCA, PMLE first)**

```text
| **Phase 4 — GCP deep dive (PCA, PMLE first)** | Part V at Lens-3: Storage/DB, Networking, Data/Analytics | **P07**, **P04**, **P03**, **P02**, **P05**; then **Q05, Q19, Q15, Q16, Q18, Q01, Q09, Q13, Q10, Q11, Q12, Q03, Q04, Q20, Q23** |
```

````

**J61** · G3 · anchor-rewrite

````text
> **Refactor note (2026-09-24, C-25):** SD-04's prerequisite `A9` reads as: `Curriculum` A8 gives the CAP statement and intuition; A9 gives the formal limits and PACELC (A8 lists "CAP theorem"). SD-14, SD-15 and SD-17 are PRIMARY at A9 with an A8 forward pointer. The checked order is in `primer-binding-table.md` §2.
````

**J62** · G3 · anchor-rewrite

````text
> **Refactor note (2026-09-24, C-34):** O01, O02 and O07 are A4 recall checkpoints (practice, not re-teaching). O03–O06 are A7 checkpoints: O03 after DP-18 Chain of Responsibility and DP-16 State; O04 and O05 after F-01…F-04 and SOLID (PR-01…PR-05); O06 after SD-12. The "defects to find" lists double as anti-pattern practice: cross-reference design-patterns AP-01…AP-10 (`design-patterns-companion.md` §8). Card text unchanged.
````

**J63** · G5 · anchor-rewrite

````text
- `V-COMP, V-STOR, V-NET, V-DATA, V-AI, V-SEC, V-OPS` — `Curriculum` Part V service-map categories (C-22). `M1…M6`, `U1…U7`, `S1…S11` — new `Curriculum` tracks (stubs until R4). `Nx.y` — sections of `northstar-reference-app.md`.
````

**J64** · G5 · anchor-rewrite

````text
- Binding notation (C-24): `SD-21@A8` primary · `SD-21[hash-table slice]@A4` slice · `SD-21~C2` recall. The single source is `primer-binding-table.md`; the header stitches, §2 and §4.5 are generated from it.
````

**J65** · G5 · anchor-rewrite

````text
| **A4** Data structures & algorithms | SX-11 (via O02) | SD-19[B-tree index slice] · SD-21[hash-table slice] · SD-24[graph representation slice] · SD-38[consistent-hash ring slice (SD-38a)] · SX-07[heaps/sorted sets] · SX-09[heaps] · SX-10[BFS slice] | — | — | O01, O02, O07 — recall checkpoints, run as practice, not re-teaching (C-34) |
````

**J66** · G5 · anchor-rewrite

````text
| **A5** Computer networking | SD-08, SD-29, SD-09, SD-30, SD-10, SD-11, SD-31 | SD-01[clones + single-box ceiling slice] · SD-02[performance-vs-scalability slice] · SD-06 *(named only: P08 Users++ networking slice)* · SD-12 *(named only: P08 Users++ networking slice)* · SD-26[HTTP-layer caching slice: client/browser cache, Cache-Control/ETag, CDN-as-cache, reverse-proxy cache] · SD-35[transit-encryption slice (TLS in transit)] | — | — | P08 *Single box* step (SD-08 + the P08 network hardening → NT-01, NT-05) and the *Users++* networking slice (SD-09, SD-10, SD-11); SD-06 → A9 and SD-12 → A7 are named, not taught (C-33) |
````

**J67** · G5 · anchor-rewrite

````text
| **A6** Linux & OS | SD-01, SX-12 (via P08) | SD-19[profiling tools] · SD-30[connection and file-descriptor limits] | SD-37~ (memory/disk numbers) | — | P08 step 0 (the single-box OS view), then the full P08 first pass (outline) (C-33) |
````

**J68** · G5 · anchor-rewrite

````text
| **A7** Software architecture & APIs | SD-12, SD-28, SD-32, SD-33, SD-34 | SD-16[functional partitioning as service decomposition] | SD-02~ · SD-29~ | — | P01, O03 (after DP-18 + DP-16 State), O04, O05 (after F-01…F-04 + PR-01…PR-05 SOLID), O06 (C-34) |
````

**J69** · G5 · anchor-rewrite

````text
- **Prop Lock (C-28):** before Phase 4 the controls named above (VPC Service Controls, CMEK, Cloud Armor WAF rules, mTLS, Web Security Scanner) are Lens-1 names only; their mechanisms are taught in cyber NT-06, CR-14, WA-11, CR-17 and WA-02.
````

**J70** · G5 · anchor-rewrite

````text
- **Shared lab (C-28):** run once as cyber WA-05 / SQL SL-13; SD-35 recalls it. The lab text above is kept.
````

**J71** · G5 · anchor-rewrite

````text
- **Check owner (C-28):** the replay mechanism is taught by cyber CR-17 / PV-03; SD-35 keeps the question.
````

**J72** · G5 · anchor-rewrite

````text
   *Exception (added by the refactor, C-30):* `session-progress-ledger.md` is the single sanctioned cross-file tracker; inline `- [ ]` ticks remain authoritative and the ledger mirrors them. Refactor artifacts (`refactor-state.md`, manifests, reports) are build tooling, not trackers, and are not uploaded to teaching sessions.
````

**J73** · G5 · anchor-rewrite

````text
*Generated from `primer-binding-table.md` (2026-09-24, C-24).* Columns: PRIMARY = the session that teaches the concept in full; slices = one named ingredient taught earlier (or a continuation after); recalls = a one-line reference back; also in this session = the problem-level work (and, for V rows, the Lens-3 service wording) the pre-refactor row named, kept verbatim. The full pre-refactor table is kept verbatim in the D3 archive at the end of this file.
````

**J74** · G5 · anchor-rewrite

````text
| **A3** Programming foundations | — | SD-21[dict as a hash table] · SD-27[cache-aside code] · SD-32[RPC calls in Python] · SD-33[REST calls in Python + curl] · SD-34[REST vs RPC calls in Python + curl] · SX-02[Base62 code] | — | all O-problems' Python | — (O01, O02 move to the A4 recall checkpoints, C-34) |
````

**J75** · G5 · anchor-rewrite

````text
- **Taught by (index module, C-28):** in transit → `Curriculum` A5 TLS + cyber CR-11/CR-12 (the A5 transit slice; C-14) · at rest → CR-14 @ Phase 4 · XSS → WA-02 @ A10 · SQL injection / parameterized queries → SQL SL-13 (mechanics) + cyber WA-05 (attacker model) · least privilege → B5 + CL-03 · the P08 network hardening → NT-01, NT-05, NT-07 @ A5.
````

**J76** · G5 · anchor-rewrite

````text
*Column 2 of the Phase 0–4 rows is generated from `primer-binding-table.md` (2026-09-24, C-24): `ID[slice]` = a named ingredient taught before the concept's full session; `ID~` = recall. The pre-refactor rows are in the D3 archive.*
````

**J77** · G5 · anchor-rewrite

````text
| **Phase 0 — Track A** (A1–A11) | A1: SD-36, SD-37 · A2: SD-02[proportional-scaling arithmetic], SD-03[throughput/latency arithmetic; Little's law sizing], SD-07[availability math: series vs parallel, nines], SD-28[Little's law], SX-02[62^7 key-space math], SD-00 · A3: SD-21[dict as a hash table], SD-27[cache-aside code], SD-32[RPC calls in Python], SD-33[REST calls in Python + curl], SD-34[REST vs RPC calls in Python + curl], SX-02[Base62 code] · A4: SD-19[B-tree index slice], SD-21[hash-table slice], SD-24[graph representation slice], SD-38[consistent-hash ring slice (SD-38a)], SX-07[heaps/sorted sets], SX-09[heaps], SX-10[BFS slice], SX-11 · A5: SD-01[clones + single-box ceiling slice], SD-02[performance-vs-scalability slice], SD-26[HTTP-layer caching slice: client/browser cache, Cache-Control/ETag, CDN-as-cache, reverse-proxy cache], SD-35[transit-encryption slice (TLS in transit)], SD-08, SD-29, SD-09, SD-30, SD-10, SD-11, SD-31 · A6: SD-19[profiling tools], SD-01, SX-12, SD-30[connection and file-descriptor limits] · A7: SD-16[functional partitioning as service decomposition], SD-12, SD-28, SD-32, SD-33, SD-34 · A8: SD-05[strong vs eventual consistency as the C in CAP], SD-16[split databases by function: schema view], SD-18[denormalization as the inverse of normalization], SD-25[SQL-vs-NoSQL decision lists, family level], SD-04, SD-13, SD-19, SD-20, SD-21, SD-22, SD-23, SD-24, SD-26, SX-01, SX-02, SX-03, SX-04 · A9: SD-05, SD-06, SD-07, SD-14, SD-15, SD-16, SD-17, SD-18, SD-25, SD-27, SD-38, SD-39, SD-04[formal limits + PACELC] · A10: SD-35 · recall — A6: SD-37~ · A7: SD-02~, SD-29~ · A9: SD-20~, SD-23~ · A11: SD-00~ | **O01, O02, O07** (A4 recall checkpoints, C-34), **Q21**; **P08** A5 checkpoint (*Single box* + *Users++* networking slice) and A6 step 0, then **P08 first pass** (full outline, after A6; C-33); **O03, O04, O05, O06** (A7, after the design-patterns modules they exercise; C-34); **P01** (after A7/A8); **Q17** (after A1 + SX-02); **Q08** (= P01) |
````

**J78** · G9 · anchor-rewrite

````text
### 0.5 Learner teaching preferences (binding; copied unchanged from session-progress-ledger.md §5, invariant 4)
````

**J79** · G9 · anchor-rewrite

````text
- When companion-file content (system-design-primer, SQL, design-patterns) overlaps a `Curriculum` module, **teach it once, stitched into the same session** — never as a separate pass, per each companion's own §0.2 stitching rules.
````

**J80** · G9 · anchor-rewrite

````text
- If a companion file references module IDs that don't exist in `Curriculum` (as `sql-databases-companion.md` does), **say so plainly rather than forcing a silent, possibly-wrong mapping** — this was well received when done for the SQL companion.
````

**J464** · PRI-1 · anchor-rewrite

````text
Companion to `Curriculum` ("The Consolidated Cloud Mastery Curriculum")
````

**J465** · PRI-1 · anchor-rewrite

````text
Modified by the curriculum refactor on 2026-09-24; changes listed in CHANGELOG.md.
````

**J466** · PRI-2 · anchor-rewrite

````text
**This file is a complement to `Curriculum`, not a second curriculum. Read both. Whenever a Curriculum module is taught, also teach every companion concept bound to it (Section 2) in the same session, as one story. Similar, related, and overlapping concepts are stitched together and taught in parallel — never in separate sessions, never twice.**
````

**J467** · PRI-2 · anchor-rewrite

````text
   *Exception (added by the refactor):* `session-progress-ledger.md` is the single sanctioned cross-file tracker; inline `- [ ]` ticks remain authoritative and the ledger mirrors them. Refactor artifacts (`refactor-state.md`, manifests, reports) are build tooling, not trackers, and are not uploaded to teaching sessions.
````

**J468** · PRI-2 · anchor-rewrite

````text
When other companions bind to the same session, the Suite Session Protocol in `Curriculum` §0.4 governs.
````

**J469** · PRI-3 · anchor-rewrite

````text
- `V-COMP, V-STOR, V-NET, V-DATA, V-AI, V-SEC, V-OPS` — `Curriculum` Part V service-map categories. `M1…M6`, `U1…U7`, `S1…S11` — new `Curriculum` tracks (stubs until R4). `Nx.y` — sections of `northstar-reference-app.md`.
````

**J470** · PRI-3 · anchor-rewrite

````text
- Binding notation: `SD-21@A8` primary · `SD-21[hash-table slice]@A4` slice · `SD-21~C2` recall. The single source is `primer-binding-table.md`; the header stitches, §2 and §4.5 are generated from it.
````

**J471** · PRI-4 · anchor-rewrite

````text
*Generated from `primer-binding-table.md` (2026-09-24).* Columns: PRIMARY = the session that teaches the concept in full; slices = one named ingredient taught earlier (or a continuation after); recalls = a one-line reference back; also in this session = the problem-level work (and, for V rows, the Lens-3 service wording) the pre-refactor row named, kept verbatim. The full pre-refactor table is kept verbatim in the D3 archive at the end of this file.
````

**J472** · PRI-4 · anchor-rewrite

````text
Suite-wide ownership lives in the register in `Curriculum` §0.3 (which also carries the v1.1 rows for PACELC, cache stampede, tail latency, Little's law, consistent hashing, CRDTs, sketches, unique IDs, GC, event sourcing and credential storage). This table is the primer's slice of it; on a conflict §0.3 wins.
````

**J473** · PRI-4 · anchor-rewrite

````text
- **Taught by (index module):** in transit → `Curriculum` A5 TLS + cyber CR-11/CR-12 (the A5 transit slice) · at rest → CR-14 @ Phase 4 · XSS → WA-02 @ A10 · SQL injection / parameterized queries → SQL SL-13 (mechanics) + cyber WA-05 (attacker model) · least privilege → B5 + CL-03 · the P08 network hardening → NT-01, NT-05, NT-07 @ A5.
````

**J474** · PRI-4 · anchor-rewrite

````text
> **Note:** SD-04's prerequisite `A9` reads as: `Curriculum` A8 gives the CAP statement and intuition; A9 gives the formal limits and PACELC (A8 lists "CAP theorem"). SD-14, SD-15 and SD-17 are PRIMARY at A9 with an A8 forward pointer. The checked order is in `primer-binding-table.md` §2.
````

**J475** · PRI-4 · anchor-rewrite

````text
> **Note:** SD-04's prerequisite `A9` reads as: A8 gives the CAP statement and intuition; A9 gives the formal limits and PACELC (A8 lists "CAP theorem"). SD-14, SD-15 and SD-17 are PRIMARY at A9 with an A8 forward pointer. The checked order is in `primer-binding-table.md` §2.
````

**J476** · PRI-4 · anchor-rewrite

````text
> **Note:** O01, O02 and O07 are A4 recall checkpoints (practice, not re-teaching). O03–O06 are A7 checkpoints: O03 after DP-18 Chain of Responsibility and DP-16 State; O04 and O05 after F-01…F-04 and SOLID (PR-01…PR-05); O06 after SD-12. The "defects to find" lists double as anti-pattern practice: cross-reference design-patterns AP-01…AP-10 (`design-patterns-companion.md` §8). Card text unchanged.
````

**J477** · PRI-4 · anchor-rewrite

````text
*Column 2 of the Phase 0–4 rows is generated from `primer-binding-table.md` (2026-09-24): `ID[slice]` = a named ingredient taught before the concept's full session; `ID~` = recall. The pre-refactor rows are in the D3 archive.*
````

**J878** · R4-8 · anchor-rewrite

````text
- `V-COMP, V-STOR, V-NET, V-DATA, V-AI, V-SEC, V-OPS` — the main course's Part V service-map categories. `M1…M6`, `U1…U7`, `S1…S11` — the main course's reserved tracks (scope stubs; its reserved-tracks table says what each covers).
````

**J1073** · R7-2 · §0.1–§0.3 replaced by the part's own §0 (generic rules are in the course guide)

````text
## 0. Read this first — how this file complements Curriculum

### 0.1 Standing instruction (for Claude, every session)

**This file is a complement to the main course, not a second curriculum. Read both. Whenever a Curriculum module is taught, also teach every companion concept bound to it (Section 2) in the same session, as one story. Similar, related, and overlapping concepts are stitched together and taught in parallel — never in separate sessions, never twice.**

Why: the primer teaches *what* scalable systems are made of, in vendor-neutral words (load balancer, cache, queue, shard). Curriculum teaches *which real cloud resources* those words become, and the exam-grade judgment around them. Industry builds high-scale systems out of cloud resources, so every primer concept must arrive with its GCP resource attached — and every GCP resource should arrive with the primer's trade-off reasoning attached.

### 0.2 Stitching rules

1. **One concept, one teaching.** Where both files cover the same idea (L4 vs L7 load balancing, CAP, least privilege, queues, Big-O, TLS, replication), teach it once, in the Curriculum module that owns it. This file adds the *system-design layer*: trade-offs and disadvantages, numbers, interview framing, and the GCP resource. Later sessions refer back; they don't re-teach.
2. **Every concept gets a GCP lens the moment it is taught**, at three depths:
   - **Lens-1 (name it):** name the GCP resource, say why it is the answer, show one `gcloud`/console/Terraform line. Used throughout Phases 0–3.
   - **Lens-2 (touch it):** hands-on inside Lab Reality (free tier, a slice of the $300, a local emulator, or `terraform plan`).
   - **Lens-3 (design with it):** cert-depth trade-offs and limits. Phase 4 onward, alongside the PCA/PMLE/Data/Network/Database/DevOps material.
3. **AWS and Azure names come from Curriculum Part VIII — don't teach three times.** The primer's own examples are AWS-flavoured (S3, RDS, ELB, CloudFront, ElastiCache, SQS, Route 53, DynamoDB, Redshift, CloudWatch); every concept below translates them to GCP, and Part VIII gives the Azure side.
4. **Order and pacing belong to Curriculum** (Phase plan, Part X, "skip ahead" rights). **SD content and problems belong to this file.** On a conflict, Curriculum wins on order, Lab Reality, and exam time-sensitivity; this file wins on system-design content.
5. **Problems are checkpoints, not detours.** Run a problem from the ladder (Section 4.5) only when its prerequisite gate is met (Section 4.3). A problem session introduces at most one new concept and otherwise integrates what is already learned.
6. **Tracking is inline.** Tick the `- [ ]` box on a concept or problem in this file, or say "done" in chat. Do **not** create a separate tracker, log, or research file.
   *Exception:* the tutor's progress ledger (main course §0.1) is a running record beside these boxes, not a separate tracker; the inline `- [ ]` ticks remain authoritative.
7. **Honesty flags.** `(verify)` marks a GCP detail that changes often or that I could not confirm here — check the live docs before you rely on it for an exam or production. The primer itself is 2017-vintage; where industry has moved on, the concept block says so under **Modern note**.
8. **User can override anything:** skip a concept already known, jump to a specific problem, or go hands-on — same rights as Curriculum Part X.
9. **Read economically.** This file is large by design. Each session read §0 and §2, then only the blocks bound to today's Curriculum module (search by ID: `SD-10`, `SX-05`, `P02`…). Do not reload the whole file, and do not copy its contents into other files.

### 0.3 How one stitched session runs

1. **Anchor** — announce the Curriculum module and list the companion concepts bound to it (Section 2).
2. **Concept** — teach the shared idea once (Curriculum depth) and layer the primer's trade-offs and disadvantages on top.
3. **GCP lens** — the resource(s), Lens-1 always, Lens-2 when Lab Reality allows.
4. **Numbers** — one back-of-the-envelope calculation using Appendix 6.1–6.3.
5. **Micro-problem** — apply the concept to a ladder problem, or to the "Users+" step of P08 that introduces it.
6. **Check** — the concept's check questions; the user answers before I explain.
7. **Close** — tick the boxes in both files' sense (Curriculum module + companion concepts).

When other companions bind to the same session, the Suite Session Protocol (rule 0.4.2 in §0.6) governs.

````

**J1074** · R7-2 · anchor-rewrite

````text
### 0.4 Notation
````

**J1075** · R7-2 · copied preferences, contract and Lab Safety moved out

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

**J1076** · R7-3 · overlap-register slice moved to rule 0.3

````text
### 2.1 Overlap register — concepts that appear in both files (teach once, here)

Suite-wide ownership lives in the register in the main course §0.3 (which also carries the v1.1 rows for PACELC, cache stampede, tail latency, Little's law, consistent hashing, CRDTs, sketches, unique IDs, GC, event sourcing and credential storage). This table is the primer's slice of it; on a conflict §0.3 wins.

| Concept | Owner (teach here) | Companion adds |
|---|---|---|
| L4 vs L7 load balancing, algorithms | Curriculum A5 | SD-10: SSL termination, session persistence, LB failover, disadvantages |
| Reverse proxy vs forward proxy | Curriculum A5 / C3 | SD-11: benefits list, LB-vs-RP decision rule |
| DNS record types | Curriculum A5 | SD-08: TTL staleness, weighted/latency/geo routing, DNS-as-SPOF |
| TCP vs UDP | Curriculum A5 | SD-30/31: when-to-use rules, connection pooling |
| Message queues / event-driven | Curriculum A7 | SD-28: task queues, back pressure, delivery semantics |
| REST / gRPC | Curriculum A7 | SD-32/33/34: RPC-vs-REST decision, HATEOAS |
| ACID, NoSQL families, CAP | Curriculum A8 / A9 | SD-13…SD-25: scaling techniques, SQL-vs-NoSQL decision lists |
| Replication, sharding, consensus | Curriculum A9 | SD-06, SD-14, SD-15, SD-17, SD-38 |
| Availability vs durability, nines | Curriculum A9 / C7 | SD-07 tables and series/parallel formulas |
| HA, horizontal vs vertical scaling, DR | Curriculum B3 | SD-06, SD-10, P08 walk-through |
| Least privilege, encryption | Curriculum A10 / B5 | SD-35 checklist |
| Big-O, hash lookup, indexes | Curriculum A2 / A4 | SD-19 index trade-offs, SX-11 |
| Observability, SRE | Curriculum C6 / C7 | P08 monitoring list, back pressure |
| Autoscaling (HPA, MIG) | Curriculum C2 / V-COMP | P08 "Users++++" |
````

**J1093** · R7-4 · anchor-rewrite

````text
"Must know" = concepts that have to be complete *before* the problem. "New here" = the one concept the problem is allowed to introduce (rule 5, §0.2). Each problem's tier is the highest tier it needs.
````
