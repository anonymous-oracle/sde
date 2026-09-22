## Part 7 — Cybersecurity (concept + GCP offerings)

**Goal:** Secure software systems, not just a green SCC dashboard. Identity, data, runtime, supply chain, detect, respond.

### 7.1 Security principles


Security here is engineering: assumptions, boundaries, and proof — not a green dashboard.

#### Concepts
- **CIA:** confidentiality, integrity, availability — every control names which letter it serves.
- **Least privilege:** identity gets the minimum role on the minimum resource for the minimum time.
- **Defense in depth:** IAM + network + app authz + data encryption + detection — one layer failing must not equal game over.
- **Assume breach:** design for credential leak and malicious insider; detection + containment (7.6–7.8).
- **Zero trust:** authenticate/authorize every request; no “inside VPC = trusted.” IAP and service IAM embody this on GCP.
- **Shared responsibility:** you — IAM, data classification, app code, who can invoke, logging config; Google — physical, hypervisor, and baseline managed-service hardening. Misconfigured public bucket is on you.
- **Well-Architected security/privacy/compliance pillar:** map Northstar ADRs to these themes for PCA.

#### From scratch (required)
- For one Northstar flow (`PlaceOrder`), write a control matrix: threat → CIA → control → residual risk. Table-test that each abuse case from 3.0 evidence pack maps to at least one control.

#### Lab
- Walk Cloud Architecture Center security overview pages; annotate your Part 0 hierarchy with trust boundaries (org/folder/project).

#### Gate
- Control matrix reviewed; can explain shared responsibility for Cloud Run vs GCE guest OS patching in one paragraph.

#### Decision table
| Instinct | Prefer | Avoid |
|---|---|---|
| Trust the VPC | mTLS / IAM / IAP | Flat allow-all firewall |
| Broad Owner role | Custom/predefined least role | Standing org Owner for deploys |
| “Encrypt later” | CMEK/Secret Manager now for secrets | Secrets in env in images |
### 7.2 Identity and access (GCP offerings)

Part 4 taught customer and workload auth. Here you operate **org-scale** identity and access for PCA 3.1.

#### Concepts
- **Cloud Identity / Workspace:** employees and groups — directory source of truth.
- **Cloud IAM:** resource access; predefined vs custom roles; IAM conditions; deny policies; principal access boundary literacy.
- **Identity Platform:** customers (Part 4) — separate plane from employees.
- **IAP:** human access to apps without VPN; still need app authz.
- **WIF / Workforce Federation:** external workloads and external human IdPs without syncing passwords into Google.
- **Privileged Access Manager (PAM):** just-in-time elevation where available — prefer over standing Admin.
- **Groups, not users:** bind roles to groups; break-glass user monitored and rare.

#### From scratch (required)
- Policy Analyzer-style toy: input bindings JSON + principal + resource → effective allow/deny. Tests: group inheritance; deny beats allow; condition false ⇒ no access.

#### Lab
- Export a project policy dump (`gcloud projects get-iam-policy`); run the toy or Policy Analyzer; remove one over-broad binding in Terraform.
- Document break-glass procedure (who, how long, audit).

#### Gate
- No standing user Owner on prod; WIF for CI (4.8); effective-access exercise checked in.

#### Decision table
| Who | Prefer | Avoid |
|---|---|---|
| Employee admin UI | IAP + group role | Public admin + password only |
| CI deploy | WIF | SA keys |
| Customer login | Identity Platform | Recreating IAM users for customers |
| Emergency | Break-glass + PAM/JIT | Shared root passwords |
### 7.3 Data protection

Protect data at rest, in use (as offered), and in logs. Classification drives the control, not the other way around.

#### Concepts
- **Default encryption at rest** on Google Cloud — necessary, not sufficient for custody requirements.
- **CMEK / CSEK / Cloud KMS / Cloud HSM / Cloud EKM:** customer-managed keys when you need key custody, rotation policy, or regulatory “hold your keys.” CSEK rare; HSM/EKM for higher assurance.
- **Secret Manager:** versioned secrets, IAM per secret, rotation — vs env vars (non-secrets) vs Binary Authorization attestations (provenance, not secret storage).
- **Sensitive Data Protection (DLP):** inspect, de-identify, infoTypes, templates — use before BQ/notebook exports and before prompts (9b/9c).
- **GCS:** uniform bucket-level access, public-prevention org policy, VPC-SC for exfil-resistant perimeters (6.15).

#### From scratch (required)
- Envelope-encryption toy: generate data key, “wrap” with a master key in a local file (stdlib Fernet or AES from a vetted lib — **do not invent crypto**). Tests: rotate master → rewrap; decrypt fails with wrong key. Name substitute: KMS + CMEK.

#### Lab (free-tier boxed)
1. Create a KMS key ring/key (KMS Free Tier: note Autokey free-tier nuances on official pricing — destroy unused key versions).
2. CMEK on a GCS bucket **or** encrypt a single field with KMS before SQL insert.
3. Secret Manager for Stripe + DB URLs; access logged; no secrets in Cloud Run env YAML checked into Git.
4. DLP inspect on a **synthetic** order export sample (or local sample payloads if API cost is a concern).

#### Gate
- Secrets inventory exists; CMEK or field encryption path demonstrated; public bucket org policy planned in 7.7; DLP infoTypes listed for PII fields.

#### Decision table
| Data | Prefer | Avoid |
|---|---|---|
| API keys / PSP secrets | Secret Manager + IAM | .env in image |
| Regulated object store | CMEK + uniform access | Public ACL “temporary” |
| Analytics export | DLP de-identify | Raw PII to shared BQ |
### 7.4 Application and API security

OWASP-shaped bugs are how GCP-perfect IAM still loses data. Fix them in the app and in tests.

#### Concepts
- **OWASP API Top 10** mapped onto Cloud Run + Identity Platform + SQL: BOLA/BFLA, broken auth, unconstrained resources, injection, misconfig, SSRF, etc.
- **Input validation & output encoding:** allowlists; parameterized SQL; context-aware HTML/JSON encoding.
- **CSRF** for cookie sessions (4.4); **SSRF** — block link-local / metadata IPs; on GCE disable unnecessary default SA scopes; prefer Cloud Run where metadata model is tighter.
- **GCE metadata** (`169.254.169.254`): classic SSRF target for SA tokens — teach detection and prevention on a **local** vulnerable app only.
- **Hard bans:** no scanning third-party systems; no malware; vulnerable-by-design local apps only (Pedagogy).

#### From scratch (required)
- Deliberately weak local API fixtures: missing object authz, string-built SQL, open redirect. Write exploits **against localhost** then fixes; tests that fail on the weak version and pass on the fixed one.
- SSRF guard: URL parse + deny private/link-local/metadata ranges before `fetch`.

#### Lab
- Re-test Northstar handlers with negative authz matrix (4.9 L1).
- Parameterized queries only on Part 2 schema; fuzz one endpoint with bounded corpus.

#### Gate
- Weak fixtures not deployed; authz matrix green; SSRF guard tested; no production scan tooling aimed outside your project.

#### Decision table
| Risk | Prefer | Avoid |
|---|---|---|
| Object authz bugs | Explicit `(principal, action, resource)` checks | “Hidden URL” security |
| SQL injection | Bound parameters | String concat |
| SSRF | Allowlist egress / block metadata | Fetch user URLs raw |
### 7.5 Workload and supply chain

If the build pipeline lies, runtime IAM cannot save you. Provenance and minimal runtime privilege are required.

#### Concepts
- **Artifact Registry:** store images; enable vulnerability scanning; promote digests, not `:latest` alone.
- **Binary Authorization:** admit only attested images to GKE/Cloud Run (as supported); attestations from Cloud Build.
- **SLSA:** levels as a maturity story — hermetic builds, provenance, verified source.
- **Shielded VM / Secure Boot / vTPM:** GCE integrity literacy for bastions and stateful VMs.
- **Container contract:** non-root, read-only root FS, drop capabilities, no secret files in layers (Part 1.2 / D5).

#### From scratch (required)
- Makefile/`cosign`-shaped toy: hash a tarball; write `attestation.json` with builder id + source commit; verifier checks hash + builder allowlist. Tests: tampered artifact fails.

#### Lab (free-tier boxed)
1. Build Northstar image to Artifact Registry (0.5 GB free storage — prune).
2. Scan image; **fail the build** on CRITICAL (policy in Cloud Build).
3. Document Binary Authorization plan for GKE path (9.2); Cloud Run digest pins in Terraform.
4. Prove image runs as non-root in Cloud Run/local.

#### Gate
- CRITICAL fails CI; digest pinned in deploy config; attestation toy green; no SA keys in image layers (`docker history` / scan).

#### Decision table
| Stage | Prefer | Avoid |
|---|---|---|
| Store | Artifact Registry + scan | Random Docker Hub prod pulls |
| Deploy | Digest + BinAuth/attestation | Mutable `:latest` only |
| Runtime | Non-root, RO FS | Root + docker.sock |
### 7.6 Detection and posture
GCP offerings:
- **Cloud Audit Logs** (admin, data access, system).
- **Security Command Center** (Standard / Premium / Enterprise) — findings, mute rules, attack path, security health analytics.
- **Web Security Scanner**.
- **Cloud IDS**.
- **Google SecOps / Chronicle** (concept; cost).
- **Assured Workloads** (compliance perimeters).

**SCC runbook template (copy into Northstar `runbooks/scc.md`):**
1. **Detect:** SCC finding or log-based alert fires (`category`, `severity`, `resourceName`).
2. **Triage (15 min):** confirm resource project/folder; check mute rules; ask “active exploit vs misconfig?”
3. **Contain:** IAM deny / remove public ACE / disable key / close firewall; snapshot disks if GCE compromise suspected.
4. **Eradicate:** fix Terraform; rotate secrets; redeploy clean revision.
5. **Recover:** verify SLO; re-enable traffic canary.
6. **Lessons:** file finding → ticket; add regression test or org policy; update mute only with justification.
- **Lab:** parse audit logs; alert on `SetIamPolicy` and `serviceAccount.keys.create`. Wire one SCC-style finding (even exported JSON) through the template. **Python / Go.**

### 7.7 Org policy and landing zone
- `iam.disableServiceAccountKeyCreation`, `compute.vmExternalIpAccess`, resource locations, uniform bucket access, `sql.restrictPublicIp`, domain restricted sharing as applicable.
- Security baseline for orgs created after 2024-05-23.
- Landing zone: identity, hierarchy, network, security — now you have the product to put in it.

**Org policy change runbook template (`runbooks/org-policy.md`):**
1. **Propose:** policy constraint + desired value + blast radius (org/folder/project).
2. **Dry-run:** list resources that would violate; owners notified.
3. **Stage:** apply at folder `nonprod` first; break-glass project tagged.
4. **Enforce:** promote to `prod` folder; monitor SCC / Policy Controller rejects for 72h.
5. **Rollback:** keep previous policy JSON in Git; `gcloud org-policies set-policy` from last good.
- **Lab:** write Terraform `google_org_policy_policy` for key-creation disable + uniform bucket access (apply only if you own an org; otherwise plan-only).

### 7.8 Incident response
**Four required runbook templates** (same headings: Detect → Contain → Eradicate → Recover → Comms → Follow-up):

1. **Leaked GitHub token / WIF misbind** — revoke OAuth/PAT; invalidate WIF attribute conditions; rotate; audit `CreateServiceAccountKey` / GitHub Actions logs; notify if repo public.
2. **Leaked Stripe webhook secret** — roll secret in Stripe + Secret Manager versions; reject old signing secret; replay-safe inbox check; customer impact = none if only signing secret.
3. **Public bucket / public object ACE** — remove `allUsers`; enable uniform access + org policy; scan object listing; SDP if PII; customer notification if exposure confirmed.
4. **Compromised SA** — disable SA; kill keys; check last auth in audit logs; rotate workloads to new SA; forensics on caller IP / `principalEmail`.

- **Tabletop:** 60 min clock; facilitator injects one of the four; scribe fills the template; grade = time-to-contain + whether restore was tested.
- **Exercise:** commit all four runbooks next to Northstar; run one tabletop.

### 7.9 Compliance mapping

Compliance is evidence + scope + location — mapped onto controls you already built — not a sticker on the README.

#### Concepts
- **Commercial / privacy:** PCI (Part 5), PII handling, SOC 2 / ISO 27001 evidence posture (your logs, access reviews, change control).
- **Healthcare / children’s / sovereignty:** HIPAA BAA with Google; Assured Workloads; `resourceLocations` org policy; children’s data extra care — do not invent legal advice; map to products.
- **Evidence:** Cloud Audit Logs retained; access reviews; Compliance Reports Manager for **Google’s** attestations vs **your** control evidence.
- **PCA 3.2** themes: legislation classes; PCI/PII; SOC 2; audits/logs.

#### From scratch (required)
- Compliance matrix spreadsheet/markdown: obligation → Northstar control → GCP product → evidence artifact path → gap. Unit-ish test: required rows present (PCI, PII, residency, audit).

#### Lab
- Pull or screenshot Compliance Reports Manager path (org-dependent); store procedure in `runbooks/compliance.md`.
- Set (or plan-only Terraform) `resourceLocations` for a nonprod folder.

#### Gate
- Matrix complete for PCI + PII + residency; no “we’ll be careful” as a PHI plan; audit log retention called out in 10.0/7.6.

#### PCA: 3.2 Compliance design

**Guide themes (matrix):** health/children’s/privacy/sovereignty legislation; PCI/PII commercial; SOC 2; audits/logs. Homes: 5, 7.9.

| Obligation | Prefer | Accept |
|---|---|---|
| PHI | BAA + Assured Workloads / location policy | DIY “we’ll be careful” |
| PCI | Tokenize; CDE segmentation (Part 5) | Store PAN in GCS |
| Sovereignty | `resourceLocations` + regional resources | Global bucket “for simplicity” |
| Evidence | Audit logs retained + access reviews | Screenshots only |

**Scenario prompt:** EU autonomous-driving data and a US analytics team want one global BQ dataset.

**Expected answer shape:** “I pick EU regional processing + Assured Workloads because Y, I accept Z (aggregated non-personal exports only).”
