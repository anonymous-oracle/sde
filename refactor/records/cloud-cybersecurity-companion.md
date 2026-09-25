# Records for cloud-cybersecurity-companion.md (R2b, R2c and R4 build edits, 2026-09-24)

Refactor bookkeeping only, not course material. Decision D6 keeps provenance, the D3 archive and every line the build changed or removed (R2b; the R2c Go tie-ins; R4, rules R4-*) out of the course files; decision D3 keeps them here, verbatim. Each entry names the build journal number (outputs/r2b/journal.jsonl), the rule and the class.

**J178** · G0 · R2 in-file D3 archive, moved out whole

````text


---

## Pre-refactor text archive (D3)

*Refactor-authored section (2026-09-24).* Decision D3 says content may be re-arranged but never removed. Each block below is the exact pre-refactor text (after the §5 ID renames) of a line that R2 corrected or regenerated. It is kept for provenance only and is **not authoritative**; the live text above wins. Tooling excludes this section from ID and anchor checks.

**D3-01** · C-10 · title

```text
# The Cloud Cybersecurity Companion — Standalone Edition
```

**D3-02** · C-17 · intro "standalone" line

```text
This file is **standalone**. It does not depend on other companion files. It covers **cloud security, cybersecurity, cryptography, and network security** for cloud infrastructure and cloud-hosted distributed systems — taught in parallel with the matching sections of `gcp.md`.
```

**D3-03** · C-03 · §0.4 notation, anchor legend

```text
- `gcp.md` IDs: `A5`, `A7`, `A10`, `B1`, `B5`, `C1`, `C2`, `Phase4-Sec`, `Phase4-Net`, cert names (PCA, Cloud Security Engineer, …)
```

**D3-04** · §6.2 · §2 stitch table (pre-refactor)

```text
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
```

**D3-05** · C-14 · §3.3.1 CR session bundles

```text
1. CR-01…04 + CR-E1…E5 with Part A5 TLS / Phase 4 Armor TLS day (channel vs object encryption distinction).
2. CR-05…07 + CR-13 with A10 / B5 / API auth patterns.3 (password/KDF day).
3. CR-08…12 with Part A5 TLS / Phase 4 Armor / 6.13 (PKI/TLS depth).
4. CR-14…15 + CR-20 with GCP KMS / CMEK (Phase 4 Security) / 7.8 (KMS + key IR).
5. CR-16…19 with GCP KMS / CMEK (Phase 4 Security) Confidential Computing literacy + 9c privacy (survey depth).
```

**D3-06** · C-10 · Appendix V items 8–13 and the two footers

```text
8. **A10 / shared-responsibility principles principles** recalled never re-taught as new.
10. **Built** 2026-09-22 for the reference cloud app / gcp.md pairing.

---

*End of The Cloud Cybersecurity Companion — GCP-Native Edition.*

11. **Line-count / completeness note:** This companion prioritizes stitchable attack+crypto depth over encyclopedic CCM dumps; use §8 as a gap finder when auditing the reference cloud app evidence.
13. **When in doubt on a GCP SKU name:** prefer gcp.md product lab + live docs; companion scenarios stay valid even if a SKU renames.

---

*End of The Cloud Cybersecurity Companion — GCP-Native Edition. Stitch with gcp.md; bank ≠ dump; CR-* is a first-class pillar.*
```

````

**J179** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: foreign labels rebound: `T.SysTheory` (§6.1 → A8 + A9 (+ U5)); primary anchor per the §6.2 crosswalk: A10 (gate for CR-01).
````

**J180** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.1 recall` (C-10); primary anchor per the §6.2 crosswalk: A10.
````

**J181** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N7.1; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `B5 IAM` (C-10); primary anchor per the §6.2 crosswalk: B1.
````

**J182** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: foreign labels rebound: `F1` (§6.1 → A3 + A6); corrupted pseudo-anchors removed, not reverse-engineered: `A5 TLS / Phase 4 Armor` (C-10); primary anchor per the §6.2 crosswalk: A5 HTTP/TLS (preview).
````

**J183** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.1` (C-10); primary anchor per the §6.2 crosswalk: A10.
````

**J184** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: foreign labels rebound: `B4` (C-04: B4 is FinOps in `Curriculum`); primary anchor per the §6.2 crosswalk: A10.
````

**J185** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N0.4; C-03); primary anchor per the §6.2 crosswalk: A10.
````

**J186** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: foreign labels rebound: `B4` (C-04: B4 is FinOps in `Curriculum`); primary anchor per the §6.2 crosswalk: A10.
````

**J187** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N7.4; C-03); foreign labels rebound: `B4` (C-04: B4 is FinOps in `Curriculum`); primary anchor per the §6.2 crosswalk: A10.
````

**J188** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N3.0, N4.7; C-03); primary anchor per the §6.2 crosswalk: A7.
````

**J189** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.6` (C-10); primary anchor per the §6.2 crosswalk: Phase 4 Security (SecOps).
````

**J190** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N8; C-03); primary anchor per the §6.2 crosswalk: A9.
````

**J191** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: primary anchor per the §6.2 crosswalk: A10.
````

**J192** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: primary anchor per the §6.2 crosswalk: A10.
````

**J193** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: primary anchor per the §6.2 crosswalk: A10.
````

**J194** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: primary anchor per the §6.2 crosswalk: A10.
````

**J195** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: primary anchor per the §6.2 crosswalk: A10.
````

**J196** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: primary anchor per the §6.2 crosswalk: A10.
````

**J197** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N1.2; C-03); primary anchor per the §6.2 crosswalk: A10.
````

**J198** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: primary anchor per the §6.2 crosswalk: A10.
````

**J199** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: primary anchor per the §6.2 crosswalk: A10.
````

**J200** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N4.5, N7.5; C-03); primary anchor per the §6.2 crosswalk: A10.
````

**J201** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `A5 TLS / Phase 4 Armor` (C-10); primary anchor per the §6.2 crosswalk: A5 TLS.
````

**J202** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N6.13; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `A5 TLS / Phase 4 Armor` (C-10); primary anchor per the §6.2 crosswalk: A5 TLS.
````

**J203** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.3 owner labs` (C-10); primary anchor per the §6.2 crosswalk: A10.
````

**J204** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.3 owner product` (C-10); primary anchor per the §6.2 crosswalk: Phase 4 Security.
````

**J205** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.8` (C-10); primary anchor per the §6.2 crosswalk: Phase 4 Security.
````

**J206** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: primary anchor per the §6.2 crosswalk: A10.
````

**J207** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N4.8; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.3` (C-10); primary anchor per the §6.2 crosswalk: Phase 4 Security.
````

**J208** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N9c; C-03); primary anchor per the §6.2 crosswalk: Phase 4 Security.
````

**J209** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: primary anchor per the §6.2 crosswalk: A10.
````

**J210** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N7.3; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.9` (C-10); primary anchor per the §6.2 crosswalk: Phase 4 Security.
````

**J211** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.4` (C-10); primary anchor per the §6.2 crosswalk: A10.
````

**J212** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.4` (C-10); primary anchor per the §6.2 crosswalk: A10.
````

**J213** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.4` (C-10); primary anchor per the §6.2 crosswalk: A10.
````

**J214** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.4` (C-10); primary anchor per the §6.2 crosswalk: A10.
````

**J215** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.5` (C-10); primary anchor per the §6.2 crosswalk: A7.
````

**J216** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.6` (C-10); primary anchor per the §6.2 crosswalk: A7.
````

**J217** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.6 literacy` (C-10); primary anchor per the §6.2 crosswalk: A7.
````

**J218** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N4.10; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.3` (C-10); primary anchor per the §6.2 crosswalk: A10 (MFA).
````

**J219** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.3` (C-10); primary anchor per the §6.2 crosswalk: A10 (MFA).
````

**J220** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.3` (C-10); primary anchor per the §6.2 crosswalk: A10 (MFA).
````

**J221** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.7` (C-10); primary anchor per the §6.2 crosswalk: A7.
````

**J222** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.7` (C-10); primary anchor per the §6.2 crosswalk: A7.
````

**J223** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.7` (C-10); primary anchor per the §6.2 crosswalk: A7.
````

**J224** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.8`, `B5 IAM` (C-10); primary anchor per the §6.2 crosswalk: B5.
````

**J225** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N4.10; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.2` (C-10); primary anchor per the §6.2 crosswalk: A7.
````

**J226** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N6.13; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.10` (C-10); primary anchor per the §6.2 crosswalk: A7.
````

**J227** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.10` (C-10); primary anchor per the §6.2 crosswalk: A7.
````

**J228** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N3.x; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.10` (C-10); primary anchor per the §6.2 crosswalk: A7.
````

**J229** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N8.1; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.7` (C-10); primary anchor per the §6.2 crosswalk: A7.
````

**J230** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N5.x, N3.0; C-03); primary anchor per the §6.2 crosswalk: A7.
````

**J231** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N5; C-03); primary anchor per the §6.2 crosswalk: A7.
````

**J232** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N9b, N4.10; C-03); primary anchor per the §6.2 crosswalk: A7.
````

**J233** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `A5/Phase4-Net.16`, `A5 TLS / Phase 4 Armor` (C-10); primary anchor per the §6.2 crosswalk: A5 load balancing.
````

**J234** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `A5/Phase4-Net.16` (C-10); primary anchor per the §6.2 crosswalk: A5 DNS/UDP.
````

**J235** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N6.16; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.10` (C-10); primary anchor per the §6.2 crosswalk: A10.
````

**J236** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `A5/Phase4-Net.16` (C-10); primary anchor per the §6.2 crosswalk: Phase 4 Networking (Prop Lock).
````

**J237** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N6.13; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.2` (C-10); primary anchor per the §6.2 crosswalk: A10.
````

**J238** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N8, N4.2; C-03); primary anchor per the §6.2 crosswalk: A6.
````

**J239** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N10.3; C-03); primary anchor per the §6.2 crosswalk: B4.
````

**J240** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N8, N9.1; C-03); primary anchor per the §6.2 crosswalk: A9.
````

**J241** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.4` (C-10); primary anchor per the §6.2 crosswalk: A10.
````

**J242** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.4` (C-10); primary anchor per the §6.2 crosswalk: A10.
````

**J243** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.4` (C-10); primary anchor per the §6.2 crosswalk: A10.
````

**J244** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `A5 TLS / Phase 4 Armor` (C-10); primary anchor per the §6.2 crosswalk: A10.
````

**J245** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N7.4; C-03); foreign labels rebound: `Part 2` (the old parent's data part; §6.1 → A8 + N2.x); corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.9` (C-10); primary anchor per the §6.2 crosswalk: A10.
````

**J246** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.4` (C-10); primary anchor per the §6.2 crosswalk: A10.
````

**J247** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.4` (C-10); primary anchor per the §6.2 crosswalk: A10.
````

**J248** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N4.2; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.6` (C-10); primary anchor per the §6.2 crosswalk: A10.
````

**J249** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N10; C-03); primary anchor per the §6.2 crosswalk: C6.
````

**J250** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: primary anchor per the §6.2 crosswalk: A6 + U1.
````

**J251** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N6.16; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `A5 TLS / Phase 4 Armor` (C-10); primary anchor per the §6.2 crosswalk: V-NET (Armor).
````

**J252** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.9` (C-10); primary anchor per the §6.2 crosswalk: A10.
````

**J253** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N7.4; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.2` (C-10); primary anchor per the §6.2 crosswalk: B5.
````

**J254** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N7.7; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.3` (C-10); primary anchor per the §6.2 crosswalk: B5.
````

**J255** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N7.2; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `B5 IAM` (C-10); primary anchor per the §6.2 crosswalk: B5.
````

**J256** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N7.8; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.8` (C-10); primary anchor per the §6.2 crosswalk: B5.
````

**J257** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N4.8; C-03); primary anchor per the §6.2 crosswalk: B5.
````

**J258** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N8.1; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.7` (C-10); primary anchor per the §6.2 crosswalk: A9.
````

**J259** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `A5/Phase4-Net.15` (C-10); primary anchor per the §6.2 crosswalk: V-NET.
````

**J260** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N3.4; C-03); primary anchor per the §6.2 crosswalk: B2.
````

**J261** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N7.1; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `A5/Phase4-Net.14` (C-10); primary anchor per the §6.2 crosswalk: A5 NAT/firewalls/proxies.
````

**J262** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N7.6; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `A5/Phase4-Net.12` (C-10); primary anchor per the §6.2 crosswalk: A5 NAT/firewalls/proxies.
````

**J263** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N6.16; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `A5/Phase4-Net.15` (C-10); primary anchor per the §6.2 crosswalk: A5 DNS.
````

**J264** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `A5/Phase4-Net.16` (C-10); primary anchor per the §6.2 crosswalk: A5 DNS.
````

**J265** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `A5/Phase4-Net.14` (C-10); primary anchor per the §6.2 crosswalk: A5 VPN.
````

**J266** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `A5/Phase4-Net.15` (C-10); primary anchor per the §6.2 crosswalk: Phase 4 Security (Prop Lock).
````

**J267** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `A5/Phase4-Net.11` (C-10); primary anchor per the §6.2 crosswalk: A5 NAT/firewalls/proxies.
````

**J268** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: primary anchor per the §6.2 crosswalk: A5 TLS.
````

**J269** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N7.5; C-03); foreign labels rebound: `D8` (C-53 D0…D8 → C1–C5 by content); corrupted pseudo-anchors removed, not reverse-engineered: `A5.2` (C-10); primary anchor per the §6.2 crosswalk: C1.
````

**J270** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N9.2; C-03); foreign labels rebound: `D8` (C-53 D0…D8 → C1–C5 by content); primary anchor per the §6.2 crosswalk: C1.
````

**J271** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N9.2, N7.2; C-03); primary anchor per the §6.2 crosswalk: C2.
````

**J272** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N4.9; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.3` (C-10); primary anchor per the §6.2 crosswalk: C1.
````

**J273** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.5` (C-10); primary anchor per the §6.2 crosswalk: C2.
````

**J274** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N9.2; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `A5/Phase4-Net.15` (C-10); primary anchor per the §6.2 crosswalk: C2.
````

**J275** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.5` (C-10); primary anchor per the §6.2 crosswalk: C1.
````

**J276** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: foreign labels rebound: `D2` (§6.1 → C4); corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.8` (C-10); primary anchor per the §6.2 crosswalk: C4.
````

**J277** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.5` (C-10); primary anchor per the §6.2 crosswalk: C4.
````

**J278** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.5` (C-10); primary anchor per the §6.2 crosswalk: Phase 4 Security.
````

**J279** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N9c; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `A10/B5.9` (C-10); primary anchor per the §6.2 crosswalk: C4.
````

**J280** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.5` (C-10); primary anchor per the §6.2 crosswalk: C4.
````

**J281** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N10.0; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.6` (C-10); primary anchor per the §6.2 crosswalk: C6.
````

**J282** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.6` (C-10); primary anchor per the §6.2 crosswalk: C6.
````

**J283** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.8` (C-10); primary anchor per the §6.2 crosswalk: C7.
````

**J284** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N7.6; C-03); primary anchor per the §6.2 crosswalk: C6.
````

**J285** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.8` (C-10); primary anchor per the §6.2 crosswalk: C7.
````

**J286** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.8` (C-10); primary anchor per the §6.2 crosswalk: C7.
````

**J287** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N2.3; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.8` (C-10); primary anchor per the §6.2 crosswalk: C7.
````

**J288** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.8` (C-10); primary anchor per the §6.2 crosswalk: C7.
````

**J289** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N9c; C-03); primary anchor per the §6.2 crosswalk: D4.
````

**J290** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N9c; C-03); primary anchor per the §6.2 crosswalk: D4.
````

**J291** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N9c.2; C-03); primary anchor per the §6.2 crosswalk: D4.
````

**J292** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N9c; C-03); primary anchor per the §6.2 crosswalk: D4.
````

**J293** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N9c; C-03); primary anchor per the §6.2 crosswalk: D4.
````

**J294** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: primary anchor per the §6.2 crosswalk: A10.
````

**J295** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N8; C-03); primary anchor per the §6.2 crosswalk: B2.
````

**J296** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N7.3; C-03); primary anchor per the §6.2 crosswalk: Phase 4 Security.
````

**J297** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N7.9; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.3` (C-10); primary anchor per the §6.2 crosswalk: Phase 4 Security.
````

**J298** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N9c; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.3` (C-10); primary anchor per the §6.2 crosswalk: Phase 4 Security.
````

**J299** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N5; C-03); primary anchor per the §6.2 crosswalk: Phase 4 Security.
````

**J300** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N6.15; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.9` (C-10); primary anchor per the §6.2 crosswalk: Phase 4 Security.
````

**J301** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N7.9; C-03); primary anchor per the §6.2 crosswalk: U7.
````

**J302** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.9` (C-10); primary anchor per the §6.2 crosswalk: Phase 4 Security.
````

**J303** · G1 · line moved out of the course file

````text
- **Provenance** *(refactor, 2026-09-24)*: old numbered sections kept in N-form (N5; C-03); corrupted pseudo-anchors removed, not reverse-engineered: `Phase4-Sec.9` (C-10); primary anchor per the §6.2 crosswalk: Phase 4 Security.
````

**J304** · G2 · move

````text
| **A5** | PQ-S-04 (HTTP/TLS (preview)), CR-11 (TLS), CR-12 (TLS), DOS-01 (load balancing), DOS-02 (DNS/UDP), NT-01 (NAT/firewalls/proxies), NT-02 (NAT/firewalls/proxies), NT-07 (NAT/firewalls/proxies), NT-03 (DNS), NT-04 (DNS), NT-05 (VPN), NT-08 (TLS) — CR-11/CR-12 at mechanism level plus the minimal public-key intuition bridge (C-14) | AU-01 (HTTP cookie mechanics (recall)), AU-02 (HTTP cookie mechanics (recall)), AU-03 (HTTP cookie mechanics (recall)), AU-04 (HTTP cookie mechanics (recall)), DOS-05 (HTTP (recall)) | SEC-E4.21 (was E-NT1), CR-E12 |
````

**J305** · G2 · move

````text
| **A7** | TH-04, AU-05, AU-06, AU-07, AU-11, AU-12, AU-13, AB-01, AB-02, AB-03, AB-04, AB-05, AB-06, AB-07, AB-08 | CL-08 | SEC-E3.5 (was E-AU3), CR-E4 |
````

**J306** · G2 · move

````text
| **B1** | PQ-S-03 | PV-01, PV-02, PV-03, PV-04, CM-01, CM-02 | SEC-Z0.5 (was E-CL1) |
````

**J307** · G2 · move

````text
| **B5** | AU-14, CL-01, CL-02, CL-03, CL-04, CL-05 | CL-06 | SEC-E3.1 (was E-CL3) |
````

**J308** · G2 · move

````text
| **C1** | CK-01, CK-02, CK-04, WL-01 | — | SEC-E6.5 (was E-CK1) |
````

**J309** · G2 · move

````text
| **C2** | CK-03, CK-05, CK-06 | — | SEC-E6.8 (was E-CK2) |
````

**J310** · G2 · move

````text
| **V-NET** | WA-11 (Armor), CL-07 | AB-01 (Armor, Lens-3), AB-02 (Armor, Lens-3), AB-03 (Armor, Lens-3), AB-04 (Armor, Lens-3), AB-05 (Armor, Lens-3) | SEC-E4.3 (was E-AB1) |
````

**J311** · G2 · move

````text
| **Phase 4 Networking** | DOS-04 (Prop Lock) | — | SEC-E4.16 (was E-DD2) |
````

**J312** · G2 · move

````text
| **Cloud Network Engineer cert track** | NT-*, DOS-*, A5 recall | — | SEC-E10.7 (was E-NT3) |
````

**J313** · G3 · anchor-rewrite

````text
> **Refactor note (2026-09-24, §7):** the suite-wide register is `Curriculum` §0.3; this table is the security slice of it, and on a conflict §0.3 wins.
````

**J314** · G5 · anchor-rewrite

````text
- `Curriculum` IDs: module IDs (`A5`, `A7`, `A10`, `B1`, `B5`, `C1`, `C2` …), Part V category IDs (`V-NET`, `V-SEC` …), `Phase 4 Networking` / `Phase 4 Security`, the reserved tracks (`M`, `U`, `S`), and cert names (PCA, Cloud Security Engineer, …). `Nx.y` = a section of `northstar-reference-app.md`; it carries the old parent's number and meaning (C-03). The old pseudo-anchors (`Phase4-Sec.n`, `A5/Phase4-Net.n`, `A10/B5.n`) are gone (C-10).
````

**J315** · G5 · anchor-rewrite

````text
*Generated from the §6.2 crosswalk (2026-09-24; C-11, C-12, C-13, C-14, C-15).* Every concept module appears once as primary; secondary anchors are previews, recalls or Lens-3 passes. The nine old checkpoint IDs that were never defined (shown below as 'was E-…') are mapped to existing cards by content (`crosswalk.md` §3; `[resolved-by-default]`). VPC-SC is NT-06 (C-12). The pre-refactor table is kept in the D3 archive.
````

**J316** · G5 · anchor-rewrite

````text
| **A5** | PQ-S-04 (HTTP/TLS (preview)), CR-11 (TLS), CR-12 (TLS), DOS-01 (load balancing), DOS-02 (DNS/UDP), NT-01 (NAT/firewalls/proxies), NT-02 (NAT/firewalls/proxies), NT-07 (NAT/firewalls/proxies), NT-03 (DNS), NT-04 (DNS), NT-05 (VPN), NT-08 (TLS) — CR-11/CR-12 at mechanism level plus the minimal public-key intuition bridge (C-14) | AU-01 (HTTP cookie mechanics (recall)), AU-02 (HTTP cookie mechanics (recall)), AU-03 (HTTP cookie mechanics (recall)), AU-04 (HTTP cookie mechanics (recall)), DOS-05 (HTTP (recall)) | SEC-E4.21, CR-E12 |
````

**J317** · G5 · anchor-rewrite

````text
| **A10** | PQ-S-01 (gate for CR-01), PQ-S-02, PQ-S-05, PQ-S-06, TH-01, TH-02, TH-03, CR-01, CR-02, CR-03, CR-04, CR-05, CR-06, CR-07, CR-08, CR-09, CR-10, CR-13, CR-19, CR-16, AU-01, AU-02, AU-03, AU-04, AU-08 (MFA), AU-09 (MFA), AU-10 (MFA), DOS-03, DOS-05, WA-01, WA-02, WA-03, WA-04, WA-06, WA-07, WA-08, WA-12, WA-05, SC-01 — formalizes the A5 bridge in one recall line (C-14) | PQ-S-04, TH-04, CR-11, CR-12, AU-05 (federation/SSO), AU-06 (federation/SSO), AU-07 (federation/SSO), AU-11, AU-12, AU-13, WA-10, PV-05 | CR-E1…CR-E8, SEC-Z0.* |
````

**J318** · G5 · anchor-rewrite

````text
*Generated from the §6.2 crosswalk (2026-09-24; C-11, C-12, C-13, C-14, C-15).* Every concept module appears once as primary; secondary anchors are previews, recalls or Lens-3 passes. The nine old checkpoint IDs that were never defined (shown below as 'was E-…') are mapped to existing cards by content (`crosswalk.md` §3; `[resolved-by-default]`). VPC-SC is NT-06. The pre-refactor table is kept in the D3 archive.
````

**J319** · G5 · anchor-rewrite

````text
| TLS handshake vocabulary | `Curriculum` A5 (mechanics) / A10 (formal; C-21) | CR-12 attacks, 0-RTT, validation bugs |
````

**J320** · G9 · anchor-rewrite

````text
### 0.6 Learner teaching preferences (binding; copied unchanged from session-progress-ledger.md §5, invariant 4)
````

**J321** · G9 · anchor-rewrite

````text
- When companion-file content (system-design-primer, SQL, design-patterns) overlaps a `Curriculum` module, **teach it once, stitched into the same session** — never as a separate pass, per each companion's own §0.2 stitching rules.
````

**J322** · G9 · anchor-rewrite

````text
- If a companion file references module IDs that don't exist in `Curriculum` (as `sql-databases-companion.md` does), **say so plainly rather than forcing a silent, possibly-wrong mapping** — this was well received when done for the SQL companion.
````

**J323** · G10 · anchor-rewrite

````text
> **Note:** the suite-wide register is `Curriculum` §0.3; this table is the security slice of it, and on a conflict §0.3 wins.
````

**J324** · G8 · anchor-rewrite

````text
#### PQ-S-03 · Shared responsibility matrices (IaaS/PaaS/SaaS/serverless) — stitch: B1 · N7.1 · XACS235
````

**J325** · G8 · anchor-rewrite

````text
#### TH-01 · Attacker models: web vs network vs cloud-admin vs co-tenant — stitch: A10 · S6 · N0.4 · CS155
````

**J326** · G8 · anchor-rewrite

````text
#### TH-03 · STRIDE applied — stitch: A10 · S6 · N7.4
````

**J327** · G8 · anchor-rewrite

````text
#### TH-04 · Attack trees & abuse cases as tests — stitch: A7 · A10 · N3.0 · N4.7
````

**J328** · G8 · anchor-rewrite

````text
#### TH-06 · Distributed-system threat concepts — stitch: A9 · N8 · primer
````

**J329** · G8 · anchor-rewrite

````text
#### CR-07 · Randomness: CSPRNG, entropy, nonce/IV; cloud RNG pitfalls — stitch: A10 · N1.2 · CS255
````

**J330** · G8 · anchor-rewrite

````text
#### CR-10 · Signatures: RSA-PSS, ECDSA, Ed25519; malleability; agility attacks — stitch: A10 · N4.5 · N7.5 · CS255
````

**J331** · G8 · anchor-rewrite

````text
#### CR-12 · TLS 1.2 vs 1.3: handshake, 0-RTT, validation bugs, HSTS — stitch: A5 TLS · A10 · N6.13 · CS255
````

**J332** · G8 · anchor-rewrite

````text
#### CR-14 · Key management: hierarchy, envelope, rotation, SoD; KMS/HSM/EKM/CMEK/CSEK — stitch: Phase 4 Security · N7.x
````

**J333** · G8 · anchor-rewrite

````text
#### CR-15 · Key compromise & crypto agility; IR for leaked keys — stitch: Phase 4 Security · N7.x · IR-05
````

**J334** · G8 · anchor-rewrite

````text
#### CR-17 · Secure channels beyond TLS: mTLS, app AEAD, field-level encryption — stitch: Phase 4 Security · N7.x · N4.8
````

**J335** · G8 · anchor-rewrite

````text
#### CR-18 · Privacy-enhancing crypto survey: TEEs, MPC, HE, ZKP awareness — stitch: Phase 4 Security · N7.x · N9c · XACS235 · SC-03
````

**J336** · G8 · anchor-rewrite

````text
#### CR-20 · Crypto engineering checklist for the reference cloud app — stitch: Phase 4 Security · N7.x · N7.3 · all CR
````

**J337** · G8 · anchor-rewrite

````text
#### AU-08 · Credential stuffing & password spraying — stitch: A10 (MFA) · N4.10
````

**J338** · G8 · anchor-rewrite

````text
#### AB-01 · Rate-limit algorithms: token bucket, sliding window, leaky bucket — stitch: A7 · V-NET (Armor, Lens-3) · N4.10
````

**J339** · G8 · anchor-rewrite

````text
#### AB-02 · Where to place limits (edge vs gateway vs app) — stitch: A7 · V-NET (Armor, Lens-3) · N6.13
````

**J340** · G8 · anchor-rewrite

````text
#### AB-04 · GraphQL complexity & batching abuse — stitch: A7 · V-NET (Armor, Lens-3) · N3.x
````

**J341** · G8 · anchor-rewrite

````text
#### AB-05 · Pagination & enumeration abuse — stitch: A7 · V-NET (Armor, Lens-3) · N8.1
````

**J342** · G8 · anchor-rewrite

````text
#### AB-06 · Business-logic abuse — stitch: A7 · B4 · N5.x · N3.0
````

**J343** · G8 · anchor-rewrite

````text
#### AB-07 · Inventory hoarding & checkout abuse — stitch: A7 · B4 · N5 · AB-03
````

**J344** · G8 · anchor-rewrite

````text
#### AB-08 · Export & expensive fan-out abuse — stitch: A7 · B4 · N9b · N4.10
````

**J345** · G8 · anchor-rewrite

````text
#### DOS-03 · L7 application floods — stitch: A10 · N6.16
````

**J346** · G8 · anchor-rewrite

````text
#### DOS-05 · Slowloris / slow-POST / slow-read — stitch: A10 · A5 HTTP (recall) · N6.13
````

**J347** · G8 · anchor-rewrite

````text
#### DOS-06 · Resource exhaustion (CPU/mem/conn/disk) — stitch: A6 · N8 · N4.2
````

**J348** · G8 · anchor-rewrite

````text
#### DOS-07 · Economic DoS (cloud bill) — stitch: B4 · N10.3 · FinOps
````

**J349** · G8 · anchor-rewrite

````text
#### DOS-08 · Cache stampedes & thundering herds — stitch: A9 · SD-26 (recall) · N8 · N9.1
````

**J350** · G8 · anchor-rewrite

````text
#### WA-05 · Injection: SQLi, command, path traversal — stitch: A10 · A8 (SQL SL-13 owns the SQL mechanics) · N7.4
````

**J351** · G8 · anchor-rewrite

````text
#### WA-08 · Open redirect & header injection — stitch: A10 · N4.2
````

**J352** · G8 · anchor-rewrite

````text
#### WA-09 · Log injection & forensic pollution — stitch: C6 · N10 · IR-01
````

**J353** · G8 · anchor-rewrite

````text
#### WA-11 · WAF rule craft & bypass attempts — stitch: V-NET (Armor) · N6.16 · Armor
````

**J354** · G8 · anchor-rewrite

````text
#### CL-01 · SSRF → metadata / IMDS (ATT&CK T1552.005) — stitch: B5 · Phase 4 Security (Lens-3) · N7.4
````

**J355** · G8 · anchor-rewrite

````text
#### CL-02 · Public buckets & object ACL mistakes — stitch: B5 · Phase 4 Security (Lens-3) · N7.7
````

**J356** · G8 · anchor-rewrite

````text
#### CL-03 · IAM privilege escalation paths — stitch: B5 · Phase 4 Security (Lens-3) · N7.2
````

**J357** · G8 · anchor-rewrite

````text
#### CL-04 · Service account key theft & sprawl — stitch: B5 · Phase 4 Security (Lens-3) · N7.8
````

**J358** · G8 · anchor-rewrite

````text
#### CL-05 · Confused deputy in cloud APIs — stitch: B5 · Phase 4 Security (Lens-3) · N4.8 · AU-14
````

**J359** · G8 · anchor-rewrite

````text
#### CL-06 · Tenant isolation failures — stitch: A9 · B5 · N8.1
````

**J360** · G8 · anchor-rewrite

````text
#### CL-08 · Serverless event injection & hypervisor escape awareness — stitch: B2 · A7 · N3.4 · XACS235
````

**J361** · G8 · anchor-rewrite

````text
#### NT-01 · Perimeter myths ('inside VPC = safe') — stitch: A5 NAT/firewalls/proxies · N7.1
````

**J362** · G8 · anchor-rewrite

````text
#### NT-02 · Lateral movement — stitch: A5 NAT/firewalls/proxies · N7.6
````

**J363** · G8 · anchor-rewrite

````text
#### NT-03 · Egress exfil & DNS tunneling — stitch: A5 DNS · N6.16
````

**J364** · G8 · anchor-rewrite

````text
#### CK-01 · Container escape patterns (awareness) — stitch: C1 · B2 · N7.5
````

**J365** · G8 · anchor-rewrite

````text
#### CK-02 · Privileged pods & hostPath — stitch: C1 · B2 · N9.2
````

**J366** · G8 · anchor-rewrite

````text
#### CK-03 · K8s RBAC wildcards — stitch: C2 · N9.2 · N7.2
````

**J367** · G8 · anchor-rewrite

````text
#### CK-04 · Secrets in etcd / env / images — stitch: C1 · B2 · N4.9
````

**J368** · G8 · anchor-rewrite

````text
#### CK-06 · NetworkPolicy & service mesh mTLS lite — stitch: C2 · N9.2
````

**J369** · G8 · anchor-rewrite

````text
#### WL-05 · Secret sprawl in repos/images/logs/prompts — stitch: C4 · A11 · N9c
````

**J370** · G8 · anchor-rewrite

````text
#### IR-01 · Log gaps & trail integrity — stitch: C6 · Phase 4 Security (SecOps) · N10.0
````

**J371** · G8 · anchor-rewrite

````text
#### IR-04 · Detection engineering for cloud TTPs — stitch: C6 · Phase 4 Security (SecOps) · N7.6 · TH-05
````

**J372** · G8 · anchor-rewrite

````text
#### IR-07 · Ransomware / backup integrity (cloud) — stitch: C7 · Phase 4 Security · N2.3
````

**J373** · G8 · anchor-rewrite

````text
#### AI-01 · Prompt injection (direct & indirect) — stitch: D4 · N9c · OWASP LLM
````

**J374** · G8 · anchor-rewrite

````text
#### AI-02 · Tool / agent abuse — stitch: D4 · N9c
````

**J375** · G8 · anchor-rewrite

````text
#### AI-03 · RAG data leakage — stitch: D4 · N9c.2 · PV-02
````

**J376** · G8 · anchor-rewrite

````text
#### AI-04 · Model / data poisoning & supply chain — stitch: D4 · N9c · WL
````

**J377** · G8 · anchor-rewrite

````text
#### AI-05 · Shadow AI & sensitive paste — stitch: D4 · N9c · PV
````

**J378** · G8 · anchor-rewrite

````text
#### SC-02 · Noisy neighbor & isolation classes — stitch: B2 · N8 · CMU 95-746
````

**J379** · G8 · anchor-rewrite

````text
#### SC-03 · Confidential Computing threat model — stitch: Phase 4 Security · N7.3 · CR-18
````

**J380** · G8 · anchor-rewrite

````text
#### PV-01 · Data classification & handling — stitch: Phase 4 Security · B1 · N7.9
````

**J381** · G8 · anchor-rewrite

````text
#### PV-02 · DLP / tokenization before analytics & prompts — stitch: Phase 4 Security · B1 · N9c
````

**J382** · G8 · anchor-rewrite

````text
#### PV-03 · Tokenization vs encryption — stitch: Phase 4 Security · B1 · N5 · CR-17
````

**J383** · G8 · anchor-rewrite

````text
#### PV-04 · Residency & sovereignty controls — stitch: Phase 4 Security · B1 · N6.15
````

**J384** · G8 · anchor-rewrite

````text
#### PV-05 · Privacy vs security tension (short Embedded EthiCS angle) — stitch: U7 · A10 · N7.9 · XACS235
````

**J385** · G8 · anchor-rewrite

````text
#### CM-02 · PCI / HIPAA / SOC2 / FedRAMP idea → control map — stitch: Phase 4 Security · B1 · N5
````

**J630** · SEC-1 · anchor-rewrite

````text
**Companion to [`Curriculum`](./Curriculum.md)** (the cloud mastery / certification roadmap).
````

**J631** · SEC-1 · anchor-rewrite

````text
When other companions bind to the same session, the Suite Session Protocol in `Curriculum` §0.4 governs.
````

**J632** · SEC-2 · anchor-rewrite

````text
- `Curriculum` IDs: module IDs (`A5`, `A7`, `A10`, `B1`, `B5`, `C1`, `C2` …), Part V category IDs (`V-NET`, `V-SEC` …), `Phase 4 Networking` / `Phase 4 Security`, the reserved tracks (`M`, `U`, `S`), and cert names (PCA, Cloud Security Engineer, …). `Nx.y` = a section of `northstar-reference-app.md`; it carries the old parent's number and meaning. The old pseudo-anchors (`Phase4-Sec.n`, `A5/Phase4-Net.n`, `A10/B5.n`) are gone.
````

**J633** · SEC-3 · anchor-rewrite

````text
| CCM domain | Companion homes | the reference cloud app evidence sketch |
````

**J634** · SEC-3 · anchor-rewrite

````text
- **Lab:** SEC-Z0.3: map each Saltzer principle to one the reference cloud app control.
````

**J635** · SEC-3 · anchor-rewrite

````text
- **Lab:** SEC-E1.3: one the reference cloud app ADR that prices a control vs accept risk.
````

**J636** · SEC-3 · anchor-rewrite

````text
- **Check:** List five the reference cloud app assets and their trust boundary.
````

**J637** · SEC-3 · anchor-rewrite

````text
- **Lab:** CR-E1: for three the reference cloud app fields, name goal + required game.
````

**J638** · SEC-3 · anchor-rewrite

````text
- **Check:** Name five CCM domains and one the reference cloud app control each.
````

**J639** · SEC-3 · anchor-rewrite

````text
- **Scenario:** Five the reference cloud app controls listed.
````

**J640** · SEC-3 · anchor-rewrite

````text
- **Check:** Give a the reference cloud app Elevation example that HTTPS does not stop.
````

**J641** · SEC-3 · anchor-rewrite

````text
- **Check:** Name an expensive the reference cloud app endpoint to protect first.
````

**J642** · SEC-3 · anchor-rewrite

````text
- **Scenario:** Standing global HTTPS LB+Armor vs Hosting+Run for early the reference cloud app.
````

**J643** · SEC-3 · anchor-rewrite

````text
- **GCP lens:** Lens-1: resource hierarchy. Lens-2: annotate existing the reference cloud app HLD.
````

**J644** · SEC-3 · anchor-rewrite

````text
- **Scenario:** Marketing site on `www` sets cookie Domain=.the reference cloud app.example.
````

**J645** · SEC-3 · anchor-rewrite

````text
#### SEC-E1.1 · L1 · the reference cloud app STRIDE one-pager
````

**J646** · SEC-3 · anchor-rewrite

````text
### SEC-CAP1 · the reference cloud app hardening pass
````

**J647** · SEC-3 · anchor-rewrite

````text
Victim API decrypts CBC and returns HTTP 400 "bad padding" vs 403 "bad mac". Attacker flips bits in ciphertext block \(C_i\) and observes which error returns. Over many queries they recover plaintext bytes (Vaudenay). **Teaching move:** derive why *integrity first* (AEAD or EtM) collapses the oracle; connect to CR-03 lab card CR-E3. **the reference cloud app link:** never expose distinct crypto error classes on legacy token decrypt paths.
````

**J648** · SEC-3 · anchor-rewrite

````text
#### SEC-E3.9 · L3 · OWASP map the reference cloud app
````

**J649** · SEC-3 · anchor-rewrite

````text
- **Defense pattern:** Map the reference cloud app detections to a few techniques; do not boil the ocean.
````

**J650** · SEC-3 · anchor-rewrite

````text
- **GCP lens:** Lens-1: watch Google Cloud PQ/TLS announcements (verify). Lens-2: inventory the reference cloud app keys by lifetime.
````

**J651** · SEC-3 · anchor-rewrite

````text
- **Check:** Recite eight non-negotiables for the reference cloud app crypto.
````

**J652** · SEC-3 · anchor-rewrite

````text
- **Check:** Give a BFLA example on the reference cloud app admin.
````

**J653** · SEC-3 · anchor-rewrite

````text
- **GCP lens:** Lens-1: N6.11 map. Lens-2: redraw the reference cloud app path.
````

**J654** · SEC-3 · anchor-rewrite

````text
- **GCP lens:** Lens-1: SDP infoTypes; resource labels. Lens-2: classify the reference cloud app fields.
````

**J655** · SEC-3 · anchor-rewrite

````text
- **Predict impact (write first):** Map A01–A05 to the reference cloud app controls.
````

**J656** · SEC-3 · anchor-rewrite

````text
- **Scenario:** the reference cloud app controls known.
````

**J657** · SEC-3 · anchor-rewrite

````text
- **Scenario:** the reference cloud app crypto ADR blank.
````

**J658** · SEC-3 · anchor-rewrite

````text
Use as a *gap finder*, not a dump. Mark the reference cloud app evidence paths.
````

**J659** · SEC-3 · anchor-rewrite

````text
10. **Line-count / completeness note:** This companion prioritizes stitchable attack+crypto depth over encyclopedic CCM dumps; use §8 as a gap finder when auditing the reference cloud app evidence.
````

**J660** · SEC-3 · anchor-rewrite

````text
- **Scenario:** the reference cloud app has IAM deny, parameterized SQL, IAP admin, org policy default deny public buckets.
````

**J661** · SEC-3 · anchor-rewrite

````text
- **Scenario:** the reference app's controls known.
````

**J662** · SEC-3 · anchor-rewrite

````text
- **Scenario:** the reference app's crypto ADR blank.
````

**J663** · SEC-3 · anchor-rewrite

````text
- **GCP lens:** Lens-1: the reference cloud app ledger invariants (N5.3). Lens-2: race test.
````

**J664** · SEC-3 · anchor-rewrite

````text
9. **Built** 2026-09-22 for the reference cloud app / `Curriculum` pairing.
````

**J665** · SEC-3 · anchor-rewrite

````text
#### TH-02 · Trust boundaries & asset inventory for the reference cloud app — stitch: A10 · S6
````

**J666** · SEC-3 · anchor-rewrite

````text
#### CR-20 · Crypto engineering checklist for the reference cloud app — stitch: Phase 4 Security · all CR
````

**J667** · SEC-3 · anchor-rewrite

````text
- **GCP lens:** Lens-1: ADR linking checklist to Secret Manager/KMS/Armor TLS. Lens-2: audit the reference cloud app against checklist.
````

**J668** · SEC-3 · anchor-rewrite

````text
**Skip-test for CR track (SEC-T1+SEC-T2 in §4):** learner must, unaided: (1) state IND-CPA vs integrity goals with one example each; (2) explain why ECB and raw RSA fail; (3) give GCM nonce-reuse consequence; (4) prefer AEAD over CBC+HMAC DIY; (5) sketch envelope KEK/DEK with KMS; (6) name TLS 1.3 0-RTT risk; (7) justify Argon2id over SHA-256 for passwords; (8) list eight CR-20 checklist items for the reference cloud app.
````

**J669** · SEC-3 · anchor-rewrite

````text
- **Defense pattern:** Map the reference cloud app to subset: IAM, EKM/CEK, LOG, IVS, TVM, AIS, SEF — evidence paths.
````

**J670** · SEC-3 · anchor-rewrite

````text
- **Scenario:** Cloud Run + Cloud SQL + GCS for the reference cloud app.
````

**J671** · SEC-4 · anchor-rewrite

````text
*Generated from the §6.2 crosswalk (2026-09-24).* Every concept module appears once as primary; secondary anchors are previews, recalls or Lens-3 passes. The nine old checkpoint IDs that were never defined (shown below as 'was E-…') are mapped to existing cards by content (`crosswalk.md` §3; `[resolved-by-default]`). VPC-SC is NT-06. The pre-refactor table is kept in the D3 archive.
````

**J672** · SEC-4 · anchor-rewrite

````text
| `Curriculum` anchor | Taught here (primary, §6.2) | Also in this session (secondary) | Checkpoint |
````

**J673** · SEC-14 · anchor-rewrite

````text
| Main-course anchor | Taught here (primary, §6.2) | Also in this session (secondary) | Checkpoint |
````

**J674** · SEC-5 · anchor-rewrite

````text
*Equal scale to AU/AB/CL. `Curriculum` A7 (API auth patterns) + A10 own password/JWT *product* labs; Phase 4 Security (N7.3) owns the CMEK *product* spine; CR owns cryptographic justification and failure modes. Stanford CS255 alignment: see §0.5.*
````

**J675** · SEC-5 · anchor-rewrite

````text
- **GCP lens:** Lens-1: signed requests in N4.5 use HMAC — recall roadmap lab; CR adds composition rules.
````

**J676** · SEC-5 · anchor-rewrite

````text
- **Defense pattern:** *Roadmap N4.3 owns product labs.* CR adds: threat model (online vs offline), parameter tuning rationale, pepper in KMS, migration/version field.
````

**J677** · SEC-5 · anchor-rewrite

````text
- **GCP lens:** Lens-1: pepper in Secret Manager/KMS. Lens-2: recall N4.3 Argon2id lab — add threat-model paragraph.
````

**J678** · SEC-5 · anchor-rewrite

````text
- **Defense pattern:** *N7.3 owns CMEK lab.* CR adds: hierarchy diagram, rewrap vs re-encrypt, key purpose separation, when CMEK vs CSEK vs Google-managed.
````

**J679** · SEC-5 · anchor-rewrite

````text
- **GCP lens:** Lens-1: Cloud KMS key ring/key; CMEK on GCS/SQL (verify); Cloud HSM/EKM literacy. Lens-2: local envelope toy from N7.3 + hierarchy labels.
````

**J680** · SEC-5 · anchor-rewrite

````text
**Prop Lock for crypto props:** do not use Cloud HSM, EKM, Confidential Space, or Binary Authorization as assumed props before their Northstar sections (N7.3 / N7.5) and companion CR-14 / CR-18 / WL-04 are unlocked. Local AEAD/HMAC toys may use Tink without those props.
````

**J681** · SEC-5 · anchor-rewrite

````text
**Pairing rule with A7 (API auth patterns) + A10 & N7.3:** A7 (API auth patterns) + A10 own password *product* labs and JWT *policy* labs; CR-13/CR-10 own the cryptographic *why* and failure modes. Phase 4 Security (N7.3) owns CMEK *clickpath*; CR-14 owns hierarchy theory and SoD. Teach as one story per §2 stitch rows.
````

**J682** · SEC-5 · anchor-rewrite

````text
3. CR-05…07 + CR-13 at A10 (password/KDF day; the A7 API-auth product labs are recalled, N4.3).
````

**J683** · SEC-5 · anchor-rewrite

````text
5. CR-14…15 + CR-20 at Phase 4 Security (KMS + key IR; N7.8).
````

**J684** · SEC-5 · anchor-rewrite

````text
6. CR-16 at A10; CR-17…18 at Phase 4 Security, with Confidential Computing literacy + N9c privacy (survey depth).
````

**J685** · SEC-5 · anchor-rewrite

````text
Object bytes encrypted with DEK_AES-GCM; DEK wrapped by KMS KEK; metadata stores wrapped DEK + key version. Compromise of object store without `cloudkms.cryptoKeyEncrypterDecrypter` yields ciphertext only. **Teaching move:** draw trust boundary between storage IAM and KMS IAM; SoD. Cards CR-E9/E10/E34. Roadmap N7.3 owns the product clickpath.
````

**J686** · SEC-5 · anchor-rewrite

````text
SHA-256(password) at \(10^9\) guesses/s/GPU vs Argon2id ~64MB ~100 ms. Show order-of-magnitude table; salt kills rainbows; pepper in KMS raises bar after DB leak. Roadmap N4.3 owns implementation; CR-13 owns the math story. Card CR-E8.
````

**J687** · SEC-6 · anchor-rewrite

````text
- **GCP lens:** Lens-1: Cloud Run vs GCE vs GCS rows. Lens-2: annotate N0 hierarchy with trust boundaries.
````

**J688** · SEC-6 · anchor-rewrite

````text
- **GCP lens:** Lens-1: app middleware (N4.4 lab). Lens-2: forged Origin test.
````

**J689** · SEC-6 · anchor-rewrite

````text
- **GCP lens:** Lens-1: app PEP; IAP is not object AuthZ. Lens-2: IDOR fail-then-pass (N4.7).
````

**J690** · SEC-6 · anchor-rewrite

````text
- **GCP lens:** Lens-1: recall N8.1 cursor pager — add abuse tests.
````

**J691** · SEC-6 · anchor-rewrite

````text
- **GCP lens:** Lens-1: Cloud Run request timeout + `http.Server` timeouts (N4.2). Lens-2: slowloris against *local* fixture only.
````

**J692** · SEC-6 · anchor-rewrite

````text
- **GCP lens:** Lens-1: Cloud Run CORS middleware. Lens-2: hostile Origin tests (N4.4).
````

**J693** · SEC-6 · anchor-rewrite

````text
- **GCP lens:** Lens-1: GCE metadata server; Cloud Run identity. Lens-2: local SSRF fixture + guard tests (N4.2).
````

**J694** · SEC-6 · anchor-rewrite

````text
- **GCP lens:** Lens-1: org policy `storage.publicAccessPrevention` (verify). Lens-2: paper IR for public ACE (N7.8).
````

**J695** · SEC-6 · anchor-rewrite

````text
- **GCP lens:** Lens-1: N6.11 map. Lens-2: redraw the reference app's path.
````

**J696** · SEC-6 · anchor-rewrite

````text
- **GCP lens:** Lens-1: Binary Authorization + Artifact Registry. Lens-2: recall N7.5 lab analytic layer.
````

**J697** · SEC-6 · anchor-rewrite

````text
- **GCP lens:** Lens-1: Binary Authorization API. Lens-2: N7.5 toy attestation analytic.
````

**J698** · SEC-6 · anchor-rewrite

````text
- **GCP lens:** Lens-1: SCC findings + log-based metrics. Lens-2: wire one alert to N7.6 template.
````

**J699** · SEC-6 · anchor-rewrite

````text
- **Defense pattern:** Disable SA/keys → hunt audit → rotate workloads → rewrap secrets → postmortem. Use roadmap N7.8 template; CR-15 for crypto keys.
````

**J700** · SEC-6 · anchor-rewrite

````text
- **Defense pattern:** PAN: tokenize (N5); secrets: Secret Manager; fields: AEAD when needed.
````

**J701** · SEC-6 · anchor-rewrite

````text
- **GCP lens:** Lens-1: PCI themes N5 + SDP. Lens-2: decision table.
````

**J702** · SEC-6 · anchor-rewrite

````text
- **GCP lens:** Lens-1: Well-Architected + CCM crosswalk lite. Lens-2: gap spreadsheet.
````

**J703** · SEC-6 · anchor-rewrite

````text
Skip a companion family only by passing its skip-test. `Curriculum` and Northstar still own product labs — skipping companion theory does not skip Armor attach / IAP / CMEK product evidence.
````

**J713** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** A5 TLS / N6.11 path
````

**J714** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** N7.1 recall + PQ-S-02
````

**J715** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** N0.4 HLD
````

**J716** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** N0.4
````

**J717** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** N6.14
````

**J718** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** N4.4
````

**J719** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** N4.4
````

**J720** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** N7.4
````

**J721** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CR-14, N7.3 toy
````

**J722** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** N3.0, AB-06
````

**J723** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** WA-01, N4.4
````

**J724** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CL-01, N4.2
````

**J725** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** AU-08, AB-03, N4.10
````

**J726** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** AU-11, N4.7
````

**J727** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** DOS-05, N4.2
````

**J728** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** AB-02, N4.10
````

**J729** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** N6.11, NT-07
````

**J730** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CR-12, N6.13
````

**J731** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** AB-03, N4.10
````

**J732** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** NT-04, N6.16
````

**J733** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CL-03, N7.2
````

**J734** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CL-04, IR-05, N7.8
````

**J735** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** NT-02, N6.12
````

**J736** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** NT-05, N6.14
````

**J737** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** NT-06, N6.15
````

**J738** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** PV-01, N7.3
````

**J739** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** WL-04, CK-05, N7.5
````

**J740** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** PV-03, N5
````

**J741** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** IR-05, N7.8
````

**J742** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** DOS-07, N10.3
````

**J743** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CM-01, N7.9
````

**J744** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** AI-01, AI-02, N9c
````

**J745** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CR-13, N4.3
````

**J746** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CR-14, N7.3
````

**J747** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CR-14, N7.3
````

**J748** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** AB-02, DOS-03, N4.10, N6.16
````

**J749** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CL-04, IR-05, N4.8, N7.8
````

**J750** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** AU-03, AU-04, N4.4
````

**J751** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** WL-04, CK-05, N7.5
````

**J752** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** IR-01, N7.6, N10
````

**J753** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** AI-01, AI-03, PV-02, N9c
````

**J754** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CL-02, PV-01, N7.3, N7.7
````

**J755** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** AB-04, N4.10
````

**J756** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** AU-06, N4.6
````

**J757** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CR-14, CR-15, N7.3
````

**J758** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CR-13, N4.3, N4.9
````

**J759** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** PQ-S-03, N2.3
````

**J760** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CL-01, CL-02, NT-06, N4.2, N6.15
````

**J761** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** WL-01, WL-04, CK-05, N7.5
````

**J762** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** WA-05, WA-11, N7.4
````

**J763** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** IR-03, CR-15, N7.8
````

**J764** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** AI-01, AI-02, N9c
````

**J765** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** AU-05, CR-10, N4.5
````

**J766** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CL-07, NT-02, N6.15
````

**J767** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** DOS-07, AB-01, N10.3
````

**J768** · SEC-7 · anchor-rewrite

````text
- **Design control:** Follow N7.8 public ACE runbook + evidence.
````

**J769** · SEC-7 · anchor-rewrite

````text
- **Design control:** Argon2id+salt+pepper plan (N4.3 owns lab).
````

**J770** · SEC-7 · anchor-rewrite

````text
- **Design control:** Fill N7.8 template; grade order.
````

**J771** · SEC-8 · anchor-rewrite

````text
- **Depends:** AU-*, WA-* core, AB-01/02, CL-01, CR-12/13/14/20, A7 (API auth patterns) + A10 + N7.3–N7.4.
````

**J772** · SEC-8 · anchor-rewrite

````text
- **Depends:** IR-*, CL-02/04, CR-15, roadmap N7.8 templates.
````

**J773** · SEC-8 · anchor-rewrite

````text
- **Depends:** AB-*, DOS-03/05/07, AU-08, N4.10, 6.16.
````

**J774** · SEC-8 · anchor-rewrite

````text
- **Depends:** AI-01…05, PV-02, CR-18 lite, 9c.
````

**J775** · SEC-8 · anchor-rewrite

````text
Run **SEC-CAP1** after A7 (API auth patterns) + A10 + CR-20 unlocked; **SEC-CAP2** after N7.8 + IR/CR-15; **SEC-CAP3** after N4.10 + N6.16 + AB/DOS; **SEC-CAP4** after N9c + AI-*. Never schedule a capstone that smuggles a locked prop — postpone or unlock first (Prop Lock).
````

**J776** · SEC-8 · anchor-rewrite

````text
3. **Prop Lock examples:** no VPC-SC before N6.15; no BinAuth before N7.5; no Confidential VM as assumed before CR-18/SC-03.
````

**J777** · SEC-8 · anchor-rewrite

````text
8. **SCC green ≠ secure:** pair N7.6 with IR-02 alert design on day one of detection.
````

**J778** · SEC-9 · anchor-rewrite

````text
| IAM | CL-03, AU-*, B5 / N7.2 | Least privilege bindings |
````

**J779** · SEC-9 · anchor-rewrite

````text
| GRC | CM-01, N7.9 | ADRs, risk register |
````

**J780** · SEC-9 · anchor-rewrite

````text
| A&A | CM-02, N7.9 | Control matrix |
````

**J781** · SEC-9 · anchor-rewrite

````text
| UEM | NT-05, N6.14 | IAP device signals literacy |
````

**J782** · SEC-9 · anchor-rewrite

````text
| EKM / CEK | CR-14…15, N7.3 | KMS keys, CMEK |
````

**J783** · SEC-9 · anchor-rewrite

````text
| DSP | PV-02, N7.3 | SDP jobs |
````

**J784** · SEC-9 · anchor-rewrite

````text
| IVS | CK-*, WL-*, N7.5 | Hardened runtime |
````

**J785** · SEC-9 · anchor-rewrite

````text
| MSC | NT-*, N6.x | Network segmentation |
````

**J786** · SEC-9 · anchor-rewrite

````text
| Plane | Assets | Primary attackers | Top companion modules | Roadmap anchors |
````

**J787** · SEC-9 · anchor-rewrite

````text
| Storefront | Session, catalog, carts | Web attacker, bots | AU-01…04, WA-02, AB-03, DOS-03 | A5 TLS, N4.4, N4.10 |
````

**J788** · SEC-9 · anchor-rewrite

````text
| Customer API | Orders, PII, tokens | Web, stuffing, IDOR | AU-08, AU-11, WA-05, AB-01, CL-01 | N4.2–N4.7, N4.10 |
````

**J789** · SEC-9 · anchor-rewrite

````text
| Admin | Refunds, config | Stolen session, CSRF, BFLA | AU-03, AU-12, NT-05 | N4.4, N4.7, N6.14 |
````

**J790** · SEC-9 · anchor-rewrite

````text
| Service-to-service | SA identity, internal RPC | Confused deputy, key theft | AU-14, CL-04, CR-17 | N4.8, N7.2 |
````

**J791** · SEC-9 · anchor-rewrite

````text
| Data | SQL, GCS, BQ | Public ACE, SSRF→cred, insider | CL-02, CR-14, PV-*, NT-06 | N7.3, N6.15 |
````

**J792** · SEC-9 · anchor-rewrite

````text
| CI/CD | Build SA, images | Poisoned PR, unsigned deploy | WL-02, WL-04, CK-05 | N4.8, N7.5 |
````

**J793** · SEC-9 · anchor-rewrite

````text
| AI gateway | Tools, RAG corpus | Prompt injection, tool abuse | AI-01…05, PV-02 | N9c |
````

**J794** · SEC-9 · anchor-rewrite

````text
11. **When in doubt on a GCP SKU name:** prefer the `Curriculum` / Northstar product lab + live docs; companion scenarios stay valid even if a SKU renames.
````

**J795** · SEC-13 · anchor-rewrite

````text
- **Defense pattern:** Complete mediation; fail-safe defaults; economy of mechanism; least common mechanism; psychological acceptability — *recall* CIA/least-privilege/defense-in-depth/assume-breach/zero-trust/shared-responsibility from 7.1.
````

**J796** · SEC-13 · anchor-rewrite

````text
- **GCP lens:** Lens-1: Policy Analyzer / IAM recommender (verify). Lens-2: toy effective-access from 7.2.
````

**J797** · SEC-13 · anchor-rewrite

````text
- **GCP lens:** Lens-1: Cloud DNS DNSSEC; destroy-order checklist 6.16. Lens-2: paper only.
````

**J798** · SEC-13 · anchor-rewrite

````text
- **GCP lens:** Lens-1: IAP lab 6.14. Lens-2: compare threat tables.
````

**J799** · SEC-13 · anchor-rewrite

````text
- **GCP lens:** Lens-1: Cloud Build provenance (verify). Lens-2: cosign-shaped toy from 7.5.
````

**J800** · SEC-13 · anchor-rewrite

````text
**Prop Lock reminder:** passing SEC-T2 does not unlock VPC-SC props before 6.15.
````

**J801** · SEC-13 · anchor-rewrite

````text
- **Design control:** Redesign per 4.3+AU-10.
````

**J802** · SEC-13 · anchor-rewrite

````text
- **Design control:** Set timeout suite from 4.2.
````

**J803** · SEC-13 · anchor-rewrite

````text
| AIS | 3.0/4.x, WA-* | Secure SDLC tests |
````

**J804** · SEC-10 · anchor-rewrite

````text
- **Scenario:** GCE guest OS CVE; Cloud Run app SQLi; GCS public ACE; Google DC physical.
````

**J805** · SEC-10 · anchor-rewrite

````text
- **Scenario:** Docs skim (verify).
````

**J806** · SEC-10 · anchor-rewrite

````text
- **Scenario:** CNAME to deleted Cloud Run.
````

**J822** · SEC-12 · anchor-rewrite

````text
This file has **self-contained content**; ownership is shared per the suite overlap register (`Curriculum` §0.3). It covers **cloud security, cybersecurity, cryptography, and network security** for cloud infrastructure and cloud-hosted distributed systems — taught in parallel with the matching sections of `Curriculum`.
````

**J823** · SEC-12 · anchor-rewrite

````text
**Does not own:** non-security tracks in `Curriculum` (ML math, general DSA, FinOps deep-dives, non-security data modeling). Those stay in `Curriculum` only.
````

**J824** · SEC-12 · anchor-rewrite

````text
## 0. Read this first — how this file complements `Curriculum`
````

**J825** · SEC-12 · anchor-rewrite

````text
**This file is a complement to `Curriculum`, not a second roadmap. Read both. Whenever a security-relevant `Curriculum` section is taught, also teach every companion concept bound to it (§2) in the same session, as one story. Similar, related, and overlapping security concepts are stitched and taught in parallel — never in separate sessions, never twice.**
````

**J826** · SEC-12 · anchor-rewrite

````text
Why: `Curriculum` owns the *roadmap spine* — what to learn, in what order, tied to certs (PCA, Cloud Security Engineer, Network Engineer, SecOps, SCS-C03, etc.) and the provider service maps. It lists security topics at outline depth (A5 networking, A10 crypto/security fundamentals, B1 shared responsibility, B5 IAM model, Track C container/K8s hardening, Phase 4 GCP Security services). It does not own attacker playbooks, misuse cases, rate-limit/WAF craft, session/JWT/OAuth failure modes, supply-chain attacker paths, IR tabletop depth, AI threat mechanics, or a full applied-cryptography track. This file supplies those and hangs each piece on the `Curriculum` section that needs it **when that section is taught**.
````

**J827** · SEC-12 · anchor-rewrite

````text
2. **Ownership split.** *`Curriculum` owns:* learning order, cert mapping, service vocabulary (IAM, Armor, VPC-SC, KMS, SCC, SecOps), shared-responsibility framing at roadmap level. *This file owns:* attack mechanics, defensive design patterns, cryptography depth (`CR-*`), network-security attacks, exercise/scenario bank, IR tabletops.
````

**J828** · SEC-12 · anchor-rewrite

````text
3. **Same teaching discipline.** Issue **one** exercise at a time; learner attempts before keys; predict blast radius / control placement before revealing the answer. Prop Lock: do not use a later control (VPC-SC, Confidential VM, Binary Authorization) as a "known" prop before its `Curriculum` section has been covered (suite-wide rule: `Curriculum` §0.4.6) — postpone the exercise or teach the prerequisite first.
````

**J829** · SEC-12 · anchor-rewrite

````text
4. **GCP lens at three depths** when a concept is taught: **Lens-1** name the GCP (and AWS/Azure twin from `Curriculum` mapping tables) resource; **Lens-2** touch via local vulnerable-by-design fixture or credits-safe lab; **Lens-3** cert-depth trade-offs (Cloud Security Engineer / PCA Security / SCS-C03).
````

**J830** · SEC-12 · anchor-rewrite

````text
11. **User can override** skip/jump. On conflict: `Curriculum` wins on order and cert timing; this file wins on security/crypto content and exercise specs.
````

**J831** · SEC-12 · anchor-rewrite

````text
1. **Anchor** — name the `Curriculum` section (e.g. A10, B5, Phase 4 Security) and list bound companion IDs from §2.
````

**J832** · SEC-12 · anchor-rewrite

````text
## 2. Stitch table — teach these with `Curriculum`
````

**J833** · SEC-12 · anchor-rewrite

````text
| **AWS Security Specialty / Azure SC-100 (later phases)** | same mechanics; map controls via `Curriculum` Part VIII tables — no new theory | — | IR mapping drill |
````

**J834** · SEC-12 · anchor-rewrite

````text
> **Note:** the suite-wide register is `Curriculum` §0.3; this table is the security slice of it, and on a conflict the main course's register wins.
````

**J835** · SEC-12 · anchor-rewrite

````text
| Shared responsibility one-liner | `Curriculum` B1 | PQ-S-03 matrices by service model |
````

**J836** · SEC-12 · anchor-rewrite

````text
| TLS handshake vocabulary | `Curriculum` A5 (mechanics) / A10 (formal) | CR-12 attacks, 0-RTT, validation bugs |
````

**J837** · SEC-12 · anchor-rewrite

````text
| IAM principals/roles | `Curriculum` B5 | CL IAM privesc / key sprawl playbooks |
````

**J838** · SEC-12 · anchor-rewrite

````text
| "Use KMS/CMEK" | `Curriculum` Phase 4 Security | CR-14 envelope hierarchy + compromise IR |
````

**J839** · SEC-12 · anchor-rewrite

````text
| Armor / DDoS product names | `Curriculum` V-NET / Phase 4 Networking | DOS taxonomy + rate-limit/bot design |
````

**J840** · SEC-12 · anchor-rewrite

````text
| Container non-root / PSS | `Curriculum` C1/C2 | CK escape & supply-chain attacker paths |
````

**J841** · SEC-12 · anchor-rewrite

````text
| OAuth/JWT mentioned | `Curriculum` A7 | AU/CR failure modes (alg confusion, mix-up) |
````

**J842** · SEC-12 · anchor-rewrite

````text
1. CR-11 + CR-12 on the `Curriculum` A5 TLS day, at mechanism level, with the minimal public-key intuition bridge (what a key pair does, what a signature proves, why DH gives a shared secret) — CR-E12.
````

**J843** · SEC-12 · anchor-rewrite

````text
*End of The Cloud Cybersecurity Companion. Stitch with `Curriculum`; bank ≠ dump; CR-* is a first-class pillar.*
````

**J847** · GO-13 · anchor-rewrite

````text
- **Build lab (hardened HTTP server):** on a Go `http.Server` set `ReadHeaderTimeout` 5 s, `ReadTimeout` 15 s, `WriteTimeout` 15 s, `IdleTimeout` 60 s and `MaxHeaderBytes` 1 MiB; wrap request bodies in `http.MaxBytesReader`; cap in-flight requests with a semaphore that answers 503 when full (the Python twin sets the same limits in its ASGI server `(verify)` the option names). Against a *local* copy only, run a slow-header client (200 connections, one header byte every 10 s) before and after: before, the workers fill; after, each connection closes at the header timeout. Write the Cloud Run request timeout and the load balancer's backend timeout beside the server values so the three agree.
````

**J848** · GO-14 · anchor-rewrite

````text
- **Build lab (password storage):** register and login endpoints on a local service. Store per user `argon2id$v=19$m=65536,t=3,p=1$<salt>$<hash>` from a vetted library (argon2-cffi, `golang.org/x/crypto/argon2`), with parameters from the current OWASP password-storage guidance `(verify)`, a unique 16-byte random salt per user, and a pepper: HMAC-SHA-256 of the password under a key held in Secret Manager (lab: an environment variable), applied before hashing, with a pepper-version field. Steps: (1) time one hash and tune memory and iterations to about 100 ms on the lab machine; (2) import a table of legacy SHA-256 hashes and upgrade each one on its next successful login (rehash-on-login, version field); (3) rate-limit login per account and per IP (AU-08). Tests: the same password gives different stored strings; a wrong pepper version fails closed; a login for an unknown user takes as long as for a known one (hash a dummy value).
````

**J912** · R4-10 · anchor-rewrite

````text
- Main-course IDs: module IDs (`A5`, `A7`, `A10`, `B1`, `B5`, `C1`, `C2` …), Part V category IDs (`V-NET`, `V-SEC` …), `Phase 4 Networking` / `Phase 4 Security`, the reserved tracks (`M`, `U`, `S`; scope stubs in the main course), and cert names (PCA, Cloud Security Engineer, …). IDs from the other companions keep their own prefixes and are named with their part, e.g. SQL DD-03, SQL OD-11.
````

**J913** · R4-10 · anchor-rewrite

````text
| **A6** | DOS-06, WA-10 (+ U1) | — | — |
````

**J914** · R4-10 · anchor-rewrite

````text
| **U7** | PV-05 | — | — |
````

**J915** · R4-10 · anchor-rewrite

````text
| **Phase 4 Security** | TH-05 (SecOps), CR-14, CR-15, CR-17, CR-18, CR-20, NT-06 (Prop Lock), WL-04, SC-03, PV-01, PV-02, PV-03, PV-04, CM-01, CM-02 | CL-01 (Lens-3), CL-02 (Lens-3), CL-03 (Lens-3), CL-04 (Lens-3), CL-05 (Lens-3), IR-01 (SecOps), IR-02 (SecOps), IR-04 (SecOps), IR-03, IR-05, IR-06, IR-07, IR-08 | CR-E9…CR-E15, SEC-CAP1 |
````

**J916** · R4-10 · anchor-rewrite

````text
#### TH-01 · Attacker models: web vs network vs cloud-admin vs co-tenant — stitch: A10 · S6 · S2 · CS155
````

**J917** · R4-10 · anchor-rewrite

````text
#### TH-02 · Trust boundaries & asset inventory for the reference app — stitch: A10 · S6
````

**J918** · R4-10 · anchor-rewrite

````text
#### TH-03 · STRIDE applied — stitch: A10 · S6 · Phase 4 Security
````

**J919** · R4-10 · anchor-rewrite

````text
#### TH-06 · Distributed-system threat concepts — stitch: A9 · S2 · primer
````

**J920** · R4-10 · anchor-rewrite

````text
#### DOS-06 · Resource exhaustion (CPU/mem/conn/disk) — stitch: A6 · S2 · A10
````

**J921** · R4-10 · anchor-rewrite

````text
#### DOS-08 · Cache stampedes & thundering herds — stitch: A9 · SD-26 (recall) · S2 · V-STOR
````

**J922** · R4-10 · anchor-rewrite

````text
#### WA-10 · Memory/control-flow → cloud RCE (applied) — stitch: A6 + U1 · A10 · CS155 · CK · GCE
````

**J923** · R4-10 · anchor-rewrite

````text
#### SC-02 · Noisy neighbor & isolation classes — stitch: B2 · S2 · CMU 95-746
````

**J924** · R4-10 · anchor-rewrite

````text
#### PV-05 · Privacy vs security tension (short Embedded EthiCS angle) — stitch: U7 · A10 · Phase 4 Security · XACS235
````

**J925** · R4-10 · anchor-rewrite

````text
- **Map to GCP:** DOS-08, architecture studios (security-relevant only)
````

**J1068** · R6-2 · new-content

````text
- **Defense pattern:** DNSSEC for authenticity; delete DNS with services; inventory dangling; RPKI literacy (conceptual).
````

**J1069** · R6-2 · new-content

````text
- **Defense pattern:** Detect key create, anomalous IAM, public bindings, metadata token use patterns, impossible travel for admins.
````

**J1085** · R7-2 · §0.1–§0.3 replaced by the part's own §0 (generic rules are in the course guide)

````text
## 0. Read this first — how this file complements the main course

### 0.1 Standing instruction (every teaching session)

**This file is a complement to the main course, not a second roadmap. Read both. Whenever a security-relevant main-course section is taught, also teach every companion concept bound to it (§2) in the same session, as one story. Similar, related, and overlapping security concepts are stitched and taught in parallel — never in separate sessions, never twice.**

Why: the main course owns the *roadmap spine* — what to learn, in what order, tied to certs (PCA, Cloud Security Engineer, Network Engineer, SecOps, SCS-C03, etc.) and the provider service maps. It lists security topics at outline depth (A5 networking, A10 crypto/security fundamentals, B1 shared responsibility, B5 IAM model, Track C container/K8s hardening, Phase 4 GCP Security services). It does not own attacker playbooks, misuse cases, rate-limit/WAF craft, session/JWT/OAuth failure modes, supply-chain attacker paths, IR tabletop depth, AI threat mechanics, or a full applied-cryptography track. This file supplies those and hangs each piece on the main-course section that needs it **when that section is taught**.

### 0.2 Stitching rules

1. **One concept, one teaching.** If both files mention an idea, teach it once in the owner (§2.1), and the other file only *adds*. Later sessions recall in one line.
2. **Ownership split.** *The main course owns:* learning order, cert mapping, service vocabulary (IAM, Armor, VPC-SC, KMS, SCC, SecOps), shared-responsibility framing at roadmap level. *This file owns:* attack mechanics, defensive design patterns, cryptography depth (`CR-*`), network-security attacks, exercise/scenario bank, IR tabletops.
3. **Same teaching discipline.** Issue **one** exercise at a time; learner attempts before keys; predict blast radius / control placement before revealing the answer. Prop Lock: do not use a later control (VPC-SC, Confidential VM, Binary Authorization) as a "known" prop before its main-course section has been covered (suite-wide rule: the main course §0.4.6) — postpone the exercise or teach the prerequisite first.
4. **GCP lens at three depths** when a concept is taught: **Lens-1** name the GCP (and AWS/Azure twin from the main-course mapping tables) resource; **Lens-2** touch via local vulnerable-by-design fixture or credits-safe lab; **Lens-3** cert-depth trade-offs (Cloud Security Engineer / PCA Security / SCS-C03).
5. **Bank ≠ dump.** §5 is a bank of scenario specs. Never paste Appendix K before an attempt.
6. **Predict → attempt → discrepancy → ledger.**
7. **Qualitative keys only** (no invented lab DB goldens).
8. **Inline tracking** with `- [ ]` boxes.
9. **Honesty:** `(verify)` on version-sensitive cloud product details.
10. **Lab safety hard bans:** no scanning third parties; no malware; no live DDoS; no credential stuffing against real accounts; fixtures on localhost / disposable projects only; crypto via vetted libraries only.
11. **User can override** skip/jump. On conflict: the main course wins on order and cert timing; this file wins on security/crypto content and exercise specs.
12. **Read economically:** §0 + §2, then only today's bound modules.

### 0.3 How one stitched session runs

1. **Anchor** — name the main-course section (e.g. A10, B5, Phase 4 Security) and list bound companion IDs from §2.
2. **Concept** — teach roadmap idea once, then layer attack/crypto depth from this file.
3. **GCP lens** — Lens-1 always; Lens-2 when Lab Reality allows.
4. **Numbers** — one estimate (QPS to throttle, key size, blast radius, RTO/RPO for IR).
5. **Exercise** — one card from §5 (prediction first).
6. **Check** — module check questions; learner answers first.
7. **Close** — tick boxes; note unlocked / shaky / postponed.

When other companions bind to the same session, the Suite Session Protocol (rule 0.4.2 in §0.7) governs.

````

**J1086** · R7-2 · anchor-rewrite

````text
### 0.4 Notation
````

**J1087** · R7-2 · copied preferences, contract and Lab Safety moved out

````text
### 0.5 University alignment (coverage checklist)

| Course / framework | Maps into |
|---|---|
| Stanford CS155 | TH, AU, WA, NT, DOS, CL, AI |
| Stanford CS255 | CR-01 … CR-20 |
| Stanford XACS235 Cloud Security | B1/CL shared responsibility, CK/WL, CR-14, IR, CM, SC/TEEs |
| MIT 6.858 / 6.566 | TH, CK isolation, WA, NT/TLS, SC, AU |
| Berkeley CS161 | CR foundations, NT, DOS, WA, AU |
| MIT 6.1600 Foundations of Computer Security · Boneh and Shoup, *A Graduate Course in Applied Cryptography*, version 0.6 (2023) | §10 academic pass: CRA.1…CRA.10 over CR-01…CR-19; CRA.11…CRA.17 over WA, AU, NT, DOS, AB, TH, PV and AI; SC |
| CMU Cloud Security | CL multi-tenancy, B5/IAM abuse, IR, CM |
| CSA CCM v4.x | §8 checklist (not a control dump) |
| OWASP Top 10:2025 · ATT&CK Cloud | WA, AU, CL, WL, IR |

### 0.6 Learner teaching preferences (binding)

- **Check questions must be woven into the concept explanation itself**, not asked as separate "what do you already know" diagnostics — the learner explicitly opted out of background-probing questions and asked for calibration to happen through how they handle the material.
- **"Maintain curriculum depth and academic rigour"** has been repeated multiple times as an explicit standing instruction — do not compress, simplify, or skip the "why," even under time pressure or a fast pace of correct answers.
- When companion-file content (system-design-primer, SQL, design-patterns) overlaps a main-course module, **teach it once, stitched into the same session** — never as a separate pass, per each companion's own §0.2 stitching rules.
- If a companion file references module IDs that don't exist in the main course (as the SQL companion's did before its IDs were rebound), **say so plainly rather than forcing a silent, possibly-wrong mapping** — this was well received when done for the SQL companion.

### 0.7 Suite Teaching Contract and Lab Safety (same text in every part)

The main course's §0.4 and §0.5, copied whole so that this companion can be taught on its own terms. The rule numbers stay the main course's (0.4.1…0.4.10, and the five Lab Safety rules), so "main course §0.4.3" and rule 0.4.3 here are the same rule. The **progress ledger** named below is the tutor's running record beside the inline boxes (main course §0.1): each ID's mastery state, the misconception register, the errata list, the recorded overrides and wrong predictions, and the exact resume point. The inline `- [ ]` boxes stay authoritative.

**Suite Teaching Contract (main course §0.4).**

One contract for every part; each companion carries the same contract in its own §0 and adds its session detail. When two rules conflict, the higher one wins: (1) the learner's explicit instruction in the current chat · (2) the learner teaching preferences (§0.6 here) · (3) the main course on order, cert timing and Lab Reality · (4) the owning part on its content (main course §0.3) · (5) the companions' defaults.

**0.4.1 Rhythm.**

- One concept per turn, at full depth. New material is taught by direct explanation; procedures by worked, parallel examples.
- Every turn carries exactly one focused question, embedded in the teaching. Diagnosis happens through those checks; there is no separate probing (the learner preferences in §0.6 rule out separate calibrating questions). A turn may be as long as one concept needs.
- Correction style: confirm the correct part explicitly, then sharpen the imprecise part by naming the exact mechanism. No false praise. Hold the line under "just tell me"; give a foothold when the learner is genuinely stuck.
- Overrides: the learner may skip (after passing the skip-test), jump, or go hands-on. Every override is recorded in the ledger so the prerequisite check can flag what was skipped.

**0.4.2 Suite Session Protocol.** When several files bind to one module, the session runs:

1. **Anchor** — list the bound IDs from *all* files (each companion's §2).
2. **Concept** — taught once, by the owner in main course §0.3.
3. **Layers**, in fixed order: system design (primer) → SQL/engine → patterns → Go implementation (Go companion) → attacker/crypto (cyber).
4. **GCP lens.**
5. **One Numbers step** for the whole session.
6. **One application item**: a primer micro-problem *or* a companion exercise card, never both for the same concept.
7. **Checks**, woven in per §0.6.
8. **Close**, ticking boxes in every file (§0.4.8).

**0.4.3 Exercise progression.** The first five rungs of the ten-rung ramp (anchor, vocabulary, representation, core move, worked illustration) are the teaching turns. Exercises then climb, one item per turn, advancing only when the current rung is passed: basic unseen check → routine variation → mixed transfer (the new idea plus exactly two earlier mastered ideas) → top-rung challenge → reflection (the learner explains back or invents an example).

**0.4.4 Predict → run → discrepancy.** Every exercise with a result shape, row count, plan shape, isolation outcome or attack outcome starts with a one-line prediction. Then run. A wrong prediction is recorded in the ledger and taught from.

**0.4.5 Mastery states.** Every ID is `not-started` → `in-progress` → `taught` (explained, first check answered) → `mastered` (passed a rung-3 or rung-4 item, or the skip-test). It may also be `shaky` (missed a check after teaching), `unverified` (claimed done without evidence) or `sliced` (only a named slice taught). Taught and mastered IDs get one-question recalls woven into later relevant sessions at about +1, +3, +7 and +21 sessions; a missed recall sets `shaky` and re-teaches only the gap. The misconception register lives in the ledger; checks probe each entry until two consecutive correct answers retire it.

**0.4.6 Anchoring and suite-wide Prop Lock.** No term, product or control is used in an explanation, example or check unless it is anchored: taught this session, or at least `taught` on the ledger. A named-but-not-taught mention is allowed only when labelled "we'll cover this in X". A check that relies on unanchored terms is invalid: fix the check; don't mark the learner shaky.

**0.4.7 Check questions and exercise pre-flight.** A check tests mechanism or application, asks one thing (split a multi-part check across turns), is answerable from anchored material, has a written expected answer and at least one expected wrong answer in the owning file's keys, is precision-sensitive, and is never answered by the tutor in the same turn. Before issuing any exercise the tutor checks: internal consistency (for example, a CNAME never points at an IP) · every term anchored · exactly one question · the answer derivable from what was taught · any numbers computed. The tutor is precise about mechanisms and says explicitly when unsure. An error found later is corrected openly in the next turn and logged in the errata list of the progress ledger.

**0.4.8 Pacing, checkpoints and session close.** Each module is budgeted at roughly 3–5 concepts per session at full depth; an over-budget module is split into teaching blocks. The budget is a plan, never a reason to compress depth. A problem or checkpoint runs only when all its must-know IDs are at least `taught`, and it introduces at most one new concept. Every session ends by: (1) marking every ID bound to the session taught / sliced / deferred-with-reason / recalled (nothing left unmarked); (2) updating mastery states and the recall schedule; (3) updating the misconception register; (4) adding any errata; (5) emitting a ledger delta block (and a full ledger every 5th session or on request); (6) naming the exact resume point and any open question, verbatim.

**0.4.9 Implementation language: Go.** Go is the suite's language for application code: services, build labs that write a program, and capstones. Python stays the first language of A3, the language of Track D's machine-learning work, and the language of labs already written in Python (the SQL companion's lab kit, the "Python twin" that some labs name). Go is taught by the Go Language Companion: its language core (GO-01…GO-14) is the Go block of A3, and its later modules bind where they are first used. Four rules:

1. **Syntax unlock** — rule 0.4.6 applied to code. A Go construct appears in an explanation, a lab or a check only once the GO module that unlocks it is at least `taught`; before that, the lab runs in Python or waits, and the construct is named only as "we'll cover this in GO-nn". The first use of each construct carries its unlock block: signature → semantics → runtime and memory → contrast with Python, Java, C or JavaScript, naming the bug the other habit causes in Go.
2. **Lab acceptance** — Go lab code is accepted when `gofmt -l` prints nothing, `go vet ./...` is clean, the tests pass (under `go test -race` from GO-19 on; the race detector needs cgo), no error is silently dropped, and every goroutine the code starts has a way to be stopped.
3. **Version honesty** — the baseline release is the one the learner's own module declares. A behaviour is taught as fact only when it has been run on the installed release; anything else carries `(verify)`. The go command downloads modules, and whole toolchains when a module's `go` line is newer than the installed release: name what a step will fetch before running it.
4. **Involved problem** — every GO module ends with one involved problem: a program the learner designs and writes alone, aimed at the module's hardest idea, with its rubric kept in the Go companion's keys and shown only after submission. It is the module's top-rung challenge (rule 0.4.3), so a GO module is `mastered` only when its problem passes its rubric or its skip-test passes (this tightens rule 0.4.5 for GO modules). It is a project across several turns, not a check: hints come only when asked, one at a time, and the tutor never writes the solution.

**0.4.10 Academic depth (undergraduate prerequisites).** The course teaches every undergraduate prerequisite of cloud and system architecture at the depth of a university course, not only at the engineering depth of a first pass. Each module of Tracks A to D, and each companion, carries an **academic pass**: formal definitions, theorems with their proofs or proof sketches, derivations, named readings, and a numbered problem set whose written keys (an expected answer and at least one expected wrong answer, rule 0.4.7) sit in the owning part's keys. The University and textbook alignment table (main course §0.6) says which university courses and textbooks each pass is aligned with. Four rules:

1. **Two passes, one module.** The engineering pass comes first. The academic pass follows under the same module ID, as its own teaching blocks (rule 0.4.8), never as a separate course. A "first-pass scope" note limits the first pass only.
2. **Proof standard.** A claim presented as a theorem is proved in the session, set as a proof problem, or labelled "stated without proof", naming where the proof is found. Derivations show every step, and every number is computed, not asserted.
3. **Problem sets are exercises.** They climb the ramp (rule 0.4.3). An academic block is `mastered` only when at least one proof (or derivation) problem and one computational problem in it pass against their keys (this tightens rule 0.4.5 for academic blocks), so every block's problem set carries both kinds. In the main course the block is a module's academic pass (its D lines and its problem set); in a companion it is the companion's academic pass.
4. **Readings are named, not linked.** A text is cited by author, title and edition; a course by institution and course name. Editions and course numbers change, so the alignment table carries its check date, and anything not checked carries `(verify)`.

**Lab Safety (main course §0.5).**

One rule set for every file; it unifies the cybersecurity companion's rule 10, the SQL companion's rule 10 and the main course's Lab Reality paragraph.

1. **Hard bans:** no scanning of third parties; no malware; no live DDoS; no credential stuffing against real accounts; fixtures on localhost or disposable projects only; crypto through vetted libraries only.
2. **Money and time:** local first (Docker Postgres, local fixtures). Credit-using services are created for one lab and destroyed the same day, with a budget alert set before the first apply.
3. **Secrets and data:** never put a password, key or real customer data in a query, a prompt or a course file. Lab data is synthetic.
4. **The workplace console is read-only:** look, never create or change.
5. **Every lab carries a Lab Reality tag:** `[free-tier]` · `[credit ~$X]` · `[plan-only]` · `[paper]` · `[local]`.
````

**J1088** · R7-3 · overlap-register slice moved to rule 0.3

````text
### 2.1 Overlap register — teach once

> **Note:** the suite-wide register is the main course §0.3; this table is the security slice of it, and on a conflict the main course's register wins.

| Idea | Owner | This file adds |
|---|---|---|
| Shared responsibility one-liner | B1 | PQ-S-03 matrices by service model |
| TLS handshake vocabulary | A5 (mechanics) / A10 (formal) | CR-12 attacks, 0-RTT, validation bugs |
| IAM principals/roles | B5 | CL IAM privesc / key sprawl playbooks |
| "Use KMS/CMEK" | The main course's Phase 4 Security | CR-14 envelope hierarchy + compromise IR |
| Armor / DDoS product names | V-NET / Phase 4 Networking | DOS taxonomy + rate-limit/bot design |
| Container non-root / PSS | C1/C2 | CK escape & supply-chain attacker paths |
| OAuth/JWT mentioned | A7 | AU/CR failure modes (alg confusion, mix-up) |
````

**J1105** · R7-4 · anchor-rewrite

````text
This file has **self-contained content**; ownership is shared per the suite overlap register (the main course §0.3). It covers **cloud security, cybersecurity, cryptography, and network security** for cloud infrastructure and cloud-hosted distributed systems — taught in parallel with the matching sections of the main course.
````

**J1106** · R7-4 · anchor-rewrite

````text
*Equal scale to AU/AB/CL. A7 (API auth patterns) and A10 name the password and JWT products; the build labs are here — CR-13 (passwords), AU-05 (JWT policy), CR-14 (KMS and CMEK) — and CR owns the cryptographic justification and failure modes. Stanford CS255 alignment: see §0.5.*
````

**J1107** · R7-4 · anchor-rewrite

````text
- **Map to GCP:** DOS-02, §0.2.10
````

**J1108** · R7-4 · anchor-rewrite

````text
The academic pass of this companion: cryptography with definitions and proofs (CRA.1–CRA.10), then the formal core of the other families — web security, authentication protocols, network security and zero trust, denial of service, threat modelling, privacy and the security of machine-learning systems (CRA.11–CRA.17) — at the depth of Stanford CS 255, Stanford CS 253, MIT 6.1600 and Berkeley CS 161 (main course §0.6 and §0.5 here). Each block is taught after the engineering pass of the cards it names. It is the formal layer that the main course's A10.D3 points to. Problems CRA-P1…CRA-P24 are in §10.18, with keys in Appendix K under "K-academic" (after the attempt only). A block is `mastered` by rule 0.4.10.3. Notation: ⊕ is XOR, |x| is the length of x, and "negligible" means smaller than any inverse polynomial in the security parameter.
````
