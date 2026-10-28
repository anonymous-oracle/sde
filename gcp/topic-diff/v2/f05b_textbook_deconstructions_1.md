# Topic diff: Textbook deconstructions, part 1

Source: `gcp/unified-curriculum.md` lines 2116–2489 (section 2, "Textbook deconstructions", through the ICSE Aggarwal table)
Counts: covered 326 · partial 121 · missing 36 · out of scope 14 (total 497)

Method: case-insensitive searches over `gcp-lite/index/*.topics.md` and `gcp-lite/Rust_Track_AI_Infrastructure.md`. A hit counts only after its line is read. Locations give the topic file and nearest `###` heading, with line numbers in the Note column. `part01_school_foundations.topics.md` has no `###` headings, so its rows give the line number instead. Topics repeated across the range get one row, at first appearance. Statuses marked "judgment" rest on heading-level reading, not a named hit.

## Calculus — Michael Spivak

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Basic properties of numbers (field axioms, order) | covered | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Field axioms and ordered-field properties (line 48) |
| Numbers of various sorts (naturals, integers, rationals, reals) | partial | part01_school_foundations.topics.md:8 | Number system named; the sorts are not separated (judgment) |
| Functions and graphs | covered | part01_school_foundations.topics.md:30 | Function notation, domain and range (line 30) |
| Polar coordinates | partial | part03b_analysis_calculus_and_number_theory.topics.md — Coordinate geometry and conics | Polar forms of lines and conics only (lines 34, 41) |
| Conic sections | covered | part03b_analysis_calculus_and_number_theory.topics.md — Coordinate geometry and conics | Conics named (line 34) |
| Limits and continuity | covered | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Epsilon-delta limits and continuity (line 50) |
| Three hard theorems (IVT, EVT, MVT) | partial | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Rolle and mean value theorems (line 57); IVT and EVT not checked by name |
| Least upper bounds | covered | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Supremum and completeness axiom (line 49) |
| Uniform continuity | partial | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Uniform convergence named (line 56); uniform continuity not checked by name |
| Derivatives and differentiation | covered | part03b_analysis_calculus_and_number_theory.topics.md — Calculus and differential equations | Derivative rules in the calculus section (judgment) |
| Convexity and concavity | partial | part03_mathematics.topics.md — Calculus and optimization | Convex optimization named; convexity of functions not checked by name (judgment) |
| Inverse functions | covered | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Inverse and implicit function theorems (line 59) |
| Parametric curves | covered | part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering | Parametric curves and splines (line 55) |
| Riemann sums and integrals | covered | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Riemann and Riemann–Stieltjes integration (line 60) |
| Fundamental theorem of calculus | covered | part03b_analysis_calculus_and_number_theory.topics.md — Calculus and differential equations | Named (line 19) |
| Integration in elementary terms | partial | part03b_analysis_calculus_and_number_theory.topics.md — Calculus and differential equations | Definite integrals and techniques (line 18); no elementary-function theory |
| Trigonometric functions | partial | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Not checked by name in the analysis section (judgment) |
| π is irrational | covered | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Irrationality proofs (line 62) |
| Logarithm and exponential functions | partial | part03b_analysis_calculus_and_number_theory.topics.md — Complex and functional analysis | Holomorphic and log only in complex functions (line 67) |
| Planetary motion | out of scope | - | Application example, not a topic |
| Cosmopolitan integral (appendix) | out of scope | - | Appendix example |
| Approximation by polynomial functions (Taylor) | covered | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Taylor theorem (line 57) |
| e is transcendental | covered | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Transcendence proofs (line 62) |
| Infinite sequences | covered | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Bounded and monotone sequences (line 55) |
| Infinite series | covered | part03b_analysis_calculus_and_number_theory.topics.md — Calculus and differential equations | Absolute and conditional convergence (lines 20, 22) |
| Uniform convergence and power series | covered | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Pointwise versus uniform convergence (line 56) |
| Complex numbers | covered | part03b_analysis_calculus_and_number_theory.topics.md — Complex and functional analysis | Complex functions and holomorphy (line 67) |
| Complex functions | covered | part03b_analysis_calculus_and_number_theory.topics.md — Complex and functional analysis | Cauchy theory, conformal geometry (lines 67) |
| Complex power series | partial | part03b_analysis_calculus_and_number_theory.topics.md — Complex and functional analysis | Power series in the real case only |
| Fields | covered | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Field axioms (line 48) |
| Construction of the real numbers | covered | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Dedekind cuts (line 47) |
| Uniqueness of the real numbers | missing | → suggest part03 | No hit for uniqueness of the reals |
| Answers, glossary, suggested reading | out of scope | - | Back matter |

## Principles of Mathematical Analysis — Walter Rudin

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Ordered sets and fields | covered | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Field axioms (line 48) |
| Extended real number system | partial | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Infinite limits only (judgment) |
| The complex field | covered | part03b_analysis_calculus_and_number_theory.topics.md — Complex and functional analysis | Line 67 |
| Euclidean spaces | covered | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Metric spaces (line 53) |
| Countable and uncountable sets | missing | → suggest part03 | No hit for countability |
| Metric spaces | covered | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Metric axioms (line 53) |
| Compact sets | partial | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Compactness not checked by name (judgment) |
| Perfect and connected sets | missing | → suggest part03b | No hit for perfect or connected sets |
| Convergent and Cauchy sequences | covered | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Completeness (line 49) |
| Summation by parts | missing | → suggest part03b | No hit |
| Cauchy product and rearrangements of series | missing | → suggest part03b | No Cauchy product; rearrangement only in part04 Inequalities (line 27) |
| Root and ratio tests | partial | part03b_analysis_calculus_and_number_theory.topics.md — Calculus and differential equations | Series convergence named; tests not checked by name |
| Limits of functions and continuous functions | covered | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Line 50 |
| Continuity and compactness / connectedness | partial | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Continuity covered; the compactness and connectedness theorems not checked by name |
| Monotonic functions | partial | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Monotone sequences and convergence (lines 55, 61) |
| Mean value theorems | covered | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Line 57 |
| L'Hôpital's rule | partial | part03b_analysis_calculus_and_number_theory.topics.md — Calculus and differential equations | Not checked by name (judgment) |
| Taylor's theorem | covered | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Line 57 |
| Riemann–Stieltjes integral | covered | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Line 60 |
| Rectifiable curves | missing | → suggest part03b | No hit |
| Uniform convergence and continuity / integration | covered | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Line 56 |
| Equicontinuous families | missing | → suggest part03b | No hit |
| Stone–Weierstrass theorem | covered | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Line 58 |
| Fourier series | covered | part03c_signals_systems_and_communications.topics.md — Transforms and system analysis | Line 25 |
| The gamma function | missing | → suggest part03b | No hit |
| Algebraic completeness of the complex field | partial | part03b_analysis_calculus_and_number_theory.topics.md — Complex and functional analysis | Complex functions only (judgment) |
| Linear transformations (several variables) | partial | part03_mathematics.topics.md — Linear algebra | Matrices as linear maps (line 144) |
| Differentiation in several variables | partial | part03b_analysis_calculus_and_number_theory.topics.md — Calculus and differential equations | Jacobian and gradient not checked by name (judgment) |
| Contraction principle | covered | part03_mathematics.topics.md — Numerical computing | Successive approximation and contraction (line 196) |
| Inverse and implicit function theorems | covered | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Line 59 |
| Rank theorem | partial | part03_mathematics.topics.md — Linear algebra | Rank–nullity theorem (line 144) |
| Determinants | covered | part03_mathematics.topics.md — Linear algebra | Line 145 |
| Differentiation of integrals | missing | → suggest part03b | No hit |
| Stokes' theorem | covered | part03b_analysis_calculus_and_number_theory.topics.md — Calculus and differential equations | Differential forms and Stokes (line 25) |
| Partitions of unity | missing | → suggest part03b | No hit |
| Change of variables | partial | part03b_analysis_calculus_and_number_theory.topics.md — Calculus and differential equations | Not checked by name (judgment) |
| Closed and exact forms | partial | part03b_analysis_calculus_and_number_theory.topics.md — Calculus and differential equations | Differential forms named (line 25) |
| Lebesgue measure and integration | covered | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Line 61 |
| Measurable functions | partial | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Lebesgue integration named (line 61) |
| L² functions | covered | part03b_analysis_calculus_and_number_theory.topics.md — Complex and functional analysis | Hilbert spaces (line 69) |
| End-of-chapter exercises, bibliography, symbols | out of scope | - | Back matter |

## Linear Algebra and Its Applications — Gilbert Strang

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Matrices and Gaussian elimination | covered | part03_mathematics.topics.md — Linear algebra | Line 145 |
| Vector spaces and subspaces | covered | part03_mathematics.topics.md — Linear algebra | Line 143 |
| Linear independence, basis, dimension | covered | part03_mathematics.topics.md — Linear algebra | Line 143 |
| Orthogonality | covered | part03_mathematics.topics.md — Linear algebra | Projections and least squares (line 146) |
| Determinants | covered | part03_mathematics.topics.md — Linear algebra | Line 145 |
| Eigenvalues and eigenvectors | covered | part03_mathematics.topics.md — Linear algebra | Line 147 |
| Diagonalization | covered | part03_mathematics.topics.md — Linear algebra | Line 153 |
| Difference equations and powers A^k | covered | part03_mathematics.topics.md — Linear algebra | Linear recurrences (line 24) |
| Differential equations and e^{At} | covered | part03_mathematics.topics.md — Linear algebra | Matrix exponential (line 154) |
| Complex matrices | partial | part03_mathematics.topics.md — Linear algebra | Hermitian and unitary not checked by name |
| Similarity transformations | partial | part03_mathematics.topics.md — Linear algebra | Not checked by name (judgment) |
| Positive definite matrices | covered | part03_mathematics.topics.md — Linear algebra | Line 152 |
| Computations with matrices | covered | part03_mathematics.topics.md — Linear algebra | LU and QR (lines 145, 155) |
| Linear programming and game theory | covered | part03_mathematics.topics.md — Calculus and optimization | Line 176; game theory in part19 Specialised learning areas |
| Lorentz group | out of scope | - | Appendix |
| Compactness criterion for finite dimensionality | out of scope | - | Appendix |
| Characterization of commutators | out of scope | - | Appendix |
| Liapunov stability | covered | part03_mathematics.topics.md — Linear algebra | Jordan form and Lyapunov stability (line 154) |
| Jordan canonical form | covered | part03_mathematics.topics.md — Linear algebra | Line 154 |
| Halmos' conjecture (Pearcy's proof) | out of scope | - | Research-level appendix |

## Introduction to Linear Algebra — Gilbert Strang (5e)

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Vectors, linear combinations and dot products | covered | part03_mathematics.topics.md — Linear algebra | Line 143 |
| Elimination and LU factorization | covered | part03_mathematics.topics.md — Linear algebra | Line 145 |
| Matrix operations and transposes | partial | part03_mathematics.topics.md — Linear algebra | Transposes named in matrix rows (judgment) |
| Inverse matrices | missing | → suggest part03 | No hit for matrix inverse |
| Permutations | partial | part03_mathematics.topics.md — Linear algebra | Not checked by name (judgment) |
| Vector spaces and subspaces | covered | part03_mathematics.topics.md — Linear algebra | Line 143 |
| Orthogonality | covered | part03_mathematics.topics.md — Linear algebra | Line 146 |
| Determinants | covered | part03_mathematics.topics.md — Linear algebra | Line 145 |
| Eigenvalues and eigenvectors | covered | part03_mathematics.topics.md — Linear algebra | Line 147 |
| Singular value decomposition | covered | part03_mathematics.topics.md — Linear algebra | Line 148 |
| Linear transformations | partial | part03_mathematics.topics.md — Linear algebra | Matrices as linear maps (line 144); no change-of-basis rows |
| Complex vectors and matrices | partial | part03_mathematics.topics.md — Linear algebra | Not checked by name (judgment) |
| Applications | out of scope | - | Generic applications list |

## Probability Theory: The Logic of Science — E.T. Jaynes

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Deductive and plausible reasoning | covered | part03_mathematics.topics.md — Probability | Cox's desiderata (line 74) |
| Product rule and sum rule | covered | part03_mathematics.topics.md — Probability | Lines 22, 74 |
| Kolmogorov axioms | partial | part03_mathematics.topics.md — Probability | Axioms not checked by name (judgment) |
| Sampling without replacement | missing | → suggest part03 | No hit |
| Binomial distribution | partial | part03_mathematics.topics.md — Probability | Not checked by name (judgment) |
| Maximum-entropy distributions | covered | part03_mathematics.topics.md — Probability | Line 78 |
| Jeffreys and ignorance priors | covered | part03_mathematics.topics.md — Probability | Line 79 |
| Predictive distributions | partial | part19_machine_learning.topics.md — Specialised learning areas | Posterior predictive named (line 87); not in part03 |
| Interval estimation | covered | part03_mathematics.topics.md — Statistics and experimental design | Confidence intervals (line 87) |
| Gauss and Herschel–Maxwell derivations | partial | part03_mathematics.topics.md — Information theory | Gaussian channel named (line 206); the derivations are not |
| Central limit theorem | covered | part03_mathematics.topics.md — Probability | Law of large numbers and CLT (line 62) |
| Hermite polynomials | partial | part03b_analysis_calculus_and_number_theory.topics.md — Real analysis | Hermite's method for e only (line 62) |
| Sufficiency and the likelihood principle | covered | part03_mathematics.topics.md — Statistics and experimental design | Factorization theorem (line 103) |
| Ancillarity | covered | part03_mathematics.topics.md — Statistics and experimental design | Basu's theorem (line 104) |
| Fisher information | covered | part03_mathematics.topics.md — Probability | Line 79 |
| Chi-squared | partial | part03_mathematics.topics.md — Statistics and experimental design | Chi-square distribution (line 109); no chi-squared test |
| Bertrand's problem | missing | → suggest part03 | No hit |
| Halley's mortality table | out of scope | - | Historical example |
| Decision theory and loss functions | partial | part03_mathematics.topics.md — Decision mathematics | Utility in part19 (line 16); loss functions not checked by name |
| Nonconglomerability and Borel–Kolmogorov paradox | covered | part03_mathematics.topics.md — Probability | Line 80 |
| Rule of succession and de Finetti | covered | part03_mathematics.topics.md — Probability | Line 81 |
| Model comparison | covered | part19_machine_learning.topics.md — Classical machine learning | AIC and BIC (lines 74, 80) |
| Outliers and robustness | partial | part03_mathematics.topics.md — Statistics and experimental design | Not checked by name (judgment) |
| Communication theory (channel coding) | covered | part03_mathematics.topics.md — Information theory | Shannon's source-coding bound (line 203) and channel capacity (line 206) |

## All of Statistics — Larry Wasserman

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Sample spaces, random variables, expectations | covered | part03_mathematics.topics.md — Probability | Standard probability rows |
| Inequalities | covered | part03_mathematics.topics.md — Probability | Markov, Chebyshev and Chernoff (line 61) |
| Convergence in probability | covered | part03_mathematics.topics.md — Probability | Line 62 |
| Stochastic processes | covered | part03_mathematics.topics.md — Probability | Markov chains (lines 72, 201) |
| Maximum likelihood estimation and its properties | covered | part03_mathematics.topics.md — Statistics and experimental design | Line 86 |
| Delta method | covered | part03_mathematics.topics.md — Statistics and experimental design | Line 107 |
| Parametric bootstrap | covered | part03_mathematics.topics.md — Statistics and experimental design | Line 89 |
| Jackknife and percentile intervals | partial | part03_mathematics.topics.md — Statistics and experimental design | Jackknife named (line 89); percentile intervals not checked by name |
| Exponential families | covered | part03_mathematics.topics.md — Statistics and experimental design | Line 105 |
| Density estimation | partial | part03_mathematics.topics.md — Statistics and experimental design | Nonparametric inference (line 117) |
| Curve estimation and smoothing | partial | part19_machine_learning.topics.md — Deep learning | Splines and basis expansions (line 77) |
| Classification, machine learning and data mining | covered | part19_machine_learning.topics.md — Classical machine learning | Logistic regression and ensembles |
| Graphical EDA | partial | part03_mathematics.topics.md — Statistics and experimental design | Quantiles from histograms (line 96) |

## Statistical Inference — Casella & Berger

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Set theory | partial | part03_mathematics.topics.md — Proof and discrete mathematics | Sets named in proof and discrete rows (judgment) |
| Distribution of functions of a random variable | partial | part03_mathematics.topics.md — Probability | Change of variables not checked by name |
| Expected values | covered | part03_mathematics.topics.md — Probability | Standard rows |
| Exponential family | covered | part03_mathematics.topics.md — Statistics and experimental design | Line 105 |
| Location-scale family | missing | → suggest part03 | No hit |
| Joint, marginal and conditional distributions | covered | part03_mathematics.topics.md — Probability | Total probability (line 75) |
| Sampling from the normal; t and F | covered | part03_mathematics.topics.md — Statistics and experimental design | Student's t and F (line 109) |
| Order statistics | covered | part08_data_structures_algorithms.topics.md — Sorting, searching and strings | Median and order statistics (line 63) |
| Convergence almost surely and in distribution | partial | part03_mathematics.topics.md — Probability | Convergence in probability only (line 62) |
| Delta method | covered | part03_mathematics.topics.md — Statistics and experimental design | Line 107 |
| Basu's theorem | covered | part03_mathematics.topics.md — Statistics and experimental design | Line 104 |
| ANOVA | partial | part03_mathematics.topics.md — Statistics and experimental design | Experimental design named; ANOVA not checked by name (judgment) |
| Errors in variables | missing | → suggest part03 | No hit |
| Logistic regression | covered | part19_machine_learning.topics.md — Classical machine learning | Named in classical ML (judgment) |
| Robust regression | partial | part19_machine_learning.topics.md — Classical machine learning | Not checked by name (judgment) |
| Hypothesis testing and interval estimation | covered | part03_mathematics.topics.md — Statistics and experimental design | Type I and II errors (line 112); confidence intervals (line 87) |
| Examples, exercises and tables | out of scope | - | Back matter |

## Introduction to Algorithms — CLRS

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Asymptotic notation (O, Ω, Θ) | covered | part08_data_structures_algorithms.topics.md — Analysis | Line 7–23 block |
| Insertion sort | partial | part08_data_structures_algorithms.topics.md — Analysis | Analysis block (line 16); insertion sort not checked by name |
| Divide-and-conquer and Strassen | covered | part08_data_structures_algorithms.topics.md — Analysis | Strassen (line 21) |
| Master method, substitution, recursion tree | covered | part08_data_structures_algorithms.topics.md — Analysis | Recurrences (line 19) |
| Akra–Bazzi method | covered | part08_data_structures_algorithms.topics.md — Analysis | Line 19 names the recurrence family (judgment) |
| Probabilistic analysis and randomized algorithms | covered | part08_data_structures_algorithms.topics.md — Randomized and probabilistic structures | Randomized section (line 85) |
| Heapsort and priority queues | covered | part08_data_structures_algorithms.topics.md — Trees and heaps | Line 42–52 block |
| Quicksort | covered | part08_data_structures_algorithms.topics.md — Sorting, searching and strings | Sorting block (judgment) |
| Linear-time sorts (counting, radix, bucket) | partial | part08_data_structures_algorithms.topics.md — Sorting, searching and strings | Not checked by name |
| Medians and order statistics | covered | part08_data_structures_algorithms.topics.md — Sorting, searching and strings | Median of medians (line 63) |
| Stacks, queues, linked lists | covered | part08_data_structures_algorithms.topics.md — Linear structures and techniques | Line 24–33 block |
| Hash tables (open addressing) | covered | part08_data_structures_algorithms.topics.md — Hashing | Lines 36–37 |
| Binary search trees | covered | part08_data_structures_algorithms.topics.md — Trees and heaps | Line 45 |
| Red-black trees | covered | part08_data_structures_algorithms.topics.md — Trees and heaps | Red-black or AVL (line 45) |
| Augmenting data structures | missing | → suggest part08 | No hit |
| B-trees | covered | part08_data_structures_algorithms.topics.md — Trees and heaps | Line 46 |
| Disjoint sets | partial | part08_data_structures_algorithms.topics.md — Graph algorithms | Union-find only in part06 (line 234); Kruskal named (line 74) |
| Dynamic programming | covered | part08_data_structures_algorithms.topics.md — Greedy algorithms and dynamic programming | Line 82 |
| Greedy algorithms | covered | part08_data_structures_algorithms.topics.md — Greedy algorithms and dynamic programming | Line 80 |
| Amortized analysis | covered | part08_data_structures_algorithms.topics.md — Analysis | Line 16 and line 26 |
| Graph representations and traversals | covered | part08_data_structures_algorithms.topics.md — Graph algorithms | BFS and DFS (line 121) |
| Minimum spanning trees (Prim, Kruskal) | covered | part08_data_structures_algorithms.topics.md — Graph algorithms | Line 74 |
| Single-source shortest paths (Bellman–Ford, Dijkstra) | covered | part08_data_structures_algorithms.topics.md — Graph algorithms | Line 72 |
| All-pairs shortest paths (Floyd–Warshall) | covered | part08_data_structures_algorithms.topics.md — Graph algorithms | Line 73 |
| Maximum flow | covered | part08_data_structures_algorithms.topics.md — Graph algorithms | Line 75 |
| Bipartite matching | missing | → suggest part08 | Bipartite graphs named only (part03 line 37); no matching algorithm |
| Number-theoretic algorithms (GCD, CRT, RSA, primality) | covered | part03_mathematics.topics.md — Proof and discrete mathematics | CRT (line 30); RSA (part14 line 43); primality (part03b line 98) |
| Approximation algorithms (vertex cover, TSP, set cover, subset sum) | covered | part08_data_structures_algorithms.topics.md — Computability and complexity | Lines 96–98 |
| Counting, probability and binomial tails | covered | part03_mathematics.topics.md — Probability | Standard rows |
| Fourth-edition additions | out of scope | - | Edition change log |

## Optimization by Vector Space Methods — Luenberger

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Hilbert space | covered | part03b_analysis_calculus_and_number_theory.topics.md — Complex and functional analysis | Line 69 |
| Least-squares estimation | covered | part03_mathematics.topics.md — Linear algebra | Line 146 |
| Dual spaces and Hahn–Banach | covered | part03b_analysis_calculus_and_number_theory.topics.md — Complex and functional analysis | Line 70 |
| Linear operators and adjoints | partial | part03b_analysis_calculus_and_number_theory.topics.md — Complex and functional analysis | Bounded operators (line 69); adjoints not checked by name |
| Optimization of functionals | partial | part03_mathematics.topics.md — Calculus and optimization | Not checked by name (judgment) |
| Constrained optimization and Kuhn–Tucker | covered | part03_mathematics.topics.md — Calculus and optimization | KKT conditions (line 175) |
| Pontryagin maximum principle | covered | part03_mathematics.topics.md — Calculus and optimization | Line 185 |
| Successive approximation | covered | part03_mathematics.topics.md — Numerical computing | Line 196 |
| Newton's method | covered | part03_mathematics.topics.md — Calculus and optimization | Line 178 |
| Steepest descent | partial | part03_mathematics.topics.md — Calculus and optimization | Gradient descent named (line 172); steepest descent not named |
| Conjugate directions and conjugate gradient | covered | part03_mathematics.topics.md — Calculus and optimization | Line 179 |
| Projection methods | covered | part03_mathematics.topics.md — Numerical computing | Line 196 |

## Advanced Engineering Mathematics — Kreyszig

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| First-order ODEs | covered | part03b_analysis_calculus_and_number_theory.topics.md — Calculus and differential equations | Judgment from the ODE rows |
| Second-order linear ODEs | covered | part03b_analysis_calculus_and_number_theory.topics.md — Calculus and differential equations | Wronskian (line 27) |
| Series solutions (Frobenius, Bessel) | covered | part03b_analysis_calculus_and_number_theory.topics.md — Calculus and differential equations | Line 28 |
| Laplace transforms | covered | part03c_signals_systems_and_communications.topics.md — Transforms and system analysis | Line 19 |
| Matrices, vectors and determinants | covered | part03_mathematics.topics.md — Linear algebra | Lines 143–145 |
| Eigenvalue problems | covered | part03_mathematics.topics.md — Linear algebra | Line 147 |
| Vector differential calculus | partial | part03b_analysis_calculus_and_number_theory.topics.md — Calculus and differential equations | Not checked by name (judgment) |
| Vector integral calculus (Green, Stokes, divergence) | covered | part03b_analysis_calculus_and_number_theory.topics.md — Calculus and differential equations | Stokes' theorem (line 25) |
| Fourier analysis | covered | part03c_signals_systems_and_communications.topics.md — Transforms and system analysis | Line 25 |
| Partial differential equations | covered | part03b_analysis_calculus_and_number_theory.topics.md — Calculus and differential equations | Classification of PDEs (line 26) |
| Complex integration (Cauchy theorem and formula) | covered | part03b_analysis_calculus_and_number_theory.topics.md — Complex and functional analysis | Line 67 |
| Potential theory and conformal mapping | covered | part03b_analysis_calculus_and_number_theory.topics.md — Complex and functional analysis | Conformal geometry (line 67) |
| Numerics for ODEs and PDEs | partial | part03_mathematics.topics.md — Numerical computing | Numerical methods named; PDE solvers not checked by name |
| Optimization and graphs | covered | part03_mathematics.topics.md — Calculus and optimization | Linear programming (line 176); graphs in part08 |
| Probability and statistics | covered | part03_mathematics.topics.md — Probability | Standard rows |
| Review questions and CAS projects | out of scope | - | Exercises |

## Digital Signal Processing — Proakis & Manolakis

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Signals, systems and classification | covered | part03c_signals_systems_and_communications.topics.md — Signals and linear time-invariant systems | Line 7–16 block |
| Convolution sum and LTI properties | covered | part03c_signals_systems_and_communications.topics.md — Signals and linear time-invariant systems | Line 9 (judgment) |
| z-transform | covered | part03c_signals_systems_and_communications.topics.md — Transforms and system analysis | Line 18 |
| Discrete Fourier transform and DTFT | covered | part03c_signals_systems_and_communications.topics.md — Transforms and system analysis | Line 25 |
| Cepstrum | covered | part03c_signals_systems_and_communications.topics.md — Practical spectral analysis | Real cepstrum (line 41) |
| STFT and spectrograms | covered | part03_mathematics.topics.md — Signals and sequences | Spectrograms (line 218) |
| Frequency response, deconvolution | partial | part03c_signals_systems_and_communications.topics.md — Transforms and system analysis | Not checked by name (judgment) |
| Ideal sampling and reconstruction | covered | part03c_signals_systems_and_communications.topics.md — Signals and linear time-invariant systems | Line 11 |
| Bandpass sampling | partial | part03c_signals_systems_and_communications.topics.md — Signals and linear time-invariant systems | Aliasing covered (line 11); bandpass not checked by name |
| Oversampling and A/D, D/A conversion | partial | part03c_signals_systems_and_communications.topics.md — Digital filters and multirate processing | Quantization (line 30) |
| DFT properties and Goertzel | covered | part03c_signals_systems_and_communications.topics.md — Practical spectral analysis | Goertzel (line 38) |
| Chirp-z transform | covered | part03c_signals_systems_and_communications.topics.md — Practical spectral analysis | Line 38 |
| Quantization errors and limit cycles | covered | part03c_signals_systems_and_communications.topics.md — Digital filters and multirate processing | Line 30 |
| Sparse FFT | missing | → suggest part03c | No hit |
| FIR structures and implementation | partial | part03c_signals_systems_and_communications.topics.md — Digital filters and multirate processing | FIR design (line 29); structures not checked by name |
| Multirate filter banks and wavelets | covered | part03c_signals_systems_and_communications.topics.md — Digital filters and multirate processing | Line 33 |

## Digital Communications — Proakis & Salehi

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Channel models | partial | part03c_signals_systems_and_communications.topics.md — Digital communications | Channel models implicit (judgment) |
| Signal space and Gram–Schmidt | partial | part03_mathematics.topics.md — Linear algebra | Gram–Schmidt (line 146); signal space not named |
| Karhunen–Loève expansion | missing | → suggest part03 | No hit |
| Modulation (PAM, PSK, QAM) | covered | part03c_signals_systems_and_communications.topics.md — Digital communications | Line 49 |
| Optimum receivers for AWGN | covered | part03c_signals_systems_and_communications.topics.md — Digital communications | Matched filter (line 50) |
| Carrier and symbol synchronization (PLL) | covered | part03c_signals_systems_and_communications.topics.md — Digital communications | Line 51 |
| Information theory (entropy, mutual information, rate distortion) | covered | part03_mathematics.topics.md — Information theory | Lines 201, 208 |
| Linear block codes | covered | part03_mathematics.topics.md — Information theory | LDPC (line 211); block codes (part08 line 104) |
| Trellis and graph codes | partial | part08_data_structures_algorithms.topics.md — Computability and complexity | Trellis named only in linear block codes context (judgment) |
| Band-limited channels | partial | part03c_signals_systems_and_communications.topics.md — Digital communications | Pulse shape and bandwidth (line 49) |
| Adaptive equalization | covered | part03c_signals_systems_and_communications.topics.md — Digital communications | Line 52 |
| Multichannel and multicarrier | covered | part03c_signals_systems_and_communications.topics.md — Digital communications | Spread spectrum and OFDM (line 53) |
| Spread spectrum | covered | part03c_signals_systems_and_communications.topics.md — Digital communications | Line 53 |
| Fading channels (Ricean, Rayleigh) | covered | part03c_signals_systems_and_communications.topics.md — Digital communications | Line 55 |
| Multiple antennas | covered | part03c_signals_systems_and_communications.topics.md — Digital communications | MIMO (line 54) |
| Multiuser communications | covered | part03_mathematics.topics.md — Information theory | Network information theory (line 210) |

## Understanding Digital Signal Processing — Lyons

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Discrete sequences and LTI systems | covered | part03c_signals_systems_and_communications.topics.md — Signals and linear time-invariant systems | Line 7 block |
| Periodic sampling and aliasing | covered | part03c_signals_systems_and_communications.topics.md — Signals and linear time-invariant systems | Line 11 |
| DFT: leakage, windows, zero padding | covered | part03_mathematics.topics.md — Signals and sequences | Windowing (line 217) |
| Radix-2 FFT and bit reversal | partial | part03_mathematics.topics.md — Signals and sequences | FFT named (line 217); bit reversal not checked |
| FIR filters (Parks–McClellan, half-band) | covered | part03c_signals_systems_and_communications.topics.md — Digital filters and multirate processing | Line 29 |
| IIR filters (impulse invariance, bilinear transform) | covered | part03c_signals_systems_and_communications.topics.md — Digital filters and multirate processing | Line 29 |
| Specialized networks (differentiators, integrators, matched filters, CIC) | covered | part03c_signals_systems_and_communications.topics.md — Digital filters and multirate processing | CIC filters (line 34) |
| Quadrature signals | partial | part03c_signals_systems_and_communications.topics.md — Digital communications | Not checked by name (judgment) |
| Discrete Hilbert transform | partial | part03c_signals_systems_and_communications.topics.md — Digital filters and multirate processing | Not checked by name (judgment) |
| Sample-rate conversion (decimation, polyphase) | covered | part03c_signals_systems_and_communications.topics.md — Digital filters and multirate processing | Polyphase (line 32) |
| Signal averaging | partial | part03_mathematics.topics.md — Statistics and experimental design | Not checked by name (judgment) |
| Fixed- and floating-point formats | partial | part03_mathematics.topics.md — Numerical computing | Numerical computing named (line 187) |
| DSP tricks (frequency translation, linear interpolation) | missing | → suggest part03c | No hit |

## Signals and Systems — Oppenheim & Willsky

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Signals and systems; LTI systems | covered | part03c_signals_systems_and_communications.topics.md — Signals and linear time-invariant systems | Line 7 block |
| Fourier series and transforms | covered | part03c_signals_systems_and_communications.topics.md — Transforms and system analysis | Line 25 |
| Sampling | covered | part03c_signals_systems_and_communications.topics.md — Signals and linear time-invariant systems | Line 11 |
| Communication systems | covered | part03c_signals_systems_and_communications.topics.md — Digital communications | Section 47–57 |
| Laplace transform | covered | part03c_signals_systems_and_communications.topics.md — Transforms and system analysis | Line 19 |
| z-transform | covered | part03c_signals_systems_and_communications.topics.md — Transforms and system analysis | Line 18 |
| Linear feedback | covered | part03c_signals_systems_and_communications.topics.md — Signals and linear time-invariant systems | Line 24 |

## Linear Systems and Signals — B.P. Lathi (3e, with Roger Green)

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Complex numbers, sinusoids, partial fractions | partial | part03c_signals_systems_and_communications.topics.md — Signals and linear time-invariant systems | Not checked by name (judgment) |
| Signal size (energy and power) | partial | part03c_signals_systems_and_communications.topics.md — Signals and linear time-invariant systems | Not checked by name (judgment) |
| Time-domain analysis (convolution, impulse response) | covered | part03c_signals_systems_and_communications.topics.md — Signals and linear time-invariant systems | Line 9 |
| Laplace and z-transform analysis | covered | part03c_signals_systems_and_communications.topics.md — Transforms and system analysis | Lines 18–19 |
| Fourier series and transform | covered | part03c_signals_systems_and_communications.topics.md — Transforms and system analysis | Line 25 |
| Sampling and discrete Fourier analysis | covered | part03c_signals_systems_and_communications.topics.md — Signals and linear time-invariant systems | Line 11 |
| State-space analysis of LTI systems | covered | part03c_signals_systems_and_communications.topics.md — Signals and linear time-invariant systems | Line 23 |

## Discrete-Time Signal Processing — Oppenheim & Schafer (3e)

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Discrete-time signals and systems | covered | part03c_signals_systems_and_communications.topics.md — Signals and linear time-invariant systems | Line 7 block |
| The z-transform | covered | part03c_signals_systems_and_communications.topics.md — Transforms and system analysis | Line 18 |
| Sampling of continuous-time signals | covered | part03c_signals_systems_and_communications.topics.md — Signals and linear time-invariant systems | Line 11 |
| Structures for discrete-time systems | partial | part03c_signals_systems_and_communications.topics.md — Digital filters and multirate processing | Polyphase structures (line 32) |
| Filter design techniques | covered | part03c_signals_systems_and_communications.topics.md — Digital filters and multirate processing | Line 29 |
| The discrete Fourier transform and its computation | covered | part03_mathematics.topics.md — Signals and sequences | Line 217 |
| Parametric signal modeling | covered | part03c_signals_systems_and_communications.topics.md — Practical spectral analysis | LPC estimation (line 41–64 block) |
| Discrete Hilbert transforms | partial | part03c_signals_systems_and_communications.topics.md — Digital filters and multirate processing | Not checked by name (judgment) |

## Spoken Language Processing — Huang, Acero, Hon

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Spoken language structure (phonetics, phonology) | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech science and analysis | Phonetics block (line 7–20) |
| Pattern recognition (Bayes, EM, CART) | covered | part19_machine_learning.topics.md — Classical machine learning | Expectation maximization in classical ML (judgment) |
| Digital signal processing for speech (filterbanks) | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech science and analysis | Filter-bank analysis (line 13) |
| Speech representations: LPC, cepstrum, MFCC, formants, pitch | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech science and analysis | Formants (lines 9, 11); MFCC in part03 (line 218); PLP not named |
| Speech coding (PCM, µ-law, CELP) | missing | → suggest part19b | No hit |
| Hidden Markov models (Viterbi, Baum–Welch) | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech recognition: from HMMs to Kaldi | Line 25 |
| Acoustic modeling (MAP, MLLR, confidence) | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech recognition: from HMMs to Kaldi | Lines 25, 43 |
| Environmental robustness (CMN, PMC, VTS) | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech science and analysis | CMN, PMC, VTS (line 19); acoustic echo cancellation and arrays missing |
| Acoustic echo cancellation and beamforming | missing | → suggest part19b | No hit |
| Language modeling: Chomsky hierarchy | partial | part07 regular languages (line 63) | Regular languages and pumping lemma only; the full hierarchy and language-model link not checked |
| n-gram language models and smoothing | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Classical NLP and toolkits | Kneser–Ney (line 94) |
| Cache, topic and maximum-entropy language models | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Classical NLP and toolkits | Not named in part19b; maximum-entropy distributions in part03 (line 78) |
| Basic search (Viterbi beam, stack decoding, A*) | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech recognition: from HMMs to Kaldi | Stack decoding (line 33); A* (part19 line 20) |
| Large-vocabulary search (lexical trees, N-best) | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech recognition: from HMMs to Kaldi | N-best (line 24); lexical trees missing |
| Text analysis, normalization, letter-to-sound | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech synthesis, speakers and spoken-language systems | Not checked by name (judgment) |
| Prosody (duration, pitch) | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech synthesis, speakers and spoken-language systems | Not checked by name (judgment) |
| Speech synthesis (formant, concatenative, PSOLA) | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech synthesis, speakers and spoken-language systems | PSOLA (line 40) |
| Spoken language understanding and dialog | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech synthesis, speakers and spoken-language systems | Dialogue state tracking (line 44) |
| Applications and user interfaces | out of scope | - | Broad applications chapter |

## Elements of Information Theory — Cover & Thomas (2e)

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Entropy, relative entropy and mutual information | covered | part03_mathematics.topics.md — Information theory | Line 201 |
| Asymptotic equipartition property | covered | part03_mathematics.topics.md — Information theory | AEP experiment (line 246, from-scratch block) |
| Entropy rates of stochastic processes | partial | part03_mathematics.topics.md — Information theory | Not checked by name (judgment) |
| Data compression (Huffman) | covered | part03_mathematics.topics.md — Information theory | Line 203 |
| Gambling and data compression | missing | → suggest part03 | No hit for Kelly or gambling |
| Channel capacity | covered | part03_mathematics.topics.md — Information theory | Line 206 |
| Differential entropy | covered | part03_mathematics.topics.md — Information theory | Line 206 |
| Gaussian channel | covered | part03_mathematics.topics.md — Information theory | Line 206 |
| Rate distortion theory | covered | part03_mathematics.topics.md — Information theory | Line 208 |
| Information theory and statistics | partial | part03_mathematics.topics.md — Information theory | Not checked by name (judgment) |
| Maximum entropy | covered | part03_mathematics.topics.md — Probability | Line 78 |
| Universal source coding (Lempel–Ziv) | covered | part08_data_structures_algorithms.topics.md — Computability and complexity | Line 102 |
| Kolmogorov complexity | covered | part08_data_structures_algorithms.topics.md — Computability and complexity | Line 103 |
| Network information theory | covered | part03_mathematics.topics.md — Information theory | Line 210 |
| Information theory and portfolio theory | missing | → suggest part30 | No hit |
| Inequalities in information theory | partial | part04_problem_solving.topics.md — Contest mathematics toolkit | Jensen's inequality (line 27); information inequalities not checked by name |

## Pattern Recognition and Machine Learning — Bishop

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Polynomial curve fitting | covered | part19_machine_learning.topics.md — Classical machine learning | Regression (judgment) |
| Probability distributions (binary variables) | partial | part03_mathematics.topics.md — Probability | Not checked by name (judgment) |
| Linear models for regression | covered | part19_machine_learning.topics.md — Classical machine learning | Judgment |
| Linear models for classification | covered | part19_machine_learning.topics.md — Classical machine learning | Judgment |
| Neural networks | covered | part19_machine_learning.topics.md — Deep learning | Line 90–115 block |
| Kernel methods | partial | part19_machine_learning.topics.md — Classical machine learning | Kernels not checked by name (judgment) |
| Sparse kernel machines (SVM, RVM) | partial | part19_machine_learning.topics.md — Classical machine learning | SVMs covered; relevance vector machines missing |
| Graphical models | covered | part19_machine_learning.topics.md — Classical AI: search, knowledge and reasoning | Bayesian networks (lines 33, 35) |
| Mixture models and EM | covered | part19_machine_learning.topics.md — Classical machine learning | Judgment |
| Approximate inference | covered | part19_machine_learning.topics.md — Classical AI: search, knowledge and reasoning | Rejection sampling (line 34) |
| Sampling methods (Gibbs, Metropolis) | covered | part19_machine_learning.topics.md — Classical machine learning | Lines 34, 84, 86 |
| Continuous latent variables (PCA) | covered | part03_mathematics.topics.md — Linear algebra | PCA (line 148) |
| Sequential data (HMM, Kalman) | covered | part19_machine_learning.topics.md — Classical machine learning | Kalman (line 88) |
| Combining models (ensembles) | covered | part19_machine_learning.topics.md — Classical machine learning | Boosting and random forests (line 58) |

## Pattern Classification — Duda, Hart, Stork (2e)

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Bayesian decision theory | covered | part19_machine_learning.topics.md — Classical AI: search, knowledge and reasoning | Utility (line 16) |
| Maximum-likelihood and Bayesian parameter estimation | covered | part03_mathematics.topics.md — Statistics and experimental design | Line 86 |
| Nonparametric techniques | partial | part03_mathematics.topics.md — Statistics and experimental design | Nonparametric inference (line 117) |
| Linear discriminant functions | covered | part19_machine_learning.topics.md — Classical machine learning | Judgment |
| Multilayer neural networks | covered | part19_machine_learning.topics.md — Deep learning | Judgment |
| Stochastic methods (simulated annealing) | covered | part19_machine_learning.topics.md — Classical AI: search, knowledge and reasoning | Simulated annealing (line 21) |
| Nonmetric methods | partial | part19_machine_learning.topics.md — Classical machine learning | Not checked by name (judgment) |
| Algorithm-independent machine learning | missing | → suggest part19 | No hit |
| Unsupervised learning and clustering | covered | part19_machine_learning.topics.md — Classical machine learning | Spectral clustering (line 81) |

## The Elements of Statistical Learning — Hastie, Tibshirani, Friedman

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Linear methods for regression and classification | covered | part19_machine_learning.topics.md — Classical machine learning | Judgment |
| Basis expansions and splines | covered | part19_machine_learning.topics.md — Deep learning | Splines and basis expansions (line 77) |
| Kernel smoothing | partial | part19_machine_learning.topics.md — Classical machine learning | Not checked by name |
| Model assessment and selection | covered | part19_machine_learning.topics.md — Classical machine learning | AIC and BIC (lines 74, 80) |
| Additive models | missing | → suggest part19 | No hit (GAMs not named) |
| Boosting and random forests | covered | part19_machine_learning.topics.md — Classical machine learning | Line 58 |
| Reproducing kernel Hilbert spaces | missing | → suggest part19 | No hit |
| Spectral clustering | covered | part19_machine_learning.topics.md — Classical machine learning | Line 81 |
| False discovery rate and high-dimensional problems | covered | part03_mathematics.topics.md — Statistics and experimental design | Line 93 |
| Undirected graphical models | covered | part19_machine_learning.topics.md — Classical machine learning | Markov random fields (line 84) |

## Deep Learning — Goodfellow, Bengio, Courville

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Linear algebra and probability | covered | part03_mathematics.topics.md — Linear algebra | Standard rows |
| Numerical computation | covered | part03_mathematics.topics.md — Numerical computing | Line 187 block |
| Regularization and dropout | covered | part19_machine_learning.topics.md — Deep learning | Line 104 |
| Optimization for training (SGD, Adam) | covered | part19_machine_learning.topics.md — Deep learning | Adam and momentum (line 98) |
| Convolutional networks | covered | part19_machine_learning.topics.md — Deep learning | Convolutions (line 105) |
| Sequence modeling (RNN) | covered | part19_machine_learning.topics.md — Deep learning | Lines 106–108 |
| Practical methodology | partial | part19_machine_learning.topics.md — Deep learning | Not checked by name (judgment) |
| Autoencoders | covered | part20_generative_ai_1of3.topics.md — How LLMs work | Lines 40, 56, 151 |
| Structured probabilistic models | covered | part19_machine_learning.topics.md — Classical AI: search, knowledge and reasoning | Bayesian networks (line 33) |
| Monte Carlo methods | covered | part19_machine_learning.topics.md — Classical machine learning | Lines 34, 84 |
| Partition function | missing | → suggest part19 | No hit |
| Deep generative models | covered | part20_generative_ai_1of3.topics.md — Generative models beyond autoregression | Line 148 block |

## Artificial Intelligence: A Modern Approach — Russell & Norvig

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Intelligent agents | covered | part19_machine_learning.topics.md — Foundations of AI | Lines 7–12 block |
| Searching (A*) | covered | part19_machine_learning.topics.md — Classical AI: search, knowledge and reasoning | A* (line 20) |
| Constraint satisfaction problems | partial | part19_machine_learning.topics.md — Classical AI: search, knowledge and reasoning | Not checked by name |
| Adversarial search and games (MCTS) | covered | part19_machine_learning.topics.md — Classical AI: search, knowledge and reasoning | Monte Carlo tree search (line 23) |
| First-order logic and inference | partial | part19_machine_learning.topics.md — Classical AI: search, knowledge and reasoning | Not checked by name |
| Automated planning | partial | part19_machine_learning.topics.md — Classical AI: search, knowledge and reasoning | Not checked by name |
| Quantifying uncertainty and probabilistic reasoning | covered | part19_machine_learning.topics.md — Classical AI: search, knowledge and reasoning | Bayesian networks (line 33) |
| Reasoning over time (HMM, Kalman filters) | covered | part19_machine_learning.topics.md — Classical machine learning | Kalman (line 88) |
| Decisions (utility) | covered | part19_machine_learning.topics.md — Classical AI: search, knowledge and reasoning | Line 16 |
| Multiagent decisions (game theory) | covered | part19_machine_learning.topics.md — Specialised learning areas | Line 156 |
| Probabilistic programming | covered | part19_machine_learning.topics.md — Specialised learning areas | Line 87 |
| Natural language processing | covered | part19_machine_learning.topics.md — Natural language processing foundations | Line 116 block |
| Robotics | covered | part19_machine_learning.topics.md — Specialised learning areas | Robotics (line 39) |
| Computer vision | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Computer vision: images, motion and multi-view geometry | Line 46 block |
| Philosophy, ethics and safety | partial | part19_machine_learning.topics.md — Foundations of AI | Not checked by name (judgment) |

## Foundations of Statistical Natural Language Processing — Manning & Schütze

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Collocations and pointwise mutual information | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Classical NLP and toolkits | PPMI (line 88) |
| n-gram models over sparse data | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Classical NLP and toolkits | Kneser–Ney (line 94) |
| Word sense disambiguation | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Classical NLP and toolkits | Not checked by name (judgment) |
| Lexical acquisition | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Classical NLP and toolkits | Not checked by name (judgment) |
| Markov models and part-of-speech tagging | covered | part19_machine_learning.topics.md — Natural language processing foundations | Sequence labelling (line 126) |
| Probabilistic CFGs and probabilistic parsing | partial | part19_machine_learning.topics.md — Natural language processing foundations | CKY parsing (line 127); PCFGs not named |
| Statistical machine translation | partial | part19_machine_learning.topics.md — Natural language processing foundations | Not checked by name (judgment) |
| Clustering | covered | part19_machine_learning.topics.md — Classical machine learning | Judgment |
| Topics in information retrieval | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Information retrieval engines | Line 73 block |
| Text categorization | covered | part19_machine_learning.topics.md — Natural language processing foundations | Summarization, classification and sentiment (line 132) |

## Automatic Speech Recognition: A Deep Learning Approach — Yu & Deng

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Gaussian mixture models | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech recognition: from HMMs to Kaldi | Line 21 block |
| Deep neural networks and backpropagation | covered | part19_machine_learning.topics.md — Deep learning | Judgment |
| RBMs and DBN pretraining | missing | → suggest part19 | No hit |
| DNN–HMM hybrid systems | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech recognition: from HMMs to Kaldi | Line 26 |
| Training and decoding speedup (ADMM, async SGD, distillation) | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech recognition: from HMMs to Kaldi | Distillation (line 26); ADMM missing |
| Sequence-discriminative training | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech recognition: from HMMs to Kaldi | Not checked by name |
| Feature representation learning | covered | part19_machine_learning.topics.md — Deep learning | Judgment |
| Adaptation of DNNs | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech recognition: from HMMs to Kaldi | MAP and MLLR (line 25) |
| Multitask, multilingual and transfer | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech recognition: from HMMs to Kaldi | Line 29 |
| Recurrent neural networks (BPTT, LSTM) | covered | part19_machine_learning.topics.md — Deep learning | Lines 106–108 |
| Computational network | partial | part19_machine_learning.topics.md — Deep learning | Not checked by name (judgment) |

## Speech and Language Processing — Jurafsky & Martin

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Unicode, regex, text normalization, minimum edit distance | covered | part08_data_structures_algorithms.topics.md — Greedy algorithms and dynamic programming | Edit distance (line 82) |
| n-gram language models and perplexity | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Classical NLP and toolkits | Kneser–Ney (line 94) |
| Logistic regression, Naive Bayes, sentiment | covered | part19_machine_learning.topics.md — Classical machine learning | Judgment |
| Vector semantics, TF-IDF and embeddings | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Classical NLP and toolkits | TF-IDF and Word2Vec (lines 120–121) |
| Large language models | covered | part20_generative_ai_1of3.topics.md — How LLMs work | Line 7 block |
| Transformers and self-attention | covered | part19_machine_learning.topics.md — Deep learning | Transformer (line 111) |
| Post-training (instruction tuning, DPO) | covered | part20_generative_ai_1of3.topics.md — Fine-tuning and adaptation | DPO (line 97) |
| Masked language models (BERT) | covered | part20_generative_ai_1of3.topics.md — How LLMs work | Lines 15, 34, 39 |
| Information retrieval and RAG | covered | part20_generative_ai_1of3.topics.md — Embeddings and retrieval | Line 162 block |
| Machine translation and encoder-decoder | partial | part19_machine_learning.topics.md — Natural language processing foundations | Not checked by name (judgment) |
| Phonetics and speech features | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech science and analysis | Line 7–20 block |
| Automatic speech recognition and TTS | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech recognition: from HMMs to Kaldi | Lines 21–45 |
| Sequence labeling (HMM, CRF) | covered | part19_machine_learning.topics.md — Natural language processing foundations | CRF (line 126) |
| CFGs and constituency parsing | covered | part19_machine_learning.topics.md — Natural language processing foundations | Line 127 |
| Dependency parsing | missing | → suggest part19 | No hit |
| Information extraction | covered | part19_machine_learning.topics.md — Natural language processing foundations | Line 130 |
| Semantic role labeling | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Classical NLP and toolkits | Line 90 |
| Coreference and entity linking | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Classical NLP and toolkits | Coreference (line 108); entity linking (part19 line 130) |
| Discourse coherence (entity grid) | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Classical NLP and toolkits | Line 87 |
| Conversation structure and dialogue acts | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech synthesis, speakers and spoken-language systems | Dialogue state tracking (line 44); dialogue acts not named |
| Combinatory categorial grammar | missing | → suggest part19b | No hit |
| WordNet | covered | part19_machine_learning.topics.md — Natural language processing foundations | Line 128 |

## Game Engine Architecture — Jason Gregory

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Runtime architecture and game loop | covered | part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering | Line 36 block |
| Asset pipeline and resources | partial | part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering | Not checked by name (judgment) |
| Tools (version control, profilers) | partial | part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering | Not checked by name (judgment) |
| Parallelism: threads, lock-free, SIMD | covered | part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering | Lock-free hand-off (line 43); SIMD (part02 line 74) |
| 3D math: vectors, matrices, quaternions | covered | part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering | Quaternion slerp (line 41) |
| Engine support and memory | partial | part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering | Not checked by name (judgment) |
| Human input devices | partial | part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering | Not checked by name (judgment) |
| Rendering | covered | part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering | Lines 46–48 block |
| Animation | covered | part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering | Skeletal animation (line 41) |
| Collision and rigid body | partial | part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering | Ray–primitive intersection (line 52); rigid body not named |
| Audio | partial | part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering | Not checked by name (judgment) |
| Object models, events and scripting | partial | part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering | Not checked by name (judgment) |

## Real-Time Rendering — Akenine-Möller et al.

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Graphics pipeline | covered | part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering | Line 36 block |
| GPU | covered | part02_computer_organization.topics.md:74 | SIMD and GPUs (line 74); no `###` heading in the cited block (judgment) |
| Transforms | covered | part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering | Skeletal animation (line 41) |
| Texturing | partial | part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering | Not checked by name (judgment) |
| Shadows | covered | part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering | Shadow maps (line 48) |
| Light and color | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Computer vision: images, motion and multi-view geometry | Light, shading and reflectance (line 54) |
| Physically based rendering and BRDFs | covered | part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering | Shading and BRDFs (line 46) |
| Global illumination | partial | part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering | Not checked by name (judgment) |
| Image-space effects (depth of field, tone mapping) | partial | part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering | Not checked by name (judgment) |
| Particles and point clouds | covered | part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering | Particles (line 61) |
| Volumetric and translucent rendering | missing | → suggest part30 | No hit |
| Non-photorealistic rendering | missing | → suggest part30 | No hit |
| Curves and curved surfaces | covered | part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering | Splines (line 55) |
| Acceleration structures | covered | part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering | BVH (line 52) |
| VR and AR | covered | part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering | Virtual and augmented reality (line 54) |
| Intersection tests and real-time ray tracing | covered | part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering | Line 52 |

## ICSE / Selina Concise (Classes 6–10)

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Class 6: estimation | covered | part01_school_foundations.topics.md:10 | Rounding and estimation (line 10) |
| Class 6: place value | missing | → suggest part01 | No hit |
| Class 6: natural and whole numbers, closure | covered | part01_school_foundations.topics.md:8 | Closure (line 8) |
| Class 6: integers and the number line | partial | part01_school_foundations.topics.md:8 | Integers named (line 8); number line missing |
| Class 6: speed, distance, time | covered | part01_school_foundations.topics.md:12 | Speed (line 12) |
| Class 6: unitary method | covered | part01_school_foundations.topics.md:17 | Unitary method (line 17) |
| Class 6: algebra (substitution, linear equations) | covered | part01_school_foundations.topics.md:24 | Algebra block |
| Class 7: percent | covered | part01_school_foundations.topics.md:8 | Percentages (line 8) |
| Class 7: profit, loss, discount | partial | part01_school_foundations.topics.md:120 | Discounts only (line 120) |
| Class 7: simple interest | covered | part01_school_foundations.topics.md:120 | I = Prt/100 (line 120) |
| Class 7: Pythagoras | covered | part01_school_foundations.topics.md:44 | Line 44 |
| Class 7: mensuration | covered | part01_school_foundations.topics.md:73 | Mensuration (line 73) |
| Class 7: data handling and probability | covered | part01_school_foundations.topics.md:95 | Probability and data (line 95) |
| Class 8: direct and inverse variation | covered | part01_school_foundations.topics.md:16 | Line 16 |
| Class 8: algebraic identities and factorisation | covered | part01_school_foundations.topics.md:62 | Factoring (line 62) |
| Class 8: linear inequalities | covered | part01_school_foundations.topics.md:24 | Inequalities (line 24) |
| Class 8: constructions | covered | part01_school_foundations.topics.md:72 | Line 72 |
| Class 8: circles | covered | part01_school_foundations.topics.md:68 | Circle theorems (lines 68–69) |
| Class 9: compound interest | partial | part01_school_foundations.topics.md:120 | Simple interest only (line 120); compound not named |
| Class 9: midpoint theorem | covered | part01_school_foundations.topics.md:65 | Line 65 |
| Class 9: trigonometric ratios and heights and distances | covered | part01_school_foundations.topics.md:55 | Heights and distances (line 55) |
| Class 10: GST | covered | part30_supplementary_applied_domains.topics.md — Corporate finance | VAT and GST (line 17) |
| Class 10: banking and recurring deposits | covered | part30_supplementary_applied_domains.topics.md — Corporate finance | Recurring deposits and amortization (line 10) |
| Class 10: shares and dividends | missing | → suggest part30 | No hit |
| Class 10: linear inequations | covered | part01_school_foundations.topics.md:24 | Line 24 |
| Class 10: quadratic equations | partial | part01_school_foundations.topics.md:31 | Quadratic functions named (line 31); equation solving not checked by name |
| Class 10: ratio and proportion | covered | part01_school_foundations.topics.md:14 | Componendo and dividendo (lines 14–15) |
| Class 10: remainder and factor theorems | partial | part01_school_foundations.topics.md:62 | Factor theorem not checked by name |
| Class 10: matrices | covered | part03_mathematics.topics.md — Linear algebra | Matrix operations (judgment) |
| Class 10: AP and GP | partial | part03_mathematics.topics.md — Probability | Not checked by name (judgment) |
| Class 10: section and midpoint formula | covered | part01_school_foundations.topics.md:77 | Line 77 |
| Class 10: equation of a line | covered | part03b_analysis_calculus_and_number_theory.topics.md — Coordinate geometry and conics | Line 32 block |
| Class 10: loci | covered | part01_school_foundations.topics.md:71 | Line 71 |
| Class 10: circles and tangents | covered | part01_school_foundations.topics.md:70 | Tangents (line 70) |
| Class 10: cylinder, cone, sphere | covered | part01_school_foundations.topics.md:73 | Mensuration (line 73) |
| Class 10: trigonometric identities | partial | part01_school_foundations.topics.md:55 | Not checked by name (judgment) |
| Class 10: measures of central tendency | covered | part03_mathematics.topics.md — Statistics and experimental design | Judgment |

## Understanding ICSE Mathematics — M.L. Aggarwal (Class 10)

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| VAT and GST (intra- and inter-state, ITC) | covered | part30_supplementary_applied_domains.topics.md — Corporate finance | Line 17 |
| Banking (compound interest, recurring deposits, amortization) | partial | part30_supplementary_applied_domains.topics.md — Corporate finance | Recurring deposits and amortization (line 10); compound interest not named |
| Shares and dividends | missing | → suggest part30 | No hit |
| Linear inequations | covered | part01_school_foundations.topics.md:24 | Line 24 |
| Quadratics (nature of roots) | partial | part01_school_foundations.topics.md:31 | Not checked by name |
| Factorization (factor theorem, remainder theorem) | partial | part01_school_foundations.topics.md:62 | Factoring named (line 62) |
| Ratio and proportion (componendo, continued proportion) | covered | part01_school_foundations.topics.md:14 | Lines 14–15 |
| Matrices | covered | part03_mathematics.topics.md — Linear algebra | Judgment |
| AP and GP | partial | part03_mathematics.topics.md — Probability | Not checked by name (judgment) |

## Missing in this range

- Uniqueness of the real numbers — → suggest part03 No hit for uniqueness of the reals
- Countable and uncountable sets — → suggest part03 No hit for countability
- Perfect and connected sets — → suggest part03b No hit for perfect or connected sets
- Summation by parts — → suggest part03b No hit
- Cauchy product and rearrangements of series — → suggest part03b No Cauchy product; rearrangement only in part04 Inequalities (line 27)
- Rectifiable curves — → suggest part03b No hit
- Equicontinuous families — → suggest part03b No hit
- The gamma function — → suggest part03b No hit
- Differentiation of integrals — → suggest part03b No hit
- Partitions of unity — → suggest part03b No hit
- Inverse matrices — → suggest part03 No hit for matrix inverse
- Sampling without replacement — → suggest part03 No hit
- Bertrand's problem — → suggest part03 No hit
- Location-scale family — → suggest part03 No hit
- Errors in variables — → suggest part03 No hit
- Augmenting data structures — → suggest part08 No hit
- Bipartite matching — → suggest part08 Bipartite graphs named only (part03 line 37); no matching algorithm
- Sparse FFT — → suggest part03c No hit
- Karhunen–Loève expansion — → suggest part03 No hit
- DSP tricks (frequency translation, linear interpolation) — → suggest part03c No hit
- Speech coding (PCM, µ-law, CELP) — → suggest part19b No hit
- Acoustic echo cancellation and beamforming — → suggest part19b No hit
- Gambling and data compression — → suggest part03 No hit for Kelly or gambling
- Information theory and portfolio theory — → suggest part30 No hit
- Algorithm-independent machine learning — → suggest part19 No hit
- Additive models — → suggest part19 No hit (GAMs not named)
- Reproducing kernel Hilbert spaces — → suggest part19 No hit
- Partition function — → suggest part19 No hit
- RBMs and DBN pretraining — → suggest part19 No hit
- Dependency parsing — → suggest part19 No hit
- Combinatory categorial grammar — → suggest part19b No hit
- Volumetric and translucent rendering — → suggest part30 No hit
- Non-photorealistic rendering — → suggest part30 No hit
- Class 6: place value — → suggest part01 No hit
- Class 10: shares and dividends — → suggest part30 No hit
- Shares and dividends — → suggest part30 No hit

## Partial in this range

- Numbers of various sorts (naturals, integers, rationals, reals) — part01_school_foundations.topics.md:8 — Number system named; the sorts are not separated (judgment)
- Polar coordinates — part03b_analysis_calculus_and_number_theory.topics.md — Coordinate geometry and conics — Polar forms of lines and conics only (lines 34, 41)
- Three hard theorems (IVT, EVT, MVT) — part03b_analysis_calculus_and_number_theory.topics.md — Real analysis — Rolle and mean value theorems (line 57); IVT and EVT not checked by name
- Uniform continuity — part03b_analysis_calculus_and_number_theory.topics.md — Real analysis — Uniform convergence named (line 56); uniform continuity not checked by name
- Convexity and concavity — part03_mathematics.topics.md — Calculus and optimization — Convex optimization named; convexity of functions not checked by name (judgment)
- Integration in elementary terms — part03b_analysis_calculus_and_number_theory.topics.md — Calculus and differential equations — Definite integrals and techniques (line 18); no elementary-function theory
- Trigonometric functions — part03b_analysis_calculus_and_number_theory.topics.md — Real analysis — Not checked by name in the analysis section (judgment)
- Logarithm and exponential functions — part03b_analysis_calculus_and_number_theory.topics.md — Complex and functional analysis — Holomorphic and log only in complex functions (line 67)
- Complex power series — part03b_analysis_calculus_and_number_theory.topics.md — Complex and functional analysis — Power series in the real case only
- Extended real number system — part03b_analysis_calculus_and_number_theory.topics.md — Real analysis — Infinite limits only (judgment)
- Compact sets — part03b_analysis_calculus_and_number_theory.topics.md — Real analysis — Compactness not checked by name (judgment)
- Root and ratio tests — part03b_analysis_calculus_and_number_theory.topics.md — Calculus and differential equations — Series convergence named; tests not checked by name
- Continuity and compactness / connectedness — part03b_analysis_calculus_and_number_theory.topics.md — Real analysis — Continuity covered; the compactness and connectedness theorems not checked by name
- Monotonic functions — part03b_analysis_calculus_and_number_theory.topics.md — Real analysis — Monotone sequences and convergence (lines 55, 61)
- L'Hôpital's rule — part03b_analysis_calculus_and_number_theory.topics.md — Calculus and differential equations — Not checked by name (judgment)
- Algebraic completeness of the complex field — part03b_analysis_calculus_and_number_theory.topics.md — Complex and functional analysis — Complex functions only (judgment)
- Linear transformations (several variables) — part03_mathematics.topics.md — Linear algebra — Matrices as linear maps (line 144)
- Differentiation in several variables — part03b_analysis_calculus_and_number_theory.topics.md — Calculus and differential equations — Jacobian and gradient not checked by name (judgment)
- Rank theorem — part03_mathematics.topics.md — Linear algebra — Rank–nullity theorem (line 144)
- Change of variables — part03b_analysis_calculus_and_number_theory.topics.md — Calculus and differential equations — Not checked by name (judgment)
- Closed and exact forms — part03b_analysis_calculus_and_number_theory.topics.md — Calculus and differential equations — Differential forms named (line 25)
- Measurable functions — part03b_analysis_calculus_and_number_theory.topics.md — Real analysis — Lebesgue integration named (line 61)
- Complex matrices — part03_mathematics.topics.md — Linear algebra — Hermitian and unitary not checked by name
- Similarity transformations — part03_mathematics.topics.md — Linear algebra — Not checked by name (judgment)
- Matrix operations and transposes — part03_mathematics.topics.md — Linear algebra — Transposes named in matrix rows (judgment)
- Permutations — part03_mathematics.topics.md — Linear algebra — Not checked by name (judgment)
- Linear transformations — part03_mathematics.topics.md — Linear algebra — Matrices as linear maps (line 144); no change-of-basis rows
- Complex vectors and matrices — part03_mathematics.topics.md — Linear algebra — Not checked by name (judgment)
- Kolmogorov axioms — part03_mathematics.topics.md — Probability — Axioms not checked by name (judgment)
- Binomial distribution — part03_mathematics.topics.md — Probability — Not checked by name (judgment)
- Predictive distributions — part19_machine_learning.topics.md — Specialised learning areas — Posterior predictive named (line 87); not in part03
- Gauss and Herschel–Maxwell derivations — part03_mathematics.topics.md — Information theory — Gaussian channel named (line 206); the derivations are not
- Hermite polynomials — part03b_analysis_calculus_and_number_theory.topics.md — Real analysis — Hermite's method for e only (line 62)
- Chi-squared — part03_mathematics.topics.md — Statistics and experimental design — Chi-square distribution (line 109); no chi-squared test
- Decision theory and loss functions — part03_mathematics.topics.md — Decision mathematics — Utility in part19 (line 16); loss functions not checked by name
- Outliers and robustness — part03_mathematics.topics.md — Statistics and experimental design — Not checked by name (judgment)
- Jackknife and percentile intervals — part03_mathematics.topics.md — Statistics and experimental design — Jackknife named (line 89); percentile intervals not checked by name
- Density estimation — part03_mathematics.topics.md — Statistics and experimental design — Nonparametric inference (line 117)
- Curve estimation and smoothing — part19_machine_learning.topics.md — Deep learning — Splines and basis expansions (line 77)
- Graphical EDA — part03_mathematics.topics.md — Statistics and experimental design — Quantiles from histograms (line 96)
- Set theory — part03_mathematics.topics.md — Proof and discrete mathematics — Sets named in proof and discrete rows (judgment)
- Distribution of functions of a random variable — part03_mathematics.topics.md — Probability — Change of variables not checked by name
- Convergence almost surely and in distribution — part03_mathematics.topics.md — Probability — Convergence in probability only (line 62)
- ANOVA — part03_mathematics.topics.md — Statistics and experimental design — Experimental design named; ANOVA not checked by name (judgment)
- Robust regression — part19_machine_learning.topics.md — Classical machine learning — Not checked by name (judgment)
- Insertion sort — part08_data_structures_algorithms.topics.md — Analysis — Analysis block (line 16); insertion sort not checked by name
- Linear-time sorts (counting, radix, bucket) — part08_data_structures_algorithms.topics.md — Sorting, searching and strings — Not checked by name
- Disjoint sets — part08_data_structures_algorithms.topics.md — Graph algorithms — Union-find only in part06 (line 234); Kruskal named (line 74)
- Linear operators and adjoints — part03b_analysis_calculus_and_number_theory.topics.md — Complex and functional analysis — Bounded operators (line 69); adjoints not checked by name
- Optimization of functionals — part03_mathematics.topics.md — Calculus and optimization — Not checked by name (judgment)
- Steepest descent — part03_mathematics.topics.md — Calculus and optimization — Gradient descent named (line 172); steepest descent not named
- Vector differential calculus — part03b_analysis_calculus_and_number_theory.topics.md — Calculus and differential equations — Not checked by name (judgment)
- Numerics for ODEs and PDEs — part03_mathematics.topics.md — Numerical computing — Numerical methods named; PDE solvers not checked by name
- Frequency response, deconvolution — part03c_signals_systems_and_communications.topics.md — Transforms and system analysis — Not checked by name (judgment)
- Bandpass sampling — part03c_signals_systems_and_communications.topics.md — Signals and linear time-invariant systems — Aliasing covered (line 11); bandpass not checked by name
- Oversampling and A/D, D/A conversion — part03c_signals_systems_and_communications.topics.md — Digital filters and multirate processing — Quantization (line 30)
- FIR structures and implementation — part03c_signals_systems_and_communications.topics.md — Digital filters and multirate processing — FIR design (line 29); structures not checked by name
- Channel models — part03c_signals_systems_and_communications.topics.md — Digital communications — Channel models implicit (judgment)
- Signal space and Gram–Schmidt — part03_mathematics.topics.md — Linear algebra — Gram–Schmidt (line 146); signal space not named
- Trellis and graph codes — part08_data_structures_algorithms.topics.md — Computability and complexity — Trellis named only in linear block codes context (judgment)
- Band-limited channels — part03c_signals_systems_and_communications.topics.md — Digital communications — Pulse shape and bandwidth (line 49)
- Radix-2 FFT and bit reversal — part03_mathematics.topics.md — Signals and sequences — FFT named (line 217); bit reversal not checked
- Quadrature signals — part03c_signals_systems_and_communications.topics.md — Digital communications — Not checked by name (judgment)
- Discrete Hilbert transform — part03c_signals_systems_and_communications.topics.md — Digital filters and multirate processing — Not checked by name (judgment)
- Signal averaging — part03_mathematics.topics.md — Statistics and experimental design — Not checked by name (judgment)
- Fixed- and floating-point formats — part03_mathematics.topics.md — Numerical computing — Numerical computing named (line 187)
- Complex numbers, sinusoids, partial fractions — part03c_signals_systems_and_communications.topics.md — Signals and linear time-invariant systems — Not checked by name (judgment)
- Signal size (energy and power) — part03c_signals_systems_and_communications.topics.md — Signals and linear time-invariant systems — Not checked by name (judgment)
- Structures for discrete-time systems — part03c_signals_systems_and_communications.topics.md — Digital filters and multirate processing — Polyphase structures (line 32)
- Discrete Hilbert transforms — part03c_signals_systems_and_communications.topics.md — Digital filters and multirate processing — Not checked by name (judgment)
- Speech representations: LPC, cepstrum, MFCC, formants, pitch — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech science and analysis — Formants (lines 9, 11); MFCC in part03 (line 218); PLP not named
- Environmental robustness (CMN, PMC, VTS) — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech science and analysis — CMN, PMC, VTS (line 19); acoustic echo cancellation and arrays missing
- Cache, topic and maximum-entropy language models — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Classical NLP and toolkits — Not named in part19b; maximum-entropy distributions in part03 (line 78)
- Large-vocabulary search (lexical trees, N-best) — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech recognition: from HMMs to Kaldi — N-best (line 24); lexical trees missing
- Text analysis, normalization, letter-to-sound — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech synthesis, speakers and spoken-language systems — Not checked by name (judgment)
- Prosody (duration, pitch) — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech synthesis, speakers and spoken-language systems — Not checked by name (judgment)
- Entropy rates of stochastic processes — part03_mathematics.topics.md — Information theory — Not checked by name (judgment)
- Information theory and statistics — part03_mathematics.topics.md — Information theory — Not checked by name (judgment)
- Inequalities in information theory — part04_problem_solving.topics.md — Contest mathematics toolkit — Jensen's inequality (line 27); information inequalities not checked by name
- Probability distributions (binary variables) — part03_mathematics.topics.md — Probability — Not checked by name (judgment)
- Kernel methods — part19_machine_learning.topics.md — Classical machine learning — Kernels not checked by name (judgment)
- Sparse kernel machines (SVM, RVM) — part19_machine_learning.topics.md — Classical machine learning — SVMs covered; relevance vector machines missing
- Nonparametric techniques — part03_mathematics.topics.md — Statistics and experimental design — Nonparametric inference (line 117)
- Nonmetric methods — part19_machine_learning.topics.md — Classical machine learning — Not checked by name (judgment)
- Kernel smoothing — part19_machine_learning.topics.md — Classical machine learning — Not checked by name
- Practical methodology — part19_machine_learning.topics.md — Deep learning — Not checked by name (judgment)
- Constraint satisfaction problems — part19_machine_learning.topics.md — Classical AI: search, knowledge and reasoning — Not checked by name
- First-order logic and inference — part19_machine_learning.topics.md — Classical AI: search, knowledge and reasoning — Not checked by name
- Automated planning — part19_machine_learning.topics.md — Classical AI: search, knowledge and reasoning — Not checked by name
- Philosophy, ethics and safety — part19_machine_learning.topics.md — Foundations of AI — Not checked by name (judgment)
- Word sense disambiguation — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Classical NLP and toolkits — Not checked by name (judgment)
- Lexical acquisition — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Classical NLP and toolkits — Not checked by name (judgment)
- Probabilistic CFGs and probabilistic parsing — part19_machine_learning.topics.md — Natural language processing foundations — CKY parsing (line 127); PCFGs not named
- Statistical machine translation — part19_machine_learning.topics.md — Natural language processing foundations — Not checked by name (judgment)
- Training and decoding speedup (ADMM, async SGD, distillation) — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech recognition: from HMMs to Kaldi — Distillation (line 26); ADMM missing
- Sequence-discriminative training — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech recognition: from HMMs to Kaldi — Not checked by name
- Computational network — part19_machine_learning.topics.md — Deep learning — Not checked by name (judgment)
- Machine translation and encoder-decoder — part19_machine_learning.topics.md — Natural language processing foundations — Not checked by name (judgment)
- Conversation structure and dialogue acts — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md — Speech synthesis, speakers and spoken-language systems — Dialogue state tracking (line 44); dialogue acts not named
- Asset pipeline and resources — part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering — Not checked by name (judgment)
- Tools (version control, profilers) — part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering — Not checked by name (judgment)
- Engine support and memory — part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering — Not checked by name (judgment)
- Human input devices — part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering — Not checked by name (judgment)
- Collision and rigid body — part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering — Ray–primitive intersection (line 52); rigid body not named
- Audio — part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering — Not checked by name (judgment)
- Object models, events and scripting — part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering — Not checked by name (judgment)
- Texturing — part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering — Not checked by name (judgment)
- Global illumination — part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering — Not checked by name (judgment)
- Image-space effects (depth of field, tone mapping) — part30_supplementary_applied_domains.topics.md — Game engines and real-time rendering — Not checked by name (judgment)
- Class 6: integers and the number line — part01_school_foundations.topics.md:8 — Integers named (line 8); number line missing
- Class 7: profit, loss, discount — part01_school_foundations.topics.md:120 — Discounts only (line 120)
- Class 9: compound interest — part01_school_foundations.topics.md:120 — Simple interest only (line 120); compound not named
- Class 10: quadratic equations — part01_school_foundations.topics.md:31 — Quadratic functions named (line 31); equation solving not checked by name
- Class 10: remainder and factor theorems — part01_school_foundations.topics.md:62 — Factor theorem not checked by name
- Class 10: AP and GP — part03_mathematics.topics.md — Probability — Not checked by name (judgment)
- Class 10: trigonometric identities — part01_school_foundations.topics.md:55 — Not checked by name (judgment)
- Banking (compound interest, recurring deposits, amortization) — part30_supplementary_applied_domains.topics.md — Corporate finance — Recurring deposits and amortization (line 10); compound interest not named
- Quadratics (nature of roots) — part01_school_foundations.topics.md:31 — Not checked by name
- Factorization (factor theorem, remainder theorem) — part01_school_foundations.topics.md:62 — Factoring named (line 62)
- AP and GP — part03_mathematics.topics.md — Probability — Not checked by name (judgment)
- Language modeling: Chomsky hierarchy — part07 regular languages (line 63) Regular languages and pumping lemma only; the full hierarchy and language-model link not checked
