# Master Curriculum

Single syllabus of record. Every unique topic, textbook, chapter map, library, statistical technique, and IIT / upGrad lecture fact from the five source files lives here once.

Teaching brief: `mlo-instructions.md`.

## How to read this file

Each block is tagged:

| Tag | Meaning |
|---|---|
| `CORE` | Destination topics of the course |
| `PREREQ` | Taught first, because CORE topics depend on them |
| `TOOL` | Libraries and production tools, taught with the matching CORE/PREREQ slice |
| `ARCHIVE` | Kept so nothing is lost; not taught unless a real CORE dependency appears |

Source keys: `CUR` curriculum spine, `IIT` IIT GenAI master list, `DL` deep-learning module list, `LEC` IIT/upGrad lectures, `LIB` python-libs, `STAT` stat-tech, `BIB` bibliography / textbook deconstructions.

A book list appears in §1. Chapter maps appear in §2. The spine in §3 points at those books instead of repeating their tables of contents.

## Learning tracks and deferral policy

This file is intentionally broad so prior source work is not lost. Teaching is not equally broad. The active course follows three tracks:

1. **Primary destination track.** ML, LLMs, signal processing, image processing, NLP, Kaldi / ASR, neural networks, information theory, computer vision, GCP PMLE, IIT Kharagpur GenAI / Agentic AI, and the production systems needed to build and deploy them.
2. **Required support track.** Mathematics, Python, statistics, algorithms, and software practice taught because they unlock the primary destination track. This includes the necessary depth of algebra, calculus, linear algebra, probability, inference, optimization, transforms, spectral methods, information theory, automata, and numerical computing.
3. **Deferred enrichment track.** Material that is valuable but not currently load-bearing for the primary destination track: unrelated pure-math depth, PhD/research number theory, medical and mechanical inventories, game-engine/rendering tracks, unrelated software-web stacks, and any `ARCHIVE` topic.

Deferral is not deletion. Deferred material remains in the file for provenance and future expansion. Pull it back into teaching only when a primary destination topic genuinely depends on it, and then teach only the needed slice.

Advanced mathematics is not automatically deferred. Keep it active when it is load-bearing for ML, LLMs, DSP, image processing, ASR, NLP, information theory, computer vision, or production ML. Defer it when it becomes depth for its own sake.

---

# 1. Bibliography

## ICSE Mathematics Series (Classes 6–10)

- Concise Mathematics Series (Selina Publishers) — R.K. Bansal
- Understanding ICSE Mathematics — M.L. Aggarwal
- S. Chand’s ICSE Mathematics — O.P. Malhotra, S.K. Gupta, Anubhuti Gangal
- Frank Modern Certificate Mathematics — Nirmala Shastry
- Together With ICSE Mathematics — Rachna Sagar
- Foundation Mathematics (ICSE Edition) — R.S. Aggarwal

## NCERT Mathematics

- Mathematics Textbook for Class XI (2025–2026 edition)
- Mathematics Textbook for Class XII — Part I (2025–2026 edition)
- Mathematics Textbook for Class XII — Part II (2025–2026 edition)

## Higher Algebra and Classical Texts

- Higher Algebra — Hall & Knight
- Plane Trigonometry (Part 1) — S.L. Loney
- The Elements of Coordinate Geometry (Part 1) — S.L. Loney
- Problems in Calculus of One Variable — I.A. Maron
- Calculus — Michael Spivak

## JEE Advanced Reference Series

- Advanced Problems in Mathematics for JEE Main & Advanced — Vikas Gupta & Pankaj Joshi
- Cengage Mathematics Series (5 volumes: Algebra, Trigonometry, Coordinate Geometry, Calculus Part 1 & 2, Vectors & 3D) — G. Tewani
- Arihant Skills in Mathematics Series (7 volumes) — Dr. S.K. Goyal & Amit M. Agarwal

## Number Theory

- Elementary Number Theory (7th Edition) — David M. Burton
- A Friendly Introduction to Number Theory (4th Edition) — Joseph H. Silverman
- Elementary Number Theory and Its Applications — Kenneth H. Rosen
- An Introduction to the Theory of Numbers — Niven, Zuckerman, Montgomery
- An Introduction to the Theory of Numbers — G.H. Hardy & E.M. Wright
- A Course in Arithmetic — Jean-Pierre Serre
- Introduction to Analytic Number Theory — Tom M. Apostol
- Algebraic Number Theory — Serge Lang
- Elementary Number Theory in Nine Chapters — James J. Tattersall

## Proof and Abstract Algebra

- An Introduction to Proof via Inquiry-Based Learning — Dana C. Ernst
- Introduction to Proof — Ron Taylor
- Notes for a Course on Proofs — Jacqueline A. Jensen-Vallin
- Mathematical Reasoning: Writing and Proof — Ted Sundstrom
- Book of Proof (3rd Edition) — Richard Hammack
- An Inquiry-Based Approach to Abstract Algebra — Dana C. Ernst
- Abstract Algebra: Theory and Applications — Tom Judson

## Real Analysis and Measure Theory

- Introduction to Real Analysis — Dana C. Ernst
- Analysis — W. Ted Mahavier
- How We Got from There to Here: A Story of Real Analysis — Eugene Boman & Robert Rogers
- Real Analysis — Gary Towsley
- Analysis WebNotes — John Lindsay Orr
- Measure, Integration & Real Analysis — Sheldon Axler
- Principles of Mathematical Analysis — Walter Rudin

## Discrete Mathematics

- Discrete Mathematics and Its Applications — Kenneth H. Rosen
- Discrete and Combinatorial Mathematics: An Applied Introduction — Ralph P. Grimaldi

## Linear Algebra

- Introduction to Linear Algebra (5th Edition) — Gilbert Strang
- Linear Algebra and Its Applications — Gilbert Strang

## Higher Engineering Mathematics

- Higher Engineering Mathematics (44th/45th Edition) — B.S. Grewal
- Advanced Engineering Mathematics — Erwin Kreyszig

## Probability, Statistics, Inference

- Probability Theory: The Logic of Science — E.T. Jaynes
- All of Statistics — Larry Wasserman
- Statistical Inference — George Casella & Roger L. Berger

## Algorithms and Optimization

- Introduction to Algorithms — Cormen, Leiserson, Rivest, Stein
- Optimization by Vector Space Methods — David G. Luenberger

## Signals, Systems, Digital Signal Processing, Communications

- Signals and Systems — Alan V. Oppenheim & Alan S. Willsky
- Digital Signal Processing: Principles, Algorithms, and Applications — John G. Proakis & Dimitris G. Manolakis
- Understanding Digital Signal Processing — Richard G. Lyons
- Linear Systems and Signals — B.P. Lathi
- Discrete-Time Signal Processing — Alan V. Oppenheim & Ronald W. Schafer
- Digital Communications — John G. Proakis & Masoud Salehi

## Information Theory

- Elements of Information Theory — Cover & Thomas
- Information Theory, Inference, and Learning Algorithms — David J.C. MacKay

## Machine Learning and AI

- Pattern Recognition and Machine Learning — Christopher Bishop
- Pattern Classification (2nd Edition) — Richard O. Duda, Peter E. Hart, David G. Stork
- The Elements of Statistical Learning — Trevor Hastie, Robert Tibshirani, Jerome Friedman
- Deep Learning — Ian Goodfellow, Yoshua Bengio, Aaron Courville
- Artificial Intelligence: A Modern Approach — Stuart Russell & Peter Norvig
- Probabilistic Machine Learning: An Introduction — Kevin P. Murphy (2022)
- Reinforcement Learning: An Introduction (2nd Edition) — Richard S. Sutton & Andrew G. Barto
- Convex Optimization — Stephen Boyd & Lieven Vandenberghe
- Understanding Deep Learning — Simon J.D. Prince
- Dive into Deep Learning — Aston Zhang, Zachary C. Lipton, Mu Li, Alexander J. Smola

## Image Processing and Computer Vision

- Digital Image Processing (4th Edition) — Rafael C. Gonzalez & Richard E. Woods
- Computer Vision: Algorithms and Applications (2nd Edition, 2022) — Richard Szeliski
- Computer Vision: A Modern Approach (2nd Edition) — David A. Forsyth & Jean Ponce
- Multiple View Geometry in Computer Vision (2nd Edition) — Richard Hartley & Andrew Zisserman

## Information Retrieval

- Introduction to Information Retrieval — Christopher D. Manning, Prabhakar Raghavan, Hinrich Schütze

## Speech, Language, Weighted Automata

- Fundamentals of Speech Recognition — Lawrence Rabiner & Biing-Hwang Juang
- Spoken Language Processing — X. Huang, A. Acero, H.W. Hon
- Speech and Language Processing — Daniel Jurafsky & James H. Martin
- Foundations of Statistical Natural Language Processing — Christopher D. Manning & Hinrich Schütze
- Automatic Speech Recognition: A Deep Learning Approach — Dong Yu & Li Deng
- OpenFst Toolkit documentation and Kaldi graph-creation guidelines
- Discrete-Time Speech Signal Processing — Thomas F. Quatieri (full ToC in §2; speech-specific DSP for M41/M43)

## Automata (WFST prerequisite)

- Introduction to Automata Theory, Languages, and Computation — John E. Hopcroft, Rajeev Motwani, Jeffrey D. Ullman

## Production ML and Software Engineering

- Machine Learning Design Patterns — Valliappa Lakshmanan, Sara Robinson, Michael Munn
- Designing Machine Learning Systems — Chip Huyen
- Google Professional Machine Learning Engineer Official Syllabus (2026 Update)
- Software Engineering at Google — Titus Winters, Tom Manshreck, Hyrum Wright
- Effective Software Testing: A Developer’s Guide — Mauricio Aniche
- The Programmer’s Brain — Felienne Hermans
- Fundamentals of Software Architecture — Mark Richards & Neal Ford
- Refactoring: Improving the Design of Existing Code — Martin Fowler
- Learn React with TypeScript 3 — Carl Rippon
- Programming TypeScript — Boris Cherny

## Rendering and Game Engines

- Game Engine Architecture — Jason Gregory
- Real-Time Rendering — Tomas Akenine-Möller et al.

## Mechanical, Fluid, Aerospace

- Fluid Dynamics — M.D. Raisinghania
- Manufacturing Engineering and Technology — S.R. Schmid
- Theory of Mechanisms and Machines
- Introduction to Aerospace Engineering

## Clinical and Basic Medical Sciences

- Pathology: The Big Picture (2026 Update)
- Levinson’s Review of Medical Microbiology
- Jawetz, Melnick, & Adelberg’s Medical Microbiology
- LANGE Q&A: Physician Assistant Examination (8th Edition)
- AccessMedicine full suite (Anatomy & Physiology, Biochemistry, Microbiology, Pathology, Pharmacology, Clinical Diagnosis & Treatment, Radiology, and related collections)

---

# 2. Textbook deconstructions

Chapter, module, exercise, and topic maps. Each book appears once.

## Calculus — Michael Spivak

| Block | Topics |
|---|---|
| Prologue | 1. Basic Properties of Numbers. 2. Numbers of Various Sorts. |
| Foundations | 3. Functions; Appendix: Ordered Pairs. 4. Graphs; Appendix 1: Vectors; Appendix 2: The Conic Sections; Appendix 3: Polar Coordinates. 5. Limits. 6. Continuous Functions. 7. Three Hard Theorems. 8. Least Upper Bounds; Appendix: Uniform Continuity. |
| Derivatives and Integrals | 9. Derivatives. 10. Differentiation. 11. Significance of the Derivative; Appendix: Convexity and Concavity. 12. Inverse Functions; Appendix: Parametric Representation of Curves. 13. Integrals; Appendix: Riemann Sums. 14. The Fundamental Theorem of Calculus. 15. The Trigonometric Functions. 16. π is Irrational. 17. Planetary Motion. 18. The Logarithm and Exponential Functions. 19. Integration in Elementary Terms; Appendix: The Cosmopolitan Integral. |
| Sequences and Series | 20. Approximation by Polynomial Functions. 21. e is Transcendental. 22. Infinite Sequences. 23. Infinite Series. 24. Uniform Convergence and Power Series. 25. Complex Numbers. 26. Complex Functions. 27. Complex Power Series. |
| Epilogue | 28. Fields. 29. Construction of the Real Numbers. 30. Uniqueness of the Real Numbers. |
| Addenda | Answers to Selected Problems. Glossary of Symbols. Suggested Reading. |

## Principles of Mathematical Analysis — Walter Rudin

| Block | Topics |
|---|---|
| Ch. 1 Foundational systems | Ordered Sets, Fields, The Real Field, Extended Real Number System, The Complex Field, Euclidean Spaces, Appendix. |
| Ch. 2 Topology | Finite / countable / uncountable sets, Metric Spaces, Compact Sets, Perfect Sets, Connected Sets. |
| Ch. 3 Sequences and series | Convergent Sequences, Subsequences, Cauchy Sequences, Upper/Lower Limits, Special Sequences, Series of Nonnegative Terms, The Number e, Root and Ratio Tests, Power Series, Summation by Parts, Absolute Convergence, Addition/Multiplication of Series, Rearrangements. |
| Ch. 4 Continuity | Limits of Functions, Continuous Functions, Continuity and Compactness, Continuity and Connectedness, Discontinuities, Monotonic Functions, Infinite Limits / Limits at Infinity. |
| Ch. 5 Differentiation | Derivative of a Real Function, Mean Value Theorems, Continuity of Derivatives, L'Hospital's Rule, Higher-Order Derivatives, Taylor's Theorem, Differentiation of Vector-valued Functions. |
| Ch. 6 Integration | The Riemann-Stieltjes Integral: definition and existence, properties, integration and differentiation, vector-valued functions, rectifiable curves. |
| Ch. 7 Sequences and series of functions | Uniform Convergence; Uniform Convergence and Continuity / Integration / Differentiation; Equicontinuous Families; Stone-Weierstrass Theorem. |
| Ch. 8 Special functions | Power Series, Exponential and Logarithmic Functions, Trigonometric Functions, Algebraic Completeness, Fourier Series, The Gamma Function. |
| Ch. 9 Several variables | Linear Transformations, Differentiation, Contraction Principle, Inverse Function Theorem, Implicit Function Theorem, Rank Theorem, Determinants, Higher-Order Derivatives, Differentiation of Integrals. |
| Ch. 10 Differential forms | Primitive Mappings, Partitions of Unity, Change of Variables, Simplexes and Chains, Stokes' Theorem, Closed/Exact Forms, Vector Analysis. |
| Ch. 11 Lebesgue theory | Set Functions, Construction of Lebesgue Measure, Measure Spaces, Measurable Functions, Simple Functions, Integration, Comparison with Riemann, Complex Functions, Functions of Class L². |
| Addenda | End-of-chapter exercises (Ch. 1–11), Bibliography, List of Special Symbols. |

## Linear Algebra and Its Applications — Gilbert Strang

| Block | Topics |
|---|---|
| Linear systems | 1. Matrices and Gaussian Elimination (1.1–1.3). 2. Vector Spaces and Linear Equations (2.1 Vector Spaces and Subspaces, 2.2 m equations in n unknowns, 2.3 Linear Independence, Basis, Dimension). |
| Orthogonality and determinants | 3. Orthogonality (3.1 Perpendicular Vectors and Orthogonal Subspaces). 4. Determinants (4.1 Introduction). |
| Eigen theory | 5. Eigenvalues and Eigenvectors (5.1 Introduction, 5.2 Diagonalization, 5.3 Difference Equations and Powers A^k, 5.4 Differential Equations and e^{At}, 5.5 Complex Matrices, 5.6 Similarity Transformations). |
| Advanced applications | 6. Positive Definite Matrices (6.1 Minima, Maxima, Saddle Points). 7. Computations with Matrices. 8. Linear Programming and Game Theory (8.1 Linear Inequalities). |
| Appendices | Lorentz group; compactness criterion for finite dimensionality; characterization of commutators; Liapunov's stability criterion; Jordan Canonical form; Carl Pearcy's proof of Halmos' conjecture. |
| Addenda | End-of-chapter Review Exercises (e.g. Chapter 5). |

*Introduction to Linear Algebra* (5e) is the first-pass undergraduate text (ToC below). Use *Linear Algebra and Its Applications* for the chapter map above.

## Introduction to Linear Algebra — Gilbert Strang (5e)

MIT public ToC (`math.mit.edu/~gs/linearalgebra/ila5`):

1. Introduction to vectors — 1.1 Vectors and linear combinations; 1.2 Lengths and dot products; 1.3 Matrices  
2. Solving linear equations — 2.1 Vectors and linear equations; 2.2 The idea of elimination; 2.3 Elimination using matrices; 2.4 Rules for matrix operations; 2.5 Inverse matrices; 2.6 Elimination = factorization A = LU; 2.7 Transposes and permutations  
3. Vector spaces and subspaces  
4. Orthogonality  
5. Determinants  
6. Eigenvalues and eigenvectors  
7. The singular value decomposition (SVD)  
8. Linear transformations  
9. Complex vectors and matrices  
10. Applications  

Section numbers for Ch. 3–10 follow the same MIT page.

## Probability Theory: The Logic of Science — E.T. Jaynes

| Block | Topics |
|---|---|
| 1. Plausible reasoning | Deductive and plausible reasoning, analogies with physical theories, the thinking computer, the robot, Boolean algebra, adequate sets of operations, basic desiderata, common language vs formal logic. |
| 2. Quantitative rules | Product rule, sum rule, qualitative properties, numerical values, notation and finite-sets policy, subjective vs objective, Gödel's theorem, Venn diagrams, Kolmogorov axioms. |
| 3. Elementary sampling | Sampling without / with replacement, logic vs propensity, expectations, binomial distribution, correction for correlations. |
| 4. Elementary hypothesis testing | Prior probabilities, binary hypotheses, multiple hypothesis testing, continuous PDFs, simple and compound hypotheses. |
| 5. Queer uses | ESP, visual perception, discovery of Neptune, horse racing and weather, paradoxes of intuition, Bayesian jurisprudence. |
| 6. Parameter estimation | Inversion of urn distributions, uniform / truncated / concave / Jeffreys priors, predictive distributions, interval estimation, variance. |
| 7. Gaussian / normal | Herschel-Maxwell, Gauss, Landon derivations; error cancellation; convolution of Gaussians; CLT; Hermite polynomials; Fourier relations. |
| 8. Sufficiency | Fisher sufficiency, Blackwell-Rao, likelihood principle, ancillarity, Fisher information. |
| 9. Probability and frequency | Induction, multiplicity, entropy algorithms, entropy maximization, significance tests, chi-squared, Halley's mortality table. |
| 10. Physics of random experiments | Coin and die tossing, bridge hands, independence of tosses. |
| 11. Entropy principle | Shannon's theorem, Wallis derivation, maximum-entropy distributions. |
| 12. Ignorance priors | Location and scale, Poisson rate, Bertrand's problem. |
| 13–14. Decision theory | Bernoulli, Wald, loss functions, widget problem. |
| 15. Paradoxes | Nonconglomerability, finite vs countable additivity, Borel-Kolmogorov, marginalization paradox. |
| 16–17. Orthodox methods | Fisher, Jeffreys, Neyman; information loss, unbiased estimators, sampling variance. |
| 18. Rule of succession | Laplace, Carnap, exchangeable sequences, de Finetti. |
| 19–22 | Physical measurements; model comparison; outliers and robustness; communication theory (noiseless / noisy channel, optimum encoding). |
| Appendices | Other approaches to probability; mathematical formalities; convolutions and cumulants. References, author index, subject index. |

## All of Statistics — Larry Wasserman

| Block | Topics |
|---|---|
| Part I Probability | Sample spaces and events; random variables; distributions; expectations; inequalities; convergence; stochastic processes. |
| Part II Inference | Estimation, hypothesis testing, confidence intervals, method of moments. Ch. 9 Parametric Inference: MLE and its properties (consistency, equivariance, asymptotic normality, optimality), delta method, multiparameter models, parametric bootstrap, sufficiency, exponential families. Jackknife and percentile intervals. |
| Models and nonparametric | Nonparametric inference, curve estimation, density estimation, graphical EDA, classification, machine learning, data mining. |
| Addenda | End-of-chapter exercises (explicitly Ch. 8 and Ch. 9). |

## Statistical Inference — Casella & Berger

| Block | Topics |
|---|---|
| 1. Probability theory | Set theory. |
| 2. Transformations and expectations | Distribution of functions of a random variable; expected values. |
| 3. Common families | Discrete and continuous families; exponential family; location-scale family; inequalities and identities. |
| 4. Multiple random variables | Joint and marginal; conditional; bivariate random vectors. |
| 5. Random samples | Sampling from the normal; sample mean and variance; Student's t and Snedecor's F; order statistics; convergence in probability, almost sure, in distribution; delta method. |
| 6. Data reduction | Sufficiency, complete sufficient statistics, ancillary statistics, Basu's theorem. |
| 7–10 | Point estimation; hypothesis testing; interval estimation; asymptotic evaluations. |
| 11–12 | ANOVA and regression; functional/structural relationships; least squares; MLE; confidence sets; errors in variables; logistic regression; robust regression. |
| Addenda | 502 examples, 625 exercises. Appendix: Computer Algebra. Table of Common Distributions. References. Author and subject indexes. |

## Introduction to Algorithms — CLRS

| Block | Topics |
|---|---|
| Foundations | 1. Role of algorithms. 2. Getting Started (insertion sort, analyzing and designing algorithms). 3. Asymptotic notation (O, Ω, Θ). 4. Divide-and-conquer (matrix multiply, Strassen, substitution / recursion-tree / master / Akra-Bazzi methods). 5. Probabilistic analysis and randomized algorithms. |
| Sorting | 6. Heapsort and priority queues. 7. Quicksort. 8. Linear-time sorts (counting, radix, bucket). 9. Medians and order statistics. |
| Data structures | 10. Stacks, queues, linked lists. 11. Hash tables (open addressing). 12. BSTs. 13. Red-black trees. 17. Augmenting data structures. 18. B-trees. 19. Disjoint sets. |
| Design | 14. Dynamic programming. 15. Greedy algorithms. 16. Amortized analysis. |
| Graphs | 20. Representations and traversals. 21. MSTs (Prim, Kruskal). 22. Single-source shortest paths (Bellman-Ford, Dijkstra). 23. All-pairs (Floyd-Warshall). 24. Maximum flow. 25. Bipartite matching. |
| Advanced | 31. Number-theoretic algorithms (GCD, modular arithmetic, CRT, RSA, primality). 35. Approximation algorithms (vertex cover, TSP, set cover, subset-sum). |
| Appendix C | Counting, probability, discrete RVs, geometric and binomial, binomial tails. |
| Addenda | 4th edition: 140 new exercises and 22 new problems. |

## Optimization by Vector Space Methods — Luenberger

| Block | Topics |
|---|---|
| 1–6 Spaces | Introduction; linear spaces; Hilbert space; approximation and Fourier series; least-squares estimation; dual spaces (Hahn-Banach, extension and geometric forms). |
| 7–8 Operators | Linear operators and adjoints; optimization of functionals. |
| 9 Constrained | Global and local constrained optimization; inequality constraints; Kuhn-Tucker. |
| 10–11 Control and iteration | Pontryagin maximum principle; successive approximation; Newton; steepest descent; conjugate directions; conjugate gradient; projection methods. |
| Addenda | End-of-chapter problems, symbol index. |

## Advanced Engineering Mathematics — Kreyszig

| Block | Topics |
|---|---|
| Part A ODEs | Ch. 1 First-order. Ch. 2 Second-order linear. Ch. 3 Higher-order linear. Ch. 4 Systems. Ch. 5 Series solutions (Frobenius, Bessel). Ch. 6 Laplace transforms. |
| Part B Linear algebra and vector calculus | Ch. 7 Matrices, vectors, determinants. Ch. 8 Eigenvalue problems. Ch. 9 Vector differential calculus. Ch. 10 Vector integral calculus. |
| Parts C–D | Ch. 11 Fourier analysis. Ch. 12 PDEs. |
| Part E Complex analysis | Ch. 13–17. Ch. 14 Complex integration (Cauchy theorem and formula). Ch. 18 Potential theory (electrostatics, conformal mapping, heat, fluid flow, Poisson integral, uniqueness for Dirichlet). |
| Part F Numerics | Ch. 19–20. Ch. 21 Numerics for ODEs and PDEs (multistep, elliptic / parabolic / hyperbolic, Neumann and mixed, irregular boundary). |
| Parts G and probability | Ch. 22–23 Optimization and graphs. Ch. 24–25 Probability and statistics. |
| Addenda | Review questions and problems; CAS projects and experiments. |

## Digital Signal Processing — Proakis & Manolakis

| Block | Topics |
|---|---|
| 1. Introduction | Signals, systems, DSP elements, analog vs digital. Classification: multichannel, multidimensional, continuous/discrete time, continuous/discrete valued, deterministic vs random. |
| 2. Discrete-time LTI | Impulse resolution, convolution sum and properties, interconnection, causality, stability, FIR/IIR, difference equations, correlation (auto, cross, periodic). |
| 3. z-transform | Direct and inverse, properties, rational transforms, poles/zeros, contour integration, power series, one-sided z-transform, difference-equation solution. |
| 4. Frequency analysis | Continuous and discrete sinusoids, Fourier series (periodic), FT (aperiodic), power and energy density spectra, relation to z-transform, cepstrum, bandwidth, STFT. |
| 5. Frequency-domain LTI | Frequency response, rational system functions, correlation and spectra, filters, inverse systems, deconvolution, reverberation. |
| 6. Sampling | Ideal sampling and reconstruction, discrete-time processing of continuous-time signals, bandpass sampling, A/D and D/A, oversampling. |
| 7. DFT | Properties, Goertzel, chirp-z, quantization errors, sparse FFT. |
| 8. Implementation | FIR structures (direct, cascade, frequency-sampling), fixed- and floating-point, rounding/truncation, coefficient quantization, limit cycles, scaling. Multirate filter banks and wavelets. |
| Addenda | 500+ end-of-chapter problems, MATLAB computer problems. |

## Digital Communications — Proakis & Salehi

1. Channel models, historical perspective. 2. Deterministic and random signal analysis (bandpass/lowpass, signal space, Gram-Schmidt, random processes, Karhunen-Loève). 3. Modulation (PAM, PSK, QAM, CPFSK, CPM). 4. Optimum receivers for AWGN. 5. Carrier and symbol synchronization (PLL). 6. Information theory (entropy, mutual information, rate distortion). 7. Linear block codes. 8. Trellis and graph codes. 9. Band-limited channels. 10. Adaptive equalization. 11. Multichannel / multicarrier. 12. Spread spectrum. 13–14. Fading (Ricean/Rayleigh, capacity and coding). 15. Multiple antennas. 16. Multiuser communications.

## Understanding Digital Signal Processing — Lyons

1. Discrete sequences and LTI systems. 2. Periodic sampling and aliasing. 3. DFT (leakage, windows, scalloping, zero padding). 4. Radix-2 FFT, bit reversal, butterflies. 5. FIR filters (Parks-McClellan, half-band). 6. IIR (impulse invariance, bilinear transform). 7. Specialized networks (differentiators, integrators, matched filters, CIC). 8. Quadrature signals. 9. Discrete Hilbert transform. 10. Sample-rate conversion (decimation, interpolation, polyphase). 11. Signal averaging. 12. Fixed- and floating-point formats. 13. DSP tricks (frequency translation without multiplication, linear interpolation).

## Signals and Systems — Oppenheim & Willsky

Signals and systems; LTI systems; Fourier series and transforms (continuous and discrete); sampling; communication systems; Laplace transform; z-transform; linear feedback.

## Linear Systems and Signals — B.P. Lathi (3e, with Roger Green)

OUP / dokumen.pub / Quizlet:

- **B Background** — B.1 Complex numbers; B.2 Sinusoids; B.3 Sketching signals; B.4 Cramer's rule; B.5 Partial fractions; B.6 Vectors and matrices; B.7 MATLAB elementary operations; B.8 Useful formulas  
- **1 Signals and systems** — size of a signal (energy/power); time shift/scale/reversal; classification; step/impulse/exponential; even/odd; system classes (linear, TI, causal, BIBO, …)  
- **2 Time-domain analysis of continuous-time systems** — zero-input response; impulse response; convolution; stability; time constant / resonance  
- **3 Time-domain analysis of discrete-time systems** — discrete impulse/step/exponential; difference equations; convolution sum; stability  
- **4 Continuous-time system analysis using the Laplace transform**  
- **5 Discrete-time system analysis using the z-transform**  
- **6 Continuous-time signal analysis: the Fourier series**  
- **7 Continuous-time signal analysis: the Fourier transform**  
- **8 Discrete-time signal analysis** (DTFS / DTFT family; Quizlet/dokumen signal-analysis block Ch. 6–9)  
- **9 Sampling and discrete Fourier analysis**  
- **10 State-space analysis of LTI systems**  

## Discrete-Time Signal Processing — Oppenheim & Schafer (3e)

Pearson + Quizlet chapter list:

1. Introduction  
2. Discrete-time signals and systems  
3. The z-transform  
4. Sampling of continuous-time signals  
5. Transform analysis of LTI systems  
6. Structures for discrete-time systems  
7. Filter design techniques  
8. The discrete Fourier transform  
9. Computation of the discrete Fourier transform  
10. Fourier analysis of signals using the DFT  
11. Parametric signal modeling  
12. Discrete Hilbert transforms

## Spoken Language Processing — Huang, Acero, Hon

Book contents (Academia ToC; SearchWorks / Kyobo for front matter). Each chapter ends with Historical Perspective and Further Reading.

**I Fundamental theory**  
1. Introduction — motivations; spoken language system architecture  
2. Spoken language structure — sound and human speech systems; phonetics and phonology; syllables and words; syntax and semantics  
3. Probability, statistics, and information theory  
4. Pattern recognition — Bayes, discriminative training, EM, CART  

**II Speech processing**  
5. Digital signal processing — digital signals and systems; DFT/FFT; FIR/IIR; filterbanks  
6. Speech signal representations — short-time Fourier analysis; LPC; cepstrum; MFCC; PLP; formants; pitch  
7. Speech coding — PCM, µ-law, transform coders, CELP, low-bit-rate vocoders  

**III Speech recognition**  
8. Hidden Markov models — Markov chain, forward, Viterbi, Baum–Welch; continuous and semi-continuous HMMs  
9. Acoustic modeling — units and context; MAP / MLLR; confidence; Whisper case  
10. Environmental robustness — noise and reverberation; AEC; arrays; CMN; PMC; VTS  
11. Language modeling — Chomsky hierarchy; n-grams; smoothing; cache / topic / maxent  
12. Basic search algorithms — graph search; Viterbi beam; stack / A*  
13. Large vocabulary search algorithms — lexical trees; N-best; multipass; Whisper case  

**IV Text-to-speech systems**  
14. Text and phonetic analysis — lexicon, normalization, letter-to-sound; Festival case  
15. Prosody — symbolic prosody, duration, pitch  
16. Speech synthesis — formant, concatenative, PSOLA  

**V Spoken language systems**  
17. Spoken language understanding — frames, dialog, Dr. Who case  
18. Applications and user interfaces

## Elements of Information Theory — Cover & Thomas (2e)

1. Introduction and preview  
2. Entropy, relative entropy, and mutual information  
3. Asymptotic equipartition property  
4. Entropy rates of a stochastic process  
5. Data compression  
6. Gambling and data compression  
7. Channel capacity  
8. Differential entropy  
9. Gaussian channel  
10. Rate distortion theory  
11. Information theory and statistics  
12. Maximum entropy  
13. Universal source coding  
14. Kolmogorov complexity  
15. Network information theory  
16. Information theory and portfolio theory  
17. Inequalities in information theory  


## Pattern Recognition and Machine Learning — Bishop

1. Introduction (polynomial curve fitting). 2. Probability distributions (binary variables). 3. Linear models for regression. 4. Linear models for classification. 5. Neural networks. 6. Kernel methods. 7. Sparse kernel machines. 8. Graphical models. 9. Mixture models and EM. 10. Approximate inference. 11. Sampling methods. 12. Continuous latent variables. 13. Sequential data. 14. Combining models. Addenda: 431 graded exercises, solutions manual, figures, errata.

## Pattern Classification — Duda, Hart, Stork (2e)

Wiley / Google Books contents:

1. Introduction — machine perception, pattern recognition systems  
2. Bayesian decision theory  
3. Maximum-likelihood and Bayesian parameter estimation  
4. Nonparametric techniques  
5. Linear discriminant functions  
6. Multilayer neural networks  
7. Stochastic methods  
8. Nonmetric methods  
9. Algorithm-independent machine learning  
10. Unsupervised learning and clustering

## The Elements of Statistical Learning — Hastie, Tibshirani, Friedman

1. Introduction. 2. Overview of supervised learning. 3. Linear methods for regression. 4. Linear methods for classification. 5. Basis expansions and regularization (phoneme recognition, smoothing splines, bias-variance, RKHS). 6. Kernel smoothing. 7. Model assessment and selection. 8. Model inference and averaging. 9. Additive models, trees. 10. Boosting and additive trees. 11. Neural networks (Bayesian NNs). 12. SVMs and flexible discriminants. 13. Prototype methods and nearest neighbors. 14. Unsupervised learning (clustering, k-means, spectral clustering). 15. Random forests. 16. Ensemble learning. 17. Undirected graphical models. 18. High-dimensional problems (wide data, multiple testing, FDR).

## Deep Learning — Goodfellow, Bengio, Courville

- Part I: Applied math and ML basics — 1 Introduction; 2 Linear algebra; 3 Probability and information theory; 4 Numerical computation; 5 Machine learning basics.
- Part II: Modern practices — 6 Deep feedforward networks; 7 Regularization; 8 Optimization for training; 9 Convolutional networks; 10 Sequence modeling (RNN/recursive); 11 Practical methodology; 12 Applications (CV, speech, NLP).
- Part III: Research — 13 Linear factor models; 14 Autoencoders; 15 Representation learning; 16 Structured probabilistic models; 17 Monte Carlo; 18 Partition function; 19 Approximate inference; 20 Deep generative models.

## Artificial Intelligence: A Modern Approach — Russell & Norvig

- Part I: 1 Introduction; 2 Intelligent agents.
- Part II Problem-solving: 3 Searching; 4 Complex environments; 5 CSPs; 6 Adversarial search and games (MCTS).
- Part III Knowledge: 7 Logical agents; 8 First-order logic; 9 FOL inference; 10 Knowledge representation; 11 Automated planning.
- Part IV Uncertainty: 12 Quantifying uncertainty; 13 Probabilistic reasoning; 14 Reasoning over time; 15–16 Decisions; 17 Multiagent decisions; 18 Probabilistic programming.
- Part V ML: 19 Learning from examples; 20 Knowledge in learning; 21 Learning probabilistic models; 22 Deep learning; 23 Reinforcement learning.
- Part VI: 24 NLP; 25 Deep learning for NLP; 26 Robotics; 27 Computer vision.
- Part VII: 28 Philosophy, ethics, safety; 29 Future of AI.
- Appendices: mathematical background; languages and algorithms. Implementations: aima-python, aima-java, aima-exercises, aima-pseudocode.

## Foundations of Statistical Natural Language Processing — Manning & Schütze

Stanford FSNLP brief contents:

**I Preliminaries** — 1 Introduction; 2 Mathematical foundations; 3 Linguistic essentials; 4 Corpus-based work  
**II Words** — 5 Collocations; 6 Statistical inference: n-gram models over sparse data; 7 Word sense disambiguation; 8 Lexical acquisition  
**III Grammar** — 9 Markov models; 10 Part-of-speech tagging; 11 Probabilistic CFGs; 12 Probabilistic parsing  
**IV Applications** — 13 Statistical alignment and machine translation; 14 Clustering; 15 Topics in information retrieval; 16 Text categorization  

## Automatic Speech Recognition: A Deep Learning Approach — Yu & Deng

Springer book contents (15 chapters; author PDF ToC + Li Deng chapter index):

**I Conventional acoustic models**  
1. Introduction  
2. Gaussian mixture models  
3. Hidden Markov models and the variants  

**II Deep neural networks**  
4. Deep neural networks — architecture, error backpropagation  
5. Advanced model initialization techniques — RBMs, DBN pretraining, denoising autoencoder, discriminative / hybrid / dropout pretraining  

**III DNN–HMM hybrid systems for ASR**  
6. Deep neural network–hidden Markov model hybrid systems — CD-DNN-HMM architecture, decoding, training  
7. Training and decoding speedup — pipelined BP, async SGD, ADMM, sparse / low-rank nets, distill small DNN  
8. Deep neural network sequence-discriminative training  

**IV Representation learning in deep neural networks**  
9. Feature representation learning in deep neural networks  
10. Fuse deep neural network and Gaussian mixture model systems  
11. Adaptation of deep neural networks  

**V Advanced deep models**  
12. Representation sharing and transfer in deep neural networks — multitask / transfer, multilingual DNN, audio-visual  
13. Recurrent neural networks and related models — BPTT, LSTM, contrast with hidden dynamic models  
14. Computational network — forward compute, node types, CNN and recurrent connections  
15. Summary and future directions  

Complements Rabiner (classical) and Kaldi M43–M44.

## Speech and Language Processing — Jurafsky & Martin

- Volume I LLMs: 1 Introduction. 2 Words and tokens (Unicode, regex, normalization, corpora, minimum edit distance). 3 N-gram LMs (perplexity). 4 Logistic regression and text classification (Naive Bayes, sentiment). 5 Vector semantics and embeddings (TF-IDF, bias). 6 Neural networks. 7 Large language models. 8 Transformers. 9 Post-training (instruction tuning, alignment, test-time compute, DPO). 10 Masked LMs. 11 IR and RAG. 12 MT and encoder-decoder. 13 RNNs and LSTMs. 14 Phonetics and speech features. 15 ASR. 16 TTS.
- Volume II Structure: 17 Sequence labeling (POS, NER, HMM, CRF). 18 CFGs and constituency parsing. 19 Dependency parsing. 20 Information extraction. 21 Semantic role labeling. 22 Sentiment lexicons. 23 Coreference and entity linking (Winograd, gender bias). 24 Discourse coherence (RST, PDTB, entity grid). 25 Conversation structure.
- Web supplements: HMM, Naive Bayes, Kneser-Ney, noisy-channel spelling, statistical constituency, CCG, logical meaning, WordNet, PPMI, frame-based dialogue.

## Game Engine Architecture — Jason Gregory

I Foundations: 1 Game / engine / genre survey, runtime architecture, asset pipeline. 2 Tools (VCS, compilers, profilers, leak detection). 3 SE for games (C++, memory layout, hardware). 4 Parallelism (threads, lock-free, SIMD, GPGPU). 5 3D math (vectors, matrices, quaternions, RNG). II Low-level: 6 Engine support and memory. 7 Resources and filesystem. 8 Game loop. 9 HIDs. III Graphics, motion, sound: 11 Rendering. 12 Animation. 13 Collision and rigid body. 14 Audio. IV Gameplay: 14–15 Object models, streaming, events, scripting. V Conclusion.

## Real-Time Rendering — Akenine-Möller et al.

1 Introduction. 2 Graphics pipeline. 3 GPU. 4 Transforms. 5 Shading basics. 6 Texturing. 7 Shadows. 8 Light and color. 9 PBR. 10 Local illumination. 11 Global illumination (light baking, BRDFs, water). 12 Image-space effects (DoF, tone mapping, motion blur). 13 Beyond polygons (particles, point clouds). 14 Volumetric and translucency. 15 NPR and style transfer. 16 Polygonal techniques, photogrammetry. 17 Curves and curved surfaces. 18 Pipeline optimization. 19 Acceleration. 20 Efficient shading. 21 VR/AR. 22 Intersection tests. 23 Graphics hardware. 24 Future. Online: 25 Collision; 26 Real-time ray tracing. Appendices: linear algebra and trigonometry.

## ICSE / Selina Concise (Classes 6–10)

**Class 6.** Ch. 1 Number System (greater/smaller, ascending/descending, Ex 1A). 2 Estimation. 3 Indian and International systems. 4 Place value (local value, Ex 4A, 4B). 5 Natural and whole numbers (closure, commutative, distributive). 6 Negative numbers and integers. 7 Number line. 9 Playing with numbers (BODMAS, factors, divisibility). 10 Sets (roster, set-builder, Ex 10A, 10B). 13 Unitary method. 14 Fractions. 17 Speed, distance, time. 18–22 Algebra: fundamental concepts and operations, substitution, framing expressions, simple linear equations.

**Class 7.** Integers, rationals, fractions, decimals, exponents, ratio/proportion, unitary method, percent, profit/loss/discount, simple interest, linear equations, sets, lines/angles, triangles, Pythagoras, symmetry, solids, congruency, mensuration, data handling, probability.

**Class 8.** Rationals, exponents, squares/cubes and roots, playing with numbers, sets, percentage, simple/compound interest, direct/inverse variation, algebraic identities, factorisation, linear equations/inequalities, quadrilaterals, constructions, circle, symmetry (reflection/rotation), solid shapes, mensuration, data handling.

**Class 9.** Rational/irrational numbers, compound interest, expansions, factorisation, simultaneous linear equations, indices, logarithms, triangle congruency and isosceles triangles, inequalities, mid-point theorem, similarity, rectilinear figures, Pythagoras, area, circle, graphical statistics, trigonometric ratios of standard angles, right-triangle solutions, heights and distances.

**Class 10.** 1 GST (computation, ITC, Ex 1A, 1B). 2 Banking (RD accounts). 3 Shares and dividend (premium, discount, Ex 3A–3C). 4 Linear inequations. 5 Quadratic equations (factorisation, formula). 6 Problems on quadratics (Ex 6A–6C). 7 Ratio and proportion. 8 Remainder and factor theorems. 9 Matrices (order, types, transpose, equality). 10 AP. 11 GP. 12 Reflection (Ex 12A). 13 Section and mid-point formula. 14 Equation of a line. 15 Similarity. 16 Loci. 17 Circles. 18 Tangents and intersecting chords. 19 Constructions. 20 Cylinder, cone, sphere. 21 Trigonometric identities. 22 Heights and distances. 23 Graphical representation. 24 Measures of central tendency. 25 Probability.

## Understanding ICSE Mathematics — M.L. Aggarwal (Class 10)

| Chapter | Concepts | Exercise metrics |
|---|---|---|
| 1. VAT / GST | Intra/inter-state, CGST, SGST, IGST, ITC, final price | Ex 1.1, 1.2 |
| 2. Banking | CI, recurring deposits, loan amortization, maturity | — |
| 3. Shares and dividends | Premium/discount purchase, dividend | — |
| 4. Linear inequations | Combining inequalities, product of two linear expressions, representation | — |
| 5. Quadratics | Reducible equations, factorisation, nature of roots, Shreedharacharya | — |
| 6. Factorization | Factor theorem, division algorithm, remainder theorem, grouping, difference of squares | — |
| 7. Ratio and proportion | Composition, continued proportion, componendo-dividendo, direct/inverse | Ex 7.1 (45), 7.2 (56), 7.3 (29), MCQs (10), Chapter Test (25) |
| 8. Matrices | Compatibility, equality, operations, properties, transpose, types | Ex 8.1 (17), 8.2 (17), 8.3 (44), MCQs (14), Chapter Test (17) |
| 9. AP and GP | AM, GM, general term, finite sums | Ex 9.1 (19), 9.2 (39), 9.3 (26), 9.4, 9.5, MCQs, Chapter Test |
| 10. Reflection | Across x-axis, y-axis, y=x | — |
| 11. Section formula | Coordinate applications | — |
| 12. Straight line | Slope, forms, inclination, intercepts, parallel/perpendicular | — |
| 13. Similarity | BPT, AAA, SAS, area ratios, maps/models | — |
| 14. Locus | Perpendicular bisector, angle bisectors, fixed distance | — |
| 15. Circles | Arc, chord, cyclic quad, concyclic, tangents, angle theorems | — |
| 16. Constructions | Circumcircle, incircle, tangents, regular polygon | — |
| 17. Mensuration | Surface area and volume | — |
| 18–20. Trigonometry | Identities, tables, heights and distances | — |
| 21. Central tendency | Mean, median, mode | — |
| 22. Probability | Event likelihood | — |

## NCERT Mathematics (Classes 11–12)

**Class 11** (NCERT 2025–26 rationalized list + `kemh1ps` sections for Ch. 1–3):

1. Sets — 1.1 Introduction; 1.2 Representations; 1.3 Empty set; 1.4 Finite and infinite; 1.5 Equal sets; 1.6 Subsets; 1.7 Universal set; 1.8 Venn diagrams; 1.9 Operations; 1.10 Complement  
2. Relations and functions — Cartesian product, relations, functions  
3. Trigonometric functions — angles, functions, sum and difference  
4. Complex numbers and quadratic equations  
5. Linear inequalities  
6. Permutations and combinations  
7. Binomial theorem  
8. Sequences and series  
9. Straight lines  
10. Conic sections  
11. Introduction to three-dimensional geometry  
12. Limits and derivatives  
13. Statistics  
14. Probability  

(Older induction / mathematical-reasoning chapters were dropped in the rationalized edition.)

**Class 12 Part I:** 1 Relations and functions; 2 Inverse trigonometric functions; 3 Matrices; 4 Determinants; 5 Continuity and differentiability; 6 Application of derivatives; 7 Integrals; 8 Application of integrals.

**Class 12 Part II:** 9 Differential equations; 10 Vector algebra; 11 Three-dimensional geometry; 12 Linear programming; 13 Probability.

## Hall & Knight — Higher Algebra

Ratio, proportion, variation; AP, GP (insertion of means, infinite sum), HP; theorems on progressions; scales of notation; surds and imaginaries; theory of quadratic equations; miscellaneous equations; permutations and combinations; mathematical induction; binomial and multinomial theorems; logarithms; exponential and logarithmic series; interest and annuities; inequalities; limiting values and vanishing fractions; convergency and divergency of series; undetermined coefficients; partial fractions; recurring series; continued fractions; indeterminate equations of first and second degree; recurring continued fractions; summation of series (method of differences); theory of numbers; general theory of continued fractions; probability; determinants; miscellaneous theorems; theory of equations.

## S.L. Loney — Plane Trigonometry

Trigonometric ratios, domain and range, graphs, inverse functions, identities.

## S.L. Loney — The Elements of Coordinate Geometry

1. Introduction (algebraic results, quadratics, determinants, elimination). 2. Coordinates (lengths, triangle areas). 3. Locus. 4. Straight line (rectangular). 5. Straight line (polar, oblique). 6. Two or more straight lines. 7. Transformation of coordinates. 8. The circle. 9. Systems of circles (orthogonal, radical axis, coaxal). 10–11. Parabola (tangents, normals, diameters, loci). 12. Ellipse (auxiliary circle, eccentric angle, conjugate diameters, four normals). 13. Hyperbola (asymptotes). 14. Polar equation of a conic. 15. General equation / tracing. 17. Miscellaneous propositions.

## I.A. Maron — Problems in Calculus of One Variable

Introduction to analysis; function; limit; continuity; derivative and differential calculus; investigating functions and graphs; definite integral; indefinite integral; methods for definite integrals; improper integrals; applications; series; functions of several variables.

## JEE series chapter maps

**Vikas Gupta & Pankaj Joshi.** Function; limit, continuity, derivative; definite / indefinite integral; area; DEs; series; coordinate geometry (2D and 3D); vector algebra.

**Cengage (Tewani), 5 volumes.**

- Algebra: sets and reals, theory of equations, complex numbers, progressions, inequalities of means, PnC, binomial, probability I, statistics, determinants, matrices, probability II.
- Calculus: relations and functions, limits, differentiation, continuity and differentiability, AoD, monotonicity and max/min, indefinite / definite integration, area, DEs.
- Trigonometry: logarithm, trig functions, transformation formulas, equations, inverse trig.
- Coordinate geometry: coordinate system, straight lines, pair of lines, circle, parabola, ellipse, hyperbola.
- Vectors & 3D: 3D geometry, vectors, products, line and plane.

**Arihant Skills (Goyal & Agarwal), 7 volumes.**

- Algebra: complex numbers, theory of equations, sequences, logarithms, PnC, binomial, determinants, matrices, probability, induction, sets, relations and functions.
- Coordinate geometry: coordinates, straight lines, pair of lines, circle, parabola, ellipse, hyperbola.
- Differential calculus: tools, differentiation, functions, graphical transformations, limits, continuity/differentiability, rate measure, tangents/normals, monotonicity, max/min.
- Integral calculus: indefinite, definite, area, DEs (Bernoulli, first-order higher degree).
- Trigonometry: functions and identities, equations and inequations, properties of triangles, inverse trig.
- Vectors & 3D: vector algebra, point/line/plane, products.
- Play with Graphs: graphs, curvature, transformations, asymptotes, singular points, curve tracing.
- Assessment: Practice Milestone 1 (JEE Main), 2 (JEE Advanced), 3 (challenging), JEE Scanner PYQs; single correct, multi-correct, comprehension, matrix match, numerical value.

## Elementary Number Theory — Burton

Preliminaries; divisibility; GCD; Diophantine equations; primes (FTA, Goldbach); congruences (CRT); Fermat; number-theoretic functions (Möbius inversion); Euler; primitive roots; quadratic reciprocity; cryptography; special forms (perfect, Mersenne, amicable); Fermat's Last Theorem; Fibonacci; continued fractions; primality testing; zeta function.

## A Friendly Introduction to Number Theory — Silverman

Pythagorean triples and the unit circle; sums of higher powers; divisibility and GCD; factorization; congruences; Euler; primitive roots; discrete logs; quadratic reciprocity; Pell; elliptic curves; ABC conjecture.

## An Introduction to the Theory of Numbers — Hardy & Wright

I–II Series of primes (Euclid, Fermat and Mersenne numbers, FTA). III Farey series and Minkowski. IV Irrational numbers. V Congruences and residues (φ(m), trigonometrical sums, regular polygons). VI Fermat and consequences (Wilson, Gauss's lemma, reciprocity, primality tests). VII General properties of congruences (Wolstenholme, von Staudt). VIII Congruences to composite moduli. IX Decimal representation. X Continued fractions. XI Approximation.

## A Course in Arithmetic — Serre

Part I Algebraic: I Finite fields and quadratic reciprocity. II p-adic fields (ℤ_p, ℚ_p). III Hilbert symbol. IV Quadratic forms over ℚ_p and ℚ (Hasse-Minkowski, sums of three squares). V Integral quadratic forms of discriminant ±1. Part II Analytic: VI Dirichlet's theorem on arithmetic progressions. VII Modular forms (theta, Eisenstein, cusp forms).

## An Introduction to the Theory of Numbers — Niven, Zuckerman, Montgomery

Ch. 1 Elementary review (divisibility, GCD, LCM, primes, congruences, CRT, special congruences, lifting the exponents, primitive roots, quadratic residues). Hensel's lemma. 2.10 Algebraic viewpoint. 2.11 Groups, rings, fields. Ch. 3 Quadratic reciprocity and forms (Jacobi symbol, binary quadratic forms). Simultaneous linear Diophantine systems. Rational points on curves. Elliptic curves.

## Elementary Number Theory in Nine Chapters — Tattersall

1. Natural numbers (polygonal, sequences, induction). 2. Divisibility (division algorithm, GCD, Euclidean algorithm, Pythagorean triples). 3. Primes (Euclid, arithmetic functions, multiplicative functions, factoring, greatest integer). 4. Perfect, Fermat, amicable numbers. 5. Modular arithmetic (congruence, divisibility criteria, φ, linear congruences). 6. Higher-degree congruences, quadratic congruences, primitive roots. 7. Cryptology (mono/polyalphabetic, knapsack, block, exponential). 8. Representations (sums of squares, Pell, binary quadratic forms, finite/infinite continued fractions, p-adic). 9. Partitions (generating functions, pentagonal number theorem). Tables: symbols, primes < 10 000, function values.

## Introduction to Analytic Number Theory — Apostol

Dirichlet series, arithmetical functions, Prime Number Theorem formulations.

## Discrete Mathematics — Rosen

Logic, proofs, sets, functions, relations, graphs, trees, Boolean algebra, modeling computation, number theory, counting (addition and multiplication principles), probability, recurrence relations, combinatorics.

## Discrete and Combinatorial Mathematics — Grimaldi

Combinatorics, counting principles, permutations and combinations (with repetition), inclusion-exclusion, finite state machines, logic, set theory, generating functions, recurrence relations, graph theory, modern applied algebra, Catalan numbers, binomial coefficients, pigeonhole principle.

## Higher Engineering Mathematics — Grewal

Algebra, determinants/matrices, vector algebra, differential/integral calculus, DEs, complex analysis, probability/statistics, numerical techniques, Fourier series/transforms, Laplace/Z-transforms, special functions, PDEs, engineering applications.

## Book of Proof — Richard Hammack (3e)

Part I Fundamentals: Ch. 1 Sets; Ch. 2 Logic; Ch. 3 Counting.  
Part II Proving conditional statements: Ch. 4 Direct proof; Ch. 5 Contrapositive proof; Ch. 6 Proof by contradiction.  
Part III More on proof: Ch. 7 Proving non-conditional statements; Ch. 8 Proofs involving sets; Ch. 9 Disproof; Ch. 10 Mathematical induction.  
Part IV Relations, functions, cardinality: Ch. 11 Relations; Ch. 12 Functions; Ch. 13 Proofs in calculus; Ch. 14 Cardinality of sets.

## Digital Image Processing — Gonzalez & Woods (4e)

1. Introduction — what DIP is, origins, example fields  
2. Digital image fundamentals — visual perception, sampling and quantization  
3. Intensity transformations and spatial filtering  
4. Filtering in the frequency domain  
5. Image restoration and reconstruction  
6. Color image processing  
7. Wavelets and other image transforms / multiresolution  
8. Image compression and watermarking  
9. Morphological image processing  
10. Image segmentation  
11. Feature extraction  
12. Image pattern classification  

Finer 4e section numbers (3.1, 4.2, …) are in the Pearson detailed ToC PDF; not recopied here.

## Computer Vision: Algorithms and Applications — Szeliski (2e, 2022)

2e titles (SpringerProfessional + Scribd 2e extract + official 15-chapter sequence):

1. Introduction  
2. Image formation  
3. Image processing  
4. Model fitting and optimization  
5. Deep learning  
6. Recognition  
7. Feature detection and matching  
8. Image alignment and stitching  
9. Motion estimation — translational alignment, parametric motion, optical flow, layered motion  
10. Computational photography  
11. Structure from motion and SLAM  
12. Depth estimation  
13. 3D reconstruction — shape from X, 3D scanning, surfaces  
14. Image-based rendering  
15. Conclusion

## Computer Vision: A Modern Approach — Forsyth & Ponce (2e)

Pearson / UIUC chapter list:

**I Image formation**  
1. Geometric camera models — pinhole, weak perspective, lenses  
2. Light and shading — pixel brightness  
3. Color — human color perception  

**II Early vision: just one image**  
4. Linear filters — convolution  
5. Local image features — image gradient, edge detectors, orientations  
6. Texture — filter-bank representations  

**III Early vision: multiple images**  
7. Stereopsis — binocular geometry, epipolar constraint  
8. Structure from motion  

**IV Mid-level vision**  
9. Segmentation by clustering — grouping and Gestalt  
10. Grouping and model fitting — Hough transform  
11. Tracking — tracking by detection, matching translations  

**V High-level vision**  
12. Registration — rigid objects, iterated closest points  
13. Smooth surfaces and their outlines — differential geometry, aspect graph  
14. Range data — active sensors, range segmentation  
15. Classifiers  
16. Classifying images  
17. Detection  
18. Object recognition  

## Multiple View Geometry in Computer Vision — Hartley & Zisserman (2e)

Oxford VGG figures page (official 2e chapter list):

**0 Background**  
1. Introduction — a tour of multiple view geometry  
2. Projective geometry and transformations of 2D  
3. Projective geometry and transformations of 3D  
4. Estimation — 2D projective transformations  
5. Algorithm evaluation and error analysis  

**1 Camera geometry and single-view geometry**  
6. Camera models  
7. Computation of the camera matrix P  
8. More single view geometry  

**2 Two-view geometry**  
9. Epipolar geometry and the fundamental matrix  
10. 3D reconstruction of cameras and structure  
11. Computation of the fundamental matrix F  
12. Structure computation  
13. Scene planes and homographies  
14. Affine epipolar geometry  

**3 Three-view geometry**  
15. The trifocal tensor  
16. Computation of the trifocal tensor T  

**4 N-view geometry**  
17. N-linearities and multiple view tensors  
18. N-view computational methods  
19. Autocalibration  
20. Duality  
21. Cheirality  
22. Degenerate configurations  
Appendices  

Teach through two-view geometry (Ch. 1–14) for CORE; later parts only if a vision slice needs them.

## Introduction to Information Retrieval — Manning, Raghavan, Schütze

1 Boolean retrieval. 2 The term vocabulary and postings lists. 3 Dictionaries and tolerant retrieval. 4 Index construction. 5 Index compression. 6 Scoring, term weighting, and the vector space model. 7 Computing scores in a complete search system. 8 Evaluation in information retrieval. 9 Relevance feedback and query expansion. 10 XML retrieval. 11 Probabilistic information retrieval. 12 Language models for information retrieval. 13 Text classification and Naive Bayes. 14 Vector space classification. 15 SVMs and machine learning on documents. 16 Flat clustering. 17 Hierarchical clustering. 18 Matrix decompositions and LSI. 19 Web search basics. 20 Web crawling and indexes. 21 Link analysis (PageRank, hubs and authorities).

## Reinforcement Learning: An Introduction — Sutton & Barto (2e)

1. Introduction  
2. Multi-armed bandits  
3. Finite Markov decision processes  
4. Dynamic programming  
5. Monte Carlo methods  
6. Temporal-difference learning  
7. n-step bootstrapping  
8. Planning and learning with tabular methods  
9. On-policy prediction with approximation  
10. On-policy control with approximation  
11. Off-policy methods with approximation  
12. Eligibility traces  
13. Policy gradient methods  
14. Psychology  
15. Neuroscience  
16. Applications and case studies  
17. Frontiers  

CORE teaching uses Ch. 1–6 and 13. Ch. 14–17 optional. Section-level ToC is in the free 2e draft at incompleteideas.net; chapter titles above are from that book.

## Convex Optimization — Boyd & Vandenberghe

1. Introduction — mathematical optimization, least-squares and LP, convex vs nonlinear, notation  
2. Convex sets — affine/convex sets, examples, operations that preserve convexity, generalized inequalities, separating/supporting hyperplanes, dual cones  
3. Convex functions — basic properties, operations that preserve convexity, conjugate, quasiconvex, log-concave/convex  
4. Convex optimization problems — LP, QP, geometric programming, generalized inequalities, vector optimization  
5. Duality  
6. Approximation and fitting  
7. Statistical estimation  
8. Geometric problems  
9. Unconstrained minimization  
10. Equality-constrained minimization  
11. Interior-point methods  
Appendices. (Ch. 5–11: chapter titles from the public ToC; section lists for 5–11 were not copied from the LOC/dokumen extract used here.)

## Information Theory, Inference, and Learning Algorithms — MacKay

Part I Data compression (entropy, source coding). Part II Noisy-channel coding (mutual information, channel capacity). Part III Further topics in information theory. Part IV Probabilities and inference (Bayes, clustering, Monte Carlo, Ising, exact inference). Part V Neural networks. Part VI Sparse graph codes. Complements Cover & Thomas; do not teach as a second full information-theory course.

## Probabilistic Machine Learning: An Introduction — Murphy (2022)

1 Introduction.  
Part I Foundations: 2 Probability — univariate models; 3 Probability — multivariate models; 4 Statistics; 5 Decision theory; 6 Information theory; 7 Linear algebra; 8 Optimization.  
Part II Linear models: 9 Linear discriminant analysis; 10 Logistic regression; 11 Linear regression; 12 Generalized linear models.  
Part III Deep neural networks: 13 Neural networks for tabular data; 14 Neural networks for images; 15 Neural networks for sequences.  
Part IV Nonparametric models: 16 Exemplar-based methods; 17 Kernel methods; 18 Trees, forests, bagging, and boosting.  
Book 2 (*Advanced Topics*) is out of CORE teaching scope. Complements Bishop and ESL.

## Introduction to Automata Theory — Hopcroft, Motwani, Ullman

1 Automata: methods and the madness. 2 Finite automata. 3 Regular expressions and languages. 4 Properties of regular languages. 5 Context-free grammars and languages. 6 Pushdown automata. 7 Properties of CFLs. 8 Turing machines. 9 Undecidability. 10 Intractable problems. 11 Additional classes. CORE for M44: Ch. 1–3 (acceptors vs transducers later via OpenFst). Undecidability is not a destination.

## Designing Machine Learning Systems — Chip Huyen

1 Overview of ML systems. 2 Introduction to ML systems design. 3 Data engineering fundamentals. 4 Training data. 5 Feature engineering. 6 Model development and offline evaluation. 7 Model deployment and prediction service. 8 Data distribution shifts and monitoring. 9 Continual learning and test in production. 10 Infrastructure and tooling for MLOps. 11 The human side of ML.

## Dive into Deep Learning — Zhang, Lipton, Li, Smola

1 Introduction. 2 Preliminaries. 3 Linear NNs for regression. 4 Linear NNs for classification. 5 MLPs. 6 Builders’ guide. 7 CNNs. 8 Modern CNNs. 9 RNNs. 10 Modern RNNs. 11 Attention and transformers. 12 Optimization. 13 Computational performance. 14 Computer vision. 15 NLP pretraining. 16 NLP applications. 17 Reinforcement learning. Later chapters (GPs, HPO, GANs, recommenders) as needed.

## Understanding Deep Learning — Prince

Public ToC (dokumen.pub / author figure index / MIT Press listings):

1. Introduction — supervised, unsupervised, RL, ethics, how to read  
2. Supervised learning — overview, linear regression example  
3. Shallow neural networks — example, universal approximation, multivariate I/O, terminology  
4. Deep neural networks — composing networks, matrix notation, shallow vs deep  
5. Loss functions — maximum likelihood, univariate/binary/multiclass recipes, cross-entropy  
6. Fitting models — gradient descent, SGD, momentum, Adam, hyperparameters  
7. Gradients and initialization — derivatives, backpropagation, parameter initialization  
8. Measuring performance — sources of error, double descent, hyperparameters  
9. Regularization — explicit, implicit, heuristics  
10. Convolutional networks — invariance/equivariance, 1D/2D conv, down/upsampling  
11. Residual networks — residual blocks, exploding gradients, batch norm, common architectures  
12. Transformers — self-attention, BERT/GPT/translation examples, long sequences, images  
13. Graph neural networks — graph representation, GCN, node/graph classification  
14. Unsupervised learning — taxonomy, what makes a good generative model  
15. Generative adversarial networks — discrimination as signal, StyleGAN, image translation  
16. Normalizing flows — invertible layers, multi-scale flows  
17. Variational autoencoders — latent variables, ELBO, reparameterization  
18. Diffusion models — forward/reverse process, training, implementation  
19. Reinforcement learning — MDPs, Q-learning, policy gradient, actor-critic, offline RL  
20. Why does deep learning work? — fitting vs generalization, double descent, lottery tickets  
21. Deep learning and ethics — value alignment, misuse, responsible research  

Use alongside Goodfellow.

## Fundamentals of Speech Recognition — Rabiner & Juang

1 Fundamentals of speech recognition. 2 The speech signal: production, perception, acoustic-phonetic characterization. 3 Signal processing and analysis methods for speech recognition. 4 Pattern-comparison techniques. 5 Speech recognition system design and implementation issues. 6 Theory and implementation of hidden Markov models. 7 Speech recognition based on connected word models. 8 Large-vocabulary continuous speech recognition. 9 Task-oriented applications of automatic speech recognition.

## Discrete-Time Speech Signal Processing — Quatieri

Library of Congress ToC (LCCN 2001021821). Speech-specific DSP for M41 / M43.

1. Introduction  
2. A discrete-time signal processing framework  
3. Production and classification of speech sounds  
4. Acoustics of speech production  
5. Analysis and synthesis of pole-zero speech models  
6. Homomorphic signal processing  
7. Short-time Fourier transform analysis and synthesis  
8. Filter-bank analysis/synthesis  
9. Sinusoidal analysis/synthesis  
10. Frequency-domain pitch estimation  
11. Nonlinear measurement and modeling techniques  
12. Speech coding  
13. Speech enhancement  
14. Speaker recognition

## Software, mechanical, medical inventories

Retained as title-plus-scope lists. Full teaching maps are not in the sources beyond module titles.

## Books in §1 with no public chapter+subtopic ToC in this file

Left as titles (or the inventory notes above). Do not invent chapters.

S. Chand ICSE; Frank Modern Certificate; Together With ICSE; Foundation Mathematics (R.S. Aggarwal).  
Kenneth H. Rosen *Elementary Number Theory and Its Applications*; Serge Lang *Algebraic Number Theory*.  
Ernst proof and abstract-algebra notes; Ron Taylor; Jensen-Vallin; Sundstrom; Judson.  
Ernst/Mahavier/Boman/Towsley/Orr analysis notes; Axler *Measure, Integration & Real Analysis*.  
OpenFst / Kaldi documentation.  
Lakshmanan *ML Design Patterns*.  
Winters *SE at Google*; Aniche; Hermans; Richards & Ford; Fowler; Rippon; Cherny.  
Raisinghania; Schmid; *Theory of Mechanisms and Machines*; *Introduction to Aerospace Engineering*.  
Pathology: The Big Picture; Levinson; Jawetz; LANGE PA Q&A; AccessMedicine suite.

**Software.** Winters et al.: Google SE practices. Aniche: developer testing (Java examples). Hermans: reading and writing code, cognition. Richards & Ford: architectural patterns. Fowler: smells and refactoring. Rippon: React + TypeScript 3 (Router, Jest). Cherny: TypeScript for Java/C#/Python programmers.

**Mechanical / aerospace.** Raisinghania: properties, statics, kinematics, Bernoulli, measurements, viscous flow, boundary layer, pipe flow. Schmid: manufacturing processes. Mechanisms: 1 kinematic pairs and chains; 2 cam and follower; 3 gear trains and cams; 4 linkage analysis and synthesis; 5 dynamics. Aerospace: 1 history of flight; 2 aerodynamics; 3 structures and materials; 4 propulsion and jets; 5 stability and control.

**Medical / AccessMedicine.** Basic science: A&P, biochem, epidemiology & biostatistics, micro, pathology & histology, pharmacology, neuroanatomy, pathophysiology, genetics. Clinical / board: laboratory methods, Current Diagnosis and Treatment, LANGE PA Q&A 8e, rotation/PANCE case Q&A. Imaging: CT, echo, EM/critical care, fetal US, GI/hepatology, nephrology/urology, neurology, ophthalmology, pediatrics, POCUS, pulmonology, rheumatology. Interactive: auscultation, 3D anatomy, biochem/genetics, DeGowin, histology, micro/ID, pathology, pharmacology, physiology, Vanderbilt Rapid Recall. Clerkships: cards, pulm, renal, GI, heme/onc, ID, endo, rheum. Specialties: anesthesiology through surgery as listed in the source inventory.

---

# 3. Teaching spine

Eight-tier modules M1–M46 are the backbone. IIT GenAI modules and the eight DL modules are folded into the matching M-block. Lecture facts that belong to a module are pointed at §6 rather than copied.

## IIT Kharagpur EPGC — official map `CORE`

**Programme.** Executive Post Graduate Certificate in Generative AI & Agentic AI. Department of Computer Science & Engineering, IIT Kharagpur. Fee ₹1,99,000 (incl. tax). 8 months, 100% live (Saturday 10 AM–1 PM). Source: [online.iitkgp.ac.in](https://online.iitkgp.ac.in/executive-post-graduate-in-generative-ai-and-agentic-ai).

Published progression: Generative AI → LLMs → Customisation / Fine-Tuning → RAG → Agentic AI → Production Deployment.

This is the same course as `iit-genai.md` and the §6 lecture bank. The table below is the official week map. Teach the matching M-modules and lecture sections; do not run a second parallel course.

| Official module | Weeks | Topics | Where it lives here |
|---|---|---|---|
| Bridge | before W1 | Python, SQL, statistics, linear algebra, probability, calculus | Tiers 1–4 + §4 NumPy + new SQL block below |
| 1 Foundations of GenAI & LLMs | 1–6 | AI & DL essentials; transformer (attention, tokenisation, embeddings, positional encoding); foundation models (GPT, Gemini, LLaMA, Mistral — cost / capability / constraints) | DL Modules 1–3, M45, §6.2–6.7 |
| 2 Advanced Prompting & RAG | 7–12 | Tool-calling, retrieval-aware and safety prompts, failure handling; chunking, retrieval architectures, vector DBs; hybrid search, rerank, RAGAS-style eval, debugging retrieval | Folded IIT 7–8, §6.9–6.11 |
| 3 LLM Fine-Tuning & Alignment | 13–18 | When to fine-tune vs prompt vs RAG; PEFT LoRA/QLoRA on open models and SLMs; lab: dataset, train, evaluate vs baseline | Folded IIT 9, M45 fine-tuning |
| 4 Multimodal & Agentic AI | 19–24 | Vision-language models and image generation; planning, tools, memory, LangGraph-style orchestration, multi-agent workflows | Folded IIT 10–11, §6.11 agentic |
| 5 Deployment, Optimisation & AI Safety | 25–32 | Production RAG/agents; FastAPI, containers, monitoring, latency/cost; guardrails, privacy, hallucination handling, governance docs; industry capstone | Folded IIT 12–13, M46, §6.8 |

**Faculty.** Sourangshu Bhattacharya (Programme Director); Niloy Ganguly; Pawan Goyal; Sudeshna Sarkar; Plaban Bhowmick; Jiaul Hoque Paik; Somak Aditya; Debaditya Roy; Abhijnan Chakraborty; Koustav Rudra.

**Official prerequisites (the learner here does not yet have them).** Write Python functions and basic data structures; has used APIs; can read technical docs; familiar with basic ML math/stats. Bridge + Tiers 1–4 remain mandatory.

**Five portfolio systems.** (1) Enterprise RAG: hybrid search, rerank, eval on large collections. (2) Fine-tuned LLM: LoRA/QLoRA on domain data, served as an API. (3) Multi-agent system: plan, tools, coordination, deployed end to end. (4) Deployed GenAI API: containerised, monitored, real traffic. (5) Industry capstone: healthcare / BFSI / manufacturing, business problem → deployed solution.

**SQL bridge `PREREQ` / `TOOL`.** SELECT, WHERE, JOIN, GROUP BY, aggregations, subqueries; connecting Python to a SQL store for extraction. No extra database textbook.

**Fine-tune vs prompt vs RAG.** Prompt when the base model already knows the task format. RAG when facts must stay current or private. Fine-tune (PEFT) when style, schema, or domain language must change and a dataset exists. Prefer the cheapest option that meets the eval.

**RAGAS-style metrics.** Faithfulness, answer relevancy, context precision, context recall.

**LangGraph-style orchestration.** Graph of nodes as actions; state passed between nodes; loops for Plan → Act → Observe → Track; specialists return control to a triage node.

**VLM / image generation (Module 4).** Vision encoders into token generators (ViT, CLIP); text-to-image diffusion / DALL·E / Stable Diffusion as generation heads; cross-attention for joint text–image.

### Foundational papers (cite; not textbooks)

Vaswani et al. 2017, *Attention Is All You Need*. Devlin et al. 2019, BERT. Radford et al. 2019, GPT-2. Brown et al. 2020, GPT-3. Lewis et al. 2020, RAG. Hu et al. 2021, LoRA. Dettmers et al. 2023, QLoRA. Ouyang et al. 2022, InstructGPT. Yao et al. 2023, ReAct. Zou et al. 2023, GCG.

## Tier 1 — Foundational mathematics (ICSE 6–10) `PREREQ`

Textbooks: Selina, Aggarwal, S. Chand, Frank, Together With, R.S. Aggarwal. JEE habit starts here with Cengage / Arihant later.

### M1 Foundational arithmetic and bases `PREREQ`

Number systems, base transformations, place/local values, rounding/estimation, divisibility, prime factorization, GCD/HCF, LCM, BODMAS. Skills: fast integer manipulation, factorization pipelines, base-n representation.

### M2 Rational fields and the real line `PREREQ`

Field properties of ℚ, fraction conversion, repeating decimals, absolute value, negatives, real-line mappings, exponent laws.

### M3 Set-theoretic foundations `PREREQ` · also IIT Module 1 discrete math

Definition, membership, roster vs set-builder, empty/finite/infinite, Cartesian product, union/intersection/complement/difference/symmetric difference, De Morgan. **Propositional logic gates** (AND, OR, NOT, implication) as membership mappings — IIT Module 1 discrete-math bullet. Skills: Venn proofs, parsing set-builder notation. Rosen / Grimaldi / Hammack later deepen this.

### M4 Ratios, proportions, scales `PREREQ`

Unitary method, compounding ratios, continued proportion, direct/inverse variation, scale factors, componendo, dividendo, alternando, invertendo.

### M5 Foundational algebra `PREREQ`

Polynomial identities, substitution, framing expressions from words, linear equations in one variable.

### M6 Linear inequations in one variable `PREREQ`

Inequality properties (especially multiplying by negatives), interval maps, multi-step inequalities, ℕ/ℤ/ℝ solution sets.

### M7 Quadratic equations `PREREQ`

Standard form, discriminant, nature of roots, splitting the middle term, Shreedharacharya, equations reducible to quadratics.

### M8 Polynomial factors and remainder theorems `PREREQ`

Functions, remainder and factor theorems, division algorithm, synthetic division, cubic factoring.

### M9 Matrices and 2D linear systems `PREREQ` · also IIT Module 2 primitives

Order, row/column vectors, identity and null, addition, **vector array scaling** (scalar–vector multiply), multiply compatibility, 2×2 determinants, **matrix transpose**. **Linear mappings by row substitution** (IIT Module 2) before Cramer's rule in M26. Skills: matrix multiply from scratch; two-variable linear systems. Python hook: NumPy arrays (§4).

### M10 Arithmetic progressions `PREREQ`

Sequence, \(a_n = a+(n-1)d\), \(S_n = n/2\,(2a+(n-1)d)\), arithmetic mean. IIT Module 1 sequences.

### M11 Geometric progressions `PREREQ`

\(a_n = ar^{n-1}\), finite sum, \(|r|<1\) convergence, \(S_\infty = a/(1-r)\), geometric mean.

### M12 Foundational coordinate geometry `PREREQ` · IIT Module 1 coordinate maps

Cartesian plane, reflections, section (internal), midpoint, centroid. **Distance metrics** on the plane (Euclidean first; later cosine / Manhattan when vectors appear in M27 and embeddings).

### M13 Linear equations in two variables `PREREQ` · IIT Module 1 linear systems

Grid lines \(ax+by=c\), slopes, **point intersections**. Slope, inclination, slope-intercept / point-slope / two-point / intercept forms, parallel and perpendicular conditions.

### M14 Euclidean geometry of triangles `PREREQ` (JEE aptitude)

Congruence, similarity (AAA, SAS, AA), Thales / BPT, midpoint theorem, area ratios vs side ratios.

### M15 Circle geometry and tangents `PREREQ` (JEE aptitude)

Chords, cyclic quads, angles in a segment, tangent theorems, intersecting chords, secants, concyclic points.

### M16 Classical mensuration `PREREQ`

Plane areas; SA and volume of cylinder, cone, sphere, hemisphere; combined solids.

### M17 Foundational trigonometry `PREREQ`

Six ratios (sine, cosine, tangent, secant, cosecant, cotangent), \(\sin^2\theta+\cos^2\theta=1\), heights and distances, elevation and depression.

### M18 Commercial arithmetic `ARCHIVE`

VAT/GST (CGST, SGST, IGST, ITC), recurring deposits, shares and dividends. Retained from Selina / Aggarwal Class 10 Ch. 1–3. Not a teaching destination.

## Tier 2 — Senior secondary and JEE `PREREQ`

Textbooks: NCERT XI–XII, Hall & Knight, Loney, Maron, Cengage, Arihant, Vikas Gupta.

### M19 Relations, equivalence, functions `PREREQ`

Cartesian products, equivalence relations and classes, domain/codomain/range, injective/surjective/bijective, composition, inverses, even/odd, special functions (floor, fractional part, signum, log, exp, power).

### M20 Complex fields and roots of unity `PREREQ`

Field ℂ, conjugates, polar and Euler form \(e^{j\theta}\), modulus and principal argument, triangle inequalities, de Moivre, n-th roots of unity, geometric maps.

### M21 Combinatorics and permutations `PREREQ`

Counting principle, permutations with/without repetition, circular permutations, combinations, constrained selection, partitions of identical objects. Rosen / Grimaldi / CLRS App. C.

### M22 Binomial and multinomial theorems `PREREQ`

Positive integral index, general and middle terms, coefficient identities, multinomial expansions.

### M23 Plane trigonometry and equations `PREREQ`

Periodic graphs, addition/subtraction, multiple and half-angle, general solutions, inverse circular functions and principal values.

### M24 Advanced coordinate geometry: circle `PREREQ`

General second-degree equation, parametric form, tangent and normal, chord of contact, director circle, orthogonal circles.

### M25 Conic sections `PREREQ`

Eccentricity-focus-directrix, parabola / ellipse / hyperbola, auxiliary circles, asymptotes, tangents and normals.

### M26 Matrices, determinants, Cramer's rule `PREREQ`

3×3 determinants, transpose, adjoint, inverse, row/column ops, diagonal / symmetric / skew-symmetric, simultaneous systems, Cramer's rule.

### M27 Vector algebra and triple products `PREREQ`

Direction cosines/ratios, dot and cross, scalar triple \([a,b,c]\), vector triple \(a\times(b\times c)\).

### M28 Three-dimensional coordinate space `PREREQ`

Skew lines, symmetric/unsymmetric line forms, planes, angles, point-to-plane distance.

### M29 Real limits and continuity `PREREQ`

ε-δ definition, limit properties, IVT, indeterminate forms, L'Hôpital. Spivak Ch. 5–8; Maron; Rudin Ch. 4 later.

### M30 Differential calculus `PREREQ`

First principles, product/quotient/chain, implicit and parametric, higher-order derivatives. Skill: finite-difference gradient kernels.

### M31 Applications of derivatives `PREREQ`

Rates, tangents/normals, Rolle and Lagrange MVT, monotonicity, local/absolute extrema. This is the first optimization habit used later in gradient descent.

### M32 Indefinite and definite integration `PREREQ`

Antiderivatives, substitution, parts, partial fractions, Riemann sums, FTC, properties of definite integrals.

### M33 Applications of integrals `PREREQ`

Area under curves and between intersections, symmetry.

### M34 Ordinary differential equations `PREREQ`

Order, degree, formation, separable, homogeneous first-order, linear first-order, integrating factors. Skill: IVP numerical solvers.

## Tier 3 — Undergraduate engineering mathematics `PREREQ`

Textbooks: Grewal, Kreyszig.

### M35 ODE and PDE systems `PREREQ`

Linear ODEs with constant coefficients, series solutions, Bessel and Legendre, Beta and Gamma, PDEs.

### M36 Advanced transform calculus `PREREQ` · feeds DSP

Laplace and inverse, convolution theorem, Fourier series / integrals / transforms, discrete z-transform, ROC. Skill: frequency-domain analysis, transfer functions.

### M37 Numerical methods and difference equations `PREREQ`

Curve fitting, finite differences, interpolation, numerical differentiation/integration, Euler, RK4, difference equations. Skill: error-propagation modeling. Python hook: SciPy.

## Tier 4 — Graduate-level rigor, proof to Python

### M38 Topological real analysis `PREREQ` (ceiling: undergraduate analysis, not research)

Metric spaces, open/closed, limit points, Cauchy, completeness, compactness (Heine-Borel), continuous maps, uniform continuity, uniform convergence, Stone-Weierstrass. Rudin Ch. 2–7; Axler as optional measure follow-on. `ARCHIVE` if pushed into research measure theory.

### M39 Spectral theory and matrix decompositions `CORE`

Inner products, Hilbert space, orthonormal bases, Gram-Schmidt, self-adjoint operators, spectral theorem, SVD, low-rank approximation, matrix norms. Skill: SVD from scratch via power iteration and Hotelling deflation in NumPy. Strang Ch. 5–6; Luenberger Ch. 2–5. Lecture hook: PCA motivation in §6.3.

### M40 Mathematical statistics and inference `CORE` · absorbs IIT Module 3 and STAT 1–9

Joint / marginal / conditional; parameter estimation; MLE; Fisher information; Cramér-Rao; hypothesis testing; confidence intervals; Bayesian inference (prior/posterior); MCMC. Bayes' theorem written out:

\[
P(A\mid B)=\frac{P(B\mid A)\,P(A)}{P(B)}
\]

Expectation and variance as sampling-theory markers (IIT Module 3). Casella & Berger; Wasserman; Jaynes; Murphy. Full STAT inventory is §5, mapped here. Python hook: SciPy / NumPy simulation.

## Tier 5 — Signal and image processing `CORE`

Textbooks: Oppenheim & Willsky, Oppenheim & Schafer, Proakis & Manolakis, Lyons, Lathi, Proakis & Salehi (as needed). Cover & Thomas and MacKay for information theory used in later ML.

### M41 Digital signal processing `CORE`

Sampling theorem, aliasing, discrete-time LTI, z-transform, DFT, FFT, FIR/IIR design, cepstral analysis. Skill: 1D FFT and convolution from scratch in NumPy. SciPy signal. Speech-specific follow-on (cepstrum, STFT, LPC, filter banks): Quatieri Ch. 2, 5–9.

### M42 Digital image processing `CORE` · Computer vision entry

2D sampling and quantization, 2D discrete convolution, spatial filters (smoothing, sharpening, Sobel, LoG), frequency-domain filtering, restoration, noise models, histogram equalization, morphology. Textbook: Gonzalez & Woods (full ToC in §2). Later: CNN / detection / multi-view in Szeliski, Forsyth & Ponce, and Hartley & Zisserman; CNN applications in DL Module 4.

Open-course companions for the later vision chapters (use when the printed book is not in hand):

| Topic | Book chapters | Open companions |
|---|---|---|
| SfM / SLAM | Szeliski 11; Hartley 9–12 | UW CSE 576; Columbia FPCV *Structure from Motion* + COMS4731; CMU 16-385; MIT 6.8300 |
| Depth / stereo | Szeliski 12; Forsyth 7 | Brown CSCI 1430; Stanford CS231A; Princeton COS 429 |
| 3D reconstruction / IBR | Szeliski 13–14 | CMU 15-463; Berkeley CS180 |
| Multi-view geometry | Hartley 1–14 | Oxford VGG book site; Harvard CS283 |

Information theory (Cover & Thomas) is taught with M40–M41 and again when cross-entropy / KL appear in nets: entropy, mutual information, KL divergence, Shannon theorems.

## Tier 6 — Deep learning and Kaldi-level ASR `CORE`

Textbooks: Rabiner & Juang, Huang/Acero/Hon, Yu & Deng (neural ASR), Quatieri (speech DSP), Jurafsky & Martin Ch. 14–15, OpenFst / Kaldi docs.

### M43 Kaldi-level acoustic modeling `CORE`

Speech production and hearing; MFCC / PLP; i-vectors; HMMs; GMMs (including diagonal); EM; forward-backward; state clustering; phonetic decision trees. Skill: GMM-EM from scratch in NumPy. Proakis cepstrum from M41 and Quatieri Ch. 5–7 are prerequisites.

Open-course companions (same edition topics; not a second spine):

| Topic | Book chapters | Open companions |
|---|---|---|
| Speech coding / representations | Huang 6–7; Quatieri 5–12 | MIT / Rabiner digital speech notes; NPTEL speech processing |
| HMM / acoustic / robustness / LM / search | Huang 8–13; Rabiner 6–8 | Stanford CS224S; CMU 11-751; IITB CS753; IITM BSEE4001; IISc E9 261 |
| Neural ASR | Yu 4–14 | Stanford CS224S deep-speech weeks; Kaldi / ESPnet docs |
| TTS / SLU | Huang 14–18 | CS224S dialogue and synthesis weeks |

Kaldi secondary spine (do not treat as a second course):

1. Acoustic fundamentals and DSP dependencies (BLAS/LAPACK matrix wrappers assume M39 + M41).
2. Probabilistic sequence modeling and HMM-GMM (multivariate inference from M40).
3. Decoding graph and WFSTs — see M44.
4. Hybrid DNN-HMM: DNN posteriors replace GMM emissions.
5. Practical Kaldi: recipes, scripting, deployment.

### M44 OpenFst-based automata `CORE`

WFSTs; symbol tables (`words.txt`, `phones.txt`); transducers H, C, L, G; composition \(H \circ C \circ L \circ G\); determinization, minimization, epsilon removal; disambiguation symbols `#0 #1 #2`; self-loop addition; Viterbi decoding graphs.

- G: language-model acceptor (word-sequence probabilities; n-gram LMs, perplexity, Kneser-Ney).
- L: lexicon (CI phones → words).
- C: context-dependency (CD phones → CI phones).
- H: HMM (states → transition-ids).

Skill: OpenFst composition simulation and graph parsing. Rosen / Grimaldi automata are the discrete-math prerequisite.

## Tier 7 — Sequence models and transformers `CORE`

Absorbs IIT Modules 4–6, DL Modules 1–6, Lectures 3–4. Unique lecture facts live in §6.5–6.7.

### Folded DL Module 1 — Math and ML primitives `CORE`

1.1 Tensors, eigendecomposition, PCA (M39). 1.2 Partial derivatives, chain rule, Hessians (M30–M31). 1.3 Distributions, cross-entropy, KL (M40 + Cover & Thomas). 1.4 Capacity, over/underfitting, bias-variance. 1.5 MLE and Bayesian stats (M40). 1.6 SVM, logistic regression, shallow classifiers (Bishop 3–4, 7; ESL 3–4, 12; Duda–Hart–Stork 2–6).

### Folded DL Module 2–3 and IIT Module 4 — Neural nets `CORE`

Perceptron; feedforward layers; activations (sigmoid, tanh, ReLU, leaky ReLU, GELU, Swish); cost functions and output units; backprop and computational graphs; **layer dimensions vs depth bounds** (IIT Module 4; same idea as depth vs width); universal approximation. Regularization: L1/L2, augmentation, noise, early stopping, parameter tying, dropout, ensembles. Optimizers: SGD, mini-batch, Momentum, Nesterov, AdaGrad, RMSProp, Adam. BatchNorm and LayerNorm. Goodfellow Parts I–II; Bishop 5; lecture §6.5. Skill: forward and backward pass from scratch.

### Folded DL Module 4 — CNNs / CV `CORE`

Convolution (padding, stride, dilation); pooling (max, average) and translation invariance; LeNet, AlexNet, VGG, Inception, ResNet; detection, segmentation, YOLO; visualizing representations. Goodfellow Ch. 9. Sits on M42.

### Folded DL Module 5 — Sequence models `CORE`

RNN unrolling; vanishing/exploding gradients; LSTM, GRU; bidirectional and deep RNNs; encoder-decoder seq2seq; NLP and time-series uses. Goodfellow Ch. 10; Jurafsky Ch. 13. Prerequisite for M45.

### M45 Attention and transformers `CORE` · IIT Module 5–6, DL Module 6

Tokenization (BPE, WordPiece); embeddings; **sinusoidal** positional encoding; scaled dot-product attention

\[
S = QK^\top / \sqrt{d_k},\quad A = \mathrm{softmax}(S),\quad Z = AV
\]

Multi-head projections, **residual connections**, layer norm, decoder masking, unembedding, **softmax normalization**. LLM families: BERT, GPT, T5. Fine-tuning: instruction tuning, RLHF, DPO. Skill: multi-head self-attention and backprop in NumPy; later `torch.nn.MultiheadAttention`. Lecture bank §6.5–6.7.

### Folded DL Module 7 — Generative models `CORE` (to industry competence, not research depth)

Undercomplete / regularized / sparse / denoising autoencoders; representation and manifold learning; VAEs; GANs; diffusion and normalizing flows; GNNs. Goodfellow Part III. Stop at working competence.

## Tier 8 — Production, GenAI systems, GCP PMLE `CORE`

Absorbs IIT Modules 7–13, DL Module 8, Lectures 4 / 6 / Module 2, Lakshmanan design patterns, GCP PMLE 2026 syllabus.

### Folded IIT Module 7 / Lecture prompting — Prompt engineering `CORE`

System vs user prompts; **system routing tokens**; zero-shot; few-shot; CoT; self-consistency; ToT; ReAct; meta-prompting; directional stimulus; tool-calling / JSON structural returns; **guard prompts**, **structural boundary checking**, **exception paths**. Details §6.9–6.10.

### Folded IIT Module 8 / RAG lectures — RAG `CORE`

Chunking, overlapping spans, **structural parsing blocks**; vector indexes; k-NN; hybrid dense+sparse; cross-encoder rerank; context precision. Naive vs advanced (pre- and post-retrieval). IVF, product quantization, HNSW, FAISS vs Chroma. Agentic RAG. Manning IR for BM25 / inverted indexes. Details §6.11.

### Folded IIT Module 9 — PEFT `CORE`

LoRA, QLoRA (4-bit), adapter-only optimization, compare adapters to base.

### Folded IIT Modules 10–11 — Multimodal and agents `CORE`

Cross-attention for text+image; vision encoder into token generation (ViT, CLIP, Whisper). Plan–Act–Track loops; graph orchestration; **persistence layer**: memory design across stateless model endpoint calls. Lecture 6 of Module 2: enterprise DevOps/support agent.

### Folded IIT Modules 12–13 and DL Module 8 — Serving, safety, hardware `CORE`

vLLM-style paging; **asynchronous** FastAPI request handling; **Docker minimal layers**; **real-time** verification filters for hallucinations; latency logging and **token-cost functions**. GPUs/TPUs, parallelization; TF/PyTorch; APIs and edge; pruning, quantization, distillation.

### M46 Enterprise production MLOps / GCP PMLE `CORE`

Official PMLE exam guide (as of 1 June 2026, Google PDF):

- **Section 1** Architecting low-code AI solutions (~13%) — BigQuery ML / AutoML / Gemini Enterprise Agent Platform; cost, latency, availability of Gemini apps  
- **Section 2** Collaborating within and across teams to manage data and models — metadata, Feature Store, shared datasets  
- **Section 3** Scaling prototypes into ML models (~21%) — distributed training, HPT, Vertex training  
- **Section 4** Serving and scaling models (~20%) — batch and online inference, Agent / Vertex Endpoints  
- **Section 5** ML pipeline automation and orchestration — Vertex Pipelines, metadata, experiment tracking  
- **Section 6** Monitoring, optimization, and maintenance — drift, retraining, responsible AI, troubleshooting

Vertex product map (unchanged): BigQuery ML; Feature Store (online + offline point-in-time); TFX; Beam on Dataflow; distributed training; Vertex HPT; AutoML; preemptible VMs; Endpoints; batch prediction; custom containers; multi-model endpoints; Vertex Pipelines; Kubeflow; Cloud Composer; Cloud Build; Model Monitoring; PSI; TFDV; Explainable AI (Integrated Gradients, SHAP); Fairness Lens; guardrails.

Skills: end-to-end Vertex pipelines, Cloud Build triggers, PSI retraining, FastAPI serving. Libraries: MLflow, wandb, Evidently, FastAPI, Ray, PySpark, Dask (§4).

---

# 4. Python library curriculum `TOOL`

Theory of each library is taught from scratch in the slice that first needs it. Do not dump full solutions; pose implementation problems.

## Core numerical and data

- **NumPy** — vectorized computation, linear algebra backbone. Teach with M9 / M26 / M39: `ndarray`, broadcasting, indexing/masks, reshape, `dot`/`@`, `linalg.inv/det/eig/norm/solve`, save/load. Lecture quick-ref absorbed here.
- **Pandas** — tabular joins, groupby, cleaning. Teach with M40 EDA / classical ML.
- **SciPy** — optimization, statistics, signal processing. Teach with M37 / M40 / M41.

## Visualization and EDA

- **Matplotlib** — line, bar, scatter, hist, pie, stem, step; figure/axes; style; subplots/GridSpec; contour, heatmap, 3D; savefig. Lecture quick-ref absorbed here.
- **Seaborn** — statistical plots on Matplotlib.
- **Plotly** — interactive dashboards.

## Classical ML

- **scikit-learn** — regression, classification, pipelines, preprocessing. Estimator protocol: `fit` / `transform` / `predict`. `StandardScaler`, `MinMaxScaler`, `OneHotEncoder`, imputer, `ColumnTransformer`, `Pipeline`. SVM, trees, forests, boosting, linear/logistic, k-NN. Unsupervised: k-means, DBSCAN, PCA, t-SNE, GMM. Selection: CV, Grid/RandomSearchCV, ROC-AUC, PR, confusion matrix. Breast-cancer logistic-regression walkthrough lives in §6.3.
- **XGBoost** — gradient boosting for tabular production.
- **LightGBM** — faster boosting on large sets.

## Deep learning

- **TensorFlow** — production DL, Google / Vertex ecosystem.
- **PyTorch** — dynamic graphs; research and industry default for from-scratch nets after NumPy.
- **Keras** — high-level API on TensorFlow.

## NLP and transformers

- **Hugging Face Transformers** — pretrained BERT/GPT-class models.
- **spaCy** — industrial NLP pipelines.
- **NLTK** — tokenization, stemming, classical pipeline; BLEU / METEOR helpers in §6.8.

## Data engineering

- **PySpark** — distributed processing.
- **Dask** — parallel computing on large arrays/frames.

## MLOps

- **MLflow** — experiment tracking, model registry.
- **Weights & Biases** — experiment monitoring.
- **Evidently** — drift and model monitoring.

## Deployment and agentic add-ons

- **FastAPI** — model APIs (M46, IIT Module 12).
- **LangChain** — LLM orchestration.
- **LlamaIndex** — RAG pipelines.
- **vLLM** — paged LLM serving.
- **Ray** — distributed AI workloads.

---

# 4A. NLP library theory curriculum `TOOL` / `CORE`

Official documentation folded in here: Hugging Face Transformers and Tokenizers; spaCy linguistic-features and processing-pipeline guides; NLTK Book Ch. 3 and Ch. 5. Teach this section with §4, §6.1, §6.4, M45, and M46. Do not teach APIs as magic wrappers. First teach the representation, data structure, algorithm, failure mode, and evaluation signal; then use the library.

## Shared text-processing substrate `PREREQ` / `TOOL`

Raw text is not yet NLP data. The learner must understand the conversion chain: bytes -> Unicode string -> normalized string -> sentences -> tokens -> spans -> labels -> tensors -> model outputs -> decoded text or structured annotations.

- **Unicode and encodings.** Code points, UTF-8 bytes, decoding vs encoding, mojibake, normalization, language scripts, case folding vs lowercasing, glyph vs character. This is required before tokenization, multilingual NLP, ASR transcripts, web corpora, and LLM prompts.
- **Raw text acquisition.** Local files, web pages, HTML stripping, metadata/header/footer removal, RSS/API text, corpora, PDF text vs OCR routing, and the difference between raw strings, token lists, sentence lists, and annotated corpora.
- **Regular expressions.** Anchors, character classes, ranges, groups, alternation, greedy vs non-greedy closures, raw strings, word boundaries, extraction vs substitution, and why regex tokenizers are useful but limited.
- **Normalization.** Whitespace cleanup, punctuation policy, contractions, casing, stop words, numbers/dates/acronyms, stemming vs lemmatization, vocabulary cutoffs, OOV / UNK replacement, and task-specific tradeoffs.
- **Segmentation.** Sentence segmentation, word segmentation, subword segmentation, token boundaries, span offsets, no-whitespace writing systems, speech-like continuous streams, and why no universal tokenizer exists.
- **Evaluation.** Gold tokenization, gold POS / NER labels, train/test split, error analysis, confusion matrices, inter-annotator ambiguity, precision/recall/F1 for span labels, and downstream error propagation.

Bare-metal exercises: implement Unicode-safe text loading; an HTML-to-text cleanup pipeline; a regex tokenizer with offsets for dates, money, abbreviations, and names; a sentence segmenter; a vocabulary builder with UNK replacement; and a tiny concordance / frequency-distribution tool.

## NLTK theory `TOOL`

NLTK is the pedagogy and classical NLP laboratory. Use it to expose corpus structure, tokenization, frequency analysis, lexical resources, taggers, and evaluation before relying on neural models.

- **Corpus interfaces.** `raw()`, `words()`, `sents()`, `tagged_words()`, `tagged_sents()`, file IDs, categories, multilingual corpora, and why sentence-level tagged data is the right unit for sequence models.
- **Core data structures.** Python strings vs lists; dictionaries as lexical maps; `defaultdict`; word -> count maps; word -> tag maps; `FreqDist`; `ConditionalFreqDist`; `Index`; n-grams; conditional counts; sorted vocabulary; corpus-derived evidence.
- **Lexical resources.** WordNet synsets, lemmas, hypernyms, similarity; stopword lists; pronouncing dictionaries; words corpora; treebanks; Brown / Treebank / CoNLL-style annotations.
- **Tokenization and normalization.** `word_tokenize`, `sent_tokenize` / Punkt, `regexp_tokenize`, stemmers, WordNet lemmatizer, tokenized-text regex search, collocations, concordance, and known failures on domain text.
- **POS tagging.** Tagsets, Universal vs Penn vs Brown tags, tagged-token tuples, default taggers, regex taggers, lookup taggers, unigram / bigram / trigram taggers, backoff chains, sparse data, unknown-word handling, Brill transformation rules, model size vs accuracy.
- **Classical sequence thinking.** A tagger predicts a label per token using local evidence. This is the conceptual bridge to HMMs, CRFs, token classification heads, ASR decoding labels, and transformer NER.

Bare-metal exercises: implement `FreqDist` and `ConditionalFreqDist`; a regex stemmer and regex tokenizer; a unigram POS tagger; a bigram tagger with backoff to unigram and default taggers; UNK replacement for rare words; and a confusion matrix for a tagger.

## spaCy theory `TOOL`

spaCy is the industrial linguistic-pipeline library. Teach it as a typed annotation engine over `Doc`, `Token`, and `Span`, with a configurable pipeline that mixes rules, statistical models, and custom components.

- **Object model.** `Language`, `Vocab`, `StringStore`, `Lexeme`, `Doc`, `Token`, `Span`; token text, whitespace, character offsets, lexical attributes, context-dependent token attributes, and why `Token` / `Span` are views over a `Doc`.
- **Tokenizer design.** Non-destructive tokenization (`doc.text == input_text`), language-specific exceptions, prefixes, suffixes, infixes, `token_match`, `url_match`, special cases, retokenization, pre-tokenized `Doc` construction, and debugging with tokenizer explanations.
- **Token alignment.** Align spaCy tokens with external annotations and transformer word pieces. Preserve offsets when moving between NLTK corpora, spaCy `Doc`s, Hugging Face subwords, and human span labels.
- **Pipeline architecture.** Tokenizer first, then components in order. `tok2vec`, `transformer`, `tagger`, `morphologizer`, `attribute_ruler`, `lemmatizer`, `parser`, `senter`, `sentencizer`, `ner`, `entity_ruler`, `entity_linker`, `textcat`, and custom components.
- **Linguistic annotations.** POS tags, fine tags, morphology, lemmas, dependency heads and labels, projective vs non-projective parses, noun chunks, sentence boundaries, named entities, IOB / BILUO entity encodings, entity linking IDs, word vectors, OOV flags, vector norms, and similarity limits.
- **Rules plus models.** `Matcher`, `PhraseMatcher`, `EntityRuler`, `AttributeRuler`, custom extension attributes, custom pipeline components, component factories, pipeline configs, serialization, wrappers around outside models, and `nlp.analyze_pipes` for dependency checks.
- **Efficiency.** `nlp.pipe` for batching, disabling or excluding unused components, `select_pipes`, batch size, multiprocessing limits on macOS / Windows, GPU caveats, and transformer multiprocessing deadlocks.

Bare-metal exercises: build a minimal `Doc` / `Token` / `Span` representation with text offsets; implement rule-based tokenizer exceptions; implement BILUO span encoding and decoding; traverse a dependency tree from head indices; implement vector averaging and cosine similarity; and build a tiny pipeline that passes a document through ordered components.

## Hugging Face Tokenizers theory `TOOL` / `CORE`

Hugging Face Tokenizers is the production subword-tokenization layer behind transformer workflows. Teach the tokenizer as a deterministic pipeline that must match the model checkpoint.

- **Tokenizer pipeline.** Normalizer -> pre-tokenizer -> tokenization model -> post-processor -> decoder, with optional truncation, padding, special tokens, and offset tracking.
- **Subword models.** WordPiece, BPE, byte-level BPE, Unigram LM, WordLevel; vocabulary size; merge rules; continuation markers; unknown-token policy; byte fallback; special-token inventory (`[CLS]`, `[SEP]`, `[PAD]`, `[MASK]`, BOS, EOS).
- **Encoding outputs.** `input_ids`, token strings, `attention_mask`, `token_type_ids`, special-token masks, overflowing windows, offset mappings, word IDs, padding direction, truncation strategy, and batch collation.
- **Alignment problems.** Word-level labels must be aligned to subword pieces for NER and POS; answer spans must be aligned to character offsets for QA; generation output must be decoded while removing or preserving special tokens as required.
- **Failure modes.** Tokenization mismatch between training and inference, bad domain segmentation, too-small vocabulary, excessive sequence length, label drift after normalization, destructive normalization without offset recovery, and prompt length surprises because tokens are not words.

Bare-metal exercises: train a toy BPE vocabulary; implement greedy WordPiece encoding; encode and decode with offsets; add special tokens; build attention masks and padded batches; and align word-level NER labels to subword labels.

## Hugging Face Transformers theory `TOOL` / `CORE`

Transformers is the model-definition and pretrained-checkpoint interface for modern NLP, LLMs, speech, vision-language, and multimodal models. It should be taught as preprocessing -> tensors -> model -> logits / hidden states -> task-specific postprocessing.

- **Core abstractions.** Checkpoint, model card, config, tokenizer / processor, model class, task head, pipeline, `AutoTokenizer`, `AutoModel`, `AutoModelFor...`, Hub revisions, local cache, framework backend, and reproducible model loading.
- **Inputs and outputs.** Token IDs, attention masks, token type IDs, position IDs, labels, logits, hidden states, attentions, pooled outputs, encoder outputs, decoder outputs, `past_key_values`, loss values, and generated sequences.
- **Task heads.** Masked language modeling, causal language modeling, seq2seq generation, sequence classification, token classification, question answering, feature extraction / embeddings, summarization, translation, ASR, image-to-text, VLM chat, and multimodal processors.
- **Pipelines.** A pipeline is convenience orchestration: preprocessing, batching, model forward pass, postprocessing, and output formatting. Teach what each pipeline hides before using it.
- **Fine-tuning workflow.** Dataset schema, train/validation/test split, tokenization map, data collator, dynamic padding, labels, loss, metrics, `Trainer`, callbacks, checkpoints, gradient accumulation, mixed precision, distributed training, and when PEFT / LoRA / QLoRA is preferable to full fine-tuning.
- **Generation and decoding.** Greedy search, beam search, sampling, temperature, top-k, top-p, repetition penalty, stop sequences, max tokens, streaming, KV cache, chat templates, structured output constraints, and why decoding knobs do not solve hallucination without grounding.
- **Operational concerns.** GPU memory, device maps, quantization, batching, latency, throughput, safety filters, eval harnesses, reproducible prompts, model-card limitations, license constraints, and handoff to vLLM / TGI / Vertex when serving becomes the goal.

Bare-metal exercises: implement a tokenizer-to-tensor batch; attention masks; masked-LM cross-entropy; a sequence-classification head; token-classification span reconstruction; greedy, beam, and nucleus decoding; a tiny PyTorch fine-tuning loop after the NumPy version is understood; and a minimal evaluation harness for text classification / NER / generation.

## Cross-library selection and integration `TOOL`

Use NLTK when the goal is classical NLP, corpus inspection, frequency distributions, lexical resources, tagger pedagogy, or transparent baselines. Use spaCy when the goal is fast production text annotation, rule+model pipelines, entity extraction, custom linguistic components, or robust document objects. Use Hugging Face when the goal is pretrained neural models, transformers, embeddings, LLM fine-tuning, ASR, VLMs, or modern generation.

Shared contracts across all three: tokenization policy, offsets, labels, schema, train/test split, metrics, error analysis, and reproducible preprocessing. A mismatch in any one of those can silently ruin an NLP system even when the API calls look correct.

---

# 5. Statistical techniques `CORE` / `PREREQ`

Canonical list. Taught inside M40 and the ML slices, not as a second course.

1. **Descriptive (EDA)** — mean, median, mode, variance, standard deviation, range, IQR, skewness, kurtosis, percentiles/quantiles.
2. **Probability** — conditional, Bayes, joint, marginal, law of total probability, independence.
3. **Distributions** — Normal, Bernoulli, Binomial, Poisson, Uniform, Exponential, Log-normal, Multinomial.
4. **Inference** — sampling (random, stratified, …), CLT, confidence intervals, hypothesis-testing framework, p-values, Type I / II errors, power.
5. **Named tests** — t-test (one-sample, two-sample), z-test, chi-square, ANOVA, Mann-Whitney U, Wilcoxon signed-rank.
6. **Relationships** — covariance, Pearson, Spearman, Kendall tau.
7. **Regression** — linear, multiple linear, logistic, ridge, lasso, polynomial.
8. **Bayesian** — inference, prior/posterior.
9. **MCMC** — Markov Chain Monte Carlo.

Lecture classification metrics (accuracy, precision, recall, F1, confusion matrix) sit with supervised learning in §6.3, not as a tenth STAT family.

---

# 6. IIT / upGrad knowledge bank

Topic-ordered. Page dumps, OCR noise, recap repeats, and thank-you slides are not reproduced. Quizzes are kept as compact items.

Sources: NLP Foundation (14 pp.); Deep Learning foundations (13 pp.); AI & Deep Learning Essentials — Ganguly (87 pp.); Lecture 3 Transformers — Ganguly (71 pp.); Lecture 4 Models & APIs — Bhattacharya (59 pp.); Lecture 6 Evaluations & Safety — Bhattacharya (92 pp.); Module 2 Session 1 Advanced Prompting — Rudra (50 pp.); Session 2 Prompt Optimization & Security — Rudra (73 pp.); Session 3 RAG — Rudra (58 pp.); Module 2 Lectures 4–6 RAG — Goyal (71 + 85 + 97 pp.).

## 6.1 NLP foundations `CORE`

NLP is the interface layer of GenAI systems (chat, search, automation; support, finance, healthcare).

Representation ladder: Bag of Words → TF-IDF → Word2Vec → dense embeddings. Goal: text → numbers. Similar meaning → nearby vectors. Classic analogy: \(\mathrm{king}-\mathrm{man}+\mathrm{woman}\approx\mathrm{queen}\).

Language modeling: predict the next word; context window; a probability distribution over the vocabulary. Evolution: n-grams → RNN → Transformers (parallel + long context).

Classical pipeline: clean → tokenize → stopwords → lemmatize → features → model. Hands-on: NLTK tokenize, TF-IDF, simple classifier. Limits: no deep context, manual features, poor generalization.

Bridge: classical NLP → DL → LLMs → agents. Agent loop: Observe → Reason → Act. Modern path: input → embeddings → retrieval → LLM → output. Hands-on comparison: TF-IDF vs embeddings.

## 6.2 AI history and classical knowledge `PREREQ` for ML language

1956 Dartmouth conference: McCarthy, Minsky, Shannon, Rochester; first use of “artificial intelligence.” Turing Test: judge cannot tell human from machine on a text channel; ELIZA, Mitsuku/Kuki as variants.

Four-quadrant definition (think/act × human/rational). Modern AI emphasizes acting rationally (AlphaGo).

Knowledge: logic (predicate inference), production rules, semantic nets. Expert systems emulate specialist decisions. First AI winter: ambiguity (Russian–English “spirit/flesh” → “vodka/meat”), scalability, brittle representations. Boom/winter cycle: GOFAI 1960s → winter 1970s → expert systems 1980s → winter 1990s → ML boom.

Mitchell (1997): a program learns from experience E on task T measured by P if P on T improves with E.

## 6.3 Supervised / unsupervised / RL and classical ML `CORE`

**Paradigms.** Supervised: labeled pairs, learn \(f:X\to Y\), classification and regression, train/test split. Unsupervised: no labels; clustering (k-means, DBSCAN), dimensionality reduction (PCA, t-SNE), anomaly detection, association rules; recommenders. RL: agent, actions, rewards/penalties.

**Workflow.** Raw data → feature extractor → model.fit → learned parameters. Test: extractor frozen, parameters frozen, compare to ground truth.

**Breast-cancer sklearn walkthrough.** `load_breast_cancer`; 80/20 `train_test_split`; `StandardScaler` fit on train only; `LogisticRegression(max_iter=1000)`; `accuracy_score`, `confusion_matrix`, `classification_report`.

**Confusion matrix.** Rows = actual, columns = predicted. TP / FN / FP / TN. Accuracy \((TP+TN)/N\); precision \(TP/(TP+FP)\); recall \(TP/(TP+FN)\); F1 \(2PR/(P+R)\). Accuracy for balanced data; precision when false alarms are costly; recall when misses are dangerous; F1 when both matter.

**Unsupervised intuition.** Height-line for a photo (self-organize without labels). Recommenders: “those who bought this also bought…”. PCA: high-d data (images 150k dims, vocab 100k, genes 20k) has a low-d subspace of variance; orthogonal basis of max variance; curse of dimensionality makes distances meaningless. Workflow: features → reduce → cluster.

**Hand-crafted features vs embeddings.** Expert features (landmarks, TF-IDF, PCA axes) are brittle. Embeddings: model learns dense vectors; transferable; geometry encodes meaning.

**Bias–variance.** High bias = underfit (train and val both high). High variance = overfit (train low, val high). Total error ≈ bias² + variance + irreducible noise. Detect: train↓ val↑ → overfit (early stop / regularize); both high → underfit (capacity / more epochs).

**Regularization.** L2 Ridge: \(\lambda\sum w^2\), circular constraint, shrinks all weights, differentiable, closed form. L1 Lasso: \(\lambda\sum|w|\), diamond constraint, exact zeros (feature selection), coordinate descent. Dropout: random zero of neurons, rate p. Early stopping: patience on val loss, restore best. Pipeline pattern: `PolynomialFeatures` → `StandardScaler` → `Ridge`; hold out test; `cross_val_score`; tune α with GridSearchCV.

**Fix table.** Underfit → bigger model / more features / more epochs. Overfit → regularize, dropout, more data. High variance → L2 + CV. High bias → polynomial features or richer model class.

## 6.4 Embeddings and text representations `CORE`

One-hot: index in a fixed vocab, a single 1, rest 0. Orthogonal by construction — `cat · kitten = 0`. Bag-of-words / TF-IDF: no order (`dog bites man` = `man bites dog`), OOV → zero vector, curse of dimensionality.

Dense embeddings: every coordinate active (e.g. 300-d). **Cosine similarity** is the IIT Module 5 distance measure for vector alignment:

\[
\cos(\mathbf{u},\mathbf{v})=\frac{\mathbf{u}\cdot\mathbf{v}}{\|\mathbf{u}\|\,\|\mathbf{v}\|}
\]

Geometry: \(\mathrm{king}-\mathrm{man}+\mathrm{woman}\approx\mathrm{queen}\); \(\mathrm{Paris}-\mathrm{France}+\mathrm{Germany}\approx\mathrm{Berlin}\); \(\cos(\mathrm{cat},\mathrm{kitten})\approx 0.92\).

Evolution of representations (Lecture 3): one-hot (structure, no semantics) → dense (compact, context-free) → Word2Vec (semantics, still static: bank=bank) → ELMo/BiLSTM (contextual, sequential, slow) → cross-attention (alignment across sequences) → self-attention + positional encoding (every token attends to all, order-aware).

Subword tokenization (BPE / WordPiece): frequent words stay whole (`transformer`); rare words split (`methylation` → `methyl` + `ation`). Tokens ≠ words; ~1.3 tokens/word; “ChatGPT” = 3 tokens.

## 6.5 Neural nets `CORE`

Biological analogy: dendrites / weights, soma / weighted sum \(z=\sum w_i x_i+b\), axon / activation, synapse strengthening / learning.

Rosenblatt perceptron (1958): \(\hat y=f(z)\). Linearly separable problems only. Non-linearity from activations. MLP: input → hidden feature layers → output.

Backprop: forward → loss (MSE regression \(L=\frac1n\sum(y-\hat y)^2\); cross-entropy classification \(L=-\sum y\log\hat y\)) → backward chain rule \(\partial L/\partial w = \partial L/\partial\hat y\cdot\partial\hat y/\partial z\cdot\partial z/\partial w\) → \(w\leftarrow w-\eta\,\partial L/\partial w\). Variants: SGD, mini-batch, Adam, RMSProp. Failures: vanishing gradients, overfitting, local minima. CS231n figures used in the IIT deck.

Deep Learning deck path: business problem (churn) → NN → loss → optimization → overfitting → attention → transformers → GenAI / agents.

End-to-end examples: summarization, segmentation, spam, captioning.

## 6.6 Transformers `CORE`

**Why attention.** Pre-attention failures: fixed-length context bottleneck; vanishing/exploding gradients; poor long-range paths; no training parallelism; uniform treatment of inputs.

Seq2seq RNN: encoder folds the source into one vector; decoder conditions only on that vector. Bahdanau attention: keep all encoder states; at each decoder step compute weights α and a fresh context \(c_t\). Still sequential; attention is decoder→encoder only; no intra-sequence attention; position only implicit in the RNN.

**Self-attention.** Each token attends to every other token in the *same* sequence. Formula: \(\mathrm{Attention}(Q,K,V)=\mathrm{softmax}(QK^\top/\sqrt{d_k})V\).

Q = what I am looking for; K = what I offer; V = what I give. Example: in “The animal didn’t cross the street because it was too tired,” `it` scores high on `animal` (0.70) and `tired` (0.20).

**Transformer (Vaswani et al. 2017).** No recurrence. Encoder stack and decoder stack (N=6 in the paper). Each encoder block: multi-head self-attention + FFN, each wrapped in residual + LayerNorm. Each decoder block: (i) masked multi-head self-attention, (ii) cross-attention (Q from decoder, K/V from encoder), (iii) FFN. FFN is a two-layer MLP, typically \(d_{ff}=4\,d_{model}\). Positional encodings (sin/cos) added to embeddings because attention is permutation-invariant.

Causal mask: future positions set to −∞ before softmax → lower-triangular attention. Enables parallel training with left-to-right generation.

Autoregressive loop: encode source once; start with `<BOS>`; masked decode; softmax; greedy / beam / temperature sample; append; stop at `<EOS>` or max length.

Multi-head: 8–16 heads, different Q/K/V projections, different relation types in parallel.

GPT-2-style size cited in lecture: 12 layers, 12 heads, \(d_{model}=768\), \(d_{ff}=3072\).

**Quiz (Lecture 3).** Self-attention: Q,K,V from the same sequence. Cross-attention: Q from decoder, K,V from encoder. Positional encodings exist because attention has no inherent order (“the cat chased the mouse” ≠ “the mouse chased the cat”).

Pretraining *is* learning Q, K, V. Fine-tuning steers them; LoRA injects a low-rank Δ.

## 6.7 Foundation models, decoding, APIs `CORE`

**Architecture map.**

| Era | Architecture | Training / data | Alignment / inference |
|---|---|---|---|
| Pre-2018 | word2vec, ELMo (biLSTM) | small corpora | feature transfer |
| BERT 2018 | encoder only; Base 110M/12L, Large 340M/24L; WordPiece | MLM (15%) + NSP; BookCorpus+Wiki ~3.3B tokens | small task head, GLUE 82.1 Large |
| GPT-1/2 2018–19 | decoder-only; 117M → 1.5B | BookCorpus → WebText 40 GB | zero-shot via prompts; LAMBADA 63.2% at 1.5B |
| T5 / BART 2019–20 | enc–dec; T5 span-corruption on C4 750 GB, 60M–11B; BART denoising | SuperGLUE T5-11B 88.9 vs human 89.8 | unified text-to-text |
| GPT-3 2020 | 175B, 2048 context, ~300B tokens | in-context learning | TriviaQA 0/1/10/64-shot: 64.3 / 68.0 / 69.7 / 71.2 |
| Chinchilla | same arch, ~20 tokens/parameter | predictable loss | |
| InstructGPT 2022 | SFT → reward model on rankings → PPO with KL to SFT | 1.3B InstructGPT preferred to 175B GPT-3 (71% vs 37%) | ChatGPT |
| Open weights 2023–24 | LLaMA 7–70B; LLaMA 2 commercial; Mistral 7B; Mixtral 8×7B MoE; Falcon + RefinedWeb | MMLU: Mistral 7B 60.1, LLaMA-2 70B 68.9, Mixtral 70.6, GPT-3.5 70.0 | fine-tunes: Alpaca, Vicuna |
| Multimodal / reasoning 2023–25 | GPT-4V, Gemini, Claude 3/4; o1/o3, DeepSeek-R1 | text+image+audio; RL on verifiable outcomes | inference-time CoT; costly in tokens/time |

GLUE tasks: CoLA, SST-2, MRPC, STS-B, QQP, MNLI, QNLI, RTE, WNLI. MMLU: 57-subject 4-way MCQ. LAMBADA: last-word prediction needing 4+ sentence discourse.

Zoo (all = embeddings + positions + self-attention + FFN): BERT (encoder, classify/NER/QA); GPT (decoder, generate); T5/BART (enc–dec, translate/summarize); ViT (image patches); Whisper (speech→text); CLIP (image–text).

**Decoding parameters.** Temperature scales logits; T→0 ≈ greedy (implementations clamp, e.g. 1e-6). Example logits [4,2,1,0]: T=0.5 entropy 0.110; T=1 entropy 0.594; T=2 entropy 1.109.

Top-k: keep k tokens, renormalize, sample. Top-p / nucleus: smallest set with cumulative prob ≥ p. Do not crank both to extremes. Repetition penalty: divide seen-token logits (typical 1.2–1.5). Frequency penalty: subtract count × penalty (OpenAI, 0–2). Presence penalty: binary version. `max_tokens` caps length. Stop sequences cut structured output (```` `, `\nUser:`, `}\n`).

Cheat sheet (creative vs factual): temperature 1.2 vs 0.3; top-k 80 vs 10; top-p 0.95 vs 0.7; rep 1.2 vs 1.1; freq 0.4 vs 0.1; max_tokens 1024 vs 256.

APIs. OpenAI (proprietary, pay-per-token): chat completions; JSON mode (`response_format={"type":"json_object"}`); Structured Outputs (`strict:true` schema); function/tool calling (tools array, e.g. `get_weather(location)`, `tool_choice="auto"`); vision, audio, embeddings; fine-tuning. Anthropic `messages.create`. Factual preset: temp 0.3, top_p 0.7, max_tokens 256.

**Quiz notes.** Decoder is the generation component. Temperature / top-k / top-p / max-tokens do not by themselves “solve” hallucination; grounding (RAG, tools) does. Reasoning models’ main cited disadvantage: time / token cost.

## 6.8 LLM evaluation and safety `CORE`

Evaluation has two axes: output quality (instruction following, coherence, factuality) and system performance (latency, price, reliability). This bank is about quality.

Human rating is gold but subjective. Agreement beyond chance: Cohen’s κ, Fleiss’ κ, Krippendorff’s α.

**Automatic metrics** on reference “The quick brown dog jumps over the lazy fox” vs candidate with dog/fox swapped:

| Metric | Measures | Best for | Speed | Semantic | Same-pair example |
|---|---|---|---|---|---|
| ROUGE-N / ROUGE-L | recall of n-grams / LCS | summarization | fast | no | ROUGE-1 F=1.0; ROUGE-L F=0.778 |
| BLEU | n-gram precision × brevity penalty \(BP=\exp(1-|r|/|c|)\) if short | translation | fast | no | 0.46 |
| METEOR | F-score, stems, WordNet synonyms, chunk penalty | translation / generation | medium | partial | 0.99 (`fast`≈`quick`) |
| BERTScore | greedy cosine match of BERT contextual vectors | semantic tasks | slow | yes | F1≈0.964 |

ROUGE-N = matched n-grams / reference n-grams. BLEU = \(BP\cdot\exp\sum_n w_n\log p_n\); >0.3 often “reasonable” for MT; multiple references allowed. Limits: style paraphrases score badly; still need humans. For reasoning models, n-gram overlap is a poor fit; BERTScore / LaaJ preferred.

**LLM-as-a-Judge (Zheng et al. 2023, MT-Bench / Chatbot Arena).** Prompt a judge LLM with user prompt, model response, and criteria; require a short rationale and a score (e.g. 0/1 relevance).

**Safety.** Threat models: white-box and black-box. Jailbreak = prompt that bypasses refusal. Attacks:

- GCG (Zou et al. 2023): gradient-based suffix search. High ASR on Vicuna-7B (~99%) and LLaMA-2 (~88%); suffixes transfer to GPT-3.5/4, Claude, Bard (~84%). AdvBench: 500 behaviors + 500 strings; success = no refusal prefix.
- AutoDAN, Hotflip, TextFooler, DeepWordBug.
- PAIR (Chao et al. 2023): attacker LLM iteratively refines a jailbreak in ~20 queries (black-box).
- Low-resource language jailbreaks (e.g. Zulu) where alignment is thin.
- Few-shot demonstrations that contaminate context.
- Indirect prompt injection via documents, email, APIs: data exfiltration, tool abuse, resource loops, social engineering (poisoned resume).
- Prompt leakage: extract system prompt (IP, recon, brand risk).

Defenses belong with prompt security in §6.10.

## 6.9 Prompting `CORE`

A prompt is the input that steers an autoregressive LM. System prompt = standing rules; user prompt = the turn. Prompting is programming in natural language.

Ladder: zero-shot (instruction only) → few-shot (input/output exemplars) → CoT (explicit steps; stronger with few-shot and larger models) → self-consistency → ToT → ReAct → meta-prompting → directional stimulus.

**Self-consistency** (Wang et al., arXiv:2203.11171): a hard problem usually has several reasoning paths to one correct answer. Sample diverse CoTs instead of greedy decode; pick the answer that is most consistent after marginalizing paths. Lecture example: Janet’s 16 eggs, eat 3, bake 4, sell rest at $2 — greedy can output $14; sampled paths concentrate on $18.

**Tree of Thoughts** (Yao / Li et al., NeurIPS 2023): thoughts are nodes; combine generation with symbolic tree search (BFS or DFS), lookahead and backtracking. Self-evaluation of partial thoughts. Multi-expert pattern: several approaches, share, keep the highest-confidence branch. Costs more tokens; use when quality is worth the spend.

Zero-shot fails when the task is multi-step arithmetic without scaffolding (IIT example: 3/7 of 84). Few-shot still fails some parity / odd-sum puzzles; CoT repairs them.

**Auto-CoT** (Zhang et al., arXiv:2210.03493): cluster questions, pick a representative per cluster, generate a zero-shot-CoT demonstration (“Let’s think step by step”), use those as few-shot CoT. Comparable or better than hand-written CoT on reasoning tasks.

**ReAct** (Yao et al., ICLR 2023): interleave Thought → Act (tool/search) → Observation until Finish. Example: Taj Mahal city → Yamuna → origin; Apple Remote → Front Row, recovering from a failed search by refining the query. Thoughts decompose, extract, reformulate, and synthesize.

**Meta prompting** (Zhang, Yuan, Yao, arXiv:2311.11482): structure-oriented, not content-oriented. A skeleton such as: start with “Let’s think step by step”; reason in numbered steps; box the answer (`\boxed{}`); end with “The answer is …”. Syntax is the template; works across domains.

**Directional Stimulus Prompting** (Li et al., NeurIPS 2023): instance-specific hints (keywords a summary should cover, dialogue acts) generated from the query itself — not retrieved documents. A small policy LM (T5/GPT-2) is trained to emit the hints that steer a frozen black-box LLM.

## 6.10 Prompt optimization and security `CORE`

LLMs are sensitive to phrasing, order, and examples. Arbitrary edits cause inconsistency, token waste, hallucination, bad format, weak reasoning. Prompt optimization = systematically improving the prompt so outputs get better: manual iteration vs automatic search.

**Verbalized sampling** (Zhang et al., 2025, arXiv:2510.01171): training-free fix for mode collapse. Ask the model for k candidates (e.g. 5) with explicit probabilities, then sample from that verbalized distribution. Use for creative generation, brainstorming, social simulation, synthetic captions. Temperature / nucleus tuning is a weaker alternative when models disagree after retuning.

**Compression.** Basic: extract, summarize, drop low-value tokens. **LLMLingua** (Microsoft, arXiv:2310.05736): budget controller + token-level iterative compression + distribution alignment between a small compressor and the target LLM; typically 2–5× fewer tokens. **LLMLingua-2** (arXiv:2403.12968): replace perplexity heuristics with a learned compressor (teacher distillation, supervised token retention); 3–6× faster inference, better faithfulness and reasoning preservation, cheaper than LLMLingua.

Security (overlaps §6.8): injection, leaking, jailbreaks, backdoors; defenses (instruction hierarchy, output filters, least-privilege tools). Evaluation of prompts: statistical scorers vs model-based scorers.

## 6.11 Retrieval-augmented generation `CORE`

**Why.** Closed-book LLMs hallucinate (including fake citations), are hard to verify, go stale at the knowledge cutoff, and cannot see private or live data. Dangers: bad medical/engineering advice, confident DB writes, distorted history, stale procedures.

Putting everything in the prompt does not scale. RAG (Lewis et al., NeurIPS 2020): retrieve relevant docs → augment the prompt → generate a grounded answer.

**Naive RAG.** Index → retrieve top-k → generate. Assumes perfect retrieval and complete context. Breaks on multi-hop questions.

**Six-stage retrieval pipeline.** (1) Ingest (PDF/HTML/DB; **if the PDF is image-only, route to OCR, never to pypdf**). (2) Chunk. (3) Encode / index (dense embeddings or sparse inverted index). (4) Query processing (same representation as the index). (5) Retrieve and rank (cosine or BM25, top-k). (6) Optional cross-encoder rerank.

**Chunking strategies.** Fixed-size sliding window, typically 256–512 tokens with ~10% overlap (fast, can split mid-sentence). Sentence / paragraph splits (better coherence). Semantic chunking (cut where embedding similarity drops). Hierarchical / parent-child: retrieve a small chunk, send the larger parent to the LLM.

**Advanced RAG.** Pre-retrieval: query rewrite / expansion (domain terms, extra context). Post-retrieval: rerank, filter low-value chunks.

**Sparse vs dense.** Sparse (TF-IDF, BM25): keyword overlap, fast, interpretable; fails when query and doc share no words (“How much vacation do I get?” vs “Employees accrue 18 days of paid leave annually.”). Dense: embed query and chunks, k-NN in vector space. Hybrid: dense + sparse.

**Retrieve cheap, rerank dear.** Bi-encoder + ANN pulls a broad top-K; a cross-encoder rescores each (query, chunk) pair; top 5–20 go to the LLM. Rule of thumb from the lectures: most bad RAG answers start at retrieval; smaller chunks help recall; pick the embedder and store for the data; retrieve broadly then rerank.

**Query shaping (pre-retrieval).**

- Rewrite: LLM turns a vague query into a specific one (“attention paper” → “Attention Is All You Need / Transformer architecture”). Used in RAG-Fusion, Azure AI Search, LangChain SelfQueryRetriever.
- Conversational: resolve coreference and turn a follow-up into a standalone question. Used in ChatGPT-style retrieval, LangChain history-aware retrievers.
- Multi-query / RAG-Fusion: generate several phrasings, retrieve for each, union + dedup (LangChain MultiQueryRetriever, Promptagator).
- Step-back (Anthropic): retrieve a higher-abstraction question first (“How does attention work in Transformers?”) then answer the specific one.
- HyDE: embed a hypothetical document the model writes for the question, then search with that embedding.

**Indexing (vector DB).**

- **IVF / IVFFlat.** Cluster into `nlist` centroids (`nlist ≈ √N`); at query time scan `nprobe` lists. `nprobe=1` is fastest / lowest recall; `nprobe=nlist` degenerates to exact search.
- **Product quantization.** Split a D-vector into m subvectors; k-means a codebook per subspace; store codes not floats.
- **HNSW** (Hierarchical Navigable Small World). Multi-layer proximity graph; enter at the top (sparse) layer and zoom in. \(M\) = max edges per node (build-time recall/memory); `ef` = search width at layer 0 (the recall–speed knob, analogous to `nprobe`). Query cost ~ log N. Used inside FAISS, nmslib, Qdrant, Weaviate, Milvus.
- **FAISS vs Chroma.** FAISS is an ANN *library*: it returns vector IDs — you must keep the ID→text map or you lose the documents. Chroma is a *database* around that search: stores text, metadata, and the index together; supports `where={"source": "policy.docx"}` filters; default index is HNSW on CPU. Use Chroma for a working service in tens of lines; graduate to FAISS when you need billions of vectors or fine index control.

**Assessment.** Context precision / recall of retrieved chunks; groundedness of the answer; LLM-as-judge for faithfulness.

**Agentic RAG.** Linear retrieve→generate cannot plan. Complex tasks (find papers, summarize, compare, outline slides) need Plan → Act → Observe → Refine / Track, tools, and memory. **Triage pattern:** a triage agent decides who acts next; specialist agents always return control to triage after their step.

Enterprise pattern (Lecture 6): query rewrite; intent router to isolated sources (code hybrid BM25+embed, time-series logs, semantic policy/runbooks, tool APIs); context assembler; Vertex-style inference; LLM-as-judge; identity, least privilege, PII redaction, quotas, audit.

---

# 7. Inventory retained but out of teaching scope `ARCHIVE`

Kept so the source files lose no unique title or module. Not taught unless a CORE topic truly depends on a sliver.

- **M18** GST/VAT (CGST, SGST, IGST, ITC), banking RD, shares and dividends (Selina / Aggarwal Class 10 Ch. 1–3).
- **AccessMedicine** full suite (anatomy & physiology, biochemistry, microbiology, pathology, pharmacology, clinical diagnosis & treatment, radiology, and the specialty collections listed in §2).
- **PhD number theory as a destination:** Serre *A Course in Arithmetic*, Lang *Algebraic Number Theory*, Apostol analytic NT / prime-number theorem research, Hardy & Wright beyond elementary congruences, elliptic-curve research chapters. Undergraduate Burton / Silverman / Niven elementary chapters remain available as optional PREREQ enrichment.
- **Software-web stack as a destination:** Rippon React+TS, Cherny TypeScript. General SE books (Winters, Aniche, Hermans, Richards & Ford, Fowler) may be cited when M46 needs a practice, not taught as a track.
- **Game engines / real-time rendering** as a primary track (Gregory, Akenine-Möller). Matrix/transform facts already live under M27–M28 / M39.
- **Mechanical, fluid, aerospace** module lists in §2.
- **Clinical / AccessMedicine** inventory in §2.

---

# Source coverage check

| Source | Where it landed |
|---|---|
| `curriculum_unified_deduped.md` bibliography | §1 |
| Textbook deconstructions and ICSE/JEE/NT/DSP/ML ToCs | §2 (each book once; Rudin and Strang not repeated) |
| Eight-tier M1–M46, Kaldi spine, DL modules 1–8 | §3 |
| `iit-genai.md` Modules 1–13 | Folded into §3 Tiers 1, 4, 7, 8 |
| IIT Kharagpur EPGC (₹1,99,000) official pages | §3 official map |
| `python-libs.md` 21 libraries | §4 |
| Official NLP library docs: Hugging Face Transformers / Tokenizers, spaCy, NLTK Book | §4A |
| `stat-tech.md` 50 techniques | §5 |
| `lecture_slides_unified.md` 12 decks | §6 topic bank |
| Unrelated domains | §7 `ARCHIVE` |

## Restored or added in remigration

- IIT micro-bullets: propositional logic gates; row substitution and transpose; plane distance metrics; Bayes formula; cosine similarity as the embedding distance; system routing tokens, guard prompts, boundary checks, exception paths; structural parsing blocks; Docker minimal layers; token-cost functions.
- Lecture systems: 6-stage retrieval pipeline; four chunking strategies; HNSW (`M`, `ef`); FAISS vs Chroma; IVFFlat `nlist`/`nprobe`; OCR vs pypdf; ToT; self-consistency; triage agent.
- Official EPGC week map, faculty, five portfolio projects, SQL bridge, RAGAS metrics, LangGraph, fine-tune-vs-RAG-vs-prompt, VLM/image-gen list, named papers.
- NLP library theory section: shared text-processing substrate; NLTK corpora / taggers / lexical resources; spaCy Doc / Token / Span pipelines; Hugging Face tokenizers and transformers abstractions; cross-library alignment and evaluation contracts.
- New CORE textbooks with verified chapter maps: Hammack; Gonzalez & Woods; Szeliski (2e, all 15); Hartley & Zisserman (2e, 1–22); Manning/Raghavan/Schütze; Sutton & Barto; Boyd & Vandenberghe; MacKay; Murphy; Hopcroft/Motwani/Ullman; Huyen; Zhang et al. D2L; Prince; Rabiner & Juang; Huang/Acero/Hon (1–18); Yu & Deng (1–15); Quatieri (1–14).
