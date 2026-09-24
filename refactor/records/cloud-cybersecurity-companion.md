# Records for cloud-cybersecurity-companion.md (R2b, 2026-09-24)

Refactor bookkeeping only, not course material. Decision D6 keeps provenance, the D3 archive and every line R2b changed or removed out of the course files; decision D3 keeps them here, verbatim. Each entry names the R2b journal number (outputs/r2b/journal.jsonl), the rule and the class.

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

**J626** · SEC-1 · anchor-rewrite

````text
**Companion to [`Curriculum`](./Curriculum.md)** (the cloud mastery / certification roadmap).
````

**J627** · SEC-1 · anchor-rewrite

````text
When other companions bind to the same session, the Suite Session Protocol in `Curriculum` §0.4 governs.
````

**J628** · SEC-2 · anchor-rewrite

````text
- `Curriculum` IDs: module IDs (`A5`, `A7`, `A10`, `B1`, `B5`, `C1`, `C2` …), Part V category IDs (`V-NET`, `V-SEC` …), `Phase 4 Networking` / `Phase 4 Security`, the reserved tracks (`M`, `U`, `S`), and cert names (PCA, Cloud Security Engineer, …). `Nx.y` = a section of `northstar-reference-app.md`; it carries the old parent's number and meaning. The old pseudo-anchors (`Phase4-Sec.n`, `A5/Phase4-Net.n`, `A10/B5.n`) are gone.
````

**J629** · SEC-3 · anchor-rewrite

````text
| CCM domain | Companion homes | the reference cloud app evidence sketch |
````

**J630** · SEC-3 · anchor-rewrite

````text
- **Lab:** SEC-Z0.3: map each Saltzer principle to one the reference cloud app control.
````

**J631** · SEC-3 · anchor-rewrite

````text
- **Lab:** SEC-E1.3: one the reference cloud app ADR that prices a control vs accept risk.
````

**J632** · SEC-3 · anchor-rewrite

````text
- **Check:** List five the reference cloud app assets and their trust boundary.
````

**J633** · SEC-3 · anchor-rewrite

````text
- **Lab:** CR-E1: for three the reference cloud app fields, name goal + required game.
````

**J634** · SEC-3 · anchor-rewrite

````text
- **Check:** Name five CCM domains and one the reference cloud app control each.
````

**J635** · SEC-3 · anchor-rewrite

````text
- **Scenario:** Five the reference cloud app controls listed.
````

**J636** · SEC-3 · anchor-rewrite

````text
- **Check:** Give a the reference cloud app Elevation example that HTTPS does not stop.
````

**J637** · SEC-3 · anchor-rewrite

````text
- **Check:** Name an expensive the reference cloud app endpoint to protect first.
````

**J638** · SEC-3 · anchor-rewrite

````text
- **Scenario:** Standing global HTTPS LB+Armor vs Hosting+Run for early the reference cloud app.
````

**J639** · SEC-3 · anchor-rewrite

````text
- **GCP lens:** Lens-1: resource hierarchy. Lens-2: annotate existing the reference cloud app HLD.
````

**J640** · SEC-3 · anchor-rewrite

````text
- **Scenario:** Marketing site on `www` sets cookie Domain=.the reference cloud app.example.
````

**J641** · SEC-3 · anchor-rewrite

````text
#### SEC-E1.1 · L1 · the reference cloud app STRIDE one-pager
````

**J642** · SEC-3 · anchor-rewrite

````text
### SEC-CAP1 · the reference cloud app hardening pass
````

**J643** · SEC-3 · anchor-rewrite

````text
Victim API decrypts CBC and returns HTTP 400 "bad padding" vs 403 "bad mac". Attacker flips bits in ciphertext block \(C_i\) and observes which error returns. Over many queries they recover plaintext bytes (Vaudenay). **Teaching move:** derive why *integrity first* (AEAD or EtM) collapses the oracle; connect to CR-03 lab card CR-E3. **the reference cloud app link:** never expose distinct crypto error classes on legacy token decrypt paths.
````

**J644** · SEC-3 · anchor-rewrite

````text
#### SEC-E3.9 · L3 · OWASP map the reference cloud app
````

**J645** · SEC-3 · anchor-rewrite

````text
- **Defense pattern:** Map the reference cloud app detections to a few techniques; do not boil the ocean.
````

**J646** · SEC-3 · anchor-rewrite

````text
- **GCP lens:** Lens-1: watch Google Cloud PQ/TLS announcements (verify). Lens-2: inventory the reference cloud app keys by lifetime.
````

**J647** · SEC-3 · anchor-rewrite

````text
- **Check:** Recite eight non-negotiables for the reference cloud app crypto.
````

**J648** · SEC-3 · anchor-rewrite

````text
- **Check:** Give a BFLA example on the reference cloud app admin.
````

**J649** · SEC-3 · anchor-rewrite

````text
- **GCP lens:** Lens-1: N6.11 map. Lens-2: redraw the reference cloud app path.
````

**J650** · SEC-3 · anchor-rewrite

````text
- **GCP lens:** Lens-1: SDP infoTypes; resource labels. Lens-2: classify the reference cloud app fields.
````

**J651** · SEC-3 · anchor-rewrite

````text
- **Predict impact (write first):** Map A01–A05 to the reference cloud app controls.
````

**J652** · SEC-3 · anchor-rewrite

````text
- **Scenario:** the reference cloud app controls known.
````

**J653** · SEC-3 · anchor-rewrite

````text
- **Scenario:** the reference cloud app crypto ADR blank.
````

**J654** · SEC-3 · anchor-rewrite

````text
Use as a *gap finder*, not a dump. Mark the reference cloud app evidence paths.
````

**J655** · SEC-3 · anchor-rewrite

````text
10. **Line-count / completeness note:** This companion prioritizes stitchable attack+crypto depth over encyclopedic CCM dumps; use §8 as a gap finder when auditing the reference cloud app evidence.
````

**J656** · SEC-3 · anchor-rewrite

````text
- **Scenario:** the reference cloud app has IAM deny, parameterized SQL, IAP admin, org policy default deny public buckets.
````

**J657** · SEC-3 · anchor-rewrite

````text
- **Scenario:** the reference app's controls known.
````

**J658** · SEC-3 · anchor-rewrite

````text
- **Scenario:** the reference app's crypto ADR blank.
````

**J659** · SEC-3 · anchor-rewrite

````text
- **GCP lens:** Lens-1: the reference cloud app ledger invariants (N5.3). Lens-2: race test.
````

**J660** · SEC-3 · anchor-rewrite

````text
9. **Built** 2026-09-22 for the reference cloud app / `Curriculum` pairing.
````

**J661** · SEC-3 · anchor-rewrite

````text
#### TH-02 · Trust boundaries & asset inventory for the reference cloud app — stitch: A10 · S6
````

**J662** · SEC-3 · anchor-rewrite

````text
#### CR-20 · Crypto engineering checklist for the reference cloud app — stitch: Phase 4 Security · all CR
````

**J663** · SEC-3 · anchor-rewrite

````text
- **GCP lens:** Lens-1: ADR linking checklist to Secret Manager/KMS/Armor TLS. Lens-2: audit the reference cloud app against checklist.
````

**J664** · SEC-3 · anchor-rewrite

````text
**Skip-test for CR track (SEC-T1+SEC-T2 in §4):** learner must, unaided: (1) state IND-CPA vs integrity goals with one example each; (2) explain why ECB and raw RSA fail; (3) give GCM nonce-reuse consequence; (4) prefer AEAD over CBC+HMAC DIY; (5) sketch envelope KEK/DEK with KMS; (6) name TLS 1.3 0-RTT risk; (7) justify Argon2id over SHA-256 for passwords; (8) list eight CR-20 checklist items for the reference cloud app.
````

**J665** · SEC-3 · anchor-rewrite

````text
- **Defense pattern:** Map the reference cloud app to subset: IAM, EKM/CEK, LOG, IVS, TVM, AIS, SEF — evidence paths.
````

**J666** · SEC-3 · anchor-rewrite

````text
- **Scenario:** Cloud Run + Cloud SQL + GCS for the reference cloud app.
````

**J667** · SEC-4 · anchor-rewrite

````text
*Generated from the §6.2 crosswalk (2026-09-24).* Every concept module appears once as primary; secondary anchors are previews, recalls or Lens-3 passes. The nine old checkpoint IDs that were never defined (shown below as 'was E-…') are mapped to existing cards by content (`crosswalk.md` §3; `[resolved-by-default]`). VPC-SC is NT-06. The pre-refactor table is kept in the D3 archive.
````

**J668** · SEC-4 · anchor-rewrite

````text
| `Curriculum` anchor | Taught here (primary, §6.2) | Also in this session (secondary) | Checkpoint |
````

**J669** · SEC-5 · anchor-rewrite

````text
*Equal scale to AU/AB/CL. `Curriculum` A7 (API auth patterns) + A10 own password/JWT *product* labs; Phase 4 Security (N7.3) owns the CMEK *product* spine; CR owns cryptographic justification and failure modes. Stanford CS255 alignment: see §0.5.*
````

**J670** · SEC-5 · anchor-rewrite

````text
- **GCP lens:** Lens-1: signed requests in N4.5 use HMAC — recall roadmap lab; CR adds composition rules.
````

**J671** · SEC-5 · anchor-rewrite

````text
- **Defense pattern:** *Roadmap N4.3 owns product labs.* CR adds: threat model (online vs offline), parameter tuning rationale, pepper in KMS, migration/version field.
````

**J672** · SEC-5 · anchor-rewrite

````text
- **GCP lens:** Lens-1: pepper in Secret Manager/KMS. Lens-2: recall N4.3 Argon2id lab — add threat-model paragraph.
````

**J673** · SEC-5 · anchor-rewrite

````text
- **Defense pattern:** *N7.3 owns CMEK lab.* CR adds: hierarchy diagram, rewrap vs re-encrypt, key purpose separation, when CMEK vs CSEK vs Google-managed.
````

**J674** · SEC-5 · anchor-rewrite

````text
- **GCP lens:** Lens-1: Cloud KMS key ring/key; CMEK on GCS/SQL (verify); Cloud HSM/EKM literacy. Lens-2: local envelope toy from N7.3 + hierarchy labels.
````

**J675** · SEC-5 · anchor-rewrite

````text
**Prop Lock for crypto props:** do not use Cloud HSM, EKM, Confidential Space, or Binary Authorization as assumed props before their Northstar sections (N7.3 / N7.5) and companion CR-14 / CR-18 / WL-04 are unlocked. Local AEAD/HMAC toys may use Tink without those props.
````

**J676** · SEC-5 · anchor-rewrite

````text
**Pairing rule with A7 (API auth patterns) + A10 & N7.3:** A7 (API auth patterns) + A10 own password *product* labs and JWT *policy* labs; CR-13/CR-10 own the cryptographic *why* and failure modes. Phase 4 Security (N7.3) owns CMEK *clickpath*; CR-14 owns hierarchy theory and SoD. Teach as one story per §2 stitch rows.
````

**J677** · SEC-5 · anchor-rewrite

````text
3. CR-05…07 + CR-13 at A10 (password/KDF day; the A7 API-auth product labs are recalled, N4.3).
````

**J678** · SEC-5 · anchor-rewrite

````text
5. CR-14…15 + CR-20 at Phase 4 Security (KMS + key IR; N7.8).
````

**J679** · SEC-5 · anchor-rewrite

````text
6. CR-16 at A10; CR-17…18 at Phase 4 Security, with Confidential Computing literacy + N9c privacy (survey depth).
````

**J680** · SEC-5 · anchor-rewrite

````text
Object bytes encrypted with DEK_AES-GCM; DEK wrapped by KMS KEK; metadata stores wrapped DEK + key version. Compromise of object store without `cloudkms.cryptoKeyEncrypterDecrypter` yields ciphertext only. **Teaching move:** draw trust boundary between storage IAM and KMS IAM; SoD. Cards CR-E9/E10/E34. Roadmap N7.3 owns the product clickpath.
````

**J681** · SEC-5 · anchor-rewrite

````text
SHA-256(password) at \(10^9\) guesses/s/GPU vs Argon2id ~64MB ~100 ms. Show order-of-magnitude table; salt kills rainbows; pepper in KMS raises bar after DB leak. Roadmap N4.3 owns implementation; CR-13 owns the math story. Card CR-E8.
````

**J682** · SEC-6 · anchor-rewrite

````text
- **GCP lens:** Lens-1: Cloud Run vs GCE vs GCS rows. Lens-2: annotate N0 hierarchy with trust boundaries.
````

**J683** · SEC-6 · anchor-rewrite

````text
- **GCP lens:** Lens-1: app middleware (N4.4 lab). Lens-2: forged Origin test.
````

**J684** · SEC-6 · anchor-rewrite

````text
- **GCP lens:** Lens-1: app PEP; IAP is not object AuthZ. Lens-2: IDOR fail-then-pass (N4.7).
````

**J685** · SEC-6 · anchor-rewrite

````text
- **GCP lens:** Lens-1: recall N8.1 cursor pager — add abuse tests.
````

**J686** · SEC-6 · anchor-rewrite

````text
- **GCP lens:** Lens-1: Cloud Run request timeout + `http.Server` timeouts (N4.2). Lens-2: slowloris against *local* fixture only.
````

**J687** · SEC-6 · anchor-rewrite

````text
- **GCP lens:** Lens-1: Cloud Run CORS middleware. Lens-2: hostile Origin tests (N4.4).
````

**J688** · SEC-6 · anchor-rewrite

````text
- **GCP lens:** Lens-1: GCE metadata server; Cloud Run identity. Lens-2: local SSRF fixture + guard tests (N4.2).
````

**J689** · SEC-6 · anchor-rewrite

````text
- **GCP lens:** Lens-1: org policy `storage.publicAccessPrevention` (verify). Lens-2: paper IR for public ACE (N7.8).
````

**J690** · SEC-6 · anchor-rewrite

````text
- **GCP lens:** Lens-1: N6.11 map. Lens-2: redraw the reference app's path.
````

**J691** · SEC-6 · anchor-rewrite

````text
- **GCP lens:** Lens-1: Binary Authorization + Artifact Registry. Lens-2: recall N7.5 lab analytic layer.
````

**J692** · SEC-6 · anchor-rewrite

````text
- **GCP lens:** Lens-1: Binary Authorization API. Lens-2: N7.5 toy attestation analytic.
````

**J693** · SEC-6 · anchor-rewrite

````text
- **GCP lens:** Lens-1: SCC findings + log-based metrics. Lens-2: wire one alert to N7.6 template.
````

**J694** · SEC-6 · anchor-rewrite

````text
- **Defense pattern:** Disable SA/keys → hunt audit → rotate workloads → rewrap secrets → postmortem. Use roadmap N7.8 template; CR-15 for crypto keys.
````

**J695** · SEC-6 · anchor-rewrite

````text
- **Defense pattern:** PAN: tokenize (N5); secrets: Secret Manager; fields: AEAD when needed.
````

**J696** · SEC-6 · anchor-rewrite

````text
- **GCP lens:** Lens-1: PCI themes N5 + SDP. Lens-2: decision table.
````

**J697** · SEC-6 · anchor-rewrite

````text
- **GCP lens:** Lens-1: Well-Architected + CCM crosswalk lite. Lens-2: gap spreadsheet.
````

**J698** · SEC-6 · anchor-rewrite

````text
Skip a companion family only by passing its skip-test. `Curriculum` and Northstar still own product labs — skipping companion theory does not skip Armor attach / IAP / CMEK product evidence.
````

**J708** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** A5 TLS / N6.11 path
````

**J709** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** N7.1 recall + PQ-S-02
````

**J710** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** N0.4 HLD
````

**J711** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** N0.4
````

**J712** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** N6.14
````

**J713** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** N4.4
````

**J714** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** N4.4
````

**J715** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** N7.4
````

**J716** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CR-14, N7.3 toy
````

**J717** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** N3.0, AB-06
````

**J718** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** WA-01, N4.4
````

**J719** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CL-01, N4.2
````

**J720** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** AU-08, AB-03, N4.10
````

**J721** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** AU-11, N4.7
````

**J722** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** DOS-05, N4.2
````

**J723** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** AB-02, N4.10
````

**J724** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** N6.11, NT-07
````

**J725** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CR-12, N6.13
````

**J726** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** AB-03, N4.10
````

**J727** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** NT-04, N6.16
````

**J728** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CL-03, N7.2
````

**J729** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CL-04, IR-05, N7.8
````

**J730** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** NT-02, N6.12
````

**J731** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** NT-05, N6.14
````

**J732** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** NT-06, N6.15
````

**J733** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** PV-01, N7.3
````

**J734** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** WL-04, CK-05, N7.5
````

**J735** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** PV-03, N5
````

**J736** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** IR-05, N7.8
````

**J737** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** DOS-07, N10.3
````

**J738** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CM-01, N7.9
````

**J739** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** AI-01, AI-02, N9c
````

**J740** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CR-13, N4.3
````

**J741** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CR-14, N7.3
````

**J742** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CR-14, N7.3
````

**J743** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** AB-02, DOS-03, N4.10, N6.16
````

**J744** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CL-04, IR-05, N4.8, N7.8
````

**J745** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** AU-03, AU-04, N4.4
````

**J746** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** WL-04, CK-05, N7.5
````

**J747** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** IR-01, N7.6, N10
````

**J748** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** AI-01, AI-03, PV-02, N9c
````

**J749** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CL-02, PV-01, N7.3, N7.7
````

**J750** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** AB-04, N4.10
````

**J751** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** AU-06, N4.6
````

**J752** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CR-14, CR-15, N7.3
````

**J753** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CR-13, N4.3, N4.9
````

**J754** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** PQ-S-03, N2.3
````

**J755** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CL-01, CL-02, NT-06, N4.2, N6.15
````

**J756** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** WL-01, WL-04, CK-05, N7.5
````

**J757** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** WA-05, WA-11, N7.4
````

**J758** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** IR-03, CR-15, N7.8
````

**J759** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** AI-01, AI-02, N9c
````

**J760** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** AU-05, CR-10, N4.5
````

**J761** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** CL-07, NT-02, N6.15
````

**J762** · SEC-7 · anchor-rewrite

````text
- **Map to GCP:** DOS-07, AB-01, N10.3
````

**J763** · SEC-7 · anchor-rewrite

````text
- **Design control:** Follow N7.8 public ACE runbook + evidence.
````

**J764** · SEC-7 · anchor-rewrite

````text
- **Design control:** Argon2id+salt+pepper plan (N4.3 owns lab).
````

**J765** · SEC-7 · anchor-rewrite

````text
- **Design control:** Fill N7.8 template; grade order.
````

**J766** · SEC-8 · anchor-rewrite

````text
- **Depends:** AU-*, WA-* core, AB-01/02, CL-01, CR-12/13/14/20, A7 (API auth patterns) + A10 + N7.3–N7.4.
````

**J767** · SEC-8 · anchor-rewrite

````text
- **Depends:** IR-*, CL-02/04, CR-15, roadmap N7.8 templates.
````

**J768** · SEC-8 · anchor-rewrite

````text
- **Depends:** AB-*, DOS-03/05/07, AU-08, N4.10, 6.16.
````

**J769** · SEC-8 · anchor-rewrite

````text
- **Depends:** AI-01…05, PV-02, CR-18 lite, 9c.
````

**J770** · SEC-8 · anchor-rewrite

````text
Run **SEC-CAP1** after A7 (API auth patterns) + A10 + CR-20 unlocked; **SEC-CAP2** after N7.8 + IR/CR-15; **SEC-CAP3** after N4.10 + N6.16 + AB/DOS; **SEC-CAP4** after N9c + AI-*. Never schedule a capstone that smuggles a locked prop — postpone or unlock first (Prop Lock).
````

**J771** · SEC-8 · anchor-rewrite

````text
3. **Prop Lock examples:** no VPC-SC before N6.15; no BinAuth before N7.5; no Confidential VM as assumed before CR-18/SC-03.
````

**J772** · SEC-8 · anchor-rewrite

````text
8. **SCC green ≠ secure:** pair N7.6 with IR-02 alert design on day one of detection.
````

**J773** · SEC-9 · anchor-rewrite

````text
| IAM | CL-03, AU-*, B5 / N7.2 | Least privilege bindings |
````

**J774** · SEC-9 · anchor-rewrite

````text
| GRC | CM-01, N7.9 | ADRs, risk register |
````

**J775** · SEC-9 · anchor-rewrite

````text
| A&A | CM-02, N7.9 | Control matrix |
````

**J776** · SEC-9 · anchor-rewrite

````text
| UEM | NT-05, N6.14 | IAP device signals literacy |
````

**J777** · SEC-9 · anchor-rewrite

````text
| EKM / CEK | CR-14…15, N7.3 | KMS keys, CMEK |
````

**J778** · SEC-9 · anchor-rewrite

````text
| DSP | PV-02, N7.3 | SDP jobs |
````

**J779** · SEC-9 · anchor-rewrite

````text
| IVS | CK-*, WL-*, N7.5 | Hardened runtime |
````

**J780** · SEC-9 · anchor-rewrite

````text
| MSC | NT-*, N6.x | Network segmentation |
````

**J781** · SEC-9 · anchor-rewrite

````text
| Plane | Assets | Primary attackers | Top companion modules | Roadmap anchors |
````

**J782** · SEC-9 · anchor-rewrite

````text
| Storefront | Session, catalog, carts | Web attacker, bots | AU-01…04, WA-02, AB-03, DOS-03 | A5 TLS, N4.4, N4.10 |
````

**J783** · SEC-9 · anchor-rewrite

````text
| Customer API | Orders, PII, tokens | Web, stuffing, IDOR | AU-08, AU-11, WA-05, AB-01, CL-01 | N4.2–N4.7, N4.10 |
````

**J784** · SEC-9 · anchor-rewrite

````text
| Admin | Refunds, config | Stolen session, CSRF, BFLA | AU-03, AU-12, NT-05 | N4.4, N4.7, N6.14 |
````

**J785** · SEC-9 · anchor-rewrite

````text
| Service-to-service | SA identity, internal RPC | Confused deputy, key theft | AU-14, CL-04, CR-17 | N4.8, N7.2 |
````

**J786** · SEC-9 · anchor-rewrite

````text
| Data | SQL, GCS, BQ | Public ACE, SSRF→cred, insider | CL-02, CR-14, PV-*, NT-06 | N7.3, N6.15 |
````

**J787** · SEC-9 · anchor-rewrite

````text
| CI/CD | Build SA, images | Poisoned PR, unsigned deploy | WL-02, WL-04, CK-05 | N4.8, N7.5 |
````

**J788** · SEC-9 · anchor-rewrite

````text
| AI gateway | Tools, RAG corpus | Prompt injection, tool abuse | AI-01…05, PV-02 | N9c |
````

**J789** · SEC-9 · anchor-rewrite

````text
11. **When in doubt on a GCP SKU name:** prefer the `Curriculum` / Northstar product lab + live docs; companion scenarios stay valid even if a SKU renames.
````

**J790** · SEC-13 · anchor-rewrite

````text
- **Defense pattern:** Complete mediation; fail-safe defaults; economy of mechanism; least common mechanism; psychological acceptability — *recall* CIA/least-privilege/defense-in-depth/assume-breach/zero-trust/shared-responsibility from 7.1.
````

**J791** · SEC-13 · anchor-rewrite

````text
- **GCP lens:** Lens-1: Policy Analyzer / IAM recommender (verify). Lens-2: toy effective-access from 7.2.
````

**J792** · SEC-13 · anchor-rewrite

````text
- **GCP lens:** Lens-1: Cloud DNS DNSSEC; destroy-order checklist 6.16. Lens-2: paper only.
````

**J793** · SEC-13 · anchor-rewrite

````text
- **GCP lens:** Lens-1: IAP lab 6.14. Lens-2: compare threat tables.
````

**J794** · SEC-13 · anchor-rewrite

````text
- **GCP lens:** Lens-1: Cloud Build provenance (verify). Lens-2: cosign-shaped toy from 7.5.
````

**J795** · SEC-13 · anchor-rewrite

````text
**Prop Lock reminder:** passing SEC-T2 does not unlock VPC-SC props before 6.15.
````

**J796** · SEC-13 · anchor-rewrite

````text
- **Design control:** Redesign per 4.3+AU-10.
````

**J797** · SEC-13 · anchor-rewrite

````text
- **Design control:** Set timeout suite from 4.2.
````

**J798** · SEC-13 · anchor-rewrite

````text
| AIS | 3.0/4.x, WA-* | Secure SDLC tests |
````

**J799** · SEC-10 · anchor-rewrite

````text
- **Scenario:** GCE guest OS CVE; Cloud Run app SQLi; GCS public ACE; Google DC physical.
````

**J800** · SEC-10 · anchor-rewrite

````text
- **Scenario:** Docs skim (verify).
````

**J801** · SEC-10 · anchor-rewrite

````text
- **Scenario:** CNAME to deleted Cloud Run.
````

**J817** · SEC-12 · anchor-rewrite

````text
This file has **self-contained content**; ownership is shared per the suite overlap register (`Curriculum` §0.3). It covers **cloud security, cybersecurity, cryptography, and network security** for cloud infrastructure and cloud-hosted distributed systems — taught in parallel with the matching sections of `Curriculum`.
````

**J818** · SEC-12 · anchor-rewrite

````text
**Does not own:** non-security tracks in `Curriculum` (ML math, general DSA, FinOps deep-dives, non-security data modeling). Those stay in `Curriculum` only.
````

**J819** · SEC-12 · anchor-rewrite

````text
## 0. Read this first — how this file complements `Curriculum`
````

**J820** · SEC-12 · anchor-rewrite

````text
**This file is a complement to `Curriculum`, not a second roadmap. Read both. Whenever a security-relevant `Curriculum` section is taught, also teach every companion concept bound to it (§2) in the same session, as one story. Similar, related, and overlapping security concepts are stitched and taught in parallel — never in separate sessions, never twice.**
````

**J821** · SEC-12 · anchor-rewrite

````text
Why: `Curriculum` owns the *roadmap spine* — what to learn, in what order, tied to certs (PCA, Cloud Security Engineer, Network Engineer, SecOps, SCS-C03, etc.) and the provider service maps. It lists security topics at outline depth (A5 networking, A10 crypto/security fundamentals, B1 shared responsibility, B5 IAM model, Track C container/K8s hardening, Phase 4 GCP Security services). It does not own attacker playbooks, misuse cases, rate-limit/WAF craft, session/JWT/OAuth failure modes, supply-chain attacker paths, IR tabletop depth, AI threat mechanics, or a full applied-cryptography track. This file supplies those and hangs each piece on the `Curriculum` section that needs it **when that section is taught**.
````

**J822** · SEC-12 · anchor-rewrite

````text
2. **Ownership split.** *`Curriculum` owns:* learning order, cert mapping, service vocabulary (IAM, Armor, VPC-SC, KMS, SCC, SecOps), shared-responsibility framing at roadmap level. *This file owns:* attack mechanics, defensive design patterns, cryptography depth (`CR-*`), network-security attacks, exercise/scenario bank, IR tabletops.
````

**J823** · SEC-12 · anchor-rewrite

````text
3. **Same teaching discipline.** Issue **one** exercise at a time; learner attempts before keys; predict blast radius / control placement before revealing the answer. Prop Lock: do not use a later control (VPC-SC, Confidential VM, Binary Authorization) as a "known" prop before its `Curriculum` section has been covered (suite-wide rule: `Curriculum` §0.4.6) — postpone the exercise or teach the prerequisite first.
````

**J824** · SEC-12 · anchor-rewrite

````text
4. **GCP lens at three depths** when a concept is taught: **Lens-1** name the GCP (and AWS/Azure twin from `Curriculum` mapping tables) resource; **Lens-2** touch via local vulnerable-by-design fixture or credits-safe lab; **Lens-3** cert-depth trade-offs (Cloud Security Engineer / PCA Security / SCS-C03).
````

**J825** · SEC-12 · anchor-rewrite

````text
11. **User can override** skip/jump. On conflict: `Curriculum` wins on order and cert timing; this file wins on security/crypto content and exercise specs.
````

**J826** · SEC-12 · anchor-rewrite

````text
1. **Anchor** — name the `Curriculum` section (e.g. A10, B5, Phase 4 Security) and list bound companion IDs from §2.
````

**J827** · SEC-12 · anchor-rewrite

````text
## 2. Stitch table — teach these with `Curriculum`
````

**J828** · SEC-12 · anchor-rewrite

````text
| **AWS Security Specialty / Azure SC-100 (later phases)** | same mechanics; map controls via `Curriculum` Part VIII tables — no new theory | — | IR mapping drill |
````

**J829** · SEC-12 · anchor-rewrite

````text
> **Note:** the suite-wide register is `Curriculum` §0.3; this table is the security slice of it, and on a conflict the main course's register wins.
````

**J830** · SEC-12 · anchor-rewrite

````text
| Shared responsibility one-liner | `Curriculum` B1 | PQ-S-03 matrices by service model |
````

**J831** · SEC-12 · anchor-rewrite

````text
| TLS handshake vocabulary | `Curriculum` A5 (mechanics) / A10 (formal) | CR-12 attacks, 0-RTT, validation bugs |
````

**J832** · SEC-12 · anchor-rewrite

````text
| IAM principals/roles | `Curriculum` B5 | CL IAM privesc / key sprawl playbooks |
````

**J833** · SEC-12 · anchor-rewrite

````text
| "Use KMS/CMEK" | `Curriculum` Phase 4 Security | CR-14 envelope hierarchy + compromise IR |
````

**J834** · SEC-12 · anchor-rewrite

````text
| Armor / DDoS product names | `Curriculum` V-NET / Phase 4 Networking | DOS taxonomy + rate-limit/bot design |
````

**J835** · SEC-12 · anchor-rewrite

````text
| Container non-root / PSS | `Curriculum` C1/C2 | CK escape & supply-chain attacker paths |
````

**J836** · SEC-12 · anchor-rewrite

````text
| OAuth/JWT mentioned | `Curriculum` A7 | AU/CR failure modes (alg confusion, mix-up) |
````

**J837** · SEC-12 · anchor-rewrite

````text
1. CR-11 + CR-12 on the `Curriculum` A5 TLS day, at mechanism level, with the minimal public-key intuition bridge (what a key pair does, what a signature proves, why DH gives a shared secret) — CR-E12.
````

**J838** · SEC-12 · anchor-rewrite

````text
*End of The Cloud Cybersecurity Companion. Stitch with `Curriculum`; bank ≠ dump; CR-* is a first-class pillar.*
````

**J842** · GO-13 · anchor-rewrite

````text
- **Build lab (hardened HTTP server):** on a Go `http.Server` set `ReadHeaderTimeout` 5 s, `ReadTimeout` 15 s, `WriteTimeout` 15 s, `IdleTimeout` 60 s and `MaxHeaderBytes` 1 MiB; wrap request bodies in `http.MaxBytesReader`; cap in-flight requests with a semaphore that answers 503 when full (the Python twin sets the same limits in its ASGI server `(verify)` the option names). Against a *local* copy only, run a slow-header client (200 connections, one header byte every 10 s) before and after: before, the workers fill; after, each connection closes at the header timeout. Write the Cloud Run request timeout and the load balancer's backend timeout beside the server values so the three agree.
````

**J843** · GO-14 · anchor-rewrite

````text
- **Build lab (password storage):** register and login endpoints on a local service. Store per user `argon2id$v=19$m=65536,t=3,p=1$<salt>$<hash>` from a vetted library (argon2-cffi, `golang.org/x/crypto/argon2`), with parameters from the current OWASP password-storage guidance `(verify)`, a unique 16-byte random salt per user, and a pepper: HMAC-SHA-256 of the password under a key held in Secret Manager (lab: an environment variable), applied before hashing, with a pepper-version field. Steps: (1) time one hash and tune memory and iterations to about 100 ms on the lab machine; (2) import a table of legacy SHA-256 hashes and upgrade each one on its next successful login (rehash-on-login, version field); (3) rate-limit login per account and per IP (AU-08). Tests: the same password gives different stored strings; a wrong pepper version fails closed; a login for an unknown user takes as long as for a known one (hash a dummy value).
````
