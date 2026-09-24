"""R4 Harden: withdraw the reserved tracks M, U and S (learner decision D16) and rebind every anchor to them.

D16 (2026-09-24): the learner declined Tracks M, U and S. The meta-prompt's M/U/S tracks mirror the legacy GCP notes
(its "M.NS" and "12.S0–S4 Foundations" sections), and the learner wants no more material from that file: "Work with
what we already have." So R4 writes no new module. It removes the stub table, moves the scope text that some stub rows
held into the one existing module that owns the topic (D7), and rewrites every anchor to a stub so that it names a
module that exists and teaches the topic. Nothing is lost (D3): each changed or removed line is journaled and kept
verbatim in records/.

Where a stub row held material (added in R2c-bis, D13), the material moves to its owner:
  M5 scope (IEEE 754 … log-sum-exp)          → an A2 line; the Floating point register row names A2
  the sketches register row (count-min, HLL,  → an A4 line; the register row names A4
    Bloom filters with their false-positive rate)
  S2 scope (views, C4, ADRs, HLD/LLD, NFR)    → an A7 line; A7's teaching block A7.10 names it
  S8 scope (migration, PCA 1.4)              → a line in the PCA block of Part V
  S11 scope (the PCA case studies as HLDs)    → already stated in the PCA block; the pointer to S11 goes
It also splits every module over 20 bound concepts into teaching blocks (C-49, rule 0.4.8), naming existing cards
only (blocks()).
Scope text that no existing module teaches (M1's number theory, M6's "statement + proof sketch" and "order
statistics, fan-out amplification", M1's birthday bound, M2–M4's "rigorous passes", U2's "rigorous pass") is not
re-homed: it was a plan for modules the learner declined, so it stays in records/ only.
"""
from r2b_common import CUR, PRI, SQL, SEC, RECORDS

GOF = "go-language-companion.md"
EV = ("D16 (2026-09-24): no Track M, U or S; the learner: \"Work with what we already have. I never wanted to copy "
      "more bloat from gcp curriculum file.\"")
EVR = EV + " An anchor to a withdrawn stub is rebound to the existing module that teaches the topic."
EVM = EV + " The stub row's scope text moves to the one existing module that owns the topic (D7); the row itself " \
           "goes to records (D3)."
EVX = EV + " The scope text was a plan for a declined module; no existing module teaches it, so it goes to records " \
           "only (D3), not into another part."


def cur(f):
    # ---- the stub table leaves the course
    h = f.heading("Reserved tracks M, U and S (stubs)")
    e = f.section_end(h)
    f.block("R4-1", "move", h, e, [], EV + " The reserved-track table (M1–M6, U1–U7, S1–S11) and its preamble "
            "move to records whole; its material rows are re-homed by R4-2…R4-5.", what="reserved-track stub section")
    # ---- material from the stub rows moves to its owner
    f.ins_after("R4-2", "Big-O notation for algorithm/cost reasoning", [
        "Floating point: IEEE 754, rounding, decimal vs binary; catastrophic cancellation, compensated (Kahan) "
        "summation, stable reformulations (`log1p`, log-sum-exp)"], EVM + " From the M5 row.", cls="move")
    f.ins_after("R4-3", "Sorting/searching intuition (enough to reason", [
        "Probabilistic structures: Bloom filters with their false-positive rate (1 − e^(−kn/m))^k, count-min sketch, "
        "HyperLogLog"], EVM + " From the sketches register row (its U2 owner is withdrawn).", cls="move")
    f.ins_after("R4-4", "API authentication patterns: API keys, OAuth 2.0, JWTs, service accounts", [
        "Architecture documentation: views, C4, ADRs (\"I pick X because Y, I accept Z\"), the HLD/LLD contract and "
        "NFR tables"], EVM + " From the S2 row (S1's requirements and quality attributes are its NFR tables).",
        cls="move")
    f.rep("R4-4", "anchor-rewrite", "A7.10 S1–S2 · A7.11 checkpoints",
          "A7.10 architecture documentation (views, C4, ADRs, HLD/LLD, NFR tables) · A7.11 checkpoints", EVR)
    f.rep("R4-5", "anchor-rewrite", "one \"I pick X because Y, I accept Z\" answer per requirement in S11.",
          "one \"I pick X because Y, I accept Z\" answer per requirement.", EVR + " The S11 row only restated this "
          "line.")
    f.ins_after("R4-5", "answer per requirement.", [
        "Migration and modernization (PCA 1.4): the six Rs mapped to landings (rehost with Migrate to Virtual "
        "Machines, replatform, re-architect for GKE or Cloud Run, retire, retain, repurchase); Migration Center "
        "discovery, dependency mapping and wave planning; licence impact (bring-your-own vs included) before wave 1; "
        "data movement (Database Migration Service, Datastream, Storage Transfer Service, Transfer Appliance); "
        "wave-0 connectivity; cutover checklist with a written rollback"], EVM + " From the S8 row.", cls="move")
    # ---- first-pass notes: the declined rigorous passes
    f.rep("R4-6", "anchor-rewrite", " The rigorous passes follow in M2 (linear algebra), M3 (calculus) and M4 "
          "(probability & statistics).", "", EVX)
    f.rep("R4-6", "anchor-rewrite", " The rigorous pass (proofs, recurrences, and implementing a balanced search "
          "tree) is U2.", "", EVX)
    # ---- the §0.3 register: every owner is a module that teaches the topic
    R = lambda old, new, ev=EVR: f.rep("R4-7", "anchor-rewrite", old, new, ev)
    R("| Floating point | M5 | SQL PQ-03 (decimal semantics) |",
      "| Floating point | A2 | SQL PQ-03 (decimal semantics); Go companion GO-03 (no implicit conversions) |")
    R("| Discrete-math foundations of relations | M1 | SQL PQ-01/02, RT-01 |",
      "| Discrete-math foundations of relations | SQL PQ-01/02 | SQL RT-01 |")
    f.line("R4-7", "move", "| Number theory for cryptography | M1 | Cyber CR-01…10 |", [], EVX + " No part teaches "
           "modular arithmetic as a topic; CR-08/CR-09 use it inside DH and RSA.")
    R("| M6 (the math: order statistics, fan-out amplification) | Primer SD-03/SD-38c (design levers: timeouts, "
      "hedging, replicas); C6/C7 (alerting/SLOs) |",
      "| Primer SD-03/SD-38c (percentiles; design levers: timeouts, hedging, replicas) | C6/C7 (alerting/SLOs) |",
      EVR + " SD-03 teaches percentiles, not averages (p50/p99 lab); SD-38c teaches tail = slowest shard. The M6 "
      "parenthesis goes to records: no existing module teaches that math.")
    R("| M6 (statement + proof sketch) | Primer SD-03/SD-28 (sizing checks, e.g. 400 rps × 250 ms); the A2 slice",
      "| Primer SD-03/SD-28 (L = λW; sizing checks, e.g. 400 rps × 250 ms) | the A2 slice",
      EVR + " SD-03's check teaches L = λW.")
    R("| Consistent hashing | U2 (analysis: expected movement 1/N, virtual nodes, load bounds) | Primer SD-38a "
      "(sharding/rebalancing design); A4 ring slice |",
      "| Consistent hashing | Primer SD-38a (the ring: ~1/N of keys move, virtual nodes; sharding/rebalancing) | "
      "A4 ring slice |", EVR + " SD-38a teaches the ring, the ~1/N movement and virtual nodes.")
    R("| Heavy hitters / sketches / approximate counting (count-min sketch, HyperLogLog, Bloom filters with their "
      "false-positive rate (1 − e^(−kn/m))^k) | U2 (randomized algorithms) |",
      "| Heavy hitters / sketches / approximate counting | A4 (probabilistic structures) |",
      EVR + " The parenthesis is now A4's line (R4-3).")
    R("| M1 (counting, birthday bound for collisions); A1 recall (bit layout) |", "| A1 recall (bit layout) |", EVX)
    R("| Garbage collection | U4 (memory management) | Primer Q21 (design problem); SX-04 (data GC/TTL); Go companion "
      "GO-09 (Go's collector, `GOGC`, `GOMEMLIMIT`) |",
      "| Garbage collection | Go companion GO-09 (Go's collector, escape analysis, `GOGC`, `GOMEMLIMIT`) | Primer Q21 "
      "(design problem); SX-04 (data GC/TTL) |")
    R("| Track S1–S3 recall it; they never restate it |", "| every later design exercise recalls it; none restates "
      "it |")
    R("| Primer P08 + SX-12 | Track S4/S9 recall |", "| Primer P08 + SX-12 | recalled wherever scale comes up; never "
      "restated |")
    R("| Concurrency | U5 (theory; reserved) | Go companion GO-15…GO-19 (goroutines, channels, `context`, the Go "
      "memory model, the race detector); A9 (distributed theory) |",
      "| Concurrency | Go companion GO-15…GO-19 (goroutines, channels, `context`, `sync`, the Go memory model, data "
      "races, deadlock, the race detector) | SQL CS-05 (serializability, 2PL, snapshot isolation); A9 (distributed "
      "theory) |")
    R("| A4 / U2 (concepts and costs) |", "| A4 (concepts and costs) |")


EVB = ("C-49 + rule 0.4.8 (3–5 concepts per session; a module over 20 bound concepts is split into teaching blocks). "
       "refactor-tools/budget.py counts the concept cards the six parts bind to each module; A3, A5, A7, A8, A9 and "
       "A10 are over 20. Each block names only existing cards, grouped by the module's own topic lines; no material "
       "is added. verify.py checks that every bound card is named in its module's blocks.")
LEAD = ("> **Note:** {m} binds more than twenty suite concepts (rule 0.4.8), so it is taught as ordered teaching "
        "blocks. These are sessions, not new modules; the module ID stays {m}. ")
BLOCKS = {
    "A3": ("A3. Programming Foundations",
           "A3.P1 Python (+ primer SD-21 [dict as a hash table], SD-27 [cache-aside code]) · A3.P2 Bash, APIs from "
           "code and Git (+ primer SD-32…SD-34 [RPC and REST calls in Python and curl]; SQL PQ-04 files and "
           "encodings, PQ-05 `psql` and a Docker Postgres, PQ-06 DB-API parameter binding) · A3.G1…A3.G4 the Go "
           "blocks above (GO-01…GO-14) · A3.C checkpoints."),
    "A5": ("A5. Computer Networking",
           "A5.1 layers, addressing, routing, TCP and UDP (+ primer SD-30, SD-31, SD-01 [clones + single-box "
           "ceiling], SD-02 [performance vs scalability]) · A5.2 DNS (+ primer SD-08; cyber DOS-02, NT-03, NT-04) · "
           "A5.3 HTTP and HTTP-layer caching (+ primer SD-29, SD-09, SD-26 [HTTP-layer caching]; cyber PQ-S-04) · "
           "A5.4 TLS mechanics (+ cyber CR-11, CR-12, NT-08; primer SD-35 [TLS in transit]) · A5.5 NAT, firewalls "
           "and proxies (+ primer SD-11; cyber NT-01, NT-02, NT-07) · A5.6 load balancing (+ primer SD-10; cyber "
           "DOS-01) · A5.7 VPNs and private connectivity (+ cyber NT-05) · A5.8 the Go renderings, once the Go "
           "companion reaches them (GO-21 `net/http`, GO-28 cookies, GO-17 deadlines, GO-23 gRPC) · A5.9 "
           "checkpoints."),
    "A8": ("A8. Databases & Data Modeling",
           "A8.1 relational model, keys, dependencies and normal forms; DDL, evaluation order, NULL (SQL RT-01, "
           "RT-04, RT-05, RT-07, SL-01…SL-03, DD-12; slice DB-2; primer SD-13) · A8.2 relational algebra and the "
           "query language (SQL RT-02, RT-03, RT-08, SL-04…SL-09, SL-14; slices DB-1, DB-3) · A8.3 transactions and "
           "isolation (SQL SL-10, CS-05; slice DB-9; primer SD-04 [the CAP statement], SD-05 [strong vs eventual as "
           "the C in CAP]) · A8.4 storage, indexes and the executor (SQL CS-01…CS-04, CS-08, OD-01; slices "
           "DB-4…DB-8; primer SD-19) · A8.5 recovery and replication in the engine (SQL CS-06, CS-07; slice DB-10) · "
           "A8.6 data modeling (SQL RT-06, DD-01…DD-08, DD-11, OD-08, SL-11, SL-12; primer SD-16 [schema view], "
           "SD-18 [denormalization as the inverse of normalization]; cyber PV-03, CM-02) · A8.7 NoSQL families and "
           "the choice (primer SD-20…SD-25, SD-26; SQL AN-06) · A8.8 warehousing: OLTP vs OLAP (SQL AN-01) · A8.9 "
           "attacks on the data layer (cyber WA-05, AB-06, AB-07) · A8.10 the Go renderings, once the Go companion "
           "reaches them (GO-22, GO-29) · A8.11 checkpoints."),
    "A9": ("A9. Distributed Systems Theory",
           "A9.1 consistency models and CAP in full (primer SD-04 [formal limits + PACELC], SD-05) · A9.2 "
           "replication, availability and durability (primer SD-06, SD-07, SD-14, SD-15; SQL CS-06) · A9.3 "
           "partitioning and sharding (primer SD-16, SD-17, SD-18, SD-25, SD-38; SQL DD-10, DD-13, AN-05) · A9.4 "
           "consensus, distributed transactions and failure design (SQL CS-07, SL-10; patterns ARCH-09…ARCH-12) · "
           "A9.5 caching at scale (primer SD-27; cyber DOS-08) · A9.6 scale primitives with SQL evidence (SQL OD-03, "
           "OD-09, DD-11; multi-tenancy: SQL DD-09, SL-13, cyber CL-06; cyber AB-05) · A9.7 the database theory "
           "tier, taught with the A8 sessions (SQL RT-02, RT-03, RT-04, RT-08, CS-02, CS-05, CS-08) · A9.8 the "
           "fallacies and distributed threats (cyber TH-06); the papers (primer SD-39) · A9.9 the Go renderings, "
           "once the Go companion reaches them (GO-15…GO-19, GO-29) · A9.10 checkpoints."),
    "A10": ("A10. Security & Cryptography Fundamentals",
            "A10.1 principles, economics and threat modeling (cyber PQ-S-02, PQ-S-05, PQ-S-06, TH-01…TH-04) · A10.2 "
            "cryptographic primitives (cyber PQ-S-01, CR-01…CR-10, CR-13, CR-16, CR-17, CR-19, SC-01) · A10.3 TLS "
            "and PKI, formally (cyber CR-11, CR-12; primer SD-35) · A10.4 authentication, sessions, federation and "
            "MFA (cyber AU-01…AU-13) · A10.5 web attack classes (cyber PQ-S-04, WA-01…WA-08, WA-10, WA-12; SQL "
            "SL-13) · A10.6 denial of service and resource exhaustion (cyber DOS-03, DOS-05, DOS-06) · A10.7 least "
            "privilege, defense in depth, zero trust (cyber CL-05, CK-04, PV-05) · A10.8 the Go renderings, once "
            "the Go companion reaches them (GO-07, GO-13, GO-21, GO-25, GO-26, GO-28) · A10.9 checkpoints."),
}
A7_BLOCKS = ("A7.1 client-server and API styles (+ primer SD-12, SD-32…SD-34) · A7.2 async and queues (+ primer "
             "SD-28; SQL SL-10 idempotent writes) · A7.3 OOP foundations + SOLID (patterns F-01…F-04, PR-01…PR-05) · "
             "A7.4 GRASP + creational patterns (PR-06…PR-14, DP-01…DP-05) · A7.5 structural patterns (DP-06…DP-12) · "
             "A7.6 behavioral patterns (DP-13…DP-23) · A7.7 architecture styles + DDD (ARCH-01…ARCH-08, anti-patterns "
             "AP-01…AP-10; primer SD-16 [functional partitioning as service design]; SQL OD-09 data access through "
             "repositories) · A7.8 API authentication/authorization + attacks (cyber AU-05…AU-08, AU-11…AU-13, "
             "CR-10, TH-04, CL-08) · A7.9 abuse and rate limits (cyber AB-01…AB-08) · A7.10 architecture "
             "documentation (views, C4, ADRs, HLD/LLD, NFR tables; SQL DD-01, RT-06, DD-08, DD-10, DD-12 as schema "
             "ADRs) · A7.11 the Go renderings, once the Go companion reaches them (GO-10, GO-11, GO-21, GO-22, GO-23, "
             "GO-28, GO-29) · A7.12 checkpoints. A3, A5, A8, A9 and A10 are split the same way (their notes).")


def blocks(f):
    f.line("R4-12", "anchor-rewrite", "> **Note:** A7 binds several dozen suite concepts, so it is taught as ordered "
           "teaching blocks.", "> **Note:** A7 binds several dozen suite concepts, so it is taught as ordered teaching "
           "blocks. These are sessions, not new modules; the module ID stays A7. " + A7_BLOCKS, EVB + " A7's R2 "
           "blocks keep their order and titles; each now names its cards, and checkpoints move to A7.12.")
    for m, (head, text) in BLOCKS.items():
        f.ins_section_end("R4-12", head, [LEAD.format(m=m) + text], EVB)


def comp(files, go):
    pri, sql, sec = files[PRI], files[SQL], files[SEC]
    # ---- primer
    pri.rep("R4-8", "anchor-rewrite", " `M1…M6`, `U1…U7`, `S1…S11` — the main course's reserved tracks (scope stubs; "
            "its reserved-tracks table says what each covers).", "", EVR)
    # ---- SQL
    S = lambda old, new, n=1: sql.rep("R4-9", "anchor-rewrite", old, new, EVR, n=n)
    S("(`A1…D4`, `M1…M6`, `U1…U7`, `S1…S11`, the Part V category IDs `V-…`)",
      "(`A1…D4`, `Phase 4`, the Part V category IDs `V-…`)")
    S("(§2 rows for M1 and A8 + A9)", "(§2 rows for A2 and A8 + A9)")
    S("| **M1** (logic, sets, proofs, counting, graphs) — *Tier", "| **A2** (math recall; PQ-01/PQ-02 teach the sets, "
      "logic and counting SQL needs) — *Tier")
    S("| **A4** (recall) + **U2** (structures, hashing theory, complexity) |",
      "| **A4** (recall: structures, hashing, complexity) |")
    S("| **A1/A2** (recall) + **M6** (units, orders of magnitude) |", "| **A1/A2** (recall: units, orders of "
      "magnitude) |")
    S("| **M5** (numerical stability) |", "| **A2** (floating point) |")
    S("*recall IEEE from M5; add decimal semantics*", "*recall IEEE from A2; add decimal semantics*")
    S("| **A8 + A9** (+ U5) — DB theory", "| **A8 + A9** — DB theory")
    S("| **S2** HLD/LLD contract, ADR template, NFR table |", "| **A7** architecture documentation (HLD/LLD contract, "
      "ADR template, NFR table) |")
    S("| **S2** + primer building blocks · HLD evidence packs |", "| **A7** architecture documentation + primer "
      "building blocks · HLD evidence packs |")
    S("| **S11** case-study capstone |", "| **Phase 4** case-study capstone (the PCA case studies) |")
    S("| **S11** control-plane case study |", "| **Phase 4** case-study HLDs (a control-plane store) |")
    S("**M1 / A4 + U2 / A8 + A9 / A8**", "**A2 / A4 / A8 + A9 / A8**")
    S("; the reserved M/U/S tracks are not placed yet.", ".")
    S("| **A1–A4 + M1** (SQL-T-HS", "| **A1–A4** (SQL-T-HS")
    S("| **A3, A6, A11 + M5** |", "| **A2, A3, A6, A11** |")
    S("| **A9 + S2** |", "| **A7 + A9** |")
    S("| **S11** | SQL-CAP1 – SQL-CAP4 |", "| **Phase 4** (PCA case studies) | SQL-CAP1 – SQL-CAP4 |")
    S("Sets, relations, functions, bags — stitch: M1",
      "Sets, relations, functions, bags — stitch: A2")
    S("3VL preview — stitch: M1 · DB-1", "3VL preview — stitch: A2 · DB-1")
    S("integer money vs float — stitch: M5", "integer money vs float — stitch: A2")
    S("IEEE recall from M5 then add decimal semantics.", "IEEE recall from A2 then add decimal semantics.")
    S("access-path raw material — stitch: A4 + U2 · DB-6", "access-path raw material — stitch: A4 · DB-6")
    S("page/row arithmetic — stitch: A1/A2 recall + M6 · DB-4", "page/row arithmetic — stitch: A1/A2 recall · DB-4")
    S("— stitch: A8 + A9 + U5 · DB-3", "— stitch: A8 + A9 · DB-3")
    S("ER → tables — stitch: S2 · DD-01", "ER → tables — stitch: A7 · DD-01")
    S("Conceptual → logical → physical — stitch: S2", "Conceptual → logical → physical — stitch: A7")
    S("Money, units, time — stitch: A8 · M5", "Money, units, time — stitch: A8 · A2")
    S("Soft delete, audit, history — stitch: A8 · S11", "Soft delete, audit, history — stitch: A8")
    S("Denormalisation with ADRs — stitch: S2 · primer SD-18", "Denormalisation with ADRs — stitch: A7 · primer SD-18")
    S("with the A8 + A9 (+ U5) theory", "with the A8 + A9 theory")
    S("- **Tags:** DD-02·S2", "- **Tags:** DD-02·A7")
    S("for the S11 case-study capstone.", "for the Phase 4 case-study capstone (the PCA case studies).")
    # ---- cyber
    C = lambda old, new: sec.rep("R4-10", "anchor-rewrite", old, new, EVR)
    C(", the reserved tracks (`M`, `U`, `S`; scope stubs in the main course),", ",")
    C("| **A6** | DOS-06, WA-10 (+ U1) |", "| **A6** | DOS-06, WA-10 |")
    sec.line("R4-10", "anchor-rewrite", "| **U7** | PV-05 | — | — |", [], EVR + " PV-05 moves to the Phase 4 Security "
             "row (its other anchor with a privacy home: PV-01…PV-04 are primary there).")
    C("PV-04, CM-01, CM-02 | CL-01 (Lens-3)", "PV-04, PV-05, CM-01, CM-02 | CL-01 (Lens-3)")
    C("co-tenant — stitch: A10 · S6 · S2 · CS155", "co-tenant — stitch: A10 · CS155")
    C("for the reference app — stitch: A10 · S6", "for the reference app — stitch: A10")
    C("STRIDE applied — stitch: A10 · S6 · Phase 4 Security", "STRIDE applied — stitch: A10 · Phase 4 Security")
    C("threat concepts — stitch: A9 · S2 · primer", "threat concepts — stitch: A9 · primer")
    C("— stitch: A6 · S2 · A10", "— stitch: A6 · A10")
    C("— stitch: A9 · SD-26 (recall) · S2 · V-STOR", "— stitch: A9 · SD-26 (recall) · V-STOR")
    C("— stitch: A6 + U1 · A10 · CS155", "— stitch: A6 · A10 · CS155")
    C("— stitch: B2 · S2 · CMU 95-746", "— stitch: B2 · CMU 95-746")
    C("— stitch: U7 · A10 · Phase 4 Security · XACS235", "— stitch: Phase 4 Security · A10 · XACS235")
    C("- **Map to GCP:** DOS-08, architecture studios (security-relevant only)", "- **Map to GCP:** DOS-08")
    # ---- Go (records below the build marker of records/go-language-companion.md)
    RECORDS.setdefault(GOF, [])
    G = lambda old, new, ev=EVR: go.rep("R4-11", "anchor-rewrite", old, new, ev)
    G("data-structure theory (A4, U2), HTTP (A5), concurrency theory in general (U5), design patterns",
      "data-structure theory (A4), HTTP (A5), design patterns")
    G("| A9 owns the theory; U5 owns concurrency theory in general |", "| A9 owns the distributed-systems theory; "
      "GO-15…GO-19 own concurrency in general (the main course's register) |")
    for needle in ("| U4 Programming Languages & Paradigms (reserved) |", "| U5 Concurrency & Parallel Computing "
                   "(reserved) |", "| Races, locks, deadlock, memory models in general | U5 |",
                   "| Garbage-collection theory | U4 |"):
        go.line("R4-11", "anchor-rewrite", needle, [], EVR + " The row pointed at a withdrawn stub; this part now "
                "owns the topic (main-course register: Concurrency → GO-15…GO-19, Garbage collection → GO-09).")
    G("| Data-structure theory and costs | A4 / U2 |", "| Data-structure theory and costs | A4 |")
    G("U5 (reserved) owns concurrency theory in general and A9 owns distributed-systems theory. These five modules own "
      "how Go does it:", "A9 owns distributed-systems theory. These five modules own concurrency for the whole suite "
      "(races, locks, deadlock, memory models), taught through how Go does it:")
    G("conversions — stitch: A3 · A1 · M5", "conversions — stitch: A3 · A1 · A2")
    G("memory — stitch: A3 · A6 · U4", "memory — stitch: A3 · A6")
    G("iterators — stitch: A3 · A4 · U4", "iterators — stitch: A3 · A4")
    G("scheduler — stitch: A6 · U5", "scheduler — stitch: A6")
    G("`select` — stitch: A9 · U5", "`select` — stitch: A9")
    G("memory model — stitch: U5 · A9", "memory model — stitch: A9")
    G("failure modes — stitch: A9 · U5 · C7", "failure modes — stitch: A9 · C7")
    G("fuzzing — stitch: C4 · U6", "fuzzing — stitch: C4")
    G("(recognition) — stitch: U4 · A10", "(recognition) — stitch: A10")
    G("implementations) — stitch: A4 · U2", "implementations) — stitch: A4")
    G("A4 owns the concepts and costs and U2 their analysis;", "A4 owns the concepts and costs;")
    G("*Stitch:* A9 · U5.", "*Stitch:* A9.")
    G("Floating point is IEEE 754 (recall M5 when it is written; the SQL companion's PQ-03 for decimals)",
      "Floating point is IEEE 754 (recall A2; the SQL companion's PQ-03 for decimals)")
    G("is already owned by A4, U2, the System Design Primer", "is already owned by A4, the System Design Primer")


def build(files, go):
    cur(files[CUR])
    blocks(files[CUR])
    comp(files, go)
