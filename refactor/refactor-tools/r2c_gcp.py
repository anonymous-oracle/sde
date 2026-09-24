"""R2c-bis: the final check of the legacy GCP course notes against the six parts (learner decision D13).

The learner restored the legacy GCP notes and asked for one last pass: add only what no part yet teaches, each at its
one home (D7), and nothing that merely repeats a part at more length. The notes are material only (D10): no rule,
structure or capstone comes from them, and this build never reads them — each addition is authored here, and its
evidence names the section of the notes it came from. The full candidate list, with what was not added and why, is
in refactor-state.md §6d.

Every edit is journaled (rule IDs GAP-n) into the main course, run right after r2c_go.cur.
"""
from r2b_common import F  # noqa: F401  (documented type of f)

EV = "D13: final check of the legacy GCP notes (material only, D10); "


def cur(f):
    # Part V service map: names the certifications test that no part listed
    f.rep("GAP-1", "anchor-rewrite", "Networking: VPC, Cloud Load Balancing, Cloud CDN, Cloud Interconnect/VPN, Cloud DNS, "
          "Cloud Armor", "Networking: VPC, Cloud Load Balancing, Cloud CDN, Cloud Interconnect/VPN, Cloud DNS, Cloud "
          "Armor, Cloud Router, Cloud NAT, Private Service Connect, Network Connectivity Center, Cloud NGFW",
          EV + "notes Part 8b (hybrid connectivity, PCA 2.1) and 6.12 (Cloud NGFW)")
    f.rep("GAP-2", "anchor-rewrite", "Storage/DB: Cloud Storage, Cloud SQL, Spanner, Bigtable, Firestore, Memorystore, "
          "AlloyDB", "Storage/DB: Cloud Storage, Cloud SQL, Spanner, Bigtable, Firestore, Memorystore, AlloyDB, "
          "Filestore, Persistent Disk / Hyperdisk, Backup and DR Service",
          EV + "notes 2.5, 2.7 and 1.8 (block and file storage, backup)")
    f.rep("GAP-3", "anchor-rewrite", "Data/Analytics: BigQuery, Pub/Sub, Dataflow, Dataproc, Cloud Composer, Looker",
          "Data/Analytics: BigQuery, Pub/Sub, Dataflow, Dataproc, Cloud Composer, Looker, Datastream, Data Fusion, "
          "Dataplex, BigLake, Analytics Hub", EV + "notes 9b.1 (Big Data services)")
    f.rep("GAP-4", "anchor-rewrite", "Gemini Enterprise/Agent Platform, AutoML, BigQuery ML", "Gemini Enterprise/Agent "
          "Platform, AutoML, BigQuery ML, the pre-built AI APIs (Vision, Video Intelligence, Speech-to-Text, Natural "
          "Language, Translation, Document AI)", EV + "notes 9b.3 (pre-built AI APIs, PCA 2.5 / PMLE low-code)")
    f.rep("GAP-5", "anchor-rewrite", "Security: IAM, Cloud KMS, VPC Service Controls, Binary Authorization, Security Command "
          "Center, Google SecOps (Chronicle)", "Security: IAM, Cloud KMS, VPC Service Controls, Binary Authorization, "
          "Security Command Center, Google SecOps (Chronicle), Identity-Aware Proxy, Identity Platform, Secret "
          "Manager, Certificate Manager, Sensitive Data Protection, Organization Policy Service, Cloud Asset "
          "Inventory, Assured Workloads", EV + "notes 4.1 (identity product map), 7.2–7.7")
    f.rep("GAP-6", "anchor-rewrite", "Ops/DevOps: Cloud Build, Cloud Deploy, Artifact Registry, Cloud Monitoring/Logging",
          "Ops/DevOps: Cloud Build, Cloud Deploy, Artifact Registry, Cloud Monitoring/Logging, Cloud Trace, Cloud "
          "Profiler, Error Reporting, Managed Service for Prometheus, Service Health, Cloud Billing reports and the "
          "billing export to BigQuery, Recommender (Active Assist), Cloud Quotas, Carbon Footprint",
          EV + "notes 0.1 (billing), 10.0, 10.3, 10.4, 10.6")
    f.ins_after("GAP-7", "What makes it hard: it's not \"what does this service do,\"", [
        "The published case studies (exam guide v6.1): Altostrat Media, Cymbal Retail, EHR Healthcare, KnightMotives "
        "Automotive `(verify)` against the live guide. Each gets a written HLD and one \"I pick X because Y, I accept "
        "Z\" answer per requirement in S11."], EV + "notes, research basis (PCA v6.1 row) and Part 11")
    # reserved-track scopes the notes fill
    f.rep("GAP-8", "anchor-rewrite", "| S8 | Migration & modernization | |", "| S8 | Migration & modernization | the "
          "six Rs mapped to landings (rehost with Migrate to Virtual Machines, replatform, re-architect for GKE or Cloud "
          "Run, retire, retain, repurchase); Migration Center discovery, dependency mapping and wave planning; "
          "licence impact (bring-your-own vs included) before wave 1; data movement (Database Migration Service, "
          "Datastream, Storage Transfer Service, Transfer Appliance); wave-0 connectivity; cutover checklist with a "
          "written rollback (PCA 1.4) |", EV + "notes Part 8c (migration, PCA 1.4)")
    f.rep("GAP-9", "anchor-rewrite", "| S11 | Case-study studio | |", "| S11 | Case-study studio | the four published PCA "
          "case studies, each as an HLD with its trade-off answers |", EV + "notes Part 11 (PCA case HLDs)")
    f.rep("GAP-10", "anchor-rewrite", "| M5 | Numerical Methods & Floating Point | IEEE 754, rounding, decimal vs binary |",
          "| M5 | Numerical Methods & Floating Point | IEEE 754, rounding, decimal vs binary; catastrophic "
          "cancellation, compensated (Kahan) summation, stable reformulations (`log1p`, log-sum-exp) |",
          EV + "notes M.NS (numerical stability)")
    # track lines: topics no part teaches
    f.rep("GAP-11", "anchor-rewrite", "| Heavy hitters / sketches / approximate counting | U2 (randomized algorithms) |",
          "| Heavy hitters / sketches / approximate counting (count-min sketch, HyperLogLog, Bloom filters with their "
          "false-positive rate (1 − e^(−kn/m))^k) | U2 (randomized algorithms) |",
          EV + "notes 8.1 (Bloom FPR formula) and 8.D (HyperLogLog); the register already gives sketches to U2 (D7)")
    f.ins_after("GAP-12", "SSH and remote access", [
        "Observing a live system: `/proc`, `ps`, `ss`, the OOM killer and cgroup memory limits (why a Cloud Run "
        "instance is killed), predicted before they are observed, on your own VM only"],
        EV + "notes 10.7 (Linux / OS internals)")
    f.ins_after("GAP-13", "Budget alerts, tagging/labeling for cost allocation", [
        "Three budgets per system: money (billing account → project link, budgets, the billing export for analysis), "
        "errors (the C7 error budget) and quota (per-project API and resource quotas, raised before launch). GCP's "
        "discount forms: sustained-use, committed-use, Spot. Carbon as a cost-adjacent signal (region choice, the "
        "provider's footprint report)"], EV + "notes 0.1, 10.3, 10.4, 10.6 (three budgets)")
    f.ins_after("GAP-14", "Service accounts / managed identities and workload identity federation", [
        "Role types (basic, predefined, custom), conditional bindings (IAM Conditions), deny policies, and "
        "workforce federation for people beside workload federation for machines"],
        EV + "notes 0.5 (Cloud IAM, PCA 3.1)")
    f.ins_after("GAP-15", "Universal/cross-cloud: GitHub Actions, Jenkins, GitLab CI", [
        "Delivery performance: the four DORA metrics (deployment frequency, lead time for changes, change failure "
        "rate, failed-deployment recovery time), and platform engineering — a golden-path service template and "
        "preview environments destroyed on merge"], EV + "notes D0 (DORA four keys) and D6 (platform engineering)")
    f.ins_after("GAP-16", "Incident management, on-call, postmortem culture (blameless postmortems)", [
        "Proving reliability: load tests against the SLO, and chaos experiments (kill a revision, fail a push "
        "subscription, stall a queue) in non-production first, each with its error-budget cost written down"],
        EV + "notes 10.1 and PCA 4.3 (chaos / load)")
    f.ins_after("GAP-17", "Feature engineering: scaling, encoding categoricals, handling missing data", [
        "Applied problem families, as literacy: retrieve-then-rank recommenders (two-tower retrieval, learning to "
        "rank), bandits for exploration, time-series forecasting (seasonality, backtesting), fraud and anomaly "
        "detection with human review, and uplift measurement (why a lift claim needs a control group)"],
        EV + "notes 9c.0–9c.4, M.TS, M.CAUSAL")
