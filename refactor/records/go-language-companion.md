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

R6 (2026-09-25, the learn-anything.xyz cross-check) extended GO-11 and GO-18 in place with sealed interfaces and progress guarantees; entries G18 onward keep the lines as they stood before, in the same form.

**G18** · R6 · R2c source line 242 → current source line 263 (similarity 0.85)

````text
- **Core:** an interface type is a method set. A type **satisfies an interface implicitly**, by having the methods; there is no `implements`. The check is static, at the point of assignment. Interfaces are small and owned by the consumer (`io.Reader` has one method). `any` is `interface{}`. Type assertion `v, ok := x.(T)` (without `ok` it panics on a mismatch), type switch `switch v := x.(type)`. A compile-time assertion: `var _ Store = (*PGStore)(nil)`. **Embedding:** a struct that embeds a type gets that type's fields and methods *promoted*; an interface that embeds interfaces takes the union (`io.ReadWriter`).
````

now:

````text
- **Core:** an interface type is a method set. A type **satisfies an interface implicitly**, by having the methods; there is no `implements`. The check is static, at the point of assignment. Interfaces are small and owned by the consumer (`io.Reader` has one method). `any` is `interface{}`. Type assertion `v, ok := x.(T)` (without `ok` it panics on a mismatch), type switch `switch v := x.(type)`. A compile-time assertion: `var _ Store = (*PGStore)(nil)`. A **sealed interface** has an unexported marker method, `type Event interface{ isEvent() }`, so only types in its own package can implement it: Go's nearest thing to a closed sum type, for payment events or AST nodes (GOT.2). **Embedding:** a struct that embeds a type gets that type's fields and methods *promoted*; an interface that embeds interfaces takes the union (`io.ReadWriter`).
````

**G19** · R6 · R2c source line 246 → current source line 267 (similarity 0.68)

````text
- **Pitfalls:** large interfaces declared by the producer "for mocking"; a pointer to an interface (`*io.Reader`), which is almost always wrong; embedding `sync.Mutex` in an exported type, which exports `Lock` and `Unlock` to every caller.
````

now:

````text
- **Pitfalls:** a type switch over a sealed interface with no failing `default`: the compiler does not check that every member has a case, and `go vet` is silent, so a member added later is ignored without warning `(checked on 1.27.1)`; large interfaces declared by the producer "for mocking"; a pointer to an interface (`*io.Reader`), which is almost always wrong; embedding `sync.Mutex` in an exported type, which exports `Lock` and `Unlock` to every caller.
````

**G20** · R6 · R2c source line 318 → current source line 346 (similarity 0.88)

````text
- **Semantics and runtime:** the **Go memory model** (the 2022 revision) defines *happens-before* through synchronising operations: a send on a channel happens before the matching receive completes; an unlock happens before the next lock; `Once.Do`'s function happens before any `Do` returns; atomic operations are sequentially consistent. **A data race** is two accesses to the same memory location from different goroutines, at least one a write, not ordered by happens-before. A race-free program behaves as if sequentially consistent ("DRF-SC"); a racy one does not. A race on a single machine word gives a stale or torn-free but unpredictable value; a race on a multi-word value — a slice, string or interface header — can produce a corrupted header and crash the program. A `Mutex` must not be copied after first use (`go vet` copylocks, GO-10). `WaitGroup.Add` must happen before the goroutine starts, not inside it. `sync.Pool` is a cache that the collector may empty at any time — never a free list you can count on. `sync.Map` pays off only for keys written once and read many times, or for disjoint key sets per goroutine; otherwise a map plus a `Mutex` is simpler and faster.
````

now:

````text
- **Semantics and runtime:** the **Go memory model** (the 2022 revision) defines *happens-before* through synchronising operations: a send on a channel happens before the matching receive completes; an unlock happens before the next lock; `Once.Do`'s function happens before any `Do` returns; atomic operations are sequentially consistent. **A data race** is two accesses to the same memory location from different goroutines, at least one a write, not ordered by happens-before. A race-free program behaves as if sequentially consistent ("DRF-SC"); a racy one does not. A race on a single machine word gives a stale or torn-free but unpredictable value; a race on a multi-word value — a slice, string or interface header — can produce a corrupted header and crash the program. A `Mutex` must not be copied after first use (`go vet` copylocks, GO-10). `WaitGroup.Add` must happen before the goroutine starts, not inside it. `sync.Pool` is a cache that the collector may empty at any time — never a free list you can count on. `sync.Map` pays off only for keys written once and read many times, or for disjoint key sets per goroutine; otherwise a map plus a `Mutex` is simpler and faster. **Progress guarantees** (main course A6.D4): a `Mutex` is blocking, since a goroutine descheduled while holding it stalls every waiter; a `CompareAndSwap` retry loop is lock-free (some goroutine always succeeds) but not wait-free (one goroutine can lose every race); `atomic.Int64.Add` has no loop at all (GOT.5).
````

**G21** · R6 · R2c source line 320 → current source line 348 (similarity 0.68)

````text
- **Pitfalls:** "it's only a counter" races; locking inside a method with a value receiver (it locks a copy); holding a lock across a channel send or an I/O call; double-checked locking hand-rolled instead of `sync.Once`.
````

now:

````text
- **Pitfalls:** "it's only a counter" races; locking inside a method with a value receiver (it locks a copy); holding a lock across a channel send or an I/O call; double-checked locking hand-rolled instead of `sync.Once`; a hand-rolled lock-free structure that recycles nodes (a free list or `sync.Pool`), which brings back the ABA problem the collector otherwise prevents — use a `Mutex` until a profile (GO-24) shows contention.
````

**G22** · R6 · R2c source line 377 → current source line 411 (similarity 0.63)

````text
- **Core:** `runtime/pprof` and `net/http/pprof` (CPU, heap, allocations, goroutine, block and mutex profiles); `go tool pprof` (top, list, web, flame graphs); `runtime/trace` and `go tool trace`; `GODEBUG=gctrace=1`; profile-guided optimisation (a CPU profile saved as `default.pgo` in the main package directory is used by `go build` `(verify)` the file name); OpenTelemetry for Go (traces and metrics, context-propagated, GO-17); `slog` (GO-14) with trace IDs.
````

now:

````text
- **Core:** `runtime/pprof` and `net/http/pprof` (CPU, heap, allocations, goroutine, block and mutex profiles); `go tool pprof` (top, list, web, flame graphs); `runtime/trace` and `go tool trace`; `GODEBUG=gctrace=1`; profile-guided optimisation (a CPU profile saved as `default.pgo` in the main package directory is used by `go build` `(verify)` the file name); OpenTelemetry for Go (traces and metrics, context-propagated, GO-17); `slog` (GO-14) with trace IDs. Delve (`dlv debug`, `dlv test`, `dlv attach <pid>`, `dlv core` on a core dump) is the Go-aware debugger: it understands goroutines, channels and interfaces where gdb does not; build with `-gcflags=all="-N -l"` to turn off optimisation and inlining so variables are not optimised away `(verify)` the Delve commands. `GOTRACEBACK=all` prints every goroutine's stack on a fatal panic and `GOTRACEBACK=crash` also raises SIGABRT for a core dump; the default prints only the failing goroutine and exits with code 2 (from `go doc runtime`).
````

**G23** · R6 · R2c source line 387 → current source line 422 (similarity 0.80)

````text
- **Core:** cross-compilation by environment (`GOOS=linux GOARCH=arm64 go build`); `CGO_ENABLED=0` for a fully static binary when no package needs cgo; `-trimpath` (drops local paths); `-ldflags "-s -w -X main.version=…"`; build information embedded in every binary (`go version -m ./app`, `runtime/debug.ReadBuildInfo`, including module versions and VCS revision); multi-stage container builds into a distroless or `scratch` base; `govulncheck` (the Go vulnerability database, `golang.org/x/vuln`); GoReleaser for release automation.
````

now:

````text
- **Core:** cross-compilation by environment (`GOOS=linux GOARCH=arm64 go build`); `CGO_ENABLED=0` for a fully static binary when no package needs cgo; `-trimpath` (drops local paths); `-ldflags "-s -w -X main.version=…"`; build information embedded in every binary (`go version -m ./app`, `runtime/debug.ReadBuildInfo`, including module versions and VCS revision); multi-stage container builds into a distroless or `scratch` base; `govulncheck` (the Go vulnerability database, `golang.org/x/vuln`); GoReleaser for release automation. Lint beyond `go vet` with golangci-lint (one binary running `staticcheck`, `errcheck`, `gosec`, `revive` and many others from one configuration file checked into the repository) `(verify)` the linter set, pinned to one version in CI so a new linter release cannot fail an unchanged commit.
````

## Journaled build edits (written by r2b_build.py; do not edit below this line)

Journaled edits the build applies to the Go companion after it is assembled from its authored source (R4 onward). Each entry names the journal number (outputs/r2b/journal.jsonl), the rule and the class, and keeps the line as the authored source has it.

**J926** · R4-11 · anchor-rewrite

````text
2. **One concept, one teaching.** Concepts owned elsewhere are recalled in one line, never re-taught: data-structure theory (A4, U2), HTTP (A5), concurrency theory in general (U5), design patterns (the Design Patterns companion), the SQL itself (the SQL companion), attacks and cryptography (the Cloud Cybersecurity companion). This part owns only the Go rendering of each: the syntax, the semantics, the runtime behaviour and the idiom.
````

**J927** · R4-11 · anchor-rewrite

````text
| A9 Distributed Systems Theory | GO-17 (deadline propagation), GO-19 (bounded concurrency, retries), GO-29 (idempotency keys, at-least-once webhooks); GO-CAP2 | A9 owns the theory; U5 owns concurrency theory in general |
````

**J928** · R4-11 · anchor-rewrite

````text
| U4 Programming Languages & Paradigms (reserved) | GO-09, GO-11, GO-12 are the worked instance: value semantics, structural typing, parametric polymorphism | U4 is reserved and not written; say so plainly (the learner preferences, §0.5) |
````

**J929** · R4-11 · anchor-rewrite

````text
| U5 Concurrency & Parallel Computing (reserved) | GO-15…GO-19 are the worked instance: CSP, the memory model, data races, deadlock | U5 is reserved and not written; say so plainly |
````

**J930** · R4-11 · anchor-rewrite

````text
| Races, locks, deadlock, memory models in general | U5 | GO-15…GO-19: goroutines, channels, `sync`, the Go memory model, the race detector |
````

**J931** · R4-11 · anchor-rewrite

````text
| Garbage-collection theory | U4 | GO-09: Go's collector, escape analysis, `GOGC`/`GOMEMLIMIT` |
````

**J932** · R4-11 · anchor-rewrite

````text
| Data-structure theory and costs | A4 / U2 | GO-27: the Go implementations |
````

**J933** · R4-11 · anchor-rewrite

````text
U5 (reserved) owns concurrency theory in general and A9 owns distributed-systems theory. These five modules own how Go does it: the goroutine, the channel, `select`, `context`, the `sync` package, the Go memory model and the race detector. Order is enforced: GO-15 → GO-16 → GO-17 → GO-18 → GO-19.
````

**J934** · R4-11 · anchor-rewrite

````text
#### GO-03 · Types, zero values, constants and conversions — stitch: A3 · A1 · M5
````

**J935** · R4-11 · anchor-rewrite

````text
#### GO-09 · Pointers, values and memory — stitch: A3 · A6 · U4
````

**J936** · R4-11 · anchor-rewrite

````text
#### GO-12 · Generics and iterators — stitch: A3 · A4 · U4
````

**J937** · R4-11 · anchor-rewrite

````text
#### GO-15 · Goroutines and the scheduler — stitch: A6 · U5
````

**J938** · R4-11 · anchor-rewrite

````text
#### GO-16 · Channels and `select` — stitch: A9 · U5
````

**J939** · R4-11 · anchor-rewrite

````text
#### GO-18 · `sync`, `sync/atomic` and the Go memory model — stitch: U5 · A9
````

**J940** · R4-11 · anchor-rewrite

````text
#### GO-19 · Concurrency patterns and failure modes — stitch: A9 · U5 · C7
````

**J941** · R4-11 · anchor-rewrite

````text
#### GO-20 · Testing, benchmarks and fuzzing — stitch: C4 · U6
````

**J942** · R4-11 · anchor-rewrite

````text
#### GO-26 · Reflection, `unsafe` and cgo (recognition) — stitch: U4 · A10
````

**J943** · R4-11 · anchor-rewrite

````text
#### GO-27 · Data structures in Go (the A4 implementations) — stitch: A4 · U2
````

**J944** · R4-11 · anchor-rewrite

````text
- **Core:** A4 owns the concepts and costs and U2 their analysis; this module owns only the Go. Stack, queue and deque on slices; a ring buffer; a singly and a doubly linked list (and `container/list`); a hash map with separate chaining; an LRU cache (map plus `container/list`); a binary heap through `container/heap` (implementing `heap.Interface`); a priority queue with an index for decrease-key; union-find with union by rank and path compression; a trie; a binary search tree; `sort.Slice`, `slices.SortFunc` and `slices.BinarySearch` (and `sort.Search` for binary search on a predicate).
````

**J945** · R4-11 · anchor-rewrite

````text
- [ ] **GO-CAP2 · The concurrent event worker.** *After:* GO-17, GO-19, GO-22. *Stitch:* A9 · U5. A worker that consumes order events from a local queue (a Postgres table used as a queue with `FOR UPDATE SKIP LOCKED`, or a local emulator), processes them with bounded concurrency (`errgroup` with `SetLimit`), and is **idempotent**: each event ID is recorded in the same transaction as its effect, so redelivery changes nothing. Retries use exponential backoff with jitter under a context deadline; a poisoned event goes to a dead-letter table after N attempts. **Acceptance:** a test that delivers every event twice and checks the totals; a test that cancels the context mid-batch and checks that nothing is half-applied and no goroutine is left; `-race` clean; a goroutine profile taken under load, read aloud.
````

**J946** · R4-11 · anchor-rewrite

````text
- **Semantics and runtime:** **no implicit conversions**, not even `int32` to `int64` or `int` to `float64`: mixed-type arithmetic is a compile error and every conversion is written `T(x)`. **Untyped constants** have arbitrary precision (the specification requires at least 256 bits for integer constants) and take a type only where used: `const big = 1 << 100` is legal, `float64(big)` is fine, `int(big)` is a compile error. **Integer division truncates toward zero:** `-7/2` is `-3` and `-7%2` is `-1` `(checked on 1.27.1)`. **Signed overflow wraps** in two's complement and is defined behaviour: an `int8` holding 127, incremented, is -128 `(checked on 1.27.1)`. Integer division by a zero variable panics at run time; by a zero constant it does not compile. Floating point is IEEE 754 (recall M5 when it is written; the SQL companion's PQ-03 for decimals): `NaN != NaN`, and float division by a zero variable gives ±Inf. Go has no enum type: a named integer type plus an `iota` block, with no exhaustiveness check in `switch`.
````

**J947** · R4-11 · anchor-rewrite

````text
- **Where the material came from.** The module list follows the Go nodes of the learner's Nasiko course notes (orientation and tooling; foundations I and II; types, interfaces and generics; files and I/O; CLI and logging; concurrency I and II; rate limiting; testing and reflection; advanced concurrency; HTTP; the REST project; Protocol Buffers; gRPC; observability; security; deployment), re-cut into 27 modules with a contrast line each and bound to the main course; GO-28 and GO-29 were added later, at the learner's request, and are written from the standards listed above and from the sibling parts' owner modules (AU, CR, PV-03, AB-06, AB-07, DD-03, SD-28), not from those notes. Not brought in: the Nasiko control-plane reconstruction phases and its service specifications, the machine-learning and mathematics tracks, the payments addendum (payments are taught instead by GO-29, from the owners named above), and the contest problem ladder — those belong to a different project, and the data-structure and database material they carry is already owned by A4, U2, the System Design Primer and the SQL companion.
````

**J1091** · FDE-16 · anchor-rewrite

````text
| GO-21 | `net/http` server and client, `ServeMux` patterns, `http.Handler`, middleware, `crypto/tls` config, `signal.NotifyContext`, graceful shutdown |
````

**J1092** · FDE-16 · anchor-rewrite

````text
- **Build lab `[local]`:** the `shop.example` orders API skeleton (the reference application defined in the Cloud Cybersecurity companion): `GET /orders/{id}`, `POST /orders`, JSON in and out with a size limit, middleware for recovery, request ID and structured logging, the DOS-05 timeouts, `CrossOriginProtection`, graceful shutdown, and `httptest` tests for 200, 400, 404, 405 and 413.
````

**J1131** · R7-2 · §0.1–§0.3 replaced by the part's own §0 (generic rules are in the course guide)

````text
## 0. Read this first

### 0.1 Standing instruction (for Claude, every session)
This part is a complement to the main course, not a second course. It supplies one thing the main course needs everywhere but teaches nowhere: **the implementation language**. Go is the suite's language for application code — services, build labs that write a program, and capstones (rule 0.4.9 in §0.6); Python stays the first language of A3, the language of the machine-learning track, and the language of labs already written in Python. This part teaches Go as a language — its grammar, its semantics, its runtime and its toolchain — and, at every construct, what it does *differently* from Python, Java, C and JavaScript, because the bugs a newcomer writes in Go are almost all habits carried across from another language. Its last two modules, GO-28 and GO-29, apply the language to the two things most services must get right — authentication and payment integration — building each piece from scratch against its published test vectors, so the mechanism is visible; the attacks, the cryptography and the ledger rules stay with their owners. Every module ends with one involved problem for the learner to solve alone (rule 8 of §0.2). It supplies content; it does not relax the teaching rhythm.

### 0.2 Stitching / no-overlap rules
1. **The main course owns order.** This part's modules bind to main-course modules in §2 and are taught in those sessions. The language core (GO-01…GO-14) is the Go block of A3; everything later binds where its first real use is.
2. **One concept, one teaching.** Concepts owned elsewhere are recalled in one line, never re-taught: data-structure theory (A4), HTTP (A5), design patterns (the Design Patterns companion), the SQL itself (the SQL companion), attacks and cryptography (the Cloud Cybersecurity companion). This part owns only the Go rendering of each: the syntax, the semantics, the runtime behaviour and the idiom.
3. **Syntax unlock.** A Go construct is used in an explanation, lab or check only when the module that unlocks it is at least `taught` (rule 0.4.9; §0.4 lists what each module unlocks). The first use of each construct carries its **unlock block** (§0.3). Before its module, a construct is named only as "we'll cover this in GO-nn".
4. **Every module carries a contrast.** Each module's **Contrast** line names what Python, Java, C and JavaScript do instead, and the exact bug the other habit produces in Go. §9 collects them into one atlas for revision; the atlas never replaces the teaching.
5. **Mechanism before idiom.** An idiom ("accept interfaces, return structs", "don't communicate by sharing memory") is taught only after the mechanism that justifies it, and always with the case where it is wrong.
6. **Version honesty.** The baseline is Go 1.27, the version the learner's own module declares. A construct newer than Go 1.21 names the release that introduced it, because a `go` line older than that release in `go.mod` turns the construct off (the compiler says so). `(checked on 1.27.1)` marks a behaviour run on Go 1.27.1 (linux/amd64) on 2026-09-24 while this part was written; `(verify)` marks a claim that was not run and must be checked against the installed release before it is taught as fact.
7. **Tracking is inline**, same as the sibling parts: tick `- [ ]` or say "done" in chat.
8. **One involved problem per module.** Every module ends with an **involved problem** (`GO-Pnn`, the card's last line): one program the learner designs and writes alone, bigger than the build lab and aimed at the module's hardest idea. It is the module's top-rung challenge (rule 0.4.3), so a GO module is `mastered` only when its problem passes its rubric (§10.2) or its skip-test passes (rule 0.4.9). It is a project, not a check: it runs across several turns, Claude gives hints only when asked, one at a time, and never writes the solution, and the rubric is shown only after the learner submits. It uses only constructs already unlocked (rule 3). Before GO-20 is taught, its checks are a self-checking `main` that prints one PASS or FAIL line per case; from GO-20 on they are `go test` tests. When a problem needs a download (a module, a container image), it names it first, as every lab does. Two problems wait for a later module: GO-01's, GO-02's and GO-03's are set at the close of A3.G1 (they need GO-04's loops), and GO-15's after GO-16 (a leak needs a channel).

### 0.3 How one stitched session runs
1. **Anchor** — name the GO module(s) and the main-course module they ride with.
2. **Unlock** — for each new construct, the unlock block, in this order:
   - **Signature** — the grammar or the function signature, exactly.
   - **Semantics** — what it does, including the zero value, what is copied and what is shared.
   - **Runtime and memory** — where the value lives (stack, heap, inside a header), what can block, what can panic, what it costs.
   - **Contrast** — one precise difference from Python, Java, C or JavaScript and the bug that habit causes here.
3. **Predict → run** — a four-to-ten-line program whose output the learner predicts before running it (rule 0.4.4). Most of this part's surprises are cheap to show this way.
4. **Idiom** — how Go code in the standard library actually uses it.
5. **Check** — the module's check question, woven in.
6. **Involved problem** — set the module's `GO-Pnn` (rule 8 of §0.2); the learner works on it between sessions, and it is reviewed against its rubric (§10.2) when submitted.
7. **Close** — tick the box; record any carried-over habit in the misconception register (rule 0.4.5).

When other parts bind to the same session, the Suite Session Protocol (rule 0.4.2 in §0.6) governs; the Go layer runs after the patterns layer and before the attacker/crypto layer.

````

**J1132** · R7-2 · anchor-rewrite

````text
### 0.4 Notation and the unlock list
````

**J1133** · R7-2 · copied preferences, contract and Lab Safety moved out

````text
### 0.5 Learner teaching preferences (binding)

- **Check questions must be woven into the concept explanation itself**, not asked as separate "what do you already know" diagnostics — the learner explicitly opted out of background-probing questions and asked for calibration to happen through how they handle the material.
- **"Maintain curriculum depth and academic rigour"** has been repeated multiple times as an explicit standing instruction — do not compress, simplify, or skip the "why," even under time pressure or a fast pace of correct answers.
- When companion-file content (system-design-primer, SQL, design-patterns) overlaps a main-course module, **teach it once, stitched into the same session** — never as a separate pass, per each companion's own §0.2 stitching rules.
- If a companion file references module IDs that don't exist in the main course (as the SQL companion's did before its IDs were rebound), **say so plainly rather than forcing a silent, possibly-wrong mapping** — this was well received when done for the SQL companion.

### 0.6 Suite Teaching Contract and Lab Safety (same text in every part)

The main course's §0.4 and §0.5, copied whole so that this companion can be taught on its own terms. The rule numbers stay the main course's (0.4.1…0.4.10, and the five Lab Safety rules), so "main course §0.4.3" and rule 0.4.3 here are the same rule. The **progress ledger** named below is the tutor's running record beside the inline boxes (main course §0.1): each ID's mastery state, the misconception register, the errata list, the recorded overrides and wrong predictions, and the exact resume point. The inline `- [ ]` boxes stay authoritative.

**Suite Teaching Contract (main course §0.4).**

One contract for every part; each companion carries the same contract in its own §0 and adds its session detail. When two rules conflict, the higher one wins: (1) the learner's explicit instruction in the current chat · (2) the learner teaching preferences (§0.5 here) · (3) the main course on order, cert timing and Lab Reality · (4) the owning part on its content (main course §0.3) · (5) the companions' defaults.

**0.4.1 Rhythm.**

- One concept per turn, at full depth. New material is taught by direct explanation; procedures by worked, parallel examples.
- Every turn carries exactly one focused question, embedded in the teaching. Diagnosis happens through those checks; there is no separate probing (the learner preferences in §0.5 rule out separate calibrating questions). A turn may be as long as one concept needs.
- Correction style: confirm the correct part explicitly, then sharpen the imprecise part by naming the exact mechanism. No false praise. Hold the line under "just tell me"; give a foothold when the learner is genuinely stuck.
- Overrides: the learner may skip (after passing the skip-test), jump, or go hands-on. Every override is recorded in the ledger so the prerequisite check can flag what was skipped.

**0.4.2 Suite Session Protocol.** When several files bind to one module, the session runs:

1. **Anchor** — list the bound IDs from *all* files (each companion's §2).
2. **Concept** — taught once, by the owner in main course §0.3.
3. **Layers**, in fixed order: system design (primer) → SQL/engine → patterns → Go implementation (Go companion) → attacker/crypto (cyber).
4. **GCP lens.**
5. **One Numbers step** for the whole session.
6. **One application item**: a primer micro-problem *or* a companion exercise card, never both for the same concept.
7. **Checks**, woven in per §0.5.
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

**J1134** · R7-3 · overlap-register slice moved to rule 0.3

````text
### 2.1 Overlap register — what is intentionally *not* re-taught here
> **Note:** the suite-wide register is the main course §0.3; this table is the Go slice of it, and on a conflict the main course's register wins.

| Concept | Already owned by | What this part adds instead |
|---|---|---|
| Variables, control flow, functions, OOP basics | A3 (Python) | Go's versions and every difference from Python |
| Data-structure theory and costs | A4 | GO-27: the Go implementations |
| HTTP semantics, TLS handshake | A5 | GO-21: `net/http`, `crypto/tls` |
| Design patterns | the Design Patterns companion | the Go rendering (§2, A7 row) |
| SQL, parameterisation | the SQL companion (SL-13) | GO-22: placeholders and pools in `database/sql` |
| Rate-limit algorithms | the Cloud Cybersecurity companion (AB-01) | GO-19: `golang.org/x/time/rate` |
| Slow-client attacks and the timeout values | the Cloud Cybersecurity companion (DOS-05) | GO-21: which `http.Server` field does what |
| Password KDFs | the Cloud Cybersecurity companion (CR-13) | CR-13's build lab written in Go (after GO-07 and GO-21): `golang.org/x/crypto/argon2` in a Go service; GO-28 wraps it in a versioned record with rehash-on-login |
| Authentication attacks: sessions, CSRF, JWT, OAuth, MFA, credential stuffing | the Cloud Cybersecurity companion (AU-01…AU-10) | GO-28: each defence built in Go, with a test that replays the attack |
| Hashes, MACs, randomness, constant-time comparison | the Cloud Cybersecurity companion (CR-05, CR-06, CR-07, CR-16) | GO-28: `crypto/sha256`, `crypto/hmac`, `crypto/rand` and `hmac.Equal` in use |
| Money storage, the order state machine, ledger rules | the SQL companion (DD-03) | GO-29: the Go types, the transition table and the transactional writes |
| Card data, tokenization, PCI DSS scope | the Cloud Cybersecurity companion (PV-03) | GO-29: the service never sees a card number; it stores the provider's tokens and IDs |
| Checkout abuse | the Cloud Cybersecurity companion (AB-06, AB-07) | GO-29: per-account caps and idempotency in the handler |
| Queues, back-pressure, asynchronous work | the System Design Primer (SD-28) | GO-29: acknowledge a webhook fast and apply its effect from a queue |
````

**J1152** · R7-4 · anchor-rewrite

````text
One rubric per module's involved problem (rule 8 of §0.2). Each says what a passing submission shows and names the trap the problem is built around. A submission that misses one point is returned with that point only, not with the fix.
````

**J1154** · R7-4 · anchor-rewrite

````text
Companion to the main course, "The Consolidated Cloud Mastery Curriculum". Sibling to the System Design Primer companion, the SQL & Databases companion, the Design Patterns companion and the Cloud Cybersecurity companion.
````
