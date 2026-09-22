## Part 4 — Authentication and authorization

**Goal:** Distinguish the four identity planes. Implement customer auth and workload auth correctly.

### 4.1 Identity product map (memorize; PCA loves this)
| Product | Who it authenticates | Use |
|---|---|---|
| Cloud Identity / Workspace | Employees | Directory, groups, org |
| IAM | Anyone accessing GCP resources | Roles on org/folder/project/resource |
| Identity Platform | *Your customers* | Email, social, SAML/OIDC, MFA, multi-tenancy, SLA 99.95%, PCI in scope |
| Firebase Authentication | Same backend, consumer subset | Faster start; no MFA/SAML/multi-tenancy/IAP/BAA |
| IAP | Users hitting an app | IAM in front of Cloud Run/GKE/App Engine; Google or Identity Platform identities |
| Workforce Identity Federation | Employees via external IdP | No Cloud Identity users required |
| Workload Identity Federation | Machines/CI/other clouds | **No service account keys** |
| Managed workload identities | GKE/GCE/agents | SPIFFE / mTLS |

### 4.2 Hardened HTTP and middleware (Go type here; Python twin after)

Build `func(http.Handler) http.Handler`: chaining, short-circuit, typed request context, cancellation, status/byte capture, panic recovery, capability-preserving ResponseWriter. Prove **order** with tests. This **is** G10–G12 HTTP, not a later language unit. Race-test shared limiter/session (**G6–G7**).

Server: explicit `http.Server`; read-header/read/write/idle timeouts; max header/body; no state change on GET/HEAD/OPTIONS; strict JSON (unknown fields / trailing data); 400/401/403/404/405/406/413/415/429/500; generic external errors; no stack traces; graceful shutdown. Sanitize forwarding headers at the trusted-proxy boundary.

Outbound: reusable client/transport; total and phase timeouts; body close; redirect policy; destination allowlist; TLS verify; size limits; bounded concurrency. **SSRF:** parse once; restrict schemes; reject userinfo/fragments when unused; resolve and validate every destination IP; block loopback/private/link-local/multicast/metadata (`169.254.169.254`); DNS rebinding and redirect escape.

Labs: middleware recorder; table-test every short-circuit and order permutation; fuzz headers/paths/JSON/forwarded-host; race-test limiter/session; benchmark rejection paths.


#### Go G11 — middleware chain, REST, status table
SYNTAX UNLOCK: Middleware is `func(http.Handler) http.Handler`. Chain outside-in. Wrap `ResponseWriter` to capture status/bytes without losing `Flush`/`Hijack` when needed. Contrast Python: Starlette middleware stack.
Concept: Prove order with tests (auth before handler; panic recover outermost). Strict JSON; no state change on safe methods; status matrix 400/401/403/404/405/406/413/415/429/500. Same `httpserver` package from G10 — extend, do not fork.
Python twin first: after Go type here (per 4.2 heading) — FastAPI/Starlette twin of the chain order tests.
Go artifact: package `httpserver/middleware`; tests: `TestChainOrder`, `TestShortCircuit401`, `TestStatusTable`, `TestStrictJSONRejectsUnknown`, `TestPanicBecomes500`; gate: table-test every short-circuit; fuzz headers/paths; this + G10 + G12 = one lab evidence pack.

---

#### Go G12 — outbound client, SSRF policy, SQL CRUD wiring
SYNTAX UNLOCK: `http.Client{Timeout, Transport}`; `defer resp.Body.Close()`; custom `DialContext` / IP allowlist for SSRF. `database/sql` with `pgx` driver: `QueryContext(ctx, ...)`. Contrast Python: `httpx` + connectors.
Concept: Reusable transport; destination allowlist; block metadata IP; redirect policy. CRUD handlers use ports from G3; SQL in adapters only. Graphs-as-needed only if a 4.2/Part 2 exercise needs adjacency — do not invent a graph course.
Python twin first: httpx SSRF tests + psycopg CRUD; then Go (Go is typed first for middleware in 4.2; CRUD Python-first still holds per Pedagogy §3 for Part 2).
Go artifact: package `httpserver/client` + `adapters/sql`; tests: `TestSSRFBlocksMetadata`, `TestClientTimeout`, `TestCRUDIdempotentInsert`, `TestContextCancelAbortsQuery`; gate: hardened server timeouts/limits/4xx table complete; race-test limiter (G7); Part 11 matrix checks G10–G12 under **4.2** heading (1.2 shows contract only).

---
### 4.3 Identity, passwords, recovery, MFA
Identity ≠ credentials. Opaque non-sequential public IDs. Email/phone are mutable verified attributes. Equivalent controls on login, register, password change, recovery, admin-assisted recovery, API login, federation.

Passwords: long passphrases, ≥64 chars supported, no silent truncate; min 15 if password-only, ≥8 if MFA; spaces/Unicode with documented normalization; no composition theater or periodic rotation; change on compromise; blocklist common/breached/contextual; allow paste/autofill/managers; no security questions.

Storage: Argon2id, unique random salt, versioned record (alg, version, params, salt, derived); input limits; tune memory/time/parallelism; constant-time compare; upgrade params after login; optional pepper with rotation plan. Never plaintext or reversible; never a fast general hash as KDF. Dummy KDF on unknown users. Generic public errors; equivalent timing. Throttle without cheap lockout. Log events without credentials. Recent-auth for high-risk changes.

Recovery: high-entropy single-use expiring tokens, stored hashed, bound to purpose/account, invalidate after use, rotate sessions after auth/privilege change, notify on another channel. Recovery must not be weaker than what it bypasses.

MFA: recovery codes; TOTP (HMAC, trusted time, replay prevention, rate limits, bounded skew, enrollment confirmation, revocation). Then WebAuthn/passkey via a maintained library (challenge freshness, origin/RP binding, UV flags, counters). SMS/OTP is not phishing-resistant.

### 4.4 Opaque sessions, cookies, CSRF, CORS
≥128 bits randomness; expose only the opaque id; keep identity, assurance, permissions, created/last-active, idle/absolute deadlines, revocation **server-side**. Hash for lookup. Never in query strings.

Cookies: `Secure`, `HttpOnly`, `SameSite=Lax` or `Strict`, host-only, `Path=/`, no extra `Domain`, expiry ≤ server validity. Rotate after login/reauth/privilege change; destroy old state. Idle+absolute expiry; logout; all-session revoke; account-disable revoke; `Cache-Control: no-store` on sensitive responses. No tokens in `localStorage`.

CSRF: no state change on safe methods; synchronizer token or session-bound HMAC double-submit; constant-time compare; never in URLs/logs; Origin/Fetch Metadata. SameSite is defense in depth, not the only control.

CORS: off unless needed; exact origin allowlist; explicit methods/headers; preflight; `Vary: Origin`. Never credentials + `*`. CORS is not authz.

Adversarial tests: fixation, guessing, stale/revoked, privilege-change rotation, logout replay, concurrent renewal, missing/forged CSRF, hostile Origin, cookie attributes.

### 4.5 API keys, signed requests, JWT policy
API keys: crypto random; show once; store hash + lookup prefix; bind owner, purpose, scopes, env, expiry, revocation; overlapping rotation; never in URLs. Identification/metering, not the sole control for high-value user actions.

Signed requests: versioned canonical string (method, target, selected headers, body digest, timestamp, nonce, key id, audience); HMAC; constant-time; clock window; nonce cache; fuzz canonicalization; replay/body/method substitution tests.

JWT: maintained JOSE library for crypto; **you** own policy. Pin alg allowlist; never `none`; no HMAC/RSA key confusion; one alg+purpose per key; validate every signature layer; iss, aud, exp, nbf, iat, typ, jti/replay, max lifetime, skew. Keys only from preconfigured issuers — never attacker `jku`/`kid` as a URL. Separate keys/rules for access vs ID vs refresh vs reset. Signature ≠ current authorization. Rotation, cache refresh, incident cutoff.

Then Cloud Run: Identity Platform / Google ID tokens; reject wrong aud. Multi-tenancy. Blocking functions. **Lab:** email/password + Google sign-in. Python then Go.

### 4.6 OAuth 2.0 / OIDC
OAuth = delegated API access; OIDC = authentication. Access vs refresh vs ID tokens are different artifacts.

Client lab: authorization code + high-entropy `state` + PKCE S256 + OIDC `nonce`; bind to session; exact redirect URIs; issuer mix-up defense; codes over TLS; tokens out of URLs and browser storage; least-privilege scopes; BFF when appropriate.

AS literacy (isolated learning implementation, not a production IdP): exact redirects; one-time short-lived codes; mandatory PKCE S256; no implicit, no password grant; refresh rotation / family revoke; 303 not 307 after credential POST.

Resource server: type, iss, aud, lifetime, signature, scope, resource/action, subject vs client. Reject tokens meant for another service.

OIDC RP: discovery only from a preconfigured issuer; exact metadata issuer; ID Token sig, iss, aud, exp, nonce, sub. Namespace by issuer+sub. Access token is not “user is present.”

Identity Platform is the production substitute after these labs.

### 4.7 Authorization (app + GCP)


#### Concept
**Deny by default.** Authorization is **server-side** — never trust the client’s claimed role. Decision matrix: **subject × action × resource × field × tenant × workflow state**. Progression you implement in order: (1) **RBAC** with explicit permissions (not scattered role-name strings in handlers); (2) **object ownership / IDOR** — guessable ids must not cross tenants; (3) **field-level** (hide `cost`, PII); (4) **tenant isolation** in queries, cache keys, jobs, exports, logs, admin paths; (5) **ABAC** (attributes: plan tier, region); (6) **ReBAC** (relationship: “editor of store X”); (7) **PDP vs PEP** — policy decision point vs enforcement point; policy versioning and cache invalidation when roles change. AuthN (who) is 4.3–4.6; AuthZ (what) is here — do not conflate “valid JWT” with “may refund order.”

#### From scratch / exercise
Middleware shape: authenticate → load principal (roles/attrs/tenant) → **authorize(action, resource)** before handler body. Table-drive tests: allow; deny; missing policy; stale role/token; confused deputy; guessed ids; batch endpoints; overposting; cross-tenant cache leak; admin separation; policy-store failure (fail closed). **Python then Go** same matrix.

#### HLD / LLD
**HLD:** PEP on every Northstar API edge; optional central PDP later; GCP **IAM** for cloud resources (SA roles); **IAP** for admin UI; context-aware access literacy for corp users.
**LLD:** Permission constants; resource id + tenant id in every query; never `WHERE id=?` without tenant; cache key includes tenant; admin paths require separate role + IAP.

#### Free-tier lab note
App AuthZ is free (your code). IAM/IAP use existing project; IAP behind HTTPS LB is **credits-optional** — paper IAP + prove app-level deny tests on Cloud Run without IAP if needed.

#### Gate
IDOR test fails then passes with tenant scope. Deny-by-default on unknown action. IAM vs app AuthZ boundary stated in one ADR sentence. **Python / Go:** authenticate → load principal → authorize action on resource — green tests for allow and deny.

### 4.8 Workload auth

Humans use Identity Platform / IAP (4.x). Workloads use **service accounts**, short-lived tokens, and federation — not JSON keys in GitHub secrets.

#### Concepts
- **Attached SA:** Cloud Run / GCE / GKE Workload Identity bind a runtime SA; ADC finds credentials. Prefer user-managed SAs per service over the Compute default SA.
- **Impersonation:** `roles/iam.serviceAccountTokenCreator` on a break-glass or CI pattern — audited, time-bounded.
- **Workload Identity Federation (WIF):** GitHub Actions (or GitLab) OIDC → Google STS → SA impersonation. Attribute conditions pin `repository`, `ref`, etc.
- **Org policy:** `iam.disableServiceAccountKeyCreation` — user-managed keys off by default for landing zones.
- **Tokens:** ID tokens for `roles/run.invoker` audience = receiving URL (3.2); access tokens for Google APIs. Never log tokens.

#### From scratch (required)
- Mock OIDC: local JWT with `iss`/`aud`/`sub` claims; verifier allowlists issuer + audience + subject pattern (repo name). Tests: wrong aud fails; expired fails; right claims pass. This is the shape of WIF attribute checks — not a replacement for Google STS.

#### Lab (free-tier boxed)
1. Create deploy SA; grant `run.admin` / Artifact Registry writer **on the project or resources**, not Owner.
2. Configure GitHub WIF pool/provider + attribute condition `assertion.repository == 'org/northstar'`.
3. Actions workflow: authenticate via WIF; deploy Cloud Run; **prove no `*.json` key in repo or secrets**.
4. Negative test: wrong repo claim cannot impersonate.
5. **Python / Go:** use ADC in Cloud Run; ID-token client to sibling service.

#### Gate
- Key creation blocked or unused; WIF deploy green; audit log shows federated principal; runbook for leaked key (7.8) still exists for legacy exceptions.

#### Decision table
| Caller | Prefer | Avoid |
|---|---|---|
| Cloud Run → GCP API | Attached SA + ADC | Downloaded key on disk |
| GitHub Actions → deploy | WIF | SA JSON in Actions secrets |
| Break-glass human | Impersonate + audit | Standing Owner keys |
| Local dev | User ADC / impersonate | Commit keys |
### 4.9 Application, secrets, supply chain, assurance
Allowlist validation; parameterized SQL; context-aware encoding; path containment; zip/file limits. Secrets: inventory, no secrets in source/images/logs/traces/prompts; Secret Manager; overlapping rotation; emergency revoke. TLS 1.2+; verify hostnames. Security logs: when/where/who/what/object/outcome/reason/trace id — never passwords, keys, raw session ids, tokens.

**Assurance ladder (learning gates, not a certificate):**
| Level | Implementation | Evidence |
|---|---|---|
| L1 | Hardened server + chain; Argon2id; register/login/change/reset; opaque sessions; CSRF/CORS; RBAC+object; input limits | Threat model, negative authz matrix, no-secret logs, timeouts |
| L2 | MFA/recovery; session mgmt; OIDC client; JWT RS; ABAC/tenant/field; secrets rotation; SSRF policy | Fuzz, race, rotation drills, multi-tenant suite, runbooks |
| L3 | WebAuthn or mTLS study; step-up; hardened admin plane | Independent review, revoke exercise, residual-risk memo |

Integrated project: multi-tenant service with public, user, operator, and s2s paths; then **replace** the learning IdP with Identity Platform while keeping learner-owned interfaces and contract tests.

### 4.10 API abuse (GCP)

Abuse controls sit at the edge and at the app: bots, credential stuffing, scraping, and expensive API fan-out.

#### Concepts
- **reCAPTCHA Enterprise:** Always Free **10k assessments/month**. Score/token verify on signup, login, checkout start — server-side verify, never trust the browser alone.
- **Gateway / Armor quotas:** API Gateway quotas (3.3); Cloud Armor rate-based bans / throttles on LB; app token-bucket still required for fine-grained per-tenant limits (4.2).
- **App Check (Firebase):** later literacy for mobile/web attestation — not a substitute for server authz.
- **Identity-aware signals:** step-up MFA on risky login (4.3); block disposable email domains as policy, not as sole control.

#### From scratch (required)
- Extend rate limiter (Pedagogy §6): per-IP and per-user buckets; return 429 with `Retry-After`. Tests: burst then throttle; tenant A cannot starve tenant B if keyed by tenant.
- Fake “captcha” port: `AbusePort.Verify(token) -> score`; fail closed on verifier errors for signup.

#### Lab (free-tier boxed)
1. Enable reCAPTCHA Enterprise; create a key; wire signup + login verify on Cloud Run; stay under 10k/mo.
2. Optional: Armor rate rule on a test path behind HTTPS LB — tear down to avoid idle LB IP cost (6.3).
3. **Python / Go:** verify assessment; reject low scores; log reason codes **without** raw tokens.

#### Gate
- Signup without valid assessment fails; limiter table tests green; ADR: where Armor vs app limit vs reCAPTCHA applies.

#### Decision table
| Abuse class | Prefer | Accept |
|---|---|---|
| Bot signup | reCAPTCHA + mail verify | Friction for real users |
| HTTP flood | Armor + LB | Idle LB cost if left up |
| Per-tenant API hammer | App token bucket / Gateway quota | Tuning false positives |
| Mobile API scrape | App Check later + authz | Not enough alone |
