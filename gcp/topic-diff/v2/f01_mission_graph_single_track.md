# Topic diff: Mission, knowledge graph and single learning track

Source: `gcp/unified-curriculum.md` lines 1-385 (Section 4.2 owner nodes; Section 5 stage table and subsections 5.1-5.7).
Compared against: `gcp-lite/index/*.topics.md` and `gcp-lite/Rust_Track_AI_Infrastructure.md`.

Counts: total 607 | covered 461 | partial 107 | missing 37 | out of scope 2

## 4.2 Canonical Owner Nodes

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Hardware and files basics | covered | part02_computer_organization / Machine organization |  |
| Terminal and shell basics | covered | part05_programming_languages_python_and_shell / Shell and working with APIs from code |  |
| Text editor use | partial | part05_programming_languages_python_and_shell | No dedicated editor topic; tooling only implied |
| Git version control | covered | part15_software_delivery / Git |  |
| HTTP and JSON vocabulary | covered | part09_networking / HTTP and the web |  |
| Python syntax for numerical work | covered | part05_programming_languages_python_and_shell / Python |  |
| NumPy arrays | covered | part05_programming_languages_python_and_shell / Python | NumPy arrays |
| Notebooks and scripts | partial | part05_programming_languages_python_and_shell | Notebooks mentioned only in passing |
| Go syntax and runtime | covered | part06_programming_languages_go |  |
| Go error handling | covered | part06_programming_languages_go |  |
| Go interfaces | covered | part06_programming_languages_go |  |
| Go generics | covered | part06_programming_languages_go |  |
| Go concurrency | covered | part06_programming_languages_go / Go — concurrency |  |
| Go net/http | covered | part06_programming_languages_go / Go — the everyday standard library |  |
| gRPC | covered | part06_programming_languages_go / Go — engineering | gRPC services |
| Profiling and pprof | covered | part06_programming_languages_go / Go — engineering | pprof |
| Go toolchain and releases | covered | part06_programming_languages_go / Go — toolchain and program structure |  |
| Arithmetic and number bases | covered | part01_school_foundations |  |
| Fractions and ratios | covered | part01_school_foundations |  |
| Percentages | covered | part01_school_foundations |  |
| Real line and inequalities | covered | part01_school_foundations |  |
| Algebra | covered | part01_school_foundations |  |
| Functions, domain, codomain and composition | covered | part01_school_foundations |  |
| Coordinate geometry and conics | covered | part03b_analysis_calculus_and_number_theory / Coordinate geometry and conics |  |
| Trigonometry | partial | part01_school_foundations | Only a remedial trigonometry line |
| Logic and quantifiers | covered | part03_mathematics / Proof and discrete mathematics |  |
| Sets | covered | part03_mathematics / Proof and discrete mathematics |  |
| Relations | covered | part03_mathematics / Proof and discrete mathematics |  |
| Induction | covered | part03_mathematics / Proof and discrete mathematics |  |
| Counting and pigeonhole | covered | part03_mathematics / Proof and discrete mathematics |  |
| Recurrences | covered | part08_data_structures_algorithms / Analysis |  |
| Graphs | covered | part08_data_structures_algorithms / Graph algorithms |  |
| Modular arithmetic | covered | part03b_analysis_calculus_and_number_theory / Number theory |  |
| Finite automata | covered | part07_programming_languages_typescript_wire_theory_exercises / Language theory |  |
| Vectors | covered | part03_mathematics / Linear algebra |  |
| Matrices | covered | part03_mathematics / Linear algebra |  |
| Determinants | covered | part03_mathematics / Linear algebra |  |
| Row operations and Gaussian elimination | partial | part03_mathematics / Linear algebra | Row reduction appears only in an exercise |
| Vector spaces | covered | part03_mathematics / Linear algebra |  |
| Eigenvalues and eigenvectors | covered | part03_mathematics / Linear algebra |  |
| Singular value decomposition (SVD) | covered | part03_mathematics / Linear algebra |  |
| Principal component analysis (PCA) | covered | part03_mathematics / Linear algebra |  |
| Spectral methods | partial | part03_mathematics / Linear algebra | Spectral theorem only |
| Limits and continuity | covered | part03b_analysis_calculus_and_number_theory / Real analysis |  |
| Derivatives | covered | part03b_analysis_calculus_and_number_theory / Calculus and differential equations |  |
| Gradients | covered | part03_mathematics / Calculus and optimization |  |
| Integration | covered | part03b_analysis_calculus_and_number_theory / Calculus and differential equations |  |
| ODE intuition | covered | part03b_analysis_calculus_and_number_theory / Calculus and differential equations | ODE intuition |
| Numerical methods | covered | part03_mathematics / Numerical computing |  |
| Finite differences | covered | part03_mathematics / Numerical computing | Finite differences via gradient checking |
| Interpolation | covered | part03_mathematics / Numerical computing |  |
| Runge-Kutta (RK4) | partial | part03b_analysis_calculus_and_number_theory | Runge-Kutta appears only in exercises |
| Probability | covered | part03_mathematics / Probability |  |
| Probability distributions | covered | part03_mathematics / Probability |  |
| Statistical inference | covered | part03_mathematics / Statistics and experimental design |  |
| Maximum likelihood estimation | covered | part03_mathematics / Statistics and experimental design |  |
| Fisher information | partial | part03_mathematics / Statistics and experimental design | Fisher information not named |
| Bootstrap | covered | part03_mathematics / Statistics and experimental design |  |
| Bayesian updating | covered | part03_mathematics / Statistics and experimental design |  |
| Information theory (entropy, KL, mutual information) | covered | part03_mathematics / Information theory |  |
| Experiments and A/B tests | covered | part19_machine_learning / Applied problem families | Experimentation and rollout |
| ML problem framing | covered | part19_machine_learning / Applied problem families | Problem framing |
| Features and feature engineering | covered | part19_machine_learning / Classical machine learning |  |
| Evaluation metrics | covered | part19_machine_learning / Classical machine learning |  |
| Regression | covered | part19_machine_learning / Classical machine learning |  |
| Classification | covered | part19_machine_learning / Classical machine learning |  |
| Decision trees | covered | part19_machine_learning / Classical machine learning |  |
| Clustering | covered | part19_machine_learning | Clustering |
| Anomaly detection | covered | part19_machine_learning / Applied problem families |  |
| Ranking | covered | part19_machine_learning / Classical machine learning | Ranking measures |
| Recommender systems | covered | part19_machine_learning / Applied problem families |  |
| Multi-armed bandits | covered | part03_mathematics / Decision mathematics |  |
| Causal inference | covered | part03_mathematics / Statistics and experimental design |  |
| Neural networks | covered | part19_machine_learning / Deep learning |  |
| Convolutional networks | covered | part19_machine_learning / Deep learning |  |
| Recurrent networks | covered | part19_machine_learning / Deep learning |  |
| Transformers | covered | part20_generative_ai_1of3 / How LLMs work |  |
| Tokenisation | covered | part19_machine_learning / Natural language processing foundation |  |
| NLP libraries (NLTK, spaCy) | covered | part19b_speech_vision_retrieval_and_nlp_toolkits / Classical NLP and toolkits |  |
| Digital signal processing | covered | part03c_signals_systems_and_communications |  |
| Image processing | covered | part19_machine_learning / Classical computer vision and geometry |  |
| Automatic speech recognition | covered | part19b_speech_vision_retrieval_and_nlp_toolkits / Speech recognition: from HMMs to Kaldi |  |
| Kaldi and OpenFst | partial | part19b_speech_vision_retrieval_and_nlp_toolkits | Kaldi covered; OpenFst only in passing |
| Prompting | covered | part21_generative_ai_2of3 / Prompt, context and output engineering |  |
| Decoding strategies (greedy, beam, top-k, top-p) | covered | part20_generative_ai_1of3 / How LLMs work |  |
| Retrieval-augmented generation | covered | part21_generative_ai_2of3 / Retrieval-augmented generation |  |
| Vector indexes and ANN search | partial | part20_generative_ai_1of3 | ANN only in passing; HNSW and IVF not found |
| Agent loops | covered | part22_generative_ai_3of3 / Agents and workflows |  |
| Guardrails | covered | part22_generative_ai_3of3 / Security and safety of LLM application |  |
| LLM evaluation | covered | part22_generative_ai_3of3 / Evaluation, testing and debugging |  |
| LLM safety | covered | part14_security / AI and LLM application threats |  |
| Multimodal models | covered | part20_generative_ai_1of3 / Multimodal models |  |
| Fine-tuning | covered | part20_generative_ai_1of3 / Fine-tuning and adaptation |  |
| Parameter-efficient fine-tuning (LoRA, QLoRA) | covered | part20_generative_ai_1of3 / Fine-tuning and adaptation |  |
| Arrays | covered | part08_data_structures_algorithms / Linear structures and techniques |  |
| Stacks | covered | part08_data_structures_algorithms / Linear structures and techniques |  |
| Queues | covered | part08_data_structures_algorithms / Linear structures and techniques |  |
| Hash maps and hash tables | covered | part08_data_structures_algorithms / Hashing |  |
| Trees and binary search trees | covered | part08_data_structures_algorithms / Trees and heaps |  |
| Heaps | covered | part08_data_structures_algorithms / Trees and heaps |  |
| Union-find | covered | part08_data_structures_algorithms | Union-find |
| Sorting algorithms | covered | part08_data_structures_algorithms / Sorting, searching and strings |  |
| Graph algorithms (BFS, DFS, shortest paths, MST) | covered | part08_data_structures_algorithms / Graph algorithms |  |
| Dynamic programming | covered | part08_data_structures_algorithms / Greedy algorithms and dynamic programming |  |
| Tries | covered | part08_data_structures_algorithms / Sorting, searching and strings | Tries |
| Relational algebra | partial | part12_databases / Relational theory | Relational algebra named only as a term |
| SQL | covered | part12_databases / The SQL language |  |
| Schemas and constraints | covered | part12_databases / Data modelling and design |  |
| Transactions | covered | part12_databases / Transactions and concurrency control |  |
| Joins | covered | part12_databases / Query processing |  |
| Common table expressions | partial | part12_databases / Relational theory | WITH RECURSIVE present; CTE phrase absent |
| Window functions | partial | part12_databases | Window functions not confirmed by name |
| PostgreSQL storage, pages and catalogs | covered | part12_databases / Storage and access methods |  |
| Buffer pool | covered | part12_databases / Storage and access methods |  |
| B-tree indexes | covered | part12_databases / Storage and access methods |  |
| Query executor and planner | covered | part12_databases / Query processing |  |
| MVCC | covered | part12_databases / Transactions and concurrency control |  |
| Locks | covered | part12_databases / Transactions and concurrency control |  |
| Write-ahead logging (WAL) | covered | part12_databases / Recovery and replication |  |
| Replication | covered | part12_databases / Recovery and replication |  |
| Point-in-time recovery | partial | part12_databases / Recovery and replication | Backup and restore present; point-in-time recovery not named |
| REST APIs | covered | part11_software_architecture / API design |  |
| Protocol Buffers | covered | part07_programming_languages_typescript_wire_theory_exercises / Wire formats |  |
| JSON-RPC | partial | part07_programming_languages_typescript_wire_theory_exercises | JSON-RPC not named |
| API gateways | covered | part18_devops_sre | API gateways in NGINX and Kong |
| Schema evolution and API compatibility | covered | part07_programming_languages_typescript_wire_theory_exercises / Wire formats |  |
| API contracts | covered | part11_software_architecture / API design |  |
| Threat modelling | covered | part14_security / Security management, risk and governance | Threat modelling |
| Secure HTTP middleware | covered | part14_security / Web application security | Secure HTTP middleware |
| Authentication | covered | part14_security / Authentication and sessions |  |
| Authorization | covered | part14_security / Authentication and sessions |  |
| Password handling | covered | part14_security / Authentication and sessions |  |
| Sessions | covered | part14_security / Authentication and sessions |  |
| CSRF and CORS | covered | part14_security / Web application security | CSRF and CORS |
| API keys | partial | part14_security | API keys mentioned; signed requests not confirmed |
| JSON Web Tokens | covered | part14_security / Authentication and sessions | JWT |
| OAuth 2.0 and OpenID Connect | covered | part14_security / Authentication and sessions |  |
| MFA and passkeys | covered | part14_security | Passkeys and WebAuthn |
| Secrets management | covered | part14_security | Secrets also covered in part06 Go engineering |
| Supply-chain security | covered | part14_security / Supply chain |  |
| Security verification (ASVS) | partial | part14_security | ASVS mentioned once; not a named group |
| Clean architecture | partial | part11_software_architecture / Architecture fundamentals | Clean architecture not named |
| High-level and low-level design (HLD, LLD) | covered | part13_distributed_systems / System design method | HLD and LLD |
| SOLID principles | covered | part11_software_architecture / Design principles |  |
| Domain-driven design | partial | part11_software_architecture | DDD not named |
| Microservices | covered | part11_software_architecture / Architecture fundamentals |  |
| Design patterns | covered | part11_software_architecture / Gang of Four patterns |  |
| Architecture decision records | covered | part11_software_architecture / Architecture documentation |  |
| C4 model and Mermaid diagrams | covered | part11_software_architecture / Architecture documentation |  |
| Caching | covered | part13_distributed_systems / Caching at scale |  |
| Message queues | covered | part13_distributed_systems / Stream and batch processing |  |
| Backpressure | partial | part13_distributed_systems | Backpressure as flow control in part13; back-pressure only in a part07 exercise |
| Consistency models | covered | part13_distributed_systems / Foundations |  |
| Idempotency | covered | part06_programming_languages_go / Go — engineering | Idempotent retries |
| Retries and timeouts | covered | part06_programming_languages_go / Go — concurrency |  |
| Circuit breakers | partial | part18_devops_sre | Circuit breakers mentioned only in passing |
| Service level objectives (SLOs) | covered | part18_devops_sre / Site reliability engineering |  |
| Observability | covered | part18_devops_sre / Observability |  |
| Rollout and rollback | covered | part18_devops_sre | Deployment strategies: rollout and rollback |
| Feature stores | covered | part19_machine_learning / MLOps | Feature stores |
| Model registry | partial | part19_machine_learning / MLOps | Model registry mentioned only in passing |
| Training and evaluation pipelines | covered | part19_machine_learning / MLOps |  |
| Model serving | covered | part19_machine_learning / MLOps | Model serving |
| Data and model drift | covered | part19_machine_learning / MLOps | Drift monitoring |
| ML governance | covered | part19_machine_learning / MLOps | Governance and responsible ML |
| GCP ML Engineer certification (PMLE) | covered | part24_cloud_providers_2of2 / Certifications — Google Cloud |  |
| Production ML case studies | covered | part25_ml_case_studies_1of5 | Production ML case studies across parts 25 to 29 |
| Docker | covered | part18_devops_sre / Docker |  |
| Docker Compose | covered | part18_devops_sre / Docker |  |
| Kubernetes | covered | part18_devops_sre / Kubernetes |  |
| Terraform | covered | part18_devops_sre / Infrastructure as code |  |
| Kong and NGINX | covered | part18_devops_sre | NGINX and API gateways |
| MongoDB | covered | part12_databases / NoSQL and choosing a store | MongoDB |
| Redis | covered | part12_databases / NoSQL and choosing a store | Redis |
| pgvector and Qdrant | partial | part20_generative_ai_1of3 / Embeddings and retrieval | Qdrant covered; pgvector not confirmed |
| OpenTelemetry | covered | part18_devops_sre / Observability | OpenTelemetry |
| MLflow, W&B and Evidently | covered | part19_machine_learning / MLOps | MLflow, W&B and Evidently |
| Ray, PySpark and Dask | partial | part19_machine_learning | Dask covered; Ray not confirmed |
| FastAPI | partial | part22_generative_ai_3of3 | FastAPI not confirmed |
| LangChain and LlamaIndex | partial | part22_generative_ai_3of3 / Agents and workflows | LangChain covered; LlamaIndex not named |
| vLLM | partial | part20_generative_ai_1of3 | vLLM serving mentioned only in passing |
| System-design and OOD problem set | covered | part13_distributed_systems / System design method |  |

## 5. Single Graph-Ordered Learning Track

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Process versus program | covered | part10_operating_systems / Processes and threads | Program versus process covered |
| Python functions and data structures (lists, tuples, dicts, sets) | covered | part05_programming_languages_python_and_shell / Python |  |
| Unit testing | covered | part05_programming_languages_python_and_shell / Python | pytest and unit tests |
| Estimation and order of magnitude | covered | part01_school_foundations | Rounding and estimation |
| Units and dimensional analysis | covered | part01_school_foundations | Units and dimensional reasoning |
| Go slices and backing arrays | covered | part06_programming_languages_go / Go — composite data, functions, errors | Slice header and backing arrays |
| Go maps and missing-key behaviour | covered | part06_programming_languages_go / Go — composite data, functions, errors | Comma-ok and nil-map write panics |
| Go strings, bytes and runes | covered | part06_programming_languages_go | UTF-8 in part02 data representation |
| Go control flow and variables | covered | part06_programming_languages_go / Go — toolchain and program structure |  |
| Polynomials | covered | part01_school_foundations |  |
| Logarithms and exponents | covered | part01_school_foundations |  |
| Distance metrics (Euclidean, Manhattan, cosine) | partial | part01_school_foundations | Cosine and norms appear in part20 RoPE and embeddings; no metric group |
| Dot product | partial | part20_generative_ai_1of3 / How LLMs work | Dot product only in the RoPE context |
| Matrix multiplication | covered | part03_mathematics / Linear algebra |  |
| Pointers and ownership | covered | part06_programming_languages_go / Go — memory, types with behaviour and interfaces | Pointers and ownership |
| Method sets | covered | part06_programming_languages_go | Method sets |
| Linked lists | covered | part08_data_structures_algorithms / Linear structures and techniques |  |
| Invariants | covered | part03_mathematics / Proof and discrete mathematics | Invariants |
| Binary search | covered | part08_data_structures_algorithms / Sorting, searching and strings |  |
| Greedy algorithms | covered | part08_data_structures_algorithms / Greedy algorithms and dynamic programming |  |
| Asymptotic analysis | covered | part08_data_structures_algorithms / Analysis |  |
| Partial derivatives | covered | part03_mathematics / Calculus and optimization |  |
| Random variables | covered | part03_mathematics / Probability |  |
| Expectation and variance | covered | part03_mathematics / Probability |  |
| Central limit theorem | covered | part03_mathematics / Statistics and experimental design |  |
| Confidence intervals | covered | part03_mathematics / Statistics and experimental design |  |
| Hypothesis testing | covered | part03_mathematics / Statistics and experimental design |  |
| Data contracts | missing | → suggest part12 | Data contracts not named |
| Data leakage | covered | part19_machine_learning | Leakage and point-in-time correctness |
| k-nearest neighbours | partial | part19_machine_learning / Classical machine learning | kNN only as a brute-force mention in part03 |
| Logistic and softmax regression | covered | part19_machine_learning / Classical machine learning |  |
| Generalised linear models | partial | part19_machine_learning / Classical machine learning | GLM covered in one line |
| Naive Bayes | covered | part19_machine_learning / Classical machine learning |  |
| Support vector machines | covered | part19_machine_learning / Classical machine learning |  |
| Ensembles (bagging, random forests, boosting) | covered | part19_machine_learning / Classical machine learning |  |
| Gaussian mixtures and EM | covered | part19_machine_learning / Classical AI: search, knowledge and reasoning | Expectation–maximization |
| NULL three-valued logic | covered | part12_databases / Pre-SQL foundations | Three-valued logic and NULL handling |
| Pagination | covered | part11_software_architecture / API design | Pagination |
| TOAST | covered | part12_databases / Storage and access methods | TOAST |
| Database statistics | partial | part12_databases / Query processing | Cost-based planning only; ANALYZE statistics not named |
| Crash recovery | covered | part12_databases / Recovery and replication | Crash recovery |
| Convex sets and functions | covered | part03_mathematics / Calculus and optimization |  |
| Stochastic gradient descent | covered | part03_mathematics / Calculus and optimization |  |
| Momentum | covered | part19_machine_learning / Deep learning | Momentum also in part03 |
| Coordinate descent | covered | part03_mathematics / Calculus and optimization |  |
| Linear programming | covered | part03_mathematics / Calculus and optimization |  |
| Assignment problem | covered | part03_mathematics / Calculus and optimization | Hungarian method |
| Markov decision processes | covered | part03_mathematics / Decision mathematics |  |
| Propensity scores | covered | part03_mathematics / Statistics and experimental design |  |
| Uplift modelling | covered | part03_mathematics / Statistics and experimental design |  |
| Convolution and correlation | covered | part03c_signals_systems_and_communications / Digital filters and multirate processing |  |
| Sampling and aliasing | covered | part03_mathematics / Signals and sequences |  |
| DFT and FFT | covered | part03_mathematics / Signals and sequences |  |
| Short-time Fourier transform and MFCC | covered | part03_mathematics / Signals and sequences |  |
| Unicode code points and graphemes | covered | part05_programming_languages_python_and_shell / Python |  |
| Regular expressions | covered | part06_programming_languages_go / Go — the everyday standard library |  |
| Image filters | covered | part03_mathematics / Signals and sequences |  |
| n-gram language models | covered | part19_machine_learning / Natural language processing foundation |  |
| Edit distance | covered | part08_data_structures_algorithms / Greedy algorithms and dynamic programming |  |
| Finite-state automata | covered | part02_computer_organization / Digital logic |  |
| Perceptron | covered | part19_machine_learning / Deep learning |  |
| Loss functions | covered | part19_machine_learning / Deep learning |  |
| Activation functions | covered | part19_machine_learning / Deep learning |  |
| Backpropagation | covered | part19_machine_learning / Deep learning |  |
| Regularisation | covered | part03_mathematics / Calculus and optimization |  |
| Recurrent networks (LSTM, GRU) | covered | part19_machine_learning / Deep learning |  |
| Attention mechanisms | covered | part20_generative_ai_1of3 / How LLMs work |  |
| Positional encoding | covered | part20_generative_ai_1of3 / How LLMs work | RoPE |
| Decoder masking | covered | part20_generative_ai_1of3 / How LLMs work |  |
| Tool schemas | partial | part22_generative_ai_3of3 / Agents and workflows | Tool schemas named only in passing |
| Hybrid retrieval | covered | part12_databases / Analytics and other engines | Hybrid lexical and vector retrieval |
| Cross-encoder reranking | covered | part20_generative_ai_1of3 / Embeddings and retrieval |  |
| Grounded generation | covered | part21_generative_ai_2of3 / Retrieval-augmented generation | Grounded generation |
| Workflow patterns (chaining, routing, parallelisation, orchestrator-worker) | covered | part22_generative_ai_3of3 / Agents and workflows |  |
| Prompt injection | covered | part14_security / AI and LLM application threats |  |
| Data and model poisoning | covered | part14_security / AI and LLM application threats | Poisoned chunks |
| Improper output handling | covered | part14_security / AI and LLM application threats |  |
| Excessive agency | covered | part14_security / AI and LLM application threats | Excessive agency |
| Sensitive information disclosure | partial | part19_machine_learning / Governance and responsible ML | PII minimisation in part19 and part22; LLM-specific disclosure not named |
| Misinformation | partial | part14_security / AI and LLM application threats | Misinformation mentioned once |
| Unbounded consumption | partial | part14_security / Resource exhaustion | Generic resource exhaustion only; LLM cost abuse not named |
| HTTP and TLS semantics | covered | part09_networking / HTTP and the web |  |
| Secure outbound calls | partial | part14_security / Web application security | SSRF only |
| Coupling and cohesion | covered | part11_software_architecture / Architecture fundamentals |  |
| Synchronous versus asynchronous communication | covered | part11_software_architecture / Architecture fundamentals |  |
| Outbox pattern | covered | part12_databases / NoSQL and choosing a store | Outboxes |
| Saga pattern | covered | part13_distributed_systems / Distributed transactions |  |
| CQRS | covered | part11_software_architecture / Distributed application patterns |  |
| Capacity estimation | covered | part13_distributed_systems / System design method |  |
| Lineage and promotion gates | partial | part04_problem_solving | Lineage used only as a research term |
| Training-serving skew and parity | partial | part19_machine_learning / Leakage and point-in-time correctness | Training–serving skew named; parity not |
| Continuous integration and delivery (CI/CD) | covered | part18_devops_sre | CI/CD group |
| Continuous training (CT) | partial | part19_machine_learning / MLOps | Continuous training in one line |
| Silent-failure drills | partial | part21_generative_ai_2of3 | Silent pipeline failures noted; deliberate failure drills not named |

## 5.1 Research Baseline and Evidence Hierarchy

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Go memory model | covered | part06_programming_languages_go / Go — concurrency | Go memory model |
| Profile-guided optimisation (PGO) | covered | part06_programming_languages_go / Go — engineering | Profile-guided optimisation |
| Go vulnerability management | covered | part06_programming_languages_go / Go — engineering | Go vulnerability management |
| Algorithm design paradigms | partial | part08_data_structures_algorithms | Paradigms appear as topics, not as a named group |
| Distributed optimisation (ADMM) | missing | → suggest part03 | ADMM not named |
| Statistical learning theory | covered | part19_machine_learning / Classical machine learning | Statistical learning theory |
| Self-supervised vision learning | partial | part19b_speech_vision_retrieval_and_nlp_toolkits | Self-supervised speech only; vision SSL not named |
| Dense bi-encoder retrieval | covered | part20_generative_ai_1of3 / Embeddings and retrieval | Dense bi-encoder retrieval |
| Whisper | covered | part20_generative_ai_1of3 / How LLMs work | Whisper |
| Multilingual and low-resource evaluation | partial | part14_security / AI and LLM application threats | Low-resource attacks; multilingual evaluation not named |
| Generalisation and bias-variance | covered | part03_mathematics / Calculus and optimization | Generalisation and bias–variance |
| Product quantisation and IVF | missing | → suggest part20 | Product quantisation and IVF not named |
| RAG component and end-to-end evaluation (Ragas) | covered | part21_generative_ai_2of3 / Retrieval-augmented generation | RAG component evaluation (RAGAS) |
| Service level indicators (SLIs) | covered | part18_devops_sre / Site reliability engineering | Service level indicators |
| Reachable-vulnerability checks | covered | part06_programming_languages_go / Go — engineering | Reachable-vulnerability checks (govulncheck) |

## 5.2 S0-S4: Computing, Language, and Reasoning Foundations

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Bits, bytes and CPU, memory and storage | covered | part02_computer_organization / Data representation |  |
| Environment variables | partial | part14_security / Containers and Kubernetes security | Environment variables only in secrets context |
| Ports and ports numbers | covered | part09_networking | Ports |
| DNS name lookup | covered | part09_networking / DNS |  |
| Shell pipes and composition | covered | part05_programming_languages_python_and_shell / Shell and working with APIs from code |  |
| Exit status and standard streams | covered | part05_programming_languages_python_and_shell / Shell and working with APIs from code |  |
| Git index and working tree | covered | part15_software_delivery / Git |  |
| Reproducible repository layout | partial | part03_mathematics / Numerical computing | Seeding covered; repo layout not named |
| Python modules and virtual environments | covered | part05_programming_languages_python_and_shell / Python |  |
| Exceptions and file I/O | covered | part05_programming_languages_python_and_shell / Python |  |
| Integer overflow by dtype | covered | part02_computer_organization / Data representation |  |
| Floating-point representation error | covered | part03_mathematics / Numerical computing |  |
| Tolerance-based assertions | partial | part06_programming_languages_go / Go — engineering | Timestamp tolerance only; no float tolerance |
| Seeded random generators | covered | part03_mathematics / Numerical computing |  |
| Vectorisation | covered | part05_programming_languages_python_and_shell / Python |  |
| Broadcasting | covered | part05_programming_languages_python_and_shell / Python |  |
| Shape, dtype and axis reasoning | partial | part05_programming_languages_python_and_shell | Shape and axis reasoning implicit only |
| Copies versus views | covered | part05_programming_languages_python_and_shell / Python |  |
| Strides and memory layout | covered | part05_programming_languages_python_and_shell / Python |  |
| Elementwise versus matrix multiplication | partial | part20_generative_ai_1of3 | Elementwise product appears; contrast with matrix product not named |
| Go module and package layout | covered | part06_programming_languages_go / Go — toolchain and program structure |  |
| Go structs and zero values | covered | part06_programming_languages_go / Go — memory, types with behaviour and interfaces | Structs and zero values |
| Go vet, gofmt and benchmarks | covered | part06_programming_languages_go / Go — toolchain and program structure | gofmt, vet and benchmarks |
| Table-driven tests | covered | part06_programming_languages_go / Go — engineering |  |
| Proof by contradiction and counterexample | covered | part03_mathematics / Proof and discrete mathematics |  |
| Contrapositive proofs | covered | part03_mathematics / Proof and discrete mathematics |  |

## 5.3 S5-S10: Mathematical and Algorithmic Core

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Equations and absolute value | covered | part01_school_foundations |  |
| Sequences | covered | part01_school_foundations |  |
| Domain, codomain, range and inverse | covered | part03_mathematics / Proof and discrete mathematics |  |
| Piecewise functions | covered | part01_school_foundations |  |
| Amortised growth | covered | part08_data_structures_algorithms / Analysis |  |
| Property-based testing | covered | part11_software_architecture / Software testing at depth |  |
| Fuzz testing | covered | part06_programming_languages_go / Go — engineering | Fuzzing |
| Race detector | covered | part06_programming_languages_go / Go — concurrency | Race detector |
| Benchmark crossover points | missing | → suggest part08 | Benchmark crossover points not named |
| Span, independence, basis and dimension | covered | part03_mathematics / Linear algebra |  |
| Four fundamental subspaces | covered | part03_mathematics / Linear algebra |  |
| Linear maps | covered | part03_mathematics / Linear algebra |  |
| Orthogonality and projection | covered | part03_mathematics / Linear algebra |  |
| Least squares | covered | part03_mathematics / Linear algebra |  |
| Diagonalisation | covered | part03_mathematics / Linear algebra |  |
| Symmetric and positive-definite matrices | covered | part03_mathematics / Linear algebra |  |
| Pseudoinverse | covered | part03_mathematics / Linear algebra |  |
| Condition number | covered | part03_mathematics / Numerical computing |  |
| Rank and nullity | covered | part03_mathematics / Linear algebra |  |
| Low-rank approximation | covered | part03_mathematics / Linear algebra |  |
| QR decomposition and Gram-Schmidt | covered | part03_mathematics / Linear algebra |  |
| Power iteration | covered | part03_mathematics / Linear algebra |  |
| Residual and reconstruction checks | partial | part03_mathematics / Statistics and experimental design | Residual plots covered; reconstruction checks not named |
| Lower bounds | covered | part03b_analysis_calculus_and_number_theory / Real analysis |  |
| Recurrence solving and master theorem | covered | part08_data_structures_algorithms / Analysis |  |
| Quickselect and selection | partial | part08_data_structures_algorithms / Sorting, searching and strings | Quickselect not named |
| Divide and conquer | covered | part08_data_structures_algorithms / Linear structures and techniques |  |
| Strongly connected components | covered | part08_data_structures_algorithms / Graph algorithms |  |
| Max-flow | covered | part08_data_structures_algorithms / Graph algorithms |  |
| Exchange arguments | covered | part08_data_structures_algorithms / Greedy algorithms and dynamic programming |  |
| Differential testing | missing | → suggest part11 | Differential testing not named |
| Linearisation (tangent approximation) | covered | part03b_analysis_calculus_and_number_theory / Calculus and differential equations | Tangents in part01 |
| Chain, product and implicit rules | covered | part03b_analysis_calculus_and_number_theory / Calculus and differential equations | Chain rule |
| Curve sketching and critical points | covered | part03b_analysis_calculus_and_number_theory / Calculus and differential equations |  |
| Fundamental theorem of calculus | partial | part03b_analysis_calculus_and_number_theory | Fundamental theorem of calculus not confirmed by name |
| Integration techniques | partial | part03b_analysis_calculus_and_number_theory | Integration techniques not confirmed by name |
| Sequences and series, convergence tests | covered | part03b_analysis_calculus_and_number_theory / Real analysis |  |
| Jacobian and Hessian | covered | part03_mathematics / Calculus and optimization |  |
| Multiple integrals | covered | part03b_analysis_calculus_and_number_theory / Calculus and differential equations | Multiple integrals |
| Vector calculus (divergence, curl) | partial | part03b_analysis_calculus_and_number_theory | Vector calculus not confirmed by name |
| Conditioning and numerical stability | covered | part03_mathematics / Numerical computing |  |
| Root finding (bisection, Newton) | covered | part03_mathematics / Calculus and optimization | Newton's method |
| Numerical quadrature | missing | → suggest part03 | Numerical quadrature not named |
| Convergence plots and step-size stability | partial | part03b_analysis_calculus_and_number_theory | Step-size check only in an exercise |
| Sample spaces and conditioning | covered | part03_mathematics / Probability |  |
| Joint, marginal and conditional distributions | covered | part03_mathematics / Probability |  |
| Transformations of random variables | missing | → suggest part03 |  |
| Concentration inequalities | covered | part03_mathematics / Probability |  |
| Law of large numbers | covered | part03_mathematics / Probability |  |
| Markov chains | covered | part03_mathematics / Probability |  |
| Estimands and sampling | partial | part03_mathematics / Probability | Survey sampling designs covered; estimands not named |
| MAP estimation | covered | part03_mathematics / Decision mathematics |  |
| Sufficiency | covered | part03_mathematics / Statistics and experimental design |  |
| Permutation tests | covered | part03_mathematics / Statistics and experimental design |  |
| Regression diagnostics | partial | part19_machine_learning | Regression diagnostics not named |
| Cross-entropy and log-loss | covered | part03_mathematics / Information theory |  |
| Perplexity | covered | part03_mathematics / Information theory |  |
| Source coding and Huffman coding | covered | part03_mathematics / Information theory |  |
| Statistical power | missing | → suggest part03 |  |
| Multiple-comparison correction | covered | part03_mathematics / Statistics and experimental design |  |
| Sequential testing | covered | part03_mathematics / Statistics and experimental design |  |
| Practical significance | missing | → suggest part03 |  |

## 5.4 S11-S14: Classical ML, Databases, Optimization, RL, and Causality

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Non-ML baselines | covered | part04_problem_solving / Research method |  |
| Missing-data handling | missing | → suggest part19 |  |
| Class imbalance | covered | part19_machine_learning / Classical machine learning |  |
| Probability calibration | partial | part03_mathematics / Information theory | Calibration named only |
| Ridge and lasso regularisation | covered | part03_mathematics / Decision mathematics |  |
| LDA and QDA | covered | part19_machine_learning / Classical machine learning |  |
| Kernel methods | partial | part03_mathematics / Statistics and experimental design | KDE only; kernel methods not named |
| Gradient boosting | covered | part19_machine_learning / Classical machine learning |  |
| Feature selection | covered | part19_machine_learning / Classical machine learning |  |
| Ablation and error taxonomy | covered | part04_problem_solving / Research method |  |
| Functional dependencies and normalisation | partial | part12_databases | Normal forms not verified by name |
| Keys (primary, foreign, candidate) | covered | part12_databases / Relational theory | Keys |
| DDL and column types | covered | part12_databases / The SQL language | DDL and column types |
| Semi and anti joins | missing | → suggest part12 |  |
| Outer joins | missing | → suggest part12 |  |
| Aggregation and GROUP BY | partial | part12_databases / The SQL language | GROUP BY not confirmed by name |
| Recursive queries | covered | part12_databases / Relational theory | Recursive queries via WITH RECURSIVE |
| Isolation levels | covered | part12_databases / Transactions and concurrency control | Isolation levels |
| Parameterised queries | covered | part12_databases / Operating databases | Parameterised queries |
| Connection pools | covered | part06_programming_languages_go / Go — engineering | Connection pools |
| Migrations and rollback | partial | part12_databases / Operating databases | Migrations and rollback not named as a topic |
| Row, column and log-structured storage | covered | part12_databases / NoSQL and choosing a store | Row, column and log-structured storage |
| Heap files and tuples | partial | part12_databases / Storage and access methods | Heap files implicit only |
| Hash indexes | covered | part12_databases / Storage and access methods | Hash indexes |
| GIN, GiST and BRIN indexes | missing | → suggest part12 | GIN, GiST and BRIN not named |
| Nested-loop, hash and merge joins | covered | part12_databases / Query processing |  |
| Cardinality estimation and cost-based plans | partial | part12_databases / Query processing | Cost-based plans not named |
| Deadlock detection | covered | part06_programming_languages_go / Go — concurrency | Deadlock detection |
| Vacuum | covered | part12_databases / Transactions and concurrency control | Vacuum |
| Checkpoints | covered | part12_databases / Storage and access methods | Checkpoints |
| EXPLAIN ANALYZE | partial | part12_databases / Query processing | EXPLAIN ANALYZE not named |
| Parallel and distributed database trade-offs | covered | part12_databases / Query processing |  |
| Storage media and latency | covered | part02_computer_organization / Machine organization | Storage latency numbers |
| Adaptive optimisers (Adam, RMSProp) | covered | part19_machine_learning / Deep learning | Adaptive optimisers |
| Lagrangian duality and KKT conditions | partial | part03_mathematics / Calculus and optimization | Lagrange multipliers covered; KKT not named |
| Proximal methods | covered | part03_mathematics / Calculus and optimization | Proximal methods |
| Robust and stochastic optimisation | missing | → suggest part03 |  |
| Non-convex optimisation diagnostics | covered | part03_mathematics / Calculus and optimization | Non-convex diagnostics |
| Bellman equations | partial | part08_data_structures_algorithms / Graph algorithms | Bellman–Ford only; Bellman equations not named |
| Value and policy iteration | covered | part19_machine_learning / Specialised learning areas | Value and policy iteration |
| Monte Carlo methods | covered | part03_mathematics / Probability | Monte Carlo |
| Temporal-difference learning | covered | part19_machine_learning / Specialised learning areas | Temporal-difference learning |
| Q-learning | covered | part19_machine_learning / Specialised learning areas | Q-learning |
| Policy gradients | covered | part19_machine_learning / Specialised learning areas | Policy gradients |
| Potential outcomes and counterfactuals | covered | part19_machine_learning / Applied problem families | Potential outcomes |
| DAGs and structural causal models | covered | part03_mathematics / Statistics and experimental design | DAGs and structural causal models |
| Randomised experiments | covered | part03_mathematics / Statistics and experimental design | Randomised experiments |
| Backdoor and frontdoor adjustment | covered | part03_mathematics / Statistics and experimental design | Backdoor adjustment |
| Instrumental variables | covered | part19_machine_learning / Applied problem families | Instrumental variables |
| Difference-in-differences | covered | part03_mathematics / Statistics and experimental design | Difference-in-differences |
| Regression discontinuity | covered | part19_machine_learning / Applied problem families | Regression discontinuity |
| Synthetic control | covered | part19_machine_learning / Applied problem families | Synthetic control |
| Overlap and sensitivity analysis | partial | part19_machine_learning / Applied problem families | Overlap named; sensitivity analysis not named |

## 5.5 S15-S16: Domain Mathematics and Deep Learning

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Signal energy and power | covered | part03c_signals_systems_and_communications / Signals and linear time-invariant systems |  |
| Complex exponentials | covered | part03c_signals_systems_and_communications / Signals and linear time-invariant systems |  |
| Impulse and step responses | covered | part03c_signals_systems_and_communications / Signals and linear time-invariant systems |  |
| LTI system properties | covered | part03c_signals_systems_and_communications / Signals and linear time-invariant systems |  |
| Frequency response | covered | part03c_signals_systems_and_communications / Signals and linear time-invariant systems |  |
| Fourier series | covered | part03c_signals_systems_and_communications / Transforms and system analysis |  |
| Fourier transform | covered | part03c_signals_systems_and_communications / Transforms and system analysis |  |
| Laplace transform | partial | part03c_signals_systems_and_communications / Transforms and system analysis | Laplace transform not confirmed by name |
| z-transform | covered | part03c_signals_systems_and_communications / Transforms and system analysis | z-transform |
| Window functions and spectral leakage | covered | part03c_signals_systems_and_communications / Practical spectral analysis | Window functions and leakage |
| FIR and IIR filters | covered | part03c_signals_systems_and_communications / Digital filters and multirate processing | FIR and IIR filters |
| Pole-zero stability | partial | part03c_signals_systems_and_communications / Transforms and system analysis | Pole-zero stability not named |
| Filter banks | covered | part03c_signals_systems_and_communications / Digital filters and multirate processing | Filter banks |
| Multirate processing | covered | part03c_signals_systems_and_communications / Digital filters and multirate processing | Multirate processing |
| Quantisation | covered | part03c_signals_systems_and_communications / Digital filters and multirate processing | Quantisation |
| Parseval's theorem | covered | part03b_analysis_calculus_and_number_theory / Complex and functional analysis | Parseval |
| Image formation | covered | part19b_speech_vision_retrieval_and_nlp_toolkits | Image formation in the computer vision section |
| Colour spaces and gamma | partial | part19_machine_learning | Colour spaces not named |
| Histograms and point transforms | partial | part03_mathematics / Statistics and experimental design | Histogram quantiles only |
| Separable 2D filters | covered | part03_mathematics / Signals and sequences | Separable 2D filters |
| Denoising and sharpening | covered | part03_mathematics / Signals and sequences | Denoising and sharpening |
| Edge detection | covered | part03_mathematics / Signals and sequences | Edge detection |
| Mathematical morphology | covered | part03_mathematics / Signals and sequences | Mathematical morphology |
| Frequency-domain image filtering | partial | part19b_speech_vision_retrieval_and_nlp_toolkits | Pitch spectrum only; frequency-domain filtering not named |
| Deconvolution and restoration | covered | part19b_speech_vision_retrieval_and_nlp_toolkits | Image restoration and deconvolution |
| Image segmentation | partial | part19_machine_learning | Segmentation not named |
| Corner detection | missing | → suggest part19 |  |
| Feature descriptors and matching | missing | → suggest part19 |  |
| Homography | covered | part19_machine_learning / Classical computer vision and geometry | Homography |
| RANSAC | missing | → suggest part19 | RANSAC not named |
| Camera calibration | missing | → suggest part19 |  |
| Epipolar geometry | covered | part19_machine_learning / Classical computer vision and geometry | Epipolar geometry |
| Stereo vision | covered | part19_machine_learning / Classical computer vision and geometry | Stereo vision |
| Optical flow | covered | part19b_speech_vision_retrieval_and_nlp_toolkits | Optical flow |
| Detection and recognition metrics (IoU, mAP) | covered | part19_machine_learning / Applied problem families | Detection metrics |
| Unicode normalisation | covered | part06_programming_languages_go / Go — composite data, functions, errors | Unicode normalisation |
| Sentence splitting | covered | part19b_speech_vision_retrieval_and_nlp_toolkits / Classical NLP and toolkits |  |
| Smoothing | covered | part03_mathematics / Signals and sequences | Smoothing |
| Inverted index and Boolean retrieval | covered | part19_machine_learning / Applied problem families | Inverted index and Boolean retrieval |
| TF-IDF | covered | part19_machine_learning / Natural language processing foundation | TF-IDF |
| BM25 | covered | part19_machine_learning / Applied problem families | BM25 |
| Word vectors | covered | part19_machine_learning / Natural language processing foundation | Word vectors |
| Byte-pair encoding | covered | part20_generative_ai_1of3 / How LLMs work | Byte-pair encoding |
| WordPiece and unigram tokenisation | partial | part19b_speech_vision_retrieval_and_nlp_toolkits | Unigram LM only; WordPiece not named |
| Part-of-speech tagging | partial | part19_machine_learning / Natural language processing foundation | POS tagging not named |
| Parsing (constituency and dependency) | partial | part07_programming_languages_typescript_wire_theory_exercises / Language theory | Parsing only in passing |
| Weighted finite-state transducers | partial | part06_programming_languages_go | Weighted automata named; WFST not named |
| Acoustic phonetics | covered | part19b_speech_vision_retrieval_and_nlp_toolkits / Speech science and analysis | Acoustic phonetics |
| Pre-emphasis and framing | covered | part03_mathematics / Signals and sequences | Pre-emphasis and framing |
| Mel spectrogram | covered | part03_mathematics / Signals and sequences | Mel spectrogram |
| Pronunciation lexicon | covered | part19b_speech_vision_retrieval_and_nlp_toolkits / Speech recognition: from HMMs to Kaldi | Pronunciation lexicon |
| Noisy-channel model | covered | part19_machine_learning / Natural language processing foundation | Noisy-channel model |
| Hidden Markov models | covered | part19b_speech_vision_retrieval_and_nlp_toolkits / Speech recognition: from HMMs to Kaldi | Hidden Markov models |
| Viterbi algorithm | covered | part08_data_structures_algorithms | Viterbi on the decoding graph |
| GMM-HMM acoustic models | covered | part19b_speech_vision_retrieval_and_nlp_toolkits / Speech recognition: from HMMs to Kaldi | GMM-HMM |
| HMM-DNN hybrid systems | missing | → suggest part19 | HMM-DNN hybrid not named |
| Connectionist temporal classification (CTC) | covered | part19b_speech_vision_retrieval_and_nlp_toolkits / Speech recognition: from HMMs to Kaldi | CTC |
| Encoder-decoder ASR | partial | part19b_speech_vision_retrieval_and_nlp_toolkits | Encoder-decoder ASR not confirmed by name |
| Conformer | covered | part19b_speech_vision_retrieval_and_nlp_toolkits / Speech recognition: from HMMs to Kaldi | Conformer |
| Self-supervised speech representations | covered | part19b_speech_vision_retrieval_and_nlp_toolkits | Self-supervised speech representations |
| Word error rate | covered | part19_machine_learning / Specialised learning areas | Word error rate |
| Character error rate | missing | → suggest part19 | CER not named |
| Streaming latency | partial | part02_computer_organization | Latency numbers only; streaming ASR latency not named |
| Accent and noise robustness | missing | → suggest part19 | Accent and noise robustness not named |
| Speech synthesis (TTS) | covered | part19b_speech_vision_retrieval_and_nlp_toolkits / Speech synthesis, speakers and spoken-language systems | TTS |
| Spoken dialogue systems | covered | part19b_speech_vision_retrieval_and_nlp_toolkits / Speech synthesis, speakers and spoken-language systems | Spoken dialogue |
| Automatic differentiation | covered | part06_programming_languages_go / Go — the everyday standard library | Automatic differentiation |
| Weight initialisation | partial | part03_mathematics / Calculus and optimization | Initialisation only as restarts |
| Residual networks | covered | part19_machine_learning / Deep learning | Residual networks in CNN lineage |
| Sequence masking and padding | covered | part20_generative_ai_1of3 / How LLMs work | Sequence masking and padding |
| Backpropagation through time | covered | part19_machine_learning / Deep learning | Backpropagation through time |
| Encoder-only, decoder-only and encoder-decoder transformers | covered | part20_generative_ai_1of3 / How LLMs work | Encoder-only and decoder-only variants |
| Pretraining objectives | covered | part20_generative_ai_1of3 / How LLMs work | Pretraining objectives |
| Distributed training and memory | partial | part02_computer_organization / Machine organization | Data parallelism covered; training memory not named |
| Gradient checking | covered | part03_mathematics / Numerical computing | Gradient checking |
| Overfitting a tiny batch | partial | part04_problem_solving / Research method | Overfitting and leakage touched; tiny-batch check not named |
| Learning curves and seed variance | partial | part04_problem_solving / Research method | Seed variance only; learning curves not named |

## 5.6.2 Official Curriculum Crosswalk Into the Single Course

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Autoregressive factorisation | covered | part03c_signals_systems_and_communications / Practical spectral analysis | Autoregressive models (LPC) |
| Context windows and KV cache | partial | part20_generative_ai_1of3 / How LLMs work | Context windows named; KV cache not named |
| Scaling laws | missing | → suggest part20 | Scaling laws not named |
| Closed versus open models | covered | part20_generative_ai_1of3 / How LLMs work | Open-weight models |
| Instruction hierarchy and delimiters | covered | part21_generative_ai_2of3 / Prompt, context and output engineering | Instruction hierarchy and delimiters |
| Zero-shot and few-shot prompting | covered | part20_generative_ai_1of3 / How LLMs work | Zero-shot and few-shot |
| Prompt decomposition and chain-of-thought | covered | part21_generative_ai_2of3 / Prompt, context and output engineering | Chain-of-thought |
| Self-consistency | covered | part21_generative_ai_2of3 / Prompt, context and output engineering | Self-consistency |
| Structured outputs and constrained decoding | partial | part07_programming_languages_typescript_wire_theory_exercises | Schema validation covered; constrained decoding not named |
| Prompt versioning and regression tests | covered | part21_generative_ai_2of3 / Prompt, context and output engineering | Prompt versioning and regression tests |
| Chunking | partial | part21_generative_ai_2of3 | Chunking strategy not confirmed by name |
| Metadata and ACL filtering | partial | part14_security / Access-control models | Metadata-filter ACL not named |
| Supervised fine-tuning | covered | part20_generative_ai_1of3 / How LLMs work | Supervised fine-tuning |
| Preference data, RLHF and DPO | covered | part20_generative_ai_1of3 / Fine-tuning and adaptation | Preference data, RLHF and DPO |
| Reward modelling | covered | part20_generative_ai_1of3 / Fine-tuning and adaptation | Reward modelling |
| Catastrophic forgetting | missing | → suggest part20 | Catastrophic forgetting not named |
| Data contamination | partial | part14_security / AI and LLM application threats | Benchmark contamination not named; context contamination only |
| Safety regression testing | missing | → suggest part22 | Safety regression testing not named |
| Contrastive image-text learning (CLIP) | partial | part20_generative_ai_1of3 / Multimodal models | CLIP not confirmed by name |
| Vision-language models | covered | part20_generative_ai_1of3 / Multimodal models | Vision-language models |
| Image captioning and VQA | covered | part20_generative_ai_1of3 / Multimodal models | Image captioning and VQA |
| Diffusion models | covered | part20_generative_ai_1of3 / Generative models beyond autoregressive | Diffusion models |
| Augmented LLMs | missing | → suggest part22 | Augmented LLMs not named |
| Agent state and memory | partial | part22_generative_ai_3of3 / Agents and workflows | Agent state covered; memory mostly RAG |
| Least privilege and per-action authorisation | covered | part12_databases / The SQL language | Least privilege in SQL; authorisation in part14 |
| Human approval for agent actions | covered | part22_generative_ai_3of3 / Agents and workflows | Human approval for agent actions |
| Iteration, time and token budgets | missing | → suggest part22 | Token budgets not named |
| Offline evaluation sets | covered | part19_machine_learning / Applied problem families | Offline evaluation sets |
| Red-teaming | covered | part14_security / AI and LLM application threats | Red-teaming |
| Risk register | covered | part14_security / Security management, risk and governance | Risk register |

## 5.6.3 Detailed S17 Learning Order

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Image patches as tokens | partial | part20_generative_ai_1of3 | ViT patches only in passing |
| Classifier-free guidance | missing | → suggest part20 |  |
| Provenance and watermarking | missing | → suggest part20 | Provenance and watermarking not named |
| Retrieval metrics (recall@k, MRR, NDCG) | covered | part19_machine_learning / Classical machine learning | Retrieval metrics |
| Faithfulness and groundedness metrics | covered | part21_generative_ai_2of3 / Retrieval-augmented generation | Faithfulness and groundedness |
| Context precision and recall | covered | part21_generative_ai_2of3 / Retrieval-augmented generation | Context precision and recall |
| Answer relevance and correctness | partial | part21_generative_ai_2of3 / Retrieval-augmented generation | Answer relevancy named via RAGAS |
| Abstention | covered | part21_generative_ai_2of3 / Retrieval-augmented generation | Abstention |
| LLM-as-judge calibration | partial | part22_generative_ai_3of3 / Evaluation, testing and debugging | Model graders covered; calibration not named |
| Data curation and dataset cards | missing | → suggest part19 | Data curation and dataset cards not named |
| Multimodal evaluation | missing | → suggest part20 | Multimodal evaluation not named |
| Parallelisation (agent workflows) | partial | part22_generative_ai_3of3 / Agents and workflows | Parallelisation in agent workflows not named |
| LLM routing | missing | → suggest part22 | LLM routing not named |
| Evaluator-optimiser loops | missing | → suggest part22 | Evaluator-optimiser loops not named |
| Embedding and vector weaknesses | covered | part14_security / AI and LLM application threats | Embedding and vector weaknesses |
| System-prompt leakage | missing | → suggest part14 | System-prompt leakage not named |
| NIST AI RMF (Govern, Map, Measure, Manage) | covered | part14_security / Security management, risk and governance | NIST AI RMF |
| Bias and fairness evaluation | partial | part19_machine_learning / MLOps | Fairness covered via governance; bias evaluation not named |
| Model decommissioning | covered | part14_security / Security management, risk and governance | Model decommissioning |
| Reproducible training manifests | covered | part18_devops_sre / Docker | Reproducible training manifests |
| Dataset licence review | partial | part15_software_delivery / The profession | Software licences covered; dataset licences not named |

## 5.6.4 IIT-Aligned Portfolio Systems and Acceptance Evidence

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Load and soak testing | covered | part13_distributed_systems / Performance at scale | Load and soak testing |
| Domain-expert validation | missing | → suggest part04 | Domain-expert validation not named |
| Reproducible evaluation | missing | → suggest part19 | Reproducible evaluation not named |

## 5.7 S18-S24: Services, Security, Architecture, Operations, and Integration

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| HTTP content negotiation and conditional requests | covered | part09_networking / HTTP and the web | Content negotiation and conditional requests |
| Status codes | covered | part09_networking / HTTP and the web | Status codes |
| Retry-After and overload signalling | covered | part06_programming_languages_go / Go — concurrency | Retry-After and overload |
| Request framing and smuggling | covered | part09_networking / HTTP and the web | Request framing and smuggling |
| gRPC deadlines and cancellation | partial | part06_programming_languages_go / Go — engineering | gRPC deadlines and cancellation via gRPC notes; not a named group |
| Protobuf field presence and reserved numbers | covered | part07_programming_languages_typescript_wire_theory_exercises / Wire formats | Protobuf field presence |
| NIST SP 800-63B and AAL levels | covered | part14_security / Cryptography | NIST SP 800-63B and AAL |
| OAuth redirect and PKCE attacks | covered | part06_programming_languages_go / Go — engineering | OAuth redirect and PKCE |
| Token injection and mix-up attacks | covered | part14_security / Authentication and sessions | Token injection and mix-up |
| Refresh token rotation | partial | part14_security / Authentication and sessions | Refresh token rotation not named |
| Sender-constrained tokens | partial | part14_security / Cryptography | Sender-constrained tokens: mTLS only |
| Referer leakage and untrusted proxy headers | covered | part14_security / Authentication and sessions | Referer leakage and proxy headers |
| Unsafe 307 redirects | covered | part14_security / Web application security | Unsafe 307 redirects |
| Account recovery and session invalidation | partial | part14_security / Authentication and sessions | Session invalidation covered; account recovery partial |
| Modular monolith | covered | part11_software_architecture / Architecture fundamentals | Modular monolith |
| Leader election and consensus | covered | part13_distributed_systems / Consensus and coordination | Leader election and consensus |
| MapReduce | covered | part08_data_structures_algorithms / Algorithms at scale | MapReduce |
| Linearizable key-value store | covered | part13_distributed_systems / Foundations | Linearizability |
| Sharded key-value store | covered | part13_distributed_systems / Caching at scale | Sharded key-value store |
| Partitioning (sharding) | partial | part13_distributed_systems | Partitioning covered only indirectly |
| Failure injection and chaos testing | covered | part18_devops_sre / Site reliability engineering | Failure injection and chaos testing |
| Error budgets | covered | part18_devops_sre / Site reliability engineering | Error budgets |
| Cascading failure and overload | partial | part13_distributed_systems | Cascading failure covered only through overload notes |
| Postmortems and launch reviews | covered | part17_architects_practice / Learning from failure | Postmortems and launch reviews |
| Six-step system-design method | covered | part13_distributed_systems / System design method | Six-step system-design method |
| Read-heavy, write-heavy and realtime systems | covered | part13_distributed_systems / System design method | Read-heavy, write-heavy and realtime systems |
| Multi-tenant systems | covered | part13_distributed_systems / System design method | Multi-tenant systems |
| Globally distributed systems | covered | part12_databases / Analytics and other engines | Globally distributed systems |
| Batch processing | covered | part13_distributed_systems / Stream and batch processing | Batch processing |
| Sequence and state diagrams | partial | part11_software_architecture / Architecture documentation | Sequence diagrams via Mermaid; state diagrams not named |
| Quality attributes | covered | part11_software_architecture / Quality attributes and evaluation | Quality attributes |
| ML Test Score | covered | part19_machine_learning / MLOps | ML Test Score |
| Shadow and canary deployment | covered | part18_devops_sre | Shadow and canary deployment |
| Retraining policy | partial | part19_machine_learning / MLOps | Retraining covered; retraining policy not named |
| Data versioning | missing | → suggest part19 | Data versioning not named |
| Backup and restore | covered | part12_databases / Operating databases | Backup and restore |
| Operational readiness review | covered | part18_devops_sre / Site reliability engineering | Operational readiness review |
| Dashboards and runbooks | partial | part05_programming_languages_python_and_shell | Dashboards via Python callbacks only; runbooks not named |
| Requirements and threat models | missing | → suggest part14 | Requirements and threat models not named |
| Freshness monitoring | partial | part09_networking / HTTP and the web | Freshness via max-age; freshness monitoring not named |
| Nasiko P0-P10 control-plane phases (gateway, registry, A2A agents, CLI) | out of scope | - | Nasiko control-plane phases; Nasiko-specific |
| Game and real-time rendering (S24) | covered | part30_supplementary_applied_domains / Game engines and real-time rendering | Game and real-time rendering |
| Medical, mechanical and aerospace domains (S24) | out of scope | - | Clinical, mechanical and aerospace domains |
| Deep pure mathematics and extra number theory (S24) | partial | part03b_analysis_calculus_and_number_theory | Deep pure mathematics only partly covered by number theory |

## Missing in this range

- Data contracts (→ suggest part12) — from: 5. Single Graph-Ordered Learning Track
- Benchmark crossover points (→ suggest part08) — from: 5.3 S5-S10: Mathematical and Algorithmic Core
- Differential testing (→ suggest part11) — from: 5.3 S5-S10: Mathematical and Algorithmic Core
- Numerical quadrature (→ suggest part03) — from: 5.3 S5-S10: Mathematical and Algorithmic Core
- Transformations of random variables (→ suggest part03) — from: 5.3 S5-S10: Mathematical and Algorithmic Core
- Statistical power (→ suggest part03) — from: 5.3 S5-S10: Mathematical and Algorithmic Core
- Practical significance (→ suggest part03) — from: 5.3 S5-S10: Mathematical and Algorithmic Core
- Missing-data handling (→ suggest part19) — from: 5.4 S11-S14: Classical ML, Databases, Optimization, RL, and Causality
- Semi and anti joins (→ suggest part12) — from: 5.4 S11-S14: Classical ML, Databases, Optimization, RL, and Causality
- Outer joins (→ suggest part12) — from: 5.4 S11-S14: Classical ML, Databases, Optimization, RL, and Causality
- GIN, GiST and BRIN indexes (→ suggest part12) — from: 5.4 S11-S14: Classical ML, Databases, Optimization, RL, and Causality
- Robust and stochastic optimisation (→ suggest part03) — from: 5.4 S11-S14: Classical ML, Databases, Optimization, RL, and Causality
- Corner detection (→ suggest part19) — from: 5.5 S15-S16: Domain Mathematics and Deep Learning
- Feature descriptors and matching (→ suggest part19) — from: 5.5 S15-S16: Domain Mathematics and Deep Learning
- RANSAC (→ suggest part19) — from: 5.5 S15-S16: Domain Mathematics and Deep Learning
- Camera calibration (→ suggest part19) — from: 5.5 S15-S16: Domain Mathematics and Deep Learning
- HMM-DNN hybrid systems (→ suggest part19) — from: 5.5 S15-S16: Domain Mathematics and Deep Learning
- Character error rate (→ suggest part19) — from: 5.5 S15-S16: Domain Mathematics and Deep Learning
- Accent and noise robustness (→ suggest part19) — from: 5.5 S15-S16: Domain Mathematics and Deep Learning
- Scaling laws (→ suggest part20) — from: 5.6.2 Official Curriculum Crosswalk Into the Single Course
- Catastrophic forgetting (→ suggest part20) — from: 5.6.2 Official Curriculum Crosswalk Into the Single Course
- Safety regression testing (→ suggest part22) — from: 5.6.2 Official Curriculum Crosswalk Into the Single Course
- Augmented LLMs (→ suggest part22) — from: 5.6.2 Official Curriculum Crosswalk Into the Single Course
- Iteration, time and token budgets (→ suggest part22) — from: 5.6.2 Official Curriculum Crosswalk Into the Single Course
- Classifier-free guidance (→ suggest part20) — from: 5.6.3 Detailed S17 Learning Order
- Provenance and watermarking (→ suggest part20) — from: 5.6.3 Detailed S17 Learning Order
- Data curation and dataset cards (→ suggest part19) — from: 5.6.3 Detailed S17 Learning Order
- Multimodal evaluation (→ suggest part20) — from: 5.6.3 Detailed S17 Learning Order
- LLM routing (→ suggest part22) — from: 5.6.3 Detailed S17 Learning Order
- Evaluator-optimiser loops (→ suggest part22) — from: 5.6.3 Detailed S17 Learning Order
- System-prompt leakage (→ suggest part14) — from: 5.6.3 Detailed S17 Learning Order
- Domain-expert validation (→ suggest part04) — from: 5.6.4 IIT-Aligned Portfolio Systems and Acceptance Evidence
- Reproducible evaluation (→ suggest part19) — from: 5.6.4 IIT-Aligned Portfolio Systems and Acceptance Evidence
- Data versioning (→ suggest part19) — from: 5.7 S18-S24: Services, Security, Architecture, Operations, and Integration
- Requirements and threat models (→ suggest part14) — from: 5.7 S18-S24: Services, Security, Architecture, Operations, and Integration
- Distributed optimisation (ADMM) (→ suggest part03) — from: 5.1 Research Baseline and Evidence Hierarchy
- Product quantisation and IVF (→ suggest part20) — from: 5.1 Research Baseline and Evidence Hierarchy

## Partial in this range

- Text editor use — No dedicated editor topic; tooling only implied — part05_programming_languages_python_and_shell.topics.md
- Notebooks and scripts — Notebooks mentioned only in passing — part05_programming_languages_python_and_shell.topics.md
- Trigonometry — Only a remedial trigonometry line — part01_school_foundations.topics.md
- Row operations and Gaussian elimination — Row reduction appears only in an exercise — part03_mathematics.topics.md
- Spectral methods — Spectral theorem only — part03_mathematics.topics.md
- Runge-Kutta (RK4) — Runge-Kutta appears only in exercises — part03b_analysis_calculus_and_number_theory.topics.md
- Fisher information — Fisher information not named — part03_mathematics.topics.md
- Kaldi and OpenFst — Kaldi covered; OpenFst only in passing — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md
- Vector indexes and ANN search — ANN only in passing; HNSW and IVF not found — part20_generative_ai_1of3.topics.md
- Relational algebra — Relational algebra named only as a term — part12_databases.topics.md
- Common table expressions — WITH RECURSIVE present; CTE phrase absent — part12_databases.topics.md
- Window functions — Window functions not confirmed by name — part12_databases.topics.md
- Point-in-time recovery — Backup and restore present; point-in-time recovery not named — part12_databases.topics.md
- JSON-RPC — JSON-RPC not named — part07_programming_languages_typescript_wire_theory_exercises.topics.md
- API keys — API keys mentioned; signed requests not confirmed — part14_security.topics.md
- Security verification (ASVS) — ASVS mentioned once; not a named group — part14_security.topics.md
- Clean architecture — Clean architecture not named — part11_software_architecture.topics.md
- Domain-driven design — DDD not named — part11_software_architecture.topics.md
- Backpressure — Backpressure as flow control in part13; back-pressure only in a part07 exercise — part13_distributed_systems.topics.md
- Circuit breakers — Circuit breakers mentioned only in passing — part18_devops_sre.topics.md
- Model registry — Model registry mentioned only in passing — part19_machine_learning.topics.md
- pgvector and Qdrant — Qdrant covered; pgvector not confirmed — part20_generative_ai_1of3.topics.md
- Ray, PySpark and Dask — Dask covered; Ray not confirmed — part19_machine_learning.topics.md
- FastAPI — FastAPI not confirmed — part22_generative_ai_3of3.topics.md
- LangChain and LlamaIndex — LangChain covered; LlamaIndex not named — part22_generative_ai_3of3.topics.md
- vLLM — vLLM serving mentioned only in passing — part20_generative_ai_1of3.topics.md
- Distance metrics (Euclidean, Manhattan, cosine) — Cosine and norms appear in part20 RoPE and embeddings; no metric group — part01_school_foundations.topics.md
- Dot product — Dot product only in the RoPE context — part20_generative_ai_1of3.topics.md
- k-nearest neighbours — kNN only as a brute-force mention in part03 — part19_machine_learning.topics.md
- Generalised linear models — GLM covered in one line — part19_machine_learning.topics.md
- Database statistics — Cost-based planning only; ANALYZE statistics not named — part12_databases.topics.md
- Tool schemas — Tool schemas named only in passing — part22_generative_ai_3of3.topics.md
- Sensitive information disclosure — PII minimisation in part19 and part22; LLM-specific disclosure not named — part19_machine_learning.topics.md
- Misinformation — Misinformation mentioned once — part14_security.topics.md
- Unbounded consumption — Generic resource exhaustion only; LLM cost abuse not named — part14_security.topics.md
- Secure outbound calls — SSRF only — part14_security.topics.md
- Lineage and promotion gates — Lineage used only as a research term — part04_problem_solving.topics.md
- Training-serving skew and parity — Training–serving skew named; parity not — part19_machine_learning.topics.md
- Continuous training (CT) — Continuous training in one line — part19_machine_learning.topics.md
- Silent-failure drills — Silent pipeline failures noted; deliberate failure drills not named — part21_generative_ai_2of3.topics.md
- Environment variables — Environment variables only in secrets context — part14_security.topics.md
- Reproducible repository layout — Seeding covered; repo layout not named — part03_mathematics.topics.md
- Tolerance-based assertions — Timestamp tolerance only; no float tolerance — part06_programming_languages_go.topics.md
- Shape, dtype and axis reasoning — Shape and axis reasoning implicit only — part05_programming_languages_python_and_shell.topics.md
- Elementwise versus matrix multiplication — Elementwise product appears; contrast with matrix product not named — part20_generative_ai_1of3.topics.md
- Residual and reconstruction checks — Residual plots covered; reconstruction checks not named — part03_mathematics.topics.md
- Quickselect and selection — Quickselect not named — part08_data_structures_algorithms.topics.md
- Fundamental theorem of calculus — Fundamental theorem of calculus not confirmed by name — part03b_analysis_calculus_and_number_theory.topics.md
- Integration techniques — Integration techniques not confirmed by name — part03b_analysis_calculus_and_number_theory.topics.md
- Vector calculus (divergence, curl) — Vector calculus not confirmed by name — part03b_analysis_calculus_and_number_theory.topics.md
- Convergence plots and step-size stability — Step-size check only in an exercise — part03b_analysis_calculus_and_number_theory.topics.md
- Estimands and sampling — Survey sampling designs covered; estimands not named — part03_mathematics.topics.md
- Regression diagnostics — Regression diagnostics not named — part19_machine_learning.topics.md
- Probability calibration — Calibration named only — part03_mathematics.topics.md
- Kernel methods — KDE only; kernel methods not named — part03_mathematics.topics.md
- Functional dependencies and normalisation — Normal forms not verified by name — part12_databases.topics.md
- Aggregation and GROUP BY — GROUP BY not confirmed by name — part12_databases.topics.md
- Migrations and rollback — Migrations and rollback not named as a topic — part12_databases.topics.md
- Heap files and tuples — Heap files implicit only — part12_databases.topics.md
- Cardinality estimation and cost-based plans — Cost-based plans not named — part12_databases.topics.md
- EXPLAIN ANALYZE — EXPLAIN ANALYZE not named — part12_databases.topics.md
- Lagrangian duality and KKT conditions — Lagrange multipliers covered; KKT not named — part03_mathematics.topics.md
- Bellman equations — Bellman–Ford only; Bellman equations not named — part08_data_structures_algorithms.topics.md
- Overlap and sensitivity analysis — Overlap named; sensitivity analysis not named — part19_machine_learning.topics.md
- Laplace transform — Laplace transform not confirmed by name — part03c_signals_systems_and_communications.topics.md
- Pole-zero stability — Pole-zero stability not named — part03c_signals_systems_and_communications.topics.md
- Colour spaces and gamma — Colour spaces not named — part19_machine_learning.topics.md
- Histograms and point transforms — Histogram quantiles only — part03_mathematics.topics.md
- Frequency-domain image filtering — Pitch spectrum only; frequency-domain filtering not named — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md
- Image segmentation — Segmentation not named — part19_machine_learning.topics.md
- WordPiece and unigram tokenisation — Unigram LM only; WordPiece not named — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md
- Part-of-speech tagging — POS tagging not named — part19_machine_learning.topics.md
- Parsing (constituency and dependency) — Parsing only in passing — part07_programming_languages_typescript_wire_theory_exercises.topics.md
- Weighted finite-state transducers — Weighted automata named; WFST not named — part06_programming_languages_go.topics.md
- Encoder-decoder ASR — Encoder-decoder ASR not confirmed by name — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md
- Streaming latency — Latency numbers only; streaming ASR latency not named — part02_computer_organization.topics.md
- Weight initialisation — Initialisation only as restarts — part03_mathematics.topics.md
- Distributed training and memory — Data parallelism covered; training memory not named — part02_computer_organization.topics.md
- Overfitting a tiny batch — Overfitting and leakage touched; tiny-batch check not named — part04_problem_solving.topics.md
- Learning curves and seed variance — Seed variance only; learning curves not named — part04_problem_solving.topics.md
- Context windows and KV cache — Context windows named; KV cache not named — part20_generative_ai_1of3.topics.md
- Structured outputs and constrained decoding — Schema validation covered; constrained decoding not named — part07_programming_languages_typescript_wire_theory_exercises.topics.md
- Chunking — Chunking strategy not confirmed by name — part21_generative_ai_2of3.topics.md
- Metadata and ACL filtering — Metadata-filter ACL not named — part14_security.topics.md
- Data contamination — Benchmark contamination not named; context contamination only — part14_security.topics.md
- Contrastive image-text learning (CLIP) — CLIP not confirmed by name — part20_generative_ai_1of3.topics.md
- Agent state and memory — Agent state covered; memory mostly RAG — part22_generative_ai_3of3.topics.md
- Image patches as tokens — ViT patches only in passing — part20_generative_ai_1of3.topics.md
- Answer relevance and correctness — Answer relevancy named via RAGAS — part21_generative_ai_2of3.topics.md
- LLM-as-judge calibration — Model graders covered; calibration not named — part22_generative_ai_3of3.topics.md
- Parallelisation (agent workflows) — Parallelisation in agent workflows not named — part22_generative_ai_3of3.topics.md
- Bias and fairness evaluation — Fairness covered via governance; bias evaluation not named — part19_machine_learning.topics.md
- Dataset licence review — Software licences covered; dataset licences not named — part15_software_delivery.topics.md
- gRPC deadlines and cancellation — gRPC deadlines and cancellation via gRPC notes; not a named group — part06_programming_languages_go.topics.md
- Refresh token rotation — Refresh token rotation not named — part14_security.topics.md
- Sender-constrained tokens — Sender-constrained tokens: mTLS only — part14_security.topics.md
- Account recovery and session invalidation — Session invalidation covered; account recovery partial — part14_security.topics.md
- Partitioning (sharding) — Partitioning covered only indirectly — part13_distributed_systems.topics.md
- Cascading failure and overload — Cascading failure covered only through overload notes — part13_distributed_systems.topics.md
- Sequence and state diagrams — Sequence diagrams via Mermaid; state diagrams not named — part11_software_architecture.topics.md
- Retraining policy — Retraining covered; retraining policy not named — part19_machine_learning.topics.md
- Dashboards and runbooks — Dashboards via Python callbacks only; runbooks not named — part05_programming_languages_python_and_shell.topics.md
- Freshness monitoring — Freshness via max-age; freshness monitoring not named — part09_networking.topics.md
- Algorithm design paradigms — Paradigms appear as topics, not as a named group — part08_data_structures_algorithms.topics.md
- Self-supervised vision learning — Self-supervised speech only; vision SSL not named — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md
- Multilingual and low-resource evaluation — Low-resource attacks; multilingual evaluation not named — part14_security.topics.md
- Deep pure mathematics and extra number theory (S24) — Deep pure mathematics only partly covered by number theory — part03b_analysis_calculus_and_number_theory.topics.md
