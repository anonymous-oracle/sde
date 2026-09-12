# Google Cloud Production Architect — Curriculum

Student-facing copy. Canonical teaching order is the course spine below. Python exercise first; Go version after you submit. Teaching does not start until you say to start.

**Outcome:** You can design, implement, and operate **secure industry software on GCP** — frontend, backend microservices, identity, and payments — at Professional Cloud Architect judgment, with HLD and LLD as working habits.

**Constraints you set (locked):**
- Production deploy of frontend + backend microservices is taught **first**.
- Billing is at the **start** (cannot deploy industry software without it).
- Then authentication, then payment systems, then the rest of architect depth.
- **First-class (not optional, not “later if time”):** SQL database design; Cloud SQL setup on GCP; Compute Engine; App Engine; Cloud Run; Cloud Functions; GKE; hybrid connectivity (VPN, Interconnect); network security; cybersecurity; IAM; Cloud Identity; storage; Spanner; NoSQL; Big Data; Vertex AI / Gemini; Operations Suite; billing; DevOps/Docker/K8s/CI/CD/GitOps; **gRPC + protobuf + HTTP/2; QUIC + HTTP/3; SOLID; design patterns; hexagonal/clean architecture; DDD; microservices pattern catalog; production-scale primitives (bloom filters, consistent hashing, WAL, load shedding, …)**. Each idea has **one home** (see placement: Part 3.0, 3.2, 6.1, 8). No parallel duplicate parts.
- **PCA v6.1 complete:** every bullet in the official exam guide (English on/after 30 Oct) has a home in this course, including Vertex AI Pipelines, AI Hypercomputer, Model Garden, Gemini Enterprise, Model Armor, Migration Center, Google Cloud VMware Engine, Apigee, Terraform, Cloud Emulators, Gemini Cloud Assist.
- **Absolute-beginner prerequisites** sit in Foundation Block F. A software engineer can skip-test; an absolute beginner cannot skip F.
- Prerequisites are researched and taught **just-in-time**, not as a six-month wall before GCP.
- After every subtopic: concept → **from-scratch implementation** (your own code, servers, middleware) → HLD → LLD → GCP lab → **Python exercise**. After you submit, the **same exercise in Go**.
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

### 4. HLD vs LLD (taught as a craft, not a slide)
| | HLD | LLD |
|---|---|---|
| Question | What exists and why? | Exactly how does it work? |
| Audience | stakeholders, PCA case study, new teammates | implementers, reviewers, on-call |
| Artifacts | context diagram, container diagram, NFR table, cost/risk, ADRs | sequence, schema, API spec, IAM, Terraform, class/module design, failure matrix |
| Donne Martin step | Step 2: high-level design | Step 3: core components + Step 4: scale |

Donne Martin’s four interview steps become the **design loop for every Northstar change**: constraints → HLD → core LLD → scale/security/cost.

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
| Big data / AI | Pub/Sub, Dataflow, Dataproc, BigQuery, Vertex AI, Gemini, Model Garden, Model Armor |
| Operations | Cloud Logging, Monitoring, Trace, Profiler, Error Reporting, alerting, SLOs |
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
| Go modules, `context`, `net/http`, table tests | after each Python submit | Taught as a parallel implementation, not a language course first. |
| HLD/LLD literacy | 0.4 then every module | Donne Martin loop. |
| SOLID, hexagonal, DDD | 3.0 | Before split; CI grep on imports. |
| Protobuf, gRPC | 3.2 | Internal s2s; REST stays public. |
| HTTP/2 HOL, QUIC ideas | 6.1 | Transport only; crypto is stdlib. |
| Bloom, hashing, WAL, shed | 8.1 | Scale primitives. |

Linux/OS/sysadmin/networking/cybersecurity from the original request are **not dropped**. They are sequenced **after you have a running product**, so they attach to real GCP failure modes (IAM, VPC, audit logs, container escape surface, supply chain) instead of abstract distro admin.

---

## Course spine

```
F  Foundation for absolute beginners + cloud computing fundamentals
   F1 Computers, OS, CLI, Git, HTTP, Python/Go enough-to-start
   F2 What is cloud, deployment models, service models (IaaS/PaaS/SaaS)
   F3 Google Cloud global infrastructure (regions, zones, PoPs, edge)
   F4 Account setup: hierarchy, free tier, console, SDK, Cloud Shell, projects, quotas, APIs, admin user

0  Billing (full), cost kill-switch, HLD/LLD contract
   + IAM core (policies, conditions, service accounts, Cloud Identity, best practices)

1  Compute platforms + first production deploy
     1A Docker (full) then Cloud Run (deploy frontend + backend first)
     1B Compute Engine
     1C App Engine + Cloud Functions
     1D HA: load balancers + MIGs
     1E Decision matrix

D  DevOps, CI/CD, GitOps, supply chain (first-class; after you have a running service)
     D0 Culture: CALMS, DORA, SRE vs DevOps vs platform engineering
     D1 Docker/OCI/BuildKit (if not already solid from 1A)
     D2 Continuous integration (Cloud Build, GitHub Actions, WIF, tests, scanners)
     D3 Continuous delivery + GitOps (Cloud Deploy, Skaffold, kustomize, Helm, Argo/Flux)
     D4 Progressive delivery (rolling, blue-green, canary) on Cloud Run and GKE
     D5 Supply chain (SLSA, Binary Authorization, Artifact Analysis, SBOM, cosign)
     D6 Platform engineering (preview envs, golden paths, policy as code)

2  SQL design + Cloud SQL setup + GCS + Firestore + Spanner + NoSQL map

3  Microservices: SOLID/hexagonal/DDD (3.0) → split → gRPC (3.2) → saga/outbox
   (no separate architecture or protocol semester)

4  Authentication and authorization (customers + workloads) — Identity Platform, IAP, WIF

5  Payments, webhooks, PCI-aware design

6  Networking in full + HTTP/2 HOL demo + mini-QUIC (ideas only; crypto is stdlib)

7  Network security + cybersecurity (NGFW, Armor, IAP, VPC-SC, KMS, SCC, DLP, org policy, IR)

8  Hybrid connectivity (Cloud VPN, Cloud Interconnect, NCC) + migration (Migration Center)

9  Kubernetes internals (CKA-level) + GKE + GitOps onto the cluster

10 HLD/LLD mastery (Donne Martin) + Well-Architected + PCA design domains

11 Vertex AI / Gemini / Big Data (PCA v6.1 §§2.4–2.5 and 1.3 ML/AI)

12 Operations Suite + reliability + FinOps + IaC (Terraform primary, Deployment Manager legacy)

13 Capstone (Northstar v1) + PCA case studies (Altostrat, Cymbal, EHR, KnightMotives)
```

This file is `~/gcp-curriculum.md`.

---

## Block F — Absolute beginner + cloud computing fundamentals

Required if you cannot yet: use a terminal, explain HTTP, or explain IaaS vs PaaS. Software engineers skip-test each F subsection; fail any check and you do that subsection fully.

### F1 Absolute beginner computing (pre-GCP)
- Computer: CPU, RAM, disk, network interface.
- OS: process, file, user, permission, env var, stdout/stderr. Linux enough to survive Cloud Shell: `ls`, `cd`, `cat`, `chmod`, `ps`, `grep`, `jq`, pipes.
- CLI vs GUI. Shell, PATH, exit codes.
- Git: clone, branch, commit, push, PR.
- Networks in one sitting: IP, port, DNS, TCP vs UDP, HTTP methods, status codes, TLS, JSON.
- **From scratch:** bind a TCP socket, read a request line, write `HTTP/1.1 200` + JSON. This is the first middleware host. FastAPI comes after.
- Python enough: venv, `pip`, functions, types, pytest, then FastAPI.
- Go enough (after first Python submit later): modules, `net/http`, `testing`.
- **Exercise:** Python HTTP server that returns JSON; after submit, Go version.

### F2 What is cloud computing
- On-prem vs colocation vs cloud. Elasticity, pooled resources, metered billing, API-provisioned.
- **Deployment models:** public, private, hybrid, community, multi-cloud.
- **Service models:** IaaS (GCE), PaaS (App Engine, Cloud Run), SaaS (Workspace). FaaS as a PaaS slice (Cloud Run functions).
- Shared responsibility.
- CapEx vs OpEx (PCA 4.2).
- **HLD exercise:** classify 10 Northstar components as IaaS/PaaS/SaaS and defend.

### F3 Google Cloud global infrastructure
- Regions, zones, multi-region, dual-region. Latency vs data residency.
- Points of presence, Cloud CDN edge, Google Front End.
- Resource scope: zonal (GCE VM, PD), regional (Cloud Run, subnet, Cloud SQL HA), global (VPC, IAM, GCS multi-region, global LB).
- **Python / Go:** given a list of products, tag zonal/regional/global (unit tests).

### F4 Account setup (from the video outline, required)
- Resource hierarchy: org, folder, project, resource. Inheritance.
- Create / link free-tier + trial. Securing the account (2SV, recovery, super-admin hygiene).
- Console overview: search, Cloud Shell button, IAM, APIs, billing.
- Cloud APIs: enable, quotas, why APIs are closed by default.
- Adding an admin user; Organization Admin vs Project Owner vs Billing Admin (separation of duties — PCA 3.1).
- Cloud SDK and CLI: install, `gcloud init`, configurations, components, updates, `gcloud` vs `gsutil` vs `bq` vs `kubectl`.
- Managing Cloud SDK: versions, named configs, `CLOUDSDK_CORE_PROJECT`.
- Cloud Shell and Editor; Cloud Code (PCA 5.2).
- Creating and managing projects. Project ID vs number vs name.
- Limits and quotas: default, how to request, how quotas stop surprise bills.
- **Lab:** new project, enable APIs, second admin user in a group, `gcloud` from Cloud Shell and from local, hit a quota wall on purpose (e.g. list), document it.

---

## Part 0 — Day-zero: billing, IAM core, and how we design

**Why first:** You asked for billing at the start. Google’s landing zone series also starts with organization + billing account. You cannot deploy industry software without this. IAM is here because billing without IAM is an open checkbook.

### 0.1 Cloud Billing (full, not a sidebar)
- Billing account vs project vs organization vs folder.
- Cloud Billing is **not** in the resource hierarchy; it attaches at project. Reports can roll up by hierarchy.
- Roles: Billing Account Administrator, User, Viewer, Costs Manager. Least privilege vs Organization Admin.
- Invoices, credits, Always Free vs $300 trial, committed use (later).
- SKUs you will actually hit: Cloud Run CPU/memory/requests; GCE instance-hours + idle public IP; App Engine instance-hours above 28 F1/day; Cloud SQL instance-hours (no free tier); PD GB-month; egress; Artifact Registry; Logging beyond 50 GiB; accidental LB forwarding rules and Cloud NAT hours.
- Budgets, alerts, billing export to BigQuery (export may exceed free tier — teach, optional lab).
- Labels vs tags for cost allocation.
- **Lab:** create/link billing, budget $10 with 50/90/100% alerts, confirm Always Free products, write a one-page cost model for Northstar v0.
- **Python exercise:** parse a sample Cloud Billing CSV/JSON export; group cost by `service` + `sku` + label; flag any SKU that is not Always Free.
- **Go version after submit:** same report as a CLI (`cobra` or stdlib flags).

### 0.2 You, the CLI, and Cloud Shell
- `gcloud` auth, ADC, `gcloud config`, projects, quota.
- Cloud Shell vs local SDK.
- **JIT Linux:** filesystem, `$PATH`, env, permissions, pipes, `jq`.
- **Lab:** `gcloud` from Cloud Shell; list projects; enable APIs via service usage (and why enabling APIs costs nothing until you use them).

### 0.3 Resource hierarchy (minimum to deploy)
- Organization → folders → projects → resources.
- Inheritance of IAM and org policies.
- One org when possible. Projects as trust + billing boundaries.
- **HLD:** Northstar folder layout: `shared`, `prod`, `nonprod`.
- **Python:** Resource Manager API — list projects, print ancestry.

### 0.4 HLD/LLD contract + Donne Martin
- Four steps: constraints → HLD → core LLD → scale.
- ADR template (context, decision, consequences, status).
- NFR table: latency, availability (nines), RPO/RTO, threat, cost, compliance.
- **Exercise (no code):** HLD one-pager for Northstar v0 using Donne Martin’s questions (users, QPS, read/write ratio, data size). This artifact is reused all course.

### 0.5 Cloud IAM (full offering — video outline + PCA 3.1)
- Resource hierarchy as the attachment point for allow policies.
- Principals: user, group, service account, domain, workforce/workload federated.
- Roles: basic (Owner/Editor/Viewer — avoid), predefined, custom.
- Allow policy structure: bindings, conditions (CEL), time/resource attributes.
- Deny policies. Policy inheritance and effective policy.
- Service accounts: user-managed vs default (disable defaults). Attach vs impersonate vs keys (keys last resort).
- Service account best practices: one SA per service, no key files, WIF, `iam.disableServiceAccountKeyCreation`.
- Cloud Identity vs Google Workspace vs Identity Platform (three different products).
- Cloud Identity: users, groups, Directory Sync, super admin.
- IAM best practices: groups, least privilege, SoD, break-glass, audit.
- **Lab:** custom role with three permissions; condition on time; SA with no keys; group-based binding.
- **Python / Go:** parse an IAM policy JSON; evaluate whether principal P can do permission X on resource R (simplified).

---

## Part 1 — Compute platforms, then deploy frontend + backend first

**Goal:** Understand the three first-party compute offerings you will actually be asked about as an architect (Cloud Run, Compute Engine, App Engine), then **ship** Northstar v0 on Cloud Run. GKE comes later.

### 1.0 Compute landscape (architect, not catalog)
- Cloud Run if Google manages infra and the workload is a container (request, job, worker pool).
- App Engine if you want a PaaS with services/versions/traffic split and are in an existing GAE estate — or for the PCA.
- Compute Engine if you must manage the OS, custom kernels, third-party appliances, or lift-and-shift VMs.
- GKE if you need Kubernetes (custom networking, sidecars, stateful operators, GPU pools).
- Cloud Run **functions** = specialized source deploy of a Cloud Run **service**.
- **ADR-001:** Cloud Run for Northstar v0 default. You will still **implement the same API** on GCE and App Engine so the trade-offs are felt, not memorized.

### 1.2 Container contract (LLD that production depends on)
- Docker/OCI from Part D1 is assumed: multi-stage image, nonroot, digest, SIGTERM.
- Listen on `PORT`. Stateless. Ephemeral local disk. SIGTERM drain. Concurrency (default 80, max 1000). CPU allocation (request-based vs instance-based billing). Min instances vs scale-to-zero.
- Revisions, traffic split, tags (canary).
- **Lab:** containerize a FastAPI health + echo API; deploy Cloud Run service; hit `*.run.app`; read logs.
- **Python exercise:** implement `/healthz`, `/readyz`, graceful shutdown, structured JSON logs, request ID middleware.
- **Go after submit:** same contract with `net/http` + `errgroup` + SIGTERM.

### 1.3 Frontend hosting (industry options, free-tier path)
Decision tree:
| Frontend type | GCP path | Free-tier lab |
|---|---|---|
| Static SPA | Cloud Storage website + (optional) LB/CDN | GCS bucket public read **or** Firebase Hosting |
| SSR (Next/Nuxt) | Firebase App Hosting = Cloud Build + Cloud Run + CDN | Firebase Hosting static export if App Hosting exceeds credits |
| Server-rendered from your API | Cloud Run service serving HTML | Cloud Run |

- CORS, cache headers, security headers (CSP, HSTS).
- **Lab:** static storefront on Firebase Hosting calling the Cloud Run API.
- **Python:** tiny Jinja/static generator or FastAPI `StaticFiles` alternative path; document why Hosting is preferred for SPA.

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
- Runtime service account per service. No user credentials in prod. No downloaded keys.
- Secret Manager for API keys (Stripe later). Env vars for non-secret config.
- **Lab:** dedicated SA, `roles/secretmanager.secretAccessor` only, deny `roles/editor`.
- **Python:** read a secret at startup, never log it, rotate-friendly.

### 1.6 First pipeline (minimum to ship) — full CI/CD is Part D
- Enough to stop deploying from a laptop: Cloud Build + Artifact Registry + WIF from GitHub.
- Buildpacks vs Dockerfile (Dockerfile is the LLD you already wrote in D1 / 1.2).
- **Lab:** push → test → build → Cloud Run revision → 10% traffic tag → 100%.
- After this lab, Part D replaces this ad-hoc deploy with Cloud Deploy, GitOps, and supply-chain gates.
- **Python / Go:** tests must pass in the build.

### 1.7 Observability from day one
- Structured logs, trace context, Error Reporting, uptime check (external IP limitation: Cloud Run URL works).
- SLIs for the API: availability, latency p95.
- **Python:** OpenTelemetry or Cloud Trace spans around Firestore later; for now request timing.

**Part 1A exit criteria:** You can explain and demo: “Here is the frontend, here is the API on Cloud Run, here is how it deploys, here is who it runs as, here is what it costs if I leave it up.”

### 1.8 Compute Engine (full offering)

Concept first: you own the guest OS. Google owns the hypervisor, host, and physical network.

GCP offerings in this family:
- **Compute Engine VMs** — machine families (E2, N2, N2D, C3, C4, Tau T2A/T2D, GPU/TPU attachments, Axion/Arm).
- **Persistent Disk / Hyperdisk** — pd-standard, pd-balanced, pd-ssd, Hyperdisk Extreme/Throughput; snapshots; images.
- **Instance templates + Managed Instance Groups** — autoscaler, autohealing, rolling updates, stateful MIGs.
- **OS Login, OS Config / VM Manager, OS patch** — the sysadmin surface.
- **Spot / preemptible VMs**, sole-tenant nodes, confidential VMs, Shielded VMs.
- **IAP TCP forwarding** — SSH without a public IP.
- **Ops Agent** — logs and metrics.
- Always Free: **1× e2-micro** in us-central1, us-west1, or us-east1 + 30 GB standard PD.

Curriculum (covers the full Compute Engine video block):
- **Virtualization fundamentals:** hypervisor, guest OS, paravirtualization vs HVM; why GCE is IaaS.
- Machine type selection, families, custom types, shared-core (e2-micro), GPU/TPU, Spot vs standard (PCA 2.3 volatility).
- Creating and managing instances; live migrate vs terminate; availability policy.
- Connecting: SSH keys vs OS Login vs IAP TCP (no public IP).
- Metadata server and startup scripts; project vs instance metadata; why metadata SSRF is a real attack.
- Compute Engine **billing SKUs**: vCPU, memory, PD, GPU, idle public IP, egress, CUD, Spot discount.
- **Storage on GCE:** Persistent Disk (standard/balanced/SSD/extreme), Hyperdisk, Local SSD (ephemeral, performance), boot vs additional, resize, attach/detach, zonal vs regional PD.
- Snapshots, snapshot schedules, images, image families, custom images.
- Startup scripts vs instance templates vs OS Config / VM Manager / OS patch.
- VPC NIC, external IP vs no external IP + Cloud NAT + IAP SSH.
- Unmanaged vs managed instance groups; health checks; backend service for HTTP(S) LB.
- Patching, image baking (Packer concept), golden images vs cattle.
- **Deployment Manager** (legacy YAML/Jinja/Python templates) — PCA still mentions IaC broadly; **Terraform is the production default**. Lab: read a DM template, rewrite it in Terraform. Do not start new work in DM.
- **Lab (Always Free):** e2-micro, no public IP, OS Login + IAP tunnel, Ops Agent, nginx or the Northstar API in a systemd unit, snapshot, custom image. Tear down if you attach a public IP or extra disks that bill.
- **HLD:** lift-and-shift 3-tier (MIG web + MIG app + Cloud SQL). When this loses to Cloud Run.
- **Python:** use Compute Engine API to list instances, start/stop the sandbox VM, attach a label. **Go:** same with `google.golang.org/api/compute/v1`.
- **Billing SKUs to memorize:** instance-hours, PD GB-month, snapshot, external IP (idle IP charges), egress, NAT gateway hours.

### 1.9 App Engine (full offering)

Concept: PaaS. You give it code; Google gives you versions, traffic split, cron, and a appspot.com HTTPS URL.

GCP offerings:
- **App Engine standard** — sandboxed runtimes (Python, Go, Java, Node, PHP, Ruby), scale-to-zero, 28 F1 hours/day free.
- **App Engine flexible** — containers on GCE VMs you don't fully manage; no scale-to-zero; rarely the right new choice vs Cloud Run.
- Services, versions, traffic splitting, App Engine cron, Task Queues (legacy; Cloud Tasks is the successor), app.yaml, dispatch.yaml, cron.yaml, IAP on App Engine.
- **App Engine vs Cloud Run vs Cloud Run functions** — Google’s current guidance: new container HTTP apps → Cloud Run. App Engine remains on PCA and in brownfield.

Curriculum:
- `app.yaml`, automatic vs basic vs manual scaling, max instances, warmup.
- Deploy a version, split 50/50, roll back.
- App Engine firewall, IAP, service-to-service `X-Appengine-*` (legacy) vs IAM.
- **Lab (Always Free standard):** deploy the same Northstar health API as an App Engine standard Python service; split traffic; then deploy the Go version as a second version. Delete when done so F1 hours stay inside the free 28/day.
- **Python / Go:** identical handlers on GAE standard.
- **ADR-001b:** App Engine is taught and labbed; Northstar production path stays Cloud Run unless a constraint (existing GAE org, specific sandbox) wins.

### 1.10 Decision matrix (you will reuse this on the PCA)

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
- Event-driven FaaS: HTTP, Pub/Sub, Storage, Firestore triggers.
- 1st gen vs 2nd gen (2nd gen **is** a Cloud Run service).
- Cold start, timeout, IAM invoker, VPC connector.
- Always Free: 2M invocations/month on Blaze.
- **Lab:** GCS object-finalize → function writes metadata to Firestore. Python then Go.
- **ADR:** new HTTP APIs → Cloud Run services; glue events → Cloud Run functions / Eventarc.

### 1.12 High availability and autoscaling (video block, required)
- Why a single VM is not an architecture.
- **Cloud Load Balancing** in full: HTTP(S) external global/regional, internal HTTP(S), SSL proxy, TCP proxy, network passthrough (external/internal), target pools vs backend services.
- Health checks, backend services, NEGs (GCE, zonal, internet, serverless, hybrid).
- Session affinity, CDN enable, SSL policies, URL maps, host/path rules.
- **Instance templates** + **MIGs**: autoscaler (CPU, load balancing, Cloud Monitoring metric, schedules), autohealing, rolling updates, canary, proactive/opportunistic.
- Regional MIG vs zonal. Multi-zone HA.
- **Lab (free-tier boxed):** two e2-micro in a regional MIG is usually **not** free (second VM bills). Diagram + Terraform required; live MIG only if credits. Alternative: Cloud Run min-instances=0 with a second region sketched.
- **Python / Go:** health endpoint that fails on a file flag — used by LB health checks in the credits lab.

**Part 1 full exit:** Same API proven on Cloud Run (primary), App Engine standard, Cloud Functions (event glue), and a GCE MIG/systemd path. You can defend the choice in an ADR. You can draw an HTTP(S) LB → MIG and an HTTP(S) LB → serverless NEG.

---

## Part D — DevOps, Docker, Kubernetes, CI/CD, GitOps

**Goal:** You can build, sign, promote, and roll back Northstar the way a 2026 GCP platform team does — not “a Jenkinsfile that SSHs to a VM.”

Research used: Google Cloud Build + Artifact Registry + Cloud Deploy + Skaffold (GCP-native shortest path); modern CI/CD with GKE (GitHub, kustomize, two-repo GitOps); Cloud Deploy canary for GKE and Cloud Run; Binary Authorization + SLSA; DORA; Docker BuildKit multi-stage/distroless; Kubernetes 1.33–1.37 (sidecar GA, user namespaces, DRA, Pod-level resources, PSA); Argo CD vs Flux vs Cloud Deploy.

Free-tier: Cloud Build 2,500 e2-standard-2 minutes/month; Artifact Registry 500 MB; Cloud Deploy first active pipeline per billing account. GKE/Argo live remains credits-optional; kind/minikube is required.

---

### D0 DevOps culture (concept, then GCP)

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
      → hand digest to CD (do not kubectl here)
```
- Build once, promote the digest. Rebuild-per-env is a defect.
- Branching: trunk-based as the DORA-friendly default; GitFlow only if you can defend the lead-time cost.
- Quality gates: tests must be deterministic. Flaky tests are change-failure-rate.

#### D2.2 Cloud Build (GCP-native CI)
- `cloudbuild.yaml` steps, images (`gcr.io/cloud-builders/docker`, `gke-deploy`, official builders).
- Substitutions, secrets from Secret Manager, available secrets vs worker pool.
- Triggers: GitHub (2nd gen, **WIF, no PAT in a secret if you can avoid it**), Cloud Source Repositories, Pub/Sub, manual.
- Private pools (VPC, private GKE, private Cloud SQL). Default pool has no VPC.
- Caching: Kaniko/BuildKit cache to AR; Kaniko is legacy-ish — Cloud Build docker + buildx is the 2026 path.
- Provenance: Cloud Build can emit SLSA provenance (trusted builder for Binary Authorization SLSA check).
- Quotas: 2,500 e2-standard-2 minutes/month Always Free. Use small images.
- **Lab:** trigger on `main` → pytest → docker build → push `:sha` and digest. No deploy step yet.
- **Python:** a failing test must fail the build. **Go:** `go test ./...` same.

#### D2.3 GitHub Actions (where the code lives)
- Workflows, jobs, matrix, environments, OIDC.
- **Workload Identity Federation** from GitHub → GCP. No JSON keys. This is the production pattern.
- `google-github-actions/auth` then `setup-gcloud` / docker auth to AR.
- When Actions vs Cloud Build: Actions if the org is GitHub-first; Cloud Build if you want provenance from Google’s trusted builder and builds inside Google’s network (faster AR/GKE push).
- GitLab CI, CircleCI: same OIDC/WIF idea. Jenkins only as brownfield (PCA may still mention it).
- Tekton: Kubernetes-native pipelines; Cloud Build is hosted Tekton-ish. Teach as “if you must run CI on GKE.”

#### D2.4 Tests in CI
- Unit, contract (OpenAPI/schemathesis), integration (Firestore emulator, Pub/Sub emulator, Postgres in Docker — PCA 5.2 emulators).
- Load is **not** CI-on-every-commit; it is a CD verify job or nightly.
- **Python / Go:** Testcontainers-style Postgres test for the order transaction from Part 2.

#### D2.5 Scanning in CI (DevSecOps gates)
- Secret scanning (gitleaks / GitHub native) — fail on `STRIPE` keys.
- SAST (lightweight).
- SCA / `pip-audit` / `govulncheck`.
- Image scan: Artifact Analysis on AR; fail on CRITICAL. Trivy as local equivalent.
- IaC: `tflint`, Checkov/tfsec on Terraform.
- **Lab:** a planted secret must fail the pipeline. A CRITICAL CVE in a base image must fail.

---

### D3 Continuous delivery and GitOps

CD = the **same digest** moves through environments with an audit trail and a rollback.

#### D3.1 CI vs CD vs GitOps
| | CI | CD (push) | GitOps (pull) |
|---|---|---|---|
| Trigger | commit | pipeline step / promote | Git desired-state change |
| Actor | Cloud Build / Actions | Cloud Deploy / `gcloud run deploy` | Argo CD / Flux / Cloud Build-on-env-repo |
| Source of truth | source repo | pipeline config + artifact | **env Git repo** |
| Prod kubectl | forbidden | via controller | via controller |

Google’s two documented patterns:
1. **Cloud Build + Cloud Deploy + Skaffold** — GCP-native, canary on GKE and Cloud Run, Console promote/rollback.
2. **Two-repo GitOps** — app repo CI pushes digest; env repo holds manifests; second pipeline/Argo applies to GKE.

**ADR-D01:** Northstar v1 uses Cloud Build → Artifact Registry → Cloud Deploy to **Cloud Run** (free-tier friendly). GKE GitOps is Part 9. Argo CD is taught; not required live.

#### D3.2 Skaffold
- Dev/CI/CD parity: `skaffold dev` locally, Cloud Build/Cloud Deploy call `skaffold render` / `apply`.
- `skaffold.yaml`: manifests (raw YAML / Helm / kustomize), deploy.cloudrun vs deploy.kubectl.
- Profiles per environment.
- Version pinning: Cloud Deploy supports specific Skaffold versions on a 12-month window — pin it.

#### D3.3 Cloud Deploy (GCP-native CD)
- Delivery pipeline + **targets** (GKE cluster, Cloud Run service/job/worker pool, custom).
- Release = a digest + rendered manifests. Promote through stages (dev → staging → prod).
- Strategies: standard vs **canary** (percentages, verify jobs, pre/post deploy). Cloud Run canary uses traffic splits; GKE canary uses Service/Gateway or pod counts.
- Parallel deploy (multi-region Cloud Run / multi-cluster).
- Rollback is a first-class action, not “redeploy old tag.”
- First active pipeline per billing account is free; extra pipelines bill — destroy labs.
- **Lab:** Cloud Deploy pipeline with two Cloud Run targets (dev project service, prod-shaped service). Create release from Cloud Build. Promote. Rollback. Python/Go apps are the same image digest.

#### D3.4 Manifest management
- Raw YAML for v0.
- **kustomize:** bases + overlays (Google’s modern CI/CD with GKE uses this). Platform team owns base; app team owns overlay.
- **Helm:** charts, values, when the org already standardized on it. Templating vs kustomize overlay — both taught; pick one per service.
- Kustomize is the default for Northstar GKE.

#### D3.5 GitOps in depth
- Desired state in Git. Cluster reconciles. Drift is an event.
- App repo vs env repo (Google tutorial). Promotion = PR that changes a digest in env repo.
- Argo CD: UI, Application CR, sync waves, SSO via Cloud Identity/IAP, HA install. Pull model.
- Flux: Kustomize-controller + HelmRelease, no first-class UI.
- Cloud Deploy is **push** from Google; Argo/Flux are **pull** in-cluster. Multi-cloud → Argo/Flux. GCP-only progressive delivery → Cloud Deploy.
- Never `kubectl apply` in prod except break-glass, logged.

**Python / Go:** a small tool that, given a new digest, opens/updates the env-repo kustomization (the “CI writes digest” step).

---

### D4 Progressive delivery

- Recreate (downtime) — only jobs.
- Rolling (default Deployment / Cloud Run gradual).
- Blue-green (two stacks, flip). Instant rollback. Cost of double capacity.
- Canary (1% → 10% → 50% → 100%) with **automated verify** (Cloud Deploy verify job, Cloud Monitoring SLO, or Argo Rollouts analysis).
- Shadow / dark launch (concept).
- Cloud Run traffic tags (`--tag`) + traffic split without Cloud Deploy — you already used this in 1.6; here it becomes a pipeline.
- Feature flags vs deploy (separate axes). Flags are not a substitute for canary.

**HLD:** Northstar checkout canary 5% for 15 minutes; auto-rollback on 5xx burn.

---

### D5 Software supply chain

PCA 3.1 “securing software supply chain.” This is not optional color.

- Threats: compromised CI, malicious dep, unsigned image, tag mutability, stolen deploy SA.
- **SLSA** levels: provenance exists (1) → hosted, isolated build (2) → unforgeable provenance from trusted builder (3). Cloud Build is the trusted builder Binary Authorization’s SLSA check accepts.
- **SBOM** (Syft/gcloud) attached to the image.
- **cosign** sign/verify (keyless via OIDC or KMS). Artifact Registry + signatures.
- **Artifact Analysis:** notes/occurrences; vulnerability + attestation storage.
- **Binary Authorization:**
  - Policy: require attestations, deny `:latest`, allowlist, dry-run vs enforce.
  - Attestors + KMS keys.
  - GKE and Cloud Run.
  - **Continuous validation** after deploy (policy drift).
  - SLSA check: `trustedBuilder: GOOGLE_CLOUD_BUILD`, trusted source repo patterns.
- Separation of duties: builder project ≠ deploy project ≠ attestor project (Google multi-project tutorial).
- **Lab (local + policy YAML required):** write a BinAuthz policy that would reject an unsigned image. Credits-optional: enforce on a Cloud Run service.
- **Python / Go:** verify a dummy attestation payload; fail the pipeline if missing.

---

### D6 Platform engineering and developer experience

- Golden path: `cookiecutter` / template repo with Dockerfile, cloudbuild.yaml, skaffold, Terraform module, CODEOWNERS.
- Preview environments (ephemeral Cloud Run tagged revision per PR). Destroy on merge.
- Policy as code: OPA/Gatekeeper, Kyverno, Organization Policy, Binary Authorization — layered.
- Self-service: developers do not file a ticket to get a Cloud Run service.
- **Exercise:** write the Northstar service template README a new hire follows to production in one PR.

---

### D7 IaC in the pipeline (ties to Terraform)

- Plan on PR, apply on merge to `infra` repo. Never apply from a laptop to prod.
- State: GCS backend + locking. Separate state per env.
- Cloud Build trigger on infra repo. WIF.
- Deployment Manager is legacy (already in 1.8). Config Connector / Infrastructure Manager: GCP-native, optional.
- OpenTofu as Terraform fork — know it exists; this course uses official Terraform Google provider.

**Python / Go:** parse `terraform show -json` and fail if a resource has no `labels.env`.

---

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

- Conceptual → logical → physical. ER diagrams, entities for catalog, cart, order, payment_intent, user, tenant.
- Normalization (1NF–3NF, when to denormalize). Keys, FKs, uniqueness, check constraints.
- Integrity: ACID, isolation levels (read committed vs repeatable read vs serializable), phantom reads.
- Indexing: B-tree, composite, covering, partial; `EXPLAIN ANALYZE`; what Firestore indexes taught you vs SQL.
- Transactions and idempotency (`orders.idempotency_key UNIQUE`).
- Migrations: expand/contract, never destructive in one step. Tools: Alembic (Python), golang-migrate (Go).
- Multi-tenant SQL: `tenant_id` on every table vs schema-per-tenant vs DB-per-tenant. Default: shared schema + RLS (Postgres row-level security).
- OLTP vs OLAP: Cloud SQL/AlloyDB/Spanner vs BigQuery. Do not run analytics scans on the primary.
- Donne Martin: master-replica, failover, federation, sharding — mapped to Cloud SQL HA/replicas, not to hand-rolled MySQL.

**Lab (local, required):** Docker PostgreSQL. You design the Northstar OLTP schema, apply migrations, load seed data, write queries.

**Python exercise:** SQLAlchemy or `psycopg` — create order + line items in one transaction; concurrent stock decrement test (must not oversell). **Go after submit:** `database/sql` + `pgx`, same tests.

**LLD artifacts:** ERD, DDL, index list, isolation choice ADR, migration plan.

### 2.2 GCP relational offerings (decision table)

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
- Document model, indexes, transactions, security rules vs server-only.
- Dual-write period: cart in Firestore, orders in SQL — or SQL-only after 2.3.
- **Python / Go:** repository interface with two implementations (Postgres, Firestore). Tests against the interface.

### 2.5 Cloud Storage (full offering — video block)
- Storage classes: Standard, Nearline, Coldline, Archive; regional vs dual-region vs multi-region.
- Object lifecycle (transition, delete), object versioning, retention, holds, Autoclass.
- Access: IAM vs ACLs (uniform bucket-level access is the default you will use), public prevention, signed URLs, signed policy documents, HMAC (legacy).
- Requester pays, customer-supplied encryption, CMEK.
- Transfer: Storage Transfer Service, Transfer Appliance (concept), `gcloud storage` / `gsutil`.
- **Lab:** product images; lifecycle to Nearline after 30 days; versioning on; signed URL upload.
- **Python / Go:** V4 signed URLs; never public-write.

### 2.7 Spanner and NoSQL map (PCA storage types)
- **Cloud Spanner:** global SQL, TrueTime, interleaved tables, pickers vs SQL, when Cloud SQL HA is not enough.
- **Firestore / Datastore** mode; Realtime Database (Firebase) — when not to use it for Northstar OLTP.
- **Bigtable:** wide-column, row keys, when time-series wins.
- **Memorystore:** Redis/Memcached — cache, not SoR.
- **Filestore:** NFS file; GKE RWX; not object storage.
- **Lab:** Spanner emulator (PCA 5.2 Cloud Emulators) for a two-table schema; no live Spanner required.
- **Python / Go:** same repository interface; Spanner emulator implementation optional.

### 2.6 Config, migrations, jobs
- Cloud Run Jobs for SQL migrations and reports (vs stuffing DDL into a request).
- Cloud Scheduler (3 free jobs) to trigger a job.
- **Python:** Alembic upgrade as a Cloud Run Job (locally invoked if no live SQL). **Go:** golang-migrate job.

---

## Part 3 — Microservices (industry)

SOLID, hexagonal, DDD, gRPC, and the pattern catalog live **here only**. Later parts link back. Do not re-teach them in Part 8.

### 3.0 Software design (before you split)

Northstar is still a modular monolith. You impose structure so the later split is a cut, not a rewrite.

**SOLID (tests fail if you violate):**
| | Rule in this repo |
|---|---|
| S | HTTP handler, `PlaceOrder` use case, and `OrderRepository` are three modules. A PR that mixes them is rejected. |
| O | New PSP = new `PaymentPort` adapter, not another `if provider ==`. |
| L | `InMemoryOrderRepo` substitutes for Postgres in tests with zero use-case edits. |
| I | Small ports: `OrderWriter`, `CatalogReader` — no 40-method god interface. |
| D | `domain/` and `app/` **must not** import `google.cloud`, `psycopg`, FastAPI. CI grep / import-linter. |

**Hexagonal / Clean / Onion:** same dependency rule (inward). Code layout: `domain/`, `app/` (use cases), `ports/`, `adapters/http|grpc|sql|pubsub`. Driving adapters (HTTP/gRPC) vs driven (SQL, Stripe ACL). Catalog listing may stay layered CRUD; **order/payment is hexagonal**.

**DDD tactical:** Order is an aggregate; line items don’t leak; `OrderPlaced` is a domain event; Pub/Sub carries an *integration* event. Stripe/Identity Platform sit behind an anti-corruption layer. Anemic model is an anti-pattern except honest transaction scripts.

**CQRS:** two *queries* before two databases. Event-source checkout only if you can defend audit/replay; default is outbox (3.5).

**Patterns you implement once (50–150 lines + tests), then keep:**
Factory (clients), Adapter (GCP SDK), Decorator/Chain (middleware — Pedagogy §6), Strategy (pricing), State (order machine), Repository, Circuit breaker / Retry / Timeout / Bulkhead (client), Command (use case).

**From scratch:** `PlaceOrder` with in-memory adapter tests, then Postgres adapter. Use case file cannot import the DB driver.

### 3.1 When to split
- Modular monolith is the **default until** independent deploy, scale, failure, data, or team.
- Split on bounded contexts (3.0): catalog, cart, order, payment, notification.
- Strangler fig: extract catalog first, not payment.
- **HLD:** sync user path; async side effects.
- **Pattern catalog (one table, GCP mapping):**

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

### 3.2 Service-to-service + gRPC + protobuf
- Public browser API stays **JSON/HTTP**. Internal: **gRPC/HTTP/2** on Cloud Run.
- Auth: `roles/run.invoker` + ID tokens; service bindings (preview) as direction of travel.
- Timeouts, retries with jitter, circuit breaker — **your client middleware** (3.0 / §6), not a library you don’t read.

**Protobuf from scratch:** encode/decode `{id, name, price_cents}` (varint, wire type 2). Golden test vs `protoc`. Then official runtime. Field numbers never reused.

**HTTP/2 / HOL:** taught in Part 6.1 (not repeated here). gRPC mapping: `POST /package.Service/Method`, `application/grpc`, 5-byte prefix (compressed flag + length) + protobuf. Unary + server-stream in a toy over HTTP/1 first if needed; all four RPC types with `grpcio` / `google.golang.org/grpc`.

**Production gRPC:** interceptors = middleware (auth, log, deadline). Status codes. Health `grpc.health.v1`. Reflection off in prod. REST BFF calls `catalog.v1.CatalogService`. Same `.proto` → Python then Go stubs.

**Lab:** GetProduct gRPC on Cloud Run; BFF REST in front. **Python / Go:** ID-token client + generated stub. N+1 is a fail — batch or stream (Part 8).

### 3.3 API facade
- URL map on LB vs **API Gateway** (OpenAPI, API keys, JWT, quotas; cheap) vs **Apigee** (API-as-product, monetization, hybrid).
- Cloud Endpoints / ESPv2 as sidecar (GKE).
- **ADR-003:** API Gateway or Cloud Run ingress for Northstar; Apigee when APIs are a product.
- **Lab:** OpenAPI spec in front of two Cloud Run services (API Gateway has a free call tier; stay inside it).
- **Python:** generate OpenAPI from FastAPI; contract tests.

### 3.4 Async: Pub/Sub, Eventarc, Tasks
- **From scratch first:** in-memory broker (topic, pull, ack deadline, nack, DLQ after N, at-least-once). Then the same producer/consumer against real Pub/Sub.
- At-least-once. Idempotency keys. Dead letter topics. Ordering vs throughput.
- Eventarc Standard: CloudEvents to Cloud Run.
- Cloud Run **Worker Pools** for pull consumers (2026 model).
- Cloud Tasks for deferred HTTP with delay.
- **Lab:** `order.placed` → Pub/Sub → notification service; poison message → DLQ.
- **Python / Go:** publisher + subscriber with exactly-once *business* effect (idempotency store in Firestore).

### 3.5 Failure design
- Partial failure. Dual-write (`sql.commit()` + `pubsub.publish()`) is forbidden.
- **From scratch:** in-process saga + outbox on SQLite; same tests against SQL + Pub/Sub.
- Saga: choreography default; compensating `ReleaseStock`. Orchestration only if the graph is painful.
- Inbox on the consumer (idempotency). Poison → DLQ → **redrive API** (not a grave).
- **HLD + LLD:** order placement sequence with payment stub, then Stripe in Part 5.

---

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

### 4.2 Customer auth (Identity Platform)
- **From scratch first:** HS256 JWT issue/verify middleware (header.payload.signature, `exp`/`nbf`/`aud`/`iss`); then RS256 with a fetched JWKS. Cookie session signer. Password hash via bcrypt/argon2 library — not homemade.
- JWT verification on Cloud Run (audience, issuer, expiry).
- Multi-tenancy for B2B SaaS.
- Blocking functions, MFA (Identity Platform, not Firebase Auth).
- Session cookies vs bearer tokens.
- **Lab:** email/password + Google sign-in; API rejects unsigned/wrong-aud tokens.
- **Python:** `google.oauth2.id_token` verify; FastAPI dependency. **Go:** `idtoken.Validate`.

### 4.3 Authorization
- IAM for GCP. App RBAC/ABAC in Firestore (`owner`, `admin`, `member`).
- IAP for admin UI (internal) vs Identity Platform for customers.
- Context-aware access (concept).
- **Python / Go:** middleware: authenticate JWT → load principal → authorize action on resource.

### 4.4 Workload auth
- Attached SA, impersonation, WIF for GitHub.
- Org policy `iam.disableServiceAccountKeyCreation` (default on orgs created after 2024-05-23).
- **Lab:** GitHub Actions → WIF → deploy. Prove no JSON key exists.

### 4.5 API abuse
- reCAPTCHA Enterprise (10k/month), rate limits at gateway, App Check for mobile later.
- **Python:** verify reCAPTCHA on signup.

---

## Part 5 — Payments and money movement

**Goal:** Production-shaped checkout that is **PCI-sane**. You will not store PAN.

### 5.1 PCI as architecture
- CDE, SAQ A vs A-EP vs D.
- Google is PCI DSS Level 1 **infrastructure**. You still own the app.
- Scope reduction: tokenization, no PAN on your servers, dedicated project/VPC if you ever handle cards.
- **ADR-004:** Stripe Checkout or Elements (hosted/iframe). Northstar is SAQ A. Server never sees card numbers.

### 5.2 Stripe on GCP (the real integration)
- Checkout Session from Cloud Run.
- Webhook endpoint: raw body, `Stripe-Signature`, idempotency, replay window.
- Map Stripe events → Pub/Sub → order service.
- Secret Manager for `STRIPE_SECRET_KEY` / webhook secret.
- Test clocks, test cards, failure injection (card_declined).
- **Lab:** end-to-end test-mode payment; order becomes `paid` only after verified webhook, not after redirect.
- **Python:** FastAPI webhook with signature verify + idempotency key in Firestore. **Go:** official Stripe Go SDK, same tests.

### 5.3 Ledger and consistency
- Your DB is not Stripe. Source of truth for money is the PSP; you store tokens, PaymentIntent IDs, amounts, currency, status.
- Refunds, disputes, idempotent retry.
- **HLD:** payment orchestrator service; no other service talks to Stripe.
- **LLD:** state machine `created → requires_action → paid → fulfilled | refunded | failed`.

### 5.4 What we do *not* build (and why)
- Homegrown card forms posting PAN to Cloud Run = SAQ D. Forbidden in this course.
- Storing PAN in Firestore “encrypted” is still in-scope. Forbidden.

---

## Part 6 — Networking services (full video block) then network security

**Goal:** You can design, draw, and (within free-tier) implement VPC, IPs, firewalls, DNS, NAT, peering, and Shared VPC — then place security controls on that network.

### 6.1 Networking refresher + HTTP/2 + QUIC (from scratch)
- OSI vs TCP/IP. Ethernet, IP, TCP, UDP, ICMP, TLS (stdlib only — no homemade crypto).
- MAC vs IP vs port. ARP. Default gateway.
- Subnets, CIDR, public vs RFC1918, NAT, routes, DNS.
- Stateful firewalls, implicit deny. East-west vs north-south.

**HTTP/2 subset (why gRPC is multiplexed):**
- One TCP+TLS connection, many streams, binary frames. Toy frames: SETTINGS, DATA, uncompressed HEADERS (not full HPACK Huffman), RST_STREAM.
- **HOL demo (required):** two streams on one TCP socket; drop a byte on stream 1; prove stream 2 stalls. This is TCP HOL. It is why QUIC exists.

**QUIC / HTTP/3 (ideas, then library):**
- UDP, connection IDs (survive NAT/IP change), independent stream buffers, 1-RTT with TLS 1.3 integrated, 0-RTT replay-unsafe (never checkout).
- **From scratch:** UDP echo; mini-QUIC mux (conn ID + two stream buffers); inject loss on stream 1; **prove stream 2 continues**. Contrast with the HTTP/2 HOL demo. Do **not** implement packet protection.
- Then `aioquic` / `quic-go` HTTP/3 echo. QPACK is “headers without HOL” — do not implement.
- **GCP:** GFE / Cloud CDN speak HTTP/3 to browsers. Cloud Run origin remains HTTP/1.1 or HTTP/2. You do not terminate QUIC yourself. Internal Northstar stays gRPC/HTTP/2 unless you measure HOL on a lossy path.

gRPC service implementation stays in **Part 3.2**. This section is transport only.

### 6.2 VPC, subnets, routing, Private Google Access
- VPC is global; subnets are regional. Auto vs custom mode (**custom in prod**; delete default network).
- Primary and secondary ranges (GKE alias IPs).
- Routes: system-generated, custom static, dynamic (Cloud Router / BGP).
- Private Google Access (subnet flag) vs Private Google Access for on-prem vs PSC.
- Direct VPC egress from Cloud Run vs Serverless VPC Access (legacy).
- **Lab:** custom VPC, two subnets in two regions, no default network.

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

#### Decision table (PCA)
| Need | Address type |
|---|---|
| VM that can die and come back on the same private IP | Regional **internal static** |
| Partner allowlists your egress | Cloud NAT **static** regional external |
| Public website, one IP worldwide | **Global external static** on HTTPS LB |
| Throwaway sandbox VM | Ephemeral internal, **no** external |
| Cloud Run / GAE | You do not assign; platform does. Custom domain → Hosting or LB IP |

### 6.4 Firewall and firewall rules
- Implied allow-egress / deny-ingress.
- Priority, direction, protocol/port, source/destination, tags vs SA targets (prefer SA).
- Hierarchical firewall policy vs VPC rules vs Cloud NGFW (deep in 6.8).
- **Lab:** allow IAP SSH (`35.235.240.0/20`) and health checks; deny the rest.

### 6.5 Custom VPC labs PART 1–2
- End-to-end: VPC, two subnets, firewall, one e2-micro, IAP SSH, Cloud NAT for egress, no public IP.
- **Python / Go:** `gcloud`/`google-cloud-compute` create/destroy the sandbox from a script (idempotent).

### 6.6 VPC Network Peering
- Non-transitive. CIDR cannot overlap. Routes exchanged. Who pays egress.
- When peering loses to Shared VPC or PSC.
- **Lab:** two projects (or two VPCs) peered; verify `traceroute`/connectivity; then destroy.

### 6.7 Shared VPC
- Host project vs service projects. Landing zone pattern. Who owns subnets/firewalls.
- **HLD:** Northstar org: host `shared-net`, service `prod-app`. No live org required; Terraform + diagram required.

### 6.8 VPC Flow Logs
- Enable, sampling, metadata; sink to Logging/BigQuery (BigQuery 1 TiB free queries).
- Use for incident response and denied-traffic debug.
- **Python / Go:** parse a sample flow log; count top talkers and denies.

### 6.9 NAT PART 1–2
- Why Cloud NAT exists (no public IP on VMs). Cloud NAT vs instance-level NAT vs Cloud Router.
- NAT IPs, logging, error `NAT allocation failed`.
- **Lab:** Cloud NAT on the custom VPC; VM wget to `https://example.com` without external IP. NAT has cost — destroy after.

### 6.10 DNS fundamentals, record types, Cloud DNS
- Recursive vs authoritative. TTL. A, AAAA, CNAME, MX, TXT, NS, SRV, CAA, PTR.
- Cloud DNS public vs private zones, peering, forwarding, DNSSEC.
- Split horizon.
- **Lab:** private zone for `internal.northstar.dev` A record to internal IP. Cloud DNS is not Always Free — use `/etc/hosts` + diagram if no credits; Terraform still written.

### 6.11 Network security overlay (NGFW, Armor, IAP, VPC-SC, LB TLS)
(Previously 6.3–6.7; keep in full.)
- Cloud NGFW, hierarchical policy, threat intel.
- Load balancing + SSL policies + Cloud Armor + Cloud CDN (credits-optional live).
- IAP, context-aware access.
- Segmentation, PSC, VPC-SC.
- DDoS at GFE.

### 6.12 Firewall and Cloud NGFW (security depth)
GCP offerings:
- **VPC firewall rules** (legacy per-network).
- **Hierarchical firewall policies** (org/folder/project).
- **Global network firewall policy** / **Cloud NGFW** — threat intelligence, geolocation, FQDN, TLS inspection (Enterprise).
- Implied rules (allow egress, deny ingress). Priority math.
- Target tags vs service accounts as targets (prefer SA).
- **Python / Go:** given a rule set + 5-tuple, decide allow/deny (unit tests). Write the equivalent Terraform `google_compute_firewall` / `google_compute_network_firewall_policy`.

### 6.13 Load balancing, TLS, CDN, and the edge
- External vs internal; global vs regional; Application vs Network vs Proxy.
- SSL policies, managed certs, HTTPS redirect.
- Serverless NEGs (Cloud Run, App Engine, Cloud Functions).
- Forwarding rule **must** have an IP: ephemeral or reserved static (see 6.3). Deleting the rule without deleting a reserved IP leaves a billing leak.
- Cloud CDN on that same HTTPS LB (see 1.4): cache modes, keys, signed URLs, invalidation, hit ratio.
- **From scratch:** your L4/L7 proxies from 1.4 sit in front of two local backends; add weighted round-robin and a drain flag (canary). Then map each feature to a GCP LB type.
- **Cloud Armor:** WAF rules, preconfigured OWASP, rate limiting, bot management, Adaptive Protection, named IP lists.
- **Cloud CDN:** cache modes, signed URLs, cache invalidation.
- **reCAPTCHA Enterprise** at the edge.
- **Lab:** Cloud Run auth as the free-tier “edge.” Credits-optional: global HTTPS LB + Armor + CDN in front of Cloud Run.

### 6.14 Zero-trust access
- **IAP** for admin UIs (App Engine, Cloud Run, GKE, GCE via IAP TCP).
- Context-aware access / Chrome Enterprise Premium.
- BeyondCorp: identity + device + request context, not “inside VPC = trusted.”
- **Lab:** IAP on an App Engine or Cloud Run admin service.

### 6.15 Segmentation and exfil controls
- Separate VPCs or subnets for CDE vs general (PCI).
- **VPC Service Controls** perimeters (org).
- PSC to consume services without public IPs.
- **HLD:** Northstar network: public frontend, private API, private Cloud SQL, no VM public IPs.

### 6.16 DNS and DDoS (security view)
- Cloud DNS, DNSSEC, Cloud DNS peering.
- Google’s front-end DDoS + Armor + Cloud Load Balancing.
- **Billing:** forwarding-rule hours, NAT hours, Armor policies — why the free-tier path avoids them.

---

## Part 7 — Cybersecurity (concept + GCP offerings)

**Goal:** Secure software systems, not just a green SCC dashboard. Identity, data, runtime, supply chain, detect, respond.

### 7.1 Security principles
- CIA, least privilege, defense in depth, assume breach, zero trust.
- Shared responsibility on GCP (you: config, IAM, data, app; Google: physical, hypervisor, some managed-service hardening).
- Well-Architected security/privacy/compliance pillar.

### 7.2 Identity and access (GCP offerings)
- Cloud Identity, IAM, Identity Platform, IAP, WIF, Workforce Federation (Part 4 reused, now at org scale).
- Predefined vs custom roles, conditions, deny policies, Privileged Access Manager (if available in org).
- Groups, not users. Break-glass.
- **Python / Go:** Policy Analyzer-style: given a binding dump, compute effective access for a principal on a resource.

### 7.3 Data protection
- Default encryption at rest. CMEK, CSEK, Cloud KMS, Cloud HSM, Cloud EKM.
- Secret Manager vs env vars vs Binary Authorization attestations.
- **Sensitive Data Protection / DLP** — inspect, de-identify, templates.
- GCS uniform access, public-prevention org policy, VPC-SC.
- **Lab:** KMS-encrypt a field; Secret Manager rotation story; DLP inspect a sample order export (API has cost — use sample payloads locally if needed).

### 7.4 Application and API security
- OWASP API Top 10 mapped onto Cloud Run + Identity Platform + SQL.
- Input validation, output encoding, CSRF (cookies), SSRF (metadata server — **disable** default SA on GCE, use `metadata concealment` / no default scopes).
- GCE metadata server attack (`169.254.169.254`) and why Cloud Run’s model is safer.
- **Python / Go:** exploit-and-fix exercises on a deliberately weak local API (open redirect, missing authz, SQL injection against the Part 2 schema). No malware, no scanning third-party systems.

### 7.5 Workload and supply chain
- Artifact Registry vulnerability scanning.
- Binary Authorization, attestations, SLSA.
- Shielded VM, Secure Boot, vTPM.
- Container contract: non-root, read-only FS, dropped caps (where the platform allows).
- **Lab:** scan the Northstar image; fail the build on CRITICAL.

### 7.6 Detection and posture
GCP offerings:
- **Cloud Audit Logs** (admin, data access, system).
- **Security Command Center** (Standard / Premium / Enterprise) — findings, mute rules, attack path.
- **Web Security Scanner**.
- **Cloud IDS**.
- **Google SecOps / Chronicle** (concept; cost).
- **Assured Workloads** (compliance perimeters).
- **Lab:** parse audit logs; alert on `SetIamPolicy` and `serviceAccount.keys.create`. **Python / Go.**

### 7.7 Org policy and landing zone
- `iam.disableServiceAccountKeyCreation`, `compute.vmExternalIpAccess`, resource locations, uniform bucket access.
- Security baseline for orgs created after 2024-05-23.
- Landing zone: identity, hierarchy, network, security — now you have the product to put in it.

### 7.8 Incident response
- Runbooks: leaked GitHub token, leaked Stripe webhook secret, public bucket, compromised SA.
- Revoke, rotate, forensics (logs), customer notification.
- **Exercise:** write both runbooks and a tabletop.

### 7.9 Compliance mapping
- PCI (Part 5), SOC 2, ISO 27001, HIPAA BAA, GDPR data residency (`resourceLocations`).
- Compliance Reports Manager — how to pull Google’s attestations vs your own.

---

## Part 8 — HLD/LLD mastery (Donne Martin → GCP)

Every Donne Martin building block becomes a GCP decision table plus a Northstar ADR.

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

**From-scratch required in this part:** bloom filter + FPR tests; consistent-hash ring; singleflight; load-shed middleware; cursor pager. WAL toy may reuse Pedagogy §6 KV. LSM is a written comparison + optional flush toy.

Worked HLD/LLD studios (Python models + Go after submit where there is code):
1. URL shortener (Pastebin) on Cloud Run + Firestore.
2. News feed / timeline — Pub/Sub fanout.
3. Web crawler — Cloud Run Jobs + GCS.
4. Rate limiter / LRU — Memorystore conceptually; Firestore or in-process for lab.
5. Mint-like transaction aggregator — BigQuery (1 TiB free queries) for analytics path.

Back-of-envelope: powers of two, latency numbers, GCP SKU napkin math (Part 0 skills reused).

PCA-style writing: “Given this constraint, I pick X because Y, and I accept Z.”

---

## Part 8b — Hybrid connectivity (PCA 2.1)

- **Cloud VPN:** HA VPN vs Classic. IKE, BGP, Cloud Router. When VPN is enough.
- **Cloud Interconnect:** Dedicated vs Partner. VLAN attachments. When bandwidth/SLA beats VPN.
- **Network Connectivity Center.** VPC peering vs HA VPN vs Interconnect vs PSC.
- Multi-cloud: VPN to AWS/Azure; Google Cloud to Google Cloud (VPC peering / PSC).
- **Google Cloud VMware Engine** (PCA 2.3) — lift VMware as-is; when not to.
- **HLD:** on-prem DC ↔ HA VPN ↔ Shared VPC host. No live Interconnect (you cannot buy a 10 Gbps circuit in this course).
- **Python / Go:** given latency/bandwidth/SLA constraints, pick VPN vs Interconnect vs peering (decision tests).

## Part 8c — Migration (PCA 1.4)
- Migration Center. Assess, wave plan, dependency mapping.
- 6Rs / Google: rehost (Migrate to VMs), replatform, refactor (GKE/Cloud Run), retire, retain, repurchase.
- License implications (Windows, Oracle, SQL Server).
- **Exercise:** migration plan for a fictional 3-tier on-prem app into Northstar’s GCP landing zone.

---

## Part 9 — Kubernetes internals applied on GKE + mesh + cache

Part D8 is the CKA-level object/scheduling/security model. This part is **GKE as a product** plus running Northstar on it with GitOps.

### 9.0 Introduction to containers
- Image, layer, registry, runtime, PID 1. Docker → containerd. Why Kubernetes exists.

### 9.1 Memorystore
- Redis/Memcached. Cache-aside vs write-through (Donne Martin).
- Local substitute: Docker Redis. Credits-optional Memorystore.
- **Python / Go:** catalog cache in front of Cloud SQL.

### 9.2 GKE and Kubernetes concepts
- Control plane vs nodes. Autopilot vs Standard. Cluster versions, release channels.
- Cluster and node management: node pools, machine types, taints/tolerations, autoscaling (cluster + HPA + VPA).
- Pods, Deployments, ReplicaSets, StatefulSets, DaemonSets, Jobs, CronJobs, ConfigMaps, Secrets.
- Kubernetes Services: ClusterIP, NodePort, LoadBalancer, ExternalName, headless.
- Ingress vs Gateway API. GKE Ingress, HTTP(S) LB, NEG.
- GKE storage: PD CSI, Filestore, GCS FUSE (when not to), StorageClass, PVC/PV.
- Workload Identity Federation for GKE. Binary Authorization. Policy Controller / Gatekeeper. Private cluster, master authorized networks, Cloud NAT.
- [Enterprise-grade production GKE template](https://docs.cloud.google.com/application-design-center/docs/enterprise-grade-production-gke).
- **Local lab (required):** kind/minikube — Deploy, Service, Ingress/Gateway, HPA, PVC, NetworkPolicy, PSA restricted, rolling update + rollback (D8).
- **GitOps lab:** env-repo kustomize overlay; apply via script or Argo-in-kind (kind required; GKE Autopilot credits-optional).
- **Credits-optional:** Autopilot, Cloud Deploy target, canary 10%, destroy same day.
- Exit criteria Cloud Run → GKE: sidecars, custom CNI, stateful operators, GPU/DRA, mesh.

### 9.3 Service mesh
- Cloud Service Mesh / Istio: mTLS, traffic split, retries.
- Teach *when* (many services, heterogeneous runtimes), not as default.

### 9.4 Spanner, AlloyDB, Bigtable, BigQuery (ops view)
- Decision tree already in Part 2. Here: BigQuery lab on order events export (1 TiB free queries).

---

## Part 9b — Vertex AI, Gemini, Big Data (PCA v6.1 §§1.3, 2.4, 2.5)

v6.1 made ML/AI a first-class architect domain. This is not a data-scientist career track; it is **service selection and secure integration**.

### 9b.1 Big Data services
- Pub/Sub (already Part 3) as the bus.
- Dataflow (batch/stream), Dataproc (Hadoop/Spark lift), Dataform, Composer (Airflow).
- BigQuery: datasets, slots vs on-demand, 1 TiB free queries, partitioning/clustering, authorized views.
- BigLake, Dataplex (concept).
- **Lab:** Pub/Sub → BigQuery subscription or batch load of order events; SQL on the warehouse. Python then Go.

### 9b.2 Vertex AI end-to-end (PCA 2.4)
- Vertex AI Pipelines to orchestrate the ML lifecycle.
- Data integration into Vertex.
- AI Hypercomputer: GPUs/TPUs, Cloud Run functions + Vertex for serving, consumption models, large-scale training (concept + SKU awareness).
- **HLD:** Northstar “recommend products” as a Vertex endpoint, not a custom GPU cluster.

### 9b.3 Pre-built AI APIs and Gemini (PCA 2.5)
- Google AI APIs: Search, Conversation, Vision, Image, Video, Audio — when to buy vs build.
- Gemini Enterprise: AI Agents, NotebookLM.
- Model Garden: pick a model, wrap it, don’t train if an API suffices.
- Gemini Cloud Assist (PCA 1.2, 5.1) as an architect copilot — use it, don’t blindly trust it.
- **Securing AI (PCA 3.1):** Model Armor, Sensitive Data Protection, secure model deployment. Prompt injection as a threat.
- **Lab (free-tier boxed):** call a Gemini API from Cloud Run with a Vertex/AI Studio key in Secret Manager; never log prompts that contain PII. Python then Go.

---

## Part 10 — Operations Suite, reliability, FinOps, compliance

Well-Architected pillars, now that you have a system. Operations Suite is the former Stackdriver video block.

### 10.0 Operations Suite (Observability — PCA 6.2)
- Cloud Logging: log buckets, sinks, exclusion, 50 GiB free ingest.
- Cloud Monitoring: metrics, SLOs, uptime checks, dashboards, alerting (channels, policies).
- Cloud Trace, Cloud Profiler, Error Reporting.
- Cloud Audit Logs (admin / data access / system) — already in Part 7; here: operational use.
- Alerting strategies: avoid pager fatigue; SLOs not “CPU > 80%.”
- **Lab:** dashboard for Northstar API (request count, latency, 5xx); alert on error-budget burn. Python/Go: emit a custom metric.

### 10.1 Reliability
- SLI/SLO/SLA, error budgets.
- Regional Cloud Run is multi-zone already. Multi-region: dual Cloud Run + global LB + Firestore multi-region.
- RPO/RTO. Backup Firestore (paid) vs application-level export to GCS.
- Chaos: kill a revision, fail a Pub/Sub push, revoke a secret.

### 10.2 Operational excellence
- DORA metrics. Terraform modules. Environments. Promotion.
- Runbooks. On-call. Postmortems.

### 10.3 Cost optimization (deep billing, returning to Part 0)
- Request-based vs instance-based Cloud Run billing.
- Committed use, CUD, idle Artifact Registry, log ingestion.
- **Python / Go:** cost anomaly detector on a synthetic export.

### 10.4 Performance
- Concurrency tuning, connection pooling to Firestore, CDN cache hit ratio, payload size.

### 10.5 Sustainability
- Region carbon, scale-to-zero as a sustainability feature (pillar added Jan 2026).

### 10.6 Linux / OS internals (earned, after GCE + Cloud Run)
- Namespaces, cgroups (what Cloud Run abstracts; what you still see on GCE).
- Why the container contract exists.
- TCP handshake, TLS handshake, HTTP/2, gRPC — packet path you already drew in Part 6.
- iptables vs VPC firewall vs Cloud NGFW vs Cloud Armor.
- This is the original Linux/OS request, attached to VMs and containers you already operate.

---

## Part 11 — Capstone and PCA

### Capstone: Northstar v1 (must run on free tier)
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

Deliverables: HLD deck, LLD pack (OpenAPI + `.proto`, ERD/DDL, sequences, firewall policy, IAM, hexagonal layout), Python services, Go ports of at least **two** services, GCE e2-micro and App Engine labs documented (can be torn down), lab teardown.

### PCA alignment (v6.1)
Not a dump of dumps. After capstone:
- Map every ADR to an exam domain.
- Four official case studies: Altostrat Media, Cymbal Retail, EHR Healthcare, KnightMotives Automotive — full HLD per case.
- Practice the exam skill: pick the *Google-preferred managed* option unless a constraint forbids it.
- Optional: sit ACE first if IAM/gcloud is still shaky; PCA is the target.

---

## Exercise engine (how teaching will actually work)

For each numbered subtopic when teaching starts:

```
1. Concept (short, sourced)
2. FROM-SCRATCH.md — stdlib server / middleware / parser / state machine
   → you submit Python; then Go
3. HLD prompt (you write; reviewed)
4. LLD prompt (you write; reviewed)
5. Lab steps (gcloud/Terraform, free-tier boxed)
6. PYTHON-EXERCISE.md  — GCP-wired version, tests included
   → you submit
7. GOLANG-EXERCISE.md  — same tests, same behavior
   → you submit
8. Review notes: what the toy got wrong vs the managed product
```

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

Each has a Go twin after submission.

---

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
- Donne Martin `system-design-primer` (topics index + Pastebin/Twitter/crawler/Mint/scaling solutions).
- Donne Martin `interactive-coding-challenges` used only as the style model for exercise notebooks — GCP exercises are original.
- Cloud CDN overview, cache modes, best practices; Compute Engine / VPC IP address docs (ephemeral vs static, regional vs global).
- RFC 9111 (HTTP caching), RFC 7519 (JWT), protobuf encoding, RFC 9000 (QUIC concepts only) as from-scratch specs.
- Bloom filters; consistent hashing; DDD/hexagonal as used in Northstar, not as a second course.

---

## What this course will not do

- Will not start with a month of isolated Linux before any GCP.
- Will not skip Compute Engine, App Engine, SQL design, Cloud SQL setup, network security, cybersecurity, Docker, Kubernetes internals, CI/CD, GitOps, or supply-chain security — they are first-class.
- Will not require a **live** Cloud SQL instance, GKE cluster, or global load balancer to complete required labs (Terraform + local Postgres + free-tier GCE/GAE/Cloud Run are required).
- Will not teach storing card data.
- Will not treat PCA dumps as architecture education.
- Will not skip Go; it is sequenced after each Python submit, not as a separate language semester.
- Will not skip from-scratch implementations (servers, proxies, middleware, bloom filters, gRPC toys, mini-QUIC). Managed GCP is the second step, not the first.
- Will not duplicate SOLID/gRPC/QUIC in extra parts — one home each (3.0, 3.2, 6.1).
- Will not have you implement TLS/AES/RSA, store PAN, or attack systems you do not own.

---

## PCA v6.1 coverage matrix (every official bullet has a home)

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

Case studies (required reading before Part 11): Altostrat Media, Cymbal Retail, EHR Healthcare, KnightMotives Automotive.

---

## How we run it

1. This file is the curriculum: `~/gcp-curriculum.md`.
2. Teaching starts at **F** (skip-test if you are already a software engineer) then **0.1 Billing** — when you say start.
3. One subtopic at a time. You submit Python. Then Go. Then next subtopic.
4. Northstar repo lives in your workspace; each part is a PR-quality increment.

No teaching content is delivered until you say start.
