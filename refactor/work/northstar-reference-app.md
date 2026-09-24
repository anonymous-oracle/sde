# Northstar Reference Application (Track N)

*Skeleton created by the curriculum refactor on 2026-09-24 (R2; C-03, C-05, C-06, C-07, §6.3). R9 authors it.* Northstar is the one running reference application every file builds on: storefront, customer API, admin, service-to-service, data, CI/CD and AI-gateway planes (the cybersecurity companion's Appendix N sketches its threat model). `Curriculum` owns order and cert timing; this file will own the concrete build, milestone by milestone.

**How the sections were numbered.** The companions were written against an older parent, `gcp-curriculum.md`, and cite its numbered sections. Each such section `x.y` becomes `Nx.y` here, with the same meaning (C-03, §6.3). The meaning line quotes that section's heading and line in `gcp-curriculum.md`. Under decision D1, R9 may port the original text with a `Source material:` line, or reconstruct it; a reconstructed section is labelled `[reconstructed from companion references]` (C-07). Every section below is still a **stub**: nothing in this file is teaching content yet.

**Rules carried into R9.** Each milestone that changes the deployed architecture cites the primer P08 ladder step it realizes and reuses the primer's Terraform exercise by ID (TF-1…TF-7), never a copy (C-32). Each milestone lists its companion stitches, its Lab Reality budget, its acceptance evidence and the S2-format documents it produces (§9.4).

Wildcard references (`N2.x`, `N3.x`, `N5.x`, `N6.x`) resolve to the milestone of the same number.

## N0 · Day-zero: billing, IAM core, and how we design

- **Meaning:** `gcp-curriculum.md`:1509 (Part 0).
- **Referenced by:** Curriculum A7. Software Architecture & APIs; Curriculum Reserved tracks M, U, S and N; cyber PQ-S-03
- **Status:** [stub — authored in R9]

### N0.4 · HLD/LLD contract + Donne Martin

- **Meaning:** `gcp-curriculum.md`:1726 (§0.4).
- **Referenced by:** SQL 2. Stitch table; SQL DD-01; SQL RT-06; cyber SEC-E1.1; cyber SEC-Z0.4; cyber TH-01
- **Status:** [stub — authored in R9]

## N1 · Compute platforms, then deploy frontend + backend first

- **Meaning:** `gcp-curriculum.md`:1929 (Part 1).
- **Referenced by:** — (milestone container)
- **Status:** [stub — authored in R9]

### N1.2 · Container contract (LLD that production depends on)

- **Meaning:** `gcp-curriculum.md`:2000 (§1.2).
- **Referenced by:** cyber CR-07
- **Status:** [stub — authored in R9]

## N2 · SQL design, Cloud SQL setup, Firestore, objects

- **Meaning:** `gcp-curriculum.md`:3091 (Part 2).
- **Referenced by:** cyber WA-05
- **Status:** [stub — authored in R9]

### N2.3 · How to set up Cloud SQL on GCP (required procedure)

- **Meaning:** `gcp-curriculum.md`:3231 (§2.3).
- **Referenced by:** Curriculum 0.3 Suite overlap and ownership register; SQL 0.1 Standing instruction; SQL 0.2 Stitching rules; SQL 2. Stitch table; SQL 2.1 Overlap register; SQL 2.2 A8 slice pairing; SQL 2.3 Parallel calendar; SQL 3.2 Bring-up; SQL 4.0 Engine slices; SQL DB-10; SQL OD-03; SQL OD-04; cyber IR-07; cyber SEC-Z0.8
- **Status:** [stub — authored in R9]

### N2.4 · Firestore (still live on free tier)

- **Meaning:** `gcp-curriculum.md`:3265 (§2.4).
- **Referenced by:** SQL 0.2 Stitching rules; SQL 2. Stitch table; SQL 2.1 Overlap register; SQL AN-06; SQL DT-7
- **Status:** [stub — authored in R9]

### N2.5 · Cloud Storage (full offering — video block)

- **Meaning:** `gcp-curriculum.md`:3299 (§2.5).
- **Referenced by:** SQL 2. Stitch table; SQL PQ-04; SQL SL-12
- **Status:** [stub — authored in R9]

### N2.6 · Config, migrations, jobs

- **Meaning:** `gcp-curriculum.md`:3369 (§2.6).
- **Referenced by:** SQL 0.2 Stitching rules; SQL 2. Stitch table; SQL 2.1 Overlap register; SQL DB-2; SQL DD-11; SQL OD-08; SQL SCH-4; SQL SQL-E9.6
- **Status:** [stub — authored in R9]

### N2.7 · Spanner and NoSQL map (PCA storage types)

- **Meaning:** `gcp-curriculum.md`:3333 (§2.7).
- **Referenced by:** SQL 0.2 Stitching rules; SQL 2. Stitch table; SQL 2.1 Overlap register; SQL 2.3 Parallel calendar; SQL AN-05; SQL CS-07; SQL DD-10; SQL SCH-5
- **Status:** [stub — authored in R9]

## N3 · Microservices (industry)

- **Meaning:** `gcp-curriculum.md`:3398 (Part 3).
- **Referenced by:** cyber AB-04
- **Status:** [stub — authored in R9]

### N3.0 · Software design (before you split)

- **Meaning:** `gcp-curriculum.md`:3402 (§3.0).
- **Referenced by:** cyber AB-06; cyber SEC-E2.4; cyber TH-04
- **Status:** [stub — authored in R9]

### N3.4 · Async: Pub/Sub, Eventarc, Cloud Tasks, Cloud Scheduler

- **Meaning:** `gcp-curriculum.md`:3607 (§3.4).
- **Referenced by:** cyber CL-08
- **Status:** [stub — authored in R9]

## N4 · Authentication and authorization

- **Meaning:** `gcp-curriculum.md`:3688 (Part 4).
- **Referenced by:** — (milestone container)
- **Status:** [stub — authored in R9]

### N4.2 · Hardened HTTP and middleware (Go type here; Python twin after)

- **Meaning:** `gcp-curriculum.md`:3704 (§4.2).
- **Referenced by:** cyber Appendix N; cyber CL-01; cyber DOS-05; cyber DOS-06; cyber SEC-E10.1; cyber SEC-E3.2; cyber SEC-E4.2; cyber WA-08
- **Status:** [stub — authored in R9]

### N4.3 · Identity, passwords, recovery, MFA

- **Meaning:** `gcp-curriculum.md`:3730 (§4.3).
- **Referenced by:** cyber 3.3.1 Cryptography pillar coda; cyber CR worked illustration F; cyber CR-13; cyber CR-E35; cyber CR-E8
- **Status:** [stub — authored in R9]

### N4.4 · Opaque sessions, cookies, CSRF, CORS

- **Meaning:** `gcp-curriculum.md`:3741 (§4.4).
- **Referenced by:** cyber AU-03; cyber Appendix N; cyber SEC-E2.2; cyber SEC-E2.3; cyber SEC-E2.7; cyber SEC-E9.3; cyber WA-01
- **Status:** [stub — authored in R9]

### N4.5 · API keys, signed requests, JWT policy

- **Meaning:** `gcp-curriculum.md`:3752 (§4.5).
- **Referenced by:** cyber CR-06; cyber CR-10; cyber SEC-E10.6
- **Status:** [stub — authored in R9]

### N4.6 · OAuth 2.0 / OIDC

- **Meaning:** `gcp-curriculum.md`:3761 (§4.6).
- **Referenced by:** cyber SEC-E9.10
- **Status:** [stub — authored in R9]

### N4.7 · Authorization (app + GCP)

- **Meaning:** `gcp-curriculum.md`:3774 (§4.7).
- **Referenced by:** cyber AU-11; cyber Appendix N; cyber SEC-E3.8; cyber TH-04
- **Status:** [stub — authored in R9]

### N4.8 · Workload auth

- **Meaning:** `gcp-curriculum.md`:3793 (§4.8).
- **Referenced by:** cyber Appendix N; cyber CL-05; cyber CR-17; cyber SEC-E9.2
- **Status:** [stub — authored in R9]

### N4.9 · Application, secrets, supply chain, assurance

- **Meaning:** `gcp-curriculum.md`:3824 (§4.9).
- **Referenced by:** cyber CK-04; cyber CR-E35
- **Status:** [stub — authored in R9]

### N4.10 · API abuse (GCP)

- **Meaning:** `gcp-curriculum.md`:3836 (§4.10).
- **Referenced by:** cyber AB-01; cyber AB-08; cyber AU-08; cyber Appendix N; cyber Capstone scheduling note; cyber SEC-CAP3; cyber SEC-E3.3; cyber SEC-E4.4; cyber SEC-E4.9; cyber SEC-E9.1; cyber SEC-E9.9
- **Status:** [stub — authored in R9]

## N5 · Payments and money movement

- **Meaning:** `gcp-curriculum.md`:3865 (Part 5).
- **Referenced by:** cyber AB-06; cyber AB-07; cyber CM-02; cyber PV-03; cyber SEC-E6.13
- **Status:** [stub — authored in R9]

### N5.3 · Ledger and consistency

- **Meaning:** `gcp-curriculum.md`:3928 (§5.3).
- **Referenced by:** SQL 0.2 Stitching rules; SQL 2. Stitch table; SQL 2.1 Overlap register; SQL 2.3 Parallel calendar; SQL BH-4; SQL DD-03; SQL DD-05; SQL DD-07; SQL SQL-E8.2; cyber AB-06
- **Status:** [stub — authored in R9]

## N6 · Networking services (full video block) then network security

- **Meaning:** `gcp-curriculum.md`:3981 (Part 6).
- **Referenced by:** cyber 8. CSA CCM v4.x coverage checklist
- **Status:** [stub — authored in R9]

### N6.11 · Network security overlay (NGFW, Armor, IAP, VPC-SC, LB TLS)

- **Meaning:** `gcp-curriculum.md`:4547 (§6.11).
- **Referenced by:** cyber NT-07; cyber SEC-E4.5; cyber SEC-Z0.2
- **Status:** [stub — authored in R9]

### N6.12 · Firewall and Cloud NGFW (security depth)

- **Meaning:** `gcp-curriculum.md`:4579 (§6.12).
- **Referenced by:** cyber SEC-E5.4
- **Status:** [stub — authored in R9]

### N6.13 · Load balancing, TLS, CDN, and the edge

- **Meaning:** `gcp-curriculum.md`:4622 (§6.13).
- **Referenced by:** cyber AB-02; cyber CR-12; cyber DOS-05; cyber SEC-E4.6
- **Status:** [stub — authored in R9]

### N6.14 · Zero-trust access

- **Meaning:** `gcp-curriculum.md`:4654 (§6.14).
- **Referenced by:** cyber 8. CSA CCM v4.x coverage checklist; cyber Appendix N; cyber SEC-E1.4; cyber SEC-E5.5
- **Status:** [stub — authored in R9]

### N6.15 · Segmentation and exfil controls

- **Meaning:** `gcp-curriculum.md`:4695 (§6.15).
- **Referenced by:** cyber 7. Teaching notes bank; cyber Appendix N; cyber PV-04; cyber SEC-E10.1; cyber SEC-E10.7; cyber SEC-E5.6
- **Status:** [stub — authored in R9]

### N6.16 · DNS and DDoS (security view)

- **Meaning:** `gcp-curriculum.md`:4728 (§6.16).
- **Referenced by:** cyber Capstone scheduling note; cyber DOS-03; cyber NT-03; cyber SEC-E4.21; cyber SEC-E9.1; cyber WA-11
- **Status:** [stub — authored in R9]

## N7 · Cybersecurity (concept + GCP offerings)

- **Meaning:** `gcp-curriculum.md`:4767 (Part 7).
- **Referenced by:** — (milestone container)
- **Status:** [stub — authored in R9]

### N7.1 · Security principles

- **Meaning:** `gcp-curriculum.md`:4771 (§7.1).
- **Referenced by:** cyber NT-01; cyber PQ-S-03; cyber SEC-Z0.3
- **Status:** [stub — authored in R9]

### N7.2 · Identity and access (GCP offerings)

- **Meaning:** `gcp-curriculum.md`:4800 (§7.2).
- **Referenced by:** cyber 8. CSA CCM v4.x coverage checklist; cyber Appendix N; cyber CK-03; cyber CL-03; cyber SEC-E5.1
- **Status:** [stub — authored in R9]

### N7.3 · Data protection

- **Meaning:** `gcp-curriculum.md`:4830 (§7.3).
- **Referenced by:** SQL 2. Stitch table; SQL SCH-6; cyber 3.3 Cryptography; cyber 3.3.1 Cryptography pillar coda; cyber 8. CSA CCM v4.x coverage checklist; cyber Appendix N; cyber CR worked illustration C; cyber CR-14; cyber CR-20; cyber CR-E10; cyber CR-E30; cyber CR-E34; cyber CR-E9; cyber SC-03; cyber SEC-CAP1; cyber SEC-E6.3; cyber SEC-E9.8
- **Status:** [stub — authored in R9]

### N7.4 · Application and API security

- **Meaning:** `gcp-curriculum.md`:4859 (§7.4).
- **Referenced by:** cyber CL-01; cyber SEC-CAP1; cyber SEC-E10.3; cyber SEC-E3.9; cyber TH-03; cyber WA-05
- **Status:** [stub — authored in R9]

### N7.5 · Workload and supply chain

- **Meaning:** `gcp-curriculum.md`:4887 (§7.5).
- **Referenced by:** cyber 3.3.1 Cryptography pillar coda; cyber 7. Teaching notes bank; cyber 8. CSA CCM v4.x coverage checklist; cyber Appendix N; cyber CK-01; cyber CK-05; cyber CR-10; cyber SEC-E10.2; cyber SEC-E6.4; cyber SEC-E9.4; cyber WL-04
- **Status:** [stub — authored in R9]

### N7.6 · Detection and posture

- **Meaning:** `gcp-curriculum.md`:4916 (§7.6).
- **Referenced by:** cyber 7. Teaching notes bank; cyber IR-02; cyber IR-04; cyber NT-02; cyber SEC-E9.5
- **Status:** [stub — authored in R9]

### N7.7 · Org policy and landing zone

- **Meaning:** `gcp-curriculum.md`:4934 (§7.7).
- **Referenced by:** cyber CL-02; cyber SEC-E9.8
- **Status:** [stub — authored in R9]

### N7.8 · Incident response

- **Meaning:** `gcp-curriculum.md`:4947 (§7.8).
- **Referenced by:** cyber 3.3.1 Cryptography pillar coda; cyber CL-02; cyber CL-04; cyber Capstone scheduling note; cyber IR-05; cyber SEC-CAP2; cyber SEC-E10.4; cyber SEC-E5.3; cyber SEC-E5.7; cyber SEC-E7.2; cyber SEC-E9.2
- **Status:** [stub — authored in R9]

### N7.9 · Compliance mapping

- **Meaning:** `gcp-curriculum.md`:4958 (§7.9).
- **Referenced by:** cyber 8. CSA CCM v4.x coverage checklist; cyber PV-01; cyber PV-05; cyber SEC-E8.1
- **Status:** [stub — authored in R9]

## N8 · HLD/LLD mastery (Donne Martin → GCP)

- **Meaning:** `gcp-curriculum.md`:4992 (Part 8).
- **Referenced by:** cyber DOS-06; cyber DOS-08; cyber SC-02; cyber TH-06
- **Status:** [stub — authored in R9]

### N8.0 · Donne Martin → GCP building blocks

- **Meaning:** `gcp-curriculum.md`:5000 (§8.0).
- **Referenced by:** SQL 2. Stitch table; SQL 2.3 Parallel calendar; SQL DD-01; SQL DD-08; SQL SCH-2
- **Status:** [stub — authored in R9]

### N8.1 · Production-scale primitives (from scratch, then product)

- **Meaning:** `gcp-curriculum.md`:5478 (§8.1).
- **Referenced by:** SQL 0.2 Stitching rules; SQL 2. Stitch table; SQL 2.1 Overlap register; SQL 2.3 Parallel calendar; SQL CS-02; SQL DD-09; SQL DD-13; SQL OD-03; SQL SL-13; SQL SQL-E10.2; SQL SQL-E10.6; cyber AB-05; cyber CL-06
- **Status:** [stub — authored in R9]

### N8.1.1 · Bloom filter + FPR (required)

- **Meaning:** `gcp-curriculum.md`:5527 (§8.1.1).
- **Referenced by:** — (named by C-06)
- **Status:** [stub — authored in R9]

### N8.1.2 · Hash ring (required; shared with 8.A.2)

- **Meaning:** `gcp-curriculum.md`:5541 (§8.1.2).
- **Referenced by:** — (named by C-06)
- **Status:** [stub — authored in R9]

### N8.1.3 · Singleflight / stampede control (required)

- **Meaning:** `gcp-curriculum.md`:5549 (§8.1.3).
- **Referenced by:** — (named by C-06)
- **Status:** [stub — authored in R9]

### N8.1.4 · Load shedding (required)

- **Meaning:** `gcp-curriculum.md`:5563 (§8.1.4).
- **Referenced by:** — (named by C-06)
- **Status:** [stub — authored in R9]

### N8.1.5 · Cursor pagination (required)

- **Meaning:** `gcp-curriculum.md`:5577 (§8.1.5).
- **Referenced by:** SQL 2. Stitch table; SQL 2.1 Overlap register; SQL OD-09; SQL PX-9
- **Status:** [stub — authored in R9]

### N8.1.6 · Other primitives (compressed ownership)

- **Meaning:** `gcp-curriculum.md`:5591 (§8.1.6).
- **Referenced by:** — (named by C-06)
- **Status:** [stub — authored in R9]

### N8.C · Evidence-pack HLDs (full packs; paper + sequences OK)

- **Meaning:** `gcp-curriculum.md`:5324 (§8.C).
- **Referenced by:** SQL 2. Stitch table; SQL 2.3 Parallel calendar
- **Status:** [stub — authored in R9]

## N9 · Kubernetes internals applied on GKE + mesh + cache

- **Meaning:** `gcp-curriculum.md`:5749 (Part 9).
- **Referenced by:** — (milestone container)
- **Status:** [stub — authored in R9]

### N9.1 · Memorystore

- **Meaning:** `gcp-curriculum.md`:5781 (§9.1).
- **Referenced by:** SQL 2. Stitch table; SQL 2.3 Parallel calendar; cyber DOS-08
- **Status:** [stub — authored in R9]

### N9.2 · GKE and Kubernetes concepts

- **Meaning:** `gcp-curriculum.md`:5810 (§9.2).
- **Referenced by:** cyber CK-02; cyber CK-03; cyber CK-06
- **Status:** [stub — authored in R9]

### N9.4 · Spanner, AlloyDB, Bigtable, BigQuery (ops view)

- **Meaning:** `gcp-curriculum.md`:5884 (§9.4).
- **Referenced by:** SQL 0.2 Stitching rules; SQL 2. Stitch table; SQL 2.1 Overlap register; SQL 2.3 Parallel calendar; SQL AN-01; SQL AN-02; SQL AN-05; SQL CS-09
- **Status:** [stub — authored in R9]

## N9b · Vertex AI, Gemini, Big Data (PCA v6.1 §§1.3, 2.4, 2.5)

- **Meaning:** `gcp-curriculum.md`:5914 (Part 9b).
- **Referenced by:** cyber AB-08
- **Status:** [stub — authored in R9]

### N9b.1 · Big Data services

- **Meaning:** `gcp-curriculum.md`:5918 (§9b.1).
- **Referenced by:** SQL 0.2 Stitching rules; SQL 2. Stitch table; SQL 2.1 Overlap register; SQL 2.3 Parallel calendar; SQL AN-02; SQL AN-03; SQL AN-04; SQL SL-11; SQL SQL-E13.3
- **Status:** [stub — authored in R9]

## N9c · Production ML systems (industry case-study atlas)

- **Meaning:** `gcp-curriculum.md`:6060 (Part 9c).
- **Referenced by:** cyber 3.3.1 Cryptography pillar coda; cyber AI-01; cyber AI-02; cyber AI-04; cyber AI-05; cyber Appendix N; cyber CR-18; cyber Capstone scheduling note; cyber PV-02; cyber SEC-E10.5; cyber SEC-E8.3; cyber SEC-E9.6; cyber WL-05
- **Status:** [stub — authored in R9]

### N9c.1 · Features, labels, skew

- **Meaning:** `gcp-curriculum.md`:6137 (§9c.1).
- **Referenced by:** SQL 0.2 Stitching rules; SQL 2. Stitch table; SQL 2.1 Overlap register; SQL 2.3 Parallel calendar; SQL DD-05; SQL SL-04; SQL SL-12; SQL SQL-E6.4
- **Status:** [stub — authored in R9]

### N9c.2 · Retrieval, rank, recommend, bandits

- **Meaning:** `gcp-curriculum.md`:6147 (§9c.2).
- **Referenced by:** SQL 2. Stitch table; SQL AN-07; cyber AI-03
- **Status:** [stub — authored in R9]

### N9c.5 · LLM applications (GCP RAG slice)

- **Meaning:** `gcp-curriculum.md`:6176 (§9c.5).
- **Referenced by:** SQL 2. Stitch table; SQL AN-07
- **Status:** [stub — authored in R9]

## N10 · Observability, reliability, FinOps

- **Meaning:** `gcp-curriculum.md`:6579 (Part 10).
- **Referenced by:** cyber SEC-E9.5; cyber WA-09
- **Status:** [stub — authored in R9]

### N10.0 · Google Cloud Observability (full — PCA 6.2)

- **Meaning:** `gcp-curriculum.md`:6583 (§10.0).
- **Referenced by:** cyber IR-01
- **Status:** [stub — authored in R9]

### N10.3 · FinOps + API / SKU cost analysis

- **Meaning:** `gcp-curriculum.md`:6689 (§10.3).
- **Referenced by:** cyber DOS-07; cyber SEC-E10.8; cyber SEC-E7.6
- **Status:** [stub — authored in R9]

## N11 · Capstone and PCA

- **Meaning:** `gcp-curriculum.md`:6835 (Part 11).
- **Referenced by:** SQL 2. Stitch table; SQL 2.3 Parallel calendar; SQL 9. Capstones
- **Status:** [stub — authored in R9]

## N11b · Control-plane capstone (after Northstar v1)

- **Meaning:** `gcp-curriculum.md`:6927 (Part 11b).
- **Referenced by:** SQL 2. Stitch table; SQL 2.3 Parallel calendar; SQL DD-07
- **Status:** [stub — authored in R9]

## N12 · Continuation (after 11b)

- **Meaning:** `gcp-curriculum.md`:7169 (Part 12).
- **Referenced by:** Curriculum Reserved tracks M, U, S and N
- **Status:** [stub — authored in R9]
