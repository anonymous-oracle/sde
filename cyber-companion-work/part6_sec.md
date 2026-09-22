### 6.11 Network security overlay (NGFW, Armor, IAP, VPC-SC, LB TLS)

This is the **map** of controls you will deepen in 6.12–6.16 and Part 7. Place each control on the packet path; do not invent a seventh product that duplicates another.

#### Concepts
- **Cloud NGFW / hierarchical FW** — org-wide policy, threat intel, FQDN/geo (Enterprise features) — depth in **6.12**.
- **Cloud Armor** — WAF / OWASP / rate-limit / bot on **external Application LB** (global). Pair with CDN lesson in **1.4**; do not re-teach CDN here.
- **IAP** — identity-aware access to apps and SSH/TCP — **6.14**.
- **VPC Service Controls** — perimeter around Google APIs / data to limit exfil — **6.15**.
- **LB TLS** — managed certs, SSL policies (min TLS 1.2+), HTTPS redirect on Application LB — types in **1.12** / **6.13**.
- **DDoS** — GFE absorbs volumetric; Armor adds L7 — **6.16**.

#### From scratch / decision exercise
Draw Northstar packet path and label **one** primary control per hop:
Internet → GFE/Armor → URL map → serverless NEG → Cloud Run → (VPC-SC) → GCS/SQL.

#### HLD
Defense in depth diagram: edge (Armor/LB TLS) → identity (IAP) → network (FW/NGFW) → data (VPC-SC/CMEK).

#### LLD
One-pager ADR: which controls are free-tier / Always Free adjacent vs credits-optional.

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ Diagram-only REQUIRED. Live Armor + global LB = credits.    │
│ Free path: IAP on App Engine/Cloud Run admin (6.14 lab).    │
└─────────────────────────────────────────────────────────────┘
```

#### Gate
- Can place NGFW, Armor, IAP, VPC-SC, LB TLS on a path diagram without overlapping responsibilities wrongly.
### 6.12 Firewall and Cloud NGFW (security depth)

VPC firewall rules (6.4) scale into **hierarchical policies** and **Cloud NGFW**. Same 5-tuple mental model; richer match conditions and org scope.

#### Concepts — GCP offerings
- **VPC firewall rules** — per-network, classic surface (6.4).
- **Hierarchical firewall policies** — org / folder / project attachment; evaluate before or with network rules per product rules.
- **Global network firewall policy / Cloud NGFW** — threat intelligence lists, geolocation, FQDN objects, optional TLS inspection (**Enterprise** — know it exists; do not require paid lab).
- **Implied rules** remain (allow egress, deny ingress). Priority math across layers — draw the evaluation order from current docs when you lab.
- **Targets:** prefer **service accounts** over tags (tags are not authn).
- Intrusion / malware features are NGFW Enterprise territory — PCA literacy, not free-tier dependency.

#### From scratch
- Expand the 6.4 evaluator: multiple layers (org policy deny → VPC allow). Unit tests prove org deny wins.
- **Python then Go:** given rule set + 5-tuple, decide allow/deny. Write Terraform for `google_compute_firewall` and stub `google_compute_network_firewall_policy` resources.

#### Decision exercise

| Control need | Pick |
|---|---|
| One project lab | VPC firewall rules |
| Company-wide SSH deny from internet | Hierarchical policy at org/folder |
| Block known bad IPs / geo | NGFW threat intel / geo (credits) |
| L7 OWASP on public HTTPS | Cloud Armor on Application LB (not NGFW) |

#### HLD
Org policy “deny ingress 22 from `0.0.0.0/0`” + project VPC allows IAP only. Armor sits at edge LB, not as a substitute for VPC FW.

#### LLD
- Priority bands documented (e.g. 1000 deny, 2000 IAP allow, 3000 app allow).
- Logging enabled on deny rules used in IR drills.

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ Unit-test evaluator REQUIRED. Live hierarchical policy may │
│ need org admin — diagram + TF if you lack permission.       │
│ Credits-optional: NGFW Enterprise features — read only.     │
└─────────────────────────────────────────────────────────────┘
```

#### Gate
- 5-tuple tests cover layered deny; Terraform for VPC FW merges clean; can contrast Armor (L7 edge) vs NGFW (L3/4+/org).
### 6.13 Load balancing, TLS, CDN, and the edge

**Dedupe:** the full CDN lesson is **1.4** only. The full HA / LB axis lesson (external vs internal; global vs regional; application vs proxy vs passthrough) is **1.12**. This subsection is the networking-part **pointer + TLS/edge checklist** — do not re-teach CDN modes or rebuild Raft here (Raft → **8.1** / **12.S20**).

#### Concepts
- External vs internal; global vs regional; Application vs Network vs Proxy — **see 1.12 anchors A–D** before any quiz.
- SSL policies, Google-managed certs, HTTPS redirect on Application LB.
- Serverless NEGs (Cloud Run, App Engine, Cloud Functions) behind HTTPS LB.
- Forwarding rule **must** have an IP: ephemeral or reserved static (**6.3** C4/C5). Deleting the rule without deleting a reserved IP leaves a billing leak.
- Cloud CDN enables on the **global external Application LB** (or classic) — modes, keys, signed URLs, invalidation → **1.4**.
- Cloud Armor and reCAPTCHA at this edge; details 1.4 / 4.10.

#### From scratch
- L4/L7 proxies from 1.4 in front of two local backends; weighted round-robin + drain (canary). Map each feature to a GCP LB type using the 1.12 table.

#### HLD
Credits-optional production edge: global external Application LB + managed cert + Armor + CDN → serverless NEG → Cloud Run. Free-tier edge: Firebase Hosting + `run.app` / IAM invoker.

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ Free path: Cloud Run auth / Hosting as the edge.            │
│ Credits-optional: global HTTPS LB + Armor + CDN.            │
│ ALWAYS release reserved static IPs same sitting.            │
└─────────────────────────────────────────────────────────────┘
```

#### Lab
- Cloud Run auth as the free-tier “edge.” Credits-optional: global HTTPS LB + Armor + CDN in front of Cloud Run.

#### Gate
- Can point to 1.12 for LB choice and 1.4 for CDN; can explain managed cert + SSL policy; idle IP leak named.
### 6.14 Zero-trust access

“Inside the VPC” is not a trust tier. Zero trust: authenticate and authorize every request with **identity + device + context**, then least-privilege network paths.

#### Concepts
- **IAP (Identity-Aware Proxy)** for admin UIs and for **IAP TCP** (SSH to VMs without public IP — already used in 6.5).
- Supported surfaces: App Engine, Cloud Run, GKE (via Ingress/Gateway patterns), GCE via IAP TCP.
- **Context-aware access / Chrome Enterprise Premium:** device posture, IP, region — beyond “has Google login.”
- **BeyondCorp model:** identity-aware access to apps; network location is a signal, not the perimeter.
- Pair with Part 4: IAP can use Google identities or Identity Platform identities depending on setup.

#### From scratch / decision exercise

| Access | Prefer | Reject |
|---|---|---|
| Human admin SSH | IAP TCP + OS Login | Public `0.0.0.0/0` SSH |
| Human admin UI | IAP in front of Cloud Run/GAE | VPN-only as sole control |
| Service-to-service | SA + IAM / mTLS mesh later | Flat allow-all subnet |

#### HLD
Users → IAP → admin Cloud Run; attackers on the VPC still fail without identity. VPN optional for legacy, not the only gate.

#### LLD
- IAP-secured Web App User role binding to a group.
- HTTPS LB + IAP brand/OAuth client when using full LB path (credits-optional); free path: App Engine/Cloud Run IAP toggles.

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ Enable IAP on App Engine standard admin service OR Cloud    │
│ Run (per current product support in your project).          │
│ Prove unauthenticated access fails; group member succeeds.  │
│ Credits-optional: context-aware access policies.            │
└─────────────────────────────────────────────────────────────┘
```

#### Lab
- IAP on an App Engine or Cloud Run admin service.

#### Gate
- Unauthenticated denied; group allow works; HLD states VPC ≠ trusted.
### 6.15 Segmentation and exfil controls

Segment so a breach in the storefront cannot read the cardholder data environment (or your customer DB) by default. Exfil controls limit what can leave Google APIs even with stolen credentials.

#### Concepts
- **Separate VPCs or subnets** for CDE vs general (PCI mental model from Part 5) — FW + routing enforce.
- **VPC Service Controls (VPC-SC):** perimeters around projects/services so data cannot be copied to arbitrary projects/internet paths even if IAM is mis-granted. Org-level; diagram required if you cannot enable.
- **Private Service Connect (PSC):** consume services (APIs, published services) via private endpoints without public IPs or full peering mesh.
- **Private Google Access / restricted VIP:** keep API traffic on private paths (ties to 6.2).
- Defense in depth with CMEK / Secret Manager (Part 7) — network is necessary, not sufficient.

#### From scratch / decision exercise
Label Northstar tiers: public FE, private API, private SQL, admin. Which links are PSC vs peering vs Shared VPC?

#### HLD
Northstar network: public frontend (Hosting/LB), private API (no VM public IPs), private Cloud SQL, VPC-SC perimeter sketch around data projects.

#### LLD
- Subnet CIDRs per tier; FW allow only north-south required ports.
- PSC endpoint attachment sketch for a produced API.
- VPC-SC perimeter dry-run mode literacy (prefer dry-run before enforce).

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ HLD + Terraform sketches REQUIRED. Live VPC-SC needs org    │
│ policy admin — credits/org-optional. Free path: two subnets │
│ + FW segmentation on custom VPC (extend 6.5).               │
└─────────────────────────────────────────────────────────────┘
```

#### Gate
- HLD shows segmented tiers; can explain VPC-SC vs IAM vs FW in one paragraph each; PSC vs peering contrast clear.
### 6.16 DNS and DDoS (security view)

Close the networking block by viewing DNS and DDoS as **attack surfaces** and **managed mitigations**, not only as “make the website resolve.”

#### Concepts
- **Cloud DNS security:** DNSSEC for public zones (authenticity); private zones reduce internet exposure of internal names; monitoring for unexpected record changes.
- **DNS attacks literacy:** cache poisoning (why DNSSEC), zone takeover via dangling CNAME/NS, subdomain takeover on abandoned Hosting/LB IPs — release IPs and delete records together (**6.3**).
- **DDoS:** Google Front End / Maglev absorb many volumetric attacks in front of Cloud Load Balancing. **Cloud Armor** adds L7 / WAF / rate-limit for Application LB. You do not build your own scrubbing center on free tier.
- **Billing awareness:** forwarding-rule hours, NAT hours, Armor policies, idle static IPs — free-tier path avoids standing edge SKUs (use Hosting + Run).
- Pointers: CDN/Armor deep content → **1.4**; LB choice → **1.12**; DNS product → **6.10**.

#### From scratch / decision exercise

| Threat | Control |
|---|---|
| Volumetric flood on public HTTPS | GFE + Armor on Application LB |
| Stolen IAM writes evil DNS A | DNS IAM least privilege + alerts |
| Dangling CNAME to deleted Run | Inventory + delete records with services |
| Internal name leak | Private zones only |

#### HLD
Internet noise → GFE → Armor → LB → backends. DNSSEC on public zone. Private DNS not published.

#### LLD
- Checklist: destroy LB ⇒ release IP ⇒ delete DNS A/AAAA.
- Armor preview policy (rate limit) as credits-optional TF.

#### GCP lab (free-tier boxed)
```
┌─ FREE-TIER BOX ─────────────────────────────────────────────┐
│ Checklist drill on paper/TF: create/destroy order for LB+IP │
│ +DNS. No live DDoS testing against Google or third parties. │
│ Credits-optional: Armor rate-limit policy attached to LB.   │
└─────────────────────────────────────────────────────────────┘
```

#### Gate
- Can explain GFE/Armor roles without claiming “GCP is un-DDoS-able”; DNSSEC purpose stated; destroy-order checklist memorized.
