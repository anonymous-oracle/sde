# Google Cloud Production Architect — Curriculum

Student-facing copy. Canonical teaching order is the course spine below. Python exercise first; Go version after you submit. Teaching does not start until you say to start.

**Outcome:** You can design, implement, and operate **secure industry software on GCP** — frontend, backend microservices, identity, and payments — at Professional Cloud Architect judgment, with HLD and LLD as working habits.

**Constraints you set (locked):**
- Production deploy of frontend + backend microservices is taught **first**.
- Billing is at the **start** (cannot deploy industry software without it).
- Then authentication, then payment systems, then the rest of architect depth.
- **First-class (not optional, not “later if time”):** SQL; Cloud SQL; GCE; App Engine dashboards; Cloud Run; GKE; networking/security; IAM; Observability + quotas + SKU analysis; Tasks/Scheduler; DevOps; gRPC/QUIC; SOLID/hexagonal; scale primitives; **production ML systems (9c) + Donne Martin complete topic map (8)**. Each idea has **one home**. Full ML catalog is Appendix M (309 studies). No parallel primer/ML encyclopedias.
- **PCA v6.1 complete:** every bullet in the official exam guide (English on/after 30 Oct) has a home in this course, including Vertex AI Pipelines, AI Hypercomputer, Model Garden, Gemini Enterprise, Model Armor, Migration Center, Google Cloud VMware Engine, Apigee, Terraform, Cloud Emulators, Gemini Cloud Assist.
- **Absolute-beginner / theory prerequisites** sit in **Block T** (HS → undergrad → Ivy-grad-as-needed theory ladder, mapped from unified owner nodes) then Foundation **Block F**. A software engineer can skip-test T tiers and F; an absolute beginner confirms needed **Tier HS** families before F. Confirmed skip-tests only. Do not dump the unified corpus into this file.
- Prerequisites are researched and taught **just-in-time**, not as a six-month wall before GCP.
- After every subtopic: climb the **difficulty ramp** (Pedagogy §7) — concept → from-scratch → HLD/LLD → GCP lab. Python then Go. Unseen check, not “I understand.”
- **You implement the mechanism yourself before you consume the managed product.** Frameworks and GCP APIs come second. See Pedagogy §6.
- Include Donne Martin (`system-design-primer`) mapped onto GCP, not as a separate interview-only track.
- Thoroughness is the priority. **Do not compress for calendar time.**
- Target **all** outcomes: job-ready architect, PCA exam, production delivery.
- Labs stay on **Always Free + trial credits**. Paid-only products (Cloud SQL, Armor, CDN, Memorystore) are still taught in full: you write the Terraform, run the equivalent locally, and apply live only if credits allow. Completion does not depend on burning money.

This file is the curriculum. Teaching starts only when you say so.

---

## Research basis (2026)

Primary sources used to shape the stack and sequence:

| Source | Why it matters |
|---|---|
| [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework) (reviewed 2026-01-28) | Six pillars: operational excellence, security/privacy/compliance, reliability, cost, performance, sustainability. Core principles: design for change, document architecture, prefer managed services, decouple, prefer stateless. |
| [Landing zone design](https://docs.cloud.google.com/architecture/landing-zones) | Identity onboarding, resource hierarchy, network, security. Billing account + organization are day-zero. |
| [Choose compute options](https://docs.cloud.google.com/docs/compute-area/choose-compute-options) | Decision tree: Cloud Run (Google manages infra), GKE (need Kubernetes), Compute Engine (you manage VMs/OS), App Engine (PaaS; still in production estates and on the PCA). |
| [Compute Engine](https://docs.cloud.google.com/compute/docs) | VMs, disks, MIGs, autoscaler, images, OS patch, sole-tenant, Spot. Always Free: 1× e2-micro in us-central1 / us-west1 / us-east1. |
| [App Engine](https://docs.cloud.google.com/appengine/docs) | Standard vs Flexible, services/versions/traffic split. Free: 28 F1 instance-hours/day. Google’s current default for *new* container apps is Cloud Run; App Engine is still required knowledge. |
| [Cloud SQL](https://docs.cloud.google.com/sql/docs) | Managed MySQL / PostgreSQL / SQL Server. HA, PITR, Auth Proxy, private IP, IAM DB auth. **No Always Free tier** — full setup is curriculum; live instance is credits-optional. |
| [AlloyDB](https://docs.cloud.google.com/alloydb/docs) | PostgreSQL-compatible, columnar + OLTP. PCA/architect alternative to Cloud SQL when analytics-on-operational data matters. |
| [Spanner](https://docs.cloud.google.com/spanner/docs) | Globally consistent relational. The “SQL that survives multi-region.” |
| [Cloud NGFW / VPC firewall](https://docs.cloud.google.com/firewall/docs/about-firewalls) | Hierarchical policies, global network firewall policy, threat intelligence, TLS inspection (NGFW). |
| [Cloud Armor](https://docs.cloud.google.com/armor/docs) | WAF, DDoS, bot, Adaptive Protection. |
| [Security Command Center](https://docs.cloud.google.com/security-command-center/docs) | CSPM + findings. Standard vs Premium/Enterprise. |
| [Cloud Run resource model](https://docs.cloud.google.com/run/docs/resource-model) (updated 2026-09-09) | Four resource types: **Services** (HTTP/gRPC APIs), **Jobs** (run-to-completion), **Worker Pools** (Pub/Sub/Kafka consumers), **Instances** (preview singletons). This is the 2026 production model — not “Cloud Functions vs App Engine” as the default. |
| [Three-tier web app template](https://docs.cloud.google.com/application-design-center/docs/three-tier-web-app) | Official ADC pattern: global LB → Cloud Run frontend → Cloud Run API → data + cache. |
| [Website hosting options](https://docs.cloud.google.com/architecture/web-serving-overview) | Static: Cloud Storage / Firebase Hosting. Dynamic: Cloud Run. CDN + Armor + IAP at the edge. |
| [Firebase App Hosting](https://firebase.google.com/docs/app-hosting/about-app-hosting) | SSR frontends: Cloud Build → Artifact Registry → Cloud Run → Cloud CDN. |
| [Identity products](https://docs.cloud.google.com/docs/authentication/identity-products) | Cloud Identity ≠ Identity Platform ≠ IAP ≠ IAM. Identity Platform is the recommended customer-auth backend; Firebase Auth is the consumer subset; IAP is a front-door for Google identities. |
| [PCI DSS on GCP](https://docs.cloud.google.com/architecture/pci-dss-compliance-in-gcp) | SAQ A / A-EP / D. Industry default for a software product: **never touch PAN**; use a PSP (Stripe Checkout/Elements) and stay SAQ A. |
| [PCA exam guide v6.1](https://services.google.com/fh/files/misc/v6.1_pca_professional_cloud_architect_exam_guide_english.pdf) | English exam on/after 30 Oct uses v6.1. Domains: design ~25%, provision ~18%, security ~19%, processes, implementation, reliability. Case studies include Altostrat Media, Cymbal Retail, EHR Healthcare, KnightMotives Automotive. |
| [Donne Martin, system-design-primer](https://github.com/donnemartin/system-design-primer) | HLD method + building blocks (DNS, CDN, LB, reverse proxy, microservices, SQL/NoSQL, cache, queues, REST/RPC, CAP). No dedicated GCP repo — we **map every topic to a GCP product and a lab**. |
| [Free program](https://docs.cloud.google.com/free/docs/free-cloud-features) | Always Free is the lab budget. Cloud SQL, Memorystore, Cloud CDN, Cloud Armor, Cloud DNS, global forwarding rules are **not** Always Free. |
| [Modern CI/CD with GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/modern-cicd-gke-reference-architecture) | GitHub + kustomize + Cloud Build + Cloud Deploy + Artifact Registry + GKE. App repo vs env repo. |
| [GitOps-style CD with Cloud Build](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/gitops-cloud-build) | Two-repo GitOps: CI writes image digest into env repo; CD applies to GKE. |
| [Cloud Deploy](https://cloud.google.com/deploy) | Managed progressive delivery to GKE and Cloud Run (services + worker pools). Canary, promote, rollback, Skaffold render/apply. |
| [Cloud Build](https://docs.cloud.google.com/build/docs) | Hosted CI. Triggers, private pools, WIF, provenance. Always Free: 2,500 e2-standard-2 build-minutes/month. |
| [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs) | Deploy-time policy + continuous validation. Attestations via Artifact Analysis. GKE and Cloud Run. SLSA checks. |
| [SLSA](https://slsa.dev) | Supply-chain levels. Cloud Build provenance; Binary Authorization SLSA check; Google-internal Binary Authorization for Borg as the origin story. |
| [DORA / WAF operational excellence](https://dora.dev) | Deployment frequency, lead time, change fail rate, failed-deployment recovery. Architecture (loose coupling) predicts CD. |
| Docker / OCI / BuildKit (2026 production pattern) | Multi-stage, `# syntax=docker/dockerfile:1`, cache mounts, distroless/nonroot, digest pinning, multi-arch. |

**Industry default stack this course teaches (2026):**

```
Browser
  → Firebase Hosting / Cloud Storage (+ CDN / Armor / global LB when credits allow)
  → Identity Platform (customer JWT)  |  IAP (admin)
  → API Gateway or URL map
  → Compute (you will run the same API on all three, then pick):
        Cloud Run services (default for new microservices)
        App Engine standard (PaaS, versions/traffic split)
        Compute Engine MIG + HTTP(S) LB (you own the OS)
  → Pub/Sub + Eventarc + Cloud Run Jobs / Worker Pools
  → Data:
        Cloud SQL PostgreSQL  (OLTP system of record — design + setup required)
        Firestore             (session, catalog cache, free-tier live lab)
        Cloud Storage         (objects)
        BigQuery              (analytics)
  → Secret Manager + Cloud KMS
  → Cloud Build + Artifact Registry + Workload Identity Federation (no keys)
  → VPC + Cloud NGFW / firewall policies + IAP + VPC-SC (org)
  → Cloud Logging / Monitoring / Trace + Security Command Center
```

GKE, Spanner, AlloyDB, Memorystore, Apigee, Cloud Armor, VPC-SC are **required as architect knowledge**. Live clusters/instances are credits-optional; Terraform + local substitutes are required.

---

## Pedagogy (non-negotiable)

This Pedagogy section **is** the teaching method. The Parts below **are** the content. Bind every lesson to a `###` owner heading in this curriculum. Do not consult a parallel instruction file.

**Purpose.** The learner understands theory, rebuilds important primitives, chooses production trade-offs, and operates real systems on Google Cloud — Northstar + PCA/PMLE competence. Using agents, libraries, and consoles is a waypoint, not the destination. This Pedagogy absorbs teaching-contract **method** rigor (depth floor, ramp, dependency gate, ledger); it does **not** rewrite the destination into a standalone middle-school-to-Ivy math PhD track.

**How this file was unified.** Concepts from teaching policy (the teaching contract), the production GCP spine, and institutional CS/math/ML maps were extracted, aliases merged (SQL/relational algebra, RAG/retrieval, HLD/LLD/architecture), and each concept given **one owner**. Later mentions are applications. Unique reading lists and case indexes live in appendices. The **teaching order is the Course spine below** (graph-ordered continuation **T→F→11b**, then Part 12) — never a second numbered degree sequence and never filename-dependent.

**Mathematical aptitude (theoretical topics).** A non-routine challenge is an unfamiliar formulation, hidden structure or constraint, a deliberate representation choice, several justified reasoning moves, and a check or counterexample. It is not a relabeled formula substitution, library call, or coding chore. The “JEE-Advanced” reference names that **structure-first aptitude**, not a level cap and not a second contest track: build the habit on unlocked objects, then carry it unchanged in kind to each topic’s own ceiling (graduate coursework / staff-engineer ops — not original research). On platform and GCP slices, translate the same habits into production, adversarial, diagnostic, or design challenges (see §7).

### 1. One product, growing
You build **Northstar** — a multi-tenant storefront SaaS (catalog, cart, checkout, orders, webhooks, admin). Every module adds a real production concern to the same system. No toy “hello world” that is thrown away.

### 2. Five artifacts per subtopic
1. **Concept** — what it is, why it exists, failure modes.
2. **From scratch** — you write the mechanism in stdlib Python (then Go): servers, proxies, middleware, parsers, state machines. No FastAPI/Gin magic until the stdlib version works. No GCP client until the local version works.
3. **HLD** — C4 container/context, GCP architecture sketch, NFRs, trade-offs, ADR.
4. **LLD** — OpenAPI or protobuf, sequence diagram, data model, IAM bindings, Terraform module shape, error/idempotency contract.
5. **GCP lab + exercise** — wire the same contract to the real product. Python first; Go after submit.

### 3. Python → Go rule
- Python is the learning language (FastAPI or stdlib `http.server` + `google-cloud-*`).
- Go is the industry language for many GCP control-plane and high-performance services.
- You do not get the Go starter until the Python submission exists. Review compares both: types, error handling, context cancellation, goroutines vs async, client libraries.
- **Lab order is locked:** Python twin first, Go after submit, on every implementable Northstar/GCP slice. Ownership specializations (Python math/ML scratch; Go services/systems/security middleware; hybrid production ML) live in Teaching contract §8 — they clarify *what* each language owns; they do **not** flip this submit sequence.

### 4. HLD vs LLD (taught as a craft, not a slide)
| | HLD | LLD |
|---|---|---|
| Question | What exists and why? | Exactly how does it work? |
| Audience | stakeholders, PCA case study, new teammates | implementers, reviewers, on-call |
| Artifacts | context diagram, container diagram, NFR table, cost/risk, ADRs | sequence, schema, API spec, IAM, Terraform, class/module design, failure matrix |
| Donne Martin step | Step 2: high-level design | Step 3: core components + Step 4: scale |

Donne Martin’s four interview steps become the **design loop for every Northstar change**: constraints → HLD → core LLD → scale/security/cost. Full six-step protocol (NFRs, capacity, Mermaid HLD, LLD, failures, hardening) is Pedagogy §8.

### 6. From-scratch rule (required guideline — every topic)

You do not “call the SDK and call it learned.” For every concept in this curriculum you:

1. **Write it** with the language standard library (Python `http.server` / `socket` / `asyncio`, then Go `net/http` / `net` / `context`). Prefer no framework. If a framework is used later, you must be able to point to the middleware you would have written.
2. **Test it** with table-driven tests: happy path, failure, timeout, replay, concurrency.
3. **Name the production substitute:** “this is what Cloud CDN / Cloud Load Balancing / Identity Platform / Pub/Sub is doing for me, and here is where my toy version is wrong.”
4. **Then** use the GCP offering. The managed product is the *deployment*, not the *understanding*.

**Middleware you will write yourself (stdlib), then keep in Northstar until a gateway replaces them:**

| Middleware | What you implement | Later replaced / fronted by |
|---|---|---|
| Request ID / correlation | UUID per request, `X-Request-Id` | Cloud Trace |
| Structured logging | JSON logs, no secrets | Cloud Logging |
| Access log | method, path, status, latency | Cloud Logging + LB logs |
| Recover / panic | catch, 500, don’t leak traces | Error Reporting |
| Timeouts | per-request deadline | Cloud Run request timeout, LB timeout |
| Authn | parse Bearer JWT, verify (local HMAC first, then Google certs) | Identity Platform + IAP |
| Authz | RBAC on `(principal, action, resource)` | IAM + app RBAC |
| CORS | origin allowlist, preflight | CDN/LB cannot replace this on APIs |
| Rate limit | token bucket / sliding window in memory, then Redis | Cloud Armor rate limit, API Gateway quota |
| Idempotency | `Idempotency-Key` header + store | your DB unique constraint |
| Body size limit | reject oversized bodies | LB / Cloud Armor |
| Security headers | CSP, HSTS, X-Content-Type-Options | CDN / Hosting |
| Cache | `Cache-Control`, ETag, If-None-Match, in-process LRU | Cloud CDN |
| Retry + backoff + jitter | client middleware | — you still own this |
| Circuit breaker | consecutive failures → open | — you still own this |
| HMAC webhook verify | Stripe-style signature | — you still own this |

**Bare-metal / from-scratch servers (required, local):**

| Concept | You write | You do **not** write |
|---|---|---|
| HTTP/1.1 | request parser + response writer on a TCP socket (subset: request line, headers, Content-Length) | HTTP/2 framing, HPACK |
| Reverse proxy / L7 LB | round-robin to N backends, health check, Host/path routing | Maglev, GFE |
| L4 forwarder | TCP accept → dial backend → bidirectional copy | Anycast, DSR |
| CDN edge | cache key, TTL, revalidation, stale-while-revalidate | global PoPs |
| DNS | recursive stub: parse A/AAAA, follow CNAME, honor TTL | DNSSEC crypto |
| NAT | rewrite source IP/port with a mapping table (userspace toy) | kernel conntrack, Cloud NAT |
| Firewall | 5-tuple evaluator (already in Part 6) | kernel netfilter |
| JWT | create/verify HS256 yourself; then verify RS256 with a JWKS fetch | Identity Platform |
| Sessions | signed cookie, expiry, rotation | — |
| Password hashing | Argon2/bcrypt via library; never roll a hash | — |
| TLS | use stdlib TLS; draw the handshake; **do not invent crypto** | OpenSSL |
| Pub/Sub | in-memory topics, at-least-once delivery, ack deadline, DLQ | global Pub/Sub |
| Task queue | delayed jobs, lease/heartbeat | Cloud Tasks |
| KV store | hash map + WAL file (append log, replay) | Spanner |
| LRU cache | the Donne Martin exercise, wired as middleware | Memorystore |
| Rate limiter | token bucket | Armor |
| CI runner | watch a git dir, run tests, fail on non-zero | Cloud Build |
| Reconcile loop | desired vs actual, act, requeue (mini-controller) | kube-controller-manager |
| Namespaces toy | optional Linux: `unshare` + chroot + cgroups read-only (no new kernel modules) | Docker |

**Hard bans (from-scratch does not mean reckless):**
- Do not implement TLS, AES, or RSA from scratch. Use the stdlib. You *must* still explain the handshake and certificates.
- Do not store or parse PAN. Stripe test mode only.
- Do not scan, attack, or exploit any system you do not own. Vulnerable-by-design local apps only.
- Do not write malware, miners, or persistence kits. Container escape is discussed, not practiced against GCP.

**Order on every topic:** toy implementation → tests → “what I got wrong vs production” → GCP/product lab.

### 7. Difficulty ramp

This ladder governs **how** each sub-topic in this curriculum is taught. It is not a second syllabus.

**Execution contract (one unit at a time):**
- One owner heading (`###` in this file) and one coherent idea per unit. Short title, then teach. No destination essays. Inside a dense `#### Concepts` bullet, **one idea** means one intuition cluster — split before ramping (see Bundled Concepts below). **MUST NOT** dump an entire multi-intuition Concepts bullet in one unit and call the dump the concrete anchor.
- Walk prerequisites first (the JIT map + earlier confirmed sub-topics). Do not import a later Part’s machinery to make a “harder” question. Within the current `###`, also walk **intra-topic** dependencies: co-listed terms in a bundled `#### Concepts` bullet are **not** prerequisites of each other until each has its own confirmed anchor.
- Later appearances of an owned idea: one-line recall + application. Do not re-teach. Recall is allowed **only** for ideas already unlocked-and-confirmed on the ledger — never as a cover for a co-listed sibling that was never anchored.
- Persist and update the **learner ledger** (see Teaching contract → Learner state). Do not dump it into chat.
- **Confirmation = unseen check**, not “I understand.” Fail → mark shaky, step down, do not advance. Mixed problems reuse shaky tools until unmarked. An unseen check that uses unanchored terms is invalid confirmation — fix the check, do not mark the learner shaky.
- If they struggle: step **down one rung** and rebuild the missing tool. Do not skip rungs. Skip coding rungs only when the sub-topic is purely definitional (named fact, console-only click, theorem statement). Productive struggle on an unlocked hard problem is expected — step down only when the attempt reveals a missing prereq, a shaky earlier tool, or repeated dead ends after minimal hints.

**Universal ten-rung sequence** (every non-definitional sub-topic):

| # | Rung | Pass signal |
|---|---|---|
| 1 | **Concrete anchor** | Point at the object (trace, packet, IAM binding, billing line, failing request) and say what changes |
| 2 | **Vocabulary / notation** | Translate words ↔ GCP name / flag / proto field using **only terms anchored this session** — no later tool, no unanchored sibling from the same `#### Concepts` bullet, no new product |
| 3 | **Representation** | Defend the picture: sequence, state machine, CIDR, SLO burn chart, hexagonal ports, C4, `EXPLAIN` |
| 4 | **Core move** | Name the new operation or design decision; say when it is illegal / fails |
| 5 | **Worked illustration** | Trace one clean example; predict one intermediate step |
| 6 | **Basic unseen check** | Correct answer plus a short reason |
| 7 | **Routine variation** | Same method, new numbers / API / region / failure |
| 8 | **Mixed transfer** | New idea **plus exactly two** earlier unlocked ideas. Name all three before executing |
| 9 | **Top-rung challenge** | Sub-topic close only, after mixed. Domain-matched (below). Structure-first plan, unlocked tools only, check a boundary / wrong path |
| 10 | **Reflection + ledger** | Move that mattered, one failure mode, unlocked / shaky / postponed; if a process failure occurred, note it as instructor-side (not shaky) and keep confirmed unlocks |

Do not replace this ramp with a lecture, a formula list, or a bulk exercise dump. Productive struggle on an **unlocked** hard problem is expected. Readiness-matched ≠ easy: difficulty comes from structure, hidden constraints, transfer, or production pressure — not from Part 9 GKE while you are still on Part 1 Cloud Run. Readiness-matched also ≠ later machinery: a harder wording that imports an unconfirmed product, Part, Go token, or sibling term from a bundled Concepts bullet is not “raised pressure” — it is a dependency-gate failure.

**Bundled Concepts → split anchors (MUST).** A `#### Concepts` bullet that lists more than two named things is **not** one teachable beat. Before any ramp starts on that bullet:
1. Split clusters of *genuinely distinct intuitions* into separate rung-1 anchors. Terms that share one intuition (e.g. region vs zone from one VM failure-domain picture) may share an anchor; terms that need a new intuition (e.g. multi-region “named group” vs dual-region “named pair”) **MUST** get their own concrete anchor first. When unsure whether two co-listed terms share one intuition, **MUST** split — false merges caused the vocabulary-check failure mode this rule exists to prevent. **MUST NOT** count reading the Concepts headline aloud, listing the comma-separated names, or a parenthetical aside as an anchor — the learner must be able to point at what changes for that intuition.
2. **MUST NOT** treat the concept-list headline as the scope of a single rung-2 check. Headline proximity is not teaching.
3. **One new idea per unit** still binds inside a dense bullet: finish and confirm one intuition cluster before opening the next.

**Rung-2 vocabulary audit (MUST, every pose; also any vocab-bearing item at rungs 6–7 that introduces a new name).** Before posing a vocabulary / notation check, list every term, flag, identifier, or product name the learner must translate, and confirm each was **named and explained in a concrete anchor this session** **or** is already unlocked-and-confirmed on the live ledger — not assumed because it sits in the same Concepts bullet, the same `###` heading, the same table row, or the curriculum file. Audit against what was *actually taught and confirmed*, not against the concept-list headline. Presence on a `#### Concepts` list is **never** evidence the term is unlocked.

**MUST NOT introduce a new product or system inside a vocabulary / notation check.** If a translation item needs a product the current anchors did not use (e.g. object-storage location codes after a compute-only region/zone anchor), give that product its own concrete anchor first (learner can **point at** what the product is doing — a name-drop or parenthetical does **not** count), then translate. A vocab check is for words ↔ names of ideas already in hand — never a stealth product intro.

**Pre-rung-2 / pre-anchor self-check (MUST, one line, before every rung-1 concrete picture and every rung-2 pose):** *Every term on this check was point-at anchored this session (or is already unlocked-and-confirmed on the ledger); no unanchored sibling from a bundled bullet; no new product; **every noun in this picture is unlocked or anchored in this unit before use**.* If any clause fails, **MUST NOT** pose — split and anchor the missing intuition/product, postpone that item on the ledger until anchored, or **postpone the picture**. Do not permanently delete curriculum content to dodge the audit. Time pressure, “one sitting” wording in the source, or a dense headline **MUST NOT** skip this self-check.

**Prop Lock (MUST — concrete anchors / create-dialogs / metaphors / vocab items).** Every named product, resource type, or systems noun used as a **concrete prop** (create-dialog walkthrough, metaphor, classification fixture, “point-at” object) **MUST** already be unlocked-and-confirmed on the ledger, **OR** receive its own concept + theory anchor in *this* unit *before* being used as a prop.
- **MUST NOT** use later-Part systems as “helpful pictures” for an earlier intuition (canonical bug: **F3** teaching global/regional/zonal scope via VPC → subnet → VM create-dialogs, or asking learners to classify VPC / subnet / firewall rule, before **Part 6** + **T.SysTheory Networking**).
- If the best picture needs a later system: **postpone the picture** until that system unlocks, **or** teach the system first (with the Block T / Theory prerequisites map tier required by that concept) — then use it as a prop.
- Smuggling an untaught product/system as a prop is an **instructor process failure** — same ledger rules as unanchored vocab (MUST NOT mark learner shaky; keep fair unlocks; record postponed / needs-own-anchor; re-anchor before re-pose).
- **Scan note (teach-time audit targets):** F3 VPC/subnet/firewall picture; any early Billing/IAM examples that assume **VPC-SC**; early hierarchy gates that assume **Shared VPC** as known; early compute ADRs that assume **Cloud SQL HA** / **GKE** / **Interconnect** as if already taught — name + defer with a Part owner, or anchor first.

**Block T / academic rigor applies to all subjects a concept needs** — theory, math, CS, and industry fundamentals — not only “math for ML.” Networking, databases, security, and distributed systems each have **T.SysTheory** (and related) tiers that **MUST** be confirmed (or skip-tested) before the product lab that depends on them. A console click without the theory tier is incomplete the same way a Vertex call without the metric derive is incomplete.

**High-risk bundled Concepts (teach-time audit targets — not a re-teach now):**

| Owner | Bundled bullet | Why audit hard at teach time |
|---|---|---|
| **F1** | Networks in one sitting (IP, port, DNS, TCP/UDP, HTTP, TLS, JSON, …) | Many distinct intuitions compressed into “one sitting” |
| **F3** | Global/regional/zonal scope via VPC/subnet/firewall props | **Prop Lock:** VPC/subnet/firewall live in **Part 6** — MUST NOT use as F3 pictures or classification items |
| **F2** | Deployment models: public, private, hybrid, community, multi-cloud | Public/private/hybrid share an intuition; community and multi-cloud often need their own anchors |
| **0.1** | Cloud Billing “SKUs you will actually hit” (long enumerated list) | Whole-list vocab checks repeat the bundled-bullet failure at volume |
| **0.5** | IAM principals: user, group, service account, domain, workforce federated, workload federated | Near-identical naming pair (workforce vs workload) — same shape as multi-region vs dual-region |
| **1.12** | Cloud Load Balancing map (many named LB variants) | Overlapping words (regional/global, internal/external, proxy/passthrough) — high conflation if tested as one set |
| **6.3** | IP addressing: ephemeral/static × regional/global × internal/external | Combinatorial naming space under one headline |

These are flags for the rung-2 audit above at teach time. Do **not** retroactively re-teach them unless the live lesson hits that owner.

**Map onto this course’s artifacts (Pedagogy §§2–6):**

| Ramp | What happens here |
|---|---|
| 1–5 | Concept + one worked trace (console or stdlib); **split** bundled Concepts into separate anchors before any rung-2 |
| 6–7 | Basic/routine: from-scratch write in Python, then Go after submit |
| 8 | Mixed: HLD/LLD that uses **exactly two** earlier Northstar pieces (e.g. JWT middleware + Pub/Sub inbox) |
| 9 | Top rung: GCP lab **or** production failure drill **or** ADR under a nasty constraint |
| 10 | Consolidation, not a ledger reprint |

**Software-engineering five-rung shorthand** (same ramp, collapsed for Go/DS/platform slices — do not skip the ten internally):

1. **Basic** — vocabulary **of terms already anchored this session**, one tiny program or one `gcloud` use (same rung-2 audit: no bundled siblings, no new product).
2. **Guided** — one worked implementation with tests; they read and trace it.
3. **Routine** — they write the happy path (Python, then Go).
4. **Mixed** — new idea + exactly two earlier unlocked nodes (errors, edges, a boundary).
5. **Hard / production** — last rung at sub-topic close: production-flavored slice (failures, contract, observability, rollback, cost) **or** an adversarial/diagnostic drill. Still only unlocked tools.

**If a topic is theoretically required, the academic bar is complete — not a survey.** Classify each `###` as one of:

| Class | What “complete” means | Typical owners |
|---|---|---|
| **Theoretical** | Central results are **derived or proved from first principles**, not recalled. Assumptions and validity conditions stated; what breaks when each fails; counterexample or boundary; unseen transfer that cannot copy the illustration. Then the from-scratch primitive (if implementable). | 8.1 primitives; SLO/error-budget math; CAP/consistency; isolation/MVCC; WAL; HOL/QUIC stream independence; protobuf wire types; JWT structure (not crypto); bloom FPR; consistent-hash remap; 9c metrics/leakage/ranking losses that you actually use |
| **Systems / design** | Unfamiliar constraint, hidden structure, multi-step trade-off, failure and rollback, observability and cost. Not a library-call dressed as hard. | Cloud Run, IAM, VPC, CI/CD, HLD/LLD, microservices, payments |
| **Security** | Adversarial: property at risk, failing test first, invariant, what an attacker cheaply exhausts | Parts 4, 6, 7, PCI |
| **Engine / data** | **Predict** engine behavior before running; explain the discrepancy after (`EXPLAIN`, isolation anomaly, index, lock, PITR) | Part 2, Spanner/Firestore |
| **Definitional** | Named fact, historical label, console-only click. No derivation demand it cannot support | Product nicknames, exam case names |

Do not leave a theoretical topic at “I can call the API” or “I sketched the formula.” Do not inflate a definitional topic into fake proofs.

**Skip when definitional.** Named theorem statements, historical labels, product nicknames, and console-only clicks get **no** top-rung challenge and **no** forced scratch implementation. Skip coding rungs only when the idea cannot be meaningfully implemented in the owner language. All other practice happens at teach time — not as a bulk exercise dump stored in this file. **MUST NOT** use “definitional” as a license to put an unanchored term or new product on a vocabulary check, or to skip the concrete anchor for a co-listed sibling you still intend to test. If you will test it at rung 2, you **MUST** anchor it first — even when the eventual top rung is skipped.

**Top-rung budget (mandatory on every substantial non-definitional `###`):** after mixed transfer passes, pose **one to three** non-routine challenges. Prefer two or three when the topic has distinct representations. At least one is an unseen integrated problem that cannot be completed by copying the worked illustration. These **are** the top rung of the difficulty ramp — not a second parallel problem set and not extra contest homework after the ramp already ended. Do not open the top rung until that sub-topic’s mixed transfer has passed. If a full-ceiling item needs a locked tool, record it under **postponed challenges** on the ledger and pose the strongest **unlocked** version now. Fake difficulty (bloated arithmetic, future-module tricks, disguised later-Part APIs) is forbidden. A derivation followed by a tiny Python/Go check or ablation may form one integrated top rung; reasoning comes first.

**Top-rung by class:**

| Class | Top rung |
|---|---|
| Theoretical | Prove or disprove; derive; state precise conditions; construct a counterexample; check dimensions/units/complexity/FPR/error bound; then a tiny numerical or code check if implementable |
| Platform / GCP product | Production failure: misconfig, blast radius, rollback, cost leak, quota burn, idle IP, dual-write |
| Security / IAM / PCI | Least-privilege hole, confused deputy, replay, leaked-token runbook — **no** attacking systems you do not own |
| Data / SQL / Firestore / Spanner | Predict: isolation anomaly, index miss, hot key, pool exhaustion, WAL/PITR |
| Protocols | HOL vs independent streams, wire-format golden test, deadline/cancel |
| HLD/LLD | Design under constraint: protocol, data ownership, retry/idempotency, observability, rollback; “I pick X because Y, I accept Z” |
| Definitional | No top rung, no forced scratch |

**Intuition moves / structural aptitude** (pick one or two per unit; lenses, not a checklist dump). The “JEE-Advanced” label names an **aptitude**, not a level cap: read an unfamiliar problem, expose hidden structure, choose/switch representations, plan before computing or coding, check the result. Build that habit on unlocked objects, then carry it upward to this course’s ceilings (graduate coursework / staff-engineer ops — not original research). On theoretical slices (8.1, M.*, 9c metrics/losses), apply it to derive/prove, state precise conditions, counterexample/boundary, conditioning/error/complexity. On platform slices, translate the same habits into production, adversarial, diagnostic, or design challenges.

Move bank (unlocked only; postpone if locked): translate representations (words ↔ diagram ↔ schema ↔ state machine ↔ C4 ↔ `EXPLAIN`); smaller/zero/boundary/extreme case first; invariant, symmetry, conservation, or repeated substructure; reverse from the target or the incident; bound size/latency/cost/quota/probability before solving; split cases only when it reduces uncertainty; construct or disprove with a minimal failing input; choose the simplest coordinate, schema, API, or service boundary that exposes the constraint; sanity-check against the original wording, SLO, budget, IAM, or units.

**Domain application (this course — same ramp, different surface):**
- **Math / ML (M.*, 8.1, 9c theory):** objective geometry, dimensions, gradients, probability, metrics, generalization **before** coding; top rung = derivation or structural prediction + tiny Python check/ablation. Structure-first plan before computation.
- **Go / DS / platform:** invariant, complexity, edge-case, and implementation reasoning; top rung = hard platform problem or production-flavored slice after mixed — unlocked syntax/structures only. Audit required tokens and data structures before hard work.
- **Databases (Part 2):** predict engine behavior before running (`EXPLAIN`, isolation anomaly, index miss, WAL/PITR, lock/deadlock); explain the discrepancy after.
- **System design / HLD/LLD:** production-flavored design under constraint — trade-offs, failure, observability, rollback, cost, “I pick X because Y, I accept Z.”
- **Production ML (9c):** hybrid — Python owns model math/eval primitives; Go owns service boundary (evaluator, ranker, feature access, rollout); top rung ties leakage/skew/metric to a serving or ops decision.
- **Security / IAM / PCI (Parts 4, 6, 7, 5):** adversarial top rung — property at risk, failing test first, confused deputy / replay / least-privilege hole; never attack systems you do not own.
- **Networking / edge / ops (1.4, 6, 10):** representation choice (packet path, CIDR, SLO burn, quota) + production failure (idle IP, blast radius, rollback, cost leak).

**Theoretical pass signals (stricter than a correct output):** the learner names the representation; states governing assumptions; explains why each important move works; checks a boundary or a plausible wrong path and repairs it. A right number or a green test with no structure named is routine fluency, not close.

**Learner attempts first.** No solution dump. If stuck: what structure do you see → smaller case → smallest unlocked hint. Escalate only if still stuck. After resolution, name the move that made it easy; add one nearby variant if a shaky habit showed.

**Dependency gate (silent):** before any explanation, problem, hint, proof, coding exercise, design prompt, **vocabulary / notation check**, **or concrete anchor / create-dialog / metaphor**, audit the **whole intended solution path** — not only the stem: notation and vocabulary, GCP/product concepts, Python or Go syntax, data structures, library assumptions, production-system ideas, the likely debugging path, **every sibling term drawn from a bundled `#### Concepts` bullet**, **and every named product/resource/systems noun used as a prop (Prop Lock)**. If any required tool, term, or prop is not unlocked-and-confirmed on the live store (anchored this session for vocab checks / same-unit-anchored before use for props), replace the path, postpone the item on the ledger, **or postpone the picture**. Do **not** jump ahead in the spine to keep a harder wording or a prettier create-dialog. Leave the current `###` only when the idea cannot be practiced at all without that tool. Do not print the audit. Harder is not “smuggle GKE into Cloud Run week,” a locked Go token into G0, a Part 9c metric into Part M before it unlocks, **unanchored siblings from the same Concepts bullet treated as if one anchor covered the set**, **or “helpful” VPC/subnet/firewall/VPC-SC pictures before their Part + T.* tiers**. **Readiness-matched ≠ easy** and **readiness-matched ≠ later machinery:** difficulty comes from structure, hidden constraints, transfer, or production pressure — not from future-module machinery, unanchored co-listed terms, or smuggled props.

**Blocked-path examples (this course):**
- Part 1 Cloud Run week: may harden the container contract, timeouts, and IAM invoker. May **not** require GKE scheduling, Gateway API, or Autopilot node pools — postpone those to Part 9 / D4.
- Part M metrics: may derive precision/recall/FPR by hand and in tiny Python. May **not** import Feature Store, shadow traffic, or Vertex Pipelines until 9c unlocks them.
- Early Go (G0–G5): may use unlocked tokens only. A “harder” CLI that needs channels, `context.Context` cancel trees, or generics before their `SYNTAX UNLOCK` is the same violation as posing the locked method first.
- Part 2 isolation: may predict anomalies with unlocked MVCC vocabulary. May **not** smuggle Spanner interleaved-table design or full PITR runbooks into the first Postgres transcript if those owners are still locked — use the strongest unlocked prediction task instead.
- Bundled `#### Concepts` bullet (any owner): may translate terms that received their own concrete anchor this session. May **not** pull co-listed siblings or a new product into the same vocabulary check because the headline listed them together — split, anchor the missing intuition (and product, if any), then check. “Taught in one sitting” in the source text is **not** a waiver of split-anchor or of the rung-2 audit.
- **Prop Lock (F3 / early Parts):** may teach global vs regional vs zonal scope with **already-unlocked or same-unit-anchored** objects (GCE VM as a rented computer in a zone; GCS location codes after the GCS anchor). May **not** require classifying VPC, subnet, or firewall rule, or walk VPC→subnet→VM create-dialogs, until **Part 6.2+** after **T.SysTheory Networking** UG (+ addressing theory). May **not** assume VPC-SC, Shared VPC, Interconnect, or Cloud SQL HA as known props in F/0/early-1 — name + defer with a Part owner, or teach first.

**Sub-topic complete when** they can: explain it in plain language; **derive or prove** its central results if the topic is theoretical; state assumptions and failure; solve basic + routine; finish mixed (two earlier tools named); **pass** (not merely attempt) the current unlocked top rung; then solve or substantially advance **one fresh nearby transfer** without copying the prior path; name a failure case; implement the core primitive from scratch (Python then Go) unless definitional. A postponed full-ceiling challenge does not block if a genuine prereq is locked — the strongest unlocked challenge is never optional.

**Part / module complete when** every in-scope `###` has been confirmed that way. A postponed top-rung (genuine locked prereq) does not block the part; keep it on the ledger and revisit as soon as the prereq unlocks. End the part with a few lines: unlocked, still shaky, next — not a full ledger reprint.

**Assignments at teach time only** (not bulk-stored in this file). Rungs 1–3 are illustration + routine write. Mixed then hard/production is **exactly one** interconnected Northstar scenario, not a list of micro-problems. **Structural gate:** the scenario must fail to compile, test, or pass the lab if the new concept is omitted. The two earlier unlocked nodes in mixed **are** the revision pair — name them on one line with part/owner, not a header block. **No dumps:** not a full solution, not a contest editorial, not a primer sample as the learner’s code; guidance only if they struggle (next protocol step or a question). Skip coding rungs only when purely definitional.

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

### 9.0 Introduction to containers

Containers package an app with its userspace dependencies so “works on my laptop” becomes “runs the same digest in Cloud Run/GKE.” Kubernetes exists because fleets of containers need scheduling, healing, and networking policy.

#### Concepts
- **Image & layers:** immutable filesystem layers; content-addressed digests; small base images reduce CVEs and pull time.
- **Registry:** Artifact Registry (7.5) stores digests you deploy.
- **Runtime:** Docker Engine → **containerd** (GKE); OCI runtime runs the container.
- **PID 1:** your process must reap zombies and handle signals (`SIGTERM` for graceful shutdown on Cloud Run/GKE).
- **Why Kubernetes:** desired-state control loops, service discovery, rolling updates — not because every app needs a cluster (Cloud Run first for Northstar).

#### From scratch (required)
- Pedagogue namespaces toy (optional): document `unshare`/`chroot` mental model — do not build a production runtime.
- Minimal image: static Go or distroless Python; `ENTRYPOINT`; non-root USER; prove `docker run` then `docker kill` sends SIGTERM and your app exits 0 after drain.

#### Lab (free-tier boxed)
- Build/push to Artifact Registry; run on Cloud Run from digest; compare to local containerd/docker.
- Gate prep for 9.2: same image must satisfy non-root + RO FS where platform allows.

#### Gate
- Can explain image vs container vs pod in one paragraph; SIGTERM handler tested; digest pinned.

#### Decision table
| Need | Prefer | Avoid |
|---|---|---|
| Single HTTP service | Cloud Run | GKE day one |
| Fleet + DaemonSets / custom CNI | GKE | Fake Kubernetes on one VM for prod |
| Local dig | docker/containerd | Privileged DinD in CI without need |
### 9.1 Memorystore

Memorystore is managed Redis/Memcached for **cache and ephemeral** data. It is not the order ledger.

#### Concepts
- **Redis vs Memcached:** Redis — rich structures, persistence options, pub/sub; Memcached — simple KV cache. Northstar catalog cache typically Redis-shaped.
- **Cache patterns (Donne Martin):** cache-aside (app loads on miss), write-through, write-behind, refresh-ahead. Stampede control: singleflight (8.1).
- **Failure modes:** treating Redis as SoR; hot keys; unbounded keys without TTL; cache poisoning from unauthorized writes.
- **Cost:** Memorystore is **not** Always Free — default lab uses **Docker Redis** locally; Memorystore is credits-optional and must be destroyed same day.

#### From scratch (required)
- In-process LRU + TTL + singleflight already owned in 8.1 — wire as `CatalogCache` port.
- Redis protocol literacy: `GET`/`SET`/`DEL`/`EXPIRE` against Docker Redis; tests for miss/hit/TTL expiry.

#### Lab (free-tier boxed)
1. Docker Redis in compose; catalog cache-aside in front of Cloud SQL/Firestore.
2. Metrics: hit ratio counter (feeds 10.5).
3. Optional Memorystore Basic tier — create, point app, **delete** before idle charges.
4. **Python / Go:** cache port with Redis adapter + memory adapter for tests.

#### Gate
- Cache tests green without Memorystore; ADR: Redis never SoR; TTL + stampede control documented; no production dependency on an undestroyed trial instance.

#### Decision table
| Need | Prefer | Avoid |
|---|---|---|
| Local/dev cache | Docker Redis | Paid Memorystore always-on |
| Prod shared cache | Memorystore + auth/IAM path | Redis without TTL |
| Session SoR | SQL/Firestore | Redis-only sessions without durability story |
### 9.2 GKE and Kubernetes concepts
- Control plane vs nodes. Cluster versions, release channels (Rapid/Regular/Stable).
- Cluster and node management: node pools, machine types, taints/tolerations, autoscaling (cluster + HPA + VPA).
- Pods, Deployments, ReplicaSets, StatefulSets, DaemonSets, Jobs, CronJobs, ConfigMaps, Secrets.
- Kubernetes Services: ClusterIP, NodePort, LoadBalancer, ExternalName, headless.
- GKE storage: PD CSI, Filestore, GCS FUSE (when not to), StorageClass, PVC/PV.
- Binary Authorization. Policy Controller / Gatekeeper. Private cluster, master authorized networks, Cloud NAT.
- [Enterprise-grade production GKE template](https://docs.cloud.google.com/application-design-center/docs/enterprise-grade-production-gke).
- Exit criteria Cloud Run → GKE: sidecars, custom CNI, stateful operators, GPU/DRA, mesh.

#### Autopilot vs Standard (decision)

| Dimension | Autopilot | Standard |
|---|---|---|
| Node ops | Google manages nodes | You manage node pools |
| Billing | Per-pod requests | Node (VM) hours |
| Escape hatches | Fewer (hardened defaults) | DaemonSets, privileged exceptions, custom CNI |
| Default posture | Restricted-leaning | You must enable PSA/BinAuth |
| Pick when | Most microservices | GPU/DRA, Windows, nested virt, exotic agents |

“I pick Autopilot because Y, I accept Z (move to Standard only when a measured constraint appears).”

#### Workload Identity (GKE)
- Bind KSA → GSA; pods call GCP APIs without JSON keys.
- **kind stand-in:** annotate ServiceAccount; mock token exchange in unit tests; on GKE use WI / WIF docs.
- Fail the lab if any key file is mounted.

#### Gateway API vs Ingress
- Prefer **Gateway** + HTTPRoute on new work; Ingress remains literacy.
- GKE Gateway controller → external/internal Application LB + NEGs.
- **kind:** install Gateway API CRDs; one Gateway + HTTPRoute to the catalog Service.

#### NetworkPolicy + PSA (kind lab steps — required)
1. `kind create cluster --name northstar` (CNI that enforces NetworkPolicy).
2. Apply PSA labels: `pod-security.kubernetes.io/enforce=restricted` on `ns-catalog`.
3. Deploy catalog Deployment (non-root, drop caps, read-only root FS) + ClusterIP Service.
4. Apply NetworkPolicy: deny ingress by default; allow from `ns-frontend` only on app port.
5. Prove: curl from a forbidden namespace fails; from frontend pod succeeds.
6. Install Gateway API; route `/catalog` → Service; curl via gateway.
7. HPA on CPU; generate load; PVC for a tiny stateful demo (or skip if Autopilot-shaped).
8. Rolling update + rollback (`kubectl rollout undo`); record PDB.
9. **GitOps:** kustomize overlay in env-repo; apply via script or Argo-in-kind.
10. Tear down: `kind delete cluster`.

- **Credits-optional:** Autopilot, Cloud Deploy target, canary 10%, destroy same day.

### 9.3 Service mesh

A mesh (Cloud Service Mesh / Istio) adds mTLS, traffic split, and retries as **sidecar/proxied** policy. It is not the default for Northstar on Cloud Run.

#### Concepts
- **What you get:** workload identity mTLS, fine-grained authz, canary/traffic split, outlier detection, telemetry.
- **Cost / complexity:** sidecar resources, upgrade coupling, debugging two hops. Prefer app middleware + Cloud Run IAM until forces appear.
- **When:** many services, heterogeneous runtimes, need uniform mTLS without rewriting every client, GKE-scale east-west policy.
- **When not:** two Cloud Run services — use ID tokens + `roles/run.invoker` (3.2).

#### From scratch (required)
- Client middleware already owns retries/timeouts/circuit breaker (3.0/3.2). Document which mesh features duplicate your middleware and which add unique value (identity mTLS across polyglot).

#### Lab
- Paper HLD: Northstar on GKE with mesh canary 10% — compare to Cloud Deploy canary without mesh.
- Optional: Kind + Istio ambient/sidecar hello — tear down; not required for Part 11.

#### Gate
- ADR: mesh deferred until named force; canary strategy chosen without mandating mesh.
- Can explain mTLS identity vs `roles/run.invoker` ID tokens in one paragraph.

#### Decision table
| Force | Prefer | Avoid |
|---|---|---|
| 2–3 Cloud Run services | Run IAM + middleware | Mesh tax |
| 20+ GKE services polyglot | Cloud Service Mesh | Per-language reinvent mTLS |
| Canary only | Cloud Deploy / revisions | Mesh-only canary excuse |
| Retries already in client | Keep middleware | Double-retry mesh + client |
### 9.4 Spanner, AlloyDB, Bigtable, BigQuery (ops view)

Part 2 chose storage types. Here you **operate** analytics and know when AlloyDB/Spanner/Bigtable enter the ops picture.

#### Concepts
- **Decision tree recall:** OLTP → Cloud SQL / AlloyDB / Spanner; analytics → BigQuery; wide-column → Bigtable; cache → Memorystore (9.1).
- **AlloyDB:** PostgreSQL-compatible, HRD/columnar options, for demanding OLTP/HTAP — credits/trial aware (30-day AlloyDB trial exists; destroy after).
- **Spanner ops:** instance sizing, databases, interleaved ops, monitored latency — emulator first (2.7).
- **Bigtable ops:** nodes, GC policies, key design monitoring — rarely free; paper unless credits.
- **BigQuery ops:** datasets, partitioning/clustering, on-demand vs slots, **1 TiB free queries / 10 GiB free storage** per month — primary free analytics lab.

#### From scratch (required)
- Export schema: define an `order_events` JSON/CSV shape; local DuckDB or SQLite warehouse query that mirrors the BQ lab SQL (counts by day, p95 amount).

#### Lab (free-tier boxed)
1. Stream or batch-load order events to BigQuery (Pub/Sub subscription or GCS load).
2. Partition by date; cluster by `tenant_id`; authorized view for analyst SA.
3. Stay under free query/storage; document bytes processed.
4. **Python / Go:** insert rows + run parameterized query job.

#### Gate
- BQ table partitioned; cost/bytes noted; ADR links 2.7 map; no OLTP traffic pointed at BQ.

#### Decision table
| Job | Prefer | Avoid |
|---|---|---|
| Checkout OLTP | Cloud SQL | BigQuery |
| Order analytics | BigQuery free tier | SELECT * unscanned mess |
| Global SQL OLTP | Spanner (trial/emulator first) | Dual Cloud SQL hack |
| Postgres-compatible perf | AlloyDB trial then destroy | Idle large cluster |
## Part 9b — Vertex AI, Gemini, Big Data (PCA v6.1 §§1.3, 2.4, 2.5)

v6.1 made ML/AI a first-class architect domain. This is not a data-scientist career track; it is **service selection and secure integration**.

### 9b.1 Big Data services

Architect literacy for PCA 1.3-style data platforms: bus → process → warehouse → govern. Not a Spark career track.

#### Concepts
- **Pub/Sub (Part 3.4):** ingestion bus; 10 GiB/mo free messages.
- **Dataflow:** managed Apache Beam — batch/stream unified; autoscaling; templates. Prefer for new GCP-native ETL.
- **Dataproc:** managed Hadoop/Spark for lift-and-shift Spark estates.
- **Dataform:** SQL workflow transformation in BQ.
- **Cloud Composer:** managed Airflow when you already think in DAGs / need multi-system orchestration.
- **BigQuery:** datasets; on-demand (1 TiB free queries) vs slots; partitioning/clustering; authorized views; row-level security literacy.
- **BigLake / Dataplex:** open formats + governance literacy.

#### From scratch (required)
- Mini pipeline: generate order events → write JSONL → “transform” to daily aggregates → assert metrics. Then replace stages with Pub/Sub + BQ.

#### Lab (free-tier boxed)
1. Pub/Sub topic → BigQuery subscription **or** GCS batch load of order events.
2. SQL: daily GMV by tenant; partition filter required in queries.
3. **Python then Go:** publish + query.
4. Credits-optional: Dataflow template wordcount — destroy jobs/workers same day.

#### Gate
- Events queryable in BQ under free bytes; ADR: Dataflow vs Dataproc vs SQL-only for Northstar analytics.

#### Decision table
| Estate | Prefer | Avoid |
|---|---|---|
| New GCP ETL | Dataflow / BQ SQL / Dataform | New Hadoop cluster |
| Existing Spark | Dataproc | Rewrite everything week one |
| Cronny SQL transforms | Dataform / Scheduled queries | Composer for two queries |
### 9b.2 Vertex AI end-to-end (PCA 2.4)

This subsection is the **Vertex / Agent Platform product**, not a second recs course (recs design → **9c.2**).

#### Concepts
- **Pipelines:** orchestrate ingest → train/eval → register → deploy; lineage over notebook folklore.
- **Data integration:** BQ / Feature Store into training; avoid ad-hoc CSVs as prod features.
- **AI Hypercomputer / accelerators:** GPUs/TPUs for large training — quota and cost first; no idle GPU fleets for weekly tiny jobs.
- **Serving:** managed endpoints vs Cloud Run for light models; scale-to-zero economics.
- **Consumption models:** pay per prediction / capacity — read SKUs before HLD fantasy.

#### From scratch (required)
- Local sklearn (or heuristic) ranker behind a `RankPort`; save model blob + metrics JSON; load in a Tiny HTTP server. This is the contract Vertex endpoint will replace.

#### Lab (free-tier / budget boxed)
- HLD: Northstar “recommend products” as a Vertex endpoint (or Cloud Run wrapping a small model) — not a custom GPU cluster.
- Register a model artifact in Vertex Model Registry **or** document the click-path with screenshots if API quotas block; tear down endpoints.
- **Python then Go:** predict client with ADC; secrets in Secret Manager.

#### Gate
- ADR rejects permanent GPU GCE for BQML-sized work; port + offline metrics exist before managed endpoint.

#### PCA: 2.4 Vertex / Agent Platform ML workflows

**Guide themes (matrix):** Vertex/Agent Platform Pipelines; data integration; Hypercomputer/GPU/TPU; Cloud Run functions + platform for ML; consumption models; large-scale training. Home: 9b.

| Stage | Prefer | Accept |
|---|---|---|
| Orchestrate | Vertex/Agent Platform Pipelines | Composer when Airflow estate exists |
| Train at scale | Hypercomputer / managed accelerators | Unmanaged GPU MIG without quotas plan |
| Serve | Managed endpoint / Run | Custom GKE serving if needed |
| Data in | Feature Store / BQ integration | Ad-hoc CSVs in prod |

**Scenario prompt:** Data science wants a permanent GPU GCE fleet for a weekly BQML-sized job.

**Expected answer shape:** “I pick Pipelines + right-sized accelerators (or BQML) because Y, I accept Z (no idle GPU fleet).”
### 9b.3 Pre-built AI APIs and Gemini (PCA 2.5)

Buy-vs-build for Google AI APIs and Gemini. Application patterns (RAG, eval, agents) live in **9c.5** / 11b — here you **select and secure** the model/API.

#### Concepts
- **Google AI APIs:** Vision, Document AI, Speech, Translation, Natural Language, Video Intelligence — free-tier units exist for several (e.g. Vision 1k units/mo, Speech 60 min/mo — verify live tables).
- **Gemini Enterprise / Conversational Agents / NotebookLM:** assistants and agents as products.
- **Model Garden:** pick/wrap foundation or task models; do not train if an API meets the SLA.
- **Gemini Cloud Assist (PCA 1.2, 5.1):** architect copilot — use, verify, don’t paste secrets into prompts.
- **Securing AI (PCA 3.1):** Model Armor, Sensitive Data Protection, secure deployment; prompt injection as a threat; never log PII prompts.

#### From scratch (required)
- `ModelPort.Complete(prompt) -> text` with a fake adapter + a Gemini adapter; redaction middleware strips emails/card-shaped tokens before send and before log.

#### Lab (free-tier boxed)
1. Call Gemini (AI Studio/Vertex) from Cloud Run; API key / ADC in **Secret Manager**.
2. One Vision API call on a catalog image for labels (stay in free units) **or** skip-live with recorded fixture if quota exhausted.
3. Document Model Armor / SDP plan for prod prompts.
4. **Python then Go** clients; contract tests on the port.

#### Gate
- No keys in repo; PII redaction tested; ADR: Vision API before custom CV team; RAG design deferred to 9c.5.

#### PCA: 2.5 Prebuilt AI APIs + Model Garden

**Guide themes (matrix):** Google AI APIs (Search, Conversation, Vision, Image, Video, Audio); Gemini Enterprise (Agents, NotebookLM); Model Garden integration. Home: 9b.

| Need | Prefer | Accept |
|---|---|---|
| Catalog vision attrs | Vision / Document AI | Custom CV only if API insufficient |
| Chat support | Gemini Enterprise / Conversational Agents | Homegrown LLM ops first |
| Model pick | Model Garden wrap | Train from scratch |

**Scenario prompt:** Retail wants a custom vision PhD team before calling Vision API.

**Expected answer shape:** “I pick Vision AI + Model Garden baseline because Y, I accept Z (custom Vertex only after API gap is measured).”
### 9b.4 PMLE low-code and platform (required in the initial track)

PMLE domain **1 — Architect low-code AI solutions** (exam guide as of **1 Jun 2026**: Gemini Enterprise **Agent Platform**, BQML, Model Garden). This subsection is **product literacy + decision tables**, not a second 9c systems course. Recs/ETA/fraud/RAG **design** stays Part 9c. Cite the **official PMLE exam guide** in the lab write-up (Appendix C).

#### 1. Low-code selection (when to use which)

| Path | Use when | Avoid when |
|---|---|---|
| **BQML** `CREATE MODEL` | Data already in BigQuery; SQL team; tabular classify/regress/forecast/cluster; need `TRANSFORM` train/serve parity; remote Gemini fine-tune via SQL | You need custom architectures, exotic losses, or non-BQ feature pipelines |
| **AutoML** (Agent Platform) | Tabular/text/image/forecasting with limited ML staff; want managed search over architectures | You must own every layer; strict latency/cost envelopes already known |
| **Model Garden** | Buy/wrap a foundation or task model (Gemini, Imagen, Veo, open models); one-click or SDK deploy | You confuse “pick a model” with “design the application” (app design → 9c.5) |
| **Document AI / Vision / Translate** | Buy OCR, classification, translation APIs | Building a CV research stack for a form-digitization SLA |
| **Gemini / Imagen / Veo selection** | Multimodal generate/understand; choose by modality, context window, cost, safety | Defaulting to largest model without latency/cost math |

**BQML surface (teach statements, not slogans):**
- Model types: linear/logistic, boosted trees, DNN (as offered), time-series forecasting, k-means, matrix factorization / PCA as listed in current docs — always verify against live `CREATE MODEL` docs for the exam date.
- `TRANSFORM` / `ML.TRANSFORM`: **identical** preprocess in train and predict; this is the BQ answer to train/serving skew for SQL features.
- Remote model / fine-tune Gemini with SQL (concept + one worked statement shape): data stays in BQ; model lives on Agent Platform; predict via SQL or endpoint.
- Decision: BQML vs AutoML vs custom training — data gravity, team skills, need for control, iteration speed.

**AutoML literacy:** tabular/text/image; forecasting; read evaluation panels (AUC, precision@k, RMSE); export/register to Model Registry; know what you cannot debug without leaving AutoML.

**Model Garden:** first-party (Gemini, Imagen, Veo, Chirp, Gemma, …) vs partner vs open; managed API vs self-deploy container; fine-tune notebooks vs prompt-only. Document AI / Vision / Translate: buy vs build table in the ADR.

**Gemini / Imagen / Veo selection checklist:** modality, max input, output type, safety filters, regional availability, $/1k tokens or $/image, latency class, whether RAG/tools are required (app → 9c.5).

#### 2. Data plane for low-code + platform

- **Feature Store** (Agent Platform): entity keys, feature views, offline (training) vs online (serving) consistency — diagram for Northstar catalog/user features.
- **Workbench / Colab Enterprise:** exploratory notebooks; not the production trainer. Promote code into pipelines (9c.7).
- **Dataflow vs Dataproc/Spark vs BigQuery SQL vs pandas:** batch/stream volume, existing Spark estate, SQL-centric teams, laptop prototypes. Pick one path in the lab and justify.
- **DLP / Sensitive Data Protection / PII:** tokenize or drop before prompts and training tables; never log raw PII in notebook outputs (ties Part 7).
- **Experiments + ML Metadata:** parameters, metrics, artifacts, lineage — enough to reproduce a run; link pipeline run → experiment.

#### Lab (free-tier boxed)

One of: (A) BQML `CREATE MODEL` + `TRANSFORM` on a public/synthetic table with SQL predict; or (B) documented AutoML walk-through with screenshots + Registry export notes; plus a Feature Store **or** TRANSFORM diagram for Northstar catalog features. Python/SQL first; Go client for predict second. ADR cites PMLE guide § low-code + the product doc you used.

**Gate:** choose BQML vs AutoML vs Model Garden API for a stated Northstar constraint; write the `TRANSFORM` (or equivalent) that forbids a named skew; call predict from Go without embedding secrets.
## Part 9c — Production ML systems (industry case-study atlas)

Full one-line index is **Appendix M** (309 studies). You do not re-implement 309 blogs. Learn **families**, attach Northstar slices, map to GCP. Do not re-teach IAM, Cloud Run, Pub/Sub, BQ, Monitoring.

Each 9c unit uses the difficulty ramp. Pattern: problem → labels/leakage → **derive the metric or estimator you use** → offline evaluation → serving → monitor/rollback/cost → one named case. Metrics, leakage, skew, ranking utility, and FPR that appear in the slice are **theoretical** topics: complete floor, not “call Vertex.”

**M.ML** (incl. IPS), **M.TS**, and **M.CAUSAL** lite are required before the families that gate on them; see **9c.0**. Classical zoo appears **once**, at the end of 9c (after 9c.7). PMLE product depth for scale/serve/pipeline/monitor is **9c.7**; low-code buy-vs-build is **9b.4**.

### 9c.0 Case-study atlas — unified concepts & prerequisites

Source index: Engineer1999 catalog → **Appendix M** (309 one-liners). Teaching lives in **families** (9c.1–9c.7 + Northstars + classical zoo). This section lists **only gaps** that industry case studies require beyond **M.ML** (+ IPS), **M.TS**, **M.CAUSAL**, 9c.1–9c.7, and the zoo — unified across families, one home each. Do **not** treat Appendix M as a second course; do not paste article text here.

#### Unified gap table (highest-priority MISSING / PARTIAL)

| Concept | Kind | Why case studies need it | Owner (learn under) | Gate (complete means) | Defer? |
|---|---|---|---|---|---|
| Position bias + IPS estimator | Math | Click ≠ relevance; Search/Recommend packs name IPS | **M.ML** IPS derive → apply in **9c.2** / Search pack | Derive propensity + HT-style IPS; synthetic click-log toy green | No |
| Diversity / coverage / multi-objective feed | Math / Theory | Anti-popularity collapse; engagement × satisfaction × safety | **9c.2** (+ Recommend pack) | Formalize 2+ objectives + one re-rank diversity rule on a toy list | No (literacy) |
| Contextual bandit beyond slogan (regret; cascade literacy) | Theory | Module order / ranked lists (Instacart, Expedia) | **9c.2**; cascade one-pager | State regret vs CTR; cascade-bandit literacy paragraph | Full RL → **Part 12 / T-RL** |
| BM25 / inverted-index hybrid IR primer | Academic / CS | When semantic/ANN helps vs lexical | **9c.2** Search pack | Score 3 docs with BM25-shaped formula; name hybrid handoff | Depth → IR literacy / 9c.2 only (full IR PhD out of syllabus) |
| Ads auction literacy (bid × quality) | Industry | Ads serving constraint | Search / LTR / ads pack | Rank by bid×quality on a 5-ad toy; no mechanism-design PhD | Mechanism design PhD → defer |
| Deep CTR / wide&deep literacy | Theory | Ads CTR beyond logistic | Search pack | Name wide (memorization) vs deep (generalization); not from-scratch net | Full DL-from-scratch → out of syllabus / external T-DL (not Part 12) |
| Classical TS (trend/seasonality/holiday) vs DL | Math | Ocado/Zalando-class; BQML path | **M.TS** → **9c.3** | Decompose tiny series; when ARIMA/seasonal beats DL | No |
| Causal forecasting / uplift / potential outcomes lite | Theory | Lyft causal forecast; marketing incrementality | **M.CAUSAL** → **9c.3** + Marketing pack | Two-arm toy; holdout vs observational named | Full DAGs → **T-CAUSAL / 12.S14** |
| Supply–demand + constrained opt with ML predictions | Math / Industry | Pricing / dispatch | **9c.3** literacy | State ML forecast as input to a capacity/price constraint | Solvers → **T-OPT** / 12.S14 |
| Weak / semi-supervised labels; graph CC for fraud rings; GNN literacy | Theory / CS | Swiggy/Zillow/Grab-class | **9c.4** | Connected-components on a toy graph; weak-label slogan + gate | Full GNN course → Part 12 |
| Sequence labeling (entity F1); GEC as structured prediction literacy | Academic | Grab tagging; Grammarly-class | NLP pack / **9c** | Entity-F1 on 5-token toy; GEC = structured pred one-liner | Full GEC course → defer |
| Metric learning / contrastive for CV retrieval; on-device/edge literacy | Theory / Industry | Image search; Apple-class edge | **9c.6**; open **T-CV / T-SIGNAL** | Contrastive pair cartoon + edge constraints paragraph | CV/DSP PhD → T-* |
| Survival/hazard / CLV depth; lookalikes; send-time as constrained opt | Math / Industry | Churn/CLV/notify cases | Marketing pack | Hazard slogan + lookalike similarity + frequency-cap constraint | Deep survival → Part 12 |
| Entity resolution; marketplace pricing themes (Other) | Industry | Walmart ER; Lyft pricing | Attach to Forecast/NLP when promoted; else **index-only** | One-liner owner if promoted | Until promoted |

**ALREADY (cross-link only — do not rewrite):** empirical risk / leakage / skew / metrics (**M.ML**, 9c.1); NDCG / pairwise LTR / two-tower+ANN / multi-stage funnel (**9c.2** + zoo); pinball/quantile ETA (**9c.3**); cost-weighted fraud + HITL (**9c.4**); RAG/LoRA slice (**9c.5**); Vision/Speech buy-vs-build (**9c.6**); serve/monitor/CT/experiments (**9c.7**).

#### Academic prerequisite ladder (before opening each family)

| Before family | Must already have | Points at (no duplicate teaching) |
|---|---|---|
| Any 9c family | HS tools if shaky; empirical risk, losses, metrics, leak-free splits | **T.ProbStat** recall only; **M.ML**; features/skew **9c.1** |
| Recommend / Search / ads | Vectors/cosine; ranking metrics; IPS gate | Part M vectors; **M.ML** IPS; **9c.2** |
| Forecast / ETA | Regression + quantile idea; classical TS gate | **M.ML** MSE; **M.TS**; **9c.3** |
| Fraud / HITL | Imbalance metrics; graph CC literacy when rings appear | **M.ML**; **9c.4** |
| LLM / RAG | Softmax/LSE numerics; embeddings slogan | **M.NS**; **9c.5** (production GenAI/RAG owner) |
| NLP / support | Multiclass F1; DLP awareness | **M.ML**; Part 7; NLP pack |
| CV / speech | Serving path first; open T-CV/T-SIGNAL as needed | **9c.6**; F1 tensors as used |
| Marketing / CLV | Holdout lift + causal-lite gate | **M.CAUSAL**; Marketing pack; Experiments **9c.7** |
| Discrete/systems toys used in packs | Asymptotics / bloom / queues as encountered | **F1**, **8.1**, Parts **2–5** |

#### Industry prerequisite ladder (GCP product-patterns)

GCP products already taught in family packs / 9b / 9c.7 stay as-is (BQ, Feature Store, Vector Search, Run/Endpoint, Pipelines, Monitoring, Experiments, Model Armor, Vision/Speech SKUs). **Add only missing patterns:**

| Pattern | Why | Where |
|---|---|---|
| Real-time action stream → **Pub/Sub** → Feature Store (ranker features) | Homefeed engagement freshness (Pinterest-class) | **9c.2** + Recommend pack lab note |
| Inventory / event stream → Pub/Sub → Feature Store | Availability already sketches this — keep one home | Availability pack / **9c.1** |
| Batch score → BQ → Scheduler/Tasks notify | Marketing serving (already in pack) | Marketing pack — ALREADY |

#### Explicit DEFER → Part 12 / T-* / out of syllabus

- Full **RL** for Netflix-style budget-constrained recs → **T-RL** / **12.S14** (bandits stay in 9c.2).
- Full **transformer-from-scratch** / attention derive → **out of syllabus** (external / optional **T-DL**); RAG production slice stays **9c.5** — not a Part 12 dump.
- Full **GNN** course → out of syllabus / external (9c.4 = CC + GNN literacy only).
- **Kaldi / DSP PhD / full CV PhD** → **out of syllabus** (external). Production speech/CV **serving** stays **9c.6** literacy only (**T-SIGNAL** / **T-CV** slivers as used for serving — not a domain-gate track in Part 12).
- Multimodal gen / five GenAI portfolios → **out of syllabus**; production GenAI/RAG (+ optional PEFT/eval already in **9c.5**) stays **9c.5** — no Part 12 five-portfolio track.
- Combinatorial **OR solvers** beyond literacy → **T-OPT** / **12.S14**.
- Formal causal DAGs / IV / DiD → **T-CAUSAL** / **12.S14** (**M.CAUSAL** is lite only).

#### Full-density owners (do not duplicate)

| Topic | Density home | Apply / systems home |
|---|---|---|
| IPS / position bias | **M.ML** (derive + toy) | 9c.2 / Search + Recommend packs |
| Classical TS | **M.TS** | 9c.3 + optional zoo cross-link |
| Causal / uplift lite | **M.CAUSAL** | 9c.3 + Marketing pack |
| BM25 primer, auction, deep CTR, diversity, bandit regret, weak labels, seq labeling, metric learning, survival/lookalike | Literacy rows in gap table above | Named owner column |


### 9c.1 Features, labels, skew

**Split anchors:** (1) **Leakage / point-in-time joins** are not (2) **train/serving skew** tests, and neither is (3) **feature-store online vs offline** serving — own each failure mode separately before 9c.7 transforms.

- Leakage: define it; construct a leak; prove a point-in-time / as-of join forbids it.
- Train/serving skew: name the distribution shift; a test that fails if online features diverge from training transforms.
- Feature store (Agent Platform Feature Store / Feast-shaped toy). Online vs offline features; entity keys; point-in-time correctness.
- **From scratch:** feature table with `event_time` + as-of join that fails if you leak future labels; assert identical preprocess path (scratch transform before BQ `TRANSFORM` in 9c.7).
- **Gate:** break a join to leak; show the metric inflate; fix with as-of; commit the failing then passing tests.

### 9c.2 Retrieval, rank, recommend, bandits

**Split anchors (do not bundle):** (1) **Candidate generation** (two-tower / ANN retrieval) is not ranking — own recall@k and ANN ops separately from (2) **pointwise/pairwise LTR** and (3) **re-rank / diversity / multi-objective**. Bandits are explore-exploit with regret — not feature flags (8.1). IPS / position bias gates stay **M.ML** → apply here; full RL → Part 12.

- Candidate generation → rank → re-rank/diversity. Two-tower + ANN (Vector Search). LTR, multi-task, cold start.
- Bandits / explore-exploit (Instacart, Trivago, DoorDash homepage). Feature flags (8.1) are not bandits.
- Cases (index): Netflix recs, Instagram Explore, Etsy ranker, Airbnb LTR, Twitter algorithm — **worked HLD packs below** for Netflix + Etsy/Airbnb-class LTR.
- **Northstar implementation:** § **9c.2 Northstar — Ranker** (full, not a one-liner).
- **9c.0 gates (do not re-derive here):** IPS + position bias → **M.ML** IPS; diversity / multi-objective re-rank → 9c.0 table; contextual-bandit regret + cascade literacy → 9c.0 (full RL → T-RL); BM25/hybrid IR, ads auction, deep CTR literacy → Search pack via 9c.0; real-time action stream → Pub/Sub → Feature Store pattern → 9c.0 industry ladder.

### 9c.3 Forecast, ETA, demand

**Split anchors:** (1) **Classical TS** (trend/seasonality/holiday — **M.TS**) before (2) **quantile / pinball ETA** losses and (3) **causal / uplift lite** (**M.CAUSAL**) when marketing slogans appear. Constrained supply–demand opt is literacy here; solvers → T-OPT / 12.S14.

- Time series, cascade/ensemble (DoorDash holidays), DeepETA-class tabular/seq models.
- Cases: Uber DeepETA, Swiggy delivery time, Grubhub volume — **worked pack: Uber DeepETA**.
- **Northstar implementation:** § **9c.3 Northstar — ETA**.
- **9c.0 gates:** classical TS decompose → **M.TS**; causal-forecast / uplift lite → **M.CAUSAL**; supply–demand + constrained-opt literacy → 9c.0 (solvers → T-OPT).

### 9c.4 Fraud, graph, HITL

**Split anchors:** (1) **Cost-weighted / imbalanced classification** metrics are not (2) **graph connected-components / ring detection**, and neither is (3) **HITL review-queue** design. Score **tokens** only — PCI/PAN path stays Part 5. GNN depth → Part 12.

- Imbalance, embeddings of journeys (Wayfair Melange), graph anomaly (Grab), HITL (Uber RADAR-class review queues).
- Score **tokens**, never PAN. PCI path stays Part 5.
- Cases: Stripe Radar — **worked pack below**.
- **Northstar implementation:** § **9c.4 Northstar — Fraud-on-tokens**.
- **9c.0 gates:** weak/semi-supervised labels; graph connected-components for fraud rings; GNN literacy only (full GNN → Part 12) — see 9c.0 table.

### 9c.5 LLM applications (GCP RAG slice)

**Split anchors:** (1) **Model/API pick** stays 9b.3/9b.4; (2) **RAG** (retrieve→augment→generate + index) is this owner’s core; (3) **agents/tools/authz** deepen in 11b P5/P9; (4) **PEFT/LoRA** as adapters — derive low-rank update, don’t slogan it. Full transformer-from-scratch / five-portfolio GenAI track → **out of syllabus**; production RAG/agents/PEFT depth that is in-syllabus lives in **9c.5** (+ 11b P5/P9).

- **9c.0 / defer:** multimodal gen portfolios and full transformer-from-scratch are **out of syllabus** (external / optional T-DL) — not new 9c.5 lessons and not a Part 12 dump; appendix concepts decompose in **9c.0**.

Units (institutional GenAI progression, **this owner only** for the initial track): (1) generative vs discriminative; (2) LLM tokenization/embeddings/context; (3) PEFT/LoRA as adapters — derive the low-rank update; (4) RAG: retrieve → augment → generate; index IVF/HNSW as used (**T-NLP**); (5) agents: tool loop, memory, authz (11b P5/P9); (6) production: latency, cost, eval, refusal, logging without PII.

- Gemini / Model Garden **pick** stays 9b.3 / 9b.4. Open **T-DL** when you need backprop/attention derived, not as a prefix to this unit. Softmax/log-sum-exp is **M.NS**.
- Prompting, jailbreak, eval (exact match, rubric, LLM-as-judge caveats).
- **Northstar implementation:** § **9c.5 Northstar — RAG** (help-doc RAG on Cloud Run + Gemini).
- **Portfolio depth:** complete the GCP RAG slice here (**9c.5**). Five-system / Kaldi / from-scratch-transformer GenAI tracks are **out of syllabus** — do not open a Part 12 portfolio dump; optional PEFT/eval depth only if already in this unit.

### 9c.6 CV / speech serving

**Split anchors:** (1) **Buy Vision/Speech APIs** (9b.3) before (2) **custom embedding / metric-learning retrieval**, and separate (3) **batch vs online serving** SLOs. Open T-CV / T-SIGNAL for convolution/sampling as used — serving path before CV PhD.

- Batch vs online. Cases: Netflix in-video search, Etsy image search, Dropbox OCR, speech/music.
- Open **T-CV** / **T-SIGNAL** for convolution, sampling, FT as used — then serve; do not start a vision PhD before the serving path.
- Architect literacy + Agent Platform custom job / prebuilt Vision/Speech APIs; not a CV PhD. Full HLD pack under families below; no second Northstar required in the initial track.
- **9c.0 gates:** metric learning / contrastive retrieval literacy; on-device/edge ML literacy — see 9c.0; depth → T-CV / T-SIGNAL.

### 9c.7 Platform, experiments, serving (PMLE 2–6 depth)

Michelangelo ≈ Agent Platform / Vertex lineage. A/B/holdout/shadow ≠ Cloud Deploy **app** canary (**D4**). Low-code buy-vs-build stays **9b.4**; this block is scale, serve, pipelines, monitor. Cite **PMLE exam guide (1 Jun 2026)** domains: collaborate on data/models; scale prototypes; serve/scale; automate/orchestrate; monitor AI solutions.

#### 3. Scale prototypes into models

| Choice | Prefer when | Cost / failure notes |
|---|---|---|
| **Custom training** | Own architecture, libraries, multi-GPU/TPU | You own containers, retries, checkpointing |
| **AutoML** | Strong baseline, limited staff | Less control; still Registry + monitor |
| **BQML** | Data in BQ, SQL team | TRANSFORM parity; remote fine-tune for Gemini |
| **Tabular Workflows** | Managed tabular path on platform | Literacy: when it replaces DIY pipeline |

- **HP tuning:** search space, budget (trials × hours), early stop; log to Experiments.
- **CPU / GPU / TPU:** arithmetic — examples/sec × params × bytes; memory floor; TPU when large dense matmuls and platform support; GPU default for many custom nets; CPU for classical/BQML/light scoring.
- **Data vs model parallelism (arithmetic, not a CUDA degree):** data parallel ≈ replica × batch (sync grad); model parallel when one replica cannot hold the model. Write the inequality that forces the choice.
- **Training failure modes:** OOM, exploding/vanishing loss, data skew across shards, silent wrong labels, non-deterministic pipelines, checkpoint corruption — detect with unit tests + metric floors.
- **Interpretability:** linear coefficients / tree importances vs Integrated Gradients / example attributions on Agent Platform Explainable AI; LLMs need different eval (9c.5 / monitor).

#### 4. Serve and scale models

- **Batch vs online:** SLA, fan-out, cost. Batch: BQ ML.PREDICT / Dataflow / Run Jobs. Online: Endpoint / Cloud Run / GKE.
- **Model Registry:** versions, aliases (`staging`/`prod`), lineage to dataset + code digest.
- **Prebuilt vs custom containers:** framework prebuilts (TF/PyTorch/sklearn/XGBoost as offered) vs custom when native deps or multi-step preprocess must ship with the model.
- **Feature Store online:** lookup by entity at request time; timeout + fallback defaults; assert parity with training offline store (skew tests).
- **Public vs private endpoints:** VPC-SC / private IP when data cannot leave; auth via IAM + audience-bound tokens (Part 4).
- **Cloud Run vs GKE vs Agent Platform endpoints:** Run for spiky HTTP scorers and RAG apps; GKE when mesh/custom scheduling/GPU pools; Agent Platform managed endpoints for standard model serving.
- **MODEL canary vs APP canary:** traffic split across **model versions** (shadow/holdout/A-B on predictions) ≠ Cloud Deploy progressive delivery of the **service binary** (**D4**). Both can exist; name which dial you turn in an incident.

#### 5. Pipelines and CT

- **Agent Platform Pipelines** (KFP/TFX literacy): DAG, artifacts, caching, retries.
- **Composer / Airflow:** when ML is one tenant in a broader data estate.
- **Ray-on-platform:** literacy — distributed Python training/tuning when the team already Ray-shaped.
- **CI/CD/CT:** Cloud Build builds trainer + serving images; provenance; deploy only attested digests. **CT** = continuous **training** triggered by schedule, data volume, or monitor breach — policy written down (not “retrain when sad”).
- **Identical preprocess train/serve:** implement scratch transform + tests first; then BQ `TRANSFORM` or shared library imported by trainer and scorer. Skew test must fail if paths diverge.

#### 6. Monitor AI solutions

Define on a **synthetic-shift toy** (you inject the shift):

| Term | Definition | Toy |
|---|---|---|
| **Training–serving skew** | Feature or preprocess differs train vs serve | Drop a normalize step online; PSI / max-mean diff trips |
| **Data drift** | \(P(x)\) shifts | Shift a feature mean in stream |
| **Concept drift** | \(P(y\mid x)\) shifts | Flip label policy after time \(t\) |
| **Attribution drift** | Feature importance / attributions shift | Monitor Explainable AI summary stats |

Products: **Model Monitoring**; **Explainable AI**; **Model Armor** (prompt/response filters — Part 7/9b.3); gen-AI eval / **LLM-as-judge caveats** (position bias, self-preference — 9c.5); bias / responsible AI slices on sensitive attributes with documented policy.

**Lab / diagram each:** one scale decision write-up; one serve topology (Run or Endpoint) with Registry version; one pipeline or CT policy ADR; one synthetic-shift monitor that pages. Python then Go where there is a client.

**Gate:** explain model canary ≠ app canary with a Northstar incident story; show skew test red then green; state retraining policy tied to a monitor.

---

### Required Northstar implementations (FULL — Python then Go port)

Each of the four is a **teachable slice**, not a one-liner: problem, labels, leakage control, **metric derivation**, offline eval, GCP serving, monitor, cost. Shared rule: M.ML metrics package reused; no PAN; no PII in logs/prompts.

#### 9c.2 Northstar — Ranker (catalog retrieval + rank)

**Problem.** Given user/context and Northstar catalog, return a short ranked list for home/search. Business: conversion and diversity, not accuracy on “not clicked.”

**Data / labels.** Impressions → clicks/purchases with `event_time`, `user_id`, `item_id`. Label: click or purchase within a horizon. Negative sampling explicit. Cold-start items/users flagged.

**Leakage.** No future aggregates (e.g. “tomorrow’s popularity”) in features; no target encoding without time-aware folds; group split by user **or** time cut — document which. Point-in-time join for user history.

**Metric (derive).** Offline: pairwise logistic or MSE on relevance; **Recall@K**, **NDCG@K** (derive DCG discount \(\log_2(1+i)\)); AUC on scored pairs as a sanity check. Online: CTR / purchase rate with exploration policy. Show why accuracy is wrong.

**Serving on GCP.** Candidate gen: SQL/BQ or two-tower ANN (Vector Search) → ranker on **Cloud Run** (Python first) reading Feature Store online or precomputed embeddings in Memorystore/Firestore; optional Agent Platform endpoint for the heavy model. Auth: private if needed.

**Monitor.** Feature skew vs training; Recall@K proxy on a held-out stream; latency p95; empty-candidate rate; cost per 1k requests (embedding + rank).

**Cost.** Prefer CPU ranker; ANN quota; cache top queries; batch embedding refresh (Run Job) vs online.

**Python → Go.** Python: train toy two-tower or linear LTR on features; FastAPI/stdlib scorer. Go: same **service boundary** (protobuf/JSON contract), port scoring or call Python/Vertex endpoint; table tests for ordering stability and leakage fixtures.

**Worked company lens (implement the design, not the brand):** Netflix-style candidate → rank → re-rank with diversity; Etsy/Airbnb LTR features (listing quality, historic CTR) — see family packs.

#### 9c.3 Northstar — ETA (“order arriving”)

**Problem.** Predict delivery/ready time band for an order so the UI can show an honest window.

**Data / labels.** Label = `actual_delivery_ts - quote_ts` (or ready time). Features: distance, store load, hour-of-week, courier availability proxies — all known at quote time.

**Leakage.** Forbidding post-quote signals (actual route taken, future weather updates not available at quote). Time-based split.

**Metric (derive).** MAE / RMSE on minutes; **pinball / quantile loss** if you show a window (derive pinball for \(\tau\)); % of arrivals inside promised band (coverage) vs band width (tightness). Optimize the trade-off explicitly.

**Serving.** Online regression on Cloud Run or BQML forecast for batch capacity planning; Feature Store for store load. Pub/Sub order events → optional async refresh.

**Monitor.** Coverage vs width; residual bias by city/hour; drift on distance feature; cost of over-promising (support tickets) as a product metric.

**Cost.** Tabular model on CPU; avoid GPU; batch retrain nightly.

**Python → Go.** Python: scratch linear/quantile GD (**M.ML**) or library GBM after stating objective; Go port of predict API + metric helpers.

**Worked company lens:** Uber DeepETA — cascade/ensemble literacy in the family pack; Northstar stays a honest stub, not a clone.

#### 9c.4 Northstar — Fraud-on-tokens

**Problem.** Score checkout risk using **Stripe payment method tokens** and behavioral features; never PAN/CVV. Escalate uncertain/high scores to HITL via **Cloud Tasks**.

**Data / labels.** Chargeback / fraud label with severe delay — use provisional labels carefully. Features: velocity, device, geo mismatch, amount, history — all token-side.

**Leakage.** No post-chargeback analyst notes in training features; time cut; careful with “prior fraud count” that includes the current case.

**Metric (derive).** Precision/recall at a fixed **FPR** the review queue can handle; expected cost = \(C_{FP}\cdot FP + C_{FN}\cdot FN\); PR-AUC under imbalance. Derive why accuracy is toxic here (**M.ML**).

**Serving.** Sync score on checkout path (Cloud Run, tight timeout + fail-open/closed policy in ADR); async HITL queue (Cloud Tasks) for review; Pub/Sub for chargeback labels back into BQ.

**Monitor.** Score distribution shift; precision at operating point; queue depth/age; Model Armor N/A — but DLP on logs; never log full tokens.

**Cost.** HITL minutes dominate; model CPU; threshold set by queue capacity math.

**Python → Go.** Python: logistic GD from **M.ML** on a tiny token-feature table; Go service enforces timeout, idempotency, Tasks enqueue.

**Worked company lens:** Stripe Radar — rules + ML + list features; human review — family pack.

#### 9c.5 Northstar — RAG (help-doc)

**Problem.** Answer Northstar help questions grounded in owned docs; refuse when ungrounded.

**Data / labels.** Doc chunks with ids; eval set of (question, answer, must-cite chunk ids). No user PII in traces.

**Leakage.** Eval questions must not appear verbatim only in train prompts; version the corpus; don’t tune on the test rubric.

**Metric (derive).** Retrieval Recall@K first; answer faithfulness / citation hit; abstention rate; latency and $/question. LLM-as-judge only with known caveats (position bias) — human spot-check required.

**Serving.** GCS corpus → chunk/embed (batch Job) → Vector Search or pgvector/Firestore-shaped toy → Cloud Run orchestrator → Gemini (Model Garden) with tool-less RAG prompt; Secret Manager for API auth; never log raw prompts with PII.

**Monitor.** Retrieval empty rate; citation miss; refusal rate; token cost; Model Armor / safety filters; skew when docs update but index doesn’t.

**Cost.** Embedding refresh schedule; context token budget; cache frequent queries.

**Python → Go.** Python: chunker, embed client, retrieve, prompt pack, eval harness. Go: same HTTP API + retrieval client; contract tests on citation required fields.

**Cross-link:** this unit is the **GCP RAG slice** (production GenAI owner). Deeper five-portfolio / from-scratch-transformer / Kaldi tracks are **out of syllabus** — not Part 12 content.

---

### Required family HLD packs (evidence pack even if not implemented)

For **each** family: problem, data, labels, leakage, metric, serving, monitor, cost, **GCP products**. Implement code only for the four Northstars above. Appendix M “Other” stays index-only.

#### Family: Recommend / feed

**9c.0 prereq gates:** IPS + diversity / multi-objective — see **9c.0** / **M.ML** IPS (do not re-teach).  
**Problem.** Personalized feed or “recommended for you” under engagement + satisfaction + safety constraints.  
**Data.** Impressions, clicks, dwell, hides, follows; catalog metadata; social graph if any.  
**Labels.** Implicit (click) vs explicit (rating); position bias must be modeled or randomized.  
**Leakage.** Future popularity; same-session target leakage; train/test user overlap when measuring generalization to new users.  
**Metric.** NDCG@K, Recall@K, calibration of p(click); online A/B on downstream retention — not offline alone.  
**Serving.** Candidate → rank → re-rank (diversity/authority); Vector Search + ranker endpoint; edge cache for anonymous.  
**Monitor.** Segment-wise NDCG proxy; skew; empty shelf rate; feedback loops (popularity bias).  
**Cost.** ANN + rank flops; exploration budget.  
**GCP.** BQ, Feature Store, Vector Search, Agent Platform / Run, Experiments, Monitoring.  
**Worked examples:**
- **Netflix recommendations:** problem = maximize satisfied viewing hours under catalog constraints; data = play, stop, thumb; labels = play quality with debiasing for UI position; leakage = using post-play completion features at recommend time; metric = ranking + online A/B on retention; serving = multi-stage candidate (title similarity, continue-watching) → rank → row construction; monitor = catalog coverage, model age; cost = precompute rows offline + light online re-rank; GCP map = BQ events, batch embedding Job, Feature Store user state, Run/GKE rank, Experiments for A/B (≠ D4 canary).
- **Instacart homepage / DoorDash-style bandits:** explore-exploit for module order; metric = regret vs CTR; serving = contextual bandit with feature flags **not** substituting for the policy.

#### Family: Search / LTR / ads

**9c.0 prereq gates:** IPS (M.ML); BM25/hybrid IR primer; ads auction literacy; deep CTR / wide&deep literacy — see **9c.0** (one home each).  
**Problem.** Rank documents/listings/ads for a query under relevance + revenue + fairness.  
**Data.** Query, context, impressions, clicks, conversions, bid (ads).  
**Labels.** Graded relevance or click with position debias (IPS).  
**Leakage.** Using click to define features that won’t exist for new ads; advertiser leakage across auctioneers.  
**Metric.** NDCG, MRR; ads: revenue × quality; calibration of pCTR/pCVR.  
**Serving.** Retrieval (inverted / semantic) → LTR → auction (ads).  
**Monitor.** pCTR calibration; latency; junk query rate.  
**Cost.** Index build vs online features.  
**GCP.** BQ, Dataflow index build, Vector Search, Run LTR, Armor for abuse.  
**Worked examples:**
- **Airbnb search / LTR:** listing quality, historical booking, geography; metric NDCG with booking label; leakage = using post-booking review at rank time; serving = retrieval then GBDT/LTR; GCP = Feature Store for listing stats, endpoint for score.
- **Etsy ads / marketplace rank:** pCTR model + auction constraints; monitor calibration by category.

#### Family: Forecast / ETA / demand

**9c.0 prereq gates:** classical TS (**M.TS**); causal-forecast lite (**M.CAUSAL**); supply–demand literacy — see **9c.0**.  
**Problem.** Predict time, demand, or volume for planning and UX promises.  
**Data.** Event times, covariates (weather, holidays, capacity).  
**Labels.** Realized time/volume; censored observations documented.  
**Leakage.** Future covariates; aligning series with peeking.  
**Metric.** MAE/MAPE carefully; quantile coverage; peak-hour error.  
**Serving.** Batch forecasts to BQ; online ETA on Run.  
**Monitor.** Coverage of intervals; bias by geo.  
**Cost.** Retrain cadence vs drift.  
**GCP.** BQML forecasting, Dataflow, Run, Monitoring.  
**Worked examples:**
- **Uber DeepETA:** multi-model cascade (route, traffic, handoff); labels = actual trip time; leakage = features unavailable at request; metric = MAE + coverage of ETA band; serving = online low-latency ensemble; monitor = city-level residual; cost = feature compute vs accuracy; GCP map = Feature Store, custom training on GPU optional, Run/GKE scorers, BQ training warehouse.
- **Swiggy / Grubhub volume:** store-level demand for staffing; batch BQML + Composer schedule.

#### Family: Fraud / HITL

**9c.0 prereq gates:** weak/semi-sup labels; graph CC; GNN literacy — see **9c.0** / **9c.4**.  
**Problem.** Stop abuse/fraud under review capacity and false-positive harm.  
**Data.** Account/device graphs, velocities, payment tokens, disputes.  
**Labels.** Chargeback/fraud with delay; partial labels.  
**Leakage.** Analyst notes; future graph edges.  
**Metric.** Recall@FPR; cost-weighted; queue SLA.  
**Serving.** Sync score + async case management (Tasks).  
**Monitor.** Threshold stability; adversary drift.  
**Cost.** Human review dominates.  
**GCP.** Run, Tasks, BQ, DLP, Monitoring; never store PAN (Part 5).  
**Worked examples:**
- **Stripe Radar:** rules + ML on tokenized payments; labels = fraud outcomes; serving = real-time authorize path; HITL for reviews; metric = catch rate at review budget; GCP map = Run scorer, Tasks queue, BQ labels, Feature Store velocities.
- **Uber RADAR-class / Grab graph:** graph features for collusion; monitor graph-feature drift.

#### Family: LLM / RAG

**Problem.** Grounded generation over private corpora with refusal and cost control.  
**Data.** Documents, ACLs, eval rubrics.  
**Labels.** Faithful answers + citations; human grades.  
**Leakage.** Contaminating eval; prompt stuffing secrets into logs.  
**Metric.** Recall@K retrieval; faithfulness; cost/latency.  
**Serving.** Cloud Run RAG + Gemini; Vector Search; Model Armor.  
**Monitor.** Index staleness; jailbreak hits; token spend.  
**Cost.** Context tokens dominate.  
**GCP.** Model Garden Gemini, Vector Search, GCS, Run, Secret Manager, Model Armor.  
**Worked examples:**
- **GitHub Copilot-class (assistive code):** problem = suggest code in context; data = permissive training + IDE context; metric = acceptance rate ≠ correctness — need eval harness; serving = low-latency endpoint; monitor = toxic/insecure suggestion rate; GCP map for *your* analog = private RAG over internal eng docs + Gemini, not a Copilot clone.
- **Enterprise helpdesk RAG:** ACL-aware retrieval; citation required; 9c.5 Northstar is the thin slice.

#### Family: NLP / support

**9c.0 prereq gates:** sequence labeling / entity F1; GEC as structured-prediction literacy — see **9c.0** (not a full GEC course).  
**Problem.** Route, classify, or summarize support tickets; suggest replies.  
**Data.** Tickets, macros, CSAT.  
**Labels.** Queue/topic; resolution quality.  
**Leakage.** Using post-resolution fields at intake.  
**Metric.** Macro-F1; handle time; deflection rate.  
**Serving.** Classify on Run; optional Gemini summarize with human send.  
**Monitor.** Class imbalance drift; toxic reply rate.  
**Cost.** Human agents vs model.  
**GCP.** BQML/AutoML text, Gemini, Run, DLP.  
**Worked examples:**
- **Airbnb / Zendesk-style support routing:** topic model + priority; metric = misroute cost; serving = online classifier at ticket create.
- **Grammarly-class assist (bounded):** suggest edits with accept/reject logging — eval on held-out essays, not production keystrokes without policy.

#### Family: CV / speech serving

**9c.0 prereq gates:** metric learning / contrastive; on-device/edge literacy — see **9c.0** / **9c.6**.  
**Problem.** Online or batch perception (OCR, image search, ASR) under latency/cost.  
**Data.** Images/audio + labels/transcripts.  
**Labels.** Boxes, transcripts, relevance.  
**Leakage.** Train/test near-duplicate images; speaker leakage.  
**Metric.** mAP / WER / Recall@K; serving latency.  
**Serving.** Batch Dataflow/Run Jobs; online GPU endpoint only if SLA needs it; prefer Vision/Speech APIs when buy > build (9b.4).  
**Monitor.** Blur/noise drift; WER by locale.  
**Cost.** GPU-minutes vs API SKU.  
**GCP.** Vision/Document AI/Speech APIs, custom training optional, Run/GKE, GCS.  
**Worked examples:**
- **Dropbox OCR / Document AI path:** buy Document AI unless custom layout demands; metric = field accuracy; monitor = doc-type drift.
- **Netflix in-video search / Etsy image search:** embedding index; batch embed; online ANN; cost = embed refresh.

#### Family: Marketing / CLV / notify

**9c.0 prereq gates:** uplift / potential-outcomes lite (**M.CAUSAL**); survival/hazard + lookalike + send-time constrained-opt literacy — see **9c.0**.  
**Problem.** Who to message, when, and with what offer under fatigue and unsubscribe.  
**Data.** Purchases, visits, notify history.  
**Labels.** Convert / CLV proxy; churn.  
**Leakage.** Using post-campaign purchases as features pre-send.  
**Metric.** Incremental lift (need holdout); not raw CTR alone.  
**Serving.** Batch score to BQ → Scheduler/Tasks notify; frequency caps.  
**Monitor.** Lift decay; unsubscribe rate.  
**Cost.** Message cost × expected lift.  
**GCP.** BQML, Composer, Tasks, Experiments (geo/holdout).  
**Worked examples:**
- **Lyft / Meta-style notify personalization:** send-time and content; metric = incremental sessions with holdout; serving = batch.
- **CLV for Northstar offers:** BQML regress CLV; target top decile with holdout.

#### Family: Availability / inventory

**Problem.** Predict whether an item/store is available to promise (ATP).  
**Data.** Stock movements, vendor lead times, substitutions.  
**Labels.** Sold-out / found in aisle / canceled for OOS.  
**Leakage.** Using post-pick outcomes at browse time incorrectly.  
**Metric.** Precision/recall on OOS; cost of false “in stock.”  
**Serving.** Online feature of store-item; cache aggressively with TTL.  
**Monitor.** Surprise OOS rate; regional drift.  
**Cost.** Cache vs freshness.  
**GCP.** Feature Store, Run, BQ, Pub/Sub inventory events.  
**Worked examples:**
- **Instacart availability:** browse-time probability item is pickable; labels from shopper finds; leakage = using completed-batch info; metric = calibration of availability prob; serving = online store-item features; monitor = found-rate vs prediction; GCP = Feature Store + Run + stream inventory.
- **DoorDash store-open prediction:** binary open/closed with hours + exceptions.

#### Family: ML platform (Michelangelo ↔ Agent Platform)

**Problem.** Many teams ship models with shared feature, train, serve, monitor paths.  
**Data.** Feature definitions, pipelines, registries, access control.  
**Labels.** N/A — platform SLIs: time-to-train, failed deploy rate, skew incidents.  
**Leakage.** Platform must enforce point-in-time joins as a service.  
**Metric.** Developer lead time; incident rate; cost per training hour.  
**Serving.** Shared Feature Store, Registry, Pipelines, standard endpoints.  
**Monitor.** Platform-level Model Monitoring defaults; quota.  
**Cost.** Central GPU/TPU pools vs per-team sprawl.  
**GCP.** Agent Platform (Pipelines, Feature Store, Registry, Experiments, Monitoring), Composer, Ray literacy, Cloud Build CT.  
**Worked examples:**
- **Uber Michelangelo:** feature store, DSL/train jobs, serve, measure — map each box to Agent Platform product; Northstar uses a **thin** subset (one pipeline, one registry alias, one monitor).
- **King playtesting automation (index):** CI-triggered eval jobs — map to Cloud Build + Pipelines CT policy.

---

### Classical zoo (required here — end of 9c only; not 12.S11 dump)

One home for classical models. **Do not** dump Kaldi, DSP/CV PhD, or full transformer-from-scratch here (those are **out of syllabus**). Logistic/linear **GD from scratch** is **M.ML**. For each family: objective, assumptions, complexity, failure mode, when simpler wins, scratch vs library. **12.S11** only skip-tests this block → **9c zoo / M.ML** (no classical-ML re-teach dump in Part 12).

#### kNN
- **Objective.** Predict from majority / average of \(k\) nearest under a metric (Euclidean, cosine).
- **Assumptions.** Local smoothness; meaningful distance; comparable scales.
- **Complexity.** Naive \(O(n d)\) per query; indexes help approximately.
- **Failure.** Curse of dimensionality; slow at scale; sensitive to feature scaling.
- **Simpler wins.** Tiny tabular baselines; debugging embeddings (retrieval sanity).
- **Scratch vs library.** Scratch distance + vote on a toy; FAISS/Annoy/Vertex Vector Search for production ANN — don’t hand-roll HNSW for Northstar.

#### Linear regression
- **Objective.** Minimize MSE \(\|Xw-y\|_2^2\) (optionally + L2).
- **Assumptions.** Approximate linearity; additive noise; features informative.
- **Complexity.** \(O(np^2)\) closed form / iterative GD \(O(np)\) per epoch.
- **Failure.** Collinearity; outliers (MSE); non-linear truth.
- **Simpler wins.** Strong baseline for ETA minutes, CLV proxies.
- **Scratch vs library.** **Scratch GD in M.ML**; sklearn/BQML after gradient check.

#### Logistic regression
- **Objective.** Minimize Bernoulli NLL / log-loss; outputs calibrated-ish scores if model is right.
- **Assumptions.** Linear log-odds; i.i.d.; no severe separation without regularization.
- **Complexity.** Same order as linear GD per epoch.
- **Failure.** Uncalibrated under shift; cannot express XOR-style interactions without features.
- **Simpler wins.** Fraud token score v1; CTR baselines.
- **Scratch vs library.** **Scratch GD in M.ML**; library/BQML after matching \(\partial\ell/\partial w\).

#### Decision trees
- **Objective.** Greedy partition to minimize impurity (Gini/entropy) or variance.
- **Assumptions.** Axis-aligned splits suffice; enough data per leaf.
- **Complexity.** Train roughly \(O(n p \log n)\) class implementations; depth limits capacity.
- **Failure.** Overfit deep trees; unstable splits; poor extrapolation.
- **Simpler wins.** Interpretable policy rules; when interactions are coarse.
- **Scratch vs library.** Scratch impurity split on 2-D toy; production = library.

#### Forests / boosting (RF, GBM, XGBoost-class)
- **Objective.** RF: average high-variance trees. Boosting: stagewise minimize loss (derive one stage additive step in words).
- **Assumptions.** Tabular features dominate; weak learners combine well.
- **Complexity.** Many trees × depth × rows; training heavier than linear.
- **Failure.** Leakage amplifies; distribution shift; huge models for tiny gains.
- **Simpler wins.** When linear + two features already hits the metric floor.
- **Scratch vs library.** State objective + one boosting step on a toy; then library/BQML boosted trees. No need to reimplement XGBoost.

#### Clustering (k-means et al.)
- **Objective.** k-means: minimize within-cluster sum of squares; alternate assign/update.
- **Assumptions.** Spherical clusters, choose \(k\), scale matters.
- **Complexity.** \(O(n k d)\) per iteration.
- **Failure.** Wrong \(k\); non-convex shapes; sensitive to init.
- **Simpler wins.** Segmentation sketches; initialization for mixture models.
- **Scratch vs library.** Scratch k-means on 2-D Gaussians; BQML k-means when data in BQ.

#### PCA
- **Objective.** Orthogonal directions of max variance; minimize reconstruction SSE.
- **Assumptions.** Variance ≈ signal; roughly linear subspace.
- **Complexity.** SVD \(O(\min(n p^2, p n^2))\) classically; randomized SVD for large.
- **Failure.** Scaling; interpreting components as causation; heavy tails.
- **Simpler wins.** Dimensionality reduction before kNN; noise filter.
- **Scratch vs library.** Derive reconstruction error on 2-D; NumPy SVD; BQML PCA as used.

#### Ranking models
- **Objective.** Pointwise (regress relevance), pairwise (e.g. logistic on pairs), listwise (e.g. Softmax/ListNet-style — literacy).
- **Assumptions.** Comparable items in a list; position bias handled for click data.
- **Complexity.** Pairwise can be \(O(n^2)\) if naive — sample pairs.
- **Failure.** Optimizing pairwise AUC while product needs calibration; ignoring position bias.
- **Simpler wins.** Cosine retrieval + linear re-rank before deep LTR.
- **Scratch vs library.** Scratch pairwise logistic on a 5-item toy (**M.ML** metrics for AUC); library LTR / two-tower after. Full transformers → not here (**out of syllabus** / optional external T-DL).

**Zoo gate:** for a Northstar metric, pick the simplest model that could work; state objective and one failure mode; logistic or linear GD evidence from **M.ML**; no Kaldi / DSP / full transformer-from-scratch in this section (out of syllabus).

---

**Required Northstar implementations (summary):** ranker (9c.2), ETA (9c.3), fraud-on-tokens (9c.4), RAG (9c.5) — full sections above.  
**Required family HLDs:** all ten packs above. Appendix M “Other” = index-only.  
**Classical zoo:** this end-of-9c block only (deduped).

## Part 10 — Observability, reliability, FinOps

Well-Architected pillars, now that you have a system. Operations Suite is the former Stackdriver video block.

### 10.0 Google Cloud Observability (full — PCA 6.2)

#### PCA: 6.x Operations excellence (6.1–6.6)

**Guide themes (matrix):** WAF operational excellence pillar; monitoring/logging/profiling/alerting; release management; support; QC; chaos/load. Homes: D0, D4, 10.

| Pillar ask | Prefer | Accept |
|---|---|---|
| 6.1 Ops excellence | Runbooks, IaC, gradual change | Heroics |
| 6.2 Observability | RED + SLO burn + structured logs | Email-only alerts |
| 6.3 Release | Canary / Cloud Deploy | Big-bang Friday |
| 6.4 Support | Owned runbooks + escalation | Undocumented tribal knowledge |
| 6.5 QC | Tests in CI + progressive delivery | “We tested in prod” |
| 6.6 Reliability drills | Load + chaos + authorized pentest | Hope |

**Scenario prompt:** Alerts email a list nobody reads; releases are weekend all-hands.

**Expected answer shape:** “I pick SLO burn paging + canary releases because Y, I accept Z (alert SKU budget; freeze when fast-burning).”


Three budgets stay distinct: **dollar** (0.1 / 10.3), **error** (10.1), **quota** (10.7).

**Start from the App Engine dashboard you already used in 1.9.** Rebuild those tiles here, then add Cloud Run, Tasks, Scheduler.

Products:
- **Cloud Monitoring:** Metrics Explorer, dashboards, alerting policies, notification channels, snooze, incidents, metrics scopes (multi-project), MQL / PromQL (Managed Service for Prometheus), uptime checks (HTTP/TCP; public vs private), synthetic monitors, SLO catalog, service monitoring. Managed dashboards for App Engine, Cloud Run, App Hub.
- **App Engine metrics to copy:** `http/server/response_count`, `response_latencies` (p50/p95/p99), codes, instance hours (health **and** 28 F1/day budget).
- **Cloud Run:** request count, latencies, billable instance time, CPU/memory, startup latency.
- **Cloud Tasks:** `cloud_tasks_queue` depth, `task_attempt_count`, `task_attempt_delays`. Alert if depth or delay grows.
- **Cloud Scheduler:** job success/failure, last-run.
- **Cloud Logging:** buckets, views, sinks (GCS/BQ/Pub/Sub), exclusions, log-based metrics, 50 GiB free ingest, retention, CMEK. Audit logs for IR stay Part 7; here they are ops.
- **Cloud Trace:** spans, sampling, W3C / `X-Cloud-Trace-Context`. Pedagogy §6 request-ID becomes the trace ID.
- **Cloud Profiler:** CPU/heap — p95 CPU vs lock.
- **Error Reporting:** grouped exceptions ↔ 5xx.
- **Ops Agent** on GCE (1.8). Cloud Run structured logs auto-ingest.
- **Alerting:** metric-threshold, MQL, log-based, SLO burn (fast 1h + slow 24h). Channels: email, Pub/Sub, PagerDuty/Slack. Alerting **has a SKU** — don’t alert on everything.
- **From scratch:** in-process RED (rate, errors, duration histogram); `/metrics`; SLO calculator `(1-SLO)*events`; burn-rate. Then `custom.googleapis.com/northstar/...` or OTel.
- **Lab:** Northstar dashboard = GAE tiles + Run + Tasks depth + Scheduler last-run. Alert on 5xx and SLO burn. Uptime check on Cloud Run URL. Python/Go: custom metric + list time series.

### 10.1 Reliability + SLO / error budget


Reliability is a **budgeted** property: you measure SLIs, set SLOs, spend error budget consciously, and freeze risk when burning too fast.

#### Concepts
- **SLI examples:** availability = `good/total` (non-5xx / total); latency = fraction of checkouts with latency ≤ threshold; freshness = order-events age.
- **SLO:** e.g. 99.9% monthly → error budget = 0.1% of events in the window.
- **Burn-rate math (derive):** budget fraction `B = 1 - SLO`. Burn rate `R` = (error rate in window) / B. At R=1 you exhaust exactly at window end; **R=14.4** on 1h vs 30d is a common fast-burn page; **R≈6** on 6h vs 30d slow-burn. Implement both (`select_slo_burn_rate` or equivalent).
- **Error budget gates deploys (DORA):** freeze prod while fast-burn is open.
- **Topology:** regional Cloud Run is already multi-zone. Multi-region: dual Run + global LB + multi-region data plane.
- **RPO/RTO:** backup/restore drills (11b P10). Chaos: kill a revision, fail a Pub/Sub push, stall Tasks, miss Scheduler.

#### From scratch (required)
- CSV of `{ts, ok}` → remaining budget calculator; unit test a synthetic outage that trips **fast-burn but not slow-burn** (and the reverse).
- Then Monitoring SLO API / Terraform `google_monitoring_slo`.

#### Lab
- Define checkout availability SLO in Monitoring; wire fast + slow burn alerts to a channel you own.
- Chaos in non-prod first; record budget impact.

#### Gate
- Burn-rate tests green; alert policies checked in; deploy freeze policy written.

#### PCA: 4.3 Chaos / pentest awareness

**Guide themes (matrix):** chaos; pentest (authorized). Homes: 7.4, 10.1.

| Activity | Prefer | Accept |
|---|---|---|
| Chaos | Kill revision / fail push / stall Tasks in non-prod first | Random prod kill without budget |
| Security test | Scoped pentest + fix loop | Unscoped scanning of third parties |
| Gate | Error-budget policy | Ship while fast-burning |

**Scenario prompt:** Someone proposes production chaos on Black Friday without a budget policy.

**Expected answer shape:** “I pick staged chaos tied to error budget because Y, I accept Z (no unsanctioned pentest).”
### 10.2 Operational excellence

Operational excellence is how change reaches production safely and how humans recover when it does not.

#### Concepts
- **DORA metrics:** deployment frequency, lead time, change fail rate, time to restore — measure Northstar pipelines (Part D), do not vanity-screenshot.
- **Environments & promotion:** dev → staging → prod with identical artifacts (digest); Terraform modules per env; no snowflake console clicks as SoR.
- **Runbooks:** Detect → Contain → Eradicate → Recover → Comms (tie 7.8 templates).
- **On-call:** clear ownership, escalation, snooze hygiene; alerts must be actionable (10.0).
- **Postmortems:** blameless; action items with owners; link to error-budget spend.

#### From scratch (required)
- `runbooks/checkout_5xx.md` filled from a real staged failure you caused; timer fields for TTX.
- Script: list Cloud Run revisions; rollback to previous digest (dry-run flag).

#### Lab
- One progressive delivery path (Cloud Deploy or traffic split) documented end-to-end.
- Postmortem template committed; complete one after a staged incident.

#### Gate
- DORA snapshot for last two weeks exists; rollback rehearsed; runbook linked from alert policy.
- Postmortem has at least one completed action item with owner + due date.

#### Decision table
| Change type | Prefer | Avoid |
|---|---|---|
| App release | Canary / digest promote | Big-bang Friday |
| Infra | Terraform PR + plan | Console-only prod |
| Alert | SLO burn + runbook | Email nobody reads |
| Incident | Blameless postmortem | Blame + no actions |
### 10.3 FinOps + API / SKU cost analysis


**Billing export SQL (required patterns — run on export or synthetic tables):**
```sql
-- Top SKUs last 7 days
SELECT service.description AS service, sku.description AS sku,
       ROUND(SUM(cost), 4) AS cost
FROM `billing_export.gcp_billing_export_v1_XXXX`
WHERE usage_start_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 7 DAY)
GROUP BY 1, 2 ORDER BY cost DESC LIMIT 20;

-- Cost by label.service (requires labels on resources)
SELECT labels.value AS service, ROUND(SUM(cost), 4) AS cost
FROM `billing_export.gcp_billing_export_v1_XXXX` t, UNNEST(labels) labels
WHERE labels.key = 'service'
  AND usage_start_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
GROUP BY 1 ORDER BY cost DESC;

-- Idle-ish waste candidates: forwarding rules / static IPs / NAT (filter by sku.description)
SELECT sku.description, ROUND(SUM(cost), 4) AS cost
FROM `billing_export.gcp_billing_export_v1_XXXX`
WHERE REGEXP_CONTAINS(LOWER(sku.description), r'ip|forwarding|nat|load balanc')
  AND usage_start_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
GROUP BY 1 ORDER BY cost DESC;
```
Unit economics: join checkout count from your events table → `$ / 1k checkout`. DuckDB may substitute if export exceeds credits.

### 10.4 Cloud Quotas, consumed APIs, API budgeting


Quota is a budget equal to money: hitting `quotaExceeded` stops product just like an empty billing account.

#### Concepts
- **Cloud Quotas:** allocation vs rate; project/folder/org; increase requests; usage alerts (~80%).
- **Service Usage API:** Terraform-enable only what you need; disable unused APIs.
- **Consumed API metrics** (`serviceruntime.googleapis.com`): `api/request_count`, latencies, `quota/allocation/usage`, `quota/rate/net_usage`, `quota/exceeded`. Filter `service`, `method`, `credential_id`.
- **Two quota planes:** **your** API quotas (Gateway/Apigee — 3.3) vs **Google** API quotas (your project calling Google).
- **Billable APIs** (Maps, Gemini): quota **and** SKU — cap with org policy + Monitoring.

#### From scratch (required)
- Token-bucket (§6 / Pedagogy) *is* a rate quota — already owned; script: Cloud Quotas API or Metrics API → % used for one metric; exit non-zero if > N%.

#### Lab
- Metrics Explorer on Consumed API for `run.googleapis.com` or `compute.googleapis.com`. Alert at 80%.
- Document a quota increase you do **not** file unless needed.
- **Python / Go:** query `api/request_count` by method; fail CI if last hour > N.

#### Gate
- 80% alert exists; unused APIs listed for disable; CI guard optional but demonstrated once.

#### Decision table
| Symptom | Prefer | Avoid |
|---|---|---|
| Near limit | Alert + optimize callers | Silent increase forever |
| Runaway key | Disable key + quota alert | Only budget $ alert |
| Unused API surface | Disable API | Leave enabled “just in case” |
### 10.5 Performance

Performance work starts with a measured bottleneck, not a larger machine.

#### Concepts
- **Cloud Run concurrency:** too low → more instances/cost; too high → tail latency / memory pressure. Load-test to choose.
- **Connection pooling:** SQL and Firestore client pools sized to instance concurrency (Part 2 pool ADR).
- **CDN cache hit ratio:** catalog static/edge cache (1.4 / 6.13); miss storms hit origin.
- **Payload size:** truncate lists; pagination (cursor); compress where appropriate; avoid huge JSON on mobile.
- **Profiler / Trace:** Cloud Profiler + Trace (10.0) before rewriting algorithms.

#### From scratch (required)
- Benchmark harness: p50/p95 for `GetProduct` with and without cache; assert cache improves p95 under identical load script.
- Connection pool math worksheet: `max_instances * concurrency ≤ DB max_connections` headroom.

#### Lab (free-tier boxed)
- Load script against Cloud Run (modest QPS); capture concurrency setting; CDN hit ratio dashboard if CDN enabled.
- One Profiler capture on a CPU-heavy path (or local pprof for Go).

#### Gate
- Pool ADR numbers; before/after p95 recorded; no “optimize everything” PR without Trace link.
- Payload size budget written for catalog list (bytes / item).

#### Decision table
| Symptom | Prefer | Avoid |
|---|---|---|
| High p95 cold start | Min instances / startup CPU (cost trade) | Blind max concurrency |
| DB saturates | Pool + instance caps | Unlimited scale-out |
| Origin overload | CDN + cache-aside | Bigger SQL only |
| Huge JSON pages | Cursor + field mask | Unbounded list |
### 10.6 Sustainability

Sustainability is a Well-Architected pillar (added to Google’s framing — treat region carbon and idle compute as first-class design inputs, not afterthoughts).

#### Concepts
- **Region carbon intensity:** prefer lower-carbon regions when latency/residency allow; document the trade.
- **Scale-to-zero:** Cloud Run / scale-to-zero friendly designs cut idle energy and dollars — align FinOps (10.3) with carbon.
- **Right-sizing & teardown:** e2-micro labs, destroy Memorystore/Spanner trials, idle IP deletion (6.3) are sustainability controls.
- **Data lifecycle:** Nearline/Archive and Autoclass (2.5) reduce footprint of cold bytes.
- **Measurement literacy:** carbon reports / region pickers as available — do not invent fake precision.

#### From scratch (required)
- Cost+carbon one-pager for Northstar: list always-on vs scale-to-zero components; estimate idle hours eliminated by moving a service from GCE to Cloud Run.

#### Lab
- Pick a primary region with residency + carbon note in ADR.
- Verify no idle external IPs / unused disks after teardown script.

#### Gate
- ADR mentions carbon/region; teardown checklist includes idle resources; scale-to-zero defended for non-latency-critical paths.
- Idle IP / unused disk check appears in weekly FinOps script (10.3).

#### Decision table
| Need | Prefer | Avoid |
|---|---|---|
| Spiky HTTP API | Cloud Run scale-to-zero | Always-on GCE for idle API |
| Residency vs carbon conflict | Residency wins + note | Ignore both |
| Cold data | Lifecycle/Autoclass | Hot Standard forever |
| Forgotten lab | Same-day destroy | “We’ll delete later” |
### 10.7 Linux / OS internals (earned, after GCE + Cloud Run)

You earn OS depth **after** operating GCE and Cloud Run — so every concept maps to something you already deployed.

#### Concepts
- **Namespaces & cgroups:** what isolate pid/mount/net/user and what limits CPU/memory — Cloud Run abstracts; GCE shows the raw shape.
- **Container contract origin:** non-root, RO FS, capabilities — kernel features, not fashion (1.2, 7.5).
- **Packet path recall:** TCP handshake, TLS handshake, HTTP/2, gRPC — drawn in Part 6; observe with `ss`/`tcpdump` only on **your** VMs.
- **Filtering layers:** iptables/nftables on guest vs VPC firewall vs Cloud NGFW vs Cloud Armor — different planes.
- **T-OS (required, not optional):** scheduling classes; page tables intuition; inode vs dentry; deadlock four conditions — predict then observe on the e2-micro.

#### From scratch (required)
- On e2-micro (Always Free eligible regions): write a tiny C or Go program that allocates, forks, or locks; predict `/proc` and `ps` output before running.
- Deadlock demo: two mutexes, wrong order — then fix; test detects hang via timeout.

#### Lab (free-tier boxed)
1. e2-micro via IAP SSH; no public IP.
2. Observe cgroup limits inside a container vs on the VM.
3. Map one Cloud Run OOM to cgroup memory; fix requests/limits story.
4. Tear down VM same sitting if not your standing free micro.

#### Gate
- T-OS predictions written then checked; deadlock fixed; can map Cloud Run memory limit to cgroup; no scanning others’ hosts.

#### Decision table
| Question | Observe on | Avoid |
|---|---|---|
| Who kills OOM? | cgroup / Run metrics | Guessing without metrics |
| Why TIME_WAIT? | Your VM `ss` | Random internet scans |
| Policy deny | VPC FW vs Armor | Mixing planes in one rule lore |
## Part 11 — Capstone and PCA

### Capstone: Northstar v1 (must run on free tier)

Ship a stranger-demoable Northstar on Always Free / free-trial boxes. Credits-optional resources must have teardown evidence.

A stranger can:
1. Open the hosted frontend.
2. Sign up (Identity Platform).
3. Browse catalog, add to cart.
4. Pay with Stripe test card.
5. See order `paid` only after webhook.
6. Receive an async notification path (email stub or in-app inbox via Pub/Sub).
7. You show: Terraform (or equivalent IaC), Cloud Build + WIF, per-service SAs, Secret Manager, budget alerts, ADRs, threat model, SLO, cost model, runbook.
8. OLTP schema + migrations exist (Postgres). Live Cloud SQL if credits; Docker Postgres if not. Either way the Terraform for Cloud SQL is in the repo.
9. ADRs covering Cloud Run vs App Engine vs GCE for the API, and Cloud SQL vs Firestore vs Spanner for orders.
10. Bloom-filter negative cache on catalog; cursor pagination; Cloud SQL pool-size ADR; load-shed on checkout; outbox (not dual-write); proto-stable internal gRPC.
11. Dashboard (GAE-shaped tiles + Run + Tasks depth + Scheduler), SLO + burn-rate alert, billing SKU report, quota alert, unit-economics one-pager.
12. Optional: one ML slice from 9c behind a port (ranker, fraud score, ETA, or RAG).

#### Acceptance tests (automated + demo script)

| # | Capability | How you prove it |
|---|---|---|
| 1 | Hosted frontend | Public HTTPS URL loads; curl/smoke in demo script |
| 2 | Sign up | Identity Platform user created; duplicate email rejected |
| 3 | Catalog + cart | Cursor page; add/remove line; totals match fixtures |
| 4 | Pay (test mode) | Stripe Checkout/Elements; Secret Manager for sk; test cards only |
| 5 | Webhook truth | `paid` only after verified webhook; redirect-alone → `pending_payment`; replay idempotent |
| 6 | Async notify | Pub/Sub/Tasks delivers stub; duplicate → one effect (inbox) |
| 7 | Platform evidence | IaC plan; WIF deploy (no JSON key); budget alert; ADR/threat/SLO/cost/runbook links |
| 8 | OLTP | Migrations up/down; Docker or Cloud SQL; Cloud SQL TF in repo either way |
| 9 | ADRs | Compute + storage picks with “I pick… accept…” |
| 10 | Hardening | Bloom + cursor + pool ADR + load-shed + outbox lint + proto stable |
| 11 | Ops | Dashboard + burn-rate alert + SKU report + quota alert + unit economics |
| 12 | Optional ML | Port + offline metric for one 9c slice |

**Negative tests (required):** unauthenticated checkout fails; cross-tenant cart access fails; webhook bad sig fails; no migrate-on-request.

Deliverables: HLD deck, LLD pack (OpenAPI + `.proto`, ERD/DDL, sequences, firewall policy, IAM, hexagonal layout), Python services, Go ports of at least **two** services, GCE e2-micro and App Engine labs documented (can be torn down), lab teardown checklist signed.

**Gate:** demo script green on a clean project; teardown leaves no idle external IPs / Memorystore / forgotten LB; PCA case HLDs unlocked only after this gate.
### PCA alignment (v6.1)
Not a dump of dumps. After capstone:
- Map every ADR to an exam domain.
- Four official case studies below — structured HLD each (read the official Google case text first; do **not** invent a fifth case).
- Practice the exam skill: pick the *Google-preferred managed* option unless a constraint forbids it.
**Part 11 gates:** same as the spine “initial course complete when,” plus the e2e demo. Optional ACE if IAM/`gcloud` is still shaky.

#### Case HLD template (use for all four)
For each case deliver one page: **Business** → **Constraints** → **Compute / Data / Net / IAM / Ops** → **Trade-offs** → closing line “I pick X because Y, I accept Z.”

#### Altostrat Media — HLD
- **Business:** Media library (podcasts, interviews, news, documentaries); modernize CMS/engagement with generative AI — recommendations, natural-language interaction, 24/7 self-service; revenue via dynamic pricing/targeted marketing; reliability and cost management are executive priorities.
- **Constraints:** Already substantially cloud-native (GKE, GCS, BigQuery, Cloud Run functions) with remaining on-prem ingestion/archive; hybrid connectivity required; AI must detect/filter inappropriate content and stay auditable/explainable; storage cost as volumes grow; CI/CD modernization for containers.
- **Compute:** Keep customer-facing on GKE; event work on Cloud Run functions; Vertex / Conversational Agents / Vision–Video–NL APIs for summaries, metadata, moderation; GKE Enterprise when on-prem+cloud Kubernetes consistency is required.
- **Data:** GCS media + lifecycle/Autoclass; BigQuery for behavior/consumption analytics; Workflows/Pipelines for enrichment.
- **Net:** Secure high-performance hybrid (Interconnect primary, HA VPN backup) for ingestion.
- **IAM / security:** Model Armor + Sensitive Data Protection; Explainable AI / governed endpoints; Binary Authorization on deploy path; IAP where admin UIs exist.
- **Ops:** Centralize CI/CD (Cloud Build + Cloud Deploy + Artifact Registry); replace email-only alerts with Cloud Monitoring policies; cost dashboards on storage classes.
- **Trade-offs:** “I pick layering GenAI on the existing GKE/BQ/GCS estate + Autoclass because Y, I accept Z (no big-bang rewrite of working delivery; Interconnect cost vs reliability).”

#### Cymbal Retail — HLD
- **Business:** Fast-growing online retailer; three tracks — (1) generative catalog/content enrichment, (2) conversational commerce + product discovery, (3) stack modernization; cut call-center staffing and data-center hosting cost; raise conversion.
- **Constraints:** Mixed on-prem/cloud; MySQL/SQL Server/Redis/Mongo; Kubernetes apps; legacy SFTP/ETL; IVR + human agents; fragmented open-source monitoring; **associates must review** generated content before catalog updates; customer data in virtual-agent flows must meet regulations.
- **Compute:** Autoscale GKE/Cloud Run commerce services; Conversational Agents replacing IVR; Vertex AI Search for NL discovery; Imagen-class models for image variations.
- **Data:** Supplier landing on GCS → Vision/NL/Document AI → HITL review store → production DBs; DMS/Datastream into BigQuery; Memorystore for Redis-shaped cache.
- **Net:** Private paths for data; Armor at public edge; no customer PII on public buckets.
- **IAM / security:** SDP, SCC, Assured Workloads as needed; least-privilege SAs for enrichment pipeline; no PAN in ML features.
- **Ops:** Consolidate Grafana/Nagios/Elastic → Cloud Monitoring; progressive delivery for storefront.
- **Trade-offs:** “I pick Conversational Agents + Vertex AI Search + HITL catalog pipeline because Y, I accept Z (no auto-publish of generated content; migrate DBs with DMS, not weekend hope).”

#### EHR Healthcare — HLD
- **Business:** SaaS EHR for clinics/hospitals/insurers; replace colo (lease pressure); onboard insurers fast; **≥99.9%** availability for customer-facing systems; healthcare insights/predictions; lower admin cost; reduce latency; regulatory compliance (HIPAA-class via BAA).
- **Constraints:** Web apps recently containerized; mixed MySQL/SQL Server/Redis/Mongo; **legacy insurer file/API integrations stay on-prem for years**; AD identities; ignored email alerts; hybrid must remain.
- **Compute:** Regional multi-zone GKE for customer-facing; GKE Enterprise for consistent container ops across environments; avoid over-building multi-region Spanner for a 99.9% ask.
- **Data:** Cloud SQL HA (+ Memorystore); Pub/Sub + Dataflow for new insurer feeds → BigQuery analytics; DMS for DB moves.
- **Net:** Dedicated/Partner Interconnect (+ HA VPN backup); no PHI over unmanaged public paths.
- **IAM / security:** Cloud Identity Federation / AD sync patterns; CMEK where custody requires; VPC-SC for sensitive projects; audit logs retained.
- **Ops:** Cloud Monitoring/Logging replace ignored email; Cloud Build + Cloud Deploy; capacity via autoscaling + IaC.
- **Trade-offs:** “I pick regional HA GKE + Cloud SQL HA + Interconnect because Y (meets 99.9% and hybrid), I accept Z (insurer interfaces remain on-prem; not multi-region active-active).”

#### KnightMotives Automotive — HLD
- **Business:** Global OEM (BEV/hybrid/ICE + autonomous); modernize in-vehicle and shop/buy/service experience in ~5 years; monetize corporate data to fund AI; improve unreliable build-to-order; better dealer/technician tools.
- **Constraints:** Largely on-prem + some multi-cloud; outdated mainframe supply chain + ERP; fragmented vehicle codebases; **dealers have no hardware budget**; rural coverage gaps; past breaches; **EU data protection** for autonomous platform; Cloud IoT Core is retired.
- **Compute:** GKE Enterprise for gradual hybrid modernization; Cloud Run/App Engine + IAP for **cloud-hosted** dealer portal; Vertex + accelerators (Hypercomputer/TPU as needed) for AV training/simulation — not a one-step mainframe rewrite.
- **Data:** Partner MQTT → Pub/Sub → Dataflow → Bigtable (telemetry) + BigQuery/Dataplex (governed monetization); Apigee for partner/dealer APIs.
- **Net:** Network Connectivity Center; Interconnect/VPN to plants; edge buffering for offline-tolerant vehicles.
- **IAM / security:** SCC, SDP, CMEK, Binary Authorization for vehicle software supply chain; Assured Workloads + location org policies for EU.
- **Ops:** Phased waves; Apigee façades in front of mainframe/ERP; SLOs on dealer portal and ingestion lag.
- **Trade-offs:** “I pick Pub/Sub/Dataflow/Bigtable + governed BQ + cloud dealer portal + Apigee façades because Y, I accept Z (no dealer appliances; no IoT Core; no big-bang ERP rewrite).”

### Part 11b — Control-plane capstone (after Northstar v1)

Second integration, not a replacement for Northstar. Do not start until Northstar v1, Part 4 identity (including hardened HTTP), Part D enough to ship, and 10.0 tiles are unlocked. Python models stay behind typed contracts; the control plane is Go-first with Python allowed at the adapter. CLI (**G5**), concurrency in the worker (**G6–G7**), and release image (**G18**) are P0/P7/P8, not a prior language semester.

**Inventory (GCP-mapped):** API gateway (Cloud Run + IAP or API Gateway), backend API, auth service, router (9c.5 RAG), registry (Artifact Registry + metadata in SQL/Firestore), chat/history store, orchestrator + worker (Cloud Tasks / Pub/Sub + Cloud Run Jobs + Cloud Build), CLI, sample agents (authenticated JSON-RPC). Optional: Memorystore streams/cache, object storage.

**Flow:** upload artifact → registry → build request → worker build/deploy → registry discover → gateway route → router shortlist → model pick → chat logged → traces.

| Phase | Output | Acceptance tests (how) | GCP mapping |
|---|---|---|---|
| P0 | Go monorepo, dev loop, tooling | `go test ./...`; `gofmt`/`vet` clean; `make run` boots; module graph pinned; CI module cache | Cloud Shell / local; Artifact Registry later |
| P1 | Shared config, secret-safe logs, traces, error model, hardened servers/clients, ordered middleware | Logs redaction test (secret patterns fail CI); timeouts on all HTTP clients; trace ID propagates; middleware order test; panic recover = 500 without stack leak | Cloud Logging; Cloud Trace; Secret Manager for config refs |
| P2 | SQL auth/audit schema, tenant constraints, migrations, transactions, backup invariants | Migration up/down; tenant isolation SQL test; tx rollback test; backup restore dry-run script; dirty migration blocks deploy | Cloud SQL / Postgres Docker; GCS backup bucket |
| P3 | Handlers, repositories, password/OIDC, sessions, JWT validation, CSRF/CORS, idempotency, pagination | Authz matrix table tests; CSRF negative; JWT alg confusion rejected; idempotent POST; cursor page stable; session revoke works | Identity Platform / IAP; Cloud Run services |
| P4 | Registry + gateway identity, scoped credentials, route authorization, health, stale cleanup | Route deny-by-default; stale artifact GC; `/healthz` fails if dependency down; digest immutability check | Artifact Registry; API Gateway or IAP+URL map |
| P5 | Embeddings behind a contract, shortlist/rerank, structured model pick, offline eval, tenant/data boundaries, tool guardrails | Eval set score floor; cross-tenant retrieve fails; tool allowlist test; schema-validated pick; prompt PII redaction | Vertex embeddings / Model Garden; VPC-SC as needed |
| P6 | Authenticated history ingest, object/tenant/field authz, append-only audit, retention | Append-only trigger/test; field-level deny; retention job deletes only expired; export respects authz | Firestore/SQL; GCS objects; DLP optional |
| P7 | Queue/stream worker, short-lived identity, provenance, deploy/rollback, idempotent consumers | Duplicate message → one effect; rollback revision test; provenance attestation present; worker honors ctx cancel | Cloud Tasks / Pub/Sub; Cloud Build; Cloud Run Jobs |
| P8 | CLI, device/browser login, least-privilege commands, no credential leakage | CLI help; `TestCLINoSecretStdout`; command authz tests; config file mode bits documented | `gcloud` patterns; WIF for automation |
| P9 | Authorized agent protocol, card validation, per-tool policy, replay control, stream limits | Replay rejected; tool policy deny; stream size cap; AgentCard schema validate; rate limit per agent | Cloud Run JSON-RPC; IAM + app authz |
| P10 | SLOs, dashboards, load/abuse/fuzz/race, secret scans, key rotation, backup/restore, incident, **ORR** | Burn-rate alert config tested; `go test -race`; fuzz harness; secret scan clean; restore drill recorded; ORR checklist signed | Cloud Monitoring dashboards; SCC; Part 7 runbooks |

**ORR must show, not claim:** data-flow and trust-boundary diagram; abuse register; authorization matrix; identity propagation with no network-location trust; deny-by-default tests; session/JWT fixation/replay/revocation; bounded inputs; no secrets in logs/images/prompts; `go test` + race + fuzz; alerts with owned runbooks; rehearsed key rotation, rollback, restore. Each P0–P10 row above is incomplete without its acceptance column passing in CI.

**11b Gate:** P0–P10 acceptance columns green in CI; ORR packet reviewed; Northstar v1 demo still green (no regression of Part 11).

**Spec inventory (required, GCP-mapped). Explicitly dropped:** n8n, NANDA, Kong plugin YAML, Mongo as SoR — those were another stack; concepts (workflow credentials, agent cards, gateway plugins) map as follows.

| Spec group | This course |
|---|---|
| Backend health, upload, access, user registration | Cloud Run services + Identity Platform |
| Build/deploy/update/rollback | Cloud Build + Cloud Deploy / Cloud Run revisions |
| Registry + AgentCard/skills/upload status | Artifact Registry + SQL/Firestore metadata schema (card JSON, skills, status) |
| Chat session/history, JSON-RPC `message/send` | Authenticated HTTP/JSON-RPC on Cloud Run; append-only history table |
| Auth service, GitHub OAuth | Part 4 labs + Identity Platform + IAP |
| Router algorithm (shortlist → rerank → structured pick) | 9c.5 / P5; documented as `ALG-ROUTE-001` equivalent: embed → kNN/shortlist → rerank → JSON schema pick |
| Tool calling, per-tool policy, replay | P9; IAM + app authz |
| Jobs | Cloud Tasks / Pub/Sub (not Redis streams required) |
| Gateway routes/plugins | API Gateway or IAP + Cloud Armor; URL map |
| CLI commands, config matrix | 0.1 billing CLI + P8 |
| Infra/ops/tests | Terraform, Cloud Build, Part 10 dashboards |
| SQL teaching schema, query-performance fixture, transaction fixture | Part 2 |

Schemas to write: AgentCard, skills, upload status, agent build, deployment, session, message, GitHub credential handle (never raw), plus the Part 2 fixtures.

---

## Exercise engine (how teaching will actually work)

For each numbered subtopic when teaching starts, **walk Pedagogy §7** (do not skip rungs):

```
1–5  Concrete → vocab → representation → core move → one worked illustration
6–7  From-scratch write (basic + routine) — Python, then Go after submit
8    Mixed: HLD/LLD using this idea + exactly two earlier unlocked Northstar pieces
9    Top rung (after mixed): GCP lab / production failure / ADR / adversarial drill
10   Reflection + ledger stamp (part · sub-topic · rung · unlocked · shaky · postponed · next)
```

Lab steps (gcloud/Terraform, free-tier boxed) sit on rungs 7–9 as appropriate. The routine then GCP-wired write is Python first, Go after submit. Review notes: what the toy got wrong vs the managed product.

Sample of early Python exercises (illustrative, not started):
- Billing export aggregator (Run, GCE, GAE, SQL SKUs).
- Cloud Run container-contract server.
- Compute Engine API: list / start / stop / label the sandbox VM.
- App Engine-compatible handlers (same tests as Cloud Run).
- ERD + Alembic migrations + transactional stock decrement (Postgres).
- Cloud SQL connector (IAM auth) against local proxy.
- Signed URL issuer.
- Firestore transactional stock decrement (second backend).
- VPC firewall 5-tuple allow/deny engine.
- OIDC ID-token service-to-service client.
- JWT authn middleware + RBAC.
- Stripe webhook verifier + idempotency store.
- Pub/Sub publisher with outbox.
- Audit-log detector.
- Multi-stage Dockerfile (Python then Go distroless).
- Cloud Build `cloudbuild.yaml` that fails on a red test and on a planted secret.
- DORA metric calculator from a deploy log.
- Env-repo digest bumper (GitOps CI step).
- Binary Authorization policy evaluator (allow/deny a fake image).
- kind: generate Deployment YAML + apply + wait for Available.
- Minimal HTTP/1.1 server on a raw TCP socket.
- L7 reverse proxy (round-robin + health check).
- In-process CDN cache (TTL, ETag, 304, LRU).
- Ephemeral vs static IP lease allocator (CIDR).
- Userspace NAT mapping table.
- Token-bucket rate-limit middleware.
- JWT HS256 sign/verify middleware; then RS256 + JWKS.
- In-memory Pub/Sub (ack deadline + DLQ).
- Append-only WAL + hashmap (toy KV).
- Reconcile loop (desired vs actual).
- Protobuf varint encode/decode vs `protoc` golden file.
- Bloom filter + false-positive-rate tests.
- Consistent-hash ring (vnode remap %).
- Singleflight cache fill.
- Load-shed middleware (queue depth).
- Cursor pager `(created_at, id)`.
- Mini-QUIC: two UDP streams, loss on stream 1, stream 2 continues.
- RED metrics + SLO remaining-budget from a CSV of requests.
- Cloud Tasks enqueue + idempotent handler.
- Cloud Scheduler create/pause (stay within 3 jobs).
- Consumed-API request_count grouped by method (Monitoring API).

Each has a Go twin after submission.

---

## Appendix B — Bibliography (Go, software, architecture, security, discrete math)

Use as a hierarchy: official language and product docs first, then these texts. Security: governing RFC/BCP, then NIST/ASVS, then cheat sheets; record the date checked.

**Go and CS:** Donovan and Kernighan, *The Go Programming Language*; Bodner, *Learning Go*; current Go `net/http`, `crypto/*`, `context`, testing, race detector, and release notes. Rosen or Grimaldi (discrete math). CLRS; Sedgewick & Wayne. Silberschatz/Galvin/Gagne *Operating System Concepts* and Tanenbaum *Computer Networks* when Part 10.7 / 6.1 need a text.

**Architecture and SE:** Evans, *Domain-Driven Design*; Fowler, *Patterns of Enterprise Application Architecture*; Bass et al., *Software Architecture in Practice*; Richards and Ford, *Fundamentals of Software Architecture*; Newman, *Building Microservices*; Kleppmann, *Designing Data-Intensive Applications*; Google SRE work; Microsoft REST API Guidelines; *Software Engineering at Google*; Fowler *Refactoring*.

**Data:** current PostgreSQL documentation (and source when a DB-4–10 toy needs it).

**Auth/security standards:** HTTP Semantics; cookie specs; RFC 7519 and RFC 8725 (JWT); OAuth PKCE RFC 7636; RFC 8414, 8705, 9126, 9207, 9449, 9700; OpenID Connect Core; NIST SP 800-63B; OWASP ASVS and current cheat sheets (authn, session, authz, CSRF, REST, SSRF, logging, secrets, supply chain).

**Production ML / systems:** Huyen; Lakshmanan/Robinson/Munn *Machine Learning Design Patterns*; Google SRE; DORA.

## Appendix C — Initial-course coverage (bibliography as gate)

Each Part’s ADR or lab write-up must **use** (cite a section, not a vibe) at least one of:

| Part | Must appear |
|---|---|
| M.NS | Higham and/or IEEE 754 |
| 0 | Cloud Billing / IAM docs |
| 2–3 | Kleppmann DDIA (storage, replication, or queues as used) |
| 3.0 | Evans or Fowler PoEAA — one pattern with a **force** |
| 4 | RFC 7519/8725 or NIST 800-63B or ASVS — one control |
| 6 | Kurose or Tanenbaum — one mechanism (window, routing, or DNS) |
| 8 | Primer building block + GCP product in the same ADR |
| 9b–9c | **PMLE official exam guide** (as of 1 Jun 2026 — Agent Platform, BQML, Model Garden) **must-cite** in the ADR/lab; plus official BQML/Agent Platform/Model Garden doc for the product you chose; **M.ML** derivation in the notebook |
| 10 | Google SRE — SLI/SLO or toil |
| 11 | PCA exam guide case + Well-Architected pillar |

Not extra homework: if the write-up cannot point to a page, the part is not complete.

## Appendix I — Institutional CS/math texts and extra tracks

IIT/IISc BTech/MTech CSE cores map to owners above; texts extend Appendix B (do not duplicate). Required tracks (ARCH/OS/NET) are in Parts 1.8, 10.7, 6. Other T-* only when that owner opens them. Never a second spine.

**Systems:** Hennessy and Patterson, *Computer Organization and Design*; Silberschatz, Galvin, Gagne, *Operating System Concepts*; Kurose and Ross, *Computer Networking*; Tanenbaum and Wetherall, *Computer Networks*; Aho, Lam, Sethi, Ullman, *Compilers*.

**Theory:** Sipser, *Introduction to the Theory of Computation*; CLRS (already B); Arora and Barak, *Computational Complexity* only if T-TOC is opened to that ceiling; Hopcroft, Motwani, Ullman automata as T-TOC need (WFST/Kaldi-style ASR depth is out of syllabus).

**Math as used:** Strang (LA); Boyd and Vandenberghe, *Convex Optimization* (T-OPT); Cover and Thomas, *Elements of Information Theory* (T-IT); Higham, *Accuracy and Stability of Numerical Algorithms* (**M.NS**); IEEE 754. West, *Introduction to Graph Theory* only if 8.1 needs a graph-theory text beyond CLRS.

**Security theory:** Katz and Lindell, *Introduction to Modern Cryptography* (T-CRYPTO). Goldreich as further reading. Implementation remains vetted stdlib.

**AI/ML (production / IR — keep):** Russell and Norvig, *AIMA* (as used); Manning, Raghavan, Schütze, *Introduction to Information Retrieval* (9c.2 / IR literacy); Raschka, *Build a Large Language Model (From Scratch)* only for attention/LoRA slivers when **9c.5** needs them; Huyen *AI Engineering* for **9c.5** / **9c.7** production.

**AI/ML demoted (not Part 12 domain dumps):** Goodfellow, Bengio, Courville, *Deep Learning* — optional external / **T-DL** reading only; **not** a Part 12 from-scratch-DL course text. Full CV PhD texts (e.g. Szeliski), DSP/Kaldi/OpenFst tool courses, and Dive-into-DL-as-semester are **out of syllabus** — production speech/CV stays **9c.6** serving literacy.

**Archive (not taught unless an owner names a slice):** Dummit and Foote; Munkres; Ahlfors; Royden; do Carmo; Enderton; Evans PDE; school-level arithmetic series; game-engine and medical inventories.

## Appendix T — Chapter maps (reading, not order)

Use the owner’s bibliography; chapters are entered only when that owner is taught.

| Text | Enter through |
|---|---|
| Sipser 1–5, 7 | T-TOC |
| H&P pipeline/cache/VM chapters | T-ARCH / 1.8 |
| Silberschatz process/VM/FS/sync | T-OS / 10.7 |
| Kurose 1–5 | Part 6 / T-NET |
| Dragon book front/middle/back | T-PL |
| Boyd 2–5, 9 | T-OPT |
| Cover/Thomas 2, 7 | Part M / T-IT |
| Katz/Lindell 1–5 | T-CRYPTO |
| Goodfellow 6–8, 9 | Optional external / T-DL only (not Part 12 DL course) |
| Manning IR 1–6, 8 | 9c.2 / T-NLP |
| Raschka LLM-from-scratch 1–4, app. LoRA | 9c.5 / T-DL |
| Huyen AI Engineering 3–9 | 9c.5, 9c.7 |

## Official reading list (course texts, not extras)

- Well-Architected Framework (all six pillars + FSI perspective when we hit payments).
- Landing zone series (identity, hierarchy, network, security).
- Cloud Run docs: container contract, resource model, auth, Direct VPC.
- Compute Engine: VM, MIG, disks, IAP SSH, VM Manager.
- App Engine: standard vs flexible, services, versions, traffic splitting.
- Cloud SQL: HA, Auth Proxy, private IP, IAM DB auth; AlloyDB and Spanner decision docs.
- Cloud NGFW / hierarchical firewall; Cloud Armor; IAP; VPC Service Controls.
- Security Command Center; Sensitive Data Protection; Cloud KMS; Binary Authorization.
- Identity Platform vs Firebase Auth comparison.
- PCI DSS compliance in GCP + limiting PCI scope.
- Application Design Center three-tier web app.
- Cloud Build, Cloud Deploy, Skaffold, Artifact Registry, Binary Authorization, SLSA.
- Modern CI/CD with GKE reference architecture; GitOps-style CD with Cloud Build.
- DORA metrics; Well-Architected operational excellence.
- PCA exam guide v6.1 + the four case studies.
- System-design topic index and worked studios (Part 8).
- Industry ML system-design catalog (Appendix M; taught as Part 9c families).
- Donne Martin `interactive-coding-challenges` used only as the style model for exercise notebooks — GCP exercises are original.
- Cloud CDN overview, cache modes, best practices; Compute Engine / VPC IP address docs (ephemeral vs static, regional vs global).
- RFC 9111 (HTTP caching), RFC 7519 (JWT), protobuf encoding, RFC 9000 (QUIC concepts only) as from-scratch specs.
- Bloom filters; consistent hashing; DDD/hexagonal as used in Northstar, not as a second course.
- Cloud Monitoring SLO / burn-rate; Cloud Quotas; consumed API (`serviceruntime`) metrics; Cloud Tasks observability; Cloud Scheduler; App Engine metrics (`http/server/*`).

---

## What this course will not do

- Isolated Linux month before GCP; live Cloud SQL/GKE/global LB as **required** (Terraform + local Postgres + free-tier Run/GCE/GAE suffice).
- Storing PAN; homemade TLS/AES/RSA; attacking systems you do not own; PCA dumps as architecture class.
- A second teaching order before billing; a second Go semester (Appendix G is an index); duplicate SOLID/gRPC/QUIC homes.

---

## PCA v6.1 coverage matrix (every official bullet has a home)

**Index only** — teaching text is the `#### PCA: …` blocks under owner parts (not duplicated here). Use this table to navigate.

| Exam | Bullet | Course home |
|---|---|---|
| 1.1 | Business requirements, NFR, BCP, cost, integration, data movement, trade-offs, build/buy, KPI/ROI, security, observability | F2, 0.4, 8, 10, 11 |
| 1.2 | WAF, HA/failover, flexibility, scale, performance, Gemini Cloud Assist, backup/recovery | 1.12, 8, 9b, 10 |
| 1.3 | Hybrid/multicloud, ML/AI (Gemini, Agent Builder, Model Garden, Hypercomputer), VPC/peering/FW/LB/routing/containers/Shared VPC/PSC, data processing, storage types, GKE/Cloud Run/functions, spot/custom/specialized compute | 1, 2, 6, 8b, 9, 9b |
| 1.4 | Migration Center, methodologies, licenses, diagrams | 8c |
| 1.5 | Cloud-first, evolution | 8, 11 |
| 2.1 | Hybrid, multi-cloud, IPS/FW, VPC, LB | 6, 8b |
| 2.2 | Storage allocation, processing, access, transfer/latency, lifecycle, growth, backup | 2 |
| 2.3 | Provisioning, spot vs standard, GCE/GKE/serverless/GCVE networking, orchestration/patch, containers, serverless | 1, 9, 8b |
| 2.4 | Vertex Pipelines, data integration, Hypercomputer/GPU/TPU | 9b |
| 2.5 | Google AI APIs, Gemini Enterprise, Model Garden | 9b |
| 3.1 | IAM, hierarchy, KMS/secrets, SoD, audit/VPC-SC/CAA/org policy/hierarchical FW, IAP/impersonation/Chrome Enterprise/WIF, supply chain, Model Armor/SDP | 0.3, 0.5, 4, 7, D5, 9b |
| 3.2 | HIPAA/COPPA/privacy/sovereignty, PCI/PII, SOC 2, audits | 5, 7.9 |
| 4.1 | SDLC, CI/CD, RCA, testing, service catalog, DR | D, 1.6, 10 |
| 4.2 | Stakeholders, change, skills, decisions, customer success, CapEx/OpEx, BCP | F2, 0, 10, 11 |
| 4.3 | Chaos, pentest | 7.4, 10.1 |
| 5.1 | Deploy, Apigee, test frameworks, migration tooling, Gemini Cloud Assist | D3, 3.3, 8c, 9b |
| 5.2 | Cloud Shell/Code, gcloud/gsutil/bq, emulators, Terraform, API clients | F4, 0.2, 2.7, all labs |
| 6.1–6.6 | WAF ops pillar, monitoring/logging/profiling/alerting, release mgmt, support, QC, chaos/load | D0, D4, 10 |

Case studies (required reading before Part 11): Altostrat Media, Cymbal Retail, EHR Healthcare, KnightMotives Automotive. — structured HLDs live under Part 11 PCA alignment (four only).

---

## Part 12 — Continuation (after 11b)

Do **not** open this part until Northstar v1 and 11b are done or skip-tested. Pedagogy §§7–8 still apply. This part is the **single graph-ordered continuation** for graduate-depth math, ML, and CS that remain after the initial track closes — not a second parallel spine before 11b.

**Initial track closable without Part 12.** F–11b plus Northstar/11b evidence is enough to close PCA/PMLE literacy for the initial course. Part 12 is optional continuation depth: full algebra/calculus/spectral work, DB/engine depth, full RL/causal/OR, services/security/architecture, and S24 archive slices. Do not delay 11b for Part 12. Pure DSP/Kaldi, full CV PhD, transformer-from-scratch, and five GenAI portfolios are **out of syllabus** — production speech/CV serving stays **9c.6**; GenAI/RAG production stays **9c.5**.

**Language ownership (reminder).** Python first for math, numerical methods, probability/statistics, classical ML continuation, and production-ML eval primitives (NumPy-level scratch before library shortcuts). Go first for DS/algo, DB toys, APIs, auth/middleware, concurrency, distributed systems, HLD/LLD labs, operations, and the control-plane capstone. Production ML is hybrid: model/eval in Python; service boundaries, gateways, evaluators, registries, rollout, and observability in Go. Cloud/MLOps/vector DBs are tool-backed after the concept is clear. Pure DSP/CV/ASR/from-scratch-transformer tracks are **out of syllabus** (not Part 12 language work). Cryptographic algorithms stay in the Go standard library or vetted packages — **never invent** a cipher, hash, password KDF, signature scheme, RNG, or TLS variant.

**Skip-test (strengthen, do not re-teach).** If F–11b already confirmed the same artifacts, stamp the stage complete and do not re-teach. Approximate overlap:

| Continuation stage | Initial-track owner | What skip-test confirms |
|---|---|---|
| S12 / S13 | Part 2 (SQL + Cloud SQL / engine literacy) | FDs, joins, transactions, pagination, planner/`EXPLAIN` literacy as gated in Part 2 |
| S18 | 3.2 (gRPC / contracts) | Resource semantics, protobuf compatibility, stream/deadline contract tests |
| S19 | Part 4 (auth / ASVS map) | NIST AAL ladder, OAuth BCP attacks, ASVS 5 control map as gated in 4.2–4.10 |
| S20 | 3.0 + **8.1 toys** | SOLID/hexagonal; MapReduce/KV/Raft toys — sharded KV only if 8.1 omitted it |
| S21 | Part 8 (Donne Martin gated studios) | Six-step HLD/LLD dossiers already in Part 8; Part 12 only indexes residual primer problems |
| S22 | 9c.7 (+ 9c.0 atlas) | PMLE pipeline/monitor block; remainder is ML Test Score + silent-failure restore |
| S23 | 11b ORR | Control-plane P0–P10 + operational-readiness review |

All other stages (S0–S11, S14, S17 pointer, S18–S24, and any unconfirmed residual on skip-tested stages) are taught here in graph order. S15/S16 domain dumps and five-portfolio GenAI tracks are removed — **out of syllabus**. A readiness test may compress already mastered material but must not reorder a dependency.

**Block T skip-test (S0–S10 / S14).** If the matching **Block T** undergrad/grad gate is already confirmed, stamp the continuation stage and do **not** re-teach: S3↔**T.Alg**/`MATH-FUND`, S4↔**T.Disc**/`PROOF-DISCRETE`, S5/S7↔**T.LA**/`MATH-LA`, S6/S8↔**T.Algo**/`DS-ALGO`, S9↔**T.CalcOpt**/`MATH-CALC-NUM`, S10↔**T.ProbStat**/`PROB-STAT-INFO`, S14↔**T.CalcOpt**/**T.MLTheory**/T-OPT/T-CAUSAL depth. S0–S2 remain language/tool bases if Python/Go numerical base unconfirmed. Deep drill complements Block T — not a second unified dump and not Kaldi/CV/transformer.

### 12.0 Evidence hierarchy and research families

Use sources in this order: **(1)** current standards and official docs for behavioral contracts; **(2)** official university course pages for prerequisite order and assessment shape; **(3)** canonical textbooks and peer-reviewed papers for derivations; **(4)** maintained tool docs for APIs. A blog, vendor tutorial, or preserved note may illustrate a topic but **cannot** overrule a current standard or create a new stage. At teach time, follow only the source portions named by the active sub-topic and record version or access date on the artifact.

| Family | Anchors (pointer) | Imports into continuation |
|---|---|---|
| Python / numerical | Python tutorial; NumPy basics; pytest | Shape/dtype/strides; broadcast; copy vs view; tolerance tests |
| Go | Go docs/tour; memory model; diagnostics; security | Modules, generics, fuzz, concurrency visibility, vuln management |
| Discrete math / algorithms | MIT 6.042J; MIT 6.006 | Proof before structures; invariants; paradigms; unseen exams |
| Continuous math | MIT 18.01SC / 18.02SC / 18.06 | Limits→derivatives→integrals; systems/spaces/eigen/SVD |
| Probability / optimization | MIT 6.041SC; Stanford EE364A/B | RV→inference; convexity/duality/KKT before stochastic methods |
| Classical ML / RL / causality | Stanford CS229; scikit-learn guide; Sutton & Barto; Brady Neal CI | Supervised→unsupervised; bandits→MDP; estimand before DAG/IV — S11 skip-tests 9c zoo; S14 owns full opt/RL/causal |
| Production GenAI / RAG (not Part 12 dump) | **9c.5**; FAISS wiki; Sentence Transformers retrieve-rerank; Ragas; Huyen *AI Engineering* | Exact search→ANN; bi-encoder→rerank; component + e2e eval — five portfolios / from-scratch transformers **out of syllabus** |
| Speech / CV serving literacy (not Part 12) | **9c.6**; Vision/Speech product docs | Serving path + T-SIGNAL/T-CV slivers as used — DSP/Kaldi/OpenCV-as-course / full CV PhD **out of syllabus** |
| Databases | PostgreSQL docs; CMU 15-445/645 | SQL before internals; pages/indexes/MVCC/WAL/replica |
| APIs | RFC 9110; gRPC concepts; protobuf guide; Google AIPs | Safety/idempotency; streams/deadlines; field compatibility |
| Identity / appsec | OWASP ASVS 5; NIST 800-63B; OAuth BCP 240; Go security | AAL; PKCE/refresh rotation; fuzz and reachable-vuln checks |
| Distributed / SRE | MIT 6.5840; Google SRE book/workbook | MapReduce/KV/Raft/sharded-KV; SLI/SLO/error budgets |
| Production ML / GenAI risk | Rules of ML; PMLE guide; NIST AI 600-1; OWASP LLM Top 10 | Baseline-first; pipeline tests; Govern-Map-Measure-Manage |

### 12.0.1 Pace table (planning aid, not mastery)

Calendar time plans work; mastery gates do. Roughly 20–25 focused hours/week for a ~12-month intensive continuation, or 10–15 for a ~24-month sustainable path. Slow down when a prerequisite is shaky; accelerate only with unseen checks.

| Phase | Stages | Share of continuation core | Career evidence |
|---|---|---:|---|
| Foundations | S0–S4 | 15% | Repos, Python numerical basics, tested Go, proof/DS notes |
| Mathematical and algorithmic core | S5–S10 | 25% | Numerical kernels, Go DS packages, stats/experiment tools |
| Classical ML skip-test, DB, opt/RL/causal | S11–S14 | 25% | S11 → 9c zoo / M.ML only; SQL/engine labs; optimizer/RL/causal depth |
| GenAI pointer (no dump) | S17 | — | Pointer to **9c.5** only — no five-portfolio / Kaldi / from-scratch track |
| Services, security, architecture, prod ML | S18–S22 | 25% | Secure Go API, auth package, HLD/LLD dossier, prod-ML slice |
| Integrated capstone | S23 | 10% | Operable control plane + ORR (often skip-tested via 11b) |
| Optional archive | S24 | outside core | Only after S23 or a documented CORE dependency |
| *Removed from syllabus* | ~~S15–S16~~ | — | DSP/CV/NLP/ASR domain gates + transformer-from-scratch — **out of syllabus** |

Every **8–12 weeks** of continuation work, harden one existing artifact into portfolio evidence (problem, setup, derivation/architecture, tests, measurements, failure analysis, security, short demo). Portfolio hardening must not create a parallel course or bypass the graph.

### 12.0.2 Learner-ledger fields (continuation)

Compact stamp still applies (`part · sub-topic · ramp · unlocked · shaky · postponed · next`). For Part 12 stages also record:

| Field | Meaning |
|---|---|
| `stage` | Active S0–S24 id |
| `owner_node` | Canonical owner (see 12.Graph) |
| `sub_topic` | Exact heading / unit inside the stage |
| `ramp` | Current difficulty rung |
| `skip_test` | `pass` / `partial` / `n/a` with initial-track evidence pointer |
| `artifact` | Path or id of required gate artifact |
| `shaky` | Tools/ideas that failed unseen transfer |
| `postponed` | Challenges deferred with reason |
| `next_gate` | Concrete next unseen check |

No unit advances on reading or verbal confidence alone.

---

### 12.Graph — Knowledge-graph owner map

One owner per concept. Later appearances are recall, transfer, or integration — not a second full lesson. Edge literacy: `requires` (teach A first), `implements` (B is the coding lab for A), `strengthens` / `contrasts` / `revises` (brief recall after both unlocked).

| Node | Owns | Code owner | Primary stages | Key `requires` literacy |
|---|---|---|---|---|
| `BASE` | Hardware, files, shell, Git, HTTP/JSON vocabulary | Go shell/repo labs | S0 | — |
| `PY-CORE` | Python for numerical/ML work, NumPy, pytest | Python | S1 | `BASE` |
| `GO-CORE` | Go syntax, errors, tests, interfaces, concurrency, HTTP/gRPC | Go | S2, S6, S18 | `BASE` |
| `MATH-FUND` | Arithmetic, algebra, functions, coordinates, trig | Python | S1, S3, S5 | `PY-CORE` |
| `PROOF-DISCRETE` | Logic, sets, induction, counting, graphs, automata gate | Go CS labs; Python where feeding ML | S4 | `MATH-FUND` |
| `MATH-LA` | Vectors, matrices, eigen, SVD/PCA, spectral | Python | S5, S7 | `MATH-FUND` |
| `MATH-CALC-NUM` | Limits, gradients, ODE, finite differences, RK4 | Python | S9, S14 | `MATH-LA` |
| `PROB-STAT-INFO` | Probability, inference, bootstrap, information theory | Python | S10, S14 | `MATH-CALC-NUM` |
| `ML-CORE` | Classical ML, ranking, bandits, causal framing | Python first | S11 (skip-test → 9c/M.ML), S14 | `MATH-LA`, `PROB-STAT-INFO` |
| `DS-ALGO` | Arrays→graphs, DP, hard practice | Go | S4, S6, S8, S21 | `GO-CORE`, `PROOF-DISCRETE` |
| `DB-SQL` | Relational algebra, SQL, transactions | SQL + Go | S12 | `GO-CORE` |
| `DB-ENGINE` | Pages, indexes, MVCC, WAL, replica, PITR | Go + Postgres labs | S13 | `DB-SQL`, `DS-ALGO` |
| `API-SVC` | REST, gRPC, protobuf, schema evolution | Go | S18 | `GO-CORE`, `DB-SQL` |
| `SEC-AUTH` | Threat models, authn/z, sessions, OAuth/OIDC, secrets | Go | S19 | `API-SVC`, `DB-SQL` |
| `ARCH-HLD-LLD` | HLD/LLD, SOLID, DDD, patterns, ADRs | Go | S20 | `API-SVC`, `SEC-AUTH`, `DB-ENGINE` |
| `DIST-OPS` | Caches, queues, consistency, SLOs, rollout | Go | S20, S22 | `ARCH-HLD-LLD`, `SEC-AUTH` |
| `ML-SYS-MLOPS` | Pipelines, registry, serving, drift, PMLE, case studies | Hybrid | S22 | `ML-CORE`, `API-SVC`, `DIST-OPS` (GenAI/RAG production literacy from **9c.5**, not a Part 12 GenAI node) |
| `SDP-OOD` | System-design and OOD practice bank | Go | S21 | `ARCH-HLD-LLD`, `DS-ALGO`, `SEC-AUTH`, `DIST-OPS` |
| `NASIKO-CAPSTONE` | P0–P10 control plane → **11b** | Go | S23 | `SDP-OOD`, `ML-SYS-MLOPS`, `SEC-AUTH`, `DB-ENGINE`, `DIST-OPS` |
| `TOOLS` | Docker/K8s/Terraform/vector DBs/OTEL/MLflow… | Tool labs at first use | first real use | never a sightseeing module |
| `ARCHIVE` | Game/medical/mechanical/deep pure math/extra NT | None unless pulled | S24 | CORE dependency only |

**Structural ownership rule.** New material about Python/Go mechanics → S1 or S2/S6; proof/math/probability/optimization → S3–S10 or S14; classical ML → S11 skip-test to **9c zoo / M.ML** only (no re-teach dump); SQL/engine → S12–S13; prompting/RAG/agents production → **9c.5** (S17 is a pointer only); API behavior → S18; identity/appsec → S19; architecture/distributed → S20; open design problems → S21; MLOps/governance → S22; integrated product → S23. Pure DSP/image/NLP/speech domain gates and neural/transformer-from-scratch are **out of syllabus** (not S15/S16). Legal traversal: `S0 → … → S14 → S17(pointer) → S18 → … → S23`, with S24 closed by default.

---

### 12.S0–S4 Foundations

#### 12.S0 Zero setup — `BASE`

**Theory.** Bits/bytes; CPU–memory–storage; files vs directories; absolute/relative paths; process vs program; environment variables; ports; DNS/HTTP/JSON vocabulary; shell composition, exit status, standard streams; Git working tree/index/commit/remote; reproducible repository layout.

**Implementation.** Trace one command from shell parse to process exit and one HTTP request from name lookup to response. Repo layout with a first test loop.

| | |
|---|---|
| **Prerequisites** | None (entry) |
| **Artifacts** | Setup runbook that works from a clean directory; recovery notes |
| **Gate** | Recover deliberately broken path, env, Git branch, and local HTTP call |
| **Research anchors** | Go install/env docs; shell/`git` official manuals |

#### 12.S1 Python numerical base — `PY-CORE`, `MATH-FUND`

**Order.** Literals and numeric representation → names/mutability → conditions/loops → functions and contracts → strings/lists/tuples/dicts/sets → modules and venvs → exceptions and file/JSON I/O → pytest → NumPy `ndarray`.

**Array discipline.** Before execution, predict `shape`, `ndim`, `size`, `dtype`, strides/axis meaning, indexing result, broadcasting result, and copy/view aliasing. Cover dtype overflow, floating-point representation error, tolerance assertions, seeded generators, vectorization, and elementwise vs matrix multiplication.

**Skip-test note.** Numerical-stability *policy* and floating-point contracts already gated in **M.NS** — recall, do not re-derive the whole stability chapter.

| | |
|---|---|
| **Prerequisites** | S0 |
| **Artifacts** | Tested numerical utility package (loop form ≡ vectorized form) |
| **Gate** | Agreement on normal, empty, boundary, aliasing, and non-finite inputs |
| **Research anchors** | Python tutorial; NumPy fundamentals; pytest |

#### 12.S2 Go programming base — `GO-CORE`

**Order.** Module/package/function → scalar types and conversions → control flow → arrays/slices/maps → strings/bytes/runes → structs and zero values → errors and wrapping → table tests → format, vet, benchmarks.

**Discipline.** Trace slice length/capacity/backing arrays and map missing-value behavior; reject unchecked errors and accidental Unicode byte assumptions. Integer wrap vs Python bigint remains an **M.NS** contrast, not a second numerics course.

| | |
|---|---|
| **Prerequisites** | S0 |
| **Artifacts** | One small command + one package |
| **Gate** | Table tests, edge cases, `go vet`, formatting, and a benchmark *explanation* |
| **Research anchors** | Tour of Go; Effective Go (supplementary); Go diagnostics |

#### 12.S3 Algebra and functions — `MATH-FUND`, `PY-CORE`
**Block T skip-test:** if **T.Alg** undergrad gate confirmed → stamp; else deep drill (`MATH-FUND`).

**Order.** Fractions, ratios, units, estimation → equations, inequalities, absolute value → exponents/logs → polynomials, sequences → relations and functions. Represent each function as rule, table, graph, mapping, and code; distinguish domain, codomain, range, inverse, and composition. Top rung combines algebraic structure with a prior numerical representation — not blind substitution.

| | |
|---|---|
| **Prerequisites** | S1 |
| **Artifacts** | Piecewise expression evaluator; inverse/composition counterexample set |
| **Gate** | Fresh parameterized problems; false-inverse counterexamples |
| **Research anchors** | Continuous-math family entry via algebra texts; MIT 18.01SC readiness |

#### 12.S4 Proof, discrete math, and basic DS — `PROOF-DISCRETE`, `DS-ALGO`, `GO-CORE`
**Block T skip-test:** if **T.Disc** (+ **T.Algo** as needed) gate confirmed → stamp; else deep drill.

**Order.** Propositions/quantifiers → direct, contrapositive, contradiction, counterexample → sets/functions/relations → induction and invariants → counting and pigeonhole → recurrences → graphs and state machines → arrays/stacks/queues/maps in Go. Every implementation states its representation invariant and proves preservation by each operation.

| | |
|---|---|
| **Prerequisites** | S2, S3 |
| **Artifacts** | Short proof portfolio + tested Go structures |
| **Gate** | Unseen problem that **chooses** the technique or structure (not told) |
| **Research anchors** | MIT 6.042J; Book of Proof–class logic/sets coverage |

---

### 12.S5–S10 Mathematical and algorithmic core

#### 12.S5 Geometry, coordinates, and vectors — `MATH-FUND`, `MATH-LA`
**Block T skip-test:** if **T.LA** undergrad vectors gate confirmed → stamp residual only; else deep drill.

Build Euclidean geometry and trigonometry into coordinates, affine combinations, norms, distance metrics, dot product, angles, projections, lines/planes, and transformations. Compare Euclidean, Manhattan, and cosine under scaling and translation.

| | |
|---|---|
| **Prerequisites** | S3 |
| **Artifacts** | NumPy-free vector/matrix kernels, then NumPy comparison |
| **Gate** | Geometric invariants + degenerate cases |
| **Research anchors** | MIT 18.06 entry; applied LA texts |

#### 12.S6 Go types and core data structures — `GO-CORE`, `DS-ALGO`
**Block T skip-test:** if **T.Algo** undergrad + Go G modules confirmed → stamp; else deep drill.

**Order.** Pointers and ownership-by-convention → structs/method sets → interfaces and composition → generics and constraints → linked structures → BST/balanced-tree concepts → heap/priority queue → union-find → hash table. Include allocation/escape intuition, nil-interface traps, comparable constraints, amortized growth, and mutation under aliasing.

| | |
|---|---|
| **Prerequisites** | S2, S4 |
| **Artifacts** | Reusable Go packages with property tests and fuzz seeds |
| **Gate** | Complexity arguments + benchmarks that explain crossover points |
| **Research anchors** | Go docs (interfaces/generics); CLRS/Sedgewick for structure contracts |

#### 12.S7 Linear algebra and spectral methods — `MATH-LA`
**Block T skip-test:** if **T.LA** grad-as-needed (SVD/PCA residual) confirmed → stamp; else deep drill.

**Order.** Linear systems and elimination → span/independence/basis/dimension → four fundamental subspaces → linear maps → orthogonality/projection/least squares → determinants as structure (not a solver) → eigenvalues/eigenvectors/diagonalization → symmetric and SPD matrices → SVD/pseudoinverse/condition → PCA and low-rank approximation. **Predict** rank, nullity, shape, and stability before computing.

| | |
|---|---|
| **Prerequisites** | S5 |
| **Artifacts** | GE, QR/Gram-Schmidt, power iteration, PCA with residual checks |
| **Gate** | Residuals, orthogonality, reconstruction error, adversarial ill-conditioning |
| **Research anchors** | MIT 18.06; Strang ILA; Axler (rigor track) |

#### 12.S8 Sorting, graphs, and complexity — `DS-ALGO`, `PROOF-DISCRETE`
**Block T skip-test:** if **T.Algo** undergrad/grad complexity gate confirmed → stamp; else deep drill.

**Order.** Asymptotic models and lower-bound intuition → loop/recurrence analysis → binary-search invariant → elementary and divide-and-conquer sorting → heaps and selection → hashing/amortization → BFS/DFS/topo/SCC → shortest paths → MST/greedy exchange → DP → max-flow entry. Derive state, invariant, recurrence, or exchange argument **before** code.

| | |
|---|---|
| **Prerequisites** | S4, S6 |
| **Artifacts** | Go algorithm package with differential/property tests |
| **Gate** | Mixed unseen problem whose constraints force the paradigm |
| **Research anchors** | MIT 6.006; CLRS paradigm chapters |

#### 12.S9 Calculus and numerical methods — `MATH-CALC-NUM`
**Block T skip-test:** if **T.CalcOpt** undergrad/grad gate confirmed → stamp; **M.NS** still owns FP policy.

**Order.** Limits/continuity → derivative as local linearization → product/chain/implicit → optimization and curve behavior → definite integral and FTC → integration methods → sequences/series → partial/directional derivatives → gradient/Jacobian/Hessian → multiple-integral/vector-calculus intuition → ODE models → floating-point error, conditioning, stability → roots/interpolation/quadrature → Euler/RK4 and finite differences.

**Policy recall.** Floating-point **policy** remains **M.NS** — this stage owns analytic vs numerical agreement within a *justified* bound.

| | |
|---|---|
| **Prerequisites** | S7 |
| **Artifacts** | Gradient checker; numerical integrator; RK4 toy with step-size failure notes |
| **Gate** | Analytic vs finite-difference gradients within justified ulp/rel bound; stability explanation |
| **Research anchors** | MIT 18.01SC / 18.02SC; numerical-methods chapter maps |

#### 12.S10 Probability, statistics, and information — `PROB-STAT-INFO`
**Block T skip-test:** if **T.ProbStat** undergrad/grad gate confirmed → stamp; do **not** re-derive **M.ML** IPS here.

**Order.** Sample spaces/counting/conditioning/Bayes → discrete and continuous RVs → joint/marginal/conditional → expectation/variance/covariance → transformations → concentration and LLN/CLT → Markov-chain entry → sampling and estimands → likelihood/MLE/MAP/sufficiency → CIs and tests → bootstrap/permutation → regression diagnostics → Bayesian updating → entropy/CE/KL/mutual information → experiment design and sequential caveats.

| | |
|---|---|
| **Prerequisites** | S9 |
| **Artifacts** | Samplers; MLE; bootstrap CI; A/B analyzer; log-loss/perplexity tools |
| **Gate** | Simulation verifies a derivation (does not replace it); power, uncertainty, multiple-comparison, practical-significance checks |
| **Research anchors** | MIT 6.041SC; Wasserman/Casella–Berger class coverage; Cover/Thomas for info theory |

---

### 12.S11–S14 ML, databases, optimization, RL, causality

#### 12.S11 Classical ML — skip-test only — `ML-CORE`

**Skip-test → 9c classical zoo / M.ML only.** If the end-of-**9c** classical zoo + **M.ML** (logistic/linear GD, metrics, IPS as gated) confirmed, stamp **12.S11** complete and move on. **Do not** re-teach the classical-ML dump here.

If the skip-test fails, return to **9c zoo / M.ML** (and **9c.0** gaps) — those remain the owners. Part 12 does not host a second from-scratch classical-ML course, nor Kaldi / DSP / transformer-from-scratch content.

| | |
|---|---|
| **Prerequisites** | S7, S10 literacy as needed for S14; classical content owned by **9c** / **M.ML** |
| **Artifacts** | Ledger stamp pointing at 9c zoo + M.ML evidence (no new Part 12 dump) |
| **Gate** | Skip-test pass, or remediation completed at **9c** / **M.ML** owners |
| **Research anchors** | End of **9c** classical zoo; **M.ML**; Stanford CS229 / scikit-learn only via those owners |

#### 12.S12 SQL and relational correctness — `DB-SQL`, `GO-CORE`

**Skip-test.** If Part 2 confirmed FDs/joins/transactions/pagination/client hygiene, stamp and skip full re-teach.

**Else order.** Relations/keys/FDs/normalization → relational algebra → DDL/types/constraints → SELECT semantics and NULL/3VL → joins including semi/anti/outer → aggregation → subqueries/CTEs/recursion → windows → transactions/isolation → pagination and application access. Predict multiplicity and NULL behavior before execution.

| | |
|---|---|
| **Prerequisites** | S2 (and S4 literacy) |
| **Artifacts** | SQL edge-case transcript; parameterized Go `database/sql` client |
| **Gate** | Context cancellation, transactions, pool limits, migration rollback, property-based relational checks |
| **Research anchors** | PostgreSQL SQL docs; CMU 15-445 SQL-before-internals |

#### 12.S13 PostgreSQL internals — `DB-ENGINE`, `DS-ALGO`

**Skip-test.** If DB-1–10 (or Part 2 engine literacy equivalent) confirmed, stamp; retain only residual `EXPLAIN` drills if needed.

**Else order.** Storage media and row/column/log-structured layouts → pages/tuples/TOAST/catalogs → buffer manager → hash/B-Tree/GIN/GiST/BRIN/vector indexes → iterators, sort/aggregate, join algorithms → statistics/cardinality/cost plans → MVCC snapshots/isolation/locks/deadlocks/vacuum → WAL/checkpoints/recovery → replication/PITR → parallel/distributed trade-offs.

| | |
|---|---|
| **Prerequisites** | S12, S8 |
| **Artifacts** | Slotted-page, B-Tree, iterator, MVCC/WAL toys; predicted `EXPLAIN (ANALYZE, BUFFERS)` |
| **Gate** | Crash/recovery evidence + plan predictions that match measured plans |
| **Research anchors** | PostgreSQL internals docs; CMU 15-445/645 |

#### 12.S14 Optimization, RL, and causality — `MATH-CALC-NUM`, `PROB-STAT-INFO`, `ML-CORE`
**Block T skip-test:** if **T.CalcOpt** / **T.MLTheory** / opened T-OPT/T-CAUSAL grad gates confirmed → stamp residual only; no Kaldi/CV/transformer dump.

**Optimization.** Geometry/convexity → first/second-order methods → SGD/momentum/adaptive → constraints/Lagrangian/KKT/duality → proximal and coordinate methods → LP/assignment → robust/stochastic formulations → non-convex diagnostics.

**RL.** Exploration and multi-armed bandits → MDP/Bellman → DP → Monte Carlo → TD/Q-learning → function approximation/policy gradients only after tabular checks.

**Causal.** Question/estimand/intervention → potential outcomes → DAGs/SCMs → randomization → backdoor/frontdoor and identification → estimation/heterogeneous effects → overlap and sensitivity → IV, DiD, RDD, synthetic control.

*(M.CAUSAL lite and 9c observational caveats are recall inputs — this stage owns full identification and assumption-violation experiments.)*

| | |
|---|---|
| **Prerequisites** | S9, S10, S11 |
| **Artifacts** | Optimizers; assignment solver; bandit/MDP simulator; causal estimators |
| **Gate** | Distinguish prediction vs intervention vs counterfactual; assumption-violation experiments |
| **Research anchors** | Stanford EE364; Sutton & Barto; Brady Neal CI course |

---

### 12.S17 GenAI / RAG — pointer only

GenAI/RAG **production** slice lives in **9c.5** (GCP RAG, PEFT/LoRA as adapters, eval, agents handoff to 11b P5/P9). Optional PEFT/eval depth only if already in **9c.5** — do **not** re-add S15/S16 domain dumps here.

**Out of syllabus (not Part 12 content):** five-portfolio GenAI track; Kaldi / DSP / OpenFst ASR course; full CV PhD / OpenCV-as-semester; transformer-from-scratch / attention-derive semester. Production speech/CV **serving** stays **9c.6** literacy only.

| | |
|---|---|
| **Action** | Stamp via **9c.5** (+ **9c.6** serving literacy if relevant); no Part 12 GenAI portfolio gate |
| **Research anchors** | **9c.5**; Huyen *AI Engineering*; FAISS/SBERT/Ragas as used in 9c.5 — not a second GenAI course |

---

### 12.S18–S22 Services and operations

#### 12.S18 APIs and service contracts — `API-SVC`, `GO-CORE`, `TOOLS`

**Skip-test.** If 3.2 confirmed, stamp; keep only residual compatibility drills if needed.

**Else.** RFC 9110 resources, representations, origins, methods, status codes, content negotiation, caching, validators, conditional requests. Derive safe/idempotent/retry behavior; test lost updates with `ETag`/`If-Match`, overload with `Retry-After`, and malformed framing at the server boundary. Then resource-oriented REST; protobuf field presence/numbers/unknown fields/reservations; compatibility matrices; gRPC unary/server/client/bidi streams with deadlines, cancellation, metadata, status, backpressure.

| | |
|---|---|
| **Artifacts** | Go REST + gRPC services |
| **Gate** | Old-client/new-server **and** new-client/old-server contract tests |
| **Research anchors** | RFC 9110; gRPC core concepts; protobuf guide; Google AIPs |

#### 12.S19 Go authentication, security, and middleware — `SEC-AUTH`

**Skip-test.** If Part 4 / 4.2–4.10 confirmed, stamp.

**Else deepen.** NIST SP 800-63B distinctions among passwords, authenticators, sessions, and access tokens; AAL1/AAL2/AAL3; phishing/replay resistance; authenticator intent/binding/recovery/invalidation; syncable passkey trade-offs. OAuth BCP attacks: redirect mismatch, code/access-token injection, mix-up, referer/history leakage, PKCE downgrade, counterfeit resource server, refresh replay, open redirect, unsafe 307, untrusted proxy headers. Map controls to versioned ASVS 5 requirements.

| | |
|---|---|
| **Artifacts** | From-scratch Go security package (protocol/middleware/policy — **not** homemade crypto); hardened local service |
| **Gate** | Positive/negative/fuzz/race/resource-exhaustion/rotation/revocation/recovery tests |
| **Research anchors** | OWASP ASVS 5; NIST 800-63B; OAuth BCP 240; Go security guidance |

#### 12.S20 HLD, LLD, SOLID, patterns, distributed systems — `ARCH-HLD-LLD`, `DIST-OPS`

**Skip-test.** SOLID/hexagonal if 3.0 confirmed. MapReduce/KV/Raft if **8.1 toys** confirmed. Sharded KV only if 8.1 did not cover it — do not rebuild Raft in Part 12 when 8.1 already owns it.

**Else order.** Quality attributes and measurable SLOs → boundaries/data ownership → LLD contracts, cohesion/coupling → SOLID in idiomatic Go → clean architecture and DDD → modular monolith → sync/async → retries/timeouts/idempotency/backpressure → cache and queue semantics → replication/partition/consistency → leader election/consensus → transactions/outbox/saga → observability/operations → microservice split only when justified.

Teach SOLID as five **testable** heuristics (SRP = one coherent reason to change; OCP via composition; LSP preserves behavioral contracts including errors/side effects/concurrency; ISP = small consumer-owned interfaces; DIP = policy depends on abstractions). Patterns answer named forces and include rejection criteria.

| | |
|---|---|
| **Artifacts** | Refactored Go service with before/after dependency evidence; ADRs; sequence/state diagrams |
| **Gate** | Substitutability and boundary isolation tests; failure injection; SLO/error budget; overload/cascade analysis; recovery evidence |
| **Research anchors** | MIT 6.5840 progression; Google SRE book/workbook |

#### 12.S21 System-design and OOD practice bank — `SDP-OOD`

**Skip-test to Part 8.** Part 8 already owns Donne Martin gated studios and the six-step protocol (NFRs, capacity, Mermaid HLD, LLD, failures, hardening). **Do not re-teach Part 8 studios.** Part 12.S21 only indexes residual problems and enforces coverage breadth.

**Method (recall).** For each unlocked residual problem: clarify functional/quality/security requirements → estimate load/storage/bandwidth → define API/data/consistency → draw HLD → deep-dive one bottleneck → enumerate failures/abuse/privacy → define observability/rollout/recovery → implement a thin Go slice. Cover at least one read-heavy, write-heavy, realtime, batch, multi-tenant, globally distributed, ML-backed, and adversarial system. Revisit one prior design at **10×** scale or changed consistency/privacy.

**Primer topic checklist (index).** Performance vs scalability; latency vs throughput; availability vs consistency; consistency/availability patterns; DNS; CDN; load balancing; reverse proxies; application layer and microservices; database design and scaling; NoSQL; caches; asynchronism; communication; security; powers of two and latency numbers — teach at Part 8 owners first; use here only as coverage audit.

**Official SDP set (index).** Pastebin/Bitly; Twitter timeline/search; web crawler; Mint.com; social-network data structures; search-engine KV store; Amazon sales ranking; scale to millions on AWS.

**Official OOD set (index).** Hash map; LRU cache; call center; deck of cards; parking lot; chat server; circular array.

**Additional primer questions (residual index — pick gaps after Part 8).** File sync; search engine; scalable crawler; collaborative docs; Redis-like store; Memcached-like cache; recommendations; TinyURL/Bitly; chat; picture sharing; feed/timeline/graph search; CDN; trending topics; Snowflake ID; top-k in a window; multi-datacenter serving; multiplayer card game; garbage collector; API rate limiter; stock exchange.

**Pattern forces (recall, not a second pattern course).** Repository, unit of work, adapter, strategy, factory, builder, middleware/decorator, chain of responsibility, observer/pub-sub, mediator, command, state, outbox, saga, CQRS/read model, idempotent consumer, circuit breaker, bulkhead, retry with jitter, strangler fig — each with rejection criteria.

| | |
|---|---|
| **Prerequisites** | S20 (or Part 8 + 3.0 skip-test) |
| **Gate** | Residual dossiers with threat model + Go slice; breadth coverage checklist checked |
| **Research anchors** | system-design-primer topic map; Part 8 studios as owner |

#### 12.S22 Production ML systems and MLOps — `ML-SYS-MLOPS`

**Skip-test.** If 9c.7 PMLE pipeline/monitor block confirmed, stamp the bulk; remainder is ML Test Score drill plus silent-failure restore of prior model/data/config.

**Case-study bank — do not duplicate.** Production rotations live in **Appendix M** (complete catalog) and the concept atlas at **9c.0**. Part 12 points; it does not paste the 309 studies. Cluster reminder for rotations: ranking/search/recs/ads; forecasting/ETA/pricing; fraud/risk/spam; LLM/NLP/assistants; CV/audio/documents; feature platforms/MLOps; graph ML/entity resolution; bandits/RL; causal/experimentation — each rotation needs the artifact type already named in 9c.0 / Appendix M headers.

**Else full order.** Decide whether ML is warranted → metric and non-ML baseline → data/label/feature contracts and ownership → reproducible experiment → pipeline components and lineage → registry/promotion → batch/online/stream serving → training-serving parity → automated data/model/infrastructure tests → shadow/canary/A-B → freshness, skew, drift, quality, resource monitoring → retraining policy → rollback/incident/governance/decommission. Code, data, and model are independently versioned change axes. For GenAI add corpus/prompt/model/tool versions, judge calibration, token/spend budgets, safety regressions.

| | |
|---|---|
| **Artifacts** | Versioned Python model/data/eval + secure Go feature facade / evaluator CLI; parity fixture; shadow/canary report; drift/freshness alerts |
| **Gate** | PMLE-style design/build/operationalize/govern defense; ML Test Score; silent-failure restore drill |
| **Research anchors** | Rules of ML; PMLE exam guide; NIST AI 600-1; Appendix M + 9c.0 |

---

### 12.S23 Control plane — `NASIKO-CAPSTONE` → 11b

**Skip-test.** If 11b ORR passed, stamp Part 12.S23 complete. Capstone phases do not introduce surprise database, security, GenAI, or distributed-systems subcourses — they consume already mastered owner-stage contracts at boundaries.

**Else finish P0–P10 and ORR here.**

| Phase | Output |
|---|---|
| P0 Foundations | Go monorepo, dev loop, tooling |
| P1 Core platform skeleton | Shared config, secret-safe logs/traces, hardened servers/clients, ordered middleware |
| P2 Data stores and contracts | Stores, tenant constraints, migrations, transactions, backup invariants |
| P3 Backend API and identity | Handlers/services/repos; password/OIDC; opaque sessions; granular authz; CSRF/CORS; idempotency |
| P4 Registry and gateway | Discovery, routes/plugins, workload identity, scoped credentials, health/stale cleanup |
| P5 Router | Python embeddings behind typed contract; shortlist/rerank; structured pick; tenant/data boundaries |
| P6 Chat history | Authenticated ingest; object/tenant/field authz; append-only audit; retention/deletion |
| P7 Orchestrator and worker | Streams; short-lived workload identity; provenance; deploy/rollback; idempotent consumers |
| P8 CLI | Operator workflows; device/browser login; least-privilege commands; no credential leakage |
| P9 Sample agents | Authenticated A2A; AgentCard validation; per-tool policy; replay control; streaming limits |
| P10 Production hardening | SLOs, dashboards, alert drills, load/abuse/fuzz/race, scans, rotation, model rollback, backup/restore, incident recovery, security review, **ORR** |

**ORR must show (not claim):** updated data-flow and trust-boundary maps; abuse-case and residual-risk registers; identity propagation without network-location trust; deny-by-default function/object/field/tenant/tool authz with regression tests; password/session/OIDC/JWT behavior inherited from `SEC-AUTH`; bounded inputs and artifact provenance; `go test` + fuzz + race + load/abuse evidence; alerts with owned runbooks; rehearsed credential/key rotation, malicious-agent containment, backup restore, rollback, and post-incident review.

---

### 12.S24 Optional archive / deferral — `ARCHIVE` (Tier 2)

Closed by default. Open **one** specialization only after S23 (or when a documented CORE dependency requires a slice). Entry order: prerequisite gap analysis → bounded question → authoritative syllabus/text → small theory-and-implementation slice → transfer artifact. Archive breadth is **never** counted as incomplete core work.

| Deferred family | When a slice may open | Entry path |
|---|---|---|
| Game engines / rendering | CORE needs geometry/GPU pipeline | Geometry/LA → GPU pipeline; not a game-engine semester |
| Medical / clinical inventories | Supervised domain need | Biology/statistics/ethics + domain supervision |
| Mechanical / fluid / aerospace | Numerics/PDE need | Calculus/ODE/PDE/numerics |
| Deep pure math (analysis, algebra, topology, measure, DG, logic, pure combinatorics beyond CORE) | Proof-track dependency | Proof and analysis gate first |
| Extra number theory | Beyond GCD/modular/CRT/hashing/crypto-practice | Keep GCD/modular/CRT in CORE; deep NT stays archive |
| Commercial arithmetic encyclopedias | Finance/payment examples only | Examples attach to payments owners; encyclopedia stays archive |
| Unrelated web stacks (e.g. React/TS sightseeing) | Explicit UI track opened | Otherwise archive |
| Theory of computation / architecture / OS / networks / compilers beyond systems gates | Slice already required by a CORE node | Otherwise archive; pure DSP/ASR/Kaldi stays out of syllabus |

---

### 12.Assessment — Mastery, assessment, and portfolio standard

#### Universal stage gate

A continuation stage is complete only when the learner can:

1. Explain the concept in plain language, use the right notation or system vocabulary, and reconstruct the central idea without notes.
2. Pass unseen basic and routine checks, a mixed transfer using earlier unlocked tools, and the domain-appropriate top rung.
3. Implement the core primitive in the owner language, where implementable, without a library that hides the learning objective.
4. Verify the result and explain complexity, numerical stability, uncertainty, security properties, failure behavior, or production trade-offs as appropriate.
5. Diagnose a deliberately broken or misleading case and state when the idea fails or a simpler alternative is better.
6. Produce the stage’s required artifact and defend one consequential design choice, one rejected alternative, and one residual risk.

**Minimum pass.** Every prerequisite-critical criterion passes; at least ~80% on the remaining rubric; any failed unseen transfer is repaired and retested with a **different** problem. Speed is recorded only after correctness and explanation are stable. Skip-tests from F–11b count as stage completion when the named artifacts are on the ledger.

#### Domain evidence matrix

| Domain | Unseen assessment | Implementation evidence | Required analysis |
|---|---|---|---|
| Mathematics and probability | Basic, routine, mixed, readiness-matched hard problems | Python/NumPy experiment when meaningful | Derivation/proof idea, assumptions, counterexample, numerical error |
| Classical ML / production ML (9c owners) | New dataset slice; metric prediction; ablation or error diagnosis — via **9c** / **M.ML** / **S14** as applicable | Python scratch at **M.ML** / 9c zoo; library comparison | Baseline, leakage, uncertainty, metric choice, failure slices — not DSP/Kaldi/from-scratch-transformer |
| Go and DS/algo | New constraints, trace, edge cases, hard platform problem | Idiomatic Go package and tests | Invariant, correctness, time/space, benchmark where relevant |
| Database and distributed systems | Query/transaction/failure scenario | Go or SQL engine/component lab | Plan or state trace, consistency, recovery, ops trade-off |
| Security and middleware | Threat or abuse case not in the worked example | Go control + positive/negative/fuzz/race/resource tests | Security invariant, attacker model, residual risk, production boundary |
| HLD/LLD and production ML | Changed scale, SLO, failure, privacy, or tenancy | Go service slice consuming Python ML artifacts where applicable | Capacity, trust boundaries, alternatives, observability, rollback, incident response |

#### Cadence

- **Every session:** short retrieval of prior unlocked ideas + one immediate unseen check.
- **Every module:** cumulative mixed transfer, implementation or proof artifact, failure diagnosis, learner explanation.
- **Every stage:** timed and untimed checks, artifact review against the domain rubric, fresh transfer after feedback.
- **Every 4–6 weeks:** interleaved review from the learner ledger; weak prerequisites return to the graph before new dependent content.
- **Every 8–12 weeks of continuation:** portfolio hardening + concise oral/design defense. Do not add unrelated topics merely to enlarge a project.
- **Before S19, S22, and S23:** cumulative gates for Go concurrency/testing, APIs/databases, and security respectively. The capstone is not where missing foundations are first taught.

#### Portfolio evidence (continuation)

Maintain a small set of deep artifacts rather than many tutorial clones. Each published artifact: precise problem and scope; prerequisite map; reproducible environment; derivation or architecture; owner-language implementation; tests; measured results; failure analysis; security/privacy considerations; operational instructions where relevant; short demonstration. Preserve commit history that shows hypothesis → failure → repair → verification. Remove real credentials and personal/proprietary data.

**By S23** (including skip-tested initial-track evidence), the portfolio should include at least: one mathematics/numerical notebook or report; one Go DS/algo package; one statistics/ML experiment with leakage-safe evaluation (via **9c** / **M.ML**); one database/storage lab; one secure Go service with auth/middleware evidence; one HLD/LLD dossier; one production-ML boundary joining Python and Go (**9c.5** RAG slice and/or **9c.7** MLOps as applicable); and the integrated capstone with ORR. No Kaldi / OpenCV-as-course / from-scratch-transformer portfolio requirement.

**Part 12 complete when** S0–S23 gates pass (skip-tests count). S24 is outside core completion.

---

### 12.Ref — Continuation atlas (index, not dumps)

Pointers for Part 12 beyond the initial-course Appendices B / C / I / T. **Do not** paste textbook deconstruction corpora or Section-18-style source dumps here. Follow the evidence hierarchy in 12.0; open the named chapter or tool page only for the active sub-topic.

#### Bibliography / course pointers by owner stage

| Stage cluster | Prefer | Role |
|---|---|---|
| S0–S2 | Official Python, NumPy, pytest, Go tour/docs | Language and tooling contracts |
| S3–S4 | Hammack *Book of Proof*; MIT 6.042J | Proof and discrete foundations |
| S5, S7 | Strang *Introduction to Linear Algebra*; Axler *Linear Algebra Done Right* (rigor track); MIT 18.06 | Computational vs rigorous LA |
| S6, S8 | CLRS; Sedgewick; MIT 6.006 | Algorithms and DS packages |
| S9 | MIT 18.01SC / 18.02SC; a standard numerical-methods text | Calculus + numerics |
| S10 | MIT 6.041SC; Wasserman *All of Statistics*; Cover & Thomas | Probability, inference, information |
| S11 | End of **9c** classical zoo; **M.ML** | Skip-test only — no Part 12 classical dump |
| S12–S13 | PostgreSQL official docs; CMU 15-445/645 | SQL then engine |
| S14 | Stanford EE364; Sutton & Barto; Brady Neal CI | Optimization, RL, causality |
| S17 | **9c.5** (+ Huyen; FAISS/SBERT/Ragas as used there) | Pointer only — production GenAI/RAG; no five-portfolio track |
| *Removed* | ~~S15 / S16~~ (MIT 6.003; Szeliski; CS224S; Dive into DL; Kaldi/OpenFst) | **Out of syllabus** — retarget production speech/CV to **9c.6**; DL-from-scratch external |
| S18 | RFC 9110; gRPC; protobuf; Google AIPs | Service contracts |
| S19 | OWASP ASVS 5; NIST 800-63B; OAuth BCP 240; Go security | Auth and middleware |
| S20–S21 | MIT 6.5840; Google SRE; system-design-primer (via Part 8) | Architecture + practice bank |
| S22 | Rules of ML; PMLE guide; **Appendix M** + **9c.0** | Production ML rotations |
| S23 | 11b ORR checklist; P0–P10 phase map above | Capstone integration |
| S24 | Authoritative domain syllabus only when CORE pulls a slice | Archive entry |

#### Tool atlas (first real use only)

| Tool family | Typical first stage | Rule |
|---|---|---|
| pytest / NumPy / notebook or script runner | S1 | After mental model of the primitive |
| `go test` / vet / bench / fuzz | S2, S6 | Always with explanation, not vanity timings |
| PostgreSQL / `EXPLAIN` | S12–S13 | SQL semantics before internals |
| Vector DB / ANN library | **9c.5** (first real use) | After exact-search baseline in the RAG slice — not a Part 12 DL course |
| *Removed tools* | ~~OpenCV / Kaldi / OpenFst / PyTorch-as-DL-course~~ | **Out of syllabus** as Part 12 domain-gate tools; Vision/Speech serving stays **9c.6** product literacy |
| Docker / Compose / K8s / Terraform / OTEL | S18–S22 / S23 | At the consuming service boundary |
| MLflow / wandb / Evidently / feature store | S22 | After lineage and metric contracts |

#### Practice-bank cross-links

| Bank | Owner in this curriculum | Part 12 use |
|---|---|---|
| Donne Martin gated studios | Part 8 | Skip-test; S21 residual index only |
| Production ML case studies (309) | Appendix M + 9c.0 | Pointer from S22 — never duplicate |
| GenAI / RAG production | **9c.5** | S17 is pointer only — no five-portfolio Part 12 bank |
| Capstone P0–P10 / ORR | 11b / 12.S23 | Skip-test or finish here |

---

## How we run it

1. This curriculum is the syllabus of record. Pedagogy is the teaching law; the Parts are the content.
2. Teaching starts at **F** then **0.1 Billing** when you say start. **Part 12 opens only after 11b** (or skip-test). During F–11b, extra theory is a **prereq ref** to 12.Sx, not a full stage. The initial track may close for PCA/PMLE without opening Part 12.
3. **One `###` sub-topic at a time**, full difficulty ramp. Unseen check. Ledger stamp (including continuation fields in 12.0.2). Python then Go per language ownership.
4. Northstar then 11b in the learner workspace; Part 12 artifacts are separate packages/systems as gated.
5. Preferred: overwrite a live learner ledger. Compact stamp: `part · sub-topic · ramp · unlocked · shaky · postponed · next`.
6. Every 8–12 weeks of continuation work: portfolio hardening (12.Assessment). S23 ORR is required unless 11b already passed it.

No teaching content is delivered until you say start.

## Appendix M — ML system-design case studies (complete catalog)

Source: [Engineer1999/A-Curated-List-of-ML-System-Design-Case-Studies](https://github.com/Engineer1999/A-Curated-List-of-ML-System-Design-Case-Studies) (309 studies, 84 companies). Teach **Part 9c** families; this appendix is the full index. One-liners are `Company — description (year)`. Concept decomposition and MISSING math/CS/theory/industry prerequisites live in **9c.0** — do **not** treat this appendix as a second course.

**Family → Part 9c teaching map** (teach at the owner; this appendix stays the 309 one-liner index — do **not** paste article text into lessons; gaps → **9c.0**):

| Appendix M heading | Teach under | Notes |
|---|---|---|
| Recommend / personalize / feed | **9c.2** (+ **9c.0** gaps) | Northstar ranker; Netflix / Instacart-class packs; IPS/diversity gates → 9c.0 |
| Search / rank / ads | **9c.2** (+ **9c.0** gaps) | LTR / ads family pack; BM25/auction/CTR literacy → 9c.0 |
| Forecast / ETA / demand | **9c.3** (+ **9c.0** / M.TS / M.CAUSAL) | Northstar ETA; Uber DeepETA pack |
| Fraud / trust & safety | **9c.4** (+ **9c.0** gaps) | Northstar fraud-on-tokens; Stripe Radar pack |
| LLM / genAI apps | **9c.5** | Northstar RAG slice; five-portfolio / from-scratch-transformer tracks **out of syllabus**; concept gaps → 9c.0 defer |
| NLP / text / support | **9c.5** (+ family pack; **9c.0**) | Support routing / assist; seq-label/GEC literacy → 9c.0 |
| CV / video / OCR | **9c.6** (+ **9c.0**) | Buy Vision/Document AI unless constraints force custom |
| Speech / audio | **9c.6** (+ **9c.0**) | Serving literacy; T-SIGNAL when opened |
| Marketing / churn / CLV / notify | **9c family pack** (+ **9c.0** / M.CAUSAL) | Batch BQML + holdout lift; uplift/survival literacy → 9c.0 |
| Availability / inventory | **9c family pack** | Instacart availability worked example |
| ML platform / infra | **9c.7** | Michelangelo ↔ Agent Platform |
| Other (…) | **Index-only** (+ **9c.0** themes) | Attach a one-liner to a family if it becomes a Northstar force |

Features/labels/skew for every family → **9c.1**. Case-study concept/prereq gaps → **9c.0**. Low-code product pick → **9b.4**. Classical models → **end of 9c** zoo only.

### Recommend / personalize / feed (65)

- Walmart — Recommend complementary items (2023)
- Swiggy — Recommend items to order (2023)
- Lyft — Recommend content in app (2023)
- Etsy — Recommend relevant marketplace items (2023)
- Airbnb — Personalized listing search (2023)
- Twitter — Recommend interesting tweets (2023)
- Linkedin — Personalize the homepage feed (2023)
- Netflix — Personalize video clips (2023)
- Instacart — Personalize user experience by recommending relevant products (2023)
- Pinterest — Recommend similar visual content (2023)
- Spotify — Recommend new complementary music (2023)
- Dailymotion — Recommend diversified video content (2023)
- New York Times — Recommend recipes to readers (2023)
- Expedia — Suggest diverse travel recommendations (2023)
- Stitch Fix — Personalize styling recommendations (2023)
- Netflix — Generate content recommendations for users (2023)
- Delivery Hero — Recommend restaurants for new customers (2023)
- Salesforce — Recommend apps in the marketplace (2023)
- Delivery Hero — Recommend restaurants (2023)
- Ebay — Recommend relevant e-commerce items (2022)
- Doordash — Recommend substitute items (2022)
- Pinterest — Personalize homepage contents (2022)
- Expedia — Categorize customer feedback (2022)
- Ebay — Recommend products and content (2022)
- Yelp — Personalize recommendations (2022)
- Gousto — Recommend food items and recipes (2022)
- Meta — Personalize daily digest notifications (2022)
- Instacart — Recommend relevant food items (2022)
- Doordash — Personalize recommendations on homepage (2022)
- Autotrader — Personalize automotive search results (2022)
- Peloton — Recommend fitness training videos (2022)
- New York Times — Personalize paywall limits (2022)
- Netflix — Recommend content to view (2022)
- Stitch Fix — Recommend e-commerce items (2022)
- Walmart — Curate e-commerce product recommendations (2022)
- Twitter — Recommend accounts to follow (2022)
- Glassdoor — Recommend interesting posts to users (2022)
- Glassdoor — Recommend interesting posts to users (2022)
- Dailymotion — Recommend diversified video content (2022)
- Linkedin — Deliver more relevant job recommendations (2022)
- Cookidoo — Personalize recipe recommendations (2022)
- Pinterest — Recommend bids for advertizers (2021)
- OLX — Recommend e-commerce items (2021)
- Stitch Fix — Recommend e-commerce inventory (2021)
- Gousto — Recommend food items and recipes (2021)
- Spotify — Personalize homepage content (podcasts, playlist, music) (2021)
- Stitch Fix — Recommend looks (2021)
- Walmart — Recommend learning content (2021)
- New York Times — Recommend content to read (2021)
- PayPal — Recommend financial products (2021)
- Scribd — Recommend content to read (2021)
- Wayfair — Recommend furniture items (2021)
- Zillow — Recommend similar homes (2021)
- Spotify — Personalize homepage content (podcasts, playlist, music) (2021)
- Expedia — Personalize travel search results (2021)
- Meta — Personalize the newsfeed content (2021)
- Linkedin — Serve personalized learning recommendations (2020)
- Linkedin — Serve personalized learning recommendations (2020)
- Etsy — Personalize e-commerce search (2020)
- Zynga — Personalize push notification timing (2020)
- Spotify — Recommend shortcuts for homepage (2020)
- Wayfair — Recommend complementary products (2020)
- Airbnb — Recommend marketplace items (2019)
- Gojek — Personalize search results (2019)
- Lyft — Personalize marketing offers (2018)

### Search / rank / ads (36)

- Pinterest — Prevent advertiser churn (2023)
- Airbnb — Improve travel search experience (2023)
- Algolia — Suggest relevant search queries (2023)
- Netflix — In-video search (2023)
- Etsy — Show relevant ads (2023)
- Swiggy — Сonversational and open-ended search (2023)
- Etsy — Search by image (2023)
- Linkedin — Show relevant jobs in search (2023)
- Instacart — Search food and grocery items (2022)
- Spotify — Search for podcasts (2022)
- PayPal — Prioritize sales leads (2022)
- Trivago — Optimize accommodation ranking (2022)
- Airbnb — Improve travel search experience (2022)
- Expedia — Rank relevant travel deals (2022)
- Linkedin — Improve post search functionality (2022)
- Snap — Rank relevant ads (2022)
- Instacart — Autocomplete user searches in e-commerce (2022)
- Doordash — Search food and grocery items (2022)
- Faire — Rank e-commerce items (feature store) (2022)
- Linkedin — Predict ad click-through rate (2022)
- Etsy — Rank marketplace search results (2022)
- Faire — Search and navigate marketplace items (2021)
- Dropbox — Search by image content (2021)
- Microsoft — Rank customer support cases (2021)
- Swiggy — Rank restaurants in search (2021)
- Swiggy — Rank food dishes in search (2021)
- Wayfair — Automate ads placement and bidding (2021)
- Dailymotion — Target contextual advertising (2021)
- Wayfair — Optimize digital ads (2021)
- Airbnb — Rank travel search results (2020)
- Wayfair — Improve search experience for new customers (2020)
- Zillow — Rank homes to buy (2020)
- Doordash — Search for restaurants and dishes (2020)
- Dropbox — Predict files users search for (2019)
- Gojek — Analyse the relevance of search results (2019)
- Airbnb — ML Powered search ranking (2019)

### Forecast / ETA / demand (27)

- Uber — Forecast demand for airport rides (2023)
- Wayfair — Predict delivery times (2023)
- Zalando — Forecast demand in fashion e-commerce (2023)
- Doordash — Forecast order volumes and deliveries (2023)
- Expedia — Forecast flight prices (2023)
- Doordash — Accurately forecast demand during holidays (2023)
- Swiggy — Predict food delivery time (2023)
- Swiggy — Predict food delivery time (2023)
- Swiggy — Predict food delivery time (2023)
- OLX — Predict order delivery time (2023)
- Grubhub — Forecast order volume (2022)
- Gojek — Predict food delivery times (2022)
- Uber — Predict estimated time of arrival (2022)
- Spotify — Forecast user activity metrics (2022)
- Walmart — Forecast anomalies in refrigeration (2022)
- Gojek — Predict estimated time of delivery (2022)
- Lyft — Make causally valid forecasts (2022)
- Lyft — Make causally valid forecasts (2022)
- Grubhub — Forecast volume order (2021)
- Doordash — Predict delivery supply and demand (2021)
- Scribd — Extract metadata from documents (2021)
- Twitter — Forecast resource usage and cost (2021)
- Ocado — Forecast e-commerce grocery demand (2021)
- Mercado Libre — Forecast demand for e-commerce items (2021)
- Instacart — Spot lost demand (2019)
- Gojek — Accurately forecast demand (2019)
- Uber — 100+ Petabytes with Minute Latency (2018)

### Fraud / trust & safety (24)

- Stripe — Prevent fraudelent transactions (2023)
- Linkedin — Detect viral spam (2023)
- Wayfair — Detect fraud with embeddings (2023)
- Zillow — Identify and block unwanted callers (2023)
- BlaBlaCar — Prevent phishing and payment fraud (2023)
- Uber — Detect potential fraudulent entities (2023)
- Grab — Automatically detect new fraud types (2023)
- Whatnot — Detect marketplace spam (2023)
- BlaBlaCar — Prevent phishing and payment fraud (2023)
- Uber — Detect payment fraud (2022)
- Netflix — Detect account or content fraud (2022)
- Grab — Detect fraud with graph models (2022)
- Slack — Detect spam invites (2021)
- Pinterest — Detect spam users (2021)
- PayPal — Detect payment fraud (2021)
- Swiggy — Detect fraud in online food delivery (2021)
- Stripe — Detect fraud in online payments (2021)
- PayPal — Prevent repeated payment fraud (2021)
- Wayfair — Detect payment fraud (2020)
- PayPal — Detect payment fraud (2020)
- Stripe — Detect fraud in online payments (2020)
- Lyft — Predict fraudulent activity (2018)
- Lyft — Identify user fraud (2018)
- Lyft — Shallow to deep learning in fraud (2018)

### LLM / genAI apps (19)

- Stitch Fix — Generate ad headlines (2023)
- Microsoft — Diagnose production incidents with LLM (2023)
- GitHub — Generate code and code suggestions (2023)
- Honeycomb — Generate queries with natural language (2023)
- Spotify — Automatically generate ad content (2023)
- Nextdoor — Generate engaging email subject lines (2023)
- Meta — Generate code with LLM (2023)
- GitHub — AI copilot for code generation (2023)
- Doordash — Areas for using Generative AI (2023)
- Spotify — Generate audio podcast previews (2023)
- Thoughtworks — AI copilot for product strategy (2023)
- Salesforce — Summarize Slack conversations (2023)
- Instacart — Build an internal AI assistant (2023)
- Vimeo — Customer support AI assistant (2023)
- Google — Generate summaries (2022)
- Google — Summarize conversations (2022)
- Nordstrom — Generate outfit combinations (2021)
- Gojek — Generate names for pickup points (2020)
- Zillow — Generate floor plans from photos (2020)

### NLP / text / support (7)

- Grab — Automatically tag sensitive data (2023)
- Salesforce — Extract relevant information from a knowledge article (2023)
- Dropbox — Identify date formats in file names (2023)
- Meta — Translate and transcribe across speech and text (2023)
- Nextdoor — Predict harmful comments (2022)
- Wayfair — Predict intent in customer support messages (2022)
- Pinterest — Detect policy-violating comments (2021)

### CV / video / OCR (6)

- Apple — Identify objects on images (2023)
- Netflix — Improve video quality at scale (2022)
- Doordash — Extract information from images (2021)
- Bumble — Derive information from images (2020)
- Dailymotion — Automatically categorize videos (2020)
- Dropbox — Modern OCR with CV and DL (2017)

### Speech / audio (3)

- Netflix — Detect speech and music in audio (2023)
- Walmart — Fill shopping cart via voice dialog (2022)
- Amazon — Suggest music to listen to (2022)

### Marketing / churn / CLV / notify (14)

- Monzo — Select relevant marketing messages (2023)
- Expedia — Predict Customer Lifetime Value (CLV) (2023)
- Grab — Сreate scalable lookalike audiences (2023)
- Grab — Optimize promotional campaigns (2023)
- Gousto — Predict subscription churn (2022)
- Uber — Send timely push notifications (2022)
- Artefact — Evaluate success of past promotions (2022)
- Linkedin — Predict churn and upsell products (2022)
- Wayfair — Optimize email sending time and frequency (2022)
- Netflix — Apply causality in experiments and marketing (2022)
- Pinterest — Find lookalike users for ad targeting (2021)
- Wayfair — Optimize paid media marketing (2021)
- Doordash — Optimize marketing spending (2020)
- Lyft — Build a marketing automation platform (2019)

### Availability / inventory (5)

- DoorDash — Predict if a store is open (2023)
- Instacart — Predict availability of food items (2023)
- Instacart — Predict grocery item availability (2023)
- Instacart — Predict availability of food items (2023)
- Instacart — Predict grocery item availability (2018)

### ML platform / infra (2)

- King — Automate playtesting pipeline (2019)
- Uber — Scaling ML with Michelangelo (2019)

### Other (pricing, classification, routing, dimensions, …) (101)

- Foodpanda — Optimize menu sorting order (2023)
- Zillow — Estimate the house market value (2023)
- Airbnb — Identify user interests (2023)
- DoorDash — Optimize courier waiting time (2023)
- Linkedin — Select best payment gateway (2023)
- Yelp — Organize e-commerce content using embeddings (2023)
- Monzo — Detect patterns in text data (2023)
- Wayfair — Predict new product’s sales potential (2023)
- Wayfair — Identify business customers (2023)
- Criteo — Figure out users' preferences (2023)
- Grammarly — Suggest gender-inclusive grammatical error corrections (2023)
- Delivery Hero — Better understand user behavior (2023)
- Expedia — Alert users about optimal deals (2023)
- Walmart — Resolve entities and detect relationships (2023)
- Wayfair — Send relevant communications to customers (2023)
- Meta — Show users relevant content at scale (2023)
- GitHub — Automated code reviews and PR tagging (2023)
- Spotify — Target in-app messaging (2023)
- Nubank — Automatically route customer phone calls (2023)
- Mercado Libre — Predict product dimensions for delivery (2022)
- Walmart — Assist in e-commerce shopping (2022)
- Foodpanda — Classify restaurants and cuisines (2022)
- Github — Detect vulnerabilities in code (2022)
- Doordash — Find high-value merchants (2022)
- Grammarly — Suggest text edits (2022)
- Zillow — Select tags for product listings (2022)
- Airbnb — Improve customer support (2022)
- Walmart — Categorize e-commerce products (2022)
- Zillow — Identify customers that are likely to convert (2022)
- Zillow — Extract text features (2022)
- Lyft — Optimize trip price (2022)
- Grammarly — Correct grammatical errors (2022)
- Airbnb — Improve customer travel experience (2022)
- Swiggy — Flag incorrectly captured locations (2022)
- Uber — Verify documents (2022)
- Didact AI — Predict stock prices (2022)
- Wayfair — Identify specific entities within a text (2022)
- Oda — Predict driver's non-driving time (2022)
- Linkedin — Estimate the impact of product changes (2022)
- Siemens Healthineers — Optimize software testing (2022)
- Linkedin — Improve ML model performance with multitask learning (2022)
- Google — Suggest past photos to look at (2021)
- Uber — Identify cash intermediaries (2021)
- Microsoft — Cluster customer support issues by similarity (2021)
- Apple — Recognize people in photos (2021)
- Datto — Predict hard drive failures (2021)
- Bumble — Detect rude messages (2021)
- Nextdoor — Send relevant and timely updates (2021)
- Dropbox — Identify best time for renewal charge (2021)
- Brex — Classify bank transactions (2021)
- Grammarly — Capture what readers pay attention to (2021)
- Apple — Identify best user experience (2021)
- Airbnb — Data privacy and security (2021)
- Capital One — Identify suspicious account activity (2021)
- Wayfair — Assign color names to products (2021)
- Capital One — Automate incident management (2021)
- Walmart — Categorize e-commerce products (2021)
- Walmart — Identify refrigeration defrost (2021)
- Capital One — Improve cardholder experience (2021)
- Shopify — Categorize e-commerce products (2021)
- Amazon — Predict coordinates of delivery location (2021)
- PayPal — Predict declined transactions (2021)
- Slack — Predict Slack connect invites (2021)
- Grammarly — Detect grammatical errors (2021)
- Doordash — Deliver orders on time (2021)
- Lifen — Recognize PDF layout (2021)
- Bumble — Detect rude messages (2021)
- Swiggy — Estimate travel distance (2021)
- Scribd — Classify documents (2021)
- Google — Correct grammatical errors (2021)
- Nubank — Predict conversions and attract new customers (2021)
- Grammarly — Correct grammatical errors (2021)
- Scribd — Classify user-uploaded documents (2021)
- Oda — Predict driver's non-driving time (2021)
- Mercado Libre — Predict customer engagement and LTV (2021)
- Wayfair — Show relevant content to new customers (2021)
- Microsoft — Classify cloud workload types (2021)
- Github — Help users find contribution opportunities (2020)
- Mozilla — Predict the outcome of software tests (2020)
- Adyen — Predict probability of transaction success (2020)
- Lyft — Provide location suggestions (2020)
- Twitter — Predict value of ad requests (2020)
- Picnic — Predict delivery drop times (2020)
- Shopify — Categorize e-commerce products (2020)
- Gojek — Target cross-sell to existing users (2020)
- OLX — Detect stolen photos (2020)
- Duolingo — Teaching foreign languages (2020)
- Firefox — Automatically assign new untriaged bugs (2019)
- Zoominfo — Predict data accuracy (2019)
- Lyft — Predict location of traffic control elements (2019)
- Apple — Identify text language (2019)
- Stitch Fix — Extract information from customer notes (2019)
- Lyft — Detect errors in maps (2019)
- Wayfair — Model uplift (2019)
- Lyft — Predict rides and driver hours (2019)
- Netflix — Improve streaming quality (2018)
- Instacart — Optimize food delivery logistics (2017)
- Airbnb — Predict Value of Homes (2017)
- Netflix — Improve Streamning Quality (2018)
- Booking.com — 150 Successful Machine Learning Models (2019)
- Chicisimo — Grow User base using vertical ML approch (2019)

---

## Appendix G — Go module reference (not a teaching track)

Unlock each module at the **owner** below. Artifact is required when that owner is taught. Python still comes first on the same slice. **Part 11 cannot close until every owner in F–11b has its Go artifact (or a documented skip-test).** G10–G12 is the **same lab as Part 4.2**, not a second HTTP course.

| Module | Concepts | Artifact | Owner |
|---|---|---|---|
| **G0** | Git/SSH, install, modules, `go env`, `gofmt`/`go vet` | Recover broken `go.mod`; setup runbook | F1, 0.1 |
| **G1** | `main`, types, vars, `for`/`if`/`switch`, arrays, `_` | Tested command; predict overflow | F1, 0.1 |
| **G2** | slices, maps, functions, `defer`, errors, runes; stacks/queues | Slice aliasing + map tests; no ignored errors | F1, first Go submit |
| **G3** | pointers, structs, methods, interfaces, generics; lists/heap/hash | Ports as interfaces; nil-interface tests | 3.0 |
| **G4** | files, `bufio`, `embed`, time; serialize | WAL-shaped codec | 2.1 / DB-10 |
| **G5** | flags, env, JSON; CLI | `--help`, env override | 0.1, 11b P8 |
| **G6–G7** | goroutines, `select`, `context`, mutex, race detector | Cancelled context stops work; race pass | 3.2, 3.4, 4.2 |
| **G8–G9** | sort, binary-search invariant, recurrences, DP, benchmarks | Choose paradigm; explain crossover | 8.1 |
| **G10–G12** | `net/http`, REST, middleware, SQL CRUD, graphs as needed | Hardened server timeouts/limits/4xx table | 1.2, 4.2, Part 2 CRUD |
| **G12b** | Postgres internals | DB-1–10 artifacts | Part 2 |
| **G13–G15** | protobuf, gRPC streams, interceptors | Same `.proto` as catalog RPC | 3.2 |
| **G16–G18** | OTel, pprof, `govulncheck`, Docker, release | Traced service; nonroot image | 1.6, 1.7, 10.0, D1 |
| **G19** | Synthesis | Unseen DS + API + concurrency from unlocked tools | Part 8 studios |
| **G20** | Ledger, idempotent charge, webhook | Types + tests with Stripe | Part 5 |

**G-CS (discrete):** with F1 (counterexample, loop invariant) and 8.1 (asymptotics, hash-ring invariant). Not a separate part.

Every **Owner** cell above is a real `####` / `###` after this expansion — unlock the Go artifact when that owner is taught; do not treat Appendix G as a second track. Appendix M stays an index (no article text added here).
