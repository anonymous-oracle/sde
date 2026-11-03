# Unified Curriculum: index and resume point

Compact map of `unified_curriculum.md` (the single unified document, about 440 KB, in the learner's `sde` folder next to `nptel.txt` and `iit-genai.md`; it holds the curriculum, an NPTEL-style assignment with a collapsed key inside every content unit, and the appendices). Built 2026-11-03 under Master_Rules.md Part III.1 from 43 NPTEL and learner-supplied outlines plus the 12-chapter GenAI course. 564 source cells (486 NPTEL, 78 GenAI), all cited by at least one unit; 155 units in 18 domains. Stochastic Approximation and Approximation Algorithms were added on 2026-11-03. 148 assignments, A1.1 to A17.7 (MCQ, multiple-select, numerical, derivation, programming; 10 marks each), embedded in their units.

**Resume point:** U1.1, first block; nothing taught yet. **Open decisions:** see Appendix F of the full file (official-assignment downloads, gap candidates, truncated sources, inferred titles).

**Standing instructions recorded (nptel.txt and chat, 2026-11-03):** (1) learn every technique from scratch in Python, with NumPy as the default toolbox. This is a guideline, not a prohibition: the learner said NumPy-only is "more of a suggestion" and to "design as needed", so units that depart from the NumPy default name their tooling. (2) NPTEL-style assignments for every unit; create them where NPTEL provides none.


## Part A. Mathematical foundations

**D1. Discrete Mathematics and Mathematical Reasoning**
U1.1 Logic, proof paradigms and formal languages; U1.2 Counting, generating functions and combinatorics; U1.3 Posets, lattices, Boolean algebra and switching circuits; U1.4 Graph theory; U1.5 Number theory and cryptography; U1.6 Algebra: finite fields, codes, groups and orbit counting; U1.7 An invitation to mathematics: polynomials, functions, matrices, conservation laws

**D2. Single-Variable Calculus and Real Analysis**
U2.1 Numbers, countability, functions, limits and continuity; U2.2 Differentiation and mean value theorems; U2.3 Integration, applications and transcendental functions; U2.4 Taylor expansion, sequences, series and power series; U2.5 Improper integrals, Gamma and Beta functions, integrals dependent on parameters

**D3. Multivariable and Vector Calculus**
U3.1 Functions of several variables, partial derivatives and differentiability; U3.2 Taylor expansion in several variables, maxima, minima and Lagrange multipliers; U3.3 Multiple integrals and their applications; U3.4 Vector calculus: fields, line and surface integrals, Green, Gauss and Stokes; U3.5 Matrix calculus, Jacobians and Hessians for machine learning

**D4. Linear Algebra: Core, Abstract, Numerical and Applied**
U4.1 Systems of linear equations, matrices, elimination, rank and inverses; U4.2 Vectors, vector spaces, subspaces, bases and dimension; U4.3 Linear maps, representation by matrices, duality and quotient spaces; U4.4 Inner products, norms, orthogonality, projections and Gram–Schmidt; U4.5 Determinants, multilinear forms and permutations; U4.6 Eigenvalues, eigenvectors, similarity and diagonalization; U4.7 Canonical forms: minimal polynomial, invariant subspaces, Jordan and rational forms; U4.8 Spectral theory: normal operators, symmetric matrices, quadratic forms, PSD matrices and kernels; U4.9 LU, QR, conditioning, SVD, pseudo-inverse and low-rank approximation; U4.10 Least squares, regularized and constrained least squares; U4.11 Applications of linear algebra: PageRank, sparsity, dynamical systems, Markov chains, signal processing and data analytics

**D5. Probability and Stochastic Models**
U5.1 Probability foundations: from events to Bayes' theorem; U5.2 Random variables, distributions and moments; U5.3 Special discrete distributions and the Poisson process; U5.4 Special continuous distributions and the normal distribution; U5.5 Functions of random variables, transformations and order statistics; U5.6 Joint distributions, conditioning, covariance and multivariate normal; U5.7 Limit theorems and concentration inequalities; U5.8 Markov chains, queueing theory and reliability; U5.9 Conditional expectation and martingales

**D6. Statistics and Statistical Inference**
U6.1 Data, descriptive statistics and measures of association; U6.2 Sampling distributions and point estimation; U6.3 Confidence intervals and hypothesis testing; U6.4 Correlation, regression and multivariate analysis; U6.5 Bayesian inference and MCMC; U6.6 Forecasting with statistical and machine-learning models: hydrology and water-resources applications

**D7. Differential Equations, Dynamical Systems, Numerical Methods, Complex Analysis and Transforms**
U7.1 First- and higher-order ordinary differential equations; U7.2 Numerical analysis: iteration, root finding, interpolation and quadrature; U7.3 Complex variables: analytic functions and complex integration; U7.4 Series, singularities, residues, real integrals and conformal mapping; U7.5 Laplace, Z, Fourier and discrete Fourier transforms; U7.6 Mathematical modelling: discrete and continuous dynamical systems; U7.7 ODE theory for dynamical systems: Gronwall, limit sets, invariant sets and chain transitivity

**D8. Optimization: Theory, Algorithms and Applications**
U8.1 Optimization problems: formulation, history, transformations and basic facts; U8.2 Convex sets, cones, polyhedra and separation; U8.3 Convex functions and their calculus; U8.4 Unconstrained optimization theory; U8.5 Constrained optimization theory: Lagrange, cones, Fritz John and KKT; U8.6 Lagrangian duality, saddle points and minimax; U8.7 Linear programming: simplex, duality, sensitivity and interior-point methods; U8.8 Unconstrained descent methods: line search, gradient, Newton, quasi-Newton, conjugate gradient, trust region; U8.9 Constrained optimization algorithms: QP, projected and reduced gradient, penalty, augmented Lagrangian, SQP; U8.10 First-order methods for ML: stochastic, accelerated, proximal, adaptive, and the dynamical-systems view; U8.11 Conic and structured convex programs: QCQP, SOCP, SDP, geometric programs; U8.12 Applications of optimization: signal estimation, compressive sensing, radar, big data and finance; U8.13 Non-smooth and difference-of-convex optimization; U8.14 Distributed optimization: graphs, consensus, ADMM and dual decomposition; U8.15 Dynamic optimization and complementarity problems; U8.16 Stochastic approximation: algorithms, step sizes and the ODE method; U8.17 Convergence rates, stability, two-timescale algorithms and stochastic recursive inclusions


## Part B. Machine learning

**D9. Machine Learning Foundations: Supervised, Unsupervised, Probabilistic, Data Mining and Learning Theory**
U9.0 History of AI, symbolic AI and the machine-learning workflow; U9.1 What machine learning is: paradigms, data, hypothesis spaces and the statistical framework; U9.2 Model evaluation and selection: bias–variance, validation, tuning and metrics; U9.3 Linear regression and linear classification: estimation, logistic and softmax regression, surrogate losses; U9.4 Regularization and implicit regularization; U9.5 Perceptron, support vector machines and kernel methods; U9.6 Bayes decision theory, density estimation and probabilistic classifiers; U9.7 Decision trees and ensembles: bagging, boosting, random forests; U9.8 Dimensionality reduction and feature learning; U9.9 Clustering, mixture models and the EM algorithm; U9.10 Probabilistic graphical models, hidden Markov models, inference and Gaussian processes; U9.11 Instance-based learning, collaborative filtering and recommendation; U9.12 Data mining: preprocessing, association rules, sequence mining, outliers and case studies; U9.13 Learning theory: PAC, VC dimension, generalization and modern overparametrization; U9.14 Symbolic and knowledge-based machine learning, tools and cognitive-science influences

**D10. Sequential Decision Making: Bandits and Reinforcement Learning**
U10.1 From batch to online learning: adversarial full-information and bandit settings; U10.2 Stochastic bandits: regret notions, UCB, KL-UCB and lower bounds; U10.3 Contextual bandits and pure exploration; U10.4 Markov decision processes, dynamic programming and temporal-difference learning; U10.5 Policy gradient, actor–critic and proximal policy optimization; U10.6 Stochastic approximation in reinforcement learning


## Part C. Deep learning and generative AI

**D11. Deep Learning Foundations**
U11.1 Perceptron, multilayer networks, activations and loss functions; U11.2 Backpropagation and training deep networks; U11.3 Overfitting, regularization and generalization in deep networks; U11.4 Convolutional neural networks and image representation; U11.5 Explainable AI for deep models; U11.6 Segmentation and object detection; U11.7 Recurrent networks: RNN, LSTM, GRU, backpropagation through time and attention in RNNs; U11.8 Autoencoders and representation learning

**D12. Natural Language Processing, the Transformer and Large Language Models**
U12.1 NLP foundations and the classical NLP pipeline; U12.2 Word representations and multilingual embeddings; U12.3 Attention and the Transformer architecture; U12.4 Pretraining, self-supervised learning and the LLM landscape; U12.5 Scaling laws, LLM architectures and long context; U12.6 Decoding strategies and sampling; U12.7 Prompting: fundamentals, APIs and advanced techniques; U12.8 Instruction tuning, RLHF and alignment: PPO and DPO; U12.9 Parameter-efficient fine-tuning: LoRA and QLoRA; U12.10 Prompt optimization, compression and prompt security

**D13. Deep Generative Models**
U13.1 Probabilistic deep generative modelling: foundations and taxonomy; U13.2 Generative modelling via variational divergence minimization; U13.3 Generative adversarial networks: formulation, training, WGAN and applications; U13.4 Variational autoencoders, improvements and VQ-VAE; U13.5 Autoregressive models; U13.6 Energy-based and score-based models; Langevin sampling; U13.7 Denoising diffusion probabilistic models, conditional diffusion and Stable Diffusion; U13.8 Normalizing flows (gap-fill from the references)


## Part D. LLM applications, evaluation, safety

**D14. Retrieval-Augmented Generation and Agentic Systems**
U14.1 Why RAG, RAG architecture and classical retrievers; U14.2 RAG failure modes, types of RAG and assessment; U14.3 Sparse retrieval limits and dense representations; U14.4 Learning retrieval-oriented embeddings and choosing an embedding model; U14.5 Document processing and chunking; U14.6 Vector databases and indexes: KNN, IVF, PQ, HNSW, FAISS and ChromaDB; U14.7 The retrieval pipeline: bi-encoder, cross-encoder, ColBERT and two-stage retrieval; U14.8 Production RAG: request shaping, query transformation, routing, security, cost and observability; U14.9 Limits of single-shot RAG and the move to agents; U14.10 Agent basics, tool calling and orchestration; U14.11 Planning with ReAct; U14.12 State machines and LangGraph; U14.13 Agentic memory; U14.14 Provenance and citations; U14.15 Multi-agent architecture summary, error handling and best practices

**D15. Evaluation, Safety and Responsible AI**
U15.1 LLM evaluation: metric architecture and reference-based metrics; U15.2 LLM-as-a-judge and factuality; U15.3 AI safety foundations and threat models; U15.4 White-box attacks and prompt injection; U15.5 Black-box attacks and the jailbreak taxonomy; U15.6 Defense, interpretability and ethics


## Part E. Algorithms, systems and integration

**D16. ML Systems, Efficiency and Distributed and Federated Learning**
U16.1 CNN computation and accelerators; U16.2 Parallelism for training, communication and fault tolerance; U16.3 LLM decoding, memory management and serving infrastructure; U16.4 Model compression and quantization; U16.5 Graph neural network inference systems; U16.6 Federated learning

**D17. Approximation Algorithms and Computational Complexity**
U17.1 Review of NP-completeness and the approximation framework; U17.2 Approximation for vertex cover, set cover and the traveling salesman problem; U17.3 Approximation for the knapsack problem and job scheduling; U17.4 Linear programming basics and deterministic rounding; U17.5 Randomized rounding; U17.6 The primal–dual method; U17.7 Semidefinite programming for max cut, and hardness of approximation

**D18. Integration and Capstones**
U18.1 Capstone A: the mathematics of machine learning, end to end; U18.2 Capstone B: a classical-ML library from scratch; U18.3 Capstone C: a deep-learning framework from scratch; U18.4 Capstone D: an LLM application platform (RAG + agents + safety); U18.5 Capstone E: generative models; U18.6 Capstone F: ML systems and efficiency; U18.7 Final integrated capstone: train, align, compress, serve, evaluate and secure a small language model
