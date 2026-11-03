# Generative AI: Topics and Chapter Structure

Twelve chapters in four parts, ordered as a learning path: foundations, then LLMs and prompting, then retrieval-augmented generation (RAG) and agents, then evaluation and safety.

## Contents

**Part 1. Foundations**
1. NLP Foundations
2. AI, Machine Learning and Deep Learning Essentials
3. Deep Learning Foundations for GenAI and Agentic AI
4. The Transformer Architecture

**Part 2. LLMs and Prompting**
5. LLMs, Decoding and APIs
6. Advanced Prompt Engineering
7. Prompt Optimization and Security

**Part 3. Retrieval-Augmented Generation and Agents**
8. RAG Fundamentals
9. Embeddings, Chunking and Vector Databases
10. Vector Indexes and Production RAG
11. Agentic RAG and Multi-Agent Systems

**Part 4. Evaluation and Safety**
12. LLM Evaluation and AI Safety

---

# PART 1. FOUNDATIONS

## Chapter 1. NLP Foundations

1.1 NLP in the GenAI context
- NLP as the interface layer of AI systems: chatbots, search, automation
- Real-world uses: support, finance, healthcare

1.2 Text representation
- Bag of Words → TF-IDF → Word2Vec → embeddings
- Goal: convert text to numbers
- Intuition: similar meaning, similar vectors

1.3 Language modelling basics
- Predicting the next word
- Context window
- Probability distribution over words

1.4 Evolution of language models
- N-grams → RNN → Transformers
- Parallel processing and context awareness

1.5 The classical NLP pipeline
- Cleaning → tokenization → stopwords → lemmatization → features → model
- Hands-on: tokenize with NLTK, apply TF-IDF, build a simple classifier

1.6 Limitations of classical NLP
- No deep context, manual features, poor generalization

1.7 Bridge to GenAI
- Classical NLP → deep learning → LLMs → agents
- The agent loop: observe, reason, act
- Modern NLP architecture: input → embeddings → retrieval → LLM → output
- Hands-on task: build and compare a mini NLP pipeline

## Chapter 2. AI, Machine Learning and Deep Learning Essentials

2.1 History of AI
- The birth of AI: the 1956 Dartmouth Conference
- Major milestones
- The Turing Test
- What is artificial intelligence?

2.2 The symbolic AI era
- Representing knowledge: logic, rule-based inference, semantic nets
- Expert systems
- Hitting the wall: the AI winter

2.3 Machine learning and data
- Data as the fuel of machine learning
- The journey of AI

2.4 Supervised learning
- Core paradigms
- Workflow: train/test split, training, testing
- Tutorial with scikit-learn (with NumPy and Matplotlib)
- Evaluation metrics: confusion matrix; accuracy, precision, recall, F1

2.5 Unsupervised learning
- Core paradigms
- Why compress high-dimensional data
- Workflow: training
- Challenges and limitations

2.6 Feature learning through embeddings
- One-hot vectors and classification with them
- Limitations of sparse representations; why sparsity breaks similarity
- Distributional semantics: words by context
- Dense (distributed) representations; embeddings

2.7 Deep learning
- Biological inspiration: the neuron
- Examples of end-to-end deep learning
- The perceptron (Rosenblatt, 1958)
- Activation functions and non-linearity
- Multi-layer perceptron (MLP)
- Backpropagation: how neural networks learn

2.8 Overfitting, underfitting and regularization
- What overfitting and underfitting are
- The bias–variance tradeoff
- Detecting overfitting: training versus validation loss
- Regularization: penalizing complexity; L1 versus L2 (geometry and sparsity)
- Dropout and early stopping
- Putting it together: a scikit-learn pipeline
- Summary and quick reference

## Chapter 3. Deep Learning Foundations for GenAI and Agentic AI

3.1 A problem-first approach
- A business problem: why is customer churn increasing, what data is needed, how to model it

3.2 Neural networks
- Basics: input → weights → activation → output; layers and neurons
- Hands-on: build a simple network on a dummy dataset

3.3 Learning
- Loss functions
- Optimization
- Overfitting

3.4 Toward GenAI
- Attention intuition
- Self-attention
- Transformers
- The bridge to GenAI

## Chapter 4. The Transformer Architecture

4.1 Before transformers
- Limitations of pre-attention models
- Seq2seq with an RNN; seq2seq with an attention layer
- The attention idea, and why attention alone was not enough
- The self-attention idea

4.2 The encoder
- What self-attention is
- Query, key, value, step by step
- The attention mechanism, vectorized
- A tiny worked example
- The feed-forward layer

4.3 Making deep networks train
- Residual connections
- Layer normalization
- Scaled dot-product attention

4.4 Positional encoding
- Injecting order into attention

4.5 Multi-head attention
- Why multiple heads
- A 2-head worked example: computing Q, K, V; scores, softmax and the attention matrix; head outputs; combining heads; comparing the heads
- A full model in PyTorch

4.6 The decoder
- Decoder design and overview
- Masked self-attention, and masked multi-head self-attention
- Cross-attention: Q, K, V; encoder–decoder attention; matrix form; a worked example; what it cannot do
- Self-attention versus cross-attention
- The complete decoder
- Autoregressive generation: the decoder loop, with a step-by-step example

4.7 Evolution
- "Attention Is All You Need"
- From attention to pretrained models
- The modern transformer zoo

---

# PART 2. LLMS AND PROMPTING

## Chapter 5. LLMs, Decoding and APIs

5.1 The LLM landscape
- BERT: contextual language-model training; the GLUE benchmark
- GPT-1 and GPT-2: decoder-only generation; LAMBADA
- T5 and BART: text-to-text and denoising seq2seq
- GPT-3: few-shot learning and in-context learning
- InstructGPT and RLHF: aligning models with human preferences
- The open-weights wave: LLaMA, Mistral, Falcon
- MMLU: massive multitask language understanding
- The multimodal and reasoning era
- A map of innovations: architecture, training, data

5.2 Prompts
- What prompts are
- A first basic prompt, then a more advanced one
- Elements of a prompt

5.3 Decoding strategies
- Choosing the next word at each step
- Greedy decoding and its problem
- Beam search: how it works, with an example
- Greedy and beam search are deterministic
- The quality versus diversity tradeoff
- Random sampling: temperature, top-k, top-p (nucleus)
- Repetition and frequency penalties
- Max tokens and stop sequences
- Parameter cheat sheet
- Tutorial: putting it all together

5.4 Prompting through APIs
- Introduction to the OpenAI API; frontier models
- Basic chat completion
- Roles in prompting
- Tool calling, with an example
- Coding and reasoning models
- Image generation models
- Examples: a chatbot application, image generation

## Chapter 6. Advanced Prompt Engineering

6.1 Introduction
- Prompting and the autoregressive language model
- What a prompt is; what prompt engineering is

6.2 Common LLM inference terms
- Tokens, temperature, top-k, top-p

6.3 Types of prompting
- Overview
- Zero-shot and few-shot prompting
- Chain-of-thought (CoT) prompting and its variants: zero-shot CoT, few-shot CoT, automatic CoT, self-consistency
- ReAct prompting
- Meta prompting
- Directional stimulus prompting (DSP)
- Prompt chaining
- Tree of thoughts (ToT)

6.4 Limits and defenses
- Limitations of LLM prompting
- Mitigating prompt-injection attacks

## Chapter 7. Prompt Optimization and Security

7.1 Prompt optimization
- Motivation
- The need for versioning, testing and iteration; prompts as versioned artifacts
- Optimization objectives
- Types: manual and automatic
- Automatic prompt optimization (APO): instruction search, gradient optimization, evolutionary optimization, DSPy

7.2 Verbalized sampling
- The mode collapse problem
- Verbalized sampling

7.3 LLM evaluation
- The metric architecture
- Common metrics
- Ways to compute metric scores: statistical scorers, model-based scorers

7.4 Prompt compression
- Basic techniques and advanced techniques
- The LLMLingua family: LLMLingua, LLMLingua-2, with examples

7.5 Prompt security
- Prompt injection
- Indirect prompt injection
- Prompt leaking

---

# PART 3. RETRIEVAL-AUGMENTED GENERATION AND AGENTS

## Chapter 8. RAG Fundamentals

8.1 Why RAG
- Limitations of LLMs: hallucinations, verifiability, knowledge cutoff
- Motivation for RAG

8.2 Introduction to RAG
- Overview, architecture and workflow, with an example
- Sparse retrieval and dense retrieval
- Augmentation and generation
- The retrieval phase in detail: the retrieval pipeline, chunking and query formulation

8.3 Retrievers
- Information-retrieval methods
- TF-IDF
- BM25: a non-binary model

8.4 RAG failure modes
- Retrieval failures
- Context failures
- Generation failures

8.5 Types of RAG
- Standard RAG
- Standard RAG with memory
- Agentic RAG
- Chain-of-RAG (CoRAG): mechanics and more examples

8.6 Assessment
- The RAG assessment framework
- RAGAS

## Chapter 9. Embeddings, Chunking and Vector Databases

9.1 Sparse retrieval and its limits
- RAG workflow recap
- Sparse retrieval; why sparsity breaks similarity

9.2 Dense representations
- Vector embeddings
- The RAG-with-embeddings pipeline
- Sentence embeddings from BERT, and how they compare

9.3 Learning retrieval-oriented embeddings
- Getting negative examples; hard mining
- Dense retrieval with a bi-encoder
- The costlier but more accurate alternative
- Sentence-BERT architecture

9.4 Choosing an embedding model
- Common models: all-MiniLM-L6-v2 (for prototyping), OpenAI text-embedding-3-small
- Matryoshka embeddings and how they order dimensions
- Design decisions, including under real conditions
- The most common silent production RAG bug

9.5 Document processing
- Basics, including OCR
- Design decisions for documents

9.6 Chunking
- Why chunk; right-sizing for retrieval
- Strategies: fixed-size, sliding window, semantic
- Matching strategy to document type: uniform prose and baselines; strongly structured documents (Markdown, legal clauses, API docs, code)
- Tuning chunking, and an overlap myth
- General RAG prose

9.7 Vector databases
- Introduction; why an efficient vector database is required
- KNN: the naive approach
- IVF: the inverted file index, and how much work it saves
- PQ: product quantization (indexing), the 95% memory claim, and search

## Chapter 10. Vector Indexes and Production RAG

10.1 Vector index methods
- IVF and PQ recap
- IVF + PQ combined, and why the approximation works
- HNSW: zooming in through layers; the efSearch candidate list; why search is about log N
- FAISS
- ChromaDB: a database wrapped around vector search

10.2 Design decisions for vector databases
- Prototype scale versus raw speed and large scale
- Choosing a FAISS index (corpus size is the main driver)

10.3 The retrieval pipeline
- Semantic search and a minimal end-to-end pipeline
- Bi-encoder versus cross-encoder: the cost of accuracy
- ColBERT and late interaction
- The two-stage pattern as the industry standard
- Three failures that silently wreck a RAG system

10.4 Production RAG
- From RAG to agentic: the enterprise DevOps and support agent
- What is different in production
- Request shaping, with a project example

10.5 Query transformations
- Rewriting
- Follow-up questions
- Multi-query retrieval
- Step-back prompting

10.6 Query routing
- Routing strategies: rule-based, embedding-based, classifier-based, LLM-based, hybrid
- Applications: data-source routing, model and workflow routing, prompt and index routing

10.7 Security, cost and observability
- Retrieval gateways; access control and least privilege
- Cost management; semantic caching and choosing the threshold
- Observability

10.8 Limits of single-shot RAG
- The multi-hop query case study
- Why if/else logic is not enough; from passive search to active problem solving

## Chapter 11. Agentic RAG and Multi-Agent Systems

11.1 From pipelines to agents
- The limits of linear RAG; from passive to active problem solving
- Simple versus complex tasks
- Agentic RAG: from pipeline to control loop

11.2 Basics of agentic AI
- Anatomy of an agent and its core loop
- An example in the project context
- Tool calling: the engine of agency; designing a tool
- The multi-agent concept: a DevOps multi-agent team

11.3 Orchestration
- Planners and executors; why separate planning from execution
- A case study of the planner in action
- Specialist agents in the execution phase
- Re-planning

11.4 Planning with ReAct
- The limitation of pure chain-of-thought reasoning
- The formal definition of the ReAct loop
- Scaling ReAct: the context and tool-exhaustion problem
- Hierarchical ReAct: triage as a meta-planner
- Caveat in production: the planning trap

11.5 State machines and LangGraph
- What a state machine is; why use one for AI
- LangChain versus LangGraph
- Core concepts: nodes and edges
- Designing the multi-agent DevOps graph (three parts)
- Wiring the team in code; the power of compile()
- Human-in-the-loop (HITL): pausing the infrastructure agent
- Caveats: multi-agent infinite loops; state bloat

11.6 Agentic memory
- The concept and types of memory
- Episodic memory, and its limits
- Semantic (long-term) memory: writing and reading
- The self-healing system in action
- Caveats: memory contradiction; the needle in a haystack

11.7 Provenance and citations
- What provenance is and why citations matter
- The spectrum of citation architectures: inline prompting, structured tool forcing, post-hoc attribution, agentic state provenance
- The trade-off matrix
- Citations in the multi-agent project; UI and UX of citations
- Post-processing: verifying citations
- Connecting provenance to state machines

11.8 Summary and best practices
- Summary of the multi-agent architecture and the DevOps agent journey
- Project implementation steps
- Inter-agent error handling; system prompts
- Key takeaways of multi-agent orchestration strategy

---

# PART 4. EVALUATION AND SAFETY

## Chapter 12. LLM Evaluation and AI Safety

12.1 LLM evaluation
- Why evaluate LLMs; the setup, the ideal scenario and its limitations
- The coefficient of agreement

12.2 Reference-based metrics
- Precision and recall: the foundations
- ROUGE: recall-oriented n-gram overlap, with code
- BLEU: precision-based n-gram scoring, with code
- METEOR: F-score with stems and synonyms, with code
- BERTScore: semantic similarity, with code
- Comparison: when to use which; limitations

12.3 LLM-as-a-judge
- Overview and main variations
- The original and revised workflows
- Typical dimensions to evaluate
- Factuality: focus and quantification

12.4 AI safety foundations
- Early security: information security
- Trustworthy ML
- AI safety for LLMs; threat models

12.5 Attacks on models
- Membership inference
- Model extraction
- Model poisoning
- Model hijacking
- Adversarial attacks

12.6 Risks of GenAI
- Data privacy risks
- Jailbreak risks
- Legal and IP risks

12.7 White-box attacks
- Greedy Coordinate Gradient: method and results
- Indirect prompt injection; prompt leakage

12.8 Black-box attacks
- Model weakness; categories of responses; overall results
- Context contamination; DeepWordBug
- Instruction-centric prompts (TechHazardQA)
- Prompt Automatic Iterative Refinement (PAIR) and its results

12.9 Jailbreak taxonomy
- Language strategies
- Rhetoric techniques
- Imaginary words
- LLM operational exploitation

12.10 Defense
- Red teaming versus blue teaming
- Summary
