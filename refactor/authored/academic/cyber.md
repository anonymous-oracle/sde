@@@ align-row
| MIT 6.1600 Foundations of Computer Security · Boneh and Shoup, *A Graduate Course in Applied Cryptography*, version 0.6 (2023) | §10 academic pass (CRA.1…CRA.10) over CR-01…CR-19; TH, AU, SC |
@@@ u-row
| MIT 6.1600 | Security definitions; crypto proofs; authentication; isolation; side channels | §10 (CRA.1…CRA.10), CR-01…CR-19, TH-*, AU-*, SC-* |
@@@ section
## 10. Academic depth (rule 0.4.10)

The academic pass of this companion: cryptography with definitions and proofs, at the depth of Stanford CS 255, MIT 6.1600 and Berkeley CS 161 (main course §0.6 and §0.5 here). Each block is taught after the engineering pass of the CR cards it names. It is the formal layer that the main course's A10.D3 points to. Problems CRA-P1…CRA-P10 are in §10.11, with keys in Appendix K under "K-academic" (after the attempt only). Rule 0.4.10: a block is `mastered` only when one proof problem and one computational problem in it pass. Notation: ⊕ is XOR, |x| is the length of x, and "negligible" means smaller than any inverse polynomial in the security parameter.

### 10.1 CRA.1 · Provable security (deepens CR-01)

- A security definition is a game between a challenger and an efficient (probabilistic polynomial-time) adversary. The adversary's advantage is how much better than guessing it wins. A scheme is secure when every efficient adversary's advantage is negligible.
- Proof by reduction: "if an adversary A breaks the scheme with advantage ε, then an algorithm B built from A breaks the assumption with advantage close to ε". Its contrapositive is the security theorem. A proof is only as strong as its assumption and its model.
- Computational indistinguishability and the hybrid argument: if each of k neighbouring distributions is ε-close, the ends are kε-close.
- Kerckhoffs's principle as a modelling rule: the adversary knows the algorithm; only the key is secret.

### 10.2 CRA.2 · Perfect secrecy (deepens CR-01, CR-02)

- Shannon's definition: for every two messages m₀, m₁ and every ciphertext c, P(E(k, m₀) = c) = P(E(k, m₁) = c) over a uniform key.
- The one-time pad is perfectly secret (CRA-P1). Shannon's theorem: perfect secrecy needs at least as many keys as messages, |K| ≥ |M| (CRA-P2), which is why practical ciphers settle for computational security.
- The two-time pad: reusing a pad gives c₁ ⊕ c₂ = m₁ ⊕ m₂, and the same failure reappears as nonce reuse in CTR and GCM (CR-04).

### 10.3 CRA.3 · Pseudorandomness and chosen-plaintext security (deepens CR-03, CR-07)

- Pseudorandom generators, pseudorandom functions (PRFs) and pseudorandom permutations (PRPs); AES modelled as a PRP.
- The PRP/PRF switching lemma: an adversary making q queries distinguishes a random permutation from a random function on n-bit blocks with advantage at most q²/2ⁿ⁺¹ — the birthday bound (main course A2.D5), and the reason 64-bit block ciphers are retired.
- IND-CPA: a deterministic scheme cannot be CPA-secure (CRA-P4), so secure encryption is randomized or nonce-based. ECB fails even without chosen plaintexts; CTR mode is CPA-secure when the block cipher is a PRF and counters never repeat.

### 10.4 CRA.4 · Integrity and authenticated encryption (deepens CR-04, CR-06)

- MAC security (existential unforgeability under chosen-message attack, EUF-CMA). CBC-MAC is secure only for fixed-length messages; HMAC is a PRF under assumptions on the compression function (Bellare, Canetti and Krawczyk, 1996).
- Authenticated encryption = CPA security plus ciphertext integrity, and it implies CCA security. Generic composition (Bellare and Namprempre, 2000): encrypt-then-MAC with independent keys always gives authenticated encryption; MAC-then-encrypt does not in general (the padding-oracle history of CR-03).
- AES-GCM and ChaCha20-Poly1305 as nonce-based authenticated encryption with associated data; the security bound collapses on nonce reuse.

### 10.5 CRA.5 · Hash functions (deepens CR-05)

- Collision resistance, second-preimage resistance and preimage resistance, and the implications between them.
- The generic birthday attack finds a collision in about 2^(n/2) evaluations of an n-bit hash, so a 256-bit hash gives 128-bit collision security.
- Merkle–Damgård: a collision-resistant compression function gives a collision-resistant hash; the same structure causes length extension, which is why HMAC exists and why SHA-3's sponge does not need it. The random-oracle model, named with its caveat: a proof in it is a heuristic.

### 10.6 CRA.6 · Public-key encryption (deepens CR-08, CR-09)

- Groups, generators and the discrete-logarithm, computational Diffie–Hellman (CDH) and decisional Diffie–Hellman (DDH) assumptions; Diffie–Hellman key exchange and why it is secure only against a passive attacker.
- ElGamal encryption is IND-CPA-secure under DDH (proof sketch by reduction).
- RSA as a trapdoor permutation, with its correctness from Euler's theorem (main course A2.D3); textbook RSA is deterministic and malleable (CRA-P8); RSA-OAEP is CCA-secure in the random-oracle model.
- Hybrid encryption (the KEM/DEM paradigm): public-key encryption carries a fresh symmetric key, and authenticated encryption carries the data (CR-14's envelope encryption is the same shape).

### 10.7 CRA.7 · Digital signatures (deepens CR-10)

- EUF-CMA for signatures; hash-and-sign and why the hash must be collision-resistant.
- Schnorr signatures from an identification protocol through the Fiat–Shamir transform; ECDSA and EdDSA.
- Nonce reuse in ECDSA reveals the private key by two lines of algebra (CRA-P5); Ed25519 derives its nonce deterministically from the key and the message to remove that failure.

### 10.8 CRA.8 · Key exchange and protocol analysis (deepens CR-08, CR-12, CR-17)

- Authenticated key exchange: what "the key is known only to the intended peer" means; forward secrecy (a later key compromise does not reveal past sessions) and the SIGMA design (sign-and-MAC) that TLS 1.3 follows.
- The TLS 1.3 key schedule as repeated HKDF extract-and-expand (CR-05); why 0-RTT data is replayable (CR-12).
- Formal analysis: TLS 1.3 was analysed with the Tamarin prover and in computational models during its design, and those analyses found flaws in drafts before standardization (Cremers et al., 2016–2017) `(verify)`. The Dolev–Yao model is main course A10.D4.

### 10.9 CRA.9 · Passwords, entropy and cost (deepens CR-07, CR-13)

- Entropy of a uniformly chosen secret: log₂ of the number of choices. A human-chosen password has far less guessing entropy than its length suggests.
- Memory-hard functions (scrypt, Argon2id) raise the attacker's cost per guess on parallel hardware by forcing memory as well as time; the cost model is area × time.
- Salts stop precomputation across users; a pepper held outside the database adds a secret an attacker must also steal.

### 10.10 CRA.10 · Quantum threats and post-quantum cryptography (deepens CR-19)

- Shor's algorithm breaks RSA and elliptic-curve discrete logarithms in polynomial time on a large fault-tolerant quantum computer. Grover's algorithm gives only a square-root speed-up on key search, so AES-256 keeps about 128-bit security.
- NIST published the first post-quantum standards in August 2024: ML-KEM (FIPS 203, lattice-based key encapsulation), ML-DSA (FIPS 204, lattice-based signatures) and SLH-DSA (FIPS 205, hash-based signatures). Hybrid key exchange (classical plus ML-KEM) is the migration step already deployed in TLS.
- "Harvest now, decrypt later" is why confidentiality migrates before signatures.
- Readings for the whole pass: Boneh and Shoup, *A Graduate Course in Applied Cryptography*, version 0.6 (2023), parts I–III; Katz and Lindell, *Introduction to Modern Cryptography*, 3rd ed. (2020); Anderson, *Security Engineering*, 3rd ed. (2020), chapters 5 and 21 `(verify)`.

### 10.11 Problem set (CRA-P1…CRA-P10)

- **CRA-P1** · proof · Prove that the one-time pad over n-bit strings is perfectly secret.
- **CRA-P2** · proof · Prove Shannon's bound: if an encryption scheme is perfectly secret then |K| ≥ |M|.
- **CRA-P3** · compute · A service picks a random 64-bit nonce per message. After about how many messages is a repeated nonce more likely than not? A 96-bit random GCM nonce is used for 2³² messages; estimate the collision probability.
- **CRA-P4** · proof · Show that no deterministic encryption scheme is IND-CPA-secure, by giving an adversary and its advantage.
- **CRA-P5** · derive · Two ECDSA signatures (r, s₁) on hash h₁ and (r, s₂) on hash h₂ used the same nonce k (so the same r), with sᵢ = k⁻¹(hᵢ + r·d) mod n. Recover k and the private key d.
- **CRA-P6** · compute · Two messages were encrypted under AES-CTR with the same key and the same nonce. Show what an eavesdropper learns from the two ciphertexts, and what one known plaintext gives away.
- **CRA-P7** · compute · Textbook RSA with p = 61, q = 53, e = 17. Compute n, φ(n), d and the encryption of m = 65. Check that decryption returns 65.
- **CRA-P8** · proof · Using CRA-P7's key, show that textbook RSA is malleable: from the ciphertext of m, build the ciphertext of 2m without the private key.
- **CRA-P9** · compute · How many bits of entropy does a password of 10 characters drawn uniformly from 62 letters and digits have? What work does Grover's algorithm need against AES-128 and against AES-256?
- **CRA-P10** · compute · AES is used as a PRF on 2³² blocks. Bound the advantage lost by the PRP/PRF switching lemma. What is the bound for a 64-bit block cipher on the same number of blocks, and what does it mean?
@@@ keys
### K-academic (CRA-P1…CRA-P10, §10.11)

- **CRA-P1** — Expected: for any m and c, exactly one key gives E(k, m) = c, namely k = m ⊕ c, so P(E(k, m) = c) = 2⁻ⁿ for every m: the ciphertext distribution does not depend on the message. · Wrong: "it is secure because the key is random" — the proof needs the key to be used once and to be as long as the message.
- **CRA-P2** — Expected: fix a ciphertext c with nonzero probability. If |K| < |M|, decrypting c under every key gives fewer than |M| messages, so some m' is never a decryption of c; then P(E(k, m') = c) = 0 while it is positive for some other message, contradicting perfect secrecy. · Wrong: "the key must be random" — randomness is not length; the bound is a counting argument.
- **CRA-P3** — Expected: 50% collision chance near 1.18 × √(2⁶⁴) = 1.18 × 2³² ≈ 5.1 × 10⁹ messages. For 96-bit nonces and 2³² messages, P ≈ q²/2N = 2⁶⁴ / 2⁹⁷ = 2⁻³³ ≈ 1.2 × 10⁻¹⁰, which is why NIST limits random-nonce GCM to 2³² invocations per key. · Wrong: 2⁶³ messages — half the space is the wrong intuition; collisions arrive near the square root.
- **CRA-P4** — Expected: the adversary queries the encryption oracle on m₀, receiving c₀; it then submits (m₀, m₁) as the challenge and answers "0" exactly when the challenge ciphertext equals c₀. It wins with probability 1, advantage 1. · Wrong: "deterministic is fine if the key is secret" — the attack never learns the key.
- **CRA-P5** — Expected: s₁ − s₂ = k⁻¹(h₁ − h₂), so k = (h₁ − h₂)(s₁ − s₂)⁻¹ mod n; then d = (s₁·k − h₁)·r⁻¹ mod n. · Wrong: "nonce reuse only links the two signatures" — it discloses the private key.
- **CRA-P6** — Expected: both use the same keystream K, so c₁ ⊕ c₂ = m₁ ⊕ m₂: the XOR of the plaintexts leaks, and knowing m₁ gives m₂ = c₁ ⊕ c₂ ⊕ m₁ outright. · Wrong: "without the key nothing leaks" — the keystream cancels.
- **CRA-P7** — Expected: n = 3233, φ(n) = 60 × 52 = 3120, d = 17⁻¹ mod 3120 = 2753 (17 × 2753 = 46,801 = 15 × 3120 + 1), c = 65¹⁷ mod 3233 = 2790, and 2790²⁷⁵³ mod 3233 = 65. · Wrong: φ(n) = 3233 − 1 — that holds only for prime n.
- **CRA-P8** — Expected: c' = c · 2¹⁷ mod 3233 decrypts to (m^e · 2^e)^d = 2m mod n, so from 2790 the attacker builds the ciphertext of 130 without d. · Wrong: "RSA is secure because factoring is hard" — malleability needs no factoring; OAEP padding removes it.
- **CRA-P9** — Expected: 10 × log₂ 62 ≈ 59.5 bits. Grover needs about 2⁶⁴ sequential quantum operations for AES-128 and about 2¹²⁸ for AES-256, which is why AES-256 is the post-quantum recommendation. · Wrong: "Grover halves the key length, so AES-128 has 64 bits and is broken today" — 2⁶⁴ sequential quantum steps are far from practical, but the margin is thin.
- **CRA-P10** — Expected: q²/2ⁿ⁺¹ = 2⁶⁴/2¹²⁹ = 2⁻⁶⁵ for 128-bit blocks, which is negligible. For 64-bit blocks: 2⁶⁴/2⁶⁵ = 1/2, so the bound is useless; in practice the birthday collision leaks plaintext (the Sweet32 attack on 64-bit ciphers, 2016). · Wrong: "the bound depends only on the key size" — it depends on the block size.
