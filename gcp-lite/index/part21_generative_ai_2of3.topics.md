# Part 21 · Generative AI, LLMs, Agents & Claude Applications (part 2 of 3) · TOPIC LIST

Rules and directives for this part: `index/part21_generative_ai_2of3.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Generative AI, LLMs, Agents & Claude Applications (part 2 of 3)

### Retrieval-augmented generation

- Why retrieval: hallucination, unverifiable answers, the knowledge cutoff and private data; indexing, retrieval and generation conditioned on retrieved passages
- Naive, advanced (pre-retrieval query rewriting; post-retrieval reranking, filtering and compression) and modular pipelines
- **Document parsing**
  - PDF versus DOCX versus HTML; probing for a text layer before OCR (Tesseract over rendered pages) for scans
  - Tables extracted as HTML or Markdown (pdfplumber, Camelot); layout-aware parsers (Unstructured, Docling, GROBID, document-AI services, vision-language models)
  - HTML boilerplate removal (BeautifulSoup versus readability-style extractors); metadata captured with each chunk
- **Chunking**
  - Fixed-size token windows with 10–20% overlap; sentence and paragraph boundaries
  - Structure-aware splitting by headings, clauses or code syntax trees; recursive splitters
  - Semantic chunking at topic shifts with a maximum size
  - Hierarchical parent–child chunks: retrieve small, return the larger parent
  - Starting near a few hundred tokens and tuning by evaluation
- Contextual retrieval: prepending a generated description of each chunk's place before embedding and indexing
- **Query transformation**: rewriting; follow-up questions made standalone from the conversation; multi-query expansion; HyDE (embedding a hypothetical answer); step-back questions; request shaping before retrieval
- **Query routing**: rules and regular expressions; embedding similarity to route profiles; trained classifiers; LLM routers returning JSON; hybrid waterfalls from cheap to expensive; routing among data sources, models and workflows, prompts and indexes
- Two-stage retrieval: hybrid search for a shortlist, then cross-encoder reranking
- **Citations and provenance**
  - Inline citation by prompting; structured tool output forcing exact quotes; post-hoc attribution by entailment (NLI); provenance carried in agent state
  - Their trade-offs in accuracy, latency and cost; verifying every cited quote against retrieved text; citations linking back to source systems
- **Failure modes**
  - Retrieval: vocabulary mismatch, incomplete recall, multi-hop questions, stale indexes, single-vector dilution of multi-part questions
  - Context: lost in the middle, overload, irrelevant passages
  - Generation: hallucination despite retrieval, conflicts between retrieved and parametric knowledge, wrong attribution
  - Silent pipeline failures: empty chunks from scanned PDFs, missing query and passage prefixes, an L2 index over a cosine-trained model, a lost ID-to-text map
- **Variants**: stateless retrieval; conversational retrieval with history-aware rewriting; agentic retrieval in observe–think–act loops; Chain-of-RAG (retrieval chains learned by rejection sampling and decoded greedily, best-of-N or by tree search)
- Permissions enforced at retrieval time as role-based metadata filters inside the vector store
- **Multimodal RAG**
  - Retrieved content as images, tables, charts or whole pages, because the answer often sits in a figure that text extraction discards
  - Image search: text-to-image and image-to-image over a shared embedding space, on the same approximate-nearest-neighbour indexes as text; weak on compositional and fine-grained queries
  - Parse-then-embed (OCR and layout analysis, then text embeddings) versus retrieval in vision space (a page image embedded directly by a vision-language model)
  - ColPali: one low-dimensional vector per image patch and per query token; the late-interaction score Σ over query tokens of the maximum similarity to any patch; in-batch contrastive training on query–page pairs; page-level indexing; larger indexes than single-vector retrieval
  - Storage choices: one unified embedding space, original modalities kept with cross-modal search, or separate indexes searched separately
  - Fusion of retrieved evidence: similarity-score fusion in a shared space, cross-attention against the query, or conversion to one representation such as captions
  - Generation by a vision-language model over retrieved pages; answers restricted to retrieved content with a page or region citation and a permitted "not found"; a citation that does not prove the answer came from the page
  - Page-retrieval evaluation with ViDoRe and nDCG@5; multi-page reasoning and faithfulness evaluation as open problems
  - Choosing the level: text search for plain text, image search for photo and product corpora, vision-space retrieval for documents mixing text, tables and charts
- **Training retriever and generator together**: the right documents as a latent variable, marginalized over the top-k retrieved (the original RAG and REALM formulations) in an alternation resembling expectation–maximization; contrastive alignment loss with hard negatives; robustness training that injects irrelevant passages so the generator learns to ignore them; in practice, separate pre-training followed by joint fine-tuning
- Evaluation: context precision and context recall for retrieval; faithfulness (claims supported by the context) and answer relevancy; RAGAS and TruLens
- Ingestion by an idempotent, event-triggered embedding worker; scheduled re-embedding

### Model APIs

- **The Messages API by hand**
  - `POST /v1/messages`; headers `x-api-key`, `anthropic-version`, `content-type`
  - Body: `model`, `max_tokens`, alternating `user` and `assistant` turns, top-level `system`, content blocks (`text`, `image`, `document`, `tool_use`, `tool_result`, thinking blocks)
  - Response: `content` blocks, `stop_reason` (`end_turn`, `max_tokens`, `stop_sequence`, `tool_use`, `pause_turn`, `refusal`), `usage` including cache counters
  - Streaming events: `message_start`, `content_block_start`, `content_block_delta` (`text_delta`, `input_json_delta`), `content_block_stop`, `message_delta`, `message_stop`, `ping`, and mid-stream `error` events
  - Error types: 400 `invalid_request_error`, 401 `authentication_error`, 402 `billing_error`, 403 `permission_error`, 404 `not_found_error`, 409 `conflict_error`, 413 `request_too_large`, 429 `rate_limit_error`, 500 `api_error`, 504 `timeout_error`, 529 `overloaded_error`; request IDs
  - Retrying 429, 529 and 5xx with exponential backoff and full jitter honouring `retry-after`; never retrying 400, 401, 403 or 413
  - Rate limits per organization tier and per model, reported in response headers; spend limits
  - A cost calculator from `usage` and a configurable price table
- **The SDKs**: Python, TypeScript and Go SDKs; typed requests, responses and errors; stream helpers that assemble the final message; built-in retries (two by default) and timeouts
- **Request anatomy on current models**
  - No prefilled assistant turns; structure comes from structured outputs instead
  - Adaptive thinking with an effort setting; thinking blocks passed back unchanged in multi-turn tool use
  - `max_tokens` as a hard output cap set from the task
  - Which sampling parameters a model accepts
- **Documents, images and citations**: image and PDF blocks and their token cost; the Files API (`file_id` reuse); citation blocks pointing into documents; what vision is bad at (small text, counting, geometry)
- **Cost, caching, batches and model choice**
  - Token counting before sending
  - Prompt caching: `cache_control` breakpoints (up to four), prefix order tools → system → messages, automatic caching, model-dependent minimum lengths, a five-minute default lifetime refreshed on hits and a one-hour option, writes priced above and reads far below base input, invalidation by any earlier change, `cache_read_input_tokens` and `cache_creation_input_tokens`
  - Message Batches: half price, results within 24 hours, matched by `custom_id` because order is not guaranteed
  - Model choice on quality, latency and price; routing easy requests to small models and escalating; pinned model IDs versus moving aliases; deprecations and migrations; listing models through the Models API
  - Claude through Gemini Enterprise Agent Platform and Amazon Bedrock: different endpoints, credentials and model-ID forms; features that can lag the first-party API
- **OpenAI-compatible chat APIs**: Chat Completions roles (system, developer, user, assistant, tool); JSON mode versus strict schema-constrained outputs; `tools` with `tool_choice` (auto, none, required or a named function) and the two-call tool flow; sampling parameters per request
- **Local models**: Ollama with Modelfiles built from GGUF files and context-length settings

### Prompt, context and output engineering

- **Prompt engineering**: prompt elements (instruction, context, input data, output indicator); clear, direct instructions with the context a new colleague would need; role prompting and rules in the system prompt; zero-shot versus few-shot (multishot) examples, varied and tagged; XML tags separating instructions, data and examples; reasoning before answering; prompt chaining; long documents before the question; saying what to do rather than what not to do
- **Reasoning techniques**
  - Chain of thought: few-shot reasoning exemplars and zero-shot "think step by step"; Auto-CoT (clustering questions, then sampling generated demonstrations)
  - Self-consistency: a majority vote over sampled reasoning paths
  - Tree of Thoughts: breadth- or depth-first search over self-evaluated intermediate thoughts
  - ReAct: interleaved thoughts, actions and observations grounded by tools
  - Meta prompting: structure- and syntax-focused templates rather than content examples
  - Directional stimulus prompting: a small policy model, fine-tuned then trained by reinforcement learning, generating hints for the large model
- **Prompt optimization**
  - Objectives: accuracy, robustness, faithfulness, format adherence, tool use, safety, latency and cost
  - Prompts as versioned artifacts: semantic versions, changelogs, examples, evals, metrics and rationale tracked together; an eval on every change
  - Branching experiments, regression tests, A/B tests, deployment and monitoring
  - Manual refinement versus automatic optimization loops (generate candidates, evaluate, select): APE; ProTeGi textual gradients with beam selection; evolutionary search; reinforcement learning; DSPy programs whose prompts are compiled against a metric
- **Mode collapse and verbalized sampling**: preference tuning sharpening outputs toward the most typical answer; asking for several responses with stated probabilities to recover diversity
- **Prompt compression**: extractive selection, summarization and token-level pruning; LLMLingua (a budget controller, iterative token-level compression scored by a small model, distribution alignment); LLMLingua-2 (token classification trained on distilled compression data)
- **Context engineering**: the context window as a budget; just-in-time retrieval through tools versus loading everything; compaction of old turns; memory written and read across sessions; subagents returning summaries; stable prompt order to keep caches hitting; conversation state in an application-owned store with retention rules
- **Output handling**: structured outputs constrained by JSON Schema; constrained decoding that masks tokens a grammar forbids; strict tool definitions; validating anyway; detecting truncation and refusal from `stop_reason` before parsing; one repair-and-retry then visible failure; prompt versions recorded in every log line

### Tools and the Model Context Protocol

- **The tool loop**: tools declared by `name`, `description` and `input_schema`; `tool_use` blocks and `stop_reason: "tool_use"`; one user turn of `tool_result` blocks matched by `tool_use_id`, all parallel results together, `is_error` on failure; `tool_choice` modes and the models that reject forced tool use; disabling parallel calls; server tools (web search, web fetch, code execution) and `pause_turn`; the SDK tool runner with approval and logging hooks
- **Tool design**: descriptions as prompts; fewer, task-shaped tools rather than one per endpoint, since selection errors grow with the number of tools; namespacing; token-frugal results with paging and summary modes; actionable error messages returned verbatim so the model can correct itself; idempotent tools; evaluating tools by success rate and tokens per task; least-privilege service accounts behind tools
- **MCP fundamentals**: hosts, clients and servers; server primitives (tools, resources addressed by URI, prompts) and client primitives (sampling, roots, elicitation); JSON-RPC lifecycle (`initialize`, `notifications/initialized`, `tools/list`, `tools/call`, `resources/read`, change notifications); capability negotiation, cancellation, progress, pagination; the stdio transport (stdout for messages, stderr for logs); a date-versioned specification; official SDKs; an MCP server in Go by hand
- **MCP in production**: Streamable HTTP with JSON or SSE responses and session headers; remote servers as OAuth 2.0 protected resources advertising their authorization server (RFC 9728); authorization code with PKCE; audience-checked tokens; the MCP Inspector; servers as code that runs with your permissions; remote servers behind an identity-aware proxy with secrets in a secret manager
- **Customizing Claude beyond MCP**: Agent Skills, subagents, slash commands and plugins, and when each is the right artifact
