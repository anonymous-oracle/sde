# Design Patterns, SOLID & Clean Architecture — A Companion Curriculum
Companion to `Curriculum` ("The Consolidated Cloud Mastery Curriculum"). Sibling to `system-design-primer-companion.md` and `sql-databases-companion.md`.
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

### 0.4 Notation
`PR-nn` SOLID/GRASP principles · `DP-nn` GoF design patterns · `ARCH-nn` architectural styles/DDD/enterprise patterns · `AP-nn` anti-patterns. `[Cr]` = Creational, `[St]` = Structural, `[Bh]` = Behavioral (GoF's own three categories).

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
| **A7 — Software Architecture & APIs** | **Everything in this file**, in order: F-01…04, then PR-01…14, then DP-01…23, then ARCH-01…12 (minus ARCH-09…12 if A9 isn't done yet), then AP-01…10 | Primary landing module — flagged as a curriculum gap during the A5 networking session, filled here |
| A9 Distributed Systems Theory | ARCH-09 (CQRS), ARCH-10 (Event Sourcing), ARCH-11 (Saga), ARCH-12 (Circuit Breaker/Strangler/Bulkhead) — gated behind A9 being complete | These are distributed-systems theory wearing OOP-pattern clothing; A9 owns the consistency/failure theory, this file owns the shape |
| B3 Architecture Patterns & Well-Architected | ARCH-01…04 recalled when discussing HA/DR patterns, one line only | Different axis: B3 is *deployment* resilience, this file is *code* structure — do not conflate (rule 5) |
| C2 Kubernetes | DP-14 Observer (recall) for controller watch-loops; DP-18 Chain of Responsibility (recall) for admission webhooks | The K8s "Operator pattern" itself is taught in C2 natively; cross-reference only |
| C4 CI/CD | ARCH-12's Strangler Fig, recalled as the pattern behind incremental legacy migration via pipelines | — |
| System-design-primer companion | DP-14 Observer ↔ SD-28 Pub/Sub; PR-01 (SRP) ↔ SD-12 microservices; DP-09 Facade ↔ SD-11 reverse proxy | Cross-reference only, not a re-teach |

### 2.1 Overlap register — what is intentionally *not* re-taught here
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
**Formal statement:** bundling data and the operations on that data into a single unit, restricting direct access to that data from outside the unit.
**Why it's not just "private variables":** encapsulation protects an **invariant** — a fact that must always be true about an object's state. A `BankAccount` with a public `balance` field lets any code set `balance = -1000000`, violating "balance is never negative." Routing every state change through a method (`withdraw()`) lets that method *enforce* the invariant.
**Check:** what invariant does hiding `balance` behind `withdraw(amount)` protect, that a public field cannot?

#### F-02 · Abstraction
**Formal statement:** exposing only the essential features of an object relevant to the current context, hiding implementation complexity. Where encapsulation hides *data*, abstraction hides *complexity of behavior*.
**The distinction that trips people up:** encapsulation is a *mechanism* (access control); abstraction is a *design concept* (what to expose at all). A class can be encapsulated (private fields) but a poor abstraction (40 pointless getters/setters that still force callers to think about internals) — conflating the two is a common interview trap.
**Check:** describe a class that is encapsulated but is *not* a good abstraction.

#### F-03 · Inheritance
**Recall from A3**, formalized: inheritance models an **"is-a"** relationship. It serves two distinct purposes often conflated: (1) code reuse and (2) polymorphic substitutability (F-04). Reason (1) alone is a trap — "reuse via inheritance" without an honest is-a relationship is exactly how a hierarchy ends up violating the Liskov Substitution Principle (PR-03).
**The load-bearing rule:** prefer **composition** ("has-a") over **inheritance** ("is-a") whenever the relationship isn't a true taxonomic one. A `Car` *has an* `Engine`; it is not a kind of `Engine`. This single rule is arguably the most consequential piece of OOP wisdom in this file — DP-08 (Decorator) and DP-13 (Strategy) exist specifically as composition-based alternatives to problems people instinctively solve with inheritance.
**Check:** a `Square` inherits from `Rectangle`, overriding `setWidth`/`setHeight` to keep both sides equal. Why does this break substitutability even though "a square is-a rectangle" is mathematically true?

#### F-04 · Polymorphism
**Formal statement:** different objects respond to the same method call in ways appropriate to their own type. Two kinds worth distinguishing: **subtype polymorphism** (a `Dog` and `Cat`, both `Animal`s, implement `makeSound()` differently — what A3 covered) and **parametric polymorphism** (a generic `List<T>` works identically regardless of `T` — the *same* code, not different implementations). GoF-pattern polymorphism is almost always the subtype kind.
**Why it matters for everything after this:** nearly every GoF Behavioral pattern is, mechanically, "define an interface, write several implementations, let the caller hold a reference to the interface and never know which implementation is running." That sentence *is* subtype polymorphism, used as a design tool.
**Check:** in one sentence, why does polymorphism let you add a new `Animal` subclass without modifying code that already calls `makeSound()`? (This is Open/Closed, PR-02, arriving early.)

---

## 4. SOLID (PR-01…PR-05)

Five principles from Robert C. Martin, each naming a specific way a class design rots, and the rule that prevents it.

#### PR-01 · Single Responsibility Principle (SRP)
**Formal statement (Martin's sharper, later version):** a class should have only one reason to change — one *actor* (stakeholder) it answers to.
**Why "does one thing" misleads:** the precise test is **actors**. If an `Employee` class's `calculatePay()` changes when Finance's rules change, and its `save()` changes when the DBA's schema changes, those are two different reasons to change, driven by two different stakeholders — split them, even though both feel "about an employee."
**Cloud-relevant example:** a Cloud Function that validates input, calls a payment API, *and* writes an audit log serves three actors in one function — an audit-format change now risks silently breaking payment logic.
**Check:** a `ReportGenerator` both formats a report as HTML and saves it to Cloud Storage. Name the two actors, and what happens to each responsibility once split.

#### PR-02 · Open/Closed Principle (OCP)
**Formal statement (Bertrand Meyer, 1988):** software entities should be **open for extension, closed for modification** — add new behavior without editing existing, already-tested code.
**The mechanism:** polymorphism (F-04). Instead of `calculateArea(shape)` with an `if/elif` chain on `shape.type`, give every shape an `area()` method behind a common interface — a new shape means a new class, not an edited function.
**Direct link forward:** the formal justification for **DP-13 Strategy** and **DP-15 Template Method**.
**Check:** rewrite this in words as OCP-compliant: `if (shape.type == "circle") {...} else if (shape.type == "square") {...}`. What do you add for a triangle, and what do you never touch?

#### PR-03 · Liskov Substitution Principle (LSP)
**Formal statement (Barbara Liskov, 1987):** if `S` is a subtype of `T`, objects of `T` may be replaced with objects of `S` **without altering program correctness**.
**Precise technical conditions:** a valid override may only **weaken preconditions** and may only **strengthen postconditions**, while preserving the parent's invariants. `Square extends Rectangle` violates this: `setWidth()` on a `Square` has a *stronger, surprising* side effect (height changes too) that breaks the postcondition "only width changed" that callers rely on.
**Why it's the hardest SOLID letter in practice:** it's a *behavioral contract*, not something a compiler fully checks — violations surface only when a subclass is used polymorphically, exactly the situation OCP encourages.
**Check:** a `Bird` base class has `fly()`; `Penguin` overrides it to throw. Which LSP condition is violated, and what's the actual fix (is "is-a" even the right relationship)?

#### PR-04 · Interface Segregation Principle (ISP)
**Formal statement:** no client should be forced to depend on methods it does not use — many small, specific interfaces beat one large, general one.
**Concrete failure:** a `Worker` interface with `work()` and `eat()` forces `RobotWorker` to implement a nonsensical `eat()`. Split into `Workable` and `Eatable`.
**Relation to SRP:** ISP is SRP applied to interfaces — a "fat interface" is an SRP violation one level up.
**Check:** a `Printer` interface has `print()`, `scan()`, `fax()`. A print-only inkjet is forced to implement all three. Redesign it.

#### PR-05 · Dependency Inversion Principle (DIP)
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

**Check:** a `PaymentValidator` exists purely to check payment rules, representing no real-world "thing." Which GRASP principle justifies it, and which one answers "why isn't this just inside `Payment`?"

---

## 6. The GoF Catalog — 23 Design Patterns

Format per pattern: **Intent** (GoF's own line) → **Problem** → **Structure** → **Trade-offs** → **Real-world example**.

### 6.1 Creational [Cr] — DP-01…05: how objects get created, so the system doesn't depend on the concrete classes it instantiates (PR-07 + PR-05 in action).

**DP-01 · Singleton [Cr]**
- **Intent:** ensure a class has only one instance, with a global access point.
- **Problem:** some resources (a single DB connection pool) genuinely must not be duplicated.
- **Structure:** private constructor; a static `getInstance()` returning the same instance every call.
- **Trade-offs `(debated)`:** the most cited pattern that's also an anti-pattern in disguise — it introduces global mutable state and a hidden dependency, bypassing DIP's "explicit dependencies via abstraction." Modern practice increasingly prefers a DI container managing a single instance's *lifetime* instead.
- **Real-world example:** most DI frameworks offer "singleton scope" as a lifetime option rather than a hand-rolled class — industry has largely migrated away from the textbook form.
- **Check:** why does a hand-written Singleton make unit testing harder — what can't you do to it that you could do to an injected object?

**DP-02 · Factory Method [Cr]**
- **Intent:** define an interface for creating an object, letting subclasses decide which class to instantiate.
- **Problem:** a class can't anticipate which concrete class it needs — the decision belongs to a subclass.
- **Structure:** an abstract `Creator` with an abstract `factoryMethod()`; concrete `Creator` subclasses return different concrete `Product` types.
- **Trade-offs:** a class hierarchy purely for creation logic — worth it only when "which concrete class" genuinely varies by context.
- **Real-world example:** `DocumentCreator.createDocument()`; `PDFCreator`/`WordCreator` subclasses each return their own document type.
- **Check:** how is Factory Method a direct application of PR-07 combined with PR-05?

**DP-03 · Abstract Factory [Cr]**
- **Intent:** provide an interface for creating **families** of related objects without specifying concrete classes.
- **Problem:** sometimes you need a whole matched set (a UI toolkit's `Button`+`Checkbox`+`Scrollbar` that must share one visual theme).
- **Structure:** an `AbstractFactory` interface with one creation method per product; concrete factories (`WindowsFactory`, `MacFactory`) each produce the whole matched family.
- **Trade-offs:** adding a new *product* to the family is painful (touches every concrete factory); adding a new *family* is easy.
- **Real-world example:** `PostgresFactory` producing `PostgresConnection`+`PostgresQueryBuilder` together, guaranteed never mixed with MySQL's equivalents.
- **Check:** what breaks specifically if you need to add a `Slider` to every existing theme family?

**DP-04 · Builder [Cr]**
- **Intent:** separate construction of a complex object from its representation, so the same process can build different representations.
- **Problem:** a constructor with 10 optional parameters is unreadable and error-prone (the "telescoping constructor" problem).
- **Structure:** a `Builder` with chained methods (each returning `this`), and a final `build()` assembling the result.
- **Trade-offs:** more code than a plain constructor for simple objects — earns its keep with many optional pieces or a required valid sequence.
- **Real-world example:** cloud SDK request-object construction (`RequestBuilder().setTimeout(30).setRetries(3).build()`).
- **Check:** why is a fluent Builder a better fit than 10 constructor parameters specifically when several are *optional*?

**DP-05 · Prototype [Cr]**
- **Intent:** specify kinds of objects using a prototypical instance, creating new objects by **copying** it.
- **Problem:** building from scratch is expensive, or the exact concrete class isn't known until runtime, but a similar instance already exists.
- **Structure:** a `clone()` method; the caller copies a configured instance instead of re-running expensive setup.
- **Trade-offs:** requires careful **deep vs. shallow copy** handling — a shallow clone sharing a reference can leave two "independent" objects secretly sharing mutable state.
- **Real-world example:** cloning a configured game-character template to spawn instances without re-running expensive initialization.
- **Check:** you clone an object holding a `List<String> tags`. If the clone is shallow, what breaks when the original's list is modified after cloning?

### 6.2 Structural [St] — DP-06…12: composing classes/objects into larger structures while staying flexible (F-03's "favor composition," and PR-14).

**DP-06 · Adapter [St]**
- **Intent:** convert one class's interface into another interface clients expect.
- **Problem:** an existing (often unmodifiable) class's interface doesn't match what your code expects.
- **Structure:** an `Adapter` implementing the target interface, internally delegating to the incompatible adaptee.
- **Trade-offs:** cheap indirection — usually clearly worth it since the alternative is editing code you don't own.
- **Real-world example:** wrapping a legacy XML payment API behind the JSON-based `PaymentGateway` interface your app expects.
- **Check:** how does Adapter differ from Facade (DP-09) in *intent*, though both "wrap" something?

**DP-07 · Bridge [St]**
- **Intent:** decouple an abstraction from its implementation so both can vary independently.
- **Problem:** combining "N abstractions × M implementations" via inheritance alone produces a combinatorial subclass explosion.
- **Structure:** an `Abstraction` holds a reference to an `Implementor` interface (composition) — `Shape` holds a `DrawingAPI`; new shapes and new drawing APIs each grow independently.
- **Trade-offs:** upfront design complexity — worth it only when both axes are genuinely expected to grow independently.
- **Real-world example:** `Notification` (abstraction) bridged to `NotificationChannel` (Email/SMS/Push) — new notification types and channels don't multiply each other.
- **Check:** without Bridge, how many subclasses for 3 shapes × 4 rendering engines? With Bridge?

**DP-08 · Composite [St]**
- **Intent:** compose objects into tree structures for part-whole hierarchies; treat individual objects and compositions uniformly.
- **Problem:** code handling both a single item and a group of items ends up full of `if (isGroup)` checks.
- **Structure:** a common `Component` interface implemented by both `Leaf` and `Composite` (which holds other `Component`s) — calling a method on a folder recursively applies it to everything inside.
- **Trade-offs:** can become overly general — hard to restrict what children a composite may legally contain.
- **Real-world example:** a filesystem, or a UI widget tree.
- **Check:** why does `totalSize()` on a top-level folder work correctly without the caller checking "file or folder" itself?

**DP-09 · Facade [St]**
- **Intent:** provide a unified, higher-level interface to a subsystem, making it easier to use.
- **Problem:** a client using a complex subsystem (compiling: lexer→parser→optimizer→codegen) shouldn't need to orchestrate all four steps.
- **Structure:** one `Facade` exposing a simple method that internally coordinates the subsystem; subsystem classes remain accessible for those needing finer control.
- **Trade-offs:** can become a God Object (AP-01) if it accumulates orchestration logic instead of delegating.
- **Real-world example:** a cloud SDK's high-level client (`.upload(file)`) hiding auth, retries, chunking, and raw HTTP.
- **Check:** does a Facade remove the subsystem's original interfaces, or only add a simpler option alongside them — and why does that matter?

**DP-10 · Flyweight [St]**
- **Intent:** use sharing to support large numbers of fine-grained objects efficiently, separating **intrinsic** (shared) from **extrinsic** (context-specific) state.
- **Problem:** instantiating millions of similar objects wastes memory if each duplicates identical data.
- **Structure:** a `Flyweight` holds only intrinsic state and is shared; extrinsic state is passed in by the client at use-time, never stored in the flyweight.
- **Trade-offs:** passing extrinsic state correctly is easy to get wrong; only worth it at genuinely large object counts.
- **Real-world example:** a text editor sharing one glyph object per unique character+font, tracking position separately per occurrence.
- **Check:** name one intrinsic and one extrinsic piece of state in the text-editor example.

**DP-11 · Proxy [St]**
- **Intent:** provide a surrogate for another object to control access to it.
- **Problem:** you need access control, lazy loading, caching, or logging around an object without changing it or its callers.
- **Structure:** a `Proxy` implementing the same interface as the `RealSubject`, adding logic before/after delegating.
- **Trade-offs:** near-identical structure to Adapter and Decorator — the difference is *intent*: Proxy controls access, Adapter changes an interface, Decorator adds behavior. A genuinely common confusion, worth drilling.
- **Real-world example:** an ORM's lazy-loaded related object hits the database only when a real field is actually accessed.
- **Check:** state the one-word difference in *purpose* for Proxy vs. Adapter vs. Decorator, given near-identical shapes.

**DP-12 · Decorator [St]**
- **Intent:** attach additional responsibilities to an object dynamically — a flexible alternative to subclassing.
- **Problem:** subclassing every combination of optional feature (`CoffeeWithMilkAndSugar…`) produces the same explosion Bridge solves on a different axis.
- **Structure:** `Decorator` implements the same interface as the wrapped `Component`, adding behavior before/after delegating — decorators stack, each adding one responsibility.
- **Trade-offs:** many stacked decorators can be hard to debug; stacking order can silently change behavior.
- **Real-world example:** Java's `BufferedReader(new FileReader(...))` I/O streams.
- **Check:** in one sentence, why does stacking three Decorators avoid the subclass explosion three optional features via inheritance would cause?

### 6.3 Behavioral [Bh] — DP-13…23: algorithms and responsibility/communication between objects.

**DP-13 · Strategy [Bh]**
- **Intent:** define a family of algorithms, encapsulate each, make them interchangeable.
- **Problem:** the direct application of PR-02: an `if/elif` chain picking behavior must be edited for every new behavior.
- **Structure:** a `Strategy` interface; concrete strategies; a `Context` holds a `Strategy` reference, swappable at runtime.
- **Trade-offs:** clients must be aware different strategies exist to choose between them.
- **Real-world example:** a payment processor holding a `PaymentStrategy` chosen at checkout.
- **Check:** what new class do you write to add a payment method, and what existing code stays untouched?

**DP-14 · Observer [Bh]**
- **Intent:** define a one-to-many dependency so when one object (`Subject`) changes, all dependents (`Observer`s) are notified automatically.
- **Problem:** many objects need to react to a state change without the `Subject` being tightly coupled to all of them.
- **Structure:** `Subject` maintains `Observer`s via `attach()`/`detach()`/`notify()`; each `Observer` implements `update()`.
- **Trade-offs:** notification order isn't guaranteed; update cascades are a real bug risk; memory leaks if observers aren't detached.
- **Real-world example:** the OOP-level version of SD-28 (Pub/Sub) — same decoupled fan-out shape, in-process instead of over a network.
- **Check:** what does a `Subject`/`Observer` pair share structurally with a Pub/Sub topic, and what differs about the failure modes?

**DP-15 · Template Method [Bh]**
- **Intent:** define an algorithm's skeleton in a method, deferring some steps to subclasses.
- **Problem:** several classes share an algorithm's shape but need different behavior for one or two steps.
- **Structure:** a base class's `final templateMethod()` calls several steps in fixed order; some are abstract "hooks" subclasses must implement.
- **Trade-offs:** relies on inheritance (heavier coupling than Strategy's composition) — right when the overall structure must stay fixed and only specific steps vary.
- **Real-world example:** a test framework's `setUp()`→`runTest()`→`tearDown()` skeleton.
- **Check:** what varies via composition in Strategy, and what varies via inheritance in Template Method — when would you deliberately pick the latter?

**DP-16 · State [Bh]**
- **Intent:** let an object alter its behavior when its internal state changes — it appears to change class.
- **Problem:** behavior driven by a `status` field scatters `if (status == ...)` across every method.
- **Structure:** a `State` interface; concrete states each implement behavior appropriately, including transitioning the context to the next state.
- **Trade-offs:** near-identical structure to Strategy — the difference is intent: State's implementations actively transition between one another, modeling a state machine.
- **Real-world example:** an `Order` whose `ship()`/`cancel()` behavior legitimately differs by status, illegal transitions simply not offered.
- **Check:** what does a Strategy object *not* do that a State object does?

**DP-17 · Command [Bh]**
- **Intent:** encapsulate a request as an object, enabling queuing, logging, and undo.
- **Problem:** decouple "what triggers an action" from "what performs it," often needing to queue/log/undo.
- **Structure:** a `Command` interface with `execute()` (often `undo()`); an `Invoker` triggers commands without knowing what they do.
- **Trade-offs:** a class per action — worth it specifically for queuing, logging, undo, or invoker/receiver decoupling.
- **Real-world example:** a job queue (Cloud Tasks) is Command at the infrastructure level — a serialized "do this later" object.
- **Check:** why does representing an action as an object make "undo" possible in a way a direct method call cannot?

**DP-18 · Chain of Responsibility [Bh]**
- **Intent:** give more than one object a chance to handle a request; chain receivers and pass the request along until handled.
- **Problem:** a request might need one of several handlers, but the sender shouldn't know which or in what order.
- **Structure:** each `Handler` holds a reference to the next; `handle()` either processes or passes it along.
- **Trade-offs:** no guarantee a request is handled at all — requires an explicit fallback.
- **Real-world example:** HTTP middleware — auth, then logging, then rate limiting, each short-circuiting or forwarding.
- **Check:** what plays "the request" and what plays "each handler" in an HTTP middleware chain?

**DP-19 · Mediator [Bh]**
- **Intent:** encapsulate how a set of objects interact, promoting loose coupling.
- **Problem:** many objects communicating directly with each other produce a tangled many-to-many web.
- **Structure:** a `Mediator` all colleagues talk *to* instead of each other directly.
- **Trade-offs:** the mediator can itself become a God Object — complexity concentrates rather than disappears.
- **Real-world example:** an air traffic control tower (GoF's own example); a chat server mediating clients.
- **Check:** with 6 UI components all reacting to each other, how many direct reference pairs exist without a Mediator, versus with one?

**DP-20 · Iterator [Bh]**
- **Intent:** access elements of an aggregate sequentially without exposing its underlying representation.
- **Problem:** code walking a collection shouldn't need to know if it's an array, list, or tree.
- **Structure:** an `Iterator` interface (`hasNext()`, `next()`); the aggregate returns one via `createIterator()`.
- **Trade-offs:** minimal — this pattern is built directly into most modern languages' syntax now.
- **Real-world example:** every `for...of` construct in a modern language *is* this pattern, already implemented.
- **Check:** why does hiding array-vs-linked-list behind a common iterator let you swap the implementation later without breaking loops over it?

**DP-21 · Memento [Bh]**
- **Intent:** capture and externalize an object's internal state, without violating encapsulation, so it can be restored later.
- **Problem:** implementing undo requires saving past state, but that state is (correctly) private.
- **Structure:** the `Originator` creates a `Memento`; a `Caretaker` stores mementos but never looks inside them.
- **Trade-offs:** storing many full snapshots can be memory-expensive.
- **Real-world example:** a text editor's undo history.
- **Check:** why does a `Caretaker` that "can't look inside" a memento preserve encapsulation in a way `getInternalState()` would not?

**DP-22 · Visitor [Bh]**
- **Intent:** represent an operation over elements of an object structure, adding new operations without changing element classes.
- **Problem:** a stable hierarchy (an AST) keeps needing new operations (print, evaluate, optimize) without editing every node class each time.
- **Structure:** each element implements `accept(visitor)`, calling back `visitor.visitX(this)` — "double dispatch."
- **Trade-offs:** the most conceptually demanding GoF pattern — adding a new *element* type requires touching every visitor, the inverse of Strategy's trade-off.
- **Real-world example:** a compiler walking an AST to type-check, then again to generate code — each a separate Visitor over the same fixed hierarchy.
- **Check:** state precisely what becomes easy to add (operations) and what becomes hard (element types), and why that's the opposite of Strategy.

**DP-23 · Interpreter [Bh]**
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

**ARCH-02 · Hexagonal Architecture (Ports & Adapters)** — Alistair Cockburn. The application core defines **ports** (interfaces expressing what it needs); external technology plugs in via **adapters** implementing them. The core knows nothing about the database, framework, or external APIs. DIP (PR-05) applied at whole-application scale.

**ARCH-03 · Onion Architecture** — Jeffrey Palermo. Concentric rings: Domain Model at center, Domain Services, Application Services, Infrastructure/UI outermost. Dependencies point only inward. Structurally near-identical to Hexagonal; the two names largely describe the same idea from different angles.

**ARCH-04 · Clean Architecture** — Robert C. Martin. Synthesizes Hexagonal/Onion: **Entities** → **Use Cases** → **Interface Adapters** → **Frameworks & Drivers**. **The Dependency Rule:** source dependencies point only inward; an inner circle may know nothing about an outer one, not even its name. Data crossing a boundary must be framework-independent (plain structures), never a leaking ORM entity or HTTP object.
**Why it matters practically:** a Clean Architecture codebase can swap its database, web framework, or UI without touching business logic, because business logic never depended on any of them.
**Check:** why is it a dependency-rule violation for a `UseCase` to import an ORM's `@Entity` annotation onto its own domain object, even for "just one annotation"?

**ARCH-05 · MVC / MVP / MVVM family** — **MVC:** `Model` holds data/logic, `View` renders, `Controller` handles input; the View typically observes the Model (DP-14). **MVP:** the View is passive; a `Presenter` handles all UI logic, updating the View via an interface — more testable than MVC's often-blurry line. **MVVM:** a `ViewModel` exposes state the View **data-binds** to automatically. All three apply PR-08 (Controller) and DP-14 (Observer) at UI-architecture scale.

**ARCH-06 · Domain-Driven Design — tactical building blocks** — Eric Evans.
- **Entity:** defined by identity, not attributes.
- **Value Object:** defined entirely by attributes, no identity, typically immutable.
- **Aggregate:** a cluster of Entities/Value Objects as one consistency boundary, with a single **Aggregate Root** as the only external entry point.
- **Repository:** collection-like access to Aggregates, hiding persistence (PR-12 in action).
- **Domain Event:** something significant that happened, often triggering decoupled side effects (DP-14 at domain scale).
- **Bounded Context:** an explicit boundary within which a model is internally consistent — the same word can mean different things in different contexts, deliberately.

**ARCH-07 · Enterprise patterns (Fowler, PoEAA)** — **Repository:** collection-like interface between domain and data-mapping. **Unit of Work:** tracks changes during a transaction, writes them out atomically. **DTO:** a plain, no-behavior object moving data across a boundary — deliberately not the domain Entity, avoiding structure leakage (connects to Clean Architecture's boundary rule). **Service Layer:** defines an application boundary with use-case-shaped operations.

**ARCH-08 · Dependency Injection & IoC Containers** — recall PR-05: DIP is the principle, DI is the mechanism. **Constructor injection** (generally preferred — dependencies are visible, impossible to forget), **setter injection**, **interface injection**. An **IoC Container** automates wiring at scale, typically at app startup.

**ARCH-09 · CQRS** *(gated behind A9)* — separate the **write** model (Commands, invariant-enforcing) from the **read** model (Queries, often denormalized). Not universal — earns its keep when read/write shapes and scale diverge significantly; the read model may lag the write model, which is SD-05's eventual consistency, reapplied.

**ARCH-10 · Event Sourcing** *(gated behind A9)* — store the sequence of **events** (`OrderCreated`, `ItemAdded`) rather than current state; current state is derived by replaying. Gains a full audit trail and point-in-time reconstruction; costs cheap "current state" queries (hence the common pairing with ARCH-09) and requires periodic **snapshots** to bound replay cost.

**ARCH-11 · Saga Pattern** *(gated behind A9)* — manages a distributed transaction across services (no cross-service ACID, per A9's CAP material) via local transactions each with a **compensating transaction** to undo on failure. **Choreography** (each service reacts to events — Observer-shaped) vs. **orchestration** (one coordinator calls each step — Mediator-shaped).

**ARCH-12 · Resilience micro-patterns** *(gated behind A9)* — **Circuit Breaker:** wraps a remote call; after enough failures, "opens" and fails fast for a cooldown, protecting the caller. **Strangler Fig:** incrementally migrate a legacy system by routing growing traffic shares to new services via a facade/proxy layer until legacy is retired — the formal pattern behind C4's legacy-migration-via-CI/CD question. **Bulkhead:** isolate resources per downstream dependency so one failing dependency can't exhaust resources needed elsewhere.

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
