"""R2b per-file rules for the SQL & Databases companion. Learner decisions D5, D6, D7, D9, D10, D11.

Three kinds of change:
  1. pointers: file names, the file-style parent name, Northstar and N-section pointers, refactor bookkeeping;
  2. gap content (D9): the material the N-pointers named, written into the module that owns it (one home, D7):
     OD-11 Cloud SQL (new), OD-08 migrations as jobs, OD-09 cursor pager, OD-03 pool worksheet, DD-03 ledger rules,
     DD-05 leakage, DD-09 tenant RLS design, DD-13 key histogram, CS-02 LSM-vs-B-tree, AN-02 BigQuery operations,
     AN-06 Firestore rules; the store-choice map stays in the primer (SD-22, SD-23, SD-25);
  3. the lab kit (D6): every kit file is printed in full in §3.8, verbatim, under its own name.
Facts for (2) come from the learner's legacy course, used only as a content reference (D10).
"""
import json
import os

from r2b_shared import contract_copy, parent_name

EV6 = "D6: no file names, links or file dependencies in course text"
EV5 = "D5: Northstar and every N pointer are deleted; the pointer now names the part that holds the material"
EV9 = "D9: the material the N-pointer named is written into its owning module (one home, D7)"
EV11 = "D11: the file-style parent name becomes 'the main course'; IDs stay as stitch tags"

KIT = ["lab_schema.sql", "lab_seed.sql", "run_ex.py", "ex_l1_4.py", "ex_l5_8.py", "ex_l9_13.py", "ex_l14.py",
       "plans.py", "tx_tests.py", "two.py", "wrongs.py", "naive.sql", "safe.sql", "slow_bad.sql",
       "slow_bad_idx.sql", "slow_good.sql", "goldens_ex_l1_4.json", "goldens_ex_l5_8.json",
       "goldens_ex_l9_13.json", "goldens_ex_l14.json", "goldens_wrong.json"]
LANG = {"sql": "sql", "py": "python", "json": "json"}
KIT_ROLE = {
    "lab_schema.sql": "schemas `lab` and `work`, every table and constraint, and the fingerprint functions",
    "lab_seed.sql": "the deterministic seed v1 (no `random()`), ending in `ANALYZE`",
    "run_ex.py": "runs exercise keys inside `BEGIN…ROLLBACK` and writes the goldens file for the chosen levels",
    "ex_l1_4.py": "exercise keys, levels 1–4", "ex_l5_8.py": "exercise keys, levels 5–8",
    "ex_l9_13.py": "exercise keys, levels 9–13", "ex_l14.py": "exercise keys, level 14 (capstones)",
    "plans.py": "the PX plan catalogue (PX-1…PX-11)", "tx_tests.py": "the TX scenarios, run in two sessions",
    "two.py": "the two-session psql driver used by the TX scenarios", "wrongs.py": "canonical wrong queries (trap fingerprints)",
    "naive.sql": "check-then-act oversell (application read-modify-write)", "safe.sql": "single-statement atomic claim",
    "slow_bad.sql": "SQL-CAP4 baseline", "slow_bad_idx.sql": "SQL-CAP4 baseline with an index-assisted path",
    "slow_good.sql": "SQL-CAP4 rewrite", "goldens_ex_l1_4.json": "goldens, levels 1–4",
    "goldens_ex_l5_8.json": "goldens, levels 5–8", "goldens_ex_l9_13.json": "goldens, levels 9–13",
    "goldens_ex_l14.json": "goldens, level 14", "goldens_wrong.json": "wrong-path fingerprints",
}

OD11 = [
    "#### OD-11 · Cloud SQL: provisioning, connectivity, security, operations — stitch: V-STOR · B5 · B3 · C5",
    "- [ ] done",
    "- **Core (provisioning):** engine and major version; region and zone; machine tier (the smallest shared-core "
    "tier is the cheapest credits demo and is not HA `(verify)`); SSD vs HDD storage and automatic storage increase; "
    "automated backups, point-in-time recovery and the retained-backup count; maintenance window; database flags "
    "(`max_connections`, `work_mem`); deletion protection. **HA (regional):** a primary and a standby in a second "
    "zone; failover moves the instance to the standby; cost ≈ 2×. Read replicas are separate and asynchronous "
    "(OD-05).",
    "- **Core (connectivity — the part people get wrong):** public IP with authorized networks is rejected for "
    "production. Use **private IP** in a VPC through private services access, reached from Cloud Run through "
    "Direct VPC egress (or the older Serverless VPC Access connector) and from GCE or GKE directly. The **Cloud SQL "
    "Auth Proxy** or a **language connector** (Python, Go, Java) wraps the connection in TLS and authorises it with "
    "IAM, so no database password has to sit in an environment variable. **IAM database authentication** makes IAM "
    "principals database users (SL-13 grants their privileges); built-in users remain for tools that cannot use "
    "IAM. Require TLS (`sslmode=require` or `verify-ca`).",
    "- **Core (security):** one dedicated service account per workload; Secret Manager for any built-in password; "
    "authorized networks empty — never `0.0.0.0/0`; CMEK optional (cyber CR-14 owns the key hierarchy); Cloud SQL "
    "Admin audit logs for control-plane actions plus `pgAudit` for statement auditing.",
    "- **Core (operations):** import and export through Cloud Storage (PQ-04 formats); the major-version upgrade "
    "path; Query Insights and the slow-query log (OD-02); connection pooling with an application pool or PgBouncer, "
    "sized with the OD-03 worksheet (Cloud Run max instances × pool size per instance against `max_connections`).",
    "- **Theory:** RPO and RTO arithmetic for automated backups vs PITR vs HA (OD-04). HA is not a backup and a "
    "replica is not a backup: both copy a bad `DELETE` within seconds.",
    "- **GCP lens:** Lens-1: `gcloud sql instances create` with no public IP and a VPC network `(verify flags)`. "
    "Lens-2: the labs below. Lens-3: Cloud SQL editions, and the exits to AlloyDB or Spanner (primer SD-25).",
    "- **Lab `[local]` (required):** simulate the connector flow. The application reads only an instance connection "
    "name and asks one small factory function for a connection; in the lab the factory returns a connection to the "
    "Docker Postgres of §3, in production it calls the Cloud SQL connector with IAM authentication. The application "
    "code does not change between the two. Then fill the OD-03 worksheet for the check below.",
    "- **Lab `[credit ~$X]` (optional; destroy the same day):** with Terraform (TF-DB1), a PostgreSQL instance on "
    "private IP; connect from a Cloud Run service or an e2-micro VM through the connector with IAM database "
    "authentication; run the OD-08 migration job; take an on-demand backup; if the instance is HA, trigger a "
    "failover and time it; `terraform destroy`.",
    "- **Terraform LLD (deliverable):** `google_sql_database_instance` (private IP, deletion protection, backup "
    "configuration, insights configuration), `google_sql_database`, `google_sql_user` (IAM type), and "
    "`google_service_networking_connection` for private services access. TF-DB1 (§8.2) is the exercise; primer TF-2 "
    "draws the same private-IP pattern at system level.",
    "- **Check:** A Cloud Run service with max 20 instances and a pool of 10 connections per instance points at an "
    "instance with `max_connections = 100`. What fails first as traffic grows, and name two fixes.",
]

OD08_THEORY = [
    "- **Theory:** Migrations and backfills are **jobs**: never part of a user request, never run on every container "
    "start. A **Cloud Run Job** (run to completion, one service account, bounded retries, a task timeout) runs "
    "`migrate up`; **Cloud Scheduler** can trigger a nightly job (its retry setting is not handler idempotency — "
    "both are needed); an advisory lock stops two executions racing; there is no public migrate URL. The job's "
    "service account cannot act as the API's service account, and the checkout path never opens a DDL connection.",
    "- **Build lab `[local]`:** a local migrator. Ordered files (`001_init.sql`, `002_add_column.sql`, …), a "
    "`schema_migrations (version, dirty)` table, `up` and `down`, and a refusal to run while a version is dirty. "
    "Tests: running `up` twice is a no-op; a file that fails midway leaves its version dirty and blocks the next "
    "run; two concurrent runs serialise on the advisory lock. Then package the same migrations as a Cloud Run Job "
    "manifest (`[plan-only]` unless credits allow).",
]

OD09_THEORY = [
    "- **Theory:** the seek predicate, its index, and a from-scratch pager. Failure modes: an unstable sort (always "
    "end the key with a unique tiebreaker), internal IDs leaked without an authorisation check, and cursors that "
    "neither expire nor carry a signature. The seek is binary-search-shaped: state the invariant (every row before "
    "the cursor is already returned, every row after it is not) before writing it.",
    "- **Build lab `[local]`:** a `cursorpage` package (Python, then Go). Encode and decode an opaque, signed cursor "
    "over `(placed_at, order_id)`; run it against a fake ordered store searched by binary search, then against the "
    "lab's `customer_order`. Tests: forward pages; the empty result; a row deleted between two pages; a tampered "
    "cursor rejected. API shape: `GET /items?cursor=&limit=`.",
]

OD03_THEORY = ("- **Theory:** the pool-math worksheet, built here: one row per workload that connects (each Cloud Run "
               "service, each job, admin tools), with columns max instances, pool size per instance and their product. "
               "The sum must stay at or below `max_connections` minus the reserved superuser slots, with headroom for "
               "the reconnect storm after a failover. Add a test that fails when a configuration change breaks the "
               "inequality.")

DD03_LEDGER = [
    "- **Ledger rules (owned here):** amounts in integer minor units (`bigint`) with an explicit currency, never "
    "`float`. The payment provider is the system of record for money movement: the database stores provider tokens, "
    "payment and session IDs, amounts, currency and status — never card numbers (cyber PV-03). An order moves "
    "`created → requires_action → paid → fulfilled | refunded | failed`, and every arrow has a written guard (who, "
    "or what evidence). Illegal: `fulfilled` without `paid`; `paid` without a verified provider event (a browser "
    "redirect is not proof of payment); skipping `requires_action` when the provider demands it. A refund "
    "(`paid | fulfilled → refunded`) tracks the remaining minor units for partial refunds. A replayed provider event "
    "must not fulfil twice: idempotency key plus `ON CONFLICT` (SL-10).",
    "- **Build lab `[local]`:** the lab's `customer_order.status` uses a smaller set (`created`, `paid`, "
    "`fulfilled`, `refunded`, `cancelled`). Write the transition table for it, a check that rejects illegal arrows "
    "(a trigger or one guarded `UPDATE … WHERE status = …`), and table tests for every legal and every illegal "
    "transition.",
]

DD05_THEORY = [
    "- **Theory:** This module owns leakage prevention as well as the SQL shapes. **Leakage** is a feature built "
    "from information that did not exist at prediction time — most often a label or a later row pulled in by a "
    "plain equi-join. Train/serving skew (online features computed differently from training features) is a "
    "different failure, taught with D3.",
    "- **Build lab `[local]`:** build a feature table keyed by `event_time`; join labels with a plain join and "
    "measure the inflated metric; rewrite it as an as-of join (`LATERAL … WHERE valid_from <= t ORDER BY valid_from "
    "DESC LIMIT 1`) and show the metric fall back. Keep the failing test and the passing test.",
]

DD13_BUILD = ("- **Build lab `[local]`:** a key histogram. Count writes per key on the lab data (user 1 ≈ 135 "
              "orders), then compare three keys for a `(tenant, sku, ts)` event log — timestamp first, a hash prefix, "
              "a reversed timestamp — by simulating the partition each write lands in. Unit-test that the chosen "
              "partitioner keeps every partition within a stated bound of the mean.")

CS02_BUILD = ("- **Build lab `[paper]`:** a written LSM-vs-B-tree comparison with one flush diagram (memtable → "
              "immutable memtable → SSTable flush → compaction). Count the writes one update costs in each design, and "
              "explain why Bigtable's write path differs from Cloud SQL's B-tree pages. No full engine.")

AN02_THEORY = [
    "- **Theory:** BigQuery operations as well as SQL-level reading: datasets; partition by date and cluster by "
    "`tenant_id`; require a partition filter; on-demand bytes vs slot reservations; an authorized view for an "
    "analyst service account. The free tier (1 TiB of queries and 10 GiB of storage per month `(verify)`) is the "
    "primary free analytics lab. BigQuery never serves the checkout path.",
    "- **Build lab `[free-tier]`:** first run the query locally on the lab data: daily GMV by tenant from "
    "`customer_order`. Then batch-load the same rows into a date-partitioned, tenant-clustered BigQuery table, run "
    "the query with and without the partition filter, and record the dry-run bytes for each.",
]


def kit_block(root):
    d = os.path.abspath(os.path.join(root, "..", "sql-companion-work"))
    out = ["### 3.8 The lab kit files, in full", "",
           "Every file of the kit, in full, under its own name. Copy each block into a file of that name in one "
           "directory, bring the database up as in §3.2, and run the runners from that directory. Generated state "
           "(the database volume, run logs) is not part of the kit; the goldens files are, because the exercise "
           "cards cite them.", ""]
    for name in KIT:
        text = open(os.path.join(d, name), encoding="utf-8").read()
        if "```" in text:
            raise SystemExit(f"kit file {name} contains a code fence")
        if name.endswith(".json"):
            json.loads(text)
        role = KIT_ROLE[name]
        out += [f"#### `{name}`", "", role[0].upper() + role[1:] + ".", "", "```" + LANG[name.rsplit(".", 1)[1]]]
        out += text.rstrip("\n").split("\n") + ["```", ""]
    return out


def build(f, files, root):
    R = lambda old, new, ev, n=1: f.rep("SQL-1", "anchor-rewrite", old, new, ev, n=n)  # noqa: E731

    # title block and §0
    R('Companion to `Curriculum` ("The Consolidated Cloud Mastery Curriculum") and to its reference application '
      '`northstar-reference-app.md` (Track N).', 'Companion to the main course, "The Consolidated Cloud Mastery '
      'Curriculum".', EV5 + "; " + EV11)
    R("Sibling of `system-design-primer-companion.md` (its SD-13", "Sibling of the System Design Primer companion "
      "(its SD-13", EV6)
    f.line("SQL-1", "anchor-rewrite", "> **Note:** the `TB-…` / `SRC-…` labels in the line above are this file's",
           "> **Note:** the `TB-…` / `SRC-…` labels in the line above are this file's bibliography keys; the books "
           "and courses are named in full beside them.", EV6)
    R("Why: `Curriculum` owns the order and the module spine; `northstar-reference-app.md` owns the *product spine* "
      "(Northstar on GCP) and the Cloud SQL procedure (N2.3). Since the refactor this file also owns the engine "
      "slices DB-1 … DB-10 (§4.0). `Curriculum` deliberately does not own",
      "Why: the main course owns the order and the module spine. This file owns the engine slices DB-1 … DB-10 "
      "(§4.0) and the Cloud SQL procedure (OD-11). The main course deliberately does not own", EV5 + "; " + EV11)
    f.line("SQL-1", "anchor-rewrite", "2. **Ownership split (memorise).**",
           "2. **Ownership split (memorise).** *Other parts own:* the Firestore, Bigtable and store-choice material "
           "(primer SD-22, SD-23, SD-25), outbox/inbox (A9 theory; design-patterns ARCH-11 shape), payment-flow "
           "abuse (cyber AB-06), billing-export SQL (B4). *This file owns:* SQL-language mastery (SL), relational "
           "theory (RT), the CS theory tier under the slices (CS), data-design method (DD) including the ledger "
           "rules (DD-03) and point-in-time correctness and leakage (DD-05), operating-a-database craft (OD) "
           "including Cloud SQL (OD-11), migrations as jobs (OD-08), the cursor pager (OD-09) and pool math "
           "(OD-03), analytics and dialect craft (AN) including BigQuery operations (AN-02), pre-SQL prerequisites "
           "(PQ), the exercise ladder (§6), and the engine slices DB-1 … DB-10 and their toys (§4.0). **Where a "
           "§4.0 slice toy exists (WAL codec, slotted page, B-tree, iterator executor, visibility simulator) this "
           "file never asks for a second toy — it adds the analytic layer (formulas, schedules, cost models) that "
           "the toy's tests do not reach.**", EV5 + "; " + EV9)
    R("ten-rung sequence (`Curriculum` §0.4.3)", "ten-rung sequence (rule 0.4.3, §0.6)", EV6)
    R("before its N2.3 session", "before its OD-11 session", EV5)
    R("exactly as in `Curriculum` §0.4.6.", "exactly as in rule 0.4.6 (§0.6).", EV6)
    R("(`Curriculum` §0.4.4, predict → run → discrepancy; C-53.)", "(Rule 0.4.4 in §0.6: predict → run → "
      "discrepancy.)", EV6)
    R("the learner ledger `session-progress-ledger.md` (C-57; it replaces the old parent's \"Teaching contract → "
      "Learner state\") records", "the tutor's progress ledger (§0.6) records", EV6)
    R("(`Curriculum` §0.5 Lab Safety)", "(Lab Safety, §0.6)", EV6)
    R("same rights as `Curriculum` §0.4.1. **On a conflict:** `Curriculum` wins on", "same rights as rule 0.4.1 "
      "(§0.6). **On a conflict:** the main course wins on", EV6 + "; " + EV11)
    R("the Suite Session Protocol in `Curriculum` §0.4 governs.", "the Suite Session Protocol (rule 0.4.2 in §0.6) "
      "governs.", EV6)
    f.line("SQL-1", "anchor-rewrite", "- The old parent's labels (`T.*`",
           "- Main-course IDs (`A1…D4`, `M1…M6`, `U1…U7`, `S1…S11`, the Part V category IDs `V-…`) are stitch tags "
           "into the main course. `DB-1 … DB-10` are this file's engine slices (§4.0). `SD-…` are primer-companion "
           "IDs. `TB-…`/`SRC-…` are this file's bibliography labels (title block).", EV5 + "; " + EV6)
    R("; renamed from `HS` / `UG` / `grad` in §5 of the refactor)", ")", EV6)
    f.line("SQL-1", "anchor-rewrite", "- `Northstar` = the running reference application",
           "- **The lab database** (§3) is a small multi-tenant storefront — tenants, users, categories, products "
           "with effective-dated prices, stock, orders and order lines, payments, shipments and reviews — plus a "
           "semi-structured event stream and a deliberately messy staging table.", EV5)

    # §2 stitch table
    R("| `Curriculum` module (was: old-parent label) |", "| Main-course module |", EV11)
    R("| **S2** + **N0.4** HLD/LLD contract", "| **S2** HLD/LLD contract", EV5)
    R("| **B5** IAM (+ **N2.3** IAM DB auth) |", "| **B5** IAM (+ **OD-11** IAM DB auth) |", EV5)
    R("; *N8.1 owns the spreadsheet — recall it* |", ", with the OD-03 worksheet |", EV5)
    R("| **N2.3** Cloud SQL setup (required procedure) | OD-03", "| **V-STOR** Cloud SQL setup (required procedure) | "
      "**OD-11** provisioning, connectivity, security, operations · OD-03", EV5)
    R("| **A8** (NoSQL) + **N2.4** Firestore |", "| **A8** (NoSQL) + **V-STOR** Firestore (primer SD-22) |", EV5)
    R("| **N2.5** Cloud Storage |", "| **V-STOR** Cloud Storage |", EV5)
    R("| **A8** + **C4** + **N2.6** config, migrations, jobs |", "| **A8** + **C4** config, migrations, jobs |", EV5)
    R("OD-08 migration tooling & testing (dirty state, advisory lock)", "OD-08 migrations as jobs, tooling & testing "
      "(dirty state, advisory lock)", EV9)
    R("| **A9** + **V-STOR** + **N2.7** Spanner & NoSQL map |", "| **A9** + **V-STOR** Spanner & NoSQL map (primer "
      "SD-25) |", EV5)
    R("| **A8** + **N5.3** ledger and consistency |", "| **A8** ledger and consistency |", EV5)
    R("DD-05 money (integer minor units), DD-09 audit/history", "DD-03 money and ledger rules (integer minor units), "
      "DD-07 audit/history", "correction: the money module is DD-03 and audit/history is DD-07 (§4.5 headings)")
    R("| **Phase 4 Security** + **N7.3** data protection |", "| **Phase 4 Security** data protection (cyber CR-14) |",
      EV5)
    R("| **S2** + **N8.0** Donne-Martin building blocks · **N8.C** evidence packs |", "| **S2** + primer building "
      "blocks · HLD evidence packs |", EV5)
    R("| **N8.1** primitives — cursor pagination", "| **A9** scale primitives — cursor pagination", EV5)
    R("(**N8.1.5 owns the from-scratch pager**)", "(with the from-scratch pager)", EV5 + "; " + EV9)
    R("| **V-STOR** + **N9.1** Memorystore |", "| **V-STOR** Memorystore |", EV5)
    R("| **V-STOR** + **N9.4** Spanner, AlloyDB", "| **V-STOR** Spanner, AlloyDB", EV5)
    R("| **V-DATA** + **N9b.1** Big-data services", "| **V-DATA** Big-data services", EV5)
    R("| **D3** + **N9c.1** features, labels, skew (**as-of join** owner) | SL-08 / SL-04:", "| **D3** features, "
      "labels, skew | DD-05 leakage and point-in-time correctness · SL-08 / SL-04:", EV5 + "; " + EV9)
    R(" *N9c.1 owns leakage; this file owns the join* |", " |", EV5)
    R("| **D4** + **N9c.2 / N9c.5** retrieval, RAG |", "| **D4** retrieval, RAG |", EV5)
    R("| **N11** capstone (Northstar v1) | SQL-CAP1 – SQL-CAP4 are the database acceptance tests of the capstone |",
      "| **S11** case-study capstone | SQL-CAP1 – SQL-CAP4 are its database acceptance tests |", EV5)
    R("| **N11b** control-plane capstone |", "| **S11** control-plane case study |", EV5)

    # §2.1 overlap register
    R("> **Note:** the suite-wide register is `Curriculum` §0.3;", "> **Note:** the suite-wide register is the main "
      "course §0.3;", EV11)
    R("DB-1 … DB-10 are owned by this file since C-05 (§4.0).", "DB-1 … DB-10 are owned by this file (§4.0).", EV6)
    R("(this file since C-05; A8)", "(this file; A8)", EV6)
    R("| WAL, replica, PITR (DB-10; foreign `G4` → N2.3) |", "| WAL, replica, PITR (DB-10) |", EV5)
    R("| Cloud SQL provisioning, Auth Proxy, private IP, HA, flags | **N2.3** |", "| Cloud SQL provisioning, Auth "
      "Proxy, private IP, HA, flags | **OD-11** |", EV5 + "; " + EV9)
    R("| Migrations as jobs, expand/contract | **N2.6** |", "| Migrations as jobs, expand/contract | **OD-08** (jobs) "
      "+ **DD-11** (expand/contract) |", EV5 + "; " + EV9)
    R("| Spanner, Bigtable, Firestore map | **N2.7 / N2.4** |", "| Spanner, Bigtable, Firestore map | **Primer SD-22 / "
      "SD-23 / SD-25** |", EV5)
    R("| Cursor pagination | **N8.1.5** (from-scratch pager) | OD-09 the SQL seek predicate & its supporting index; "
      "PX-9 measured against OFFSET |", "| Cursor pagination | **OD-09** (seek predicate, index, from-scratch pager) "
      "| PX-9 measured against OFFSET |", EV5 + "; " + EV9)
    R("| Hot partition, key histogram | **N8.1** |", "| Hot partition, key histogram | **DD-13** (key histogram) + "
      "primer SD-23 (row keys) |", EV5 + "; " + EV9)
    R("| Connection-pool math | **N8.1 / N2.3** |", "| Connection-pool math | **OD-03** (worksheet) |", EV5 + "; " + EV9)
    R("| RLS multi-tenancy | **N8.1 / A8** |", "| RLS multi-tenancy | **A8** + DD-09 (design) |", EV5)
    R("(`Curriculum` §0.3: 2PC/Saga/outbox)", "(main course §0.3: 2PC/Saga/outbox)", EV11)
    R("| Ledger, minor-unit ints | **N5.3** |", "| Ledger, minor-unit ints | **DD-03** (ledger rules) |", EV5 + "; " + EV9)
    R("| BigQuery partition/cluster/cost | **N9.4 / N9b.1** | AN-02 SQL-level cost reading; DT drills |",
      "| BigQuery partition/cluster/cost | **AN-02** (cost and operations) | DT drills |", EV5 + "; " + EV9)
    R("| As-of / point-in-time join | **N9c.1** (D3) |", "| As-of / point-in-time join | **DD-05** (leakage; D3) |",
      EV5 + "; " + EV9)
    R("| `Curriculum` **M1 / A4", "| **M1 / A4", EV11)

    # §2.2 / §2.3
    R("| **DB-10** WAL, replica, PITR (**N2.3**) |", "| **DB-10** WAL, replica, PITR (**OD-11**) |", EV5)
    R("`Curriculum`'s spine is Phases 0–3 (Tracks A–D, mostly in parallel) → Phase 4 → …, with the reserved M/U/S "
      "tracks placed by R4.", "The main course's spine is Phases 0–3 (Tracks A–D, mostly in parallel) → Phase 4 → …; "
      "the reserved M/U/S tracks are not placed yet.", EV6 + "; " + EV11)
    R("the V-STOR and N2.3…N2.7 rows as bound in §2", "the V-STOR, OD-11 and OD-08 rows as bound in §2", EV5)
    R("| **A7, A9, A10 + N5.3** | SQL-E9.3 (A7), TX-5 (A9), SQL-E10.6 (A10), SQL-E4.5/SQL-CAP2 (N5.3) |",
      "| **A7, A8, A9, A10** | SQL-E9.3 (A7), TX-5 (A9), SQL-E10.6 (A10), SQL-E4.5/SQL-CAP2 (A8 ledger, DD-03) |", EV5)
    R("| **N8.0/N8.1/N8.C + S2** | PX-9 / DD-13 with N8.1;", "| **A9 + S2** | PX-9 / DD-13 with the scale "
      "primitives;", EV5)
    R("| **V-STOR, V-DATA, D3/D4 + N9.1/N9.4/N9b.1/N9c.1** |", "| **V-STOR, V-DATA, D3/D4** |", EV5)
    R("SQL-E6.4/SQL-E13.4/SQL-E13.5 at D3 (N9c.1) |", "SQL-E6.4/SQL-E13.4/SQL-E13.5 at D3 (DD-05) |", EV5)
    R("| **N11 / N11b** |", "| **S11** |", EV5)
    R(" (order unchanged; provenance: `unified-curriculum.md` §5.4):**", " (order unchanged):**", EV6)

    # §3 lab kit
    R("## 3. Lab kit — deterministic Northstar SQL lab", "## 3. Lab kit — deterministic SQL lab", EV5)
    R("with schema `lab` (OLTP slice of Northstar) plus `work` (scratch) and fingerprint functions `lab.chk` / "
      "`lab.chk_o`. Sources on this box: `sql-companion-work/lab_schema.sql`, `lab_seed.sql`, runners `run_ex.py`, "
      "`plans.py`, `tx_tests.py`.", "with schema `lab` (the storefront OLTP data of §0.4) plus `work` (scratch) and "
      "fingerprint functions `lab.chk` / `lab.chk_o`. Every kit file is printed in full in §3.8: the schema "
      "`lab_schema.sql`, the seed `lab_seed.sql`, the runners `run_ex.py`, `plans.py`, `tx_tests.py`, and the rest.",
      EV5 + "; D6: the kit is inside the file (§3.8)")
    R("**destroy the same day** (`Curriculum` §0.5). Auth Proxy for IAM DB auth when N2.3 is unlocked",
      "**destroy the same day** (Lab Safety, §0.6). Auth Proxy for IAM DB auth when OD-11 is unlocked", EV5 + "; " + EV6)
    R("wrong predictions are the teaching moment (gcp \"Database protocol\").", "wrong predictions are the teaching "
      "moment.", EV6 + " (a pointer to the legacy course)")
    R("### 3.7 How runners relate", "### 3.7 How runners relate (files in §3.8)", EV6)
    R("Format per module (same contract as `system-design-primer-companion.md`):", "Format per module (same contract "
      "as the primer companion):", EV6)
    f.line("SQL-1", "anchor-rewrite", "*Ported by the refactor (2026-09-24, C-05; decision D1).*",
           "*The engine slices.* This file **owns** the slices DB-1 … DB-10; main course A8 points here, and each "
           "slice is taught as one session with the companion theory paired to it in §2.2. The Cloud SQL procedure "
           "they map onto is OD-11.", EV6 + "; D10: no pointer to the legacy course")
    R("migrations via Job (N2.6)", "migrations via Job (OD-08)", EV5)
    R("#### DB-10 — WAL, replica, PITR (foreign `G4` WAL codec → N2.3)", "#### DB-10 — WAL, replica, PITR (WAL codec; "
      "the Cloud SQL side is OD-11)", EV5)

    # §4 module bodies
    R("Lens-1: Northstar OLTP stays ≥3NF;", "Lens-1: the lab's OLTP schema stays ≥3NF;", EV5)
    R("Lens-2: lab ER is Northstar OLTP slice.", "Lens-2: the lab ER diagram (the storefront OLTP schema, §3).", EV5)
    R("(leakage owner is N9c.1)", "(leakage owner is DD-05)", EV5)
    R("- **GCP lens:** Lens-1: N8.1 owns LSM-vs-B-tree comparison toy; here formulas + PX cards.",
      "- **GCP lens:** Lens-1: Cloud SQL and AlloyDB (B-tree pages) vs Bigtable (LSM write path); here formulas + PX "
      "cards and the build lab below.", EV5)
    f.ins_after("SQL-2", "and the build lab below. Lens-2: PX-1…PX-6.", [CS02_BUILD], EV9)
    R("when A9 / N2.7 is unlocked", "when A9 and primer SD-25 are unlocked", EV5)
    R("- **GCP lens:** Lens-1: ledger rules in N5.3 — this file models them.", "- **GCP lens:** Lens-1: the ledger "
      "rules below, on Cloud SQL Postgres.", EV5)
    f.ins_after("SQL-2", "- **Check:** Why store both `currency` and `total_minor` rather than a float USD conversion?",
                DD03_LEDGER, EV9)
    f.line("SQL-2", "new-content", "- **Theory:** Leakage prevention is owned by N9c.1; SQL shapes live here.",
           DD05_THEORY, EV5 + "; " + EV9)
    R("- **GCP lens:** Lens-1: N8.1 owns RLS primitive; here SQL policies + composite FKs.", "- **GCP lens:** Lens-1: "
      "RLS on Cloud SQL Postgres with the tenant set per transaction (`SET LOCAL`; SL-13 owns the syntax); here the "
      "design — policies + composite FKs.", EV5 + "; " + EV9)
    R("- **Theory:** Hot-tenant skew.", "- **Theory:** Hot-tenant skew; a noisy tenant is capped by a per-tenant "
      "limit (cyber AB-01 owns the limiter).", EV9)
    R("- **Theory:** N2.6 owns migrations-as-jobs; here lock/SQL craft.", "- **Theory:** OD-08 owns running "
      "migrations as jobs; here lock/SQL craft.", EV5)
    R("- **GCP lens:** Lens-1: N8.1 owns the hot-partition primitive.", "- **GCP lens:** Lens-1: Spanner and "
      "Bigtable key design (primer SD-23 owns row keys); build lab below.", EV5)
    f.ins_after("SQL-2", "- **Check:** Write a query that ranks users by order count and spot the hotspot.",
                [DD13_BUILD], EV9)
    f.line("SQL-2", "new-content", "- **Theory:** N8.1 owns the spreadsheet — recall it.", OD03_THEORY, EV5 + "; " + EV9)
    f.line("SQL-2", "new-content", "- **Theory:** gcp owns migrations-as-jobs; here SQL test discipline.",
           OD08_THEORY, "D10: no pointer to the legacy course; " + EV9)
    f.line("SQL-2", "new-content", "- **Theory:** N8.1.5 owns the from-scratch pager — here the seek predicate & index.",
           OD09_THEORY, EV5 + "; " + EV9)
    # OD-11, new, after OD-10
    R("### 4.6 Operating databases (OD-01 … OD-10)", "### 4.6 Operating databases (OD-01 … OD-11)", EV9)
    R("OD-01 … OD-10, PX-1 … PX-11", "OD-01 … OD-11, PX-1 … PX-11", EV9)
    h = f.heading("OD-10 · Testing SQL")
    e = f.section_end(h)
    while f.L[e - 1].strip() == "":
        e -= 1
    f.ins("SQL-3", e, [""] + OD11, EV9 + " (Cloud SQL procedure: provisioning, connectivity, security, operations, "
          "Terraform LLD)")
    R("- **Theory:** Northstar OLTP lab vs analytics copies.", "- **Theory:** the OLTP lab schema vs analytics "
      "copies.", EV5)
    f.line("SQL-2", "new-content", "- **Theory:** gcp owns ops; here SQL-level reading.", AN02_THEORY,
           "D10: no pointer to the legacy course; " + EV9)
    R("- **Theory:** Firestore when it wins/loses — gcp owns product; here same-question drill.",
      "- **Theory:** Firestore when it wins/loses — primer SD-22 owns the product; here the same-question drill, "
      "with the two rules it depends on: a server using the Admin SDK bypasses security rules, so tenant and role "
      "checks live in server code; and while carts live in Firestore and orders in SQL, the handoff goes through an "
      "outbox (SL-10), never a dual write.", "D10: no pointer to the legacy course; " + EV9)
    R(" (provenance: `unified-curriculum.md` nodes `DB-SQL` / `DB-ENGINE`)", "", EV6)

    # §6–§9, appendices
    R("This is the same shape as **N9c.1** (D3) point-in-time joins.", "This is the same shape as the DD-05 (D3) "
      "point-in-time joins.", EV5)
    R("Same principle as the Northstar ledger's (N5.3) determinism rules.", "Same principle as the ledger's "
      "determinism rules (DD-03).", EV5)
    R("— N2.6 expand/contract.)", "— DD-11 expand/contract, run as an OD-08 job.)", EV5)
    R("This is defence in depth beneath RLS (N8.1).", "This is defence in depth beneath RLS (DD-09).", EV5)
    R("— N8.1 RLS.", "— DD-09 RLS.", EV5)
    R("(V-DATA, N9b.1)", "(V-DATA, AN-02)", EV5)
    R("- **Tags:** PX-9 · OD-09 · N8.1.5", "- **Tags:** PX-9 · OD-09", EV5)
    R("- **Tags:** N5.3·DD-05", "- **Tags:** DD-03·DD-05", EV5)
    R("- **Tags:** AN-06·N2.4", "- **Tags:** AN-06·SD-22", EV5)
    R("- **Tags:** DD-02·N8.0", "- **Tags:** DD-02·S2", EV5)
    R("- **Tags:** DD-11·N2.6", "- **Tags:** DD-11·OD-08", EV5)
    R("- **Tags:** DD-13·N2.7", "- **Tags:** DD-13·SD-25", EV5)
    R("- **Tags:** DD-07·N7.3", "- **Tags:** DD-07·CR-14", EV5)
    R("Mirror `Curriculum` C5 posture:", "Mirror the C5 posture:", EV11)
    R("| Ties OD-03/04; Auth Proxy as separate module |", "| Ties OD-03/04; the Auth Proxy side is OD-11 |", EV9)
    R("Database acceptance tests for N11 (Northstar).", "Database acceptance tests for the S11 case-study capstone.",
      EV5)
    R("does not re-execute Postgres in the markdown generator.", "does not re-execute Postgres when this file is "
      "assembled. The goldens files are printed in full in §3.8.", EV6)
    R("- **SQL-E3.7 note:** `out_ex_l1_4.txt` contains a duplicate run line", "- **SQL-E3.7 note:** the run log of "
      "levels 1–4 contained a duplicate run line", EV6)
    R("- **gcp toys DB-1…DB-10:** not duplicated; analytic layer only.", "- **Engine-slice toys DB-1…DB-10 (§4.0):** "
      "not duplicated; the concept modules add the analytic layer only.", "D10: no pointer to the legacy course")

    # the lab kit, in full (D6), at the end of §3
    s = f.heading("3.7 How runners relate")
    e = f.section_end(s)
    while f.L[e - 1].strip() in ("", "---"):
        e -= 1
    f.ins("SQL-4", e, [""] + kit_block(root)[:-1], "D6: all material inside the file — the lab kit, verbatim from "
          "the kit directory", cls="new-content")
    f.rep("SQL-4", "anchor-rewrite", "-- Northstar SQL Lab — ", "-- Storefront SQL Lab — ", EV5 + " (the kit's two "
          "header comments; comments only, so no golden fingerprint changes)", n=2, fence=True)
    evk = ("D10 + D11: an exercise note in the kit pointed at the legacy course; it now names the module that holds "
           "the material (note text only, so no golden fingerprint changes)")
    for o, n in [("same shape as gcp-curriculum **9c.1** point-in-time joins", "same shape as the point-in-time joins "
                  "of DD-05"),
                 ("Same principle as the gcp-curriculum ledger's determinism rules.", "Same principle as the ledger's "
                  "determinism rules (DD-03)."),
                 ("the whole point of gcp-curriculum 3.4/3.5.", "the whole point of at-least-once pipelines (A9)."),
                 ("every chunk commits separately — gcp-curriculum 2.6 expand/contract.", "every chunk commits "
                  "separately — the OD-08 expand/contract pattern."),
                 ("beneath RLS (gcp-curriculum 8.1).", "beneath RLS (DD-09)."),
                 ("must be `SET LOCAL` per transaction — gcp-curriculum 8.1 RLS.", "must be `SET LOCAL` per "
                  "transaction — DD-09 RLS."),
                 ("cluster by product (gcp-curriculum 9b.1)", "cluster by product (AN-02)")]:
        f.rep("SQL-4", "anchor-rewrite", o, n, evk, fence=True)
    f.rep("SQL-4", "anchor-rewrite", "makes it a seq scan per user (E12.1).", "makes it a seq scan per user (PX-1).",
          "R3 + C-51: the kit's copy of the E4.7 trap kept the undefined label E12.1, which the rename resolved to PX-1 "
          "in the course text (note text only, so no golden fingerprint changes)", fence=True)

    # R3 zero-orphans gate: BH-1 and BH-6 were bound nowhere in §2 since the input (their Tags name the home)
    ev8 = ("R3 §8.2 zero orphans: the bug-hunt card was bound in no §2 row since the input; its own Tags line names "
           "the module it belongs to")
    f.rep("SQL-8", "anchor-rewrite", "| SQL-E1 → SQL-E10 by level (§6 gates) |",
          "| SQL-E1 → SQL-E10 by level (§6 gates); BH-1 after SQL-E3.5 |", ev8 + " (SQL-E3.5, the fan-out join)")
    f.rep("SQL-8", "anchor-rewrite", "| SQL-E9.6, SCH-4 |", "| SQL-E9.6, SCH-4, BH-6 |", ev8 + " (DD-11 expand/contract)")

    # shared contract after the preferences (§0.5), then the file-style parent name everywhere else
    h = f.heading("0.5 Learner teaching preferences")
    e = f.section_end(h)
    while f.L[e - 1].strip() in ("", "---"):
        e -= 1
    f.ins("SQL-5", e, [""] + contract_copy(files, 5, 6), "D6: each part carries the shared teaching rules in its own "
          "§0 (D7 exemption: rules, not topics)", cls="append")
    parent_name(f, "SQL-6")

    # D9: the two thin items the gap scan found — the TF-DB rows had goals only, SQL-CAP3 had no acceptance test
    ev9 = "D9: a thin exercise gets its acceptance criteria inside the file (facts only, D10)"
    f.ins_after("SQL-7", "| **TF-DB6** | IAM bindings for DB roles / BQ dataset access | SL-13 least privilege |", [
        "",
        "**What each plan must show** (resource and attribute names from the Google provider; `(verify)` them "
        "against the provider version you pin). The exercise is done when `terraform plan` lists these and nothing "
        "public:",
        "",
        "- **TF-DB1:** `google_compute_global_address` (purpose `VPC_PEERING`) + "
        "`google_service_networking_connection` for private services access; `google_sql_database_instance` with "
        "`database_version = \"POSTGRES_16\"`, `settings.ip_configuration.ipv4_enabled = false` and "
        "`private_network` set, `backup_configuration` with `point_in_time_recovery_enabled = true`, one "
        "`database_flags` block (e.g. `log_min_duration_statement`), `deletion_protection = true`. Fail: any "
        "`authorized_networks` entry or a public IP.",
        "- **TF-DB2:** the TF-DB1 primary with `availability_type = \"REGIONAL\"` (HA, same-region standby) plus a "
        "second `google_sql_database_instance` with `master_instance_name` pointing at it (read replica). Explain in "
        "one line why the replica is not the failover target for HA and which OD-05 lag SLI you would alert on.",
        "- **TF-DB3:** `google_alloydb_cluster` (network config on the same VPC) + `google_alloydb_instance` with "
        "`instance_type = \"PRIMARY\"` and a `machine_config` CPU count. Write the monthly cost line next to TF-DB1's "
        "at the same vCPU count.",
        "- **TF-DB4:** `google_spanner_instance` (a regional `config`, `processing_units = 100`, the smallest paid "
        "size) + `google_spanner_database` whose `ddl` list creates a parent table and an interleaved child "
        "(`INTERLEAVE IN PARENT … ON DELETE CASCADE`); `deletion_protection = true`.",
        "- **TF-DB5:** `google_bigquery_dataset` (location, default table expiration for the sandbox) + "
        "`google_bigquery_table` with `time_partitioning` (`type = \"DAY\"`, `field` = the event timestamp), "
        "`clustering` on the filter columns and a required partition filter. Pair it with the AN-02 bytes napkin: "
        "bytes scanned by one day's query vs the whole table.",
        "- **TF-DB6:** `google_project_iam_member` giving the app's service account `roles/cloudsql.client` and "
        "`roles/cloudsql.instanceUser`; `google_sql_user` of type `CLOUD_IAM_SERVICE_ACCOUNT`; "
        "`google_bigquery_dataset_iam_member` giving an analyst group `roles/bigquery.dataViewer` on one dataset. "
        "Fail: any primitive role (`roles/owner`, `roles/editor`) or a project-wide BigQuery grant.",
    ], ev9)
    f.ins_after("SQL-7", "**SQL-CAP3 spec (consistent with lab):**", [
        "",
        "**SQL-CAP3 acceptance** (all four must hold; run on the local lab Postgres):",
        "",
        "1. **No oversell.** Set one product's `stock.on_hand` to 1. Run the checkout from 10 concurrent sessions "
        "(`pgbench -n -c 10 -t 1 -f` with your checkout transaction as the script, or two `psql` sessions as in TX-1). Pass: exactly one new "
        "`customer_order`, `on_hand = 0`, and the other nine end cleanly (\"sold out\", not an error trace). The claim "
        "is one conditional `UPDATE … WHERE on_hand >= qty RETURNING` (the `safe.sql` shape), or a `SELECT … FOR "
        "UPDATE` then update (TX-8); a read-then-write without either fails.",
        "2. **Idempotent.** Submit the same `(tenant_id, idempotency_key)` twice. Pass: one order row, and both calls "
        "return the same `order_id` (`INSERT … ON CONFLICT (tenant_id, idempotency_key) DO NOTHING RETURNING "
        "order_id`, then read the existing row when nothing returns). Stock moves once.",
        "3. **Money in minor units.** `total_minor` equals `sum(qty * unit_price_minor)` over the order's lines "
        "(prove it with a query that returns zero mismatched orders); no `float`/`real` column anywhere in the delta.",
        "4. **ADR.** One page naming the isolation level and why: READ COMMITTED is enough when the claim is a single "
        "conditional `UPDATE`; a check that reads several rows before writing needs SERIALIZABLE (or explicit row "
        "locks) plus a retry loop on SQLSTATE `40001`. Name the retry limit and what the customer sees when it is hit.",
        "",
        "Evidence: the DDL delta, the transcript of tests 1–3 (commands and final `SELECT`s) and the ADR. Tutor key "
        "(after attempt): the lab schema already holds `CHECK (on_hand >= 0)` and `UNIQUE (tenant_id, "
        "idempotency_key)`, so the minimal correct delta is often just the checkout transaction itself; a submission "
        "that adds a second uniqueness table or an application-side lock has missed that.",
    ], ev9)
    f.line("SQL-7", "anchor-rewrite", "- **SQL-CAP3:** design/TX evidence capstone — no single `lab.chk` fingerprint",
           "- **SQL-CAP3:** design/TX evidence capstone — no single `lab.chk` fingerprint; acceptance is the four "
           "tests in §9 (transcript + ADR).", ev9)
    f.line("SQL-7", "anchor-rewrite", "- **TF-DB*:** plan-only stubs; no checked-in `.tf`",
           "- **TF-DB*:** plan-only by default; the learner writes the `.tf`, and §8.2 lists what each plan must show. "
           "Provider attribute names are `(verify)`.", ev9)
