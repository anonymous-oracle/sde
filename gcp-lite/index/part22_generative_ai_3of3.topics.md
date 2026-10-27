# Part 22 · Generative AI, LLMs, Agents & Claude Applications (part 3 of 3) · TOPIC LIST

Rules and directives for this part: `index/part22_generative_ai_3of3.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Generative AI, LLMs, Agents & Claude Applications (part 3 of 3)

### Agents and workflows

- An agent as a model using tools in a loop until a stop condition; loop, tools, context, memory, planning, subagents and a budget of turns, tokens, time and money
- Workflows (code-fixed paths) versus agents (model-chosen paths); the simplest thing that works first
- The capability ladder, each rung keeping those beneath it: a model, plus retrieval, plus conversation state, plus tools, plus model-chosen control flow, plus delegation; question answering (one retrieval, one generation, text out) versus task completion (a goal with constraints, steps ordered at run time, a change in the world)
- Choosing between them: a workflow when the steps are the same for every input, the path must be auditable, cost and latency must be bounded exactly, or a wrong call is irreversible; an agent when the number of steps depends on the data, a later step can invalidate an earlier one, or recovery must be dynamic; the test of whether the flowchart can be drawn before the request arrives; a workflow with an agent embedded at the one uncertain step
- What the loop costs: a stateless model re-reads the goal, tool schemas and every earlier step on each turn, so cost grows faster than the step count; observations truncated, superseded steps summarized, only the last few kept in full
- Workflow patterns: prompt chaining with gates, routing, parallelization (sectioning and voting), orchestrator–workers, evaluator–optimizer
- **Planning and reasoning loops**
  - Plan, act, observe and track; the ReAct trace (task, thoughts, actions, observations) as the growing context
  - Closed-book reasoning drifting into hallucination as chains lengthen
  - Planner–executor separation: a planner emitting a task graph, cheaper executor models, re-planning on failure, for accuracy, cost and fault tolerance
  - Hierarchical ReAct: a triage meta-planner delegating to specialist agents
  - Reflection: draft, critique, revise, looping on the output rather than the task, at two to three times the tokens
  - Choosing a shape: ReAct for cheap, debuggable short tasks; plan-then-execute for parallel steps and predictable cost; reflection for written output
  - Retrieval as one tool among several: the agent decides whether to retrieve, rewrites the query, retrieves again mid-task, and re-retrieves to verify a draft against its source
- The Claude Agent SDK: the Claude Code harness as a library; `query()` and its message stream; built-in file, shell and search tools; permissions and permission modes; hooks for deterministic enforcement; the difference between an SDK tool runner, the Agent SDK and provider-hosted agents
- **LangChain and LangGraph**
  - Chains as fixed pipelines versus graphs with cycles
  - Typed state, nodes, conditional edges and compilation (`StateGraph`, `add_node`, `add_edge`, `add_conditional_edges`, `compile`)
  - LangChain's components: one model interface across providers; tools declared with `@tool` from a function's type hints and docstring; messages; structured output validated against a schema, enforced by the provider in strict mode; retrievers, MCP servers and other agents plugged in as tools
  - Runnables composed with `|` into prompt, model and parser chains, each supporting `invoke`, `batch` and `stream`; chains as one-way data flow with no loops, pauses or saved state
  - State reducers: each field's merge rule (overwrite, append, add) so that nodes writing the same field never clobber each other; nodes returning only what changed
  - Execution in super-steps: run the active nodes, merge their updates through the reducers, save a checkpoint, follow the edges; termination at `END` or the recursion limit
  - Thread checkpointers (SQLite, PostgreSQL) keyed by `thread_id`, so a run outlives its process; time travel by rewinding to an earlier checkpoint and re-running; human-in-the-loop interrupts that pause before a write and resume later; streaming of tokens, per-node state updates or custom events; summarization nodes against state growth
  - Multi-agent graphs: each specialist a subgraph added as one node, sharing state or returning a summary; handoffs in which a node returns both the next node and a state update (`Command`); fan-out with the number of parallel branches decided at run time (`Send`)
  - The prebuilt `create_agent` loop and middleware for summarization, approval and call limits; tracing runs as a tree of spans with latency, cost and retries (LangSmith, Langfuse)
  - Explicit state machines versus hidden prompts and hard debugging
- **Agent memory**
  - Three lifetimes: conversation state for one thread, task state for one run (what is done, what remains, what must be re-checked), and long-term memory across sessions
  - Short-term thread state versus long-term semantic memory in a vector store, written through save and update tools
  - Timestamps, pruning and conflict resolution against contradictory memories; retrieving only the most relevant memories
  - Memory as persistence across stateless model calls
- **Workflow orchestration and durable execution**
  - Data-pipeline schedulers (Airflow: DAGs, operators, sensors, retries, backfill and catch-up)
  - Serverless step orchestrators (steps in YAML or JSON, retries with backoff, callbacks, parallel branches, long-held state)
  - Queues with per-task retry and rate control
  - Durable-execution engines (Temporal): deterministic replay from event history; side effects in activities
  - Idempotency keys, bounded retries, timeouts at every level, compensating steps, human approval as a paused workflow, timers and callbacks instead of sleeping processes, checkpointed agent state
  - Long-running agents as jobs rather than inside requests
- **Reliability of a deployed agent**
  - Six failure modes: a tool that hangs; a tool that fails (transient or permanent); a tool that correctly returns nothing; a call with wrong arguments; a loop that does not converge; a world that changed between steps
  - Infrastructure failures retried with backoff; semantic failures returned to the model as observations to plan around; a run that never crashes silently, since an uninformed model may invent a result
  - Retry safety by action type: searches repeated freely; a booking whose reply was lost repeated only under an idempotency key, so the provider answers "already booked" with the same ticket
  - Three nested clocks: a tool-call timeout inside a node or model-call timeout inside a whole-run deadline, so the innermost names the stalled dependency
  - Tool fallback order: live data, then cached data labelled stale, then asking the user; a degraded answer that declares itself rather than a confident figure no tool returned; failing loudly with what was and was not done
- **Multi-agent systems**
  - Topologies: supervisor with workers, a triage agent with specialists, hierarchical teams, handoffs between specialists, pipelines, debate and critic pairs, shared task boards
  - Message passing versus shared state
  - When splitting pays (breadth-first, independent sub-questions exceeding one context, too many tools for one agent) and when it does not (tightly coupled edits)
  - Token cost: agents use about 4× the tokens of a chat and multi-agent systems about 15×
  - Failures: lost context, duplicated work, runaway cost, mutual agreement with mistakes, conflicting merges, endless delegation, parallel writes, goals lost across handoffs
  - Controls: per-agent system prompts as guardrails, typed hand-off messages carrying claim sources, per-agent and total budgets, hard stops, one writer per resource, verifiers
  - Where one agent breaks: several goals traded off invisibly in one prompt; sub-task results that conflict with nothing comparing them; one context crowded by every tool and document
  - An agent's contract: its role, model, permitted tools, state, input and output schema, and limits; precise, non-overlapping roles that a coordinator can choose between
  - The hand-off payload: task ID, goal, constraints and return format rather than the whole conversation; who may change a decision and who only recommends
  - The coordination cycle: decompose into bounded tasks, execute (in parallel when independent, in sequence when one needs another's result), attribute each result to its agent and task, reconcile and re-plan
  - Bounding the loop: a round limit, a token budget, a deadlock check for the same conflict recurring, and escalation of the partial plan to a person
  - Results validated against schema, required fields and hard constraints before entering shared state; failures recorded as structured errors, then retried, reassigned or raised to the user
  - Supervisor (simple governance and tracing, one hub for all messages) versus peer-to-peer (fewer hops, harder-to-control paths)
  - Permissions: read and analyse agents run automatically within limits; write actions are proposed by the coordinator and confirmed by a person
  - Messages between agents as untrusted input: tagged as data, checked against constraints, flagged and logged, never obeyed as instructions
  - Logging at every hand-off: the delegation and its context, tool call and arguments, raw result, validation outcome, latency and retries, approvals of writes
  - Evaluation: agent and tool selection accuracy, argument correctness, task completion or a clear refusal, groundedness of every figure in a tool result, conflicts caught before acting, rounds and cost to finish
  - The agent-framework landscape (Claude Agent SDK, OpenAI Agents SDK, Google ADK, Microsoft Agent Framework, Pydantic AI, Strands, Mastra, Agno): chosen by stack; the loop is portable, the state store is not, and the protocol layer outlives any one of them
  - Interoperability standards: MCP for agents reaching tools and data, A2A for agents reaching agents, and proposals for decentralized agent identity, discovery and messaging (ANP, AGNTCY)
  - Cross-boundary agents with Google's Agent Development Kit and A2A
- **Agent-to-agent protocol (A2A)**
  - JSON-RPC 2.0 `message/send` with message parts and session and context IDs; standard JSON-RPC errors
  - Task tracking: submitted, working, artifacts, streaming, terminal states
  - AgentCards: identity, URL, transport, provider, version, capabilities, security schemes, input and output modes, skills, signatures; validation and versioning
  - Tool errors mapped to task failure rather than a hang
- **LLM routing across agents**
  - Retrieving a shortlist of agents by embedding, lexical and metadata features, then reranking
  - A schema-constrained pick (agent ID, confidence, reason) with an explicit fallback policy and no silent pick
  - An evaluation event per decision: candidates, versions, choice, confidence, fallback reason, latency, cost, later success label
  - Edge cases: empty registry, embedding timeouts, near-zero scores, unroutable agents, oversized queries, injection attempts, stale versions, cold-start agents

### Claude Code

- Memory files (`CLAUDE.md`) and their hierarchy: enterprise policy, user, project, local
- Settings files (`settings.json`, `settings.local.json`) and managed settings that cannot be overridden
- Permission rules (allow, ask, deny); skills, slash commands and subagents as project files; hooks on tool events that can block; project MCP configuration (`.mcp.json`); plan mode and auto-accept modes
- Shared project configuration in the repository versus personal local files
- Headless runs (`claude -p`) with JSON or streamed JSON output; exit codes; restricted tools and permissions for unattended runs; CI integrations; keys as CI secrets; cost and time limits per run
- Running against Claude on Gemini Enterprise Agent Platform or Amazon Bedrock to keep traffic and billing in the customer's cloud

### Security and safety of LLM applications

- The lethal trifecta: private data, untrusted content and an exfiltration channel in one agent; removing one leg
- Least-privilege tools; sandboxing (no network, one directory); human approval before irreversible actions
- System prompts as guardrails (scope, refusal rules, output limits); input and output guardrail classifiers and their false-positive cost
- Hooks as deterministic enforcement; staged rollouts, feature flags and kill switches; a flag read at request time, percentage rollout by hashing the user or tenant ID into buckets so that each user keeps one variant across requests, and a kill switch whose default value is the safe path
- Handling refusals in code
- API keys scoped to workspaces with spend limits; rotation; no keys in browsers or mobile apps; keys in a secret manager; keys shown once and stored only as a SHA-256 hash, which suffices for random high-entropy keys unlike low-entropy passwords; a non-secret key prefix stored in clear to find the record, after which the hash is compared in constant time
- Per-user identity carried through MCP so actions are attributable
- Enterprise data questions: retention, training on inputs, processing location, compliance reports; minimizing personal data before sending
- Egress controls and service perimeters removing the exfiltration leg
- **Structural boundary checking**: untrusted input and tool results wrapped in explicit delimiters that the system prompt names as data, not instructions; the output checked in code against its expected structure and boundary markers, so a reply that breaks out of its schema is rejected; guard prompts and exception paths for the cases the checks refuse; the instruction hierarchy as a fixed priority order (system prompt, then developer and user turns, then tool results and retrieved text, which carry data but no instruction authority), so that a conflict resolves toward the higher level

### Evaluation, testing and debugging

- Success criteria agreed before building: specific, measurable, tied to business outcomes (accuracy, latency, cost per task, refusal rate)
- Output quality versus system performance; golden datasets with hard and adversarial cases; task-specific harnesses: per-class precision, recall and macro-averaged F1 for classification; entity-level span F1 for NER, where a predicted entity counts only when its boundaries and type both match the gold; reference-based metrics for generation
- Code-graded, model-graded and human grading; agreement among humans and graders by Cohen's κ, Fleiss' κ and Krippendorff's α
- **Reference-based text metrics**
  - Word-overlap precision and recall; ROUGE-N and ROUGE-L (longest common subsequence, optional stemming)
  - BLEU: clipped n-gram precision, brevity penalty exp(1 − r ÷ c), corpus-level aggregation
  - METEOR: recall-weighted harmonic mean over exact, stem and synonym matches with a fragmentation penalty
  - Levenshtein distance; BERTScore greedy matching of contextual embeddings into precision, recall and F1; BLEURT as a learned metric
  - Blind spots for paraphrase, factuality and open-ended answers
- **Model graders (LLM as a judge)**
  - Pointwise scores versus pairwise preferences (MT-Bench, Chatbot Arena)
  - Rubrics with concrete levels, reasoning before verdict, one criterion per call; G-Eval (generated evaluation steps, form filling, probability-weighted scores)
  - Dimensions: helpfulness, factuality, relevance, tone, style, safety; task completion and tool-call correctness for agents
  - Validation against humans; position, length and self-preference biases and their controls
- **Factuality and hallucination detection**: entailment (NLI) scoring against sources; importance-weighted atomic-fact scoring; groundedness checks against retrieved context; agreement across samples; real-time output filters
- Pass rates as binomial proportions with Wilson score intervals; sample size n ≈ 1.96² p(1 − p) ÷ E² (at most 385 for E = 0.05)
- Comparing prompts or models on the same items with McNemar's test χ² = (b − c)² ÷ (b + c); Pearson's chi-square test over a contingency table, χ² = Σ (O − E)² ÷ E with expected counts E = row total × column total ÷ N and (r − 1)(c − 1) degrees of freedom, for comparing proportions across independent groups
- Regression suites in CI on every prompt or model change; offline golden sets before release, A/B tests and feedback after
- Systematic debugging: reproduce with the recorded request; read `stop_reason`, `usage`, raw blocks, tool calls and results before touching the prompt
- Common failures: silent truncation, malformed tool calls, misread tool results, refusals, context overflow, caches that never hit, retry storms
- Tracing LLM applications: one trace per request, spans per model and tool call with prompt version, model ID, tokens, cost and latency; redacted logs

### Application architecture and LLMOps

- Synchronous versus asynchronous calls; queues for work that can wait
- Caching at three levels: prompt caching, response caching, retrieval caching
- **Semantic caching**: similarity-threshold lookup as a precision decision set from labelled same/different question pairs, biased high because a false hit costs more than a miss; savings as hit rate × cost per call; keys including tenant, permission scope, prompt version and model; expiry when sources change
- **The LLM (AI) gateway**: authentication and per-team keys, rate limits and spend budgets in tokens, throttling and fallback models, failover across models and providers, model cascades, logging with redaction, guardrail hooks, enforcement of pinned model IDs; a token budget as a counter debited per tenant and window by the input and output tokens of each call, checked before the call against the estimated cost from token counting, and refusing or degrading when the remaining budget cannot cover the call
- **Self-hosted model serving**
  - vLLM: PagedAttention storing the key–value cache in fixed-size blocks to cut fragmentation; continuous batching; prefix caching; an OpenAI-compatible server
  - GPU memory budgeting for weights plus key–value cache; throughput versus latency; the batch size that fits set by the memory left after weights, each sequence's key–value cache growing with its length; cost per token = hourly GPU price ÷ (tokens per second × 3600), with tokens per second rising with batch size until the hardware saturates; device maps placing whole layers on different GPUs, which run one after another, so that the added devices add memory but no speed for a single request
  - Asynchronous API front ends (FastAPI) streaming tokens; slim container images with weights mounted rather than baked in
- **Speculative decoding**: a small draft model proposes k tokens, and the target model checks all k in one forward pass; each proposal is accepted with probability min(1, p_target ÷ p_draft), and a rejected position is resampled from the normalized residual, so the output distribution equals the target's exactly; the speed-up set by the acceptance rate and the draft-to-target cost ratio, largest at small batch sizes and shrinking as batches fill the hardware
- **Ray distributed AI workloads**: tasks as stateless remote functions and actors as stateful remote objects, both scheduled across a cluster against declared CPU, GPU and memory resources; an object store passing large results between tasks by reference; the Ray libraries for data preprocessing, distributed training, tuning and model serving; failures handled by task retry and actor restart, with the cost of serializing large arguments
- Fallbacks (smaller model, cached answer, human) and graceful degradation; latency budgets split across retrieval, model and tools; streaming for perceived latency
- Prototype → pilot → production and what each adds (evals, monitoring, cost controls, on-call)
- Model deprecation and migration: evals on the new model, a flag to switch back
- **LLMOps**
  - Releasing prompt, model ID, tool definitions, retrieval index, embedding model and configuration together as one versioned set
  - Eval gates in CI, shadow traffic, canary by traffic split, A/B tests, rollback by flag
  - Monitoring: scheduled golden-set scores; online grading of sampled traffic; time to first token, latency percentiles, tokens and cost per request and tenant, error classes, cache hit rates, retrieval health (empty results, citation share)
  - Drift in hosted-model systems: input-mix shift, provider model changes, stale corpora
  - The feedback flywheel: thumbs, edits and escalations turned into golden-set cases under privacy rules
  - SLOs and error budgets for latency, quality and cost; per-tenant budgets and quotas; kill switches
- **Roofline performance model**
  - Arithmetic intensity I = FLOPs ÷ bytes moved to and from memory; a kernel's attainable throughput is min(peak compute, I × memory bandwidth), the two roofs meeting at the ridge point I* = peak FLOP/s ÷ bandwidth
  - Prefill, processing the whole prompt at once, is a large matrix–matrix product with high arithmetic intensity, so it is compute-bound; decode produces one token per step, reading all the weights and the key–value cache for little arithmetic, so it is memory-bound at small batch sizes
  - Batching raises the arithmetic intensity of decode because one read of the weights serves every sequence in the batch, so throughput rises with batch size until the compute roof is reached
  - Placing a measured serving run under the roof it sits beneath: the gap to that roof is the headroom left for kernel or scheduling work

### The forward-deployed engineer's craft

- The FDE role: building and running production LLM applications inside a customer's systems
- Discovery: stakeholder mapping (who asks, pays, uses, can block); shadowing the workflow; five whys; the job to be done versus the proposed solution; scoping by value against feasibility; ROI against a measured baseline; explaining non-determinism to executives
- Delivering inside an enterprise: demos with real data and failure cases; design documents and decision memos; SSO, private networks, egress rules, security reviews, procurement and legal met early; hand-off with runbooks, dashboards, eval suites and training; feeding field learning back to product

### Exercises

- From scratch: a byte-level BPE tokenizer with a round-trip property test, measuring tokens per character across languages and code
- From scratch: a bigram model by counting and by gradient descent
- From scratch: a scalar autodiff engine and a small network, gradients checked by finite differences
- From scratch: scaled dot-product and multi-head attention, sinusoidal positions and a masked decoder block with cross-attention in NumPy, then in PyTorch
- From scratch: a tiny character-level GPT and a sampler with temperature, top-k, top-p, beam search, repetition penalties and stop sequences
- From scratch: a LoRA layer wrapped around a frozen linear layer, then a LoRA and a QLoRA fine-tune of a small open model with libraries, evaluated against the base model
- From scratch: BM25, brute-force cosine search and reciprocal rank fusion with recall@10 on labelled queries
- From scratch: IVF with k-means cells, product quantization with asymmetric distance tables and a small HNSW graph, measured for recall against a flat index and compared with FAISS and Chroma
- From scratch: BLEU, ROUGE-L and edit distance, compared with BERTScore and an LLM judge on the same outputs
- From scratch: a Messages API client with streaming, retries and a cost calculator; then the SDK
- From scratch: an agent loop with tools, then the Agent SDK, attacked with indirect prompt injection and defended
- From scratch: an MCP server in Go over stdio, then over Streamable HTTP with OAuth
- From scratch: a semantic cache and an LLM gateway with budgets, failover and redaction
- From scratch: a durable workflow runner with replay, compensation and human approval
- From scratch: a fine-tuning loop with warmup and cosine decay, gradient clipping and gradient accumulation, run with and without each to reproduce a loss spike and a divergence
- From scratch: a bottleneck adapter and a prompt-tuning layer on a frozen model, compared with LoRA on trainable parameters, accuracy and inference latency
- A forgetting experiment: a general suite scored before and after a narrow fine-tune, then recovered with rehearsal, an L2-SP penalty and weight interpolation across α
- From scratch: a toy CLIP with two encoders and the symmetric InfoNCE loss, used for zero-shot classification and text-to-image search with Recall@K
- A vision-encoder-to-language-model prototype for captioning or visual question answering: a projector trained with both towers frozen, then tested for hallucination against a blurred-image baseline
- Structured extraction from invoices with a vision-language model: a JSON schema, missing-field handling and a field-level accuracy report against an OCR-only pipeline
- From scratch: late-interaction scoring over patch embeddings, then page-image retrieval compared with parse-then-embed on documents containing charts and tables
- A LangGraph travel-planning agent: typed state with reducers, a tool loop, a policy check that forces a re-plan, a PostgreSQL checkpointer, an approval interrupt before the booking tool, an idempotent retry, nested timeouts and a traced run
- A coordinator with three specialist agents: contracts, schema-validated hand-offs, a round limit, a poisoned tool result rejected as untrusted data, and the six multi-agent evaluation measures reported
- A long-context position experiment with Wilson intervals
- A support assistant with tools, guardrails and a 50-case golden set graded by a κ-validated model grader in CI
- A RAG pipeline with document parsing, contextual retrieval, query rewriting, hybrid search, reranking, verified citations and permission-aware retrieval, scored with RAGAS
- A multi-agent DevOps assistant in LangGraph: triage and specialist agents, checkpointed state, long-term memory and a retrieval gateway
- A prompt-optimization and compression experiment scored on a golden set
- A vLLM and FastAPI serving stack in containers with latency and token-cost logging and a groundedness filter
- An LLM routing service choosing agents from a shortlist, with A2A sample agents
- An authenticated remote MCP server; Claude Code run headless in CI
- A customer engagement simulated from discovery conversation to scoped design document and hand-off
- From scratch: a transformer block with grouped-query attention and RMS normalization in NumPy, with the key–value cache size checked by hand against the formula for a given width, head count and context length
- From scratch: speculative decoding with a draft model and a target model over a toy vocabulary, checking by sampling that the output distribution matches the target's and measuring the acceptance rate
- From scratch: DPO on a toy preference set, with the loss written out by hand, the reference-model anchor and β swept to show how the preferred margin and the drift from the reference move
- **Reasoning drills**
  - Estimate tokens, latency and cost for a workload before calling a model
  - Predict how a prompt or retrieval change moves an evaluation metric, then measure it with intervals
  - Derive attention's cost and the key–value cache memory for a given model size and context length
  - Estimate the quality gain that would justify a larger model's extra cost, then test it on a golden set
  - Predict an adapter's parameter count from d and m, and a run's optimizer steps from dataset size and effective batch, before training
  - Estimate how an agent's token bill grows with its step budget, then measure it with and without context trimming
  - Decide from a task description alone whether it needs a workflow, one agent or several, as a decision record
