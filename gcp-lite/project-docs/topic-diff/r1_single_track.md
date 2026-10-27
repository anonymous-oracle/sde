# Topic diff: Single learning track S0-S24

Source: gcp/unified-curriculum.md lines 197-385. Compared against: gcp-lite/index/*.topics.md and gcp-lite/Rust_Track_AI_Infrastructure.md.

Counts: 394 topics; 226 covered, 127 partial, 33 missing, 8 out of scope.

## 5. Single Graph-Ordered Learning Track

Stage table, lines 203-229, and prose, lines 256-360. Rows are theory items, first appearance only.

## 5.2 S0-S4: Computing, Language, and Reasoning Foundations

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| S0 bits and bytes | covered | part02_computer_organization.topics.md › line 10 | Bits and bytes; why base 2 |
| S0 CPU, memory and storage | covered | part02_computer_organization.topics.md › memory hierarchy (56-78) | |
| S0 files versus directories, absolute and relative paths | partial | part10_operating_systems.topics.md › Linux (7-16) | File system named at heading level; paths not spelled out |
| S0 process versus program | partial | part10_operating_systems.topics.md › processes (18-28) | Processes covered; program/process distinction not stated |
| S0 environment variables | missing | - | Not in part05 or part06 read; → suggest part05 |
| S0 ports | partial | part09_networking.topics.md › addressing (15-21) | Port numbers not confirmed |
| S0 DNS, HTTP and JSON vocabulary | covered | part09_networking.topics.md › DNS (58-66), HTTP semantics (70-78); part07_programming_languages_typescript_wire_theory_exercises.topics.md › JSON (34) | |
| S0 shell composition, exit status, standard streams | covered | part05_programming_languages_python_and_shell.topics.md › shell (44-47); line 20 standard I/O | |
| S0 Git working tree, index, commit and remote | covered | part15_software_delivery.topics.md › Git data model (13-19), Git CLI (20-26) | |
| S0 reproducible repository layout | partial | part18_devops_sre.topics.md › reproducible builds (75) | Builds covered; repo layout not named |
| S1 numeric representation and integer overflow by dtype | covered | part02_computer_organization.topics.md › two's complement (13); part06_programming_languages_go.topics.md › types (30) | Python dtype overflow not stated |
| S1 floating-point error and tolerance-based assertions | covered | part06_programming_languages_go.topics.md › IEEE 754 (31); part03_mathematics.topics.md › numerical computing (146-154) | |
| S1 Python core: names, collections, functions, modules, exceptions, file and JSON I/O | covered | part05_programming_languages_python_and_shell.topics.md › Python core | |
| S1 virtual environments | covered | part05_programming_languages_python_and_shell.topics.md › line 22 | |
| S1 pytest | partial | part05_programming_languages_python_and_shell.topics.md | Testing present; pytest not named |
| S1 NumPy ndarray, shape, dtype and broadcasting | covered | part05_programming_languages_python_and_shell.topics.md › NumPy (31) | |
| S1 strides, copy versus view | partial | part05_programming_languages_python_and_shell.topics.md › NumPy (31) | Strides and copy/view aliasing not named |
| S1 seeded generators | partial | part05_programming_languages_python_and_shell.topics.md › NumPy (31) | "random routines" only |
| S1 units, SI prefixes and estimation | covered | part01_school_foundations.topics.md › units (12-15); part03_mathematics.topics.md › Fermi estimation (108) | |
| S2 module, package and function layout | covered | part06_programming_languages_go.topics.md › Go core (16) | |
| S2 scalar types, conversions and control flow | covered | part06_programming_languages_go.topics.md › types and control flow (25-37) | |
| S2 arrays, slices and maps; aliasing and growth | covered | part06_programming_languages_go.topics.md › slices and maps (41-49) | |
| S2 strings, bytes and runes | covered | part06_programming_languages_go.topics.md › strings (64-70) | |
| S2 structs and zero values | covered | part06_programming_languages_go.topics.md › structs (81-87) | |
| S2 errors and wrapping | covered | part06_programming_languages_go.topics.md › errors (56-63) | |
| S2 table tests, formatting, vetting and benchmarks | covered | part06_programming_languages_go.topics.md › testing (171-177); gofmt and go vet (16) | |
| S3 fractions, ratios, units and estimation | covered | part01_school_foundations.topics.md › units (12-15) | |
| S3 equations, inequalities, absolute value, exponents and logs | covered | part01_school_foundations.topics.md › algebra (16-19), exponents and logs (24-27) | |
| S3 polynomials and sequences | covered | part01_school_foundations.topics.md › algebra (16-19), sequences (28-30) | |
| S3 relations and functions: domain, codomain, range, inverse, composition | covered | part01_school_foundations.topics.md › functions and graphs (20-23) | |
| S4 propositions, quantifiers and proof techniques | covered | part03_mathematics.topics.md › proof and logic (7-39) | |
| S4 sets, functions and relations | covered | part03_mathematics.topics.md › proof and logic (7-39) | |
| S4 induction | covered | part03_mathematics.topics.md › proof and logic (7-39) | |
| S4 invariants | partial | part08_data_structures_algorithms.topics.md › analysis (7-21) | Named as a proof tool only in passing |
| S4 counting and pigeonhole | covered | part03_mathematics.topics.md › proof and logic (7-39) | |
| S4 recurrences | covered | part08_data_structures_algorithms.topics.md › analysis (7-21) | |
| S4 graphs and state machines | covered | part08_data_structures_algorithms.topics.md › graphs (64-74); part02_computer_organization.topics.md › finite state machines (37-44) | |
| S4 arrays, stacks, queues and maps in Go | covered | part08_data_structures_algorithms.topics.md › linear structures (23-31), hashing (33-39) | |
## 5.3 S5-S10: Mathematical and Algorithmic Core

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| S5 coordinate geometry and distance metrics (Euclidean, Manhattan, cosine) | partial | part03_mathematics.topics.md › linear algebra (112-123); cosine similarity in Go from-scratch line (182) | Coordinate geometry and Manhattan distance not named |
| S5 dot product, angles and projections | covered | part03_mathematics.topics.md › linear algebra (112-123) | |
| S5 affine combinations, lines, planes and transformations | partial | part03_mathematics.topics.md › linear algebra (112-123) | Affine not named |
| S6 pointers, structs, method sets, interfaces and generics | covered | part06_programming_languages_go.topics.md › pointers (74-80), structs (81-87), interfaces (88-96), generics (97-103) | |
| S6 nil-interface traps | covered | part06_programming_languages_go.topics.md › interfaces (62) | Typed-nil trap |
| S6 linked structures, BST, heap and priority queue | covered | part08_data_structures_algorithms.topics.md › trees and heaps (41-50) | |
| S6 union-find | covered | part06_programming_languages_go.topics.md › data structures (230) | |
| S6 hash tables and amortized growth | covered | part08_data_structures_algorithms.topics.md › hashing (33-39) | |
| S6 allocation and escape intuition | covered | part06_programming_languages_go.topics.md › pointers and escape (74-80) | |
| S7 Gaussian elimination, rank and nullity | covered | part03_mathematics.topics.md › linear algebra (112-123) | |
| S7 span, independence, basis and dimension | covered | part03_mathematics.topics.md › linear algebra (112-123) | |
| S7 four fundamental subspaces | partial | part03_mathematics.topics.md › linear algebra (112-123) | Subspaces not named |
| S7 linear maps | covered | part03_mathematics.topics.md › linear algebra (112-123) | |
| S7 orthogonality and projection | covered | part03_mathematics.topics.md › linear algebra (112-123) | |
| S7 least squares | partial | part03_mathematics.topics.md › linear algebra (112-123) | Not named |
| S7 determinants | covered | part03_mathematics.topics.md › from-scratch Go vector and matrix package (182) | |
| S7 eigenvalues, eigenvectors and diagonalization | covered | part03_mathematics.topics.md › eigenvalues and power iteration (120) | |
| S7 symmetric and positive-definite matrices | partial | part03_mathematics.topics.md › linear algebra (112-123) | Not named |
| S7 SVD and pseudoinverse | partial | part03_mathematics.topics.md › linear algebra (112-123) | SVD partly covered; pseudoinverse not found |
| S7 condition number | partial | part03_mathematics.topics.md › numerical computing (151) | Conditioning named; condition number not |
| S7 PCA and low-rank approximation | covered | part19_machine_learning.topics.md › dimensionality reduction (59); part03_mathematics.topics.md › from-scratch PCA projection (182) | |
| S7 QR factorization and Gram-Schmidt | partial | part03_mathematics.topics.md › from-scratch Gram-Schmidt (182) | Gram-Schmidt covered; QR not named |
| S8 asymptotic models and lower-bound intuition | covered | part08_data_structures_algorithms.topics.md › analysis (7-21) | |
| S8 loop and recurrence analysis | covered | part08_data_structures_algorithms.topics.md › analysis (7-21) | |
| S8 binary search invariant | partial | part08_data_structures_algorithms.topics.md › sorting (52-62) | Invariant not stated |
| S8 elementary and divide-and-conquer sorting | covered | part08_data_structures_algorithms.topics.md › sorting (52-62) | |
| S8 heaps and selection | covered | part08_data_structures_algorithms.topics.md › trees and heaps (41-50) | |
| S8 hashing and amortization | covered | part08_data_structures_algorithms.topics.md › hashing (33-39) | |
| S8 BFS, DFS and topological order | covered | part08_data_structures_algorithms.topics.md › graphs (64-74) | |
| S8 strongly connected components | partial | part08_data_structures_algorithms.topics.md › graphs (64-74) | Not named |
| S8 shortest paths | covered | part08_data_structures_algorithms.topics.md › graphs (64-74) | |
| S8 MST and greedy exchange | partial | part08_data_structures_algorithms.topics.md › greedy (76-81); part03_mathematics.topics.md › Huffman (161) | |
| S8 dynamic programming | covered | part08_data_structures_algorithms.topics.md › greedy and DP (76-81) | |
| S8 max-flow | covered | part08_data_structures_algorithms.topics.md › graphs (73) | Max-flow and min-cut named |
| S9 limits and continuity | covered | part03_mathematics.topics.md › calculus and optimization (125-144) | |
| S9 derivatives, product and chain rules | covered | part03_mathematics.topics.md › calculus and optimization (125-144) | |
| S9 implicit differentiation | partial | part03_mathematics.topics.md › calculus and optimization (125-144) | Not named |
| S9 gradient | covered | part03_mathematics.topics.md › calculus and optimization (125-144) | |
| S9 Jacobian and Hessian | partial | part03_mathematics.topics.md › calculus and optimization (125-144) | Hessian not named |
| S9 definite integral and fundamental theorem | partial | part03_mathematics.topics.md › calculus and optimization (125-144) | Integration named at heading level |
| S9 integration methods | partial | part03_mathematics.topics.md › numerical computing (146-154) | |
| S9 sequences and series | partial | part01_school_foundations.topics.md › sequences (28-30) | Series not named |
| S9 multiple integrals and vector-calculus intuition | missing | - | Divergence and curl not found; → suggest part03 |
| S9 ODE models | covered | part03_mathematics.topics.md › RK4 (132) | |
| S9 floating-point error, conditioning and stability | partial | part03_mathematics.topics.md › numerical computing (146-154); part06_programming_languages_go.topics.md › IEEE 754 (31) | Conditioning not named |
| S9 roots and interpolation | partial | part03_mathematics.topics.md › numerical computing (146-154) | Root finding not confirmed |
| S9 Euler and RK4 | covered | part03_mathematics.topics.md › RK4 (132) | |
| S9 finite differences | partial | part03_mathematics.topics.md › numerical computing (146-154) | Not named |
| S10 sample spaces, counting, conditioning and Bayes | covered | part03_mathematics.topics.md › probability (41-70) | |
| S10 discrete and continuous random variables | covered | part03_mathematics.topics.md › probability (41-70) | |
| S10 joint, marginal and conditional laws | covered | part03_mathematics.topics.md › probability (41-70) | |
| S10 expectation, variance and covariance | covered | part03_mathematics.topics.md › probability (41-70) | |
| S10 transformations of random variables | partial | part03_mathematics.topics.md › probability (41-70) | Change of variable not named |
| S10 concentration, LLN and CLT | covered | part03_mathematics.topics.md › probability (41-70) | |
| S10 random processes and Markov chains | partial | part03_mathematics.topics.md › probability (41-70) | Entry level only |
| S10 sampling and estimands | covered | part03_mathematics.topics.md › sampling and Monte Carlo (53) | |
| S10 MLE | covered | part03_mathematics.topics.md › statistics (72-91) | |
| S10 MAP | partial | part19_machine_learning.topics.md › Bayesian inference (34); part28_ml_case_studies_4of5.topics.md › Wayfair (38) | Case-study mention only |
| S10 sufficiency | missing | - | Not found; → suggest part03 |
| S10 confidence intervals and tests | covered | part03_mathematics.topics.md › statistics (72-91) | |
| S10 bootstrap | covered | part03_mathematics.topics.md › statistics (72-91) | |
| S10 permutation tests | partial | part03_mathematics.topics.md › statistics (72-91) | Not named |
| S10 regression diagnostics | partial | part19_machine_learning.topics.md › regression (73) | |
| S10 Bayesian updating | covered | part03_mathematics.topics.md › probability (41-70) | |
| S10 entropy, cross-entropy, KL and mutual information | covered | part03_mathematics.topics.md › information theory (156-163) | |
| S10 experiment design and sequential caveats | partial | part03_mathematics.topics.md › statistics (72-91) | A/B testing covered; sequential testing not named |
## 5.4 S11-S14: Classical ML, Databases, Optimization, RL, and Causality

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| S11 problem, label and metric framing with a non-ML baseline | partial | part19_machine_learning.topics.md › evaluation (60-67) | Baseline not named |
| S11 split strategy, leakage boundary and calibration | partial | part19_machine_learning.topics.md › evaluation (60-67); calibration (64); near-duplicate leakage (187) | Calibration covered; leakage only in passing |
| S11 kNN | covered | part19_machine_learning.topics.md › other supervised (56) | |
| S11 linear and regularized regression | covered | part19_machine_learning.topics.md › linear models (53-55), regularization as constraint (48) | |
| S11 logistic and softmax regression | covered | part19_machine_learning.topics.md › linear models (53-55) | |
| S11 GLMs | partial | part19_machine_learning.topics.md › linear models (53-55) | Not named |
| S11 naive Bayes | covered | part03_mathematics.topics.md › from-scratch naive Bayes (186) | |
| S11 LDA and QDA | partial | part19_machine_learning.topics.md › classical ML (42-75) | Not named; LDA appears only as a topic model (111) |
| S11 margins, kernels and SVM | partial | part19_machine_learning.topics.md › other supervised (56) | |
| S11 trees, bagging, random forests and boosting | covered | part19_machine_learning.topics.md › trees and ensembles (57) | |
| S11 clustering | covered | part19_machine_learning.topics.md › unsupervised and anomaly (58) | |
| S11 GMM and EM | partial | part19_machine_learning.topics.md › unsupervised and anomaly (58) | Not named |
| S11 PCA and feature selection | covered | part19_machine_learning.topics.md › dimensionality reduction (59), feature selection (75) | |
| S11 anomaly detection | covered | part19_machine_learning.topics.md › unsupervised and anomaly (58) | |
| S11 ranking and recommendation | covered | part19_machine_learning.topics.md › recommendation (154-158), search and LTR (159-164) | |
| S12 relations, keys, functional dependencies and normalization | covered | part12_databases.topics.md › relational theory (17-44) | |
| S12 relational algebra | covered | part12_databases.topics.md › relational theory (17-44) | |
| S12 DDL, types and constraints | partial | part12_databases.topics.md › data modelling (132-146) | |
| S12 SELECT semantics and NULL three-valued logic | covered | part12_databases.topics.md › SQL (46-62), NULL (50) | |
| S12 joins including semi, anti and outer | partial | part12_databases.topics.md › SQL (46-62) | Semi and anti joins not named |
| S12 aggregation | covered | part12_databases.topics.md › SQL (46-62) | |
| S12 subqueries, CTEs and recursion | covered | part12_databases.topics.md › SQL (46-62), CTEs (56) | |
| S12 window functions | covered | part12_databases.topics.md › SQL (46-62), window functions (55) | |
| S12 transactions and isolation | covered | part12_databases.topics.md › transactions (104-116), isolation (112) | |
| S12 pagination | partial | part12_databases.topics.md › SQL (46-62) | Not named |
| S12 database/sql client, parameterization and pool limits | covered | part06_programming_languages_go.topics.md › database/sql (190-197) | |
| S12 context cancellation | covered | part06_programming_languages_go.topics.md › concurrency and context (147-148) | |
| S13 storage layouts: row, column and log-structured | covered | part12_databases.topics.md › storage (64-81), LSM (78) | |
| S13 pages, tuples, TOAST and catalogs | partial | part12_databases.topics.md › storage (64-81) | TOAST not named |
| S13 buffer manager | partial | part12_databases.topics.md › storage (64-81) | Not named |
| S13 B-tree indexes | covered | part12_databases.topics.md › storage (64-81), B+ trees (76) | |
| S13 hash, GIN, GiST and BRIN indexes | partial | part12_databases.topics.md › storage (64-81) | GIN, GiST and BRIN not named |
| S13 vector indexes | covered | part20_generative_ai_1of3.topics.md › IVF (152), HNSW (154) | |
| S13 iterators, sort, aggregate and join algorithms | covered | part12_databases.topics.md › query processing (83-102), Volcano (86) | |
| S13 statistics, cardinality and cost-based plans | covered | part12_databases.topics.md › query processing (83-102), Selinger (95) | |
| S13 MVCC, locks and deadlocks | partial | part12_databases.topics.md › transactions (104-116), MVCC (111), 2PL (108) | Deadlocks not named |
| S13 vacuum | partial | part12_databases.topics.md › transactions (104-116) | Not named |
| S13 WAL, checkpoints and recovery | covered | part12_databases.topics.md › recovery (118-130), WAL (121), ARIES (122) | |
| S13 replication and PITR | partial | part13_distributed_systems.topics.md › replication (39-47) | PITR not named |
| S13 parallel and distributed trade-offs | covered | part13_distributed_systems.topics.md › foundations (7-28) | |
| S14 convexity | partial | part03_mathematics.topics.md › calculus and optimization (125-144) | Not named |
| S14 first- and second-order methods | partial | part03_mathematics.topics.md › calculus and optimization (125-144) | Newton and BFGS not named |
| S14 SGD, momentum and adaptive methods | covered | part19_machine_learning.topics.md › optimizers (85); part03_mathematics.topics.md › momentum and adaptive optimizers (140) | |
| S14 constraints, Lagrangian and KKT | covered | part03_mathematics.topics.md › constrained optimization (142) | |
| S14 duality | partial | part03_mathematics.topics.md › constrained optimization (142) | Not named |
| S14 proximal methods | missing | - | Not found; → suggest part03 |
| S14 coordinate descent | covered | part03_mathematics.topics.md › regularization and coordinate descent (141); part19_machine_learning.topics.md › lasso (48) | |
| S14 LP and assignment | covered | part03_mathematics.topics.md › linear programming and Hungarian method (143) | |
| S14 robust and stochastic formulations | missing | - | Not found; → suggest part03 |
| S14 non-convex diagnostics | missing | - | Not found; → suggest part03 |
| S14 exploration and multi-armed bandits | covered | part03_mathematics.topics.md › bandits (177); part19_machine_learning.topics.md › explore and exploit (165-169) | |
| S14 MDP and Bellman equations | covered | part19_machine_learning.topics.md › reinforcement learning (124, 134) | Bellman not named; MDPs and value functions covered |
| S14 dynamic programming for RL | partial | part19_machine_learning.topics.md › reinforcement learning in detail (134) | Value and policy iteration covered |
| S14 Monte Carlo methods for RL | partial | part19_machine_learning.topics.md › Monte Carlo tree search (23) | RL Monte Carlo not named |
| S14 temporal difference and Q-learning | covered | part19_machine_learning.topics.md › reinforcement learning in detail (134) | |
| S14 function approximation and policy gradients | covered | part19_machine_learning.topics.md › reinforcement learning (124) | Function approximation not named |
| S14 causal question, estimand and intervention | covered | part19_machine_learning.topics.md › causal inference (189, 194) | |
| S14 potential outcomes | covered | part19_machine_learning.topics.md › causal inference (189) | |
| S14 DAGs | covered | part03_mathematics.topics.md › causal DAGs and adjustment (89) | |
| S14 SCMs | missing | - | Not found; → suggest part19 |
| S14 randomization | covered | part19_machine_learning.topics.md › causal inference (189) | |
| S14 backdoor adjustment | partial | part03_mathematics.topics.md › causal DAGs and adjustment (89) | Named as DAG adjustment; criterion not stated |
| S14 frontdoor adjustment | missing | - | Not found; → suggest part19 |
| S14 heterogeneous effects and uplift | covered | part19_machine_learning.topics.md › randomization and uplift (189) | |
| S14 overlap | missing | - | Not found; → suggest part19 |
| S14 sensitivity analysis | missing | - | Not found; → suggest part19 |
| S14 instrumental variables | covered | part19_machine_learning.topics.md › causal inference (194) | |
| S14 difference-in-differences | covered | part03_mathematics.topics.md › difference-in-differences (90); part19_machine_learning.topics.md › causal inference (194) | |
| S14 regression discontinuity | missing | - | Not found; → suggest part19 |
| S14 synthetic control | covered | part19_machine_learning.topics.md › causal inference (194) | |
## 5.5 S15-S16: Domain Mathematics and Deep Learning

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| S15-A convolution and correlation | covered | part03_mathematics.topics.md › signals and sequences (165-172) | |
| S15-A signal classes, energy and power | partial | part03_mathematics.topics.md › signals and sequences (165-172) | Not named |
| S15-A complex exponentials | partial | part03_mathematics.topics.md › signals and sequences (165-172) | Not named |
| S15-A impulse and step | partial | part03_mathematics.topics.md › signals and sequences (165-172) | Not named |
| S15-A LTI properties | partial | part03_mathematics.topics.md › signals and sequences (165-172) | Not named |
| S15-A frequency response | partial | part03_mathematics.topics.md › signals and sequences (165-172) | Not named |
| S15-A Fourier series and transform | partial | part03_mathematics.topics.md › signals and sequences (165-172) | DFT and FFT covered; continuous forms not named |
| S15-A Laplace and z-transform | missing | - | No match; → suggest part03 |
| S15-A DFT and FFT | covered | part03_mathematics.topics.md › signals and sequences (165-172) | |
| S15-A sampling and aliasing | partial | part19_machine_learning.topics.md › classical CV (138) | Sampling named for images; aliasing not named |
| S15-A windows and leakage | covered | part03_mathematics.topics.md › signals and sequences (165-172) | Windowing |
| S15-A FIR and IIR filters | missing | - | No match; → suggest part03 |
| S15-A pole-zero stability | missing | - | No match; → suggest part03 |
| S15-A STFT | covered | part03_mathematics.topics.md › signals and sequences (165-172) | |
| S15-A filter banks | missing | - | No match; → suggest part03 |
| S15-A cepstrum and MFCC | partial | part19_machine_learning.topics.md › audio and speech (128) | MFCC covered; cepstrum not named |
| S15-A multirate processing | missing | - | No match; → suggest part03 |
| S15-A quantization | partial | part19_machine_learning.topics.md › classical CV (138) | Image sampling and quantization only |
| S15-A Parseval and reconstruction checks | missing | - | No match; → suggest part03 |
| S15-B image formation | partial | part19_machine_learning.topics.md › classical CV (136-147) | Camera geometry covered; image formation not named |
| S15-B sampling and quantization | covered | part19_machine_learning.topics.md › classical CV (138) | |
| S15-B color and gamma | partial | part19_machine_learning.topics.md › classical CV (139) | Color named; gamma not named |
| S15-B point transforms and histograms | partial | part19_machine_learning.topics.md › classical CV (136-147) | |
| S15-B 2D convolution and separable filters | partial | part03_mathematics.topics.md › signals and sequences (165-172) | Not named for images |
| S15-B denoising and sharpening | partial | part03_mathematics.topics.md › signals and sequences (165-172) | Not named |
| S15-B gradients and edges | covered | part03_mathematics.topics.md › Sobel (signals and sequences) | |
| S15-B morphology | covered | part03_mathematics.topics.md › morphology (signals and sequences) | |
| S15-B Fourier image filtering | partial | part03_mathematics.topics.md › DFT and FFT (signals and sequences) | |
| S15-B restoration and deconvolution | missing | - | Not found; → suggest part19 |
| S15-B segmentation | partial | part19_machine_learning.topics.md › classical CV (136-147) | Not named |
| S15-B corners, descriptors and matching | covered | part19_machine_learning.topics.md › classical CV (136-147), features (140-144) | |
| S15-B homography and RANSAC | covered | part19_machine_learning.topics.md › classical CV (140-144) | |
| S15-B camera calibration and epipolar geometry | covered | part19_machine_learning.topics.md › camera geometry and stereo (140-144) | |
| S15-B optical flow | missing | - | No match; → suggest part19 |
| S15-B detection and recognition metrics | covered | part19_machine_learning.topics.md › evaluation (60-67), mean average precision (187) | |
| S15-B reproducibility of image experiments | partial | part19_machine_learning.topics.md › evaluation (60-67) | |
| S15-C Unicode, code points and graphemes | covered | part06_programming_languages_go.topics.md › strings, bytes and runes (64-70) | |
| S15-C normalization | covered | part06_programming_languages_go.topics.md › Unicode normalisation (69); part19_machine_learning.topics.md › cleaning (101) | |
| S15-C regular expressions and finite-state basics | partial | part06_programming_languages_go.topics.md › RE2 (112); part12_databases.topics.md › LIKE (46-62) | Finite automata not named |
| S15-C linguistic units and tokenization | covered | part19_machine_learning.topics.md › NLP foundations (98-114); part20_generative_ai_1of3.topics.md › tokenization (12-16) | |
| S15-C sentence splitting | partial | part19_machine_learning.topics.md › NLP foundations (98-114) | Not named |
| S15-C edit distance | covered | part19_machine_learning.topics.md › spelling correction (106) | |
| S15-C n-grams, smoothing and perplexity | partial | part20_generative_ai_1of3.topics.md › n-grams (17) | Smoothing and perplexity not named |
| S15-C inverted indexes, Boolean retrieval and TF-IDF | covered | part19_machine_learning.topics.md › TF-IDF (102); part21_generative_ai_2of3.topics.md › BM25 (139) | Inverted index not named |
| S15-C BM25 | covered | part20_generative_ai_1of3.topics.md › BM25 (139) | |
| S15-C word vectors | covered | part19_machine_learning.topics.md › word2vec (103) | |
| S15-C BPE tokenization | covered | part22_generative_ai_3of3.topics.md › exercise BPE (159) | |
| S15-C WordPiece and unigram tokenization | partial | part20_generative_ai_1of3.topics.md › tokenization (12-16) | Not named |
| S15-C tagging and parsing | covered | part19_machine_learning.topics.md › sequence labelling (108), CKY (109) | |
| S15-C finite automata, weighted semirings and composition | partial | part06_programming_languages_go.topics.md › RE2 (112) | Semirings and composition missing |
| S15-D acoustic phonetics and transcription | missing | - | No match; → suggest part19 |
| S15-D waveform, framing and pre-emphasis | partial | part03_mathematics.topics.md › STFT (signals and sequences) | Pre-emphasis not named |
| S15-D spectrogram, mel and MFCC | covered | part19_machine_learning.topics.md › audio and speech (128) | |
| S15-D pronunciation lexicon | missing | - | No match; → suggest part19 |
| S15-D language-model interface | covered | part20_generative_ai_1of3.topics.md › n-grams (17) | |
| S15-D HMM, noisy channel and Viterbi | covered | part19_machine_learning.topics.md › sequence labelling (108), noisy channel (106) | |
| S15-D GMM and HMM-DNN | partial | part19_machine_learning.topics.md › unsupervised and anomaly (58) | HMM-DNN not named |
| S15-D CTC | partial | part28_ml_case_studies_4of5.topics.md › Dropbox OCR (46) | Case-study mention only |
| S15-D end-to-end encoder-decoder speech models | covered | part20_generative_ai_1of3.topics.md › architectures (27) | Whisper named |
| S15-D Conformer and self-supervised speech representations | missing | - | No match beyond Whisper in part20 line 27; → suggest part19 |
| S15-D WFST and decoding | missing | - | No match; → suggest part19 |
| S15-D WER and CER | covered | part19_machine_learning.topics.md › audio and speech (128) | |
| S15-D streaming latency, noise, accents and multilingual evaluation | partial | part19_machine_learning.topics.md › audio and speech (128) | Not named |
| S15-D TTS and spoken dialog | missing | - | No match; → suggest part19 |
| S16 tensor contracts and autodiff | partial | part19_machine_learning.topics.md › deep learning (77-96), backprop (83); part22_generative_ai_3of3.topics.md › autodiff exercise (161) | |
| S16 perceptron and linear units | covered | part19_machine_learning.topics.md › perceptron and XOR (79) | |
| S16 MLP and backprop | covered | part19_machine_learning.topics.md › backprop (83) | |
| S16 initialization, activations and numerical stability | covered | part19_machine_learning.topics.md › activations (80), initialization (90), vanishing gradients (84) | |
| S16 regularization and generalization | covered | part19_machine_learning.topics.md › regularization (91) | |
| S16 optimizer and learning-rate diagnostics | covered | part19_machine_learning.topics.md › optimizers (85), LR schedules (86), loss curves (89) | |
| S16 CNNs and residual blocks | partial | part19_machine_learning.topics.md › CNN (92) | Residual CNN blocks not named |
| S16 sequence batching and masking | partial | part19_machine_learning.topics.md › batch size (88) | Masking named for transformers only |
| S16 RNN, BPTT, LSTM and GRU | partial | part19_machine_learning.topics.md › RNN, LSTM and BPTT (93, 95) | GRU not named |
| S16 encoder-decoder and beam search | covered | part19_machine_learning.topics.md › encoder-decoder (93); part20_generative_ai_1of3.topics.md › decoding (36-40) | |
| S16 attention from similarity | covered | part20_generative_ai_1of3.topics.md › attention (19-20) | |
| S16 multi-head self-attention | covered | part20_generative_ai_1of3.topics.md › multi-head (22) | |
| S16 positional schemes and masking | covered | part20_generative_ai_1of3.topics.md › positional (23), causal mask (24) | |
| S16 encoder-only, decoder-only and encoder-decoder transformers | covered | part20_generative_ai_1of3.topics.md › architectures (27) | |
| S16 pretraining objectives | partial | part20_generative_ai_1of3.topics.md › architectures (27) | Objectives not named |
| S16 distributed-compute and memory intuition | missing | - | No match; → suggest part19 |
| S16 data parallelism | partial | part02_computer_organization.topics.md › SIMD and GPUs (74) | Hardware level only |
## 5.6.3 Detailed S17 Learning Order

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| S17 autoregressive factorization, logits, softmax, likelihood and cross-entropy | covered | part20_generative_ai_1of3.topics.md › autoregressive loop (26); part19_machine_learning.topics.md › losses (81) | |
| S17 greedy, beam, temperature, top-k and top-p decoding | covered | part20_generative_ai_1of3.topics.md › decoding (36-40) | |
| S17 repetition controls | partial | part20_generative_ai_1of3.topics.md › decoding (36-40) | Not named |
| S17 context windows, KV cache and quantization | covered | part20_generative_ai_1of3.topics.md › context window (28), KV cache (29), quantization (78) | |
| S17 batching and cost equations | partial | part22_generative_ai_3of3.topics.md › token cost (57) | Batching not named |
| S17 diffusion and classifier-free guidance | covered | part20_generative_ai_1of3.topics.md › diffusion (131) | |
| S17 instruction hierarchy, delimiters and data/instruction separation | covered | part21_generative_ai_2of3.topics.md › prompt engineering (78) | |
| S17 zero-shot and few-shot prompting | covered | part21_generative_ai_2of3.topics.md › prompt engineering (78) | |
| S17 self-consistency | covered | part21_generative_ai_2of3.topics.md › reasoning techniques (81) | |
| S17 structured outputs and constrained decoding | covered | part21_generative_ai_2of3.topics.md › output handling (94) | |
| S17 tool schemas and validation | covered | part21_generative_ai_2of3.topics.md › tool loop (98), output handling (94) | |
| S17 prompt and dataset versioning with regression tests | covered | part21_generative_ai_2of3.topics.md › prompt optimization (86-90) | |
| S17 corpus and access contract | partial | part21_generative_ai_2of3.topics.md › permissions at retrieval (34) | |
| S17 document parsing and deduplication | partial | part21_generative_ai_2of3.topics.md › document parsing (11-14) | Deduplication not named |
| S17 chunking and metadata | covered | part21_generative_ai_2of3.topics.md › chunking (15-20) | |
| S17 lexical baseline | covered | part20_generative_ai_1of3.topics.md › BM25 (139) | |
| S17 dense bi-encoder retrieval | covered | part20_generative_ai_1of3.topics.md › bi-encoders (146) | |
| S17 exact vector search | partial | part20_generative_ai_1of3.topics.md › IVF (152), HNSW (154) | Exact baseline not named |
| S17 ANN recall, latency and memory trade-offs | covered | part20_generative_ai_1of3.topics.md › IVF (152), PQ (153), HNSW (154) | |
| S17 hybrid fusion | covered | part20_generative_ai_1of3.topics.md › RRF (140) | |
| S17 cross-encoder reranking | covered | part20_generative_ai_1of3.topics.md › cross-encoders (146) | |
| S17 context packing and citation | covered | part21_generative_ai_2of3.topics.md › citations and provenance (25-27) | |
| S17 grounded generation | covered | part21_generative_ai_2of3.topics.md › multimodal RAG generation (42) | |
| S17 recall@k, MRR and NDCG | partial | part19_machine_learning.topics.md › nDCG (65) | Recall@k and MRR not named |
| S17 context precision and recall | covered | part21_generative_ai_2of3.topics.md › RAG evaluation (46) | |
| S17 faithfulness and answer relevance | covered | part21_generative_ai_2of3.topics.md › RAG evaluation (46) | |
| S17 citation accuracy | covered | part21_generative_ai_2of3.topics.md › citations and provenance (26-27) | |
| S17 abstention | partial | part21_generative_ai_2of3.topics.md › generation (42) | "Not found" response only |
| S17 LLM judges calibrated against human labels | covered | part22_generative_ai_3of3.topics.md › LLM-judge (117-121) | |
| S17 RLHF | covered | part20_generative_ai_1of3.topics.md › alignment (42) | |
| S17 reward modeling | partial | part20_generative_ai_1of3.topics.md › alignment (42) | Not named |
| S17 DPO | missing | - | Not found; → suggest part20 |
| S17 SFT, LoRA and QLoRA | covered | part20_generative_ai_1of3.topics.md › fine-tuning (49-80), LoRA (66), QLoRA (67) | |
| S17 catastrophic forgetting and contamination | covered | part20_generative_ai_1of3.topics.md › catastrophic forgetting (54-60); multimodal benchmarks contamination (120) | |
| S17 contrastive image-text representations (CLIP) | covered | part20_generative_ai_1of3.topics.md › CLIP and InfoNCE (88-93) | |
| S17 VLM connectors and cross-attention | covered | part20_generative_ai_1of3.topics.md › LLaVA (94-100), cross-attention (21) | |
| S17 caption, VQA and retrieval | covered | part20_generative_ai_1of3.topics.md › benchmarks (120) | |
| S17 multimodal evaluation | partial | part20_generative_ai_1of3.topics.md › benchmarks (120) | |
| S17 augmented LLM, chaining, routing and parallelization | covered | part22_generative_ai_3of3.topics.md › workflow patterns (14), workflow vs agent (12) | |
| S17 orchestrator-worker and evaluator-optimizer | covered | part22_generative_ai_3of3.topics.md › multi-agent systems (53-73), reflection (20) | |
| S17 state and memory | covered | part22_generative_ai_3of3.topics.md › LangGraph memory (35-39) | |
| S17 checkpointing and human approval | covered | part22_generative_ai_3of3.topics.md › checkpointers and interrupts (31) | |
| S17 bounded agent loops and budgets | covered | part22_generative_ai_3of3.topics.md › bounding the loop (64), token cost (57) | |
| S17 least privilege and per-action authorization | covered | part22_generative_ai_3of3.topics.md › security (94-104), least privilege (97) | |
| S17 idempotency | covered | part22_generative_ai_3of3.topics.md › reliability (47-52) | |
| S17 prompt injection and excessive agency | covered | part14_security.topics.md › AI/LLM threats (225-245), prompt injection (229), excessive agency (238) | |
| S17 sensitive disclosure, supply chain and misinformation | partial | part14_security.topics.md › AI/LLM threats (225-245) | Misinformation not named |
| S17 data and model poisoning | covered | part14_security.topics.md › poisoning (240) | |
| S17 improper output handling | partial | part14_security.topics.md › AI/LLM threats (225-245) | Output handling not named |
| S17 system-prompt leakage | partial | part14_security.topics.md › AI/LLM threats (225-245) | Not named |
| S17 vector and embedding weaknesses | partial | part14_security.topics.md › AI/LLM threats (225-245) | Not named |
| S17 unbounded consumption | covered | part14_security.topics.md › economic DoS (138) | |
| S17 NIST Govern-Map-Measure-Manage | missing | - | No match; → suggest part14 |
## 5.7 S18-S24: Services, Security, Architecture, Operations, and Integration

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| S18 RFC 9110 resources, methods, status codes and content negotiation | covered | part09_networking.topics.md › HTTP semantics (70-78) | |
| S18 caching and validators | partial | part09_networking.topics.md › HTTP semantics (70-78) | Validators named; caching not detailed |
| S18 conditional requests and ETag/If-Match lost-update tests | partial | part09_networking.topics.md › HTTP semantics (74); part11_software_architecture.topics.md › ETag exercise (192) | If-Match not named; lost updates only in part12 (112) |
| S18 Retry-After and back-pressure | covered | part09_networking.topics.md › overload signals (73) | |
| S18 safe, idempotent and retry behaviour | covered | part09_networking.topics.md › idempotency keys (73); part11_software_architecture.topics.md › API design (30-52) | |
| S18 malformed and ambiguous framing | missing | - | No HTTP request-smuggling match; → suggest part09 |
| S18 resource-oriented REST | covered | part11_software_architecture.topics.md › API design (30-52) | |
| S18 protobuf field presence, numbers, unknown fields and reservations | covered | part06_programming_languages_go.topics.md › protobuf (198-205) | |
| S18 compatibility matrices | partial | part06_programming_languages_go.topics.md › protobuf (198-205) | Not named |
| S18 gRPC unary, server, client and bidirectional streams | covered | part06_programming_languages_go.topics.md › gRPC (198-205) | |
| S18 deadlines and cancellation | covered | part06_programming_languages_go.topics.md › context (147-151), grpc-timeout (203) | |
| S18 gRPC metadata and status | partial | part06_programming_languages_go.topics.md › protobuf and gRPC (198-205) | |
| S19 passwords, sessions and tokens | covered | part14_security.topics.md › authentication and sessions (94-109) | |
| S19 AAL1, AAL2 and AAL3 | missing | - | No match; → suggest part14 |
| S19 phishing and replay resistance | partial | part14_security.topics.md › MFA (106) | Phishing-resistant WebAuthn named; replay not named |
| S19 authenticator binding, recovery and invalidation | partial | part14_security.topics.md › account recovery (107) | Binding and invalidation not named |
| S19 syncable passkey trade-offs | partial | part14_security.topics.md › MFA (106) | Passkeys named; syncable trade-offs not |
| S19 OAuth redirect mismatch and open redirect | covered | part14_security.topics.md › OAuth (101), open redirects (152) | |
| S19 code and access-token injection | partial | part14_security.topics.md › OAuth (101) | Not named |
| S19 mix-up attacks | covered | part14_security.topics.md › OAuth (101) | |
| S19 referer and history leakage | partial | part14_security.topics.md › web app (142-157) | Not named |
| S19 PKCE downgrade | partial | part14_security.topics.md › OAuth (101) | PKCE named; downgrade not |
| S19 counterfeit resource server | missing | - | No match; → suggest part14 |
| S19 refresh-token replay and rotation | missing | - | No match; → suggest part14 |
| S19 unsafe 307 redirects | missing | - | No match; → suggest part14 |
| S19 untrusted proxy headers | partial | part14_security.topics.md › web app (142-157) | Header injection only |
| S19 OWASP ASVS 5.0 | missing | - | No match; → suggest part14 |
| S19 CSRF and CORS | covered | part14_security.topics.md › CSRF (99), CORS (144-145) | |
| S19 JWT | covered | part14_security.topics.md › JWT pitfalls (100), JWT exercise (274) | |
| S19 secrets management | partial | part14_security.topics.md › engineering checklist (92) | Not a full topic |
| S19 SSRF | covered | part14_security.topics.md › OWASP Top 10:2025 (157) | |
| S19 fuzz and race evidence | covered | part06_programming_languages_go.topics.md › fuzzing (171-177) | |
| S20 quality attributes and SLOs | covered | part11_software_architecture.topics.md › quality attributes (152-158); part18_devops_sre.topics.md › SRE (106-117) | |
| S20 boundaries and data ownership | covered | part11_software_architecture.topics.md › DDD (127-133) | |
| S20 LLD cohesion and coupling | partial | part11_software_architecture.topics.md › OO (54-60) | Coupling not named |
| S20 SOLID | covered | part11_software_architecture.topics.md › SOLID (64-69) | |
| S20 clean architecture | covered | part11_software_architecture.topics.md › application architecture (117-125) | |
| S20 modular monolith | partial | part11_software_architecture.topics.md › application architecture (117-125) | Not named |
| S20 synchronous and asynchronous communication | covered | part11_software_architecture.topics.md › distributed patterns (135-140) | |
| S20 retries, timeouts, idempotency and backpressure | covered | part06_programming_languages_go.topics.md › retries (164); part09_networking.topics.md › overload (73) | |
| S20 cache and queue semantics | covered | part13_distributed_systems.topics.md › caching (72-79), async (81-87) | |
| S20 replication, partitioning and consistency | covered | part13_distributed_systems.topics.md › replication (39-47), partitioning (56-62) | |
| S20 leader election and consensus | covered | part13_distributed_systems.topics.md › consensus (30-37), Raft (34) | |
| S20 transactions, outbox and saga | covered | part13_distributed_systems.topics.md › distributed transactions (64-70), sagas (68), outbox (70) | |
| S20 observability and operations | covered | part18_devops_sre.topics.md › observability (96-104) | |
| S20 microservice split decisions | partial | part11_software_architecture.topics.md › distributed patterns (135-140) | Not named |
| S20 MapReduce | covered | part13_distributed_systems.topics.md › dataflow (91-92) | MapReduce and job patterns named |
| S20 linearizable KV service | partial | part13_distributed_systems.topics.md › consistency (foundations 7-28) | Linearizability not named |
| S20 sharded KV | partial | part13_distributed_systems.topics.md › partitioning (56-62) | |
| S20 failure injection | covered | part13_distributed_systems.topics.md › testing (107-111) | Jepsen |
| S20 SLO and error budget | covered | part18_devops_sre.topics.md › error budgets (109) | |
| S20 overload and cascading failure | partial | part18_devops_sre.topics.md › SRE (106-117) | Not named |
| S20 recovery evidence | covered | part12_databases.topics.md › recovery (118-130) | |
| S21 requirements and quality clarification | partial | part11_software_architecture.topics.md › fundamentals (7-28) | |
| S21 capacity and load estimation | covered | part03_mathematics.topics.md › queueing and Fermi estimation (93-110) | |
| S21 bottleneck analysis | partial | part03_mathematics.topics.md › queueing (93-110) | Not named |
| S21 failure modes and availability | covered | part13_distributed_systems.topics.md › availability (49-54) | |
| S21 abuse cases | covered | part14_security.topics.md › API abuse (119-128) | |
| S21 observability and rollout | covered | part18_devops_sre.topics.md › CI/CD (65-77), observability (96-104) | |
| S21 multi-tenant systems | partial | part16_cloud_core.topics.md › resource management (63-68) | Not named |
| S21 ML-backed systems | covered | part19_machine_learning.topics.md › MLOps (197-214) | |
| S21 adversarial systems | covered | part14_security.topics.md › AI/LLM threats (225-245) | |
| S22 decide whether ML is warranted | partial | part19_machine_learning.topics.md › foundations of AI (7-11) | |
| S22 metric and non-ML baseline | partial | part19_machine_learning.topics.md › evaluation (60-67) | Baseline not named |
| S22 data, label and feature contracts | covered | part19_machine_learning.topics.md › feature engineering (68-72), data platforms (201) | |
| S22 reproducible experiments and lineage | covered | part19_machine_learning.topics.md › experimentation (206), training pipelines (202) | |
| S22 registry and promotion | partial | part19_machine_learning.topics.md › MLOps (197-214) | Registry not named |
| S22 batch, online and streaming serving | covered | part19_machine_learning.topics.md › serving (205) | |
| S22 training-serving parity | partial | part19_machine_learning.topics.md › serving (205) | Not named |
| S22 automated data, model and infrastructure tests | covered | part19_machine_learning.topics.md › ML Test Score (203) | |
| S22 shadow, canary and A/B | covered | part19_machine_learning.topics.md › experimentation (206); part18_devops_sre.topics.md › CI/CD (65-77) | |
| S22 drift, skew and freshness monitoring | covered | part19_machine_learning.topics.md › drift (207-211) | |
| S22 retraining policy | partial | part19_machine_learning.topics.md › MLOps (197-214) | |
| S22 rollback and incident drill | covered | part18_devops_sre.topics.md › CI/CD (65-77); part14_security.topics.md › incident response (216-223) | |
| S22 governance and decommissioning | covered | part19_machine_learning.topics.md › governance (212); part22_generative_ai_3of3.topics.md › deprecation (142) | |
| S22 code, data and model as independent change axes | partial | part19_machine_learning.topics.md › MLOps (197-214) | |
| S22 GenAI corpus, prompt, model and tool versions | covered | part21_generative_ai_2of3.topics.md › prompt versions (94); part22_generative_ai_3of3.topics.md › LLMOps (130-149) | |
| S22 PMLE-style design, build, operationalize and govern | partial | part19_machine_learning.topics.md › MLOps (197-214) | PMLE not named |
| S23 Nasiko control plane: gateway, backend, auth, router, registry and chat history | out of scope | - | Nasiko-specific capstone |
| S23 Nasiko orchestrator, worker, CLI and A2A agents | out of scope | - | Nasiko-specific capstone |
| S23 Nasiko P0-P10 phases and operational-readiness review | out of scope | - | Nasiko-specific capstone |
| S24 game and rendering specializations | out of scope | - | ARCHIVE |
| S24 medical specialization | out of scope | - | ARCHIVE |
| S24 mechanical and aerospace specializations | out of scope | - | ARCHIVE |
| S24 deep pure mathematics and extra number theory | out of scope | - | ARCHIVE |
| S24 unrelated web stacks | out of scope | - | ARCHIVE |

## Missing in this range

- S0 environment variables (→ suggest part05) — from: 5.2 S0-S4: Computing, Language, and Reasoning Foundations
- S9 multiple integrals and vector-calculus intuition (→ suggest part03) — from: 5.3 S5-S10: Mathematical and Algorithmic Core
- S10 sufficiency (→ suggest part03) — from: 5.3 S5-S10: Mathematical and Algorithmic Core
- S14 proximal methods (→ suggest part03) — from: 5.4 S11-S14: Classical ML, Databases, Optimization, RL, and Causality
- S14 robust and stochastic formulations (→ suggest part03) — from: 5.4 S11-S14: Classical ML, Databases, Optimization, RL, and Causality
- S14 non-convex diagnostics (→ suggest part03) — from: 5.4 S11-S14: Classical ML, Databases, Optimization, RL, and Causality
- S14 SCMs (→ suggest part19) — from: 5.4 S11-S14: Classical ML, Databases, Optimization, RL, and Causality
- S14 frontdoor adjustment (→ suggest part19) — from: 5.4 S11-S14: Classical ML, Databases, Optimization, RL, and Causality
- S14 overlap (→ suggest part19) — from: 5.4 S11-S14: Classical ML, Databases, Optimization, RL, and Causality
- S14 sensitivity analysis (→ suggest part19) — from: 5.4 S11-S14: Classical ML, Databases, Optimization, RL, and Causality
- S14 regression discontinuity (→ suggest part19) — from: 5.4 S11-S14: Classical ML, Databases, Optimization, RL, and Causality
- S15-A Laplace and z-transform (→ suggest part03) — from: 5.5 S15-S16: Domain Mathematics and Deep Learning
- S15-A FIR and IIR filters (→ suggest part03) — from: 5.5 S15-S16: Domain Mathematics and Deep Learning
- S15-A pole-zero stability (→ suggest part03) — from: 5.5 S15-S16: Domain Mathematics and Deep Learning
- S15-A filter banks (→ suggest part03) — from: 5.5 S15-S16: Domain Mathematics and Deep Learning
- S15-A multirate processing (→ suggest part03) — from: 5.5 S15-S16: Domain Mathematics and Deep Learning
- S15-A Parseval and reconstruction checks (→ suggest part03) — from: 5.5 S15-S16: Domain Mathematics and Deep Learning
- S15-B restoration and deconvolution (→ suggest part19) — from: 5.5 S15-S16: Domain Mathematics and Deep Learning
- S15-B optical flow (→ suggest part19) — from: 5.5 S15-S16: Domain Mathematics and Deep Learning
- S15-D acoustic phonetics and transcription (→ suggest part19) — from: 5.5 S15-S16: Domain Mathematics and Deep Learning
- S15-D pronunciation lexicon (→ suggest part19) — from: 5.5 S15-S16: Domain Mathematics and Deep Learning
- S15-D Conformer and self-supervised speech representations (→ suggest part20) — from: 5.5 S15-S16: Domain Mathematics and Deep Learning
- S15-D WFST and decoding (→ suggest part19) — from: 5.5 S15-S16: Domain Mathematics and Deep Learning
- S15-D TTS and spoken dialog (→ suggest part19) — from: 5.5 S15-S16: Domain Mathematics and Deep Learning
- S16 distributed-compute and memory intuition (→ suggest part19) — from: 5.5 S15-S16: Domain Mathematics and Deep Learning
- S17 DPO (→ suggest part20) — from: 5.6.3 Detailed S17 Learning Order
- S17 NIST Govern-Map-Measure-Manage (→ suggest part14) — from: 5.6.3 Detailed S17 Learning Order
- S18 malformed and ambiguous framing (→ suggest part09) — from: 5.7 S18-S24: Services, Security, Architecture, Operations, and Integration
- S19 AAL1, AAL2 and AAL3 (→ suggest part14) — from: 5.7 S18-S24: Services, Security, Architecture, Operations, and Integration
- S19 counterfeit resource server (→ suggest part14) — from: 5.7 S18-S24: Services, Security, Architecture, Operations, and Integration
- S19 refresh-token replay and rotation (→ suggest part14) — from: 5.7 S18-S24: Services, Security, Architecture, Operations, and Integration
- S19 unsafe 307 redirects (→ suggest part14) — from: 5.7 S18-S24: Services, Security, Architecture, Operations, and Integration
- S19 OWASP ASVS 5.0 (→ suggest part14) — from: 5.7 S18-S24: Services, Security, Architecture, Operations, and Integration

## Partial in this range

- S0 files versus directories, absolute and relative paths — File system named at heading level; paths not spelled out — part10_operating_systems.topics.md
- S0 process versus program — Processes covered; program/process distinction not stated — part10_operating_systems.topics.md
- S0 ports — Port numbers not confirmed — part09_networking.topics.md
- S0 reproducible repository layout — Builds covered; repo layout not named — part18_devops_sre.topics.md
- S1 pytest — Testing present; pytest not named — part05_programming_languages_python_and_shell.topics.md
- S1 strides, copy versus view — Strides and copy/view aliasing not named — part05_programming_languages_python_and_shell.topics.md
- S1 seeded generators — "random routines" only — part05_programming_languages_python_and_shell.topics.md
- S4 invariants — Named as a proof tool only in passing — part08_data_structures_algorithms.topics.md
- S5 coordinate geometry and distance metrics (Euclidean, Manhattan, cosine) — Coordinate geometry and Manhattan distance not named — part03_mathematics.topics.md
- S5 affine combinations, lines, planes and transformations — Affine not named — part03_mathematics.topics.md
- S7 four fundamental subspaces — Subspaces not named — part03_mathematics.topics.md
- S7 least squares — Not named — part03_mathematics.topics.md
- S7 symmetric and positive-definite matrices — Not named — part03_mathematics.topics.md
- S7 SVD and pseudoinverse — SVD partly covered; pseudoinverse not found — part03_mathematics.topics.md
- S7 condition number — Conditioning named; condition number not — part03_mathematics.topics.md
- S7 QR factorization and Gram-Schmidt — Gram-Schmidt covered; QR not named — part03_mathematics.topics.md
- S8 binary search invariant — Invariant not stated — part08_data_structures_algorithms.topics.md
- S8 strongly connected components — Not named — part08_data_structures_algorithms.topics.md
- S8 MST and greedy exchange — see location — part08_data_structures_algorithms.topics.md
- S9 implicit differentiation — Not named — part03_mathematics.topics.md
- S9 Jacobian and Hessian — Hessian not named — part03_mathematics.topics.md
- S9 definite integral and fundamental theorem — Integration named at heading level — part03_mathematics.topics.md
- S9 integration methods — see location — part03_mathematics.topics.md
- S9 sequences and series — Series not named — part01_school_foundations.topics.md
- S9 floating-point error, conditioning and stability — Conditioning not named — part03_mathematics.topics.md
- S9 roots and interpolation — Root finding not confirmed — part03_mathematics.topics.md
- S9 finite differences — Not named — part03_mathematics.topics.md
- S10 transformations of random variables — Change of variable not named — part03_mathematics.topics.md
- S10 random processes and Markov chains — Entry level only — part03_mathematics.topics.md
- S10 MAP — Case-study mention only — part19_machine_learning.topics.md
- S10 permutation tests — Not named — part03_mathematics.topics.md
- S10 regression diagnostics — see location — part19_machine_learning.topics.md
- S10 experiment design and sequential caveats — A/B testing covered; sequential testing not named — part03_mathematics.topics.md
- S11 problem, label and metric framing with a non-ML baseline — Baseline not named — part19_machine_learning.topics.md
- S11 split strategy, leakage boundary and calibration — Calibration covered; leakage only in passing — part19_machine_learning.topics.md
- S11 GLMs — Not named — part19_machine_learning.topics.md
- S11 LDA and QDA — Not named; LDA appears only as a topic model (111) — part19_machine_learning.topics.md
- S11 margins, kernels and SVM — see location — part19_machine_learning.topics.md
- S11 GMM and EM — Not named — part19_machine_learning.topics.md
- S12 DDL, types and constraints — see location — part12_databases.topics.md
- S12 joins including semi, anti and outer — Semi and anti joins not named — part12_databases.topics.md
- S12 pagination — Not named — part12_databases.topics.md
- S13 pages, tuples, TOAST and catalogs — TOAST not named — part12_databases.topics.md
- S13 buffer manager — Not named — part12_databases.topics.md
- S13 hash, GIN, GiST and BRIN indexes — GIN, GiST and BRIN not named — part12_databases.topics.md
- S13 MVCC, locks and deadlocks — Deadlocks not named — part12_databases.topics.md
- S13 vacuum — Not named — part12_databases.topics.md
- S13 replication and PITR — PITR not named — part13_distributed_systems.topics.md
- S14 convexity — Not named — part03_mathematics.topics.md
- S14 first- and second-order methods — Newton and BFGS not named — part03_mathematics.topics.md
- S14 duality — Not named — part03_mathematics.topics.md
- S14 dynamic programming for RL — Value and policy iteration covered — part19_machine_learning.topics.md
- S14 Monte Carlo methods for RL — RL Monte Carlo not named — part19_machine_learning.topics.md
- S14 backdoor adjustment — Named as DAG adjustment; criterion not stated — part03_mathematics.topics.md
- S15-A signal classes, energy and power — Not named — part03_mathematics.topics.md
- S15-A complex exponentials — Not named — part03_mathematics.topics.md
- S15-A impulse and step — Not named — part03_mathematics.topics.md
- S15-A LTI properties — Not named — part03_mathematics.topics.md
- S15-A frequency response — Not named — part03_mathematics.topics.md
- S15-A Fourier series and transform — DFT and FFT covered; continuous forms not named — part03_mathematics.topics.md
- S15-A sampling and aliasing — Sampling named for images; aliasing not named — part19_machine_learning.topics.md
- S15-A cepstrum and MFCC — MFCC covered; cepstrum not named — part19_machine_learning.topics.md
- S15-A quantization — Image sampling and quantization only — part19_machine_learning.topics.md
- S15-B image formation — Camera geometry covered; image formation not named — part19_machine_learning.topics.md
- S15-B color and gamma — Color named; gamma not named — part19_machine_learning.topics.md
- S15-B point transforms and histograms — see location — part19_machine_learning.topics.md
- S15-B 2D convolution and separable filters — Not named for images — part03_mathematics.topics.md
- S15-B denoising and sharpening — Not named — part03_mathematics.topics.md
- S15-B Fourier image filtering — see location — part03_mathematics.topics.md
- S15-B segmentation — Not named — part19_machine_learning.topics.md
- S15-B reproducibility of image experiments — see location — part19_machine_learning.topics.md
- S15-C regular expressions and finite-state basics — Finite automata not named — part06_programming_languages_go.topics.md
- S15-C sentence splitting — Not named — part19_machine_learning.topics.md
- S15-C n-grams, smoothing and perplexity — Smoothing and perplexity not named — part20_generative_ai_1of3.topics.md
- S15-C WordPiece and unigram tokenization — Not named — part20_generative_ai_1of3.topics.md
- S15-C finite automata, weighted semirings and composition — Semirings and composition missing — part06_programming_languages_go.topics.md
- S15-D waveform, framing and pre-emphasis — Pre-emphasis not named — part03_mathematics.topics.md
- S15-D GMM and HMM-DNN — HMM-DNN not named — part19_machine_learning.topics.md
- S15-D CTC — Case-study mention only — part28_ml_case_studies_4of5.topics.md
- S15-D streaming latency, noise, accents and multilingual evaluation — Not named — part19_machine_learning.topics.md
- S16 tensor contracts and autodiff — see location — part19_machine_learning.topics.md
- S16 CNNs and residual blocks — Residual CNN blocks not named — part19_machine_learning.topics.md
- S16 sequence batching and masking — Masking named for transformers only — part19_machine_learning.topics.md
- S16 RNN, BPTT, LSTM and GRU — GRU not named — part19_machine_learning.topics.md
- S16 pretraining objectives — Objectives not named — part20_generative_ai_1of3.topics.md
- S16 data parallelism — Hardware level only — part02_computer_organization.topics.md
- S17 repetition controls — Not named — part20_generative_ai_1of3.topics.md
- S17 batching and cost equations — Batching not named — part22_generative_ai_3of3.topics.md
- S17 corpus and access contract — see location — part21_generative_ai_2of3.topics.md
- S17 document parsing and deduplication — Deduplication not named — part21_generative_ai_2of3.topics.md
- S17 exact vector search — Exact baseline not named — part20_generative_ai_1of3.topics.md
- S17 recall@k, MRR and NDCG — Recall@k and MRR not named — part19_machine_learning.topics.md
- S17 abstention — "Not found" response only — part21_generative_ai_2of3.topics.md
- S17 reward modeling — Not named — part20_generative_ai_1of3.topics.md
- S17 multimodal evaluation — see location — part20_generative_ai_1of3.topics.md
- S17 sensitive disclosure, supply chain and misinformation — Misinformation not named — part14_security.topics.md
- S17 improper output handling — Output handling not named — part14_security.topics.md
- S17 system-prompt leakage — Not named — part14_security.topics.md
- S17 vector and embedding weaknesses — Not named — part14_security.topics.md
- S18 caching and validators — Validators named; caching not detailed — part09_networking.topics.md
- S18 conditional requests and ETag/If-Match lost-update tests — If-Match not named; lost updates only in part12 (112) — part09_networking.topics.md
- S18 compatibility matrices — Not named — part06_programming_languages_go.topics.md
- S18 gRPC metadata and status — see location — part06_programming_languages_go.topics.md
- S19 phishing and replay resistance — Phishing-resistant WebAuthn named; replay not named — part14_security.topics.md
- S19 authenticator binding, recovery and invalidation — Binding and invalidation not named — part14_security.topics.md
- S19 syncable passkey trade-offs — Passkeys named; syncable trade-offs not — part14_security.topics.md
- S19 code and access-token injection — Not named — part14_security.topics.md
- S19 referer and history leakage — Not named — part14_security.topics.md
- S19 PKCE downgrade — PKCE named; downgrade not — part14_security.topics.md
- S19 untrusted proxy headers — Header injection only — part14_security.topics.md
- S19 secrets management — Not a full topic — part14_security.topics.md
- S20 LLD cohesion and coupling — Coupling not named — part11_software_architecture.topics.md
- S20 modular monolith — Not named — part11_software_architecture.topics.md
- S20 microservice split decisions — Not named — part11_software_architecture.topics.md
- S20 linearizable KV service — Linearizability not named — part13_distributed_systems.topics.md
- S20 sharded KV — see location — part13_distributed_systems.topics.md
- S20 overload and cascading failure — Not named — part18_devops_sre.topics.md
- S21 requirements and quality clarification — see location — part11_software_architecture.topics.md
- S21 bottleneck analysis — Not named — part03_mathematics.topics.md
- S21 multi-tenant systems — Not named — part16_cloud_core.topics.md
- S22 decide whether ML is warranted — see location — part19_machine_learning.topics.md
- S22 metric and non-ML baseline — Baseline not named — part19_machine_learning.topics.md
- S22 registry and promotion — Registry not named — part19_machine_learning.topics.md
- S22 training-serving parity — Not named — part19_machine_learning.topics.md
- S22 retraining policy — see location — part19_machine_learning.topics.md
- S22 code, data and model as independent change axes — see location — part19_machine_learning.topics.md
- S22 PMLE-style design, build, operationalize and govern — PMLE not named — part19_machine_learning.topics.md
