# Part 03 · Mathematics, Probability, Statistics, Queueing & Performance Modelling · TOPIC LIST

Rules and directives for this part: `index/part03_mathematics.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Mathematics, Probability, Statistics, Queueing & Performance Modelling

### Proof and discrete mathematics

- **Proof techniques**
  - Direct proof, contraposition, contradiction and cases; biconditional proofs as two implications, proving P ⇒ Q and Q ⇒ P; existence proofs by explicit construction versus a contradiction showing that no counterexample exists
  - Ordinary and strong induction; structural induction over lists and trees
  - The well-ordering principle
  - Invariants as the proof tool for algorithms
- **Logic and sets**
  - Propositions and connectives; implication, converse, inverse and contrapositive; logical equivalence and tautologies
  - Predicates and the quantifiers ∀ and ∃; negating quantified statements
  - Rules of inference: modus ponens, modus tollens, syllogism
  - Set-builder notation, subsets, power sets, Cartesian products; roster notation listing the elements of a finite set
- **Relations, functions and counting**
  - Equivalence relations and partitions; partial orders
  - Injections, surjections and bijections, and what they say about cardinality; composition of functions and the inverse f⁻¹, which exists exactly when f is a bijection and satisfies f⁻¹(f(x)) = x; countable sets such as the integers and the rationals, and Cantor's diagonal argument that the reals are uncountable; a sequence as a function from the natural numbers, with partial sums and the telescoping identity; the graph of f as the set of pairs (x, f(x)), and the graph of f⁻¹ as the reflection of that graph in the line y = x
  - The pigeonhole principle; the sum and product rules
  - Permutations, combinations, the binomial theorem, inclusion–exclusion; permutations with repetition n^k and combinations with repetition C(n + k − 1, k) counted by stars and bars; the general term C(n, r)·aⁿ⁻ʳbʳ of (a + b)ⁿ and the middle term(s), one when n is even and two when n is odd
  - Linear recurrences solved by the characteristic equation; first-order difference systems x_{k+1} = Ax_k with solution x_k = A^k x_0, the matrix form of a linear recurrence
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
- **Circular permutations**: (n − 1)! arrangements of n distinct objects around a circle, since rotations are identified; fixing one object to break the rotational symmetry; reflections identify further arrangements only for necklaces and bracelets
- **Multinomial theorem and expansion**: (x₁ + … + xₖ)ⁿ as a sum over compositions of n with coefficients n!/(n₁! … nₖ!); the coefficient as the number of ways to split n labelled items into k labelled groups; the count of terms C(n + k − 1, k − 1); extracting a single coefficient
- **Catalan numbers**: Cₙ = C(2n, n)/(n + 1) counting correct bracketings, binary trees with n internal nodes and lattice paths that never cross the diagonal; the recurrence Cₙ₊₁ = Σᵢ CᵢCₙ₋ᵢ; growth as 4ⁿ/(n^{3/2}√π)

### Probability

- **Foundations**
  - Sample spaces, events and the axioms; the Kolmogorov axioms: nonnegativity, P(Ω) = 1, and countable additivity for pairwise disjoint events
  - Joint and marginal probability; marginalizing a joint table
  - Conditional probability, independence and Bayes' theorem derived from the definition
  - Random variables, expectation, linearity of expectation (no independence needed), variance and covariance
  - Indicator variables
- **Distributions**
  - Probability mass, density and cumulative distribution functions
  - Bernoulli, binomial, geometric, Poisson, uniform, exponential and normal, with their means and variances
  - The memoryless property
  - Sampling from distributions; Monte Carlo estimation; survey sampling designs: stratified sampling with proportional allocation, whose variance is no larger than simple random sampling's, and cluster sampling, whose variance grows with the correlation inside each cluster
- **The birthday bound**
  - P(some collision) ≈ 1 − e^(−n(n−1)/2N); collisions become likely near n ≈ √N
  - Why a random 64-bit ID collides after about 2³² draws
- **Tail bounds and order statistics**
  - Markov, Chebyshev and Chernoff bounds; the union bound
  - The law of large numbers and the central limit theorem; convergence in probability (the weak law) versus almost sure convergence (the strong law), which is the stronger mode
  - The maximum of n samples: P(max ≤ t) = F(t)ⁿ; the k-th order statistic X₍ₖ₎ with P(X₍ₖ₎ ≤ t) = Σ from j = k to n of C(n, j)·F(t)ʲ·(1 − F(t))ⁿ⁻ʲ
  - Fan-out tails: a request waiting on 100 sub-requests, each slow with probability 1%, is slow with probability 1 − 0.99¹⁰⁰ ≈ 63%
  - Hedged requests: a second copy after the p95 delay makes the tail P(X > t)² for about 5% extra load; tied requests cancel the loser
  - Why averages hide tails, and why a p99 cannot be averaged across hosts
- **Balls into bins**
  - n requests at random onto n servers: maximum load Θ(log n / log log n)
  - The power of two choices: the less loaded of d ≥ 2 random servers drops the maximum load to ln ln n / ln d + O(1)
  - Why "least connections" over stale load reports herds, and why two random choices tolerate staleness
- **Stochastic processes**
  - Markov chains and stationary distributions; the transition matrix P, the stationary equation πP = π, and the n-step probabilities given by P^n, whose rows converge to the stationary law for an irreducible aperiodic chain
  - Poisson processes
- **Plausible reasoning and Cox's desiderata**: degrees of plausibility ordered qualitatively; Cox's desiderata of consistency and rationality forcing the sum and product rules up to a monotone reparametrization; probability as the unique consistent extension of deductive logic to uncertain propositions
- **Law of total probability**: P(B) = Σᵢ P(B | Aᵢ)P(Aᵢ) over a partition of the sample space; the continuous form with integration against a density; its role as the denominator of Bayes' theorem when conditioning on competing causes
- **Transformations of random variables**: the change-of-variable formula f_Y(y) = f_X(g⁻¹(y))·|d g⁻¹(y)/dy| for monotone maps; the CDF method for general maps; summing over branches for non-monotone maps; the Jacobian determinant for vector transformations
- **Log-normal and multinomial distributions**: a log-normal variable exp(X) with X normal, median e^μ and mean e^(μ + σ²/2), arising from multiplicative effects; the multinomial as n trials over k categories with probability n!/(∏ nᵢ!)·∏ pᵢ^nᵢ; negative covariance between category counts
- **Maximum-entropy distributions**: maximizing entropy under moment constraints with Lagrange multipliers, giving exponential-family densities; the uniform law with no constraint, the geometric law for a fixed mean on the non-negative integers, the normal for a fixed mean and variance, the exponential for a fixed mean on the positive reals; the maximum-entropy principle as the rule for choosing a prior or model consistent with known constraints and nothing more
- **Jeffreys and ignorance priors**: non-informative priors for parameters about which nothing is known; the Jeffreys prior proportional to the square root of the Fisher information, invariant under reparametrization; the flat prior for a location parameter and 1/σ for a scale parameter; a flat prior in one parametrization becoming informative in another
- **Paradoxes of probability (Borel–Kolmogorov)**: conditioning on an event of probability zero depends on the limiting sequence of events chosen, so the same conditioning event on a sphere yields different conditional densities in different coordinates; nonconglomerability and the marginalization paradox as related failures of naive conditioning
- **Rule of succession and exchangeable sequences**: a sequence is exchangeable when its joint law is invariant under permutation of its terms; de Finetti's representation as a mixture of independent and identically distributed sequences; Laplace's rule (k + 1)/(n + 2) after k successes in n trials under a uniform prior

### Statistics and experimental design

- **Estimation**
  - Estimators, bias and variance; maximum-likelihood estimation; Fisher information; consistency (θ̂ₙ → θ in probability as n grows) and asymptotic normality of the maximum-likelihood estimator; the mean squared error as bias² + variance, and the trade of added bias for lower variance
  - The sample mean, its standard error σ/√n, and confidence intervals; the median and mode as the other measures of central tendency, the median being the 0.5 quantile and the trimmed mean its outlier-resistant compromise
  - Bayesian inference: prior and posterior updates; the naive Bayes classifier, whose posterior P(y | x) ∝ P(y)·∏ᵢ P(xᵢ | y) assumes the features are independent given the class
  - The bootstrap and the jackknife; the parametric bootstrap, which resamples from a fitted distribution instead of the data, and the jackknife's leave-one-out estimate of bias
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
  - Causal DAGs and adjustment; propensity scores and inverse-propensity weighting; the backdoor criterion, under which a set Z of covariates adjusts for confounding when it blocks every backdoor path from treatment to outcome and contains no descendant of the treatment
  - Difference-in-differences; uplift modelling
- **Association between variables**: the correlation matrix; Pearson correlation for linear association versus Spearman rank correlation for monotone association and outlier resistance; Kendall tau from concordant and discordant pairs; correlation is not causation
- **Sufficiency and the factorization theorem**: a statistic T(X) is sufficient for θ when the conditional law of the data given T does not depend on θ; the factorization criterion f(x; θ) = g(T(x); θ)h(x); the sample mean of a normal sample as sufficient for its mean; a sufficient statistic loses no information about θ
- **Basu's theorem and complete sufficient statistics**: completeness, meaning E[g(T)] = 0 for all θ forces g(T) = 0 almost surely; a complete sufficient statistic is independent of every ancillary statistic; the sample mean and sample variance of a normal sample are independent
- **Exponential families and multiparameter models**: densities in the form exp(η(θ)·T(x) − A(θ))h(x); natural parameters, and the log-partition function A whose derivatives give the mean and variance of T; the normal, Bernoulli and Poisson as members; multiparameter maximum likelihood with the Fisher information matrix
- **Method of moments**: equating sample moments to population moments and solving for the parameters; consistency from the law of large numbers; the gamma distribution as a worked example; efficiency compared with maximum likelihood
- **Delta method**: the asymptotic normal law of g(θ̂) from a central limit theorem for θ̂ through a first-order Taylor expansion, with variance g′(θ)²σ²/n; variance-stabilizing transformations; the second-order case when g′(θ) = 0
- **Cramér–Rao bound**: Var(θ̂) ≥ 1/(n I(θ)) for unbiased estimators, from the Cauchy–Schwarz inequality applied to the score; efficient estimators attain it and the maximum-likelihood estimator attains it asymptotically; the Bernoulli mean as a worked case
- **Student's t and F distributions**: t as a standard normal divided by the square root of a chi-square over its degrees of freedom, with heavier tails at small n; F as a ratio of independent scaled chi-squares, governing variance ratios and F-tests
- **One-sample and two-sample t-tests**: t = (x̄ − μ₀)/(s/√n) with n − 1 degrees of freedom; Welch's test for unequal variances; paired differences; the assumptions of independence and an approximately normal sample mean
- **z-test**: z = (x̄ − μ₀)/(σ/√n) when σ is known or n is large; the two-proportion z-test for conversion rates, with a pooled variance under the null
- **Type I and Type II errors**: rejecting a true null with probability α, the significance level; failing to reject a false one with probability β; power 1 − β; the trade-off at a fixed sample size and the Neyman–Pearson lemma for the most powerful test at a given α
- **Analysis of variance (ANOVA)**: splitting the total sum of squares into between-group and within-group parts; the F ratio of mean squares under the null of equal means; one-way and two-way designs; post hoc comparisons with multiple-comparison correction
- **Mann–Whitney U test**: a rank test for two independent samples, where U counts the pairs in which one sample exceeds the other; the normal approximation for large samples with a tie correction; insensitive to outliers because only ranks enter
- **Wilcoxon signed-rank test**: paired differences ranked by absolute size, with the sum of ranks of positive differences as the statistic; its null distribution under symmetry about zero; corrections for ties and zero differences
- **Skewness and kurtosis**: standardized third and fourth central moments, skewness E[(X − μ)³]/σ³ and excess kurtosis E[(X − μ)⁴]/σ⁴ − 3; what they say about asymmetry and tail weight; sample estimates of them being unstable at small n
- **Nonparametric inference**: estimating a distribution without a parametric family; the empirical CDF Fₙ(x) = (1/n)Σ 1{Xᵢ ≤ x} and the Dvoretzky–Kiefer–Wolfowitz bound on its uniform error; kernel density estimation and the bias–variance trade-off in its bandwidth; permutation tests that shuffle group labels to build the null distribution of a statistic under exchangeability
- **Exploratory data analysis**: the five-number summary (minimum, Q1, median, Q3, maximum) drawn as a box plot, with the 1.5 × IQR fence (IQR = Q3 − Q1) for flagging outliers; residual plots against fitted values to check linearity and constant variance; quantile–quantile plots against a reference distribution to compare tail shapes

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

- Vectors, matrices, scalar multiplication, the transpose, dot and cross products, norms; the order m × n of a matrix and its types (square, diagonal, triangular, symmetric, identity); (AB)ᵀ = BᵀAᵀ and the adjoint identity ⟨Ax, y⟩ = ⟨x, Aᵀy⟩ for real matrices; permutation matrices P that reorder the rows of the identity, with PᵀP = I
- Matrix multiplication and its O(n³) naive cost; why it parallelizes
- Vector spaces, span, linear independence, basis and dimension
- Matrices as linear maps; rank and the rank–nullity theorem; composition of linear maps as the matrix product AB; a linear map fixed by the images of the basis vectors, which are the columns of its matrix; rotation matrices in three dimensions and unit quaternions q = (w, x, y, z) acting by v ↦ qvq̄
- Solving Ax = b by Gaussian elimination and LU factorization; Cramer's rule as determinant ratios xᵢ = det(Aᵢ)/det(A), where Aᵢ replaces column i with b, factorial in cost by cofactor expansion; row operations; determinants (ad − bc for 2 × 2) and invertibility; the n × n determinant by cofactor expansion along a row, with the 3 × 3 case a(ei − fh) − b(di − fg) + c(dh − eg) and the sum over permutations; the adjugate with A⁻¹ = adj(A)/det(A); row substitution, replacing one row by itself plus a multiple of another, which leaves the solution set and the determinant unchanged
- Orthogonality, projections, Gram–Schmidt and least squares (the normal equations AᵀAx = Aᵀb)
- Eigenvalues and eigenvectors; power iteration; Hotelling deflation A − λ₁v₁v₁ᵀ, which removes a found eigenpair of a symmetric matrix so that power iteration finds the next
- The singular value decomposition, principal component analysis and low-rank approximation
- Distance and similarity: Euclidean, Manhattan, cosine
- Column space and null space; the Moore–Penrose pseudo-inverse for over- and under-determined systems; hyperplanes and the distance of a point to a hyperplane; the four fundamental subspaces (column space, null space, row space and left null space) with dimensions r, n − r, r and m − r for a rank-r matrix of size m × n
- **Symmetric and skew-symmetric matrices**: real symmetric matrices have real eigenvalues and orthogonal eigenvectors by the spectral theorem; skew-symmetric matrices have purely imaginary eigenvalues; every square matrix splits uniquely into ½(A + Aᵀ) plus ½(A − Aᵀ)
- **Positive definite matrices and minima**: xᵀAx > 0 for every nonzero x, equivalently positive eigenvalues, positive pivots or a Cholesky factorization; the quadratic ½xᵀAx − bᵀx minimized where Ax = b; a positive definite Hessian as the second-order test for a strict minimum
- **Complex matrices and similarity transformations**: the conjugate transpose, Hermitian and unitary matrices; similar matrices B = P⁻¹AP share eigenvalues and the characteristic polynomial; diagonalizability as similarity to a diagonal matrix; powers A^k = P D^k P⁻¹ computed from the diagonal form D = P⁻¹AP
- **Jordan form and Lyapunov stability**: Jordan blocks as the canonical form of defective matrices, built from generalized eigenvectors; the system x′ = Ax is asymptotically stable exactly when every eigenvalue has negative real part, and the Lyapunov equation AᵀP + PA = −Q certifies it; the matrix exponential e^(At) = Σ (At)^k / k! as the solution of x′ = Ax, computed from the Jordan form
- **QR factorization and the QR algorithm**: A = QR with orthogonal Q and upper-triangular R, computed by Gram–Schmidt, Householder reflections or Givens rotations; least squares by solving Rx = Qᵀb without forming AᵀA; the QR algorithm iterating QR factorizations, with shifts, to reveal eigenvalues
- **Sparse and structured matrix problems**: compressed storage of nonzeros; fill-in during elimination and reordering to limit it; banded, triangular, Toeplitz and circulant structure giving fast solves; iterative methods preferred for large sparse systems

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
  - Convex sets and functions; every local minimum of a convex function is global; the separating hyperplane theorem, under which disjoint convex sets are split by a hyperplane aᵀx ≤ b on one side and aᵀx ≥ b on the other; the dual cone K* = {y : yᵀx ≥ 0 for all x in K}; quasiconvex functions, whose sublevel sets are convex; the conjugate f*(y) = sup over x of (yᵀx − f(x))
  - Gradient descent and its convergence rates; stochastic gradient descent
  - Momentum and adaptive optimizers
  - Regularization (L1, L2); coordinate descent
  - Constrained optimization: Lagrange multipliers and KKT conditions; the Lagrangian dual function g(λ) = inf over x of L(x, λ) for λ ≥ 0, weak duality g(λ) ≤ f(x*), and strong duality under Slater's condition
  - Linear programming; the assignment problem and the Hungarian method; quadratic programming, minimizing ½xᵀQx + cᵀx subject to linear constraints with Q positive semidefinite; geometric programming with posynomial objectives, which become convex under the substitution x = e^y
  - Generalization versus optimization; approximation error
- **Newton's method**: the step x ← x − H⁻¹∇f(x) from the second-order Taylor model; quadratic convergence near a minimum with a positive definite Hessian; O(n³) per step to solve the Hessian system; quasi-Newton updates (BFGS) that build the Hessian from gradient differences; with equality constraints Ax = b, the Newton step from the KKT block system whose matrix has H and Aᵀ in the first block row and A and 0 in the second
- **Conjugate gradient**: solving Ax = b for symmetric positive definite A with A-conjugate search directions in a Krylov subspace; termination in at most n steps in exact arithmetic; convergence governed by the square root of the condition number; preconditioning; the Krylov subspace K_k(A, b) = span{b, Ab, …, A^(k−1)b}, from which the k-th iterate is drawn and in which it minimizes the error in the A-norm
- **Proximal methods**: minimizing f(x) + g(x) with a nonsmooth g through the proximal operator prox_g(v) = argmin over x of g(x) + ½‖x − v‖²; proximal gradient iterations; soft-thresholding as the proximal operator of the L1 norm
- **Robust and stochastic formulations**: the min–max robust problem min over x of the maximum over an uncertainty set of f(x, u); the stochastic program min over x of E[f(x, ξ)] solved by sample average approximation; chance constraints; the trade-off between conservatism and expected performance
- **Non-convex diagnostics**: the gradient norm and the Hessian's eigenvalues at a stationary point to separate local minima, saddle points and maxima; restarts and sensitivity to initialization as the test of a local answer; a local minimum is not certified global
- **Interior-point methods**: inequality constraints handled by the log barrier −(1/t)Σ log(−fᵢ(x)); Newton steps on each centering problem as t grows along the central path; polynomial-time bounds for linear and self-concordant convex programs
- **Geometric problems (minimum-volume ellipsoids)**: the smallest-volume ellipsoid enclosing a point set as a convex problem in the ellipsoid's matrix and centre, with the negative log-determinant as the objective; the Löwner–John ellipsoid as its theory
- **Pontryagin maximum principle**: a necessary condition for optimal control; the Hamiltonian H = p·f + L with costate p obeying the adjoint equation, and H maximized pointwise over admissible controls; bang-bang controls in time-optimal problems

### Numerical computing

- Floating point: IEEE 754, rounding, decimal versus binary
- Catastrophic cancellation; compensated (Kahan) summation
- Overflow and underflow; stable reformulations: `log1p`, log-sum-exp, stable softmax
- Conditioning and the stability of algorithms; iterative solvers; the condition number κ(A) = ‖A‖·‖A⁻¹‖ built from induced matrix norms, with the spectral norm ‖A‖₂ equal to the largest singular value, bounding how a relative change in b is amplified into a relative change in x
- Numerical differentiation (finite differences, gradient checking) and integration
- Interpolation and curve fitting; error propagation; ℓ1 and Chebyshev (minimax) fitting, where the ℓ1 fit is a linear program and the minimax fit equioscillates between its extreme errors; root finding by bisection on a sign change and by Newton's iteration x_{k+1} = x_k − f(x_k)/f′(x_k), which converges quadratically to a simple root
- Reproducibility: seeding pseudo-random generators, deterministic tests
- **Projection methods and successive approximation**: fixed-point iteration x_{k+1} = T(x_k) and the contraction mapping theorem, with geometric convergence at the rate of the contraction constant; alternating projections onto convex sets; stopping on residuals rather than on iteration count

### Information theory

- Entropy H(X) = −Σ p·log₂ p
- Cross-entropy, KL divergence and mutual information; Gibbs' inequality D(p‖q) ≥ 0 with equality only when p = q, and the data-processing inequality, under which a Markov chain X → Y → Z satisfies I(X; Z) ≤ I(X; Y)
- Log loss, perplexity and calibration
- Shannon's source-coding bound; Huffman codes within one bit per symbol of it; the Kraft inequality Σ 2^(−ℓᵢ) ≤ 1 as the condition on codeword lengths ℓᵢ for a prefix code to exist
- Why compressed or well-encrypted data looks uniformly random
- Channel capacity; the binary symmetric channel with crossover probability p, whose capacity is 1 − H(p) bits per use, and capacity as the maximum of I(X; Y) over input distributions
- **Differential entropy and the Gaussian channel**: h(X) = −∫ f log f for densities, which can be negative and shifts by log|Jacobian| under a change of variables; the Gaussian as the maximum-entropy density for a fixed variance; the capacity C = ½ log(1 + P/N) of the additive Gaussian noise channel
- **Asymptotic equipartition property**: −(1/n) log p(X₁…Xₙ) → H(X) in probability for i.i.d. sources; the typical set of about 2^(nH) sequences carrying almost all probability; the consequence that about nH bits suffice for lossless coding
- **Rate distortion theory**: R(D) = min I(X; X̂) over test channels whose expected distortion is at most D; the Gaussian source with R(D) = ½ log(σ²/D) for D ≤ σ²; the rate–fidelity trade-off in lossy compression
- **Entropy rates of stochastic processes**: H = lim (1/n) H(X₁…Xₙ) for stationary processes, equal to the limit of H(Xₙ | Xₙ₋₁…X₁); the entropy rate of a stationary Markov chain as the stationary-weighted entropy of its transition rows
- **Network information theory**: multi-user sources and channels; the multiple-access channel capacity region; the broadcast channel; the Slepian–Wolf region for distributed lossless compression with rates H(X|Y), H(Y|X) and H(X, Y)
- **Sparse graph codes (LDPC)**: linear codes defined by a sparse parity-check matrix whose Tanner graph is bipartite; belief-propagation decoding by message passing; the threshold near Shannon capacity under density evolution for irregular degree distributions

### Signals and sequences

- Sampling and aliasing
- Convolution and correlation in one and two dimensions; separable kernels applied as two one-dimensional passes, costing 2k multiplications per pixel instead of k²
- The discrete Fourier transform and the FFT; windowing and the short-time Fourier transform
- Spectrograms and MFCC features; image representation; pre-emphasis y[n] = x[n] − αx[n−1] and framing into short overlapping windows before the spectrum; formants as peaks of the spectral envelope, and the mel filterbank followed by a DCT that yields MFCCs
- Image filters: Sobel edges and morphology; Canny edges from Gaussian smoothing, gradient magnitude and orientation, non-maximum suppression along the gradient and hysteresis thresholds; erosion and dilation as the minimum and maximum over a structuring element, with opening and closing built from them; denoising by Gaussian and median filters, sharpening by unsharp masking, and Fourier filtering by multiplying the 2-D DFT by a transfer function
- Sequence probability: n-gram models and perplexity; finite-state tokenizers

### Decision mathematics

- Markov decision processes
- Multi-armed and contextual bandits: epsilon-greedy, UCB, Thompson sampling; the linear contextual bandit with expected reward θᵀx and LinUCB's ridge-regression confidence bound
- **Decision theory (expected loss, Bayes decision rule)**: a loss L(θ, a) and risk R(θ, δ) = E[L(θ, δ(X))]; Bayes risk averaged over a prior; the Bayes decision rule choosing the action of least posterior expected loss; the posterior mean for squared-error loss, the posterior median for absolute loss and the MAP estimate for 0–1 loss

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
- From scratch: one-sample and two-sample t-tests, a z-test, a Mann–Whitney U test and a Wilcoxon signed-rank test, each run on simulated null data to measure its Type I error rate against the nominal significance level
- From scratch: QR least squares, conjugate gradient and Newton solvers compared on ill-conditioned systems such as Hilbert matrices, with residuals and iteration counts reported against the condition number
- From scratch: a rate-distortion or AEP experiment on i.i.d. Bernoulli sequences, measuring how the typical set's size and probability change with block length and comparing the per-symbol size with H
- **Reasoning drills**
  - Counting, probability and inequality problems, each solved two ways and checked by simulation
  - Derive the M/M/1 knee, then predict a service's latency at 50%, 90% and 99% utilization before load-testing it
  - Find the factor a Fermi estimate is most sensitive to and estimate it two independent ways
  - Construct a counterexample to each common misreading of a p-value
  - Derive the Cramér–Rao bound for a Bernoulli mean, then simulate the sample mean's variance and check that it sits at or above the bound
