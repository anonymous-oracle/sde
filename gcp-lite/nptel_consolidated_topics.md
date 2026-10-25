# NPTEL 2026 courses: consolidated, deduplicated topic list and where each topic lives in GCP Lite

Source: the 22 NPTEL / SWAYAM courses of the July 2026 semester (course layouts in `nptel_courses_26.md`). The 22 syllabi were merged into 192 unified topics: repeated topics collapsed to one entry with all their source courses listed, and each entry checked against the 29 existing topic files. Status: **Covered** = already in the index (no change); **Extended** = the index had part of it and the missing part was added; **Added** = a gap, new lines inserted. Original index lines were not altered: every insertion is new text placed in the matching group (or a new group), mirrored in `Consolidated_Topic_Index_GCP.md`.

## Source courses

- `cs129` Artificial Intelligence: Concepts and Techniques
- `cs182` Artificial Intelligence: Foundations and Algorithms
- `cs150` Cloud Computing
- `cs158` Computer Vision
- `mg99` Corporate Finance
- `cs144` Cyber Security and Privacy
- `cs112` Data Science for Engineers
- `cs146` Data Structures and Algorithms Design
- `cs162` Data Structure and Algorithms using Java
- `cs109` Programming, Data Structures And Algorithms Using Python
- `cs117` Data Base Management System
- `cs138` Deep Learning - IIT Ropar
- `mg139` Digital Marketing in the AI era, Part 1
- `cs157` Ethical Hacking
- `cs104` Generative AI for Computer Vision
- `cs171` Introduction to Large Language Models
- `cs161` Introduction to Internet of Things
- `cs119` Introduction to Machine Learning - IITKGP
- `cs123` Introduction To Operating Systems
- `ge72` Learning Analytics Tools
- `cs97` Mathematical Foundations of Generative AI
- `cs180` Natural Language Processing

## Summary

- Covered already: 56
- Extended (partial coverage, missing part added): 74
- Added (gap): 62

New material by destination: part 03 (correlation, pseudo-inverse); part 05 (Python core, R); part 07 (Java and the JVM); part 08 (algorithm techniques); part 09 (IoT and constrained networking); part 10 (OS teaching kernel, concurrency, information flow); part 11 (web services and SOA); part 12 (ER model); part 14 (ethical hacking, security management, privacy); part 16 (resource management, edge and fog); part 19 (classical AI, regression and learning theory, NLP, classical computer vision); part 20 (generative models, interpretability); new part 30 (corporate finance, marketing, learning analytics).


## AI foundations

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| AI01 | History and philosophy of AI; definitions (thinking vs acting, humanly vs rationally) | cs129, cs182 | Extended | Part 19 · Classical AI: search, knowledge and reasoning (new group) |
| AI02 | Rational agents; agent types; task environments and their properties | cs129, cs182 | Added | Part 19 · Classical AI: search, knowledge and reasoning (new group) |

## Search

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| AI03 | State-space formulation of a problem as search; uninformed search (BFS, DFS, uniform-cost, depth-limited, iterative deepening, bidirectional) | cs129, cs182 | Added | Part 19 · Classical AI: search, knowledge and reasoning (new group) |
| AI04 | Informed search: best-first, greedy, A*, optimality proof, admissible and consistent heuristics, domain relaxation, pattern databases, IDA*, depth-first branch and bound | cs129, cs182 | Added | Part 19 · Classical AI: search, knowledge and reasoning (new group) |
| AI05 | Local search: satisfaction vs optimization, hill climbing and its drawbacks, random walk and restart, simulated annealing, local beam search, N-Queens | cs129, cs182 | Added | Part 19 · Classical AI: search, knowledge and reasoning (new group) |
| AI06 | Genetic algorithms and operators; genetic programming; swarm intelligence | cs129, cs182 | Added | Part 19 · Classical AI: search, knowledge and reasoning (new group) |
| AI07 | Adversarial search: minimax, alpha-beta pruning and its analysis, cutoff, horizon effect, game databases | cs129, cs182 | Added | Part 19 · Classical AI: search, knowledge and reasoning (new group) |
| AI08 | Constraint satisfaction problems: representation, backtracking, variable and value ordering, inference (forward checking, arc consistency), exploiting structure | cs129, cs182 | Added | Part 19 · Classical AI: search, knowledge and reasoning (new group) |

## Logic

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| AI09 | Propositional and first-order logic: syntax, semantics, forward chaining, resolution, inference in FOL | cs129, cs182 | Extended | Part 19 · Classical AI: search, knowledge and reasoning (new group) |
| AI10 | Reduction to SAT; SAT solvers (DPLL, WalkSAT) | cs182 | Added | Part 19 · Classical AI: search, knowledge and reasoning (new group) |

## Knowledge

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| AI11 | Knowledge-based agents; knowledge representation schemes; non-monotonic reasoning | cs129 | Extended | Part 19 · Classical AI: search, knowledge and reasoning (new group) |
| AI12 | Expert systems and their applications; AI programming languages (Lisp, Prolog, CLIPS) | cs129 | Extended | Part 19 · Classical AI: search, knowledge and reasoning (new group) |

## Planning

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| AI13 | Classical planning, planning graphs, planning and scheduling | cs129 | Added | Part 19 · Classical AI: search, knowledge and reasoning (new group) |

## Uncertainty

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| AI14 | Probability for AI: conditional independence, Bayes rule | cs182 | Added | Part 19 · Classical AI: search, knowledge and reasoning (new group) |
| AI15 | Bayesian networks: syntax, factorization, d-separation, exact inference by variable elimination | cs129, cs182, cs119 | Extended | Part 19 · Classical AI: search, knowledge and reasoning (new group) |
| AI16 | Approximate inference in Bayes nets: rejection sampling, likelihood weighting, MCMC with Gibbs sampling | cs182 | Extended | Part 19 · Classical AI: search, knowledge and reasoning (new group) |
| AI17 | Learning Bayes nets: maximum likelihood, MAP, Bayesian learning, structure learning, expectation maximization | cs182 | Extended | Part 19 · Classical AI: search, knowledge and reasoning (new group) |
| AI18 | Dynamic belief networks; reduction of 3-SAT to Bayes net inference | cs129, cs182 | Added | Part 19 · Classical AI: search, knowledge and reasoning (new group) |

## Decisions

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| AI19 | Decision theory: steps, non-deterministic and probabilistic uncertainty, value of perfect information, utility theory, expected utility vs expected value | cs129, cs182 | Covered | Part 17 · Decision theory |
| AI20 | Markov decision processes: policy, policy evaluation (linear system, iterative), value iteration, policy iteration | cs182 | Extended | Part 19 · Specialised learning areas (added bullets) |
| AI21 | Reinforcement learning: passive model-based and model-free evaluation, TD learning, Q-learning, exploration vs exploitation, generalization, deep RL | cs182 | Extended | Part 19 · Specialised learning areas (added bullets) |

## Soft AI

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| AI22 | Fuzzy sets and systems; fuzzification and defuzzification | cs129 | Extended | Part 19 · Classical AI: search, knowledge and reasoning (new group) |

## Agents

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| AI23 | Multi-agent systems: web-based, mobile and negotiating agents | cs129 | Extended | Part 19 · Classical AI: search, knowledge and reasoning (new group) |

## Ethics

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| AI24 | AI ethics: humans vs robots, robustness and transparency, data bias and fairness, accountability, privacy, human-AI interaction | cs129, cs182 | Extended | Part 19 · Classical AI: search, knowledge and reasoning (new group) |

## Classical ML

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| ML01 | Types of learning; hypothesis space and inductive bias; evaluation and cross-validation | cs119 | Extended | Part 19 · Classical machine learning (added bullets) |
| ML02 | Linear regression; model assessment and diagnostics; multiple regression; variable and subset selection | cs119, cs112, ge72 | Added | Part 19 · Classical machine learning (added bullets) |
| ML03 | Decision trees (learning, overfitting) | cs119, ge72 | Covered | Part 08 · Analysis; Part 17 · Decision theory |
| ML04 | Instance-based learning (kNN); feature selection and feature extraction; collaborative filtering | cs119, cs112 | Extended | Part 19 · Classical machine learning (added bullets) |
| ML05 | Bayesian learning and Naive Bayes | cs119, ge72 | Covered | Part 03 · Exercises; Part 19 · Classical machine learning |
| ML06 | Logistic regression and classification performance measures (accuracy, precision, recall, F-score, kappa) | cs119, cs112, ge72 | Extended | Part 19 · Classical machine learning (added bullets) |
| ML07 | Support vector machines: dual formulation, maximum margin with noise, kernels | cs119 | Covered | Part 19 · Classical machine learning; Part 26 · Search / rank / ads; Part 29 · Other (pricing, classification, routing, dimensions and more) |
| ML08 | Computational learning theory: PAC model, sample complexity, VC dimension | cs119 | Added | Part 19 · Classical machine learning (added bullets) |
| ML09 | Ensembles: bagging, boosting | cs119, cs129 | Covered | Part 19 · Classical machine learning; Part 28 · LLM / genAI apps; Part 26 · Search / rank / ads |
| ML10 | Clustering: k-means, agglomerative hierarchical, Gaussian mixture model | cs119, cs112, ge72 | Covered | Part 19 · Classical machine learning; Part 19 · Exercises |
| ML11 | Correlation matrix; Spearman rank correlation | ge72 | Added | Part 03 · Statistics and experimental design (added bullets) |

## Deep learning

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| DL01 | McCulloch-Pitts neuron, perceptron, perceptron learning algorithm and its convergence proof, linearly separable Boolean functions | cs138, cs129 | Extended | Part 19 · Deep learning (added bullets) |
| DL02 | Sigmoid neurons; representation power of multilayer networks (universal approximation) | cs138 | Extended | Part 19 · Deep learning (added bullets) |
| DL03 | Feedforward networks; output and loss functions; backpropagation through a computational graph; information content, entropy, cross entropy | cs138, cs182 | Covered | Part 19 · Deep learning; Part 03 · Exercises; Part 03 · Information theory |
| DL04 | Optimizers: momentum, Nesterov, SGD and mini-batch, AdaGrad, RMSProp, Adam (bias correction), line search, learning-rate tips | cs138 | Covered | Part 19 · Deep learning; Part 19 · Exercises; Part 03 · Calculus and optimization |
| DL05 | Eigen decomposition, PCA (several interpretations), SVD | cs138, cs112 | Covered | Part 03 · Exercises; Part 19 · Classical machine learning; Part 03 · Linear algebra |
| DL06 | Autoencoders (relation to PCA; denoising, sparse, contractive) | cs138 | Covered | Part 20 · How LLMs work; Part 20 · Multimodal models |
| DL07 | Regularization: bias-variance, L2, dataset augmentation, parameter sharing, noise injection, early stopping, ensembles, dropout | cs138 | Covered | Part 19 · Deep learning; Part 19 · Exercises; Part 20 · Fine-tuning and adaptation |
| DL08 | Training practice: unsupervised pre-training, activation functions, initialization, batch normalization | cs138 | Covered | Part 19 · Exercises; Part 08 · Analysis; Part 19 · Deep learning |
| DL09 | CNNs: convolution operation, size relations, architectures (LeNet to ResNet), visualization (max-activating patches, filters, occlusion, guided backprop), Deep Dream, Deep Art, adversarial fooling | cs138, cs158, cs104 | Extended | Part 19 · Deep learning (added bullets) |
| DL10 | RNNs, backpropagation through time, vanishing and exploding gradients, truncated BPTT, LSTM and GRU | cs138, cs104 | Extended | Part 19 · Deep learning (added bullets) |
| DL11 | Encoder-decoder models; attention mechanism; attention over images; hierarchical attention | cs138, cs171 | Extended | Part 19 · Deep learning (added bullets) |
| DL12 | Thin deep vs fat shallow networks; deep tooling and hands-on practice with frameworks | cs182, cs129 | Extended | Part 19 · Deep learning (added bullets) |

## Embeddings

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| EMB01 | Word representations: one-hot, SVD, CBOW, skip-gram, contrastive estimation, hierarchical softmax, GloVe, evaluation; relation of SVD and Word2Vec | cs138, cs171, cs180 | Covered | Part 19 · Exercises; Part 19 · Natural language processing foundations; Part 25 · Recommend / personalize / feed |

## Vision

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| CV01 | Image processing fundamentals and image transforms | cs158 | Extended | Part 19 · Classical computer vision and geometry (new group) |
| CV02 | 2-D projective geometry, projective transformation, homography and its properties | cs158 | Added | Part 19 · Classical computer vision and geometry (new group) |
| CV03 | Camera geometry: pinhole model, intrinsics and extrinsics, calibration | cs158 | Added | Part 19 · Classical computer vision and geometry (new group) |
| CV04 | Stereo geometry: epipolar geometry, fundamental and essential matrices, rectification, triangulation, disparity | cs158 | Added | Part 19 · Classical computer vision and geometry (new group) |
| CV05 | Feature detection and description (corners, scale-space, SIFT-style descriptors) | cs158 | Added | Part 19 · Classical computer vision and geometry (new group) |
| CV06 | Feature matching and model fitting (RANSAC, Hough, least squares) | cs158 | Added | Part 19 · Classical computer vision and geometry (new group) |
| CV07 | Colour fundamentals and colour processing | cs158 | Added | Part 19 · Classical computer vision and geometry (new group) |
| CV08 | Range images: depth sensing, point clouds, range image processing | cs158 | Added | Part 19 · Classical computer vision and geometry (new group) |
| CV09 | Clustering and classification for vision; dimensionality reduction and sparse representation (sparse coding, dictionaries) | cs158 | Extended | Part 19 · Classical computer vision and geometry (new group) |
| CV10 | Deep architectures for vision: object detection, segmentation, vision applications | cs158, cs104 | Extended | Part 19 · Classical computer vision and geometry (new group) |

## Generative vision

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| GV01 | Generative modelling basics; generative vision models; image captioning, VQA, scene understanding | cs104 | Extended | Part 20 · Generative models beyond autoregression (new group) |
| GV02 | Autoregressive generative models; transformers; vision transformers | cs104, cs97 | Covered | Part 19 · Applied problem families; Part 20 · How LLMs work; Part 20 · Multimodal models |
| GV03 | Variational autoencoders: latent variable models, beta-VAE, VQ-VAE, improvisations | cs104, cs97 | Added | Part 20 · Generative models beyond autoregression (new group) |
| GV04 | GANs: formulation, DCGAN, conditional GAN, WGAN (clipping, gradient penalty), GAN inversion, FID, mode collapse | cs104, cs97 | Extended | Part 20 · Generative models beyond autoregression (new group) |
| GV05 | f-divergences and variational divergence minimization | cs97 | Extended | Part 20 · Generative models beyond autoregression (new group) |
| GV06 | Diffusion models: DDPM formulation, noise scheduling, conditional, score-based, implementation | cs104, cs97 | Added | Part 20 · Generative models beyond autoregression (new group) |
| GV07 | Flow matching models | cs97 | Added | Part 20 · Generative models beyond autoregression (new group) |
| GV08 | Vision-language models, multimodal generative models, LLMs for vision, agentic AI for vision | cs104 | Covered | Part 20 · Multimodal models; Part 21 · Retrieval-augmented generation; Part 19 · Specialised learning areas |

## LLM

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| LLM01 | NLP pipeline and applications; LLM recent advances overview | cs171 | Covered | Part 19 · Natural language processing foundations |
| LLM02 | Statistical language models; smoothing; evaluation (perplexity) | cs171, cs180 | Covered | Part 03 · Exercises; Part 03 · Information theory; Part 19 · Applied problem families |
| LLM03 | Tokenization strategies (BPE, WordPiece, unigram) | cs171 | Covered | Part 03 · Signals and sequences; Part 13 · Design techniques; Part 20 · How LLMs work |
| LLM04 | Neural LMs, seq2seq, decoding (greedy, beam, nucleus, temperature, top-k), attention in seq2seq | cs171 | Covered | Part 20 · How LLMs work; Part 22 · Exercises; Part 13 · Exercises |
| LLM05 | Transformers: self and multi-head attention, positional encoding, layer norm, implementation in PyTorch | cs171, cs104 | Covered | Part 20 · How LLMs work; Part 22 · Exercises; Part 20 · Multimodal models |
| LLM06 | Pre-training strategies: ELMo, BERT, encoder-decoder, decoder-only; Hugging Face | cs171 | Covered | Part 20 · Embeddings and retrieval; Part 20 · How LLMs work; Part 19 · Natural language processing foundations |
| LLM07 | Instruction tuning; prompt-based learning; advanced prompting and prompt sensitivity | cs171 | Covered | Part 20 · Fine-tuning and adaptation; Part 20 · How LLMs work; Part 20 · Multimodal models |
| LLM08 | Alignment: RLHF, PPO, DPO, reward modelling | cs171, cs97 | Covered | Part 20 · How LLMs work; Part 19 · Specialised learning areas; Part 28 · LLM / genAI apps |
| LLM09 | Knowledge graphs: representation, completion, evaluation, translation and rotation models, multiplicative models, hierarchies, temporal KGs; KGQA; GNN vs neural KG inference | cs171 | Added | Part 19 · Natural language processing foundations (added bullets) |
| LLM10 | Parameter-efficient fine-tuning (prompt/prefix tuning, LoRA); quantization, pruning, distillation | cs171, cs97 | Covered | Part 20 · Fine-tuning and adaptation; Part 22 · Exercises; Part 20 · Embeddings and retrieval |
| LLM11 | Residual-stream view of transformers; interpretability | cs171 | Extended | Part 20 · How LLMs work (added bullets) |
| LLM12 | Open-book QA and retrieval augmentation (REALM, RAG, FiD, Unlimiformer) | cs171 | Covered | Part 20 · How LLMs work; Part 21 · Retrieval-augmented generation; Part 14 · AI and LLM application threats |
| LLM13 | Responsible LLMs: bias, toxicity, hallucination, ethics | cs171 | Covered | Part 14 · AI and LLM application threats; Part 29 · Other (pricing, classification, routing, dimensions and more); Part 20 · Multimodal models |
| LLM14 | Survey of recent models (GPT-4, Llama, Claude, Mistral, Gemini) | cs171 | Covered | Part 20 · How LLMs work; Part 28 · LLM / genAI apps; Part 21 · Model APIs |

## NLP

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| NLP01 | Why NLP is hard; empirical laws of text (Zipf, Heaps); text processing basics | cs180 | Extended | Part 19 · Natural language processing foundations (added bullets) |
| NLP02 | Spelling correction: edit distance (weighted), noisy channel model | cs180, cs171, ge72 | Extended | Part 19 · Natural language processing foundations (added bullets) |
| NLP03 | Computational morphology and finite-state methods | cs180 | Extended | Part 19 · Natural language processing foundations (added bullets) |
| NLP04 | POS tagging: HMMs, Viterbi decoding, Baum-Welch | cs180 | Extended | Part 19 · Natural language processing foundations (added bullets) |
| NLP05 | Sequence labelling: maximum entropy models, CRFs | cs180 | Extended | Part 19 · Natural language processing foundations (added bullets) |
| NLP06 | Constituency parsing: CKY, PCFGs, inside-outside probabilities | cs180 | Extended | Part 19 · Natural language processing foundations (added bullets) |
| NLP07 | Dependency parsing: transition-based and MST-based | cs180 | Added | Part 19 · Natural language processing foundations (added bullets) |
| NLP08 | Distributional and lexical semantics: WordNet, word sense disambiguation, novel sense detection | cs180 | Extended | Part 19 · Natural language processing foundations (added bullets) |
| NLP09 | Topic models: LDA and Gibbs sampling, variants | cs180 | Extended | Part 19 · Natural language processing foundations (added bullets) |
| NLP10 | Entity linking; information extraction; relation extraction; distant supervision | cs180 | Extended | Part 19 · Natural language processing foundations (added bullets) |
| NLP11 | Text summarization (LexRank, optimization-based, evaluation); text classification | cs180 | Extended | Part 19 · Natural language processing foundations (added bullets) |
| NLP12 | Sentiment analysis: affective lexicons, aspect-based sentiment | cs180 | Extended | Part 19 · Natural language processing foundations (added bullets) |

## Algorithms

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| DS01 | What an algorithm is; efficiency; Euclid's gcd; sorting, searching and arrays as a first view | cs146, cs109 | Covered | Part 03 · Linear algebra; Part 03 · Proof and discrete mathematics; Part 01 ·  |
| DS02 | Clever algorithm problems: max-sum subarray in linear time, local minima in 1D and 2D, range-minima, half-majority | cs146 | Extended | Part 08 · Linear structures and techniques (added bullets) |
| DS03 | Asymptotics and recurrences | cs146, cs109 | Covered | Part 08 · Analysis; Part 03 · Proof and discrete mathematics; Part 04 · Contest mathematics toolkit |

## Data structures

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| DS04 | Abstract data types: lists, linked lists, stacks (expression evaluation), queues | cs146, cs162, cs109 | Covered | Part 11 · Object-oriented foundations; Part 06 · Go — engineering; Part 08 · Exercises |
| DS05 | BST (search, insert, delete), balancing, height-balanced trees, red-black trees, AVL | cs146, cs162, cs109 | Covered | Part 08 · Trees and heaps; Part 06 · Go — engineering |
| DS06 | Heaps: binary heap, heapification, priority queues; augmented trees | cs146, cs162, cs109 | Covered | Part 08 · Exercises; Part 08 · Trees and heaps; Part 06 · Go — engineering |
| DS07 | Disjoint-set (union-find), fast union; dynamic range-min and multi-increment | cs146 | Covered | Part 06 · Go — engineering; Part 08 · Exercises |

## Algorithms

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| DS08 | Order statistics: i-th statistic, approximate median, median of medians | cs146 | Extended | Part 08 · Sorting, searching and strings (added bullets) |
| DS09 | Divide and conquer: integer multiplication, inversions counting | cs146 | Covered | Part 04 · Systems thinking; Part 10 · Concurrency; Part 08 · Analysis |
| DS10 | Graph algorithms: BFS, DFS, bipartiteness, DFS tree, biconnectivity, articulation points | cs146, cs162 | Extended | Part 08 · Graph algorithms (added bullets) |
| DS11 | Greedy algorithms: job scheduling, MST, Dijkstra's algorithm | cs146, cs162 | Covered | Part 07 · Language theory; Part 08 · Exercises; Part 08 · Graph algorithms |
| DS12 | Linear-time sorting: counting sort, radix sort | cs146 | Covered | Part 08 · Analysis; Part 08 · Exercises |
| DS13 | Merge sort, quicksort and analysis; selection and insertion sort; in-place and stable sorting | cs109, cs162 | Covered | Part 08 · Analysis; Part 08 · Exercises; Part 08 · Sorting, searching and strings |
| DS14 | Backtracking (N-Queens, permutations); memoization and dynamic programming (grid paths, LCS, matrix-chain) | cs109 | Covered | Part 06 · Go — the everyday standard library; Part 08 · Linear structures and techniques; Part 18 · Docker |
| DS15 | Huffman coding and Huffman trees | cs162 | Covered | Part 03 · Information theory; Part 08 · Greedy algorithms and dynamic programming |
| DS16 | Linear and non-linear searching algorithms; binary search | cs162, cs109 | Covered | Part 06 · Go — engineering; Part 08 · Analysis |

## Python

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| PY01 | Types and expressions: int, float, bool, strings and string functions, formatted output | cs109 | Extended | Part 05 · Python › Core language (new sub-bullets) |
| PY02 | Control flow: loops, break, range(); pass, del, None | cs109 | Extended | Part 05 · Python › Core language (new sub-bullets) |
| PY03 | List comprehensions; higher-order functions (map, filter); passing functions as arguments; optional and default arguments | cs109 | Added | Part 05 · Python › Core language (new sub-bullets) |
| PY04 | Scope: local, global, nonlocal; nested functions | cs109 | Extended | Part 05 · Python › Core language (new sub-bullets) |
| PY05 | Input/output: standard input/output and file handling | cs109, cs162 | Extended | Part 05 · Python › Core language (new sub-bullets) |
| PY06 | Python memory model: names, mutable and immutable values; slices; arrays vs lists | cs109 | Covered | Part 05 · Python; Part 18 · Docker; Part 06 · Go — composite data, functions, errors and text |
| PY07 | Exceptions; classes and objects; user-defined data types | cs109 | Covered | Part 05 · Python; Part 06 · Go — composite data, functions, errors and text; Part 03 · Exercises |
| PY08 | Functional programming paradigm; other languages (C, manual memory management) | cs109 | Extended | Part 05 · Python › Core language (new sub-bullets) |

## Java

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| JV01 | Generics: generic methods and classes, bounded type parameters | cs162 | Extended | Part 07 · Java and the JVM (new group) |
| JV02 | Java Collections Framework: List, Set, Map, legacy classes (Vector, Hashtable), cursors and iterators | cs162 | Extended | Part 07 · Java and the JVM (new group) |
| JV03 | java.io: byte and character streams, file I/O, random access files | cs162 | Added | Part 07 · Java and the JVM (new group) |
| JV04 | String, StringBuffer, utilities | cs162 | Added | Part 07 · Java and the JVM (new group) |
| JV05 | Java language and OOP in Java | cs162 | Extended | Part 07 · Java and the JVM (new group) |

## Databases

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| DB01 | Intro to DBMS and the relational model; SQL (basic, intermediate, advanced); formal relational query languages | cs117 | Covered | Part 12 · Relational theory; Part 06 · Go — engineering; Part 12 ·  |
| DB02 | ER model; relational design and normalization | cs117 | Extended | Part 12 · Data modelling and design (added bullets) |
| DB03 | Application design and development (multi-tier, web database applications) | cs117 | Covered | Part 18 · Exercises; Part 24 · Exercises; Part 14 · Web application security |
| DB04 | Storage and file structure; indexing, hashing, index design | cs117 | Covered | Part 12 · Storage and access methods; Part 01 · ; Part 02 ·  |
| DB05 | Transactions: serializability, recoverability; concurrency control; recovery; query processing and optimization | cs117 | Covered | Part 07 · Exercises; Part 12 · Exercises; Part 12 · Transactions and concurrency control |

## OS

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| OS01 | PC hardware, booting, xv6 as a teaching OS | cs123 | Extended | Part 10 · Processes and threads (added bullets) |
| OS02 | Memory management: virtual memory, MMU mapping, segmentation | cs123 | Covered | Part 14 · Network security and zero trust; Part 19 · Specialised learning areas; Part 02 · Machine organization |
| OS03 | Processes: create, execute, exit; system calls for process management | cs123 | Covered | Part 10 · Exercises; Part 10 · Processes and threads; Part 02 · Machine organization |
| OS04 | Interrupts and handling; software interrupts; CPU context switching | cs123 | Extended | Part 10 · Processes and threads (added bullets) |
| OS05 | Scheduling: priority-based, multiprocessor, Linux scheduling, CFS | cs123 | Extended | Part 10 · CPU scheduling (added bullets) |
| OS06 | IPC; synchronization; critical sections (software solutions, bakery algorithm); hardware locks; mutexes; semaphores | cs123 | Extended | Part 10 · Concurrency (added bullets) |
| OS07 | Dining philosophers; deadlocks and dealing with them; threads | cs123 | Extended | Part 10 · Concurrency (added bullets) |
| OS08 | OS security: information-flow policies, buffer overflows and their prevention | cs123 | Extended | Part 10 · Isolation (added bullets) |

## Security

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| SEC01 | Ethical hacking: networking fundamentals for security, subnetting, routing protocols, IPv6 | cs157 | Covered | Part 09 · Addressing and the link layer; Part 23 · Google Cloud — command line; Part 09 · Routing |
| SEC02 | Reconnaissance and scanning: whois, dig, dnsenum, Netcraft, Google dorking, NMAP, Nessus, vulnerability scanning | cs157 | Extended | Part 14 · Ethical hacking and offensive techniques (new group) |
| SEC03 | System hacking: password cracking, privilege escalation, malware, trojans, viruses, worms | cs157 | Extended | Part 14 · Ethical hacking and offensive techniques (new group) |
| SEC04 | Network attacks: ARP spoofing, MAC attacks, DNS and email security, packet sniffing (Wireshark, Burp Suite) | cs157 | Added | Part 14 · Ethical hacking and offensive techniques (new group) |
| SEC05 | Social engineering; denial of service | cs157 | Extended | Part 14 · Ethical hacking and offensive techniques (new group) |
| SEC06 | Steganography; biometrics | cs157 | Added | Part 14 · Ethical hacking and offensive techniques (new group) |
| SEC07 | Hardware security: side-channel attacks, physical unclonable functions, hardware trojans | cs157 | Extended | Part 14 · Ethical hacking and offensive techniques (new group) |
| SEC08 | Web application attacks: SQL injection (auth bypass, error-based, sqlmap), XSS, file upload vulnerabilities; Metasploit | cs157 | Extended | Part 14 · Ethical hacking and offensive techniques (new group) |
| SEC09 | Cyber security management: CIA triad, cyber security vs information security, data breach case studies | cs144 | Extended | Part 14 · Security management, risk and governance (new group) |
| SEC10 | Governance, risk and compliance (GRC); security standards; security management | cs144 | Extended | Part 14 · Security management, risk and governance (new group) |
| SEC11 | Contingency planning: incident response, disaster recovery, business continuity planning | cs144 | Covered | Part 24 · Certifications — AWS; Part 24 · Certifications — Microsoft Azure; Part 16 · Architecture patterns and well-architected frameworks |
| SEC12 | Security policy tiers (enterprise, issue-specific, system-specific) | cs144 | Extended | Part 14 · Security management, risk and governance (new group) |
| SEC13 | Cyber risk management: identification, assessment, control | cs144 | Added | Part 14 · Security management, risk and governance (new group) |

## Privacy

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| SEC14 | Privacy foundations: information privacy, measurement, theories | cs144 | Added | Part 14 · Privacy (added bullets) |
| SEC15 | Privacy regulation: GDPR, India's DPDP Act, Aadhaar privacy; anonymity | cs144 | Added | Part 14 · Privacy (added bullets) |
| SEC16 | Economics of privacy: value of privacy (willingness to accept and to pay), business strategy, privacy vs safety | cs144 | Added | Part 14 · Privacy (added bullets) |

## Cloud

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| CL01 | Cloud overview, architecture, deployment models, XML basics, web services, SOA | cs150, cs161 | Extended | Part 11 · API design (added bullets) |
| CL02 | SLA; cloud economics | cs150 | Extended | Part 16 · Cloud economics and FinOps (added bullets) |
| CL03 | MapReduce; managing data in the cloud; OpenStack | cs150 | Extended | Part 16 · Virtualization and containers (added bullets) |
| CL04 | Resource management and VM allocation in the cloud; cloud broker and marketplace; cloud federation | cs150 | Extended | Part 16 · Resource management, edge and cloud paradigms (new group) |
| CL05 | Mobile cloud computing | cs150 | Added | Part 16 · Resource management, edge and cloud paradigms (new group) |
| CL06 | Fog, edge and dew computing; cloud-fog-edge analytics | cs150, cs161 | Added | Part 16 · Resource management, edge and cloud paradigms (new group) |
| CL07 | Green and sustainable cloud computing | cs150 | Covered | Part 14 · AI and LLM application threats; Part 16 · Architecture patterns and well-architected frameworks; Part 16 · Cloud economics and FinOps |
| CL08 | Cloud migration; container-based virtualization (Docker) | cs150 | Covered | Part 09 · DNS; Part 09 · Transport; Part 06 · Go — engineering |
| CL09 | Serverless and FaaS | cs150 | Covered | Part 14 · Cloud-specific attacks; Part 14 · Principles and economics; Part 16 · What cloud computing is |
| CL10 | Cloud in the 5G era; cyber-physical systems and cloud; sensor-cloud; IoT cloud; geo-spatial cloud; health-things case studies | cs150, cs161 | Added | Part 16 · Resource management, edge and cloud paradigms (new group) |

## IoT

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| IOT01 | IoT fundamentals: sensing and actuation; IoT networking; connectivity technologies (BLE, ZigBee, LoRa, etc.) | cs161 | Extended | Part 09 · IoT and constrained-device networking (new group) |
| IOT02 | Sensor networks; UAV networks; machine-to-machine communication; interoperability | cs161 | Extended | Part 09 · IoT and constrained-device networking (new group) |
| IOT03 | IoT application protocols (MQTT, CoAP) | cs161 | Added | Part 09 · IoT and constrained-device networking (new group) |
| IOT04 | Embedded platforms: Arduino, Raspberry Pi; interfacing sensors and actuators | cs161 | Extended | Part 09 · IoT and constrained-device networking (new group) |
| IOT05 | Software-defined networking and SDN for IoT | cs161 | Added | Part 09 · IoT and constrained-device networking (new group) |
| IOT06 | IoT verticals: smart cities and homes, connected vehicles, smart grid, industrial IoT, agriculture, healthcare, activity monitoring | cs161 | Added | Part 09 · IoT and constrained-device networking (new group) |
| IOT07 | IoT data handling and analytics | cs161 | Extended | Part 09 · IoT and constrained-device networking (new group) |

## Data science

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| DSE01 | R language: variables, data frames, joins, matrix operations, functions, control structures, basic graphics | cs112 | Added | Part 05 · R for data science (new group) |
| DSE02 | Linear algebra for data science: solving linear equations, rank, null space, pseudo-inverse, distance, hyperplanes and halfspaces | cs112 | Extended | Part 03 · Linear algebra (added bullets) |
| DSE03 | Statistical modelling: random variables, PMF/PDF, sample statistics, hypothesis testing | cs112 | Covered | Part 03 · Probability; Part 03 · Statistics and experimental design; Part 19 · MLOps |
| DSE04 | Optimization: unconstrained multivariate, gradient descent, equality constraints (Lagrange), inequality constraints (KKT) | cs112 | Covered | Part 03 · Calculus and optimization; Part 19 · Classical machine learning; Part 29 · Other (pricing, classification, routing, dimensions and more) |
| DSE05 | Data science problem typology and a guided solution framework | cs112 | Added | Part 19 · Classical AI: search, knowledge and reasoning (new group) |
| DSE06 | Data preprocessing: missing data, outliers, categorical encoding, transformations | ge72 | Covered | Part 05 · Python; Part 19 · Classical machine learning; Part 19 · Deep learning |

## Finance

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| CF01 | Corporate finance basics: goals of the firm, governance, sources of finance | mg99 | Added | Part 30 · Corporate finance (new part) |
| CF02 | Return, risk and portfolio theory (CAPM, diversification) | mg99 | Added | Part 30 · Corporate finance (new part) |
| CF03 | Time value of money; valuation of cash flows, bonds and stocks | mg99 | Added | Part 30 · Corporate finance (new part) |
| CF04 | Capital budgeting: NPV, IRR, payback, profitability index | mg99 | Added | Part 30 · Corporate finance (new part) |
| CF05 | Cost of capital (WACC) and firm value | mg99 | Added | Part 30 · Corporate finance (new part) |
| CF06 | Leverage (operating, financial, combined); capital structure theories (MM, trade-off, pecking order) | mg99 | Added | Part 30 · Corporate finance (new part) |
| CF07 | Working capital: liquidity measures, operating and cash conversion cycles, inventory (EOQ) and credit management | mg99 | Added | Part 30 · Corporate finance (new part) |
| CF08 | Dividend decisions and theories (Gordon, MM, Lintner) | mg99 | Added | Part 30 · Corporate finance (new part) |

## Marketing

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| MK01 | Marketing fundamentals: eras, branding, segmentation-targeting-positioning, 4Ps, 3P and 4C | mg139 | Added | Part 30 · Marketing and digital marketing (new part) |
| MK02 | Digital marketing: frameworks (RACE, AIDA), channel ecosystem, performance metrics | mg139 | Added | Part 30 · Marketing and digital marketing (new part) |
| MK03 | Content marketing: content types, funnel (TOFU, MOFU, BOFU), AI in the content workflow | mg139 | Added | Part 30 · Marketing and digital marketing (new part) |
| MK04 | Social media marketing and planning; influencer marketing; SEO | mg139 | Added | Part 30 · Marketing and digital marketing (new part) |
| MK05 | Email marketing: foundations, campaigns, AI-powered campaigns | mg139 | Added | Part 30 · Marketing and digital marketing (new part) |

## Analytics

| ID | Topic | Courses | Status | Where in GCP Lite |
|---|---|---|---|---|
| LA01 | Learning analytics: definition, academic analytics, educational data mining, four levels (descriptive, diagnostic, predictive, prescriptive) | ge72 | Added | Part 30 · Learning analytics (new part) |
| LA02 | Educational data collection; technology-enhanced learning; ethics and student privacy | ge72 | Added | Part 30 · Learning analytics (new part) |
| LA03 | Descriptive analytics: chart types and comparison, dashboards, Excel | ge72 | Added | Part 30 · Learning analytics (new part) |
| LA04 | Sequential pattern mining; differential sequence mining; process mining | ge72 | Added | Part 30 · Learning analytics (new part) |
| LA05 | Multimodal learning analytics: affective computing, eye tracking | ge72 | Added | Part 30 · Learning analytics (new part) |
| LA06 | Analytics tools: Weka, Orange, iSAT, ProM, Excel | ge72 | Added | Part 30 · Learning analytics (new part) |

## Placement decisions

- Corporate finance, marketing and learning analytics have no natural home in the engineering parts, so they form a new, optional part 30. Finance connects back to cloud economics (part 16) and build-buy-rent decisions (part 17).
- Java is its own group in part 07 (beside TypeScript and Node), not part 06, which is Go-specific.
- R is a short group in part 05 after Python.
- Classical AI (search, logic, planning, Bayesian networks) is a new group in part 19, between Foundations of AI and Classical machine learning.
- Coverage screening used keyword probes, which are approximate; borderline items were judged by reading the destination group.
