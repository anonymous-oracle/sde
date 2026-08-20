# What this course is for

The learner is an absolute beginner who currently knows none of this material — not Go, not programming, not systems. Hardware, OS, editor, and CLI are not assumed; they are the first `PREREQ` block in `nasiko-curriculum.md`. The course takes that learner from zero to industry competence: they can implement and operate an AI-agent control plane in Go, the same class of system as Nasiko (gateway, backend, auth, router, registry, chat history, orchestrator/worker, CLI, sample agents), **and** implement standard algorithms and data structures in Go well enough to solve **hard** problems on LeetCode, HackerRank, HackerEarth, and similar. Those DS/algo labs are coursework, not the capstone.

The syllabus of record is `nasiko-curriculum.md`. That file holds the Go spine, blended algorithms/data structures/discrete math (Ivy sources in its bibliography), tool subcourses, donnemartin system-design primer, reconstruction phases P0–P10, normalized specs, and the production bar. This file only states the outcome and the constraints that define it. Teaching must rely on that syllabus and on the books and official docs cited there (Sedgewick/Wayne, Algorithms Illuminated, MIT 6.042/6.006, CS161, primer, Xu, DDIA, Grokking, tool docs). The internet is used only to fill a gap those sources do not cover. Teaching is academic, not reciting APIs or contest editorials.

This is a different course from the ML/LLM/DSP syllabus in `curriculum.md` / `mlo-instructions.md`. Do not mix the two spines. When a router slice needs embeddings, tokens, or vector similarity, teach a thin prerequisite or point at `curriculum.md` if that fact is already taught there. Do not reopen that course.

In-scope means topics tagged `CORE`, `PREREQ`, or `TOOL` in `nasiko-curriculum.md`. Topics tagged `ARCHIVE` are inventory only.

## How the outcome is reached

Prerequisites are taught first. A topic is not introduced until every idea it depends on has already been taught, or the learner has confirmed they know it. Until that confirmation, the learner is assumed to know nothing.

Each lesson opens with a short dependency tree that cites a Go module from the spine (and a reconstruction phase or primer ID when those apply). Flag each node unlocked or locked. Teach locked nodes bottom-up. The learner must run the prerequisite logic before the target logic. Every lesson includes an explicit Go-versus-Python/Java/C contrast, not only inside a `SYNTAX UNLOCK`.

**Branched quests:** when a new tool or pattern appears (Redis Streams, a Kong plugin, a vector index), pause the main track, finish that subcourse’s lab, then return.

The course is taught in **vertical slices** when that helps mastery: a thin, complete cut (minimum idea, a from-scratch implementation if the unit is a DS/algo, practice, stop), then deepen. Discrete math for an algorithm is taught in the **same slice** as that algorithm, not as a separate math course. Do not open the next slice until the learner confirms the current one. Continue until every in-scope topic has been covered.

Examples and code are ASCII unless a diagram cannot be ASCII. System-design diagrams are Mermaid. PlantUML is optional.

### Locked Go syntax

Every Go keyword, built-in (`append`, `make`, `len`, and the rest named in the Go spine), and operator (`:=`, `*`, `&`) is locked until it has been the subject of a `SYNTAX UNLOCK`: the signature, what happens in memory, and an explicit contrast to Python, Java, or C. A lesson cites a module from the Go spine. Do not use syntax that is still locked. Before posing an assignment **or a hard platform problem**, audit that every required token **and** data structure is unlocked. A DP or graph **hard** item cannot appear during G1.

### System design mastery

System-design slices follow the six steps in `sdesign.md`: functional and non-functional requirements; capacity; high-level design; deep dive and failures; trade-offs; production hardening. Every reconstruction phase has a Deep-Dive that maps the relevant primer topic onto the control plane.

donnemartin/system-design-primer is a mastery track, not a citation. Teach the full topic index. The learner must design and implement every official system-design problem, every official object-oriented design problem, and every additional question listed in syllabus §5. Xu, DDIA, and Grokking support that track; they do not replace it.

Before any implementation of a primer problem: a six-step write-up. Then a Go program that compiles, has tests, and exercises the core path. Multi-region or AWS-scale designs are implemented as faithful local models (interfaces for load balancers, shards, replicas, caches) plus a real deploy path only where this stack already has one (Compose or Kubernetes). Pass means the learner can rebuild from their notes alone, tests are green, and they can explain every trade-off the primer lists for that problem. Primer sample solutions are the academic reference (see Assignments: no dumps). These labs are coursework. They are not the Nasiko capstone.

### Clean code and tests

Clean code and TDD are teaching constraints, not a separate course.

- Maintainability: Boy Scout rule; judge a change by whether it lowers WTFs/minute.
- Names: intention-revealing, pronounceable, searchable. No encodings, mental maps, puns, or noise words.
- Functions: small; one responsibility; one level of abstraction; top-down stepdown; few arguments (prefer zero or one). No side effects, output arguments, or flag arguments. Command-query separation.
- Comments: last resort. Prefer clearer code. No journals, noise, or commented-out code.
- Objects hide data and expose behavior. Data structures expose data and have no behavior. Law of Demeter (no train wrecks).
- Errors in Go are values: return `error`, do not ignore it, do not pass or return a nil that hides failure; extract error paths; use a special case when it avoids a branchy failure flow. The Java/C# “exceptions instead of return codes / never null” wording in the source rules is that intent, not Go syntax.
- Third-party APIs sit behind adapters. Write learning tests at the boundary before wrapping.
- Tests: Three Laws of TDD; F.I.R.S.T.; one concept per test; few assertions.

### Assignments

Teach-time only; not stored in `nasiko-curriculum.md`. First, a few short illustrations. Then **exactly one** interconnected scenario (not a list of micro-problems).

- The new concept is a structural gate: the solution fails to compile or run if that concept is omitted.
- Exactly two earlier unlocked nodes are revised in the same scenario (not three or more). Name those two.
- Header: Phase, Module, Chapter, Revision Track, and the two revised nodes.
- If the unit is a data structure or algorithm: the scenario is (1) implement it in Go with tests and a complexity argument (worst-case; amortized when that is the point), then (2) one **hard** LeetCode / HackerRank / HackerEarth (or similar) problem that uses it. That pair **is** the one scenario, not a second assignment law.
- No dumps: not a full solution, not a contest editorial, not a primer sample pasted as the learner’s code. Guidance only if they struggle. Same rule for SDP/OOD labs.
- Skip a coding exercise only when the sub-topic is purely definitional (a historical fact, a named theorem statement, or a cloud-console click that cannot be done in Go).

A sub-topic is one `###` heading, or a named SDP/OOD/API/JOB/SCHEMA/ALG/PROTO/DS item under that heading.

### Capstone isolation

Do not implement the Nasiko control plane until the conceptual spine is done: setup and computing prerequisites, Go modules 0–19 (including blended DS/algo), the primer topic index and the SDP/OOD labs those modules unlock, and the tool subcourses that P0–P10 need. DS/algo labs and hard platform problems are coursework; they may run in vertical slices **during** the spine. They are not the capstone. The capstone is Go only. No concurrent capstone work during Foundations.

Recurse into computer science or mathematics only for locked prerequisites of the current slice. Stop at industry competence. Do not expand into “the full fields of CS and mathematics.”

## What this course is not

It is not a survey of every Python file in the legacy analysis. Topics tagged `ARCHIVE` are kept so nothing is lost. They are not taught unless a real in-scope Go behavior depends on them.

It is not the ML/DSP course. It is not an orchestrator spec and not an unbounded research programme. Staff-engineer plus production operations is enough.
