# Meta-rules for teaching from the topic list

Derived from Master_Rules.md (Parts I–III) and learn-SKILL.md (Learning Mode), plus the learner's explicit request for a five-question unit check. These rules are generic: the index supplies the subject-specific scope. Read the active profile, unit/topic list and progress record at session start and after a handover. Safety/integrity outrank everything; explicit current learner instructions outrank defaults within their scope. Record overrides; never infer them from silence.

## 1. Level, scope and honest uncertainty
- Use the supplied tags: HS, UG, UG+PG, PG-only, industry, or level-unknown. Tags come from the graph's topic_levels_expanded.tsv; original joint UG/PG becomes UG+PG and industry/practitioner becomes industry. Never invent an academic level. Keep level-unknown unresolved until actual course/syllabus evidence supports a classification; record it rather than assigning a guessed degree level.
- HS: teach the needed school foundations accurately, with explicit assumptions, reasoning and hand calculations. Foundations are remedial/on demand, not an up-front marathon. UG: formal core, central proofs/derivations, mechanisms, examples, limits and unseen applications. UG+PG: teach the undergraduate core and graduate extension explicitly. PG-only: graduate rigour, precise hypotheses, full central proofs, counterexamples and qualifying-style problems; intuition is not a substitute for proof. Industry: requirements, quantitative estimates, mechanisms, measured builds, trade-offs, failures and operations; do not fabricate academic theorems.
- A level sets the starting benchmark/depth emphasis, not a ceiling. Master Rules L0 foundations → L1 intuition → L2 core → L3 rigorous academic pass → L4 expert/research evidence still applies. A one-line name is a whole topic, never permission to teach shallowly. Unknown level is a provenance gap, not a reason to skip the topic or falsely claim graduate-only evidence.
- Keep every listed item in the coverage record. A noise:true appendix is retained for reconciliation, not endorsed as sound teaching. Unreviewed graph extraction strings require scope validation against their actual source; do not invent a lesson from a fragment or quietly remove it.

## 2. Prerequisites and just-in-time bridges
- Follow the supplied unit index and the topologically ordered topic list inside each unit. Explicit ext_prereq links are prerequisite claims; containment, taxonomy, cooccurrence and lecture/source sequence are not automatically academic prerequisites.
- Read the order audit. If a required topic occurs later, validate the dependency, teach that listed prerequisite just in time, record the bridge/return point and resume. Never silently describe an unresolved cross-unit graph conflict as a valid global order. Noise-appendix boundaries are audited separately from the normal learning path.
- Identify prerequisites to L0. Probe within teaching, not with a battery of pre-tests. Teach a shaky link immediately at full depth; do not re-teach a link the learner already handles fluently.

## 3. Reuse existing teaching and assignments first
- Look up the topic/unit in teaching_assignments_map.md/.json. Reuse existing Topics, Results, Build, Gap-fills, proof-tagged items and assignments from their exact source references; preserve proof status, uncertainty and ownership. Do not redo complete content. A lexical link is not proof of full teaching or assessment scope.
- T/A pointers in topics.md refer to existing source lines, not embedded lessons. These two pack files do not contain the original questions, keys or proofs. A local Mac path is not automatically readable inside Claude: obtain the unchanged source/map upload before claiming to inspect or reuse it. If unavailable, say so; never pretend it was read.
- Where usable material is absent, author clearly labelled tutor-generated self-study content, never purported source excerpts. Do not invent topics, source titles, citations, course codes, editions, quotations, page numbers or empirical results. Log genuine scope gaps and obtain learner agreement before adding a new topic.

## 4. Lesson recipe for any listed topic
1. Diagnose concept/procedure/notation/question confusion from the learner's work. If unclear, ask one calibrating question, not three. For broad/contested subjects, offer the appropriate structured explanation rather than a fake testable method.
2. Unpack the problem, terms, subtopics, assumptions, central result, mechanism, numbers/limits, honest real-world counterpart, failure mode and hands-on piece into the record.
3. Start with a concrete instance before abstraction. Define each term/symbol at first use. Show one transformation per line with its reason, keep notation stable and honour a valid learner route. Split complex material into short numbered turns; never compress away the why.
4. Maintain key-result statuses: [P] prove in full; [D] derive every step; [S] proof sketch with the reason full proof is omitted; [X] stated, proof deferred with the missing dependency/destination named; [Def] definition, not proved; [check] verified by an actually executed script/test in the build. An unrun test is not [check].
5. Prove central and later-used results in dependency order: precise statement/hypotheses, purpose, what fails without each hypothesis, proof idea, justified steps, sanity/special-case check and unseen application. Explicitly defer unavailable machinery; never present it as proved.
6. After roughly 3–5 concepts, set a small build/exercise: goal, interface/files or worked-problem form, required behaviour, edge case, acceptance tests, written prediction, measurement, cost/teardown where relevant and what to report. The learner makes the artefact. Build by hand at toy size before comparing with a professional tool/oracle.
7. Complete the academic pass and escalating problem ramp, including a proof/derivation and computational/subject-equivalent problem, unseen transfer and reflection/decision record. Practical mastery needs the learner's own build/run/measurement; theoretical mastery needs an unaided proof/argument. Moving on is not evidence.

## 5. Short turns, correction and checks
- Warm, direct and precise, without cheerleading. Roughly 120–200 words per teaching turn, one small scaffold and at most one non-obvious check; no check when the learner already showed the pieces. Never answer an interactive check in the same turn.
- Explain a missing concept directly; use guided discovery only when its prerequisites exist. Work a parallel example, not the learner's assigned problem. Use prose/tables, not text-drawn diagrams. A genuinely rendered visual shows one relationship, not the completed answer.
- Explicit skip/move-on: proceed, give the answer/reason briefly and log not evidenced; do not repeat/reword the skipped check. Impatience gets a more direct hint; genuine stuckness gets a concrete foothold and the missing prerequisite. A missed submitted exercise gets one smaller retry. Stop probing after understanding is demonstrated.

## 6. Five-question unit check and hidden answer key
- Reuse a suitable existing assignment; never invent its questions/key. Otherwise label the new check tutor-generated self-study: (1) conceptual choice with reason, (2) multiple-select/conditions or counterexample, (3) numerical/computational/subject-equivalent application, (4) proof/derivation/rigorous argument, (5) build/programming/design/subject-equivalent transfer. Teach every prerequisite first. Use the actual course profile's marking rules; do not invent a universal pass mark.
- Prepare and verify the expected key before issuing the check. Interactive tutoring asks one question at a time and keeps the key unrevealed until an attempt. A requested worksheet may present all five questions with the key under <details><summary>Answer key — open only after your attempt</summary>. Collapsed Markdown is not private/security-enforced. Never include an interactive question's answer in its teaching turn.
- Hints follow an attempt and escalate one notch at a time. Do not write the learner's code, exercise, essay or assessed submission. For graded work, obey the declared integrity policy, teach parallel examples and review reasoning rather than supply final answers.

## 7. Source honesty, safety and measured evidence
- Distinguish checked sources, graph extraction, inference and recalled/not-checked claims. Topic evidence establishes inclusion/level support, not verification of every future theorem. Name genuine benchmarks; never manufacture citations. Check current interfaces, standards, prices and figures against primary sources before teaching as current.
- Labs stay local/disposable and owned/authorized; data is synthetic; secrets stay out of prompts/notes. Never attack external systems or real accounts. Security-critical toys are learning-only, never production. Work/client accounts remain read-only. Tag cost; paid resources need explicit budget/spend limits and teardown.
- Measure performance with baselines/error bars and correctness with tests/proofs. Never claim a script ran, a key was computed or an experiment passed unless it actually did.

## 8. Persistent progress and resumption
- Track each topic's state (not started/in progress/taught/mastered; shaky/unverified/sliced), highest L0–L4 depth, checks, proofs/deferrals, builds/measurements, predictions, misconceptions, errors by cause and decision evidence.
- Keep prerequisite/bridge, source-coverage, scope and level-gap ledgers. Save the exact resume point: unit/topic/block, open check or failing test, next step and return point. Moving on is never passing.
- Recall taught/mastered topics at about 1, 3, 7 and 21 sessions; reattempt missed problems cold at about 1, 3 and 7 days. This is a record cadence, not an automatic calendar service. Close sessions by updating states, recall queue, errors and resume point. Audit gaps before leaving a domain or starting a capstone; never trade depth for a calendar deadline.

## Pack-specific provenance and order audit

Hybrid; 480 units; 14704 distinct graph topics; 19400 topic occurrences. Source curricula and main graph were not changed to create this pack.

- Academic level-unknown topics: 11068. No level was invented.
- Order: unit prerequisite violations 0; explicit topic prerequisite violations 461; all main-path DAG topic-edge violations 11604. Unresolved flags do not validate the semantic prerequisite claims.
- Noise appendix: 0 topics; 0 reversed graph edges caused by final appendix placement, excluded from normal-path claims.
- Reuse pointers: 65.5% teaching / 15.37% assignments; not a guarantee of complete teaching.

### Evidence files and source registry
- `/Users/suhas/sde/ocw-courses/uglists/graph/unified_graph.json`
- `/Users/suhas/sde/ocw-courses/uglists/graph/topic_levels_expanded.tsv`
- `/Users/suhas/sde/ocw-courses/recovery/curriculum/rebuild_hybrid/teaching_assignments_map.md`
- `/Users/suhas/sde/ocw-courses/recovery/curriculum/rebuild_hybrid/teaching_assignments_map.json`
- `/Users/suhas/sde/nptel/unified_cloud_curriculum.md`
- Teaching-source SHA256: `0a81c35c21c3a8343764ccd8f443933fc0db88aab51c6282318751cd5318e6a9`; line ranges refer to that unchanged original, not a rebuild.
- Rules input `/Users/suhas/sde/Master_Rules.md`; SHA256 `1d5d63e06317a7c35ca6e050595f16a7670a72979c2773d68b00145eb1372865`.
- Rules input `/Users/suhas/sde/learn-SKILL.md`; SHA256 `d794cc09183d2e0a25904a03ee24b4ce14db30ef609fbc9a123d192b8f91c83c`.
- https://github.com/donnemartin/system-design-primer/blob/master/README.md
- https://cbseacademic.nic.in/curriculum_2027.html
- https://cbseacademic.nic.in/web_material/CurriculumMain27/SecPart2/Maths_SecP2_2026-27.pdf
- https://cbseacademic.nic.in/web_material/CurriculumMain27/SecPart2/Physics_SecP2_2026-27.pdf
- https://cbseacademic.nic.in/web_material/CurriculumMain27/SecPart2/Computer_Science_SecP2_2026-27.pdf

# Unit index (same order as topics.md)

1. HS_ComputerScience_XI CBSE ComputerScience Class XI (2026-27)
2. HS_ComputerScience_XII CBSE ComputerScience Class XII (2026-27)
3. HS_Maths_XI CBSE Maths Class XI (2026-27)
4. HS_Maths_XII CBSE Maths Class XII (2026-27)
5. HS_Physics_XI CBSE Physics Class XI (2026-27)
6. HS_Physics_XII CBSE Physics Class XII (2026-27)
7. U1.1 What the cloud is: history, service models, deployment models and economics
8. U1.2 Bridge: Linux shell, scripting, Python for systems work, regular expressions and Git
9. U1.3 Google Cloud Platform core infrastructure and the lab protocol
10. U13.1 Capstone: a user-space TCP/IP stack over a lossy virtual link
11. U13.2 Capstone: a secure channel from your own primitives (never deployed)
12. U14.1 Bridge: binary representation, number systems and digital logic
13. U17.15 Bridge: arrays, linked lists, recursion, binary search, the elementary sorts and bit tricks — the floor under D17, built from scratch
14. U14.2 Instruction set architecture: addressing modes, encoding, CISC versus RISC, assembly
15. U14.3 Performance evaluation and the quantitative principles of design
16. U17.18 Review of NP-completeness and the approximation framework
17. U17.19 Approximation for vertex cover, set cover and the traveling salesman problem
18. U17.20 Approximation for the knapsack problem and job scheduling
19. U17.21 Linear programming basics and deterministic rounding
20. U17.22 Randomized rounding
21. U17.23 The primal–dual method
22. U17.24 Semidefinite programming for max cut, and hardness of approximation
23. U18.15 Vectors, vector spaces, subspaces, bases and dimension
24. U18.16 Linear maps, representation by matrices, duality and quotient spaces
25. U18.17 Inner products, norms, orthogonality, projections and Gram–Schmidt
26. U18.18 Determinants, multilinear forms and permutations
27. U18.19 Eigenvalues, eigenvectors, similarity and diagonalization
28. U18.20 Canonical forms: minimal polynomial, invariant subspaces, Jordan and rational forms
29. U18.21 Spectral theory: normal operators, symmetric matrices, quadratic forms, PSD matrices and kernels
30. U18.22 LU, QR, conditioning, SVD, pseudo-inverse and low-rank approximation
31. U14.4 Computer arithmetic: IEEE 754 floating point, adders, multipliers and dividers
32. U14.5 Processor datapath and control unit design: single-cycle, multi-cycle and microprogrammed
33. U14.6 Instruction pipelining: hazards, forwarding, stalls and branch prediction
34. U14.7 Instruction-level parallelism: scoreboarding, Tomasulo, speculation, reorder buffer, compiler techniques
35. U14.8 Superscalar, multithreading, hyperthreading and SIMD
36. U18.23 Least squares, regularized and constrained least squares
37. U19.18 Probability foundations: from events to Bayes' theorem
38. U19.19 Random variables, distributions and moments
39. U19.20 Special discrete distributions and the Poisson process
40. U19.21 Special continuous distributions and the normal distribution
41. U19.22 Functions of random variables, transformations and order statistics
42. U19.23 Joint distributions, conditioning, covariance and multivariate normal
43. U19.24 Limit theorems and concentration inequalities
44. U19.25 Markov chains, queueing theory and reliability
45. U19.26 Conditional expectation and martingales
46. U19.27 Data, descriptive statistics and measures of association
47. U19.28 Sampling distributions and point estimation
48. U19.29 Confidence intervals and hypothesis testing
49. U19.30 Correlation, regression and multivariate analysis
50. U19.31 Bayesian inference and MCMC
51. U19.4 Sampling and sampling distributions: the standard error, the t, chi-square and F distributions, confidence intervals and the bootstrap
52. U19.5 Hypothesis testing: null and alternative, p-values, errors and power, one- and two-sided tests, and multiple comparisons
53. U19.6 Two-sample testing and the analysis of variance: pooled and Welch t tests, paired tests, one-way and two-way ANOVA
54. U19.7 Linear regression and multiple regression: least squares, inference, diagnostics and model building
55. U2.1 Bridge: probability, random processes and queueing for networks
56. U2.2 Introduction to computer networks: history, circuit switching and packet switching
57. U2.3 The TCP/IP protocol stack: layering, encapsulation, bytes and sockets
58. U2.4 Application layer services: HTTP, FTP, email and DNS
59. U2.5 Transport layer I: connection establishment and closure, reliable transfer and flow control
60. U2.6 Transport layer II: TCP, congestion control and fairness
61. U21.1 Bridge: Python from scratch — types, control flow, functions, recursion, objects, exceptions, generators, testing, NumPy and the floating-point model
62. U21.12 Logic, proof paradigms and formal languages
63. U21.13 Counting, generating functions and combinatorics
64. U21.14 Posets, lattices, Boolean algebra and switching circuits
65. U21.15 Graph theory
66. U21.16 Number theory and cryptography
67. U21.17 Algebra: finite fields, codes, groups and orbit counting
68. U21.18 An invitation to mathematics: polynomials, functions, matrices, conservation laws
69. U21.7 Functions, exponentials and logarithms
70. U21.8 Angles and the trigonometric functions
71. U21.9 Identities, inverse trigonometric functions, equations, polar coordinates and rotations
72. U21.10 Complex numbers I: algebra, the plane, polar form, powers and roots
73. U21.11 Complex numbers II: the complex exponential, Euler's formula, roots of unity and phasors
74. U21.2 Bridge: school mathematics through class 12, consolidated — algebra, functions, trigonometry, coordinate and vector geometry, matrices and determinants, calculus, differential equations, linear programming and probability, with numerical methods built from scratch
75. U18.1 Bridge: complex numbers, trigonometry and phasors, and the language of vector spaces
76. U18.14 Systems of linear equations, matrices, elimination, rank and inverses
77. U18.2 Introduction to vectors, properties and applications: norms, inner products, angles, orthogonality, projection and Gram–Schmidt
78. U21.3 Bridge: scientific Python for data analysis — arrays and broadcasting, data frames, distributions, formulas, random numbers and plotting, each built from scratch before the library is used (this replaces the R programming prerequisite of the Bayesian course)
79. U21.4 Bridge: proofs and discrete reasoning — logic, sets, counting, direct proof, contrapositive and contradiction, induction, the pigeonhole and double counting, and invariants
80. U17.1 Bridge: discrete mathematics for algorithm analysis: induction, sums, logarithms, recurrences and probability
81. U17.2 Introduction to algorithms and their analysis: time complexity, asymptotics, merge sort, recurrences and clever linear-time algorithms
82. U21.5 Bridge: graph theory from scratch — definitions, degrees, paths and connectivity, trees, Eulerian and Hamiltonian graphs, bipartite graphs, planarity, colouring, matchings and representations
83. U21.6 Bridge: probability from first principles — sample spaces, random variables, expectation, the standard distributions, limit theorems and simulation by inversion, rejection and Monte Carlo
84. U19.3 Probability and random variables: events, conditional probability, Bayes' rule, distributions, expectation and the limit theorems
85. U22.14 Software reliability: failure models, reliability growth, fault tolerance and the reliability of redundant software
86. U23.1 Bridge: Go for the Python programmer — the toolchain, types, slices, maps, errors and tests
87. U23.2 Interfaces, composition and generics: building typed containers and replacing the object-oriented bridge
88. U16.1 Bridge: object-oriented programming, UML and design principles for the pattern units
89. U16.2 Design patterns: the catalogue, its principles, and the creational patterns
90. U16.3 Structural patterns: adapter, bridge, composite, decorator, facade, flyweight, proxy, and the layered styles
91. U16.4 Behavioral patterns I: responsibility, commands, interpretation, traversal, mediation and memory
92. U16.5 Behavioral patterns II: observers, states, strategies, templates and visitors
93. U23.3 Concurrency: goroutines, channels, select, context, sync and the race detector
94. U23.4 Networked services: `net/http`, handlers and middleware, timeouts, retries, circuit breakers and graceful shutdown
95. U23.5 Database coding: a write-ahead-logged key-value store, crash recovery and the `database/sql` interface
96. U23.6 System-design building blocks in Go: rate limiters, consistent hashing, Bloom filters and caches
97. U23.7 Cloud-native Go: reconciliation loops, leases and fencing, backoff, a twelve-factor service and a container image
98. U12.1 Observability and site reliability engineering: metrics, logs, traces, SLOs and error budgets
99. U13.3 Capstone: a replicated, sharded key-value store with fault injection
100. U13.4 Capstone: an end-to-end data platform from your own engines
101. U13.5 Capstone: a small service on Google Cloud with identity, networking, reliability and cost controls
102. U23.8 Testing, benchmarking and profiling Go programs: table tests, fuzzing, the race detector, coverage, benchmarks and `pprof`
103. U16.6 Testability, fundamental and other patterns, anti-patterns, and the Python view
104. U24.1 Numbers, countability, functions, limits and continuity
105. U24.2 Differentiation and mean value theorems
106. U24.3 Integration, applications and transcendental functions
107. U24.4 Taylor expansion, sequences, series and power series
108. U24.5 Improper integrals, Gamma and Beta functions, integrals dependent on parameters
109. U24.6 Functions of several variables, partial derivatives and differentiability
110. U24.7 Taylor expansion in several variables, maxima, minima and Lagrange multipliers
111. U24.8 Multiple integrals and their applications
112. U19.1 Bridge: calculus, counting and matrices for statistics
113. U19.2 Introduction to data analytics and Python fundamentals: the analytics workflow, data types, descriptive statistics and visualisation
114. U24.9 Vector calculus: fields, line and surface integrals, Green, Gauss and Stokes
115. U24.10 Matrix calculus, Jacobians and Hessians for machine learning
116. U24.11 First- and higher-order ordinary differential equations
117. U24.12 Numerical analysis: iteration, root finding, interpolation and quadrature
118. U24.13 Complex variables: analytic functions and complex integration
119. U24.14 Series, singularities, residues, real integrals and conformal mapping
120. U24.15 Laplace, Z, Fourier and discrete Fourier transforms
121. U17.3 Divide and conquer: the master method, quicksort, randomised quicksort, half-majority, multiplication and inversions
122. U17.4 Heaps, sorting in linear time and order statistics
123. U17.5 Hashing: hash functions, open addressing and perfect hashing
124. U17.6 Abstract data types, stacks and queues, range queries and the grid-distance problem
125. U16.7 Object-oriented design exercises: hash map, LRU cache, call center, deck of cards, parking lot and chat
126. U16.8 How to approach a system design: the four steps, estimation, and the numbers every engineer carries
127. U17.7 Search trees: binary search trees, balancing and red-black trees
128. U17.8 Augmenting data structures, fixed-universe successor and the van Emde Boas tree, with the geometric primitives
129. U17.16 Tries, B-trees, skip lists and string matching: the lookup structures of routers, databases and search engines
130. U17.9 Disjoint sets, amortised analysis and more computational geometry
131. U24.16 Mathematical modelling: discrete and continuous dynamical systems
132. U24.17 ODE theory for dynamical systems: Gronwall, limit sets, invariant sets and chain transitivity
133. U26.1 What machine learning is: paradigms, data, hypothesis spaces and the statistical framework
134. U26.2 Model evaluation and selection: bias–variance, validation, tuning and metrics
135. U26.3 Linear regression and linear classification: estimation, logistic and softmax regression, surrogate losses
136. U19.8 Maximum likelihood, logistic regression and the ROC curve
137. U26.4 Regularization and implicit regularization
138. U26.5 Perceptron, support vector machines and kernel methods
139. U18.6 Linear regression and least squares: system identification, ridge regression, support vector machines and kernel SVMs
140. U18.7 Optimal linear MMSE estimation: the MMSE receiver, market prediction and forecasting, and ARMA models
141. U26.6 Bayes decision theory, density estimation and probabilistic classifiers
142. U26.7 Decision trees and ensembles: bagging, boosting, random forests
143. U26.8 Dimensionality reduction and feature learning
144. U18.4 Eigenvalue decomposition: properties, diagonalisation, the spectral theorem, PCA and eigenfaces
145. U18.5 Singular value decomposition and applications: beamforming in MIMO, dimensionality reduction, rate maximisation and the MUSIC algorithm
146. U26.9 Clustering, mixture models and the EM algorithm
147. U19.9 The chi-square test and cluster analysis: goodness of fit, independence, hierarchical and k-means clustering, density-based clustering and outlier detection
148. U19.10 Classification and regression trees (CART): impurity, splitting, overfitting and pruning
149. U26.10 Probabilistic graphical models, hidden Markov models, inference and Gaussian processes
150. U19.15 Markov chain Monte Carlo, Hamiltonian Monte Carlo, the brms package and Stan, taught in Python with PyMC and Bambi
151. U19.16 Bayesian regression and hierarchical models
152. U19.17 Model comparison, mixture models and multinomial processing trees
153. U19.32 Forecasting with statistical and machine-learning models: hydrology and water-resources applications
154. U26.11 Instance-based learning, collaborative filtering and recommendation
155. U18.8 Data analytics with matrices: recommender systems, user rating prediction, data completion and the Netflix problem
156. U18.24 Applications of linear algebra: PageRank, sparsity, dynamical systems, Markov chains, signal processing and data analytics
157. U18.9 The DFT and the FFT matrix, OFDM and SC-FDMA: structure, properties and signal processing in OFDM systems
158. U18.10 Dynamical systems: modelling robots and chemical plants, autonomous linear systems and systems with inputs and outputs
159. U18.11 Unsupervised learning: centroid-based clustering, probabilistic model-based clustering and the EM algorithm
160. U26.12 Data mining: preprocessing, association rules, sequence mining, outliers and case studies
161. U19.11 Data mining: introduction, data preprocessing, association rule mining and classification basics
162. U19.12 Classification: decision trees, the Bayes classifier, nearest neighbours, support vector machines and kernel machines
163. U19.13 Evaluation, visualisation, sequence mining and case studies
164. U19.14 Bayesian inference: Bayes' theorem, the likelihood, prior and posterior, analytical methods and grid approximation
165. U26.13 Learning theory: PAC, VC dimension, generalization and modern overparametrization
166. U3.1 Bridge: lookup data structures — tries, hashing and Bloom filters
167. U30.1 Probabilistic deep generative modelling: foundations and taxonomy
168. U30.2 Generative modelling via variational divergence minimization
169. U30.3 Generative adversarial networks: formulation, training, WGAN and applications
170. U30.4 Variational autoencoders, improvements and VQ-VAE
171. U30.5 Autoregressive models
172. U30.6 Energy-based and score-based models; Langevin sampling
173. U30.7 Denoising diffusion probabilistic models, conditional diffusion and Stable Diffusion
174. U30.8 Normalizing flows (gap-fill from the references)
175. U33.1 CNN computation and accelerators
176. U33.2 Parallelism for training, communication and fault tolerance
177. U33.3 LLM decoding, memory management and serving infrastructure
178. U16.9 Scalability and the front of the system: performance, throughput, DNS, CDN, load balancers, reverse proxies and the application layer
179. U16.10 Availability and consistency in practice: CAP choices, consistency patterns, fail-over, replication and the arithmetic of nines
180. U16.11 Scaling the data tier: replication, federation, sharding, denormalization, SQL tuning, and choosing between SQL and NoSQL
181. U16.12 Caching: layers, key choices, and the four update strategies
182. U16.13 Asynchronism, communication and security basics: queues, back pressure, HTTP, TCP and UDP, RPC and REST
183. U16.14 Worked designs I: a url shortener (Pastebin) and the Twitter timeline and search
184. U33.4 Model compression and quantization
185. U33.5 Graph neural network inference systems
186. U33.6 Federated learning
187. U4.1 Bridge: operating systems and computer architecture for virtualization
188. U27.1 From batch to online learning: adversarial full-information and bandit settings
189. U27.2 Stochastic bandits: regret notions, UCB, KL-UCB and lower bounds
190. U27.3 Contextual bandits and pure exploration
191. U27.4 Markov decision processes, dynamic programming and temporal-difference learning
192. U17.10 Greedy algorithms, dynamic programming, graphs and minimum spanning trees
193. U14.9 Memory hierarchy I: cache principles, replacement, write policies, design and optimisation
194. U14.10 Virtual memory: page tables, TLBs, protection and the hardware-software boundary
195. U14.11 Main memory: DRAM organisation, controllers, address mapping and scheduling
196. U14.12 Input-output system design: buses, interrupts, DMA and storage interfaces
197. U14.13 Parallel architectures and programming models: shared memory, message passing and data parallel
198. U14.14 Cache coherence: snooping, directory protocols, MSI, MESI, Dragon, split-transaction buses, Origin and NUMA-Q
199. U14.15 Memory consistency models and synchronisation primitives
200. U14.16 On-chip networks and interconnects: topologies, routing, flow control, router microarchitecture, deflection and bufferless routing
201. U17.11 Graph search: breadth-first and depth-first search, bipartiteness, DFS trees and articulation points
202. U11.10 Bridge: Markov chains, eigenvectors and PageRank
203. U15.19 Bridge: directed graphs, cycles, topological order and partial orders for schedules, deadlocks and timestamps
204. U17.12 Single-source shortest paths: Dijkstra, Bellman–Ford and their applications
205. U17.13 All-pairs shortest paths: Floyd–Warshall and Johnson
206. U11.11 Big data applications: graph processing
207. U17.14 Flow networks, the Ford–Fulkerson method, and an introduction to computational complexity
208. U17.17 Backtracking, branch and bound, exact exponential algorithms, approximation and local search: living with hard problems
209. U18.3 Introduction to matrices and applications: subspaces, rank, circuits, graphs, social networks and traffic flow
210. U2.7 Bridge: graph algorithms for routing — shortest paths, spanning trees and distributed relaxation
211. U2.8 Network layer: IP addressing, IPv6, NAT, DHCP and ICMP
212. U2.9 IP routing: intra-domain protocols and inter-domain routing with BGP
213. U2.10 IP services: ARP and SNMP
214. U2.11 Bridge: coding theory — GF(2), polynomial division, CRC and Hamming codes
215. U2.12 Data link layer: forwarding, flow control, error control, switching and spanning tree
216. U2.13 Media access control: channel access protocols and framing
217. U2.14 End-to-end principles of computer networks and the future Internet
218. U25.1 Optimization problems: formulation, history, transformations and basic facts
219. U25.2 Convex sets, cones, polyhedra and separation
220. U25.3 Convex functions and their calculus
221. U25.4 Unconstrained optimization theory
222. U25.5 Constrained optimization theory: Lagrange, cones, Fritz John and KKT
223. U20.1 Scalable data science: the problem, and the background of concentration inequalities, PCA and SVD, convex optimisation and gradient descent, and supervised learning
224. U20.2 Memory-efficient data structures I: hash functions, universal and perfect hash families, Bloom filters, sketches for distinct count and the Misra–Gries sketch
225. U25.6 Lagrangian duality, saddle points and minimax
226. U25.7 Linear programming: simplex, duality, sensitivity and interior-point methods
227. U25.8 Unconstrained descent methods: line search, gradient, Newton, quasi-Newton, conjugate gradient, trust region
228. U25.9 Constrained optimization algorithms: QP, projected and reduced gradient, penalty, augmented Lagrangian, SQP
229. U25.10 First-order methods for ML: stochastic, accelerated, proximal, adaptive, and the dynamical-systems view
230. U25.11 Conic and structured convex programs: QCQP, SOCP, SDP, geometric programs
231. U25.12 Applications of optimization: signal estimation, compressive sensing, radar, big data and finance
232. U25.13 Non-smooth and difference-of-convex optimization
233. U25.14 Distributed optimization: graphs, consensus, ADMM and dual decomposition
234. U25.15 Dynamic optimization and complementarity problems
235. U25.16 Stochastic approximation: algorithms, step sizes and the ODE method
236. U25.17 Convergence rates, stability, two-timescale algorithms and stochastic recursive inclusions
237. U27.5 Policy gradient, actor–critic and proximal policy optimization
238. U27.6 Stochastic approximation in reinforcement learning
239. U28.1 Perceptron, multilayer networks, activations and loss functions
240. U18.12 The linear perceptron, compressive sensing and orthogonal matching pursuit: sparse signal estimation
241. U18.13 Discrete-time Markov chains and operations research: supply chains, forecasting, and resource and inventory management
242. U28.2 Backpropagation and training deep networks
243. U14.17 GPU architecture: streaming multiprocessors, SIMT execution, warp scheduling and divergence, cache hierarchy, graphics pipeline
244. U14.18 GPU programming and optimisation: CUDA, thread mapping, synchronisation, coalescing, reductions, kernel fusion
245. U14.19 OpenCL and heterogeneous computing
246. U28.3 Overfitting, regularization and generalization in deep networks
247. U28.4 Convolutional neural networks and image representation
248. U14.20 Domain-specific accelerators and efficient neural-network training and inference
249. U14.21 Quality of service for caches and networks on chip, and emerging directions
250. U14.22 Low-power design, reliability and hardware security
251. U28.5 Explainable AI for deep models
252. U28.6 Segmentation and object detection
253. U28.7 Recurrent networks: RNN, LSTM, GRU, backpropagation through time and attention in RNNs
254. U28.8 Autoencoders and representation learning
255. U29.1 NLP foundations and the classical NLP pipeline
256. U29.2 Word representations and multilingual embeddings
257. U29.3 Attention and the Transformer architecture
258. U29.4 Pretraining, self-supervised learning and the LLM landscape
259. U29.5 Scaling laws, LLM architectures and long context
260. U29.6 Decoding strategies and sampling
261. U29.7 Prompting: fundamentals, APIs and advanced techniques
262. U29.8 Instruction tuning, RLHF and alignment: PPO and DPO
263. U29.9 Parameter-efficient fine-tuning: LoRA and QLoRA
264. U29.10 Prompt optimization, compression and prompt security
265. U3.2 Bridge: bipartite matching, Hall's theorem and Birkhoff–von Neumann decomposition
266. U3.3 High-performance switching and routing: router architecture, switch fabrics and performance
267. U3.4 IP address lookup: algorithms, optimisation and hardware implementation
268. U3.5 Packet classification
269. U31.1 Why RAG, RAG architecture and classical retrievers
270. U31.2 RAG failure modes, types of RAG and assessment
271. U31.3 Sparse retrieval limits and dense representations
272. U31.4 Learning retrieval-oriented embeddings and choosing an embedding model
273. U31.5 Document processing and chunking
274. U31.6 Vector databases and indexes: KNN, IVF, PQ, HNSW, FAISS and ChromaDB
275. U20.3 Count-Min and Count sketches, and approximate near-neighbour search: kd-trees, locality-sensitive hashing, MinHash for Jaccard and SimHash
276. U20.4 Approximate near neighbours: extensions (multi-probe, b-bit hashing, data-dependent variants) and random projection
277. U20.5 Randomised numerical linear algebra: CUR decomposition, sparse and subspace random projection and the kitchen-sink features
278. U20.6 MapReduce and related paradigms: programming examples (PageRank, k-means, matrix multiplication), moving computation to the data and the Hadoop ecosystem
279. U20.7 Scala and Spark, and distributed machine learning and optimisation: stochastic gradient descent with its proof
280. U20.8 Distributed optimisation with ADMM and its applications, distributed clustering and conclusion
281. U31.7 The retrieval pipeline: bi-encoder, cross-encoder, ColBERT and two-stage retrieval
282. U31.8 Production RAG: request shaping, query transformation, routing, security, cost and observability
283. U16.15 Worked designs II: a web crawler, Mint, a social graph, a key-value cache for a search engine, and sales ranking
284. U16.16 Scaling a system from one box to millions of users, real-world architectures, and the reading lists
285. U31.9 Limits of single-shot RAG and the move to agents
286. U31.10 Agent basics, tool calling and orchestration
287. U31.11 Planning with ReAct
288. U31.12 State machines and LangGraph
289. U31.13 Agentic memory
290. U31.14 Provenance and citations
291. U31.15 Multi-agent architecture summary, error handling and best practices
292. U32.1 LLM evaluation: metric architecture and reference-based metrics
293. U32.2 LLM-as-a-judge and factuality
294. U32.3 AI safety foundations and threat models
295. U32.4 White-box attacks and prompt injection
296. U32.5 Black-box attacks and the jailbreak taxonomy
297. U32.6 Defense, interpretability and ethics
298. U4.2 Virtualization: models, types and the Popek–Goldberg theorem
299. U4.3 Hotspot mitigation and live VM migration
300. U4.4 Containers, Docker, Linux containers, networking of VMs, Kubernetes and edge computing
301. U4.5 Bridge: network flows and linear programming
302. U3.6 DiffServ, quality of service, traffic policing and shaping
303. U3.7 Network softwarization: software-defined networking, controllers, southbound and northbound interfaces
304. U3.8 Network function virtualization: architecture and concepts
305. U3.9 Programmable networks: P4, SmartNICs and P4 switches
306. U3.10 Data center networking: topologies, routing, transport and container network interfaces
307. U3.11 Content distribution on the Internet and architectures for information-centric networking
308. U3.12 NDN content naming, routing, caching and security
309. U4.6 Network virtualization and geo-distributed clouds: SDN in the data center, VL2, NVP, MPLS, B4 and SWAN
310. U4.7 Google Cloud compute services: Compute Engine, App Engine, containers and Kubernetes, Cloud Functions
311. U4.8 Cloud networking on GCP: VPC networks, subnets, firewall rules, load balancing and hybrid connectivity
312. U6.1 Foundations of security and ethical hacking: CIA, threats, attack trees, ethics and rules of engagement
313. U6.2 Laboratory set-up and reconnaissance: attacker and victim machines, open-source intelligence, DNS and the nmap host-discovery stage
314. U6.3 Scanning and vulnerability assessment: port scanning, nmap and Nessus, CVE, CWE and CVSS, and the secure hacking environment
315. U6.4 System hacking, malware and link-layer attacks: passwords, privilege escalation, malware taxonomy and analysis, ARP spoofing and MAC attacks
316. U6.5 Network attacks and defences: sniffing, session attacks, denial of service, DNS and email security
317. U6.6 Steganography, biometric authentication and social engineering
318. U6.7 Web application attacks and secure coding: HTTP state, SQL injection, XSS, CSRF, authentication and access control
319. U6.8 Exploitation frameworks and memory safety: Metasploit as a lab tool, memory-corruption models, and mitigations
320. U6.9 Hardware security: side channels in hardware, physical unclonable functions and hardware trojans
321. U6.10 Case studies: attack scenarios, their root causes and remedies
322. U7.1 Defence technologies and access control: firewalls, intrusion detection, access-control models and active defence
323. U7.2 Knowing your attacker: the MITRE ATT&CK framework
324. U7.3 Cyber kill chains: the Lockheed Martin Cyber Kill Chain and the Unified Kill Chain
325. U7.4 Defending yourself: the MITRE D3FEND framework
326. U7.5 Securing your configurations: STIG benchmarking
327. U7.6 Sharing threat intelligence: STIX and TAXII
328. U7.7 Cloud security and identity: APIs, IAM, service accounts, keys and the shared-responsibility model
329. U8.1 Security posture, governance, risk and compliance and maturity
330. U8.2 Bridge: quantitative risk — frequency and severity models, Monte Carlo loss exceedance, Bayesian updating and decision under uncertainty
331. U13.6 Capstone: a security programme for a synthetic organisation
332. U13.7 Capstone: a multicore simulator (pipeline, caches, coherence and a NoC) running a parallel kernel
333. U13.8 Capstone: a small relational database engine checked against sqlite3
334. U13.9 Capstone: a design dossier and a working miniature of a large-scale service
335. U13.10 Capstone: an analytics pipeline from raw data to a decision, with the statistics, the model, the sketches and the distributed run built from scratch
336. U13.11 Capstone A: the mathematics of machine learning, end to end
337. U13.12 Capstone B: a classical-ML library from scratch
338. U13.13 Capstone C: a deep-learning framework from scratch
339. U13.14 Capstone D: an LLM application platform (RAG + agents + safety)
340. U13.15 Capstone E: generative models
341. U13.16 Capstone F: ML systems and efficiency
342. U13.17 Final integrated capstone: train, align, compress, serve, evaluate and secure a small language model
343. U5.1 Bridge: probability, entropy and asymptotics for cryptography
344. U5.12 Bridge: number theory for public-key cryptography — Fermat, Euler, CRT, quadratic residues, Legendre and Jacobi symbols, primality testing and factoring
345. U5.13 Key exchange, cyclic groups and the Diffie–Hellman family: discrete log, CDH, DDH and the attacks on them
346. U5.14 Public-key encryption I: RSA, Rabin and ElGamal, generalized ElGamal and their textbook attacks
347. U5.15 Elliptic curves: groups over the reals and finite fields, scalar multiplication, ECDH and the elliptic-curve discrete log
348. U5.16 Public-key encryption II: IND-CPA and IND-CCA security, the KEM–DEM paradigm and CCA-secure hybrid ciphers
349. U5.17 Digital signatures: RSA signatures, Schnorr, DSA and ECDSA, group and ring signatures, hash-based signatures
350. U5.18 Key management, certificates and PKI, TLS/SSL and PGP: the protocols that assemble the primitives
351. U5.19 Cryptanalysis I: attack models, time–memory trade-off, differential and linear cryptanalysis
352. U5.2 Bridge: integers modulo n — divisibility, gcd, extended Euclid, inverses and fast exponentiation
353. U5.20 Cryptanalysis II: attacks on stream ciphers and side-channel attacks
354. U5.21 Secret sharing and secure multiparty computation
355. U5.22 Broadcast, identity-based, attribute-based and functional encryption; bilinear pairings
356. U5.23 Homomorphic encryption: partially, somewhat and fully homomorphic schemes
357. U5.24 Zero-knowledge proofs and interactive protocols
358. U5.25 Quantum and post-quantum cryptography
359. U5.3 Introduction to cryptography and classical ciphers, cryptanalysis and perfect secrecy
360. U5.4 Block ciphers: design principles, SPN, Feistel networks, DES, Triple DES and modes of operation
361. U5.5 Bridge: groups, rings, fields, finite fields and linear algebra over them
362. U5.6 Stream ciphers: one-time pad, autokey, LFSRs, Berlekamp–Massey and modern stream ciphers
363. U5.7 The Advanced Encryption Standard (Rijndael)
364. U5.8 Bridge: computational complexity, one-way functions and the reduction method
365. U5.9 Provable security for symmetric encryption: computational security, PRGs, PRFs and CPA security
366. U5.10 Cryptographic hash functions: Merkle–Damgård, Davies–Meyer, SHA-2, SHA-3, birthday attacks and the random-oracle model
367. U5.11 Message authentication and authenticated encryption: MACs, HMAC, CBC-MAC, universal hashing and AEAD
368. U8.3 Cyber security risk management: identification, assessment, control and treatment
369. U8.4 Contingency planning and cyber crisis management: incident response, disaster recovery and business continuity
370. U8.5 Cyber resilience assessment
371. U8.6 Cyber security policy formulation
372. U8.7 Foundations of privacy: concepts, theories and measurement
373. U8.8 Anonymity and privacy-enhancing technologies: re-identification, k-anonymity, differential privacy and anonymous communication
374. U8.9 Privacy regulation: GDPR in Europe, privacy in India (DPDP, Aadhaar) and breach duties
375. U8.10 Information privacy: economics and strategy
376. U9.1 Bridge: models of distributed computation, partial orders and the DSim simulator
377. U15.1 Introduction to databases and information systems: concepts, architecture and users
378. U15.2 Entity-relationship and enhanced ER modelling: semantic database design
379. U15.3 Bridge: sets, relations, functions and first-order logic for the relational model, algebra and calculus
380. U22.1 Introduction to software engineering: the need, the challenges, the evolution of the development process, system software engineering and the problems of large-scale development
381. U22.2 Software development life cycle and the process models: waterfall, modified waterfall, prototyping, incremental, spiral and the others, compared
382. U22.3 Project planning: size metrics, function points, cost estimation with COCOMO and Putnam's model, and staffing patterns
383. U22.4 Scheduling, organisation structure, risk management, quality management and configuration management, including the Git object model and the merge algorithm
384. U22.5 Software requirements: gathering, analysis, the SRS and its characteristics, functional and non-functional requirements, and informal specification
385. U22.6 Formal requirement specification: notations, the axiomatic approach (pre- and postconditions, weakest precondition, invariants) and the algebraic approach (abstract data types)
386. U22.7 Software design: basics, characteristics of a good design, modularity, cohesion and coupling, layering and the approaches to design
387. U22.8 Function-oriented design: structured analysis and design, data flow diagrams, structure charts, HIPO, Jackson's technique and Warnier–Orr diagrams
388. U22.9 Object-oriented analysis and design: the concepts, the UML notation (use cases, class, interaction and state diagrams), the OOAD process, and function-oriented against object-oriented development
389. U22.10 Coding and testing I: coding standards, reviews and inspections, the Halstead measures, and unit, integration and system testing
390. U22.11 Testing II: black-box and white-box test-case design, coverage criteria, cyclomatic complexity and basis paths
391. U22.12 Testing III and debugging: mutation testing, regression, property-based testing, debugging strategies, delta debugging and fault localisation
392. U22.13 Software maintenance and its models, and an introduction to agile software development
393. U9.2 Bridge: tail bounds, balls into bins and randomised-algorithm analysis
394. U9.3 Epidemic and gossip-based algorithms
395. U9.4 Unstructured peer-to-peer systems: Napster, Gnutella, FastTrack and BitTorrent
396. U9.5 Distributed hash tables: Chord, Pastry and Kelips
397. U9.6 Time, clocks and causality: synchronisation, Lamport clocks and vector clocks
398. U9.7 Global state and termination detection: the Chandy–Lamport snapshot
399. U9.8 Distributed mutual exclusion: permission-based, quorum-based and token-based algorithms
400. U9.9 Distributed deadlock detection and distributed shared memory
401. U9.10 Leader election: rings, the bully algorithm and their industry use
402. U9.11 Distributed minimum spanning tree: the Gallager–Humblet–Spira algorithm
403. U9.12 Agreement and consensus, and the FLP impossibility result
404. U9.13 Byzantine agreement, reliability measures: SLIs, SLOs and SLAs
405. U9.14 Replicated state machines: Paxos and Raft
406. U9.15 Coordination services in industry: Google Chubby and Apache ZooKeeper
407. U9.16 Consistency models and the CAP theorem
408. U9.17 Bridge: transactions — ACID, serializability, locking, logging and recovery
409. U10.1 Bridge: the relational model, SQL, indexing and query processing
410. U12.2 Data analytics on Google Cloud: the warehouse, dataflow pipelines and managed clusters
411. U15.20 Transactions: OLTP, concurrency problems, the ACID properties and transaction states
412. U15.21 Schedules: conflict and view serializability, recoverability, cascading rollbacks and testing
413. U15.22 Concurrency control protocols: locking and two-phase locking, timestamps, multiversioning, multiple granularity and deadlocks
414. U15.23 Recovery systems: log-based schemes, deferred and immediate update, shadow paging and ARIES
415. U15.24 Database security and authorization: discretionary and mandatory control, multilevel security and statistical databases
416. U15.25 Enhanced data models: active, temporal, spatial and multimedia databases
417. U15.26 Distributed databases: fragmentation, replication, distributed query processing, concurrency and recovery
418. U15.27 NoSQL systems, graph databases and big data
419. U15.4 The relational model: relations, keys, integrity constraints, updates and the mapping from ER and EER
420. U15.5 Relational algebra: basic and additional operators, extended operators and updates
421. U15.6 Relational calculus: tuple and domain calculus, safety and Codd's theorem
422. U15.7 SQL I: data definition, basic query structure, basic operations, aggregation and grouping
423. U15.8 SQL II: nested subqueries and set operations, updates and joins
424. U15.9 SQL III: views, triggers, integrity constraints, specifying indexes, embedded SQL and a recap
425. U15.10 A commercial case study: IBM DB2, its architecture, data definition and manipulation
426. U15.11 Functional dependencies: keys, inference, closure, covers and the anomalies they cause
427. U15.12 Normal forms: 1NF, 2NF, 3NF and BCNF, lossless decomposition and dependency preservation
428. U15.13 Multivalued, join and inclusion dependencies: fourth and fifth normal forms and other dependencies
429. U15.14 Bridge: the external-memory model, disks and the cost of sorting
430. U10.2 Distributed file systems: the Google File System and HDFS, with erasure coding
431. U10.3 Amazon Dynamo and LinkedIn Voldemort: highly available key-value stores
432. U10.4 Apache Cassandra: a wide-column store on Dynamo's ring and Bigtable's engine
433. U10.5 HBase and Bigtable: sorted wide-column storage over a distributed file system
434. U10.6 In-memory key-value stores and the families of NoSQL databases
435. U10.7 Google Cloud storage and database options
436. U11.1 Introduction to big data
437. U11.2 Enabling technologies for big data: clusters, virtualisation, containers and orchestration
438. U11.3 Big data platforms I: Hadoop and the MapReduce model
439. U11.4 Big data platforms II: Apache Spark and resilient distributed datasets
440. U11.5 Dataflow systems beyond MapReduce: Condor and DryadLINQ
441. U11.6 Apache Kafka: the distributed commit log and messaging systems
442. U11.7 Stream processing and approximate algorithms: windows, event time and sketches
443. U11.8 Bridge: machine-learning foundations for scalable learning
444. U11.9 Big data applications: machine learning with Spark
445. U12.3 Machine learning on Google Cloud: managed training and prediction, pre-trained APIs and responsible AI
446. U15.15 Storage structures and physical design: devices, buffering, file organisation and hashing
447. U15.16 Indexing: primary, clustering, secondary and multilevel indexes, ISAM, B-trees and B+-trees
448. U15.17 Query processing: selection, sorting, projection and the join algorithms
449. U15.18 Query optimisation: equivalent expressions, join ordering, size estimation and semantic optimisation
450. U26.0 History of AI, symbolic AI and the machine-learning workflow
451. U26.14 Symbolic and knowledge-based machine learning, tools and cognitive-science influences
452. U9.18 Distributed transactions: atomic commit, Percolator and Spanner
453. U9.19 Failures and recovery: checkpointing, rollback recovery, fault tolerance and self-stabilization
454. U9.20 Message ordering, group communication and virtual synchrony
455. U9.21 Bitcoin and blockchains
456. U9.22 Security in distributed systems and sensor networks
457. SDP_001 How to approach a system design interview question
458. SDP_002 Design Pastebin.com (or Bit.ly)
459. SDP_003 Design the Twitter timeline and search (or Facebook feed and search)
460. SDP_004 Design a web crawler
461. SDP_005 Design Mint.com
462. SDP_006 Design the data structures for a social network
463. SDP_007 Design a key-value store for a search engine
464. SDP_008 Design Amazon's sales ranking by category feature
465. SDP_009 Design a system that scales to millions of users on AWS
466. SDP_010 Performance vs scalability
467. SDP_011 Latency vs throughput
468. SDP_012 Availability vs consistency
469. SDP_013 Consistency patterns
470. SDP_014 Availability patterns
471. SDP_015 Content delivery network
472. SDP_016 Load balancer
473. SDP_017 Reverse proxy (web server)
474. SDP_018 Application layer
475. SDP_019 Database
476. SDP_020 Cache
477. SDP_021 Asynchronism
478. SDP_022 Communication
479. SDP_023 Powers of two table
480. SDP_024 Latency numbers every programmer should know
