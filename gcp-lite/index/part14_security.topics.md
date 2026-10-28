# Part 14 · Security, Cryptography, Privacy & Compliance · TOPIC LIST

Rules and directives for this part: `index/part14_security.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Security, Cryptography, Privacy & Compliance

### Principles and economics

- Confidentiality, integrity, availability; least privilege; defence in depth; assume breach; zero trust
- Saltzer and Schroeder's principles: economy of mechanism, fail-safe defaults, complete mediation, open design, separation of privilege, least privilege, least common mechanism, psychological acceptability; separation of duties, where no one person completes a sensitive action alone (maker and checker, two-person approval for payouts and key ceremonies); secure defaults that ship the safe setting, with any override explicit, audited and tested
- The reference monitor and the trusted computing base: the reference monitor is the access check that mediates every request from a subject to an object, and it must always be invoked, be tamper-proof and be small enough to verify; the trusted computing base is the set of hardware, firmware and software that a security claim depends on, so a smaller base leaves fewer places for a flaw to hide
- Shared responsibility across IaaS, PaaS, SaaS and serverless
- Security economics: residual risk in decisions, attacker cost versus user friction, MTTD and MTTR; security usability and accessibility: prompts and challenges tested with a screen reader and keyboard-only use, with an accessible alternative for each; each security decision judged by whether the people who must complete it finish the task, measured as completion rate, time taken and error rate, so that the safe path is also the easiest path
- Privacy versus security tensions: retention, employee monitoring, minimization; keeping logs and records longer helps investigations but enlarges what a breach exposes; monitoring staff activity conflicts with their privacy and needs a stated purpose and limits; data minimization collects and keeps only what the stated purpose needs, which reduces both privacy harm and breach impact

### Threat modelling

- Attacker models: web, network, cloud administrator, co-tenant, insider; each model fixes what the attacker can reach and observe: a web attacker controls only the requests a browser sends, a network attacker can read and inject traffic on the path, a cloud administrator holds platform-level access, a co-tenant shares hardware or a host with the victim, and an insider holds legitimate credentials; a design is judged against the models it claims to resist
- Trust boundaries, planes (front end, API, admin, service-to-service, data, CI) and asset inventories with data classes
- STRIDE mapped to the property each threat violates, applied per data-flow element and trust boundary; Spoofing violates authenticity, Tampering integrity, Repudiation non-repudiation, Information disclosure confidentiality, Denial of service availability and Elevation of privilege authorization; the per-element walk-through checks external entities for spoofing and repudiation, processes against all six letters, data stores for tampering, repudiation, disclosure and denial, and data flows for tampering, disclosure and denial, recording each cell as a threat with a mitigation or a reason it does not apply
- Attack trees: OR as minimum cost, AND as sum; probabilities; raising the cost of the cheapest path
- Abuse cases converted into deny tests; an authorization test matrix over subject, action and resource, with an allowed and a denied case for each combination
- MITRE ATT&CK cloud techniques (including cloud instance metadata credential access) mapped to detections
- Distributed-system threats: operator honesty, poisoned configuration across regions, the control plane as its own threat model; node identity and authenticated peer channels, since a replica that accepts unauthenticated messages can be impersonated and replayed; the fault model sets the bound: crash-tolerant majority protocols such as Paxos and Raft survive f crashes with n ≥ 2f + 1, while Byzantine agreement needs n ≥ 3f + 1, because under the crash model one lying node can break agreement; clocks as an attack surface, since a skewed or attacker-set time breaks leases, certificate validity and replay windows
- Risk as likelihood × impact: an ordinal heuristic, not arithmetic; likelihood and impact scored in ordinal bands, and a threat register with one row per threat: asset, actor, precondition, attack path, violated property, mitigation, detection, test, owner and residual risk

### Access-control models

- The access-control matrix; ACLs versus capabilities; a capability as an unforgeable reference that carries both the designation and the authority to use it, so possession is the permission; delegation by passing the reference, attenuation by wrapping it in a narrower one (a read-only view), and revocation through an indirection object; the confused-deputy problem avoided because the deputy holds no ambient authority, only the references it was handed; ACLs checking the caller's identity at each access, which lets a deputy act with its own authority
- Discretionary versus mandatory access control: in discretionary access control the owner of an object decides who may access it, as with file permissions and ACLs; in mandatory access control a central policy labels subjects and objects and the system enforces it, so an owner cannot grant access the policy forbids; the cost of mandatory control is rigidity and administration effort
- Bell–LaPadula (no read up, no write down) and Biba: Bell–LaPadula protects confidentiality with the simple security property (no read up) and the star property (no write down); Biba protects integrity with the reverse rules, no read down and no write up, so low-integrity input cannot contaminate high-integrity data; both assume the labels are correct and neither addresses covert channels
- Clark–Wilson: well-formed transactions, separation of duty; data changes only through transformation procedures certified to preserve integrity constraints, each run by a user authorized for that transaction; separation of duty means one person cannot complete a transaction alone, as in a maker and checker pair; unlike Bell–LaPadula it protects integrity through certified transactions rather than through labels
- RBAC (users, roles, permissions, sessions, hierarchies), ABAC and ReBAC; ABAC as a policy over subject, resource, action and environment attributes, such as the same department as the resource owner within an allowed time window
- Relationship-based authorization at scale: Zanzibar-style tuples and consistency tokens
- Policy decision and enforcement separation: a policy decision point evaluates each request and returns allow or deny with an explanation; enforcement points at the gateway or service call it on every request; OPA (Rego) and Cedar as policy languages; decision caching with immediate invalidation or a bounded stale window

### Cryptography

- **Foundations and hygiene**
  - Goals (confidentiality, integrity, authenticity) and security games: IND-CPA, IND-CCA, EUF-CMA
  - Kerckhoffs's principle; why roll-your-own fails (ECB patterns, XOR stream reuse, Base64 as "encryption", compress-then-encrypt)
  - Classical ciphers and the knapsack cryptosystem: Caesar and Vigenère broken by frequency and index-of-coincidence analysis; the Merkle–Hellman knapsack public-key scheme, broken by cryptanalysis of its hidden superincreasing structure
  - Provable security: efficient adversaries, advantage, negligible functions, reductions, the hybrid argument
  - Perfect secrecy and the one-time pad; Shannon's |K| ≥ |M|; the two-time pad: a scheme has perfect secrecy when the ciphertext is independent of the message, so Pr[M = m | C = c] = Pr[M = m] for every message and ciphertext; the one-time pad XORs the message with a uniformly random key of the same length, used once, and Shannon proved that perfect secrecy forces |K| ≥ |M|; reusing a key gives C1 XOR C2 = m1 XOR m2, which leaks the relation between the two messages
- **Symmetric encryption**
  - PRGs, PRFs and PRPs; AES as a PRP; the PRP/PRF switching lemma and retiring 64-bit blocks
  - Modes: ECB, CBC, CTR; deterministic schemes cannot be CPA-secure; ECB encrypts each block alone, so equal plaintext blocks give equal ciphertext blocks; CBC XORs each plaintext block with the previous ciphertext block and needs a random IV; CTR XORs the message with a keystream made from a counter and a nonce, so it works as a stream cipher; a deterministic scheme gives the same ciphertext for the same message, so an adversary who gets the encryption of m0 and then a challenge on m0 or m1 can compare the ciphertexts and win
  - Padding oracles and CTR nonce reuse: a padding oracle reveals whether a CBC-decrypted message has valid PKCS#7 padding, often through an error or a timing difference, and repeated queries recover the plaintext one byte at a time; CTR nonce reuse XORs two messages under the same keystream, so C1 XOR C2 = m1 XOR m2 and a known or guessable message exposes the other; both failures come from using a mode without authentication
  - Authenticated encryption: AES-GCM and ChaCha20-Poly1305; associated data; nonce-reuse catastrophe; tag truncation; XChaCha nonces
- **Hashes and MACs**
  - Collision, second-preimage and preimage resistance; the 2^(n/2) birthday attack: for an n-bit hash, preimage resistance means that finding any input with a given digest costs about 2^n work; second-preimage resistance means that, given one input, finding a different input with the same digest costs about 2^n; collision resistance means finding any two inputs with equal digests costs about 2^(n/2), by the birthday paradox, which needs roughly 1.18 × 2^(n/2) random samples for a 50% chance
  - SHA-2 and SHA-3; Merkle–Damgård and length extension; sponges; the random-oracle model
  - HMAC, KMAC and Poly1305; CBC-MAC's fixed-length limit: HMAC is H((K XOR opad) || H((K XOR ipad) || m)) and is secure for variable-length messages when H is a suitable hash; KMAC is a MAC built on the SHA-3 sponge; Poly1305 is a one-time authenticator over a prime field, combined with a stream cipher in ChaCha20-Poly1305, and its key must never be reused; CBC-MAC is secure only for messages of one fixed length, since for variable lengths an attacker can combine two tagged messages to forge a tag for a new one
  - Encrypt-then-MAC versus MAC-then-encrypt (generic composition): encrypt-then-MAC computes the tag over the ciphertext and verifies it before any decryption, and it is the only generic composition proved to give CCA security for any secure encryption and MAC pair; MAC-then-encrypt authenticates the plaintext, so the receiver must decrypt before it can verify, which is how the padding-oracle attacks against some TLS deployments worked; encrypt-then-MAC rejects forged input without touching the decryptor
  - HKDF extract-and-expand with explicit `info`: extract computes a pseudorandom key PRK = HMAC(salt, input keying material), which concentrates the entropy of a possibly non-uniform input into a fixed-length key; expand outputs blocks T(i) = HMAC(PRK, T(i−1) || info || i) and concatenates them to the length needed; the info string binds each derived key to its purpose and context, so two keys derived from one secret with different info are independent
  - Canonical request signing with HMAC: a versioned canonical string of method, canonical target, selected headers, body digest, timestamp, nonce, key identifier and audience; HMAC compared in constant time; a narrow clock window and nonce cache against replay; ambiguous encodings rejected
- **Randomness**
  - OS CSPRNGs (`getrandom`, `SecureRandom`); entropy; nonces and IVs: a cryptographically secure generator must stay unpredictable even when its output is observed, and the operating system seeds it from hardware and event entropy; `getrandom` on Linux blocks until its pool is initialised, and `SecureRandom` is the Java interface to such a generator; a nonce must be unique per key, and a CBC IV must also be unpredictable
  - VM snapshot cloning of PRNG state; low-entropy boots: a virtual machine image or snapshot captured with a generator's state already advanced restarts every clone from the same state, so the clones produce identical keys and nonces; a device that boots with little entropy, such as an embedded system before its entropy sources have produced data, can generate predictable keys at first start; the defences are to reseed after a snapshot restore and to block key generation until the pool is initialised
- **Public-key cryptography**
  - Groups, generators; discrete log, CDH and DDH assumptions: a cyclic group G of prime order q has a generator g so that every element is a power of g; the discrete logarithm problem asks for x given g^x; computational Diffie–Hellman asks for g^(ab) given g^a and g^b; decisional Diffie–Hellman asks to tell g^(ab) from a random element; each is assumed hard rather than proved hard, and DDH is the stronger assumption, since solving CDH also solves DDH
  - Diffie–Hellman and ECDH; forward secrecy; small-subgroup and invalid-curve attacks
  - ElGamal; RSA as a trapdoor permutation; textbook RSA's malleability; RSA-OAEP: ElGamal encrypts m as (g^r, m·h^r) with h = g^x, so its security rests on DDH, and it is malleable because scaling the second part scales the plaintext; RSA is a trapdoor permutation, where c = m^e mod N is easy and inverting it without the private exponent d is believed hard; textbook RSA is deterministic and malleable, since c·2^e decrypts to 2m; RSA-OAEP adds randomized padding so that the scheme is IND-CCA2 secure in the random-oracle model
  - Hybrid encryption (KEM/DEM): a key encapsulation mechanism (KEM) turns a public key into a fresh shared secret and a ciphertext for it, and a data encapsulation mechanism (DEM), such as AES-GCM, encrypts the message under that secret, so the pair gives public-key encryption for long messages at symmetric speed; the KEM must be IND-CCA secure and the DEM must be an authenticated encryption scheme; ML-KEM is a standard KEM
- **Signatures**
  - Hash-and-sign; RSA-PSS, ECDSA, Schnorr via Fiat–Shamir, EdDSA/Ed25519: hash-and-sign signs a digest of the message, so the signing cost does not grow with message size; RSA-PSS is randomized RSA signing with a tighter security argument than the older PKCS#1 v1.5 padding; ECDSA signs with a random nonce k, and the pair (r, s) is checked against the public point on an elliptic curve; Schnorr's signature is the Fiat–Shamir transform of its identification protocol; EdDSA with Ed25519 derives its nonce deterministically on a fixed curve, which removes the nonce risk
  - ECDSA nonce reuse revealing the key; deterministic nonces: if two signatures share the nonce k, then s1 − s2 = k⁻¹(m1 − m2) mod n, so k = (m1 − m2)/(s1 − s2) and the private key x = (s·k − m)/r mod n follows from one signature; deterministic nonces derive k from the private key and the message with an HMAC-based construction, as in RFC 6979, so a nonce cannot repeat across different messages
  - Algorithm-confusion and agility attacks: agility is the ability to switch algorithms, which helps migration but lets an attacker force a weaker one when a protocol negotiates the choice; the defence is a fixed allow-list of algorithms per key and purpose, with no fallback to a weaker option and a rejection of any unknown identifier
- **Key exchange and protocols**
  - Authenticated key exchange; SIGMA; the TLS 1.3 key schedule: an authenticated key exchange proves to each side who the peer is while deriving a session key from fresh ephemeral Diffie–Hellman values; SIGMA signs the exchanged values and binds the identities, which defeats unknown key-share attacks; the TLS 1.3 key schedule runs HKDF-Extract over the shared secret to produce handshake and traffic secrets, each expanded with a label and the transcript hash, so every key depends on the whole handshake
  - The Dolev–Yao attacker; nonces and freshness; replay and reflection; Lowe's attack on Needham–Schroeder
  - Formal protocol verification (Tamarin, ProVerif) and TLS 1.3's co-design with analysis
- **PKI and TLS**
  - X.509 certificates, chains, hostname verification, revocation, Certificate Transparency, pinning trade-offs, ACME
  - TLS 1.2 versus 1.3; downgrade attacks; 0-RTT replay; HSTS; `Strict-Transport-Security` with `max-age`, `includeSubDomains` and `preload`, where preload is slow to undo
  - mTLS; application-layer AEAD and field-level encryption: in mutual TLS the server also requests and verifies the client's certificate, so both sides authenticate with keys bound to certificates and any peer without a valid chain is refused; application-layer AEAD encrypts a payload or a single field with a key from a key hierarchy, so the data stays encrypted in storage and logs after the transport has ended, and the associated data binds each ciphertext to its record and column
  - TLS interception and its risks: a middlebox, such as a corporate proxy, terminates the client's TLS session, inspects the plaintext and opens a second session to the server; this works only if the client trusts an inserted root certificate; the risks are that the proxy sees every plaintext secret, that its key compromise breaks all traffic it handles, that pinned clients fail, and that weak proxy settings lower the security of every session through it
- **Password cryptography**
  - Online versus offline guessing; guessing entropy; NIST SP 800-63B length rules: at least 15 characters for a password-only login and 8 as one MFA factor, passphrases of at least 64 characters accepted untruncated, and no composition rules or periodic rotation
  - Memory-hard KDFs (Argon2id, scrypt) and bcrypt; area × time cost: a memory-hard KDF forces each guess to use a large block of memory, so an attacker with GPUs or ASICs pays for area as well as time; scrypt takes CPU and memory cost parameters N and r and a parallelism parameter p; Argon2id takes a memory size, an iteration count and a parallelism degree, and its hybrid mode resists both side-channel and time-memory trade-off attacks; bcrypt is older, uses only a small fixed memory footprint, and ignores input beyond 72 bytes
  - Salts, peppers held in a key manager, versioned records and rehashing: a salt is a random per-user value stored with the hash, so identical passwords give different hashes and precomputed tables are useless; a pepper is a secret key applied on top and held outside the database in a key manager, so a stolen table alone cannot be checked; a versioned record stores the algorithm and its parameters so that old hashes stay verifiable; rehashing upgrades a stored hash to new parameters on the next successful login, when the plaintext is available
- **Key management**
  - Key hierarchies and envelope encryption (DEKs and KEKs); rewrap versus re-encrypt
  - Rotation with dual-key overlap; key-purpose separation; separation of duty: rotation with a dual-key overlap publishes the new key and keeps the old one valid until every consumer has switched, so no request fails at the boundary; key-purpose separation gives each purpose its own key, such as encryption, signing or MAC, so a key used for one cannot be misused for another; separation of duty keeps the people who create, approve and use key material distinct
  - KMS, HSM, external key managers; customer-managed versus customer-supplied versus provider-managed keys
  - Key compromise response and crypto agility; key inventories; JWT cutoff timestamps
- **Side channels**
  - Timing attacks on comparisons; constant-time APIs; uniform errors: a comparison that returns at the first differing byte takes time that grows with the length of the matching prefix, so an attacker who measures the time can recover a MAC or token one byte at a time; a constant-time comparison always reads every byte and combines the differences without branching, as `subtle.ConstantTimeCompare` or `hmac.Equal` do in Go; uniform errors return the same message and timing for an unknown user and a wrong password, so the response reveals nothing
  - Cache and speculative-execution side channels on shared hardware: a shared cache lets a process learn which lines another process touched by timing its own accesses, as in Flush+Reload and Prime+Probe, which leaks key-dependent table lookups; speculative execution runs instructions past a branch that is later rolled back, and Spectre leaks data through the cache state those speculative loads leave; mitigations are constant-time code, no secret-dependent memory addresses, no sharing of physical cores between tenants where needed, and isolation on separate hardware
- **Privacy-enhancing cryptography (survey)**: trusted execution environments, multi-party computation, homomorphic encryption, zero-knowledge proofs
- **Post-quantum cryptography**
  - Shor and Grover; AES-256 under Grover
  - ML-KEM (FIPS 203), ML-DSA (FIPS 204), SLH-DSA (FIPS 205)
  - Hybrid key exchange in TLS; harvest now, decrypt later; inventories of long-lived keys
- **Engineering checklist**: vetted libraries (Tink, libsodium, standard libraries), AEAD, CSPRNG, KMS-held KEKs, no tokens in URLs, verification on, algorithm allow-lists, versioned password records, inventories
- **Computational hardness and semantic security**: efficient adversaries (probabilistic polynomial time) and negligible functions (smaller than the inverse of every polynomial); one-way functions as the base object, with the hardness assumptions (discrete log, RSA, learning with errors) each a stated conjecture rather than a proof; computational indistinguishability of distributions; semantic security, where whatever an efficient adversary learns about any function of the plaintext from the ciphertext it could learn without the ciphertext, shown equivalent to indistinguishability for encryption (Goldwasser and Micali); pseudorandom generators exist if and only if one-way functions exist (Håstad, Impagliazzo, Levin and Luby); reductions turning an adversary against a scheme into an adversary against the assumption, with the hybrid argument joining the steps
- **Zero-knowledge proofs**: a prover convinces a verifier that a statement is true without revealing why, defined by completeness (an honest prover convinces an honest verifier), soundness (a cheating prover succeeds with negligible probability) and zero knowledge (the verifier's view can be simulated without the witness); Schnorr's protocol as the worked case: commit t = gʳ, challenge c, response s = r + cx, and the verifier checks gˢ = t·yᶜ for y = gˣ; special soundness, since two accepting transcripts with one commitment and two challenges reveal x = (s₁ − s₂)/(c₁ − c₂) mod q; honest-verifier zero knowledge by choosing s and c first and setting t = gˢ·y⁻ᶜ; Fiat–Shamir hashing the commitment into the challenge for a non-interactive proof in the random-oracle model; zk-SNARKs (succinct, with a trusted setup) and zk-STARKs (hash-based, transparent) as succinct non-interactive arguments; uses such as proving an age range or a balance without revealing the value

### Authentication and sessions

- Authentication versus authorization; identity, credentials and authenticators modelled as separate things: opaque non-sequential public identifiers, with email or phone as mutable verified attributes rather than identity keys; the subject, the principal an authorization decision names, distinct from the identity record, the credential that proved it and the session that carries it
- Session hijacking; session fixation and ID rotation; idle and absolute timeouts; explicit logout that destroys the server-side session and not only the cookie, all-session revocation on password change or account disable, and a concurrent-session policy that caps or lists active sessions
- Cookie attributes and theft vectors: `Secure`, `HttpOnly`, `SameSite`, `Path`, host-only cookies, the `__Host-` prefix, subdomain injection; no session identifier, access token or refresh token in script-readable browser storage (localStorage or sessionStorage), since any script that runs through an XSS flaw can read it, so the session identifier stays in an HttpOnly cookie
- CSRF: synchronizer and HMAC double-submit tokens, Origin checks, SameSite as defence in depth; Fetch Metadata policy on `Sec-Fetch-Site` and `Sec-Fetch-Mode`, rejecting cross-site unsafe requests, with a documented fallback for clients that omit the headers
- JWT pitfalls: `alg=none`, RS256-to-HS256 confusion, attacker-controlled `kid`/`jku`; claim validation (iss, aud, exp, nbf, jti); key selection only from the JWKS of a preconfigured trusted issuer, with the `kid` used to choose among already-trusted keys and never as a path, query or URL, and each key bound to one algorithm and purpose; an explicit token type (`typ`) so that an ID, refresh, reset or logout token cannot be presented as an access token
- OAuth 2.0 as delegation: authorization code with PKCE, exact redirect allow-lists, bound `state`, mix-up defences, no implicit grant; one-time short-lived authorization codes and consent bound to client, resource and scope; PKCE with S256 required, since an authorization server that accepts a request with no challenge or the plain method allows a downgrade; code and access-token injection, where a stolen code or token is placed into another session, defeated by binding the code to the PKCE verifier and the client; referer and history leakage, since codes and tokens in URLs reach logs, browser history and `Referer` headers; the resource-owner password credentials grant refused as well, since it hands the client the user's password and bypasses the browser redirect where phishing-resistant checks and MFA run
- OpenID Connect ID tokens and nonces; discovery through the issuer's `.well-known/openid-configuration` document, the issuer string compared exactly, and the `iss` claim checked against the issuer that sent the response so a mix-up cannot swap providers; external identities keyed by the pair of issuer and subject, never by subject alone, since a subject is unique only within one issuer, and never by email
- Counterfeit resource server: a fake API that receives a client's access token and replays it to a genuine API; defences are audience-restricted tokens, resource indicators, and resource servers that reject tokens intended for another service
- Refresh-token rotation with family revocation: each refresh returns a new refresh token and retires the old one; replay of a retired token marks theft and revokes the whole token family; absolute expiry caps the family's life
- Sender-constrained tokens (DPoP, mTLS-bound tokens): the token is bound to a key the client holds, so a stolen bearer token is unusable; DPoP proof JWTs per request carrying the HTTP method and URI; certificate-thumbprint binding for mTLS; the resource server verifies the binding
- Pushed authorization requests, resource indicators and rich authorization details: parameters posted to the authorization server over a back channel and referenced by a request URI; resource indicators naming the target API as the audience; structured `authorization_details` in place of scope strings
- SAML and XML signature wrapping; XXE in SAML parsers
- Kerberos: tickets, ticket-granting service, pass-the-ticket and offline cracking of service tickets
- Credential stuffing and password spraying: breach blocklists, rate limits, bot signals, generic errors; account-aware throttling: progressive delays per account and per source, counted on failures, with no hard lockout, so an attacker cannot lock a victim out
- MFA: TOTP, push fatigue and number matching, SIM swap, phishing-resistant WebAuthn and passkeys; replay resistance from single-use challenges and a signature counter; relying-party checks that the RP ID matches the origin, user verification is set when required and the signature verifies against the stored public key; syncable passkeys trade recovery and availability against trust in the sync provider's account, while device-bound keys need a second enrolled authenticator; authenticators bound at enrolment and invalidated when the password changes or a credential is removed; enrolment confirmed before a new authenticator is trusted, several authenticators supported with a recovery path, and a lost or compromised authenticator revoked and removed by a verified flow
- Authenticator assurance levels AAL1, AAL2 and AAL3 (NIST SP 800-63B): the rising strength of authentication a relying party can require; AAL3 requires a hardware-based authenticator with verifier-impersonation resistance; reauthentication and session binding set per level; a recent-authentication check that requires a fresh login within a configured window before password, email, MFA, recovery, payout or privilege changes, with step-up to a stronger factor once the window has passed
- Account recovery as strong as login: hashed single-use tokens, out-of-band notification, step-up; the password-change flow with the same controls: the current password or a recent reauthentication, all other sessions revoked, and the same blocklist checks as reset
- Unguessable session tokens: success probability s / 2ᵏ
- Identity federation and SSO
- OAuth 2.0 dynamic client registration (RFC 7591): a client posts its metadata (redirect URIs, grant types, token endpoint authentication method, scopes) to a registration endpoint and receives a client identifier and, for a confidential client, a secret, plus a registration access token for later updates (RFC 7592); an open endpoint lets anyone create clients, so it requires an initial access token or a signed software statement, redirect URIs validated at registration and again at authorization (exact matches, TLS except loopback for native apps), and grant types limited to those the server allows
- API keys: generated from a cryptographic random source and shown once; stored as a hash with a non-secret lookup prefix, so the server finds the record without comparing secrets; bound to owner, purpose, scopes, environment, creation, last use, expiry and revocation; rotated with an overlap so that both keys work during the change; rejected in URLs and redacted from logs; used for client identification, metering and bounded machine access, never as the sole control for a high-value user action; a signed request (method, target, body digest, timestamp, nonce) is the stronger form, as in canonical request signing with HMAC
- One-time recovery codes: a batch of random codes generated from a cryptographic random source and shown to the user once, stored as hashes, each usable once; redemption rate-limited and logged; regenerating the batch invalidates every earlier code; the codes are a recovery factor, weaker than a second authenticator, and carry the same notification and session-revocation rules as recovery
- Token revocation and stale authorization: a valid signature proves who issued a token, not that its holder is still allowed to act; access tokens kept short-lived, with revocation through a list, token introspection or a server-side session check for high-risk actions; role changes, disabled accounts and removed grants taking effect on the next request where possible, and a bounded stale window documented where not; tests replay an unexpired token after its role was revoked and expect a denial
- Sensitive responses: `Cache-Control: no-store` on responses carrying credentials, session data, tokens or personal data, so that neither the browser's cache nor a shared cache keeps a copy; `no-cache` alone permits storage that is revalidated before reuse, so it does not protect; `private` restricts only shared caches; the header set by the application on the response itself

### Authorization flaws

- IDOR/BOLA: server-side checks on every object; tenant in every query
- Broken function-level authorization: deny by default, explicit permissions
- Mass assignment: allow-listed DTO fields; server-side prices and roles; field-level read policy: response DTOs filtered by the caller's role so internal fields such as roles, cost or internal IDs are never serialized
- Confused deputies: audience-restricted tokens, capability tokens, per-service least privilege
- Object-level authorization as a predicate over principal, action and object
- Administrator and service identity separation: a human administrator acts through a separate administrative role with its own stronger authentication and its own audited session, never through the everyday account; a service account holds only the permissions of its one workload; no credential is shared between people or between services; administrative endpoints tested to refuse ordinary sessions, and service tokens tested to refuse human-only actions

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
- Open redirects and header (CRLF) injection; untrusted proxy headers: `X-Forwarded-For`, `Forwarded` and `X-Forwarded-Host` honoured only from configured proxies, with the client's leftmost values ignored and the address taken from the last hop a trusted proxy added; the request ID taken from an inbound header only when that hop is trusted, otherwise generated fresh, length- and character-checked, and carried into every log line and downstream call
- Unsafe 307 redirects: a 307 keeps the method and body, so a credential-bearing POST answered with a 307 resends the secret to the redirect target; 303 instead after credential-bearing POST flows; redirect targets checked against an allow-list
- Log injection and forensic pollution; a structured security event schema (time, actor, action, target, outcome, request ID) with secrets, tokens and card numbers redacted before the log sink; each security event also records where it happened, a reason category and a confidence value; access logs record method, route template, status, latency and request ID, never raw query strings or the Authorization and Cookie headers; redaction tested by sending a planted fake credential and asserting that it appears in no log line, trace or metric
- Memory-safety bugs (buffer overflows, use-after-free) and mitigations (canaries, ASLR, NX, CFI); memory-safe languages; privilege separation and sandboxing
- WAF rules, bypasses and preview modes
- File uploads: type allow-lists, size limits, scanning, re-encoding, storage outside the web root
- The OWASP Top 10:2025: broken access control (including SSRF), security misconfiguration, software supply chain failures, cryptographic failures, injection, insecure design, authentication failures, software or data integrity failures, security logging and alerting failures, mishandling of exceptional conditions
- OWASP ASVS 5.0 as the verification catalogue: versioned requirements mapped to each control and proved by positive, negative, fuzz, race, resource-exhaustion, rotation, revocation and recovery tests; chapters for authentication, session management, authorization, self-contained tokens, OAuth and OpenID Connect, cryptography, communication security, data protection, API, logging and configuration, each requirement verified at the ASVS level (L1 to L3) that the application's risk calls for
- Host header validation: the Host value compared with an allow-list of authoritative hostnames before any link, redirect or cache key is built from it, and an unknown Host rejected (400, or 421 Misdirected Request for a connection that reached the wrong server); absolute URLs in password-reset and verification emails built from configuration rather than from the request's Host, so that a forged Host cannot send a victim a poisoned link; a forwarded host honoured only from a trusted hop
- Secure outbound calls: a reusable HTTP client with total and per-phase timeouts, response size limits and bounded concurrency; a URL parsed once, with the scheme restricted to http and https and userinfo rejected; every resolved destination address checked against loopback, private, link-local, multicast and cloud metadata ranges, and the connection made to the checked address so that DNS rebinding cannot swap it; redirects followed only to allow-listed hosts and checked again at each hop; egress network controls as a second layer
- Middleware chain order and its security checks: an outermost-first chain of request ID, panic recovery with generic errors, Host and method checks, security headers, body and header limits, access logging with redaction and response-time measurement, deadline and concurrency budget, CORS and CSRF checks, rate limits, authentication, authorization, input validation, then the handler; each short circuit and each swap of order tested; response compression avoided for responses that mix secrets with attacker-controlled input, because the compressed length leaks the secret (the CRIME and BREACH attacks)

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
- Microservice security: each service has its own workload identity (for example a SPIFFE ID carried in an X.509 SVID) used for mutual TLS between services; each call authorized on the caller's identity and, where a user is involved, the end user's identity, carried by token exchange (RFC 8693) as a narrower token for the downstream service instead of forwarding the original token; per-service least privilege; east–west authorization written per route rather than per network segment; the mesh enforces identity, and the service still checks authorization

### Containers and Kubernetes security

- Container escape patterns: privileged containers, `docker.sock` mounts, kernel exploits
- Privileged pods, `hostPath` and Pod Security Standards
- RBAC wildcards; per-workload service accounts
- Secrets in etcd, environment variables and image layers; CSI secret drivers; etcd encryption
- Admission control and supply-chain gates: digest pins, signed images, vulnerability gates
- Default-deny NetworkPolicy; service-mesh mTLS
- Environment variables as a secret channel: values set in a container or pod specification are readable by anyone who can read that specification and by every process in the container, and they reach crash dumps, child processes and debug output; secrets instead mounted as files with restrictive permissions, or fetched at start through the workload's identity; no environment dump written to logs; tests that a planted fake value appears in neither the image layers, the specification nor the logs

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
- **Security assurance and Common Criteria**: ISO/IEC 15408 evaluates a product's security claims, stated in a Security Target (the threats, assets and security functions claimed) or in a Protection Profile reused across products of one kind; each claim is paired with functional requirements and assurance components; Evaluation Assurance Levels run from EAL1 (functionally tested) through EAL4 (methodically designed, tested and reviewed) to EAL7 (formally verified design and tested), with higher levels costing more evaluation effort; the evaluation proves that the claimed functions work as specified, not that the claims are the right ones, and mutual recognition between national schemes covers only the lower levels, so a high EAL is not automatically accepted abroad
- **Secure development lifecycle**: security requirements and abuse cases written with each feature; a threat model at design, redone when a change touches a trust boundary, identity flow or data class; secure coding standards and vetted libraries; static analysis, dependency and secret scanning in CI; dynamic testing and fuzzing of parsers before release; a security review before release with recorded findings; incident response and vulnerability disclosure plans kept current; the NIST Secure Software Development Framework (SP 800-218) as a checklist of its practices

### Detection and incident response

- Log coverage and trail integrity: admin and data-access logs, immutable sinks in a separate project, retention, time sync; append-only audit records with hash chaining, so that any edit or deletion breaks verification
- Alert design: few high-precision detections, owners and runbooks
- Detection engineering for cloud techniques: key creation, anomalous IAM changes, honeytokens, public bindings, metadata access
- Containment on ephemeral compute: disable identities, revoke tokens, pin known-good revisions, preserve logs
- Playbooks: compromised service account or leaked key; public data exposure; ransomware and backup integrity
- Tabletop exercises: clocks, injects, scribes, time-to-contain

### AI and LLM application threats

- Security goals for ML systems: confidentiality, integrity and availability plus authentication, authorization and non-repudiation; trustworthy-ML dimensions (fairness, toxicity, safety, sustainability, explainability); threat models by attacker knowledge (white-box, black-box) and goal
- Prompt safety (harmful outputs) versus prompt security (attacks on the application); misinformation as harmful output: fluent wrong answers and invented citations, checked by testing each claim against the retrieved sources; measured as the share of claims on a labelled question set that the retrieved sources do not support, with abstention or a stated uncertainty when no source supports a claim
- Direct and indirect prompt injection; separating instructions from data; output as untrusted input; improper output handling: model text rendered as HTML, run in a shell, or passed to SQL or a template without encoding and validation, so the model's output becomes an injection vector
  - Indirect channels: poisoned documents, emails and calendar invites, API responses, résumés
  - Impacts: data exfiltration, remote tool execution, denial of service, social engineering
- Prompt leaking: exposure of system prompts, intellectual property and reconnaissance for further attacks; a system prompt is not a secret store, so no credential or access rule may depend on it staying hidden
- **Jailbreaking**
  - Taxonomy: language strategies (payload smuggling, modified instructions, stylized prompts and responses); rhetoric (innocent purpose, persuasion, alignment hacking, conversational coercion, Socratic questioning); imaginary worlds (hypotheticals, storytelling, role-play, world building); operational exploitation (many-shot examples, "unrestricted model" personas, meta-prompting)
  - White-box attacks: HotFlip gradient-guided flips; TextFooler synonym substitution; greedy coordinate gradient (GCG) adversarial suffixes optimized toward an affirmative reply, transferring across models, measured by attack success rate on AdvBench; AutoDAN readable suffixes
  - Black-box attacks: translation into low-resource languages; past-tense reformulation; context contamination with harmful in-context demonstrations; DeepWordBug character perturbations; PAIR (an attacker model refining prompts against a judge in a few dozen queries); instruction-centric harmful requests; multilingual evaluation: attack success rate measured per language, since alignment is thinner in low-resource languages, so an English-only safety suite overstates the protection
  - Red teaming versus blue teaming
- Tool and agent abuse; excessive agency
- RAG data leakage; authorization at retrieval; per-tenant indexes; vector and embedding weaknesses: poisoned chunks ranked high by similarity, embedding inversion recovering text from stored vectors, and tenant filters enforced inside the index query rather than after retrieval; access-control metadata stored on each chunk and applied as a filter predicate inside the query, since filtering a top-k list after retrieval can leak result counts and under-fill the answer
- Model and data poisoning, including poisoned federated updates; backdoors and trojan triggers; model hijacking; malicious serialized model files; signed models and private registries
- Model extraction by query-based distillation
- Shadow AI and sensitive pastes; secrets exposed to code assistants; legal and intellectual-property risk
- Adversarial examples (FGSM and optimization attacks) and robust training
- Membership inference and differentially private training
- The OWASP Top 10 for LLM Applications
- Unbounded consumption (OWASP LLM10): inference, tool calls and agent loops that spend without limit, costing money or starving other users; caps on input and output tokens per request, per session and per tenant; a bound on agent steps and tool-call depth; queue length and concurrency limits; spend alerts and a kill switch; cost metered per request and attributed to a key, so that one runaway client is visible; denial of wallet as the economic form of the attack
- Benchmark and training-data contamination: test items found in pretraining, fine-tuning or retrieval data inflate reported scores; detected by n-gram or embedding overlap between test items and the training corpus, canary strings planted in held-out sets, and private evaluation sets that never leave the evaluator; any known overlap rate reported alongside the score

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
- From scratch: a recovery-code store with hashed single-use codes and a regeneration that invalidates the old batch, plus a stale-authorization test in which a token minted before its role was revoked is refused after the change; each rule written as a failing test before its code
- **Reasoning drills**
  - Name the cheapest attack on a design before listing its defences
  - Reduce a protocol's security to a stated assumption, then find the attack when that assumption is dropped
  - Estimate the cost in money and time of brute-forcing a key or password space
  - Decide the residual risk to accept, as a decision record with review triggers
  - Predict which requests succeed when a retired refresh token is replayed after rotation, and which family is revoked, then check the prediction against the implementation
  - Given a password-reset link built from the request's Host header, name the one check that stops the poisoned link and the layer where it runs
  - Decide whether an open dynamic client registration endpoint needs an initial access token, and what a stolen registration access token can still do
