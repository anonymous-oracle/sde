# Primer binding table (C-24)

Built by `refactor-tools/binding.py` in R2 (2026-09-24). **Refactor-authored**: every row is a binding decision, not primer text. The primer's module-header stitches, its §2 table and its §4.5 ladder are generated from this table, so the three cannot drift apart (primer §7.3 maintenance rule, C-41).

Notation (C-24): `ID@X` = PRIMARY, the session that teaches the concept in full (exactly one) · `ID[slice]@X` = SLICE, the session teaches one named ingredient · `ID[forward pointer]@X` = named, not taught · `ID~X` = RECALL, a one-line reference back.

Candidate set: the union of the header stitch, the §2 table and the §4.5 ladder, with `Part V <category>` mapped to its V-ID (C-22). Nothing is dropped: `binding.py` fails if any candidate anchor is missing. SX techniques are PRIMARY at the first problem that introduces them (§4.3 "New here", C-35).

**Checks (this run):** 53 IDs, one PRIMARY each · candidate anchors dropped: 0 · C-25 topological violations: 0 · total errors: 0.

## 1. Bindings

| ID | PRIMARY | SLICE / forward pointer | RECALL | Primer candidate anchors (header ∪ §2 ∪ §4.5) |
|---|---|---|---|---|
| SD-00 | `SD-00@A2` | — | `SD-00~A11` (iterative loop: benchmark → profile → fix → repeat); `SD-00~B3`; `SD-00~C4` (iterative delivery); `SD-00~V-OPS` (the SD-00 loop) | A2, A11, B3, C4, V-OPS |
| SD-01 | `SD-01@A6` | `SD-01[clones + single-box ceiling slice]@A5` | `SD-01~B2` (clones); `SD-01~C1` (clones); `SD-01~V-COMP` | A6, B2, C1, V-COMP |
| SD-02 | `SD-02@B3` | `SD-02[proportional-scaling arithmetic]@A2`; `SD-02[performance-vs-scalability slice]@A5` | `SD-02~A7` | A2, A7, B3 |
| SD-03 | `SD-03@B3` | `SD-03[throughput/latency arithmetic; Little's law sizing]@A2` | `SD-03~C6` (tail latency); `SD-03~C7` (percentiles) | A2, B3, C6, C7 |
| SD-04 | `SD-04@A8` | `SD-04[formal limits + PACELC]@A9` | — | A8, A9 |
| SD-05 | `SD-05@A9` | `SD-05[strong vs eventual consistency as the C in CAP]@A8` | — | A9 |
| SD-06 | `SD-06@A9` | `SD-06[P08 Users++ networking slice]@A5` (fwd) | `SD-06~B3` (active-passive ≈ warm standby/pilot light; active-active ≈ multi-site); `SD-06~C4` (blue-green/canary ↔ active-active/passive); `SD-06~C7` (fail-over) | A9, B3, C4, C7 |
| SD-07 | `SD-07@A9` | `SD-07[availability math: series vs parallel, nines]@A2` | `SD-07~B3`; `SD-07~C7` (nines ↔ SLO/error budget) | A2, A9, B3, C7 |
| SD-08 | `SD-08@A5` | — | `SD-08~V-NET` | A5, V-NET |
| SD-09 | `SD-09@A5` | — | `SD-09~B4` (CDN cost vs origin cost); `SD-09~V-NET` | A5, B4, V-NET |
| SD-10 | `SD-10@A5` | — | `SD-10~B2` (horizontal scaling from identical images); `SD-10~B3` (vertical vs horizontal); `SD-10~C1` (stateless servers); `SD-10~C2` (Service/Ingress = L4/L7; HPA); `SD-10~C3`; `SD-10~V-COMP` (MIG + autoscaling); `SD-10~V-NET` | A5, B2, B3, C1, C2, C3, V-COMP, V-NET |
| SD-11 | `SD-11@A5` | — | `SD-11~C2`; `SD-11~C3` (reverse proxy in NGINX); `SD-11~V-NET` | A5, C3, V-NET |
| SD-12 | `SD-12@A7` | `SD-12[P08 Users++ networking slice]@A5` (fwd) | `SD-12~B5` (service-to-service auth); `SD-12~C2` (Services, CoreDNS); `SD-12~C3`; `SD-12~V-COMP` | A7, B5, C2, V-COMP |
| SD-13 | `SD-13@A8` | — | `SD-13~V-STOR` | A8, V-STOR |
| SD-14 | `SD-14@A9` | `SD-14[forward pointer]@A8` (fwd) | `SD-14~C2` (StatefulSet ↔ stateful tier); `SD-14~V-STOR` | A8, A9, C2, V-STOR |
| SD-15 | `SD-15@A9` | `SD-15[forward pointer]@A8` (fwd) | `SD-15~V-STOR` | A8, A9, V-STOR |
| SD-16 | `SD-16@A9` | `SD-16[functional partitioning as service decomposition]@A7`; `SD-16[split databases by function: schema view]@A8` | `SD-16~V-STOR` | A7, A8, V-STOR |
| SD-17 | `SD-17@A9` | `SD-17[forward pointer]@A8` (fwd) | `SD-17~V-STOR` | A8, A9, V-STOR |
| SD-18 | `SD-18@A9` | `SD-18[denormalization as the inverse of normalization]@A8` | `SD-18~V-STOR` | A8, V-STOR |
| SD-19 | `SD-19@A8` | `SD-19[B-tree index slice]@A4`; `SD-19[profiling tools]@A6` | `SD-19~C6` (benchmark/profile); `SD-19~V-OPS`; `SD-19~V-STOR` | A4, A6, A8, C6, V-STOR, V-OPS |
| SD-20 | `SD-20@A8` | — | `SD-20~A9` (BASE ↔ eventual consistency); `SD-20~V-STOR` | A8, A9, V-STOR |
| SD-21 | `SD-21@A8` | `SD-21[dict as a hash table]@A3`; `SD-21[hash-table slice]@A4` | `SD-21~C2` (StatefulSet ↔ stateful tier); `SD-21~V-STOR` | A4, A8, C2, V-STOR |
| SD-22 | `SD-22@A8` | — | `SD-22~V-STOR` | A8, V-STOR |
| SD-23 | `SD-23@A8` | — | `SD-23~A9`; `SD-23~V-STOR` | A8, A9, V-STOR |
| SD-24 | `SD-24@A8` | `SD-24[graph representation slice]@A4` | `SD-24~V-STOR` | A4, A8, V-STOR |
| SD-25 | `SD-25@A9` | `SD-25[SQL-vs-NoSQL decision lists, family level]@A8` | `SD-25~V-STOR`; `SD-25~Part V cert 8` (Cloud Database Engineer) | A8, V-STOR, Part V cert 8 |
| SD-26 | `SD-26@A8` | `SD-26[HTTP-layer caching slice: client/browser cache, Cache-Control/ETag, CDN-as-cache, reverse-proxy cache]@A5` | `SD-26~B4` (cache vs DB cost); `SD-26~C3` (NGINX/Varnish web-server cache); `SD-26~V-STOR` | A5, B4, C3, V-STOR |
| SD-27 | `SD-27@A9` | `SD-27[cache-aside code]@A3` | `SD-27~V-STOR` | A3, A9, V-STOR |
| SD-28 | `SD-28@A7` | `SD-28[Little's law]@A2` | `SD-28~C7` (back pressure/retries); `SD-28~V-COMP` (workers); `SD-28~V-DATA` (Pub/Sub) | A2, A7, C7, V-COMP, V-DATA |
| SD-29 | `SD-29@A5` | — | `SD-29~A7`; `SD-29~C3` | A5, A7, C3 |
| SD-30 | `SD-30@A5` | `SD-30[connection and file-descriptor limits]@A6` | `SD-30~V-NET` | A5, A6, V-NET |
| SD-31 | `SD-31@A5` | — | `SD-31~V-NET` | A5, V-NET |
| SD-32 | `SD-32@A7` | `SD-32[RPC calls in Python]@A3` | — | A3, A7 |
| SD-33 | `SD-33@A7` | `SD-33[REST calls in Python + curl]@A3` | — | A3, A7 |
| SD-34 | `SD-34@A7` | `SD-34[REST vs RPC calls in Python + curl]@A3` | — | A3, A7 |
| SD-35 | `SD-35@A10` | `SD-35[transit-encryption slice (TLS in transit)]@A5` | `SD-35~B5` (least privilege); `SD-35~C3` (TLS termination); `SD-35~V-SEC` | A5, A10, B5, C3, V-SEC |
| SD-36 | `SD-36@A1` | — | — | A1 |
| SD-37 | `SD-37@A1` | — | `SD-37~A6` (memory/disk numbers); `SD-37~C6` | A1, A6, C6 |
| SD-38 | `SD-38@A9` | `SD-38[consistent-hash ring slice (SD-38a)]@A4` | `SD-38~V-DATA` (MapReduce → Dataflow/Dataproc) | A4, A9, V-DATA |
| SD-39 | `SD-39@A9` | — | `SD-39~C6` (Dapper); `SD-39~V-COMP`; `SD-39~V-STOR`; `SD-39~V-NET`; `SD-39~V-DATA`; `SD-39~V-AI`; `SD-39~V-SEC`; `SD-39~V-OPS` | A9, C6, V-COMP, V-STOR, V-NET, V-DATA, V-AI, V-SEC, V-OPS |
| SX-01 | `SX-01@A8` (via P01) | — | `SX-01~B4` (storage tiering); `SX-01~V-STOR` | B4, V-STOR |
| SX-02 | `SX-02@A8` (via P01) | `SX-02[62^7 key-space math]@A2`; `SX-02[Base62 code]@A3` | — | A2, A3 |
| SX-03 | `SX-03@A8` (via P01) | — | `SX-03~V-DATA` (log analytics → BigQuery) | V-DATA |
| SX-04 | `SX-04@A8` (via P01) | — | — | — (SX: §2/§4.5 only) |
| SX-05 | `SX-05@Phase 4` (via P02) | — | — | — (SX: §2/§4.5 only) |
| SX-06 | `SX-06@D4` (via Q02) | — | `SX-06~Phase 4` | D4 |
| SX-07 | `SX-07@Phase 4` (via P03) | `SX-07[heaps/sorted sets]@A4` | — | A4 |
| SX-08 | `SX-08@Phase 4` (via P07) | — | `SX-08~V-DATA` (log analytics → BigQuery) | — (SX: §2/§4.5 only) |
| SX-09 | `SX-09@Phase 4` (via P04) | `SX-09[heaps]@A4` | — | A4 |
| SX-10 | `SX-10@Phase 4` (via P05) | `SX-10[BFS slice]@A4` | — | A4 |
| SX-11 | `SX-11@A4` (via O02) | — | — | A4 |
| SX-12 | `SX-12@A6` (via P08) | — | — | — (SX: §2/§4.5 only) |
| SX-13 | `SX-13@Phase 4` (via P04) | — | — | — (SX: §2/§4.5 only) |

## 2. C-25 topological check (hard prerequisites from primer §4.1)

Rule: every hard prerequisite `p` of `s` has PRIMARY(p) ≤ PRIMARY(s) in the order A1…A11, B1…B5, C1…C7, D1…D4, Phase 4, or a SLICE of `p` at or before PRIMARY(s) that is declared to serve `s` (C-25: "fix it by adding a named slice earlier"). Module prerequisites must be ≤ PRIMARY(s). Amendment applied (C-25): SD-04's module prerequisite `A9` reads as `A8` (statement + intuition), with A9 teaching the formal limits + PACELC as a slice.

| Concept @ PRIMARY | Hard prerequisite | Satisfied by |
|---|---|---|
| SD-00 @ A2 | SD-36 | `SD-36@A1` |
| SD-00 @ A2 | SD-37 | `SD-37@A1` |
| SD-02 @ B3 | SD-01 | `SD-01@A6` |
| SD-03 @ B3 | SD-02 | `SD-02@B3` |
| SD-04 @ A8 | SD-02 | `SD-02[performance-vs-scalability slice]@A5` |
| SD-05 @ A9 | SD-04 | `SD-04@A8` |
| SD-06 @ A9 | SD-04 | `SD-04@A8` |
| SD-06 @ A9 | SD-05 | `SD-05@A9` |
| SD-06 @ A9 | SD-10 | `SD-10@A5` |
| SD-07 @ A9 | SD-06 | `SD-06@A9` |
| SD-09 @ A5 | SD-08 | `SD-08@A5` |
| SD-09 @ A5 | SD-29 | `SD-29@A5` |
| SD-10 @ A5 | SD-02 | `SD-02[performance-vs-scalability slice]@A5` |
| SD-10 @ A5 | SD-29 | `SD-29@A5` |
| SD-10 @ A5 | SD-30 | `SD-30@A5` |
| SD-11 @ A5 | SD-10 | `SD-10@A5` |
| SD-11 @ A5 | SD-29 | `SD-29@A5` |
| SD-12 @ A7 | SD-10 | `SD-10@A5` |
| SD-12 @ A7 | SD-11 | `SD-11@A5` |
| SD-14 @ A9 | SD-05 | `SD-05@A9` |
| SD-14 @ A9 | SD-06 | `SD-06@A9` |
| SD-14 @ A9 | SD-13 | `SD-13@A8` |
| SD-15 @ A9 | SD-04 | `SD-04@A8` |
| SD-15 @ A9 | SD-14 | `SD-14@A9` |
| SD-16 @ A9 | SD-13 | `SD-13@A8` |
| SD-16 @ A9 | SD-14 | `SD-14@A9` |
| SD-17 @ A9 | SD-16 | `SD-16@A9` |
| SD-18 @ A9 | SD-13 | `SD-13@A8` |
| SD-18 @ A9 | SD-16 | `SD-16@A9` |
| SD-19 @ A8 | SD-13 | `SD-13@A8` |
| SD-19 @ A8 | SD-37 | `SD-37@A1` |
| SD-20 @ A8 | SD-04 | `SD-04@A8` |
| SD-20 @ A8 | SD-05 | `SD-05[strong vs eventual consistency as the C in CAP]@A8` |
| SD-20 @ A8 | SD-13 | `SD-13@A8` |
| SD-21 @ A8 | SD-20 | `SD-20@A8` |
| SD-22 @ A8 | SD-21 | `SD-21@A8` |
| SD-23 @ A8 | SD-21 | `SD-21@A8` |
| SD-24 @ A8 | SD-20 | `SD-20@A8` |
| SD-25 @ A9 | SD-13 | `SD-13@A8` |
| SD-25 @ A9 | SD-14 | `SD-14@A9` |
| SD-25 @ A9 | SD-15 | `SD-15@A9` |
| SD-25 @ A9 | SD-16 | `SD-16@A9` |
| SD-25 @ A9 | SD-17 | `SD-17@A9` |
| SD-25 @ A9 | SD-18 | `SD-18@A9` |
| SD-25 @ A9 | SD-19 | `SD-19@A8` |
| SD-25 @ A9 | SD-20 | `SD-20@A8` |
| SD-25 @ A9 | SD-21 | `SD-21@A8` |
| SD-25 @ A9 | SD-22 | `SD-22@A8` |
| SD-25 @ A9 | SD-23 | `SD-23@A8` |
| SD-25 @ A9 | SD-24 | `SD-24@A8` |
| SD-26 @ A8 | SD-09 | `SD-09@A5` |
| SD-26 @ A8 | SD-21 | `SD-21@A8` |
| SD-26 @ A8 | SD-37 | `SD-37@A1` |
| SD-27 @ A9 | SD-05 | `SD-05@A9` |
| SD-27 @ A9 | SD-26 | `SD-26@A8` |
| SD-28 @ A7 | SD-10 | `SD-10@A5` |
| SD-28 @ A7 | SD-12 | `SD-12@A7` |
| SD-31 @ A5 | SD-30 | `SD-30@A5` |
| SD-32 @ A7 | SD-29 | `SD-29@A5` |
| SD-32 @ A7 | SD-30 | `SD-30@A5` |
| SD-33 @ A7 | SD-29 | `SD-29@A5` |
| SD-34 @ A7 | SD-32 | `SD-32@A7` |
| SD-34 @ A7 | SD-33 | `SD-33@A7` |
| SD-35 @ A10 | SD-13 | `SD-13@A8` |
| SD-35 @ A10 | SD-29 | `SD-29@A5` |
| SD-37 @ A1 | SD-36 | `SD-36@A1` |
| SD-38 @ A9 | SD-17 | `SD-17@A9` |
| SD-38 @ A9 | SD-21 | `SD-21@A8` |
| SD-38 @ A9 | SD-23 | `SD-23@A8` |
| SD-38 @ A9 | SD-26 | `SD-26@A8` |
| SD-38 @ A9 | SD-28 | `SD-28@A7` |

Violations: none.

## 3. Decisions to review (`[resolved-by-default]`)

- SD-16: PRIMARY A9 is outside the primer's candidate set (C-25 cascade / C-27 / C-35) `[resolved-by-default]`
- SD-18: PRIMARY A9 is outside the primer's candidate set (C-25 cascade / C-27 / C-35) `[resolved-by-default]`
- SD-25: PRIMARY A9 is outside the primer's candidate set (C-25 cascade / C-27 / C-35) `[resolved-by-default]`
- SD-26: PRIMARY A8 is outside the primer's candidate set (C-25 cascade / C-27 / C-35) `[resolved-by-default]`
- SX-01: PRIMARY A8 is outside the primer's candidate set (C-25 cascade / C-27 / C-35) `[resolved-by-default]`
- SX-02: PRIMARY A8 is outside the primer's candidate set (C-25 cascade / C-27 / C-35) `[resolved-by-default]`
- SX-03: PRIMARY A8 is outside the primer's candidate set (C-25 cascade / C-27 / C-35) `[resolved-by-default]`
- SX-04: PRIMARY A8 is outside the primer's candidate set (C-25 cascade / C-27 / C-35) `[resolved-by-default]`
- SX-05: PRIMARY Phase 4 is outside the primer's candidate set (C-25 cascade / C-27 / C-35) `[resolved-by-default]`
- SX-07: PRIMARY Phase 4 is outside the primer's candidate set (C-25 cascade / C-27 / C-35) `[resolved-by-default]`
- SX-08: PRIMARY Phase 4 is outside the primer's candidate set (C-25 cascade / C-27 / C-35) `[resolved-by-default]`
- SX-09: PRIMARY Phase 4 is outside the primer's candidate set (C-25 cascade / C-27 / C-35) `[resolved-by-default]`
- SX-10: PRIMARY Phase 4 is outside the primer's candidate set (C-25 cascade / C-27 / C-35) `[resolved-by-default]`
- SX-12: PRIMARY A6 is outside the primer's candidate set (C-25 cascade / C-27 / C-35) `[resolved-by-default]`
- SX-13: PRIMARY Phase 4 is outside the primer's candidate set (C-25 cascade / C-27 / C-35) `[resolved-by-default]`

## 4. Teaching order inside each session (PRIMARY items, topological by §4.1)

- **A1:** SD-36 → SD-37
- **A2:** SD-02[proportional-scaling arithmetic] → SD-03[throughput/latency arithmetic; Little's law sizing] → SD-07[availability math: series vs parallel, nines] → SD-28[Little's law] → SX-02[62^7 key-space math] → SD-00
- **A4:** SD-19[B-tree index slice] → SD-21[hash-table slice] → SD-24[graph representation slice] → SD-38[consistent-hash ring slice (SD-38a)] → SX-07[heaps/sorted sets] → SX-09[heaps] → SX-10[BFS slice] → SX-11
- **A5:** SD-01[clones + single-box ceiling slice] → SD-02[performance-vs-scalability slice] → SD-06[P08 Users++ networking slice] → SD-12[P08 Users++ networking slice] → SD-26[HTTP-layer caching slice: client/browser cache, Cache-Control/ETag, CDN-as-cache, reverse-proxy cache] → SD-35[transit-encryption slice (TLS in transit)] → SD-08 → SD-29 → SD-09 → SD-30 → SD-10 → SD-11 → SD-31
- **A6:** SD-19[profiling tools] → SD-01 → SX-12
- **A7:** SD-16[functional partitioning as service decomposition] → SD-12 → SD-28 → SD-32 → SD-33 → SD-34
- **A8:** SD-05[strong vs eventual consistency as the C in CAP] → SD-14[forward pointer] → SD-15[forward pointer] → SD-16[split databases by function: schema view] → SD-17[forward pointer] → SD-18[denormalization as the inverse of normalization] → SD-25[SQL-vs-NoSQL decision lists, family level] → SD-04 → SD-13 → SD-19 → SD-20 → SD-21 → SD-22 → SD-23 → SD-24 → SD-26 → SX-01 → SX-02 → SX-03 → SX-04
- **A9:** SD-05 → SD-06 → SD-07 → SD-14 → SD-15 → SD-16 → SD-17 → SD-18 → SD-25 → SD-27 → SD-38 → SD-39
- **A10:** SD-35
- **B3:** SD-02 → SD-03
- **D4:** SX-06
- **Phase 4:** SX-05 → SX-07 → SX-08 → SX-09 → SX-10 → SX-13
