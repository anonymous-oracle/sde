# What this course is for

The learner is an absolute beginner who currently knows none of this material — not Go, not programming, not systems. Hardware, OS, editor, and CLI are not assumed; they are the first `PREREQ` block in `nasiko-curriculum.md`. The course takes that learner from zero to industry competence: they can implement and operate an AI-agent control plane in Go, the same class of system as Nasiko (gateway, backend, auth, router, registry, chat history, orchestrator/worker, CLI, sample agents), understand and tune PostgreSQL-backed systems from relational algebra down to MVCC/WAL/index internals, design HLD/LLD/microservice architectures at an industry bar, **and** implement standard algorithms and data structures in Go well enough to solve **hard** problems on LeetCode, HackerRank, HackerEarth, and similar. Those DS/algo and database-systems labs are coursework, not the capstone.

The syllabus of record is `nasiko-curriculum.md`. That file holds the canonical knowledge graph, graph-ordered teaching stages, Go spine, blended algorithms/data structures/discrete math (Ivy sources in its bibliography), the PostgreSQL/database-systems braid, tool subcourses, donnemartin system-design primer, industry architecture research atlas, reconstruction phases P0–P10, normalized specs, and the production bar. This file only states the outcome and the constraints that define it. Teaching must rely on that syllabus and on the books and official docs cited there (Sedgewick/Wayne, Algorithms Illuminated, MIT 6.042/6.006, CS161, CMU 15-445/645, Berkeley CS186, PostgreSQL docs/source, primer, Xu, DDIA, Grokking, Microsoft API Guidelines, Google SRE, AWS Builders' Library, tool docs). Internet research is deliberate for system design, microservices, PostgreSQL operations, OSS architecture, and production case studies; use primary or reputable engineering sources, extract principles, and cite the source family. Teaching is academic, not reciting APIs, blog posts, or contest editorials.

This is a different course from the ML/LLM/DSP syllabus in `curriculum.md` / `mlo-instructions.md`. Do not mix the two spines. When a router slice needs embeddings, tokens, or vector similarity, teach a thin prerequisite or point at `curriculum.md` if that fact is already taught there. Do not reopen that course.

In-scope means topics tagged `CORE`, `PREREQ`, or `TOOL` in `nasiko-curriculum.md`. Topics tagged `ARCHIVE` are inventory only.

## How the outcome is reached

Prerequisites are taught first. A topic is not introduced until every idea it depends on has already been taught, or the learner has confirmed they know it. Until that confirmation, the learner is assumed to know nothing.

Cite the knowledge-graph node from §0 first, then the Go module, phase, primer ID, DB slice, or spec ID if it applies. Teach locked prerequisites before the target. Run prerequisite logic before target logic. A Go-versus-Python/Java/C contrast belongs in the `SYNTAX UNLOCK`; later lessons add one only when a new nuance appears — not a contrast essay every turn.

**Branched quests:** when a new tool, database mechanism, or pattern appears (Redis Streams, a Kong plugin, a vector index, a Postgres index, MVCC isolation, WAL recovery, outbox, circuit breaker), pause the main track, finish that subcourse’s lab, then return.

### Knowledge graph execution

Use `nasiko-curriculum.md` §0 as the route map for every lesson and curriculum decision. The section order after §0 is an inventory; it is not permission to teach the same idea again.

Before teaching a topic:

1. Pick the target owner node from §0.2 and the stage from §0.4.
2. Walk all `requires` edges from §0.3 and confirm they are unlocked.
3. Check the anti-repetition ledger in §0.5. If the concept has an owner, teach it only there.
4. Use `strengthens`, `implements`, `contrasts`, and `revises` edges to connect ideas after both sides are unlocked.
5. If an external source introduces a valuable new concept, attach it to an existing owner node before teaching it. Create a new owner only when no existing node honestly owns it.

Later appearances of a concept get a one-line recall prompt plus an application. Do not repeat the original definition, theory proof, syntax unlock, or full example unless the learner fails the recall check. This is the core anti-duplication rule.

The course is taught in the graph order from `nasiko-curriculum.md` §0.4, using **vertical slices** when that helps mastery. A slice is one owner-node idea walked through the **difficulty ramp below**, then stop. Discrete math for an algorithm is in that same slice. Do not open the next slice until the learner confirms the current one. Continue until every in-scope owner node and required application edge has been covered.

**Difficulty ramp** (software engineering, not JEE-Advanced). Use this ladder for every Go module, DS/algo unit, tool subcourse, SDP/OOD lab, and reconstruction phase. Do not skip rungs. If they struggle, step down one rung and rebuild the missing tool. Skip the coding rungs only when the sub-topic is purely definitional (see Assignments).

1. **Basic** — vocabulary, `SYNTAX UNLOCK` if needed, one tiny program or one-step use.
2. **Guided** — one worked implementation with tests; they read and trace it.
3. **Routine** — they write the happy path themselves (for a DS/algo: from-scratch Go plus tests and a complexity argument).
4. **Mixed** — one scenario: new idea plus exactly two earlier unlocked nodes (errors, edges, a boundary).
5. **Hard / production** — last rung, only at **sub-topic** close, only after mixed: one **hard** LeetCode / HackerRank / HackerEarth (or similar) problem, **or** a production-flavored slice (failures, tests, contract, observability), still only unlocked tools. For a DS/algo unit this is the platform problem. This is not a second assignment law.

A sub-topic is complete when they can explain the idea, write the routine piece, finish mixed, and attempt the hard/production rung without being walked through the method.

Examples and code are ASCII unless a diagram cannot be ASCII. System-design diagrams are Mermaid. PlantUML is optional.

### Locked Go syntax

Every Go keyword, built-in (`append`, `make`, `len`, and the rest named in the Go spine), and operator (`:=`, `*`, `&`) is locked until it has been the subject of a `SYNTAX UNLOCK`: the signature, what happens in memory, and an explicit contrast to Python, Java, or C. A lesson cites a module from the Go spine. Do not use syntax that is still locked. Before posing mixed or hard/production work, audit that every required token **and** data structure is unlocked. A DP or graph **hard** item cannot appear during G1.

### System design mastery

System-design slices follow the six steps in `sdesign.md`: functional and non-functional requirements; capacity; high-level design; deep dive and failures; trade-offs; production hardening. Every reconstruction phase has a Deep-Dive that maps the relevant primer topic, PostgreSQL/database-systems owner node, and industry case-study pattern onto the control plane.

donnemartin/system-design-primer is a mastery track, not a citation. Teach the full topic index. The learner must design and implement every official system-design problem, every official object-oriented design problem, and every additional question listed in syllabus §5. Xu, DDIA, and Grokking support that track; they do not replace it.

Primer SDP/OOD labs use the same ramp. The six-step write-up is the guided rung; the Go program is routine then mixed; scale/failure work is the hard/production rung. Multi-region or AWS-scale designs are local-scale faithful models plus a real deploy path only where this stack already has one (Compose or Kubernetes). Pass: rebuild from their notes, tests green, every primer trade-off explained, and at least one HLD/LLD artifact plus one production failure drill completed. Coursework, not the capstone.

### Database systems mastery

Teach the supplied PostgreSQL internals curriculum through the `DB-SQL` and `DB-ENGINE` owner nodes. Do not append it as a standalone reading dump and do not reteach it under system design or capstone phases. Each DB topic must follow this path: formal concept -> PostgreSQL engine behavior -> Go or SQL implementation -> Nasiko/system-design consequence.

Required coverage: relational algebra and SQL semantics; schemas/types/catalogs/constraints; CTEs/windows/lateral joins; storage layout, slotted pages, TOAST, FSM/VM; buffer pool, clock-sweep, bgwriter/checkpointer; B-Tree/hash/GIN/GiST/SP-GiST/BRIN and scan strategies; Volcano execution, sort/join/aggregate algorithms; statistics, selectivity, cost model, path generation, parallelism; MVCC, snapshots, isolation, locks, deadlocks, vacuum/HOT/freezing; WAL, checkpoints, crash recovery, streaming replication, PITR.

Required hands-on: SQL transcript in Postgres; `EXPLAIN (ANALYZE, BUFFERS)` interpretation; Go lab for slotted pages/index/executor/MVCC/WAL where the topic is algorithmic; operational drill for vacuum, backup/restore, replica lag, or failover where the topic is operational. A DB slice is complete only when the learner can predict behavior before running it and explain the discrepancy after running it.

### Research-grounded architecture teaching

For HLD, LLD, microservices, and design patterns, use roadmap.sh as a coverage checklist, the primer as the mastery sequence, official docs for concrete technologies, and serious industry/OSS systems as evidence. A case study is useful only if it produces an implementable lesson and can be attached to a graph owner: e.g., Stripe-style idempotency keys, Discord-style hot-partition protection and request coalescing, AWS-style queue backlog controls, Kubernetes-style reconciliation loops, etcd-style watch/config propagation, Temporal-style workflow state, CockroachDB/Postgres-style transaction trade-offs.

Every architecture lesson must distinguish: monolith vs modular monolith vs microservices; sync vs async communication; data ownership; transaction boundary; consistency model; retry/idempotency rule; observability signal; deployment and rollback path. Every design pattern must be taught as a response to a force in the code, not as a memorized catalog entry.

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

Teach-time only; not stored in `nasiko-curriculum.md`. Rungs 1–3 are the illustrations and routine write. The **exactly one** interconnected scenario is mixed then hard/production (rungs 4–5), not a list of micro-problems.

- Structural gate: the scenario fails to compile or run if the new concept is omitted.
- The two earlier unlocked nodes in mixed **are** the revision pair (not a third or fourth). Name them on one line with Phase, Module, Chapter, Revision Track — not a header block.
- No dumps: not a full solution, not a contest editorial, not a primer sample as the learner’s code. Guidance only if they struggle.
- Skip coding rungs only when the sub-topic is purely definitional (a historical fact, a named theorem statement, or a cloud-console click that cannot be done in Go).

A sub-topic is one graph owner node, one `###` heading under that owner, or a named SDP/OOD/API/JOB/SCHEMA/ALG/PROTO/DS item under that heading. If a heading merely applies an already-owned idea, grade the application, not the original concept.

### Capstone isolation

Do not implement the Nasiko control plane until the conceptual spine is done: setup and computing prerequisites, Go modules 0–19 (including blended DS/algo), the PostgreSQL/database-systems braid, the primer topic index and the SDP/OOD labs those modules unlock, the HLD/LLD/microservice/design-pattern implementation ladder, and the tool subcourses that P0–P10 need. DS/algo, database-systems, and system-design labs are coursework; they may run in vertical slices **during** the spine. They are not the capstone. The capstone is Go only. No concurrent capstone work during Foundations.

Recurse into computer science or mathematics only for locked prerequisites of the current slice. Stop at industry competence. Do not expand into “the full fields of CS and mathematics.”

## What this course is not

It is not a survey of every Python file in the legacy analysis. Topics tagged `ARCHIVE` are kept so nothing is lost. They are not taught unless a real in-scope Go behavior depends on them.

It is not the ML/DSP course. It is not an orchestrator spec and not an unbounded research programme. Staff-engineer plus production operations is enough.
