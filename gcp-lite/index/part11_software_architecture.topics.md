# Part 11 · Software Architecture, APIs, Design Patterns & Clean Architecture · TOPIC LIST

Rules and directives for this part: `index/part11_software_architecture.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Software Architecture, APIs, Design Patterns & Clean Architecture

### Architecture fundamentals

- **System decomposition**
  - The client–server model
  - Separating the web layer from the application layer so each scales independently
  - Monoliths, modular monoliths and microservices, and their trade-offs; split decisions made along bounded contexts or business capabilities rather than technical layers, each split justified by a change-rate and team-ownership test and by which transactions it would force across the boundary
  - Schema ownership per service: each service owns its tables and migrations; other services read through its API or its events, never its tables; shared-database coupling as the anti-pattern; the consequences for joins and transactions
  - Service discovery: registries (Consul, etcd, ZooKeeper), health checks, configuration key-value stores
  - Liveness, readiness and startup probes
- **Modularity**
  - Information hiding: decompose by design decisions likely to change (Parnas)
  - Coupling and cohesion; afferent and efferent coupling; instability I = Ce/(Ca + Ce); the stable-dependencies principle
  - Interfaces as contracts
  - Conway's law and the inverse Conway manoeuvre
- **Architectural styles**
  - Layered; pipes and filters; event-based implicit invocation; repository and blackboard; microkernel (plug-in); client–server
  - Service-scale styles: modular monolith, microservices, service-based, space-based
  - Styles as named trade-offs judged against quality-attribute scenarios
- **Communication styles**
  - Synchronous versus asynchronous communication
  - Message queues and event-driven architecture
  - The API gateway's offloaded concerns: TLS, authentication, rate limiting, routing
  - Backend for Frontend: one thin API per client type

### API design

- **RPC**
  - Client and server stubs, marshalling, the communication module
  - Exposing behaviours; tight coupling; debugging and caching difficulties
  - Frameworks: Protocol Buffers and gRPC, Thrift, Avro
  - gRPC security: TLS on the channel with server certificate verification, mutual TLS when the client also presents a certificate, and per-call credentials attached to each RPC as metadata (a bearer token refreshed per call) that the server validates in an interceptor before the handler runs
- **REST**
  - Fielding's constraints: client–server, stateless, cacheable, uniform interface, layered system, optional code on demand
  - Resources identified by URIs; representations; self-descriptive status codes
  - HATEOAS: hypermedia links driven by state
  - Where REST fits poorly: non-hierarchical queries, few verbs, nested round trips, bloated responses
  - Resource-oriented API design guidelines (Google's AIPs)
- **RPC versus REST**
  - Mapping RPC-style operations to resources and verbs
  - RPC internally for performance, REST for public APIs; transcoding one `.proto` to both
- **GraphQL** as a query language that addresses over-fetching and round trips
- **API design theory**
  - Safety and idempotency as algebraic properties, f(f(x)) = f(x); safe methods (GET, HEAD, OPTIONS) change no server state; idempotent methods (GET, HEAD, PUT, DELETE, OPTIONS) leave the same server state when repeated, so a client may retry them after a timeout; POST is neither, so a retried POST needs an idempotency key to avoid a second effect
  - Compatibility rules for evolving APIs and schemas; Hyrum's law
  - Content negotiation: `Accept`, `Accept-Encoding`, `Accept-Language` and `Vary`
  - Machine-readable contracts (OpenAPI, `.proto`) that generate clients, servers and contract tests; consumer-driven contract tests, where each consumer records the requests it sends and the response fields it reads, and the provider's build replays those recorded interactions
  - Pagination, filtering and versioning; deprecation as a timed process: a `Deprecation` header from the date the old version is marked, a `Sunset` header with the removal date, per-client usage metering, and removal only after the sunset date with no recent calls from clients still on it; keyset (seek) pagination on a unique sort key with an opaque cursor, whose cost per page stays flat, against offset pagination, whose cost grows with the rows skipped and whose pages shift when rows are inserted
- Web services and service-oriented architecture: SOAP and WSDL, XML and XML Schema; the enterprise service bus; how SOA relates to REST and microservices

### Object-oriented foundations

- **Encapsulation**: protecting invariants, not just hiding fields
- **Abstraction**: hiding complexity of behaviour; encapsulated but poor abstractions
- **Inheritance**: is-a relationships; reuse versus substitutability; composition over inheritance; the square–rectangle problem
- **Polymorphism**: subtype versus parametric; interfaces with several implementations as the basis of behavioural patterns
- **Abstract data types**: specification by operations; representation invariants and abstraction functions

### Design principles

- **SOLID**
  - Single Responsibility: one actor, one reason to change
  - Open/Closed: extension through polymorphism instead of type switches
  - Liskov Substitution: weaker preconditions, stronger postconditions, preserved invariants
  - Interface Segregation: small client-specific interfaces
  - Dependency Inversion: depend on abstractions; DIP as the principle, dependency injection as the mechanism
- **GRASP**
  - Information Expert, Creator, Controller
  - Low Coupling (the Law of Demeter, Tell Don't Ask) and High Cohesion
  - Polymorphism, Pure Fabrication, Indirection, Protected Variations
- **Everyday rules**
  - DRY as one authoritative representation of each piece of knowledge; the rule of three
  - YAGNI and KISS

### Design by contract and behavioural subtyping

- Preconditions, postconditions and class invariants (Meyer)
- The Liskov–Wing rule: contravariant preconditions, covariant postconditions, invariants, the history constraint
- What type systems can and cannot check about substitutability

### Gang of Four patterns

- **Creational**
  - Singleton: one instance with global access; hidden global state; one-per-process clients injected instead
  - Factory Method: subclasses choose the concrete product
  - Abstract Factory: families of related products
  - Builder: step-by-step construction; functional options as an alternative; a director that orders the builder's steps, a fluent builder whose methods return the receiver, and a build step that checks the invariants before returning the product; in Go, functional options (a variadic list of functions that each set one field) as the idiomatic builder for optional arguments
  - Prototype: creation by cloning
- **Structural**
  - Adapter: converting one interface to another
  - Bridge: separating an abstraction from its implementation
  - Composite: tree structures treated uniformly
  - Facade: one simple interface over a subsystem
  - Flyweight: sharing intrinsic state
  - Proxy: a stand-in that controls access (remote, virtual, protection)
  - Decorator: adding behaviour by wrapping; middleware
- **Behavioural**
  - Strategy: interchangeable algorithms
  - Observer: publish–subscribe notification
  - Template Method: an algorithm skeleton with varying steps
  - State: behaviour that changes with internal state; state machines
  - Command: requests as objects; undo and queues
  - Chain of Responsibility: passing a request along handlers
  - Mediator: centralising communication between colleagues
  - Iterator: sequential access without exposing representation
  - Memento: capturing and restoring state
  - Visitor: new operations over a fixed structure
  - Interpreter: a grammar evaluated by a class hierarchy
- **Patterns and language features**
  - Patterns that become functions, closures, generators, folds or composition in functional languages (Norvig's observation)
  - The expression problem: open versus closed sums; Visitor versus Strategy; object algebras, type classes and tagless final (named)
  - The design decision about which axis of change to protect as the essence of a pattern

### Application architecture

- Layered (n-tier) architecture and pass-through costs
- Hexagonal architecture: ports and adapters
- Onion architecture
- Clean Architecture: entities, use cases, interface adapters, frameworks and drivers; the dependency rule; framework-free boundary data
- MVC, MVP and MVVM
- Dependency injection: constructor, setter and interface injection; IoC containers
- Enterprise patterns: Repository, Unit of Work, Data Transfer Object, Service Layer; Repository as a collection-like interface with add, get and remove operations over one aggregate root, with the query language hidden inside one adapter; Unit of Work as the object that records changed aggregates during a use case and commits them in one transaction at its end; Data Transfer Object as a plain carrier of one request's data across a process boundary, so the remote call moves one object rather than many fields; Remote Facade as one coarse-grained method per remote use case that fills a DTO, so one network round trip replaces many fine-grained calls
- Transaction script, active record and data mapper: a transaction script as one procedure per use case over plain data, simple and fast for small domains but repeating the rules in each procedure; active record as one class per table holding both the state and its persistence methods, so the object's schema binds it to the database; a data mapper as a separate layer that moves data between domain objects and tables, keeping the domain model free of persistence concerns at the cost of building and maintaining the mapping

### Domain-driven design

- Entities, value objects and aggregates with a single root
- One repository per aggregate root
- Domain events
- Bounded contexts and anti-corruption layers
- Aggregates as consistency boundaries: one aggregate per transaction; eventual consistency across aggregates

### Distributed application patterns

- CQRS: separate write and read models; when one model is enough
- Event sourcing: state as a left fold over events; deterministic replay; snapshots and projections; projection lag as the time between an event's commit and its appearance in the read model, measured as an SLI; rebuilding a projection by replaying the log from the start into a new table and switching reads when it catches up; projection handlers idempotent, so a redelivered event leaves the read model unchanged
- Resilience patterns: circuit breaker (closed, open, half-open), bulkhead, graceful degradation, retry with exponential backoff and jitter within a retry budget; resilient serving of machine-learning models: a timeout on each prediction call with a fallback to a cached prediction, a simpler model or a rule, and load shedding of low-priority requests when the model server's queue is full
- Strangler fig migration behind a facade

### Anti-patterns

- God Object; Spaghetti Code; Big Ball of Mud
- Golden Hammer; Cargo Cult Programming
- Anemic Domain Model
- Premature Optimization
- Magic numbers and strings
- Shotgun Surgery
- Interface Bloat
- Refactoring as behaviour-preserving steps: extract method and extract class, replace a type switch with polymorphism, introduce a parameter object, each step run under a test that pins the current behaviour before the change; the wider catalogue of named moves: rename, move method, inline method, encapsulate field, replace a magic number with a named constant, each answering the smell it names

### Quality attributes and evaluation

- Quality-attribute scenarios: source, stimulus, artifact, environment, response, response measure
- Tactics for availability, performance, modifiability, security and testability; availability tactics (heartbeat, active and passive redundancy, rollback, exception handling with retry); performance tactics (reduce resource demand by caching and batching, manage contention by concurrency and prioritization); modifiability tactics (encapsulate, split, abstract common services, defer binding); each tactic chosen to meet one scenario's response measure and recorded with its cost
- The Architecture Tradeoff Analysis Method: utility trees, sensitivity and trade-off points, risks
- Design-quality metrics: the Chidamber–Kemerer suite (WMC, DIT, NOC, CBO, RFC, LCOM); Martin's package metrics (abstractness, distance from the main sequence D = |A + I − 1|, the Stable Abstractions Principle); cyclomatic complexity V(G) = E − N + 2P
- Technical debt as a metaphor and its limits; estimation error; the evidence on code review
- Architectural drivers: the few requirements (quality-attribute scenarios, hard constraints and the use cases they serve) that most shape the architecture; elicited, ranked by business value and by difficulty, and used to choose the style and tactics before any structure is drawn

### Architecture documentation

- Architecture views and the C4 model
- Mermaid diagram notation: flowchart, sequence, class and state diagrams written as text in version control and rendered by the host; C4 context and container diagrams in the same notation; diagrams kept beside the decision records they support
- Sequence diagrams: lifelines, synchronous and asynchronous messages, activation bars, alternative and loop fragments; used to check an LLD contract against its failure and retry paths
- Architecture decision records
- High-level and low-level design documents and the contract between them; the LLD method in order: name the entities and their invariants, list each class's operations with preconditions, draw each stateful class as a state machine, mark the transaction scope of every operation, then draw the sequence diagram of its failure and retry paths
- Non-functional requirement tables; each NFR written as a quality-attribute scenario with a measure, and elicited by asking stakeholders for numbers (peak requests per second, the latency at the 99th percentile, the availability target, data retention), with words such as fast or secure rewritten as measurable responses; functional requirements written as use cases with an actor, a goal, the main steps and the failure paths
- UML class-diagram notation: inheritance, realization, composition, aggregation, association, dependency
- Architecture reconstruction: recovering the as-built architecture from the code and runtime evidence (package dependency extraction, call and data-flow graphs, deployment manifests, traces), comparing it with the intended design as a gap list, and ranking each gap by its effect on the quality-attribute scenarios

### Formal methods

- State machines as specifications
- Safety versus liveness properties; temporal logic
- Model checking by exhaustive state enumeration (a lock, two-phase commit)
- TLA+ as used in industry to find design bugs before code

### Software testing at depth

- Test oracles, equivalence partitioning and boundary values
- Example-based versus property-based testing
- Fuzzing theory: coverage guidance and corpora
- Mutation testing
- Static analysis

### Exercises

- Object-oriented designs: a hash map, an LRU cache, a call center with escalation, a deck of cards and blackjack, a parking lot, an online chat with friends and group chats; for each, the requirements, the entities and their invariants, the operations with their preconditions, and the pattern the design forces: a hash map with separate chaining and a resize at a load factor, with the get, put and remove contracts; a call center with an escalation chain of responders and a queue of waiting calls; a deck of cards with a shuffle and deal, and blackjack as a round state machine with a hand-scoring strategy; a parking lot with spot allocation by vehicle size and a ticket lifecycle from entry to exit
- From scratch in Go: one implementation per GoF pattern
- From scratch: a dependency-injection container; an in-process event bus; a circuit breaker, retry with jittered backoff and a bulkhead
- Pattern selection: multiple payment providers, pluggable export formats, unlimited undo, a switchable HTTP client chain, refactoring a 40-method manager
- A payment domain placed into Clean Architecture rings; an order aggregate's invariants; an order lifecycle with the State pattern
- A booking saga with compensations; an event-sourced cart with CQRS and snapshots
- Singleton configuration and database objects critiqued and refactored
- A gRPC service from a `.proto`; a REST API with ETags, idempotent PUT and HATEOAS links; an OpenAPI contract imported into an API gateway; a combo service that serves one `.proto` both as gRPC and as REST through transcoding, with one error mapping and one test suite run against both protocols
- Two services calling each other with authenticated invocation
- A notification platform with preferences, retries, rate limits and provider fallback
- A small protocol model-checked; property-based and mutation tests on a domain module
- From scratch: one small order use case written three ways, as a transaction script, an active record and a data mapper over the same storage interface; then a short note on which later change (a new business rule, a second table, a test without a database) each one makes cheap or costly
- **Reasoning drills**
  - Name the binding quality attribute from a requirements list before choosing a style
  - Predict which modules a changed requirement will touch, then make the change and compare
  - Re-solve a design in a second architectural style and compare failure modes and cost
  - Prove that a subtype satisfies the Liskov rule or construct the counterexample
  - Reconstruct the as-built structure of a small repository from its imports and deployment files, then list each gap against the intended design
