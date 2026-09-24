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

The main course's §0.4 and §0.5, copied whole so that this companion can be taught on its own terms. The rule numbers stay the main course's (0.4.1…0.4.9, and the five Lab Safety rules), so "main course §0.4.3" and rule 0.4.3 here are the same rule. The **progress ledger** named below is the tutor's running record beside the inline boxes (main course §0.1): each ID's mastery state, the misconception register, the errata list, the recorded overrides and wrong predictions, and the exact resume point. The inline `- [ ]` boxes stay authoritative.

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
- **PR-07 Creator:** class `A` should create `B` if `A` aggregates, records, closely uses, or holds the data to initialize `B` — the formal justification for DP-01…05 (Creational patterns) existing at all.
- **PR-08 Controller:** route system events to a class representing the overall system or use case, not a UI/view class — the formal root of MVC's separation (ARCH-05).
- **PR-09 Low Coupling:** minimize how many other classes a class depends on.
- **PR-10 High Cohesion:** keep a class's responsibilities strongly, purposefully related — SRP's older academic sibling, stated as a design-quality metric.
- **PR-11 Polymorphism:** assign type-varying behavior via polymorphic operations, not type-check chains — the GRASP-level PR-02.
- **PR-12 Pure Fabrication:** when no domain concept cleanly owns a responsibility, invent a class purely for design convenience — the formal justification for utility/service/repository classes.
- **PR-13 Indirection:** assign responsibility to an intermediate object to avoid direct coupling — the formal root of DP-19 (Mediator) and DP-06 (Adapter).
- **PR-14 Protected Variations:** wrap a stable interface around points of predicted instability — nearly the motivation clause behind every GoF Structural pattern.

- [ ] PR-06 · [ ] PR-07 · [ ] PR-08 · [ ] PR-09 · [ ] PR-10 · [ ] PR-11 · [ ] PR-12 · [ ] PR-13 · [ ] PR-14

**Check:** a `PaymentValidator` exists purely to check payment rules, representing no real-world "thing." Which GRASP principle justifies it, and which one answers "why isn't this just inside `Payment`?"

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
- **Check:** why does a hand-written Singleton make unit testing harder — what can't you do to it that you could do to an injected object?

**DP-02 · Factory Method [Cr]**
- [ ] DP-02
- **Intent:** define an interface for creating an object, letting subclasses decide which class to instantiate.
- **Problem:** a class can't anticipate which concrete class it needs — the decision belongs to a subclass.
- **Structure:** an abstract `Creator` with an abstract `factoryMethod()`; concrete `Creator` subclasses return different concrete `Product` types.
- **Trade-offs:** a class hierarchy purely for creation logic — worth it only when "which concrete class" genuinely varies by context.
- **Real-world example:** `DocumentCreator.createDocument()`; `PDFCreator`/`WordCreator` subclasses each return their own document type.
- **Check:** how is Factory Method a direct application of PR-07 combined with PR-05?

**DP-03 · Abstract Factory [Cr]**
- [ ] DP-03
- **Intent:** provide an interface for creating **families** of related objects without specifying concrete classes.
- **Problem:** sometimes you need a whole matched set (a UI toolkit's `Button`+`Checkbox`+`Scrollbar` that must share one visual theme).
- **Structure:** an `AbstractFactory` interface with one creation method per product; concrete factories (`WindowsFactory`, `MacFactory`) each produce the whole matched family.
- **Trade-offs:** adding a new *product* to the family is painful (touches every concrete factory); adding a new *family* is easy.
- **Real-world example:** `PostgresFactory` producing `PostgresConnection`+`PostgresQueryBuilder` together, guaranteed never mixed with MySQL's equivalents.
- **Check:** what breaks specifically if you need to add a `Slider` to every existing theme family?

**DP-04 · Builder [Cr]**
- [ ] DP-04
- **Intent:** separate construction of a complex object from its representation, so the same process can build different representations.
- **Problem:** a constructor with 10 optional parameters is unreadable and error-prone (the "telescoping constructor" problem).
- **Structure:** a `Builder` with chained methods (each returning `this`), and a final `build()` assembling the result.
- **Trade-offs:** more code than a plain constructor for simple objects — earns its keep with many optional pieces or a required valid sequence.
- **Real-world example:** cloud SDK request-object construction (`RequestBuilder().setTimeout(30).setRetries(3).build()`).
- **Check:** why is a fluent Builder a better fit than 10 constructor parameters specifically when several are *optional*?

**DP-05 · Prototype [Cr]**
- [ ] DP-05
- **Intent:** specify kinds of objects using a prototypical instance, creating new objects by **copying** it.
- **Problem:** building from scratch is expensive, or the exact concrete class isn't known until runtime, but a similar instance already exists.
- **Structure:** a `clone()` method; the caller copies a configured instance instead of re-running expensive setup.
- **Trade-offs:** requires careful **deep vs. shallow copy** handling — a shallow clone sharing a reference can leave two "independent" objects secretly sharing mutable state.
- **Real-world example:** cloning a configured game-character template to spawn instances without re-running expensive initialization.
- **Check:** you clone an object holding a `List<String> tags`. If the clone is shallow, what breaks when the original's list is modified after cloning?

### 6.2 Structural [St] — DP-06…12: composing classes/objects into larger structures while staying flexible (F-03's "favor composition," and PR-14).

**DP-06 · Adapter [St]**
- [ ] DP-06
- **Intent:** convert one class's interface into another interface clients expect.
- **Problem:** an existing (often unmodifiable) class's interface doesn't match what your code expects.
- **Structure:** an `Adapter` implementing the target interface, internally delegating to the incompatible adaptee.
- **Trade-offs:** cheap indirection — usually clearly worth it since the alternative is editing code you don't own.
- **Real-world example:** wrapping a legacy XML payment API behind the JSON-based `PaymentGateway` interface your app expects.
- **Check:** how does Adapter differ from Facade (DP-09) in *intent*, though both "wrap" something?

**DP-07 · Bridge [St]**
- [ ] DP-07
- **Intent:** decouple an abstraction from its implementation so both can vary independently.
- **Problem:** combining "N abstractions × M implementations" via inheritance alone produces a combinatorial subclass explosion.
- **Structure:** an `Abstraction` holds a reference to an `Implementor` interface (composition) — `Shape` holds a `DrawingAPI`; new shapes and new drawing APIs each grow independently.
- **Trade-offs:** upfront design complexity — worth it only when both axes are genuinely expected to grow independently.
- **Real-world example:** `Notification` (abstraction) bridged to `NotificationChannel` (Email/SMS/Push) — new notification types and channels don't multiply each other.
- **Check:** without Bridge, how many subclasses for 3 shapes × 4 rendering engines? With Bridge?

**DP-08 · Composite [St]**
- [ ] DP-08
- **Intent:** compose objects into tree structures for part-whole hierarchies; treat individual objects and compositions uniformly.
- **Problem:** code handling both a single item and a group of items ends up full of `if (isGroup)` checks.
- **Structure:** a common `Component` interface implemented by both `Leaf` and `Composite` (which holds other `Component`s) — calling a method on a folder recursively applies it to everything inside.
- **Trade-offs:** can become overly general — hard to restrict what children a composite may legally contain.
- **Real-world example:** a filesystem, or a UI widget tree.
- **Check:** why does `totalSize()` on a top-level folder work correctly without the caller checking "file or folder" itself?

**DP-09 · Facade [St]**
- [ ] DP-09
- **Intent:** provide a unified, higher-level interface to a subsystem, making it easier to use.
- **Problem:** a client using a complex subsystem (compiling: lexer→parser→optimizer→codegen) shouldn't need to orchestrate all four steps.
- **Structure:** one `Facade` exposing a simple method that internally coordinates the subsystem; subsystem classes remain accessible for those needing finer control.
- **Trade-offs:** can become a God Object (AP-01) if it accumulates orchestration logic instead of delegating.
- **Real-world example:** a cloud SDK's high-level client (`.upload(file)`) hiding auth, retries, chunking, and raw HTTP.
- **Check:** does a Facade remove the subsystem's original interfaces, or only add a simpler option alongside them — and why does that matter?

**DP-10 · Flyweight [St]**
- [ ] DP-10
- **Intent:** use sharing to support large numbers of fine-grained objects efficiently, separating **intrinsic** (shared) from **extrinsic** (context-specific) state.
- **Problem:** instantiating millions of similar objects wastes memory if each duplicates identical data.
- **Structure:** a `Flyweight` holds only intrinsic state and is shared; extrinsic state is passed in by the client at use-time, never stored in the flyweight.
- **Trade-offs:** passing extrinsic state correctly is easy to get wrong; only worth it at genuinely large object counts.
- **Real-world example:** a text editor sharing one glyph object per unique character+font, tracking position separately per occurrence.
- **Check:** name one intrinsic and one extrinsic piece of state in the text-editor example.

**DP-11 · Proxy [St]**
- [ ] DP-11
- **Intent:** provide a surrogate for another object to control access to it.
- **Problem:** you need access control, lazy loading, caching, or logging around an object without changing it or its callers.
- **Structure:** a `Proxy` implementing the same interface as the `RealSubject`, adding logic before/after delegating.
- **Trade-offs:** near-identical structure to Adapter and Decorator — the difference is *intent*: Proxy controls access, Adapter changes an interface, Decorator adds behavior. A genuinely common confusion, worth drilling.
- **Real-world example:** an ORM's lazy-loaded related object hits the database only when a real field is actually accessed.
- **Check:** state the one-word difference in *purpose* for Proxy vs. Adapter vs. Decorator, given near-identical shapes.

**DP-12 · Decorator [St]**
- [ ] DP-12
- **Intent:** attach additional responsibilities to an object dynamically — a flexible alternative to subclassing.
- **Problem:** subclassing every combination of optional feature (`CoffeeWithMilkAndSugar…`) produces the same explosion Bridge solves on a different axis.
- **Structure:** `Decorator` implements the same interface as the wrapped `Component`, adding behavior before/after delegating — decorators stack, each adding one responsibility.
- **Trade-offs:** many stacked decorators can be hard to debug; stacking order can silently change behavior.
- **Real-world example:** Java's `BufferedReader(new FileReader(...))` I/O streams.
- **Check:** in one sentence, why does stacking three Decorators avoid the subclass explosion three optional features via inheritance would cause?

### 6.3 Behavioral [Bh] — DP-13…23: algorithms and responsibility/communication between objects.

**DP-13 · Strategy [Bh]**
- [ ] DP-13
- **Intent:** define a family of algorithms, encapsulate each, make them interchangeable.
- **Problem:** the direct application of PR-02: an `if/elif` chain picking behavior must be edited for every new behavior.
- **Structure:** a `Strategy` interface; concrete strategies; a `Context` holds a `Strategy` reference, swappable at runtime.
- **Trade-offs:** clients must be aware different strategies exist to choose between them.
- **Real-world example:** a payment processor holding a `PaymentStrategy` chosen at checkout.
- **Check:** what new class do you write to add a payment method, and what existing code stays untouched?

**DP-14 · Observer [Bh]**
- [ ] DP-14
- **Intent:** define a one-to-many dependency so when one object (`Subject`) changes, all dependents (`Observer`s) are notified automatically.
- **Problem:** many objects need to react to a state change without the `Subject` being tightly coupled to all of them.
- **Structure:** `Subject` maintains `Observer`s via `attach()`/`detach()`/`notify()`; each `Observer` implements `update()`.
- **Trade-offs:** notification order isn't guaranteed; update cascades are a real bug risk; memory leaks if observers aren't detached.
- **Real-world example:** the OOP-level version of SD-28 (Pub/Sub) — same decoupled fan-out shape, in-process instead of over a network.
- **Check:** what does a `Subject`/`Observer` pair share structurally with a Pub/Sub topic, and what differs about the failure modes?

**DP-15 · Template Method [Bh]**
- [ ] DP-15
- **Intent:** define an algorithm's skeleton in a method, deferring some steps to subclasses.
- **Problem:** several classes share an algorithm's shape but need different behavior for one or two steps.
- **Structure:** a base class's `final templateMethod()` calls several steps in fixed order; some are abstract "hooks" subclasses must implement.
- **Trade-offs:** relies on inheritance (heavier coupling than Strategy's composition) — right when the overall structure must stay fixed and only specific steps vary.
- **Real-world example:** a test framework's `setUp()`→`runTest()`→`tearDown()` skeleton.
- **Check:** what varies via composition in Strategy, and what varies via inheritance in Template Method — when would you deliberately pick the latter?

**DP-16 · State [Bh]**
- [ ] DP-16
- **Intent:** let an object alter its behavior when its internal state changes — it appears to change class.
- **Problem:** behavior driven by a `status` field scatters `if (status == ...)` across every method.
- **Structure:** a `State` interface; concrete states each implement behavior appropriately, including transitioning the context to the next state.
- **Trade-offs:** near-identical structure to Strategy — the difference is intent: State's implementations actively transition between one another, modeling a state machine.
- **Real-world example:** an `Order` whose `ship()`/`cancel()` behavior legitimately differs by status, illegal transitions simply not offered.
- **Check:** what does a Strategy object *not* do that a State object does?

**DP-17 · Command [Bh]**
- [ ] DP-17
- **Intent:** encapsulate a request as an object, enabling queuing, logging, and undo.
- **Problem:** decouple "what triggers an action" from "what performs it," often needing to queue/log/undo.
- **Structure:** a `Command` interface with `execute()` (often `undo()`); an `Invoker` triggers commands without knowing what they do.
- **Trade-offs:** a class per action — worth it specifically for queuing, logging, undo, or invoker/receiver decoupling.
- **Real-world example:** a job queue (Cloud Tasks) is Command at the infrastructure level — a serialized "do this later" object.
- **Check:** why does representing an action as an object make "undo" possible in a way a direct method call cannot?

**DP-18 · Chain of Responsibility [Bh]**
- [ ] DP-18
- **Intent:** give more than one object a chance to handle a request; chain receivers and pass the request along until handled.
- **Problem:** a request might need one of several handlers, but the sender shouldn't know which or in what order.
- **Structure:** each `Handler` holds a reference to the next; `handle()` either processes or passes it along.
- **Trade-offs:** no guarantee a request is handled at all — requires an explicit fallback.
- **Real-world example:** HTTP middleware — auth, then logging, then rate limiting, each short-circuiting or forwarding.
- **Check:** what plays "the request" and what plays "each handler" in an HTTP middleware chain?

**DP-19 · Mediator [Bh]**
- [ ] DP-19
- **Intent:** encapsulate how a set of objects interact, promoting loose coupling.
- **Problem:** many objects communicating directly with each other produce a tangled many-to-many web.
- **Structure:** a `Mediator` all colleagues talk *to* instead of each other directly.
- **Trade-offs:** the mediator can itself become a God Object — complexity concentrates rather than disappears.
- **Real-world example:** an air traffic control tower (GoF's own example); a chat server mediating clients.
- **Check:** with 6 UI components all reacting to each other, how many direct reference pairs exist without a Mediator, versus with one?

**DP-20 · Iterator [Bh]**
- [ ] DP-20
- **Intent:** access elements of an aggregate sequentially without exposing its underlying representation.
- **Problem:** code walking a collection shouldn't need to know if it's an array, list, or tree.
- **Structure:** an `Iterator` interface (`hasNext()`, `next()`); the aggregate returns one via `createIterator()`.
- **Trade-offs:** minimal — this pattern is built directly into most modern languages' syntax now.
- **Real-world example:** every `for...of` construct in a modern language *is* this pattern, already implemented.
- **Check:** why does hiding array-vs-linked-list behind a common iterator let you swap the implementation later without breaking loops over it?

**DP-21 · Memento [Bh]**
- [ ] DP-21
- **Intent:** capture and externalize an object's internal state, without violating encapsulation, so it can be restored later.
- **Problem:** implementing undo requires saving past state, but that state is (correctly) private.
- **Structure:** the `Originator` creates a `Memento`; a `Caretaker` stores mementos but never looks inside them.
- **Trade-offs:** storing many full snapshots can be memory-expensive.
- **Real-world example:** a text editor's undo history.
- **Check:** why does a `Caretaker` that "can't look inside" a memento preserve encapsulation in a way `getInternalState()` would not?

**DP-22 · Visitor [Bh]**
- [ ] DP-22
- **Intent:** represent an operation over elements of an object structure, adding new operations without changing element classes.
- **Problem:** a stable hierarchy (an AST) keeps needing new operations (print, evaluate, optimize) without editing every node class each time.
- **Structure:** each element implements `accept(visitor)`, calling back `visitor.visitX(this)` — "double dispatch."
- **Trade-offs:** the most conceptually demanding GoF pattern — adding a new *element* type requires touching every visitor, the inverse of Strategy's trade-off.
- **Real-world example:** a compiler walking an AST to type-check, then again to generate code — each a separate Visitor over the same fixed hierarchy.
- **Check:** state precisely what becomes easy to add (operations) and what becomes hard (element types), and why that's the opposite of Strategy.

**DP-23 · Interpreter [Bh]**
- [ ] DP-23
- **Intent:** given a grammar, define a representation for it plus an interpreter that evaluates sentences in it.
- **Problem:** repeatedly evaluating expressions in a small, well-defined grammar.
- **Structure:** each grammar rule becomes a class implementing `interpret(context)`; a sentence becomes a tree of these (often built with Composite, DP-08).
- **Trade-offs:** GoF itself flags this as suited only to *simple* grammars — the pattern most rarely used verbatim in modern industry code.
- **Real-world example:** a simple rules engine evaluating `age > 18 AND hasLicense`.
- **Check:** what specifically grows unmanageable as grammar rules multiply, per GoF's own warning?

---

## 7. Architecture — Clean/Hexagonal/Onion, DDD, and Enterprise/Microservice Patterns (ARCH-01…12)

Where §6 shaped classes, this section shapes *systems* — often built by applying several §4–§6 tools at once, at scale. Per stitching rule 5: don't confuse with B3's deployment-resilience patterns.

**ARCH-01 · Layered (N-Tier) Architecture** — horizontal layers (Presentation→Business Logic→Data Access), each calling only the layer below. Simple and default for a reason, but strict layering forces pass-through code and lets business logic quietly leak into data-access over time.
- [ ] ARCH-01

**ARCH-02 · Hexagonal Architecture (Ports & Adapters)** — Alistair Cockburn. The application core defines **ports** (interfaces expressing what it needs); external technology plugs in via **adapters** implementing them. The core knows nothing about the database, framework, or external APIs. DIP (PR-05) applied at whole-application scale.
- [ ] ARCH-02

**ARCH-03 · Onion Architecture** — Jeffrey Palermo. Concentric rings: Domain Model at center, Domain Services, Application Services, Infrastructure/UI outermost. Dependencies point only inward. Structurally near-identical to Hexagonal; the two names largely describe the same idea from different angles.
- [ ] ARCH-03

**ARCH-04 · Clean Architecture** — Robert C. Martin. Synthesizes Hexagonal/Onion: **Entities** → **Use Cases** → **Interface Adapters** → **Frameworks & Drivers**. **The Dependency Rule:** source dependencies point only inward; an inner circle may know nothing about an outer one, not even its name. Data crossing a boundary must be framework-independent (plain structures), never a leaking ORM entity or HTTP object.
- [ ] ARCH-04
**Why it matters practically:** a Clean Architecture codebase can swap its database, web framework, or UI without touching business logic, because business logic never depended on any of them.
**Check:** why is it a dependency-rule violation for a `UseCase` to import an ORM's `@Entity` annotation onto its own domain object, even for "just one annotation"?

**ARCH-05 · MVC / MVP / MVVM family** — **MVC:** `Model` holds data/logic, `View` renders, `Controller` handles input; the View typically observes the Model (DP-14). **MVP:** the View is passive; a `Presenter` handles all UI logic, updating the View via an interface — more testable than MVC's often-blurry line. **MVVM:** a `ViewModel` exposes state the View **data-binds** to automatically. All three apply PR-08 (Controller) and DP-14 (Observer) at UI-architecture scale.
- [ ] ARCH-05

**ARCH-06 · Domain-Driven Design — tactical building blocks** — Eric Evans.
- [ ] ARCH-06
- **Entity:** defined by identity, not attributes.
- **Value Object:** defined entirely by attributes, no identity, typically immutable.
- **Aggregate:** a cluster of Entities/Value Objects as one consistency boundary, with a single **Aggregate Root** as the only external entry point.
- **Repository:** collection-like access to Aggregates, hiding persistence (PR-12 in action).
  - *Owner pointer:* Repository's definition is owned by ARCH-07 (Fowler, PoEAA). Here, recall it in one line and add the DDD constraint: one repository per aggregate root.
- **Domain Event:** something significant that happened, often triggering decoupled side effects (DP-14 at domain scale).
- **Bounded Context:** an explicit boundary within which a model is internally consistent — the same word can mean different things in different contexts, deliberately.

**ARCH-07 · Enterprise patterns (Fowler, PoEAA)** — **Repository:** collection-like interface between domain and data-mapping. **Unit of Work:** tracks changes during a transaction, writes them out atomically. **DTO:** a plain, no-behavior object moving data across a boundary — deliberately not the domain Entity, avoiding structure leakage (connects to Clean Architecture's boundary rule). **Service Layer:** defines an application boundary with use-case-shaped operations.
- [ ] ARCH-07

**ARCH-08 · Dependency Injection & IoC Containers** — recall PR-05: DIP is the principle, DI is the mechanism. **Constructor injection** (generally preferred — dependencies are visible, impossible to forget), **setter injection**, **interface injection**. An **IoC Container** automates wiring at scale, typically at app startup.
- [ ] ARCH-08

**ARCH-09 · CQRS** *(gated behind A9)* — separate the **write** model (Commands, invariant-enforcing) from the **read** model (Queries, often denormalized). Not universal — earns its keep when read/write shapes and scale diverge significantly; the read model may lag the write model, which is SD-05's eventual consistency, reapplied.
- [ ] ARCH-09

**ARCH-10 · Event Sourcing** *(gated behind A9)* — store the sequence of **events** (`OrderCreated`, `ItemAdded`) rather than current state; current state is derived by replaying. Gains a full audit trail and point-in-time reconstruction; costs cheap "current state" queries (hence the common pairing with ARCH-09) and requires periodic **snapshots** to bound replay cost.
- [ ] ARCH-10

**ARCH-11 · Saga Pattern** *(gated behind A9)* — manages a distributed transaction across services (no cross-service ACID, per A9's CAP material) via local transactions each with a **compensating transaction** to undo on failure. **Choreography** (each service reacts to events — Observer-shaped) vs. **orchestration** (one coordinator calls each step — Mediator-shaped).
- [ ] ARCH-11

**ARCH-12 · Resilience micro-patterns** *(gated behind A9)* — **Circuit Breaker:** wraps a remote call; after enough failures, "opens" and fails fast for a cooldown, protecting the caller. **Strangler Fig:** incrementally migrate a legacy system by routing growing traffic shares to new services via a facade/proxy layer until legacy is retired — the formal pattern behind C4's legacy-migration-via-CI/CD question. **Bulkhead:** isolate resources per downstream dependency so one failing dependency can't exhaust resources needed elsewhere.
- [ ] ARCH-12

---

## 8. Anti-Patterns (AP-01…10)

Most arise from a *correct* pattern applied poorly, or a principle ignored under deadline pressure.

- **AP-01 God Object:** one class knows/does far too much (maximal SRP violation) — grows because "just add it here" is always the path of least resistance.
- **AP-02 Spaghetti Code:** tangled control flow from ignoring SRP and Low Coupling (PR-09) over many incremental changes.
- **AP-03 Golden Hammer:** applying a familiar pattern to every problem regardless of fit — a reminder every pattern here has a specific problem it solves.
- **AP-04 Anemic Domain Model:** domain objects as pure data bags with all logic in separate "service" classes — violates F-01's actual point (a data bag protects no invariant).
- **AP-05 Big Ball of Mud:** no recognizable architecture — the end state of consistently ignoring ARCH-01…04's boundary discipline.
- **AP-06 Cargo Cult Programming:** copying a pattern's structure without understanding the problem it solves.
- **AP-07 Premature Optimization:** applying a pattern (often Flyweight) for a performance problem that doesn't yet exist.
- **AP-08 Magic Numbers/Strings:** unexplained literals (`if (status == 3)`) — a small-scale Encapsulation failure, since the meaning is hidden nowhere.
- **AP-09 Shotgun Surgery:** one logical change requires editing many unrelated classes — the mirror image of SRP done right.
- **AP-10 Interface Bloat:** the ISP (PR-04) violation restated as a smell — an interface with far more methods than any implementer needs.

- [ ] AP-01 · [ ] AP-02 · [ ] AP-03 · [ ] AP-04 · [ ] AP-05 · [ ] AP-06 · [ ] AP-07 · [ ] AP-08 · [ ] AP-09 · [ ] AP-10

**Check:** a `UserManager` has 40 methods covering auth, email, reports, and DB migrations. Name the anti-pattern and the SOLID violation at its root.

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

---

## 11. Sources & honesty notes

- GoF definitions (§6) adapt Gamma, Helm, Johnson, Vlissides (1994) — "Intent" lines are close paraphrases, since exact phrasing is often what's tested.
- SOLID (§4) synthesizes Martin's writing across *Agile Software Development* (2002) and *Clean Architecture* (2017) — Martin revised SRP's phrasing over time; this file uses the sharper, later "one actor" version.
- GRASP (§5) is from Larman, *Applying UML and Patterns* — less universally taught than SOLID/GoF, included for full theoretical rigor.
- ARCH-02/03 (Hexagonal/Onion) predate and directly informed ARCH-04 (Clean Architecture) — treat the three as one lineage, not three unrelated ideas.
- `(debated)` flags (Singleton, primarily) reflect genuine, ongoing industry disagreement — present both sides, don't adjudicate.