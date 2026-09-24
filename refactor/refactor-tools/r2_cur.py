"""R2 repairs for `Curriculum` (C-05, C-18…C-22, C-29, C-44…C-49, C-NEW-04/05, D3, D4, invariant 4).

D3 rule for this file: every original line survives. Lines are moved, get a heading marker (C-NEW-05), or get a
refactor note directly beneath them. The only in-place wording changes are the C-44 corrections, and their original
text is kept in the D3 archive.
"""
import re

from r2_common import DATE, PREFS_HEAD, note

VER = "Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`)"


def vnote(text):
    return f"> **{VER}:** {text} (verify live before scheduling)"


def fix(d, cid, needle, pairs, evidence, what):
    """in-place correction of one line; the original goes to the D3 archive. pairs: [(old, new), ...]"""
    i = d.one(needle)
    new = d.L[i]
    for old, rep in pairs:
        assert new.count(old) == 1, (cid, old, new)
        new = new.replace(old, rep)
    d.replace_line(cid, "correction", i, new, evidence, what=what)


def under(d, cid, cls, needle, lines, evidence, **kw):
    i = d.one(needle, **kw)
    d.insert_after(cid, cls, i, lines if isinstance(lines, list) else [lines], evidence)


# ------------------------------------------------------------------------------------------------ §0 text
REGISTER = [
    ("DNS mechanics", "`Curriculum` A5", "Primer SD-08 adds routing policies/TTL discipline; cyber NT-03/04 and "
     "DOS-02 add attacks"),
    ("HTTP", "`Curriculum` A5", "Primer SD-29 adds idempotency/HTTP/2/3; cyber PQ-S-04 adds the browser security "
     "preview"),
    ("Cookie attributes (`Domain`, `Secure`, `HttpOnly`, `SameSite`, `__Host-`)", "`Curriculum` A5 HTTP",
     "Cyber AU-01…04 adds attacks at A10"),
    ("TLS", "`Curriculum` A5 (mechanics) / A10 (formal)", "Primer SD-35 transit slice; cyber CR-11/12, NT-08"),
    ("Load balancing, reverse proxy", "`Curriculum` A5 / C3", "Primer SD-10/11; cyber NT-07, DOS-01"),
    ("Rate limiting", "Cyber AB-01 (algorithms + abuse)", "Primer Q22 is the design exercise and recalls AB-01"),
    ("Caching", "Primer SD-26/27", "Cyber DOS-08 (stampede as an attack); SQL OD-09 (read path)"),
    ("SQL injection / parameterisation", "SQL SL-13 (the SQL mechanics)",
     "Cyber WA-05 (attacker model across the whole injection family)"),
    ("Field / column encryption", "Cyber CR-17 (the cryptography)", "SQL SL-13 `pgcrypto` syntax"),
    ("Backup/restore", "SQL OD-04 (runbook) + N2.3", "Cyber IR-07 (ransomware integrity)"),
    ("2PC / Saga / outbox", "`Curriculum` A9 (theory)", "SQL CS-07 + SL-10 (SQL); design-patterns ARCH-11 (shape)"),
    ("Pub/Sub", "`Curriculum` A7", "Primer SD-28; design-patterns DP-14 (Observer)"),
    ("Shared responsibility", "`Curriculum` B1", "Cyber PQ-S-03, CM-01"),
    ("Least privilege / IAM", "`Curriculum` B5", "Primer SD-35; cyber CL-03…05, AU-14"),
    ("Floating point", "M5", "SQL PQ-03 (decimal semantics)"),
    ("Discrete-math foundations of relations", "M1", "SQL PQ-01/02, RT-01"),
    ("Number theory for cryptography", "M1", "Cyber CR-01…10"),
    ("Security checklist (encrypt in transit/at rest, XSS, SQLi, least privilege)",
     "Distributed per C-28: `Curriculum` A5/A10/B5 + cyber modules",
     "Primer SD-35 is an index module that points to each owner; its lab is shared with WA-05/SL-13"),
    ("Cache stampede / thundering herd", "Primer SD-27 (mechanics: locking, request coalescing, TTL jitter; primer "
     "\"my addition\")", "Cyber DOS-08 (adversarially triggered stampede)"),
    ("Tail latency, percentiles, hedged requests", "M6 (the math: order statistics, fan-out amplification)",
     "Primer SD-03/SD-38c (design levers: timeouts, hedging, replicas); `Curriculum` C6/C7 (alerting/SLOs)"),
    ("Little's law", "M6 (statement + proof sketch)", "Primer SD-03/SD-28 (sizing checks, e.g. 400 rps × 250 ms); "
     "the A2 slice (`primer-binding-table.md`)"),
    ("CAP / PACELC", "`Curriculum` A8 (CAP statement) → A9 (formal limits, PACELC)",
     "Primer SD-04/SD-05 (per-dataset choice, GCP store mapping)"),
    ("Consistent hashing", "U2 (analysis: expected movement 1/N, virtual nodes, load bounds)",
     "Primer SD-38a (sharding/rebalancing design); A4 ring slice"),
    ("MapReduce / scatter-gather", "A9 (distributed computation model)",
     "Primer SD-38b/c, SX-08 (job patterns); `Curriculum` V-DATA (Dataflow/Dataproc)"),
    ("CRDTs, operational transform", "A9 deepening", "Primer Q04 (Google Docs design problem)"),
    ("Vector clocks, quorums, gossip", "A9 deepening", "Primer Q05 (Redis-like KV design problem), SD-39 papers"),
    ("Heavy hitters / sketches / approximate counting", "U2 (randomized algorithms)",
     "Primer Q16/Q18 (design); SQL AN-04 (SQL approximation)"),
    ("Unique ID generation (Base62, Snowflake)", "Primer SX-02/Q17",
     "M1 (counting, birthday bound for collisions); A1 recall (bit layout)"),
    ("Garbage collection", "U4 (memory management)", "Primer Q21 (design problem); SX-04 (data GC/TTL)"),
    ("Event sourcing", "Design-patterns ARCH-10 (shape) + A9 (theory)",
     "Primer Q23 (stock exchange design); SQL IR/audit designs"),
    ("Credential storage & replay", "Cyber CR-13 (password KDFs) + CR-17/PV-03 (tokenization/encryption for "
     "replayable secrets)", "Primer P04 (design context) + SD-35 check question"),
    ("OOD problems O01–O07", "Primer (problems)",
     "Design-patterns (principles and patterns they exercise, C-34); A4 recall"),
    ("Interview/design method, back-of-the-envelope", "Primer SD-00", "Track S1–S3 recall it; they never restate it "
     "(C-31)"),
    ("Scaling evolution (single box → millions)", "Primer P08 + SX-12",
     "Northstar milestones cite P08 steps (C-32); Track S4/S9 recall"),
    ("Terraform labs", "Primer TF-1…TF-7 (P08/P01/P07 infra)",
     "SQL TF-DB*; Northstar reuses TF IDs rather than duplicating"),
    ("Real-world architecture papers (Dynamo, Bigtable, Spanner, GFS, Chubby, MapReduce, Dapper, Kafka, "
     "ZooKeeper…)", "Primer SD-39 / §6.4 (index)",
     "A9 deepening and the university alignment appendix cite the same papers; the reading list lives once, in the "
     "primer"),
]

S01 = [
    "### 0.1 The course files and the companion stitch rule",
    "",
    f"*Refactor-authored ({DATE}, C-01, C-NEW-04).* This roadmap is the **only parent**. Every companion names it "
    "`Curriculum` and binds its modules to the IDs below. The files:",
    "",
    "- `Curriculum` (this file) — order, cert timing, Lab Reality and track structure.",
    "- `system-design-primer-companion.md` — the system-design layer (SD, SX, P, O, Q, TF). Its bindings are "
    "generated from `primer-binding-table.md`.",
    "- `sql-databases-companion.md` — SQL, relational theory and engine internals. It owns the engine slices "
    "DB-1…DB-10 (C-05).",
    "- `design-patterns-companion.md` — OOP design theory, patterns and architecture styles (A7, A9).",
    "- `cloud-cybersecurity-companion.md` — security, attacks and cryptography.",
    "- `northstar-reference-app.md` — Track N, the one running reference application (sections `Nx.y`). R2 creates "
    "its skeleton; R9 authors it.",
    "- `session-progress-ledger.md` — the learner's state; it mirrors the inline boxes, which are authoritative.",
    "",
    "Each companion's §2 lists what it binds to each module. When a module is taught, every bound companion ID is "
    "taught in the same session, once, by its owner (§0.3), in the order §0.4 gives. The cybersecurity companion's "
    "original stitch block, first added to this file on 2026-09-22 between A10 and A11, now sits here unchanged:",
    "",
]

S03_HEAD = [
    "### 0.3 Suite overlap and ownership register",
    "",
    f"*Refactor-authored ({DATE}, §7 of the refactor prompt; C-17, C-36).* When two files touch the same concept, "
    "the **owner** teaches it and the others only **add**. Later sessions recall it in one line. Each companion's "
    "own overlap table is its slice of this register; on a conflict this register wins.",
    "",
    "| Concept | Owner | Adds |",
    "|---|---|---|",
]

S04 = [
    "### 0.4 Suite Teaching Contract",
    "",
    f"*Refactor-authored ({DATE}, C-29, C-47, C-53, C-54, C-55, C-69, C-70, C-72, C-73, C-75).* One contract for "
    "every file. Each companion keeps its own §0.3 session text and points here. When two rules conflict, the higher "
    "one wins: (1) the learner's explicit instruction in the current chat · (2) the ledger §5 preferences (§0.2) · "
    "(3) the refactor invariants · (4) this file on order, cert timing and Lab Reality · (5) the owning companion on "
    "its content (§0.3) · (6) the companions' defaults · (7) `learn-SKILL.md` defaults.",
    "",
    "**0.4.1 Rhythm.**",
    "",
    "- One concept per turn, at full depth. New material is taught by direct explanation; procedures by worked, "
    "parallel examples.",
    "- Every turn carries exactly one focused question, embedded in the teaching. Diagnosis happens through those "
    "checks; there is no separate probing (ledger §5 wins over the skill's calibrating question, C-70). A turn may "
    "be as long as one concept needs.",
    "- Correction style: confirm the correct part explicitly, then sharpen the imprecise part by naming the exact "
    "mechanism. No false praise. Hold the line under \"just tell me\"; give a foothold when the learner is "
    "genuinely stuck.",
    "- Overrides (C-75): the learner may skip (after passing the skip-test), jump, or go hands-on. Every override is "
    "recorded in the ledger so the prerequisite check can flag what was skipped.",
    "",
    "**0.4.2 Suite Session Protocol (C-29).** When several files bind to one module, the session runs:",
    "",
    "1. **Anchor** — list the bound IDs from *all* files (each companion's §2; the primer's from "
    "`primer-binding-table.md`).",
    "2. **Concept** — taught once, by the owner in §0.3.",
    "3. **Layers**, in fixed order: system design (primer) → SQL/engine → patterns → attacker/crypto (cyber).",
    "4. **GCP lens.**",
    "5. **One Numbers step** for the whole session.",
    "6. **One application item**: a primer micro-problem *or* a companion exercise card, never both for the same "
    "concept.",
    "7. **Checks**, woven in per ledger §5.",
    "8. **Close**, ticking boxes in every file (§0.4.8).",
    "",
    "**0.4.3 Exercise progression (C-54).** The first five rungs of the ten-rung ramp (anchor, vocabulary, "
    "representation, core move, worked illustration) are the teaching turns. Exercises then climb, one item per "
    "turn, advancing only when the current rung is passed: basic unseen check → routine variation → mixed transfer "
    "(the new idea plus exactly two earlier mastered ideas) → top-rung challenge → reflection (the learner explains "
    "back or invents an example).",
    "",
    "**0.4.4 Predict → run → discrepancy (C-53).** Every exercise with a result shape, row count, plan shape, "
    "isolation outcome or attack outcome starts with a one-line prediction. Then run. A wrong prediction is recorded "
    "in the ledger and taught from.",
    "",
    "**0.4.5 Mastery states.** Every ID is `not-started` → `in-progress` → `taught` (explained, first check "
    "answered) → `mastered` (passed a rung-3 or rung-4 item, or the skip-test). It may also be `shaky` (missed a "
    "check after teaching), `unverified` (claimed done without evidence) or `sliced` (only a named slice taught). "
    "Taught and mastered IDs get one-question recalls woven into later relevant sessions at about +1, +3, +7 and "
    "+21 sessions; a missed recall sets `shaky` and re-teaches only the gap. The misconception register lives in the "
    "ledger; checks probe each entry until two consecutive correct answers retire it.",
    "",
    "**0.4.6 Anchoring and suite-wide Prop Lock (C-55).** No term, product or control is used in an explanation, "
    "example or check unless it is anchored: taught this session, or at least `taught` on the ledger. A "
    "named-but-not-taught mention is allowed only when labelled \"we'll cover this in X\". A check that relies on "
    "unanchored terms is invalid: fix the check; don't mark the learner shaky.",
    "",
    "**0.4.7 Check questions and exercise pre-flight.** A check tests mechanism or application, asks one thing "
    "(C-69: split a multi-part check across turns), is answerable from anchored material, has a written expected "
    "answer and at least one expected wrong answer in the owning file's keys, is precision-sensitive, and is never "
    "answered by the tutor in the same turn. Before issuing any exercise the tutor checks: internal consistency "
    "(for example, a CNAME never points at an IP) · every term anchored · exactly one question · the answer "
    "derivable from what was taught · any numbers computed. An error found later is corrected openly in the next "
    "turn and logged in `errata.md`.",
    "",
    "**0.4.8 Pacing, checkpoints and session close (C-72, C-73).** Each module is budgeted at roughly 3–5 concepts "
    "per session at full depth; an over-budget module is split into teaching blocks (C-49). The budget is a plan, "
    "never a reason to compress depth. A problem or checkpoint runs only when all its must-know IDs are at least "
    "`taught`, and it introduces at most one new concept. Every session ends by: (1) marking every ID bound to the "
    "session taught / sliced / deferred-with-reason / recalled (nothing left unmarked); (2) updating mastery states "
    "and the recall schedule; (3) updating the misconception register; (4) adding any errata; (5) emitting a ledger "
    "delta block (and a full ledger every 5th session or on request); (6) naming the exact resume point and any "
    "open question, verbatim.",
    "",
]

S05 = [
    "### 0.5 Lab Safety",
    "",
    f"*Refactor-authored ({DATE}, C-47, C-53).* One rule set for every file; it unifies the cybersecurity "
    "companion's rule 10, the SQL companion's rule 10 and the Lab Reality paragraph above.",
    "",
    "1. **Hard bans:** no scanning of third parties; no malware; no live DDoS; no credential stuffing against real "
    "accounts; fixtures on localhost or disposable projects only; crypto through vetted libraries only.",
    "2. **Money and time:** local first (Docker Postgres, local fixtures). Credit-using services are created for one "
    "lab and destroyed the same day, with a budget alert set before the first apply.",
    "3. **Secrets and data:** never put a password, key or real customer data in a query, a prompt or a course file. "
    "Lab data is synthetic.",
    "4. **The workplace console is read-only:** look, never create or change.",
    "5. **Every lab carries a Lab Reality tag:** `[free-tier]` · `[credit ~$X]` · `[plan-only]` · `[paper]` · "
    "`[local]`.",
    "",
]

A7_BLOCKS = note("C-49", "A7 binds several dozen suite concepts, so it is taught as ordered teaching blocks. These "
                 "are sessions, not new modules; the module ID stays A7. A7.1 client-server and API styles (+ SD-32…"
                 "SD-34) · A7.2 async and queues (+ SD-28) · A7.3 OOP foundations + SOLID · A7.4 GRASP + creational "
                 "patterns · A7.5 structural patterns · A7.6 behavioral patterns · A7.7 architecture styles + DDD "
                 "(ARCH-01…ARCH-08) · A7.8 API authentication/authorization + attacks · A7.9 abuse and rate limits · "
                 "A7.10 S1–S2 · A7.11 N0 · A7.12 checkpoints. A5, A8 and A10 get the same split in R4, from the "
                 "§0.4.8 pacing budget.")

RESERVED = [
    "### Reserved tracks M, U, S and N (stubs; authored in R4 and R9)",
    "",
    f"*Refactor-authored ({DATE}).* The companions' foreign anchors were rebound to these IDs by the §6 crosswalks "
    "(`crosswalk.md`). Each ID is reserved here with its scope; the modules themselves are written in R4 (M, U, S) "
    "and R9 (N). Nothing here is teaching content yet.",
    "",
    "| ID | Title | Scope (what the rebound references need) |",
    "|---|---|---|",
    "| M1 | Discrete Mathematics & Proof | logic, proof techniques, sets and relations, counting, graphs, elementary "
    "number theory |",
    "| M2 | Linear Algebra | rigorous pass on A2 |",
    "| M3 | Calculus | rigorous pass on A2 |",
    "| M4 | Probability & Statistics | rigorous pass on A2 |",
    "| M5 | Numerical Methods & Floating Point | IEEE 754, rounding, decimal vs binary |",
    "| M6 | Information Theory & Performance Modeling | queueing, Little's law, tail latency |",
    "| U1 | Computer Architecture & Systems Programming | machine-level representation, memory hierarchy |",
    "| U2 | Algorithms: Design & Analysis | rigorous pass on A4 |",
    "| U3 | Theory of Computation | automata, grammars, decidability |",
    "| U4 | Programming Languages & Paradigms | paradigms, types, memory management |",
    "| U5 | Concurrency & Parallel Computing | races, locks, deadlock, memory models |",
    "| U6 | Software Engineering & Testing | requirements, testing theory, specification |",
    "| U7 | Professional Practice, Ethics & Law | ethics, privacy law literacy, licensing |",
    "| S1 | Requirements & quality attributes | Track S — System Architecture Design Studio |",
    "| S2 | Architecture documentation | views, C4, ADRs, the HLD/LLD contract and NFR tables |",
    "| S3 | Capacity & performance engineering | |",
    "| S4 | Reliability architecture | |",
    "| S5 | Data architecture | |",
    "| S6 | Security architecture | threat-model-driven design |",
    "| S7 | Integration & event-driven architecture | |",
    "| S8 | Migration & modernization | |",
    "| S9 | Cost architecture & unit economics | |",
    "| S10 | Architecture evaluation | |",
    "| S11 | Case-study studio | |",
    "| N0…N12 | Northstar reference application | milestones and sections `Nx.y` in `northstar-reference-app.md` |",
    "",
]

V_IDS = [
    ("V-COMP", "Compute:"), ("V-STOR", "Storage/DB:"), ("V-NET", "Networking:"), ("V-DATA", "Data/Analytics:"),
    ("V-AI", "AI/ML:"), ("V-SEC", "Security:"), ("V-OPS", "Ops/DevOps:"),
]

# cert title line prefix → (box label, Lab Reality line, D4 note or None)
CERTS = [
    ("1. Professional Cloud Architect (PCA)", "PCA",
     "`[free-tier]` Compute Engine / Cloud Run / Cloud Storage builds · `[plan-only]` multi-region and hybrid "
     "designs · `[paper]` the published case studies",
     None),
    ("2. Professional Machine Learning Engineer (PMLE)", "PMLE",
     "`[local]` notebooks · `[credit ~$X]` timeboxed Vertex AI training/prediction (Part V note) · `[plan-only]` "
     "large training runs", None),
    ("3. Data Engineer", "Professional Data Engineer",
     "`[free-tier]` Pub/Sub and the BigQuery sandbox `(verify)` · `[credit ~$X]` short Dataflow runs · "
     "`[plan-only]` Dataproc/Composer at scale", "Active; a branding update is pending."),
    ("4. Cloud Developer", "Professional Cloud Developer",
     "`[free-tier]` Cloud Run, Cloud Functions, Firestore · `[credit ~$X]` Cloud Build / Cloud Deploy beyond the "
     "free quota `(verify)`", "Active; its own page is live and registration is open, although it is missing from "
     "the certification index page's rendered list."),
    ("5. Cloud DevOps Engineer", "Professional Cloud DevOps Engineer",
     "`[free-tier]` Cloud Build, Cloud Monitoring/Logging · `[credit ~$X]` a short-lived GKE cluster", None),
    ("6. Cloud Security Engineer", "Professional Cloud Security Engineer",
     "`[free-tier]` IAM and firewall rules · `[credit ~$X]` Cloud KMS keys `(verify)` · `[plan-only]` VPC Service "
     "Controls perimeters and organization policies (they need an organization)", None),
    ("7. Cloud Network Engineer", "Professional Cloud Network Engineer",
     "`[local]` packet labs · `[credit ~$X]` small VPC + load-balancer labs destroyed the same day · `[plan-only]` "
     "Interconnect / HA VPN designs", None),
    ("8. Cloud Database Engineer", "Professional Cloud Database Engineer",
     "`[local]` Postgres (SQL companion lab kit) · `[credit ~$X]` Cloud SQL destroyed the same day · `[plan-only]` "
     "Spanner and AlloyDB", "Active; a branding update is pending. Guide weights: design ~32%, manage ~25%, "
     "migrate ~23%, deploy ~20%."),
    ("9. Security Operations Engineer", "Professional Security Operations Engineer",
     "`[paper]` detection engineering · `[local]` log fixtures · `[plan-only]` Google SecOps, an enterprise product "
     "`(verify)` trial availability", "Active. Six sections: platform operations 14, data management 14, threat "
     "hunting 19, detection engineering 22, incident response 21, observability 10."),
    ("10. Agentic Architect (Beta → GA)", "Agentic Architect",
     "`[local]` ADK agents · `[credit ~$X]` model API calls beyond the free quota `(verify)`",
     "Still in beta, open until Sept 30, 2026. The exam is 3 hours: about 80 multiple-choice questions, then labs in "
     "Google Skills. Five sections, with custom agents at about 33%. The guide names ADK, A2A and **MCP**; it does "
     "**not** name \"Agent Registry\" or \"Agent Gateway\"."),
    ("1. Solutions Architect – Professional (SAP-C02)", "AWS SAP",
     "`[free-tier]` single-account labs · `[plan-only]` Organizations / multi-account Terraform",
     "Domain weights 26/29/25/20 confirmed. **SAP-C02 is being replaced:** SAP-C03 registration opens Oct 27, 2026, "
     "and the last day for SAP-C02 is Nov 17, 2026."),
    ("2. DevOps Engineer – Professional (DOP-C02)", "AWS DOP",
     "`[free-tier]` CodeBuild/CodePipeline within the free quota `(verify)` · `[plan-only]` the rest",
     "Active. Six domains, 22/17/15/15/14/17. The Korean-language exam retires after Dec 31, 2026."),
    ("3. Generative AI Developer – Professional (AIP-C01)", "AWS AIP",
     "`[local]` RAG prototypes · `[credit ~$X]` Bedrock calls (no free tier assumed; `(verify)`)",
     "Active. Five domains: FM integration & data 31, implementation 26, AI safety/governance 20, efficiency 12, "
     "testing 11."),
    ("4. Security – Specialty (SCS-C03)", "AWS SCS",
     "`[free-tier]` IAM and KMS basics · `[plan-only]` organization-level controls",
     "Weights confirmed. The last domain is named **\"Security Foundations and Governance\" (14%)**, not "
     "\"Management & Security Governance\"."),
    ("5. Advanced Networking – Specialty (ANS-C01)", "AWS ANS",
     "`[local]` BGP labs in containers · `[plan-only]` Direct Connect and Transit Gateway",
     "Retiring: last exam day Dec 31, 2026; no new certifications are issued after retirement. Domains 30/26/20/24."),
    ("1. Solutions Architect Expert (AZ-305)", "Azure AZ-305",
     "`[paper]` design documents · `[free-tier]` small always-free services",
     "Confirmed: skills as of Apr 17, 2026; the prerequisite is Azure Administrator Associate."),
    ("2. DevOps Engineer Expert (AZ-400)", "Azure AZ-400",
     "`[free-tier]` Azure DevOps / GitHub Actions minutes `(verify)`",
     "Skills revised as of **July 27, 2026**; build/release pipelines is 50–55%."),
    ("3. Cybersecurity Architect Expert (SC-100)", "Azure SC-100",
     "`[paper]` Zero Trust designs · `[free-tier]` Entra ID basics",
     "The study guide now shows skills measured **as of Oct 21, 2026** (an upcoming revision). The AZ-500 "
     "prerequisite is now listed as **\"Cloud and AI Security Engineer Associate\"**."),
]


def build_curriculum(d, prefs):
    E44 = ("C-44 + D4: Parts V–VII list 18 certs (10 GCP + 5 AWS + 3 Azure; cert-verification.md, all 18 live on "
           "2026-09-24). D4 (learner, rung 1) settles the count at 18, so the open question C-44 asked for is closed.")
    # ---------- C-44 corrections (the only in-place wording changes) ----------
    fix(d, "C-44", "Scope, honestly. Fifteen professional-tier",
        [("Fifteen professional-tier", "Eighteen professional-tier"), ("cert #2 through #15", "cert #2 through #18")],
        E44, "§0 scope paragraph")
    fix(d, "C-44", "tested, in some form, on every single one of your fifteen certs",
        [("your fifteen certs", "your eighteen certs")], E44, "\"Why this order\" paragraph")
    fix(d, "C-44", "Phase 5  Remaining GCP Professional certs", [("not all 8)",
        "not all 7; Agentic Architect is Phase 8)")],
        "C-44: after PCA and PMLE, 8 GCP certs remain only if Agentic Architect is counted, but Phase 8 schedules it "
        "separately (Curriculum Phase 8 line)", "Phase 5 line")

    # ---------- C-NEW-05: markdown headings for the native structure ----------
    EH = "C-NEW-05: Curriculum's native structure is plain text; headings make it addressable (no words changed)"
    heads = [(r"^The Consolidated Cloud Mastery Curriculum$", "# "), (r"^0\. Read this first$", "## "),
             (r"^1\. The Phase Plan$", "## "), (r"^PART [IVX]+ — ", "## "), (r"^[ABCD]\d{1,2}\. \S", "### ")]
    n = 0
    for i, l in enumerate(d.L):
        for pat, mark in heads:
            if re.match(pat, l):
                d.replace_line("C-NEW-05", "anchor-rewrite", i, mark + l, EH, archive=False)
                n += 1
                break
    assert n == 1 + 2 + 10 + 27, n

    # ---------- phase-plan diagram: fence it so markdown keeps its alignment ----------
    s = d.one("Phase 0  Universal Fundamentals (Track A)")
    e = d.one("Phase 8  Agentic Architect (GA)")
    d.insert("C-NEW-05", "append", e + 1, ["```text"], "fence the phase-plan diagram (no line changed)")
    d.insert("C-NEW-05", "append", s, ["```text"], "fence the phase-plan diagram (no line changed)")

    # ---------- C-NEW-04: move the cyber pointer block into §0.1 ----------
    b0 = d.one("## Companion — Cloud Cybersecurity (standalone)") - 2
    assert d.L[b0] == "---" and d.L[b0 + 10] == "---", (d.L[b0], d.L[b0 + 10])
    d.replace_line("C-NEW-04", "anchor-rewrite", b0 + 2, "#" * 2 + d.L[b0 + 2],
                   "C-NEW-04: demoted to sit under §0.1 (text unchanged)", archive=False)
    dest = d.one("## 1. The Phase Plan")
    d.move("C-NEW-04", b0, b0 + 11, dest, "C-NEW-04: the 2026-09-22 cyber stitch block moves into §0.1 (move, "
           "not delete; it split Part I between A10 and A11)", prefix=S01, suffix=[""])
    under(d, "C-17", "append", "That companion is **standalone** (no other companion files).",
          ["", note("C-17", "\"Standalone\" is superseded: the companion has self-contained content, and ownership "
                    "is shared per the suite overlap register (§0.3). Its §2 bindings now use this file's IDs (§6.2 "
                    "crosswalk).")], "C-17 resolution")
    under(d, "C-47", "append", "**Lab safety:** local vulnerable-by-design fixtures only",
          ["", note("C-47", "the suite-wide rule set is §0.5.")], "C-47: Lab Safety unified in §0.5")

    # ---------- §0.2–§0.5 ----------
    dest = d.one("## 1. The Phase Plan")
    reg = [f"| {c} | {o} | {a} |" for c, o, a in REGISTER]
    block = (["### 0.2 " + PREFS_HEAD, ""] + prefs + [""] + S03_HEAD + reg + [""] + S04 + S05)
    d.insert("INV-4/§7/C-47", "new-content", dest, block,
             "invariant 4 (ledger §5 copied unchanged); §7 register → §0.3; C-29/C-47 contract → §0.4; C-47 Lab "
             "Safety → §0.5")

    # ---------- C-18: first-pass scope notes (caveats kept verbatim) ----------
    under(d, "C-18", "append", "Calculus intuition: derivatives as \"rate of change,\"",
          note("C-18", "First-pass scope: this intuition pass is the first pass and is complete as written. The "
               "rigorous passes follow in M2 (linear algebra), M3 (calculus) and M4 (probability & statistics)."),
          "C-18: caveat kept; rigorous passes follow in M1–M4")
    under(d, "C-18", "append", "Sorting/searching intuition (enough to reason",
          note("C-18", "First-pass scope: A4 stays at engineering-practical depth. The rigorous pass (proofs, "
               "recurrences, and implementing a balanced search tree) is U2."),
          "C-18: caveat kept; rigorous pass follows in U2")

    # ---------- C-20: status lines ----------
    status = ("Status as of 2026-09-24 (C-20, D2): the course is a fresh start, so this sentence is still true. "
              "The live position is kept in `session-progress-ledger.md`.")
    under(d, "C-20", "append", "→ We start here, today, below.", note("C-20", status), "C-20 + D2")
    under(d, "C-20", "append", "We start with A1: Digital Logic & Data Representation below, right now.",
          ["", note("C-20", status)], "C-20 + D2")
    under(d, "C-20", "append", "Agentic Architect (Beta) — registration is open now",
          vnote("the beta is still open until Sept 30, 2026. The GA date is not announced; recheck after the window "
                "closes."), "C-20 + D4")
    under(d, "C-20", "append", "One item on your list is confirmed accurate as stated: AWS Advanced Networking",
          vnote("ANS-C01's last exam day is still Dec 31, 2026, with no successor."), "C-20 + D4")
    under(d, "C-20", "append", "the cert itself is optional depending on how our timeline looks by mid-2026",
          note("C-20", "mid-2026 has passed. The ANS-C01 decision is due before its last exam day, Dec 31, 2026 "
               "(verified 2026-09-24; verify live)."), "C-20: time-bound text annotated, not rewritten")

    # ---------- C-21: TLS split ----------
    under(d, "C-21", "append", "TLS/SSL: the handshake, certificates, certificate authorities",
          note("C-21", "TLS split: A5 teaches the handshake mechanics, certificates and CAs, plus a minimal "
               "public-key intuition bridge (what a key pair does, what a signature proves, why DH gives a shared "
               "secret). A10 formalizes the cryptographic primitives underneath and recalls A5 in one line."),
          "C-21 + C-14")
    under(d, "C-21", "append", "The TLS handshake in detail, PKI and certificate chains",
          note("C-21", "A10 formalizes what A5 taught at mechanism level (see the A5 note); it does not re-teach "
               "the handshake."), "C-21 + C-14")

    # ---------- C-05: A8 engine-slice pointer ----------
    under(d, "C-05", "append", "Data warehousing basics: OLTP vs OLAP, star schemas",
          "Engine slices DB-1…DB-10 (bag relations, slotted page, buffer clock sweep, B-tree + inverted index, "
          "iterators + spill, histograms, MVCC visibility + deadlock detection, mini-WAL): owned and taught by "
          "`sql-databases-companion.md` §4.0 inside the A8 sessions *(added by the refactor, C-05)*",
          "C-05: Curriculum A8 gets one outline bullet that points to the slices")

    # ---------- C-49: A7 teaching blocks ----------
    under(d, "C-49", "append", "API authentication patterns: API keys, OAuth 2.0, JWTs, service accounts",
          ["", A7_BLOCKS], "C-49 suggested order")

    # ---------- C-46: Track D Lab Reality; reserved tracks ----------
    i = d.one("Responsible AI: bias, fairness, explainability, safety evaluation")
    d.insert_after("C-46", "append", i, [
        "Lab Reality (Track D) *(added by the refactor, C-46)*: D1 `[local]` notebooks (scikit-learn) · D2 `[local]` "
        "small models on CPU, `[plan-only]` for large training · D3 `[local]` tracking and pipelines, "
        "`[free-tier]` Vertex AI pieces where a free tier exists `(verify)` · D4 `[local]` RAG and agent prototypes, "
        "`[credit ~$X]` timeboxed model API calls `(verify)`.", ""] + RESERVED,
        "C-46 (Track D Lab Reality); reserved M/U/S/N IDs so the §6 crosswalk targets resolve before R4")

    # ---------- C-22: Part V category IDs ----------
    i = d.one("Service map by category (the vocabulary we'll build fluency in)")
    rows = ["", f"*Category IDs (C-22, {DATE}).* Other files anchor to these IDs instead of the category names:", "",
            "| V-ID | Category (line below) |", "|---|---|"]
    end = d.one("Certification-by-certification breakdown")
    for v, c in V_IDS:
        d.one("^" + re.escape(c) + " ", regex=True, start=i, end=end)
        rows.append(f"| {v} | {c.rstrip(':')} |")
    d.insert_after("C-22", "append", i, rows + [""], "C-22: stable IDs for the Part V service-map categories")

    # ---------- C-45 boxes + C-46 cert Lab Reality + D4 notes ----------
    k = 0
    while k < len(d.L):
        m = re.match(r"^### ([ABCD]\d{1,2})\. ", d.L[k])
        if m:
            d.insert_after("C-45", "append", k, [f"- [ ] {m.group(1)} done"], "C-45: one inline box per module")
            k += 1
        k += 1
    for prefix, label, lab, ver in CERTS:
        i = d.one("^" + re.escape(prefix), regex=True)
        add = [f"- [ ] {label} passed",
               f"- **Lab Reality** *(added by the refactor, C-46)*: {lab}."]
        if ver:
            add.append(vnote(ver))
        d.insert_after("C-45/C-46/D4", "append", i, add, "C-45 box, C-46 Lab Reality, D4 verification")
    under(d, "D4", "append", "Format: 50 scenario-based questions, 2 hours, includes 4 published case studies",
          vnote("50–60 questions; 4 case studies are published and 2 appear per exam."), "D4 / cert-verification G1")
    under(d, "D4", "append", "Domains (verified): Designing (24%) · Provisioning (15%)",
          vnote("the live guide's weights are 25 / 17.5 / 17.5 / 15 / 12.5 / 12.5, under different section names. "
                "The line above keeps the 2026-09-16 reading."), "D4 / cert-verification G1")
    under(d, "D4", "append", "6 domains covering the full ML lifecycle: framing business problems",
          vnote("still 6 sections, renamed: low-code AI 13, data & models 16, scaling prototypes 21, serving 20, "
                "pipelines 18, monitoring 13. The exam moved from Vertex AI to the **Gemini Enterprise Agent "
                "Platform**."), "D4 / cert-verification G2")
    under(d, "D4", "append", "Lab Reality (AWS): Free tier covers EC2 t2/t3.micro",
          note("D4", "new AWS accounts since July 2025 get a credit-based free plan instead of the 12-month free "
               "tier described above (verify)."), "cert-verification.md, volatility items")

    # ---------- C-19: Track G ----------
    under(d, "C-19", "append", "we'll fold AZ-104-equivalent knowledge into Track G teaching",
          ["", note("C-19", "there is no Track G. AZ-104-equivalent knowledge folds into Phase 7 through B5 and "
                    "C-track recall, taught as the sub-block below."), "",
           "**AZ-104-equivalent sub-block** *(added by the refactor, C-19; Phase 7, before AZ-305)*: Entra ID and "
           "Azure RBAC (recall B5) · VNet, NSGs, Load Balancer and Azure DNS (recall A5 and Part VIII) · virtual "
           "machines and storage (recall B2, C1 and Part VIII) · Azure Monitor (recall C6) · governance with Azure "
           "Policy (recall B5, Part VIII). Check the topic list against the live AZ-104 guide `(verify)`."],
          "C-19 resolution")

    # ---------- C-48: Part IX as-of ----------
    under(d, "C-48", "append", "## PART IX — Time-Sensitive Notes Recap",
          note("C-48", "status as of 2026-09-24: the three notes below were re-checked that day "
               "(`cert-verification.md`). New dated items are in the Part V–VII verification notes. R4 moves every "
               "date-bearing line into `volatility-register.md` with a last-checked date."), "C-48")

    # ---------- Part X → §0.4 ----------
    under(d, "C-75", "append", "Go hands-on on something — I'll tell you honestly",
          ["", note("C-75", "these overrides are the suite-wide rule in §0.4.1; the session shape is §0.4.2.")],
          "C-75 + C-47")
    return d
