# Unified Curriculum: Mathematical Foundations → Machine Learning → Deep Learning → LLMs, RAG, Agents and Safety

**Built:** 2026-11-03, from `nptel.txt` (43 NPTEL and learner-supplied course outlines) and `iit-genai.md` (a 12-chapter, 78-section Generative AI course), under `Master_Rules.md`, Part III.1 (starting a course: generate the full structure first).
**Status:** one unified document: the curriculum structure with, inside every content unit, an NPTEL-style assignment and its key (collapsed), and a NumPy-first tooling guideline for from-scratch work (a default, not a prohibition; added 2026-11-03 at the learner's request). It replaces the earlier separate curriculum, assignments, answer-key and index files. Two courses were added the same day: Stochastic Approximation (units U5.9, U7.7, U8.16, U8.17, U10.6) and Approximation Algorithms (domain D17). Per Master Rules III.1.9, the learner may add, reorder or (as a recorded override) remove anything before teaching starts. Nothing here has been taught yet; every topic is "not started".

---

## How to read this document

1. **Parts and domains.** Five parts, 18 domains (D1–D18). Each domain has an aim, named benchmarks, and units.
2. **Units.** A unit (`U<domain>.<n>`) is a group of related topics. Each has: **Sources** (generated: which source course weeks or outline cells it absorbs), **Topics** (every topic and subtopic, merged across sources and kept close to the sources' own words), **Results** (the theorems and formulas it teaches, each with a proof status), **Build** (the from-scratch implementation, with the professional tool as oracle afterwards), and **Gap-fills** (anything the references cover that the outlines miss, labelled *inferred* with its source).
3. **Assignment and tooling.** Each content unit ends with its **Assignment** (`A<domain>.<n>`): five questions, with the key in a collapsed block that you open only after an attempt. The default tooling is stated once, in the course profile; a unit mentions tooling only where it departs from the default.
4. **Proof-status tags** on results: **[P]** prove in full; **[D]** derive with every step; **[S]** proof sketch (the reason a full proof is not given is stated); **[X]** stated, proof deferred (the unit that will prove it, or "beyond course scope", is named); **[Def]** definition, not proved (Master Rules 4.2, 4.7, III.1.5).
5. **Source keys** (e.g. `MFML`, `GEN`) are listed in Appendix A. `W3` means Week 3 of that course; `o` means the course's outline or about-text; `GEN 4.5` means GenAI section 4.5.
6. **Merging rule.** Where several courses cover the same ground (for example, linear algebra draws on 14 sources and optimization on 16), they are merged into one unit at the deepest source level, and every source week is cited. The overlap is the point of unifying.

## Course profile (Master Rules II.1)

| Item | Value |
|---|---|
| **Aim** | Expert-level command of the mathematics of ML, classical and deep ML, generative models, LLMs, RAG and agents, evaluation and safety, with the three habits of the contest solver, the researcher and the architect (Master Rules section 10). Every algorithm is also implemented from scratch. |
| **Starting level** | No prior knowledge assumed beyond school mathematics (Class XII) and basic Python. Everything else, including proof technique, is taught (Master Rules III.1.6). |
| **Benchmarks** | Named per domain in each domain's intro. Titles marked *recalled, not checked* have not been verified against the book itself. Appendix D lists what was checked. |
| **Learner's standing instructions (recorded as overrides, Master Rules 0.3)** | (1) From `nptel.txt`: "learn to implement these techniques from the scratch in python, numpy, etc." and "If there are no assignments provided for certain topics, then create them." (2) In chat, 2026-11-03: "Add assignments just like an academic/nptel course. I also need to learn from the scratch python implementations (numpy at maximum). Add this requirement too." (3) In chat, 2026-11-03, replacing the strict reading of (2): "The numpy only rule is not strict. It is more of a suggestion. Feel free to design as needed." (4) In chat, 2026-11-03: add the courses Stochastic Approximation and Approximation Algorithms to the curriculum and the files. Scope of all: the whole course, until revoked. Effects: every content unit has a **Build** written from scratch first, and an **Assignment** (NPTEL style); the tooling for each Build is a design choice, stated in the unit. |
| **Acceptance gates (6.7)** | Formatter clean (`ruff format --check`), linter clean (`ruff check`), `pytest` passes, gradient checks within 1e-5 against finite differences, and results within stated tolerance of an oracle. The optional import report (Assignment A0) lists imports beyond the default set so each is a conscious choice; it informs and never blocks. No hidden failure. |
| **Layer order for a topic (3.6)** | Concept and intuition → formal statement and derivation → from-scratch build → professional tool → real-world application and limits → check and close. |
| **Real-world lens (II.6)** | Name it, touch it in a lab, design with it. Cost tags: *local* for all from-scratch work; *replay-first, spend-capped* for any paid LLM API (Master Rules 11.2). |
| **Pacing (2.7, 8.5)** | The sources' durations (8 or 12 weeks, credits) describe their own pacing only. Here the learner advances by passing checks, never by the calendar. |
| **Order of languages and tools; from-scratch guideline (NumPy-first, flexible)** | (1) Write the algorithm you are learning by hand first. (2) Default toolbox: Python standard library + NumPy (+ Matplotlib for plots), because it keeps every step visible. (3) This is a **guideline, not a prohibition** (the learner's words: "not strict ... more of a suggestion"): where another library serves the learning goal better, the unit says so, and only units that depart from the default mention tooling (for example U11.4 uses PyTorch for transfer learning, U14.12 uses LangGraph, U16.2 uses PyTorch DDP, U17.7 may use `cvxpy`). (4) Libraries that implement the same algorithm (scikit-learn, SciPy solvers, PyTorch autograd) normally serve as oracles in a separate test file after your version passes, or as the practical tool afterwards (Master Rules 6.8). (5) Derive gradients by hand and check them by finite differences. (6) Keep models toy-sized so they train in minutes on a CPU. Optional environment task **A0** (not scored): create `scratch/` and `tests/oracle/`, write `grad_check(f, x)` returning the maximum relative error (target below 1e-6 on f(x) = sum(x**3)), and, if you want, an import report listing imports beyond the default set. The report informs and never blocks. |
| **Assignments (NPTEL style)** | One per content unit (148, A1.1–A17.7); capstones are projects with their own criteria. Five questions: MCQ (1 mark), multiple-select (2; all correct options and none wrong), numerical answer (2), prove or derive (2), programming (3); 10 marks. **Pass** at 7/10 with the derivation and the code both accepted (Master Rules 6.12). **Attempt before any hint**; hints escalate one notch at a time and only when asked: what structure do you see, then a smaller case, then the smallest useful hint, then the key (5.7). A missed question gets one smaller, reworded retry (6.5). **Predict first**: write a one-line prediction of Q5's outcome before running it, then report prediction, code and result (6.1, 6.4). **Keys** sit in a collapsed block under each assignment; numerical answers were computed by script, and the 148 programming questions are specs that were not run (you write the solutions; the tutor never does, 2.10, 6.13). **Source alignment:** each unit's Sources line says which official course weeks it absorbs, so an assignment can be set beside the matching official NPTEL weekly assignment if you fetch those (none were downloaded). **Domain exit:** a qualifying-style set drawn from the domain's assignments runs before its capstone (8.7, 9.5). **Recall:** missed questions are re-attempted cold at about 1, 3 and 7 days (8.2). |
| **Cross-domain capstones (9.6)** | U18.1–U18.7, one per stretch, then one integrated final capstone. |
| **Record** | The list of units in this document is the record template. Initial state: every unit not started, depth L0, no evidence; resume point U1.1, first block (proof paradigms). The live record (mastery states, misconception register, error log, heuristics catalogue, decision journal) belongs in your tracker file (Master Rules 8.3). The results inventory of Master Rules III.1.5 is the **Results** line of each unit. |

## Domain map

| Part | Domain | Units | Absorbs mainly |
|---|---|---|---|
| A. Mathematical foundations | D1 Discrete mathematics and reasoning | U1.1–U1.7 | DM, HEM, IM |
| | D2 Single-variable calculus and real analysis | U2.1–U2.5 | CAL1, EM1, AEMK, PMO |
| | D3 Multivariable and vector calculus | U3.1–U3.5 | EM1, EM2, AEMK, MFML, EMML |
| | D4 Linear algebra | U4.1–U4.11 | LAR, LAP, ALAB, ALAK, ALAJ, MFML, EMML |
| | D5 Probability and stochastic models | U5.1–U5.9 | IPS, PSS, MFML, AEMA, SMLM, S50, SA |
| | D6 Statistics and inference | U6.1–U6.6 | IPS, SMLM, S50, AEMA |
| | D7 Differential equations, complex analysis, transforms, numerics | U7.1–U7.7 | EM1, EM2, AEMK, AEMA, MM, SA |
| | D8 Optimization | U8.1–U8.17 | PMO, CVX, OFF, OAT, OMLH, AOW, LPCS, DOML, SA |
| B. Machine learning | D9 Classical ML, data mining, learning theory | U9.0–U9.14 | MLCE, MLDL, MLE, MLESA, FML, IMLK, MLK, DMIN, SMLM, GEN Ch.2 |
| | D10 Bandits and reinforcement learning | U10.1–U10.6 | BAN, MLESA, FDL, SA |
| C. Deep learning and generative AI | D11 Deep learning foundations | U11.1–U11.8 | FDL, MLDL, MLE, MFML, GEN Ch.2–3 |
| | D12 NLP, Transformers, LLMs | U12.1–U12.10 | GEN Ch.1, 3–7, DLNLP, FDL |
| | D13 Deep generative models | U13.1–U13.8 | MFGAI, FML, FDL |
| D. LLM applications, evaluation, safety | D14 RAG and agentic systems | U14.1–U14.15 | GEN Ch.8–11 |
| | D15 Evaluation, safety, responsible AI | U15.1–U15.6 | GEN Ch.7, 12, DLNLP |
| E. Algorithms, systems and integration | D16 ML systems and efficiency | U16.1–U16.6 | CSO, DOML |
| | D17 Approximation algorithms and computational complexity | U17.1–U17.7 | AA |
| | D18 Integration and capstones | U18.1–U18.7 | none (assembles all) |

## Default order (a plan, not a cage: Master Rules 3.3)

| Stage | Units | Why here |
|---|---|---|
| 0 | U1.1; D2 | Proof habits and one-variable analysis before anything that uses limits. |
| 1 | U4.1–U4.6; U3.1–U3.2; U5.1–U5.5 | Vectors, matrices, eigen-structure, gradients and the language of probability: the minimum that ML notation needs. |
| 2 | U4.7–U4.10; U5.6–U5.7; D6; U3.3–U3.5 | Decompositions, least squares, joint distributions, inference, matrix calculus. |
| 3 | U8.1–U8.8; U9.0–U9.4 | Optimization basics and the first ML models, built by hand: regression, logistic regression, regularization, evaluation. |
| 4 | U8.9–U8.13; U9.5–U9.14; U1.2–U1.6; D7 (except U7.7); D17 (after U8.7 and U8.11) | Duality, SVMs, kernels, trees, clustering, graphical models, learning theory; discrete structures and applied analysis as they are needed. |
| 5 | D11; U5.9; U7.7; U8.16–U8.17 | Deep learning (backpropagation uses U3.1, U3.5, U8.10); stochastic approximation explains why SGD and RL updates converge, and needs martingales (U5.9) and ODE limit sets (U7.7). |
| 6 | D12; D10 (U10.6 last) | Attention, Transformers, LLMs, then alignment (needs RL: U10.4–U10.5; U10.6 needs U8.16–U8.17). |
| 7 | D13 | Generative models (needs U5.6, U9.9, U9.10, U13.1 foundations, U7.5). |
| 8 | D14; D15 | RAG, agents, evaluation and safety. |
| 9 | D16; U8.14; D18 | Systems, distributed and federated learning, capstones. |

Just-in-time rule: a prerequisite from another domain is taught immediately before the topic that first uses it (Master Rules 3.3), and the stage table above is updated when that happens.

## Coverage guarantee: what was checked and how

- **Cells.** Every source week, outline, lecture-block and GenAI section is a "cell": 486 cells from `nptel.txt` and 78 from `iit-genai.md`, 564 in all. **All 564 are cited by at least one unit** (Appendix B lists the full matrix).
- **Atoms.** Each cell's text was split into 3,400+ topic atoms. A script checked that each atom's key words appear in the units that cite its cell. The atoms it still flags (listed in Appendix E) are **source typos** (for example "Grpah", "Dula", "diinensionality"), **section labels**, and **descriptive prose** (audience, marketing sentences), none of which is a topic.
- **Limits of the check.** It is a word-level check, not a proof of meaning; it cannot confirm that a topic is explained well. Outline prose was reviewed by hand once after the script ran.
- **Nothing was dropped to save space.** Overlapping courses are merged, never sampled. Repeated or truncated source text is flagged in Appendix E rather than silently fixed.

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

**Assignment A1.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Which formula is a tautology?

(A) p AND (NOT p)  
(B) (p -> q) OR (q -> p)  
(C) p XOR q  
(D) p -> (NOT p)

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are logically equivalent to p -> q?

(A) (NOT p) OR q  
(B) (NOT q) -> (NOT p)  
(C) q -> p  
(D) NOT (p AND (NOT q))

**Q3 (2 marks, numerical answer (functions)).** How many distinct Boolean functions of 3 variables exist?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove by induction that 1 + 2 + ... + n = n(n+1)/2 for all n >= 1, stating the base case, the inductive hypothesis and where it is used.

**Q5 (3 marks, programming).** Write truth_table_is_tautology(f, n) (f takes n Booleans) and dfa_run(delta, start, accepting, word). Enumerate inputs with NumPy. Acceptance: the tautology test accepts (p->q) or (q->p) and rejects p xor q; a DFA you design accepts exactly binary strings with an even number of 1s on 6 hand-picked words. Predict the number of rows enumerated for n=6.

<details><summary>Key for A1.1 (open only after your attempt)</summary>

- **Q1:** B. Either p implies q or q implies p in every row; the others fail for some assignment.
- **Q2:** ABD. The converse q -> p is not equivalent; the other three are the standard equivalent forms.
- **Q3:** 256 functions (tolerance ±0). Each of the 8 input rows independently takes value 0 or 1, so 2^8.
- **Q4 (marking outline):** Base n=1; assume for n; add n+1 to both sides and factor to (n+1)(n+2)/2.
- **Q5 (what a passing submission shows):** 64 rows enumerated; all stated tests pass; the DFA has two states.

</details>

### U1.2 Counting, generating functions and combinatorics
**Sources:** DM W2–3; IM A
- **Topics:** Counting; generating functions; basic combinatorics; counting principles (basic methods, the pigeonhole principle, the binomial theorem, permutations, graphs, recurrence relations, bijective proofs); polynomials in several variables and counting monomials.
- **Results:** Binomial theorem [P]; pigeonhole principle and generalized form [P]; inclusion–exclusion [P]; solution of linear recurrences by characteristic roots and by generating functions [D]; bijective proof of Vandermonde-type identities [P].
- **Build:** recurrence solver and coefficient extraction from power series using NumPy; brute-force verification of counting formulas on small cases.
- **Gap-fills:** *[inferred: Concrete Mathematics; Lovász]* ordinary and exponential generating functions, partitions, Catalan numbers, Stirling numbers, derangements, double counting.

**Assignment A1.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** How many distinct arrangements of the letters of BANANA exist?

(A) 720  
(B) 120  
(C) 60  
(D) 30

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which identities are true for all 0 <= k <= n?

(A) C(n,k) = C(n,n-k)  
(B) sum over k of C(n,k) = 2^n  
(C) C(n,k) = C(n-1,k) + C(n-1,k-1)  
(D) C(n,k) = n!/k!

**Q3 (2 marks, numerical answer (permutations)).** How many derangements (no fixed point) of 5 objects exist?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that the sum over k of C(n,k) equals 2^n twice: once by the binomial theorem and once by a bijection between subsets and binary strings.

**Q5 (3 marks, programming).** Using np.convolve on coefficient arrays, count the ways to make 50 cents from coins 1, 5, 10 and 25 (order irrelevant). Predict the answer first, then compare with a brute-force count you also write. Both must agree.

<details><summary>Key for A1.2 (open only after your attempt)</summary>

- **Q1:** C. 6!/(3! 2!) = 60.
- **Q2:** ABC. D omits the (n-k)! in the denominator.
- **Q3:** 44 permutations (tolerance ±0). Inclusion-exclusion: 5! (1 - 1 + 1/2 - 1/6 + 1/24 - 1/120) = 44.
- **Q4 (marking outline):** Set x=y=1 in (x+y)^n; each subset of an n-set corresponds to its indicator string of length n.
- **Q5 (what a passing submission shows):** 49 ways by generating-function product and by brute force.

</details>

### U1.3 Posets, lattices, Boolean algebra and switching circuits
**Sources:** DM W4; HEM W2–5
- **Topics:** Posets, chains and anti-chains; partially ordered sets I and II; duality and lattices as an algebraic system; sublattice I and II; Boolean algebra; switching algebra; Boolean functions; different representations of Boolean functions; circuit minimization and simplification (I and II); Karnaugh map I and II; table diagrams (of Boolean functions and of finite-state machines).
- **Results:** Dilworth's theorem [P]; Mirsky's theorem [P]; Boolean algebra axioms imply duality and De Morgan laws [P]; canonical (sum-of-products) form exists and is unique [P].
- **Build:** Quine–McCluskey minimizer from scratch; checked against hand Karnaugh-map reductions.
- **Gap-fills:** *[inferred: Rosen]* Hasse diagrams, Sperner's theorem, distributive and complemented lattices, Stone representation (statement).

**Assignment A1.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** In a partially ordered set, an antichain is a subset in which

(A) every two elements are comparable  
(B) no two distinct elements are comparable  
(C) there is a greatest element  
(D) the order is total

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are laws of Boolean algebra?

(A) x + xy = x  
(B) x + x' = 1  
(C) x x' = 1  
(D) x + yz = (x + y)(x + z)

**Q3 (2 marks, numerical answer (cells)).** In a 4-variable Karnaugh map, how many cells does the largest group representing a single-literal product term contain?

**Q4 (2 marks, prove or derive; every step with its reason).** From the Boolean algebra axioms, prove De Morgan's law (x + y)' = x' y' by showing x' y' is the complement of x + y and using uniqueness of complements.

**Q5 (3 marks, programming).** Implement prime_implicants(minterms, nvars) by Quine-McCluskey merging with NumPy bit operations. Acceptance: for minterms {0,1,2,5,6,7} on 3 variables it returns exactly six implicants; compare with the cover you find by hand on a Karnaugh map. Predict the count first.

<details><summary>Key for A1.3 (open only after your attempt)</summary>

- **Q1:** B. Antichain means pairwise incomparable.
- **Q2:** ABD. x x' = 0, so C is false.
- **Q3:** 8 cells (tolerance ±0). A single literal fixes one variable, leaving 3 free: 2^3 cells.
- **Q4 (marking outline):** Show (x+y)+x'y' = 1 and (x+y)x'y' = 0 by distributivity; uniqueness gives the result.
- **Q5 (what a passing submission shows):** Six: 00-, 0-0, -01, 1-1, 11-, -10.

</details>

### U1.4 Graph theory
**Sources:** DM W5–7; HEM W5–8
- **Topics:** Basic graph theory; various types of graph; tours, cycles, cliques, covers; Eulerian and Hamiltonian graphs; travelling salesman problem; vertex and edge connectivity; matrix representation of graphs (incidence and adjacency matrices); coloring, matching, planarity; planar graphs; Kuratowski's theorem; detection of planarity; Euler's formula; dual of a planar graph; colouring of graphs; chromatic numbers; four colour theorem; various types of graphs; dual of a planar graph.
- **Results:** Handshake lemma [P]; Euler's circuit theorem [P]; Euler's formula V−E+F=2 [P]; Kuratowski's theorem [X→proof deferred, stated with the two obstruction graphs]; five-colour theorem [P]; four-colour theorem [X]; Hall's marriage theorem [P]; König's theorem [P]; Menger / max-flow–min-cut [X→U8.6, proved there by LP duality].
- **Build:** graph class with adjacency/incidence matrices, BFS/DFS, bipartiteness and Euler-tour test; greedy and DSATUR colouring; TSP by dynamic programming (Held–Karp) at toy size.
- **Gap-fills:** *[inferred: West]* trees and spanning trees (Kruskal, Prim), shortest paths (Dijkstra), Dirac and Ore conditions, Ramsey's theorem, spectral graph theory (adjacency/Laplacian eigenvalues; link to U4.8 and to spectral clustering in U9.9).

**Assignment A1.4** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** A connected planar graph has 6 vertices and 9 edges. How many faces does it have?

(A) 3  
(B) 4  
(C) 5  
(D) 6

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are true?

(A) K5 is not planar  
(B) K3,3 is not planar  
(C) Every planar graph is 4-colourable  
(D) A graph with an Euler circuit has all degrees odd

**Q3 (2 marks, numerical answer (edges)).** How many edges does the complete graph K8 have?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove the handshake lemma (sum of degrees = 2E) and deduce that the number of odd-degree vertices is even.

**Q5 (3 marks, programming).** Write is_bipartite(adj) using BFS two-colouring on a NumPy adjacency matrix, and has_euler_circuit(adj) using connectivity and degree parity. Acceptance: C5 not bipartite, C6 bipartite, K3,3 bipartite; K4 has no Euler circuit and C6 has one. Predict each answer first.

<details><summary>Key for A1.4 (open only after your attempt)</summary>

- **Q1:** C. Euler: V - E + F = 2 gives F = 5.
- **Q2:** ABC. An Euler circuit needs all degrees even.
- **Q3:** 28 edges (tolerance ±0). C(8,2) = 28.
- **Q4 (marking outline):** Each edge contributes 2 to the degree sum; an even sum forces an even count of odd terms.
- **Q5 (what a passing submission shows):** C5 False, C6 True, K3,3 True; K4 False, C6 True.

</details>

### U1.5 Number theory and cryptography
**Sources:** DM W8–9; IM A
- **Topics:** Basic number theory; elementary number theory (modular arithmetic, divisibility, prime numbers); density of primes; cryptography.
- **Results:** Euclid's algorithm and Bézout's identity [P]; fundamental theorem of arithmetic [P]; Chinese remainder theorem [P]; Fermat's little theorem and Euler's theorem [P]; infinitude of primes [P]; Chebyshev-type density bounds [S]; prime number theorem [X]; correctness of RSA [P].
- **Build:** extended Euclid, fast modular exponentiation, Miller–Rabin and toy RSA from scratch. Hand-built cryptography is for learning only and is never deployed (Master Rules 6.8).
- **Gap-fills:** *[inferred: Hardy–Wright; Rosen]* primality tests, Diffie–Hellman, discrete logarithm, hashing as modular arithmetic.

**Assignment A1.5** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What is 3^100 mod 7?

(A) 1  
(B) 2  
(C) 4  
(D) 5

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) gcd(a,b) divides ax + by for all integers x, y  
(B) If prime p divides ab then p divides a or b  
(C) phi(n) = n - 1 for every n > 1  
(D) The Chinese remainder theorem needs pairwise coprime moduli

**Q3 (2 marks, numerical answer).** Compute Euler's totient phi(36).

**Q4 (2 marks, prove or derive; every step with its reason).** Prove Fermat's little theorem: for prime p and p not dividing a, a^(p-1) = 1 mod p, by multiplying the residues 1..p-1 by a.

**Q5 (3 marks, programming).** Implement ext_gcd, modinv, modpow (square and multiply) and miller_rabin with plain integer code (NumPy optional, for testing arrays of inputs). Acceptance: modinv(3,11)=4; modpow(7,560,561)=1 while miller_rabin(561) is False; toy RSA with p=61, q=53, e=17 recovers a message. Never deploy hand-built cryptography.

<details><summary>Key for A1.5 (open only after your attempt)</summary>

- **Q1:** C. 3^6 = 1 mod 7 and 100 = 4 mod 6, so 3^4 = 81 = 4 mod 7.
- **Q2:** ABD. phi(n) = n - 1 only for prime n.
- **Q3:** 12 (tolerance ±0). Count integers up to 36 coprime to 36: 12.
- **Q4 (marking outline):** a, 2a, ..., (p-1)a is a permutation of 1..p-1 mod p; equate the products and cancel (p-1)!.
- **Q5 (what a passing submission shows):** modinv(3,11)=4; 561 (a Carmichael number) is rejected; RSA round trip succeeds.

</details>

### U1.6 Algebra: finite fields, codes, groups and orbit counting
**Sources:** DM W10–12
- **Topics:** Finite fields; codes; basic group theory; orbit counting; normal subgroups.
- **Results:** Lagrange's theorem [P]; existence and uniqueness of finite fields of order p^n [S]; Hamming bound and distance of linear codes [P]; orbit–stabilizer theorem [P]; Burnside's lemma [P]; first isomorphism theorem for groups [P].
- **Build:** GF(2^m) arithmetic; Hamming and Reed–Solomon encoder/decoder at toy size; Burnside-count of necklaces by enumeration versus formula.
- **Gap-fills:** *[inferred: Artin; MacWilliams–Sloane]* cyclic groups, permutation groups (link to U4.5 signature of a permutation), quotient groups, BCH codes.

**Assignment A1.6** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** A group of order 12 can have a subgroup of order

(A) 5  
(B) 7  
(C) 8  
(D) 6

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) A field with 8 elements exists  
(B) A field with 6 elements exists  
(C) The Hamming (7,4) code corrects any single-bit error  
(D) The minimum distance of the Hamming (7,4) code is 3

**Q3 (2 marks, numerical answer (necklaces)).** Using Burnside's lemma, how many distinct necklaces of 4 beads in 2 colours exist under rotation?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove the orbit-stabilizer theorem: for a group G acting on X, abs(orbit of x) times abs(stabilizer of x) equals abs(G).

**Q5 (3 marks, programming).** Implement gf8_mul over GF(2^3) with modulus x^3 + x + 1 using bit operations, then a Hamming(7,4) encoder and single-error corrector. Acceptance: gf8_mul(3,5)=4; flipping any one of 7 bits of any of the 16 codewords is corrected. Predict gf8_mul(3,5) first.

<details><summary>Key for A1.6 (open only after your attempt)</summary>

- **Q1:** D. Lagrange: the subgroup order must divide 12; only 6 does.
- **Q2:** ACD. Finite field orders are prime powers, so 6 is impossible.
- **Q3:** 6 necklaces (tolerance ±0). Rotations fix 16, 2, 4, 2 colourings; the average is 6.
- **Q4 (marking outline):** The map gStab -> g.x is a bijection from left cosets of the stabilizer to the orbit.
- **Q5 (what a passing submission shows):** gf8_mul(3,5)=4 and 16 x 7 = 112 single-bit errors are all corrected.

</details>

### U1.7 An invitation to mathematics: polynomials, functions, matrices, conservation laws
**Sources:** IM o, A
- **Topics:** Polynomials (interpolation, Taylor's formula, polynomials with integer values, polynomials in several variables, counting monomials); functions (continuous functions, the intermediate value property and its applications, fixed points, linear transformations of the plane, the derivative and dilations, higher-order derivatives and the binomial theorem, polynomial approximation to functions); matrices (matrices and transformations, multiplication versus composition, determinants as dilation factors, polynomials applied to matrices, matrices in probability theory, matrices in polynomial interpolation, the Vandermonde determinant); conservation laws (invariants of transformations, discrete transformations and applications, transformations in Euclidean geometry, circle inversions); elementary number theory (modular arithmetic, divisibility, prime numbers).
- **Results:** Lagrange interpolation uniqueness [P]; intermediate value theorem [P in U2.2]; Vandermonde determinant [D]; invariants as proof tool [P].
- **Build:** interpolation and Vandermonde solve in NumPy, with condition-number growth observed (bridge to U4.9).
- **Gap-fills:** this unit is a conceptual bridge; each theme is taught again at depth in D2, D4 and D1.5.

**Assignment A1.7** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** A polynomial of degree at most n passing through n+1 points with distinct x-values is

(A) not guaranteed to exist  
(B) unique  
(C) non-unique  
(D) only unique if n is even

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which follow from the intermediate value theorem?

(A) Every cubic polynomial has a real root  
(B) Every continuous f from [0,1] to [0,1] has a fixed point  
(C) Every continuous function is differentiable  
(D) The equation cos x = x has a solution

**Q3 (2 marks, numerical answer).** Compute the Vandermonde determinant for nodes 1, 2, 4.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that every continuous f from [0,1] to [0,1] has a fixed point by applying the intermediate value theorem to g(x) = f(x) - x.

**Q5 (3 marks, programming).** Build the Vandermonde matrix for n equally spaced nodes on [-1,1], interpolate 1/(1+25x^2) and report the maximum error on a fine grid and the condition number for n = 5, 10, 15, 20. Predict the trend first.

<details><summary>Key for A1.7 (open only after your attempt)</summary>

- **Q1:** B. The Vandermonde system is nonsingular for distinct nodes.
- **Q2:** ABD. Continuity does not imply differentiability.
- **Q3:** 6 (tolerance ±0). Product over pairs of (xj - xi) = 1*3*2 = 6.
- **Q4 (marking outline):** g(0) >= 0 and g(1) <= 0; IVT gives a zero of g.
- **Q5 (what a passing submission shows):** Error first falls then grows near the ends (Runge); condition number grows exponentially with n.

</details>

## D2. Single-Variable Calculus and Real Analysis

Aim: a rigorous single-variable calculus (Spivak-style) plus the analysis vocabulary that optimization, probability and learning theory later use. Benchmarks (recalled, not checked): Spivak, *Calculus*; Thomas–Finney, *Calculus and Analytic Geometry*; Cheney, *Analysis for Applied Mathematics*; Rudin, *Principles of Mathematical Analysis*.

### U2.1 Numbers, countability, functions, limits and continuity
**Sources:** CAL1 W1–2, o; PMO W1–2; OFF W1
- **Topics:** Introduction to numbers; countability and uncountability; examples of irrational numbers; functions; limits of functions I and II; continuous functions; intermediate value theorem; maximum value theorem; supremum and infimum; sets in Rn (balls, neighbourhood, interior point, open sets, closed sets, bounded sets, compact sets, level sets, epigraphs); supremum and infimum of a set; sequence, subsequence, limsup and liminf; order of convergence of a sequence; limit, continuity, uniform continuity and Lipschitz continuity and their geometries; overview of real analysis.
- **Results:** Uncountability of the reals (diagonal argument) [P]; completeness (least upper bound) [Def]; intermediate value theorem [P]; extreme value (maximum value) theorem [P]; Bolzano–Weierstrass [P]; Heine–Borel for Rn [S].
- **Build:** bisection and ε–δ explorers in Python; numerical estimation of convergence order from an error sequence.
- **Gap-fills:** *[inferred: Spivak; Cheney]* metric spaces and normed spaces (needed by D4 norms and D8), Cauchy sequences, completeness of Rn.

**Assignment A2.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Which set is uncountable?

(A) The rationals  
(B) The integers squared Z x Z  
(C) The interval (0,1)  
(D) The algebraic numbers

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Every Cauchy sequence of reals converges  
(B) Every bounded monotone sequence converges  
(C) Every bounded sequence converges  
(D) A continuous function on [a,b] attains its maximum

**Q3 (2 marks, numerical answer).** For f(x) = 3x + 1 at x = 2, what is the largest delta that works in the epsilon-delta definition for epsilon = 0.06?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that the interval (0,1) is uncountable using Cantor's diagonal argument.

**Q5 (3 marks, programming).** Write estimate_order(errors) returning the slope p fitted to log e_{k+1} against log e_k. Apply it to Newton iterates for sqrt(2) and to bisection errors. Predict both orders first.

<details><summary>Key for A2.1 (open only after your attempt)</summary>

- **Q1:** C. Cantor's diagonal argument; the others are countable.
- **Q2:** ABD. Bounded sequences such as (-1)^n need not converge.
- **Q3:** 0.02 (tolerance ±0.001). abs(f(x) - 7) = 3 abs(x - 2) < 0.06 iff abs(x - 2) < 0.02.
- **Q4 (marking outline):** Assume a list of decimal expansions; build a number differing from the nth in the nth digit (avoiding 0 and 9 runs); it is missing from the list.
- **Q5 (what a passing submission shows):** About 2 for Newton and about 1 for bisection.

</details>

### U2.2 Differentiation and mean value theorems
**Sources:** CAL1 W3–4; EM1 W1, o; AEMK W1; PMO W2
- **Topics:** Derivative of a function; rules of differentiation; derivatives, maxima and minima; Rolle's theorem and Lagrange MVT (mean-value theorem); Cauchy's mean value theorem; differentiability; monotonic functions and inverse function; differential calculus of functions of one variable; indeterminate forms; Newton's method for solving equations; optimization problems; little-oh and big-Oh notations.
- **Results:** Rolle and Lagrange mean value theorems [P]; Cauchy mean value theorem [P]; L'Hôpital's rule (indeterminate forms) [P]; inverse function theorem in one variable [P]; first and second derivative tests [P]; local quadratic convergence of Newton's method [D].
- **Build:** Newton and secant solvers from scratch, with the error curve plotted against the predicted order (links to U8.8).
- **Gap-fills:** *[inferred: Thomas–Finney]* related rates and curve sketching as applied optimization problems.

**Assignment A2.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Newton's method for f(x) = x^2 - 2 starting at x0 = 1 gives x1 =

(A) 1.25  
(B) 1.5  
(C) 1.75  
(D) 2

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Rolle's theorem is a special case of the mean value theorem  
(B) The mean value theorem needs continuity on [a,b] and differentiability on (a,b)  
(C) f'(c)=0 always means a local extremum at c  
(D) If f' > 0 on an interval then f is increasing there

**Q3 (2 marks, numerical answer).** Newton's method for x^2 - 2 from x0 = 1.5: compute x2 (one more step after 1.5).

**Q4 (2 marks, prove or derive; every step with its reason).** Prove the Lagrange mean value theorem from Rolle's theorem by applying Rolle to g(x) = f(x) - f(a) - (f(b)-f(a))(x-a)/(b-a).

**Q5 (3 marks, programming).** Implement bisection, Newton and secant solvers returning (root, iterations). Solve cos x = x. Acceptance: root 0.7390851332 to 1e-10; Newton from 1.0 needs at most 6 iterations. Predict the iteration counts of all three first.

<details><summary>Key for A2.2 (open only after your attempt)</summary>

- **Q1:** B. x1 = 1 - (1 - 2)/2 = 1.5.
- **Q2:** ABD. f(x)=x^3 has f'(0)=0 without an extremum.
- **Q3:** 1.417 (tolerance ±0.0001). x2 = 1.5 - 0.25/3 = 1.41667.
- **Q4 (marking outline):** g(a)=g(b)=0, so g'(c)=0 which rearranges to the MVT.
- **Q5 (what a passing submission shows):** Newton about 4-5, secant about 6, bisection about 34 iterations for 1e-10.

</details>

### U2.3 Integration, applications and transcendental functions
**Sources:** CAL1 W4–7; EM1 o; AEMK W2
- **Topics:** Integration I, II, III in the style and spirit of Newton and Leibnitz; indefinite integrals; integration by parts; integration of rational functions; trapezoidal rule for evaluating a definite integral; Simpson's rule for evaluating a definite integral; applications of definite integral I–IV; transcendental functions I and II; surface and volume of revolution; calculation of centre of gravity and centre of mass; area and volume as integrals.
- **Results:** Fundamental theorem of calculus (both parts) [P]; integrability of continuous functions [S]; error bounds for trapezoid and Simpson rules [D]; properties of exp and log from their integral definition [P].
- **Build:** trapezoid, Simpson and adaptive quadrature in NumPy, checked against `scipy.integrate`.
- **Gap-fills:** *[inferred: Thomas–Finney]* partial fractions procedure and trigonometric substitutions; Riemann sums and the Riemann–Darboux definition.

**Assignment A2.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The integral of x e^x from 0 to 1 equals

(A) 1  
(B) e - 1  
(C) e  
(D) 2

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Simpson's rule is exact for cubic polynomials  
(B) The trapezoid rule is exact for linear functions  
(C) d/dx of the integral of f from a to x equals f(x) for continuous f  
(D) Every continuous function has an elementary closed-form antiderivative

**Q3 (2 marks, numerical answer).** Trapezoid rule with n = 4 intervals for the integral of x^2 on [0,1].

**Q4 (2 marks, prove or derive; every step with its reason).** Prove the fundamental theorem of calculus, part 2: if F' = f with f continuous on [a,b] then the integral of f equals F(b) - F(a), using part 1.

**Q5 (3 marks, programming).** Implement composite trapezoid and Simpson rules and an adaptive Simpson routine. Integrate sin on [0, pi] (exact value 2). Acceptance: when n doubles, the error ratio is about 4 for trapezoid and about 16 for Simpson. Predict both ratios first.

<details><summary>Key for A2.3 (open only after your attempt)</summary>

- **Q1:** A. Integrate by parts: [x e^x - e^x] from 0 to 1 = 0 - (-1) = 1.
- **Q2:** ABC. e^(-x^2) is continuous with no elementary antiderivative.
- **Q3:** 0.3438 (tolerance ±0.0001). h/2 (f0 + 2 f1 + 2 f2 + 2 f3 + f4) = 0.34375.
- **Q4 (marking outline):** G(x)=integral from a to x of f has G'=f; F-G is constant; evaluate at a and b.
- **Q5 (what a passing submission shows):** Ratios near 4 and 16.

</details>

### U2.4 Taylor expansion, sequences, series and power series
**Sources:** CAL1 W7–8; EM1 o; AEMK W1; MFML W9; PMO W2
- **Topics:** Taylor's expansion I and II; Taylor's and Maclaurin's theorems and series; infinite sequence I and II; infinite series and their convergence; tests for convergence of a series; absolute and conditional convergence; power series; Taylor's theorem with remainder in little-o and big-O form; historical development of the calculus.
- **Results:** Taylor's theorem with Lagrange remainder [P]; ratio, root and comparison tests [P]; Abel/radius-of-convergence theorem (Cauchy–Hadamard) [P]; Rearrangement of conditionally convergent series (Riemann) [S].
- **Build:** Taylor polynomials of exp, sin, log with error versus remainder bound.
- **Gap-fills:** *[inferred: Spivak]* uniform convergence of series (needed in D7 Fourier and complex analysis).

**Assignment A2.4** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The radius of convergence of the series sum of x^n / n! is

(A) 0  
(B) 1  
(C) e  
(D) infinity

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which series converge?

(A) Sum of 1/n^2  
(B) Sum of 1/n  
(C) Sum of (-1)^n / n  
(D) Sum of 1/n!

**Q3 (2 marks, numerical answer).** Evaluate the degree-3 Maclaurin polynomial of e^x at x = 0.5.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove the ratio test: if the limit of abs(a_{n+1}/a_n) is L < 1 then the series converges absolutely.

**Q5 (3 marks, programming).** Write taylor_poly(coeffs, x) and compare Taylor polynomials of sin at 0 of degree 1 to 9 against the Lagrange remainder bound at x = 1. Acceptance: the observed error never exceeds the bound. Predict which degree first achieves 1e-6.

<details><summary>Key for A2.4 (open only after your attempt)</summary>

- **Q1:** D. The ratio of consecutive terms tends to 0 for every x.
- **Q2:** ACD. The harmonic series diverges; the alternating harmonic series converges conditionally.
- **Q3:** 1.646 (tolerance ±0.0001). 1 + 0.5 + 0.125 + 0.0208333 = 1.64583.
- **Q4 (marking outline):** Pick r with L<r<1; eventually abs(a_{n+1}) <= r abs(a_n), so terms are dominated by a geometric series.
- **Q5 (what a passing submission shows):** Degree 9 (error about 2.8e-6 for degree 7, below 1e-6 at degree 9).

</details>

### U2.5 Improper integrals, Gamma and Beta functions, integrals dependent on parameters
**Sources:** EM1 W5, o; AEMK W2
- **Topics:** Improper integrals; convergence of improper integral; tests of convergence; Gamma and Beta functions and their properties; differentiation under the integral sign; Leibnitz rule of differentiation; integrals dependent on parameters and applications.
- **Results:** Comparison and limit-comparison tests for improper integrals [P]; Γ(n+1)=nΓ(n) and the Beta–Gamma relation [P]; Leibniz rule [P under uniform-convergence conditions].
- **Build:** numerical evaluation of Γ and B and moment integrals used later in D5 (Gamma, Beta and normal densities).
- **Gap-fills:** *[inferred: Kreyszig]* Gaussian integral (needed for D5 normal distribution).

**Assignment A2.5** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The value of the Gamma function at 1/2 is

(A) 1  
(B) sqrt(pi)  
(C) pi  
(D) 1/2

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which improper integrals converge?

(A) Integral from 1 to infinity of x^-2 dx  
(B) Integral from 0 to 1 of 1/x dx  
(C) Integral from 0 to 1 of x^(-1/2) dx  
(D) Integral from 1 to infinity of 1/x dx

**Q3 (2 marks, numerical answer).** Compute the Beta function B(2,3).

**Q4 (2 marks, prove or derive; every step with its reason).** Prove Gamma(n+1) = n Gamma(n) for n > 0 by integration by parts.

**Q5 (3 marks, programming).** Compute Gamma(x) for x = 0.5, 1, 2.5 by numerical integration with a change of variables handling the endpoint singularity. Acceptance: relative error below 1e-6 against the closed forms sqrt(pi), 1 and 1.5 sqrt(pi)/2 (computed by hand). Predict which x is hardest.

<details><summary>Key for A2.5 (open only after your attempt)</summary>

- **Q1:** B. Gamma(1/2) equals the Gaussian integral over the half-line scaled to sqrt(pi).
- **Q2:** AC. The 1/x integrals diverge logarithmically.
- **Q3:** 0.08333 (tolerance ±0.0001). Gamma(2)Gamma(3)/Gamma(5) = 1*2/24 = 1/12.
- **Q4 (marking outline):** Integrate t^n e^-t by parts; the boundary term vanishes and the remaining integral is n Gamma(n).
- **Q5 (what a passing submission shows):** x = 0.5 is hardest because of the integrable singularity at 0.

</details>

## D3. Multivariable and Vector Calculus

Aim: derivatives, integrals and fields in several variables, the machinery behind gradients, Jacobians, Hessians and backpropagation. Benchmarks (recalled, not checked): Thomas' Calculus; Kreyszig, *Advanced Engineering Mathematics*; Piskunov, *Differential and Integral Calculus*; Deisenroth et al., *Mathematics for Machine Learning*, Ch. 5.

### U3.1 Functions of several variables, partial derivatives and differentiability
**Sources:** EM1 W2–3, o; AEMK W1, o; MFML W9; EMML W7; PMO W1–2; OMLH W1–2
- **Topics:** Functions of several variables; limit and continuity; partial derivatives and their geometrical interpretation; total differential and differentiability; derivatives of composite and implicit functions; implicit function theorem; derivatives of higher order and their commutativity; Euler's theorem on homogeneous functions; partial derivative, gradient, Hessian, directional derivative; differentiability and the hierarchy of partial derivatives, directional derivatives and differentiability; chain rule; gradient, Jacobian and Hessian; change of variables; vector calculus; basic concepts of calculus; tools from calculus of several variables; hierarchy of PDs (partial derivatives), DD (directional derivatives) and differentiability.
- **Results:** Equality of mixed partials (Schwarz/Clairaut) [P]; chain rule in several variables [P]; differentiability implies directional derivatives and continuity, with the converse counterexamples [P]; implicit function theorem [S, proof sketch via contraction mapping]; Euler's homogeneous function theorem [P].
- **Build:** numerical gradient and Jacobian checker (finite differences) and tape-based reverse-mode differentiation from scratch (bridge to U11.2 backpropagation).
- **Gap-fills:** *[inferred: MML Ch.5]* gradients of vector-valued functions, gradients of matrices, useful identities, automatic differentiation (forward and reverse mode).

**Assignment A3.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The gradient of f(x,y) = x^2 y at (1,2) is

(A) (2,1)  
(B) (4,1)  
(C) (4,2)  
(D) (1,4)

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Mixed second partials are equal when they are continuous  
(B) A differentiable function is continuous  
(C) Existence of all partial derivatives implies differentiability  
(D) A differentiable function has all directional derivatives

**Q3 (2 marks, numerical answer).** Directional derivative of f = x^2 y at (1,2) in the direction (3,4)/5.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that if f is differentiable at a then the directional derivative along a unit vector u equals the gradient dotted with u.

**Q5 (3 marks, programming).** Implement num_grad and num_jacobian by central differences and a small tape-based reverse-mode differentiator supporting add, mul, sin, square. Acceptance: for f(x) = sin(x1 x2) + x2^2 the tape gradient matches central differences to 1e-8 at three random points. Predict the gradient at (1, 2) first.

<details><summary>Key for A3.1 (open only after your attempt)</summary>

- **Q1:** B. (2xy, x^2) = (4, 1).
- **Q2:** ABD. Partials can exist at a point where the function is not even continuous.
- **Q3:** 3.2 (tolerance ±0.0001). Gradient (4,1) dotted with (0.6, 0.8) = 3.2.
- **Q4 (marking outline):** Apply the chain rule to g(t) = f(a + t u) at t = 0.
- **Q5 (what a passing submission shows):** Gradient (2 cos 2, cos 2 + 4) = about (-0.832, 3.584).

</details>

### U3.2 Taylor expansion in several variables, maxima, minima and Lagrange multipliers
**Sources:** EM1 W4, o; AEMK W1; MFML W9
- **Topics:** Taylor's expansion of functions of several variables; Taylor's series with gradient and Hessian terms; maxima and minima; saddle points; constrained maxima/minima problems using Lagrange's method of multipliers.
- **Results:** Second-order Taylor expansion with remainder [P]; second-derivative test via Hessian definiteness [P]; Lagrange multiplier rule for equality constraints [D]; KKT conditions [X→U8.5].
- **Build:** Newton step on a two-variable function, with Hessian eigenvalues classifying the stationary point.

**Assignment A3.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The origin is a stationary point of f(x,y) = x^2 - y^2. It is

(A) a local minimum  
(B) a local maximum  
(C) a saddle point  
(D) not stationary

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) A positive definite Hessian at a stationary point gives a strict local minimum  
(B) An indefinite Hessian gives a saddle  
(C) A positive semidefinite Hessian guarantees a local minimum  
(D) f(x) = x^4 has a minimum at 0 although f''(0) = 0

**Q3 (2 marks, numerical answer).** Maximum value of x + y subject to x^2 + y^2 = 2.

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the Lagrange condition grad f = lambda grad g for a constrained stationary point by showing grad f must be orthogonal to the tangent space of g = 0.

**Q5 (3 marks, programming).** For f(x,y) = x^3 - 3x + y^2 find stationary points by Newton's method on the gradient and classify them from Hessian eigenvalues. Acceptance: (1,0) is a minimum and (-1,0) a saddle. Predict the eigenvalues of the Hessian at (1,0) first.

<details><summary>Key for A3.2 (open only after your attempt)</summary>

- **Q1:** C. The Hessian diag(2,-2) is indefinite.
- **Q2:** ABD. PSD alone is inconclusive (x^3 at 0).
- **Q3:** 2 (tolerance ±0.001). Lagrange: x = y = 1 gives the maximum 2.
- **Q4 (marking outline):** Along any feasible curve, d/dt f = grad f . velocity = 0; tangents span the null space of grad g, so grad f is in the span of grad g.
- **Q5 (what a passing submission shows):** Eigenvalues 6 and 2 at (1,0); -6 and 2 at (-1,0).

</details>

### U3.3 Multiple integrals and their applications
**Sources:** EM1 W6–7, o; AEMK W2
- **Topics:** Double and triple integrals; multiple integrals and their properties; change of order of integration; change of variables; Jacobian transformation; Fubini theorem; surface, area and volume integrals; applications of multiple integrals.
- **Results:** Fubini's theorem [S, statement and conditions]; change-of-variables formula with Jacobian determinant [S; derived for linear maps in U4.5]; polar/spherical coordinates [D].
- **Build:** Monte Carlo and grid evaluation of double integrals (forward link to D5 Monte Carlo).

**Assignment A3.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The double integral of x y over the unit square is

(A) 1/4  
(B) 1/2  
(C) 1  
(D) 1/8

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Fubini's theorem applies to a continuous function on a rectangle  
(B) The Jacobian of polar coordinates is r  
(C) Changing the order of integration never changes the value  
(D) Spherical coordinates use rho^2 sin(phi) as Jacobian

**Q3 (2 marks, numerical answer).** Integral of r^2 over the unit disk (use polar coordinates).

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the polar-coordinate Jacobian r by computing the determinant of the partial-derivative matrix of (x,y) = (r cos t, r sin t).

**Q5 (3 marks, programming).** Estimate the integral of x^2 over the unit disk by Monte Carlo with N = 10^2, 10^4, 10^6 uniform points in the bounding square. Acceptance: the true value pi/4 lies within 3 standard errors, and the error shrinks like 1/sqrt(N). Predict the error at N = 10^6.

<details><summary>Key for A3.3 (open only after your attempt)</summary>

- **Q1:** A. (1/2)(1/2) = 1/4.
- **Q2:** ABD. Order can matter if the function is not absolutely integrable.
- **Q3:** 1.571 (tolerance ±0.001). Integral of r^2 * r dr dtheta = 2 pi * 1/4 = pi/2.
- **Q4 (marking outline):** det of [[cos t, -r sin t],[sin t, r cos t]] = r.
- **Q5 (what a passing submission shows):** Error about 1e-3; value about 0.785.

</details>

### U3.4 Vector calculus: fields, line and surface integrals, Green, Gauss and Stokes
**Sources:** EM2 W1–2, o; AEMK W9–11
- **Topics:** Vector and scalar fields; level surface; limit, continuity and differentiability of vector functions; curve and arc length; unit vectors; directional derivatives; divergence, gradient and curl; some applications to mechanics; tangent, normal and binormal; Serret–Frenet formulae; line integral; parametric representations; surface integral; volume integral; line and surface integrals; Green's, Gauss' divergence and Stokes' theorems; vector and scalar fields; limit, continuity and differentiability of vector functions; directional derivative, gradient, curl, divergence; line and surface integrals; Green, Gauss and Stokes theorems.
- **Results:** Green's theorem [P for simple regions]; divergence (Gauss) theorem [S]; Stokes' theorem [S]; conservative-field criterion [P]; Frenet–Serret equations [D].
- **Build:** numerical line and flux integrals; verification of Green/Gauss on a test field.
- **Gap-fills:** *[inferred: Kreyszig]* Laplacian and harmonic functions (links to D7 complex analysis); divergence of vector fields as it reappears in D13 continuity and Fokker–Planck equations.

**Assignment A3.4** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The curl of a gradient field is

(A) the divergence  
(B) zero  
(C) the Laplacian  
(D) a scalar

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Green's theorem is the planar case of Stokes' theorem  
(B) The divergence of a curl is zero  
(C) The curl of a gradient is zero  
(D) Gauss' theorem equates the flux through a closed surface with the volume integral of the curl

**Q3 (2 marks, numerical answer).** Divergence of F = (x^2, y^2, z^2) at (1,2,3).

**Q4 (2 marks, prove or derive; every step with its reason).** Prove Green's theorem for a rectangle by evaluating both sides of the integral of (Q_x - P_y) as iterated integrals.

**Q5 (3 marks, programming).** Compute the circulation of F = (-y, x) around the unit circle by parametrization and NumPy trapezoid, and the double integral of curl F over the disk by a grid. Acceptance: both equal 2 pi within 1e-6 and 1e-3. Predict the value first.

<details><summary>Key for A3.4 (open only after your attempt)</summary>

- **Q1:** B. curl grad f = 0 for twice continuously differentiable f.
- **Q2:** ABC. Gauss' theorem uses the divergence, not the curl.
- **Q3:** 12 (tolerance ±0.001). 2x + 2y + 2z = 12.
- **Q4 (marking outline):** Split into the integral of Q_x (x outer) and of -P_y; apply the fundamental theorem in one variable; match boundary segments.
- **Q5 (what a passing submission shows):** 2 pi = 6.283 on both sides.

</details>

### U3.5 Matrix calculus, Jacobians and Hessians for machine learning
**Sources:** MFML W10; EMML W7–8
- **Topics:** Matrix derivatives; basic concepts of calculus, gradient, Jacobian, chain rule, change of variables; calculus in Python; Jacobian and Hessian of scalar and vector functions of matrices.
- **Results:** Gradients of trace, quadratic form and log-determinant [D]; chain rule in matrix form for a two-layer network [D].
- **Build:** NumPy autodiff-checking of every matrix-derivative identity against finite differences.
- **Gap-fills:** *[inferred: MML Ch.5; Petersen–Pedersen Matrix Cookbook]* gradients of the least-squares loss and softmax cross-entropy used in D9 and D11.

**Assignment A3.5** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The gradient of x^T A x with respect to x is

(A) A x  
(B) (A + A^T) x  
(C) A^T x  
(D) 2 A x always

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which matrix-calculus identities are correct?

(A) Gradient of the squared norm of (W x - y) with respect to W is 2 (W x - y) x^T  
(B) Gradient of log det X with respect to X is X^(-T)  
(C) Derivative of trace(A X) with respect to X is A  
(D) Gradient of softmax cross-entropy with respect to logits is p - y

**Q3 (2 marks, numerical answer).** Sum of the components of grad (x^T A x) at x = (1,1) for A = [[2,1],[0,3]].

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the gradient of the least-squares loss norm(X w - y) squared with respect to w and the normal equations.

**Q5 (3 marks, programming).** Write check_identity(f, grad_f, x) using central differences and verify the three gradient identities for x^T A x, log det of a random SPD matrix, and softmax cross-entropy. Acceptance: relative error below 1e-6 for each. Predict whether the log det check needs a symmetric perturbation.

<details><summary>Key for A3.5 (open only after your attempt)</summary>

- **Q1:** B. It equals 2Ax only for symmetric A.
- **Q2:** ABD. The derivative of trace(AX) is A^T.
- **Q3:** 12 (tolerance ±0.001). (A + A^T) x = (5,7), sum 12.
- **Q4 (marking outline):** Expand to w^T X^T X w - 2 w^T X^T y + y^T y; gradient 2 X^T (X w - y); set to zero.
- **Q5 (what a passing submission shows):** All three pass; the log det gradient is checked with symmetric perturbations.

</details>

## D4. Linear Algebra: Core, Abstract, Numerical and Applied

Aim: five source courses (basic, abstract/coordinate-free, advanced canonical forms, numerical/applied for ML, signal-processing applications) merged into one ladder: computation first, then structure, then decompositions, then applications. Benchmarks (recalled, not checked): Strang, *Introduction to Linear Algebra* (5th ed.) and *Learning from Data*; Axler, *Linear Algebra Done Right* (3rd ed.); Hoffman–Kunze; Halmos; Artin; Greub; Jacobson; Deisenroth et al. Ch. 2–4; Trefethen–Bau, *Numerical Linear Algebra*; Golub–Van Loan.

### U4.1 Systems of linear equations, matrices, elimination, rank and inverses
**Sources:** LAR W1–4, o; LAP W2,9; ALAB o, P1; EM1 W8, o; AEMK W6–7; EMML W1, o; MFML W1, o; ALAK W2; MLE W1; MLESA W0
- **Topics:** Matrices and matrix operations; row echelon form (REF); linear systems; Gauss elimination and inverse of a matrix; system of linear equations (review); elementary matrix operations, elementary matrices and elementary operations on matrices; rank of a matrix and its properties; computation of the rank; matrix inverse; determinants, rank, invertibility; computational rules for matrices; row and column reduced matrices; echelon matrix and its properties; solution of a system of equations using rank concepts; homogeneous and non-homogeneous systems; existence and uniqueness of solutions; left and right inverses; pseudo inverse; triangular systems; basics of matrix algebra; Gauss elimination for homogeneous and non-homogeneous equations; system of linear equations – Gauss elimination; system of linear equations; Gauss elimination (Gauss-Jordan).
- **Results:** Row operations preserve solution set [P]; rank = row rank = column rank [P]; solvability criterion rank(A)=rank([A|b]) [P]; uniqueness of reduced row echelon form [P]; an n×n matrix is invertible iff rank n iff det≠0 [P].
- **Build:** Gaussian elimination with partial pivoting, RREF, rank and inverse from scratch; compare with `numpy.linalg`.
- **Gap-fills:** *[inferred: Strang Ch.1–3]* four fundamental subspaces, column picture versus row picture, block matrices and matrix multiplication as four equivalent views.

**Assignment A4.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The rank of the matrix [[1,2],[2,4]] is

(A) 0  
(B) 1  
(C) 2  
(D) 3

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Elementary row operations preserve the solution set  
(B) Row rank equals column rank  
(C) Ax = b is solvable iff rank(A) = rank([A b])  
(D) A 3x3 matrix with determinant 0 can be invertible

**Q3 (2 marks, numerical answer).** Solve 2x + y = 5 and x - y = 1. Compute x^2 + y^2.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that elementary row operations do not change the solution set of Ax = b, by showing each is invertible by another elementary operation.

**Q5 (3 marks, programming).** Write gauss_solve (partial pivoting), rref and rank (with a tolerance). Solve the 5x5 Hilbert system with solution all ones and report the residual and error. Predict the condition number order of magnitude first.

<details><summary>Key for A4.1 (open only after your attempt)</summary>

- **Q1:** B. The second row is twice the first.
- **Q2:** ABC. Determinant zero means singular.
- **Q3:** 5 (tolerance ±0.001). x = 2, y = 1, so 5.
- **Q4 (marking outline):** Each operation is reversible, so solutions of one system are solutions of the other.
- **Q5 (what a passing submission shows):** Hilbert(5) condition about 4.8e5; error about 1e-10 despite tiny residual.

</details>

### U4.2 Vectors, vector spaces, subspaces, bases and dimension
**Sources:** LAP W1–4, o; LAR W3; ALAB P1, P2; EM1 W8, o; AEMK W6; EMML W1; MFML W1; ALAK W1; ALAJ W1; PMO W1; OMLH W1–2
- **Topics:** Vectors, operations on vectors, properties and applications; introduction to algebraic structures (rings and fields); definition of vector spaces and examples; definition of subspaces and examples (continued); sum of subspaces; generating system, linear dependence and independence, and bases; Rn, subspaces, linear independence; examples of a basis of a vector space; review of univariate polynomials, examples of univariate polynomials and rational functions; vector spaces with finite generating system; Steinitz's exchange theorem and examples; examples of finite-dimensional vector spaces; dimension formula and its examples; existence of a basis; vectors in machine learning; vector space, subspace, basis and dimension; ordered basis and coordinate matrix; computations concerning subspaces; vector spaces over an arbitrary scalar field (even a finite field); coordinate-free algebraic methods; basis and dimension of a vector space; subspaces.
- **Results:** Steinitz exchange lemma [P]; any two bases have equal cardinality (dimension well defined) [P]; existence of a basis in finite-dimensional spaces [P]; dimension formula dim(U+W)=dim U+dim W−dim(U∩W) [P].
- **Build:** subspace-membership, basis extraction and dimension tools using exact rational arithmetic and then floating point (observe rank decisions with tolerance).
- **Gap-fills:** *[inferred: Axler Ch.1–2]* span, list length versus independence, infinite-dimensional examples (polynomials, sequences, function spaces) as motivation for D13.

**Assignment A4.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The dimension of the subspace {(x,y,z): x + y + z = 0} of R^3 is

(A) 1  
(B) 2  
(C) 3  
(D) 0

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Any three vectors in R^2 are linearly dependent  
(B) The span of any set is a subspace  
(C) The unit sphere is a subspace  
(D) Polynomials of degree at most 3 form a space of dimension 4

**Q3 (2 marks, numerical answer).** dim U = 3, dim W = 4 and dim(U intersect W) = 2. What is dim(U + W)?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that in a space spanned by n vectors, any n + 1 vectors are linearly dependent (Steinitz exchange argument).

**Q5 (3 marks, programming).** Write column_basis(A, tol) using elimination and use it to compute the dimension of the column space. Test on a 5x5 matrix of rank 3 built from products, then perturb by 1e-12 noise and by 1e-6 noise. Predict the rank each tolerance reports.

<details><summary>Key for A4.2 (open only after your attempt)</summary>

- **Q1:** B. One independent linear constraint removes one dimension.
- **Q2:** ABD. The unit sphere is not closed under scaling.
- **Q3:** 5 (tolerance ±0). Dimension formula: 5.
- **Q4 (marking outline):** Replace spanning vectors one at a time by the independent vectors; after n exchanges the (n+1)th is a combination.
- **Q5 (what a passing submission shows):** Exact rank 3; tolerance 1e-9 still reports 3 for 1e-12 noise but 5 for 1e-6 noise.

</details>

### U4.3 Linear maps, representation by matrices, duality and quotient spaces
**Sources:** LAP W5–8; LAR W5; ALAB P1, P2, o; EM1 W9, o; AEMK W6; MFML W2; EMML W2; PMO W1; ALAK W1
- **Topics:** Introduction to linear maps; examples of linear maps; linear maps and bases; pigeonhole principle in linear algebra; interpolation and the rank theorem; direct sums of vector spaces; projections; direct-sum decomposition of a vector space; dimension equality; dual spaces; quotient spaces; homomorphism theorem of vector spaces; isomorphism theorem of vector spaces; matrix of a linear map; change of bases; linear transformation; existence of linear transformation; rank–nullity theorem; representation of transformations by matrices; change of ordered basis and matrix representation of transformations; algebra of linear transformations; linear operators and linear functionals; dual space and double dual space; transpose of a linear transformation; linear transformations (EM1 Week 9); rank-nullity; linear transformations; linear transformations (ALAK Week 1); linear transformations.
- **Results:** Rank–nullity theorem [P]; a linear map is determined by its action on a basis [P]; isomorphism theorem for vector spaces [P]; V ≅ V** for finite dimension [P]; matrix of composite is product of matrices [P]; change-of-basis formula [D].
- **Build:** matrix of a map in arbitrary bases, change of basis and the effect on a matrix; null space and range via SVD, from scratch after U4.9.
- **Gap-fills:** *[inferred: Axler Ch.3]* invertibility and isomorphic vector spaces; linear transformations of the plane (rotation, shear, reflection) as pictures.

**Assignment A4.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** A 5 x 8 matrix has rank 3. The dimension of its null space is

(A) 3  
(B) 5  
(C) 8  
(D) 2

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) A linear map is determined by its values on a basis  
(B) The kernel of a linear map is a subspace  
(C) A change-of-basis matrix is singular  
(D) For finite-dimensional V, V is isomorphic to its double dual

**Q3 (2 marks, numerical answer).** A 4 x 6 matrix has rank 2. What is the nullity?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove the rank-nullity theorem: dim V = dim ker T + dim im T.

**Q5 (3 marks, programming).** Write matrix_of_map(T, basis_in, basis_out). Check T(x,y) = (y,x) in the standard basis, then in the basis (1,1),(1,-1). Predict the second matrix first.

<details><summary>Key for A4.3 (open only after your attempt)</summary>

- **Q1:** B. Rank-nullity: 8 - 3 = 5.
- **Q2:** ABD. Change-of-basis matrices are invertible.
- **Q3:** 4 (tolerance ±0). Nullity = columns - rank = 4.
- **Q4 (marking outline):** Extend a basis of the kernel to a basis of V; the images of the added vectors form a basis of the image.
- **Q5 (what a passing submission shows):** Standard matrix [[0,1],[1,0]]; in the new basis diag(1,-1).

</details>

### U4.4 Inner products, norms, orthogonality, projections and Gram–Schmidt
**Sources:** LAR W6; ALAB P4; MFML W3; EMML W2,6; ALAK W1,3; ALAJ W1; PMO W1; AOW W1
- **Topics:** Inner product spaces; inner products and norms; matrix norms; Gramian matrix; Gram–Schmidt orthogonalization and process; orthogonal complements and orthogonal complement; best approximation; orthogonality, projection and real symmetric matrices (Week 3); projection mapping; norms and spaces; inner product and vector norm; orthogonal matrices; rotators and reflectors; QR decomposition; properties of vectors and norms.
- **Results:** Cauchy–Schwarz and triangle inequalities [P]; Gram–Schmidt produces an orthonormal basis [P]; orthogonal projection onto a subspace is the best approximation (Pythagoras) [P]; V = W ⊕ W^⊥ [P]; projection matrix P = A(AᵀA)⁻¹Aᵀ [D]; equivalence of norms on Rn [S].
- **Build:** classical and modified Gram–Schmidt, Householder QR and Givens rotators from scratch, observing loss of orthogonality (MGS vs CGS).
- **Gap-fills:** *[inferred: MML Ch.3]* analytic geometry: lengths, distances, angles, orthonormal bases, orthogonal projections, rotations; p-norms and the unit ball geometry (links to L1 sparsity in U9.4).

**Assignment A4.4** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The orthogonal projection of (3,4) onto the x-axis is

(A) (3,4)  
(B) (3,0)  
(C) (0,4)  
(D) (1,0)

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) abs(u.v) <= norm(u) norm(v)  
(B) Gram-Schmidt returns an orthonormal basis of the same span  
(C) An orthogonal projection matrix satisfies P^2 = P and P^T = P  
(D) Orthogonal matrices change vector lengths

**Q3 (2 marks, numerical answer).** Cosine of the angle between (1,2,2) and (2,2,1).

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that the orthogonal projection of b onto a subspace W is the unique closest point of W to b, using Pythagoras.

**Q5 (3 marks, programming).** Implement classical Gram-Schmidt, modified Gram-Schmidt and Householder QR. On the 10x10 Hilbert matrix report the norm of Q^T Q - I for each. Predict the ranking first.

<details><summary>Key for A4.4 (open only after your attempt)</summary>

- **Q1:** B. Keep the component along (1,0).
- **Q2:** ABC. Orthogonal matrices preserve length.
- **Q3:** 0.8889 (tolerance ±0.001). Dot product 8 over norms 3 and 3.
- **Q4 (marking outline):** For w in W, norm(b-w)^2 = norm(b-p)^2 + norm(p-w)^2 because b-p is orthogonal to W.
- **Q5 (what a passing submission shows):** Classical GS loses orthogonality badly, modified GS is better, Householder is near machine epsilon.

</details>

### U4.5 Determinants, multilinear forms and permutations
**Sources:** LAP W10–12, o; LAR W4
- **Topics:** Permutation groups; canonical cycle decomposition of permutations; signature of a permutation; introduction to multilinear maps; multilinear maps (continued); introduction to determinants; determinants (continued); computational rules for determinants; properties of determinants and adjoint of a matrix; adjoint–determinant theorem; the determinant of a linear operator; determinants and volumes (and continued); LR decomposition; elementary divisor theorem; determinants via the theory of multilinear forms.
- **Results:** Existence and uniqueness of an alternating n-linear form with det(I)=1 [P]; det(AB)=det A·det B [P]; adjoint–determinant theorem A·adj(A)=det(A)·I [P]; |det A| is the volume scaling factor [D]; Cramer's rule [P].
- **Build:** determinant by permutation expansion, by LU, and by cofactor, with cost measured; volume of a parallelepiped.
- **Gap-fills:** *[inferred: Strang Ch.5]* determinant as dilation factor (links to change of variables in U3.3 and normalizing flows in D13).

**Assignment A4.5** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The determinant of [[1,2],[3,4]] is

(A) -2  
(B) 2  
(C) 10  
(D) -10

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) det(AB) = det(A) det(B)  
(B) Swapping two rows flips the sign of the determinant  
(C) det(A + B) = det(A) + det(B)  
(D) The absolute determinant is the volume scaling factor

**Q3 (2 marks, numerical answer).** Determinant of [[2,0,1],[1,3,2],[0,1,1]].

**Q4 (2 marks, prove or derive; every step with its reason).** Show that any alternating multilinear function of the rows changes sign when two rows are swapped.

**Q5 (3 marks, programming).** Compute determinants of random 6x6 matrices by permutation expansion, by LU and by cofactor recursion. Acceptance: all agree to 1e-9. Time n = 6, 7, 8 and predict the growth factor of the permutation method.

<details><summary>Key for A4.5 (open only after your attempt)</summary>

- **Q1:** A. 1*4 - 2*3.
- **Q2:** ABD. The determinant is not additive.
- **Q3:** 3 (tolerance ±0.001). Expand along row 1: 2(3-2) + 1(1-0) = 3.
- **Q4 (marking outline):** Apply the alternating property to the sum of the two rows placed in both positions and expand by multilinearity.
- **Q5 (what a passing submission shows):** Permutation and cofactor grow about n times per extra row factorially (about 7-8x per step); LU grows as n^3.

</details>

### U4.6 Eigenvalues, eigenvectors, similarity and diagonalization
**Sources:** LAR W7–8; EM1 W10, o; AEMK W8; MFML W2; EMML W2; ALAJ W3; ALAB P3; LAP o
- **Topics:** Eigenvalues and eigenvectors; similarity, diagonalization and applications; characteristic values and diagonalization (review); Hermitian, skew-Hermitian and unitary matrices and their eigenvalue properties; similarity of matrices; diagonalization of matrices; special matrices and properties; eigenvalue decomposition, properties and applications; characteristic polynomial; algebraic versus geometric multiplicity.
- **Results:** Eigenvectors for distinct eigenvalues are independent [P]; diagonalizability criterion (geometric = algebraic multiplicity) [P]; similar matrices share characteristic polynomial [P]; trace = sum and det = product of eigenvalues [P]; Cayley–Hamilton [P in U4.7].
- **Build:** power iteration, inverse iteration and QR iteration from scratch, checked against `numpy.linalg.eig`.
- **Gap-fills:** *[inferred: Strang Ch.6]* powers of a matrix, difference/differential equation solutions via eigen-decomposition (feeds D7 and D10).

**Assignment A4.6** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** A 2x2 matrix has trace 5 and determinant 6. Its eigenvalues are

(A) 1 and 4  
(B) 2 and 3  
(C) 1 and 6  
(D) 5 and 1

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Eigenvectors for distinct eigenvalues are linearly independent  
(B) Similar matrices have the same eigenvalues  
(C) Every square matrix is diagonalizable  
(D) The trace equals the sum of the eigenvalues

**Q3 (2 marks, numerical answer).** Largest eigenvalue of [[2,1],[1,2]].

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that eigenvectors belonging to distinct eigenvalues are linearly independent.

**Q5 (3 marks, programming).** Implement power iteration, inverse iteration with a shift, and unshifted QR iteration. Compare the observed convergence rate of power iteration with abs(lambda2/lambda1) on a symmetric 5x5 matrix. Predict the rate first.

<details><summary>Key for A4.6 (open only after your attempt)</summary>

- **Q1:** B. They sum to 5 and multiply to 6.
- **Q2:** ABD. Defective matrices exist.
- **Q3:** 3 (tolerance ±0.001). Eigenvalues 3 and 1.
- **Q4 (marking outline):** Assume a minimal dependent set, apply A and subtract a multiple to get a shorter dependency, contradiction.
- **Q5 (what a passing submission shows):** Observed rate matches abs(lambda2/lambda1) within 5 percent.

</details>

### U4.7 Canonical forms: minimal polynomial, invariant subspaces, Jordan and rational forms
**Sources:** ALAB o, P3; EMML W6; LAP W10
- **Topics:** Annihilating polynomials; minimal polynomial; invariant subspace; triangulation (two lectures); simultaneous triangulation and simultaneous diagonalization; direct-sum decomposition; invariant direct sums; the primary decomposition theorem; Jordan forms and Jordan canonical form; rational form; elementary divisor theorem; canonical forms and Jordan forms (course component iv).
- **Results:** Cayley–Hamilton theorem [P]; minimal polynomial divides every annihilating polynomial [P]; triangulability over algebraically closed fields [P]; primary decomposition theorem [P]; existence and uniqueness of Jordan form [S]; rational canonical form [X, proof beyond course scope, stated].
- **Build:** Jordan-chain computation for small matrices with exact arithmetic; demonstrate numerical instability of Jordan form in floating point.

**Assignment A4.7** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The minimal polynomial of the 3x3 identity matrix is

(A) x - 1  
(B) (x - 1)^3  
(C) x  
(D) x^3 - 1

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Cayley-Hamilton: p(A) = 0 for the characteristic polynomial p  
(B) The minimal polynomial divides the characteristic polynomial  
(C) A Jordan form is always diagonal  
(D) Over C, A is diagonalizable iff its minimal polynomial has distinct roots

**Q3 (2 marks, numerical answer (blocks)).** How many Jordan blocks does [[2,1],[0,2]] have (nullity of A - 2I)?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove the Cayley-Hamilton theorem for a diagonalizable matrix.

**Q5 (3 marks, programming).** Using Python fractions (exact arithmetic), compute a Jordan chain for A = [[2,1,0],[0,2,1],[0,0,2]]. Then perturb A by 1e-10 and compute eigenvalues with your own power or QR iteration (NumPy by default). Predict the size of the eigenvalue shift.

<details><summary>Key for A4.7 (open only after your attempt)</summary>

- **Q1:** A. I satisfies A - I = 0.
- **Q2:** ABD. Jordan forms can have off-diagonal ones.
- **Q3:** 1 blocks (tolerance ±0). Nullity of [[0,1],[0,0]] is 1.
- **Q4 (marking outline):** Write A = P D P^-1; p(A) = P p(D) P^-1 and p(lambda_i) = 0 for each diagonal entry.
- **Q5 (what a passing submission shows):** One block of size 3; eigenvalue shift about the cube root of 1e-10, roughly 5e-4.

</details>

### U4.8 Spectral theory: normal operators, symmetric matrices, quadratic forms, PSD matrices and kernels
**Sources:** ALAB o, P4; MFML W3; EMML W3; PMO W1; OMLH W1–2; AOW W1; AEMK W8; ALAK W8, o
- **Topics:** Operators on inner-product spaces; the adjoint of a linear operator; normal and self-adjoint operators; unitary and orthogonal operators and their matrices; bilinear and quadratic forms; orthogonal projections and the spectral theorem; spectral decomposition; spectral theorem for symmetric matrices; real symmetric matrices; definiteness of matrices (eigenvalue criterion and Sylvester criterion); quadratic forms and quadratic functions; positive semi-definite (PSD) matrices and kernel functions; Gaussian random vectors; eigenvalue-eigenvector decomposition of square matrices.
- **Results:** Spectral theorem for real symmetric / Hermitian matrices [P]; spectral theorem for normal operators [P]; Sylvester's criterion [P]; PSD ⇔ nonnegative eigenvalues ⇔ Gram form [P]; Mercer-type statement for kernel matrices [S, used in U9.5].
- **Build:** Jacobi eigenvalue algorithm for symmetric matrices; PSD test by Cholesky; Gram-matrix kernel construction.
- **Gap-fills:** *[inferred: MML Ch.4]* Cholesky decomposition, Rayleigh quotient and variational characterization of eigenvalues (needed for PCA in U9.7).

**Assignment A4.8** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The eigenvalues of a real symmetric matrix are

(A) always positive  
(B) always real  
(C) always integers  
(D) always distinct

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Real symmetric matrices have an orthonormal eigenbasis  
(B) A symmetric matrix is PSD iff all eigenvalues are nonnegative  
(C) B^T B is positive semidefinite for any B  
(D) A symmetric matrix with positive diagonal entries is positive definite

**Q3 (2 marks, numerical answer).** Smallest eigenvalue of [[2,-1],[-1,2]].

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that a real symmetric matrix has real eigenvalues and that eigenvectors for distinct eigenvalues are orthogonal.

**Q5 (3 marks, programming).** Implement the Jacobi eigenvalue algorithm and Cholesky. Build an RBF Gram matrix on 20 random points and report its smallest eigenvalue and whether Cholesky succeeds. Predict the sign of the smallest eigenvalue.

<details><summary>Key for A4.8 (open only after your attempt)</summary>

- **Q1:** B. Spectral theorem.
- **Q2:** ABC. Positive diagonal alone is not enough.
- **Q3:** 1 (tolerance ±0.001). Eigenvalues 1 and 3.
- **Q4 (marking outline):** Use conjugate transpose to show lambda equals its conjugate; for orthogonality compare x^T A y computed two ways.
- **Q5 (what a passing submission shows):** Smallest eigenvalue is nonnegative up to about -1e-12; Cholesky succeeds after adding a tiny jitter.

</details>

### U4.9 LU, QR, conditioning, SVD, pseudo-inverse and low-rank approximation
**Sources:** ALAK W2–4,9,12, o; ALAB P4, o; EMML W3,6; MFML W4; ALAJ W4; PMO W1; OMLH W1–2
- **Topics:** LU decomposition and computational complexity; rotators and reflectors; QR decomposition; condition number of a square matrix and its geometric interpretation; norm of a matrix; sensitivity analysis results for the system of linear equations; singular value decomposition (SVD), relation to condition number, sensitivity analysis of least squares problems and variation in parameter estimates in regression; generalized (g-) inverse and pseudo-inverse; low-rank approximation (LRA) and structured low-rank approximation (SLRA); polar decomposition; spectral decomposition; Python implementation of SVD and low-rank approximation; SVD algorithms and methods; applications of SVD: beamforming in MIMO, dimensionality reduction, rate maximization in wireless, MUSIC algorithm; alternating projections for computing LRA and SLRA; approximate GCD computation; singular value decomposition (SVD) as component vii of advanced linear algebra.
- **Results:** Existence of SVD [P]; Eckart–Young–Mirsky low-rank optimality [P]; cond(A)=σmax/σmin and error amplification bound [D]; Moore–Penrose pseudo-inverse via SVD, four defining equations [P]; polar decomposition [P].
- **Build:** SVD via eigendecomposition of AᵀA, then one-sided Jacobi/Golub–Kahan from scratch; image compression by truncated SVD; compare with `numpy.linalg.svd`.
- **Gap-fills:** *[inferred: Trefethen–Bau; Strang Ch.7]* floating-point arithmetic, backward stability, Cholesky, randomized SVD (links to LoRA in U12.7).

**Assignment A4.9** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** For A = U S V^T the rank of A equals

(A) the number of nonzero singular values  
(B) the largest singular value  
(C) the trace of S  
(D) the determinant of S

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Truncated SVD gives the best rank-k approximation (Eckart-Young)  
(B) cond2(A) = sigma_max / sigma_min  
(C) Singular values equal the eigenvalues of A  
(D) The pseudo-inverse is V S^+ U^T

**Q3 (2 marks, numerical answer).** Frobenius error of the best rank-1 approximation of diag(3,2,1).

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that the singular values of A are the square roots of the eigenvalues of A^T A and that the spectral norm of A equals sigma_1.

**Q5 (3 marks, programming).** Implement SVD from the eigendecomposition of A^T A and then by one-sided Jacobi. Compress a synthetic 64x64 image by truncated SVD for k = 1..20 and check that the Frobenius error equals the square root of the sum of discarded squared singular values. Predict the identity first.

<details><summary>Key for A4.9 (open only after your attempt)</summary>

- **Q1:** A. Rank is the count of nonzero singular values.
- **Q2:** ABD. Singular values are square roots of eigenvalues of A^T A.
- **Q3:** 2.236 (tolerance ±0.001). Discard singular values 2 and 1: sqrt(5).
- **Q4 (marking outline):** A^T A is symmetric PSD; the maximum of norm(Ax)/norm(x) is the square root of its top eigenvalue.
- **Q5 (what a passing submission shows):** Error equals the square root of the sum of squares of discarded singular values to 1e-10.

</details>

### U4.10 Least squares, regularized and constrained least squares
**Sources:** ALAK W5–7, o; ALAJ W5–6; EMML W5; MFML W10
- **Topics:** Linear least squares: existence and uniqueness, geometrical interpretation, data fitting with least squares, feature engineering, application to vector auto-regressive models, fitting with continuous and discontinuous piecewise linear functions; application of least squares to classification (two-class and multi-class least-squares classifiers, polynomial classifiers, MNIST data set); multi-objective least squares; applications to estimation and regularized inversion; regularized data fitting and image de-blurring; constrained least squares; application to portfolio optimization; least square approximation and minimum-norm solution; linear regression and least squares; optimal linear MMSE estimation; applications: system identification, MMSE receiver, market prediction and forecasting, ARMA models; least squares and PCA; concept of cost function and relation to parameter estimation; parameter estimation problems; applications to portfolio optimization.
- **Results:** Normal equations characterize the minimizer [P]; solution via QR and via SVD [D]; Gauss–Markov (BLUE) [P in U6.4]; ridge solution and its SVD shrinkage form [D]; KKT system for equality-constrained least squares [D].
- **Build:** least squares by normal equations, QR and SVD with conditioning experiments; ridge and weighted LS; polynomial classifier on MNIST via LS.

**Assignment A4.10** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The normal equations for least squares are

(A) X w = y  
(B) X^T X w = X^T y  
(C) X X^T w = y  
(D) w = X^T y

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) The ridge solution is (X^T X + lambda I)^-1 X^T y  
(B) QR is numerically more stable than the normal equations  
(C) The least-squares solution is always unique  
(D) X^T X + lambda I is invertible for lambda > 0

**Q3 (2 marks, numerical answer).** Slope of the least-squares line through (0,1), (1,2), (2,2).

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the ridge solution and show that in the SVD basis each singular direction is shrunk by sigma/(sigma^2 + lambda) compared with 1/sigma.

**Q5 (3 marks, programming).** Fit a degree-12 polynomial by normal equations, by QR and by SVD on 30 noisy points. Report the error of each against the truth and the condition numbers of X and X^T X. Predict the relation between the two condition numbers.

<details><summary>Key for A4.10 (open only after your attempt)</summary>

- **Q1:** B. Setting the gradient of the squared error to zero.
- **Q2:** ABD. Rank-deficient X gives non-unique solutions.
- **Q3:** 0.5 (tolerance ±0.001). Sxy/Sxx = 1/2.
- **Q4 (marking outline):** Substitute X = U S V^T into the ridge normal equations and simplify.
- **Q5 (what a passing submission shows):** cond(X^T X) is about cond(X)^2; the normal equations lose about twice the digits.

</details>

### U4.11 Applications of linear algebra: PageRank, sparsity, dynamical systems, Markov chains, signal processing and data analytics
**Sources:** ALAK W10–12, o; ALAJ W2–4,7–12, o; EMML W6; LAP o
- **Topics:** Applications of matrices – circuits, graphs, social networks, traffic flow; eigenvalue decomposition applications – principal component analysis (PCA), eigenfaces for facial recognition; multicollinearity problem and PCA and dimensionality reduction; power method and the Google PageRank algorithm; underdetermined systems of linear equations, least-norm solutions, sparse solutions, dictionary learning and sparse code recovery; inverse eigenvalue problem and construction of Markov chains from a given stationary distribution; low-rank approximation and structured low-rank approximation with model order selection in time series (Hankel SLRA, autoregressive model order selection); image de-blurring; tensors and CP tensor decomposition, tensor-decomposition-based sparse learning in deep networks; matrix completion problems and collaborative filtering; data analytics: recommender systems, user rating prediction, the Netflix problem; structure of FFT/IFFT matrices and their properties; system model for OFDM/SC-FDMA and signal processing in OFDM systems; modelling of dynamical systems (robots, chemical plants), solution of autonomous linear dynamical systems (LDS) and solution with inputs and outputs; unsupervised learning: centroid-based clustering, probabilistic model-based clustering and the EM algorithm; linear perceptron and training a perceptron by stochastic gradient; compressive sensing and orthogonal matching pursuit for sparse signal estimation; discrete-time Markov chains with applications to supply chain management, forecasting and operations research (resource and inventory management); applications in wireless (MIMO/OFDM, beamforming, channel estimation), machine learning (regression, clustering, EM algorithm, perceptron, SVM, kernel SVM, PCA, face recognition), signal processing (signal estimation, regularization, compressive sensing, image compression, robotics and dynamical systems), data analytics (recommender systems, data completion, data prediction, forecasting, optimal estimation, financial models), operations research and miscellaneous applications; application to the Google page ranking algorithm; operations research (inventory and supply-chain management); electrical circuits; control and finance; wireless communication.
- **Results:** Perron–Frobenius for positive matrices [S]; convergence of the power method and PageRank damping [D]; stationary distribution of an irreducible aperiodic chain [P in U5.8]; DFT matrix is unitary and diagonalizes circulants [P].
- **Build:** PageRank on a small web graph; matrix completion by alternating least squares and by nuclear-norm heuristic; OMP from scratch; CP decomposition by ALS.
- **Gap-fills:** *[inferred: Strang LfD]* low-rank matrix and tensor ideas that reappear in LoRA (U12.7) and compression (U16.4).

**Assignment A4.11** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The damping factor in PageRank mainly ensures

(A) faster hashing  
(B) a unique stationary vector and convergence of the power method  
(C) symmetric links  
(D) dense graphs

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) The power method converges at rate abs(lambda2/lambda1)  
(B) PageRank is the stationary distribution of the Google matrix  
(C) Orthogonal matching pursuit is always optimal  
(D) The scaled DFT matrix is unitary

**Q3 (2 marks, numerical answer).** Stationary probability of state 1 for P = [[0.9,0.1],[0.5,0.5]].

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that the DFT matrix divided by sqrt(n) is unitary.

**Q5 (3 marks, programming).** Implement PageRank by power iteration on a 6-node graph with damping 0.85 and check it against the top eigenvector by your own eigensolver. Also implement OMP to recover a 3-sparse vector in R^50 from 20 Gaussian measurements and report the success rate over 200 trials. Predict the success rate band first.

<details><summary>Key for A4.11 (open only after your attempt)</summary>

- **Q1:** B. It makes the chain irreducible and aperiodic.
- **Q2:** ABD. OMP is greedy and can fail.
- **Q3:** 0.8333 (tolerance ±0.001). pi1 = 0.9 pi1 + 0.5 pi2 gives pi1 = 5 pi2, so 5/6.
- **Q4 (marking outline):** Entries are roots of unity; distinct columns are orthogonal because of the geometric sum identity.
- **Q5 (what a passing submission shows):** PageRank vectors agree to 1e-8; OMP success in the high 80s to 90s percent.

</details>

## D5. Probability and Stochastic Models

Aim: probability from events to limit theorems, the joint and multivariate machinery used by ML, and the stochastic models (Poisson process, Markov chains, queues, reliability) named in the sources. Benchmarks (recalled, not checked): Kay, *Intuitive Probability and Random Processes*; Rosenthal, *A First Look at Rigorous Probability Theory*; Deisenroth et al. Ch. 6; Blitzstein–Hwang, *Introduction to Probability*; Grimmett–Stirzaker.

### U5.1 Probability foundations: from events to Bayes' theorem
**Sources:** IPS W1–2, o; PSS W3, o; MFML W5, o; AEMA W9, o; EMML W10; SMLM W2; MLE W2; MLESA W0; S50 D2
- **Topics:** Sets, classes, collections; sequence of sets; ring and field (algebra) of sets; sigma-ring, sigma-field and monotone class; random experiment and events; definitions of probability; properties of the probability function I and II; conditional probability; independence of events; problems in probability I and II; probability concepts, conditional probability and Bayes' theorem; probability foundations from events to Bayes' theorem; basic concepts of probability; probability networks; review of probability, Bayes theorem; joint probability; marginal probability; law of total probability; independence of events; probability theory recap; probability theory as the core math backbone: critical for uncertainty modeling and ML intuition.
- **Results:** Continuity of probability along monotone sequences [P]; inclusion–exclusion for events [P]; law of total probability [P]; Bayes' theorem [P]; Borel–Cantelli lemmas [P]; π–λ / monotone class uniqueness theorem [S].
- **Build:** Bayes' rule on diagnostic-test and spam-filter examples; Monte Carlo verification of birthday and Monty-Hall problems.
- **Gap-fills:** *[inferred: Rosenthal; Kay]* measure-theoretic probability space (Ω, F, P), conditional independence, probabilistic graphical models as "probability networks" (links to U9.9).

**Assignment A5.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Two fair dice are rolled. The probability that the sum is 7 is

(A) 1/12  
(B) 1/6  
(C) 1/9  
(D) 7/36

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) P(A or B) = P(A) + P(B) - P(A and B)  
(B) Independent events satisfy P(A and B) = P(A) P(B)  
(C) Mutually exclusive events of positive probability are independent  
(D) The law of total probability uses a partition of the sample space

**Q3 (2 marks, numerical answer).** A disease has prevalence 1 percent; a test has sensitivity 90 percent and false-positive rate 5 percent. Probability of disease given a positive test.

**Q4 (2 marks, prove or derive; every step with its reason).** Derive Bayes' theorem and the law of total probability from the definition of conditional probability.

**Q5 (3 marks, programming).** Estimate by Monte Carlo (N = 10^5, fixed seed) the probability that switching wins the Monty Hall game and the probability that 23 people contain a shared birthday. Predict both first.

<details><summary>Key for A5.1 (open only after your attempt)</summary>

- **Q1:** B. 6 of 36 outcomes.
- **Q2:** ABD. Exclusive events with positive probability are dependent.
- **Q3:** 0.1538 (tolerance ±0.001). Bayes: 0.009/0.0585 = 0.1538.
- **Q4 (marking outline):** P(A and B) = P(A given B)P(B) = P(B given A)P(A); sum over a partition for the denominator.
- **Q5 (what a passing submission shows):** About 2/3 and about 0.507.

</details>

### U5.2 Random variables, distributions and moments
**Sources:** IPS W2–3, o; MFML W6; PSS W4; SMLM W2; EMML W10–11; S50 D1, D3
- **Topics:** Random variables; probability distribution of a random variable I and II (PMF, PDF, CDF); moments; characteristics of distributions I and II; moments of random variables; expectation and variance; expected value; mean, median, mode, variance, standard deviation, range, interquartile range, skewness, kurtosis, percentiles and quantiles as distribution characteristics.
- **Results:** Properties of the CDF and its characterization [P]; linearity of expectation [P]; variance identity Var X = E[X²] − (E X)² [P]; Jensen's inequality [P]; moment generating function determines moments [S].
- **Build:** empirical CDF, histogram and moment estimators; skewness and kurtosis from scratch.
- **Gap-fills:** *[inferred: Kay; Rosenthal]* characteristic functions, expectation as Lebesgue integral, entropy and KL divergence (needed in D9, D13).

**Assignment A5.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** For a random variable X, Var(X) equals

(A) E[X^2] - (E[X])^2  
(B) E[X]^2 - E[X^2]  
(C) E[(X)^2]  
(D) E[X] - 1

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) A CDF is non-decreasing  
(B) Expectation is linear  
(C) Var(aX) = a^2 Var(X)  
(D) E[XY] = E[X]E[Y] for all X and Y

**Q3 (2 marks, numerical answer).** Variance of a fair six-sided die.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove Var(aX + b) = a^2 Var(X).

**Q5 (3 marks, programming).** Write the empirical CDF, sample moments, skewness and excess kurtosis. For N = 10^6 draws from Exp(1) (inverse-CDF sampler) report both. Predict their theoretical values first.

<details><summary>Key for A5.2 (open only after your attempt)</summary>

- **Q1:** A. Standard variance identity.
- **Q2:** ABC. That product rule needs uncorrelated variables.
- **Q3:** 2.917 (tolerance ±0.001). E[X^2] = 91/6, mean 3.5: variance 35/12.
- **Q4 (marking outline):** Centre by the mean a E[X] + b; the shift cancels and a squares.
- **Q5 (what a passing submission shows):** Skewness about 2 and excess kurtosis about 6.

</details>

### U5.3 Special discrete distributions and the Poisson process
**Sources:** IPS W3–4; AEMA W9–10; PSS W4; EMML W11; SMLM W3; S50 D3
- **Topics:** Special discrete distributions I, II and III; discrete distributions (Bernoulli, binomial, negative binomial, Poisson, geometric, hypergeometric, multinomial); Poisson process I and II; discrete and continuous distribution functions; Poisson process and exponential distribution.
- **Results:** Poisson as the limit of binomial [P]; memorylessness of the geometric and exponential laws [P]; Poisson process: counts are Poisson and inter-arrivals exponential [D]; mean and variance of each standard law [D].
- **Build:** samplers for each discrete law from uniform random numbers; simulation of a Poisson process.
- **Gap-fills:** *[inferred: Kay]* Bernoulli trials and the multinomial as a model for categorical outputs (softmax in D11/D12).

**Assignment A5.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** For a Poisson random variable the variance equals

(A) the mean  
(B) the square of the mean  
(C) half the mean  
(D) one

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) The geometric distribution is memoryless  
(B) Binomial(n, lambda/n) tends to Poisson(lambda)  
(C) Inter-arrival times in a Poisson process are exponential  
(D) The variance of Bernoulli(p) is p

**Q3 (2 marks, numerical answer).** P(X = 3) for X ~ Poisson(2).

**Q4 (2 marks, prove or derive; every step with its reason).** Show that Binomial(n, lambda/n) probabilities converge to Poisson(lambda) as n goes to infinity.

**Q5 (3 marks, programming).** Sample Poisson by inversion and by thinning from a simulated Poisson process of rate 3 on [0,10]. Check that counts have mean about 30 and variance about 30 over 5000 runs. Predict the variance first.

<details><summary>Key for A5.3 (open only after your attempt)</summary>

- **Q1:** A. Mean = variance = lambda.
- **Q2:** ABC. The variance is p(1 - p).
- **Q3:** 0.1804 (tolerance ±0.0005). e^-2 * 8/6 = 0.1804.
- **Q4 (marking outline):** Write C(n,k)(lambda/n)^k(1-lambda/n)^(n-k) and take limits term by term.
- **Q5 (what a passing submission shows):** Mean and variance both near 30.

</details>

### U5.4 Special continuous distributions and the normal distribution
**Sources:** IPS W4–5; AEMA W10–11; PSS W4; SMLM W3; EMML W11; S50 D3
- **Topics:** Special continuous distributions I–V; uniform, exponential, gamma, beta, normal and log-normal distributions; normal distribution and problems on normal distribution; problems on special distributions I and II; continuous probability distribution; Gamma and Beta families (link to U2.5); probability distributions for modeling uncertainty: used in generative models, likelihoods and simulations; normal (Gaussian) distribution.
- **Results:** Normal density integrates to one [P]; closure of the normal under affine maps and sums of independent normals [P]; exponential is the only memoryless continuous law [P]; relationship among Gamma, chi-square and exponential [P].
- **Build:** Box–Muller and inverse-CDF samplers from scratch; Q–Q plots against the standard normal.
- **Gap-fills:** *[inferred: Blitzstein–Hwang]* heavy tails, mixture distributions and the exponential family (needed for U9.9 and U6.5).

**Assignment A5.4** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** If Z is standard normal, P(abs(Z) < 1.96) is about

(A) 0.68  
(B) 0.90  
(C) 0.95  
(D) 0.99

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) A sum of independent normals is normal  
(B) The exponential distribution is memoryless  
(C) A log-normal variable is the exponential of a normal variable  
(D) The normal density has two modes

**Q3 (2 marks, numerical answer).** P(-1 < Z < 1) for standard normal Z.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that the integral of exp(-x^2/2) over the real line equals sqrt(2 pi) using polar coordinates on the square of the integral.

**Q5 (3 marks, programming).** Implement Box-Muller and inverse-CDF exponential samplers and compute the Kolmogorov-Smirnov statistic for N = 10^5 against the exact CDFs. Predict the typical size of the statistic.

<details><summary>Key for A5.4 (open only after your attempt)</summary>

- **Q1:** C. Standard 95 percent interval.
- **Q2:** ABC. It is unimodal.
- **Q3:** 0.6827 (tolerance ±0.0005). erf(1/sqrt 2) = 0.6827.
- **Q4 (marking outline):** Square the integral, switch to polar, integrate r exp(-r^2/2) to get 2 pi.
- **Q5 (what a passing submission shows):** About 1/sqrt(N) scale, near 0.003.

</details>

### U5.5 Functions of random variables, transformations and order statistics
**Sources:** IPS W6–7
- **Topics:** Function of a random variable I and II; additive properties of distributions I and II; transformation of random variables; distribution of order statistics.
- **Results:** Density of Y=g(X) by change of variables [D]; sum of independent variables by convolution [P]; joint law of order statistics [D]; Jacobian formula for multivariate transformations [S].
- **Build:** numerical check of transformed densities against histograms of simulated samples.

**Assignment A5.5** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** If U is uniform on (0,1), then -ln U has the distribution

(A) uniform  
(B) Exp(1)  
(C) normal  
(D) Gamma(2)

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) The density of a sum of independent variables is a convolution  
(B) The CDF of the maximum of n iid variables is F(x)^n  
(C) For monotone g, f_Y(y) = f_X(g^-1(y)) abs(d g^-1/dy)  
(D) Order statistics of iid samples are independent

**Q3 (2 marks, numerical answer).** Expected value of the maximum of 3 independent U(0,1) variables.

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the density of Y = g(X) for a strictly increasing differentiable g.

**Q5 (3 marks, programming).** Simulate the maximum and minimum of n = 5 uniforms 10^5 times and compare histograms with the derived densities. Predict the mean of the maximum.

<details><summary>Key for A5.5 (open only after your attempt)</summary>

- **Q1:** B. P(-ln U > t) = e^-t.
- **Q2:** ABC. Order statistics are dependent.
- **Q3:** 0.75 (tolerance ±0.001). The maximum has density 3x^2, mean 3/4.
- **Q4 (marking outline):** F_Y(y) = F_X(g^-1(y)); differentiate with the chain rule.
- **Q5 (what a passing submission shows):** 5/6 = 0.833 for the maximum and 1/6 for the minimum.

</details>

### U5.6 Joint distributions, conditioning, covariance and multivariate normal
**Sources:** IPS W6–7; MFML W7–8; AEMA W11, o; SMLM W4–5; EMML W11; MLCE W2; S50 D2, D6; AOW W1
- **Topics:** Joint distributions I and II; jointly distributed random variables; conditioning of random variables; marginal and conditional probability distributions; independence and product moments; linearity property of correlation and examples; bivariate normal distribution I and II; joint probability distribution (three parts); bivariate and multivariate probability distributions; introduction to copulas and applications; sample geometry; covariance matrices and properties; covariance and correlation matrix; joint probability and covariance; covariance, Pearson correlation, Spearman rank correlation, Kendall tau; correlation coefficient; modelling of joint distributions through copulas.
- **Results:** Law of iterated expectation and law of total variance [P]; covariance matrix is symmetric PSD [P]; conditional of a multivariate normal is normal with explicit mean and covariance [D]; Sklar's theorem [X]; correlation = 0 implies independence only for jointly normal [P].
- **Build:** multivariate normal sampler via Cholesky; conditioning formula verified by simulation; Gaussian copula sampler.
- **Gap-fills:** *[inferred: MML Ch.6; Johnson–Wichern]* Gaussian marginalization and conditioning, change of variables for densities, sample geometry (n-dimensional view of centred data).

**Assignment A5.6** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Zero covariance implies independence

(A) always  
(B) never  
(C) for jointly normal variables  
(D) for uniform variables

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) A covariance matrix is symmetric positive semidefinite  
(B) Correlation lies in [-1, 1]  
(C) Var(Y) = E[Var(Y given X)] + Var(E[Y given X])  
(D) Normal marginals always imply a jointly normal pair

**Q3 (2 marks, numerical answer).** For a bivariate normal with means 0, sigma_x = 1, sigma_y = 2 and rho = 0.5, compute E[Y given X = 1].

**Q4 (2 marks, prove or derive; every step with its reason).** Prove the law of iterated expectation E[E[Y given X]] = E[Y] for discrete variables.

**Q5 (3 marks, programming).** Sample from a 3-D multivariate normal by Cholesky. Verify the empirical covariance, then compute the conditional mean and covariance of one component given the others by the formula and by regression on samples. Predict the agreement.

<details><summary>Key for A5.6 (open only after your attempt)</summary>

- **Q1:** C. True only for jointly Gaussian pairs.
- **Q2:** ABC. Joint normality needs more than normal marginals.
- **Q3:** 1 (tolerance ±0.001). rho sigma_y/sigma_x times x = 1.
- **Q4 (marking outline):** Sum over x of E[Y given X=x] P(X=x) and swap sums.
- **Q5 (what a passing submission shows):** Agreement within sampling error about 1/sqrt(N).

</details>

### U5.7 Limit theorems and concentration inequalities
**Sources:** MFML W8; BAN W6; S50 D4
- **Topics:** Limit theorems; central limit theorem; a primer on concentration inequalities; sampling techniques.
- **Results:** Markov and Chebyshev inequalities [P]; weak law of large numbers [P]; strong law of large numbers [S]; central limit theorem (via characteristic functions) [P]; Hoeffding and Chernoff bounds [P]; sub-Gaussian tail bounds [P].
- **Build:** empirical convergence in the CLT for several source distributions; tail-bound tightness plots (used again in U10.3 for UCB).
- **Gap-fills:** *[inferred: Lattimore–Szepesvári Ch.5]* Cramér–Chernoff method, sub-Gaussian and sub-exponential variables, martingales and Azuma–Hoeffding.

**Assignment A5.7** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Chebyshev's inequality bounds P(abs(X - mu) >= k sigma) by

(A) 1/k  
(B) 1/k^2  
(C) k^2  
(D) e^-k

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) The weak law of large numbers holds for iid variables with finite mean  
(B) The CLT applies to iid variables with finite variance  
(C) Hoeffding's inequality needs bounded variables  
(D) Markov's inequality applies to any real random variable

**Q3 (2 marks, numerical answer).** The Chebyshev bound on P(abs(X - mu) >= 3 sigma).

**Q4 (2 marks, prove or derive; every step with its reason).** Prove Chebyshev's inequality from Markov's inequality applied to (X - mu)^2.

**Q5 (3 marks, programming).** Draw sample means of n = 1, 5, 30, 200 from Exp(1) and track the skewness against 2/sqrt(n). Also compare empirical tail frequencies of Bernoulli means with Hoeffding's bound. Predict the skewness at n = 200.

<details><summary>Key for A5.7 (open only after your attempt)</summary>

- **Q1:** B. Standard form.
- **Q2:** ABC. Markov needs nonnegativity.
- **Q3:** 0.1111 (tolerance ±0.001). 1/k^2 with k = 3.
- **Q4 (marking outline):** P((X-mu)^2 >= a^2) <= E[(X-mu)^2]/a^2 = sigma^2/a^2.
- **Q5 (what a passing submission shows):** About 0.14.

</details>

### U5.8 Markov chains, queueing theory and reliability
**Sources:** HEM W11–12, o; AEMA W12, o; ALAJ W12; DOML W8
- **Topics:** Queuing system; distribution of arrivals and service times; analysis of M/M/1:FIFO and its application; analysis of M/M/S FIFO and its application; queueing theory and reliability theory; reliability, service time for a customer in a facility, life testing; discrete-time Markov chains.
- **Results:** Stationary distribution of M/M/1 [D]; Little's law [P]; Erlang-C formula for M/M/s [D]; existence and convergence of stationary distribution for finite irreducible aperiodic chains [P].
- **Build:** discrete-event simulator of M/M/1 and M/M/s queues compared with closed forms (reappears in U16.3 for LLM serving queues).
- **Gap-fills:** *[inferred: Kay Part II]* random processes, stationarity, Poisson and Gaussian processes; random walks (linking to U13 diffusion).

**Assignment A5.8** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** An M/M/1 queue has arrival rate 2 and service rate 3. Its utilization is

(A) 1/3  
(B) 2/3  
(C) 1  
(D) 3/2

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Little's law: L = lambda W  
(B) A finite irreducible aperiodic chain has a unique stationary distribution  
(C) M/M/1 is stable iff rho < 1  
(D) The Erlang-C waiting probability can exceed 1

**Q3 (2 marks, numerical answer).** Mean number in an M/M/1 system with lambda = 2 and mu = 3.

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the M/M/1 stationary distribution pi_n = (1 - rho) rho^n from the balance equations.

**Q5 (3 marks, programming).** Write a discrete-event simulator of an M/M/1 queue with lambda = 2, mu = 3 for 10^5 customers and estimate the mean time in system. Predict it from theory first.

<details><summary>Key for A5.8 (open only after your attempt)</summary>

- **Q1:** B. rho = lambda/mu.
- **Q2:** ABC. It is a probability.
- **Q3:** 2 (tolerance ±0.001). L = rho/(1 - rho) = 2.
- **Q4 (marking outline):** Balance across cuts: lambda pi_n = mu pi_{n+1}; normalize the geometric series.
- **Q5 (what a passing submission shows):** 1/(mu - lambda) = 1 time unit.

</details>

### U5.9 Conditional expectation and martingales
**Sources:** SA W2–3, o
- **Topics:** Conditional expectation: examples, definition (with respect to a sigma-field), the least-squares best predictor (orthogonal projection in L²), existence, properties (linearity, tower property, taking out what is known, Jensen); martingales: filtration, adapted process, definition, examples (random walks, Doob martingales, likelihood ratios), martingale convergence; measure-theoretic bridge taught just in time (sigma-fields, random variables as measurable functions, expectation as an integral, monotone and dominated convergence, L² spaces, modes of convergence: almost surely, in probability, in L^p).
- **Results:** Conditional expectation is the L²-orthogonal projection onto the sub-sigma-field [P]; tower property [P]; existence in general (Radon–Nikodym) [X, proof beyond course scope, stated; L² case proved]; Doob's martingale convergence for L²-bounded martingales [P]; general L¹-bounded case via upcrossings [S].
- **Build:** simulate random-walk, product and Doob martingales; verify the tower property by Monte Carlo and the L² convergence of a bounded-variance martingale.
- **Gap-fills:** *[inferred: Williams, *Probability with Martingales*; Grimmett–Stirzaker; Borkar, *Probability Theory: An Advanced Course*, all recalled, not checked]* stopping times and optional stopping, Doob's maximal inequality, Azuma–Hoeffding (link to U5.7). The source lists "measure-theoretic probability" as a prerequisite; here it is a claim to probe and teach as the topics above, not an assumption (Master Rules III.1.6).

**Assignment A5.9** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The tower property states that E[E[X given G]] equals

(A) E[X]  
(B) 0  
(C) Var(X)  
(D) E[X given G]^2

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Conditional expectation is the L2 orthogonal projection onto the sub-sigma-field  
(B) A martingale satisfies E[M_{n+1} given F_n] = M_n  
(C) Every submartingale is a martingale  
(D) The partial sums of fair coin flips (+1 or -1) form a martingale

**Q3 (2 marks, numerical answer).** Two fair dice are rolled; E[sum given first die = 3].

**Q4 (2 marks, prove or derive; every step with its reason).** Prove the tower property E[E[X given G]] = E[X] when G is generated by a finite partition.

**Q5 (3 marks, programming).** Simulate Polya's urn (start with 1 red and 1 blue ball, add a ball of the drawn colour) and track the red fraction, a martingale. Verify that its mean stays 0.5 and examine the distribution of the limit over 5000 runs. Predict the limit's distribution.

<details><summary>Key for A5.9 (open only after your attempt)</summary>

- **Q1:** A. Averaging the conditional expectation recovers the mean.
- **Q2:** ABD. Submartingales only satisfy an inequality.
- **Q3:** 6.5 (tolerance ±0.001). 3 + E[second die] = 6.5.
- **Q4 (marking outline):** Condition on each partition cell and sum with the cell probabilities.
- **Q5 (what a passing submission shows):** The limit is uniform on [0,1].

</details>

## D6. Statistics and Statistical Inference

Aim: from descriptive statistics to estimation theory, hypothesis testing, regression and Bayesian inference, including the learner's own "50 statistical techniques" list. Benchmarks (recalled, not checked): Casella–Berger, *Statistical Inference*; Miller–Freund, *Mathematical Statistics with Applications*; Johnson–Wichern, *Applied Multivariate Statistical Analysis* (6th ed.); Hastie–Tibshirani–Friedman, *The Elements of Statistical Learning*; Maity, *Statistical Methods in Hydrology and Hydroclimatology*.

### U6.1 Data, descriptive statistics and measures of association
**Sources:** PSS W1–2, o; IPS W8–9; SMLM W1, o; MLCE W1; S50 D1
- **Topics:** Different types of data; tables, charts, histograms, frequency distributions; measures of association; descriptive statistics I–IV; sample and population properties; introduction to probability and statistics; role of statistics, machine learning and data science; descriptive statistics for EDA and feature understanding; descriptive statistics as the data-understanding layer: foundation for EDA and feature understanding.
- **Results:** Sample mean minimizes squared deviation and median minimizes absolute deviation [P]; Chebyshev-type bounds for samples [P].
- **Build:** descriptive-statistics library from scratch (mean, median, mode, variance, SD, range, IQR, skewness, kurtosis, quantiles); box plots and histograms by hand.
- **Gap-fills:** *[inferred: Johnson–Wichern Ch.1]* outlier detection, standardization, graphical displays of multivariate data.

**Assignment A6.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Which statistic is least affected by one extreme outlier?

(A) Mean  
(B) Variance  
(C) Median  
(D) Range

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) IQR = Q3 - Q1  
(B) Skewness measures asymmetry  
(C) Standard deviation has the same units as the data  
(D) Variance has the same units as the data

**Q3 (2 marks, numerical answer).** Interquartile range of 1,2,3,4,5,6,7,8 (linear-interpolation percentiles).

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that the sample mean minimizes the sum of squared deviations.

**Q5 (3 marks, programming).** Write a descriptive-statistics module (mean, median, mode, variance, SD, range, IQR, skewness, kurtosis, quantiles) and a text five-number-summary box plot. Predict which statistic changes most when one value of a 100-point sample is replaced by a 10-sigma outlier.

<details><summary>Key for A6.1 (open only after your attempt)</summary>

- **Q1:** C. The median depends on order, not magnitude.
- **Q2:** ABC. Variance has squared units.
- **Q3:** 3.5 (tolerance ±0.001). Q3 = 6.25, Q1 = 2.75.
- **Q4 (marking outline):** Differentiate sum (x_i - c)^2 in c and set to zero; the second derivative is positive.
- **Q5 (what a passing submission shows):** The variance (and kurtosis) change most; the median barely moves.

</details>

### U6.2 Sampling distributions and point estimation
**Sources:** IPS W8–10; S50 D4
- **Topics:** Basic concepts; chi-square distribution; t-distribution; F-distribution; introduction to estimation; unbiased and consistent estimators; LSE and MME (least squares and method of moments); examples on MME and MLE; examples on MLE I and II; MSE; UMVUE, sufficiency and completeness; Rao–Blackwell theorem and its applications; sampling techniques (random, stratified).
- **Results:** Distribution of the sample mean and variance for normal samples (Cochran/Student) [P]; MLE invariance and asymptotic normality [D / S]; Rao–Blackwell theorem [P]; Lehmann–Scheffé [S]; Cramér–Rao bound [P].
- **Build:** MLE by closed form and by numerical optimization (links to D8); bias–variance of estimators by simulation.
- **Gap-fills:** *[inferred: Casella–Berger]* Fisher information, factorization theorem for sufficiency, bootstrap.

**Assignment A6.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The maximum-likelihood estimate of a Bernoulli parameter is

(A) the sample median  
(B) the sample mean  
(C) the sample variance  
(D) always 0.5

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) An unbiased estimator has expectation equal to the parameter  
(B) Sample variance with divisor n - 1 is unbiased  
(C) The MLE is always unbiased  
(D) Rao-Blackwellization improves an unbiased estimator using a sufficient statistic

**Q3 (2 marks, numerical answer).** MLE of the Poisson rate for the sample 2, 3, 4, 3.

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the MLE of the mean and variance of a normal sample and show that the variance MLE is biased.

**Q5 (3 marks, programming).** Fit a Gamma distribution by Newton's method on the likelihood. Estimate bias and variance of the MLE of the shape by simulation for n = 20, 100, 500. Predict the trend of the bias.

<details><summary>Key for A6.2 (open only after your attempt)</summary>

- **Q1:** B. Maximize p^s (1-p)^(n-s).
- **Q2:** ABD. The MLE of normal variance is biased.
- **Q3:** 3 (tolerance ±0.001). The sample mean, 3.
- **Q4 (marking outline):** Set derivatives of the log-likelihood to zero; E[S_MLE^2] = (n-1)/n sigma^2.
- **Q5 (what a passing submission shows):** Bias is positive for small n and shrinks like 1/n.

</details>

### U6.3 Confidence intervals and hypothesis testing
**Sources:** IPS W10–12; AEMA W12, o; S50 D4, D5
- **Topics:** Confidence intervals I–IV; basic definitions of testing; two types of errors (Type I and II); power of a test; p-values; Neyman–Pearson fundamental lemma and its applications I and II; testing for normal mean; testing for normal variance; large-sample test for variance and two-sample problem; paired t-test; testing equality of proportions; testing of hypotheses I–III; hypothesis testing framework; t-test (one-sample, two-sample); z-test; chi-square test; ANOVA; Mann–Whitney U test; Wilcoxon signed-rank test; testing of hypotheses; applications to reliability, queueing and life testing; statistical inference as decision making: used in A/B testing, experiments and validation, general framework; hypothesis testing as core business use: used in product decisions and experimentation; analysis of variance (ANOVA).
- **Results:** Neyman–Pearson lemma [P]; duality of confidence intervals and tests [P]; distribution of the t statistic [P]; likelihood-ratio test and Wilks' theorem [S].
- **Build:** each test from scratch with exact p-values, checked against `scipy.stats`; power curves by simulation; A/B-test simulator.
- **Gap-fills:** *[inferred: S50]* multiple testing (Bonferroni, Benjamini–Hochberg), effect sizes.

**Assignment A6.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** A p-value is

(A) the probability the null hypothesis is true  
(B) the probability of data at least as extreme as observed, assuming the null  
(C) the type II error rate  
(D) the effect size

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) A type I error rejects a true null hypothesis  
(B) Power equals one minus the type II error rate  
(C) A p-value is the probability that H0 is true  
(D) The Neyman-Pearson lemma gives a most powerful test for simple hypotheses

**Q3 (2 marks, numerical answer).** z statistic: sample mean 52, null mean 50, known sigma 10, n = 100.

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the 95 percent confidence interval for a normal mean with known sigma and show its duality with the two-sided z-test.

**Q5 (3 marks, programming).** Implement one-sample z and t tests with exact p-values by numerical integration of the density, a power curve by simulation, and an A/B test simulator. Acceptance: type I error near 0.05 over 20000 null runs. Predict the empirical type I rate.

<details><summary>Key for A6.3 (open only after your attempt)</summary>

- **Q1:** B. It is conditional on the null.
- **Q2:** ABD. C confuses p-values with posteriors.
- **Q3:** 2 (tolerance ±0.001). z = 2/(10/10) = 2.
- **Q4 (marking outline):** Pivot (xbar - mu)/(sigma/sqrt n) is standard normal; mu0 is in the interval iff the test fails to reject at 5 percent.
- **Q5 (what a passing submission shows):** About 0.05 within 0.005.

</details>

### U6.4 Correlation, regression and multivariate analysis
**Sources:** AEMA W11–12; SMLM W6–7; MLCE W2; MLESA W2; S50 D6, D7; MFML W8
- **Topics:** Correlation and regression I and II; simple linear regression and multiple linear regression; coefficient of determination; confidence intervals and hypothesis testing for regression; linear regression, multiple linear regression, logistic regression, ridge regression, lasso regression, polynomial regression; multivariate analysis: principal component analysis, empirical orthogonal functions (EOF) and analysis of variance (ANOVA); subset selection; shrinkage methods; principal component regression; partial least squares; sample geometry and covariance matrices; correlation and relationships: used in feature selection and diagnostics; regression and predictive modeling as the core of ML plus explainability.
- **Results:** Gauss–Markov theorem [P]; distribution of OLS estimates under normal errors [D]; R² and adjusted R² [D]; ANOVA F-test decomposition [P].
- **Build:** OLS with standard errors and t-tests from scratch; ridge and lasso (coordinate descent) from scratch.
- **Gap-fills:** *[inferred: Johnson–Wichern]* factor analysis, canonical correlation, MANOVA, Hotelling's T².

**Assignment A6.4** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** R-squared measures

(A) the proportion of variance explained by the model  
(B) the slope  
(C) the p-value  
(D) the residual mean

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) OLS is unbiased under the Gauss-Markov conditions  
(B) Ridge shrinks coefficients toward zero  
(C) Lasso can set coefficients exactly to zero  
(D) Adjusted R-squared never decreases when a predictor is added

**Q3 (2 marks, numerical answer).** R-squared for y = (1,2,3,4) and predictions (1.1,1.9,3.2,3.8).

**Q4 (2 marks, prove or derive; every step with its reason).** Show that OLS is unbiased and derive its covariance sigma^2 (X^T X)^-1.

**Q5 (3 marks, programming).** Implement OLS with standard errors and t-statistics, ridge, and lasso by coordinate descent. Recover a sparse coefficient vector in R^20 from 100 noisy rows and report support recovery for lasso. Predict which coefficients lasso keeps.

<details><summary>Key for A6.4 (open only after your attempt)</summary>

- **Q1:** A. 1 minus SSE/SST.
- **Q2:** ABC. Adjusted R-squared can decrease.
- **Q3:** 0.98 (tolerance ±0.001). SSE = 0.10 and SST = 5 give 0.98.
- **Q4 (marking outline):** beta_hat = beta + (X^T X)^-1 X^T eps; take expectation and covariance.
- **Q5 (what a passing submission shows):** Lasso keeps the true support with small shrinkage bias.

</details>

### U6.5 Bayesian inference and MCMC
**Sources:** S50 D8, D9; MLESA W5; MLE W4,11; SMLM o
- **Topics:** Bayesian inference; prior and posterior distributions; MCMC (Markov chain Monte Carlo); MLE, MAP and Bayesian estimation; Monte Carlo methods; conjugate priors; Bayesian statistics as modern AI thinking: used in uncertainty-aware AI and LLMs; MCMC stands for Markov Chain Monte Carlo.
- **Results:** Posterior ∝ likelihood × prior [P]; conjugacy of Beta–Binomial and Normal–Normal [D]; correctness (detailed balance) of Metropolis–Hastings [P]; Gibbs sampler as a special case [P].
- **Build:** Metropolis–Hastings and Gibbs sampler from scratch; posterior of a coin bias and of a linear-regression coefficient.
- **Gap-fills:** *[inferred: Murphy PML Ch.3–4; Bishop]* credible intervals, posterior predictive, Hamiltonian Monte Carlo (statement), variational inference (link to D13 VAE).

**Assignment A6.5** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** In Bayesian inference the posterior is proportional to

(A) likelihood times prior  
(B) prior divided by likelihood  
(C) likelihood plus prior  
(D) evidence only

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Beta is conjugate to the Bernoulli likelihood  
(B) Metropolis-Hastings satisfies detailed balance  
(C) Gibbs sampling uses full conditional distributions  
(D) MCMC samples are independent

**Q3 (2 marks, numerical answer).** Posterior mean for a Beta(2,2) prior after 7 heads in 10 tosses.

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the Beta-Binomial posterior from Bayes' rule.

**Q5 (3 marks, programming).** Write a Metropolis-Hastings sampler for the coin bias with a Beta(2,2) prior and 7 heads in 10 tosses. Report acceptance rate and posterior mean after burn-in. Predict the posterior mean.

<details><summary>Key for A6.5 (open only after your attempt)</summary>

- **Q1:** A. Bayes' rule.
- **Q2:** ABC. MCMC samples are correlated.
- **Q3:** 0.6429 (tolerance ±0.001). Posterior Beta(9,5) has mean 9/14.
- **Q4 (marking outline):** Multiply p^(a-1)(1-p)^(b-1) by p^s(1-p)^(n-s); recognize Beta(a+s, b+n-s).
- **Q5 (what a passing submission shows):** About 0.643 with acceptance 30-60 percent for a well-tuned proposal.

</details>

### U6.6 Forecasting with statistical and machine-learning models: hydrology and water-resources applications
**Sources:** SMLM W1,12, o
- **Topics:** Forecasting using statistical and machine-learning algorithms with applications to hydrology and water-resources engineering; the role of statistics, machine learning and data science in hydroclimatology and water resources; determining the characteristics of observational data and events; data-driven solutions for engineering challenges; probabilistic solutions from joint and conditional distributions; suitability of data-driven models and assessing their performance; time-series forecasting (ARMA/ARIMA, regression, random forest, LSTM) and forecast-skill metrics.
- **Results:** Stationarity and the Box–Jenkins identification logic for ARMA models [D]; forecast error decomposition [D].
- **Build:** rolling-origin forecasting evaluation of ARMA versus random forest versus LSTM on a streamflow-like series.
- **Gap-fills:** *[inferred: Maity, Statistical Methods in Hydrology and Hydroclimatology; Forsyth, Applied Machine Learning]* extreme-value analysis and frequency analysis of hydrologic series, copula-based joint modelling (links to U5.6).

**Assignment A6.6** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Which assumption do ARMA models standardly require?

(A) Stationarity  
(B) Independence of all variables  
(C) Normal marginals  
(D) Linear trends

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Rolling-origin evaluation respects time order  
(B) Shuffling a time series before splitting leaks future information  
(C) A persistence forecast is a useful baseline  
(D) Mean absolute error is unit-free

**Q3 (2 marks, numerical answer).** Stationary variance of AR(1) x_t = 0.8 x_(t-1) + e_t with unit-variance noise.

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the autocovariance of a stationary AR(1) process.

**Q5 (3 marks, programming).** Simulate an AR(2) streamflow-like series, fit AR coefficients by least squares, and run a rolling-origin forecast against persistence. Report the skill score. Predict the sign of the skill.

<details><summary>Key for A6.6 (open only after your attempt)</summary>

- **Q1:** A. Constant mean and autocovariance.
- **Q2:** ABC. MAE has the units of the data.
- **Q3:** 2.778 (tolerance ±0.001). sigma^2/(1 - phi^2) = 2.778.
- **Q4 (marking outline):** gamma(h) = phi^h gamma(0) by multiplying the recursion by x_(t-h) and taking expectations.
- **Q5 (what a passing submission shows):** Positive skill, since the AR model beats persistence on autocorrelated data.

</details>

## D7. Differential Equations, Dynamical Systems, Numerical Methods, Complex Analysis and Transforms

Aim: the applied-analysis toolkit (ODEs, difference equations, numerics, complex variables, Laplace/Z/Fourier) that supports optimization-as-dynamics (D8), signal processing, diffusion models (D13) and FFT-based systems (D16). Benchmarks (recalled, not checked): Kreyszig, *Advanced Engineering Mathematics* (10th ed.); O'Neil; Jain–Iyengar; Churchill–Brown; Ahlfors; Conway; Debnath–Bhatta; Strogatz, *Nonlinear Dynamics and Chaos*; Murray, *Mathematical Biology*.

### U7.1 First- and higher-order ordinary differential equations
**Sources:** EM1 W11–12, o; AEMK W3; MM W3
- **Topics:** First-order differential equations; solution of first-order ODEs; integrating factor; exact forms; ODE order, degree, solution and geometrical significance; solution of first-order first-degree ODE by separation of variables, homogeneous equation and Bernoulli equation; second-order ODEs and auxiliary solutions; higher-order differential equations with constant coefficients; Cauchy–Euler equations.
- **Results:** Existence and uniqueness (Picard–Lindelöf) [S]; solution of linear constant-coefficient ODEs by characteristic equation [P]; superposition and Wronskian [P]; variation of parameters [D].
- **Build:** Euler, Heun and RK4 integrators from scratch with global-error order measured.
- **Gap-fills:** *[inferred: Kreyszig Ch.1–2]* method of undetermined coefficients, power-series solutions, systems of ODEs (feeds U7.6 and gradient flow in U8.10).

**Assignment A7.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The solution of y' = y with y(0) = 1 is

(A) e^x  
(B) x + 1  
(C) cos x  
(D) 1/x

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Picard-Lindelof needs a Lipschitz condition  
(B) Roots of the characteristic equation give solutions of constant-coefficient linear ODEs  
(C) A nonzero Wronskian implies linear independence  
(D) The explicit Euler method has global order 2

**Q3 (2 marks, numerical answer).** y' = -2y, y(0) = 3. Compute y(1).

**Q4 (2 marks, prove or derive; every step with its reason).** Solve y'' + 3y' + 2y = 0 with y(0) = 1, y'(0) = 0 and show the solution is unique.

**Q5 (3 marks, programming).** Implement Euler, Heun and RK4 and verify the global error order on y' = -2y at h = 0.1, 0.05, 0.025. Predict the slopes first.

<details><summary>Key for A7.1 (open only after your attempt)</summary>

- **Q1:** A. Separate variables.
- **Q2:** ABC. Euler is first order.
- **Q3:** 0.406 (tolerance ±0.0005). 3 e^-2 = 0.406.
- **Q4 (marking outline):** Roots -1 and -2; y = 2e^-x - e^-2x; uniqueness from the Wronskian being nonzero.
- **Q5 (what a passing submission shows):** Slopes about 1, 2 and 4.

</details>

### U7.2 Numerical analysis: iteration, root finding, interpolation and quadrature
**Sources:** EM2 W5–6, o; AEMK W4–5
- **Topics:** Iterative methods for solution of systems of linear equations (Jacobi and Gauss–Seidel); solution of algebraic and transcendental equations (bisection, fixed-point iteration, Newton–Raphson); finite differences; interpolation; error in interpolation polynomials; Newton's forward and backward interpolation formulae; Lagrange's interpolation; numerical integration (trapezoidal, Simpson's 1/3rd and 3/8th rules).
- **Results:** Convergence of Jacobi/Gauss–Seidel for diagonally dominant matrices [P]; contraction mapping and fixed-point convergence [P]; interpolation error formula [D]; composite Simpson error [D].
- **Build:** all iterative solvers and interpolation formulae from scratch, checked against `scipy`.
- **Gap-fills:** *[inferred: Burden–Faires]* Runge's phenomenon, Chebyshev nodes, Gaussian quadrature.

**Assignment A7.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The Jacobi iteration converges for

(A) all matrices  
(B) strictly diagonally dominant matrices  
(C) singular matrices  
(D) only symmetric matrices

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Fixed-point iteration converges when abs(g') < 1 near the fixed point  
(B) Lagrange interpolation through n+1 points is unique  
(C) Equispaced interpolation can show the Runge phenomenon  
(D) Newton-Raphson converges from any starting point

**Q3 (2 marks, numerical answer).** Simpson's 1/3 rule with 2 intervals for the integral of x^2 on [0,2].

**Q4 (2 marks, prove or derive; every step with its reason).** Prove the contraction mapping fixed-point theorem on a closed interval.

**Q5 (3 marks, programming).** Implement Jacobi, Gauss-Seidel, Newton forward-difference interpolation and composite Simpson. Compare iteration counts for a diagonally dominant 5x5 system. Predict which solver needs fewer iterations.

<details><summary>Key for A7.2 (open only after your attempt)</summary>

- **Q1:** B. Diagonal dominance gives contraction.
- **Q2:** ABC. Newton can diverge.
- **Q3:** 2.667 (tolerance ±0.001). h/3 (f0 + 4 f1 + f2) = 8/3.
- **Q4 (marking outline):** Iterates form a Cauchy sequence by geometric decay; the limit is a fixed point and is unique.
- **Q5 (what a passing submission shows):** Gauss-Seidel needs about half the iterations of Jacobi.

</details>

### U7.3 Complex variables: analytic functions and complex integration
**Sources:** EM2 W3–4, o; AEMK W12; AEMA W1–3, o
- **Topics:** Function of complex variables and their properties including continuity and differentiability; analytic functions and Cauchy–Riemann equations; harmonic functions, harmonic conjugates and Milne's method; applications to the problems of potential flow I and II; line integrals in the complex plane; complex integration; Cauchy's theorem I and II; Cauchy's integral theorem and formula; Cauchy's integral formula for derivatives of an analytic function; derivatives of analytic functions; Morera's theorem; Liouville's theorem and the fundamental theorem of algebra; winding number and maximum modulus principle; limit, continuity, differentiability and analyticity of functions.
- **Results:** Cauchy–Riemann necessary and sufficient conditions [P]; Cauchy's theorem (Goursat) [S]; Cauchy integral formula and derivative formula [P]; Liouville and fundamental theorem of algebra [P]; maximum modulus [P].
- **Build:** numerical contour integration and verification of Cauchy's formula.

**Assignment A7.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The function f(z) = conjugate of z is

(A) analytic everywhere  
(B) analytic nowhere  
(C) analytic on the real axis only  
(D) entire

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Cauchy-Riemann equations are necessary for analyticity  
(B) The real part of an analytic function is harmonic  
(C) A bounded entire function is constant  
(D) Every continuous complex function is analytic

**Q3 (2 marks, numerical answer).** Magnitude of the contour integral of 1/z around the unit circle (counterclockwise).

**Q4 (2 marks, prove or derive; every step with its reason).** Show that the real and imaginary parts of an analytic function (C^2) are harmonic.

**Q5 (3 marks, programming).** Numerically evaluate the contour integral of f(z)/(z - a) over the unit circle for f = exp and a = 0.5, and compare with 2 pi i f(a). Predict the error scaling with the number of quadrature points.

<details><summary>Key for A7.3 (open only after your attempt)</summary>

- **Q1:** B. Cauchy-Riemann fails everywhere.
- **Q2:** ABC. Continuity is weaker.
- **Q3:** 6.283 (tolerance ±0.001). The integral equals 2 pi i.
- **Q4 (marking outline):** Differentiate the Cauchy-Riemann equations and use equality of mixed partials.
- **Q5 (what a passing submission shows):** Error falls geometrically with the number of points for analytic integrands.

</details>

### U7.4 Series, singularities, residues, real integrals and conformal mapping
**Sources:** EM2 W4, o; AEMK W12; AEMA W3–7, o
- **Topics:** Sequences and series; uniform convergence of series; power series and radius of convergence (Hadamard's formula); Taylor's and Laurent's series; zeros and singularities of an analytic function; zeros and poles; meromorphic functions; residue at a singularity; residue theorem; the argument principle and Rouché's theorem; evaluation of real integrals using residues I–V; integration through a branch cut; evaluation of real integrals; bilinear transformations and cross ratio; conformal mapping I and II; conformal mappings from half-plane to disk and half-plane to half-plane; disk to disk and angular region to disk; application of conformal mapping to potential theory.
- **Results:** Laurent expansion existence and uniqueness [P]; residue theorem [P]; argument principle and Rouché [P]; Möbius transformations map circles to circles [P]; Riemann mapping theorem [X].
- **Build:** residue calculator for rational functions; conformal map visualizer.

**Assignment A7.4** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The residue of 1/z at z = 0 is

(A) 0  
(B) 1  
(C) -1  
(D) infinity

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) The residue theorem sums residues inside a contour  
(B) A Laurent series converges in an annulus  
(C) Mobius transformations map circles and lines to circles and lines  
(D) The Riemann mapping theorem is proved in this unit

**Q3 (2 marks, numerical answer).** Integral of 1/(1 + x^2) over the real line.

**Q4 (2 marks, prove or derive; every step with its reason).** Evaluate the integral of 1/(1 + x^2) over the real line by the residue theorem with a large semicircle.

**Q5 (3 marks, programming).** Write a residue calculator for rational functions with simple poles, evaluate the integral above, and compare with trapezoid on [-1000, 1000]. Predict the truncation error.

<details><summary>Key for A7.4 (open only after your attempt)</summary>

- **Q1:** B. Coefficient of 1/z.
- **Q2:** ABC. Its proof is deferred.
- **Q3:** 3.142 (tolerance ±0.001). Residue at i is 1/(2i), giving 2 pi i/(2i) = pi.
- **Q4 (marking outline):** Close in the upper half plane; the arc contribution vanishes; residue at i gives pi.
- **Q5 (what a passing submission shows):** About 2/1000 = 0.002 from the tails.

</details>

### U7.5 Laplace, Z, Fourier and discrete Fourier transforms
**Sources:** EM2 W7–12, o; AEMA W7–9, o; ALAJ W8
- **Topics:** Laplace transform and its properties; Laplace transform of special functions; convolution theorem; evaluation of integrals by Laplace transform; solution of initial and boundary value problems; Fourier series representation of a function and its convergence; Fourier integral representation; Fourier sine and cosine transforms; Fourier transform and properties of the Fourier transform; applications of Fourier series to boundary value problems; review of unilateral and bilateral Z-transforms and their properties; application of calculus of residues for the inversion formula of Z-transforms and Laplace transforms; finite Fourier transforms; discrete Fourier transforms I and II and applications; Fourier integrals and Fourier transforms; structure of FFT/IFFT matrices; applications in signal processing, potential theory and bending of beams; Z-transforms I, II and III; review of bilateral Z-transforms.
- **Results:** Convolution theorem for Laplace and Fourier [P]; Dirichlet convergence theorem for Fourier series [S]; Parseval/Plancherel [P]; inversion formula for Z and Laplace transform by residues [D]; FFT divide-and-conquer recurrence [D].
- **Build:** FFT (radix-2) from scratch; spectral solution of a heat-equation boundary value problem.
- **Gap-fills:** *[inferred: Kreyszig]* Fourier transforms as a view of attention/positional encodings (link to U12.2) and of convolution (link to U11.5).

**Assignment A7.5** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The Laplace transform of e^(at) is

(A) 1/(s - a)  
(B) 1/(s + a)  
(C) a/s  
(D) s - a

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) The convolution theorem turns convolution into multiplication  
(B) Parseval's identity relates time and frequency energy  
(C) The FFT costs O(n log n)  
(D) The naive DFT costs O(n)

**Q3 (2 marks, numerical answer).** Laplace transform of f(t) = t evaluated at s = 2.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove the convolution theorem for Laplace transforms.

**Q5 (3 marks, programming).** Implement a radix-2 FFT and compare with a naive DFT (error below 1e-10). Solve u_t = u_xx on [0, pi] with u(x,0) = sin x spectrally. Predict u(x,1) first.

<details><summary>Key for A7.5 (open only after your attempt)</summary>

- **Q1:** A. Integrate e^-(s-a)t.
- **Q2:** ABC. It costs O(n^2).
- **Q3:** 0.25 (tolerance ±0.001). 1/s^2 = 0.25.
- **Q4 (marking outline):** Write the product of two integrals as a double integral and change variables to tau and t - tau.
- **Q5 (what a passing submission shows):** u(x,1) = e^-1 sin x.

</details>

### U7.6 Mathematical modelling: discrete and continuous dynamical systems
**Sources:** MM W1–4, o; LAR W7
- **Topics:** Overview of mathematical modeling, types of mathematical models and methods to solve them; discrete-time linear models (Fibonacci rabbit model, cell-growth model, prey–predator model); analytical solution methods and stability analysis of systems of linear difference equations; graphical solution by cobweb diagrams; discrete-time age-structured (Leslie) model; Jury's stability test; numerical methods to find eigenvalues (power method and LR method); discrete-time non-linear models (different cell-division models, prey–predator model); stability of non-linear discrete-time models; logistic difference equation; bifurcation diagrams; introduction to continuous-time models, limitations and advantage of discrete-time models, need of continuous-time models; model for growth of microorganisms; chemostat; stability and linearization methods for systems of ODEs; continuous-time single-species model (Allee effect); qualitative solution of differential equations using phase diagrams; Lotka–Volterra competition and prey–predator models; mathematical modelling in biological sciences, deterministic discrete and continuous time, linear and non-linear population dynamics; major content chosen from dynamical systems (population dynamics); prey–predator (preypredator) models; graphical solution for clear analysis of the nature of the models.
- **Results:** Stability of a linear difference system by eigenvalue modulus [P]; Jury criterion [S]; period-doubling route to chaos in the logistic map (observed and explained) [S]; Hartman–Grobman linearization [X]; Lyapunov stability of a fixed point [P in U8.10].
- **Build:** cobweb and bifurcation diagram generators; Lotka–Volterra phase portraits; simulation of Leslie matrices.
- **Gap-fills:** *[source gap: the source lists only 4 of 12 course weeks; remaining weeks added from benchmarks]* *[inferred: Murray; Strogatz]* Hopf bifurcation, limit cycles, SIR epidemic models, reaction–diffusion models, parameter estimation for models (links to D9).

**Assignment A7.6** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The nonzero fixed point of the logistic map x -> r x (1 - x) is

(A) 1/r  
(B) 1 - 1/r  
(C) r - 1  
(D) r/2

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) A fixed point of a 1-D map is stable if abs(f') < 1  
(B) The logistic map shows period doubling on the route to chaos  
(C) The Lotka-Volterra model has closed orbits  
(D) Linearization always decides stability

**Q3 (2 marks, numerical answer).** Nonzero fixed point of the logistic map with r = 2.5.

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the stability condition for a fixed point of x_(n+1) = f(x_n) and apply it to the logistic map to show stability for 1 < r < 3.

**Q5 (3 marks, programming).** Generate a bifurcation diagram for r from 2.8 to 4 and detect the first two period-doubling values. Integrate Lotka-Volterra with RK4 and show closed orbits. Predict the first doubling value.

<details><summary>Key for A7.6 (open only after your attempt)</summary>

- **Q1:** B. Solve x = r x (1 - x).
- **Q2:** ABC. Zero real parts are inconclusive.
- **Q3:** 0.6 (tolerance ±0.001). 1 - 1/r = 0.6.
- **Q4 (marking outline):** Linearize; stable iff abs(f'(x*)) < 1; f'(x*) = 2 - r.
- **Q5 (what a passing submission shows):** About r = 3 and r = 3.449.

</details>

### U7.7 ODE theory for dynamical systems: Gronwall, limit sets, invariant sets and chain transitivity
**Sources:** SA W4, o
- **Topics:** Ordinary differential equations: existence and uniqueness of solutions; Gronwall inequality; asymptotic behaviours of trajectories; invariant sets; internally chain transitive sets; equilibria, stability and Lyapunov functions.
- **Results:** Picard–Lindelöf existence and uniqueness [P under a Lipschitz condition]; Gronwall's inequality (integral form) [P]; the omega-limit set of a bounded trajectory is nonempty, compact and invariant [P]; LaSalle's invariance principle [S]; an internally chain transitive set is invariant and the limit set of a bounded asymptotic pseudo-trajectory is internally chain transitive [X→U8.16].
- **Build:** RK4 integration of a planar system; numerical estimate of its omega-limit set; gradient flow with an explicit Lyapunov function.
- **Gap-fills:** *[inferred: Hirsch–Smale–Devaney, recalled, not checked]* phase portraits, stability of linear systems, Poincaré–Bendixson (statement).

**Assignment A7.7** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Gronwall's inequality bounds a function u with u' <= L u by

(A) u(0) e^(L t)  
(B) u(0) + L t  
(C) u(0)/L  
(D) 0

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) The omega-limit set of a trajectory is invariant  
(B) The omega-limit set of a bounded trajectory is nonempty and compact  
(C) Every omega-limit set is a single point  
(D) A Lyapunov function can certify stability

**Q3 (2 marks, numerical answer).** Gronwall bound at t = 1 for u(0) = 1, u' <= 2u.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove: if u' <= L u for t >= 0 then u(t) <= u(0) e^(L t).

**Q5 (3 marks, programming).** Integrate the Van der Pol oscillator with RK4 (mu = 0.5) from several starting points and estimate the omega-limit set and its amplitude. Predict the amplitude of the limit cycle.

<details><summary>Key for A7.7 (open only after your attempt)</summary>

- **Q1:** A. Integrate the differential inequality.
- **Q2:** ABD. Limit cycles are limit sets that are not points.
- **Q3:** 7.389 (tolerance ±0.001). u(1) <= e^2 = 7.389.
- **Q4 (marking outline):** Multiply by e^(-L t); the product has non-positive derivative.
- **Q5 (what a passing submission shows):** About 2.

</details>

## D8. Optimization: Theory, Algorithms and Applications

Aim: eight dedicated source courses (primer, convex, LP, nonlinear programming, ML-oriented, software implementation, wireless/signal applications, distributed optimization) plus the optimization weeks of eight other courses, merged into one ladder: formulation and analysis, convex analysis, optimality and duality, linear programming, algorithms, then applications. Benchmarks (recalled, not checked unless noted): Boyd–Vandenberghe, *Convex Optimization* (Parts I and II confirmed from the published contents: convex sets, convex functions, convex optimization problems, duality; approximation and fitting, statistical estimation, geometric problems; the algorithms part on unconstrained and equality-constrained minimization and interior-point methods is recalled, not checked); Nocedal–Wright, *Numerical Optimization*; Bertsekas, *Nonlinear Programming*; Bazaraa–Sherali–Shetty; Chong–Zak; Dennis–Schnabel; Sun–Yuan; Rockafellar, *Convex Analysis*; Hiriart-Urruty–Lemaréchal; Chvátal and Dantzig–Thapa for LP; Tikhomirov, *Stories about Maxima and Minima*.

### U8.1 Optimization problems: formulation, history, transformations and basic facts
**Sources:** PMO W1, o; OAT W1–3, o; OFF W1–4, o; OMLH W3, o; MFML W10; MLE W3; EMML W8–10, o; CVX o; MLESA W0
- **Topics:** Introduction and history on the development of optimization theory; introduction to optimization; optimization overview of real analysis; optimization over open sets; optimization over surfaces; transformation of optimization problems; basic facts of maxima and minima and convex optimization; important classes of convex optimization problems; convex and non-convex optimization problems in machine learning; constrained and unconstrained optimization; numerical computation and optimization; introduction to optimization and its role as the workhorse of machine learning; introduction to Python for optimization; optimization algorithms (overview); introduction to optimization (Week 8 EMML); numerical optimization in machine learning; optimization using Python; convex optimization recap; mathematical optimization problem statement (variables, objective, constraints, feasible set, level sets); introduction to machine learning packages; Python basics for optimization; optimization using Python.
- **Results:** Fermat's necessary condition for interior extrema [P]; Weierstrass existence theorem [P in U8.4]; equivalent reformulations (epigraph form, slack variables, change of variables) preserve optimal values [P].
- **Build:** a small modelling layer in Python (objective, constraints, gradient check) used by all later optimization units.
- **Gap-fills:** *[inferred: Boyd Ch.1; Tikhomirov]* taxonomy of problem classes (LP, QP, QCQP, SOCP, SDP, GP, integer), local versus global minima, optimization over open sets and manifolds (Lagrange multipliers on surfaces).

**Assignment A8.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Minimizing f(x) is equivalent to maximizing

(A) f(x)  
(B) -f(x)  
(C) 1/f(x)  
(D) f(x)^2

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Epigraph form minimizes t subject to f(x) <= t  
(B) Slack variables turn inequality constraints into equalities  
(C) Every local minimum is a global minimum  
(D) Equivalent reformulations preserve the optimal value

**Q3 (2 marks, numerical answer).** Minimum value of f(x,y) = x^2 + y^2 - 2x - 4y.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that minimizing f over a feasible set C is equivalent to minimizing t over (x,t) with f(x) <= t and x in C.

**Q5 (3 marks, programming).** Write a small Problem class holding an objective, gradient, constraints and a feasibility check, plus grad_check. Test on the Rosenbrock function. Acceptance: gradient error below 1e-6 at 5 random points. Predict the minimizer first.

<details><summary>Key for A8.1 (open only after your attempt)</summary>

- **Q1:** B. The maximizers of -f are the minimizers of f.
- **Q2:** ABD. Local minima are global only under convexity.
- **Q3:** -5 (tolerance ±0.001). Stationary point (1,2) gives -5.
- **Q4 (marking outline):** At the optimum t = f(x); any feasible (x,t) has t >= f(x), so the optimal values coincide.
- **Q5 (what a passing submission shows):** Minimizer (1,1) with value 0.

</details>

### U8.2 Convex sets, cones, polyhedra and separation
**Sources:** PMO W3; CVX o, L1-9; AOW W2; EMML W8; LPCS W1–5, o; OFF W4; DOML W1
- **Topics:** Convex sets, examples of commonly occurring convex sets and convexity-preserving operations; separation result (a point and a closed convex set); hyperplanes and half-spaces; affine and linear combinations, cones and polyhedra; basics of convex optimization and basic properties of convex sets; introduction to polyhedral sets; separation theorems for convex sets; theorems of the alternative (Farkas' theorem, Gordan's theorem and other results); hyperplane separation theorems; Application: power constraints in wireless systems; convex sets and convex functions (week 1 DOML); structure behind convex optimization and why so many special cases can be solved efficiently; column space–row space duality; basic facts of convex optimization; mathematical optimization; motivation behind studying linear programming; basics of linear algebra for LP; algorithmic game theory, theoretical computer science and machine learning as application areas of LP; linear and affine combinations; this leads to the simplex algorithm; hyperplane separation theorems; Section III convex sets and convex functions.
- **Results:** Separating hyperplane theorem (point and closed convex set) [P]; supporting hyperplane theorem [P]; Farkas' lemma [P]; Gordan's theorem [P]; Carathéodory's theorem [P]; Minkowski/Krein–Milman for polytopes [S].
- **Build:** projection onto convex sets (ball, box, simplex, halfspace) from scratch; separating-hyperplane finder via QP.

**Assignment A8.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The intersection of any family of convex sets is

(A) always convex  
(B) never convex  
(C) convex only if finite  
(D) convex only if closed

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are convex sets?

(A) A hyperplane  
(B) The union of two disjoint intervals  
(C) A halfspace  
(D) The cone of positive semidefinite matrices

**Q3 (2 marks, numerical answer).** Distance from the point (3,4) to the closed unit ball.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove the separating hyperplane theorem for a point x0 outside a closed convex set C using the projection of x0 onto C.

**Q5 (3 marks, programming).** Implement projections onto a ball, a box, a halfspace and the probability simplex (sort-based). Verify the variational inequality (c - p).(x - p) <= 0 on random points. Predict the projection of (0.5, 0.5, 2) onto the simplex.

<details><summary>Key for A8.2 (open only after your attempt)</summary>

- **Q1:** A. Convex combinations stay in every member.
- **Q2:** ACD. Disjoint intervals are not convex together.
- **Q3:** 4 (tolerance ±0.001). Norm 5 minus radius 1.
- **Q4 (marking outline):** Let p be the projection; the vector x0 - p separates because (c - p).(x0 - p) <= 0 for all c in C.
- **Q5 (what a passing submission shows):** (0, 0, 1).

</details>

### U8.3 Convex functions and their calculus
**Sources:** PMO W3–4; CVX L1-9, L10-19; AOW W3; EMML W8; DOML W1–2; OMLH W3; MLESA W0
- **Topics:** Convex functions and their continuity, Lipschitz continuity and directional derivative; zeroth-order and first-order characterizations of convexity; second-order characterization of convexity; convexity-preserving operations; properties of convex functions; convex/concave functions, examples and conditions for convexity; continuity and differentiability properties of convex functions; differentiable convex functions; non-differentiable convex functions; calculus of sub-differentials (subdifferential of a convex function); Fenchel conjugate; strong convexity and its implications; first- and second-order conditions for optimization; application: beamforming in wireless systems, multi-user wireless, cognitive radio systems.
- **Results:** Jensen's inequality [P]; first-order condition f(y) ≥ f(x)+∇f(x)ᵀ(y−x) [P]; Hessian PSD ⇔ convex [P]; convex functions are locally Lipschitz in the interior [P]; subdifferential is nonempty, convex and compact in the interior [P]; Fenchel–Moreau (statement) [X]; strong convexity ⇒ unique minimizer and quadratic growth [P].
- **Build:** numerical convexity tester via random Hessian sampling; subgradient computation for ℓ1, hinge and max functions.

**Assignment A8.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Which function is convex on the real line?

(A) sin x  
(B) x^3  
(C) e^x  
(D) log x

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) A C^2 function is convex iff its Hessian is positive semidefinite  
(B) A sum of convex functions is convex  
(C) A pointwise maximum of convex functions is convex  
(D) A composition of convex functions is always convex

**Q3 (2 marks, numerical answer).** Length of the subdifferential interval of f(x) = abs(x) at x = 0.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove the first-order characterization: a differentiable f is convex iff f(y) >= f(x) + grad f(x).(y - x) for all x, y.

**Q5 (3 marks, programming).** Write a convexity tester sampling random points and Hessians by finite differences, and subgradient routines for hinge, L1 and max. Acceptance: softplus passes, sin fails. Predict the verdict for x^4 - x^2.

<details><summary>Key for A8.3 (open only after your attempt)</summary>

- **Q1:** C. Its second derivative is positive everywhere.
- **Q2:** ABC. Composition needs monotonicity conditions.
- **Q3:** 2 (tolerance ±0.001). The subdifferential is [-1, 1].
- **Q4 (marking outline):** One direction by the limit of the convexity inequality along a segment; the other by combining two supporting lines at a convex combination.
- **Q5 (what a passing submission shows):** Not convex: second derivative is negative near 0.

</details>

### U8.4 Unconstrained optimization theory
**Sources:** PMO W4–5; OMLH W3; OFF W2–3; CVX L20-26
- **Topics:** Local optima and its variants; saddle point; coercive functions; existence of optima (Weierstrass theorem; theorem for coercive functions); descent direction and its first-order and second-order characterizations; direction of descent; first-order and second-order necessary and sufficient conditions for minima; first- and second-order conditions for optimisation; optimization over open sets.
- **Results:** First-order necessary condition [P]; second-order necessary and sufficient conditions [P]; for convex f, stationary ⇒ global minimum [P]; coercive continuous functions attain their minimum [P].
- **Build:** classify the stationary points of Rosenbrock, Himmelblau and a saddle function by Hessian eigenvalues.

**Assignment A8.4** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** A necessary condition for an interior local minimum of a differentiable f is

(A) f = 0  
(B) grad f = 0  
(C) Hessian = 0  
(D) f is convex

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) f'(x) = 0 and f''(x) > 0 imply a strict local minimum  
(B) A continuous coercive function attains its minimum  
(C) A stationary point of a convex function is a global minimum  
(D) Every stationary point is a local minimum

**Q3 (2 marks, numerical answer).** Minimum value of f(x) = x^4 - 4x.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove the second-order necessary condition: if x* is a local minimizer of a C^2 function then the Hessian is positive semidefinite.

**Q5 (3 marks, programming).** Find stationary points of Himmelblau's function with Newton's method from 200 random starts, classify by Hessian eigenvalues and count each type. Predict the counts first.

<details><summary>Key for A8.4 (open only after your attempt)</summary>

- **Q1:** B. Fermat's condition.
- **Q2:** ABC. Saddles are stationary but not minima.
- **Q3:** -3 (tolerance ±0.001). f' = 4x^3 - 4 = 0 at x = 1, f = -3.
- **Q4 (marking outline):** Taylor expand along any direction d: f(x*+td) - f(x*) = (t^2/2) d^T H d + o(t^2) >= 0.
- **Q5 (what a passing submission shows):** Four minima, one maximum, four saddle points.

</details>

### U8.5 Constrained optimization theory: Lagrange, cones, Fritz John and KKT
**Sources:** PMO W8–9; CVX L10-19, o; DOML W2–3; AOW W6; EMML W12; MFML W10
- **Topics:** Revisit of the Lagrange multipliers method; cones for constrained optimization (cone, dual cone, cone of feasible directions, linearizing cone, cone of descent directions, tangent cone); geometric optimality conditions; first-order Fritz John (FJ) and KKT necessary optimality conditions; first-order KKT sufficient optimality condition; second-order KKT necessary and sufficient conditions; constraint qualification; Rockafellar–Pshenichny optimality condition; properties of normals and projections; projection on a convex set and normal cone; computing the normal cone of inequality constraints; tangent cone; minimization of a convex function with convex inequality constraints; constrained optimization problems (primal and Lagrangian dual); KKT conditions and primal/dual methods; Lagrangian multiplier method; Karush–Kuhn–Tucker conditions (CVX outline); saddle-point conditions; Karush–Kuhn–Tucker conditions; projection on a convex set and normal cone; sub-differential of a convex function (subdifferential); Section VI constraint optimization theory.
- **Results:** Lagrange multiplier theorem [P under regularity]; Fritz John conditions [P]; KKT necessary conditions under LICQ/MFCQ [P]; KKT sufficient for convex problems [P]; Slater's condition [P in U8.6].
- **Build:** KKT-system solver for small QPs; verification of KKT residuals on solutions from `scipy.optimize`.

**Assignment A8.5** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** KKT stationarity for min f(x) subject to g(x) <= 0 is

(A) grad f = 0  
(B) grad f + lambda grad g = 0 with lambda >= 0  
(C) grad f = lambda grad g with lambda < 0  
(D) g = 0 always

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Complementary slackness requires lambda g(x*) = 0  
(B) KKT conditions are necessary under a constraint qualification  
(C) KKT conditions are sufficient for convex problems  
(D) Multipliers of inequality constraints may be negative in standard form

**Q3 (2 marks, numerical answer).** Lagrange multiplier at the solution of min x^2 subject to x >= 1 (written 1 - x <= 0).

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that for a convex problem any point satisfying the KKT conditions is a global minimizer.

**Q5 (3 marks, programming).** Solve min 0.5 x^T Q x + c^T x s.t. A x <= b for 2 variables by enumerating active sets and checking KKT. Report the residual. Predict how many active sets you must check for 3 constraints.

<details><summary>Key for A8.5 (open only after your attempt)</summary>

- **Q1:** B. Plus complementary slackness lambda g = 0.
- **Q2:** ABC. They must be nonnegative.
- **Q3:** 2 (tolerance ±0.001). 2x - lambda = 0 with x = 1 gives lambda = 2.
- **Q4 (marking outline):** The Lagrangian is convex in x, so stationarity gives its global minimum; weak duality and complementary slackness equate the values.
- **Q5 (what a passing submission shows):** At most 2^3 = 8 candidate active sets; residual below 1e-9.

</details>

### U8.6 Lagrangian duality, saddle points and minimax
**Sources:** PMO W10; CVX o, L10-19; DOML W2–3,7; AOW W6; EMML W12; LPCS W4–6; OFF W6–7
- **Topics:** Lagrangian duality (how one discovers duality; geometric interpretation of duality); results on the dual function (the dual problem is a convex optimization problem; differentiability of the dual function); weak duality theorem and duality gap; equal primal and dual objective values imply optimality; strong duality theorem (convex problem and Slater's constraint qualification imply strong duality); saddle-point optimality and absence of duality gap; relationship between saddle-point criteria and KKT conditions; duality in connection with linear programming; strong duality for convex problems and consequences; Lagrangian duality and examples; duality principle and KKT framework for optimization; concepts of duality, hard and soft margin classifier (SVM dual); duality theory and strong duality (LP); Von Neumann's minimax theorem as an application of strong duality; existence of Nash equilibria; Yao's technique for lower bounds in communication complexity; the relation between primal and dual used to prove the max-flow min-cut theorem; primal–dual methods and an algorithm for max flow; dual ascent and dual decomposition; application: water-filling power allocation; duality theory, one of the main reasons LP has so many applications; Nash equilibria (John Nash); primal–dual methods; an algorithm for the max-flow problem; Section VII Lagrangian duality theory.
- **Results:** Weak duality [P]; strong duality under Slater [P]; LP strong duality [P]; complementary slackness [P]; Von Neumann minimax theorem [P]; Nash existence for finite two-player zero-sum games [P]; max-flow = min-cut [P].
- **Build:** dual of an LP and of an SVM computed and checked numerically; zero-sum game solved by LP.

**Assignment A8.6** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** For a minimization problem, weak duality states

(A) dual optimum <= primal optimum  
(B) dual optimum >= primal optimum  
(C) they are always equal  
(D) the dual is nonconvex

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Strong duality holds for convex problems under Slater's condition  
(B) The dual function is concave  
(C) For a feasible bounded LP, strong duality holds  
(D) The duality gap is always zero

**Q3 (2 marks, numerical answer).** Dual optimal value of min 3 x1 + 2 x2 s.t. x1 + x2 >= 4, x >= 0.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove weak duality for min f(x) s.t. g(x) <= 0: the dual function lower-bounds the primal optimum.

**Q5 (3 marks, programming).** Compute the value of the zero-sum game [[3,-1],[-2,4]] analytically and by fictitious play for 10^5 rounds. Predict the value first.

<details><summary>Key for A8.6 (open only after your attempt)</summary>

- **Q1:** A. Any dual function value lower-bounds the primal optimum.
- **Q2:** ABC. Gaps can be positive for nonconvex problems.
- **Q3:** 8 (tolerance ±0.001). The dual max 4 y s.t. y <= 3, y <= 2 gives 8.
- **Q4 (marking outline):** For feasible x and lambda >= 0, L(x, lambda) <= f(x), and the dual function is the infimum of L over x.
- **Q5 (what a passing submission shows):** Value 1; fictitious play empirical value approaches 1.

</details>

### U8.7 Linear programming: simplex, duality, sensitivity and interior-point methods
**Sources:** CVX L10-19, L20-26, L27-33, o; HEM W9–10, o; LPCS W1–3,7–8, o; OFF W5–7; OAT W9–11; AOW W4; EMML W11; MFML W10
- **Topics:** Pleasures of linear programming; direction of descent; extreme points of linear programming; polyhedral sets and cones; foundation of simplex methods; fundamental theorem of linear programming; simplex methods (and continued); simplex method; two-phase method II; dual simplex method and its application; sensitivity analysis I; graphical method I and II; introduction to linear programming; Gaussian elimination, rank–nullity, basics of LP and its definition; linear programming basics and examples; basic results and the fundamental theorems of linear programming; introduction to interior-point methods; log barrier function; primal–dual framework; overview of interior-point algorithm; short-step algorithm and short-step path-following method; predictor–corrector method; affine scaling method; Karmarkar's algorithm; LP with integer constraints and relaxation (ILP, rounding, approximation algorithm for set cover); applications of LP in machine learning (linear regression and classification by LP tools, Boolean functions); error-minimizing LPP; Linear programming problems (HEM main topic 3); linear program application: power allocation in multi-cell cooperative OFDM; introduction to linear programming and duality; short-step path-following method; modelling a quantity as an integer linear program (ILP) and the concept of relaxation of a linear program; linear regression and classification approached with LP tools; Section VIII linearly constrained nonlinear optimization algorithms.
- **Results:** Fundamental theorem of LP (optimum at a vertex) [P]; simplex terminates under Bland's rule [P]; strong duality and complementary slackness [P]; polynomial-time convergence of short-step path-following [S]; integrality gap of LP relaxation of set cover and rounding bound [P]; ℓ1 and ℓ∞ regression as LPs [D].
- **Build:** tableau simplex (two-phase and dual) from scratch; log-barrier interior-point method from scratch; compare with `scipy.optimize.linprog`.
- **Gap-fills:** *[inferred: Chvátal; Dantzig–Thapa]* degeneracy and cycling, network simplex, transportation and assignment problems, total unimodularity.

**Assignment A8.7** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** If a linear program has an optimum and its feasible region is a pointed polyhedron, an optimum is attained at

(A) an interior point  
(B) a vertex  
(C) the origin  
(D) the centroid

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) The simplex method moves between vertices  
(B) Bland's rule prevents cycling  
(C) Interior-point methods follow the central path  
(D) The dual simplex method maintains primal feasibility

**Q3 (2 marks, numerical answer).** Maximum of 3x + 2y subject to x + y <= 4, x <= 2, x, y >= 0.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that if an LP in standard form has an optimal solution, it has an optimal basic feasible solution.

**Q5 (3 marks, programming).** Implement tableau simplex (two-phase) and a log-barrier interior-point method. Solve the example above and report the dual values. Predict the optimal dual variables.

<details><summary>Key for A8.7 (open only after your attempt)</summary>

- **Q1:** B. Fundamental theorem of linear programming.
- **Q2:** ABC. It maintains dual feasibility.
- **Q3:** 10 (tolerance ±0.001). Vertex (2,2) gives 10.
- **Q4 (marking outline):** Take an optimal solution with the fewest positive entries; if its columns were dependent, move along the null direction without worsening the cost, reducing support.
- **Q5 (what a passing submission shows):** Optimum 10 at (2,2); duals 2 for the sum constraint and 1 for x <= 2.

</details>

### U8.8 Unconstrained descent methods: line search, gradient, Newton, quasi-Newton, conjugate gradient, trust region
**Sources:** PMO W5–8; OAT W3–6; OMLH W4,7–8; OFF W10–11; EMML W9–10; MFML W10; FML W4; DOML W3
- **Topics:** General structure of an optimization algorithm, global convergence, descent property, quadratic termination property; introduction to line search (exact and inexact); inexact line searches (Armijo–Goldstein, Wolfe–Powell, Armijo backtracking); global convergence of gradient descent methods using exact and inexact line searches; where general descent methods converge (almost always to a local minimizer; capture theorem); scaling of variables; practical stopping criteria; steepest descent method, descent property, zigzagging, scaling effect, Barzilai–Borwein gradient method; global convergence of steepest descent and its order of convergence, scaling effect and dimension independence; Newton method and its local convergence; dimension dependency of Newton method and scaling effect; Levenberg–Marquardt and other modified Newton methods; quasi-Newton methods (quasi-Newton equation, general quasi-Newton algorithm, variable metric method, comparison of Newton and quasi-Newton methods); global convergence of quasi-Newton methods for uniformly convex functions; superlinear convergence of quasi-Newton methods; basic conjugate direction method and its convergence rate (basic CG method); gradient descent/conjugate gradient algorithm; Newton's method; quasi-Newton methods; trust region methods (Cauchy point, dogleg and double dogleg methods); gradient descent: math and programming of basic optimization problems and their solutions; Newton's method and optimization for ML in practice with PyTorch/TensorFlow; gradient descent and other optimization algorithms in machine learning; gradient descent primal and dual view and convergence for linear and logistic regression; Barzilai and Borwein (Borwin) gradient method; dog leg and double dog leg methods; Section V unconstrained optimization methods; continued lectures on Newton and quasi-Newton methods.
- **Results:** Convergence of gradient descent for L-smooth convex functions at rate O(1/k) and for strongly convex at linear rate [P]; Zoutendijk condition [P]; local quadratic convergence of Newton [P]; superlinear convergence of BFGS [S]; CG finds the minimizer of an n-dimensional quadratic in ≤ n steps [P]; Armijo backtracking terminates [P].
- **Build:** GD with backtracking, Newton, BFGS/L-BFGS, CG and dogleg trust region from scratch; iteration-count and condition-number experiments on quadratics and Rosenbrock; compare with `scipy.optimize.minimize`.
- **Gap-fills:** *[inferred: Nocedal–Wright Ch.3–7; Dennis–Schnabel]* Wolfe-condition line-search algorithms, limited-memory BFGS, nonlinear least squares (Gauss–Newton), derivative-free methods.

**Assignment A8.8** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Steepest descent on a badly conditioned quadratic typically

(A) zigzags and converges slowly  
(B) converges in one step  
(C) diverges always  
(D) ignores curvature and is exact

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Newton's method converges quadratically near a nondegenerate minimizer  
(B) BFGS converges superlinearly  
(C) Conjugate gradient solves an n-dimensional quadratic in at most n steps  
(D) Gradient descent converges for every step size

**Q3 (2 marks, numerical answer).** Gradient descent on f = x^2/2 with step 0.5 from x0 = 4. Value after 3 steps.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that gradient descent with step 1/L on an L-smooth, mu-strongly convex quadratic contracts the error by a factor of at most (1 - mu/L) per step.

**Q5 (3 marks, programming).** Implement GD with backtracking, Newton, BFGS and conjugate gradient. Compare iteration counts on quadratics with condition numbers 10 and 1000. Predict the CG iteration count for n = 20.

<details><summary>Key for A8.8 (open only after your attempt)</summary>

- **Q1:** A. Rate is governed by the condition number.
- **Q2:** ABC. Large steps diverge.
- **Q3:** 0.5 (tolerance ±0.001). Each step multiplies x by 0.5.
- **Q4 (marking outline):** Error update e <- (I - A/L) e; eigenvalues of I - A/L lie in [0, 1 - mu/L].
- **Q5 (what a passing submission shows):** At most 20 iterations in exact arithmetic; GD needs hundreds for condition 1000.

</details>

### U8.9 Constrained optimization algorithms: QP, projected and reduced gradient, penalty, augmented Lagrangian, SQP
**Sources:** PMO W11–12; OAT W7–8; OFF W10–11; DOML W6; OMLH W5–6
- **Topics:** Quadratic programming methods (active-set method; interior-point method); projected gradient algorithm; reduced gradient algorithm; penalty methods (exterior penalty method; interior penalty method); quadratic penalty method; augmented Lagrangian method and method of multipliers; sequential quadratic programming (Lagrange–Newton method; reduced Hessian matrix method); trust region method; null space method; linearly constrained and nonlinearly constrained nonlinear optimization algorithms; projected gradient descent; Section IX nonlinearly constrained nonlinear optimization algorithms; continued lectures on variants of gradient descent and neural-network training theory; Section VIII: linearly constrained nonlinear optimization algorithms.
- **Results:** Exterior penalty solutions converge to a constrained minimizer as the penalty grows [P]; augmented Lagrangian avoids ill-conditioning and converges with bounded penalty [S]; SQP as Newton on the KKT system [D]; active-set termination for convex QP [S].
- **Build:** quadratic-penalty and augmented-Lagrangian solvers from scratch on a small equality-constrained problem; projected gradient onto the simplex.
- **Gap-fills:** *[inferred: Nocedal–Wright Ch.16–18; Bertsekas]* filter methods and merit functions, barrier methods (link to U8.7 IPM).

**Assignment A8.9** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The quadratic penalty method may suffer because

(A) the penalty must grow, making the problem ill-conditioned  
(B) it needs no gradients  
(C) it is exact for finite penalty  
(D) it ignores constraints

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Augmented Lagrangian methods avoid sending the penalty to infinity  
(B) Projected gradient requires an easy projection  
(C) SQP applies Newton's method to the KKT system  
(D) Exterior penalty iterates are always feasible

**Q3 (2 marks, numerical answer).** Minimizer of x^2 + 9 (x - 1)^2 (quadratic penalty for min x^2 s.t. x = 1, mu = 9).

**Q4 (2 marks, prove or derive; every step with its reason).** For min x^2 s.t. x = 1, derive the penalty minimizer for general mu and show it converges to the constrained solution as mu goes to infinity.

**Q5 (3 marks, programming).** Solve min x^2 + y^2 s.t. x + y = 1 with quadratic penalty and with augmented Lagrangian; compare iteration counts and condition numbers. Predict the solution.

<details><summary>Key for A8.9 (open only after your attempt)</summary>

- **Q1:** A. Conditioning degrades as mu grows.
- **Q2:** ABC. They approach feasibility from outside.
- **Q3:** 0.9 (tolerance ±0.001). Derivative: 2x + 18 (x - 1) = 0 gives x = 0.9.
- **Q4 (marking outline):** Set 2x + 2 mu (x - 1) = 0 so x = mu/(1+mu), which tends to 1.
- **Q5 (what a passing submission shows):** (0.5, 0.5); augmented Lagrangian reaches it with a bounded penalty.

</details>

### U8.10 First-order methods for ML: stochastic, accelerated, proximal, adaptive, and the dynamical-systems view
**Sources:** OMLH W5–8; DOML W3–6; FML W4–5; MLCE W5; FDL W2; OAT W12; MFML W10; MLESA W5
- **Topics:** Variants of gradient descent (projected, stochastic, proximal, accelerated, coordinate descent) and training a neural network (theory and implementation); analysis of gradient descent; analysis of accelerated optimization algorithms; optimization algorithms as dynamical systems and introduction to stability theory; Lyapunov analysis of gradient flows; gradient flows for equality-constrained optimization and saddle-point problems; accelerated gradient flows; SGD and its analysis for linear and logistic regression, SGD versus GD as a learning algorithm, model selection; training of ML models; gradient descent algorithm; stochastic gradient descent; momentum-based GD, Nesterov accelerated GD, AdaDelta, AdaGrad, RMSProp, Adam; variants such as momentum, AdaGrad, Adam and RMSprop; gradient descent and stochastic gradient descent (MFML); an application from machine learning (OAT Week 12); initialization, training and validation; along with implementation and optimization in real-world applications.
- **Results:** SGD convergence for convex and strongly convex objectives with variance bound [P]; Nesterov's O(1/k²) rate and its optimality [S]; Lyapunov function for gradient flow gives exponential convergence for strongly convex f [P]; proximal gradient converges at O(1/k) [P]; Adam update as adaptive preconditioning (no general convergence guarantee, counterexample) [S].
- **Build:** SGD, momentum, Nesterov, AdaGrad, RMSProp and Adam from scratch in NumPy on least squares and logistic regression; ODE-view simulation of gradient flow versus discrete GD.
- **Gap-fills:** *[inferred: Bach LTFP Ch.5; Goodfellow Ch.8]* learning-rate schedules, mini-batching and variance reduction (SVRG), second-order and natural-gradient ideas.

**Assignment A8.10** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** SGD with a constant step size converges

(A) exactly for any loss  
(B) to a neighbourhood of the minimizer  
(C) never  
(D) only if the loss is linear

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Momentum accelerates movement along consistently signed gradients  
(B) Adam uses first and second moment estimates  
(C) Nesterov acceleration attains O(1/k^2) on smooth convex problems  
(D) AdaGrad's effective step size grows over time

**Q3 (2 marks, numerical answer).** Adam's first update magnitude with learning rate 0.001, gradient 1 and epsilon 1e-8.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that gradient descent is the Euler discretization of the gradient flow x' = -grad f(x) and that f decreases along the flow at rate norm(grad f)^2.

**Q5 (3 marks, programming).** Implement SGD, momentum, Nesterov, AdaGrad, RMSProp and Adam on least squares and on logistic regression and plot loss curves. Predict which optimizer is least sensitive to feature scaling.

<details><summary>Key for A8.10 (open only after your attempt)</summary>

- **Q1:** B. Gradient noise keeps it from converging exactly.
- **Q2:** ABC. It shrinks.
- **Q3:** 0.001 (tolerance ±0.0001). Bias-corrected m = 1 and v = 1 give about the learning rate.
- **Q4 (marking outline):** d/dt f(x(t)) = grad f . x' = -norm(grad f)^2.
- **Q5 (what a passing submission shows):** Adam and RMSProp are least sensitive because they rescale per coordinate.

</details>

### U8.11 Conic and structured convex programs: QCQP, SOCP, SDP, geometric programs
**Sources:** AOW W4–6,9, o; CVX o, L34-40; MLESA W0
- **Topics:** Convex optimization problems; linear programs; QCQP and SOCP problems; application: channel shortening for wireless equalization and robust beamforming in wireless systems; semi-definite programming (SDP); saddle-point type conditions for SDP; approximate solutions; geometric programs and optimal power allocation for cooperative communication; optimization for MIMO systems, OFDM systems and MIMO-OFDM systems; cognitive radio and cooperative communication.
- **Results:** Every LP, QP, QCQP and SOCP is an SDP-representable convex program [P]; Schur-complement representation of quadratic constraints [P]; GP becomes convex under log transformation [P]; SDP strong duality under strict feasibility [S].
- **Build:** the same problems solved with from-scratch IPM and with `cvxpy`, with solver comparison. **Tooling:** from-scratch interior point in NumPy; `cvxpy` as the reference solver.

**Assignment A8.11** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Second-order cone programs generalize

(A) only LP  
(B) LP and convex QCQP  
(C) nonconvex problems  
(D) only integer programs

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Every LP is a semidefinite program  
(B) A geometric program becomes convex after a log transform  
(C) A QCQP is convex if every quadratic form is PSD  
(D) SDP solves every nonconvex problem exactly

**Q3 (2 marks, numerical answer).** Largest x with [[1,x],[x,1]] positive semidefinite.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that norm(A x + b) <= c^T x + d is a second-order cone constraint and that squaring gives a convex quadratic constraint when c^T x + d >= 0.

**Q5 (3 marks, programming).** Solve min c^T x s.t. norm(x) <= 1 with your own log-barrier method for c = (3,4). Compare with the analytic solution. Predict the optimal value.

<details><summary>Key for A8.11 (open only after your attempt)</summary>

- **Q1:** B. A convex quadratic constraint is a cone constraint.
- **Q2:** ABC. SDP gives relaxations, not exact solutions in general.
- **Q3:** 1 (tolerance ±0.001). Eigenvalues 1 plus or minus x need to be nonnegative.
- **Q4 (marking outline):** The constraint is membership of (Ax+b, c^T x + d) in the Lorentz cone.
- **Q5 (what a passing submission shows):** Optimal value -5 at x = -c/norm(c).

</details>

### U8.12 Applications of optimization: signal estimation, compressive sensing, radar, big data and finance
**Sources:** AOW W2–12, o; EMML o; MLCE W4
- **Topics:** Optimization for signal estimation (LS, WLS, regularization); wireless channel estimation; image reconstruction and deblurring; convex optimization for machine learning (PCA and SVM); compressive sensing and sparse signal processing; OMP (orthogonal matching pursuit); LASSO (least absolute shrinkage and selection operator) for signal estimation; radar for target detection, array processing, MUSIC and MIMO-radar schemes for enhanced target detection; convex optimization for big-data analytics, recommender systems, user-rating prediction and latent-factor methods; optimization for finance (financial models and portfolio optimization); water-filling power allocation; loss functions as optimization objectives (MSE, MAE, MSLE, cross-entropy, Tweedie, MAPE) and their statistical basis; Principal Component Analysis (PCA); Support Vector Machines (SVM); LASSO techniques; wireless communication, signal processing, machine learning, big data and finance as application fields.
- **Results:** LASSO yields sparse solutions (subgradient optimality) [D]; restricted-isometry sufficient condition for exact recovery (statement) [X]; water-filling is the KKT solution of capacity maximization [D]; Markowitz mean–variance solution [D].
- **Build:** ISTA and coordinate-descent LASSO; OMP recovery experiments (phase transition); water-filling solver.

**Assignment A8.12** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The LASSO penalty promotes sparsity because

(A) L1 balls have corners on the axes  
(B) it is smooth  
(C) it equals L2  
(D) it ignores data

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) ISTA uses soft thresholding  
(B) Water-filling is the KKT solution for capacity maximization  
(C) Orthogonal matching pursuit is greedy  
(D) Compressive sensing requires dense signals

**Q3 (2 marks, numerical answer).** Soft-threshold of 2.5 with threshold 1.

**Q4 (2 marks, prove or derive; every step with its reason).** Derive soft thresholding as the proximal operator of lambda times abs(x).

**Q5 (3 marks, programming).** Implement ISTA and coordinate-descent LASSO, OMP, and a water-filling solver for four channels with gains 1, 2, 4, 8 and total power 4. Predict the water level.

<details><summary>Key for A8.12 (open only after your attempt)</summary>

- **Q1:** A. Level sets of the loss often first touch corners.
- **Q2:** ABC. It exploits sparsity.
- **Q3:** 1.5 (tolerance ±0.001). sign(x) max(abs(x) - 1, 0) = 1.5.
- **Q4 (marking outline):** Minimize 0.5 (z - x)^2 + lambda abs(z); case on the sign of z.
- **Q5 (what a passing submission shows):** Water level between the channel noise levels; the weakest channel gets zero power if its level exceeds the water level.

</details>

### U8.13 Non-smooth and difference-of-convex optimization
**Sources:** CVX o, L34-40
- **Topics:** Descent direction for non-smooth functions; minimization of difference-convex (DC) functions (and continued); approximate solutions; concluding lecture (overview of convex optimization).
- **Results:** Optimality 0 ∈ ∂f(x) [P]; subgradient method convergence rate [P]; DC algorithm (DCA) monotone descent [P].
- **Build:** subgradient method for hinge-loss SVM; DCA for a sparse regression with a non-convex penalty.

**Assignment A8.13** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** For a convex f, x* is a minimizer iff

(A) 0 is in the subdifferential at x*  
(B) f(x*) = 0  
(C) the gradient is positive  
(D) the Hessian is zero

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) The subgradient method converges at O(1/sqrt k) in objective  
(B) DCA monotonically decreases a DC objective  
(C) Every subgradient step decreases the objective  
(D) abs(x) is differentiable at 0

**Q3 (2 marks, numerical answer).** Largest subgradient of f(x) = max(0, x) at x = 0.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that for convex f, 0 belongs to the subdifferential at x* iff x* minimizes f.

**Q5 (3 marks, programming).** Train a hinge-loss linear classifier by the subgradient method with diminishing steps on a toy dataset, and apply a DC algorithm to a sparse regression with a nonconvex penalty. Predict the shape of the objective curve.

<details><summary>Key for A8.13 (open only after your attempt)</summary>

- **Q1:** A. Subgradient optimality.
- **Q2:** AB. Subgradient steps need not descend.
- **Q3:** 1 (tolerance ±0.001). The subdifferential is [0,1].
- **Q4 (marking outline):** Subgradient inequality f(y) >= f(x*) + 0.(y - x*) is exactly minimality.
- **Q5 (what a passing submission shows):** Noisy non-monotone objective for the subgradient method; monotone decrease for DCA.

</details>

### U8.14 Distributed optimization: graphs, consensus, ADMM and dual decomposition
**Sources:** DOML W1,7–10, o; MFML o
- **Topics:** Introduction to distributed optimization; ADMM (alternating direction method of multipliers); dual ascent and dual decomposition; introduction to graph theory; distributed consensus; continuous-time analysis of consensus algorithms; distributed optimization problem (economic dispatch problem); distributed optimization algorithms; centralized versus distributed or decentralized algorithms under communication overhead, network topology, computational resources and robustness; graph theory, iterative methods for convex problems, synchronous and asynchronous setups, consensus algorithms; recent literature that exploits control theory for accelerated distributed optimization algorithms; graph theory, iterative methods for convex problems; distributed machine learning; synchronous and asynchronous setups.
- **Results:** ADMM convergence for convex problems [S]; consensus convergence rate governed by the second-smallest Laplacian eigenvalue [P]; dual decomposition for separable problems [D]; distributed gradient descent converges to a neighbourhood with constant steps [S].
- **Build:** ADMM for LASSO and consensus averaging over a graph from scratch (reuses U1.4 and U4.8).
- **Gap-fills:** *[inferred: Nedić, Distributed Optimization Over Networks; Boyd et al., ADMM monograph]* push-sum and directed graphs, gradient tracking, asynchronous updates.

**Assignment A8.14** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Averaging consensus on a connected undirected graph converges to

(A) the maximum  
(B) the average of initial values  
(C) zero  
(D) a random value

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Convergence rate is governed by the Laplacian's second-smallest eigenvalue  
(B) ADMM alternates minimization over blocks and a dual update  
(C) Dual decomposition applies to separable objectives  
(D) Consensus reaches the global mean on a disconnected graph

**Q3 (2 marks, numerical answer).** Second-smallest eigenvalue of the Laplacian of a path on 3 nodes.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that x <- (I - eps L) x preserves the average and converges to it on a connected graph when 0 < eps < 2/lambda_max(L).

**Q5 (3 marks, programming).** Run averaging consensus on a ring of 10 nodes and on the complete graph, and ADMM for LASSO. Predict which graph converges faster.

<details><summary>Key for A8.14 (open only after your attempt)</summary>

- **Q1:** B. With symmetric doubly stochastic weights.
- **Q2:** ABC. Components never mix.
- **Q3:** 1 (tolerance ±0.001). Eigenvalues 0, 1, 3.
- **Q4 (marking outline):** 1^T L = 0 preserves the sum; other eigenmodes contract by abs(1 - eps lambda_i) < 1.
- **Q5 (what a passing submission shows):** The complete graph; the ring needs far more iterations.

</details>

### U8.15 Dynamic optimization and complementarity problems
**Sources:** OFF W8–9,12, o
- **Topics:** Nonlinear and convex optimization (Weeks 8–9); complementarity problems and algorithms for the same; dynamic optimization; real analysis and convexity as the base for LP, convex optimization and nonlinear programming.
- **Results:** Bellman's principle of optimality [P]; finite-horizon dynamic programming recursion [P]; KKT conditions as a complementarity problem [D].
- **Build:** value-iteration and backward-induction solver for a finite-horizon problem (feeds U10.4 MDPs).
- **Gap-fills:** *[inferred: Bertsekas, Dynamic Programming and Optimal Control]* linear–quadratic regulator, Pontryagin principle (statement), calculus of variations.

**Assignment A8.15** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Bellman's principle of optimality says that

(A) any tail of an optimal policy is optimal for its subproblem  
(B) greedy is always optimal  
(C) optimal policies are unique  
(D) costs must be convex

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Finite-horizon DP works backward from the last stage  
(B) KKT conditions can be written as a complementarity problem  
(C) The LQR solution comes from a Riccati recursion  
(D) A greedy choice is always optimal

**Q3 (2 marks, numerical answer).** Shortest path cost A to D with edges A-B 2, A-C 5, B-C 1, B-D 4, C-D 1.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove the principle of optimality for finite-horizon deterministic DP: the value function satisfies V_t(x) = min over u of cost + V_{t+1}(next state).

**Q5 (3 marks, programming).** Implement backward induction for a finite-horizon inventory problem and value iteration for the infinite-horizon discounted version. Verify the policies agree for a long horizon. Predict the form of the optimal policy.

<details><summary>Key for A8.15 (open only after your attempt)</summary>

- **Q1:** A. Substructure.
- **Q2:** ABC. Greedy fails without special structure.
- **Q3:** 4 (tolerance ±0.001). The path A-B-C-D costs 4.
- **Q4 (marking outline):** If a tail were improvable, replacing it would improve the whole path.
- **Q5 (what a passing submission shows):** A base-stock (order-up-to) policy.

</details>

### U8.16 Stochastic approximation: algorithms, step sizes and the ODE method
**Sources:** SA W1,5–6, o
- **Topics:** Introduction to stochastic approximation: iterative algorithms that locate zeroes or optimal points of functions when function evaluations are compromised by noise; motivating examples from web-crawling and reinforcement learning; applications in regression, system identification, adaptive control and machine learning; the Robbins–Monro scheme and stochastic gradient descent as special cases; step-size conditions (sum of steps infinite, sum of squares finite); convergence of stochastic approximation algorithms by the ODE method (martingale noise, interpolated trajectory, asymptotic pseudo-trajectory, limit set of the algorithm as an internally chain transitive set of the mean ODE); ODE method continued: convergence to equilibria under a Lyapunov function.
- **Results:** Gronwall-based tracking lemma (the interpolated iterates follow the ODE on every finite horizon) [P]; martingale noise vanishes along tails for square-summable steps [P]; Robbins–Monro convergence with a Lyapunov function [S]; the limit set of the iterates is internally chain transitive [X, stated from U7.7].
- **Build:** Robbins–Monro mean estimation and root finding with noise; SGD as stochastic approximation; compare step sizes 1/n and n^-0.6; plot iterates against the mean ODE.
- **Gap-fills:** *[inferred: Borkar, *Stochastic Approximation: A Dynamical Systems Viewpoint*, recalled, not checked]* Kiefer–Wolfowitz finite-difference variant; asynchronous updates (needed in U10.6).

**Assignment A8.16** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The Robbins-Monro step-size conditions are

(A) sum of steps infinite and sum of squares finite  
(B) steps constant  
(C) steps growing  
(D) sum of steps finite

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) SGD is a special case of stochastic approximation  
(B) Steps a_n = n^-0.6 satisfy the Robbins-Monro conditions  
(C) A constant step size converges exactly to the zero  
(D) The ODE method compares the iterates to a mean ODE

**Q3 (2 marks, numerical answer).** Running estimate x_n = x_(n-1) + (1/n)(X_n - x_(n-1)), x_0 = 0, observations 2, 4, 6. Value of x_3.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that the recursion with steps 1/n produces the sample mean and satisfies the Robbins-Monro conditions.

**Q5 (3 marks, programming).** Run Robbins-Monro root finding for f(x) = x - 3 with unit Gaussian noise using steps 1/n, n^-0.6 and a constant 0.1. Plot the error. Predict which gives the lowest final error and which has a noise floor.

<details><summary>Key for A8.16 (open only after your attempt)</summary>

- **Q1:** A. They average out the noise while still reaching the target.
- **Q2:** ABD. Constant steps leave a noise floor.
- **Q3:** 4 (tolerance ±0.001). The recursion is the running mean, 4.
- **Q4 (marking outline):** Induction on n for the mean; the harmonic series diverges and the sum of 1/n^2 converges.
- **Q5 (what a passing submission shows):** 1/n gives the lowest error; the constant step has a noise floor.

</details>

### U8.17 Convergence rates, stability, two-timescale algorithms and stochastic recursive inclusions
**Sources:** SA W7–10, o
- **Topics:** Convergence rates of linear stochastic approximation algorithms; stability of stochastic approximation algorithms (boundedness of the iterates); two-timescale stochastic approximation: convergence; stochastic recursive inclusions: convergence (set-valued drift, differential inclusions).
- **Results:** Mean-square error of linear stochastic approximation with steps c/n decays like 1/n under a condition on c [D]; asymptotic normality at the square-root rate [S]; Borkar–Meyn stability criterion via the scaled ODE [S]; two-timescale convergence [S]; convergence of stochastic recursive inclusions to invariant sets of the differential inclusion [S].
- **Build:** rate experiments for linear stochastic approximation with several constants c; a two-timescale example on a small bandit actor–critic; the subgradient method as a stochastic recursive inclusion.
- **Gap-fills:** *[inferred: Borkar, recalled, not checked]* Polyak–Ruppert averaging, Markov-noise and constant-step-size analysis.

**Assignment A8.17** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** In two-timescale stochastic approximation the fast iterate sees the slow iterate as

(A) quasi-static  
(B) random noise only  
(C) diverging  
(D) zero

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) The Borkar-Meyn criterion uses the scaled ODE to prove stability  
(B) Polyak-Ruppert averaging improves the asymptotic rate constant  
(C) The mean-square error of linear stochastic approximation with steps c/n decays like 1/n under a condition on c  
(D) Stability of the iterates is automatic

**Q3 (2 marks, numerical answer).** Asymptotic variance c^2 sigma^2/(2c - 1) of sqrt(n)(x_n - theta) for c = 2 and sigma = 1.

**Q4 (2 marks, prove or derive; every step with its reason).** Derive, to first order in 1/n, the recursion v_(n+1) = (1 - 2c/n) v_n + c^2 sigma^2/n^2 for the variance of linear stochastic approximation with unit slope and show n v_n tends to c^2 sigma^2/(2c - 1) when c > 1/2.

**Q5 (3 marks, programming).** Simulate the linear recursion x_(n+1) = x_n + (c/n)(-(x_n - theta) + noise) for c = 0.4, 1, 2 and estimate n times the mean-square error. Predict which c converges slower than 1/n.

<details><summary>Key for A8.17 (open only after your attempt)</summary>

- **Q1:** A. Time-scale separation.
- **Q2:** ABC. Boundedness must be proved.
- **Q3:** 1.333 (tolerance ±0.001). 4/3.
- **Q4 (marking outline):** Expand the squared error; substitute n v_n = w_n and analyse the fixed point.
- **Q5 (what a passing submission shows):** c = 0.4, which is below 1/2.

</details>


# PART B. MACHINE LEARNING

## D9. Machine Learning Foundations: Supervised, Unsupervised, Probabilistic, Data Mining and Learning Theory

Aim: nine dedicated source courses (engineering ML, IIT ML courses, KTH symbolic ML, data mining, statistical ML) merged into one classical-ML ladder, each algorithm built from scratch in NumPy first, then compared with scikit-learn. Benchmarks (recalled, not checked unless noted): Bishop, *Pattern Recognition and Machine Learning*; Hastie–Tibshirani–Friedman, *The Elements of Statistical Learning*; Murphy, *Probabilistic Machine Learning: An Introduction* (book site confirmed: a long contents PDF exists, not retrievable as text); Bach, *Learning Theory from First Principles* (chapters confirmed: mathematical preliminaries, supervised learning, least-squares regression, empirical risk minimization, optimization, local averaging, kernel methods, sparse methods, neural networks, ensemble learning, online learning to bandits, overparameterized models, structured prediction, probabilistic methods, lower bounds); Mitchell, *Machine Learning*; Alpaydin; Duda–Hart–Stork; Rengaswamy–Suresh, *Data Science for Engineers*; Deisenroth et al. Part II (when models meet data, linear regression, PCA, GMM, SVM).

### U9.0 History of AI, symbolic AI and the machine-learning workflow
**Sources:** GEN 2.1, 2.2, 2.3, 2.4, 2.5, 2.6
- **Topics:** History of AI: the birth of AI (the 1956 Dartmouth Conference), major milestones, the Turing Test, what is artificial intelligence; the symbolic AI era: representing knowledge (logic, rule-based inference, semantic nets), expert systems, hitting the wall (the AI winter); machine learning and data: data as the fuel of machine learning, the journey of AI; supervised learning: core paradigms, workflow (train/test split, training, testing), tutorial with scikit-learn (with NumPy and Matplotlib), evaluation metrics (confusion matrix; accuracy, precision, recall, F1); unsupervised learning: core paradigms, why compress high-dimensional data, workflow (training), challenges and limitations; feature learning through embeddings: one-hot vectors and classification with them, limitations of sparse representations and why sparsity breaks similarity, distributional semantics (words by context), dense (distributed) representations and embeddings.
- **Results:** Confusion-matrix identities for accuracy, precision, recall and F1 [D]; sparsity of one-hot vectors makes all distinct words orthogonal [P].
- **Build:** a rule-based expert-system toy, then the scikit-learn supervised and unsupervised workflows end to end, with each metric recomputed by hand from the confusion matrix.

**Assignment A9.0** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The Turing test was proposed in

(A) 1936  
(B) 1950  
(C) 1956  
(D) 1969

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Expert systems encode rules written by humans  
(B) The AI winter followed unmet expectations and funding cuts  
(C) One-hot vectors of distinct words are orthogonal  
(D) Accuracy is always an adequate metric under heavy class imbalance

**Q3 (2 marks, numerical answer).** F1 score with TP = 40, FP = 10, FN = 20.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that F1 is the harmonic mean of precision and recall and is at most their arithmetic mean.

**Q5 (3 marks, programming).** Write a forward-chaining rule engine for a toy diagnosis task, then a confusion-matrix utility computing accuracy, precision, recall and F1 from predictions. Verify the F1 identity above on random labels. Predict which metric a majority-class predictor scores well on.

<details><summary>Key for A9.0 (open only after your attempt)</summary>

- **Q1:** B. Turing's 1950 paper; Dartmouth was 1956.
- **Q2:** ABC. Accuracy misleads on imbalanced data.
- **Q3:** 0.7273 (tolerance ±0.001). Precision 0.8, recall 0.667, F1 0.727.
- **Q4 (marking outline):** F1 = 2PR/(P+R); AM-HM inequality.
- **Q5 (what a passing submission shows):** Accuracy is high on imbalanced data while recall of the minority class is 0.

</details>

### U9.1 What machine learning is: paradigms, data, hypothesis spaces and the statistical framework
**Sources:** MLCE W1, o; MLDL W1, o; MLK W1–3, o; MLE W1–3, o; MLESA W1, o; FML W1, o; IMLK W1, o; SMLM W8–9; MFML W12; DMIN W1, o
- **Topics:** Introduction to data science and machine learning; differences between supervised, unsupervised and reinforcement learning with examples from engineering disciplines; introduction to ML and performance measures; basic definitions, types of learning, hypothesis space and inductive bias; machine learning in its context within AI; the introduction to the machine-learning course; characterization of learning problems; forms of representation; statistical decision theory for regression and classification; overview of ML; stochastic framework for supervised learning; risk minimization; Bayes optimal predictor; stochastic optimization; empirical risk minimization (ERM); statistical learning: introduction, supervised and unsupervised learning problems, loss functions; introduction to artificial intelligence and neural networks (SMLM Week 9); algorithms for ML – classification, clustering and regression; intro to machine learning packages; broad heuristics governing basic ML algorithms in engineering applications; limits and applicability of ML algorithms; mathematical basics (linear algebra and probability recap); computational basics; basics of Python; scientific-computing packages NumPy, SciPy, Matplotlib; simple ML packages (scikit-learn, PyTorch); Bayesian classification; multilayer perceptron; autoencoders; convolutional and recurrent neural networks and attention mechanisms; decision trees and ensemble methods, boosting and bagging, random forests, support vector machines, Gaussian process regression; logistic regression, k-nearest neighbour, basic clustering algorithms, feature reduction methods; hypothesis space; evaluation strategies and cross-validation; adaptive systems; reinforcement learning and deep learning through decision trees; optimization (SGD) and energy-based models with Langevin sampling as foundations of generative models; Classical Techniques 1 and 2 and Advanced Techniques 1 and 2 (course blocks).
- **Results:** Bayes optimal classifier minimizes 0–1 risk [P]; Bayes optimal regressor is the conditional mean under squared loss [P]; ERM decomposition into estimation and approximation error [D]; no-free-lunch theorem [S].
- **Build:** a minimal ML framework in NumPy (dataset split, fit/predict API, metrics) used by all later units.
- **Gap-fills:** *[inferred: Mitchell Ch.1–2; Bach Ch.2; Murphy]* concept learning, version spaces, the formal learning problem (inputs, targets, loss, risk), data cleaning and feature scaling.

**Assignment A9.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Under 0-1 loss the Bayes optimal classifier predicts

(A) the class with the highest posterior  
(B) the most common class  
(C) a random class  
(D) the class with highest prior only

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Supervised learning needs labelled examples  
(B) ERM minimizes average loss on the training set  
(C) No classifier is best on all distributions (no free lunch)  
(D) Test error is typically below training error

**Q3 (2 marks, numerical answer).** Bayes error at a point where P(y = 1 given x) = 0.3.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that the Bayes classifier minimizes the probability of error among all classifiers.

**Q5 (3 marks, programming).** Build a minimal ML framework: train/test split, a fit/predict interface, accuracy, a majority-class baseline and a kNN classifier. Acceptance: kNN beats the baseline on a synthetic two-moons dataset. Predict the gap.

<details><summary>Key for A9.1 (open only after your attempt)</summary>

- **Q1:** A. Argmax of P(y given x).
- **Q2:** ABC. Test error is typically above training error.
- **Q3:** 0.3 (tolerance ±0.001). The error of the argmax rule is the smaller posterior.
- **Q4 (marking outline):** Conditional on x, choosing the class with the larger posterior leaves the smaller error probability; integrate over x.
- **Q5 (what a passing submission shows):** kNN reaches above 90 percent versus about 50 percent for majority.

</details>

### U9.2 Model evaluation and selection: bias–variance, validation, tuning and metrics
**Sources:** MLCE W3,6, o; MLDL W1; MLESA W1,7; MLE W4; IMLK W1; EMML W6; DMIN W7; SMLM W8
- **Topics:** Overfitting and underfitting; bias–variance tradeoff; performance measures; k-fold cross-validation and leave-one-out cross-validation; hyperparameter tuning via grid search, randomized search and Bayesian approaches; bootstrapping and cross-validation; classification evaluation measures; ROC curve; MDL (minimum description length); classification metrics; evaluation and visualization (data mining); evaluation strategies and cross-validation; confidence intervals and goodness of fit; train/validation/test discipline; implementation of regression models in Python.
- **Results:** Bias–variance decomposition of expected squared error [D]; leave-one-out cross-validation estimator formula for linear smoothers [D]; AUC equals the probability that a positive outranks a negative [P].
- **Build:** cross-validation, ROC/AUC, confusion-matrix metrics (accuracy, precision, recall, F1) and grid/random search from scratch.
- **Gap-fills:** *[inferred: ESL Ch.7]* optimism and AIC/BIC, nested cross-validation, calibration, statistical comparison of classifiers.

**Assignment A9.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** A model with low bias and high variance is typically

(A) underfit  
(B) overfit  
(C) perfect  
(D) biased

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) k-fold cross-validation estimates generalization error  
(B) Expected squared error decomposes into bias squared, variance and noise  
(C) AUC is the probability a random positive outranks a random negative  
(D) Accuracy is the best metric for imbalanced classes

**Q3 (2 marks, numerical answer).** AUC for positive scores 0.9, 0.8, 0.4 and negative scores 0.7, 0.3.

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the bias-variance decomposition of expected squared error for an estimator of a noisy target.

**Q5 (3 marks, programming).** Implement k-fold cross-validation, ROC and AUC, and grid and random search. Check your AUC equals the pairwise-ordering estimate on random scores. Predict why random search often wins in high dimension.

<details><summary>Key for A9.2 (open only after your attempt)</summary>

- **Q1:** B. It tracks noise.
- **Q2:** ABC. Use precision-recall or AUC.
- **Q3:** 0.8333 (tolerance ±0.001). 5 of 6 pairs are ordered correctly.
- **Q4 (marking outline):** Add and subtract the expected prediction; cross terms vanish.
- **Q5 (what a passing submission shows):** It explores more distinct values of the important hyperparameters per trial.

</details>

### U9.3 Linear regression and linear classification: estimation, logistic and softmax regression, surrogate losses
**Sources:** MLCE W2–4, o; MLDL W1,5; MLESA W2–3; MLE W4; FML W2–3; IMLK W2,5; SMLM W6; EMML W5; S50 D7
- **Topics:** Linear regression, model parametrization and fitting; coefficient of determination; linear regression estimation error and model error; linear modelling; multivariate regression; subset selection; shrinkage methods; principal component regression; partial least squares; linear classification and surrogate losses; logistic regression; softmax regression; bounding estimation error in binary classification; loss functions (mean-squared error, mean absolute error, mean-squared logarithmic error, cross-entropy loss, Tweedie loss, mean absolute percentage error) and the statistical basis of some loss functions; MLE and MAP interpretation; linear discriminant analysis; Bayesian regression; nonlinear regression; Basics of Python; dealing with overfitting via regularization (ridge regression and LASSO); decision trees and overfitting.
- **Results:** OLS = MLE under Gaussian noise [D]; logistic regression log-likelihood is concave, gradient and Hessian [D]; softmax cross-entropy gradient is (p−y) [D]; estimation error bound for linear least squares [P]; surrogate-loss consistency (hinge, logistic) [S].
- **Build:** linear, logistic and softmax regression with gradient descent and Newton/IRLS from scratch; compare with scikit-learn.
- **Gap-fills:** *[inferred: Bishop Ch.3–4; ESL Ch.3–4]* generalized linear models, Poisson regression, perceptron convergence (see U9.5).

**Assignment A9.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The logistic regression loss is

(A) convex  
(B) concave  
(C) nonconvex  
(D) linear

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) OLS is the maximum-likelihood estimate under Gaussian noise  
(B) The gradient of softmax cross-entropy with respect to logits is p - y  
(C) The logistic loss is nonconvex  
(D) Newton's method (IRLS) applies to logistic regression

**Q3 (2 marks, numerical answer).** Predicted probability of logistic regression for logit 1.

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the gradient and Hessian of the logistic-regression negative log-likelihood.

**Q5 (3 marks, programming).** Implement linear, logistic and softmax regression with gradient descent and Newton's method. Gradient-check each and compare accuracy and iterations. Predict the number of Newton iterations to converge.

<details><summary>Key for A9.3 (open only after your attempt)</summary>

- **Q1:** A. Negative log-likelihood of a log-linear model.
- **Q2:** ABD. It is convex.
- **Q3:** 0.7311 (tolerance ±0.001). sigma(1) = 0.731.
- **Q4 (marking outline):** Gradient X^T (p - y); Hessian X^T diag(p(1-p)) X, positive semidefinite.
- **Q5 (what a passing submission shows):** Newton converges in 5-8 iterations versus hundreds for GD.

</details>

### U9.4 Regularization and implicit regularization
**Sources:** MLCE W3; MLDL W1; MLE W4; FML W6; MLESA W2; ALAK W7
- **Topics:** Regularization (ridge regression and LASSO); min-norm regularization for linear regression and classification; equivalent forms of regularization (penalized, constrained, early stopping); implicit regularization; L1 versus L2 (geometry and sparsity); variants of gradient descent; regularization and shrinkage; sparsity.
- **Results:** Ridge shrinkage in the SVD basis [D]; lasso soft-thresholding solution for orthonormal design [D]; gradient descent from zero converges to the min-norm interpolant for under-determined least squares [P]; constrained and penalized forms are equivalent (Lagrangian) [P].
- **Build:** ridge path, lasso path and elastic net by coordinate descent from scratch.

**Assignment A9.4** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Which penalty tends to produce exactly sparse solutions?

(A) L2  
(B) L1  
(C) none  
(D) dropout only

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Ridge shrinks all coefficients  
(B) Gradient descent from zero on an underdetermined least-squares problem finds the minimum-norm solution  
(C) The L1 ball has corners  
(D) Ridge coefficients grow without bound as lambda grows

**Q3 (2 marks, numerical answer).** 1-D ridge coefficient with x = (1,1,1), y = (1,1,1), lambda = 3.

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the lasso solution for an orthonormal design as soft thresholding of the OLS coefficients.

**Q5 (3 marks, programming).** Compute ridge and lasso paths (coordinate descent) and elastic net on synthetic data with 5 true nonzero features in 30. Predict the number of nonzero lasso coefficients at very large lambda.

<details><summary>Key for A9.4 (open only after your attempt)</summary>

- **Q1:** B. Corners of the L1 ball.
- **Q2:** ABC. They shrink toward zero.
- **Q3:** 0.5 (tolerance ±0.001). w = sum xy/(sum x^2 + lambda) = 0.5.
- **Q4 (marking outline):** Decouple coordinates; solve 0.5 (z - b)^2 + lambda abs(z).
- **Q5 (what a passing submission shows):** Zero.

</details>

### U9.5 Perceptron, support vector machines and kernel methods
**Sources:** MLDL W4; MLESA W4; FML W7–8; IMLK W5; MLCE W9–10; DMIN W4; MFML W4; EMML W11–12; MLE W9; ALAJ W5,11; SMLM W11
- **Topics:** Perceptron criteria; discriminative models; support vector machines (SVM) for classification and regression; perceptron; kernel function and kernel SVM; kernel machines; linear models in infinite-dimensional spaces; kernels (linear, polynomial, Gaussian); the kernel trick; the representer theorem; universal kernels; Bayes consistency and generalization rate with universal kernel machines; hard and soft margin classifier; SVM in Python; introduction to SVM and error-minimizing LPP; Support Vector Machines and applications (MFML Week 4); SVM and kernel machine (data mining); linear perceptron and training a perceptron by stochastic gradient; SVM and kernel SVM; kernel machines; deep neural networks, SVM and K-means clustering as covered in the statistical-methods course.
- **Results:** Perceptron convergence theorem (mistake bound) [P]; SVM primal–dual derivation and support vectors [D]; representer theorem [P]; Mercer's theorem [X]; universal kernel ⇒ Bayes consistency (statement and sketch) [S].
- **Build:** perceptron, SVM via SMO and via QP (cvx), kernel ridge regression and kernel SVM from scratch; compare with `sklearn.svm`.
- **Gap-fills:** *[inferred: Bishop Ch.6–7; Bach Ch.7]* support-vector regression, multi-class SVM, reproducing-kernel Hilbert spaces.

**Assignment A9.5** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** A support vector machine chooses the separator that

(A) maximizes the margin  
(B) minimizes the number of features  
(C) maximizes training error  
(D) ignores labels

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) The kernel trick computes inner products in a feature space implicitly  
(B) Support vectors lie on or inside the margin  
(C) The perceptron converges on separable data  
(D) The SVM dual has one variable per feature

**Q3 (2 marks, numerical answer).** Perceptron mistake bound (R/gamma)^2 for R = 2 and margin gamma = 0.5.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove the perceptron convergence theorem for linearly separable data with margin gamma and radius R.

**Q5 (3 marks, programming).** Implement the perceptron, a kernel SVM by SMO and kernel ridge regression. Show an RBF kernel solving XOR. Predict the number of support vectors on XOR.

<details><summary>Key for A9.5 (open only after your attempt)</summary>

- **Q1:** A. Maximum-margin principle.
- **Q2:** ABC. The dual has one variable per sample.
- **Q3:** 16 (tolerance ±0.001). 16 mistakes.
- **Q4 (marking outline):** Weight inner product with the separator grows linearly; weight norm grows like sqrt of mistakes; combine.
- **Q5 (what a passing submission shows):** All four points are support vectors.

</details>

### U9.6 Bayes decision theory, density estimation and probabilistic classifiers
**Sources:** MLDL W2–3; MLESA W3,5,8; MLE W9; IMLK W4; DMIN W3; MLK W4; FML W12
- **Topics:** Bayes decision theory; normal density and discriminant function; Bayes decision theory for binary features; Bayesian belief network; parametric and non-parametric density estimation (ML and Bayesian estimation); Parzen window and KNN; probability and Bayes learning; naive Bayes; Bayes classifier; K-nearest neighbour; linear discriminant analysis; parameter estimation (MLE, MAP, Bayesian estimation); multi-class classification; k-NNs; kNN (Classical Techniques 2); applications.
- **Results:** Discriminant functions of Gaussian class-conditionals are quadratic (linear for shared covariance) [D]; naive Bayes factorization and Laplace smoothing [D]; kNN asymptotic error ≤ 2× Bayes error (Cover–Hart) [S]; Parzen estimator bias–variance [D].
- **Build:** Gaussian discriminant analysis, naive Bayes, Parzen and kNN from scratch.

**Assignment A9.6** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Naive Bayes assumes

(A) features are conditionally independent given the class  
(B) features are independent of the class  
(C) labels are continuous  
(D) the prior is uniform

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Gaussian class-conditionals with shared covariance give a linear boundary  
(B) The 1-NN error is at most twice the Bayes error asymptotically  
(C) A Parzen window is a kernel density estimator  
(D) Naive Bayes never needs smoothing

**Q3 (2 marks, numerical answer).** Posterior spam probability: prior 0.4, P(word given spam) 0.5, P(word given ham) 0.1.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that Gaussian class-conditionals with equal covariance give a linear discriminant.

**Q5 (3 marks, programming).** Implement Gaussian discriminant analysis, naive Bayes with Laplace smoothing, a Parzen classifier and kNN. Compare on two datasets. Predict which suffers most from the curse of dimensionality.

<details><summary>Key for A9.6 (open only after your attempt)</summary>

- **Q1:** A. Factorization of the likelihood.
- **Q2:** ABC. Zero counts need Laplace smoothing.
- **Q3:** 0.7692 (tolerance ±0.001). 0.2/0.26 = 0.769.
- **Q4 (marking outline):** The log-odds is linear because the quadratic terms cancel.
- **Q5 (what a passing submission shows):** kNN and Parzen.

</details>

### U9.7 Decision trees and ensembles: bagging, boosting, random forests
**Sources:** MLCE W8–10; MLDL W5–6; MLESA W6–8; MLE W9; IMLK W2,7; SMLM W10; DMIN W3; FML W12; MLK W4
- **Topics:** Decision trees and their working; recursive binary splitting; regression and classification via decision trees; regression trees; stopping criterion and pruning loss functions; categorical attributes; multiway splits; missing values; decision-tree instability and evaluation measures; ensembling of decision trees; ensemble methods (ensemble strategies, bagging, committee machines and stacking, boosting); random forests; adaptive boosting (AdaBoost); gradient boosting; gradient-boosted machine learning; decision-tree-based inductive learning; model averaging; regularization for boosted trees; binary trees; implementation of decision trees, SVM and GPR in Python; Classical Techniques 1 (course block).
- **Results:** Information gain and Gini impurity as concave impurity measures [D]; bagging variance reduction for correlated estimators [D]; AdaBoost training-error bound [P]; gradient boosting as functional gradient descent [D].
- **Build:** CART, random forest, AdaBoost and gradient boosting from scratch; compare with scikit-learn and XGBoost-style implementations.
- **Gap-fills:** *[inferred: ESL Ch.9–10, 15–16]* out-of-bag error, variable importance, shrinkage and subsampling.

**Assignment A9.7** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Bagging mainly reduces

(A) bias  
(B) variance  
(C) noise  
(D) dimension

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Random forests decorrelate trees by feature subsampling  
(B) AdaBoost reweights misclassified points  
(C) Gradient boosting fits successive residual gradients  
(D) A single decision tree is a low-variance model

**Q3 (2 marks, numerical answer).** Gini impurity of a node with 6 positive and 4 negative examples.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that splitting never increases weighted Gini or entropy impurity, using concavity.

**Q5 (3 marks, programming).** Implement CART, a random forest, AdaBoost and gradient boosting. Compare to a single tree on noisy data and report out-of-bag error. Predict the ranking.

<details><summary>Key for A9.7 (open only after your attempt)</summary>

- **Q1:** B. Averaging decorrelated predictors.
- **Q2:** ABC. Trees are high variance.
- **Q3:** 0.48 (tolerance ±0.001). 1 - 0.36 - 0.16 = 0.48.
- **Q4 (marking outline):** Parent impurity is concave in class proportions; Jensen gives parent >= weighted children.
- **Q5 (what a passing submission shows):** Boosting and forest beat a single tree; the single tree overfits.

</details>

### U9.8 Dimensionality reduction and feature learning
**Sources:** MLCE W7–8; MLDL W7; IMLK W3; EMML W3–4; MFML W4,10; MLESA W2; SMLM W7; DMIN W1; MLE o
- **Topics:** Unsupervised learning; why compress high-dimensional data; singular value decomposition; principal component analysis (PCA); Python implementation of PCA; linear discriminant analysis (LDA) and its Python implementation; the dimensionality problem; feature reduction; nonlinear dimensionality reduction via uniform manifold approximation and projection (UMAP), t-distributed stochastic neighbour embedding (t-SNE) and autoencoders; implementation of unsupervised learning in Python; PCA and least squares; principal component regression; multicollinearity; empirical orthogonal functions.
- **Results:** PCA as top-k eigenvectors of the covariance matrix (variance maximization) [P]; PCA equals best rank-k reconstruction (Eckart–Young) [P in U4.9]; Fisher's criterion for LDA [D]; t-SNE gradient [D]; linear autoencoder spans the PCA subspace [P].
- **Build:** PCA via covariance eigendecomposition and via SVD, LDA, kernel PCA and a t-SNE sketch from scratch; compare with scikit-learn.
- **Gap-fills:** *[inferred: MML Ch.10; ESL Ch.14]* probabilistic PCA, independent component analysis, spectral embedding.

**Assignment A9.8** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The first principal component is the direction of

(A) maximum variance  
(B) minimum variance  
(C) maximum mean  
(D) class separation

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) PCA can be computed from the SVD of centred data  
(B) Explained-variance ratios sum to 1  
(C) t-SNE preserves global distances exactly  
(D) LDA uses class labels

**Q3 (2 marks, numerical answer).** Explained-variance ratio of the first component for covariance eigenvalues 2 and 1.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that the direction maximizing projected variance is the top eigenvector of the covariance matrix.

**Q5 (3 marks, programming).** Implement PCA (covariance and SVD routes), LDA, kernel PCA and a basic t-SNE. Verify the two PCA routes agree to 1e-10. Predict their sign relationship.

<details><summary>Key for A9.8 (open only after your attempt)</summary>

- **Q1:** A. Top eigenvector of the covariance.
- **Q2:** ABD. t-SNE preserves local neighbourhoods.
- **Q3:** 0.6667 (tolerance ±0.001). 2/(2+1).
- **Q4 (marking outline):** Maximize w^T C w subject to norm(w) = 1 by a Lagrange multiplier.
- **Q5 (what a passing submission shows):** Components agree up to sign.

</details>

### U9.9 Clustering, mixture models and the EM algorithm
**Sources:** MLCE W7–8; MLDL W8–9; MLESA W10–11; MLE W10; IMLK W8; DMIN W5; ALAJ W10; SMLM W11
- **Topics:** Clustering algorithms including k-means and density-based clustering; concept of mixture model; Gaussian mixture model (GMM); expectation–maximization (EM) algorithm; K-means clustering; fuzzy K-means clustering; hierarchical agglomerative clustering (adaptive hierarchical clustering); mean-shift clustering; partitional clustering; BIRCH algorithm; CURE algorithm; density-based clustering; outlier detection; centroid-based and probabilistic model-based clustering; k-means clustering (statistical-methods course Week 11); kNN and applications (Classical Techniques 2); Classical Techniques 2 (course block).
- **Results:** k-means monotonically decreases its objective and converges to a local minimum [P]; EM never decreases the likelihood [P]; k-means as the hard-assignment limit of spherical GMM [D]; Jensen-based ELBO derivation of EM [D].
- **Build:** k-means++, GMM-EM, DBSCAN, agglomerative linkage and mean-shift from scratch.
- **Gap-fills:** *[inferred: MML Ch.11; Bishop Ch.9]* choosing k (silhouette, BIC), spectral clustering (uses U4.8 and U1.4).

**Assignment A9.9** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The k-means objective is

(A) non-increasing at each iteration  
(B) non-decreasing  
(C) constant  
(D) random

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) EM never decreases the likelihood  
(B) k-means depends on initialization  
(C) DBSCAN can find non-convex clusters  
(D) A GMM uses hard assignments

**Q3 (2 marks, numerical answer).** k-means SSE for points 1, 2, 10, 11 with two converged clusters.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that each k-means iteration does not increase the objective.

**Q5 (3 marks, programming).** Implement k-means++, GMM-EM and DBSCAN. Compare on blobs and on two moons using the adjusted Rand index. Predict which fails on moons.

<details><summary>Key for A9.9 (open only after your attempt)</summary>

- **Q1:** A. Assignment and update steps each reduce it.
- **Q2:** ABC. It uses soft assignments.
- **Q3:** 1 (tolerance ±0.001). Centres 1.5 and 10.5, each point 0.5 away.
- **Q4 (marking outline):** Assignment minimizes distance for fixed centres; the mean minimizes squared distance for fixed assignments.
- **Q5 (what a passing submission shows):** k-means and a spherical GMM fail; DBSCAN succeeds.

</details>

### U9.10 Probabilistic graphical models, hidden Markov models, inference and Gaussian processes
**Sources:** MLESA W5,8–9; MLDL W2,5; MLE W11; MLCE W10; FML W11–12
- **Topics:** Bayesian networks; undirected graphical models; hidden Markov models (HMM); variable elimination; belief propagation; structured probabilistic models; Monte Carlo methods; Gaussian process regression (GPR) and its implementation in Python; probabilistic models for supervised learning; likelihood estimation; Bayesian belief network; Advanced Techniques 1 (structured probabilistic models and Monte Carlo methods).
- **Results:** d-separation and the factorization theorem [S]; forward–backward and Viterbi algorithms [D]; belief propagation is exact on trees [P]; GP posterior mean and variance [D].
- **Build:** HMM (forward, Viterbi, Baum–Welch), variable elimination on a small Bayesian network and GP regression from scratch.
- **Gap-fills:** *[inferred: Bishop Ch.8, 11, 13; Murphy; Goodfellow Ch.16–19]* sampling methods, approximate inference, partition-function problem (links to U13.6).

**Assignment A9.10** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The Viterbi algorithm finds

(A) the most probable hidden state sequence  
(B) the likelihood only  
(C) the transition matrix  
(D) the emission matrix

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) The forward algorithm computes the sequence likelihood  
(B) Belief propagation is exact on trees  
(C) Baum-Welch is an EM algorithm  
(D) A GP posterior variance does not depend on where the inputs are

**Q3 (2 marks, numerical answer).** GP posterior mean at x = 1 given one noiseless observation y = 1 at x = 0, RBF kernel exp(-(x-x')^2/2).

**Q4 (2 marks, prove or derive; every step with its reason).** Show the forward algorithm computes the likelihood in O(T N^2) rather than O(N^T).

**Q5 (3 marks, programming).** Implement HMM forward, Viterbi and Baum-Welch, variable elimination on a 5-node Bayesian network, and GP regression. Verify forward probabilities sum to the brute-force likelihood on a short sequence. Predict the Baum-Welch likelihood trend.

<details><summary>Key for A9.10 (open only after your attempt)</summary>

- **Q1:** A. Dynamic programming over paths.
- **Q2:** ABC. Variance shrinks near observed inputs.
- **Q3:** 0.6065 (tolerance ±0.001). k(1,0)/k(0,0) * 1 = 0.6065.
- **Q4 (marking outline):** alpha_t(j) = sum_i alpha_{t-1}(i) a_ij b_j(o_t): N^2 work per step.
- **Q5 (what a passing submission shows):** Monotone non-decreasing.

</details>

### U9.11 Instance-based learning, collaborative filtering and recommendation
**Sources:** IMLK W3; DMIN W3; ALAJ W7
- **Topics:** Instance-based learning; collaborative-filtering-based recommendation; K-nearest neighbour; the Netflix problem and data completion.
- **Results:** Matrix-factorization objective and ALS updates [D]; curse of dimensionality for distance-based methods [P].
- **Build:** kNN with KD-tree, user–user and item–item collaborative filtering, ALS matrix factorization from scratch.

**Assignment A9.11** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Item-based collaborative filtering typically uses

(A) cosine similarity of rating vectors  
(B) the sigmoid  
(C) FFT  
(D) entropy of words

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Matrix factorization can be fitted by alternating least squares  
(B) kNN suffers from the curse of dimensionality  
(C) New users face a cold-start problem  
(D) Mean imputation is always optimal

**Q3 (2 marks, numerical answer).** Cosine similarity of (5,3,0) and (4,2,1).

**Q4 (2 marks, prove or derive; every step with its reason).** Show that, with the item factors fixed, the ALS update for a user vector is a ridge regression.

**Q5 (3 marks, programming).** Implement kNN, user-user collaborative filtering and ALS matrix factorization. Evaluate RMSE on synthetic rank-3 ratings with 30 percent observed. Predict the RMSE trend with rank.

<details><summary>Key for A9.11 (open only after your attempt)</summary>

- **Q1:** A. Similarity between rating columns.
- **Q2:** ABC. It is only a baseline.
- **Q3:** 0.973 (tolerance ±0.001). 26/26.72 = 0.973.
- **Q4 (marking outline):** Minimize the sum of squared errors over rated items plus lambda times norm squared.
- **Q5 (what a passing submission shows):** RMSE drops sharply at the true rank 3.

</details>

### U9.12 Data mining: preprocessing, association rules, sequence mining, outliers and case studies
**Sources:** DMIN W1–2,5–8, o
- **Topics:** Introduction to data mining; data preprocessing; association rule mining; classification basics; clustering and outlier detection; sequence mining; evaluation and visualization; case studies on industrial problems; implementations in open-source software; data mining as an interdisciplinary topic spanning databases, machine learning and algorithms.
- **Results:** Apriori anti-monotonicity (downward closure) [P]; FP-growth correctness [S]; support, confidence and lift [Def].
- **Build:** Apriori and FP-growth, PrefixSpan sketch and an end-to-end mining pipeline (clean, mine, evaluate, visualize).
- **Gap-fills:** *[inferred: Han–Kamber; Tan–Steinbach–Kumar]* feature selection, imbalanced data, data warehousing basics.

**Assignment A9.12** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Apriori relies on

(A) downward closure of frequent itemsets  
(B) FFT  
(C) convexity  
(D) Bayes rule

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Support is the fraction of transactions containing an itemset  
(B) Confidence is P(consequent given antecedent)  
(C) Lift above 1 indicates positive association  
(D) Lift always equals confidence

**Q3 (2 marks, numerical answer).** Lift with support(A) = 0.4, support(B) = 0.5, support(A and B) = 0.3.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove the downward closure property used by Apriori.

**Q5 (3 marks, programming).** Implement Apriori and FP-growth on toy baskets and check they return the same frequent itemsets and rules. Predict which candidates Apriori prunes.

<details><summary>Key for A9.12 (open only after your attempt)</summary>

- **Q1:** A. Subsets of frequent sets are frequent.
- **Q2:** ABC. Lift divides confidence by consequent support.
- **Q3:** 1.5 (tolerance ±0.001). 1.5.
- **Q4 (marking outline):** Any transaction containing the superset also contains each subset, so support(subset) >= support(superset).
- **Q5 (what a passing submission shows):** All supersets of infrequent itemsets are pruned.

</details>

### U9.13 Learning theory: PAC, VC dimension, generalization and modern overparametrization
**Sources:** IMLK W7, o; MLESA W12; FML W1,3,5,8–10,12; MLE o
- **Topics:** Computational learning theory; PAC learning model; sample complexity; VC dimension; learning theory; Bayes consistency and generalization rate; overparametrization; minimal versus optimal regularization; latent variables; modularity in modelling; deep learning models; estimation error in deep learning; optimization error and implicit bias in deep learning; tradeoffs between representational power and learnability; model averaging; hypothesis-space capacity; overparametrization regime in linear regression connecting to billion-parameter models; modern concepts in ML: overparametrization; optional videos (RL framework, TD learning, solution methods, applications).
- **Results:** PAC bound for finite hypothesis classes [P]; VC-dimension generalization bound [S]; Sauer–Shelah lemma [P]; Rademacher-complexity bound [S]; benign overfitting / double descent for min-norm interpolation [S].
- **Build:** empirical double-descent experiment with random features and min-norm least squares.
- **Gap-fills:** *[inferred: Bach Ch.4, 12, 15; Shalev-Shwartz–Ben-David]* uniform convergence, margin bounds, lower bounds, online-to-batch conversion (link to U10).

**Assignment A9.13** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The VC dimension of linear classifiers in R^d (with bias) is

(A) d  
(B) d + 1  
(C) 2d  
(D) infinite

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) A PAC bound for finite classes grows with log of the class size  
(B) The Sauer-Shelah lemma bounds the growth function  
(C) Double descent occurs for min-norm interpolation near n = p  
(D) A larger VC dimension always shrinks the generalization gap

**Q3 (2 marks, numerical answer).** PAC sample size (1/eps)(ln abs(H) + ln(1/delta)) for abs(H) = 1000, eps = 0.1, delta = 0.05.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove the finite-hypothesis-class PAC bound for a consistent learner.

**Q5 (3 marks, programming).** Run a random-features regression with min-norm least squares for p from 5 to 200 on n = 50 samples and plot test error against p. Predict the location of the peak.

<details><summary>Key for A9.13 (open only after your attempt)</summary>

- **Q1:** B. Radon's theorem.
- **Q2:** ABC. It tends to enlarge the gap.
- **Q3:** 99.03 (tolerance ±0.5). (6.908 + 2.996)/0.1 = 99.0.
- **Q4 (marking outline):** Union bound over bad hypotheses with true error above eps, each surviving m samples with probability at most (1 - eps)^m.
- **Q5 (what a passing submission shows):** Test error peaks near p = n.

</details>

### U9.14 Symbolic and knowledge-based machine learning, tools and cognitive-science influences
**Sources:** MLK W4–8, o
- **Topics:** Inductive learning based on symbolic representations and weak theories; learning enabled by prior theories; inductive logic programming; decision-tree-based inductive learning; reinforcement learning and deep learning as seen in the course; machine-learning-based artificial neural networks; tools and resources; cognitive science influences; examples, demos and exam preparation.
- **Results:** Version-space convergence [P]; ID3 entropy criterion [D]; inductive-bias characterization of learners [P].
- **Build:** a small ILP learner (FOIL-style) and ID3 from scratch.
- **Gap-fills:** *[inferred: Mitchell Ch.2, 10–12]* version spaces, explanation-based learning, first-order rule learning; link to neuro-symbolic agent design in D14.

**Assignment A9.14** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The version space is the set of hypotheses

(A) consistent with all training examples  
(B) with the lowest bias  
(C) with highest variance  
(D) that are linear

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) ID3 chooses splits by information gain  
(B) Inductive logic programming learns first-order rules  
(C) Every learner needs an inductive bias  
(D) Explanation-based learning requires no domain theory

**Q3 (2 marks, numerical answer).** Entropy in bits of a node with 9 positive and 5 negative examples.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that binary entropy is maximized at p = 1/2.

**Q5 (3 marks, programming).** Implement ID3 and a FOIL-style rule learner on a small family-relations dataset. Predict the first split chosen on the play-tennis dataset.

<details><summary>Key for A9.14 (open only after your attempt)</summary>

- **Q1:** A. Candidate-elimination definition.
- **Q2:** ABC. It uses a domain theory.
- **Q3:** 0.9403 (tolerance ±0.001). 0.940.
- **Q4 (marking outline):** H' = log((1-p)/p) is zero at 1/2 and H is concave.
- **Q5 (what a passing submission shows):** Outlook.

</details>

## D10. Sequential Decision Making: Bandits and Reinforcement Learning

Aim: online learning, regret analysis and bandits (from the Bandit Algorithms course), then MDPs and reinforcement learning, which the LLM-alignment units (RLHF, PPO, DPO) require. Benchmarks (recalled; partly confirmed from published contents): Lattimore–Szepesvári, *Bandit Algorithms* (parts on probability and concentration, stochastic and adversarial bandits, lower bounds, contextual and linear bandits, Bayesian methods and non-stationary bandits, ending with partial monitoring and Markov decision processes); Cesa-Bianchi–Lugosi, *Prediction, Learning, and Games*; Bubeck–Cesa-Bianchi, *Regret Analysis of Stochastic and Nonstochastic Multi-armed Bandit Problems*; Sutton–Barto, *Reinforcement Learning: An Introduction*.

### U10.1 From batch to online learning: adversarial full-information and bandit settings
**Sources:** BAN W1–4, o
- **Topics:** Introduction to bandit algorithms; from the batch to the online setting; exploration versus exploitation dilemma; adversarial setting with full information (Halving algorithm, weighted majority (WM) algorithm); adversarial setting with bandit information; regret lower bounds for the adversarial setting; applications in online advertising, recommendation systems, auctions, routing and e-commerce.
- **Results:** Halving mistake bound log₂|H| [P]; weighted-majority/Hedge regret O(√(T ln N)) [P]; Exp3 regret O(√(TK ln K)) [P]; adversarial lower bound Ω(√(TK)) [S].
- **Build:** Hedge and Exp3 from scratch and regret curves against adaptive and oblivious adversaries.

**Assignment A10.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The Hedge algorithm has regret of order

(A) log T  
(B) sqrt(T ln N)  
(C) T  
(D) T^2

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Exp3 handles bandit feedback  
(B) The halving algorithm makes at most log2 of the class size mistakes  
(C) Adversarial bandit regret has a lower bound of order sqrt(T K)  
(D) Exp3 requires full-information feedback

**Q3 (2 marks, numerical answer).** Halving mistake bound for a class of 1024 hypotheses.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that the halving algorithm makes at most log2 of the number of hypotheses mistakes in the realizable case.

**Q5 (3 marks, programming).** Implement Hedge and Exp3 and plot regret against sqrt(T) versus an adaptive adversary. Predict the slope on a log-log plot.

<details><summary>Key for A10.1 (open only after your attempt)</summary>

- **Q1:** B. Standard bound for N experts.
- **Q2:** ABC. Exp3 uses importance-weighted estimates.
- **Q3:** 10 (tolerance ±0.001). log2(1024) = 10.
- **Q4 (marking outline):** Each mistake removes at least half the hypotheses.
- **Q5 (what a passing submission shows):** About 0.5.

</details>

### U10.2 Stochastic bandits: regret notions, UCB, KL-UCB and lower bounds
**Sources:** BAN W5–8, o
- **Topics:** Introduction to the stochastic setting and various regret notions; a primer on concentration inequalities (see U5.7); stochastic bandit algorithms UCB and KL-UCB; explore-then-commit and ε-greedy; lower bounds for stochastic bandits; Thompson sampling as a Bayesian alternative.
- **Results:** UCB logarithmic regret bound [P]; KL-UCB asymptotic optimality [S]; Lai–Robbins instance-dependent lower bound [S]; minimax lower bound via change of measure [S].
- **Build:** UCB1, KL-UCB, Thompson sampling and ε-greedy on Bernoulli bandits with confidence-interval plots.
- **Gap-fills:** *[inferred: Lattimore–Szepesvári Ch.6–16, 34–36]* MOSS, Bayesian regret, non-stationary bandits.

**Assignment A10.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The UCB1 index of an arm is

(A) empirical mean plus a confidence bonus  
(B) empirical mean minus a bonus  
(C) the median  
(D) a random value

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) UCB has logarithmic regret in the stochastic setting  
(B) Thompson sampling samples arms from their posterior  
(C) A fixed-epsilon greedy strategy has sublinear regret  
(D) The Lai-Robbins bound lower-bounds regret

**Q3 (2 marks, numerical answer).** UCB1 index for mean 0.5, 10 pulls, round t = 100: mean + sqrt(2 ln t / n).

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the Hoeffding confidence radius sqrt(ln(1/delta)/(2n)) for the mean of n rewards in [0,1].

**Q5 (3 marks, programming).** Implement UCB1, Thompson sampling and epsilon-greedy on a 10-armed Bernoulli bandit; plot cumulative regret. Predict which has the flattest regret curve.

<details><summary>Key for A10.2 (open only after your attempt)</summary>

- **Q1:** A. Optimism in the face of uncertainty.
- **Q2:** ABD. Fixed epsilon explores forever and has linear regret.
- **Q3:** 1.46 (tolerance ±0.001). 0.5 + 0.960 = 1.460.
- **Q4 (marking outline):** Hoeffding: P(mean - mu >= r) <= exp(-2 n r^2); set equal to delta.
- **Q5 (what a passing submission shows):** UCB1 and Thompson sampling grow logarithmically; epsilon-greedy grows linearly.

</details>

### U10.3 Contextual bandits and pure exploration
**Sources:** BAN W9–12, o
- **Topics:** Introduction to contextual bandits; overview of contextual bandit algorithms; introduction to pure-exploration setups (fixed confidence versus fixed budget); algorithms for pure exploration (LUCB, KL-LUCB, lil'UCB).
- **Results:** LinUCB regret bound [S]; sample complexity of LUCB [S]; lower bound for best-arm identification [S].
- **Build:** LinUCB on a simulated recommendation task; LUCB for best-arm identification.
- **Gap-fills:** *[inferred: Lattimore–Szepesvári Ch.18–19]* linear bandits, offline policy evaluation (links to U15.3 evaluation of deployed systems).

**Assignment A10.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** LinUCB assumes rewards are

(A) linear in the context features  
(B) constant  
(C) independent of context  
(D) binary only

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Contextual bandits use side information  
(B) Pure exploration aims to identify the best arm  
(C) Fixed-confidence and fixed-budget are two settings  
(D) Pure exploration minimizes cumulative regret

**Q3 (2 marks, numerical answer).** LinUCB bonus alpha sqrt(x^T A^-1 x) with A = I, x = (3,4), alpha = 0.5.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that the ridge estimate in LinUCB is theta_hat = A^-1 b with A = I + sum x x^T and b = sum r x.

**Q5 (3 marks, programming).** Simulate LinUCB on a linear recommendation task and LUCB for best-arm identification. Predict the sample complexity ordering by arm gap.

<details><summary>Key for A10.3 (open only after your attempt)</summary>

- **Q1:** A. Ridge estimate plus an ellipsoidal bonus.
- **Q2:** ABC. It minimizes simple regret or identification error.
- **Q3:** 2.5 (tolerance ±0.001). 0.5 * 5 = 2.5.
- **Q4 (marking outline):** Minimize squared error plus norm squared; set the gradient to zero.
- **Q5 (what a passing submission shows):** Smaller gaps need quadratically more samples.

</details>

### U10.4 Markov decision processes, dynamic programming and temporal-difference learning
**Sources:** MLESA W12; MLK o; OFF W12
- **Topics:** Introduction to reinforcement learning; the RL framework; temporal-difference (TD) learning; solution methods; applications; reinforcement learning within the symbolic-ML course; Markov decision processes and value functions; dynamic programming (policy and value iteration); Monte Carlo, TD(0) and Q-learning; exploration in RL; optional videos on the RL framework, TD learning, solution methods and applications.
- **Results:** Bellman optimality equation [D]; contraction of the Bellman operator and convergence of value iteration [P]; policy-improvement theorem [P]; Q-learning convergence (statement) [X].
- **Build:** value iteration, tabular Q-learning and SARSA on a grid world; deep Q-network sketch (after U11).
- **Gap-fills:** *[inferred: Sutton–Barto Ch.3–7, 9–10]* function approximation, off-policy learning, eligibility traces.

**Assignment A10.4** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Value iteration converges because the Bellman operator is

(A) a contraction  
(B) linear  
(C) random  
(D) nonmonotone

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) The Bellman optimality equation characterizes V*  
(B) Q-learning is off-policy  
(C) SARSA is on-policy  
(D) TD(0) needs a transition model

**Q3 (2 marks, numerical answer).** Optimal value of a state with reward 1 per step forever and discount 0.9.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that the Bellman optimality operator is a gamma-contraction in the sup norm.

**Q5 (3 marks, programming).** Implement value iteration and tabular Q-learning on a 4x4 gridworld with a goal and a pit. Compare learned policies. Predict the greedy action next to the pit.

<details><summary>Key for A10.4 (open only after your attempt)</summary>

- **Q1:** A. Banach fixed-point theorem.
- **Q2:** ABC. TD learns from samples.
- **Q3:** 10 (tolerance ±0.001). 1/(1 - gamma) = 10.
- **Q4 (marking outline):** abs(max_a x_a - max_a y_a) <= max_a abs(x_a - y_a); transitions average.
- **Q5 (what a passing submission shows):** The agent avoids stepping toward the pit.

</details>

### U10.5 Policy gradient, actor–critic and proximal policy optimization
**Sources:** FDL W12; MFGAI W12
- **Topics:** Reinforcement learning for fine-tuning; proximal policy optimization (PPO); policy gradient theorem; baselines and advantage estimation; trust-region and clipped-surrogate objectives; connection to RLHF and alignment (taught again in U12.9).
- **Results:** Policy-gradient theorem [D]; baseline invariance [P]; monotonic-improvement bound motivating TRPO/PPO [S]; PPO clipped objective [D].
- **Build:** REINFORCE with baseline and a PPO implementation on a small control task.
- **Gap-fills:** *[inferred: Sutton–Barto Ch.13; Schulman et al. TRPO/PPO papers, recalled, not checked]* generalized advantage estimation, KL penalties and entropy regularization.

**Assignment A10.5** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The policy-gradient theorem expresses grad J as

(A) an expectation of grad log pi times return  
(B) the sum of rewards only  
(C) a Hessian  
(D) a constant

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) A baseline reduces gradient variance  
(B) PPO clips the probability ratio  
(C) REINFORCE is unbiased  
(D) A baseline biases the gradient

**Q3 (2 marks, numerical answer).** PPO clipped objective value for ratio 1.5, epsilon 0.2, advantage 1.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that subtracting a state-dependent baseline from the return does not change the expected policy gradient.

**Q5 (3 marks, programming).** Implement REINFORCE with a baseline and PPO on a pole-balancing environment you write (NumPy by default). Predict which gives a smoother learning curve.

<details><summary>Key for A10.5 (open only after your attempt)</summary>

- **Q1:** A. Score-function form.
- **Q2:** ABC. Baselines independent of the action leave it unbiased.
- **Q3:** 1.2 (tolerance ±0.001). min(1.5, clip(1.5) = 1.2) = 1.2.
- **Q4 (marking outline):** E[grad log pi * b(s)] = b(s) grad sum_a pi = 0.
- **Q5 (what a passing submission shows):** PPO.

</details>

### U10.6 Stochastic approximation in reinforcement learning
**Sources:** SA W11–12, o
- **Topics:** Applications of stochastic approximation to reinforcement learning: temporal-difference learning as a linear stochastic approximation and its convergence under linear function approximation; Q-learning as stochastic approximation (the Bellman operator as a contraction in the mean ODE); asynchronous updates; actor–critic as two-timescale stochastic approximation; rates of policy evaluation.
- **Results:** TD(0) with linear features converges to the projected Bellman fixed point on-policy [S]; Q-learning converges under step-size and visitation conditions [S, completing the statement deferred in U10.4]; two-timescale actor–critic convergence [S].
- **Build:** TD(0) with linear features, Q-learning with decaying steps and a two-timescale actor–critic on a small MDP.
- **Gap-fills:** *[inferred: Sutton–Barto; Borkar, recalled, not checked]* off-policy divergence examples, gradient-TD methods.

**Assignment A10.6** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The TD(0) update can be viewed as

(A) a stochastic approximation iteration  
(B) a batch least-squares fit  
(C) a tree search  
(D) a Monte Carlo rollout only

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Q-learning can be analysed as asynchronous stochastic approximation  
(B) TD(0) with linear features converges on-policy  
(C) Off-policy TD with linear features always converges  
(D) Actor-critic is naturally analysed with two timescales

**Q3 (2 marks, numerical answer).** TD(0): V(s) = 0.5, r = 1, gamma = 0.9, V(s') = 0.8, alpha = 0.1. Updated V(s).

**Q4 (2 marks, prove or derive; every step with its reason).** Show that the mean ODE of TD(0) with linear features is theta' = -A theta + b with A = Phi^T D (I - gamma P) Phi.

**Q5 (3 marks, programming).** Implement TD(0) with linear features on a 5-state chain, compare with the projected fixed point computed by linear algebra, and write Q-learning and a two-timescale actor-critic for a small MDP. Predict the TD error against the fixed point as steps decay like 1/n.

<details><summary>Key for A10.6 (open only after your attempt)</summary>

- **Q1:** A. Noisy sample of the Bellman equation drives the update.
- **Q2:** ABD. Off-policy linear TD can diverge.
- **Q3:** 0.622 (tolerance ±0.001). delta = 1.22; V(s) becomes 0.622.
- **Q4 (marking outline):** Take the expectation of the TD update over the stationary state distribution D.
- **Q5 (what a passing submission shows):** It shrinks to the sampling noise level with decaying steps.

</details>


# PART C. DEEP LEARNING AND GENERATIVE AI

## D11. Deep Learning Foundations

Aim: neural networks from perceptron to CNNs, RNNs, autoencoders and explainability, with backpropagation and every optimizer written by hand before PyTorch. Benchmarks (recalled; contents partly confirmed): Goodfellow–Bengio–Courville, *Deep Learning* (applied math and ML basics; modern practical deep networks: feedforward networks, regularization, optimization, CNNs, sequence modelling, practical methodology, applications; research topics: linear factor models, autoencoders, representation learning, structured probabilistic models, Monte Carlo methods, partition function, approximate inference, deep generative models); Nielsen, *Neural Networks and Deep Learning*; Haykin; Bengio, *Learning Deep Architectures for AI*; Foster, *Generative Deep Learning* 2nd ed. (Ch. 2 on deep learning); Bhuyan, *Computer Vision and Image Processing*.

### U11.1 Perceptron, multilayer networks, activations and loss functions
**Sources:** FDL W1, o; MFML W11; MLDL W10; MLE W5; MLESA W5; IMLK W6; MLCE W11; FML W9; MLK W6; GEN 2.7, 3.1, 3.2; SMLM W9,11
- **Topics:** Overview of machine learning and deep learning; difference between ML and DL with an example; history and evolution of deep learning with computational efficiency; biological inspiration (the neuron); examples of end-to-end deep learning; perceptron (Rosenblatt, 1958): single-layer perceptron, perceptron learning algorithm, single-layer perceptron numerical problem and limitations; introduction to the Colab environment and building a simple perceptron; multilayer perceptron (MLP); shallow versus deep neural networks; how to design a neural network with examples; activation functions and non-linearity; loss functions; neural networks: input → weights → activation → output, layers and neurons; hands-on network on a dummy dataset; a problem-first approach (business problem: why customer churn is increasing, what data is needed, how to model it); neural nets, perceptron, backpropagation algorithm; RBF neural network and applications; early models of neural networks; machine-learning-based artificial neural networks; deep learning models (modularity in modelling, overparametrization); Back Propagation Algorithm; computer vision, natural language processing, healthcare and robotics as application areas; CNNs, RNNs and autoencoders as the course arc; deep neural networks (SMLM Week 11); Advanced Techniques 2 (autoencoders, GAN).
- **Results:** Single-layer perceptron cannot represent XOR [P]; universal approximation theorem for one hidden layer [S]; depth–width separation examples [S].
- **Build:** perceptron, a 2-layer MLP and arbitrary-depth MLP from scratch in NumPy, trained on XOR, a churn-style tabular dataset and MNIST.
- **Gap-fills:** *[inferred: Goodfellow Ch.6; Nielsen Ch.1–2]* hidden-unit choices (ReLU family, GELU, SiLU), output units and cost functions as maximum likelihood.

**Assignment A11.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** A single-layer perceptron cannot represent

(A) AND  
(B) OR  
(C) XOR  
(D) NAND

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) ReLU(x) = max(0, x)  
(B) The sigmoid saturates for large inputs  
(C) A one-hidden-layer network is a universal approximator on compact sets  
(D) Deeper networks always generalize better

**Q3 (2 marks, numerical answer (parameters)).** Number of parameters in an MLP 784-128-10 with biases.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that no single linear threshold unit computes XOR.

**Q5 (3 marks, programming).** Implement a perceptron and a configurable MLP (forward only first) in NumPy. Show the perceptron failing on XOR and a 2-2-1 MLP with hand-chosen weights solving it. Predict the number of hidden units needed.

<details><summary>Key for A11.1 (open only after your attempt)</summary>

- **Q1:** C. XOR is not linearly separable.
- **Q2:** ABC. Depth is not a guarantee.
- **Q3:** 101770 parameters (tolerance ±0). 100,352 + 128 + 1,280 + 10 = 101,770.
- **Q4 (marking outline):** Four inequalities on w1, w2, b are inconsistent: w1 + b > 0, w2 + b > 0, b <= 0, w1 + w2 + b <= 0.
- **Q5 (what a passing submission shows):** Two hidden units suffice.

</details>

### U11.2 Backpropagation and training deep networks
**Sources:** FDL W2; MFML W11; GEN 2.7, 3.3; MLE W5; MLESA W5; MLDL W10; MLCE W11; FML W10
- **Topics:** Gradient descent and mathematical formulation of the backpropagation algorithm; backpropagation: how neural networks learn; learning: loss functions, optimization, overfitting; initialization; training and validation; backpropagation in deep learning (estimation error, optimization error, implicit bias); working of feed-forward neural networks; hands-on artificial neural network for classification and regression with exposure to hyperparameter tuning; momentum-based GD, Nesterov accelerated GD, stochastic GD, AdaDelta, AdaGrad, RMSProp and Adam (optimizers taught in U8.10 and used here); back propagation algorithm (MFML Week 11).
- **Results:** Backpropagation computes the exact gradient in O(forward cost) [D]; vanishing/exploding gradient bounds for deep chains [D]; Xavier/He initialization variance derivation [D].
- **Build:** reverse-mode autodiff engine and full MLP training loop from scratch; gradient check against finite differences; then re-implementation in PyTorch (`autograd`) as the oracle. **Tooling:** NumPy autodiff first; PyTorch `autograd` as the oracle.
- **Gap-fills:** *[inferred: Goodfellow Ch.8, 11]* batch normalization, learning-rate warm-up and schedules, practical methodology (debugging, diagnostics).

**Assignment A11.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Backpropagation is an application of

(A) the chain rule  
(B) Bayes' rule  
(C) the central limit theorem  
(D) the pigeonhole principle

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) He initialization uses variance 2/n_in for ReLU layers  
(B) Backpropagation costs about the same as one forward pass  
(C) Deep sigmoid networks suffer vanishing gradients  
(D) Backpropagation needs one forward pass per weight

**Q3 (2 marks, numerical answer).** Product of the maximum sigmoid derivative (0.25) over 10 layers.

**Q4 (2 marks, prove or derive; every step with its reason).** Derive backpropagation for a two-layer network with tanh hidden units and mean-squared error, giving each gradient.

**Q5 (3 marks, programming).** Write a reverse-mode autodiff engine (tape of operations) and an MLP trained by SGD on a 2-class spiral. Acceptance: gradient check below 1e-6 and training accuracy above 95 percent. Predict the loss at initialization for 2 classes.

<details><summary>Key for A11.2 (open only after your attempt)</summary>

- **Q1:** A. Reverse-mode differentiation.
- **Q2:** ABC. That is finite differences, not backpropagation.
- **Q3:** 9.537e-07 (tolerance ±1e-9). 0.25^10 = 9.54e-7.
- **Q4 (marking outline):** delta2 = yhat - y; grad W2 = delta2 h^T; delta1 = (W2^T delta2) * (1 - h^2); grad W1 = delta1 x^T.
- **Q5 (what a passing submission shows):** ln 2 = 0.693.

</details>

### U11.3 Overfitting, regularization and generalization in deep networks
**Sources:** FDL W2; GEN 2.8, 3.3; MLESA W5
- **Topics:** What overfitting and underfitting are; the bias–variance tradeoff; detecting overfitting: training versus validation loss; regularization: penalizing complexity; L1 versus L2 (geometry and sparsity); dropout and early stopping; data augmentation; regularization techniques; putting it together: a scikit-learn pipeline; summary and quick reference; hyperparameter tuning.
- **Results:** Dropout as an ensemble/approximate Bayesian average [S]; L2 regularization equals weight decay for SGD [P]; early stopping as implicit L2 for quadratic loss [D].
- **Build:** dropout, weight decay, early stopping and augmentation layers from scratch; learning-curve diagnostics.

**Assignment A11.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Weight decay with plain SGD is equivalent to

(A) L2 regularization  
(B) L1 regularization  
(C) dropout  
(D) batch normalization

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Early stopping acts as a regularizer  
(B) Data augmentation enlarges the effective training set  
(C) Dropout approximates an ensemble of subnetworks  
(D) L2 regularization produces exactly sparse weights

**Q3 (2 marks, numerical answer).** Inverted-dropout scale factor for keep probability 0.8.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that adding lambda/2 norm(w)^2 to the loss gives the SGD update w <- (1 - eta lambda) w - eta grad L.

**Q5 (3 marks, programming).** Add dropout, weight decay, early stopping and augmentation to your MLP from A11.2. Plot train and validation loss. Predict the effect of each on the generalization gap.

<details><summary>Key for A11.3 (open only after your attempt)</summary>

- **Q1:** A. The gradient of lambda/2 norm(w)^2 is lambda w.
- **Q2:** ABC. L1 produces sparsity.
- **Q3:** 1.25 (tolerance ±0.001). Divide kept activations by the keep probability.
- **Q4 (marking outline):** Differentiate the penalty and substitute.
- **Q5 (what a passing submission shows):** Each reduces the gap; early stopping halts near the validation minimum.

</details>

### U11.4 Convolutional neural networks and image representation
**Sources:** FDL W3–4; MLE W6–7; MLDL W11; MLCE W11–12; CSO W1
- **Topics:** Fundamentals of image representation, image preprocessing and data augmentation; introduction to convolutional neural networks (CNN), inspiration behind CNN, key components and CNN layers explained in detail with the math behind; hands-on simple CNN for binary and multiclass classification; CNN operations and CNN architectures; CNN training, transfer learning and applications; vanishing and exploding gradients in deep neural networks; standard CNN architectures (LeNet-5, AlexNet, VGGNet, GoogLeNet, ResNet); introduction to transfer learning; hands-on transfer learning and building an ensemble model; working of convolutional neural networks; basics of CNN computations.
- **Results:** Convolution as a linear, translation-equivariant operator [P]; output-size and parameter-count formulae [D]; ResNet identity mapping eases optimization (gradient path) [D]; backpropagation through convolution is a correlation [D].
- **Build:** conv, pooling and a small CNN (forward and backward) in NumPy via im2col; then PyTorch; compare receptive-field arithmetic with measured gradients. **Tooling:** conv, pooling and the small CNN in NumPy; PyTorch is the sensible tool for transfer learning with pretrained weights.
- **Gap-fills:** *[inferred: Goodfellow Ch.9]* pooling and invariance, 1-D/3-D convolutions, depthwise-separable convolutions, normalization layers.

**Assignment A11.4** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** A 32-wide input, 5-wide kernel, no padding and stride 1 gives an output width of

(A) 27  
(B) 28  
(C) 30  
(D) 32

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Convolution is translation-equivariant  
(B) Pooling adds some local translation invariance  
(C) Residual connections ease gradient flow  
(D) The parameter count of a convolution layer grows with image size

**Q3 (2 marks, numerical answer (parameters)).** Parameters in a 3x3 convolution with 3 input and 16 output channels, with biases.

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the gradient of the loss with respect to the input of a convolution layer as a correlation with the flipped kernel.

**Q5 (3 marks, programming).** Implement conv2d forward and backward (via im2col), max-pooling and a small CNN in NumPy. Gradient-check every layer to 1e-6. Predict the output shape for a 28x28 input through conv 3x3 (no padding) then 2x2 pooling.

<details><summary>Key for A11.4 (open only after your attempt)</summary>

- **Q1:** B. (32 - 5)/1 + 1 = 28.
- **Q2:** ABC. Weights are shared across positions.
- **Q3:** 448 parameters (tolerance ±0). 432 weights + 16 biases.
- **Q4 (marking outline):** Write the output as a sum over kernel taps and apply the chain rule per input position.
- **Q5 (what a passing submission shows):** 13 x 13 spatial size.

</details>

### U11.5 Explainable AI for deep models
**Sources:** FDL W5
- **Topics:** Introduction to XAI and the need for XAI; techniques of XAI; XAI methods with mathematical foundations and numerical examples (PCI, occlusion, SHAP, LIME, Grad-CAM, guided backpropagation, CAMs); hands-on interpreting the results of a CNN model using XAI techniques.
- **Results:** Shapley value axioms and uniqueness [P]; Grad-CAM as gradient-weighted activation map [D]; LIME as local linear surrogate [D].
- **Build:** occlusion maps, LIME and Shapley sampling from scratch; Grad-CAM in PyTorch. **Tooling:** occlusion, LIME and exact Shapley in NumPy; Grad-CAM on a pretrained CNN in PyTorch.

**Assignment A11.5** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The Shapley efficiency axiom says attributions

(A) sum to the value of the full coalition minus the empty coalition  
(B) are all equal  
(C) are all positive  
(D) are independent of the model

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) LIME fits a local linear surrogate  
(B) Grad-CAM weights feature maps by gradients of the class score  
(C) Occlusion maps measure score drops when regions are masked  
(D) SHAP values ignore feature correlations by construction

**Q3 (2 marks, numerical answer).** Shapley value of player 1 with v({1}) = 2, v({2}) = 3, v({1,2}) = 7.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that for two players the Shapley values sum to v({1,2}).

**Q5 (3 marks, programming).** Implement occlusion maps, a LIME explainer and exact Shapley values for a 4-feature model, all in NumPy. Verify that exact Shapley values sum to f(x) minus the baseline. Predict how many coalitions are evaluated.

<details><summary>Key for A11.5 (open only after your attempt)</summary>

- **Q1:** A. They fully distribute the payoff.
- **Q2:** ABC. Handling correlation is an open issue.
- **Q3:** 3 (tolerance ±0.001). Average marginal contribution: (2 + 4)/2 = 3.
- **Q4 (marking outline):** phi1 + phi2 = 0.5(v1 + v12 - v2) + 0.5(v2 + v12 - v1) = v12.
- **Q5 (what a passing submission shows):** 2^4 = 16.

</details>

### U11.6 Segmentation and object detection
**Sources:** FDL W6; MLDL W12
- **Topics:** CNN-based segmentation algorithms: UNet and attention-based UNet; CNN-based object detection models: YOLO, RCNN and Faster RCNN; hands-on object detection using YOLO; hands-on UNet and attention UNet; U-Net, applications and case studies.
- **Results:** Intersection-over-union and non-maximum suppression [Def]; anchor/region-proposal losses [D].
- **Build:** U-Net for a small segmentation set; IoU and NMS from scratch; YOLO inference with a pretrained model. **Tooling:** IoU, NMS and the small U-Net in NumPy; YOLO inference with a pretrained model.

**Assignment A11.6** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Intersection over union of two boxes is

(A) overlap area divided by union area  
(B) overlap divided by the smaller area  
(C) the sum of areas  
(D) the distance of centres

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Non-maximum suppression removes overlapping duplicate detections  
(B) U-Net uses skip connections between encoder and decoder  
(C) YOLO is a single-stage detector  
(D) IoU can exceed 1

**Q3 (2 marks, numerical answer).** IoU of boxes [0,0,2,2] and [1,1,3,3].

**Q4 (2 marks, prove or derive; every step with its reason).** Show that IoU lies in [0,1] and equals 1 only for identical sets.

**Q5 (3 marks, programming).** Implement IoU, NMS and a small U-Net-style segmentation network on synthetic shapes in NumPy. Predict the Dice score after a short training run on easy shapes.

<details><summary>Key for A11.6 (open only after your attempt)</summary>

- **Q1:** A. Standard definition.
- **Q2:** ABC. IoU lies between 0 and 1.
- **Q3:** 0.1429 (tolerance ±0.001). Intersection 1, union 4 + 4 - 1 = 7.
- **Q4 (marking outline):** Intersection is a subset of the union; equality of measures forces equal sets up to null sets.
- **Q5 (what a passing submission shows):** Above 0.9 on circles versus a background.

</details>

### U11.7 Recurrent networks: RNN, LSTM, GRU, backpropagation through time and attention in RNNs
**Sources:** FDL W7–8; MLE W8; MLCE W12; MLDL W12; MLK W6; DLNLP W4
- **Topics:** Sequence-to-sequence models; introduction to recurrent neural networks (RNN), limitations of feed-forward neural networks, need for RNN and their structure; variants of RNN; challenges in RNN (vanishing and exploding gradients); backpropagation through time; numerical problem on RNN; hands-on RNN and its variants on structured data; long short-term memory (LSTM) architecture and its necessity; bidirectional LSTM; stacked LSTMs; GRU architecture; LSTM versus GRU: speed, accuracy, complexity and when to use GRU over LSTM; why attention mechanism in RNNs, working of the attention mechanism and its benefits; hands-on LSTM models for structured and unstructured data; recurrent neural networks implementation in Python; RNN language models (RNN LMs), GRUs, LSTMs, Bi-LSTMs; LSTMs for sequence labeling; LSTMs for sequence-to-sequence.
- **Results:** Gradient of BPTT as a product of Jacobians [D]; vanishing/exploding conditions via spectral radius [D]; LSTM cell-state additive path [D].
- **Build:** vanilla RNN, LSTM and GRU with BPTT from scratch; character-level language model.
- **Gap-fills:** *[inferred: Goodfellow Ch.10]* gradient clipping, echo-state ideas, teacher forcing.

**Assignment A11.7** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** LSTMs mitigate vanishing gradients mainly through

(A) an additive cell-state path  
(B) larger learning rates  
(C) sigmoid activations only  
(D) dropout

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) BPTT unrolls the network in time  
(B) A GRU has fewer parameters than an LSTM  
(C) Gradient clipping helps with exploding gradients  
(D) RNN training is parallel across time steps

**Q3 (2 marks, numerical answer).** Factor by which a gradient shrinks through 20 steps when the recurrent Jacobian has norm 0.9.

**Q4 (2 marks, prove or derive; every step with its reason).** Write the BPTT gradient as a product of Jacobians and state when it vanishes or explodes.

**Q5 (3 marks, programming).** Implement RNN, LSTM and GRU with BPTT and a character-level language model in NumPy. Gradient-check one LSTM step. Predict the effect of gradient clipping on loss spikes.

<details><summary>Key for A11.7 (open only after your attempt)</summary>

- **Q1:** A. The forget-gated linear path carries gradient.
- **Q2:** ABC. The recurrence is sequential.
- **Q3:** 0.1216 (tolerance ±0.001). 0.9^20 = 0.1216.
- **Q4 (marking outline):** dL/dh_k contains the product of W^T diag(f'); behaviour depends on the largest singular value relative to 1.
- **Q5 (what a passing submission shows):** Clipping removes the rare loss explosions.

</details>

### U11.8 Autoencoders and representation learning
**Sources:** FDL W10; MLDL W12; MLE W12; MLCE W8; GEN 2.6
- **Topics:** Unsupervised learning: introduction to autoencoder and architecture of AE with mathematical foundation; types (simple, deep, CNN-based); training of autoencoders; hands-on building an AE and its variants; autoencoders and their relation to PCA; feature learning through embeddings: one-hot vectors and classification with them, limitations of sparse representations, why sparsity breaks similarity, distributional semantics (words by context), dense (distributed) representations and embeddings; auto encoders and relation to PCA; Advanced Techniques 2 (autoencoders, generative adversarial networks).
- **Results:** Linear autoencoder with MSE recovers the PCA subspace [P]; sparse/denoising/contractive objectives [D].
- **Build:** dense, convolutional and denoising autoencoders from scratch; latent-space visualization.

**Assignment A11.8** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** An autoencoder forces compression through

(A) a bottleneck layer  
(B) a larger hidden layer  
(C) label supervision  
(D) a softmax

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) A linear autoencoder with MSE recovers the PCA subspace  
(B) A denoising autoencoder is trained to reconstruct clean inputs from noisy ones  
(C) A VAE is the same as a plain autoencoder  
(D) A larger latent than input always improves representation

**Q3 (2 marks, numerical answer).** Compression ratio of an autoencoder from 784 inputs to a 32-dimensional code.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that the optimal linear autoencoder with squared error spans the top-k principal subspace (Eckart-Young).

**Q5 (3 marks, programming).** Implement a dense and a denoising autoencoder in NumPy and compare reconstruction error with PCA of the same dimension. Predict the relation for the linear case.

<details><summary>Key for A11.8 (open only after your attempt)</summary>

- **Q1:** A. Low-dimensional code.
- **Q2:** AB. A VAE adds a probabilistic prior; overcomplete codes can learn the identity.
- **Q3:** 24.5 (tolerance ±0.001). 24.5.
- **Q4 (marking outline):** Reconstruction error is the Frobenius distance to a rank-k matrix, minimized by truncated SVD.
- **Q5 (what a passing submission shows):** Equal up to optimization error.

</details>

## D12. Natural Language Processing, the Transformer and Large Language Models

Aim: NLP foundations, embeddings, attention and the Transformer, pretraining, decoding, prompting, alignment (RLHF, PPO, DPO), parameter-efficient fine-tuning and prompt optimization, with every mechanism built in NumPy or PyTorch. Benchmarks (confirmed against the published contents): Jurafsky–Martin, *Speech and Language Processing* 3rd ed. (words and tokens, n-gram language models, logistic regression and text classification, embeddings, neural networks, Transformers and pretraining, post-training, masked language models, interpretability, information retrieval and RAG, agents, machine translation, RNNs and LSTMs); Foster, *Generative Deep Learning* 2nd ed. (Transformers and large language models); Goodfellow Ch. 10 and 12.4.

### U12.1 NLP foundations and the classical NLP pipeline
**Sources:** GEN 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7; DLNLP W1, o; FDL W9
- **Topics:** NLP in the GenAI context: NLP as the interface layer of AI systems (chatbots, search, automation); real-world uses in support, finance and healthcare; text representation: Bag of Words → TF-IDF → Word2Vec → embeddings; goal: convert text to numbers; intuition: similar meaning, similar vectors; language modelling basics: predicting the next word, context window, probability distribution over words; evolution of language models: n-grams → RNN → Transformers, parallel processing and context awareness; the classical NLP pipeline: cleaning → tokenization → stopwords → lemmatization → features → model; hands-on: tokenize with NLTK, apply TF-IDF, build a simple classifier; limitations of classical NLP (no deep context, manual features, poor generalization); bridge to GenAI: classical NLP → deep learning → LLMs → agents; the agent loop (observe, reason, act); modern NLP architecture: input → embeddings → retrieval → LLM → output; hands-on task: build and compare a mini NLP pipeline; what is natural language processing; a brief primer on word-level and sentence-level tasks; n-gram language model; introduce NLP tasks; classical NLP versus deep-learning NLP; text preprocessing (tokenization, stopwords, lemmatization); question answering, text summarization and dialogs as NLP applications; in the last decade deep-learning methods became the default for NLP problems.
- **Results:** Chain rule for language-model probability [P]; maximum-likelihood n-gram estimates and smoothing (add-k, Kneser–Ney idea) [D]; perplexity as exponentiated cross-entropy [D]; TF-IDF weighting rationale [D].
- **Build:** tokenizer, n-gram LM with smoothing, TF-IDF and a Naive-Bayes/logistic text classifier from scratch; compare with NLTK and scikit-learn.
- **Gap-fills:** *[inferred: SLP3 Ch.2–4, 18]* byte-pair encoding and subword tokenization (also needed by U12.4), regular expressions and text normalization, sequence labelling for parts of speech and named entities.

**Assignment A12.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The chain rule gives the probability of a sentence as

(A) a product of conditional next-word probabilities  
(B) a sum of unigram counts  
(C) the maximum word probability  
(D) the vocabulary size

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) TF-IDF down-weights terms common across documents  
(B) Perplexity is the exponential of the cross-entropy  
(C) n-gram models need smoothing for unseen events  
(D) Bag-of-words preserves word order

**Q3 (2 marks, numerical answer).** Perplexity of a model assigning probability 1/8 to every token.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that perplexity equals exp of the average negative log-likelihood per token and that a uniform model has perplexity equal to the vocabulary size.

**Q5 (3 marks, programming).** Implement a tokenizer, a bigram language model with add-k smoothing and a TF-IDF plus naive-Bayes classifier on a toy corpus. Predict the perplexity of a unigram model on the training text versus bigram.

<details><summary>Key for A12.1 (open only after your attempt)</summary>

- **Q1:** A. P(w1..wn) = product of P(wi given earlier words).
- **Q2:** ABC. Order is discarded.
- **Q3:** 8 (tolerance ±0.001). exp(-log(1/8)) = 8.
- **Q4 (marking outline):** Definition; uniform gives exp(log V) = V.
- **Q5 (what a passing submission shows):** Bigram perplexity is lower on training text.

</details>

### U12.2 Word representations and multilingual embeddings
**Sources:** DLNLP W2–3; FDL W9; GEN 1.2; MFGAI o
- **Topics:** Introduction to deep learning for NLP: shallow and deep neural networks and representation learning; word representations: one-hot encoding, word embeddings Word2Vec, GloVe, fastText; multilingual representations with emphasis on Indian languages; hands-on RNN for an NLP task.
- **Results:** Skip-gram with negative sampling implicitly factorizes a shifted PMI matrix [S]; GloVe objective [D].
- **Build:** skip-gram with negative sampling and GloVe from scratch; analogy and similarity tests.
- **Gap-fills:** *[inferred: SLP3 Ch.5]* contextual versus static embeddings, bias in embeddings (link to U15.4).

**Assignment A12.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Skip-gram predicts

(A) context words from a centre word  
(B) the centre word from the sum of contexts  
(C) the next sentence  
(D) the part of speech

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Negative sampling replaces the full softmax  
(B) GloVe uses global co-occurrence counts  
(C) Static embeddings give one vector per word type  
(D) fastText ignores subword information

**Q3 (2 marks, numerical answer).** Cosine similarity of (1,0) and (1,1).

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the gradient of the skip-gram negative-sampling loss with respect to the centre vector.

**Q5 (3 marks, programming).** Train skip-gram with negative sampling in NumPy on a small corpus and list nearest neighbours of three words. Predict whether frequent or rare words have noisier nearest neighbours.

<details><summary>Key for A12.2 (open only after your attempt)</summary>

- **Q1:** A. Standard definition.
- **Q2:** ABC. fastText adds character n-grams.
- **Q3:** 0.7071 (tolerance ±0.001). 1/sqrt 2 = 0.707.
- **Q4 (marking outline):** Loss = -log sigma(u_o.v_c) - sum log sigma(-u_k.v_c); differentiate.
- **Q5 (what a passing submission shows):** Rare words, because they receive few updates.

</details>

### U12.3 Attention and the Transformer architecture
**Sources:** GEN 3.4, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7; DLNLP W5; FDL W11; FML W9
- **Topics:** Toward GenAI: attention intuition, self-attention, transformers, the bridge to GenAI; before transformers: limitations of pre-attention models, seq2seq with an RNN, seq2seq with an attention layer, the attention idea and why attention alone was not enough, the self-attention idea; the encoder: what self-attention is, query/key/value step by step, the attention mechanism vectorized, a tiny worked example, the feed-forward layer; making deep networks train: residual connections, layer normalization, scaled dot-product attention; positional encoding (injecting order into attention); multi-head attention: why multiple heads, a 2-head worked example (computing Q, K, V; scores, softmax and the attention matrix; head outputs; combining heads; comparing the heads), a full model in PyTorch; the decoder: decoder design and overview, masked self-attention and masked multi-head self-attention, cross-attention (Q, K, V; encoder–decoder attention; matrix form; a worked example; what it cannot do), self-attention versus cross-attention, the complete decoder, autoregressive generation (the decoder loop, with a step-by-step example); evolution: "Attention Is All You Need", from attention to pretrained models, the modern transformer zoo; sequence-to-sequence with attention; transformer architectures: self-attention, encoder–decoder attention.
- **Results:** Scaled dot-product attention with 1/√d_k scaling stabilizes softmax variance [D]; permutation equivariance of self-attention without positions [P]; parameter and FLOP count of a Transformer block [D]; causal mask makes training parallel but generation sequential [P].
- **Build:** single-head, multi-head and masked attention, sinusoidal positional encoding, an encoder block, a decoder block and a tiny decoder-only Transformer trained on characters, all from scratch in NumPy, then PyTorch as the oracle. **Tooling:** attention and a tiny Transformer in NumPy; once gradient checks pass, PyTorch is fine for anything beyond toy scale.
- **Gap-fills:** *[inferred: SLP3 Ch.7; Foster Ch.9]* rotary and relative positional encodings, grouped-query attention, FlashAttention (links to U16.3), encoder-only versus decoder-only versus encoder–decoder families.

**Assignment A12.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Attention scores are divided by sqrt(d_k) to

(A) keep dot-product variance from growing with dimension  
(B) reduce parameters  
(C) enforce causality  
(D) normalize labels

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) A causal mask blocks attention to future positions  
(B) Self-attention without positional information is permutation-equivariant  
(C) Multi-head outputs are concatenated and projected  
(D) Attention cost is linear in sequence length

**Q3 (2 marks, numerical answer).** Attention weight on the first token for scores (2, 0) after softmax.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that for independent unit-variance components the dot product of two d-dimensional vectors has variance d, motivating the 1/sqrt(d) scaling.

**Q5 (3 marks, programming).** Implement scaled dot-product attention, multi-head attention, a causal mask and sinusoidal positional encoding in NumPy. Acceptance: the output at position t does not change when later tokens change. Predict the shape of the attention matrix for T = 6.

<details><summary>Key for A12.3 (open only after your attempt)</summary>

- **Q1:** A. The variance of q.k grows with d_k.
- **Q2:** ABC. Cost is quadratic.
- **Q3:** 0.8808 (tolerance ±0.001). e^2/(e^2 + 1) = 0.881.
- **Q4 (marking outline):** Sum of d independent products each with variance 1.
- **Q5 (what a passing submission shows):** 6 x 6 lower-triangular after masking.

</details>

### U12.4 Pretraining, self-supervised learning and the LLM landscape
**Sources:** GEN 5.1; DLNLP W6–7, o; FDL W11–12; MFGAI W10, o
- **Topics:** The LLM landscape: BERT (contextual language-model training; the GLUE benchmark); GPT-1 and GPT-2 (decoder-only generation; LAMBADA); T5 and BART (text-to-text and denoising seq2seq); GPT-3 (few-shot and in-context learning); InstructGPT and RLHF; the open-weights wave (LLaMA, Mistral, Falcon); MMLU; the multimodal and reasoning era; a map of innovations (architecture, training, data); self-supervised learning (SSL) and pretraining, designing SSL objectives; pretrained Bi-LSTMs: ELMo; pretrained Transformers: BERT, GPT, T5, BART; self-supervised learning objectives and loss functions; masked language modeling; large language models: tokenizers, pre-training and post-training, multimodal alignment; applications: question answering, dialog modeling, text summarization; multilingual extension with application to Indian languages; auto-regressive models and large language models introduction; massive multitask language understanding (MMLU); in-context learning, parameter-efficient fine-tuning and RLHF as the course arc; deep generative models, autoregressive models, diffusion models and large language models.
- **Results:** Masked-LM and causal-LM objectives as conditional likelihoods [D]; cross-entropy loss per token and perplexity [D]; next-sentence and denoising objectives compared [P].
- **Build:** a masked-LM and a causal-LM pretraining loop at toy scale; fine-tune a small pretrained BERT/GPT for classification and QA. **Tooling:** LM pipelines and losses in NumPy; fine-tuning a pretrained checkpoint with PyTorch.
- **Gap-fills:** *[inferred: SLP3 Ch.7, 9]* data curation and deduplication, training-data contamination (links to U15.1), pretraining compute budgets.

**Assignment A12.4** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** BERT is pretrained with

(A) masked language modelling  
(B) causal language modelling only  
(C) reinforcement learning  
(D) image captions

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) GPT models are decoder-only  
(B) T5 casts tasks as text-to-text  
(C) BERT is autoregressive  
(D) MMLU measures multitask knowledge

**Q3 (2 marks, numerical answer).** Perplexity for a per-token cross-entropy of 2.0 nats.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that the causal language-modelling loss is the sum over positions of token cross-entropies, from the chain rule.

**Q5 (3 marks, programming).** Build the data pipeline and loss for a causal LM and a masked LM on a toy corpus in NumPy, and verify that the loss of a uniform random model equals ln V. Predict ln V for V = 64.

<details><summary>Key for A12.4 (open only after your attempt)</summary>

- **Q1:** A. Masked-token prediction.
- **Q2:** ABD. BERT is bidirectional and not autoregressive.
- **Q3:** 7.389 (tolerance ±0.001). e^2 = 7.389.
- **Q4 (marking outline):** Take the negative log of the product of conditionals.
- **Q5 (what a passing submission shows):** ln 64 = 4.159.

</details>

### U12.5 Scaling laws, LLM architectures and long context
**Sources:** DLNLP W9,11; CSO W5
- **Topics:** Scaling laws; various large language models and their unique architectural differences; handling long context; basics of large language models (systems view).
- **Results:** Power-law loss versus compute, parameters and data (Kaplan/Chinchilla form) [X, empirical law: fitted, not proved]; compute-optimal allocation [D from the fitted law].
- **Build:** fit a scaling law to training runs of a family of tiny Transformers.
- **Gap-fills:** *[inferred: SLP3 Ch.7; Kaplan et al. and Hoffmann et al., recalled, not checked]* mixture-of-experts, sliding-window and sparse attention, positional-interpolation tricks for long context.

**Assignment A12.5** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Neural scaling laws show loss falling as

(A) a power law in compute, data and parameters  
(B) a linear function  
(C) an exponential in time  
(D) a constant

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Compute-optimal training balances parameters and data  
(B) Loss follows a power law in compute  
(C) More parameters always lower loss regardless of data  
(D) Mixture-of-experts activates a sparse subset of parameters

**Q3 (2 marks, numerical answer).** Loss ratio when parameters double, for L proportional to N^-0.076.

**Q4 (2 marks, prove or derive; every step with its reason).** For L = A N^-a + A D^-a with compute C = 6 N D, show the minimum has N = D.

**Q5 (3 marks, programming).** Fit a power law to the final losses of five toy models of increasing size by log-log least squares, in NumPy. Predict whether the fitted exponent is close to the true generating exponent.

<details><summary>Key for A12.5 (open only after your attempt)</summary>

- **Q1:** A. Empirical power laws.
- **Q2:** ABD. Without enough data, big models overfit.
- **Q3:** 0.9487 (tolerance ±0.001). 0.9487.
- **Q4 (marking outline):** Substitute D = C/(6N); by symmetry and convexity the minimum is at N = D.
- **Q5 (what a passing submission shows):** Within a few percent for low noise.

</details>

### U12.6 Decoding strategies and sampling
**Sources:** GEN 5.3, 6.2; MFGAI W11
- **Topics:** Choosing the next word at each step; greedy decoding and its problem; beam search (how it works, with an example); greedy and beam search are deterministic; the quality-versus-diversity tradeoff; random sampling: temperature, top-k, top-p (nucleus); repetition and frequency penalties; max tokens and stop sequences; parameter cheat sheet; tutorial: putting it all together; common LLM inference terms: tokens, temperature, top-k, top-p; LLMs: models, sampling, inference and quantization methods (sampling part).
- **Results:** Temperature as softmax scaling and its entropy limits [D]; top-p truncation as adaptive support [P]; beam search is not exact search [P].
- **Build:** greedy, beam, temperature, top-k and top-p decoders from scratch over a small LM.

**Assignment A12.6** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** As temperature goes to zero, sampling approaches

(A) greedy decoding  
(B) uniform sampling  
(C) beam search  
(D) top-p

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Top-p chooses the smallest set with cumulative probability at least p  
(B) Beam search is guaranteed to find the most probable sequence  
(C) Higher temperature gives more diverse outputs  
(D) Greedy decoding is deterministic

**Q3 (2 marks, numerical answer).** Softmax probability of the first token for logits (2,1,0) at temperature 1.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that softmax(z/T) concentrates on the argmax as T goes to 0 and approaches uniform as T goes to infinity.

**Q5 (3 marks, programming).** Implement greedy, beam search, temperature, top-k and top-p decoding over your bigram model. Predict which produces the most repetition.

<details><summary>Key for A12.6 (open only after your attempt)</summary>

- **Q1:** A. The softmax concentrates on the argmax.
- **Q2:** ACD. Beam search is a heuristic.
- **Q3:** 0.6652 (tolerance ±0.001). 0.665.
- **Q4 (marking outline):** Divide numerator and denominator by the largest term; take limits.
- **Q5 (what a passing submission shows):** Greedy decoding.

</details>

### U12.7 Prompting: fundamentals, APIs and advanced techniques
**Sources:** GEN 5.2, 5.4, 6.1, 6.3, 6.4; DLNLP W9; FDL W11
- **Topics:** What prompts are; a first basic prompt, then a more advanced one; elements of a prompt; prompting through APIs: introduction to the OpenAI API and frontier models; basic chat completion; roles in prompting; tool calling with an example; coding and reasoning models; image generation models; examples: a chatbot application, image generation; introduction: prompting and the autoregressive language model, what a prompt is, what prompt engineering is; types of prompting: overview, zero-shot and few-shot prompting, chain-of-thought (CoT) prompting and its variants (zero-shot CoT, few-shot CoT, automatic CoT, self-consistency), ReAct prompting, meta prompting, directional stimulus prompting (DSP), prompt chaining, tree of thoughts (ToT); limitations of LLM prompting; mitigating prompt-injection attacks; in-context learning; chain-of-thought prompting; limits and defenses.
- **Results:** Self-consistency as marginalization over reasoning paths [D]; why chain-of-thought helps (extra serial computation) [S].
- **Build:** a chat client with roles, tool-calling and a ReAct loop; prompt-chaining pipeline; ToT search on a small puzzle. Live API calls follow a recorded-response replay first and run only under a spend cap (Master Rules 11.2). **Tooling:** client, tool loop and ReAct against a mock model first; live API calls are replay-first and spend-capped.

**Assignment A12.7** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Few-shot prompting differs from zero-shot by

(A) including worked examples in the prompt  
(B) updating model weights  
(C) using a smaller model  
(D) removing the instruction

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Chain-of-thought prompting elicits intermediate reasoning  
(B) Self-consistency takes a majority vote over sampled reasoning paths  
(C) ReAct interleaves reasoning with tool actions  
(D) Prompt chaining uses a single prompt only

**Q3 (2 marks, numerical answer).** Probability that a majority of 5 independent samples, each correct with probability 0.6, is correct.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that a majority vote of 3 independent voters each correct with probability p exceeds p when p > 1/2.

**Q5 (3 marks, programming).** Build a chat client with roles and a tool-calling loop against a deterministic mock model you write (no network), plus a ReAct loop with a calculator tool. Predict the number of model calls for a two-step arithmetic question.

<details><summary>Key for A12.7 (open only after your attempt)</summary>

- **Q1:** A. In-context examples.
- **Q2:** ABC. It uses several linked prompts.
- **Q3:** 0.6826 (tolerance ±0.001). 0.6826.
- **Q4 (marking outline):** P(majority) = 3p^2 - 2p^3; compare with p.
- **Q5 (what a passing submission shows):** Three calls: two tool requests and a final answer.

</details>

### U12.8 Instruction tuning, RLHF and alignment: PPO and DPO
**Sources:** DLNLP W8, o; MFGAI W12; FDL W12; GEN 5.1
- **Topics:** Instruction fine-tuning; FLAN-T5; reinforcement learning through human feedback (RLHF); LLMs: reinforcement-learning-based alignment methods (PPO, DPO); reinforcement learning for fine-tuning; proximal policy optimization; InstructGPT and RLHF: aligning models with human preferences; post-training.
- **Results:** Bradley–Terry reward-model likelihood [D]; KL-regularized RLHF objective and its closed-form optimal policy [D]; DPO loss derived from that closed form [D]; PPO clipped objective (see U10.5) [D].
- **Build:** reward model on preference pairs; toy PPO-for-text and DPO fine-tuning of a tiny LM, from scratch.
- **Gap-fills:** *[inferred: SLP3 Ch.8; Ouyang et al., Rafailov et al., recalled, not checked]* constitutional and AI-feedback methods, reward hacking.

**Assignment A12.8** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Direct preference optimization differs from PPO-based RLHF in that it

(A) needs no separate reward model or rollouts  
(B) needs more rewards  
(C) uses no preferences  
(D) requires a critic network

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Reward models are commonly trained with the Bradley-Terry model  
(B) RLHF uses a KL penalty to a reference policy  
(C) PPO-based RLHF needs a reward signal  
(D) DPO needs online rollouts

**Q3 (2 marks, numerical answer).** Bradley-Terry probability that item a (reward 1) beats item b (reward 0).

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the optimal policy of the KL-regularized objective: pi*(y) proportional to pi_ref(y) exp(r(y)/beta).

**Q5 (3 marks, programming).** Train a reward model by logistic regression on preference pairs and write the DPO loss with a gradient check on a tiny tabular policy. Predict the sign of the DPO gradient on the preferred response.

<details><summary>Key for A12.8 (open only after your attempt)</summary>

- **Q1:** A. It optimizes a closed-form objective on preference pairs.
- **Q2:** ABC. DPO is offline.
- **Q3:** 0.7311 (tolerance ±0.001). sigma(1) = 0.731.
- **Q4 (marking outline):** Lagrangian over the simplex; stationarity gives the exponential tilt.
- **Q5 (what a passing submission shows):** It increases the preferred response's relative log-probability.

</details>

### U12.9 Parameter-efficient fine-tuning: LoRA and QLoRA
**Sources:** DLNLP W10; FDL W11
- **Topics:** Parameter-efficient fine-tuning (PEFT): LoRA and QLoRA; low-rank adaptation.
- **Results:** Low-rank update ΔW = BA parameter count and rank bound [D]; QLoRA 4-bit NormalFloat plus paged optimizers (stated) [X→U16.4].
- **Build:** LoRA layer from scratch merged into a frozen Transformer; compare full fine-tuning and LoRA on a small task.
- **Gap-fills:** *[inferred: Hu et al., Dettmers et al., recalled, not checked]* adapters, prefix tuning, link to SVD low-rank theory in U4.9.

**Assignment A12.9** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** LoRA represents a weight update as

(A) a product of two low-rank matrices  
(B) a sparse mask  
(C) a quantized copy  
(D) a hash

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) The rank of B A is at most r  
(B) The base weights are frozen during LoRA training  
(C) QLoRA keeps the frozen base in 4-bit precision  
(D) LoRA must increase inference latency

**Q3 (2 marks, numerical answer).** Ratio of full-update to LoRA parameters for a 1024 x 1024 layer with rank 8.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that rank(B A) is at most r and count the parameters of a LoRA update of a d x d weight.

**Q5 (3 marks, programming).** Implement a LoRA linear layer in NumPy with forward, backward and merge. Fine-tune a frozen regression network and compare with full fine-tuning. Predict the parameter ratio.

<details><summary>Key for A12.9 (open only after your attempt)</summary>

- **Q1:** A. Delta W = B A.
- **Q2:** ABC. The update can be merged into the base weights.
- **Q3:** 64 (tolerance ±0.001). 1,048,576 / 16,384 = 64.
- **Q4 (marking outline):** rank(BA) <= min(rank B, rank A) <= r; parameters 2 d r.
- **Q5 (what a passing submission shows):** About 64x fewer trainable parameters at rank 8 and width 1024.

</details>

### U12.10 Prompt optimization, compression and prompt security
**Sources:** GEN 7.1, 7.2, 7.4, 7.5
- **Topics:** Prompt optimization: motivation; the need for versioning, testing and iteration (prompts as versioned artifacts); optimization objectives; types: manual and automatic; automatic prompt optimization (APO): instruction search, gradient optimization, evolutionary optimization, DSPy; verbalized sampling: the mode collapse problem and verbalized sampling; prompt compression: basic and advanced techniques, the LLMLingua family (LLMLingua, LLMLingua-2, with examples); prompt security: prompt injection, indirect prompt injection, prompt leaking.
- **Results:** Prompt search as discrete black-box optimization (objective, search space, evaluation noise) [Def]; mode collapse from preference tuning [S].
- **Build:** a prompt-version registry and A/B test harness; evolutionary prompt search over a tiny task; token-pruning prompt compressor.

**Assignment A12.10** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Indirect prompt injection arrives through

(A) retrieved or external content processed by the model  
(B) the system administrator only  
(C) the learning rate  
(D) the tokenizer

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Prompts should be versioned and tested like code  
(B) Automatic prompt optimization searches over instructions  
(C) LLMLingua compresses prompts using a small model's token importance  
(D) Prompt leaking is harmless

**Q3 (2 marks, numerical answer).** Compression ratio when a 1000-token prompt is compressed to 250 tokens.

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the sample size n >= ln(2/delta)/(2 eps^2) needed so an A/B accuracy estimate is within eps with probability 1 - delta (Hoeffding).

**Q5 (3 marks, programming).** Write a prompt registry with versions and an A/B harness scored by a deterministic mock grader, an evolutionary prompt search over a toy task, and a token-pruning compressor. Predict n for eps = 0.05 and delta = 0.05.

<details><summary>Key for A12.10 (open only after your attempt)</summary>

- **Q1:** A. Instructions hidden in data.
- **Q2:** ABC. Leaked prompts can expose secrets.
- **Q3:** 4 (tolerance ±0.001). 4x.
- **Q4 (marking outline):** Two-sided Hoeffding: 2 exp(-2 n eps^2) <= delta.
- **Q5 (what a passing submission shows):** About 738 samples.

</details>

## D13. Deep Generative Models

Aim: the probabilistic foundations of generative modelling and every major model family (GANs, VAEs, autoregressive models, energy-based and score-based models, diffusion models), each derived and implemented from scratch. Benchmarks (confirmed from published contents where stated): Foster, *Generative Deep Learning* 2nd ed. (generative modeling, deep learning, VAEs, GANs, autoregressive models, normalizing flows, energy-based models, diffusion models, Transformers, advanced GANs, music generation, world models, multimodal models); Goodfellow Ch. 13–20; Murphy, *Probabilistic Machine Learning: Advanced Topics* (recalled, not checked); Kingma–Welling, Goodfellow et al., Ho et al., Song et al. (recalled, not checked).

### U13.1 Probabilistic deep generative modelling: foundations and taxonomy
**Sources:** MFGAI W1, o; FML W11, o; MLE W11
- **Topics:** Introduction to probabilistic deep generative modelling; probabilistic foundations and learning algorithms of deep generative models; likelihood estimation; energy-based models (EBMs); MLE; structured probabilistic models; Monte Carlo methods; taxonomy of generative models (explicit/implicit density, tractable/approximate); hands-on PyTorch implementation.
- **Results:** MLE equals minimizing KL(p_data‖p_θ) [D]; the partition function makes EBM likelihood intractable [P]; importance sampling and its variance [D].
- **Build:** a tiny density estimator by MLE (Gaussian mixture) and importance-sampling estimator from scratch.
- **Gap-fills:** *[inferred: Foster Ch.1; Goodfellow Ch.16–17]* generative versus discriminative modelling, representation learning, core probability tools.

**Assignment A13.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Maximum-likelihood training minimizes

(A) KL(p_data relative to p_model)  
(B) KL(p_model relative to p_data)  
(C) squared error only  
(D) total variation

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) The partition function makes energy-based likelihood intractable  
(B) Importance sampling gives unbiased estimates  
(C) A generative model represents the data distribution  
(D) Explicit-density models cannot be sampled

**Q3 (2 marks, numerical answer).** KL(Bernoulli(0.5) relative to Bernoulli(0.25)) in nats.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that maximizing expected log-likelihood is equivalent to minimizing KL(p_data relative to p_theta).

**Q5 (3 marks, programming).** Fit a Gaussian mixture by EM on 2-D data and estimate a rare-event probability by importance sampling, both in NumPy. Predict the variance reduction versus naive Monte Carlo.

<details><summary>Key for A13.1 (open only after your attempt)</summary>

- **Q1:** A. Equivalent up to a constant.
- **Q2:** ABC. Many can.
- **Q3:** 0.1438 (tolerance ±0.001). 0.1438.
- **Q4 (marking outline):** KL = E log p_data - E log p_theta; the first term is constant.
- **Q5 (what a passing submission shows):** Large reduction when the proposal covers the rare region.

</details>

### U13.2 Generative modelling via variational divergence minimization
**Sources:** MFGAI W2
- **Topics:** Generative modelling via variational divergence minimization; f-divergences (KL, reverse KL, Jensen–Shannon, total variation); variational (dual) representation of f-divergences; f-GAN.
- **Results:** Variational lower bound on an f-divergence via the Fenchel conjugate [D]; JS divergence recovers the original GAN objective [D].
- **Build:** numerical estimation of f-divergences between Gaussians; f-GAN objective on a 1-D toy distribution.

**Assignment A13.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The Jensen-Shannon divergence is

(A) symmetric and bounded by ln 2  
(B) asymmetric  
(C) unbounded  
(D) negative

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) KL divergence is asymmetric  
(B) f-divergences have a variational (dual) representation  
(C) JS divergence is at most ln 2  
(D) Total variation is unbounded

**Q3 (2 marks, numerical answer).** Total variation between Bernoulli(0.2) and Bernoulli(0.7).

**Q4 (2 marks, prove or derive; every step with its reason).** Show that JS(P, Q) is at most ln 2.

**Q5 (3 marks, programming).** Estimate KL, JS and TV between two Gaussians numerically and compare with the closed form for KL. Predict how the three behave as the means separate.

<details><summary>Key for A13.2 (open only after your attempt)</summary>

- **Q1:** A. JS of two distributions is at most ln 2 nats.
- **Q2:** ABC. TV is at most 1.
- **Q3:** 0.5 (tolerance ±0.001). TV = half the L1 distance = 0.5.
- **Q4 (marking outline):** JS is the average of two KLs to the mixture, each at most ln 2 by log-sum bounds on mixture ratios.
- **Q5 (what a passing submission shows):** KL grows quadratically; JS saturates at ln 2; TV saturates at 1.

</details>

### U13.3 Generative adversarial networks: formulation, training, WGAN and applications
**Sources:** MFGAI W3–4, o; MLDL W12; MLE W12; FDL W12
- **Topics:** Generative adversarial networks Part 1 (introduction and formulation); minimax game and optimal discriminator; GAN training difficulties (mode collapse, vanishing gradients); Part 2: WGANs (Wasserstein distance, Kantorovich–Rubinstein duality, weight clipping and gradient penalty) and applications; generative adversarial network (GAN) as a recent trend in deep learning; VAEs and GANs as deep generative models; generative adversarial networks.
- **Results:** Optimal discriminator D*(x)=p_data/(p_data+p_g) [D]; the generator objective equals 2·JS(p_data‖p_g) − log 4 at D* [D]; Kantorovich–Rubinstein duality [S]; Wasserstein distance remains informative for disjoint supports [P].
- **Build:** vanilla GAN, WGAN-GP and a conditional GAN from scratch on 2-D and MNIST data; mode-collapse experiments.
- **Gap-fills:** *[inferred: Foster Ch.4, 10]* DCGAN, StyleGAN-style progressive growing, evaluation with Inception score and FID.

**Assignment A13.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** For a fixed generator the optimal GAN discriminator is

(A) p_data/(p_data + p_g)  
(B) 0.5 everywhere  
(C) p_g/p_data  
(D) 1

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Mode collapse is a known GAN failure  
(B) WGAN uses the Wasserstein distance  
(C) Saturating generator losses can cause vanishing gradients  
(D) GANs are trained by exact likelihood

**Q3 (2 marks, numerical answer).** Optimal discriminator value where p_data = 0.6 and p_g = 0.2.

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the optimal discriminator by maximizing the pointwise integrand p log D + q log(1 - D).

**Q5 (3 marks, programming).** Implement a GAN and a WGAN with gradient penalty in NumPy with hand-derived gradients on a 1-D Gaussian target. Acceptance: generated mean and variance within 10 percent. Predict the failure mode with an overly strong discriminator.

<details><summary>Key for A13.3 (open only after your attempt)</summary>

- **Q1:** A. Derived in the original GAN paper.
- **Q2:** ABC. They are implicit models.
- **Q3:** 0.75 (tolerance ±0.001). 0.75.
- **Q4 (marking outline):** Differentiate in D and set to zero: D = p/(p + q).
- **Q5 (what a passing submission shows):** Vanishing generator gradients with the saturating loss.

</details>

### U13.4 Variational autoencoders, improvements and VQ-VAE
**Sources:** MFGAI W5–6; FDL W12; MLE W12
- **Topics:** Generative modelling via variational auto-encoding; evidence lower bound (ELBO); reparameterization trick; amortized inference; VAE improvisations (β-VAE, importance-weighted bounds, hierarchical and conditional VAEs); VQ-VAE (vector-quantized latents, straight-through estimator, codebook learning); VAEs and GANs compared; improvisations and VQVAE.
- **Results:** ELBO = reconstruction − KL(q‖p) and the gap equals KL(q‖posterior) [D]; reparameterization gives low-variance pathwise gradients [D]; closed-form KL between Gaussians [D].
- **Build:** VAE and VQ-VAE from scratch, with latent interpolation and posterior-collapse diagnostics.

**Assignment A13.4** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The ELBO equals reconstruction term minus

(A) KL(q(z given x) relative to p(z))  
(B) the entropy of x  
(C) the variance of z  
(D) zero

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) The reparameterization trick gives low-variance gradients  
(B) Posterior collapse is a failure mode  
(C) VQ-VAE uses a straight-through estimator  
(D) VAEs maximize the exact likelihood

**Q3 (2 marks, numerical answer).** KL(N(2,1) relative to N(0,1)) in nats.

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the ELBO from the log marginal likelihood using Jensen's inequality.

**Q5 (3 marks, programming).** Implement a VAE with a 2-D latent on toy data in NumPy with hand gradients. Gradient-check the ELBO. Predict the KL term at initialization.

<details><summary>Key for A13.4 (open only after your attempt)</summary>

- **Q1:** A. Standard decomposition.
- **Q2:** ABC. They maximize a bound.
- **Q3:** 2 (tolerance ±0.001). mu^2/2 = 2.
- **Q4 (marking outline):** log p(x) = log E_q[p(x,z)/q(z)] >= E_q[log p(x,z) - log q(z)].
- **Q5 (what a passing submission shows):** Near zero.

</details>

### U13.5 Autoregressive models
**Sources:** MFGAI W10, o
- **Topics:** Auto-regressive models (chain-rule factorization, masked/causal networks, PixelCNN-style and Transformer-based decoders) and the introduction to large language models; likelihood training and sampling cost.
- **Results:** Exact likelihood by chain rule [P]; exposure bias and teacher forcing [S].
- **Build:** a character/pixel-level autoregressive model from scratch (shares code with U12.3).

**Assignment A13.5** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** An autoregressive model factorizes a joint distribution by

(A) the chain rule  
(B) independence  
(C) marginalization  
(D) Bayes' rule on labels

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Teacher forcing feeds ground-truth history during training  
(B) Exposure bias arises from the train-test mismatch  
(C) Likelihood is tractable and exact  
(D) Sampling is parallel across tokens

**Q3 (2 marks, numerical answer).** Log-likelihood of a 3-token sequence where each token has probability 0.5.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that the chain-rule factorization of a joint distribution is exact for any ordering.

**Q5 (3 marks, programming).** Build a character-level trigram autoregressive model, sample from it and compare negative log-likelihood with the bigram model. Predict which has lower held-out NLL on a small corpus.

<details><summary>Key for A13.5 (open only after your attempt)</summary>

- **Q1:** A. Product of conditionals.
- **Q2:** ABC. Sampling is sequential.
- **Q3:** -2.079 (tolerance ±0.001). ln(0.125) = -2.079.
- **Q4 (marking outline):** Repeated application of P(A, B) = P(A) P(B given A).
- **Q5 (what a passing submission shows):** Trigram on large text; bigram can win on tiny text because of sparsity.

</details>

### U13.6 Energy-based and score-based models; Langevin sampling
**Sources:** FML W11; MFGAI W9; MLE W11
- **Topics:** Energy-based models, maximum-likelihood training with MCMC and contrastive divergence; Langevin sampling; score-based models; score matching (explicit, denoising, sliced); conditional diffusion models and score-based models; Monte Carlo methods.
- **Results:** Gradient of the log-likelihood of an EBM is a difference of expectations [D]; Langevin dynamics targets p(x) [S]; denoising score matching equals score of the noised distribution [D].
- **Build:** Langevin sampler on a 2-D mixture; denoising score matching on toy data.
- **Gap-fills:** *[inferred: Goodfellow Ch.18; Foster Ch.7]* contrastive divergence, noise-contrastive estimation.

**Assignment A13.6** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The score of a density is

(A) the gradient of its log-density  
(B) the density itself  
(C) its Fourier transform  
(D) its entropy

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Langevin dynamics uses the score to sample  
(B) Denoising score matching learns the score of a noised distribution  
(C) The EBM log-likelihood gradient is a difference of expectations  
(D) Score matching needs the partition function

**Q3 (2 marks, numerical answer).** Score of the standard normal at x = 2.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that the score of N(mu, sigma^2) is -(x - mu)/sigma^2.

**Q5 (3 marks, programming).** Run Langevin sampling on a 2-D two-component mixture using the analytic score, then train a small network by denoising score matching. Predict the effect of a too-large step.

<details><summary>Key for A13.6 (open only after your attempt)</summary>

- **Q1:** A. grad log p(x).
- **Q2:** ABC. It avoids the partition function.
- **Q3:** -2 (tolerance ±0.001). -(x - mu)/sigma^2 = -2.
- **Q4 (marking outline):** Differentiate the log-density.
- **Q5 (what a passing submission shows):** Samples drift past modes and become unstable.

</details>

### U13.7 Denoising diffusion probabilistic models, conditional diffusion and Stable Diffusion
**Sources:** MFGAI W7–9, o; FDL W12
- **Topics:** Denoising diffusion probabilistic models (DDPMs): formulation; forward and reverse diffusion; variational lower bound; denoising score matching; diffusion models: multiple forms and implementation (ε-prediction, x₀-prediction, v-prediction, DDIM, SDE and probability-flow ODE views); conditional diffusion models (classifier guidance, classifier-free guidance); score-based models; Stable Diffusion: latent-space denoising; deep generative models overview.
- **Results:** Closed-form forward marginal q(x_t|x₀) [D]; reverse-process posterior mean [D]; ELBO simplifies to a denoising regression loss [D]; DDIM as a deterministic reverse process [D]; SDE/probability-flow correspondence [S].
- **Build:** DDPM with a small U-Net (reuse U11.6) on 2-D then MNIST; classifier-free guidance; latent diffusion using the autoencoder of U11.8. **Tooling:** 1-D/2-D DDPM in NumPy with hand gradients; a PyTorch U-Net is reasonable for the image version, where hand gradients get long.
- **Gap-fills:** *[inferred: Foster Ch.8; Ho et al.; Song et al., recalled, not checked]* noise schedules, fast samplers, evaluation by FID, text-to-image conditioning with cross-attention (reuses U12.3).

**Assignment A13.7** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The forward diffusion marginal q(x_t given x_0) is

(A) Gaussian with mean sqrt(alpha_bar) x_0  
(B) uniform  
(C) Laplace  
(D) deterministic

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Many DDPMs train a network to predict the added noise  
(B) DDIM provides a deterministic sampler  
(C) Classifier-free guidance combines conditional and unconditional predictions  
(D) The reverse process has no learned parameters

**Q3 (2 marks, numerical answer).** alpha_bar_3 for constant beta = 0.1.

**Q4 (2 marks, prove or derive; every step with its reason).** Derive q(x_t given x_0) = N(sqrt(alpha_bar_t) x_0, (1 - alpha_bar_t) I) by induction.

**Q5 (3 marks, programming).** Implement a DDPM on 1-D data with an MLP noise predictor trained by hand-derived gradients in NumPy, and sample. Acceptance: sample mean and variance within 15 percent. Predict the effect of fewer sampling steps.

<details><summary>Key for A13.7 (open only after your attempt)</summary>

- **Q1:** A. Closed form from a product of Gaussians.
- **Q2:** ABC. The reverse mean is learned.
- **Q3:** 0.729 (tolerance ±0.0005). (1 - beta)^3 = 0.729.
- **Q4 (marking outline):** Compose Gaussian steps; means multiply and variances add appropriately.
- **Q5 (what a passing submission shows):** Quality degrades, a deterministic DDIM-style sampler degrades less.

</details>

### U13.8 Normalizing flows (gap-fill from the references)
**Sources:** none (gap-fill unit added from the references)
- **Topics:** Change of variables for densities and the Jacobian determinant (links to U3.3 and U4.5); invertible networks with tractable determinants; coupling layers (RealNVP-style) and autoregressive flows; training by exact maximum likelihood; continuous normalizing flows and the probability-flow ODE (link to U13.7); comparison of flows, GANs, VAEs, autoregressive and diffusion models on likelihood, sampling speed and sample quality.
- **Results:** Change-of-variables formula for densities [D]; determinant of a triangular Jacobian is the product of its diagonal [P]; log-likelihood of a flow [D].
- **Build:** RealNVP on a 2-D dataset from scratch, with density plots.
- **Gap-fills:** *[inferred: Foster, chapter on normalizing flow models (the publisher's description confirms the book covers them; chapter number recalled, not checked); Goodfellow Ch.20]* this family appears in the references but in none of the outlines; added so the model taxonomy of U13.1 is complete.

**Assignment A13.8** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** A normalizing flow computes densities using

(A) the change-of-variables formula  
(B) a partition function  
(C) MCMC  
(D) adversarial training

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Triangular Jacobians have determinants equal to the product of diagonal entries  
(B) Coupling layers are invertible by design  
(C) Flows give exact likelihoods  
(D) Flows require MCMC to sample

**Q3 (2 marks, numerical answer).** log p_x(1) for x = 2z + 1 with z standard normal.

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the 1-D change-of-variables formula p_x(x) = p_z(g^-1(x)) abs(d g^-1/dx).

**Q5 (3 marks, programming).** Implement an affine coupling layer with forward, inverse and log-determinant in NumPy. Acceptance: inverse(forward(x)) equals x to 1e-10 and the log-determinant matches finite differences. Predict the log-determinant for scale s(x1) = 0 everywhere.

<details><summary>Key for A13.8 (open only after your attempt)</summary>

- **Q1:** A. With the Jacobian determinant.
- **Q2:** ABC. Sampling is one pass.
- **Q3:** -1.612 (tolerance ±0.001). z = 0, log p_z(0) = -0.919, minus log 2: -1.612.
- **Q4 (marking outline):** P(X <= x) = P(Z <= g^-1(x)) for monotone increasing g; differentiate.
- **Q5 (what a passing submission shows):** Zero.

</details>


# PART D. LLM APPLICATIONS, EVALUATION AND SAFETY

## D14. Retrieval-Augmented Generation and Agentic Systems

Aim: RAG from first principles to production, then agentic RAG, multi-agent orchestration, memory and provenance, implemented with and without frameworks. Benchmarks: Jurafsky–Martin, *SLP3* (confirmed: information retrieval and RAG; agents); Manning–Raghavan–Schütze, *Introduction to Information Retrieval* (recalled, not checked); Khattab–Zaharia (ColBERT), Reimers–Gurevych (Sentence-BERT), Lewis et al. (RAG), Yao et al. (ReAct) (recalled, not checked).

### U14.1 Why RAG, RAG architecture and classical retrievers
**Sources:** GEN 8.1, 8.2, 8.3; DLNLP W11
- **Topics:** Why RAG: limitations of LLMs (hallucinations, verifiability, knowledge cutoff); motivation for RAG; introduction to RAG: overview, architecture and workflow, with an example; sparse retrieval and dense retrieval; augmentation and generation; the retrieval phase in detail (the retrieval pipeline, chunking and query formulation); retrievers: information-retrieval methods; TF-IDF; BM25 (a non-binary model); retrieval-augmented generation in the course on long context.
- **Results:** TF-IDF and BM25 scoring formulas and saturation of term frequency [D]; inverted-index query processing [D].
- **Build:** inverted index, TF-IDF and BM25 retriever and a minimal RAG loop from scratch.
- **Gap-fills:** *[inferred: SLP3 Ch.11; Manning et al.]* retrieval metrics (precision@k, recall@k, MRR, nDCG), query likelihood models.

**Assignment A14.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Retrieval-augmented generation reduces hallucination mainly by

(A) grounding answers in retrieved documents  
(B) increasing temperature  
(C) shrinking the model  
(D) removing the prompt

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) BM25 saturates the contribution of repeated terms  
(B) IDF is commonly log(N / document frequency)  
(C) An inverted index maps terms to the documents containing them  
(D) Dense retrieval needs no embeddings

**Q3 (2 marks, numerical answer).** IDF = ln(N/df) for a term occurring in 10 of 1000 documents.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that the BM25 term-frequency component tf (k1 + 1)/(tf + k1 (1 - b + b dl/avgdl)) is bounded above by k1 + 1 for fixed document length.

**Q5 (3 marks, programming).** Build an inverted index, TF-IDF and BM25 retrievers and a minimal RAG loop with a mock generator that quotes the top passage. Acceptance: recall@3 above 0.9 on a 20-question toy corpus. Predict which retriever wins on keyword-heavy queries.

<details><summary>Key for A14.1 (open only after your attempt)</summary>

- **Q1:** A. The answer is conditioned on evidence.
- **Q2:** ABC. Dense retrieval compares embeddings.
- **Q3:** 4.605 (tolerance ±0.001). ln 100 = 4.605.
- **Q4 (marking outline):** Divide numerator and denominator by tf and let tf go to infinity.
- **Q5 (what a passing submission shows):** BM25 on exact keyword queries.

</details>

### U14.2 RAG failure modes, types of RAG and assessment
**Sources:** GEN 8.4, 8.5, 8.6
- **Topics:** RAG failure modes: retrieval failures, context failures, generation failures; types of RAG: standard RAG, standard RAG with memory, agentic RAG, Chain-of-RAG (CoRAG) mechanics and more examples; assessment: the RAG assessment framework; RAGAS.
- **Results:** Decomposition of end-to-end RAG error into retrieval recall and generation faithfulness [D].
- **Build:** failure-injection harness (drop gold chunk, add distractor, conflicting context) and RAGAS-style metrics (faithfulness, answer relevance, context precision/recall).

**Assignment A14.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** A retrieval failure is

(A) the gold passage is not retrieved  
(B) the answer is too long  
(C) the prompt is misspelled  
(D) the model is quantized

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Generation failures include unfaithful answers  
(B) Retrieval failures include missing the gold passage  
(C) Context failures include contradictory or overloaded context  
(D) RAGAS metrics are computed without any model

**Q3 (2 marks, numerical answer).** Context recall when 3 of 4 gold facts are supported by the retrieved context.

**Q4 (2 marks, prove or derive; every step with its reason).** Let r be retrieval recall, a1 the answer accuracy when the gold passage is retrieved and a0 otherwise. Show P(correct) = r a1 + (1 - r) a0 and that it increases in r when a1 > a0.

**Q5 (3 marks, programming).** Write a failure-injection harness (drop the gold chunk, add a distractor, add a contradicting chunk) and token-overlap proxies for faithfulness and context recall. Predict which injection hurts most.

<details><summary>Key for A14.2 (open only after your attempt)</summary>

- **Q1:** A. The needed evidence never reaches the generator.
- **Q2:** ABC. RAGAS uses LLM or embedding judgements.
- **Q3:** 0.75 (tolerance ±0.001). 0.75.
- **Q4 (marking outline):** Law of total probability; derivative equals a1 - a0.
- **Q5 (what a passing submission shows):** Dropping the gold chunk.

</details>

### U14.3 Sparse retrieval limits and dense representations
**Sources:** GEN 9.1, 9.2
- **Topics:** RAG workflow recap; sparse retrieval and why sparsity breaks similarity; dense representations; vector embeddings; the RAG-with-embeddings pipeline; sentence embeddings from BERT and how they compare.
- **Results:** Cosine similarity versus dot product versus Euclidean distance and when they coincide [P].
- **Build:** mean-pooled BERT sentence embeddings versus TF-IDF on a retrieval benchmark.

**Assignment A14.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Cosine similarity ranges over

(A) [0, 1] only  
(B) [-1, 1]  
(C) [0, infinity)  
(D) (-infinity, infinity)

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) For unit vectors cosine similarity equals the dot product  
(B) Sparse bag-of-words vectors of documents with no shared words are orthogonal  
(C) Dense embeddings can place synonyms close together  
(D) Dense embeddings of synonyms must be orthogonal

**Q3 (2 marks, numerical answer).** Second component of the mean-pooled vector of (1,2) and (3,4).

**Q4 (2 marks, prove or derive; every step with its reason).** Show that for unit vectors a and b, norm(a - b)^2 = 2 - 2 cos(a,b), so cosine and Euclidean rankings agree.

**Q5 (3 marks, programming).** With a small trained embedding table (from A12.2), build mean-pooled sentence embeddings and compare retrieval with TF-IDF on a paraphrase-heavy toy set. Predict which wins.

<details><summary>Key for A14.3 (open only after your attempt)</summary>

- **Q1:** B. Cosine of the angle between vectors.
- **Q2:** ABC. Synonyms are close, not orthogonal.
- **Q3:** 3 (tolerance ±0.001). (2 + 4)/2 = 3.
- **Q4 (marking outline):** Expand the squared norm.
- **Q5 (what a passing submission shows):** Embeddings win on paraphrases; TF-IDF on exact terms.

</details>

### U14.4 Learning retrieval-oriented embeddings and choosing an embedding model
**Sources:** GEN 9.3, 9.4
- **Topics:** Getting negative examples and hard mining; dense retrieval with a bi-encoder; the costlier but more accurate alternative (cross-encoder); Sentence-BERT architecture; choosing an embedding model: common models (all-MiniLM-L6-v2 for prototyping, OpenAI text-embedding-3-small); Matryoshka embeddings and how they order dimensions; design decisions, including under real conditions; the most common silent production RAG bug.
- **Results:** InfoNCE/contrastive loss with in-batch negatives [D]; Matryoshka loss as a multi-prefix objective [D].
- **Build:** a bi-encoder trained with in-batch and hard negatives; embedding-model comparison with a cost and quality table.

**Assignment A14.4** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** In-batch negatives in contrastive training are

(A) other examples' positives used as negatives  
(B) random noise  
(C) test labels  
(D) held-out queries

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Hard negatives often improve retrieval quality  
(B) A bi-encoder allows document embeddings to be precomputed  
(C) A cross-encoder is more accurate but slower  
(D) Matryoshka embeddings are useful only at full dimension

**Q3 (2 marks, numerical answer).** InfoNCE loss for a batch of 4 when all similarity scores are equal.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that the InfoNCE loss with uniform scores over N candidates equals ln N.

**Q5 (3 marks, programming).** Train a NumPy bi-encoder (two linear towers) with in-batch negatives on toy query-document pairs and then with mined hard negatives. Report recall@1. Predict the effect of hard negatives.

<details><summary>Key for A14.4 (open only after your attempt)</summary>

- **Q1:** A. They are free negatives.
- **Q2:** ABC. They are designed to truncate gracefully.
- **Q3:** 1.386 (tolerance ±0.001). ln N = 1.386.
- **Q4 (marking outline):** The softmax probability of the positive is 1/N; take the negative log.
- **Q5 (what a passing submission shows):** Recall@1 improves, with some risk from false negatives.

</details>

### U14.5 Document processing and chunking
**Sources:** GEN 9.5, 9.6
- **Topics:** Document processing basics, including OCR; design decisions for documents; chunking: why chunk, right-sizing for retrieval; strategies: fixed-size, sliding window, semantic; matching strategy to document type (uniform prose and baselines; strongly structured documents: Markdown, legal clauses, API docs, code); tuning chunking and an overlap myth; general RAG prose.
- **Build:** four chunkers and a recall@k comparison on structured and unstructured corpora.

**Assignment A14.5** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Chunk overlap mainly helps to

(A) avoid losing information at chunk boundaries  
(B) reduce index size  
(C) speed up training  
(D) remove duplicates

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Fixed-size chunking is a simple baseline  
(B) Sliding windows overlap neighbouring chunks  
(C) Semantic chunking splits where embedding similarity drops  
(D) Chunk size has no effect on retrieval quality

**Q3 (2 marks, numerical answer (chunks)).** Number of chunks for 1000 tokens with chunk size 200 and overlap 50.

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the number of sliding windows for length L, size w and stride s as ceil((L - w)/s) + 1.

**Q5 (3 marks, programming).** Implement fixed-size, sliding-window, sentence and semantic chunkers. Compare recall@3 on a structured (Markdown) and an unstructured corpus. Predict the winner on structured documents.

<details><summary>Key for A14.5 (open only after your attempt)</summary>

- **Q1:** A. Context spans boundaries.
- **Q2:** ABC. It has a large effect.
- **Q3:** 7 chunks (tolerance ±0). Stride 150; windows start at 0, 150, ..., 900 (the last is shorter).
- **Q4 (marking outline):** Windows start at multiples of s until the end is covered.
- **Q5 (what a passing submission shows):** Structure-aware chunking by headings.

</details>

### U14.6 Vector databases and indexes: KNN, IVF, PQ, HNSW, FAISS and ChromaDB
**Sources:** GEN 9.7, 10.1, 10.2
- **Topics:** Vector databases: introduction and why an efficient vector database is required; KNN, the naive approach; IVF (inverted file index) and how much work it saves; PQ (product quantization): indexing, the 95% memory claim, and search; IVF and PQ recap; IVF + PQ combined and why the approximation works; HNSW: zooming in through layers, the efSearch candidate list, why search is about log N; FAISS; ChromaDB (a database wrapped around vector search); design decisions for vector databases: prototype scale versus raw speed and large scale; choosing a FAISS index (corpus size is the main driver); vector index methods.
- **Results:** Memory and distance-computation cost of IVF, PQ and IVF-PQ [D]; HNSW expected search complexity (small-world argument) [S]; recall–latency trade-off curves [Def].
- **Build:** brute-force KNN, IVF with k-means centroids, PQ codebooks and a small HNSW from scratch; compare with FAISS and ChromaDB. **Tooling:** brute force, IVF, PQ and HNSW in NumPy; FAISS and ChromaDB for the scale comparison.

**Assignment A14.6** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** HNSW search cost scales roughly as

(A) O(N)  
(B) O(log N)  
(C) O(N^2)  
(D) O(1) always

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) IVF searches only the nprobe nearest cluster lists  
(B) Product quantization compresses vectors  
(C) FAISS is a vector-search library  
(D) Brute-force KNN is sublinear in N

**Q3 (2 marks, numerical answer).** Compression factor of PQ: 128-dim float32 vector (512 bytes) stored as 16 one-byte codes.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that the IVF cost nlist + nprobe N/nlist distance computations is minimized at nlist = sqrt(nprobe N).

**Q5 (3 marks, programming).** Implement brute-force KNN, IVF (k-means lists), PQ and a small HNSW in NumPy. Plot recall versus distance computations. Predict the nlist for N = 10^6 and nprobe = 1.

<details><summary>Key for A14.6 (open only after your attempt)</summary>

- **Q1:** B. Navigable small-world layers.
- **Q2:** ABC. Brute force is linear.
- **Q3:** 32 (tolerance ±0.001). 32x.
- **Q4 (marking outline):** Set the derivative in nlist to zero.
- **Q5 (what a passing submission shows):** About 1000.

</details>

### U14.7 The retrieval pipeline: bi-encoder, cross-encoder, ColBERT and two-stage retrieval
**Sources:** GEN 10.3
- **Topics:** Semantic search and a minimal end-to-end pipeline; bi-encoder versus cross-encoder: the cost of accuracy; ColBERT and late interaction; the two-stage pattern as the industry standard; three failures that silently wreck a RAG system.
- **Results:** Latency/cost model of two-stage retrieve-then-rerank [D]; MaxSim late-interaction scoring [Def].
- **Build:** hybrid (BM25 + dense) first stage with reciprocal-rank fusion and a cross-encoder reranker.

**Assignment A14.7** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The two-stage retrieval pattern is

(A) cheap retrieval of candidates followed by expensive reranking  
(B) expensive then cheap  
(C) only reranking all documents  
(D) only BM25

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) A cross-encoder scores query and document jointly  
(B) ColBERT uses late interaction over token embeddings  
(C) Reciprocal rank fusion merges ranked lists  
(D) Cross-encoding a million documents per query is cheap

**Q3 (2 marks, numerical answer).** Reciprocal rank fusion (k = 60) score for a document ranked 1 in one list and 3 in another.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that two-stage retrieval beats cross-encoding all N documents when c1 N + c2 K < c2 N, with first-stage cost c1 per document and rerank cost c2 per candidate on K candidates.

**Q5 (3 marks, programming).** Build a hybrid BM25 plus dense first stage with reciprocal rank fusion and a toy cross-encoder reranker. Report recall@10 and latency. Predict whether hybrid beats either alone.

<details><summary>Key for A14.7 (open only after your attempt)</summary>

- **Q1:** A. Recall first, precision second.
- **Q2:** ABC. It is prohibitively expensive.
- **Q3:** 0.03227 (tolerance ±0.0001). 0.0323.
- **Q4 (marking outline):** Compare total costs and rearrange.
- **Q5 (what a passing submission shows):** Typically yes on mixed query types.

</details>

### U14.8 Production RAG: request shaping, query transformation, routing, security, cost and observability
**Sources:** GEN 10.4, 10.5, 10.6, 10.7
- **Topics:** From RAG to agentic: the enterprise DevOps and support agent; what is different in production; request shaping, with a project example; query transformations: rewriting, follow-up questions, multi-query retrieval, step-back prompting; query routing strategies (rule-based, embedding-based, classifier-based, LLM-based, hybrid) and applications (data-source routing, model and workflow routing, prompt and index routing); security, cost and observability: retrieval gateways, access control and least privilege, cost management, semantic caching and choosing the threshold, observability.
- **Results:** Semantic-cache hit-rate versus threshold and error trade-off [D].
- **Build:** query rewriter, multi-query retriever, router and semantic cache with metrics and tracing.

**Assignment A14.8** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Raising a semantic cache's similarity threshold

(A) reduces false hits but lowers the hit rate  
(B) raises both  
(C) has no effect  
(D) guarantees correctness

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Query rewriting can resolve follow-up questions  
(B) Multi-query retrieval merges results of several rewrites  
(C) Step-back prompting asks a more general question first  
(D) Routers must always call an LLM

**Q3 (2 marks, numerical answer).** Expected cost per request with a 30 percent cache hit rate, LLM cost 0.02 and cache lookup cost 0.001 paid on every request.

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the break-even hit rate h* = c_cache / c_llm at which a cache lookup costing c_cache on every request pays for itself.

**Q5 (3 marks, programming).** Implement a rule-based query rewriter, multi-query retrieval, a router and a semantic cache with a threshold. Plot hit rate and wrong-answer rate against the threshold. Predict the shape.

<details><summary>Key for A14.8 (open only after your attempt)</summary>

- **Q1:** A. Precision-recall trade-off.
- **Q2:** ABC. Rule or classifier routers exist.
- **Q3:** 0.015 (tolerance ±0.0001). 0.014 + 0.001 = 0.015.
- **Q4 (marking outline):** Savings h c_llm equal the lookup cost.
- **Q5 (what a passing submission shows):** Hit rate falls and wrong-hit rate falls as the threshold rises.

</details>

### U14.9 Limits of single-shot RAG and the move to agents
**Sources:** GEN 10.8, 11.1
- **Topics:** Limits of single-shot RAG: the multi-hop query case study; why if/else logic is not enough; from passive search to active problem solving; from pipelines to agents: the limits of linear RAG; simple versus complex tasks; agentic RAG: from pipeline to control loop.
- **Build:** a multi-hop QA benchmark and a single-shot baseline measuring where it fails.

**Assignment A14.9** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** A multi-hop question requires

(A) combining facts from several documents  
(B) a longer prompt only  
(C) a bigger embedding  
(D) a lower temperature

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Single-shot retrieval often fails on multi-hop questions  
(B) An agentic loop can retrieve iteratively  
(C) Simple lookup tasks rarely need an agent  
(D) Fixed if/else routing scales to all question types

**Q3 (2 marks, numerical answer).** Probability that both hops are retrieved correctly if each succeeds independently with probability 0.8.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that the success probability of a k-hop pipeline with independent hop success p is p^k and decays geometrically.

**Q5 (3 marks, programming).** Build a 30-question toy multi-hop QA set over a small knowledge base and a single-shot baseline. Report accuracy by hop count. Predict the accuracy drop from 1 to 3 hops.

<details><summary>Key for A14.9 (open only after your attempt)</summary>

- **Q1:** A. Intermediate answers feed later retrieval.
- **Q2:** ABC. Branch logic cannot anticipate every question.
- **Q3:** 0.64 (tolerance ±0.001). 0.64.
- **Q4 (marking outline):** Product rule for independent events.
- **Q5 (what a passing submission shows):** Roughly multiplicative decay.

</details>

### U14.10 Agent basics, tool calling and orchestration
**Sources:** GEN 11.2, 11.3
- **Topics:** Anatomy of an agent and its core loop; an example in the project context; tool calling, the engine of agency, and designing a tool; the multi-agent concept: a DevOps multi-agent team; orchestration: planners and executors, why separate planning from execution; a case study of the planner in action; specialist agents in the execution phase; re-planning.
- **Build:** tool schema, a tool-calling loop and a planner–executor pair from scratch (no framework).

**Assignment A14.10** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** A tool schema tells the agent

(A) the tool's name, description and argument types  
(B) the learning rate  
(C) the model weights  
(D) the tokenizer

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Planner and executor can be separated  
(B) Re-planning handles failed steps  
(C) Clear tool descriptions improve tool selection  
(D) Agents have no loop

**Q3 (2 marks, numerical answer (calls)).** Model calls for one planner call, three steps each with one reasoning call and one tool-selection call, and one final answer.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that an agent loop with step budget B makes at most B iterations and therefore terminates.

**Q5 (3 marks, programming).** Write tool-schema validation, a tool-calling loop and a planner-executor pair with a deterministic mock model, standard library and NumPy by default. Acceptance: invalid arguments are rejected with a message; a two-step task completes. Predict the number of calls.

<details><summary>Key for A14.10 (open only after your attempt)</summary>

- **Q1:** A. It is the interface contract.
- **Q2:** ABC. Agents loop until done or a budget runs out.
- **Q3:** 8 calls (tolerance ±0). 1 + 6 + 1 = 8.
- **Q4 (marking outline):** The loop counter increases each iteration and the loop exits at B.
- **Q5 (what a passing submission shows):** Eight calls for the example in Q3.

</details>

### U14.11 Planning with ReAct
**Sources:** GEN 11.4
- **Topics:** The limitation of pure chain-of-thought reasoning; the formal definition of the ReAct loop; scaling ReAct: the context and tool-exhaustion problem; hierarchical ReAct: triage as a meta-planner; caveat in production: the planning trap.
- **Build:** ReAct and hierarchical-ReAct agents with a step-budget and failure analysis.

**Assignment A14.11** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The ReAct loop alternates

(A) thought, action, observation  
(B) train, test, deploy  
(C) encode, decode, embed  
(D) rank, fuse, cache

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Hierarchical ReAct delegates sub-tasks to sub-agents  
(B) Context grows with each step  
(C) Too many tools can exhaust the context and confuse selection  
(D) ReAct eliminates all reasoning errors

**Q3 (2 marks, numerical answer (tokens)).** Context length after 10 steps if it starts at 500 tokens and each step adds 300.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that if each step re-reads the whole context, total tokens processed over T steps grows quadratically in T.

**Q5 (3 marks, programming).** Implement ReAct and hierarchical ReAct with a step budget on a mock model and tools. Report calls, tokens and failures. Predict which handles 8-tool tasks better.

<details><summary>Key for A14.11 (open only after your attempt)</summary>

- **Q1:** A. Reason, act, observe.
- **Q2:** ABC. It does not.
- **Q3:** 3500 tokens (tolerance ±0). 3500.
- **Q4 (marking outline):** Sum of an arithmetic series c0 + k d.
- **Q5 (what a passing submission shows):** The hierarchical version.

</details>

### U14.12 State machines and LangGraph
**Sources:** GEN 11.5
- **Topics:** What a state machine is and why use one for AI; LangChain versus LangGraph; core concepts: nodes and edges; designing the multi-agent DevOps graph (three parts); wiring the team in code and the power of compile(); human-in-the-loop (HITL): pausing the infrastructure agent; caveats: multi-agent infinite loops and state bloat.
- **Results:** Graph termination conditions and loop bounds [D].
- **Build:** the same agent team as a hand-written state machine, then in LangGraph; HITL interrupt and resume. **Tooling:** hand-written state machine first, then LangGraph.
- **Gap-fills:** *[inferred: SLP3 Ch.12]* agent protocols and tool standards (stated at survey level).

**Assignment A14.12** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** In a state-machine view of an agent, edges represent

(A) allowed transitions between nodes  
(B) tokens  
(C) embeddings  
(D) gradients

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Graph frameworks make control flow explicit  
(B) Human-in-the-loop interrupts pause before risky actions  
(C) Loops need bounds to avoid infinite cycles  
(D) State never grows

**Q3 (2 marks, numerical answer (executions)).** Maximum node executions with a loop bound of 5 cycles through 3 nodes.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that a cyclic graph whose loop edge is guarded by a counter with bound B terminates in at most B cycles.

**Q5 (3 marks, programming).** Implement the agent team as a hand-written state machine (standard library), with an interrupt and resume for human approval, then re-implement it in LangGraph (framework use is a design choice here). Acceptance: both versions produce the same trace on a scripted task. Predict the trace length.

<details><summary>Key for A14.12 (open only after your attempt)</summary>

- **Q1:** A. Control flow.
- **Q2:** ABC. State can bloat.
- **Q3:** 15 executions (tolerance ±0). 15.
- **Q4 (marking outline):** The counter strictly increases and the guard fails at B.
- **Q5 (what a passing submission shows):** Equal traces; length equals node executions.

</details>

### U14.13 Agentic memory
**Sources:** GEN 11.6
- **Topics:** The concept and types of memory; episodic memory and its limits; semantic (long-term) memory: writing and reading; the self-healing system in action; caveats: memory contradiction and the needle in a haystack.
- **Build:** episodic buffer and semantic store with conflict resolution and recall evaluation.

**Assignment A14.13** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Episodic memory stores

(A) specific past interactions  
(B) general facts only  
(C) model weights  
(D) embeddings of words only

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Stored memories can contradict each other  
(B) Retrieval can miss a needle in a long memory  
(C) Semantic memory holds distilled long-term facts  
(D) Memory never needs maintenance

**Q3 (2 marks, numerical answer).** Recall@k when 17 of 20 queries retrieve the right memory.

**Q4 (2 marks, prove or derive; every step with its reason).** Give a counterexample showing last-write-wins conflict resolution can overwrite a correct memory with an incorrect newer one.

**Q5 (3 marks, programming).** Implement an episodic buffer and a semantic store with conflict resolution by timestamp and confidence, and a recall evaluation. Predict the effect of adding confidence.

<details><summary>Key for A14.13 (open only after your attempt)</summary>

- **Q1:** A. Event-level records.
- **Q2:** ABC. It needs pruning and conflict handling.
- **Q3:** 0.85 (tolerance ±0.001). 0.85.
- **Q4 (marking outline):** A newer but wrong statement replaces an older correct fact; the policy has no notion of reliability.
- **Q5 (what a passing submission shows):** Fewer wrong overwrites.

</details>

### U14.14 Provenance and citations
**Sources:** GEN 11.7
- **Topics:** What provenance is and why citations matter; the spectrum of citation architectures (inline prompting, structured tool forcing, post-hoc attribution, agentic state provenance); the trade-off matrix; citations in the multi-agent project; UI and UX of citations; post-processing: verifying citations; connecting provenance to state machines.
- **Build:** structured-output citations with a verifier that checks each claim against retrieved spans.

**Assignment A14.14** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Provenance in a RAG answer tells the reader

(A) which sources support each claim  
(B) the model size  
(C) the training loss  
(D) the GPU used

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Inline citations can be prompted  
(B) Structured output can force citation fields  
(C) Post-hoc attribution links claims to sources after generation  
(D) Citations never need verification

**Q3 (2 marks, numerical answer).** Citation precision when 8 of 10 citations actually support their claims.

**Q4 (2 marks, prove or derive; every step with its reason).** With citation precision 1 and recall 0.5, show the F1 score is 2/3.

**Q5 (3 marks, programming).** Implement structured citations (claim, source id, quoted span) and a verifier that checks that the span appears in the source. Predict the false-positive risk of token-overlap verification.

<details><summary>Key for A14.14 (open only after your attempt)</summary>

- **Q1:** A. Traceability.
- **Q2:** ABC. Models can fabricate citations.
- **Q3:** 0.8 (tolerance ±0.001). 0.8.
- **Q4 (marking outline):** F1 = 2 P R/(P + R) = 1/1.5.
- **Q5 (what a passing submission shows):** It accepts spans that overlap lexically but do not entail the claim.

</details>

### U14.15 Multi-agent architecture summary, error handling and best practices
**Sources:** GEN 11.8
- **Topics:** Summary of the multi-agent architecture and the DevOps agent journey; project implementation steps; inter-agent error handling; system prompts; key takeaways of multi-agent orchestration strategy; summary and best practices.
- **Build:** the D14 integrated project (see U18.4).

**Assignment A14.15** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** A robust multi-agent system handles a failed agent by

(A) retries, fallbacks and escalation  
(B) ignoring errors  
(C) restarting training  
(D) increasing temperature

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) System prompts define roles and constraints  
(B) Errors propagate along agent chains  
(C) Retries with backoff help transient failures  
(D) Agents should never log decisions

**Q3 (2 marks, numerical answer).** End-to-end success of a chain of 3 agents each succeeding with probability 0.95.

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the success probability of a series chain and show a single retry improves each component to 1 - (1 - p)^2.

**Q5 (3 marks, programming).** Simulate an agent chain with random failures and policies (none, retry once, fallback). Verify the series formula for the no-policy case to within sampling error. Predict the success rate with one retry.

<details><summary>Key for A14.15 (open only after your attempt)</summary>

- **Q1:** A. Explicit error policy.
- **Q2:** ABC. Logging is essential for debugging.
- **Q3:** 0.8574 (tolerance ±0.001). 0.857.
- **Q4 (marking outline):** Independent attempts; the failure probability squares.
- **Q5 (what a passing submission shows):** About 0.9975^3 = 0.9925.

</details>

## D15. Evaluation, Safety and Responsible AI

Aim: measuring LLM systems rigorously, then the threat landscape (attacks, jailbreaks, privacy, legal risk) and defenses. All attacks are studied only in local or disposable setups against models and data the learner owns (Master Rules 11.1). Benchmarks (recalled, not checked unless noted): Jurafsky–Martin *SLP3* (confirmed: interpretability); Zou et al. (GCG), Chao et al. (PAIR), Carlini et al. on extraction and membership inference, Zheng et al. on LLM-as-a-judge.

### U15.1 LLM evaluation: metric architecture and reference-based metrics
**Sources:** GEN 7.3, 12.1, 12.2; FDL W12
- **Topics:** LLM evaluation: the metric architecture; common metrics; ways to compute metric scores (statistical scorers, model-based scorers); why evaluate LLMs; the setup, the ideal scenario and its limitations; the coefficient of agreement; reference-based metrics: precision and recall (the foundations); ROUGE (recall-oriented n-gram overlap, with code); BLEU (precision-based n-gram scoring, with code); METEOR (F-score with stems and synonyms, with code); BERTScore (semantic similarity, with code); comparison: when to use which, and limitations; benchmarking and evaluation of LLMs.
- **Results:** BLEU brevity penalty and modified n-gram precision [D]; ROUGE-N/L definitions [Def]; Cohen's kappa [D].
- **Build:** ROUGE, BLEU, METEOR-style and BERTScore-style scorers from scratch, checked against reference libraries; inter-annotator agreement.
- **Gap-fills:** *[inferred: SLP3 Ch.13]* human evaluation design, confidence intervals for metrics, benchmark contamination.

**Assignment A15.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** BLEU is primarily based on

(A) n-gram precision  
(B) recall  
(C) embeddings  
(D) human votes

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) ROUGE emphasizes recall  
(B) METEOR uses stems and synonyms  
(C) BERTScore compares contextual embeddings  
(D) BLEU measures recall

**Q3 (2 marks, numerical answer).** Clipped unigram precision of candidate "the the cat" against reference "the cat sat".

**Q4 (2 marks, prove or derive; every step with its reason).** Show that without clipping the candidate "the the the" against reference "the cat" would get unigram precision 1, whereas with clipping it gets 1/3.

**Q5 (3 marks, programming).** Implement ROUGE-1, ROUGE-L, BLEU, a METEOR-like score and a BERTScore-like score (cosine over a toy embedding table), plus Cohen's kappa. Verify clipping on the example. Predict which metric rewards a paraphrase most.

<details><summary>Key for A15.1 (open only after your attempt)</summary>

- **Q1:** A. With a brevity penalty.
- **Q2:** ABC. BLEU is precision-oriented.
- **Q3:** 0.6667 (tolerance ±0.001). The word 'the' is clipped to 1 match (the reference has one); 'cat' matches once; 2 of 3.
- **Q4 (marking outline):** Count matches with and without the clip at the reference count.
- **Q5 (what a passing submission shows):** The embedding-based score.

</details>

### U15.2 LLM-as-a-judge and factuality
**Sources:** GEN 12.3
- **Topics:** LLM-as-a-judge: overview and main variations; the original and revised workflows; typical dimensions to evaluate; factuality: focus and quantification.
- **Results:** Position and verbosity bias of judges and calibration against human labels [S].
- **Build:** pairwise and rubric judges with position-swap debiasing and agreement with human labels.

**Assignment A15.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Position bias in an LLM judge means

(A) it prefers an answer because of its position  
(B) it dislikes long answers  
(C) it ignores the question  
(D) it uses more memory

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Swapping answer order and averaging reduces position bias  
(B) Judges can favour verbose answers  
(C) Rubrics improve consistency  
(D) LLM judges agree perfectly with humans

**Q3 (2 marks, numerical answer).** Cohen's kappa with observed agreement 0.85 and chance agreement 0.5.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that kappa equals 1 for perfect agreement and 0 when agreement equals chance.

**Q5 (3 marks, programming).** Build a pairwise judge and a rubric judge on a deterministic mock scorer with an injected position bias, then debias by order swapping and report agreement with synthetic human labels. Predict the kappa change.

<details><summary>Key for A15.2 (open only after your attempt)</summary>

- **Q1:** A. Order effects.
- **Q2:** ABC. Agreement is imperfect.
- **Q3:** 0.7 (tolerance ±0.001). 0.7.
- **Q4 (marking outline):** Substitute p_o = 1 and p_o = p_e.
- **Q5 (what a passing submission shows):** Kappa rises after debiasing.

</details>

### U15.3 AI safety foundations and threat models
**Sources:** GEN 12.4, 12.5, 12.6
- **Topics:** AI safety foundations: early security (information security), trustworthy ML, AI safety for LLMs, threat models; attacks on models: membership inference, model extraction, model poisoning, model hijacking, adversarial attacks; risks of GenAI: data privacy risks, jailbreak risks, legal and IP risks.
- **Results:** Membership-inference advantage and its link to overfitting [D]; extraction cost via query complexity [S].
- **Build:** a membership-inference test on a model the learner trained; adversarial examples (FGSM) on a small CNN.

**Assignment A15.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Membership inference exploits

(A) a model behaving differently on training data  
(B) network latency  
(C) tokenization  
(D) GPU memory

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Model extraction queries a model to copy it  
(B) Data poisoning corrupts training data  
(C) Adversarial examples are small perturbations that flip predictions  
(D) All attacks require access to the weights

**Q3 (2 marks, numerical answer).** Attack advantage TPR - FPR for TPR 0.7 and FPR 0.4.

**Q4 (2 marks, prove or derive; every step with its reason).** Show the best threshold attack has zero advantage when the loss distributions of members and non-members are identical.

**Q5 (3 marks, programming).** Train an overfitted logistic regression in NumPy, run a loss-threshold membership-inference attack, and craft FGSM examples against a linear model you own. Predict the advantage drop under L2 regularization.

<details><summary>Key for A15.3 (open only after your attempt)</summary>

- **Q1:** A. Overfitting leaks membership.
- **Q2:** ABC. Black-box attacks exist.
- **Q3:** 0.3 (tolerance ±0.001). 0.3.
- **Q4 (marking outline):** TPR(t) = FPR(t) for every threshold.
- **Q5 (what a passing submission shows):** Advantage falls.

</details>

### U15.4 White-box attacks and prompt injection
**Sources:** GEN 12.7
- **Topics:** White-box attacks: Greedy Coordinate Gradient (method and results); indirect prompt injection; prompt leakage.
- **Build:** a GCG-style discrete optimization against a small open model in a disposable sandbox, measuring attack success and transfer.

**Assignment A15.4** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Greedy Coordinate Gradient attacks use

(A) token-level gradients to pick substitutions  
(B) image filters  
(C) network packets  
(D) no gradients

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Indirect injection hides instructions in external content  
(B) Prompt leakage reveals hidden instructions  
(C) White-box attacks need access to gradients or weights  
(D) Black-box attacks use model gradients

**Q3 (2 marks, numerical answer).** Attack success rate for 12 successes in 50 attempts.

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the normal-approximation half-width 1.96 sqrt(p (1 - p)/n) of a 95 percent interval for a success rate.

**Q5 (3 marks, programming).** In a sandbox, implement a GCG-style discrete search against a toy linear text classifier you train, in NumPy by default, and report attack success with intervals. No real model is attacked. Predict the interval half-width for 24 percent over 50 tries.

<details><summary>Key for A15.4 (open only after your attempt)</summary>

- **Q1:** A. White-box discrete optimization.
- **Q2:** ABC. Black-box attacks use only queries.
- **Q3:** 0.24 (tolerance ±0.001). 0.24.
- **Q4 (marking outline):** CLT for a binomial proportion.
- **Q5 (what a passing submission shows):** About 0.118.

</details>

### U15.5 Black-box attacks and the jailbreak taxonomy
**Sources:** GEN 12.8, 12.9
- **Topics:** Black-box attacks: model weakness, categories of responses and overall results; context contamination; DeepWordBug; instruction-centric prompts (TechHazardQA); Prompt Automatic Iterative Refinement (PAIR) and its results; jailbreak taxonomy: language strategies, rhetoric techniques, imaginary words, LLM operational exploitation.
- **Build:** measurement harness (attack success rate by category) against a locally hosted model, with no harmful payloads stored.

**Assignment A15.5** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** PAIR is

(A) an iterative attacker-model refinement of prompts  
(B) a defense  
(C) a dataset  
(D) a tokenizer

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) A taxonomy organizes jailbreaks by strategy  
(B) Context contamination changes the model's prior context  
(C) DeepWordBug perturbs characters  
(D) Jailbreaks are always single-turn

**Q3 (2 marks, numerical answer).** Expected number of queries to the first success with per-query probability 0.1.

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the expected number of trials until the first success for a geometric random variable.

**Q5 (3 marks, programming).** Build a measurement harness reporting attack success by category against a locally hosted mock model with benign placeholder prompts, with confidence intervals. Predict the CI width for 100 trials at 20 percent.

<details><summary>Key for A15.5 (open only after your attempt)</summary>

- **Q1:** A. Prompt Automatic Iterative Refinement.
- **Q2:** ABC. Multi-turn attacks exist.
- **Q3:** 10 (tolerance ±0.001). Geometric mean 10.
- **Q4 (marking outline):** Sum k (1-p)^(k-1) p = 1/p.
- **Q5 (what a passing submission shows):** About plus or minus 0.078.

</details>

### U15.6 Defense, interpretability and ethics
**Sources:** GEN 12.10; DLNLP W12; FDL W5
- **Topics:** Defense: red teaming versus blue teaming and the summary; analysis and interpretability of language models; ethical considerations; explainability as a safety tool.
- **Build:** a red-team/blue-team exercise on the learner's own RAG agent, producing a defect list and fixes.

**Assignment A15.6** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Red teaming is

(A) adversarial testing of your own system  
(B) a training method  
(C) a metric  
(D) a database

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Blue teaming builds and tests defenses  
(B) Defense in depth uses several layers  
(C) Interpretability helps explain failures  
(D) One defense layer suffices

**Q3 (2 marks, numerical answer).** Residual attack success if each of 3 independent layers blocks 70 percent.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that independent layers multiply failure probabilities and give a counterexample where perfectly correlated layers give no benefit.

**Q5 (3 marks, programming).** Run a red-team/blue-team exercise against your own mock RAG agent: write 10 attack cases, a defect list, fixes and a regression test. Predict the residual failures after one round.

<details><summary>Key for A15.6 (open only after your attempt)</summary>

- **Q1:** A. Find failures before attackers do.
- **Q2:** ABC. Single layers fail.
- **Q3:** 0.027 (tolerance ±0.0005). 0.027.
- **Q4 (marking outline):** Independent: product; perfectly correlated layers fail together, so residual equals one layer's.
- **Q5 (what a passing submission shows):** Some attacks still succeed; the defect list drives round two.

</details>


# PART E. ALGORITHMS, SYSTEMS AND INTEGRATION

## D16. ML Systems, Efficiency and Distributed and Federated Learning

Aim: how neural networks, LLMs and graph networks actually run: accelerators, parallelism, memory, serving, compression, fault tolerance and federated training. Benchmarks: Sze–Chen–Yang–Emer, *Efficient Processing of Deep Neural Networks* (listed reference) with research articles shared in the lectures; Boyd et al., Nedić (distributed optimization); Hennessy–Patterson (recalled, not checked).

### U16.1 CNN computation and accelerators
**Sources:** CSO W1–3,10–12, o
- **Topics:** Basics of convolutional neural network (CNN) computations; CNN accelerators 1 and 2; ML accelerators with emerging technologies; workload characterization of ML algorithms; introduction to neural processing units (NPUs); computing kernels of training and inference and how they can be efficiently computed; edge versus cloud execution.
- **Results:** Roofline model and arithmetic intensity of convolution and matmul [D]; dataflow classes (weight-, output-, row-stationary) and data-reuse counts [D].
- **Build:** loop-nest convolution with tiling in NumPy/C and a roofline plot from measured throughput.

**Assignment A16.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The roofline model bounds performance by

(A) peak compute and memory bandwidth times arithmetic intensity  
(B) disk size  
(C) network latency  
(D) clock only

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Arithmetic intensity is FLOPs per byte moved  
(B) Weight-stationary dataflows keep weights in local storage  
(C) NPUs specialize for neural-network kernels  
(D) Convolutions are always compute-bound

**Q3 (2 marks, numerical answer (FLOP/byte)).** Arithmetic intensity (FLOPs per byte) of a 1024^3 float32 matrix multiply.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that a convolution layer with Hout x Wout outputs, Cout output channels, Cin input channels and a K x K kernel performs Hout Wout Cout K^2 Cin multiply-accumulates.

**Q5 (3 marks, programming).** Write a loop-nest convolution with tiling and count memory accesses with and without tiling; plot a roofline from measured throughput. Predict the access reduction from tiling.

<details><summary>Key for A16.1 (open only after your attempt)</summary>

- **Q1:** A. min(peak, bandwidth x intensity).
- **Q2:** ABC. Small layers can be memory-bound.
- **Q3:** 170.7 FLOP/byte (tolerance ±0.01). 2 N^3 FLOPs over 3 N^2 values of 4 bytes.
- **Q4 (marking outline):** Each output element needs K^2 Cin MACs.
- **Q5 (what a passing submission shows):** Roughly the tile reuse factor.

</details>

### U16.2 Parallelism for training, communication and fault tolerance
**Sources:** CSO W4,8; DOML W10
- **Topics:** Parallelism for training large ML models (data, tensor, pipeline parallelism); fault tolerance in ML training (checkpointing, recovery); introduction to neural networks and the ring-allreduce algorithm.
- **Results:** Ring-allreduce bandwidth cost 2(p−1)/p·n [D]; pipeline bubble fraction [D]; Young's checkpoint-interval approximation [D].
- **Build:** ring-allreduce simulator; data-parallel SGD across processes with PyTorch DDP. **Tooling:** ring all-reduce simulator in NumPy; PyTorch DDP for the real run.

**Assignment A16.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Data-parallel training replicates

(A) the model on each worker with different data shards  
(B) the data on each worker  
(C) one layer per worker  
(D) nothing

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Ring all-reduce has per-worker traffic near 2n independent of worker count  
(B) Pipeline parallelism creates a bubble  
(C) Checkpointing limits lost work after a failure  
(D) All-reduce traffic per worker grows linearly with workers

**Q3 (2 marks, numerical answer (GB)).** Per-worker traffic of ring all-reduce for 8 workers and a 1 GB gradient (GB).

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the per-worker traffic 2 (p - 1)/p n of ring all-reduce from its reduce-scatter and all-gather phases.

**Q5 (3 marks, programming).** Write a ring all-reduce simulator in NumPy and verify it sums gradients across 8 simulated workers; then run data-parallel SGD with PyTorch DDP (framework use is a design choice here). Predict the traffic count.

<details><summary>Key for A16.2 (open only after your attempt)</summary>

- **Q1:** A. Gradients are averaged.
- **Q2:** ABC. It stays near 2n.
- **Q3:** 1.75 GB (tolerance ±0.001). 2 (p - 1)/p times n = 1.75.
- **Q4 (marking outline):** Each phase sends (p - 1) chunks of size n/p.
- **Q5 (what a passing submission shows):** 1.75 n per worker.

</details>

### U16.3 LLM decoding, memory management and serving infrastructure
**Sources:** CSO W5–7, o; MFGAI W11
- **Topics:** Basics of large language models; accelerated decoding and memory management of LLMs (KV cache, paged attention, speculative decoding, batching); LLM serving infrastructure (scheduling, continuous batching, queueing); LLMs: models, sampling, inference and quantization methods (inference part).
- **Results:** KV-cache memory per sequence 2·L·H·d_head·T·b bytes (layers L, heads H, head size d_head, tokens T, bytes per value b) [D]; memory-bound decoding throughput bound [D]; M/M/c queue intuition for serving (link to U5.8) [D].
- **Build:** a KV-cache decoder and a continuous-batching scheduler simulator; measure tokens/s versus batch size.

**Assignment A16.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The KV cache stores

(A) keys and values of past tokens  
(B) model weights  
(C) gradients  
(D) token strings

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Continuous batching adds new requests between decode steps  
(B) Paged attention manages KV memory in blocks  
(C) Speculative decoding drafts tokens with a smaller model  
(D) Decoding at batch size 1 is compute-bound

**Q3 (2 marks, numerical answer (bytes)).** KV-cache bytes per token for 32 layers, 32 heads, head size 128 and fp16 (2 bytes).

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the KV-cache memory per sequence 2 L H d_head T b.

**Q5 (3 marks, programming).** Implement a KV-cache decoder for your tiny Transformer and a continuous-batching scheduler simulator. Verify cached and uncached decoding give identical logits to 1e-10, and plot tokens per second versus batch size. Predict the trend.

<details><summary>Key for A16.3 (open only after your attempt)</summary>

- **Q1:** A. Avoids recomputation in decoding.
- **Q2:** ABC. It is memory-bandwidth-bound.
- **Q3:** 524288 bytes (tolerance ±0). 2 (K and V) x L x H x d_head x bytes = 524,288.
- **Q4 (marking outline):** One K and one V vector of size H d_head per layer per token.
- **Q5 (what a passing submission shows):** Throughput rises with batch size until compute saturates.

</details>

### U16.4 Model compression and quantization
**Sources:** FDL W12; MFGAI W11; CSO o
- **Topics:** Model compression (pruning, distillation, low-rank factorization); quantization methods (post-training and quantization-aware; INT8/INT4; NormalFloat as used by QLoRA); system optimization techniques for CNNs, LLMs and graph neural networks.
- **Results:** Quantization error bounds and scale/zero-point derivation [D]; distillation loss with temperature [D].
- **Build:** uniform and per-channel quantization, magnitude pruning and logit distillation from scratch.

**Assignment A16.4** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Symmetric int8 quantization sets the scale to the largest absolute weight divided by

(A) 127  
(B) 255  
(C) 8  
(D) 1

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Per-channel scales usually reduce error versus per-tensor  
(B) Magnitude pruning removes small weights  
(C) Distillation uses temperature-softened teacher outputs  
(D) Quantization never changes outputs

**Q3 (2 marks, numerical answer).** int8 scale for weights in the range [-2.54, 2.54].

**Q4 (2 marks, prove or derive; every step with its reason).** Show that uniform rounding error is at most half the scale.

**Q5 (3 marks, programming).** Implement per-tensor and per-channel int8 quantization, magnitude pruning and logit distillation on your MLP. Plot accuracy against bits. Predict the bit width at which accuracy collapses.

<details><summary>Key for A16.4 (open only after your attempt)</summary>

- **Q1:** A. Maps the largest magnitude to 127.
- **Q2:** ABC. Rounding introduces error.
- **Q3:** 0.02 (tolerance ±0.0001). 0.02.
- **Q4 (marking outline):** The nearest grid point is within scale/2.
- **Q5 (what a passing submission shows):** Around 3-4 bits without calibration.

</details>

### U16.5 Graph neural network inference systems
**Sources:** CSO W9, o
- **Topics:** System optimization for graph neural network (GNN) inference; sparse versus dense kernels; neighbourhood sampling; large language models, CNNs and GNNs as the three kernels studied.
- **Build:** message-passing GCN layer from scratch with sparse matrix multiply and a sampling baseline.
- **Gap-fills:** *[inferred: Hamilton, Graph Representation Learning, recalled, not checked]* GCN, GraphSAGE and attention-based GNN layers (link to U1.4 and U4.8).

**Assignment A16.5** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** A GCN layer computes

(A) normalized adjacency times features times weights  
(B) only weights  
(C) convolution over pixels  
(D) attention over tokens

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) GCN layers are permutation-equivariant  
(B) Neighbourhood sampling bounds memory  
(C) Message passing aggregates neighbour features  
(D) Dense N x N adjacency is always best

**Q3 (2 marks, numerical answer).** Symmetric normalization weight between nodes with self-loop degrees 2 and 3.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that a GCN layer is permutation-equivariant.

**Q5 (3 marks, programming).** Implement a GCN layer with a sparse adjacency using index arrays and np.add.at, plus a neighbour-sampling baseline. Check permutation equivariance numerically. Predict the memory ratio of sparse to dense on a graph with 1% density.

<details><summary>Key for A16.5 (open only after your attempt)</summary>

- **Q1:** A. A_hat H W.
- **Q2:** ABC. Sparse formats scale better.
- **Q3:** 0.4082 (tolerance ±0.001). 1/sqrt 6 = 0.408.
- **Q4 (marking outline):** Relabeling nodes permutes rows and columns of A and rows of H consistently; the output rows permute equally.
- **Q5 (what a passing submission shows):** Sparse storage is far smaller at 1 percent density; index arrays dominate its size.

</details>

### U16.6 Federated learning
**Sources:** DOML W11–12
- **Topics:** Introduction to federated learning; data heterogeneity in federated learning; computational heterogeneity in federated learning; robustness in federated learning.
- **Results:** FedAvg client drift under non-IID data [S]; Byzantine-robust aggregation (median, Krum) guarantees [S].
- **Build:** FedAvg simulation with non-IID partitions and a robust aggregator against a poisoning client.
- **Gap-fills:** *[inferred: McMahan et al., recalled, not checked]* differential privacy and secure aggregation (stated; link to U15.3).

**Assignment A16.6** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** FedAvg aggregates

(A) client model updates weighted by data size  
(B) raw client data  
(C) only gradients of one client  
(D) random weights

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Non-IID data causes client drift  
(B) Robust aggregation resists malicious clients  
(C) Secure aggregation hides individual updates  
(D) Federated learning removes all communication

**Q3 (2 marks, numerical answer).** Weighted average of client parameters 1.0 (100 samples) and 3.0 (300 samples).

**Q4 (2 marks, prove or derive; every step with its reason).** Show that FedAvg with one local gradient step per round equals centralized SGD on the weighted mean gradient.

**Q5 (3 marks, programming).** Simulate FedAvg with non-IID partitions and one malicious client, comparing mean and coordinate-wise median aggregation. Predict which resists the attacker.

<details><summary>Key for A16.6 (open only after your attempt)</summary>

- **Q1:** A. Weighted averaging.
- **Q2:** ABC. Communication is the bottleneck.
- **Q3:** 2.5 (tolerance ±0.001). 2.5.
- **Q4 (marking outline):** Averaging the updated weights averages the gradient steps with the same weights.
- **Q5 (what a passing submission shows):** The coordinate-wise median.

</details>

## D17. Approximation Algorithms and Computational Complexity

Aim: coping with NP-hard problems: the approximation framework, combinatorial algorithms, LP rounding (deterministic and randomized), the primal–dual method, SDP rounding, and hardness of approximation. It reuses linear programming and duality (U8.6, U8.7), probability (U5.7) and graph theory (U1.4), and gives the integer-programming view behind LP relaxations used in D8. Benchmarks (listed by the course, recalled, not checked): Vazirani, *Approximation Algorithms*; Williamson–Shmoys, *The Design of Approximation Algorithms*; Garey–Johnson, *Computers and Intractability*; Arora–Barak, *Computational Complexity*.

### U17.1 Review of NP-completeness and the approximation framework
**Sources:** AA W1, o
- **Topics:** Review of NP-completeness; many real-world problems are NP-complete and unlikely to admit polynomial-time algorithms; designing efficient algorithms for approximately optimal solutions; approximation ratio (relative and absolute guarantees), PTAS and FPTAS; bounding the optimum from below or above as the basic proof technique.
- **Results:** Vertex cover is NP-hard by reduction from independent set [P]; transitivity of polynomial-time reductions [P]; Cook–Levin theorem [X, stated]; definition of an alpha-approximation [Def].
- **Build:** a reduction checker for small SAT to vertex cover instances and an exact exponential-time solver for baselines.
- **Gap-fills:** *[inferred: Garey–Johnson; Arora–Barak, recalled, not checked]* P, NP, co-NP, canonical NP-complete problems (3-SAT, clique, Hamiltonian cycle, subset sum, partition).

**Assignment A17.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** A set S is independent in a graph iff the complement of S is

(A) a vertex cover  
(B) a clique  
(C) a matching  
(D) a spanning tree

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) P is contained in NP  
(B) Polynomial-time reductions are transitive  
(C) An approximation ratio for a minimization problem is at least 1  
(D) If P is not NP, every NP-hard problem has a PTAS

**Q3 (2 marks, numerical answer (vertices)).** Size of a minimum vertex cover of an 8-vertex graph whose largest independent set has 3 vertices.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that S is an independent set iff V minus S is a vertex cover.

**Q5 (3 marks, programming).** Write a brute-force exact vertex cover and independent set solver and the reduction between them; verify the identity size(IS) + size(VC) = n on 200 random graphs. Predict the result.

<details><summary>Key for A17.1 (open only after your attempt)</summary>

- **Q1:** A. Every edge must have an endpoint outside S.
- **Q2:** ABC. Many NP-hard problems provably do not.
- **Q3:** 5 vertices (tolerance ±0). The complement of a maximum independent set is a minimum vertex cover.
- **Q4 (marking outline):** An edge has both endpoints in S exactly when it is uncovered by V minus S.
- **Q5 (what a passing submission shows):** The identity holds on every instance.

</details>

### U17.2 Approximation for vertex cover, set cover and the traveling salesman problem
**Sources:** AA W2
- **Topics:** Approximation algorithm for the vertex cover problem (maximal matching, factor 2); weighted vertex cover; set cover (greedy algorithm with logarithmic ratio); the traveling salesman problem (metric TSP by doubling a minimum spanning tree, factor 2).
- **Results:** Matching-based vertex cover is a 2-approximation [P]; greedy set cover is an H_n-approximation [P]; MST doubling gives a 2-approximation for metric TSP [P]; Christofides' 3/2 bound [X, stated; the matching argument is sketched].
- **Build:** the three algorithms with worst-case instance generators showing the ratios are tight.
- **Gap-fills:** *[inferred: Vazirani, recalled, not checked]* tight examples, the primal-dual view previewed for U17.6.

**Assignment A17.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The maximal-matching algorithm for vertex cover is a

(A) 2-approximation  
(B) 1.5-approximation  
(C) log n-approximation  
(D) exact algorithm

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Greedy set cover has a logarithmic approximation ratio  
(B) Doubling a minimum spanning tree gives a 2-approximation for metric TSP  
(C) General TSP has a constant-factor approximation  
(D) The size of a maximal matching is at most the optimal vertex cover size

**Q3 (2 marks, numerical answer).** Harmonic number H_10, the greedy set-cover ratio for 10 elements.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that the maximal-matching algorithm returns a vertex cover of size at most twice the optimum.

**Q5 (3 marks, programming).** Implement the three algorithms and build tight instances. Predict the ratio of the vertex cover algorithm on the complete bipartite graph K_{n,n}.

<details><summary>Key for A17.2 (open only after your attempt)</summary>

- **Q1:** A. Take both endpoints of every matching edge.
- **Q2:** ABD. General TSP has none unless P = NP.
- **Q3:** 2.929 (tolerance ±0.001). 1 + 1/2 + ... + 1/10 = 2.929.
- **Q4 (marking outline):** Matching edges are disjoint, so OPT needs one endpoint per edge; the algorithm takes two per edge.
- **Q5 (what a passing submission shows):** Exactly 2.

</details>

### U17.3 Approximation for the knapsack problem and job scheduling
**Sources:** AA W3
- **Topics:** Approximation algorithm for the knapsack problem (pseudo-polynomial dynamic programming, profit scaling and an FPTAS); job scheduling problems (list scheduling, longest-processing-time rule, makespan minimization on identical machines).
- **Results:** Knapsack FPTAS error bound [P]; list scheduling is a (2 - 1/m)-approximation [P]; LPT scheduling bound [S].
- **Build:** knapsack DP and FPTAS, list scheduling and LPT on random and adversarial instances, with ratio-versus-instance plots.
- **Gap-fills:** *[inferred: Williamson–Shmoys, recalled, not checked]* PTAS for makespan, strong NP-hardness and why no FPTAS exists for it.

**Assignment A17.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The knapsack FPTAS works by

(A) scaling profits and running the dynamic program  
(B) random sampling  
(C) branching  
(D) ignoring weights

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Knapsack has a pseudo-polynomial dynamic program  
(B) List scheduling is a (2 - 1/m)-approximation  
(C) Knapsack is strongly NP-hard  
(D) LPT is at least as good as arbitrary list order in the worst case

**Q3 (2 marks, numerical answer).** List-scheduling bound 2 - 1/m for m = 4 machines.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that list scheduling has makespan at most (2 - 1/m) times optimal.

**Q5 (3 marks, programming).** Implement the knapsack DP and FPTAS and list scheduling and LPT; compare measured ratios on random and adversarial instances. Predict which scheduler is better on random instances.

<details><summary>Key for A17.3 (open only after your attempt)</summary>

- **Q1:** A. Rounding profits keeps the table small.
- **Q2:** ABD. Knapsack is only weakly NP-hard.
- **Q3:** 1.75 (tolerance ±0.001). 1.75.
- **Q4 (marking outline):** The last job finishes at average load of the others plus its length; both are bounded by OPT.
- **Q5 (what a passing submission shows):** LPT.

</details>

### U17.4 Linear programming basics and deterministic rounding
**Sources:** AA W4–6
- **Topics:** Basics of linear programming (relaxations, duality, integrality gap; see U8.6 and U8.7); deterministic rounding for set cover and vertex cover (threshold rounding); deterministic rounding for the Steiner tree problem and the facility location problem (filtering and rounding).
- **Results:** LP rounding gives an f-approximation for set cover (f = maximum element frequency) [P]; threshold rounding gives a 2-approximation for vertex cover [P]; the integrality gap of the vertex cover LP is 2 [P]; ratios for Steiner tree and facility location rounding [S, ratios to be confirmed against Williamson–Shmoys Ch. 4, recalled, not checked].
- **Build:** LP relaxations solved with your simplex from A8.7 (or a library solver, your choice) and rounded; integrality-gap instances. **Tooling:** your own simplex from A8.7 or `scipy.optimize.linprog` for the LP solves; the rounding logic is yours.

**Assignment A17.4** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The integrality gap of the vertex-cover LP is

(A) 2  
(B) 1  
(C) log n  
(D) n

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Threshold rounding at 1/2 gives a 2-approximation for vertex cover  
(B) LP rounding gives an f-approximation for set cover  
(C) For a minimization problem the LP optimum is at most the integer optimum  
(D) For a minimization problem the LP optimum is at least the integer optimum

**Q3 (2 marks, numerical answer).** Ratio of integer to LP optimum for vertex cover on the complete graph K_10 (integer n-1 versus LP n/2).

**Q4 (2 marks, prove or derive; every step with its reason).** Show that setting x_v = 1/2 for every vertex is feasible for the vertex-cover LP of any graph, and deduce that the LP optimum is at most n/2.

**Q5 (3 marks, programming).** Solve vertex-cover and set-cover LP relaxations (your simplex from A8.7 or a library LP solver, your choice), round, and report the ratios against exact optima on random instances. Predict the vertex-cover ratio bound.

<details><summary>Key for A17.4 (open only after your attempt)</summary>

- **Q1:** A. Shown by the complete graph.
- **Q2:** ABC. The relaxation can only lower the minimum.
- **Q3:** 1.8 (tolerance ±0.001). 9/5 = 1.8.
- **Q4 (marking outline):** Each edge constraint requires x_u + x_v >= 1, which equals 1.
- **Q5 (what a passing submission shows):** At most 2, usually about 1.1 to 1.3 on random graphs.

</details>

### U17.5 Randomized rounding
**Sources:** AA W7–8
- **Topics:** Randomized rounding for the max-SAT problem (random assignment, LP-based randomized rounding, combining the two); randomized rounding for the Steiner tree problem and the facility location problem.
- **Results:** A uniformly random assignment satisfies at least half the clauses in expectation, and a k-literal clause with probability 1 - 2^-k [P]; LP randomized rounding gives 1 - 1/e [P]; the better of the two gives 3/4 [P]; derandomization by conditional expectations [S].
- **Build:** the three max-SAT procedures on random formulas with measured ratios against the LP bound and an exact solver at small size.
- **Gap-fills:** *[inferred: Williamson–Shmoys, recalled, not checked]* Chernoff-bound rounding (link to U5.7) and a randomized-rounding ratio for facility location of about 1 + 2/e.

**Assignment A17.5** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** A uniformly random assignment satisfies a clause with k distinct literals with probability

(A) 1 - 2^-k  
(B) 1/2  
(C) 2^-k  
(D) k/2

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) LP-based randomized rounding gives a 1 - 1/e ratio for max-SAT  
(B) Taking the better of random assignment and LP rounding gives 3/4  
(C) Conditional expectations can derandomize the algorithms  
(D) A random assignment is optimal

**Q3 (2 marks, numerical answer).** Expected fraction of satisfied clauses under a random assignment when every clause has 3 distinct literals.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that a random assignment satisfies at least half of the clauses in expectation, by linearity of expectation.

**Q5 (3 marks, programming).** Implement random assignment, LP randomized rounding and their combination for max-SAT on random formulas and compare with the exact optimum on small ones. Predict the ratio on random 3-SAT with clause density 4.

<details><summary>Key for A17.5 (open only after your attempt)</summary>

- **Q1:** A. Only the all-false assignment of its literals fails.
- **Q2:** ABC. It is not optimal.
- **Q3:** 0.875 (tolerance ±0.001). 7/8.
- **Q4 (marking outline):** Each clause is satisfied with probability at least 1/2; sum over clauses.
- **Q5 (what a passing submission shows):** Random assignment alone gets about 7/8.

</details>

### U17.6 The primal–dual method
**Sources:** AA W9–10
- **Topics:** Primal-dual method for set cover; primal-dual method for the Steiner tree problem; relaxed complementary slackness; growing dual variables until constraints go tight.
- **Results:** Primal-dual set cover is an f-approximation [P]; the primal-dual Steiner forest/tree algorithm is a 2-approximation [S]; relaxed complementary slackness implies the cost bound [P].
- **Build:** dual-ascent set cover and a primal-dual Steiner tree on random graphs, tracking the dual lower bound against the primal cost.

**Assignment A17.6** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The primal-dual method for set cover gives an

(A) f-approximation  
(B) exact solution  
(C) log n guarantee only  
(D) 1/2-approximation

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) Relaxed complementary slackness underlies the analysis  
(B) Any feasible dual solution lower-bounds the optimum  
(C) The primal-dual Steiner algorithm is a 2-approximation  
(D) The method always solves the LP exactly

**Q3 (2 marks, numerical answer).** Bound on the ratio when the primal cost is 14 and the best feasible dual value is 7.5.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that the primal-dual set-cover algorithm is an f-approximation using relaxed complementary slackness.

**Q5 (3 marks, programming).** Implement dual ascent for set cover and a primal-dual Steiner tree on random graphs, tracking the dual lower bound against the primal cost. Predict the final ratio against f.

<details><summary>Key for A17.6 (open only after your attempt)</summary>

- **Q1:** A. f is the maximum element frequency.
- **Q2:** ABC. It builds a feasible primal and dual, not an exact LP solution.
- **Q3:** 1.867 (tolerance ±0.001). OPT >= 7.5 so cost/OPT <= 1.867.
- **Q4 (marking outline):** Each chosen set is tight; cost <= sum over elements of y_e times frequency <= f times dual <= f OPT.
- **Q5 (what a passing submission shows):** At most f, usually well below it.

</details>

### U17.7 Semidefinite programming for max cut, and hardness of approximation
**Sources:** AA W11–12
- **Topics:** Semidefinite programming for the max-cut problem (vector relaxation, random-hyperplane rounding); hardness of approximation: the traveling salesman problem (no constant-factor approximation in general unless P = NP) and job scheduling (hardness of improving on known ratios).
- **Results:** Random-hyperplane rounding of the max-cut SDP gives about 0.878 [P for the per-edge analysis]; general TSP has no polynomial-time approximation within any constant unless P = NP, by a gap-introducing reduction from Hamiltonian cycle [P]; makespan on unrelated machines cannot be approximated within 3/2 - epsilon unless P = NP [X, stated, recalled, not checked].
- **Build:** the SDP solved by a simple low-rank projected-gradient method (or `cvxpy`, your choice) and hyperplane rounding on random graphs, with the measured cut ratio. **Tooling:** a low-rank projected-gradient SDP solver in NumPy, or `cvxpy`; the rounding is yours.
- **Gap-fills:** *[inferred: Williamson–Shmoys; Arora–Barak, recalled, not checked]* PCP theorem (statement), gap problems and the Unique Games Conjecture (statement).

**Assignment A17.7** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** The Goemans-Williamson max-cut algorithm guarantees about

(A) 0.878 of the optimum  
(B) 0.5  
(C) 0.99  
(D) 1/e

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are true?

(A) General TSP cannot be approximated within a constant unless P = NP  
(B) Random hyperplane rounding separates vectors with probability proportional to their angle  
(C) Metric TSP cannot be approximated within any constant  
(D) Gap-introducing reductions prove hardness of approximation

**Q3 (2 marks, numerical answer).** Probability a random hyperplane separates two unit vectors at angle pi/3.

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that a random hyperplane through the origin separates unit vectors at angle theta with probability theta/pi.

**Q5 (3 marks, programming).** Solve the max-cut SDP by a low-rank projected-gradient method (or `cvxpy`, your choice), round with random hyperplanes and report the average cut against the SDP bound on random graphs. Predict the ratio.

<details><summary>Key for A17.7 (open only after your attempt)</summary>

- **Q1:** A. Random hyperplane rounding of the SDP.
- **Q2:** ABD. Metric TSP has a 3/2 approximation.
- **Q3:** 0.3333 (tolerance ±0.001). theta/pi = 1/3.
- **Q4 (marking outline):** Project onto the plane they span; the normal direction is uniform; the separating arcs have measure 2 theta of 2 pi.
- **Q5 (what a passing submission shows):** At least 0.878 on average, usually 0.95 or more on random graphs.

</details>

## D18. Integration and Capstones

Aim: each stretch of the course closes with one integrated, learner-built deliverable defended end to end (Master Rules 9.6). The tutor reviews and questions; the learner writes everything (Master Rules 9.4). **Acceptance criteria common to every capstone (written before work starts, Master Rules 9.3):** required behaviour with automated tests; one number predicted, then measured; one injected failure detected and recovered from; cost estimated, then read from the actual bill (local labs: zero); a threat model; a decision record for each major choice (the judgment turn, Master Rules 10.4); a clean teardown; an oral defence against adversarial questions. Capstone code follows the NumPy-first tooling guideline of the course profile (standard library + NumPy + Matplotlib by default, libraries as oracles in tests, other tools where they serve the deliverable); record each such choice in the decision record. A capstone never replaces unit-by-unit mastery; domain exit audits (Master Rules 8.7) run first.

### U18.1 Capstone A: the mathematics of machine learning, end to end
**Sources:** none (integration unit; assembles earlier units)
- **Topics:** Closes D1–D8. A qualifying-examination-level unseen problem set (at least one proof or derivation and one computational problem per domain, key written first) plus a small reproduction: implement PCA via SVD, ridge/lasso regression, logistic regression by Newton/IRLS, SGD with momentum and Adam, an SVM dual solver and a simple LP/QP solver, each checked against a hand computation and against the professional library.
- **Predict then measure:** the number of Newton iterations to convergence and the condition number of the Hessian; the SGD error floor for a given step size.
- **Injected failure:** an ill-conditioned design matrix; diagnose by SVD and fix by regularization.
- **Defence:** derive the SVD-based PCA, the KKT conditions of the SVM and the convergence rate of gradient descent on a quadratic.
- **Tooling:** capstone code follows the course's NumPy-first guideline; record any other choice in the decision record.

### U18.2 Capstone B: a classical-ML library from scratch
**Sources:** none (integration unit; assembles earlier units)
- **Topics:** Closes D9–D10. A NumPy library (kNN, naive Bayes, CART and random forest, AdaBoost and gradient boosting, kernel SVM, k-means, GMM-EM, PCA, HMM, UCB and Thompson-sampling bandits, tabular Q-learning) with a uniform fit/predict interface, a benchmark harness against scikit-learn on at least five datasets, and a written learning-theory note (PAC/VC bound versus observed generalization gap).
- **Predict then measure:** test-accuracy gap versus scikit-learn for each algorithm; regret slope of UCB versus Thompson sampling.
- **Injected failure:** label noise and covariate shift; detect with the evaluation tools of U9.2.
- **Tooling:** capstone code follows the course's NumPy-first guideline; record any other choice in the decision record.

### U18.3 Capstone C: a deep-learning framework from scratch
**Sources:** none (integration unit; assembles earlier units)
- **Topics:** Closes D11. A reverse-mode autodiff engine with Linear, Conv2d, RNN/LSTM, LayerNorm, Dropout, attention layers; SGD/Adam; a gradient checker; training an MLP, a CNN, an LSTM and a small Transformer on real data; every layer's gradient verified against PyTorch to 1e-5; explanation maps (U11.5) on the CNN.
- **Predict then measure:** parameter counts, FLOPs and the training loss at step 100.
- **Injected failure:** exploding gradients in the LSTM; fix with clipping and initialization changes.
- **Tooling:** capstone code follows the course's NumPy-first guideline; record any other choice in the decision record.

### U18.4 Capstone D: an LLM application platform (RAG + agents + safety)
**Sources:** none (integration unit; assembles earlier units)
- **Topics:** Closes D12, D14 and D15. A grounded multi-agent support/DevOps assistant: ingestion and chunking, hybrid retrieval with reranking, query routing, planner–executor agents in a state machine with human-in-the-loop, episodic and semantic memory, citations with a verifier, semantic caching, observability, an evaluation harness (retrieval metrics, RAGAS-style faithfulness, LLM-as-judge with debiasing) and a red-team/blue-team report covering prompt injection, indirect injection and leakage.
- **Predict then measure:** recall@k, answer faithfulness, p95 latency and cost per request.
- **Injected failure:** poisoned document in the corpus; detect with provenance checks and contain with least-privilege tools.
- **Cost tag:** live API calls only after recorded-response replay and under a spend cap (Master Rules 11.2).
- **Tooling:** capstone code follows the course's NumPy-first guideline; record any other choice in the decision record.

### U18.5 Capstone E: generative models
**Sources:** none (integration unit; assembles earlier units)
- **Topics:** Closes D13. Small-scale GAN (WGAN-GP), VAE/VQ-VAE and DDPM with classifier-free guidance on the same dataset, compared by sample quality (FID proxy), likelihood bound, sampling cost and failure modes (mode collapse, posterior collapse, sampling slowness).
- **Predict then measure:** ELBO versus bits per dimension; sampling steps versus quality curve.
- **Injected failure:** mode collapse in the GAN; diagnose and apply gradient penalty.
- **Tooling:** capstone code follows the course's NumPy-first guideline; record any other choice in the decision record.

### U18.6 Capstone F: ML systems and efficiency
**Sources:** none (integration unit; assembles earlier units)
- **Topics:** Closes D16. Serve a small Transformer with a KV cache, continuous batching and quantization; load-test with a Poisson arrival process against the M/M/c prediction of U5.8; simulate data-parallel training with ring-allreduce and checkpoint recovery; run a federated-averaging experiment with non-IID clients and one malicious client.
- **Predict then measure:** tokens/s versus batch size, memory per request and queueing delay at 70% utilization.
- **Injected failure:** a worker crash mid-training; recover from checkpoint and quantify lost work.
- **Tooling:** capstone code follows the course's NumPy-first guideline; record any other choice in the decision record.

### U18.7 Final integrated capstone: train, align, compress, serve, evaluate and secure a small language model
**Sources:** none (integration unit; assembles earlier units)
- **Topics:** Closes the whole course and assembles parts the learner built in every earlier capstone: pretrain a tiny decoder-only Transformer from scratch (U12.3, U18.3), align it with SFT plus DPO/PPO (U12.8, U10.5), adapt it with LoRA (U12.9), quantize and serve it (U16.3, U16.4), put it behind the RAG-agent platform (U18.4), and evaluate and red-team the full system (U15.1–U15.6). Defended as a professional design review with a decision record for each major choice.
- **Predict then measure:** perplexity versus scaling-law prediction (U12.5); win-rate against the base model; end-to-end latency and cost; attack success rate before and after defenses.
- **Injected failure:** reward hacking in the preference stage or a jailbreak that bypasses the system prompt; detect, patch and re-test.
- **Tooling:** capstone code follows the course's NumPy-first guideline; record any other choice in the decision record.


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
| SA | Stochastic Approximation: Theory and Applications | Gugan Chandrashekhar Mallika Thoppe, IISc Bangalore (106108700) | 1709–1732 | 13 |
| AA | Approximation Algorithms | Palash Dey, IIT Kharagpur (106105471) | 1756–1779 | 13 |
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

**SA** (Stochastic Approximation: Theory and Applications): o → U5.9, U7.7, U8.16, U8.17, U10.6; W1 → U8.16; W2 → U5.9; W3 → U5.9; W4 → U7.7; W5 → U8.16; W6 → U8.16; W7 → U8.17; W8 → U8.17; W9 → U8.17; W10 → U8.17; W11 → U10.6; W12 → U10.6

**AA** (Approximation Algorithms): o → U17.1; W1 → U17.1; W2 → U17.2; W3 → U17.3; W4 → U17.4; W5 → U17.4; W6 → U17.4; W7 → U17.5; W8 → U17.5; W9 → U17.6; W10 → U17.6; W11 → U17.7; W12 → U17.7

**GEN** (GenAI course sections): 1.1 → U12.1; 1.2 → U12.1, U12.2; 1.3 → U12.1; 1.4 → U12.1; 1.5 → U12.1; 1.6 → U12.1; 1.7 → U12.1; 2.1 → U9.0; 2.2 → U9.0; 2.3 → U9.0; 2.4 → U9.0; 2.5 → U9.0; 2.6 → U9.0, U11.8; 2.7 → U11.1, U11.2; 2.8 → U11.3; 3.1 → U11.1; 3.2 → U11.1; 3.3 → U11.2, U11.3; 3.4 → U12.3; 4.1 → U12.3; 4.2 → U12.3; 4.3 → U12.3; 4.4 → U12.3; 4.5 → U12.3; 4.6 → U12.3; 4.7 → U12.3; 5.1 → U12.4, U12.8; 5.2 → U12.7; 5.3 → U12.6; 5.4 → U12.7; 6.1 → U12.7; 6.2 → U12.6; 6.3 → U12.7; 6.4 → U12.7; 7.1 → U12.10; 7.2 → U12.10; 7.3 → U15.1; 7.4 → U12.10; 7.5 → U12.10; 8.1 → U14.1; 8.2 → U14.1; 8.3 → U14.1; 8.4 → U14.2; 8.5 → U14.2; 8.6 → U14.2; 9.1 → U14.3; 9.2 → U14.3; 9.3 → U14.4; 9.4 → U14.4; 9.5 → U14.5; 9.6 → U14.5; 9.7 → U14.6; 10.1 → U14.6; 10.2 → U14.6; 10.3 → U14.7; 10.4 → U14.8; 10.5 → U14.8; 10.6 → U14.8; 10.7 → U14.8; 10.8 → U14.9; 11.1 → U14.9; 11.2 → U14.10; 11.3 → U14.10; 11.4 → U14.11; 11.5 → U14.12; 11.6 → U14.13; 11.7 → U14.14; 11.8 → U14.15; 12.1 → U15.1; 12.2 → U15.1; 12.3 → U15.2; 12.4 → U15.3; 12.5 → U15.3; 12.6 → U15.3; 12.7 → U15.4; 12.8 → U15.5; 12.9 → U15.5; 12.10 → U15.6

## Appendix C. Prerequisite map (Master Rules III.1.6)

### C.1 Prerequisite claims made by the sources (to verify, not trust)

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
| SA | Real analysis, Measure-theoretic Probability, Optimization, Design and Analysis of Algorithms, Ordinary Differential Equations |
| AA | Knowledge of algorithm design principles. |

### C.2 Prerequisite chain to L0, as concrete topics

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
| Measure-theoretic probability (sigma-fields, expectation as an integral, convergence modes), claimed as a prerequisite by SA | U5.9 | L3 | Prove that a limit of measurable functions is measurable; taught first if shaky |
| Real analysis (sequences, compactness, Lipschitz continuity), claimed by SA and CVX | U2.1 | L3 | Prove a compactness statement |
| Design and analysis of algorithms (greedy, dynamic programming, graph algorithms, reductions), claimed by SA and AA | U17.1 and U1.4 | L3 | Analyse an unseen greedy algorithm's cost; taught first if shaky |
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

## Appendix D. Validation against the listed books and references

Master Rules 1.6 and 1.7: benchmarks are named, never linked; contents "recalled, not checked" are labelled so. Checks were run on 2026-11-03.

### D.1 What was checked, and what it changed

| Reference (listed by) | How checked | Outcome |
|---|---|---|
| Jurafsky–Martin, *Speech and Language Processing*, 3rd ed. (DLNLP) | **Checked**: 26 chapter titles read from the authors' site | Ch. 2–12 and 14 map to U12.1–U12.10, U11.7, U14.1–U14.12, U15.6. **Not covered by any source:** speech (Ch. 15–17), machine translation (Ch. 13), and classical linguistic structure (Ch. 18–26: sequence labelling, parsing, information extraction, semantic roles, coreference, discourse, conversation). Listed as a gap candidate in D.2, pending your agreement. |
| Deisenroth–Faisal–Ong, *Mathematics for Machine Learning* (MFML) | **Checked**: 12 chapter titles from the publisher and the book site | All 12 chapters map: Ch. 2 → U4.1–U4.2; Ch. 3 → U4.4; Ch. 4 → U4.6–U4.9; Ch. 5 → U3.1–U3.5; Ch. 6 → D5; Ch. 7 → D8; Ch. 8 → U9.1–U9.2; Ch. 9 → U9.3; Ch. 10 → U9.8; Ch. 11 → U9.9; Ch. 12 → U9.5. Added: Cholesky, Rayleigh quotient, analytic-geometry topics, probabilistic PCA. |
| Boyd–Vandenberghe, *Convex Optimization* (DOML, CVX) | **Partly checked**: parts and chapters 1–8 confirmed from publisher contents; the algorithms part (unconstrained, equality-constrained, interior-point) is *recalled, not checked* | Theory → U8.2, U8.3, U8.6; applications (approximation and fitting, statistical estimation, geometric problems) → U4.10, U8.12; algorithms → U8.8, U8.7. Added: problem taxonomy, epigraph forms, SDP representability. |
| Bach, *Learning Theory from First Principles* (FML) | **Checked**: 15 chapter titles from the PDF | Ch. 2–12, 14, 15 map to U9.1, U9.3–U9.7, U9.13, U8.10, D10, U9.10. **Not in any outline:** Ch. 13 (structured prediction) → gap candidate E.3. |
| Lattimore–Szepesvári, *Bandit Algorithms* (BAN) | **Partly checked**: part structure and several chapter titles from the publisher | D10 covers the stochastic, adversarial, contextual and pure-exploration topics; added MOSS, Bayesian and non-stationary bandits, linear bandits, MDP bridge. Gap candidate: partial monitoring. |
| Goodfellow–Bengio–Courville, *Deep Learning* (MLDL) | **Partly checked**: part structure and chapter headings from the book site | Part I → D4, D5, D8, D9; Part II → D11; Part III: autoencoders → U11.8, structured probabilistic models and Monte Carlo → U9.10, U13.6, deep generative models → D13. Gap candidates: linear factor models, ICA, sparse coding, partition-function estimation, approximate inference. |
| Foster, *Generative Deep Learning*, 2nd ed. (MFGAI) | **Checked**: contents from the publisher | VAEs, GANs, autoregressive, EBMs, diffusion, Transformers map to D13 and U12.3. **Normalizing flows** appear in the book's description and in no outline: added as U13.8. Gap candidates: music generation, world models. |
| Murphy, *Probabilistic Machine Learning: An Introduction* (FML) | **Not verified**: the book site gives its contents only as an image and a PDF | Cited as *recalled, not checked* in D9 and D13. |
| Borkar, *Stochastic Approximation: A Dynamical Systems Viewpoint*; Borkar, *Probability Theory: An Advanced Course*; Williams, *Probability with Martingales*; Grimmett–Stirzaker; Hirsch–Smale–Devaney (all listed by SA) | **Not verified** | Used to label the SA units' gap-fills *recalled, not checked*. Spot-check against the books before closing U5.9, U7.7 and U8.16–U8.17. |
| Vazirani, *Approximation Algorithms*; Williamson–Shmoys, *The Design of Approximation Algorithms* (both listed by AA) | **Not verified** | D17 ratios that the sources do not state (Steiner tree and facility-location rounding, scheduling hardness) are marked *recalled, not checked* in the units. |
| Strang (LA, *Learning from Data*), Axler, Kay, Rosenthal, Johnson–Wichern, Nocedal–Wright, Bishop, Hastie et al., Alpaydin, Duda–Hart–Stork, Haykin, Nielsen, Bengio, Mitchell, Spivak, Thomas–Finney, Kreyszig, Piskunov, O'Neil, Cheney, Artin, Halmos, Herstein, Hoffman–Kunze, Jacobson, Greub, Chvátal, Dantzig–Thapa, Bazaraa et al., Bertsekas, Chong–Zak, Dennis–Schnabel, Sun–Yuan, Rockafellar, Hiriart-Urruty–Lemaréchal, Tikhomirov, Churchill–Brown, Ahlfors, Conway, Debnath–Bhatta, Jain–Iyengar, Miller–Freund, Mayer, Maity, Forsyth, Pradhan–Kumar, Rengaswamy–Suresh, Sze et al., Nedić | **Not verified** (no machine-readable contents reached) | Named as benchmarks and used to label gap-fills as *[inferred: …, recalled, not checked]*. They should be spot-checked against the physical books before a domain is closed (Master Rules 1.6). |


### D.2 Gap candidates (not added; need your agreement per Master Rules 7.4)

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

## Appendix E. Source anomalies, truncations and residual flagged atoms

### E.1 Anomalies in the sources (kept visible, not silently fixed)

| Source | Issue | Handling |
|---|---|---|
| EM2 | prerequisite: Engineering Mathematics I | Recorded in Appendix C. |
| MM | source lists only 4 of the course weeks | Missing weeks or categories are filled from benchmarks and marked *inferred* in the units that cite this source. |
| HEM | source Week 4 text duplicates Week 2 text (copy error); stray "288" in Week 12 | Repeated text is cited as given in each cell; nothing is lost and nothing is double-counted as a new topic. |
| DM | title absent in source | Title inferred from the course content; please confirm (Appendix F.2). |
| OMLH | source lists only 8 weeks; Weeks 2, 6, 8 repeat Weeks 1, 5, 7 text | Missing weeks or categories are filled from benchmarks and marked *inferred* in the units that cite this source. |
| ALAJ | source Weeks 8 and 9 both carry the dynamical-systems text | Repeated text is cited as given in each cell; nothing is lost and nothing is double-counted as a new topic. |
| MLE | title absent in source | Title inferred from the course content; please confirm (Appendix F.2). |
| S50 | heading says 50 techniques; only categories 1-9 appear in the source | Missing weeks or categories are filled from benchmarks and marked *inferred* in the units that cite this source. |
| LPCS | source Weeks 1-3 and 4-5 repeat the same module text | Repeated text is cited as given in each cell; nothing is lost and nothing is double-counted as a new topic. |
| PSS | title absent in source | Title inferred from the course content; please confirm (Appendix F.2). |
| IPS | lines 1579-1594 duplicate Week 1-2 items | Repeated text is cited as given in each cell; nothing is lost and nothing is double-counted as a new topic. |
| CVX | Lines 318–329 are page header/footer text (prerequisites, a pointer to Boyd's lectures, coordinator), interleaved with the lecture list | Prerequisites go to Appendix C; the Boyd lectures are treated as a reference. |
| nptel.txt line 213 | Cites course id 106104573, which matches no course id listed in the file (it follows the Discrete Mathematics block) | Flagged in Appendix F. |
| Typos | 'Grpah', 'Dula' (HEM), 'diinensionality' (ALAK), 'Resarch' (ALAJ), 'liner' (LPCS), 'Borwin', 'Byod', 'Rockafeller', 'Hiriat', 'Seidal' | Meaning taken from context; the unit text uses the correct spelling. |

### E.2 Atoms the word-level check still flags, reviewed by hand

- **Outline-prose atoms flagged:** 272. All were reviewed by hand: they are audience statements, marketing sentences and connective phrases; every topic named in an outline appears in the units that cite it.
- **Non-outline atoms flagged:** 52. All were reviewed: source typos, section labels (for example 'Section VIII', 'Classical Techniques 1'), key-takeaway sentences, and prose in LPCS and FDL whose topics are present under other wording.

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
- `SA:W12` continue.
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

## Appendix F. Notes found inside the source file, and decisions needed

`nptel.txt` contains five notes written to an assistant, not course content. **None was acted on**: no file was downloaded, fetched or deleted. They are reported here so you can decide.

| Line | What the note says | Status |
|---|---|---|
| 99 | "ingest the project files. Also, along with learning this course, I also want to learn to implement these techniques from the scratch in python, numpy, etc." | **Applied to the design**: every unit has a from-scratch **Build** and the project docs (Master Rules) governed the structure. |
| 101 | Fetch NPTEL assignment images for course 106108702 (Mathematical Foundations for ML), weeks 1–12, from `archive.nptel.ac.in`, store as text, delete the images | **Not done.** Needs your OK to download. |
| 103 | "store it in text and delete the images to save space" | Not done (see 101). |
| 105 | "integrate into the curriculum and unify. If there are no assignments provided for certain topics, then create them." | **Unification done.** Authoring missing assignments is a next step (below). |
| 151 | Fetch assignment PDFs for course 111107137 (Essential Mathematics for ML), 8 weeks, extract text, delete the PDFs | **Not done.** Needs your OK to download. |
| 213 | Fetch assignment images for course id 106104573, weeks 1–12 (pattern `noc25_cs27_assignment_Week_N`), store, delete | **Not done.** The id matches no listed course; it follows the Discrete Mathematics block, so it is probably that course. Please confirm. |

### F.1 Assignment status

| Source course | NPTEL assignments | Plan |
|---|---|---|
| All 148 content units | Authored NPTEL-style assignments `A1.1`–`A17.7`, embedded at the end of each unit (keys collapsed under each) | **Done.** Five questions each: MCQ, multiple-select, numerical, prove/derive, NumPy programming. |
| MFML (W1–W12), EMML (8 weeks of PDFs), DM (probable; id to confirm) | Official NPTEL weekly assignments exist (lines 101, 151, 213) | **Not downloaded.** Optional: on your approval they can be fetched, stored as text and mapped to units through Appendix B, to be set beside the authored ones. |

### F.2 Decisions I need from you

1. **Official NPTEL assignments** (F above): do you still want them downloaded as a supplement to the authored ones, with the images and PDFs deleted afterwards? Approve each, or skip.
2. **Gap candidates** in D.2: add any, none, or all (speech and linguistic NLP are the largest).
3. **Truncated sources** (OMLH has 8 of its weeks, MM has 4, S50 has 9 of 50 categories): confirm that benchmark fill-ins are acceptable, or supply the missing outlines.
4. **Missing course titles** (DM, MLE, PSS): confirm the inferred titles in Appendix A.
5. **Where the record lives:** your existing tracker file, or a new one built from the unit list.
6. **Tooling choices:** the NumPy-first guideline leaves me to pick tools per unit; the Build lines say what I chose. Tell me if any choice should change.
