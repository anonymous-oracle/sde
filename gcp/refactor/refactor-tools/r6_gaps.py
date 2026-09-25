"""R6 Gap fills from the learn-anything.xyz cross-check (learner request, 2026-09-25).

The learner asked for the course to be cross-checked against learn-anything.xyz and for the gaps found to be added
"properly". The check (14 topic pages against all six parts) found four gaps. Three are taught in text that has an
authored source and need no rule here:
  - progress conditions and ABA: main course A6.D4 and GOT.5 (authored/academic/main-course.md, go.md), GO-18
    (authored/go-language-companion.md); problem GOT-P10
  - closed sum types through sealed interfaces: GOT.2 and GO-11; problem GOT-P9
  - checking a history for linearizability: main course A9.D9; problem A9-P10
The fourth, PostgreSQL LISTEN/NOTIFY, is taught in SQL SL-10, whose text comes from the frozen R2 snapshot, so this
module edits it through journaled replacements (every replaced line goes to records/, D3). Its academic side is
DBT.9 and DBT-P15 (authored/academic/sql.md, sql-keys.md).
R6-2 (same day) swaps the reference: the learner asked for College Compendium (collegecompendium.org, a catalogue of
university CS courses) and roadmap.sh (the topic trees of the backend, system-design, Go, SQL, PostgreSQL DBA,
Kubernetes, DevOps, Terraform, API-design, software-architecture and cyber-security roadmaps, read from
github.com/nilbuild/developer-roadmap) to be used as topic references, not as lists to paste. Every roadmap topic was
searched for in all six parts; vendor products, certifications and consumer-security items were ruled out of scope, and
each remaining gap was taught in the one module that owns it. Authored additions (no rule here): A4.D6 skip lists and
Rabin–Karp, A7.D4 architectural styles, A7.D5 content negotiation and API contracts, CRA.12 Kerberos and authorization
models, GO-24 Delve and GOTRACEBACK, GO-25 golangci-lint, and the Compendium's courses in the §0.6 table.
"""
from r2b_common import CUR, SQL, DPC, SEC

EV = ("R6 (2026-09-25): the learner asked that gaps found by cross-checking the course against learn-anything.xyz be "
      "added properly; PostgreSQL LISTEN/NOTIFY was taught nowhere, and SL-10 owns the queue and outbox SQL it pairs with.")


def sql(f):
    f.rep("R6-1", "new-content",
          "- **Core:** `INSERT…ON CONFLICT`, `UPDATE…FROM`, writable CTEs, `MERGE` (PG15+), `DELETE…RETURNING`.",
          "- **Core:** `INSERT…ON CONFLICT`, `UPDATE…FROM`, writable CTEs, `MERGE` (PG15+), `DELETE…RETURNING`. "
          "`LISTEN channel` / `NOTIFY channel, 'payload'` (or `pg_notify(channel, payload)`) as the wake-up beside a "
          "`FOR UPDATE SKIP LOCKED` queue table or an outbox: the notification is sent when the transaction commits, "
          "and never if it rolls back.", EV)
    f.rep("R6-1", "new-content", "- **Theory:** Idempotency keys; batching to bound WAL/bloat.",
          "- **Theory:** Idempotency keys; batching to bound WAL/bloat. A notification is a hint, not a message: "
          "it reaches only sessions listening at commit time and is never stored, so a worker drains the table after "
          "every wake-up and every reconnect (DBT.9, DBT-P15). A listener needs its own long-lived session, so it "
          "cannot sit behind a transaction-mode connection pooler.", EV)
    f.rep("R6-1", "anchor-rewrite", "SL-10 idempotent writes: `INSERT … ON CONFLICT`, unique keys",
          "SL-10 idempotent writes: `INSERT … ON CONFLICT`, unique keys; `LISTEN`/`NOTIFY` as the worker wake-up", EV)

EV2 = ("R6-2 (2026-09-25): the learner asked that College Compendium and roadmap.sh be used as topic references for the "
       "course; each topic here appears on a roadmap.sh roadmap (backend, PostgreSQL DBA, Kubernetes, Terraform, API "
       "design, software architecture, cyber security) and was taught nowhere in the six parts, so it goes into the "
       "module that owns the subject rather than into a new list.")


def sql2(f):
    f.rep("R6-2", "new-content", "`DELETE…RETURNING`. `LISTEN channel`",
          "`DELETE…RETURNING`. `SAVEPOINT name` / `ROLLBACK TO SAVEPOINT name` / `RELEASE SAVEPOINT name` undo part of a "
          "transaction without abandoning it (one failed row in a batch, retried or skipped); in PostgreSQL any error "
          "aborts the whole transaction until you roll back to a savepoint (psql's `\\set ON_ERROR_ROLLBACK on` sets an "
          "implicit savepoint before each statement to do exactly that). `LISTEN channel`", EV2)
    f.rep("R6-2", "new-content", "- **Core:** `pg_stat_statements`, auto_explain, wait events; stale analyze symptoms.",
          "- **Core:** `pg_stat_statements`, auto_explain, wait events; stale analyze symptoms. Live triage from "
          "`pg_stat_activity` (state, `wait_event_type`, `xact_start`, `query`): an `idle in transaction` session holds "
          "its locks and its snapshot, so it blocks DDL and stops vacuum; `pg_blocking_pids(pid)` names who blocks whom; "
          "`pg_cancel_backend` stops a query and `pg_terminate_backend` ends the session; `lock_timeout`, "
          "`statement_timeout` and `idle_in_transaction_session_timeout` bound all three.", EV2)
    f.rep("R6-2", "new-content", "- **Core:** Runbook literacy: schedule, retain, test restore to a *new* instance, measure RPO/RTO.",
          "- **Core:** Runbook literacy: schedule, retain, test restore to a *new* instance, measure RPO/RTO. Logical "
          "backup (`pg_dump -Fc` / `pg_restore`, one database, portable across major versions, restores to the moment "
          "of the dump) versus physical backup with continuous WAL archiving (`pg_basebackup` plus archived WAL, the "
          "whole cluster, point-in-time recovery to any moment covered by the archive); the second is what managed "
          "services such as Cloud SQL run for you.", EV2)
    f.rep("R6-2", "new-content", "- **Core:** Physical vs logical replication; failover;",
          "- **Core:** Physical vs logical replication (a publication on the source, a subscription on the target, row "
          "changes decoded from the WAL, across major versions); change data capture as the same logical decoding read "
          "by another system (Debezium, Datastream) through a replication slot, which keeps WAL on the primary until "
          "the consumer confirms it, so a dead consumer fills the disk; CDC is the log-based alternative to the "
          "outbox's polling reader; failover;", EV2)
    f.rep("R6-2", "new-content", "BRIN for append-mostly.",
          "BRIN for append-mostly. An LSM memtable is usually a skip list (A4.D6): ordered, cheap concurrent inserts, "
          "flushed in key order as an SSTable.", EV2)


def cur2(f):
    f.rep("R6-2", "new-content",
          "Scheduling & scaling: node affinity/taints/tolerations, Horizontal Pod Autoscaler, Vertical Pod Autoscaler, Cluster Autoscaler",
          "Scheduling & scaling: node affinity/taints/tolerations, pod anti-affinity and topology spread constraints "
          "(replicas across zones and nodes), Horizontal Pod Autoscaler, Vertical Pod Autoscaler, Cluster Autoscaler; "
          "PodDisruptionBudgets, so a node drain or cluster upgrade never evicts more replicas than the service can "
          "lose", EV2)
    f.rep("R6-2", "new-content", "Operators and the Operator pattern (brief — enough for exam recognition)",
          "Operators and the Operator pattern (brief — enough for exam recognition): a CustomResourceDefinition adds "
          "a new resource type to the API server, and the Operator is the controller that reconciles it, the same "
          "control loop as a Deployment's", EV2)
    f.rep("R6-2", "new-content", "providers, resources, modules, plan/apply/destroy, remote state, workspaces — ",
          "providers, resources, modules, plan/apply/destroy, remote state, workspaces, `count` and `for_each`, "
          "implicit dependencies through references and `depends_on` when there is none, static IaC scanning "
          "(Checkov, tfsec/Trivy) in the pipeline before `plan` — ", EV2)
    f.rep("R6-2", "new-content", "REST principles, gRPC, GraphQL (awareness-level)",
          "REST principles, gRPC, GraphQL (awareness-level); the API gateway's offloaded concerns (TLS, "
          "authentication, rate limiting, request routing) and the Backend for Frontend, one thin API per client type "
          "(web, mobile) over the same services", EV2)


def dpc2(f):
    f.rep("R6-2", "new-content", "different things in different contexts, deliberately.",
          "different things in different contexts, deliberately. An **Anti-Corruption Layer** sits where one context "
          "consumes another's (or a legacy system's) model: it translates their terms into ours, so their model never "
          "leaks into our domain; it is DP-06 (Adapter) and DP-07 (Facade) applied at a context boundary, and the usual "
          "companion of ARCH-12's Strangler Fig.", EV2)
    f.rep("R6-2", "new-content", "- **PR-09 Low Coupling:** minimize how many other classes a class depends on.",
          "- **PR-09 Low Coupling:** minimize how many other classes a class depends on. The **Law of Demeter** "
          "(Lieberherr and Holland, 1989) is its method-level rule: talk only to your own fields, your parameters and "
          "objects you create, so `order.customer().address().city()` becomes a question `order` answers; "
          "**Tell, Don't Ask** is the same idea stated as behaviour: tell an object to act instead of pulling its state "
          "out to decide for it.", EV2)
    f.rep("R6-2", "new-content",
          "**Bulkhead:** isolate resources per downstream dependency so one failing dependency can't exhaust resources needed elsewhere.",
          "**Bulkhead:** isolate resources per downstream dependency so one failing dependency can't exhaust resources "
          "needed elsewhere. **Graceful degradation:** when a dependency is down or the breaker is open, serve a "
          "reduced answer (cached, default, or the feature switched off) instead of an error, decided per feature in "
          "advance; paired with **retry with exponential backoff and jitter**, only for idempotent calls and bounded "
          "by a retry budget so retries do not multiply the overload.", EV2)
    f.rep("R6-2", "new-content",
          "- **AP-07 Premature Optimization:** applying a pattern (often Flyweight) for a performance problem that doesn't yet exist.",
          "- **AP-07 Premature Optimization:** applying a pattern (often Flyweight) for a performance problem that "
          "doesn't yet exist. Its design-level siblings are named by two slogans: **YAGNI** (\"you aren't gonna need "
          "it\", from Extreme Programming) against building for requirements nobody has asked for, and **KISS** for "
          "the simplest design that passes the tests.", EV2)
    f.rep("R6-2", "new-content",
          "- **AP-09 Shotgun Surgery:** one logical change requires editing many unrelated classes — the mirror image of SRP done right.",
          "- **AP-09 Shotgun Surgery:** one logical change requires editing many unrelated classes — the mirror image "
          "of SRP done right. **DRY** (Hunt and Thomas, *The Pragmatic Programmer*, 1999) is the cure stated as a "
          "rule: every piece of *knowledge* has one authoritative representation; two identical-looking lines that "
          "encode different rules are not duplication, and merging them couples what should change apart (the rule "
          "of three: abstract on the third repetition, not the second).", EV2)


def sec2(f):
    f.rep("R6-2", "new-content", "DNSSEC for authenticity; delete DNS with services;",
          "DNSSEC for authenticity; SPF, DKIM and DMARC (TXT records) so mail claiming the domain must come from listed "
          "servers or carry the domain's signature, with DMARC `p=reject` telling receivers to drop the rest (an "
          "unprotected domain is free to spoof in phishing); delete DNS with services;", EV2)
    f.rep("R6-2", "new-content", "Detect key create, anomalous IAM,",
          "Detect key create, anomalous IAM, any use of a honeytoken (a decoy service-account key or credential planted "
          "where an attacker looks, never used legitimately, so one use is a near-certain alert),", EV2)


def build(files):
    sql(files[SQL])
    sql2(files[SQL])
    cur2(files[CUR])
    dpc2(files[DPC])
    sec2(files[SEC])
