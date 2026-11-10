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

Staged enhance; 450 units; 14574 distinct graph topics; 19247 topic occurrences. Source curricula and main graph were not changed to create this pack.

- Academic level-unknown topics: 11068. No level was invented.
- Order: unit prerequisite violations 0; explicit topic prerequisite violations 456; all main-path DAG topic-edge violations 11595. Unresolved flags do not validate the semantic prerequisite claims.
- Noise appendix: 0 topics; 0 reversed graph edges caused by final appendix placement, excluded from normal-path claims.
- Reuse pointers: 65.69% teaching / 15.42% assignments; not a guarantee of complete teaching.
- This pack reorders the existing 450 IDs using verified hybrid DAG order without rewriting staged curriculum/index. Its explicit per-unit inventory excludes mere global appendix source-label mentions.

### Evidence files and source registry
- `/Users/suhas/sde/ocw-courses/uglists/graph/unified_graph.json`
- `/Users/suhas/sde/ocw-courses/uglists/graph/topic_levels_expanded.tsv`
- `/Users/suhas/sde/ocw-courses/recovery/curriculum/out/teaching_assignments_map.md`
- `/Users/suhas/sde/ocw-courses/recovery/curriculum/out/teaching_assignments_map.json`
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

1. U1.1 What the cloud is: history, service models, deployment models and economics
2. U1.2 Bridge: Linux shell, scripting, Python for systems work, regular expressions and Git
3. U1.3 Google Cloud Platform core infrastructure and the lab protocol
4. U13.1 Capstone: a user-space TCP/IP stack over a lossy virtual link
5. U13.2 Capstone: a secure channel from your own primitives (never deployed)
6. U14.1 Bridge: binary representation, number systems and digital logic
7. U17.15 Bridge: arrays, linked lists, recursion, binary search, the elementary sorts and bit tricks — the floor under D17, built from scratch
8. U14.2 Instruction set architecture: addressing modes, encoding, CISC versus RISC, assembly
9. U14.3 Performance evaluation and the quantitative principles of design
10. U17.18 Review of NP-completeness and the approximation framework
11. U17.19 Approximation for vertex cover, set cover and the traveling salesman problem
12. U17.20 Approximation for the knapsack problem and job scheduling
13. U17.21 Linear programming basics and deterministic rounding
14. U17.22 Randomized rounding
15. U17.23 The primal–dual method
16. U17.24 Semidefinite programming for max cut, and hardness of approximation
17. U18.15 Vectors, vector spaces, subspaces, bases and dimension
18. U18.16 Linear maps, representation by matrices, duality and quotient spaces
19. U18.17 Inner products, norms, orthogonality, projections and Gram–Schmidt
20. U18.18 Determinants, multilinear forms and permutations
21. U18.19 Eigenvalues, eigenvectors, similarity and diagonalization
22. U18.20 Canonical forms: minimal polynomial, invariant subspaces, Jordan and rational forms
23. U18.21 Spectral theory: normal operators, symmetric matrices, quadratic forms, PSD matrices and kernels
24. U18.22 LU, QR, conditioning, SVD, pseudo-inverse and low-rank approximation
25. U14.4 Computer arithmetic: IEEE 754 floating point, adders, multipliers and dividers
26. U14.5 Processor datapath and control unit design: single-cycle, multi-cycle and microprogrammed
27. U14.6 Instruction pipelining: hazards, forwarding, stalls and branch prediction
28. U14.7 Instruction-level parallelism: scoreboarding, Tomasulo, speculation, reorder buffer, compiler techniques
29. U14.8 Superscalar, multithreading, hyperthreading and SIMD
30. U18.23 Least squares, regularized and constrained least squares
31. U19.18 Probability foundations: from events to Bayes' theorem
32. U19.19 Random variables, distributions and moments
33. U19.20 Special discrete distributions and the Poisson process
34. U19.21 Special continuous distributions and the normal distribution
35. U19.22 Functions of random variables, transformations and order statistics
36. U19.23 Joint distributions, conditioning, covariance and multivariate normal
37. U19.24 Limit theorems and concentration inequalities
38. U19.25 Markov chains, queueing theory and reliability
39. U19.26 Conditional expectation and martingales
40. U19.27 Data, descriptive statistics and measures of association
41. U19.28 Sampling distributions and point estimation
42. U19.29 Confidence intervals and hypothesis testing
43. U19.30 Correlation, regression and multivariate analysis
44. U19.31 Bayesian inference and MCMC
45. U19.4 Sampling and sampling distributions: the standard error, the t, chi-square and F distributions, confidence intervals and the bootstrap
46. U19.5 Hypothesis testing: null and alternative, p-values, errors and power, one- and two-sided tests, and multiple comparisons
47. U19.6 Two-sample testing and the analysis of variance: pooled and Welch t tests, paired tests, one-way and two-way ANOVA
48. U19.7 Linear regression and multiple regression: least squares, inference, diagnostics and model building
49. U2.1 Bridge: probability, random processes and queueing for networks
50. U2.2 Introduction to computer networks: history, circuit switching and packet switching
51. U2.3 The TCP/IP protocol stack: layering, encapsulation, bytes and sockets
52. U2.4 Application layer services: HTTP, FTP, email and DNS
53. U2.5 Transport layer I: connection establishment and closure, reliable transfer and flow control
54. U2.6 Transport layer II: TCP, congestion control and fairness
55. U21.1 Bridge: Python from scratch — types, control flow, functions, recursion, objects, exceptions, generators, testing, NumPy and the floating-point model
56. U21.12 Logic, proof paradigms and formal languages
57. U21.13 Counting, generating functions and combinatorics
58. U21.14 Posets, lattices, Boolean algebra and switching circuits
59. U21.15 Graph theory
60. U21.16 Number theory and cryptography
61. U21.17 Algebra: finite fields, codes, groups and orbit counting
62. U21.18 An invitation to mathematics: polynomials, functions, matrices, conservation laws
63. U21.7 Functions, exponentials and logarithms
64. U21.8 Angles and the trigonometric functions
65. U21.9 Identities, inverse trigonometric functions, equations, polar coordinates and rotations
66. U21.10 Complex numbers I: algebra, the plane, polar form, powers and roots
67. U21.11 Complex numbers II: the complex exponential, Euler's formula, roots of unity and phasors
68. U21.2 Bridge: school mathematics through class 12, consolidated — algebra, functions, trigonometry, coordinate and vector geometry, matrices and determinants, calculus, differential equations, linear programming and probability, with numerical methods built from scratch
69. U18.1 Bridge: complex numbers, trigonometry and phasors, and the language of vector spaces
70. U18.14 Systems of linear equations, matrices, elimination, rank and inverses
71. U18.2 Introduction to vectors, properties and applications: norms, inner products, angles, orthogonality, projection and Gram–Schmidt
72. U21.3 Bridge: scientific Python for data analysis — arrays and broadcasting, data frames, distributions, formulas, random numbers and plotting, each built from scratch before the library is used (this replaces the R programming prerequisite of the Bayesian course)
73. U21.4 Bridge: proofs and discrete reasoning — logic, sets, counting, direct proof, contrapositive and contradiction, induction, the pigeonhole and double counting, and invariants
74. U17.1 Bridge: discrete mathematics for algorithm analysis: induction, sums, logarithms, recurrences and probability
75. U17.2 Introduction to algorithms and their analysis: time complexity, asymptotics, merge sort, recurrences and clever linear-time algorithms
76. U21.5 Bridge: graph theory from scratch — definitions, degrees, paths and connectivity, trees, Eulerian and Hamiltonian graphs, bipartite graphs, planarity, colouring, matchings and representations
77. U21.6 Bridge: probability from first principles — sample spaces, random variables, expectation, the standard distributions, limit theorems and simulation by inversion, rejection and Monte Carlo
78. U19.3 Probability and random variables: events, conditional probability, Bayes' rule, distributions, expectation and the limit theorems
79. U22.14 Software reliability: failure models, reliability growth, fault tolerance and the reliability of redundant software
80. U23.1 Bridge: Go for the Python programmer — the toolchain, types, slices, maps, errors and tests
81. U23.2 Interfaces, composition and generics: building typed containers and replacing the object-oriented bridge
82. U16.1 Bridge: object-oriented programming, UML and design principles for the pattern units
83. U16.2 Design patterns: the catalogue, its principles, and the creational patterns
84. U16.3 Structural patterns: adapter, bridge, composite, decorator, facade, flyweight, proxy, and the layered styles
85. U16.4 Behavioral patterns I: responsibility, commands, interpretation, traversal, mediation and memory
86. U16.5 Behavioral patterns II: observers, states, strategies, templates and visitors
87. U23.3 Concurrency: goroutines, channels, select, context, sync and the race detector
88. U23.4 Networked services: `net/http`, handlers and middleware, timeouts, retries, circuit breakers and graceful shutdown
89. U23.5 Database coding: a write-ahead-logged key-value store, crash recovery and the `database/sql` interface
90. U23.6 System-design building blocks in Go: rate limiters, consistent hashing, Bloom filters and caches
91. U23.7 Cloud-native Go: reconciliation loops, leases and fencing, backoff, a twelve-factor service and a container image
92. U12.1 Observability and site reliability engineering: metrics, logs, traces, SLOs and error budgets
93. U13.3 Capstone: a replicated, sharded key-value store with fault injection
94. U13.4 Capstone: an end-to-end data platform from your own engines
95. U13.5 Capstone: a small service on Google Cloud with identity, networking, reliability and cost controls
96. U23.8 Testing, benchmarking and profiling Go programs: table tests, fuzzing, the race detector, coverage, benchmarks and `pprof`
97. U16.6 Testability, fundamental and other patterns, anti-patterns, and the Python view
98. U24.1 Numbers, countability, functions, limits and continuity
99. U24.2 Differentiation and mean value theorems
100. U24.3 Integration, applications and transcendental functions
101. U24.4 Taylor expansion, sequences, series and power series
102. U24.5 Improper integrals, Gamma and Beta functions, integrals dependent on parameters
103. U24.6 Functions of several variables, partial derivatives and differentiability
104. U24.7 Taylor expansion in several variables, maxima, minima and Lagrange multipliers
105. U24.8 Multiple integrals and their applications
106. U19.1 Bridge: calculus, counting and matrices for statistics
107. U19.2 Introduction to data analytics and Python fundamentals: the analytics workflow, data types, descriptive statistics and visualisation
108. U24.9 Vector calculus: fields, line and surface integrals, Green, Gauss and Stokes
109. U24.10 Matrix calculus, Jacobians and Hessians for machine learning
110. U24.11 First- and higher-order ordinary differential equations
111. U24.12 Numerical analysis: iteration, root finding, interpolation and quadrature
112. U24.13 Complex variables: analytic functions and complex integration
113. U24.14 Series, singularities, residues, real integrals and conformal mapping
114. U24.15 Laplace, Z, Fourier and discrete Fourier transforms
115. U17.3 Divide and conquer: the master method, quicksort, randomised quicksort, half-majority, multiplication and inversions
116. U17.4 Heaps, sorting in linear time and order statistics
117. U17.5 Hashing: hash functions, open addressing and perfect hashing
118. U17.6 Abstract data types, stacks and queues, range queries and the grid-distance problem
119. U16.7 Object-oriented design exercises: hash map, LRU cache, call center, deck of cards, parking lot and chat
120. U16.8 How to approach a system design: the four steps, estimation, and the numbers every engineer carries
121. U17.7 Search trees: binary search trees, balancing and red-black trees
122. U17.8 Augmenting data structures, fixed-universe successor and the van Emde Boas tree, with the geometric primitives
123. U17.16 Tries, B-trees, skip lists and string matching: the lookup structures of routers, databases and search engines
124. U17.9 Disjoint sets, amortised analysis and more computational geometry
125. U24.16 Mathematical modelling: discrete and continuous dynamical systems
126. U24.17 ODE theory for dynamical systems: Gronwall, limit sets, invariant sets and chain transitivity
127. U26.1 What machine learning is: paradigms, data, hypothesis spaces and the statistical framework
128. U26.2 Model evaluation and selection: bias–variance, validation, tuning and metrics
129. U26.3 Linear regression and linear classification: estimation, logistic and softmax regression, surrogate losses
130. U19.8 Maximum likelihood, logistic regression and the ROC curve
131. U26.4 Regularization and implicit regularization
132. U26.5 Perceptron, support vector machines and kernel methods
133. U18.6 Linear regression and least squares: system identification, ridge regression, support vector machines and kernel SVMs
134. U18.7 Optimal linear MMSE estimation: the MMSE receiver, market prediction and forecasting, and ARMA models
135. U26.6 Bayes decision theory, density estimation and probabilistic classifiers
136. U26.7 Decision trees and ensembles: bagging, boosting, random forests
137. U26.8 Dimensionality reduction and feature learning
138. U18.4 Eigenvalue decomposition: properties, diagonalisation, the spectral theorem, PCA and eigenfaces
139. U18.5 Singular value decomposition and applications: beamforming in MIMO, dimensionality reduction, rate maximisation and the MUSIC algorithm
140. U26.9 Clustering, mixture models and the EM algorithm
141. U19.9 The chi-square test and cluster analysis: goodness of fit, independence, hierarchical and k-means clustering, density-based clustering and outlier detection
142. U19.10 Classification and regression trees (CART): impurity, splitting, overfitting and pruning
143. U26.10 Probabilistic graphical models, hidden Markov models, inference and Gaussian processes
144. U19.15 Markov chain Monte Carlo, Hamiltonian Monte Carlo, the brms package and Stan, taught in Python with PyMC and Bambi
145. U19.16 Bayesian regression and hierarchical models
146. U19.17 Model comparison, mixture models and multinomial processing trees
147. U19.32 Forecasting with statistical and machine-learning models: hydrology and water-resources applications
148. U26.11 Instance-based learning, collaborative filtering and recommendation
149. U18.8 Data analytics with matrices: recommender systems, user rating prediction, data completion and the Netflix problem
150. U18.24 Applications of linear algebra: PageRank, sparsity, dynamical systems, Markov chains, signal processing and data analytics
151. U18.9 The DFT and the FFT matrix, OFDM and SC-FDMA: structure, properties and signal processing in OFDM systems
152. U18.10 Dynamical systems: modelling robots and chemical plants, autonomous linear systems and systems with inputs and outputs
153. U18.11 Unsupervised learning: centroid-based clustering, probabilistic model-based clustering and the EM algorithm
154. U26.12 Data mining: preprocessing, association rules, sequence mining, outliers and case studies
155. U19.11 Data mining: introduction, data preprocessing, association rule mining and classification basics
156. U19.12 Classification: decision trees, the Bayes classifier, nearest neighbours, support vector machines and kernel machines
157. U19.13 Evaluation, visualisation, sequence mining and case studies
158. U19.14 Bayesian inference: Bayes' theorem, the likelihood, prior and posterior, analytical methods and grid approximation
159. U26.13 Learning theory: PAC, VC dimension, generalization and modern overparametrization
160. U3.1 Bridge: lookup data structures — tries, hashing and Bloom filters
161. U30.1 Probabilistic deep generative modelling: foundations and taxonomy
162. U30.2 Generative modelling via variational divergence minimization
163. U30.3 Generative adversarial networks: formulation, training, WGAN and applications
164. U30.4 Variational autoencoders, improvements and VQ-VAE
165. U30.5 Autoregressive models
166. U30.6 Energy-based and score-based models; Langevin sampling
167. U30.7 Denoising diffusion probabilistic models, conditional diffusion and Stable Diffusion
168. U30.8 Normalizing flows (gap-fill from the references)
169. U33.1 CNN computation and accelerators
170. U33.2 Parallelism for training, communication and fault tolerance
171. U33.3 LLM decoding, memory management and serving infrastructure
172. U16.9 Scalability and the front of the system: performance, throughput, DNS, CDN, load balancers, reverse proxies and the application layer
173. U16.10 Availability and consistency in practice: CAP choices, consistency patterns, fail-over, replication and the arithmetic of nines
174. U16.11 Scaling the data tier: replication, federation, sharding, denormalization, SQL tuning, and choosing between SQL and NoSQL
175. U16.12 Caching: layers, key choices, and the four update strategies
176. U16.13 Asynchronism, communication and security basics: queues, back pressure, HTTP, TCP and UDP, RPC and REST
177. U16.14 Worked designs I: a url shortener (Pastebin) and the Twitter timeline and search
178. U33.4 Model compression and quantization
179. U33.5 Graph neural network inference systems
180. U33.6 Federated learning
181. U4.1 Bridge: operating systems and computer architecture for virtualization
182. U27.1 From batch to online learning: adversarial full-information and bandit settings
183. U27.2 Stochastic bandits: regret notions, UCB, KL-UCB and lower bounds
184. U27.3 Contextual bandits and pure exploration
185. U27.4 Markov decision processes, dynamic programming and temporal-difference learning
186. U17.10 Greedy algorithms, dynamic programming, graphs and minimum spanning trees
187. U14.9 Memory hierarchy I: cache principles, replacement, write policies, design and optimisation
188. U14.10 Virtual memory: page tables, TLBs, protection and the hardware-software boundary
189. U14.11 Main memory: DRAM organisation, controllers, address mapping and scheduling
190. U14.12 Input-output system design: buses, interrupts, DMA and storage interfaces
191. U14.13 Parallel architectures and programming models: shared memory, message passing and data parallel
192. U14.14 Cache coherence: snooping, directory protocols, MSI, MESI, Dragon, split-transaction buses, Origin and NUMA-Q
193. U14.15 Memory consistency models and synchronisation primitives
194. U14.16 On-chip networks and interconnects: topologies, routing, flow control, router microarchitecture, deflection and bufferless routing
195. U17.11 Graph search: breadth-first and depth-first search, bipartiteness, DFS trees and articulation points
196. U11.10 Bridge: Markov chains, eigenvectors and PageRank
197. U15.19 Bridge: directed graphs, cycles, topological order and partial orders for schedules, deadlocks and timestamps
198. U17.12 Single-source shortest paths: Dijkstra, Bellman–Ford and their applications
199. U17.13 All-pairs shortest paths: Floyd–Warshall and Johnson
200. U11.11 Big data applications: graph processing
201. U17.14 Flow networks, the Ford–Fulkerson method, and an introduction to computational complexity
202. U17.17 Backtracking, branch and bound, exact exponential algorithms, approximation and local search: living with hard problems
203. U18.3 Introduction to matrices and applications: subspaces, rank, circuits, graphs, social networks and traffic flow
204. U2.7 Bridge: graph algorithms for routing — shortest paths, spanning trees and distributed relaxation
205. U2.8 Network layer: IP addressing, IPv6, NAT, DHCP and ICMP
206. U2.9 IP routing: intra-domain protocols and inter-domain routing with BGP
207. U2.10 IP services: ARP and SNMP
208. U2.11 Bridge: coding theory — GF(2), polynomial division, CRC and Hamming codes
209. U2.12 Data link layer: forwarding, flow control, error control, switching and spanning tree
210. U2.13 Media access control: channel access protocols and framing
211. U2.14 End-to-end principles of computer networks and the future Internet
212. U25.1 Optimization problems: formulation, history, transformations and basic facts
213. U25.2 Convex sets, cones, polyhedra and separation
214. U25.3 Convex functions and their calculus
215. U25.4 Unconstrained optimization theory
216. U25.5 Constrained optimization theory: Lagrange, cones, Fritz John and KKT
217. U20.1 Scalable data science: the problem, and the background of concentration inequalities, PCA and SVD, convex optimisation and gradient descent, and supervised learning
218. U20.2 Memory-efficient data structures I: hash functions, universal and perfect hash families, Bloom filters, sketches for distinct count and the Misra–Gries sketch
219. U25.6 Lagrangian duality, saddle points and minimax
220. U25.7 Linear programming: simplex, duality, sensitivity and interior-point methods
221. U25.8 Unconstrained descent methods: line search, gradient, Newton, quasi-Newton, conjugate gradient, trust region
222. U25.9 Constrained optimization algorithms: QP, projected and reduced gradient, penalty, augmented Lagrangian, SQP
223. U25.10 First-order methods for ML: stochastic, accelerated, proximal, adaptive, and the dynamical-systems view
224. U25.11 Conic and structured convex programs: QCQP, SOCP, SDP, geometric programs
225. U25.12 Applications of optimization: signal estimation, compressive sensing, radar, big data and finance
226. U25.13 Non-smooth and difference-of-convex optimization
227. U25.14 Distributed optimization: graphs, consensus, ADMM and dual decomposition
228. U25.15 Dynamic optimization and complementarity problems
229. U25.16 Stochastic approximation: algorithms, step sizes and the ODE method
230. U25.17 Convergence rates, stability, two-timescale algorithms and stochastic recursive inclusions
231. U27.5 Policy gradient, actor–critic and proximal policy optimization
232. U27.6 Stochastic approximation in reinforcement learning
233. U28.1 Perceptron, multilayer networks, activations and loss functions
234. U18.12 The linear perceptron, compressive sensing and orthogonal matching pursuit: sparse signal estimation
235. U18.13 Discrete-time Markov chains and operations research: supply chains, forecasting, and resource and inventory management
236. U28.2 Backpropagation and training deep networks
237. U14.17 GPU architecture: streaming multiprocessors, SIMT execution, warp scheduling and divergence, cache hierarchy, graphics pipeline
238. U14.18 GPU programming and optimisation: CUDA, thread mapping, synchronisation, coalescing, reductions, kernel fusion
239. U14.19 OpenCL and heterogeneous computing
240. U28.3 Overfitting, regularization and generalization in deep networks
241. U28.4 Convolutional neural networks and image representation
242. U14.20 Domain-specific accelerators and efficient neural-network training and inference
243. U14.21 Quality of service for caches and networks on chip, and emerging directions
244. U14.22 Low-power design, reliability and hardware security
245. U28.5 Explainable AI for deep models
246. U28.6 Segmentation and object detection
247. U28.7 Recurrent networks: RNN, LSTM, GRU, backpropagation through time and attention in RNNs
248. U28.8 Autoencoders and representation learning
249. U29.1 NLP foundations and the classical NLP pipeline
250. U29.2 Word representations and multilingual embeddings
251. U29.3 Attention and the Transformer architecture
252. U29.4 Pretraining, self-supervised learning and the LLM landscape
253. U29.5 Scaling laws, LLM architectures and long context
254. U29.6 Decoding strategies and sampling
255. U29.7 Prompting: fundamentals, APIs and advanced techniques
256. U29.8 Instruction tuning, RLHF and alignment: PPO and DPO
257. U29.9 Parameter-efficient fine-tuning: LoRA and QLoRA
258. U29.10 Prompt optimization, compression and prompt security
259. U3.2 Bridge: bipartite matching, Hall's theorem and Birkhoff–von Neumann decomposition
260. U3.3 High-performance switching and routing: router architecture, switch fabrics and performance
261. U3.4 IP address lookup: algorithms, optimisation and hardware implementation
262. U3.5 Packet classification
263. U31.1 Why RAG, RAG architecture and classical retrievers
264. U31.2 RAG failure modes, types of RAG and assessment
265. U31.3 Sparse retrieval limits and dense representations
266. U31.4 Learning retrieval-oriented embeddings and choosing an embedding model
267. U31.5 Document processing and chunking
268. U31.6 Vector databases and indexes: KNN, IVF, PQ, HNSW, FAISS and ChromaDB
269. U20.3 Count-Min and Count sketches, and approximate near-neighbour search: kd-trees, locality-sensitive hashing, MinHash for Jaccard and SimHash
270. U20.4 Approximate near neighbours: extensions (multi-probe, b-bit hashing, data-dependent variants) and random projection
271. U20.5 Randomised numerical linear algebra: CUR decomposition, sparse and subspace random projection and the kitchen-sink features
272. U20.6 MapReduce and related paradigms: programming examples (PageRank, k-means, matrix multiplication), moving computation to the data and the Hadoop ecosystem
273. U20.7 Scala and Spark, and distributed machine learning and optimisation: stochastic gradient descent with its proof
274. U20.8 Distributed optimisation with ADMM and its applications, distributed clustering and conclusion
275. U31.7 The retrieval pipeline: bi-encoder, cross-encoder, ColBERT and two-stage retrieval
276. U31.8 Production RAG: request shaping, query transformation, routing, security, cost and observability
277. U16.15 Worked designs II: a web crawler, Mint, a social graph, a key-value cache for a search engine, and sales ranking
278. U16.16 Scaling a system from one box to millions of users, real-world architectures, and the reading lists
279. U31.9 Limits of single-shot RAG and the move to agents
280. U31.10 Agent basics, tool calling and orchestration
281. U31.11 Planning with ReAct
282. U31.12 State machines and LangGraph
283. U31.13 Agentic memory
284. U31.14 Provenance and citations
285. U31.15 Multi-agent architecture summary, error handling and best practices
286. U32.1 LLM evaluation: metric architecture and reference-based metrics
287. U32.2 LLM-as-a-judge and factuality
288. U32.3 AI safety foundations and threat models
289. U32.4 White-box attacks and prompt injection
290. U32.5 Black-box attacks and the jailbreak taxonomy
291. U32.6 Defense, interpretability and ethics
292. U4.2 Virtualization: models, types and the Popek–Goldberg theorem
293. U4.3 Hotspot mitigation and live VM migration
294. U4.4 Containers, Docker, Linux containers, networking of VMs, Kubernetes and edge computing
295. U4.5 Bridge: network flows and linear programming
296. U3.6 DiffServ, quality of service, traffic policing and shaping
297. U3.7 Network softwarization: software-defined networking, controllers, southbound and northbound interfaces
298. U3.8 Network function virtualization: architecture and concepts
299. U3.9 Programmable networks: P4, SmartNICs and P4 switches
300. U3.10 Data center networking: topologies, routing, transport and container network interfaces
301. U3.11 Content distribution on the Internet and architectures for information-centric networking
302. U3.12 NDN content naming, routing, caching and security
303. U4.6 Network virtualization and geo-distributed clouds: SDN in the data center, VL2, NVP, MPLS, B4 and SWAN
304. U4.7 Google Cloud compute services: Compute Engine, App Engine, containers and Kubernetes, Cloud Functions
305. U4.8 Cloud networking on GCP: VPC networks, subnets, firewall rules, load balancing and hybrid connectivity
306. U6.1 Foundations of security and ethical hacking: CIA, threats, attack trees, ethics and rules of engagement
307. U6.2 Laboratory set-up and reconnaissance: attacker and victim machines, open-source intelligence, DNS and the nmap host-discovery stage
308. U6.3 Scanning and vulnerability assessment: port scanning, nmap and Nessus, CVE, CWE and CVSS, and the secure hacking environment
309. U6.4 System hacking, malware and link-layer attacks: passwords, privilege escalation, malware taxonomy and analysis, ARP spoofing and MAC attacks
310. U6.5 Network attacks and defences: sniffing, session attacks, denial of service, DNS and email security
311. U6.6 Steganography, biometric authentication and social engineering
312. U6.7 Web application attacks and secure coding: HTTP state, SQL injection, XSS, CSRF, authentication and access control
313. U6.8 Exploitation frameworks and memory safety: Metasploit as a lab tool, memory-corruption models, and mitigations
314. U6.9 Hardware security: side channels in hardware, physical unclonable functions and hardware trojans
315. U6.10 Case studies: attack scenarios, their root causes and remedies
316. U7.1 Defence technologies and access control: firewalls, intrusion detection, access-control models and active defence
317. U7.2 Knowing your attacker: the MITRE ATT&CK framework
318. U7.3 Cyber kill chains: the Lockheed Martin Cyber Kill Chain and the Unified Kill Chain
319. U7.4 Defending yourself: the MITRE D3FEND framework
320. U7.5 Securing your configurations: STIG benchmarking
321. U7.6 Sharing threat intelligence: STIX and TAXII
322. U7.7 Cloud security and identity: APIs, IAM, service accounts, keys and the shared-responsibility model
323. U8.1 Security posture, governance, risk and compliance and maturity
324. U8.2 Bridge: quantitative risk — frequency and severity models, Monte Carlo loss exceedance, Bayesian updating and decision under uncertainty
325. U13.6 Capstone: a security programme for a synthetic organisation
326. U13.7 Capstone: a multicore simulator (pipeline, caches, coherence and a NoC) running a parallel kernel
327. U13.8 Capstone: a small relational database engine checked against sqlite3
328. U13.9 Capstone: a design dossier and a working miniature of a large-scale service
329. U13.10 Capstone: an analytics pipeline from raw data to a decision, with the statistics, the model, the sketches and the distributed run built from scratch
330. U13.11 Capstone A: the mathematics of machine learning, end to end
331. U13.12 Capstone B: a classical-ML library from scratch
332. U13.13 Capstone C: a deep-learning framework from scratch
333. U13.14 Capstone D: an LLM application platform (RAG + agents + safety)
334. U13.15 Capstone E: generative models
335. U13.16 Capstone F: ML systems and efficiency
336. U13.17 Final integrated capstone: train, align, compress, serve, evaluate and secure a small language model
337. U5.1 Bridge: probability, entropy and asymptotics for cryptography
338. U5.12 Bridge: number theory for public-key cryptography — Fermat, Euler, CRT, quadratic residues, Legendre and Jacobi symbols, primality testing and factoring
339. U5.13 Key exchange, cyclic groups and the Diffie–Hellman family: discrete log, CDH, DDH and the attacks on them
340. U5.14 Public-key encryption I: RSA, Rabin and ElGamal, generalized ElGamal and their textbook attacks
341. U5.15 Elliptic curves: groups over the reals and finite fields, scalar multiplication, ECDH and the elliptic-curve discrete log
342. U5.16 Public-key encryption II: IND-CPA and IND-CCA security, the KEM–DEM paradigm and CCA-secure hybrid ciphers
343. U5.17 Digital signatures: RSA signatures, Schnorr, DSA and ECDSA, group and ring signatures, hash-based signatures
344. U5.18 Key management, certificates and PKI, TLS/SSL and PGP: the protocols that assemble the primitives
345. U5.19 Cryptanalysis I: attack models, time–memory trade-off, differential and linear cryptanalysis
346. U5.2 Bridge: integers modulo n — divisibility, gcd, extended Euclid, inverses and fast exponentiation
347. U5.20 Cryptanalysis II: attacks on stream ciphers and side-channel attacks
348. U5.21 Secret sharing and secure multiparty computation
349. U5.22 Broadcast, identity-based, attribute-based and functional encryption; bilinear pairings
350. U5.23 Homomorphic encryption: partially, somewhat and fully homomorphic schemes
351. U5.24 Zero-knowledge proofs and interactive protocols
352. U5.25 Quantum and post-quantum cryptography
353. U5.3 Introduction to cryptography and classical ciphers, cryptanalysis and perfect secrecy
354. U5.4 Block ciphers: design principles, SPN, Feistel networks, DES, Triple DES and modes of operation
355. U5.5 Bridge: groups, rings, fields, finite fields and linear algebra over them
356. U5.6 Stream ciphers: one-time pad, autokey, LFSRs, Berlekamp–Massey and modern stream ciphers
357. U5.7 The Advanced Encryption Standard (Rijndael)
358. U5.8 Bridge: computational complexity, one-way functions and the reduction method
359. U5.9 Provable security for symmetric encryption: computational security, PRGs, PRFs and CPA security
360. U5.10 Cryptographic hash functions: Merkle–Damgård, Davies–Meyer, SHA-2, SHA-3, birthday attacks and the random-oracle model
361. U5.11 Message authentication and authenticated encryption: MACs, HMAC, CBC-MAC, universal hashing and AEAD
362. U8.3 Cyber security risk management: identification, assessment, control and treatment
363. U8.4 Contingency planning and cyber crisis management: incident response, disaster recovery and business continuity
364. U8.5 Cyber resilience assessment
365. U8.6 Cyber security policy formulation
366. U8.7 Foundations of privacy: concepts, theories and measurement
367. U8.8 Anonymity and privacy-enhancing technologies: re-identification, k-anonymity, differential privacy and anonymous communication
368. U8.9 Privacy regulation: GDPR in Europe, privacy in India (DPDP, Aadhaar) and breach duties
369. U8.10 Information privacy: economics and strategy
370. U9.1 Bridge: models of distributed computation, partial orders and the DSim simulator
371. U15.1 Introduction to databases and information systems: concepts, architecture and users
372. U15.2 Entity-relationship and enhanced ER modelling: semantic database design
373. U15.3 Bridge: sets, relations, functions and first-order logic for the relational model, algebra and calculus
374. U22.1 Introduction to software engineering: the need, the challenges, the evolution of the development process, system software engineering and the problems of large-scale development
375. U22.2 Software development life cycle and the process models: waterfall, modified waterfall, prototyping, incremental, spiral and the others, compared
376. U22.3 Project planning: size metrics, function points, cost estimation with COCOMO and Putnam's model, and staffing patterns
377. U22.4 Scheduling, organisation structure, risk management, quality management and configuration management, including the Git object model and the merge algorithm
378. U22.5 Software requirements: gathering, analysis, the SRS and its characteristics, functional and non-functional requirements, and informal specification
379. U22.6 Formal requirement specification: notations, the axiomatic approach (pre- and postconditions, weakest precondition, invariants) and the algebraic approach (abstract data types)
380. U22.7 Software design: basics, characteristics of a good design, modularity, cohesion and coupling, layering and the approaches to design
381. U22.8 Function-oriented design: structured analysis and design, data flow diagrams, structure charts, HIPO, Jackson's technique and Warnier–Orr diagrams
382. U22.9 Object-oriented analysis and design: the concepts, the UML notation (use cases, class, interaction and state diagrams), the OOAD process, and function-oriented against object-oriented development
383. U22.10 Coding and testing I: coding standards, reviews and inspections, the Halstead measures, and unit, integration and system testing
384. U22.11 Testing II: black-box and white-box test-case design, coverage criteria, cyclomatic complexity and basis paths
385. U22.12 Testing III and debugging: mutation testing, regression, property-based testing, debugging strategies, delta debugging and fault localisation
386. U22.13 Software maintenance and its models, and an introduction to agile software development
387. U9.2 Bridge: tail bounds, balls into bins and randomised-algorithm analysis
388. U9.3 Epidemic and gossip-based algorithms
389. U9.4 Unstructured peer-to-peer systems: Napster, Gnutella, FastTrack and BitTorrent
390. U9.5 Distributed hash tables: Chord, Pastry and Kelips
391. U9.6 Time, clocks and causality: synchronisation, Lamport clocks and vector clocks
392. U9.7 Global state and termination detection: the Chandy–Lamport snapshot
393. U9.8 Distributed mutual exclusion: permission-based, quorum-based and token-based algorithms
394. U9.9 Distributed deadlock detection and distributed shared memory
395. U9.10 Leader election: rings, the bully algorithm and their industry use
396. U9.11 Distributed minimum spanning tree: the Gallager–Humblet–Spira algorithm
397. U9.12 Agreement and consensus, and the FLP impossibility result
398. U9.13 Byzantine agreement, reliability measures: SLIs, SLOs and SLAs
399. U9.14 Replicated state machines: Paxos and Raft
400. U9.15 Coordination services in industry: Google Chubby and Apache ZooKeeper
401. U9.16 Consistency models and the CAP theorem
402. U9.17 Bridge: transactions — ACID, serializability, locking, logging and recovery
403. U10.1 Bridge: the relational model, SQL, indexing and query processing
404. U12.2 Data analytics on Google Cloud: the warehouse, dataflow pipelines and managed clusters
405. U15.20 Transactions: OLTP, concurrency problems, the ACID properties and transaction states
406. U15.21 Schedules: conflict and view serializability, recoverability, cascading rollbacks and testing
407. U15.22 Concurrency control protocols: locking and two-phase locking, timestamps, multiversioning, multiple granularity and deadlocks
408. U15.23 Recovery systems: log-based schemes, deferred and immediate update, shadow paging and ARIES
409. U15.24 Database security and authorization: discretionary and mandatory control, multilevel security and statistical databases
410. U15.25 Enhanced data models: active, temporal, spatial and multimedia databases
411. U15.26 Distributed databases: fragmentation, replication, distributed query processing, concurrency and recovery
412. U15.27 NoSQL systems, graph databases and big data
413. U15.4 The relational model: relations, keys, integrity constraints, updates and the mapping from ER and EER
414. U15.5 Relational algebra: basic and additional operators, extended operators and updates
415. U15.6 Relational calculus: tuple and domain calculus, safety and Codd's theorem
416. U15.7 SQL I: data definition, basic query structure, basic operations, aggregation and grouping
417. U15.8 SQL II: nested subqueries and set operations, updates and joins
418. U15.9 SQL III: views, triggers, integrity constraints, specifying indexes, embedded SQL and a recap
419. U15.10 A commercial case study: IBM DB2, its architecture, data definition and manipulation
420. U15.11 Functional dependencies: keys, inference, closure, covers and the anomalies they cause
421. U15.12 Normal forms: 1NF, 2NF, 3NF and BCNF, lossless decomposition and dependency preservation
422. U15.13 Multivalued, join and inclusion dependencies: fourth and fifth normal forms and other dependencies
423. U15.14 Bridge: the external-memory model, disks and the cost of sorting
424. U10.2 Distributed file systems: the Google File System and HDFS, with erasure coding
425. U10.3 Amazon Dynamo and LinkedIn Voldemort: highly available key-value stores
426. U10.4 Apache Cassandra: a wide-column store on Dynamo's ring and Bigtable's engine
427. U10.5 HBase and Bigtable: sorted wide-column storage over a distributed file system
428. U10.6 In-memory key-value stores and the families of NoSQL databases
429. U10.7 Google Cloud storage and database options
430. U11.1 Introduction to big data
431. U11.2 Enabling technologies for big data: clusters, virtualisation, containers and orchestration
432. U11.3 Big data platforms I: Hadoop and the MapReduce model
433. U11.4 Big data platforms II: Apache Spark and resilient distributed datasets
434. U11.5 Dataflow systems beyond MapReduce: Condor and DryadLINQ
435. U11.6 Apache Kafka: the distributed commit log and messaging systems
436. U11.7 Stream processing and approximate algorithms: windows, event time and sketches
437. U11.8 Bridge: machine-learning foundations for scalable learning
438. U11.9 Big data applications: machine learning with Spark
439. U12.3 Machine learning on Google Cloud: managed training and prediction, pre-trained APIs and responsible AI
440. U15.15 Storage structures and physical design: devices, buffering, file organisation and hashing
441. U15.16 Indexing: primary, clustering, secondary and multilevel indexes, ISAM, B-trees and B+-trees
442. U15.17 Query processing: selection, sorting, projection and the join algorithms
443. U15.18 Query optimisation: equivalent expressions, join ordering, size estimation and semantic optimisation
444. U26.0 History of AI, symbolic AI and the machine-learning workflow
445. U26.14 Symbolic and knowledge-based machine learning, tools and cognitive-science influences
446. U9.18 Distributed transactions: atomic commit, Percolator and Spanner
447. U9.19 Failures and recovery: checkpointing, rollback recovery, fault tolerance and self-stabilization
448. U9.20 Message ordering, group communication and virtual synchrony
449. U9.21 Bitcoin and blockchains
450. U9.22 Security in distributed systems and sensor networks
