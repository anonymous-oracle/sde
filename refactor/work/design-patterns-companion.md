# Design Patterns, SOLID & Clean Architecture — A Companion Curriculum
Companion to the main course, "The Consolidated Cloud Mastery Curriculum". Sibling to the System Design Primer companion and the SQL & Databases companion.
Built September 21, 2026. Sources: Gamma, Helm, Johnson, Vlissides — *Design Patterns: Elements of Reusable Object-Oriented Software* (1994, "GoF"); Robert C. Martin — *Clean Architecture* (2017) and *Agile Software Development, Principles, Patterns, and Practices* (2002, SOLID's origin); Martin Fowler — *Patterns of Enterprise Application Architecture* (2002); Craig Larman — *Applying UML and Patterns* (GRASP); Alistair Cockburn — Hexagonal Architecture; Jeffrey Palermo — Onion Architecture; Eric Evans — *Domain-Driven Design* (2003).

---

## 0. Read this first

### 0.1 Standing instruction (for Claude, every session)
This file is a complement to the Curriculum, not a second curriculum. It supplies one thing Curriculum module **A7 (Software Architecture & APIs)** names but doesn't detail: formal OOP design theory — SOLID, GRASP, the GoF catalog, Clean/Hexagonal/Onion architecture, DDD building blocks, and the enterprise/microservice patterns layered on top. Teach this file's modules when A7 is reached, in the same session shape already used for the other two companions: one concept at a time, checked before moving on. This file supplies content; it does not relax the core teaching rhythm.

### 0.2 Stitching / no-overlap rules
1. **A3 already taught operational OOP** (class, object, `self`, constructor, inheritance mechanics via the `Dog` example) — this file never re-derives that; every module below assumes it and *recalls* it in one clause, never re-teaches it.
2. **One concept, one teaching**, same convention as the sibling companions. Where a pattern's core idea overlaps a system-design-primer concept (Observer ↔ Pub/Sub's fan-out, Strategy ↔ SD-10's load-balancer algorithms), teach the OOP-level mechanism here and cross-reference the SD companion's system-level version — don't re-teach either.
3. **Order is enforced.** Foundations (§3) → SOLID (§4) → GRASP (§5) → GoF catalog (§6) → Architecture (§7) → Anti-patterns (§8). A pattern is never taught before the principle it embodies — e.g., Strategy is not taught before Open/Closed, because Strategy *is* Open/Closed made concrete.
4. **Every pattern gets three things, always:** the problem it solves (pain before solution, never the reverse), the formal structure using canonical GoF participant names, and at least one real industry example — a cloud SDK, a popular library, or a framework this Curriculum touches elsewhere. Academic rigor and industry grounding are both mandatory, every time, not alternatives.
5. **Distinguish pattern from principle from architecture, explicitly, whenever one could be mistaken for another.** A *principle* (SOLID, GRASP) is a rule for arranging responsibility. A *pattern* (GoF) is a named, reusable solution shape to a recurring problem, usually at class/object level. An *architecture* (Clean, Hexagonal, microservice patterns) is a system-level arrangement, often built from several patterns and principles at once. Conflating these three is the most common shallow-learning failure in this material — call it out on sight.
6. **Tracking is inline**, same as the sibling files: tick `- [ ]` or say "done" in chat.
7. **Honesty flags.** `(debated)` marks where the industry itself disagrees (e.g., whether Singleton is a pattern or an anti-pattern in modern practice); `(GoF)` marks a definition quoted/adapted directly from the 1994 book, since its precise wording is often what's actually tested.

### 0.3 How one stitched session runs
1. **Anchor** — name the module(s) from §1's ledger being taught this session.
2. **Motivate** — state the problem *before* the solution; a pattern introduced without its pain is cargo-cult programming (AP-06) in the making.
3. **Structure** — the formal participants, using GoF's own names.
4. **Trade-offs** — every pattern costs something; name it, don't just sell the benefit.
5. **Real-world anchor** — one concrete industry example.
6. **Check** — the module's check question; the learner answers before being told the answer.
7. **Close** — tick the box; note anything shaky for a later recall.

When other companions bind to the same session, the Suite Session Protocol (rule 0.4.2 in §0.6) governs.

### 0.4 Notation
`F-nn` OOP foundations · `PR-nn` SOLID/GRASP principles · `DP-nn` GoF design patterns · `ARCH-nn` architectural styles/DDD/enterprise patterns · `AP-nn` anti-patterns. `[Cr]` = Creational, `[St]` = Structural, `[Bh]` = Behavioral (GoF's own three categories).

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

---

## 1. Coverage ledger

| Area | Modules | Count |
|---|---|---|
| OOP foundations, formalized | F-01…F-04 | 4 |
| SOLID | PR-01…PR-05 | 5 |
| GRASP | PR-06…PR-14 | 9 |
| GoF Creational patterns | DP-01…DP-05 | 5 |
| GoF Structural patterns | DP-06…DP-12 | 7 |
| GoF Behavioral patterns | DP-13…DP-23 | 11 |
| Architecture & DDD | ARCH-01…ARCH-12 | 12 |
| Anti-patterns | AP-01…AP-10 | 10 |
| **Total** | | **63** |

---

## 2. Stitch table — where this binds into the Curriculum

| Curriculum module | Companion modules taught alongside | Notes |
|---|---|---|
| A3 (recall only, not retaught) | — | classes/objects/`self`/inheritance mechanics already covered there |
| **A7 — Software Architecture & APIs** | **Everything in this file**, in order: F-01…04, then PR-01…14, then DP-01…23, then ARCH-01…08, then AP-01…10. ARCH-09…12 are taught in the A9 session (next row). A7 splits this into teaching blocks A7.3–A7.7 | Primary landing module — flagged as a curriculum gap during the A5 networking session, filled here |
| A9 Distributed Systems Theory | ARCH-09 (CQRS), ARCH-10 (Event Sourcing), ARCH-11 (Saga), ARCH-12 (Circuit Breaker/Strangler/Bulkhead) — gated behind A9 being complete | These are distributed-systems theory wearing OOP-pattern clothing; A9 owns the consistency/failure theory, this file owns the shape |
| B3 Architecture Patterns & Well-Architected | ARCH-01…04 recalled when discussing HA/DR patterns, one line only | Different axis: B3 is *deployment* resilience, this file is *code* structure — do not conflate (rule 5) |
| C2 Kubernetes | DP-14 Observer (recall) for controller watch-loops; DP-18 Chain of Responsibility (recall) for admission webhooks | The K8s "Operator pattern" itself is taught in C2 natively; cross-reference only |
| C4 CI/CD | ARCH-12's Strangler Fig, recalled as the pattern behind incremental legacy migration via pipelines | — |
| System-design-primer companion | DP-14 Observer ↔ SD-28 Pub/Sub; PR-01 (SRP) ↔ SD-12 microservices; DP-09 Facade ↔ SD-11 reverse proxy | Cross-reference only, not a re-teach |
| Go Language Companion | GO-11 renders the patterns in Go: PR-05 and PR-04 as small consumer-owned interfaces, F-03 as embedding (which delegates and never dispatches back), DP-04 as functional options, DP-12 and DP-18 as `http.Handler` middleware, DP-01 as `sync.Once`, DP-13 as a function type, DP-14 as channels, DP-20 as `iter.Seq` | This file owns the patterns; the Go companion owns only their Go shape. DP-15 Template Method cannot be built by overriding in Go |

### 2.1 Overlap register — what is intentionally *not* re-taught here
> **Note:** the suite-wide register is the main course §0.3; this table is the patterns slice of it, and on a conflict the main course's register wins.

| Concept | Already owned by | What this file adds instead |
|---|---|---|
| Classes, objects, `self`, constructors | A3 | Formal theory built on top (F-01…04) |
| Inheritance mechanics | A3 (the `Dog` example) | The formal is-a contract and its limits (F-03, PR-03) |
| Microservices, service discovery | A7 base content, SD-12 | The class-level patterns (Strategy, Observer) that compose into them |
| Pub/Sub, message queues | A7, SD-28 | Observer (DP-14) as its in-process ancestor |
| HA/DR patterns (active-active, warm standby) | B3 | Explicitly distinguished as infrastructure, not code architecture |

---

## 3. Foundations — the four pillars of OOP, formally (F-01…F-04)

A3 taught *how* to write a class. These four are the *why*, at the rigor a formal CS curriculum demands — "encapsulation means hiding stuff" fails a rigorous interview and doesn't actually guide a design decision.

#### F-01 · Encapsulation
- [ ] F-01
**Formal statement:** bundling data and the operations on that data into a single unit, restricting direct access to that data from outside the unit.
**Why it's not just "private variables":** encapsulation protects an **invariant** — a fact that must always be true about an object's state. A `BankAccount` with a public `balance` field lets any code set `balance = -1000000`, violating "balance is never negative." Routing every state change through a method (`withdraw()`) lets that method *enforce* the invariant.
**Check:** what invariant does hiding `balance` behind `withdraw(amount)` protect, that a public field cannot?

#### F-02 · Abstraction
- [ ] F-02
**Formal statement:** exposing only the essential features of an object relevant to the current context, hiding implementation complexity. Where encapsulation hides *data*, abstraction hides *complexity of behavior*.
**The distinction that trips people up:** encapsulation is a *mechanism* (access control); abstraction is a *design concept* (what to expose at all). A class can be encapsulated (private fields) but a poor abstraction (40 pointless getters/setters that still force callers to think about internals) — conflating the two is a common interview trap.
**Check:** describe a class that is encapsulated but is *not* a good abstraction.

#### F-03 · Inheritance
- [ ] F-03
**Recall from A3**, formalized: inheritance models an **"is-a"** relationship. It serves two distinct purposes often conflated: (1) code reuse and (2) polymorphic substitutability (F-04). Reason (1) alone is a trap — "reuse via inheritance" without an honest is-a relationship is exactly how a hierarchy ends up violating the Liskov Substitution Principle (PR-03).
**The load-bearing rule:** prefer **composition** ("has-a") over **inheritance** ("is-a") whenever the relationship isn't a true taxonomic one. A `Car` *has an* `Engine`; it is not a kind of `Engine`. This single rule is arguably the most consequential piece of OOP wisdom in this file — DP-08 (Decorator) and DP-13 (Strategy) exist specifically as composition-based alternatives to problems people instinctively solve with inheritance.
**Check:** a `Square` inherits from `Rectangle`, overriding `setWidth`/`setHeight` to keep both sides equal. Why does this break substitutability even though "a square is-a rectangle" is mathematically true?

#### F-04 · Polymorphism
- [ ] F-04
**Formal statement:** different objects respond to the same method call in ways appropriate to their own type. Two kinds worth distinguishing: **subtype polymorphism** (a `Dog` and `Cat`, both `Animal`s, implement `makeSound()` differently — what A3 covered) and **parametric polymorphism** (a generic `List<T>` works identically regardless of `T` — the *same* code, not different implementations). GoF-pattern polymorphism is almost always the subtype kind.
**Why it matters for everything after this:** nearly every GoF Behavioral pattern is, mechanically, "define an interface, write several implementations, let the caller hold a reference to the interface and never know which implementation is running." That sentence *is* subtype polymorphism, used as a design tool.
**Check:** in one sentence, why does polymorphism let you add a new `Animal` subclass without modifying code that already calls `makeSound()`? (This is Open/Closed, PR-02, arriving early.)

---

## 4. SOLID (PR-01…PR-05)

Five principles from Robert C. Martin, each naming a specific way a class design rots, and the rule that prevents it.

#### PR-01 · Single Responsibility Principle (SRP)
- [ ] PR-01
**Formal statement (Martin's sharper, later version):** a class should have only one reason to change — one *actor* (stakeholder) it answers to.
**Why "does one thing" misleads:** the precise test is **actors**. If an `Employee` class's `calculatePay()` changes when Finance's rules change, and its `save()` changes when the DBA's schema changes, those are two different reasons to change, driven by two different stakeholders — split them, even though both feel "about an employee."
**Cloud-relevant example:** a Cloud Function that validates input, calls a payment API, *and* writes an audit log serves three actors in one function — an audit-format change now risks silently breaking payment logic.
**Check:** a `ReportGenerator` both formats a report as HTML and saves it to Cloud Storage. Name the two actors, and what happens to each responsibility once split.

#### PR-02 · Open/Closed Principle (OCP)
- [ ] PR-02
**Formal statement (Bertrand Meyer, 1988):** software entities should be **open for extension, closed for modification** — add new behavior without editing existing, already-tested code.
**The mechanism:** polymorphism (F-04). Instead of `calculateArea(shape)` with an `if/elif` chain on `shape.type`, give every shape an `area()` method behind a common interface — a new shape means a new class, not an edited function.
**Direct link forward:** the formal justification for **DP-13 Strategy** and **DP-15 Template Method**.
**Check:** rewrite this in words as OCP-compliant: `if (shape.type == "circle") {...} else if (shape.type == "square") {...}`. What do you add for a triangle, and what do you never touch?

#### PR-03 · Liskov Substitution Principle (LSP)
- [ ] PR-03
**Formal statement (Barbara Liskov, 1987):** if `S` is a subtype of `T`, objects of `T` may be replaced with objects of `S` **without altering program correctness**.
**Precise technical conditions:** a valid override may only **weaken preconditions** and may only **strengthen postconditions**, while preserving the parent's invariants. `Square extends Rectangle` violates this: `setWidth()` on a `Square` has a *stronger, surprising* side effect (height changes too) that breaks the postcondition "only width changed" that callers rely on.
**Why it's the hardest SOLID letter in practice:** it's a *behavioral contract*, not something a compiler fully checks — violations surface only when a subclass is used polymorphically, exactly the situation OCP encourages.
**Check:** a `Bird` base class has `fly()`; `Penguin` overrides it to throw. Which LSP condition is violated, and what's the actual fix (is "is-a" even the right relationship)?

#### PR-04 · Interface Segregation Principle (ISP)
- [ ] PR-04
**Formal statement:** no client should be forced to depend on methods it does not use — many small, specific interfaces beat one large, general one.
**Concrete failure:** a `Worker` interface with `work()` and `eat()` forces `RobotWorker` to implement a nonsensical `eat()`. Split into `Workable` and `Eatable`.
**Relation to SRP:** ISP is SRP applied to interfaces — a "fat interface" is an SRP violation one level up.
**Check:** a `Printer` interface has `print()`, `scan()`, `fax()`. A print-only inkjet is forced to implement all three. Redesign it.

#### PR-05 · Dependency Inversion Principle (DIP)
- [ ] PR-05
**Formal statement:** high-level modules should not depend on low-level modules — both should depend on **abstractions**; abstractions should not depend on details, details should depend on abstractions.
**What "inversion" means:** traditionally `PaymentService` (high-level) directly instantiates `StripeAPI` (low-level detail) — a downward dependency. DIP inverts this: `PaymentService` depends on a `PaymentGateway` **interface**; `StripeAPI` implements it. The *detail* now depends on the abstraction the high-level module defined.
**Distinguish from Dependency Injection:** DIP is the *principle* ("depend on abstractions"); Dependency Injection is the *mechanism* handing the concrete implementation to the high-level module instead of it constructing one itself. DIP is the why, DI is the how — conflating them is extremely common and worth actively correcting.
**Direct link forward:** the formal principle behind **ARCH-04 Clean Architecture**'s entire dependency rule.
**Check:** a `NotificationService` directly instantiates `new EmailSender()` in its constructor. Name the violation and the missing abstraction.

---

## 5. GRASP — General Responsibility Assignment Software Patterns (PR-06…PR-14)

Craig Larman's academically rigorous complement to SOLID: given a set of responsibilities, *which class should own which one?* Covered at working depth for completeness.

- **PR-06 Information Expert:** give a responsibility to the class holding the data needed to fulfill it.
  - **Check:** an `Order` holds its lines and each line's price. Which class should compute the order total under Information Expert, and why not an `OrderService`?
- **PR-07 Creator:** class `A` should create `B` if `A` aggregates, records, closely uses, or holds the data to initialize `B` — the formal justification for DP-01…05 (Creational patterns) existing at all.
  - **Check:** an `Order` aggregates `OrderLine`s. Which class should create an `OrderLine`, by Creator, and which of Creator's conditions applies?
- **PR-08 Controller:** route system events to a class representing the overall system or use case, not a UI/view class — the formal root of MVC's separation (ARCH-05).
  - **Check:** a web handler validates input, applies the discount rules and saves the order. What should the handler delegate, and to which Controller?
- **PR-09 Low Coupling:** minimize how many other classes a class depends on.
  - **Check:** class A imports seven other classes to do one job. Name one way to cut its coupling without moving its responsibility.
- **PR-10 High Cohesion:** keep a class's responsibilities strongly, purposefully related — SRP's older academic sibling, stated as a design-quality metric.
  - **Check:** a `Utils` class holds date parsing, e-mail sending and currency rounding. What does low cohesion cost you here, concretely?
- **PR-11 Polymorphism:** assign type-varying behavior via polymorphic operations, not type-check chains — the GRASP-level PR-02.
  - **Check:** a `switch` on `paymentType` appears in five places. What does Polymorphism replace it with, and what happens when a new payment type arrives?
- **PR-12 Pure Fabrication:** when no domain concept cleanly owns a responsibility, invent a class purely for design convenience — the formal justification for utility/service/repository classes.
  - **Check:** why is a `Repository` a pure fabrication, and what would be wrong with putting `save()` on the domain entity instead?
- **PR-13 Indirection:** assign responsibility to an intermediate object to avoid direct coupling — the formal root of DP-19 (Mediator) and DP-06 (Adapter).
  - **Check:** two services call each other's HTTP APIs directly. Which intermediate object would Indirection add, and what does it buy you?
- **PR-14 Protected Variations:** wrap a stable interface around points of predicted instability — nearly the motivation clause behind every GoF Structural pattern.
  - **Check:** a payment provider's API is predicted to change. Where do you put the stable interface, and which GoF pattern implements the protection?

- [ ] PR-06 · [ ] PR-07 · [ ] PR-08 · [ ] PR-09 · [ ] PR-10 · [ ] PR-11 · [ ] PR-12 · [ ] PR-13 · [ ] PR-14

**Integration check:** a `PaymentValidator` exists purely to check payment rules, representing no real-world "thing." Which GRASP principle justifies it, and which one answers "why isn't this just inside `Payment`?"

---

## 6. The GoF Catalog — 23 Design Patterns

Format per pattern: **Intent** (paraphrased from GoF) → **Problem** → **Structure** → **Trade-offs** → **Real-world example**.

### 6.1 Creational [Cr] — DP-01…05: how objects get created, so the system doesn't depend on the concrete classes it instantiates (PR-07 + PR-05 in action).

**DP-01 · Singleton [Cr]**
- [ ] DP-01
- **Intent:** ensure a class has only one instance, with a global access point.
- **Problem:** some resources (a single DB connection pool) genuinely must not be duplicated.
- **Structure:** private constructor; a static `getInstance()` returning the same instance every call.
- **Trade-offs `(debated)`:** the most cited pattern that's also an anti-pattern in disguise — it introduces global mutable state and a hidden dependency, bypassing DIP's "explicit dependencies via abstraction." Modern practice increasingly prefers a DI container managing a single instance's *lifetime* instead.
- **Real-world example:** most DI frameworks offer "singleton scope" as a lifetime option rather than a hand-rolled class — industry has largely migrated away from the textbook form.
- **Named real examples:** `sync.Once` and `sync.OnceValue` in Go's standard library (one lazy initialization, safe under concurrency); `http.DefaultClient` and `slog.Default()` as process-wide defaults, each replaceable, which is the honest modern form.
- **GCP lens:** Google Cloud client libraries recommend creating one client per process and reusing it (clients hold connection pools and credentials); inject that one client rather than hiding it in a global.
- **Check:** why does a hand-written Singleton make unit testing harder — what can't you do to it that you could do to an injected object?

**DP-02 · Factory Method [Cr]**
- [ ] DP-02
- **Intent:** define an interface for creating an object, letting subclasses decide which class to instantiate.
- **Problem:** a class can't anticipate which concrete class it needs — the decision belongs to a subclass.
- **Structure:** an abstract `Creator` with an abstract `factoryMethod()`; concrete `Creator` subclasses return different concrete `Product` types.
- **Trade-offs:** a class hierarchy purely for creation logic — worth it only when "which concrete class" genuinely varies by context.
- **Real-world example:** `DocumentCreator.createDocument()`; `PDFCreator`/`WordCreator` subclasses each return their own document type.
- **Named real examples:** Java's `Iterable.iterator()`, which GoF itself cites as a factory method (each collection returns its own iterator class); Go's `database/sql/driver.Driver.Open`, which each driver implements to return its own connection type.
- **GCP lens:** each Cloud Go client's `NewClient(ctx, opts...)` chooses the transport and the credentials at run time from Application Default Credentials, so the caller never names a concrete credential type.
- **Check:** how is Factory Method a direct application of PR-07 combined with PR-05?

**DP-03 · Abstract Factory [Cr]**
- [ ] DP-03
- **Intent:** provide an interface for creating **families** of related objects without specifying concrete classes.
- **Problem:** sometimes you need a whole matched set (a UI toolkit's `Button`+`Checkbox`+`Scrollbar` that must share one visual theme).
- **Structure:** an `AbstractFactory` interface with one creation method per product; concrete factories (`WindowsFactory`, `MacFactory`) each produce the whole matched family.
- **Trade-offs:** adding a new *product* to the family is painful (touches every concrete factory); adding a new *family* is easy.
- **Real-world example:** `PostgresFactory` producing `PostgresConnection`+`PostgresQueryBuilder` together, guaranteed never mixed with MySQL's equivalents.
- **Named real examples:** Java's `javax.xml.parsers.DocumentBuilderFactory` (the installed implementation supplies a matched parser family); Swing's pluggable look-and-feel, where one `LookAndFeel` supplies every widget's UI delegate.
- **GCP lens:** many generated Cloud Go clients offer a gRPC constructor and a REST constructor for the same API, each producing a matched set of call stubs `(verify)`.
- **Check:** what breaks specifically if you need to add a `Slider` to every existing theme family?

**DP-04 · Builder [Cr]**
- [ ] DP-04
- **Intent:** separate construction of a complex object from its representation, so the same process can build different representations.
- **Problem:** a constructor with 10 optional parameters is unreadable and error-prone (the "telescoping constructor" problem).
- **Structure:** a `Builder` with chained methods (each returning `this`), and a final `build()` assembling the result.
- **Trade-offs:** more code than a plain constructor for simple objects — earns its keep with many optional pieces or a required valid sequence.
- **Real-world example:** cloud SDK request-object construction (`RequestBuilder().setTimeout(30).setRetries(3).build()`).
- **Named real examples:** Java's `HttpRequest.newBuilder()…build()`; the Google Cloud Java client's `BlobInfo.newBuilder(bucket, name)…build()` `(verify)`; Go's `strings.Builder` (incremental construction; Go usually prefers functional options for configuration, as the Cloud Go clients' `option.With…` values show).
- **GCP lens:** Cloud client configuration in Go uses functional options (`option.WithCredentialsFile`, `option.WithEndpoint`), the Go-idiomatic cousin of Builder; Java clients use builders directly.
- **Check:** why is a fluent Builder a better fit than 10 constructor parameters specifically when several are *optional*?

**DP-05 · Prototype [Cr]**
- [ ] DP-05
- **Intent:** specify kinds of objects using a prototypical instance, creating new objects by **copying** it.
- **Problem:** building from scratch is expensive, or the exact concrete class isn't known until runtime, but a similar instance already exists.
- **Structure:** a `clone()` method; the caller copies a configured instance instead of re-running expensive setup.
- **Trade-offs:** requires careful **deep vs. shallow copy** handling — a shallow clone sharing a reference can leave two "independent" objects secretly sharing mutable state.
- **Real-world example:** cloning a configured game-character template to spawn instances without re-running expensive initialization.
- **Named real examples:** Go's `http.Request.Clone(ctx)`, documented as a deep copy, beside `slices.Clone` and `maps.Clone`, which are shallow; JavaScript's `Object.create(proto)`, where objects are built from a prototype object.
- **GCP lens:** Compute Engine instance templates and machine images: new VMs are copies of a configured prototype.
- **Check:** you clone an object holding a `List<String> tags`. If the clone is shallow, what breaks when the original's list is modified after cloning?

### 6.2 Structural [St] — DP-06…12: composing classes/objects into larger structures while staying flexible (F-03's "favor composition," and PR-14).

**DP-06 · Adapter [St]**
- [ ] DP-06
- **Intent:** convert one class's interface into another interface clients expect.
- **Problem:** an existing (often unmodifiable) class's interface doesn't match what your code expects.
- **Structure:** an `Adapter` implementing the target interface, internally delegating to the incompatible adaptee.
- **Trade-offs:** cheap indirection — usually clearly worth it since the alternative is editing code you don't own.
- **Real-world example:** wrapping a legacy XML payment API behind the JSON-based `PaymentGateway` interface your app expects.
- **Named real examples:** Go's `http.HandlerFunc`, whose documentation calls it an adapter (an ordinary function becomes an `http.Handler`); Java's `Arrays.asList` (an array seen as a `List`).
- **GCP lens:** Eventarc delivers events from many sources in the one CloudEvents format, an adapter from each source's native shape to one interface.
- **Check:** how does Adapter differ from Facade (DP-09) in *intent*, though both "wrap" something?

**DP-07 · Bridge [St]**
- [ ] DP-07
- **Intent:** decouple an abstraction from its implementation so both can vary independently.
- **Problem:** combining "N abstractions × M implementations" via inheritance alone produces a combinatorial subclass explosion.
- **Structure:** an `Abstraction` holds a reference to an `Implementor` interface (composition) — `Shape` holds a `DrawingAPI`; new shapes and new drawing APIs each grow independently.
- **Trade-offs:** upfront design complexity — worth it only when both axes are genuinely expected to grow independently.
- **Real-world example:** `Notification` (abstraction) bridged to `NotificationChannel` (Email/SMS/Push) — new notification types and channels don't multiply each other.
- **Named real examples:** Go's `database/sql` (the `DB` abstraction) and `database/sql/driver` (the implementation side), which vary independently; `log/slog`'s `Logger` in front of any `Handler`; JDBC in Java.
- **GCP lens:** OpenTelemetry's API is the abstraction, and exporters (Cloud Trace, Cloud Monitoring) are implementations that vary independently of it.
- **Check:** without Bridge, how many subclasses for 3 shapes × 4 rendering engines? With Bridge?

**DP-08 · Composite [St]**
- [ ] DP-08
- **Intent:** compose objects into tree structures for part-whole hierarchies; treat individual objects and compositions uniformly.
- **Problem:** code handling both a single item and a group of items ends up full of `if (isGroup)` checks.
- **Structure:** a common `Component` interface implemented by both `Leaf` and `Composite` (which holds other `Component`s) — calling a method on a folder recursively applies it to everything inside.
- **Trade-offs:** can become overly general — hard to restrict what children a composite may legally contain.
- **Real-world example:** a filesystem, or a UI widget tree.
- **Named real examples:** the DOM, where an element and a text node are both `Node`s; Java AWT's `Container`, which is itself a `Component`; Go's `io.MultiReader` and `io.MultiWriter` (many readers or writers seen as one).
- **GCP lens:** the resource hierarchy (organization, folders, projects) is a composite: a folder answers "what is the effective IAM policy" the same way a project does.
- **Check:** why does `totalSize()` on a top-level folder work correctly without the caller checking "file or folder" itself?

**DP-09 · Facade [St]**
- [ ] DP-09
- **Intent:** provide a unified, higher-level interface to a subsystem, making it easier to use.
- **Problem:** a client using a complex subsystem (compiling: lexer→parser→optimizer→codegen) shouldn't need to orchestrate all four steps.
- **Structure:** one `Facade` exposing a simple method that internally coordinates the subsystem; subsystem classes remain accessible for those needing finer control.
- **Trade-offs:** can become a God Object (AP-01) if it accumulates orchestration logic instead of delegating.
- **Real-world example:** a cloud SDK's high-level client (`.upload(file)`) hiding auth, retries, chunking, and raw HTTP.
- **Named real examples:** Go's `http.Get`, one call over `Client`, `Transport` and `Request`; the `gcloud` command line over the Google Cloud APIs.
- **GCP lens:** the Cloud client libraries are a facade over each API's REST and gRPC surfaces; `gcloud` is a facade over many APIs.
- **Check:** does a Facade remove the subsystem's original interfaces, or only add a simpler option alongside them — and why does that matter?

**DP-10 · Flyweight [St]**
- [ ] DP-10
- **Intent:** use sharing to support large numbers of fine-grained objects efficiently, separating **intrinsic** (shared) from **extrinsic** (context-specific) state.
- **Problem:** instantiating millions of similar objects wastes memory if each duplicates identical data.
- **Structure:** a `Flyweight` holds only intrinsic state and is shared; extrinsic state is passed in by the client at use-time, never stored in the flyweight.
- **Trade-offs:** passing extrinsic state correctly is easy to get wrong; only worth it at genuinely large object counts.
- **Real-world example:** a text editor sharing one glyph object per unique character+font, tracking position separately per occurrence.
- **Named real examples:** Java's `Integer.valueOf`, which returns cached instances for small values, and `String.intern`; Go's `unique.Make` (Go 1.23 and later), which interns comparable values into shared handles.
- **GCP lens:** container image layers in Artifact Registry are content-addressed and stored once, however many images share them (the shared layer is the intrinsic state).
- **Check:** name one intrinsic and one extrinsic piece of state in the text-editor example.

**DP-11 · Proxy [St]**
- [ ] DP-11
- **Intent:** provide a surrogate for another object to control access to it.
- **Problem:** you need access control, lazy loading, caching, or logging around an object without changing it or its callers.
- **Structure:** a `Proxy` implementing the same interface as the `RealSubject`, adding logic before/after delegating.
- **Trade-offs:** near-identical structure to Adapter and Decorator — the difference is *intent*: Proxy controls access, Adapter changes an interface, Decorator adds behavior. A genuinely common confusion, worth drilling.
- **Real-world example:** an ORM's lazy-loaded related object hits the database only when a real field is actually accessed.
- **Named real examples:** Go's `httputil.ReverseProxy`; generated gRPC client stubs (a remote proxy: the call looks local, the work is remote); Java's `java.lang.reflect.Proxy`.
- **GCP lens:** the Cloud SQL Auth Proxy (a protection and connection proxy) and Identity-Aware Proxy (an access-control proxy in front of an application).
- **Check:** state the one-word difference in *purpose* for Proxy vs. Adapter vs. Decorator, given near-identical shapes.

**DP-12 · Decorator [St]**
- [ ] DP-12
- **Intent:** attach additional responsibilities to an object dynamically — a flexible alternative to subclassing.
- **Problem:** subclassing every combination of optional feature (`CoffeeWithMilkAndSugar…`) produces the same explosion Bridge solves on a different axis.
- **Structure:** `Decorator` implements the same interface as the wrapped `Component`, adding behavior before/after delegating — decorators stack, each adding one responsibility.
- **Trade-offs:** many stacked decorators can be hard to debug; stacking order can silently change behavior.
- **Real-world example:** Java's `BufferedReader(new FileReader(...))` I/O streams.
- **Named real examples:** Go's `bufio.NewReader(r)`, `gzip.NewReader(r)` and `io.LimitReader(r, n)`, each an `io.Reader` wrapping an `io.Reader`; Java's `BufferedInputStream` around any `InputStream`.
- **GCP lens:** in Go, an `http.RoundTripper` is decorated by OAuth2 token injection and by OpenTelemetry's `otelhttp` transport, each wrapping the next.
- **Check:** in one sentence, why does stacking three Decorators avoid the subclass explosion three optional features via inheritance would cause?

### 6.3 Behavioral [Bh] — DP-13…23: algorithms and responsibility/communication between objects.

**DP-13 · Strategy [Bh]**
- [ ] DP-13
- **Intent:** define a family of algorithms, encapsulate each, make them interchangeable.
- **Problem:** the direct application of PR-02: an `if/elif` chain picking behavior must be edited for every new behavior.
- **Structure:** a `Strategy` interface; concrete strategies; a `Context` holds a `Strategy` reference, swappable at runtime.
- **Trade-offs:** clients must be aware different strategies exist to choose between them.
- **Real-world example:** a payment processor holding a `PaymentStrategy` chosen at checkout.
- **Named real examples:** Go's `slices.SortFunc(s, cmp)` with the comparison passed in; Java's `Comparator`; retry and backoff policies passed to a client.
- **GCP lens:** retry behaviour in the Cloud Go clients is a pluggable policy (for example, the Cloud Storage client's retry options) `(verify)`.
- **Check:** what new class do you write to add a payment method, and what existing code stays untouched?

**DP-14 · Observer [Bh]**
- [ ] DP-14
- **Intent:** define a one-to-many dependency so when one object (`Subject`) changes, all dependents (`Observer`s) are notified automatically.
- **Problem:** many objects need to react to a state change without the `Subject` being tightly coupled to all of them.
- **Structure:** `Subject` maintains `Observer`s via `attach()`/`detach()`/`notify()`; each `Observer` implements `update()`.
- **Trade-offs:** notification order isn't guaranteed; update cascades are a real bug risk; memory leaks if observers aren't detached.
- **Real-world example:** the OOP-level version of SD-28 (Pub/Sub) — same decoupled fan-out shape, in-process instead of over a network.
- **Named real examples:** Go's `signal.Notify` (the runtime notifies registered channels); the DOM's `addEventListener`; Kubernetes informers, which call registered event handlers on add, update and delete.
- **GCP lens:** Pub/Sub topics and subscriptions, Eventarc triggers and Cloud Storage notifications are Observer at system scale.
- **Check:** what does a `Subject`/`Observer` pair share structurally with a Pub/Sub topic, and what differs about the failure modes?

**DP-15 · Template Method [Bh]**
- [ ] DP-15
- **Intent:** define an algorithm's skeleton in a method, deferring some steps to subclasses.
- **Problem:** several classes share an algorithm's shape but need different behavior for one or two steps.
- **Structure:** a base class's `final templateMethod()` calls several steps in fixed order; some are abstract "hooks" subclasses must implement.
- **Trade-offs:** relies on inheritance (heavier coupling than Strategy's composition) — right when the overall structure must stay fixed and only specific steps vary.
- **Real-world example:** a test framework's `setUp()`→`runTest()`→`tearDown()` skeleton.
- **Named real examples:** Go's `sort.Sort`, a fixed algorithm whose steps (`Len`, `Less`, `Swap`) the caller supplies; Java's `InputStream.read(byte[])` built on the abstract single-byte `read()`, and `AbstractList`.
- **GCP lens:** Apache Beam on Dataflow: the runner owns the skeleton, and a `DoFn` fills in the steps (setup, process each element, finish a bundle, teardown).
- **Check:** what varies via composition in Strategy, and what varies via inheritance in Template Method — when would you deliberately pick the latter?

**DP-16 · State [Bh]**
- [ ] DP-16
- **Intent:** let an object alter its behavior when its internal state changes — it appears to change class.
- **Problem:** behavior driven by a `status` field scatters `if (status == ...)` across every method.
- **Structure:** a `State` interface; concrete states each implement behavior appropriately, including transitioning the context to the next state.
- **Trade-offs:** near-identical structure to Strategy — the difference is intent: State's implementations actively transition between one another, modeling a state machine.
- **Real-world example:** an `Order` whose `ship()`/`cancel()` behavior legitimately differs by status, illegal transitions simply not offered.
- **Named real examples:** the lexer of Go's `text/template/parse`, where each state is a function that returns the next state (`stateFn`); GoF's own `TCPConnection` example.
- **GCP lens:** a Compute Engine VM's lifecycle (provisioning, staging, running, stopping, terminated) is a state machine with legal transitions.
- **Check:** what does a Strategy object *not* do that a State object does?

**DP-17 · Command [Bh]**
- [ ] DP-17
- **Intent:** encapsulate a request as an object, enabling queuing, logging, and undo.
- **Problem:** decouple "what triggers an action" from "what performs it," often needing to queue/log/undo.
- **Structure:** a `Command` interface with `execute()` (often `undo()`); an `Invoker` triggers commands without knowing what they do.
- **Trade-offs:** a class per action — worth it specifically for queuing, logging, undo, or invoker/receiver decoupling.
- **Real-world example:** a job queue (Cloud Tasks) is Command at the infrastructure level — a serialized "do this later" object.
- **Named real examples:** Go's `exec.Cmd` (a command built, stored and run later); Java's `Runnable`; database migration tools whose steps each carry an up and a down.
- **GCP lens:** Cloud Tasks stores an HTTP request as a task object and runs it later, with retries: a Command queue as a service.
- **Check:** why does representing an action as an object make "undo" possible in a way a direct method call cannot?

**DP-18 · Chain of Responsibility [Bh]**
- [ ] DP-18
- **Intent:** give more than one object a chance to handle a request; chain receivers and pass the request along until handled.
- **Problem:** a request might need one of several handlers, but the sender shouldn't know which or in what order.
- **Structure:** each `Handler` holds a reference to the next; `handle()` either processes or passes it along.
- **Trade-offs:** no guarantee a request is handled at all — requires an explicit fallback.
- **Real-world example:** HTTP middleware — auth, then logging, then rate limiting, each short-circuiting or forwarding.
- **Named real examples:** the Java Servlet `FilterChain`; Go HTTP middleware stacks, where each handler may answer or call the next.
- **GCP lens:** a request to an external Application Load Balancer can pass Cloud Armor, then Identity-Aware Proxy, then the backend; any link can reject it.
- **Check:** what plays "the request" and what plays "each handler" in an HTTP middleware chain?

**DP-19 · Mediator [Bh]**
- [ ] DP-19
- **Intent:** encapsulate how a set of objects interact, promoting loose coupling.
- **Problem:** many objects communicating directly with each other produce a tangled many-to-many web.
- **Structure:** a `Mediator` all colleagues talk *to* instead of each other directly.
- **Trade-offs:** the mediator can itself become a God Object — complexity concentrates rather than disappears.
- **Real-world example:** an air traffic control tower (GoF's own example); a chat server mediating clients.
- **Named real examples:** the Kubernetes API server, through which controllers coordinate instead of calling each other `(debated)`; an air-traffic control tower, GoF's classic analogy.
- **GCP lens:** Pub/Sub between services and Workflows as an orchestrator both take on the Mediator role: services talk to them, not to each other.
- **Check:** with 6 UI components all reacting to each other, how many direct reference pairs exist without a Mediator, versus with one?

**DP-20 · Iterator [Bh]**
- [ ] DP-20
- **Intent:** access elements of an aggregate sequentially without exposing its underlying representation.
- **Problem:** code walking a collection shouldn't need to know if it's an array, list, or tree.
- **Structure:** an `Iterator` interface (`hasNext()`, `next()`); the aggregate returns one via `createIterator()`.
- **Trade-offs:** minimal — this pattern is built directly into most modern languages' syntax now.
- **Real-world example:** every `for...of` construct in a modern language *is* this pattern, already implemented.
- **Named real examples:** Go's `iter.Seq` (Go 1.23 and later), `bufio.Scanner` and `sql.Rows`; the Google Cloud Go clients' iterators, which return `iterator.Done` at the end.
- **GCP lens:** list APIs return pages with a page token, and the Go clients wrap that in an iterator that ends with `iterator.Done`.
- **Check:** why does hiding array-vs-linked-list behind a common iterator let you swap the implementation later without breaking loops over it?

**DP-21 · Memento [Bh]**
- [ ] DP-21
- **Intent:** capture and externalize an object's internal state, without violating encapsulation, so it can be restored later.
- **Problem:** implementing undo requires saving past state, but that state is (correctly) private.
- **Structure:** the `Originator` creates a `Memento`; a `Caretaker` stores mementos but never looks inside them.
- **Trade-offs:** storing many full snapshots can be memory-expensive.
- **Real-world example:** a text editor's undo history.
- **Named real examples:** Go's hash states, which implement `encoding.BinaryMarshaler` (`crypto/sha256`'s digest can be saved and restored mid-stream); the generators of `math/rand/v2`, such as ChaCha8, whose state marshals the same way.
- **GCP lens:** persistent-disk snapshots and Cloud Storage object versioning keep a restorable state without exposing the internals.
- **Check:** why does a `Caretaker` that "can't look inside" a memento preserve encapsulation in a way `getInternalState()` would not?

**DP-22 · Visitor [Bh]**
- [ ] DP-22
- **Intent:** represent an operation over elements of an object structure, adding new operations without changing element classes.
- **Problem:** a stable hierarchy (an AST) keeps needing new operations (print, evaluate, optimize) without editing every node class each time.
- **Structure:** each element implements `accept(visitor)`, calling back `visitor.visitX(this)` — "double dispatch."
- **Trade-offs:** the most conceptually demanding GoF pattern — adding a new *element* type requires touching every visitor, the inverse of Strategy's trade-off.
- **Real-world example:** a compiler walking an AST to type-check, then again to generate code — each a separate Visitor over the same fixed hierarchy.
- **Named real examples:** Go's `go/ast.Walk` with an `ast.Visitor`; compiler passes over a fixed syntax tree.
- **GCP lens:** few Google Cloud APIs expose Visitor directly; you meet it in tooling that walks a fixed tree, such as policy checks over a Kubernetes manifest or a Terraform plan.
- **Check:** state precisely what becomes easy to add (operations) and what becomes hard (element types), and why that's the opposite of Strategy.

**DP-23 · Interpreter [Bh]**
- [ ] DP-23
- **Intent:** given a grammar, define a representation for it plus an interpreter that evaluates sentences in it.
- **Problem:** repeatedly evaluating expressions in a small, well-defined grammar.
- **Structure:** each grammar rule becomes a class implementing `interpret(context)`; a sentence becomes a tree of these (often built with Composite, DP-08).
- **Trade-offs:** GoF itself flags this as suited only to *simple* grammars — the pattern most rarely used verbatim in modern industry code.
- **Real-world example:** a simple rules engine evaluating `age > 18 AND hasLicense`.
- **Named real examples:** CEL (the Common Expression Language), evaluated by IAM Conditions and by Kubernetes validation rules; Go's `regexp` and `text/template`, each of which parses a small language into a tree and evaluates it.
- **GCP lens:** CEL expressions in IAM Conditions and in Cloud Armor's custom rules language are interpreted against each request `(verify)`.
- **Check:** what specifically grows unmanageable as grammar rules multiply, per GoF's own warning?

---

## 7. Architecture — Clean/Hexagonal/Onion, DDD, and Enterprise/Microservice Patterns (ARCH-01…12)

Where §6 shaped classes, this section shapes *systems* — often built by applying several §4–§6 tools at once, at scale. Per stitching rule 5: don't confuse with B3's deployment-resilience patterns.

**ARCH-01 · Layered (N-Tier) Architecture** — horizontal layers (Presentation→Business Logic→Data Access), each calling only the layer below. Simple and default for a reason, but strict layering forces pass-through code and lets business logic quietly leak into data-access over time.
- [ ] ARCH-01
- **Check:** a request to "show the order total" passes through Presentation, Business Logic and Data Access, and the business layer only forwards the call. Name the cost this shows and one legitimate reason to accept it.

**ARCH-02 · Hexagonal Architecture (Ports & Adapters)** — Alistair Cockburn. The application core defines **ports** (interfaces expressing what it needs); external technology plugs in via **adapters** implementing them. The core knows nothing about the database, framework, or external APIs. DIP (PR-05) applied at whole-application scale.
- [ ] ARCH-02
- **Check:** your core defines a port `OrderRepository`. Name the adapter a test uses and the adapter production uses, and say which of the two the core imports.

**ARCH-03 · Onion Architecture** — Jeffrey Palermo. Concentric rings: Domain Model at center, Domain Services, Application Services, Infrastructure/UI outermost. Dependencies point only inward. Structurally near-identical to Hexagonal; the two names largely describe the same idea from different angles.
- [ ] ARCH-03
- **Check:** Onion and Hexagonal describe nearly the same structure. What does Onion's ring picture add that "ports and adapters" does not say explicitly?

**ARCH-04 · Clean Architecture** — Robert C. Martin. Synthesizes Hexagonal/Onion: **Entities** → **Use Cases** → **Interface Adapters** → **Frameworks & Drivers**. **The Dependency Rule:** source dependencies point only inward; an inner circle may know nothing about an outer one, not even its name. Data crossing a boundary must be framework-independent (plain structures), never a leaking ORM entity or HTTP object.
- [ ] ARCH-04
**Why it matters practically:** a Clean Architecture codebase can swap its database, web framework, or UI without touching business logic, because business logic never depended on any of them.
**Check:** why is it a dependency-rule violation for a `UseCase` to import an ORM's `@Entity` annotation onto its own domain object, even for "just one annotation"?

**ARCH-05 · MVC / MVP / MVVM family** — **MVC:** `Model` holds data/logic, `View` renders, `Controller` handles input; the View typically observes the Model (DP-14). **MVP:** the View is passive; a `Presenter` handles all UI logic, updating the View via an interface — more testable than MVC's often-blurry line. **MVVM:** a `ViewModel` exposes state the View **data-binds** to automatically. All three apply PR-08 (Controller) and DP-14 (Observer) at UI-architecture scale.
- [ ] ARCH-05
- **Check:** in MVP the View is passive. What can you unit-test in MVP without a UI framework that is hard to test in classic MVC?

**ARCH-06 · Domain-Driven Design — tactical building blocks** — Eric Evans.
- [ ] ARCH-06
- **Entity:** defined by identity, not attributes.
- **Value Object:** defined entirely by attributes, no identity, typically immutable.
- **Aggregate:** a cluster of Entities/Value Objects as one consistency boundary, with a single **Aggregate Root** as the only external entry point.
- **Repository:** collection-like access to Aggregates, hiding persistence (PR-12 in action).
  - *Owner pointer:* Repository's definition is owned by ARCH-07 (Fowler, PoEAA). Here, recall it in one line and add the DDD constraint: one repository per aggregate root.
- **Domain Event:** something significant that happened, often triggering decoupled side effects (DP-14 at domain scale).
- **Bounded Context:** an explicit boundary within which a model is internally consistent — the same word can mean different things in different contexts, deliberately.
- **Check:** an `Order` aggregate holds `OrderLine`s. Another service wants to change one line's quantity directly. What rule does that break, and what must it do instead?

**ARCH-07 · Enterprise patterns (Fowler, PoEAA)** — **Repository:** collection-like interface between domain and data-mapping. **Unit of Work:** tracks changes during a transaction, writes them out atomically. **DTO:** a plain, no-behavior object moving data across a boundary — deliberately not the domain Entity, avoiding structure leakage (connects to Clean Architecture's boundary rule). **Service Layer:** defines an application boundary with use-case-shaped operations.
- [ ] ARCH-07
- **Check:** what does a Unit of Work add on top of several Repositories when one business operation changes three aggregates?

**ARCH-08 · Dependency Injection & IoC Containers** — recall PR-05: DIP is the principle, DI is the mechanism. **Constructor injection** (generally preferred — dependencies are visible, impossible to forget), **setter injection**, **interface injection**. An **IoC Container** automates wiring at scale, typically at app startup.
- [ ] ARCH-08
- **Check:** a class takes its database connection through a setter that tests sometimes forget to call. Which injection style removes that failure, and why?

**ARCH-09 · CQRS** *(gated behind A9)* — separate the **write** model (Commands, invariant-enforcing) from the **read** model (Queries, often denormalized). Not universal — earns its keep when read/write shapes and scale diverge significantly; the read model may lag the write model, which is SD-05's eventual consistency, reapplied.
- [ ] ARCH-09
- **Check:** when is CQRS not worth it? Give the condition on the read and write models under which one model is enough.

**ARCH-10 · Event Sourcing** *(gated behind A9)* — store the sequence of **events** (`OrderCreated`, `ItemAdded`) rather than current state; current state is derived by replaying. Gains a full audit trail and point-in-time reconstruction; costs cheap "current state" queries (hence the common pairing with ARCH-09) and requires periodic **snapshots** to bound replay cost.
- [ ] ARCH-10
- **Check:** an event-sourced account has 2 million events. How do you keep reads fast without giving up the event log as the source of truth?

**ARCH-11 · Saga Pattern** *(gated behind A9)* — manages a distributed transaction across services (no cross-service ACID, per A9's CAP material) via local transactions each with a **compensating transaction** to undo on failure. **Choreography** (each service reacts to events — Observer-shaped) vs. **orchestration** (one coordinator calls each step — Mediator-shaped).
- [ ] ARCH-11
- **Check:** step 3 of a four-step saga fails after steps 1 and 2 committed in other services. What runs next, and why is that not a rollback in the ACID sense?

**ARCH-12 · Resilience micro-patterns** *(gated behind A9)* — **Circuit Breaker:** wraps a remote call; after enough failures, "opens" and fails fast for a cooldown, protecting the caller. **Strangler Fig:** incrementally migrate a legacy system by routing growing traffic shares to new services via a facade/proxy layer until legacy is retired — the formal pattern behind C4's legacy-migration-via-CI/CD question. **Bulkhead:** isolate resources per downstream dependency so one failing dependency can't exhaust resources needed elsewhere.
- [ ] ARCH-12
- **Check:** a circuit breaker is open. What happens to a call now, and what event moves it to half-open?

---

## 8. Anti-Patterns (AP-01…10)

Most arise from a *correct* pattern applied poorly, or a principle ignored under deadline pressure.

- **AP-01 God Object:** one class knows/does far too much (maximal SRP violation) — grows because "just add it here" is always the path of least resistance.
  - **Check:** a `Platform` class has 3,000 lines and imports half the codebase. Which principle is violated at its root, and what is the first extraction you make?
- **AP-02 Spaghetti Code:** tangled control flow from ignoring SRP and Low Coupling (PR-09) over many incremental changes.
  - **Check:** a function has seven nested `if`s and three flags that change meaning halfway down. Name the restructuring you apply first.
- **AP-03 Golden Hammer:** applying a familiar pattern to every problem regardless of fit — a reminder every pattern here has a specific problem it solves.
  - **Check:** a team uses event sourcing for a settings page with one user. Which anti-pattern is this, and what question should have stopped it?
- **AP-04 Anemic Domain Model:** domain objects as pure data bags with all logic in separate "service" classes — violates F-01's actual point (a data bag protects no invariant).
  - **Check:** an `Invoice` has only getters and setters, and `InvoiceService` enforces "total equals the sum of the lines". What is wrong, and where should the rule live?
- **AP-05 Big Ball of Mud:** no recognizable architecture — the end state of consistently ignoring ARCH-01…04's boundary discipline.
  - **Check:** every module imports every other and there is no layer rule. Which ARCH item gives the first boundary to draw?
- **AP-06 Cargo Cult Programming:** copying a pattern's structure without understanding the problem it solves.
  - **Check:** a team adds a `Factory` for every class "because patterns are best practice". Which anti-pattern is this, and which test tells you whether a factory is justified?
- **AP-07 Premature Optimization:** applying a pattern (often Flyweight) for a performance problem that doesn't yet exist.
  - **Check:** someone adds a Flyweight to a form with 12 fields. What is the evidence you ask for before accepting it?
- **AP-08 Magic Numbers/Strings:** unexplained literals (`if (status == 3)`) — a small-scale Encapsulation failure, since the meaning is hidden nowhere.
  - **Check:** `if status == 3` appears in six files. What replaces the literal, and which principle does the replacement serve?
- **AP-09 Shotgun Surgery:** one logical change requires editing many unrelated classes — the mirror image of SRP done right.
  - **Check:** adding one field to "customer" requires edits in eleven files. Which principle, done right, would have kept the change in one place?
- **AP-10 Interface Bloat:** the ISP (PR-04) violation restated as a smell — an interface with far more methods than any implementer needs.
  - **Check:** a `Storage` interface has 30 methods, and most callers use 2. Which principle applies, and what do you split it into?

- [ ] AP-01 · [ ] AP-02 · [ ] AP-03 · [ ] AP-04 · [ ] AP-05 · [ ] AP-06 · [ ] AP-07 · [ ] AP-08 · [ ] AP-09 · [ ] AP-10

**Integration check:** a `UserManager` has 40 methods covering auth, email, reports, and DB migrations. Name the anti-pattern and the SOLID violation at its root.

---

## 9. UML essentials for expressing these patterns

- **Inheritance ("is-a"):** solid line, **hollow triangle**, pointing at the parent/interface.
- **Interface realization:** dashed line, hollow triangle — same arrowhead, dashed instead of solid.
- **Composition ("owns-a," lifecycle-bound):** solid line, **filled diamond** at the owner end.
- **Aggregation ("has-a," independent lifecycle):** solid line, **hollow diamond** at the owner end.
- **Association ("uses/knows about"):** plain solid line, optional directional arrowhead.
- **Dependency (weaker, often temporary "uses"):** dashed line, open arrowhead.

**Check:** a `Car` connects to `Engine` with a filled diamond, and to `Driver` with a plain arrowed line. State what each relationship means and why they're drawn differently.

---

## 10. Dependency gate — teaching order (enforced)

1. F-01…04 (recall-heavy, fast)
2. PR-01…05 (SOLID) — each before any pattern that embodies it
3. PR-06…14 (GRASP) — fast, mostly definitional
4. DP-01…05 → DP-06…12 → DP-13…23, in that order
5. ARCH-01…08 — requires §6 complete
6. ARCH-09…12 — requires A9 also complete; hold back and flag if not
7. AP-01…10 — taught last, explicitly as violations of principles/patterns already covered, never introduced cold
8. The additions of the academic pass (learner decision of 2026-09-24): the per-item checks come with their items; the section skip-tests (§12) may be taken before a section to skip it; each Go kata (§13) runs once GO-11 and any later Go card its task line names are `taught` (rule 0.4.9), and is done on paper before then; the exercise bank (§14) follows §8; the academic pass (§15) follows the items each block names.

---

## 11. Sources & honesty notes

- GoF definitions (§6) adapt Gamma, Helm, Johnson, Vlissides (1994) — "Intent" lines are close paraphrases, since exact phrasing is often what's tested.
- SOLID (§4) synthesizes Martin's writing across *Agile Software Development* (2002) and *Clean Architecture* (2017) — Martin revised SRP's phrasing over time; this file uses the sharper, later "one actor" version.
- GRASP (§5) is from Larman, *Applying UML and Patterns* — less universally taught than SOLID/GoF, included for full theoretical rigor.
- ARCH-02/03 (Hexagonal/Onion) predate and directly informed ARCH-04 (Clean Architecture) — treat the three as one lineage, not three unrelated ideas.
- `(debated)` flags (Singleton, primarily) reflect genuine, ongoing industry disagreement — present both sides, don't adjudicate.

---

## 12. Skip-tests (one per section)

A skip-test lets the learner skip a section by passing it (rule 0.4.1). Each is three questions; all three must be answered correctly, without hints, against the keys in Appendix K. A miss sends the learner into the section, starting with the item the miss points to.

- **DPS-3 · Foundations (§3).** (a) Give an invariant that a public field cannot protect. (b) Give a class that is encapsulated but a poor abstraction. (c) Explain why `Square extends Rectangle` breaks substitution.
- **DPS-4 · SOLID (§4).** (a) State SRP in terms of actors. (b) State the two contract rules an override must follow under LSP. (c) Distinguish DIP from dependency injection in one sentence each.
- **DPS-5 · GRASP (§5).** (a) Name the principle that assigns a responsibility to the class that has the data. (b) Name the principle that justifies a `Repository`. (c) Name the principle behind wrapping an unstable API.
- **DPS-6.1 · Creational patterns (§6.1).** (a) What does Abstract Factory make hard to add? (b) Why can a shallow Prototype clone be a bug? (c) Why is a hand-written Singleton hard to test?
- **DPS-6.2 · Structural patterns (§6.2).** (a) Adapter versus Facade, by intent. (b) Decorator versus Proxy, by intent. (c) Intrinsic versus extrinsic state in Flyweight.
- **DPS-6.3 · Behavioral patterns (§6.3).** (a) Strategy versus State. (b) Visitor versus Strategy: what each makes easy to add. (c) What a Memento hides and from whom.
- **DPS-7 · Architecture (§7).** (a) State the dependency rule. (b) What is an aggregate's consistency boundary? (c) What does a saga give up compared with a distributed ACID transaction?
- **DPS-8 · Anti-patterns (§8).** (a) God Object: the principle violated. (b) Anemic Domain Model: why it is a smell. (c) Shotgun Surgery: its mirror-image principle.

## 13. Go katas (one per pattern) `[local]`

One small, test-driven kata per GoF pattern, written in Go, the suite's implementation language (rule 0.4.9). The suite standard first asked for Python katas; Go replaces Python here because the suite's application code is Go, and the change is recorded as a deviation (the learner decisions that made Go the implementation language, and that of 2026-09-24). For each kata the learner makes a scratch module whose `go.mod` has the `go` line 1.27.1 and the package name shown in the test, writes the solution in one `.go` file, saves the given test beside it in a file whose name ends in `_test.go`, and runs `gofmt -l .`, `go vet ./...` and `go test ./...` (and `go test -race ./...` from GO-19 on). Everything runs offline; nothing is downloaded. The reference solutions are in Appendix K, to be opened only after the tests pass or the learner asks for the key. Every given test passed against its reference solution, with `gofmt`, `go vet` and `go test -race` clean (checked on 1.27.1, 2026-09-24).

### 13.1 Kata for DP-01 · Singleton

**Task.** Write `Config`, a package-level function value that returns the same `*Settings` on every call and counts each load in a package variable `loads`, safe when 50 goroutines call it at once. Needs GO-18 (`sync.OnceValue`).

Given test:

```go
package dp01

import (
	"sync"
	"testing"
)

func TestConfigOnce(t *testing.T) {
	var wg sync.WaitGroup
	got := make([]*Settings, 50)
	for i := range got {
		wg.Add(1)
		go func() {
			defer wg.Done()
			got[i] = Config()
		}()
	}
	wg.Wait()
	for _, s := range got {
		if s != got[0] {
			t.Fatal("two different instances")
		}
	}
	if loads != 1 {
		t.Fatalf("loads = %d, want 1", loads)
	}
}
```

### 13.2 Kata for DP-02 · Factory Method

**Task.** Write the `Store` interface (`Put`, `Get`) and `NewStore(kind string) (Store, error)`, which returns an in-memory store for "memory" and an error for any other kind; the caller never names the concrete type.

Given test:

```go
package dp02

import "testing"

func TestNewStore(t *testing.T) {
	s, err := NewStore("memory")
	if err != nil {
		t.Fatal(err)
	}
	s.Put("a", "1")
	if v, ok := s.Get("a"); !ok || v != "1" {
		t.Fatalf("Get(a) = %q, %v", v, ok)
	}
	if _, err := NewStore("tape"); err == nil {
		t.Fatal("unknown kind must be an error")
	}
}
```

### 13.3 Kata for DP-03 · Abstract Factory

**Task.** Write the `Factory` interface (`NewLogger`, `NewMetrics`) and two factories, `LocalFactory` and `CloudFactory`, whose products report the same `Family()`, so a family can never be mixed.

Given test:

```go
package dp03

import "testing"

func TestFamiliesNeverMix(t *testing.T) {
	for _, f := range []Factory{LocalFactory{}, CloudFactory{}} {
		if f.NewLogger().Family() != f.NewMetrics().Family() {
			t.Fatalf("%T produced a mixed family", f)
		}
	}
	if (LocalFactory{}).NewLogger().Family() == (CloudFactory{}).NewLogger().Family() {
		t.Fatal("the two families must differ")
	}
}
```

### 13.4 Kata for DP-04 · Builder

**Task.** Write `NewRequest(url)`, returning a `*Builder` with `WithTimeout`, `WithRetries` and `Build() (Request, error)`; `Build` applies a 30-second default timeout and rejects an empty URL and negative retries.

Given test:

```go
package dp04

import (
	"testing"
	"time"
)

func TestBuilder(t *testing.T) {
	r, err := NewRequest("https://example.com").WithRetries(3).Build()
	if err != nil || r.Timeout != 30*time.Second || r.Retries != 3 {
		t.Fatalf("got %+v, %v", r, err)
	}
	if _, err := NewRequest("").Build(); err == nil {
		t.Fatal("empty URL must fail")
	}
	if _, err := NewRequest("x").WithRetries(-1).Build(); err == nil {
		t.Fatal("negative retries must fail")
	}
}
```

### 13.5 Kata for DP-05 · Prototype

**Task.** Write `Template.Clone()` so that changing the clone's `Tags` never changes the original's (a deep copy: the clone gets its own backing array).

Given test:

```go
package dp05

import "testing"

func TestCloneIsDeep(t *testing.T) {
	orig := Template{Name: "base", Tags: []string{"a", "b"}}
	c := orig.Clone()
	c.Tags[0] = "changed"
	if orig.Tags[0] != "a" {
		t.Fatal("clone shares its slice with the original")
	}
}
```

### 13.6 Kata for DP-06 · Adapter

**Task.** Write `Adapter`, which makes a `LegacyThermometer` (Fahrenheit, `ReadF`) satisfy the `Celsius` interface.

Given test:

```go
package dp06

import "testing"

func TestAdapter(t *testing.T) {
	var c Celsius = Adapter{LegacyThermometer{F: 212}}
	if c.C() != 100 {
		t.Fatalf("C() = %v, want 100", c.C())
	}
}
```

### 13.7 Kata for DP-07 · Bridge

**Task.** Write the `Renderer` interface and two renderers, `SVG` and `Text`, and a `Circle` (a radius, then a renderer) whose `Draw` delegates to whichever renderer it holds, so shapes and renderers vary independently.

Given test:

```go
package dp07

import "testing"

func TestBridge(t *testing.T) {
	if got := (Circle{2, SVG{}}).Draw(); got != `<circle r="2"/>` {
		t.Fatal(got)
	}
	if got := (Circle{2, Text{}}).Draw(); got != "circle(r=2)" {
		t.Fatal(got)
	}
}
```

### 13.8 Kata for DP-08 · Composite

**Task.** Write `Node`, `File` and `Dir`, so `Size()` on a directory sums every file below it through the one interface.

Given test:

```go
package dp08

import "testing"

func TestComposite(t *testing.T) {
	root := Dir{[]Node{File{10}, Dir{[]Node{File{5}, File{7}}}, Dir{}}}
	if root.Size() != 22 {
		t.Fatalf("Size = %d, want 22", root.Size())
	}
}
```

### 13.9 Kata for DP-09 · Facade

**Task.** Write `Subsystems.Buy(item, cents)`, the facade: reserve, then charge, then ship; if the charge fails, release the reservation and return the error. The steps are recorded in `Log`.

Given test:

```go
package dp09

import (
	"slices"
	"testing"
)

func TestFacade(t *testing.T) {
	ok := &Subsystems{}
	if err := ok.Buy("book", 1200); err != nil {
		t.Fatal(err)
	}
	if !slices.Equal(ok.Log, []string{"reserve book", "charge", "ship book"}) {
		t.Fatal(ok.Log)
	}
	bad := &Subsystems{CardDenied: true}
	if err := bad.Buy("book", 1200); err == nil {
		t.Fatal("want an error")
	}
	if !slices.Equal(bad.Log, []string{"reserve book", "charge", "release book"}) {
		t.Fatal(bad.Log)
	}
}
```

### 13.10 Kata for DP-10 · Flyweight

**Task.** Write a `Factory` whose `Get(r rune)` returns one shared `*Glyph` per distinct rune, and `Distinct()`, the number of glyphs made.

Given test:

```go
package dp10

import "testing"

func TestFlyweight(t *testing.T) {
	var f Factory
	var gs []*Glyph
	for _, r := range "banana" {
		gs = append(gs, f.Get(r))
	}
	if f.Distinct() != 3 {
		t.Fatalf("Distinct = %d, want 3", f.Distinct())
	}
	if gs[1] != gs[3] {
		t.Fatal("the two 'a' glyphs must be one shared value")
	}
}
```

### 13.11 Kata for DP-11 · Proxy

**Task.** Write `CachingProxy` (field `Real Fetcher`), a `Fetcher` in front of a `Backend` that forwards each key's first request and answers repeats from its cache.

Given test:

```go
package dp11

import "testing"

func TestProxy(t *testing.T) {
	b := &Backend{}
	var f Fetcher = &CachingProxy{Real: b}
	f.Fetch("k")
	if f.Fetch("k") != "value:k" || b.Calls != 1 {
		t.Fatalf("backend calls = %d, want 1", b.Calls)
	}
}
```

### 13.12 Kata for DP-12 · Decorator

**Task.** Write the decorators `Upper` and `Exclaim`, each `func(Handler) Handler`, so they stack in any order.

Given test:

```go
package dp12

import "testing"

func TestDecorators(t *testing.T) {
	base := Handler(func(s string) string { return "hi " + s })
	if got := Exclaim(Upper(base))("ann"); got != "HI ANN!" {
		t.Fatal(got)
	}
	if got := Upper(Exclaim(base))("ann"); got != "HI ANN!" {
		t.Fatal(got)
	}
	if got := Exclaim(Exclaim(base))("ann"); got != "hi ann!!" {
		t.Fatal(got)
	}
}
```

### 13.13 Kata for DP-13 · Strategy

**Task.** Write `Pricing` (a function type), the strategies `Full` and `TenOff`, and `Checkout.Total`, which applies the chosen strategy to the sum.

Given test:

```go
package dp13

import "testing"

func TestStrategy(t *testing.T) {
	items := []int{1000, 500}
	if (Checkout{Full}).Total(items) != 1500 {
		t.Fatal("full price")
	}
	if (Checkout{TenOff}).Total(items) != 1350 {
		t.Fatal("ten percent off")
	}
}
```

### 13.14 Kata for DP-14 · Observer

**Task.** Write a `Bus` whose `Subscribe(f)` returns an unsubscribe function and whose `Publish(msg)` calls every current subscriber.

Given test:

```go
package dp14

import "testing"

func TestObserver(t *testing.T) {
	var b Bus
	var a, c []string
	stopA := b.Subscribe(func(m string) { a = append(a, m) })
	b.Subscribe(func(m string) { c = append(c, m) })
	b.Publish("one")
	stopA()
	b.Publish("two")
	if len(a) != 1 || len(c) != 2 {
		t.Fatalf("a=%v c=%v", a, c)
	}
}
```

### 13.15 Kata for DP-15 · Template Method

**Task.** Write `Run(s Steps) (int, error)`: fetch, transform each value, and sum, in that fixed order; a fetch error stops the run.

Given test:

```go
package dp15

import (
	"errors"
	"testing"
)

type squares struct{}

func (squares) Fetch() ([]int, error) { return []int{1, 2, 3}, nil }
func (squares) Transform(x int) int   { return x * x }

type broken struct{ squares }

func (broken) Fetch() ([]int, error) { return nil, errors.New("down") }

func TestTemplate(t *testing.T) {
	if got, err := Run(squares{}); err != nil || got != 14 {
		t.Fatalf("got %d, %v", got, err)
	}
	if _, err := Run(broken{}); err == nil {
		t.Fatal("fetch error must stop the skeleton")
	}
}
```

### 13.16 Kata for DP-16 · State

**Task.** Write the states `Pending`, `Paid` and `Shipped`, each with `Name()` and `On(event) State`; "pay" moves pending to paid, "ship" moves paid to shipped, and any other event leaves the state unchanged.

Given test:

```go
package dp16

import "testing"

func TestState(t *testing.T) {
	var s State = Pending{}
	for _, e := range []string{"ship", "pay", "pay", "ship", "pay"} {
		s = s.On(e)
	}
	if s.Name() != "shipped" {
		t.Fatalf("state = %s, want shipped", s.Name())
	}
	if (Pending{}).On("ship").Name() != "pending" {
		t.Fatal("cannot ship before paying")
	}
}
```

### 13.17 Kata for DP-17 · Command

**Task.** Write the `Append` command with `Do` and `Undo`, and an `Editor` whose `Run` executes and records a command and whose `Undo` reverses the last one.

Given test:

```go
package dp17

import "testing"

func TestCommand(t *testing.T) {
	var e Editor
	e.Run(Append{"hello"})
	e.Run(Append{" world"})
	e.Undo()
	if e.Doc.Text != "hello" {
		t.Fatalf("text = %q", e.Doc.Text)
	}
	e.Undo()
	e.Undo()
	if e.Doc.Text != "" {
		t.Fatalf("text = %q", e.Doc.Text)
	}
}
```

### 13.18 Kata for DP-18 · Chain of Responsibility

**Task.** Write `Chain(final, links...)` and the links `RejectAnonymous` (answers "401" to the request "anon") and `RejectBlocked` (answers "403" to "blocked"); each link either answers or calls the next, and the first link given runs first.

Given test:

```go
package dp18

import "testing"

func TestChain(t *testing.T) {
	h := Chain(func(string) string { return "200" }, RejectAnonymous, RejectBlocked)
	for req, want := range map[string]string{"anon": "401", "blocked": "403", "ann": "200"} {
		if got := h(req); got != want {
			t.Fatalf("%s: got %s, want %s", req, got, want)
		}
	}
}
```

### 13.19 Kata for DP-19 · Mediator

**Task.** Write a `Room` mediator: `Join(name)` returns a `*User` with an `Inbox`, and `User.Say(msg)` puts "name: msg" in every other user's inbox through the room, never directly.

Given test:

```go
package dp19

import "testing"

func TestMediator(t *testing.T) {
	var r Room
	a, b, c := r.Join("a"), r.Join("b"), r.Join("c")
	a.Say("hi")
	if len(a.Inbox) != 0 || len(b.Inbox) != 1 || len(c.Inbox) != 1 || b.Inbox[0] != "a: hi" {
		t.Fatalf("a=%v b=%v c=%v", a.Inbox, b.Inbox, c.Inbox)
	}
}
```

### 13.20 Kata for DP-20 · Iterator

**Task.** Write `Countdown(n) iter.Seq[int]`, which yields n, n−1, …, 1 and stops at once when the loop breaks. Needs GO-12 (`iter.Seq`).

Given test:

```go
package dp20

import (
	"slices"
	"testing"
)

func TestIterator(t *testing.T) {
	if got := slices.Collect(Countdown(3)); !slices.Equal(got, []int{3, 2, 1}) {
		t.Fatal(got)
	}
	seen := 0
	for v := range Countdown(10) {
		seen++
		if v == 8 {
			break
		}
	}
	if seen != 3 {
		t.Fatalf("seen = %d, want 3", seen)
	}
}
```

### 13.21 Kata for DP-21 · Memento

**Task.** Write an `Editor` with `Save() Memento` and `Restore(Memento)`, where the memento's field is unexported, so no other package can read or change it.

Given test:

```go
package dp21

import "testing"

func TestMemento(t *testing.T) {
	e := &Editor{Text: "v1"}
	snap := e.Save()
	e.Text = "v2"
	e.Restore(snap)
	if e.Text != "v1" {
		t.Fatalf("text = %q", e.Text)
	}
}
```

### 13.22 Kata for DP-22 · Visitor

**Task.** Write the visitors `Eval` and `Print` over `Num` and `Add`, so a new operation is a new visitor and no expression type changes.

Given test:

```go
package dp22

import "testing"

func TestVisitor(t *testing.T) {
	e := Add{Num{1}, Add{Num{2}, Num{3}}}
	var ev Eval
	var pr Print
	e.Accept(&ev)
	e.Accept(&pr)
	if ev.Result != 6 || pr.Out != "(1 + (2 + 3))" {
		t.Fatalf("eval=%d print=%s", ev.Result, pr.Out)
	}
}
```

### 13.23 Kata for DP-23 · Interpreter

**Task.** Write `Eval(src, env)` for the grammar `expr := term { "AND" term }`, `term := "NOT" term | name`, returning an error for an unknown name or a malformed expression.

Given test:

```go
package dp23

import "testing"

func TestInterpreter(t *testing.T) {
	env := map[string]bool{"adult": true, "banned": false}
	if v, err := Eval("adult AND NOT banned", env); err != nil || !v {
		t.Fatalf("got %v, %v", v, err)
	}
	if v, _ := Eval("NOT adult", env); v {
		t.Fatal("NOT adult should be false")
	}
	if _, err := Eval("adult OR banned", env); err == nil {
		t.Fatal("OR is not in the grammar")
	}
}
```

## 14. Exercise bank (DPE-01…DPE-12)

Transfer exercises that combine several items. They climb the ramp (rule 0.4.3); each starts with a one-line prediction (rule 0.4.4). Keys are in Appendix K.

- **DPE-01** · rung 5 · A checkout service must support three payment providers now and more later, and each provider's SDK has a different interface. Choose two patterns, draw the classes in UML (§9), and say which principle each pattern serves.
- **DPE-02** · rung 5 · A report can be exported as CSV, JSON or PDF, and new formats arrive every quarter; the report's structure never changes. Strategy or Visitor? Justify it from what changes.
- **DPE-03** · rung 6 · A document editor needs unlimited undo across typing, formatting and deletion. Design it with Command and Memento, and say which one you would drop if memory were tight.
- **DPE-04** · rung 6 · An HTTP client needs logging, retries, a circuit breaker and authentication, each switchable per call site. Design the chain in Go (by name only; no code), and state the order and why.
- **DPE-05** · rung 6 · Restructure: an `OrderManager` with 40 methods covers pricing, stock, e-mail and persistence. Name the anti-patterns and give the target classes, each with its GRASP justification.
- **DPE-06** · rung 7 · Place a payment domain into Clean Architecture rings: `Money`, `Order`, `PlaceOrder`, `StripeGateway`, `PostgresOrderRepository`, `HTTPHandler`. Mark every dependency arrow and check each against the dependency rule.
- **DPE-07** · rung 7 · An `Order` aggregate must keep "total equals the sum of the lines" and "at most 50 lines". Write the invariants, the aggregate's public methods, and the one method a repository needs.
- **DPE-08** · rung 7 · Model an order's lifecycle (created, paid, shipped, cancelled, refunded) with the State pattern. List every legal transition and say what an illegal event does.
- **DPE-09** · rung 8 · A booking spans three services (flight, hotel, car). Design the saga: the steps, the compensations and the order of compensation, and one failure the compensations cannot hide from the user.
- **DPE-10** · rung 8 · An event-sourced cart must answer "items in the cart now" in under 10 ms with 10⁶ events per cart at worst. Design the read side with CQRS and snapshots, and say how you rebuild a projection after a bug fix.
- **DPE-11** · rung 9 · Critique: "every service gets a Singleton `Config` and a Singleton `DB`". Give two failure modes in tests and one in production, and the replacement.
- **DPE-12** · rung 10 · Capstone design: a notification platform (e-mail, SMS, push) with per-user preferences, retries, rate limits and a provider fallback. Name every pattern you use, the principle behind it, and one pattern you deliberately rejected, with the reason.

## 15. Academic depth (rule 0.4.10)

The academic pass of this companion: the theory under object-oriented design, at the depth of a software-engineering and programming-languages course (main course §0.6: the software-engineering row, and main course A7.D1–A7.D2). Each block is taught after the items it names. Problems DPA-P1…DPA-P8 are in §15.7, keys in Appendix K. Rule 0.4.10: a block is `mastered` only when one proof or derivation problem and one computational problem in it pass.

### 15.1 DPA.1 · Abstract data types and information hiding (deepens F-01, F-02, PR-01)

- An abstract data type is a set of values with operations, specified by what the operations do (their axioms or pre- and postconditions), not by representation (Liskov and Zilles, 1974). A representation invariant says which concrete states are legal; an abstraction function maps each legal concrete state to the abstract value it stands for.
- Parnas's criterion (1972): decompose so that each module hides one design decision likely to change. Encapsulation (F-01) is the language mechanism; information hiding is the design criterion it serves.

### 15.2 DPA.2 · Behavioural subtyping, formally (deepens PR-03, F-03)

- The Liskov–Wing rule (1994): S is a behavioural subtype of T when, for every method, S's precondition is implied by T's (contravariance: preconditions may only weaken), S's postcondition implies T's (covariance: postconditions may only strengthen), S preserves T's invariants, and S satisfies T's history constraint (no new way to change state that T forbids).
- Type systems check the signature part: method parameters may be contravariant and results covariant. They cannot check the behavioural part, which is why LSP is a design obligation.
- Design by contract (Meyer): contracts as the specification against which substitution is judged.

### 15.3 DPA.3 · The expression problem (deepens DP-13, DP-22, F-04)

- Wadler's expression problem (1998): extend both the set of data variants and the set of operations, without editing or recompiling existing code and with static type safety.
- Object-oriented decomposition (Strategy and Composite: one class per variant) makes new variants easy and new operations hard. Visitor (and functional pattern matching) makes new operations easy and new variants hard. DPA-P3 asks for the count.
- Solutions in the literature (object algebras, type classes, tagless final) are named, not taught.

### 15.4 DPA.4 · Patterns as language features (deepens §6)

- Norvig (1996) observed that 16 of the 23 GoF patterns are simpler or invisible in a language with first-class functions, dynamic types and macros.
- The functional correspondences: Strategy and Command are functions as values; Template Method is a higher-order function that takes the steps; Iterator is a generator or a fold (Go's `iter.Seq` is a push iterator); Visitor is a fold over an algebraic data type (a catamorphism); Decorator is function composition; Observer is a list of callbacks. The Go katas of §13 show several of these directly.
- What survives the translation is the design decision about which axis of change to protect. That decision is the pattern; the class diagram is only one encoding of it.

### 15.5 DPA.5 · Design quality metrics (deepens PR-09, PR-10, AP-01, AP-05)

- The Chidamber–Kemerer suite (1994): weighted methods per class (WMC), depth of inheritance tree (DIT), number of children (NOC), coupling between objects (CBO), response for a class (RFC) and lack of cohesion in methods (LCOM). These measures correlate with fault-proneness in later empirical studies, but a metric is a signal, not a verdict.
- Martin's package metrics: afferent coupling Ca (who depends on me), efferent coupling Ce (whom I depend on), instability I = Ce / (Ca + Ce), abstractness A (the share of abstract types), and the distance from the main sequence D = |A + I − 1|. The Stable Abstractions Principle says a stable package should be abstract.
- Cyclomatic complexity (McCabe, 1976): V(G) = E − N + 2P for a control-flow graph with E edges, N nodes and P connected components; for one function it equals the number of decisions plus one.

### 15.6 DPA.6 · Architecture, consistency and events (deepens ARCH-06, ARCH-09, ARCH-10, ARCH-11)

- An aggregate is a consistency boundary: its invariants hold after every transaction, which is why one transaction changes one aggregate and why cross-aggregate rules are eventually consistent (main course A9.D3).
- Event sourcing as a left fold: state = foldl(apply, s₀, events). Replays are deterministic only if `apply` is a pure function of the state and the event; snapshots cache a prefix of the fold.
- Sagas (Garcia-Molina and Salem, 1987): a long-lived transaction split into steps T₁…Tₙ with compensations C₁…Cₙ₋₁. The guarantee is that either T₁…Tₙ all run, or T₁…Tₖ run followed by Cₖ…C₁. Compensation is semantic, not an undo of bytes, and the intermediate states are visible to others (no isolation).
- Readings for the whole pass: Liskov and Guttag, *Program Development in Java* (2000); Meyer, *Object-Oriented Software Construction*, 2nd ed. (1997); Wadler, "The Expression Problem" (1998 mailing-list note); Chidamber and Kemerer, "A Metrics Suite for Object Oriented Design", *IEEE Transactions on Software Engineering* 20(6), 1994; Garcia-Molina and Salem, "Sagas" (SIGMOD 1987).

### 15.7 Problem set (DPA-P1…DPA-P8)

- **DPA-P1** · proof · A `Stack` specification says `push(x)` then `pop()` returns x. Give a representation invariant and an abstraction function for a stack stored as a slice plus a length, and show that `push` preserves the invariant.
- **DPA-P2** · proof · `Rectangle.setWidth(w)` has the postcondition "width = w and height unchanged". Show, from the Liskov–Wing rule, that a `Square` override cannot be a behavioural subtype.
- **DPA-P3** · compute · A system has 4 expression variants and 3 operations. Adding one variant and one operation: how many new methods, and how many existing classes edited, under the object-oriented design and under Visitor?
- **DPA-P4** · compute · A package has 3 incoming dependencies, 9 outgoing, and 2 abstract types out of 10. Compute I, A and D, and say what the result suggests.
- **DPA-P5** · compute · A function's control-flow graph has 11 edges, 9 nodes and one component. What is its cyclomatic complexity, and how many test paths does basis-path testing need?
- **DPA-P6** · derive · Write event sourcing's state reconstruction as a fold, and show that a snapshot taken after event k gives the same state as a full replay.
- **DPA-P7** · proof · Show that if every step Tᵢ and compensation Cᵢ of a saga eventually succeeds when retried, the saga ends in one of its two allowed outcomes.
- **DPA-P8** · design · Rewrite Strategy, Command and Template Method as function values in Go (signatures only), and say what the class-based versions give that the function forms do not.

---

## Appendix K — Keys (AFTER attempt only)

Keys for every check in this companion, the skip-tests (§12), the Go katas (§13), the exercise bank (§14) and the academic problems (§15.7). Each key gives the expected answer and at least one expected wrong answer (rule 0.4.7). Open a key only after the learner's attempt.

### K-checks · the item checks (§3–§9)

- **F-01** — Expected: the non-negative balance (or "every change is a recorded transaction"); `withdraw` can refuse, but a public field accepts any assignment. · Wrong: "it hides the data" — hiding is the mechanism, the invariant is the point.
- **F-02** — Expected: a class with private fields whose methods expose its internal steps (`setBufferSize`, `flushInternalCache`), so callers must know how it works. · Wrong: "a class with public fields" — that fails encapsulation, not abstraction.
- **F-03** — Expected: callers of `Rectangle` rely on "setting the width leaves the height alone"; `Square` breaks that postcondition, so code correct for rectangles fails for squares. Mathematical "is-a" is not behavioural "is-a". · Wrong: "it works because a square is a rectangle".
- **F-04** — Expected: the caller depends only on the `Animal` interface; the new subclass supplies its own `makeSound`, so no calling code changes. · Wrong: "because inheritance copies the code".
- **PR-01** — Expected: presentation (whoever owns the report's format) and storage (whoever owns the bucket layout); after the split, a format change cannot break storage and the reverse. · Wrong: "HTML and Cloud Storage" — those are technologies, not actors.
- **PR-02** — Expected: a `Shape` interface with `area()`; add a `Triangle` type implementing it; never touch the existing shapes or the code that calls `area()`. · Wrong: "add an `else if` for triangle" — that modifies tested code.
- **PR-03** — Expected: `fly()`'s postcondition (the bird is flying) is broken by a throwing override (which also adds a failure the base does not allow). Fix the hierarchy: flying is a capability (`Flyer`), not part of `Bird`. · Wrong: "catch the exception at every call site".
- **PR-04** — Expected: split into `Printer`, `Scanner` and `Fax` interfaces; the inkjet implements only `Printer`, and a multifunction device implements all three. · Wrong: "implement `scan()` and `fax()` to do nothing" — the fat interface stays.
- **PR-05** — Expected: DIP is violated: the high-level service depends on a concrete sender. The missing abstraction is a `Notifier` (or `MessageSender`) interface, injected. · Wrong: "Single Responsibility" — the problem is the direction of the dependency.
- **PR-06** — Expected: `Order`, which holds the lines, each of which knows its price (each `OrderLine` computes its own subtotal); an `OrderService` would have to pull the data out to compute with it. · Wrong: "a service, because computing is business logic" — that leads towards an anemic model (AP-04).
- **PR-07** — Expected: `Order`, because it aggregates (contains) `OrderLine`s — the first of Creator's conditions. · Wrong: "a factory class" — a factory is justified only when creation varies (DP-02), not by default.
- **PR-08** — Expected: the handler keeps only HTTP concerns (parsing, status codes) and delegates the system event to a use-case controller such as `PlaceOrder`, which applies the discount rules through the domain and saves through a repository. · Wrong: "move all of it into the `Order` entity" — HTTP and persistence do not belong in the domain.
- **PR-09** — Expected: depend on an interface the class owns (DIP, PR-05), or introduce a facade or mediator so it talks to one collaborator instead of seven. · Wrong: "merge the seven classes into one" — that trades coupling for a God Object.
- **PR-10** — Expected: unrelated reasons to change meet in one class: a change to e-mail sending risks date parsing and rounding, every user of one function depends on all three, and tests must set up all three. · Wrong: "it is too long" — length is a symptom; unrelated responsibilities are the cost.
- **PR-11** — Expected: a `PaymentMethod` interface with one implementation per type, each carrying its own behaviour; a new type is one new class, and none of the five sites changes. · Wrong: "a sixth `switch`" — every site must still be found and edited.
- **PR-12** — Expected: persistence is not a domain concept, so the `Repository` is invented for design convenience (cohesion and low coupling). `save()` on the entity couples the domain to storage and gives the entity a second reason to change. · Wrong: "the entity knows its own data, so Information Expert puts `save()` there" — Expert is weighed against cohesion and coupling.
- **PR-13** — Expected: a message broker (Pub/Sub, DP-14 at system scale) or an API gateway or mediator between them; it removes the direct dependency, so either side can change, fail or scale independently. · Wrong: "a shared database" — that is tighter coupling, not indirection.
- **PR-14** — Expected: a `PaymentGateway` interface that your code owns, at the point of predicted change; the Adapter pattern (DP-06) implements the protection, one adapter per provider version. · Wrong: "wrap it in try/catch" — that handles failures, not change.
- **PR-06…PR-14 (integration check)** — Expected: Pure Fabrication (PR-12) justifies `PaymentValidator`; High Cohesion (PR-10), or Information Expert weighed against cohesion, answers why it is not inside `Payment`: validation rules change for different reasons than payment data. · Wrong: "Information Expert says it must go in `Payment`" — Expert is weighed against cohesion, not applied alone.
- **DP-01** — Expected: you cannot substitute a fake: the code reaches the instance through a global accessor, so tests share state and cannot inject a double. · Wrong: "it is slow".
- **DP-02** — Expected: Creator decides which class makes the product (PR-07), and the caller depends on the product interface, not the concrete class (PR-05). · Wrong: "it is just a constructor".
- **DP-03** — Expected: the `AbstractFactory` interface gains `createSlider()`, so every concrete factory must change. · Wrong: "only the new theme changes" — that is adding a family, which is the easy direction.
- **DP-04** — Expected: named steps make optional values explicit and order-free, and `build()` validates the whole; ten positional parameters invite swapped arguments and long null lists. · Wrong: "Builder is faster".
- **DP-05** — Expected: the clone shares the original's list, so a change to one appears in the other. · Wrong: "nothing; the clone is a new object" — the object is new, the list is not.
- **DP-06** — Expected: Adapter makes an existing interface fit an expected one; Facade gives a simpler interface to a subsystem. · Wrong: "a Facade wraps one class".
- **DP-07** — Expected: 3 × 4 = 12 subclasses without Bridge (every shape–engine pair); with Bridge 3 + 4 = 7 classes, and adding one shape or one engine adds one class. · Wrong: 7 subclasses without Bridge — that is the Bridge count.
- **DP-08** — Expected: the folder's `totalSize()` calls `totalSize()` on each child, and a subfolder does the same, so the recursion covers the whole tree through one interface. · Wrong: "the folder keeps a cached size".
- **DP-09** — Expected: no; the subsystem stays usable directly, and the facade is one simpler door. · Wrong: "yes, the facade replaces it".
- **DP-10** — Expected: intrinsic: the character's glyph or font; extrinsic: its position on the page. · Wrong: "the colour is always extrinsic" — it depends on whether it is shared.
- **DP-11** — Expected: Adapter converts (an interface), Decorator adds (behaviour), Proxy controls (access). · Wrong: "Proxy is a Decorator with one layer" — the shapes match, the purposes do not.
- **DP-12** — Expected: each decorator has the component's interface, so each can wrap another in any order and number. · Wrong: "they inherit from each other".
- **DP-13** — Expected: a new strategy class implementing the interface; the context is not edited. · Wrong: "a new `case` in the checkout".
- **DP-14** — Expected: shared: publishers know only an interface (a topic, or the observer's update method), never the concrete receivers, and fan-out is one-to-many. Different: in-process observers are called synchronously and share the caller's failure (a panicking observer breaks the notify loop); Pub/Sub adds a network, so delivery is asynchronous, at-least-once and possibly out of order, and a slow subscriber backs up its own subscription instead of the publisher. · Wrong: "they fail the same way, only faster".
- **DP-15** — Expected: Strategy varies a whole algorithm by composition; Template Method varies steps of a fixed algorithm by overriding (or by passing the steps in). Pick Template Method when the skeleton's order is an invariant the base must enforce (setup always before the test, teardown always after). · Wrong: "they are the same pattern".
- **DP-16** — Expected: a Strategy does not choose the next strategy; a State object decides the transition to the next state. · Wrong: "a State has more methods".
- **DP-17** — Expected: an object can be stored, queued, logged and reversed, so undo keeps a list of executed commands, each with its inverse. · Wrong: "because commands run faster".
- **DP-18** — Expected: the request is the object passed along; each handler (middleware) decides to handle it or pass it to the next. · Wrong: "the chain is a list of requests".
- **DP-19** — Expected: without a mediator up to 6 × 5 / 2 = 15 pairwise links; with one, 6 links, all to the mediator. · Wrong: 36 links — that counts each component with itself and each pair twice.
- **DP-20** — Expected: callers use `Next()` (or `range`) the same way over both, so the storage can change without changing callers. · Wrong: "linked lists are faster to iterate".
- **DP-21** — Expected: encapsulation of the originator: only the originator can read the memento's contents, so its internals stay private. · Wrong: "for security".
- **DP-22** — Expected: operations are easy to add (one new visitor); element types are hard (every visitor needs a new method). Strategy is the opposite: new variants are easy, new operations touch every class. · Wrong: "Visitor makes everything easy to add".
- **DP-23** — Expected: one class per grammar rule, so a large grammar becomes a huge class hierarchy that is slow and hard to maintain; GoF recommends a parser generator instead. · Wrong: "it cannot handle recursion".
- **ARCH-01** — Expected: pass-through (sinkhole) code; accepted when the layer rule keeps the data access replaceable and the team small. · Wrong: "layered architecture has no cost".
- **ARCH-02** — Expected: an in-memory adapter in tests and a database adapter in production; the core imports neither, only the port. · Wrong: "the core imports the database adapter".
- **ARCH-03** — Expected: the explicit inward dependency direction across named rings (domain model at the centre, then domain services, then application services). · Wrong: "Onion allows the domain to import infrastructure".
- **ARCH-04** — Expected: the annotation is a source-code dependency from the inner ring on a framework; the domain now changes and fails to compile when the ORM changes. · Wrong: "annotations are metadata, so they don't count".
- **ARCH-05** — Expected: the Presenter's UI logic, against a fake View interface. · Wrong: "the rendering".
- **ARCH-06** — Expected: outside code must go through the aggregate root; the other service asks `Order` to change the line, so the order's invariants are checked. · Wrong: "lock the `OrderLine` row and update it".
- **ARCH-07** — Expected: it tracks every change across the repositories and commits them as one transaction, or none. · Wrong: "it caches reads".
- **ARCH-08** — Expected: constructor injection: the object cannot exist without the dependency. · Wrong: "field injection".
- **ARCH-09** — Expected: when the read and write models have the same shape and scale, one model is enough; CQRS adds a second model and eventual consistency for no gain. · Wrong: "CQRS is always better at scale".
- **ARCH-10** — Expected: snapshots plus read projections: store periodic snapshots and replay from the latest, or keep a projection updated from the log. The log stays the source of truth. · Wrong: "delete old events".
- **ARCH-11** — Expected: the compensations for step 2 and then step 1 run, in reverse order. They are new business actions (refund, cancel), and others may already have seen the intermediate state. · Wrong: "the database rolls back all three services".
- **ARCH-12** — Expected: the call fails fast without reaching the remote service; when the cooldown timer expires, the breaker lets a trial call through (half-open). · Wrong: "it retries the call".
- **AP-01…AP-10 (integration check)** — Expected: a God Object (AP-01), rooted in a Single Responsibility violation (PR-01). · Wrong: "Interface Bloat" — that names the symptom at the interface, not the class.
- **AP-01** — Expected: Single Responsibility (PR-01); extract the responsibility that changes most often, behind an interface. · Wrong: "split the file into two files".
- **AP-02** — Expected: extract method, or replace conditionals with guard clauses and polymorphism (PR-11). · Wrong: "add comments".
- **AP-03** — Expected: Golden Hammer; "what problem does this pattern solve here?" · Wrong: "Premature Optimization" — the motive is familiarity, not speed.
- **AP-04** — Expected: Anemic Domain Model; the rule belongs in `Invoice`, which should refuse inconsistent states. · Wrong: "move it to a validator service".
- **AP-05** — Expected: ARCH-01's layering (or ARCH-04's dependency rule) gives the first boundary. · Wrong: "rewrite everything as microservices".
- **AP-06** — Expected: Cargo Cult Programming; a factory is justified only when the concrete class really varies by context. · Wrong: "Golden Hammer" — close, but the tell here is copying structure without the problem.
- **AP-07** — Expected: a profile or a measurement showing memory pressure from duplicated intrinsic state. · Wrong: "a design review".
- **AP-08** — Expected: a named constant or an enumerated type (`StatusShipped`); it serves encapsulation of meaning and one point of change. · Wrong: "a comment next to each 3".
- **AP-09** — Expected: Single Responsibility, with information hiding: one module owning the customer's representation. · Wrong: "Open/Closed".
- **AP-10** — Expected: Interface Segregation (PR-04); split by client need into small role interfaces. · Wrong: "add default implementations".
- **§9** — Expected: filled diamond: composition, where the car owns the engine and their lifetimes are bound; plain arrow: association, where the car knows a driver who exists independently. · Wrong: "the diamond means inheritance".

### K-skip · skip-tests (§12)

- **DPS-3** — Expected: (a) a non-negative balance; (b) a class exposing its internal steps; (c) the width-setter's postcondition fails for a square. · Wrong: any answer that uses "is-a" in the mathematical sense for (c).
- **DPS-4** — Expected: (a) one actor it answers to; (b) preconditions no stronger and postconditions no weaker; (c) DIP: depend on abstractions; DI: hand dependencies in from outside. · Wrong: treating DIP and DI as synonyms.
- **DPS-5** — Expected: (a) Information Expert; (b) Pure Fabrication; (c) Protected Variations. · Wrong: "Indirection" for (b) — Indirection is the mechanism, Pure Fabrication the justification.
- **DPS-6.1** — Expected: (a) new products; (b) shared mutable state; (c) no substitution of a fake. · Wrong: "new families" for (a).
- **DPS-6.2** — Expected: (a) Adapter converts an interface, Facade simplifies a subsystem; (b) Decorator adds behaviour, Proxy controls access; (c) intrinsic is shared, extrinsic is passed in. · Wrong: "Proxy adds caching, so it is a Decorator" for (b).
- **DPS-6.3** — Expected: (a) a State chooses the next state, a Strategy does not; (b) Visitor: new operations; Strategy: new variants; (c) the originator's internals, from everyone but the originator. · Wrong: reversing (b).
- **DPS-7** — Expected: (a) source dependencies point inward only; (b) the set of objects whose invariants one transaction keeps; (c) isolation and atomic rollback (it uses compensations). · Wrong: "a saga gives up durability".
- **DPS-8** — Expected: (a) SRP; (b) the objects protect no invariant, so the rules scatter; (c) SRP done right (one change, one place). · Wrong: "Open/Closed" for (c).

### K-katas · reference solutions (§13)

Each solution below passed its given test with `gofmt`, `go vet`, `go test` and `go test -race` clean (checked on 1.27.1). A learner's solution passes when the given test passes and the lab-acceptance rule (rule 0.4.9, item 2) holds; it need not match these line by line.

#### K-kata 13.1 · DP-01 Singleton — reference solution

```go
package dp01

import "sync"

// Settings is the one shared configuration value.
type Settings struct{ Region string }

var loads int

// Config returns the same *Settings on every call; the loader runs once.
var Config = sync.OnceValue(func() *Settings {
	loads++
	return &Settings{Region: "europe-west2"}
})
```

#### K-kata 13.2 · DP-02 Factory Method — reference solution

```go
package dp02

import "fmt"

// Store is the product interface.
type Store interface {
	Put(k, v string)
	Get(k string) (string, bool)
}

type memStore struct{ m map[string]string }

func (s *memStore) Put(k, v string) { s.m[k] = v }

func (s *memStore) Get(k string) (string, bool) {
	v, ok := s.m[k]
	return v, ok
}

// NewStore is the factory: the caller names a kind, never a concrete type.
func NewStore(kind string) (Store, error) {
	switch kind {
	case "memory":
		return &memStore{m: map[string]string{}}, nil
	default:
		return nil, fmt.Errorf("unknown store kind %q", kind)
	}
}
```

#### K-kata 13.3 · DP-03 Abstract Factory — reference solution

```go
package dp03

// Logger and Metrics are the two products of one family.
type Logger interface{ Family() string }
type Metrics interface{ Family() string }

// Factory creates a matched family.
type Factory interface {
	NewLogger() Logger
	NewMetrics() Metrics
}

type fam string

func (f fam) Family() string { return string(f) }

// LocalFactory builds the local family.
type LocalFactory struct{}

func (LocalFactory) NewLogger() Logger   { return fam("local") }
func (LocalFactory) NewMetrics() Metrics { return fam("local") }

// CloudFactory builds the cloud family.
type CloudFactory struct{}

func (CloudFactory) NewLogger() Logger   { return fam("cloud") }
func (CloudFactory) NewMetrics() Metrics { return fam("cloud") }
```

#### K-kata 13.4 · DP-04 Builder — reference solution

```go
package dp04

import (
	"errors"
	"time"
)

// Request is built step by step; Build validates the whole.
type Request struct {
	URL     string
	Timeout time.Duration
	Retries int
}

// Builder holds the request under construction.
type Builder struct{ r Request }

// NewRequest starts a builder with the defaults.
func NewRequest(url string) *Builder {
	return &Builder{r: Request{URL: url, Timeout: 30 * time.Second}}
}

func (b *Builder) WithTimeout(d time.Duration) *Builder { b.r.Timeout = d; return b }
func (b *Builder) WithRetries(n int) *Builder           { b.r.Retries = n; return b }

// Build returns the request or the first rule it breaks.
func (b *Builder) Build() (Request, error) {
	switch {
	case b.r.URL == "":
		return Request{}, errors.New("url is required")
	case b.r.Retries < 0:
		return Request{}, errors.New("retries must be >= 0")
	}
	return b.r, nil
}
```

#### K-kata 13.5 · DP-05 Prototype — reference solution

```go
package dp05

import "slices"

// Template is the prototype that new values are copied from.
type Template struct {
	Name string
	Tags []string
}

// Clone is a deep copy: the clone's slice has its own backing array.
func (t Template) Clone() Template {
	return Template{Name: t.Name, Tags: slices.Clone(t.Tags)}
}
```

#### K-kata 13.6 · DP-06 Adapter — reference solution

```go
package dp06

// LegacyThermometer is the adaptee: it reports Fahrenheit.
type LegacyThermometer struct{ F float64 }

func (l LegacyThermometer) ReadF() float64 { return l.F }

// Celsius is the interface the client expects.
type Celsius interface{ C() float64 }

// Adapter makes a LegacyThermometer satisfy Celsius.
type Adapter struct{ L LegacyThermometer }

func (a Adapter) C() float64 { return (a.L.ReadF() - 32) * 5 / 9 }
```

#### K-kata 13.7 · DP-07 Bridge — reference solution

```go
package dp07

import "fmt"

// Renderer is the implementation side of the bridge.
type Renderer interface{ Circle(r float64) string }

type SVG struct{}

func (SVG) Circle(r float64) string { return fmt.Sprintf(`<circle r="%g"/>`, r) }

type Text struct{}

func (Text) Circle(r float64) string { return fmt.Sprintf("circle(r=%g)", r) }

// Circle is the abstraction side; it holds a Renderer instead of subclassing one.
type Circle struct {
	R   float64
	Ren Renderer
}

func (c Circle) Draw() string { return c.Ren.Circle(c.R) }
```

#### K-kata 13.8 · DP-08 Composite — reference solution

```go
package dp08

// Node is the component: a leaf and a composite answer the same call.
type Node interface{ Size() int }

type File struct{ N int }

func (f File) Size() int { return f.N }

type Dir struct{ Children []Node }

func (d Dir) Size() int {
	total := 0
	for _, c := range d.Children {
		total += c.Size()
	}
	return total
}
```

#### K-kata 13.9 · DP-09 Facade — reference solution

```go
package dp09

import "errors"

// Subsystems is what the facade hides; each step is recorded in Log.
type Subsystems struct {
	Log        []string
	CardDenied bool
}

func (s *Subsystems) reserve(item string) { s.Log = append(s.Log, "reserve "+item) }
func (s *Subsystems) release(item string) { s.Log = append(s.Log, "release "+item) }
func (s *Subsystems) ship(item string)    { s.Log = append(s.Log, "ship "+item) }

func (s *Subsystems) charge(cents int) error {
	s.Log = append(s.Log, "charge")
	if s.CardDenied {
		return errors.New("card denied")
	}
	return nil
}

// Buy is the facade: one call, the right order, and the undo on failure.
func (s *Subsystems) Buy(item string, cents int) error {
	s.reserve(item)
	if err := s.charge(cents); err != nil {
		s.release(item)
		return err
	}
	s.ship(item)
	return nil
}
```

#### K-kata 13.10 · DP-10 Flyweight — reference solution

```go
package dp10

// Glyph holds only intrinsic state (the rune); position is extrinsic.
type Glyph struct{ R rune }

// Factory hands out one shared Glyph per rune.
type Factory struct{ pool map[rune]*Glyph }

func (f *Factory) Get(r rune) *Glyph {
	if f.pool == nil {
		f.pool = map[rune]*Glyph{}
	}
	g, ok := f.pool[r]
	if !ok {
		g = &Glyph{R: r}
		f.pool[r] = g
	}
	return g
}

func (f *Factory) Distinct() int { return len(f.pool) }
```

#### K-kata 13.11 · DP-11 Proxy — reference solution

```go
package dp11

// Fetcher is the subject interface.
type Fetcher interface{ Fetch(key string) string }

// Backend is the real subject; it counts its calls.
type Backend struct{ Calls int }

func (b *Backend) Fetch(key string) string { b.Calls++; return "value:" + key }

// CachingProxy has the same interface and controls access to the backend.
type CachingProxy struct {
	Real  Fetcher
	cache map[string]string
}

func (p *CachingProxy) Fetch(key string) string {
	if v, ok := p.cache[key]; ok {
		return v
	}
	if p.cache == nil {
		p.cache = map[string]string{}
	}
	v := p.Real.Fetch(key)
	p.cache[key] = v
	return v
}
```

#### K-kata 13.12 · DP-12 Decorator — reference solution

```go
package dp12

import "strings"

// Handler is the component; decorators take one and return one.
type Handler func(string) string

func Upper(next Handler) Handler {
	return func(s string) string { return strings.ToUpper(next(s)) }
}

func Exclaim(next Handler) Handler {
	return func(s string) string { return next(s) + "!" }
}
```

#### K-kata 13.13 · DP-13 Strategy — reference solution

```go
package dp13

// Pricing is the strategy: a function value is the lightest Go form.
type Pricing func(cents int) int

func Full(c int) int   { return c }
func TenOff(c int) int { return c * 90 / 100 }

// Checkout holds a strategy and never branches on which one it is.
type Checkout struct{ Price Pricing }

func (c Checkout) Total(items []int) int {
	sum := 0
	for _, it := range items {
		sum += c.Price(it)
	}
	return sum
}
```

#### K-kata 13.14 · DP-14 Observer — reference solution

```go
package dp14

// Bus is the subject; observers are functions.
type Bus struct {
	next int
	subs map[int]func(string)
}

// Subscribe registers f and returns the function that removes it.
func (b *Bus) Subscribe(f func(string)) (unsubscribe func()) {
	if b.subs == nil {
		b.subs = map[int]func(string){}
	}
	id := b.next
	b.next++
	b.subs[id] = f
	return func() { delete(b.subs, id) }
}

func (b *Bus) Publish(msg string) {
	for _, f := range b.subs {
		f(msg)
	}
}
```

#### K-kata 13.15 · DP-15 Template Method — reference solution

```go
package dp15

// Steps are the hooks; Run is the fixed skeleton.
type Steps interface {
	Fetch() ([]int, error)
	Transform(int) int
}

// Run fixes the order: fetch, transform each, sum. Callers vary only the steps.
func Run(s Steps) (int, error) {
	xs, err := s.Fetch()
	if err != nil {
		return 0, err
	}
	sum := 0
	for _, x := range xs {
		sum += s.Transform(x)
	}
	return sum, nil
}
```

#### K-kata 13.16 · DP-16 State — reference solution

```go
package dp16

// State decides the next state for an event; unknown events keep the state.
type State interface {
	Name() string
	On(event string) State
}

type Pending struct{}
type Paid struct{}
type Shipped struct{}

func (Pending) Name() string { return "pending" }
func (Paid) Name() string    { return "paid" }
func (Shipped) Name() string { return "shipped" }

func (s Pending) On(e string) State {
	if e == "pay" {
		return Paid{}
	}
	return s
}

func (s Paid) On(e string) State {
	if e == "ship" {
		return Shipped{}
	}
	return s
}

func (s Shipped) On(string) State { return s }
```

#### K-kata 13.17 · DP-17 Command — reference solution

```go
package dp17

// Doc is the receiver the commands act on.
type Doc struct{ Text string }

// Command is a request as an object: it can be stored and undone.
type Command interface {
	Do(*Doc)
	Undo(*Doc)
}

type Append struct{ S string }

func (a Append) Do(d *Doc)   { d.Text += a.S }
func (a Append) Undo(d *Doc) { d.Text = d.Text[:len(d.Text)-len(a.S)] }

// Editor is the invoker; it keeps the history.
type Editor struct {
	Doc     Doc
	history []Command
}

func (e *Editor) Run(c Command) { c.Do(&e.Doc); e.history = append(e.history, c) }

func (e *Editor) Undo() {
	if n := len(e.history); n > 0 {
		e.history[n-1].Undo(&e.Doc)
		e.history = e.history[:n-1]
	}
}
```

#### K-kata 13.18 · DP-18 Chain of Responsibility — reference solution

```go
package dp18

// Handler handles a request or passes it on.
type Handler func(req string) string

// Link wraps next with one check; the chain is built by nesting.
type Link func(next Handler) Handler

func RejectAnonymous(next Handler) Handler {
	return func(req string) string {
		if req == "anon" {
			return "401"
		}
		return next(req)
	}
}

func RejectBlocked(next Handler) Handler {
	return func(req string) string {
		if req == "blocked" {
			return "403"
		}
		return next(req)
	}
}

// Chain applies links so that the first one runs first.
func Chain(final Handler, links ...Link) Handler {
	for i := len(links) - 1; i >= 0; i-- {
		final = links[i](final)
	}
	return final
}
```

#### K-kata 13.19 · DP-19 Mediator — reference solution

```go
package dp19

// Room is the mediator: users talk to it, never to each other.
type Room struct{ users map[string]*User }

type User struct {
	Name  string
	Inbox []string
	room  *Room
}

func (r *Room) Join(name string) *User {
	if r.users == nil {
		r.users = map[string]*User{}
	}
	u := &User{Name: name, room: r}
	r.users[name] = u
	return u
}

func (u *User) Say(msg string) { u.room.broadcast(u.Name, msg) }

func (r *Room) broadcast(from, msg string) {
	for name, u := range r.users {
		if name != from {
			u.Inbox = append(u.Inbox, from+": "+msg)
		}
	}
}
```

#### K-kata 13.20 · DP-20 Iterator — reference solution

```go
package dp20

import "iter"

// Countdown yields n, n-1, ..., 1 and stops early when the consumer stops.
func Countdown(n int) iter.Seq[int] {
	return func(yield func(int) bool) {
		for i := n; i > 0; i-- {
			if !yield(i) {
				return
			}
		}
	}
}
```

#### K-kata 13.21 · DP-21 Memento — reference solution

```go
package dp21

// Memento is opaque outside the package: its field is unexported.
type Memento struct{ text string }

// Editor is the originator.
type Editor struct{ Text string }

func (e *Editor) Save() Memento     { return Memento{text: e.Text} }
func (e *Editor) Restore(m Memento) { e.Text = m.text }
```

#### K-kata 13.22 · DP-22 Visitor — reference solution

```go
package dp22

import "strconv"

// Expr is the element hierarchy; each node accepts a visitor.
type Expr interface{ Accept(Visitor) }

type Num struct{ V int }
type Add struct{ L, R Expr }

func (n Num) Accept(v Visitor) { v.VisitNum(n) }
func (a Add) Accept(v Visitor) { v.VisitAdd(a) }

// Visitor is one operation over the whole hierarchy (double dispatch).
type Visitor interface {
	VisitNum(Num)
	VisitAdd(Add)
}

type Eval struct{ Result int }

func (e *Eval) VisitNum(n Num) { e.Result = n.V }
func (e *Eval) VisitAdd(a Add) {
	var l, r Eval
	a.L.Accept(&l)
	a.R.Accept(&r)
	e.Result = l.Result + r.Result
}

type Print struct{ Out string }

func (p *Print) VisitNum(n Num) { p.Out = strconv.Itoa(n.V) }
func (p *Print) VisitAdd(a Add) {
	var l, r Print
	a.L.Accept(&l)
	a.R.Accept(&r)
	p.Out = "(" + l.Out + " + " + r.Out + ")"
}
```

#### K-kata 13.23 · DP-23 Interpreter — reference solution

```go
package dp23

import (
	"fmt"
	"strings"
)

// Grammar:  expr := term { "AND" term } ;  term := "NOT" term | name
// Eval parses and evaluates in one recursive-descent pass.
func Eval(src string, env map[string]bool) (bool, error) {
	toks := strings.Fields(src)
	pos := 0
	var term func() (bool, error)
	term = func() (bool, error) {
		if pos >= len(toks) {
			return false, fmt.Errorf("unexpected end")
		}
		t := toks[pos]
		pos++
		if t == "NOT" {
			v, err := term()
			return !v, err
		}
		v, ok := env[t]
		if !ok {
			return false, fmt.Errorf("unknown name %q", t)
		}
		return v, nil
	}
	v, err := term()
	for err == nil && pos < len(toks) {
		if toks[pos] != "AND" {
			return false, fmt.Errorf("want AND, got %q", toks[pos])
		}
		pos++
		var r bool
		r, err = term()
		v = v && r
	}
	return v, err
}
```

### K-DPE · exercise bank (§14)

- **DPE-01** — Expected: Adapter per provider SDK (to one `PaymentGateway` interface) plus Strategy or a Factory to choose the provider at run time; Adapter serves Protected Variations (PR-14), and the factory serves DIP (PR-05). · Wrong: "a Facade over all three" — a facade simplifies, it does not unify three interfaces behind one.
- **DPE-02** — Expected: Strategy (an `Exporter` interface with one implementation per format): the format axis grows, and the report structure is fixed. Visitor would suit a varying set of operations over a fixed node hierarchy, which is not the case here. · Wrong: "Visitor, because there are several formats".
- **DPE-03** — Expected: Command for each edit (do and undo) with a history stack; Memento snapshots for operations that are hard to invert. Under memory pressure keep Commands (small deltas) and drop full-state Mementos. · Wrong: "keep a Memento after every keystroke".
- **DPE-04** — Expected: Decorator (or middleware) around `http.RoundTripper`: authentication innermost, next to the network, so every retry carries a fresh token; then the circuit breaker; then retries; then logging outermost, which sees each logical call once. A variant that logs every attempt puts logging inside retries; either order is acceptable if argued. · Wrong: retries outside the circuit breaker, which hammer an open breaker.
- **DPE-05** — Expected: God Object and Shotgun Surgery; `PriceCalculator` (Information Expert on prices), `Inventory` (Expert on stock), `Notifier` (Pure Fabrication plus Protected Variations), `OrderRepository` (Pure Fabrication), and the `Order` aggregate keeping its invariants. · Wrong: "split into four files by method count".
- **DPE-06** — Expected: entities: `Money`, `Order`; use case: `PlaceOrder`; interface adapters: `HTTPHandler`, `PostgresOrderRepository` and `StripeGateway` implementing ports that `PlaceOrder` defines. Every arrow points inward; a use case importing Postgres would violate the rule. · Wrong: placing the repository interface in the infrastructure ring.
- **DPE-07** — Expected: invariants: total = Σ line totals, and the line count is at most 50; methods `AddLine`, `RemoveLine` and `ChangeQuantity`, each checking both invariants; the repository needs `Save(order)` (and `ByID`). · Wrong: a public `Lines` slice that callers append to.
- **DPE-08** — Expected: created → paid, created → cancelled, paid → shipped, paid → refunded (or cancelled with a refund), shipped → refunded (after a return); an illegal event leaves the state unchanged and reports an error. · Wrong: allowing shipped → cancelled.
- **DPE-09** — Expected: steps: book the flight, then the hotel, then the car; compensations in reverse order: cancel the hotel, then the flight. A user-visible failure the compensations cannot hide: a cancellation fee, or a seat that is now gone. · Wrong: "use a distributed lock across the three services".
- **DPE-10** — Expected: a projection "cart contents" updated from events (the read model), with snapshots every N events for rebuilds; rebuild after a bug fix by replaying the log into a new projection and switching reads over. · Wrong: "query the event log on every read".
- **DPE-11** — Expected: tests: shared state leaks between tests, and a fake cannot be injected; production: hidden coupling, initialization-order bugs, and no per-tenant configuration. Replace with constructor injection of one instance created in `main`. · Wrong: "make the Singleton thread-safe" — that fixes one problem and keeps the others.
- **DPE-12** — Expected (rubric): Strategy per channel; Adapter per provider; Chain of Responsibility or Decorator for retries and rate limits; Observer or a queue for fan-out; State for delivery status; the principles named per pattern; one rejected pattern with a reason (for example, Singleton for provider clients, rejected for testability). · Wrong: a pattern list with no principle or rejected alternative.

### K-DPA · academic problems (§15.7)

- **DPA-P1** — Expected: representation invariant 0 ≤ n ≤ len(s); abstraction function: the stack is ⟨s[0], …, s[n−1]⟩, top last. `push(x)` sets s[n] = x (growing s if needed) and n ← n + 1, so 0 ≤ n + 1 ≤ len(s) holds afterwards. · Wrong: an invariant that mentions the abstract stack instead of the concrete fields.
- **DPA-P2** — Expected: `Square.setWidth(w)` must also set the height to w to keep its invariant, so its postcondition contradicts "height unchanged". It does not imply the base postcondition, which breaks the Liskov–Wing rule. · Wrong: "the signatures match, so it is a subtype".
- **DPA-P3** — Expected: object-oriented design: a new variant is 1 new class with 3 methods, and a new operation is 1 method in each of 5 classes (4 old variants edited). Visitor: a new operation is 1 new visitor with 5 methods, and a new variant is 1 new class plus 1 method in each existing visitor (3, or 4 counting the new visitor, edited). · Wrong: "no edits under Visitor".
- **DPA-P4** — Expected: I = 9 / (3 + 9) = 0.75, A = 2 / 10 = 0.2, D = |0.2 + 0.75 − 1| = 0.05: near the main sequence, an unstable and concrete package, which is acceptable for a leaf. · Wrong: I = 3/12 — that swaps afferent and efferent coupling.
- **DPA-P5** — Expected: V(G) = 11 − 9 + 2 = 4, so 4 basis paths. · Wrong: 2 — E − N alone, without the +2P.
- **DPA-P6** — Expected: state = foldl(apply, s₀, [e₁, …, eₙ]). Since foldl(f, s, xs ++ ys) = foldl(f, foldl(f, s, xs), ys), taking the snapshot S = foldl(apply, s₀, [e₁…eₖ]) gives foldl(apply, S, [eₖ₊₁…eₙ]), the same state. This needs `apply` to be deterministic. · Wrong: "snapshots are only an optimization, so no proof is needed".
- **DPA-P7** — Expected: by cases on the first failing step k. If none fails, T₁…Tₙ all run. Otherwise, T₁…Tₖ₋₁ committed, and retrying each compensation until it succeeds runs Cₖ₋₁…C₁. The saga ends in either outcome, and retries need each step to be idempotent. · Wrong: "compensations always succeed" — the proof assumes they eventually succeed when retried.
- **DPA-P8** — Expected: `type Strategy func(Input) Output`; `type Command struct{ Do, Undo func() }`; `func Run(fetch func() ([]T, error), step func(T) U) ([]U, error)`. Classes add named types, several methods with shared state, and discoverable documentation; bare functions lose those. · Wrong: "the function forms cannot be tested".