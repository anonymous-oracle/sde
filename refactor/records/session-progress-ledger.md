# Records for session-progress-ledger.md (R5 build edits, 2026-09-24)

Refactor bookkeeping only, not course material. Decision D6 keeps provenance, the D3 archive and every line the build changed or removed (R2b; the R2c Go tie-ins; R4, rules R4-*) out of the course files; decision D3 keeps them here, verbatim. Each entry names the build journal number (outputs/r2b/journal.jsonl), the rule and the class.

**J1266** · R5-16 · regenerate

````text
# GCP Cloud Mastery — Session Progress & Resumption Ledger
Snapshot taken September 21, 2026, at the close of a `/learn`-mode tutoring session on `Curriculum` ("The Consolidated Cloud Mastery Curriculum"). Upload this file **alongside** `Curriculum`, `system-design-primer-companion.md`, `sql-databases-companion.md`, and `design-patterns-companion.md` in the new chat — this ledger references all four and assumes they're available.

---

## 0. How to use this file (read first, in the new chat)

1. This is a **status file, not a transcript.** It records what's done, what's shaky, and exactly where to pick up — it does not reproduce the teaching itself. Re-derive explanations fresh; don't assume the learner remembers wording from a session you don't have access to.
2. Continue in **`/learn` mode**: one concept per turn, a check question before any answer is given, direct explanation for new material, worked examples for procedure — same rhythm the source skill defines.
3. **Resume point is §4** — start there. Everything in §3 is confirmed done and should be *recalled*, not re-taught, unless the learner asks to review.
4. **Teaching preferences confirmed this session (§5) are binding** — follow them without re-asking.

---

## 1. Source documents this ledger depends on

| File | Role | Status |
|---|---|---|
| `Curriculum` | Primary syllabus — Track A (A1–A11) → Track B → Track C → Track D → certs | Authoritative on order, scope, Lab Reality |
| `system-design-primer-companion.md` | Stitches System Design Primer concepts (SD-nn) into A5, A7–A9, B-track, C-track sessions | Ingested, aligns cleanly with `Curriculum`'s A1–D4 module IDs |
| `sql-databases-companion.md` | Stitches SQL/relational-theory depth into A8 | Ingested, but **flagged**: references a different, more granular document (`gcp-curriculum.md`/`unified-curriculum.md`, section numbers like `2.3`, `8.1`, `11b`) that does not match `Curriculum`'s actual A/B/C/D structure. Default plan: extract its SQL/relational content and bind it to **A8** directly when reached, ignoring its internal cross-references. If the learner has the actual file it's built against, ask for it and switch to following it exactly. |
| `design-patterns-companion.md` | Stitches SOLID, GRASP, all 23 GoF patterns, Clean/Hexagonal/Onion architecture, DDD, enterprise/microservice patterns, and anti-patterns into **A7** | Created this session to fill a confirmed gap — `Curriculum` had no dedicated design-patterns coverage |

---

## 2. Learner profile

- True beginner at session start (explicitly self-described as "high school student" level) — **no gaps left un-taught**; everything below was built from first principles, not assumed.
- Picks up new mechanisms fast, usually correct on the first attempt; when wrong, the error is consistently at the *terminology/precision* layer, not the underlying logic (e.g., naming "call stack" for something else, saying "centered" instead of tracing the exact variance mechanism, saying "power of 9" instead of clearly separating host-bit-count from prefix-length). **Standing correction style that's working well:** confirm the correct part explicitly, then sharpen the imprecise part with the exact mechanism — don't just restate the right answer.
- Explicitly wants checks embedded *in* the teaching turn, not as separate "what do you already know" diagnostic questions — see §5.
- Handles genuinely hard material well on first pass: Bayes' theorem, gradient descent by hand, and subnetting/VLSM math all landed within one or two turns each.

---

## 3. Track A — confirmed complete (recall only, do not re-teach)

- [x] **A1 — Digital Logic & Data Representation.** Binary/hex place-value systems, bits/bytes, boolean AND/OR/NOT/XOR (drilled via a real firewall-rule evaluation), KiB/MiB/GiB vs. KB/MB/GB storage prefixes and why the gap isn't "missing space," ASCII/UTF-8 encoding.
- [x] **A2 — Math for Cloud & ML.** Exponents/logs (log₂ as "halvings to reach n"), functions (a trained model *is* a function), vectors/dot products/matrix multiplication (the literal arithmetic inside a neural-network layer), mean/variance/std-dev, conditional probability including the `P(A|B) ≠ P(B|A)` asymmetry, Bayes' theorem worked via the "two roads" people-table until it stopped being a formula, derivatives/gradients/gradient descent by hand, correlation vs. causation, Big-O growth rates.
- [x] **A3 — Programming Foundations.** Python (variables, dynamic typing, floor-division's negative-number trap, `if/elif/else`, `for`/`while` with the infinite-loop failure mode, functions/`return`, all four core data structures with Big-O-grounded choice reasoning, OOP — classes/`self`/the "one method, many objects" binding mechanism), virtual environments/`pip`, Bash (variables, conditionals, loops, pipes, redirection, exit codes as the literal CI/CD pass/fail mechanism), APIs from code (`requests`, JSON parsing, SDKs as an HTTP wrapper, 401-vs-403 = authentication-vs-authorization), Git basics (working directory → staged → committed).
- [x] **A4 — Data Structures & Algorithms.** Arrays vs. linked lists traced to actual memory layout, hash maps (collision mechanism, average-`O(1)`-vs-worst-case-`O(n)`), stacks/queues (LIFO/FIFO via the call stack and browser back-button history), trees/BSTs (`O(log n)` search tied back to A2's binary search, plus the honest balance caveat), graphs (directed/undirected, modeled directly onto firewall reachability).
- [x] **Design-patterns gap identified and filled.** `Curriculum` had no SOLID/GoF/Clean-Architecture coverage; flagged mid-A5, resolved by creating `design-patterns-companion.md`, bound to **A7**. Nothing further needed here until A7.

---

## 4. Track A — in progress: **A5, Computer Networking** ← resume here

**Done, confirmed solid:**
- [x] OSI 7-layer model and the 4-layer TCP/IP model, including L4-vs-L7 load-balancer reasoning (what each layer can and cannot "see")
- [x] IP addressing: dotted-decimal octets tied back to A1's byte/255 ceiling
- [x] Subnetting & CIDR math, including VLSM (variable-length subnetting) for unequal subnet sizes — worked several `/x` prefix calculations correctly
- [x] Routing fundamentals: hop-by-hop forwarding, default gateway, explicitly connected to A4's graph material
- [x] TCP vs. UDP: three-way handshake, reliability/speed trade-off, DHCP's UDP requirement, correctly applied to a mixed game-traffic (position=UDP, chat=TCP) scenario
- [x] DNS: hierarchy (root → TLD → authoritative), caching/TTL mechanics, record types (A/AAAA/CNAME/MX/NS/TXT), DNS as a real SPOF (Dyn 2016 cited)

**Stitched-in companion content already folded into the above:** SD-30/SD-31 (TCP connection-pooling/Cloud SQL connection-budget trap, UDP's GCP lens — passthrough LBs, Cloud Run's no-raw-UDP limit, Agones), SD-08 (DNS — Cloud DNS routing policies, TTL-before-migration discipline).

**⚠️ One question asked, not yet answered — re-ask before moving on:**
> "You're migrating `api.example.com` from an old server to a new one, and its A record currently has a TTL of 24 hours. Walk through the correct order of operations — what do you do first, how long do you wait, and why — to avoid a chunk of users hitting the old server after cutover."

**Not yet started, remaining in A5 (teach in this order):**
- [ ] HTTP/HTTPS — request/response cycle, methods, status codes, headers, cookies. *(Companion stitch: SD-29 — verb idempotency/cacheability table, HTTP/2 vs HTTP/3 modern note, GCP lens on LB protocol support.)*
- [ ] TLS/SSL — the handshake, certificates, certificate authorities. *(Companion stitch: SD-35's transit-encryption slice only — the rest of SD-35 is gated to A10.)*
- [ ] NAT, firewalls, proxies vs. reverse proxies *(sets up NGINX in Track C; companion stitch: SD-11 reverse proxy, once load balancing is also done)*
- [ ] Load balancing concepts: L4 vs. L7 depth beyond what's already covered, algorithms (round robin, least connections, consistent hashing) *(companion stitch: SD-10's SSL termination/session persistence/failover/disadvantages, SD-09 CDN pull-vs-push)*
- [ ] VPNs and private connectivity concepts *(no companion stitch — `Curriculum`-native content)*

---

## 5. Standing teaching preferences confirmed this session (binding — don't re-ask)

- **Check questions must be woven into the concept explanation itself**, not asked as separate "what do you already know" diagnostics — the learner explicitly opted out of background-probing questions and asked for calibration to happen through how they handle the material.
- **"Maintain curriculum depth and academic rigour"** has been repeated multiple times as an explicit standing instruction — do not compress, simplify, or skip the "why," even under time pressure or a fast pace of correct answers.
- When companion-file content (system-design-primer, SQL, design-patterns) overlaps a `Curriculum` module, **teach it once, stitched into the same session** — never as a separate pass, per each companion's own §0.2 stitching rules.
- If a companion file references module IDs that don't exist in `Curriculum` (as `sql-databases-companion.md` does), **say so plainly rather than forcing a silent, possibly-wrong mapping** — this was well received when done for the SQL companion.

---

## 6. Open items for a future session

1. **Resolve the `sql-databases-companion.md` mismatch** before A8 — either the learner supplies the actual `gcp-curriculum.md`/`unified-curriculum.md` it's built against, or proceed with the fallback plan already noted in §1.
2. **A9 must be complete before teaching `design-patterns-companion.md`'s ARCH-09…12** (CQRS, Event Sourcing, Saga, Circuit Breaker/Strangler/Bulkhead) — that companion's own dependency gate requires it.
3. Nothing else outstanding — Tracks B, C, D and all cert-specific phases (Phase 4 onward) are entirely untouched and should follow `Curriculum`'s own phase plan once Track A finishes.

````
