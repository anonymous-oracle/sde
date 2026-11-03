# Unified Curriculum: Mathematical Foundations → Machine Learning → Deep Learning → LLMs, RAG, Agents and Safety

**Built:** 2026-11-03, from `nptel.txt` (41 NPTEL and learner-supplied course outlines) and `iit-genai.md` (a 12-chapter, 78-section Generative AI course), under `Master_Rules.md`, Part III.1 (starting a course: generate the full structure first).
**Status:** structure for review. Per Master Rules III.1.9, the learner may add, reorder or (as a recorded override) remove anything before teaching starts. Nothing here has been taught yet; every topic is "not started".

---

## How to read this document

1. **Parts and domains.** Five parts, 17 domains (D1–D17). Each domain has an aim, named benchmarks, and units.
2. **Units.** A unit (`U<domain>.<n>`) is a group of related topics. Each has: **Sources** (generated: which source course weeks or outline cells it absorbs), **Topics** (every topic and subtopic, merged across sources and kept close to the sources' own words), **Results** (the theorems and formulas it teaches, each with a proof status), **Build** (the from-scratch implementation, with the professional tool as oracle afterwards), and **Gap-fills** (anything the references cover that the outlines miss, labelled *inferred* with its source).
3. **Proof-status tags** on results: **[P]** prove in full; **[D]** derive with every step; **[S]** proof sketch (the reason a full proof is not given is stated); **[X]** stated, proof deferred (the unit that will prove it, or "beyond course scope", is named); **[Def]** definition, not proved (Master Rules 4.2, 4.7, III.1.5).
4. **Source keys** (e.g. `MFML`, `GEN`) are listed in Appendix A. `W3` means Week 3 of that course; `o` means the course's outline or about-text; `GEN 4.5` means GenAI section 4.5.
5. **Merging rule.** Where several courses cover the same ground (for example, linear algebra draws on 14 sources and optimization on 16), they are merged into one unit at the deepest source level, and every source week is cited. The overlap is the point of unifying.

## Course profile (Master Rules II.1)

| Item | Value |
|---|---|
| **Aim** | Expert-level command of the mathematics of ML, classical and deep ML, generative models, LLMs, RAG and agents, evaluation and safety, with the three habits of the contest solver, the researcher and the architect (Master Rules section 10). Every algorithm is also implemented from scratch. |
| **Starting level** | No prior knowledge assumed beyond school mathematics (Class XII) and basic Python. Everything else, including proof technique, is taught (Master Rules III.1.6). |
| **Benchmarks** | Named per domain in each domain's intro. Titles marked *recalled, not checked* have not been verified against the book itself. Appendix E lists what was checked. |
| **Learner's standing instructions found in the source** | (a) "learn to implement these techniques from the scratch in python, numpy, etc." (b) weekly assignments exist for some courses and are wanted. (c) "If there are no assignments provided for certain topics, then create them." Recorded as overrides 0.3: scope = the whole course; date = 2026-11-03 (the file's date; the notes themselves are undated). Effect: every unit has a **Build**, and assignment slots are listed in Appendix G. |
| **Order of languages and tools** | Track 1: Python + NumPy only (from scratch). Track 2: SciPy, scikit-learn as oracles. Track 3: PyTorch for deep learning. MATLAB (named in one source) and TensorFlow are optional. The from-scratch track and the framework track are kept separate: a model is first built by hand, then re-built with the framework, and the two are compared (Master Rules 6.8). |
| **Acceptance gates (6.7)** | Formatter clean (`ruff format --check`), linter clean (`ruff check`), type check (`mypy`, optional), `pytest` passes, gradient checks within 1e-5 against finite differences, and results within stated tolerance of the oracle library. No hidden failure. |
| **Layer order for a topic (3.6)** | Concept and intuition → formal statement and derivation → from-scratch build → professional tool → real-world application and limits → check and close. |
| **Real-world lens (II.6)** | Name it, touch it in a lab, design with it. Cost tags: *local* for all from-scratch work; *replay-first, spend-capped* for any paid LLM API (Master Rules 11.2). |
| **Pacing (2.7, 8.5)** | The sources' durations (8 or 12 weeks, credits) describe their own pacing only. Here the learner advances by passing checks, never by the calendar. |
| **Cross-domain capstones (9.6)** | U17.1–U17.7, one per stretch, then one integrated final capstone. |
| **Record** | Appendix H gives the initial record. The live record belongs in the learner's tracker file. |

## Domain map

| Part | Domain | Units | Absorbs mainly |
|---|---|---|---|
| A. Mathematical foundations | D1 Discrete mathematics and reasoning | U1.1–U1.7 | DM, HEM, IM |
| | D2 Single-variable calculus and real analysis | U2.1–U2.5 | CAL1, EM1, AEMK, PMO |
| | D3 Multivariable and vector calculus | U3.1–U3.5 | EM1, EM2, AEMK, MFML, EMML |
| | D4 Linear algebra | U4.1–U4.11 | LAR, LAP, ALAB, ALAK, ALAJ, MFML, EMML |
| | D5 Probability and stochastic models | U5.1–U5.8 | IPS, PSS, MFML, AEMA, SMLM, S50 |
| | D6 Statistics and inference | U6.1–U6.6 | IPS, SMLM, S50, AEMA |
| | D7 Differential equations, complex analysis, transforms, numerics | U7.1–U7.6 | EM1, EM2, AEMK, AEMA, MM |
| | D8 Optimization | U8.1–U8.15 | PMO, CVX, OFF, OAT, OMLH, AOW, LPCS, DOML |
| B. Machine learning | D9 Classical ML, data mining, learning theory | U9.0–U9.14 | MLCE, MLDL, MLE, MLESA, FML, IMLK, MLK, DMIN, SMLM, GEN Ch.2 |
| | D10 Bandits and reinforcement learning | U10.1–U10.5 | BAN, MLESA, FDL |
| C. Deep learning and generative AI | D11 Deep learning foundations | U11.1–U11.8 | FDL, MLDL, MLE, MFML, GEN Ch.2–3 |
| | D12 NLP, Transformers, LLMs | U12.1–U12.10 | GEN Ch.1, 3–7, DLNLP, FDL |
| | D13 Deep generative models | U13.1–U13.8 | MFGAI, FML, FDL |
| D. LLM applications, evaluation, safety | D14 RAG and agentic systems | U14.1–U14.15 | GEN Ch.8–11 |
| | D15 Evaluation, safety, responsible AI | U15.1–U15.6 | GEN Ch.7, 12, DLNLP |
| E. Systems and integration | D16 ML systems and efficiency | U16.1–U16.6 | CSO, DOML |
| | D17 Integration and capstones | U17.1–U17.7 | none (assembles all) |

## Default order (a plan, not a cage: Master Rules 3.3)

| Stage | Units | Why here |
|---|---|---|
| 0 | U1.1; D2 | Proof habits and one-variable analysis before anything that uses limits. |
| 1 | U4.1–U4.6; U3.1–U3.2; U5.1–U5.5 | Vectors, matrices, eigen-structure, gradients and the language of probability: the minimum that ML notation needs. |
| 2 | U4.7–U4.10; U5.6–U5.7; D6; U3.3–U3.5 | Decompositions, least squares, joint distributions, inference, matrix calculus. |
| 3 | U8.1–U8.8; U9.0–U9.4 | Optimization basics and the first ML models, built by hand: regression, logistic regression, regularization, evaluation. |
| 4 | U8.9–U8.13; U9.5–U9.14; U1.2–U1.6; D7 | Duality, SVMs, kernels, trees, clustering, graphical models, learning theory; discrete structures and applied analysis as they are needed. |
| 5 | D11 | Deep learning (backpropagation uses U3.1, U3.5, U8.10). |
| 6 | D12; D10 | Attention, Transformers, LLMs, then alignment (needs RL: U10.4–U10.5). |
| 7 | D13 | Generative models (needs U5.6, U9.9, U9.10, U13.1 foundations, U7.5). |
| 8 | D14; D15 | RAG, agents, evaluation and safety. |
| 9 | D16; U8.14; D17 | Systems, distributed and federated learning, capstones. |

Just-in-time rule: a prerequisite from another domain is taught immediately before the topic that first uses it (Master Rules 3.3), and the stage table above is updated when that happens.

## Coverage guarantee: what was checked and how

- **Cells.** Every source week, outline, lecture-block and GenAI section is a "cell": 460 cells from `nptel.txt` and 78 from `iit-genai.md`, 538 in all. **All 538 are cited by at least one unit** (Appendix B lists the full matrix).
- **Atoms.** Each cell's text was split into 3,300+ topic atoms. A script checked that each atom's key words appear in the units that cite its cell. The atoms it still flags (listed in Appendix F) are **source typos** (for example "Grpah", "Dula", "diinensionality"), **section labels**, and **descriptive prose** (audience, marketing sentences), none of which is a topic.
- **Limits of the check.** It is a word-level check, not a proof of meaning; it cannot confirm that a topic is explained well. Outline prose was reviewed by hand once after the script ran.
- **Nothing was dropped to save space.** Overlapping courses are merged, never sampled. Repeated or truncated source text is flagged in Appendix F rather than silently fixed.

---



# PART A. MATHEMATICAL FOUNDATIONS

## D1. Discrete Mathematics and Mathematical Reasoning

Aim: proof fluency, counting, graphs, number theory and algebra. Taught early because every later proof (limits, linear algebra, probability, learning theory) rests on the proof paradigms here. Benchmarks (recalled, not checked): Rosen, *Discrete Mathematics and Its Applications*; Lovász–Pelikán–Vesztergombi, *Discrete Mathematics*; Graham–Knuth–Patashnik, *Concrete Mathematics*; West, *Introduction to Graph Theory*; Artin, *Algebra*.

### U1.1 Logic, proof paradigms and formal languages
**Sources:** DM W1, o; HEM W1–2, o; IM o
- **Topics:** Formalizing proofs and proof paradigms; representation of statements; duality; tautologies and contradictions; quantifiers; predicates and validity of arguments; propositional logics; languages and grammar; finite state machines and their transition table diagrams; the idea of mathematics beyond "procedures-to-solve-routine-problems"; interconnections between seemingly disjoint topics; HEM main topics: discrete mathematics, graph theory, linear programming problems, queuing theory; discrete mathematics as the study of mathematical structures that are discrete (elements take finite values as opposed to continuous structures); five main topics: proofs, combinatorics, graphs, number theory and algebra; the course will be full of puzzles and CS examples.
- **Results:** Equivalence laws and duality principle [P]; soundness of standard inference rules (modus ponens, resolution) [P]; principle of mathematical induction and strong induction [P].
- **Build:** a truth-table and tautology checker in Python; a DFA simulator driven by a transition table.
- **Gap-fills:** *[inferred: Rosen]* direct proof, contrapositive, contradiction, cases, induction, strong induction, structural induction, well-ordering; sets, relations and functions as the common language; regular languages and context-free grammars as the bridge to formal-language theory (see language-theory track).

### U1.2 Counting, generating functions and combinatorics
**Sources:** DM W2–3; IM A
- **Topics:** Counting; generating functions; basic combinatorics; counting principles (basic methods, the pigeonhole principle, the binomial theorem, permutations, graphs, recurrence relations, bijective proofs); polynomials in several variables and counting monomials.
- **Results:** Binomial theorem [P]; pigeonhole principle and generalized form [P]; inclusion–exclusion [P]; solution of linear recurrences by characteristic roots and by generating functions [D]; bijective proof of Vandermonde-type identities [P].
- **Build:** recurrence solver and coefficient extraction from power series using NumPy; brute-force verification of counting formulas on small cases.
- **Gap-fills:** *[inferred: Concrete Mathematics; Lovász]* ordinary and exponential generating functions, partitions, Catalan numbers, Stirling numbers, derangements, double counting.

### U1.3 Posets, lattices, Boolean algebra and switching circuits
**Sources:** DM W4; HEM W2–5
- **Topics:** Posets, chains and anti-chains; partially ordered sets I and II; duality and lattices as an algebraic system; sublattice I and II; Boolean algebra; switching algebra; Boolean functions; different representations of Boolean functions; circuit minimization and simplification (I and II); Karnaugh map I and II; table diagrams (of Boolean functions and of finite-state machines).
- **Results:** Dilworth's theorem [P]; Mirsky's theorem [P]; Boolean algebra axioms imply duality and De Morgan laws [P]; canonical (sum-of-products) form exists and is unique [P].
- **Build:** Quine–McCluskey minimizer from scratch; checked against hand Karnaugh-map reductions.
- **Gap-fills:** *[inferred: Rosen]* Hasse diagrams, Sperner's theorem, distributive and complemented lattices, Stone representation (statement).

### U1.4 Graph theory
**Sources:** DM W5–7; HEM W5–8
- **Topics:** Basic graph theory; various types of graph; tours, cycles, cliques, covers; Eulerian and Hamiltonian graphs; travelling salesman problem; vertex and edge connectivity; matrix representation of graphs (incidence and adjacency matrices); coloring, matching, planarity; planar graphs; Kuratowski's theorem; detection of planarity; Euler's formula; dual of a planar graph; colouring of graphs; chromatic numbers; four colour theorem; various types of graphs; dual of a planar graph.
- **Results:** Handshake lemma [P]; Euler's circuit theorem [P]; Euler's formula V−E+F=2 [P]; Kuratowski's theorem [X→proof deferred, stated with the two obstruction graphs]; five-colour theorem [P]; four-colour theorem [X]; Hall's marriage theorem [P]; König's theorem [P]; Menger / max-flow–min-cut [X→U8.6, proved there by LP duality].
- **Build:** graph class with adjacency/incidence matrices, BFS/DFS, bipartiteness and Euler-tour test; greedy and DSATUR colouring; TSP by dynamic programming (Held–Karp) at toy size.
- **Gap-fills:** *[inferred: West]* trees and spanning trees (Kruskal, Prim), shortest paths (Dijkstra), Dirac and Ore conditions, Ramsey's theorem, spectral graph theory (adjacency/Laplacian eigenvalues; link to U4.8 and to spectral clustering in U9.9).

### U1.5 Number theory and cryptography
**Sources:** DM W8–9; IM A
- **Topics:** Basic number theory; elementary number theory (modular arithmetic, divisibility, prime numbers); density of primes; cryptography.
- **Results:** Euclid's algorithm and Bézout's identity [P]; fundamental theorem of arithmetic [P]; Chinese remainder theorem [P]; Fermat's little theorem and Euler's theorem [P]; infinitude of primes [P]; Chebyshev-type density bounds [S]; prime number theorem [X]; correctness of RSA [P].
- **Build:** extended Euclid, fast modular exponentiation, Miller–Rabin and toy RSA from scratch. Hand-built cryptography is for learning only and is never deployed (Master Rules 6.8).
- **Gap-fills:** *[inferred: Hardy–Wright; Rosen]* primality tests, Diffie–Hellman, discrete logarithm, hashing as modular arithmetic.

### U1.6 Algebra: finite fields, codes, groups and orbit counting
**Sources:** DM W10–12
- **Topics:** Finite fields; codes; basic group theory; orbit counting; normal subgroups.
- **Results:** Lagrange's theorem [P]; existence and uniqueness of finite fields of order p^n [S]; Hamming bound and distance of linear codes [P]; orbit–stabilizer theorem [P]; Burnside's lemma [P]; first isomorphism theorem for groups [P].
- **Build:** GF(2^m) arithmetic; Hamming and Reed–Solomon encoder/decoder at toy size; Burnside-count of necklaces by enumeration versus formula.
- **Gap-fills:** *[inferred: Artin; MacWilliams–Sloane]* cyclic groups, permutation groups (link to U4.5 signature of a permutation), quotient groups, BCH codes.

### U1.7 An invitation to mathematics: polynomials, functions, matrices, conservation laws
**Sources:** IM o, A
- **Topics:** Polynomials (interpolation, Taylor's formula, polynomials with integer values, polynomials in several variables, counting monomials); functions (continuous functions, the intermediate value property and its applications, fixed points, linear transformations of the plane, the derivative and dilations, higher-order derivatives and the binomial theorem, polynomial approximation to functions); matrices (matrices and transformations, multiplication versus composition, determinants as dilation factors, polynomials applied to matrices, matrices in probability theory, matrices in polynomial interpolation, the Vandermonde determinant); conservation laws (invariants of transformations, discrete transformations and applications, transformations in Euclidean geometry, circle inversions); elementary number theory (modular arithmetic, divisibility, prime numbers).
- **Results:** Lagrange interpolation uniqueness [P]; intermediate value theorem [P in U2.2]; Vandermonde determinant [D]; invariants as proof tool [P].
- **Build:** interpolation and Vandermonde solve in NumPy, with condition-number growth observed (bridge to U4.9).
- **Gap-fills:** this unit is a conceptual bridge; each theme is taught again at depth in D2, D4 and D1.5.

## D2. Single-Variable Calculus and Real Analysis

Aim: a rigorous single-variable calculus (Spivak-style) plus the analysis vocabulary that optimization, probability and learning theory later use. Benchmarks (recalled, not checked): Spivak, *Calculus*; Thomas–Finney, *Calculus and Analytic Geometry*; Cheney, *Analysis for Applied Mathematics*; Rudin, *Principles of Mathematical Analysis*.

### U2.1 Numbers, countability, functions, limits and continuity
**Sources:** CAL1 W1–2, o; PMO W1–2; OFF W1
- **Topics:** Introduction to numbers; countability and uncountability; examples of irrational numbers; functions; limits of functions I and II; continuous functions; intermediate value theorem; maximum value theorem; supremum and infimum; sets in Rn (balls, neighbourhood, interior point, open sets, closed sets, bounded sets, compact sets, level sets, epigraphs); supremum and infimum of a set; sequence, subsequence, limsup and liminf; order of convergence of a sequence; limit, continuity, uniform continuity and Lipschitz continuity and their geometries; overview of real analysis.
- **Results:** Uncountability of the reals (diagonal argument) [P]; completeness (least upper bound) [Def]; intermediate value theorem [P]; extreme value (maximum value) theorem [P]; Bolzano–Weierstrass [P]; Heine–Borel for Rn [S].
- **Build:** bisection and ε–δ explorers in Python; numerical estimation of convergence order from an error sequence.
- **Gap-fills:** *[inferred: Spivak; Cheney]* metric spaces and normed spaces (needed by D4 norms and D8), Cauchy sequences, completeness of Rn.

### U2.2 Differentiation and mean value theorems
**Sources:** CAL1 W3–4; EM1 W1, o; AEMK W1; PMO W2
- **Topics:** Derivative of a function; rules of differentiation; derivatives, maxima and minima; Rolle's theorem and Lagrange MVT (mean-value theorem); Cauchy's mean value theorem; differentiability; monotonic functions and inverse function; differential calculus of functions of one variable; indeterminate forms; Newton's method for solving equations; optimization problems; little-oh and big-Oh notations.
- **Results:** Rolle and Lagrange mean value theorems [P]; Cauchy mean value theorem [P]; L'Hôpital's rule (indeterminate forms) [P]; inverse function theorem in one variable [P]; first and second derivative tests [P]; local quadratic convergence of Newton's method [D].
- **Build:** Newton and secant solvers from scratch, with the error curve plotted against the predicted order (links to U8.8).
- **Gap-fills:** *[inferred: Thomas–Finney]* related rates and curve sketching as applied optimization problems.

### U2.3 Integration, applications and transcendental functions
**Sources:** CAL1 W4–7; EM1 o; AEMK W2
- **Topics:** Integration I, II, III in the style and spirit of Newton and Leibnitz; indefinite integrals; integration by parts; integration of rational functions; trapezoidal rule for evaluating a definite integral; Simpson's rule for evaluating a definite integral; applications of definite integral I–IV; transcendental functions I and II; surface and volume of revolution; calculation of centre of gravity and centre of mass; area and volume as integrals.
- **Results:** Fundamental theorem of calculus (both parts) [P]; integrability of continuous functions [S]; error bounds for trapezoid and Simpson rules [D]; properties of exp and log from their integral definition [P].
- **Build:** trapezoid, Simpson and adaptive quadrature in NumPy, checked against `scipy.integrate`.
- **Gap-fills:** *[inferred: Thomas–Finney]* partial fractions procedure and trigonometric substitutions; Riemann sums and the Riemann–Darboux definition.

### U2.4 Taylor expansion, sequences, series and power series
**Sources:** CAL1 W7–8; EM1 o; AEMK W1; MFML W9; PMO W2
- **Topics:** Taylor's expansion I and II; Taylor's and Maclaurin's theorems and series; infinite sequence I and II; infinite series and their convergence; tests for convergence of a series; absolute and conditional convergence; power series; Taylor's theorem with remainder in little-o and big-O form; historical development of the calculus.
- **Results:** Taylor's theorem with Lagrange remainder [P]; ratio, root and comparison tests [P]; Abel/radius-of-convergence theorem (Cauchy–Hadamard) [P]; Rearrangement of conditionally convergent series (Riemann) [S].
- **Build:** Taylor polynomials of exp, sin, log with error versus remainder bound.
- **Gap-fills:** *[inferred: Spivak]* uniform convergence of series (needed in D7 Fourier and complex analysis).

### U2.5 Improper integrals, Gamma and Beta functions, integrals dependent on parameters
**Sources:** EM1 W5, o; AEMK W2
- **Topics:** Improper integrals; convergence of improper integral; tests of convergence; Gamma and Beta functions and their properties; differentiation under the integral sign; Leibnitz rule of differentiation; integrals dependent on parameters and applications.
- **Results:** Comparison and limit-comparison tests for improper integrals [P]; Γ(n+1)=nΓ(n) and the Beta–Gamma relation [P]; Leibniz rule [P under uniform-convergence conditions].
- **Build:** numerical evaluation of Γ and B and moment integrals used later in D5 (Gamma, Beta and normal densities).
- **Gap-fills:** *[inferred: Kreyszig]* Gaussian integral (needed for D5 normal distribution).

## D3. Multivariable and Vector Calculus

Aim: derivatives, integrals and fields in several variables, the machinery behind gradients, Jacobians, Hessians and backpropagation. Benchmarks (recalled, not checked): Thomas' Calculus; Kreyszig, *Advanced Engineering Mathematics*; Piskunov, *Differential and Integral Calculus*; Deisenroth et al., *Mathematics for Machine Learning*, Ch. 5.

### U3.1 Functions of several variables, partial derivatives and differentiability
**Sources:** EM1 W2–3, o; AEMK W1, o; MFML W9; EMML W7; PMO W1–2; OMLH W1–2
- **Topics:** Functions of several variables; limit and continuity; partial derivatives and their geometrical interpretation; total differential and differentiability; derivatives of composite and implicit functions; implicit function theorem; derivatives of higher order and their commutativity; Euler's theorem on homogeneous functions; partial derivative, gradient, Hessian, directional derivative; differentiability and the hierarchy of partial derivatives, directional derivatives and differentiability; chain rule; gradient, Jacobian and Hessian; change of variables; vector calculus; basic concepts of calculus; tools from calculus of several variables; hierarchy of PDs (partial derivatives), DD (directional derivatives) and differentiability.
- **Results:** Equality of mixed partials (Schwarz/Clairaut) [P]; chain rule in several variables [P]; differentiability implies directional derivatives and continuity, with the converse counterexamples [P]; implicit function theorem [S, proof sketch via contraction mapping]; Euler's homogeneous function theorem [P].
- **Build:** numerical gradient and Jacobian checker (finite differences) and tape-based reverse-mode differentiation from scratch (bridge to U11.2 backpropagation).
- **Gap-fills:** *[inferred: MML Ch.5]* gradients of vector-valued functions, gradients of matrices, useful identities, automatic differentiation (forward and reverse mode).

### U3.2 Taylor expansion in several variables, maxima, minima and Lagrange multipliers
**Sources:** EM1 W4, o; AEMK W1; MFML W9
- **Topics:** Taylor's expansion of functions of several variables; Taylor's series with gradient and Hessian terms; maxima and minima; saddle points; constrained maxima/minima problems using Lagrange's method of multipliers.
- **Results:** Second-order Taylor expansion with remainder [P]; second-derivative test via Hessian definiteness [P]; Lagrange multiplier rule for equality constraints [D]; KKT conditions [X→U8.5].
- **Build:** Newton step on a two-variable function, with Hessian eigenvalues classifying the stationary point.

### U3.3 Multiple integrals and their applications
**Sources:** EM1 W6–7, o; AEMK W2
- **Topics:** Double and triple integrals; multiple integrals and their properties; change of order of integration; change of variables; Jacobian transformation; Fubini theorem; surface, area and volume integrals; applications of multiple integrals.
- **Results:** Fubini's theorem [S, statement and conditions]; change-of-variables formula with Jacobian determinant [S; derived for linear maps in U4.5]; polar/spherical coordinates [D].
- **Build:** Monte Carlo and grid evaluation of double integrals (forward link to D5 Monte Carlo).

### U3.4 Vector calculus: fields, line and surface integrals, Green, Gauss and Stokes
**Sources:** EM2 W1–2, o; AEMK W9–11
- **Topics:** Vector and scalar fields; level surface; limit, continuity and differentiability of vector functions; curve and arc length; unit vectors; directional derivatives; divergence, gradient and curl; some applications to mechanics; tangent, normal and binormal; Serret–Frenet formulae; line integral; parametric representations; surface integral; volume integral; line and surface integrals; Green's, Gauss' divergence and Stokes' theorems; vector and scalar fields; limit, continuity and differentiability of vector functions; directional derivative, gradient, curl, divergence; line and surface integrals; Green, Gauss and Stokes theorems.
- **Results:** Green's theorem [P for simple regions]; divergence (Gauss) theorem [S]; Stokes' theorem [S]; conservative-field criterion [P]; Frenet–Serret equations [D].
- **Build:** numerical line and flux integrals; verification of Green/Gauss on a test field.
- **Gap-fills:** *[inferred: Kreyszig]* Laplacian and harmonic functions (links to D7 complex analysis); divergence of vector fields as it reappears in D13 continuity and Fokker–Planck equations.

### U3.5 Matrix calculus, Jacobians and Hessians for machine learning
**Sources:** MFML W10; EMML W7–8
- **Topics:** Matrix derivatives; basic concepts of calculus, gradient, Jacobian, chain rule, change of variables; calculus in Python; Jacobian and Hessian of scalar and vector functions of matrices.
- **Results:** Gradients of trace, quadratic form and log-determinant [D]; chain rule in matrix form for a two-layer network [D].
- **Build:** NumPy autodiff-checking of every matrix-derivative identity against finite differences.
- **Gap-fills:** *[inferred: MML Ch.5; Petersen–Pedersen Matrix Cookbook]* gradients of the least-squares loss and softmax cross-entropy used in D9 and D11.

## D4. Linear Algebra: Core, Abstract, Numerical and Applied

Aim: five source courses (basic, abstract/coordinate-free, advanced canonical forms, numerical/applied for ML, signal-processing applications) merged into one ladder: computation first, then structure, then decompositions, then applications. Benchmarks (recalled, not checked): Strang, *Introduction to Linear Algebra* (5th ed.) and *Learning from Data*; Axler, *Linear Algebra Done Right* (3rd ed.); Hoffman–Kunze; Halmos; Artin; Greub; Jacobson; Deisenroth et al. Ch. 2–4; Trefethen–Bau, *Numerical Linear Algebra*; Golub–Van Loan.

### U4.1 Systems of linear equations, matrices, elimination, rank and inverses
**Sources:** LAR W1–4, o; LAP W2,9; ALAB o, P1; EM1 W8, o; AEMK W6–7; EMML W1, o; MFML W1, o; ALAK W2; MLE W1; MLESA W0
- **Topics:** Matrices and matrix operations; row echelon form (REF); linear systems; Gauss elimination and inverse of a matrix; system of linear equations (review); elementary matrix operations, elementary matrices and elementary operations on matrices; rank of a matrix and its properties; computation of the rank; matrix inverse; determinants, rank, invertibility; computational rules for matrices; row and column reduced matrices; echelon matrix and its properties; solution of a system of equations using rank concepts; homogeneous and non-homogeneous systems; existence and uniqueness of solutions; left and right inverses; pseudo inverse; triangular systems; basics of matrix algebra; Gauss elimination for homogeneous and non-homogeneous equations; system of linear equations – Gauss elimination; system of linear equations; Gauss elimination (Gauss-Jordan).
- **Results:** Row operations preserve solution set [P]; rank = row rank = column rank [P]; solvability criterion rank(A)=rank([A|b]) [P]; uniqueness of reduced row echelon form [P]; an n×n matrix is invertible iff rank n iff det≠0 [P].
- **Build:** Gaussian elimination with partial pivoting, RREF, rank and inverse from scratch; compare with `numpy.linalg`.
- **Gap-fills:** *[inferred: Strang Ch.1–3]* four fundamental subspaces, column picture versus row picture, block matrices and matrix multiplication as four equivalent views.

### U4.2 Vectors, vector spaces, subspaces, bases and dimension
**Sources:** LAP W1–4, o; LAR W3; ALAB P1, P2; EM1 W8, o; AEMK W6; EMML W1; MFML W1; ALAK W1; ALAJ W1; PMO W1; OMLH W1–2
- **Topics:** Vectors, operations on vectors, properties and applications; introduction to algebraic structures (rings and fields); definition of vector spaces and examples; definition of subspaces and examples (continued); sum of subspaces; generating system, linear dependence and independence, and bases; Rn, subspaces, linear independence; examples of a basis of a vector space; review of univariate polynomials, examples of univariate polynomials and rational functions; vector spaces with finite generating system; Steinitz's exchange theorem and examples; examples of finite-dimensional vector spaces; dimension formula and its examples; existence of a basis; vectors in machine learning; vector space, subspace, basis and dimension; ordered basis and coordinate matrix; computations concerning subspaces; vector spaces over an arbitrary scalar field (even a finite field); coordinate-free algebraic methods; basis and dimension of a vector space; subspaces.
- **Results:** Steinitz exchange lemma [P]; any two bases have equal cardinality (dimension well defined) [P]; existence of a basis in finite-dimensional spaces [P]; dimension formula dim(U+W)=dim U+dim W−dim(U∩W) [P].
- **Build:** subspace-membership, basis extraction and dimension tools using exact rational arithmetic and then floating point (observe rank decisions with tolerance).
- **Gap-fills:** *[inferred: Axler Ch.1–2]* span, list length versus independence, infinite-dimensional examples (polynomials, sequences, function spaces) as motivation for D13.

### U4.3 Linear maps, representation by matrices, duality and quotient spaces
**Sources:** LAP W5–8; LAR W5; ALAB P1, P2, o; EM1 W9, o; AEMK W6; MFML W2; EMML W2; PMO W1; ALAK W1
- **Topics:** Introduction to linear maps; examples of linear maps; linear maps and bases; pigeonhole principle in linear algebra; interpolation and the rank theorem; direct sums of vector spaces; projections; direct-sum decomposition of a vector space; dimension equality; dual spaces; quotient spaces; homomorphism theorem of vector spaces; isomorphism theorem of vector spaces; matrix of a linear map; change of bases; linear transformation; existence of linear transformation; rank–nullity theorem; representation of transformations by matrices; change of ordered basis and matrix representation of transformations; algebra of linear transformations; linear operators and linear functionals; dual space and double dual space; transpose of a linear transformation; linear transformations (EM1 Week 9); rank-nullity; linear transformations; linear transformations (ALAK Week 1); linear transformations.
- **Results:** Rank–nullity theorem [P]; a linear map is determined by its action on a basis [P]; isomorphism theorem for vector spaces [P]; V ≅ V** for finite dimension [P]; matrix of composite is product of matrices [P]; change-of-basis formula [D].
- **Build:** matrix of a map in arbitrary bases, change of basis and the effect on a matrix; null space and range via SVD, from scratch after U4.9.
- **Gap-fills:** *[inferred: Axler Ch.3]* invertibility and isomorphic vector spaces; linear transformations of the plane (rotation, shear, reflection) as pictures.

### U4.4 Inner products, norms, orthogonality, projections and Gram–Schmidt
**Sources:** LAR W6; ALAB P4; MFML W3; EMML W2,6; ALAK W1,3; ALAJ W1; PMO W1; AOW W1
- **Topics:** Inner product spaces; inner products and norms; matrix norms; Gramian matrix; Gram–Schmidt orthogonalization and process; orthogonal complements and orthogonal complement; best approximation; orthogonality, projection and real symmetric matrices (Week 3); projection mapping; norms and spaces; inner product and vector norm; orthogonal matrices; rotators and reflectors; QR decomposition; properties of vectors and norms.
- **Results:** Cauchy–Schwarz and triangle inequalities [P]; Gram–Schmidt produces an orthonormal basis [P]; orthogonal projection onto a subspace is the best approximation (Pythagoras) [P]; V = W ⊕ W^⊥ [P]; projection matrix P = A(AᵀA)⁻¹Aᵀ [D]; equivalence of norms on Rn [S].
- **Build:** classical and modified Gram–Schmidt, Householder QR and Givens rotators from scratch, observing loss of orthogonality (MGS vs CGS).
- **Gap-fills:** *[inferred: MML Ch.3]* analytic geometry: lengths, distances, angles, orthonormal bases, orthogonal projections, rotations; p-norms and the unit ball geometry (links to L1 sparsity in U9.4).

### U4.5 Determinants, multilinear forms and permutations
**Sources:** LAP W10–12, o; LAR W4
- **Topics:** Permutation groups; canonical cycle decomposition of permutations; signature of a permutation; introduction to multilinear maps; multilinear maps (continued); introduction to determinants; determinants (continued); computational rules for determinants; properties of determinants and adjoint of a matrix; adjoint–determinant theorem; the determinant of a linear operator; determinants and volumes (and continued); LR decomposition; elementary divisor theorem; determinants via the theory of multilinear forms.
- **Results:** Existence and uniqueness of an alternating n-linear form with det(I)=1 [P]; det(AB)=det A·det B [P]; adjoint–determinant theorem A·adj(A)=det(A)·I [P]; |det A| is the volume scaling factor [D]; Cramer's rule [P].
- **Build:** determinant by permutation expansion, by LU, and by cofactor, with cost measured; volume of a parallelepiped.
- **Gap-fills:** *[inferred: Strang Ch.5]* determinant as dilation factor (links to change of variables in U3.3 and normalizing flows in D13).

### U4.6 Eigenvalues, eigenvectors, similarity and diagonalization
**Sources:** LAR W7–8; EM1 W10, o; AEMK W8; MFML W2; EMML W2; ALAJ W3; ALAB P3; LAP o
- **Topics:** Eigenvalues and eigenvectors; similarity, diagonalization and applications; characteristic values and diagonalization (review); Hermitian, skew-Hermitian and unitary matrices and their eigenvalue properties; similarity of matrices; diagonalization of matrices; special matrices and properties; eigenvalue decomposition, properties and applications; characteristic polynomial; algebraic versus geometric multiplicity.
- **Results:** Eigenvectors for distinct eigenvalues are independent [P]; diagonalizability criterion (geometric = algebraic multiplicity) [P]; similar matrices share characteristic polynomial [P]; trace = sum and det = product of eigenvalues [P]; Cayley–Hamilton [P in U4.7].
- **Build:** power iteration, inverse iteration and QR iteration from scratch, checked against `numpy.linalg.eig`.
- **Gap-fills:** *[inferred: Strang Ch.6]* powers of a matrix, difference/differential equation solutions via eigen-decomposition (feeds D7 and D10).

### U4.7 Canonical forms: minimal polynomial, invariant subspaces, Jordan and rational forms
**Sources:** ALAB o, P3; EMML W6; LAP W10
- **Topics:** Annihilating polynomials; minimal polynomial; invariant subspace; triangulation (two lectures); simultaneous triangulation and simultaneous diagonalization; direct-sum decomposition; invariant direct sums; the primary decomposition theorem; Jordan forms and Jordan canonical form; rational form; elementary divisor theorem; canonical forms and Jordan forms (course component iv).
- **Results:** Cayley–Hamilton theorem [P]; minimal polynomial divides every annihilating polynomial [P]; triangulability over algebraically closed fields [P]; primary decomposition theorem [P]; existence and uniqueness of Jordan form [S]; rational canonical form [X, proof beyond course scope, stated].
- **Build:** Jordan-chain computation for small matrices with exact arithmetic; demonstrate numerical instability of Jordan form in floating point.

### U4.8 Spectral theory: normal operators, symmetric matrices, quadratic forms, PSD matrices and kernels
**Sources:** ALAB o, P4; MFML W3; EMML W3; PMO W1; OMLH W1–2; AOW W1; AEMK W8; ALAK W8, o
- **Topics:** Operators on inner-product spaces; the adjoint of a linear operator; normal and self-adjoint operators; unitary and orthogonal operators and their matrices; bilinear and quadratic forms; orthogonal projections and the spectral theorem; spectral decomposition; spectral theorem for symmetric matrices; real symmetric matrices; definiteness of matrices (eigenvalue criterion and Sylvester criterion); quadratic forms and quadratic functions; positive semi-definite (PSD) matrices and kernel functions; Gaussian random vectors; eigenvalue-eigenvector decomposition of square matrices.
- **Results:** Spectral theorem for real symmetric / Hermitian matrices [P]; spectral theorem for normal operators [P]; Sylvester's criterion [P]; PSD ⇔ nonnegative eigenvalues ⇔ Gram form [P]; Mercer-type statement for kernel matrices [S, used in U9.5].
- **Build:** Jacobi eigenvalue algorithm for symmetric matrices; PSD test by Cholesky; Gram-matrix kernel construction.
- **Gap-fills:** *[inferred: MML Ch.4]* Cholesky decomposition, Rayleigh quotient and variational characterization of eigenvalues (needed for PCA in U9.7).

### U4.9 LU, QR, conditioning, SVD, pseudo-inverse and low-rank approximation
**Sources:** ALAK W2–4,9,12, o; ALAB P4, o; EMML W3,6; MFML W4; ALAJ W4; PMO W1; OMLH W1–2
- **Topics:** LU decomposition and computational complexity; rotators and reflectors; QR decomposition; condition number of a square matrix and its geometric interpretation; norm of a matrix; sensitivity analysis results for the system of linear equations; singular value decomposition (SVD), relation to condition number, sensitivity analysis of least squares problems and variation in parameter estimates in regression; generalized (g-) inverse and pseudo-inverse; low-rank approximation (LRA) and structured low-rank approximation (SLRA); polar decomposition; spectral decomposition; Python implementation of SVD and low-rank approximation; SVD algorithms and methods; applications of SVD: beamforming in MIMO, dimensionality reduction, rate maximization in wireless, MUSIC algorithm; alternating projections for computing LRA and SLRA; approximate GCD computation; singular value decomposition (SVD) as component vii of advanced linear algebra.
- **Results:** Existence of SVD [P]; Eckart–Young–Mirsky low-rank optimality [P]; cond(A)=σmax/σmin and error amplification bound [D]; Moore–Penrose pseudo-inverse via SVD, four defining equations [P]; polar decomposition [P].
- **Build:** SVD via eigendecomposition of AᵀA, then one-sided Jacobi/Golub–Kahan from scratch; image compression by truncated SVD; compare with `numpy.linalg.svd`.
- **Gap-fills:** *[inferred: Trefethen–Bau; Strang Ch.7]* floating-point arithmetic, backward stability, Cholesky, randomized SVD (links to LoRA in U12.7).

### U4.10 Least squares, regularized and constrained least squares
**Sources:** ALAK W5–7, o; ALAJ W5–6; EMML W5; MFML W10
- **Topics:** Linear least squares: existence and uniqueness, geometrical interpretation, data fitting with least squares, feature engineering, application to vector auto-regressive models, fitting with continuous and discontinuous piecewise linear functions; application of least squares to classification (two-class and multi-class least-squares classifiers, polynomial classifiers, MNIST data set); multi-objective least squares; applications to estimation and regularized inversion; regularized data fitting and image de-blurring; constrained least squares; application to portfolio optimization; least square approximation and minimum-norm solution; linear regression and least squares; optimal linear MMSE estimation; applications: system identification, MMSE receiver, market prediction and forecasting, ARMA models; least squares and PCA; concept of cost function and relation to parameter estimation; parameter estimation problems; applications to portfolio optimization.
- **Results:** Normal equations characterize the minimizer [P]; solution via QR and via SVD [D]; Gauss–Markov (BLUE) [P in U6.4]; ridge solution and its SVD shrinkage form [D]; KKT system for equality-constrained least squares [D].
- **Build:** least squares by normal equations, QR and SVD with conditioning experiments; ridge and weighted LS; polynomial classifier on MNIST via LS.

### U4.11 Applications of linear algebra: PageRank, sparsity, dynamical systems, Markov chains, signal processing and data analytics
**Sources:** ALAK W10–12, o; ALAJ W2–4,7–12, o; EMML W6; LAP o
- **Topics:** Applications of matrices – circuits, graphs, social networks, traffic flow; eigenvalue decomposition applications – principal component analysis (PCA), eigenfaces for facial recognition; multicollinearity problem and PCA and dimensionality reduction; power method and the Google PageRank algorithm; underdetermined systems of linear equations, least-norm solutions, sparse solutions, dictionary learning and sparse code recovery; inverse eigenvalue problem and construction of Markov chains from a given stationary distribution; low-rank approximation and structured low-rank approximation with model order selection in time series (Hankel SLRA, autoregressive model order selection); image de-blurring; tensors and CP tensor decomposition, tensor-decomposition-based sparse learning in deep networks; matrix completion problems and collaborative filtering; data analytics: recommender systems, user rating prediction, the Netflix problem; structure of FFT/IFFT matrices and their properties; system model for OFDM/SC-FDMA and signal processing in OFDM systems; modelling of dynamical systems (robots, chemical plants), solution of autonomous linear dynamical systems (LDS) and solution with inputs and outputs; unsupervised learning: centroid-based clustering, probabilistic model-based clustering and the EM algorithm; linear perceptron and training a perceptron by stochastic gradient; compressive sensing and orthogonal matching pursuit for sparse signal estimation; discrete-time Markov chains with applications to supply chain management, forecasting and operations research (resource and inventory management); applications in wireless (MIMO/OFDM, beamforming, channel estimation), machine learning (regression, clustering, EM algorithm, perceptron, SVM, kernel SVM, PCA, face recognition), signal processing (signal estimation, regularization, compressive sensing, image compression, robotics and dynamical systems), data analytics (recommender systems, data completion, data prediction, forecasting, optimal estimation, financial models), operations research and miscellaneous applications; application to the Google page ranking algorithm; operations research (inventory and supply-chain management); electrical circuits; control and finance; wireless communication.
- **Results:** Perron–Frobenius for positive matrices [S]; convergence of the power method and PageRank damping [D]; stationary distribution of an irreducible aperiodic chain [P in U5.8]; DFT matrix is unitary and diagonalizes circulants [P].
- **Build:** PageRank on a small web graph; matrix completion by alternating least squares and by nuclear-norm heuristic; OMP from scratch; CP decomposition by ALS.
- **Gap-fills:** *[inferred: Strang LfD]* low-rank matrix and tensor ideas that reappear in LoRA (U12.7) and compression (U16.4).

## D5. Probability and Stochastic Models

Aim: probability from events to limit theorems, the joint and multivariate machinery used by ML, and the stochastic models (Poisson process, Markov chains, queues, reliability) named in the sources. Benchmarks (recalled, not checked): Kay, *Intuitive Probability and Random Processes*; Rosenthal, *A First Look at Rigorous Probability Theory*; Deisenroth et al. Ch. 6; Blitzstein–Hwang, *Introduction to Probability*; Grimmett–Stirzaker.

### U5.1 Probability foundations: from events to Bayes' theorem
**Sources:** IPS W1–2, o; PSS W3, o; MFML W5, o; AEMA W9, o; EMML W10; SMLM W2; MLE W2; MLESA W0; S50 D2
- **Topics:** Sets, classes, collections; sequence of sets; ring and field (algebra) of sets; sigma-ring, sigma-field and monotone class; random experiment and events; definitions of probability; properties of the probability function I and II; conditional probability; independence of events; problems in probability I and II; probability concepts, conditional probability and Bayes' theorem; probability foundations from events to Bayes' theorem; basic concepts of probability; probability networks; review of probability, Bayes theorem; joint probability; marginal probability; law of total probability; independence of events; probability theory recap; probability theory as the core math backbone: critical for uncertainty modeling and ML intuition.
- **Results:** Continuity of probability along monotone sequences [P]; inclusion–exclusion for events [P]; law of total probability [P]; Bayes' theorem [P]; Borel–Cantelli lemmas [P]; π–λ / monotone class uniqueness theorem [S].
- **Build:** Bayes' rule on diagnostic-test and spam-filter examples; Monte Carlo verification of birthday and Monty-Hall problems.
- **Gap-fills:** *[inferred: Rosenthal; Kay]* measure-theoretic probability space (Ω, F, P), conditional independence, probabilistic graphical models as "probability networks" (links to U9.9).

### U5.2 Random variables, distributions and moments
**Sources:** IPS W2–3, o; MFML W6; PSS W4; SMLM W2; EMML W10–11; S50 D1, D3
- **Topics:** Random variables; probability distribution of a random variable I and II (PMF, PDF, CDF); moments; characteristics of distributions I and II; moments of random variables; expectation and variance; expected value; mean, median, mode, variance, standard deviation, range, interquartile range, skewness, kurtosis, percentiles and quantiles as distribution characteristics.
- **Results:** Properties of the CDF and its characterization [P]; linearity of expectation [P]; variance identity Var X = E[X²] − (E X)² [P]; Jensen's inequality [P]; moment generating function determines moments [S].
- **Build:** empirical CDF, histogram and moment estimators; skewness and kurtosis from scratch.
- **Gap-fills:** *[inferred: Kay; Rosenthal]* characteristic functions, expectation as Lebesgue integral, entropy and KL divergence (needed in D9, D13).

### U5.3 Special discrete distributions and the Poisson process
**Sources:** IPS W3–4; AEMA W9–10; PSS W4; EMML W11; SMLM W3; S50 D3
- **Topics:** Special discrete distributions I, II and III; discrete distributions (Bernoulli, binomial, negative binomial, Poisson, geometric, hypergeometric, multinomial); Poisson process I and II; discrete and continuous distribution functions; Poisson process and exponential distribution.
- **Results:** Poisson as the limit of binomial [P]; memorylessness of the geometric and exponential laws [P]; Poisson process: counts are Poisson and inter-arrivals exponential [D]; mean and variance of each standard law [D].
- **Build:** samplers for each discrete law from uniform random numbers; simulation of a Poisson process.
- **Gap-fills:** *[inferred: Kay]* Bernoulli trials and the multinomial as a model for categorical outputs (softmax in D11/D12).

### U5.4 Special continuous distributions and the normal distribution
**Sources:** IPS W4–5; AEMA W10–11; PSS W4; SMLM W3; EMML W11; S50 D3
- **Topics:** Special continuous distributions I–V; uniform, exponential, gamma, beta, normal and log-normal distributions; normal distribution and problems on normal distribution; problems on special distributions I and II; continuous probability distribution; Gamma and Beta families (link to U2.5); probability distributions for modeling uncertainty: used in generative models, likelihoods and simulations; normal (Gaussian) distribution.
- **Results:** Normal density integrates to one [P]; closure of the normal under affine maps and sums of independent normals [P]; exponential is the only memoryless continuous law [P]; relationship among Gamma, chi-square and exponential [P].
- **Build:** Box–Muller and inverse-CDF samplers from scratch; Q–Q plots against the standard normal.
- **Gap-fills:** *[inferred: Blitzstein–Hwang]* heavy tails, mixture distributions and the exponential family (needed for U9.9 and U6.5).

### U5.5 Functions of random variables, transformations and order statistics
**Sources:** IPS W6–7
- **Topics:** Function of a random variable I and II; additive properties of distributions I and II; transformation of random variables; distribution of order statistics.
- **Results:** Density of Y=g(X) by change of variables [D]; sum of independent variables by convolution [P]; joint law of order statistics [D]; Jacobian formula for multivariate transformations [S].
- **Build:** numerical check of transformed densities against histograms of simulated samples.

### U5.6 Joint distributions, conditioning, covariance and multivariate normal
**Sources:** IPS W6–7; MFML W7–8; AEMA W11, o; SMLM W4–5; EMML W11; MLCE W2; S50 D2, D6; AOW W1
- **Topics:** Joint distributions I and II; jointly distributed random variables; conditioning of random variables; marginal and conditional probability distributions; independence and product moments; linearity property of correlation and examples; bivariate normal distribution I and II; joint probability distribution (three parts); bivariate and multivariate probability distributions; introduction to copulas and applications; sample geometry; covariance matrices and properties; covariance and correlation matrix; joint probability and covariance; covariance, Pearson correlation, Spearman rank correlation, Kendall tau; correlation coefficient; modelling of joint distributions through copulas.
- **Results:** Law of iterated expectation and law of total variance [P]; covariance matrix is symmetric PSD [P]; conditional of a multivariate normal is normal with explicit mean and covariance [D]; Sklar's theorem [X]; correlation = 0 implies independence only for jointly normal [P].
- **Build:** multivariate normal sampler via Cholesky; conditioning formula verified by simulation; Gaussian copula sampler.
- **Gap-fills:** *[inferred: MML Ch.6; Johnson–Wichern]* Gaussian marginalization and conditioning, change of variables for densities, sample geometry (n-dimensional view of centred data).

### U5.7 Limit theorems and concentration inequalities
**Sources:** MFML W8; BAN W6; S50 D4
- **Topics:** Limit theorems; central limit theorem; a primer on concentration inequalities; sampling techniques.
- **Results:** Markov and Chebyshev inequalities [P]; weak law of large numbers [P]; strong law of large numbers [S]; central limit theorem (via characteristic functions) [P]; Hoeffding and Chernoff bounds [P]; sub-Gaussian tail bounds [P].
- **Build:** empirical convergence in the CLT for several source distributions; tail-bound tightness plots (used again in U10.3 for UCB).
- **Gap-fills:** *[inferred: Lattimore–Szepesvári Ch.5]* Cramér–Chernoff method, sub-Gaussian and sub-exponential variables, martingales and Azuma–Hoeffding.

### U5.8 Markov chains, queueing theory and reliability
**Sources:** HEM W11–12, o; AEMA W12, o; ALAJ W12; DOML W8
- **Topics:** Queuing system; distribution of arrivals and service times; analysis of M/M/1:FIFO and its application; analysis of M/M/S FIFO and its application; queueing theory and reliability theory; reliability, service time for a customer in a facility, life testing; discrete-time Markov chains.
- **Results:** Stationary distribution of M/M/1 [D]; Little's law [P]; Erlang-C formula for M/M/s [D]; existence and convergence of stationary distribution for finite irreducible aperiodic chains [P].
- **Build:** discrete-event simulator of M/M/1 and M/M/s queues compared with closed forms (reappears in U16.3 for LLM serving queues).
- **Gap-fills:** *[inferred: Kay Part II]* random processes, stationarity, Poisson and Gaussian processes; random walks (linking to U13 diffusion).

## D6. Statistics and Statistical Inference

Aim: from descriptive statistics to estimation theory, hypothesis testing, regression and Bayesian inference, including the learner's own "50 statistical techniques" list. Benchmarks (recalled, not checked): Casella–Berger, *Statistical Inference*; Miller–Freund, *Mathematical Statistics with Applications*; Johnson–Wichern, *Applied Multivariate Statistical Analysis* (6th ed.); Hastie–Tibshirani–Friedman, *The Elements of Statistical Learning*; Maity, *Statistical Methods in Hydrology and Hydroclimatology*.

### U6.1 Data, descriptive statistics and measures of association
**Sources:** PSS W1–2, o; IPS W8–9; SMLM W1, o; MLCE W1; S50 D1
- **Topics:** Different types of data; tables, charts, histograms, frequency distributions; measures of association; descriptive statistics I–IV; sample and population properties; introduction to probability and statistics; role of statistics, machine learning and data science; descriptive statistics for EDA and feature understanding; descriptive statistics as the data-understanding layer: foundation for EDA and feature understanding.
- **Results:** Sample mean minimizes squared deviation and median minimizes absolute deviation [P]; Chebyshev-type bounds for samples [P].
- **Build:** descriptive-statistics library from scratch (mean, median, mode, variance, SD, range, IQR, skewness, kurtosis, quantiles); box plots and histograms by hand.
- **Gap-fills:** *[inferred: Johnson–Wichern Ch.1]* outlier detection, standardization, graphical displays of multivariate data.

### U6.2 Sampling distributions and point estimation
**Sources:** IPS W8–10; S50 D4
- **Topics:** Basic concepts; chi-square distribution; t-distribution; F-distribution; introduction to estimation; unbiased and consistent estimators; LSE and MME (least squares and method of moments); examples on MME and MLE; examples on MLE I and II; MSE; UMVUE, sufficiency and completeness; Rao–Blackwell theorem and its applications; sampling techniques (random, stratified).
- **Results:** Distribution of the sample mean and variance for normal samples (Cochran/Student) [P]; MLE invariance and asymptotic normality [D / S]; Rao–Blackwell theorem [P]; Lehmann–Scheffé [S]; Cramér–Rao bound [P].
- **Build:** MLE by closed form and by numerical optimization (links to D8); bias–variance of estimators by simulation.
- **Gap-fills:** *[inferred: Casella–Berger]* Fisher information, factorization theorem for sufficiency, bootstrap.

### U6.3 Confidence intervals and hypothesis testing
**Sources:** IPS W10–12; AEMA W12, o; S50 D4, D5
- **Topics:** Confidence intervals I–IV; basic definitions of testing; two types of errors (Type I and II); power of a test; p-values; Neyman–Pearson fundamental lemma and its applications I and II; testing for normal mean; testing for normal variance; large-sample test for variance and two-sample problem; paired t-test; testing equality of proportions; testing of hypotheses I–III; hypothesis testing framework; t-test (one-sample, two-sample); z-test; chi-square test; ANOVA; Mann–Whitney U test; Wilcoxon signed-rank test; testing of hypotheses; applications to reliability, queueing and life testing; statistical inference as decision making: used in A/B testing, experiments and validation, general framework; hypothesis testing as core business use: used in product decisions and experimentation; analysis of variance (ANOVA).
- **Results:** Neyman–Pearson lemma [P]; duality of confidence intervals and tests [P]; distribution of the t statistic [P]; likelihood-ratio test and Wilks' theorem [S].
- **Build:** each test from scratch with exact p-values, checked against `scipy.stats`; power curves by simulation; A/B-test simulator.
- **Gap-fills:** *[inferred: S50]* multiple testing (Bonferroni, Benjamini–Hochberg), effect sizes.

### U6.4 Correlation, regression and multivariate analysis
**Sources:** AEMA W11–12; SMLM W6–7; MLCE W2; MLESA W2; S50 D6, D7; MFML W8
- **Topics:** Correlation and regression I and II; simple linear regression and multiple linear regression; coefficient of determination; confidence intervals and hypothesis testing for regression; linear regression, multiple linear regression, logistic regression, ridge regression, lasso regression, polynomial regression; multivariate analysis: principal component analysis, empirical orthogonal functions (EOF) and analysis of variance (ANOVA); subset selection; shrinkage methods; principal component regression; partial least squares; sample geometry and covariance matrices; correlation and relationships: used in feature selection and diagnostics; regression and predictive modeling as the core of ML plus explainability.
- **Results:** Gauss–Markov theorem [P]; distribution of OLS estimates under normal errors [D]; R² and adjusted R² [D]; ANOVA F-test decomposition [P].
- **Build:** OLS with standard errors and t-tests from scratch; ridge and lasso (coordinate descent) from scratch.
- **Gap-fills:** *[inferred: Johnson–Wichern]* factor analysis, canonical correlation, MANOVA, Hotelling's T².

### U6.5 Bayesian inference and MCMC
**Sources:** S50 D8, D9; MLESA W5; MLE W4,11; SMLM o
- **Topics:** Bayesian inference; prior and posterior distributions; MCMC (Markov chain Monte Carlo); MLE, MAP and Bayesian estimation; Monte Carlo methods; conjugate priors; Bayesian statistics as modern AI thinking: used in uncertainty-aware AI and LLMs; MCMC stands for Markov Chain Monte Carlo.
- **Results:** Posterior ∝ likelihood × prior [P]; conjugacy of Beta–Binomial and Normal–Normal [D]; correctness (detailed balance) of Metropolis–Hastings [P]; Gibbs sampler as a special case [P].
- **Build:** Metropolis–Hastings and Gibbs sampler from scratch; posterior of a coin bias and of a linear-regression coefficient.
- **Gap-fills:** *[inferred: Murphy PML Ch.3–4; Bishop]* credible intervals, posterior predictive, Hamiltonian Monte Carlo (statement), variational inference (link to D13 VAE).

### U6.6 Forecasting with statistical and machine-learning models: hydrology and water-resources applications
**Sources:** SMLM W1,12, o
- **Topics:** Forecasting using statistical and machine-learning algorithms with applications to hydrology and water-resources engineering; the role of statistics, machine learning and data science in hydroclimatology and water resources; determining the characteristics of observational data and events; data-driven solutions for engineering challenges; probabilistic solutions from joint and conditional distributions; suitability of data-driven models and assessing their performance; time-series forecasting (ARMA/ARIMA, regression, random forest, LSTM) and forecast-skill metrics.
- **Results:** Stationarity and the Box–Jenkins identification logic for ARMA models [D]; forecast error decomposition [D].
- **Build:** rolling-origin forecasting evaluation of ARMA versus random forest versus LSTM on a streamflow-like series.
- **Gap-fills:** *[inferred: Maity, Statistical Methods in Hydrology and Hydroclimatology; Forsyth, Applied Machine Learning]* extreme-value analysis and frequency analysis of hydrologic series, copula-based joint modelling (links to U5.6).

## D7. Differential Equations, Dynamical Systems, Numerical Methods, Complex Analysis and Transforms

Aim: the applied-analysis toolkit (ODEs, difference equations, numerics, complex variables, Laplace/Z/Fourier) that supports optimization-as-dynamics (D8), signal processing, diffusion models (D13) and FFT-based systems (D16). Benchmarks (recalled, not checked): Kreyszig, *Advanced Engineering Mathematics* (10th ed.); O'Neil; Jain–Iyengar; Churchill–Brown; Ahlfors; Conway; Debnath–Bhatta; Strogatz, *Nonlinear Dynamics and Chaos*; Murray, *Mathematical Biology*.

### U7.1 First- and higher-order ordinary differential equations
**Sources:** EM1 W11–12, o; AEMK W3; MM W3
- **Topics:** First-order differential equations; solution of first-order ODEs; integrating factor; exact forms; ODE order, degree, solution and geometrical significance; solution of first-order first-degree ODE by separation of variables, homogeneous equation and Bernoulli equation; second-order ODEs and auxiliary solutions; higher-order differential equations with constant coefficients; Cauchy–Euler equations.
- **Results:** Existence and uniqueness (Picard–Lindelöf) [S]; solution of linear constant-coefficient ODEs by characteristic equation [P]; superposition and Wronskian [P]; variation of parameters [D].
- **Build:** Euler, Heun and RK4 integrators from scratch with global-error order measured.
- **Gap-fills:** *[inferred: Kreyszig Ch.1–2]* method of undetermined coefficients, power-series solutions, systems of ODEs (feeds U7.6 and gradient flow in U8.10).

### U7.2 Numerical analysis: iteration, root finding, interpolation and quadrature
**Sources:** EM2 W5–6, o; AEMK W4–5
- **Topics:** Iterative methods for solution of systems of linear equations (Jacobi and Gauss–Seidel); solution of algebraic and transcendental equations (bisection, fixed-point iteration, Newton–Raphson); finite differences; interpolation; error in interpolation polynomials; Newton's forward and backward interpolation formulae; Lagrange's interpolation; numerical integration (trapezoidal, Simpson's 1/3rd and 3/8th rules).
- **Results:** Convergence of Jacobi/Gauss–Seidel for diagonally dominant matrices [P]; contraction mapping and fixed-point convergence [P]; interpolation error formula [D]; composite Simpson error [D].
- **Build:** all iterative solvers and interpolation formulae from scratch, checked against `scipy`.
- **Gap-fills:** *[inferred: Burden–Faires]* Runge's phenomenon, Chebyshev nodes, Gaussian quadrature.

### U7.3 Complex variables: analytic functions and complex integration
**Sources:** EM2 W3–4, o; AEMK W12; AEMA W1–3, o
- **Topics:** Function of complex variables and their properties including continuity and differentiability; analytic functions and Cauchy–Riemann equations; harmonic functions, harmonic conjugates and Milne's method; applications to the problems of potential flow I and II; line integrals in the complex plane; complex integration; Cauchy's theorem I and II; Cauchy's integral theorem and formula; Cauchy's integral formula for derivatives of an analytic function; derivatives of analytic functions; Morera's theorem; Liouville's theorem and the fundamental theorem of algebra; winding number and maximum modulus principle; limit, continuity, differentiability and analyticity of functions.
- **Results:** Cauchy–Riemann necessary and sufficient conditions [P]; Cauchy's theorem (Goursat) [S]; Cauchy integral formula and derivative formula [P]; Liouville and fundamental theorem of algebra [P]; maximum modulus [P].
- **Build:** numerical contour integration and verification of Cauchy's formula.

### U7.4 Series, singularities, residues, real integrals and conformal mapping
**Sources:** EM2 W4, o; AEMK W12; AEMA W3–7, o
- **Topics:** Sequences and series; uniform convergence of series; power series and radius of convergence (Hadamard's formula); Taylor's and Laurent's series; zeros and singularities of an analytic function; zeros and poles; meromorphic functions; residue at a singularity; residue theorem; the argument principle and Rouché's theorem; evaluation of real integrals using residues I–V; integration through a branch cut; evaluation of real integrals; bilinear transformations and cross ratio; conformal mapping I and II; conformal mappings from half-plane to disk and half-plane to half-plane; disk to disk and angular region to disk; application of conformal mapping to potential theory.
- **Results:** Laurent expansion existence and uniqueness [P]; residue theorem [P]; argument principle and Rouché [P]; Möbius transformations map circles to circles [P]; Riemann mapping theorem [X].
- **Build:** residue calculator for rational functions; conformal map visualizer.

### U7.5 Laplace, Z, Fourier and discrete Fourier transforms
**Sources:** EM2 W7–12, o; AEMA W7–9, o; ALAJ W8
- **Topics:** Laplace transform and its properties; Laplace transform of special functions; convolution theorem; evaluation of integrals by Laplace transform; solution of initial and boundary value problems; Fourier series representation of a function and its convergence; Fourier integral representation; Fourier sine and cosine transforms; Fourier transform and properties of the Fourier transform; applications of Fourier series to boundary value problems; review of unilateral and bilateral Z-transforms and their properties; application of calculus of residues for the inversion formula of Z-transforms and Laplace transforms; finite Fourier transforms; discrete Fourier transforms I and II and applications; Fourier integrals and Fourier transforms; structure of FFT/IFFT matrices; applications in signal processing, potential theory and bending of beams; Z-transforms I, II and III; review of bilateral Z-transforms.
- **Results:** Convolution theorem for Laplace and Fourier [P]; Dirichlet convergence theorem for Fourier series [S]; Parseval/Plancherel [P]; inversion formula for Z and Laplace transform by residues [D]; FFT divide-and-conquer recurrence [D].
- **Build:** FFT (radix-2) from scratch; spectral solution of a heat-equation boundary value problem.
- **Gap-fills:** *[inferred: Kreyszig]* Fourier transforms as a view of attention/positional encodings (link to U12.2) and of convolution (link to U11.5).

### U7.6 Mathematical modelling: discrete and continuous dynamical systems
**Sources:** MM W1–4, o; LAR W7
- **Topics:** Overview of mathematical modeling, types of mathematical models and methods to solve them; discrete-time linear models (Fibonacci rabbit model, cell-growth model, prey–predator model); analytical solution methods and stability analysis of systems of linear difference equations; graphical solution by cobweb diagrams; discrete-time age-structured (Leslie) model; Jury's stability test; numerical methods to find eigenvalues (power method and LR method); discrete-time non-linear models (different cell-division models, prey–predator model); stability of non-linear discrete-time models; logistic difference equation; bifurcation diagrams; introduction to continuous-time models, limitations and advantage of discrete-time models, need of continuous-time models; model for growth of microorganisms; chemostat; stability and linearization methods for systems of ODEs; continuous-time single-species model (Allee effect); qualitative solution of differential equations using phase diagrams; Lotka–Volterra competition and prey–predator models; mathematical modelling in biological sciences, deterministic discrete and continuous time, linear and non-linear population dynamics; major content chosen from dynamical systems (population dynamics); prey–predator (preypredator) models; graphical solution for clear analysis of the nature of the models.
- **Results:** Stability of a linear difference system by eigenvalue modulus [P]; Jury criterion [S]; period-doubling route to chaos in the logistic map (observed and explained) [S]; Hartman–Grobman linearization [X]; Lyapunov stability of a fixed point [P in U8.10].
- **Build:** cobweb and bifurcation diagram generators; Lotka–Volterra phase portraits; simulation of Leslie matrices.
- **Gap-fills:** *[source gap: the source lists only 4 of 12 course weeks; remaining weeks added from benchmarks]* *[inferred: Murray; Strogatz]* Hopf bifurcation, limit cycles, SIR epidemic models, reaction–diffusion models, parameter estimation for models (links to D9).

## D8. Optimization: Theory, Algorithms and Applications

Aim: eight dedicated source courses (primer, convex, LP, nonlinear programming, ML-oriented, software implementation, wireless/signal applications, distributed optimization) plus the optimization weeks of eight other courses, merged into one ladder: formulation and analysis, convex analysis, optimality and duality, linear programming, algorithms, then applications. Benchmarks (recalled, not checked unless noted): Boyd–Vandenberghe, *Convex Optimization* (Parts I and II confirmed from the published contents: convex sets, convex functions, convex optimization problems, duality; approximation and fitting, statistical estimation, geometric problems; the algorithms part on unconstrained and equality-constrained minimization and interior-point methods is recalled, not checked); Nocedal–Wright, *Numerical Optimization*; Bertsekas, *Nonlinear Programming*; Bazaraa–Sherali–Shetty; Chong–Zak; Dennis–Schnabel; Sun–Yuan; Rockafellar, *Convex Analysis*; Hiriart-Urruty–Lemaréchal; Chvátal and Dantzig–Thapa for LP; Tikhomirov, *Stories about Maxima and Minima*.

### U8.1 Optimization problems: formulation, history, transformations and basic facts
**Sources:** PMO W1, o; OAT W1–3, o; OFF W1–4, o; OMLH W3, o; MFML W10; MLE W3; EMML W8–10, o; CVX o; MLESA W0
- **Topics:** Introduction and history on the development of optimization theory; introduction to optimization; optimization overview of real analysis; optimization over open sets; optimization over surfaces; transformation of optimization problems; basic facts of maxima and minima and convex optimization; important classes of convex optimization problems; convex and non-convex optimization problems in machine learning; constrained and unconstrained optimization; numerical computation and optimization; introduction to optimization and its role as the workhorse of machine learning; introduction to Python for optimization; optimization algorithms (overview); introduction to optimization (Week 8 EMML); numerical optimization in machine learning; optimization using Python; convex optimization recap; mathematical optimization problem statement (variables, objective, constraints, feasible set, level sets); introduction to machine learning packages; Python basics for optimization; optimization using Python.
- **Results:** Fermat's necessary condition for interior extrema [P]; Weierstrass existence theorem [P in U8.4]; equivalent reformulations (epigraph form, slack variables, change of variables) preserve optimal values [P].
- **Build:** a small modelling layer in Python (objective, constraints, gradient check) used by all later optimization units.
- **Gap-fills:** *[inferred: Boyd Ch.1; Tikhomirov]* taxonomy of problem classes (LP, QP, QCQP, SOCP, SDP, GP, integer), local versus global minima, optimization over open sets and manifolds (Lagrange multipliers on surfaces).

### U8.2 Convex sets, cones, polyhedra and separation
**Sources:** PMO W3; CVX o, L1-9; AOW W2; EMML W8; LPCS W1–5, o; OFF W4; DOML W1
- **Topics:** Convex sets, examples of commonly occurring convex sets and convexity-preserving operations; separation result (a point and a closed convex set); hyperplanes and half-spaces; affine and linear combinations, cones and polyhedra; basics of convex optimization and basic properties of convex sets; introduction to polyhedral sets; separation theorems for convex sets; theorems of the alternative (Farkas' theorem, Gordan's theorem and other results); hyperplane separation theorems; Application: power constraints in wireless systems; convex sets and convex functions (week 1 DOML); structure behind convex optimization and why so many special cases can be solved efficiently; column space–row space duality; basic facts of convex optimization; mathematical optimization; motivation behind studying linear programming; basics of linear algebra for LP; algorithmic game theory, theoretical computer science and machine learning as application areas of LP; linear and affine combinations; this leads to the simplex algorithm; hyperplane separation theorems; Section III convex sets and convex functions.
- **Results:** Separating hyperplane theorem (point and closed convex set) [P]; supporting hyperplane theorem [P]; Farkas' lemma [P]; Gordan's theorem [P]; Carathéodory's theorem [P]; Minkowski/Krein–Milman for polytopes [S].
- **Build:** projection onto convex sets (ball, box, simplex, halfspace) from scratch; separating-hyperplane finder via QP.

### U8.3 Convex functions and their calculus
**Sources:** PMO W3–4; CVX L1-9, L10-19; AOW W3; EMML W8; DOML W1–2; OMLH W3; MLESA W0
- **Topics:** Convex functions and their continuity, Lipschitz continuity and directional derivative; zeroth-order and first-order characterizations of convexity; second-order characterization of convexity; convexity-preserving operations; properties of convex functions; convex/concave functions, examples and conditions for convexity; continuity and differentiability properties of convex functions; differentiable convex functions; non-differentiable convex functions; calculus of sub-differentials (subdifferential of a convex function); Fenchel conjugate; strong convexity and its implications; first- and second-order conditions for optimization; application: beamforming in wireless systems, multi-user wireless, cognitive radio systems.
- **Results:** Jensen's inequality [P]; first-order condition f(y) ≥ f(x)+∇f(x)ᵀ(y−x) [P]; Hessian PSD ⇔ convex [P]; convex functions are locally Lipschitz in the interior [P]; subdifferential is nonempty, convex and compact in the interior [P]; Fenchel–Moreau (statement) [X]; strong convexity ⇒ unique minimizer and quadratic growth [P].
- **Build:** numerical convexity tester via random Hessian sampling; subgradient computation for ℓ1, hinge and max functions.

### U8.4 Unconstrained optimization theory
**Sources:** PMO W4–5; OMLH W3; OFF W2–3; CVX L20-26
- **Topics:** Local optima and its variants; saddle point; coercive functions; existence of optima (Weierstrass theorem; theorem for coercive functions); descent direction and its first-order and second-order characterizations; direction of descent; first-order and second-order necessary and sufficient conditions for minima; first- and second-order conditions for optimisation; optimization over open sets.
- **Results:** First-order necessary condition [P]; second-order necessary and sufficient conditions [P]; for convex f, stationary ⇒ global minimum [P]; coercive continuous functions attain their minimum [P].
- **Build:** classify the stationary points of Rosenbrock, Himmelblau and a saddle function by Hessian eigenvalues.

### U8.5 Constrained optimization theory: Lagrange, cones, Fritz John and KKT
**Sources:** PMO W8–9; CVX L10-19, o; DOML W2–3; AOW W6; EMML W12; MFML W10
- **Topics:** Revisit of the Lagrange multipliers method; cones for constrained optimization (cone, dual cone, cone of feasible directions, linearizing cone, cone of descent directions, tangent cone); geometric optimality conditions; first-order Fritz John (FJ) and KKT necessary optimality conditions; first-order KKT sufficient optimality condition; second-order KKT necessary and sufficient conditions; constraint qualification; Rockafellar–Pshenichny optimality condition; properties of normals and projections; projection on a convex set and normal cone; computing the normal cone of inequality constraints; tangent cone; minimization of a convex function with convex inequality constraints; constrained optimization problems (primal and Lagrangian dual); KKT conditions and primal/dual methods; Lagrangian multiplier method; Karush–Kuhn–Tucker conditions (CVX outline); saddle-point conditions; Karush–Kuhn–Tucker conditions; projection on a convex set and normal cone; sub-differential of a convex function (subdifferential); Section VI constraint optimization theory.
- **Results:** Lagrange multiplier theorem [P under regularity]; Fritz John conditions [P]; KKT necessary conditions under LICQ/MFCQ [P]; KKT sufficient for convex problems [P]; Slater's condition [P in U8.6].
- **Build:** KKT-system solver for small QPs; verification of KKT residuals on solutions from `scipy.optimize`.

### U8.6 Lagrangian duality, saddle points and minimax
**Sources:** PMO W10; CVX o, L10-19; DOML W2–3,7; AOW W6; EMML W12; LPCS W4–6; OFF W6–7
- **Topics:** Lagrangian duality (how one discovers duality; geometric interpretation of duality); results on the dual function (the dual problem is a convex optimization problem; differentiability of the dual function); weak duality theorem and duality gap; equal primal and dual objective values imply optimality; strong duality theorem (convex problem and Slater's constraint qualification imply strong duality); saddle-point optimality and absence of duality gap; relationship between saddle-point criteria and KKT conditions; duality in connection with linear programming; strong duality for convex problems and consequences; Lagrangian duality and examples; duality principle and KKT framework for optimization; concepts of duality, hard and soft margin classifier (SVM dual); duality theory and strong duality (LP); Von Neumann's minimax theorem as an application of strong duality; existence of Nash equilibria; Yao's technique for lower bounds in communication complexity; the relation between primal and dual used to prove the max-flow min-cut theorem; primal–dual methods and an algorithm for max flow; dual ascent and dual decomposition; application: water-filling power allocation; duality theory, one of the main reasons LP has so many applications; Nash equilibria (John Nash); primal–dual methods; an algorithm for the max-flow problem; Section VII Lagrangian duality theory.
- **Results:** Weak duality [P]; strong duality under Slater [P]; LP strong duality [P]; complementary slackness [P]; Von Neumann minimax theorem [P]; Nash existence for finite two-player zero-sum games [P]; max-flow = min-cut [P].
- **Build:** dual of an LP and of an SVM computed and checked numerically; zero-sum game solved by LP.

### U8.7 Linear programming: simplex, duality, sensitivity and interior-point methods
**Sources:** CVX L10-19, L20-26, L27-33, o; HEM W9–10, o; LPCS W1–3,7–8, o; OFF W5–7; OAT W9–11; AOW W4; EMML W11; MFML W10
- **Topics:** Pleasures of linear programming; direction of descent; extreme points of linear programming; polyhedral sets and cones; foundation of simplex methods; fundamental theorem of linear programming; simplex methods (and continued); simplex method; two-phase method II; dual simplex method and its application; sensitivity analysis I; graphical method I and II; introduction to linear programming; Gaussian elimination, rank–nullity, basics of LP and its definition; linear programming basics and examples; basic results and the fundamental theorems of linear programming; introduction to interior-point methods; log barrier function; primal–dual framework; overview of interior-point algorithm; short-step algorithm and short-step path-following method; predictor–corrector method; affine scaling method; Karmarkar's algorithm; LP with integer constraints and relaxation (ILP, rounding, approximation algorithm for set cover); applications of LP in machine learning (linear regression and classification by LP tools, Boolean functions); error-minimizing LPP; Linear programming problems (HEM main topic 3); linear program application: power allocation in multi-cell cooperative OFDM; introduction to linear programming and duality; short-step path-following method; modelling a quantity as an integer linear program (ILP) and the concept of relaxation of a linear program; linear regression and classification approached with LP tools; Section VIII linearly constrained nonlinear optimization algorithms.
- **Results:** Fundamental theorem of LP (optimum at a vertex) [P]; simplex terminates under Bland's rule [P]; strong duality and complementary slackness [P]; polynomial-time convergence of short-step path-following [S]; integrality gap of LP relaxation of set cover and rounding bound [P]; ℓ1 and ℓ∞ regression as LPs [D].
- **Build:** tableau simplex (two-phase and dual) from scratch; log-barrier interior-point method from scratch; compare with `scipy.optimize.linprog`.
- **Gap-fills:** *[inferred: Chvátal; Dantzig–Thapa]* degeneracy and cycling, network simplex, transportation and assignment problems, total unimodularity.

### U8.8 Unconstrained descent methods: line search, gradient, Newton, quasi-Newton, conjugate gradient, trust region
**Sources:** PMO W5–8; OAT W3–6; OMLH W4,7–8; OFF W10–11; EMML W9–10; MFML W10; FML W4; DOML W3
- **Topics:** General structure of an optimization algorithm, global convergence, descent property, quadratic termination property; introduction to line search (exact and inexact); inexact line searches (Armijo–Goldstein, Wolfe–Powell, Armijo backtracking); global convergence of gradient descent methods using exact and inexact line searches; where general descent methods converge (almost always to a local minimizer; capture theorem); scaling of variables; practical stopping criteria; steepest descent method, descent property, zigzagging, scaling effect, Barzilai–Borwein gradient method; global convergence of steepest descent and its order of convergence, scaling effect and dimension independence; Newton method and its local convergence; dimension dependency of Newton method and scaling effect; Levenberg–Marquardt and other modified Newton methods; quasi-Newton methods (quasi-Newton equation, general quasi-Newton algorithm, variable metric method, comparison of Newton and quasi-Newton methods); global convergence of quasi-Newton methods for uniformly convex functions; superlinear convergence of quasi-Newton methods; basic conjugate direction method and its convergence rate (basic CG method); gradient descent/conjugate gradient algorithm; Newton's method; quasi-Newton methods; trust region methods (Cauchy point, dogleg and double dogleg methods); gradient descent: math and programming of basic optimization problems and their solutions; Newton's method and optimization for ML in practice with PyTorch/TensorFlow; gradient descent and other optimization algorithms in machine learning; gradient descent primal and dual view and convergence for linear and logistic regression; Barzilai and Borwein (Borwin) gradient method; dog leg and double dog leg methods; Section V unconstrained optimization methods; continued lectures on Newton and quasi-Newton methods.
- **Results:** Convergence of gradient descent for L-smooth convex functions at rate O(1/k) and for strongly convex at linear rate [P]; Zoutendijk condition [P]; local quadratic convergence of Newton [P]; superlinear convergence of BFGS [S]; CG finds the minimizer of an n-dimensional quadratic in ≤ n steps [P]; Armijo backtracking terminates [P].
- **Build:** GD with backtracking, Newton, BFGS/L-BFGS, CG and dogleg trust region from scratch; iteration-count and condition-number experiments on quadratics and Rosenbrock; compare with `scipy.optimize.minimize`.
- **Gap-fills:** *[inferred: Nocedal–Wright Ch.3–7; Dennis–Schnabel]* Wolfe-condition line-search algorithms, limited-memory BFGS, nonlinear least squares (Gauss–Newton), derivative-free methods.

### U8.9 Constrained optimization algorithms: QP, projected and reduced gradient, penalty, augmented Lagrangian, SQP
**Sources:** PMO W11–12; OAT W7–8; OFF W10–11; DOML W6; OMLH W5–6
- **Topics:** Quadratic programming methods (active-set method; interior-point method); projected gradient algorithm; reduced gradient algorithm; penalty methods (exterior penalty method; interior penalty method); quadratic penalty method; augmented Lagrangian method and method of multipliers; sequential quadratic programming (Lagrange–Newton method; reduced Hessian matrix method); trust region method; null space method; linearly constrained and nonlinearly constrained nonlinear optimization algorithms; projected gradient descent; Section IX nonlinearly constrained nonlinear optimization algorithms; continued lectures on variants of gradient descent and neural-network training theory; Section VIII: linearly constrained nonlinear optimization algorithms.
- **Results:** Exterior penalty solutions converge to a constrained minimizer as the penalty grows [P]; augmented Lagrangian avoids ill-conditioning and converges with bounded penalty [S]; SQP as Newton on the KKT system [D]; active-set termination for convex QP [S].
- **Build:** quadratic-penalty and augmented-Lagrangian solvers from scratch on a small equality-constrained problem; projected gradient onto the simplex.
- **Gap-fills:** *[inferred: Nocedal–Wright Ch.16–18; Bertsekas]* filter methods and merit functions, barrier methods (link to U8.7 IPM).

### U8.10 First-order methods for ML: stochastic, accelerated, proximal, adaptive, and the dynamical-systems view
**Sources:** OMLH W5–8; DOML W3–6; FML W4–5; MLCE W5; FDL W2; OAT W12; MFML W10; MLESA W5
- **Topics:** Variants of gradient descent (projected, stochastic, proximal, accelerated, coordinate descent) and training a neural network (theory and implementation); analysis of gradient descent; analysis of accelerated optimization algorithms; optimization algorithms as dynamical systems and introduction to stability theory; Lyapunov analysis of gradient flows; gradient flows for equality-constrained optimization and saddle-point problems; accelerated gradient flows; SGD and its analysis for linear and logistic regression, SGD versus GD as a learning algorithm, model selection; training of ML models; gradient descent algorithm; stochastic gradient descent; momentum-based GD, Nesterov accelerated GD, AdaDelta, AdaGrad, RMSProp, Adam; variants such as momentum, AdaGrad, Adam and RMSprop; gradient descent and stochastic gradient descent (MFML); an application from machine learning (OAT Week 12); initialization, training and validation; along with implementation and optimization in real-world applications.
- **Results:** SGD convergence for convex and strongly convex objectives with variance bound [P]; Nesterov's O(1/k²) rate and its optimality [S]; Lyapunov function for gradient flow gives exponential convergence for strongly convex f [P]; proximal gradient converges at O(1/k) [P]; Adam update as adaptive preconditioning (no general convergence guarantee, counterexample) [S].
- **Build:** SGD, momentum, Nesterov, AdaGrad, RMSProp and Adam from scratch in NumPy on least squares and logistic regression; ODE-view simulation of gradient flow versus discrete GD.
- **Gap-fills:** *[inferred: Bach LTFP Ch.5; Goodfellow Ch.8]* learning-rate schedules, mini-batching and variance reduction (SVRG), second-order and natural-gradient ideas.

### U8.11 Conic and structured convex programs: QCQP, SOCP, SDP, geometric programs
**Sources:** AOW W4–6,9, o; CVX o, L34-40; MLESA W0
- **Topics:** Convex optimization problems; linear programs; QCQP and SOCP problems; application: channel shortening for wireless equalization and robust beamforming in wireless systems; semi-definite programming (SDP); saddle-point type conditions for SDP; approximate solutions; geometric programs and optimal power allocation for cooperative communication; optimization for MIMO systems, OFDM systems and MIMO-OFDM systems; cognitive radio and cooperative communication.
- **Results:** Every LP, QP, QCQP and SOCP is an SDP-representable convex program [P]; Schur-complement representation of quadratic constraints [P]; GP becomes convex under log transformation [P]; SDP strong duality under strict feasibility [S].
- **Build:** the same problems solved with from-scratch IPM and with `cvxpy`, with solver comparison.

### U8.12 Applications of optimization: signal estimation, compressive sensing, radar, big data and finance
**Sources:** AOW W2–12, o; EMML o; MLCE W4
- **Topics:** Optimization for signal estimation (LS, WLS, regularization); wireless channel estimation; image reconstruction and deblurring; convex optimization for machine learning (PCA and SVM); compressive sensing and sparse signal processing; OMP (orthogonal matching pursuit); LASSO (least absolute shrinkage and selection operator) for signal estimation; radar for target detection, array processing, MUSIC and MIMO-radar schemes for enhanced target detection; convex optimization for big-data analytics, recommender systems, user-rating prediction and latent-factor methods; optimization for finance (financial models and portfolio optimization); water-filling power allocation; loss functions as optimization objectives (MSE, MAE, MSLE, cross-entropy, Tweedie, MAPE) and their statistical basis; Principal Component Analysis (PCA); Support Vector Machines (SVM); LASSO techniques; wireless communication, signal processing, machine learning, big data and finance as application fields.
- **Results:** LASSO yields sparse solutions (subgradient optimality) [D]; restricted-isometry sufficient condition for exact recovery (statement) [X]; water-filling is the KKT solution of capacity maximization [D]; Markowitz mean–variance solution [D].
- **Build:** ISTA and coordinate-descent LASSO; OMP recovery experiments (phase transition); water-filling solver.

### U8.13 Non-smooth and difference-of-convex optimization
**Sources:** CVX o, L34-40
- **Topics:** Descent direction for non-smooth functions; minimization of difference-convex (DC) functions (and continued); approximate solutions; concluding lecture (overview of convex optimization).
- **Results:** Optimality 0 ∈ ∂f(x) [P]; subgradient method convergence rate [P]; DC algorithm (DCA) monotone descent [P].
- **Build:** subgradient method for hinge-loss SVM; DCA for a sparse regression with a non-convex penalty.

### U8.14 Distributed optimization: graphs, consensus, ADMM and dual decomposition
**Sources:** DOML W1,7–10, o; MFML o
- **Topics:** Introduction to distributed optimization; ADMM (alternating direction method of multipliers); dual ascent and dual decomposition; introduction to graph theory; distributed consensus; continuous-time analysis of consensus algorithms; distributed optimization problem (economic dispatch problem); distributed optimization algorithms; centralized versus distributed or decentralized algorithms under communication overhead, network topology, computational resources and robustness; graph theory, iterative methods for convex problems, synchronous and asynchronous setups, consensus algorithms; recent literature that exploits control theory for accelerated distributed optimization algorithms; graph theory, iterative methods for convex problems; distributed machine learning; synchronous and asynchronous setups.
- **Results:** ADMM convergence for convex problems [S]; consensus convergence rate governed by the second-smallest Laplacian eigenvalue [P]; dual decomposition for separable problems [D]; distributed gradient descent converges to a neighbourhood with constant steps [S].
- **Build:** ADMM for LASSO and consensus averaging over a graph from scratch (reuses U1.4 and U4.8).
- **Gap-fills:** *[inferred: Nedić, Distributed Optimization Over Networks; Boyd et al., ADMM monograph]* push-sum and directed graphs, gradient tracking, asynchronous updates.

### U8.15 Dynamic optimization and complementarity problems
**Sources:** OFF W8–9,12, o
- **Topics:** Nonlinear and convex optimization (Weeks 8–9); complementarity problems and algorithms for the same; dynamic optimization; real analysis and convexity as the base for LP, convex optimization and nonlinear programming.
- **Results:** Bellman's principle of optimality [P]; finite-horizon dynamic programming recursion [P]; KKT conditions as a complementarity problem [D].
- **Build:** value-iteration and backward-induction solver for a finite-horizon problem (feeds U10.4 MDPs).
- **Gap-fills:** *[inferred: Bertsekas, Dynamic Programming and Optimal Control]* linear–quadratic regulator, Pontryagin principle (statement), calculus of variations.


# PART B. MACHINE LEARNING

## D9. Machine Learning Foundations: Supervised, Unsupervised, Probabilistic, Data Mining and Learning Theory

Aim: nine dedicated source courses (engineering ML, IIT ML courses, KTH symbolic ML, data mining, statistical ML) merged into one classical-ML ladder, each algorithm built from scratch in NumPy first, then compared with scikit-learn. Benchmarks (recalled, not checked unless noted): Bishop, *Pattern Recognition and Machine Learning*; Hastie–Tibshirani–Friedman, *The Elements of Statistical Learning*; Murphy, *Probabilistic Machine Learning: An Introduction* (book site confirmed: a long contents PDF exists, not retrievable as text); Bach, *Learning Theory from First Principles* (chapters confirmed: mathematical preliminaries, supervised learning, least-squares regression, empirical risk minimization, optimization, local averaging, kernel methods, sparse methods, neural networks, ensemble learning, online learning to bandits, overparameterized models, structured prediction, probabilistic methods, lower bounds); Mitchell, *Machine Learning*; Alpaydin; Duda–Hart–Stork; Rengaswamy–Suresh, *Data Science for Engineers*; Deisenroth et al. Part II (when models meet data, linear regression, PCA, GMM, SVM).

### U9.0 History of AI, symbolic AI and the machine-learning workflow
**Sources:** GEN 2.1, 2.2, 2.3, 2.4, 2.5, 2.6
- **Topics:** History of AI: the birth of AI (the 1956 Dartmouth Conference), major milestones, the Turing Test, what is artificial intelligence; the symbolic AI era: representing knowledge (logic, rule-based inference, semantic nets), expert systems, hitting the wall (the AI winter); machine learning and data: data as the fuel of machine learning, the journey of AI; supervised learning: core paradigms, workflow (train/test split, training, testing), tutorial with scikit-learn (with NumPy and Matplotlib), evaluation metrics (confusion matrix; accuracy, precision, recall, F1); unsupervised learning: core paradigms, why compress high-dimensional data, workflow (training), challenges and limitations; feature learning through embeddings: one-hot vectors and classification with them, limitations of sparse representations and why sparsity breaks similarity, distributional semantics (words by context), dense (distributed) representations and embeddings.
- **Results:** Confusion-matrix identities for accuracy, precision, recall and F1 [D]; sparsity of one-hot vectors makes all distinct words orthogonal [P].
- **Build:** a rule-based expert-system toy, then the scikit-learn supervised and unsupervised workflows end to end, with each metric recomputed by hand from the confusion matrix.

### U9.1 What machine learning is: paradigms, data, hypothesis spaces and the statistical framework
**Sources:** MLCE W1, o; MLDL W1, o; MLK W1–3, o; MLE W1–3, o; MLESA W1, o; FML W1, o; IMLK W1, o; SMLM W8–9; MFML W12; DMIN W1, o
- **Topics:** Introduction to data science and machine learning; differences between supervised, unsupervised and reinforcement learning with examples from engineering disciplines; introduction to ML and performance measures; basic definitions, types of learning, hypothesis space and inductive bias; machine learning in its context within AI; the introduction to the machine-learning course; characterization of learning problems; forms of representation; statistical decision theory for regression and classification; overview of ML; stochastic framework for supervised learning; risk minimization; Bayes optimal predictor; stochastic optimization; empirical risk minimization (ERM); statistical learning: introduction, supervised and unsupervised learning problems, loss functions; introduction to artificial intelligence and neural networks (SMLM Week 9); algorithms for ML – classification, clustering and regression; intro to machine learning packages; broad heuristics governing basic ML algorithms in engineering applications; limits and applicability of ML algorithms; mathematical basics (linear algebra and probability recap); computational basics; basics of Python; scientific-computing packages NumPy, SciPy, Matplotlib; simple ML packages (scikit-learn, PyTorch); Bayesian classification; multilayer perceptron; autoencoders; convolutional and recurrent neural networks and attention mechanisms; decision trees and ensemble methods, boosting and bagging, random forests, support vector machines, Gaussian process regression; logistic regression, k-nearest neighbour, basic clustering algorithms, feature reduction methods; hypothesis space; evaluation strategies and cross-validation; adaptive systems; reinforcement learning and deep learning through decision trees; optimization (SGD) and energy-based models with Langevin sampling as foundations of generative models; Classical Techniques 1 and 2 and Advanced Techniques 1 and 2 (course blocks).
- **Results:** Bayes optimal classifier minimizes 0–1 risk [P]; Bayes optimal regressor is the conditional mean under squared loss [P]; ERM decomposition into estimation and approximation error [D]; no-free-lunch theorem [S].
- **Build:** a minimal ML framework in NumPy (dataset split, fit/predict API, metrics) used by all later units.
- **Gap-fills:** *[inferred: Mitchell Ch.1–2; Bach Ch.2; Murphy]* concept learning, version spaces, the formal learning problem (inputs, targets, loss, risk), data cleaning and feature scaling.

### U9.2 Model evaluation and selection: bias–variance, validation, tuning and metrics
**Sources:** MLCE W3,6, o; MLDL W1; MLESA W1,7; MLE W4; IMLK W1; EMML W6; DMIN W7; SMLM W8
- **Topics:** Overfitting and underfitting; bias–variance tradeoff; performance measures; k-fold cross-validation and leave-one-out cross-validation; hyperparameter tuning via grid search, randomized search and Bayesian approaches; bootstrapping and cross-validation; classification evaluation measures; ROC curve; MDL (minimum description length); classification metrics; evaluation and visualization (data mining); evaluation strategies and cross-validation; confidence intervals and goodness of fit; train/validation/test discipline; implementation of regression models in Python.
- **Results:** Bias–variance decomposition of expected squared error [D]; leave-one-out cross-validation estimator formula for linear smoothers [D]; AUC equals the probability that a positive outranks a negative [P].
- **Build:** cross-validation, ROC/AUC, confusion-matrix metrics (accuracy, precision, recall, F1) and grid/random search from scratch.
- **Gap-fills:** *[inferred: ESL Ch.7]* optimism and AIC/BIC, nested cross-validation, calibration, statistical comparison of classifiers.

### U9.3 Linear regression and linear classification: estimation, logistic and softmax regression, surrogate losses
**Sources:** MLCE W2–4, o; MLDL W1,5; MLESA W2–3; MLE W4; FML W2–3; IMLK W2,5; SMLM W6; EMML W5; S50 D7
- **Topics:** Linear regression, model parametrization and fitting; coefficient of determination; linear regression estimation error and model error; linear modelling; multivariate regression; subset selection; shrinkage methods; principal component regression; partial least squares; linear classification and surrogate losses; logistic regression; softmax regression; bounding estimation error in binary classification; loss functions (mean-squared error, mean absolute error, mean-squared logarithmic error, cross-entropy loss, Tweedie loss, mean absolute percentage error) and the statistical basis of some loss functions; MLE and MAP interpretation; linear discriminant analysis; Bayesian regression; nonlinear regression; Basics of Python; dealing with overfitting via regularization (ridge regression and LASSO); decision trees and overfitting.
- **Results:** OLS = MLE under Gaussian noise [D]; logistic regression log-likelihood is concave, gradient and Hessian [D]; softmax cross-entropy gradient is (p−y) [D]; estimation error bound for linear least squares [P]; surrogate-loss consistency (hinge, logistic) [S].
- **Build:** linear, logistic and softmax regression with gradient descent and Newton/IRLS from scratch; compare with scikit-learn.
- **Gap-fills:** *[inferred: Bishop Ch.3–4; ESL Ch.3–4]* generalized linear models, Poisson regression, perceptron convergence (see U9.5).

### U9.4 Regularization and implicit regularization
**Sources:** MLCE W3; MLDL W1; MLE W4; FML W6; MLESA W2; ALAK W7
- **Topics:** Regularization (ridge regression and LASSO); min-norm regularization for linear regression and classification; equivalent forms of regularization (penalized, constrained, early stopping); implicit regularization; L1 versus L2 (geometry and sparsity); variants of gradient descent; regularization and shrinkage; sparsity.
- **Results:** Ridge shrinkage in the SVD basis [D]; lasso soft-thresholding solution for orthonormal design [D]; gradient descent from zero converges to the min-norm interpolant for under-determined least squares [P]; constrained and penalized forms are equivalent (Lagrangian) [P].
- **Build:** ridge path, lasso path and elastic net by coordinate descent from scratch.

### U9.5 Perceptron, support vector machines and kernel methods
**Sources:** MLDL W4; MLESA W4; FML W7–8; IMLK W5; MLCE W9–10; DMIN W4; MFML W4; EMML W11–12; MLE W9; ALAJ W5,11; SMLM W11
- **Topics:** Perceptron criteria; discriminative models; support vector machines (SVM) for classification and regression; perceptron; kernel function and kernel SVM; kernel machines; linear models in infinite-dimensional spaces; kernels (linear, polynomial, Gaussian); the kernel trick; the representer theorem; universal kernels; Bayes consistency and generalization rate with universal kernel machines; hard and soft margin classifier; SVM in Python; introduction to SVM and error-minimizing LPP; Support Vector Machines and applications (MFML Week 4); SVM and kernel machine (data mining); linear perceptron and training a perceptron by stochastic gradient; SVM and kernel SVM; kernel machines; deep neural networks, SVM and K-means clustering as covered in the statistical-methods course.
- **Results:** Perceptron convergence theorem (mistake bound) [P]; SVM primal–dual derivation and support vectors [D]; representer theorem [P]; Mercer's theorem [X]; universal kernel ⇒ Bayes consistency (statement and sketch) [S].
- **Build:** perceptron, SVM via SMO and via QP (cvx), kernel ridge regression and kernel SVM from scratch; compare with `sklearn.svm`.
- **Gap-fills:** *[inferred: Bishop Ch.6–7; Bach Ch.7]* support-vector regression, multi-class SVM, reproducing-kernel Hilbert spaces.

### U9.6 Bayes decision theory, density estimation and probabilistic classifiers
**Sources:** MLDL W2–3; MLESA W3,5,8; MLE W9; IMLK W4; DMIN W3; MLK W4; FML W12
- **Topics:** Bayes decision theory; normal density and discriminant function; Bayes decision theory for binary features; Bayesian belief network; parametric and non-parametric density estimation (ML and Bayesian estimation); Parzen window and KNN; probability and Bayes learning; naive Bayes; Bayes classifier; K-nearest neighbour; linear discriminant analysis; parameter estimation (MLE, MAP, Bayesian estimation); multi-class classification; k-NNs; kNN (Classical Techniques 2); applications.
- **Results:** Discriminant functions of Gaussian class-conditionals are quadratic (linear for shared covariance) [D]; naive Bayes factorization and Laplace smoothing [D]; kNN asymptotic error ≤ 2× Bayes error (Cover–Hart) [S]; Parzen estimator bias–variance [D].
- **Build:** Gaussian discriminant analysis, naive Bayes, Parzen and kNN from scratch.

### U9.7 Decision trees and ensembles: bagging, boosting, random forests
**Sources:** MLCE W8–10; MLDL W5–6; MLESA W6–8; MLE W9; IMLK W2,7; SMLM W10; DMIN W3; FML W12; MLK W4
- **Topics:** Decision trees and their working; recursive binary splitting; regression and classification via decision trees; regression trees; stopping criterion and pruning loss functions; categorical attributes; multiway splits; missing values; decision-tree instability and evaluation measures; ensembling of decision trees; ensemble methods (ensemble strategies, bagging, committee machines and stacking, boosting); random forests; adaptive boosting (AdaBoost); gradient boosting; gradient-boosted machine learning; decision-tree-based inductive learning; model averaging; regularization for boosted trees; binary trees; implementation of decision trees, SVM and GPR in Python; Classical Techniques 1 (course block).
- **Results:** Information gain and Gini impurity as concave impurity measures [D]; bagging variance reduction for correlated estimators [D]; AdaBoost training-error bound [P]; gradient boosting as functional gradient descent [D].
- **Build:** CART, random forest, AdaBoost and gradient boosting from scratch; compare with scikit-learn and XGBoost-style implementations.
- **Gap-fills:** *[inferred: ESL Ch.9–10, 15–16]* out-of-bag error, variable importance, shrinkage and subsampling.

### U9.8 Dimensionality reduction and feature learning
**Sources:** MLCE W7–8; MLDL W7; IMLK W3; EMML W3–4; MFML W4,10; MLESA W2; SMLM W7; DMIN W1; MLE o
- **Topics:** Unsupervised learning; why compress high-dimensional data; singular value decomposition; principal component analysis (PCA); Python implementation of PCA; linear discriminant analysis (LDA) and its Python implementation; the dimensionality problem; feature reduction; nonlinear dimensionality reduction via uniform manifold approximation and projection (UMAP), t-distributed stochastic neighbour embedding (t-SNE) and autoencoders; implementation of unsupervised learning in Python; PCA and least squares; principal component regression; multicollinearity; empirical orthogonal functions.
- **Results:** PCA as top-k eigenvectors of the covariance matrix (variance maximization) [P]; PCA equals best rank-k reconstruction (Eckart–Young) [P in U4.9]; Fisher's criterion for LDA [D]; t-SNE gradient [D]; linear autoencoder spans the PCA subspace [P].
- **Build:** PCA via covariance eigendecomposition and via SVD, LDA, kernel PCA and a t-SNE sketch from scratch; compare with scikit-learn.
- **Gap-fills:** *[inferred: MML Ch.10; ESL Ch.14]* probabilistic PCA, independent component analysis, spectral embedding.

### U9.9 Clustering, mixture models and the EM algorithm
**Sources:** MLCE W7–8; MLDL W8–9; MLESA W10–11; MLE W10; IMLK W8; DMIN W5; ALAJ W10; SMLM W11
- **Topics:** Clustering algorithms including k-means and density-based clustering; concept of mixture model; Gaussian mixture model (GMM); expectation–maximization (EM) algorithm; K-means clustering; fuzzy K-means clustering; hierarchical agglomerative clustering (adaptive hierarchical clustering); mean-shift clustering; partitional clustering; BIRCH algorithm; CURE algorithm; density-based clustering; outlier detection; centroid-based and probabilistic model-based clustering; k-means clustering (statistical-methods course Week 11); kNN and applications (Classical Techniques 2); Classical Techniques 2 (course block).
- **Results:** k-means monotonically decreases its objective and converges to a local minimum [P]; EM never decreases the likelihood [P]; k-means as the hard-assignment limit of spherical GMM [D]; Jensen-based ELBO derivation of EM [D].
- **Build:** k-means++, GMM-EM, DBSCAN, agglomerative linkage and mean-shift from scratch.
- **Gap-fills:** *[inferred: MML Ch.11; Bishop Ch.9]* choosing k (silhouette, BIC), spectral clustering (uses U4.8 and U1.4).

### U9.10 Probabilistic graphical models, hidden Markov models, inference and Gaussian processes
**Sources:** MLESA W5,8–9; MLDL W2,5; MLE W11; MLCE W10; FML W11–12
- **Topics:** Bayesian networks; undirected graphical models; hidden Markov models (HMM); variable elimination; belief propagation; structured probabilistic models; Monte Carlo methods; Gaussian process regression (GPR) and its implementation in Python; probabilistic models for supervised learning; likelihood estimation; Bayesian belief network; Advanced Techniques 1 (structured probabilistic models and Monte Carlo methods).
- **Results:** d-separation and the factorization theorem [S]; forward–backward and Viterbi algorithms [D]; belief propagation is exact on trees [P]; GP posterior mean and variance [D].
- **Build:** HMM (forward, Viterbi, Baum–Welch), variable elimination on a small Bayesian network and GP regression from scratch.
- **Gap-fills:** *[inferred: Bishop Ch.8, 11, 13; Murphy; Goodfellow Ch.16–19]* sampling methods, approximate inference, partition-function problem (links to U13.6).

### U9.11 Instance-based learning, collaborative filtering and recommendation
**Sources:** IMLK W3; DMIN W3; ALAJ W7
- **Topics:** Instance-based learning; collaborative-filtering-based recommendation; K-nearest neighbour; the Netflix problem and data completion.
- **Results:** Matrix-factorization objective and ALS updates [D]; curse of dimensionality for distance-based methods [P].
- **Build:** kNN with KD-tree, user–user and item–item collaborative filtering, ALS matrix factorization from scratch.

### U9.12 Data mining: preprocessing, association rules, sequence mining, outliers and case studies
**Sources:** DMIN W1–2,5–8, o
- **Topics:** Introduction to data mining; data preprocessing; association rule mining; classification basics; clustering and outlier detection; sequence mining; evaluation and visualization; case studies on industrial problems; implementations in open-source software; data mining as an interdisciplinary topic spanning databases, machine learning and algorithms.
- **Results:** Apriori anti-monotonicity (downward closure) [P]; FP-growth correctness [S]; support, confidence and lift [Def].
- **Build:** Apriori and FP-growth, PrefixSpan sketch and an end-to-end mining pipeline (clean, mine, evaluate, visualize).
- **Gap-fills:** *[inferred: Han–Kamber; Tan–Steinbach–Kumar]* feature selection, imbalanced data, data warehousing basics.

### U9.13 Learning theory: PAC, VC dimension, generalization and modern overparametrization
**Sources:** IMLK W7, o; MLESA W12; FML W1,3,5,8–10,12; MLE o
- **Topics:** Computational learning theory; PAC learning model; sample complexity; VC dimension; learning theory; Bayes consistency and generalization rate; overparametrization; minimal versus optimal regularization; latent variables; modularity in modelling; deep learning models; estimation error in deep learning; optimization error and implicit bias in deep learning; tradeoffs between representational power and learnability; model averaging; hypothesis-space capacity; overparametrization regime in linear regression connecting to billion-parameter models; modern concepts in ML: overparametrization; optional videos (RL framework, TD learning, solution methods, applications).
- **Results:** PAC bound for finite hypothesis classes [P]; VC-dimension generalization bound [S]; Sauer–Shelah lemma [P]; Rademacher-complexity bound [S]; benign overfitting / double descent for min-norm interpolation [S].
- **Build:** empirical double-descent experiment with random features and min-norm least squares.
- **Gap-fills:** *[inferred: Bach Ch.4, 12, 15; Shalev-Shwartz–Ben-David]* uniform convergence, margin bounds, lower bounds, online-to-batch conversion (link to U10).

### U9.14 Symbolic and knowledge-based machine learning, tools and cognitive-science influences
**Sources:** MLK W4–8, o
- **Topics:** Inductive learning based on symbolic representations and weak theories; learning enabled by prior theories; inductive logic programming; decision-tree-based inductive learning; reinforcement learning and deep learning as seen in the course; machine-learning-based artificial neural networks; tools and resources; cognitive science influences; examples, demos and exam preparation.
- **Results:** Version-space convergence [P]; ID3 entropy criterion [D]; inductive-bias characterization of learners [P].
- **Build:** a small ILP learner (FOIL-style) and ID3 from scratch.
- **Gap-fills:** *[inferred: Mitchell Ch.2, 10–12]* version spaces, explanation-based learning, first-order rule learning; link to neuro-symbolic agent design in D14.

## D10. Sequential Decision Making: Bandits and Reinforcement Learning

Aim: online learning, regret analysis and bandits (from the Bandit Algorithms course), then MDPs and reinforcement learning, which the LLM-alignment units (RLHF, PPO, DPO) require. Benchmarks (recalled; partly confirmed from published contents): Lattimore–Szepesvári, *Bandit Algorithms* (parts on probability and concentration, stochastic and adversarial bandits, lower bounds, contextual and linear bandits, Bayesian methods and non-stationary bandits, ending with partial monitoring and Markov decision processes); Cesa-Bianchi–Lugosi, *Prediction, Learning, and Games*; Bubeck–Cesa-Bianchi, *Regret Analysis of Stochastic and Nonstochastic Multi-armed Bandit Problems*; Sutton–Barto, *Reinforcement Learning: An Introduction*.

### U10.1 From batch to online learning: adversarial full-information and bandit settings
**Sources:** BAN W1–4, o
- **Topics:** Introduction to bandit algorithms; from the batch to the online setting; exploration versus exploitation dilemma; adversarial setting with full information (Halving algorithm, weighted majority (WM) algorithm); adversarial setting with bandit information; regret lower bounds for the adversarial setting; applications in online advertising, recommendation systems, auctions, routing and e-commerce.
- **Results:** Halving mistake bound log₂|H| [P]; weighted-majority/Hedge regret O(√(T ln N)) [P]; Exp3 regret O(√(TK ln K)) [P]; adversarial lower bound Ω(√(TK)) [S].
- **Build:** Hedge and Exp3 from scratch and regret curves against adaptive and oblivious adversaries.

### U10.2 Stochastic bandits: regret notions, UCB, KL-UCB and lower bounds
**Sources:** BAN W5–8, o
- **Topics:** Introduction to the stochastic setting and various regret notions; a primer on concentration inequalities (see U5.7); stochastic bandit algorithms UCB and KL-UCB; explore-then-commit and ε-greedy; lower bounds for stochastic bandits; Thompson sampling as a Bayesian alternative.
- **Results:** UCB logarithmic regret bound [P]; KL-UCB asymptotic optimality [S]; Lai–Robbins instance-dependent lower bound [S]; minimax lower bound via change of measure [S].
- **Build:** UCB1, KL-UCB, Thompson sampling and ε-greedy on Bernoulli bandits with confidence-interval plots.
- **Gap-fills:** *[inferred: Lattimore–Szepesvári Ch.6–16, 34–36]* MOSS, Bayesian regret, non-stationary bandits.

### U10.3 Contextual bandits and pure exploration
**Sources:** BAN W9–12, o
- **Topics:** Introduction to contextual bandits; overview of contextual bandit algorithms; introduction to pure-exploration setups (fixed confidence versus fixed budget); algorithms for pure exploration (LUCB, KL-LUCB, lil'UCB).
- **Results:** LinUCB regret bound [S]; sample complexity of LUCB [S]; lower bound for best-arm identification [S].
- **Build:** LinUCB on a simulated recommendation task; LUCB for best-arm identification.
- **Gap-fills:** *[inferred: Lattimore–Szepesvári Ch.18–19]* linear bandits, offline policy evaluation (links to U15.3 evaluation of deployed systems).

### U10.4 Markov decision processes, dynamic programming and temporal-difference learning
**Sources:** MLESA W12; MLK o; OFF W12
- **Topics:** Introduction to reinforcement learning; the RL framework; temporal-difference (TD) learning; solution methods; applications; reinforcement learning within the symbolic-ML course; Markov decision processes and value functions; dynamic programming (policy and value iteration); Monte Carlo, TD(0) and Q-learning; exploration in RL; optional videos on the RL framework, TD learning, solution methods and applications.
- **Results:** Bellman optimality equation [D]; contraction of the Bellman operator and convergence of value iteration [P]; policy-improvement theorem [P]; Q-learning convergence (statement) [X].
- **Build:** value iteration, tabular Q-learning and SARSA on a grid world; deep Q-network sketch (after U11).
- **Gap-fills:** *[inferred: Sutton–Barto Ch.3–7, 9–10]* function approximation, off-policy learning, eligibility traces.

### U10.5 Policy gradient, actor–critic and proximal policy optimization
**Sources:** FDL W12; MFGAI W12
- **Topics:** Reinforcement learning for fine-tuning; proximal policy optimization (PPO); policy gradient theorem; baselines and advantage estimation; trust-region and clipped-surrogate objectives; connection to RLHF and alignment (taught again in U12.9).
- **Results:** Policy-gradient theorem [D]; baseline invariance [P]; monotonic-improvement bound motivating TRPO/PPO [S]; PPO clipped objective [D].
- **Build:** REINFORCE with baseline and a PPO implementation on a small control task.
- **Gap-fills:** *[inferred: Sutton–Barto Ch.13; Schulman et al. TRPO/PPO papers, recalled, not checked]* generalized advantage estimation, KL penalties and entropy regularization.


# PART C. DEEP LEARNING AND GENERATIVE AI

## D11. Deep Learning Foundations

Aim: neural networks from perceptron to CNNs, RNNs, autoencoders and explainability, with backpropagation and every optimizer written by hand before PyTorch. Benchmarks (recalled; contents partly confirmed): Goodfellow–Bengio–Courville, *Deep Learning* (applied math and ML basics; modern practical deep networks: feedforward networks, regularization, optimization, CNNs, sequence modelling, practical methodology, applications; research topics: linear factor models, autoencoders, representation learning, structured probabilistic models, Monte Carlo methods, partition function, approximate inference, deep generative models); Nielsen, *Neural Networks and Deep Learning*; Haykin; Bengio, *Learning Deep Architectures for AI*; Foster, *Generative Deep Learning* 2nd ed. (Ch. 2 on deep learning); Bhuyan, *Computer Vision and Image Processing*.

### U11.1 Perceptron, multilayer networks, activations and loss functions
**Sources:** FDL W1, o; MFML W11; MLDL W10; MLE W5; MLESA W5; IMLK W6; MLCE W11; FML W9; MLK W6; GEN 2.7, 3.1, 3.2; SMLM W9,11
- **Topics:** Overview of machine learning and deep learning; difference between ML and DL with an example; history and evolution of deep learning with computational efficiency; biological inspiration (the neuron); examples of end-to-end deep learning; perceptron (Rosenblatt, 1958): single-layer perceptron, perceptron learning algorithm, single-layer perceptron numerical problem and limitations; introduction to the Colab environment and building a simple perceptron; multilayer perceptron (MLP); shallow versus deep neural networks; how to design a neural network with examples; activation functions and non-linearity; loss functions; neural networks: input → weights → activation → output, layers and neurons; hands-on network on a dummy dataset; a problem-first approach (business problem: why customer churn is increasing, what data is needed, how to model it); neural nets, perceptron, backpropagation algorithm; RBF neural network and applications; early models of neural networks; machine-learning-based artificial neural networks; deep learning models (modularity in modelling, overparametrization); Back Propagation Algorithm; computer vision, natural language processing, healthcare and robotics as application areas; CNNs, RNNs and autoencoders as the course arc; deep neural networks (SMLM Week 11); Advanced Techniques 2 (autoencoders, GAN).
- **Results:** Single-layer perceptron cannot represent XOR [P]; universal approximation theorem for one hidden layer [S]; depth–width separation examples [S].
- **Build:** perceptron, a 2-layer MLP and arbitrary-depth MLP from scratch in NumPy, trained on XOR, a churn-style tabular dataset and MNIST.
- **Gap-fills:** *[inferred: Goodfellow Ch.6; Nielsen Ch.1–2]* hidden-unit choices (ReLU family, GELU, SiLU), output units and cost functions as maximum likelihood.

### U11.2 Backpropagation and training deep networks
**Sources:** FDL W2; MFML W11; GEN 2.7, 3.3; MLE W5; MLESA W5; MLDL W10; MLCE W11; FML W10
- **Topics:** Gradient descent and mathematical formulation of the backpropagation algorithm; backpropagation: how neural networks learn; learning: loss functions, optimization, overfitting; initialization; training and validation; backpropagation in deep learning (estimation error, optimization error, implicit bias); working of feed-forward neural networks; hands-on artificial neural network for classification and regression with exposure to hyperparameter tuning; momentum-based GD, Nesterov accelerated GD, stochastic GD, AdaDelta, AdaGrad, RMSProp and Adam (optimizers taught in U8.10 and used here); back propagation algorithm (MFML Week 11).
- **Results:** Backpropagation computes the exact gradient in O(forward cost) [D]; vanishing/exploding gradient bounds for deep chains [D]; Xavier/He initialization variance derivation [D].
- **Build:** reverse-mode autodiff engine and full MLP training loop from scratch; gradient check against finite differences; then re-implementation in PyTorch (`autograd`) as the oracle.
- **Gap-fills:** *[inferred: Goodfellow Ch.8, 11]* batch normalization, learning-rate warm-up and schedules, practical methodology (debugging, diagnostics).

### U11.3 Overfitting, regularization and generalization in deep networks
**Sources:** FDL W2; GEN 2.8, 3.3; MLESA W5
- **Topics:** What overfitting and underfitting are; the bias–variance tradeoff; detecting overfitting: training versus validation loss; regularization: penalizing complexity; L1 versus L2 (geometry and sparsity); dropout and early stopping; data augmentation; regularization techniques; putting it together: a scikit-learn pipeline; summary and quick reference; hyperparameter tuning.
- **Results:** Dropout as an ensemble/approximate Bayesian average [S]; L2 regularization equals weight decay for SGD [P]; early stopping as implicit L2 for quadratic loss [D].
- **Build:** dropout, weight decay, early stopping and augmentation layers from scratch; learning-curve diagnostics.

### U11.4 Convolutional neural networks and image representation
**Sources:** FDL W3–4; MLE W6–7; MLDL W11; MLCE W11–12; CSO W1
- **Topics:** Fundamentals of image representation, image preprocessing and data augmentation; introduction to convolutional neural networks (CNN), inspiration behind CNN, key components and CNN layers explained in detail with the math behind; hands-on simple CNN for binary and multiclass classification; CNN operations and CNN architectures; CNN training, transfer learning and applications; vanishing and exploding gradients in deep neural networks; standard CNN architectures (LeNet-5, AlexNet, VGGNet, GoogLeNet, ResNet); introduction to transfer learning; hands-on transfer learning and building an ensemble model; working of convolutional neural networks; basics of CNN computations.
- **Results:** Convolution as a linear, translation-equivariant operator [P]; output-size and parameter-count formulae [D]; ResNet identity mapping eases optimization (gradient path) [D]; backpropagation through convolution is a correlation [D].
- **Build:** conv, pooling and a small CNN (forward and backward) in NumPy via im2col; then PyTorch; compare receptive-field arithmetic with measured gradients.
- **Gap-fills:** *[inferred: Goodfellow Ch.9]* pooling and invariance, 1-D/3-D convolutions, depthwise-separable convolutions, normalization layers.

### U11.5 Explainable AI for deep models
**Sources:** FDL W5
- **Topics:** Introduction to XAI and the need for XAI; techniques of XAI; XAI methods with mathematical foundations and numerical examples (PCI, occlusion, SHAP, LIME, Grad-CAM, guided backpropagation, CAMs); hands-on interpreting the results of a CNN model using XAI techniques.
- **Results:** Shapley value axioms and uniqueness [P]; Grad-CAM as gradient-weighted activation map [D]; LIME as local linear surrogate [D].
- **Build:** occlusion maps, LIME and Shapley sampling from scratch; Grad-CAM in PyTorch.

### U11.6 Segmentation and object detection
**Sources:** FDL W6; MLDL W12
- **Topics:** CNN-based segmentation algorithms: UNet and attention-based UNet; CNN-based object detection models: YOLO, RCNN and Faster RCNN; hands-on object detection using YOLO; hands-on UNet and attention UNet; U-Net, applications and case studies.
- **Results:** Intersection-over-union and non-maximum suppression [Def]; anchor/region-proposal losses [D].
- **Build:** U-Net for a small segmentation set; IoU and NMS from scratch; YOLO inference with a pretrained model.

### U11.7 Recurrent networks: RNN, LSTM, GRU, backpropagation through time and attention in RNNs
**Sources:** FDL W7–8; MLE W8; MLCE W12; MLDL W12; MLK W6; DLNLP W4
- **Topics:** Sequence-to-sequence models; introduction to recurrent neural networks (RNN), limitations of feed-forward neural networks, need for RNN and their structure; variants of RNN; challenges in RNN (vanishing and exploding gradients); backpropagation through time; numerical problem on RNN; hands-on RNN and its variants on structured data; long short-term memory (LSTM) architecture and its necessity; bidirectional LSTM; stacked LSTMs; GRU architecture; LSTM versus GRU: speed, accuracy, complexity and when to use GRU over LSTM; why attention mechanism in RNNs, working of the attention mechanism and its benefits; hands-on LSTM models for structured and unstructured data; recurrent neural networks implementation in Python; RNN language models (RNN LMs), GRUs, LSTMs, Bi-LSTMs; LSTMs for sequence labeling; LSTMs for sequence-to-sequence.
- **Results:** Gradient of BPTT as a product of Jacobians [D]; vanishing/exploding conditions via spectral radius [D]; LSTM cell-state additive path [D].
- **Build:** vanilla RNN, LSTM and GRU with BPTT from scratch; character-level language model.
- **Gap-fills:** *[inferred: Goodfellow Ch.10]* gradient clipping, echo-state ideas, teacher forcing.

### U11.8 Autoencoders and representation learning
**Sources:** FDL W10; MLDL W12; MLE W12; MLCE W8; GEN 2.6
- **Topics:** Unsupervised learning: introduction to autoencoder and architecture of AE with mathematical foundation; types (simple, deep, CNN-based); training of autoencoders; hands-on building an AE and its variants; autoencoders and their relation to PCA; feature learning through embeddings: one-hot vectors and classification with them, limitations of sparse representations, why sparsity breaks similarity, distributional semantics (words by context), dense (distributed) representations and embeddings; auto encoders and relation to PCA; Advanced Techniques 2 (autoencoders, generative adversarial networks).
- **Results:** Linear autoencoder with MSE recovers the PCA subspace [P]; sparse/denoising/contractive objectives [D].
- **Build:** dense, convolutional and denoising autoencoders from scratch; latent-space visualization.

## D12. Natural Language Processing, the Transformer and Large Language Models

Aim: NLP foundations, embeddings, attention and the Transformer, pretraining, decoding, prompting, alignment (RLHF, PPO, DPO), parameter-efficient fine-tuning and prompt optimization, with every mechanism built in NumPy or PyTorch. Benchmarks (confirmed against the published contents): Jurafsky–Martin, *Speech and Language Processing* 3rd ed. (words and tokens, n-gram language models, logistic regression and text classification, embeddings, neural networks, Transformers and pretraining, post-training, masked language models, interpretability, information retrieval and RAG, agents, machine translation, RNNs and LSTMs); Foster, *Generative Deep Learning* 2nd ed. (Transformers and large language models); Goodfellow Ch. 10 and 12.4.

### U12.1 NLP foundations and the classical NLP pipeline
**Sources:** GEN 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7; DLNLP W1, o; FDL W9
- **Topics:** NLP in the GenAI context: NLP as the interface layer of AI systems (chatbots, search, automation); real-world uses in support, finance and healthcare; text representation: Bag of Words → TF-IDF → Word2Vec → embeddings; goal: convert text to numbers; intuition: similar meaning, similar vectors; language modelling basics: predicting the next word, context window, probability distribution over words; evolution of language models: n-grams → RNN → Transformers, parallel processing and context awareness; the classical NLP pipeline: cleaning → tokenization → stopwords → lemmatization → features → model; hands-on: tokenize with NLTK, apply TF-IDF, build a simple classifier; limitations of classical NLP (no deep context, manual features, poor generalization); bridge to GenAI: classical NLP → deep learning → LLMs → agents; the agent loop (observe, reason, act); modern NLP architecture: input → embeddings → retrieval → LLM → output; hands-on task: build and compare a mini NLP pipeline; what is natural language processing; a brief primer on word-level and sentence-level tasks; n-gram language model; introduce NLP tasks; classical NLP versus deep-learning NLP; text preprocessing (tokenization, stopwords, lemmatization); question answering, text summarization and dialogs as NLP applications; in the last decade deep-learning methods became the default for NLP problems.
- **Results:** Chain rule for language-model probability [P]; maximum-likelihood n-gram estimates and smoothing (add-k, Kneser–Ney idea) [D]; perplexity as exponentiated cross-entropy [D]; TF-IDF weighting rationale [D].
- **Build:** tokenizer, n-gram LM with smoothing, TF-IDF and a Naive-Bayes/logistic text classifier from scratch; compare with NLTK and scikit-learn.
- **Gap-fills:** *[inferred: SLP3 Ch.2–4, 18]* byte-pair encoding and subword tokenization (also needed by U12.4), regular expressions and text normalization, sequence labelling for parts of speech and named entities.

### U12.2 Word representations and multilingual embeddings
**Sources:** DLNLP W2–3; FDL W9; GEN 1.2; MFGAI o
- **Topics:** Introduction to deep learning for NLP: shallow and deep neural networks and representation learning; word representations: one-hot encoding, word embeddings Word2Vec, GloVe, fastText; multilingual representations with emphasis on Indian languages; hands-on RNN for an NLP task.
- **Results:** Skip-gram with negative sampling implicitly factorizes a shifted PMI matrix [S]; GloVe objective [D].
- **Build:** skip-gram with negative sampling and GloVe from scratch; analogy and similarity tests.
- **Gap-fills:** *[inferred: SLP3 Ch.5]* contextual versus static embeddings, bias in embeddings (link to U15.4).

### U12.3 Attention and the Transformer architecture
**Sources:** GEN 3.4, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7; DLNLP W5; FDL W11; FML W9
- **Topics:** Toward GenAI: attention intuition, self-attention, transformers, the bridge to GenAI; before transformers: limitations of pre-attention models, seq2seq with an RNN, seq2seq with an attention layer, the attention idea and why attention alone was not enough, the self-attention idea; the encoder: what self-attention is, query/key/value step by step, the attention mechanism vectorized, a tiny worked example, the feed-forward layer; making deep networks train: residual connections, layer normalization, scaled dot-product attention; positional encoding (injecting order into attention); multi-head attention: why multiple heads, a 2-head worked example (computing Q, K, V; scores, softmax and the attention matrix; head outputs; combining heads; comparing the heads), a full model in PyTorch; the decoder: decoder design and overview, masked self-attention and masked multi-head self-attention, cross-attention (Q, K, V; encoder–decoder attention; matrix form; a worked example; what it cannot do), self-attention versus cross-attention, the complete decoder, autoregressive generation (the decoder loop, with a step-by-step example); evolution: "Attention Is All You Need", from attention to pretrained models, the modern transformer zoo; sequence-to-sequence with attention; transformer architectures: self-attention, encoder–decoder attention.
- **Results:** Scaled dot-product attention with 1/√d_k scaling stabilizes softmax variance [D]; permutation equivariance of self-attention without positions [P]; parameter and FLOP count of a Transformer block [D]; causal mask makes training parallel but generation sequential [P].
- **Build:** single-head, multi-head and masked attention, sinusoidal positional encoding, an encoder block, a decoder block and a tiny decoder-only Transformer trained on characters, all from scratch in NumPy, then PyTorch as the oracle.
- **Gap-fills:** *[inferred: SLP3 Ch.7; Foster Ch.9]* rotary and relative positional encodings, grouped-query attention, FlashAttention (links to U16.3), encoder-only versus decoder-only versus encoder–decoder families.

### U12.4 Pretraining, self-supervised learning and the LLM landscape
**Sources:** GEN 5.1; DLNLP W6–7, o; FDL W11–12; MFGAI W10, o
- **Topics:** The LLM landscape: BERT (contextual language-model training; the GLUE benchmark); GPT-1 and GPT-2 (decoder-only generation; LAMBADA); T5 and BART (text-to-text and denoising seq2seq); GPT-3 (few-shot and in-context learning); InstructGPT and RLHF; the open-weights wave (LLaMA, Mistral, Falcon); MMLU; the multimodal and reasoning era; a map of innovations (architecture, training, data); self-supervised learning (SSL) and pretraining, designing SSL objectives; pretrained Bi-LSTMs: ELMo; pretrained Transformers: BERT, GPT, T5, BART; self-supervised learning objectives and loss functions; masked language modeling; large language models: tokenizers, pre-training and post-training, multimodal alignment; applications: question answering, dialog modeling, text summarization; multilingual extension with application to Indian languages; auto-regressive models and large language models introduction; massive multitask language understanding (MMLU); in-context learning, parameter-efficient fine-tuning and RLHF as the course arc; deep generative models, autoregressive models, diffusion models and large language models.
- **Results:** Masked-LM and causal-LM objectives as conditional likelihoods [D]; cross-entropy loss per token and perplexity [D]; next-sentence and denoising objectives compared [P].
- **Build:** a masked-LM and a causal-LM pretraining loop at toy scale; fine-tune a small pretrained BERT/GPT for classification and QA.
- **Gap-fills:** *[inferred: SLP3 Ch.7, 9]* data curation and deduplication, training-data contamination (links to U15.1), pretraining compute budgets.

### U12.5 Scaling laws, LLM architectures and long context
**Sources:** DLNLP W9,11; CSO W5
- **Topics:** Scaling laws; various large language models and their unique architectural differences; handling long context; basics of large language models (systems view).
- **Results:** Power-law loss versus compute, parameters and data (Kaplan/Chinchilla form) [X, empirical law: fitted, not proved]; compute-optimal allocation [D from the fitted law].
- **Build:** fit a scaling law to training runs of a family of tiny Transformers.
- **Gap-fills:** *[inferred: SLP3 Ch.7; Kaplan et al. and Hoffmann et al., recalled, not checked]* mixture-of-experts, sliding-window and sparse attention, positional-interpolation tricks for long context.

### U12.6 Decoding strategies and sampling
**Sources:** GEN 5.3, 6.2; MFGAI W11
- **Topics:** Choosing the next word at each step; greedy decoding and its problem; beam search (how it works, with an example); greedy and beam search are deterministic; the quality-versus-diversity tradeoff; random sampling: temperature, top-k, top-p (nucleus); repetition and frequency penalties; max tokens and stop sequences; parameter cheat sheet; tutorial: putting it all together; common LLM inference terms: tokens, temperature, top-k, top-p; LLMs: models, sampling, inference and quantization methods (sampling part).
- **Results:** Temperature as softmax scaling and its entropy limits [D]; top-p truncation as adaptive support [P]; beam search is not exact search [P].
- **Build:** greedy, beam, temperature, top-k and top-p decoders from scratch over a small LM.

### U12.7 Prompting: fundamentals, APIs and advanced techniques
**Sources:** GEN 5.2, 5.4, 6.1, 6.3, 6.4; DLNLP W9; FDL W11
- **Topics:** What prompts are; a first basic prompt, then a more advanced one; elements of a prompt; prompting through APIs: introduction to the OpenAI API and frontier models; basic chat completion; roles in prompting; tool calling with an example; coding and reasoning models; image generation models; examples: a chatbot application, image generation; introduction: prompting and the autoregressive language model, what a prompt is, what prompt engineering is; types of prompting: overview, zero-shot and few-shot prompting, chain-of-thought (CoT) prompting and its variants (zero-shot CoT, few-shot CoT, automatic CoT, self-consistency), ReAct prompting, meta prompting, directional stimulus prompting (DSP), prompt chaining, tree of thoughts (ToT); limitations of LLM prompting; mitigating prompt-injection attacks; in-context learning; chain-of-thought prompting; limits and defenses.
- **Results:** Self-consistency as marginalization over reasoning paths [D]; why chain-of-thought helps (extra serial computation) [S].
- **Build:** a chat client with roles, tool-calling and a ReAct loop; prompt-chaining pipeline; ToT search on a small puzzle. Live API calls follow a recorded-response replay first and run only under a spend cap (Master Rules 11.2).

### U12.8 Instruction tuning, RLHF and alignment: PPO and DPO
**Sources:** DLNLP W8, o; MFGAI W12; FDL W12; GEN 5.1
- **Topics:** Instruction fine-tuning; FLAN-T5; reinforcement learning through human feedback (RLHF); LLMs: reinforcement-learning-based alignment methods (PPO, DPO); reinforcement learning for fine-tuning; proximal policy optimization; InstructGPT and RLHF: aligning models with human preferences; post-training.
- **Results:** Bradley–Terry reward-model likelihood [D]; KL-regularized RLHF objective and its closed-form optimal policy [D]; DPO loss derived from that closed form [D]; PPO clipped objective (see U10.5) [D].
- **Build:** reward model on preference pairs; toy PPO-for-text and DPO fine-tuning of a tiny LM, from scratch.
- **Gap-fills:** *[inferred: SLP3 Ch.8; Ouyang et al., Rafailov et al., recalled, not checked]* constitutional and AI-feedback methods, reward hacking.

### U12.9 Parameter-efficient fine-tuning: LoRA and QLoRA
**Sources:** DLNLP W10; FDL W11
- **Topics:** Parameter-efficient fine-tuning (PEFT): LoRA and QLoRA; low-rank adaptation.
- **Results:** Low-rank update ΔW = BA parameter count and rank bound [D]; QLoRA 4-bit NormalFloat plus paged optimizers (stated) [X→U16.4].
- **Build:** LoRA layer from scratch merged into a frozen Transformer; compare full fine-tuning and LoRA on a small task.
- **Gap-fills:** *[inferred: Hu et al., Dettmers et al., recalled, not checked]* adapters, prefix tuning, link to SVD low-rank theory in U4.9.

### U12.10 Prompt optimization, compression and prompt security
**Sources:** GEN 7.1, 7.2, 7.4, 7.5
- **Topics:** Prompt optimization: motivation; the need for versioning, testing and iteration (prompts as versioned artifacts); optimization objectives; types: manual and automatic; automatic prompt optimization (APO): instruction search, gradient optimization, evolutionary optimization, DSPy; verbalized sampling: the mode collapse problem and verbalized sampling; prompt compression: basic and advanced techniques, the LLMLingua family (LLMLingua, LLMLingua-2, with examples); prompt security: prompt injection, indirect prompt injection, prompt leaking.
- **Results:** Prompt search as discrete black-box optimization (objective, search space, evaluation noise) [Def]; mode collapse from preference tuning [S].
- **Build:** a prompt-version registry and A/B test harness; evolutionary prompt search over a tiny task; token-pruning prompt compressor.

## D13. Deep Generative Models

Aim: the probabilistic foundations of generative modelling and every major model family (GANs, VAEs, autoregressive models, energy-based and score-based models, diffusion models), each derived and implemented from scratch. Benchmarks (confirmed from published contents where stated): Foster, *Generative Deep Learning* 2nd ed. (generative modeling, deep learning, VAEs, GANs, autoregressive models, normalizing flows, energy-based models, diffusion models, Transformers, advanced GANs, music generation, world models, multimodal models); Goodfellow Ch. 13–20; Murphy, *Probabilistic Machine Learning: Advanced Topics* (recalled, not checked); Kingma–Welling, Goodfellow et al., Ho et al., Song et al. (recalled, not checked).

### U13.1 Probabilistic deep generative modelling: foundations and taxonomy
**Sources:** MFGAI W1, o; FML W11, o; MLE W11
- **Topics:** Introduction to probabilistic deep generative modelling; probabilistic foundations and learning algorithms of deep generative models; likelihood estimation; energy-based models (EBMs); MLE; structured probabilistic models; Monte Carlo methods; taxonomy of generative models (explicit/implicit density, tractable/approximate); hands-on PyTorch implementation.
- **Results:** MLE equals minimizing KL(p_data‖p_θ) [D]; the partition function makes EBM likelihood intractable [P]; importance sampling and its variance [D].
- **Build:** a tiny density estimator by MLE (Gaussian mixture) and importance-sampling estimator from scratch.
- **Gap-fills:** *[inferred: Foster Ch.1; Goodfellow Ch.16–17]* generative versus discriminative modelling, representation learning, core probability tools.

### U13.2 Generative modelling via variational divergence minimization
**Sources:** MFGAI W2
- **Topics:** Generative modelling via variational divergence minimization; f-divergences (KL, reverse KL, Jensen–Shannon, total variation); variational (dual) representation of f-divergences; f-GAN.
- **Results:** Variational lower bound on an f-divergence via the Fenchel conjugate [D]; JS divergence recovers the original GAN objective [D].
- **Build:** numerical estimation of f-divergences between Gaussians; f-GAN objective on a 1-D toy distribution.

### U13.3 Generative adversarial networks: formulation, training, WGAN and applications
**Sources:** MFGAI W3–4, o; MLDL W12; MLE W12; FDL W12
- **Topics:** Generative adversarial networks Part 1 (introduction and formulation); minimax game and optimal discriminator; GAN training difficulties (mode collapse, vanishing gradients); Part 2: WGANs (Wasserstein distance, Kantorovich–Rubinstein duality, weight clipping and gradient penalty) and applications; generative adversarial network (GAN) as a recent trend in deep learning; VAEs and GANs as deep generative models; generative adversarial networks.
- **Results:** Optimal discriminator D*(x)=p_data/(p_data+p_g) [D]; the generator objective equals 2·JS(p_data‖p_g) − log 4 at D* [D]; Kantorovich–Rubinstein duality [S]; Wasserstein distance remains informative for disjoint supports [P].
- **Build:** vanilla GAN, WGAN-GP and a conditional GAN from scratch on 2-D and MNIST data; mode-collapse experiments.
- **Gap-fills:** *[inferred: Foster Ch.4, 10]* DCGAN, StyleGAN-style progressive growing, evaluation with Inception score and FID.

### U13.4 Variational autoencoders, improvements and VQ-VAE
**Sources:** MFGAI W5–6; FDL W12; MLE W12
- **Topics:** Generative modelling via variational auto-encoding; evidence lower bound (ELBO); reparameterization trick; amortized inference; VAE improvisations (β-VAE, importance-weighted bounds, hierarchical and conditional VAEs); VQ-VAE (vector-quantized latents, straight-through estimator, codebook learning); VAEs and GANs compared; improvisations and VQVAE.
- **Results:** ELBO = reconstruction − KL(q‖p) and the gap equals KL(q‖posterior) [D]; reparameterization gives low-variance pathwise gradients [D]; closed-form KL between Gaussians [D].
- **Build:** VAE and VQ-VAE from scratch, with latent interpolation and posterior-collapse diagnostics.

### U13.5 Autoregressive models
**Sources:** MFGAI W10, o
- **Topics:** Auto-regressive models (chain-rule factorization, masked/causal networks, PixelCNN-style and Transformer-based decoders) and the introduction to large language models; likelihood training and sampling cost.
- **Results:** Exact likelihood by chain rule [P]; exposure bias and teacher forcing [S].
- **Build:** a character/pixel-level autoregressive model from scratch (shares code with U12.3).

### U13.6 Energy-based and score-based models; Langevin sampling
**Sources:** FML W11; MFGAI W9; MLE W11
- **Topics:** Energy-based models, maximum-likelihood training with MCMC and contrastive divergence; Langevin sampling; score-based models; score matching (explicit, denoising, sliced); conditional diffusion models and score-based models; Monte Carlo methods.
- **Results:** Gradient of the log-likelihood of an EBM is a difference of expectations [D]; Langevin dynamics targets p(x) [S]; denoising score matching equals score of the noised distribution [D].
- **Build:** Langevin sampler on a 2-D mixture; denoising score matching on toy data.
- **Gap-fills:** *[inferred: Goodfellow Ch.18; Foster Ch.7]* contrastive divergence, noise-contrastive estimation.

### U13.7 Denoising diffusion probabilistic models, conditional diffusion and Stable Diffusion
**Sources:** MFGAI W7–9, o; FDL W12
- **Topics:** Denoising diffusion probabilistic models (DDPMs): formulation; forward and reverse diffusion; variational lower bound; denoising score matching; diffusion models: multiple forms and implementation (ε-prediction, x₀-prediction, v-prediction, DDIM, SDE and probability-flow ODE views); conditional diffusion models (classifier guidance, classifier-free guidance); score-based models; Stable Diffusion: latent-space denoising; deep generative models overview.
- **Results:** Closed-form forward marginal q(x_t|x₀) [D]; reverse-process posterior mean [D]; ELBO simplifies to a denoising regression loss [D]; DDIM as a deterministic reverse process [D]; SDE/probability-flow correspondence [S].
- **Build:** DDPM with a small U-Net (reuse U11.6) on 2-D then MNIST; classifier-free guidance; latent diffusion using the autoencoder of U11.8.
- **Gap-fills:** *[inferred: Foster Ch.8; Ho et al.; Song et al., recalled, not checked]* noise schedules, fast samplers, evaluation by FID, text-to-image conditioning with cross-attention (reuses U12.3).

### U13.8 Normalizing flows (gap-fill from the references)
**Sources:** none (gap-fill unit added from the references)
- **Topics:** Change of variables for densities and the Jacobian determinant (links to U3.3 and U4.5); invertible networks with tractable determinants; coupling layers (RealNVP-style) and autoregressive flows; training by exact maximum likelihood; continuous normalizing flows and the probability-flow ODE (link to U13.7); comparison of flows, GANs, VAEs, autoregressive and diffusion models on likelihood, sampling speed and sample quality.
- **Results:** Change-of-variables formula for densities [D]; determinant of a triangular Jacobian is the product of its diagonal [P]; log-likelihood of a flow [D].
- **Build:** RealNVP on a 2-D dataset from scratch, with density plots.
- **Gap-fills:** *[inferred: Foster, chapter on normalizing flow models (the publisher's description confirms the book covers them; chapter number recalled, not checked); Goodfellow Ch.20]* this family appears in the references but in none of the outlines; added so the model taxonomy of U13.1 is complete.


# PART D. LLM APPLICATIONS, EVALUATION AND SAFETY

## D14. Retrieval-Augmented Generation and Agentic Systems

Aim: RAG from first principles to production, then agentic RAG, multi-agent orchestration, memory and provenance, implemented with and without frameworks. Benchmarks: Jurafsky–Martin, *SLP3* (confirmed: information retrieval and RAG; agents); Manning–Raghavan–Schütze, *Introduction to Information Retrieval* (recalled, not checked); Khattab–Zaharia (ColBERT), Reimers–Gurevych (Sentence-BERT), Lewis et al. (RAG), Yao et al. (ReAct) (recalled, not checked).

### U14.1 Why RAG, RAG architecture and classical retrievers
**Sources:** GEN 8.1, 8.2, 8.3; DLNLP W11
- **Topics:** Why RAG: limitations of LLMs (hallucinations, verifiability, knowledge cutoff); motivation for RAG; introduction to RAG: overview, architecture and workflow, with an example; sparse retrieval and dense retrieval; augmentation and generation; the retrieval phase in detail (the retrieval pipeline, chunking and query formulation); retrievers: information-retrieval methods; TF-IDF; BM25 (a non-binary model); retrieval-augmented generation in the course on long context.
- **Results:** TF-IDF and BM25 scoring formulas and saturation of term frequency [D]; inverted-index query processing [D].
- **Build:** inverted index, TF-IDF and BM25 retriever and a minimal RAG loop from scratch.
- **Gap-fills:** *[inferred: SLP3 Ch.11; Manning et al.]* retrieval metrics (precision@k, recall@k, MRR, nDCG), query likelihood models.

### U14.2 RAG failure modes, types of RAG and assessment
**Sources:** GEN 8.4, 8.5, 8.6
- **Topics:** RAG failure modes: retrieval failures, context failures, generation failures; types of RAG: standard RAG, standard RAG with memory, agentic RAG, Chain-of-RAG (CoRAG) mechanics and more examples; assessment: the RAG assessment framework; RAGAS.
- **Results:** Decomposition of end-to-end RAG error into retrieval recall and generation faithfulness [D].
- **Build:** failure-injection harness (drop gold chunk, add distractor, conflicting context) and RAGAS-style metrics (faithfulness, answer relevance, context precision/recall).

### U14.3 Sparse retrieval limits and dense representations
**Sources:** GEN 9.1, 9.2
- **Topics:** RAG workflow recap; sparse retrieval and why sparsity breaks similarity; dense representations; vector embeddings; the RAG-with-embeddings pipeline; sentence embeddings from BERT and how they compare.
- **Results:** Cosine similarity versus dot product versus Euclidean distance and when they coincide [P].
- **Build:** mean-pooled BERT sentence embeddings versus TF-IDF on a retrieval benchmark.

### U14.4 Learning retrieval-oriented embeddings and choosing an embedding model
**Sources:** GEN 9.3, 9.4
- **Topics:** Getting negative examples and hard mining; dense retrieval with a bi-encoder; the costlier but more accurate alternative (cross-encoder); Sentence-BERT architecture; choosing an embedding model: common models (all-MiniLM-L6-v2 for prototyping, OpenAI text-embedding-3-small); Matryoshka embeddings and how they order dimensions; design decisions, including under real conditions; the most common silent production RAG bug.
- **Results:** InfoNCE/contrastive loss with in-batch negatives [D]; Matryoshka loss as a multi-prefix objective [D].
- **Build:** a bi-encoder trained with in-batch and hard negatives; embedding-model comparison with a cost and quality table.

### U14.5 Document processing and chunking
**Sources:** GEN 9.5, 9.6
- **Topics:** Document processing basics, including OCR; design decisions for documents; chunking: why chunk, right-sizing for retrieval; strategies: fixed-size, sliding window, semantic; matching strategy to document type (uniform prose and baselines; strongly structured documents: Markdown, legal clauses, API docs, code); tuning chunking and an overlap myth; general RAG prose.
- **Build:** four chunkers and a recall@k comparison on structured and unstructured corpora.

### U14.6 Vector databases and indexes: KNN, IVF, PQ, HNSW, FAISS and ChromaDB
**Sources:** GEN 9.7, 10.1, 10.2
- **Topics:** Vector databases: introduction and why an efficient vector database is required; KNN, the naive approach; IVF (inverted file index) and how much work it saves; PQ (product quantization): indexing, the 95% memory claim, and search; IVF and PQ recap; IVF + PQ combined and why the approximation works; HNSW: zooming in through layers, the efSearch candidate list, why search is about log N; FAISS; ChromaDB (a database wrapped around vector search); design decisions for vector databases: prototype scale versus raw speed and large scale; choosing a FAISS index (corpus size is the main driver); vector index methods.
- **Results:** Memory and distance-computation cost of IVF, PQ and IVF-PQ [D]; HNSW expected search complexity (small-world argument) [S]; recall–latency trade-off curves [Def].
- **Build:** brute-force KNN, IVF with k-means centroids, PQ codebooks and a small HNSW from scratch; compare with FAISS and ChromaDB.

### U14.7 The retrieval pipeline: bi-encoder, cross-encoder, ColBERT and two-stage retrieval
**Sources:** GEN 10.3
- **Topics:** Semantic search and a minimal end-to-end pipeline; bi-encoder versus cross-encoder: the cost of accuracy; ColBERT and late interaction; the two-stage pattern as the industry standard; three failures that silently wreck a RAG system.
- **Results:** Latency/cost model of two-stage retrieve-then-rerank [D]; MaxSim late-interaction scoring [Def].
- **Build:** hybrid (BM25 + dense) first stage with reciprocal-rank fusion and a cross-encoder reranker.

### U14.8 Production RAG: request shaping, query transformation, routing, security, cost and observability
**Sources:** GEN 10.4, 10.5, 10.6, 10.7
- **Topics:** From RAG to agentic: the enterprise DevOps and support agent; what is different in production; request shaping, with a project example; query transformations: rewriting, follow-up questions, multi-query retrieval, step-back prompting; query routing strategies (rule-based, embedding-based, classifier-based, LLM-based, hybrid) and applications (data-source routing, model and workflow routing, prompt and index routing); security, cost and observability: retrieval gateways, access control and least privilege, cost management, semantic caching and choosing the threshold, observability.
- **Results:** Semantic-cache hit-rate versus threshold and error trade-off [D].
- **Build:** query rewriter, multi-query retriever, router and semantic cache with metrics and tracing.

### U14.9 Limits of single-shot RAG and the move to agents
**Sources:** GEN 10.8, 11.1
- **Topics:** Limits of single-shot RAG: the multi-hop query case study; why if/else logic is not enough; from passive search to active problem solving; from pipelines to agents: the limits of linear RAG; simple versus complex tasks; agentic RAG: from pipeline to control loop.
- **Build:** a multi-hop QA benchmark and a single-shot baseline measuring where it fails.

### U14.10 Agent basics, tool calling and orchestration
**Sources:** GEN 11.2, 11.3
- **Topics:** Anatomy of an agent and its core loop; an example in the project context; tool calling, the engine of agency, and designing a tool; the multi-agent concept: a DevOps multi-agent team; orchestration: planners and executors, why separate planning from execution; a case study of the planner in action; specialist agents in the execution phase; re-planning.
- **Build:** tool schema, a tool-calling loop and a planner–executor pair from scratch (no framework).

### U14.11 Planning with ReAct
**Sources:** GEN 11.4
- **Topics:** The limitation of pure chain-of-thought reasoning; the formal definition of the ReAct loop; scaling ReAct: the context and tool-exhaustion problem; hierarchical ReAct: triage as a meta-planner; caveat in production: the planning trap.
- **Build:** ReAct and hierarchical-ReAct agents with a step-budget and failure analysis.

### U14.12 State machines and LangGraph
**Sources:** GEN 11.5
- **Topics:** What a state machine is and why use one for AI; LangChain versus LangGraph; core concepts: nodes and edges; designing the multi-agent DevOps graph (three parts); wiring the team in code and the power of compile(); human-in-the-loop (HITL): pausing the infrastructure agent; caveats: multi-agent infinite loops and state bloat.
- **Results:** Graph termination conditions and loop bounds [D].
- **Build:** the same agent team as a hand-written state machine, then in LangGraph; HITL interrupt and resume.
- **Gap-fills:** *[inferred: SLP3 Ch.12]* agent protocols and tool standards (stated at survey level).

### U14.13 Agentic memory
**Sources:** GEN 11.6
- **Topics:** The concept and types of memory; episodic memory and its limits; semantic (long-term) memory: writing and reading; the self-healing system in action; caveats: memory contradiction and the needle in a haystack.
- **Build:** episodic buffer and semantic store with conflict resolution and recall evaluation.

### U14.14 Provenance and citations
**Sources:** GEN 11.7
- **Topics:** What provenance is and why citations matter; the spectrum of citation architectures (inline prompting, structured tool forcing, post-hoc attribution, agentic state provenance); the trade-off matrix; citations in the multi-agent project; UI and UX of citations; post-processing: verifying citations; connecting provenance to state machines.
- **Build:** structured-output citations with a verifier that checks each claim against retrieved spans.

### U14.15 Multi-agent architecture summary, error handling and best practices
**Sources:** GEN 11.8
- **Topics:** Summary of the multi-agent architecture and the DevOps agent journey; project implementation steps; inter-agent error handling; system prompts; key takeaways of multi-agent orchestration strategy; summary and best practices.
- **Build:** the D14 integrated project (see U17.4).

## D15. Evaluation, Safety and Responsible AI

Aim: measuring LLM systems rigorously, then the threat landscape (attacks, jailbreaks, privacy, legal risk) and defenses. All attacks are studied only in local or disposable setups against models and data the learner owns (Master Rules 11.1). Benchmarks (recalled, not checked unless noted): Jurafsky–Martin *SLP3* (confirmed: interpretability); Zou et al. (GCG), Chao et al. (PAIR), Carlini et al. on extraction and membership inference, Zheng et al. on LLM-as-a-judge.

### U15.1 LLM evaluation: metric architecture and reference-based metrics
**Sources:** GEN 7.3, 12.1, 12.2; FDL W12
- **Topics:** LLM evaluation: the metric architecture; common metrics; ways to compute metric scores (statistical scorers, model-based scorers); why evaluate LLMs; the setup, the ideal scenario and its limitations; the coefficient of agreement; reference-based metrics: precision and recall (the foundations); ROUGE (recall-oriented n-gram overlap, with code); BLEU (precision-based n-gram scoring, with code); METEOR (F-score with stems and synonyms, with code); BERTScore (semantic similarity, with code); comparison: when to use which, and limitations; benchmarking and evaluation of LLMs.
- **Results:** BLEU brevity penalty and modified n-gram precision [D]; ROUGE-N/L definitions [Def]; Cohen's kappa [D].
- **Build:** ROUGE, BLEU, METEOR-style and BERTScore-style scorers from scratch, checked against reference libraries; inter-annotator agreement.
- **Gap-fills:** *[inferred: SLP3 Ch.13]* human evaluation design, confidence intervals for metrics, benchmark contamination.

### U15.2 LLM-as-a-judge and factuality
**Sources:** GEN 12.3
- **Topics:** LLM-as-a-judge: overview and main variations; the original and revised workflows; typical dimensions to evaluate; factuality: focus and quantification.
- **Results:** Position and verbosity bias of judges and calibration against human labels [S].
- **Build:** pairwise and rubric judges with position-swap debiasing and agreement with human labels.

### U15.3 AI safety foundations and threat models
**Sources:** GEN 12.4, 12.5, 12.6
- **Topics:** AI safety foundations: early security (information security), trustworthy ML, AI safety for LLMs, threat models; attacks on models: membership inference, model extraction, model poisoning, model hijacking, adversarial attacks; risks of GenAI: data privacy risks, jailbreak risks, legal and IP risks.
- **Results:** Membership-inference advantage and its link to overfitting [D]; extraction cost via query complexity [S].
- **Build:** a membership-inference test on a model the learner trained; adversarial examples (FGSM) on a small CNN.

### U15.4 White-box attacks and prompt injection
**Sources:** GEN 12.7
- **Topics:** White-box attacks: Greedy Coordinate Gradient (method and results); indirect prompt injection; prompt leakage.
- **Build:** a GCG-style discrete optimization against a small open model in a disposable sandbox, measuring attack success and transfer.

### U15.5 Black-box attacks and the jailbreak taxonomy
**Sources:** GEN 12.8, 12.9
- **Topics:** Black-box attacks: model weakness, categories of responses and overall results; context contamination; DeepWordBug; instruction-centric prompts (TechHazardQA); Prompt Automatic Iterative Refinement (PAIR) and its results; jailbreak taxonomy: language strategies, rhetoric techniques, imaginary words, LLM operational exploitation.
- **Build:** measurement harness (attack success rate by category) against a locally hosted model, with no harmful payloads stored.

### U15.6 Defense, interpretability and ethics
**Sources:** GEN 12.10; DLNLP W12; FDL W5
- **Topics:** Defense: red teaming versus blue teaming and the summary; analysis and interpretability of language models; ethical considerations; explainability as a safety tool.
- **Build:** a red-team/blue-team exercise on the learner's own RAG agent, producing a defect list and fixes.


# PART E. SYSTEMS AND INTEGRATION

## D16. ML Systems, Efficiency and Distributed and Federated Learning

Aim: how neural networks, LLMs and graph networks actually run: accelerators, parallelism, memory, serving, compression, fault tolerance and federated training. Benchmarks: Sze–Chen–Yang–Emer, *Efficient Processing of Deep Neural Networks* (listed reference) with research articles shared in the lectures; Boyd et al., Nedić (distributed optimization); Hennessy–Patterson (recalled, not checked).

### U16.1 CNN computation and accelerators
**Sources:** CSO W1–3,10–12, o
- **Topics:** Basics of convolutional neural network (CNN) computations; CNN accelerators 1 and 2; ML accelerators with emerging technologies; workload characterization of ML algorithms; introduction to neural processing units (NPUs); computing kernels of training and inference and how they can be efficiently computed; edge versus cloud execution.
- **Results:** Roofline model and arithmetic intensity of convolution and matmul [D]; dataflow classes (weight-, output-, row-stationary) and data-reuse counts [D].
- **Build:** loop-nest convolution with tiling in NumPy/C and a roofline plot from measured throughput.

### U16.2 Parallelism for training, communication and fault tolerance
**Sources:** CSO W4,8; DOML W10
- **Topics:** Parallelism for training large ML models (data, tensor, pipeline parallelism); fault tolerance in ML training (checkpointing, recovery); introduction to neural networks and the ring-allreduce algorithm.
- **Results:** Ring-allreduce bandwidth cost 2(p−1)/p·n [D]; pipeline bubble fraction [D]; Young's checkpoint-interval approximation [D].
- **Build:** ring-allreduce simulator; data-parallel SGD across processes with PyTorch DDP.

### U16.3 LLM decoding, memory management and serving infrastructure
**Sources:** CSO W5–7, o; MFGAI W11
- **Topics:** Basics of large language models; accelerated decoding and memory management of LLMs (KV cache, paged attention, speculative decoding, batching); LLM serving infrastructure (scheduling, continuous batching, queueing); LLMs: models, sampling, inference and quantization methods (inference part).
- **Results:** KV-cache memory per sequence 2·L·H·d_head·T·b bytes (layers L, heads H, head size d_head, tokens T, bytes per value b) [D]; memory-bound decoding throughput bound [D]; M/M/c queue intuition for serving (link to U5.8) [D].
- **Build:** a KV-cache decoder and a continuous-batching scheduler simulator; measure tokens/s versus batch size.

### U16.4 Model compression and quantization
**Sources:** FDL W12; MFGAI W11; CSO o
- **Topics:** Model compression (pruning, distillation, low-rank factorization); quantization methods (post-training and quantization-aware; INT8/INT4; NormalFloat as used by QLoRA); system optimization techniques for CNNs, LLMs and graph neural networks.
- **Results:** Quantization error bounds and scale/zero-point derivation [D]; distillation loss with temperature [D].
- **Build:** uniform and per-channel quantization, magnitude pruning and logit distillation from scratch.

### U16.5 Graph neural network inference systems
**Sources:** CSO W9, o
- **Topics:** System optimization for graph neural network (GNN) inference; sparse versus dense kernels; neighbourhood sampling; large language models, CNNs and GNNs as the three kernels studied.
- **Build:** message-passing GCN layer from scratch with sparse matrix multiply and a sampling baseline.
- **Gap-fills:** *[inferred: Hamilton, Graph Representation Learning, recalled, not checked]* GCN, GraphSAGE and attention-based GNN layers (link to U1.4 and U4.8).

### U16.6 Federated learning
**Sources:** DOML W11–12
- **Topics:** Introduction to federated learning; data heterogeneity in federated learning; computational heterogeneity in federated learning; robustness in federated learning.
- **Results:** FedAvg client drift under non-IID data [S]; Byzantine-robust aggregation (median, Krum) guarantees [S].
- **Build:** FedAvg simulation with non-IID partitions and a robust aggregator against a poisoning client.
- **Gap-fills:** *[inferred: McMahan et al., recalled, not checked]* differential privacy and secure aggregation (stated; link to U15.3).

## D17. Integration and Capstones

Aim: each stretch of the course closes with one integrated, learner-built deliverable defended end to end (Master Rules 9.6). The tutor reviews and questions; the learner writes everything (Master Rules 9.4). **Acceptance criteria common to every capstone (written before work starts, Master Rules 9.3):** required behaviour with automated tests; one number predicted, then measured; one injected failure detected and recovered from; cost estimated, then read from the actual bill (local labs: zero); a threat model; a decision record for each major choice (the judgment turn, Master Rules 10.4); a clean teardown; an oral defence against adversarial questions. A capstone never replaces unit-by-unit mastery; domain exit audits (Master Rules 8.7) run first.

### U17.1 Capstone A: the mathematics of machine learning, end to end
**Sources:** none (integration unit; assembles earlier units)
- **Topics:** Closes D1–D8. A qualifying-examination-level unseen problem set (at least one proof or derivation and one computational problem per domain, key written first) plus a small reproduction: implement PCA via SVD, ridge/lasso regression, logistic regression by Newton/IRLS, SGD with momentum and Adam, an SVM dual solver and a simple LP/QP solver, each checked against a hand computation and against the professional library.
- **Predict then measure:** the number of Newton iterations to convergence and the condition number of the Hessian; the SGD error floor for a given step size.
- **Injected failure:** an ill-conditioned design matrix; diagnose by SVD and fix by regularization.
- **Defence:** derive the SVD-based PCA, the KKT conditions of the SVM and the convergence rate of gradient descent on a quadratic.

### U17.2 Capstone B: a classical-ML library from scratch
**Sources:** none (integration unit; assembles earlier units)
- **Topics:** Closes D9–D10. A NumPy library (kNN, naive Bayes, CART and random forest, AdaBoost and gradient boosting, kernel SVM, k-means, GMM-EM, PCA, HMM, UCB and Thompson-sampling bandits, tabular Q-learning) with a uniform fit/predict interface, a benchmark harness against scikit-learn on at least five datasets, and a written learning-theory note (PAC/VC bound versus observed generalization gap).
- **Predict then measure:** test-accuracy gap versus scikit-learn for each algorithm; regret slope of UCB versus Thompson sampling.
- **Injected failure:** label noise and covariate shift; detect with the evaluation tools of U9.2.

### U17.3 Capstone C: a deep-learning framework from scratch
**Sources:** none (integration unit; assembles earlier units)
- **Topics:** Closes D11. A reverse-mode autodiff engine with Linear, Conv2d, RNN/LSTM, LayerNorm, Dropout, attention layers; SGD/Adam; a gradient checker; training an MLP, a CNN, an LSTM and a small Transformer on real data; every layer's gradient verified against PyTorch to 1e-5; explanation maps (U11.5) on the CNN.
- **Predict then measure:** parameter counts, FLOPs and the training loss at step 100.
- **Injected failure:** exploding gradients in the LSTM; fix with clipping and initialization changes.

### U17.4 Capstone D: an LLM application platform (RAG + agents + safety)
**Sources:** none (integration unit; assembles earlier units)
- **Topics:** Closes D12, D14 and D15. A grounded multi-agent support/DevOps assistant: ingestion and chunking, hybrid retrieval with reranking, query routing, planner–executor agents in a state machine with human-in-the-loop, episodic and semantic memory, citations with a verifier, semantic caching, observability, an evaluation harness (retrieval metrics, RAGAS-style faithfulness, LLM-as-judge with debiasing) and a red-team/blue-team report covering prompt injection, indirect injection and leakage.
- **Predict then measure:** recall@k, answer faithfulness, p95 latency and cost per request.
- **Injected failure:** poisoned document in the corpus; detect with provenance checks and contain with least-privilege tools.
- **Cost tag:** live API calls only after recorded-response replay and under a spend cap (Master Rules 11.2).

### U17.5 Capstone E: generative models
**Sources:** none (integration unit; assembles earlier units)
- **Topics:** Closes D13. Small-scale GAN (WGAN-GP), VAE/VQ-VAE and DDPM with classifier-free guidance on the same dataset, compared by sample quality (FID proxy), likelihood bound, sampling cost and failure modes (mode collapse, posterior collapse, sampling slowness).
- **Predict then measure:** ELBO versus bits per dimension; sampling steps versus quality curve.
- **Injected failure:** mode collapse in the GAN; diagnose and apply gradient penalty.

### U17.6 Capstone F: ML systems and efficiency
**Sources:** none (integration unit; assembles earlier units)
- **Topics:** Closes D16. Serve a small Transformer with a KV cache, continuous batching and quantization; load-test with a Poisson arrival process against the M/M/c prediction of U5.8; simulate data-parallel training with ring-allreduce and checkpoint recovery; run a federated-averaging experiment with non-IID clients and one malicious client.
- **Predict then measure:** tokens/s versus batch size, memory per request and queueing delay at 70% utilization.
- **Injected failure:** a worker crash mid-training; recover from checkpoint and quantify lost work.

### U17.7 Final integrated capstone: train, align, compress, serve, evaluate and secure a small language model
**Sources:** none (integration unit; assembles earlier units)
- **Topics:** Closes the whole course and assembles parts the learner built in every earlier capstone: pretrain a tiny decoder-only Transformer from scratch (U12.3, U17.3), align it with SFT plus DPO/PPO (U12.8, U10.5), adapt it with LoRA (U12.9), quantize and serve it (U16.3, U16.4), put it behind the RAG-agent platform (U17.4), and evaluate and red-team the full system (U15.1–U15.6). Defended as a professional design review with a decision record for each major choice.
- **Predict then measure:** perplexity versus scaling-law prediction (U12.5); win-rate against the base model; end-to-end latency and cost; attack success rate before and after defenses.
- **Injected failure:** reward hacking in the preference stage or a jailbreak that bypasses the system prompt; detect, patch and re-test.


---

# APPENDICES

## Appendix A. Source course index

| Key | Course | Instructor / institution (course id) | Source lines in `nptel.txt` | Cells |
|---|---|---|---|---|
| MFML | Mathematical Foundations for Machine Learning | Rao & Rajan, IISc/NITK (106108702) | 18–45 | 13 |
| MFGAI | Mathematical Foundations of Generative AI | Prathosh A P, IISc (106108004) | 70–93 | 13 |
| EMML | Essential Mathematics for Machine Learning | Gupta & Kumar, IIT Roorkee (111107137) | 124–144 | 13 |
| EM1 | Engineering Mathematics I | Jitendra Kumar, IIT Kharagpur (111105121) | 170–189 | 13 |
| EM2 | Engineering Mathematics II | Jitendra Kumar, IIT Kharagpur | 198 | 13 |
| MM | Mathematical Modelling: Analysis and Applications | Ameeya Kumar Nayak, IIT Roorkee | 201 | 5 |
| HEM | Higher Engineering Mathematics | P. N. Agrawal, IIT Roorkee (2019) | 203 | 13 |
| IM | An Invitation to Mathematics | NPTEL video course | 205–206 | 2 |
| AEMK | Advanced Engineering Mathematics | Hari Shankar Mahato, IIT Kharagpur | 208–209 | 13 |
| DM | Discrete Mathematics (title not in source; inferred from content) | Nitin Saxena, IIT Kanpur | 211 | 13 |
| AEMA | Advanced Engineering Mathematics | P. N. Agarwal, IIT Roorkee (111107119) | 232–252 | 13 |
| OMLH | Optimisation for Machine Learning: Theory and Implementation (Hindi) | Pravesh Biyani, IIIT Delhi | 265–286 | 9 |
| CVX | Convex Optimization | Joydeep Dutta, IIT Kanpur | 290–362 | 6 |
| AOW | Applied Optimization for Wireless, Machine Learning, Big Data | Aditya K. Jagannatham, IIT Kanpur | 390–426 | 13 |
| OAT | Optimization Algorithms: Theory and Software Implementation | D. Thirumulanathan, IIT Kanpur | 440–455 | 13 |
| PMO | A Primer to Mathematical Optimization | Debdas Ghosh, IIT (BHU) (111104165) | 474–497 | 13 |
| OFF | Optimization from Fundamentals | Ankur A. Kulkarni, IIT Bombay | 513–530 | 13 |
| CSO | Computer System Optimizations for ML | Sumit K. Mandal, IISc (106108003) | 550–573 | 13 |
| DOML | Distributed Optimization and Machine Learning | Mayank Baranwal, IIT Bombay (106101466) | 595–618 | 13 |
| BAN | Bandit Algorithm (Online Machine Learning) | Manjesh Kumar Hanawal, IIT Bombay (110101145) | 640–663 | 13 |
| MLCE | Machine Learning for Core Engineering Disciplines | Ananth Govind Rajan, IISc (127108778) | 686–707 | 13 |
| ALAJ | Applied Linear Algebra for Signal Processing, Data Analytics and ML | Aditya K. Jagannatham, IIT Kanpur (108104174) | 729–757 | 13 |
| MLDL | Machine Learning and Deep Learning - Fundamentals and Applications | M. K. Bhuyan, IIT Guwahati (108103192) | 779–802 | 13 |
| MLK | Machine Learning (ML) | Carl Gustaf Jansson, KTH | 823–839 | 9 |
| MLE | Machine Learning for Engineering (title not in source) | Balaji Srinivasan & Ganapathy Krishnamurthi, IIT Madras | 854–880 | 13 |
| MLESA | Machine Learning for Engineering and Science Applications | Balaraman Ravindran, IIT Madras | 894–916 | 14 |
| FML | Foundations of Machine Learning | J. Saketha Nath, IIT Hyderabad (106106001) | 937–960 | 13 |
| IMLK | Introduction to Machine Learning (IITKGP) | Sudeshna Sarkar, IIT Kharagpur (106105152) | 985–1002 | 9 |
| SMLM | Statistical and Machine Learning Methods: Basics and Applications | Rajib Maity, IIT Kharagpur (105105001) | 1025–1048 | 13 |
| S50 | 50 Statistical Techniques an AI Engineer Needs to Know (learner list, 9 of 50 categories present) | learner-supplied list | 1058–1125 | 9 |
| DMIN | Data Mining | Pabitra Mitra, IIT Kharagpur | 1134–1149 | 9 |
| FDL | Foundations of Deep Learning: Concepts and Applications | Multifaculty (AICTE) | 1174–1262 | 13 |
| DLNLP | Deep Learning for Natural Language Processing | Pawan Goyal, IIT Kharagpur (108105572) | 1280–1303 | 13 |
| CAL1 | Calculus of One Real Variable | Joydeep Dutta, IIT Kanpur (109104124) | 1325–1340 | 9 |
| ALAB | Advanced Linear Algebra | Premananda Bera, IIT Roorkee | 1352–1399 | 5 |
| ALAK | Applied Linear Algebra in AI and ML | Swanand Khare, IIT Kharagpur | 1408–1446 | 13 |
| LAP | Linear Algebra | Dilip P. Patil, IIT Bombay (111108098) | 1465–1486 | 13 |
| LAR | Basic Linear Algebra | I. K. Rana, IIT Bombay | 1503–1513 | 9 |
| LPCS | Linear Programming and its Applications to Computer Science | Rajat Mittal, IIT Kanpur (106104356) | 1531–1549 | 9 |
| PSS | Preparatory Probability and Statistics (title not in source) | G. Srinivasan, IIT Madras | 1562–1570 | 5 |
| IPS | Introduction to Probability and Statistics | Somesh Kumar, IIT Kharagpur | 1600–1689 | 13 |
| GEN | Generative AI: Topics and Chapter Structure (12 chapters, 78 sections) | `iit-genai.md` | 1–505 | 78 |

## Appendix B. Coverage matrix: every source cell and the units that teach it

Each entry is `cell → units`. A cell may feed several units because one source week often spans several topics (for example, MFML Week 10 spans matrix calculus, optimization, least squares and PCA).

**MFML** (Mathematical Foundations for Machine Learning): o → U4.1, U5.1, U8.14; W1 → U4.1, U4.2; W2 → U4.3, U4.6; W3 → U4.4, U4.8; W4 → U4.9, U9.5, U9.8; W5 → U5.1; W6 → U5.2; W7 → U5.6; W8 → U5.6, U5.7, U6.4; W9 → U2.4, U3.1, U3.2; W10 → U3.5, U4.10, U8.1, U8.5, U8.7, U8.8, U8.10, U9.8; W11 → U11.1, U11.2; W12 → U9.1

**MFGAI** (Mathematical Foundations of Generative AI): o → U12.2, U12.4, U13.1, U13.3, U13.5, U13.7; W1 → U13.1; W2 → U13.2; W3 → U13.3; W4 → U13.3; W5 → U13.4; W6 → U13.4; W7 → U13.7; W8 → U13.7; W9 → U13.6, U13.7; W10 → U12.4, U13.5; W11 → U12.6, U16.3, U16.4; W12 → U10.5, U12.8

**EMML** (Essential Mathematics for Machine Learning): o → U4.1, U8.1, U8.12; W1 → U4.1, U4.2; W2 → U4.3, U4.4, U4.6; W3 → U4.8, U4.9, U9.8; W4 → U9.8; W5 → U4.10, U9.3; W6 → U4.4, U4.7, U4.9, U4.11, U9.2; W7 → U3.1, U3.5; W8 → U3.5, U8.1, U8.2, U8.3; W9 → U8.1, U8.8; W10 → U5.1, U5.2, U8.1, U8.8; W11 → U5.2, U5.3, U5.4, U5.6, U8.7, U9.5; W12 → U8.5, U8.6, U9.5

**EM1** (Engineering Mathematics I): o → U2.2, U2.3, U2.4, U2.5, U3.1, U3.2, U3.3, U4.1, U4.2, U4.3, U4.6, U7.1; W1 → U2.2; W2 → U3.1; W3 → U3.1; W4 → U3.2; W5 → U2.5; W6 → U3.3; W7 → U3.3; W8 → U4.1, U4.2; W9 → U4.3; W10 → U4.6; W11 → U7.1; W12 → U7.1

**EM2** (Engineering Mathematics II): o → U3.4, U7.2, U7.3, U7.4, U7.5; W1 → U3.4; W2 → U3.4; W3 → U7.3; W4 → U7.3, U7.4; W5 → U7.2; W6 → U7.2; W7 → U7.5; W8 → U7.5; W9 → U7.5; W10 → U7.5; W11 → U7.5; W12 → U7.5

**MM** (Mathematical Modelling: Analysis and Applications): o → U7.6; W1 → U7.6; W2 → U7.6; W3 → U7.1, U7.6; W4 → U7.6

**HEM** (Higher Engineering Mathematics): o → U1.1, U5.8, U8.7; W1 → U1.1; W2 → U1.1, U1.3; W3 → U1.3; W4 → U1.3; W5 → U1.3, U1.4; W6 → U1.4; W7 → U1.4; W8 → U1.4; W9 → U8.7; W10 → U8.7; W11 → U5.8; W12 → U5.8

**IM** (An Invitation to Mathematics): o → U1.1, U1.7; A → U1.2, U1.5, U1.7

**AEMK** (Advanced Engineering Mathematics): o → U3.1; W1 → U2.2, U2.4, U3.1, U3.2; W2 → U2.3, U2.5, U3.3; W3 → U7.1; W4 → U7.2; W5 → U7.2; W6 → U4.1, U4.2, U4.3; W7 → U4.1; W8 → U4.6, U4.8; W9 → U3.4; W10 → U3.4; W11 → U3.4; W12 → U7.3, U7.4

**DM** (Discrete Mathematics (title not in source; inferred from content)): o → U1.1; W1 → U1.1; W2 → U1.2; W3 → U1.2; W4 → U1.3; W5 → U1.4; W6 → U1.4; W7 → U1.4; W8 → U1.5; W9 → U1.5; W10 → U1.6; W11 → U1.6; W12 → U1.6

**AEMA** (Advanced Engineering Mathematics): o → U5.1, U5.6, U5.8, U6.3, U7.3, U7.4, U7.5; W1 → U7.3; W2 → U7.3; W3 → U7.3, U7.4; W4 → U7.4; W5 → U7.4; W6 → U7.4; W7 → U7.4, U7.5; W8 → U7.5; W9 → U5.1, U5.3, U7.5; W10 → U5.3, U5.4; W11 → U5.4, U5.6, U6.4; W12 → U5.8, U6.3, U6.4

**OMLH** (Optimisation for Machine Learning: Theory and Implementation (Hindi)): o → U8.1; W1 → U3.1, U4.2, U4.8, U4.9; W2 → U3.1, U4.2, U4.8, U4.9; W3 → U8.1, U8.3, U8.4; W4 → U8.8; W5 → U8.9, U8.10; W6 → U8.9, U8.10; W7 → U8.8, U8.10; W8 → U8.8, U8.10

**CVX** (Convex Optimization): o → U8.1, U8.2, U8.5, U8.6, U8.7, U8.11, U8.13; L1-9 → U8.2, U8.3; L10-19 → U8.3, U8.5, U8.6, U8.7; L20-26 → U8.4, U8.7; L27-33 → U8.7; L34-40 → U8.11, U8.13

**AOW** (Applied Optimization for Wireless, Machine Learning, Big Data): o → U8.11, U8.12; W1 → U4.4, U4.8, U5.6; W2 → U8.2, U8.12; W3 → U8.3, U8.12; W4 → U8.7, U8.11, U8.12; W5 → U8.11, U8.12; W6 → U8.5, U8.6, U8.11, U8.12; W7 → U8.12; W8 → U8.12; W9 → U8.11, U8.12; W10 → U8.12; W11 → U8.12; W12 → U8.12

**OAT** (Optimization Algorithms: Theory and Software Implementation): o → U8.1; W1 → U8.1; W2 → U8.1; W3 → U8.1, U8.8; W4 → U8.8; W5 → U8.8; W6 → U8.8; W7 → U8.9; W8 → U8.9; W9 → U8.7; W10 → U8.7; W11 → U8.7; W12 → U8.10

**PMO** (A Primer to Mathematical Optimization): o → U8.1; W1 → U2.1, U3.1, U4.2, U4.3, U4.4, U4.8, U4.9, U8.1; W2 → U2.1, U2.2, U2.4, U3.1; W3 → U8.2, U8.3; W4 → U8.3, U8.4; W5 → U8.4, U8.8; W6 → U8.8; W7 → U8.8; W8 → U8.5, U8.8; W9 → U8.5; W10 → U8.6; W11 → U8.9; W12 → U8.9

**OFF** (Optimization from Fundamentals): o → U8.1, U8.15; W1 → U2.1, U8.1; W2 → U8.1, U8.4; W3 → U8.1, U8.4; W4 → U8.1, U8.2; W5 → U8.7; W6 → U8.6, U8.7; W7 → U8.6, U8.7; W8 → U8.15; W9 → U8.15; W10 → U8.8, U8.9; W11 → U8.8, U8.9; W12 → U8.15, U10.4

**CSO** (Computer System Optimizations for ML): o → U16.1, U16.3, U16.4, U16.5; W1 → U11.4, U16.1; W2 → U16.1; W3 → U16.1; W4 → U16.2; W5 → U12.5, U16.3; W6 → U16.3; W7 → U16.3; W8 → U16.2; W9 → U16.5; W10 → U16.1; W11 → U16.1; W12 → U16.1

**DOML** (Distributed Optimization and Machine Learning): o → U8.14; W1 → U8.2, U8.3, U8.14; W2 → U8.3, U8.5, U8.6; W3 → U8.5, U8.6, U8.8, U8.10; W4 → U8.10; W5 → U8.10; W6 → U8.9, U8.10; W7 → U8.6, U8.14; W8 → U5.8, U8.14; W9 → U8.14; W10 → U8.14, U16.2; W11 → U16.6; W12 → U16.6

**BAN** (Bandit Algorithm (Online Machine Learning)): o → U10.1, U10.2, U10.3; W1 → U10.1; W2 → U10.1; W3 → U10.1; W4 → U10.1; W5 → U10.2; W6 → U5.7, U10.2; W7 → U10.2; W8 → U10.2; W9 → U10.3; W10 → U10.3; W11 → U10.3; W12 → U10.3

**MLCE** (Machine Learning for Core Engineering Disciplines): o → U9.1, U9.2, U9.3; W1 → U6.1, U9.1; W2 → U5.6, U6.4, U9.3; W3 → U9.2, U9.3, U9.4; W4 → U8.12, U9.3; W5 → U8.10; W6 → U9.2; W7 → U9.8, U9.9; W8 → U9.7, U9.8, U9.9, U11.8; W9 → U9.5, U9.7; W10 → U9.5, U9.7, U9.10; W11 → U11.1, U11.2, U11.4; W12 → U11.4, U11.7

**ALAJ** (Applied Linear Algebra for Signal Processing, Data Analytics and ML): o → U4.11; W1 → U4.2, U4.4; W2 → U4.11; W3 → U4.6, U4.11; W4 → U4.9, U4.11; W5 → U4.10, U9.5; W6 → U4.10; W7 → U4.11, U9.11; W8 → U4.11, U7.5; W9 → U4.11; W10 → U4.11, U9.9; W11 → U4.11, U9.5; W12 → U4.11, U5.8

**MLDL** (Machine Learning and Deep Learning - Fundamentals and Applications): o → U9.1; W1 → U9.1, U9.2, U9.3, U9.4; W2 → U9.6, U9.10; W3 → U9.6; W4 → U9.5; W5 → U9.3, U9.7, U9.10; W6 → U9.7; W7 → U9.8; W8 → U9.9; W9 → U9.9; W10 → U11.1, U11.2; W11 → U11.4; W12 → U11.6, U11.7, U11.8, U13.3

**MLK** (Machine Learning (ML)): o → U9.1, U9.14, U10.4; W1 → U9.1; W2 → U9.1; W3 → U9.1; W4 → U9.6, U9.7, U9.14; W5 → U9.14; W6 → U9.14, U11.1, U11.7; W7 → U9.14; W8 → U9.14

**MLE** (Machine Learning for Engineering (title not in source)): o → U9.1, U9.8, U9.13; W1 → U4.1, U9.1; W2 → U5.1, U9.1; W3 → U8.1, U9.1; W4 → U6.5, U9.2, U9.3, U9.4; W5 → U11.1, U11.2; W6 → U11.4; W7 → U11.4; W8 → U11.7; W9 → U9.5, U9.6, U9.7; W10 → U9.9; W11 → U6.5, U9.10, U13.1, U13.6; W12 → U11.8, U13.3, U13.4

**MLESA** (Machine Learning for Engineering and Science Applications): o → U9.1; W0 → U4.1, U5.1, U8.1, U8.3, U8.11; W1 → U9.1, U9.2; W2 → U6.4, U9.3, U9.4, U9.8; W3 → U9.3, U9.6; W4 → U9.5; W5 → U6.5, U8.10, U9.6, U9.10, U11.1, U11.2, U11.3; W6 → U9.7; W7 → U9.2, U9.7; W8 → U9.6, U9.7, U9.10; W9 → U9.10; W10 → U9.9; W11 → U9.9; W12 → U9.13, U10.4

**FML** (Foundations of Machine Learning): o → U9.1, U13.1; W1 → U9.1, U9.13; W2 → U9.3; W3 → U9.3, U9.13; W4 → U8.8, U8.10; W5 → U8.10, U9.13; W6 → U9.4; W7 → U9.5; W8 → U9.5, U9.13; W9 → U9.13, U11.1, U12.3; W10 → U9.13, U11.2; W11 → U9.10, U13.1, U13.6; W12 → U9.6, U9.7, U9.10, U9.13

**IMLK** (Introduction to Machine Learning (IITKGP)): o → U9.1, U9.13; W1 → U9.1, U9.2; W2 → U9.3, U9.7; W3 → U9.8, U9.11; W4 → U9.6; W5 → U9.3, U9.5; W6 → U11.1; W7 → U9.7, U9.13; W8 → U9.9

**SMLM** (Statistical and Machine Learning Methods: Basics and Applications): o → U6.1, U6.5, U6.6; W1 → U6.1, U6.6; W2 → U5.1, U5.2; W3 → U5.3, U5.4; W4 → U5.6; W5 → U5.6; W6 → U6.4, U9.3; W7 → U6.4, U9.8; W8 → U9.1, U9.2; W9 → U9.1, U11.1; W10 → U9.7; W11 → U9.5, U9.9, U11.1; W12 → U6.6

**S50** (50 Statistical Techniques an AI Engineer Needs to Know (learner list, 9 of 50 categories present)): D1 → U5.2, U6.1; D2 → U5.1, U5.6; D3 → U5.2, U5.3, U5.4; D4 → U5.7, U6.2, U6.3; D5 → U6.3; D6 → U5.6, U6.4; D7 → U6.4, U9.3; D8 → U6.5; D9 → U6.5

**DMIN** (Data Mining): o → U9.1, U9.12; W1 → U9.1, U9.8, U9.12; W2 → U9.12; W3 → U9.6, U9.7, U9.11; W4 → U9.5; W5 → U9.9, U9.12; W6 → U9.12; W7 → U9.2, U9.12; W8 → U9.12

**FDL** (Foundations of Deep Learning: Concepts and Applications): o → U11.1; W1 → U11.1; W2 → U8.10, U11.2, U11.3; W3 → U11.4; W4 → U11.4; W5 → U11.5, U15.6; W6 → U11.6; W7 → U11.7; W8 → U11.7; W9 → U12.1, U12.2; W10 → U11.8; W11 → U12.3, U12.4, U12.7, U12.9; W12 → U10.5, U12.4, U12.8, U13.3, U13.4, U13.7, U15.1, U16.4

**DLNLP** (Deep Learning for Natural Language Processing): o → U12.1, U12.4, U12.8; W1 → U12.1; W2 → U12.2; W3 → U12.2; W4 → U11.7; W5 → U12.3; W6 → U12.4; W7 → U12.4; W8 → U12.8; W9 → U12.5, U12.7; W10 → U12.9; W11 → U12.5, U14.1; W12 → U15.6

**CAL1** (Calculus of One Real Variable): o → U2.1; W1 → U2.1; W2 → U2.1; W3 → U2.2; W4 → U2.2, U2.3; W5 → U2.3; W6 → U2.3; W7 → U2.3, U2.4; W8 → U2.4

**ALAB** (Advanced Linear Algebra): o → U4.1, U4.3, U4.7, U4.8, U4.9; P1 → U4.1, U4.2, U4.3; P2 → U4.2, U4.3; P3 → U4.6, U4.7; P4 → U4.4, U4.8, U4.9

**ALAK** (Applied Linear Algebra in AI and ML): o → U4.8, U4.9, U4.10, U4.11; W1 → U4.2, U4.3, U4.4; W2 → U4.1, U4.9; W3 → U4.4, U4.9; W4 → U4.9; W5 → U4.10; W6 → U4.10; W7 → U4.10, U9.4; W8 → U4.8; W9 → U4.9; W10 → U4.11; W11 → U4.11; W12 → U4.9, U4.11

**LAP** (Linear Algebra): o → U4.2, U4.5, U4.6, U4.11; W1 → U4.2; W2 → U4.1, U4.2; W3 → U4.2; W4 → U4.2; W5 → U4.3; W6 → U4.3; W7 → U4.3; W8 → U4.3; W9 → U4.1; W10 → U4.5, U4.7; W11 → U4.5; W12 → U4.5

**LAR** (Basic Linear Algebra): o → U4.1; W1 → U4.1; W2 → U4.1; W3 → U4.1, U4.2; W4 → U4.1, U4.5; W5 → U4.3; W6 → U4.4; W7 → U4.6, U7.6; W8 → U4.6

**LPCS** (Linear Programming and its Applications to Computer Science): o → U8.2, U8.7; W1 → U8.2, U8.7; W2 → U8.2, U8.7; W3 → U8.2, U8.7; W4 → U8.2, U8.6; W5 → U8.2, U8.6; W6 → U8.6; W7 → U8.7; W8 → U8.7

**PSS** (Preparatory Probability and Statistics (title not in source)): o → U5.1, U6.1; W1 → U6.1; W2 → U6.1; W3 → U5.1; W4 → U5.2, U5.3, U5.4

**IPS** (Introduction to Probability and Statistics): o → U5.1, U5.2; W1 → U5.1; W2 → U5.1, U5.2; W3 → U5.2, U5.3; W4 → U5.3, U5.4; W5 → U5.4; W6 → U5.5, U5.6; W7 → U5.5, U5.6; W8 → U6.1, U6.2; W9 → U6.1, U6.2; W10 → U6.2, U6.3; W11 → U6.3; W12 → U6.3

**GEN** (GenAI course sections): 1.1 → U12.1; 1.2 → U12.1, U12.2; 1.3 → U12.1; 1.4 → U12.1; 1.5 → U12.1; 1.6 → U12.1; 1.7 → U12.1; 2.1 → U9.0; 2.2 → U9.0; 2.3 → U9.0; 2.4 → U9.0; 2.5 → U9.0; 2.6 → U9.0, U11.8; 2.7 → U11.1, U11.2; 2.8 → U11.3; 3.1 → U11.1; 3.2 → U11.1; 3.3 → U11.2, U11.3; 3.4 → U12.3; 4.1 → U12.3; 4.2 → U12.3; 4.3 → U12.3; 4.4 → U12.3; 4.5 → U12.3; 4.6 → U12.3; 4.7 → U12.3; 5.1 → U12.4, U12.8; 5.2 → U12.7; 5.3 → U12.6; 5.4 → U12.7; 6.1 → U12.7; 6.2 → U12.6; 6.3 → U12.7; 6.4 → U12.7; 7.1 → U12.10; 7.2 → U12.10; 7.3 → U15.1; 7.4 → U12.10; 7.5 → U12.10; 8.1 → U14.1; 8.2 → U14.1; 8.3 → U14.1; 8.4 → U14.2; 8.5 → U14.2; 8.6 → U14.2; 9.1 → U14.3; 9.2 → U14.3; 9.3 → U14.4; 9.4 → U14.4; 9.5 → U14.5; 9.6 → U14.5; 9.7 → U14.6; 10.1 → U14.6; 10.2 → U14.6; 10.3 → U14.7; 10.4 → U14.8; 10.5 → U14.8; 10.6 → U14.8; 10.7 → U14.8; 10.8 → U14.9; 11.1 → U14.9; 11.2 → U14.10; 11.3 → U14.10; 11.4 → U14.11; 11.5 → U14.12; 11.6 → U14.13; 11.7 → U14.14; 11.8 → U14.15; 12.1 → U15.1; 12.2 → U15.1; 12.3 → U15.2; 12.4 → U15.3; 12.5 → U15.3; 12.6 → U15.3; 12.7 → U15.4; 12.8 → U15.5; 12.9 → U15.5; 12.10 → U15.6

## Appendix C. Results inventory (Master Rules III.1.5)

Status key: **P** prove in full · **D** derive · **S** sketch · **X** stated, proof deferred · **Def** definition, not proved.

| Unit | Result | Status |
|---|---|---|
| U1.1 | Equivalence laws and duality principle | P |
| U1.1 | soundness of standard inference rules (modus ponens, resolution) | P |
| U1.1 | principle of mathematical induction and strong induction | P |
| U1.2 | Binomial theorem | P |
| U1.2 | pigeonhole principle and generalized form | P |
| U1.2 | inclusion–exclusion | P |
| U1.2 | solution of linear recurrences by characteristic roots and by generating functions | D |
| U1.2 | bijective proof of Vandermonde-type identities | P |
| U1.3 | Dilworth's theorem | P |
| U1.3 | Mirsky's theorem | P |
| U1.3 | Boolean algebra axioms imply duality and De Morgan laws | P |
| U1.3 | canonical (sum-of-products) form exists and is unique | P |
| U1.4 | Handshake lemma | P |
| U1.4 | Euler's circuit theorem | P |
| U1.4 | Euler's formula V−E+F=2 | P |
| U1.4 | Kuratowski's theorem | X→proof deferred, stated with the two obstruction graphs |
| U1.4 | five-colour theorem | P |
| U1.4 | four-colour theorem | X |
| U1.4 | Hall's marriage theorem | P |
| U1.4 | König's theorem | P |
| U1.4 | Menger / max-flow–min-cut | X→U8.6, proved there by LP duality |
| U1.5 | Euclid's algorithm and Bézout's identity | P |
| U1.5 | fundamental theorem of arithmetic | P |
| U1.5 | Chinese remainder theorem | P |
| U1.5 | Fermat's little theorem and Euler's theorem | P |
| U1.5 | infinitude of primes | P |
| U1.5 | Chebyshev-type density bounds | S |
| U1.5 | prime number theorem | X |
| U1.5 | correctness of RSA | P |
| U1.6 | Lagrange's theorem | P |
| U1.6 | existence and uniqueness of finite fields of order p^n | S |
| U1.6 | Hamming bound and distance of linear codes | P |
| U1.6 | orbit–stabilizer theorem | P |
| U1.6 | Burnside's lemma | P |
| U1.6 | first isomorphism theorem for groups | P |
| U1.7 | Lagrange interpolation uniqueness | P |
| U1.7 | intermediate value theorem | P in U2.2 |
| U1.7 | Vandermonde determinant | D |
| U1.7 | invariants as proof tool | P |
| U2.1 | Uncountability of the reals (diagonal argument) | P |
| U2.1 | completeness (least upper bound) | Def |
| U2.1 | intermediate value theorem | P |
| U2.1 | extreme value (maximum value) theorem | P |
| U2.1 | Bolzano–Weierstrass | P |
| U2.1 | Heine–Borel for Rn | S |
| U2.2 | Rolle and Lagrange mean value theorems | P |
| U2.2 | Cauchy mean value theorem | P |
| U2.2 | L'Hôpital's rule (indeterminate forms) | P |
| U2.2 | inverse function theorem in one variable | P |
| U2.2 | first and second derivative tests | P |
| U2.2 | local quadratic convergence of Newton's method | D |
| U2.3 | Fundamental theorem of calculus (both parts) | P |
| U2.3 | integrability of continuous functions | S |
| U2.3 | error bounds for trapezoid and Simpson rules | D |
| U2.3 | properties of exp and log from their integral definition | P |
| U2.4 | Taylor's theorem with Lagrange remainder | P |
| U2.4 | ratio, root and comparison tests | P |
| U2.4 | Abel/radius-of-convergence theorem (Cauchy–Hadamard) | P |
| U2.4 | Rearrangement of conditionally convergent series (Riemann) | S |
| U2.5 | Comparison and limit-comparison tests for improper integrals | P |
| U2.5 | Γ(n+1)=nΓ(n) and the Beta–Gamma relation | P |
| U2.5 | Leibniz rule | P under uniform-convergence conditions |
| U3.1 | Equality of mixed partials (Schwarz/Clairaut) | P |
| U3.1 | chain rule in several variables | P |
| U3.1 | differentiability implies directional derivatives and continuity, with the converse counterexamples | P |
| U3.1 | implicit function theorem | S, proof sketch via contraction mapping |
| U3.1 | Euler's homogeneous function theorem | P |
| U3.2 | Second-order Taylor expansion with remainder | P |
| U3.2 | second-derivative test via Hessian definiteness | P |
| U3.2 | Lagrange multiplier rule for equality constraints | D |
| U3.2 | KKT conditions | X→U8.5 |
| U3.3 | Fubini's theorem | S, statement and conditions |
| U3.3 | change-of-variables formula with Jacobian determinant | S; derived for linear maps in U4.5 |
| U3.3 | polar/spherical coordinates | D |
| U3.4 | Green's theorem | P for simple regions |
| U3.4 | divergence (Gauss) theorem | S |
| U3.4 | Stokes' theorem | S |
| U3.4 | conservative-field criterion | P |
| U3.4 | Frenet–Serret equations | D |
| U3.5 | Gradients of trace, quadratic form and log-determinant | D |
| U3.5 | chain rule in matrix form for a two-layer network | D |
| U4.1 | Row operations preserve solution set | P |
| U4.1 | rank = row rank = column rank | P |
| U4.1 | solvability criterion rank(A)=rank([A/b]) | P |
| U4.1 | uniqueness of reduced row echelon form | P |
| U4.1 | an n×n matrix is invertible iff rank n iff det≠0 | P |
| U4.2 | Steinitz exchange lemma | P |
| U4.2 | any two bases have equal cardinality (dimension well defined) | P |
| U4.2 | existence of a basis in finite-dimensional spaces | P |
| U4.2 | dimension formula dim(U+W)=dim U+dim W−dim(U∩W) | P |
| U4.3 | Rank–nullity theorem | P |
| U4.3 | a linear map is determined by its action on a basis | P |
| U4.3 | isomorphism theorem for vector spaces | P |
| U4.3 | V ≅ V** for finite dimension | P |
| U4.3 | matrix of composite is product of matrices | P |
| U4.3 | change-of-basis formula | D |
| U4.4 | Cauchy–Schwarz and triangle inequalities | P |
| U4.4 | Gram–Schmidt produces an orthonormal basis | P |
| U4.4 | orthogonal projection onto a subspace is the best approximation (Pythagoras) | P |
| U4.4 | V = W ⊕ W^⊥ | P |
| U4.4 | projection matrix P = A(AᵀA)⁻¹Aᵀ | D |
| U4.4 | equivalence of norms on Rn | S |
| U4.5 | Existence and uniqueness of an alternating n-linear form with det(I)=1 | P |
| U4.5 | det(AB)=det A·det B | P |
| U4.5 | adjoint–determinant theorem A·adj(A)=det(A)·I | P |
| U4.5 | /det A/ is the volume scaling factor | D |
| U4.5 | Cramer's rule | P |
| U4.6 | Eigenvectors for distinct eigenvalues are independent | P |
| U4.6 | diagonalizability criterion (geometric = algebraic multiplicity) | P |
| U4.6 | similar matrices share characteristic polynomial | P |
| U4.6 | trace = sum and det = product of eigenvalues | P |
| U4.6 | Cayley–Hamilton | P in U4.7 |
| U4.7 | Cayley–Hamilton theorem | P |
| U4.7 | minimal polynomial divides every annihilating polynomial | P |
| U4.7 | triangulability over algebraically closed fields | P |
| U4.7 | primary decomposition theorem | P |
| U4.7 | existence and uniqueness of Jordan form | S |
| U4.7 | rational canonical form | X, proof beyond course scope, stated |
| U4.8 | Spectral theorem for real symmetric / Hermitian matrices | P |
| U4.8 | spectral theorem for normal operators | P |
| U4.8 | Sylvester's criterion | P |
| U4.8 | PSD ⇔ nonnegative eigenvalues ⇔ Gram form | P |
| U4.8 | Mercer-type statement for kernel matrices | S, used in U9.5 |
| U4.9 | Existence of SVD | P |
| U4.9 | Eckart–Young–Mirsky low-rank optimality | P |
| U4.9 | cond(A)=σmax/σmin and error amplification bound | D |
| U4.9 | Moore–Penrose pseudo-inverse via SVD, four defining equations | P |
| U4.9 | polar decomposition | P |
| U4.10 | Normal equations characterize the minimizer | P |
| U4.10 | solution via QR and via SVD | D |
| U4.10 | Gauss–Markov (BLUE) | P in U6.4 |
| U4.10 | ridge solution and its SVD shrinkage form | D |
| U4.10 | KKT system for equality-constrained least squares | D |
| U4.11 | Perron–Frobenius for positive matrices | S |
| U4.11 | convergence of the power method and PageRank damping | D |
| U4.11 | stationary distribution of an irreducible aperiodic chain | P in U5.8 |
| U4.11 | DFT matrix is unitary and diagonalizes circulants | P |
| U5.1 | Continuity of probability along monotone sequences | P |
| U5.1 | inclusion–exclusion for events | P |
| U5.1 | law of total probability | P |
| U5.1 | Bayes' theorem | P |
| U5.1 | Borel–Cantelli lemmas | P |
| U5.1 | π–λ / monotone class uniqueness theorem | S |
| U5.2 | Properties of the CDF and its characterization | P |
| U5.2 | linearity of expectation | P |
| U5.2 | variance identity Var X = E[X²] − (E X)² | P |
| U5.2 | Jensen's inequality | P |
| U5.2 | moment generating function determines moments | S |
| U5.3 | Poisson as the limit of binomial | P |
| U5.3 | memorylessness of the geometric and exponential laws | P |
| U5.3 | Poisson process: counts are Poisson and inter-arrivals exponential | D |
| U5.3 | mean and variance of each standard law | D |
| U5.4 | Normal density integrates to one | P |
| U5.4 | closure of the normal under affine maps and sums of independent normals | P |
| U5.4 | exponential is the only memoryless continuous law | P |
| U5.4 | relationship among Gamma, chi-square and exponential | P |
| U5.5 | Density of Y=g(X) by change of variables | D |
| U5.5 | sum of independent variables by convolution | P |
| U5.5 | joint law of order statistics | D |
| U5.5 | Jacobian formula for multivariate transformations | S |
| U5.6 | Law of iterated expectation and law of total variance | P |
| U5.6 | covariance matrix is symmetric PSD | P |
| U5.6 | conditional of a multivariate normal is normal with explicit mean and covariance | D |
| U5.6 | Sklar's theorem | X |
| U5.6 | correlation = 0 implies independence only for jointly normal | P |
| U5.7 | Markov and Chebyshev inequalities | P |
| U5.7 | weak law of large numbers | P |
| U5.7 | strong law of large numbers | S |
| U5.7 | central limit theorem (via characteristic functions) | P |
| U5.7 | Hoeffding and Chernoff bounds | P |
| U5.7 | sub-Gaussian tail bounds | P |
| U5.8 | Stationary distribution of M/M/1 | D |
| U5.8 | Little's law | P |
| U5.8 | Erlang-C formula for M/M/s | D |
| U5.8 | existence and convergence of stationary distribution for finite irreducible aperiodic chains | P |
| U6.1 | Sample mean minimizes squared deviation and median minimizes absolute deviation | P |
| U6.1 | Chebyshev-type bounds for samples | P |
| U6.2 | Distribution of the sample mean and variance for normal samples (Cochran/Student) | P |
| U6.2 | MLE invariance and asymptotic normality | D / S |
| U6.2 | Rao–Blackwell theorem | P |
| U6.2 | Lehmann–Scheffé | S |
| U6.2 | Cramér–Rao bound | P |
| U6.3 | Neyman–Pearson lemma | P |
| U6.3 | duality of confidence intervals and tests | P |
| U6.3 | distribution of the t statistic | P |
| U6.3 | likelihood-ratio test and Wilks' theorem | S |
| U6.4 | Gauss–Markov theorem | P |
| U6.4 | distribution of OLS estimates under normal errors | D |
| U6.4 | R² and adjusted R² | D |
| U6.4 | ANOVA F-test decomposition | P |
| U6.5 | Posterior ∝ likelihood × prior | P |
| U6.5 | conjugacy of Beta–Binomial and Normal–Normal | D |
| U6.5 | correctness (detailed balance) of Metropolis–Hastings | P |
| U6.5 | Gibbs sampler as a special case | P |
| U6.6 | Stationarity and the Box–Jenkins identification logic for ARMA models | D |
| U6.6 | forecast error decomposition | D |
| U7.1 | Existence and uniqueness (Picard–Lindelöf) | S |
| U7.1 | solution of linear constant-coefficient ODEs by characteristic equation | P |
| U7.1 | superposition and Wronskian | P |
| U7.1 | variation of parameters | D |
| U7.2 | Convergence of Jacobi/Gauss–Seidel for diagonally dominant matrices | P |
| U7.2 | contraction mapping and fixed-point convergence | P |
| U7.2 | interpolation error formula | D |
| U7.2 | composite Simpson error | D |
| U7.3 | Cauchy–Riemann necessary and sufficient conditions | P |
| U7.3 | Cauchy's theorem (Goursat) | S |
| U7.3 | Cauchy integral formula and derivative formula | P |
| U7.3 | Liouville and fundamental theorem of algebra | P |
| U7.3 | maximum modulus | P |
| U7.4 | Laurent expansion existence and uniqueness | P |
| U7.4 | residue theorem | P |
| U7.4 | argument principle and Rouché | P |
| U7.4 | Möbius transformations map circles to circles | P |
| U7.4 | Riemann mapping theorem | X |
| U7.5 | Convolution theorem for Laplace and Fourier | P |
| U7.5 | Dirichlet convergence theorem for Fourier series | S |
| U7.5 | Parseval/Plancherel | P |
| U7.5 | inversion formula for Z and Laplace transform by residues | D |
| U7.5 | FFT divide-and-conquer recurrence | D |
| U7.6 | Stability of a linear difference system by eigenvalue modulus | P |
| U7.6 | Jury criterion | S |
| U7.6 | period-doubling route to chaos in the logistic map (observed and explained) | S |
| U7.6 | Hartman–Grobman linearization | X |
| U7.6 | Lyapunov stability of a fixed point | P in U8.10 |
| U8.1 | Fermat's necessary condition for interior extrema | P |
| U8.1 | Weierstrass existence theorem | P in U8.4 |
| U8.1 | equivalent reformulations (epigraph form, slack variables, change of variables) preserve optimal values | P |
| U8.2 | Separating hyperplane theorem (point and closed convex set) | P |
| U8.2 | supporting hyperplane theorem | P |
| U8.2 | Farkas' lemma | P |
| U8.2 | Gordan's theorem | P |
| U8.2 | Carathéodory's theorem | P |
| U8.2 | Minkowski/Krein–Milman for polytopes | S |
| U8.3 | Jensen's inequality | P |
| U8.3 | first-order condition f(y) ≥ f(x)+∇f(x)ᵀ(y−x) | P |
| U8.3 | Hessian PSD ⇔ convex | P |
| U8.3 | convex functions are locally Lipschitz in the interior | P |
| U8.3 | subdifferential is nonempty, convex and compact in the interior | P |
| U8.3 | Fenchel–Moreau (statement) | X |
| U8.3 | strong convexity ⇒ unique minimizer and quadratic growth | P |
| U8.4 | First-order necessary condition | P |
| U8.4 | second-order necessary and sufficient conditions | P |
| U8.4 | for convex f, stationary ⇒ global minimum | P |
| U8.4 | coercive continuous functions attain their minimum | P |
| U8.5 | Lagrange multiplier theorem | P under regularity |
| U8.5 | Fritz John conditions | P |
| U8.5 | KKT necessary conditions under LICQ/MFCQ | P |
| U8.5 | KKT sufficient for convex problems | P |
| U8.5 | Slater's condition | P in U8.6 |
| U8.6 | Weak duality | P |
| U8.6 | strong duality under Slater | P |
| U8.6 | LP strong duality | P |
| U8.6 | complementary slackness | P |
| U8.6 | Von Neumann minimax theorem | P |
| U8.6 | Nash existence for finite two-player zero-sum games | P |
| U8.6 | max-flow = min-cut | P |
| U8.7 | Fundamental theorem of LP (optimum at a vertex) | P |
| U8.7 | simplex terminates under Bland's rule | P |
| U8.7 | strong duality and complementary slackness | P |
| U8.7 | polynomial-time convergence of short-step path-following | S |
| U8.7 | integrality gap of LP relaxation of set cover and rounding bound | P |
| U8.7 | ℓ1 and ℓ∞ regression as LPs | D |
| U8.8 | Convergence of gradient descent for L-smooth convex functions at rate O(1/k) and for strongly convex at linear rate | P |
| U8.8 | Zoutendijk condition | P |
| U8.8 | local quadratic convergence of Newton | P |
| U8.8 | superlinear convergence of BFGS | S |
| U8.8 | CG finds the minimizer of an n-dimensional quadratic in ≤ n steps | P |
| U8.8 | Armijo backtracking terminates | P |
| U8.9 | Exterior penalty solutions converge to a constrained minimizer as the penalty grows | P |
| U8.9 | augmented Lagrangian avoids ill-conditioning and converges with bounded penalty | S |
| U8.9 | SQP as Newton on the KKT system | D |
| U8.9 | active-set termination for convex QP | S |
| U8.10 | SGD convergence for convex and strongly convex objectives with variance bound | P |
| U8.10 | Nesterov's O(1/k²) rate and its optimality | S |
| U8.10 | Lyapunov function for gradient flow gives exponential convergence for strongly convex f | P |
| U8.10 | proximal gradient converges at O(1/k) | P |
| U8.10 | Adam update as adaptive preconditioning (no general convergence guarantee, counterexample) | S |
| U8.11 | Every LP, QP, QCQP and SOCP is an SDP-representable convex program | P |
| U8.11 | Schur-complement representation of quadratic constraints | P |
| U8.11 | GP becomes convex under log transformation | P |
| U8.11 | SDP strong duality under strict feasibility | S |
| U8.12 | LASSO yields sparse solutions (subgradient optimality) | D |
| U8.12 | restricted-isometry sufficient condition for exact recovery (statement) | X |
| U8.12 | water-filling is the KKT solution of capacity maximization | D |
| U8.12 | Markowitz mean–variance solution | D |
| U8.13 | Optimality 0 ∈ ∂f(x) | P |
| U8.13 | subgradient method convergence rate | P |
| U8.13 | DC algorithm (DCA) monotone descent | P |
| U8.14 | ADMM convergence for convex problems | S |
| U8.14 | consensus convergence rate governed by the second-smallest Laplacian eigenvalue | P |
| U8.14 | dual decomposition for separable problems | D |
| U8.14 | distributed gradient descent converges to a neighbourhood with constant steps | S |
| U8.15 | Bellman's principle of optimality | P |
| U8.15 | finite-horizon dynamic programming recursion | P |
| U8.15 | KKT conditions as a complementarity problem | D |
| U9.0 | Confusion-matrix identities for accuracy, precision, recall and F1 | D |
| U9.0 | sparsity of one-hot vectors makes all distinct words orthogonal | P |
| U9.1 | Bayes optimal classifier minimizes 0–1 risk | P |
| U9.1 | Bayes optimal regressor is the conditional mean under squared loss | P |
| U9.1 | ERM decomposition into estimation and approximation error | D |
| U9.1 | no-free-lunch theorem | S |
| U9.2 | Bias–variance decomposition of expected squared error | D |
| U9.2 | leave-one-out cross-validation estimator formula for linear smoothers | D |
| U9.2 | AUC equals the probability that a positive outranks a negative | P |
| U9.3 | OLS = MLE under Gaussian noise | D |
| U9.3 | logistic regression log-likelihood is concave, gradient and Hessian | D |
| U9.3 | softmax cross-entropy gradient is (p−y) | D |
| U9.3 | estimation error bound for linear least squares | P |
| U9.3 | surrogate-loss consistency (hinge, logistic) | S |
| U9.4 | Ridge shrinkage in the SVD basis | D |
| U9.4 | lasso soft-thresholding solution for orthonormal design | D |
| U9.4 | gradient descent from zero converges to the min-norm interpolant for under-determined least squares | P |
| U9.4 | constrained and penalized forms are equivalent (Lagrangian) | P |
| U9.5 | Perceptron convergence theorem (mistake bound) | P |
| U9.5 | SVM primal–dual derivation and support vectors | D |
| U9.5 | representer theorem | P |
| U9.5 | Mercer's theorem | X |
| U9.5 | universal kernel ⇒ Bayes consistency (statement and sketch) | S |
| U9.6 | Discriminant functions of Gaussian class-conditionals are quadratic (linear for shared covariance) | D |
| U9.6 | naive Bayes factorization and Laplace smoothing | D |
| U9.6 | kNN asymptotic error ≤ 2× Bayes error (Cover–Hart) | S |
| U9.6 | Parzen estimator bias–variance | D |
| U9.7 | Information gain and Gini impurity as concave impurity measures | D |
| U9.7 | bagging variance reduction for correlated estimators | D |
| U9.7 | AdaBoost training-error bound | P |
| U9.7 | gradient boosting as functional gradient descent | D |
| U9.8 | PCA as top-k eigenvectors of the covariance matrix (variance maximization) | P |
| U9.8 | PCA equals best rank-k reconstruction (Eckart–Young) | P in U4.9 |
| U9.8 | Fisher's criterion for LDA | D |
| U9.8 | t-SNE gradient | D |
| U9.8 | linear autoencoder spans the PCA subspace | P |
| U9.9 | k-means monotonically decreases its objective and converges to a local minimum | P |
| U9.9 | EM never decreases the likelihood | P |
| U9.9 | k-means as the hard-assignment limit of spherical GMM | D |
| U9.9 | Jensen-based ELBO derivation of EM | D |
| U9.10 | d-separation and the factorization theorem | S |
| U9.10 | forward–backward and Viterbi algorithms | D |
| U9.10 | belief propagation is exact on trees | P |
| U9.10 | GP posterior mean and variance | D |
| U9.11 | Matrix-factorization objective and ALS updates | D |
| U9.11 | curse of dimensionality for distance-based methods | P |
| U9.12 | Apriori anti-monotonicity (downward closure) | P |
| U9.12 | FP-growth correctness | S |
| U9.12 | support, confidence and lift | Def |
| U9.13 | PAC bound for finite hypothesis classes | P |
| U9.13 | VC-dimension generalization bound | S |
| U9.13 | Sauer–Shelah lemma | P |
| U9.13 | Rademacher-complexity bound | S |
| U9.13 | benign overfitting / double descent for min-norm interpolation | S |
| U9.14 | Version-space convergence | P |
| U9.14 | ID3 entropy criterion | D |
| U9.14 | inductive-bias characterization of learners | P |
| U10.1 | Halving mistake bound log₂/H/ | P |
| U10.1 | weighted-majority/Hedge regret O(√(T ln N)) | P |
| U10.1 | Exp3 regret O(√(TK ln K)) | P |
| U10.1 | adversarial lower bound Ω(√(TK)) | S |
| U10.2 | UCB logarithmic regret bound | P |
| U10.2 | KL-UCB asymptotic optimality | S |
| U10.2 | Lai–Robbins instance-dependent lower bound | S |
| U10.2 | minimax lower bound via change of measure | S |
| U10.3 | LinUCB regret bound | S |
| U10.3 | sample complexity of LUCB | S |
| U10.3 | lower bound for best-arm identification | S |
| U10.4 | Bellman optimality equation | D |
| U10.4 | contraction of the Bellman operator and convergence of value iteration | P |
| U10.4 | policy-improvement theorem | P |
| U10.4 | Q-learning convergence (statement) | X |
| U10.5 | Policy-gradient theorem | D |
| U10.5 | baseline invariance | P |
| U10.5 | monotonic-improvement bound motivating TRPO/PPO | S |
| U10.5 | PPO clipped objective | D |
| U11.1 | Single-layer perceptron cannot represent XOR | P |
| U11.1 | universal approximation theorem for one hidden layer | S |
| U11.1 | depth–width separation examples | S |
| U11.2 | Backpropagation computes the exact gradient in O(forward cost) | D |
| U11.2 | vanishing/exploding gradient bounds for deep chains | D |
| U11.2 | Xavier/He initialization variance derivation | D |
| U11.3 | Dropout as an ensemble/approximate Bayesian average | S |
| U11.3 | L2 regularization equals weight decay for SGD | P |
| U11.3 | early stopping as implicit L2 for quadratic loss | D |
| U11.4 | Convolution as a linear, translation-equivariant operator | P |
| U11.4 | output-size and parameter-count formulae | D |
| U11.4 | ResNet identity mapping eases optimization (gradient path) | D |
| U11.4 | backpropagation through convolution is a correlation | D |
| U11.5 | Shapley value axioms and uniqueness | P |
| U11.5 | Grad-CAM as gradient-weighted activation map | D |
| U11.5 | LIME as local linear surrogate | D |
| U11.6 | Intersection-over-union and non-maximum suppression | Def |
| U11.6 | anchor/region-proposal losses | D |
| U11.7 | Gradient of BPTT as a product of Jacobians | D |
| U11.7 | vanishing/exploding conditions via spectral radius | D |
| U11.7 | LSTM cell-state additive path | D |
| U11.8 | Linear autoencoder with MSE recovers the PCA subspace | P |
| U11.8 | sparse/denoising/contractive objectives | D |
| U12.1 | Chain rule for language-model probability | P |
| U12.1 | maximum-likelihood n-gram estimates and smoothing (add-k, Kneser–Ney idea) | D |
| U12.1 | perplexity as exponentiated cross-entropy | D |
| U12.1 | TF-IDF weighting rationale | D |
| U12.2 | Skip-gram with negative sampling implicitly factorizes a shifted PMI matrix | S |
| U12.2 | GloVe objective | D |
| U12.3 | Scaled dot-product attention with 1/√d_k scaling stabilizes softmax variance | D |
| U12.3 | permutation equivariance of self-attention without positions | P |
| U12.3 | parameter and FLOP count of a Transformer block | D |
| U12.3 | causal mask makes training parallel but generation sequential | P |
| U12.4 | Masked-LM and causal-LM objectives as conditional likelihoods | D |
| U12.4 | cross-entropy loss per token and perplexity | D |
| U12.4 | next-sentence and denoising objectives compared | P |
| U12.5 | Power-law loss versus compute, parameters and data (Kaplan/Chinchilla form) | X, empirical law: fitted, not proved |
| U12.5 | compute-optimal allocation | D from the fitted law |
| U12.6 | Temperature as softmax scaling and its entropy limits | D |
| U12.6 | top-p truncation as adaptive support | P |
| U12.6 | beam search is not exact search | P |
| U12.7 | Self-consistency as marginalization over reasoning paths | D |
| U12.7 | why chain-of-thought helps (extra serial computation) | S |
| U12.8 | Bradley–Terry reward-model likelihood | D |
| U12.8 | KL-regularized RLHF objective and its closed-form optimal policy | D |
| U12.8 | DPO loss derived from that closed form | D |
| U12.8 | PPO clipped objective (see U10.5) | D |
| U12.9 | Low-rank update ΔW = BA parameter count and rank bound | D |
| U12.9 | QLoRA 4-bit NormalFloat plus paged optimizers (stated) | X→U16.4 |
| U12.10 | Prompt search as discrete black-box optimization (objective, search space, evaluation noise) | Def |
| U12.10 | mode collapse from preference tuning | S |
| U13.1 | MLE equals minimizing KL(p_data‖p_θ) | D |
| U13.1 | the partition function makes EBM likelihood intractable | P |
| U13.1 | importance sampling and its variance | D |
| U13.2 | Variational lower bound on an f-divergence via the Fenchel conjugate | D |
| U13.2 | JS divergence recovers the original GAN objective | D |
| U13.3 | Optimal discriminator D*(x)=p_data/(p_data+p_g) | D |
| U13.3 | the generator objective equals 2·JS(p_data‖p_g) − log 4 at D* | D |
| U13.3 | Kantorovich–Rubinstein duality | S |
| U13.3 | Wasserstein distance remains informative for disjoint supports | P |
| U13.4 | ELBO = reconstruction − KL(q‖p) and the gap equals KL(q‖posterior) | D |
| U13.4 | reparameterization gives low-variance pathwise gradients | D |
| U13.4 | closed-form KL between Gaussians | D |
| U13.5 | Exact likelihood by chain rule | P |
| U13.5 | exposure bias and teacher forcing | S |
| U13.6 | Gradient of the log-likelihood of an EBM is a difference of expectations | D |
| U13.6 | Langevin dynamics targets p(x) | S |
| U13.6 | denoising score matching equals score of the noised distribution | D |
| U13.7 | Closed-form forward marginal q(x_t/x₀) | D |
| U13.7 | reverse-process posterior mean | D |
| U13.7 | ELBO simplifies to a denoising regression loss | D |
| U13.7 | DDIM as a deterministic reverse process | D |
| U13.7 | SDE/probability-flow correspondence | S |
| U13.8 | Change-of-variables formula for densities | D |
| U13.8 | determinant of a triangular Jacobian is the product of its diagonal | P |
| U13.8 | log-likelihood of a flow | D |
| U14.1 | TF-IDF and BM25 scoring formulas and saturation of term frequency | D |
| U14.1 | inverted-index query processing | D |
| U14.2 | Decomposition of end-to-end RAG error into retrieval recall and generation faithfulness | D |
| U14.3 | Cosine similarity versus dot product versus Euclidean distance and when they coincide | P |
| U14.4 | InfoNCE/contrastive loss with in-batch negatives | D |
| U14.4 | Matryoshka loss as a multi-prefix objective | D |
| U14.6 | Memory and distance-computation cost of IVF, PQ and IVF-PQ | D |
| U14.6 | HNSW expected search complexity (small-world argument) | S |
| U14.6 | recall–latency trade-off curves | Def |
| U14.7 | Latency/cost model of two-stage retrieve-then-rerank | D |
| U14.7 | MaxSim late-interaction scoring | Def |
| U14.8 | Semantic-cache hit-rate versus threshold and error trade-off | D |
| U14.12 | Graph termination conditions and loop bounds | D |
| U15.1 | BLEU brevity penalty and modified n-gram precision | D |
| U15.1 | ROUGE-N/L definitions | Def |
| U15.1 | Cohen's kappa | D |
| U15.2 | Position and verbosity bias of judges and calibration against human labels | S |
| U15.3 | Membership-inference advantage and its link to overfitting | D |
| U15.3 | extraction cost via query complexity | S |
| U16.1 | Roofline model and arithmetic intensity of convolution and matmul | D |
| U16.1 | dataflow classes (weight-, output-, row-stationary) and data-reuse counts | D |
| U16.2 | Ring-allreduce bandwidth cost 2(p−1)/p·n | D |
| U16.2 | pipeline bubble fraction | D |
| U16.2 | Young's checkpoint-interval approximation | D |
| U16.3 | KV-cache memory per sequence 2·L·H·d_head·T·b bytes (layers L, heads H, head size d_head, tokens T, bytes per value b) | D |
| U16.3 | memory-bound decoding throughput bound | D |
| U16.3 | M/M/c queue intuition for serving (link to U5.8) | D |
| U16.4 | Quantization error bounds and scale/zero-point derivation | D |
| U16.4 | distillation loss with temperature | D |
| U16.6 | FedAvg client drift under non-IID data | S |
| U16.6 | Byzantine-robust aggregation (median, Krum) guarantees | S |

478 results listed. A deferred result (**X**) is never presented as proved; the unit that will prove it is named in the entry or a later unit's list.

## Appendix D. Prerequisite map (Master Rules III.1.6)

### D.1 Prerequisite claims made by the sources (to verify, not trust)

Generated from each source's own prerequisite lines; each is rewritten below as concrete topics and probed when reached (Master Rules 3.3).


| Course | Prerequisite line(s) in the source |
|---|---|
| MFML | Basic Mathematics at school and undergraduate level |
| MFGAI | Prerequisites Probability, Course in Machine Learning |
| EM2 | prerequisite: Engineering Mathematics I |
| OMLH | PRE-REQUISITES : Linear Algebra, Basic Calculus, Basic Programming courses |
| CVX | Pre-requisites: Knowledge in Linear Algebra & RealAnalysis Hyperlinks: |
| AOW | PRE-REQUISITES : Basic knowledge of - Calculus, Probability, Matrices |
| OAT | PRE-REQUISITES : A basic knowledge on optimization theory is expected Foundations of Optimization - https://nptel.ac.in/courses/111104071 |
| PMO | Calculus, Linear Algebra, Coordinate Geometry |
| CSO | Computer Organization |
| DOML | A background in convex optimization and differential equations is preferred |
| BAN | PREREQUISITES : Basics of Probability Theory and Optimization |
| MLDL | Knowledge of Linear Algebra, Probability and Random Process, PDE will be helpful. |
| MLK | PRE-REQUISITES : Basic knowledge in Computer science and applied Mathematics |
| MLE | PREREQUISITES: Familiarity with Multivariable Calculus, Linear Algebra, Probability, Statistics. Comfortable with basic programming. |
| MLESA | PRE-REQUISITES: We will assume that the students know programming for some of the assignments.If the students have done introductory courses on probability theory and linear algebra it would be helpful. We will review some of the basic topics in the first two  |
| FML | Anyone with a good understanding of basic engineering math is eligible. Especially subjects like linear algebra, probability theory, and optimization. |
| IMLK | Basic programming skills (in Python), algorithm design, basics of probability &amp; statisticsINDUSTRY SUPPORT : Data science companies and many other industries value machine learning skills. |
| SMLM | Basic Knowledge of Probability and Statistics |
| FDL | This course is designed to be self-contained and suitable for learners with no prior background in the subject. However, a basic familiarity with Python programming is recommended to facilitate better understanding of the concepts and hands-on components of th |
| DLNLP | Participants should have done a course on MachineLearning, and should know basics of PythonProgramming |
| CAL1 | First year engineering, science and economics students with mathematics as main course.Prerequisites : Basic mathematics till 12th standard |
| ALAB | PRE-REQUISITES : Linear Algebra B.Sc /BE I/II year |
| ALAK | PRE-REQUISITES : Senior undergraduate and post graduate students from CSE, EE, ECE, AI, Maths INTENDED AUDIENCE : First course in Engineering Mathematics with some exposure to linear algebra |
| LAP | PREREQUISITES : Language of Set Theory; Elementary Algebra and Calculus |
| LAR | PREREQUISITES : Core INDUSTRY SUPPORT : Basic mathematics at school level undergraduate level |
| LPCS | Linear algebraBasic Linear Algebra - https://nptel.ac.in/courses/111101115Linear Algebra - https://nptel.ac.in/courses/111104137https://nptel.ac.in/courses/111106135 |
| IPS | PRE-REQUISITES: Must have good knowledge of Differential and Integral Calculus, sequences and series, Basic Linear/ Matrix Algebra (usually students who have completed Mathematics-I and II at first year undergraduate |

### D.2 Prerequisite chain to L0, as concrete topics

| Prerequisite (concrete) | First needed in | Depth needed | How probed |
|---|---|---|---|
| Algebra, functions, graphs, trigonometry, exponents and logarithms | U2.1 | L2 | Mixed unseen set of 6 items, first 10 minutes of U2.1 |
| Sets, relations, functions; basic logic | U1.1 | L2 | Prediction on a quantifier negation |
| Proof by induction, contradiction, contrapositive | U1.1 | L3 | Prove an unseen identity; taught first if shaky |
| Limits and continuity (ε–δ) | U2.1 | L3 | Prove a limit |
| Derivative rules, chain rule | U2.2 | L2 | Differentiate an unseen composite |
| Integration techniques | U2.3 | L2 | Evaluate an unseen integral |
| Series convergence tests | U2.4 | L3 | Decide convergence of an unseen series with a reason |
| Partial derivatives, gradient | U3.1 | L3 | Compute a gradient and check it numerically |
| Vectors, dot product, geometry of R² and R³ | U4.2 | L2 | Projection of one vector on another |
| Matrix multiplication, elimination | U4.1 | L2 | Solve a 3×3 system by hand |
| Eigenvalues and diagonalization | U4.6 | L3 | Diagonalize an unseen 3×3 matrix |
| Counting (permutations, combinations) | U5.1 | L2 | Unseen counting problem |
| Probability axioms, conditional probability | U5.1 | L3 | Unseen Bayes problem with a prediction |
| Expectation, variance, standard distributions | U5.2–U5.4 | L3 | Derive a mean and a variance |
| Covariance matrix, multivariate normal | U5.6 | L3 | Compute and interpret a conditional |
| Convexity and Jensen's inequality | U8.3 | L3 | Prove a function convex |
| Gradient descent as a loop | U8.8 | L2 | Predict the next iterate on a quadratic |
| Python programming (functions, classes, NumPy arrays, plotting) | U1.1 builds | L2 | First build; remedial Python taught on demand |
| Big-O and basic algorithms (sorting, search, graphs) | U1.4, U8.8 | L2 | Predict the cost of a loop nest |
| Floating-point arithmetic | U4.9 | L2 | Predict a rounding failure |
| Information theory (entropy, KL divergence) | U5.2, U9.9, U13.2 | L3 | Compute KL between two Bernoulli laws |
| Reinforcement-learning vocabulary | U10.4 | L2 | Describe an MDP |
| Computer organization (cache, memory hierarchy, parallelism) | U16.1 (source prerequisite of CSO) | L2 | Predict a cache-miss pattern; taught first if shaky |

**Remedial rule (Master Rules II.3):** school-level algebra, trigonometry and Python are remedial and on demand: a short probe locates a gap, the matching area is taught, and the learner returns to the exact point they left.

## Appendix E. Validation against the listed books and references

Master Rules 1.6 and 1.7: benchmarks are named, never linked; contents "recalled, not checked" are labelled so. Checks were run on 2026-11-03.

### E.1 What was checked, and what it changed

| Reference (listed by) | How checked | Outcome |
|---|---|---|
| Jurafsky–Martin, *Speech and Language Processing*, 3rd ed. (DLNLP) | **Checked**: 26 chapter titles read from the authors' site | Ch. 2–12 and 14 map to U12.1–U12.10, U11.7, U14.1–U14.12, U15.6. **Not covered by any source:** speech (Ch. 15–17), machine translation (Ch. 13), and classical linguistic structure (Ch. 18–26: sequence labelling, parsing, information extraction, semantic roles, coreference, discourse, conversation). Listed as a gap candidate in E.3, pending your agreement. |
| Deisenroth–Faisal–Ong, *Mathematics for Machine Learning* (MFML) | **Checked**: 12 chapter titles from the publisher and the book site | All 12 chapters map: Ch. 2 → U4.1–U4.2; Ch. 3 → U4.4; Ch. 4 → U4.6–U4.9; Ch. 5 → U3.1–U3.5; Ch. 6 → D5; Ch. 7 → D8; Ch. 8 → U9.1–U9.2; Ch. 9 → U9.3; Ch. 10 → U9.8; Ch. 11 → U9.9; Ch. 12 → U9.5. Added: Cholesky, Rayleigh quotient, analytic-geometry topics, probabilistic PCA. |
| Boyd–Vandenberghe, *Convex Optimization* (DOML, CVX) | **Partly checked**: parts and chapters 1–8 confirmed from publisher contents; the algorithms part (unconstrained, equality-constrained, interior-point) is *recalled, not checked* | Theory → U8.2, U8.3, U8.6; applications (approximation and fitting, statistical estimation, geometric problems) → U4.10, U8.12; algorithms → U8.8, U8.7. Added: problem taxonomy, epigraph forms, SDP representability. |
| Bach, *Learning Theory from First Principles* (FML) | **Checked**: 15 chapter titles from the PDF | Ch. 2–12, 14, 15 map to U9.1, U9.3–U9.7, U9.13, U8.10, D10, U9.10. **Not in any outline:** Ch. 13 (structured prediction) → gap candidate E.3. |
| Lattimore–Szepesvári, *Bandit Algorithms* (BAN) | **Partly checked**: part structure and several chapter titles from the publisher | D10 covers the stochastic, adversarial, contextual and pure-exploration topics; added MOSS, Bayesian and non-stationary bandits, linear bandits, MDP bridge. Gap candidate: partial monitoring. |
| Goodfellow–Bengio–Courville, *Deep Learning* (MLDL) | **Partly checked**: part structure and chapter headings from the book site | Part I → D4, D5, D8, D9; Part II → D11; Part III: autoencoders → U11.8, structured probabilistic models and Monte Carlo → U9.10, U13.6, deep generative models → D13. Gap candidates: linear factor models, ICA, sparse coding, partition-function estimation, approximate inference. |
| Foster, *Generative Deep Learning*, 2nd ed. (MFGAI) | **Checked**: contents from the publisher | VAEs, GANs, autoregressive, EBMs, diffusion, Transformers map to D13 and U12.3. **Normalizing flows** appear in the book's description and in no outline: added as U13.8. Gap candidates: music generation, world models. |
| Murphy, *Probabilistic Machine Learning: An Introduction* (FML) | **Not verified**: the book site gives its contents only as an image and a PDF | Cited as *recalled, not checked* in D9 and D13. |
| Strang (LA, *Learning from Data*), Axler, Kay, Rosenthal, Johnson–Wichern, Nocedal–Wright, Bishop, Hastie et al., Alpaydin, Duda–Hart–Stork, Haykin, Nielsen, Bengio, Mitchell, Spivak, Thomas–Finney, Kreyszig, Piskunov, O'Neil, Cheney, Artin, Halmos, Herstein, Hoffman–Kunze, Jacobson, Greub, Chvátal, Dantzig–Thapa, Bazaraa et al., Bertsekas, Chong–Zak, Dennis–Schnabel, Sun–Yuan, Rockafellar, Hiriart-Urruty–Lemaréchal, Tikhomirov, Churchill–Brown, Ahlfors, Conway, Debnath–Bhatta, Jain–Iyengar, Miller–Freund, Mayer, Maity, Forsyth, Pradhan–Kumar, Rengaswamy–Suresh, Sze et al., Nedić | **Not verified** (no machine-readable contents reached) | Named as benchmarks and used to label gap-fills as *[inferred: …, recalled, not checked]*. They should be spot-checked against the physical books before a domain is closed (Master Rules 1.6). |

### E.2 Gap-fills added to the curriculum (inventory)

Generated from the units: every topic below is **inferred** from a reference, is not in any outline, and is taught like any other topic.


| Unit | Gap-fill (inferred, not in any outline) |
|---|---|
| U1.1 | *[inferred: Rosen]* direct proof, contrapositive, contradiction, cases, induction, strong induction, structural induction, well-ordering; sets, relations and functions as the common language; regular languages and context-free grammars as the bridge to formal-language theory (see language-theory track). |
| U1.2 | *[inferred: Concrete Mathematics; Lovász]* ordinary and exponential generating functions, partitions, Catalan numbers, Stirling numbers, derangements, double counting. |
| U1.3 | *[inferred: Rosen]* Hasse diagrams, Sperner's theorem, distributive and complemented lattices, Stone representation (statement). |
| U1.4 | *[inferred: West]* trees and spanning trees (Kruskal, Prim), shortest paths (Dijkstra), Dirac and Ore conditions, Ramsey's theorem, spectral graph theory (adjacency/Laplacian eigenvalues; link to U4.8 and to spectral clustering in U9.9). |
| U1.5 | *[inferred: Hardy–Wright; Rosen]* primality tests, Diffie–Hellman, discrete logarithm, hashing as modular arithmetic. |
| U1.6 | *[inferred: Artin; MacWilliams–Sloane]* cyclic groups, permutation groups (link to U4.5 signature of a permutation), quotient groups, BCH codes. |
| U1.7 | this unit is a conceptual bridge; each theme is taught again at depth in D2, D4 and D1.5. |
| U2.1 | *[inferred: Spivak; Cheney]* metric spaces and normed spaces (needed by D4 norms and D8), Cauchy sequences, completeness of Rn. |
| U2.2 | *[inferred: Thomas–Finney]* related rates and curve sketching as applied optimization problems. |
| U2.3 | *[inferred: Thomas–Finney]* partial fractions procedure and trigonometric substitutions; Riemann sums and the Riemann–Darboux definition. |
| U2.4 | *[inferred: Spivak]* uniform convergence of series (needed in D7 Fourier and complex analysis). |
| U2.5 | *[inferred: Kreyszig]* Gaussian integral (needed for D5 normal distribution). |
| U3.1 | *[inferred: MML Ch.5]* gradients of vector-valued functions, gradients of matrices, useful identities, automatic differentiation (forward and reverse mode). |
| U3.4 | *[inferred: Kreyszig]* Laplacian and harmonic functions (links to D7 complex analysis); divergence of vector fields as it reappears in D13 continuity and Fokker–Planck equations. |
| U3.5 | *[inferred: MML Ch.5; Petersen–Pedersen Matrix Cookbook]* gradients of the least-squares loss and softmax cross-entropy used in D9 and D11. |
| U4.1 | *[inferred: Strang Ch.1–3]* four fundamental subspaces, column picture versus row picture, block matrices and matrix multiplication as four equivalent views. |
| U4.2 | *[inferred: Axler Ch.1–2]* span, list length versus independence, infinite-dimensional examples (polynomials, sequences, function spaces) as motivation for D13. |
| U4.3 | *[inferred: Axler Ch.3]* invertibility and isomorphic vector spaces; linear transformations of the plane (rotation, shear, reflection) as pictures. |
| U4.4 | *[inferred: MML Ch.3]* analytic geometry: lengths, distances, angles, orthonormal bases, orthogonal projections, rotations; p-norms and the unit ball geometry (links to L1 sparsity in U9.4). |
| U4.5 | *[inferred: Strang Ch.5]* determinant as dilation factor (links to change of variables in U3.3 and normalizing flows in D13). |
| U4.6 | *[inferred: Strang Ch.6]* powers of a matrix, difference/differential equation solutions via eigen-decomposition (feeds D7 and D10). |
| U4.8 | *[inferred: MML Ch.4]* Cholesky decomposition, Rayleigh quotient and variational characterization of eigenvalues (needed for PCA in U9.7). |
| U4.9 | *[inferred: Trefethen–Bau; Strang Ch.7]* floating-point arithmetic, backward stability, Cholesky, randomized SVD (links to LoRA in U12.7). |
| U4.11 | *[inferred: Strang LfD]* low-rank matrix and tensor ideas that reappear in LoRA (U12.7) and compression (U16.4). |
| U5.1 | *[inferred: Rosenthal; Kay]* measure-theoretic probability space (Ω, F, P), conditional independence, probabilistic graphical models as "probability networks" (links to U9.9). |
| U5.2 | *[inferred: Kay; Rosenthal]* characteristic functions, expectation as Lebesgue integral, entropy and KL divergence (needed in D9, D13). |
| U5.3 | *[inferred: Kay]* Bernoulli trials and the multinomial as a model for categorical outputs (softmax in D11/D12). |
| U5.4 | *[inferred: Blitzstein–Hwang]* heavy tails, mixture distributions and the exponential family (needed for U9.9 and U6.5). |
| U5.6 | *[inferred: MML Ch.6; Johnson–Wichern]* Gaussian marginalization and conditioning, change of variables for densities, sample geometry (n-dimensional view of centred data). |
| U5.7 | *[inferred: Lattimore–Szepesvári Ch.5]* Cramér–Chernoff method, sub-Gaussian and sub-exponential variables, martingales and Azuma–Hoeffding. |
| U5.8 | *[inferred: Kay Part II]* random processes, stationarity, Poisson and Gaussian processes; random walks (linking to U13 diffusion). |
| U6.1 | *[inferred: Johnson–Wichern Ch.1]* outlier detection, standardization, graphical displays of multivariate data. |
| U6.2 | *[inferred: Casella–Berger]* Fisher information, factorization theorem for sufficiency, bootstrap. |
| U6.3 | *[inferred: S50]* multiple testing (Bonferroni, Benjamini–Hochberg), effect sizes. |
| U6.4 | *[inferred: Johnson–Wichern]* factor analysis, canonical correlation, MANOVA, Hotelling's T². |
| U6.5 | *[inferred: Murphy PML Ch.3–4; Bishop]* credible intervals, posterior predictive, Hamiltonian Monte Carlo (statement), variational inference (link to D13 VAE). |
| U6.6 | *[inferred: Maity, Statistical Methods in Hydrology and Hydroclimatology; Forsyth, Applied Machine Learning]* extreme-value analysis and frequency analysis of hydrologic series, copula-based joint modelling (links to U5.6). |
| U7.1 | *[inferred: Kreyszig Ch.1–2]* method of undetermined coefficients, power-series solutions, systems of ODEs (feeds U7.6 and gradient flow in U8.10). |
| U7.2 | *[inferred: Burden–Faires]* Runge's phenomenon, Chebyshev nodes, Gaussian quadrature. |
| U7.5 | *[inferred: Kreyszig]* Fourier transforms as a view of attention/positional encodings (link to U12.2) and of convolution (link to U11.5). |
| U7.6 | *[source gap: the source lists only 4 of 12 course weeks; remaining weeks added from benchmarks]* *[inferred: Murray; Strogatz]* Hopf bifurcation, limit cycles, SIR epidemic models, reaction–diffusion models, parameter estimation for models (links to D9). |
| U8.1 | *[inferred: Boyd Ch.1; Tikhomirov]* taxonomy of problem classes (LP, QP, QCQP, SOCP, SDP, GP, integer), local versus global minima, optimization over open sets and manifolds (Lagrange multipliers on surfaces). |
| U8.7 | *[inferred: Chvátal; Dantzig–Thapa]* degeneracy and cycling, network simplex, transportation and assignment problems, total unimodularity. |
| U8.8 | *[inferred: Nocedal–Wright Ch.3–7; Dennis–Schnabel]* Wolfe-condition line-search algorithms, limited-memory BFGS, nonlinear least squares (Gauss–Newton), derivative-free methods. |
| U8.9 | *[inferred: Nocedal–Wright Ch.16–18; Bertsekas]* filter methods and merit functions, barrier methods (link to U8.7 IPM). |
| U8.10 | *[inferred: Bach LTFP Ch.5; Goodfellow Ch.8]* learning-rate schedules, mini-batching and variance reduction (SVRG), second-order and natural-gradient ideas. |
| U8.14 | *[inferred: Nedić, Distributed Optimization Over Networks; Boyd et al., ADMM monograph]* push-sum and directed graphs, gradient tracking, asynchronous updates. |
| U8.15 | *[inferred: Bertsekas, Dynamic Programming and Optimal Control]* linear–quadratic regulator, Pontryagin principle (statement), calculus of variations. |
| U9.1 | *[inferred: Mitchell Ch.1–2; Bach Ch.2; Murphy]* concept learning, version spaces, the formal learning problem (inputs, targets, loss, risk), data cleaning and feature scaling. |
| U9.2 | *[inferred: ESL Ch.7]* optimism and AIC/BIC, nested cross-validation, calibration, statistical comparison of classifiers. |
| U9.3 | *[inferred: Bishop Ch.3–4; ESL Ch.3–4]* generalized linear models, Poisson regression, perceptron convergence (see U9.5). |
| U9.5 | *[inferred: Bishop Ch.6–7; Bach Ch.7]* support-vector regression, multi-class SVM, reproducing-kernel Hilbert spaces. |
| U9.7 | *[inferred: ESL Ch.9–10, 15–16]* out-of-bag error, variable importance, shrinkage and subsampling. |
| U9.8 | *[inferred: MML Ch.10; ESL Ch.14]* probabilistic PCA, independent component analysis, spectral embedding. |
| U9.9 | *[inferred: MML Ch.11; Bishop Ch.9]* choosing k (silhouette, BIC), spectral clustering (uses U4.8 and U1.4). |
| U9.10 | *[inferred: Bishop Ch.8, 11, 13; Murphy; Goodfellow Ch.16–19]* sampling methods, approximate inference, partition-function problem (links to U13.6). |
| U9.12 | *[inferred: Han–Kamber; Tan–Steinbach–Kumar]* feature selection, imbalanced data, data warehousing basics. |
| U9.13 | *[inferred: Bach Ch.4, 12, 15; Shalev-Shwartz–Ben-David]* uniform convergence, margin bounds, lower bounds, online-to-batch conversion (link to U10). |
| U9.14 | *[inferred: Mitchell Ch.2, 10–12]* version spaces, explanation-based learning, first-order rule learning; link to neuro-symbolic agent design in D14. |
| U10.2 | *[inferred: Lattimore–Szepesvári Ch.6–16, 34–36]* MOSS, Bayesian regret, non-stationary bandits. |
| U10.3 | *[inferred: Lattimore–Szepesvári Ch.18–19]* linear bandits, offline policy evaluation (links to U15.3 evaluation of deployed systems). |
| U10.4 | *[inferred: Sutton–Barto Ch.3–7, 9–10]* function approximation, off-policy learning, eligibility traces. |
| U10.5 | *[inferred: Sutton–Barto Ch.13; Schulman et al. TRPO/PPO papers, recalled, not checked]* generalized advantage estimation, KL penalties and entropy regularization. |
| U11.1 | *[inferred: Goodfellow Ch.6; Nielsen Ch.1–2]* hidden-unit choices (ReLU family, GELU, SiLU), output units and cost functions as maximum likelihood. |
| U11.2 | *[inferred: Goodfellow Ch.8, 11]* batch normalization, learning-rate warm-up and schedules, practical methodology (debugging, diagnostics). |
| U11.4 | *[inferred: Goodfellow Ch.9]* pooling and invariance, 1-D/3-D convolutions, depthwise-separable convolutions, normalization layers. |
| U11.7 | *[inferred: Goodfellow Ch.10]* gradient clipping, echo-state ideas, teacher forcing. |
| U12.1 | *[inferred: SLP3 Ch.2–4, 18]* byte-pair encoding and subword tokenization (also needed by U12.4), regular expressions and text normalization, sequence labelling for parts of speech and named entities. |
| U12.2 | *[inferred: SLP3 Ch.5]* contextual versus static embeddings, bias in embeddings (link to U15.4). |
| U12.3 | *[inferred: SLP3 Ch.7; Foster Ch.9]* rotary and relative positional encodings, grouped-query attention, FlashAttention (links to U16.3), encoder-only versus decoder-only versus encoder–decoder families. |
| U12.4 | *[inferred: SLP3 Ch.7, 9]* data curation and deduplication, training-data contamination (links to U15.1), pretraining compute budgets. |
| U12.5 | *[inferred: SLP3 Ch.7; Kaplan et al. and Hoffmann et al., recalled, not checked]* mixture-of-experts, sliding-window and sparse attention, positional-interpolation tricks for long context. |
| U12.8 | *[inferred: SLP3 Ch.8; Ouyang et al., Rafailov et al., recalled, not checked]* constitutional and AI-feedback methods, reward hacking. |
| U12.9 | *[inferred: Hu et al., Dettmers et al., recalled, not checked]* adapters, prefix tuning, link to SVD low-rank theory in U4.9. |
| U13.1 | *[inferred: Foster Ch.1; Goodfellow Ch.16–17]* generative versus discriminative modelling, representation learning, core probability tools. |
| U13.3 | *[inferred: Foster Ch.4, 10]* DCGAN, StyleGAN-style progressive growing, evaluation with Inception score and FID. |
| U13.6 | *[inferred: Goodfellow Ch.18; Foster Ch.7]* contrastive divergence, noise-contrastive estimation. |
| U13.7 | *[inferred: Foster Ch.8; Ho et al.; Song et al., recalled, not checked]* noise schedules, fast samplers, evaluation by FID, text-to-image conditioning with cross-attention (reuses U12.3). |
| U13.8 | *[inferred: Foster, chapter on normalizing flow models (the publisher's description confirms the book covers them; chapter number recalled, not checked); Goodfellow Ch.20]* this family appears in the references but in none of the outlines; added so the model taxonomy of U13.1 is complete. |
| U14.1 | *[inferred: SLP3 Ch.11; Manning et al.]* retrieval metrics (precision@k, recall@k, MRR, nDCG), query likelihood models. |
| U14.12 | *[inferred: SLP3 Ch.12]* agent protocols and tool standards (stated at survey level). |
| U15.1 | *[inferred: SLP3 Ch.13]* human evaluation design, confidence intervals for metrics, benchmark contamination. |
| U16.5 | *[inferred: Hamilton, Graph Representation Learning, recalled, not checked]* GCN, GraphSAGE and attention-based GNN layers (link to U1.4 and U4.8). |
| U16.6 | *[inferred: McMahan et al., recalled, not checked]* differential privacy and secure aggregation (stated; link to U15.3). |

84 units carry gap-fills.

### E.3 Gap candidates (not added; need your agreement per Master Rules 7.4)

These are covered by a listed reference but by no outline, and each is a whole subject. They are **not** in the structure above until you agree.

| Candidate | Reference | Would sit in |
|---|---|---|
| Speech: phonetics, feature extraction, ASR, text-to-speech | SLP3 Ch. 15–17 | new D12-X |
| Machine translation | SLP3 Ch. 13 | D12 |
| Classical linguistic structure: tagging, parsing, information extraction, semantic roles, coreference, discourse, dialogue | SLP3 Ch. 18–26 | new D12-X |
| Structured prediction | Bach Ch. 13 | D9 |
| Linear factor models, ICA, slow-feature analysis, sparse coding; partition-function estimation; approximate inference | Goodfellow Ch. 13, 18, 19 | D9 / D13 |
| Music generation, world models | Foster Ch. 11–12 | D13 |
| Partial monitoring | Lattimore–Szepesvári | D10 |

## Appendix F. Source anomalies, truncations and residual flagged atoms

### F.1 Anomalies in the sources (kept visible, not silently fixed)

| Source | Issue | Handling |
|---|---|---|
| EM2 | prerequisite: Engineering Mathematics I | Recorded in Appendix D. |
| MM | source lists only 4 of the course weeks | Missing weeks or categories are filled from benchmarks and marked *inferred* in the units that cite this source. |
| HEM | source Week 4 text duplicates Week 2 text (copy error); stray "288" in Week 12 | Repeated text is cited as given in each cell; nothing is lost and nothing is double-counted as a new topic. |
| DM | title absent in source | Title inferred from the course content; please confirm (Appendix G.2). |
| OMLH | source lists only 8 weeks; Weeks 2, 6, 8 repeat Weeks 1, 5, 7 text | Missing weeks or categories are filled from benchmarks and marked *inferred* in the units that cite this source. |
| ALAJ | source Weeks 8 and 9 both carry the dynamical-systems text | Repeated text is cited as given in each cell; nothing is lost and nothing is double-counted as a new topic. |
| MLE | title absent in source | Title inferred from the course content; please confirm (Appendix G.2). |
| S50 | heading says 50 techniques; only categories 1-9 appear in the source | Missing weeks or categories are filled from benchmarks and marked *inferred* in the units that cite this source. |
| LPCS | source Weeks 1-3 and 4-5 repeat the same module text | Repeated text is cited as given in each cell; nothing is lost and nothing is double-counted as a new topic. |
| PSS | title absent in source | Title inferred from the course content; please confirm (Appendix G.2). |
| IPS | lines 1579-1594 duplicate Week 1-2 items | Repeated text is cited as given in each cell; nothing is lost and nothing is double-counted as a new topic. |
| CVX | Lines 318–329 are page header/footer text (prerequisites, a pointer to Boyd's lectures, coordinator), interleaved with the lecture list | Prerequisites go to Appendix D; the Boyd lectures are treated as a reference. |
| nptel.txt line 213 | Cites course id 106104573, which matches no course id listed in the file (it follows the Discrete Mathematics block) | Flagged in Appendix G. |
| Typos | 'Grpah', 'Dula' (HEM), 'diinensionality' (ALAK), 'Resarch' (ALAJ), 'liner' (LPCS), 'Borwin', 'Byod', 'Rockafeller', 'Hiriat', 'Seidal' | Meaning taken from context; the unit text uses the correct spelling. |

### F.2 Atoms the word-level check still flags, reviewed by hand

- **Outline-prose atoms flagged:** 266. All were reviewed by hand: they are audience statements, marketing sentences and connective phrases; every topic named in an outline appears in the units that cite it.
- **Non-outline atoms flagged:** 51. All were reviewed: source typos, section labels (for example 'Section VIII', 'Classical Techniques 1'), key-takeaway sentences, and prose in LPCS and FDL whose topics are present under other wording.

<details><summary>Full list of non-outline flagged atoms</summary>

- `IM:A` COURSEABSTRACT ◦ Polynomials
- `HEM:W5` Various types of Grpah
- `HEM:W7` Dula of a Planar graph
- `ALAK:W10` and diinensionality reduction
- `HEM:W12` Application of M/M/S FIFO 288
- `MLE:W4` Applications
- `AEMK:W4` Jacobi and Gauss-Seidal method
- `LPCS:W1` we will move to the basics of liner algebra
- `LPCS:W1` In particular
- `LPCS:W2` we will move to the basics of liner algebra
- `LPCS:W2` In particular
- `LPCS:W3` we will move to the basics of liner algebra
- `LPCS:W3` In particular
- `LPCS:W4` This module will start with hyperplane separation theorems
- `LPCS:W4` will be covered in detail
- `LPCS:W4` from John Nash of “a beautiful mind”
- `LPCS:W5` This module will start with hyperplane separation theorems
- `LPCS:W5` will be covered in detail
- `LPCS:W5` from John Nash of “a beautiful mind”
- `CVX:L10-19` considered
- `LPCS:W6` We will discuss primal-dual methods too
- `LPCS:W6` this will allow us to develop an algorithm for the max flow problem
- `LPCS:W7` In many instance
- `LPCS:W7` the quantity in focus does not turn out to be a linear program
- `LPCS:W8` In particular
- `LPCS:W8` If time permits
- `LPCS:W8` we will see other applications
- `LPCS:W8` like in the area of Boolean functions
- `LPCS:W8` of linear programming and possible extensions
- `FDL:W12` how multimodal and instructionfollowing capabilities emerge
- `FDL:W12` Concepts of generative models like VAEs
- `FDL:W1` A conceptual and practical foundation on the basic architecture of Neural Networks
- `FDL:W3` Understand how CNNs learn visual patterns
- `FDL:W3` effective convolution-based models from the scratch
- `FDL:W4` Understand the progression from AlexNet to ResNet
- `FDL:W4` and also be able to apply powerful pretrained
- `FDL:W4` models using transfer learning and boost performance using ensemble techniques
- `FDL:W5` Understand the theory behind explainable AI
- `FDL:W6` real-world tasks
- `FDL:W8` Understand the GRU architecture
- `FDL:W8` Compare LSTM vs GRU
- `FDL:W8` A conceptual and practical understanding of LSTMs
- `FDL:W8` and attention-enhanced RNNs
- `MLE:W8` Applications
- `FDL:W10` Understanding the working mechanism of Autoencoders and its implementation
- `FDL:W11` A strong conceptual foundation in Transformers
- `LPCS:W4` we will also cover Yao’s technique to give lower bounds in communication complexity setting
- `LPCS:W5` we will also cover Yao’s technique to give lower bounds in communication complexity setting
- `FDL:W12` Diffusion uses latent-space denoising to generate high-quality images
- `FDL:W6` Understanding of modern CNN-based segmentation and detection architectures and be able to apply them to
- `FDL:W7` Conceptual foundation in sequential deep learning models using RNNs and understand their limitations

</details>

## Appendix G. Notes found inside the source file, and decisions needed

`nptel.txt` contains five notes written to an assistant, not course content. **None was acted on**: no file was downloaded, fetched or deleted. They are reported here so you can decide.

| Line | What the note says | Status |
|---|---|---|
| 99 | "ingest the project files. Also, along with learning this course, I also want to learn to implement these techniques from the scratch in python, numpy, etc." | **Applied to the design**: every unit has a from-scratch **Build** and the project docs (Master Rules) governed the structure. |
| 101 | Fetch NPTEL assignment images for course 106108702 (Mathematical Foundations for ML), weeks 1–12, from `archive.nptel.ac.in`, store as text, delete the images | **Not done.** Needs your OK to download. |
| 103 | "store it in text and delete the images to save space" | Not done (see 101). |
| 105 | "integrate into the curriculum and unify. If there are no assignments provided for certain topics, then create them." | **Unification done.** Authoring missing assignments is a next step (below). |
| 151 | Fetch assignment PDFs for course 111107137 (Essential Mathematics for ML), 8 weeks, extract text, delete the PDFs | **Not done.** Needs your OK to download. |
| 213 | Fetch assignment images for course id 106104573, weeks 1–12 (pattern `noc25_cs27_assignment_Week_N`), store, delete | **Not done.** The id matches no listed course; it follows the Discrete Mathematics block, so it is probably that course. Please confirm. |

### G.1 Assignment slots (to fill)

| Source course | NPTEL assignments | Plan |
|---|---|---|
| MFML | Weekly, W1–W12 (URL pattern in line 101) | Fetch on approval; store text; map each to its unit (Appendix B). |
| EMML | Weekly, 8 weeks of PDFs (line 151) | Fetch on approval. |
| DM (probable) | Weekly (line 213; id to confirm) | Fetch on approval. |
| All other courses and all GenAI sections | None provided | Authored problem sets per unit: routine → qualifying difficulty, at least one proof or derivation and one computational problem, key written first and shown only after an attempt (Master Rules 6.11). |

### G.2 Decisions I need from you

1. **Downloads and deletions** in G above: approve each, or skip.
2. **Gap candidates** in E.3: add any, none, or all (speech and linguistic NLP are the largest).
3. **Truncated sources** (OMLH has 8 of its weeks, MM has 4, S50 has 9 of 50 categories): confirm that benchmark fill-ins are acceptable, or supply the missing outlines.
4. **Missing course titles** (DM, MLE, PSS): confirm the inferred titles in Appendix A.
5. **Where the record lives:** your existing tracker file, or a new one generated from Appendix H.

## Appendix H. Initial record (Master Rules 8.3)

**Resume point:** U1.1, first block (proof paradigms), nothing taught yet. **Standing overrides:** see the course profile. **Misconception register, error log, heuristics catalogue, decision journal, frontier list:** empty.

| Unit | Title | State | Depth | Evidence |
|---|---|---|---|---|
| U1.1 | Logic, proof paradigms and formal languages | not started | L0 | none |
| U1.2 | Counting, generating functions and combinatorics | not started | L0 | none |
| U1.3 | Posets, lattices, Boolean algebra and switching circuits | not started | L0 | none |
| U1.4 | Graph theory | not started | L0 | none |
| U1.5 | Number theory and cryptography | not started | L0 | none |
| U1.6 | Algebra: finite fields, codes, groups and orbit counting | not started | L0 | none |
| U1.7 | An invitation to mathematics: polynomials, functions, matrices, conservation laws | not started | L0 | none |
| U2.1 | Numbers, countability, functions, limits and continuity | not started | L0 | none |
| U2.2 | Differentiation and mean value theorems | not started | L0 | none |
| U2.3 | Integration, applications and transcendental functions | not started | L0 | none |
| U2.4 | Taylor expansion, sequences, series and power series | not started | L0 | none |
| U2.5 | Improper integrals, Gamma and Beta functions, integrals dependent on parameters | not started | L0 | none |
| U3.1 | Functions of several variables, partial derivatives and differentiability | not started | L0 | none |
| U3.2 | Taylor expansion in several variables, maxima, minima and Lagrange multipliers | not started | L0 | none |
| U3.3 | Multiple integrals and their applications | not started | L0 | none |
| U3.4 | Vector calculus: fields, line and surface integrals, Green, Gauss and Stokes | not started | L0 | none |
| U3.5 | Matrix calculus, Jacobians and Hessians for machine learning | not started | L0 | none |
| U4.1 | Systems of linear equations, matrices, elimination, rank and inverses | not started | L0 | none |
| U4.2 | Vectors, vector spaces, subspaces, bases and dimension | not started | L0 | none |
| U4.3 | Linear maps, representation by matrices, duality and quotient spaces | not started | L0 | none |
| U4.4 | Inner products, norms, orthogonality, projections and Gram–Schmidt | not started | L0 | none |
| U4.5 | Determinants, multilinear forms and permutations | not started | L0 | none |
| U4.6 | Eigenvalues, eigenvectors, similarity and diagonalization | not started | L0 | none |
| U4.7 | Canonical forms: minimal polynomial, invariant subspaces, Jordan and rational forms | not started | L0 | none |
| U4.8 | Spectral theory: normal operators, symmetric matrices, quadratic forms, PSD matrices and kernels | not started | L0 | none |
| U4.9 | LU, QR, conditioning, SVD, pseudo-inverse and low-rank approximation | not started | L0 | none |
| U4.10 | Least squares, regularized and constrained least squares | not started | L0 | none |
| U4.11 | Applications of linear algebra: PageRank, sparsity, dynamical systems, Markov chains, signal processing and data analytics | not started | L0 | none |
| U5.1 | Probability foundations: from events to Bayes' theorem | not started | L0 | none |
| U5.2 | Random variables, distributions and moments | not started | L0 | none |
| U5.3 | Special discrete distributions and the Poisson process | not started | L0 | none |
| U5.4 | Special continuous distributions and the normal distribution | not started | L0 | none |
| U5.5 | Functions of random variables, transformations and order statistics | not started | L0 | none |
| U5.6 | Joint distributions, conditioning, covariance and multivariate normal | not started | L0 | none |
| U5.7 | Limit theorems and concentration inequalities | not started | L0 | none |
| U5.8 | Markov chains, queueing theory and reliability | not started | L0 | none |
| U6.1 | Data, descriptive statistics and measures of association | not started | L0 | none |
| U6.2 | Sampling distributions and point estimation | not started | L0 | none |
| U6.3 | Confidence intervals and hypothesis testing | not started | L0 | none |
| U6.4 | Correlation, regression and multivariate analysis | not started | L0 | none |
| U6.5 | Bayesian inference and MCMC | not started | L0 | none |
| U6.6 | Forecasting with statistical and machine-learning models: hydrology and water-resources applications | not started | L0 | none |
| U7.1 | First- and higher-order ordinary differential equations | not started | L0 | none |
| U7.2 | Numerical analysis: iteration, root finding, interpolation and quadrature | not started | L0 | none |
| U7.3 | Complex variables: analytic functions and complex integration | not started | L0 | none |
| U7.4 | Series, singularities, residues, real integrals and conformal mapping | not started | L0 | none |
| U7.5 | Laplace, Z, Fourier and discrete Fourier transforms | not started | L0 | none |
| U7.6 | Mathematical modelling: discrete and continuous dynamical systems | not started | L0 | none |
| U8.1 | Optimization problems: formulation, history, transformations and basic facts | not started | L0 | none |
| U8.2 | Convex sets, cones, polyhedra and separation | not started | L0 | none |
| U8.3 | Convex functions and their calculus | not started | L0 | none |
| U8.4 | Unconstrained optimization theory | not started | L0 | none |
| U8.5 | Constrained optimization theory: Lagrange, cones, Fritz John and KKT | not started | L0 | none |
| U8.6 | Lagrangian duality, saddle points and minimax | not started | L0 | none |
| U8.7 | Linear programming: simplex, duality, sensitivity and interior-point methods | not started | L0 | none |
| U8.8 | Unconstrained descent methods: line search, gradient, Newton, quasi-Newton, conjugate gradient, trust region | not started | L0 | none |
| U8.9 | Constrained optimization algorithms: QP, projected and reduced gradient, penalty, augmented Lagrangian, SQP | not started | L0 | none |
| U8.10 | First-order methods for ML: stochastic, accelerated, proximal, adaptive, and the dynamical-systems view | not started | L0 | none |
| U8.11 | Conic and structured convex programs: QCQP, SOCP, SDP, geometric programs | not started | L0 | none |
| U8.12 | Applications of optimization: signal estimation, compressive sensing, radar, big data and finance | not started | L0 | none |
| U8.13 | Non-smooth and difference-of-convex optimization | not started | L0 | none |
| U8.14 | Distributed optimization: graphs, consensus, ADMM and dual decomposition | not started | L0 | none |
| U8.15 | Dynamic optimization and complementarity problems | not started | L0 | none |
| U9.0 | History of AI, symbolic AI and the machine-learning workflow | not started | L0 | none |
| U9.1 | What machine learning is: paradigms, data, hypothesis spaces and the statistical framework | not started | L0 | none |
| U9.2 | Model evaluation and selection: bias–variance, validation, tuning and metrics | not started | L0 | none |
| U9.3 | Linear regression and linear classification: estimation, logistic and softmax regression, surrogate losses | not started | L0 | none |
| U9.4 | Regularization and implicit regularization | not started | L0 | none |
| U9.5 | Perceptron, support vector machines and kernel methods | not started | L0 | none |
| U9.6 | Bayes decision theory, density estimation and probabilistic classifiers | not started | L0 | none |
| U9.7 | Decision trees and ensembles: bagging, boosting, random forests | not started | L0 | none |
| U9.8 | Dimensionality reduction and feature learning | not started | L0 | none |
| U9.9 | Clustering, mixture models and the EM algorithm | not started | L0 | none |
| U9.10 | Probabilistic graphical models, hidden Markov models, inference and Gaussian processes | not started | L0 | none |
| U9.11 | Instance-based learning, collaborative filtering and recommendation | not started | L0 | none |
| U9.12 | Data mining: preprocessing, association rules, sequence mining, outliers and case studies | not started | L0 | none |
| U9.13 | Learning theory: PAC, VC dimension, generalization and modern overparametrization | not started | L0 | none |
| U9.14 | Symbolic and knowledge-based machine learning, tools and cognitive-science influences | not started | L0 | none |
| U10.1 | From batch to online learning: adversarial full-information and bandit settings | not started | L0 | none |
| U10.2 | Stochastic bandits: regret notions, UCB, KL-UCB and lower bounds | not started | L0 | none |
| U10.3 | Contextual bandits and pure exploration | not started | L0 | none |
| U10.4 | Markov decision processes, dynamic programming and temporal-difference learning | not started | L0 | none |
| U10.5 | Policy gradient, actor–critic and proximal policy optimization | not started | L0 | none |
| U11.1 | Perceptron, multilayer networks, activations and loss functions | not started | L0 | none |
| U11.2 | Backpropagation and training deep networks | not started | L0 | none |
| U11.3 | Overfitting, regularization and generalization in deep networks | not started | L0 | none |
| U11.4 | Convolutional neural networks and image representation | not started | L0 | none |
| U11.5 | Explainable AI for deep models | not started | L0 | none |
| U11.6 | Segmentation and object detection | not started | L0 | none |
| U11.7 | Recurrent networks: RNN, LSTM, GRU, backpropagation through time and attention in RNNs | not started | L0 | none |
| U11.8 | Autoencoders and representation learning | not started | L0 | none |
| U12.1 | NLP foundations and the classical NLP pipeline | not started | L0 | none |
| U12.2 | Word representations and multilingual embeddings | not started | L0 | none |
| U12.3 | Attention and the Transformer architecture | not started | L0 | none |
| U12.4 | Pretraining, self-supervised learning and the LLM landscape | not started | L0 | none |
| U12.5 | Scaling laws, LLM architectures and long context | not started | L0 | none |
| U12.6 | Decoding strategies and sampling | not started | L0 | none |
| U12.7 | Prompting: fundamentals, APIs and advanced techniques | not started | L0 | none |
| U12.8 | Instruction tuning, RLHF and alignment: PPO and DPO | not started | L0 | none |
| U12.9 | Parameter-efficient fine-tuning: LoRA and QLoRA | not started | L0 | none |
| U12.10 | Prompt optimization, compression and prompt security | not started | L0 | none |
| U13.1 | Probabilistic deep generative modelling: foundations and taxonomy | not started | L0 | none |
| U13.2 | Generative modelling via variational divergence minimization | not started | L0 | none |
| U13.3 | Generative adversarial networks: formulation, training, WGAN and applications | not started | L0 | none |
| U13.4 | Variational autoencoders, improvements and VQ-VAE | not started | L0 | none |
| U13.5 | Autoregressive models | not started | L0 | none |
| U13.6 | Energy-based and score-based models; Langevin sampling | not started | L0 | none |
| U13.7 | Denoising diffusion probabilistic models, conditional diffusion and Stable Diffusion | not started | L0 | none |
| U13.8 | Normalizing flows (gap-fill from the references) | not started | L0 | none |
| U14.1 | Why RAG, RAG architecture and classical retrievers | not started | L0 | none |
| U14.2 | RAG failure modes, types of RAG and assessment | not started | L0 | none |
| U14.3 | Sparse retrieval limits and dense representations | not started | L0 | none |
| U14.4 | Learning retrieval-oriented embeddings and choosing an embedding model | not started | L0 | none |
| U14.5 | Document processing and chunking | not started | L0 | none |
| U14.6 | Vector databases and indexes: KNN, IVF, PQ, HNSW, FAISS and ChromaDB | not started | L0 | none |
| U14.7 | The retrieval pipeline: bi-encoder, cross-encoder, ColBERT and two-stage retrieval | not started | L0 | none |
| U14.8 | Production RAG: request shaping, query transformation, routing, security, cost and observability | not started | L0 | none |
| U14.9 | Limits of single-shot RAG and the move to agents | not started | L0 | none |
| U14.10 | Agent basics, tool calling and orchestration | not started | L0 | none |
| U14.11 | Planning with ReAct | not started | L0 | none |
| U14.12 | State machines and LangGraph | not started | L0 | none |
| U14.13 | Agentic memory | not started | L0 | none |
| U14.14 | Provenance and citations | not started | L0 | none |
| U14.15 | Multi-agent architecture summary, error handling and best practices | not started | L0 | none |
| U15.1 | LLM evaluation: metric architecture and reference-based metrics | not started | L0 | none |
| U15.2 | LLM-as-a-judge and factuality | not started | L0 | none |
| U15.3 | AI safety foundations and threat models | not started | L0 | none |
| U15.4 | White-box attacks and prompt injection | not started | L0 | none |
| U15.5 | Black-box attacks and the jailbreak taxonomy | not started | L0 | none |
| U15.6 | Defense, interpretability and ethics | not started | L0 | none |
| U16.1 | CNN computation and accelerators | not started | L0 | none |
| U16.2 | Parallelism for training, communication and fault tolerance | not started | L0 | none |
| U16.3 | LLM decoding, memory management and serving infrastructure | not started | L0 | none |
| U16.4 | Model compression and quantization | not started | L0 | none |
| U16.5 | Graph neural network inference systems | not started | L0 | none |
| U16.6 | Federated learning | not started | L0 | none |
| U17.1 | Capstone A: the mathematics of machine learning, end to end | not started | L0 | none |
| U17.2 | Capstone B: a classical-ML library from scratch | not started | L0 | none |
| U17.3 | Capstone C: a deep-learning framework from scratch | not started | L0 | none |
| U17.4 | Capstone D: an LLM application platform (RAG + agents + safety) | not started | L0 | none |
| U17.5 | Capstone E: generative models | not started | L0 | none |
| U17.6 | Capstone F: ML systems and efficiency | not started | L0 | none |
| U17.7 | Final integrated capstone: train, align, compress, serve, evaluate and secure a small language model | not started | L0 | none |

## Appendix I. From-scratch build inventory

| Unit | Build (from scratch first, professional tool as oracle) |
|---|---|
| U1.1 | a truth-table and tautology checker in Python; a DFA simulator driven by a transition table. |
| U1.2 | recurrence solver and coefficient extraction from power series using NumPy; brute-force verification of counting formulas on small cases. |
| U1.3 | Quine–McCluskey minimizer from scratch; checked against hand Karnaugh-map reductions. |
| U1.4 | graph class with adjacency/incidence matrices, BFS/DFS, bipartiteness and Euler-tour test; greedy and DSATUR colouring; TSP by dynamic programming (Held–Karp) at toy size. |
| U1.5 | extended Euclid, fast modular exponentiation, Miller–Rabin and toy RSA from scratch. Hand-built cryptography is for learning only and is never deployed (Master Rules 6.8). |
| U1.6 | GF(2^m) arithmetic; Hamming and Reed–Solomon encoder/decoder at toy size; Burnside-count of necklaces by enumeration versus formula. |
| U1.7 | interpolation and Vandermonde solve in NumPy, with condition-number growth observed (bridge to U4.9). |
| U2.1 | bisection and ε–δ explorers in Python; numerical estimation of convergence order from an error sequence. |
| U2.2 | Newton and secant solvers from scratch, with the error curve plotted against the predicted order (links to U8.8). |
| U2.3 | trapezoid, Simpson and adaptive quadrature in NumPy, checked against `scipy.integrate`. |
| U2.4 | Taylor polynomials of exp, sin, log with error versus remainder bound. |
| U2.5 | numerical evaluation of Γ and B and moment integrals used later in D5 (Gamma, Beta and normal densities). |
| U3.1 | numerical gradient and Jacobian checker (finite differences) and tape-based reverse-mode differentiation from scratch (bridge to U11.2 backpropagation). |
| U3.2 | Newton step on a two-variable function, with Hessian eigenvalues classifying the stationary point. |
| U3.3 | Monte Carlo and grid evaluation of double integrals (forward link to D5 Monte Carlo). |
| U3.4 | numerical line and flux integrals; verification of Green/Gauss on a test field. |
| U3.5 | NumPy autodiff-checking of every matrix-derivative identity against finite differences. |
| U4.1 | Gaussian elimination with partial pivoting, RREF, rank and inverse from scratch; compare with `numpy.linalg`. |
| U4.2 | subspace-membership, basis extraction and dimension tools using exact rational arithmetic and then floating point (observe rank decisions with tolerance). |
| U4.3 | matrix of a map in arbitrary bases, change of basis and the effect on a matrix; null space and range via SVD, from scratch after U4.9. |
| U4.4 | classical and modified Gram–Schmidt, Householder QR and Givens rotators from scratch, observing loss of orthogonality (MGS vs CGS). |
| U4.5 | determinant by permutation expansion, by LU, and by cofactor, with cost measured; volume of a parallelepiped. |
| U4.6 | power iteration, inverse iteration and QR iteration from scratch, checked against `numpy.linalg.eig`. |
| U4.7 | Jordan-chain computation for small matrices with exact arithmetic; demonstrate numerical instability of Jordan form in floating point. |
| U4.8 | Jacobi eigenvalue algorithm for symmetric matrices; PSD test by Cholesky; Gram-matrix kernel construction. |
| U4.9 | SVD via eigendecomposition of AᵀA, then one-sided Jacobi/Golub–Kahan from scratch; image compression by truncated SVD; compare with `numpy.linalg.svd`. |
| U4.10 | least squares by normal equations, QR and SVD with conditioning experiments; ridge and weighted LS; polynomial classifier on MNIST via LS. |
| U4.11 | PageRank on a small web graph; matrix completion by alternating least squares and by nuclear-norm heuristic; OMP from scratch; CP decomposition by ALS. |
| U5.1 | Bayes' rule on diagnostic-test and spam-filter examples; Monte Carlo verification of birthday and Monty-Hall problems. |
| U5.2 | empirical CDF, histogram and moment estimators; skewness and kurtosis from scratch. |
| U5.3 | samplers for each discrete law from uniform random numbers; simulation of a Poisson process. |
| U5.4 | Box–Muller and inverse-CDF samplers from scratch; Q–Q plots against the standard normal. |
| U5.5 | numerical check of transformed densities against histograms of simulated samples. |
| U5.6 | multivariate normal sampler via Cholesky; conditioning formula verified by simulation; Gaussian copula sampler. |
| U5.7 | empirical convergence in the CLT for several source distributions; tail-bound tightness plots (used again in U10.3 for UCB). |
| U5.8 | discrete-event simulator of M/M/1 and M/M/s queues compared with closed forms (reappears in U16.3 for LLM serving queues). |
| U6.1 | descriptive-statistics library from scratch (mean, median, mode, variance, SD, range, IQR, skewness, kurtosis, quantiles); box plots and histograms by hand. |
| U6.2 | MLE by closed form and by numerical optimization (links to D8); bias–variance of estimators by simulation. |
| U6.3 | each test from scratch with exact p-values, checked against `scipy.stats`; power curves by simulation; A/B-test simulator. |
| U6.4 | OLS with standard errors and t-tests from scratch; ridge and lasso (coordinate descent) from scratch. |
| U6.5 | Metropolis–Hastings and Gibbs sampler from scratch; posterior of a coin bias and of a linear-regression coefficient. |
| U6.6 | rolling-origin forecasting evaluation of ARMA versus random forest versus LSTM on a streamflow-like series. |
| U7.1 | Euler, Heun and RK4 integrators from scratch with global-error order measured. |
| U7.2 | all iterative solvers and interpolation formulae from scratch, checked against `scipy`. |
| U7.3 | numerical contour integration and verification of Cauchy's formula. |
| U7.4 | residue calculator for rational functions; conformal map visualizer. |
| U7.5 | FFT (radix-2) from scratch; spectral solution of a heat-equation boundary value problem. |
| U7.6 | cobweb and bifurcation diagram generators; Lotka–Volterra phase portraits; simulation of Leslie matrices. |
| U8.1 | a small modelling layer in Python (objective, constraints, gradient check) used by all later optimization units. |
| U8.2 | projection onto convex sets (ball, box, simplex, halfspace) from scratch; separating-hyperplane finder via QP. |
| U8.3 | numerical convexity tester via random Hessian sampling; subgradient computation for ℓ1, hinge and max functions. |
| U8.4 | classify the stationary points of Rosenbrock, Himmelblau and a saddle function by Hessian eigenvalues. |
| U8.5 | KKT-system solver for small QPs; verification of KKT residuals on solutions from `scipy.optimize`. |
| U8.6 | dual of an LP and of an SVM computed and checked numerically; zero-sum game solved by LP. |
| U8.7 | tableau simplex (two-phase and dual) from scratch; log-barrier interior-point method from scratch; compare with `scipy.optimize.linprog`. |
| U8.8 | GD with backtracking, Newton, BFGS/L-BFGS, CG and dogleg trust region from scratch; iteration-count and condition-number experiments on quadratics and Rosenbrock; compare with `scipy.optimize.minimize`. |
| U8.9 | quadratic-penalty and augmented-Lagrangian solvers from scratch on a small equality-constrained problem; projected gradient onto the simplex. |
| U8.10 | SGD, momentum, Nesterov, AdaGrad, RMSProp and Adam from scratch in NumPy on least squares and logistic regression; ODE-view simulation of gradient flow versus discrete GD. |
| U8.11 | the same problems solved with from-scratch IPM and with `cvxpy`, with solver comparison. |
| U8.12 | ISTA and coordinate-descent LASSO; OMP recovery experiments (phase transition); water-filling solver. |
| U8.13 | subgradient method for hinge-loss SVM; DCA for a sparse regression with a non-convex penalty. |
| U8.14 | ADMM for LASSO and consensus averaging over a graph from scratch (reuses U1.4 and U4.8). |
| U8.15 | value-iteration and backward-induction solver for a finite-horizon problem (feeds U10.4 MDPs). |
| U9.0 | a rule-based expert-system toy, then the scikit-learn supervised and unsupervised workflows end to end, with each metric recomputed by hand from the confusion matrix. |
| U9.1 | a minimal ML framework in NumPy (dataset split, fit/predict API, metrics) used by all later units. |
| U9.2 | cross-validation, ROC/AUC, confusion-matrix metrics (accuracy, precision, recall, F1) and grid/random search from scratch. |
| U9.3 | linear, logistic and softmax regression with gradient descent and Newton/IRLS from scratch; compare with scikit-learn. |
| U9.4 | ridge path, lasso path and elastic net by coordinate descent from scratch. |
| U9.5 | perceptron, SVM via SMO and via QP (cvx), kernel ridge regression and kernel SVM from scratch; compare with `sklearn.svm`. |
| U9.6 | Gaussian discriminant analysis, naive Bayes, Parzen and kNN from scratch. |
| U9.7 | CART, random forest, AdaBoost and gradient boosting from scratch; compare with scikit-learn and XGBoost-style implementations. |
| U9.8 | PCA via covariance eigendecomposition and via SVD, LDA, kernel PCA and a t-SNE sketch from scratch; compare with scikit-learn. |
| U9.9 | k-means++, GMM-EM, DBSCAN, agglomerative linkage and mean-shift from scratch. |
| U9.10 | HMM (forward, Viterbi, Baum–Welch), variable elimination on a small Bayesian network and GP regression from scratch. |
| U9.11 | kNN with KD-tree, user–user and item–item collaborative filtering, ALS matrix factorization from scratch. |
| U9.12 | Apriori and FP-growth, PrefixSpan sketch and an end-to-end mining pipeline (clean, mine, evaluate, visualize). |
| U9.13 | empirical double-descent experiment with random features and min-norm least squares. |
| U9.14 | a small ILP learner (FOIL-style) and ID3 from scratch. |
| U10.1 | Hedge and Exp3 from scratch and regret curves against adaptive and oblivious adversaries. |
| U10.2 | UCB1, KL-UCB, Thompson sampling and ε-greedy on Bernoulli bandits with confidence-interval plots. |
| U10.3 | LinUCB on a simulated recommendation task; LUCB for best-arm identification. |
| U10.4 | value iteration, tabular Q-learning and SARSA on a grid world; deep Q-network sketch (after U11). |
| U10.5 | REINFORCE with baseline and a PPO implementation on a small control task. |
| U11.1 | perceptron, a 2-layer MLP and arbitrary-depth MLP from scratch in NumPy, trained on XOR, a churn-style tabular dataset and MNIST. |
| U11.2 | reverse-mode autodiff engine and full MLP training loop from scratch; gradient check against finite differences; then re-implementation in PyTorch (`autograd`) as the oracle. |
| U11.3 | dropout, weight decay, early stopping and augmentation layers from scratch; learning-curve diagnostics. |
| U11.4 | conv, pooling and a small CNN (forward and backward) in NumPy via im2col; then PyTorch; compare receptive-field arithmetic with measured gradients. |
| U11.5 | occlusion maps, LIME and Shapley sampling from scratch; Grad-CAM in PyTorch. |
| U11.6 | U-Net for a small segmentation set; IoU and NMS from scratch; YOLO inference with a pretrained model. |
| U11.7 | vanilla RNN, LSTM and GRU with BPTT from scratch; character-level language model. |
| U11.8 | dense, convolutional and denoising autoencoders from scratch; latent-space visualization. |
| U12.1 | tokenizer, n-gram LM with smoothing, TF-IDF and a Naive-Bayes/logistic text classifier from scratch; compare with NLTK and scikit-learn. |
| U12.2 | skip-gram with negative sampling and GloVe from scratch; analogy and similarity tests. |
| U12.3 | single-head, multi-head and masked attention, sinusoidal positional encoding, an encoder block, a decoder block and a tiny decoder-only Transformer trained on characters, all from scratch in NumPy, then PyTorch as the oracle. |
| U12.4 | a masked-LM and a causal-LM pretraining loop at toy scale; fine-tune a small pretrained BERT/GPT for classification and QA. |
| U12.5 | fit a scaling law to training runs of a family of tiny Transformers. |
| U12.6 | greedy, beam, temperature, top-k and top-p decoders from scratch over a small LM. |
| U12.7 | a chat client with roles, tool-calling and a ReAct loop; prompt-chaining pipeline; ToT search on a small puzzle. Live API calls follow a recorded-response replay first and run only under a spend cap (Master Rules 11.2). |
| U12.8 | reward model on preference pairs; toy PPO-for-text and DPO fine-tuning of a tiny LM, from scratch. |
| U12.9 | LoRA layer from scratch merged into a frozen Transformer; compare full fine-tuning and LoRA on a small task. |
| U12.10 | a prompt-version registry and A/B test harness; evolutionary prompt search over a tiny task; token-pruning prompt compressor. |
| U13.1 | a tiny density estimator by MLE (Gaussian mixture) and importance-sampling estimator from scratch. |
| U13.2 | numerical estimation of f-divergences between Gaussians; f-GAN objective on a 1-D toy distribution. |
| U13.3 | vanilla GAN, WGAN-GP and a conditional GAN from scratch on 2-D and MNIST data; mode-collapse experiments. |
| U13.4 | VAE and VQ-VAE from scratch, with latent interpolation and posterior-collapse diagnostics. |
| U13.5 | a character/pixel-level autoregressive model from scratch (shares code with U12.3). |
| U13.6 | Langevin sampler on a 2-D mixture; denoising score matching on toy data. |
| U13.7 | DDPM with a small U-Net (reuse U11.6) on 2-D then MNIST; classifier-free guidance; latent diffusion using the autoencoder of U11.8. |
| U13.8 | RealNVP on a 2-D dataset from scratch, with density plots. |
| U14.1 | inverted index, TF-IDF and BM25 retriever and a minimal RAG loop from scratch. |
| U14.2 | failure-injection harness (drop gold chunk, add distractor, conflicting context) and RAGAS-style metrics (faithfulness, answer relevance, context precision/recall). |
| U14.3 | mean-pooled BERT sentence embeddings versus TF-IDF on a retrieval benchmark. |
| U14.4 | a bi-encoder trained with in-batch and hard negatives; embedding-model comparison with a cost and quality table. |
| U14.5 | four chunkers and a recall@k comparison on structured and unstructured corpora. |
| U14.6 | brute-force KNN, IVF with k-means centroids, PQ codebooks and a small HNSW from scratch; compare with FAISS and ChromaDB. |
| U14.7 | hybrid (BM25 + dense) first stage with reciprocal-rank fusion and a cross-encoder reranker. |
| U14.8 | query rewriter, multi-query retriever, router and semantic cache with metrics and tracing. |
| U14.9 | a multi-hop QA benchmark and a single-shot baseline measuring where it fails. |
| U14.10 | tool schema, a tool-calling loop and a planner–executor pair from scratch (no framework). |
| U14.11 | ReAct and hierarchical-ReAct agents with a step-budget and failure analysis. |
| U14.12 | the same agent team as a hand-written state machine, then in LangGraph; HITL interrupt and resume. |
| U14.13 | episodic buffer and semantic store with conflict resolution and recall evaluation. |
| U14.14 | structured-output citations with a verifier that checks each claim against retrieved spans. |
| U14.15 | the D14 integrated project (see U17.4). |
| U15.1 | ROUGE, BLEU, METEOR-style and BERTScore-style scorers from scratch, checked against reference libraries; inter-annotator agreement. |
| U15.2 | pairwise and rubric judges with position-swap debiasing and agreement with human labels. |
| U15.3 | a membership-inference test on a model the learner trained; adversarial examples (FGSM) on a small CNN. |
| U15.4 | a GCG-style discrete optimization against a small open model in a disposable sandbox, measuring attack success and transfer. |
| U15.5 | measurement harness (attack success rate by category) against a locally hosted model, with no harmful payloads stored. |
| U15.6 | a red-team/blue-team exercise on the learner's own RAG agent, producing a defect list and fixes. |
| U16.1 | loop-nest convolution with tiling in NumPy/C and a roofline plot from measured throughput. |
| U16.2 | ring-allreduce simulator; data-parallel SGD across processes with PyTorch DDP. |
| U16.3 | a KV-cache decoder and a continuous-batching scheduler simulator; measure tokens/s versus batch size. |
| U16.4 | uniform and per-channel quantization, magnitude pruning and logit distillation from scratch. |
| U16.5 | message-passing GCN layer from scratch with sparse matrix multiply and a sampling baseline. |
| U16.6 | FedAvg simulation with non-IID partitions and a robust aggregator against a poisoning client. |

136 builds listed.
