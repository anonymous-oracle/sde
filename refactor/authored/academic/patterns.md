@@@ named
DP-01: `sync.Once` and `sync.OnceValue` in Go's standard library (one lazy initialization, safe under concurrency); `http.DefaultClient` and `slog.Default()` as process-wide defaults, each replaceable, which is the honest modern form.
DP-02: Java's `Iterable.iterator()`, which GoF itself cites as a factory method (each collection returns its own iterator class); Go's `database/sql/driver.Driver.Open`, which each driver implements to return its own connection type.
DP-03: Java's `javax.xml.parsers.DocumentBuilderFactory` (the installed implementation supplies a matched parser family); Swing's pluggable look-and-feel, where one `LookAndFeel` supplies every widget's UI delegate.
DP-04: Java's `HttpRequest.newBuilder()…build()`; the Google Cloud Java client's `BlobInfo.newBuilder(bucket, name)…build()` `(verify)`; Go's `strings.Builder` (incremental construction; Go usually prefers functional options for configuration, as the Cloud Go clients' `option.With…` values show).
DP-05: Go's `http.Request.Clone(ctx)`, documented as a deep copy, beside `slices.Clone` and `maps.Clone`, which are shallow; JavaScript's `Object.create(proto)`, where objects are built from a prototype object.
DP-06: Go's `http.HandlerFunc`, whose documentation calls it an adapter (an ordinary function becomes an `http.Handler`); Java's `Arrays.asList` (an array seen as a `List`).
DP-07: Go's `database/sql` (the `DB` abstraction) and `database/sql/driver` (the implementation side), which vary independently; `log/slog`'s `Logger` in front of any `Handler`; JDBC in Java.
DP-08: the DOM, where an element and a text node are both `Node`s; Java AWT's `Container`, which is itself a `Component`; Go's `io.MultiReader` and `io.MultiWriter` (many readers or writers seen as one).
DP-09: Go's `http.Get`, one call over `Client`, `Transport` and `Request`; the `gcloud` command line over the Google Cloud APIs.
DP-10: Java's `Integer.valueOf`, which returns cached instances for small values, and `String.intern`; Go's `unique.Make` (Go 1.23 and later), which interns comparable values into shared handles.
DP-11: Go's `httputil.ReverseProxy`; generated gRPC client stubs (a remote proxy: the call looks local, the work is remote); Java's `java.lang.reflect.Proxy`.
DP-12: Go's `bufio.NewReader(r)`, `gzip.NewReader(r)` and `io.LimitReader(r, n)`, each an `io.Reader` wrapping an `io.Reader`; Java's `BufferedInputStream` around any `InputStream`.
DP-13: Go's `slices.SortFunc(s, cmp)` with the comparison passed in; Java's `Comparator`; retry and backoff policies passed to a client.
DP-14: Go's `signal.Notify` (the runtime notifies registered channels); the DOM's `addEventListener`; Kubernetes informers, which call registered event handlers on add, update and delete.
DP-15: Go's `sort.Sort`, a fixed algorithm whose steps (`Len`, `Less`, `Swap`) the caller supplies; Java's `InputStream.read(byte[])` built on the abstract single-byte `read()`, and `AbstractList`.
DP-16: the lexer of Go's `text/template/parse`, where each state is a function that returns the next state (`stateFn`); GoF's own `TCPConnection` example.
DP-17: Go's `exec.Cmd` (a command built, stored and run later); Java's `Runnable`; database migration tools whose steps each carry an up and a down.
DP-18: the Java Servlet `FilterChain`; Go HTTP middleware stacks, where each handler may answer or call the next.
DP-19: the Kubernetes API server, through which controllers coordinate instead of calling each other `(debated)`; an air-traffic control tower, GoF's classic analogy.
DP-20: Go's `iter.Seq` (Go 1.23 and later), `bufio.Scanner` and `sql.Rows`; the Google Cloud Go clients' iterators, which return `iterator.Done` at the end.
DP-21: Go's hash states, which implement `encoding.BinaryMarshaler` (`crypto/sha256`'s digest can be saved and restored mid-stream); the generators of `math/rand/v2`, such as ChaCha8, whose state marshals the same way.
DP-22: Go's `go/ast.Walk` with an `ast.Visitor`; compiler passes over a fixed syntax tree.
DP-23: CEL (the Common Expression Language), evaluated by IAM Conditions and by Kubernetes validation rules; Go's `regexp` and `text/template`, each of which parses a small language into a tree and evaluates it.
@@@ lens
DP-01: Google Cloud client libraries recommend creating one client per process and reusing it (clients hold connection pools and credentials); inject that one client rather than hiding it in a global.
DP-02: each Cloud Go client's `NewClient(ctx, opts...)` chooses the transport and the credentials at run time from Application Default Credentials, so the caller never names a concrete credential type.
DP-03: many generated Cloud Go clients offer a gRPC constructor and a REST constructor for the same API, each producing a matched set of call stubs `(verify)`.
DP-04: Cloud client configuration in Go uses functional options (`option.WithCredentialsFile`, `option.WithEndpoint`), the Go-idiomatic cousin of Builder; Java clients use builders directly.
DP-05: Compute Engine instance templates and machine images: new VMs are copies of a configured prototype.
DP-06: Eventarc delivers events from many sources in the one CloudEvents format, an adapter from each source's native shape to one interface.
DP-07: OpenTelemetry's API is the abstraction, and exporters (Cloud Trace, Cloud Monitoring) are implementations that vary independently of it.
DP-08: the resource hierarchy (organization, folders, projects) is a composite: a folder answers "what is the effective IAM policy" the same way a project does.
DP-09: the Cloud client libraries are a facade over each API's REST and gRPC surfaces; `gcloud` is a facade over many APIs.
DP-10: container image layers in Artifact Registry are content-addressed and stored once, however many images share them (the shared layer is the intrinsic state).
DP-11: the Cloud SQL Auth Proxy (a protection and connection proxy) and Identity-Aware Proxy (an access-control proxy in front of an application).
DP-12: in Go, an `http.RoundTripper` is decorated by OAuth2 token injection and by OpenTelemetry's `otelhttp` transport, each wrapping the next.
DP-13: retry behaviour in the Cloud Go clients is a pluggable policy (for example, the Cloud Storage client's retry options) `(verify)`.
DP-14: Pub/Sub topics and subscriptions, Eventarc triggers and Cloud Storage notifications are Observer at system scale.
DP-15: Apache Beam on Dataflow: the runner owns the skeleton, and a `DoFn` fills in the steps (setup, process each element, finish a bundle, teardown).
DP-16: a Compute Engine VM's lifecycle (provisioning, staging, running, stopping, terminated) is a state machine with legal transitions.
DP-17: Cloud Tasks stores an HTTP request as a task object and runs it later, with retries: a Command queue as a service.
DP-18: a request to an external Application Load Balancer can pass Cloud Armor, then Identity-Aware Proxy, then the backend; any link can reject it.
DP-19: Pub/Sub between services and Workflows as an orchestrator both take on the Mediator role: services talk to them, not to each other.
DP-20: list APIs return pages with a page token, and the Go clients wrap that in an iterator that ends with `iterator.Done`.
DP-21: persistent-disk snapshots and Cloud Storage object versioning keep a restorable state without exposing the internals.
DP-22: few Google Cloud APIs expose Visitor directly; you meet it in tooling that walks a fixed tree, such as policy checks over a Kubernetes manifest or a Terraform plan.
DP-23: CEL expressions in IAM Conditions and in Cloud Armor's custom rules language are interpreted against each request `(verify)`.
@@@ arch-checks
ARCH-01: a request to "show the order total" passes through Presentation, Business Logic and Data Access, and the business layer only forwards the call. Name the cost this shows and one legitimate reason to accept it.
ARCH-02: your core defines a port `OrderRepository`. Name the adapter a test uses and the adapter production uses, and say which of the two the core imports.
ARCH-03: Onion and Hexagonal describe nearly the same structure. What does Onion's ring picture add that "ports and adapters" does not say explicitly?
ARCH-05: in MVP the View is passive. What can you unit-test in MVP without a UI framework that is hard to test in classic MVC?
ARCH-06: an `Order` aggregate holds `OrderLine`s. Another service wants to change one line's quantity directly. What rule does that break, and what must it do instead?
ARCH-07: what does a Unit of Work add on top of several Repositories when one business operation changes three aggregates?
ARCH-08: a class takes its database connection through a setter that tests sometimes forget to call. Which injection style removes that failure, and why?
ARCH-09: when is CQRS not worth it? Give the condition on the read and write models under which one model is enough.
ARCH-10: an event-sourced account has 2 million events. How do you keep reads fast without giving up the event log as the source of truth?
ARCH-11: step 3 of a four-step saga fails after steps 1 and 2 committed in other services. What runs next, and why is that not a rollback in the ACID sense?
ARCH-12: a circuit breaker is open. What happens to a call now, and what event moves it to half-open?
@@@ grasp-checks
PR-06: an `Order` holds its lines and each line's price. Which class should compute the order total under Information Expert, and why not an `OrderService`?
PR-07: an `Order` aggregates `OrderLine`s. Which class should create an `OrderLine`, by Creator, and which of Creator's conditions applies?
PR-08: a web handler validates input, applies the discount rules and saves the order. What should the handler delegate, and to which Controller?
PR-09: class A imports seven other classes to do one job. Name one way to cut its coupling without moving its responsibility.
PR-10: a `Utils` class holds date parsing, e-mail sending and currency rounding. What does low cohesion cost you here, concretely?
PR-11: a `switch` on `paymentType` appears in five places. What does Polymorphism replace it with, and what happens when a new payment type arrives?
PR-12: why is a `Repository` a pure fabrication, and what would be wrong with putting `save()` on the domain entity instead?
PR-13: two services call each other's HTTP APIs directly. Which intermediate object would Indirection add, and what does it buy you?
PR-14: a payment provider's API is predicted to change. Where do you put the stable interface, and which GoF pattern implements the protection?
@@@ ap-checks
AP-01: a `Platform` class has 3,000 lines and imports half the codebase. Which principle is violated at its root, and what is the first extraction you make?
AP-02: a function has seven nested `if`s and three flags that change meaning halfway down. Name the restructuring you apply first.
AP-03: a team uses event sourcing for a settings page with one user. Which anti-pattern is this, and what question should have stopped it?
AP-04: an `Invoice` has only getters and setters, and `InvoiceService` enforces "total equals the sum of the lines". What is wrong, and where should the rule live?
AP-05: every module imports every other and there is no layer rule. Which ARCH item gives the first boundary to draw?
AP-06: a team adds a `Factory` for every class "because patterns are best practice". Which anti-pattern is this, and which test tells you whether a factory is justified?
AP-07: someone adds a Flyweight to a form with 12 fields. What is the evidence you ask for before accepting it?
AP-08: `if status == 3` appears in six files. What replaces the literal, and which principle does the replacement serve?
AP-09: adding one field to "customer" requires edits in eleven files. Which principle, done right, would have kept the change in one place?
AP-10: a `Storage` interface has 30 methods, and most callers use 2. Which principle applies, and what do you split it into?
@@@ gate-line
8. The additions of the academic pass (learner decision of 2026-09-24): the per-item checks come with their items; the section skip-tests (§12) may be taken before a section to skip it; each Go kata (§13) runs once GO-11 and any later Go card its task line names are `taught` (rule 0.4.9), and is done on paper before then; the exercise bank (§14) follows §8; the academic pass (§15) follows the items each block names.
@@@ sections
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

@@@ kata-tasks
DP-01: Write `Config`, a package-level function value that returns the same `*Settings` on every call and counts each load in a package variable `loads`, safe when 50 goroutines call it at once. Needs GO-18 (`sync.OnceValue`).
DP-02: Write the `Store` interface (`Put`, `Get`) and `NewStore(kind string) (Store, error)`, which returns an in-memory store for "memory" and an error for any other kind; the caller never names the concrete type.
DP-03: Write the `Factory` interface (`NewLogger`, `NewMetrics`) and two factories, `LocalFactory` and `CloudFactory`, whose products report the same `Family()`, so a family can never be mixed.
DP-04: Write `NewRequest(url)`, returning a `*Builder` with `WithTimeout`, `WithRetries` and `Build() (Request, error)`; `Build` applies a 30-second default timeout and rejects an empty URL and negative retries.
DP-05: Write `Template.Clone()` so that changing the clone's `Tags` never changes the original's (a deep copy: the clone gets its own backing array).
DP-06: Write `Adapter`, which makes a `LegacyThermometer` (Fahrenheit, `ReadF`) satisfy the `Celsius` interface.
DP-07: Write the `Renderer` interface and two renderers, `SVG` and `Text`, and a `Circle` (a radius, then a renderer) whose `Draw` delegates to whichever renderer it holds, so shapes and renderers vary independently.
DP-08: Write `Node`, `File` and `Dir`, so `Size()` on a directory sums every file below it through the one interface.
DP-09: Write `Subsystems.Buy(item, cents)`, the facade: reserve, then charge, then ship; if the charge fails, release the reservation and return the error. The steps are recorded in `Log`.
DP-10: Write a `Factory` whose `Get(r rune)` returns one shared `*Glyph` per distinct rune, and `Distinct()`, the number of glyphs made.
DP-11: Write `CachingProxy` (field `Real Fetcher`), a `Fetcher` in front of a `Backend` that forwards each key's first request and answers repeats from its cache.
DP-12: Write the decorators `Upper` and `Exclaim`, each `func(Handler) Handler`, so they stack in any order.
DP-13: Write `Pricing` (a function type), the strategies `Full` and `TenOff`, and `Checkout.Total`, which applies the chosen strategy to the sum.
DP-14: Write a `Bus` whose `Subscribe(f)` returns an unsubscribe function and whose `Publish(msg)` calls every current subscriber.
DP-15: Write `Run(s Steps) (int, error)`: fetch, transform each value, and sum, in that fixed order; a fetch error stops the run.
DP-16: Write the states `Pending`, `Paid` and `Shipped`, each with `Name()` and `On(event) State`; "pay" moves pending to paid, "ship" moves paid to shipped, and any other event leaves the state unchanged.
DP-17: Write the `Append` command with `Do` and `Undo`, and an `Editor` whose `Run` executes and records a command and whose `Undo` reverses the last one.
DP-18: Write `Chain(final, links...)` and the links `RejectAnonymous` (answers "401" to the request "anon") and `RejectBlocked` (answers "403" to "blocked"); each link either answers or calls the next, and the first link given runs first.
DP-19: Write a `Room` mediator: `Join(name)` returns a `*User` with an `Inbox`, and `User.Say(msg)` puts "name: msg" in every other user's inbox through the room, never directly.
DP-20: Write `Countdown(n) iter.Seq[int]`, which yields n, n−1, …, 1 and stops at once when the loop breaks. Needs GO-12 (`iter.Seq`).
DP-21: Write an `Editor` with `Save() Memento` and `Restore(Memento)`, where the memento's field is unexported, so no other package can read or change it.
DP-22: Write the visitors `Eval` and `Print` over `Num` and `Add`, so a new operation is a new visitor and no expression type changes.
DP-23: Write `Eval(src, env)` for the grammar `expr := term { "AND" term }`, `term := "NOT" term | name`, returning an error for an unknown name or a malformed expression.
@@@ katas-tail
@@@ s14
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
@@@ s15
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
@@@ appendix-k
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

@@@ keys-tail
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
