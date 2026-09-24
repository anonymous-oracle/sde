# Records for go-language-companion.md (R2c-bis, 2026-09-24)

Bookkeeping only, not course material. The Go companion has no input in `inputs-original/`; its D3 baseline is the R2c source, frozen at `outputs/r2c/go-language-companion.r2c.md`. R2c-bis (learner decision D13) extended some of its lines in place: module counts and ranges for GO-28 and GO-29, the involved-problem step, new owner rows. Each entry below keeps the R2c line verbatim and names the line that now carries its content. `verify.py` checks that every non-blank R2c line is either in the current source or here.

**G1** · D13 · R2c source line 3 → current source line 3 (similarity 0.85)

````text
Built September 24, 2026. Sources: *The Go Programming Language Specification*; *The Go Memory Model* (the 2022 revision); *Effective Go* and the Go Code Review Comments; the standard-library documentation and the release notes of Go 1.18–1.27; Alan Donovan & Brian Kernighan — *The Go Programming Language* (2015); Katherine Cox-Buday — *Concurrency in Go* (2017); Jon Bodner — *Learning Go*, 2nd ed. (2024); C. A. R. Hoare — "Communicating Sequential Processes" (1978); Rob Pike — "Concurrency is not parallelism" (2012); Russ Cox — the Go modules and minimal-version-selection design notes; Sedgewick & Wayne — *Algorithms*, 4th ed., for the data-structure labs.
````

now:

````text
Built September 24, 2026. Sources: *The Go Programming Language Specification*; *The Go Memory Model* (the 2022 revision); *Effective Go* and the Go Code Review Comments; the standard-library documentation and the release notes of Go 1.18–1.27; Alan Donovan & Brian Kernighan — *The Go Programming Language* (2015); Katherine Cox-Buday — *Concurrency in Go* (2017); Jon Bodner — *Learning Go*, 2nd ed. (2024); C. A. R. Hoare — "Communicating Sequential Processes" (1978); Rob Pike — "Concurrency is not parallelism" (2012); Russ Cox — the Go modules and minimal-version-selection design notes; Sedgewick & Wayne — *Algorithms*, 4th ed., for the data-structure labs; for GO-28 and GO-29, RFC 4226 (HOTP), RFC 6238 (TOTP), RFC 7636 (PKCE), RFC 6749 (OAuth 2.0), RFC 7515 and RFC 7519 (JWS, JWT), RFC 9106 (Argon2), OpenID Connect Core 1.0, and the cookie-prefix rules of the RFC 6265bis draft.
````

**G2** · D13 · R2c source line 10 → current source line 10 (similarity 0.77)

````text
This part is a complement to the main course, not a second course. It supplies one thing the main course needs everywhere but teaches nowhere: **the implementation language**. Go is the suite's language for application code — services, build labs that write a program, and capstones (rule 0.4.9 in §0.6); Python stays the first language of A3, the language of the machine-learning track, and the language of labs already written in Python. This part teaches Go as a language — its grammar, its semantics, its runtime and its toolchain — and, at every construct, what it does *differently* from Python, Java, C and JavaScript, because the bugs a newcomer writes in Go are almost all habits carried across from another language. It supplies content; it does not relax the teaching rhythm.
````

now:

````text
This part is a complement to the main course, not a second course. It supplies one thing the main course needs everywhere but teaches nowhere: **the implementation language**. Go is the suite's language for application code — services, build labs that write a program, and capstones (rule 0.4.9 in §0.6); Python stays the first language of A3, the language of the machine-learning track, and the language of labs already written in Python. This part teaches Go as a language — its grammar, its semantics, its runtime and its toolchain — and, at every construct, what it does *differently* from Python, Java, C and JavaScript, because the bugs a newcomer writes in Go are almost all habits carried across from another language. Its last two modules, GO-28 and GO-29, apply the language to the two things most services must get right — authentication and payment integration — building each piece from scratch against its published test vectors, so the mechanism is visible; the attacks, the cryptography and the ledger rules stay with their owners. Every module ends with one involved problem for the learner to solve alone (rule 8 of §0.2). It supplies content; it does not relax the teaching rhythm.
````

**G3** · D13 · R2c source line 31 → current source line 33 (similarity 0.99)

````text
6. **Close** — tick the box; record any carried-over habit in the misconception register (rule 0.4.5).
````

now:

````text
7. **Close** — tick the box; record any carried-over habit in the misconception register (rule 0.4.5).
````

**G4** · D13 · R2c source line 36 → current source line 38 (similarity 0.84)

````text
`GO-nn` module · `GO-Em.n` exercise (§10) · `GO-CAPn` capstone (§11). The unlock list below is binding (rule 0.4.9): a construct is usable only from its module on.
````

now:

````text
`GO-nn` module · `GO-Em.n` exercise (§10) · `GO-Pnn` involved problem (on each card; rubrics in §10.2) · `GO-CAPn` capstone (§11). The unlock list below is binding (rule 0.4.9): a construct is usable only from its module on.
````

**G5** · D13 · R2c source line 68 → current source line 72 (similarity 0.89)

````text
Card fields: **Core** (what is taught) · **Semantics and runtime** · **Contrast** (Python / Java / C / JavaScript) · **Pitfalls** · **GCP lens** (where Go meets the platform) · **Build lab** with its Lab Reality tag · **Check**.
````

now:

````text
Card fields: **Core** (what is taught) · **Semantics and runtime** · **Contrast** (Python / Java / C / JavaScript) · **Pitfalls** · **GCP lens** (where Go meets the platform) · **Build lab** with its Lab Reality tag · **Check** · **Involved problem** (`GO-Pnn`; its rubric is in §10.2).
````

**G6** · D13 · R2c source line 93 → current source line 98 (similarity 0.96)

````text
| **Total** | | **27** |
````

now:

````text
| **Total** | | **29** |
````

**G7** · D13 · R2c source line 95 → current source line 100 (similarity 0.78)

````text
Plus the contrast atlas (§9), the exercise bank with keys (§10), three capstones (§11) and the dependency gate (§12).
````

now:

````text
Plus one involved problem per module (on each card, rubrics in §10.2), the contrast atlas (§9), the exercise bank with keys (§10), three capstones (§11) and the dependency gate (§12).
````

**G8** · D13 · R2c source line 105 → current source line 110 (similarity 0.96)

````text
| A5 Computer Networking (HTTP, TLS) | GO-21 | A5 owns HTTP and TLS; GO-21 owns `net/http` and `crypto/tls`. The Cloud Cybersecurity companion's DOS-05 build lab (the hardened server) runs on GO-21 |
````

now:

````text
| A5 Computer Networking (HTTP, TLS) | GO-21; GO-28 (cookies) | A5 owns HTTP and TLS; GO-21 owns `net/http` and `crypto/tls`. The Cloud Cybersecurity companion's DOS-05 build lab (the hardened server) runs on GO-21 |
````

**G9** · D13 · R2c source line 107 → current source line 112 (similarity 0.99)

````text
| A7 Software Architecture & APIs | GO-11 recalled for the Go rendering of patterns; GO-21, GO-22, GO-23 | The Design Patterns companion owns the patterns; this part shows their Go shape: implicit interfaces (DIP, ISP), embedding instead of inheritance (F-03), functional options (DP-04 Builder), `http.Handler` middleware (DP-12 Decorator, DP-18 Chain of Responsibility), `sync.Once` (DP-01 Singleton), iterators (DP-20 Iterator). The SQL companion's OD-09 `cursorpage` lab runs on GO-22 |
````

now:

````text
| A7 Software Architecture & APIs | GO-11 recalled for the Go rendering of patterns; GO-21, GO-22, GO-23; GO-28, GO-29 | The Design Patterns companion owns the patterns; this part shows their Go shape: implicit interfaces (DIP, ISP), embedding instead of inheritance (F-03), functional options (DP-04 Builder), `http.Handler` middleware (DP-12 Decorator, DP-18 Chain of Responsibility), `sync.Once` (DP-01 Singleton), iterators (DP-20 Iterator). The SQL companion's OD-09 `cursorpage` lab runs on GO-22 |
````

**G10** · D13 · R2c source line 108 → current source line 113 (similarity 0.67)

````text
| A8 Databases & Data Modeling | GO-22 | the SQL companion owns SQL; GO-22 owns `database/sql` |
````

now:

````text
| A8 Databases & Data Modeling | GO-22; GO-29 (the ledger in Go) | the SQL companion owns SQL and its DD-03 owns the ledger rules; GO-22 owns `database/sql`, GO-29 the Go that follows DD-03 |
````

**G11** · D13 · R2c source line 109 → current source line 114 (similarity 0.87)

````text
| A9 Distributed Systems Theory | GO-17 (deadline propagation), GO-19 (bounded concurrency, retries); GO-CAP2 | A9 owns the theory; U5 owns concurrency theory in general |
````

now:

````text
| A9 Distributed Systems Theory | GO-17 (deadline propagation), GO-19 (bounded concurrency, retries), GO-29 (idempotency keys, at-least-once webhooks); GO-CAP2 | A9 owns the theory; U5 owns concurrency theory in general |
````

**G12** · D13 · R2c source line 110 → current source line 115 (similarity 0.80)

````text
| A10 Security & Cryptography | GO-13 (`html/template`, `os.Root`), GO-21 (`CrossOriginProtection`, TLS config), GO-25 (`govulncheck`) | the Cloud Cybersecurity companion owns attacks and crypto; CR-13's Argon2id lab runs in Go after GO-07 and GO-21 |
````

now:

````text
| A10 Security & Cryptography | GO-13 (`html/template`, `os.Root`), GO-21 (`CrossOriginProtection`, TLS config), GO-25 (`govulncheck`), GO-28 (authentication built from scratch) | the Cloud Cybersecurity companion owns attacks and crypto (AU-01…AU-10, CR-05…CR-07, CR-13, CR-16); CR-13's Argon2id lab runs in Go after GO-07 and GO-21, and GO-28 builds it into a login service |
````

**G13** · D13 · R2c source line 132 → current source line 137 (similarity 0.84)

````text
| Password KDFs | the Cloud Cybersecurity companion (CR-13) | CR-13's build lab written in Go (after GO-07 and GO-21): `golang.org/x/crypto/argon2` in a Go service |
````

now:

````text
| Password KDFs | the Cloud Cybersecurity companion (CR-13) | CR-13's build lab written in Go (after GO-07 and GO-21): `golang.org/x/crypto/argon2` in a Go service; GO-28 wraps it in a versioned record with rehash-on-login |
````

**G14** · D13 · R2c source line 335 → current source line 365 (similarity 0.88)

````text
## 8. Engineering with Go: tests, services, performance, delivery (GO-20…GO-27)
````

now:

````text
## 8. Engineering with Go: tests, services, performance, delivery, identity and money (GO-20…GO-29)
````

**G15** · D13 · R2c source line 457 → current source line 523 (similarity 0.97)

````text
## 10. Exercise bank (GO-E1.1…GO-E27.2)
````

now:

````text
## 10. Exercise bank (GO-E1.1…GO-E29.2)
````

**G16** · D13 · R2c source line 596 → current source line 706 (similarity 1.00)

````text
10. Cross-part: the SQL companion's OD-09 `cursorpage` lab in Go needs GO-22; the Cloud Cybersecurity companion's DOS-05 build lab needs GO-21, and CR-13's needs GO-07 and GO-21; the System Design Primer's O01, O02 and O07 in Go need GO-27.
````

now:

````text
12. Cross-part: the SQL companion's OD-09 `cursorpage` lab in Go needs GO-22; the Cloud Cybersecurity companion's DOS-05 build lab needs GO-21, and CR-13's needs GO-07 and GO-21; the System Design Primer's O01, O02 and O07 in Go need GO-27.
````

**G17** · D13 · R2c source line 605 → current source line 717 (similarity 0.85)

````text
- **Where the material came from.** The module list follows the Go nodes of the learner's Nasiko course notes (orientation and tooling; foundations I and II; types, interfaces and generics; files and I/O; CLI and logging; concurrency I and II; rate limiting; testing and reflection; advanced concurrency; HTTP; the REST project; Protocol Buffers; gRPC; observability; security; deployment), re-cut into 27 modules with a contrast line each and bound to the main course. Not brought in: the Nasiko control-plane reconstruction phases and its service specifications, the machine-learning and mathematics tracks, the payments addendum, and the contest problem ladder — those belong to a different project, and the data-structure and database material they carry is already owned by A4, U2, the System Design Primer and the SQL companion.
````

now:

````text
- **Where the material came from.** The module list follows the Go nodes of the learner's Nasiko course notes (orientation and tooling; foundations I and II; types, interfaces and generics; files and I/O; CLI and logging; concurrency I and II; rate limiting; testing and reflection; advanced concurrency; HTTP; the REST project; Protocol Buffers; gRPC; observability; security; deployment), re-cut into 27 modules with a contrast line each and bound to the main course; GO-28 and GO-29 were added later, at the learner's request, and are written from the standards listed above and from the sibling parts' owner modules (AU, CR, PV-03, AB-06, AB-07, DD-03, SD-28), not from those notes. Not brought in: the Nasiko control-plane reconstruction phases and its service specifications, the machine-learning and mathematics tracks, the payments addendum (payments are taught instead by GO-29, from the owners named above), and the contest problem ladder — those belong to a different project, and the data-structure and database material they carry is already owned by A4, U2, the System Design Primer and the SQL companion.
````

## Journaled build edits (written by r2b_build.py; do not edit below this line)

Journaled edits the build applies to the Go companion after it is assembled from its authored source (R4 onward). Each entry names the journal number (outputs/r2b/journal.jsonl), the rule and the class, and keeps the line as the authored source has it.

**J925** · R4-11 · anchor-rewrite

````text
2. **One concept, one teaching.** Concepts owned elsewhere are recalled in one line, never re-taught: data-structure theory (A4, U2), HTTP (A5), concurrency theory in general (U5), design patterns (the Design Patterns companion), the SQL itself (the SQL companion), attacks and cryptography (the Cloud Cybersecurity companion). This part owns only the Go rendering of each: the syntax, the semantics, the runtime behaviour and the idiom.
````

**J926** · R4-11 · anchor-rewrite

````text
| A9 Distributed Systems Theory | GO-17 (deadline propagation), GO-19 (bounded concurrency, retries), GO-29 (idempotency keys, at-least-once webhooks); GO-CAP2 | A9 owns the theory; U5 owns concurrency theory in general |
````

**J927** · R4-11 · anchor-rewrite

````text
| U4 Programming Languages & Paradigms (reserved) | GO-09, GO-11, GO-12 are the worked instance: value semantics, structural typing, parametric polymorphism | U4 is reserved and not written; say so plainly (the learner preferences, §0.5) |
````

**J928** · R4-11 · anchor-rewrite

````text
| U5 Concurrency & Parallel Computing (reserved) | GO-15…GO-19 are the worked instance: CSP, the memory model, data races, deadlock | U5 is reserved and not written; say so plainly |
````

**J929** · R4-11 · anchor-rewrite

````text
| Races, locks, deadlock, memory models in general | U5 | GO-15…GO-19: goroutines, channels, `sync`, the Go memory model, the race detector |
````

**J930** · R4-11 · anchor-rewrite

````text
| Garbage-collection theory | U4 | GO-09: Go's collector, escape analysis, `GOGC`/`GOMEMLIMIT` |
````

**J931** · R4-11 · anchor-rewrite

````text
| Data-structure theory and costs | A4 / U2 | GO-27: the Go implementations |
````

**J932** · R4-11 · anchor-rewrite

````text
U5 (reserved) owns concurrency theory in general and A9 owns distributed-systems theory. These five modules own how Go does it: the goroutine, the channel, `select`, `context`, the `sync` package, the Go memory model and the race detector. Order is enforced: GO-15 → GO-16 → GO-17 → GO-18 → GO-19.
````

**J933** · R4-11 · anchor-rewrite

````text
#### GO-03 · Types, zero values, constants and conversions — stitch: A3 · A1 · M5
````

**J934** · R4-11 · anchor-rewrite

````text
#### GO-09 · Pointers, values and memory — stitch: A3 · A6 · U4
````

**J935** · R4-11 · anchor-rewrite

````text
#### GO-12 · Generics and iterators — stitch: A3 · A4 · U4
````

**J936** · R4-11 · anchor-rewrite

````text
#### GO-15 · Goroutines and the scheduler — stitch: A6 · U5
````

**J937** · R4-11 · anchor-rewrite

````text
#### GO-16 · Channels and `select` — stitch: A9 · U5
````

**J938** · R4-11 · anchor-rewrite

````text
#### GO-18 · `sync`, `sync/atomic` and the Go memory model — stitch: U5 · A9
````

**J939** · R4-11 · anchor-rewrite

````text
#### GO-19 · Concurrency patterns and failure modes — stitch: A9 · U5 · C7
````

**J940** · R4-11 · anchor-rewrite

````text
#### GO-20 · Testing, benchmarks and fuzzing — stitch: C4 · U6
````

**J941** · R4-11 · anchor-rewrite

````text
#### GO-26 · Reflection, `unsafe` and cgo (recognition) — stitch: U4 · A10
````

**J942** · R4-11 · anchor-rewrite

````text
#### GO-27 · Data structures in Go (the A4 implementations) — stitch: A4 · U2
````

**J943** · R4-11 · anchor-rewrite

````text
- **Core:** A4 owns the concepts and costs and U2 their analysis; this module owns only the Go. Stack, queue and deque on slices; a ring buffer; a singly and a doubly linked list (and `container/list`); a hash map with separate chaining; an LRU cache (map plus `container/list`); a binary heap through `container/heap` (implementing `heap.Interface`); a priority queue with an index for decrease-key; union-find with union by rank and path compression; a trie; a binary search tree; `sort.Slice`, `slices.SortFunc` and `slices.BinarySearch` (and `sort.Search` for binary search on a predicate).
````

**J944** · R4-11 · anchor-rewrite

````text
- [ ] **GO-CAP2 · The concurrent event worker.** *After:* GO-17, GO-19, GO-22. *Stitch:* A9 · U5. A worker that consumes order events from a local queue (a Postgres table used as a queue with `FOR UPDATE SKIP LOCKED`, or a local emulator), processes them with bounded concurrency (`errgroup` with `SetLimit`), and is **idempotent**: each event ID is recorded in the same transaction as its effect, so redelivery changes nothing. Retries use exponential backoff with jitter under a context deadline; a poisoned event goes to a dead-letter table after N attempts. **Acceptance:** a test that delivers every event twice and checks the totals; a test that cancels the context mid-batch and checks that nothing is half-applied and no goroutine is left; `-race` clean; a goroutine profile taken under load, read aloud.
````

**J945** · R4-11 · anchor-rewrite

````text
- **Semantics and runtime:** **no implicit conversions**, not even `int32` to `int64` or `int` to `float64`: mixed-type arithmetic is a compile error and every conversion is written `T(x)`. **Untyped constants** have arbitrary precision (the specification requires at least 256 bits for integer constants) and take a type only where used: `const big = 1 << 100` is legal, `float64(big)` is fine, `int(big)` is a compile error. **Integer division truncates toward zero:** `-7/2` is `-3` and `-7%2` is `-1` `(checked on 1.27.1)`. **Signed overflow wraps** in two's complement and is defined behaviour: an `int8` holding 127, incremented, is -128 `(checked on 1.27.1)`. Integer division by a zero variable panics at run time; by a zero constant it does not compile. Floating point is IEEE 754 (recall M5 when it is written; the SQL companion's PQ-03 for decimals): `NaN != NaN`, and float division by a zero variable gives ±Inf. Go has no enum type: a named integer type plus an `iota` block, with no exhaustiveness check in `switch`.
````

**J946** · R4-11 · anchor-rewrite

````text
- **Where the material came from.** The module list follows the Go nodes of the learner's Nasiko course notes (orientation and tooling; foundations I and II; types, interfaces and generics; files and I/O; CLI and logging; concurrency I and II; rate limiting; testing and reflection; advanced concurrency; HTTP; the REST project; Protocol Buffers; gRPC; observability; security; deployment), re-cut into 27 modules with a contrast line each and bound to the main course; GO-28 and GO-29 were added later, at the learner's request, and are written from the standards listed above and from the sibling parts' owner modules (AU, CR, PV-03, AB-06, AB-07, DD-03, SD-28), not from those notes. Not brought in: the Nasiko control-plane reconstruction phases and its service specifications, the machine-learning and mathematics tracks, the payments addendum (payments are taught instead by GO-29, from the owners named above), and the contest problem ladder — those belong to a different project, and the data-structure and database material they carry is already owned by A4, U2, the System Design Primer and the SQL companion.
````
