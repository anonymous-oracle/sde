# Textbook deconstructions, part 1: topic diff

Source: `gcp/unified-curriculum.md` lines 2116-2489 ("Textbook deconstructions, part 1"), compared with `gcp-lite/index/*.topics.md` and `gcp-lite/Rust_Track_AI_Infrastructure.md`. Each topic appears once, at its first section.

Counts: 331 topics; 118 covered, 72 partial, 140 missing, 1 out of scope.

Status: covered = same concept taught; partial = named only in passing or narrower; missing = not taught; out of scope = Nasiko-specific, ARCHIVE-tagged, or clinical, mechanical or aerospace. Location `→ suggest partNN` marks a missing topic and the index part it would fit.

## Calculus — Michael Spivak

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Field axioms and ordered-field properties | missing | → suggest part03 | Arithmetic is used; the axioms are not taught |
| Number systems: naturals, integers, rationals, reals | partial | index/part01_school_foundations.topics.md:24 | School-level number sets only |
| Functions, graphs and inverse functions | partial | index/part03_mathematics.topics.md:21 | Injections, surjections and bijections only |
| Supremum and least upper bound | missing | → suggest part03 | Not in the index |
| Limits and epsilon-delta continuity | missing | → suggest part03 | Not in the index |
| Derivatives and differentiation rules | partial | index/part03_mathematics.topics.md:130 | Gradients and the first-order Taylor approximation only |
| Mean value theorem | missing | → suggest part03 | Not in the index |
| Taylor's theorem and polynomial approximation | partial | index/part03_mathematics.topics.md:130 | First order only; no remainder term |
| Integrals as accumulated area | partial | index/part03_mathematics.topics.md:131 | Intuition only |
| Fundamental theorem of calculus | missing | → suggest part03 | Not in the index |
| Trigonometric functions | covered | index/part01_school_foundations.topics.md:34 | Sine, cosine and the unit circle at school level |
| Irrationality of π | missing | → suggest part03 | The proof section covers induction only |
| Logarithm and exponential functions | covered | index/part01_school_foundations.topics.md:26 | Log laws, growth and decay |
| Integration in elementary terms | missing | → suggest part03 | Not in the index |
| Planetary motion | out of scope | n/a | Orbital mechanics; an aerospace worked example |
| Infinite sequences and series | partial | index/part03_mathematics.topics.md:24 | Linear recurrences only; convergence is not taught |
| Uniform convergence and power series | missing | → suggest part03 | Not in the index |
| Complex numbers and complex functions | missing | → suggest part03 | Not in the index |
| Construction of the real numbers | missing | → suggest part03 | Not in the index |
| Transcendence of e | missing | → suggest part03 | Not in the index |

## Principles of Mathematical Analysis — Walter Rudin

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Countable and uncountable sets | partial | index/part03_mathematics.topics.md:21 | Cardinality named through bijections only |
| Metric spaces | missing | → suggest part03 | Not in the index |
| Compact and connected sets | missing | → suggest part03 | Not in the index |
| Cauchy sequences, subsequences, limsup and liminf | missing | → suggest part03 | Not in the index |
| Root and ratio tests | missing | → suggest part03 | Not in the index |
| Monotonic functions and discontinuities | missing | → suggest part03 | Not in the index |
| Mean value theorems and L'Hôpital's rule | missing | → suggest part03 | Not in the index |
| Riemann-Stieltjes integral | missing | → suggest part03 | Not in the index |
| Stone-Weierstrass theorem | missing | → suggest part03 | Not in the index |
| Gamma function | missing | → suggest part03 | Not in the index |
| Euclidean spaces | partial | index/part03_mathematics.topics.md:122 | Euclidean distance only |
| Linear maps and multivariable differentiation | partial | index/part03_mathematics.topics.md:117 | Matrices as linear maps; no n-dimensional derivative theory |
| Determinants | partial | index/part03_mathematics.topics.md:118 | The 2 × 2 case (ad − bc) and elimination only |
| Inverse and implicit function theorems | missing | → suggest part03 | Not in the index |
| Fourier series | partial | index/part03_mathematics.topics.md:169 | DFT and FFT only; no convergence theory |
| Lebesgue measure and integration | missing | → suggest part03 | Not in the index |
| Differential forms and Stokes' theorem | missing | → suggest part03 | Not in the index |
| Vector analysis: divergence and curl | missing | → suggest part03 | Not in the index |

## Linear Algebra and Its Applications — Gilbert Strang

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Gaussian elimination and LU factorization | covered | index/part03_mathematics.topics.md:118 | |
| Inverse matrices | covered | index/part03_mathematics.topics.md:118 | |
| Vector spaces, subspaces, basis and dimension | covered | index/part03_mathematics.topics.md:116 | |
| Matrices as linear maps; rank and nullity | covered | index/part03_mathematics.topics.md:117 | |
| Column space and null space | covered | index/part03_mathematics.topics.md:123 | |
| Orthogonality, projections, Gram–Schmidt and least squares | covered | index/part03_mathematics.topics.md:119 | |
| Eigenvalues and eigenvectors | covered | index/part03_mathematics.topics.md:120 | |
| Diagonalization and powers A^k | partial | index/part03_mathematics.topics.md:120 | Eigenvalues and power iteration only; diagonalization not named |
| Difference and differential equations (e^{At}) | partial | index/part03_mathematics.topics.md:132 | First-order ODEs by Euler and RK4; no matrix exponential |
| Complex matrices and similarity transformations | missing | → suggest part03 | Not in the index |
| Positive definite matrices and minima | missing | → suggest part03 | Not in the index |
| Singular value decomposition | covered | index/part03_mathematics.topics.md:121 | |
| Linear programming and game theory | covered | index/part03_mathematics.topics.md:143 | Game theory also at index/part19_machine_learning.topics.md:132 |
| Computations with matrices (QR, iterative methods) | partial | index/part03_mathematics.topics.md:118 | LU only |
| Jordan form and Lyapunov stability (appendices) | missing | → suggest part03 | Not in the index |

## Introduction to Linear Algebra — Gilbert Strang (5e)

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Vectors, dot products and lengths | partial | index/part03_mathematics.topics.md:122 | Norms and cosine similarity only |
| Transposes and permutation matrices | partial | index/part03_mathematics.topics.md:182 | Transposes appear only in a Go exercise |

## Probability Theory: The Logic of Science — E.T. Jaynes

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Plausible reasoning and Cox's desiderata | missing | → suggest part03 | Not in the index |
| Product rule and Bayes' theorem | covered | index/part03_mathematics.topics.md:46 | Derived from the definition of conditional probability |
| Kolmogorov axioms | partial | index/part03_mathematics.topics.md:46 | Assumed, not named |
| Binomial distribution and sampling with or without replacement | covered | index/part03_mathematics.topics.md:51 | |
| Prior probabilities and Bayesian updating | covered | index/part03_mathematics.topics.md:77 | |
| Jeffreys and ignorance priors | missing | → suggest part03 | Not in the index |
| Maximum-entropy distributions | missing | → suggest part03 | Entropy is covered at line 158; maximum-entropy classifiers at part19 line 108 are a different idea |
| Shannon's source-coding bound | covered | index/part03_mathematics.topics.md:161 | |
| Decision theory: Bayes risk and loss functions | partial | index/part17_architects_practice.topics.md:18 | Expected utility only |
| Paradoxes of probability (Borel–Kolmogorov) | missing | → suggest part03 | Not in the index |
| Unbiased estimators and sampling variance | covered | index/part03_mathematics.topics.md:75 | |
| Rule of succession and exchangeable sequences | missing | → suggest part03 | Not in the index |
| Model comparison and Bayes factors | missing | → suggest part19 | Not in the index |
| Gaussian derivations and the central limit theorem | covered | index/part03_mathematics.topics.md:59 | The theorem is stated; derivations are not |
| Fisher information | partial | index/part03_mathematics.topics.md:75 | Named; sufficiency and information bounds are not taught |

## All of Statistics — Larry Wasserman

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Sample spaces, random variables and distributions | covered | index/part03_mathematics.topics.md:46 | |
| Expectation and variance | covered | index/part03_mathematics.topics.md:47 | |
| Inequalities (Markov, Chebyshev, Chernoff) | covered | index/part03_mathematics.topics.md:58 | |
| Convergence in probability and almost surely | partial | index/part03_mathematics.topics.md:59 | Laws of large numbers; the almost-sure mode is not named |
| Stochastic processes and Markov chains | covered | index/part03_mathematics.topics.md:68 | |
| Maximum-likelihood estimation | covered | index/part03_mathematics.topics.md:75 | |
| Delta method | missing | → suggest part03 | Not in the index |
| Method of moments | missing | → suggest part03 | Not in the index |
| Confidence intervals | partial | index/part03_mathematics.topics.md:187 | Bootstrap intervals in a project exercise only |
| Hypothesis testing and p-values | covered | index/part03_mathematics.topics.md:80 | |
| Bootstrap and jackknife | covered | index/part03_mathematics.topics.md:78 | |
| Parametric bootstrap | partial | index/part03_mathematics.topics.md:78 | Nonparametric bootstrap only |
| Multiparameter models and exponential families | missing | → suggest part03 | Not in the index |
| Sufficiency | missing | → suggest part03 | Not in the index |
| Nonparametric and curve estimation | partial | index/part19_machine_learning.topics.md:171 | Exponential smoothing for time series only |
| Graphical exploratory data analysis | partial | index/part03_mathematics.topics.md:85 | Quantiles from histograms |
| Classification and data mining | covered | index/part19_machine_learning.topics.md:57 | |

## Statistical Inference — Casella & Berger

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Transformations of random variables | missing | → suggest part03 | Not in the index |
| Student's t and F distributions | missing | → suggest part03 | Not in the index |
| Order statistics | partial | index/part03_mathematics.topics.md:57 | Named alongside tail bounds |
| Basu's theorem and complete sufficient statistics | missing | → suggest part03 | Not in the index |
| ANOVA | missing | → suggest part03 | Not in the index |
| Robust regression and errors-in-variables | missing | → suggest part19 | Not in the index |
| Least squares and regression | covered | index/part19_machine_learning.topics.md:54 | |
| Logistic regression | covered | index/part19_machine_learning.topics.md:218 | Built from scratch in Go |

## Introduction to Algorithms — CLRS

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Asymptotic notation (O, Ω, Θ) | covered | index/part08_data_structures_algorithms.topics.md:16 | |
| Insertion sort | covered | index/part08_data_structures_algorithms.topics.md:11 | |
| Divide-and-conquer and the master theorem | covered | index/part08_data_structures_algorithms.topics.md:19 | |
| Strassen matrix multiplication | missing | → suggest part08 | Not in the index |
| Akra–Bazzi method | missing | → suggest part08 | Not in the index |
| Randomized algorithms and expected-time analysis | covered | index/part08_data_structures_algorithms.topics.md:54 | |
| Heapsort and priority queues | covered | index/part08_data_structures_algorithms.topics.md:46 | |
| Quicksort | covered | index/part08_data_structures_algorithms.topics.md:54 | |
| Counting sort and radix sort | covered | index/part08_data_structures_algorithms.topics.md:21 | |
| Bucket sort | missing | → suggest part08 | Not in the index |
| Medians and order statistics | covered | index/part08_data_structures_algorithms.topics.md:62 | |
| Hash tables with open addressing | covered | index/part08_data_structures_algorithms.topics.md:36 | |
| Binary search trees | covered | index/part08_data_structures_algorithms.topics.md:44 | |
| Red-black trees | covered | index/part08_data_structures_algorithms.topics.md:44 | Balanced trees named; red-black or AVL |
| B-trees | partial | index/part12_databases.topics.md:180 | Database context only; no B-tree algorithm in part08 |
| Disjoint sets (union-find) | covered | index/part08_data_structures_algorithms.topics.md:113 | |
| Dynamic programming | covered | index/part08_data_structures_algorithms.topics.md:80 | |
| Greedy algorithms | covered | index/part08_data_structures_algorithms.topics.md:78 | |
| Amortized analysis | covered | index/part08_data_structures_algorithms.topics.md:16 | |
| Graph representations and traversals | covered | index/part08_data_structures_algorithms.topics.md:115 | |
| Minimum spanning trees (Prim, Kruskal) | covered | index/part08_data_structures_algorithms.topics.md:72 | |
| Shortest paths (Bellman-Ford, Dijkstra) | covered | index/part08_data_structures_algorithms.topics.md:71 | |
| All-pairs shortest paths (Floyd-Warshall) | missing | → suggest part08 | Not in the index |
| Maximum flow | covered | index/part08_data_structures_algorithms.topics.md:73 | Ford–Fulkerson and min-cut |
| Bipartite matching | partial | index/part03_mathematics.topics.md:143 | Assignment problem and the Hungarian method |
| Number-theoretic algorithms (GCD, CRT) | covered | index/part03_mathematics.topics.md:30 | |
| RSA | covered | index/part03_mathematics.topics.md:32 | |
| Primality testing | missing | → suggest part03 | Not in the index |
| Approximation algorithms (vertex cover, subset sum) | partial | index/part08_data_structures_algorithms.topics.md:94 | NP-completeness only |
| Traveling salesman and set cover | missing | → suggest part08 | Not in the index |
| Counting, probability and binomial tails | covered | index/part03_mathematics.topics.md:51 | |

## Optimization by Vector Space Methods — Luenberger

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Hilbert space | missing | → suggest part03 | Not in the index |
| Hahn-Banach and dual spaces | missing | → suggest part03 | Not in the index |
| Least-squares estimation | covered | index/part03_mathematics.topics.md:119 | |
| Linear operators and adjoints | partial | index/part03_mathematics.topics.md:117 | Matrices as linear maps only |
| Constrained optimization and Lagrange multipliers | covered | index/part03_mathematics.topics.md:142 | |
| Kuhn-Tucker conditions | covered | index/part03_mathematics.topics.md:142 | Named as KKT |
| Pontryagin maximum principle | missing | → suggest part03 | Not in the index |
| Newton's method | missing | → suggest part03 | Not in the index |
| Steepest descent and gradient descent | covered | index/part03_mathematics.topics.md:139 | |
| Conjugate gradient | missing | → suggest part03 | Not in the index |
| Convex optimization | covered | index/part03_mathematics.topics.md:138 | |
| Projection methods and successive approximation | missing | → suggest part03 | Not in the index |

## Advanced Engineering Mathematics — Kreyszig

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| First-order ODEs | covered | index/part03_mathematics.topics.md:132 | Euler and RK4 |
| Second-order linear ODEs | missing | → suggest part03 | Not in the index |
| Laplace transform | missing | → suggest part03 | Not in the index |
| Frobenius series and Bessel functions | missing | → suggest part03 | Not in the index |
| Vector calculus: gradient, divergence and curl | partial | index/part03_mathematics.topics.md:130 | Gradient only |
| Partial differential equations | missing | → suggest part03 | Not in the index |
| Complex analysis: Cauchy's theorem and residues | missing | → suggest part03 | Not in the index |
| Numerics for ODEs and PDEs | partial | index/part03_mathematics.topics.md:132 | Euler and RK4 only; no PDE numerics |

## Digital Signal Processing — Proakis & Manolakis

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Signals, systems and their classification | partial | index/part03_mathematics.topics.md:165 | Section heading "Signals and sequences" only |
| Convolution and LTI systems | partial | index/part03_mathematics.topics.md:192 | Convolution in a project exercise only |
| The z-transform | missing | → suggest part03 | Not in the index |
| Frequency analysis, DFT and FFT | covered | index/part03_mathematics.topics.md:169 | |
| Short-time Fourier transform and spectrograms | covered | index/part03_mathematics.topics.md:169 | |
| Sampling and reconstruction | partial | index/part19_machine_learning.topics.md:138 | Image sampling only |
| Quantization and fixed-point effects | missing | → suggest part03 | Image quantization only (index/part19_machine_learning.topics.md:138) |
| Correlation and spectra | partial | index/part03_mathematics.topics.md:91 | Correlation matrix and Pearson only |
| FIR and IIR filter design | missing | → suggest part03 | Not in the index |
| Goertzel and chirp-z transforms | missing | → suggest part03 | Not in the index |
| Multirate filter banks and wavelets | missing | → suggest part03 | Not in the index |

## Digital Communications — Proakis & Salehi

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Channel models and channel capacity | partial | index/part03_mathematics.topics.md:163 | Channel capacity only |
| Modulation: PAM, PSK, QAM | missing | → suggest part03 | Not in the index |
| Optimum receivers in AWGN | missing | → suggest part03 | Not in the index |
| Carrier and symbol synchronization (PLL) | missing | → suggest part03 | Not in the index |
| Rate distortion | missing | → suggest part03 | Not in the index |
| Linear block codes and trellis codes | partial | index/part08_data_structures_algorithms.topics.md:98 | Viterbi-style shortest path only; no error-correcting codes |
| Adaptive equalization | missing | → suggest part03 | Not in the index |
| Spread spectrum and OFDM | missing | → suggest part03 | Not in the index |
| MIMO and multiple antennas | missing | → suggest part03 | Not in the index |
| Multiuser communications | missing | → suggest part03 | Not in the index |
| Fading channels (Rayleigh, Ricean) | missing | → suggest part03 | Not in the index |

## Understanding Digital Signal Processing — Lyons

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Periodic sampling and aliasing | missing | → suggest part03 | Not in the index |
| Leakage, windowing and scalloping | partial | index/part03_mathematics.topics.md:169 | Windowing named only |
| Radix-2 FFT and bit reversal | partial | index/part03_mathematics.topics.md:169 | FFT named only |
| Quadrature signals and the Hilbert transform | missing | → suggest part03 | Not in the index |
| Sample-rate conversion and polyphase filters | missing | → suggest part03 | Not in the index |
| Signal averaging | missing | → suggest part03 | Not in the index |
| DSP tricks (CIC filters, frequency translation) | missing | → suggest part03 | Not in the index |

## Signals and Systems — Oppenheim & Willsky

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Continuous-time Fourier series and transform | partial | index/part03_mathematics.topics.md:169 | Discrete-time DFT only |
| Linear feedback systems | missing | → suggest part03 | Not in the index |

## Linear Systems and Signals — B.P. Lathi

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Partial fractions and Cramer's rule | missing | → suggest part03 | Not in the index |
| State-space analysis of LTI systems | missing | → suggest part03 | Not in the index |
| Stability and BIBO stability | missing | → suggest part03 | Not in the index |
| Impulse response and convolution | partial | index/part03_mathematics.topics.md:192 | Convolution in a project exercise only |
| Discrete-time signal analysis (DTFS, DTFT) | partial | index/part03_mathematics.topics.md:169 | DFT only |

## Discrete-Time Signal Processing — Oppenheim & Schafer

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Parametric signal modeling (LPC) | missing | → suggest part03 | Not in the index |

## Spoken Language Processing — Huang, Acero, Hon

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Hidden Markov models and Viterbi decoding | covered | index/part19_machine_learning.topics.md:108 | |
| Phonetics and phonology | missing | → suggest part19 | Not in the index |
| Baum-Welch training | partial | index/part19_machine_learning.topics.md:108 | Named in the HMM sequence-labelling line only |
| Speech signal representations (MFCC, cepstrum, formants) | partial | index/part03_mathematics.topics.md:170 | MFCC only |
| Speech coding (PCM, mu-law, CELP) | missing | → suggest part19 | Not in the index |
| Acoustic modeling and speaker adaptation | missing | → suggest part19 | Not in the index |
| Language modeling (n-grams, smoothing) | covered | index/part20_generative_ai_1of3.topics.md:17 | |
| Perplexity | covered | index/part03_mathematics.topics.md:172 | |
| Viterbi beam search and A* | partial | index/part19_machine_learning.topics.md:20 | A* in informed search; not speech decoding |
| Environmental robustness and noise | missing | → suggest part19 | Not in the index |
| Text normalization and letter-to-sound | missing | → suggest part19 | Not in the index |
| Prosody and speech synthesis | missing | → suggest part19 | Not in the index |
| Spoken language understanding and dialogue | missing | → suggest part19 | Not in the index |

## Elements of Information Theory — Cover & Thomas

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Asymptotic equipartition property | missing | → suggest part03 | Not in the index |
| Entropy rates of stochastic processes | missing | → suggest part03 | Not in the index |
| Data compression and the Kraft inequality | partial | index/part03_mathematics.topics.md:161 | Shannon bound and Huffman codes only |
| Gambling and portfolio theory (Kelly) | partial | index/part30_supplementary_applied_domains.topics.md:12 | Mean-variance portfolio theory only; Kelly not named |
| Differential entropy and the Gaussian channel | missing | → suggest part03 | Not in the index |
| Universal source coding and Lempel-Ziv | missing | → suggest part08 | Not in the index |
| Kolmogorov complexity | missing | → suggest part08 | Not in the index |
| Network information theory | missing | → suggest part03 | Not in the index |
| Inequalities in information theory | partial | index/part03_mathematics.topics.md:159 | KL divergence only |

## Pattern Recognition and Machine Learning — Bishop

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Polynomial curve fitting and linear regression | covered | index/part19_machine_learning.topics.md:54 | |
| Linear models for classification | covered | index/part19_machine_learning.topics.md:56 | |
| Neural networks | covered | index/part19_machine_learning.topics.md:85 | |
| Kernel methods and support vector machines | covered | index/part19_machine_learning.topics.md:56 | |
| Graphical models | covered | index/part19_machine_learning.topics.md:33 | |
| Mixture models and EM | covered | index/part19_machine_learning.topics.md:58 | |
| Approximate inference and sampling | covered | index/part19_machine_learning.topics.md:34 | |
| Continuous latent variables (PCA) | covered | index/part03_mathematics.topics.md:121 | |
| Sequential data (HMMs) | covered | index/part19_machine_learning.topics.md:36 | |
| Combining models: boosting and bagging | covered | index/part19_machine_learning.topics.md:57 | |
| Variational inference | partial | index/part20_generative_ai_1of3.topics.md:125 | Named within the VAE ELBO only |

## Pattern Classification — Duda, Hart, Stork

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Nonparametric methods (nearest neighbours, Parzen) | covered | index/part19_machine_learning.topics.md:56 | |
| Stochastic methods (simulated annealing) | partial | index/part19_machine_learning.topics.md:21 | Named in local search only |
| Nonmetric methods (decision trees) | covered | index/part19_machine_learning.topics.md:57 | |
| Unsupervised learning and clustering | covered | index/part19_machine_learning.topics.md:58 | |

## The Elements of Statistical Learning — Hastie et al.

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Bias–variance trade-off | partial | index/part03_mathematics.topics.md:75 | Bias and variance of estimators only |
| Basis expansions and regularization | partial | index/part19_machine_learning.topics.md:91 | Regularization in deep networks; ridge and lasso not named |
| Kernel smoothing | missing | → suggest part19 | Not in the index |
| Model assessment and cross-validation | partial | index/part19_machine_learning.topics.md:52 | Hoeffding generalization bound; cross-validation not explicit |
| Spectral clustering | missing | → suggest part19 | Not in the index |
| Random forests and ensembles | covered | index/part19_machine_learning.topics.md:57 | |
| High-dimensional problems and FDR | covered | index/part03_mathematics.topics.md:82 | |
| Undirected graphical models | missing | → suggest part19 | Not in the index |

## Deep Learning — Goodfellow et al.

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Numerical computation (conditioning, overflow) | partial | index/part03_mathematics.topics.md:185 | Finite-difference gradient checks only |
| Convolutional networks | covered | index/part19_machine_learning.topics.md:92 | |
| Sequence modeling: recurrent networks | missing | → suggest part19 | Not in the index |
| Optimization for training (SGD, Adam) | covered | index/part19_machine_learning.topics.md:85 | |
| Autoencoders | partial | index/part20_generative_ai_1of3.topics.md:125 | Within the VAE only |
| Representation learning and embeddings | partial | index/part19_machine_learning.topics.md:103 | Dense word embeddings only |
| Partition function | missing | → suggest part19 | Not in the index |
| Monte Carlo methods | covered | index/part03_mathematics.topics.md:53 | |
| Batch normalization | partial | index/part19_machine_learning.topics.md:218 | Named in a Go project only |
| Deep generative models | covered | index/part20_generative_ai_1of3.topics.md:124 | |

## Artificial Intelligence: A Modern Approach — Russell & Norvig

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Intelligent agents | covered | part19_machine_learning.topics.md › Classical AI: search, knowledge and reasoning | Rational agents, PEAS and agent types |
| Informed and uninformed search | covered | index/part19_machine_learning.topics.md:20 | |
| Adversarial search (minimax, alpha-beta) | covered | index/part19_machine_learning.topics.md:23 | |
| Constraint satisfaction problems | covered | index/part19_machine_learning.topics.md:24 | |
| Propositional logic and SAT | covered | index/part19_machine_learning.topics.md:27 | |
| First-order logic and inference | covered | index/part19_machine_learning.topics.md:28 | |
| Knowledge representation | covered | index/part19_machine_learning.topics.md:29 | |
| Automated planning (STRIPS) | covered | index/part19_machine_learning.topics.md:30 | |
| Quantifying uncertainty and Bayesian networks | covered | index/part19_machine_learning.topics.md:33 | |
| Reasoning over time: Kalman filters | missing | → suggest part19 | Hidden Markov models are covered at line 36; Kalman filters are not |
| Decisions and utility | partial | index/part17_architects_practice.topics.md:18 | Expected utility only |
| Multiagent decisions and game theory | covered | index/part19_machine_learning.topics.md:132 | |
| Probabilistic programming | missing | → suggest part19 | Not in the index |
| Reinforcement learning | covered | index/part19_machine_learning.topics.md:134 | |
| Natural language processing | covered | index/part19_machine_learning.topics.md:98 | |
| Robotics | missing | → suggest part19 | Not in the index |
| Computer vision | covered | index/part19_machine_learning.topics.md:127 | |
| Ethics and safety of AI | covered | index/part19_machine_learning.topics.md:39 | |

## Foundations of Statistical Natural Language Processing — Manning & Schütze

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Collocations | missing | → suggest part19 | Not in the index |
| Word sense disambiguation | covered | index/part19_machine_learning.topics.md:110 | |
| Corpus work and tokenization | covered | index/part20_generative_ai_1of3.topics.md:15 | |
| Markov models and part-of-speech tagging | covered | index/part19_machine_learning.topics.md:108 | |
| Probabilistic CFGs and parsing | covered | index/part19_machine_learning.topics.md:109 | |
| Statistical alignment and machine translation | missing | → suggest part20 | Encoder-decoder architectures are covered at index/part20_generative_ai_1of3.topics.md:27; MT is not named |
| Topics in information retrieval (LSA, LDA) | covered | index/part19_machine_learning.topics.md:111 | |
| Text categorization | missing | → suggest part19 | Not in the index as a topic |

## Automatic Speech Recognition: A Deep Learning Approach — Yu & Deng

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Automatic speech recognition pipeline | partial | index/part19_machine_learning.topics.md:128 | MFCCs and word error rate only |
| DNN–HMM hybrid systems | missing | → suggest part19 | Not in the index |
| CTC and sequence-discriminative training | missing | → suggest part19 | Not in the index |
| Speech feature learning and transfer | missing | → suggest part19 | Not in the index |

## Speech and Language Processing — Jurafsky & Martin

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Text classification (Naive Bayes, sentiment) | partial | index/part03_mathematics.topics.md:186 | Naive Bayes in a project exercise only |
| Vector semantics and embeddings | covered | index/part19_machine_learning.topics.md:103 | |
| Neural networks and transformers | covered | index/part20_generative_ai_1of3.topics.md:27 | |
| Large language models and post-training | covered | index/part20_generative_ai_1of3.topics.md:42 | |
| Masked language models (BERT) | covered | index/part20_generative_ai_1of3.topics.md:31 | |
| Information retrieval and RAG | covered | index/part21_generative_ai_2of3.topics.md:33 | |
| Sequence labeling (POS, NER, CRF) | covered | index/part19_machine_learning.topics.md:108 | |
| Dependency parsing | covered | index/part19_machine_learning.topics.md:109 | Constituency and CKY covered; dependency grammar named |
| Information extraction | covered | index/part19_machine_learning.topics.md:112 | |
| Coreference and entity linking | partial | index/part19_machine_learning.topics.md:112 | Entity linking only; coreference is not named |
| Discourse coherence (RST, PDTB) | missing | → suggest part19 | Not in the index |
| Semantic role labeling | missing | → suggest part19 | Not in the index |
| Kneser-Ney smoothing | missing | → suggest part20 | Smoothing is named at index/part20_generative_ai_1of3.topics.md:17 without Kneser-Ney |

## Game Engine Architecture — Jason Gregory

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Game loop and engine runtime architecture | missing | → suggest part30 | No game or graphics part in the index |
| Entity-component object models | missing | → suggest part30 | Not in the index |
| Lock-free and parallel programming | covered | index/part06_programming_languages_go.topics.md:158 | |
| SIMD and data parallelism | covered | index/part02_computer_organization.topics.md:74 | |
| 3D math: vectors and matrices | partial | index/part03_mathematics.topics.md:122 | Vectors and norms; quaternions missing |
| Animation (skeletal) | missing | → suggest part30 | Not in the index |
| Collision detection and rigid-body dynamics | missing | → suggest part30 | Not in the index |
| Audio systems | missing | → suggest part30 | Not in the index |
| Scripting | partial | index/part05_programming_languages_python_and_shell.topics.md:44 | Bash scripting only |
| Input devices and game timing | missing | → suggest part30 | Not in the index |
| Memory management for engines | missing | → suggest part02 | Not in the index |

## Real-Time Rendering — Akenine-Möller et al.

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Graphics pipeline | missing | → suggest part30 | No graphics part in the index |
| Shading and BRDFs | missing | → suggest part30 | Not in the index |
| Texturing and mipmaps | missing | → suggest part30 | Not in the index |
| Shadow maps | missing | → suggest part30 | Not in the index |
| Physically based rendering | missing | → suggest part30 | Not in the index |
| Global illumination | missing | → suggest part30 | Not in the index |
| Image-space effects (tone mapping, depth of field, motion blur) | missing | → suggest part30 | Not in the index |
| Ray tracing and BVH acceleration | missing | → suggest part30 | Not in the index |
| Level of detail and culling | missing | → suggest part30 | Not in the index |
| Virtual and augmented reality | missing | → suggest part30 | Not in the index |
| Curves and splines | missing | → suggest part30 | Not in the index |
| Transforms and matrix pipelines | partial | index/part03_mathematics.topics.md:117 | Matrices as linear maps only |

## ICSE / Selina Concise (Classes 6–10)

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Place value, factors and BODMAS | covered | index/part01_school_foundations.topics.md | School-level arithmetic |
| Fractions, decimals and percentages | covered | index/part01_school_foundations.topics.md | School-level arithmetic |
| Ratio, proportion and the unitary method | covered | index/part01_school_foundations.topics.md | School-level |
| Simple and compound interest | partial | index/part01_school_foundations.topics.md:27 | Exponential growth only; no interest arithmetic |
| Linear equations and inequalities | covered | index/part01_school_foundations.topics.md | School-level algebra |
| Lines, angles and triangles | covered | index/part01_school_foundations.topics.md:31 | Geometry section |
| Pythagoras' theorem | covered | index/part01_school_foundations.topics.md:31 | Geometry section |
| Mensuration (area and volume) | partial | index/part01_school_foundations.topics.md:31 | Geometry section only |
| Data handling and graphical statistics | partial | index/part03_mathematics.topics.md:85 | Quantiles from histograms only |
| Probability (school level) | covered | index/part03_mathematics.topics.md:46 | |
| Trigonometric ratios and heights and distances | covered | index/part01_school_foundations.topics.md:34 | |
| Sets (roster and set-builder notation) | partial | index/part03_mathematics.topics.md:21 | Functions as sets only |
| Speed, distance and time | missing | → suggest part01 | Not in the index |
| Logarithms in school algebra | covered | index/part01_school_foundations.topics.md:26 | |

## Understanding ICSE Mathematics — M.L. Aggarwal (Class 10)

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| VAT and GST (CGST, SGST, IGST, ITC) | missing | → suggest part30 | Not in the index |
| Recurring deposits and loan amortization | missing | → suggest part30 | Not in the index |
| Shares and dividends | partial | index/part30_supplementary_applied_domains.topics.md:16 | Dividend theory only; no share arithmetic |
| Linear inequations | partial | index/part01_school_foundations.topics.md | School-level inequalities |
| Nature of roots of quadratics | missing | → suggest part01 | Not in the index |
| Factor and remainder theorems | missing | → suggest part03 | Not in the index |
| Ratio, proportion and componendo–dividendo | missing | → suggest part01 | Not in the index |
| Matrices: order, types and transpose | partial | index/part03_mathematics.topics.md:117 | Matrices as linear maps only |
| Arithmetic and geometric progressions | covered | index/part01_school_foundations.topics.md:29 | |
| Coordinate geometry: section formula and lines | missing | → suggest part01 | Not in the index |
| Circles and tangents | missing | → suggest part01 | Not in the index |
| Loci and constructions | missing | → suggest part01 | Not in the index |
| Measures of central tendency | partial | index/part03_mathematics.topics.md:85 | Quantiles only |

## Missing in this range

- Field axioms and ordered-field properties (Calculus — Michael Spivak)
- Supremum and least upper bound (Calculus — Michael Spivak)
- Limits and epsilon-delta continuity (Calculus — Michael Spivak)
- Mean value theorem (Calculus — Michael Spivak)
- Fundamental theorem of calculus (Calculus — Michael Spivak)
- Irrationality of π (Calculus — Michael Spivak)
- Integration in elementary terms (Calculus — Michael Spivak)
- Uniform convergence and power series (Calculus — Michael Spivak)
- Complex numbers and complex functions (Calculus — Michael Spivak)
- Construction of the real numbers (Calculus — Michael Spivak)
- Transcendence of e (Calculus — Michael Spivak)
- Metric spaces (Principles of Mathematical Analysis — Walter Rudin)
- Compact and connected sets (Principles of Mathematical Analysis — Walter Rudin)
- Cauchy sequences, subsequences, limsup and liminf (Principles of Mathematical Analysis — Walter Rudin)
- Root and ratio tests (Principles of Mathematical Analysis — Walter Rudin)
- Monotonic functions and discontinuities (Principles of Mathematical Analysis — Walter Rudin)
- Mean value theorems and L'Hôpital's rule (Principles of Mathematical Analysis — Walter Rudin)
- Riemann-Stieltjes integral (Principles of Mathematical Analysis — Walter Rudin)
- Stone-Weierstrass theorem (Principles of Mathematical Analysis — Walter Rudin)
- Gamma function (Principles of Mathematical Analysis — Walter Rudin)
- Inverse and implicit function theorems (Principles of Mathematical Analysis — Walter Rudin)
- Lebesgue measure and integration (Principles of Mathematical Analysis — Walter Rudin)
- Differential forms and Stokes' theorem (Principles of Mathematical Analysis — Walter Rudin)
- Vector analysis: divergence and curl (Principles of Mathematical Analysis — Walter Rudin)
- Complex matrices and similarity transformations (Linear Algebra and Its Applications — Gilbert Strang)
- Positive definite matrices and minima (Linear Algebra and Its Applications — Gilbert Strang)
- Jordan form and Lyapunov stability (appendices) (Linear Algebra and Its Applications — Gilbert Strang)
- Plausible reasoning and Cox's desiderata (Probability Theory: The Logic of Science — E.T. Jaynes)
- Jeffreys and ignorance priors (Probability Theory: The Logic of Science — E.T. Jaynes)
- Maximum-entropy distributions (Probability Theory: The Logic of Science — E.T. Jaynes)
- Paradoxes of probability (Borel–Kolmogorov) (Probability Theory: The Logic of Science — E.T. Jaynes)
- Rule of succession and exchangeable sequences (Probability Theory: The Logic of Science — E.T. Jaynes)
- Model comparison and Bayes factors (Probability Theory: The Logic of Science — E.T. Jaynes)
- Delta method (All of Statistics — Larry Wasserman)
- Method of moments (All of Statistics — Larry Wasserman)
- Multiparameter models and exponential families (All of Statistics — Larry Wasserman)
- Sufficiency (All of Statistics — Larry Wasserman)
- Transformations of random variables (Statistical Inference — Casella & Berger)
- Student's t and F distributions (Statistical Inference — Casella & Berger)
- Basu's theorem and complete sufficient statistics (Statistical Inference — Casella & Berger)
- ANOVA (Statistical Inference — Casella & Berger)
- Robust regression and errors-in-variables (Statistical Inference — Casella & Berger)
- Strassen matrix multiplication (Introduction to Algorithms — CLRS)
- Akra–Bazzi method (Introduction to Algorithms — CLRS)
- Bucket sort (Introduction to Algorithms — CLRS)
- All-pairs shortest paths (Floyd-Warshall) (Introduction to Algorithms — CLRS)
- Primality testing (Introduction to Algorithms — CLRS)
- Traveling salesman and set cover (Introduction to Algorithms — CLRS)
- Hilbert space (Optimization by Vector Space Methods — Luenberger)
- Hahn-Banach and dual spaces (Optimization by Vector Space Methods — Luenberger)
- Pontryagin maximum principle (Optimization by Vector Space Methods — Luenberger)
- Newton's method (Optimization by Vector Space Methods — Luenberger)
- Conjugate gradient (Optimization by Vector Space Methods — Luenberger)
- Projection methods and successive approximation (Optimization by Vector Space Methods — Luenberger)
- Second-order linear ODEs (Advanced Engineering Mathematics — Kreyszig)
- Laplace transform (Advanced Engineering Mathematics — Kreyszig)
- Frobenius series and Bessel functions (Advanced Engineering Mathematics — Kreyszig)
- Partial differential equations (Advanced Engineering Mathematics — Kreyszig)
- Complex analysis: Cauchy's theorem and residues (Advanced Engineering Mathematics — Kreyszig)
- The z-transform (Digital Signal Processing — Proakis & Manolakis)
- Quantization and fixed-point effects (Digital Signal Processing — Proakis & Manolakis)
- FIR and IIR filter design (Digital Signal Processing — Proakis & Manolakis)
- Goertzel and chirp-z transforms (Digital Signal Processing — Proakis & Manolakis)
- Multirate filter banks and wavelets (Digital Signal Processing — Proakis & Manolakis)
- Modulation: PAM, PSK, QAM (Digital Communications — Proakis & Salehi)
- Optimum receivers in AWGN (Digital Communications — Proakis & Salehi)
- Carrier and symbol synchronization (PLL) (Digital Communications — Proakis & Salehi)
- Rate distortion (Digital Communications — Proakis & Salehi)
- Adaptive equalization (Digital Communications — Proakis & Salehi)
- Spread spectrum and OFDM (Digital Communications — Proakis & Salehi)
- MIMO and multiple antennas (Digital Communications — Proakis & Salehi)
- Multiuser communications (Digital Communications — Proakis & Salehi)
- Fading channels (Rayleigh, Ricean) (Digital Communications — Proakis & Salehi)
- Periodic sampling and aliasing (Understanding Digital Signal Processing — Lyons)
- Quadrature signals and the Hilbert transform (Understanding Digital Signal Processing — Lyons)
- Sample-rate conversion and polyphase filters (Understanding Digital Signal Processing — Lyons)
- Signal averaging (Understanding Digital Signal Processing — Lyons)
- DSP tricks (CIC filters, frequency translation) (Understanding Digital Signal Processing — Lyons)
- Linear feedback systems (Signals and Systems — Oppenheim & Willsky)
- Partial fractions and Cramer's rule (Linear Systems and Signals — B.P. Lathi)
- State-space analysis of LTI systems (Linear Systems and Signals — B.P. Lathi)
- Stability and BIBO stability (Linear Systems and Signals — B.P. Lathi)
- Parametric signal modeling (LPC) (Discrete-Time Signal Processing — Oppenheim & Schafer)
- Phonetics and phonology (Spoken Language Processing — Huang, Acero, Hon)
- Speech coding (PCM, mu-law, CELP) (Spoken Language Processing — Huang, Acero, Hon)
- Acoustic modeling and speaker adaptation (Spoken Language Processing — Huang, Acero, Hon)
- Environmental robustness and noise (Spoken Language Processing — Huang, Acero, Hon)
- Text normalization and letter-to-sound (Spoken Language Processing — Huang, Acero, Hon)
- Prosody and speech synthesis (Spoken Language Processing — Huang, Acero, Hon)
- Spoken language understanding and dialogue (Spoken Language Processing — Huang, Acero, Hon)
- Asymptotic equipartition property (Elements of Information Theory — Cover & Thomas)
- Entropy rates of stochastic processes (Elements of Information Theory — Cover & Thomas)
- Differential entropy and the Gaussian channel (Elements of Information Theory — Cover & Thomas)
- Universal source coding and Lempel-Ziv (Elements of Information Theory — Cover & Thomas)
- Kolmogorov complexity (Elements of Information Theory — Cover & Thomas)
- Network information theory (Elements of Information Theory — Cover & Thomas)
- Kernel smoothing (The Elements of Statistical Learning — Hastie et al.)
- Spectral clustering (The Elements of Statistical Learning — Hastie et al.)
- Undirected graphical models (The Elements of Statistical Learning — Hastie et al.)
- Sequence modeling: recurrent networks (Deep Learning — Goodfellow et al.)
- Partition function (Deep Learning — Goodfellow et al.)
- Reasoning over time: Kalman filters (Artificial Intelligence: A Modern Approach — Russell & Norvig)
- Probabilistic programming (Artificial Intelligence: A Modern Approach — Russell & Norvig)
- Robotics (Artificial Intelligence: A Modern Approach — Russell & Norvig)
- Collocations (Foundations of Statistical Natural Language Processing — Manning & Schütze)
- Statistical alignment and machine translation (Foundations of Statistical Natural Language Processing — Manning & Schütze)
- Text categorization (Foundations of Statistical Natural Language Processing — Manning & Schütze)
- DNN–HMM hybrid systems (Automatic Speech Recognition: A Deep Learning Approach — Yu & Deng)
- CTC and sequence-discriminative training (Automatic Speech Recognition: A Deep Learning Approach — Yu & Deng)
- Speech feature learning and transfer (Automatic Speech Recognition: A Deep Learning Approach — Yu & Deng)
- Discourse coherence (RST, PDTB) (Speech and Language Processing — Jurafsky & Martin)
- Semantic role labeling (Speech and Language Processing — Jurafsky & Martin)
- Kneser-Ney smoothing (Speech and Language Processing — Jurafsky & Martin)
- Game loop and engine runtime architecture (Game Engine Architecture — Jason Gregory)
- Entity-component object models (Game Engine Architecture — Jason Gregory)
- Animation (skeletal) (Game Engine Architecture — Jason Gregory)
- Collision detection and rigid-body dynamics (Game Engine Architecture — Jason Gregory)
- Audio systems (Game Engine Architecture — Jason Gregory)
- Input devices and game timing (Game Engine Architecture — Jason Gregory)
- Memory management for engines (Game Engine Architecture — Jason Gregory)
- Graphics pipeline (Real-Time Rendering — Akenine-Möller et al.)
- Shading and BRDFs (Real-Time Rendering — Akenine-Möller et al.)
- Texturing and mipmaps (Real-Time Rendering — Akenine-Möller et al.)
- Shadow maps (Real-Time Rendering — Akenine-Möller et al.)
- Physically based rendering (Real-Time Rendering — Akenine-Möller et al.)
- Global illumination (Real-Time Rendering — Akenine-Möller et al.)
- Image-space effects (tone mapping, depth of field, motion blur) (Real-Time Rendering — Akenine-Möller et al.)
- Ray tracing and BVH acceleration (Real-Time Rendering — Akenine-Möller et al.)
- Level of detail and culling (Real-Time Rendering — Akenine-Möller et al.)
- Virtual and augmented reality (Real-Time Rendering — Akenine-Möller et al.)
- Curves and splines (Real-Time Rendering — Akenine-Möller et al.)
- Speed, distance and time (ICSE / Selina Concise (Classes 6–10))
- VAT and GST (CGST, SGST, IGST, ITC) (Understanding ICSE Mathematics — M.L. Aggarwal (Class 10))
- Recurring deposits and loan amortization (Understanding ICSE Mathematics — M.L. Aggarwal (Class 10))
- Nature of roots of quadratics (Understanding ICSE Mathematics — M.L. Aggarwal (Class 10))
- Factor and remainder theorems (Understanding ICSE Mathematics — M.L. Aggarwal (Class 10))
- Ratio, proportion and componendo–dividendo (Understanding ICSE Mathematics — M.L. Aggarwal (Class 10))
- Coordinate geometry: section formula and lines (Understanding ICSE Mathematics — M.L. Aggarwal (Class 10))
- Circles and tangents (Understanding ICSE Mathematics — M.L. Aggarwal (Class 10))
- Loci and constructions (Understanding ICSE Mathematics — M.L. Aggarwal (Class 10))

## Partial in this range

- Number systems: naturals, integers, rationals, reals (Calculus — Michael Spivak)
- Functions, graphs and inverse functions (Calculus — Michael Spivak)
- Derivatives and differentiation rules (Calculus — Michael Spivak)
- Taylor's theorem and polynomial approximation (Calculus — Michael Spivak)
- Integrals as accumulated area (Calculus — Michael Spivak)
- Infinite sequences and series (Calculus — Michael Spivak)
- Countable and uncountable sets (Principles of Mathematical Analysis — Walter Rudin)
- Euclidean spaces (Principles of Mathematical Analysis — Walter Rudin)
- Linear maps and multivariable differentiation (Principles of Mathematical Analysis — Walter Rudin)
- Determinants (Principles of Mathematical Analysis — Walter Rudin)
- Fourier series (Principles of Mathematical Analysis — Walter Rudin)
- Diagonalization and powers A^k (Linear Algebra and Its Applications — Gilbert Strang)
- Difference and differential equations (e^{At}) (Linear Algebra and Its Applications — Gilbert Strang)
- Computations with matrices (QR, iterative methods) (Linear Algebra and Its Applications — Gilbert Strang)
- Vectors, dot products and lengths (Introduction to Linear Algebra — Gilbert Strang (5e))
- Transposes and permutation matrices (Introduction to Linear Algebra — Gilbert Strang (5e))
- Kolmogorov axioms (Probability Theory: The Logic of Science — E.T. Jaynes)
- Decision theory: Bayes risk and loss functions (Probability Theory: The Logic of Science — E.T. Jaynes)
- Fisher information (Probability Theory: The Logic of Science — E.T. Jaynes)
- Convergence in probability and almost surely (All of Statistics — Larry Wasserman)
- Confidence intervals (All of Statistics — Larry Wasserman)
- Parametric bootstrap (All of Statistics — Larry Wasserman)
- Nonparametric and curve estimation (All of Statistics — Larry Wasserman)
- Graphical exploratory data analysis (All of Statistics — Larry Wasserman)
- Order statistics (Statistical Inference — Casella & Berger)
- B-trees (Introduction to Algorithms — CLRS)
- Bipartite matching (Introduction to Algorithms — CLRS)
- Approximation algorithms (vertex cover, subset sum) (Introduction to Algorithms — CLRS)
- Linear operators and adjoints (Optimization by Vector Space Methods — Luenberger)
- Vector calculus: gradient, divergence and curl (Advanced Engineering Mathematics — Kreyszig)
- Numerics for ODEs and PDEs (Advanced Engineering Mathematics — Kreyszig)
- Signals, systems and their classification (Digital Signal Processing — Proakis & Manolakis)
- Convolution and LTI systems (Digital Signal Processing — Proakis & Manolakis)
- Sampling and reconstruction (Digital Signal Processing — Proakis & Manolakis)
- Correlation and spectra (Digital Signal Processing — Proakis & Manolakis)
- Channel models and channel capacity (Digital Communications — Proakis & Salehi)
- Linear block codes and trellis codes (Digital Communications — Proakis & Salehi)
- Leakage, windowing and scalloping (Understanding Digital Signal Processing — Lyons)
- Radix-2 FFT and bit reversal (Understanding Digital Signal Processing — Lyons)
- Continuous-time Fourier series and transform (Signals and Systems — Oppenheim & Willsky)
- Impulse response and convolution (Linear Systems and Signals — B.P. Lathi)
- Discrete-time signal analysis (DTFS, DTFT) (Linear Systems and Signals — B.P. Lathi)
- Baum-Welch training (Spoken Language Processing — Huang, Acero, Hon)
- Speech signal representations (MFCC, cepstrum, formants) (Spoken Language Processing — Huang, Acero, Hon)
- Viterbi beam search and A* (Spoken Language Processing — Huang, Acero, Hon)
- Data compression and the Kraft inequality (Elements of Information Theory — Cover & Thomas)
- Gambling and portfolio theory (Kelly) (Elements of Information Theory — Cover & Thomas)
- Inequalities in information theory (Elements of Information Theory — Cover & Thomas)
- Variational inference (Pattern Recognition and Machine Learning — Bishop)
- Stochastic methods (simulated annealing) (Pattern Classification — Duda, Hart, Stork)
- Bias–variance trade-off (The Elements of Statistical Learning — Hastie et al.)
- Basis expansions and regularization (The Elements of Statistical Learning — Hastie et al.)
- Model assessment and cross-validation (The Elements of Statistical Learning — Hastie et al.)
- Numerical computation (conditioning, overflow) (Deep Learning — Goodfellow et al.)
- Autoencoders (Deep Learning — Goodfellow et al.)
- Representation learning and embeddings (Deep Learning — Goodfellow et al.)
- Batch normalization (Deep Learning — Goodfellow et al.)
- Decisions and utility (Artificial Intelligence: A Modern Approach — Russell & Norvig)
- Automatic speech recognition pipeline (Automatic Speech Recognition: A Deep Learning Approach — Yu & Deng)
- Text classification (Naive Bayes, sentiment) (Speech and Language Processing — Jurafsky & Martin)
- Coreference and entity linking (Speech and Language Processing — Jurafsky & Martin)
- 3D math: vectors and matrices (Game Engine Architecture — Jason Gregory)
- Scripting (Game Engine Architecture — Jason Gregory)
- Transforms and matrix pipelines (Real-Time Rendering — Akenine-Möller et al.)
- Simple and compound interest (ICSE / Selina Concise (Classes 6–10))
- Mensuration (area and volume) (ICSE / Selina Concise (Classes 6–10))
- Data handling and graphical statistics (ICSE / Selina Concise (Classes 6–10))
- Sets (roster and set-builder notation) (ICSE / Selina Concise (Classes 6–10))
- Shares and dividends (Understanding ICSE Mathematics — M.L. Aggarwal (Class 10))
- Linear inequations (Understanding ICSE Mathematics — M.L. Aggarwal (Class 10))
- Matrices: order, types and transpose (Understanding ICSE Mathematics — M.L. Aggarwal (Class 10))
- Measures of central tendency (Understanding ICSE Mathematics — M.L. Aggarwal (Class 10))
