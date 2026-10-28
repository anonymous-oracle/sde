# Topic diff: Reference maps, bibliography, atlases and policies

Source: gcp/unified-curriculum.md lines 386-882. Compared against: gcp-lite/index/*.topics.md and gcp-lite/Rust_Track_AI_Infrastructure.md.

Counts: 488 topics; 374 covered, 102 partial, 4 missing, 8 out of scope.

## 7.1 Go Module Detail Map

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Git and GitHub over SSH | partial | part15_software_delivery.topics.md › Git | Git covered in part15; SSH key setup for remotes is not named there (SSH keys sit in part10) |
| VS Code editor for Go | partial | part05_programming_languages_python_and_shell.topics.md › Python | Editor setup is taught for Python only; no Go editor setup |
| Go toolchain install and environment (GOROOT, GOPATH, go env) | covered | part06_programming_languages_go.topics.md › Go — toolchain and program structure |  |
| gofmt and formatting habits | covered | part06_programming_languages_go.topics.md › Go — toolchain and program structure |  |
| Program structure, constants and iota | covered | part06_programming_languages_go.topics.md › Go — toolchain and program structure |  |
| Integer arithmetic and overflow | covered | part06_programming_languages_go.topics.md › Go — toolchain and program structure |  |
| Control flow for, if, switch | covered | part06_programming_languages_go.topics.md › Go — toolchain and program structure |  |
| Arrays and the blank identifier | covered | part06_programming_languages_go.topics.md › Go — toolchain and program structure |  |
| Two pointers and prefix sums | covered | part08_data_structures_algorithms.topics.md › Linear structures and techniques |  |
| Slices and maps | covered | part06_programming_languages_go.topics.md › Go — composite data, functions, errors and text |  |
| Range loops | covered | part06_programming_languages_go.topics.md › Go — toolchain and program structure |  |
| Variadic functions and multiple returns | covered | part06_programming_languages_go.topics.md › Go — composite data, functions, errors and text |  |
| defer, panic and recover | covered | part06_programming_languages_go.topics.md › Go — composite data, functions, errors and text |  |
| Closures and init functions | covered | part06_programming_languages_go.topics.md › Go — composite data, functions, errors and text |  |
| Recursion | covered | part08_data_structures_algorithms.topics.md › Linear structures and techniques |  |
| Error values and wrapping | covered | part06_programming_languages_go.topics.md › Go — composite data, functions, errors and text |  |
| Strings, runes and fmt | covered | part06_programming_languages_go.topics.md › Go — composite data, functions, errors and text |  |
| Stacks, queues, sliding windows, backtracking | covered | part06_programming_languages_go.topics.md › Go — engineering | Sliding windows and backtracking are in part08 |
| Pointers, structs and methods | covered | part06_programming_languages_go.topics.md › Go — memory, types with behaviour and generics |  |
| Interfaces and struct embedding | covered | part06_programming_languages_go.topics.md › Go — memory, types with behaviour and generics |  |
| Struct tags | covered | part06_programming_languages_go.topics.md › Go — memory, types with behaviour and generics |  |
| Generics | covered | part06_programming_languages_go.topics.md › Go — memory, types with behaviour and generics |  |
| Type conversions | covered | part06_programming_languages_go.topics.md › Go — toolchain and program structure |  |
| Linked lists | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Binary search trees and red-black trees | covered | part08_data_structures_algorithms.topics.md › Trees and heaps |  |
| Heaps and priority queues | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Union-find (disjoint sets) | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Hash tables | covered | part06_programming_languages_go.topics.md › Go — composite data, functions, errors and text |  |
| File I/O with bufio | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library |  |
| Paths, directories and temp files | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library |  |
| embed package | covered | part06_programming_languages_go.topics.md › Go — memory, types with behaviour and generics |  |
| text/template | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library |  |
| Regular expressions | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library |  |
| time package | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library |  |
| Tries | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| KMP string matching | covered | part08_data_structures_algorithms.topics.md › Sorting, searching and strings |  |
| Rolling hash (Rabin-Karp) | covered | part08_data_structures_algorithms.topics.md › Sorting, searching and strings |  |
| Slotted-page serialization | covered | part12_databases.topics.md › Storage and access methods |  |
| Write-ahead log serialization | covered | part12_databases.topics.md › Recovery and replication |  |
| CLI flags and subcommands | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library |  |
| Environment variables | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library |  |
| Structured logging (slog) | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library |  |
| JSON encoding and decoding | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library |  |
| XML encoding | covered | part07_programming_languages_typescript_wire_theory_exercises.topics.md › Wire formats |  |
| Goroutines, channels and select | covered | part06_programming_languages_go.topics.md › Go — concurrency |  |
| context package | covered | part06_programming_languages_go.topics.md › Go — concurrency |  |
| Worker pools | covered | part06_programming_languages_go.topics.md › Go — concurrency |  |
| Sync primitives (WaitGroup, Mutex, atomics) | covered | part06_programming_languages_go.topics.md › Go — concurrency |  |
| sync.Cond, sync.Once and sync.Pool | covered | part06_programming_languages_go.topics.md › Go — concurrency |  |
| Rate limiters (token bucket) | covered | part06_programming_languages_go.topics.md › Go — concurrency |  |
| Sorting and the sort package | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Binary search | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Recurrences and the master theorem | covered | part08_data_structures_algorithms.topics.md › Analysis |  |
| Greedy algorithms and minimum spanning trees | covered | part08_data_structures_algorithms.topics.md › Graph algorithms |  |
| Testing with go test | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Benchmarking | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| OS signals | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library |  |
| Reflection | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Asymptotic analysis (big-O) | covered | part08_data_structures_algorithms.topics.md › Analysis |  |
| Loop and data-structure invariants | covered | part03_mathematics.topics.md › Proof and discrete mathematics |  |
| Dynamic programming | covered | part08_data_structures_algorithms.topics.md › Greedy algorithms and dynamic programming |  |
| Discrete probability | covered | part03_mathematics.topics.md › Proof and discrete mathematics |  |
| Pipelines, fan-in and fan-out | covered | part06_programming_languages_go.topics.md › Go — concurrency |  |
| Race detector | covered | part06_programming_languages_go.topics.md › Go — concurrency |  |
| Deadlocks | covered | part06_programming_languages_go.topics.md › Go — concurrency |  |
| net/http server and client | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| TLS in Go | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Graph algorithms (BFS, DFS, Dijkstra, topological sort) | covered | part08_data_structures_algorithms.topics.md › Graph algorithms |  |
| REST API design | covered | part11_software_architecture.topics.md › API design |  |
| HTTP middleware | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| database/sql CRUD | covered | part06_programming_languages_go.topics.md › Go — concurrency |  |
| Pagination (offset and cursor) | covered | part12_databases.topics.md › Operating databases | Offset and cursor pagination are in part11 API design |
| Relational algebra | covered | part12_databases.topics.md › Relational theory |  |
| Protocol Buffers | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| RPC | covered | part11_software_architecture.topics.md › API design |  |
| Protobuf compatibility and schema evolution | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| gRPC services | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| gRPC streaming | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| gRPC metadata | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Input validation | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| MongoDB and NoSQL CRUD | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library |  |
| gRPC interceptors | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| REST and gRPC gateway | partial | part19_machine_learning.topics.md › Exercises | Served side by side in an exercise; no gRPC gateway or transcoding |
| OpenTelemetry | covered | part18_devops_sre.topics.md › Observability |  |
| pprof profiling | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Distributed tracing | covered | part18_devops_sre.topics.md › Observability |  |
| Argon2 password hashing | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| JWT | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| CSRF | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| XSS | covered | part14_security.topics.md › Web application security |  |
| govulncheck | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Secrets management | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library |  |
| Audit logging | covered | part14_security.topics.md › Detection and incident response |  |
| Docker | covered | part18_devops_sre.topics.md › Docker |  |
| Cross-compilation | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| GoReleaser | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Payment ledger and reconciliation | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Idempotent charges and webhooks | covered | part06_programming_languages_go.topics.md › Go — engineering |  |

## 7.2 PostgreSQL Slice Detail Map

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Semi and anti joins | partial | part12_databases.topics.md › The SQL language | Named in a join list only; no semi or anti join lab |
| Outer joins | partial | part12_databases.topics.md › Relational theory | Outer joins named in a list; no outer-join semantics or NULL-extension lab |
| Bag versus set semantics | covered | part12_databases.topics.md › Pre-SQL foundations |  |
| NULL and three-valued logic | covered | part12_databases.topics.md › Pre-SQL foundations |  |
| PostgreSQL system catalogs and namespaces | covered | part12_databases.topics.md › Storage and access methods |  |
| Hidden tuple columns (ctid, xmin, xmax) | partial | part12_databases.topics.md › Storage and access methods | Catalogs and system columns named; ctid, xmin and xmax not taught |
| JSONB, range and UUID types | covered | part12_databases.topics.md › The SQL language |  |
| PK, FK, CHECK and DOMAIN constraints | covered | part12_databases.topics.md › Relational theory |  |
| Deferrable constraints | covered | part12_databases.topics.md › Relational theory |  |
| Common table expressions | covered | part12_databases.topics.md › The SQL language |  |
| Recursive CTEs | covered | part12_databases.topics.md › Relational theory |  |
| Window functions and frames | covered | part12_databases.topics.md › The SQL language |  |
| Lateral joins | partial | part12_databases.topics.md › The SQL language | Named in a join list only; no lateral join lab |
| EXPLAIN ANALYZE and buffers | covered | part12_databases.topics.md › Query processing |  |
| Relation forks and segments in PGDATA | covered | part12_databases.topics.md › Storage and access methods |  |
| Free-space and visibility maps | covered | part12_databases.topics.md › Storage and access methods |  |
| TOAST | covered | part12_databases.topics.md › Storage and access methods |  |
| Buffer pool and clock-sweep eviction | covered | part12_databases.topics.md › Storage and access methods |  |
| Background writer and checkpointer | covered | part12_databases.topics.md › Storage and access methods |  |
| B-tree with Lehman-Yao links | covered | part12_databases.topics.md › Storage and access methods |  |
| Hash indexes | covered | part12_databases.topics.md › Storage and access methods |  |
| GIN, GiST, SP-GiST and BRIN indexes | covered | part12_databases.topics.md › Storage and access methods |  |
| Bitmap and index-only scans | partial | part12_databases.topics.md › Storage and access methods | Bitmap scans taught; index-only scans not named |
| Volcano iterator execution model | covered | part12_databases.topics.md › Query processing |  |
| External merge sort | covered | part08_data_structures_algorithms.topics.md › Sorting, searching and strings |  |
| Join algorithms (nested-loop, hash, merge) | covered | part12_databases.topics.md › Query processing |  |
| Aggregation strategies | covered | part12_databases.topics.md › Query processing |  |
| Query pipeline (parse, rewrite, plan) | partial | part12_databases.topics.md › Relational theory | Rewrite rules named in relational theory; parse-rewrite-plan pipeline not taught |
| Table statistics (MCV, histograms, correlation) | covered | part12_databases.topics.md › Query processing |  |
| Join-order search and GEQO | partial | part08_data_structures_algorithms.topics.md › Greedy algorithms and dynamic programming | Dynamic-programming join-order search named; GEQO not |
| Parallel query execution | covered | part12_databases.topics.md › Query processing |  |
| MVCC snapshots and visibility | covered | part12_databases.topics.md › Transactions and concurrency control |  |
| Serializable snapshot isolation (SSI) | covered | part12_databases.topics.md › Transactions and concurrency control |  |
| Row and table locks | covered | part12_databases.topics.md › The SQL language |  |
| Deadlock detection | covered | part12_databases.topics.md › Transactions and concurrency control |  |
| HOT updates | covered | part12_databases.topics.md › Storage and access methods |  |
| Autovacuum and XID freezing | covered | part12_databases.topics.md › Transactions and concurrency control |  |
| Synchronous commit | covered | part12_databases.topics.md › Recovery and replication |  |
| Full-page writes | covered | part12_databases.topics.md › Recovery and replication |  |
| Checkpoints | covered | part12_databases.topics.md › Recovery and replication |  |
| Streaming replication | covered | part12_databases.topics.md › Recovery and replication |  |
| WAL archiving and point-in-time recovery | covered | part12_databases.topics.md › Recovery and replication |  |

## 9. Textbook and Chapter Atlas

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Limits, continuity and derivatives | covered | part01_school_foundations.topics.md › (no group heading) | Taught at school level in part01 |
| Fundamental theorem of calculus (integrals) | covered | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations |  |
| Sequences and series convergence | covered | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations |  |
| Complex numbers | covered | part01_school_foundations.topics.md › (no group heading) | School level in part01 |
| Dedekind cuts and real-number construction | covered | part03b_analysis_calculus_and_number_theory.topics.md › Real analysis |  |
| Ordered fields and completeness | covered | part03b_analysis_calculus_and_number_theory.topics.md › Real analysis |  |
| Metric-space topology | covered | part03b_analysis_calculus_and_number_theory.topics.md › Real analysis |  |
| Riemann-Stieltjes integral | covered | part03b_analysis_calculus_and_number_theory.topics.md › Real analysis |  |
| Uniform convergence | covered | part03b_analysis_calculus_and_number_theory.topics.md › Real analysis |  |
| Power series and special functions | covered | part03b_analysis_calculus_and_number_theory.topics.md › Real analysis |  |
| Multivariable differentiation (Jacobian, inverse function theorem) | partial | part03_mathematics.topics.md › Probability | Change-of-variable Jacobian named; inverse and implicit function theorems not |
| Differential forms and Stokes' theorem | covered | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations |  |
| Lebesgue integration and measure | covered | part03b_analysis_calculus_and_number_theory.topics.md › Real analysis |  |
| Vectors and linear systems (elimination) | covered | part03_mathematics.topics.md › Linear algebra |  |
| Vector spaces and subspaces | covered | part03_mathematics.topics.md › Linear algebra |  |
| Orthogonality and projections | covered | part03_mathematics.topics.md › Linear algebra |  |
| Determinants | covered | part03_mathematics.topics.md › Linear algebra |  |
| Eigenvalues and eigenvectors | covered | part03_mathematics.topics.md › Linear algebra |  |
| Singular value decomposition | covered | part03_mathematics.topics.md › Linear algebra |  |
| Linear transformations and matrix of a map | covered | part03_mathematics.topics.md › Linear algebra |  |
| Plausible reasoning and Bayesian product and sum rules | covered | part03_mathematics.topics.md › Probability |  |
| Maximum-entropy priors | covered | part03_mathematics.topics.md › Probability |  |
| Sufficiency | covered | part03_mathematics.topics.md › Statistics and experimental design |  |
| Bayesian decision theory | covered | part03_mathematics.topics.md › Decision mathematics |  |
| Bootstrap and jackknife | covered | part03_mathematics.topics.md › Statistics and experimental design |  |
| Nonparametric inference | covered | part03_mathematics.topics.md › Statistics and experimental design |  |
| Exploratory data analysis | covered | part03_mathematics.topics.md › Statistics and experimental design |  |
| Transformations of random variables | covered | part03_mathematics.topics.md › Probability |  |
| Exponential family | covered | part03_mathematics.topics.md › Statistics and experimental design |  |
| Joint and conditional distributions | partial | part03_mathematics.topics.md › Probability | Conditional probability taught; joint distributions not named as a topic |
| Sampling distributions | partial | part03_mathematics.topics.md › Statistics and experimental design | Named through the t and F distributions; no general sampling-distribution treatment |
| Point estimation (MLE, method of moments) | covered | part03_mathematics.topics.md › Statistics and experimental design |  |
| Hypothesis tests and confidence intervals | covered | part03_mathematics.topics.md › Statistics and experimental design |  |
| ANOVA | covered | part03_mathematics.topics.md › Statistics and experimental design |  |
| Maximum flow | covered | part08_data_structures_algorithms.topics.md › Graph algorithms |  |
| Approximation algorithms | missing | → suggest part08 |  |
| Amortized analysis | covered | part08_data_structures_algorithms.topics.md › Analysis |  |
| Randomized algorithms | partial | part08_data_structures_algorithms.topics.md › Sorting, searching and strings | Randomized quicksort only; randomized algorithms as a topic not taught |
| Number-theoretic algorithms (primes, modular arithmetic) | covered | part03_mathematics.topics.md › Proof and discrete mathematics |  |
| Hilbert spaces | covered | part03b_analysis_calculus_and_number_theory.topics.md › Complex and functional analysis |  |
| Best approximation and least-squares projection | covered | part03_mathematics.topics.md › Linear algebra |  |
| Constrained optimization and KKT conditions | covered | part03_mathematics.topics.md › Calculus and optimization |  |
| Newton's method | covered | part03_mathematics.topics.md › Calculus and optimization |  |
| Steepest descent | covered | part03_mathematics.topics.md › Calculus and optimization |  |
| Conjugate gradient | covered | part03_mathematics.topics.md › Calculus and optimization |  |
| Ordinary differential equations | covered | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations |  |
| Partial differential equations | covered | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations |  |
| Vector calculus (gradient, divergence, curl) | covered | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations |  |
| Fourier series | covered | part03c_signals_systems_and_communications.topics.md › Transforms and system analysis |  |
| Laplace transform | covered | part03c_signals_systems_and_communications.topics.md › Transforms and system analysis |  |
| z-transform | covered | part03c_signals_systems_and_communications.topics.md › Transforms and system analysis |  |
| Numerical methods (root finding, quadrature) | partial | part03_mathematics.topics.md › Numerical computing | Root finding and interpolation named; quadrature not |
| LTI systems and convolution | covered | part03c_signals_systems_and_communications.topics.md › Signals and linear time-invariant systems |  |
| DFT and FFT | covered | part03_mathematics.topics.md › Signals and sequences |  |
| Sampling theorem and aliasing | covered | part03_mathematics.topics.md › Signals and sequences |  |
| Digital filter design | covered | part03c_signals_systems_and_communications.topics.md › Digital filters and multirate processing |  |
| Short-time Fourier transform | covered | part03_mathematics.topics.md › Signals and sequences |  |
| Cepstrum | covered | part03c_signals_systems_and_communications.topics.md › Practical spectral analysis |  |
| Multirate processing | covered | part03c_signals_systems_and_communications.topics.md › Digital filters and multirate processing |  |
| Fixed-point arithmetic effects | covered | part03c_signals_systems_and_communications.topics.md › Digital filters and multirate processing |  |
| Signal-space and modulation | covered | part03c_signals_systems_and_communications.topics.md › Digital communications |  |
| Receivers and synchronization | covered | part03c_signals_systems_and_communications.topics.md › Digital communications |  |
| Channel coding | partial | part03_mathematics.topics.md › Information theory | Linear and LDPC codes named; channel coding theorem not taught |
| Fading and MIMO | covered | part03c_signals_systems_and_communications.topics.md › Digital communications |  |
| Harmonics and spectra | covered | part03c_signals_systems_and_communications.topics.md › Transforms and system analysis |  |
| Noise models | partial | part03c_signals_systems_and_communications.topics.md › Digital filters and multirate processing | Quantization noise only; Gaussian and AWGN noise models not named |
| Autocorrelation | covered | part03c_signals_systems_and_communications.topics.md › Signals and linear time-invariant systems |  |
| Discrete cosine transform | partial | part03_mathematics.topics.md › Signals and sequences | Spectrograms and MFCC named; DCT not |
| Asymptotic equipartition property | covered | part03_mathematics.topics.md › Information theory |  |
| Source coding and compression | covered | part03_mathematics.topics.md › Information theory |  |
| Rate-distortion theory | covered | part03_mathematics.topics.md › Information theory |  |
| Information inequalities (Jensen, data processing) | covered | part03_mathematics.topics.md › Information theory |  |
| Graphical models | covered | part19_machine_learning.topics.md › Classical AI: search, knowledge and reasoning |  |
| Mixture models and EM | partial | part19_machine_learning.topics.md › Classical machine learning | Gaussian mixtures named under clustering; EM not taught |
| Kernel methods and SVMs | covered | part19_machine_learning.topics.md › Classical machine learning |  |
| Generalized linear models | partial | part19_machine_learning.topics.md › Classical machine learning | Logistic regression only; GLM family not named |
| Cross-validation (model assessment) | covered | part19_machine_learning.topics.md › Classical machine learning |  |
| Clustering (k-means) | covered | part19_machine_learning.topics.md › Classical machine learning |  |
| MCMC sampling | partial | part19_machine_learning.topics.md › Classical AI: search, knowledge and reasoning | Approximate inference named; MCMC mentioned only in passing |
| Variational inference | partial | part19_machine_learning.topics.md › Classical machine learning | Probabilistic programming named; variational inference not |
| Decision trees | covered | part19_machine_learning.topics.md › Classical machine learning |  |
| Numerical stability (overflow, conditioning) | covered | part03_mathematics.topics.md › Calculus and optimization |  |
| Regularization and dropout | partial | part03_mathematics.topics.md › Calculus and optimization | L1 and L2 named; dropout not |
| Convolutional networks | covered | part19_machine_learning.topics.md › Deep learning |  |
| Recurrent networks | covered | part19_machine_learning.topics.md › Deep learning |  |
| Transformers and attention | covered | part19_machine_learning.topics.md › Deep learning |  |
| Generative models (VAE, GAN, diffusion) | covered | part20_generative_ai_1of3.topics.md › Generative models beyond autoregression |  |
| Reinforcement learning | covered | part19_machine_learning.topics.md › Classical machine learning |  |
| Backpropagation | covered | part19_machine_learning.topics.md › Deep learning |  |
| Residual connections | covered | part19_machine_learning.topics.md › Deep learning |  |
| Normalization layers (batch, layer) | covered | part19_machine_learning.topics.md › Deep learning |  |
| Graph neural networks | partial | part19_machine_learning.topics.md › Specialised learning areas | Graph learning and PageRank named; message-passing GNNs not |
| Intelligent agents and environments | covered | part19_machine_learning.topics.md › Classical AI: search, knowledge and reasoning |  |
| Constraint satisfaction problems | covered | part19_machine_learning.topics.md › Classical AI: search, knowledge and reasoning |  |
| Adversarial search (minimax, alpha-beta) | covered | part19_machine_learning.topics.md › Classical AI: search, knowledge and reasoning |  |
| First-order and propositional logic | partial | part19_machine_learning.topics.md › Classical AI: search, knowledge and reasoning | Propositional logic covered; first-order logic not named |
| Automated planning | covered | part19_machine_learning.topics.md › Classical AI: search, knowledge and reasoning |  |
| Utility theory and maximum expected utility | covered | part17_architects_practice.topics.md › Decision theory |  |
| AI ethics and safety | covered | part19_machine_learning.topics.md › Classical AI: search, knowledge and reasoning |  |
| N-gram language models | covered | part03_mathematics.topics.md › Signals and sequences |  |
| Part-of-speech tagging | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Classical NLP and toolkits |  |
| Syntactic parsing (CKY, dependency) | covered | part19_machine_learning.topics.md › Natural language processing foundations |  |
| Text classification | covered | part19_machine_learning.topics.md › Natural language processing foundations |  |
| Tokenization (BPE) | covered | part20_generative_ai_1of3.topics.md › How LLMs work |  |
| Post-training (RLHF, instruction tuning) | covered | part20_generative_ai_1of3.topics.md › How LLMs work |  |
| Discourse and coreference | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Classical NLP and toolkits |  |
| Image formation and camera models | covered | part19_machine_learning.topics.md › Classical computer vision and geometry |  |
| Edge detection and image filtering | covered | part03_mathematics.topics.md › Signals and sequences |  |
| Local features (SIFT, Harris) | partial | part19_machine_learning.topics.md › Classical computer vision and geometry |  |
| Image segmentation | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Computer vision: images, motion and multi-view geometry |  |
| Object detection | covered | part19_machine_learning.topics.md › Classical computer vision and geometry |  |
| Stereo vision | covered | part19_machine_learning.topics.md › Classical computer vision and geometry |  |
| Structure from motion and SLAM | partial | part19_machine_learning.topics.md › Classical computer vision and geometry |  |
| Multi-view reconstruction | partial | part19_machine_learning.topics.md › Classical computer vision and geometry |  |
| Rendering | covered | part30_supplementary_applied_domains.topics.md › Game engines and real-time rendering |  |
| Data engineering for ML | covered | part19_machine_learning.topics.md › Machine learning in Python |  |
| Feature engineering | covered | part19_machine_learning.topics.md › Classical machine learning |  |
| Continual learning | covered | part19_machine_learning.topics.md › Deep learning |  |
| Human-in-the-loop and the human side of ML | partial | part19_machine_learning.topics.md › MLOps | Governance and retraining policy named; human-in-the-loop labeling not |
| Adversarial bandits (EXP3) | partial | part19_machine_learning.topics.md › Applied problem families | Adversarial bandits named; EXP3 algorithm not |
| Pure exploration and best-arm identification | covered | part19_machine_learning.topics.md › Applied problem families |  |
| Bandit lower bounds | partial | part19_machine_learning.topics.md › Applied problem families | Bandit regret named; lower bounds not |
| Ridge and lasso shrinkage | partial | part03_mathematics.topics.md › Calculus and optimization | L1 and L2 named; ridge and lasso as shrinkage estimators not |
| Survival analysis | covered | part19_machine_learning.topics.md › Applied problem families |  |
| Multiple testing (FDR) | covered | part03_mathematics.topics.md › Statistics and experimental design |  |
| Splines and generalized additive models | partial | part19_machine_learning.topics.md › Classical machine learning | Splines named; GAMs not |
| Boosting, bagging and random forests | covered | part19_machine_learning.topics.md › Classical machine learning |  |
| Hidden Markov models | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech recognition: from HMMs to Kaldi |  |
| Acoustic modeling | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech recognition: from HMMs to Kaldi |  |
| Robustness in speech recognition | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech science and analysis | Robustness named; speech-recognition noise robustness not taught |
| Decoding and search (WFST) | covered | part08_data_structures_algorithms.topics.md › Computability and complexity |  |
| Spoken language understanding | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech synthesis, speakers and spoken-language systems |  |
| Monte Carlo and temporal-difference learning | partial | part03_mathematics.topics.md › Probability | Monte Carlo named; temporal-difference learning not |
| Policy gradient methods | partial | part19_machine_learning.topics.md › Specialised learning areas | Reinforcement learning named; policy gradients not |
| Markov chains | covered | part03_mathematics.topics.md › Probability |  |
| Krylov subspace methods | partial | part03_mathematics.topics.md › Calculus and optimization | Conjugate gradient named; Krylov subspaces not |
| Line search and trust regions | missing | → suggest part03 |  |
| Quasi-Newton methods (BFGS) | partial | part03_mathematics.topics.md › Calculus and optimization | Newton's method named; quasi-Newton updates not |
| Convex sets and functions | covered | part03_mathematics.topics.md › Calculus and optimization |  |
| Lagrangian duality | partial | part03_mathematics.topics.md › Probability | Lagrange multipliers and KKT named; duality not |
| Interior-point methods | covered | part03_mathematics.topics.md › Calculus and optimization |  |
| Finite automata and regular languages | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library | Regex engine as NFA and DFA, in part06 |
| Context-free grammars and pushdown automata | covered | part07_programming_languages_typescript_wire_theory_exercises.topics.md › Language theory |  |
| Turing machines and undecidability | covered | part07_programming_languages_typescript_wire_theory_exercises.topics.md › Language theory |  |
| Compiler phases and code generation | out of scope | - | ARCHIVE-tagged in the curriculum (Aho, Lam, Sethi, Ullman row) |
| Hennessy-Patterson architecture (pipeline, cache) | out of scope | - | ARCHIVE-tagged; part02 covers pipelines and caches anyway |
| Groups, rings and fields (abstract algebra) | out of scope | - | ARCHIVE-tagged (Dummit and Foote row) |
| Point-set and algebraic topology | out of scope | - | ARCHIVE-tagged (Munkres row) |
| Mathematical logic and set theory | out of scope | - | ARCHIVE-tagged (Enderton row) |
| Zero-knowledge proofs and hardness assumptions | out of scope | - | ARCHIVE-tagged (Katz and Lindell row) |

## 10. Python Library and ML Tool Atlas

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Numerical and data libraries (NumPy, Pandas, SciPy) | partial | part05_programming_languages_python_and_shell.topics.md › Python | NumPy named; Pandas and SciPy not |
| Visualization libraries (Matplotlib, Seaborn, Plotly) | partial | part05_programming_languages_python_and_shell.topics.md › Python | Matplotlib and Plotly named; Seaborn not |
| Classical ML libraries (scikit-learn, XGBoost, LightGBM) | partial | part19_machine_learning.topics.md › Machine learning in Python | XGBoost named; LightGBM not |
| Deep learning frameworks (PyTorch, TensorFlow, Keras) | covered | part19_machine_learning.topics.md › Machine learning in Python |  |
| NLP and transformer libraries (NLTK, spaCy, Hugging Face) | covered | part19_machine_learning.topics.md › Machine learning in Python |  |
| Distributed data processing (PySpark, Dask) | covered | part19_machine_learning.topics.md › Machine learning in Python |  |
| MLOps tooling (MLflow, Weights & Biases, Evidently) | partial | part19_machine_learning.topics.md › MLOps | Evidently not named |
| Serving and agent frameworks (FastAPI, LangChain, LlamaIndex, vLLM, Ray) | partial | part05_programming_languages_python_and_shell.topics.md › Python | FastAPI named; LangChain, LlamaIndex, vLLM and Ray not |

## 11. Go Tool, Platform, and System Atlas

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Go HTTP routers and frameworks (Chi, Gin, Fiber) | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| JSON-RPC | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Typed service boundaries and contract tests | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Redis caching and streams | covered | part18_devops_sre.topics.md › Observability |  |
| Vector stores (pgvector, Qdrant) | partial | part12_databases.topics.md › Analytics and other engines | Vector similarity with pgvector named; Qdrant not |
| Docker Compose | covered | part18_devops_sre.topics.md › Docker |  |
| BuildKit image builds | covered | part18_devops_sre.topics.md › Docker |  |
| Kubernetes | covered | part18_devops_sre.topics.md › (no group heading) |  |
| Helm charts | covered | part18_devops_sre.topics.md › Kubernetes |  |
| Terraform | covered | part18_devops_sre.topics.md › Infrastructure as code |  |
| Kong and Nginx gateways | covered | part18_devops_sre.topics.md › NGINX and API gateways |  |
| Phoenix LLM tracing | partial | part18_devops_sre.topics.md › Observability | Named in passing with other trace UIs |
| Dashboards and alerting | covered | part18_devops_sre.topics.md › Site reliability engineering |  |
| Cobra and Viper | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library |  |
| Go numerical and ML libraries (Gonum, Gorgonia, GoMLX, ONNX) | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library |  |
| Model serving over HTTP behind a Go interface | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library |  |

## 11.1.1 Threat Modeling and Security Foundations

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Assets, trust boundaries and data-flow diagrams | covered | part14_security.topics.md › Threat modelling |  |
| STRIDE threat modelling | partial | part14_security.topics.md › Threat modelling | STRIDE named once; per-element walk-through not taught |
| Attacker capabilities and misuse cases | covered | part14_security.topics.md › Threat modelling |  |
| Threat register and residual risk | covered | part14_security.topics.md › Principles and economics |  |
| Likelihood, impact and blast radius | covered | part14_security.topics.md › Threat modelling |  |
| Defence in depth and least privilege | covered | part14_security.topics.md › Principles and economics |  |
| Deny by default and fail closed | covered | part14_security.topics.md › Authorization flaws |  |
| Secure defaults and separation of duties | partial | part14_security.topics.md › Principles and economics | Fail-safe defaults named; separation of duties not taught |
| Security usability and accessibility | partial | part14_security.topics.md › Principles and economics | one clause in the security economics bullet; not taught as a practice |
| CIA triad and privacy | covered | part14_security.topics.md › Principles and economics |  |

## 11.1.2 Hardened Go HTTP and Middleware Mechanics

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Middleware chaining and request context | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Response-writer wrappers and status capture | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Panic recovery middleware | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Request IDs and trusted-proxy handling | partial | part14_security.topics.md › Web application security | Trusted-proxy headers named; request IDs not |
| Security headers (HSTS, CSP) | covered | part14_security.topics.md › Web application security |  |
| Request size and header limits | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| HTTP status code semantics (400-500) | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Access logging and secret redaction | partial | part14_security.topics.md › Detection and incident response | Log coverage named; access logging and redaction not taught |
| Request deadlines and load shedding | covered | part13_distributed_systems.topics.md › Asynchronism and flow control |  |
| Rate limiting (per client and per account) | covered | part14_security.topics.md › API abuse |  |
| HTTP server timeouts | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Strict JSON decoding | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library |  |
| Graceful shutdown | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Outbound HTTP client hardening | partial | part06_programming_languages_go.topics.md › Go — engineering | Client timeouts named; redirect and destination allow-listing not |
| SSRF defence | covered | part14_security.topics.md › Web application security |  |
| DNS rebinding | covered | part14_security.topics.md › Cloud-specific attacks |  |
| Host header validation | missing | → suggest part14 |  |
| HTTP method semantics (safe and idempotent) | partial | part11_software_architecture.topics.md › Exercises | Idempotent PUT in an exercise; safe-method rules not taught |

## 11.1.3 Identity, Passwords, Recovery, and MFA

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Identities, credentials and sessions model | partial | part14_security.topics.md › Authentication and sessions | Credentials and sessions covered; no explicit subject and identifier model |
| Password policy (NIST SP 800-63B) | covered | part14_security.topics.md › Threat modelling |  |
| Argon2id password hashing | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Password hash parameter upgrade and pepper | covered | part14_security.topics.md › Cryptography |  |
| Constant-time comparison | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Account enumeration and timing defences | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Login throttling and lockout | partial | part14_security.topics.md › Authentication and sessions | Rate limits named; account lockout not |
| Recent authentication and step-up | partial | part14_security.topics.md › Authentication and sessions | Step-up named only through recovery; no recent-authentication gate |
| Account recovery tokens | covered | part14_security.topics.md › Authentication and sessions |  |
| Authenticator lifecycle and revocation | partial | part14_security.topics.md › Authentication and sessions | assurance levels named; enrolment, replacement and revocation of authenticators not taught |
| One-time recovery codes | partial | part14_security.topics.md › Authentication and sessions | single-use recovery tokens named; MFA backup or recovery codes not taught |
| TOTP (time-based one-time passwords) | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| HMAC message authentication | covered | part14_security.topics.md › Cryptography |  |
| WebAuthn and passkeys | covered | part14_security.topics.md › Authentication and sessions |  |
| Phishing-resistant authentication | covered | part14_security.topics.md › Authentication and sessions |  |

## 11.1.4 Opaque Sessions, Cookies, CSRF, and CORS

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| CORS (exact origin allowlist) | covered | part14_security.topics.md › Web application security |  |
| Opaque server-side sessions | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Session fixation and rotation | covered | part14_security.topics.md › Authentication and sessions |  |
| Session expiry (idle and absolute) | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Session revocation and logout | partial | part14_security.topics.md › Authentication and sessions | Revocation named for refresh tokens; per-session logout not taught |
| Cookie attributes (Secure, HttpOnly, SameSite) | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Cache-Control no-store for sensitive responses | missing | → suggest part14 |  |
| Browser token storage risks | partial | part14_security.topics.md › Authentication and sessions | cookie attributes and theft vectors covered; token storage in browser script-accessible storage not named |
| CSRF synchronizer token | covered | part14_security.topics.md › Authentication and sessions |  |
| Double-submit CSRF tokens | covered | part14_security.topics.md › Authentication and sessions |  |
| Origin and Referer validation | covered | part14_security.topics.md › Authentication and sessions |  |
| Fetch Metadata policy | partial | part06_programming_languages_go.topics.md › Go — engineering | CrossOriginProtection used; Fetch Metadata not named |

## 11.1.5 API Keys, Signed Requests, and JWT Validation

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| API key lifecycle (hashed storage, rotation) | partial | part07_programming_languages_typescript_wire_theory_exercises.topics.md › TypeScript, Node and the web client | Server-side key handling only; hashed storage and rotation not |
| Signed requests (HMAC canonical request) | covered | part14_security.topics.md › Cryptography |  |
| Replay protection (nonce and timestamp) | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| JWT claim validation | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| JWT algorithm pinning and key confusion | covered | part14_security.topics.md › Authentication and sessions |  |
| JWKS and trusted issuer key selection | partial | part14_security.topics.md › Authentication and sessions | Attacker-controlled kid and jku named; JWKS trust selection not |
| Token class separation (audience and type) | partial | part14_security.topics.md › Authentication and sessions | Audience named in confused-deputy list; token type separation not |

## 11.1.6 OAuth 2.0, OpenID Connect, and Federation

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Token revocation and stale authorization | partial | part14_security.topics.md › Authentication and sessions | Refresh-token family revocation named; stale-authorization tests not |
| OAuth 2.0 versus OpenID Connect | covered | part14_security.topics.md › Authentication and sessions |  |
| OAuth authorization code flow | covered | part14_security.topics.md › Authentication and sessions |  |
| PKCE | covered | part14_security.topics.md › Authentication and sessions |  |
| OAuth state and OIDC nonce | covered | part14_security.topics.md › Authentication and sessions |  |
| Exact redirect URI matching | covered | part14_security.topics.md › Authentication and sessions |  |
| Issuer verification and mix-up attacks | covered | part14_security.topics.md › Authentication and sessions |  |
| Backend-for-frontend pattern | covered | part11_software_architecture.topics.md › Architecture fundamentals |  |
| Refresh token rotation | covered | part14_security.topics.md › Authentication and sessions |  |
| Deprecated OAuth grants (implicit, password) | partial | part14_security.topics.md › Authentication and sessions | Implicit grant excluded; password grant deprecation not named |
| Sender-constrained tokens (mTLS, DPoP) | covered | part14_security.topics.md › Authentication and sessions |  |
| Pushed authorization requests | covered | part14_security.topics.md › Authentication and sessions |  |
| Resource indicators and rich authorization requests | covered | part14_security.topics.md › Authentication and sessions |  |
| OIDC discovery and authorization server metadata | covered | part14_security.topics.md › Authentication and sessions |  |
| ID token validation | covered | part14_security.topics.md › Authentication and sessions |  |
| Open-redirect prevention | covered | part14_security.topics.md › Web application security |  |
| Federated identity namespacing (issuer plus subject) | partial | part14_security.topics.md › Authentication and sessions | Issuer string compare named; issuer-plus-subject keys not |

## 11.1.7 Authorization and Multi-Tenant Policy

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Access-control matrix | covered | part14_security.topics.md › Access-control models |  |
| Role-based access control (RBAC) | covered | part14_security.topics.md › Access-control models |  |
| Object-level authorization (IDOR, BOLA) | covered | part14_security.topics.md › Authorization flaws |  |
| Field-level authorization and mass assignment | covered | part14_security.topics.md › Authorization flaws |  |
| Multi-tenant isolation | covered | part12_databases.topics.md › Data modelling and design |  |
| Attribute-based access control (ABAC) | covered | part14_security.topics.md › Access-control models |  |
| Relationship-based access control (ReBAC) | covered | part14_security.topics.md › Access-control models |  |
| Policy decision and enforcement points | covered | part14_security.topics.md › Access-control models |  |
| Confused deputy problem | covered | part14_security.topics.md › Authorization flaws |  |
| Administrator and service identity separation | partial | part14_security.topics.md › Authorization flaws | Per-service least privilege named; admin and service identity split not |

## 11.1.8 Application, Data, Secrets, and Supply-Chain Security

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Input and data boundary validation | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Secret inventory, rotation and revocation | covered | part14_security.topics.md › Cryptography |  |
| TLS defaults and trusted proxy headers | covered | part14_security.topics.md › Web application security |  |
| Security event logging fields | partial | part14_security.topics.md › Detection and incident response | Log coverage named; field-level event schema not |
| Dependency and supply-chain review | partial | part06_programming_languages_go.topics.md › Go — engineering | Vulnerability scanning named; provenance and pinning review not |
| Reproducible builds and release provenance | covered | part06_programming_languages_go.topics.md › Go — engineering |  |

## 12.1 Required Primer Topics

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Performance versus scalability | covered | part13_distributed_systems.topics.md › Performance at scale |  |
| Latency versus throughput | covered | part13_distributed_systems.topics.md › Performance at scale |  |
| Availability versus consistency (CAP) | covered | part13_distributed_systems.topics.md › Foundations |  |
| Consistency patterns (weak, eventual, strong) | covered | part13_distributed_systems.topics.md › Foundations |  |
| Availability patterns (failover, replication) | partial | part13_distributed_systems.topics.md › Consensus and coordination | Replication taught; failover named only as a DNS routing policy |
| DNS in system design | covered | part09_networking.topics.md › DNS |  |
| CDN | covered | part09_networking.topics.md › Middleboxes, proxies and load balancing |  |
| Load balancing | covered | part09_networking.topics.md › Middleboxes, proxies and load balancing |  |
| Reverse proxies | covered | part09_networking.topics.md › Middleboxes, proxies and load balancing |  |
| Application layer and microservices | covered | part11_software_architecture.topics.md › Architecture fundamentals |  |
| Database design and scaling (sharding, replication) | covered | part13_distributed_systems.topics.md › Partitioning |  |
| NoSQL stores | covered | part12_databases.topics.md › NoSQL and choosing a store |  |
| Caches (cache-aside, eviction) | covered | part13_distributed_systems.topics.md › Caching at scale |  |
| Asynchronism and message queues | covered | part11_software_architecture.topics.md › Architecture fundamentals |  |
| Communication (sync and async, REST, RPC) | covered | part11_software_architecture.topics.md › Architecture fundamentals |  |
| Security as a system-design primer | covered | part14_security.topics.md › Threat modelling |  |
| Back-of-the-envelope estimation (powers of two, latency numbers) | covered | part02_computer_organization.topics.md › Data representation |  |

## 12.2 Official System-Design Problems

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| URL shortener design (Pastebin, Bitly, TinyURL) | partial | part13_distributed_systems.topics.md › Exercises | Named in an exercise; short-link design covered as Base62 only |
| Social feed and timeline design | covered | part13_distributed_systems.topics.md › Design techniques | Fan-out and celebrity problem taught; no full design lab |
| Web crawler design | covered | part13_distributed_systems.topics.md › Design techniques |  |
| Search engine design | covered | part13_distributed_systems.topics.md › Design techniques |  |
| Key-value store and cache design (Redis-like, Memcached-like) | partial | part13_distributed_systems.topics.md › Replication | Dynamo-style replication taught; key-value store design lab not |
| Mint.com personal finance design | partial | part13_distributed_systems.topics.md › Exercises | named in a design list only |
| Scaling to millions of users on AWS | covered | part13_distributed_systems.topics.md › System design method |  |
| Amazon sales ranking design | partial | part13_distributed_systems.topics.md › Exercises | named in a design list only |
| Social-network data structures | partial | part08_data_structures_algorithms.topics.md › Graph algorithms | Adjacency lists taught; social-graph design not |

## 12.3 Official OOD Problems

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Card game design (deck of cards) | partial | part11_software_architecture.topics.md › Exercises | Named in an OOD exercise list only |
| Parking lot design | partial | part11_software_architecture.topics.md › Exercises | named in an OOD design list only |
| LRU cache design | covered | part06_programming_languages_go.topics.md › Go — engineering |  |
| Hash map design (OOD) | partial | part11_software_architecture.topics.md › Exercises | Named in an OOD exercise list; hash tables taught in part06 |
| Call center design | partial | part11_software_architecture.topics.md › Exercises | Named in an OOD exercise list only |
| Chat system design | partial | part13_distributed_systems.topics.md › Exercises | named in a design list only |
| Circular array and ring buffer design | covered | part06_programming_languages_go.topics.md › Go — engineering |  |

## 12.4 Additional Primer Questions

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| File sync design | partial | part13_distributed_systems.topics.md › Exercises | Named in an exercise; chunking and delta sync taught as concepts only |
| Collaborative editing design (Google Docs) | partial | part13_distributed_systems.topics.md › Replication | CRDTs and OT taught; collaborative editing lab not |
| Recommendation system design | partial | part19_machine_learning.topics.md › Applied problem families | Recommender concepts and case-study headings exist; no recommendation system design lab |
| Top-k and trending topics | covered | part13_distributed_systems.topics.md › Stream and batch processing |  |
| Snowflake-style ID generation | partial | part12_databases.topics.md › Data modelling and design | Named in the keys list only |
| Garbage collector design | partial | part06_programming_languages_go.topics.md › Go — memory, types with behaviour and generics | Collector internals named; design problem not |
| Stock exchange and order matching design | partial | part13_distributed_systems.topics.md › Exercises | named in a design list only |
| Multi-datacenter serving | partial | part23_cloud_providers_1of2.topics.md › Google Cloud — storage and databases | Spanner named as a cloud product; multi-region serving design not taught |
| API rate limiter design | covered | part14_security.topics.md › API abuse |  |
| Photo sharing feed design (Instagram) | partial | part13_distributed_systems.topics.md › Exercises | named in a design list only |

## 12.5 HLD/LLD/Pattern Ladder

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Capacity estimation | partial | part13_distributed_systems.topics.md › System design method | Named in the six-step write-up; estimation procedure in part02 and part03 |
| Architecture decision records (ADR) | covered | part11_software_architecture.topics.md › Architecture documentation |  |
| Transactional outbox | covered | part13_distributed_systems.topics.md › Distributed transactions |  |
| Repository pattern | covered | part11_software_architecture.topics.md › Architecture fundamentals |  |
| Unit of work | covered | part11_software_architecture.topics.md › Application architecture |  |
| Adapter pattern | covered | part11_software_architecture.topics.md › Gang of Four patterns |  |
| Strategy pattern | covered | part11_software_architecture.topics.md › Gang of Four patterns |  |
| Factory and builder patterns | partial | part11_software_architecture.topics.md › Gang of Four patterns | Factory taught; builder named only as functional options |
| Middleware and decorator patterns | covered | part06_programming_languages_go.topics.md › Go — memory, types with behaviour and generics |  |
| Chain of responsibility | covered | part11_software_architecture.topics.md › Gang of Four patterns |  |
| Observer and pub/sub | covered | part11_software_architecture.topics.md › Gang of Four patterns |  |
| Mediator pattern | covered | part11_software_architecture.topics.md › Gang of Four patterns |  |
| Command pattern | covered | part11_software_architecture.topics.md › Gang of Four patterns |  |
| State pattern | covered | part11_software_architecture.topics.md › Gang of Four patterns |  |
| Saga pattern | covered | part13_distributed_systems.topics.md › Distributed transactions |  |
| CQRS and read models | covered | part11_software_architecture.topics.md › Distributed application patterns |  |
| Idempotent consumer | covered | part13_distributed_systems.topics.md › Distributed transactions |  |
| Circuit breaker | covered | part11_software_architecture.topics.md › Distributed application patterns |  |
| Bulkhead pattern | covered | part11_software_architecture.topics.md › Distributed application patterns |  |
| Retry with jitter | covered | part06_programming_languages_go.topics.md › Go — concurrency |  |
| Strangler fig migration | covered | part11_software_architecture.topics.md › Distributed application patterns |  |
| Mermaid HLD and LLD diagrams | covered | part11_software_architecture.topics.md › Architecture documentation |  |
| Trust boundaries and abuse-case register | covered | part14_security.topics.md › Threat modelling |  |
| Secret-redaction checks in observability | partial | part14_security.topics.md › Web application security | Redaction named; redaction tests in observability not |
| Rollback, revocation and recovery stories | covered | part18_devops_sre.topics.md › Kubernetes |  |

## 13. Production ML and ML-System Case-Study Bank

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Ranking, search, recommendations, ads and feeds (case studies) | partial | part25_ml_case_studies_1of5.topics.md › Recommend / personalize / feed | Case studies named; retrieval, rerank and NDCG labs only partly in part19 |
| Forecasting, ETA, scheduling and pricing (case studies) | partial | part27_ml_case_studies_3of5.topics.md › Forecast / ETA / demand | Case studies named; forecast and assignment simulator not |
| Fraud, risk, anomaly, spam and trust (case studies) | partial | part27_ml_case_studies_3of5.topics.md › Fraud / trust & safety | Case studies named; threshold review queue not |
| LLM, NLP and generative assistant systems (case studies) | partial | part28_ml_case_studies_4of5.topics.md › LLM / genAI apps | Case studies named; RAG evaluator labs in part21-22 |
| CV, audio and document systems (case studies) | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Computer vision: images, motion and multi-view geometry | Case studies named; embedding and multimodal retrieval eval not |
| Feature platforms and MLOps (case studies) | partial | part25_ml_case_studies_1of5.topics.md › Recommend / personalize / feed | Case studies named; feature-store facade and drift monitor partly in part19 |
| Graph ML and entity resolution (case studies) | partial | part25_ml_case_studies_1of5.topics.md › Recommend / personalize / feed | Case studies named; blocking and candidate generation not |
| Bandits, RL and explore-exploit (case studies) | partial | part26_ml_case_studies_2of5.topics.md › Search / rank / ads | Case studies named; offline replay evaluator not |
| Causal inference and experimentation (case studies) | partial | part25_ml_case_studies_1of5.topics.md › Recommend / personalize / feed | Case studies named; CUPED and exposure logs not taught |

## 14.1 Service and Infrastructure Inventory

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Nasiko service and infrastructure inventory | out of scope | - | Nasiko-project-specific service names and endpoints |

## 14.2 Phase Map

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Nasiko phase map (P0 to P10 build-out) | out of scope | - | Nasiko-project-specific build plan |

## Missing in this range

- Approximation algorithms (→ suggest part08) — from: 9. Textbook and Chapter Atlas
- Line search and trust regions (→ suggest part03) — from: 9. Textbook and Chapter Atlas
- Host header validation (→ suggest part14) — from: 11.1.2 Hardened Go HTTP and Middleware Mechanics
- Cache-Control no-store for sensitive responses (→ suggest part14) — from: 11.1.4 Opaque Sessions, Cookies, CSRF, and CORS

## Partial in this range

- Git and GitHub over SSH — Git covered in part15; SSH key setup for remotes is not named there (SSH keys sit in part10) — part15_software_delivery.topics.md
- VS Code editor for Go — Editor setup is taught for Python only; no Go editor setup — part05_programming_languages_python_and_shell.topics.md
- REST and gRPC gateway — Served side by side in an exercise; no gRPC gateway or transcoding — part19_machine_learning.topics.md
- Semi and anti joins — Named in a join list only; no semi or anti join lab — part12_databases.topics.md
- Outer joins — Outer joins named in a list; no outer-join semantics or NULL-extension lab — part12_databases.topics.md
- Hidden tuple columns (ctid, xmin, xmax) — Catalogs and system columns named; ctid, xmin and xmax not taught — part12_databases.topics.md
- Lateral joins — Named in a join list only; no lateral join lab — part12_databases.topics.md
- Bitmap and index-only scans — Bitmap scans taught; index-only scans not named — part12_databases.topics.md
- Query pipeline (parse, rewrite, plan) — Rewrite rules named in relational theory; parse-rewrite-plan pipeline not taught — part12_databases.topics.md
- Join-order search and GEQO — Dynamic-programming join-order search named; GEQO not — part08_data_structures_algorithms.topics.md
- Multivariable differentiation (Jacobian, inverse function theorem) — Change-of-variable Jacobian named; inverse and implicit function theorems not — part03_mathematics.topics.md
- Joint and conditional distributions — Conditional probability taught; joint distributions not named as a topic — part03_mathematics.topics.md
- Sampling distributions — Named through the t and F distributions; no general sampling-distribution treatment — part03_mathematics.topics.md
- Randomized algorithms — Randomized quicksort only; randomized algorithms as a topic not taught — part08_data_structures_algorithms.topics.md
- Numerical methods (root finding, quadrature) — Root finding and interpolation named; quadrature not — part03_mathematics.topics.md
- Channel coding — Linear and LDPC codes named; channel coding theorem not taught — part03_mathematics.topics.md
- Noise models — Quantization noise only; Gaussian and AWGN noise models not named — part03c_signals_systems_and_communications.topics.md
- Discrete cosine transform — Spectrograms and MFCC named; DCT not — part03_mathematics.topics.md
- Mixture models and EM — Gaussian mixtures named under clustering; EM not taught — part19_machine_learning.topics.md
- Generalized linear models — Logistic regression only; GLM family not named — part19_machine_learning.topics.md
- MCMC sampling — Approximate inference named; MCMC mentioned only in passing — part19_machine_learning.topics.md
- Variational inference — Probabilistic programming named; variational inference not — part19_machine_learning.topics.md
- Regularization and dropout — L1 and L2 named; dropout not — part03_mathematics.topics.md
- Graph neural networks — Graph learning and PageRank named; message-passing GNNs not — part19_machine_learning.topics.md
- First-order and propositional logic — Propositional logic covered; first-order logic not named — part19_machine_learning.topics.md
- Part-of-speech tagging —  — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md
- Local features (SIFT, Harris) —  — part19_machine_learning.topics.md
- Structure from motion and SLAM —  — part19_machine_learning.topics.md
- Multi-view reconstruction —  — part19_machine_learning.topics.md
- Human-in-the-loop and the human side of ML — Governance and retraining policy named; human-in-the-loop labeling not — part19_machine_learning.topics.md
- Adversarial bandits (EXP3) — Adversarial bandits named; EXP3 algorithm not — part19_machine_learning.topics.md
- Bandit lower bounds — Bandit regret named; lower bounds not — part19_machine_learning.topics.md
- Ridge and lasso shrinkage — L1 and L2 named; ridge and lasso as shrinkage estimators not — part03_mathematics.topics.md
- Splines and generalized additive models — Splines named; GAMs not — part19_machine_learning.topics.md
- Robustness in speech recognition — Robustness named; speech-recognition noise robustness not taught — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md
- Monte Carlo and temporal-difference learning — Monte Carlo named; temporal-difference learning not — part03_mathematics.topics.md
- Policy gradient methods — Reinforcement learning named; policy gradients not — part19_machine_learning.topics.md
- Krylov subspace methods — Conjugate gradient named; Krylov subspaces not — part03_mathematics.topics.md
- Quasi-Newton methods (BFGS) — Newton's method named; quasi-Newton updates not — part03_mathematics.topics.md
- Lagrangian duality — Lagrange multipliers and KKT named; duality not — part03_mathematics.topics.md
- Numerical and data libraries (NumPy, Pandas, SciPy) — NumPy named; Pandas and SciPy not — part05_programming_languages_python_and_shell.topics.md
- Visualization libraries (Matplotlib, Seaborn, Plotly) — Matplotlib and Plotly named; Seaborn not — part05_programming_languages_python_and_shell.topics.md
- Classical ML libraries (scikit-learn, XGBoost, LightGBM) — XGBoost named; LightGBM not — part19_machine_learning.topics.md
- MLOps tooling (MLflow, Weights & Biases, Evidently) — Evidently not named — part19_machine_learning.topics.md
- Serving and agent frameworks (FastAPI, LangChain, LlamaIndex, vLLM, Ray) — FastAPI named; LangChain, LlamaIndex, vLLM and Ray not — part05_programming_languages_python_and_shell.topics.md
- Vector stores (pgvector, Qdrant) — Vector similarity with pgvector named; Qdrant not — part12_databases.topics.md
- Phoenix LLM tracing — Named in passing with other trace UIs — part18_devops_sre.topics.md
- STRIDE threat modelling — STRIDE named once; per-element walk-through not taught — part14_security.topics.md
- Secure defaults and separation of duties — Fail-safe defaults named; separation of duties not taught — part14_security.topics.md
- Security usability and accessibility — one clause in the security economics bullet; not taught as a practice — part14_security.topics.md
- Request IDs and trusted-proxy handling — Trusted-proxy headers named; request IDs not — part14_security.topics.md
- Access logging and secret redaction — Log coverage named; access logging and redaction not taught — part14_security.topics.md
- Outbound HTTP client hardening — Client timeouts named; redirect and destination allow-listing not — part06_programming_languages_go.topics.md
- HTTP method semantics (safe and idempotent) — Idempotent PUT in an exercise; safe-method rules not taught — part11_software_architecture.topics.md
- Identities, credentials and sessions model — Credentials and sessions covered; no explicit subject and identifier model — part14_security.topics.md
- Login throttling and lockout — Rate limits named; account lockout not — part14_security.topics.md
- Recent authentication and step-up — Step-up named only through recovery; no recent-authentication gate — part14_security.topics.md
- Authenticator lifecycle and revocation — assurance levels named; enrolment, replacement and revocation of authenticators not taught — part14_security.topics.md
- One-time recovery codes — single-use recovery tokens named; MFA backup or recovery codes not taught — part14_security.topics.md
- Session revocation and logout — Revocation named for refresh tokens; per-session logout not taught — part14_security.topics.md
- Browser token storage risks — cookie attributes and theft vectors covered; token storage in browser script-accessible storage not named — part14_security.topics.md
- Fetch Metadata policy — CrossOriginProtection used; Fetch Metadata not named — part06_programming_languages_go.topics.md
- API key lifecycle (hashed storage, rotation) — Server-side key handling only; hashed storage and rotation not — part07_programming_languages_typescript_wire_theory_exercises.topics.md
- JWKS and trusted issuer key selection — Attacker-controlled kid and jku named; JWKS trust selection not — part14_security.topics.md
- Token class separation (audience and type) — Audience named in confused-deputy list; token type separation not — part14_security.topics.md
- Token revocation and stale authorization — Refresh-token family revocation named; stale-authorization tests not — part14_security.topics.md
- Deprecated OAuth grants (implicit, password) — Implicit grant excluded; password grant deprecation not named — part14_security.topics.md
- Federated identity namespacing (issuer plus subject) — Issuer string compare named; issuer-plus-subject keys not — part14_security.topics.md
- Administrator and service identity separation — Per-service least privilege named; admin and service identity split not — part14_security.topics.md
- Security event logging fields — Log coverage named; field-level event schema not — part14_security.topics.md
- Dependency and supply-chain review — Vulnerability scanning named; provenance and pinning review not — part06_programming_languages_go.topics.md
- Availability patterns (failover, replication) — Replication taught; failover named only as a DNS routing policy — part13_distributed_systems.topics.md
- URL shortener design (Pastebin, Bitly, TinyURL) — Named in an exercise; short-link design covered as Base62 only — part13_distributed_systems.topics.md
- Key-value store and cache design (Redis-like, Memcached-like) — Dynamo-style replication taught; key-value store design lab not — part13_distributed_systems.topics.md
- Mint.com personal finance design — named in a design list only — part13_distributed_systems.topics.md
- Amazon sales ranking design — named in a design list only — part13_distributed_systems.topics.md
- Social-network data structures — Adjacency lists taught; social-graph design not — part08_data_structures_algorithms.topics.md
- Card game design (deck of cards) — Named in an OOD exercise list only — part11_software_architecture.topics.md
- Parking lot design — named in an OOD design list only — part11_software_architecture.topics.md
- Hash map design (OOD) — Named in an OOD exercise list; hash tables taught in part06 — part11_software_architecture.topics.md
- Call center design — Named in an OOD exercise list only — part11_software_architecture.topics.md
- Chat system design — named in a design list only — part13_distributed_systems.topics.md
- File sync design — Named in an exercise; chunking and delta sync taught as concepts only — part13_distributed_systems.topics.md
- Collaborative editing design (Google Docs) — CRDTs and OT taught; collaborative editing lab not — part13_distributed_systems.topics.md
- Recommendation system design — Recommender concepts and case-study headings exist; no recommendation system design lab — part19_machine_learning.topics.md
- Snowflake-style ID generation — Named in the keys list only — part12_databases.topics.md
- Garbage collector design — Collector internals named; design problem not — part06_programming_languages_go.topics.md
- Stock exchange and order matching design — named in a design list only — part13_distributed_systems.topics.md
- Multi-datacenter serving — Spanner named as a cloud product; multi-region serving design not taught — part23_cloud_providers_1of2.topics.md
- Photo sharing feed design (Instagram) — named in a design list only — part13_distributed_systems.topics.md
- Capacity estimation — Named in the six-step write-up; estimation procedure in part02 and part03 — part13_distributed_systems.topics.md
- Factory and builder patterns — Factory taught; builder named only as functional options — part11_software_architecture.topics.md
- Secret-redaction checks in observability — Redaction named; redaction tests in observability not — part14_security.topics.md
- Ranking, search, recommendations, ads and feeds (case studies) — Case studies named; retrieval, rerank and NDCG labs only partly in part19 — part25_ml_case_studies_1of5.topics.md
- Forecasting, ETA, scheduling and pricing (case studies) — Case studies named; forecast and assignment simulator not — part27_ml_case_studies_3of5.topics.md
- Fraud, risk, anomaly, spam and trust (case studies) — Case studies named; threshold review queue not — part27_ml_case_studies_3of5.topics.md
- LLM, NLP and generative assistant systems (case studies) — Case studies named; RAG evaluator labs in part21-22 — part28_ml_case_studies_4of5.topics.md
- CV, audio and document systems (case studies) — Case studies named; embedding and multimodal retrieval eval not — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md
- Feature platforms and MLOps (case studies) — Case studies named; feature-store facade and drift monitor partly in part19 — part25_ml_case_studies_1of5.topics.md
- Graph ML and entity resolution (case studies) — Case studies named; blocking and candidate generation not — part25_ml_case_studies_1of5.topics.md
- Bandits, RL and explore-exploit (case studies) — Case studies named; offline replay evaluator not — part26_ml_case_studies_2of5.topics.md
- Causal inference and experimentation (case studies) — Case studies named; CUPED and exposure logs not taught — part25_ml_case_studies_1of5.topics.md
