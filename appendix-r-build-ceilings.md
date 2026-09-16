# Appendix R (DRAFT — not merged) — Theory spine + from-scratch build ceilings for the 309

**Status.** Standalone draft. Nothing here has been written into `gcp-curriculum.md`, which
remains the **syllabus of record** and is untouched. Researched and curated 2026-09-16.

**How to read this file.**

```
PART A  The finding — why the 309 are not yet buildable-from-scratch
PART B  The existing theory spine (Block T + Part M), carried from the curriculum
        so this draft stands alone
PART C  Bridge — which spine family feeds which ceiling
PART D  The ceilings (R.1–R.5) — the new curation: text + course per family
PART E  Source links, verified
```

Part B is **carried from `gcp-curriculum.md`** (Block T, lines 633–888; Part M, lines
1316–1508; course spine, lines 591–628; prerequisite map, lines 549–588). It is reproduced
in substance — tiers, derive/prove gates, sources, overlap bans — so a learner can work from
this file alone. The curriculum is still the source of record; if the two ever diverge, the
curriculum wins.

---

# PART A — The finding

Appendix M's families are taught as **literacy + evidence packs**. That is enough to
*architect* a case study and to ship the four Northstars. It is **not** enough to *build one
from scratch unaided*, for three reasons found by reading the file:

1. **Ceilings are named but empty.** `T-RL`, `T-CAUSAL`, `T-CV`, `T-SIGNAL`, `T-DL`, `T-NLP`
   appear only as one-line scope pointers (Part 12 map lines 491–494; 9c.0 defer rows
   6116–6124) with **no assigned text and no course**. Grep counts: T-RL 4, T-CAUSAL 8,
   T-CV 8, T-SIGNAL 10, T-DL 9, T-NLP 3 — every one a pointer, never a shelf.
2. **The two largest families have no theory owner at all.** Recommend/feed (65) +
   Search/rank/ads (36) = **101 of 309**. There is no `T-REC`, no `T-IR`, no `T-GRAPH`
   anywhere in the file (grep: 0 hits each). Manning IIR is the only retrieval text, entered
   at 9c.2 for IR literacy only.
3. **"Other" (101) is index-only** — pricing, routing, entity resolution, anomaly,
   dimensions have no owner and no reading. A third of the catalog.

Coverage arithmetic: 65 + 36 + 101 = **202 of 309 studies (65%)** sit on a ceiling that is
either unstocked or absent.

**Scope warning — decide before opening.** Populating these ceilings **contradicts current
out-of-syllabus lines** (transformer-from-scratch, full CV, full RL/GNN, DSP/Kaldi). Those
lines are deliberate and I have not reversed them. Part D is the **continuation** you open
*after* T–11b, per family, when the goal changes from "architect and defend" to "build
unaided." Flagged, not silently overturned.

**Access.** **[free]** = author- or publisher-hosted at no cost, link-checked 2026-09-16.
The Appendix B excluded-host rule was honoured: no Scribd, Z-Library, dokumen.pub, or scan
mirrors were fetched or are cited, though several surfaced in search results.

---

# PART B — The existing theory spine (carried from the curriculum)

## B.0 Placement in the course spine

```
T  Theory prerequisites (T.Quant…T.MLTheory) — HS→UG→grad-as-needed; skip-testable;
   Tier HS before F for absolute beginners
F  Foundation (F1–F4) — network vocab + Discrete JIT in F1; cloud literacy F2–F4
M  Quantitative prereqs: M.NS; M.ML (+ IPS); M.TS; M.CAUSAL lite (before 9c)
0…11b  GCP + software system/architecture design
12 Continuation AFTER 11b — deep drills S0–S24
```

**Order:** `T → F → M → 0…11b → 12`. No GCP product labs in Block T — paper + derive + tiny
Python → Go where implementable. Depth is **per topic up to graduate-coursework level** when
the main-track owner needs it. **Skip-test any tier already confirmed.**

**Block T complete when:** for each family needed on the live track, the required tier's
derive/prove gate (or skip-test) is on the ledger → enter F1.

## B.1 Unified owner-node map

| Unified node | Block T home | Main-track / continuation |
|---|---|---|
| `MATH-FUND` | **T.Quant** + **T.Alg** | F/0/8.F/10; deep drill 12.S3 |
| `PROOF-DISCRETE` | **T.Disc** | F1 Discrete JIT *application*; IAM/SQL; 12.S4 |
| `MATH-LA` | **T.LA** | 9c embeddings; 12.S5/S7 |
| `MATH-CALC-NUM` | **T.CalcOpt** | M.ML GD *uses*; 12.S9/S14 |
| `PROB-STAT-INFO` | **T.ProbStat** | language under M.ML/10.1/8.1; 12.S10 |
| `DS-ALGO` | **T.Algo** | Go G / 8.1 / Part 2 indexes; 12.S6/S8 |
| `DB-SQL` / `DB-ENGINE` *theory* | **T.SysTheory** DB | product setup stays Part 2; drills 12.S12/S13 |
| `SEC-AUTH` *theory* | **T.SysTheory** Security | product controls Part 4/7; drills 12.S19 |
| `ARCH-HLD-LLD` / `DIST-OPS` *formal* | **T.SysTheory** Distributed / Reliability / Net | studios Part 8; net Part 6; SLO 10.1 |
| `ML-CORE` *learning theory* | **T.MLTheory** → M.ML / 9c | classical zoo 9c; IPS/ERM M.ML; 12.S11 skip-test |

## B.2 Theory prerequisites map (main owner → required T.* tier)

| Main-track owner | Required T.* (confirm or skip-test before / with) |
|---|---|
| **F1** Discrete JIT + network vocab | T.Disc HS; T.Quant HS |
| **F2–F4** cloud literacy | T.Alg HS; T.Disc HS sets/predicates |
| **F3** scope (global/regional/zonal) | T.Quant HS — **not** VPC/subnet or T.SysTheory Net UG |
| **M.NS** | T.Quant HS; binary/powers-of-two (T.Disc HS) |
| **M.ML** | T.Alg HS→UG; T.ProbStat HS→UG; T.CalcOpt UG gradients JIT |
| **M.TS / M.CAUSAL** | T.Alg; T.ProbStat conditional language |
| **0.1 / 8.F / 10.3** billing & napkins | T.Quant + T.Alg HS |
| **0.5 / 4.7 / 6.4** IAM & AuthZ & FW | T.Disc predicates; T.SysTheory Security UG |
| **2.x** SQL / transactions | T.Disc; T.SysTheory DB UG; T.Algo indexes |
| **6.1 / T-NET** transport | T.SysTheory Networking UG (e2e / AIMD); T.Quant RTT |
| **6.1b / 6.2** VPC / subnet | T.SysTheory Net UG (encapsulation, L2 vs L3, address+mask, subnet-as-partition, routing-as-path, isolation boundary) + T.Disc graphs |
| **8.1** scale primitives | T.Algo UG; T.ProbStat independent-trials *language*; FPR formula @ 8.1 |
| **8.B / Part 3** distributed | T.SysTheory Distributed UG→grad |
| **10.1** SLO | T.SysTheory Reliability UG; T.ProbStat rates |
| **9c / embeddings** | T.LA UG→grad; T.MLTheory as needed; metrics/IPS @ M.ML |

## B.3 The nine Block T families

### T.Quant — quantities, units, orders of magnitude
*Node:* `MATH-FUND` (units/estimation). *Feeds:* 0.1, 8.F, 10.x, F3.

- **HS gate.** SI prefixes n…G; scientific notation; order-of-magnitude *class*; unit cancel in `qty × rate`; reject `ms + MB`. → `to_seconds`, `sci`, napkin helpers → Go `units`.
- **UG gate.** Dimensional homogeneity; GiB vs GB disclosure; latency ≈ distance/speed + RTT class labels. → `rtt_ms` + order-band asserts.
- **Grad-as-needed.** Uncertainty propagation for FinOps/SLO numerics beyond M.NS tolerance — rare.
- *Sources:* OpenStax *Prealgebra* / quantitative literacy.

### T.Alg — algebra through inequalities, functions, composition
*Node:* `MATH-FUND`. *Feeds:* modeling everywhere (0.1, M.ML \(f\), 0.4/Part 3 composition).

- **HS gate.** Linear solve; proportions; % ↔ fraction; inequalities as ceilings; function = unique output; rise/run.
- **UG gate.** Domain/codomain/range; false-inverse counterexample; composition on finite maps; logs/exponents for orders; piecewise defs.
- **Grad-as-needed.** Abstract-algebra slogans only if a force needs pipeline monoid rigor.
- *Sources:* OpenStax *Algebra and Trigonometry* / *Precalculus*; Hall & Knight as used.

### T.Disc — logic, sets, proofs, counting, graphs, invariants, asymptotics
*Node:* `PROOF-DISCRETE`. *Feeds:* F1 Discrete JIT, IAM predicates, SQL, 8.1 hash/bloom intuition, Part 3.

- **HS gate.** Sets ∪∩∖⊆; Boolean ∧∨¬ + truth table; row predicates; product rule; \(2^w\); pigeonhole; binary/hex/bit vs byte.
- **UG gate.** Direct/contrapositive/contradiction/induction; relations; counting as used; graph BFS/DFS literacy; representation invariants; big-O from a loop. → proof portfolio + tested structure with named invariant.
- **Grad-as-needed (T-TOC lite).** Automata/complexity literacy only when a main-track force needs it.
- *Sources:* Rosen *Discrete Mathematics*; Hammack *Book of Proof*; MIT 6.042J.

### T.LA — vectors, matrices, norms, least squares, eigen/SVD as used
*Node:* `MATH-LA`. *Feeds:* 9c embeddings/two-tower, PCA in zoo.

- **UG gate.** \(\mathbb{R}^n\) as used; norms; dot → cosine; matrix–vector; least squares + residual \(\|Ax-b\|\); rank/nullity on small examples. → NumPy-free kernels then NumPy compare; cosine degenerates.
- **Grad gate.** Four subspaces; QR idea; eigen/SVD; PCA reconstruction error; \(\kappa_2=\sigma_{\max}/\sigma_{\min}\). → power iteration / PCA residual.
- *Sources:* Strang *Introduction to Linear Algebra*; MIT 18.06; Trefethen & Bau / Golub & Van Loan as used.

### T.CalcOpt — limits, derivatives, gradients, convexity, GD/Lagrange
*Node:* `MATH-CALC-NUM`. *Feeds:* M.ML GD, 9c losses, T-OPT when opened.

- **UG gate.** Derivative as local linearization; chain rule on scalar losses; \(\nabla\frac12\|Ax-b\|^2\); convexity cartoon; GD with chosen step; Lagrange slogan for one equality. → FD gradient checker vs analytic; tiny GD on quadratic.
- **Grad gate.** Jacobian/Hessian as used; KKT literacy; convex vs nonconvex failure modes; duality as used by T-OPT.
- *Sources:* MIT 18.01SC/18.02SC; OpenStax *Calculus*; Nocedal & Wright / Boyd & Vandenberghe at grad; Stanford EE364A/B as used.

### T.ProbStat — probability spaces, RVs, estimation, tests, information
*Node:* `PROB-STAT-INFO`. *Feeds:* M.ML metrics *language*, M.CAUSAL conditionals, 10.1 rates, 8.1 FPR intuition.

- **HS gate.** Sample space; equally likely \(P\); disjoint additivity; independence cartoon; conditional-by-table; mean/median/percentile; rates; \(\sum\) / mean of indicators.
- **UG gate.** RV, \(\mathbb{E}\), Var; LLN/CLT statement + simulation check; MLE on Bernoulli/Gaussian; CI/test literacy; entropy/CE/KL **definitions**.
- **Grad gate.** (1) a.s. vs in-probability convergence on a concrete sequence. (2) Sufficiency: sample mean sufficient for Bernoulli \(p\) via factorization. (3) State Cramér–Rao and check a Bernoulli MLE numerically. (4) Bonferroni on a 5-test toy + one sequential-testing caveat for 9c.7. (5) Prove \(D_{\mathrm{KL}}(p\|q)\ge 0\) via Jensen; use CE/KL to explain a calibration/drift alarm.
- *Sources:* MIT 6.041SC; Wasserman *All of Statistics*; Casella–Berger; Grinstead & Snell; Cover & Thomas for info.

### T.Algo — data structures, invariant-based algorithms, complexity, hashing
*Node:* `DS-ALGO`. *Feeds:* Go G modules, 8.1, Part 2 indexes.

- **UG gate.** Array/slice/map/heap/tree/union-find contracts; loop invariants; amortized growth; hash families + collision *language*; sorting lower-bound intuition; BFS/DFS/Dijkstra as used; Master theorem on one recurrence. → **Go-first** for structures; property tests; complexity argument before code.
- **Grad-as-needed.** Hard-platform / external-memory as used by Bigtable/Spanner literacy.
- *Sources:* CLRS; Sedgewick & Wayne; MIT 6.006.

### T.SysTheory — formal models behind the main track
Product labs stay in Parts 2/4/6/7/8/10. Five subfamilies, each UG + grad-as-needed:

**Reliability (before/with 10.1).**
- *UG.* Series availability \(\prod A_i\), parallel \(1-\prod(1-A_i)\) from independence; name the independence assumption; SLI/SLO vocabulary **without** burn formula.
- *Grad.* Error-budget identity: budget = \((1-\mathrm{SLO})\times\mathrm{window}\); multi-window burn ratio as rate-of-spend; renewal/reward MTBF vs availability, one worked numeric.

**Networking (with 6.1 T-NET / before 6.1b–6.2 VPC).**
- *UG (required before VPC labs).* (1) Encapsulation — payload wrapped by successive headers. (2) L2 vs L3 with one counterexample where broadcast domain ≠ L3 subnet. (3) Address + mask → network ID and host range; prove two addresses share a partition or not. (4) Subnet as address partition — not a VPC, region, or firewall. (5) Routing as graph path — longest-prefix next hop; show a blackhole. (6) Failure domain vs trust boundary. (7) End-to-end argument + counterexample where hop-by-hop checksum is insufficient. (8) AIMD: on ACK \(w\leftarrow w+1/w\), on loss \(w\leftarrow w/2\) — simulate 20 RTTs.
- *Grad.* Little's law \(L=\lambda W\) derived from arrival/departure counts over \([0,T]\); apply to RPS × latency → concurrency. One fairness/stability trade-off of a TCP variant.
- *Sources:* Kurose/Ross or Tanenbaum & Wetherall; Saltzer–Reed–Clark.

**Distributed systems.**
- *UG.* Happens-before on a 3-process timeline (prove one pair incomparable); CAP — which two you keep under a named partition; consensus safety vs liveness.
- *Grad.* Quorum intersection for majority quorums \(\lfloor n/2\rfloor+1\); FLP impossibility (async + one crash) and why production adds timeouts/partial synchrony; linearizability vs serializability — one schedule serializable but not linearizable.
- *Sources:* DDIA + Lynch-lite / MIT 6.5840 as used.

**DB theory (with Part 2).**
- *UG.* Push a selection through a join; keys/FDs justifying 3NF on a 4-attribute toy; one dirty-read and one lost-update schedule; WAL durability argument.
- *Grad.* MVCC snapshot — given begin-ts/commit-ts of two writers, decide which version a reader sees, prove no dirty read under SI; cost-model row estimation given selectivity.
- *Sources:* Ramakrishnan/Gehrke; PostgreSQL docs; CMU 15-445.

**Security theory.**
- *UG.* STRIDE-as-used on a toy HTTP+DB diagram; authz as predicate `allow(principal, action, resource)` with a SoD counterexample; state discrete-log / factoring hardness *as used* — no cipher design.
- *Grad.* Sketch one reduction shape ("if adversary breaks X then oracle Y breaks hardness Z") for a stdlib primitive you **call**. **Never invent ciphers.**
- *Sources:* Katz–Lindell / Goldreich only if T-CRYPTO ceiling opened.

**Information & coding lite.**
- *UG/Grad.* Erasure vs replication: 3-way replication vs Reed–Solomon k-of-n — storage overhead and surviving-failure count on a toy.

### T.MLTheory — statistical learning theory as needed for 9c
*Node:* `ML-CORE` theory under. Implementations and IPS stay M.ML.

- **UG gate.** Train/test rationale; bias–variance with a derive-able quadratic example; overfitting vs generalization gap; ranking utility foundations without stealing IPS.
- **Grad gate.** (1) PAC: state \((\varepsilon,\delta)\)-learnability; sample-size bound \(m \gtrsim \frac{1}{\varepsilon^2}\log\frac{1}{\delta}\) for a finite class. (2) VC-dimension of thresholds on \(\mathbb{R}\). (3) Relate train–test gap to a complexity term. (4) ECE on a 3-bin reliability diagram. (5) Pairwise logistic/hinge ranking loss; show how a score swap changes it. (6) Covariate/label shift — broken assumption + monitoring signal.
- *Sources:* ISL 2e; Wasserman ML chapters; Shalev-Shwartz & Ben-David as used.

## B.4 Part M — quantitative prerequisites (owns specific derives)

| Topic | Complete means |
|---|---|
| Bits, integers, floats, error, tolerance | Full IEEE/conditioning/Kahan/logsumexp in **M.NS** before Part 0 |
| Functions, composition, inverse | Counterexample to a false inverse claim |
| Vectors, norms, dot, cosine | Derive cosine; degenerate cases |
| Matrices, least squares, SVD/PCA as used | Residual and reconstruction error |
| Probability: sample space, conditional-by-table | T.ProbStat owns language; M.ML owns ERM/metrics/IPS |
| Entropy, cross-entropy, KL as used | Derive CE from likelihood |
| Recurrences, Master theorem | Match a loop to a recurrence |
| Limits, derivatives, integrals as used | Derive the move; numerics with tolerance |
| Convex sets/functions, GD, Lagrange | KKT as used; not a convex-analysis PhD unless T-OPT opened |
| Sampling theorem / DFT as used | Predict aliasing (T-SIGNAL from 9c.6) |
| NumPy `ndarray` | Predict shape/dtype/strides/broadcast; copy vs view |
| Ranking / IPS / position bias | Derive propensity + Horvitz–Thompson IPS on synthetic click logs |
| Classical time series | Decompose tiny series; when BQML ARIMA/seasonal beats DL |
| Causal / uplift lite | Two-arm toy; uplift = treatment effect |

**M.NS — numerical stability.** IEEE-754 binary64/32 (sign, biased exponent, significand, subnormals, ±0/±∞/NaN); rounding modes, machine ε, ulp, \(fl(x)=x(1+\delta)\); absolute vs relative, forward vs backward error; **condition number of a problem κ vs stability of an algorithm**; catastrophic cancellation; FP add non-associativity; overflow/underflow; FMA; reformulation (`log1p`, `expm1`, `hypot`, two-sum/Kahan); \(\kappa_2(A)=\sigma_{\max}/\sigma_{\min}\), residual vs true error, Hilbert trap; **softmax overflow, log-sum-exp, scaled dot-product attention \(1/\sqrt d\)**; never `==` on computed floats; Python unbounded ints vs Go `int64` wrap; money as integer cents.
*Gate:* derive κ vs stability; predict a cancellation failure then show it in **both** languages; ship both packages.

**M.ML — empirical risk, losses, metrics (+ IPS).**
- Empirical risk \(\hat{R}(f)=\frac1n\sum_i \ell(f(x_i),y_i)\); i.i.d. fails under time/group/target leakage. A random 80/20 on time-ordered events is a defect until proven otherwise.
- MSE: \(\nabla_w \hat{R}(w)=\frac{2}{n}X^\top(Xw-y)\); GD step \(w \leftarrow w-\eta\nabla\).
- Logistic from likelihood: \(\ell=-y\log p-(1-y)\log(1-p)\), derive \(\partial\ell/\partial w=(p-y)x\).
- L2: \(\hat{R}_\lambda=\hat{R}+\frac{\lambda}{2}\|w\|_2^2\); L1 sparsity cartoon.
- Metrics implemented, not imported: precision, recall, F1, ROC/AUC as pairwise ranking probability, PR curve, **calibration / reliability / ECE**.
- **IPS / position bias:** \(\mathbb{E}[c_{i,k}]=p_k\cdot r_i\); \(\hat{R}_{\mathrm{IPS}}(f)=\frac1n\sum_i \frac{c_i}{\hat p_{k(i)}}\ell(f(x_i),\tilde y_i)\); clip propensities, report effective sample size.
*Gate:* derive log-loss gradient for one example and match code; compute P/R/F1 and one ROC point by hand; name a metric that would hide a failure in fraud vs catalog rank.

**M.TS — classical time series.** \(y_t=T_t+S_t+R_t\) (multiplicative when amplitude scales); residual ACF; **time cut only**, never a shuffle. *Gate:* decompose one series; state when classical seasonal beats DL.

**M.CAUSAL — causal / uplift lite.** Potential outcomes \(Y_i(1), Y_i(0)\); ATE \(=\mathbb{E}[Y(1)-Y(0)]\); randomization → difference in means unbiased (SUTVA caveat); observational confounding; **uplift = conditional treatment effect**, not high baseline \(Y\). *Gate:* two-arm delta by hand and in code; write "Experiments ≠ full causal" on the ledger when a case study claims observational causality.

## B.5 Overlap bans carried forward (one home per artifact)

M.NS owns IEEE/ε/Kahan/LSE/money-integer · M.ML owns ERM/losses/P/R/F1/ROC/AUC/IPS ·
M.TS owns trend/seasonality · M.CAUSAL owns potential-outcomes toy · F1 owns
IP/port/DNS/TCP/UDP/HTTP/TLS/JSON + Discrete JIT application · 8.1 owns Bloom FPR
\((1-e^{-kn/m})^k\) and ring/hash toys · 10.1 owns SLO burn-rate · Part 4/7 own auth product
controls · Part 6 owns VPC/CIDR design. **Never invent ciphers.**

---

# PART C — Bridge: spine family → ceiling

The spine is the **floor**; the ceilings are what each family needs *above* it to build
unaided. This mapping does not exist in the curriculum today — it is the join this draft adds.

| Spine family (Part B) | Already sufficient for | Ceiling it feeds (Part D) |
|---|---|---|
| T.LA UG→grad | embeddings, cosine, PCA residual | **T-REC** (MF/two-tower), **T-GRAPH** (spectral/node embeddings) |
| T.CalcOpt UG→grad | one GD step, convexity cartoon, KKT literacy | **T-DL** (backprop), **T-OPT** (LP/duality, solvers) |
| T.ProbStat grad | MLE, CLT, KL ≥ 0, multiple comparison | **T-CAUSAL** (identification), **T-RL** (regret proofs) |
| T.MLTheory grad | PAC/VC, ECE, pairwise ranking loss, shift | **T-REC**/**T-IR** (LTR objectives), **T-DL** (generalization) |
| T.Algo UG→grad | hashing, heaps, BFS/DFS/Dijkstra, external memory | **T-IR** (index construction), **T-GRAPH** (CC at scale), **T-ER** (blocking) |
| T.Disc UG | invariants, counting, graph literacy | **T-GRAPH**, **T-OPT** (combinatorial formulation) |
| T.SysTheory Distributed + DB | quorums, linearizability, MVCC, WAL | **T-MLSYS** (parallel training), **T-STREAM** (exactly-once) |
| T.SysTheory Reliability + Net | availability algebra, Little's law | **T-MLSYS** (serving economics, concurrency) |
| M.ML (+ IPS) | ERM, metrics, off-policy weighting | **T-REC**, **T-RL** (off-policy eval), **T-IR** |
| M.TS | decomposition, time cut | **T-TS** (ETS/ARIMA/hierarchical) |
| M.CAUSAL | potential outcomes, two-arm delta | **T-CAUSAL** (DAGs, IV/DiD, CUPED) |
| M.NS | LSE, softmax, \(1/\sqrt d\), tolerance | **T-DL** (stable training), **T-MLSYS** (quantization) |

**Read this as:** every ceiling in Part D already has its floor built. Nothing in Part D
asks the learner to start from zero — it asks them to climb from a gate they have passed.

---

# PART D — The ceilings (the new curation)

**What this is.** A curated **opening set** for the `T-*` ceilings the course names but never
stocks: which text and which course you enter when an owner opens that ceiling. **Index
only** — same status as Appendix M/G. Not a second spine, not a teaching order, not a
PCA/PMLE gate.

## R.1 Family → build ceiling (Appendix M counts)

| Family (n) | What "from scratch" adds beyond 9c literacy | Ceiling | Primary text | Course |
|---|---|---|---|---|
| Recommend / feed (65) | CF, implicit feedback, MF/BPR, two-tower, sequential recs, cold start, offline↔online gap | **T-REC** *(new)* | Aggarwal, *Recommender Systems: The Textbook* (Springer 2016); Leskovec/Rajaraman/Ullman, *Mining of Massive Datasets* Ch. 9 **[free]** | Stanford **CS246** |
| Search / rank / ads (36) | Index construction, BM25 → LTR objectives, query understanding; auction mechanics | **T-IR** + **T-AUCTION** *(both new)* | Manning IIR *(already Appendix I)* + Aggarwal LTR chapters; Narahari, *Game Theory and Mechanism Design* (IISc Press/World Scientific 2014); Easley & Kleinberg, *Networks, Crowds, and Markets* **[free]** | Stanford CS246 (computational advertising); **IISc E1 254**; NPTEL `noc22_cs77`; Cornell INFO 2040 |
| Forecast / ETA / demand (27) | ETS/ARIMA properly, hierarchical reconciliation, quantile loss, backtesting | **T-TS** *(new, above M.TS)* | Hyndman & Athanasopoulos, *FPP3* **[free]** (+ Python edition **[free]**) | author-hosted (Monash) |
| Fraud / trust & safety (24) | Community detection, node embeddings, GNN message passing, ring detection at scale | **T-GRAPH** *(new)* | Hamilton, *Graph Representation Learning* **[free]**; Easley & Kleinberg **[free]** | Stanford **CS224W** |
| LLM / genAI (19) | Backprop, attention, training dynamics — the derive currently out of syllabus | **T-DL** | Prince, *Understanding Deep Learning* (MIT Press) **[free]** | NPTEL **Deep Learning** (Khapra, IIT Madras **CS6910/CS7015**); Stanford CS224n |
| NLP / text / support (7) | Sequence labeling, CRF/structured prediction, eval beyond accuracy | **T-NLP** | Jurafsky & Martin, *SLP3* **[free]** (Jan 6 2026 release) | Stanford CS224n; CMU 11-711 |
| CV / video / OCR (6) | Convolution, detection, metric learning, OCR pipeline | **T-CV** | Szeliski, *Computer Vision: Algorithms and Applications* 2e **[free]** | Stanford CS231n |
| Speech / audio (3) | Sampling/STFT, CTC/RNN-T — **without** a Kaldi tooling course | **T-SIGNAL** | *SLP3* ASR/TTS chapters **[free]** | SLP3 suffices at this ceiling |
| Marketing / churn / CLV (14) | Identification, DAGs, IV/DiD, uplift, variance reduction | **T-CAUSAL** | Hernán & Robins, *Causal Inference: What If* **[free]** (Harvard); Kohavi/Tang/Xu, *Trustworthy Online Controlled Experiments* (Cambridge 2020 — CUPED) | Hernán, *Causal Diagrams* (edX) |
| Availability / inventory (5) | Watermarks, exactly-once, event-time correctness | **T-STREAM** *(new)* | Akidau/Chernyak/Lax, *Streaming Systems* (O'Reilly 2018) → Dataflow/Beam | maps to Part 2/3 products |
| ML platform / infra (2) | Parallelism arithmetic, quantization, KV-cache, serving economics | **T-MLSYS** *(new)* | Harvard **CS249r** *Machine Learning Systems* **[free]** | Stanford CS329S; MIT 6.5940 EfficientML |
| **Other (101)** — pricing, routing, ER, dims | LP/MIP + duality; VRP; record linkage; revenue management | **T-OPT** (stocked) + **T-ER** *(new)* | Bertsimas & Tsitsiklis, *Introduction to Linear Optimization*; Google **OR-Tools** docs; Talluri & van Ryzin, *Revenue Management* (Springer 2004); Christen, *Data Matching* (Springer 2012) | MIT 15.053; Stanford EE364A *(Boyd already Appendix I)* |

## R.2 Cross-cutting: bandits → RL (Recommend, Search, pricing)

9c.2 owns bandit **literacy**; the derive ceiling is unstocked. Entry path:

1. Lattimore & Szepesvári, *Bandit Algorithms* (Cambridge 2020) **[free]** — regret proofs,
   UCB/Thompson sampling, contextual bandits, off-policy evaluation.
2. Sutton & Barto, *Reinforcement Learning: An Introduction* 2e (MIT Press) — MDPs, Bellman,
   policy gradient.

Courses: **IISc E1 245** *Online Prediction and Learning* (ECE — uses Lattimore as text);
NPTEL **Reinforcement Learning** (Ravindran, IIT Madras, `106106143`); Stanford CS234.
Floor: **T.ProbStat grad** (concentration) + **M.ML IPS**. Off-policy evaluation connects
back to M.ML IPS — that gate stays at M.ML, not here.

## R.3 IIT / IISc institutional track (free, ties to Appendix I)

| Ceiling | Indian-institution source |
|---|---|
| **T-DL** | NPTEL *Deep Learning* — Khapra, IIT Madras (**CS6910/CS7015**); IIT Ropar offerings also live |
| **T-RL** | NPTEL *Reinforcement Learning* — Ravindran, IIT Madras (`106106143`) |
| **T-AUCTION** | **IISc E1 254** *Game Theory* — Narahari; NPTEL `noc22_cs77`; text *Game Theory and Mechanism Design* (IISc Press) |
| bandits / online learning | **IISc E1 245** *Online Prediction and Learning* (ECE) |
| **ML-CORE** theory recall | **IISc E0 270** *Machine Learning* (CSA) |

Appendix I keeps the systems/theory cores (H&P, Silberschatz, Kurose, Sipser, CLRS) — not
duplicated here. Narahari is the single best fit for the ads-auction gap that 9c.0 defers as
"no mechanism-design PhD": his auction chapters are exactly the bid × quality, GSP/VCG,
sponsored-search layer the Search/ads family needs, and stop well short of a degree.

## R.4 Appendix T chapter-map extensions (entered only when the ceiling opens)

| Text | Enter through |
|---|---|
| MMDS 3 (LSH/ANN), 6 (association), 9 (recsys), 12 (large-scale ML) | T-REC / 9c.2 candidate generation |
| Aggarwal RecSys 2–3 (CF), 7 (evaluation), 13 (bandits/LTR) | T-REC |
| Hamilton GRL 2–3 (node embeddings), 5–6 (GNN) | T-GRAPH / 9c.4 rings |
| Prince UDL 6–7 (training/backprop), 12 (transformers) | T-DL *(only if the out-of-syllabus line is lifted)* |
| SLP3 ASR + TTS chapters; sequence-labeling chapters | T-SIGNAL / T-NLP / 9c.6 |
| Szeliski 5 (deep learning), 6 (recognition), 7 (features) | T-CV / 9c.6 |
| FPP3 3 (decomposition), 8 (ETS), 9 (ARIMA), 11 (hierarchical) | M.TS → T-TS → 9c.3 |
| *What If* 1–3 (no models), 6–7 (DAGs/confounding), 14–16 (IV) | T-CAUSAL |
| Lattimore 4–9 (stochastic/UCB), 18–19 (contextual) | T-RL entry / 9c.2 |
| CS249r MLSysBook: training, optimizations, serving, ops chapters | T-MLSYS / 9c.7 |
| Bertsimas 1–4 (LP/duality); OR-Tools routing + CP-SAT guides | T-OPT / "Other" pricing + routing |

## R.5 Still out, even with Part D open

Kaldi/OpenFst tooling courses; CV beyond Szeliski's recognition chapters; convex-analysis
PhD; mechanism-design PhD beyond Narahari's auction chapters; five-portfolio GenAI tracks;
re-implementing the 309 blogs. Appendix M stays a **309-line index** — Part D stocks the
shelf, it does not add lessons.

---

# PART E — Source links (verified 2026-09-16)

## Spine sources (Part B — already named in the curriculum)

OpenStax *Prealgebra* / *Algebra and Trigonometry* / *Calculus* · Hall & Knight · Rosen
*Discrete Mathematics* · Hammack *Book of Proof* **[free]** · MIT 6.042J · Strang +
MIT 18.06 · MIT 18.01SC/18.02SC · Nocedal & Wright · Boyd & Vandenberghe **[free]** ·
Stanford EE364A/B · MIT 6.041SC · Wasserman *All of Statistics* · Casella–Berger ·
Grinstead & Snell **[free]** · Cover & Thomas · CLRS · Sedgewick & Wayne · MIT 6.006 ·
Kurose/Ross · Tanenbaum & Wetherall · Saltzer–Reed–Clark · DDIA · MIT 6.5840 ·
Ramakrishnan/Gehrke · CMU 15-445 · Katz–Lindell · ISL 2e · Shalev-Shwartz & Ben-David
**[free]** · Higham · IEEE 754.

## Ceiling sources (Part D — new this pass)

| Resource | Link |
|---|---|
| Mining of Massive Datasets **[free]** | http://mmds.org |
| Stanford CS246 | https://web.stanford.edu/class/cs246/ |
| Aggarwal, *Recommender Systems* | https://www.charuaggarwal.net/Recommender-Systems.pdf |
| Stanford CS224W | https://cs224w.stanford.edu/ |
| Hamilton, *Graph Representation Learning* **[free]** | https://www.cs.mcgill.ca/~wlh/grl_book/ |
| Easley & Kleinberg **[free]**, Cornell | https://www.cs.cornell.edu/home/kleinber/networks-book/ |
| Narahari, IISc — Game Theory Lab | https://gtl.csa.iisc.ac.in/hari/ |
| IISc E1 254 Game Theory | https://iisc.ac.in/wp-content/uploads/2017/12/E1254.pdf |
| NPTEL Game Theory & Mechanism Design | https://onlinecourses.nptel.ac.in/noc22_cs77/preview |
| Hyndman & Athanasopoulos FPP3 **[free]** | https://otexts.com/fpp3/ |
| FPP — Python edition **[free]** | https://otexts.com/fpppy/ |
| Hernán & Robins, *What If* **[free]** | https://miguelhernan.org/whatifbook |
| Lattimore & Szepesvári **[free]** | https://tor-lattimore.com/downloads/book/book.pdf |
| IISc E1 245 (uses Lattimore) | https://ece.iisc.ac.in/~aditya/E1245_Online_Prediction_Learning_F2018/ |
| NPTEL Reinforcement Learning (Ravindran) | https://nptel.ac.in/courses/106106143 |
| NPTEL Deep Learning (Khapra) | https://onlinecourses.nptel.ac.in/noc19_cs85/preview |
| IIT Madras CS6910/CS7015 | https://www.cse.iitm.ac.in/~miteshk/CS6910.html |
| Prince, *Understanding Deep Learning* **[free]** | https://udlbook.github.io/udlbook/ |
| Jurafsky & Martin SLP3 **[free]** | https://web.stanford.edu/~jurafsky/slp3/ |
| Szeliski CV 2e **[free]** | https://szeliski.org/Book/ |
| Harvard CS249r MLSysBook **[free]** | https://mlsysbook.ai/book/ |
| Stanford CS329S | https://stanford-cs329s.github.io/ |
| Google OR-Tools | https://developers.google.com/optimization |
| Christen, *Data Matching* | https://link.springer.com/book/10.1007/978-3-642-31164-2 |
| Talluri & van Ryzin, *Revenue Management* | https://link.springer.com/book/10.1007/b139000 |
| IISc E0 270 Machine Learning | https://sml.csa.iisc.ac.in/Courses/Spring25/E0_270/JAN-2025.html |
