# Topic diff: Atlases, Go auth and security, design and case-study banks, modern transformer sources

Source: gcp/unified-curriculum.md lines 517-759 and 1620-1653. Compared against: gcp-lite/index/*.topics.md and gcp-lite/Rust_Track_AI_Infrastructure.md.

Counts: 314 rows: covered 207, partial 50, missing 51, out of scope 6.

## 9. Textbook and Chapter Atlas

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Real numbers and the real construction | missing | → suggest part03 | Ordered fields, completeness and the real construction are absent |
| Limits, continuity and the derivative | covered | part03_mathematics.topics.md › Calculus and optimization | - |
| Integrals and the fundamental theorem of calculus | partial | part03_mathematics.topics.md › Calculus and optimization | Integral as accumulated area only; the fundamental theorem is not named |
| Sequences and infinite series with convergence tests | partial | part01_school_foundations.topics.md › Algebra | Arithmetic and geometric sums only; convergence tests absent |
| Complex numbers | missing | → suggest part03 | Only Go's complex type appears |
| Uniform convergence and power series | missing | → suggest part03 | - |
| Riemann–Stieltjes and Lebesgue integration | missing | → suggest part03 | Source says measure theory only if needed |
| Differential forms and integral theorems (Stokes, Green) | partial | part03_mathematics.topics.md › Calculus and optimization | Gradients and Jacobians covered; divergence, curl and integral theorems absent |
| Vector spaces, span, basis and dimension | covered | part03_mathematics.topics.md › Linear algebra | - |
| Linear systems by elimination and LU factorization | covered | part03_mathematics.topics.md › Linear algebra | - |
| Orthogonality, projections and least squares | covered | part03_mathematics.topics.md › Linear algebra | Least squares via normal equations |
| Determinants and invertibility | covered | part03_mathematics.topics.md › Linear algebra | - |
| Eigenvalues, eigenvectors and power iteration | covered | part03_mathematics.topics.md › Linear algebra | - |
| Singular value decomposition and low-rank approximation | covered | part03_mathematics.topics.md › Linear algebra | - |
| Linear maps, rank and nullity | covered | part03_mathematics.topics.md › Linear algebra | - |
| Hilbert spaces and linear operators | missing | → suggest part03 | - |
| Product and sum rules of probability | covered | part03_mathematics.topics.md › Probability | Sum rule via marginalization; product rule via conditional probability |
| Plausible reasoning (Cox desiderata) | missing | → suggest part03 | Probability as extended logic not taught |
| Sampling and Monte Carlo estimation | covered | part03_mathematics.topics.md › Probability | - |
| Hypothesis testing | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| Parameter estimation and maximum likelihood | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| Sufficient statistics | missing | → suggest part03 | - |
| Maximum-entropy principle | missing | → suggest part03 | Entropy covered; maximum-entropy distributions absent |
| Priors and Bayesian updating | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| Decision theory | covered | part17_architects_practice.topics.md › Decision theory | - |
| Bootstrap and jackknife | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| Nonparametric inference (kernel density, empirical CDF) | missing | → suggest part03 | - |
| Exploratory data analysis | partial | part03_mathematics.topics.md › Statistics and experimental design | Histograms and quantiles only; the EDA method is not taught |
| Classification and ML as statistical inference | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Transformations of random variables | missing | → suggest part03 | Change of variables for densities absent |
| Joint and conditional distributions | covered | part03_mathematics.topics.md › Probability | - |
| Common distribution families (Bernoulli through normal) | covered | part03_mathematics.topics.md › Probability | - |
| Exponential families | missing | → suggest part03 | - |
| Confidence intervals | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| Analysis of variance (ANOVA) | missing | → suggest part03 | Regression diagnostics covered in part19; ANOVA and F-tests absent |
| Asymptotics and efficiency of estimators | partial | part03_mathematics.topics.md › Probability | LLN and CLT covered; consistency and asymptotic efficiency not named |
| Asymptotic notation and recurrences | covered | part08_data_structures_algorithms.topics.md › Analysis | - |
| Divide and conquer | covered | part08_data_structures_algorithms.topics.md › Analysis | - |
| Sorting algorithms | covered | part08_data_structures_algorithms.topics.md › Sorting, searching and strings | - |
| Randomized algorithms and quickselect | covered | part08_data_structures_algorithms.topics.md › Sorting, searching and strings | - |
| Heaps, hash tables and trees | covered | part08_data_structures_algorithms.topics.md › Trees and heaps | - |
| Dynamic programming | covered | part08_data_structures_algorithms.topics.md › Greedy algorithms and dynamic programming | - |
| Greedy algorithms | covered | part08_data_structures_algorithms.topics.md › Greedy algorithms and dynamic programming | - |
| Amortized analysis | covered | part08_data_structures_algorithms.topics.md › Analysis | - |
| Graph algorithms (Dijkstra, Kruskal, Prim) | covered | part08_data_structures_algorithms.topics.md › Graph algorithms | - |
| Maximum flow and minimum cut | covered | part08_data_structures_algorithms.topics.md › Graph algorithms | - |
| Number theory (gcd, congruences, CRT, Fermat and Euler) | covered | part03_mathematics.topics.md › Proof and discrete mathematics | - |
| Primitive roots and continued fractions | missing | → suggest part03 | - |
| Approximation algorithms | partial | part08_data_structures_algorithms.topics.md › Computability and complexity | Approximations named as engineering responses; approximation ratios not taught |
| Constrained optimization and KKT conditions | covered | part03_mathematics.topics.md › Calculus and optimization | - |
| Newton's method | missing | → suggest part03 | - |
| Steepest descent (gradient descent) | covered | part03_mathematics.topics.md › Calculus and optimization | Taught as gradient descent with convergence rates |
| Conjugate gradient | missing | → suggest part03 | - |
| Ordinary differential equations | partial | part03_mathematics.topics.md › Calculus and optimization | First-order equations with Euler and RK4 only; higher-order and systems absent |
| Partial differential equations | missing | → suggest part03 | - |
| Fourier series and transform (DFT, FFT) | covered | part03_mathematics.topics.md › Signals and sequences | - |
| Laplace transform | missing | → suggest part03 | - |
| z-transform | missing | → suggest part03 | - |
| Gradients, Jacobians and the Hessian | covered | part03_mathematics.topics.md › Calculus and optimization | - |
| Numerical methods (interpolation, numerical integration) | covered | part03_mathematics.topics.md › Numerical computing | - |
| QR factorization and the QR algorithm | missing | → suggest part03 | Least squares covered via normal equations; QR absent |
| Krylov subspace and iterative methods | partial | part03_mathematics.topics.md › Numerical computing | Iterative solvers named in passing only |
| Sparse and structured matrix problems | missing | → suggest part03 | - |
| Conditioning and floating-point stability | covered | part03_mathematics.topics.md › Numerical computing | - |
| Markov chains and stationary distributions | covered | part03_mathematics.topics.md › Probability | - |
| Law of large numbers and central limit theorem | covered | part03_mathematics.topics.md › Probability | - |
| Multi-armed bandits (epsilon-greedy, UCB, Thompson sampling) | covered | part03_mathematics.topics.md › Decision mathematics | - |
| Finite MDPs and value functions | covered | part03_mathematics.topics.md › Decision mathematics | - |
| Dynamic programming for MDPs (value and policy iteration) | covered | part19_machine_learning.topics.md › Specialised learning areas | - |
| Temporal-difference learning and Q-learning | covered | part19_machine_learning.topics.md › Specialised learning areas | Monte Carlo control not named |
| Policy gradients and PPO | covered | part19_machine_learning.topics.md › Specialised learning areas | - |
| n-step returns and eligibility traces | missing | → suggest part19 | - |
| Function approximation in reinforcement learning | missing | → suggest part19 | - |
| Planning with learned models (Dyna) | missing | → suggest part19 | - |
| Regret bounds and bandit lower bounds | partial | part19_machine_learning.topics.md › Applied problem families | Regret defined; minimax lower bounds absent |
| Adversarial bandits | missing | → suggest part19 | - |
| Contextual and linear bandits | partial | part03_mathematics.topics.md › Decision mathematics | Named only |
| Pure exploration | missing | → suggest part19 | - |
| Entropy, relative entropy and mutual information | covered | part03_mathematics.topics.md › Information theory | - |
| Asymptotic equipartition property | missing | → suggest part03 | Typical sets absent |
| Source coding bound and Huffman codes | covered | part03_mathematics.topics.md › Information theory | - |
| Channel capacity | covered | part03_mathematics.topics.md › Information theory | - |
| Rate distortion theory | missing | → suggest part03 | - |
| Differential entropy | missing | → suggest part03 | - |
| Information inequalities (Jensen, data processing) | partial | part04_problem_solving.topics.md › Contest mathematics toolkit | Jensen named as a contest inequality; information inequalities absent |
| Bayesian networks and exact inference | covered | part19_machine_learning.topics.md › Classical AI: search, knowledge and reasoning | - |
| Mixtures and the EM algorithm | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Model assessment and cross-validation | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Clustering (k-means, DBSCAN) | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Decision trees, boosting and random forests | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Support vector machines and kernels | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Ridge and lasso regularization | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Splines and basis expansions | missing | → suggest part19 | Polynomial features appear only in the scikit-learn list |
| Survival analysis | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Multiple testing and false discovery rate | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| Neural networks and backpropagation | covered | part19_machine_learning.topics.md › Deep learning | - |
| Vanishing gradients and residual connections | covered | part19_machine_learning.topics.md › Deep learning | - |
| Recurrent networks and LSTMs | covered | part19_machine_learning.topics.md › Deep learning | - |
| Convolutional networks | covered | part19_machine_learning.topics.md › Deep learning | - |
| Attention and transformers | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Generative models (VAE, GAN, diffusion) | covered | part20_generative_ai_1of3.topics.md › Generative models beyond autoregression | - |
| Graph neural networks and graph learning | covered | part19_machine_learning.topics.md › Specialised learning areas | - |
| Syntactic parsing (CKY, PCFGs) | covered | part19_machine_learning.topics.md › Natural language processing foundations | - |
| Part-of-speech tagging with HMMs | covered | part19_machine_learning.topics.md › Natural language processing foundations | - |
| Speech recognition and text-to-speech | partial | part19_machine_learning.topics.md › Specialised learning areas | Audio frames, MFCCs and word error rate covered; acoustic models, decoding and TTS absent |
| Speech features (MFCC and spectrograms) | covered | part03_mathematics.topics.md › Signals and sequences | - |
| Text classification and summarization | covered | part19_machine_learning.topics.md › Natural language processing foundations | - |
| Topic models and latent semantic indexing | covered | part19_machine_learning.topics.md › Natural language processing foundations | - |
| Information retrieval: inverted indexes and BM25 | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Index compression | missing | → suggest part19 | - |
| Relevance feedback and probabilistic IR | partial | part19_machine_learning.topics.md › Applied problem families | BM25 covered; relevance feedback absent |
| Ranking evaluation (precision, recall, MAP, nDCG) | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Web search and PageRank | covered | part19_machine_learning.topics.md › Specialised learning areas | - |
| Discourse analysis | missing | → suggest part19 | - |
| Language modelling and n-gram models | covered | part03_mathematics.topics.md › Signals and sequences | - |
| Tokenization (BPE, WordPiece) | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Image formation and filtering | covered | part19_machine_learning.topics.md › Classical computer vision and geometry | - |
| Local features (Harris, SIFT) | covered | part19_machine_learning.topics.md › Classical computer vision and geometry | - |
| Image segmentation | covered | part19_machine_learning.topics.md › Classical computer vision and geometry | - |
| Object detection | covered | part19_machine_learning.topics.md › Classical computer vision and geometry | - |
| Projective geometry and camera models | covered | part19_machine_learning.topics.md › Classical computer vision and geometry | - |
| Stereo and epipolar geometry | covered | part19_machine_learning.topics.md › Classical computer vision and geometry | - |
| Structure from motion, SLAM and 3D reconstruction | partial | part19_machine_learning.topics.md › Classical computer vision and geometry | Range sensing and depth covered; structure from motion and SLAM absent |
| Signals, harmonics and noise | partial | part03_mathematics.topics.md › Signals and sequences | Sampling and Fourier covered; noise and harmonic content not taught |
| Autocorrelation | missing | → suggest part03 | - |
| Discrete cosine transform | partial | part19_machine_learning.topics.md › Classical computer vision and geometry | Named in image transforms only |
| Convolution and filtering | covered | part03_mathematics.topics.md › Signals and sequences | - |
| LTI systems and impulse response | missing | → suggest part03 | - |
| Sampling and aliasing | covered | part03_mathematics.topics.md › Signals and sequences | - |
| Amplitude modulation | missing | → suggest part03 | - |
| Short-time Fourier transform | covered | part03_mathematics.topics.md › Signals and sequences | - |
| Cepstral analysis | missing | → suggest part03 | - |
| Multirate processing (decimation, interpolation) | missing | → suggest part03 | - |
| Digital filter design (FIR and IIR) | missing | → suggest part03 | - |
| Fixed-point arithmetic and quantization error | missing | → suggest part02 | - |
| Finite automata and regular expressions | covered | part08_data_structures_algorithms.topics.md › Computability and complexity | - |
| Context-free grammars | covered | part07_programming_languages_typescript_wire_theory_exercises.topics.md › Language theory | - |
| Pushdown automata and Turing machines | partial | part08_data_structures_algorithms.topics.md › Computability and complexity | Halting problem covered; pushdown automata absent; Turing machines named only in passing |
| Decidability and intractability (P, NP, NP-completeness) | covered | part08_data_structures_algorithms.topics.md › Computability and complexity | - |
| Abstract algebra, topology and pure analysis texts | out of scope | - | Owner tagged ARCHIVE |
| Algorithm and systems theory texts (CPU, OS, networking and compiler theory) | out of scope | - | Owner tagged ARCHIVE |
| Complexity theory beyond the gate and cryptographic theory texts | out of scope | - | Owner tagged ARCHIVE |
| Digital communications (modulation, receivers, MIMO, fading) | out of scope | - | Owner tagged ARCHIVE |
| Robotics | out of scope | - | Archive unless needed |
| Game, rendering, mechanical and medical archive maps | out of scope | - | Owner tagged ARCHIVE; clinical and mechanical subject matter |
| Arithmetic, algebra and sets (school level) | covered | part01_school_foundations.topics.md › Arithmetic and number sense | - |
| Trigonometry and geometry (school level) | covered | part01_school_foundations.topics.md › Geometry, trigonometry and vectors | - |
| Introductory statistics and quantitative literacy | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| Multivariable calculus | covered | part03_mathematics.topics.md › Calculus and optimization | - |

## 10. Python Library and ML Tool Atlas

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Numerical and data tools (NumPy, pandas, SciPy) | partial | part05_programming_languages_python_and_shell.topics.md › Python | NumPy and pandas covered; SciPy absent |
| Plotting tools (Matplotlib, Seaborn, Plotly) | partial | part05_programming_languages_python_and_shell.topics.md › Python | Matplotlib covered; Seaborn and Plotly absent |
| Classical ML libraries (scikit-learn, XGBoost, LightGBM) | partial | part19_machine_learning.topics.md › Machine learning in Python | scikit-learn covered; XGBoost and LightGBM absent |
| Deep learning frameworks (PyTorch, TensorFlow, Keras) | partial | part19_machine_learning.topics.md › Machine learning in Python | PyTorch covered; TensorFlow and Keras absent |
| NLP and transformer libraries (NLTK, spaCy, Hugging Face Tokenizers and Transformers) | partial | part19_machine_learning.topics.md › Machine learning in Python | NLTK covered; Hugging Face Transformers in part20_generative_ai_1of3.topics.md › Fine-tuning and adaptation; spaCy and Hugging Face Tokenizers absent |
| Data engineering at scale (PySpark, Dask) | missing | → suggest part19 | Spark named only as a system in part13; no tool taught |
| MLOps tools (MLflow, Weights and Biases, Evidently) | partial | part19_machine_learning.topics.md › MLOps | Experiment tracking, registries and drift covered as concepts; the named tools absent |
| Serving and agent frameworks (FastAPI, LangChain, LlamaIndex, vLLM, Ray) | partial | part22_generative_ai_3of3.topics.md › Agents and workflows | FastAPI, LangChain and vLLM covered; LlamaIndex and Ray absent |

## 11. Go Tool, Platform, and System Atlas

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Go service frameworks and RPC (Chi, Gin, Fiber, protobuf, gRPC, JSON-RPC) | partial | part06_programming_languages_go.topics.md › Go — engineering | Chi, Gin, Echo, Fiber, protobuf and gRPC covered; JSON-RPC absent |
| Data-store clients (Postgres, MongoDB, Redis, pgvector, Qdrant) | covered | part06_programming_languages_go.topics.md › Go — engineering | pgvector in part12_databases.topics.md › Analytics and other engines; Qdrant in part20_generative_ai_1of3.topics.md › Embeddings and retrieval |
| Container and infrastructure tools (Docker, Compose, BuildKit, Kubernetes, Helm, Terraform, Kong, Nginx) | partial | part18_devops_sre.topics.md › Docker | Docker, Kubernetes, Helm, Terraform, Kong and NGINX covered; Compose and BuildKit absent |
| Observability tools (OpenTelemetry, pprof, Phoenix, dashboards, alerts) | covered | part06_programming_languages_go.topics.md › Go — engineering | pprof and OpenTelemetry in part06; Phoenix and dashboards in part18_devops_sre.topics.md › Observability |
| CLI frameworks (Cobra, Viper) | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library | - |
| Go numerical and ML support (Gonum, Gorgonia, GoMLX, ONNX Runtime, model services) | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library | - |

## 11.1.1 Threat Modeling and Security Foundations

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Threat modeling with STRIDE and data-flow diagrams | covered | part14_security.topics.md › Threat modelling | - |
| Assets, trust boundaries and attacker models | covered | part14_security.topics.md › Threat modelling | - |
| Least privilege, deny by default and defense in depth | covered | part14_security.topics.md › Principles and economics | - |
| Fail-safe defaults and separation of duties | covered | part14_security.topics.md › Principles and economics | Saltzer and Schroeder principles |
| Risk scoring: likelihood, impact and residual risk | partial | part14_security.topics.md › Principles and economics | Residual risk named; likelihood and impact scoring and threat register absent |
| Misuse and abuse cases as tests | covered | part14_security.topics.md › Threat modelling | Abuse cases converted into deny tests |
| Security usability and accessibility | partial | part14_security.topics.md › Principles and economics | Attacker cost versus user friction covered; accessibility absent |

## 11.1.2 Hardened Go HTTP and Middleware Mechanics

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Middleware as func(http.Handler) http.Handler and chain order | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Request-scoped context values and cancellation | covered | part06_programming_languages_go.topics.md › Go — concurrency | Deadline propagation through net/http |
| Response-writer wrappers that preserve capabilities | missing | → suggest part06 | Flusher, Hijacker and ResponseController absent |
| Panic recovery middleware | covered | part06_programming_languages_go.topics.md › Go — composite data, functions, errors and text | panic and recover |
| Security response headers (CSP, nosniff, HSTS) | partial | part14_security.topics.md › Cryptography | HSTS named in the TLS list only; CSP and nosniff absent |
| Header and body size limits | covered | part06_programming_languages_go.topics.md › Go — engineering | MaxBytesReader |
| Server timeouts and a hardened server instance | covered | part06_programming_languages_go.topics.md › Go — engineering | ReadHeaderTimeout and related fields |
| Strict JSON decoding with unknown fields | covered | part06_programming_languages_go.topics.md › Go — the everyday standard library | DisallowUnknownFields named |
| HTTP error status semantics and problem details | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Graceful shutdown | covered | part06_programming_languages_go.topics.md › Go — engineering | Server.Shutdown |
| Outbound client timeouts and response-body closure | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| SSRF defenses and DNS rebinding | covered | part14_security.topics.md › Cloud-specific attacks | - |
| Token-bucket rate limiting | covered | part06_programming_languages_go.topics.md › Go — concurrency | - |
| Load shedding and concurrency budgets | covered | part13_distributed_systems.topics.md › Asynchronism and flow control | - |
| CORS and cross-origin protection | covered | part14_security.topics.md › Web application security | CrossOriginProtection in part06 › Go — engineering |
| Fuzzing, race detection and benchmarks | covered | part06_programming_languages_go.topics.md › Go — engineering | Native fuzzing with a seed corpus |

## 11.1.3 Identity, Passwords, Recovery, and MFA

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Identity, credentials and authenticators as separate concepts | partial | part14_security.topics.md › Authentication and sessions | Authentication versus authorization named; identity model absent |
| Password length, composition and breached-password policy | partial | part14_security.topics.md › Authentication and sessions | Breach blocklists covered; NIST length and no-composition rules absent |
| Argon2id password hashing with versioned records | covered | part06_programming_languages_go.topics.md › Go — engineering | Rehash on login |
| Generic failures and timing-equalized login | covered | part06_programming_languages_go.topics.md › Go — engineering | Timing-equalised login for unknown users |
| Account-aware throttling without victim lockout | partial | part14_security.topics.md › Authentication and sessions | Rate limits named; account-aware throttling absent |
| Recovery and reset tokens | covered | part14_security.topics.md › Authentication and sessions | Hashed single-use tokens |
| TOTP and HOTP verifiers with replay protection | covered | part06_programming_languages_go.topics.md › Go — engineering | RFC test vectors |
| WebAuthn and passkey relying-party validation | partial | part14_security.topics.md › Authentication and sessions | WebAuthn and passkeys named; relying-party checks absent |
| Step-up and recent-authentication checks | covered | part14_security.topics.md › Authentication and sessions | - |

## 11.1.4 Opaque Sessions, Cookies, CSRF, and CORS

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Opaque server-side sessions with idle and absolute expiry | covered | part06_programming_languages_go.topics.md › Go — engineering | Hashed opaque session IDs |
| Session fixation and ID rotation | covered | part14_security.topics.md › Authentication and sessions | - |
| Cookie attributes and the __Host- prefix | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| CSRF synchronizer and double-submit tokens | covered | part06_programming_languages_go.topics.md › Go — engineering | Session-bound CSRF tokens |
| Fetch Metadata and Origin validation | partial | part14_security.topics.md › Authentication and sessions | Origin checks named; Fetch Metadata absent |
| CORS allowlists and preflight | covered | part14_security.topics.md › Web application security | CORS pitfalls |

## 11.1.5 API Keys, Signed Requests, and JWT Validation

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| API key issuance, hashed storage and rotation | partial | part22_generative_ai_3of3.topics.md › Security and safety of LLM applications | Scoped keys and rotation named; hash-at-rest storage and lookup prefix absent |
| Canonical request signing with HMAC | missing | → suggest part14 | HMAC primitive covered in part14 › Cryptography; the request signing scheme is absent |
| JWT validation: algorithm allow-list, alg none, key confusion, trusted keys, claims | covered | part14_security.topics.md › Authentication and sessions | HS256 allow-list in part06 › Go — engineering |

## 11.1.6 OAuth 2.0, OpenID Connect, and Federation

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| OAuth roles versus OpenID Connect identity | covered | part14_security.topics.md › Authentication and sessions | - |
| Authorization code flow with PKCE, state and nonce | covered | part06_programming_languages_go.topics.md › Go — engineering | - |
| Authorization-server conformance: exact redirects, one-time codes, consent | partial | part14_security.topics.md › Authentication and sessions | Exact redirect allow-lists and no implicit grant covered; one-time codes and consent binding absent |
| Refresh-token rotation with family revocation | missing | → suggest part14 | - |
| Sender-constrained tokens (DPoP, mTLS-bound tokens) | missing | → suggest part14 | - |
| Pushed authorization requests, resource indicators and rich authorization details | missing | → suggest part14 | - |
| OpenID Connect relying party: discovery, issuer and ID-token checks | partial | part14_security.topics.md › Authentication and sessions | ID tokens and nonces covered; discovery and issuer namespacing absent |
| Identity federation and SSO | covered | part14_security.topics.md › Authentication and sessions | - |

## 11.1.7 Authorization and Multi-Tenant Policy

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Access-control matrix | covered | part14_security.topics.md › Access-control models | - |
| Role-based access control (RBAC) | covered | part14_security.topics.md › Access-control models | - |
| Attribute-based access control (ABAC) | partial | part14_security.topics.md › Access-control models | Named only |
| Relationship-based access control and Zanzibar-style tuples | covered | part14_security.topics.md › Access-control models | - |
| Object ownership checks against IDOR and BOLA | covered | part14_security.topics.md › Authorization flaws | - |
| Mass assignment and allow-listed write fields | covered | part14_security.topics.md › Authorization flaws | - |
| Field-level read and write policy | partial | part14_security.topics.md › Authorization flaws | Allow-listed DTO fields for writes only; read-side field policy absent |
| Tenant isolation across queries, caches, jobs and logs | partial | part12_databases.topics.md › Data modelling and design | Multi-tenancy in SQL covered; caches, jobs, exports and logs absent |
| Policy decision and enforcement separation (PDP, PEP, OPA, Cedar) | missing | → suggest part14 | - |
| Confused deputy and audience-restricted tokens | covered | part14_security.topics.md › Authorization flaws | - |
| Authorization test matrix (allowed and denied cases) | partial | part14_security.topics.md › Threat modelling | Abuse cases become deny tests; no subject-action-resource matrix |

## 11.1.8 Application, Data, Secrets, and Supply-Chain Security

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Input validation at trust boundaries | partial | part14_security.topics.md › Web application security | Allow-lists named; general validation pipeline and canonicalization absent |
| Injection defenses: parameterized queries and path containment | covered | part14_security.topics.md › Web application security | os.Root in part06 › Go — the everyday standard library |
| Archive limits and file-upload validation | covered | part14_security.topics.md › Web application security | Zip bombs in part14 › Denial of service |
| Output encoding and XSS | covered | part14_security.topics.md › Web application security | - |
| Secrets inventory, rotation and KMS or HSM storage | covered | part14_security.topics.md › Cryptography | - |
| TLS verification and mutual TLS | covered | part14_security.topics.md › Cryptography | crypto/tls in part06 › Go — engineering |
| Security event logging schema and redaction | partial | part14_security.topics.md › Web application security | Log injection covered; event schema and secret redaction absent |
| Tamper-evident audit trail | missing | → suggest part14 | - |
| SBOM | covered | part14_security.topics.md › Supply chain | - |
| Build provenance and SLSA levels | covered | part14_security.topics.md › Supply chain | - |
| Vulnerability scanning with govulncheck | covered | part06_programming_languages_go.topics.md › Go — engineering | Reachability versus module scanners |
| Artifact signing and attestation verification | covered | part14_security.topics.md › Supply chain | - |
| Reproducible builds and pinned dependencies | covered | part06_programming_languages_go.topics.md › Go — engineering | Reproducible, byte-identical builds |

## 12.1 Required Primer Topics

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Performance versus scalability; latency versus throughput | covered | part13_distributed_systems.topics.md › Performance at scale | - |
| Availability versus consistency (CAP trade-off) | partial | part13_distributed_systems.topics.md › Foundations | Consistency models covered; CAP trade-off not named |
| Consistency patterns | covered | part13_distributed_systems.topics.md › Foundations | - |
| Availability patterns (fail-over, replication) | covered | part13_distributed_systems.topics.md › Availability | - |
| DNS | covered | part09_networking.topics.md › DNS | - |
| CDN | covered | part09_networking.topics.md › Middleboxes, proxies and load balancing | Push and pull CDNs |
| Load balancing and reverse proxies | covered | part09_networking.topics.md › Middleboxes, proxies and load balancing | - |
| Application layer and microservices | covered | part11_software_architecture.topics.md › Architecture fundamentals | - |
| Database design and scaling (partitioning, replication) | covered | part13_distributed_systems.topics.md › Partitioning | - |
| NoSQL | covered | part12_databases.topics.md › NoSQL and choosing a store | - |
| Caches | covered | part13_distributed_systems.topics.md › Caching at scale | - |
| Asynchronism (queues and workers) | covered | part13_distributed_systems.topics.md › Asynchronism and flow control | - |
| Communication (REST, RPC, gRPC) | covered | part11_software_architecture.topics.md › API design | gRPC in part06 › Go — engineering |
| Security as a design concern | covered | part14_security.topics.md › Principles and economics | - |
| Powers of two and latency numbers | covered | part02_computer_organization.topics.md › Data representation; Machine organization | - |

## 12.2 Official System-Design Problems

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Pastebin and URL shortener design | covered | part13_distributed_systems.topics.md › Exercises | - |
| Twitter timeline and search design | covered | part13_distributed_systems.topics.md › Exercises | - |
| Web crawler design | covered | part13_distributed_systems.topics.md › Exercises | - |
| Personal-finance aggregator (Mint.com) design | covered | part13_distributed_systems.topics.md › Exercises | - |
| Social-network data structures and shortest paths | covered | part13_distributed_systems.topics.md › Exercises | - |
| Search-engine key-value cache | covered | part13_distributed_systems.topics.md › Exercises | - |
| Sales ranking by category (Amazon) | covered | part13_distributed_systems.topics.md › Exercises | - |
| Scaling a service from one machine to millions of users | covered | part13_distributed_systems.topics.md › Exercises | AWS not named |

## 12.3 Official OOD Problems

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Hash map design | covered | part11_software_architecture.topics.md › Exercises | - |
| LRU cache design | covered | part11_software_architecture.topics.md › Exercises | - |
| Call center design | covered | part11_software_architecture.topics.md › Exercises | Escalation |
| Deck of cards design | covered | part11_software_architecture.topics.md › Exercises | Blackjack |
| Parking lot design | covered | part11_software_architecture.topics.md › Exercises | - |
| Chat server design | covered | part11_software_architecture.topics.md › Exercises | Online chat with group chats |
| Circular array design | covered | part08_data_structures_algorithms.topics.md › Linear structures and techniques | Ring buffers covered |

## 12.4 Additional Primer Questions

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| File sync design | covered | part13_distributed_systems.topics.md › Exercises | - |
| Search engine design | covered | part13_distributed_systems.topics.md › Exercises | - |
| Google Docs and collaborative editing | covered | part13_distributed_systems.topics.md › Exercises | OT and CRDTs |
| Redis-like store design | covered | part13_distributed_systems.topics.md › Exercises | - |
| Memcached-like cache design | covered | part13_distributed_systems.topics.md › Exercises | - |
| Amazon recommendations design | covered | part13_distributed_systems.topics.md › Exercises | - |
| WhatsApp or chat design | covered | part13_distributed_systems.topics.md › Exercises | Chat app with presence |
| Instagram or photo-sharing design | covered | part13_distributed_systems.topics.md › Exercises | - |
| Facebook feed, timeline and graph search | covered | part13_distributed_systems.topics.md › Exercises | - |
| Trending topics | covered | part13_distributed_systems.topics.md › Exercises | - |
| Snowflake-style ID generation | covered | part13_distributed_systems.topics.md › Exercises | Snowflake-style generator also built in the lab list |
| Top-k requests in a time window | covered | part13_distributed_systems.topics.md › Exercises | - |
| Multi-datacenter serving | covered | part13_distributed_systems.topics.md › Exercises | - |
| Multiplayer card game design | covered | part13_distributed_systems.topics.md › Exercises | - |
| Garbage collector service design | covered | part13_distributed_systems.topics.md › Exercises | - |
| API rate limiter design | covered | part13_distributed_systems.topics.md › Exercises | Distributed rate limiter also built in the lab list |
| Stock exchange design | covered | part13_distributed_systems.topics.md › Exercises | Matching-engine design listed among the exercises |

## 12.5 HLD/LLD/Pattern Ladder

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Repository and unit of work | covered | part11_software_architecture.topics.md › Application architecture | - |
| Adapter, strategy, factory and builder | covered | part11_software_architecture.topics.md › Gang of Four patterns | - |
| Middleware, decorator and chain of responsibility | covered | part11_software_architecture.topics.md › Gang of Four patterns | - |
| Observer, pub-sub, mediator, command and state | covered | part11_software_architecture.topics.md › Gang of Four patterns | - |
| Outbox, saga and CQRS read model | covered | part13_distributed_systems.topics.md › Distributed transactions | CQRS in part11 › Distributed application patterns |
| Idempotent consumer | covered | part13_distributed_systems.topics.md › Distributed transactions | - |
| Circuit breaker and bulkhead | covered | part11_software_architecture.topics.md › Distributed application patterns | - |
| Retry with jitter | covered | part11_software_architecture.topics.md › Distributed application patterns | Exponential backoff with jitter also in part06 › Go — concurrency |
| Strangler fig migration | covered | part11_software_architecture.topics.md › Distributed application patterns | - |

## 13. Production ML and ML-System Case-Study Bank

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Ranking, search, recommendations, ads and feeds | covered | part25_ml_case_studies_1of5.topics.md › Recommend / personalize / feed | Search in part26_ml_case_studies_2of5.topics.md › Search / rank / ads |
| Forecasting, ETA, scheduling and pricing | covered | part27_ml_case_studies_3of5.topics.md › Forecast / ETA / demand | Pricing in part29_ml_case_studies_5of5.topics.md › Other |
| Fraud, risk, anomaly, spam and trust | covered | part27_ml_case_studies_3of5.topics.md › Fraud / trust & safety | - |
| LLM, NLP and generative assistant systems | covered | part28_ml_case_studies_4of5.topics.md › LLM / genAI apps | NLP in part28 › NLP / text / support |
| CV, audio and document systems | covered | part28_ml_case_studies_4of5.topics.md › CV / video / OCR | Speech in part28 › Speech / audio |
| Feature platforms and MLOps | covered | part28_ml_case_studies_4of5.topics.md › ML platform / infra | - |
| Graph ML and entity resolution | covered | part29_ml_case_studies_5of5.topics.md › Other | Graph ML theory in part19_machine_learning.topics.md › Specialised learning areas |
| Bandits, RL and explore-exploit case studies | partial | part19_machine_learning.topics.md › Specialised learning areas | Bandit theory covered in part03; case-study cluster and offline replay evaluator absent |
| Causal inference and experimentation | covered | part03_mathematics.topics.md › Statistics and experimental design | Experiments in part19 › Applied problem families |

## 17.1.16 Verified Primary Sources: Modern Transformer, Serving, and Post-Training Layer

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| RMS normalization and GLU variants | missing | → suggest part20 | - |
| Rotary position embedding (RoPE) | partial | Rust_Track_AI_Infrastructure.md › P9. An LLM inference engine | Built as one P9 step; no GCP-lite topic teaches it |
| Multi-query and grouped-query attention | missing | → suggest part20 | - |
| IO-aware attention kernels (FlashAttention) | missing | → suggest part20 | - |
| Sparse mixture-of-experts | partial | part20_generative_ai_1of3.topics.md › How LLMs work | Mixture-of-experts layers named in passing; sparse routing absent |
| Paged KV-cache memory management | covered | part22_generative_ai_3of3.topics.md › Application architecture and LLMOps | vLLM PagedAttention; also Rust_Track_AI_Infrastructure.md › P10. An inference server with continuous batching |
| Speculative decoding | missing | → suggest part22 | - |
| Distributed training partitioning (tensor, pipeline, optimizer sharding) | missing | → suggest part20 | Data parallelism named in part02 only |
| Post-training quantization (LLM.int8, GPTQ, AWQ) | partial | part20_generative_ai_1of3.topics.md › Fine-tuning and adaptation | Weight quantization and QLoRA covered; GPTQ and AWQ absent |
| Scaling laws and compute-optimal training | covered | part20_generative_ai_1of3.topics.md › How LLMs work | Chinchilla named |
| Policy optimization for reasoning (PPO, GRPO, GSPO) | partial | part19_machine_learning.topics.md › Specialised learning areas | PPO covered; GRPO and GSPO absent |
| Continuous batching | covered | Rust_Track_AI_Infrastructure.md › P10. An inference server with continuous batching | - |
| Roofline performance model | partial | Rust_Track_AI_Infrastructure.md › How a stage is taught | Named only as a P20 checkpoint; not taught in the track body |

## Missing in this range

- Real numbers and the real construction
- Complex numbers
- Uniform convergence and power series
- Riemann–Stieltjes and Lebesgue integration
- Hilbert spaces and linear operators
- Plausible reasoning (Cox desiderata)
- Sufficient statistics
- Maximum-entropy principle
- Nonparametric inference (kernel density, empirical CDF)
- Transformations of random variables
- Exponential families
- Analysis of variance (ANOVA)
- Primitive roots and continued fractions
- Newton's method
- Conjugate gradient
- Partial differential equations
- Laplace transform
- z-transform
- QR factorization and the QR algorithm
- Sparse and structured matrix problems
- n-step returns and eligibility traces
- Function approximation in reinforcement learning
- Planning with learned models (Dyna)
- Adversarial bandits
- Pure exploration
- Asymptotic equipartition property
- Rate distortion theory
- Differential entropy
- Splines and basis expansions
- Index compression
- Discourse analysis
- Autocorrelation
- LTI systems and impulse response
- Amplitude modulation
- Cepstral analysis
- Multirate processing (decimation, interpolation)
- Digital filter design (FIR and IIR)
- Fixed-point arithmetic and quantization error
- Data engineering at scale (PySpark, Dask)
- Response-writer wrappers that preserve capabilities
- Canonical request signing with HMAC
- Refresh-token rotation with family revocation
- Sender-constrained tokens (DPoP, mTLS-bound tokens)
- Pushed authorization requests, resource indicators and rich authorization details
- Policy decision and enforcement separation (PDP, PEP, OPA, Cedar)
- Tamper-evident audit trail
- RMS normalization and GLU variants
- Multi-query and grouped-query attention
- IO-aware attention kernels (FlashAttention)
- Speculative decoding
- Distributed training partitioning (tensor, pipeline, optimizer sharding)

## Partial in this range

- Integrals and the fundamental theorem of calculus
- Sequences and infinite series with convergence tests
- Differential forms and integral theorems (Stokes, Green)
- Exploratory data analysis
- Asymptotics and efficiency of estimators
- Approximation algorithms
- Ordinary differential equations
- Krylov subspace and iterative methods
- Regret bounds and bandit lower bounds
- Contextual and linear bandits
- Information inequalities (Jensen, data processing)
- Speech recognition and text-to-speech
- Relevance feedback and probabilistic IR
- Structure from motion, SLAM and 3D reconstruction
- Signals, harmonics and noise
- Discrete cosine transform
- Pushdown automata and Turing machines
- Numerical and data tools (NumPy, pandas, SciPy)
- Plotting tools (Matplotlib, Seaborn, Plotly)
- Classical ML libraries (scikit-learn, XGBoost, LightGBM)
- Deep learning frameworks (PyTorch, TensorFlow, Keras)
- NLP and transformer libraries (NLTK, spaCy, Hugging Face Tokenizers and Transformers)
- MLOps tools (MLflow, Weights and Biases, Evidently)
- Serving and agent frameworks (FastAPI, LangChain, LlamaIndex, vLLM, Ray)
- Go service frameworks and RPC (Chi, Gin, Fiber, protobuf, gRPC, JSON-RPC)
- Container and infrastructure tools (Docker, Compose, BuildKit, Kubernetes, Helm, Terraform, Kong, Nginx)
- Risk scoring: likelihood, impact and residual risk
- Security usability and accessibility
- Security response headers (CSP, nosniff, HSTS)
- Identity, credentials and authenticators as separate concepts
- Password length, composition and breached-password policy
- Account-aware throttling without victim lockout
- WebAuthn and passkey relying-party validation
- Fetch Metadata and Origin validation
- API key issuance, hashed storage and rotation
- Authorization-server conformance: exact redirects, one-time codes, consent
- OpenID Connect relying party: discovery, issuer and ID-token checks
- Attribute-based access control (ABAC)
- Field-level read and write policy
- Tenant isolation across queries, caches, jobs and logs
- Authorization test matrix (allowed and denied cases)
- Input validation at trust boundaries
- Security event logging schema and redaction
- Availability versus consistency (CAP trade-off)
- Bandits, RL and explore-exploit case studies
- Rotary position embedding (RoPE)
- Sparse mixture-of-experts
- Post-training quantization (LLM.int8, GPTQ, AWQ)
- Policy optimization for reasoning (PPO, GRPO, GSPO)
- Roofline performance model
