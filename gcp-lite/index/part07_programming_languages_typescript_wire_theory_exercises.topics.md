# Part 07 · Programming Languages & Language Theory (part 3 of 3) · TOPIC LIST

Rules and directives for this part: `index/part07_programming_languages_typescript_wire_theory_exercises.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Programming Languages & Language Theory (part 3 of 3)

### TypeScript, Node and the web client

- **TypeScript and Node**
  - Erased types; structural typing; `strict` mode; contrasts: Java's nominal classes with erased generics, C#'s nominal types with generics kept at run time, and Python type hints that a separate checker such as mypy reads while the interpreter ignores them
  - Union and literal types and narrowing; `unknown` versus `any`; generics; a union is narrowed inside each branch by `typeof`, `in`, equality with a literal or a discriminant field, so the checker knows the member type there; `unknown` accepts any value but must be narrowed before use, while `any` switches checking off and lets errors pass silently; a generic function declares a type parameter, as in `function first<T>(xs: T[]): T`, that the checker instantiates at each call and that is erased at run time
  - ES modules versus CommonJS: ES modules are static `import` and `export` declarations whose bindings are resolved before the file runs and stay live, while CommonJS `require` is an ordinary function call that returns the exports object as it stands at that moment, so a value copied out of it does not update later; Node chooses the format by file extension (`.mjs` or `.cjs`) or by the `type` field of `package.json`, and loading one format from the other is a common source of errors
  - The Node event loop; blocking the loop with CPU work and moving it off; Node runs JavaScript on one thread, and the loop dispatches callbacks from timers, completed network and file operations and resolved promises, so a synchronous loop of CPU work (a large JSON parse, a hash over a big buffer) delays every other request until it returns; move that work to `worker_threads` or a separate process, and measure the damage as event-loop delay
  - Promises, `async`/`await`; `Promise.all` failure semantics; `AbortController`; `Promise.all` rejects as soon as one input rejects, and the other promises keep running because it does not cancel them; `Promise.allSettled` waits for every input and reports each outcome; an `async` function returns a promise and `await` suspends the function until that promise settles; `AbortController` produces an `AbortSignal` that fetch and timers accept, and aborting it rejects the pending operation so the caller's `catch` can clean up
  - npm, `package.json`, lockfiles, `npx`; `tsc`, `node --test` or Vitest, ESLint; `package.json` declares dependency ranges and scripts, the lockfile pins the exact resolved versions, and `npm ci` installs exactly what the lockfile records, so a clean checkout reproduces the same tree; `npx` runs a package's binary without a global install; `tsc --noEmit` type-checks without writing output; `node --test` is Node's built-in runner, and Vitest is a faster alternative with the same test shape; ESLint reports lint rules over the source
- **Runtime validation and a minimal React client**
  - "Parse, don't trust": a hand-written validator, then Zod (`safeParse`, error paths, inferred types, JSON Schema export)
  - React components as functions of state; `useState` and `useEffect`; rendering a stream as it arrives; React Router's route table with nested outlets for client-side pages, and Jest tests that render a component and query its output, the same test shape as Vitest
  - Keeping API keys server-side behind a server route; the split of roles in which the browser client renders state and sends user actions, while the server holds credentials, checks authentication and validates input, and the request and response shapes between them are a schema that both sides parse; API key lifecycle: a key is generated from `crypto/rand` with at least 256 bits of entropy, shown once, and stored as a SHA-256 hash (a fast hash is fine for a high-entropy key, unlike a password) with a short prefix for lookup, compared in constant time; rotation by issuing a second active key, moving clients over, and then revoking the old one; keys carry scopes and an expiry

### Java and the JVM

- **Language and object model**: classes, interfaces and abstract classes; inheritance and polymorphism; packages and access modifiers; checked and unchecked exceptions; compilation to bytecode and execution on the JVM
- **Strings and utilities**: `String` immutability and the string pool; `StringBuilder` versus the synchronized `StringBuffer`; `Scanner`, `Random`, `Arrays`, `Objects` and `Optional`
- **Generics**: generic classes and methods; bounded type parameters and wildcards; type erasure and its consequences
- **Collections Framework**
  - `List`, `Set`, `Map` and `Queue`; `ArrayList` versus `LinkedList`; `HashMap`, `LinkedHashMap` and `TreeMap`
  - Legacy classes (`Vector`, `Hashtable`, `Stack`) and why they are avoided: they are synchronized on every method, so each call takes a lock even in single-threaded code; `Hashtable` also rejects null keys and values; `Stack` extends `Vector`, so it inherits index access and insertion at arbitrary positions, which a stack should not offer; `ArrayList`, `HashMap` and `ArrayDeque` are unsynchronized and faster, and shared structures are wrapped in `Collections` synchronized views or replaced by `java.util.concurrent` types
  - Cursors: `Iterator` and `ListIterator`; fail-fast iteration; `Comparable` versus `Comparator`
- **I/O**: byte streams and character streams; buffering; file I/O; `RandomAccessFile`; serialization; `java.nio` channels and paths

### Wire formats

- **JSON**: the RFC 8259 grammar; no comments or trailing commas; unbounded numbers and 64-bit IDs in JavaScript; duplicate keys; a recursive-descent parser by hand
- **JSON Schema**: `type`, `properties`, `required`, `enum`, `additionalProperties`, `$ref`; schemas as contracts for tool inputs and structured outputs; constrained decoding: at each generation step the model's logits are masked so that only tokens that keep the output a prefix of some string in the target language (defined by a JSON Schema or a regular expression) keep nonzero probability; the schema is compiled to an automaton, the allowed-token set is computed per automaton state, and the output is valid by construction, though still in need of semantic checks; the cost is one mask computed over the vocabulary per generated token
- **JSON-RPC 2.0**: requests and notifications, `result` versus `error`, batches, reserved error codes −32700 to −32603
- **Server-Sent Events**: `text/event-stream`, `event:`, `data:`, `id:`, `retry:`, comments; incremental parsing across chunk boundaries; reconnection with `Last-Event-ID`; buffering proxies that break streaming
- **XML**: elements, attributes, namespaces and well-formedness rules; the declared encoding and character escaping; struct-tag marshalling and unmarshalling with `encoding/xml`

### Language theory

- **Program semantics**
  - Values versus references, mutability and aliasing: a variable holding a reference and another holding the same reference name one object, so a change made through either is seen through both; copying an immutable value creates no observable alias; `==` on references tests identity (the same object), not equality of contents, so a mutable value passed around is shared rather than duplicated
  - Scope, closures and lexical environments: scope is the region where a name is visible; lexical scoping resolves a name by the nesting of the source text, so a function body sees the bindings of the place where it was written, not where it is called; a closure pairs a function's code with the environment it captured, which keeps those variables alive after the enclosing call returns; in a loop, closures share one binding unless each iteration creates a fresh one, which some languages do and others do not
  - Evaluation order; call by value, call by sharing, explicit pointers; evaluation order is the order in which operands and calls run, which some languages fix (Python and Java evaluate arguments left to right) and others leave to the compiler (C leaves the order of many operands unspecified); call by value copies the argument, so the callee cannot rebind the caller's variable; call by sharing, as in Python and in Java for objects, passes a copy of the reference, so the callee can mutate the object the caller sees but cannot rebind the caller's name; explicit pointers pass an address that the callee can dereference and assign through
- **Recursion and correctness**
  - Base cases and decreasing measures; correctness and termination by induction; a recursive definition is correct when its base cases return the right answer and each recursive call is on a smaller input under a measure that decreases in a well-founded order, usually a natural number; induction on that measure proves both that the result is correct and that the recursion stops; a missing base case, or a call whose argument does not shrink, makes the recursion unbounded and exhausts the stack
  - Recursion versus iteration; tail calls; stack depth limits; each call needs a stack frame, so recursion depth is bounded by the stack; a tail call is one whose result is returned unchanged, and an implementation with tail-call elimination can reuse the frame and run in constant stack space, which turns the recursion into a loop; languages differ, since some guarantee tail calls while Go does not, and CPython's default recursion limit of about 1000 frames stops deep recursion early, so a deep recursion must be rewritten as a loop or given more stack
- **Type systems**
  - Static versus dynamic, strong versus weak, nominal versus structural typing: static checking happens before the program runs and dynamic checking at run time; strong typing refuses operations on mismatched types (Python's `'1' + 1` raises a TypeError), while weak typing converts silently (JavaScript's `'1' + 1` gives `'11'`), and both are points on a spectrum; nominal typing makes two types compatible only when declared so, as Java's `implements` does, while structural typing makes a type match any type with the required shape, as Go interfaces do
  - Parametric versus subtype polymorphism; variance; parametric polymorphism gives one implementation that works for all types, as in a Go generic `Map` function with type parameters T and U, while subtype polymorphism dispatches on the run-time type through an interface or a subclass; variance says how a generic type relates to its parameters: a read-only container may be covariant, so that `List<Cat>` is a subtype of `List<Animal>`, but a container that is written must be invariant; Java arrays are covariant, so a store can fail at run time with `ArrayStoreException`
  - Type soundness: progress and preservation; progress says a well-typed closed term is either a value or can take a step, and preservation says a step keeps the term's type; together they state that a well-typed program never reaches a stuck state, the formal content of the slogan that well-typed programs do not go wrong; each proof is by induction on the typing or evaluation derivation
  - Open versus closed sum types; the expression problem; Featherweight Go; a closed sum type lists its variants in one place, so a function over it can be checked for exhaustiveness, but adding a variant means editing every function that matches on it; an open family of interface implementations makes adding a new variant easy and adding a new operation hard, and no choice avoids both costs, which is the expression problem; Featherweight Go is a small formal calculus of Go's structs, methods and interfaces, in which the soundness of its type system is proved
- **Specification and testing theory**
  - Preconditions, postconditions, loop invariants; Hoare triples and the assignment rule
  - Why line coverage does not prove correctness: line coverage records only which statements ran, so a test that executes every line can still miss a wrong comparison, a boundary value or an interleaving of concurrent operations; branch and condition coverage are stronger, and mutation testing, which plants small faults and checks that some test fails for each, measures whether the tests detect faults at all
  - Benchmarks as samples with confidence intervals: a benchmark run is a sample of noisy timings, so report a central value with a confidence interval over repeated runs, and compare two versions with a test that accounts for that spread (Go's `benchstat` does this) rather than with two single numbers; warm-up, garbage collection and CPU frequency changes move results, so the measurement must control for them
- **Compilers and interpreters**
  - Lexing, parsing, abstract syntax trees, type checking; lexing as a DFA built from the token regular expressions by Thompson's construction and subset construction, with longest match and rule priority; recursive-descent and LR parsing of the grammar, and precedence climbing for binary operators; type checking by unification for Hindley–Milner inference, where type variables are solved from equations, with the occurs check rejecting a variable that would contain itself
  - Grammars in EBNF; context-free grammars; Go's semicolon-insertion rule; `go/ast` and `go/parser`
  - Intermediate representations and SSA; optimisation; code generation; linking; SSA form in which each variable has a single definition, with φ-functions placed on the iterated dominance frontier of each definition site and dominator trees computed by an iterative dataflow algorithm; dataflow analysis as a fixed point over a lattice, with live variables computed backwards and reaching definitions forwards
  - Register allocation by graph colouring: build the interference graph from live ranges (two variables interfere when both are live at one point), colour it with k colours for k machine registers by simplify-and-select (remove a node of degree below k, push it on a stack, and pop to colour it), spilling to memory when no colour is free; graph colouring with k colours is NP-complete, so compilers use this heuristic and optimistic colouring rather than an exact solver
  - Linear-scan register allocation: sort live intervals by start point, expire the intervals that end before the current point, assign a free register, or spill the interval that ends furthest away; O(n log n) time with the sort dominating, simpler than colouring, at the cost of coarser live ranges
  - Interpreters and the Interpreter pattern: an interpreter evaluates a syntax tree directly, with a case for each node type that recurses into its children and an environment that maps names to values; the Interpreter pattern gives each grammar rule its own class with an `interpret` method that composes the same way; it is simple and easy to extend, but each node costs a dispatch and a call, which is why production systems compile to bytecode or machine code
- **Regular languages and the pumping lemma**
  - The pumping lemma as a necessary condition for regularity, proved by the pigeonhole principle on a DFA's states; used to refute regularity
  - Closure under union, intersection, complement, concatenation and star; decidable membership, emptiness and equivalence
- **Closure and decision properties of context-free languages**
  - Closure under union, concatenation, star and reversal, but not under intersection or complement; closure under intersection with a regular language
  - The pumping lemma for context-free languages; decidable membership (CYK parsing) and emptiness; undecidable equivalence and universality
  - Pushdown automata: a finite control with one stack, where each transition reads an input symbol and pops and pushes stack symbols; acceptance by final state or by empty stack, with the same language class as context-free grammars
- **Concurrency theory in Go**
  - Hoare's CSP; rendezvous and bounded queues; guarded choice; in Hoare's communicating sequential processes, processes interact only by synchronous message passing: an unbuffered send blocks until a receive takes the value, a rendezvous, and a channel of capacity n lets up to n sends proceed before a send blocks; guarded choice offers several communications and proceeds with one whose guard is ready, nondeterministically when more than one is ready, as Go's `select` does
  - Deadlock as a cycle in the wait-for graph
  - Herlihy's consensus hierarchy and why compare-and-swap exists: a primitive's consensus number is the largest number of processes for which it can solve wait-free consensus; read-write registers have consensus number 1, test-and-set and fetch-and-add have 2, and compare-and-swap has infinite consensus number, which is why it is universal, able to build a wait-free version of any object; compare-and-swap writes a new value only if the current value still equals the expected one, the basis of lock-free retry loops
  - Work stealing: expected time T₁/P + O(T∞); speed-up bounded by min(P, T₁/T∞); each worker keeps a double-ended queue of ready tasks, pushes and pops at its own end, and an idle worker steals from the other end of a randomly chosen victim, so steals are rare and move large pieces of work; with total work T₁ and critical path T∞, the expected running time on P workers is T₁/P + O(T∞), and the speed-up is bounded by both P and the parallelism T₁/T∞
- **Memory-management theory**
  - Conservative escape analysis: a compiler decides whether a value can outlive its function by tracking whether it is returned, stored in the heap, or passed to a callee it cannot see; it keeps the value in the stack frame only when it can prove that it does not escape, and conservative means that any doubt counts as an escape, so the analysis may miss a stack allocation but never frees a value still in use; the decisions can be inspected with the compiler's diagnostic flags
  - Tri-colour marking and the strong tri-colour invariant; Dijkstra insertion and Yuasa deletion write barriers
  - The GC pacer: the controller that decides when a collection starts, so that marking finishes before the heap reaches its target; it trades CPU time spent in the collector against heap growth; Go's pacer sets the trigger from the live heap after the previous cycle and the `GOGC` percentage, and `GOMEMLIMIT` is a soft ceiling on total memory that makes collection more frequent as the program nears it
- **The language design space**
  - Manual memory versus garbage collection versus ownership: manual management (`malloc` and `free` in C) is fast but allows use-after-free and double free; tracing garbage collection finds unreachable objects at run time, trading pause time and memory headroom for safety; reference counting, as in CPython, frees an object when its count reaches zero and needs a separate cycle collector for cycles; ownership, as in Rust, gives each value one owner that frees it when the owner's scope ends, checked at compile time, so no run-time collector is needed
  - Exceptions versus error values; threads and locks versus actors versus CSP; exceptions unwind the stack to a handler, so the error path is invisible at the call site, while error values make each failure an ordinary return value that the caller must examine, as Go's `error` does, which is explicit but verbose; for concurrency, locks guard shared memory, which makes data races the typical bug; actors own their state and communicate through mailboxes, where a mailbox that overflows or is never drained is the risk; CSP passes values over named channels, where a cycle of blocked sends and receives is the deadlock
- **Parsing for natural language**
  - Constituency parsing groups the words of a sentence into nested phrases (noun phrase, verb phrase) under a context-free grammar; the CKY algorithm fills a table of spans in O(n³·|G|) time for a grammar in Chomsky normal form
  - Dependency parsing links each word to exactly one head word by a labelled arc, forming a tree with one root; a transition-based parser builds it with a stack and a buffer, using 2n − 1 shift and reduce actions for n words in the arc-standard system
  - Parsers are scored by unlabelled and labelled attachment scores (UAS and LAS): the share of words whose head, and whose head with its label, match the gold tree
- **The Chomsky hierarchy and language models**
  - Type 3 (regular) languages are recognized by finite automata, type 2 (context-free) by pushdown automata, type 1 (context-sensitive) by linear-bounded automata, and type 0 (recursively enumerable) by Turing machines; each class is strictly contained in the next, with witnesses such as aⁿbⁿ (context-free, not regular) and aⁿbⁿcⁿ (context-sensitive, not context-free)
  - A language model is a probability distribution over strings; an n-gram model is a Markov chain over the previous n − 1 tokens
  - The hierarchy speaks to expressive power, not to the statistics of trained networks, so it asks what a model class can express and does not measure how well a model predicts text; perplexity, the exponential of the mean negative log-likelihood per token, is the measure for comparing models on the same text
- **Formal semantics**
  - Operational semantics as a transition relation on configurations: small-step ⟨e, σ⟩ → ⟨e′, σ′⟩ or big-step judgments e ⇓ v, with properties such as determinism proved by induction on the derivation
  - Denotational semantics assigns each phrase a mathematical object: a while loop denotes the least fixed point of a functional on partial functions, obtained as the supremum of the iterates from the everywhere-undefined function (Kleene's fixed-point theorem for continuous functionals on a domain with a least element); the denotation of recursion is that least fixed point, not an informal unrolling
  - Adequacy relates the two: the operational and denotational meanings agree for each phrase of the language

### Exercises

- A tested Python command-line program in version control
- A NumPy broadcasting and vectorization benchmark against plain loops; a FastAPI service with Pydantic models and async endpoints
- From scratch: a JSON parser; a chunk-boundary-safe Server-Sent Events parser; a minimal test runner discovering `test_` functions
- From scratch: a module graph served from a local proxy, with a predicted build list
- Untangling a package import cycle; predicting initialisation order
- Python-exact floor division and modulo, and overflow detection, in Go
- A command-string vending machine with labelled breaks
- Non-overlapping chunking, in-place dedupe and the nested-map panic
- A memoiser and the recursion-bypass trap, with `defer` tracing
- All-or-nothing batch transfers with joined errors and panic-safe rollback
- Rune-safe word wrap and card-number redaction
- An allocation-free parser and GC experiments under `GOGC` and `GOMEMLIMIT`
- Money that never loses a cent: largest-remainder allocation and an order type
- A notifier with decorators, functional options and the embedding trap
- A generic ordered map with iterators and a pull-based merge
- A configuration loader that rejects ambiguity and saves atomically
- `shopctl`: subcommands, config precedence and exit codes
- A goroutine-leak hunter; ordered fan-out with early stop
- A polite fetcher on a fake network with rate limits and retry budgets
- A fuzzed, benchmarked test suite with `synctest`
- A hardened orders HTTP edge with graceful shutdown and slow-client defence
- Serializable money transfers with retries, and the lost-update demonstration
- Streaming inventory over gRPC with back-pressure and schema evolution
- Finding three planted regressions from profiles alone
- A byte-identical reproducible build and minimal container image
- A reflection-based tag validator compared with hand-written and generic code
- A timing wheel versus a timer heap
- A login service with an adversarial test suite
- A checkout that survives a hostile payment provider, with reconciliation
- Unblocking a Node service stalled by CPU work; a streaming page with Zod-validated input
- Payments in Go: an idempotent charge endpoint, a webhook receiver with signature and replay checks, a double-entry ledger with property tests, a refund and dispute state machine, a nightly reconciliation job
- Services in Go: an orders API; a concurrent event worker; a gRPC inventory service
- An agent control plane in Go: an API gateway with custom plugins, a backend API, an auth service issuing JWTs, an LLM router over embeddings, an agent registry synced to the gateway, chat history over JSON-RPC, an orchestrator and build worker on Redis Streams, an operator CLI and A2A sample agents, verified end to end from upload through build, deploy, registration, routing, chat and traces, then promoted from staging to production with a load test, a backup and restore drill and a security review
- From scratch: a register allocator by linear scan over live intervals, compared with a graph-colouring allocator on the same interference graph, with the spill count of each recorded
- **Reasoning drills**
  - Predict the output of tricky programs (aliasing, closures, integer division, `defer` order, slice sharing) before running them
  - Prove a loop correct with an invariant, then find the smallest input that violates its precondition
  - Estimate allocation and garbage-collection cost from a profile before optimizing, then measure the gain
  - Choose between Python, Go and TypeScript for a new service, as a decision record
  - Predict which Chomsky class a given language belongs to, then prove the class by a pumping or closure argument
  - Predict the tokens a constrained decoder allows after a given prefix of a small schema, then check the prediction against the automaton
