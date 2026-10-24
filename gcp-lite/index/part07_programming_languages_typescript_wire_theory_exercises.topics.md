# Part 07 · Programming Languages & Language Theory (part 3 of 3) · TOPIC LIST

Rules and directives for this part: `index/part07_programming_languages_typescript_wire_theory_exercises.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Programming Languages & Language Theory (part 3 of 3)

### TypeScript, Node and the web client

- **TypeScript and Node**
  - Erased types; structural typing; `strict` mode
  - Union and literal types and narrowing; `unknown` versus `any`; generics
  - ES modules versus CommonJS
  - The Node event loop; blocking the loop with CPU work and moving it off
  - Promises, `async`/`await`; `Promise.all` failure semantics; `AbortController`
  - npm, `package.json`, lockfiles, `npx`; `tsc`, `node --test` or Vitest, ESLint
- **Runtime validation and a minimal React client**
  - "Parse, don't trust": a hand-written validator, then Zod (`safeParse`, error paths, inferred types, JSON Schema export)
  - React components as functions of state; `useState` and `useEffect`; rendering a stream as it arrives
  - Keeping API keys server-side behind a server route

### Wire formats

- **JSON**: the RFC 8259 grammar; no comments or trailing commas; unbounded numbers and 64-bit IDs in JavaScript; duplicate keys; a recursive-descent parser by hand
- **JSON Schema**: `type`, `properties`, `required`, `enum`, `additionalProperties`, `$ref`; schemas as contracts for tool inputs and structured outputs
- **JSON-RPC 2.0**: requests and notifications, `result` versus `error`, batches, reserved error codes −32700 to −32603
- **Server-Sent Events**: `text/event-stream`, `event:`, `data:`, `id:`, `retry:`, comments; incremental parsing across chunk boundaries; reconnection with `Last-Event-ID`; buffering proxies that break streaming

### Language theory

- **Program semantics**
  - Values versus references, mutability and aliasing
  - Scope, closures and lexical environments
  - Evaluation order; call by value, call by sharing, explicit pointers
- **Recursion and correctness**
  - Base cases and decreasing measures; correctness and termination by induction
  - Recursion versus iteration; tail calls; stack depth limits
- **Type systems**
  - Static versus dynamic, strong versus weak, nominal versus structural typing
  - Parametric versus subtype polymorphism; variance
  - Type soundness: progress and preservation
  - Open versus closed sum types; the expression problem; Featherweight Go
- **Specification and testing theory**
  - Preconditions, postconditions, loop invariants; Hoare triples and the assignment rule
  - Why line coverage does not prove correctness
  - Benchmarks as samples with confidence intervals
- **Compilers and interpreters**
  - Lexing, parsing, abstract syntax trees, type checking
  - Grammars in EBNF; context-free grammars; Go's semicolon-insertion rule; `go/ast` and `go/parser`
  - Intermediate representations and SSA; optimisation; code generation; linking
  - Interpreters and the Interpreter pattern
- **Concurrency theory in Go**
  - Hoare's CSP; rendezvous and bounded queues; guarded choice
  - Deadlock as a cycle in the wait-for graph
  - Herlihy's consensus hierarchy and why compare-and-swap exists
  - Work stealing: expected time T₁/P + O(T∞); speed-up bounded by min(P, T₁/T∞)
- **Memory-management theory**
  - Conservative escape analysis
  - Tri-colour marking and the strong tri-colour invariant; Dijkstra insertion and Yuasa deletion write barriers
  - The GC pacer
- **The language design space**
  - Manual memory versus garbage collection versus ownership
  - Exceptions versus error values; threads and locks versus actors versus CSP

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
- **Reasoning drills**
  - Predict the output of tricky programs (aliasing, closures, integer division, `defer` order, slice sharing) before running them
  - Prove a loop correct with an invariant, then find the smallest input that violates its precondition
  - Estimate allocation and garbage-collection cost from a profile before optimizing, then measure the gain
  - Choose between Python, Go and TypeScript for a new service, as a decision record
