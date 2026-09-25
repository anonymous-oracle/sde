# The Forward Deployed Engineer Companion — Claude Applications in Production and the CCDV-F Certification
Companion to the main course, "The Consolidated Cloud Mastery Curriculum".
Built September 25, 2026, from the learner's Forward Deployed Engineer and CCDV-F brief (the material only; its teaching rules joined the course guide's rules and its stage plan joined the main course's order). Sources: Anthropic's documentation for the Claude API, Claude Code, the Claude Agent SDK and prompt engineering, as current on the day a module is taught `(verify)`; the Model Context Protocol specification, at the revision current when taught `(verify)`; the JSON-RPC 2.0 specification (2010); JSON Schema, draft 2020-12; RFC 8259 (JSON); RFC 9110 and RFC 9112 (HTTP semantics, HTTP/1.1); the WHATWG HTML Living Standard, section "Server-sent events"; RFC 6749 (OAuth 2.0), RFC 7636 (PKCE) and RFC 9728 (OAuth 2.0 Protected Resource Metadata); Anthropic's engineering essays "Building Effective Agents" (Schluntz and Zhang, December 2024), "Introducing Contextual Retrieval" (September 2024), "Effective Context Engineering for AI Agents" (2025) and "Writing Effective Tools for AI Agents" (2025) `(verify)`; Bai et al., "Constitutional AI: Harmlessness from AI Feedback" (2022); Karpathy's lecture series *Neural Networks: Zero to Hero* (micrograd, makemore, nanoGPT) as the pattern for the LB builds; Willison, "The Lethal Trifecta for AI Agents" (June 2025); Anthropic Academy's free courses Building with the Claude API, Claude Code in Action, Introduction to Model Context Protocol and Introduction to Agent Skills `(verify)`; and a community summary of Anthropic's CCDV-F Exam Guide v1.0 (effective July 2026), to be checked against the official guide `(verify)`.

---

## 0. Read this first — what this part adds

This part follows the rules of the course guide (rules 0.1–0.5). This section holds only what is particular to it.

### 0.1 What this part owns

Main course D5 names the work; this part supplies it. It teaches building production applications with Claude, the role that builds them inside customer organizations (the **Forward Deployed Engineer**, FDE), and the preparation for Anthropic's **Claude Certified Developer – Foundations** exam (CCDV-F). It owns: the from-scratch builds of the models that D2 and D4 explain (LB-1…LB-7); TypeScript and the wire formats of LLM applications (FDE-01…FDE-03); the Claude API, prompt, context and output engineering, tools and MCP, workflows and agents, Claude Code, the Claude-side security controls, evaluation and debugging, application architecture and the delivery craft (FDE-04…FDE-28); three checkpoints (FDE-CK1…FDE-CK3); five capstones (FDE-CAP1…FDE-CAP5); and the CCDV-F preparation (§15).

The theory under it belongs to other parts and is recalled in one line, never re-taught: how LLMs generate text, attention, decoding and RLHF (D4); backpropagation (D2); offline metrics and online experiments (D1, D3); retries, backoff and graceful degradation (the Design Patterns companion's ARCH-12); rate limiting (the Cloud Cybersecurity companion's AB-01); the attacks on AI applications (its AI-01…AI-05); OAuth, tokens and sessions (its AU modules; the Go companion's GO-28); HTTP and TLS (A5); CI/CD (C4); observability (C6). Rule 0.3 has the rows.

### 0.2 Rules particular to this part

1. **Binding.** LB-1…LB-7 ride D2 and D4 (§2). Everything else is taught in D5, in the order of its teaching blocks D5.F1…D5.F7 (main course D5), once the dependency gate (§16) is met. The capstones and the CCDV-F preparation close D5.
2. **Three passes** (rule 0.2). A card with a **By hand** line is taught in that order: the toy by hand, then its **Library and production** line, which names what the library handles that the toy did not. Anything cryptographic stays learning-only (rule 0.5).
3. **Exam tags.** Each card's **Exam** line names the CCDV-F domain it serves (CF1…CF8, §3.2), so exam coverage stays visible. Teach to the job; tag to the exam. Evaluation is 2.6% of the exam and most of the job, so it is taught at the job's depth.
4. **Discovery in every lab.** Each lab opens with a **customer ask**. Before building, the learner states the real problem behind the ask in one sentence, and one measurable success criterion (FDE-22). Where a lab says so, the tutor plays the customer.
5. **Volatile facts.** Model names, prices, context-window sizes, rate limits, beta features and the exam's details change often. They carry `(verify)`, are checked against Anthropic's live documentation and the Models API before a lab or the exam relies on them, and are never taught from memory. Lab code reads the model ID from configuration, in one place.
6. **Recorded first, live second** (rule 0.5). Each lab runs first against recorded responses `[local]`: the learner records one real response per case once, then replays it in tests. It runs live `[credit ~$X]` only inside a workspace whose spend limit is set before the first call.
7. **Numbers and application.** In this part's layer of a session (rule 0.4.2), the Numbers step is one token, cost or latency estimate, computed from a `usage` block or from token counting; the application item is the card's lab.
8. **TypeScript lab acceptance** (rule 0.4.9). A TypeScript lab is accepted when `tsc --noEmit` is clean under `"strict": true`, the tests pass, every promise is awaited or deliberately handled, and untrusted input is parsed through a schema before use.

### 0.3 Notation

`LB-n` a from-scratch model build · `FDE-nn` a module · `FDE-CKn` a checkpoint · `FDE-CAPn` a capstone · `CFn` a CCDV-F exam domain (§3.2). This part's academic pass is main course D5.D, with its problem set D5-P1…D5-P7 (rule 0.4.10). Check keys are in Appendix K.

Card fields: **Core** · **By hand** (when the card has a toy) · **Library and production** · **GCP lens** · **Lab** with its Lab Reality tag, opening with the customer ask · **Exam** · **Check**.

---

## 1. Coverage ledger

The brief this part was built from asked for more than this part holds. Each item is taught once, by its owner; this table says where.

| Brief area | Taught by | This part adds |
|---|---|---|
| How computers run programs; the terminal | A1 (data representation), A6 (processes, files, the shell), A3.P2 (Bash) | — |
| Python from zero: values, control flow, functions, scope, data structures, classes, errors, modules | A3.P1; A3.D1–A3.D2 (semantics, recursion) | — |
| From-scratch builds of Stage A: a hash map, binary search, merge sort, a tiny test runner | A4 (the build line; the System Design Primer companion's O01 is the hash map); A3 (the test runner before pytest) | — |
| Git, virtual environments, pytest; the "tested CLI pushed to a Git host" checkpoint | A3, A11 | — |
| Vectors, matrices, calculus, probability, softmax; the hand-computed softmax and gradient step | A2 (A2.3, A2.D5, A2.D9–A2.D11, with its build lines and checkpoint) | — |
| Go fundamentals and concurrency; a worker pool | The Go companion's GO-01…GO-19 (GO-19 is the worker pool) | — |
| TCP/IP, DNS, ports, TLS; HTTP | A5 | — |
| An echo server on raw TCP; HTTP/1.1 over raw sockets in Go and Python; the raw-socket service rewritten on `net/http` | The Go companion's GO-21 build lab | — |
| JSON, JSON Schema, JSON-RPC, Server-Sent Events; a JSON parser and an SSE parser | — | FDE-03 |
| Timeouts, retries, backoff with jitter; rate limiting and a token bucket; idempotency | The Design Patterns companion's ARCH-12; the Cloud Cybersecurity companion's AB-01 and its SEC-E4.3; the Go companion's GO-17, GO-19, GO-29 | FDE-04 recalls them for 429 and 529 |
| SQL, schemas, indexes, transactions; a key-value store with a write-ahead log | A8 and the SQL companion (its DB-10 is the write-ahead-log toy) | — |
| API keys, sessions, OAuth 2.0, JWT, SSO and OIDC; JWT signing by hand, learning only | The Cloud Cybersecurity companion's AU modules and CR-05…CR-07; the Go companion's GO-28 | FDE-21 (keys and identity for LLM applications) |
| Linux and containers; cloud and delivery, CI/CD, secrets, per-environment configuration; a minimal CI script | A6, C1, C4 (with its hand-written CI script), Track B, the Cloud Cybersecurity companion's WL-05 | — |
| Observability; request-tracing middleware | C6; the Go companion's GO-21 (request-ID middleware) and GO-24 (OpenTelemetry) | FDE-24 (tracing an LLM application) |
| TypeScript, async, Node, Zod, basic React | — | FDE-01, FDE-02 |
| LLMs from scratch: tokenization, bigram models, neural networks, attention, generation, frontier models, embeddings and retrieval | D2, D4 (the concepts and their academic pass) | LB-1…LB-7, FDE-CK1 (the builds) |
| The Claude API; prompt and context engineering; tools and MCP; agents; Claude Code; security; evals; application design and the FDE craft | — | FDE-04…FDE-28, FDE-CK2, FDE-CK3 |
| Capstones; CCDV-F preparation; interviews; a track record | — | §14, §15 |
| Teaching rules, retention, the session protocol and the progress log | The course guide (rules 0.2, 0.4 and 0.4.8) | — |

---

## 2. Stitch table — where this binds into the main course

| Main-course module | This part's modules taught alongside | Notes |
|---|---|---|
| D2 Deep Learning | LB-3 | D2 owns backpropagation and D2.D1 its theory; LB-3 is the build |
| D4 Generative AI, LLMs & Agents | LB-1, LB-2, LB-4, LB-5, LB-6, LB-7; FDE-CK1 closes D4 | D4 owns the concepts and D4.D1–D4.D5 the theory; the LB cards are the builds (D4's teaching-block note gives the pairing). The SQL companion's AN-07 owns search and vectors in Postgres |
| **D5 Building with Claude** | **FDE-01…FDE-28**, FDE-CK2, FDE-CK3, FDE-CAP1…FDE-CAP5, §15 | Primary landing, in teaching blocks D5.F1 FDE-01…FDE-03 · D5.F2 FDE-04…FDE-07 · D5.F3 FDE-08…FDE-10 · D5.F4 FDE-11…FDE-14 · D5.F5 FDE-15…FDE-19 · D5.F6 FDE-20…FDE-24 · D5.F7 FDE-25…FDE-28 |

D5's cards recall A5 (HTTP), A7 (APIs), A9 (idempotency, at-least-once delivery), A10 and the Cloud Cybersecurity companion (attacks), C4 (CI), C6 (observability) and the Go companion (services) in one line each, at the point of use.

---

## 3. The role and the exam

### 3.1 The Forward Deployed Engineer

An FDE builds and runs production software for one customer or a small set of customers, working with them in the field rather than through ticket hand-offs. The title began at Palantir. At Anthropic, FDEs sit on the Applied AI team, embed with strategic customers, build production applications with Claude inside customer systems, and deliver artifacts such as MCP servers, subagents and agent skills `(verify)`. Postings ask for production LLM experience (advanced prompting, agent development, evaluation frameworks, deployment at scale), strong Python and ideally TypeScript or Java, high agency in ambiguous organizations, frequent travel to customer sites, and several years of customer-facing engineering `(verify)`.

The distinctive skill is **discovery**: peeling back a customer's request to find the real problem, and giving them the right solution rather than the one they asked for. It is practised in every lab (rule 4 of §0.2) and taught as a method in FDE-27.

### 3.2 CCDV-F, the exam

Facts from a community summary of the Exam Guide v1.0, effective July 2026; every one is checked against the official guide before booking `(verify)`. Fifty-three multiple-choice and multiple-response items in 120 minutes, at Pearson VUE (online or at a test centre). Passing is a scaled score of 720 on a 100–1,000 scale. The target candidate has 1–5 years of engineering, six months or more hands-on with Claude or a similar model, Python or TypeScript, and fluency with REST APIs and command-line tools. Registration runs through Anthropic's Partner Academy, for members of the Claude Partner Network; the learner's employer is not one, so §15 checks whether public registration has opened `(verify)`.

| Domain | Weight | Sub-skills (weight) | Taught in |
|---|---|---|---|
| CF1 Agents & Workflows | 14.7% | Agent Architecture (4.5), Agent Construction with Claude (5.3), Agent Patterns & Frameworks (4.9) | FDE-15…FDE-17 |
| CF2 Applications & Integration | 33.1% | Understanding Requirements (3.4), Systems Life Cycle (2.8), Claude API Mechanics (6.8), Software Engineering Foundations (7.4), Claude Application Design (8.6), Configuration Management (4.1) | FDE-01…FDE-06, FDE-26…FDE-28; the main course's Tracks A–C and the Go companion for the foundations |
| CF3 Claude Code | 3.1% | Claude Code Operation (3.1) | FDE-18, FDE-19 |
| CF4 Eval, Testing & Debugging | 2.6% | Debugging & Error Handling (2.6) | FDE-22…FDE-24 |
| CF5 Model Selection & Optimisation | 16.8% | LLM Fundamentals (5.2), Technical Fundamentals (6.1), Model Selection & Trade-offs (2.7), Cost & Token Management (2.8) | LB-1…LB-7 with D4; FDE-07 |
| CF6 Prompt & Context Engineering | 11% | Context Engineering (3.8), Prompt Engineering (4.6), Output Handling (2.6) | FDE-08…FDE-10 |
| CF7 Security & Safety | 8.1% | AI Application Security (3.2), Guardrails & Safe Deployment (2.3), Claude Hooks (1.0), Identity, Secrets & Key Management (1.6) | FDE-20, FDE-21; FDE-18 (hooks) |
| CF8 Tools & MCPs | 10.6% | Tool Implementation (4.4), MCP Server Development (2.1), Agentic Customisation (4.1) | FDE-11…FDE-14 |

### 3.3 Exam against job

The exam weights application mechanics and model choice; the job is judged on whether the system works for the customer, which is measured by evaluation. The course teaches the job's full depth everywhere and uses the CF tags only to make sure nothing on the exam is left untaught.

---

## 4. LLMs from scratch — the builds under D2 and D4

Each build is Python, small enough to read in one sitting, and follows the theory its main-course owner teaches; the tutor recalls that theory in one line and does not re-teach it. They run on a laptop CPU `[local]`.

#### LB-1 · A byte-pair-encoding tokenizer — stitch: D4
- [ ] done
- **Core:** characters against subwords against bytes; byte-level BPE training (count adjacent pairs, merge the most frequent, record the merge, repeat) and encoding (apply merges in the order learned); special tokens; why the same text costs different token counts in different languages and why code and numbers tokenize badly; tokens as the unit of price, limits and latency. D4.D1 owns the definition.
- **By hand:** train BPE on a few hundred kilobytes of text to a 512-token vocabulary; `encode` and `decode` with the round-trip property `decode(encode(s)) == s` for every UTF-8 string, tested on emoji and mixed scripts.
- **Library and production:** a production tokenizer (for example `tiktoken` or Hugging Face `tokenizers`) adds pre-tokenization rules, a fast merge implementation and a fixed vocabulary; Claude's own tokenizer is not public, so production counts come from the token-counting endpoint (FDE-07), never from another model's tokenizer.
- **GCP lens:** Vertex AI bills Claude by the same token counts `(verify)`; a token budget is a cost line in the design.
- **Lab `[local]`:** customer ask: "why did our Japanese support tickets cost three times more than the English ones?" Measure tokens per character for English, Japanese and Go source code on your tokenizer and explain the ratio.
- **Exam:** CF5 (LLM Fundamentals; Cost & Token Management).
- **Check:** your BPE merges the pair ("t", "h") before ("th", "e"). Why must `encode` apply merges in the learned order rather than the longest match first?

#### LB-2 · A bigram language model — stitch: D4
- [ ] done
- **Core:** next-token prediction as a probability table; counting, smoothing and normalizing; sampling from the table; the negative log-likelihood loss and why it is the cross-entropy of D4.D1; the same model as a single linear layer trained by gradient descent (A2's minimizer recalled).
- **By hand:** a character-level bigram model on a list of names — once by counting, once as a trained 27 × 27 weight matrix — reaching the same loss both ways.
- **Library and production:** a framework (PyTorch) replaces the hand-written gradient only after LB-3 has built one.
- **GCP lens:** none; this is a laptop lab.
- **Lab `[local]`:** customer ask: "can a model this small autocomplete our product codes?" Train it on a synthetic list of codes, report the loss, and sample ten.
- **Exam:** CF5 (LLM Fundamentals).
- **Check:** a bigram model gives probability 0 to a pair it never saw. What does that do to the loss on a test set, and what fixes it?

#### LB-3 · An autodiff engine and a small neural network — stitch: D2
- [ ] done
- **Core:** a scalar `Value` that records its parents and the operation that made it; reverse-mode differentiation by topological sort (D2.D1 owns the theory); a neuron, a layer and a multilayer perceptron; a training loop of forward pass, zeroing gradients, backward pass and update.
- **By hand:** the engine in about a hundred lines, gradients checked against finite differences to 1e-6; a two-layer network that learns a small classification set.
- **Library and production:** PyTorch's autograd is the same algorithm on tensors, with fused kernels and a GPU; the learner names three things it does that the toy does not (tensors, memory reuse, numerically stable fused operations).
- **GCP lens:** training at scale runs on Vertex AI custom training with accelerators `[plan-only]`; the lab never does.
- **Lab `[local]`:** customer ask: "our data scientist says the gradient is wrong." Given a network with one deliberately broken backward rule, find it with a finite-difference check.
- **Exam:** CF5 (LLM Fundamentals).
- **Check:** a node `c = a * b` is used twice later in the graph. Why must the backward pass add into `a.grad` rather than assign to it?

#### LB-4 · A tiny GPT — stitch: D4
- [ ] done
- **Core:** token and position embeddings; one head of causal self-attention, then several; the residual stream, layer normalization and the MLP block; the context window as the fixed length of the position table; training on a small text corpus. D4.D2 owns the theory.
- **By hand:** a character-level decoder-only Transformer in PyTorch (autograd now allowed, LB-3 having built it), trained on a few megabytes of text on a CPU until its samples show structure.
- **Library and production:** the same shape as production models, at about a millionth of the size; the learner lists what production adds (tokenizer, scale, mixed precision, the KV cache, instruction tuning and preference training — D4.D5).
- **GCP lens:** none; this is a laptop lab.
- **Lab `[local]`:** customer ask: "why can't the model read our 400-page contract in one go?" Show, with your model, what happens to a token beyond the context length, and connect it to the context windows of FDE-09.
- **Exam:** CF5 (LLM Fundamentals; Technical Fundamentals).
- **Check:** remove the causal mask and train again. The training loss falls much faster. Why is that model useless for generation?

#### LB-5 · A sampler — stitch: D4
- [ ] done
- **Core:** greedy decoding, temperature, top-k and top-p (nucleus) sampling, stop sequences and a maximum length (D4.D3 owns the theory); why sampling makes answers vary and why a fluent answer can be false (hallucination as sampling from a distribution with no truth check).
- **By hand:** a sampler for LB-4 with temperature, top-k, top-p and stop sequences, and a seeded run that is reproducible.
- **Library and production:** the Claude API exposes some of these knobs and not others, and current models restrict some combinations `(verify)`; FDE-05 teaches which, and why reproducibility at an API is not guaranteed even at temperature 0.
- **GCP lens:** none.
- **Lab `[local]`:** customer ask: "the model gives different answers to the same question." Show the distribution of ten samples at three temperatures and write the two-sentence explanation you would give the customer.
- **Exam:** CF5 (LLM Fundamentals).
- **Check:** with top-p = 0.9, the most likely next token has probability 0.95. How many tokens can be sampled at that step?

#### LB-6 · Frontier models — stitch: D4
- [ ] done
- **Core:** pretraining, then instruction tuning and preference training (D4.D5 recalled); Constitutional AI — a model critiques and revises its own outputs against written principles, and AI feedback against those principles replaces much of the human preference labelling (Bai et al., 2022); extended and adaptive thinking — the model spends output tokens reasoning before it answers, controlled by an effort setting on current models `(verify)`; multimodality (images and PDFs in, text out); latency as time to first token plus output tokens divided by throughput (D5.D3), and why bigger models are slower per token.
- **By hand:** none; this card is explanation and measurement.
- **Library and production:** measured through the API in FDE-05 and FDE-07: time to first token and tokens per second for two model sizes, with and without thinking.
- **GCP lens:** the models offered on Vertex AI and their regions `(verify)`.
- **Lab `[credit ~$1]`:** customer ask: "our chat feels slow." Measure time to first token and total time for one prompt on a small and a large model, streamed and not streamed, and say which change the user would notice.
- **Exam:** CF5 (LLM Fundamentals; Model Selection & Trade-offs).
- **Check:** streaming cuts the time to the first visible word from 6 s to 0.7 s. Did it change the total time to the last word, and why?

#### LB-7 · Embeddings and retrieval — stitch: D4
- [ ] done
- **Core:** embeddings as vectors whose geometry encodes similarity; cosine similarity (D5.D1); BM25 as the lexical ranker; brute-force nearest neighbours and why approximate indexes exist; hybrid search by reciprocal rank fusion; recall@k as the measure (D4.D5 owns retrieval-augmented generation as a concept).
- **By hand:** BM25 over a few thousand short documents, a brute-force cosine search over precomputed embeddings, and reciprocal rank fusion of the two; recall@10 on twenty labelled queries for each.
- **Library and production:** a vector index (Vertex AI Vector Search, `pgvector` in Postgres — the SQL companion's AN-07 — or a managed store) replaces brute force when the collection outgrows memory or latency; an embedding model comes from a provider, since Anthropic does not offer one `(verify)`.
- **GCP lens:** Vertex AI Vector Search, or AlloyDB and Cloud SQL for PostgreSQL with `pgvector` `(verify)`; Vertex AI text-embedding models.
- **Lab `[local]`:** customer ask: "search can't find error code E4012 even though it is in the manual." Show that the vector search misses it, BM25 finds it, and the hybrid keeps both kinds of hit.
- **Exam:** CF5 (Technical Fundamentals); CF2 (Claude Application Design).
- **Check:** why does a pure embedding search often miss an exact product code that BM25 finds at rank 1?

#### FDE-CK1 · Checkpoint — why a model loses track in a long context — stitch: D4
- [ ] done
- **Task:** explain in plain language, with your LB-4 model and a retrieval experiment, why information far back in a long context can be lost: the fixed context length (LB-4), attention spread over many positions (D4.D2), and the measured "lost in the middle" effect (D5.D3). Place one fact at the start, middle and end of long prompts to a Claude model, twenty trials each `[credit ~$2]`, and report accuracy by position with its Wilson interval (D5.D2).
- **Passes when:** the explanation separates the hard limit (the window) from the soft one (retrieval accuracy inside the window), and the measured intervals are reported honestly, including when they overlap.

---

## 5. TypeScript and the wire formats

#### FDE-01 · TypeScript and Node — stitch: D5
- [ ] done
- **Core:** why TypeScript: the Claude and MCP SDKs, most web clients and many MCP servers are TypeScript-first. Types erased at run time; structural typing (compare Go's interfaces, the Go companion's GO-11); `strict` mode; union and literal types and narrowing; `unknown` against `any`; generics; modules (ES modules against CommonJS); Node's event loop — one thread, a task queue, and I/O that never blocks it; promises and `async`/`await`; `Promise.all` and its failure mode; `AbortController` for cancellation (compare `context`, the Go companion's GO-17); `npm`, `package.json`, lockfiles and `npx`.
- **Contrast:** **Python** — `async` in Python needs an event loop you start; in Node it is always running. **Go** — goroutines block cheaply; in Node a blocking loop freezes every request. A type annotation in TypeScript is never checked at run time, so data from the network must be parsed (FDE-02).
- **Library and production:** Node's LTS release, `tsc`, a test runner (`node --test` or Vitest), ESLint; the version is the one the project's lockfile pins `(verify)`.
- **GCP lens:** Cloud Run runs a Node container the same way as a Go one (the Go companion's GO-25 recalled for the image).
- **Lab `[local]`:** customer ask: "our Node service stops answering when one report runs." Reproduce it with a CPU-bound loop in a handler, then fix it by moving the work off the event loop.
- **Exam:** CF2 (Software Engineering Foundations).
- **Check:** `const r = await Promise.all([a(), b(), c()])` and `b()` rejects after 10 ms while `a()` runs for 5 s. What does the caller see, and when, and what is still running?

#### FDE-02 · Runtime validation with Zod, and a minimal React client — stitch: D5
- [ ] done
- **Core:** parse, don't trust: a Zod schema validates unknown input and produces a typed value; `safeParse` and error paths; deriving a TypeScript type from a schema so the two cannot drift; the same schema as JSON Schema for tools and structured outputs (FDE-03, FDE-10). React at the depth an FDE demo needs: components as functions of state, `useState` and `useEffect`, rendering a stream as it arrives, and why the API key never reaches the browser (a server route calls Claude; rule 0.5).
- **By hand:** a twenty-line validator for one object shape (required keys, types, a string length limit) before Zod.
- **Library and production:** Zod adds composition, refinements, readable error paths and JSON Schema export; React is used through a framework's starter only as far as the demo needs.
- **GCP lens:** the client and its server route deploy as one Cloud Run service; the key comes from Secret Manager.
- **Lab `[local]`:** customer ask: "we need a demo by Friday that our CFO can click." A page that streams an answer from a server route, with the route's input parsed by Zod.
- **Exam:** CF2 (Software Engineering Foundations; Claude Application Design).
- **Check:** a teammate writes `const body = req.body as Order`. What does that line check at run time, and what should replace it?

#### FDE-03 · Wire formats: JSON, JSON Schema, JSON-RPC 2.0 and Server-Sent Events — stitch: D5
- [ ] done
- **Core:** JSON's grammar (RFC 8259) and its traps: no comments, no trailing commas, numbers without a size limit (a 64-bit ID loses precision in JavaScript), duplicate keys left undefined. JSON Schema: `type`, `properties`, `required`, `enum`, `additionalProperties`, `$ref`, and its role as the contract for tool inputs and structured outputs. JSON-RPC 2.0: requests with `id`, notifications without one, `result` against `error` with `code` and `message`, batches, and the reserved codes (−32700 parse error, −32600 invalid request, −32601 method not found, −32602 invalid params, −32603 internal error) — the envelope of MCP (FDE-13). Server-Sent Events: a long HTTP response of `text/event-stream`, events separated by a blank line, `event:`, `data:` (several `data:` lines join with a newline), `id:`, `retry:`, and lines starting with `:` as comments — the stream format of the Messages API (FDE-04).
- **By hand:** a recursive-descent JSON parser for objects, arrays, strings with escapes, numbers, `true`, `false` and `null`, tested against the standard library on a shared corpus; an incremental SSE parser that accepts arbitrary chunk boundaries (an event split across two network reads) and yields `(event, data)` pairs.
- **Library and production:** the standard library's JSON; the SDKs' stream parsers; the learner names what the toys skip (Unicode surrogate pairs, deep-nesting limits, the byte-order mark, reconnection with `Last-Event-ID`).
- **GCP lens:** Cloud Run supports streamed responses; a proxy or load balancer that buffers responses breaks SSE, which is one of the first things to check in a customer's network `(verify)`.
- **Lab `[local]`:** customer ask: "our proxy team says streaming is 'just HTTP'; answers arrive all at once." Feed your SSE parser a recorded stream in 1-byte, 7-byte and whole-body chunks and show the events are identical; then explain what a buffering proxy does to the user.
- **Exam:** CF2 (Software Engineering Foundations; Claude API Mechanics); CF8 (MCP Server Development).
- **Check:** a network read ends in the middle of a `data:` line. What must your SSE parser do with the partial line?

---

## 6. The Claude API

#### FDE-04 · The Messages API by hand — stitch: D5
- [ ] done
- **Core:** one endpoint, `POST /v1/messages`, with the headers `x-api-key`, `anthropic-version` and `content-type: application/json`. The body: `model`, `max_tokens`, `messages` (alternating `user` and `assistant` turns, each with a string or a list of content blocks), and `system` as a top-level field, not a role. The response: `content` blocks, `stop_reason` (`end_turn`, `max_tokens`, `stop_sequence`, `tool_use`, `pause_turn`, `refusal`) and `usage` (`input_tokens`, `output_tokens`, and the cache counters of FDE-07). With `"stream": true` the response is SSE (FDE-03): `message_start`, then for each block `content_block_start`, `content_block_delta` events (`text_delta`, and `input_json_delta` for tool input) and `content_block_stop`, then `message_delta` (the `stop_reason` and final output tokens) and `message_stop`; `ping` events keep the connection alive, and an `error` event can arrive mid-stream. Errors carry a type: 400 `invalid_request_error`, 401 `authentication_error`, 403 `permission_error`, 404 `not_found_error`, 413 `request_too_large`, 429 `rate_limit_error` (with a `retry-after` header), 500 `api_error`, 529 `overloaded_error` `(verify)`. Rate limits are per organization tier and per model, in requests and tokens per minute, reported in response headers `(verify)`.
- **By hand:** a Python client on a plain HTTP library: one call, then streaming through your FDE-03 parser, then retries — retry 429, 529 and 5xx with exponential backoff and full jitter, honouring `retry-after`, never retrying 400, 401, 403 or 413 (the Design Patterns companion's ARCH-12 and the Go companion's GO-19 recalled) — and a cost calculator that turns `usage` into dollars from a price table read from configuration `(verify)` the prices.
- **Library and production:** FDE-05's SDKs do all of this, including retries (a default of two for connection errors, 408, 409, 429 and 5xx `(verify)`); the toy exists so the learner can read a failing trace.
- **GCP lens:** on Vertex AI the same body goes to a Vertex endpoint with the model in the URL and Google credentials instead of `x-api-key` (FDE-07).
- **Lab `[local]` then `[credit ~$1]`:** customer ask: "the integration fails randomly at 9 a.m." Replay a recorded morning of 429 and 529 responses against your client and show that it recovers without a retry storm; then one live call, with its cost computed from `usage`.
- **Exam:** CF2 (Claude API Mechanics); CF4 (Debugging & Error Handling); CF5 (Cost & Token Management).
- **Check:** a response ends with `stop_reason: "max_tokens"` and the JSON you asked for is cut off. Is retrying the same request the fix? What is?

#### FDE-05 · The SDKs and the anatomy of a request — stitch: D5
- [ ] done
- **Core:** the official Python and TypeScript SDKs (`anthropic`, `@anthropic-ai/sdk`) and Go through its SDK or plain HTTP `(verify)`; typed requests and responses; streaming helpers that assemble the final message; the SDK's retries, timeouts and typed errors. The anatomy of a request: the system prompt sets role and rules; turns alternate; content blocks (`text`, `image`, `document`, `tool_use`, `tool_result`); a response prefilled with the start of an assistant turn is not supported on current models (it returns 400), so structure comes from structured outputs (FDE-10) `(verify)`; `max_tokens` is a hard cap on output, set from the task, not from habit; the sampling parameters that current models accept `(verify)`; adaptive thinking, turned on with a `thinking` field and tuned by an effort setting, returns thinking blocks that must be passed back unchanged in multi-turn tool use `(verify)`.
- **Library and production:** the SDK against the toy of FDE-04: the learner lists what the SDK adds (typed errors, retries with backoff, stream assembly, request IDs for support tickets).
- **GCP lens:** the Vertex AI client class of the same SDK (FDE-07).
- **Lab `[local]` then `[credit ~$1]`:** customer ask: "port our prototype from raw HTTP to something we can maintain." Rewrite the FDE-04 client on the SDK in Python and in TypeScript, with recorded-response tests for both.
- **Exam:** CF2 (Claude API Mechanics).
- **Check:** why does the Messages API put `system` in a top-level field rather than a turn with a `system` role, and what goes wrong if user-supplied text is concatenated into it?

#### FDE-06 · Documents, images and citations — stitch: D5
- [ ] done
- **Core:** image blocks (base64, URL or an uploaded file) and PDF document blocks, and what each costs in tokens `(verify)`; the Files API — upload once, reference by `file_id` in later requests `(verify)`; citations — enable them on a document block and the response carries citation blocks pointing into the document (character or page ranges), which is the grounding a regulated customer asks for; citations cannot be combined with structured outputs `(verify)`; what vision is bad at (small text, counting, precise geometry).
- **Library and production:** the SDK's file and document helpers; a check that every claim in an answer has a citation.
- **GCP lens:** documents stored in Cloud Storage are read by the server and sent as blocks; the file never goes from the browser to the model directly.
- **Lab `[local]` then `[credit ~$2]`:** customer ask: "our analysts need answers from 200-page policy PDFs, and legal needs to see where each answer came from." Answer five questions over one PDF with citations, and flag any sentence without one.
- **Exam:** CF2 (Claude API Mechanics; Claude Application Design).
- **Check:** a customer wants JSON output validated against a schema and a citation for every field. Why can one request not do both, and how would you split it?

#### FDE-07 · Cost, caching, batches and model choice — stitch: D5
- [ ] done
- **Core:** counting tokens before sending (`/v1/messages/count_tokens`); prompt caching — mark a block with `cache_control` and the prefix up to it (in the order tools, then system, then messages) is cached; up to four breakpoints; a minimum cacheable length that depends on the model; a default lifetime of five minutes, refreshed on each hit, with a one-hour option; a write costs more than an uncached input token and a read costs about a tenth `(verify)` the multipliers; any change before a breakpoint invalidates it; `usage.cache_read_input_tokens` shows whether it worked. Message Batches — many requests submitted at once, at about half price, finished within 24 hours, results matched by `custom_id` because they come back in any order `(verify)` the limits. Model choice — larger models against smaller ones on quality, latency and price; routing easy requests to a small model and escalating; pinned model IDs against aliases that move, and what a deprecation notice means for a customer (FDE-26); listing the available models through the Models API instead of from memory; Claude through Vertex AI and Amazon Bedrock, whose features can lag the first-party API `(verify)`.
- **Library and production:** the SDK's caching fields, batch helpers and the Models API; a cost dashboard fed by `usage` logs.
- **GCP lens:** Claude on Vertex AI: the Vertex client of the SDK with a project and a region, authenticated by Application Default Credentials; regional and global endpoints, quotas per region, and model IDs that differ in form from the first-party ones `(verify)`; billing through the Google Cloud account.
- **Lab `[local]` then `[credit ~$3]`:** customer ask: "our bill tripled after we added a 30-page policy to every request." Measure the uncached and cached cost of 100 requests with the policy in a cached prefix, prove the cache hit with `usage`, then price the same work as a batch.
- **Exam:** CF5 (Cost & Token Management; Model Selection & Trade-offs); CF2 (Claude API Mechanics; Configuration Management).
- **Check:** a system prompt starts with the current date and time, then a 20,000-token policy with a cache breakpoint after it. Why do the cache reads stay at zero?

---

## 7. Prompt, context and output engineering

#### FDE-08 · Prompt engineering — stitch: D5
- [ ] done
- **Core:** clear and direct instructions with the context a new colleague would need; examples (multishot) that are varied and wrapped in tags; XML tags to separate instructions, data and examples; role and rules in the system prompt; asking for reasoning before the answer, or letting adaptive thinking do it; prompt chaining for tasks with separable steps; long documents placed before the question; saying what to do rather than what not to do. D4 owns zero-shot and few-shot as concepts; this card owns the craft.
- **By hand:** a small template system — templates with named slots, escaping of inserted data so it cannot close a tag, a version string, and a test that renders every template with fixture data.
- **Library and production:** prompts live in version control beside the code, reviewed like code, with an eval run on every change (FDE-23); a template library adds little beyond that.
- **GCP lens:** templates are configuration, deployed with the service; no prompt is edited in a console in production.
- **Lab `[local]` then `[credit ~$2]`:** customer ask: "the classifier is 'pretty good'." Improve a ticket-classification prompt in three recorded steps (clear instructions, examples, structure) and report each step's score on the same twenty items.
- **Exam:** CF6 (Prompt Engineering).
- **Check:** user-supplied text is inserted between `<ticket>` tags. What must the template do to that text, and what attack does it blunt (the Cloud Cybersecurity companion's AI-01)?

#### FDE-09 · Context engineering — stitch: D5
- [ ] done
- **Core:** the context window as a budget, not a bin: what earns a place (instructions, the task, the few facts that matter now) and what does not; quality falls as irrelevant context grows, well before the window is full (FDE-CK1); just-in-time retrieval (tools that fetch on demand) against loading everything up front; compaction — summarizing old turns when a conversation nears its limit; memory — notes the application writes and reads back across sessions; subagents that work in their own context and return only a summary; the order of the prompt kept stable so caching (FDE-07) still works.
- **Library and production:** the SDK's and the Agent SDK's compaction and memory features where they exist `(verify)`; otherwise the application's own summarizer.
- **GCP lens:** conversation state and memory live in a store the application owns (Firestore or Cloud SQL), with retention set by the customer's policy (FDE-21).
- **Lab `[local]` then `[credit ~$2]`:** customer ask: "the assistant forgets what we said an hour ago." Build compaction for a long recorded conversation and show that a fact from turn 3 survives to turn 80.
- **Exam:** CF6 (Context Engineering).
- **Check:** a team loads their whole 300-page wiki into every request "so the model knows everything". Name two costs of that and the design you would propose.

#### FDE-10 · Output handling — stitch: D5
- [ ] done
- **Core:** structured outputs — a JSON Schema in the request constrains the response, and strict tool definitions constrain tool inputs `(verify)`; validating anyway, because the schema says what shape and not whether it is true; detecting truncation (`max_tokens`) and refusal (`refusal`) from `stop_reason` before parsing; repair and retry — send the validation error back once, then fail visibly; prompts versioned, with the version recorded in every log line.
- **By hand:** an output validator with repair-and-retry: parse, validate against a schema, on failure send the error text back in one follow-up turn, and give up after one repair with a typed error.
- **Library and production:** structured outputs remove most repair loops; the validator stays as the guard for truncation, refusals and wrong values.
- **GCP lens:** validation failures are counted in Cloud Monitoring as a metric with an alert (C6 recalled).
- **Lab `[local]` then `[credit ~$2]`:** customer ask: "one invoice in fifty breaks our import." Extract invoice fields to a schema over fifty recorded documents, with truncation, refusal and schema failures each counted separately.
- **Exam:** CF6 (Output Handling).
- **Check:** a response parses as valid JSON against the schema, but `stop_reason` is `max_tokens`. Can that happen with structured outputs, and what should the code do?

---

## 8. Tools and the Model Context Protocol

#### FDE-11 · The tool loop by hand — stitch: D5
- [ ] done
- **Core:** tools declared with a `name`, a `description` and an `input_schema`; the model answers with `tool_use` blocks and `stop_reason: "tool_use"`; the application runs each tool and sends back one `user` turn holding a `tool_result` block per call (matched by `tool_use_id`, all results of parallel calls in the same turn), with `is_error: true` when a tool failed; `tool_choice` (`auto`, `any`, a named tool, `none`) and the restrictions current models place on forcing `(verify)`; parallel calls and turning them off; server tools (web search, web fetch, code execution) that run on Anthropic's side and can end a turn with `pause_turn` `(verify)`.
- **By hand:** the loop in plain Python on the FDE-04 client: call, run tools, return results, stop on `end_turn`, with a turn limit and an error path.
- **Library and production:** the SDK's tool runner runs this loop for you with hooks for approval and logging `(verify)`; the learner states what they give up by using it (control over each step) and what they gain.
- **GCP lens:** tools that touch Google Cloud call its APIs with a service account that holds only the roles the tool needs (B5 recalled).
- **Lab `[local]` then `[credit ~$2]`:** customer ask: "can it check order status instead of telling customers to phone us?" Two tools (`get_order`, `list_orders`) over a fake orders service, with one tool that fails and is reported with `is_error`.
- **Exam:** CF8 (Tool Implementation); CF2 (Claude API Mechanics).
- **Check:** the model calls three tools in parallel. You send three separate `user` turns, one result each. What goes wrong?

#### FDE-12 · Tool design — stitch: D5
- [ ] done
- **Core:** a tool description is a prompt: say what it does, when to use it, what each parameter means, and what it returns; fewer, better tools — one tool per task the agent does, not one per API endpoint; namespacing (`orders_get`, `orders_search`) when many tools are loaded; results that spend few tokens (the fields the agent needs, paging, a summary mode); error messages the model can act on ("no order 1234; order IDs are 8 digits"); idempotent tools where the model may retry (the Go companion's GO-29 recalled).
- **Library and production:** evaluating tools the way prompts are evaluated (FDE-22): tasks, success rate, tokens per task.
- **GCP lens:** none beyond FDE-11's service accounts.
- **Lab `[local]` then `[credit ~$2]`:** customer ask: "we exposed all 40 endpoints of our API as tools and the agent is confused." Redesign them into five task-level tools and compare success rate and tokens per task on ten recorded tasks.
- **Exam:** CF8 (Tool Implementation; Agentic Customisation).
- **Check:** a tool returns `500 Internal Error` as its whole result. Rewrite the result so the model can recover.

#### FDE-13 · MCP: the protocol, and a server by hand in Go — stitch: D5
- [ ] done
- **Core:** why MCP exists: one protocol so any host (Claude Code, Claude Desktop, an agent) can use any server's capabilities. Roles: a host runs clients, each client talks to one server. Server primitives: tools (model-invoked), resources (application-attached data addressed by URI) and prompts (user-chosen templates); client primitives: sampling, roots and elicitation `(verify)`. JSON-RPC 2.0 messages (FDE-03). The lifecycle: `initialize` with a protocol version and capabilities, the `notifications/initialized` notification, then `tools/list`, `tools/call`, `resources/read`, and change notifications. Transports: stdio (newline-delimited JSON messages on stdin and stdout; logs go to stderr, never stdout) and Streamable HTTP (FDE-14). The specification is versioned by date `(verify)` the current revision.
- **By hand:** an MCP server in Go over raw JSON-RPC on stdio — read lines, dispatch `initialize`, `tools/list` and `tools/call`, answer with the right `id`, reply with the JSON-RPC error codes for unknown methods and bad parameters — with two tools over a fake internal system, run from a host (the Go companion's GO-13, GO-14 and GO-20 must be taught).
- **Library and production:** the official MCP SDKs (TypeScript, Python, Go `(verify)`) handle negotiation, schemas and transports; the learner lists what the toy skipped (capability negotiation, cancellation, progress, pagination).
- **GCP lens:** a stdio server runs on the user's machine; a server that needs Google Cloud data authenticates as the user, never with a shared key (FDE-21).
- **Lab `[local]`:** customer ask: "our engineers want Claude Code to look up incidents in our internal tracker." The stdio server above, wired into Claude Code and exercised with the MCP Inspector.
- **Exam:** CF8 (MCP Server Development); CF2 (Software Engineering Foundations).
- **Check:** your stdio server prints a debug line with `fmt.Println`. Why does the host disconnect?

#### FDE-14 · MCP in production, and customizing Claude — stitch: D5
- [ ] done
- **Core:** Streamable HTTP — one endpoint that takes JSON-RPC over POST and may answer with JSON or an SSE stream, with a session identifier header `(verify)`; remote servers and authorization — the server is an OAuth 2.0 protected resource that advertises its authorization server (RFC 9728), the client uses the authorization-code flow with PKCE (RFC 7636; the Cloud Cybersecurity companion's AU modules and the Go companion's GO-28 recalled), and tokens are checked for their audience; the MCP Inspector; server discovery and trust — an MCP server is code you run with your permissions (FDE-20). Customizing Claude beyond MCP: Agent Skills (a folder with instructions and resources loaded only when relevant), subagents, slash commands and plugins that bundle them `(verify)`; when each is the right artifact to hand a customer.
- **Library and production:** the SDKs' HTTP transport and auth helpers; a managed identity provider for the OAuth side.
- **GCP lens:** a remote MCP server on Cloud Run behind Identity-Aware Proxy or with its own OAuth, secrets in Secret Manager, logs in Cloud Logging `(verify)` the IAP pattern for MCP clients.
- **Lab `[local]` then `[free-tier]`:** customer ask: "every team wants the tracker in Claude, but security won't allow a shared key." Port FDE-13's server to Streamable HTTP with the SDK, protect it with OAuth so each user acts as themselves, and package a skill that teaches Claude how to triage an incident with it.
- **Exam:** CF8 (MCP Server Development; Agentic Customisation); CF7 (Identity, Secrets & Key Management).
- **Check:** a remote MCP server accepts any valid token from the company's identity provider. What claim must it also check, and what attack does that stop?

---

## 9. Agents and workflows

#### FDE-15 · An agent loop by hand — stitch: D5
- [ ] done
- **Core:** an agent is a model using tools in a loop, deciding its own next step, until a stop condition; the parts: the loop, the tools, the context (FDE-09), memory, subagents with their own context, and the budget (turns, tokens, time, money) that stops it.
- **By hand:** an agent in about 200 lines of Python on the FDE-11 loop: a planner prompt, file and search tools, a subagent call that returns a summary, a notes file as memory, and hard budgets on turns and tokens.
- **Library and production:** FDE-17's Agent SDK; the toy is the reference the learner debugs against.
- **GCP lens:** long-running agents run as jobs (Cloud Run jobs) rather than inside a request (the Cloud Run request timeout, C5 recalled).
- **Lab `[local]` then `[credit ~$3]`:** customer ask: "can it research a supplier and write us a one-page summary?" Run your agent on three recorded research tasks and log every step, tool call and token.
- **Exam:** CF1 (Agent Architecture; Agent Construction with Claude).
- **Check:** your agent repeats the same failing search forever. Name two changes to the loop, not the prompt, that stop it.

#### FDE-16 · Workflows or agents, and the patterns — stitch: D5
- [ ] done
- **Core:** a workflow runs model calls along paths the code fixes; an agent chooses its own path. Start with the simplest thing that works: one call, then a workflow, then an agent only when the steps cannot be known in advance and the task is worth the cost and the risk. The patterns (Schluntz and Zhang, 2024): prompt chaining (with gates between steps), routing (classify, then send to a specialist prompt or model), parallelization (sectioning and voting), orchestrator-workers, and evaluator-optimizer. D4's agentic-patterns line names them; this card owns choosing and building them.
- **Library and production:** most workflows need no framework: plain code and the SDK.
- **GCP lens:** a workflow of long steps can run on Workflows or Cloud Tasks, with each step idempotent (A9 recalled).
- **Lab `[local]` then `[credit ~$2]`:** customer ask: "we want an autonomous agent to answer our email." Show by building it that a router plus three prompt chains handles their five email types better, cheaper and more predictably, and say which one case would justify an agent.
- **Exam:** CF1 (Agent Patterns & Frameworks); CF2 (Claude Application Design).
- **Check:** name the pattern: one call writes a draft, a second grades it against a rubric, and the draft is revised until it passes or three rounds end.

#### FDE-17 · The Agent SDK, harnesses and multi-agent systems — stitch: D5
- [ ] done
- **Core:** the Claude Agent SDK gives the harness that runs Claude Code — the loop, built-in file, shell and search tools, context management, MCP, subagents and hooks — as a library you host yourself; `query()` and its message stream; input modes; permissions and permission modes; hooks for deterministic actions (a hook, not a prompt, enforces a rule); the difference between the SDK's tool runner (a loop over your own tools), the Agent SDK (the Claude Code harness) and Anthropic-hosted agents (Anthropic runs the loop and the sandbox) `(verify)` what is in beta; custom harnesses; supervisor and subagent hierarchies; memory; long runs and context management; when a framework such as LangGraph helps (explicit state machines, checkpoints) and when it hurts (hidden prompts, hard debugging); how multi-agent systems fail (lost context between agents, duplicated work, runaway cost, agents agreeing with each other's mistakes).
- **Library and production:** the Agent SDK in Python or TypeScript against the FDE-15 toy.
- **GCP lens:** the SDK's agent runs in a container on Cloud Run jobs or GKE with a sandboxed filesystem, egress limited to what its tools need (C3 recalled).
- **Lab `[local]` then `[credit ~$3]`:** customer ask: "our analysts spend a day a week reconciling spreadsheets." Rebuild the FDE-15 agent on the Agent SDK with a hook that blocks any write outside one directory, and compare its runs with the toy's.
- **Exam:** CF1 (Agent Construction with Claude; Agent Patterns & Frameworks); CF7 (Claude Hooks).
- **Check:** why is "never delete files" better enforced by a hook than by a sentence in the system prompt?

---

## 10. Claude Code

#### FDE-18 · Configuring Claude Code — stitch: D5
- [ ] done
- **Core:** memory files (`CLAUDE.md`) and their hierarchy — enterprise policy, user, project and local, more specific ones read in addition to broader ones; settings files at the same levels (`settings.json` and `settings.local.json`), where a managed enterprise setting cannot be overridden; permissions (allow, ask and deny rules for tools and commands); rules, skills, slash commands and subagents as files in the project; hooks on tool events (for example before a tool runs, where a blocking exit stops it); MCP server configuration for a project (`.mcp.json`); plan mode and auto-accept modes `(verify)` the current names and file locations.
- **Library and production:** a team's shared project configuration checked into the repository; personal preferences kept in local files that are not.
- **GCP lens:** Claude Code can run against Claude on Vertex AI through environment settings, so a customer keeps traffic and billing in Google Cloud `(verify)`.
- **Lab `[local]`:** customer ask: "juniors keep letting Claude Code run migrations on production." A project configuration that denies the production database command, asks before any migration, adds a hook that blocks writes to the migrations directory without a ticket number, and a `CLAUDE.md` that explains the team's conventions.
- **Exam:** CF3 (Claude Code Operation); CF7 (Claude Hooks).
- **Check:** a rule in a developer's user settings allows a command that the project settings deny. Which wins, and why is that the safe default?

#### FDE-19 · Claude Code headless and in CI — stitch: D5
- [ ] done
- **Core:** non-interactive runs (`claude -p`) with machine-readable output (JSON, or streamed JSON events) `(verify)` the flags; exit codes; limiting tools and permissions for unattended runs; the CI integrations (for example the GitHub Actions integration) `(verify)`; keys as CI secrets (C4 and the Cloud Cybersecurity companion's WL-05 recalled); cost and time limits per run.
- **Library and production:** a CI job that reviews a pull request or fixes a failing lint, with a human approving the change.
- **GCP lens:** the same run in Cloud Build with the key from Secret Manager, or through Vertex AI with the build's service account `(verify)`.
- **Lab `[local]` then `[credit ~$2]`:** customer ask: "can it at least write our release notes?" A CI step that runs Claude Code headless on each merged pull request, writes a release-notes entry, and fails the job on an error rather than committing a partial file.
- **Exam:** CF3 (Claude Code Operation); CF2 (Configuration Management).
- **Check:** a headless run in CI needs to edit files but must never run shell commands. Where is that expressed, and what happens when the model tries?

---

## 11. Security and safety

#### FDE-20 · Attacking and defending your own agent — stitch: D5
- [ ] done
- **Core:** the Cloud Cybersecurity companion's AI-01 (prompt injection) and AI-02 (tool and agent abuse) own the attacks and their labs (SEC-E8.3, SEC-E8.4); this card applies them to the learner's own FDE-15 agent and adds the Claude-side controls. The **lethal trifecta** (Willison, 2025): private data, untrusted content and a way to send data out in one agent means an injected instruction can steal the data — remove one of the three. Least-privilege tools; sandboxing (no network, one directory); human approval before any irreversible action; input and output guardrails (a small classifier model screening inputs and outputs, and its false-positive cost); hooks as deterministic enforcement (FDE-17); staged rollouts, feature flags and a kill switch; the model's refusals, and `stop_reason: "refusal"` handled in code.
- **By hand:** attack your FDE-15 agent with a direct injection and an indirect one hidden in a document it reads, get it to leak a planted secret, then add controls until both fail, and keep the attacks as regression tests.
- **Library and production:** the Agent SDK's permission system and hooks; a moderation or guardrail model in front; the controls reviewed by the customer's security team (FDE-28).
- **GCP lens:** VPC Service Controls and egress rules remove the "send data out" leg for agents that run in a customer project (the Cloud Cybersecurity companion's CL modules recalled).
- **Lab `[local]`:** customer ask: "security will sign off if you can show it can't be tricked." A red-team report on your own agent: each attack, its result before and after, and the one leg of the trifecta each control removes.
- **Exam:** CF7 (AI Application Security; Guardrails & Safe Deployment; Claude Hooks).
- **Check:** an email-summarizing agent can read the inbox and send email. Which leg of the trifecta would you remove, and how?

#### FDE-21 · Identity, secrets and data — stitch: D5
- [ ] done
- **Core:** API keys scoped to workspaces, with spend limits, rotated on a schedule and at once when exposed; no key ever in a browser or a mobile app — a server route calls the API (FDE-02); keys in a secret manager, read at start-up; per-user identity carried through MCP (FDE-14) so actions are attributable; the data questions every enterprise asks — what is retained and for how long, whether inputs train models, where data is processed, the available compliance reports and agreements `(verify)` the current terms; personal data minimized before it is sent (the Cloud Cybersecurity companion's PV modules recalled).
- **Library and production:** Secret Manager or the customer's vault; the workspace and admin controls of the Anthropic Console `(verify)`.
- **GCP lens:** through Vertex AI, access is IAM on the Google Cloud project, data residency follows the chosen region, and the customer's existing Google Cloud agreements apply `(verify)`.
- **Lab `[local]`:** customer ask: "our CISO has a 40-question vendor questionnaire." Answer the ten questions about keys, identity, retention and residency for your capstone design, marking every fact you had to verify.
- **Exam:** CF7 (Identity, Secrets & Key Management).
- **Check:** a developer ships a React app that calls the Claude API directly with a key in an environment variable at build time. What is exposed, and what is the fix?

---

## 12. Evaluation, testing and debugging

#### FDE-22 · Success criteria and an eval harness — stitch: D5
- [ ] done
- **Core:** success criteria agreed with the customer before building: specific, measurable, achievable, and tied to the business outcome (accuracy on a labelled set, latency, cost per task, a refusal rate); a golden dataset — real, varied inputs with expected outputs, including the hard and the adversarial cases; three kinds of grading: code-graded (exact match, schema checks, string rules), model-graded (FDE-23) and human; the pass rate as a proportion with an interval (D5.D2). D1's evaluation metrics are recalled; this card owns evaluating LLM applications.
- **By hand:** an eval harness in Python: load cases, run the system on each (recorded or live), grade, and report the pass rate with its Wilson interval, per-case results and cost, written so a new grader is one function.
- **Library and production:** an evaluation framework or the Anthropic Console's evaluation tool `(verify)` once the harness has shown what is needed.
- **GCP lens:** eval results written to BigQuery, one row per case per run, so runs can be compared over time.
- **Lab `[local]` then `[credit ~$3]`:** customer ask: "leadership wants to know if it is 'good enough' to launch." Agree two success criteria with the tutor playing the customer, build a 50-case golden set, and report whether the system meets them with intervals.
- **Exam:** CF4 (Debugging & Error Handling); CF2 (Understanding Requirements).
- **Check:** your system passes 47 of 50 cases, and the criterion is "at least 90%". Can you tell leadership it meets the criterion? Say what the interval shows.

#### FDE-23 · Model-graded evaluation and regression — stitch: D5
- [ ] done
- **Core:** a model as grader: a rubric with concrete levels, the grader reasoning before its verdict, one criterion per call; checking the grader against human labels with Cohen's κ (D5.D2) before trusting it; known grader biases (position, length, preferring its own style) and the controls (swap the order, blind the source); regression suites run in CI on every prompt or model change, compared with a paired test (McNemar, D5.D2); offline against online evaluation — the golden set before release, A/B tests and user feedback after (D3.D4 recalled).
- **By hand:** an LLM grader with a rubric added to the FDE-22 harness, κ computed against 50 human labels, and the disagreements read one by one.
- **Library and production:** the grader and the harness run as a CI job (C4, FDE-19) that fails the build when the pass rate drops significantly.
- **GCP lens:** the CI job runs in Cloud Build; the golden set lives in a versioned Cloud Storage bucket.
- **Lab `[local]` then `[credit ~$3]`:** customer ask: "a prompt change last month quietly broke refunds." A CI regression suite that would have caught it, with the McNemar result on the old and new prompts.
- **Exam:** CF4 (Debugging & Error Handling); CF1 (Agent Patterns & Frameworks).
- **Check:** your grader agrees with you on 85% of items and κ is 0.2. What does that tell you?

#### FDE-24 · Systematic debugging and observability — stitch: D5
- [ ] done
- **Core:** a method: reproduce with the recorded request, then read the trace in order — `stop_reason`, `usage`, the raw content blocks, tool calls and results — before touching the prompt. The usual failures: silent truncation (`max_tokens`), malformed or missing tool calls, a tool result the model misread, refusals, context overflow, a cache that never hits, and rate-limit cascades where retries multiply load (the Design Patterns companion's ARCH-12 recalled). Tracing an LLM application: one trace per request with a span per model call and tool call, prompt version, model ID, tokens, cost and latency (C6 and the Go companion's GO-24 recalled); logging with personal data redacted.
- **Library and production:** OpenTelemetry spans around SDK calls; an LLM-observability tool if the customer already has one.
- **GCP lens:** Cloud Trace and Cloud Logging, with log-based metrics for tokens and cost.
- **Lab `[local]`:** customer ask: "it just gives wrong answers sometimes." Given ten recorded failing traces, classify each failure by the method above and name its fix.
- **Exam:** CF4 (Debugging & Error Handling).
- **Check:** after a deploy, every request retries three times and the error rate rises. What cascade is this, and which two changes stop it?

#### FDE-CK2 · Checkpoint — a tested, attacked and measured assistant — stitch: D5
- [ ] done
- **Task:** a support assistant from FDE-11…FDE-24: tools over a fake orders service, guardrails, and a golden set of at least 50 cases with a model grader validated by κ, run in CI.
- **Passes when:** the success criteria are written before the build; the pass rate is reported with its interval; the FDE-20 attacks are in the suite and fail; and every failing case in the final run has a written diagnosis.

---

## 13. Application design and the FDE craft

#### FDE-25 · Retrieval-augmented generation end to end — stitch: D5
- [ ] done
- **Core:** D4 owns retrieval-augmented generation as a concept and LB-7 built the rankers; this card builds the pipeline: chunking (by structure, with overlap, sized to the question), contextual retrieval (prepending a short, generated description of where each chunk sits before embedding and indexing it), hybrid search, reranking the top results, and answering with citations (FDE-06); evaluating retrieval (recall@k) separately from the answer; permissions enforced at retrieval time. The Cloud Cybersecurity companion's AI-03 owns the leakage attacks.
- **By hand:** the whole pipeline over the LB-7 code: chunker, contextual descriptions, hybrid retrieval, a model reranker, cited answers, and recall@10 before and after contextual retrieval.
- **Library and production:** a managed vector store and a hosted reranker (FDE-26); the pipeline's evaluation stays in the FDE-22 harness.
- **GCP lens:** Vertex AI Vector Search or `pgvector` on AlloyDB; documents from Cloud Storage; permission metadata from the customer's identity system `(verify)`.
- **Lab `[local]` then `[credit ~$3]`:** customer ask: "the chatbot answers from the wrong version of the policy." Rebuild their retrieval with version metadata and a filter, and show recall and answer accuracy before and after.
- **Exam:** CF2 (Claude Application Design); CF5 (Technical Fundamentals).
- **Check:** recall@10 is 0.95 and answers are still wrong half the time. Where do you look next?

#### FDE-26 · The architecture of Claude applications — stitch: D5
- [ ] done
- **Core:** synchronous against asynchronous calls, and queues for work that can wait (the System Design Primer companion's SD-28 recalled); caching at three levels (prompt caching, response caching for repeated questions, retrieval caching); fallbacks — a smaller model, a cached answer or a human — and graceful degradation (the Design Patterns companion's ARCH-12); latency budgets split across retrieval, model and tools; streaming for perceived latency; prototype → pilot → production, and what changes at each step (evals, monitoring, cost controls, on-call); model deprecation and migration — pinned IDs, an eval run on the new model before switching, a flag to switch back; configuration and prompt versioning; feature flags.
- **Library and production:** the design written as a design document with a decision record for each choice (FDE-28).
- **GCP lens:** Cloud Run for the service, Pub/Sub or Cloud Tasks for queued work, Memorystore for response caching, Vertex AI as the model endpoint where the customer requires it.
- **Lab `[paper]`:** customer ask: "we need the assistant for 20,000 agents by next quarter." A one-page architecture with a latency budget, the fallback chain, the cost per 1,000 conversations, and the migration plan for the next model.
- **Exam:** CF2 (Claude Application Design; Systems Life Cycle; Configuration Management).
- **Check:** the pinned model is announced for retirement in six months. List the steps between the notice and the switch.

#### FDE-27 · Discovery and scoping — stitch: D5
- [ ] done
- **Core:** discovery as a method: stakeholder mapping (who asked, who pays, who uses, who can block); shadowing the workflow the system will change; the "five whys" from the request to the problem; separating the job to be done from the solution the customer proposed; scoping by value against feasibility; ROI stated in the customer's measure (hours saved, tickets deflected, error rate), with a baseline measured before the build; explaining non-determinism to executives — what varies, how it is measured (FDE-22), and what controls it.
- **Library and production:** a discovery document template the learner writes and reuses.
- **GCP lens:** none; this is a people card.
- **Lab `[paper]`, roleplay:** the tutor plays a difficult customer who asks for "a chatbot for our intranet". Run a discovery conversation, then write one page: the real problem, the success criteria, what you will not build, and why.
- **Exam:** CF2 (Understanding Requirements).
- **Check:** the customer asks for a chatbot; shadowing shows staff spend most of their time copying data between two systems. What do you propose, and how do you say it?

#### FDE-28 · Delivering inside an enterprise — stitch: D5
- [ ] done
- **Core:** demos that show the real data and the failure cases, not only the happy path; design documents and decision memos; enterprise IT — single sign-on, private networks and VPCs, egress rules, security reviews, procurement and legal — met early, because they set the timeline; hand-off and enablement: runbooks, dashboards, the eval suite, and training the customer's team to change prompts safely; feeding what the field learns back to the product team.
- **Library and production:** a hand-off checklist the learner builds from this card and reuses in FDE-CAP5.
- **GCP lens:** delivery inside the customer's Google Cloud organization: their projects, their VPC Service Controls perimeter, their Cloud Build (the Cloud Cybersecurity companion's CL modules recalled).
- **Lab `[paper]`, roleplay:** the tutor plays the customer's security reviewer. Present FDE-CK2's assistant, answer the review, and write the decision memo for one control you chose not to add.
- **Exam:** CF2 (Systems Life Cycle; Understanding Requirements).
- **Check:** name three things the customer's team must own after hand-off, and one thing that stays with you.

#### FDE-CK3 · Checkpoint — a scoped design — stitch: D5
- [ ] done
- **Task:** from one roleplayed discovery conversation, a design document: the problem, success criteria with a baseline, the architecture (FDE-26), the retrieval plan (FDE-25), the security review answers (FDE-20, FDE-21), the eval plan (FDE-22, FDE-23) and a pilot plan.
- **Passes when:** a reviewer can trace each design choice to a stated requirement, and nothing is built that no requirement asks for.

---

## 14. Capstones

Each capstone has its own repository, a README with how to run it, recorded-response tests that run with no key, and an eval report. Rubrics are in Appendix K.

#### FDE-CAP1 · A support agent with tools, guardrails and an eval suite — stitch: D5
- [ ] done
- **Build:** FDE-CK2 carried to production quality: Python or TypeScript, deployed on Cloud Run `[credit ~$5]`, with tracing (FDE-24), a kill switch (FDE-20) and the regression suite in CI (FDE-23).

#### FDE-CAP2 · An authenticated remote MCP server — stitch: D5
- [ ] done
- **Build:** a remote MCP server for a mock internal system (the FDE-14 server grown to five task-level tools, FDE-12), with OAuth so each user acts as themselves, deployed on Cloud Run `[free-tier]`, and a skill that teaches Claude to use it.

#### FDE-CAP3 · A document pipeline — stitch: D5
- [ ] done
- **Build:** a pipeline that extracts structured data from a few hundred synthetic documents using the Files API, prompt caching, message batches and structured outputs (FDE-06, FDE-07, FDE-10), with a cost report comparing the batch run against the synchronous one `[credit ~$5]`.

#### FDE-CAP4 · Claude Code headless in CI — stitch: D5
- [ ] done
- **Build:** a repository whose CI runs Claude Code headless (FDE-19) on each pull request to review changes against the team's `CLAUDE.md` conventions, with permissions limited to reading and commenting, and a cost cap per run `[credit ~$2]`.

#### FDE-CAP5 · A simulated engagement — stitch: D5
- [ ] done
- **Build:** the tutor plays a difficult enterprise customer across several sessions. The learner runs discovery (FDE-27), writes the design (FDE-CK3), builds, evaluates (FDE-22, FDE-23), passes a security review (FDE-28) and hands off, and keeps a delivery log of every decision and its reason. Main course B6.C later takes this system before an architecture review board.

---

## 15. CCDV-F, interviews and a track record

1. **Practice by weight.** Practice questions in proportion to the CF weights (§3.2), interleaved with earlier material (rule 0.4.5); every wrong answer goes to the misconception register.
2. **A timed mock.** Fifty-three items in 120 minutes, scored against the pass mark, then the weakest two domains re-taught from their cards.
3. **Registration.** Check whether public registration has opened or whether the learner's employer has joined the Claude Partner Network `(verify)`; book only then.

**CCDV-F — Claude Certified Developer – Foundations (Anthropic)**
- [ ] CCDV-F passed

**Interviews.** Coding in Python or Go (the main course's Tracks A and C and the Go companion), AI system design (FDE-26 with the System Design Primer companion's method), and customer-scenario cases (FDE-27, FDE-28), each practised as a timed roleplay with the tutor as the interviewer.

**A track record.** The capstone repositories made public; one open-source MCP server; a real deployment for a nonprofit or a freelance client, with the client's permission; and a public write-up of one lesson from each. Each goes in the ledger's list of projects built (rule 0.1). Main course B6 extends this record into the architect's portfolio and interview.

---

## 16. Dependency gate

A card is taught only when the modules it names are at least `taught` (rule 0.4.6).

| Before | Needs |
|---|---|
| LB-1, LB-2 | A2 (A2.3, A2.4); A3.P1; D4 begun |
| LB-3 | A2 (A2.3); LB-2; D2 begun |
| LB-4, LB-5 | LB-1, LB-3; D4.D2, D4.D3 |
| LB-6, LB-7 | LB-5; A2.D9 (vectors); D4.D5 |
| FDE-01, FDE-02 | A3 (the Python and Go blocks); A5 |
| FDE-03 | FDE-01; A5 |
| FDE-04…FDE-07 | FDE-03; LB-1; A7; the Design Patterns companion's ARCH-12 |
| FDE-08…FDE-10 | FDE-05; D4 |
| FDE-11, FDE-12 | FDE-05, FDE-10 |
| FDE-13 | FDE-11; the Go companion's GO-13, GO-14 and GO-20 |
| FDE-14 | FDE-13; A10; the Cloud Cybersecurity companion's AU modules; the Go companion's GO-28 |
| FDE-15…FDE-17 | FDE-09, FDE-12 |
| FDE-18, FDE-19 | FDE-17; C4 |
| FDE-20, FDE-21 | FDE-15; the Cloud Cybersecurity companion's AI-01, AI-02 |
| FDE-22…FDE-24 | FDE-10; D1; C6 |
| FDE-25 | LB-7, FDE-06, FDE-22 |
| FDE-26…FDE-28 | FDE-22, FDE-25; A7, A9 |
| FDE-CAP1…FDE-CAP5, §15 | FDE-CK2, FDE-CK3; C1 and C4 for the deployments |

---

## Appendix K — Keys (AFTER attempt only)

### K.1 Check keys

- **LB-1** — Expected: each merge was learned on text in which the earlier merges had already been applied, so later merges are defined over the earlier tokens; applying them in another order produces tokens the training never saw and a different, longer encoding. · Wrong: "longest match first gives the same result" — it can pick a merge whose parts were never formed at that point.
- **LB-2** — Expected: one zero-probability pair makes that example's log-likelihood −∞, so the average loss is infinite; add-one (Laplace) smoothing or a trained model with a small weight penalty gives every pair a non-zero probability. · Wrong: "ignore unseen pairs in the loss" — that hides the failure instead of fixing the model.
- **LB-3** — Expected: `c` contributes to the output through two paths, and by the multivariable chain rule the gradient is the sum of the contributions from both; assigning keeps only the last one. · Wrong: "assigning is fine because the graph is a tree" — reuse makes it a DAG, not a tree.
- **LB-4** — Expected: without the mask each position can see the tokens after it, so the model learns to copy the next token instead of predicting it; at generation time the future is not there, so the model has learned nothing usable. · Wrong: "it overfits" — the problem is information leakage, not capacity.
- **LB-5** — Expected: one; the smallest set whose probability reaches 0.9 is that single token, so top-p samples it with certainty at that step. · Wrong: "the tokens covering 90% of the mass after the top one" — nucleus sampling starts from the most likely token and stops once the threshold is reached.
- **LB-6** — Expected: no; streaming changes when the first tokens are shown, not how fast they are generated, so the total time is about the same; the user perceives it as faster. · Wrong: "streaming makes the model faster" — generation throughput is unchanged.
- **LB-7** — Expected: embeddings capture meaning and blur rare exact strings such as product codes, which may be split into odd tokens; BM25 matches the exact term and gives a rare term a high IDF, so it ranks it first. · Wrong: "the embedding model is too small" — even strong embedding models miss exact identifiers, which is why hybrid search is used.
- **FDE-01** — Expected: the `await` rejects after about 10 ms with `b`'s error; `a()` and `c()` keep running, because promises cannot be cancelled, and their results are discarded unless the code uses `Promise.allSettled` or passes an `AbortSignal`. · Wrong: "it waits 5 s and then fails" — `Promise.all` rejects on the first rejection.
- **FDE-02** — Expected: nothing — a type assertion is erased at compile time; parse the body with a schema (`Order.parse(req.body)` in Zod) and handle the failure with a 400. · Wrong: "TypeScript checks it when the request arrives" — types do not exist at run time.
- **FDE-03** — Expected: keep the partial line in a buffer and prepend it to the next chunk; an event is complete only at a blank line, so nothing is emitted until then. · Wrong: "emit the partial data as its own event" — it splits one JSON payload into two invalid ones.
- **FDE-04** — Expected: no; the same request will stop at the same limit. Raise `max_tokens` to fit the output, shrink the output (fewer fields, no prose), or split the task; and always check `stop_reason` before parsing. · Wrong: "retry with backoff" — it is not a transient error.
- **FDE-05** — Expected: the system prompt is the application's instructions, kept apart from user turns so the model can weigh them differently; concatenating user text into it gives that text the authority of the application's own instructions, which is a direct prompt injection (the Cloud Cybersecurity companion's AI-01). · Wrong: "it is only a formatting convention" — the separation is a trust boundary.
- **FDE-06** — Expected: citations are not compatible with structured outputs `(verify)`, so do two steps: a cited answer over the document, then a structured-output call that converts the cited answer to the schema, keeping the citations beside each field. · Wrong: "ask for citations inside the JSON" — model-written citations are not grounded in the document the way API citations are.
- **FDE-07** — Expected: the cache matches the prefix exactly, and the timestamp at the start changes on every request, so every prefix is new; move the date after the breakpoint (or into the user turn). · Wrong: "the policy is too long to cache" — length helps caching; the changing prefix breaks it.
- **FDE-08** — Expected: escape or neutralize anything in the text that could close or open the tags (and label it as data in the instructions), so the input cannot pretend to end the ticket and start new instructions; it blunts injection that relies on breaking out of the data section. · Wrong: "tags make injection impossible" — they reduce it; the controls of FDE-20 still apply.
- **FDE-09** — Expected: cost and latency on every request, and worse answers because irrelevant text dilutes attention (FDE-CK1); propose retrieval of the few relevant pages (FDE-25) or a search tool the model calls on demand. · Wrong: "a bigger context window fixes it" — the window may fit it; quality and cost still suffer.
- **FDE-10** — Expected: yes — the output can be cut off at `max_tokens`, and the result must be treated as incomplete even if what arrived parses; check `stop_reason` first and treat `max_tokens` as a failure to retry with a larger limit or a smaller task. · Wrong: "structured outputs guarantee a complete object" — they constrain the shape of what is generated, not the length limit.
- **FDE-11** — Expected: the API expects the results of one assistant turn's tool calls in the next single `user` turn; separate turns break the alternation and the matching of `tool_use_id`s, and the request fails or the model loses results. · Wrong: "it works, just slower" — the conversation structure is invalid.
- **FDE-12** — Expected: for example, `{"error": "order 1234 not found; order IDs are 8 digits, e.g. 10002345; use orders_search to find an order by email"}` with `is_error: true` — what failed, why, and what to try next. · Wrong: returning the stack trace — it spends tokens and gives the model nothing it can act on.
- **FDE-13** — Expected: stdout is the protocol channel; a non-JSON line there corrupts the message stream and the host fails to parse it; log to stderr. · Wrong: "the host ignores lines it cannot parse" — the transport has no such rule.
- **FDE-14** — Expected: the audience — the token must have been issued for this server; otherwise a token meant for another service can be replayed against it (a confused-deputy or token-passthrough attack). · Wrong: "the expiry" — an unexpired token for another audience is still the wrong token.
- **FDE-15** — Expected: a turn or budget limit that stops the loop, and loop detection (the same tool call with the same input twice) that feeds back an error or ends the run; both are code, not prompt. · Wrong: "tell it in the prompt not to repeat itself" — that is a request, not a guarantee.
- **FDE-16** — Expected: evaluator-optimizer. · Wrong: prompt chaining — chaining has fixed steps without a loop back to revise.
- **FDE-17** — Expected: a hook runs as code on every tool call and blocks the action whatever the model decided; a prompt is an instruction the model can misread, forget in a long context, or be talked out of by injected text. · Wrong: "the model always follows the system prompt" — it usually does, which is not good enough for an irreversible action.
- **FDE-18** — Expected: the deny rule wins — in the permission system a deny at any level is not overridden by an allow at another `(verify)` — so a project or organization can forbid a command no matter what a developer allows. · Wrong: "the most specific file wins" — that is how preferences combine, not denials.
- **FDE-19** — Expected: in the run's permissions or allowed-tools settings (on the command line or in the project's settings); the attempted shell command is refused by the harness and the model receives an error, and the run continues or ends without executing it `(verify)` the flags. · Wrong: "in the prompt" — unattended runs need enforcement, not a request.
- **FDE-20** — Expected: the send leg: remove the send tool or require human approval of every outgoing email, so injected instructions in an email cannot send data out; reading untrusted mail is the product, and the inbox is the private data. · Wrong: "filter emails for injections" — detection helps but cannot be complete.
- **FDE-21** — Expected: the key is compiled into the JavaScript bundle and anyone can read it from the browser and spend on the account; revoke it, and call the API from a server route that holds the key in a secret manager. · Wrong: "hide it with obfuscation" — anything shipped to the browser is public.
- **FDE-22** — Expected: not yet: 47/50 = 94%, but the Wilson 95% interval is about 83.8% to 97.9%, which includes values below 90%; report the interval and grow the set, or agree the criterion as a lower bound. · Wrong: "94% > 90%, so yes" — it ignores the uncertainty of 50 items.
- **FDE-23** — Expected: most agreement is chance (you and the grader both pass most items), so the grader is not measuring what you measure; read the disagreements, fix the rubric, and re-check κ before using it. · Wrong: "85% agreement is good enough" — κ corrects for chance and says otherwise.
- **FDE-24** — Expected: a retry storm — client retries (often at several layers) multiply the load on a struggling dependency; retry at one layer only with capped exponential backoff and jitter and a retry budget, and add a circuit breaker (the Design Patterns companion's ARCH-12). · Wrong: "raise the rate limit" — it feeds the cascade.
- **FDE-25** — Expected: the generation side: read the failing cases' retrieved chunks and answers — the right chunk is retrieved but not used or misread (too many chunks, poor ordering, the prompt), or chunks lack context (contextual retrieval), or the question needs several chunks combined. · Wrong: "increase k" — recall is already high; more chunks usually make it worse.
- **FDE-26** — Expected: read the deprecation date and the recommended replacement; run the eval suite on the new model and fix regressions; check cost and latency; roll out behind a flag to a slice of traffic with monitoring; switch fully before the date with a path back while both exist. · Wrong: "switch the alias on the last day" — it skips evaluation and leaves no rollback.
- **FDE-27** — Expected: propose automating the copying (an integration, perhaps with Claude extracting and mapping fields) instead of a chatbot, framed around their goal ("you asked for faster answers for staff; most of their time goes here") and the hours it would save, with a small pilot to prove it. · Wrong: "build the chatbot as asked" — it solves the stated request, not the problem.
- **FDE-28** — Expected: for example the prompts and their eval suite, the runbook and on-call, the dashboards and cost budget, and the model-migration process; the product feedback and anything under your company's contract (support for the API itself) stay with you. · Wrong: "everything, once it is live" — ownership has to be named, or nobody owns it.

### K.2 Checkpoint and capstone rubrics

- **FDE-CK1 rubric:** passes when the explanation separates the context limit from retrieval accuracy inside it, uses the learner's own LB-4 model to show the limit, and reports accuracy by position with Wilson intervals from at least twenty trials per position. The trap: claiming a position effect from overlapping intervals.
- **FDE-CK2 rubric:** passes when the criteria predate the build (dated in the repository), the pass rate has its interval, κ ≥ 0.6 is shown for the grader or its weakness is stated, the injection tests fail against the defended agent, and each failing case has a diagnosis. The trap: tuning the prompt on the golden set until it passes, with no held-out cases.
- **FDE-CK3 rubric:** passes when every component traces to a requirement, the baseline is measured or its absence named, and the pilot has an exit criterion. The trap: an architecture that answers the customer's first request instead of the problem found in discovery.
- **FDE-CAP1 rubric:** passes FDE-CK2's rubric in production, plus a working kill switch shown in a test, traces with tokens and cost per request, and a cost per 1,000 conversations. The trap: a demo-only guardrail that the deployed path bypasses.
- **FDE-CAP2 rubric:** passes when each call is attributable to the calling user, tokens are checked for audience and expiry, the tools follow FDE-12, and the server is tested with the MCP Inspector and a host. The trap: a shared service account behind the OAuth screen.
- **FDE-CAP3 rubric:** passes when every document's output validates against the schema or is listed as failed with its reason, the cache-read tokens prove caching, and the batch and synchronous costs are compared from `usage`. The trap: counting a truncated output as a success.
- **FDE-CAP4 rubric:** passes when the CI job runs unattended with read-and-comment permissions only, fails visibly on an error, and stays under its cost cap. The trap: a job token with write access "just in case".
- **FDE-CAP5 rubric:** passes when the delivery log shows the problem found in discovery differing from the first request, the success criteria met with intervals, the security review answered, and a hand-off the tutor-customer can run without the learner. The trap: skipping discovery because the customer sounded certain.
