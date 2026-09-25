@@@ section
## 14. Academic depth (rule 0.4.10)

The academic pass of this companion: the theory of the language. It covers the specification as a formal object, the type system, the concurrency model and its memory model, the scheduler, and the memory manager, at the depth of a programming-languages and systems course (main course §0.6: the programming and operating-systems rows). Each block is taught after the GO module it names and before that module's involved problem, and it obeys the syntax unlock (rule 0.4.9). Problems GOT-P1…GOT-P10 are in §14.10, with keys in §14.11 (reveal only after the learner answers). A block is `mastered` by rule 0.4.10.3. Program outputs marked `(checked on 1.27.1)` were run on Go 1.27.1, linux/amd64, on 2026-09-24, offline.

### 14.1 GOT.1 · The specification as a formal object (deepens GO-02, GO-04)

- The Go specification defines its grammar in EBNF. Lexing turns bytes into tokens, and parsing turns tokens into a syntax tree. The grammar is context-free (main course A4.D7 names the Chomsky hierarchy), and the `go/ast` and `go/parser` packages expose the tree.
- The semicolon-insertion rule: the lexer inserts a semicolon after a line's final token when that token is an identifier, a literal, one of the keywords `break`, `continue`, `fallthrough` or `return`, one of `++`, `--`, or a closing `)`, `]` or `}`. This one rule explains why an opening brace cannot start a new line.
- Compilation phases in outline: parse, type-check, lower to SSA form, optimize, generate machine code, link.
- Reading: The Go Programming Language Specification (the version matching the installed release); Aho, Lam, Sethi and Ullman, *Compilers: Principles, Techniques, and Tools*, 2nd ed. (2006), chapters 1–4.

### 14.2 GOT.2 · The type system (deepens GO-03, GO-10, GO-11, GO-12)

- Defined types and type identity are nominal: `type Celsius float64` is a new type. Interface satisfaction is structural: a type implements an interface when its method set contains the interface's methods, with no declaration.
- Method sets: the method set of T contains the value-receiver methods; that of *T contains both kinds. So a T value does not satisfy an interface whose method has a pointer receiver (GOT-P3); the reason is that an interface holding a copy of T has no addressable variable to take a pointer to.
- Generics: a constraint denotes a type set; `~int` means every type whose underlying type is int. Type inference unifies argument types with parameter types. The implementation (GC-shape stenciling with dictionaries) sits between full monomorphization, as in C++ and Rust, and uniform boxed representation, as in Java's erasure.
- Parametric polymorphism versus subtype polymorphism (main course A3.D3), and why Go has no variance on generic types.
- Sum types. An interface is an *open* sum: any type in any package that has the methods is a member. Go has no *closed* sum (Rust's `enum` with payloads, an algebraic data type in ML or Haskell). The idiom that approximates one is the sealed interface: an interface with an unexported marker method, `type Event interface{ isEvent() }`, which only types declared in the same package can implement (GOT-P9). The compiler still does not check that a type switch covers every member, and `go vet` is silent, so a new variant falls through to `default` without warning. This is the expression problem (Wadler, 1998): open sums make new types cheap and new operations expensive, closed sums the reverse, and Visitor (the Design Patterns companion's DP-22) trades one for the other.
- Reading: Griesemer et al., "Featherweight Go" (OOPSLA 2020), the formal core of Go's generics.

### 14.3 GOT.3 · Evaluation semantics (deepens GO-06, GO-07)

- The specification's evaluation order: operands are evaluated left to right for function calls, method calls and communication operations; other orderings are unspecified.
- `defer` evaluates the function value and its arguments when the `defer` statement runs, and runs deferred calls last-in, first-out when the function returns (GOT-P1).
- Closures capture variables, not values. Since Go 1.22, each iteration of a `for` loop has its own loop variable, for modules whose `go` line is 1.22 or later (GOT-P7).
- Errors as values, formally: an error is part of the function's type, and `errors.Is` and `errors.As` search the wrap tree. Compare this with exceptions, which are an effect not visible in the type (Java's checked exceptions are the exception).

### 14.4 GOT.4 · Communicating sequential processes (deepens GO-16, GO-19)

- Hoare's CSP (1978): processes that share nothing and communicate by synchronous messages. An unbuffered Go channel is a rendezvous: the send and the receive complete together. A buffered channel of capacity k behaves as a bounded queue.
- `select` is guarded choice. When several cases are ready, the runtime picks one uniformly at random, so no case starves.
- Deadlock as a cycle in the wait-for relation (main course A6.D4). The runtime reports "all goroutines are asleep" only when every goroutine is blocked, so a partial deadlock is silent (GOT-P8).
- Reading: Hoare, "Communicating Sequential Processes", *Communications of the ACM* 21(8), 1978.

### 14.5 GOT.5 · The memory model (deepens GO-18)

- Happens-before (main course A9.D2) inside one process. A send on a channel happens before the matching receive completes. The k-th receive on a channel of capacity C happens before the (k + C)-th send completes. An `Unlock` happens before the next `Lock` returns, and `sync.Once`'s function returns before any `Do` returns.
- Progress conditions (main course A6.D4). A structure guarded by a `Mutex` is blocking: a goroutine descheduled while holding the lock stops everyone. A compare-and-swap retry loop (`for { old := c.Load(); if c.CompareAndSwap(old, old+1) { break } }`) is lock-free but not wait-free (GOT-P10). `atomic.Int64.Add` has no retry loop: on amd64 it compiles to one `LOCK XADDQ` instruction (checked on 1.27.1, `GOARCH=amd64`, with `go tool objdump`). Herlihy's consensus hierarchy (1991) explains why hardware provides compare-and-swap: atomic read/write registers have consensus number 1, so no wait-free queue or stack for two goroutines can be built from loads and stores alone, while compare-and-swap has an infinite consensus number. The ABA problem (a value changes from A to B and back, so a compare-and-swap wrongly succeeds) needs reused memory; Go's collector does not reuse an object that is still referenced, so a lock-free structure that swaps pointers to fresh nodes avoids it, but one that recycles nodes through a free list or `sync.Pool`, or swaps indices, does not.
- The Go memory model, revised in 2022 for Go 1.19, guarantees DRF-SC: a program without data races behaves as if its goroutines were interleaved on one processor (sequential consistency). The `sync/atomic` operations are sequentially consistent.
- A data race on a multi-word value (an interface, a slice or a string) can produce a value that was never written, which is why races are bugs and not just stale reads. The race detector finds races that happen during a run, not every possible race.
- Reading: The Go Memory Model (the version for the installed release); Adve and Boehm, "Memory Models: A Case for Rethinking Parallel Languages and Hardware", *Communications of the ACM* 53(8), 2010; Herlihy, "Wait-Free Synchronization", *ACM Transactions on Programming Languages and Systems* 13(1), 1991; Herlihy, Shavit, Luchangco and Spear, *The Art of Multiprocessor Programming*, 2nd ed. (2020), chapters 3 and 5.

### 14.6 GOT.6 · The scheduler (deepens GO-15)

- M:N scheduling: many goroutines (G) run on a few OS threads (M), through logical processors (P), and GOMAXPROCS sets the number of Ps.
- Work stealing: an idle P steals half of another P's run queue. For a computation with total work T₁ and critical-path length T∞, randomized work stealing runs in expected time T₁/P + O(T∞) on P processors (Blumofe and Leiserson, 1999). The speed-up is therefore bounded by min(P, T₁/T∞) (GOT-P5).
- Asynchronous preemption (since Go 1.14) stops a tight loop from holding a P forever. The network poller parks goroutines on `epoll` and friends (main course A6.D7).

### 14.7 GOT.7 · Memory management (deepens GO-09, GO-24)

- Escape analysis decides at compile time whether a variable can live on the stack. It is conservative: a variable whose address outlives the function moves to the heap, and `-gcflags=-m` prints the decisions (GOT-P6).
- Garbage collection is concurrent, tri-colour mark and sweep. White objects are unvisited, grey ones are visited with unscanned children, and black ones are fully scanned. The strong tri-colour invariant (no black object points to a white object) guarantees that the objects still white when marking ends are unreachable (GOT-P2). A write barrier maintains the invariant while the program mutates pointers; Go uses a hybrid of the Dijkstra insertion barrier and the Yuasa deletion barrier.
- The pacer: GOGC sets the heap growth before the next cycle, and GOMEMLIMIT sets a soft limit on total memory.
- Readings: Dijkstra, Lamport, Martin, Scholten and Steffens, "On-the-Fly Garbage Collection: An Exercise in Cooperation", *Communications of the ACM* 21(11), 1978; Jones, Hosking and Moss, *The Garbage Collection Handbook*, 2nd ed. (2023).

### 14.8 GOT.8 · Testing theory in Go (deepens GO-20)

- Property-based testing states an invariant and checks it on generated inputs. Coverage-guided fuzzing (`go test -fuzz`) mutates inputs toward new code paths and keeps a corpus of the inputs that found them.
- Benchmarks are samples: report a confidence interval, not one number (main course A2.D7), and compare runs with a statistical tool (benchstat) rather than by eye.

### 14.9 GOT.9 · Where Go sits among languages (deepens GO-11, §9)

- Go is a garbage-collected, statically typed language with structural interfaces and CSP concurrency. The contrast atlas of §9 compares its habits with other languages; this block names the design space instead. The axes are manual memory management versus GC versus ownership (Rust), nominal versus structural typing, exceptions versus error values, and threads with locks versus actors versus CSP.
- Reading: Pike, "Go at Google: Language Design in the Service of Software Engineering" (SPLASH 2012 keynote); Donovan and Kernighan, *The Go Programming Language* (2015), chapters 7–9.

### 14.10 Problem set (GOT-P1…GOT-P10)

- **GOT-P1** · compute · Predict the exact output (after GO-06):
  ```go
  x := 1
  defer fmt.Println("deferred", x)
  x = 2
  for i := 0; i < 3; i++ {
  	defer fmt.Print(i, " ")
  }
  fmt.Println("x", x)
  ```
- **GOT-P2** · proof · Prove that if the strong tri-colour invariant holds when marking ends (there are no grey objects), every white object is unreachable from the roots.
- **GOT-P3** · compute · Does this compile? If not, what is the error and the one-character fix? `type I interface{ M() }`, `type T struct{}`, `func (t *T) M() {}`, and `var i I = T{}`.
- **GOT-P4** · proof · A goroutine sets `data = 42` and then `done = true`; `main` loops until `done` is true and then prints `data`, with no other synchronization. Explain why the program has a data race and may never print 42. Rewrite it with a channel, and prove from the happens-before rules that it prints 42.
- **GOT-P5** · compute · A parallel job has total work T₁ = 800 ms and critical path T∞ = 10 ms. Estimate its running time on 8 processors under work stealing, and bound its possible speed-up.
- **GOT-P6** · compute · Which variable escapes to the heap, and why? `func f() *int { x := 1; return &x }` and `func g() int { x := 1; p := &x; return *p }`.
- **GOT-P7** · compute · Predict the output of this loop under a module whose `go` line is 1.27.1, and again under `go 1.21`:
  ```go
  var fs []func()
  for i := 0; i < 3; i++ {
  	fs = append(fs, func() { fmt.Print(i) })
  }
  for _, f := range fs {
  	f()
  }
  ```
- **GOT-P8** · compute · What happens when `main` runs `ch := make(chan int); ch <- 1; println(<-ch)`? Why, and what is the smallest fix?
- **GOT-P9** · compute · Package `shape` declares `type Event interface{ isEvent() }` with members `Paid` and `Refunded`, and `Describe(e Event) string` switches on `e.(type)` with a case for `Paid` only. (a) Does `shape` compile, and does `go vet` report anything? (b) Package `other` declares `type Chargeback struct{}` with `func (Chargeback) isEvent() {}` and `var _ shape.Event = Chargeback{}`. Does it compile? (c) What does sealing buy, and what does it not buy?
- **GOT-P10** · proof · A counter's `Inc` runs `for { old := c.Load(); if c.CompareAndSwap(old, old+1) { return } }`. Prove that `Inc` is lock-free, and show by a schedule that it is not wait-free.

### 14.11 Keys (reveal only after the learner answers)

- **GOT-P1** — Expected: `x 2` on the first line, then `2 1 0 deferred 1` (checked on 1.27.1). The deferred calls run last-in, first-out, and `x` was evaluated as 1 when the `defer` ran. · Wrong: `deferred 2` — the argument is evaluated at the `defer` statement, not when the call runs.
- **GOT-P2** — Expected: suppose a white object w is reachable. Take a path from a root (roots are shaded grey or black before marking ends) to w. Along it there is a first white object; its predecessor is black, because no grey objects remain. A black object pointing to a white one contradicts the invariant, so no white object is reachable, and sweeping the whites is safe. · Wrong: "whites are unreachable because the collector visited everything" — the program mutates pointers concurrently, which is exactly why the invariant (and a write barrier) is needed.
- **GOT-P3** — Expected: it does not compile: `T does not implement I (method M has pointer receiver)` (checked on 1.27.1). Fix: `var i I = &T{}`. · Wrong: "Go takes the address automatically" — it does so for method calls on addressable variables, not for interface satisfaction.
- **GOT-P4** — Expected: nothing orders the write to `data` before main's read, so there is a race, and DRF-SC promises nothing: the compiler may hoist the load of `done` out of the loop, or `main` may see `done` before `data`. Fix: the goroutine runs `data = 42; ch <- struct{}{}` and main runs `<-ch; println(data)`. The write to `data` is sequenced before the send, the send happens before the receive completes, and the receive is sequenced before the read, so the write happens before the read. · Wrong: "make `done` a `volatile`-style variable" — Go has no volatile; use a channel, a mutex or `sync/atomic`.
- **GOT-P5** — Expected: about T₁/P + T∞ = 100 + 10 = 110 ms; the speed-up is at most min(8, 800/10) = 8. · Wrong: 100 ms — ignores the critical path, which no number of processors shortens.
- **GOT-P6** — Expected: in f, x escapes (`moved to heap: x`) because its address is returned and outlives the call; in g, x stays on the stack because the pointer never leaves g (checked on 1.27.1 with `-gcflags=-m`). · Wrong: "any `&x` puts x on the heap" — escape depends on where the pointer flows, not on taking an address.
- **GOT-P7** — Expected: `012` with `go 1.27.1`, because each iteration has its own i; `333` with `go 1.21`, because all closures share one i, which is 3 after the loop (both checked on 1.27.1, varying only the module's `go` line). · Wrong: "the output depends on the installed toolchain" — it depends on the module's `go` line.
- **GOT-P8** — Expected: `fatal error: all goroutines are asleep - deadlock!` (checked on 1.27.1). An unbuffered send waits for a receiver, and the only receiver is the same goroutine, after the send. Fix: `make(chan int, 1)`, or send from another goroutine. · Wrong: "it prints 1" — that needs a buffer or a second goroutine.
- **GOT-P9** — Expected: (a) it compiles, and `go vet` is silent; `Describe(Refunded{})` returns the fall-through value (checked on 1.27.1). (b) It does not compile: `Chargeback does not implement shape.Event (unexported method isEvent)` (checked on 1.27.1): an unexported method name belongs to its package, so `other`'s `isEvent` is a different method. (c) Sealing closes the set of members to the declaring package; it does not make the compiler check that a switch is exhaustive, so each switch needs a `default` that fails loudly, or a test that lists every member. · Wrong: "a missing case is a compile error" — that holds for Rust's `match`, not for a Go type switch.
- **GOT-P10** — Expected: lock-free: a CAS fails only if `c` changed between the `Load` and the CAS, and `c` changes only when another `Inc` succeeds, so every failed attempt is matched by a completed `Inc` elsewhere; the system as a whole always makes progress. Not wait-free: let goroutine G load `old`, then let another goroutine complete an `Inc` before G's CAS, and repeat forever; G fails on every attempt while the others succeed, so G's number of steps has no bound. · Wrong: "it is wait-free because it never blocks" — not blocking gives lock-freedom at best; wait-freedom bounds every goroutine's own steps.
