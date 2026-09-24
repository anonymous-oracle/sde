# Records for Curriculum.md (R2b, R2c and R4 build edits, 2026-09-24)

Refactor bookkeeping only, not course material. Decision D6 keeps provenance, the D3 archive and every line the build changed or removed (R2b; the R2c Go tie-ins; R4, rules R4-*) out of the course files; decision D3 keeps them here, verbatim. Each entry names the build journal number (outputs/r2b/journal.jsonl), the rule and the class.

**J1** · G0 · R2 in-file D3 archive, moved out whole

````text


---

## Pre-refactor text archive (D3)

*Refactor-authored section (2026-09-24).* Decision D3 says content may be re-arranged but never removed. Each block below is the exact pre-refactor text (after the §5 ID renames) of a line that R2 corrected or regenerated. It is kept for provenance only and is **not authoritative**; the live text above wins. Tooling excludes this section from ID and anchor checks.

**D3-01** · C-44 · §0 scope paragraph

```text
Scope, honestly. Fifteen professional-tier certifications, three providers, plus the full engineering stack underneath them, is not a weekend, a month, or even a semester. Treated seriously — with real understanding, not memorized dumps — this is 18–30 months of consistent study for someone starting from true fundamentals. I'm telling you this not to discourage you but so we plan like adults: we go in phases, we build real skill that transfers across providers (so cert #2 through #15 get progressively faster), and we don't burn your $300 GCP credit or your motivation in week one.
```

**D3-02** · C-44 · "Why this order" paragraph

```text
Why this order: everything in Phases 0–3 is provider-agnostic and is tested, in some form, on every single one of your fifteen certs. Front-loading it means each subsequent cert is 60–70% "same concepts, new console." GCP goes first because you named PCA/PMLE explicitly and have a workplace GCP account to look around in. AWS and Azure then go faster because you already know what a load balancer, an IAM policy, and a Kubernetes pod are — you're just learning new names and new console layouts for concepts you already own.
```

**D3-03** · C-44 · Phase 5 line

```text
Phase 5  Remaining GCP Professional certs (pick 2–4 that match your goals, not all 8)
```

````

**J2** · G3 · anchor-rewrite

````text
> **Refactor note (2026-09-24, C-17):** "Standalone" is superseded: the companion has self-contained content, and ownership is shared per the suite overlap register (§0.3). Its §2 bindings now use this file's IDs (§6.2 crosswalk).
````

**J3** · G3 · anchor-rewrite

````text
> **Refactor note (2026-09-24, C-47):** the suite-wide rule set is §0.5.
````

**J4** · G3 · anchor-rewrite

````text
> **Refactor note (2026-09-24, C-20):** Status as of 2026-09-24 (C-20, D2): the course is a fresh start, so this sentence is still true. The live position is kept in `session-progress-ledger.md`.
````

**J5** · G3 · anchor-rewrite

````text
> **Refactor note (2026-09-24, C-18):** First-pass scope: this intuition pass is the first pass and is complete as written. The rigorous passes follow in M2 (linear algebra), M3 (calculus) and M4 (probability & statistics).
````

**J6** · G3 · anchor-rewrite

````text
> **Refactor note (2026-09-24, C-18):** First-pass scope: A4 stays at engineering-practical depth. The rigorous pass (proofs, recurrences, and implementing a balanced search tree) is U2.
````

**J7** · G3 · anchor-rewrite

````text
> **Refactor note (2026-09-24, C-21):** TLS split: A5 teaches the handshake mechanics, certificates and CAs, plus a minimal public-key intuition bridge (what a key pair does, what a signature proves, why DH gives a shared secret). A10 formalizes the cryptographic primitives underneath and recalls A5 in one line.
````

**J8** · G3 · anchor-rewrite

````text
> **Refactor note (2026-09-24, C-49):** A7 binds several dozen suite concepts, so it is taught as ordered teaching blocks. These are sessions, not new modules; the module ID stays A7. A7.1 client-server and API styles (+ SD-32…SD-34) · A7.2 async and queues (+ SD-28) · A7.3 OOP foundations + SOLID · A7.4 GRASP + creational patterns · A7.5 structural patterns · A7.6 behavioral patterns · A7.7 architecture styles + DDD (ARCH-01…ARCH-08) · A7.8 API authentication/authorization + attacks · A7.9 abuse and rate limits · A7.10 S1–S2 · A7.11 N0 · A7.12 checkpoints. A5, A8 and A10 get the same split in R4, from the §0.4.8 pacing budget.
````

**J9** · G3 · anchor-rewrite

````text
> **Refactor note (2026-09-24, C-21):** A10 formalizes what A5 taught at mechanism level (see the A5 note); it does not re-teach the handshake.
````

**J10** · G3 · anchor-rewrite

````text
> **Refactor note (2026-09-24, C-20):** mid-2026 has passed. The ANS-C01 decision is due before its last exam day, Dec 31, 2026 (verified 2026-09-24; verify live).
````

**J11** · G3 · anchor-rewrite

````text
> **Refactor note (2026-09-24, D4):** new AWS accounts since July 2025 get a credit-based free plan instead of the 12-month free tier described above (verify).
````

**J12** · G3 · anchor-rewrite

````text
> **Refactor note (2026-09-24, C-19):** there is no Track G. AZ-104-equivalent knowledge folds into Phase 7 through B5 and C-track recall, taught as the sub-block below.
````

**J13** · G3 · anchor-rewrite

````text
> **Refactor note (2026-09-24, C-48):** status as of 2026-09-24: the three notes below were re-checked that day (`cert-verification.md`). New dated items are in the Part V–VII verification notes. R4 moves every date-bearing line into `volatility-register.md` with a last-checked date.
````

**J14** · G3 · anchor-rewrite

````text
> **Refactor note (2026-09-24, C-75):** these overrides are the suite-wide rule in §0.4.1; the session shape is §0.4.2.
````

**J15** · G3 · anchor-rewrite

````text
> **Refactor note (2026-09-24, C-20):** Status as of 2026-09-24 (C-20, D2): the course is a fresh start, so this sentence is still true. The live position is kept in `session-progress-ledger.md`.
````

**J16** · G4 · anchor-rewrite

````text
*Refactor-authored (2026-09-24, C-01, C-NEW-04).* This roadmap is the **only parent**. Every companion names it `Curriculum` and binds its modules to the IDs below. The files:
````

**J17** · G4 · anchor-rewrite

````text
*Refactor-authored (2026-09-24, §7 of the refactor prompt; C-17, C-36).* When two files touch the same concept, the **owner** teaches it and the others only **add**. Later sessions recall it in one line. Each companion's own overlap table is its slice of this register; on a conflict this register wins.
````

**J18** · G4 · anchor-rewrite

````text
*Refactor-authored (2026-09-24, C-29, C-47, C-53, C-54, C-55, C-69, C-70, C-71, C-72, C-73, C-74, C-75).* One contract for every file. Each companion keeps its own §0.3 session text and points here. When two rules conflict, the higher one wins: (1) the learner's explicit instruction in the current chat · (2) the ledger §5 preferences (§0.2) · (3) the refactor invariants · (4) this file on order, cert timing and Lab Reality · (5) the owning companion on its content (§0.3) · (6) the companions' defaults · (7) `learn-SKILL.md` defaults.
````

**J19** · G4 · anchor-rewrite

````text
*Refactor-authored (2026-09-24, C-47, C-53).* One rule set for every file; it unifies the cybersecurity companion's rule 10, the SQL companion's rule 10 and the Lab Reality paragraph above.
````

**J20** · G4 · anchor-rewrite

````text
Engine slices DB-1…DB-10 (bag relations, slotted page, buffer clock sweep, B-tree + inverted index, iterators + spill, histograms, MVCC visibility + deadlock detection, mini-WAL): owned and taught by `sql-databases-companion.md` §4.0 inside the A8 sessions *(added by the refactor, C-05)*
````

**J21** · G4 · anchor-rewrite

````text
Lab Reality (Track D) *(added by the refactor, C-46)*: D1 `[local]` notebooks (scikit-learn) · D2 `[local]` small models on CPU, `[plan-only]` for large training · D3 `[local]` tracking and pipelines, `[free-tier]` Vertex AI pieces where a free tier exists `(verify)` · D4 `[local]` RAG and agent prototypes, `[credit ~$X]` timeboxed model API calls `(verify)`.
````

**J22** · G4 · anchor-rewrite

````text
*Refactor-authored (2026-09-24).* The companions' foreign anchors were rebound to these IDs by the §6 crosswalks (`crosswalk.md`). Each ID is reserved here with its scope; the modules themselves are written in R4 (M, U, S) and R9 (N). Nothing here is teaching content yet.
````

**J23** · G4 · anchor-rewrite

````text
- **Lab Reality** *(added by the refactor, C-46)*: `[free-tier]` Compute Engine / Cloud Run / Cloud Storage builds · `[plan-only]` multi-region and hybrid designs · `[paper]` the published case studies.
````

**J24** · G4 · anchor-rewrite

````text
- **Lab Reality** *(added by the refactor, C-46)*: `[local]` notebooks · `[credit ~$X]` timeboxed Vertex AI training/prediction (Part V note) · `[plan-only]` large training runs.
````

**J25** · G4 · anchor-rewrite

````text
- **Lab Reality** *(added by the refactor, C-46)*: `[free-tier]` Pub/Sub and the BigQuery sandbox `(verify)` · `[credit ~$X]` short Dataflow runs · `[plan-only]` Dataproc/Composer at scale.
````

**J26** · G4 · anchor-rewrite

````text
- **Lab Reality** *(added by the refactor, C-46)*: `[free-tier]` Cloud Run, Cloud Functions, Firestore · `[credit ~$X]` Cloud Build / Cloud Deploy beyond the free quota `(verify)`.
````

**J27** · G4 · anchor-rewrite

````text
- **Lab Reality** *(added by the refactor, C-46)*: `[free-tier]` Cloud Build, Cloud Monitoring/Logging · `[credit ~$X]` a short-lived GKE cluster.
````

**J28** · G4 · anchor-rewrite

````text
- **Lab Reality** *(added by the refactor, C-46)*: `[free-tier]` IAM and firewall rules · `[credit ~$X]` Cloud KMS keys `(verify)` · `[plan-only]` VPC Service Controls perimeters and organization policies (they need an organization).
````

**J29** · G4 · anchor-rewrite

````text
- **Lab Reality** *(added by the refactor, C-46)*: `[local]` packet labs · `[credit ~$X]` small VPC + load-balancer labs destroyed the same day · `[plan-only]` Interconnect / HA VPN designs.
````

**J30** · G4 · anchor-rewrite

````text
- **Lab Reality** *(added by the refactor, C-46)*: `[local]` Postgres (SQL companion lab kit) · `[credit ~$X]` Cloud SQL destroyed the same day · `[plan-only]` Spanner and AlloyDB.
````

**J31** · G4 · anchor-rewrite

````text
- **Lab Reality** *(added by the refactor, C-46)*: `[paper]` detection engineering · `[local]` log fixtures · `[plan-only]` Google SecOps, an enterprise product `(verify)` trial availability.
````

**J32** · G4 · anchor-rewrite

````text
- **Lab Reality** *(added by the refactor, C-46)*: `[local]` ADK agents · `[credit ~$X]` model API calls beyond the free quota `(verify)`.
````

**J33** · G4 · anchor-rewrite

````text
- **Lab Reality** *(added by the refactor, C-46)*: `[free-tier]` single-account labs · `[plan-only]` Organizations / multi-account Terraform.
````

**J34** · G4 · anchor-rewrite

````text
- **Lab Reality** *(added by the refactor, C-46)*: `[free-tier]` CodeBuild/CodePipeline within the free quota `(verify)` · `[plan-only]` the rest.
````

**J35** · G4 · anchor-rewrite

````text
- **Lab Reality** *(added by the refactor, C-46)*: `[local]` RAG prototypes · `[credit ~$X]` Bedrock calls (no free tier assumed; `(verify)`).
````

**J36** · G4 · anchor-rewrite

````text
- **Lab Reality** *(added by the refactor, C-46)*: `[free-tier]` IAM and KMS basics · `[plan-only]` organization-level controls.
````

**J37** · G4 · anchor-rewrite

````text
- **Lab Reality** *(added by the refactor, C-46)*: `[local]` BGP labs in containers · `[plan-only]` Direct Connect and Transit Gateway.
````

**J38** · G4 · anchor-rewrite

````text
**AZ-104-equivalent sub-block** *(added by the refactor, C-19; Phase 7, before AZ-305)*: Entra ID and Azure RBAC (recall B5) · VNet, NSGs, Load Balancer and Azure DNS (recall A5 and Part VIII) · virtual machines and storage (recall B2, C1 and Part VIII) · Azure Monitor (recall C6) · governance with Azure Policy (recall B5, Part VIII). Check the topic list against the live AZ-104 guide `(verify)`.
````

**J39** · G4 · anchor-rewrite

````text
- **Lab Reality** *(added by the refactor, C-46)*: `[paper]` design documents · `[free-tier]` small always-free services.
````

**J40** · G4 · anchor-rewrite

````text
- **Lab Reality** *(added by the refactor, C-46)*: `[free-tier]` Azure DevOps / GitHub Actions minutes `(verify)`.
````

**J41** · G4 · anchor-rewrite

````text
- **Lab Reality** *(added by the refactor, C-46)*: `[paper]` Zero Trust designs · `[free-tier]` Entra ID basics.
````

**J42** · G5 · anchor-rewrite

````text
- `sql-databases-companion.md` — SQL, relational theory and engine internals. It owns the engine slices DB-1…DB-10 (C-05).
````

**J43** · G5 · anchor-rewrite

````text
| Interview/design method, back-of-the-envelope | Primer SD-00 | Track S1–S3 recall it; they never restate it (C-31) |
````

**J44** · G5 · anchor-rewrite

````text
| Scaling evolution (single box → millions) | Primer P08 + SX-12 | Northstar milestones cite P08 steps (C-32); Track S4/S9 recall |
````

**J45** · G5 · anchor-rewrite

````text
- Overrides (C-75): the learner may skip (after passing the skip-test), jump, or go hands-on. Every override is recorded in the ledger so the prerequisite check can flag what was skipped.
````

**J46** · G5 · anchor-rewrite

````text
**0.4.2 Suite Session Protocol (C-29).** When several files bind to one module, the session runs:
````

**J47** · G5 · anchor-rewrite

````text
**0.4.3 Exercise progression (C-54).** The first five rungs of the ten-rung ramp (anchor, vocabulary, representation, core move, worked illustration) are the teaching turns. Exercises then climb, one item per turn, advancing only when the current rung is passed: basic unseen check → routine variation → mixed transfer (the new idea plus exactly two earlier mastered ideas) → top-rung challenge → reflection (the learner explains back or invents an example).
````

**J48** · G5 · anchor-rewrite

````text
**0.4.4 Predict → run → discrepancy (C-53).** Every exercise with a result shape, row count, plan shape, isolation outcome or attack outcome starts with a one-line prediction. Then run. A wrong prediction is recorded in the ledger and taught from.
````

**J49** · G5 · anchor-rewrite

````text
**0.4.5 Mastery states (C-71).** Every ID is `not-started` → `in-progress` → `taught` (explained, first check answered) → `mastered` (passed a rung-3 or rung-4 item, or the skip-test). It may also be `shaky` (missed a check after teaching), `unverified` (claimed done without evidence) or `sliced` (only a named slice taught). Taught and mastered IDs get one-question recalls woven into later relevant sessions at about +1, +3, +7 and +21 sessions; a missed recall sets `shaky` and re-teaches only the gap. The misconception register lives in the ledger; checks probe each entry until two consecutive correct answers retire it.
````

**J50** · G5 · anchor-rewrite

````text
**0.4.6 Anchoring and suite-wide Prop Lock (C-55).** No term, product or control is used in an explanation, example or check unless it is anchored: taught this session, or at least `taught` on the ledger. A named-but-not-taught mention is allowed only when labelled "we'll cover this in X". A check that relies on unanchored terms is invalid: fix the check; don't mark the learner shaky.
````

**J51** · G5 · anchor-rewrite

````text
**0.4.7 Check questions and exercise pre-flight.** A check tests mechanism or application, asks one thing (C-69: split a multi-part check across turns), is answerable from anchored material, has a written expected answer and at least one expected wrong answer in the owning file's keys, is precision-sensitive, and is never answered by the tutor in the same turn. Before issuing any exercise the tutor checks: internal consistency (for example, a CNAME never points at an IP) · every term anchored · exactly one question · the answer derivable from what was taught · any numbers computed. The tutor is precise about mechanisms and says explicitly when unsure (C-74). An error found later is corrected openly in the next turn and logged in `errata.md`.
````

**J52** · G5 · anchor-rewrite

````text
**0.4.8 Pacing, checkpoints and session close (C-72, C-73).** Each module is budgeted at roughly 3–5 concepts per session at full depth; an over-budget module is split into teaching blocks (C-49). The budget is a plan, never a reason to compress depth. A problem or checkpoint runs only when all its must-know IDs are at least `taught`, and it introduces at most one new concept. Every session ends by: (1) marking every ID bound to the session taught / sliced / deferred-with-reason / recalled (nothing left unmarked); (2) updating mastery states and the recall schedule; (3) updating the misconception register; (4) adding any errata; (5) emitting a ledger delta block (and a full ledger every 5th session or on request); (6) naming the exact resume point and any open question, verbatim.
````

**J53** · G5 · anchor-rewrite

````text
| Security checklist (encrypt in transit/at rest, XSS, SQLi, least privilege) | Distributed per C-28: `Curriculum` A5/A10/B5 + cyber modules | Primer SD-35 is an index module that points to each owner; its lab is shared with WA-05/SL-13 |
````

**J54** · G5 · anchor-rewrite

````text
**0.4.7 Check questions and exercise pre-flight.** A check tests mechanism or application, asks one thing (C-69: split a multi-part check across turns), is answerable from anchored material, has a written expected answer and at least one expected wrong answer in the owning file's keys, is precision-sensitive, and is never answered by the tutor in the same turn. Before issuing any exercise the tutor checks: internal consistency (for example, a CNAME never points at an IP) · every term anchored · exactly one question · the answer derivable from what was taught · any numbers computed. The tutor is precise about mechanisms and says explicitly when unsure. An error found later is corrected openly in the next turn and logged in `errata.md`.
````

**J55** · G5 · anchor-rewrite

````text
| OOD problems O01–O07 | Primer (problems) | Design-patterns (principles and patterns they exercise, C-34); A4 recall |
````

**J56** · G5 · anchor-rewrite

````text
- Every turn carries exactly one focused question, embedded in the teaching. Diagnosis happens through those checks; there is no separate probing (ledger §5 wins over the skill's calibrating question, C-70). A turn may be as long as one concept needs.
````

**J57** · G9 · anchor-rewrite

````text
### 0.2 Learner teaching preferences (binding; copied unchanged from session-progress-ledger.md §5, invariant 4)
````

**J58** · G9 · anchor-rewrite

````text
- When companion-file content (system-design-primer, SQL, design-patterns) overlaps a `Curriculum` module, **teach it once, stitched into the same session** — never as a separate pass, per each companion's own §0.2 stitching rules.
````

**J59** · G9 · anchor-rewrite

````text
- If a companion file references module IDs that don't exist in `Curriculum` (as `sql-databases-companion.md` does), **say so plainly rather than forcing a silent, possibly-wrong mapping** — this was well received when done for the SQL companion.
````

**J386** · CUR-1 · anchor-rewrite

````text
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** the beta is still open until Sept 30, 2026. The GA date is not announced; recheck after the window closes. (verify live before scheduling)
````

**J387** · CUR-1 · anchor-rewrite

````text
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** ANS-C01's last exam day is still Dec 31, 2026, with no successor. (verify live before scheduling)
````

**J388** · CUR-1 · anchor-rewrite

````text
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** 50–60 questions; 4 case studies are published and 2 appear per exam. (verify live before scheduling)
````

**J389** · CUR-1 · anchor-rewrite

````text
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** the live guide's weights are 25 / 17.5 / 17.5 / 15 / 12.5 / 12.5, under different section names. The line above keeps the 2026-09-16 reading. (verify live before scheduling)
````

**J390** · CUR-1 · anchor-rewrite

````text
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** still 6 sections, renamed: low-code AI 13, data & models 16, scaling prototypes 21, serving 20, pipelines 18, monitoring 13. The exam moved from Vertex AI to the **Gemini Enterprise Agent Platform**. (verify live before scheduling)
````

**J391** · CUR-1 · anchor-rewrite

````text
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** Active; a branding update is pending. (verify live before scheduling)
````

**J392** · CUR-1 · anchor-rewrite

````text
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** Active; its own page is live and registration is open, although it is missing from the certification index page's rendered list. (verify live before scheduling)
````

**J393** · CUR-1 · anchor-rewrite

````text
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** Active; a branding update is pending. Guide weights: design ~32%, manage ~25%, migrate ~23%, deploy ~20%. (verify live before scheduling)
````

**J394** · CUR-1 · anchor-rewrite

````text
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** Active. Six sections: platform operations 14, data management 14, threat hunting 19, detection engineering 22, incident response 21, observability 10. (verify live before scheduling)
````

**J395** · CUR-1 · anchor-rewrite

````text
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** Still in beta, open until Sept 30, 2026. The exam is 3 hours: about 80 multiple-choice questions, then labs in Google Skills. Five sections, with custom agents at about 33%. The guide names ADK, A2A and **MCP**; it does **not** name "Agent Registry" or "Agent Gateway". (verify live before scheduling)
````

**J396** · CUR-1 · anchor-rewrite

````text
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** Domain weights 26/29/25/20 confirmed. **SAP-C02 is being replaced:** SAP-C03 registration opens Oct 27, 2026, and the last day for SAP-C02 is Nov 17, 2026. (verify live before scheduling)
````

**J397** · CUR-1 · anchor-rewrite

````text
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** Active. Six domains, 22/17/15/15/14/17. The Korean-language exam retires after Dec 31, 2026. (verify live before scheduling)
````

**J398** · CUR-1 · anchor-rewrite

````text
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** Active. Five domains: FM integration & data 31, implementation 26, AI safety/governance 20, efficiency 12, testing 11. (verify live before scheduling)
````

**J399** · CUR-1 · anchor-rewrite

````text
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** Weights confirmed. The last domain is named **"Security Foundations and Governance" (14%)**, not "Management & Security Governance". (verify live before scheduling)
````

**J400** · CUR-1 · anchor-rewrite

````text
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** Retiring: last exam day Dec 31, 2026; no new certifications are issued after retirement. Domains 30/26/20/24. (verify live before scheduling)
````

**J401** · CUR-1 · anchor-rewrite

````text
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** Confirmed: skills as of Apr 17, 2026; the prerequisite is Azure Administrator Associate. (verify live before scheduling)
````

**J402** · CUR-1 · anchor-rewrite

````text
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** Skills revised as of **July 27, 2026**; build/release pipelines is 50–55%. (verify live before scheduling)
````

**J403** · CUR-1 · anchor-rewrite

````text
> **Verified 2026-09-24 against the vendor's live page (D4; `cert-verification.md`):** The study guide now shows skills measured **as of Oct 21, 2026** (an upcoming revision). The AZ-500 prerequisite is now listed as **"Cloud and AI Security Engineer Associate"**. (verify live before scheduling)
````

**J404** · CUR-2 · §0.1 part list and cyber stitch block (file names, link, Northstar, superseded notes)

````text
### 0.1 The course files and the companion stitch rule

This roadmap is the **only parent**. Every companion names it `Curriculum` and binds its modules to the IDs below. The files:

- `Curriculum` (this file) — order, cert timing, Lab Reality and track structure.
- `system-design-primer-companion.md` — the system-design layer (SD, SX, P, O, Q, TF). Its bindings are generated from `primer-binding-table.md`.
- `sql-databases-companion.md` — SQL, relational theory and engine internals. It owns the engine slices DB-1…DB-10.
- `design-patterns-companion.md` — OOP design theory, patterns and architecture styles (A7, A9).
- `cloud-cybersecurity-companion.md` — security, attacks and cryptography.
- `northstar-reference-app.md` — Track N, the one running reference application (sections `Nx.y`). R2 creates its skeleton; R9 authors it.
- `session-progress-ledger.md` — the learner's state; it mirrors the inline boxes, which are authoritative.

Each companion's §2 lists what it binds to each module. When a module is taught, every bound companion ID is taught in the same session, once, by its owner (§0.3), in the order §0.4 gives. The cybersecurity companion's original stitch block, first added to this file on 2026-09-22 between A10 and A11, now sits here unchanged:

---

#### Companion — Cloud Cybersecurity (standalone)

**Standing stitch rule.** Teach security-relevant sections of this roadmap with [`cloud-cybersecurity-companion.md`](./cloud-cybersecurity-companion.md). Whenever **A5**, **A7 (auth patterns)**, **A10**, **B1 (shared responsibility)**, **B5**, **C1/C2 hardening**, **Phase 4 Networking/Security**, or the **Cloud Security / Network / SecOps** cert tracks are taught, also teach every companion module bound in companion **§2** in the **same session** — one story, never twice.

That companion is **standalone** (no other companion files). It owns attack mechanics, network/cloud cybersecurity, cryptography (`CR-*`), and the exercise bank. This roadmap still owns order, cert mapping, and service vocabulary.

> **Note:** "Standalone" is superseded: the companion has self-contained content, and ownership is shared per the suite overlap register (§0.3). Its §2 bindings now use this file's IDs (§6.2 crosswalk).

**Lab safety:** local vulnerable-by-design fixtures only; no live DDoS, third-party scanning, malware, or credential stuffing against real accounts.

> **Note:** the suite-wide rule set is §0.5.

---
````

**J405** · CUR-3 · anchor-rewrite

````text
| DNS mechanics | `Curriculum` A5 | Primer SD-08 adds routing policies/TTL discipline; cyber NT-03/04 and DOS-02 add attacks |
````

**J406** · CUR-3 · anchor-rewrite

````text
| HTTP | `Curriculum` A5 | Primer SD-29 adds idempotency/HTTP/2/3; cyber PQ-S-04 adds the browser security preview |
````

**J407** · CUR-3 · anchor-rewrite

````text
| Cookie attributes (`Domain`, `Secure`, `HttpOnly`, `SameSite`, `__Host-`) | `Curriculum` A5 HTTP | Cyber AU-01…04 adds attacks at A10 |
````

**J408** · CUR-3 · anchor-rewrite

````text
| TLS | `Curriculum` A5 (mechanics) / A10 (formal) | Primer SD-35 transit slice; cyber CR-11/12, NT-08 |
````

**J409** · CUR-3 · anchor-rewrite

````text
| Load balancing, reverse proxy | `Curriculum` A5 / C3 | Primer SD-10/11; cyber NT-07, DOS-01 |
````

**J410** · CUR-3 · anchor-rewrite

````text
| 2PC / Saga / outbox | `Curriculum` A9 (theory) | SQL CS-07 + SL-10 (SQL); design-patterns ARCH-11 (shape) |
````

**J411** · CUR-3 · anchor-rewrite

````text
| Pub/Sub | `Curriculum` A7 | Primer SD-28; design-patterns DP-14 (Observer) |
````

**J412** · CUR-3 · anchor-rewrite

````text
| Shared responsibility | `Curriculum` B1 | Cyber PQ-S-03, CM-01 |
````

**J413** · CUR-3 · anchor-rewrite

````text
| Least privilege / IAM | `Curriculum` B5 | Primer SD-35; cyber CL-03…05, AU-14 |
````

**J414** · CUR-3 · anchor-rewrite

````text
| Security checklist (encrypt in transit/at rest, XSS, SQLi, least privilege) | Distributed per `Curriculum` A5/A10/B5 + cyber modules | Primer SD-35 is an index module that points to each owner; its lab is shared with WA-05/SL-13 |
````

**J415** · CUR-3 · anchor-rewrite

````text
| Tail latency, percentiles, hedged requests | M6 (the math: order statistics, fan-out amplification) | Primer SD-03/SD-38c (design levers: timeouts, hedging, replicas); `Curriculum` C6/C7 (alerting/SLOs) |
````

**J416** · CUR-3 · anchor-rewrite

````text
| CAP / PACELC | `Curriculum` A8 (CAP statement) → A9 (formal limits, PACELC) | Primer SD-04/SD-05 (per-dataset choice, GCP store mapping) |
````

**J417** · CUR-3 · anchor-rewrite

````text
| MapReduce / scatter-gather | A9 (distributed computation model) | Primer SD-38b/c, SX-08 (job patterns); `Curriculum` V-DATA (Dataflow/Dataproc) |
````

**J418** · CUR-3 · anchor-rewrite

````text
| Backup/restore | SQL OD-04 (runbook) + N2.3 | Cyber IR-07 (ransomware integrity) |
````

**J419** · CUR-3 · anchor-rewrite

````text
| Little's law | M6 (statement + proof sketch) | Primer SD-03/SD-28 (sizing checks, e.g. 400 rps × 250 ms); the A2 slice (`primer-binding-table.md`) |
````

**J420** · CUR-3 · anchor-rewrite

````text
| Scaling evolution (single box → millions) | Primer P08 + SX-12 | Northstar milestones cite P08 steps; Track S4/S9 recall |
````

**J421** · CUR-3 · anchor-rewrite

````text
| Terraform labs | Primer TF-1…TF-7 (P08/P01/P07 infra) | SQL TF-DB*; Northstar reuses TF IDs rather than duplicating |
````

**J422** · CUR-4 · anchor-rewrite

````text
One contract for every file. Each companion keeps its own §0.3 session text and points here. When two rules conflict, the higher one wins: (1) the learner's explicit instruction in the current chat · (2) the ledger §5 preferences (§0.2) · (3) the refactor invariants · (4) this file on order, cert timing and Lab Reality · (5) the owning companion on its content (§0.3) · (6) the companions' defaults · (7) `learn-SKILL.md` defaults.
````

**J423** · CUR-4 · anchor-rewrite

````text
- Every turn carries exactly one focused question, embedded in the teaching. Diagnosis happens through those checks; there is no separate probing (ledger §5 wins over the skill's calibrating question). A turn may be as long as one concept needs.
````

**J424** · CUR-4 · anchor-rewrite

````text
1. **Anchor** — list the bound IDs from *all* files (each companion's §2; the primer's from `primer-binding-table.md`).
````

**J425** · CUR-4 · anchor-rewrite

````text
7. **Checks**, woven in per ledger §5.
````

**J426** · CUR-4 · anchor-rewrite

````text
**0.4.7 Check questions and exercise pre-flight.** A check tests mechanism or application, asks one thing (split a multi-part check across turns), is answerable from anchored material, has a written expected answer and at least one expected wrong answer in the owning file's keys, is precision-sensitive, and is never answered by the tutor in the same turn. Before issuing any exercise the tutor checks: internal consistency (for example, a CNAME never points at an IP) · every term anchored · exactly one question · the answer derivable from what was taught · any numbers computed. The tutor is precise about mechanisms and says explicitly when unsure. An error found later is corrected openly in the next turn and logged in `errata.md`.
````

**J427** · CUR-5 · anchor-rewrite

````text
> **Note:** Status as of 2026-09-24 (C-20, D2): the course is a fresh start, so this sentence is still true. The live position is kept in `session-progress-ledger.md`.
````

**J428** · CUR-5 · anchor-rewrite

````text
> **Note:** Status as of 2026-09-24 (C-20, D2): the course is a fresh start, so this sentence is still true. The live position is kept in `session-progress-ledger.md`.
````

**J429** · CUR-6 · anchor-rewrite

````text
> **Note:** A7 binds several dozen suite concepts, so it is taught as ordered teaching blocks. These are sessions, not new modules; the module ID stays A7. A7.1 client-server and API styles (+ SD-32…SD-34) · A7.2 async and queues (+ SD-28) · A7.3 OOP foundations + SOLID · A7.4 GRASP + creational patterns · A7.5 structural patterns · A7.6 behavioral patterns · A7.7 architecture styles + DDD (ARCH-01…ARCH-08) · A7.8 API authentication/authorization + attacks · A7.9 abuse and rate limits · A7.10 S1–S2 · A7.11 N0 · A7.12 checkpoints. A5, A8 and A10 get the same split in R4, from the §0.4.8 pacing budget.
````

**J430** · CUR-6 · anchor-rewrite

````text
Engine slices DB-1…DB-10 (bag relations, slotted page, buffer clock sweep, B-tree + inverted index, iterators + spill, histograms, MVCC visibility + deadlock detection, mini-WAL): owned and taught by `sql-databases-companion.md` §4.0 inside the A8 sessions
````

**J431** · CUR-7 · anchor-rewrite

````text
### Reserved tracks M, U, S and N (stubs; authored in R4 and R9)
````

**J432** · CUR-7 · anchor-rewrite

````text
The companions' foreign anchors were rebound to these IDs by the §6 crosswalks (`crosswalk.md`). Each ID is reserved here with its scope; the modules themselves are written in R4 (M, U, S) and R9 (N). Nothing here is teaching content yet.
````

**J433** · CUR-7 · move

````text
| N0…N12 | Northstar reference application | milestones and sections `Nx.y` in `northstar-reference-app.md` |
````

**J434** · CUR-8 · anchor-rewrite

````text
*Category IDs (C-22, 2026-09-24).* Other files anchor to these IDs instead of the category names:
````

**J435** · CUR-8 · anchor-rewrite

````text
> **Note:** status as of 2026-09-24: the three notes below were re-checked that day (`cert-verification.md`). New dated items are in the Part V–VII verification notes. R4 moves every date-bearing line into `volatility-register.md` with a last-checked date.
````

**J436** · GO-1 · anchor-rewrite

````text
This course is one course in five parts. This roadmap, the **main course**, is the **only parent**: every companion binds its modules to the IDs below, and a module ID from any part may be used as a stitch tag in any other part. The parts:
````

**J438** · GO-3 · anchor-rewrite

````text
Progress lives in the inline `- [ ]` boxes of the five parts, which are authoritative. The tutor also keeps a **progress ledger**, a running record beside the boxes: each ID's mastery state (§0.4.5), the misconception register, the errata list, the recorded overrides and wrong predictions, and the exact resume point (§0.4.8).
````

**J439** · GO-4 · anchor-rewrite

````text
| Rate limiting | Cyber AB-01 (algorithms + abuse) | Primer Q22 is the design exercise and recalls AB-01 |
````

**J440** · GO-4 · anchor-rewrite

````text
| SQL injection / parameterisation | SQL SL-13 (the SQL mechanics) | Cyber WA-05 (attacker model across the whole injection family) |
````

**J441** · GO-4 · anchor-rewrite

````text
| Garbage collection | U4 (memory management) | Primer Q21 (design problem); SX-04 (data GC/TTL) |
````

**J443** · GO-6 · anchor-rewrite

````text
3. **Layers**, in fixed order: system design (primer) → SQL/engine → patterns → attacker/crypto (cyber).
````

**J446** · GAP-1 · anchor-rewrite

````text
Networking: VPC, Cloud Load Balancing, Cloud CDN, Cloud Interconnect/VPN, Cloud DNS, Cloud Armor
````

**J447** · GAP-2 · anchor-rewrite

````text
Storage/DB: Cloud Storage, Cloud SQL, Spanner, Bigtable, Firestore, Memorystore, AlloyDB
````

**J448** · GAP-3 · anchor-rewrite

````text
Data/Analytics: BigQuery, Pub/Sub, Dataflow, Dataproc, Cloud Composer, Looker
````

**J449** · GAP-4 · anchor-rewrite

````text
AI/ML: Vertex AI (full suite: Workbench, Training, Pipelines, Feature Store, Model Registry, Endpoints, Vizier), Model Garden, Gemini Enterprise/Agent Platform, AutoML, BigQuery ML
````

**J450** · GAP-5 · anchor-rewrite

````text
Security: IAM, Cloud KMS, VPC Service Controls, Binary Authorization, Security Command Center, Google SecOps (Chronicle)
````

**J451** · GAP-6 · anchor-rewrite

````text
Ops/DevOps: Cloud Build, Cloud Deploy, Artifact Registry, Cloud Monitoring/Logging
````

**J453** · GAP-8 · anchor-rewrite

````text
| S8 | Migration & modernization | |
````

**J454** · GAP-9 · anchor-rewrite

````text
| S11 | Case-study studio | |
````

**J455** · GAP-10 · anchor-rewrite

````text
| M5 | Numerical Methods & Floating Point | IEEE 754, rounding, decimal vs binary |
````

**J456** · GAP-11 · anchor-rewrite

````text
| Heavy hitters / sketches / approximate counting | U2 (randomized algorithms) | Primer Q16/Q18 (design); SQL AN-04 (SQL approximation) |
````

**J849** · R4-1 · reserved-track stub section

````text
### Reserved tracks M, U and S (stubs)

The companions anchor to these IDs. Each ID is reserved here with its scope; the modules themselves are not written yet, so nothing here is teaching content yet. Until a module is written, a pointer to it names its scope only: say so plainly (§0.2) and teach the concept from the part that owns it in §0.3.

| ID | Title | Scope (what the rebound references need) |
|---|---|---|
| M1 | Discrete Mathematics & Proof | logic, proof techniques, sets and relations, counting, graphs, elementary number theory |
| M2 | Linear Algebra | rigorous pass on A2 |
| M3 | Calculus | rigorous pass on A2 |
| M4 | Probability & Statistics | rigorous pass on A2 |
| M5 | Numerical Methods & Floating Point | IEEE 754, rounding, decimal vs binary; catastrophic cancellation, compensated (Kahan) summation, stable reformulations (`log1p`, log-sum-exp) |
| M6 | Information Theory & Performance Modeling | queueing, Little's law, tail latency |
| U1 | Computer Architecture & Systems Programming | machine-level representation, memory hierarchy |
| U2 | Algorithms: Design & Analysis | rigorous pass on A4 |
| U3 | Theory of Computation | automata, grammars, decidability |
| U4 | Programming Languages & Paradigms | paradigms, types, memory management |
| U5 | Concurrency & Parallel Computing | races, locks, deadlock, memory models |
| U6 | Software Engineering & Testing | requirements, testing theory, specification |
| U7 | Professional Practice, Ethics & Law | ethics, privacy law literacy, licensing |
| S1 | Requirements & quality attributes | Track S — System Architecture Design Studio |
| S2 | Architecture documentation | views, C4, ADRs, the HLD/LLD contract and NFR tables |
| S3 | Capacity & performance engineering | |
| S4 | Reliability architecture | |
| S5 | Data architecture | |
| S6 | Security architecture | threat-model-driven design |
| S7 | Integration & event-driven architecture | |
| S8 | Migration & modernization | the six Rs mapped to landings (rehost with Migrate to Virtual Machines, replatform, re-architect for GKE or Cloud Run, retire, retain, repurchase); Migration Center discovery, dependency mapping and wave planning; licence impact (bring-your-own vs included) before wave 1; data movement (Database Migration Service, Datastream, Storage Transfer Service, Transfer Appliance); wave-0 connectivity; cutover checklist with a written rollback (PCA 1.4) |
| S9 | Cost architecture & unit economics | |
| S10 | Architecture evaluation | |
| S11 | Case-study studio | the four published PCA case studies, each as an HLD with its trade-off answers |

````

**J853** · R4-4 · anchor-rewrite

````text
> **Note:** A7 binds several dozen suite concepts, so it is taught as ordered teaching blocks. These are sessions, not new modules; the module ID stays A7. A7.1 client-server and API styles (+ SD-32…SD-34) · A7.2 async and queues (+ SD-28) · A7.3 OOP foundations + SOLID · A7.4 GRASP + creational patterns · A7.5 structural patterns · A7.6 behavioral patterns · A7.7 architecture styles + DDD (ARCH-01…ARCH-08) · A7.8 API authentication/authorization + attacks · A7.9 abuse and rate limits · A7.10 S1–S2 · A7.11 checkpoints. A5, A8 and A10 get the same split, from the §0.4.8 pacing budget, when they are taught.
````

**J854** · R4-5 · anchor-rewrite

````text
The published case studies (exam guide v6.1): Altostrat Media, Cymbal Retail, EHR Healthcare, KnightMotives Automotive `(verify)` against the live guide. Each gets a written HLD and one "I pick X because Y, I accept Z" answer per requirement in S11.
````

**J856** · R4-6 · anchor-rewrite

````text
> **Note:** First-pass scope: this intuition pass is the first pass and is complete as written. The rigorous passes follow in M2 (linear algebra), M3 (calculus) and M4 (probability & statistics).
````

**J857** · R4-6 · anchor-rewrite

````text
> **Note:** First-pass scope: A4 stays at engineering-practical depth. The rigorous pass (proofs, recurrences, and implementing a balanced search tree) is U2.
````

**J858** · R4-7 · anchor-rewrite

````text
| Floating point | M5 | SQL PQ-03 (decimal semantics) |
````

**J859** · R4-7 · anchor-rewrite

````text
| Discrete-math foundations of relations | M1 | SQL PQ-01/02, RT-01 |
````

**J860** · R4-7 · move

````text
| Number theory for cryptography | M1 | Cyber CR-01…10 |
````

**J861** · R4-7 · anchor-rewrite

````text
| Tail latency, percentiles, hedged requests | M6 (the math: order statistics, fan-out amplification) | Primer SD-03/SD-38c (design levers: timeouts, hedging, replicas); C6/C7 (alerting/SLOs) |
````

**J862** · R4-7 · anchor-rewrite

````text
| Little's law | M6 (statement + proof sketch) | Primer SD-03/SD-28 (sizing checks, e.g. 400 rps × 250 ms); the A2 slice (primer §2 stitch table) |
````

**J863** · R4-7 · anchor-rewrite

````text
| Consistent hashing | U2 (analysis: expected movement 1/N, virtual nodes, load bounds) | Primer SD-38a (sharding/rebalancing design); A4 ring slice |
````

**J864** · R4-7 · anchor-rewrite

````text
| Heavy hitters / sketches / approximate counting (count-min sketch, HyperLogLog, Bloom filters with their false-positive rate (1 − e^(−kn/m))^k) | U2 (randomized algorithms) | Primer Q16/Q18 (design); SQL AN-04 (SQL approximation) |
````

**J865** · R4-7 · anchor-rewrite

````text
| Unique ID generation (Base62, Snowflake) | Primer SX-02/Q17 | M1 (counting, birthday bound for collisions); A1 recall (bit layout) |
````

**J866** · R4-7 · anchor-rewrite

````text
| Garbage collection | U4 (memory management) | Primer Q21 (design problem); SX-04 (data GC/TTL); Go companion GO-09 (Go's collector, `GOGC`, `GOMEMLIMIT`) |
````

**J867** · R4-7 · anchor-rewrite

````text
| Interview/design method, back-of-the-envelope | Primer SD-00 | Track S1–S3 recall it; they never restate it |
````

**J868** · R4-7 · anchor-rewrite

````text
| Scaling evolution (single box → millions) | Primer P08 + SX-12 | Track S4/S9 recall |
````

**J869** · R4-7 · anchor-rewrite

````text
| Concurrency | U5 (theory; reserved) | Go companion GO-15…GO-19 (goroutines, channels, `context`, the Go memory model, the race detector); A9 (distributed theory) |
````

**J870** · R4-7 · anchor-rewrite

````text
| Data-structure implementations in code | A4 / U2 (concepts and costs) | Go companion GO-27 (the Go code); Primer O01, O02, O07 (the checkpoints) |
````

**J871** · R4-12 · anchor-rewrite

````text
> **Note:** A7 binds several dozen suite concepts, so it is taught as ordered teaching blocks. These are sessions, not new modules; the module ID stays A7. A7.1 client-server and API styles (+ SD-32…SD-34) · A7.2 async and queues (+ SD-28) · A7.3 OOP foundations + SOLID · A7.4 GRASP + creational patterns · A7.5 structural patterns · A7.6 behavioral patterns · A7.7 architecture styles + DDD (ARCH-01…ARCH-08) · A7.8 API authentication/authorization + attacks · A7.9 abuse and rate limits · A7.10 architecture documentation (views, C4, ADRs, HLD/LLD, NFR tables) · A7.11 checkpoints. A5, A8 and A10 get the same split, from the §0.4.8 pacing budget, when they are taught.
````
