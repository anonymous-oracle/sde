# Part 14 · Security, Cryptography, Privacy & Compliance · TOPIC LIST

Rules and directives for this part: `index/part14_security.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Security, Cryptography, Privacy & Compliance

### Principles and economics

- Confidentiality, integrity, availability; least privilege; defence in depth; assume breach; zero trust
- Saltzer and Schroeder's principles: economy of mechanism, fail-safe defaults, complete mediation, open design, separation of privilege, least privilege, least common mechanism, psychological acceptability
- The reference monitor and the trusted computing base
- Shared responsibility across IaaS, PaaS, SaaS and serverless
- Security economics: residual risk in decisions, attacker cost versus user friction, MTTD and MTTR; security usability and accessibility: prompts and challenges tested with a screen reader and keyboard-only use, with an accessible alternative for each
- Privacy versus security tensions: retention, employee monitoring, minimization

### Threat modelling

- Attacker models: web, network, cloud administrator, co-tenant, insider
- Trust boundaries, planes (front end, API, admin, service-to-service, data, CI) and asset inventories with data classes
- STRIDE mapped to the property each threat violates, applied per data-flow element and trust boundary
- Attack trees: OR as minimum cost, AND as sum; probabilities; raising the cost of the cheapest path
- Abuse cases converted into deny tests; an authorization test matrix over subject, action and resource, with an allowed and a denied case for each combination
- MITRE ATT&CK cloud techniques (including cloud instance metadata credential access) mapped to detections
- Distributed-system threats: operator honesty, poisoned configuration across regions, the control plane as its own threat model
- Risk as likelihood × impact: an ordinal heuristic, not arithmetic; likelihood and impact scored in ordinal bands, and a threat register with one row per threat: asset, actor, precondition, attack path, violated property, mitigation, detection, test, owner and residual risk

### Access-control models

- The access-control matrix; ACLs versus capabilities
- Discretionary versus mandatory access control
- Bell–LaPadula (no read up, no write down) and Biba
- Clark–Wilson: well-formed transactions, separation of duty
- RBAC (users, roles, permissions, sessions, hierarchies), ABAC and ReBAC; ABAC as a policy over subject, resource, action and environment attributes, such as the same department as the resource owner within an allowed time window
- Relationship-based authorization at scale: Zanzibar-style tuples and consistency tokens
- Policy decision and enforcement separation: a policy decision point evaluates each request and returns allow or deny with an explanation; enforcement points at the gateway or service call it on every request; OPA (Rego) and Cedar as policy languages; decision caching with immediate invalidation or a bounded stale window

### Cryptography

- **Foundations and hygiene**
  - Goals (confidentiality, integrity, authenticity) and security games: IND-CPA, IND-CCA, EUF-CMA
  - Kerckhoffs's principle; why roll-your-own fails (ECB patterns, XOR stream reuse, Base64 as "encryption", compress-then-encrypt)
  - Classical ciphers and the knapsack cryptosystem: Caesar and Vigenère broken by frequency and index-of-coincidence analysis; the Merkle–Hellman knapsack public-key scheme, broken by cryptanalysis of its hidden superincreasing structure
  - Provable security: efficient adversaries, advantage, negligible functions, reductions, the hybrid argument
  - Perfect secrecy and the one-time pad; Shannon's |K| ≥ |M|; the two-time pad
- **Symmetric encryption**
  - PRGs, PRFs and PRPs; AES as a PRP; the PRP/PRF switching lemma and retiring 64-bit blocks
  - Modes: ECB, CBC, CTR; deterministic schemes cannot be CPA-secure
  - Padding oracles and CTR nonce reuse
  - Authenticated encryption: AES-GCM and ChaCha20-Poly1305; associated data; nonce-reuse catastrophe; tag truncation; XChaCha nonces
- **Hashes and MACs**
  - Collision, second-preimage and preimage resistance; the 2^(n/2) birthday attack
  - SHA-2 and SHA-3; Merkle–Damgård and length extension; sponges; the random-oracle model
  - HMAC, KMAC and Poly1305; CBC-MAC's fixed-length limit
  - Encrypt-then-MAC versus MAC-then-encrypt (generic composition)
  - HKDF extract-and-expand with explicit `info`
  - Canonical request signing with HMAC: a versioned canonical string of method, canonical target, selected headers, body digest, timestamp, nonce, key identifier and audience; HMAC compared in constant time; a narrow clock window and nonce cache against replay; ambiguous encodings rejected
- **Randomness**
  - OS CSPRNGs (`getrandom`, `SecureRandom`); entropy; nonces and IVs
  - VM snapshot cloning of PRNG state; low-entropy boots
- **Public-key cryptography**
  - Groups, generators; discrete log, CDH and DDH assumptions
  - Diffie–Hellman and ECDH; forward secrecy; small-subgroup and invalid-curve attacks
  - ElGamal; RSA as a trapdoor permutation; textbook RSA's malleability; RSA-OAEP
  - Hybrid encryption (KEM/DEM)
- **Signatures**
  - Hash-and-sign; RSA-PSS, ECDSA, Schnorr via Fiat–Shamir, EdDSA/Ed25519
  - ECDSA nonce reuse revealing the key; deterministic nonces
  - Algorithm-confusion and agility attacks
- **Key exchange and protocols**
  - Authenticated key exchange; SIGMA; the TLS 1.3 key schedule
  - The Dolev–Yao attacker; nonces and freshness; replay and reflection; Lowe's attack on Needham–Schroeder
  - Formal protocol verification (Tamarin, ProVerif) and TLS 1.3's co-design with analysis
- **PKI and TLS**
  - X.509 certificates, chains, hostname verification, revocation, Certificate Transparency, pinning trade-offs, ACME
  - TLS 1.2 versus 1.3; downgrade attacks; 0-RTT replay; HSTS; `Strict-Transport-Security` with `max-age`, `includeSubDomains` and `preload`, where preload is slow to undo
  - mTLS; application-layer AEAD and field-level encryption
  - TLS interception and its risks
- **Password cryptography**
  - Online versus offline guessing; guessing entropy; NIST SP 800-63B length rules: at least 15 characters for a password-only login and 8 as one MFA factor, passphrases of at least 64 characters accepted untruncated, and no composition rules or periodic rotation
  - Memory-hard KDFs (Argon2id, scrypt) and bcrypt; area × time cost
  - Salts, peppers held in a key manager, versioned records and rehashing
- **Key management**
  - Key hierarchies and envelope encryption (DEKs and KEKs); rewrap versus re-encrypt
  - Rotation with dual-key overlap; key-purpose separation; separation of duty
  - KMS, HSM, external key managers; customer-managed versus customer-supplied versus provider-managed keys
  - Key compromise response and crypto agility; key inventories; JWT cutoff timestamps
- **Side channels**
  - Timing attacks on comparisons; constant-time APIs; uniform errors
  - Cache and speculative-execution side channels on shared hardware
- **Privacy-enhancing cryptography (survey)**: trusted execution environments, multi-party computation, homomorphic encryption, zero-knowledge proofs
- **Post-quantum cryptography**
  - Shor and Grover; AES-256 under Grover
  - ML-KEM (FIPS 203), ML-DSA (FIPS 204), SLH-DSA (FIPS 205)
  - Hybrid key exchange in TLS; harvest now, decrypt later; inventories of long-lived keys
- **Engineering checklist**: vetted libraries (Tink, libsodium, standard libraries), AEAD, CSPRNG, KMS-held KEKs, no tokens in URLs, verification on, algorithm allow-lists, versioned password records, inventories

### Authentication and sessions

- Authentication versus authorization; identity, credentials and authenticators modelled as separate things: opaque non-sequential public identifiers, with email or phone as mutable verified attributes rather than identity keys
- Session hijacking; session fixation and ID rotation; idle and absolute timeouts
- Cookie attributes and theft vectors: `Secure`, `HttpOnly`, `SameSite`, `Path`, host-only cookies, the `__Host-` prefix, subdomain injection
- CSRF: synchronizer and HMAC double-submit tokens, Origin checks, SameSite as defence in depth; Fetch Metadata policy on `Sec-Fetch-Site` and `Sec-Fetch-Mode`, rejecting cross-site unsafe requests, with a documented fallback for clients that omit the headers
- JWT pitfalls: `alg=none`, RS256-to-HS256 confusion, attacker-controlled `kid`/`jku`; claim validation (iss, aud, exp, nbf, jti)
- OAuth 2.0 as delegation: authorization code with PKCE, exact redirect allow-lists, bound `state`, mix-up defences, no implicit grant; one-time short-lived authorization codes and consent bound to client, resource and scope; PKCE with S256 required, since an authorization server that accepts a request with no challenge or the plain method allows a downgrade; code and access-token injection, where a stolen code or token is placed into another session, defeated by binding the code to the PKCE verifier and the client; referer and history leakage, since codes and tokens in URLs reach logs, browser history and `Referer` headers
- OpenID Connect ID tokens and nonces; discovery through the issuer's `.well-known/openid-configuration` document, the issuer string compared exactly, and the `iss` claim checked against the issuer that sent the response so a mix-up cannot swap providers
- Counterfeit resource server: a fake API that receives a client's access token and replays it to a genuine API; defences are audience-restricted tokens, resource indicators, and resource servers that reject tokens intended for another service
- Refresh-token rotation with family revocation: each refresh returns a new refresh token and retires the old one; replay of a retired token marks theft and revokes the whole token family; absolute expiry caps the family's life
- Sender-constrained tokens (DPoP, mTLS-bound tokens): the token is bound to a key the client holds, so a stolen bearer token is unusable; DPoP proof JWTs per request carrying the HTTP method and URI; certificate-thumbprint binding for mTLS; the resource server verifies the binding
- Pushed authorization requests, resource indicators and rich authorization details: parameters posted to the authorization server over a back channel and referenced by a request URI; resource indicators naming the target API as the audience; structured `authorization_details` in place of scope strings
- SAML and XML signature wrapping; XXE in SAML parsers
- Kerberos: tickets, ticket-granting service, pass-the-ticket and offline cracking of service tickets
- Credential stuffing and password spraying: breach blocklists, rate limits, bot signals, generic errors; account-aware throttling: progressive delays per account and per source, counted on failures, with no hard lockout, so an attacker cannot lock a victim out
- MFA: TOTP, push fatigue and number matching, SIM swap, phishing-resistant WebAuthn and passkeys; replay resistance from single-use challenges and a signature counter; relying-party checks that the RP ID matches the origin, user verification is set when required and the signature verifies against the stored public key; syncable passkeys trade recovery and availability against trust in the sync provider's account, while device-bound keys need a second enrolled authenticator; authenticators bound at enrolment and invalidated when the password changes or a credential is removed
- Authenticator assurance levels AAL1, AAL2 and AAL3 (NIST SP 800-63B): the rising strength of authentication a relying party can require; AAL3 requires a hardware-based authenticator with verifier-impersonation resistance; reauthentication and session binding set per level
- Account recovery as strong as login: hashed single-use tokens, out-of-band notification, step-up; the password-change flow with the same controls: the current password or a recent reauthentication, all other sessions revoked, and the same blocklist checks as reset
- Unguessable session tokens: success probability s / 2ᵏ
- Identity federation and SSO

### Authorization flaws

- IDOR/BOLA: server-side checks on every object; tenant in every query
- Broken function-level authorization: deny by default, explicit permissions
- Mass assignment: allow-listed DTO fields; server-side prices and roles; field-level read policy: response DTOs filtered by the caller's role so internal fields such as roles, cost or internal IDs are never serialized
- Confused deputies: audience-restricted tokens, capability tokens, per-service least privilege
- Object-level authorization as a predicate over principal, action and object

### API abuse

- Rate-limit algorithms: token bucket, leaky bucket, fixed and sliding windows; 429 with `Retry-After`; layered keys (tenant, user, IP); explicit fail modes; leaky bucket as a queue drained at a constant rate, and a fixed window as a counter reset at each boundary, so a client can send up to twice the limit across it
- Where to place limits: edge, gateway and application
- Bot management and scraping; risk scores and device signals
- GraphQL depth and cost limits, persisted queries, introspection off in production
- Pagination and enumeration abuse
- Business-logic abuse: coupon stacking, negative quantities, wallet races, loyalty farming
- Inventory hoarding and checkout abuse
- Expensive exports and fan-out abuse

### Denial of service

- L3/L4 volumetric floods (UDP, SYN) and anycast edge absorption
- Amplification and reflection; bandwidth amplification factors; ingress filtering (BCP 38)
- L7 floods on expensive endpoints
- Adaptive, ML-based protection and its learning period
- Slowloris, slow POST and slow read; server timeouts and connection limits
- Resource exhaustion: zip bombs, huge bodies, unbounded uploads, ReDoS
- Economic DoS: forced egress, logging, LLM tokens; budgets and kill switches; max instances × price as a bound
- Cache stampedes and retry storms: jittered TTLs, request coalescing, soft TTLs
- SYN cookies; attacker-versus-defender cost asymmetry

### Web application security

- The same-origin policy as a formal model: origins, reading versus sending, why CORS is not a CSRF defence
- CORS pitfalls and `postMessage` origin checks; CORS middleware with an exact origin allow-list, explicit methods and headers, preflight answers cached with `Access-Control-Max-Age`, and `Vary: Origin` where responses differ; never a wildcard origin with credentials
- XSS (stored, reflected, DOM) and context-aware encoding
- Content Security Policy (nonces, hashes, report-only rollout) and Trusted Types; the headers set on every response: `Content-Security-Policy` with a nonce or hash for each script, `X-Content-Type-Options: nosniff` so browsers never sniff a type, and `Referrer-Policy` limiting what the `Referer` header reveals
- Clickjacking and `frame-ancestors`
- Injection as data becoming syntax: SQL, command, path traversal; parameterized queries; input validation at each trust boundary: parse into types, allow-list, canonicalize (decode, normalize Unicode, resolve paths) before any check, and validate again at the sink
- HTTP parameter pollution: a repeated query or form parameter read differently by a proxy and the application (first, last or joined values), used to bypass validation or authorization; one parsing rule across the stack and explicit duplicate handling
- Code obfuscation: renaming and control-flow flattening raise the cost of reading shipped JavaScript or binaries; a deterrent, not a secret store or an access control, and never the only protection
- XXE and server-side template injection
- Unsafe deserialization
- Open redirects and header (CRLF) injection; untrusted proxy headers: `X-Forwarded-For`, `Forwarded` and `X-Forwarded-Host` honoured only from configured proxies, with the client's leftmost values ignored and the address taken from the last hop a trusted proxy added
- Unsafe 307 redirects: a 307 keeps the method and body, so a credential-bearing POST answered with a 307 resends the secret to the redirect target; 303 instead after credential-bearing POST flows; redirect targets checked against an allow-list
- Log injection and forensic pollution; a structured security event schema (time, actor, action, target, outcome, request ID) with secrets, tokens and card numbers redacted before the log sink
- Memory-safety bugs (buffer overflows, use-after-free) and mitigations (canaries, ASLR, NX, CFI); memory-safe languages; privilege separation and sandboxing
- WAF rules, bypasses and preview modes
- File uploads: type allow-lists, size limits, scanning, re-encoding, storage outside the web root
- The OWASP Top 10:2025: broken access control (including SSRF), security misconfiguration, software supply chain failures, cryptographic failures, injection, insecure design, authentication failures, software or data integrity failures, security logging and alerting failures, mishandling of exceptional conditions
- OWASP ASVS 5.0 as the verification catalogue: versioned requirements mapped to each control and proved by positive, negative, fuzz, race, resource-exhaustion, rotation, revocation and recovery tests

### Cloud-specific attacks

- SSRF to instance metadata; DNS rebinding; metadata-header protections
- Public buckets and ACL mistakes; uniform bucket-level access; public-access prevention
- IAM privilege-escalation paths (acting as service accounts, broad owner roles); effective-policy analysis; deny policies; just-in-time break-glass
- Service-account key theft and sprawl; keyless workload identity federation
- Tenant isolation failures in queries, caches, jobs and logs
- VPC peering and shared-VPC trust mistakes; private service connections
- Serverless event injection; hypervisor-escape residual risk

### Ethical hacking and offensive techniques

- **Methodology and authorization**: reconnaissance, scanning, gaining access, maintaining access and covering tracks; scope, rules of engagement and written authorization; reporting
- **Reconnaissance and scanning**: passive footprinting (`whois`, DNS enumeration with `dig` and `dnsenum`, Netcraft, certificate transparency, Google dorking); Nmap scan types, service and OS fingerprinting and scripts; vulnerability scanners (Nessus, OpenVAS); CVE and CVSS; false positives
- **System hacking**: password attacks (dictionary, brute force, rainbow tables, credential stuffing); privilege escalation; persistence; malware families (viruses, worms, trojans, rootkits, botnets) and their defences
- **Network attacks**: packet sniffing (Wireshark, tcpdump); ARP spoofing and MAC flooding; DNS spoofing; interception proxies (Burp Suite); email spoofing and the SPF, DKIM and DMARC defences
- **Web attack tooling**: SQL-injection techniques (authentication bypass, error-based, blind, `sqlmap`); cross-site scripting; exploiting file uploads
- **Social engineering**: phishing, pretexting, vishing, tailgating; awareness training as a control
- **Steganography and biometrics**: hiding data in carriers and detecting it (steganalysis); biometric enrolment, matching, the FAR, FRR and equal-error-rate trade-off, template protection and liveness detection
- **Hardware security**: side-channel attacks (timing, power, electromagnetic, cache); fault injection; physical unclonable functions; hardware trojans

### Network security and zero trust

- Perimeter myths; authenticated east-west traffic; micro-segmentation
- Lateral movement as graph reachability; attack graphs
- Egress exfiltration and DNS tunnelling; egress allow-lists and DNS monitoring
- BGP hijacks, DNS cache poisoning, dangling records and subdomain takeover; DNSSEC and RPKI
- Email authentication: SPF, DKIM and DMARC
- Identity-aware proxies versus VPNs
- Data-exfiltration perimeters around cloud APIs
- Control placement along the packet path
- Zero Trust Architecture (NIST SP 800-207): policy engine, administrator and enforcement point; BeyondCorp

### Containers and Kubernetes security

- Container escape patterns: privileged containers, `docker.sock` mounts, kernel exploits
- Privileged pods, `hostPath` and Pod Security Standards
- RBAC wildcards; per-workload service accounts
- Secrets in etcd, environment variables and image layers; CSI secret drivers; etcd encryption
- Admission control and supply-chain gates: digest pins, signed images, vulnerability gates
- Default-deny NetworkPolicy; service-mesh mTLS

### Supply chain

- Poisoned images, typosquatting and dependency confusion
- Poisoned CI/CD pipelines: fork PRs, self-hosted runners, secrets in logs
- SBOMs: meaning and limits
- Image signing, attestations and admission enforcement
- Secret sprawl in repositories, images, logs, traces and prompts; pre-commit scanning; secrets management: one secret manager as the store, short-lived dynamic credentials with leases, rotation without a redeploy, and runtime injection with every read audited
- Build provenance and SLSA levels; hermetic builds

### Security management, risk and governance

- **Foundations**: the CIA triad; information security versus cyber security; anatomy of a data breach (initial access, dwell time, exfiltration, disclosure) through case studies
- **Cyber risk management**: asset, threat and vulnerability identification; qualitative risk matrices and quantitative estimates (single-loss expectancy × annual rate of occurrence); treatment by mitigating, transferring, accepting or avoiding; residual risk and the risk register
- **Governance, risk and compliance (GRC)**: ISO/IEC 27001 and 27002, the NIST Cybersecurity Framework and COBIT; policy tiers (enterprise, issue-specific, system-specific) over standards, guidelines and procedures; the business impact analysis behind contingency planning
- **NIST AI Risk Management Framework** (Govern, Map, Measure, Manage): Govern as the cross-cutting function; context and stakeholders mapped before harms are measured; validity, safety, security, privacy and bias measured; mitigations, monitoring, incidents, contestability and decommissioning managed under the same governance

### Detection and incident response

- Log coverage and trail integrity: admin and data-access logs, immutable sinks in a separate project, retention, time sync; append-only audit records with hash chaining, so that any edit or deletion breaks verification
- Alert design: few high-precision detections, owners and runbooks
- Detection engineering for cloud techniques: key creation, anomalous IAM changes, honeytokens, public bindings, metadata access
- Containment on ephemeral compute: disable identities, revoke tokens, pin known-good revisions, preserve logs
- Playbooks: compromised service account or leaked key; public data exposure; ransomware and backup integrity
- Tabletop exercises: clocks, injects, scribes, time-to-contain

### AI and LLM application threats

- Security goals for ML systems: confidentiality, integrity and availability plus authentication, authorization and non-repudiation; trustworthy-ML dimensions (fairness, toxicity, safety, sustainability, explainability); threat models by attacker knowledge (white-box, black-box) and goal
- Prompt safety (harmful outputs) versus prompt security (attacks on the application); misinformation as harmful output: fluent wrong answers and invented citations, checked by testing each claim against the retrieved sources
- Direct and indirect prompt injection; separating instructions from data; output as untrusted input; improper output handling: model text rendered as HTML, run in a shell, or passed to SQL or a template without encoding and validation, so the model's output becomes an injection vector
  - Indirect channels: poisoned documents, emails and calendar invites, API responses, résumés
  - Impacts: data exfiltration, remote tool execution, denial of service, social engineering
- Prompt leaking: exposure of system prompts, intellectual property and reconnaissance for further attacks; a system prompt is not a secret store, so no credential or access rule may depend on it staying hidden
- **Jailbreaking**
  - Taxonomy: language strategies (payload smuggling, modified instructions, stylized prompts and responses); rhetoric (innocent purpose, persuasion, alignment hacking, conversational coercion, Socratic questioning); imaginary worlds (hypotheticals, storytelling, role-play, world building); operational exploitation (many-shot examples, "unrestricted model" personas, meta-prompting)
  - White-box attacks: HotFlip gradient-guided flips; TextFooler synonym substitution; greedy coordinate gradient (GCG) adversarial suffixes optimized toward an affirmative reply, transferring across models, measured by attack success rate on AdvBench; AutoDAN readable suffixes
  - Black-box attacks: translation into low-resource languages; past-tense reformulation; context contamination with harmful in-context demonstrations; DeepWordBug character perturbations; PAIR (an attacker model refining prompts against a judge in a few dozen queries); instruction-centric harmful requests
  - Red teaming versus blue teaming
- Tool and agent abuse; excessive agency
- RAG data leakage; authorization at retrieval; per-tenant indexes; vector and embedding weaknesses: poisoned chunks ranked high by similarity, embedding inversion recovering text from stored vectors, and tenant filters enforced inside the index query rather than after retrieval
- Model and data poisoning, including poisoned federated updates; backdoors and trojan triggers; model hijacking; malicious serialized model files; signed models and private registries
- Model extraction by query-based distillation
- Shadow AI and sensitive pastes; secrets exposed to code assistants; legal and intellectual-property risk
- Adversarial examples (FGSM and optimization attacks) and robust training
- Membership inference and differentially private training
- The OWASP Top 10 for LLM Applications

### Isolation classes

- Noisy neighbours and isolation classes matched to sensitivity
- Confidential computing: what TEEs protect (memory from privileged observers) and what they do not

### Privacy

- Data classification (public, internal, confidential, restricted) and handling rules
- DLP and de-identification before analytics and prompts; purpose limitation
- Tokenization versus encryption; tokenizing card numbers to shrink PCI DSS scope
- Residency and sovereignty controls
- Re-identification through quasi-identifiers and linkage
- k-anonymity and its homogeneity and background-knowledge failures
- Differential privacy: ε-DP, the Laplace mechanism, composition, post-processing
- **Information privacy**: definitions and theories (privacy as control, secrecy and contextual integrity); measuring privacy; anonymity, pseudonymity and unlinkability; Aadhaar and identity-system privacy
- **Privacy regulation**: GDPR (lawful bases, data-subject rights, controllers and processors, DPIAs, breach notification, cross-border transfers); India's Digital Personal Data Protection Act (data fiduciaries and principals, consent managers, significant data fiduciaries); CCPA
- **Economics of privacy**: the value of privacy (willingness to accept versus willingness to pay); the privacy paradox; personalization and price discrimination as business strategy; privacy versus safety and security trade-offs

### Compliance

- The CSA Cloud Controls Matrix as a coverage checklist with evidence paths
- PCI DSS, HIPAA, SOC 2 and FedRAMP: obligation → control → product → artifact; business associate agreements; regulated-workload controls; PCI DSS scope as every system that stores, processes or transmits card numbers, with segmentation to shrink it and tokenization removing the systems that only hold tokens

### Exercises

- From scratch: SHA-256 and HMAC checked against test vectors; HKDF; constant-time comparison
- From scratch: textbook RSA and Diffie–Hellman with small numbers, then the attacks that make them unsafe without padding and authentication
- From scratch: a JWT signer and verifier that rejects `alg: none` and algorithm confusion; TOTP codes per RFC 6238
- From scratch: a Merkle tree with inclusion proofs; Shamir secret sharing over a prime field
- From scratch: a token-bucket limiter with a proof of its arrival bound
- Attacks on purpose-built toys: a padding oracle, CTR nonce reuse, ECDSA nonce reuse, length extension
- Password storage with Argon2id records, rehashing and peppers
- Envelope encryption with customer-managed keys and a rotation drill
- A threat model for an order-placement flow: diagram, STRIDE table, abuse case, residual risk; attack trees converted into table-driven deny tests
- Session fixation, CSRF, JWT and OAuth attacks replayed against a deliberately vulnerable shop application, then fixed
- Server timeouts against slow-client attacks; SSRF-to-metadata defences; a public-bucket exposure response
- An abuse-resistant public API with quotas, bot signals and idempotent writes
- A leaked service-account key incident worked through a runbook; an incident-response tabletop
- An AI-gateway threat model; prompt-injection and RAG-leakage defences for an LLM application; a red-team harness of jailbreak and injection suites scored by attack success rate
- Proofs: one-time-pad secrecy, |K| ≥ |M|, deterministic encryption is not CPA-secure
- From scratch: an OAuth token service that rotates refresh tokens within a family, revokes the whole family when a retired token is replayed, and rejects an access token whose audience names another resource server; each rule written as a failing test before its code
- **Reasoning drills**
  - Name the cheapest attack on a design before listing its defences
  - Reduce a protocol's security to a stated assumption, then find the attack when that assumption is dropped
  - Estimate the cost in money and time of brute-forcing a key or password space
  - Decide the residual risk to accept, as a decision record with review triggers
  - Predict which requests succeed when a retired refresh token is replayed after rotation, and which family is revoked, then check the prediction against the implementation
