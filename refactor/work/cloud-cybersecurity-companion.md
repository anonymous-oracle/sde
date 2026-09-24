# The Cloud Cybersecurity Companion — Standalone Edition

**Companion to [`gcp.md`](./gcp.md)** (the cloud mastery / certification roadmap).

This file is **standalone**. It does not depend on other companion files. It covers **cloud security, cybersecurity, cryptography, and network security** for cloud infrastructure and cloud-hosted distributed systems — taught in parallel with the matching sections of `gcp.md`.

**Owns:** threat modeling; authentication & session attacks; API abuse / bots / rate limiting; DDoS & WAF; web/app attacks; cloud-native attacks (SSRF/metadata, IAM abuse, tenant isolation); network & zero-trust attacks; containers/K8s threats; supply chain; detection & IR; AI/LLM app threats; **full applied cryptography track (`CR-01` … `CR-20`)**; side channels & confidential computing awareness; privacy/compliance literacy for cloud.

**Does not own:** non-security tracks in `gcp.md` (ML math, general DSA, FinOps deep-dives, non-security data modeling). Those stay in `gcp.md` only.

**Sources:** Stanford CS155 · Stanford CS255 · Stanford Online Cloud Security (XACS235) · MIT 6.858 / 6.566 · Berkeley CS161 · CMU Cloud Security · CSA CCM v4.x · OWASP Top 10:2025 · MITRE ATT&CK Cloud · Google Cloud Armor / reCAPTCHA / KMS / VPC-SC / SCC docs · NIST CSF (lite). Built September 22, 2026.

---

## 0. Read this first — how this file complements `gcp.md`

### 0.1 Standing instruction (every teaching session)

**This file is a complement to `gcp.md`, not a second roadmap. Read both. Whenever a security-relevant `gcp.md` section is taught, also teach every companion concept bound to it (§2) in the same session, as one story. Similar, related, and overlapping security concepts are stitched and taught in parallel — never in separate sessions, never twice.**

Why: `gcp.md` owns the *roadmap spine* — what to learn, in what order, tied to certs (PCA, Cloud Security Engineer, Network Engineer, SecOps, SCS-C03, etc.) and the provider service maps. It lists security topics at outline depth (A5 networking, A10 crypto/security fundamentals, B1 shared responsibility, B5 IAM model, Track C container/K8s hardening, Phase 4 GCP Security services). It does not own attacker playbooks, misuse cases, rate-limit/WAF craft, session/JWT/OAuth failure modes, supply-chain attacker paths, IR tabletop depth, AI threat mechanics, or a full applied-cryptography track. This file supplies those and hangs each piece on the `gcp.md` section that needs it **when that section is taught**.

### 0.2 Stitching rules

1. **One concept, one teaching.** If both files mention an idea, teach it once in the owner (§2.1), and the other file only *adds*. Later sessions recall in one line.
2. **Ownership split.** *`gcp.md` owns:* learning order, cert mapping, service vocabulary (IAM, Armor, VPC-SC, KMS, SCC, SecOps), shared-responsibility framing at roadmap level. *This file owns:* attack mechanics, defensive design patterns, cryptography depth (`CR-*`), network-security attacks, exercise/scenario bank, IR tabletops.
3. **Same teaching discipline.** Issue **one** exercise at a time; learner attempts before keys; predict blast radius / control placement before revealing the answer. Prop Lock: do not use a later control (VPC-SC, Confidential VM, Binary Authorization) as a "known" prop before its `gcp.md` section has been covered — postpone the exercise or teach the prerequisite first.
4. **GCP lens at three depths** when a concept is taught: **Lens-1** name the GCP (and AWS/Azure twin from `gcp.md` mapping tables) resource; **Lens-2** touch via local vulnerable-by-design fixture or credits-safe lab; **Lens-3** cert-depth trade-offs (Cloud Security Engineer / PCA Security / SCS-C03).
5. **Bank ≠ dump.** §5 is a bank of scenario specs. Never paste Appendix K before an attempt.
6. **Predict → attempt → discrepancy → ledger.**
7. **Qualitative keys only** (no invented lab DB goldens).
8. **Inline tracking** with `- [ ]` boxes.
9. **Honesty:** `(verify)` on version-sensitive cloud product details.
10. **Lab safety hard bans:** no scanning third parties; no malware; no live DDoS; no credential stuffing against real accounts; fixtures on localhost / disposable projects only; crypto via vetted libraries only.
11. **User can override** skip/jump. On conflict: `gcp.md` wins on order and cert timing; this file wins on security/crypto content and exercise specs.
12. **Read economically:** §0 + §2, then only today's bound modules.

### 0.3 How one stitched session runs

1. **Anchor** — name the `gcp.md` section (e.g. A10, B5, Phase 4 Security) and list bound companion IDs from §2.
2. **Concept** — teach roadmap idea once, then layer attack/crypto depth from this file.
3. **GCP lens** — Lens-1 always; Lens-2 when Lab Reality allows.
4. **Numbers** — one estimate (QPS to throttle, key size, blast radius, RTO/RPO for IR).
5. **Exercise** — one card from §5 (prediction first).
6. **Check** — module check questions; learner answers first.
7. **Close** — tick boxes; note unlocked / shaky / postponed.

### 0.4 Notation

- `PQ-S-*` foundations · `TH-*` threat modeling · `CR-*` cryptography · `AU-*` auth/session attacks · `AB-*` API/abuse · `DOS-*` denial of service · `WA-*` web/app attacks · `CL-*` cloud-native attacks · `NT-*` network/zero-trust · `CK-*` containers/K8s · `WL-*` supply chain · `IR-*` detection/IR · `AI-*` AI/LLM threats · `SC-*` side channels/isolation · `PV-*` privacy · `CM-*` compliance literacy
- `SEC-E*` / `CR-E*` / `SEC-Z0.*` exercises · `SEC-CAP1–SEC-CAP4` capstones
- `gcp.md` IDs: `A5`, `A7`, `A10`, `B1`, `B5`, `C1`, `C2`, `Phase4-Sec`, `Phase4-Net`, cert names (PCA, Cloud Security Engineer, …)

### 0.5 University alignment (coverage checklist)

| Course / framework | Maps into |
|---|---|
| Stanford CS155 | TH, AU, WA, NT, DOS, CL, AI |
| Stanford CS255 | CR-01 … CR-20 |
| Stanford XACS235 Cloud Security | B1/CL shared responsibility, CK/WL, CR-14, IR, CM, SC/TEEs |
| MIT 6.858 / 6.566 | TH, CK isolation, WA, NT/TLS, SC, AU |
| Berkeley CS161 | CR foundations, NT, DOS, WA, AU |
| CMU Cloud Security | CL multi-tenancy, B5/IAM abuse, IR, CM |
| CSA CCM v4.x | §8 checklist (not a control dump) |
| OWASP Top 10:2025 · ATT&CK Cloud | WA, AU, CL, WL, IR |

---

## 1. Coverage ledger

| Area | Content | Modules |
|---|---|---|
| Foundations | principles beyond one-liners, shared responsibility matrices, security economics | PQ-S-* |
| Threat modeling | STRIDE, attack trees, ATT&CK cloud, trust boundaries | TH-* |
| Cryptography | goals/games → AEAD → PKI/TLS → passwords → KMS → side channels → TEEs → PQC | CR-01…CR-20 |
| AuthN/AuthZ attacks | hijack, fixation, CSRF, JWT/OAuth failures, stuffing, MFA fatigue, IDOR | AU-* |
| API abuse | rate limits, bots, scraping, GraphQL DoS, enumeration | AB-* |
| Denial of service | L3–L7, amplification, slowloris, economic DoS, Adaptive Protection | DOS-* |
| Web/app attacks | injection, XSS, SSTI, deserialization, CSP, clickjacking | WA-* |
| Cloud-native | SSRF/metadata, public buckets, IAM privesc, confused deputy, tenant isolation | CL-* |
| Network / zero trust | lateral movement, egress exfil, DNS tunneling, IAP vs VPN threat models | NT-* |
| Containers / K8s | escape patterns, privileged pods, RBAC wildcards, secrets | CK-* |
| Supply chain | poisoned images/deps, CI compromise, SBOM/signing | WL-* |
| Detection / IR | log gaps, alert design, ephemeral forensics, ransomware | IR-* |
| AI / LLM apps | prompt injection, tool abuse, RAG leakage | AI-* |
| Side channels / TEEs | timing/cache awareness, confidential computing | SC-* |
| Privacy / compliance lite | classification, DLP, CCM/SOC2/PCI literacy | PV-*, CM-* |
| Exercises & capstones | scenario bank + SEC-CAP1–SEC-CAP4 | §5–§6 |

---

## 2. Stitch table — teach these with `gcp.md`

| `gcp.md` section | Companion modules (same session) | Checkpoint |
|---|---|---|
| **A5 Networking** (OSI/TCP/IP, DNS, HTTP, TLS intro, LB, firewalls, VPN) | NT-*, DOS-01…03, CR-11/CR-12 (TLS depth), WA-01 (HTTP attacker model) | E-NT1, CR-E12 |
| **A7 APIs** (OAuth/JWT/API keys awareness) | AU-05…10, AB-*, CR-10 (JWT as signed object) | E-AU3, CR-E4 |
| **A10 Security & Cryptography Fundamentals** | PQ-S-*, TH-*, **CR-01…CR-13**, AU-01…04, WA-* overview, DOS overview | CR-E1…E8, SEC-Z0.* |
| **B1 Shared responsibility** | PQ-S-03, CL-01, CM-01 | E-CL1 |
| **B5 Cloud IAM Concepts** | AU-11…14, CL-03…05 (IAM abuse / SA keys / confused deputy) | E-CL3 |
| **C1 Docker security** | CK-01…03, WL-01 (image poison), CR-14 secrets | E-CK1 |
| **C2 Kubernetes RBAC / PSS / admission** | CK-04…06, WL-02…03, NT-04 (east-west) | E-CK2 |
| **Phase 4 GCP — Networking + Cloud Armor / Armor** | DOS-*, AB-01…04, NT-05…06, WA-WAF cards | E-DD2, E-AB1 |
| **Phase 4 GCP — Security (IAM, KMS, VPC-SC, BinAuth, SCC, SecOps)** | CR-14…CR-20, CL-*, WL-*, IR-*, SC-*, VPC-SC exfil (NT-07) | CR-E9…E15, SEC-CAP1 |
| **Cloud Security Engineer cert track** | all CL/NT/IR/CR-14+, CM-* | SEC-CAP2 |
| **Cloud Network Engineer cert track** | NT-*, DOS-*, A5 revisit | E-NT3 |
| **Security Operations Engineer / SCS-C03** | IR-*, TH-05 ATT&CK, IR capstone | SEC-CAP3 |
| **GenAI / Agentic (Phase 3–4 / Agentic Architect)** | AI-*, CR-18 awareness, PV-* | SEC-CAP4 |
| **AWS Security Specialty / Azure SC-100 (later phases)** | same mechanics; map controls via `gcp.md` provider tables — no new theory | IR mapping drill |

### 2.1 Overlap register — teach once

| Idea | Owner | This file adds |
|---|---|---|
| Shared responsibility one-liner | `gcp.md` B1 | PQ-S-03 matrices by service model |
| TLS handshake vocabulary | `gcp.md` A5/A10 | CR-12 attacks, 0-RTT, validation bugs |
| IAM principals/roles | `gcp.md` B5 | CL IAM privesc / key sprawl playbooks |
| "Use KMS/CMEK" | `gcp.md` Phase 4 Security | CR-14 envelope hierarchy + compromise IR |
| Armor / DDoS product names | `gcp.md` Phase 4 Net | DOS taxonomy + rate-limit/bot design |
| Container non-root / PSS | `gcp.md` C1/C2 | CK escape & supply-chain attacker paths |
| OAuth/JWT mentioned | `gcp.md` A7 | AU/CR failure modes (alg confusion, mix-up) |

---

## 3. Concept curriculum

Each module: checkbox · stitch IDs · Attack · Why it works · Defense pattern · GCP lens · Lab · Check.
Teach in stitch order (§2), not in ID order. Prop Lock applies.

### 3.1 Security prerequisites (PQ-S-01 … PQ-S-06)

#### PQ-S-01 · Crypto hygiene recall (not a course) — stitch: T.SysTheory · CR-01 gate
- [ ] unlocked
- **Attack:** Learner treats Base64 or a homemade XOR as 'encryption'; ships secrets in URLs; uses `Math.random` for tokens.
- **Why it works:** Encoding ≠ confidentiality; non-CSPRNG is predictable; Kerckhoffs: assume algorithm is public.
- **Defense pattern:** Only vetted AEAD + CSPRNG; never invent crypto; mark every secret path for Secret Manager.
- **GCP lens:** Lens-1: Secret Manager + KMS names. Lens-2: local CSPRNG token gen. Lens-3: PCA 'protect data' themes.
- **Lab:** SEC-Z0.1: classify 8 snippets as encoding / hashing / MAC / encryption / nothing.
- **Check:** Can you state Kerckhoffs and name one encoding-vs-encryption confusion?

#### PQ-S-02 · Principles beyond CIA (Saltzer/Schroeder add-ons) — stitch: Phase4-Sec.1 recall
- [ ] unlocked
- **Attack:** Control that is optional to call (incomplete mediation); complex multi-path auth; shared mutable policy cache without isolation.
- **Why it works:** Attackers use the path you forgot to check; complexity hides bugs; shared mechanism couples blast radius.
- **Defense pattern:** Complete mediation; fail-safe defaults; economy of mechanism; least common mechanism; psychological acceptability — *recall* CIA/least-privilege/defense-in-depth/assume-breach/zero-trust/shared-responsibility from 7.1.
- **GCP lens:** Lens-1: IAM deny policies + org policy as fail-safe defaults. Lens-2: paper control matrix.
- **Lab:** SEC-Z0.3: map each Saltzer principle to one the reference cloud app control.
- **Check:** Name three principles beyond CIA and one GCP embodiment each.

#### PQ-S-03 · Shared responsibility matrices (IaaS/PaaS/SaaS/serverless) — stitch: B5 IAM · 7.1 · XACS235
- [ ] unlocked
- **Attack:** Team assumes Google patches guest OS on GCE; or assumes Cloud Run means zero authz duty; public bucket blamed on CSP.
- **Why it works:** Responsibility splits by abstraction: you always own identity, data classification, who can invoke, logging config; CSP owns physical/hypervisor/baseline managed hardening — but *misconfig is on you*.
- **Defense pattern:** Fill a matrix per service: patch guest OS? network ACL? app AuthZ? key custody? For serverless, still own IAM invoker + app bugs.
- **GCP lens:** Lens-1: Cloud Run vs GCE vs GCS rows. Lens-2: annotate Part 0 hierarchy with trust boundaries.
- **Lab:** SEC-E1.2: complete matrix for Cloud Run + Cloud SQL + GCS.
- **Check:** Who owns guest OS patching on GCE vs runtime CVE response on Cloud Run?

#### PQ-S-04 · HTTP/TLS bits & browser security model preview — stitch: A5 TLS / Phase 4 Armor · F1 · WA-01
- [ ] unlocked
- **Attack:** Learner confuses TLS termination with end-to-end authenticity to the app identity; ignores cookies' SameSite.
- **Why it works:** HTTP is request/response with deferred security; browsers enforce SOP; TLS authenticates the *server cert to name*, not your AuthZ.
- **Defense pattern:** Separate transport security (CR-12) from session (AU-*) from AuthZ (AU-11). Draw Client→GFE→LB→Run.
- **GCP lens:** Lens-1: managed cert on Application LB. Lens-2: curl -v TLS to run.app.
- **Lab:** SEC-Z0.2: label each hop's trust assumption.
- **Check:** Does HTTPS alone stop CSRF? Why/why not?

#### PQ-S-05 · Security economics & incentives — stitch: Phase4-Sec.1 · MIT 6.858
- [ ] unlocked
- **Attack:** Under-invest in detection because breaches are rare *in the teacher's sample*; over-invest in checkbox crypto theater.
- **Why it works:** Attackers amortize tooling; defenders pay per asset; asymmetric information; moral hazard in shared cloud.
- **Defense pattern:** Price residual risk in ADRs; prefer controls with high attacker cost / low user friction; measure MTTD/MTTR.
- **GCP lens:** Lens-1: SCC finding severity as prioritization input. Lens-2: cost of standing global LB vs Hosting edge.
- **Lab:** SEC-E1.3: one the reference cloud app ADR that prices a control vs accept risk.
- **Check:** Give one example of checkbox security that fails incentive alignment.

#### PQ-S-06 · Threat-modeling warmup (STRIDE one-pager) — stitch: B4 · TH-02
- [ ] unlocked
- **Attack:** Jumping to products without naming threats; 'we have Armor' as a threat model.
- **Why it works:** Without assets + trust boundaries + STRIDE, controls are ornaments.
- **Defense pattern:** For `PlaceOrder`: diagram · STRIDE row · one abuse case · one residual risk sentence.
- **GCP lens:** Lens-1: none yet — paper. Lens-2: attach later products only after threats named.
- **Lab:** SEC-E1.1
- **Check:** What is the difference between a threat and a control?

### 3.2 Threat taxonomy & modeling (TH-01 … TH-06)

#### TH-01 · Attacker models: web vs network vs cloud-admin vs co-tenant — stitch: CS155 · 0.4
- [ ] unlocked
- **Attack:** Design only against 'script kiddie on the internet'; miss insider SA, malicious co-tenant probing IMDS, or network MITM on legacy VPN.
- **Why it works:** Different attackers have different capabilities: web (malicious site, XSS sink), network (on-path), cloud-admin (IAM), co-tenant (noisy/side-channel/isolation).
- **Defense pattern:** Name the attacker model at the top of every threat model; pick controls that match capabilities.
- **GCP lens:** Lens-1: IAP reduces network-attacker relevance for admin UI. Lens-2: paper table.
- **Lab:** SEC-E1.4
- **Check:** Which attacker model does VPC-SC primarily frustrate?

#### TH-02 · Trust boundaries & asset inventory for the reference cloud app — stitch: B4
- [ ] unlocked
- **Attack:** Flat 'inside VPC = trusted'; secrets treated as code assets.
- **Why it works:** Breach crosses the weakest unlabeled boundary; assets without owners lack controls.
- **Defense pattern:** Draw org/folder/project · FE/API/admin/s2s/data/CI planes · label data classes.
- **GCP lens:** Lens-1: resource hierarchy. Lens-2: annotate existing the reference cloud app HLD.
- **Lab:** SEC-E1.1
- **Check:** List five the reference cloud app assets and their trust boundary.

#### TH-03 · STRIDE applied — stitch: B4 · 7.4
- [ ] unlocked
- **Attack:** Skipping elevation-of-privilege; treating Spoofing as 'solved by HTTPS'.
- **Why it works:** STRIDE structures brainstorming; each letter maps to CIA+AuthZ concerns.
- **Defense pattern:** One STRIDE table per critical flow; link to tests.
- **GCP lens:** Lens-1: map Spoofing→Identity Platform/IAM; Tampering→KMS/Binary Auth; DoS→Armor.
- **Lab:** SEC-E1.1
- **Check:** Give a the reference cloud app Elevation example that HTTPS does not stop.

#### TH-04 · Attack trees & abuse cases as tests — stitch: 3.0 · 4.7
- [ ] unlocked
- **Attack:** Threat model slides with no failing test; abuse case only in prose.
- **Why it works:** Trees force AND/OR attacker paths; abuse cases become negative tests.
- **Defense pattern:** Convert top 3 trees into table-driven deny tests.
- **GCP lens:** Lens-1: Cloud Build test job runs abuse suite.
- **Lab:** SEC-E2.4
- **Check:** What makes an abuse case 'testable'?

#### TH-05 · ATT&CK cloud TTPs (incl. T1552.005) — stitch: Phase4-Sec.6 · CL-01
- [ ] unlocked
- **Attack:** Only thinking in CVE IDs; missing credential-access via metadata.
- **Why it works:** ATT&CK gives shared vocabulary for detection; T1552.005 is classic SSRF→IMDS.
- **Defense pattern:** Map the reference cloud app detections to a few techniques; do not boil the ocean.
- **GCP lens:** Lens-1: SCC + Chronicle literacy. Lens-2: parse one audit log for GetAccessToken-like events (verify names).
- **Lab:** SEC-E7.3
- **Check:** State T1552.005 in one sentence.

#### TH-06 · Distributed-system threat concepts — stitch: 8 · primer
- [ ] unlocked
- **Attack:** Assuming consensus implies honesty of operators; ignoring poisoned configs across regions.
- **Why it works:** Replication multiplies trust; control planes are high-value; eventual consistency delays revocation.
- **Defense pattern:** Threat-model the control plane separately; pin digests multi-region.
- **GCP lens:** Lens-1: org policy + Binary Authorization across projects.
- **Lab:** SEC-E8.2
- **Check:** Why is revoke-propagation latency a security property?

### 3.3 Cryptography — first-class pillar (CR-01 … CR-20)

*Equal scale to AU/AB/CL. Roadmap A10 / B5 / API auth patterns owns password/JWT *product* labs; GCP KMS / CMEK (Phase 4 Security) owns CMEK *product* spine; CR owns cryptographic justification and failure modes. Stanford CS255 alignment: see §B5 IAM.*

#### CR-01 · Crypto goals & threat models (IND-CPA/CCA; EUF-CMA; Kerckhoffs) — stitch: CS255 · PQ-S-01
- [ ] unlocked
- **Attack:** Claiming 'encrypted' without a game; reinventing algorithms 'because secret'.
- **Why it works:** Security is defined against a class of attackers with oracles; Kerckhoffs: secrecy is in keys, not algorithms.
- **Defense pattern:** State goal (confidentiality/integrity/auth) + game (IND-CPA/CCA, EUF-CMA) before picking a primitive.
- **GCP lens:** Lens-1: KMS key purpose ENCRYPT_DECRYPT vs ASYMMETRIC_SIGN (verify). Lens-2: paper games.
- **Lab:** CR-E1: for three the reference cloud app fields, name goal + required game.
- **Check:** Explain IND-CPA vs IND-CCA in one example with an active attacker.

#### CR-02 · Classical failures & why roll-your-own dies — stitch: CS255 · PQ-S-01
- [ ] unlocked
- **Attack:** ECB screenshot leakage; homemade XOR stream reuse; Base64 'encryption'; compressing then encrypting secrets (CRIME-class intuition).
- **Why it works:** Structure leaks under ECB; keystream reuse is two-time pad; encoding is reversible without a key.
- **Defense pattern:** Ban roll-your-own; use AEAD (CR-04); code review rejects custom crypto.
- **GCP lens:** Lens-1: none — library policy. Lens-2: show ECB penguin-style demo on synthetic image *offline*.
- **Lab:** CR-E2
- **Check:** Why is 'XOR with password' not encryption under Kerckhoffs?

#### CR-03 · Block ciphers & AES; modes ECB/CBC/CTR; padding oracles — stitch: CS255 · CS155
- [ ] unlocked
- **Attack:** CBC without integrity → padding oracle (Vaudenay); CTR nonce reuse; ECB patterns.
- **Why it works:** Malleability + padding validation leaks plaintext bits; nonce reuse in CTR keystream-collides.
- **Defense pattern:** Do not use raw CBC for new systems; prefer AEAD; if legacy CBC, encrypt-then-MAC (CR-06) and constant-time padding handling.
- **GCP lens:** Lens-1: Tink / language libs; KMS uses approved modes (verify). Lens-2: conceptual padding-oracle story card.
- **Lab:** CR-E3
- **Check:** What does a padding oracle return that enables decryption?

#### CR-04 · Authenticated encryption: GCM, ChaCha20-Poly1305; nonce reuse — stitch: CS255
- [ ] unlocked
- **Attack:** AES-GCM with random 96-bit nonce *reused* under the same key → catastrophic forgery/confidentiality loss; truncated tags.
- **Why it works:** AEAD binds confidentiality+integrity; GCM is fragile to nonce reuse; ChaCha20-Poly1305 often preferred in software.
- **Defense pattern:** Unique nonces (counter/XChaCha); key rotation limits; never truncate tags below ~128 bits without analysis; prefer lib defaults (Tink).
- **GCP lens:** Lens-1: Application-layer AEAD via Tink; TLS stacks pick AEAD suites. Lens-2: unit test that rejects reused nonce in a toy wrapper.
- **Lab:** CR-E5
- **Check:** What is lost if AES-GCM nonce repeats?

#### CR-05 · Hash functions: collision/preimage; SHA-2/3; length extension; HKDF — stitch: CS255
- [ ] unlocked
- **Attack:** Using bare SHA-256 as a MAC; Merkle-Damgård length extension on `H(secret||msg)`; HKDF misused as general PRF with attacker-controlled salt carelessly.
- **Why it works:** Collision ≠ preimage; MD constructions allow length extension; HKDF extracts then expands with labeled info.
- **Defense pattern:** HMAC/KMAC for authenticity; HKDF for key derivation with explicit `info`; prefer SHA-2/3 from libs.
- **GCP lens:** Lens-1: checksums in Artifact Registry ≠ MAC. Lens-2: demo length extension conceptually on paper.
- **Lab:** CR-E6
- **Check:** Why is `H(secret||msg)` not a secure MAC for MD hashes?

#### CR-06 · MACs: HMAC, Poly1305; EtM vs MtE — stitch: CS255 · CR-03
- [ ] unlocked
- **Attack:** MAC-then-encrypt enabling padding oracles; timing leaks on compare; truncated HMAC.
- **Why it works:** Order matters: encrypt-then-MAC (or AEAD) authenticates ciphertext; MtE authenticates plaintext and can interact badly with decryption errors.
- **Defense pattern:** Prefer AEAD; if composing, EtM with constant-time compare; never roll Poly1305 alone without the AEAD construction.
- **GCP lens:** Lens-1: signed requests in 4.5 use HMAC — recall roadmap lab; CR adds composition rules.
- **Lab:** CR-E7
- **Check:** State preferred composition order and why.

#### CR-07 · Randomness: CSPRNG, entropy, nonce/IV; cloud RNG pitfalls — stitch: CS255 · 1.2
- [ ] unlocked
- **Attack:** Tokens from `Math.random` / `random.random`; VM snapshots cloning PRNG state; low-entropy boot in containers.
- **Why it works:** Security tokens need unpredictability; fork/clone can duplicate state; nonce uniqueness is a resource.
- **Defense pattern:** OS CSPRNG (`getrandom`, `SecureRandom`); avoid inventing entropy gatherers; after snapshot restore, ensure uniqueness strategy (counters + key id).
- **GCP lens:** Lens-1: Cloud Run/GCE — use platform RNG via language stdlib. Lens-2: generate 128-bit session ids; prove bit length.
- **Lab:** CR-E11
- **Check:** Name one cloud-specific RNG failure mode.

#### CR-08 · Diffie–Hellman & ECDH; forward secrecy; invalid-curve — stitch: CS255 · CR-12
- [ ] unlocked
- **Attack:** Static DH without ephemeral → no forward secrecy; small-subgroup / invalid-curve if point not validated.
- **Why it works:** ECDHE gives FS if ephemeral secrets are erased; invalid points can leak private keys in poor implementations.
- **Defense pattern:** Use TLS stacks that do ECDHE + validation; never implement curve arithmetic yourself.
- **GCP lens:** Lens-1: SSL policy min TLS 1.2+ with modern suites (verify). Lens-2: paper FS timeline (compromise tomorrow vs session today).
- **Lab:** CR-E12
- **Check:** What does forward secrecy guarantee if the server long-term key leaks tomorrow?

#### CR-09 · Public-key encryption: RSA-OAEP; hybrid encryption; raw RSA fails — stitch: CS255
- [ ] unlocked
- **Attack:** Raw RSA textbook encryption; RSA without OAEP; using signing keys for encryption.
- **Why it works:** Deterministic/malleable RSA leaks; hybrid encrypts a DEK with KEM/PKE then AEAD-bulk data.
- **Defense pattern:** RSA-OAEP or modern KEM; always hybrid for bulk; separate key purposes.
- **GCP lens:** Lens-1: KMS asymmetric encrypt purpose; envelope with KMS (CR-14). Lens-2: sketch hybrid box diagram.
- **Lab:** CR-E13
- **Check:** Why is hybrid encryption used for a 10 MB object?

#### CR-10 · Signatures: RSA-PSS, ECDSA, Ed25519; malleability; agility attacks — stitch: CS255 · 4.5 · 7.5
- [ ] unlocked
- **Attack:** JWT `alg=none` / HS256 with RSA public key as HMAC secret (algorithm confusion); ECDSA nonce reuse → private key; accepting attacker `jku`.
- **Why it works:** Verification must pin algorithm+key; agility without policy is an attack surface; ECDSA needs trustworthy nonce.
- **Defense pattern:** Allowlist alg; one purpose per key; use maintained JOSE; Ed25519/RSA-PSS from libs; pin JWKS from config not URL.
- **GCP lens:** Lens-1: Binary Authorization attestations / Sigstore literacy (verify). Lens-2: AU-05 lab pairing.
- **Lab:** CR-E4, SEC-E3.5
- **Check:** Explain JWT algorithm confusion in one sentence.

#### CR-11 · Certificates & PKI: X.509, chains, CT, pinning, ACME — stitch: A5 TLS / Phase 4 Armor · CS255
- [ ] unlocked
- **Attack:** Missing chain validation; accepting expired; pinning that breaks rotation; ignoring name verify.
- **Why it works:** PKI binds keys to names via trusted CAs; CT detects mis-issuance; pinning trades tightness for operability.
- **Defense pattern:** Default: system trust store + hostname verify + revocation strategy as offered; pinning only with ops plan; prefer managed certs.
- **GCP lens:** Lens-1: Google-managed certs on Application LB; Certificate Manager (verify). Lens-2: openssl s_client chain read.
- **Lab:** CR-E14
- **Check:** What does Certificate Transparency buy you?

#### CR-12 · TLS 1.2 vs 1.3: handshake, 0-RTT, validation bugs, HSTS — stitch: A5 TLS / Phase 4 Armor · 6.13 · CS255
- [ ] unlocked
- **Attack:** Downgrade to weak suites; skipping cert validate in custom clients; 0-RTT replay; missing HSTS on cookies-only sites.
- **Why it works:** TLS 1.3 cleans handshake and forbids many legacy options; 0-RTT is replayable; validation bugs are perennial in custom code.
- **Defense pattern:** Min TLS 1.2+ (prefer 1.3); SSL policies; no custom verify; HSTS with care; treat 0-RTT as unsafe for non-idempotent.
- **GCP lens:** Lens-1: `google_compute_ssl_policy` min_tls_version (verify). Lens-2: compare handshake wire shapes on paper.
- **Lab:** CR-E15, SEC-E2.1
- **Check:** Why can TLS 1.3 0-RTT be dangerous for POST /transfer?

#### CR-13 · Password cryptography: Argon2id/scrypt/bcrypt; salt; pepper — stitch: A10/B5.3 owner labs
- [ ] unlocked
- **Attack:** Fast hashes (SHA-256) as password storage; unsalted; global pepper in source; composition theater instead of length+KDF.
- **Why it works:** Offline brute force is GPU-bound; salt prevents rainbows; memory-hard KDFs raise attacker cost; pepper is keyed hash needing custody.
- **Defense pattern:** *Roadmap 4.3 owns product labs.* CR adds: threat model (online vs offline), parameter tuning rationale, pepper in KMS, migration/version field.
- **GCP lens:** Lens-1: pepper in Secret Manager/KMS. Lens-2: recall 4.3 Argon2id lab — add threat-model paragraph.
- **Lab:** CR-E8
- **Check:** Why is bcrypt/Argon2id preferred over SHA-256 for passwords?

#### CR-14 · Key management: hierarchy, envelope, rotation, SoD; KMS/HSM/EKM/CMEK/CSEK — stitch: Phase4-Sec.3 owner product
- [ ] unlocked
- **Attack:** One master key encrypts everything forever; DEKs logged; humans export private keys; CSEK in client without threat model.
- **Why it works:** Envelope: KEK wraps DEKs; hierarchy limits blast radius; HSM/EKM raise custody; rotation needs rewrap plan; SoD separates use vs admin.
- **Defense pattern:** *7.3 owns CMEK lab.* CR adds: hierarchy diagram, rewrap vs re-encrypt, key purpose separation, when CMEK vs CSEK vs Google-managed.
- **GCP lens:** Lens-1: Cloud KMS key ring/key; CMEK on GCS/SQL (verify); Cloud HSM/EKM literacy. Lens-2: local envelope toy from 7.3 + hierarchy labels.
- **Lab:** CR-E9, CR-E10
- **Check:** Draw KEKs and DEKs for a GCS object + a DB field.

#### CR-15 · Key compromise & crypto agility; IR for leaked keys — stitch: Phase4-Sec.8 · IR-05
- [ ] unlocked
- **Attack:** No inventory of where a key was used; rotation that leaves old ciphertext forever decryptable without policy; JWT keys without cutoff.
- **Why it works:** Compromise requires: detect → contain (disable) → rewrap/reissue → invalidate sessions/tokens → hunt usage window.
- **Defense pattern:** Key inventory; dual-key overlap rotation; incident cutoff timestamps for JWT; runbook branch for KMS disable + SA key delete.
- **GCP lens:** Lens-1: KMS key state disable/destroy schedule (verify); Secret Manager versions. Lens-2: tabletop CR-15+IR-05.
- **Lab:** SEC-E7.5, CR-E16
- **Check:** List five steps after a DEK leak vs a KEK leak.

#### CR-16 · Side channels applied: timing, padding oracle, cache; constant-time APIs — stitch: MIT 6.858 · SC-01
- [ ] unlocked
- **Attack:** Early-exit compare on MACs; error messages distinguishing padding vs MAC failure; sharing cores with hostile tenants for high-value keys without threat model.
- **Why it works:** Remote timing and error oracles leak secrets; shared hardware enables microarchitectural leaks at high effort.
- **Defense pattern:** Constant-time compare APIs from libs; uniform errors; prefer KMS so key ops leave your VM; Confidential VM when threat model demands (CR-18).
- **GCP lens:** Lens-1: KMS remote crypto ops. Lens-2: broken vs fixed compare unit test.
- **Lab:** CR-E17
- **Check:** Why should MAC compare not short-circuit?

#### CR-17 · Secure channels beyond TLS: mTLS, app AEAD, field-level encryption — stitch: Phase4-Sec.3 · 4.8
- [ ] unlocked
- **Attack:** Stopping at TLS termination and writing plaintext PII to logs/DB; mTLS without cert lifecycle.
- **Why it works:** TLS protects on the wire to the peer you authenticated; app AEAD protects data at rest/across hops; field-level limits insider/DBA read.
- **Defense pattern:** mTLS or IAM+ID tokens for s2s; Tink AEAD for fields; never log plaintext secrets; key per tenant when required.
- **GCP lens:** Lens-1: Cloud Run service-to-service ID tokens; CMEK; application AEAD. Lens-2: encrypt one PII field before insert.
- **Lab:** CR-E18
- **Check:** When is field-level encryption worth the query-friction cost?

#### CR-18 · Privacy-enhancing crypto survey: TEEs, MPC, HE, ZKP awareness — stitch: XACS235 · SC-03 · 9c
- [ ] unlocked
- **Attack:** Assuming Confidential VM stops SQL injection; assuming HE is free performance; marketing ZKP without a statement.
- **Why it works:** TEEs reduce operator/host visibility with attestation trust; MPC/HE/ZKP buy specific properties at cost; none replace AuthZ.
- **Defense pattern:** Threat-model what TEE covers (memory confidentiality vs app bugs); know HE/MPC/ZKP exist for multi-party analytics — survey depth only.
- **GCP lens:** Lens-1: Confidential VM / Confidential GKE / Confidential Space literacy (verify). Lens-2: write 'buys/costs' paragraph.
- **Lab:** CR-E19, SEC-E8.5
- **Check:** Name one threat Confidential VM mitigates and one it does not.

#### CR-19 · Post-quantum migration awareness — stitch: CR-11 · CR-12
- [ ] unlocked
- **Attack:** Long-lived signatures/archives with only classical algorithms and no inventory; ignoring hybrid TLS experiments.
- **Why it works:** Store-now-decrypt-later threatens long-secrecy data; PQ migration needs inventory + crypto agility (CR-15).
- **Defense pattern:** Inventory long-lived keys/signatures; follow platform hybrid TLS as offered (verify); prefer agility in designs now.
- **GCP lens:** Lens-1: watch Google Cloud PQ/TLS announcements (verify). Lens-2: inventory the reference cloud app keys by lifetime.
- **Lab:** CR-E20
- **Check:** What is store-now-decrypt-later?

#### CR-20 · Crypto engineering checklist for the reference cloud app — stitch: A10/B5.9 · 7.3 · all CR
- [ ] unlocked
- **Attack:** One-off decisions without a checklist; copying Stack Overflow crypto.
- **Why it works:** Checklists catch omitted integrity, nonce policy, key purpose, library choice.
- **Defense pattern:** Mandatory: vetted lib (Tink/libsodium/stdlib); AEAD; CSPRNG; KMS for KEKs; no tokens in URLs; TLS verify on; alg allowlists; versioned password records; inventory.
- **GCP lens:** Lens-1: ADR linking checklist to Secret Manager/KMS/Armor TLS. Lens-2: audit the reference cloud app against checklist.
- **Lab:** SEC-CAP1 uses this checklist
- **Check:** Recite eight non-negotiables for the reference cloud app crypto.

### 3.3.1 Cryptography pillar coda — assessment & Prop Lock

**Skip-test for CR track (SEC-T1+SEC-T2 in §4):** learner must, unaided: (1) state IND-CPA vs integrity goals with one example each; (2) explain why ECB and raw RSA fail; (3) give GCM nonce-reuse consequence; (4) prefer AEAD over CBC+HMAC DIY; (5) sketch envelope KEK/DEK with KMS; (6) name TLS 1.3 0-RTT risk; (7) justify Argon2id over SHA-256 for passwords; (8) list eight CR-20 checklist items for the reference cloud app.

**Prop Lock for crypto props:** do not use Cloud HSM, EKM, Confidential Space, or Binary Authorization as assumed props before their gcp.md gcp.md sections (7.3 / 7.5) and companion CR-14 / CR-18 / WL-04 are unlocked. Local AEAD/HMAC toys may use Tink without those props.

**Pairing rule with A10 / B5 / API auth patterns & 7.3:** A10 / B5 / API auth patterns owns password *product* labs and JWT *policy* labs; CR-13/CR-10 own the cryptographic *why* and failure modes. GCP KMS / CMEK (Phase 4 Security) owns CMEK *clickpath*; CR-14 owns hierarchy theory and SoD. Teach as one story per §2 stitch rows.

**Common failure markers (mark shaky, do not shame):** saying "TLS means the DB is encrypted"; treating Base64 as confidentiality; enabling `alg` from untrusted JWT headers; logging DEKs; claiming Confidential VM stops SQLi; shipping `Math.random` session ids.

**Recommended CR session bundles (when spine allows):**
1. CR-01…04 + CR-E1…E5 with Part A5 TLS / Phase 4 Armor TLS day (channel vs object encryption distinction).
2. CR-05…07 + CR-13 with A10 / B5 / API auth patterns.3 (password/KDF day).
3. CR-08…12 with Part A5 TLS / Phase 4 Armor / 6.13 (PKI/TLS depth).
4. CR-14…15 + CR-20 with GCP KMS / CMEK (Phase 4 Security) / 7.8 (KMS + key IR).
5. CR-16…19 with GCP KMS / CMEK (Phase 4 Security) Confidential Computing literacy + 9c privacy (survey depth).

### 3.4 Authentication & session attacks (AU-01 … AU-14)

#### AU-01 · Session hijacking — stitch: A10/B5.4
- [ ] unlocked
- **Attack:** Steal session cookie via XSS, malware, or network on non-Secure cookies; replay until idle/absolute timeout.
- **Why it works:** Bearer cookie is capability; XSS bypasses HttpOnly? No — HttpOnly blocks JS, but XSS still can drive CSRF-like actions if CSRF weak; network theft if no Secure/TLS.
- **Defense pattern:** Secure+HttpOnly+SameSite; TLS everywhere; rotate on privilege change; bind to UA/IP *carefully* (false positives); short idle+absolute; XSS defense (WA-02).
- **GCP lens:** Lens-1: Identity Platform session policy literacy (verify). Lens-2: local cookie jar attack on fixture.
- **Lab:** SEC-E2.2
- **Check:** Which cookie flags stop which theft paths?

#### AU-02 · Session fixation — stitch: A10/B5.4
- [ ] unlocked
- **Attack:** Attacker sets victim's session id pre-login; victim authenticates; attacker reuses id.
- **Why it works:** If server accepts client-chosen session id or fails to rotate on login, fixation binds attacker to authenticated session.
- **Defense pattern:** Always mint new session id on login/reauth/privilege change; destroy old; reject client-supplied ids.
- **GCP lens:** Lens-1: app session store. Lens-2: fixation test fails then passes.
- **Lab:** SEC-E2.3
- **Check:** What single server behavior defeats classical fixation?

#### AU-03 · CSRF — stitch: A10/B5.4 · WA-01
- [ ] unlocked
- **Attack:** Malicious site triggers state-changing request with victim cookies (form POST, image GET misused).
- **Why it works:** Browsers attach cookies on cross-site requests per policy; without CSRF token / Fetch Metadata checks, server cannot tell intent.
- **Defense pattern:** Synchronizer token or session-bound double-submit HMAC; SameSite as defense in depth; no state change on safe methods; Origin checks.
- **GCP lens:** Lens-1: app middleware (4.4 lab). Lens-2: forged Origin test.
- **Lab:** SEC-E3.4
- **Check:** Why is SameSite alone insufficient historically?

#### AU-04 · Cookie jar & theft vectors — stitch: A10/B5.4
- [ ] unlocked
- **Attack:** Over-broad Domain attribute; missing Path; XSS exfil non-HttpOnly; subdomain cookie injection.
- **Why it works:** Cookie scope is a confused-deputy surface across apps on related hosts.
- **Defense pattern:** Host-only cookies; Path=/; no extra Domain; __Host- prefix where applicable; separate sites for untrusted content.
- **GCP lens:** Lens-1: Hosting vs API cookie domains ADR.
- **Lab:** SEC-E2.6
- **Check:** What does the __Host- prefix require?

#### AU-05 · JWT algorithm & key confusion — stitch: A10/B5.5 · CR-10
- [ ] unlocked
- **Attack:** `alg=none`; RS256→HS256 confusion using public key as HMAC secret; `kid`/`jku` pointing to attacker JWKS.
- **Why it works:** Libraries historically trusted header `alg`; agility without allowlist becomes auth bypass.
- **Defense pattern:** Pin allowlist; ignore header alg except to select among allowlisted; keys from config; validate iss/aud/exp/nbf/jti.
- **GCP lens:** Lens-1: Identity Platform / Google ID token verify with audience. Lens-2: unit tests for none/confusion.
- **Lab:** SEC-E3.5
- **Check:** Show the RS256/HS256 confusion in one diagram.

#### AU-06 · OAuth redirect / mix-up / PKCE bypass — stitch: A10/B5.6
- [ ] unlocked
- **Attack:** Open redirect on `redirect_uri`; authorization server mix-up; skipping PKCE on public clients; `state` not bound.
- **Why it works:** Code interception and client confusion let attackers attach codes to their session.
- **Defense pattern:** Exact redirect allowlist; PKCE S256; high-entropy state bound to session; issuer mix-up defenses; no implicit grant.
- **GCP lens:** Lens-1: Identity Platform OIDC. Lens-2: negative tests wrong redirect.
- **Lab:** SEC-E3.6
- **Check:** What does PKCE protect in a public client?

#### AU-07 · SAML / XML signature wrapping (lite) — stitch: A10/B5.6 literacy
- [ ] unlocked
- **Attack:** Move signed assertion while leaving signature over different nodes; XML canonicalization tricks.
- **Why it works:** XML signature references can be satisfied while application reads a different unsigned element.
- **Defense pattern:** Prefer OIDC when possible; if SAML, use maintained library, strict schema, verify before interpret, disable XXE.
- **GCP lens:** Lens-1: Workforce Federation SAML literacy (verify). Lens-2: paper wrapping diagram.
- **Lab:** SEC-E3.7
- **Check:** In one sentence, what is signature wrapping?

#### AU-08 · Credential stuffing & password spraying — stitch: A10/B5.3 · 4.10
- [ ] unlocked
- **Attack:** Automated replay of breached username/password pairs; spraying few passwords across many accounts to avoid lockouts.
- **Why it works:** Password reuse + predictable spray below threshold.
- **Defense pattern:** Breach blocklists; rate limits + device/bot signals; MFA; generic errors; credential stuffing detection; never lockout-only.
- **GCP lens:** Lens-1: reCAPTCHA Enterprise on login; Armor rate; Identity Platform MFA. Lens-2: limiter tests.
- **Lab:** SEC-E3.3
- **Check:** Contrast stuffing vs spraying.

#### AU-09 · MFA fatigue & SIM swap — stitch: A10/B5.3
- [ ] unlocked
- **Attack:** Push-bomb until victim accepts; SIM swap steals SMS OTP.
- **Why it works:** Human compliance under spam; SMS is not phishing-resistant.
- **Defense pattern:** Number matching / phishing-resistant WebAuthn; rate-limit pushes; prefer TOTP/passkeys over SMS; notify on MFA changes.
- **GCP lens:** Lens-1: Identity Platform MFA factors (verify). Lens-2: policy ADR: SMS deprecated for high risk.
- **Lab:** SEC-E3.10
- **Check:** Why is SMS OTP weaker than WebAuthn?

#### AU-10 · Recovery & account-takeover paths — stitch: A10/B5.3
- [ ] unlocked
- **Attack:** Weaker recovery than login; knowledge questions; long-lived reset tokens in logs.
- **Why it works:** Attackers choose the weakest equivalent path.
- **Defense pattern:** Recovery ≥ login strength; hashed single-use tokens; notify out-of-band; step-up for sensitive.
- **GCP lens:** Lens-1: Identity Platform reset flows. Lens-2: abuse-case tests.
- **Lab:** SEC-E3.11
- **Check:** State the 'recovery not weaker' rule.

#### AU-11 · IDOR / BOLA — stitch: A10/B5.7 · OWASP
- [ ] unlocked
- **Attack:** Change `/orders/123` to `/orders/124`; batch export without object checks.
- **Why it works:** AuthN ≠ AuthZ; guessable ids without `(subject, action, resource, tenant)` checks.
- **Defense pattern:** Server-side authorize every object; opaque ids defense in depth; tenant in every query; negative matrix.
- **GCP lens:** Lens-1: app PEP; IAP is not object AuthZ. Lens-2: IDOR fail-then-pass (4.7).
- **Lab:** SEC-E3.8
- **Check:** Why does a valid JWT not stop BOLA?

#### AU-12 · BFLA & function-level AuthZ — stitch: A10/B5.7
- [ ] unlocked
- **Attack:** Hide admin route in UI only; forged verb to privileged RPC.
- **Why it works:** Missing function checks; client-side gating.
- **Defense pattern:** Explicit permission constants; deny by default; test every admin RPC.
- **GCP lens:** Lens-1: IAM for GCP APIs + app permissions separate.
- **Lab:** SEC-E3.12
- **Check:** Give a BFLA example on the reference cloud app admin.

#### AU-13 · Mass assignment / overposting — stitch: A10/B5.7
- [ ] unlocked
- **Attack:** Client sets `role=admin` or `price=0` in JSON because binder maps all fields.
- **Why it works:** Framework convenience binds untrusted fields into models.
- **Defense pattern:** Allowlist DTO fields; never bind roles/prices from client; server-side pricing.
- **GCP lens:** Lens-1: API schema validation. Lens-2: overpost test.
- **Lab:** SEC-E3.13
- **Check:** Name two fields that must never be client-bound.

#### AU-14 · Confused deputy — stitch: A10/B5.8 · B5 IAM
- [ ] unlocked
- **Attack:** Service with broad SA is tricked into acting on attacker-chosen resource; OAuth client confused.
- **Why it works:** Deputy has authority victim lacks; confused about who asked.
- **Defense pattern:** Least privilege per service; audience-restricted tokens; capability tokens; user context propagation carefully.
- **GCP lens:** Lens-1: SA per service; ID token aud = receiver URL. Lens-2: toy confused-deputy test.
- **Lab:** SEC-E5.1
- **Check:** Define confused deputy in GCP SA terms.

### 3.5 API & abuse (AB-01 … AB-08)

#### AB-01 · Rate-limit algorithms: token bucket, sliding window, leaky bucket — stitch: A10/B5.2 · 4.10
- [ ] unlocked
- **Attack:** Unbounded bursts; global lockout; per-IP only so NAT users collide; no Retry-After.
- **Why it works:** Different algorithms trade burstiness, memory, and fairness.
- **Defense pattern:** Token bucket for bursts; sliding window for smoother; key by tenant+user+IP layers; return 429+Retry-After; fail mode explicit.
- **GCP lens:** Lens-1: app limiter + Armor rate + API Gateway quotas — placement ADR. Lens-2: table tests burst/throttle.
- **Lab:** SEC-E4.3
- **Check:** When does per-IP limiting fail fairness?

#### AB-02 · Where to place limits (edge vs gateway vs app) — stitch: A10/B5.10 · 6.13
- [ ] unlocked
- **Attack:** Only edge limits → per-tenant logic missing; only app → volumetric still bills LB.
- **Why it works:** Volumetric at edge; identity-aware at app; quotas at gateway.
- **Defense pattern:** Defense in depth: Armor for L7 flood; Gateway quota; app token bucket per tenant.
- **GCP lens:** Lens-1: Cloud Armor + API Gateway + middleware. Lens-2: ADR table.
- **Lab:** SEC-E4.4
- **Check:** Draw three layers and one abuse each stops.

#### AB-03 · Bot management & scraping — stitch: A10/B5.10
- [ ] unlocked
- **Attack:** Inventory hoarding bots; credential stuffing bots; fake signups.
- **Why it works:** Bots mimic clients; pure rate limits punish humans on shared IP.
- **Defense pattern:** reCAPTCHA Enterprise scores; device signals; poison pills carefully; AuthZ still required.
- **GCP lens:** Lens-1: reCAPTCHA Enterprise Always Free tier literacy (verify 10k/mo). Lens-2: verify assessment server-side.
- **Lab:** SEC-E4.9
- **Check:** Why is captcha not AuthZ?

#### AB-04 · GraphQL complexity & batching abuse — stitch: A10/B5.10 · 3.x
- [ ] unlocked
- **Attack:** Deep nested queries; batch alias floods; introspection in prod.
- **Why it works:** Single endpoint multiplexes expensive resolvers.
- **Defense pattern:** Depth/cost analysis; timeouts; persisted queries; disable introspection in prod; authz per field.
- **GCP lens:** Lens-1: Cloud Run timeouts + app GraphQL limits. Lens-2: cost-limit unit test.
- **Lab:** SEC-E4.10
- **Check:** Name two GraphQL-specific DoS knobs.

#### AB-05 · Pagination & enumeration abuse — stitch: A10/B5.7 · 8.1
- [ ] unlocked
- **Attack:** Walk pages to scrape; probe ids; huge page sizes.
- **Why it works:** List endpoints leak existence and enable inventory theft.
- **Defense pattern:** Keyset pagination caps; authz on lists; rate limits; consistent errors for missing vs forbidden *carefully* (UX vs security trade).
- **GCP lens:** Lens-1: recall 8.1 cursor pager — add abuse tests.
- **Lab:** SEC-E4.11
- **Check:** How does keyset pagination help abuse resistance?

#### AB-06 · Business-logic abuse — stitch: 5.x · 3.0
- [ ] unlocked
- **Attack:** Coupon stacking; negative quantity; race on wallet debit; loyalty farming.
- **Why it works:** AuthZ can pass while business invariants fail.
- **Defense pattern:** Invariant tests; idempotency keys; server-side price; transactional constraints.
- **GCP lens:** Lens-1: the reference cloud app ledger invariants (5.3). Lens-2: race test.
- **Lab:** SEC-E4.12
- **Check:** Give one business-logic abuse Armor cannot see.

#### AB-07 · Inventory hoarding & checkout abuse — stitch: 5 · AB-03
- [ ] unlocked
- **Attack:** Reserve-all-stock bots; hold timers abused.
- **Why it works:** Scarce goods + open reservation APIs.
- **Defense pattern:** Per-account reservation caps; bot signals; fair queue; short holds.
- **GCP lens:** Lens-1: reCAPTCHA on checkout start + app caps.
- **Lab:** SEC-E4.13
- **Check:** What app-level cap stops hoarding?

#### AB-08 · Export & expensive fan-out abuse — stitch: 9b · 4.10
- [ ] unlocked
- **Attack:** Trigger huge BQ exports or fan-out emails via API.
- **Why it works:** Asymmetric cost: cheap request, expensive backend.
- **Defense pattern:** Async jobs with quotas; confirm step-up; cost governors; alert on fan-out.
- **GCP lens:** Lens-1: BigQuery bytes controls; Tasks rate.
- **Lab:** SEC-E4.14
- **Check:** Define economic asymmetry in one sentence.

### 3.6 Denial of service (DOS-01 … DOS-08)

#### DOS-01 · L3/L4 volumetric taxonomy — stitch: A5/Phase4-Net.16 · A5 TLS / Phase 4 Armor
- [ ] unlocked
- **Attack:** UDP/SYN floods, reflection/amplification filling pipes.
- **Why it works:** Bandwidth and state tables exhaust before L7 logic runs.
- **Defense pattern:** Rely on GFE/Maglev absorption in front of Cloud LB; do not build DIY scrubbing on free tier; architecture: anycast edge.
- **GCP lens:** Lens-1: Cloud Load Balancing + Armor. Lens-2: paper only — **no live DDoS**.
- **Lab:** SEC-E4.1
- **Check:** What does GFE absorb vs what Armor adds?

#### DOS-02 · Amplification & reflection — stitch: A5/Phase4-Net.16
- [ ] unlocked
- **Attack:** DNS/NTP/memcached-style amplification using spoofed source.
- **Why it works:** Small query → large response to victim; cloud misconfig can make you an amplifier.
- **Defense pattern:** No open resolvers; filter spoofing where you control nets; monitor egress.
- **GCP lens:** Lens-1: Cloud DNS security posture. Lens-2: conceptual card.
- **Lab:** SEC-E4.15
- **Check:** Why does source spoofing enable reflection?

#### DOS-03 · L7 application floods — stitch: A10/B5.10 · 6.16
- [ ] unlocked
- **Attack:** HTTP floods on expensive endpoints (search, login, checkout).
- **Why it works:** Requests look legitimate; CPU/DB saturates.
- **Defense pattern:** Armor rate/WAF; cache; app quotas; challenge bots; scale+shed load.
- **GCP lens:** Lens-1: Cloud Armor rate-based rules (verify). Lens-2: local flood against fixture only.
- **Lab:** SEC-E4.7
- **Check:** Name an expensive the reference cloud app endpoint to protect first.

#### DOS-04 · Adaptive Protection literacy — stitch: A5/Phase4-Net.16 · Armor docs
- [ ] unlocked
- **Attack:** Assuming Adaptive Protection is on by default everywhere; ignoring learning period.
- **Why it works:** ML-assisted L7 anomaly detection complements static rules (verify current SKU).
- **Defense pattern:** Know when to enable; still need baseline rate rules; (verify) billing.
- **GCP lens:** Lens-1: Cloud Armor Adaptive Protection (verify). Lens-2: read docs; no attack.
- **Lab:** SEC-E4.16
- **Check:** What problem does Adaptive Protection target that static rate limits miss?

#### DOS-05 · Slowloris / slow-POST / slow-read — stitch: A10/B5.2 · 6.13
- [ ] unlocked
- **Attack:** Hold many connections half-open/slow body to exhaust workers.
- **Why it works:** Timeouts too generous; unlimited concurrent conns per IP.
- **Defense pattern:** Server read/write/header/idle timeouts; conn limits; LB/backend timeouts aligned.
- **GCP lens:** Lens-1: Cloud Run request timeout + `http.Server` timeouts (4.2). Lens-2: slowloris against *local* fixture only.
- **Lab:** SEC-E4.8
- **Check:** Which timeout stops slow-header attacks?

#### DOS-06 · Resource exhaustion (CPU/mem/conn/disk) — stitch: 8 · 4.2
- [ ] unlocked
- **Attack:** Zip bombs; huge JSON; unbounded uploads; regex DoS.
- **Why it works:** App parses untrusted input into memory.
- **Defense pattern:** Body size limits; streaming; timeouts; cgroup/Cloud Run memory caps; reject weird content-types.
- **GCP lens:** Lens-1: Cloud Run memory/CPU; Armor body size if offered (verify).
- **Lab:** SEC-E4.17
- **Check:** Give two app-level exhaustion controls.

#### DOS-07 · Economic DoS (cloud bill) — stitch: 10.3 · FinOps
- [ ] unlocked
- **Attack:** Force expensive egress, logging, LB hours, LLM tokens, image pulls.
- **Why it works:** Pay-per-use means attacker spends *your* money.
- **Defense pattern:** Budgets+alerts; quotas; auth on expensive ops; cache; rate limits; kill switches.
- **GCP lens:** Lens-1: budgets, quotas, Armor, API Gateway. Lens-2: FinOps alert drill.
- **Lab:** SEC-E7.6
- **Check:** Name three billable SKUs an attacker can inflate.

#### DOS-08 · Cache stampedes & thundering herds — stitch: 8 · 9.1
- [ ] unlocked
- **Attack:** TTL expiry stampede hits origin; retry storms amplify outage.
- **Why it works:** Synchronized clients; no jitter; no request coalescing.
- **Defense pattern:** Jittered TTL; singleflight/coalesce; soft TTL; circuit breakers; retry budgets.
- **GCP lens:** Lens-1: Memorystore + CDN TTLs (A5 TLS / Phase 4 Armor). Lens-2: paper stampede math.
- **Lab:** SEC-E8.2
- **Check:** What is singleflight doing for security/availability?

### 3.7 Web & application attacks (WA-01 … WA-12)

#### WA-01 · SOP, CORS pitfalls, postMessage — stitch: A10/B5.4 · CS161
- [ ] unlocked
- **Attack:** CORS `*` with credentials; reflecting Origin; trusting postMessage without origin check.
- **Why it works:** SOP isolates origins; CORS is a loosening; misconfig grants hostile sites privilege.
- **Defense pattern:** Exact allowlist; never credentials+`*`; `Vary: Origin`; validate `event.origin` on postMessage.
- **GCP lens:** Lens-1: Cloud Run CORS middleware. Lens-2: hostile Origin tests (4.4).
- **Lab:** SEC-E2.7
- **Check:** Is CORS an authorization mechanism?

#### WA-02 · XSS: stored, reflected, DOM — stitch: Phase4-Sec.4 · OWASP
- [ ] unlocked
- **Attack:** Inject script into stored fields / reflected params / unsafe DOM sinks (`innerHTML`).
- **Why it works:** Browser executes attacker script in victim origin → cookie theft (non-HttpOnly), actions, exfil.
- **Defense pattern:** Context-aware encoding; CSP + Trusted Types; sanitize carefully; HttpOnly cookies; frameworks auto-escape.
- **GCP lens:** Lens-1: security headers on Hosting/LB. Lens-2: local XSS fixture then fix.
- **Lab:** SEC-E2.5
- **Check:** Contrast stored vs DOM XSS.

#### WA-03 · Clickjacking / UI redress — stitch: Phase4-Sec.4
- [ ] unlocked
- **Attack:** Transparent iframe overlays trick clicks on privileged UI.
- **Why it works:** User thinks they click attacker UI; actually click victim app.
- **Defense pattern:** CSP `frame-ancestors`; `X-Frame-Options` legacy; critical actions need re-auth.
- **GCP lens:** Lens-1: Helmet-like headers on FE. Lens-2: frame test.
- **Lab:** SEC-E2.8
- **Check:** Which CSP directive stops framing?

#### WA-04 · CSP & Trusted Types — stitch: A5 TLS / Phase 4 Armor · WA-02
- [ ] unlocked
- **Attack:** CSP so loose it allows `unsafe-inline` everywhere; no report-only rollout.
- **Why it works:** CSP reduces XSS impact when tightened; Trusted Types lock DOM sinks.
- **Defense pattern:** Report-only → enforce; nonces/hashes; Trusted Types for modern browsers; never as sole control.
- **GCP lens:** Lens-1: FE headers via Hosting/LB custom response headers (verify).
- **Lab:** SEC-E2.9
- **Check:** Why roll out CSP in report-only first?

#### WA-05 · Injection: SQLi, command, path traversal — stitch: A10/B5.9 · 7.4 · Part 2
- [ ] unlocked
- **Attack:** String-built SQL; `os.system` with user input; `../` escapes upload dir.
- **Why it works:** Interpreter metacharacters change meaning.
- **Defense pattern:** Parameterized SQL; allowlists; no shell; path containment + chroot-like roots; least OS privilege.
- **GCP lens:** Lens-1: Cloud SQL + parameterized drivers. Lens-2: weak fixture exploit-then-fix *localhost*.
- **Lab:** SEC-E2.10
- **Check:** Why isn't blacklisting quotes enough for SQLi?

#### WA-06 · XXE & SSTI — stitch: Phase4-Sec.4
- [ ] unlocked
- **Attack:** XML parsers resolve external entities → file/SSRF; template engines execute user strings.
- **Why it works:** Confused parsers/engines treat data as code.
- **Defense pattern:** Disable external entities; never `render(user)`; sandbox templates; prefer non-XML.
- **GCP lens:** Lens-1: app-level. Lens-2: paper XXE→SSRF→metadata chain.
- **Lab:** SEC-E3.14
- **Check:** How does SSTI differ from XSS?

#### WA-07 · Unsafe deserialization — stitch: Phase4-Sec.4 · CK
- [ ] unlocked
- **Attack:** Java/`pickle`/PHP unserialize of untrusted blobs → RCE.
- **Why it works:** Object graphs run code on restore.
- **Defense pattern:** Avoid native deserialize of untrusted data; use JSON with schema; sign blobs; allowlist types.
- **GCP lens:** Lens-1: ban pickle in Cloud Run services. Lens-2: conceptual RCE path card.
- **Lab:** SEC-E3.15
- **Check:** Name one safe alternative to pickle for untrusted input.

#### WA-08 · Open redirect & header injection — stitch: A10/B5.6 · 4.2
- [ ] unlocked
- **Attack:** `?next=https://evil`; CRLF in headers → response split.
- **Why it works:** User trust + header parsing flaws.
- **Defense pattern:** Allowlist redirects; encode; reject CR/LF; use URL parsers carefully.
- **GCP lens:** Lens-1: IAP/app redirect config. Lens-2: open-redirect tests.
- **Lab:** SEC-E3.16
- **Check:** Why do open redirects amplify OAuth attacks?

#### WA-09 · Log injection & forensic pollution — stitch: 10 · IR-01
- [ ] unlocked
- **Attack:** Crafted input breaks log lines / injects fake events.
- **Why it works:** Downstream SIEM trusts structure.
- **Defense pattern:** Structured JSON logs; encode; never log secrets; integrity of audit trails.
- **GCP lens:** Lens-1: Cloud Logging jsonPayload. Lens-2: inject-then-detect exercise on fixture.
- **Lab:** SEC-E7.1
- **Check:** How does structured logging reduce log injection?

#### WA-10 · Memory/control-flow → cloud RCE (applied) — stitch: CS155 · CK · GCE
- [ ] unlocked
- **Attack:** Buffer overflow in native VM agent/sidecar; RCE then steal metadata tokens.
- **Why it works:** Native code in VMs/containers still memory-unsafe; cloud makes post-exploit valuable (IMDS).
- **Defense pattern:** Memory-safe languages where possible; ASLR/DEP/CFI intuition; minimal native surface; sandbox; patch.
- **GCP lens:** Lens-1: Container-Optimized OS / Shielded VM literacy; prefer managed runtimes. Lens-2: paper exploit chain to metadata.
- **Lab:** SEC-E6.6
- **Check:** Why does a VM buffer overflow become a cloud credential incident?

#### WA-11 · WAF rule craft & bypass attempts — stitch: A5 TLS / Phase 4 Armor · 6.16 · Armor
- [ ] unlocked
- **Attack:** Attacker encodes payloads to slip signatures; rule order mistakes.
- **Why it works:** WAFs are pattern filters — incomplete mediation if app still vulnerable.
- **Defense pattern:** Armor OWASP rules + custom; *still* fix app; preview/analyze mode; log false positives.
- **GCP lens:** Lens-1: Cloud Armor WAF rules (verify). Lens-2: bypass *conceptual* card — no attacking Google.
- **Lab:** SEC-E4.18
- **Check:** Why is WAF defense-in-depth not a substitute for parameterized SQL?

#### WA-12 · File upload & zip bombs — stitch: A10/B5.9 · DOS-06
- [ ] unlocked
- **Attack:** Upload webshell; zip bomb expands to disk DoS; SVG XSS.
- **Why it works:** Content-type lies; archives amplify.
- **Defense pattern:** Allowlist types; size limits; scan; store outside web root; re-encode images; no exec from bucket.
- **GCP lens:** Lens-1: GCS + virus scan patterns; Cloud Run never serves exec from uploads.
- **Lab:** SEC-E4.19
- **Check:** List four upload controls.

### 3.8 Cloud-specific attacks (CL-01 … CL-08)

#### CL-01 · SSRF → metadata / IMDS (ATT&CK T1552.005) — stitch: A10/B5.2 · 7.4
- [ ] unlocked
- **Attack:** Fetch user URL → `http://169.254.169.254/`; steal SA tokens; DNS rebinding / redirect escape.
- **Why it works:** Server is a deputy with network path to metadata; SSRF turns that into credential access.
- **Defense pattern:** Allowlist schemes/hosts; block link-local/metadata; no redirects to private; prefer Cloud Run tighter metadata; IMDSv2-like headers where applicable (verify GCP metadata headers).
- **GCP lens:** Lens-1: GCE metadata server; Cloud Run identity. Lens-2: local SSRF fixture + guard tests (4.2).
- **Lab:** SEC-E3.2
- **Check:** State T1552.005 and one GCP defense.

#### CL-02 · Public buckets & object ACL mistakes — stitch: Phase4-Sec.3 · 7.7
- [ ] unlocked
- **Attack:** `allUsers` reader; legacy ACLs; signed URL overshare; public listing.
- **Why it works:** Misconfig is customer responsibility; data exfil without exploit code.
- **Defense pattern:** Uniform bucket-level access; org policy public prevention; VPC-SC; short-lived signed URLs; audit.
- **GCP lens:** Lens-1: org policy `storage.publicAccessPrevention` (verify). Lens-2: paper IR for public ACE (7.8).
- **Lab:** SEC-E5.7
- **Check:** Name two controls that prevent accidental public GCS.

#### CL-03 · IAM privilege escalation paths — stitch: B5 IAM · 7.2
- [ ] unlocked
- **Attack:** `iam.serviceAccountUser` + deploy rights → act as SA; overly broad `roles/owner`; condition bypasses.
- **Why it works:** Permissions compose into paths not obvious from one binding.
- **Defense pattern:** Least privilege; analyze effective policy; deny policies; break-glass JIT; Policy Analyzer literacy.
- **GCP lens:** Lens-1: Policy Analyzer / IAM recommender (verify). Lens-2: toy effective-access from 7.2.
- **Lab:** SEC-E5.1
- **Check:** Give one classic SA escalation pairing.

#### CL-04 · Service account key theft & sprawl — stitch: A10/B5.8 · 7.8
- [ ] unlocked
- **Attack:** JSON keys in GitHub; keys in images; long-lived keys.
- **Why it works:** Keys are bearer credentials; sprawl multiplies leak paths.
- **Defense pattern:** Disable key creation org policy; WIF; attached SAs; inventory+rotate; IR for leaked key.
- **GCP lens:** Lens-1: `iam.disableServiceAccountKeyCreation`. Lens-2: WIF lab recall + negative test.
- **Lab:** SEC-E5.3
- **Check:** Why prefer WIF over JSON keys for GitHub Actions?

#### CL-05 · Confused deputy in cloud APIs — stitch: AU-14 · 4.8
- [ ] unlocked
- **Attack:** Automation SA with `storage.admin` copies attacker-chosen bucket to exfil project.
- **Why it works:** Broad deputies + insufficient audience/resource binding.
- **Defense pattern:** Per-resource roles; request signing with audience; VPC-SC; user project checks.
- **GCP lens:** Lens-1: VPC-SC + least SA roles.
- **Lab:** SEC-E5.8
- **Check:** How does VPC-SC reduce confused-deputy exfil?

#### CL-06 · Tenant isolation failures — stitch: A10/B5.7 · 8.1
- [ ] unlocked
- **Attack:** Missing `tenant_id` in query/cache key; cross-tenant log bleed.
- **Why it works:** Multi-tenant bugs are high-severity data breaches.
- **Defense pattern:** Tenant in every query/cache/job/export; RLS; tests for cross-tenant; separate projects for strong isolation.
- **GCP lens:** Lens-1: Identity Platform multi-tenancy literacy; Cloud SQL RLS. Lens-2: SEC-E3.8 cross-tenant.
- **Lab:** SEC-E5.2
- **Check:** Name three places tenant id must appear.

#### CL-07 · VPC peering / Shared VPC trust mistakes — stitch: A5/Phase4-Net.15
- [ ] unlocked
- **Attack:** Peer into untrusted project; flat allow; assume peering is private *and* trusted.
- **Why it works:** Peering extends network reach without identity.
- **Defense pattern:** Segment; FW defaults deny; prefer PSC; treat peered projects as semi-trusted.
- **GCP lens:** Lens-1: Shared VPC host/service project model. Lens-2: diagram trust.
- **Lab:** SEC-E5.6
- **Check:** Contrast peering trust with VPC-SC.

#### CL-08 · Serverless event injection & hypervisor escape awareness — stitch: 3.4 · XACS235
- [ ] unlocked
- **Attack:** Poison Pub/Sub message / Cloud Storage event triggers privileged function; customer residual risk if CSP escape (rare).
- **Why it works:** Event producers may be untrusted; CSP owns hypervisor — customer still owns config/IAM.
- **Defense pattern:** AuthN events; validate payloads; least privilege functions; shared-responsibility clarity for escapes.
- **GCP lens:** Lens-1: Eventarc/Pub/Sub IAM; Cloud Run invoker. Lens-2: poison-event unit test.
- **Lab:** SEC-E5.9
- **Check:** Who owns hypervisor escape mitigation vs who owns event AuthZ?

### 3.9 Network & zero-trust attacks (NT-01 … NT-08)

#### NT-01 · Perimeter myths ('inside VPC = safe') — stitch: A5/Phase4-Net.14 · 7.1
- [ ] unlocked
- **Attack:** Flat allow-all internal; no identity on east-west.
- **Why it works:** Breach + lateral movement; VPN-only is not zero trust.
- **Defense pattern:** Authenticate every request; micro-segment; IAP; mTLS/s2s IAM.
- **GCP lens:** Lens-1: IAP + service IAM. Lens-2: HLD redraw.
- **Lab:** SEC-E5.5
- **Check:** Why is VPN alone not zero trust?

#### NT-02 · Lateral movement — stitch: A5/Phase4-Net.12 · 7.6
- [ ] unlocked
- **Attack:** Pivot from compromised Run job to reachable SQL/admin via open FW.
- **Why it works:** Over-broad east-west reachability.
- **Defense pattern:** Deny-by-default FW; SA-targeted rules; private SQL; break-glass only.
- **GCP lens:** Lens-1: VPC FW / NGFW. Lens-2: path diagram.
- **Lab:** SEC-E5.4
- **Check:** Name two lateral-movement blockers on GCP.

#### NT-03 · Egress exfil & DNS tunneling — stitch: A5/Phase4-Net.15 · 6.16
- [ ] unlocked
- **Attack:** DNS queries encode stolen data; HTTPS to attacker; abuse Cloud NAT egress.
- **Why it works:** DNS often allowed; hard to inspect.
- **Defense pattern:** Egress allowlists; DNS logging/monitoring; VPC-SC; DLP on egress paths; alert unusual DNS volume.
- **GCP lens:** Lens-1: Cloud DNS logging; VPC-SC; Cloud NAT logs. Lens-2: conceptual tunneling card — no real tunnel to third parties.
- **Lab:** SEC-E4.20
- **Check:** Why is DNS a popular exfil channel?

#### NT-04 · BGP / DNS threats (conceptual) — stitch: A5/Phase4-Net.16 · CS161
- [ ] unlocked
- **Attack:** Route hijack concepts; cache poisoning; dangling CNAME/NS takeover; subdomain takeover on abandoned LB IP.
- **Why it works:** Routing/DNS integrity failures redirect victims at scale.
- **Defense pattern:** DNSSEC for authenticity; delete DNS with services; inventory dangling; RPKI literacy (conceptual).
- **GCP lens:** Lens-1: Cloud DNS DNSSEC; destroy-order checklist 6.16. Lens-2: paper only.
- **Lab:** SEC-E4.21
- **Check:** What does DNSSEC provide that plain DNS lacks?

#### NT-05 · IAP vs VPN threat models — stitch: A5/Phase4-Net.14
- [ ] unlocked
- **Attack:** VPN grants network presence; malware on laptop reaches flat subnet.
- **Why it works:** IAP authorizes *application* access by identity; VPN authorizes *network* presence.
- **Defense pattern:** Prefer IAP for admin UIs/SSH TCP; VPN only for legacy; still need app AuthZ.
- **GCP lens:** Lens-1: IAP lab 6.14. Lens-2: compare threat tables.
- **Lab:** SEC-E5.5
- **Check:** Which attacker capability does IAP remove vs VPN?

#### NT-06 · VPC-SC exfil controls — stitch: A5/Phase4-Net.15
- [ ] unlocked
- **Attack:** Stolen creds copy data to attacker-controlled project/internet path.
- **Why it works:** IAM alone insufficient if credentials valid.
- **Defense pattern:** Perimeters dry-run then enforce; private paths; combine with CMEK.
- **GCP lens:** Lens-1: VPC Service Controls. Lens-2: diagram — live optional.
- **Lab:** SEC-E5.6
- **Check:** What class of exfil does VPC-SC target?

#### NT-07 · Control placement on the packet path — stitch: A5/Phase4-Net.11
- [ ] unlocked
- **Attack:** Buying seventh overlapping product; wrong layer for OWASP vs volumetric.
- **Why it works:** Confusion wastes money and leaves gaps.
- **Defense pattern:** Internet→GFE/Armor→URL map→NEG→Run→(VPC-SC)→data — one primary control per hop.
- **GCP lens:** Lens-1: 6.11 map. Lens-2: redraw the reference cloud app path.
- **Lab:** SEC-E4.5
- **Check:** Place Armor vs NGFW vs IAP vs VPC-SC on one path.

#### NT-08 · TLS interception risks — stitch: CR-12 · corp proxies
- [ ] unlocked
- **Attack:** Corp MITM proxy with custom trust; malware installing roots.
- **Why it works:** Breaking TLS end-to-end for inspection introduces new trust anchors.
- **Defense pattern:** Minimize interception; pin only with ops; protect private keys of intercept CAs; prefer modern SSE alternatives where appropriate.
- **GCP lens:** Lens-1: understand GFE terminates TLS — still Google's trust model. Lens-2: discussion card.
- **Lab:** SEC-E2.11
- **Check:** What new asset appears when you intercept TLS?

### 3.10 Containers & Kubernetes (CK-01 … CK-06)

#### CK-01 · Container escape patterns (awareness) — stitch: A5.2 · D8 · 7.5
- [ ] unlocked
- **Attack:** Privileged container; docker.sock mount; kernel exploit from container.
- **Why it works:** Shared kernel; privileged = near-host.
- **Defense pattern:** Non-root; no privileged; drop caps; read-only FS; no docker.sock; patch runtime; prefer Cloud Run/GKE Autopilot constraints.
- **GCP lens:** Lens-1: GKE security posture; Cloud Run contract. Lens-2: review Pod security context.
- **Lab:** SEC-E6.1
- **Check:** Name three escape-enabling configs.

#### CK-02 · Privileged pods & hostPath — stitch: D8 · 9.2
- [ ] unlocked
- **Attack:** hostPath `/` write; privileged:true for convenience.
- **Why it works:** Direct host FS/devices bypass isolation.
- **Defense pattern:** Pod Security Standards/admission deny; no hostPath except tightly reviewed; Autopilot restrictions.
- **GCP lens:** Lens-1: GKE Policy Controller / Binary Authorization pairing. Lens-2: deny policy sketch.
- **Lab:** SEC-E6.7
- **Check:** Why is hostPath to /var/run/docker.sock catastrophic?

#### CK-03 · K8s RBAC wildcards — stitch: 9.2 · 7.2
- [ ] unlocked
- **Attack:** `verbs: ["*"]` on secrets cluster-wide.
- **Why it works:** Wildcards violate least privilege; credentials in etcd/API.
- **Defense pattern:** Least verbs/resources; separate SA per workload; audit RoleBindings.
- **GCP lens:** Lens-1: GKE RBAC + IAM for cluster control plane. Lens-2: review one Role yaml.
- **Lab:** SEC-E6.8
- **Check:** What is dangerous about `secrets/*` read?

#### CK-04 · Secrets in etcd / env / images — stitch: Phase4-Sec.3 · 4.9
- [ ] unlocked
- **Attack:** Env vars from plaintext Secrets; secrets in image layers; etcd not encrypted at rest (legacy).
- **Why it works:** Readable by many principals; image history leaks.
- **Defense pattern:** Secret Manager; CSI drivers; encrypt etcd; never bake secrets; file mounts with tight RBAC.
- **GCP lens:** Lens-1: Secret Manager + GKE integration (verify). Lens-2: `docker history` scan.
- **Lab:** SEC-E6.2
- **Check:** Why are env vars a weak secret channel?

#### CK-05 · Admission & supply-chain gates — stitch: Phase4-Sec.5 · WL
- [ ] unlocked
- **Attack:** Untagged `:latest` deploys; unsigned images.
- **Why it works:** Runtime IAM cannot save a poisoned image.
- **Defense pattern:** Binary Authorization; digest pins; vulnerability fail-on-CRITICAL; mutate deny.
- **GCP lens:** Lens-1: Binary Authorization + Artifact Registry. Lens-2: recall 7.5 lab analytic layer.
- **Lab:** SEC-E6.4
- **Check:** What does an attestation assert?

#### CK-06 · NetworkPolicy & service mesh mTLS lite — stitch: A5/Phase4-Net.15 · 9.2
- [ ] unlocked
- **Attack:** All pods can talk; flat cluster network.
- **Why it works:** Lateral movement inside cluster.
- **Defense pattern:** Default-deny NetworkPolicy; mesh mTLS literacy; still IAM at GCP APIs.
- **GCP lens:** Lens-1: GKE NetworkPolicy / Dataplane. Lens-2: default-deny sketch.
- **Lab:** SEC-E6.9
- **Check:** Does NetworkPolicy replace IAM for Cloud SQL?

### 3.11 Workload & supply chain (WL-01 … WL-06)

#### WL-01 · Poisoned images & dependency confusion — stitch: Phase4-Sec.5
- [ ] unlocked
- **Attack:** Typosquat package; compromised base image; malicious layer.
- **Why it works:** Build trusts upstream names; pulls mutable tags.
- **Defense pattern:** Pin digests; private proxies; lockfiles; scan; signed builds; review owners.
- **GCP lens:** Lens-1: Artifact Registry remote repos literacy (verify). Lens-2: pin digest in TF.
- **Lab:** SEC-E6.5
- **Check:** What is dependency confusion?

#### WL-02 · CI/CD poisoned pipeline — stitch: A10/B5.8 · D2
- [ ] unlocked
- **Attack:** Malicious PR runs privileged workflow; self-hosted runner compromise; secrets in logs.
- **Why it works:** CI has deploy authority — high-value.
- **Defense pattern:** Least privilege WIF; protected branches; none on fork PRs for secrets; ephemeral runners; audit.
- **GCP lens:** Lens-1: GitHub OIDC + WIF. Lens-2: negative wrong-repo claim test.
- **Lab:** SEC-E6.10
- **Check:** Why are fork PRs dangerous with secrets?

#### WL-03 · SBOM meaning & limits — stitch: Phase4-Sec.5
- [ ] unlocked
- **Attack:** Having an SBOM PDF and calling supply chain 'done'.
- **Why it works:** SBOM is inventory — not verification.
- **Defense pattern:** Generate SBOM; alert on CVE; still need attestations + admission.
- **GCP lens:** Lens-1: Artifact Analysis / AR scanning (verify). Lens-2: read one SBOM sample.
- **Lab:** SEC-E6.11
- **Check:** What decision does an SBOM enable that it does not automate alone?

#### WL-04 · Binary Authorization meaning — stitch: Phase4-Sec.5
- [ ] unlocked
- **Attack:** Thinking BinAuth encrypts images; enabling without attestations.
- **Why it works:** BinAuth is admission policy on provenance.
- **Defense pattern:** Attestors; Cloud Build signs; break-glass documented; dry-run.
- **GCP lens:** Lens-1: Binary Authorization API. Lens-2: 7.5 toy attestation analytic.
- **Lab:** SEC-E6.4
- **Check:** BinAuth vs vulnerability scan — contrast.

#### WL-05 · Secret sprawl in repos/images/logs/prompts — stitch: A10/B5.9 · 9c
- [ ] unlocked
- **Attack:** Keys in git history; in layers; in LLM prompts; in traces.
- **Why it works:** Many sinks; hard to revoke all.
- **Defense pattern:** Inventory; pre-commit secret scan; Secret Manager; never prompt secrets; redaction.
- **GCP lens:** Lens-1: Secret Manager; SDP for prompts. Lens-2: git history secret hunt on *synthetic* repo.
- **Lab:** SEC-E6.2
- **Check:** List five sprawl sinks.

#### WL-06 · Build provenance / SLSA literacy — stitch: Phase4-Sec.5 · CR-10
- [ ] unlocked
- **Attack:** Unsigned artifacts promoted as prod.
- **Why it works:** Without provenance, attestation is theater.
- **Defense pattern:** Hermetic builds; provenance documents; verify before deploy; SLSA as maturity story.
- **GCP lens:** Lens-1: Cloud Build provenance (verify). Lens-2: cosign-shaped toy from 7.5.
- **Lab:** SEC-E6.12
- **Check:** What is a hermetic build?

### 3.12 Detection & incident response (IR-01 … IR-08)

#### IR-01 · Log gaps & trail integrity — stitch: Phase4-Sec.6 · 10.0
- [ ] unlocked
- **Attack:** Data Access logs off; logs writable by attacker SA; no retention; clocks skewed.
- **Why it works:** You cannot investigate what you did not record; attackers delete or pollute trails.
- **Defense pattern:** Enable Admin+Data Access where needed; immutable sinks to separate project; retention; time sync; never log secrets.
- **GCP lens:** Lens-1: Cloud Audit Logs sinks to protected bucket/BQ. Lens-2: prove SetIamPolicy appears.
- **Lab:** SEC-E7.1
- **Check:** Why sink logs to a *separate* project?

#### IR-02 · Alert design failures — stitch: Phase4-Sec.6
- [ ] unlocked
- **Attack:** Alert on everything → fatigue; alert on nothing; no owner; no runbook link.
- **Why it works:** Humans ignore noisy pages; silent failures miss breaches.
- **Defense pattern:** Few high-precision detections (key create, public ACE, SetIamPolicy anomaly); mute with justification; page → runbook.
- **GCP lens:** Lens-1: SCC findings + log-based metrics. Lens-2: wire one alert to 7.6 template.
- **Lab:** SEC-E7.3
- **Check:** Name three high-value low-noise alerts.

#### IR-03 · Containment on ephemeral compute — stitch: Phase4-Sec.8 · Cloud Run
- [ ] unlocked
- **Attack:** Trying to 'SSH and forensics' a scaled-to-zero revision that is gone; redeploying over evidence.
- **Why it works:** Ephemeral instances destroy disk state; containment must be identity/traffic/config based.
- **Defense pattern:** Disable SA; revoke tokens; remove invoker IAM; pin traffic to known-good revision; snapshot *only if GCE*; preserve logs first.
- **GCP lens:** Lens-1: Cloud Run revision traffic; IAM deny. Lens-2: tabletop ephemeral containment.
- **Lab:** SEC-E7.4
- **Check:** List containment steps when the compromised revision no longer exists.

#### IR-04 · Detection engineering for cloud TTPs — stitch: TH-05 · 7.6
- [ ] unlocked
- **Attack:** Only CVE scanning; no credential-access detections.
- **Why it works:** Cloud attacks often are API abuse with valid creds.
- **Defense pattern:** Detect key create, anomalous IAM, public bindings, metadata token use patterns, impossible travel for admins.
- **GCP lens:** Lens-1: SCC + Cloud IDS literacy + SecOps. Lens-2: map 5 ATT&CK techniques to signals.
- **Lab:** SEC-E7.3
- **Check:** Give one detection for T1552.005 aftermath.

#### IR-05 · IR: compromised SA / leaked key — stitch: Phase4-Sec.8 · CR-15 · CL-04
- [ ] unlocked
- **Attack:** Slow rotate; leaving keys enabled; not checking audit for usage window.
- **Why it works:** Bearer keys work until disabled; delay expands blast radius.
- **Defense pattern:** Disable SA/keys → hunt audit → rotate workloads → rewrap secrets → postmortem. Use roadmap 7.8 template; CR-15 for crypto keys.
- **GCP lens:** Lens-1: `serviceAccount.keys` audit; disable SA. Lens-2: timed tabletop.
- **Lab:** SEC-E7.2, SEC-E7.5
- **Check:** Order of operations: disable first or redeploy first? Why?

#### IR-06 · IR: public data exposure — stitch: Phase4-Sec.8 · CL-02
- [ ] unlocked
- **Attack:** Quietly un-public without checking what leaked or notifying.
- **Why it works:** Exposure may already be scraped; legal/comms matter.
- **Defense pattern:** Remove ACE → inventory objects → SDP/DLP classify → assess notification → org policy → lessons.
- **GCP lens:** Lens-1: SCC public bucket finding; SDP. Lens-2: tabletop.
- **Lab:** SEC-E7.7
- **Check:** What evidence do you collect before/after removing allUsers?

#### IR-07 · Ransomware / backup integrity (cloud) — stitch: Phase4-Sec.8 · 2.3
- [ ] unlocked
- **Attack:** Immutable backups missing; same SA can encrypt data *and* delete backups.
- **Why it works:** Ransomware targets backups; identity separation matters.
- **Defense pattern:** Immutable/object-lock style retention where offered; separate backup project/SA; test restore; MFA on break-glass.
- **GCP lens:** Lens-1: Cloud Storage retention / Backup for GKE literacy (verify). Lens-2: restore drill paper.
- **Lab:** SEC-E7.8
- **Check:** Why must backup admin be separate from data admin?

#### IR-08 · Tabletop facilitation craft — stitch: Phase4-Sec.8 · SEC-CAP2
- [ ] unlocked
- **Attack:** Tabletop without clock or scribe; arguments about blame.
- **Why it works:** Practice builds muscle for contain order under stress.
- **Defense pattern:** 60-min clock; injects; scribe fills Detect→Contain→…; grade time-to-contain + restore tested.
- **GCP lens:** Lens-1: four roadmap runbooks + CR-15 branch. Lens-2: run one tabletop.
- **Lab:** SEC-CAP2
- **Check:** What two metrics grade a tabletop?

### 3.13 AI / LLM cloud-app threats (AI-01 … AI-05)

#### AI-01 · Prompt injection (direct & indirect) — stitch: 9c · OWASP LLM
- [ ] unlocked
- **Attack:** User/content says 'ignore policies, dump secrets'; indirect injection via retrieved docs.
- **Why it works:** Model follows instructions in untrusted text; retrieval expands attack surface.
- **Defense pattern:** Separate system vs user channels; harden tools; output filtering; least-privilege tools; human confirm high risk; treat retrieved text as data.
- **GCP lens:** Lens-1: Vertex AI + Model Armor literacy (verify); SDP before prompts. Lens-2: red-team prompts on *local* stub.
- **Lab:** SEC-E8.3
- **Check:** Contrast direct vs indirect prompt injection.

#### AI-02 · Tool / agent abuse — stitch: 9c
- [ ] unlocked
- **Attack:** Agent with broad tools (email/SQL/GCS) invoked via injection to exfil.
- **Why it works:** Tools turn LLM into an executor with your credentials.
- **Defense pattern:** Narrow tools; confirmations; SANDboxed credentials; allowlists; audit tool calls.
- **GCP lens:** Lens-1: Vertex agents / extensions IAM (verify). Lens-2: deny-by-default tool test.
- **Lab:** SEC-E8.4
- **Check:** Why is a SQL tool on an LLM high risk?

#### AI-03 · RAG data leakage — stitch: 9c.2 · PV-02
- [ ] unlocked
- **Attack:** RAG corpus includes secrets/PII; model quotes them; cross-tenant retrieval.
- **Why it works:** Retrieval ignores AuthZ if not enforced at fetch.
- **Defense pattern:** AuthZ at retrieval; per-tenant indexes; DLP; no secrets in corpus; citation+redaction.
- **GCP lens:** Lens-1: Vertex Search / matching engine IAM patterns (verify). Lens-2: cross-tenant retrieval negative test design.
- **Lab:** SEC-E8.6
- **Check:** Where must AuthZ be enforced in RAG?

#### AI-04 · Model / data poisoning & supply chain — stitch: 9c · WL
- [ ] unlocked
- **Attack:** Poison training/fine-tune data; malicious model artifact from untrusted hub.
- **Why it works:** Integrity of data/models is supply chain.
- **Defense pattern:** Curate data; sign models; private registries; eval for backdoors; pin digests.
- **GCP lens:** Lens-1: Artifact Registry for models; Vertex model garden caution (verify).
- **Lab:** SEC-E8.7
- **Check:** Name one control for model artifact integrity.

#### AI-05 · Shadow AI & sensitive paste — stitch: 9c · PV
- [ ] unlocked
- **Attack:** Engineers paste production data into public LLM UIs.
- **Why it works:** Bypasses DLP and contracts.
- **Defense pattern:** Policy; approved Vertex endpoints; DLP; training; block public LLM at egress if required.
- **GCP lens:** Lens-1: Chrome Enterprise / egress controls literacy; SDP. Lens-2: policy ADR.
- **Lab:** SEC-E8.8
- **Check:** What is shadow AI in one sentence?

### 3.14 Side channels & isolation (SC-01 … SC-03)

#### SC-01 · Timing & cache side channels (applied) — stitch: CR-16 · MIT 6.858
- [ ] unlocked
- **Attack:** Remote timing on compare; speculative-execution class risks on shared hardware (high effort).
- **Why it works:** Shared microarchitecture leaks under sophisticated attackers.
- **Defense pattern:** Constant-time crypto APIs; prefer KMS; threat-model co-tenancy for HSM-class secrets.
- **GCP lens:** Lens-1: Cloud HSM / KMS. Lens-2: compare timing unit test education.
- **Lab:** CR-E17
- **Check:** When do you escalate from 'software constant-time' to HSM/TEE?

#### SC-02 · Noisy neighbor & isolation classes — stitch: CMU 95-746 · 8
- [ ] unlocked
- **Attack:** DoS via co-tenant resource contention; assuming strong isolation on shared CPU without evidence.
- **Why it works:** Cloud isolation is layered (VM/container/serverless) with different residual risks.
- **Defense pattern:** Pick isolation class matching data sensitivity; quotas; Confidential VM when needed.
- **GCP lens:** Lens-1: sole-tenant / Confidential VM literacy (verify). Lens-2: isolation ADR.
- **Lab:** SEC-E8.9
- **Check:** Compare container vs VM isolation for a key-managing service.

#### SC-03 · Confidential Computing threat model — stitch: CR-18 · 7.3
- [ ] unlocked
- **Attack:** Marketing TEE as fixing IAM misconfig or SQLi.
- **Why it works:** TEEs reduce host/operator memory visibility with attestation; app bugs remain.
- **Defense pattern:** Use when threat is privileged infrastructure observer; still patch apps; attest correctly.
- **GCP lens:** Lens-1: Confidential VM / GKE / Space (verify). Lens-2: buys/costs memo.
- **Lab:** CR-E19
- **Check:** List two in-scope and two out-of-scope threats for Confidential VM.

### 3.15 Privacy & data (PV-01 … PV-05)

#### PV-01 · Data classification & handling — stitch: Phase4-Sec.3 · 7.9
- [ ] unlocked
- **Attack:** Treat all data equal; PII in debug logs.
- **Why it works:** Controls follow class; without class, over/under-protect.
- **Defense pattern:** Public/Internal/Confidential/Restricted labels; handling rules; default deny for Restricted.
- **GCP lens:** Lens-1: SDP infoTypes; resource labels. Lens-2: classify the reference cloud app fields.
- **Lab:** SEC-E6.3
- **Check:** Give handling rule differences Confidential vs Restricted.

#### PV-02 · DLP / tokenization before analytics & prompts — stitch: Phase4-Sec.3 · 9c
- [ ] unlocked
- **Attack:** Raw PII to shared BQ or LLM context.
- **Why it works:** Analytics/AI expand readership beyond original purpose.
- **Defense pattern:** SDP inspect/de-identify; tokenize; purpose limitation.
- **GCP lens:** Lens-1: Sensitive Data Protection. Lens-2: synthetic payload inspect.
- **Lab:** SEC-E8.6
- **Check:** Why de-identify before prompt assembly?

#### PV-03 · Tokenization vs encryption — stitch: CR-17 · 5
- [ ] unlocked
- **Attack:** Encrypting PANs but still needing format for PSP — wrong tool.
- **Why it works:** Tokenization replaces value with surrogate; encryption is reversible with key.
- **Defense pattern:** PAN: tokenize (Part 5); secrets: Secret Manager; fields: AEAD when needed.
- **GCP lens:** Lens-1: PCI themes Part 5 + SDP. Lens-2: decision table.
- **Lab:** SEC-E6.13
- **Check:** When is tokenization preferred over field encryption?

#### PV-04 · Residency & sovereignty controls — stitch: Phase4-Sec.9 · 6.15
- [ ] unlocked
- **Attack:** Global BQ 'for simplicity' with EU personal data.
- **Why it works:** Law may constrain location/transfers.
- **Defense pattern:** `resourceLocations`; regional resources; Assured Workloads literacy; no legal advice — map to products.
- **GCP lens:** Lens-1: org policy resourceLocations. Lens-2: plan-only TF.
- **Lab:** SEC-E8.1
- **Check:** Name two GCP levers for residency.

#### PV-05 · Privacy vs security tension (short Embedded EthiCS angle) — stitch: XACS235 · 7.9
- [ ] unlocked
- **Attack:** Maximizing retention 'for security' vs minimization; employee monitoring vs dignity.
- **Why it works:** Security logging can become privacy harm; tradeoffs need explicit ethics/policy.
- **Defense pattern:** Minimize; purpose-bind; access-review security logs; document tension in ADR.
- **GCP lens:** Lens-1: audit log access controls. Lens-2: one-page ethics memo on login telemetry retention.
- **Lab:** SEC-E8.10
- **Check:** Give one example where more security logging harms privacy.

### 3.16 Compliance literacy lite (CM-01 … CM-02)

#### CM-01 · CSA CCM v4 as coverage checklist — stitch: Phase4-Sec.9 · XACS235
- [ ] unlocked
- **Attack:** Dumping all CCM controls as homework; checkbox without evidence.
- **Why it works:** CCM organizes domains — use to find gaps, not to memorize 100s of controls.
- **Defense pattern:** Map the reference cloud app to subset: IAM, EKM/CEK, LOG, IVS, TVM, AIS, SEF — evidence paths.
- **GCP lens:** Lens-1: Well-Architected + CCM crosswalk lite. Lens-2: gap spreadsheet.
- **Lab:** SEC-E8.1
- **Check:** Name five CCM domains and one the reference cloud app control each.

#### CM-02 · PCI / HIPAA / SOC2 / FedRAMP idea → control map — stitch: Phase4-Sec.9 · 5
- [ ] unlocked
- **Attack:** Sticker on README; 'we'll be careful' as PHI plan.
- **Why it works:** Regimes demand evidence+scope+location mapped to real controls.
- **Defense pattern:** Obligation→control→GCP product→artifact; BAA/Assured Workloads literacy; no legal advice.
- **GCP lens:** Lens-1: Compliance Reports Manager for *Google* attestations vs *your* evidence. Lens-2: matrix rows.
- **Lab:** SEC-E8.1
- **Check:** Contrast Google's SOC report vs your SOC evidence.

## 4. Skip tests / readiness tiers

Skip a companion family only by passing its skip-test. gcp.md still owns product labs — skipping companion theory does not skip Armor attach / IAP / CMEK product evidence.

| Tier | Meaning | Skip-test (learner does unaided) | If fail |
|---|---|---|---|
| **SEC-T0** | Security literacy | Explain CIA+assume-breach+shared responsibility in 5 sentences; name web vs network vs cloud-admin attackers | PQ-S + TH-01…03 |
| **SEC-T1** | Applied crypto baseline | State IND-CPA vs integrity; why ECB dies; AEAD nonce rule; EtM; password KDF vs SHA; envelope KEK/DEK | CR-01…07, CR-13–14 |
| **SEC-T2** | TLS/PKI | TLS 1.3 vs 1.2 headline; 0-RTT risk; cert chain validate; HSTS purpose | CR-11, CR-12 |
| **SEC-T3** | Auth attacks | Distinguish hijack vs fixation; CSRF recipe; JWT confusion; OAuth PKCE purpose; stuffing vs spray | AU-01…09 |
| **SEC-T4** | AuthZ / cloud IDOR | BOLA example + fix; confused deputy; tenant isolation checklist | AU-11…14, CL-06 |
| **SEC-T5** | Abuse / DoS | Token bucket vs sliding window; place edge vs app limits; L3 vs L7; slowloris control; economic DoS | AB-01…02, DOS-01…07 |
| **SEC-T6** | Cloud TTPs | T1552.005 path; public bucket controls; SA key vs WIF; VPC-SC purpose | CL-01…04, NT-06 |
| **SEC-T7** | Supply chain / K8s | Privileged pod risk; BinAuth meaning; CI poison path; SBOM limit | CK-*, WL-* |
| **SEC-T8** | Detect / IR | Log sink separation; ephemeral containment order; tabletop metrics | IR-* |
| **SEC-T9** | AI surface | Direct vs indirect injection; tool abuse; RAG AuthZ point | AI-* |

**Prop Lock reminder:** passing SEC-T2 does not unlock VPC-SC props before 6.15.

---

## 5. Exercise bank — scenario cards (predict → design → GCP map)

**Bank ≠ dump.** Issue **one** card per teaching moment. Levels 0–8. Crypto cards use `CR-E*` ids and also appear mixed in levels. Appendix K opens only after attempt. No invented lab DB goldens — qualitative keys only.

### 5.0 Level 0 — paper drills (SEC-Z0)

#### SEC-Z0.1 · L0 · Encoding vs encryption
- **Scenario:** Eight snippets: Base64, AES-GCM, SHA-256, HMAC, homemade XOR, URL-encoding, bcrypt, rot13.
- **Predict impact (write first):** Which provide confidentiality against Kerckhoffs attacker?
- **Design control:** Classify each; mark misuse.
- **Map to GCP:** N/A — hygiene
- **Unlocks / depends:** PQ-S-01

#### SEC-Z0.2 · L0 · Hop trust labels
- **Scenario:** Client → DNS → GFE → Armor → LB → Cloud Run → Cloud SQL.
- **Predict impact (write first):** Which hop authenticates the user? The service? Encrypts in transit?
- **Design control:** Label each hop's trust assumption in one phrase.
- **Map to GCP:** A5 TLS / Phase 4 Armor / 6.11 path
- **Unlocks / depends:** PQ-S-04

#### SEC-Z0.3 · L0 · Saltzer mapping
- **Scenario:** the reference cloud app has IAM deny, parameterized SQL, IAP admin, org policy default deny public buckets.
- **Predict impact (write first):** Which Saltzer principle each embodies?
- **Design control:** Map four controls → principles.
- **Map to GCP:** 7.1 recall + PQ-S-02
- **Unlocks / depends:** PQ-S-02

#### SEC-Z0.4 · L0 · STRIDE warm-up
- **Scenario:** `PlaceOrder` flow sketch provided.
- **Predict impact (write first):** One threat per STRIDE letter.
- **Design control:** Write six one-liners.
- **Map to GCP:** 0.4
- **Unlocks / depends:** TH-03

#### SEC-Z0.5 · L0 · Shared responsibility quiz
- **Scenario:** GCE guest OS CVE; Cloud Run app SQLi; GCS public ACE; Google DC physical.
- **Predict impact (write first):** Who owns each?
- **Design control:** Fill matrix.
- **Map to GCP:** PQ-S-03
- **Unlocks / depends:** PQ-S-03

#### SEC-Z0.6 · L0 · ATT&CK metadata one-liner
- **Scenario:** T1552.005 description blank.
- **Predict impact (write first):** Write the technique in one sentence for GCP.
- **Design control:** Name SSRF→IMDS.
- **Map to GCP:** TH-05
- **Unlocks / depends:** TH-05

### 5.1 Level 1 — modeling

#### SEC-E1.1 · L1 · the reference cloud app STRIDE one-pager
- **Scenario:** Storefront checkout.
- **Predict impact (write first):** Highest residual risk after listing threats?
- **Design control:** STRIDE table + one abuse-case test stub.
- **Map to GCP:** 0.4 HLD
- **Unlocks / depends:** TH-02, TH-03

#### SEC-E1.2 · L1 · Responsibility matrix
- **Scenario:** Cloud Run + Cloud SQL + GCS for the reference cloud app.
- **Predict impact (write first):** Where do teams wrongly assume CSP ownership?
- **Design control:** Complete IaaS/PaaS/serverless matrix rows.
- **Map to GCP:** PQ-S-03
- **Unlocks / depends:** PQ-S-03

#### SEC-E1.3 · L1 · Economics ADR
- **Scenario:** Standing global HTTPS LB+Armor vs Hosting+Run for early the reference cloud app.
- **Predict impact (write first):** Attack cost vs $ cost?
- **Design control:** ADR: I pick X because Y, accept Z.
- **Map to GCP:** A5 TLS / Phase 4 Armor FinOps
- **Unlocks / depends:** PQ-S-05

#### SEC-E1.4 · L1 · Attacker model picker
- **Scenario:** Admin UI currently on VPN-only flat VPC.
- **Predict impact (write first):** Which attacker models remain?
- **Design control:** Propose IAP shift and name defeated model.
- **Map to GCP:** 6.14
- **Unlocks / depends:** TH-01, NT-05

### 5.2 Level 2 — web/session

#### SEC-E2.1 · L2 · TLS termination misconception
- **Scenario:** Intern says 'TLS at LB means body encrypted to SQL'.
- **Predict impact (write first):** What is actually in plaintext where?
- **Design control:** Redraw trust; say where CR-17 field AEAD helps.
- **Map to GCP:** A5 TLS / Phase 4 Armor, CR-12, CR-17
- **Unlocks / depends:** CR-12

#### SEC-E2.2 · L2 · Session hijacking
- **Scenario:** Cookie without Secure on HTTP admin path; XSS on blog subdomain sharing Domain=.example.com.
- **Predict impact (write first):** Blast radius?
- **Design control:** Flags + domain fix + session rotate policy.
- **Map to GCP:** 4.4
- **Unlocks / depends:** AU-01, AU-04

#### SEC-E2.3 · L2 · Session fixation
- **Scenario:** API accepts `X-Session-Id` from client and authenticates into it.
- **Predict impact (write first):** Attack steps?
- **Design control:** Server-mint + rotate on login test plan.
- **Map to GCP:** 4.4
- **Unlocks / depends:** AU-02

#### SEC-E2.4 · L2 · Abuse case → test
- **Scenario:** Threat: negative quantity order.
- **Predict impact (write first):** What does the failing test assert?
- **Design control:** Write table-driven test case.
- **Map to GCP:** 3.0, AB-06
- **Unlocks / depends:** TH-04

#### SEC-E2.5 · L2 · Stored XSS
- **Scenario:** Product review field reflects raw HTML.
- **Predict impact (write first):** Impact on HttpOnly session cookie? On CSRF token in DOM?
- **Design control:** Encoding + CSP plan.
- **Map to GCP:** WA-02, WA-04
- **Unlocks / depends:** WA-02

#### SEC-E2.6 · L2 · Cookie jar subdomain
- **Scenario:** Marketing site on `www` sets cookie Domain=.the reference cloud app.example.
- **Predict impact (write first):** How does XSS on marketing steal API session?
- **Design control:** Host-only + split domains.
- **Map to GCP:** AU-04
- **Unlocks / depends:** AU-04

#### SEC-E2.7 · L2 · CORS credentials+*
- **Scenario:** API returns ACAO `*` with credentials true (broken).
- **Predict impact (write first):** What can evil.com do?
- **Design control:** Exact allowlist design.
- **Map to GCP:** WA-01, 4.4
- **Unlocks / depends:** WA-01

#### SEC-E2.8 · L2 · Clickjacking admin
- **Scenario:** Admin 'Delete shop' button frameable.
- **Predict impact (write first):** Attack storyboard.
- **Design control:** frame-ancestors + reauth.
- **Map to GCP:** WA-03
- **Unlocks / depends:** WA-03

#### SEC-E2.9 · L2 · CSP rollout
- **Scenario:** SPA has inline scripts.
- **Predict impact (write first):** Breakage risk of enforce-now?
- **Design control:** Report-only → nonces plan.
- **Map to GCP:** WA-04
- **Unlocks / depends:** WA-04

#### SEC-E2.10 · L2 · SQLi → data
- **Scenario:** Search `q` concatenated into SQL.
- **Predict impact (write first):** Worst credible impact on multi-tenant DB?
- **Design control:** Parameterize + authz still required.
- **Map to GCP:** WA-05, CL-06
- **Unlocks / depends:** WA-05

#### SEC-E2.11 · L2 · TLS intercept tradeoff
- **Scenario:** Corp wants HTTPS inspection on all egress.
- **Predict impact (write first):** New crown-jewel asset?
- **Design control:** Risk memo.
- **Map to GCP:** NT-08
- **Unlocks / depends:** NT-08

### 5.3 Level 3 — authn/authz attacks

#### SEC-E3.1 · L3 · IAM privesc path
- **Scenario:** CI SA has `actAs` on deploy SA that is `roles/owner` on prod.
- **Predict impact (write first):** Escalation narrative.
- **Design control:** Break path; least privilege bindings.
- **Map to GCP:** CL-03, B5 IAM
- **Unlocks / depends:** CL-03

#### SEC-E3.2 · L3 · SSRF → metadata
- **Scenario:** Webhook URL fetcher; no allowlist.
- **Predict impact (write first):** Predict tokens stolen; blast radius.
- **Design control:** Guard design + tests; IMDSv2-like headers if any (verify).
- **Map to GCP:** CL-01, 4.2
- **Unlocks / depends:** CL-01

#### SEC-E3.3 · L3 · Credential stuffing
- **Scenario:** Login endpoint no bot signal, per-IP limit only.
- **Predict impact (write first):** Why spray still works from botnet?
- **Design control:** reCAPTCHA + per-account + MFA design.
- **Map to GCP:** AU-08, AB-03, 4.10
- **Unlocks / depends:** AU-08

#### SEC-E3.4 · L3 · CSRF state change
- **Scenario:** POST /transfer with SameSite=None Secure cookies, no CSRF token.
- **Predict impact (write first):** Exploit sketch from evil.com.
- **Design control:** Token + SameSite strategy.
- **Map to GCP:** AU-03
- **Unlocks / depends:** AU-03

#### SEC-E3.5 · L3 · JWT alg confusion
- **Scenario:** Library trusts header alg; RS256 public key configured.
- **Predict impact (write first):** How does HS256 confusion forge admin?
- **Design control:** Allowlist + tests; link CR-10.
- **Map to GCP:** AU-05, CR-10
- **Unlocks / depends:** AU-05

#### SEC-E3.6 · L3 · OAuth redirect
- **Scenario:** redirect_uri prefix match `https://app.example.com`.
- **Predict impact (write first):** Attack using `https://app.example.com.evil.com` or path tricks.
- **Design control:** Exact match allowlist + PKCE.
- **Map to GCP:** AU-06
- **Unlocks / depends:** AU-06

#### SEC-E3.7 · L3 · SAML wrapping lite
- **Scenario:** XML IdP assertion processed by hand-rolled code.
- **Predict impact (write first):** Where does wrapping bite?
- **Design control:** Library + verify-before-use; prefer OIDC ADR.
- **Map to GCP:** AU-07
- **Unlocks / depends:** AU-07

#### SEC-E3.8 · L3 · IDOR orders
- **Scenario:** `GET /orders/{id}` checks only authn.
- **Predict impact (write first):** Cross-tenant read steps.
- **Design control:** Authz predicate + test matrix.
- **Map to GCP:** AU-11, 4.7
- **Unlocks / depends:** AU-11

#### SEC-E3.9 · L3 · OWASP map the reference cloud app
- **Scenario:** Pick Top 10:2025 list (verify live).
- **Predict impact (write first):** Map A01–A05 to the reference cloud app controls.
- **Design control:** Table.
- **Map to GCP:** 7.4
- **Unlocks / depends:** WA-*

#### SEC-E3.10 · L3 · MFA fatigue
- **Scenario:** Push MFA without number matching.
- **Predict impact (write first):** Attacker with password outcome?
- **Design control:** Number matching / passkeys plan.
- **Map to GCP:** AU-09
- **Unlocks / depends:** AU-09

#### SEC-E3.11 · L3 · Weak recovery
- **Scenario:** Reset token 6-digit, 24h, logged in clear.
- **Predict impact (write first):** ATO path.
- **Design control:** Redesign per 4.3+AU-10.
- **Map to GCP:** AU-10
- **Unlocks / depends:** AU-10

#### SEC-E3.12 · L3 · BFLA admin RPC
- **Scenario:** UI hides `/admin/refund`; API still open.
- **Predict impact (write first):** Exploit.
- **Design control:** Permission check + test.
- **Map to GCP:** AU-12
- **Unlocks / depends:** AU-12

#### SEC-E3.13 · L3 · Mass assignment
- **Scenario:** PATCH /users binds entire JSON into ORM.
- **Predict impact (write first):** Privilege field?
- **Design control:** DTO allowlist.
- **Map to GCP:** AU-13
- **Unlocks / depends:** AU-13

#### SEC-E3.14 · L3 · XXE → SSRF
- **Scenario:** XML invoice upload with external entity.
- **Predict impact (write first):** Chain to metadata?
- **Design control:** Disable entities + SSRF guard.
- **Map to GCP:** WA-06, CL-01
- **Unlocks / depends:** WA-06

#### SEC-E3.15 · L3 · Pickle RCE
- **Scenario:** Cache deserializes pickle from Redis without auth.
- **Predict impact (write first):** Impact.
- **Design control:** JSON+schema; sign if needed.
- **Map to GCP:** WA-07
- **Unlocks / depends:** WA-07

#### SEC-E3.16 · L3 · Open redirect×OAuth
- **Scenario:** Login `next=` open redirect.
- **Predict impact (write first):** How it upgrades OAuth code theft.
- **Design control:** Allowlist.
- **Map to GCP:** WA-08, AU-06
- **Unlocks / depends:** WA-08

### 5.4 Level 4 — abuse & DoS

#### SEC-E4.1 · L4 · L3 vs L7 story
- **Scenario:** Outage with tiny RPS but huge SYN; another with 2k RPS on /search.
- **Predict impact (write first):** Which control class each?
- **Design control:** GFE vs Armor vs app.
- **Map to GCP:** DOS-01, DOS-03
- **Unlocks / depends:** DOS-01

#### SEC-E4.2 · L4 · Timeouts vs slowloris
- **Scenario:** Go server no ReadHeaderTimeout.
- **Predict impact (write first):** Predict failure mode.
- **Design control:** Set timeout suite from 4.2.
- **Map to GCP:** DOS-05, 4.2
- **Unlocks / depends:** DOS-05

#### SEC-E4.3 · L4 · Rate limit design
- **Scenario:** Tenant A must not starve tenant B; bursts of 20 OK; sustained 5 rps.
- **Predict impact (write first):** Pick algorithm+keys.
- **Design control:** Token bucket sketch + tests.
- **Map to GCP:** AB-01
- **Unlocks / depends:** AB-01

#### SEC-E4.4 · L4 · Placement ADR
- **Scenario:** Stuffing + L7 flood + per-SKU quota.
- **Predict impact (write first):** Armor vs Gateway vs app — who owns what?
- **Design control:** ADR table.
- **Map to GCP:** AB-02, 4.10
- **Unlocks / depends:** AB-02

#### SEC-E4.5 · L4 · Overlay map
- **Scenario:** Blank packet path.
- **Predict impact (write first):** Place NGFW, Armor, IAP, VPC-SC, LB TLS.
- **Design control:** One primary duty each.
- **Map to GCP:** 6.11, NT-07
- **Unlocks / depends:** NT-07

#### SEC-E4.6 · L4 · SSL policy
- **Scenario:** Legacy clients want TLS 1.0.
- **Predict impact (write first):** Risk?
- **Design control:** Min version policy + exception process.
- **Map to GCP:** CR-12, 6.13
- **Unlocks / depends:** CR-12

#### SEC-E4.7 · L4 · L7 flood expensive search
- **Scenario:** /search hits BQ job path.
- **Predict impact (write first):** Bill + latency impact?
- **Design control:** Cache+Armor+quota+async.
- **Map to GCP:** DOS-03, DOS-07
- **Unlocks / depends:** DOS-03

#### SEC-E4.8 · L4 · Slowloris local only
- **Scenario:** Local fixture vulnerable.
- **Predict impact (write first):** Predict worker exhaustion.
- **Design control:** Fix timeouts; **do not** attack cloud.
- **Map to GCP:** DOS-05
- **Unlocks / depends:** DOS-05

#### SEC-E4.9 · L4 · Anti-bot signup
- **Scenario:** Fake accounts flood.
- **Predict impact (write first):** Where captcha fails alone?
- **Design control:** reCAPTCHA+mail verify+limits.
- **Map to GCP:** AB-03, 4.10
- **Unlocks / depends:** AB-03

#### SEC-E4.10 · L4 · GraphQL batching
- **Scenario:** 1000 aliases in one POST.
- **Predict impact (write first):** Impact.
- **Design control:** Cost analysis limits.
- **Map to GCP:** AB-04
- **Unlocks / depends:** AB-04

#### SEC-E4.11 · L4 · Pagination scrape
- **Scenario:** pageSize=10000 accepted.
- **Predict impact (write first):** Inventory theft math.
- **Design control:** Caps+authz+rate.
- **Map to GCP:** AB-05
- **Unlocks / depends:** AB-05

#### SEC-E4.12 · L4 · Coupon logic abuse
- **Scenario:** Stacking coupons race.
- **Predict impact (write first):** Money impact.
- **Design control:** Invariant+transaction.
- **Map to GCP:** AB-06
- **Unlocks / depends:** AB-06

#### SEC-E4.13 · L4 · Inventory hoarding
- **Scenario:** Bot holds all SKUs 30m.
- **Predict impact (write first):** Fairness fix.
- **Design control:** Caps+bot+short hold.
- **Map to GCP:** AB-07
- **Unlocks / depends:** AB-07

#### SEC-E4.14 · L4 · Export fan-out
- **Scenario:** API triggers email to all users.
- **Predict impact (write first):** Economic+privacy impact.
- **Design control:** Step-up+quota+async.
- **Map to GCP:** AB-08
- **Unlocks / depends:** AB-08

#### SEC-E4.15 · L4 · Amplification ethics
- **Scenario:** Someone asks to 'test reflection' against third party.
- **Predict impact (write first):** Response?
- **Design control:** Refuse; explain lab safety.
- **Map to GCP:** DOS-02, §0.2.10
- **Unlocks / depends:** DOS-02

#### SEC-E4.16 · L4 · Adaptive Protection meaning
- **Scenario:** Docs skim (verify).
- **Predict impact (write first):** What static rate limits miss?
- **Design control:** When enable ADR.
- **Map to GCP:** DOS-04
- **Unlocks / depends:** DOS-04

#### SEC-E4.17 · L4 · Zip bomb upload
- **Scenario:** Multipart zip expands 1000×.
- **Predict impact (write first):** Disk impact.
- **Design control:** Limits+re-encode.
- **Map to GCP:** DOS-06, WA-12
- **Unlocks / depends:** DOS-06

#### SEC-E4.18 · L4 · WAF bypass conceptual
- **Scenario:** SQLi with encoding tricks; WAF on.
- **Predict impact (write first):** Why app fix still required?
- **Design control:** Armor+parameterize defense in depth.
- **Map to GCP:** WA-11
- **Unlocks / depends:** WA-11

#### SEC-E4.19 · L4 · Upload SVG XSS
- **Scenario:** SVG with script served from same origin.
- **Predict impact (write first):** Impact.
- **Design control:** Separate domain+CSP+re-encode.
- **Map to GCP:** WA-12
- **Unlocks / depends:** WA-12

#### SEC-E4.20 · L4 · DNS exfil conceptual
- **Scenario:** Compromised job encodes data in DNS labels.
- **Predict impact (write first):** What logs catch it?
- **Design control:** DNS logging+egress policy.
- **Map to GCP:** NT-03
- **Unlocks / depends:** NT-03

#### SEC-E4.21 · L4 · Subdomain takeover
- **Scenario:** CNAME to deleted Cloud Run.
- **Predict impact (write first):** Hijack path.
- **Design control:** Destroy-order checklist.
- **Map to GCP:** NT-04, 6.16
- **Unlocks / depends:** NT-04

### 5.5 Level 5 — cloud identity & data

#### SEC-E5.1 · L5 · IAM privesc analysis
- **Scenario:** Bindings dump with `tokenCreator` + `run.admin` on same human.
- **Predict impact (write first):** Path to prod owner?
- **Design control:** Remove edges; JIT admin proposal.
- **Map to GCP:** CL-03, 7.2
- **Unlocks / depends:** CL-03

#### SEC-E5.2 · L5 · Cross-tenant bleed
- **Scenario:** Redis cache key `order:{id}` without tenant.
- **Predict impact (write first):** Bleed scenario.
- **Design control:** Key layout + tests.
- **Map to GCP:** CL-06, AU-11
- **Unlocks / depends:** CL-06

#### SEC-E5.3 · L5 · SA JSON in GitHub
- **Scenario:** Key committed 40 days ago; Actions used it.
- **Predict impact (write first):** Containment order?
- **Design control:** Disable+hunt+WIF migration.
- **Map to GCP:** CL-04, IR-05, 7.8
- **Unlocks / depends:** CL-04

#### SEC-E5.4 · L5 · Lateral after Run compromise
- **Scenario:** Compromised Cloud Run can reach SQL public IP.
- **Predict impact (write first):** Pivot story.
- **Design control:** Private IP+FW+SA scopes.
- **Map to GCP:** NT-02, 6.12
- **Unlocks / depends:** NT-02

#### SEC-E5.5 · L5 · IAP vs VPN tabletop
- **Scenario:** Laptop malware on VPN.
- **Predict impact (write first):** What changes with IAP for admin UI?
- **Design control:** Threat table.
- **Map to GCP:** NT-05, 6.14
- **Unlocks / depends:** NT-05

#### SEC-E5.6 · L5 · VPC-SC exfil story
- **Scenario:** Stolen user OAuth can `gsutil cp` to personal project.
- **Predict impact (write first):** Does VPC-SC stop it? Conditions?
- **Design control:** Perimeter design sketch.
- **Map to GCP:** NT-06, 6.15
- **Unlocks / depends:** NT-06

#### SEC-E5.7 · L5 · Public bucket IR
- **Scenario:** SCC: `allUsers` on invoices bucket.
- **Predict impact (write first):** 15-min actions?
- **Design control:** Follow 7.8 public ACE runbook + evidence.
- **Map to GCP:** CL-02, IR-06
- **Unlocks / depends:** CL-02

#### SEC-E5.8 · L5 · Confused deputy copy job
- **Scenario:** ETL SA with `storage.admin` org-wide takes `src` param.
- **Predict impact (write first):** Exfil design by attacker.
- **Design control:** Resource-bound role + VPC-SC.
- **Map to GCP:** CL-05
- **Unlocks / depends:** CL-05

#### SEC-E5.9 · L5 · Poisoned GCS event
- **Scenario:** Object finalize triggers privileged function without signed event trust.
- **Predict impact (write first):** Injection?
- **Design control:** Invoker IAM + payload authz.
- **Map to GCP:** CL-08
- **Unlocks / depends:** CL-08

### 5.6 Level 6 — supply chain & K8s

#### SEC-E6.1 · L6 · Privileged pod review
- **Scenario:** YAML: privileged, hostNetwork, hostPath `/`.
- **Predict impact (write first):** Escape narrative.
- **Design control:** PSS restricted + deny admissions.
- **Map to GCP:** CK-01, CK-02
- **Unlocks / depends:** CK-01

#### SEC-E6.2 · L6 · Secret sprawl hunt
- **Scenario:** Synthetic repo with fake keys in Dockerfile env, TF, CI logs.
- **Predict impact (write first):** Find five sinks.
- **Design control:** Remediation to Secret Manager.
- **Map to GCP:** WL-05, CK-04
- **Unlocks / depends:** WL-05

#### SEC-E6.3 · L6 · Classify then CMEK
- **Scenario:** Fields: email, PAN token, product SKU, debug dump.
- **Predict impact (write first):** Class + control each.
- **Design control:** PV-01 + CR-14 mapping.
- **Map to GCP:** PV-01, 7.3
- **Unlocks / depends:** PV-01

#### SEC-E6.4 · L6 · BinAuth meaning
- **Scenario:** Cluster admits unsigned `:latest`.
- **Predict impact (write first):** Attack.
- **Design control:** Attestor policy dry-run→enforce.
- **Map to GCP:** WL-04, CK-05, 7.5
- **Unlocks / depends:** WL-04

#### SEC-E6.5 · L6 · Poisoned base image
- **Scenario:** Dockerfile `FROM node:latest`.
- **Predict impact (write first):** Supply-chain path.
- **Design control:** Digest pin + AR + scan gate.
- **Map to GCP:** WL-01
- **Unlocks / depends:** WL-01

#### SEC-E6.6 · L6 · Native crash → metadata
- **Scenario:** C++ sidecar overflows; same task SA.
- **Predict impact (write first):** Cloud impact beyond RCE.
- **Design control:** Memory-safe rewrite + metadata restrict.
- **Map to GCP:** WA-10, CL-01
- **Unlocks / depends:** WA-10

#### SEC-E6.7 · L6 · hostPath docker.sock
- **Scenario:** Debug pod mounts docker.sock.
- **Predict impact (write first):** Instant impact.
- **Design control:** Admission deny.
- **Map to GCP:** CK-02
- **Unlocks / depends:** CK-02

#### SEC-E6.8 · L6 · RBAC wildcard secrets
- **Scenario:** Role: resources secrets, verbs *.
- **Predict impact (write first):** Blast radius.
- **Design control:** Least verbs + split SA.
- **Map to GCP:** CK-03
- **Unlocks / depends:** CK-03

#### SEC-E6.9 · L6 · NetworkPolicy default deny
- **Scenario:** Flat GKE namespace.
- **Predict impact (write first):** Lateral path.
- **Design control:** Default-deny + allowlist.
- **Map to GCP:** CK-06
- **Unlocks / depends:** CK-06

#### SEC-E6.10 · L6 · Poisoned pipeline PR
- **Scenario:** Fork PR runs workflow with cloud WIF.
- **Predict impact (write first):** How to steal?
- **Design control:** Permissions + environment gates.
- **Map to GCP:** WL-02
- **Unlocks / depends:** WL-02

#### SEC-E6.11 · L6 · SBOM false comfort
- **Scenario:** Team publishes SBOM, no admissions.
- **Predict impact (write first):** What still fails?
- **Design control:** SBOM+scan+attest chain.
- **Map to GCP:** WL-03
- **Unlocks / depends:** WL-03

#### SEC-E6.12 · L6 · Hermetic build
- **Scenario:** Build curls internet for deps ad hoc.
- **Predict impact (write first):** Poison risk.
- **Design control:** Hermetic+provenance sketch.
- **Map to GCP:** WL-06
- **Unlocks / depends:** WL-06

#### SEC-E6.13 · L6 · Tokenize vs encrypt PAN
- **Scenario:** Need PSP display last4 + charge.
- **Predict impact (write first):** Pick control.
- **Design control:** Decision table PV-03.
- **Map to GCP:** PV-03, Part 5
- **Unlocks / depends:** PV-03

### 5.7 Level 7 — detection & IR

#### SEC-E7.1 · L7 · Log injection
- **Scenario:** Username field `
INFO admin login success`.
- **Predict impact (write first):** SIEM confusion?
- **Design control:** JSON logs + encode.
- **Map to GCP:** WA-09, IR-01
- **Unlocks / depends:** WA-09

#### SEC-E7.2 · L7 · Leaked SA tabletop
- **Scenario:** GitHub secret scanning alert on SA key.
- **Predict impact (write first):** First 15 minutes?
- **Design control:** Fill 7.8 template; grade order.
- **Map to GCP:** IR-05, 7.8
- **Unlocks / depends:** IR-05

#### SEC-E7.3 · L7 · Alert precision
- **Scenario:** 50 daily SCC mediums, ignored.
- **Predict impact (write first):** Which three to page?
- **Design control:** Retune mutes+runbooks.
- **Map to GCP:** IR-02
- **Unlocks / depends:** IR-02

#### SEC-E7.4 · L7 · Ephemeral containment
- **Scenario:** Malicious Run revision scaled to zero.
- **Predict impact (write first):** What evidence remains? Contain how?
- **Design control:** IAM+traffic+logs playbook.
- **Map to GCP:** IR-03
- **Unlocks / depends:** IR-03

#### SEC-E7.5 · L7 · KMS key leak branch
- **Scenario:** Suspect DEK in logs; KEK in KMS.
- **Predict impact (write first):** Different steps?
- **Design control:** CR-15 + IR-05 combined.
- **Map to GCP:** CR-15, IR-05
- **Unlocks / depends:** CR-15

#### SEC-E7.6 · L7 · Economic DoS bill spike
- **Scenario:** LB egress + logging + LLM tokens 10× overnight.
- **Predict impact (write first):** Is it attack or bug?
- **Design control:** Budget kill switch + AB/DOS controls.
- **Map to GCP:** DOS-07, 10.3
- **Unlocks / depends:** DOS-07

#### SEC-E7.7 · L7 · Public object scrape window
- **Scenario:** Bucket public 3 hours.
- **Predict impact (write first):** What can you still know?
- **Design control:** IR-06 evidence plan.
- **Map to GCP:** IR-06
- **Unlocks / depends:** IR-06

#### SEC-E7.8 · L7 · Backup ransomware
- **Scenario:** Same SA deletes SQL + GCS backups.
- **Predict impact (write first):** Design flaw?
- **Design control:** Separation + immutability.
- **Map to GCP:** IR-07
- **Unlocks / depends:** IR-07

### 5.8 Level 8 — AI, privacy, compliance, scale

#### SEC-E8.1 · L8 · CCM gap lite
- **Scenario:** the reference cloud app controls known.
- **Predict impact (write first):** Map to five CCM domains; one gap.
- **Design control:** CM-01 spreadsheet.
- **Map to GCP:** CM-01, 7.9
- **Unlocks / depends:** CM-01

#### SEC-E8.2 · L8 · Cache stampede under attack
- **Scenario:** Attacker forces TTL expiry on hot key.
- **Predict impact (write first):** Availability impact.
- **Design control:** Singleflight+jitter+Armor.
- **Map to GCP:** DOS-08, architecture studios (security-relevant only)
- **Unlocks / depends:** DOS-08

#### SEC-E8.3 · L8 · Prompt injection on Vertex app
- **Scenario:** Support bot with tool `refund(orderId)`.
- **Predict impact (write first):** Indirect injection via ticket body.
- **Design control:** Tool allowlist+confirm+AI-01 controls.
- **Map to GCP:** AI-01, AI-02, 9c
- **Unlocks / depends:** AI-01

#### SEC-E8.4 · L8 · Agent tool abuse
- **Scenario:** Agent has GCS read on all buckets.
- **Predict impact (write first):** Exfil via prompt.
- **Design control:** Narrow SA+confirm.
- **Map to GCP:** AI-02
- **Unlocks / depends:** AI-02

#### SEC-E8.5 · L8 · Confidential VM buys/costs
- **Scenario:** Store DEKs in memory on GCE.
- **Predict impact (write first):** Does Confidential VM stop SSRF? SQLi?
- **Design control:** Memo CR-18/SC-03.
- **Map to GCP:** CR-18, SC-03
- **Unlocks / depends:** CR-18

#### SEC-E8.6 · L8 · RAG AuthZ hole
- **Scenario:** Retriever ignores caller tenant.
- **Predict impact (write first):** Leak story.
- **Design control:** Enforce AuthZ at fetch.
- **Map to GCP:** AI-03, PV-02
- **Unlocks / depends:** AI-03

#### SEC-E8.7 · L8 · Poisoned fine-tune set
- **Scenario:** Crowdsourced examples include jailbreaks.
- **Predict impact (write first):** Risk.
- **Design control:** Curation+eval+sign model.
- **Map to GCP:** AI-04
- **Unlocks / depends:** AI-04

#### SEC-E8.8 · L8 · Shadow AI policy
- **Scenario:** Dev pastes prod order CSV into public chatbot.
- **Predict impact (write first):** Controls.
- **Design control:** Policy+approved Vertex+DLP.
- **Map to GCP:** AI-05
- **Unlocks / depends:** AI-05

#### SEC-E8.9 · L8 · Isolation class ADR
- **Scenario:** HSM-class signing keys proposed on multi-tenant Cloud Run.
- **Predict impact (write first):** Isolation enough?
- **Design control:** SC-02 ADR → KMS/HSM.
- **Map to GCP:** SC-02, CR-14
- **Unlocks / depends:** SC-02

#### SEC-E8.10 · L8 · Privacy vs security logging
- **Scenario:** Security wants 2-year raw HTTP bodies.
- **Predict impact (write first):** Privacy tension?
- **Design control:** PV-05 memo minimize+purpose.
- **Map to GCP:** PV-05
- **Unlocks / depends:** PV-05

### 5.9 Cryptography cards (CR-E*) — ≥25

*Issue among CR modules. Qualitative keys in Appendix K. Never invent ciphertext goldens.*

#### CR-E1 · L1 · Goals & games
- **Scenario:** Three fields: session cookie, product image CDN, bank PAN token.
- **Predict impact (write first):** Name goal+game each.
- **Design control:** Pick primitive class.
- **Map to GCP:** CR-01
- **Unlocks / depends:** CR-01

#### CR-E2 · L1 · Roll-your-own autopsy
- **Scenario:** Snippet: `cipher = xor(msg, sha1(password))`.
- **Predict impact (write first):** Attacks?
- **Design control:** Rewrite with AEAD+KDF.
- **Map to GCP:** CR-02, CR-04, CR-13
- **Unlocks / depends:** CR-02

#### CR-E3 · L2 · Padding oracle story
- **Scenario:** Legacy CBC API returns 'pad err' vs 'mac err'.
- **Predict impact (write first):** What attacker learns.
- **Design control:** Uniform errors + migrate AEAD.
- **Map to GCP:** CR-03
- **Unlocks / depends:** CR-03

#### CR-E4 · L2 · JWT as crypto+auth
- **Scenario:** `alg=none` accepted.
- **Predict impact (write first):** Forgery.
- **Design control:** Allowlist+verify tests.
- **Map to GCP:** CR-10, AU-05
- **Unlocks / depends:** CR-10

#### CR-E5 · L2 · GCM nonce reuse
- **Scenario:** Counter reset after deploy under same key.
- **Predict impact (write first):** Catastrophe class.
- **Design control:** Nonce policy+rotate.
- **Map to GCP:** CR-04
- **Unlocks / depends:** CR-04

#### CR-E6 · L2 · Length extension
- **Scenario:** API uses `sha256(secret||msg)` as auth.
- **Predict impact (write first):** Forge extension.
- **Design control:** HMAC/HKDF.
- **Map to GCP:** CR-05, CR-06
- **Unlocks / depends:** CR-05

#### CR-E7 · L2 · EtM vs MtE
- **Scenario:** Team MACs plaintext then CBC encrypts.
- **Predict impact (write first):** Oracle risk.
- **Design control:** Prefer AEAD; else EtM.
- **Map to GCP:** CR-06
- **Unlocks / depends:** CR-06

#### CR-E8 · L3 · Password KDF rationale
- **Scenario:** Hashes passwords with SHA-256 unsalted.
- **Predict impact (write first):** Offline crack cost.
- **Design control:** Argon2id+salt+pepper plan (4.3 owns lab).
- **Map to GCP:** CR-13, 4.3
- **Unlocks / depends:** CR-13

#### CR-E9 · L3 · Envelope design
- **Scenario:** Large GCS objects + field PII.
- **Predict impact (write first):** KEK/DEK diagram.
- **Design control:** KMS envelope vs app AEAD split.
- **Map to GCP:** CR-14, 7.3
- **Unlocks / depends:** CR-14

#### CR-E10 · L3 · CMEK vs CSEK vs Google-managed
- **Scenario:** Regulated bucket decision.
- **Predict impact (write first):** Pick+justify.
- **Design control:** ADR with residual risk.
- **Map to GCP:** CR-14, 7.3
- **Unlocks / depends:** CR-14

#### CR-E11 · L2 · Bad RNG tokens
- **Scenario:** Session ids from `Math.random`.
- **Predict impact (write first):** Prediction attack.
- **Design control:** CSPRNG 128+ bits.
- **Map to GCP:** CR-07
- **Unlocks / depends:** CR-07

#### CR-E12 · L3 · Forward secrecy timeline
- **Scenario:** Server key stolen Thursday.
- **Predict impact (write first):** Which past sessions readable if ECDHE vs static RSA?
- **Design control:** TLS policy.
- **Map to GCP:** CR-08, CR-12
- **Unlocks / depends:** CR-08

#### CR-E13 · L3 · Raw RSA fails
- **Scenario:** Encrypt 32-byte DEK with textbook RSA.
- **Predict impact (write first):** Problems.
- **Design control:** OAEP/hybrid.
- **Map to GCP:** CR-09
- **Unlocks / depends:** CR-09

#### CR-E14 · L3 · Broken cert validate
- **Scenario:** Mobile app `InsecureSkipVerify`.
- **Predict impact (write first):** MITM impact.
- **Design control:** Fix+pinning tradeoff memo.
- **Map to GCP:** CR-11, CR-12
- **Unlocks / depends:** CR-11

#### CR-E15 · L3 · 0-RTT POST
- **Scenario:** Idempotent GET vs fund transfer POST on 0-RTT.
- **Predict impact (write first):** Replay risk.
- **Design control:** Policy: no 0-RTT for non-idempotent.
- **Map to GCP:** CR-12
- **Unlocks / depends:** CR-12

#### CR-E16 · L4 · KEK vs DEK leak IR
- **Scenario:** Two incidents: DEK in log; KMS IAM abuse on KEK.
- **Predict impact (write first):** Different blast radii.
- **Design control:** CR-15 runbooks.
- **Map to GCP:** CR-15, IR-05
- **Unlocks / depends:** CR-15

#### CR-E17 · L4 · Timing compare
- **Scenario:** MAC check uses `==` early exit.
- **Predict impact (write first):** Remote leak feasibility.
- **Design control:** Constant-time API.
- **Map to GCP:** CR-16
- **Unlocks / depends:** CR-16

#### CR-E18 · L4 · Field-level AEAD
- **Scenario:** TLS only; DBAs read PII.
- **Predict impact (write first):** Insider threat.
- **Design control:** Tink AEAD+KMS.
- **Map to GCP:** CR-17
- **Unlocks / depends:** CR-17

#### CR-E19 · L5 · TEE misconception
- **Scenario:** 'Confidential VM means we can skip AuthZ'.
- **Predict impact (write first):** False claims.
- **Design control:** Buys/costs list.
- **Map to GCP:** CR-18, SC-03
- **Unlocks / depends:** CR-18

#### CR-E20 · L5 · PQC inventory
- **Scenario:** Archives with 10-year secrecy need.
- **Predict impact (write first):** SNDL risk.
- **Design control:** Inventory+agility plan.
- **Map to GCP:** CR-19
- **Unlocks / depends:** CR-19

#### CR-E21 · L2 · HKDF misuse
- **Scenario:** Use HKDF extract with attacker-controlled salt as only secret.
- **Predict impact (write first):** What breaks?
- **Design control:** Label info; secret IKM.
- **Map to GCP:** CR-05
- **Unlocks / depends:** CR-05

#### CR-E22 · L3 · ECDSA nonce reuse
- **Scenario:** Two signatures, same nonce.
- **Predict impact (write first):** Private key recovery awareness.
- **Design control:** Lib only; never DIY nonce.
- **Map to GCP:** CR-10
- **Unlocks / depends:** CR-10

#### CR-E23 · L3 · HSTS missing
- **Scenario:** Cookie Secure but first visit HTTP strip.
- **Predict impact (write first):** SSL strip class.
- **Design control:** HSTS+preload caution.
- **Map to GCP:** CR-12
- **Unlocks / depends:** CR-12

#### CR-E24 · L4 · mTLS lifecycle
- **Scenario:** Service mesh certs expire, outage.
- **Predict impact (write first):** Security vs availability.
- **Design control:** Rotation automation.
- **Map to GCP:** CR-17
- **Unlocks / depends:** CR-17

#### CR-E25 · L4 · Checklist audit
- **Scenario:** the reference cloud app crypto ADR blank.
- **Predict impact (write first):** Gaps vs CR-20.
- **Design control:** Fill eight non-negotiables.
- **Map to GCP:** CR-20
- **Unlocks / depends:** CR-20

#### CR-E26 · L3 · Public key as HMAC secret
- **Scenario:** JWT HS256 with RSA PEMs.
- **Predict impact (write first):** Confusion attack.
- **Design control:** Separate alg+key types.
- **Map to GCP:** CR-10, AU-05
- **Unlocks / depends:** CR-10

#### CR-E27 · L2 · ChaCha vs GCM choice
- **Scenario:** Constrained device software TLS.
- **Predict impact (write first):** Which AEAD often preferred?
- **Design control:** Rationale.
- **Map to GCP:** CR-04
- **Unlocks / depends:** CR-04

#### CR-E28 · L5 · MPC/HE fantasy
- **Scenario:** 'We'll HE the whole DB and query free'.
- **Predict impact (write first):** Cost reality.
- **Design control:** Survey-depth no/yes cases.
- **Map to GCP:** CR-18
- **Unlocks / depends:** CR-18

## 5.10 Extra mixed-transfer cards (E9.*)

#### SEC-E9.1 · L4 · Armor + app limiter cooperation
- **Scenario:** Armor throttles by IP; app by tenant. NAT many users share IP.
- **Predict impact (write first):** Who is unfairly throttled?
- **Design control:** Edge for volumetric; app for tenant; NAT-aware IP as secondary signal.
- **Map to GCP:** AB-02, DOS-03, 4.10, 6.16
- **Unlocks / depends:** AB-01, AB-02

#### SEC-E9.2 · L5 · WIF misbind tabletop
- **Scenario:** Attribute condition missing `repository`; any repo in org can mint tokens.
- **Predict impact (write first):** Blast radius to prod deploy SA.
- **Design control:** Tighten attributes; audit federated principals; rotate.
- **Map to GCP:** CL-04, IR-05, 4.8, 7.8
- **Unlocks / depends:** CL-04, WL-02

#### SEC-E9.3 · L3 · SameSite=Lax vs CSRF on subdomain
- **Scenario:** Evil on `evil.marketing.example.com` with cookie Domain=.example.com; Lax cookies.
- **Predict impact (write first):** Which requests still carry cookies?
- **Design control:** Host-only cookies; CSRF tokens; origin checks.
- **Map to GCP:** AU-03, AU-04, 4.4
- **Unlocks / depends:** AU-03, AU-04

#### SEC-E9.4 · L6 · Cosign attestation gap
- **Scenario:** BinAuth requires attestor A; CI signs with attestor B keys in break-glass.
- **Predict impact (write first):** Who can deploy?
- **Design control:** Dual control; break-glass audited; dry-run first.
- **Map to GCP:** WL-04, CK-05, 7.5
- **Unlocks / depends:** WL-04

#### SEC-E9.5 · L7 · Audit log sink IAM weak
- **Scenario:** Same project SA can overwrite log sink destination objects.
- **Predict impact (write first):** Integrity of IR evidence?
- **Design control:** Sink to separate project; bucket retention; deny overwrite.
- **Map to GCP:** IR-01, 7.6, 10
- **Unlocks / depends:** IR-01

#### SEC-E9.6 · L8 · Model Armor / prompt firewall literacy
- **Scenario:** Vertex app; untrusted docs in RAG.
- **Predict impact (write first):** Indirect injection paths.
- **Design control:** AuthZ at retrieval; DLP; prompt firewall `(verify)` product; tool confirmations.
- **Map to GCP:** AI-01, AI-03, PV-02, 9c
- **Unlocks / depends:** AI-01

#### SEC-E9.7 · L2 · HSTS preload tradeoff
- **Scenario:** Marketing wants HTTP landing A/B; security wants HSTS preload.
- **Predict impact (write first):** What breaks if preload?
- **Design control:** HSTS on app origins first; preload only when all subdomains HTTPS.
- **Map to GCP:** CR-12, A5 TLS / Phase 4 Armor
- **Unlocks / depends:** CR-12

#### SEC-E9.8 · L5 · Public BigQuery dataset ACLs
- **Scenario:** Analyst grants `allAuthenticatedUsers` on dataset "temporarily".
- **Predict impact (write first):** Exfil class.
- **Design control:** Remove; org policy; VPC-SC; SDP classify.
- **Map to GCP:** CL-02, PV-01, 7.3, 7.7
- **Unlocks / depends:** CL-02

#### SEC-E9.9 · L4 · GraphQL persisted queries only
- **Scenario:** Public `/graphql` with introspection on.
- **Predict impact (write first):** Schema recon + DoS.
- **Design control:** Persist allowlist; disable introspection; depth/cost limits.
- **Map to GCP:** AB-04, 4.10
- **Unlocks / depends:** AB-04

#### SEC-E9.10 · L3 · PKCE downgrade
- **Scenario:** AS still accepts auth code without code_verifier for "compat".
- **Predict impact (write first):** Intercept path on public clients.
- **Design control:** Mandatory S256 PKCE; reject missing verifier.
- **Map to GCP:** AU-06, 4.6
- **Unlocks / depends:** AU-06

### 5.11 Crypto deepening cards (CR-E29 … CR-E35)

#### CR-E29 · L3 · Key purpose separation
- **Scenario:** Same RSA key used for TLS and JWT sign.
- **Predict impact (write first):** Agility/compromise coupling.
- **Design control:** One purpose per key; separate KEKs.
- **Map to GCP:** CR-10, CR-14, CR-20
- **Unlocks / depends:** CR-14

#### CR-E30 · L4 · Rewrap vs reencrypt
- **Scenario:** KEK rotation annual; TBs of CMEK objects.
- **Predict impact (write first):** Downtime if reencrypt-all?
- **Design control:** Rewrap DEKs; schedule destroy of old KEK versions.
- **Map to GCP:** CR-14, CR-15, 7.3
- **Unlocks / depends:** CR-14, CR-15

#### CR-E31 · L2 · CBC+HMAC forgotten IV
- **Scenario:** IV fixed to zeros "for determinism".
- **Predict impact (write first):** Leakage class.
- **Design control:** Random IV; prefer AEAD.
- **Map to GCP:** CR-03, CR-04
- **Unlocks / depends:** CR-03

#### CR-E32 · L5 · Confidential Space attestation sketch
- **Scenario:** Process PII in third-party analytics VM.
- **Predict impact (write first):** What attestation buys vs AuthZ.
- **Design control:** CR-18 buys/costs; still AuthZ+DLP.
- **Map to GCP:** CR-18, SC-03 `(verify)`
- **Unlocks / depends:** CR-18

#### CR-E33 · L3 · ACME / managed cert failure mode
- **Scenario:** DNS CAA blocks Google CA; cert renew fails.
- **Predict impact (write first):** Availability+users seeing MITM warnings.
- **Design control:** Monitor expiry; CAA allowlist; managed cert alerts.
- **Map to GCP:** CR-11, A5 TLS / Phase 4 Armor
- **Unlocks / depends:** CR-11

#### CR-E34 · L4 · Envelope encryption local toy
- **Scenario:** Sketch DEK gen → KMS wrap → store blob+wrapped DEK.
- **Predict impact (write first):** What attacker with DB-only access gets.
- **Design control:** Without KMS decrypt IAM, ciphertext useless.
- **Map to GCP:** CR-14, 7.3 toy
- **Unlocks / depends:** CR-14

#### CR-E35 · L2 · Password pepper custody
- **Scenario:** Pepper in source repo; Argon2id otherwise correct.
- **Predict impact (write first):** Offline crack after repo leak.
- **Design control:** Pepper in Secret Manager/KMS; versioned.
- **Map to GCP:** CR-13, 4.3, 4.9
- **Unlocks / depends:** CR-13

## 5.12 Paper drills SEC-Z0.7–SEC-Z0.12

#### SEC-Z0.7 · L0 · IND-CPA cartoon
- **Scenario:** Two message lengths equal; adversary sees ciphertext.
- **Predict impact (write first):** What IND-CPA forbids the adversary from learning.
- **Design control:** State game steps in 4 bullets.
- **Map to GCP:** CR-01
- **Unlocks / depends:** CR-01

#### SEC-Z0.8 · L0 · Shared responsibility Cloud SQL
- **Scenario:** Unpatched app SQLi; Google patches MySQL engine.
- **Predict impact (write first):** Who owns which?
- **Design control:** Matrix row.
- **Map to GCP:** PQ-S-03, 2.3
- **Unlocks / depends:** PQ-S-03

#### SEC-Z0.9 · L0 · ATT&CK tactic pick
- **Scenario:** Attacker uses stolen SA JSON to list buckets.
- **Predict impact (write first):** Tactic+technique family.
- **Design control:** Name detection signal.
- **Map to GCP:** TH-05, CL-04
- **Unlocks / depends:** TH-05

#### SEC-Z0.10 · L0 · Cookie flag table
- **Scenario:** Blank table Secure/HttpOnly/SameSite/Host-only.
- **Predict impact (write first):** Threat each flag mitigates.
- **Design control:** Fill table.
- **Map to GCP:** AU-01, AU-04
- **Unlocks / depends:** AU-01

#### SEC-Z0.11 · L0 · DoS layer label
- **Scenario:** 100 Gbps SYN; 5k rps login; slow headers; bill spike from logging.
- **Predict impact (write first):** Label DOS-01/03/05/07.
- **Design control:** One control each.
- **Map to GCP:** DOS-*
- **Unlocks / depends:** DOS-01

#### SEC-Z0.12 · L0 · CCM domain match
- **Scenario:** Five the reference cloud app controls listed.
- **Predict impact (write first):** Match to IAM/EKM/LOG/TVM/AIS.
- **Design control:** CM-01 checklist row.
- **Map to GCP:** CM-01
- **Unlocks / depends:** CM-01

## 3.x-bis · Cryptography worked illustrations (teach with CR modules)

### CR worked illustration A — Padding oracle (story depth)
Victim API decrypts CBC and returns HTTP 400 "bad padding" vs 403 "bad mac". Attacker flips bits in ciphertext block \(C_i\) and observes which error returns. Over many queries they recover plaintext bytes (Vaudenay). **Teaching move:** derive why *integrity first* (AEAD or EtM) collapses the oracle; connect to CR-03 lab card CR-E3. **the reference cloud app link:** never expose distinct crypto error classes on legacy token decrypt paths.

### CR worked illustration B — GCM nonce reuse
Under AES-GCM, reusing a 96-bit nonce with the same key lets an attacker recover the authentication subkey and forge tags; confidentiality can also fail. **Teaching move:** show nonce as a *resource* like a counter allocated per key version; Cloud KMS key versions as rotation boundaries; app must still unique nonces for local AEAD (Tink). Card CR-E5.

### CR worked illustration C — Envelope encryption on GCS
Object bytes encrypted with DEK_AES-GCM; DEK wrapped by KMS KEK; metadata stores wrapped DEK + key version. Compromise of object store without `cloudkms.cryptoKeyEncrypterDecrypter` yields ciphertext only. **Teaching move:** draw trust boundary between storage IAM and KMS IAM; SoD. Cards CR-E9/E10/E34. Roadmap 7.3 owns the product clickpath.

### CR worked illustration D — JWT algorithm confusion
Library selects verify algorithm from attacker-controlled header. Attacker sets `alg=HS256` and uses the RSA *public* key bytes as HMAC secret; verifier accepts. **Teaching move:** policy allowlist; never let header choose freely; pair with AU-05 and CR-10. Card CR-E4/CR-E26.

### CR worked illustration E — TLS 1.3 0-RTT replay
Client early data replays a POST /transfer. Server accepts duplicate. **Teaching move:** 0-RTT only for safe/idempotent; anti-replay windows; prefer 1-RTT for state changes. Card CR-E15.

### CR worked illustration F — Password offline economics
SHA-256(password) at \(10^9\) guesses/s/GPU vs Argon2id ~64MB ~100 ms. Show order-of-magnitude table; salt kills rainbows; pepper in KMS raises bar after DB leak. Roadmap 4.3 owns implementation; CR-13 owns the math story. Card CR-E8.

## 5.13 Integration drills (multi-module)

#### SEC-E10.1 · L5 · SSRF → metadata → GCS exfil chain
- **Scenario:** Image-fetch API; Compute SA can read prod buckets; no egress deny.
- **Predict impact (write first):** Step chain T1552.005 → object list → exfil.
- **Design control:** Block metadata; minimize SA; VPC-SC; URL allowlist.
- **Map to GCP:** CL-01, CL-02, NT-06, 4.2, 6.15
- **Unlocks / depends:** CL-01, CL-04

#### SEC-E10.2 · L6 · Poisoned base image through BinAuth gap
- **Scenario:** `:latest` tag mutable; attestor not required on one cluster.
- **Predict impact (write first):** Persistence + credential theft.
- **Design control:** Digest pin; BinAuth default deny; break-glass ticketed.
- **Map to GCP:** WL-01, WL-04, CK-05, 7.5
- **Unlocks / depends:** WL-04

#### SEC-E10.3 · L4 · Armor bypass attempt + app still safe
- **Scenario:** Encoded SQLi slips a coarse WAF rule.
- **Predict impact (write first):** DB compromise if app concatenates.
- **Design control:** Parameterized queries primary; WAF depth; logging.
- **Map to GCP:** WA-05, WA-11, 7.4
- **Unlocks / depends:** WA-05

#### SEC-E10.4 · L7 · Ephemeral IR with key leak
- **Scenario:** Cloud Run revision gone; DEK printed in structured log.
- **Predict impact (write first):** Evidence left; crypto IR branch.
- **Design control:** IR-03 + CR-15; disable versions; rewrap.
- **Map to GCP:** IR-03, CR-15, 7.8
- **Unlocks / depends:** IR-03, CR-15

#### SEC-E10.5 · L8 · Indirect prompt injection → refund tool
- **Scenario:** Attacker ticket body instructs agent to call `refund`.
- **Predict impact (write first):** Fraud without login to admin.
- **Design control:** Human confirm; tool allowlist; AuthZ; treat docs as data.
- **Map to GCP:** AI-01, AI-02, 9c
- **Unlocks / depends:** AI-01

#### SEC-E10.6 · L3 · JWT kid pointing to attacker JWKS
- **Scenario:** Library fetches JWKS from `jku` URL.
- **Predict impact (write first):** Full auth bypass.
- **Design control:** Pin JWKS; ignore jku; CR-10 + AU-05.
- **Map to GCP:** AU-05, CR-10, 4.5
- **Unlocks / depends:** AU-05

#### SEC-E10.7 · L5 · Shared VPC trust creep
- **Scenario:** Service project peers broadly; flat allow.
- **Predict impact (write first):** Lateral from low to PCI-like tier.
- **Design control:** Segmentation; PSC; deny default; treat peer as hostile.
- **Map to GCP:** CL-07, NT-02, 6.15
- **Unlocks / depends:** CL-07

#### SEC-E10.8 · L2 · Economic DoS via log flood
- **Scenario:** Unauthenticated endpoint logs full request bodies at 10k rps.
- **Predict impact (write first):** Logging/LB bill spike.
- **Design control:** Sample; body size limits; Armor; budget alerts.
- **Map to GCP:** DOS-07, AB-01, 10.3
- **Unlocks / depends:** DOS-07

## 6. Capstones (SEC-CAP1–SEC-CAP4)

Issue only when stitch prerequisites unlocked. Each produces an ADR pack + tests/tabletop evidence — not a second product walkthrough.

### SEC-CAP1 · the reference cloud app hardening pass
- **Depends:** AU-*, WA-* core, AB-01/02, CL-01, CR-12/13/14/20, A10 / B5 / API auth patterns + 7.3–7.4.
- **Deliverable:** Threat model delta; control matrix; CR-20 checklist audit; failing→passing abuse tests (IDOR, CSRF, SSRF guard, JWT alg); residual risk ADR.
- **GCP map:** Identity Platform / IAP, Armor policy *design* (attach only if Lab Reality), KMS/Secret Manager, Run IAM.
- **Check:** Instructor grades prediction-vs-actual on two abuse tests + checklist completeness.

### SEC-CAP2 · IR tabletop (60–90 min)
- **Depends:** IR-*, CL-02/04, CR-15, roadmap 7.8 templates.
- **Deliverable:** Facilitator injects one of: leaked SA key · public bucket · poisoned CI · KEK misuse; scribe fills Detect→…→Follow-up; grade time-to-contain + whether restore/rewrap tested.
- **GCP map:** Audit logs, IAM disable, SCC finding JSON (synthetic OK).
- **Check:** Order-of-operations correct; no 'redeploy before disable' failure.

### SEC-CAP3 · Abuse-resistant public API
- **Depends:** AB-*, DOS-03/05/07, AU-08, 4.10, 6.16.
- **Deliverable:** Placement ADR (Armor vs Gateway vs app); token-bucket implementation tests; bot signal plan; economic DoS budget alerts; GraphQL or search cost governors if in scope.
- **GCP map:** Armor rate rules (credits-optional), reCAPTCHA Enterprise, Cloud Monitoring budgets.
- **Check:** Tenant fairness test; 429+Retry-After; bill-spike kill switch named.

### SEC-CAP4 · AI-gateway threat model
- **Depends:** AI-01…05, PV-02, CR-18 lite, 9c.
- **Deliverable:** DFDs for prompt/tools/RAG; abuse cases (injection, tool exfil, cross-tenant RAG); controls; shadow-AI policy; residual risk.
- **GCP map:** Vertex AI endpoint IAM, SDP, Model Armor literacy `(verify)`, Secret Manager.
- **Check:** AuthZ-at-retrieval named; tool confirmations; DLP before prompt.

---

### Capstone grading rubrics (shared)

| Dimension | Excellent | Acceptable | Redo |
|---|---|---|---|
| Prediction | Written before design; specific blast radius | Present but vague | Missing |
| Control design | Layered; names residual risk | Single control only | Product name-drop without mechanism |
| GCP map | Correct layer (edge/app/data/id) | Mostly right | Wrong product for threat |
| Ownership | Respects roadmap vs companion split | Minor bleed | Re-teaches A10 / shared-responsibility principles as new |
| Safety | Local/synthetic only | OK | Proposes live attack on third parties |

**SEC-CAP1 bar:** ≥4 abuse tests go red→green; CR-20 checklist marked with evidence paths.
**SEC-CAP2 bar:** Containment order correct on clock; scribe sheet complete; one crypto-key branch exercised.
**SEC-CAP3 bar:** Placement ADR + fairness test + budget kill switch named.
**SEC-CAP4 bar:** AuthZ-at-retrieval explicit; tool confirmation; DLP before prompt.

### Capstone scheduling note

Run **SEC-CAP1** after A10 / B5 / API auth patterns + CR-20 unlocked; **SEC-CAP2** after 7.8 + IR/CR-15; **SEC-CAP3** after 4.10 + 6.16 + AB/DOS; **SEC-CAP4** after 9c + AI-*. Never schedule a capstone that smuggles a locked prop — postpone or unlock first (Prop Lock).

### Exercise issuance reminder

Bank ≠ dump: issue **one** card; prediction line first; escalate hints; open Appendix K only after attempt. Mixed-transfer cards must name two prior unlocked IDs on the first line of the learner's answer.

## 7. Teaching notes bank (instructor-facing, short)

1. **Never open Appendix K first.** Predict → attempt → discrepancy → key.
2. **A10 / shared-responsibility principles recall line:** "CIA, least privilege, defense in depth, assume breach, zero trust, shared responsibility — already unlocked; today we add *mechanics*."
3. **Prop Lock examples:** no VPC-SC before 6.15; no BinAuth before 7.5; no Confidential VM as assumed before CR-18/SC-03.
4. **Lab safety script:** "We exploit only loopback fixtures or disposable projects we own. No third-party scanning, no live DDoS, no stuffing real accounts."
5. **Crypto library rule:** Tink / libsodium / lang stdlib — inventing AES is an automatic redo.
6. **When roadmap and companion conflict on order:** roadmap wins; postpone companion exercise.
7. **Mixed-transfer utterance:** "We'll use AU-05 and CR-10 together; name both before solving."
8. **SCC green ≠ secure:** pair 7.6 with IR-02 alert design on day one of detection.
9. **AI session:** always AuthZ-at-retrieval; never "the model will refuse."
10. **FinOps security:** DOS-07 budget alerts are security controls.

## 8. CSA CCM v4.x coverage checklist (lite)

Use as a *gap finder*, not a dump. Mark the reference cloud app evidence paths.

| CCM domain | Companion homes | the reference cloud app evidence sketch |
|---|---|---|
| GRC | CM-01, 7.9 | ADRs, risk register |
| A&A | CM-02, 7.9 | Control matrix |
| ILM | PV-01…04 | Classification labels |
| IAM | CL-03, AU-*, B5 IAM/7.2 | Least privilege bindings |
| UEM | NT-05, 6.14 | IAP device signals literacy |
| EKM / CEK | CR-14…15, 7.3 | KMS keys, CMEK |
| DSP | PV-02, 7.3 | SDP jobs |
| LOG | IR-01, 10 | Audit sinks separate project |
| IVS | CK-*, WL-*, 7.5 | Hardened runtime |
| SEF / TVM | IR-*, WL-01 | IR + scanning |
| STA | WL-*, CR-10 | Attestations |
| AIS | 3.0/4.x, WA-* | Secure SDLC tests |
| DCS | PQ-S-03 | Shared responsibility matrix |
| MSC | NT-*, 6.x | Network segmentation |
| BCE | IR-07 | Backup immutability |

## 9. ATT&CK cloud quick map (teaching)

| Technique (verify IDs live) | Companion | Detection sketch |
|---|---|---|
| T1552.005 IMDS | CL-01 | Metadata access from app; SSRF guard metrics |
| Valid SA key use | CL-04 | `google.iam.v*.*` key create; anomalous auth |
| Public storage | CL-02 | SCC public bucket; policy deny |
| Resource hijack (DNS) | NT-04 | DNS change alerts |
| Supply chain | WL-* | Admission deny; provenance missing |
| Exfil over DNS | NT-03 | DNS query volume anomalies |

## Appendix K — Instructor keys (AFTER attempt only)

*Qualitative. Do not paste before learner attempt. No numeric DB goldens.*

### K-Z0 / K-E1
- **SEC-Z0.1:** Only AES-GCM (AEAD) gives confidentiality under Kerckhoffs among typical lists; bcrypt is password KDF not general encryption; Base64/URL/rot13 none; SHA-256 integrity-ish not conf; HMAC authenticity; XOR homemade fails.
- **SEC-Z0.2:** User AuthN at app/IAP/IdP — not GFE alone; service AuthN via SA/mTLS/ID tokens; TLS hop-by-hop may terminate at LB.
- **SEC-Z0.3:** Deny default→fail-safe; parameterized SQL→economy/complete mediation; IAP→complete mediation/least privilege; org policy→fail-safe.
- **SEC-E1.1:** Accept any coherent STRIDE; must include AuthZ elevation (BOLA) and SSRF/DoS somewhere if checkout talks outbound.
- **SEC-E1.3:** Prefer cheaper edge early if threat model allows; accept residual volumetric risk on Hosting-only — explicit Z.

### K-session / CSRF / XSS (E2.x)
- **SEC-E2.2:** Secure+HttpOnly+SameSite; split cookie domains; rotate session; XSS fix on marketing.
- **SEC-E2.3:** Server mints id; regenerate on login; never accept client session id.
- **SEC-E2.5:** HttpOnly stops JS cookie read but XSS still drives actions; CSRF token in DOM readable — use cookie+header pattern carefully; encode+CSP.
- **SEC-E2.7:** Credentials+`*` is illegal/broken; evil.com can call API as user if reflection bug; exact origins.

### K-auth (E3.x)
- **SEC-E3.2:** Block link-local/metadata; allowlist; no open redirects; tests for 169.254.169.254; Run preferred over broad GCE scopes.
- **SEC-E3.5:** Attacker signs HS256 with PEM public key as secret if library switches alg; fix allowlist RS256 only + key from config.
- **SEC-E3.6:** Exact redirect URI; PKCE; state bound.
- **SEC-E3.8:** Authz `(user, action, order)` + tenant predicate; negative tests.
- **SEC-E3.10:** Number matching or WebAuthn; rate-limit pushes.

### K-abuse / DoS (E4.x)
- **SEC-E4.3:** Token bucket keyed by tenant then user; IP secondary; burst 20 capacity, refill 5/s — numbers illustrative.
- **SEC-E4.4:** Armor volumetric/L7 flood; Gateway API quotas; app business limits+bot.
- **SEC-E4.8:** Local only — safety.
- **SEC-E4.15:** Refuse third-party attack.

### K-cloud (E5.x)
- **SEC-E5.3:** Disable key/SA first; audit window; rotate; migrate WIF; never 'rotate later'.
- **SEC-E5.6:** VPC-SC stops copy to projects outside perimeter *when enforced and services in scope* `(verify)`; IAM theft alone insufficient.
- **SEC-E5.7:** Remove ACE → inventory → classify → notify decision → org policy.

### K-supply (E6.x)
- **SEC-E6.1:** Privileged+hostPath=/ ≈ host root.
- **SEC-E6.4:** BinAuth admits only attested digests — not a vuln scanner substitute.
- **SEC-E6.6:** RCE→metadata token→cloud API as SA.

### K-IR (E7.x)
- **SEC-E7.2/SEC-E7.5:** Disable/contain before rebuild; DEK leak re-encrypt data; KEK leak rewrap DEKs + disable KMS versions.
- **SEC-E7.4:** Logs+IAM+artifact registry image; traffic to last known good; no disk forensics on vanished revision.

### K-AI / privacy (E8.x)
- **SEC-E8.3:** Ticket body injects tool call; require human confirm refund; narrow tool.
- **SEC-E8.6:** Retrieval layer enforces tenant AuthZ — model cannot be trusted to filter.
- **SEC-E8.5:** TEE does not stop SQLi/SSRF/IAM misbind.

### K-crypto (CR-E*)
- **CR-E1:** Cookie: integrity+auth (MAC/AEAD session store id); image: often integrity/CDN TLS; PAN token: tokenization preferred / AEAD if stored.
- **CR-E3:** Padding oracle → byte-wise decrypt; migrate AEAD; uniform errors.
- **CR-E5:** GCM nonce reuse → forgeries + lost confidentiality.
- **CR-E6:** Length extension forgery; use HMAC.
- **CR-E8:** GPU cracks fast hashes; Argon2id memory-hard; salt unique; pepper in KMS.
- **CR-E9:** KEK in KMS wraps per-object DEKs; field AEAD separate.
- **CR-E12:** ECDHE FS: past sessions safe if ephemerals erased; static RSA KX: past sessions decryptable.
- **CR-E15:** 0-RTT replay can duplicate POST.
- **CR-E19:** Buys memory confidentiality vs host; not AuthZ/app bugs.
- **CR-E20:** Store-now-decrypt-later → inventory long-lived.
- **CR-E26:** Classic JWT confusion.

---

### K-extra (SEC-E9 / CR-E29+ / SEC-Z0.7+)
- **SEC-E9.1:** Per-IP edge unfair on NAT; tenant key in app; document layered ADR.
- **SEC-E9.2:** Missing repo attribute → any workflow in org; fix condition; audit STS; treat as key leak IR.
- **SEC-E9.3:** Cross-site subdomain cookie; Host-only + CSRF.
- **SEC-E9.5:** Log sink overwrite = evidence destruction; separate project + retention.
- **SEC-E9.10:** PKCE optional = code intercept on public clients.
- **CR-E29:** Dual purpose keys couple TLS and identity compromise.
- **CR-E30:** Rewrap DEKs under new KEK; destroy old version on schedule; no full reencrypt required for CMEK objects `(verify)` product behavior.
- **CR-E31:** Fixed IV ⇒ deterministic ciphertext leaks equality.
- **CR-E35:** Pepper in git collapses to unsalted after repo leak.
- **SEC-Z0.7:** IND-CPA: adversary cannot distinguish encryptions of equal-length chosen messages.
- **SEC-Z0.11:** SYN→DOS-01; login flood→DOS-03; slow header→DOS-05; logging bill→DOS-07.

### K-worked-illustrations
- Padding oracle: distinct errors leak plaintext via adaptive CBC malleability; AEAD removes oracle.
- GCM reuse: auth key recovery / forgery; treat nonce uniqueness as hard invariant.
- Envelope: storage IAM ≠ KMS IAM; SoD is the point.
- JWT confusion: header-driven alg + public key as HMAC secret.
- 0-RTT: replayable early data; forbid for non-idempotent.
- Password economics: memory-hard KDF changes attacker cost by orders of magnitude.

## Appendix N — Reference cloud-app threat model (living sketch)

*Update as Parts unlock. Not a second roadmap — a stitch aid.*

| Plane | Assets | Primary attackers | Top companion modules | Roadmap anchors |
|---|---|---|---|---|
| Storefront | Session, catalog, carts | Web attacker, bots | AU-01…04, WA-02, AB-03, DOS-03 | A5 TLS / Phase 4 Armor, 4.4, 4.10 |
| Customer API | Orders, PII, tokens | Web, stuffing, IDOR | AU-08, AU-11, WA-05, AB-01, CL-01 | 4.2–4.7, 4.10 |
| Admin | Refunds, config | Stolen session, CSRF, BFLA | AU-03, AU-12, NT-05 | 4.4, 4.7, 6.14 |
| Service-to-service | SA identity, internal RPC | Confused deputy, key theft | AU-14, CL-04, CR-17 | 4.8, 7.2 |
| Data | SQL, GCS, BQ | Public ACE, SSRF→cred, insider | CL-02, CR-14, PV-*, NT-06 | 7.3, 6.15 |
| CI/CD | Build SA, images | Poisoned PR, unsigned deploy | WL-02, WL-04, CK-05 | 4.8, 7.5 |
| AI gateway | Tools, RAG corpus | Prompt injection, tool abuse | AI-01…05, PV-02 | 9c |

**Always-on residual risks to name in ADRs:** insider with legitimate IAM; 0-day in managed runtime; economic DoS under budget; supply chain of transitive deps; prompt injection on any LLM tool with side effects.

## Appendix U — University course → module quick index

| Course | Lecture themes (compressed) | Open these IDs |
|---|---|---|
| Stanford CS255 | Games; PRFs; AES; AEAD; DH; RSA; signatures; TLS; randomness | CR-01…CR-12, CR-07 |
| Stanford CS155 | Control hijack; web attacker; network attacker; cloud apps; AI security | WA-10, TH-01, WA-*, NT-*, AI-* |
| Stanford XACS235 | Shared responsibility; K8s; IAM; KMS; SecOps; bots; CCM; privacy; TEEs | PQ-S-03, CK-*, CL-*, CR-14, CR-18, IR-*, AB-03, CM-*, PV-*, SC-03 |
| MIT 6.858/6.566 | Threat models; privsep; sandbox; web; TLS; side channels; economics | TH-*, WA-*, CR-12, CR-16, SC-*, PQ-S-05 |
| Berkeley CS161 | Crypto; ACL/capabilities; spoofing/TCP/BGP/DNS; TLS; DoS; XSS/CSRF; anonymity | CR-* lite, NT-04, DOS-*, WA-01…03, PR-anon lite |
| CMU 95-746 | Cloud transfer; IAM CSP/CSC; data states; TTPs; compliance; isolation | PQ-S-03, CL-*, CR-14/17/18, CM-*, IR-*, SC-02 |

*This index is a stitch aid — not a claim that the companion replaces those courses.*

## Appendix V — Verification / honesty notes

1. **`(verify)` flags** appear on version-sensitive GCP SKUs: Armor Adaptive Protection availability/billing; reCAPTCHA Enterprise free tier quotas; Binary Authorization on Cloud Run vs GKE; Confidential Computing product names; Model Armor; metadata header names for SSRF defenses; org policy constraint IDs; TLS SSL policy enums. Re-check live docs before exams/production.
2. **OWASP Top 10:2025** — confirm current letter list at teach time; map by *meaning* not memorized letter alone.
3. **No live DDoS, no third-party scanning, no stuffing real accounts, no malware.** Local fixtures only for exploit-then-fix.
4. **Crypto:** vetted libraries only (Tink, libsodium, language stdlib). Never invent AES/RSA/HMAC. No ciphertext fingerprint goldens.
5. **Roadmap wins** on order, Lab Reality, ledger; this companion wins on attack/crypto/exercise specs.
6. **University sources** paraphrased for teaching alignment — not a transcript of any course; cite CS155/CS255/XACS235/6.858/CS161/95-746/CSA CCM as inspiration.
7. **ATT&CK T1552.005** technique IDs may be renumbered — verify on attack.mitre.org.
8. **A10 / shared-responsibility principles principles** recalled never re-taught as new.
10. **Built** 2026-09-22 for the reference cloud app / gcp.md pairing.

---

*End of The Cloud Cybersecurity Companion — GCP-Native Edition.*

11. **Line-count / completeness note:** This companion prioritizes stitchable attack+crypto depth over encyclopedic CCM dumps; use §8 as a gap finder when auditing the reference cloud app evidence.
13. **When in doubt on a GCP SKU name:** prefer gcp.md product lab + live docs; companion scenarios stay valid even if a SKU renames.

---

*End of The Cloud Cybersecurity Companion — GCP-Native Edition. Stitch with gcp.md; bank ≠ dump; CR-* is a first-class pillar.*
