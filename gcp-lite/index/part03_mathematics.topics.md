# Part 03 · Mathematics, Probability, Statistics, Queueing & Performance Modelling · TOPIC LIST

Rules and directives for this part: `index/part03_mathematics.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Mathematics, Probability, Statistics, Queueing & Performance Modelling

### Proof and discrete mathematics

- **Proof techniques**
  - Direct proof, contraposition, contradiction and cases
  - Ordinary and strong induction; structural induction over lists and trees
  - The well-ordering principle
  - Invariants as the proof tool for algorithms
- **Logic and sets**
  - Propositions and connectives; implication, converse, inverse and contrapositive; logical equivalence and tautologies
  - Predicates and the quantifiers ∀ and ∃; negating quantified statements
  - Rules of inference: modus ponens, modus tollens, syllogism
  - Set-builder notation, subsets, power sets, Cartesian products
- **Relations, functions and counting**
  - Equivalence relations and partitions; partial orders
  - Injections, surjections and bijections, and what they say about cardinality
  - The pigeonhole principle; the sum and product rules
  - Permutations, combinations, the binomial theorem, inclusion–exclusion
  - Linear recurrences solved by the characteristic equation
- **Number theory for cryptography**
  - Divisibility; gcd and the Euclidean algorithm with its O(log n) step bound
  - Bézout's identity and the extended Euclidean algorithm
  - Modular arithmetic and modular inverses
  - Primes and the fundamental theorem of arithmetic
  - Fermat's little theorem and Euler's theorem; the Chinese remainder theorem
  - Fast modular exponentiation by repeated squaring
  - The correctness proof of RSA; the discrete-logarithm problem
- **Graph theory**
  - Vertices, edges and degrees; the handshake lemma
  - Paths, cycles and connectivity
  - Trees: n − 1 edges and a unique path between any two vertices
  - Bipartite graphs and 2-colouring
  - Directed acyclic graphs and topological order
  - Euler tours

### Probability

- **Foundations**
  - Sample spaces, events and the axioms
  - Joint and marginal probability; marginalizing a joint table
  - Conditional probability, independence and Bayes' theorem derived from the definition
  - Random variables, expectation, linearity of expectation (no independence needed), variance and covariance
  - Indicator variables
- **Distributions**
  - Probability mass, density and cumulative distribution functions
  - Bernoulli, binomial, geometric, Poisson, uniform, exponential and normal, with their means and variances
  - The memoryless property
  - Sampling from distributions; Monte Carlo estimation
- **The birthday bound**
  - P(some collision) ≈ 1 − e^(−n(n−1)/2N); collisions become likely near n ≈ √N
  - Why a random 64-bit ID collides after about 2³² draws
- **Tail bounds and order statistics**
  - Markov, Chebyshev and Chernoff bounds; the union bound
  - The law of large numbers and the central limit theorem
  - The maximum of n samples: P(max ≤ t) = F(t)ⁿ
  - Fan-out tails: a request waiting on 100 sub-requests, each slow with probability 1%, is slow with probability 1 − 0.99¹⁰⁰ ≈ 63%
  - Hedged requests: a second copy after the p95 delay makes the tail P(X > t)² for about 5% extra load; tied requests cancel the loser
  - Why averages hide tails, and why a p99 cannot be averaged across hosts
- **Balls into bins**
  - n requests at random onto n servers: maximum load Θ(log n / log log n)
  - The power of two choices: the less loaded of d ≥ 2 random servers drops the maximum load to ln ln n / ln d + O(1)
  - Why "least connections" over stale load reports herds, and why two random choices tolerate staleness
- **Stochastic processes**
  - Markov chains and stationary distributions
  - Poisson processes

### Statistics and experimental design

- **Estimation**
  - Estimators, bias and variance; maximum-likelihood estimation; Fisher information
  - The sample mean, its standard error σ/√n, and confidence intervals
  - Bayesian inference: prior and posterior updates
  - The bootstrap and the jackknife
- **Hypothesis testing**
  - Hypothesis tests, p-values and their common misreadings
  - Power and sample size; the sample size of an A/B test
  - Multiple testing and the false discovery rate
  - Sequential testing and the peeking problem; CUPED variance reduction
- **Quantiles**
  - Estimating quantiles from histograms
  - Why per-host p99 values do not average to the fleet p99
- **Correlation and causation**
  - Confounders
  - Causal DAGs and adjustment; propensity scores and inverse-propensity weighting
  - Difference-in-differences; uplift modelling

### Queueing and performance modelling

- **Operational laws** (no distributional assumption)
  - The utilization law U = X·S
  - The forced-flow law Xₖ = Vₖ·X
  - Little's law L = λW, with its sample-path proof
  - The bottleneck law: maximum throughput is 1 / max(Vₖ·Sₖ)
  - The interactive response-time law for closed systems: R = N/X − Z
- **Queueing models**
  - Arrival and service processes
  - M/M/1 from its birth–death chain: πₙ = (1 − ρ)ρⁿ, mean number in system ρ/(1 − ρ), mean time 1/(μ − λ)
  - The knee: 2 service times at ρ = 0.5, 10 at 0.9, 100 at 0.99; utilization ceilings of 70–80% in capacity planning
  - M/M/k and the Erlang C formula; why one shared queue for k servers beats k separate queues
  - M/G/1 and the Pollaczek–Khinchine formula, E[W_q] = ρ·E[S]·(1 + C²)/(2(1 − ρ)); why service-time variability costs as much as load
- **Estimation as a method**
  - Fermi estimation: decompose, estimate each factor within a factor of 3, multiply
  - Sensitivity: the widest-ranging factor dominates; estimate it two ways
  - Capacity planning and back-of-the-envelope arithmetic in design work

### Linear algebra

- Vectors, matrices, scalar multiplication, the transpose, dot and cross products, norms
- Matrix multiplication and its O(n³) naive cost; why it parallelizes
- Vector spaces, span, linear independence, basis and dimension
- Matrices as linear maps; rank and the rank–nullity theorem
- Solving Ax = b by Gaussian elimination and LU factorization; row operations; determinants (ad − bc for 2 × 2) and invertibility
- Orthogonality, projections, Gram–Schmidt and least squares (the normal equations AᵀAx = Aᵀb)
- Eigenvalues and eigenvectors; power iteration
- The singular value decomposition, principal component analysis and low-rank approximation
- Distance and similarity: Euclidean, Manhattan, cosine

### Calculus and optimization

- **Single-variable calculus**
  - Limits and continuity; the derivative as a limit
  - Product, quotient and chain rules
  - The first-order Taylor approximation, and why a small gradient step decreases a smooth function
  - The integral as accumulated area; probability densities
  - First-order differential equations; Euler and Runge–Kutta (RK4) methods
- **Multivariable and matrix calculus**
  - Partial derivatives and the gradient
  - Gradients of vector functions, Jacobians, the matrix chain rule
  - The Hessian
- **Optimization**
  - Convex sets and functions; every local minimum of a convex function is global
  - Gradient descent and its convergence rates; stochastic gradient descent
  - Momentum and adaptive optimizers
  - Regularization (L1, L2); coordinate descent
  - Constrained optimization: Lagrange multipliers and KKT conditions
  - Linear programming; the assignment problem and the Hungarian method
  - Generalization versus optimization; approximation error

### Numerical computing

- Floating point: IEEE 754, rounding, decimal versus binary
- Catastrophic cancellation; compensated (Kahan) summation
- Overflow and underflow; stable reformulations: `log1p`, log-sum-exp, stable softmax
- Conditioning and the stability of algorithms; iterative solvers
- Numerical differentiation (finite differences, gradient checking) and integration
- Interpolation and curve fitting; error propagation
- Reproducibility: seeding pseudo-random generators, deterministic tests

### Information theory

- Entropy H(X) = −Σ p·log₂ p
- Cross-entropy, KL divergence and mutual information
- Log loss, perplexity and calibration
- Shannon's source-coding bound; Huffman codes within one bit per symbol of it
- Why compressed or well-encrypted data looks uniformly random
- Channel capacity

### Signals and sequences

- Sampling and aliasing
- Convolution and correlation in one and two dimensions
- The discrete Fourier transform and the FFT; windowing and the short-time Fourier transform
- Spectrograms and MFCC features; image representation
- Image filters: Sobel edges and morphology
- Sequence probability: n-gram models and perplexity; finite-state tokenizers

### Decision mathematics

- Markov decision processes
- Multi-armed and contextual bandits: epsilon-greedy, UCB, Thompson sampling

### Exercises

- From scratch: matrix multiplication as three nested loops, checked against NumPy
- From scratch: a vector and matrix package in Go: Gaussian elimination, determinants, transposes, cosine similarity, Gram–Schmidt, power iteration, PCA projection, brute-force nearest neighbours
- From scratch: a gradient-descent minimizer in one and then two variables; SGD with L1 and L2 penalties; coordinate descent
- From scratch: softmax with a temperature and sampling from it; a softmax and one gradient step by hand
- From scratch: finite-difference gradient checks, logistic-regression training, numerical integration, Euler and RK4 solvers, learning-rate experiments
- From scratch: samplers, Monte Carlo estimates, a naive Bayes classifier and hash-collision simulations against the birthday bound
- From scratch: metric aggregators, maximum-likelihood estimators, bootstrap intervals, Bayesian updates and an experiment analyser over event logs
- From scratch: the Hungarian method and min-cost assignment for scheduling; constrained ranking
- From scratch: cross-entropy, calibration bins, entropy-based splits and a perplexity calculator
- From scratch: DAG adjustment checks, inverse-propensity weighting, uplift metrics, and epsilon-greedy, UCB and Thompson bandits
- From scratch: stable maths helpers (log-sum-exp), reproducible train and test splits, interpolation and curve fitting, naive-versus-optimized loop benchmarks
- From scratch: one- and two-dimensional convolution, a small DFT, a spectral-feature extractor, Sobel and morphology filters
- From scratch: a truth-table generator and tautology checker for propositional formulas
- Base, unit, rate, latency and cost calculators
- **Reasoning drills**
  - Counting, probability and inequality problems, each solved two ways and checked by simulation
  - Derive the M/M/1 knee, then predict a service's latency at 50%, 90% and 99% utilization before load-testing it
  - Find the factor a Fermi estimate is most sensitive to and estimate it two independent ways
  - Construct a counterexample to each common misreading of a p-value
