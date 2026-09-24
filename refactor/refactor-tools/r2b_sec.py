"""R2b per-file rules for the cloud cybersecurity companion. Learner decisions D5, D6, D7, D9, D10, D11.

Every Northstar pointer (N…) is replaced by the module that now holds the material. Where the pointer named a
Northstar product lab that exists nowhere else in the course, the lab is written into the owning module here as a
"Build lab" bullet (D9, D11: a pointer to a place lacking the material is a material dependency). The nine
checkpoint cards the §2 table names each become full cards: a check question on the card and a key in Appendix K
(D9). "The reference app" is defined once in §0.4 and its broken R2 wording is repaired.
"""
import re

from r2b_shared import contract_copy, parent_name

EV5 = "D5: Northstar and every N pointer are deleted; the pointer now names the module that holds the material"
EV6 = "D6: no file names, links or file dependencies in course text"
EV9 = "D9 + D11: the pointed-to Northstar lab exists nowhere else in the course, so it is written into its owner here"
EV9C = "D9: the checkpoint card becomes a full card (scenario, prediction, design, check, key)"
EV11 = "D11: the file-style parent name becomes 'the main course'; IDs stay as stitch tags"
EVR = "D5: the Northstar name's R2 stand-in 'the reference cloud app' is defined once (§0.4) and reads as English"

# where each old Northstar section's material lives now (first entry is used when none is already on the line)
NMAP = {
    "N0": ["B5"], "N0.4": ["TH-02"], "N2.3": ["SQL OD-11"], "N3.0": ["A7"], "N4.2": ["CL-01", "DOS-05"],
    "N4.3": ["CR-13"], "N4.4": ["AU-03", "AU-04", "WA-01"], "N4.5": ["AU-05", "CR-06"], "N4.6": ["AU-06"],
    "N4.7": ["AU-11"], "N4.8": ["AU-14", "CL-04"], "N4.9": ["CK-04", "WL-05"], "N4.10": ["AB-01", "AB-02"],
    "N5": ["PV-03"], "N5.3": ["SQL DD-03"], "N6.11": ["NT-07"], "N6.12": ["NT-02"], "N6.13": ["CR-12", "AB-02"],
    "N6.14": ["NT-05"], "N6.15": ["NT-06"], "N6.16": ["NT-04", "DOS-03", "WA-11"], "N7.1": ["PQ-S-02"],
    "N7.2": ["CL-03"], "N7.3": ["CR-14"], "N7.4": ["WA-05", "TH-03"], "N7.5": ["WL-04"], "N7.6": ["IR-04"],
    "N7.7": ["CL-02"], "N7.8": ["IR-05"], "N7.9": ["CM-01"], "N8.1": ["SQL OD-09"], "N9c": ["AI-01", "D3"],
    "N10": ["C6"], "N10.3": ["B4"],
}
NTOK = re.compile(r"^N\d+(?:\.\d+)*[a-c]?$")


def _map_line(m):
    head, items = m.group(1), [x.strip() for x in m.group(2).split(",")]
    keep = [x for x in items if not NTOK.match(x)]
    out = []
    for x in items:
        if not NTOK.match(x):
            out.append(x)
            continue
        if x not in NMAP:
            raise SystemExit(f"cyber: no mapping for {x!r} in {m.group(0)!r}")
        if not any(c in keep or c in out for c in NMAP[x]):
            out.append(NMAP[x][0])
    return head + ", ".join(dict.fromkeys(out))


REF_APP = (
    "- **The reference app** — the one application every scenario, lab and capstone in this part threat-models: an "
    "online shop at `shop.example`. A storefront (sessions, catalog, carts) and a customer API (orders, customer data, "
    "payment tokens) run on Cloud Run behind a global external Application Load Balancer with Cloud Armor; an admin "
    "console for refunds and configuration sits behind IAP; services call each other under service-account identity; "
    "data lives in Cloud SQL for PostgreSQL (orders, the payments ledger, customers — the same storefront data as the "
    "SQL companion's lab), Cloud Storage (product media, invoices, exports) and BigQuery (analytics), with Pub/Sub "
    "between services; a CI/CD pipeline builds with Cloud Build into Artifact Registry; and an AI gateway on Vertex AI "
    "has tools and a RAG corpus. Appendix N lists each plane's assets, attackers and modules. The main course teaches "
    "the products; each module's Lens-2 lab builds the piece it needs locally, so the app never has to exist in the "
    "cloud for the security work.")

LABS = {
    "CR-06 · ": [
        "- **Build lab (signed requests):** in a local service, the client signs `METHOD\\nPATH\\nTIMESTAMP\\n"
        "SHA-256(body)` with HMAC-SHA-256 under a per-client key (Secret Manager in the cloud; an environment "
        "variable in the lab). The server recomputes the tag, compares with a constant-time compare "
        "(`hmac.compare_digest` / `subtle.ConstantTimeCompare`), rejects timestamps more than 5 minutes off and keeps "
        "a short replay cache of seen tags. Tests: one flipped body byte fails; a replay inside the window fails; a "
        "naive `==` compare is replaced, with the reason written down (CR-16)."],
    "CR-13 · ": [
        "- **Build lab (password storage):** register and login endpoints on a local service. Store per user "
        "`argon2id$v=19$m=65536,t=3,p=1$<salt>$<hash>` from a vetted library (argon2-cffi, "
        "`golang.org/x/crypto/argon2`), with parameters from the current OWASP password-storage guidance `(verify)`, a "
        "unique 16-byte random salt per user, and a pepper: HMAC-SHA-256 of the password under a key held in Secret "
        "Manager (lab: an environment variable), applied before hashing, with a pepper-version field. Steps: (1) time "
        "one hash and tune memory and iterations to about 100 ms on the lab machine; (2) import a table of legacy "
        "SHA-256 hashes and upgrade each one on its next successful login (rehash-on-login, version field); (3) "
        "rate-limit login per account and per IP (AU-08). Tests: the same password gives different stored strings; a "
        "wrong pepper version fails closed; a login for an unknown user takes as long as for a known one (hash a dummy "
        "value)."],
    "CR-14 · ": [
        "- **Build lab (envelope encryption, then CMEK):** (1) Locally with Tink: a KEK keyset stands in for a Cloud "
        "KMS key. For each record, generate a fresh AES-256-GCM DEK, encrypt the record, wrap the DEK with the KEK and "
        "store `{wrapped_dek, kek_version, ciphertext}` (Tink carries the nonce inside the ciphertext). Rotate the "
        "KEK and rewrap every DEK without touching any ciphertext; show that a stolen table without access to the KEK "
        "yields ciphertext only. (2) On credits, if Lab Reality allows: create a key ring and a symmetric key in Cloud "
        "KMS; grant `roles/cloudkms.cryptoKeyEncrypterDecrypter` on that key to the Cloud Storage service agent only; "
        "create a bucket whose default key is that CMEK; upload an object; disable the key version and watch reads "
        "fail; re-enable; tear down (key versions are scheduled for destruction, not deleted at once `(verify)`). "
        "Separation of duties: whoever administers keys (`roles/cloudkms.admin`) is not whoever uses them."],
    "AU-03 · ": [
        "- **Build lab (sessions, cookies, CSRF — also serves AU-01, AU-02, AU-04):** on a local service, opaque "
        "128-bit session IDs from a CSPRNG, stored server-side (a local Redis or an in-memory map) with an idle and an "
        "absolute timeout; the cookie is `__Host-sid; Secure; HttpOnly; SameSite=Lax; Path=/`; the ID is regenerated "
        "on login and on every privilege change; a per-session CSRF token is checked on every POST, PUT, PATCH and "
        "DELETE, together with a Fetch Metadata check (refuse `Sec-Fetch-Site: cross-site` on state-changing routes) "
        "and an Origin allowlist. Tests: a cross-site form POST from a second local origin fails; after login no "
        "pre-login session ID works; logout invalidates the session server-side; no GET changes state."],
    "AU-11 · ": [
        "- **Build lab (object AuthZ):** a local orders API with two tenants and three users. Write the negative "
        "matrix first (each user × each action × someone else's order → 404 or 403) as failing tests. Then add one "
        "policy decision point, `authorize(subject, action, resource)`, that every handler calls, and put the tenant "
        "in every query (`WHERE tenant_id = $1 AND id = $2`). The tests go red → green; add one for batch export and "
        "one for a list endpoint (AB-05). Putting IAP or a valid JWT in front changes none of the results, and that "
        "is the lesson."],
    "DOS-05 · ": [
        "- **Build lab (hardened HTTP server):** on a Go `http.Server` set `ReadHeaderTimeout` 5 s, `ReadTimeout` "
        "15 s, `WriteTimeout` 15 s, `IdleTimeout` 60 s and `MaxHeaderBytes` 1 MiB; wrap request bodies in "
        "`http.MaxBytesReader`; cap in-flight requests with a semaphore that answers 503 when full (the Python twin "
        "sets the same limits in its ASGI server `(verify)` the option names). Against a *local* copy only, run a "
        "slow-header client (200 connections, one header byte every 10 s) before and after: before, the workers fill; "
        "after, each connection closes at the header timeout. Write the Cloud Run request timeout and the load "
        "balancer's backend timeout beside the server values so the three agree."],
    "CL-01 · ": [
        "- **Build lab (SSRF guard):** a local `/fetch?url=` endpoint, and a fake metadata server on a local address "
        "that answers `/computeMetadata/v1/instance/service-accounts/default/token` only when the request carries "
        "`Metadata-Flavor: Google`. Write the guard: allow only `https` and an allowlist of hosts; resolve the name "
        "once and reject private, loopback and link-local addresses (169.254.0.0/16, which holds 169.254.169.254) and "
        "their IPv6 equivalents; connect to the *resolved* address, with no second lookup (DNS rebinding); turn "
        "redirects off or re-check every hop; cap response size and time. Tests: the metadata URL, the same address "
        "in decimal (`http://2852039166/`), a redirect to it and a rebinding name all fail; an allowlisted host "
        "passes. Say why the header requirement is no defense once the attacker controls the request's headers."],
    "WL-04 · ": [
        "- **Build lab (toy attestation):** locally, build an image (or any artifact) and take its SHA-256 digest; "
        "sign `{digest, builder, source_commit, time}` with an Ed25519 key (Tink or libsodium) and write "
        "`attestation.json`. A deploy script admits a digest only when a valid signature from the trusted attestor "
        "key exists for exactly that digest. Tests: re-tagging the same digest still passes; a rebuild with one "
        "changed byte fails; a signature from an unknown key fails; a break-glass flag deploys but writes an audit "
        "line. Then name each piece's Binary Authorization counterpart: attestor, attestation, policy, dry-run, "
        "break-glass."],
    "IR-05 · ": [
        "- **Runbook template (fill one per incident; SEC-E7.2 and SEC-CAP2 use it):** **Detect** — the signal, the "
        "time, who saw it. **Scope** — which principals, keys and projects; the usage window from audit logs. "
        "**Contain** — disable the key or the service account first; revoke sessions; block egress if needed. "
        "**Eradicate** — delete the keys, remove the bindings, rotate every secret the principal could read, rewrap "
        "DEKs if a KEK was exposed (CR-15). **Recover** — redeploy the workloads on keyless identity (Workload "
        "Identity, Workload Identity Federation) and verify. **Follow-up** — timeline, root cause, the control that "
        "would have stopped it (for example the org policy that blocks key creation, "
        "`iam.disableServiceAccountKeyCreation` `(verify)`) and the alert that would have caught it earlier. Every "
        "step records who, when, and the evidence path."],
}

CHECKS = {
    "SEC-Z0.5 · ": "- **Check:** Why does the answer for the guest-OS CVE flip if the batch worker moves to Cloud Run, "
                   "and why does the SQL injection never flip?",
    "SEC-E3.1 · ": "- **Check:** Name the one binding whose removal breaks the path, and the audit-log entries that "
                   "would have shown it being used.",
    "SEC-E3.5 · ": "- **Check:** Why does pinning the algorithm in the verifier fix the bug, while rotating the RSA key "
                   "does not?",
    "SEC-E4.3 · ": "- **Check:** One tenant has 200 users behind a single NAT address. Which key order keeps them "
                   "working, and what is the per-IP limit still for?",
    "SEC-E4.16 · ": "- **Check:** Why does an Adaptive Protection alert not stop the attack by itself, and what has to "
                    "happen next?",
    "SEC-E4.21 · ": "- **Check:** Why is \"delete the service, then the DNS record\" the wrong order, and what does "
                    "the attacker gain beyond defacement?",
    "SEC-E6.5 · ": "- **Check:** Why does pinning a digest not make the image safe by itself, and what does the scan "
                   "gate add?",
    "SEC-E6.8 · ": "- **Check:** Why are `list` and `watch` on secrets as dangerous as `get`?",
    "SEC-E10.7 · ": "- **Check:** Why does a firewall rule allowing `10.0.0.0/8` into the sensitive tier amount to "
                    "trusting every service project, including ones added later?",
}

KEYS = {
    "- **SEC-E1.3:**": [
        "- **SEC-Z0.5:** Guest-OS CVE on GCE — customer (IaaS: the guest OS is yours; patch with OS patch management "
        "or rebuild from a patched image). SQL injection in the Cloud Run API — customer on every service model "
        "(code and queries are always yours; WA-05). `allUsers` on a bucket — customer (access configuration is "
        "yours even on a managed store; remove the grant, enforce public access prevention, IR-06). Stolen disk from "
        "a Google data centre — Google (physical security, default encryption at rest). Check: on Cloud Run Google "
        "patches the host and the managed runtime, so the OS CVE moves to the provider except for the packages in "
        "your own image; application code is the customer's under IaaS, PaaS, serverless and SaaS alike (PQ-S-03)."],
    "- **SEC-E3.10:**": [
        "- **SEC-E3.1:** Whoever can change the CI pipeline, or holds the CI service account's key, can act as the "
        "deploy SA (`iam.serviceAccounts.actAs`) and so holds `roles/owner` on prod: full takeover, including "
        "granting themselves more. Break it: take `owner` off the deploy SA and give it only the deploy roles it needs "
        "(for Cloud Run, a deploy role plus `actAs` on the one runtime SA); grant `actAs` on a single SA, never "
        "project-wide; make CI keyless with Workload Identity Federation and attribute conditions on repository and "
        "branch. Check: the binding to remove is the CI SA's `actAs` on the owner-level deploy SA (or that SA's "
        "`owner` role). Evidence: Admin Activity audit logs record `SetIamPolicy`; token minting through "
        "impersonation is recorded by the IAM Service Account Credentials API's Data Access logs when they are "
        "enabled `(verify)`; IAM Recommender and Policy Analyzer show the excess grant.",
        "- **SEC-E3.5 (check):** The forgery uses the public key, which is public by design: rotating it hands the "
        "attacker the new one. Only refusing header-chosen algorithms, and binding each key to exactly one algorithm, "
        "removes the confusion (CR-10)."],
    "- **SEC-E4.15:**": [
        "- **SEC-E4.3 (check):** Key by tenant first, then by user. A per-IP limit sized for one user would throttle "
        "the whole NAT pool, so the IP limit stays as a coarse, higher ceiling at the edge (Cloud Armor) against "
        "unauthenticated floods (AB-02, SEC-E9.1).",
        "- **SEC-E4.16:** Each bot address stays at 30 requests a minute, far under a 600-a-minute per-IP ban, yet "
        "20,000 addresses make 600,000 a minute: a static per-IP limit cannot see a distributed L7 flood. Adaptive "
        "Protection learns a backend service's normal traffic and, on an anomaly, raises an alert with an attack "
        "signature and a suggested rule, with its estimated effect on normal traffic. ADR: enable it on the "
        "internet-facing backend services behind the global external Application Load Balancer; review suggested "
        "rules in preview mode first; keep application-level per-tenant limits (AB-01) for business abuse. Check: "
        "the alert only detects and suggests; a person deploys the rule, or the auto-deploy option does if it was "
        "configured `(verify)` availability and tier.",
        "- **SEC-E4.21:** The name still resolves to a target the organisation no longer controls. Whoever claims it "
        "serves content on a trusted subdomain: phishing under the brand, cookies scoped to the parent domain read or "
        "set (session fixation, AU-02, SEC-E9.3), CORS or CSP allowlists that trust `*.shop.example`, OAuth redirect "
        "URIs registered on that host. Destroy order: remove or repoint the DNS record first, then release the "
        "resource; compare DNS records against live resources on a schedule; never allowlist wildcard subdomains for "
        "cookies, CORS or redirects. Whether a stranger can claim a given target depends on the provider's ownership "
        "checks (Google-hosted custom domains and domain-named buckets require domain verification `(verify)`); the "
        "claimable classics are a CNAME to a deleted third-party SaaS app and an A record to a released external IP. "
        "Check: deleting first opens a window, possibly permanent, in which the record points at a claimable target; "
        "the gain is the domain's trust, not just its page."],
    "- **SEC-E6.6:**": [
        "- **SEC-E6.5:** `FROM node:latest` pulls whatever the tag points at on each build: a compromised or changed "
        "upstream enters prod unreviewed, and builds are not reproducible. Control: pin by digest "
        "(`FROM node@sha256:…`); mirror approved base images into Artifact Registry; scan with Artifact Analysis and "
        "fail the build on critical findings; rebuild on a schedule to pick up patched digests; admit only attested "
        "images (WL-04). Check: a digest pins exactly what you reviewed, including its vulnerabilities and anything "
        "malicious already in it; the scan gate and the update cadence decide whether that pinned content is "
        "acceptable.",
        "- **SEC-E6.8:** A Role with `resources: [secrets]` and `verbs: [\"*\"]` lets every subject bound to it read "
        "every Secret in the namespace (service-account tokens, database passwords) and create, change or delete "
        "them; the same rule in a ClusterRole bound cluster-wide exposes every namespace. Blast radius: every "
        "workload's credentials in scope, then lateral movement to Cloud SQL, third-party APIs and the API server. "
        "Control: least verbs on named resources (`resourceNames`), one Kubernetes service account per workload, "
        "Workload Identity instead of key Secrets, Secret Manager (CSI driver) for application secrets, "
        "`kubectl auth can-i --list` audits, and a policy (Policy Controller or Gatekeeper) that forbids wildcard "
        "verbs on secrets. Check: `list` and `watch` return whole Secret objects, data included, so the attacker "
        "never needs to know a name."],
    "- **SEC-Z0.11:**": [
        "- **SEC-E10.7:** A flat allow across a Shared VPC, or broad peering, makes every service project's workload a "
        "network peer of the sensitive tier: one compromised low-value service reaches it directly (NT-02). Controls: "
        "put the sensitive tier in its own subnets and project with deny-by-default firewall policies; allow only "
        "named service accounts or secure tags on named ports; expose the tier to consumers through Private Service "
        "Connect instead of routing; grant Shared VPC subnet use per service project on named subnets only; log with "
        "VPC Flow Logs and firewall rules logging; add VPC-SC against API-level exfiltration (NT-06). Check: "
        "`10.0.0.0/8` covers every internal range the host project serves, so any service project attached later "
        "inherits access silently — trust creep by default."],
}


def _after_in_card(f, head_prefix, field, new, rule, ev, cls="new-content", span=12):
    h = f.heading(head_prefix)
    for i in range(h + 1, min(h + span, len(f.L))):
        if f.L[i].startswith(field):
            f.ins(rule, i + 1, new, ev, cls=cls)
            return
        if f.L[i].startswith("#"):
            break
    raise SystemExit(f"cyber {rule}: no {field!r} line under {head_prefix!r}")


def build(f, files):
    R = lambda rule, old, new, ev, n=1: f.rep(rule, "anchor-rewrite", old, new, ev, n=n)  # noqa: E731

    # title block, §0
    f.line("SEC-1", "anchor-rewrite", "**Companion to [`Curriculum`](./Curriculum.md)** (the cloud mastery",
           '**Companion to the main course, "The Consolidated Cloud Mastery Curriculum"** (the cloud mastery / '
           'certification roadmap).', EV6 + "; " + EV11)
    R("SEC-1", "the Suite Session Protocol in `Curriculum` §0.4 governs.",
      "the Suite Session Protocol (rule 0.4.2 in §0.7) governs.", EV6 + " (the contract is copied into §0.7)")
    f.line("SEC-2", "anchor-rewrite", "- `Curriculum` IDs: module IDs (`A5`, `A7`",
           ["- Main-course IDs: module IDs (`A5`, `A7`, `A10`, `B1`, `B5`, `C1`, `C2` …), Part V category IDs "
            "(`V-NET`, `V-SEC` …), `Phase 4 Networking` / `Phase 4 Security`, the reserved tracks (`M`, `U`, `S`; "
            "scope stubs in the main course), and cert names (PCA, Cloud Security Engineer, …). IDs from the other "
            "companions keep their own prefixes and are named with their part, e.g. SQL DD-03, SQL OD-11.", REF_APP],
           EV5 + "; " + EV6 + "; " + EVR)

    # the reference app: R2's stand-in wording repaired
    R("SEC-3", "| the reference cloud app evidence sketch |", "| Reference-app evidence sketch |", EVR)
    for pat, repl in [
            (r"\b([Oo]ne|[Tt]hree|[Ff]ive|[Ee]ight) the reference cloud app\b", r"\1 reference-app"),
            (r"\b([Aa]) the reference cloud app\b", r"\1 reference-app"),
            (r"\ban expensive the reference cloud app\b", "an expensive reference-app"),
            (r"\bfor early the reference cloud app\b", "for an early reference app"),
            (r"\bannotate existing the reference cloud app HLD\b", "annotate the reference app's existing HLD"),
            (r"Domain=\.the reference cloud app\.example", "Domain=.shop.example"),
            (r"(· L1 · |SEC-CAP1 · )the reference cloud app\b", r"\1Reference-app"),
            (r"\*\*the reference cloud app link:\*\*", "**Reference-app link:**"),
            (r"OWASP map the reference cloud app\b", "OWASP map of the reference app"),
            (r"the reference cloud app (?=(?:detections|keys|crypto|admin|fields|controls|evidence|path)\b)",
             "the reference app's "),
            (r"(\*\*Scenario:\*\* )the reference (?:cloud )?app\b(?:'s)?", lambda m: m.group(1) + "The reference app" + ("'s" if m.group(0).endswith("'s") else ""))]:
        f.rx("SEC-3", "anchor-rewrite", pat, repl, EVR, mn=1)
    R("SEC-3", "the reference cloud app ledger invariants (N5.3). Lens-2: race test.",
      "the ledger invariants of SQL DD-03 (double entry, append-only, one idempotency key per payment). Lens-2: race "
      "test — two concurrent redemptions of the same single-use coupon against a local database: with read-then-write "
      "both succeed; with a conditional `UPDATE … WHERE redeemed = false RETURNING …` or a unique constraint, one "
      "does.", EV5 + "; D7: ledger invariants have one home, SQL DD-03; this module owns the abuse")
    R("SEC-3", "9. **Built** 2026-09-22 for the reference cloud app / `Curriculum` pairing.",
      "9. **Built** 2026-09-22 for the reference app and the main course.", EVR + "; " + EV11)
    f.rx("SEC-3", "anchor-rewrite", r"\bthe reference cloud app\b", "the reference app", EVR, mn=1)

    # §2 intro and header
    f.line("SEC-4", "anchor-rewrite", "*Generated from the §6.2 crosswalk (2026-09-24).*",
           "Every concept module appears once as primary; secondary anchors are previews, recalls or Lens-3 passes. "
           "The Checkpoint column names the card to run once the module and its stitched concepts are done; each is "
           "a full card in §5 (scenario, prediction, design, check) with its key in Appendix K. VPC-SC is NT-06.",
           EV6 + "; D3 archive and refactor bookkeeping leave course text; " + EV9C)
    R("SEC-4", "| `Curriculum` anchor | Taught here", "| Main-course anchor | Taught here", EV11)

    # §3.3 cryptography: the product labs now live in the owning modules
    f.line("SEC-5", "anchor-rewrite", "*Equal scale to AU/AB/CL. `Curriculum` A7 (API auth patterns) + A10 own",
           "*Equal scale to AU/AB/CL. A7 (API auth patterns) and A10 name the password and JWT products; the build "
           "labs are here — CR-13 (passwords), AU-05 (JWT policy), CR-14 (KMS and CMEK) — and CR owns the "
           "cryptographic justification and failure modes. Stanford CS255 alignment: see §0.5.*", EV5 + "; " + EV9)
    R("SEC-5", "Lens-1: signed requests in N4.5 use HMAC — recall roadmap lab; CR adds composition rules.",
      "Lens-1: signed requests (HMAC over method, path, time and body hash) — the build lab below; CR adds the "
      "composition rules.", EV5)
    R("SEC-5", "*Roadmap N4.3 owns product labs.* CR adds: threat model", "CR owns the whole story here, build lab "
      "included: threat model", EV5)
    R("SEC-5", "Lens-2: recall N4.3 Argon2id lab — add threat-model paragraph.",
      "Lens-2: the Argon2id build lab below, plus a threat-model paragraph.", EV5)
    R("SEC-5", "*N7.3 owns CMEK lab.* CR adds: hierarchy diagram", "CR owns the hierarchy and the CMEK procedure "
      "(build lab below): hierarchy diagram", EV5)
    R("SEC-5", "Lens-2: local envelope toy from N7.3 + hierarchy labels.",
      "Lens-2: the local envelope build lab below, with hierarchy labels.", EV5)
    f.line("SEC-5", "anchor-rewrite", "**Prop Lock for crypto props:** do not use Cloud HSM",
           "**Prop Lock for crypto props:** do not use Cloud HSM, EKM, Confidential Space, or Binary Authorization as "
           "assumed props before their modules are unlocked (CR-14 and CR-18 for keys and confidential computing, "
           "WL-04 for Binary Authorization). Local AEAD/HMAC toys may use Tink without those props.", EV5)
    f.line("SEC-5", "anchor-rewrite", "**Pairing rule with A7 (API auth patterns) + A10 & N7.3:**",
           "**Pairing rule with A7 (API auth patterns), A10 and Phase 4 Security:** the main course names the "
           "password, JWT and KMS products; the labs are CR-13 (password storage), AU-05 (JWT policy) and CR-14 "
           "(envelope and CMEK). CR-13/CR-10 own the cryptographic *why* and failure modes; CR-14 owns hierarchy "
           "theory and separation of duties. Teach as one story per §2 stitch rows.", EV5)
    R("SEC-5", "(password/KDF day; the A7 API-auth product labs are recalled, N4.3).",
      "(password/KDF day; the CR-13 build lab).", EV5)
    R("SEC-5", "(KMS + key IR; N7.8).", "(KMS + key IR; the IR-05 runbook).", EV5)
    R("SEC-5", "with Confidential Computing literacy + N9c privacy (survey depth).",
      "with Confidential Computing literacy + D3 privacy (survey depth).", EV5)
    R("SEC-5", "Cards CR-E9/E10/E34. Roadmap N7.3 owns the product clickpath.",
      "Cards CR-E9/E10/E34. The CMEK procedure is the CR-14 build lab.", EV5)
    R("SEC-5", "Roadmap N4.3 owns implementation; CR-13 owns the math story.",
      "The implementation is the CR-13 build lab; this illustration is the math story.", EV5)

    # module lens lines that pointed at Northstar labs
    R("SEC-6", "Lens-2: annotate N0 hierarchy with trust boundaries.",
      "Lens-2: draw the reference app's resource hierarchy (organization → folders → prod and dev projects, B5) and "
      "mark on each layer who patches, who configures access and who holds keys.", EV5)
    R("SEC-6", "Lens-1: app middleware (N4.4 lab). Lens-2: forged Origin test.",
      "Lens-1: app middleware (the build lab below). Lens-2: forged Origin test.", EV5)
    R("SEC-6", "Lens-2: IDOR fail-then-pass (N4.7).", "Lens-2: IDOR fail-then-pass (the build lab below).", EV5)
    R("SEC-6", "Lens-1: recall N8.1 cursor pager — add abuse tests.",
      "Lens-1: the keyset (cursor) pager of SQL OD-09 — add abuse tests: a page-size cap, opaque signed cursors, a "
      "per-tenant list rate limit, no total counts on public lists.", EV5 + "; D7: the cursor pager has one home, SQL "
      "OD-09")
    R("SEC-6", "`http.Server` timeouts (N4.2). Lens-2:", "`http.Server` timeouts (the build lab below). Lens-2:", EV5)
    R("SEC-6", "Lens-1: Cloud Run CORS middleware. Lens-2: hostile Origin tests (N4.4).",
      "Lens-1: Cloud Run CORS middleware with an exact origin allowlist (never reflect `Origin`, never `*` with "
      "credentials). Lens-2: hostile Origin tests from a second local origin — a disallowed origin gets no "
      "`Access-Control-Allow-Origin`, the `null` origin is refused, and a preflight for `PUT` is answered only for "
      "allowed origins.", EV5 + "; " + EV9)
    R("SEC-6", "Lens-2: local SSRF fixture + guard tests (N4.2).",
      "Lens-2: local SSRF fixture + guard tests (the build lab below).", EV5)
    R("SEC-6", "Lens-2: paper IR for public ACE (N7.8).",
      "Lens-2: paper IR for a public grant, on the IR-06 steps (remove the grant, inventory what was exposed and for "
      "how long from Data Access logs if they were enabled, classify, decide on notification, add the org policy).",
      EV5)
    R("SEC-6", "Lens-1: N6.11 map. Lens-2: redraw the reference app's path.",
      "Lens-1: the packet-path map in the defense pattern above, one primary control per hop. Lens-2: redraw the "
      "reference app's path.", EV5)
    R("SEC-6", "Lens-2: recall N7.5 lab analytic layer.",
      "Lens-2: run the WL-04 build lab's attestation check as an admission step.", EV5)
    R("SEC-6", "Lens-2: N7.5 toy attestation analytic.", "Lens-2: the toy attestation build lab below.", EV5)
    R("SEC-6", "Lens-2: wire one alert to N7.6 template.",
      "Lens-2: wire one alert (a new service-account key: a log-based metric on the Admin Activity entry "
      "`google.iam.admin.v1.CreateServiceAccountKey` `(verify)`) to the IR-05 runbook template.", EV5)
    R("SEC-6", "postmortem. Use roadmap N7.8 template; CR-15 for crypto keys.",
      "postmortem, on the runbook template below; CR-15 for crypto keys.", EV5)
    R("SEC-6", "PAN: tokenize (N5); secrets: Secret Manager;",
      "PAN: tokenize (the payment provider's vault returns a token and the app never stores the PAN, which shrinks "
      "PCI DSS scope); secrets: Secret Manager;", EV5 + "; D7: payment tokenization has one home, PV-03")
    R("SEC-6", "Lens-1: PCI themes N5 + SDP. Lens-2: decision table.",
      "Lens-1: PCI DSS scope (the cardholder-data environment shrinks when only tokens are stored) + Sensitive Data "
      "Protection de-identification (deterministic or format-preserving tokens `(verify)`). Lens-2: decision table.",
      EV5)
    R("SEC-6", "Lens-1: Well-Architected + CCM crosswalk lite.",
      "Lens-1: Well-Architected security pillar + a light CCM-to-control mapping (§8).", EV6)
    f.line("SEC-6", "anchor-rewrite", "Skip a companion family only by passing its skip-test. `Curriculum` and Northstar",
           "Skip a companion family only by passing its skip-test. Skipping companion theory does not skip the "
           "product evidence: the Armor attach, IAP and CMEK steps still run in their labs (AB-02 and WA-11, NT-05, "
           "CR-14) when Lab Reality allows.", EV5)
    for head, lines in LABS.items():
        _after_in_card(f, head, "- **GCP lens:**", lines, "SEC-6", EV9)

    # exercise cards: single-N or phrase-shaped Map lines first, then the generic list rule
    R("SEC-7", "- **Map to GCP:** A5 TLS / N6.11 path", "- **Map to GCP:** A5 TLS / NT-07 path", EV5)
    R("SEC-7", "- **Map to GCP:** N7.1 recall + PQ-S-02", "- **Map to GCP:** PQ-S-02", EV5)
    R("SEC-7", "- **Map to GCP:** N0.4 HLD", "- **Map to GCP:** TH-02 (trust boundaries on the HLD)", EV5)
    f.line("SEC-7", "anchor-rewrite", "^- \\*\\*Map to GCP:\\*\\* N0\\.4$", "- **Map to GCP:** TH-02, TH-03", EV5,
           regex=True)
    f.line("SEC-7", "anchor-rewrite", "^- \\*\\*Map to GCP:\\*\\* N6\\.14$", "- **Map to GCP:** NT-05", EV5, regex=True)
    for card, repl in [("SEC-E2.2 · ", "AU-01, AU-04"), ("SEC-E2.3 · ", "AU-02"), ("SEC-E3.9 · ", "WA-05, TH-03")]:
        h = f.heading(card)
        f.rx("SEC-7", "anchor-rewrite", r"^- \*\*Map to GCP:\*\* N\d+\.\d+$", "- **Map to GCP:** " + repl, EV5,
             lo=h, hi=h + 8, mn=1, mx=1)
    R("SEC-7", "- **Map to GCP:** CR-14, N7.3 toy", "- **Map to GCP:** CR-14 (envelope build lab)", EV5)
    f.rx("SEC-7", "anchor-rewrite", r"^(- \*\*Map to GCP:\*\* )(.*\bN\d.*)$", _map_line, EV5, mn=30)
    R("SEC-7", "- **Design control:** Follow N7.8 public ACE runbook + evidence.",
      "- **Design control:** Follow the IR-06 steps on the IR-05 runbook template, with evidence.", EV5)
    R("SEC-7", "- **Design control:** Argon2id+salt+pepper plan (N4.3 owns lab).",
      "- **Design control:** Argon2id+salt+pepper plan (the CR-13 build lab).", EV5)
    R("SEC-7", "- **Design control:** Fill N7.8 template; grade order.",
      "- **Design control:** Fill the IR-05 runbook template; grade the order.", EV5)

    # capstones and scheduling
    R("SEC-8", "CR-12/13/14/20, A7 (API auth patterns) + A10 + N7.3–N7.4.",
      "CR-12/13/14/20, A7 (API auth patterns) + A10 + Phase 4 Security (CR-14, WA-05).", EV5)
    R("SEC-8", "- **Depends:** IR-*, CL-02/04, CR-15, roadmap N7.8 templates.",
      "- **Depends:** IR-*, CL-02/04, CR-15, the IR-05 runbook template.", EV5)
    R("SEC-8", "- **Depends:** AB-*, DOS-03/05/07, AU-08, N4.10, 6.16.",
      "- **Depends:** AB-*, DOS-03/05/07, AU-08, NT-04 (DNS and DDoS view).", EV5 + " (the bare 6.16 is the old N6.16)")
    R("SEC-8", "- **Depends:** AI-01…05, PV-02, CR-18 lite, 9c.",
      "- **Depends:** AI-01…05, PV-02, CR-18 lite, D3/D4 (production ML and LLM applications).",
      EV5 + " (the bare 9c is the old N9c)")
    R("SEC-8", "**SEC-CAP2** after N7.8 + IR/CR-15; **SEC-CAP3** after N4.10 + N6.16 + AB/DOS; **SEC-CAP4** after "
      "N9c + AI-*.", "**SEC-CAP2** after IR-05 + IR/CR-15; **SEC-CAP3** after AB-01/AB-02 + NT-04 + AB/DOS; "
      "**SEC-CAP4** after D3/D4 + AI-*.", EV5)
    R("SEC-8", "no VPC-SC before N6.15; no BinAuth before N7.5;", "no VPC-SC before NT-06; no BinAuth before WL-04;",
      EV5)
    R("SEC-8", "pair N7.6 with IR-02 alert design", "pair SCC posture (IR-04) with IR-02 alert design", EV5)

    # §8 CCM table and Appendix N anchors
    s = f.heading("8. CSA CCM v4.x coverage checklist")
    e = f.section_end(s)
    R("SEC-9", "| CL-03, AU-*, B5 / N7.2 |", "| CL-03, AU-*, B5 |", EV5)
    f.rx("SEC-9", "anchor-rewrite", r", N\d+(?:\.\d+|\.x)?(?= \|)", "", EV5, lo=s, hi=e, mn=7, mx=7)
    for old, new in [("| Primary attackers | Top companion modules | Roadmap anchors |",
                      "| Primary attackers | Top companion modules | Main-course anchors |"),
                     ("| A5 TLS, N4.4, N4.10 |", "| A5 TLS, A7, A10 |"), ("| N4.2–N4.7, N4.10 |", "| A7, A10 |"),
                     ("| N4.4, N4.7, N6.14 |", "| A7, A10, Phase 4 Security (IAP) |"),
                     ("| N4.8, N7.2 |", "| B5, Phase 4 Security |"), ("| N7.3, N6.15 |", "| V-STOR, Phase 4 Security |"),
                     ("| N4.8, N7.5 |", "| C4, Phase 4 Security |"), ("| AI-01…05, PV-02 | N9c |",
                                                                        "| AI-01…05, PV-02 | D3, D4 |")]:
        R("SEC-9", old, new, EV5)
    R("SEC-9", "prefer the `Curriculum` / Northstar product lab + live docs;",
      "prefer the main course's Part V service maps + live docs;", EV5 + "; " + EV11)

    # bare legacy section numbers (the old course's 4.x, 6.x, 7.x) the probe's N pattern cannot see
    EVL = "D10 + D11: a bare section number of the legacy course points outside the five parts; it now names the " \
          "module that holds the material"
    R("SEC-13", "zero-trust/shared-responsibility from 7.1.", "zero-trust/shared-responsibility from A10.", EVL)
    R("SEC-13", "Lens-2: toy effective-access from 7.2.",
      "Lens-2: a toy effective-access calculator — given role bindings and the `actAs` edges between service "
      "accounts, list every permission a principal can reach, then find the SEC-E3.1 path with it.", EVL + "; " + EV9)
    R("SEC-13", "destroy-order checklist 6.16.", "the destroy-order checklist of SEC-E4.21 (DNS record first, then "
      "the resource).", EVL)
    R("SEC-13", "Lens-1: IAP lab 6.14.", "Lens-1: IAP in front of the reference app's admin console (an OAuth "
      "consent screen, IAP turned on for the backend service, `roles/iap.httpsResourceAccessor` for the admin group "
      "`(verify)`).", EVL + "; " + EV9)
    R("SEC-13", "Lens-2: cosign-shaped toy from 7.5.", "Lens-2: the WL-04 toy attestation read as provenance (its "
      "builder and source-commit fields).", EVL)
    R("SEC-13", "does not unlock VPC-SC props before 6.15.", "does not unlock VPC-SC props before NT-06.", EVL)
    R("SEC-13", "- **Design control:** Redesign per 4.3+AU-10.",
      "- **Design control:** Redesign per AU-10, with the CR-13 password build lab.", EVL)
    R("SEC-13", "- **Design control:** Set timeout suite from 4.2.",
      "- **Design control:** Set the timeout suite of the DOS-05 build lab.", EVL)
    R("SEC-13", "| 3.0/4.x, WA-* |", "| A7, AU-*, WA-* |", EVL)

    # the nine checkpoint cards, in full (D9)
    R("SEC-10", "- **Scenario:** GCE guest OS CVE; Cloud Run app SQLi; GCS public ACE; Google DC physical.",
      "- **Scenario:** Four incidents on the reference app: a guest-OS kernel CVE on the GCE VM that runs the batch "
      "worker; SQL injection in the Cloud Run customer API; the invoices bucket granted to `allUsers`; a disk stolen "
      "from a Google data centre.", EV9C)
    R("SEC-10", "- **Scenario:** Docs skim (verify).",
      "- **Scenario:** The storefront's HTTPS load balancer has a Cloud Armor policy with a per-IP rate-based ban at "
      "600 requests a minute. A botnet of 20,000 residential addresses sends 30 requests a minute each to `/search`, "
      "with plausible headers. Read the Adaptive Protection overview first `(verify)`.", EV9C)
    R("SEC-10", "- **Scenario:** CNAME to deleted Cloud Run.",
      "- **Scenario:** `promo.shop.example` is a CNAME to a campaign service that was deleted after the campaign; "
      "the DNS record stayed.", EV9C)
    for head, text in CHECKS.items():
        _after_in_card(f, head, "- **Unlocks / depends:**", [text], "SEC-10", EV9C)
    for needle, lines in KEYS.items():
        f.ins_after("SEC-10", needle, lines, EV9C)

    # shared contract after the preferences (§0.6), then the parent name everywhere else
    h = f.heading("0.6 Learner teaching preferences")
    e = f.section_end(h)
    while f.L[e - 1].strip() in ("", "---"):
        e -= 1
    f.ins("SEC-11", e, [""] + contract_copy(files, 6, 7), "D6: each part carries the shared teaching rules in its own "
          "§0 (D7 exemption: rules, not topics)", cls="append")
    parent_name(f, "SEC-12")
