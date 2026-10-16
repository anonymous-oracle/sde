# Rust Track — AI Infrastructure and Real Systems from Scratch

A self-contained track for learning Rust by building, from scratch, the kinds of systems that run AI products: storage engines, servers, runtimes, tensor and inference engines, retrieval engines, proxies, consensus and sandboxes. The first part lists every Rust topic, each tagged with the project that first forces it; the second part is the projects themselves, in order.

## How this track is learned

- **The system is the syllabus**: every Rust topic is met inside a real system that needs it. No topic is taught before a project forces it, and none is left out: each topic below carries the tag of the project where it is first taught (P1 to P21).
- **Stage by stage**: each project is built in numbered stages. A stage adds at most one new Rust topic and one new systems idea, ends with passing tests, and is committed before the next stage starts.
- **Every stage is a specification**: before writing code, the stage is written out in full: the goal, the interfaces, the edge cases, the acceptance tests, a one-line prediction (what will break, how fast it will run, how much memory it will use), the measurement that settles the prediction, and what the learner will explain back afterwards. A wrong prediction is recorded and taught from.
- **Toy first, then the real system**: once the toy passes, the learner studies the design of the production system named under "Compare against" and lists what it handles that the toy does not: edge cases, performance, failure handling, security and standards. Hand-written cryptography and hand-written sandboxes are built only to learn, never deployed, and that is said each time.
- **Fight the compiler on purpose**: when the borrow checker or the type checker rejects a design, the learner writes down the rule it enforced and the bug it prevented before changing the code. These notes become a personal error catalogue, reviewed before each new project.
- **Measure, never guess**: every performance claim is backed by a `criterion` benchmark or a profile, and every correctness claim by a test, a property test or a fuzz run.
- **Code is accepted** when `cargo fmt --check` prints nothing, `cargo clippy --all-targets -- -D warnings` is clean, `cargo test` passes, every `unsafe` block carries a `// SAFETY:` comment naming the invariant it relies on and passes under Miri, no `unwrap` or `expect` appears outside tests without a comment saying why it cannot fail, and every thread or task has a way to stop.
- **Hints**: only when asked and one notch at a time: what structure do you see, then a smaller case, then the smallest useful hint, then the key. The tutor never writes the project code.
- **Mastery and recall**: a topic is mastered when the learner has used it in a passing stage and explained it back; mastered topics get a one-question recall about 1, 3, 7 and 21 sessions later, and a missed recall re-teaches only the gap.
- **Learning Go at the same time from zero**: start this track once the first two or three Go groups (toolchain, composite data, memory and types) are mastered, so that the two syntaxes do not settle at the same moment. A slip of one language's syntax into the other is logged as interference, not as a gap in the concept. Where a project also exists in Go, building it in Go first and porting it is allowed; the learner then names each place where Rust forced a different design.

**Prerequisites:** Python basics (variables, functions, lists and dictionaries, modules); the terminal and Git; binary, hexadecimal, two's complement and UTF-8; Big-O notation. Each project lists any further prerequisites of its own.

**Depth bar:** able to design, build, profile and harden production Rust services and libraries for AI infrastructure (inference serving, retrieval, data pipelines, proxies and storage) and to justify every ownership, concurrency and `unsafe` decision in them.

**Capstone:** a small AI serving platform assembled from the track's own parts: the AI gateway in front, the inference server running the hand-built inference engine, the vector database and hybrid search engine for retrieval, the MCP tool server with its WebAssembly sandbox, configuration replicated with the hand-built Raft, and metrics and traces throughout. It passes a load test with a written latency target, a fault-injection run (a killed node, a slow model, a full disk, a malicious tool) and a security review, and ships with a decision record for each major design choice.

## Part 1 — Rust topics

### Toolchain and program structure

- `rustup`, toolchain channels (stable, beta, nightly) and `rust-toolchain.toml` — P1
- `cargo new`, `build`, `run`, `check`, `test`, `doc`, `fmt`, `clippy`, `add`, `tree` — P1
- `Cargo.toml`: dependencies, dev-dependencies, features, editions; `Cargo.lock` and caret version requirements — P1
- Workspaces with several crates — P10
- Crates and the module tree; `pub`, `pub(crate)`; `use` paths; binary versus library crates — P1
- Debug versus release profiles; integer overflow panics in debug and wraps in release — P1

### Core language

- Scalar types; `char` as a Unicode scalar value; `as` casts that truncate silently versus `From`, `TryFrom` and `try_into` — P1
- `checked_`, `wrapping_` and `saturating_` arithmetic — P1
- Immutable by default and `let mut`; shadowing; blocks, `if` and `match` as expressions; labelled loops — P1
- Patterns: bindings, guards, ranges, `@`; `if let`, `while let`, `let else`; exhaustive `match` — P1
- `String` versus `&str`; no integer indexing into strings; `chars`, `char_indices`, `bytes` — P1
- Structs, tuple structs, enums carrying data, `impl` blocks, associated functions — P2

### Ownership, borrowing and lifetimes

- One owner per value; moves; `Copy` versus `Clone`; drop at the end of scope — P1
- RAII and `Drop`; drop order; `mem::take`, `mem::replace`, `mem::forget` — P3
- Shared `&T` or one exclusive `&mut T` (aliasing XOR mutability); non-lexical lifetimes; reborrowing; split borrows — P1
- Lifetime parameters and elision; structs that hold references; `'static` as a bound — P2
- Variance and higher-ranked trait bounds (`for<'a>`) — P15
- Self-referential types, `Pin` and `Unpin` — P5

### Errors

- `Option` and `Result`; `?`; the `From` conversion that `?` applies — P1
- One error enum per library with `thiserror`; `anyhow` with context in binaries — P3
- `panic!` for bugs versus errors for expected failures; `panic = "abort"`; `catch_unwind` only at thread and FFI boundaries — P4

### Traits, generics and iterators

- Traits, default methods, derivable traits, the orphan rule and newtypes — P2
- Closures and `Fn`, `FnMut`, `FnOnce`; `move` closures — P4
- Trait objects (`dyn Trait`), vtables and dyn compatibility — P4
- Generics with trait bounds and `where` clauses; monomorphisation and its code-size cost; `impl Trait` — P7
- Operator overloading through `std::ops`; `Index` and `IndexMut` — P7
- Associated types, generic associated types, supertraits, blanket implementations, marker traits and `PhantomData` — P11
- Typestate APIs that make invalid states unrepresentable — P14
- The `Iterator` trait, lazy adapters and `collect`; implementing `Iterator` for your own type — P1
- `IntoIterator` for `T`, `&T` and `&mut T`; iterator chains that compile to plain loops — P3

### Smart pointers and interior mutability

- `Box<T>` and recursive types — P2
- `Rc<T>`, `Weak<T>` and `RefCell<T>` for shared graphs; why arenas with indices are often better — P7
- `Arc<T>` across threads; `Cow<'a, T>` for borrow-or-own — P4

### Concurrency

- `thread::spawn`, `JoinHandle` and scoped threads (`thread::scope`) — P4
- `Send` and `Sync` as auto traits; data races as compile errors in safe code — P4
- `Mutex`, `RwLock`, `Condvar`; lock guards as RAII; poisoning — P4
- Channels: `std::sync::mpsc` and `crossbeam-channel`; bounded channels for back-pressure — P4
- Atomics with explicit orderings (`Relaxed`, `Acquire`, `Release`, `AcqRel`, `SeqCst`); `OnceLock` and `LazyLock` — P13
- `rayon` for data parallelism with work stealing — P7
- Lock-free structures, the ABA problem, epoch-based reclamation and `loom` model checking — P13

### Async

- `Future`, `Poll`, `Context` and `Waker`; `async fn` compiled into a state machine; futures do nothing until polled — P5
- Executors and reactors: readiness with `epoll` or `kqueue` through `mio` — P5
- Tokio: multi-threaded versus current-thread runtimes; `spawn` needing `Send + 'static`; `spawn_blocking` — P6
- `select!`, cancellation by drop and cancellation safety; `JoinSet`; `CancellationToken` — P6
- `tokio::sync` channels (`mpsc`, `oneshot`, `broadcast`, `watch`), `Semaphore`, and async `Mutex` versus holding a `std::sync::Mutex` guard across `.await` — P6
- Streams, back-pressure and `async fn` in traits — P10

### Unsafe, memory layout and FFI

- The five unsafe powers; undefined behaviour; safe abstractions over unsafe code and their soundness obligation; Miri — P7
- `MaybeUninit`, `NonNull`, `ManuallyDrop`; `#[repr(C)]`, `#[repr(transparent)]`, alignment and padding — P7
- Memory-mapped files (`memmap2`) and zero-copy casts (`bytemuck`) — P9
- FFI: `extern "C"`, `#[no_mangle]`, `bindgen`, `cbindgen`, `CString` and `CStr`; who allocates and who frees — P18
- PyO3 and maturin; releasing the GIL; sharing NumPy buffers without copying — P18
- Linux system calls through `nix` or `rustix`: namespaces, cgroups, `mount`, `pivot_root` — P19

### Performance

- Stack versus heap; counting allocations; `Vec` capacity; `SmallVec`; a global allocator (mimalloc or jemalloc) — P3
- Cache locality, struct-of-arrays layout, blocking and tiling — P7
- SIMD: auto-vectorisation, `std::arch` intrinsics, `target-feature` and run-time feature detection — P7
- Profiling with `perf` and `cargo flamegraph`; heap profiling with `dhat`; `tokio-console` — P4
- Release tuning: LTO, `codegen-units`, profile-guided optimisation — P9

### Macros

- Declarative macros (`macro_rules!`): fragment specifiers, repetition, hygiene — P12
- Procedural derive macros with `syn` and `quote`; their compile-time cost — P16

### Testing and tooling

- Unit tests, integration tests in `tests/`, doc tests — P1
- Property tests with `proptest`; fuzzing with `cargo fuzz` — P2
- Benchmarks with `criterion` — P3
- Deterministic simulation testing with a seeded scheduler and simulated network and clock — P14
- Supply chain: `cargo audit`, `cargo deny`, `cargo vet`; `build.rs` scripts and procedural macros as code that runs at build time — P17
- Cross-compilation by target triple; static `musl` builds; small container images — P17

### Ecosystem for AI infrastructure

- Services: `tokio`, `hyper`, `axum`, `tower`, `reqwest`, `tonic` and `prost`
- Data: `serde` and `serde_json`; `arrow-rs`, `parquet`, DataFusion and Polars
- Models: `candle`, `ort` (ONNX Runtime), `burn`; `safetensors`; `tokenizers`
- GPU: `cudarc` and `wgpu`
- Search and retrieval: `tantivy`; Qdrant and LanceDB as Rust-built engines
- Observability: `tracing`, `metrics`, OpenTelemetry
- Sandboxing and kernel tooling: `wasmtime`; `aya` for eBPF

## Part 2 — Projects

Each project lists what it builds, the Rust topics it forces, the systems ideas it teaches, its stages, the production systems to compare against, and when it is done.

### P1. Command-line text tools

**Builds:** a `grep`-like search tool and a log summariser that count, filter and group lines from files or standard input.

**Rust:** Cargo, modules, ownership and borrowing, `String` and `&str`, `Result` and `?`, iterators, unit and integration tests.

**Systems:** streaming input instead of loading whole files; buffered I/O; exit codes; UTF-8 versus raw bytes.

**Stages:**

1. Count lines, words and bytes of one file; match `wc` on test files.
2. Read from standard input when no file is given; stream line by line with `BufRead`.
3. Fixed-string search with line numbers and exit codes (0 found, 1 not found, 2 error).
4. Regular expressions with the `regex` crate; invalid UTF-8 lines handled without crashing.
5. Group log lines by level and print the top ten messages, using a `HashMap` and sorting.

**Compare against:** ripgrep.

**Done when:** output matches `grep` and `wc` on a test corpus that includes empty files, huge lines and invalid UTF-8, and a 1 GB file is processed in constant memory.

### P2. A JSON parser and serializer

**Builds:** a parser that turns JSON text into a value tree and back, then a zero-copy version whose strings borrow from the input.

**Rust:** enums carrying data, `Box` for recursion, traits (`Display`), lifetimes on structs that hold references, property tests and fuzzing.

**Systems:** grammars and recursive-descent parsing; escapes and surrogate pairs; number precision; rejecting malformed input safely.

**Stages:**

1. A tokenizer for JSON's grammar with byte positions in errors.
2. A recursive-descent parser into an owned `Value` enum; a depth limit against deeply nested input.
3. A serializer, and a round-trip property test (parse after print gives the same value).
4. A zero-copy parser whose strings are `&str` borrowed from the input, falling back to owned strings only when escapes are present (`Cow`).
5. A fuzz target that must never panic.

**Compare against:** `serde_json` and `simd-json`.

**Done when:** the JSON test suite of valid and invalid documents passes, the fuzzer runs for an hour without a crash, and the zero-copy version allocates measurably less than the owned one.

### P3. A log-structured key-value store

**Builds:** a persistent key-value store, first as an append-only log with an in-memory index (Bitcask style), then as a log-structured merge tree.

**Rust:** file I/O, RAII and `Drop`, error enums with `thiserror`, iterators over your own types, allocation measurement, `criterion` benchmarks.

**Systems:** write-ahead logging, `fsync` and crash recovery, checksums, compaction, sorted string tables, bloom filters, write and read amplification.

**Stages:**

1. Append-only log of set and delete records with a CRC per record; an in-memory hash index rebuilt on start.
2. Crash safety: a torn last record is detected and dropped; a test that kills the process mid-write.
3. Compaction that rewrites live keys into a new file and switches over atomically.
4. LSM tree: a sorted memtable, flushes to immutable sorted files, reads that check newest first.
5. Bloom filters per file and a size-tiered or levelled compaction policy; measure read and write amplification.

**Compare against:** Bitcask, RocksDB, `sled` and `fjall`.

**Done when:** a randomized crash test never loses an acknowledged write, and benchmarks show the write and read amplification predicted beforehand.

### P4. An HTTP/1.1 server on threads

**Builds:** an HTTP/1.1 server and client over raw TCP, served by a hand-built thread pool.

**Rust:** threads, `Arc`, `Mutex`, channels, `Send` and `Sync`, closures as jobs, trait objects for handlers, panics versus errors, profiling.

**Systems:** request parsing, keep-alive, chunked transfer encoding, timeouts, slow-client defence, graceful shutdown, thread-pool sizing.

**Stages:**

1. A single-threaded server that parses a request line and headers and returns static files.
2. A thread pool fed by a bounded channel; a full queue returns 503 instead of growing without limit.
3. Keep-alive, `Content-Length` and chunked bodies; header and body size limits.
4. Read and write timeouts; a slow-client test that must not starve other clients.
5. Graceful shutdown: stop accepting, finish in-flight requests, join every worker.

**Compare against:** `hyper` and `axum`.

**Done when:** a load generator shows stable latency up to the pool's capacity and clean 503s beyond it, and shutdown never drops an in-flight request.

### P5. An async runtime from scratch

**Builds:** a minimal async executor with a reactor and timers, able to run the P4 server as async tasks.

**Rust:** `Future`, `Poll`, `Waker`, `Context`, `Pin`, `async fn` as a state machine, `mio` for readiness events.

**Systems:** event loops, readiness versus completion I/O (`epoll`, `kqueue`, `io_uring`), cooperative scheduling, timer wheels.

**Stages:**

1. A hand-written future (a countdown) polled by a loop; then a waker that requeues the task.
2. A single-threaded executor with a task queue and `spawn`.
3. A reactor on `mio`: TCP accept, read and write futures woken by readiness events.
4. Timers with a timing wheel or a heap; a `sleep` future and a timeout combinator.
5. Port the P4 server and compare memory and latency at 10,000 idle connections.

**Compare against:** Tokio, smol and `async-std`.

**Done when:** the async server holds 10,000 idle connections with a fraction of the threaded server's memory, and the learner can explain every state of a compiled `async fn`.

### P6. A Redis-compatible server on Tokio

**Builds:** a server that speaks the Redis protocol (RESP) and supports strings, expiry, lists and publish–subscribe.

**Rust:** Tokio tasks, `select!`, cancellation, `tokio::sync` channels, shared state behind `Arc<Mutex<_>>` or sharded maps, `spawn_blocking`.

**Systems:** protocol framing, pipelining, key expiry (lazy plus active sampling), fan-out messaging, persistence snapshots.

**Stages:**

1. RESP framing over a byte buffer, tested against `redis-cli`.
2. `GET`, `SET` with expiry, `DEL`, `INCR`; a sharded map to reduce lock contention.
3. Pipelining and back-pressure on slow clients.
4. Publish–subscribe with `broadcast` channels; a slow subscriber must not block publishers.
5. Snapshot persistence on a background task; graceful shutdown with a cancellation token.

**Compare against:** Redis, Valkey and the `mini-redis` teaching project.

**Done when:** `redis-benchmark` runs against it with a measured throughput, and no lock is held across an `.await`.

### P7. A tensor library and an autograd engine

**Builds:** an n-dimensional tensor type with broadcasting and fast matrix multiplication, then reverse-mode automatic differentiation that trains a small neural network.

**Rust:** generics with trait bounds, operator overloading, `Index`, `Rc` and `RefCell` or an arena for the graph, `rayon`, unsafe code for an aligned buffer, SIMD.

**Systems:** strides and memory layout, broadcasting rules, cache blocking, data parallelism, the computation graph, numerical gradient checks.

**Stages:**

1. A `Tensor` with shape and strides; views, transposes and reshapes without copying.
2. Element-wise operations with broadcasting; a naive matrix multiply.
3. A faster matrix multiply: loop reordering, cache blocking, `rayon`, then SIMD; measure each step in GFLOP/s.
4. An aligned buffer built with `unsafe`, justified and checked under Miri.
5. Reverse-mode autograd over a tape or arena; gradients checked against finite differences.
6. Train a two-layer network on a small dataset with SGD and Adam.

**Compare against:** `ndarray`, `candle`, `burn` and PyTorch.

**Done when:** gradient checks pass, the network reaches a stated accuracy, and the matrix multiply reaches a stated fraction of the machine's measured peak.

### P8. A byte-level BPE tokenizer

**Builds:** a byte-pair-encoding tokenizer that trains a vocabulary from text and encodes and decodes losslessly.

**Rust:** byte handling, `HashMap` and `BinaryHeap`, efficient string building, `rayon` for parallel encoding, property tests.

**Systems:** subword tokenization, merge rules, special tokens, pre-tokenization, why token counts drive model cost.

**Stages:**

1. Train merges on a small corpus by counting adjacent pairs.
2. Encode with the learned merges; decode back to identical bytes for any input.
3. Faster training with a priority queue and incremental pair counts.
4. Special tokens and a pre-tokenization regex.
5. Load and run a published vocabulary and check output against its reference implementation.

**Compare against:** Hugging Face `tokenizers` (written in Rust) and `tiktoken`.

**Done when:** decoding after encoding is the identity on fuzzed input, and token IDs match the reference implementation on a test corpus.

### P9. An LLM inference engine

**Builds:** a program that loads a small open-weights transformer and generates text token by token on the CPU.

**Rust:** memory-mapped weights, zero-copy casts, `#[repr(C)]` layouts, SIMD kernels, `rayon`, release tuning with profile-guided optimisation.

**Systems:** the transformer forward pass (embeddings, RMSNorm, attention with RoPE, the MLP), the KV cache, quantization (8-bit and 4-bit with block scales), sampling (temperature, top-k, top-p), tokens per second and memory bandwidth limits.

**Stages:**

1. Read a `safetensors` file through `mmap` and map tensors by name.
2. A forward pass for one token; logits checked against a reference implementation to a tolerance.
3. A KV cache, and generation speed measured with and without it.
4. Sampling strategies, with a fixed seed for reproducible output.
5. 8-bit and 4-bit quantized weights; measure speed, memory and quality loss (perplexity) against full precision.
6. Stream tokens to the terminal as they are generated.

**Compare against:** `candle`, `llama.cpp` and `mistral.rs`.

**Done when:** output matches the reference model's greedy output for a test prompt, and measured tokens per second is explained by the machine's memory bandwidth.

### P10. An inference server with continuous batching

**Builds:** an HTTP service in front of the P9 engine that serves many users at once.

**Rust:** a workspace of crates, `axum`, streams, back-pressure with bounded channels and semaphores, `async fn` in traits, a dedicated thread for compute connected to async code.

**Systems:** request queues, continuous batching, a paged KV cache, admission control, Server-Sent Events streaming, time-to-first-token and inter-token latency, cancellation when a client disconnects.

**Stages:**

1. A single-request endpoint compatible with the common chat-completions request shape, streaming tokens over Server-Sent Events.
2. A scheduler on its own thread; async handlers talk to it through channels.
3. Continuous batching: new requests join a running batch between steps.
4. A paged KV cache with fixed-size blocks and a free list; reject or queue requests when memory runs out.
5. Cancellation when a client disconnects; metrics for queue depth, time to first token and tokens per second.

**Compare against:** vLLM and Hugging Face Text Generation Inference (whose router is written in Rust).

**Done when:** a load test shows throughput rising with batching while time to first token stays within a written target, and a disconnected client frees its KV blocks.

### P11. A vector database

**Builds:** a store for embedding vectors with exact and approximate nearest-neighbour search, metadata filters and persistence.

**Rust:** associated types and generic distance metrics, `PhantomData`, SIMD distance kernels, `rayon`, memory-mapped segments.

**Systems:** cosine, dot-product and Euclidean distance; flat search with a top-k heap; HNSW graphs; IVF and product quantization; recall versus latency trade-offs; filtered search; write-ahead logging.

**Stages:**

1. Flat search with a top-k heap; this is the ground truth for recall.
2. HNSW insertion and search; measure recall@10 and latency against flat search as `ef` changes.
3. Product quantization for memory reduction; measure the recall cost.
4. Metadata filters applied before, during and after search, and when each strategy fails.
5. Persistence with a write-ahead log and memory-mapped segments; deletes as tombstones and periodic rebuilds.
6. An HTTP API with batch upsert and query.

**Compare against:** Qdrant, LanceDB, FAISS and `usearch`.

**Done when:** a recall–latency curve is plotted for HNSW against the exact baseline, and a crash test loses no acknowledged write.

### P12. A full-text and hybrid search engine

**Builds:** an inverted-index search engine with BM25 ranking, then hybrid search combined with the P11 vector store.

**Rust:** declarative macros for repetitive codecs, iterators over compressed postings, `BinaryHeap` top-k, bit manipulation.

**Systems:** tokenization and normalization, inverted indexes, posting-list compression (delta and variable-length integers), BM25, segment merging, reciprocal rank fusion, ranking evaluation with recall@k and nDCG.

**Stages:**

1. An in-memory inverted index with term frequencies; boolean AND and OR queries.
2. BM25 scoring with a top-k heap.
3. Immutable on-disk segments with compressed postings; segment merging.
4. Phrase queries using positions.
5. Hybrid retrieval: fuse BM25 and vector results with reciprocal rank fusion; measure nDCG on a labelled query set against each alone.

**Compare against:** `tantivy`, Lucene and Elasticsearch.

**Done when:** BM25 scores match a reference implementation on a test collection, and the hybrid result beats both single methods on the labelled set or the learner explains why it does not.

### P13. Lock-free structures and a metrics library

**Builds:** a lock-free queue and counters, then a low-overhead metrics library with histograms used by every later project.

**Rust:** atomics and memory orderings, `OnceLock`, `unsafe` with raw pointers, epoch-based reclamation, `loom` model checking, Miri.

**Systems:** compare-and-swap loops, the ABA problem, false sharing and cache-line padding, histogram buckets and percentile accuracy, the cost of a metric on the hot path.

**Stages:**

1. Atomic counters and gauges; measure contention with and without per-thread sharding and cache-line padding.
2. A lock-free stack and its ABA bug, demonstrated and then fixed with epoch reclamation.
3. A bounded multi-producer multi-consumer queue, verified with `loom`.
4. A histogram with fixed relative error, checked against exact percentiles.
5. A Prometheus text-format exporter.

**Compare against:** `crossbeam`, `metrics` and HdrHistogram.

**Done when:** `loom` explores the queue without finding a bug, Miri is clean, and the overhead per recorded metric is measured in nanoseconds.

### P14. Raft consensus and a replicated key-value store

**Builds:** the Raft protocol and a key-value store replicated by it, tested under a deterministic simulator.

**Rust:** typestate for node roles, enums for messages, trait-based transports so the real network and the simulator are interchangeable, seeded randomness.

**Systems:** leader election, log replication, commit index, persistence before acknowledgement, snapshots and log compaction, linearizable reads, partitions and clock skew.

**Stages:**

1. Leader election with randomized timeouts in a simulated network.
2. Log replication and the commit rule.
3. Persistence of term, vote and log before replying; crash and restart tests.
4. Snapshots and log compaction.
5. A key-value service with linearizable reads; a linearizability checker over recorded histories.
6. Deterministic simulation: random partitions, delays, drops and crashes, replayable from a seed.

**Compare against:** `openraft`, `raft-rs` (used by TiKV) and etcd.

**Done when:** thousands of seeded simulation runs pass the linearizability checker, and any failing seed replays exactly.

### P15. A columnar query engine

**Builds:** an engine that runs a subset of SQL over columnar data with vectorized execution.

**Rust:** borrowed column views with lifetimes, variance and higher-ranked bounds in operator traits, enums for typed arrays, `rayon`.

**Systems:** columnar layout, dictionary and run-length encoding, a SQL parser, logical and physical plans, predicate pushdown, vectorized filters, hash joins and hash aggregation, spilling.

**Stages:**

1. Typed column arrays with validity bitmaps; load CSV into columns.
2. Dictionary and run-length encodings; measure size against plain columns.
3. A parser for `SELECT`, `WHERE`, `GROUP BY` and `JOIN` into a logical plan.
4. Vectorized filter and projection operators over batches.
5. Hash aggregation and hash join; predicate pushdown and projection pruning.
6. Read Parquet files and compare plans and speed.

**Compare against:** Apache DataFusion, Polars and DuckDB.

**Done when:** results match SQLite or DuckDB on a test query set, and each optimisation's speed-up is measured.

### P16. A segmented log and message queue

**Builds:** a durable, partitioned log with producers, consumer groups and offsets.

**Rust:** procedural derive macros for record encoding, `bytes` buffers, zero-copy reads, async networking.

**Systems:** append-only segments with sparse indexes, retention, consumer offsets, at-least-once delivery, idempotent producers, batching and compression, back-pressure.

**Stages:**

1. Append-only segment files with an offset index; reads by offset.
2. A derive macro that generates the binary encoding for record types.
3. A network protocol for produce and fetch with batching.
4. Consumer groups with committed offsets and rebalancing on join or leave.
5. Retention by time and size; idempotent producers with sequence numbers.

**Compare against:** Apache Kafka, Redpanda and Iggy.

**Done when:** a crash test shows no acknowledged message is lost, and duplicates appear only where at-least-once delivery allows them.

### P17. An L7 proxy and AI gateway

**Builds:** a reverse proxy that becomes a gateway for model APIs: routing, authentication, rate limiting, retries and token accounting.

**Rust:** `hyper` and `tower` layers, connection pools, `arc-swap` for hot configuration reloads, supply-chain checks, static release builds.

**Systems:** load-balancing algorithms, health checks, timeouts and retry budgets, circuit breakers, token-bucket rate limits, request hedging, streaming pass-through, per-tenant quotas measured in tokens, TLS termination with `rustls`.

**Stages:**

1. A pass-through proxy with connection pooling and streaming bodies.
2. Round-robin and least-outstanding-requests balancing with active health checks.
3. Timeouts, retries with a budget, and a circuit breaker; a fault-injection test with a flaky upstream.
4. Authentication with API keys and per-tenant token-bucket rate limits.
5. Model routing and fallback between providers; token counting on streamed responses for quotas.
6. Hot configuration reload without dropping connections; a static `musl` build in a small image, checked with `cargo deny` and `cargo audit`.

**Compare against:** Pingora, Envoy and `linkerd2-proxy`.

**Done when:** the fault-injection test keeps the error rate under a written target while one upstream fails, and a configuration reload drops no requests.

### P18. A Python extension and a C ABI library

**Builds:** a Rust library that speeds up a slow Python data-pipeline step, and the same library exposed over a C ABI.

**Rust:** PyO3 and maturin, releasing the GIL, NumPy buffers without copying, `extern "C"`, `cbindgen`, ownership rules across the boundary, panics that must not cross it.

**Systems:** foreign-function interface costs, memory ownership across languages, packaging wheels for several platforms.

**Stages:**

1. Profile a slow Python function (for example text normalization or deduplication) and set a speed target.
2. Rewrite it in Rust with PyO3; match outputs exactly on a test set.
3. Release the GIL and parallelize with `rayon`; share NumPy arrays without copying.
4. Expose the same library over a C ABI with a generated header; call it from a C or Go program.
5. Build wheels for Linux and macOS with maturin.

**Compare against:** Hugging Face `tokenizers`, `pydantic-core` and Polars, all Rust cores with Python interfaces.

**Done when:** the Python pipeline meets its speed target with identical output, and a test proves no panic crosses the boundary.

### P19. A container runtime and a WebAssembly sandbox

**Builds:** a minimal container runtime using Linux isolation primitives, then a WebAssembly sandbox for running untrusted tool code.

**Rust:** system calls through `nix` or `rustix`, `unsafe` around `fork` and `exec`, `wasmtime` embedding, resource limits.

**Systems:** namespaces (PID, mount, network, user), cgroups v2 limits, `pivot_root`, seccomp filters, capabilities; WebAssembly's memory isolation, fuel and epoch limits, WASI capabilities.

**Stages:**

1. Run a process in new PID and mount namespaces with its own root file system (Linux only, in a virtual machine).
2. Memory and CPU limits with cgroups v2; observe the out-of-memory kill.
3. A seccomp allow-list and dropped capabilities; show a blocked system call.
4. Embed `wasmtime`; run a WebAssembly tool with fuel and memory limits and no file-system access by default.
5. Grant a single directory through WASI and prove the tool cannot escape it.

**Compare against:** `youki`, `runc`, Firecracker and `wasmtime`.

**Done when:** a set of escape attempts (fork bombs, memory exhaustion, path traversal, forbidden system calls) all fail. The runtime is built only to learn and is never used to isolate real untrusted code.

### P20. GPU compute

**Builds:** matrix multiplication and a softmax kernel on the GPU, compared with the P7 CPU versions.

**Rust:** `wgpu` compute shaders or CUDA through `cudarc`, buffer management, asynchronous submission.

**Systems:** the GPU execution model (threads, blocks or workgroups, warps), memory hierarchy (global, shared, registers), memory coalescing, tiling, kernel launch and transfer overheads, numerical stability in softmax.

**Stages:**

1. Copy a buffer to the GPU, add two vectors, copy back; measure transfer time against compute time.
2. A naive matrix multiply kernel.
3. A tiled kernel using shared or workgroup memory; measure the speed-up.
4. A numerically stable softmax kernel.
5. Find the matrix size where the GPU beats the P7 CPU code, including transfer time.

**Compare against:** cuBLAS, `candle`'s GPU backends and Triton.

**Done when:** results match the CPU versions within a stated tolerance, and the crossover size is predicted and then measured.

### P21. An MCP tool server and an agent runtime

**Builds:** a Model Context Protocol server exposing tools, and a small agent loop that calls a model and those tools under strict limits.

**Rust:** JSON-RPC over standard input and output and over HTTP, `serde` with JSON Schema, Tokio timeouts, the P19 WebAssembly sandbox for tool execution.

**Systems:** tool discovery and invocation, input validation against schemas, idempotency keys for side-effecting tools, step and cost budgets, timeouts at three levels (tool, step, run), untrusted tool output, audit logging.

**Stages:**

1. An MCP server over standard input and output with `initialize`, `tools/list` and `tools/call`.
2. Schema validation of every tool input; structured errors.
3. Tools that run inside the WebAssembly sandbox with fuel and time limits.
4. An agent loop with a step budget, a cost budget and nested timeouts, calling the model through the P17 gateway.
5. Idempotency keys for side-effecting tools, and an approval pause before any irreversible action.
6. The same server over HTTP with authentication.

**Compare against:** the official MCP Rust SDK and agent frameworks.

**Done when:** a hostile-tool test (oversized output, a prompt-injection string, a hang, a crash) is contained without breaking the agent loop, and every run leaves a complete audit trail.

## Part 3 — Reasoning drills

- Predict whether a Rust snippet compiles (moves, borrows, lifetimes, `Send` bounds), and name the rule before reading the compiler error.
- For a design that the borrow checker rejected, name the bug the rejection prevented.
- Predict a benchmark's result (allocations, throughput, cache misses) before running it, then explain the gap.
- Given a flame graph from one of the projects, name the bottleneck and the change that would remove it before trying it.
- Choose between threads, an async runtime and a dedicated compute thread for a new workload, as a decision record.
- Choose between Rust, Go and Python for a new AI-infrastructure component, as a decision record with the measurements that would change the choice.
- Review an `unsafe` block: state its invariant, find an input that would break it, and decide whether it can be made safe.
