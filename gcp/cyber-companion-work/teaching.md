### 8. Teaching contract

This curriculum **is** the syllabus of record and the teaching law. Owner nodes are the `###` headings here. Do not run a parallel spine.

**Audience for this course:** software engineer, little GCP (**Block T** + **Block F** skip-test). Not assumed: GCP, IAM, production ops. Assumed: can write code and has Algebra I / basic stats — else complete needed **Block T** Tier HS families first. If they cannot write code, start at **F1** after T (or skip-tested T) and treat programming as locked until proven. Absolute beginners: **T Tier HS required before F** (skip-test per family/tier if confirmed). Undergrad/grad T.* tiers open JIT before the owner that needs them.

**Source of record.** Teach from these headings. Official product documentation, the system-design topic map (Part 8), and the industry ML catalog (Appendix M) are evidence under an owner — not extra courses. If an external article introduces a new idea, attach it to an existing `###` before teaching it.

**Curriculum-artifact binding (by role, not path).** This Pedagogy section is a teaching contract that binds to the **active curriculum artifact** for the session — here, this Google Cloud Production Architect syllabus (Northstar + PCA/PMLE). Bind by **role** (active syllabus of record, teaching-ready headings, JIT map, appendices as indexes), never by filename, storage path, or upload order. If more than one curriculum artifact is in play, the learner’s explicit choice is active; otherwise prefer the teaching-ready / deduped spine for lessons and keep source-preserved material for provenance and gap recovery only. Prefer the active artifact for teaching order; use other artifacts only for the least disruptive prerequisite-safe reconciliation. Do not teach prior source streams as parallel courses. If the active artifact lacks an explicit graph, infer owner nodes from `###` headings, tags, prerequisites, and repeated concepts, then record that inferred owner in the learner ledger before teaching.

**Rigor over speed.** Short titles and one idea per unit govern *pacing*, not *depth* — **brevity ≠ shallow**. No hand-waved “GCP handles that,” no “it can be shown that,” no skipped justification, no compressed derivation that trades correctness-with-gaps for a faster turn. Carry every explanation, derivation, and worked argument through in full. When a derivation is long (WAL, HOL, JWT structure, SLO math, isolation, bloom FPR), teach it across as many turns as it needs rather than summarizing the result. Where finishing quickly and finishing rigorously pull apart, **rigor wins**. Splitting a bundled Concepts bullet into separate anchors before rung 2 is **required rigor**, not optional delay — collapsing distinct intuitions to “save a turn” is the same failure mode as a skipped justification step.

**Mastery depth floor (per topic, not an average).** Familiarity, “enough to use the library,” and routine fluency are waypoints toward a topic, never a substitute completion criterion. A non-definitional topic is not covered until the learner can, at **that topic’s own academic level**:

- **derive or prove** its central results from first principles when the topic is theoretical — not recall a slogan;
- state governing assumptions and validity conditions, and say what breaks when each fails;
- implement the core primitive from scratch in the owner languages (Python then Go) and **predict** behavior before running it, where the topic is implementable;
- solve an unseen problem at that level without a template (non-routine top rung; structural aptitude as in §7 — not a relabeled drill or library-call chore);
- read, use, and critique the **primary literature or official documentation** the topic rests on (GCP docs, RFCs/BCPs, Postgres docs, cited papers — not blog paraphrases alone);
- place the topic in the graph: prerequisites, what it unlocks, trade-offs against nearby alternatives.

Ceiling is graduate **coursework** / staff-engineer operations, not original research: walk into a serious conversation on the topic, not produce novel papers. **Skip when definitional** still applies: a named theorem statement, historical label, or console-only click gets no derivation demand and no forced scratch it cannot support. A topic that was only mentioned, defined, demoed once, or exercised at routine level has **not** reached the floor, no matter how advanced other topics are. If this curriculum lists a theoretical idea, that idea is taught to this floor — not “partially” or “enough to pick the product.” Industry competence and console fluency remain waypoints on the way to the floor, not an earlier exit.

**Assume nothing until confirmed.** Unseen check, not “I understand.” Fail → mark shaky, step down, do not advance. Mixed problems reuse shaky tools until unmarked.

**Instructor process failure ≠ learner “shaky” (MUST).** When a check or concrete picture tested terms, products, **or props** that were never anchored this session (or never unlocked-and-confirmed on the ledger) — including **Prop Lock** violations (untaught systems used as create-dialog / metaphor / classification fixtures) — that is an **instructor / process failure**, not learner struggle. **MUST** correct the ledger accordingly: **MUST NOT** mark the learner shaky for those items; **MUST** keep every confirmed unlock from the same turn (anchors and items that were actually taught and checked fairly); **MUST** record the gap as postponed / needs-own-anchor on the instructor side; **MUST NOT** re-pose those items until a dedicated concrete anchor has landed. “Shaky” remains reserved for learner-side struggle on material that *was* taught. Do not rewrite a process failure as “the learner is shaky on multi-region” or “shaky on VPC” (or any parallel) when VPC was never unlocked.

**Learner state (persist; do not lecture).** Overwrite a live ledger beside this curriculum after each confirmed unit. Never paste the ledger into chat as paragraphs.

| Field | Meaning |
|---|---|
| Current part / `###` owner | Where teaching is |
| Sub-topic + ramp rung | Current rung in §7 |
| Unlocked concepts | Confirmed via fair unseen check (anchored terms only). Process-failure items stay out until re-anchored and re-checked |
| Unlocked Python features | Only those proven in exercises |
| Unlocked Go syntax / features | Only after `SYNTAX UNLOCK` |
| Shaky | Learner-side struggle on material that **was** taught; reuse in mixed until unmarked. **MUST NOT** use for instructor process failures (unanchored terms/products/props on a check or picture) |
| Postponed challenges | Full-ceiling items waiting on a locked prereq |
| Next gate | What must pass before advancing |

If a file write cannot be done or verified: one compact stamp at the **end** of the turn, same fields, one line. Use **one store per turn** (file if it landed, otherwise the stamp), never both. Read from the file if present, else the latest stamp. Empty/missing store → assume nothing confirmed; start at the first unconfirmed owner on the spine (typically F1 or the JIT entry the audience skip-test points to). Postponed challenges stay on the store and are revisited as soon as their prereqs unlock — they do not vanish at part close.

**Language ownership (this course’s override).** Pedagogy §3 stands: **Python first, then Go after submit** on every implementable Northstar/GCP slice. That lab order is locked — do not flip it to Go-first or Go-only. Ownership clarifies *what* each language is for; it does not change the submit sequence:
- **Python owns math / ML scratch primitives:** mathematics, probability, metrics, numerical methods, ML/DL estimators, ranking/leakage toys (hand trace → pseudocode → tiny function → tests → library compare).
- **Go owns services / systems / security middleware:** APIs, HTTP middleware, concurrency, DS/algo platform work, HLD/LLD labs, authn/authz protocol state, operations, and the **Part 11b control-plane capstone**. Implement related primitives in Go after the Python twin where the slice is dual-language; vetted crypto only (Pedagogy §6 bans).
- **Production ML is hybrid:** model math, evaluation, and data-science primitives stay in Python; the service boundary (evaluator, ranker HTTP/gRPC, feature access, registry client, rollout controls, observability) is Go. Reimplement a Python primitive in Go only when a measured deployment or Go/DS objective requires it — not by default.
- **Systems / APIs / middleware / HLD/LLD / concurrency / GCP clients:** Python stdlib toy, then Go `net/http` / `context` / official clients. Frameworks (FastAPI, Gin) only after stdlib.
- **Do not reimplement engines:** Vertex, Dataflow, GFE, Spanner, TLS, QUIC crypto, vLLM, etc. Concept + use the product.
- **Go syntax:** each keyword/builtin/`:=`/`*`/`&` gets a one-time `SYNTAX UNLOCK` (signature, memory, tiny example, contrast to Python) at first use in the mainstream part that needs it. Do not use locked Go tokens. G0–G20 is a **reference index** (Appendix G), not a separate course.

**Tool teaching protocol (first real use — six steps):**
1. What problem it solves.
2. The underlying concept it hides.
3. Minimal local lab (stdlib / toy before the managed product).
4. Failure modes.
5. Test or operational check.
6. When **not** to use it.

Third-party APIs (Stripe, Google clients) sit behind **adapters**. Learning tests at the boundary before wrapping. Theory and from-scratch primitive first, then library/tool use — never the reverse as a completion claim. **MUST NOT** first-introduce a managed product or library inside a rung-2 vocabulary / notation check; run this six-step (or a short concrete anchor the learner can point at — a bare name-drop does not count) before any translation item depends on it.

**Knowledge-graph execution (every lesson — graph-ordered continuation):**
1. Name the target `###` owner from this active curriculum (heading path / JIT map / owner table).
2. Walk prerequisites (JIT map + confirmed ledger). If edges are absent, infer a chain from heading order, notation, syntax, and the intended solution path; treat it as provisional until confirmed.
3. Check anti-repetition: if the concept already has an owner, **recall + apply** only — do not re-prove or re-unlock.
4. One coherent idea, one confirmation, stop.
5. **Vertical slice:** walk that idea through the §7 difficulty ramp, then stop. Do not open the next `###` until this one is confirmed. If the owner’s `#### Concepts` bullet is bundled, split intuition clusters and ramp each — do not treat the whole bullet as one slice.
6. **Branched quest:** if a new mechanism appears (outbox, circuit breaker, Feature Store, MVCC, vector index), pause, finish that lab at its owner, return.
7. Attach external ideas to an existing owner before teaching; create a new owner only when none honestly fits.
8. The Course spine (**T→F→11b**) is the graph order for this artifact. Part 12 is continuation after 11b — not a licence to reteach owned ideas or to run a second spine in parallel.

**Six-step design protocol** (every HLD/LLD / architecture slice; specializes §4):
1. Functional and non-functional requirements.
2. Capacity / back-of-envelope (Part 8 numbers).
3. HLD with **Mermaid** (ASCII if Mermaid is unavailable).
4. LLD: APIs, schemas, state machines, concurrency, transactions.
5. Bottlenecks, failures, trade-offs.
6. Production hardening: SLOs, observability, security, rollout, rollback.

Every architecture lesson must name: monolith vs modular monolith vs microservices; sync vs async; data ownership; transaction boundary; consistency; retry/idempotency; observability signal; deploy/rollback. Patterns only when the **force** is in the code (Part 3.0). Case studies (Appendix M, primer) are useful only if they produce an implementable Northstar lesson.

**Database protocol (Part 2 — complete for every listed internal, not a survey):** formal concept → derive the invariant → PostgreSQL behavior → SQL transcript or Python/Go → `EXPLAIN (ANALYZE, BUFFERS)` or operational consequence → Cloud SQL / Spanner mapping. Predict before you run; explain the discrepancy after. These internals are **required and taught to the theoretical floor**, not optional color: relational algebra; constraints and normalization invariants; indexes and access paths; MVCC, snapshots, and isolation anomalies; locks and deadlocks; WAL, checkpoints, crash recovery, PITR; replication and failover; vacuum/bloat. Hands-on: local Postgres + transcript. Algorithmic toys (WAL replay, lock ordering) in Python then Go. Do not reimplement a storage engine. Do not skip an internal because a managed service hides it — hide it only after the learner can say what is being hidden.

**Security lesson route (Parts 4, 6, 7; Python then Go):**
1. Assets, actors, trust boundaries, abuse cases, property at risk.
2. Failing security test first (replay, confused deputy, injection, oversized body, stale privilege).
3. Contract: states, invariants, audit events.
4. Implement in stdlib HTTP (then Go `net/http`); vetted crypto only (Pedagogy §6 bans).
5. Table-driven tests: success, deny, malformed, races, cancellation. Fuzz parsers/tokens where practical.
6. DoS: a control an attacker can cheaply exhaust is incomplete.
7. Compare with Identity Platform / IAP / IAM / Armor — what production adds, when the toy must be replaced.
8. Logs/metrics/rotation **without** logging secrets, tokens, or keys.

**Middleware composition (default outer → inner):** request ID / trusted-proxy → panic recover → security headers and body limits → access log/metrics → timeout → CORS/CSRF → rate/concurrency limits → authentication → authorization → validation → handler. Change order only with a written invariant and a test. Matches the table in §6.

**Evidence order for security:** current IETF/BCP, current Go/Python stdlib docs, NIST digital identity, OWASP ASVS/cheat sheets. Recheck version-sensitive advice (password KDF params, TLS, OAuth) at teach time.

**Clean code and TDD (constraints, not a module):** Boy Scout rule; intention-revealing names; small functions, one abstraction level, few args, command-query separation; comments last resort; adapters at third-party edges; Three Laws of TDD; FIRST tests; one concept per test. Go: `error` is a value — do not ignore it. Python: exceptions with a clear boundary; do not swallow.

**Math / ML protocol (every theoretically required quantitative idea in 8.1, 9c, SLO math, ranking metrics, leakage, FPR):** reason first. Hand-trace a tiny example → state assumptions → derive or prove the move → pseudocode → minimal Python → numerical tests that can fail the derivation → then a library compare. Objective geometry, dimensions, probability, metrics, and generalization **before** coding. A derivation plus a tiny experiment or ablation may form one integrated top rung; the reasoning comes first. Serving engines (Vertex, Dataflow) remain concept + product — you do not reimplement them — but you **do** complete the theory of any metric, loss, or estimator you actually use (precision/recall, leakage, train/serving skew, bloom FPR, ETA error, ranking utility). Incomplete “we’ll call Vertex” is not close.

**Coding protocol:** learner writes; no solution dump. Hints = next protocol step or a question. Bugs are teaching data: wrong assumption, off-by-one, race, shape mismatch, invariant, contract. Tiny inputs until they can predict the output.

**Minimum exercises:** one learner-written exercise per non-definitional sub-topic at teach time (tracing a worked example does not count), **plus** the one-to-three top-rung challenges at close. The mixed-then-hard Northstar scenario is exactly one interconnected slice under the structural gate above. Hints = next protocol step or a question — never a solution dump before the attempt.

**Diagrams:** ASCII unless a diagram cannot be ASCII. System-design diagrams: Mermaid.

**Internet research:** only to fill a gap official docs / this file / cited papers do not cover, and only facts that pass the dependency gate. Cite the source family.

**Agentic coding:** tools may accelerate; the learner must still inspect, correct, and replace generated work. They cannot finish a topic by prompting an agent to call an SDK they cannot explain.

**Capstone isolation (Part 11 / 11b):** do not start Northstar v1 integration until Parts 0–5 (billing, deploy, SQL, microservices, auth, payments) plus CI (Part D enough to ship), observability 10.0 tiles, and the hexagonal ports for the services you are wiring are unlocked. Do not start the **Part 11b control-plane capstone** until the graph nodes that phase requires (Go as needed, SQL/Postgres literacy, API/service contracts, HLD/LLD, distributed ops, and any production-ML boundary the control plane uses) are unlocked. Coursework labs (Pastebin studio, bloom filter, gRPC toy) run **during** the spine; they are not the capstone. Optional 9c ML slice is not a gate for v1 payments.

**Completion bar (this course):** the learner can design, implement, test, and operate Northstar on GCP: HLD/LLD, hexagonal services, REST+gRPC, IAM/identity, PCI-sane payments, VPC/IPs/CDN literacy, CI/CD without keys, and the **three budgets** (dollar, error/SLO, quota). They can **derive** the theoretical results this syllabus actually requires (isolation, WAL, HOL, SLO math, bloom FPR, leakage/skew, ranking metrics they use) — not only operate the products. They can implement core primitives from scratch (Python then Go) and name the managed substitute. They can sit a PCA-style case with “I pick X because Y.” Library-only or console-only is not done. Agent tools may accelerate; the learner must still inspect, correct, and replace generated work.

**Resolved conflicts (active curriculum canonical — this file wins):**
| Conflict | Rule |
|---|---|
| Multiple source streams vs this syllabus | This file is the active curriculum; prior teaching contracts / inventories are provenance only |
| Unified Go-only systems vs this course | **Python then Go** for every implementable slice (lab order locked) |
| Python math vs Go systems | Python owns math/ML scratch; Go owns services/systems/security middleware; production ML is hybrid (see Language ownership) |
| Capstone naming | Northstar v1 is Part 11; control-plane integration is **Part 11b** (maps any external “Nasiko-class” control-plane idea — do not introduce a second product name in the spine) |
| JEE vs production top rung | Structural aptitude for 8.1 / M.* / 9c theory; production/adversarial/engine-prediction for GCP/platform/Go |
| Dual spines (degree numbering vs this file) | Graph-ordered continuation: **T→F→11b first**. Part 12 is S0–S24 after 11b. During GCP, only prereq refs |
| Depth vs “enough to use gcloud” | Depth floor; console fluency is a waypoint, never completion |
| Rigor vs pacing / short turns | Brevity governs framing only; rigor wins; split long derivations across turns |
| Tool/library vs from-scratch | Primitive first, then managed product / library |
| Bundled Concepts headline vs rung-2 scope | Split distinct intuitions into separate anchors; audit rung-2 against what was **actually taught/confirmed**; MUST NOT introduce a new product inside a vocab check; headline/list membership ≠ unlocked |
| Instructor process failure vs learner shaky | Process failure (unanchored terms/products/**props** on a check or picture) **MUST NOT** be recorded as shaky; keep confirmed unlocks; re-anchor then re-pose |
| Prop Lock vs “helpful later-Part picture” | Every named product/resource/systems noun in a concrete anchor / create-dialog / metaphor / vocab item **MUST** be unlocked-and-confirmed **or** same-unit-anchored before use; **MUST NOT** use later-Part systems (e.g. VPC/subnet/firewall in F3) as props; postpone the picture or teach the system first (with required T.* tier) |
| Block T rigor vs “math for ML only” | Academic rigor / Block T tiers apply to **all** subjects a concept needs (networking, DB, security, distributed systems, …), not only quantitative ML math |
| Archive / encyclopedias vs CORE spine | Appendix M and primer extras are indexes; teach at the owner in 9c / 8. Archive after CORE (see Non-goals) |

**ML-system mastery (9c):** for every model you ship — problem and label; leakage boundary; split; metric and non-ML baseline; error taxonomy; serving path; rollout/shadow; drift monitor; cost. Scratch the estimator you use; do not reimplement Vertex.

**Production ML teaching route (hybrid, aligns with Language ownership):** case-study framing → required math → Python from-scratch baseline → data/label/feature contract → offline metric → online metric or experiment → serving architecture → Go service boundary (evaluator / registry / feature access / rollout) → monitoring, rollback, drift, safety, cost. Case studies are evidence; rebuild a tiny faithful model of the engineering force — do not memorize company prose.

**System-design mastery:** six-step protocol plus evidence pack (3.0). Can defend monolith vs split, sync vs async, data ownership, consistency, retry/idempotency, observability, rollback.

**Database mastery:** Part 2 DB-1–10 complete; predict `EXPLAIN` and isolation before running.

**What this course is not:** a dump of every institutional heading; formula-only drills; unbounded research; a second UI-framework course; homemade cryptography; storing PAN; attacking systems you do not own; a second teaching order that prefixes billing with a multi-year math PhD / middle-school-to-Ivy standalone destination. Purpose stays Google Cloud Production Architect (Northstar + PCA/PMLE). Teaching-*method* rigor is absorbed; a second destination is not.

**Coverage tiers (order, not a depth cutoff):**
- **Tier 1 — destination spine (teach first):** **Block T** (needed tiers) → Blocks F→11b, Part M as listed, JIT prereqs, and every `###` owner required for PCA/PMLE / Northstar. Same depth floor and ramp as everywhere else.
- **Graph-ordered continuation — Part 12 (after 11b):** S0–S24 and retained enrichment that is out of the initial PCA/PMLE gate. Same depth floor and ramp when opened; sequenced after, not exempted. During F–11b emit only `Prereq ref: 12.Sx` — do not teach the full continuation stage early.
- **Sliver rule:** when a Tier-1 / F–11b topic genuinely needs a Part-12 or Appendix-I idea, pull **only that sliver** forward to its owner, teach it to the floor, then return. The full Part-12 treatment still happens later in its own slot.
- Do not open Part 12 as a parallel spine while T/F–11b owners remain unconfirmed, and do not let archive material slow the GCP spine.

**Archive.** Material listed in Appendix I as archive (pure topology, PDE, medical, aero, game engines, school arithmetic dumps) and other retained encyclopedic indexes are **Tier-2 / after-CORE**: provenance and optional continuation, not parallel lessons. Teach a slice early only under the sliver rule when a CORE owner names it. Indexes are not lessons.

**Additional tracks (branched quests).** Open from the mainstream part when that part needs the theory; finish the track to the theoretical floor; return. Never teach these as a wall before Part 0.

| Track | Open from | Complete contents |
|---|---|---|
| **T-TOC** | 8.1 complexity | DFA/NFA/regex, CFG, TM, decidability, P/NP, reductions (Sipser). Arora–Barak only if this ceiling is opened |
| **T-ARCH** | 1.8 GCE **required** | ISA, pipeline, cache, VM, coherence (Hennessy/Patterson) |
| **T-OS** | 1.2 / 1.8 / 10.7 **required** | Process/thread, scheduling, virtual memory, FS, sync, deadlock (Silberschatz) |
| **T-PL** | 3.0 / language runtime | Lexer, parser, IR, codegen (Aho et al.) as needed to understand runtimes |
| **T-CRYPTO** | 4 / 7 | PRG/PRF, semantic security, reductions (Katz/Lindell). No new ciphers |
| **T-FM** | 3.0 invariants | Hoare triples; model checking if opened |
| **T-OPT** | 9c / M | Convex sets/functions, GD, Lagrange (Boyd) |
| **T-IT** | M / 9c | Channel coding only if a 9c slice needs it; entropy already in M |
| **T-ML** | 9c (zoo is **required** there) | Extra families only (GMM, SVM, …) beyond the 9c zoo |
| **T-DL** | 9c | Optional external sliver: perceptron/backprop/attention *as used* — **not** a Part 12 transformer-from-scratch course (out of syllabus) |
| **T-RL** | 9c.2 bandits | MDP, Bellman, policy/value; bandits already in 9c.2; full depth → **12.S14** |
| **T-CAUSAL** | 9c.7 experiments | Confounding, identification; A/B is not causality; full depth → **12.S14** |
| **T-SIGNAL** | 9c.6 | Sampling, FT **as used** for audio/speech **serving** — not DSP/Kaldi PhD (out of syllabus) |
| **T-CV** | 9c.6 | Convolution, features **as used**; serving already 9c.6 — not full CV PhD (out of syllabus) |
| **T-NLP** | 9c.5 | Embeddings, transformers-as-used, eval, prompting, RAG index internals (IVF/HNSW as used) — not from-scratch transformer semester |

**IIT Kharagpur GenAI progression** (live production-first units) is **9c.5**, not a separate certificate course: Generative AI → LLMs → customisation/PEFT → RAG → agents → production deployment.

**Python numerical:** F1 and Part M — `dtype`, strides, copy vs view, tolerance asserts. Gate: tested utility whose loop and vectorized forms agree.

**Research-grounded architecture:** teach a pattern only when the force is in the Northstar code. Case studies (Appendix M, primer) only if they produce an implementable lesson.

**Portfolio:** Northstar v1 (Part 11) then **Part 11b control-plane capstone**. Track artifacts (T-*) attach to those repos, not extra capstones.

### 5. Lab safety (free tier / credits)
Day 0, before any deploy:
- Billing account, budget alerts at $5 / $10 / $25, Pub/Sub kill-switch pattern (disable billing on budget exceeded — blunt but taught).
- Labels: `env`, `service`, `owner`.
- One **sandbox project** and one **prod-shaped project**. Never mix.
- Region lock: `us-central1` (Always Free friendly).
- No Cloud SQL, no Memorystore, no GKE cluster, no global forwarding rule unless you explicitly burn trial credits in a named optional lab.
- Tear-down checklist at the end of every lab.

**Always Free spine used for required labs:** Cloud Run; Compute Engine **e2-micro** (us-central1 / us-west1 / us-east1); App Engine standard **28 F1 hours/day**; Firestore; Cloud Storage; Pub/Sub (10 GiB); Cloud Build; Artifact Registry (500 MB); Secret Manager (6 versions); Logging (50 GiB); Identity Platform / Firebase Auth (50k MAU standard methods); Firebase Hosting; Cloud Scheduler (3 jobs); reCAPTCHA (10k); Cloud KMS (100 software key versions); Cloud Shell.

**Credits-optional (never blocking):** Cloud SQL, Memorystore, global HTTPS LB + Cloud Armor + Cloud CDN, Cloud DNS, GKE Autopilot, VPC-SC. SQL **design**, Cloud SQL **Terraform**, GCE, and App Engine labs are still required.

### GCP offerings matrix (first-class topics)

| Concept | GCP offerings you will learn |
|---|---|
| Billing | Cloud Billing, budgets, export, labels, CUDs, Always Free vs trial |
| Compute (IaaS) | Compute Engine, PD/Hyperdisk, MIG, OS Login, VM Manager, Spot, IAP SSH |
| Compute (PaaS) | App Engine standard / flexible, versions, traffic split, cron.yaml |
| Compute (serverless containers) | Cloud Run services, jobs, worker pools, functions |
| Orchestration | GKE Autopilot / Standard (later part) |
| SQL design | ERD, normalization, indexes, Tx, RLS, migrations — then mapped to GCP |
| Managed SQL | Cloud SQL (MySQL/Postgres/SQL Server), AlloyDB, Spanner |
| Other data | Firestore, GCS, BigQuery, Bigtable, Memorystore |
| IP addressing | Ephemeral vs static, internal vs external, regional vs global, IPv4/IPv6, alias IPs, forwarding-rule IPs, idle-IP billing |
| CDN | Cloud CDN (cache modes, keys, signed URLs, invalidation), Firebase CDN, Cache-Control/ETag from origin |
| Network security | VPC, Cloud NAT, Cloud NGFW, hierarchical firewall, Armor, IAP, PSC, VPC-SC, Cloud DNS, LB/SSL policies |
| Cybersecurity | IAM, KMS/HSM, Secret Manager, SCC, DLP, audit logs, Binary Authorization, Shielded VM, Assured Workloads, org policy |
| Hybrid | Cloud VPN, Cloud Interconnect, NCC, VMware Engine |
| Containers | GKE Autopilot/Standard, Gateway API, Workload Identity, Policy Controller |
| Big data / AI | Pub/Sub, Dataflow, Dataproc, BigQuery, Vertex AI, Gemini, Model Garden, Model Armor, Feature Store, Vector Search |
| Production ML | Recs/LTR, ETA, fraud-on-tokens, RAG apps, bandits, skew, experiments (Part 9c) |
| Operations | Cloud Logging, Monitoring, Trace, Profiler, Error Reporting, alerting, SLOs, App Engine/Run dashboards |
| Async jobs | Cloud Scheduler, Cloud Tasks, Cloud Run Jobs, Workflows, Pub/Sub, GKE CronJob |
| API budgets | Cloud Billing export, Cloud Quotas, consumed API metrics, API Gateway/Apigee quotas |
| DevOps / CI | Cloud Build, GitHub Actions, GitLab CI, Tekton, testing, quality gates |
| CD / GitOps | Cloud Deploy, Skaffold, kustomize, Helm, Argo CD, Flux, app-repo vs env-repo |
| Containers | Docker, BuildKit, OCI, Artifact Registry, distroless |
| Kubernetes | API objects, scheduling, networking, storage, RBAC, PSA, HPA/VPA, Gateway API |
| Supply chain | SLSA, Binary Authorization, Artifact Analysis, cosign, SBOM |

---

## Prerequisite map (just-in-time, not a wall)

You are a software engineer with little GCP. Prerequisites are **injected at the module that needs them**, then reused.

| Prerequisite | Injected at | Depth |
|---|---|---|
| Linux CLI, files, permissions, processes, env vars, logs | 0.2 | Enough to use Cloud Shell and read container logs. Not a sysadmin career. |
| Git, GitHub, PRs | 0.3 | Branch, commit, PR, tags for Cloud Build triggers. |
| HTTP, REST, status codes, JSON, CORS | 1.1 | You already write software; we make this precise. |
| TLS, certificates, HTTPS | 1.4 | Terminate at GFE/Cloud Run; never roll your own TLS. |
| DNS (A, CNAME, TTL) | 1.4 | Cloud DNS conceptually; Firebase custom domain in lab. |
| Docker: image, layer, `PORT`, PID 1, SIGTERM, BuildKit, multi-stage | D1 / 1.2 | Full Docker track before Cloud Run. |
| Kubernetes API, controllers, scheduling | D4 / 9 | CKA-level internals, then GKE. |
| CI vs CD vs GitOps, DORA | D0–D3 | After first deploy you automate it. |
| SLSA, attestations, admission | D5 | Before production GKE/Cloud Run policy. |
| TCP vs UDP, ports, NAT | 2.3 / 6.x | When VPC and Direct VPC egress appear. |
| AuthN vs AuthZ, sessions vs tokens, OAuth2/OIDC/JWT | 4.x | Full treatment. |
| Secrets vs config, OWASP API Top 10 | 1.5 then 4–5 | Secrets in Secret Manager from first backend. |
| Relational modeling, normalization, indexes, transactions, isolation | 2.x | Full SQL design track before Cloud SQL setup. |
| ACID, CAP, consistency, idempotency | 2.x and 7.x | Cloud SQL vs Firestore vs Spanner as decisions. |
| Linux OS on a VM (systemd, ssh, disks, patching) | 1.GCE | Compute Engine is where OS admin becomes real. |
| Queues, at-least-once, dead letters | 3.x | Pub/Sub. |
| PCI, PAN, tokenization, SAQ | 5.x | Payments. |
| Terraform HCL | 1.6 onward | All infra after the first manual deploy. |
| Python 3 typing, pytest, FastAPI | all exercises | Assumed engineer-level; we teach GCP client usage. |
| Go language (G0–G20 index) | JIT in F, 0–5, 8, 10, 11b | Appendix G maps modules to owners. Not a separate track. |
| Theory ladder (quant/alg/disc/LA/calc/prob/algo/sys/ML-theory) | **Block T** (T.* ; HS→UG→grad-as-needed; unified nodes mapped, not dumped) | Skip-test tiers JIT; see Block T map. Not shallow-HS-only destination. Chapter maps → Appendix T/B/I. |
| Discrete math, DS/algo | **T.Disc** + **T.Algo** then F1 + 8.1 + G-CS in Appendix G | Proof/sets/counting in **T.Disc**; structures/hash theory in **T.Algo**; loop-invariant *application* at **F1**; Bloom FPR formula at **8.1**. |
| Vectors, LA, probability *as used in ML metrics* | **T.LA** / **T.ProbStat** language; Part M (**M.ML**) owns ERM/metrics/IPS | T builds LA/measure language; M.ML does not re-teach sample-space toys. |
| Numerical stability (IEEE, κ, Kahan, LSE) | **M.NS** (prereq **T.Quant** HS + binary literacy) | Full module, Python then Go, before Part 0. Do not re-teach SI/binary place values in M.NS. |
| HLD/LLD literacy | 0.4 then every module | Donne Martin loop. |
| SOLID, hexagonal, DDD | 3.0 | Before split; CI grep on imports. |
| Protobuf, gRPC | 3.2 | Internal s2s; REST stays public. |
| HTTP/2 HOL, QUIC ideas | 6.1 | Transport only; crypto is stdlib. |
| Bloom, hashing, WAL, shed | 8.1 | Scale primitives. |

Linux/OS/sysadmin/networking/cybersecurity from the original request are **not dropped**. They are sequenced **after you have a running product**, so they attach to real GCP failure modes (IAM, VPC, audit logs, container escape surface, supply chain) instead of abstract distro admin.

**JIT prereq during T–11b:** needed **Block T** Tier HS families are required (or skip-tested) before F for absolute beginners; undergrad/grad T.* tiers open JIT before the owner that needs them (Block T map). **JIT prereq during F–11b:** if a GCP lesson needs theory not yet in T/M, emit `Prereq ref: 12.Sx (name) — one sentence + optional skip-test.` Do **not** teach the full continuation stage before 11b. Full S0–S24 is **Part 12**, after the GCP capstones. Part 12 S0–S10/S14 skip-test if the matching **Block T** undergrad/grad gate is already confirmed.

---

## Course spine

```
INITIAL COURSE (T–11b) — theory prerequisites + GCP + software system/architecture design.
Closable for PCA v6.1 and PMLE (Jun 2026) without Part 12.

T  Theory prerequisites (T.Quant…T.MLTheory) — HS→UG→grad-as-needed; skip-testable; **Tier HS before F** for absolute beginners
F  Foundation (F1–F4) — network vocab + Discrete JIT in F1; cloud literacy F2–F4
M  Quantitative prereqs: M.NS; **M.ML** (+ IPS); **M.TS**; **M.CAUSAL** lite (before 9c); case-study gaps → **9c.0**
   (M owns specific derives; Block T supplies the surrounding theory ladder — no re-teach of T.* toys)
0  Billing, IAM, hierarchy, HLD/LLD contract
1  Docker + Cloud Run, GCE (**T-ARCH required**), App Engine, Functions, LB/HA
D  CI/CD, GitOps, SLSA; **CT** for PMLE retraining
2  SQL, Cloud SQL, GCS, Firestore, Spanner, DB-1–10
3  Hexagonal/SOLID/DDD, microservices, gRPC, async, saga/outbox
4  Identity + from-scratch auth
5  Payments / PCI (no PAN)
6  Networking (**T-NET required**) + HTTP/2/QUIC ideas + CDN/IPs
7  Cybersecurity, DLP/PII, Model Armor (with 9c.7)
8  HLD/LLD + Donne Martin **gated studios** + 8.1 primitives including MapReduce/KV/Raft **toys**
8b/8c Hybrid + migration
9  GKE
9b Vertex / BQML / AutoML / Model Garden / Feature Store / Pipelines (PCA + PMLE products)
9c Production ML: **9c.0** concept atlas + classical zoo + family HLDs + Northstar slices + serve/monitor
10 Observability, SLO, FinOps, quotas, **T-OS required**
11 Northstar v1 + PCA four case HLDs + Go matrix + 8.1 toys
11b Control-plane capstone

12 Continuation AFTER 11b (not an exam gate): S0–S24 remainder
   (deep drills for T.* UG/grad; DB/opt/RL/causal depth; services/security/architecture; archive)
   Pure DSP/Kaldi, full CV PhD, transformer-from-scratch, five GenAI portfolios: OUT OF SYLLABUS
   (production speech/CV serving literacy stays 9c.6; GenAI/RAG production slice stays 9c.5)
```

**Line-count philosophy.** Growth in this file is **densification** of F–11b owners plus a **graduate-capable theory spine (Block T)** mapped from unified owner nodes — not filler, not twelve shallow hotel-floor metaphor sections, not a paste of unified §18, and not a second Kaldi/CV/transformer dump. Prefer fewer deeper `####` tiers, one-home derives, and bibliography pointers to **Appendix B / I / T** over redundant recall one-liners.

**Initial course complete when:** **T–11b** teaching text is expanded in place (**Block T** required-tier gates or skip-tests before F for absolute beginners / JIT before owners; Donne Martin studios, Go owners via Appendix G, ML families in 9c + Appendix M index, PCA `####` lessons under owners, PMLE literacy in 9b/9c); Northstar v1 runs; Appendix G artifacts checked; Part 8 gated toys + primer HLDs done; Appendix M families have evidence-pack HLDs; four official PCA case HLDs (Altostrat Media, Cymbal Retail, EHR Healthcare, KnightMotives); M.ML derivations + logistic/metrics/skew toy + **IPS / M.TS / M.CAUSAL lite**; **case-study concept map (9c.0) required for initial-track ML literacy**; three budgets (dollar, error, quota). Part 12 remains the continuation for deep T.* drills, DB/engine depth, full RL/causal/OR depth, services/security/architecture, and S24 — not a PCA/PMLE gate. Pure DSP/Kaldi, full CV PhD, transformer-from-scratch, and five GenAI portfolios are **out of syllabus** (external); production speech/CV serving stays **9c.6** literacy only; GenAI/RAG production stays **9c.5**.

This curriculum is the syllabus of record.

---

## Block T — Theory prerequisites (HS → undergrad → Ivy-grad as needed)

**Purpose.** This block (plus **Part M** + selected **Part 12** continuation stages) builds the theoretical machinery required to *derive and defend* decisions in **F–11b**: networking, IAM/auth, SQL/transactions, reliability/SLO, distributed systems, scale primitives, and production ML metrics/serving. Depth is **per topic up to graduate-coursework level** when the main-track owner needs it — not a survey, not a second copy of the unified §18 corpus, not a DSP/Kaldi/CV/transformer-from-scratch track (**out of syllabus**). **Academic rigor here is not “math for ML” only:** every subject a concept depends on (theory, math, CS, industry fundamentals) has a T.* home — networking, DB, security, and distributed systems each expose **T.SysTheory** (and related) tiers that **MUST** be confirmed before the product lab that depends on them (**Prop Lock** + Theory prerequisites map). **Skip-test any tier already confirmed.** Absolute beginners confirm **Tier HS** of needed families before **F**; undergrad/grad tiers open **JIT** before the owner that needs them (map below).

**Unified owner-node map (reference only — teach here, do not dump unified).** Block T absorbs the *theory ladder* for these unified nodes; Part 12 S0–S10/S14 are deep-drill continuation with skip-tests back to T.*:

| Unified node | Block T home | Main-track / continuation |
|---|---|---|
| `MATH-FUND` | **T.Quant** + **T.Alg** | F/0/8.F/10; deep drill **12.S3** |
| `PROOF-DISCRETE` | **T.Disc** | F1 Discrete JIT *application*; IAM/SQL; **12.S4** |
| `MATH-LA` | **T.LA** | 9c embeddings; **12.S5/S7** |
| `MATH-CALC-NUM` | **T.CalcOpt** | M.ML GD *uses*; **12.S9/S14** |
| `PROB-STAT-INFO` | **T.ProbStat** | language under M.ML/10.1/8.1; **12.S10** |
| `DS-ALGO` | **T.Algo** | Go G / 8.1 / Part 2 indexes; **12.S6/S8** |
| `DB-SQL` / `DB-ENGINE` *theory* | **T.SysTheory** DB | product setup stays **Part 2**; drills **12.S12/S13** |
| `SEC-AUTH` *theory* | **T.SysTheory** Security | product controls **Part 4/7**; drills **12.S19** |
| `ARCH-HLD-LLD` / `DIST-OPS` *formal models* | **T.SysTheory** Distributed / Reliability / Net | studios **Part 8**; net product **Part 6**; SLO **10.1** |
| `ML-CORE` *learning-theory as needed* | **T.MLTheory** → **M.ML** / **9c** | classical zoo **9c**; IPS/ERM **M.ML**; **12.S11** skip-test only |

**Placement.** Spine: **T → F → M → 0…11b → 12**. No GCP product labs in Block T — paper + derive + tiny Python → Go where implementable. Part 12 **S0–S10 / S14** = deep-drill continuation for T.* undergrad/grad tiers (skip-test if Block T gate confirmed). Do **not** re-add S15/S16.

**Overlap ban (hard).** Block T never steals owned derives:
- **M.NS** — IEEE / ε / Kahan / LSE / money-integer policy
- **M.ML** — ERM / losses / P/R/F1/ROC/AUC / IPS
- **M.TS** — trend/seasonality ownership
- **M.CAUSAL** — potential-outcomes toy + uplift slogan
- **F1** — IP/port/DNS/TCP/UDP/HTTP/TLS/JSON + Discrete JIT *application*
- **8.1** — Bloom FPR formula \((1-e^{-kn/m})^k\), ring/hash toys
- **10.1** — SLO burn-rate derive
- **Part 4/7** — auth product controls; **Part 6** — VPC/CIDR *design*
- Inventing ciphers (stdlib); DSP/CV/Kaldi/transformers (**out of syllabus**)

**Bibliography discipline.** Cite texts **by name** below. Full chapter maps live in **Appendix T**; Go/software/security lists in **Appendix B**; institutional cross-check in **Appendix I**. Do **not** paste the unified §8–§9 / §18 corpus into this block.

**Block T complete when:** for each family needed on the live track, the required tier’s derive/prove gate (or skip-test) is on the ledger → enter **F1**. Gate **M.NS** behind **T.Quant** HS + binary literacy; gate **M.ML** behind **T.Alg** functions + **T.ProbStat** HS/UG language (+ **T.CalcOpt** UG JIT for GD).

---

### Theory prerequisites map (main ### → required T.* tier)

| Main-track owner | Required T.* (confirm or skip-test before / with) |
|---|---|
| **F1** Discrete JIT + network vocab | **T.Disc** HS; **T.Quant** HS |
| **F2–F4** cloud literacy | **T.Alg** HS; **T.Disc** HS sets/predicates |
| **F3** scope (global / regional / zonal) | **T.Quant** HS; region/zone + GCS anchors in F3 — **does not** require VPC / subnet / firewall or **T.SysTheory** Networking UG |
| **M.NS** | **T.Quant** HS; binary/powers-of-two (**T.Disc** HS) |
| **M.ML** | **T.Alg** HS→UG; **T.ProbStat** HS→UG; **T.CalcOpt** UG gradients JIT |
| **M.TS / M.CAUSAL** | **T.Alg**; **T.ProbStat** conditional language |
| **0.1 / 8.F / 10.3** billing & napkins | **T.Quant** + **T.Alg** HS |
| **0.5 / 4.7 / 6.4** IAM & AuthZ & FW | **T.Disc** predicates; **T.SysTheory** Security UG |
| **2.x** SQL / transactions | **T.Disc**; **T.SysTheory** DB UG; **T.Algo** indexes cross-link |
| **6.1 / T-NET** transport refresher | **T.SysTheory** Networking UG (e2e / AIMD); **T.Quant** RTT |
| **6.1b / 6.2** VPC / subnet (concept + product) | **T.SysTheory** Networking UG (encapsulation, L2 vs L3, address+mask, subnet-as-partition, routing-as-path, isolation boundary) + **T.Disc** graphs; **T.Algo** path literacy as needed; **T.Quant** bits/bytes |
| **6.x** remaining net product | **T.SysTheory** Networking UG confirmed; then product owner |
| **8.1** scale primitives | **T.Algo** UG; **T.ProbStat** independent-trials *language*; FPR **formula @ 8.1** |
| **8.B / Part 3** distributed | **T.SysTheory** Distributed UG→grad-as-needed |
| **10.1** SLO | **T.SysTheory** Reliability UG; **T.ProbStat** rates; burn-rate **@ 10.1** |
| **9c / embeddings** | **T.LA** UG→grad-as-needed; **T.MLTheory** as needed; metrics/IPS **@ M.ML** |
| **12.S0–S10 / S14** | Deep drill **iff** matching T.* UG/grad gate not yet confirmed |

---

### T.Quant — Quantities, units, orders of magnitude, dimensional analysis

**Unified node:** `MATH-FUND` (units/estimation slice). **Feeds:** 0.1, 8.F, 10.x, F3.

#### Tier HS
**Derive/prove gate.** SI prefixes n…G; scientific notation; order-of-magnitude *class*; unit cancel in `qty × rate`; reject `ms + MB`.
**Python → Go.** `to_seconds`, `sci`, unit-aware napkin helpers → Go `units`.
**Does not overlap.** **M.NS** IEEE/ε; **10.1** burn-rate; **Part 6** CIDR.
**Sources.** OpenStax *Prealgebra* / quantitative literacy; SRE napkin culture as later *application*.

#### Tier Undergrad
**Derive/prove gate.** Dimensional homogeneity; GiB vs GB disclosure; latency ≈ distance/speed (given constant) + RTT class labels.
**Python → Go.** `rtt_ms` + order-band asserts; unit-crime reject path.
**Does not overlap.** Physics problem sets banned; F3/8.F *apply* napkins.

#### Tier Grad-as-needed
Uncertainty propagation for FinOps/SLO numerics beyond **M.NS** tolerance — rare; else skip. Cross-link **12.S9**, do not duplicate.

---

### T.Alg — Algebra through inequalities, functions, composition

**Unified node:** `MATH-FUND`. **Feeds:** modeling everywhere (0.1, M.ML \(f\), 0.4/Part 3 composition).

#### Tier HS
**Derive/prove gate.** Linear solve; proportions; % ↔ fraction; inequalities as ceilings; function = unique output; rise/run only.
**Python → Go.** Cost/%/alert CLI; `is_function`; composition as pipeline.
**Does not overlap.** Derivatives → **T.CalcOpt**.

#### Tier Undergrad
**Derive/prove gate.** Domain/codomain/range; false-inverse counterexample; composition on finite maps; logs/exponents for orders; piecewise defs.
**Python → Go.** Piecewise evaluator; inverse/composition counterexamples (**12.S3** deep drill / skip-test).
**Sources.** OpenStax *Algebra and Trigonometry* / *Precalculus*; Hall & Knight as used — chapter maps **Appendix T**.

#### Tier Grad-as-needed
Abstract-algebra slogans only if a force needs pipeline monoid rigor — prefer **12.S3** residual. Not a second MATH-FUND dump.

---

### T.Disc — Logic, sets, proofs, counting, graphs, invariants, asymptotics

**Unified node:** `PROOF-DISCRETE`. **Feeds:** F1 Discrete JIT (*recall* habits), IAM predicates, SQL, 8.1 hash/bloom *intuition*, Part 3. Rosen/Sipser-adjacent **as used** — not a TOC degree.

#### Tier HS
**Derive/prove gate.** Sets ∪∩∖⊆; Boolean ∧∨¬ + truth table; row predicates; product rule; \(2^w\); pigeonhole; binary/hex/bit vs byte.
**Python → Go.** SoD frozenset toy; `pred(row)`; bin/hex converters.
**Does not overlap.** **F1** applies loop invariant to HTTP parse; **8.1** owns Bloom FPR *formula*; **M.NS** owns IEEE.

#### Tier Undergrad
**Derive/prove gate.** Direct/contrapositive/contradiction/induction; relations; counting as used; graph BFS/DFS literacy; representation invariants; big-O from a loop.
**Python → Go.** Proof portfolio + tested structure with named invariant (**12.S4**; one home per artifact).
**Sources.** Rosen *Discrete Mathematics*; Hammack *Book of Proof*; MIT 6.042J — maps **Appendix T/B**.

#### Tier Grad-as-needed (**T-TOC** lite)
Automata/complexity literacy only when a main-track force needs it. Sipser excerpts **as used**; Hopcroft/Motwani/Ullman only if opened. **Not** a TOC degree; WFST/Kaldi automata **out of syllabus**. Deep drill → **12.S4/S8** residual.

---

### T.LA — Vectors, matrices, norms, least squares, eigen/SVD as used

**Unified node:** `MATH-LA`. **Feeds:** 9c embeddings/two-tower, PCA in zoo, M table rows. Derive residual/reconstruction — not spectral career.

#### Tier HS
Optional coordinate-pair bridge; most enter Undergrad.

#### Tier Undergrad
**Derive/prove gate.** \(\mathbb{R}^n\) as used; norms; dot → cosine; matrix–vector; least squares + residual \(\|Ax-b\|\); rank/nullity on small examples.
**Python → Go.** NumPy-free kernels then NumPy compare; cosine degenerates; Go embedding-dim helpers.
**Does not overlap.** **M.ML** losses/metrics; **M.NS** conditioning *policy*; full spectral → grad / **12.S7**.
**Sources.** Strang *Introduction to Linear Algebra*; MIT 18.06 — **Appendix T**.

#### Tier Grad-as-needed
**Derive/prove gate.** Four subspaces; QR idea; eigen/SVD; PCA reconstruction error; \(\kappa_2=\sigma_{\max}/\sigma_{\min}\) as used.
**Python → Go.** Power iteration / PCA residual (**12.S7** skip-test). Trefethen & Bau / Golub & Van Loan *as used* — stop before operator-theory PhD.

---

### T.CalcOpt — Limits, derivatives, gradients, convexity, GD/Lagrange as used

**Unified node:** `MATH-CALC-NUM` (+ opt slice of S14). **Feeds:** M.ML GD, 9c losses, T-OPT when opened. **12.S9/S14** host deep drills — cross-link, **don’t duplicate** full course twice.

#### Tier HS
Average rate of change only if needed; else start Undergrad.

#### Tier Undergrad
**Derive/prove gate.** Derivative as local linearization; chain rule on scalar losses; \(\nabla\frac12\|Ax-b\|^2\); convexity cartoon; GD with chosen step; Lagrange slogan for one equality **as used**.
**Python → Go.** FD gradient checker vs analytic; tiny GD on quadratic; tolerance per **M.NS**.
**Does not overlap.** ERM/log-loss derive → **M.ML**; burn-rate → **10.1**.
**Sources.** MIT 18.01SC/18.02SC; OpenStax *Calculus*; Nocedal & Wright / Boyd & Vandenberghe **as used** at grad — **Appendix T**.

#### Tier Grad-as-needed
Jacobian/Hessian as used; KKT literacy; convex vs nonconvex failure modes; duality as used by **T-OPT**. Deep drill **12.S9/S14**. Stanford EE364A/B as used — not convex-analysis PhD unless ceiling opened.

---

### T.ProbStat — Probability spaces, RVs, estimation, tests, information as used

**Unified node:** `PROB-STAT-INFO`. **Feeds:** M.ML metrics *language*, M.CAUSAL conditionals, 10.1 rates, 8.1 FPR *intuition*. Builds measure language/proof habits — **does not steal** M.ML ERM/log-loss/IPS.

#### Tier HS
**Derive/prove gate.** Sample space; equally likely \(P\); disjoint additivity; independence cartoon; conditional-by-table; mean/median/percentile; rates; \(\sum\) / mean of indicators.
**Python → Go.** Table conditionals; mean/p90; availability as mean of \(I_i\).
**Does not overlap.** P/R/F1/ROC/AUC/IPS → **M.ML**; burn-rate → **10.1**.

#### Tier Undergrad
**Derive/prove gate.** RV, \(\mathbb{E}\), Var; LLN/CLT statement + simulation check; MLE on Bernoulli/Gaussian; CI/test literacy; entropy/CE/KL **definitions** as used.
**Python → Go.** Samplers; MLE toy; bootstrap CI sketch (**12.S10**).
**Does not overlap.** **M.ML** production metric packages + IPS; **M.CAUSAL** two-arm toy.
**Sources.** MIT 6.041SC; Wasserman *All of Statistics*; Casella–Berger; Grinstead & Snell; Cover & Thomas for info — **Appendix T** (not a dump).

#### Tier Grad-as-needed
**Derive/prove gate.** (1) Distinguish a.s. convergence vs in-probability on a concrete sequence (one counterexample each direction or cite why they diverge). (2) Sufficiency: show sample mean is sufficient for Bernoulli \(p\) via factorization (or cite Neyman–Fisher on the toy). (3) State Cramér–Rao lower bound for an unbiased estimator and check a Bernoulli MLE against it numerically. (4) Multiple-comparison: Bonferroni correction on a 5-test toy; name one sequential-testing caveat for **9c.7**. (5) Info: prove \(D_{\mathrm{KL}}(p\|q)\ge 0\) via Jensen (or Gibbs) and use CE/KL to explain a calibration/drift alarm. Deep drill **12.S10/S14**. Not a math-stat PhD.

---

### T.Algo — Data structures, invariant-based algorithms, complexity, hashing theory

**Unified node:** `DS-ALGO`. **Feeds:** Go G modules, 8.1, Part 2 indexes. Cross-link **Appendix G** / **12.S6–S8**; **one home** per artifact.

#### Tier HS
Array/list/map vocabulary; linear search; sorting-as-idea.

#### Tier Undergrad
**Derive/prove gate.** Array/slice/map/heap/tree/union-find contracts; loop invariants; amortized growth; hash families + collision *language*; sorting lower-bound intuition; BFS/DFS/Dijkstra as used; Master theorem as used on one recurrence.
**Python → Go.** **Go-first** for structures; property tests; complexity argument before code.
**Does not overlap.** Bloom FPR **formula** + ring toys → **8.1**; Raft toy → **8.1/8.B**; Appendix G indexes modules only.
**Sources.** CLRS; Sedgewick & Wayne; MIT 6.006 — **Appendix B/T**.

#### Tier Grad-as-needed
Hard platform / external-memory as used by Bigtable/Spanner literacy — only if force needs. Deep drill **12.S8**. Not a contest degree.

---

### T.SysTheory — Formal models behind the main track

**Unified nodes (theory only):** Reliability/SLO math → with **10.1**; net theory → `requires` **T-NET**/6.1; distributed → `DIST-OPS` formal slice; DB → `DB-SQL`/`DB-ENGINE` theory; security → `SEC-AUTH` theory; coding lite as used by multi-region/GCS. Product labs stay in Parts 2/4/6/7/8/10. Each subfamily below has UG + **grad-as-needed Derive/prove gates** (not metaphors).

#### Reliability (before/with **10.1**)
- **UG Derive/prove gate.** Series availability \(\prod A_i\) and parallel \(1-\prod(1-A_i)\) from independence; name the independence assumption you used; SLI/SLO vocabulary **without** burn formula.
- **Grad-as-needed Derive/prove gate.** Error-budget identity: budget = \((1-\mathrm{SLO})\times\mathrm{window}\); show how a multi-window burn ratio is a rate-of-spend (algebra only) — **operational burn/freeze policy @ 10.1** (Google SRE Workbook). Renewal/reward: mean time between failures vs availability under a stated renewal model (one worked numeric).
- **Does not overlap.** **10.1** owns operational burn/freeze and freeze decisions.

#### Networking theory (with **6.1 T-NET** / before **6.1b–6.2** VPC)
- **HS (confirm before F3 optional graph metaphor / before any address-partition work).** Bits/bytes and order-of-magnitude recall → **T.Quant** HS; **graphs as connections** → **T.Disc** HS (nodes = interfaces or hosts; edges = “can reach” / adjacency) — **no GCP VPC / subnet / firewall brand names** at this tier.
- **UG Derive/prove gate (required before VPC/subnet product labs).** (1) **Encapsulation:** show a payload wrapped by successive headers; name what each layer adds/strips. (2) **L2 vs L3:** same-link delivery vs routed delivery — one counterexample where L2 broadcast domain ≠ L3 subnet. (3) **Address + mask:** given address and prefix length, compute network ID and host range; prove two addresses are/aren't in the same partition. (4) **Subnet as address partition:** a subnet is a contiguous address set under a mask — not “a VPC,” not “a region,” not “a firewall.” (5) **Routing as graph path:** pick next hop by longest-prefix / table lookup on a tiny graph; show a blackhole when no route. (6) **Isolation boundary:** distinguish **failure domain** (what dies together) from **trust boundary** (who is allowed to talk) — one sentence each with a toy. (7) End-to-end argument in one paragraph with a counterexample where hop-by-hop checksum is insufficient; layering diagram with one payload crossing layers. (8) **AIMD** window update: on ACK \(w\leftarrow w+1/w\), on loss \(w\leftarrow w/2\) — simulate 20 RTTs by hand or code.
- **Grad-as-needed Derive/prove gate.** **Little’s law** \(L=\lambda W\) on a single queue: derive from arrival/departure counts over \([0,T]\); apply to RPS × latency → concurrency. Congestion/control theory lite (name one fairness/stability trade-off of a TCP variant as used) — **do not invent crypto**; not a networking PhD.
- **Sources.** Kurose/Ross or Tanenbaum & Wetherall; Saltzer–Reed–Clark — **Appendix I/B**.
- **Does not overlap.** **F1** IP/port/DNS/TCP/UDP/HTTP/TLS/JSON vocab; **Part 6** owns VPC/CIDR *product* design and console labs; **F3** owns location/scope intuition **without** VPC props.

#### Distributed systems
- **UG Derive/prove gate.** Happens-before on a 3-process timeline (draw → prove one pair incomparable); CAP: state which two you keep under a named partition; consensus safety vs liveness in one sentence each.
- **Grad-as-needed Derive/prove gate.** Quorum intersection: for majority quorums of size \(\lfloor n/2\rfloor+1\), prove any two quorums intersect; FLP: state the impossibility claim (async + one crash) and why production systems add timeouts/partial sync assumptions; linearizability vs serializability — one counterexample schedule that is serializable but not linearizable. DDIA + Lynch-lite / MIT 6.5840 as used.
- **Does not overlap.** Raft/MapReduce/KV **toys @ 8.1/8.B**; no etcd reimplementation.

#### DB theory (with **Part 2**)
- **UG Derive/prove gate.** Push a selection through a join (relational-algebra equivalence); name keys/FDs that justify 3NF on a 4-attribute toy; produce one dirty-read and one lost-update schedule; WAL durability: argue why a commit after log flush survives crash.
- **Grad-as-needed Derive/prove gate.** MVCC snapshot: given begin-ts and commit-ts of two writers, decide which version a reader sees and prove no dirty read under snapshot isolation; cost-model literacy: estimate rows for a filter given selectivity (engine toys **12.S12–S13**).
- **Sources.** Ramakrishnan/Gehrke or equiv.; PostgreSQL docs; CMU 15-445 — **Appendix T**.
- **Does not overlap.** Cloud SQL setup **@ 2.3**.

#### Security theory
- **UG Derive/prove gate.** STRIDE-as-used: one threat per category on a toy HTTP+DB diagram; authz as a predicate `allow(principal, action, resource)` with a SoD counterexample; crypto literacy: state discrete-log / factoring hardness assumption *as used* (groups, modular arith) — no cipher design.
- **Grad-as-needed Derive/prove gate.** Sketch one reduction-style argument shape (“if adversary breaks X then oracle Y breaks hardness Z”) for a stdlib primitive you **call**, not invent — **NEVER invent ciphers**; stdlib owns primitives. Katz–Lindell / Goldreich only if T-crypto ceiling opened (**Appendix I**).
- **Does not overlap.** **Part 4/7** product controls; **12.S19** deep drill / skip-test.

#### Information & coding lite
- **UG/Grad-as-needed Derive/prove gate.** Erasure vs replication: for 3-way replication vs Reed–Solomon-style (k-of-n) intuition, compute storage overhead and surviving-failure count on a toy — **not** a Shannon PhD (Cover & Thomas only as used via **T.ProbStat**/storage owners).

**Python → Go.** Availability calculators; AIMD sim; Little’s-law concurrency check; anomaly tables; policy-evaluator stubs — Go preferred for systems toys.

---

### T.MLTheory — Statistical learning theory as needed for 9c

**Unified node:** `ML-CORE` *theory under* — implementations and IPS stay **M.ML**; classical zoo / serving stay **9c**; **12.S11** is skip-test only. Grad depth = results used in production metrics and failure modes.

#### Tier HS
Not a destination — use **T.ProbStat** HS + **T.Alg**.

#### Tier Undergrad
**Derive/prove gate.** Train/test rationale; bias–variance with derive-able quadratic example; overfitting vs generalization gap; ranking utility foundations without stealing IPS.
**Python → Go.** Synthetic overfit demo; calibration diagram sketch.
**Does not overlap.** **M.ML** ERM/log-loss/IPS gates; zoo @ end of **9c**.
**Sources.** ISL 2e; Wasserman ML chapters; Shalev-Shwartz & Ben-David *as used* — **Appendix T**; not Bishop/ESL dump.

#### Tier Grad-as-needed
**Derive/prove gate.** (1) PAC: state \((\varepsilon,\delta)\)-learnability and compute a sample-size lower bound of the form \(m \gtrsim \frac{1}{\varepsilon^2}\log\frac{1}{\delta}\) (order-of-magnitude) for a finite hypothesis class. (2) VC: give VC-dimension of thresholds on \(\mathbb{R}\) (prove \(\ge 1\) shatter, argue why 2 points fail for positive rays). (3) Uniform convergence slogan → concrete: relate train–test gap to a complexity term (one inequality citation, not a proof of VC theorem). (4) ECE: compute Expected Calibration Error on a 3-bin toy reliability diagram. (5) LTR: write a pairwise logistic or hinge ranking loss and show how a score swap changes it (utility bound *as cited in 9c* — do not steal **M.ML** IPS). (6) Covariate/label shift: name the broken assumption and the monitoring signal. Deep drill **12.S14** / CS229 notes as used. **No Kaldi, no full CV, no transformer-from-scratch** (**out of syllabus**). Speech/CV serving **@ 9c.6**; GenAI/RAG **@ 9c.5**.

---

**Block T exit checklist.** Needed families’ required tiers gated or skip-tested; absolute beginners hold **Tier HS** green before **Block F**; engineers skip-test per family/tier. Next: **Block F** — F1 owns network vocab + Discrete JIT *application* (habits from **T.Disc**; never a shallow HS-only destination).

---

## Block F — Absolute beginner + cloud computing fundamentals

**Prereq:** **Block T** needed Tier HS families complete or skip-tested (absolute beginners: T Tier HS before F; UG/grad JIT). Required if you cannot yet: use a terminal, explain HTTP, or explain IaaS vs PaaS. Software engineers skip-test each F subsection; fail any check and you do that subsection fully.

### F1 Absolute beginner computing (pre-GCP)

Required if you cannot yet: use a terminal, explain HTTP, or explain a process. Software engineers skip-test; fail any check and you do this subsection fully.

Split rule (Pedagogy §7): every network intuition below is its **own** #### Concept anchor with a point-at example. Do **not** pose one vocabulary check that spans IP+port+DNS+TCP/UDP+HTTP+TLS+JSON — unlock and confirm one cluster before opening the next.

#### Concept: Computer (hardware map)
**What / why.** A computer is CPU (executes instructions) + RAM (working state) + disk (persistence) + NIC (packets). Cloud Run “CPU/memory,” Persistent Disk, and VPC NICs reuse the same words — Google operates the metal; you still size and pay for the abstractions.
**Failure modes.** Treating “serverless” as “no CPU/memory limits”; assuming RAM survives process restart; confusing ephemeral container filesystem with Persistent Disk.
**Assumptions.** One machine mental model first; distributed failure domains unlock in F3.
**Point-at.** On Cloud Shell: `nproc`, `free -h`, `df -h`, `ip -br a` — four observables you will later see as Cloud Monitoring metrics.

#### Concept: OS — process, permissions, logs
**What / why.** The OS multiplexes CPU/RAM: a **process** owns an address space and threads; **file descriptors** are handles; **user/permission bits** gate files; **environment variables** configure without recompile; **stdout/stderr** are streams — logging services are not magic, they ingest those streams (or structured writers).
**Failure modes.** Ignoring exit codes in CI; writing secrets to stdout; `chmod 777` “to make it work”; conflating thread with process with container.
**Point-at Linux for Cloud Shell:** `ls`, `cd`, `pwd`, `cat`, `chmod`, `ps`, `grep`, `jq`, pipes, redirect, exit codes. Prove: `false; echo $?` prints non-zero.

#### Concept: CLI vs GUI
**What / why.** The CLI is scriptable and is how CI talks to GCP. Shell + `$PATH` + exit code ≠ 0 = fail the pipeline. GUIs are for exploration; production changes are reviewed text (Terraform, YAML, PRs).
**Failure modes.** “It works in console” with no IaC; broken `$PATH` after curl-install; treating interactive prompts as automation.
**Point-at.** `command -v gcloud || echo missing` — same check CI should make before deploy.

#### Concept: Git workflow and recovery
**What / why.** clone → branch → commit → push → PR is the change contract. Recovery (wrong remote, detached HEAD, broken module path) is a **runbook**, not “delete the repo.” **Go G0** lives under this owner for toolchain recover.
**Failure modes.** Force-push to shared main; committing secrets; fixing `go.mod` by guessing instead of comparing to remote convention.
**Point-at.** `git status`, `git remote -v`, `git branch -vv` on a deliberately broken fixture; restore with documented steps.

#### Concept: IP address
**What / why.** An IP identifies a network interface endpoint. IPv4 dotted quad; IPv6 longer. Loopback `127.0.0.1` / `::1` never leaves the host. Private ranges (RFC1918) are not internet-routable without NAT.
**Failure modes.** Putting a private IP in a public DNS A record; assuming Cloud Shell’s IP is stable; conflating “has an IP” with “reachable from the internet.”
**Point-at.** `ping -c1 127.0.0.1` succeeds; `ping` to a random RFC1918 from Cloud Shell usually fails — different failure domain than “DNS broken.”

#### Concept: Computer network as a graph of reachable interfaces
**What / why.** Abstractly, a **computer network** is a **graph**: nodes are interfaces (or hosts); an edge means “packets can be delivered” under some rule. Reachability is a path in that graph — not a brand name. This metaphor unlocks later routing talk; it does **not** introduce GCP **VPC**, **subnet**, or **firewall** products (those unlock in **Part 6** after **T.SysTheory Networking** UG).
**Failure modes.** Equating “I drew boxes and lines” with a VPC; assuming any two boxes with lines are the same failure domain or trust boundary; smuggling Part-6 product nouns into F1 checks (**Prop Lock**).
**Point-at.** Three loopback/lab processes as nodes; an edge only if you can `curl` one from another on your machine — count paths, not “clouds.”
**Vocab check (this anchor only):** node / edge / path / reachable — **MUST NOT** include VPC, subnet, or Cloud NGFW.

#### Concept: Port
**What / why.** A port is the demux key on one IP: `(IP, port, protocol)` selects a listening process. Clients use ephemeral source ports; servers bind well-known or configured ports (`8080`, `443`).
**Failure modes.** Two processes binding the same port; forgetting firewall allows the port; confusing container port with service/LB port.
**Point-at.** Start a tiny listener on `127.0.0.1:8765`; second bind fails with “address already in use.”

#### Concept: DNS A / AAAA
**What / why.** DNS maps names to records. **A** → IPv4; **AAAA** → IPv6. TTL controls cache stickiness. Apps should prefer stable names (`run.app`, your LB hostname) over raw IPs in configs you own.
**Failure modes.** Low TTL cannot fix wrong IP; CNAME chains you do not understand; baking ephemeral VM IPs into public A records (Part 6.3 deepens this).
**Point-at.** `getent hosts example.com` or `dig +short example.com A` — name in, addresses out. No GCP product required for the intuition.

#### Concept: TCP vs UDP
**What / why.** **TCP:** connection, ordered byte stream, retransmission — HTTP/1.1 and TLS typically ride TCP. **UDP:** datagrams, no built-in retry/order — DNS queries and many real-time protocols use it.
**Failure modes.** “UDP is always faster” without loss math; expecting HTTP semantics on a raw UDP socket; ignoring head-of-line (later Parts) when you only know “TCP is reliable.”
**Point-at.** One sentence: your F1 HTTP server uses TCP; a one-shot DNS lookup from `dig` is usually UDP to port 53.

#### Concept: HTTP methods and status codes
**What / why.** HTTP is an application protocol: request line + headers + optional body → status + headers + body. Safe methods (`GET`, `HEAD`, `OPTIONS`) must not change server state; `POST`/`PUT`/`PATCH`/`DELETE` may. Status classes: 2xx success, 4xx client, 5xx server.
**Failure modes.** Mutating on GET; returning 200 for errors with `{"error":...}` only; leaking stack traces in 500 bodies.
**Point-at.** `GET /healthz` → `200` + JSON; wrong method → `405`; missing required header → `400` — predict **before** coding the branch.

#### Concept: TLS idea (terminate vs pass-through)
**What / why.** TLS wraps a byte stream so eavesdroppers cannot read/modify cleartext. **Terminate** = decrypt at an edge (LB/GFE); **pass-through** = encrypted all the way to the origin process. You need the idea now; cipher policy and cert automation deepen in 1.4 / 6.x.
**Failure modes.** Shipping passwords over `http://`; disabling verify “temporarily”; assuming “HTTPS in front” means the app may log Authorization headers safely (it must not).
**Point-at.** Browser padlock to `https://example.com` vs raw `http://127.0.0.1:8080` lab server — same HTTP messages, different transport protection.

#### Concept: JSON as a media type
**What / why.** JSON is a text serialization (`Content-Type: application/json`), not a database and not “the API.” Objects/arrays/numbers/strings/bool/null; no trailing commas; UTF-8.
**Failure modes.** Concatenating HTML into JSON; trusting client JSON without schema limits; treating log lines as JSON without a parser.
**Point-at.** Body `{"ok":true}` with header `Content-Type: application/json` — your first golden contract for Python and Go twins.

#### Concept: Discrete JIT (invariant on the parse loop)
**What / why.** A **proposition** is true/false; a **counterexample** falsifies a claim; a **loop invariant** is what stays true each iteration. Attach to the first algorithm (e.g. “scanner consumed the entire request line”) — not a math semester.
**Failure modes.** “Tests pass” with no named invariant; off-by-one only discovered in prod.
**Point-at.** Write one invariant comment above the request-line parse loop; attempt a counterexample input (no CRLF) and predict the status code.

#### From scratch (required)
- Bind a TCP socket, read a request line, write `HTTP/1.1 200` + `Content-Type: application/json` + body. This is the first middleware host. FastAPI comes **after** you have spoken HTTP bytes once.
- Predict status codes for bad method / missing header before coding the branch.
- Separate micro-drills (do not bundle into one vocab quiz): (1) explain one IP string’s scope; (2) show port conflict; (3) resolve one A record; (4) one-sentence TCP vs UDP; (5) TLS terminate vs cleartext; (6) strict JSON parse reject.

#### Python then Go
- Python enough: venv, `pip`, functions, types, pytest, then FastAPI wrapping the same JSON contract.
- **Go at first submit (G0–G2 lesson text pasted under this heading):** modules, `gofmt`/`go vet`, `main`, types, vars, `for`/`if`/`switch`, arrays, `_` (**G0–G1**). Then slices, maps, `range`, functions, errors, `defer` (**G2**). No locked Go tokens before their SYNTAX UNLOCK.

#### HLD / ADR prompt
- One-box context diagram: Client → (DNS) → IP:port → TCP → TLS? → HTTP → JSON handler → stdout logs. NFR: “local only” vs “internet.” ADR stub: “I pick cleartext HTTP on loopback for the first lab because Y (see bytes), I accept Z (no transport security until 1.4).”

#### LLD shape
- Package `httpserver` (Python) then Go twin: parse request line; map method → handler; status table 200/400/405; golden JSON fixture. No IAM/Terraform yet — filesystem + git only. Errors are status codes, not exceptions swallowed.

#### GCP lab (free-tier boxed)
- No billable GCP required. Cloud Shell optional: run the Python server; `curl -i`; show `gcloud --version` exists for later. **Credits-optional:** none. Do not enable APIs yet (F4).

#### Lab / gate
- **Exercise:** Python HTTP server returns JSON; after submit, Go version (`net/http`, `testing`).
- **Gate (unseen + nearby — only anchored terms):** Unseen — given a broken request line (no version), pick status and one-line reason. Nearby transfer — add `Content-Length` correctly without changing the JSON contract. Also: process vs thread vs container in one paragraph; Git PR merged; both language servers return the same golden JSON; discrete invariant written above the parse loop.
- **Vocab audit reminder:** after the IP anchor, a check may use IP terms only; do not sneak DNS/TLS/JSON into that same check until those anchors are confirmed.

#### PCA: beginner → cloud literacy bridge
- **Considerations (exam guide themes):** shared responsibility starts at “what do I patch?”; tooling (Cloud Shell / SDK) is PCA 5.2 adjacent; you cannot design what you cannot operate from a terminal.
- **Decision table:**

| Situation | Pick | Accept |
|---|---|---|
| Never used a shell | Finish F1 fully | Delay all GCP labs |
| Can write Python HTTP + Git PR | Skip-test F1 | Spot-check network vocab **per anchored cluster** |
| Can explain TCP/HTTP but not Git recover | Do Git/G0 only | Do not skip toolchain |

- **Scenario prompt:** A teammate’s Cloud Shell shows `command not found: gcloud` after they “installed something with curl.” What do you check first?
- **Expected:** “I pick verify `$PATH` / Cloud Shell reset / SDK components because Y (tooling before IAM), I accept Z (reinstall beats debugging a broken profile forever).”

#### Go G0 — Toolchain, modules, Git/SSH recovery
SYNTAX UNLOCK: `go` CLI is not a language keyword. First tokens here are **module path** (`module example.com/northstar`), `go 1.22`, and the fact that `go.mod` is the lock on **what** you import. Contrast Python: `pyproject.toml` / `requirements.txt` name packages; Go names a **module root** and every import is rooted under it. Memory model not yet — this unlock is filesystem + PATH.
Concept: Install Go once; prove `go env GOPATH GOROOT GO111MODULE`. Every Northstar Go tree is a module. `gofmt` and `go vet` are gates, not style tips. Git/SSH failures (wrong remote, broken `go.mod` module path, missing `replace`) are recovered with a runbook, not by deleting the repo. Same recover path is reused when the billing CLI (0.1) ships with a wrong module path.
Python twin first: venv + `pip install -e .` + a one-file script that prints version; commit; push; open PR. Only after submit do you touch Go.
Go artifact: package `tooling`; tests: `TestModPathMatchesDir` (module path equals repo convention), `TestGofmtClean` (no diff after format), `TestVetPasses`; gate: broken `go.mod` fixture restored by documented steps; `go test ./tooling` green; runbook checked into `docs/go-setup.md`.

---

#### Go G1 — main, types, control flow, arrays, blank identifier
SYNTAX UNLOCK: `func main()` is the process entry (signature: no args, no returns — unlike Python `if __name__`). `:=` declares+assigns in function scope only; `var x T` zero-values. `for` is the only loop (`for i := 0; i < n; i++`, `for cond`, `for range`). `if`/`switch` (no paren; `switch` can be expressionless). Arrays: `[N]T` is a value (copied). `_` discards deliberately. Overflow: Go integers wrap; predict before assert.
Concept: Typed zeros (`0`, `""`, `false`, `nil` later). Explicit types at boundaries. Arrays are fixed length — prefer slices next. Never ignore errors with `_` except for unused imports/range indexes you truly discard.
Python twin first: typed functions + pytest table for overflow/edge ints; FastAPI not required yet.
Go artifact: package `cmd/hello` + `basics`; tests: `TestPredictOverflow`, `TestSwitchExhaustiveStatuses`, `TestArrayCopyIsIndependent`; gate: command runs; table tests pass; no `_ = err` in the package.

---

#### Go G2 — slices, maps, functions, defer, errors, runes; stacks/queues
SYNTAX UNLOCK: slice header = `(ptr, len, cap)` — assignment aliases the backing array (unlike Python list assignment which also aliases, but `append` may reallocate). `map[K]V` is a reference; read with `v, ok := m[k]`. Multiple returns: `(T, error)` — check every `error`. `defer` schedules LIFO on function return (close files/unlock). `range` over slice/map/string; string range yields `rune` (code point), not bytes. Errors are values: `errors.New`, `fmt.Errorf("%w")`.
Concept: Prefer slices over arrays. Map iteration order is randomized — tests must not assume order. Build stack/queue on slices with documented invariants. Never ignore `error`.
Python twin first: list/dict aliasing lab + custom exception path; pytest proves alias vs copy.
Go artifact: package `collections`; tests: `TestSliceAliasThenAppend`, `TestMapMissingOk`, `TestStackInvariant`, `TestDeferOrder`, `TestNoIgnoredError` (static check or grepped CI); gate: all green; first Go submit of the HTTP JSON twin may use this package.

---

### F2 What is cloud computing


#### PCA: 4.2 Business processes

**Guide themes (matrix):** stakeholders; change management; skills readiness; decision-making; customer success; CapEx/OpEx; BCP. Homes: F2, 0, 10, 11.

| Topic | Prefer | Accept |
|---|---|---|
| Spend model | OpEx + budgets/alerts | Untracked CapEx lift |
| Change | CAB-lite + ADRs | Silent Friday prod edits |
| Skills | Upskill plan + paired labs | Hire-only freeze |
| BCP | Tied to technical RTO/RPO | Paper plan never drilled |

**Scenario prompt:** CFO hears “cloud is always cheaper”; eng wants unlimited GPUs.

**Expected answer shape:** “I pick OpEx with SKU budgets and CUD where steady because Y, I accept Z (GPU only with utilization SLO).”

#### Concept: On-prem vs colocation vs cloud
**What / why.** Who owns hardware, who patches the hypervisor, who meters capacity. **Cloud** = elasticity, pooled resources, metered billing, API-provisioned capacity. Colocation: you own the gear in someone else’s building. On-prem: you own building + gear.
**Failure modes.** “Lift and shift” without metering; assuming cloud removes patching for *your* guest OS and IAM; treating reserved instances / CUDs as CapEx furniture.
**Point-at.** One Northstar API: on GCE you patch the guest OS; on Cloud Run you do not — same feature, different ownership line (shared responsibility next).

#### Concept: Deployment models — public, private, hybrid
**What / why.** NIST SP 800-145: **public** = open use by the general public (GCP); **private** = exclusive use by one org (on- or off-prem); **hybrid** = composition of two+ distinct infrastructures bound for portability. GCP Architecture Center working definition: **hybrid** = workloads across environments with **one public cloud** and **at least one private** (on-prem/colo) — VPN/Interconnect/NCC later in Part 8b. SaaS-alongside-GCP (e.g. Gmail + a project) is **not** hybrid in that guide’s scope.
**Failure modes.** Calling any VPC “private cloud”; hybrid without identity/network/DNS story; assuming “private” means “no shared fate with the provider’s control plane”; lift-and-shift to GCP alone labeled “hybrid.”
**Point-at.** Northstar v0 on public GCP; factory historian on-prem + HA VPN later = hybrid — not multi-cloud. Office+branch metaphor: DC = private, GCP = public, **leased fiber later** (**Interconnect / HA VPN → Part 8b** — name only now; **Prop Lock**).

#### Concept: Deployment models — community and multi-cloud
**What / why.** NIST **community** = exclusive use by several orgs with shared concerns (mission/security/compliance) — rare on PCA; know the name. GCP **multicloud** = architecture with **≥2 public CSPs** (orthogonal to hybrid). “Hybrid and multicloud” = two+ publics **and** private. Not a default for Northstar — duplicate skills, networking, identity, egress.
**Failure modes.** Multi-cloud for “avoid lock-in” without ops-tax math; conflating hybrid (public+private) with multicloud (two publics); calling Workspace+GCP “multicloud”; community ≠ “our Slack community.”
**Point-at.** Two landlords: app on GCP **and** AWS = multicloud. Prefer single public cloud until an explicit constraint appears.

#### Concept: Service models — IaaS
**What / why.** **IaaS** = you rent VMs/disks/network (Compute Engine). You choose OS images, patch guest OS, size machines, own much of the blast radius above the hypervisor.
**Failure modes.** Treating GCE like PaaS; never patching; leaving idle external IPs (0.1 / 6.3).
**Point-at.** `gcloud compute instances create` (later lab) — you still SSH and patch.

#### Concept: Service models — PaaS (and FaaS slice)
**What / why.** **PaaS** = you bring code/container; platform supplies runtime, scaling, HTTPS URL (App Engine, Cloud Run). **FaaS** is a PaaS slice focused on event functions (Cloud Run functions / Cloud Functions) — still “you secure the code and IAM.”
**Failure modes.** Needing a custom kernel on Cloud Run; assuming scale-to-zero means zero security duty; equating “PaaS” with “no VPC needs.”
**Point-at.** Same JSON health API on Cloud Run — no guest OS login.

#### Concept: Service models — SaaS
**What / why.** **SaaS** = you use the application (Workspace email/calendar, many third-party tools). Least customization; still IAM and data-handling duties as a *customer*.
**Failure modes.** Shadow SaaS with customer PII; assuming SaaS vendor IAM replaces your GCP IAM for *your* projects.
**Point-at.** Staff mail on Workspace vs Northstar API on Cloud Run — different service models on purpose.

#### Concept: Shared responsibility
**What / why.** Google secures the cloud (facilities, hypervisor, global network); **you** secure IAM, data classification, application code, who can invoke, bucket ACLs/uniform access, and (on IaaS) guest OS patching. A misconfigured public bucket is on you.
**Failure modes.** “GCP is secure so our app is secure”; leaving `allUsers` on a bucket; Owner on every human “for speed.”
**Point-at.** Cloud Run: Google patches the sandbox host; you still fix OWASP in the container. GCE: you also patch the guest OS.

#### Concept: CapEx vs OpEx (PCA 4.2)
**What / why.** **CapEx** = buy servers/upfront gear. **OpEx** = pay per second/month for metered services. Committed use discounts are still OpEx with a term — not a return to CapEx furniture accounting.
**Failure modes.** “Cloud is always cheaper”; buying GPUs CapEx-style without utilization SLO; ignoring egress and idle SKUs in OpEx forecasts.
**Point-at.** Northstar cost model (0.1): Run + DB choice billed monthly with a $10 budget alert — OpEx with guardrails.

#### From scratch / exercise
- **Classification (answer key required):** classify 10 Northstar components (storefront, API, DB, cache, CI, secrets, CDN, scheduler, webhook worker, admin UI) as IaaS/PaaS/SaaS and defend each in one sentence.
- **Answer key (typical Northstar v0):** storefront static/Hosting or Cloud Run = PaaS; API Cloud Run = PaaS; DB Cloud SQL = PaaS (managed) or GCE Postgres = IaaS; Memorystore = PaaS; Cloud Build = PaaS; Secret Manager = PaaS; Cloud CDN = PaaS-ish edge service; Cloud Scheduler = PaaS; worker on Cloud Run/GCE = PaaS/IaaS; admin via IAP = still your app on PaaS + Google SaaS-ish identity. Defend deviations.
- Separate drill: label three scenarios public / private / hybrid / multi-cloud / community — **after** both deployment-model anchors — with answer key in notes.

#### HLD / ADR prompt
- One-pager: “Why Northstar starts public + PaaS-heavy.” ADR: “I pick Cloud Run + managed DB OpEx because Y, I accept Z (less OS control; CUD later if stable).” Explicitly reject multi-cloud for v0 unless a constraint is written.

#### LLD / IAM / Terraform shape
- No live org required. Sketch: one project label `env=dev`; note future folders (0.3). IAM idea only: humans in groups, not “everyone is Owner.” Terraform: none required yet — diagram + ADR file in git.

#### GCP lab (free-tier boxed)
- Paper + console tour only: open Compute Engine vs Cloud Run vs Workspace admin (if present) and write one shared-responsibility line each. **Credits-optional:** none. Do not create billable VMs here.

#### Gate
- Draw shared-responsibility line for Cloud Run vs GCE for “who patches the guest OS?”
- Unseen: CFO demands CapEx Kubernetes cluster for one API + Postgres — answer with IaaS vs PaaS and OpEx framing (anchored terms only).
- Nearby: pick public vs hybrid for “on-prem card terminal must stay” without saying multi-cloud.

#### PCA: CapEx / OpEx and service model
- **Considerations:** finance language on case studies; “move to cloud” without naming IaaS vs PaaS fails.
- **Decision table:**

| Need | Model | Accept |
|---|---|---|
| Custom kernel / appliance | IaaS (GCE) | You patch OS |
| HTTP container, least ops | PaaS (Cloud Run) | Less OS control |
| Email/calendar for staff | SaaS | Little customization |

- **Scenario prompt:** CFO wants CapEx for “our own Kubernetes hardware” to save money. Northstar is one API + Postgres.
- **Expected:** “I pick Cloud Run + Cloud SQL OpEx because Y (elastic, no cluster tax), I accept Z (less bare-metal control, commit discounts later if stable).”

### F3 Google Cloud global infrastructure


**Incident doctrine (Pedagogy §7):** region/zone, multi-region/dual-region (GCS), and global/regional/zonal resource scope are **three separate intuition clusters**. Never one vocabulary check spanning all four location-type words plus an unintroduced product. Anchor GCS before any `US` / `nam4` translation item. **Prop Lock:** MUST NOT use VPC / subnet / firewall (Part 6) as create-dialog props or classification items in F3.

#### Concept: Region vs zone (VM failure domain)
**What / why.** A **region** is an independent geographic area that typically consists of **three or more zones** in three or more physical data centers (example: `us-central1` Iowa). A **zone** is a deployment area inside a region — **treat as a single failure domain** (power/network/cooling). Two VMs in `us-central1-a` and `us-central1-b` survive a **single-zone** outage; a whole-region event can still take both. Zone letter `a` in Iowa is unrelated to `a` in `europe-west1`. Some regions historically pack zones into fewer physical DCs — business-critical data may still need dual-region or cross-region backup (awareness).
**Failure modes.** “Multi-zone” said when both instances are actually the same zone; assuming zone HA equals multi-region DR; using zone names as if they were regions in APIs; assuming every region has identical DC topology.
**Point-at.** Two GCE VMs (paper or live): `us-central1-a` vs `us-central1-b`. Narrative: zone `a` power event → only `a` VM down; Iowa-wide event → both down. Latency/residency: EU vs US constraints appear on PCA cases — pick region for data gravity first.
**Vocab check (this anchor only):** classify `us-central1-a`, `us-central1`, `europe-west1-b` as zone or region — **do not** include `US` or `nam4` here.

#### Concept: Multi-region vs dual-region (GCS object locations)
**What / why.** Introduce **Cloud Storage (GCS)** as object storage: you create a **bucket** in a **location** (sticky at create — relocate means copy/move, not a toggle). Objects live in that location’s durability design. **Multi-region** = a *named large geography* containing ≥2 regions (codes `US`, `EU`, `ASIA`) — Google chooses centers (≥100 miles apart); you do **not** pick which two. **Dual-region** = a *named pair*: predefined codes (e.g. `nam4` = `us-central1` + `us-east1` Iowa+South Carolina; also `asia1`, `eur4`, …) **or** configurable (parent code like `US`/`EU` + explicit placement pair). Geo-replication is **async** after the first-region durable write: default designed RPO ~1 hour for 99.9% of new objects / **12 hours** for 100%; **turbo replication** (dual-region only) targets **15 minutes** RPO; designed RTO 0 (same bucket name, automated failover — active-active, not two buckets).
**Failure modes.** Treating `US` as “the us-central1 region”; treating `nam4` as a multi-region; testing these codes before this GCS anchor; assuming dual-region is “two multi-regions”; putting a `US` multi-region bucket under a single-region analytics VM and being surprised by latency/egress; assuming unreplicated brand-new writes survive a source-region catastrophe.
**Point-at.** Console bucket location picker: Region (e.g. Iowa / `us-central1`) vs Dual-region (e.g. Iowa+South Carolina / `nam4`) vs Multi-region (`US`). Whiteboard the three strings. Optional story: VM in `us-east1` reading `nam4` is served from South Carolina; SC outage → failover to Iowa, **same** `gs://` name.
**Vocab check (after this anchor):** classify `US`, `EU`, `nam4`, `asia1` — still **not** mixed with zonal VM IDs in the same quiz unless region/zone already confirmed and you are doing a deliberate mixed transfer with both anchors unlocked.
**Decision (GCS only):** colocated compute+storage → prefer **region**; precise pair + short RPO → **dual-region** (+turbo if needed); broad content / cost-sensitive geo HA → **multi-region**; short-lived data → prefer region (avoid replication charges).

#### Concept: Global vs regional vs zonal resources
**What / why.** Every GCP resource has a **scope** (Compute docs: global / regional / zonal). Teach the *scope* idea with **Prop-Lock-safe** objects only — already unlocked or same-unit-anchored **before** use. **MUST NOT** require VPC, subnet, or firewall rule as props or classification items here (those unlock in **Part 6.2+** after **T.SysTheory Networking** UG + addressing theory).
- **Same-unit minimal anchors (before any scope vocab):**
  - **GCE VM** = a rented computer that **lives in one zone** (create dialog: pick zone). No VPC story required for this intuition — treat networking as “the VM has connectivity Google provides” until Part 6.
  - **Zonal Persistent Disk (optional):** a disk resource attached in the **same zone** as the VM; zone loss ⇒ recreate/restore from snapshot.
  - **Cloud Run (same-unit, light):** a managed container service whose create dialog picks a **region** (not a zone) — enough to contrast with the zonal VM; deep Cloud Run ops stay in **Part 1**.
  - **GCS** (already anchored above): location *type* (region / dual / multi) is **not** the same question as resource *scope* (zonal / regional / global) — keep the distinction explicit.
- **Zonal scope:** resource lives in one zone — **GCE VM**, optional zonal PD. Zone loss ⇒ that resource is gone until recreate/restore.
- **Regional scope:** resource is pinned to one region — **Cloud Run** (after light anchor). (Regional static IPs, regional disks/MIGs, regional LB forwarding rules, Cloud SQL HA — **name + defer** to Parts 1/2/6; do not classify until those owners unlock.)
- **Global scope (control-plane / namespace — light):** some *configurations* and *names* are project-global (e.g. a machine **image** resource id; GCS **bucket name** uniqueness). **Project-level IAM** as “global IAM control plane” is **postponed to 0.5** — do not vocab-check IAM scope here. **Global HTTPS LB / anycast** — name only; deep dive in **1.12 / 6.13**.
- **GCS nuance (after GCS anchor):** bucket *name* is a global namespace (`gs://…` unique worldwide); *data* residency is the chosen **location type** (region / dual / multi). Scope ≠ location-type.
**Failure modes.** Expecting a zonal PD to move without snapshot/clone; treating a GCS `US` **location code** as a “global resource scope” synonym; assuming “IAM is in us-central1” (defer precise IAM scope to **0.5**); believing an edge/anycast front door alone = multi-region HA without multi-region backends; smuggling VPC/subnet/firewall into the scope quiz (**Prop Lock** / instructor process failure).
**Point-at (Prop-Lock-safe create dialogs only):**
1. Create **VM** → must pick a **zone** → zonal.
2. Optional: create/attach **zonal disk** → same zone as VM.
3. Create **GCS bucket** → pick location type (region / dual / multi) — already anchored; contrast *location type* with *scope*.
4. Create **Cloud Run** service → pick a **region** → regional (light same-unit anchor).
**Do not** walk VPC → subnet → VM dialogs. **Do not** ask learners to classify VPC, subnet, or firewall rule.
**Cross-link:** VPC / subnet / firewall **scope labs and classification** → **6.1b + 6.2+** after **T.SysTheory Networking** UG (+ addressing / subnet-as-partition theory). Official fact when that unlocks: VPC networks (and associated routes/firewall rules) are **global** resources; **subnets are regional** ([VPC networks](https://cloud.google.com/vpc/docs/vpc)).

#### Concept: Edge — PoP, Cloud CDN, GFE
**What / why.** Users often hit a **Google Front End (GFE)** / **Point of Presence (PoP)** near them; **Cloud CDN** caches at the edge; your **origin** may still be regional. A global anycast front door can present one IP while backends remain regional resources (LB SKUs deepen later).
**Failure modes.** Believing CDN makes the database multi-region; confusing edge TLS terminate with origin residency.
**Point-at.** Browser → nearby PoP/GFE → (optional CDN hit) → regional origin in `europe-west1` for EU data (Cloud Run after light anchor, or “regional API” wording).

#### From scratch / classification exercise
- **Python then Go:** package `gcpscope` — given a fixed table of `(product_or_location, tag)`, assert tags in `{zonal, regional, multi-region, dual-region, region, zone}`. Wrong tag fails.
- **Fixture (Prop-Lock-safe — F3 gate):** `gce_vm`, `zonal_pd`, `cloud_run` (only after light regional anchor), `us-central1-a`, `us-central1`, `US`, `nam4`.
- **MUST NOT include in F3 fixture / vocab check:** `vpc`, `subnet`, `firewall_rule`, `global_https_lb` (postpone to **6.2+** / **1.12**), or IAM principals/roles (postpone to **0.5**).
- **Answer key (authoritative for F3 gate):** VM/PD zonal; Cloud Run regional; `us-central1-a` zone; `us-central1` region; `US` multi-region (GCS location type); `nam4` dual-region (GCS). Part 6 reuses scope words for VPC/subnet/firewall **after** those anchors — do not silently change meanings; do not pull those items back into F3.

#### HLD / ADR prompt
- Place Northstar API: single region multi-zone vs multi-region active/active. ADR: “I pick a **regional** managed API (Cloud Run in an EU region after Part 1 depth) for residency because Y, I accept Z (US editors higher latency; not a second SoR).” If using GCS for assets: choose `EU` multi-region vs regional bucket vs dual-region with explicit RPO story. **Do not** require a VPC diagram in this ADR.

#### LLD / IAM / Terraform shape
```hcl
# Illustrative — locations only; do not apply paid dual-region casually
resource "google_storage_bucket" "assets" {
  name     = "ns-assets-${random_id.suf.hex}"
  location = "EU" # multi-region; or "nam4" dual-region; or "europe-west1" regional
  uniform_bucket_level_access = true
}
# Cloud Run regional (Part 1 deepens; location illustrates regional scope)
resource "google_cloud_run_v2_service" "api" {
  name     = "ns-api"
  location = "europe-west1"
}
```
- IAM: bucket not public; Run SA later (1.5). Org policy residency constraints mentioned as future (0.3/0.5). **No** VPC/subnet resources in this LLD sketch.

#### GCP lab (free-tier boxed)
- `gcloud compute regions list` / `gcloud compute zones list --filter=region:us-central1` (read-only).
- Classify **only** the Prop-Lock-safe unit-test table (no VPC/subnet/firewall; no create of those required).
- **Credits-optional:** create a regional Nearline/Standard bucket in one region, upload a tiny object, delete bucket same sitting. Prefer **not** creating dual-region/multi-region buckets on trial credits without a destroy checklist.
- Console: Storage → bucket create UI — point at location type dropdown (region / dual / multi) without necessarily creating. Optional: Compute Engine → create VM UI — point at **zone** picker (do not require custom VPC).

#### Gate
- Unseen: “Media app needs EU residency but US editors” — pick placement + what you accept (PCA shape) using unlocked location/scope terms only.
- Nearby transfer: given only unlocked terms, explain why `nam4` is not a zone and not the `US` multi-region; explain why a GCE VM is zonal while a GCS `US` code is a multi-region **location type**.
- **Must not** gate on VPC/subnet/firewall classification, LB SKU deep-dives, Spanner multi-region, or IAM “global vs regional” — those unlock later (**6.2+**, **1.12**, **0.5**).

#### PCA: placement and blast radius
- **Considerations:** design for locality; HA across zones; regional origin vs edge front door (deep LB later); data residency.
- **Decision table:**

| Constraint | Placement | Accept |
|---|---|---|
| HA API, single region OK | Regional managed API (Cloud Run) + multi-zone awareness | Region outage downs you |
| Edge users worldwide | Edge/PoP + regional origin (LB SKUs later) | Origin still regional unless you design multi-region backends |
| EU-only personal data | EU region + residency controls | Higher latency for US users |
| GCS durability across US | `US` multi-region or `nam4` dual-region | Cost / placement control trade-off |

- **Scenario prompt:** Altostrat-style media app needs EU residency but US editors.
- **Expected:** “I pick EU region for SoR + controlled editor access because Y, I accept Z (cross-region tooling latency, not a second SoR in US).”

### F4 Account setup (from the video outline, required)


#### PCA: 5.2 Programmatic interaction

**Guide themes (matrix):** Cloud Shell/Code; gcloud/gsutil/bq; Cloud Emulators; Terraform; API clients. Homes: F4, 0.2, 2.7, all labs.

| Task | Prefer | Accept |
|---|---|---|
| IaC | Terraform | Console clicks for one-off learn |
| Local | Emulators (Spanner/Firestore/Pub/Sub/Bigtable) | Live paid always |
| CLI | gcloud + WIF in CI | Embedded keys |

**Scenario prompt:** Learner refuses Terraform “because console is faster.”

**Expected answer shape:** “I pick Terraform + emulator labs because Y, I accept Z (console only for exploration, then codify).”

#### Concept: Resource hierarchy attachment
**What / why.** Org → folder → project → resource. IAM allow policies and organization policies inherit down. Billing **attaches** to projects (deepen in 0.1); hierarchy is the security/quota boundary (deepen in 0.3).
**Failure modes.** Creating resources at org “because convenient”; one project forever for prod+dev.
**Point-at.** Console: IAM & Admin → Resource Manager tree — name each level once.

#### Concept: Free tier vs trial vs Always Free
**What / why.** Always Free SKUs ≠ “cannot bill.” Trial credits expire; enabling APIs is free until use; misconfigured LBs/NAT/static IPs bill.
**Failure modes.** Leaving trial projects linked after experiments; assuming Cloud SQL is free; ignoring budget alerts.
**Point-at.** Billing → budgets (create $10 in 0.1 lab) — F4 only confirms billing is linked carefully.

#### Concept: Securing the account (2SV and break-glass)
**What / why.** 2-Step Verification, recovery codes, super-admin hygiene: break-glass accounts are monitored exceptions, not daily Drivers.
**Failure modes.** Shared password owner account; super-admin used for `gcloud` deploys; no recovery codes offline.
**Point-at.** Security checkup: 2SV on; document break-glass in `docs/break-glass.md` (no secrets in repo).

#### Concept: Console surfaces
**What / why.** Search, Cloud Shell, IAM, APIs & Services, Billing — five places you will live. Console is for learning and break-glass; steady state is CLI/Terraform.
**Failure modes.** ClickOps with no export; never opening APIs & Services when “permission denied” is actually “API disabled.”
**Point-at.** APIs & Services → Enabled APIs list for the active project.

#### Concept: APIs closed by default
**What / why.** Many GCP APIs are disabled until enabled per project. Enable is free; **use** meters. Quotas are safety rails against surprise scale.
**Failure modes.** Interpreting `API not enabled` as IAM failure; requesting huge quota before a budget exists.
**Point-at.** `gcloud services enable run.googleapis.com` then `gcloud services list --enabled`.

#### Concept: Separation of duties (SoD)
**What / why.** Organization Admin ≠ Billing Admin ≠ Project Owner on the same standing human if you can avoid it (PCA 3.1). Groups bind roles; individuals inherit via membership.
**Failure modes.** Every engineer `roles/owner` at org; billing admin also pushes prod.
**Point-at.** Decision table in PCA block below — map one human to one standing duty.

#### Concept: Cloud SDK tool family
**What / why.** `gcloud` (most APIs), `gsutil` (GCS), `bq` (BigQuery), `kubectl` (GKE later). `gcloud init`, named configurations, components.
**Failure modes.** Wrong configuration → wrong project; installing random kubectl that drifts from GKE.
**Point-at.** `gcloud config configurations list` and `gcloud config get-value project`.

#### Concept: Cloud Shell, Editor, Cloud Code
**What / why.** Cloud Shell = ephemeral VM with SDK + your user identity; Editor/Cloud Code speed labs. Not a production bastion architecture.
**Failure modes.** Storing long-lived keys only in Shell home; assuming Shell disk persists forever without backup.
**Point-at.** Open Cloud Shell; `echo $CLOUD_SHELL`; run `gcloud auth list`.

#### Concept: Project ID vs number vs name
**What / why.** **Name** is cosmetic; **Project ID** is the immutable-ish string you put in Terraform and CLI; **number** is numeric unique id used in some resource names/APIs.
**Failure modes.** Renaming display name and expecting ID change; hard-coding name instead of ID.
**Point-at.** `gcloud projects describe PROJECT_ID --format='value(projectId,projectNumber,name)'`.

#### Concept: Quotas as safety rails
**What / why.** Default quotas cap CPUs, APIs, LB rules, etc. Hitting a quota is often good (stopped a runaway). Increase is a conscious risk acceptance.
**Failure modes.** Panic-raising quotas without budgets; ignoring regional vs global quota dimensions.
**Point-at.** Deliberate aggressive `list` or describe a low quota in console → document which quota metric fired.

#### From scratch / exercise
- Write a one-page “landing checklist”: hierarchy sketch, billing linked, 2SV, budget stub, APIs to enable for Northstar v0 (Run, Artifact Registry, …), SoD named humans/groups.
- Classify 5 error strings: API disabled vs IAM denied vs quota exceeded vs wrong project (answer key in notes).

#### HLD / ADR prompt
- ADR-000: “Landing zone minimum for Northstar labs.” Decision: one nonprod project under a folder; SoD roles; Terraform for project services. Accept: slower first day than Owner-for-all.

#### LLD / IAM / Terraform shape
```hcl
resource "google_project_service" "run" {
  project = var.project_id
  service = "run.googleapis.com"
  disable_on_destroy = false
}
# IAM bindings via groups — no user emails in prod modules when avoidable
```
- Document named gcloud config: `gcloud config configurations create northstar-nonprod`.

#### GCP lab (required; free-tier boxed)
- New project; link billing carefully; enable APIs you need; second admin user in a **group**; `gcloud` from Cloud Shell and local; hit a quota wall on purpose (e.g. aggressive list); document the error and which quota.
- Tear-down note: leave project or set budget $10 same day (0.1).

#### Gate
- Can create a project, set `gcloud config set project`, and explain why Organization Admin should not be the daily deploy identity.
- Unseen: error `SERVICE_DISABLED` vs `PERMISSION_DENIED` — which console pane first?
- Nearby: pick Project ID vs name for a Terraform variable.

#### PCA: org hierarchy and SoD
- **Considerations:** PCA 3.1 identity/access; landing zone starts with org + billing; break-glass.
- **Decision table:**

| Role need | Binding | Accept |
|---|---|---|
| Pay invoices only | Billing Admin on billing account | Cannot deploy |
| Deploy Northstar | Custom/predefined on project via group | No org-wide Owner |
| Emergency | Break-glass user + monitored | Higher risk if used casually |

- **Scenario prompt:** Startup gives every engineer `roles/owner` at org level “for speed.”
- **Expected:** “I pick group-scoped project roles + SoD because Y, I accept Z (slightly slower first week, much smaller blast radius).”

## Part M — Quantitative prerequisites used by this syllabus (complete when listed)

Not a full analysis/PhD spine. If it is listed, it is taught to the theoretical floor.

| Topic | Why here | Complete means |
|---|---|---|
| Bits, integers, floats, error, tolerance | **T.Disc** binary literacy + **M.NS** (mainstream); F1 uses “bit” by recall | Full IEEE/conditioning/Kahan/logsumexp in M.NS before Part 0 — recall T binary literacy, do not re-teach place values |
| Functions, composition, inverse | **T.Alg** teach; M / 9c **recall** | Counterexample to a false inverse claim — M does not re-teach “what is a function?” |
| Vectors, norms, dot product, cosine | 9c two-tower | Derive cosine; degenerate cases |
| Matrices, least squares, SVD/PCA as used | embeddings, not spectral theory as a career | Residual and reconstruction error |
| Probability: sample space, elementary P, conditional-by-table | **T.ProbStat** teach language; **M.ML** / SLO / A/B deepen metrics/IPS | T.ProbStat owns measure language; M.ML owns ERM/metrics/IPS — no duplicate sample-space course |
| Entropy, cross-entropy, KL as used | 9c metrics | Derive CE from likelihood |
| Recurrences, Master theorem as used | 8.1 hash/bloom, sort | Match a loop to a recurrence |
| Limits, derivatives, integrals as used | SLO burn, GD, 9c losses | Derive the move; numerics with tolerance |
| Convex sets, convex functions, GD, Lagrange | T-OPT from 9c | KKT as used; not a convex-analysis PhD unless T-OPT ceiling is opened |
| Sampling theorem / DFT as used | T-SIGNAL from 9c.6 | Predict aliasing |
| NumPy `ndarray` | F1, 9c scratch | Predict shape/dtype/strides/broadcast; copy vs view |
| Ranking / IPS / position bias | **M.ML** IPS + **9c.0** / 9c.2 | Derive propensity + Horvitz–Thompson IPS on synthetic click logs; Python tests + Go helper |
| Classical time series (trend/seasonality/holidays) as used | **M.TS** + **9c.0** / 9c.3 | Decompose tiny series; residual ACF idea; when BQML ARIMA/seasonal beats DL |
| Causal / uplift lite (potential outcomes; A/B vs observational) | **M.CAUSAL** + **9c.0** / 9c.3 + Marketing | Two-arm toy table; uplift = treatment effect; full DAGs → T-CAUSAL / 12.S14 |

Hand-trace → derive → tiny Python → tests → then a service may consume the number in Go. **T-OPT / T-IT** are complete when opened from this table’s rows.

### M.NS Numerical stability (mainstream — Python then Go)


Taught **here**, before Part 0, not in Part 12. Required before 9c softmax/attention, SLO numerics, and money in integer cents (Part 5). Theoretical floor: derive, then implement both languages. Do not reimplement a BLAS.

**Theory (derive, do not slogans):**
- IEEE-754 binary64/binary32: sign, biased exponent, trailing significand; implicit bit; subnormals; ±0, ±∞, NaN payloads; `qNaN` vs signaling as used.
- Rounding: RN/RZ/RU/RD; **machine epsilon** ε; **ulp**; `fl(x)` = x(1+δ), |δ|≤ε.
- Absolute vs relative error. **Forward** error vs **backward** error.
- **Condition number** of a *problem* κ vs **stability** of an *algorithm*. Ill-conditioned + stable can still be useless; well-conditioned + unstable is a bug.
- Catastrophic **cancellation**; loss of trailing digits when subtracting close values.
- FP add is not associative; parallel reductions change results.
- Overflow / underflow / gradual underflow.
- Fused multiply-add (FMA) when the platform has it.
- Unstable recurrences vs reformulation (`log1p`, `expm1`, `hypot`, two-sum / Kahan).
- Linear systems: κ₂(A)=σ_max/σ_min; residual vs true error; Hilbert matrix as a trap.
- ML-facing: softmax overflow; **log-sum-exp**; log-space likelihoods; scaled dot-product attention (1/√d).
- Comparison: never `==` on computed floats. Combined abs+rel tolerance; ulp distance. NaN unordered.
- **Python integers** are unbounded; **Go** `int`/`int64` wrap (two’s complement). Mixing is a defect. Part 5 money is integer cents.

**Python artifact (`stability` package + pytest):**
- Classify fp values (`finfo`, `isinf`, `isnan`, subnormal).
- Measure ε experimentally (`1+ε != 1`).
- Cancellation: `(1+x)-1` vs `x` for x near ε.
- Kahan / pairwise sum vs naive; error growth ~nε vs ~ε.
- `hypot`, `log1p`, `expm1`, log-sum-exp vs naive exp-sum.
- Residual vs error on a mildly ill-conditioned 2×2; Hilbert n=8 as a warning.
- Softmax three ways: naive, max-shift, log-softmax; match where finite.
- Tolerances **justified** from ε, not magic `1e-6`.

**Go artifact (`stability` package + table tests):**
- Same algorithms in `float64` (`math`, `Nextafter`, `IsNaN`, `IsInf`).
- Integer: `bits.Add64` overflow flag; wrap of `uint64` max+1.
- Comparison helper: abs+rel+NaN; tests include ±0, inf, NaN.
- LogSumExp, Hypot, Kahan; softmax max-shift.
- When `float32` (memory) vs `float64` (default here).

**Gate:** derive κ vs stability on one example; predict a cancellation failure then show it in **both** languages; ship both packages; one unseen reformulation (`log1p` / `hypot` / Kahan / LSE). Unstable code with `==` or a huge slop is **not** complete.

### M.ML Empirical risk, losses, metrics (required before 9c / PMLE)


Taught **here**, complete before Part 9c / PMLE. Same density contract as **M.NS**: derive → tiny Python package → Go metric helpers → gate. Do not open Part 12 for this. Softmax / log-sum-exp numerics stay **M.NS**. Classical model zoo stays at the **end of 9c** (one home).

#### Concept (derive, do not slogans)

**i.i.d. and the split.** (**Recall T.ProbStat** sample space / event / Σ averages — do not re-teach elementary probability toys.) Training examples \((x_i, y_i)\) are modeled as draws from a joint \(P\). Empirical risk is the average loss on the sample:
\[
\hat{R}(f) = \frac{1}{n}\sum_{i=1}^{n} \ell(f(x_i), y_i).
\]
The i.i.d. story fails when the split leaks: time (future into past), group (same user/order in train and test), or **target leakage** (a feature that is a function of \(y\) at prediction time). Train / val / test must be justified by the serving time axis. A “random 80/20” on time-ordered events is a defect until proven otherwise.

**MSE from first principles.** For regression \(f_w(x)=w^\top x\) (bias folded into \(x\)) and \(\ell=(f-y)^2\):
\[
\hat{R}(w)=\frac{1}{n}\sum_i (w^\top x_i - y_i)^2.
\]
Gradient (derive component-wise, then vector form):
\[
\nabla_w \hat{R}(w) = \frac{2}{n} X^\top (Xw - y).
\]
One **gradient descent** step: \(w \leftarrow w - \eta \nabla_w \hat{R}(w)\). Closed form \(w=(X^\top X)^{-1}X^\top y\) is the check, not the production path when \(p\) is large or streaming.

**Logistic / log-loss from likelihood.** Binary \(y\in\{0,1\}\), \(p=\sigma(w^\top x)=\frac{1}{1+e^{-w^\top x}}\). Bernoulli NLL / binary cross-entropy:
\[
\ell = -y\log p - (1-y)\log(1-p).
\]
Derive \(\frac{\partial \ell}{\partial w} = (p-y)\,x\) (one example by hand). Average over the batch for GD. Numerically stable path uses `log1p` / clipped logits — tie to **M.NS**.

**L2 (and L1 as sparsity).** Complexity control: \(\hat{R}_\lambda = \hat{R} + \frac{\lambda}{2}\|w\|_2^2\) adds \(\lambda w\) to the gradient. Bias–variance in words + a 1-D cartoon you can plot: too little \(\lambda\) → wild fit on noise; too much → underfit. L1 pushes coordinates to zero (feature selection cartoon). Regularization vs more data vs simpler model: name which lever you pull and why (PMLE interpretability literacy: linear/trees explainable; DNN/LLM need different evidence).

**Metrics you implement (no sklearn-as-only-proof).** From the confusion matrix \(TP,FP,FN,TN\):
- Precision \(= TP/(TP+FP)\); Recall \(= TP/(TP+FN)\); F1 \(= 2PR/(P+R)\).
- Accuracy lies under imbalance — fraud and rare stockouts.
- ROC: treat score as a ranking; sweep threshold; plot TPR vs FPR; AUC as pairwise ranking probability (derive on a 4-point toy).
- PR curve when positives are rare.
- **Calibration:** reliability diagram idea — among examples with score \(\approx 0.8\), about 80% should be positive. ECE as a coarse check; do not confuse ranking AUC with calibrated probabilities.

**When which metric hides failure.** Catalog rank: high accuracy on “not clicked” is useless — use ranking utility / NDCG / pairwise. Fraud: optimize recall at a fixed FPR budget the HITL queue can afford; AUC alone hides operating-point pain.

#### From scratch (Python `ermetrics` / `erml` package + pytest)

Ship a small package (name in ADR): no sklearn required for the gate proofs.

1. **Leak-free split:** `event_time`-aware cut or group split; unit test that a future-label join fails.
2. **Linear MSE GD:** one step and multi-step on a tiny table; residual decreases; compare to normal equations within tolerance justified by ε (**M.NS**).
3. **Logistic GD:** hand-derived \(\partial\ell/\partial w\) for one row matches code; one GD step moves loss down on a linearly separable toy.
4. **L2:** same problem with \(\lambda>0\); \(\|w\|\) shrinks vs unregularized.
5. **Metric suite:** confusion matrix, precision, recall, F1, ROC points, AUC (trapezoid or Mann–Whitney form), reliability bins — pure NumPy/stdlib.
6. **Broken split that leaks:** feature `label_tomorrow` or same-group leakage; test **must fail** a leakage assertion.
7. **Calibration toy:** overconfident scores → high ECE; temperature or Platt sketch optional, not required.

#### Go artifact (`ermetrics` package + table tests)

Port **metric helpers** (not full GD training unless you want it): confusion counts, precision/recall/F1, ROC/AUC on `[]float64` scores + labels, abs+rel float compare from **M.NS**. Table tests include empty input, all-positive, all-negative, ties in scores. Fraud vs rank fixture: same scores, different operating-point helpers.

#### Gate

- Derive \(\mathrm{d}(\text{log-loss})/\mathrm{d}w\) for one labeled example; match code.
- Compute precision/recall/F1 and one ROC point **by hand**, then by package.
- Name a metric that would **hide** a failure in Northstar fraud vs catalog rank.
- Ship Python package + Go helpers; unstable `==` on floats or sklearn-only proof is **not** complete.

#### Ranking / IPS / position bias (derive — one home)

Click logs are **not** relevance labels: position \(k\) has propensity \(p_k = P(\text{examined}\mid k)\). Under a position-based examination model, observed click \(c_{i,k}\) has
\[
\mathbb{E}[c_{i,k}] = p_k \cdot r_i
\]
where \(r_i\) is relevance (or click propensity given examination). The **inverse propensity score (IPS)** / Horvitz–Thompson-style estimator reweights:
\[
\hat{R}_{\mathrm{IPS}}(f) = \frac{1}{n}\sum_{i=1}^{n} \frac{c_i}{\hat{p}_{k(i)}}\,\ell\big(f(x_i), \tilde{y}_i\big)
\]
(or the equivalent click-through utility with \(c_i/\hat{p}_{k(i)}\) as the weight). If \(\hat{p}_k\) is too small, variance explodes — clip propensities and report effective sample size.

**From scratch (Python, extend `ermetrics` / `erml`):**
1. Synthetic click log: items with true \(r_i\), positions 1..K with known \(p_k\), Bernoulli clicks.
2. Naive mean click-by-item vs IPS-weighted estimate; show naive ranks popular-at-top items higher.
3. Pytest: recover ranking order within tolerance when \(p_k\) known; fail if unweighted “wins.”
4. Optional SQL: `SUM(click/propensity)` grouped by item on a tiny BQ-shaped table.

**Go helper:** `IPSWeight(click, propensity float64) (float64, error)` with zero/negative propensity errors; table tests for clip + empty.

**Gate:** derive why \(\mathbb{E}[c/p]=r\) under the examination model; run the toy; name one production failure (propensity misspecification). Owner for systems use: **9c.0** / **9c.2** Search pack — do not re-derive elsewhere.


### M.TS Classical time series as used (required before 9c.3 ETA / demand literacy)


Not a forecasting PhD. Enough to know when **BQML ARIMA_PLUS / seasonal** beats a default DL stack on sparse or strongly seasonal series.

#### Concept (derive / sketch)
- **Trend** \(T_t\): slow level change. **Seasonality** \(S_t\): repeating calendar pattern (hour-of-week, week-of-year). **Holiday / event** effects: sparse spikes not in a fixed seasonal period.
- Additive cartoon: \(y_t = T_t + S_t + R_t\). Multiplicative when amplitude scales with level.
- **Residual** \(R_t\): what remains after removing \(T,S\). Autocorrelation of residuals (ACF idea): if large lag-1 ACF remains, the classical decomposition is incomplete — or you need a better model.
- Train/test: **time cut only** (already **M.ML**); no random shuffle of a series.

#### From scratch (Python)
1. Tiny weekly series (e.g. 52–104 points) with planted trend + day-of-week seasonality + noise.
2. Moving-average / STL-lite or seasonal differencing sketch; plot or print components.
3. Residual lag-1 correlation vs raw series (stdlib/NumPy — no “magic library proves understanding”).
4. One paragraph: when BQML seasonal ARIMA is the right first ship vs tabular/seq DL (data length, interpretability, cold series count).

**Go:** optional metric helper for MAE on a held-out tail; not a second forecasting engine.

**Gate:** decompose one series by hand-ish code; state when classical seasonal beats DL for Northstar ETA/demand. Depth for many-series ops / causal forecast → **9c.0** / **9c.3**; full OR/causal → Part 12.


### M.CAUSAL Causal / uplift lite (required before Marketing lift & causal-forecast slogans)


Experiments (**9c.7**) measure interventions under randomization. This module is the **slogan + one toy** so case studies that say “uplift / causal forecast / incrementality” are not empty words. Full DAGs / identification → **T-CAUSAL** / **12.S14**.

#### Concept
- **Potential outcomes:** for unit \(i\), \(Y_i(1)\) under treatment, \(Y_i(0)\) under control. You observe only one. ATE \(= \mathbb{E}[Y(1)-Y(0)]\).
- **A/B / holdout** ≈ randomized assignment → difference in means is unbiased for ATE (under SUTVA / no interference caveats you can name in one line).
- **Observational** data: treatment correlates with confounders → raw difference ≠ causal effect.
- **Uplift** = conditional treatment effect: who benefits from the message/offer, not who has high baseline \(Y\). Targeting high-\(Y\) responders without uplift wastes budget on always-buyers.

#### From scratch (Python + table)
1. Two-arm toy table (20–40 rows): `treated`, `outcome`, optional confounder.
2. Randomized case: show \(\bar{Y}_1-\bar{Y}_0\) recovers planted ATE.
3. Confounded case: same estimator is wrong; state what an experiment would fix.
4. Uplift cartoon: segment with high baseline vs high *lift* — different targeting lists.
5. SQL optional: `AVG(outcome) GROUP BY treated` on the toy.

**Go:** optional `DeltaMeans` helper with table tests; not a causal library.

**Gate:** define potential outcomes in one paragraph; compute the two-arm delta by hand and in code; write “Experiments ≠ full causal (T-CAUSAL / 12.S14)” on the ledger when a case study claims observational causality. Owner for product use: **9c.0** / Marketing pack / 9c.3.


## Part 0 — Day-zero: billing, IAM core, and how we design

**Why first:** You asked for billing at the start. Google’s landing zone series also starts with organization + billing account. You cannot deploy industry software without this. IAM is here because billing without IAM is an open checkbook.

### 0.1 Cloud Billing (full, not a sidebar)


#### Concept: Billing account vs project vs org/folder
**What / why.** Cloud Billing is **not** a node inside the resource hierarchy; a **billing account** **attaches** to projects. Orgs/folders group projects for IAM and reporting rollups; labels refine cost allocation inside a project.
**Failure modes.** Thinking “billing account IAM” replaces project IAM; orphaned projects without billing; one billing account with no budgets.
**Point-at.** Console: Billing → Account management → linked projects list.

#### Concept: Billing IAM roles (SoD)
**What / why.** Billing account IAM is a **separate plane** from project Owner. Key roles: Billing Account Administrator (`roles/billing.admin`) — pay/link/IAM/exports/budgets/CUDs; Costs Manager (`roles/billing.costsManager`) — budgets + cost view/export, **no** link/unlink; Viewer (`roles/billing.viewer`) — read costs; User (`roles/billing.user`) — link projects (with Project Creator / Project Billing Manager); Creator (`roles/billing.creator`) at org — minimize who can mint new billing accounts. Org *owns* projects; billing account *pays for* linked projects — projects do **not** inherit IAM from the billing account.
**Failure modes.** Organization Admin as the only person who can see invoices; granting Billing Admin to every developer; too many Billing Account Creators → untracked accounts; conflating Billing Admin with Project Owner.
**Point-at.** Skit: CFO = Viewer; FinOps = Costs Manager; platform lead = Admin; app team = User+Creator (open projects, cannot see whole-company invoices).

#### Concept: Invoices, credits, Always Free, trial, CUDs
**What / why.** **Free Trial** = ~$300 Welcome credit / **90 days** (gift card; restrictions while on trial). **Always Free / Free Tier** = monthly product allowances that refresh (do not roll over; many US-region limited). They coexist with paid SKUs in one project once upgraded. Trial ending without upgrade → resources stopped; grace risks data. Budgets are **alerts-only** by default (speedometer, not brake) unless spend-cap/automation is configured. CUDs = OpEx with a term (F2).
**Failure modes.** “We’re on free tier” while Cloud SQL runs; conflating trial with Always Free; budget with no thresholds/recipients; including all promo credits so post-trial run rate is invisible; ignoring credit expiry.
**Point-at.** Cost table: mark each Northstar v0 line Free Tier / Trial-covered / Paid. Billing → Budgets & alerts → 50/90/100% on one project.

#### Concept: SKU group — compute runtimes
**What / why.** You pay for **time×size** and sometimes **requests**: Cloud Run CPU/memory/requests; GCE instance-hours; App Engine instance-hours above **28 F1/day** free.
**Failure modes.** Min instances left high overnight; e2-micro forgotten; App Engine Flexible assumed free.
**Decision / failure.** Prefer scale-to-zero Cloud Run for labs; destroy GCE same day; stay on App Engine Standard free envelope or stop versions.
**Point-at.** One line in cost model: “Run: assume N req/day × cost; GCE: $0 because destroyed.”

#### Concept: SKU group — data and disks
**What / why.** Cloud SQL instance-hours (**no** free tier); Persistent Disk GB-month; Artifact Registry storage; Logging beyond ~50 GiB/month free ingest (verify current Always Free docs when you lab).
**Failure modes.** Dev Cloud SQL left up; PD snapshots pile up; debug logging at MAX in prod.
**Decision / failure.** terraform destroy SQL same sitting; snapshot retention policy; log sampling.
**Point-at.** Cost model red flags: SQL + PD + “forgot destroy.”

#### Concept: SKU group — network edge and idle addresses
**What / why.** Egress; accidental LB forwarding-rule hours; Cloud NAT gateway hours; **reserved static external IPs left idle**; idle public IP on VMs (deepen Part 6.3).
**Failure modes.** Create global HTTPS LB for a hello-world and leave it; reserve static IP “for later”; NAT for one curl.
**Decision / failure.** Free-tier path: Cloud Run URL, no LB/NAT; if you reserve an address, delete with the VM in the same sitting.
**Point-at.** Billing report line `Compute Engine` → `Ip Address` / forwarding rule — map to destroy checklist.

#### Concept: Budgets, alerts, export
**What / why.** (**Recall T.Alg** % thresholds; **recall T.Quant** if SKU units appear.) Budgets + threshold alerts (50/90/100%) catch burn early. Billing export to BigQuery is the programmatic truth (teach; optional lab — export can exceed free tier).
**Failure modes.** Budget with no pub/sub/email; 100%-only alert; export dataset without lifecycle.
**Point-at.** Create **$10** budget with three thresholds before any GCE/SQL experiment.

#### Concept: Labels vs tags for allocation
**What / why.** Labels (`env`, `service`, `owner`) on resources feed billing break-down; tags (org-level) used for policy — know both words exist; use labels in every lab (Pedagogy lab safety).
**Failure modes.** No labels ⇒ “mystery spend”; PII in label values.
**Point-at.** `gcloud run services update ... --update-labels=env=dev,service=api,owner=northstar`.

#### From scratch / code
- Sample Cloud Billing CSV/JSON export checked into the repo as a fixture (never real customer data).
- **Python exercise:** parse export; group cost by `service` + `sku` + label; flag any SKU that is not Always Free for the Northstar v0 shape — **group flags by the SKU concept anchors above**, not one giant “list every SKU name” vocab dump.
- **Go after submit (G5 + G0):** same report as a CLI — flags, env, JSON, `--help`. Recover a broken `go.mod` if the module path is wrong.

#### HLD / ADR prompt
- One-page Northstar v0 cost model: Run + Firestore/SQL choice + Hosting/Build minutes + “destroy same day” risks (idle IP, Cloud SQL). ADR: “I pick no global LB in v0 because Y (SKU), I accept Z (*.run.app URL).” 

#### LLD / IAM / Terraform shape
- Billing account IAM separate from project Owner. Terraform: `google_billing_budget` (may require billing permissions — paper OK if blocked). Labels on every creatable resource module.

#### Lab (required; free-tier boxed)
- Create/link billing; budget **$10** with 50/90/100% alerts; confirm Always Free products you will use; write the one-page cost model.
- **Credits-optional:** enable billing export to BigQuery in a dedicated project; set table expiration; estimate query cost before SELECT *.

#### Gate
- Cost model names idle IP and Cloud SQL as “destroy same day” risks; CLI golden output matches Python twin.
- Unseen: trial half gone; only asset is e2-micro with reserved external IP unused a week — what do you delete first and why (anchored idle-IP SKU)?
- Nearby: classify three invoice lines into compute / data / network SKU groups (not a 15-name vocab blast).

#### PCA: cost control and financial governance
- **Considerations:** PCA design includes cost; budgets/alerts; labeling; choosing managed services with eyes open.
- **Decision table:**

| Risk | Control | Accept |
|---|---|---|
| Surprise bill | Budget + alerts + quotas | Alert fatigue if thresholds silly |
| Idle static IP | Delete address with VM | Must not put ephemeral in DNS |
| Dev Cloud SQL left up | terraform destroy same day | Credits burned if forgotten |

- **Scenario prompt:** Trial credits half gone; only asset is one e2-micro with a reserved external IP unused for a week.
- **Expected:** “I pick release/delete the static IP immediately because Y (idle IP SKU), I accept Z (next recreate may get a new ephemeral — do not put it in DNS).”

#### Go G5 — flags, env, JSON; billing CLI
SYNTAX UNLOCK: `flag.String("o", "-", "output")` then `flag.Parse()`. Env via `os.Getenv` / `os.LookupEnv` — flags override defaults; env overrides hardcoded defaults (document precedence). `encoding/json`: `json.Marshal`/`Decoder`; struct tags `` `json:"service"` ``. `--help` comes free from `flag`. Contrast Python: `argparse` + `os.environ`.
Concept: Same billing report as the Python exercise: group cost by service+sku+label; flag Always Free violations. CLI is the deliverable, not a notebook.
Python twin first: parse sample Billing CSV/JSON; group; flag non-Always-Free SKUs.
Go artifact: package `cmd/billingreport` + `billingparse`; tests: `TestHelpExitZero`, `TestEnvOverridesDefaultProject`, `TestGroupByServiceSkuLabel`, `TestFlagNonFreeSku`; gate: `--help` works; golden JSON output matches Python twin; broken module path recovered with G0 runbook.

---

### 0.2 You, the CLI, and Cloud Shell

#### Concept: gcloud user login vs ADC
**What / why.** `gcloud auth login` authenticates the **CLI** as you. **Application Default Credentials (ADC)** for local libraries come from `gcloud auth application-default login` (or later WIF/metadata). They are related but not identical knobs.
**Failure modes.** Exporting a JSON SA key “so Python works”; assuming CLI login automatically populates ADC always; checking keys into git.
**Point-at.** `gcloud auth list` vs presence/absence of ADC path — prefer user ADC or WIF over key files.

#### Concept: gcloud config and named configurations
**What / why.** Active **project**, default **region/zone**, and **named configs** prevent “I deleted prod.” Quota project for client APIs can matter for billing/quota attribution of API calls.
**Failure modes.** One global config; forgetting to switch after a tutorial project.
**Point-at.** Deliberately run a read-only command against the wrong project; show `gcloud config configurations activate` fixing it.

#### Concept: Cloud Shell as lab identity
**What / why.** Ephemeral home, always-updated SDK, identity is your user — excellent for labs, **not** a production bastion design.
**Failure modes.** Only copy of Terraform state in Shell home; long-lived keys only there; treating Shell as forever disk.
**Point-at.** `echo $CLOUD_SHELL`; note ephemeral warning; clone from git each session if unsure.

#### Concept: Local SDK pin and env
**What / why.** Team docs pin SDK expectations; `CLOUDSDK_CORE_PROJECT` and related env vars override for scripts. Local + Cloud Shell should agree on project ID.
**Failure modes.** Divergent `gcloud` versions breaking scripts; env var pointing at prod in a shell profile.
**Point-at.** `gcloud version`; `echo $CLOUDSDK_CORE_PROJECT`.

#### Concept: JIT Linux for API JSON
**What / why.** Filesystem layout, `$PATH`, permissions, pipes, `jq` turn raw `gcloud ... --format=json` into readable fields.
**Failure modes.** Eyes-only scrolling giant JSON; `sudo` everything.
**Point-at.** `gcloud projects list --format=json | jq '.[].projectId'`.

#### From scratch
- Python then Go: tiny wrapper that runs `gcloud config get-value project` (subprocess) and fails non-zero if empty — CI gate pattern. No GCP mutate.

#### HLD / ADR prompt
- ADR: “Human interactive access via Cloud Shell / local SDK; automation via CI+WIF (Part D).” Accept: slightly more setup than a key file.

#### LLD / IAM / Terraform shape
- No keys in repo (`.gitignore` for `*-key.json`). Document named configs in `docs/gcloud-configs.md`. Terraform later uses CI identity, not laptop Owner.

#### Lab (free-tier boxed)
- `gcloud` from Cloud Shell; list projects; enable APIs via Service Usage; explain why enabling costs nothing until use.
- Deliberately run a command against the wrong project; show how named configs prevent that.
- Decode a forced error with `jq`.

#### Gate
- Can switch configs; can print active project; can decode a `gcloud` JSON error with `jq`.
- Unseen: intern exports `GOOGLE_APPLICATION_CREDENTIALS` to a JSON key — what do you replace it with (anchored ADC/WIF idea)?
- Nearby: write the one-line check CI should run before deploy (`project` non-empty + expected ID).

#### PCA: tooling and operational access
- **Considerations:** PCA 5.2 manage resources with tools; least privilege for human identities.
- **Decision table:**

| Task | Tool | Accept |
|---|---|---|
| Interactive lab | Cloud Shell | Ephemeral disk |
| Repeatable team deploy | CI + WIF (Part D) | No human Owner key |
| Break-glass | Logged Cloud Shell / pampered admin | Audited |

- **Scenario prompt:** Intern exports `GOOGLE_APPLICATION_CREDENTIALS` to a JSON key “so Python works.”
- **Expected:** “I pick ADC user login or WIF because Y (no key files), I accept Z (slightly more setup than a key).”

### 0.3 Resource hierarchy (minimum to deploy)


#### Concept: Org → folder → project → resource
**What / why.** Resource Manager tree: **Organization** (company root) → **folders** (optional grouping) → **projects** (trust + billing linkage + quota boundary) → **resources** (VMs, buckets, Run services). Most “where do I put this?” answers are project-scoped.
**Failure modes.** Creating resources hanging off the org node “because convenient”; endless folder trees; using labels alone instead of separate prod/nonprod projects.
**Point-at.** Console Resource Manager: name each level on a Northstar sketch — `example.com` org → `nonprod` folder → `ns-dev` project → Cloud Run service.

#### Concept: Inheritance of IAM and org policies
**What / why.** Allow policies and **organization policy constraints** inherit down the tree unless overridden (deny/org policy nuance deepens in 0.5 / Part 7). A binding on a folder applies to projects beneath it.
**Failure modes.** Granting Owner at org to “unblock”; assuming a project binding removes a parent allow without understanding effective policy; forgetting org policy can block external IPs even if IAM allows `compute.instances.create`.
**Point-at.** One diagram: group `eng@` → `roles/viewer` on folder `nonprod` → effective on all child projects.

#### Concept: Projects as trust + billing + quota boundaries
**What / why.** Prefer **one org**. Projects isolate IAM blast radius, quotas, and which billing account pays (linkage from 0.1). Labels refine cost *inside* a project; they do not replace project boundaries for prod data.
**Failure modes.** All envs in one project with labels only; shared prod/nonprod SA keys; quota exhaustion in dev starving prod in the same project.
**Point-at.** Decision: separate `ns-prod` / `ns-nonprod` projects even for a tiny team.

#### Concept: Folder layout without explosion
**What / why.** Folders for `shared` / `prod` / `nonprod` (or env × business unit). Avoid folder-per-microservice explosion — folders are governance, not service inventory.
**Failure modes.** 200 folders mirroring Git repos; empty folders “for later.”
**Point-at.** Northstar: `shared` (billing export, CI project), `prod`, `nonprod` — one sentence each.

#### From scratch / code
- **Python then Go:** Resource Manager API (or recorded JSON fixture if org APIs blocked) — list projects, print ancestry path org/folder/project. Tests: parse fixture ancestry; reject “resource parented at org” fake entries.

#### HLD / ADR prompt
- Northstar folder layout one-pager. ADR: “I pick separate prod/nonprod projects because Y (IAM/quota/billing blast radius), I accept Z (more projects to govern).”

#### LLD / IAM / Terraform shape
```hcl
resource "google_folder" "nonprod" {
  display_name = "nonprod"
  parent       = "organizations/${var.org_id}"
}
resource "google_project" "ns_dev" {
  name       = "Northstar Dev"
  project_id = "ns-dev-${var.suffix}"
  folder_id  = google_folder.nonprod.name
  billing_account = var.billing_account
}
# Org policy sketch (paper OK): constraints/compute.vmExternalIpAccess
```
- IAM: groups on folders; no standing human Owner at org.

#### GCP lab (free-tier boxed)
- If you have org access: create folder + project under it; link billing; set labels. If not: paper Terraform + diagram still required; use existing project and document the *intended* tree.
- **Credits-optional:** none beyond project itself.

#### Gate
- Diagram of org→folder→project for Northstar; no resources created in the org node “because it was convenient.”
- Unseen: all envs in one project with labels only — what boundary did you lose (anchored: IAM/quota/billing)?
- Nearby (pointer only — **Prop Lock**): a future **Shared VPC** host project might live under `shared` vs app projects — **do not** require Shared VPC mechanics until **6.7**; name + defer.

#### PCA: hierarchy as security boundary
- **Considerations:** PCA 1.x design environments; 3.x org policy; blast radius.
- **Decision table:**

| Boundary need | Mechanism | Accept |
|---|---|---|
| Separate prod data | Separate project | Cross-project IAM complexity |
| Same network / DNS shared (later) | Shared VPC host project (**Part 6.7** — unlock first) | Host project becomes critical; **not** an F/0 prop |
| Policy “no public IP” | Org policy constraint | Break-glass exceptions |

- **Scenario prompt:** All envs in one project with labels only.
- **Expected:** “I pick separate projects for prod/nonprod because Y (IAM/quota/billing blast radius), I accept Z (more projects to govern).”

### 0.4 HLD/LLD contract + Donne Martin


#### PCA: 1.1 Business requirements (design)

**Guide themes (matrix):** business use cases and product strategy; functional vs non-functional requirements; BCP; cost optimization; supporting application design; external integration patterns; data movement; design trade-offs; build/buy/modify/deprecate; KPI/ROI/success metrics; security and compliance; observability. Homes: 0.4, Part 8, 10, 11 (F2 CapEx/OpEx literacy).

| Decision | Prefer | Accept instead when |
|---|---|---|
| Managed vs DIY | Cloud Run / managed DB | Constraint forces GCE/appliance or existing Kubernetes estate |
| Build vs buy | Buy Google AI API / Model Garden | Differentiating IP or latency needs custom Vertex |
| Consistency | Strong for money/orders | Eventual for feed/analytics |
| Multi-region | Only if RPO/RTO/KPI demand it | Regional HA if SLO is 99.9% |

**Scenario prompt:** A SaaS product must cut infra admin cost, keep checkout correct under failure, and prove ROI in 90 days. Stakeholders disagree on Spanner vs Cloud SQL.

**Expected answer shape:** “I pick a **regional managed SQL** (Cloud SQL; HA topology details in **Part 2**) + regional Cloud Run because Y (SLO/cost), I accept Z (no multi-region active-active until KPI proves need).” Do not treat **Cloud SQL HA** as an unlocked prop before Part 2 — name + defer.

#### Concept: Donne Martin four-step loop
**What / why.** Constraints → HLD → core LLD → scale/security/cost (Pedagogy §4). Full six-step protocol (NFRs, capacity, Mermaid HLD, LLD, failures, hardening) is Pedagogy §8 — this section installs the habit.
**Failure modes.** Jumping to products before constraints; “scale” slide with no numbers; skipping failure modes.
**Point-at.** For Northstar v0, write four headings and fill one sentence each before any Terraform.

#### Concept: HLD audience and artifacts
**What / why.** **HLD** speaks to stakeholders, PCA case readers, new teammates: context diagram, containers, NFRs, cost/risk, ADRs. Not class diagrams of every struct.
**Failure modes.** HLD that is only a product shopping list; missing “what we accept.”
**Point-at.** One C4 context + one container Mermaid for Client → Run → DB.

#### Concept: LLD audience and artifacts
**What / why.** **LLD** speaks to implementers, reviewers, on-call: sequences, schemas, API contracts, IAM bindings, Terraform shapes, failure/error matrices, idempotency keys.
**Failure modes.** LLD that restates HLD; IAM left as “TBD Owner.”
**Point-at.** Sequence: client → authn → authorize → write order → outbox; IAM: Run SA roles listed.

#### Concept: ADR template
**What / why.** Architecture Decision Record: context, decision, consequences, status (proposed/accepted/superseded). Every irreversible pick gets one; update, don’t ghost-rewrite history.
**Failure modes.** ADRs after the fact as fiction; no consequences section.
**Point-at.** ADR-001 stub: “Cloud Run vs GCE for API” with Y/Z sentence.

#### Concept: NFR table
**What / why.** Latency, availability (nines), RPO/RTO, threat model notes, cost ceiling, compliance/residency — numbers beat adjectives.
**Failure modes.** “Highly available” with no nines; RPO/RTO copied from a blog for a 100-user app.
**Point-at.** Fill a 6-row table for Northstar v0 with at least one explicit accept (e.g. single-region).

#### From scratch / exercise (no production code)
- HLD one-pager for Northstar v0 using Donne Martin’s questions (users, QPS, read/write ratio, data size, retention). This artifact is **reused all course** — update, do not rewrite from scratch each part.
- Write ADR-001 and an NFR table; peer-critique missing Z.

#### HLD / ADR prompt (meta)
- Yes — this section’s deliverable *is* the HLD/ADR craft. Gate on quality of the one-pager, not on deploying it.

#### LLD / IAM / Terraform shape
- LLD checklist template in repo: API paths, schema sketch, IAM roles, Terraform resource names, error codes, idempotency. Empty IAM → fail review.

#### GCP lab (free-tier boxed)
- No billable resources required. Optional: export the Mermaid to the repo README. **Credits-optional:** none.

#### Gate
- One-pager exists; every later ADR can point at it; “I pick X because Y, I accept Z” appears at least once.
- Unseen: case asks multi-region DR for a 100-user student app — answer with NFR-driven regional choice (anchored terms).
- Nearby: turn one HLD container into three LLD bullets (API, IAM, failure).

#### PCA: case-study communication
- **Considerations:** PCA cases reward explicit trade-offs; diagrams beat buzzwords.
- **Decision table:**

| Artifact | When | Accept |
|---|---|---|
| HLD one-pager | Before first deploy | Will be wrong; version it |
| ADR | Every irreversible pick | Overhead vs silent decisions |
| LLD sequence | Before coding money path | Slower start, fewer incidents |

- **Scenario prompt:** Case study asks for DR across regions for a student app with 100 users.
- **Expected:** “I pick single-region + backups because Y (cost/complexity), I accept Z (region outage = downtime) — escalate to multi-region only if NFR demands.”

### 0.5 Cloud IAM (full offering — video outline + PCA 3.1)


#### PCA: 3.1 Security design

**Guide themes (matrix):** IAM; hierarchy; KMS/secrets; SoD; audit/VPC-SC/CAA/org policy/hierarchical FW; IAP/impersonation/Chrome Enterprise/WIF; supply chain; Model Armor/SDP. Homes: 0.3, 0.5, 4, 7, D5, 9b. **Prop Lock:** VPC-SC / hierarchical FW are **named** here for PCA map literacy; concept+lab owners are **Part 6/7** — do not use as create-dialog props in 0.5.

| Control | Prefer | Accept |
|---|---|---|
| Humans to cloud | Groups + least privilege + IAP | Long-lived user keys |
| CI to GCP | WIF | SA keys in GitHub |
| Data | CMEK where required + Secret Manager | Env secrets in images |
| AI | Model Armor + SDP | Unfiltered prompts to prod models |
| Perimeter | VPC-SC for sensitive data (**Part 7** / org perimeter — name now, lab later; **Prop Lock**) | Public APIs with only API keys |

**Scenario prompt:** Pipeline still downloads a JSON SA key; GenAI app logs full prompts with PII.

**Expected answer shape:** “I pick WIF + Secret Manager + Model Armor/SDP because Y, I accept Z (break-glass only with PAM/time-bound).”

**Split rule:** principals below are separate #### Concept anchors. Especially **workforce** vs **workload** federation — near-identical names, different subjects (humans vs machines), pool scope (org vs project), and principal URI shapes. Never one vocab check that treats them as synonyms.

#### Concept: Hierarchy as allow-policy attachment
**What / why.** Allow policies attach at org/folder/project/resource (0.3). Effective access = union of inherited allows minus denies/conditions/org policy — mental model before CEL engines.
**Failure modes.** “I removed project Owner so they’re safe” while folder Editor remains; ignoring deny policies later.
**Point-at.** Binding on folder visible when viewing a child project’s effective IAM (console “view by principals” / Policy Analyzer awareness).

#### Concept: Principal — user
**What / why.** A **Google Account** human identity (Workspace / Cloud Identity / consumer). Identifier: `user:alex@example.com`. Authenticates; can be granted roles.
**Failure modes.** Binding every role to individuals instead of groups; consumer Gmail as standing prod admin.
**Point-at.** Badge with a person’s name on it.

#### Concept: Principal — group
**What / why.** Named collection of Google Accounts (and optionally SAs). Identifier: `group:sre@example.com`. **Cannot authenticate by itself** — members do. Prefer groups for humans.
**Failure modes.** Empty groups with powerful roles; using groups as if they were service accounts for runtime.
**Point-at.** “Everyone on the SRE list” badge rack — add/remove people without rewriting every policy.

#### Concept: Principal — service account
**What / why.** Machine identity **inside** GCP. Identifier: `serviceAccount:app@PROJECT.iam.gserviceaccount.com`. User-managed vs Google-managed service agents; prefer attach/impersonate over keys.
**Failure modes.** One SA for all services; Editor on deploy SA; downloading JSON keys into GitHub.
**Point-at.** Robot badge issued by Google Cloud for an app running in GCP (Cloud Run attached SA).

#### Concept: Principal — domain
**What / why.** Virtual set of all Google Accounts in a Cloud Identity / Workspace **customer** (primary+secondary domains share customer ID). Identifier: `domain:example.com`. Use sparingly.
**Failure modes.** `domain:` on sensitive resources; thinking secondary domain is a different IAM set.
**Point-at.** “Anyone whose badge says `@example.com`” — broader than an explicit group list.

#### Concept: Workforce Identity Federation (humans, external IdP)
**What / why.** Federates **human** identities from an **external IdP** (OIDC/SAML) via org-level **workforce identity pools** — often **without** creating Google Accounts (sync-less). Official contrast: *Workforce federates user identities; Workload federates workload identities.* Principal shape resembles `principal://iam.googleapis.com/locations/global/workforcePools/POOL/subject/...`.
**Failure modes.** Calling it “WIF” when you mean GitHub→GCP workload federation; over-broad `principalSet` on a pool; attribute mapping mistakes; assuming `allAuthenticatedUsers` includes workforce federated identities (**it does not** — use pool principalSets).
**Point-at.** Contractor on Okta SSO gets a **human visitor badge** to use Console/CLI — no Google Account provisioning first. Console IAM member picker shows federated workforce principal when configured.
**Vocab check (this anchor only):** workforce = humans/external IdP/org pools — do **not** include GitHub Actions tokens in the same check until the workload anchor is confirmed.

#### Concept: Workload Identity Federation (machines/CI, external IdP)
**What / why.** Federates **machine/workload** identities outside GCP (GitHub Actions, AWS, Azure, on-prem OIDC/SAML/X.509, …) via project-scoped **workload identity pools**. Exchanges external tokens at STS for short-lived Google tokens; prefer **direct resource access** or SA **impersonation** (`roles/iam.workloadIdentityUser`) over long-lived SA keys. Principal shape resembles `principal://iam.googleapis.com/projects/NUM/locations/global/workloadIdentityPools/POOL/subject/...`. (Not the same feature as “Workload Identity” for GKE alone — mention, don’t conflate.)
**Failure modes.** SA keys in CI “temporarily”; missing attribute conditions on multi-tenant IdPs (GitHub) → wrong-repo access; naming it “workforce” because both start with “work.”
**Point-at.** Robot visiting from GitHub Actions: visitor badge at the front desk (STS) — **no photocopied master key** (JSON key file).
**Vocab check (after this anchor):** map GitHub→deploy to workload federation; map Okta employee→console to workforce — only when both anchors confirmed.

#### Concept: Roles — basic, predefined, custom
**What / why.** Basic Owner/Editor/Viewer — avoid for standing access. Prefer predefined; custom with min permissions when needed.
**Failure modes.** Standing Editor “temporarily”; custom role that is secretly `*`.
**Point-at.** Deploy SA: `run.developer` + `artifactregistry.writer`, not Editor.

#### Concept: Allow policies, conditions, deny, effective policy
**What / why.** Bindings list principals + roles; CEL conditions (time, attributes); deny policies harden; always ask “who can actually do X on R?”
**Failure modes.** Conditions that never match; deny without audit story.
**Point-at.** Time-conditioned break-glass binding that expires tomorrow.

#### Concept: Service account keys last resort
**What / why.** Attach SA to Cloud Run/GCE; impersonate; WIF for CI. Org policy `iam.disableServiceAccountKeyCreation`. Disable App Engine / Compute **default** SAs when you can.
**Failure modes.** Keys in images/logs; defaults with Editor left enabled.
**Point-at.** Lab evidence: SA with **zero** user-managed keys.

#### Concept: Cloud Identity vs Workspace vs Identity Platform
**What / why.** Three products: **Cloud Identity / Workspace** = employee directory; **IAM** = authorization on GCP resources; **Identity Platform** = *your customers* (deepen Part 4.1). Do not swap them on case studies.
**Failure modes.** Putting customers in Cloud Identity; using Firebase Auth slogans for workforce SSO.
**Point-at.** Table from Part 4.1 — employees vs customers vs GCP resource access.

#### Concept: Groups, SoD, break-glass, audit
**What / why.** Groups for humans; SAs for machines; SoD across org/billing/deploy; break-glass monitored; Cloud Audit Logs for who did what.
**Failure modes.** Shared super-admin daily driver; no audit sinks.
**Point-at.** One break-glass user documented; daily deploy via group-scoped project role.

#### From scratch / code
- **Python then Go:** parse an IAM policy JSON fixture; evaluate whether principal P can do permission X on resource R (simplified binding match — teach the shape, not a full CEL engine). Table tests: user via group; SA direct; missing binding; wrong role.
- Separate classification drill (answer key): workforce vs workload for five scenarios (Okta human, GitHub Actions, Cloud Run SA, AWS EC2→GCS, domain grant).

#### HLD / ADR prompt
- ADR: “CI uses Workload Identity Federation; contractors use Workforce Federation or Cloud Identity groups.” Consequences: no JSON keys in GitHub; attribute conditions required.

#### LLD / IAM / Terraform shape
```hcl
# Workload Identity Federation (CI) — illustrative
resource "google_iam_workload_identity_pool" "ci" {
  workload_identity_pool_id = "github-pool"
}
# Workforce pools are org-level — often console/org-admin; paper the principal URI
# Custom role
resource "google_project_iam_custom_role" "deployer" {
  role_id = "nsDeployer"
  title   = "Northstar Deployer"
  permissions = ["run.operations.get", "run.services.update", "artifactregistry.repositories.uploadArtifacts"]
}
```
- Bind humans via `group:`; CI via workload pool principalSet; never commit key JSON.

#### Lab (free-tier boxed)
- Custom role with three permissions; condition on time; SA with **no** keys; group-based binding for humans.
- **Credits-optional:** configure a workload identity pool for GitHub (or paper + `gcloud iam workload-identity-pools describe` on a training project). Workforce pool usually needs org admin — paper URI + decision table if blocked.

#### Gate
- No JSON keys in the repo; defaults disabled or documented exception; custom role evidence in Terraform or console screenshot in notes.
- Unseen: “Okta contractors without Google Accounts” vs “GitHub Actions deploy” — name workforce vs workload (only after both anchors).
- Nearby: replace Editor on deploy SA with custom role permissions list.

#### PCA: 3.1 identity and access
- **Considerations:** least privilege, SoD, federation over keys, deny policies, audit.
- **Decision table:**

| Actor | Authn | Authz |
|---|---|---|
| Human engineer | Cloud Identity + group | Predefined/custom on folder/project |
| Contractor (no Google Account) | Workforce Identity Federation | Pool principal / mapped groups |
| CI pipeline | Workload Identity Federation (GitHub) | Deploy SA narrowly scoped / direct |
| Cloud Run service | Attached SA | `secretAccessor` + invoker as needed — not Editor |

- **Scenario prompt:** Deploy SA has `roles/editor` “temporarily.”
- **Expected:** “I pick custom role with run.developer + ar.writer because Y, I accept Z (must update role when new product APIs needed).”

## Part 1 — Compute platforms, then deploy frontend + backend first

**Goal:** Understand the three first-party compute offerings you will actually be asked about as an architect (Cloud Run, Compute Engine, App Engine), then **ship** Northstar v0 on Cloud Run. GKE comes later.

### 1.0 Compute landscape (architect, not catalog)

You choose compute the way an architect chooses blast radius and ops tax — not by reading a product catalog cover-to-cover. Northstar v0 defaults to Cloud Run; you still **feel** GCE and App Engine so PCA trade-offs are lived, not memorized.

#### Concepts
- **Abstraction ladder (most managed → most control):** Cloud Functions / Cloud Run functions → Cloud Run (services/jobs/worker pools) → App Engine standard → App Engine flexible → GKE Autopilot → GKE Standard → Compute Engine. Climb only when a force requires it.
- **Cloud Run** when Google manages infra and the workload is a **container** (HTTP service, Job, or Worker Pool). Request-driven, scale-to-zero by default, concurrency knob, revisions + traffic tags. Official default for new container HTTP apps.
- **App Engine** when you want PaaS with services/versions/traffic split and are in an existing GAE estate — or for the PCA. Standard = sandboxed runtimes + free F1 hours; Flexible = containers on VMs you do not fully manage (rarely the right *new* choice vs Cloud Run).
- **Compute Engine** when you must manage the OS, custom kernels, third-party appliances, GPU/TPU attachments that are not on a managed path, or lift-and-shift VMs. Always Free e2-micro exists for literacy — not for production HA.
- **GKE** when you need the Kubernetes API (custom networking/CNI, sidecars as first-class, stateful operators, GPU pools with node lifecycle). Taught later; **do not default here** for a single JSON API.
- **Cloud Run functions** = specialized **source deploy** of a Cloud Run **service** (branding vs gen2 Functions). Gen2 Functions *are* Cloud Run under the hood (Eventarc). Gen1 is brownfield literacy only.
- **Ops burden vs control:** every step down the ladder buys a knob (SSH, CNI, custom kernel) and sells an on-call shift. PCA case studies punish “GKE for a cron” and “Spot on checkout.”

#### Decision exercise (from scratch — no GCP yet)
Write a one-page ADR draft for three fake workloads before you open Console:
1. Public JSON checkout API, p95 < 300 ms, spiky traffic, team of 3.
2. Vendor .deb + out-of-tree kernel module for a payment HSM appliance.
3. Nightly 4-hour video transcode batch that can die and restart.

For each: pick compute, list **three forces**, list **one accept** (cost/ops/latency). Peer-review: if someone picks GKE for (1) without a K8s-forced requirement, reject the ADR.

#### HLD
Draw Northstar v0: browser → (Firebase Hosting / later HTTPS LB) → Cloud Run API → Cloud SQL / Firestore. Annotate where GCE or GAE would replace the API box and what new boxes appear (MIG, health checks, `app.yaml`).

#### LLD
One table you will reuse in 1.10:

| Force | Prefer | Reject unless forced |
|---|---|---|
| Request-driven HTTP, least ops | Cloud Run service | GKE for resume points |
| Event glue (object finalize) | Functions gen2 / Eventarc | 40 sync Functions as a monolith |
| Brownfield GAE + cron.yaml | Stay / strangler | Big-bang rewrite Friday |
| Vendor appliance / custom kernel | GCE (+ sole-tenant/confidential if required) | Cloud Run |
| Mesh, custom CNI, operators | GKE | “We’ll learn K8s on checkout” |

#### ADR-001
- Cloud Run for Northstar v0 default. You will still **implement the same API** on GCE and App Engine so trade-offs are felt, not memorized.

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ Enable: Cloud Run, Artifact Registry, Cloud Build APIs.     │
│ Deploy the 1.2 health API once to Cloud Run (scale-to-zero).│
│ Do NOT create a GKE cluster or a second e2-micro yet.       │
│ Credits-optional later: same image on GAE standard + GCE. │
│ Tear-down: delete Cloud Run service if you set min>0.       │
└─────────────────────────────────────────────────────────────┘
```
Confirm in docs: [Choose a compute option](https://cloud.google.com/blog/topics/developers-practitioners/where-should-i-run-my-stuff-choosing-google-cloud-compute-option) mental model + current Cloud Run / App Engine product pages.

#### Gate
- Can recite the ladder and justify Cloud Run for Northstar without saying “serverless is magic.”
- ADR-001 written; three-workload exercise graded; no GKE cluster created “to look productive.”

#### PCA: choose compute
- **Considerations:** official “choose compute options” tree; ops burden vs control; PCA case studies punish “GKE for a cron.”
- **Decision table:**

| Force | Pick | Accept |
|---|---|---|
| Request-driven HTTP, least ops | Cloud Run | Less OS/SSH |
| Brownfield GAE + traffic split habits | App Engine | Older sandbox model |
| Vendor appliance / custom kernel | GCE | You patch |
| Mesh, custom CNI, operators | GKE | Cluster tax |

- **Scenario prompt:** Team wants GKE “for resume-driven development” for a single JSON API.
- **Expected:** “I pick Cloud Run because Y (no cluster ops), I accept Z (revisit GKE if sidecars/operators appear).”
### 1.2 Container contract (LLD that production depends on)

Docker/OCI from Part D1 is assumed: multi-stage image, nonroot, digest, SIGTERM. This section is the **Cloud Run runtime contract**. Full hardened HTTP middleware, 4xx table, SSRF — **Part 4.2** (one HTTP lab; G10 here is contract only; G11–G12 home under 4.2).

#### Concepts (Cloud Run contract)
- Listen on `PORT` (env). Stateless. Ephemeral local disk — not a database.
- **SIGTERM** drain: stop taking work; finish in-flight; exit. Cloud Run sends SIGTERM before SIGKILL.
- Concurrency (default 80, max 1000). CPU allocation: request-based vs instance-based billing.
- Min instances vs scale-to-zero (cold start vs cost).
- Revisions, traffic split, tags (canary) — first taste; Part D / Cloud Deploy industrializes this.
- Identity: runtime SA (1.5). Secrets via Secret Manager, not baked into image.

#### From scratch / LLD
- `/healthz` (liveness-ish), `/readyz` (dependency readiness), structured JSON logs, request ID middleware.
- Explicit server timeouts (language-appropriate). Body limit stub.
- Dockerfile: multi-stage, nonroot, digest base — reviewed against D1.

#### Labs
- Containerize FastAPI health + echo; deploy Cloud Run service; hit `*.run.app`; read logs in Cloud Logging.
- **Python:** implement the contract above.
- **Go after submit (G10 — contract slice only):** `net/http` + `errgroup` + SIGTERM; explicit `http.Server` timeouts; pointer/struct/interface handler wiring (**G3**). Paste Go G10 lesson under this heading; **pointer** in text to #### Go G11 / G12 under **4.2** — do not duplicate the hardened lab.

#### Gate
- Image nonroot; listens on `PORT`; SIGTERM graceful; traffic URL works; cost model notes min-instances.

#### PCA: serverless containers
- **Considerations:** scale-to-zero, concurrency, revisions; when min-instances; when not Cloud Run (long WS, custom kernel).
- **Decision table:**

| Need | Knob | Accept |
|---|---|---|
| Cheapest idle | min-instances=0 | Cold start |
| Stable p95 | min-instances≥1 | Pay for idle CPU/RAM |
| CPU during background | instance-based CPU | Higher bill |

- **Scenario prompt:** Checkout API sees 2s cold starts at 09:00.
- **Expected:** “I pick min-instances=1 in prod because Y (NFR latency), I accept Z (idle cost) — keep 0 in nonprod.”

#### Go G10 — net/http server surface (container contract slice)
SYNTAX UNLOCK: `http.Handler` / `http.HandlerFunc`; `http.NewServeMux` (Go 1.22+ method patterns); `srv := &http.Server{Addr, Handler, ReadHeaderTimeout, ReadTimeout, WriteTimeout, IdleTimeout}`. Listen on `os.Getenv("PORT")`. Contrast Python: ASGI lifespan + uvicorn timeouts.
Concept: **At 1.2 only:** `/healthz`, `/readyz`, structured JSON logs, request ID, SIGTERM graceful shutdown via `errgroup` + `srv.Shutdown(ctx)`, body/header limits stubs. Do **not** duplicate the full 4xx/SSRF/middleware order lab here — that is G11–G12 under **4.2**. Pointers/structs/interfaces for handler types reuse G3.
Python twin first: FastAPI health/ready + graceful shutdown + JSON logs.
Go artifact: package `httpserver` (shared with 4.2); tests at 1.2: `TestHealthz`, `TestReadyzFailsWhenNotReady`, `TestShutdownDrains`, `TestPortFromEnv`; gate: image listens on `PORT`, nonroot, SIGTERM exits 0; pointer from 1.2 text to #### Go G11 / G12 under 4.2.

---
### 1.3 Frontend hosting (industry options, free-tier path)

The storefront is not “whatever Vite dumps into Cloud Run.” Hosting choices set cache headers, TLS, and blast radius for the browser origin. Full CDN mechanics live in **1.4**; here you pick *where HTML/JS land*.

#### Concepts
- **Static SPA** (React/Vue/Svelte build): objects + HTTPS edge. On GCP: Cloud Storage website config **or** Firebase Hosting (simpler custom domain + CDN on free-tier path).
- **SSR** (Next/Nuxt): needs a server process. Firebase **App Hosting** = Cloud Build + Cloud Run + CDN managed path. If App Hosting exceeds credits, fall back to static export on Firebase Hosting + Cloud Run API.
- **Server-rendered from your API:** Cloud Run (or App Engine) serves HTML. Fine for admin UIs; rarely the best SPA path.
- **CORS:** browser origin (Hosting) ≠ API origin (`*.run.app`). Prefer same-site via custom domain later; until then explicit CORS allowlist + credentials rules from Part 4.4.
- **Security headers:** CSP, HSTS, `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy`. Set at Hosting/`firebase.json` headers or at the reverse proxy — not only in the JS bundle.
- **Cache headers (preview of 1.4):** static assets → versioned URLs + long `max-age`; HTML shell → short TTL or `no-cache` with revalidation; authenticated JSON → `private, no-store`.

#### Decision exercise
Fill before building:

| Frontend type | GCP path | Free-tier lab | When it loses |
|---|---|---|---|
| Static SPA | GCS website + (optional) LB/CDN **or** Firebase Hosting | Firebase Hosting or GCS public-read | Need SSR |
| SSR (Next/Nuxt) | Firebase App Hosting | Static export + Hosting if credits tight | Heavy SSR without budget |
| HTML from API | Cloud Run serving templates | Cloud Run | Separating FE/BE teams |

Write three sentences: why Northstar storefront prefers Hosting over `StaticFiles` on the API service.

#### HLD
Browser → Firebase Hosting (TLS + edge) → Cloud Run API (`Authorization` / cookies per Part 4). Draw CORS preflight. Mark where a future global HTTPS LB + serverless NEG replaces the `run.app` URL (**credits-optional**; full LB map in **1.12**).

#### LLD
- `firebase.json` headers block (CSP draft, HSTS).
- API responses: catalog public vs cart private `Cache-Control`.
- Never put secrets in the SPA bundle; Identity Platform / session cookies only (Part 4).

#### From scratch
- Local: static `index.html` + `fetch` to FastAPI with CORS middleware; tests for allowed/denied Origin.
- **Python:** tiny Jinja/static generator *or* FastAPI `StaticFiles` as the “wrong default” path — document why Hosting wins for SPA.
- **Go after Python:** `embed` + `http.FileServer` alternative path; same CORS tests (G10 surface already under 1.2).

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ Firebase Hosting (Spark/Blaze per your account) for SPA.    │
│ Cloud Run API remains the backend.                          │
│ Prefer Hosting over making the GCS bucket world-readable    │
│ unless you intentionally practice GCS website + IAM.        │
│ Credits-optional: custom domain on Hosting; do NOT reserve  │
│ a global static IP yet (that is 1.12 / 6.3 billing trap).   │
└─────────────────────────────────────────────────────────────┘
```

#### Gate
- Storefront URL loads over HTTPS; API call works with documented CORS; security headers present on HTML; ADR blurb explains Hosting vs Cloud Run `StaticFiles`.
### 1.4 Edge: TLS, DNS, LB, Armor, CDN (concept + from scratch + GCP)


**From scratch (required, local, before any GCP edge lab):**
- HTTP/1.1 origin: stdlib TCP server that speaks a minimal HTTP subset.
- L7 reverse proxy: accept, parse Host + path, pick a backend (round-robin), copy bytes, health-check `/healthz`.
- Cache middleware on the proxy: cache key = `(method, host, path, Accept, Authorization? no — never cache authenticated)`; honor `Cache-Control`, `ETag`, `If-None-Match`; TTL; size cap LRU.
- CORS + security-header middleware you wrote (Pedagogy §6).
- TLS: terminate with stdlib (`ssl` / `tls`) and a **local mkcert**. Draw the handshake. Do not write crypto.

**GCP — IPs at the edge (full treatment in 6.3):**
- Global external IP on a forwarding rule is how a global HTTPS LB is addressed. Ephemeral vs reserved static. Idle static IPs **bill** — release them.
- Cloud Run `run.app` hides this; you still must know the LB+IP model for PCA and production custom domains.

**GCP — Cloud CDN (full):**
- Cloud CDN is not a standalone box. It is a cache on the **global external Application Load Balancer** (or classic). No LB ⇒ no Cloud CDN.
- Browsers often reach GFE over **HTTP/3 (QUIC)**; your origin is still HTTP/1.1 or HTTP/2 (Part 6.1). You do not run a QUIC server on Cloud Run.
- Request path: user → GFE/PoP → cache hit return; miss → origin (GCS / MIG / serverless NEG / internet NEG).
- **Cache modes:** `CACHE_ALL_STATIC` (default; by Content-Type, still respects `private`/`no-store`), `USE_ORIGIN_HEADERS` (you own Cache-Control), `FORCE_CACHE_ALL` (**never** on authenticated APIs or user HTML).
- Cache keys: protocol, host, path, query string include/exclude, named headers. Wrong key = personalization leak or 0% hit ratio.
- TTL: client TTL vs CDN TTL vs max-age vs s-maxage vs stale-while-revalidate vs stale-if-error. Negative caching.
- Signed cookies / signed URLs for private content (match GCS V4 signed URLs — you already write those in Part 2).
- Invalidation: path, path prefix, tags. Invalidation is eventually consistent and **costs**. Prefer short TTL or versioned URLs (`/static/app.abc123.js`).
- Push vs pull (Donne Martin): Cloud CDN is **pull**. GCS + versioned objects is the production “push-like” pattern.
- Firebase Hosting / App Hosting CDN: the free-tier edge. Custom domain + SSL without a forwarding-rule SKU.
- Hit ratio, cache fill, uncacheable (Set-Cookie, Authorization, POST).
- **Billing:** cache lookup + cache egress vs origin egress. CDN exists to cut origin and LB processing.

**Labs:**
- Required: origin sets correct `Cache-Control`/`ETag`; your toy CDN caches; tests prove 304 and hit/miss.
- Required free-tier: Firebase Hosting for static; Cloud Run API sends `Cache-Control: private, no-store` on authenticated JSON and `public, max-age=60, s-maxage=300` on catalog that may be public.
- Credits-optional: global HTTPS LB + serverless NEG + Cloud CDN `USE_ORIGIN_HEADERS` + Armor. Destroy forwarding rule and **release the static IP**.

**Python / Go:** cache middleware + header policy tests. Never implement TLS ciphers.

### 1.5 Service identity (minimum)

Workload identity is not “the user’s Google account on the laptop.” Every Cloud Run service, Function, and GCE instance that talks to GCP APIs needs a **runtime service account** with least privilege. Keys on disk are a failure mode; WIF (1.6 / Part 4.8) is how CI authenticates.

#### Concepts
- **Runtime SA per service** (or per trust boundary): `ns-api@PROJECT.iam.gserviceaccount.com`, not the default Compute Engine SA for everything.
- **No user credentials in prod.** No `gcloud auth application-default` baked into images. No downloaded JSON keys in Secret Manager “because it’s easier” for runtime — prefer attached SA + ADC.
- **Secret Manager** for API keys (Stripe later), DB passwords, webhook secrets. Env vars for non-secret config (`LOG_LEVEL`, `PROJECT_ID`).
- **IAM bindings are the ACL:** grant `roles/secretmanager.secretAccessor` on *one secret* (or a naming convention), not `roles/editor`. Deny-by-default org policies later (Part 7).
- **Impersonation:** break-glass humans impersonate SAs; services do not share one god SA. Cloud Run “Runtime service account” setting is the attachment point.
- **Metadata server:** GCE default SA + broad scopes is the classic SSRF prize (`169.254.169.254`). Prefer no public IP + narrow SA; Cloud Run’s model is safer by default (Part 4.2 / 7.4).

#### Decision exercise
For Northstar API, list every secret and GCP API call. Produce a table:

| Action | Role / resource | Who (SA) |
|---|---|---|
| Read `stripe-webhook` secret | `secretAccessor` on that secret | `ns-api` |
| Write Firestore orders | `datastore.user` or custom | `ns-api` |
| Deploy revisions | `run.developer` + AR reader | CI deploy SA (not runtime) |

Cross out any row that uses `roles/owner` or a user account.

#### HLD
Box: Cloud Run revision → runtime SA → Secret Manager / Firestore / Cloud SQL Auth Proxy. Separate box: GitHub Actions → WIF → deploy SA (cannot read Stripe secret if not needed).

#### LLD
- Startup: fetch secret once (or on rotate signal); never log value; never put in response.
- Rotate-friendly: code reads latest version by name; old versions linger until cutover.
- Local: fake secret provider interface; ADC only in cloud.

#### From scratch
- **Python:** abstract `SecretProvider` protocol; env-file provider for local; Secret Manager provider for cloud; unit tests prove logs redaction.
- **Go after:** same interface in a `secrets` package; table tests for missing secret / permission denied mapping to 503 (not 500 with stack).

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ Create SA `ns-api`. Bind secretAccessor on ONE test secret. │
│ Deploy Cloud Run with --service-account=ns-api@.            │
│ Prove default compute SA is NOT used (describe revision).   │
│ Deny roles/editor on ns-api. No JSON key download.          │
│ Secret Manager Always Free envelope: stay inside free ops.  │
└─────────────────────────────────────────────────────────────┘
```

#### Gate
- Dedicated SA on the revision; secret read works; editor not granted; no key file in repo or Cloud Shell home left behind; Python tests green before Go twin.
### 1.6 First pipeline (minimum to ship) — full CI/CD is Part D

Stop deploying from a laptop as the happy path. This section is the **minimum** CI: test → build image → push digest → Cloud Run revision → traffic move. Industrial CD (Cloud Deploy, GitOps, Binary Authorization) is Part D.

#### Concepts
- **Build once, promote by digest.** Tags like `:latest` are for humans; deploys pin `IMAGE@sha256:…`.
- **Cloud Build** *or* **GitHub Actions + Workload Identity Federation** — both acceptable; WIF is mandatory for GitHub→GCP (no JSON key).
- **Buildpacks vs Dockerfile:** Buildpacks are fine for demos; the LLD you own is the Dockerfile from D1 / 1.2 (multi-stage, nonroot).
- **Traffic tags:** deploy with `--no-traffic` + tag `canary`; shift 10% → 100%. This is progressive delivery lite (Part D4 deepens).
- **Fail closed:** unit tests fail ⇒ no image push. `govulncheck` / `pip-audit` fail on CRITICAL ⇒ no promote.
- After this lab, Part D replaces ad-hoc `gcloud run deploy` with Cloud Deploy, GitOps, and supply-chain gates.

#### From scratch / decision exercise
Sketch the pipeline on paper with trust boundaries:
1. Who can push to `main`?
2. Which SA deploys to Cloud Run?
3. Which SA is the *runtime* identity (1.5) — must differ from deploy SA.
4. Where does the digests list live (Artifact Registry)?

Reject any design with a standing SA key in GitHub Secrets.

#### HLD
GitHub → (OIDC) → WIF pool/provider → deploy SA → Artifact Registry + Cloud Run Admin. Runtime SA separate. Logging: Cloud Build / Actions logs retained.

#### LLD
- `cloudbuild.yaml` or Actions workflow: `pytest`/`go test` → docker build → push → `gcloud run deploy --image ...@sha256 --no-traffic` → traffic update.
- Branch protection: required check = tests.
- Dockerfile reviewed against D1 checklist (G16).

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ Artifact Registry repo + Cloud Build OR Actions+WIF.        │
│ push → test → build → Cloud Run revision → 10% tag → 100%.  │
│ No JSON key in GitHub secrets.                              │
│ Credits-optional: second region revision (diagram OK).      │
│ Clean up unused images if storage creeps past free tier.    │
└─────────────────────────────────────────────────────────────┘
```

#### Lab
- push → test → build → Cloud Run revision → 10% traffic tag → 100%.
- **Python / Go:** tests must pass in the build. Multi-stage image, nonroot, `govulncheck` on the Go module (**G16 / G18** lesson text under this heading + D1).

#### Gate
- No JSON key in GitHub secrets for GCP; WIF wired; failing test fails the build.

#### PCA: CI without long-lived keys
- **Considerations:** supply chain / IAM; PCA hates standing keys.
- **Decision table:**

| Pattern | Use | Accept |
|---|---|---|
| WIF + deploy SA | Production | Setup cost |
| User `gcloud run deploy` | Break-glass lab only | Not audited CD |
| JSON key in Actions | Forbidden here | Key leak class |

- **Scenario prompt:** “Just put the SA key in GitHub secrets to unblock Friday.”
- **Expected:** “I pick WIF because Y (no key material), I accept Z (half-day setup) — Friday slip beats credential incident.”

#### Go G16 — Docker release surface for Go binaries
SYNTAX UNLOCK: `CGO_ENABLED=0 go build -trimpath -ldflags="-s -w" -o /out/app`; distroless nonroot final stage. Contrast Python: multi-stage without pip in runtime.
Concept: Multi-stage Dockerfile is LLD (D1). Digest push to Artifact Registry. Nonroot USER. This unlock is **build/release**, not CI YAML (G18).
Python twin first: multi-stage FastAPI image; then Go distroless.
Go artifact: package path builds to `cmd/api`; tests: image smoke (`/healthz`) in CI; gate: `USER nonroot` (or numeric), no shell in final, digest published; Dockerfile reviewed against D1 checklist.

---

#### Go G18 — govulncheck, CI test gate, provenance handoff
SYNTAX UNLOCK: `govulncheck ./...` fails the build on known vulns in the module graph. Contrast Python: `pip-audit`.
Concept: `go test ./...` must pass in Cloud Build / Actions before image push. SCA gate is not optional color. Provenance/SBOM handoff is Part D5 — here you only ensure the Go module is scannable and CI-green.
Python twin first: pytest + pip-audit in CI; then Go.
Go artifact: CI step documents; tests: module passes `govulncheck` (or justified exception file); gate: failing test fails the pipeline; CRITICAL vuln fails; image promote by digest only.

---
### 1.7 Observability from day one

If you cannot see a request, you cannot operate it. Part 10 industrializes SLOs and dashboards; this section installs the **minimum** signals on the Cloud Run API so later parts have something to measure.

#### Concepts
- **Structured logs (JSON)** to stdout: severity, message, `trace`/`spanId` fields Cloud Logging understands, request id, latency_ms. No printf archaeology.
- **Trace context propagation:** inbound `traceparent` / `X-Cloud-Trace-Context` → outbound clients. One request → one correlated story in Trace + Logging.
- **Error Reporting:** unhandled exceptions become error groups; fix the top group before adding features.
- **Uptime check** against the Cloud Run URL (or Hosting). Free-tier: sketch + cost note if you skip live checks; one probe is enough for literacy.
- **SLIs early:** availability (non-5xx ratio), latency p95 for `/api/*` — even if SLO paperwork waits for Part 10.
- **Cardinality discipline:** never label metrics by `user_id` / email / order_id. Bound label sets (route template, status class).

#### From scratch
- Local middleware: timing + request id + JSON log line; test that secrets never appear.
- Fake exporter: spans in memory; assert child span on outbound HTTP.
- **Python:** OpenTelemetry SDK or Cloud Trace; request timing middleware.
- **Go (G17):** same spans; `pprof` on localhost-only when chasing CPU — never public on Run.

#### HLD
Client → Cloud Run → Logging + Trace (+ Error Reporting). Uptime check → alerting policy (email/Pub/Sub). On-call reads RED (Rate, Errors, Duration) before guessing.

#### LLD
- Log schema version field; `httpRequest` mapping where platform supports it.
- Sampling: always sample errors; fractionally sample OK at scale.
- Health endpoints excluded from error burn or sampled separately.

#### Code
- **Python:** request timing; OpenTelemetry or Cloud Trace spans (Firestore later).
- **Go (G17):** same spans; `pprof` on localhost-only when chasing CPU — never public on Run.

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ Cloud Logging + Cloud Trace on the existing Cloud Run svc.  │
│ Generate one request; find log↔trace correlation in Console.│
│ Uptime check: create OR document cost and skip with sketch. │
│ Do not enable every Ops Agent on a fleet yet (GCE is 1.8).  │
└─────────────────────────────────────────────────────────────┘
```

#### Gate
- One request shows trace/log correlation; uptime check exists or is sketched with cost note; cardinality note in ADR.

#### PCA: operability
- **Considerations:** reliability domain; you cannot improve what you do not measure.
- **Decision table:**

| Signal | Where | Accept |
|---|---|---|
| RED logs | Cloud Logging | Cost beyond free GiB |
| Traces | Cloud Trace | Sampling required at scale |
| pprof | Local only | Not a prod endpoint |

- **Scenario prompt:** On-call only has “it feels slow.”
- **Expected:** “I pick p95 latency SLI + trace sample because Y, I accept Z (instrumentation work before feature work).”

#### Go G17 — OpenTelemetry + pprof
SYNTAX UNLOCK: OTel Go SDK spans around handlers; `net/http/pprof` registered on **localhost-only** debug mux in dev. Contrast Python: OTel SDK + py-spy/cProfile.
Concept: Structured logs with trace id; spans for outbound calls; pprof only when chasing CPU locally — never expose pprof publicly on Cloud Run.
Python twin first: request timing + trace context propagation; then Go.
Go artifact: package `obs`; tests: `TestTraceIDInLogs`, `TestSpanAroundHandler`, `TestPprofNotOnPublicMux`; gate: one traced request visible in local exporter or Cloud Trace on deployed revision; pprof gated behind build tag or localhost.

---
### 1.8 Compute Engine (full offering)

#### PCA: 2.3 Compute systems (provision)

**Guide themes (matrix):** provisioning; spot vs standard; GCE/GKE/serverless/GCVE networking; orchestration/patch; containers; serverless. Homes: 1, 9, 8b.

| Workload | Prefer | Accept |
|---|---|---|
| Stateless HTTP | Cloud Run | GKE Autopilot if K8s API needed |
| Batch/render | Spot + Batch/Jobs | Standard only if preemption costly |
| VMware lift | GCVE when required | Refactor to Run/GKE when ROI wins |
| Patch | OS Config / Autopilot | SSH snowflake |

**Scenario prompt:** Rendering farm and a checkout API share one MIG of standard VMs “for simplicity.”

**Expected answer shape:** “I pick Spot Jobs for render + Cloud Run for checkout because Y, I accept Z (separate blast radii; no Spot on checkout).”

**T-ARCH / T-OS gate on this lab:** predict then observe — `lscpu`/cache sizes; page fault via large mmap; context switch under load; systemd unit cgroup CPU; deadlock four conditions on a mutex toy. Incomplete if only “VM exists.”


Concept first: you own the guest OS. Google owns the hypervisor, host, and physical network.

#### GCP offerings in this family
- **VMs** — machine families (E2, N2, N2D, C3, C4, Tau T2A/T2D, GPU/TPU attachments, Axion/Arm).
- **Persistent Disk / Hyperdisk** — pd-standard, pd-balanced, pd-ssd, Hyperdisk; snapshots; images.
- **Instance templates + MIGs** — autoscaler, autohealing, rolling updates, stateful MIGs.
- **OS Login, OS Config / VM Manager, OS patch** — sysadmin surface.
- **Spot / preemptible**, sole-tenant, confidential VMs, Shielded VMs.
- **IAP TCP forwarding** — SSH without a public IP.
- **Ops Agent** — logs and metrics.
- Always Free: **1× e2-micro** in us-central1 / us-west1 / us-east1 + 30 GB standard PD.

#### Curriculum
- Virtualization: hypervisor, guest OS, why GCE is IaaS.
- Machine type selection, families, custom types, shared-core (e2-micro), GPU/TPU, Spot vs standard (PCA 2.3 volatility).
- Create/manage instances; live migrate vs terminate; availability policy.
- Connecting: SSH keys vs OS Login vs IAP TCP (**prefer no public IP**).
- Metadata server + startup scripts; project vs instance metadata; **metadata SSRF** is a real attack (ties to 4.2 outbound policy).
- Billing SKUs: vCPU, memory, PD, GPU, idle public IP, egress, CUD, Spot.
- Storage: PD types, Hyperdisk, Local SSD (ephemeral), boot vs additional, resize, zonal vs regional PD.
- Snapshots, schedules, images, image families, custom images.
- Startup scripts vs templates vs OS Config / VM Manager / patch.
- VPC NIC; external IP vs none + Cloud NAT + IAP SSH.
- Unmanaged vs managed instance groups; health checks; backend service for HTTP(S) LB.
- Patching, Packer-style golden images vs cattle.
- **Deployment Manager** legacy — read a DM template, rewrite in **Terraform**. Do not start new work in DM.

#### T-ARCH (required with this GCE lab)
ISA, pipeline hazards, cache hierarchy, virtual memory, coherence — taught against the **e2-micro lab**, not a cycle-accurate simulator. Map: vCPU → time slices; PD latency → memory hierarchy miss tax; live migrate → process state move analogy. One page notes: “what the guest believes vs what the hypervisor does.”

#### T-OS (complete with the systemd unit)
Process vs thread, scheduling, user/kernel, VM, filesystems, locks/deadlock, signals. Namespaces/cgroups = container contract (1.2 / D1). Lab: Northstar API under **systemd** with restart policy; prove SIGTERM handling matches Cloud Run mental model.

#### Labs
- **Always Free:** e2-micro, no public IP, OS Login + IAP tunnel, Ops Agent, nginx or Northstar API as systemd unit, snapshot, custom image. Tear down if you attach a public IP or extra disks that bill.
- **HLD:** lift-and-shift 3-tier (MIG web + MIG app + Cloud SQL). When this loses to Cloud Run.
- **Python / Go:** Compute Engine API list/start/stop/label.

#### PCA: IaaS vs managed
- **Considerations:** PCA 2.x provision compute; volatility (Spot); bastion-less admin via IAP.
- **Decision table:**

| Need | Pick | Accept |
|---|---|---|
| SSH + agent | GCE + IAP | You patch |
| HTTP API least ops | Cloud Run | No SSH |
| Batch interruptible | Spot | Preemption |

- **Scenario prompt:** Vendor requires their .deb and a kernel module.
- **Expected:** “I pick GCE (maybe sole-tenant/confidential as required) because Y, I accept Z (patching + MIG discipline) — not Cloud Run.”
### 1.9 App Engine (full offering)

Concept: PaaS. You give it code; Google gives versions, traffic split, cron, and an `appspot.com` HTTPS URL. Google’s current guidance for *new* container HTTP apps is **Cloud Run**; App Engine remains on the PCA and in brownfield estates. You lab it so the exam and migrations are not abstract.

#### Concepts
- **Standard** — sandboxed runtimes (Python, Go, Java, Node, PHP, Ruby), scale-to-zero, **28 F1 hours/day** Always Free envelope (confirm current Always Free card in lab notes).
- **Flexible** — containers on GCE VMs you don’t fully manage; no scale-to-zero; rarely the right **new** choice vs Cloud Run (awkward middle: less control than GCE, less serverless than Run).
- **Services / versions / traffic splitting** — deploy `v2` beside `v1`, shift 1%→50%→100%, instant rollback by shifting traffic back.
- **Cron & tasks:** `cron.yaml` literacy; Task Queues are legacy — **Cloud Tasks** is the successor (Part 3.4).
- **Config surface:** `app.yaml`, `dispatch.yaml`, `cron.yaml`; IAP on App Engine for admin.
- **Identity model:** legacy `X-Appengine-*` headers vs IAM invoker model — know both; prefer IAM for new paths.
- **Why still taught:** PCA case studies often ship with GAE already; strangler to Cloud Run is a valid answer.

#### From scratch / decision exercise
Compare the same health API on Cloud Run (1.2) vs App Engine standard:
- How do you set max instances / concurrency?
- How do you canary?
- What breaks if you need a custom system library?

Fill:

| Need | GAE standard | Cloud Run |
|---|---|---|
| Scale to zero | Yes | Yes |
| Arbitrary container | No (runtime list) | Yes |
| Traffic split built-in | First-class | Revisions + tags |
| Free envelope | F1 hours | Request pricing / Always Free card |

#### HLD
Brownfield: `appspot.com` service + Cloud SQL. Strangler: new routes on Cloud Run behind the same domain (dispatch or HTTPS LB later). Greenfield Northstar: stay on Cloud Run (ADR-001b).

#### LLD
- `app.yaml`: runtime, `automatic_scaling` vs `basic_scaling` vs `manual_scaling`, `max_instances`, warmup requests.
- Deploy version id strategy (`20260914t1530` style); never overwrite in place without a plan.
- Firewall / IAP notes for admin handlers.

#### Offerings
- **Standard** — sandboxed runtimes (Python, Go, Java, Node, PHP, Ruby), scale-to-zero, **28 F1 hours/day** free.
- **Flexible** — containers on GCE VMs you don’t fully manage; no scale-to-zero; rarely the right **new** choice vs Cloud Run.
- Services, versions, traffic splitting, App Engine cron, Task Queues (legacy; **Cloud Tasks** successor), `app.yaml`, `dispatch.yaml`, `cron.yaml`, IAP on App Engine.
- Google’s current guidance: new container HTTP apps → **Cloud Run**. App Engine remains on PCA and brownfield.

#### Curriculum
- `app.yaml`, automatic vs basic vs manual scaling, max instances, warmup.
- Deploy a version, split 50/50, roll back.
- App Engine firewall, IAP, legacy `X-Appengine-*` vs IAM invoker model.

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ Always Free standard: same Northstar health API as Python.  │
│ Deploy second version (Go ok after Python). Split 50/50.    │
│ Watch instance hours — stay inside ~28 F1 hours/day.        │
│ Delete/stop versions when done. No Flexible “for fun.”      │
│ Credits-optional: IAP on an admin service only.             │
└─────────────────────────────────────────────────────────────┘
```

#### Labs
- **Always Free standard:** same Northstar health API as Python service; split traffic; Go version as second version. Delete/stop when done so F1 hours stay inside 28/day.
- **Dashboard & quotas:** Console App Engine tiles — RPS, latency, errors, instance count, **instance hours**, versions, split. Metrics Explorer: `appengine.googleapis.com/http/server/response_*`. Instance hours = health **and** money. Split 50/50 compare version latency. Rebuild tiles for Cloud Run in Part 10.0.
- Task queues if shown: attempts/delay/errors/depth — same RED as Cloud Tasks (3.4). `cron.yaml` literacy; Scheduler is successor.

#### ADR-001b
- App Engine taught and labbed; Northstar production path stays Cloud Run unless constraint wins.

#### Gate
- Can deploy two versions, split, roll back; can explain standard vs flexible vs Cloud Run in one minute; F1 hours not blown.

#### PCA: PaaS literacy
- **Considerations:** versions/traffic; standard vs flexible; when not to start new on GAE.
- **Decision table:**

| Estate | Pick | Accept |
|---|---|---|
| Greenfield HTTP container | Cloud Run | Learn GAE for exam |
| Existing GAE + cron.yaml | Stay / strangler | Tech debt |
| Need flexible custom system libs | Prefer Cloud Run/GCE | Flexible is awkward middle |

- **Scenario prompt:** PCA case already runs App Engine standard.
- **Expected:** “I pick keep GAE + incremental Cloud Run strangler because Y, I accept Z (two compute styles briefly).”
### 1.10 Decision matrix (you will reuse this on the PCA)

#### PCA: 1.3 Network, storage, and compute resources (design)

**Guide themes (matrix):** hybrid/multicloud; ML/AI (Gemini, Agent Builder, Model Garden, Hypercomputer); VPC/peering/FW/LB/routing/containers/Shared VPC/PSC; data processing; storage types; GKE/Cloud Run/functions; spot/custom/specialized compute. Homes: 1, 2, 6, 8b, 9, 9b. **CDN:** full lesson is **1.4**; Part 6.13 is LB types + pointer only.

| Resource | Prefer | Accept |
|---|---|---|
| Request HTTP containers | Cloud Run | GKE if sidecars/GPU/custom CNI |
| Event FaaS | Cloud Run functions / Eventarc | Legacy 1st-gen only if brownfield |
| Object media | GCS + lifecycle/Autoclass | Filestore only if POSIX required |
| Hybrid | Shared VPC + HA VPN/Interconnect (**Parts 6.7 / 8b** — unlock before designing) | Peering when non-transitive OK |
| Training | Vertex + appropriate accelerator | DIY GPU MIG without ops plan |

**Scenario prompt:** Team wants GKE for a single CRUD API “because Kubernetes,” and a second team wants Spot for the payment API.

**Expected answer shape:** “I pick Cloud Run for the API because Y, I accept Spot only on Z (batch/stateless non-checkout), never on payment path.”


| Need | Offering |
|---|---|
| Request-driven containers, least ops | Cloud Run services |
| Run-to-completion | Cloud Run Jobs |
| Pull consumers | Cloud Run Worker Pools |
| Scale-to-zero PaaS without a container first | App Engine standard |
| You must SSH, install an agent, or run a vendor appliance | Compute Engine |
| Kubernetes API, sidecars, custom CNI | GKE |
| Always-on cheap sandbox | e2-micro GCE (not production) |

### 1.11 Cloud Functions (distinct from Cloud Run functions branding)

Event glue is not a microservice mesh. Functions shine when a **single trigger** should run a **small** piece of code; they fail when you invent a distributed monolith of sync Function→Function calls.

#### Concepts
- **Event-driven FaaS:** HTTP, Pub/Sub, Cloud Storage, Firestore (and more via Eventarc).
- **1st gen vs 2nd gen:** 2nd gen **is** a Cloud Run service under the hood (Eventarc). Prefer gen2 for new work. Gen1 = brownfield + cold-start/timeout quirks literacy.
- **Branding:** “Cloud Run functions” ≈ source-deploy path onto Cloud Run; still teach classic Functions triggers so PCA wording does not confuse you.
- **Cold start, timeout, memory:** size for the event, not for an entire checkout orchestrator.
- **IAM invoker:** unauthenticated HTTP only if explicitly required (webhooks with signed payloads are different from “public admin”).
- **VPC egress (defer detail):** Serverless VPC Access connector vs Direct VPC egress — only when the function must reach private IPs (Cloud SQL private IP, Memorystore). Default = **no VPC complexity**. **Prop Lock:** do not lab-attach a connector until **6.1b/6.2** VPC concept + theory tiers are confirmed; name the choice here, implement later.
- Always Free: ~2M invocations/month on Blaze (confirm current Always Free card in lab notes).

#### From scratch / decision exercise
Classify these (one line each):
1. GCS object-finalize → write metadata row.
2. Public multi-route shopping API.
3. Nightly 2-hour batch.
4. Stripe webhook receiver (already Part 5 — usually Cloud Run service).

Expected: (1) Functions gen2; (2) Cloud Run service; (3) Cloud Run Job / Batch; (4) Cloud Run service with raw body.

#### HLD
GCS → Eventarc/Functions gen2 → Firestore. Separate: clients → Cloud Run API. No sync Function fan-out for checkout.

#### LLD
- Trigger filter (bucket prefix).
- Idempotent write (object generation as key).
- Dead-letter / retry policy notes (Pub/Sub).
- Timeout budget < event retry storm.

#### Lab
- GCS object-finalize → function writes metadata to Firestore. Python then Go.
- Prove invoker IAM; unauthenticated HTTP only if explicitly required (prefer auth).

#### ADR
- New HTTP APIs → Cloud Run **services**; glue events → Cloud Run functions / Eventarc / Functions gen2.

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ Gen2 function on object finalize; small test bucket only.   │
│ Firestore write of metadata; IAM invoker locked down.       │
│ Stay inside Always Free invocations; delete test objects.   │
│ Credits-optional: VPC connector — skip unless SQL private.  │
└─────────────────────────────────────────────────────────────┘
```

#### Gate
- Event path works end-to-end; invoker not `allUsers` unless justified; ADR forbids Functions-as-monolith.

#### PCA: event glue vs services
- **Considerations:** right-sized compute; avoid Functions-as-monolith.
- **Decision table:**

| Trigger | Pick | Accept |
|---|---|---|
| Object finalize glue | Functions gen2 / Eventarc | Cold start |
| Public multi-route API | Cloud Run service | Not “one function per path” sprawl |
| Long CPU job | Cloud Run Job | Not Functions timeout boxing |

- **Scenario prompt:** Entire checkout written as 40 Cloud Functions calling each other sync.
- **Expected:** “I pick modular Cloud Run services (+ async Events) because Y, I accept Z (fewer nano-functions, clearer boundaries).”
### 1.12 High availability and autoscaling (video block, required)

A single VM with snapshots is **backup**, not **HA**. HA = redundant zones (or regions) + health-checked load balancing + autoscaling policies + dependency HA (SQL). This section teaches the Cloud Load Balancing map **one axis at a time** with a concrete use case **before** any classification quiz. CDN full lesson stays in **1.4**; Part **6.13** is LB types + pointer only.

#### PCA: 1.2 Technical requirements + WAF (design)

**Guide themes (matrix):** Well-Architected Framework familiarity; HA/failover; flexibility of cloud resources; scale for growth; performance/latency; Gemini Cloud Assist; backup/recovery. Homes: 1.12, 8, 9b, 10.

| Need | Prefer | Accept |
|---|---|---|
| HA for HTTP API | Multi-zone regional Cloud Run / GKE | Single-zone only for non-prod |
| Failover data | Cloud SQL HA / regional PD | Manual snapshots alone |
| Growth | Autoscale (Run concurrency, HPA, MIG) | Fixed capacity + pager |
| Assist | Gemini Cloud Assist as copilot | Blind apply of suggestions |
| Backup | Automated snapshots + tested restore | Backup without restore drill |

**Scenario prompt:** Exec asks for “five nines everywhere” and wants you to accept every Gemini Cloud Assist suggestion into prod tonight.

**Expected answer shape:** “I pick WAF-aligned regional HA matching the stated SLO because Y, I accept Z (no unreviewed Assist apply; no over-engineered multi-region).”

#### Concepts — HA and autoscaling first
- Redundancy without health checks is hope. Health checks remove bad backends; autoscaling adds capacity; autohealing replaces failed VMs in a MIG.
- **Cloud Run side:** regional multi-zone by default for many setups; min-instances for cold-start SLO; traffic split as progressive delivery (Part D4); multi-region active/active is an HLD sketch until you need it.
- **GCE side:** instance templates + **MIGs**: autoscaler (CPU, LB utilization, Cloud Monitoring metric, schedules), autohealing, rolling updates, canary, proactive/opportunistic updates.
- Regional MIG vs zonal MIG; multi-zone HA inside one region is the default “good” VM story.
- Backend services + NEGs (GCE, zonal, internet, serverless, hybrid) are how LBs point at stuff. Target pools are **legacy** — prefer backend services.
- Session affinity, SSL policies, URL maps, host/path rules — Application LB features (below).
- Docs home: [Cloud Load Balancing overview](https://cloud.google.com/load-balancing/docs/load-balancing-overview), [Choose a load balancer](https://cloud.google.com/load-balancing/docs/choosing-load-balancer).

---

#### Anchor A — External vs internal (use case before taxonomy)

**Concrete use case (external):** Shoppers on the public internet hit `www.northstar.example` HTTPS. Clients are not in your VPC. You need an **external** load balancer (or a platform URL like `*.run.app` / Firebase Hosting that already sits on Google’s edge).

**Concrete use case (internal):** The checkout API talks to an internal payments adapter only reachable on RFC1918. Employees’ browsers are *not* the client — other VPC workloads are. You need an **internal** load balancer (or PSC). Putting an internal-only service on an external LB “temporarily” is how data leaks.

| Question | External | Internal |
|---|---|---|
| Who are clients? | Internet (or Google Cloud VMs with internet path) | Same VPC / connected networks |
| Typical Northstar | Public storefront / public API | Service-to-service east-west |
| IP | Global/regional **external** address on forwarding rule | **Internal** address from subnet |
| PCA trap | “Everything external for simplicity” | “Inside VPC = trusted” (false — see 6.14) |

**Exercise:** Label three arrows on your HLD as external or internal. No quiz yet.

---

#### Anchor B — Global vs regional (use case before taxonomy)

**Concrete use case (global):** One anycast IP, users worldwide, backends in `us-central1` + `europe-west1`, Premium Network Service Tier, automatic steer to nearest healthy region. Classic fit: global external **Application** LB in front of multi-region Cloud Run or MIGs.

**Concrete use case (regional):** Data residency — traffic and backends must stay in `europe-west1`. Or Standard Tier cost optimization with a single region. Regional LB IP lives in one region; clients may still reach it from elsewhere, but backends are regional.

| Need | Prefer | Accept |
|---|---|---|
| Multi-region HTTP, one IP | Global external Application LB (Premium) | Higher tier cost |
| Residency / single-region | Regional external or internal LB | No cross-region failover |
| Cheap sandbox | Platform URL (`run.app`) — no reserved IP | Not a custom domain story |

**Exercise:** Write one sentence: “Northstar v0 uses ___ because ___.” Default answer is often regional Cloud Run without a reserved global IP until custom domain + CDN require the LB (**credits-optional**).

---

#### Anchor C — Application vs proxy vs passthrough (use case before taxonomy)

**Concrete use case (Application LB — L7):** HTTP(S) with URL maps (`/static/*` → GCS/CDN, `/api/*` → serverless NEG → Cloud Run), host rules, Cloud Armor WAF, Cloud CDN (enable on this LB — full CDN lesson **1.4**), SSL policies, HTTP→HTTPS redirect.

**Concrete use case (Proxy Network LB — L4 reverse proxy):** Non-HTTP TCP (e.g. custom binary protocol) where you want TLS offload at the proxy and advanced traffic controls, but not HTTP URL maps. Client TCP session terminates at the proxy; backend sees proxy connection.

**Concrete use case (Passthrough Network LB — L4 DSR):** Preserve **client source IP**; UDP/ESP/ICMP; direct server return. Example: a network appliance or game server that must see real client IPs and speak UDP. Packets are not proxied — backends reply directly to clients.

| Family | Layer | Preserves client IP? | HTTP features / CDN / Armor | Northstar default? |
|---|---|---|---|---|
| Application | L7 | Via headers (`X-Forwarded-For`) if configured | Yes | **Yes** for HTTPS APIs |
| Proxy Network | L4 TCP proxy | No (proxy hop) | No HTTP URL maps | Rare for Northstar |
| Passthrough Network | L4 DSR | **Yes** | No | Only if forced by protocol/IP |

**Exercise:** For each family, cite the Northstar (or anti-Northstar) use case above in your notes. Still no classification quiz.

---

#### Anchor D — Combine axes (still use-case driven)

Worked combinations you must be able to **draw**:

1. **Global external Application LB** → serverless NEG → Cloud Run (multi-region sketch) + optional Cloud CDN/Armor. Custom domain production edge.
2. **Regional external Application LB** → regional backends only (residency).
3. **Regional internal Application LB** → internal mesh of HTTP microservices.
4. **Regional external passthrough NLB** → UDP service with client IP preserved.
5. **Internal passthrough NLB** → internal L4 to a pool of VMs (databases’ friends are usually private IP / PSC — do not invent LB in front of Cloud SQL casually).

Forwarding rule **must** have an IP: ephemeral or reserved static (**6.3**). Deleting the rule without releasing a reserved IP = billing leak.

---


#### Teaching metaphors (rung-1 — from official product map)
- **Reception desk vs open hallway:** Proxy LB = receptionist takes your call then dials an employee (new connection). Passthrough = hallway sign pointing you to the employee’s desk (same packet envelope; DSR replies skip the desk).
- **One poster, many cities:** Global external Application LB = one anycast IP; GFEs nearby terminate TLS and steer to the nearest healthy region — **only if** you attached multi-region backends.
- **Embassy rule:** Traffic/TLS must not leave a jurisdiction → **regional** external Application LB with backends only there (not “regional = private”).
- **Internal water cooler:** Microservice A→B inside the VPC → internal LB (or PSC), never an external VIP “temporarily.”
- **Classic vs managed:** Classic Application LB uses older `EXTERNAL` scheme; prefer global **EXTERNAL_MANAGED** for new work ([Choose a load balancer](https://cloud.google.com/load-balancing/docs/choosing-load-balancer)).
- **Cross-region internal:** Internal Application / proxy Network LBs can span regions with regional internal IPs — not the same as global anycast.
- **Resilience:** Global/cross-region designs survive regional outage **iff** healthy backends exist elsewhere. Regional LB + single-region backends → region outage = total outage.

#### Classification quiz (only after Anchors A–D)
Given: (a) public HTTPS API multi-region; (b) internal HTTP between services in one region; (c) UDP game with real client IPs; (d) TCP TLS offload without HTTP. Pick LB family + external/internal + global/regional. Check against [Choose a load balancer](https://cloud.google.com/load-balancing/docs/choosing-load-balancer).

#### From scratch
- Reuse 1.4 local L7 proxy: two backends, health-check `/healthz`, drain one backend, prove traffic moves.
- Add weighted round-robin (canary %). Map features → GCP Application LB URL map + traffic split on Cloud Run.

#### HLD
Draw both: (1) HTTPS LB → MIG; (2) HTTPS LB → serverless NEG → Cloud Run. Mark zones. Mark SQL HA as a separate dependency.

#### LLD
- Health endpoint that fails on a file flag (for LB health checks in credits lab).
- Autoscaler signals: CPU vs request concurrency (Run) vs LB utilization (MIG).
- Autohealing ≠ autoscaling (explain in one paragraph).

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ Required: diagram + Terraform for regional MIG + HTTP(S) LB │
│          OR Cloud Run multi-zone story with traffic split.  │
│ Live second e2-micro in a MIG usually BILLS — credits only. │
│ Alternative free path: Cloud Run min=0; second region = HLD.│
│ Credits-optional: global HTTPS LB + serverless NEG + Armor. │
│ ALWAYS release reserved static IPs in the same sitting.     │
└─────────────────────────────────────────────────────────────┘
```

#### Labs
- **Free-tier boxed:** two e2-micro in a regional MIG usually **bills** the second VM — diagram + Terraform **required**; live MIG only with credits. Alternative: Cloud Run min-instances=0 with second region sketched on the HLD.
- **Python / Go:** health endpoint that fails on a file flag — used by LB health checks in the credits lab.

#### Gate
- Can draw HTTP(S) LB → MIG and HTTP(S) LB → serverless NEG.
- Can explain external/internal, global/regional, application/proxy/passthrough **with a use case each**.
- Can explain autohealing vs autoscaling; quiz only after anchors.

#### PCA: HA / LB design
- **Considerations:** multi-zone; global vs regional LB; health checks; RTO.
- **Decision table:**

| Need | LB / compute | Accept |
|---|---|---|
| Serverless HTTP HA | Global HTTPS LB + serverless NEG → Cloud Run | LB SKUs if not on run.app |
| VM fleet | Regional MIG + HTTP(S) LB | You manage images |
| Internal east-west | Internal HTTP(S) or passthrough | No internet exposure |

- **Scenario prompt:** Single zonal VM behind a DNS A record; “HA” claimed because disk snapshots exist.
- **Expected:** “I pick multi-zone MIG + LB health checks because Y (snapshots ≠ HA), I accept Z (more cost) — or Cloud Run regional.”
## Part D — DevOps, Docker, Kubernetes, CI/CD, GitOps

**Goal:** You can build, sign, promote, and roll back Northstar the way a 2026 GCP platform team does — not “a Jenkinsfile that SSHs to a VM.”

Research used: Google Cloud Build + Artifact Registry + Cloud Deploy + Skaffold (GCP-native shortest path); modern CI/CD with GKE (GitHub, kustomize, two-repo GitOps); Cloud Deploy canary for GKE and Cloud Run; Binary Authorization + SLSA; DORA; Docker BuildKit multi-stage/distroless; Kubernetes 1.33–1.37 (sidecar GA, user namespaces, DRA, Pod-level resources, PSA); Argo CD vs Flux vs Cloud Deploy.

Free-tier: Cloud Build 2,500 e2-standard-2 minutes/month; Artifact Registry 500 MB; Cloud Deploy first active pipeline per billing account. GKE/Argo live remains credits-optional; kind/minikube is required.

---

### D0 DevOps culture (concept, then GCP)


#### PCA: 4.1 Technical processes

**Guide themes (matrix):** SDLC; CI/CD; RCA; testing/validation; service catalog/provisioning; DR. Homes: D, 1.6, 10.

| Process | Prefer | Accept |
|---|---|---|
| Ship | Cloud Build + WIF + Cloud Deploy | Manual `gcloud` prod push |
| Test | Unit/contract/integration + emulators | Prod-only validation |
| DR | Documented RTO/RPO + restore drill | Backup without restore |
| RCA | Blameless + action items | Blame thread only |

**Scenario prompt:** Team skips staging and pages only when customers tweet.

**Expected answer shape:** “I pick CI/CD with gated promote + SLO burn freeze because Y, I accept Z (feature flags over hotfix-only).”


What DevOps is (and is not):
- Not a job title that “throws code over the wall to the DevOps team.”
- CALMS: Culture, Automation, Lean, Measurement, Sharing.
- You build it, you run it. Feedback loops measured in hours, not quarters.
- **SRE** (Google): error budgets, SLIs/SLOs, toil, blameless postmortems. DevOps is the culture; SRE is Google’s implementation.
- **Platform engineering:** an internal product (golden paths, paved road) so app teams self-serve. IDP is the UI; GitOps is the control plane.
- **DevSecOps:** security gates in the pipeline (SAST, SCA, secrets, image scan, policy) without becoming a bottleneck. Shift-left *and* shift-right (runtime).
- **DORA four keys** (elite vs low):
  | Metric | Elite (order of magnitude) |
  |---|---|
  | Deployment frequency | Multiple per day |
  | Lead time for changes | Less than one hour |
  | Change failure rate | 0–15% |
  | Failed-deployment recovery | Less than one hour |
- WAF operational excellence + DORA: loosely coupled architecture predicts CD. That is why Northstar is split into services *after* you can deploy one of them automatically.
- CapEx vs OpEx, change management, SDLC (PCA 4.1 / 4.2) live here as process, not slides.

**HLD exercise:** current vs target DORA for Northstar; which bottleneck is people, architecture, or pipeline.

**Python / Go:** parse a synthetic deploy log; compute the four DORA metrics for a week.

---

### D1 Docker and OCI (full offering)

This is the container track an architect and an implementer both need. Cloud Run’s contract is a *subset*; you still must understand the image.

#### D1.1 Why containers
- **From scratch (Linux):** a script that `unshare`s pid/net/mnt, `chroot`s to a directory, and runs `/bin/sh`. Read cgroup files. This is not Docker; it is why Docker exists.
- Process isolation vs VMs. Namespaces (pid, net, mnt, uts, ipc, user), cgroups v2, union FS.
- Image vs container vs registry vs runtime (containerd, not “Docker in production on GKE”).
- OCI image spec vs Docker image. Artifact Registry stores OCI.

#### D1.2 Dockerfile as LLD
2026 production pattern (required, not optional style):
- `# syntax=docker/dockerfile:1` (BuildKit frontend).
- **Multi-stage:** builder vs runtime. Copy only the binary/site.
- **Cache mounts:** `RUN --mount=type=cache` for pip/go-mod/npm.
- **Secrets mounts:** `RUN --mount=type=secret` — never `ARG` a token into a layer.
- Layer order: deps before source.
- `.dockerignore`.
- Pin bases by **digest**, not `latest`. Prefer distroless or `-slim`; nonroot USER.
- Health: your app still listens on `PORT` (Cloud Run) or `EXPOSE` is documentation only.
- PID 1, SIGTERM, zombie reaping (`tini` only if you must; Go/Python should handle signals).
- Multi-arch: `linux/amd64,linux/arm64` via buildx. Cloud Run is amd64 unless you pick otherwise.

**Python lab:** multi-stage FastAPI image, distroless or slim-nonroot, no pip in final. **Go after submit:** `CGO_ENABLED=0` → `gcr.io/distroless/static-debian12:nonroot`.

#### D1.3 Local workflow
- `docker build`, `run`, `exec`, `logs`, `compose` for local Postgres/Redis (Part 2).
- Compose is **not** production orchestrator. Do not “compose up on a GCE VM” as the architecture.

#### D1.4 Registries
- Artifact Registry (Docker, Maven, npm, Python, apt). Vulnerability scanning (Artifact Analysis).
- Immutable tags vs digest. Promote **by digest**, never rebuild per environment.
- Cleanup policies (cost). 500 MB Always Free — prune.
- **Python / Go:** list images via Artifact Registry API; fail if a tag is not a digest.

#### D1.5 Runtime contract (ties to Cloud Run / GKE)
- Read-only root FS, dropped caps, no privileged, no hostPath.
- Resource requests/limits. liveness vs readiness vs startup probes (K8s); Cloud Run uses your process + CPU allocation instead of kube probes.

---

### D2 Continuous integration

CI = every commit is **built, tested, and proven** to be an artifact. CI does not deploy production.

#### D2.1 Pipeline anatomy
```
commit → lint → unit → build image → SCA/SAST/secret scan
      → integration tests (Testcontainers / emulator)
      → push digest to Artifact Registry
      → provenance / SBOM
      → hand digest to CD (do not kubectl / gcloud run deploy to prod here)
```
- Build once, promote the digest. Rebuild-per-env is a defect.
- Branching: trunk-based default; GitFlow only if you can defend lead-time cost.
- Flaky tests are change-failure-rate.

#### D2.2 Cloud Build — full `cloudbuild.yaml` (required literacy)
Minimal production-shaped file (adapt service name):
```yaml
steps:
  - name: python:3.12
    entrypoint: bash
    args: ["-c", "pip install -r requirements.txt && pytest -q"]
  - name: golang:1.22
    entrypoint: bash
    args: ["-c", "go test ./... && go install golang.org/x/vuln/cmd/govulncheck@latest && govulncheck ./..."]
  - name: gcr.io/cloud-builders/docker
    args: ["build", "-t", "$_AR/$PROJECT_ID/$_SVC:$SHORT_SHA", "."]
  - name: gcr.io/cloud-builders/docker
    args: ["push", "$_AR/$PROJECT_ID/$_SVC:$SHORT_SHA"]
  - name: gcr.io/cloud-builders/gcloud
    args: ["artifacts", "docker", "images", "describe",
           "$_AR/$PROJECT_ID/$_SVC:$SHORT_SHA", "--format=json"]
substitutions:
  _AR: us-central1-docker.pkg.dev
  _SVC: northstar-api
images:
  - "$_AR/$PROJECT_ID/$_SVC:$SHORT_SHA"
options:
  logging: CLOUD_LOGGING_ONLY
```
- Substitutions; secrets from Secret Manager (availableSecrets); private worker pools when VPC/SQL access needed.
- Triggers: GitHub 2nd gen with **WIF** (no PAT if avoidable), CSR, Pub/Sub, manual.
- Provenance: trusted builder path for Binary Authorization SLSA check (D5).
- Quotas: 2,500 e2-standard-2 minutes/month Always Free — small images.
- **Lab:** trigger on `main` → tests → build → push `:sha` + record digest. **No prod deploy step yet.**

#### D2.3 GitHub Actions + WIF (full pattern)
1. Create Workload Identity Pool + provider (GitHub `token.actions.githubusercontent.com`).
2. Bind `roles/iam.workloadIdentityUser` on deploy/build SA to `principalSet://.../attribute.repository/ORG/REPO`.
3. Workflow:
```yaml
permissions:
  id-token: write
  contents: read
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: google-github-actions/auth@v2
        with:
          workload_identity_provider: projects/N/locations/global/workloadIdentityPools/P/providers/PR
          service_account: build@$PROJECT.iam.gserviceaccount.com
      - uses: google-github-actions/setup-gcloud@v2
      # docker auth to Artifact Registry, then build/push digest
```
- **Lab proof:** Actions log shows federated auth; repo has **zero** `GCP_SA_KEY` secrets.
- When Actions vs Cloud Build: GitHub-first org → Actions; need Google trusted builder / private network → Cloud Build. Same WIF idea for GitLab/Circle; Jenkins = brownfield only.

#### D2.4–D2.5 Tests and scanning
- Unit, contract (OpenAPI), integration (Firestore/Pub/Sub emulators, Postgres in Docker — PCA 5.2).
- Secret scan fail on Stripe keys; `pip-audit` / `govulncheck`; Artifact Analysis CRITICAL fail; tfsec/Checkov on Terraform.
- **Lab:** planted secret fails; CRITICAL base CVE fails.

#### Gate
- Digest in AR; CI green required; WIF documented in README.
### D3 Continuous delivery and GitOps

#### PCA: 5.1 Advising deploy / Apigee / migration tooling

**Guide themes (matrix):** application/infra deploy; Apigee API management; test frameworks; migration tooling; Gemini Cloud Assist. Homes: D3, 3.3, 8c, 9b.

| Concern | Prefer | Accept |
|---|---|---|
| External API product | Apigee | API Gateway for simpler Northstar |
| Deploy | Cloud Deploy / GitOps | SSH to nodes |
| Migrate | Migration Center + DMS | Untested cutover |
| Assist | Gemini Cloud Assist reviewed | Auto-merge Assist diffs |

**Scenario prompt:** Partner APIs need quotas/monetization; internal BFF does not.

**Expected answer shape:** “I pick Apigee for partner APIs + Cloud Deploy for services because Y, I accept Z (API Gateway for internal BFF).”


CD = the **same digest** moves through environments with an audit trail and a rollback.

#### D3.1 CI vs CD vs GitOps
| | CI | CD (push) | GitOps (pull) |
|---|---|---|---|
| Trigger | commit | promote | Git desired-state change |
| Actor | Cloud Build / Actions | Cloud Deploy / controller | Argo CD / Flux |
| Source of truth | source repo | pipeline + artifact | **env Git repo** |
| Prod kubectl | forbidden | via controller | via controller |

Google patterns: (1) Cloud Build + **Cloud Deploy** + Skaffold; (2) two-repo GitOps (app CI writes digest; env repo manifests; Argo/Flux apply).

**ADR-D01:** Northstar v1 = Cloud Build → AR → Cloud Deploy → **Cloud Run**. GKE GitOps in Part 9. Argo taught; not required live.

#### D3.2 Skaffold
- `skaffold.yaml`: render/apply parity local ↔ Cloud Deploy. Pin Skaffold version (12-month window). Profiles per env. `deploy.cloudrun` for this track.

#### D3.3 Cloud Deploy canary (required depth)
- Delivery pipeline + targets (Cloud Run service/job/worker pool, GKE, custom).
- Release = digest + rendered manifests. Stages: dev → staging → prod.
- **Canary strategy:** percentages (e.g. 5 → 25 → 50 → 100), **verify jobs**, pre/post deploy hooks. Cloud Run canary = traffic splits on revisions; GKE = Service/Gateway or pod counts.
- Parallel multi-region optional.
- Rollback is a first-class Console/API action — not “redeploy old tag by hand.”
- First active pipeline per billing account free; destroy lab pipelines.
- **Lab:** two Cloud Run targets; create release from Cloud Build; promote; canary verify that curls `/healthz` and checks 5xx; **rollback**. Same image digest Python/Go.

Example canary sketch (conceptual YAML fields — match current Cloud Deploy schema in docs when implementing):
```yaml
# serialPipeline stage with strategy.canary.runtimeConfig.cloudRun + percentages + verify
# verify: container that exits non-zero on SLO burn → automatic halt/rollback policy
```

#### D3.4–D3.5 Manifests and GitOps
- Raw YAML v0 → **kustomize** overlays (default for Northstar GKE) → Helm if org-standard.
- Desired state in Git; drift is an event; promotion = PR changing digest; never `kubectl apply` in prod except logged break-glass.
- Cloud Deploy = push from Google; Argo/Flux = pull in-cluster.

#### Code
- **Python / Go:** tool that updates env-repo kustomization with new digest (CI writes digest step).

#### Gate
- Promote + rollback rehearsed; canary verify job exists; no prod deploy from laptop.
### D4 Progressive delivery

#### Concept
Progressive delivery is how you **limit blast radius** while a new digest meets real traffic. Recreate (tear down → new) is for **jobs** only — not user-facing services. Rolling is the default (Deployment surge / Cloud Run gradual revision). Blue-green keeps two full stacks and flips traffic — instant rollback, **double capacity cost**. Canary shifts 1% → 10% → 50% → 100% with **automated verify** (Cloud Deploy verify job, Cloud Monitoring SLO burn, or Argo Rollouts analysis) that **halts or rolls back** on failure. Shadow / dark launch mirrors production requests to a candidate without affecting user responses — concept only unless you instrument carefully. Cloud Run `--tag` + traffic split (Part 1.6) becomes a **pipeline promotion**, not a laptop ritual. **Feature flags ≠ canary:** flags gate *behavior* inside one digest; canary gates *which digest* serves traffic. Flags do not replace canary verify.

#### From scratch / exercise
1. Write a one-page decision matrix: recreate / rolling / blue-green / canary / shadow — pick one Northstar surface each (checkout API, nightly job, admin UI).
2. Sketch Cloud Deploy canary percentages + a verify container that curls `/healthz` and fails on 5xx rate above budget.
3. Separate ADR lines: “flag for dark UI copy” vs “canary for checkout pricing digest.”

#### HLD / LLD
**HLD:** Northstar checkout canary **5% for 15 minutes**; auto-rollback on 5xx burn or latency SLO burn; sticky sessions avoided so canary mixes fairly. Mermaid: Build → AR digest → Cloud Deploy stage → Cloud Run revisions (stable + canary) → Monitoring verify → promote or rollback.
**LLD:** Release = immutable digest; traffic weights on revisions; verify job exit code is the gate; rollback is first-class API/Console action (not “redeploy old tag by hand”).

#### Free-tier lab note
Use Cloud Run traffic tags/splits on Always Free / low-cost revisions; Cloud Deploy first pipeline free per billing account — **destroy** lab pipelines. No need for dual full GKE clusters for blue-green on this track.

#### Gate
Explain when blue-green beats canary (and cost). Show a canary verify that would auto-halt. Name one misuse of flags as a canary substitute. ADR: “I pick canary 5%→100% because Y, I accept Z (longer promote).”

### D5 Software supply chain

PCA 3.1 “securing software supply chain.” Not optional color.

#### Threats
Compromised CI, malicious dep, unsigned image, mutable tags, stolen deploy SA.

#### SLSA
- L1 provenance exists → L2 hosted isolated build → L3 unforgeable provenance from **trusted builder**.
- Cloud Build is the trusted builder Binary Authorization’s SLSA check accepts.
- Attach **SBOM** (Syft / `gcloud` artifacts). **cosign** sign/verify (keyless OIDC or KMS).

#### Binary Authorization (full)
- Policy: require attestations; deny `:latest`; allowlist; dry-run vs **enforce**.
- Attestors + KMS keys; continuous validation after deploy.
- SLSA check fields: `trustedBuilder: GOOGLE_CLOUD_BUILD`, trusted source repo patterns.
- Applies to GKE and Cloud Run.
- Separation of duties: builder project ≠ deploy project ≠ attestor project (multi-project tutorial).

#### Lab
- **Required:** write a BinAuthz policy YAML that would reject an unsigned / `:latest` image; document dry-run → enforce path.
- **Credits-optional:** enforce on a Cloud Run service; prove blocked revision; then attest and pass.
- **Python / Go:** verify dummy attestation payload; fail pipeline if missing.

#### Gate
- Policy reviewed; `:latest` cannot promote; attestations required in enforce mode notes.

#### PCA: supply chain
- **Considerations:** 3.1 securing software supply chain; keys vs attestation.
- **Decision table:**

| Control | When | Accept |
|---|---|---|
| WIF + no keys | Always for CI | Setup |
| Digest promote | Always | Tag UX loss |
| BinAuthz enforce | Prod | Break-glass process needed |

- **Scenario prompt:** Prod pulls `api:latest` nightly from a shared mutable tag.
- **Expected:** “I pick digest + BinAuthz because Y, I accept Z (explicit promote) — `:latest` is a defect.”
### D6 Platform engineering and developer experience

#### Concept
Platform engineering productizes the **golden path** so product teams ship without filing tickets for Cloud Run, IAM, or CI. A template repo / `cookiecutter` ships Dockerfile, `cloudbuild.yaml`, Skaffold, Terraform module stubs, CODEOWNERS, and lint/test gates. **Preview environments:** ephemeral Cloud Run tagged revision (or project) per PR — destroy on merge/close. **Policy as code** is layered: Organization Policy (org constraints) → Binary Authorization (image admit) → OPA/Gatekeeper or Kyverno (K8s admission) — know which layer owns which decision. Self-service means a developer opens a PR that creates a service from the template; the platform team owns the path, not every ticket. DX metrics that matter: time-to-first-PR-to-prod, mean time to recover via rollback, % services on golden path — not “number of tools.”

#### From scratch / exercise
Write the **Northstar service template README** a new hire follows to production in **one PR**: clone template → fill SERVICE_NAME → PR opens preview URL → merge promotes via Cloud Deploy. Include: required labels, WIF note, who to page, how to destroy preview.

#### HLD / LLD
**HLD:** Platform control plane (template + CI + policy) vs product data plane (Northstar services). Mermaid: Dev → template PR → preview Run → merge → digest → Deploy → prod.
**LLD:** Template variables; CODEOWNERS for `/infra` and `/deploy`; preview naming `pr-{n}-{svc}`; TTL/destroy job; policy bundle version pinned in the template.

#### Free-tier lab note
Preview = Cloud Run tag on existing service or a short-lived service in the same project with budget alerts; tear down on merge. Org Policy / Gatekeeper live enforce is **credits / org-admin optional** — paper the policies if you lack org rights.

#### Gate
New hire path works from README alone. Preview destroys on merge (documented or automated). You can name which policy layer blocks `:latest` vs which blocks public bucket. ADR: “I pick golden-path template + preview tags because Y, I accept Z (less one-off snowflake).”

### D7 IaC in the pipeline (ties to Terraform)

#### Concept
Infrastructure changes follow the **same promotion rules** as app digests: plan on PR, apply on merge to the `infra` repo — **never** `terraform apply` from a laptop to prod. State lives in a **GCS backend with locking**; **separate state per env** (dev/staging/prod) so a bad plan cannot cross the blast radius. Cloud Build (or Actions + WIF) is the only apply principal in prod. Deployment Manager is legacy (Part 1.8). Config Connector / Infrastructure Manager are GCP-native options — literacy only unless your org standardizes. OpenTofu exists as a Terraform fork; **this course uses the official Terraform Google provider**. App pipelines consume outputs (AR repo URL, SA emails) via remote state or published artifacts — do not copy-paste prod IDs into app YAML by hand.

#### From scratch / exercise
1. PR workflow: `terraform fmt` + `validate` + `plan` comment on PR; apply only on merge to protected branch.
2. **Python / Go:** parse `terraform show -json` (or plan JSON) and **fail CI** if any created resource lacks `labels.env` (and ideally `labels.owner`).
3. Document break-glass: who can unlock state, how to recover a failed apply mid-way.

#### HLD / LLD
**HLD:** `infra` repo → Cloud Build WIF → plan/apply → GCS state; app repo reads outputs. Mermaid: PR plan → review → merge apply → state lock → outputs → app Deploy.
**LLD:** Backend bucket + prefix per env; SA with least privilege on that prefix; no shared “god” apply SA across prod+dev; pin provider versions; `prevent_destroy` on irreplaceable DBs.

#### Free-tier lab note
Tiny resources only (SA, bucket, Cloud Run stub). GCS state bucket is cheap — enable versioning. Destroy lab resources after. Do not leave unlocked state or broad `roles/owner` on the apply SA.

#### Gate
No laptop apply to prod in the runbook. Plan-on-PR / apply-on-merge demonstrated (or papered with exact trigger YAML). Label check fails a deliberately unlabeled resource. ADR: “I pick separate state per env + WIF apply because Y, I accept Z (more repos/triggers).”

### D8 Kubernetes internals (CKA-level — taught with Part 9)

This is Kubernetes **the system**, not only GKE product knobs. GKE is how you run it on GCP.

#### D8.1 Control plane
- kube-apiserver, etcd, scheduler, controller-manager. GKE: you do not SSH the control plane; you still must know what it does.
- Declarative desired state. Controllers reconcile. That *is* GitOps’s runtime.
- **From scratch:** a 50-line reconcile loop: desired replica count vs running processes; spawn/kill until equal; requeue on failure. That is a controller.

#### D8.2 Objects you must be able to write from memory
- Pod, ReplicaSet, Deployment, StatefulSet, DaemonSet, Job, CronJob.
- Service (ClusterIP, NodePort, LoadBalancer, headless), Endpoints/EndpointSlice.
- Ingress vs **Gateway API** (GKE preferred path going forward).
- ConfigMap, Secret (and why Secrets are not secret — use Secret Manager / External Secrets).
- PVC, PV, StorageClass. GKE PD CSI, Filestore for RWX.
- HPA, VPA, PDB. Cluster autoscaler / node auto-provisioning / Autopilot.
- NetworkPolicy. Default-deny + allow.
- ResourceQuota, LimitRange.
- RBAC: Role, ClusterRole, Binding. Least privilege. No cluster-admin for apps.
- ServiceAccount + Workload Identity Federation for GKE (no node SA keys).

#### D8.3 Scheduling and packing
- requests vs limits, QoS (Guaranteed/Burstable/BestEffort).
- taints/tolerations, affinity/anti-affinity, topologySpread.
- Pod-level resource requests (beta/GA on recent versions).
- DRA (Dynamic Resource Allocation) GA in 1.34 — GPUs/TPUs as first-class, PCA-relevant for AI nodes.

#### D8.4 Workload security
- Pod Security Admission (replace PSP, removed 1.25): privileged / baseline / restricted per namespace.
- securityContext: nonroot, readOnlyRootFilesystem, allowPrivilegeEscalation:false, seccomp, appArmorProfile (GA 1.31+).
- Sidecar containers GA 1.33 (`restartPolicy: Always` init). Mesh proxies.
- User namespaces (`hostUsers: false`) GA 1.33 — container-escape blast radius.
- Admission: Gatekeeper/Kyverno + Binary Authorization.

#### D8.5 Networking
- CNI, kube-proxy vs Dataplane V2 (Cilium-based on GKE).
- kube-dns / Cloud DNS. ClusterIP path.
- GKE Gateway, NEG, HTTP(S) LB. Container-native load balancing.

#### D8.6 Rollouts and ops
- `kubectl rollout`, surge, maxUnavailable.
- Probes. Startup probe for slow boots.
- Logs: stdout; GKE → Cloud Logging. Don’t kubectl logs as the architecture.
- Upgrades: GKE release channels (Rapid/Regular/Stable), surge upgrades, blue-green node pools, version skew (nodes ≤ 2 minors behind control plane). Control plane upgrades cannot be disabled.
- **Local lab (required):** kind — Deployment, Service, HPA, NetworkPolicy, PSA restricted, rolling update, rollback.
- **Python / Go:** a controller-shaped script is *not* required; instead, generate Deployment YAML from a template and apply to kind in CI.

Part 9 GKE product surface (Autopilot vs Standard, private cluster, etc.) continues to apply this internals model on GCP.

---

## Part 2 — SQL design, Cloud SQL setup, Firestore, objects

**Goal:** You can model a relational schema for Northstar, write migrations, and stand up **Cloud SQL PostgreSQL** the way a production team does — private IP, Auth Proxy, HA, backups — even if the live instance is credits-optional.

### 2.1 SQL database design (concept, language-agnostic, then Python/Go)


This is a full design track, not “pick Cloud SQL on the exam.”

#### Design spine
- Conceptual → logical → physical. ER for catalog, cart, order, payment_intent, user, tenant.
- Normalization 1NF–3NF; deliberate denormalize with ADR. Keys, FKs, uniqueness, CHECKs.
- ACID — **derive** what each letter forbids; isolation levels; dirty/nonrepeatable/phantom — **predict** before running.
- Engine floor: relational algebra; FDs; B-tree vs heap; MVCC; locks; WAL/checkpoints/PITR; vacuum. Hide behind Cloud SQL only after you can name what is hidden.
- Indexing + `EXPLAIN (ANALYZE, BUFFERS)`. Transactions + `orders.idempotency_key UNIQUE`.
- Migrations expand/contract (Alembic / golang-migrate). Multi-tenant: shared schema + RLS default.
- OLTP vs OLAP: do not analytics-scan the primary.

#### Lab (local, required)
Docker PostgreSQL; Northstar OLTP schema; migrations; seed; queries.
**Python:** SQLAlchemy/`psycopg` — create order + lines in one txn; concurrent stock decrement must not oversell.
**Go after submit:** `database/sql` + `pgx`, same tests. **G4** WAL codec feeds DB-10.

#### LLD artifacts
ERD, DDL, index list, isolation ADR, migration plan.

#### Engine slices DB-1–DB-10 (each: toy spec, SQL, EXPLAIN prediction, Cloud SQL mapping)

##### DB-1 — Relational algebra & 3VL
- **Toy spec:** In-memory bag relations; implement select/project/join/semi/anti/outer; NULL 3VL truth table tests.
- **SQL:** `SELECT … FROM order_line ol LEFT JOIN product p ON … WHERE p.id IS NULL` (anti-join shape); `EXCEPT` vs `NOT EXISTS`.
- **EXPLAIN prediction:** Nested loop vs hash join for small vs large build side — write prediction, then `EXPLAIN`.
- **Cloud SQL mapping:** Same planner; Query Insights shows top queries; no algebra change because managed.

##### DB-2 — Catalog, tuples, constraints
- **Toy spec:** Schema registry struct; enforce PK/FK/CHECK in a toy before SQL; deferred constraint flag.
- **SQL:** `UUID` PKs; `JSONB` attrs; `CHECK (qty > 0)`; `FOREIGN KEY … DEFERRABLE`; inspect `ctid`/`xmin`/`xmax` in learning DB.
- **EXPLAIN prediction:** PK lookup = index only; missing FK index on child → seq scan on delete-parent check.
- **Cloud SQL mapping:** Flags for constraints; migrations via Job (2.6); IAM DB users still have catalogs.

##### DB-3 — CTEs, windows, lateral
- **Toy spec:** Window functions as framed iterators over sorted partitions (unit-test ranking).
- **SQL:** Order GMV by day with `SUM() OVER (PARTITION BY day)`; recursive CTE category tree; `LATERAL` top-N per tenant.
- **EXPLAIN prediction:** Window sorts; recursive CTE worktable; predict `Sort` / `CTE Scan` nodes.
- **Cloud SQL mapping:** Same SQL; watch `work_mem` for sorts on small tiers (`db-f1-micro` spills early).

##### DB-4 — Heap pages & TOAST
- **Toy spec:** Slotted page: insert/delete/compact line pointers; overflow TOAST-like external blob store.
- **SQL:** Wide `TEXT`/`JSONB` row; compare `pg_column_size` in-row vs toasted; `VACUUM` effects later (DB-9).
- **EXPLAIN prediction:** Seq scan cost rises with toast fetch — predict heap blocks vs toast blocks in `BUFFERS`.
- **Cloud SQL mapping:** Storage autogrow; you still pay GB-month; Insights won’t replace page literacy.

##### DB-5 — Buffer pool
- **Toy spec:** Clock-sweep buffer pool with pins; hit-ratio benchmark under sequential vs random read.
- **SQL:** Warm cache vs cold (`EXPLAIN (ANALYZE, BUFFERS)` shared hit vs read).
- **EXPLAIN prediction:** Second run of same query → higher shared hit%; predict before measure.
- **Cloud SQL mapping:** Instance memory tier ≈ shared_buffers headroom; scaling tier is how you “buy” cache.

##### DB-6 — Indexes
- **Toy spec:** Userspace B-tree (insert/search/range) + inverted index for tokens (GIN-shaped).
- **SQL:** Composite `(tenant_id, created_at)`; partial `WHERE status = 'open'`; covering `INCLUDE`; `JSONB` GIN.
- **EXPLAIN prediction:** Equality on leftmost → index scan; leading-wildcard `LIKE` → seq; bitmap for OR of two indexes.
- **Cloud SQL mapping:** Create indexes concurrently in expand migrations; monitor bloat; AlloyDB/columnar later if HTAP.

##### DB-7 — Executor & spill
- **Toy spec:** Iterator nodes nested-loop / hash / merge; force spill when “work_mem” exceeded.
- **SQL:** Join order_line↔product; `SET work_mem = '64kB'` in session to force spill; compare.
- **EXPLAIN prediction:** Hash join with low `work_mem` → temp written; predict before `ANALYZE`.
- **Cloud SQL mapping:** Flags `work_mem`/`temp_file` monitoring; do not raise blindly — memory × connections.

##### DB-8 — Planner statistics
- **Toy spec:** Histogram + MCV sketch; estimate selectivity; pick join algorithm from estimates.
- **SQL:** `ANALYZE`; inspect `pg_stats`; compare predicted rows vs `EXPLAIN` rows; create skewed tenant data.
- **EXPLAIN prediction:** Write row estimates for skewed tenant vs uniform; then explain misestimates.
- **Cloud SQL mapping:** Autovacuum/analyze; Query Insights; extend statistics when needed.

##### DB-9 — MVCC, locks, vacuum
- **Toy spec:** Visibility simulator (xmin/xmax snapshots); deadlock graph detector; HOT update sketch.
- **SQL:** Isolation labs (RC vs RR vs Serializable); deliberate deadlock; observe `VACUUM`/bloat.
- **EXPLAIN prediction:** Under RR, predict anomaly prevented; under RC, predict nonrepeatable — confirm.
- **Cloud SQL mapping:** HA does not remove need for vacuum; long txns hurt; set statement timeouts.

##### DB-10 — WAL, replica, PITR (**G4**)
- **Toy spec:** Mini WAL append/CRC/replay; checkpoint; streaming replica mock; backup/restore drill.
- **SQL:** `pg_switch_wal()` in learning PG; base backup story; promote replica (local compose).
- **EXPLAIN prediction:** N/A for WAL — instead **predict** recovery: crash after commit → row present; after uncommitted → absent.
- **Cloud SQL mapping:** Automated backups, PITR window, HA regional standby, replica flags — name each Cloud SQL knob against the toy.

Do not reimplement PostgreSQL. Do not skip a slice because Cloud SQL hides it.

#### PCA: storage & consistency
- **Considerations:** PCA storage types; HA/PITR; transactions across services (outbox later).
- **Decision table:**

| Need | Pick | Accept |
|---|---|---|
| Standard OLTP | Cloud SQL Postgres | Regional limit |
| Global strong SQL | Spanner | Cost/complexity |
| Hide WAL forever | Forbidden as learning path | Managed after toys |

- **Scenario prompt:** “We don’t need backups; Cloud SQL is managed.”
- **Expected:** “I pick PITR + tested restore because Y (managed ≠ immortal), I accept Z (backup storage cost).”

#### Go G4 — files, bufio, embed, time; WAL-shaped serialize
SYNTAX UNLOCK: `os.Open`/`Create` return `(*File, error)`; always `defer f.Close()`. `bufio.Scanner` / `Writer` for buffered IO. `embed` / `//go:embed` bakes files into the binary (migrations, fixtures). `time.Time`, `time.Duration`, monotonic for deadlines. Binary framing: length-prefix + payload (WAL record shape).
Concept: Mini WAL: append-only records `{lsn, crc, payload}`; crash = truncate to last good CRC; replay rebuilds state. This is the DB-10 toy — Cloud SQL hides WAL; you still implement the shape once.
Python twin first: same codec + crash/replay tests in Python; then Go.
Go artifact: package `waltoy`; tests: `TestAppendReplay`, `TestCorruptTailTruncates`, `TestEmbedFixtureLoads`, `TestBufioRoundTrip`; gate: replay after simulated crash matches pre-crash state; Cloud SQL mapping paragraph written (what `checkpoint`/`pg_waldump` correspond to).

---
### 2.2 GCP relational offerings (decision table)

#### PCA: 2.2 Storage systems (provision)

**Guide themes (matrix):** storage allocation; processing; access; transfer/latency; lifecycle; growth; backup/recovery. Home: Part 2.

| Data | Prefer | Accept |
|---|---|---|
| OLTP orders | Cloud SQL HA / AlloyDB | Spanner if true multi-region SQL |
| Objects/media | GCS classes + lifecycle | Filestore if POSIX |
| Hot telemetry | Bigtable | SQL only if volume tiny |
| Warehouse | BigQuery | Dataproc if Hadoop lift |

**Scenario prompt:** Media library grows 40%/year; cold assets rarely read; analytics on views needed.

**Expected answer shape:** “I pick GCS Autoclass/lifecycle + BigQuery because Y, I accept Z (no Filestore; restore tested quarterly).”


| Offering | Model | You pick it when |
|---|---|---|
| **Cloud SQL** (MySQL, PostgreSQL, SQL Server) | Regional managed RDBMS | Standard OLTP, extensions, lift-and-shift |
| **AlloyDB** | PostgreSQL-compatible + columnar | High-performance Postgres, HTAP |
| **Spanner** | Globally consistent relational | Multi-region strong SQL, horizontal write scale |
| **BigQuery** | Serverless warehouse | Analytics, not checkout transactions |
| **Firestore** | Document | Flexible docs, mobile/offline, free-tier system |
| **Bigtable** | Wide-column | Time series, huge sequential writes |
| **Memorystore** | Redis/Memcached | Cache, sessions, not source of truth |

**ADR-002:** Northstar OLTP = Cloud SQL PostgreSQL. Firestore remains for session/cart cache and free-tier live demos. Analytics events → Pub/Sub → BigQuery.

### 2.3 How to set up Cloud SQL on GCP (required procedure)

You will write and understand every step even if you apply it against trial credits once, then destroy.

Provisioning:
- Instance: PostgreSQL version, region/zone, machine tier (`db-f1-micro` is cheapest for a credits demo; not HA).
- Storage: SSD vs HDD, autogrow, PITR / backups / retained backups.
- HA (regional): primary + standby, failover, RTO implications, cost ≈ 2×.
- Read replicas, maintenance window, flags (`max_connections`, `work_mem`).
- Deletion protection.

Connectivity (the part people get wrong):
- Public IP + authorized networks — **rejected for production**.
- **Private IP** in a VPC; Cloud Run / GCE / GKE reach it via Direct VPC egress or Serverless VPC Access (legacy) or private path.
- **Cloud SQL Auth Proxy** / Cloud SQL Language Connectors (Python/Go connectors) — IAM auth, no stored DB password in env if possible.
- SSL/TLS required; `sslmode=require` or `verify-ca`.
- IAM database authentication vs built-in users.

Security:
- Dedicated SA. Secret Manager for the initial password if used.
- Authorized networks empty. No `0.0.0.0/0`.
- CMEK optional. Automated backups encrypted.
- Audit: Cloud SQL Admin audit logs + `pgAudit` (Postgres).

Ops:
- Import/export to GCS. Major version upgrade path.
- Query Insights, slow query log.
- Connection pooling: **AlloyDB Auth Proxy** / **Cloud SQL Auth Proxy** + **PgBouncer** or application pool; Cloud Run concurrency vs `max_connections` math.
- **Lab (required, local):** Auth Proxy against Docker Postgres simulating the connector flow; connection-pool math exercise.
- **Lab (credits-optional, then destroy same day):** `terraform apply` Cloud SQL PostgreSQL private IP + Auth Proxy from a GCE e2-micro or Cloud Run with Direct VPC; run migrations; take a backup; failover if HA; `terraform destroy`.
- **Python / Go:** Cloud SQL Python Connector / Go connector; migrate the Part 2.1 repository from DSN-in-env to IAM auth.

**Terraform LLD (required deliverable):** `google_sql_database_instance`, `google_sql_database`, `google_sql_user`, private service access (`google_service_networking_connection`), deletion protection, backup configuration, insights config.

### 2.4 Firestore (still live on free tier)

Firestore Native mode is the free-tier document SoR for Northstar v0 carts/sessions when Cloud SQL is not yet live. Always Free (verify live [free-cloud-features](https://cloud.google.com/free/docs/free-cloud-features)): **1 GiB** storage/project, **50k reads / 20k writes / 20k deletes** per day, **10 GiB**/mo outbound. One free-tier database per project.

#### Concepts
- **Document model:** collections → documents → fields; nested maps/arrays; document ID is the primary key. Subcollections for 1:N that you query independently (cart lines under `carts/{id}/lines`).
- **Queries:** equality + inequality on one field family; composite indexes required for multi-field filters/orderBy — missing index fails with a console link (lab must create it, not ignore).
- **Transactions & batched writes:** all-or-nothing across docs in one DB; contention retries. Do not pretend multi-doc without a transaction when invariants span docs.
- **Consistency:** strong for single-document reads; queries are strongly consistent in Native mode for documents that match — still not a SQL join engine.
- **Security rules vs server-only:** browser/mobile clients use rules; Cloud Run uses Admin SDK and **must not** rely on rules for authorization — you enforce tenant/RBAC in the app (Part 4). Prefer server-only for money-adjacent paths.
- **Datastore mode:** same storage engine, different API; Northstar uses **Native** unless a migration constraint forces Datastore mode.
- **Dual-write period:** cart in Firestore, orders in SQL — or SQL-only after 2.3. Dual-write without an outbox is forbidden (3.5).

#### From scratch (required)
- In-memory document store: `put(path, doc)`, `get`, `query(eq filters)`, optimistic concurrency via `etag`/`update_time`. Table tests: missing doc, concurrent update conflict, batch abort.
- Repository interface `CartRepository` with methods used by the use case; two adapters later (Firestore, Postgres). Use-case tests run against the in-memory adapter only.

#### Lab (free-tier boxed)
1. Create Native mode DB in a free-tier region; enable API.
2. Model `tenants/{tid}/carts/{cid}` + line subcollection; composite index for `status + updated_at`.
3. Cloud Run (or local emulator) Admin SDK write/read; prove a rules-denied client path if you open a client SDK at all.
4. Emulator for CI: `firestore-emulator` in docker-compose; same repository tests.
5. **Python then Go:** `google-cloud-firestore` / Go client; destroy test docs daily so you stay under free ops.

#### Gate
- Interface tests green on memory + emulator; composite index checked in; ADR states when Firestore stops being SoR for orders; no client SDK write path for checkout.

#### Decision table
| Need | Pick | Accept |
|---|---|---|
| v0 cart / session, free tier | Firestore Native | Query limits; not SQL joins |
| Orders / money state | Cloud SQL (2.3) | Ops cost vs free Firestore |
| Global strong SQL | Spanner (2.7) | Cost; not Always Free long-term |
| Realtime mobile sync only | Firestore listeners | Not Northstar checkout SoR |
### 2.5 Cloud Storage (full offering — video block)

Object storage for product images, exports, billing dumps, and migration landings. Always Free (US regional only — `us-central1` / `us-east1` / `us-west1`): **5 GB-months** Standard, **5k Class A** / **50k Class B** ops, **100 GB** NA egress (combined across those regions). Prefer those regions for labs.

#### Concepts
- **Buckets & objects:** flat namespace with `/`-shaped names; object = data + metadata + generation.
- **Storage classes:** Standard, Nearline, Coldline, Archive; **Autoclass** when access patterns unknown. Regional vs dual-region vs multi-region — residency vs availability.
- **Lifecycle:** age-based transition/delete; abort incomplete multipart; matches cost model in 10.3.
- **Versioning, retention, holds:** versioning for recover-from-overwrite; retention/bucket lock for compliance (know before enabling — hard to undo).
- **Access:** **uniform bucket-level access** (default you use) — IAM only, no object ACLs. Public prevention org policy. Signed URLs (V4) for time-limited upload/download; signed POST policies for browser uploads. HMAC keys are legacy — avoid for new Northstar paths.
- **Encryption:** Google-managed default; CMEK via Cloud KMS; CSEK rare. Requester pays for shared scientific buckets — not Northstar default.
- **Transfer:** `gcloud storage` / Storage Transfer Service; Transfer Appliance is literacy only.

#### From scratch (required)
- Local “object store”: content-addressed files under a root; metadata JSON; generate a HMAC-like signature over `METHOD\\nEXPIRES\\n/path` for a toy signed GET (stdlib `hmac`). Tests: expired sig fails; wrong path fails; happy path streams bytes.
- Name the production substitute: Cloud Storage V4 signed URLs + IAM — your toy is not AWS SigV4 compatible and must not ship.

#### Lab (free-tier boxed)
1. Bucket in `us-central1`, uniform access, public access prevention, versioning on.
2. Lifecycle: transition to Nearline after 30 days (or Autoclass); noncurrent version delete after N days.
3. Product-image upload via **V4 signed URL** from Cloud Run; object never world-writable.
4. IAM: uploader SA `objectCreator` on prefix; reader SA `objectViewer` on prefix — no `allUsers`.
5. **Python / Go:** sign V4 URLs; upload/download; list + lifecycle get for the cost report.

#### Gate
- Signed upload works; public list fails; teardown deletes objects + bucket (or empty for reuse); ADR: CDN in front for public catalog images only via LB/CDN, not raw public ACLs.

#### Decision table
| Need | Pick | Accept |
|---|---|---|
| Product images, free tier | Standard regional US + signed URL | Class A op budget |
| Cold exports / backups | Nearline/Coldline + lifecycle | Restore latency |
| Global static via CDN | Backend bucket + Cloud CDN | Extra LB/CDN SKUs |
| Shared scientific egress | Requester pays | Ops complexity |
### 2.7 Spanner and NoSQL map (PCA storage types)

PCA storage-type fluency: pick the data plane from access pattern, consistency, and geography — not from familiarity. This section is the **map**; Cloud SQL procedure stays 2.3; Firestore depth 2.4; Memorystore product depth 9.1; BigQuery ops 9.4 / 9b.1.

#### Concepts
- **Cloud Spanner:** externally consistent global relational; TrueTime; interleaved tables for locality; secondary indexes; query via SQL. Pick when multi-region strong consistency + horizontal scale beats Cloud SQL HA. Failure modes: treating it as “free Postgres”; hot interleaved roots; cross-DB joins in app.
- **Firestore / Datastore mode:** document/KV (2.4). Realtime Database (Firebase) — mobile sync legacy; **not** Northstar OLTP.
- **Bigtable:** wide-column; row-key design is the schema; time-series and high QPS telemetry win; not ad-hoc SQL.
- **Memorystore (Redis/Memcached):** cache and ephemeral structures — **never** system of record for money or orders.
- **Filestore:** NFS; GKE RWX shared files; not object storage and not a database.
- **BigQuery:** analytical warehouse (9b.1) — not OLTP. Export orders here; do not serve checkout from BQ.

#### From scratch (required)
- Row-key sketch exercise: design keys for `(tenant, sku, ts)` event log that avoids hotspotting (reverse ts or hash prefix). Unit-test a partitioner that spreads writes.
- Interleaving sketch on paper: `Orders` parent → `OrderLines` interleaved; justify locality vs secondary index alone.
- Name substitutes: Spanner emulator ≈ your multi-row txn tests; Redis docker ≈ Memorystore; GCS ≠ Filestore.

#### Lab (free-tier / trial boxed)
1. **Spanner emulator** (PCA 5.2 tooling): two-table interleaved schema; read-write txn; no live Spanner required for the gate.
2. Optional: Spanner **90-day free trial** instance (10 GB) — create, run the same schema, **delete before idle billing surprises** after trial rules.
3. Bigtable: key-design ADR only unless credits; do not leave a production cluster up.
4. **Python / Go:** same `OrderRepository` interface; optional Spanner emulator adapter behind the interface.

#### Gate
- Decision table memorized; emulator txn test green; ADR: orders stay Cloud SQL until a named multi-region/scale force; Memorystore never SoR in threat model.

#### Decision table (PCA)
| Access / constraint | Prefer | Avoid |
|---|---|---|
| Relational OLTP, one region | Cloud SQL HA | Spanner “because cool” |
| Multi-region strong SQL | Spanner | Dual-write two Cloud SQLs |
| Mobile/offline documents | Firestore | Spanner for chatty docs |
| Time-series high write | Bigtable | Firestore mega-documents |
| Sub-ms cache | Memorystore | Cache as ledger |
| Shared GKE files | Filestore | GCS FUSE as database |
| Analytics / OLAP | BigQuery | OLTP queries on BQ |
### 2.6 Config, migrations, jobs

Schema and batch work must not ride user requests. Migrations and reports are **jobs** with identity, timeouts, and idempotency.

#### Concepts
- **Cloud Run Jobs:** run-to-completion tasks (migrate, backfill, report). One SA, bounded retries, task timeout. Distinct from request-serving Cloud Run services.
- **Cloud Scheduler:** 3 Always Free jobs — cron trigger to Jobs, Pub/Sub, or OIDC HTTP. Retry config ≠ handler idempotency (both required; see 3.4).
- **Migration discipline:** expand/contract; versioned DDL; never `migrate` on every container start in prod; lock/advisory so two Jobs do not race.
- **Config:** env for non-secrets; Secret Manager for secrets; config connectors / runtime flags with defaults tested.

#### From scratch (required)
- Local migrator: ordered SQL (or SQLite) files `001_….sql`; `schema_migrations` table; `up`/`down`; refuse dirty version. Tests: double-up no-op; failed mid-file leaves dirty and blocks.
- WAL-shaped serialize/deserialize (**G4** feed): append migration audit events to a file log; replay — ties Pedagogy KV/WAL toy to DB-10 literacy.

#### Lab (free-tier boxed)
1. Package migrations (Alembic or golang-migrate); run **locally** against Docker Postgres as default.
2. Define a Cloud Run Job manifest that runs `migrate up`; Scheduler OIDC to a `/internal/migrate` **only in nonprod** or prefer Job execute API — no public migrate URL.
3. One Scheduler job → Cloud Run Job for nightly report stub; destroy extras to stay ≤3 free jobs.
4. **Python:** Alembic upgrade as Job entrypoint. **Go:** golang-migrate Job. File I/O + WAL audit (**G4**).

#### Gate
- `migrate up/down` tested; Job SA cannot invoke the public API SA; Scheduler job count documented; checkout path does not open DDL connections.

#### Decision table
| Work | Prefer | Avoid |
|---|---|---|
| DDL / backfill | Cloud Run Job | Migrate in HTTP request |
| Nightly report | Scheduler → Job | Long request on Cloud Run service |
| Secret rotation hook | Job + Secret Manager versions | Bake secrets in image |
## Part 3 — Microservices (industry)

SOLID, hexagonal, DDD, gRPC, and the pattern catalog live **here only**. Later parts link back. Do not re-teach them in Part 8.

### 3.0 Software design (before you split)

Northstar is still a modular monolith. You impose structure so the later split is a cut, not a rewrite.

#### SOLID (tests fail if you violate)
| | Rule in this repo |
|---|---|
| S | HTTP handler, `PlaceOrder` use case, and `OrderRepository` are three modules. A PR that mixes them is rejected. |
| O | New PSP = new `PaymentPort` adapter, not another `if provider ==`. |
| L | `InMemoryOrderRepo` substitutes for Postgres in tests with zero use-case edits. |
| I | Small ports: `OrderWriter`, `CatalogReader` — no 40-method god interface. |
| D | `domain/` and `app/` **must not** import `google.cloud`, `psycopg`, FastAPI. CI grep / import-linter. |

#### Hexagonal / Clean / Onion
Dependency rule inward. Layout: `domain/`, `app/` (use cases), `ports/`, `adapters/http|grpc|sql|pubsub`. Driving vs driven adapters. Catalog may stay layered CRUD; **order/payment is hexagonal**. Go: interfaces as ports (**G3**).

#### DDD tactical
Order aggregate; line items don’t leak; `OrderPlaced` domain event; Pub/Sub carries integration event. Stripe/Identity Platform behind ACL. Anemic model only as honest transaction script.

#### CQRS / patterns
Two *queries* before two databases. Event-source checkout only if audit/replay defended; default outbox (3.5). Patterns only when the force is in the code (list unchanged from prior curriculum).

#### Evidence pack (every HLD/LLD lab)
Functional + quality requirements; assets, actors, trust boundaries, abuse cases, authorization model; capacity estimate; Mermaid HLD; LLD/API/schema/state diagrams; bottleneck/failure/security table; trade-off table; implementation (Python then Go); positive/negative/load/adversarial tests; observability with secret redaction; rollback/revocation/recovery; one ADR. Authenticating without authorizing **action and object** is incomplete.

#### S20 teaching order (do not skip) — with worked `PlaceOrder`
1. **Quality attributes / SLOs** — PlaceOrder success rate, p95 place latency, oversell = 0.
2. **Boundaries / data ownership** — Order aggregate owns lines; catalog is read model for pricing snapshot at place time.
3. **LLD contracts / cohesion** — `PlaceOrder(cmd) -> Result`; HTTP DTO ≠ domain.
4. **SOLID in code** — three modules; CI import lint.
5. **Clean + DDD** — aggregate invariants: non-empty lines, positive qty, idempotency key required.
6. **Modular monolith** — same process, separate packages; no network yet.
7. **Sync vs async** — sync: reserve stock + persist order; async: `OrderPlaced` → email/Tasks.
8. **Retries / timeouts / idempotency / backpressure** — client idempotency key; server UNIQUE; timeout on payment port.
9. **Cache / queue semantics** — do not cache “placed” without invalidation story; queue at-least-once ⇒ inbox.
10. **Replication / partition / consistency** — read-your-writes on order get; catalog replica lag OK for browse.
11. **Leader / consensus as needed** — skip for PlaceOrder v0; name when stock ledger becomes distributed.
12. **Transactions / outbox / saga** — single DB txn: insert order + outbox row; publisher drains outbox.
13. **Observability** — span `PlaceOrder`; metrics `orders_placed`, `orders_rejected_idempotency`.
14. **Split microservice only when justified** — extract payment adapter first only if deploy cadence forces it.

#### Worked PlaceOrder example (evidence-pack miniature)
**Command:** `{idempotency_key, tenant_id, customer_id, lines[{sku, qty}]}`.
**Happy path:** load catalog prices → validate stock → insert `orders` + `order_lines` + `outbox` in one txn → return `order_id` + `created`.
**Idempotent replay:** same key → return original `order_id` without double stock decrement (UNIQUE + fetch).
**Failure:** payment port timeout → order stays `pending_payment` / compensating path per ADR — never silent success.
**Tests:** concurrent duplicate keys; oversell race; use-case without DB driver import; Go port interfaces (**G3**).
**ADR one-liner:** “I pick modular monolith + outbox because Y (one txn boundary), I accept Z (async consumers must be idempotent).”

#### From scratch
`PlaceOrder` with in-memory adapter tests, then Postgres adapter. Use case file cannot import the DB driver.

#### Go G3 — pointers, structs, methods, interfaces, generics; lists/heap/hash
SYNTAX UNLOCK: `*T` / `&x` — pointer is an address; method receivers `(s *Service)` vs `(s Service)` (pointer when mutating or avoiding large copies). Interfaces: method sets; `var p Port = &Adapter{}` — **nil concrete in non-nil interface** is the classic trap (`var a *Adapter; var p Port = a; p != nil` is true). Generics: `func Keys[K comparable, V any](m map[K]V) []K`. Contrast Python: duck typing + protocols; Go interfaces are checked at compile time.
Concept: Hexagonal ports are interfaces; adapters are structs with methods. Domain types are structs with invariants enforced in constructors. Nil-interface tests are mandatory. Small ports (`OrderWriter`) beat god interfaces.
Python twin first: Protocol/`abc` ports + in-memory adapter for `PlaceOrder`; CI import-linter forbids domain→driver imports.
Go artifact: package `orderport` (interfaces) + `orderapp` + `adapters/memory`; tests: `TestNilInterfaceTrap`, `TestInMemorySatisfiesPort`, `TestPlaceOrderNoDriverImport` (analysis or build-tag grep); gate: use-case tests pass with memory adapter only; Postgres adapter later does not change `orderapp`.

---
### 3.1 When to split

Northstar stays a **modular monolith** until a force appears. Splitting early creates a distributed monolith (latency, failure, and version skew without team boundaries).

#### Concepts
- **Forces that justify a split:** independent deploy cadence; independent scale axis; failure isolation (payment outage must not take down browse); data ownership / compliance boundary; team Conway boundary with clear contracts.
- **Split on bounded contexts (3.0):** catalog, cart, order, payment, notification — not on every noun.
- **Strangler fig:** extract the edge with the clearest contract first (often catalog read), never payment first.
- **Sync vs async after split:** user-click path stays sync and short; side effects async (3.4–3.5).
- **Anti-patterns:** shared DB across “services”; nano-services; 2PC across services; chatty HTTP joins for one page; rewriting before measuring.

#### From scratch (required)
- Package graph: modules `catalog`, `order`, `payment` with **import-linter** / CI grep forbidding `payment` → `catalog` UI types. Prove you can extract `catalog` behind an interface without changing `PlaceOrder` tests.
- Write a one-page “split scorecard” for Northstar: score each force 0–2; split only if total ≥ threshold you set in an ADR.

#### Lab / HLD
- HLD: current modular monolith + dashed “future payment service” with sequence for sync place-order vs async notify.
- Pattern catalog (one table, GCP mapping):

| Pattern | Northstar | GCP |
|---|---|---|
| Database per service | Own schema/collection | Cloud SQL db or Firestore |
| Saga choreography / orchestration | `OrderPlaced` → pay → stock | Pub/Sub; Workflows if orchestrator |
| Outbox | Commit event with order row | SQL + publisher job |
| Inbox | Consumer idempotency store | Firestore/SQL unique key |
| BFF / aggregator | Storefront API | Cloud Run in front of gRPC |
| API Gateway | JWT, quota | API Gateway; Apigee if API-as-product |
| Bulkhead | Isolate payment client pool | process-level; mesh later |
| Sidecar / ACL | Stripe client | library first; mesh only at GKE scale |

**Review fails:** shared DB, distributed monolith (8 sync hops per click), nano-services, 2PC, chatty HTTP joins.

#### Gate
- Scorecard + ADR “we do not split yet” or “we extract X because force Y”; import boundaries enforced in CI; no shared mutable tables across proposed services.

#### Decision table
| Signal | Action | Accept |
|---|---|---|
| One team, one DB, fine deploys | Stay modular monolith | Less independent scale |
| Payment PCI / deploy cadence | Extract payment ACL service | Saga/outbox mandatory |
| Catalog read 10× write | Extract catalog read service | Cache invalidation story |
### 3.2 Service-to-service + gRPC + protobuf

#### Concepts
- Public browser API stays **JSON/HTTP**. Internal: **gRPC/HTTP/2** on Cloud Run.
- Auth: `roles/run.invoker` + **Google ID tokens** (audience = receiving service URL); service bindings as direction of travel.
- Timeouts, retries with jitter, circuit breaker — **your** client middleware (3.0), not an unread library.
- HTTP/2 HOL taught in Part 6.1; here map gRPC framing only.

#### Protobuf
- **From scratch:** encode/decode `{id, name, price_cents}` (varint, wire type 2). Golden vs `protoc`. Field numbers never reused; `reserved` deleted fields.

**Protobuf wire (complete here):** key = `(field_number << 3) | wire_type`; wire types 0 (varint), 1 (64-bit), 2 (length-delimited), 5 (32-bit). Varint: 7-bit groups, MSB continuation. Length-delimited: varint length + bytes (string/bytes/embedded message/packed). Golden vectors for field 1 varint, field 2 string, field 3 packed repeated — compare to `protoc --encode`. Compatibility: never reuse field numbers; reserve deleted; default zeros. (**G13–G15** artifact uses this.)

- Official runtime after golden. Same `.proto` → Python then Go (**G13**).

#### gRPC mapping
- `POST /package.Service/Method`, `application/grpc`, 5-byte prefix (compressed flag + length) + protobuf.
- Unary + server-stream toy over HTTP/1 if needed; all four RPC types with `grpcio` / `google.golang.org/grpc` (**G14**).

#### Interceptors (middleware)
- Unary/stream interceptors: auth (ID token / SA), log, deadline, metrics (**G15**).
- Status codes mapped to problem decisions; health `grpc.health.v1`; reflection **off** in prod.

#### Cloud Run + ID tokens (procedure)
1. Deploy catalog gRPC service; require authentication; grant caller SA `roles/run.invoker`.
2. Client: `idtoken.NewClient(ctx, audience)` (Go) / `google.oauth2.id_token` (Python) with audience = service URL.
3. Reject wrong audience; no `allUsers` invoker in prod.
4. BFF REST on Cloud Run calls `catalog.v1.CatalogService`; N+1 is a fail — batch or stream.

#### Lab
GetProduct gRPC on Cloud Run; BFF REST in front. Python / Go ID-token client + generated stub. Paste **G13–G15** and **G6–G7** (ctx cancel on retries) lesson text under this heading.

#### Gate
Same proto both languages; invoker IAM proven; interceptors tested; reflection disabled in prod config.

#### Go G6 — goroutines, channels, select
SYNTAX UNLOCK: `go f()` starts a goroutine (cheap OS-multiplexed thread). Channels: `ch := make(chan T, n)`; send `ch <- v`; receive `v := <-ch`; close to signal end. `select` waits on multiple channel ops (incl. `default` for non-block). Contrast Python: `asyncio` tasks / threads — Go shares memory by communicating (prefer channels for ownership transfer; mutex when sharing).
Concept: Never start a goroutine without a stop signal (next unlock: context). Race on shared maps without sync is undefined — race detector is mandatory later (G7). Used in gRPC client pools, Pub/Sub pull loops, HTTP middleware shared limiter.
Python twin first: asyncio or threading twin of the fan-in pattern with explicit shutdown.
Go artifact: package `conc/fanin`; tests: `TestFanInAllReceived`, `TestSelectDefaultNonBlock`, `TestNoLeakAfterCancel` (with G7 context); gate: `go test -race` passes on this package.

---

#### Go G7 — context, mutex, race detector
SYNTAX UNLOCK: `context.Context` carries deadline/cancel/values; `ctx, cancel := context.WithTimeout(parent, d); defer cancel()`. APIs take `ctx` as first arg. `sync.Mutex` / `RWMutex`: `Lock`/`Unlock` (defer Unlock). `go test -race` instruments shared memory. Contrast Python: no stdlib cancel token as universal; `threading.Lock` analogous.
Concept: Cancelled context must stop work (HTTP client, gRPC, DB queries, task handlers). Shared rate limiter / session store in 4.2 is race-tested. Pub/Sub ack extensions respect ctx.
Python twin first: timeout/cancel around HTTP client + lock around shared counter.
Go artifact: package `conc/limit` (shared limiter used by 4.2) + ctx helpers; tests: `TestCancelledContextStopsWork`, `TestMutexProtectsCounter` under `-race`, `TestLimiterRace`; gate: `go test -race ./...` green for HTTP middleware + async handlers that share state.

---

#### Go G13 — protobuf messages and compatibility
SYNTAX UNLOCK: `.proto` → `protoc-gen-go`; generated structs; `proto.Marshal`/`Unmarshal`. Field numbers are forever. `optional` / presence. Contrast Python: `protobuf` / betterproto — same `.proto` file.
Concept: Encode/decode golden vectors from the from-scratch varint lab. Never reuse field numbers; reserved deleted fields. Same catalog message as the Python twin.
Python twin first: golden encode/decode vs hand-rolled varint; then official runtime; then Go stubs from **same** `.proto`.
Go artifact: package `gen/catalog/v1` (generated) + `catalogcodec` tests; tests: `TestGoldenWireCompatWithPython`, `TestUnknownFieldPreserved`, `TestReservedNumberRejectedInCI`; gate: CI compiles both language stubs from one proto; compatibility doc checked in.

---

#### Go G14 — gRPC unary and streams
SYNTAX UNLOCK: `grpc.NewServer()`; register generated service; `grpc.DialContext` + credentials. Four RPC shapes: unary, server-stream, client-stream, bidi. Contrast Python: `grpcio` async/sync.
Concept: Map to HTTP/2 `POST /package.Service/Method`. Cloud Run hosts gRPC. BFF REST calls catalog gRPC — N+1 is a fail (batch or stream).
Python twin first: unary + server-stream GetProduct(s); then Go.
Go artifact: package `catalogrpc`; tests: `TestUnaryGetProduct`, `TestServerStreamBatch`, `TestDeadlineExceeded`; gate: all four RPC types exercised in tests (bidi can be toy); same proto as G13.

---

#### Go G15 — interceptors, Cloud Run, ID tokens
SYNTAX UNLOCK: `grpc.UnaryInterceptor` / `StreamInterceptor` — middleware for gRPC. Google ID token audience = Cloud Run URL; `idtoken.NewClient(ctx, audience)`. Contrast Python: interceptors + `google.oauth2.id_token`.
Concept: Auth, log, deadline interceptors. `roles/run.invoker` on caller SA. Reflection off in prod. Health `grpc.health.v1`. Retries honor `context` (G7).
Python twin first: ID-token client to Cloud Run gRPC; then Go.
Go artifact: package `catalogrpc/interceptors` + `cmd/catalogd`; tests: `TestAuthInterceptorRejectsMissing`, `TestIDTokenAudience`, `TestHealthCheck`; gate: GetProduct on Cloud Run with invoker IAM; BFF REST in front; no public-unauthenticated gRPC in prod config.

---
### 3.3 API facade

The facade is where public clients meet Northstar: authn hints, quotas, routing, and OpenAPI — not where business invariants live (those stay in use cases).

#### Concepts
- **URL map on HTTPS LB:** Host/path routing to backend services / serverless NEGs. Cheap edge routing; limited API-product features.
- **API Gateway:** OpenAPI-defined; API keys, JWT validation, quotas, per-method config; cheap for Northstar-shaped public APIs. Free call tier exists — stay inside it for labs.
- **Apigee:** API-as-product (monetization, portals, complex policies, hybrid). Overkill until APIs are sold or partner-facing at scale.
- **Cloud Endpoints / ESPv2:** sidecar or Cloud Run ESP; literacy for GKE; prefer Gateway or LB+Run for new Northstar work.
- **BFF:** storefront-specific aggregation on Cloud Run in front of internal gRPC (3.2) — still app code, not Apigee.

#### From scratch (required)
- Tiny reverse-proxy facade: path prefix → upstream base URL; inject `X-Request-Id`; reject unknown paths with 404; optional static API-key header check against an allowlist file. Tests: routing table, missing key, upstream 5xx mapped to 502 without leaking upstream body secrets.
- OpenAPI subset: document two paths; contract test that the facade only forwards documented operations.

#### Lab (free-tier boxed)
1. OpenAPI 3 spec for catalog + orders read; deploy **API Gateway** in front of two Cloud Run services (or mock upstreams).
2. API key restricted by referrer/IP where applicable; quota small enough to hit in a test.
3. **ADR-003:** API Gateway or Cloud Run ingress for Northstar; Apigee when APIs are a product.
4. **Python:** generate OpenAPI from FastAPI; schemathesis/contract tests. **Go:** chi/stdlib handlers + golden OpenAPI file.

#### Gate
- Spec checked in; gateway config matches spec; undocumented route fails; ADR-003 merged; no business rules only in gateway policies.

#### Decision table
| Need | Prefer | Avoid |
|---|---|---|
| Public REST + JWT/API key + quota | API Gateway | Apigee day one |
| Host/path only to Run | HTTPS LB URL map | Extra product tax |
| Partner monetization / portal | Apigee | Homegrown billing |
| Internal microservice hops | Direct Run IAM / gRPC | Public gateway |
### 3.4 Async: Pub/Sub, Eventarc, Cloud Tasks, Cloud Scheduler

#### From scratch first
- In-memory broker: topic, pull, ack deadline, nack, DLQ after N, at-least-once.
- Delayed queue with lease/heartbeat (= Cloud Tasks shape).
- Loop sleeping until next cron tick + POST (= Scheduler) — then delete it and use the product.

#### Shared semantics
- At-least-once ⇒ **idempotency keys / inbox**. Dead letter topics. Ordering vs throughput trade-off.
- Eventarc Standard: CloudEvents → Cloud Run.
- Cloud Run **Worker Pools** for pull consumers (2026 model).
- OIDC to Cloud Run: Scheduler/Tasks attach tokens; **handler verifies** audience/issuer — do not trust network location.

#### Cloud Scheduler (3 Always Free jobs)
- Targets: HTTP, Pub/Sub, App Engine HTTP. Unix-cron, timezone, attempt deadline.
- **Auth:** OIDC to Cloud Run (`audience` = service URL). No API keys in the job.
- Retry config ≠ “handler is idempotent” — you need **both**.
- **Lab:** (1) OIDC HTTP → `/internal/recompute`, (2) Pub/Sub tick, optional (3) App Engine target on 1.9 service. Destroy extras. Python then Go API create/pause/run.

#### Cloud Tasks
- Queue: `rateLimits` (maxDispatchesPerSecond, maxConcurrentDispatches, maxBurstSize), `retryConfig` (maxAttempts, min/maxBackoff, doublings).
- Task: HTTP (Cloud Run) or App Engine; payload; `scheduleTime`; **name** for dedupe (`ALREADY_EXISTS`).
- OIDC / dispatch token; handler verifies.
- Poison → retry → maxAttempts → DLQ/ops alert. Observability in 10.0.
- **Lab:** enqueue notification tasks; prove poison handling. Python then Go.

#### Pub/Sub
- Fan-out `OrderPlaced`; push vs pull; ack extension; DLQ; ordering keys only when required (throughput cost).
- Exactly-once delivery is not a substitute for inbox at the app layer for money-adjacent side effects.

#### Decision table
| Need | Product |
|---|---|
| Run at 03:00 UTC | Cloud Scheduler |
| Delayed/retried HTTP to **one** worker | Cloud Tasks |
| Fan-out event | Pub/Sub |
| Run-to-completion batch | Cloud Run Jobs (+ Scheduler) |
| Multi-step orchestration | Workflows |
| In-cluster cron | GKE CronJob |
| Legacy GAE | `cron.yaml` / GAE queues — literacy only |

#### Idempotency sequences (required sketch)
1. Scheduler fires twice (retry) → handler checks inbox key `recompute:2026-09-14` → second is no-op.
2. Tasks attempts 1..N on 500 → same task name / business key → single email send.
3. Pub/Sub redelivery → consumer inbox UNIQUE `(subscription, message_id)` or business key.

Paste **G6–G7** under this heading for pull loops / ctx cancel.
### 3.5 Failure design

Partial failure is the default once you have two systems. Dual-write (`sql.commit()` then `pubsub.publish()` without a transactional outbox) is **forbidden**.

#### Concepts
- **Failure modes:** process crash between writes; at-least-once redelivery; timeout with unknown outcome; poison messages; cascading retries (retry storms).
- **Outbox:** same DB transaction inserts business row + outbox row; publisher drains outbox → Pub/Sub; at-least-once to the bus, idempotent consumers.
- **Inbox:** consumer UNIQUE on `(subscription, message_id)` or business key before side effects.
- **Saga:** choreography default (`OrderPlaced` → pay → stock) with compensating `ReleaseStock`; orchestration (Workflows) only if the graph is painful to reason about.
- **DLQ + redrive:** poison → DLQ is not a grave — expose a redrive API/runbook (7.8 / 10.2).
- **Timeouts & bulkheads:** payment client pool isolated; deadlines on every egress (G7).

#### From scratch (required)
- In-process saga + outbox on SQLite (or memory+WAL): `PlaceOrder` writes order+outbox; worker publishes; consumer inbox. Tests: crash after commit before publish (worker recovers); duplicate delivery; compensating path on payment failure.
- Same tests later against SQL + Pub/Sub emulator / free-tier Pub/Sub (10 GiB/mo).

#### HLD + LLD
- Sequence: place order → outbox → `OrderPlaced` → payment stub → stock; failure branches annotated.
- State diagram for order + outbox statuses. Payment becomes Stripe in Part 5 without changing the outbox shape.

#### Lab
- Implement outbox table + publisher Job/service; prove dual-write test **fails** CI if someone calls publish inside the request without outbox.
- Redrive endpoint authenticated (OIDC) for DLQ replay.

#### Gate
- Dual-write grep/lint clean; outbox tests green; compensating path rehearsed; sequence diagram in evidence pack.

#### Decision table
| Situation | Prefer | Avoid |
|---|---|---|
| Commit + notify | Outbox | Dual-write |
| Multi-step business | Choreography + compensate | 2PC across services |
| Complex long graph | Workflows orchestration | Spaghetti sync hops |
| Poison message | DLQ + redrive | Infinite retry |
## Part 4 — Authentication and authorization

**Goal:** Distinguish the four identity planes. Implement customer auth and workload auth correctly.

### 4.1 Identity product map (memorize; PCA loves this)
| Product | Who it authenticates | Use |
|---|---|---|
| Cloud Identity / Workspace | Employees | Directory, groups, org |
| IAM | Anyone accessing GCP resources | Roles on org/folder/project/resource |
| Identity Platform | *Your customers* | Email, social, SAML/OIDC, MFA, multi-tenancy, SLA 99.95%, PCI in scope |
| Firebase Authentication | Same backend, consumer subset | Faster start; no MFA/SAML/multi-tenancy/IAP/BAA |
| IAP | Users hitting an app | IAM in front of Cloud Run/GKE/App Engine; Google or Identity Platform identities |
| Workforce Identity Federation | Employees via external IdP | No Cloud Identity users required |
| Workload Identity Federation | Machines/CI/other clouds | **No service account keys** |
| Managed workload identities | GKE/GCE/agents | SPIFFE / mTLS |

### 4.2 Hardened HTTP and middleware (Go type here; Python twin after)

Build `func(http.Handler) http.Handler`: chaining, short-circuit, typed request context, cancellation, status/byte capture, panic recovery, capability-preserving ResponseWriter. Prove **order** with tests. This **is** G10–G12 HTTP, not a later language unit. Race-test shared limiter/session (**G6–G7**).

Server: explicit `http.Server`; read-header/read/write/idle timeouts; max header/body; no state change on GET/HEAD/OPTIONS; strict JSON (unknown fields / trailing data); 400/401/403/404/405/406/413/415/429/500; generic external errors; no stack traces; graceful shutdown. Sanitize forwarding headers at the trusted-proxy boundary.

Outbound: reusable client/transport; total and phase timeouts; body close; redirect policy; destination allowlist; TLS verify; size limits; bounded concurrency. **SSRF:** parse once; restrict schemes; reject userinfo/fragments when unused; resolve and validate every destination IP; block loopback/private/link-local/multicast/metadata (`169.254.169.254`); DNS rebinding and redirect escape.

Labs: middleware recorder; table-test every short-circuit and order permutation; fuzz headers/paths/JSON/forwarded-host; race-test limiter/session; benchmark rejection paths.


#### Go G11 — middleware chain, REST, status table
SYNTAX UNLOCK: Middleware is `func(http.Handler) http.Handler`. Chain outside-in. Wrap `ResponseWriter` to capture status/bytes without losing `Flush`/`Hijack` when needed. Contrast Python: Starlette middleware stack.
Concept: Prove order with tests (auth before handler; panic recover outermost). Strict JSON; no state change on safe methods; status matrix 400/401/403/404/405/406/413/415/429/500. Same `httpserver` package from G10 — extend, do not fork.
Python twin first: after Go type here (per 4.2 heading) — FastAPI/Starlette twin of the chain order tests.
Go artifact: package `httpserver/middleware`; tests: `TestChainOrder`, `TestShortCircuit401`, `TestStatusTable`, `TestStrictJSONRejectsUnknown`, `TestPanicBecomes500`; gate: table-test every short-circuit; fuzz headers/paths; this + G10 + G12 = one lab evidence pack.

---

#### Go G12 — outbound client, SSRF policy, SQL CRUD wiring
SYNTAX UNLOCK: `http.Client{Timeout, Transport}`; `defer resp.Body.Close()`; custom `DialContext` / IP allowlist for SSRF. `database/sql` with `pgx` driver: `QueryContext(ctx, ...)`. Contrast Python: `httpx` + connectors.
Concept: Reusable transport; destination allowlist; block metadata IP; redirect policy. CRUD handlers use ports from G3; SQL in adapters only. Graphs-as-needed only if a 4.2/Part 2 exercise needs adjacency — do not invent a graph course.
Python twin first: httpx SSRF tests + psycopg CRUD; then Go (Go is typed first for middleware in 4.2; CRUD Python-first still holds per Pedagogy §3 for Part 2).
Go artifact: package `httpserver/client` + `adapters/sql`; tests: `TestSSRFBlocksMetadata`, `TestClientTimeout`, `TestCRUDIdempotentInsert`, `TestContextCancelAbortsQuery`; gate: hardened server timeouts/limits/4xx table complete; race-test limiter (G7); Part 11 matrix checks G10–G12 under **4.2** heading (1.2 shows contract only).

---
### 4.3 Identity, passwords, recovery, MFA
Identity ≠ credentials. Opaque non-sequential public IDs. Email/phone are mutable verified attributes. Equivalent controls on login, register, password change, recovery, admin-assisted recovery, API login, federation.

Passwords: long passphrases, ≥64 chars supported, no silent truncate; min 15 if password-only, ≥8 if MFA; spaces/Unicode with documented normalization; no composition theater or periodic rotation; change on compromise; blocklist common/breached/contextual; allow paste/autofill/managers; no security questions.

Storage: Argon2id, unique random salt, versioned record (alg, version, params, salt, derived); input limits; tune memory/time/parallelism; constant-time compare; upgrade params after login; optional pepper with rotation plan. Never plaintext or reversible; never a fast general hash as KDF. Dummy KDF on unknown users. Generic public errors; equivalent timing. Throttle without cheap lockout. Log events without credentials. Recent-auth for high-risk changes.

Recovery: high-entropy single-use expiring tokens, stored hashed, bound to purpose/account, invalidate after use, rotate sessions after auth/privilege change, notify on another channel. Recovery must not be weaker than what it bypasses.

MFA: recovery codes; TOTP (HMAC, trusted time, replay prevention, rate limits, bounded skew, enrollment confirmation, revocation). Then WebAuthn/passkey via a maintained library (challenge freshness, origin/RP binding, UV flags, counters). SMS/OTP is not phishing-resistant.

### 4.4 Opaque sessions, cookies, CSRF, CORS
≥128 bits randomness; expose only the opaque id; keep identity, assurance, permissions, created/last-active, idle/absolute deadlines, revocation **server-side**. Hash for lookup. Never in query strings.

Cookies: `Secure`, `HttpOnly`, `SameSite=Lax` or `Strict`, host-only, `Path=/`, no extra `Domain`, expiry ≤ server validity. Rotate after login/reauth/privilege change; destroy old state. Idle+absolute expiry; logout; all-session revoke; account-disable revoke; `Cache-Control: no-store` on sensitive responses. No tokens in `localStorage`.

CSRF: no state change on safe methods; synchronizer token or session-bound HMAC double-submit; constant-time compare; never in URLs/logs; Origin/Fetch Metadata. SameSite is defense in depth, not the only control.

CORS: off unless needed; exact origin allowlist; explicit methods/headers; preflight; `Vary: Origin`. Never credentials + `*`. CORS is not authz.

Adversarial tests: fixation, guessing, stale/revoked, privilege-change rotation, logout replay, concurrent renewal, missing/forged CSRF, hostile Origin, cookie attributes.

### 4.5 API keys, signed requests, JWT policy
API keys: crypto random; show once; store hash + lookup prefix; bind owner, purpose, scopes, env, expiry, revocation; overlapping rotation; never in URLs. Identification/metering, not the sole control for high-value user actions.

Signed requests: versioned canonical string (method, target, selected headers, body digest, timestamp, nonce, key id, audience); HMAC; constant-time; clock window; nonce cache; fuzz canonicalization; replay/body/method substitution tests.

JWT: maintained JOSE library for crypto; **you** own policy. Pin alg allowlist; never `none`; no HMAC/RSA key confusion; one alg+purpose per key; validate every signature layer; iss, aud, exp, nbf, iat, typ, jti/replay, max lifetime, skew. Keys only from preconfigured issuers — never attacker `jku`/`kid` as a URL. Separate keys/rules for access vs ID vs refresh vs reset. Signature ≠ current authorization. Rotation, cache refresh, incident cutoff.

Then Cloud Run: Identity Platform / Google ID tokens; reject wrong aud. Multi-tenancy. Blocking functions. **Lab:** email/password + Google sign-in. Python then Go.

### 4.6 OAuth 2.0 / OIDC
OAuth = delegated API access; OIDC = authentication. Access vs refresh vs ID tokens are different artifacts.

Client lab: authorization code + high-entropy `state` + PKCE S256 + OIDC `nonce`; bind to session; exact redirect URIs; issuer mix-up defense; codes over TLS; tokens out of URLs and browser storage; least-privilege scopes; BFF when appropriate.

AS literacy (isolated learning implementation, not a production IdP): exact redirects; one-time short-lived codes; mandatory PKCE S256; no implicit, no password grant; refresh rotation / family revoke; 303 not 307 after credential POST.

Resource server: type, iss, aud, lifetime, signature, scope, resource/action, subject vs client. Reject tokens meant for another service.

OIDC RP: discovery only from a preconfigured issuer; exact metadata issuer; ID Token sig, iss, aud, exp, nonce, sub. Namespace by issuer+sub. Access token is not “user is present.”

Identity Platform is the production substitute after these labs.

### 4.7 Authorization (app + GCP)


#### Concept
**Deny by default.** Authorization is **server-side** — never trust the client’s claimed role. Decision matrix: **subject × action × resource × field × tenant × workflow state**. Progression you implement in order: (1) **RBAC** with explicit permissions (not scattered role-name strings in handlers); (2) **object ownership / IDOR** — guessable ids must not cross tenants; (3) **field-level** (hide `cost`, PII); (4) **tenant isolation** in queries, cache keys, jobs, exports, logs, admin paths; (5) **ABAC** (attributes: plan tier, region); (6) **ReBAC** (relationship: “editor of store X”); (7) **PDP vs PEP** — policy decision point vs enforcement point; policy versioning and cache invalidation when roles change. AuthN (who) is 4.3–4.6; AuthZ (what) is here — do not conflate “valid JWT” with “may refund order.”

#### From scratch / exercise
Middleware shape: authenticate → load principal (roles/attrs/tenant) → **authorize(action, resource)** before handler body. Table-drive tests: allow; deny; missing policy; stale role/token; confused deputy; guessed ids; batch endpoints; overposting; cross-tenant cache leak; admin separation; policy-store failure (fail closed). **Python then Go** same matrix.

#### HLD / LLD
**HLD:** PEP on every Northstar API edge; optional central PDP later; GCP **IAM** for cloud resources (SA roles); **IAP** for admin UI; context-aware access literacy for corp users.
**LLD:** Permission constants; resource id + tenant id in every query; never `WHERE id=?` without tenant; cache key includes tenant; admin paths require separate role + IAP.

#### Free-tier lab note
App AuthZ is free (your code). IAM/IAP use existing project; IAP behind HTTPS LB is **credits-optional** — paper IAP + prove app-level deny tests on Cloud Run without IAP if needed.

#### Gate
IDOR test fails then passes with tenant scope. Deny-by-default on unknown action. IAM vs app AuthZ boundary stated in one ADR sentence. **Python / Go:** authenticate → load principal → authorize action on resource — green tests for allow and deny.

### 4.8 Workload auth

Humans use Identity Platform / IAP (4.x). Workloads use **service accounts**, short-lived tokens, and federation — not JSON keys in GitHub secrets.

#### Concepts
- **Attached SA:** Cloud Run / GCE / GKE Workload Identity bind a runtime SA; ADC finds credentials. Prefer user-managed SAs per service over the Compute default SA.
- **Impersonation:** `roles/iam.serviceAccountTokenCreator` on a break-glass or CI pattern — audited, time-bounded.
- **Workload Identity Federation (WIF):** GitHub Actions (or GitLab) OIDC → Google STS → SA impersonation. Attribute conditions pin `repository`, `ref`, etc.
- **Org policy:** `iam.disableServiceAccountKeyCreation` — user-managed keys off by default for landing zones.
- **Tokens:** ID tokens for `roles/run.invoker` audience = receiving URL (3.2); access tokens for Google APIs. Never log tokens.

#### From scratch (required)
- Mock OIDC: local JWT with `iss`/`aud`/`sub` claims; verifier allowlists issuer + audience + subject pattern (repo name). Tests: wrong aud fails; expired fails; right claims pass. This is the shape of WIF attribute checks — not a replacement for Google STS.

#### Lab (free-tier boxed)
1. Create deploy SA; grant `run.admin` / Artifact Registry writer **on the project or resources**, not Owner.
2. Configure GitHub WIF pool/provider + attribute condition `assertion.repository == 'org/northstar'`.
3. Actions workflow: authenticate via WIF; deploy Cloud Run; **prove no `*.json` key in repo or secrets**.
4. Negative test: wrong repo claim cannot impersonate.
5. **Python / Go:** use ADC in Cloud Run; ID-token client to sibling service.

#### Gate
- Key creation blocked or unused; WIF deploy green; audit log shows federated principal; runbook for leaked key (7.8) still exists for legacy exceptions.

#### Decision table
| Caller | Prefer | Avoid |
|---|---|---|
| Cloud Run → GCP API | Attached SA + ADC | Downloaded key on disk |
| GitHub Actions → deploy | WIF | SA JSON in Actions secrets |
| Break-glass human | Impersonate + audit | Standing Owner keys |
| Local dev | User ADC / impersonate | Commit keys |
### 4.9 Application, secrets, supply chain, assurance
Allowlist validation; parameterized SQL; context-aware encoding; path containment; zip/file limits. Secrets: inventory, no secrets in source/images/logs/traces/prompts; Secret Manager; overlapping rotation; emergency revoke. TLS 1.2+; verify hostnames. Security logs: when/where/who/what/object/outcome/reason/trace id — never passwords, keys, raw session ids, tokens.

**Assurance ladder (learning gates, not a certificate):**
| Level | Implementation | Evidence |
|---|---|---|
| L1 | Hardened server + chain; Argon2id; register/login/change/reset; opaque sessions; CSRF/CORS; RBAC+object; input limits | Threat model, negative authz matrix, no-secret logs, timeouts |
| L2 | MFA/recovery; session mgmt; OIDC client; JWT RS; ABAC/tenant/field; secrets rotation; SSRF policy | Fuzz, race, rotation drills, multi-tenant suite, runbooks |
| L3 | WebAuthn or mTLS study; step-up; hardened admin plane | Independent review, revoke exercise, residual-risk memo |

Integrated project: multi-tenant service with public, user, operator, and s2s paths; then **replace** the learning IdP with Identity Platform while keeping learner-owned interfaces and contract tests.

### 4.10 API abuse (GCP)

Abuse controls sit at the edge and at the app: bots, credential stuffing, scraping, and expensive API fan-out.

#### Concepts
- **reCAPTCHA Enterprise:** Always Free **10k assessments/month**. Score/token verify on signup, login, checkout start — server-side verify, never trust the browser alone.
- **Gateway / Armor quotas:** API Gateway quotas (3.3); Cloud Armor rate-based bans / throttles on LB; app token-bucket still required for fine-grained per-tenant limits (4.2).
- **App Check (Firebase):** later literacy for mobile/web attestation — not a substitute for server authz.
- **Identity-aware signals:** step-up MFA on risky login (4.3); block disposable email domains as policy, not as sole control.

#### From scratch (required)
- Extend rate limiter (Pedagogy §6): per-IP and per-user buckets; return 429 with `Retry-After`. Tests: burst then throttle; tenant A cannot starve tenant B if keyed by tenant.
- Fake “captcha” port: `AbusePort.Verify(token) -> score`; fail closed on verifier errors for signup.

#### Lab (free-tier boxed)
1. Enable reCAPTCHA Enterprise; create a key; wire signup + login verify on Cloud Run; stay under 10k/mo.
2. Optional: Armor rate rule on a test path behind HTTPS LB — tear down to avoid idle LB IP cost (6.3).
3. **Python / Go:** verify assessment; reject low scores; log reason codes **without** raw tokens.

#### Gate
- Signup without valid assessment fails; limiter table tests green; ADR: where Armor vs app limit vs reCAPTCHA applies.

#### Decision table
| Abuse class | Prefer | Accept |
|---|---|---|
| Bot signup | reCAPTCHA + mail verify | Friction for real users |
| HTTP flood | Armor + LB | Idle LB cost if left up |
| Per-tenant API hammer | App token bucket / Gateway quota | Tuning false positives |
| Mobile API scrape | App Check later + authz | Not enough alone |
## Part 5 — Payments and money movement

**Goal:** Production-shaped checkout that is **PCI-sane**. You will not store PAN.

### 5.1 PCI as architecture


PCI is a **scope** problem before it is a control checklist. Northstar’s goal is **SAQ A**: card data never touches your servers.

#### Concepts
- **CDE (Cardholder Data Environment):** systems that store, process, or transmit PAN/SAD — or that can affect the security of those systems. Shrink CDE ruthlessly.
- **SAQ types (literacy):** **SAQ A** — fully outsourced checkout pages/iframes (Stripe Checkout / Elements); **SAQ A-EP** — merchant site still constructs payment pages that touch browser script risk; **SAQ D** — you handle PAN. This course forbids SAQ D paths.
- **Shared responsibility:** Google Cloud is PCI DSS Level 1 **as infrastructure**. You still own app design, IAM, logging hygiene, and what you put in GCS/SQL.
- **Scope reduction patterns:** tokenization via PSP; no PAN in logs/traces/prompts; separate projects/VPCs only if you ever expand scope (you should not here).
- **Fraud ML** (Radar-class) is **Part 9c.4**. This part is money movement + scope only.

#### From scratch (required)
- Threat-model one-pager: data-flow diagram with trust boundaries; mark every hop that would become CDE if PAN appeared. Checklist test: CI fails if code matches `card_number`/`pan` field names in non-test packages (simple grep gate).

#### Lab / ADR
- **ADR-004:** Stripe Checkout or Elements (hosted/iframe). Northstar is **SAQ A**. Server never sees card numbers. Secret Manager for Stripe keys; test mode only until production review.
- Walk Stripe’s “never log request bodies” rule on the webhook path (raw body for sig verify, then parse).

#### Gate
- ADR-004 merged; data-flow shows no PAN at Cloud Run; grep gate green; SAQ A claimed only with Checkout/Elements — not a custom card form.

#### Decision table
| Approach | SAQ posture | Course rule |
|---|---|---|
| Stripe Checkout / Elements | SAQ A target | **Required** |
| Custom card form POST to Cloud Run | SAQ D | **Forbidden** |
| Store “encrypted PAN” in Firestore | Still in scope | **Forbidden** |
### 5.2 Stripe on GCP (the real integration)

#### Concepts
- Create Checkout Session (or PaymentIntent) from Cloud Run using secret from Secret Manager.
- Success **redirect is not proof of payment** — webhook is.
- Webhook endpoint: **raw body**, `Stripe-Signature` verify, replay window, idempotent apply.
- Map Stripe events → (optional) Pub/Sub → order service for fan-out; still idempotent at order aggregate.
- Test clocks, test cards, `card_declined` injection.

#### Webhook + idempotency sequences
1. `checkout.session.completed` arrives → verify sig → inbox insert `event.id` → transition order `paid` → ack 200.
2. Stripe retries same `event.id` → inbox hit → 200 without double fulfill.
3. Attacker replays old body → sig fail or outside tolerance → 4xx; no state change.
4. Redirect returns before webhook → UI shows `pending_payment` until webhook; never `fulfilled` on redirect alone.
5. Duplicate charge attempts from client → Stripe + your `idempotency_key` on session create → one intent.

#### Lab
End-to-end test-mode payment; order becomes `paid` only after verified webhook.
**Python:** FastAPI webhook + signature + idempotency store.
**Go (G20):** official Stripe Go SDK; same tests; ledger types live in 5.3.

#### Gate
Secret Manager only; no PAN logs; replay test green; redirect-alone cannot fulfill.

#### Go G20 — Ledger types, idempotent charge, webhook verify
SYNTAX UNLOCK: none new; money types are ordinary structs + `json` + crypto verify API from Stripe SDK. Prefer `int64` minor units, never `float64` for money.
Concept: State machine `created → requires_action → paid → fulfilled | refunded | failed`. Idempotency key unique. Webhook: raw body + `Stripe-Signature` verify + replay window + inbox. Order becomes `paid` only after verified webhook.
Python twin first: FastAPI webhook + Firestore/SQL idempotency; then Go official Stripe SDK.
Go artifact: package `ledger` + `stripehook`; tests: `TestStateMachineTransitions`, `TestIdempotentCharge`, `TestWebhookRejectsBadSig`, `TestWebhookReplayNoDoubleFulfill`; gate: test-mode e2e; Secret Manager for secrets; no PAN stored; Part 11 matrix checks G20 under Part 5 headings.

---
### 5.3 Ledger and consistency

#### Concept
Your DB is **not** Stripe. **System of record for money movement is the PSP**; you store payment-method **tokens**, PaymentIntent/Session IDs, amounts in **minor units (`int64`)**, currency, and **status** — never PAN, never `float` money. Refunds and disputes are first-class transitions with the same idempotency rules as charge. Consistency model: order aggregate moves only on **verified** webhook/event (or explicit sync reconcile job); UI redirect is **not** proof of payment (5.2). At-least-once webhooks ⇒ **inbox / idempotency key** so double deliver cannot double fulfill.

#### State machine (LLD)
`created → requires_action → paid → fulfilled | refunded | failed` — document **guards** on each arrow (who/what evidence). Illegal: `fulfilled` without `paid`; `paid` without verified webhook/event; float money types; skipping `requires_action` when 3DS demanded. Refund: `paid|fulfilled → refunded` (partial refunds: track remaining minor units).

#### From scratch / exercise
Table tests: every legal transition; every illegal transition asserts error; refund path in Stripe **test mode**; replay webhook does not double fulfill. Prefer shared `ledger` types used by 5.2 webhook handler.

#### HLD
**Payment orchestrator** service (ACL): **no other service** talks to Stripe. Mermaid: Checkout → Orchestrator → Stripe; Webhook → Orchestrator → Order; other services read order status only.

#### Go G20 (home elsewhere — see full `#### Go G20 — …` lesson)
Stub removed to avoid double-teaching; unlock/check the full **#### Go G20 —** heading under 5.2.

#### Free-tier lab note
Stripe test mode + Secret Manager; Cloud Run webhook endpoint. No paid PSP features required. Tear down public webhook URLs you no longer use.

#### Gate
State tests exhaust legal/illegal transitions; refund path rehearsed in test mode; minor units only; orchestrator ACL named in ADR (“I pick single Stripe ACL because Y, I accept Z”).

### 5.4 What we do *not* build (and why)

Explicit bans prevent “learning” projects that create real compliance and fraud risk on free tier.

#### Concepts — hard bans
- **Homegrown card forms** posting PAN to Cloud Run / GCE / Cloud Functions = SAQ D. **Forbidden.**
- **Storing PAN** in Firestore/SQL/GCS “encrypted with our key” is still in-scope card data. **Forbidden.**
- **Building a card vault** “for learning” on GCP free tier. **Forbidden.** Use Stripe test tokens only.
- **Logging raw webhook bodies** after parse, or full payment forms — secrets and PAN leakage. **Forbidden.**
- **Using live Stripe keys** in the curriculum labs. Test mode only until a deliberate production go-live checklist.

#### From scratch / evidence
- Write `SECURITY_PAYMENTS.md`: bans above + incident pointer to 7.8 “leaked Stripe webhook secret.”
- Unit test: payment adapter accepts only token/session IDs (`tok_…`, `cs_test_…`, PaymentIntent ids) — reject strings that look like PANs (Luhn-shaped) at the boundary.

#### Lab / evidence
- PR template checkbox: “No PAN fields; Stripe test mode; webhook verify path reviewed.”
- Run Luhn-reject tests in CI on every payment PR.
- Threat model lists CDE = Stripe only; Cloud Run outside CDE.

#### Gate
- Ban list in threat model; Luhn-reject test green; no vault service in Terraform; code review checklist item checked on Part 11.

#### Decision table
| Idea | Verdict | Do instead |
|---|---|---|
| “Just this once” card field | Reject | Stripe Elements |
| Encrypt PAN with KMS | Reject | PSP tokens |
| Share live sk_live in Discord | Reject | Rotate; test keys in Secret Manager |
| Log full Stripe event JSON forever | Reject | Store event.id + type; redact payloads |
## Part 6 — Networking services (full video block) then network security

**Goal:** You can design, draw, and (within free-tier) implement VPC, IPs, firewalls, DNS, NAT, peering, and Shared VPC — then place security controls on that network.

### 6.1 Networking refresher + HTTP/2 + QUIC (from scratch)
- OSI vs TCP/IP. Ethernet, IP, TCP, UDP, ICMP, TLS (stdlib only — no homemade crypto).
- MAC vs IP vs port. ARP. Default gateway.
- Subnets, CIDR, public vs RFC1918, NAT, routes, DNS.
- Stateful firewalls, implicit deny. East-west vs north-south.
- **T-NET (required with this part, not an optional quest):** layering; end-to-end argument; routing DV vs LS (converge, count-to-infinity); reliable transfer (seq, ACK, window); congestion control AIMD — derive why window grows/shrinks. GCP products are the deployment of these ideas.

**T-NET gate:** derive AIMD sawtooth on paper; show traceroute/flow across your custom VPC lab; map each idea to a GCP control (routes, FW, LB health checks, CDN cache). Incomplete if only product clicks.


**HTTP/2 subset (why gRPC is multiplexed):**
- One TCP+TLS connection, many streams, binary frames. Toy frames: SETTINGS, DATA, uncompressed HEADERS (not full HPACK Huffman), RST_STREAM.
- **HOL demo (required):** two streams on one TCP socket; drop a byte on stream 1; prove stream 2 stalls. This is TCP HOL. It is why QUIC exists.

**HOL → QUIC (ideas complete on this lab):** HTTP/2 multiplexes streams on one TCP connection — a lost packet stalls *all* streams (HOL). QUIC multiplexes on UDP with per-stream loss recovery — stream 2 continues when stream 1 loses. Lab already proves both sides; write the one-paragraph transfer: “GFE may speak HTTP/3 to browsers; Cloud Run origin remains H1/H2; internal Northstar stays gRPC/H2 unless measured HOL on a lossy path.” Do not implement QUIC crypto.


**QUIC / HTTP/3 (ideas, then library):**
- UDP, connection IDs (survive NAT/IP change), independent stream buffers, 1-RTT with TLS 1.3 integrated, 0-RTT replay-unsafe (never checkout).
- **From scratch:** UDP echo; mini-QUIC mux (conn ID + two stream buffers); inject loss on stream 1; **prove stream 2 continues**. Contrast with the HTTP/2 HOL demo. Do **not** implement packet protection.
- Then `aioquic` / `quic-go` HTTP/3 echo. QPACK is “headers without HOL” — do not implement.
- **GCP:** GFE / Cloud CDN speak HTTP/3 to browsers. Cloud Run origin remains HTTP/1.1 or HTTP/2. You do not terminate QUIC yourself. Internal Northstar stays gRPC/HTTP/2 unless you measure HOL on a lossy path.

gRPC service implementation stays in **Part 3.2**. This section is transport only.

### 6.1b Network, VPC, and subnet — concept before console

**One home for the VPC *concept*.** Block T owns networking **theory**; this `###` owns the GCP **VPC / subnet mental model** before console clicks; **6.2** owns routing/PGA/product lab detail. **F3 does not re-teach VPC** — it only deferred scope labs here (**Prop Lock**).

**Theory prerequisites (MUST confirm or skip-test before this unit):** **T.SysTheory Networking** UG (encapsulation, L2 vs L3, address+mask, subnet-as-partition, routing-as-graph-path, isolation boundary / failure vs trust) + **T.Disc** graphs; **T.Quant** bits/bytes; **T.Algo** path literacy as needed. **T-NET** / **6.1** transport (e2e, AIMD) should already be in flight or confirmed with this Part.

#### Concept: What a VPC is (and is not)
**What / why.** A **VPC network** in Google Cloud is a **global** software-defined private network resource in a project: it is **not** tied to one region or zone. Docs: [VPC networks](https://cloud.google.com/vpc/docs/vpc). It is the fabric that later holds regional **subnets**, routes, and firewall policies. It is **not** “a region,” **not** “a subnet,” **not** “the internet,” and **not** automatic multi-region HA for your app.
**Failure modes.** Calling any RFC1918 range “my VPC” without the GCP resource; assuming VPC = one data center; treating default/auto networks as production literacy.
**Point-at.** Console: VPC network create — **no region picker** on the network itself (contrast with subnet create). Paper: one box labeled VPC spanning two region columns.

#### Concept: Subnet as regional address partition inside a VPC
**What / why.** A **subnet** is a **regional** resource: an IPv4/IPv6 **address partition** (CIDR) inside a VPC, usable by VMs in **any zone of that region**. Theory recall: subnet-as-partition from **T.SysTheory Networking** UG — mask defines the set; region is the GCP placement constraint. One VPC can hold `us-central1` + `europe-west1` subnets without “peering regions together.”
**Failure modes.** “Subnet is zonal because my VM is”; “VPC is regional because my subnet is”; conflating subnet with firewall; overlapping CIDRs planned for later peering.
**Point-at.** Subnet create dialog: **must pick a region** + CIDR. Two VMs in `us-central1-a` and `us-central1-b` can share one regional subnet.

#### Concept: Auto vs custom mode (decision, not a click race)
**What / why.** **Auto mode** auto-creates one subnet per region from a Google-managed block (`10.128.0.0/9` family) — fine for throwaway demos, **forbidden as prod literacy**. **Custom mode** starts with **no** subnets; you create every subnet and CIDR. Learning path: custom mode + delete default network once you can rebuild.
**Failure modes.** Shipping auto mode “because the console defaulted it”; deleting default network before documenting how you will SSH/egress.

#### Concept: Isolation — failure domain vs trust boundary (VPC edition)
**What / why.** Region/zone (F3) are **failure domains**. VPC firewall / IAM / later VPC-SC are **trust / policy boundaries**. Being in the same VPC does **not** mean “trusted” or “highly available.” Routing decides where a packet *could* go; firewall decides whether it *may* (**6.4** deepens).
**Failure modes.** “Same VPC = trusted”; “custom VPC alone = secure”; skipping FW allows after custom VPC create.

#### From scratch (CIDR partition exercise — required)
- Paper: one VPC `10.10.0.0/16`; subnet A `10.10.0.0/20` in `us-central1`; subnet B `10.10.16.0/20` in `europe-west1`. Compute host counts; prove non-overlap; leave headroom note for later GKE secondary ranges (**Part 9** — name only).
- Userspace (Python then Go): given address+prefix, return network ID + usable range; `same_subnet(a,b,prefix)`; detect CIDR overlap. Unit tests are the gate — not console.

#### HLD
Northstar sketch (boxes only): custom VPC → app subnet (usc1) → data subnet or FW-segmented same subnet → no public IPs on VMs (intent) → PGA/NAT named as *later controls* (**6.2** / **6.9**). No Interconnect / Shared VPC required in this first HLD.

#### LLD
- Names: `ns-vpc`, `ns-subnet-usc1`, `ns-subnet-ew1`.
- Terraform shape (may be paper): `google_compute_network` with `auto_create_subnetworks=false`; `google_compute_subnetwork` with region + CIDR. PGA flag noted for **6.2**.

#### GCP lab (free-tier boxed) — concept confirmation
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ Custom-mode VPC + one regional subnet; narrate: network has │
│ no region picker; subnet does. Optional second region       │
│ subnet on diagram if credits tight. Do not skip theory gate.│
│ Firewall deep-dive is 6.4 — allow only what 6.5 needs later.│
└─────────────────────────────────────────────────────────────┘
```

#### Gate
- Unseen: given two CIDRs and two regions, say which are same-subnet, which need a route story, and whether the **VPC** or the **subnet** is the regional object.
- Nearby: why F3 correctly refused to classify VPC/subnet — and what theory tier unlocked them now.
- **Incomplete if** only product clicks without subnet-as-partition derive from T.SysTheory.

---

### 6.2 VPC, subnets, routing, Private Google Access


**Prereq:** **6.1b** concept-before-console (VPC global / subnet regional / CIDR partition) + **T.SysTheory Networking** UG confirmed. This section deepens **routing**, **Private Google Access**, and the production lab — it does **not** re-teach the VPC intuition from scratch (recall + apply). Docs: [VPC networks](https://cloud.google.com/vpc/docs/vpc), [Private Google Access](https://cloud.google.com/vpc/docs/private-google-access).

#### Concepts
- **Recall (6.1b):** **VPC is global; subnets are regional** (span all zones in that region). One VPC can hold `us-central1` + `europe-west1` subnets without peering between regions.
- **Recall — Auto vs custom mode:** auto creates regional subnets for you — fine for demos, **forbidden in prod literacy**. Custom mode: you create every subnet and CIDR. **Delete the default network** in learning projects once you can rebuild.
- **Primary and secondary ranges:** primary for VM NICs; secondary (alias IPs) for GKE Pods/Services. Plan CIDRs so they never overlap peers or on-prem (Part 8b).
- **Routes:** system-generated (subnet, default), custom static, dynamic via **Cloud Router / BGP** (VPN/Interconnect). Routing decides path; firewall decides allow/deny.
- **Private Google Access (PGA):** subnet flag so VMs **without external IPs** can reach `*.googleapis.com` / Google APIs. PGA ≠ general internet. General egress needs **Cloud NAT** (6.9).
- **PGA for on-prem** vs **Private Service Connect (PSC):** different products — do not conflate. PSC consumes services via private endpoints (6.15).
- **Cloud Run egress:** Direct VPC egress (preferred modern path) vs Serverless VPC Access connector (legacy tax). Only attach VPC when you must reach private IPs.

#### From scratch
- Paper CIDR plan: one VPC `10.10.0.0/16`, subnet A `10.10.0.0/20` us-central1, subnet B `10.10.16.0/20` europe-west1. Leave headroom for GKE secondary ranges.
- Userspace: given a CIDR, list usable host count; detect overlap between two CIDRs (unit tests). Ties to 6.3 allocator toy.

#### Decision exercise

| Need | Control | Not this |
|---|---|---|
| Prod IP plan | Custom VPC + explicit subnets | Default / auto mode |
| Private VM → GCS API | PGA on subnet | Giving the VM a public IP “for APIs” |
| Private VM → example.com | Cloud NAT | PGA |
| Reach private Cloud SQL | Private IP + VPC path / PSC | Public SQL + `0.0.0.0/0` |

#### HLD
Northstar: custom VPC, app subnet, data subnet (or same subnet with FW segmentation), no default network, no public IPs on VMs, PGA on, NAT for third-party egress.

#### LLD
- Naming: `ns-vpc`, `ns-subnet-usc1`, `ns-subnet-ew1`.
- MTU / flow logs flags noted (flow logs deep in 6.8).
- Terraform: `google_compute_network` `auto_create_subnetworks=false`, `google_compute_subnetwork` with `private_ip_google_access=true`.

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ Create custom VPC + 2 regional subnets; enable PGA.         │
│ Do not create VMs yet if you will bill — or use e2-micro.   │
│ Delete default network only after backup routes documented. │
│ Credits-optional: second project peering (6.6).             │
└─────────────────────────────────────────────────────────────┘
```

#### Lab
- Custom VPC, two subnets in two regions, no default network (when safe).

#### Gate
- Can explain global VPC vs regional subnet; PGA vs NAT; custom vs auto; CIDR plan written.
### 6.3 IP addressing — dynamic (ephemeral) vs static, end to end

This is first-class. You configure IPs on VMs, forwarding rules, Cloud NAT, and you write the user-space toys that make the words mean something.

#### Concepts
- **Internal vs external:** internal is RFC1918 (or Google internal IPv6) — not internet-routable. External is publicly routed. Cloud Run/GKE nodes often have **no** external IP; egress via Cloud NAT.
- **Ephemeral (dynamic) vs static:**
  - Ephemeral: assigned automatically; **released** when you stop/delete the VM or delete the forwarding rule. Next create may get a different address. Fine for cattle, bad for DNS A records and allowlists.
  - Static: reserved in the project (or subnet for internal). Survives VM delete/recreate. You attach/detach. You **pay for unused external static IPs**.
- **Regional vs global:**
  - Regional internal IPv4: from a subnet range; VMs, ILB, alias IPs.
  - Regional external IPv4: VMs, regional LBs. `/32` from Google’s pool.
  - Global external IPv4/IPv6: **global** external Application / proxy Network Load Balancers (Premium tier). One anycast IP, nearest GFE.
- **IPv4 / IPv6 / dual-stack / IPv6-only.** Internal IPv6 `/96` from subnet; external IPv6 `/96` regional or `/64` global.
- **Alias IP ranges:** extra internal IPs on one NIC (GKE Pod CIDR).
- **Primary internal IP** is required on IPv4 NICs. External is optional.
- **Forwarding-rule IP:** the address clients hit. Can be ephemeral or reserved static. Multiple forwarding rules can share a static IP with different ports/protocols when the LB type allows it.
- **Cloud NAT IPs:** a pool of regional external IPs used as source for private VMs. Ephemeral NAT IPs vs static NAT IPs (allowlist partners on a stable egress IP).
- **Private Google Access** is not an IP you assign; it is a subnet flag so VMs without external IPs can reach `*.googleapis.com`.
- **DNS coupling:** A/AAAA for a service must target a **static** IP or a stable hostname (`run.app`, GCLB forwarding rule you own). Never put an ephemeral VM IP in a public A record.
- **Network Service Tiers:** Premium (Google backbone, global IP) vs Standard (ISP peering, regional IP). Global LB requires Premium.

#### Combinatorial IP space — per-combination anchors (use case → type)

Work each anchor before the mega-table. Idle **external** static IPs bill — mark every lab with release steps.

##### C1 — Regional internal ephemeral
**Use case:** Cattle VM in a MIG; private IP can change on recreate; callers use LB or DNS to a stable name, not the VM IP.
**Pick:** ephemeral primary internal IP.
**Accept:** address changes on replace.

##### C2 — Regional internal static
**Use case:** Appliance or license tied to a fixed private IP; or a bastion-less admin target that must stay put across recreate.
**Pick:** `gcloud compute addresses create … --subnet=…` then attach.
**Accept:** IP planning discipline; still no internet.

##### C3 — Regional external ephemeral
**Use case:** Throwaway public demo VM you will delete today.
**Pick:** ephemeral external (or better: **no** external + IAP).
**Accept:** DNS break on stop/delete; prefer IAP over public SSH.

##### C4 — Regional external static
**Use case:** Partner allowlists a VM’s public IP (prefer NAT static — C6 — over putting public IP on the VM).
**Pick:** regional external static attached to VM or used by regional LB/NAT.
**Accept:** **bills if idle**; release in same sitting after lab.

##### C5 — Global external static
**Use case:** One anycast IPv4 for global external Application LB (custom domain apex).
**Pick:** `gcloud compute addresses create … --global`.
**Accept:** Premium tier; idle IP bills; Cloud CDN attaches to this LB story (**1.4**).

##### C6 — Cloud NAT regional external (ephemeral pool vs static)
**Use case:** Private VMs need egress to SaaS; partner allowlists your egress IP → **static NAT IPs**. Otherwise auto-allocated ephemeral NAT IPs.
**Pick:** Cloud NAT on Cloud Router; static addresses only when allowlisted.
**Accept:** NAT hourly cost; `NAT allocation failed` when ports exhaust.

##### C7 — Alias IPs / secondary ranges
**Use case:** GKE Pod CIDR on nodes.
**Pick:** secondary range on subnet + alias IP on NIC.
**Accept:** CIDR sprawl — plan before peering.

##### C8 — Platform-managed (no assign)
**Use case:** Cloud Run / App Engine / Many managed services.
**Pick:** you do not assign VM IPs; custom domain → Hosting or your LB IP (C5).
**Accept:** less IP-level control; more IAM/VPC egress design.

#### Explicit decision table (combinatorial — PCA)

| # | Scope | Visibility | Persistence | Typical attachment | Northstar / PCA pick when… |
|---|---|---|---|---|---|
| C1 | Regional | Internal | Ephemeral | VM primary NIC | MIG cattle |
| C2 | Regional | Internal | Static | VM / ILB | Stable private VIP |
| C3 | Regional | External | Ephemeral | VM (avoid) | Disposable demo only |
| C4 | Regional | External | Static | VM / regional LB / NAT | Allowlist or regional LB |
| C5 | Global | External | Static | Global HTTPS / proxy LB | Worldwide anycast HTTPS |
| C6 | Regional | External | Ephemeral or static pool | Cloud NAT | Private VMs need egress |
| C7 | Regional | Internal | N/A (range) | Alias / GKE | Pod IP space |
| C8 | n/a | Platform | n/a | Cloud Run / GAE | Managed compute |

**Anti-patterns:** ephemeral VM IP in public DNS; idle global/regional external static left reserved; public IP on VM “so apt works” instead of NAT+PGA; global IP on Standard tier (invalid for global LB).


#### Teaching metaphors (rung-1 — IP axes)
- **Hotel room phone vs reserved direct dial:** Ephemeral = tonight’s room phone. Static = you paid to keep the number after checkout (and **unassigned static external IPs bill higher** — release them).
- **Private hallway vs public listed number:** Internal vs external.
- **City phone book vs worldwide 800-number:** Regional static for a VM/NAT/regional LB; **global** static external only for global Application / proxy Network LBs (Premium).
- **Promotion:** Ephemeral external can be promoted to static to keep the number after resource delete.
- **Org policy trap:** `constraints/compute.vmExternalIpAccess` can block new externals and break MIG autoheal if mis-set.
- Console → VPC network → IP addresses: sort by Type / In use / Region vs Global and narrate C1–C8.

#### From scratch (required)
- Userspace “DHCP-like” allocator: given a CIDR, allocate/release leases with TTL (ephemeral) vs permanent reservation (static). Tests: exhaustion, double-free, persist across process restart (file).
- Userspace NAT: map `(src_ip, src_port) → (nat_ip, nat_port)` and rewrite a fake packet header struct. Tests: two clients, port reuse after expiry.
- Bind a local HTTP server to `127.0.0.1` vs `0.0.0.0`; prove with a client. This is “internal vs external” on one machine.

#### GCP configuration (required procedure — Terraform written even if you do not apply paid IPs)
```
# internal static (free-ish; still clean up)
gcloud compute addresses create ns-int --region=us-central1 --subnet=... --addresses=<in-range>

# regional external static (BILLS IF IDLE)
gcloud compute addresses create ns-ext --region=us-central1

# global external static for HTTPS LB (BILLS IF IDLE)
gcloud compute addresses create ns-gip --global

# attach to VM
gcloud compute instances create ... --private-network-ip=... --address=ns-ext   # prefer omit --address

# promote ephemeral → static
gcloud compute addresses create ns-promoted --addresses=<current> --region=...

# ALWAYS
gcloud compute addresses delete ns-ext --region=us-central1
```
- Console + Terraform: `google_compute_address` (regional), `google_compute_global_address`.
- List, describe, attach, detach, promote, release.
- **Lab PART 1:** internal static on e2-micro; SSH via IAP; no external IP.
- **Lab PART 2:** reserve a regional external static, attach, curl, **delete VM and delete address in the same sitting**. Prove idle-IP billing in the cost model even if you never leave it up.
- **Python / Go:** Compute Engine Address API — list addresses, flag `status=RESERVED` (idle) as a cost leak.

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ Prefer C1/C2 + IAP; avoid C3/C4 on Always Free path.        │
│ If you reserve C4/C5 for learning, delete address SAME day. │
│ Script: list RESERVED external addresses; alert if any.     │
│ Credits-optional: C5 + HTTPS LB (pair with 1.12).           │
└─────────────────────────────────────────────────────────────┘
```

#### Decision table (PCA) — quick
| Need | Address type |
|---|---|
| VM that can die and come back on the same private IP | Regional **internal static** (C2) |
| Partner allowlists your egress | Cloud NAT **static** regional external (C6) |
| Public website, one IP worldwide | **Global external static** on HTTPS LB (C5) |
| Throwaway sandbox VM | Ephemeral internal, **no** external (C1) |
| Cloud Run / GAE | Platform-managed (C8); custom domain → Hosting or LB IP |

#### Gate
- Can recite C1–C8 with a use case each; idle external static = bill; PGA ≠ NAT; Python/Go idle-IP scanner exists.
### 6.4 Firewall and firewall rules

Routing decides where a packet *could* go; firewall rules decide whether it *may*. VPC firewall rules are enforced on the VM (distributed); implied deny-ingress / allow-egress are always there. Prefer **service accounts as targets** over network tags for production.

#### Concepts
- **Implied rules:** allow all egress (priority 65535), deny all ingress (65535). Lower priority number = higher precedence.
- **Direction, action, protocol/port, source/destination ranges.** Ingress source = who talks *to* you; egress destination = where you may go.
- **Targets:** all instances in network, **network tags**, or **service accounts** (prefer SA — tags are forgeable by anyone who can set tags on a VM).
- **Hierarchical firewall policy** (org/folder) vs VPC rules vs **Cloud NGFW** (deep in 6.12). Evaluation order matters — org policies can deny what a VPC rule allows.
- **Common allowlists:** IAP SSH/TCP `35.235.240.0/20`; health check ranges `35.191.0.0/16`, `130.211.0.0/22` (and others per LB type — confirm docs for your LB).
- Custom VPCs do **not** ship `default-allow-internal` — two VMs in the same VPC cannot talk until you allow it.

#### From scratch
- Given a rule set + 5-tuple `(src, dst, proto, sport, dport)`, decide allow/deny (unit tests). This is the same toy as 6.12, started here.
- **Python then Go:** table-driven evaluator; prove SA-targeted rule beats a broader tag deny when priorities say so.

#### Decision exercise

| Goal | Rule sketch | Anti-pattern |
|---|---|---|
| SSH without public IP | Ingress allow TCP 22 from IAP range, target = bastion SA | `0.0.0.0/0` SSH |
| LB health checks | Ingress from Google HC ranges to serving port | Forgetting HC → backends unhealthy |
| App east-west | Ingress from app subnet CIDR or peer SA | Allow-all-internal forever |

#### HLD
Northstar: deny ingress default; allow IAP to admin; allow HC to API MIG/Run NEG path; allow app→SQL on 5432 from app SA only.

#### LLD
Terraform `google_compute_firewall` with `target_service_accounts`, explicit `priority`, description, and log config stub (flow logs in 6.8).

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ On custom VPC: allow IAP SSH + HC ranges; no 0.0.0.0/0 SSH. │
│ Optional e2-micro: prove SSH via IAP works; public SSH fails.│
│ Tear down VM if not Always Free eligible region/type.       │
└─────────────────────────────────────────────────────────────┘
```

#### Lab
- Allow IAP SSH (`35.235.240.0/20`) and health checks; deny the rest.

#### Gate
- Can explain implied rules + priority; SA targets preferred; IAP range memorized; 5-tuple tests green.
### 6.5 Custom VPC labs PART 1–2

End-to-end assembly of 6.2–6.4 + NAT preview. This is the “private VM that can still work” lab.

#### Concepts
- PART 1: custom VPC, two subnets (can be one region if free-tier constrained), firewall (IAP + optional internal), one **e2-micro**, **no public IP**, OS Login + **IAP TCP** SSH.
- PART 2: add **Cloud NAT** (6.9) so the VM can `curl` the internet; enable **PGA** so `gcloud` / GCS APIs work without NAT to Google APIs necessarily (PGA handles Google APIs; NAT handles the rest).
- Idempotent create/destroy from a script — cattle, not pets.

#### From scratch
- Shell or Python script: create → verify SSH via IAP → destroy. Second run is no-op / update. Exit non-zero if a public IP appeared.

#### HLD
Laptop → IAP → private e2-micro → (PGA → googleapis) / (NAT → internet). No bastion VM with a public IP.

#### LLD
- Startup script installs nothing heavy; Ops Agent optional (cost awareness).
- Labels: `env=lab`, `owner=northstar`.
- Terraform preferred; `gcloud` acceptable for first pass.

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ 1× e2-micro in Always Free region; no external IP; IAP SSH. │
│ Cloud NAT has cost — create, prove wget, DESTROY same day. │
│ Credits-optional: second subnet in second region (diagram). │
└─────────────────────────────────────────────────────────────┘
```

#### Lab
- End-to-end: VPC, two subnets, firewall, one e2-micro, IAP SSH, Cloud NAT for egress, no public IP.
- **Python / Go:** `gcloud`/`google-cloud-compute` create/destroy the sandbox from a script (idempotent).

#### Gate
- SSH works without public IP; NAT proof captured then destroyed; script idempotent; no orphan static IPs.
### 6.6 VPC Network Peering

Peering connects two VPC networks so private IPs can talk — **non-transitive**, CIDRs **must not overlap**, routes exchanged selectively. Firewall rules are **not** auto-updated.

#### Concepts
- **Non-transitive:** A↔B and B↔C does **not** give A↔C. Hub-and-spoke needs Network Connectivity Center / VPN / proxies — not chained peering.
- **CIDR overlap:** peering create fails or traffic blackholes — plan IP space in 6.2.
- **Route exchange:** subnet routes always (with options for some ranges); custom routes optional.
- **Who pays egress:** data transfer pricing between peered networks — know it exists for PCA cost talk.
- **When peering loses:** Shared VPC (one network, many projects) or **PSC** (consume a service without full network mesh) often win.

#### From scratch / decision exercise

| Situation | Prefer | Why |
|---|---|---|
| Two product teams, separate projects, need private API | Peering **or** PSC | Peering = full L3; PSC = service-oriented |
| Three spokes need isolation | Shared VPC or NCC hub | Peering not transitive |
| Overlapping `10.0.0.0/8` brownfield | Redesign / RFC1918 carve | Cannot peer overlap |

#### HLD
`ns-app-vpc` ↔ `ns-data-vpc` peering; draw X on “transitive hope.” Alternative: host Shared VPC (6.7).

#### LLD
- Both sides create peering; ACTIVE state required.
- Ingress FW in each VPC must allow the **peer’s subnet ranges** (or peer SAs if applicable).
- Export/import custom routes flags documented.

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ Two VPCs in one project (or two projects if available).     │
│ Peer; allow FW; ping/curl private IP; traceroute notes.     │
│ Destroy peering + VPCs after. Avoid extra VMs if billed.    │
│ Credits-optional: second project peering.                   │
└─────────────────────────────────────────────────────────────┘
```

#### Lab
- Two projects (or two VPCs) peered; verify connectivity; then destroy.

#### Gate
- Can explain non-transitive + overlap + FW must be updated; HLD shows when Shared VPC/PSC beat peering.
### 6.7 Shared VPC

Shared VPC is the landing-zone pattern: one **host project** owns the network/subnets/firewalls; **service projects** attach and place VMs/GKE/Run connectors into those subnets. Separates network admin from app admin.

#### Concepts
- **Host vs service projects** under the same organization (Shared VPC Admin IAM).
- Who owns subnets, secondary ranges, firewall, NAT, peering — almost always **host**.
- Service project principals need `roles/compute.networkUser` on the subnet (or project) to attach.
- Org policy + folder structure: `shared-net` host, `prod-app` / `prod-data` services.
- Vs peering: Shared VPC = **one** VPC many projects; peering = two VPCs.

#### From scratch / decision exercise
Sketch Northstar org: host `shared-net`, service `prod-app`. Who creates a firewall rule for IAP? Who deploys Cloud Run with Direct VPC egress into `ns-subnet-usc1`?

#### HLD
Org → folder `networking` (host) + folder `applications` (services). Diagram required even without a live org.

#### LLD
Terraform modules: host enables Shared VPC; service attaches; subnet IAM bindings; no live org required if you cannot create projects — still write the HCL.

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ Diagram + Terraform REQUIRED. Live Shared VPC needs org +   │
│ multiple projects — credits/org-optional. Do not fight IAM  │
│ on a personal account without org; submit design pack.      │
└─────────────────────────────────────────────────────────────┘
```

#### Gate
- HLD + Terraform reviewed; can explain host vs service vs peering in one minute.
### 6.8 VPC Flow Logs

Flow logs sample connection records as they leave/arrive at VMs (and some other endpoints). Use them for incident response, denied-traffic debug, and top-talker analysis — not as a full packet capture.

#### Concepts
- **Enable per subnet** (or via FW policy logging). Aggregation interval, sampling rate, metadata annotations.
- **Sinks:** Cloud Logging (default) and/or BigQuery (1 TiB free query/month — stay aware of ingest cost).
- Fields: connection 5-tuple-ish, bytes/packets, allow/deny disposition, reporter (SRC/DEST), annotations (GKE, etc.).
- Sampling means you will **miss** some flows — correlate with Firewall Rules Logging when you need every deny.
- Privacy: flow logs can reveal internal topology — treat as sensitive ops data.

#### From scratch
- **Python then Go:** parse a sample JSON flow log export; count top talkers by bytes; count denies by dst_port; unit tests on fixture files (no live traffic required).

#### Decision exercise

| Question | Tool |
|---|---|
| Who talked most to Redis last hour? | Flow logs → BQ/Logging |
| Why is HC failing? | Often FW, not flow logs first |
| PCI evidence of east-west | Flow logs + VPC-SC (6.15) |

#### HLD
Subnets with flow logs → Logging bucket / BQ dataset `ns_flow` → dashboard. Retention + cost note.

#### LLD
- Terraform: `log_config` on `google_compute_subnetwork`.
- Sample query sketches (Logging Logs Explorer and BQ SQL).

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ Enable flow logs on lab subnet at low sampling; generate a  │
│ few flows from e2-micro; export sample to file; disable or  │
│ destroy subnet after. Prefer offline fixture parsing if     │
│ Logging ingest worries you. Credits-optional: BQ sink.      │
└─────────────────────────────────────────────────────────────┘
```

#### Lab
- Enable, sampling, metadata; sink to Logging/BigQuery.
- **Python / Go:** parse a sample flow log; count top talkers and denies.

#### Gate
- Parser tests green; can explain sampling ≠ full PCAP; cost note written.
### 6.9 NAT PART 1–2

Cloud NAT gives private VMs (and some serverless paths) **egress** to the internet without assigning each VM an external IP. It is not inbound NAT for random internet clients — inbound stays via LB/IAP.

#### Concepts
- **Why:** hardened VMs with no public IP still need `apt`, webhooks out, third-party APIs.
- **Cloud NAT vs instance-level NAT vs Cloud Router:** Cloud NAT is managed, configured **on a Cloud Router** in the region; not a box you SSH to.
- **NAT IPs:** auto-allocated ephemeral pool vs **manual static** regional external IPs (partner allowlists — 6.3 C6).
- **Logging + errors:** enable NAT logging; `NAT allocation failed` = port/IP exhaustion under high concurrent connections — add IPs or reduce ports-per-VM pressure.
- **PGA vs NAT:** PGA = Google APIs without external IP; NAT = general internet. Often enable **both**.
- Billing: NAT gateway hours + data processing — **destroy after lab**.

#### From scratch
- Reuse 6.3 userspace NAT map; prove two clients share one public IP with different ports; expiry frees ports.

#### Decision exercise

| Need | Pick |
|---|---|
| Private VMs, occasional egress | Cloud NAT auto IPs |
| Partner allowlists egress IP | Cloud NAT **static** IPs |
| Only googleapis.com | PGA may suffice |
| Inbound from internet | External LB / IAP — not NAT |

#### HLD
Private subnet → Cloud NAT → internet; same subnet → PGA → googleapis. No VM external IPs.

#### LLD
```
gcloud compute routers create ns-nat-router --network=ns-vpc --region=us-central1
gcloud compute routers nats create ns-nat --router=ns-nat-router --region=us-central1 \
  --auto-allocate-nat-external-ips --nat-all-subnet-ip-ranges
```
Static IP variant uses `--nat-external-ip-pool=…`.

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ PART 1: private e2-micro (6.5) without NAT — prove Google   │
│ APIs via PGA; prove example.com FAILS.                      │
│ PART 2: add Cloud NAT; wget https://example.com succeeds.   │
│ DESTROY NAT + router same sitting (cost). Credits-optional: │
│ static NAT IP allowlist demo — release IP after.            │
└─────────────────────────────────────────────────────────────┘
```

#### Lab
- Cloud NAT on the custom VPC; VM wget to `https://example.com` without external IP. Destroy after.

#### Gate
- PART 1/2 contrast captured; NAT destroyed; can explain PGA vs NAT vs inbound LB.
### 6.10 DNS fundamentals, record types, Cloud DNS

DNS is how names become addresses. Wrong TTL or ephemeral A records are outages. Cloud DNS is Google’s managed authoritative DNS (public and private zones).

#### Concepts
- **Recursive vs authoritative.** Stub resolvers ask recursors; Cloud DNS hosts **authoritative** zones you control.
- **TTL:** caching contract. Low TTL = faster change, more query load.
- **Record types:** A, AAAA, CNAME, MX, TXT, NS, SRV, CAA, PTR — know what each points at.
- **Cloud DNS:** public zones (internet) vs **private zones** (VPC-visible); peering DNS; forwarding to on-prem; DNSSEC for public zones.
- **Split horizon:** same name, different answers internally vs publicly (private zone + public zone).
- **Coupling to 6.3:** public A/AAAA must target **static** LB IPs or stable platform hostnames — never ephemeral VM IPs.
- Cloud DNS is **not Always Free** — Terraform still written; `/etc/hosts` + diagram acceptable for free-tier path.

#### From scratch
- **Python then Go:** miniature authoritative map `name → records`; resolve with TTL expiry; tests for CNAME chains (depth limit) and apex CNAME rejection policy (document industry rule).

#### Decision exercise

| Need | Record / product |
|---|---|
| `api.internal.northstar.dev` → `10.10.0.5` | Private zone A |
| `www` → Hosting | CNAME/A per Hosting docs |
| Prove domain ownership | TXT |
| Mail | MX (+ SPF/DKIM TXT) |

#### HLD
Public zone for marketing; private zone for `*.internal.northstar.dev`; forwarding to on-prem later (8b).

#### LLD
Terraform `google_dns_managed_zone` + `google_dns_record_set`. Document DNSSEC enablement steps without requiring live purchase.

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ Preferred: private zone in lab VPC + A to internal IP.      │
│ If Cloud DNS cost is a concern: /etc/hosts + diagram + TF.  │
│ Credits-optional: public zone + DNSSEC on a cheap domain.   │
└─────────────────────────────────────────────────────────────┘
```

#### Lab
- Private zone for `internal.northstar.dev` A record to internal IP. Cloud DNS not Always Free — use `/etc/hosts` + diagram if no credits; Terraform still written.

#### Gate
- Can list record types with one-line purpose; split horizon explained; no ephemeral IP in a public A record design.
### 6.11 Network security overlay (NGFW, Armor, IAP, VPC-SC, LB TLS)

This is the **map** of controls you will deepen in 6.12–6.16 and Part 7. Place each control on the packet path; do not invent a seventh product that duplicates another.

#### Concepts
- **Cloud NGFW / hierarchical FW** — org-wide policy, threat intel, FQDN/geo (Enterprise features) — depth in **6.12**.
- **Cloud Armor** — WAF / OWASP / rate-limit / bot on **external Application LB** (global). Pair with CDN lesson in **1.4**; do not re-teach CDN here.
- **IAP** — identity-aware access to apps and SSH/TCP — **6.14**.
- **VPC Service Controls** — perimeter around Google APIs / data to limit exfil — **6.15**.
- **LB TLS** — managed certs, SSL policies (min TLS 1.2+), HTTPS redirect on Application LB — types in **1.12** / **6.13**.
- **DDoS** — GFE absorbs volumetric; Armor adds L7 — **6.16**.

#### From scratch / decision exercise
Draw Northstar packet path and label **one** primary control per hop:
Internet → GFE/Armor → URL map → serverless NEG → Cloud Run → (VPC-SC) → GCS/SQL.

#### HLD
Defense in depth diagram: edge (Armor/LB TLS) → identity (IAP) → network (FW/NGFW) → data (VPC-SC/CMEK).

#### LLD
One-pager ADR: which controls are free-tier / Always Free adjacent vs credits-optional.

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ Diagram-only REQUIRED. Live Armor + global LB = credits.    │
│ Free path: IAP on App Engine/Cloud Run admin (6.14 lab).    │
└─────────────────────────────────────────────────────────────┘
```

#### Gate
- Can place NGFW, Armor, IAP, VPC-SC, LB TLS on a path diagram without overlapping responsibilities wrongly.
### 6.12 Firewall and Cloud NGFW (security depth)

VPC firewall rules (6.4) scale into **hierarchical policies** and **Cloud NGFW**. Same 5-tuple mental model; richer match conditions and org scope.

#### Concepts — GCP offerings
- **VPC firewall rules** — per-network, classic surface (6.4).
- **Hierarchical firewall policies** — org / folder / project attachment; evaluate before or with network rules per product rules.
- **Global network firewall policy / Cloud NGFW** — threat intelligence lists, geolocation, FQDN objects, optional TLS inspection (**Enterprise** — know it exists; do not require paid lab).
- **Implied rules** remain (allow egress, deny ingress). Priority math across layers — draw the evaluation order from current docs when you lab.
- **Targets:** prefer **service accounts** over tags (tags are not authn).
- Intrusion / malware features are NGFW Enterprise territory — PCA literacy, not free-tier dependency.

#### From scratch
- Expand the 6.4 evaluator: multiple layers (org policy deny → VPC allow). Unit tests prove org deny wins.
- **Python then Go:** given rule set + 5-tuple, decide allow/deny. Write Terraform for `google_compute_firewall` and stub `google_compute_network_firewall_policy` resources.

#### Decision exercise

| Control need | Pick |
|---|---|
| One project lab | VPC firewall rules |
| Company-wide SSH deny from internet | Hierarchical policy at org/folder |
| Block known bad IPs / geo | NGFW threat intel / geo (credits) |
| L7 OWASP on public HTTPS | Cloud Armor on Application LB (not NGFW) |

#### HLD
Org policy “deny ingress 22 from `0.0.0.0/0`” + project VPC allows IAP only. Armor sits at edge LB, not as a substitute for VPC FW.

#### LLD
- Priority bands documented (e.g. 1000 deny, 2000 IAP allow, 3000 app allow).
- Logging enabled on deny rules used in IR drills.

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ Unit-test evaluator REQUIRED. Live hierarchical policy may │
│ need org admin — diagram + TF if you lack permission.       │
│ Credits-optional: NGFW Enterprise features — read only.     │
└─────────────────────────────────────────────────────────────┘
```

#### Gate
- 5-tuple tests cover layered deny; Terraform for VPC FW merges clean; can contrast Armor (L7 edge) vs NGFW (L3/4+/org).
### 6.13 Load balancing, TLS, CDN, and the edge

**Dedupe:** the full CDN lesson is **1.4** only. The full HA / LB axis lesson (external vs internal; global vs regional; application vs proxy vs passthrough) is **1.12**. This subsection is the networking-part **pointer + TLS/edge checklist** — do not re-teach CDN modes or rebuild Raft here (Raft → **8.1** / **12.S20**).

#### Concepts
- External vs internal; global vs regional; Application vs Network vs Proxy — **see 1.12 anchors A–D** before any quiz.
- SSL policies, Google-managed certs, HTTPS redirect on Application LB.
- Serverless NEGs (Cloud Run, App Engine, Cloud Functions) behind HTTPS LB.
- Forwarding rule **must** have an IP: ephemeral or reserved static (**6.3** C4/C5). Deleting the rule without deleting a reserved IP leaves a billing leak.
- Cloud CDN enables on the **global external Application LB** (or classic) — modes, keys, signed URLs, invalidation → **1.4**.
- Cloud Armor and reCAPTCHA at this edge; details 1.4 / 4.10.

#### From scratch
- L4/L7 proxies from 1.4 in front of two local backends; weighted round-robin + drain (canary). Map each feature to a GCP LB type using the 1.12 table.

#### HLD
Credits-optional production edge: global external Application LB + managed cert + Armor + CDN → serverless NEG → Cloud Run. Free-tier edge: Firebase Hosting + `run.app` / IAM invoker.

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ Free path: Cloud Run auth / Hosting as the edge.            │
│ Credits-optional: global HTTPS LB + Armor + CDN.            │
│ ALWAYS release reserved static IPs same sitting.            │
└─────────────────────────────────────────────────────────────┘
```

#### Lab
- Cloud Run auth as the free-tier “edge.” Credits-optional: global HTTPS LB + Armor + CDN in front of Cloud Run.

#### Gate
- Can point to 1.12 for LB choice and 1.4 for CDN; can explain managed cert + SSL policy; idle IP leak named.
### 6.14 Zero-trust access

“Inside the VPC” is not a trust tier. Zero trust: authenticate and authorize every request with **identity + device + context**, then least-privilege network paths.

#### Concepts
- **IAP (Identity-Aware Proxy)** for admin UIs and for **IAP TCP** (SSH to VMs without public IP — already used in 6.5).
- Supported surfaces: App Engine, Cloud Run, GKE (via Ingress/Gateway patterns), GCE via IAP TCP.
- **Context-aware access / Chrome Enterprise Premium:** device posture, IP, region — beyond “has Google login.”
- **BeyondCorp model:** identity-aware access to apps; network location is a signal, not the perimeter.
- Pair with Part 4: IAP can use Google identities or Identity Platform identities depending on setup.

#### From scratch / decision exercise

| Access | Prefer | Reject |
|---|---|---|
| Human admin SSH | IAP TCP + OS Login | Public `0.0.0.0/0` SSH |
| Human admin UI | IAP in front of Cloud Run/GAE | VPN-only as sole control |
| Service-to-service | SA + IAM / mTLS mesh later | Flat allow-all subnet |

#### HLD
Users → IAP → admin Cloud Run; attackers on the VPC still fail without identity. VPN optional for legacy, not the only gate.

#### LLD
- IAP-secured Web App User role binding to a group.
- HTTPS LB + IAP brand/OAuth client when using full LB path (credits-optional); free path: App Engine/Cloud Run IAP toggles.

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ Enable IAP on App Engine standard admin service OR Cloud    │
│ Run (per current product support in your project).          │
│ Prove unauthenticated access fails; group member succeeds.  │
│ Credits-optional: context-aware access policies.            │
└─────────────────────────────────────────────────────────────┘
```

#### Lab
- IAP on an App Engine or Cloud Run admin service.

#### Gate
- Unauthenticated denied; group allow works; HLD states VPC ≠ trusted.
### 6.15 Segmentation and exfil controls

Segment so a breach in the storefront cannot read the cardholder data environment (or your customer DB) by default. Exfil controls limit what can leave Google APIs even with stolen credentials.

#### Concepts
- **Separate VPCs or subnets** for CDE vs general (PCI mental model from Part 5) — FW + routing enforce.
- **VPC Service Controls (VPC-SC):** perimeters around projects/services so data cannot be copied to arbitrary projects/internet paths even if IAM is mis-granted. Org-level; diagram required if you cannot enable.
- **Private Service Connect (PSC):** consume services (APIs, published services) via private endpoints without public IPs or full peering mesh.
- **Private Google Access / restricted VIP:** keep API traffic on private paths (ties to 6.2).
- Defense in depth with CMEK / Secret Manager (Part 7) — network is necessary, not sufficient.

#### From scratch / decision exercise
Label Northstar tiers: public FE, private API, private SQL, admin. Which links are PSC vs peering vs Shared VPC?

#### HLD
Northstar network: public frontend (Hosting/LB), private API (no VM public IPs), private Cloud SQL, VPC-SC perimeter sketch around data projects.

#### LLD
- Subnet CIDRs per tier; FW allow only north-south required ports.
- PSC endpoint attachment sketch for a produced API.
- VPC-SC perimeter dry-run mode literacy (prefer dry-run before enforce).

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ HLD + Terraform sketches REQUIRED. Live VPC-SC needs org    │
│ policy admin — credits/org-optional. Free path: two subnets │
│ + FW segmentation on custom VPC (extend 6.5).               │
└─────────────────────────────────────────────────────────────┘
```

#### Gate
- HLD shows segmented tiers; can explain VPC-SC vs IAM vs FW in one paragraph each; PSC vs peering contrast clear.
### 6.16 DNS and DDoS (security view)

Close the networking block by viewing DNS and DDoS as **attack surfaces** and **managed mitigations**, not only as “make the website resolve.”

#### Concepts
- **Cloud DNS security:** DNSSEC for public zones (authenticity); private zones reduce internet exposure of internal names; monitoring for unexpected record changes.
- **DNS attacks literacy:** cache poisoning (why DNSSEC), zone takeover via dangling CNAME/NS, subdomain takeover on abandoned Hosting/LB IPs — release IPs and delete records together (**6.3**).
- **DDoS:** Google Front End / Maglev absorb many volumetric attacks in front of Cloud Load Balancing. **Cloud Armor** adds L7 / WAF / rate-limit for Application LB. You do not build your own scrubbing center on free tier.
- **Billing awareness:** forwarding-rule hours, NAT hours, Armor policies, idle static IPs — free-tier path avoids standing edge SKUs (use Hosting + Run).
- Pointers: CDN/Armor deep content → **1.4**; LB choice → **1.12**; DNS product → **6.10**.

#### From scratch / decision exercise

| Threat | Control |
|---|---|
| Volumetric flood on public HTTPS | GFE + Armor on Application LB |
| Stolen IAM writes evil DNS A | DNS IAM least privilege + alerts |
| Dangling CNAME to deleted Run | Inventory + delete records with services |
| Internal name leak | Private zones only |

#### HLD
Internet noise → GFE → Armor → LB → backends. DNSSEC on public zone. Private DNS not published.

#### LLD
- Checklist: destroy LB ⇒ release IP ⇒ delete DNS A/AAAA.
- Armor preview policy (rate limit) as credits-optional TF.

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ Checklist drill on paper/TF: create/destroy order for LB+IP │
│ +DNS. No live DDoS testing against Google or third parties. │
│ Credits-optional: Armor rate-limit policy attached to LB.   │
└─────────────────────────────────────────────────────────────┘
```

#### Gate
- Can explain GFE/Armor roles without claiming “GCP is un-DDoS-able”; DNSSEC purpose stated; destroy-order checklist memorized.
## Part 7 — Cybersecurity (concept + GCP offerings)

**Goal:** Secure software systems, not just a green SCC dashboard. Identity, data, runtime, supply chain, detect, respond.

### 7.1 Security principles


Security here is engineering: assumptions, boundaries, and proof — not a green dashboard.

#### Concepts
- **CIA:** confidentiality, integrity, availability — every control names which letter it serves.
- **Least privilege:** identity gets the minimum role on the minimum resource for the minimum time.
- **Defense in depth:** IAM + network + app authz + data encryption + detection — one layer failing must not equal game over.
- **Assume breach:** design for credential leak and malicious insider; detection + containment (7.6–7.8).
- **Zero trust:** authenticate/authorize every request; no “inside VPC = trusted.” IAP and service IAM embody this on GCP.
- **Shared responsibility:** you — IAM, data classification, app code, who can invoke, logging config; Google — physical, hypervisor, and baseline managed-service hardening. Misconfigured public bucket is on you.
- **Well-Architected security/privacy/compliance pillar:** map Northstar ADRs to these themes for PCA.

#### From scratch (required)
- For one Northstar flow (`PlaceOrder`), write a control matrix: threat → CIA → control → residual risk. Table-test that each abuse case from 3.0 evidence pack maps to at least one control.

#### Lab
- Walk Cloud Architecture Center security overview pages; annotate your Part 0 hierarchy with trust boundaries (org/folder/project).

#### Gate
- Control matrix reviewed; can explain shared responsibility for Cloud Run vs GCE guest OS patching in one paragraph.

#### Decision table
| Instinct | Prefer | Avoid |
|---|---|---|
| Trust the VPC | mTLS / IAM / IAP | Flat allow-all firewall |
| Broad Owner role | Custom/predefined least role | Standing org Owner for deploys |
| “Encrypt later” | CMEK/Secret Manager now for secrets | Secrets in env in images |
### 7.2 Identity and access (GCP offerings)

Part 4 taught customer and workload auth. Here you operate **org-scale** identity and access for PCA 3.1.

#### Concepts
- **Cloud Identity / Workspace:** employees and groups — directory source of truth.
- **Cloud IAM:** resource access; predefined vs custom roles; IAM conditions; deny policies; principal access boundary literacy.
- **Identity Platform:** customers (Part 4) — separate plane from employees.
- **IAP:** human access to apps without VPN; still need app authz.
- **WIF / Workforce Federation:** external workloads and external human IdPs without syncing passwords into Google.
- **Privileged Access Manager (PAM):** just-in-time elevation where available — prefer over standing Admin.
- **Groups, not users:** bind roles to groups; break-glass user monitored and rare.

#### From scratch (required)
- Policy Analyzer-style toy: input bindings JSON + principal + resource → effective allow/deny. Tests: group inheritance; deny beats allow; condition false ⇒ no access.

#### Lab
- Export a project policy dump (`gcloud projects get-iam-policy`); run the toy or Policy Analyzer; remove one over-broad binding in Terraform.
- Document break-glass procedure (who, how long, audit).

#### Gate
- No standing user Owner on prod; WIF for CI (4.8); effective-access exercise checked in.

#### Decision table
| Who | Prefer | Avoid |
|---|---|---|
| Employee admin UI | IAP + group role | Public admin + password only |
| CI deploy | WIF | SA keys |
| Customer login | Identity Platform | Recreating IAM users for customers |
| Emergency | Break-glass + PAM/JIT | Shared root passwords |
### 7.3 Data protection

Protect data at rest, in use (as offered), and in logs. Classification drives the control, not the other way around.

#### Concepts
- **Default encryption at rest** on Google Cloud — necessary, not sufficient for custody requirements.
- **CMEK / CSEK / Cloud KMS / Cloud HSM / Cloud EKM:** customer-managed keys when you need key custody, rotation policy, or regulatory “hold your keys.” CSEK rare; HSM/EKM for higher assurance.
- **Secret Manager:** versioned secrets, IAM per secret, rotation — vs env vars (non-secrets) vs Binary Authorization attestations (provenance, not secret storage).
- **Sensitive Data Protection (DLP):** inspect, de-identify, infoTypes, templates — use before BQ/notebook exports and before prompts (9b/9c).
- **GCS:** uniform bucket-level access, public-prevention org policy, VPC-SC for exfil-resistant perimeters (6.15).

#### From scratch (required)
- Envelope-encryption toy: generate data key, “wrap” with a master key in a local file (stdlib Fernet or AES from a vetted lib — **do not invent crypto**). Tests: rotate master → rewrap; decrypt fails with wrong key. Name substitute: KMS + CMEK.

#### Lab (free-tier boxed)
1. Create a KMS key ring/key (KMS Free Tier: note Autokey free-tier nuances on official pricing — destroy unused key versions).
2. CMEK on a GCS bucket **or** encrypt a single field with KMS before SQL insert.
3. Secret Manager for Stripe + DB URLs; access logged; no secrets in Cloud Run env YAML checked into Git.
4. DLP inspect on a **synthetic** order export sample (or local sample payloads if API cost is a concern).

#### Gate
- Secrets inventory exists; CMEK or field encryption path demonstrated; public bucket org policy planned in 7.7; DLP infoTypes listed for PII fields.

#### Decision table
| Data | Prefer | Avoid |
|---|---|---|
| API keys / PSP secrets | Secret Manager + IAM | .env in image |
| Regulated object store | CMEK + uniform access | Public ACL “temporary” |
| Analytics export | DLP de-identify | Raw PII to shared BQ |
### 7.4 Application and API security

OWASP-shaped bugs are how GCP-perfect IAM still loses data. Fix them in the app and in tests.

#### Concepts
- **OWASP API Top 10** mapped onto Cloud Run + Identity Platform + SQL: BOLA/BFLA, broken auth, unconstrained resources, injection, misconfig, SSRF, etc.
- **Input validation & output encoding:** allowlists; parameterized SQL; context-aware HTML/JSON encoding.
- **CSRF** for cookie sessions (4.4); **SSRF** — block link-local / metadata IPs; on GCE disable unnecessary default SA scopes; prefer Cloud Run where metadata model is tighter.
- **GCE metadata** (`169.254.169.254`): classic SSRF target for SA tokens — teach detection and prevention on a **local** vulnerable app only.
- **Hard bans:** no scanning third-party systems; no malware; vulnerable-by-design local apps only (Pedagogy).

#### From scratch (required)
- Deliberately weak local API fixtures: missing object authz, string-built SQL, open redirect. Write exploits **against localhost** then fixes; tests that fail on the weak version and pass on the fixed one.
- SSRF guard: URL parse + deny private/link-local/metadata ranges before `fetch`.

#### Lab
- Re-test Northstar handlers with negative authz matrix (4.9 L1).
- Parameterized queries only on Part 2 schema; fuzz one endpoint with bounded corpus.

#### Gate
- Weak fixtures not deployed; authz matrix green; SSRF guard tested; no production scan tooling aimed outside your project.

#### Decision table
| Risk | Prefer | Avoid |
|---|---|---|
| Object authz bugs | Explicit `(principal, action, resource)` checks | “Hidden URL” security |
| SQL injection | Bound parameters | String concat |
| SSRF | Allowlist egress / block metadata | Fetch user URLs raw |
### 7.5 Workload and supply chain

If the build pipeline lies, runtime IAM cannot save you. Provenance and minimal runtime privilege are required.

#### Concepts
- **Artifact Registry:** store images; enable vulnerability scanning; promote digests, not `:latest` alone.
- **Binary Authorization:** admit only attested images to GKE/Cloud Run (as supported); attestations from Cloud Build.
- **SLSA:** levels as a maturity story — hermetic builds, provenance, verified source.
- **Shielded VM / Secure Boot / vTPM:** GCE integrity literacy for bastions and stateful VMs.
- **Container contract:** non-root, read-only root FS, drop capabilities, no secret files in layers (Part 1.2 / D5).

#### From scratch (required)
- Makefile/`cosign`-shaped toy: hash a tarball; write `attestation.json` with builder id + source commit; verifier checks hash + builder allowlist. Tests: tampered artifact fails.

#### Lab (free-tier boxed)
1. Build Northstar image to Artifact Registry (0.5 GB free storage — prune).
2. Scan image; **fail the build** on CRITICAL (policy in Cloud Build).
3. Document Binary Authorization plan for GKE path (9.2); Cloud Run digest pins in Terraform.
4. Prove image runs as non-root in Cloud Run/local.

#### Gate
- CRITICAL fails CI; digest pinned in deploy config; attestation toy green; no SA keys in image layers (`docker history` / scan).

#### Decision table
| Stage | Prefer | Avoid |
|---|---|---|
| Store | Artifact Registry + scan | Random Docker Hub prod pulls |
| Deploy | Digest + BinAuth/attestation | Mutable `:latest` only |
| Runtime | Non-root, RO FS | Root + docker.sock |
### 7.6 Detection and posture
GCP offerings:
- **Cloud Audit Logs** (admin, data access, system).
- **Security Command Center** (Standard / Premium / Enterprise) — findings, mute rules, attack path, security health analytics.
- **Web Security Scanner**.
- **Cloud IDS**.
- **Google SecOps / Chronicle** (concept; cost).
- **Assured Workloads** (compliance perimeters).

**SCC runbook template (copy into Northstar `runbooks/scc.md`):**
1. **Detect:** SCC finding or log-based alert fires (`category`, `severity`, `resourceName`).
2. **Triage (15 min):** confirm resource project/folder; check mute rules; ask “active exploit vs misconfig?”
3. **Contain:** IAM deny / remove public ACE / disable key / close firewall; snapshot disks if GCE compromise suspected.
4. **Eradicate:** fix Terraform; rotate secrets; redeploy clean revision.
5. **Recover:** verify SLO; re-enable traffic canary.
6. **Lessons:** file finding → ticket; add regression test or org policy; update mute only with justification.
- **Lab:** parse audit logs; alert on `SetIamPolicy` and `serviceAccount.keys.create`. Wire one SCC-style finding (even exported JSON) through the template. **Python / Go.**

### 7.7 Org policy and landing zone
- `iam.disableServiceAccountKeyCreation`, `compute.vmExternalIpAccess`, resource locations, uniform bucket access, `sql.restrictPublicIp`, domain restricted sharing as applicable.
- Security baseline for orgs created after 2024-05-23.
- Landing zone: identity, hierarchy, network, security — now you have the product to put in it.

**Org policy change runbook template (`runbooks/org-policy.md`):**
1. **Propose:** policy constraint + desired value + blast radius (org/folder/project).
2. **Dry-run:** list resources that would violate; owners notified.
3. **Stage:** apply at folder `nonprod` first; break-glass project tagged.
4. **Enforce:** promote to `prod` folder; monitor SCC / Policy Controller rejects for 72h.
5. **Rollback:** keep previous policy JSON in Git; `gcloud org-policies set-policy` from last good.
- **Lab:** write Terraform `google_org_policy_policy` for key-creation disable + uniform bucket access (apply only if you own an org; otherwise plan-only).

### 7.8 Incident response
**Four required runbook templates** (same headings: Detect → Contain → Eradicate → Recover → Comms → Follow-up):

1. **Leaked GitHub token / WIF misbind** — revoke OAuth/PAT; invalidate WIF attribute conditions; rotate; audit `CreateServiceAccountKey` / GitHub Actions logs; notify if repo public.
2. **Leaked Stripe webhook secret** — roll secret in Stripe + Secret Manager versions; reject old signing secret; replay-safe inbox check; customer impact = none if only signing secret.
3. **Public bucket / public object ACE** — remove `allUsers`; enable uniform access + org policy; scan object listing; SDP if PII; customer notification if exposure confirmed.
4. **Compromised SA** — disable SA; kill keys; check last auth in audit logs; rotate workloads to new SA; forensics on caller IP / `principalEmail`.

- **Tabletop:** 60 min clock; facilitator injects one of the four; scribe fills the template; grade = time-to-contain + whether restore was tested.
- **Exercise:** commit all four runbooks next to Northstar; run one tabletop.

### 7.9 Compliance mapping

Compliance is evidence + scope + location — mapped onto controls you already built — not a sticker on the README.

#### Concepts
- **Commercial / privacy:** PCI (Part 5), PII handling, SOC 2 / ISO 27001 evidence posture (your logs, access reviews, change control).
- **Healthcare / children’s / sovereignty:** HIPAA BAA with Google; Assured Workloads; `resourceLocations` org policy; children’s data extra care — do not invent legal advice; map to products.
- **Evidence:** Cloud Audit Logs retained; access reviews; Compliance Reports Manager for **Google’s** attestations vs **your** control evidence.
- **PCA 3.2** themes: legislation classes; PCI/PII; SOC 2; audits/logs.

#### From scratch (required)
- Compliance matrix spreadsheet/markdown: obligation → Northstar control → GCP product → evidence artifact path → gap. Unit-ish test: required rows present (PCI, PII, residency, audit).

#### Lab
- Pull or screenshot Compliance Reports Manager path (org-dependent); store procedure in `runbooks/compliance.md`.
- Set (or plan-only Terraform) `resourceLocations` for a nonprod folder.

#### Gate
- Matrix complete for PCI + PII + residency; no “we’ll be careful” as a PHI plan; audit log retention called out in 10.0/7.6.

#### PCA: 3.2 Compliance design

**Guide themes (matrix):** health/children’s/privacy/sovereignty legislation; PCI/PII commercial; SOC 2; audits/logs. Homes: 5, 7.9.

| Obligation | Prefer | Accept |
|---|---|---|
| PHI | BAA + Assured Workloads / location policy | DIY “we’ll be careful” |
| PCI | Tokenize; CDE segmentation (Part 5) | Store PAN in GCS |
| Sovereignty | `resourceLocations` + regional resources | Global bucket “for simplicity” |
| Evidence | Audit logs retained + access reviews | Screenshots only |

**Scenario prompt:** EU autonomous-driving data and a US analytics team want one global BQ dataset.

**Expected answer shape:** “I pick EU regional processing + Assured Workloads because Y, I accept Z (aggregated non-personal exports only).”
## Part 8 — HLD/LLD mastery (Donne Martin → GCP)

Every Donne Martin building block becomes a GCP decision table plus a Northstar ADR. Primer 4-step loop is already Pedagogy §4; the full six-step protocol (NFRs, capacity, Mermaid HLD, LLD, failures, hardening) is Pedagogy §8. **Every HLD/LLD lab uses the 3.0 evidence pack** — one sentence is not enough.

**G19 synthesis:** completing the gated studios below **is** the G19 artifact (unseen DS + API + concurrency from unlocked tools). Appendix G indexes G19; it does not re-teach it. Do not invent a “Part G” semester.

---

### 8.0 Donne Martin → GCP building blocks

| Donne Martin | GCP mapping | Northstar use |
|---|---|---|
| Performance vs scalability | Cloud Run concurrency, min instances, HPA on GKE | p95 vs cheap scale-to-zero |
| Latency vs throughput | region choice, CDN, Firestore locality | checkout vs catalog browse |
| CAP / consistency | Firestore vs Spanner vs Cloud SQL | payments = strong; feed = eventual |
| DNS | Cloud DNS, Firebase domains | custom domain |
| CDN | Cloud CDN, Firebase CDN | static assets |
| L4 / L7 LB | Cloud Load Balancing | GFE |
| Reverse proxy | GFE, Envoy, API Gateway | authn at edge |
| Microservices | Cloud Run services / GKE | bounded contexts |
| Service discovery | Cloud Run URLs, Service Directory, GKE DNS | internal HTTPS |
| RDBMS scaling | Cloud SQL HA, read replicas, AlloyDB | later OLTP |
| NoSQL | Firestore, Bigtable, Memorystore | v0 data |
| Cache patterns | CDN, Memorystore, client cache | catalog |
| Message/task queues | Pub/Sub, Cloud Tasks, Worker Pools | orders |
| REST vs RPC | Cloud Run HTTP vs gRPC | public REST, internal gRPC (Part 3.2) |
| Security | IAM, IAP, Armor, NGFW, KMS, Secret Manager, VPC-SC, SCC | Parts 4, 6, 7 |
| CAP / failover / nines | SLO math (10.1); series vs parallel availability | checkout SLO |
| Consistency patterns | Weak / eventual / strong | Firestore vs Spanner |
| Cache-aside / write-through / write-behind / refresh-ahead | Memorystore (9.1) | catalog |
| Federation / sharding / denorm / SQL tuning | 2.1–2.3 | OLTP |
| BASE / KV / document / wide-column / graph | 2.2, 2.7 | polyglot |
| Back pressure | 8.1 + Pub/Sub outstanding | workers |
| MapReduce / Spark / Storm | Dataflow / Dataproc (9b.1) | recall |
| Bigtable / Dynamo / Redis / Memcached | Bigtable, Memorystore | |
| GFS / HDFS | GCS (2.5) | objects |
| Chubby / ZK | leases 8.1; GKE etcd | |
| Dapper | Cloud Trace (10.0) | |
| Kafka | Pub/Sub (3.4) | |
| Scale-to-millions (primer AWS chapter) | **GCP** global LB + multi-region Run + Spanner/Firestore + CDN — do not teach AWS as the platform | |

#### Performance vs scalability
**Concept:** Performance is single-request latency/resource cost; scalability is how those stay acceptable as load grows. Failure modes: optimizing p50 while p99 burns the error budget; adding min-instances “for speed” and never scale-to-zero; confusing vertical scale with horizontal fan-out.
**Northstar ADR prompt:** Context = catalog browse vs checkout p95 under Black Friday 10×. Decision = Cloud Run concurrency + min instances vs GKE HPA for each path. Consequences = idle cost, cold-start, blast radius, who owns autoscaling knobs.
**From scratch / owned:** already owned at Part 1 (Cloud Run / GCE / App Engine autoscaling) and 1.12; apply here in studio HLD packs, do not re-teach platforms.

#### Latency vs throughput
**Concept:** Latency is time to one answer; throughput is completed work per second. Batching, CDN, and locality raise throughput or cut latency at different layers. Failure modes: saturating a region while chasing global QPS; CDN that helps catalog but poisons personalized checkout; measuring only server time and ignoring client RTT.
**Northstar ADR prompt:** Context = checkout (strict latency) vs catalog browse (throughput). Decision = region pinning, Cloud CDN on static/catalog, Firestore locality vs multi-region. Consequences = consistency lag, cache invalidation, cost of Premium tier.
**From scratch / owned:** already owned at Part 1.4 (CDN) and 6.13 (LB); back-of-envelope powers-of-two from Part 0.

#### CAP / consistency
**Concept:** Under partition you choose availability or consistency; latency and operational complexity are the usual trade currency. Failure modes: claiming “CP” while serving stale caches; dual-writes without a truth store; using eventual feed semantics for payment capture.
**Northstar ADR prompt:** Context = payment ledger vs social feed. Decision = Cloud SQL/Spanner (strong) vs Firestore eventual for which aggregates. Consequences = failover behavior, conflict resolution, SLO wording.
**From scratch / owned:** already owned at Part 2 (Cloud SQL, Firestore, Spanner map); deepen with studio linearizable-KV / Raft toys.

#### DNS
**Concept:** Name → address with TTL, authority, and failure domains. Failure modes: ephemeral A records, split-horizon surprises, TTL too long for cutover, missing CAA/HTTPS redirect plan.
**Northstar ADR prompt:** Context = `shop.northstar.dev` cutover. Decision = Cloud DNS public zone + Firebase/Hosting vs GCLB static IP. Consequences = TTL drain, dual-run, rollback DNS.
**From scratch / owned:** already owned at 6.10; recursive stub toy lives there.

#### CDN
**Concept:** Pull-through edge cache keyed by URL/headers; cuts origin load and RTT. Failure modes: caching personalized or auth responses; missing `Vary`; invalidation lag; treating CDN as a write path.
**Northstar ADR prompt:** Context = catalog assets + storefront HTML. Decision = Cloud CDN on HTTPS LB vs Firebase CDN; cache keys and TTLs. Consequences = purge cost, stale SKUs, signed-URL needs.
**From scratch / owned:** already owned at 1.4; in-process LRU studio here is the app-tier analog, not a second CDN course.

#### L4 / L7 LB
**Concept:** L4 forwards connections; L7 routes on HTTP semantics, TLS, and policies. Failure modes: sticky sessions hiding bad design; idle reserved IPs; health-check flaps; using L4 when you need path-based auth at the edge.
**Northstar ADR prompt:** Context = public storefront + internal admin. Decision = external HTTPS LB (L7) vs internal LB; Serverless NEG to Cloud Run. Consequences = TLS termination, Armor attachment, IP billing (6.3).
**From scratch / owned:** already owned at 6.13 + Pedagogy reverse-proxy toy; do not re-teach Maglev/GFE.

#### Reverse proxy
**Concept:** Edge hop that terminates TLS, routes, and injects policy (authn, rate limit, headers). Failure modes: trusting `X-Forwarded-*` from the internet; proxy as the only authz; buffering that breaks streaming.
**Northstar ADR prompt:** Context = where Identity Platform / IAP / API Gateway sit relative to Cloud Run. Decision = GFE+IAP for admin, app middleware for public API. Consequences = hop count, header trust boundary, who owns CORS.
**From scratch / owned:** already owned at Pedagogy §6 reverse-proxy toy + Part 4.2 middleware.

#### Microservices
**Concept:** Independently deployable bounded contexts with clear data ownership. Failure modes: distributed monolith, shared DB, chatty sync joins, nano-services without operability.
**Northstar ADR prompt:** Context = catalog/cart/order/payment split criteria. Decision = stay modular monolith until which force appears; first extract. Consequences = saga/outbox need, on-call surface.
**From scratch / owned:** already owned at Part 3.0–3.1.

#### Service discovery
**Concept:** How callers find healthy instances without hard-coded IPs. Failure modes: DNS caching past drain; client-side lists without health; cross-project URL sprawl.
**Northstar ADR prompt:** Context = order → payment internal HTTPS. Decision = Cloud Run service URL + IAM invoker vs Service Directory vs GKE DNS. Consequences = mTLS/identity, regional failover.
**From scratch / owned:** already owned at Part 3.2 / Cloud Run wiring.

#### RDBMS scaling
**Concept:** Vertical scale, replicas, sharding/federation, and connection math before “just add Spanner.” Failure modes: read-replica lag treated as strong read; `max_connections` exhaustion; cross-shard joins.
**Northstar ADR prompt:** Context = OLTP order DB growth. Decision = Cloud SQL HA + replicas vs AlloyDB vs Spanner. Consequences = cost, consistency, migration pain.
**From scratch / owned:** already owned at 2.1–2.3; connection-pool math recalled in 8.1 table.

#### NoSQL
**Concept:** Document/KV/wide-column when access patterns beat relational generality. Failure modes: treating Firestore as a SQL dump; hot keys; missing multi-doc transaction boundaries.
**Northstar ADR prompt:** Context = v0 catalog + sessions + feed fanout. Decision = Firestore vs Bigtable vs Memorystore for each. Consequences = query limits, cost, consistency.
**From scratch / owned:** already owned at 2.2, 2.4, 2.7; KV studios deepen mechanics.

#### Cache patterns
**Concept:** Where data is served from memory/edge vs origin; aside/through/behind/refresh-ahead change write visibility. Failure modes: stampede, stampedes after deploy, inconsistent dual source of truth.
**Northstar ADR prompt:** Context = catalog SKU reads. Decision = CDN + Memorystore cache-aside vs write-through. Consequences = invalidation, stampede controls (8.1 singleflight).
**From scratch / owned:** LRU + singleflight studios here; Memorystore product depth at 9.1 — one-line recall when wiring labs.

#### Message / task queues
**Concept:** Async handoff for durability, smoothing, and fan-out. Failure modes: using a queue as a DB; poison without redrive; at-least-once without idempotency.
**Northstar ADR prompt:** Context = `OrderPlaced` side effects. Decision = Pub/Sub vs Cloud Tasks vs Worker Pools. Consequences = ordering, delay, DLQ ownership (3.4–3.5).
**From scratch / owned:** already owned at 3.4–3.5; crawler studio reuses the pattern.

#### REST vs RPC
**Concept:** Public JSON/HTTP for browsers/partners; internal gRPC for typed, efficient s2s. Failure modes: exposing gRPC to browsers without a BFF; REST chatty N+1; protobuf breaking changes without field discipline.
**Northstar ADR prompt:** Context = storefront BFF vs order→inventory. Decision = public REST, internal gRPC on Cloud Run. Consequences = codegen, deadlines, error model (3.2).
**From scratch / owned:** already owned at Part 3.2.

#### Security
**Concept:** Identity, authz, edge abuse controls, secrets, and detection as architecture — not a checklist after HLD. Failure modes: authn without object authz; SA keys; open admin UI; secrets in images.
**Northstar ADR prompt:** Context = public API + admin + workers. Decision = IAM/IAP/Armor/NGFW/KMS/Secret Manager/VPC-SC bindings per surface. Consequences = blast radius, audit, PCI adjacency.
**From scratch / owned:** already owned at Parts 4, 6, 7 — apply in every studio evidence pack.

#### CAP / failover / nines
**Concept:** Availability compounds in series and parallel; error budgets turn nines into change policy. Failure modes: marketing “five nines” without dependency math; failover that fails DNS/TLS/data.
**Northstar ADR prompt:** Context = checkout SLO. Decision = multi-region active/active vs active/passive; RPO/RTO. Consequences = cost, consistency, runbooks (10.1).
**From scratch / owned:** SLO math owned at 10.1; compute series/parallel availability napkin here in scale HLD.

#### Consistency patterns
**Concept:** Weak, eventual, and strong reads/writes — and which UX can tolerate which. Failure modes: read-your-writes broken by replica lag; “eventual” without convergence story.
**Northstar ADR prompt:** Context = cart vs payment capture vs feed. Decision = per-aggregate consistency class and product. Consequences = conflict UX, support cost.
**From scratch / owned:** Part 2 + linearizable KV / Raft toys in this Part.

#### Cache-aside / write-through / write-behind / refresh-ahead
**Concept:** Who writes cache vs store and when refresh happens. Failure modes: write-behind loss on crash; aside without TTL/stampede policy; refresh-ahead storms.
**Northstar ADR prompt:** Context = catalog. Decision = aside + singleflight vs through for admin writes. Consequences = durability, complexity (9.1).
**From scratch / owned:** implement aside in LRU/KV studios; product wiring at 9.1.

#### Federation / sharding / denorm / SQL tuning
**Concept:** Split data by domain or key; denormalize for read paths; tune indexes/queries before new products. Failure modes: premature shards; unbounded denorm drift; `OFFSET` pagination.
**Northstar ADR prompt:** Context = order history growth. Decision = partition keys, denorm projections, cursor pager (8.1). Consequences = rebalance, backfill.
**From scratch / owned:** already owned at 2.1–2.3; cursor pager required from-scratch in 8.1.

#### BASE / KV / document / wide-column / graph
**Concept:** Polyglot persistence matched to access patterns, not fashion. Failure modes: one DB for all; graph queries forced into documents; wide-column without key design.
**Northstar ADR prompt:** Context = Northstar polyglot map. Decision = which store per bounded context. Consequences = ops skill tax, joins across stores.
**From scratch / owned:** already owned at 2.2, 2.7; social-graph HLD pack here.

#### Back pressure
**Concept:** Slow consumers must slow producers or shed load — unbounded queues become outage amplifiers. Failure modes: infinite Pub/Sub backlog treated as success; thread-pool exhaustion without 503.
**Northstar ADR prompt:** Context = order workers under spike. Decision = Pub/Sub outstanding caps + Cloud Run concurrency + load-shed (8.1). Consequences = retry storms, DLQ growth.
**From scratch / owned:** load-shed + rate-limiter studios here; Pub/Sub semantics at 3.4.

#### MapReduce / Spark / Storm
**Concept:** Batch/stream parallel compute with shuffle. Failure modes: reinventing Dataflow for one job; ignoring shuffle cost; exactly-once myths.
**Northstar ADR prompt:** Context = nightly sales rank / recall features. Decision = toy MapReduce then Dataflow/Dataproc (9b.1). Consequences = ops vs flexibility.
**From scratch / owned:** MapReduce **toy** studio in this Part; managed recall at 9b.1 — do not move 9b content here.

#### Bigtable / Dynamo / Redis / Memcached
**Concept:** Wide-column vs KV cache/store trade-offs (latency, durability, data model). Failure modes: Redis as system of record; Bigtable without row-key design; Memcached without stampede plan.
**Northstar ADR prompt:** Context = session/catalog/hot counters. Decision = Memorystore vs Bigtable vs Firestore. Consequences = persistence, cost, clustering.
**From scratch / owned:** KV + LRU studios; product labs when 9.1 / Bigtable unlocked — paper ADR allowed earlier.

#### GFS / HDFS
**Concept:** Object/blob stores for immutable large objects and sequential throughput. Failure modes: using GCS as a low-latency mutex; missing generation preconditions; unbounded listing.
**Northstar ADR prompt:** Context = paste blobs, crawl warc, photo originals. Decision = GCS classes + lifecycle. Consequences = cost, consistency of overwrite (2.5).
**From scratch / owned:** already owned at 2.5; studios attach objects, do not re-teach GCS.

#### Chubby / ZK
**Concept:** Coordination via leases/locks with fencing — not a general DB. Failure modes: Redis `SETNX` as truth; lock without fence token; long critical sections.
**Northstar ADR prompt:** Context = leader for crawler or ID worker assignment. Decision = lease + fencing toy (8.1) vs Spanner/etcd at GKE. Consequences = split-brain, ops burden.
**From scratch / owned:** leases/fencing in 8.1; Raft toy is consensus literacy, **not** production etcd.

#### Dapper
**Concept:** Distributed tracing propagates context across hops. Failure modes: logs without trace ids; tracing secrets; sampling that hides rare failures.
**Northstar ADR prompt:** Context = checkout path spans. Decision = Cloud Trace + OpenTelemetry propagation. Consequences = cost, PII in spans (10.0).
**From scratch / owned:** already owned at 1.7 / 10.0; every studio ships redacted request ids.

#### Kafka
**Concept:** Durable ordered log for pub/sub and event streaming. Failure modes: “Kafka on GCE” without ops story; ordering keys that hot-partition; treating Pub/Sub exactly-once as free.
**Northstar ADR prompt:** Context = domain events. Decision = Pub/Sub (3.4) unless a hard Kafka constraint appears. Consequences = ordering, replay, cost.
**From scratch / owned:** already owned at 3.4; do not stand up Kafka in this Part.

#### Scale-to-millions (primer AWS chapter → GCP)
**Concept:** Global edge + regional compute + appropriate data plane + cache + async — on **GCP**, not an AWS port. Failure modes: copying AWS service names; multi-region without data story; ignoring quotas/SKUs.
**Northstar ADR prompt:** Context = Northstar “millions of users” napkin. Decision = global HTTPS LB + multi-region Cloud Run + Spanner/Firestore + CDN + Pub/Sub. Consequences = cost, consistency, multi-DC runbooks (evidence HLD below).
**From scratch / owned:** evidence-pack HLD in this Part; platforms already owned in Parts 1–3, 6.

---

### 8.A Gated studios — implemented (required before Part 11)

Each studio below carries **all six density blocks**. Python stdlib first; Go after submit with the **same** tests. Package names are mandatory for gates.

#### 8.A.1 Pastebin / Bitly (shortlink + paste)

**Concept:** Map a short opaque id to a URL or paste blob; reads dominate; writes must not collide; abuse and expiry matter. Failure modes: sequential ids (enumeration), no rate limit, storing secrets in URLs, missing hash collision plan, GCS without generation preconditions.

**From scratch:** Package `shortlink` (Python) then `shortlink` (Go).
- Base62 (or hash-truncate) id from crypto-random bits; reject guessable counters.
- In-memory map + optional file WAL for `(id → target|blob_meta, created, expiry)`.
- HTTP: `POST /v1/links` `{url}` → `{id}`; `GET /v1/{id}` → 302 or paste body; `DELETE` owner-only stub.
- Tests: collision resistance smoke; expiry; idempotent create with `Idempotency-Key`; reject javascript: URLs; concurrent creates; table-driven Base62 round-trip.
- Go: same API surface; `net/http`; race-test map with `-race`.

**HLD:** C4 context/container Mermaid: client → Cloud Run API → Firestore metadata → GCS object (pastes) / redirect. NFRs: p95 redirect < 100 ms warm; durability of mapping; abuse QPS. ADR: opaque id vs hash(url); Firestore vs SQL for metadata.

**LLD:** OpenAPI paths above; Firestore doc schema `{id,url,owner,exp,hash}`; GCS object name `pastes/{id}`; IAM: Run SA `datastore.user` + `storage.objectAdmin` on one bucket; Terraform: `google_cloud_run_v2_service`, `google_firestore_database`, `google_storage_bucket` (uniform access). Errors: 400 bad URL, 404 unknown, 409 idempotency conflict, 429. Idempotency: key → stored id.

**GCP lab (free-tier boxed):** Deploy API to Cloud Run; Firestore Native; GCS bucket for paste bodies > 1 KiB. Custom domain optional (**credits-optional**). `gcloud run deploy` + Terraform plan required even if apply is deferred. Tear down bucket objects same sitting.

**Gate:** Unseen — design collision handling when truncating SHA-256 to 48 bits; estimate birthday risk. Nearby transfer — add “custom alias” with uniqueness constraint without sequential scan.

#### 8.A.2 Query-cache / KV + consistent hash

**Concept:** Partition keys across N cache nodes; consistent hashing minimizes remap on node add/remove. Failure modes: no vnodes (hot spots), ignoring remapped keys on deploy, treating cache as source of truth, thundering herd on miss.

**From scratch:** Package `hashring` + `kvcache` (Python then Go).
- Ring with virtual nodes; `get/set/delete`; plot or assert % keys moved on +1/−1 node.
- Optional singleflight on miss (or depend on 8.1 singleflight once unlocked).
- Tests: determinism; remap bound with vnodes; exhausted TTL; concurrent get-or-load.
- Go: `hashring` package; benchmarks for lookup (**G8–G9** hook).

**HLD:** Mermaid: API → ring → Memorystore nodes (prod) / local processes (toy). NFRs: remap < X% on one node loss; p99 get. ADR: vnode count; Firestore as origin vs Memorystore-only ephemeral.

**LLD:** Interface `Cache { Get, Set, Delete }`; key encoding; IAM for Memorystore when live; Terraform shape `google_redis_instance` (**credits-optional** live — paper+emulator OK). Errors: 503 shed; origin timeout. Idempotent Set.

**GCP lab:** Local multi-process ring first. Optional Memorystore (**credits-optional**, destroy after). Firestore as origin for one entity type.

**Gate:** Unseen — given vnode histogram skew, propose fix. Nearby — wire catalog SKU cache-aside without dual-write bugs.

#### 8.A.3 Rate limiter (token bucket)

**Concept:** Bound accepted work per key (IP, user, API key) to protect dependency SLOs. Failure modes: global lock bottleneck; only client-side limits; no `Retry-After`; limiter state loss on multi-instance without shared store.

**From scratch:** Package `ratelimit` (Python then Go). Token bucket and/or sliding window; middleware wrapping the Part 4.2 server shape. Tests: burst then deny; refill math; per-key isolation; concurrent take; clock inject. Go race-test.

**HLD:** Where enforced (edge Armor vs app vs gateway). NFRs: false allow under multi-instance; fairness. ADR: in-process vs Memorystore vs Armor policy for public API.

**LLD:** Middleware signature; headers `X-RateLimit-*`, `Retry-After`; Terraform Armor rule sketch (**credits-optional** apply). Errors: 429 only on limit; never 500 for empty bucket. Idempotency orthogonal — do not consume tokens twice on replay of a settled write if your policy says so (document it).

**GCP lab:** In-process on Cloud Run (document multi-instance hole); optional Armor rate limit (**credits-optional**). Free-tier: local + Cloud Run without Armor is enough for gate.

**Gate:** Unseen — two instances without shared state; attacker rotates IPs. Nearby — combine with load-shed (8.1) under queue depth.

#### 8.A.4 LRU cache (+ OOD hash map / circular array)

**Concept:** Bounded in-process cache with O(1) get/put via hash map + doubly linked list (or circular buffer of slots). Failure modes: unbounded dict; caching personalized data without keying tenant; using LRU as distributed cache.

**From scratch:** Packages `lru` and `hashmap` (Python then Go).
- Hash map from scratch (chaining or open addressing) with tests for overwrite, delete, grow.
- LRU on top; optional circular array lab for ring buffer of recent keys/events (fixed capacity, overwrite oldest).
- HTTP middleware optional: cache GET by path+auth principal hash.
- Tests: capacity eviction order; update moves to front; concurrent LRU with mutex (Go `-race`).

**HLD:** When in-process LRU vs CDN vs Memorystore. NFRs: hit ratio target; memory cap. ADR: document replacement boundary.

**LLD:** Interface; metrics hits/misses; no IAM. Terraform: none for pure library — attach to Cloud Run service already used.

**GCP lab:** Ship as library in Pastebin or catalog service; prove eviction under load test. No paid cache required.

**Gate:** Unseen — implement `GetOrLoad` without stampede (hook singleflight). Nearby — circular array for “last N events” debug endpoint. **OOD:** hash map + LRU + circular array are the code labs; skip parking-lot/cards (one-line: those OOD exercises are out of scope unless a Northstar force appears).

#### 8.A.5 Web crawler

**Concept:** Fetch URLs, respect politeness, extract links, store raw content, avoid cycles. Failure modes: infinite crawl; ignoring robots; unbounded concurrency; storing secrets from pages; no checkpoint.

**From scratch:** Package `crawler` (Python then Go). Frontier queue; seen set (bloom optional from 8.1); per-host token bucket; fetcher with timeouts/size caps; writer to files. Tests: cycle; politeness delay; content-type allowlist; checkpoint resume. Go: `net/http` client policies from Part 4.2 outbound rules (SSRF allowlist for lab hosts only).

**HLD:** Mermaid: Cloud Run Job / worker pool → Pub/Sub frontier → GCS raw → optional indexing later. NFRs: pages/hour; politeness; cost cap. ADR: Jobs vs always-on workers; Pub/Sub vs Tasks.

**LLD:** Message schema `{url,depth,dedup_key}`; GCS `gs://…/raw/{hash}`; IAM: Job SA objectCreator + pubsub subscriber; Terraform: `google_cloud_run_v2_job`, topic/sub, bucket. Errors: retryable fetch vs poison to DLQ. Idempotency: dedup_key uniquely processed.

**GCP lab (free-tier boxed):** Local crawl of a tiny static fixture server first. Then Pub/Sub + GCS + Cloud Run Job on a **self-owned** fixture. **Credits-optional:** Scheduler trigger. Tear down.

**Gate:** Unseen — design checkpoint so a killed job does not re-fetch entire corpus. Nearby — add bloom negative cache for seen URLs (8.1).

#### 8.A.6 Unique IDs — Snowflake-style

**Concept:** Time-ordered unique ids without a central `ORDER BY now()` bottleneck: timestamp | worker | sequence. Failure modes: clock rewind; worker-id collision; sequence overflow; using DB autoincrement across shards without plan.

**From scratch:** Package `snowflakeid` (Python then Go). Configurable epoch, bit layout; reject rewind or wait; overflow error. Tests: monotonic per worker; uniqueness under concurrency; simulated clock backstep; parse components. Go: atomic sequence; benchmark allocs (**G8–G9**).

**HLD:** Who assigns worker ids (config vs lease). NFRs: ids/sec/worker; skew tolerance. ADR: Snowflake vs ULID vs DB sequence vs Firestore alloc — “I pick X because Y.”

**LLD:** `NextID() (int64, error)`; API exposes string form; IAM if worker registration store used; Terraform optional for config map. Errors: `ErrClockRewind`, `ErrWorkerUnassigned`. Idempotency: ids are create-time, not request replay tokens — keep `Idempotency-Key` separate.

**GCP lab:** Cloud Run multi-instance: assign worker id from instance metadata hash **or** small Firestore lease (document split-brain risk). Prefer single-region. Free-tier friendly.

**Gate:** Unseen — bit layout for 10k ids/sec and 100 workers; prove overflow time. Nearby — sort feed by snowflake id instead of `now()`.

---

### 8.B Toy distributed systems (local; not production consensus products)

#### 8.B.1 MapReduce toy

**Concept:** Map → shuffle by key → reduce; parallelism and failure restart at task grain. Failure modes: non-deterministic map; huge hot keys; treating toy as Dataflow.

**From scratch:** Package `mapreduce` (Python then Go). Word-count on local files; spill intermediate files; deterministic reduce order. Tests: empty input; single key; crash mid-map with rerun. **Then recall** Dataflow/Dataproc at 9b.1 — do not re-teach pipelines here.

**HLD:** Paper Mermaid comparing toy to Dataflow job for sales-rank batch. NFRs: throughput on one machine. ADR: when to stop at toy.

**LLD:** Function signatures `Map(k,v)→[]KV`, `Reduce(k,[]v)→[]KV`; no GCP IAM required for toy.

**GCP lab:** None required live; optional upload inputs to GCS and run local MR (**free-tier** storage). Mark Dataflow apply **credits-optional**.

**Gate:** Unseen — skew key straggler mitigation idea. Nearby — sales-rank HLD uses this mental model.

#### 8.B.2 Linearizable KV (single-node log + apply)

**Concept:** Linearizability via a single leader log: append → apply → ack. Failure modes: acknowledging before apply; dual writers; confusing with Redis.

**From scratch:** Package `linKV` (Python then Go). WAL + state machine (`Put`/`Get`); restart replay. Tests: crash recovery; concurrent clients serialized; fencing token on writer. May reuse Pedagogy §6 KV/WAL shape.

**HLD:** Contrast with Spanner TrueTime / Firestore — literacy only. ADR: why Northstar payments do not use this toy.

**LLD:** Client API; log record schema; file permissions local.

**GCP lab:** Local only. Point at Cloud SQL/Spanner as production stand-in (already owned Part 2).

**Gate:** Unseen — show a history that is sequential but not linearizable, then fix. Nearby — Raft studio extends to 3 replicas.

#### 8.B.3 Raft toy (3 processes — NOT etcd/production)

**Concept:** Leader election + log replication under crash/partition at **toy** scale. Failure modes: election storms; committing without quorum; pretending this is production lock service.

**From scratch:** Package `toyraft` (Python then Go). 3 OS processes or goroutines with lossy channels; RequestVote/AppendEntries; persist term/vote/log. Tests: elect leader; replicate; minority partition cannot commit; leader crash re-elect. **Skip-test 12.S20** if this gate confirmed. Do **not** run etcd or claim production consensus.

**HLD:** One Mermaid state diagram; NFR = learning only. ADR: production coordination → Spanner/etcd on GKE / leases — not this package.

**LLD:** RPC messages; on-disk record; no Terraform.

**GCP lab:** Local processes only. Optional: observe GKE etcd **as a product mention**, not a lab to reconfigure.

**Gate:** Unseen — draw what happens when network heals with divergent logs (toy resolution rules). Nearby — fencing tokens (8.1) vs Raft leadership.

---

### 8.C Evidence-pack HLDs (full packs; paper + sequences OK)

Each item is a **full 3.0 evidence pack**: requirements, assets/actors/trust/abuse/authz, capacity napkin, Mermaid C4 HLD, LLD/API/schema sketches, bottleneck/failure/security table, trade-offs, ADR, observability, rollback. Implementation may be thin slice or paper+sequences; if coded, Python then Go. Feed **ML ranking detail** → **9c.2** (one sentence); the HLD pack lives **here**.

#### 8.C.1 Twitter-like feed

**Concept:** Home timeline mixes followed authors’ posts under read-heavy load; fanout-on-write vs fanout-on-read vs hybrid. Failure modes: celebrity hot keys, unread backlog, ranking treated as “sort by time” forever, caching personalized timelines at CDN.

**From scratch:** Package `hldfeed` optional thin slice — merge precomputed timeline + live posts for one user (in-memory). Or paper pack + sequence diagrams explicitly marked. Tests if coded: merge order; empty follow set; celeb path stub.

**HLD:** C4/Mermaid: ingest → post store → fanout workers → timeline store → read API; CDN only for media. NFRs: p95 read, write amplification, stale window. ADR: fanout mode; Firestore vs Bigtable for timelines. Ranking/ML detail → **9c.2**.

**LLD:** `POST /posts`, `GET /timeline?cursor=`; schema `{post_id,author,ts,text}`; IAM Run invoker; Terraform shape Run + Pub/Sub + Firestore/Bigtable. Errors: 404 post, 429; idempotent create with key.

**GCP lab:** Free-tier: Cloud Run + Firestore timeline for N≤100 users. Multi-region / Bigtable **credits-optional**.

**Gate:** Unseen — 10× celeb fanout; pick hybrid and defend. Nearby — Northstar “followers get order-shipped notifications” fanout.

#### 8.C.2 Social graph

**Concept:** Directed follow edges, privacy, and traversal for fanout and recommendations. Failure modes: undirected assumptions, enumerating private graphs, hotspot hubs, graph DB without ops story.

**From scratch:** Package `hldgraph` — adjacency lists + “friends-of-friends” one hop on files; or paper pack. Tests: cycle follow; block list; degree histogram.

**HLD:** Mermaid edge service vs embed edges in user doc. NFRs: follow QPS, traverse latency. ADR: Firestore edges vs dedicated graph product (usually stay Firestore/SQL here).

**LLD:** `POST /follow`, `DELETE /follow`, `GET /followers?cursor=`; composite keys; IAM; Terraform Firestore indexes. Idempotent follow.

**GCP lab:** Firestore edge docs free-tier. **Credits-optional:** Spanner for strong multi-region graph.

**Gate:** Unseen — mutual-follow privacy. Nearby — catalog “related SKUs” graph lite.

#### 8.C.3 Sales rank

**Concept:** Periodic ranking of SKUs by sales with online serve of top-k. Failure modes: ranking on raw counts without window; hot SKU write skew; serving stale rank as stock truth.

**From scratch:** Reuse `mapreduce` toy on order logs → rank file; package `salesrank` serve top-k. Or paper + MR sequence.

**HLD:** Batch Dataflow/MR → GCS artifact → Memorystore/Firestore serve. NFRs: freshness SLA, compute cost. ADR: batch vs continuous; tie to 9b.1 recall for managed.

**LLD:** `GET /ranks?category=`; object generation precondition; IAM objectViewer; Terraform Job/Scheduler shape. Idempotent batch replace.

**GCP lab:** Local MR + GCS upload free-tier. Dataflow apply **credits-optional**.

**Gate:** Unseen — mid-window refund adjustments. Nearby — Northstar bestseller strip.

#### 8.C.4 Scale-to-millions on GCP

**Concept:** Edge + regional compute + data plane + cache + async sized for millions of users **on GCP** (not AWS service mapping). Failure modes: multi-region without data story; ignoring quotas; idle global IPs; “just add GKE.”

**From scratch:** Paper pack required: capacity napkin (Part 0 numbers), dependency graph, failure table. Optional: k6/hey script against local stubs.

**HLD:** Global HTTPS LB + Cloud CDN + multi-region Cloud Run + Spanner or multi-region Firestore + Pub/Sub + Armor sketch. NFRs: availability math, RPO/RTO, cost ceiling. ADR: Spanner vs Firestore; min instances vs cold start.

**LLD:** Terraform module map (LB, Run services, DB, DNS); IAM least privilege diagram; error budgets pointer (10.1).

**GCP lab:** Diagram + Terraform plan; single-region free-tier spike OK. Multi-region Spanner / global LB static IP **credits-optional** and tear down same day (6.3 idle IP warning).

**Gate:** Unseen — region outage + quota exhaustion same week. Nearby — Northstar Black Friday runbook one-pager.

#### 8.C.5 Dropbox-like sync

**Concept:** Client sync of file trees: content-addressed blocks, metadata namespace, conflict policy. Failure modes: checksum mismatches, split-brain clocks, syncing secrets, unbounded version history cost.

**From scratch:** Package `hldsync` — local block chunker + manifest; or paper sequences for upload/download/conflict.

**HLD:** Client → API → metadata DB + GCS blocks; notifications via Pub/Sub. NFRs: resume, dedup ratio. ADR: GCS generations + metadata; conflict = rename vs CRDT (**no CRDT research** — pick rename/last-writer and state it).

**LLD:** Block put with hash name; manifest schema; IAM objectAdmin scoped prefix; Terraform bucket + Run. Idempotent block put by hash.

**GCP lab:** GCS + Firestore manifests free-tier. **Credits-optional:** push notify.

**Gate:** Unseen — two clients offline edit same file. Nearby — Northstar “export invoice PDF” object pipeline.

#### 8.C.6 Chat

**Concept:** Channels, message fanout, presence, history pagination. Failure modes: at-least-once dupes in UI, presence as source of truth, storing messages only in memory, missing authz on channel.

**From scratch:** Package `hldchat` — in-process hub + websocket or long-poll stub + cursor history; or paper pack. Tests: fanout to N members; replay; authz deny.

**HLD:** Mermaid gateway → channel service → history store → Pub/Sub fanout. NFRs: send latency, history retention. ADR: Firestore vs SQL history; WS on Cloud Run caveats.

**LLD:** `POST /channels/{id}/messages`, `GET history?cursor=`; schema; IAM; Terraform Run + Firestore. Idempotency-Key on send.

**GCP lab:** Free-tier Run + Firestore. Load balancer sticky **credits-optional**.

**Gate:** Unseen — member removed mid-fanout. Nearby — Northstar support chat lite.

#### 8.C.7 Instagram-like photos

**Concept:** Upload, async variant generation, CDN read path, feed of media. Failure modes: sync thumbnail in request path, public buckets, huge originals without lifecycle, EXIF PII.

**From scratch:** Package `hldphotos` — accept upload to local store, enqueue resize stub; or paper sequences. Tests: size limit; content-type allowlist.

**HLD:** Client → signed URL → GCS → Pub/Sub → worker variants → CDN. NFRs: upload p95, time-to-first-thumb. ADR: Cloud Run Jobs vs Functions for variants.

**LLD:** Signed URL policy; object metadata; IAM `roles/storage.objectCreator` via signing SA; Terraform bucket + CDN backend bucket shape. Idempotent variant by generation.

**GCP lab:** GCS + Run worker free-tier (tiny images). Cloud CDN live **credits-optional**.

**Gate:** Unseen — hot celebrity album. Nearby — Northstar product image pipeline.

#### 8.C.8 Multi-DC

**Concept:** Serve from multiple regions with explicit RPO/RTO and traffic shifting. Failure modes: DNS-only failover forgetting data; active/active without conflict rules; session affinity as consistency.

**From scratch:** Paper pack + sequences mandatory (no homemade global DB). Optional: dual local processes with partitioned “regions.”

**HLD:** Mermaid users → GCLB → regional Run → regional data + async replication story. NFRs: RPO/RTO, split-brain policy. ADR: active/passive vs multi-region Spanner/Firestore.

**LLD:** Health checks, DNS TTLs, IAM per region SA; Terraform multi-region sketch. Errors during failover documented.

**GCP lab:** Paper + single-region prove. Second region / Spanner multi-region **credits-optional**.

**Gate:** Unseen — region X dies during payment capture. Nearby — checkout SLO series/parallel math (10.1 recall).

---

### 8.D Primer additional questions → HLD prompts (not a second course)

Restore as **HLD prompts under Part 8** only — evidence-pack light or full when marked. Do not open a parallel primer encyclopedia.

| Prompt | Expectation | Cross-link |
|---|---|---|
| **Web search** | HLD: crawl → index → query; ranking literacy; abuse | Indexing depth stays shallow; ML LTR families → 9c / Appendix M index |
| **Docs OT (tiny)** | Collaborative doc: presence, op transform **tiny** example (insert/delete on one string), conflict UX | **No CRDT research agenda**; not a product build |
| **Chat** | Same as 8.C.6 pack | — |
| **Photos** | Same as 8.C.7 pack | — |
| **Trends → HLL** | Cardinality of unique actors on a topic; HyperLogLog toy + BigQuery `HLL_COUNT` mention | Implemented with **8.1 HLL** row / sketch |
| **Top-k** | Heavy hitters: Count-Min or heap-per-key; serve top-k trends | 8.1 Count-Min row |
| **Stock exchange (optional)** | Matching engine HLD only: order book, fairness, latency NFR; **no** market connectivity | Optional; skip if time — ledger money movement stays Part 5 |

---

### 8.E OOD code labs (scoped)

#### Concept
Object-oriented design labs here are **data-structure studios with clear APIs**, not interview theater. Scope is locked to three packages that Northstar and Part 8.A actually reuse: hash map, LRU, circular array/ring buffer. Parking-lot / cards / call-center stay **out of scope** unless a single paragraph justifies a Northstar force (default: **skip** — do not add them).

#### From scratch
| Lab | Package | Build | Gate |
|---|---|---|---|
| Hash map | `hashmap` | Chaining or open addressing; grow; collide; delete; load-factor note | Grow, collide, delete; asymptotics note |
| LRU | `lru` | Map + doubly linked list (or equivalent); capacity eviction | See 8.A.4 |
| Circular array | `ringbuf` | Fixed cap, overwrite oldest, iterator; pair with hashmap for “last N” | Fixed cap, overwrite, iterator |

Python twin first, then Go (`-race` where concurrent). Reuse from 8.A.4 — do not fork a second LRU.

#### Free-tier lab note
Pure libraries — no GCP spend. Attach LRU middleware to an existing Cloud Run service only if you already have one.

#### Gate
All three packages green with the table gates above. Unseen: implement `GetOrLoad` on LRU without stampede (hook 8.1 singleflight). No parking-lot/cards/call-center artifacts required.

### 8.1 Production-scale primitives (from scratch, then product)


Tutorial microservices skip these. You do not. Each: small tested toy → Northstar hook → GCP stand-in. Do not re-teach SOLID/gRPC here.

| Primitive | Why | Toy | Production |
|---|---|---|---|
| **Bloom filter** | Negative lookups; cache penetration | Bit array + k hashes; measure FPR | In-process on catalog; Redis Bloom if Memorystore |
| **Cache stampede / singleflight** | Thundering herd on TTL | Coalesce concurrent misses | Client + Memorystore |
| **Consistent hashing** | Remap fewer keys when a node dies | Ring + vnodes; plot % moved | Memorystore cluster, Pub/Sub ordering keys |
| **WAL** | Durability is a log | Append + replay | Postgres WAL, Spanner |
| **LSM vs B-tree** | Why Firestore/Bigtable write path ≠ Cloud SQL | One SSTable flush diagram/toy | Cloud SQL vs Bigtable |
| **HyperLogLog / Count-Min** | Cardinality / heavy hitters | Tiny sketch | BigQuery `HLL_COUNT` |
| **Load shedding** | Survive overload | Queue depth → 503 + Retry-After | Cloud Run concurrency, Armor |
| **Hedged requests** | Tail latency | Hedge after p95 | Client middleware only |
| **Backpressure** | Slow consumer slows producer | Bounded queue | Pub/Sub outstanding, Cloud Run CPU |
| **Hot partition** | One key melts a shard | Key histogram | Firestore/Spanner key design |
| **Cursor pagination** | Never `OFFSET 100000` | Seek `(created_at, id)` | Cloud SQL / Firestore |
| **Schema evolution** | Expand/contract | Break a consumer, then proto/SQL fix | protobuf field numbers (3.2), migrations (2.1) |
| **Leases / fencing tokens** | No split-brain leader | Monotonic fence | Spanner/etcd; **Redis lock is not truth** |
| **Clock skew** | `ORDER BY now()` lies | Two clocks disagree | TrueTime; sort by ID |
| **Idempotency at scale** | Exactly-once *effect* | Unique key | SQL/Firestore + Pub/Sub |
| **N+1 / batching** | Chatty s2s | DataLoader-style batch | gRPC stream/batch (3.2) |
| **Connection pool math** | instances × pool > `max_connections` | Spreadsheet + test | Cloud SQL + PgBouncer (2.3) |
| **Multi-tenant isolation** | Noisy neighbor | `tenant_id` + per-tenant limiter | RLS (2.1) |
| **Feature flags** | Deploy ≠ release | In-memory JSON flags | Remote Config / your table |
| **Poison redrive** | DLQ is not a grave | Redrive API | Pub/Sub DLQ (3.5) |

**8.1 from-scratch (required with the gated studios, not a second list):** bloom + FPR; hash ring; singleflight; load-shed; cursor pager — expanded below. WAL toy may reuse the Pedagogy §6 KV / linKV. LSM = written comparison. Unique IDs and rate limiter are studios 8.A.6 and 8.A.3. Remaining table rows: concept + tiny toy or written ADR as timebox; do not skip the five required expansions.

**Discrete math (here):** invariants on the hash ring and bloom; asymptotics on the hash you write; binary-search on cursor seek. Open **T-TOC** only if NP-completeness is the actual obstacle. **G-CS** asymptotics/hash-ring invariant live here (Appendix G indexes only).

#### PCA: 1.5 Future improvements + cloud-first

**Guide themes (matrix):** cloud and technology improvements; evolution of business needs; cloud-first design approach. Homes: 8, 11.

| Stance | Prefer | Accept |
|---|---|---|
| Default new work | Cloud-first managed | Temporary GCE/GCVE for lift |
| Evolution | ADR + revisit quarterly | One-way rewrite with no rollback |
| Tech refresh | Adopt when KPI/SLO benefit | Chase every launch |

**Scenario prompt:** Leadership wants “cloud-first” but also freezes all managed-service spend.

**Expected answer shape:** “I pick cloud-first for new APIs on Run/SQL because Y, I accept Z (freeze applies to idle SKUs, not to replacing toil that burns OpEx).”

**Discrete-as-used (8.1):** prove ring invariant (“key maps to nearest clockwise vnode”); bloom FPR ≈ `(1-e^{-kn/m})^k` — measure vs formula; cursor seek is binary-search-shaped on ordered keys. Raft toy (studio 9) stays here; **12.S20 skip-tests** MapReduce/KV/Raft if these toys pass.


#### 8.1.1 Bloom filter + FPR (required)

**Concept:** Probabilistic set: false positives possible, false negatives not (for the standard filter). Use to skip origin lookups. Failure modes: wrong FPR math; forgetting rebuild on capacity; using as authz.

**From scratch:** Package `bloom` (Python then Go). Bit array + `k` hashes (double hashing OK); `Add`/`MightContain`; estimate FPR from formula and Monte Carlo. Tests: no FN on added keys; FPR within tolerance for chosen `m,k,n`; fill ratio. Derive \(m,k\) from target FPR before coding.

**HLD:** Where placed (before Memorystore/Firestore). NFR: FPR ≤ ε at expected `n`. ADR: in-process vs Redis Bloom.

**LLD:** Library API; optional admin reset; no IAM. Errors: refuse Add when saturated if you choose “hard full.”

**GCP lab:** Embed in catalog service; measure hit-skip rate. Free-tier.

**Gate:** Unseen — given ε and n, choose m,k and defend. Nearby — crawler seen-set.

#### 8.1.2 Hash ring (required; shared with 8.A.2)

**Concept:** Continuum of hash(vnode) → node; key maps to successor. Invariant: ownership intervals well-defined; with enough vnodes, load concentrates near mean. Failure modes: poor hash; too few vnodes; no replication factor story.

**From scratch:** Package `hashring` (see 8.A.2). Tests + remap metric; Go benchmark lookup.

**HLD / LLD / GCP / Gate:** same as 8.A.2; do not duplicate work — one artifact satisfies both.

#### 8.1.3 Singleflight / stampede control (required)

**Concept:** Coalesce concurrent misses for the same key into one origin load. Failure modes: coalescing different auth contexts; infinite wait without timeout; suppressing errors forever.

**From scratch:** Package `singleflight` (Python then Go). `Do(key, fn)`; waiters share result/error; context cancel. Tests: 100 goroutines/threads one call; error broadcast; timeout. Race pass in Go.

**HLD:** Client-side vs cache-side. ADR: couple with LRU.

**LLD:** Middleware around `GetOrLoad`. GCP: Memorystore does not replace process-local singleflight.

**GCP lab:** Attach to Cloud Run catalog handler; load-test miss path. Free-tier.

**Gate:** Unseen — tenant A must not receive tenant B’s coalesced payload. Nearby — refresh-ahead vs singleflight.

#### 8.1.4 Load shedding (required)

**Concept:** When overload is detected (queue depth, in-flight, CPU), refuse cheaply with 503 + `Retry-After` so the service stays useful for some traffic. Failure modes: shedding randomly without priority; retry storms; shedding after expensive work.

**From scratch:** Package `loadshed` (Python then Go). Token/in-flight limiter; middleware rejects before handler. Tests: under limit pass; over limit 503; Retry-After present; priority lane optional.

**HLD:** Interaction with autoscaling and Armor. ADR: shed at edge vs app.

**LLD:** Error contract; metrics `shed_total`. Terraform: optional Armor adaptive (**credits-optional**).

**GCP lab:** Cloud Run concurrency setting + app shed; prove 503 under artificial barrier. Free-tier.

**Gate:** Unseen — combine rate limit + shed without deadlock. Nearby — Pub/Sub outstanding backpressure (3.4 recall).

#### 8.1.5 Cursor pagination (required)

**Concept:** Seek by `(created_at, id)` (or snowflake id) instead of `OFFSET`. Failure modes: unstable sort; leaking internal ids without authz; cursors that do not expire/sign.

**From scratch:** Package `cursorpage` (Python then Go). Encode/decode opaque cursor; SQL/Firestore-shaped fake store with binary-search/seek tests. Tests: forward pages; empty; deleted-hole; tampered cursor rejected. Tie **binary-search invariant** to seek (**G8–G9**).

**HLD:** List APIs for orders/catalog. ADR: cursor vs page token vendor APIs.

**LLD:** `GET /items?cursor=&limit=`; schema indexes; IAM unchanged. Idempotent reads.

**GCP lab:** Cloud SQL or Firestore list endpoint on Cloud Run. Free-tier SQL tiny instance or Firestore.

**Gate:** Unseen — design cursor under changing `updated_at`. Nearby — snowflake id ordering.

#### 8.1.6 Other primitives (compressed ownership)

- **WAL / linKV:** owned with 8.B.2 + Pedagogy §6.
- **LSM vs B-tree:** written comparison + one flush diagram; no full engine.
- **HLL / Count-Min:** tiny sketch packages `hll`, `countmin` for trends/top-k prompts; BigQuery `HLL_COUNT` recall.
- **Hedged requests / backpressure / hot partition / schema evolution / leases / clock skew / idempotency / N+1 / pool math / multi-tenant / flags / redrive:** concept + Northstar ADR sentence + pointer to owners in Parts 2–5, 3.2, 3.5, 9.1, 10 — implement a toy only if not already proven.

---


#### Go G8 — sort, binary-search invariant
SYNTAX UNLOCK: `sort.Slice(xs, func(i,j int) bool { return xs[i] < xs[j] })`; `sort.Search(n, func(i int) bool { return xs[i] >= target })` — Search requires the predicate be true for a suffix (invariant). Contrast Python: `list.sort`, `bisect`.
Concept: State the invariant before coding (`∀ k < i: !pred(k)` and `∀ k ≥ i: pred(k)` after Search). Bloom/hash-ring neighbors use binary search over sorted rings (8.1 toys).
Python twin first: bisect lab with written invariant; then Go.
Go artifact: package `algo/searchsort`; tests: `TestSearchInvariant`, `TestSortStabilityChoice`, `TestEmptyAndSingle`; gate: written invariant comment above Search; tests include empty/dup/all-true/all-false.

---

#### Go G9 — recurrences, DP, benchmarks
SYNTAX UNLOCK: `testing.B` — `func BenchmarkX(b *testing.B) { for i := 0; i < b.N; i++ { ... } }`; `go test -bench=. -benchmem`. Recurrence → closed form or DP table. Contrast Python: `timeit`; same asymptotics.
Concept: Choose paradigm (greedy / DP / binary search on answer) and explain crossover with measured benches, not vibes. Hash-ring / bloom FPR toys pick representation based on N.
Python twin first: DP solution + complexity paragraph; microbench optional.
Go artifact: package `algo/dp`; tests: `TestDPMatchesRecurrence`, `BenchmarkNaiveVsDP` (document crossover N); gate: README states paradigm + crossover; Part 8.1 toy ADR cites the bench.

---
### 8.1-G G8–G9 and G19 (specified here; Appendix G is index only)

**G8–G9** unlock with 8.1 / studios. Artifacts:

| Artifact | Package | What “done” means |
|---|---|---|
| Sort paradigms | `sortlab` | Implement + test insertion / merge / quick (or stdlib compare); explain crossover on size N; `testing.B` / pytest benchmarks |
| Binary-search invariant | `binsearch` | Lo/hi invariant written; tests on empty/dup/all-less; used by `cursorpage` seek |
| Recurrences | notes + tests in `sortlab` | Match loop to \(T(n)\) for merge/hash; Master theorem **as used** (Part M row) |
| DP entry | `dplab` | One classic (e.g. LIS or knapsack 0/1) + recurrence → table → code; not a DP course |
| Benchmarks | with above | Fair bench: timer, allocs (Go), interpret crossover |

**Gate G8–G9:** choose paradigm for an unseen problem; explain complexity crossover; binary-search invariant stated before code; benchmarks attached.

**G19 synthesis:** the **Part 8 gated studios (8.A + 8.B + 8.C packs)** are the G19 artifact — unseen combinations of DS + HTTP API + concurrency already unlocked (G0–G9, G10–G12 as available). No separate G19 project. Part 11 cannot waive these studios.

---

### 8.F Back-of-envelope and close bar


Powers of two, latency numbers, SKU napkin math (Part 0). Every ADR ends with “I pick X because Y, I accept Z.”

#### Napkin templates (fill blanks in every Part 8 ADR / studio)
1. **Traffic:** QPS_peak ≈ ___ ; read:write ≈ ___ ; payload ≈ ___ B → ingress GB/day ≈ ___.
2. **Storage:** rows/day × bytes/row × retention → GB; indexes ≈ ___× ; choose SKU headroom ___%.
3. **Latency budget:** client p99 ___ ms = edge + app + DB + dependency; name the largest slice.
4. **Cost sketch:** Cloud Run vCPU-s + DB tier + egress; monthly $ ≈ ___ at stated QPS (Part 0 SKU table).
5. **Failure:** if one zone/replica dies, capacity left = ___% ; SLO error budget burn in ___ h.

#### Gate
Produce one filled napkin for Northstar checkout (or your active studio) using the five templates; numbers within an order of magnitude of Part 0 references. ADR close line present. Unseen: interviewer changes QPS ×10 — show which SKU/row breaks first.

**Part 8 complete when:** every 8.0 row has concept + ADR prompt + ownership line; all 8.A studios and 8.B toys gated; 8.C evidence packs filed; primer prompts in 8.D addressed or explicitly deferred on ledger; OOD labs green; 8.1 five required primitives gated; G8–G9 artifacts submitted; G19 satisfied by studio set. Do not move Part 12 content here. Do not homemade TLS/AES/RSA.

## Part 8b — Hybrid connectivity (PCA 2.1)

Hybrid links are how on-prem and other clouds reach your VPC without hairpinning PHI over the public Internet. You will **design and decide**; you will not buy a Dedicated Interconnect in this course.

#### Concepts
- **Cloud VPN:** **HA VPN** (2 tunnels, BGP via Cloud Router) for new prod; Classic VPN literacy only. IKE, BGP, route advertisement, encrypted path over Internet.
- **Cloud Interconnect:** Dedicated vs Partner; VLAN attachments; bandwidth/SLA when VPN is not enough.
- **Network Connectivity Center:** hub-and-spoke connectivity management literacy.
- **Topology choices:** VPC peering (non-transitive) vs HA VPN vs Interconnect vs **Private Service Connect** (consume services without VPC IP soup).
- **Multi-cloud:** HA VPN to AWS/Azure; Google↔Google via peering / Shared VPC / PSC.
- **Google Cloud VMware Engine (PCA 2.3):** lift VMware as-is; prefer refactor to Cloud Run/GKE when cheaper than GCVE forever.

#### From scratch (required)
- Decision-function tests: input `{gbps, rpo_sensitive, phi, vmware, multi_cloud}` → frozenset of products. Encode the table below; unseen rows must match mentor key.
- Draw packet path: on-prem subnet → VPN gateway → Cloud Router → VPC route → private Cloud Run/GKE — annotate encryption boundary.

#### Lab (paper + free-tier)
- HLD: on-prem DC ↔ HA VPN ↔ Shared VPC host. Terraform sketches for HA VPN + Cloud Router **plan-only** unless you have a peer device.
- No live Interconnect. Optional: cheap HA VPN between two of your VPCs as a surrogate lab, then destroy.

| Constraint | Prefer | Do not |
|---|---|---|
| < ~1–2 Gbps, need crypto path fast | **HA VPN** (2 tunnels) | Classic VPN for new prod |
| Steady multi-Gbps + SLA | **Partner/Dedicated Interconnect** | Hairpin over public IP for PHI |
| Consume SaaS without VPC IP | **PSC** | Peering into every producer VPC |
| Shared landing zone | **Shared VPC** host/service | Per-project snowflake VPCs with overlap |
| Multi-cloud burst | HA VPN + explicit routes | Transitive peering assumptions |
| VMware unchanged | **GCVE** | GCVE when refactor to Run is cheaper |

**Decision tests (required):** encode the table as pytest/Go table tests — input `{gbps, rpo_sensitive, phi, vmware}` → expected product set.

#### Gate
- Decision tests green; HLD shows encryption + routing; “I pick X because Y, I accept Z” for one hospital-style scenario.

#### PCA: 2.1 Network topologies (provision)

**Guide themes (matrix):** hybrid; multi-cloud; IPS/FW; VPC; LB; Google Cloud↔Google Cloud; security protection. Homes: 6, 8b.

| Link | Prefer | Accept |
|---|---|---|
| Steady high volume on-prem | Dedicated/Partner Interconnect | HA VPN for lower volume/start |
| Multi-cloud | HA VPN + PSC patterns | Public HTTPS only if data class allows |
| East-west GCP | VPC / Shared VPC / PSC | Peering when non-transitive OK |
| Edge protect | Armor + hierarchical FW / NGFW | VPC rules alone for tiny labs |

**Scenario prompt:** Hospital SaaS must keep insurer file drops on-prem for years and still run GKE in GCP.

**Expected answer shape:** “I pick Partner Interconnect + Shared VPC because Y, I accept Z (HA VPN backup; insurer interfaces stay on-prem).”
## Part 8c — Migration (PCA 1.4)

Migration is inventory → waves → test → cutover → rollback — not a weekend lift of the loudest VM.

#### Concepts
- **Migration Center:** discover, assess, wave plan, dependency mapping.
- **6Rs / Google mapping:** rehost (Migrate to VMs), replatform, refactor (GKE/Cloud Run), retire, retain, repurchase.
- **Licenses:** Windows, Oracle, SQL Server BYOL vs license-included — financial impact before wave 1.
- **Data movement:** Database Migration Service / Datastream; GCS landings; never big-bang without rehearsal.
- **Network & deps:** wave-0 connectivity uses Part 8b decisions.

#### From scratch (required)
- Given a fictional CMDB CSV (apps, deps, OS, DB, criticality), output wave table + chosen R + risk controls. Golden tests for 5 rows.

#### Exercise (required deliverable)
- Migration plan for a fictional 3-tier on-prem app into Northstar’s GCP landing zone: diagram + wave table + license line + “I pick X because Y, I accept Z.”

| Workload signal | Prefer R | Landing |
|---|---|---|
| COTS VM, little change allowed | Rehost | Migrate to VMs / GCE MIG |
| Needs managed OS patch + container ready | Replatform | GKE Autopilot / Cloud Run |
| Bounded context rewrite | Refactor | Cloud Run + Cloud SQL |
| Unused | Retire | Turn off; remove DNS |
| Latency to factory OT | Retain (temp) | HA VPN + façade |
| SaaS equivalent exists | Repurchase | Marketplace / Google API |

| Risk | Control |
|---|---|
| License spike | BYOL review before wave 1 |
| Hidden deps | Migration Center + packet/flow sampling |
| Data loss | DMS/Datastream + cutover checklist + rollback |
| Network surprise | Wave-0 connectivity test (8b table) |

#### Gate
- Deliverable reviewed; wave-0 network test named; rollback written before cutover day.

#### PCA: 1.4 Migration plan (documents + diagrams)

**Guide themes (matrix):** Migration Center; methodologies; licenses; diagrams; integrate with existing systems; assess/migrate systems and data; workload testing; network and dependency planning; license/financial impact. Home: 8c.

| Wave | Prefer | Accept |
|---|---|---|
| Assess | Migration Center inventory + deps | Spreadsheet-only if tiny estate |
| Move VM | Migrate to VMs / rehost | Refactor first only if ROI clear |
| DB | DMS / Datastream | Big-bang cutover |
| License | BYOL analysis (Windows/Oracle/SQL) | Ignore license until after migrate |

**Scenario prompt:** Colo lease ends in 6 months; one Windows SQL Server app; unclear dependencies.

**Expected answer shape:** “I pick Migration Center + wave plan + DMS for SQL because Y, I accept Z (temporary HA VPN, retain one legacy interface until tested).”
## Part 9 — Kubernetes internals applied on GKE + mesh + cache

Part D8 is the CKA-level object/scheduling/security model. This part is **GKE as a product** plus running Northstar on it with GitOps.

