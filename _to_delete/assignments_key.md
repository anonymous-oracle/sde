# Assignment answer keys

**Do not open a key before you have submitted an attempt** (Master Rules 6.11: the key is shown only after an attempt). A wrong answer gets one smaller, reworded retry of the same kind, not a new assignment (Master Rules 6.5).

Numerical answers were computed by script from the stated expression; the tolerance is the accepted absolute error.


---

# D1. Discrete Mathematics and Mathematical Reasoning

## A1.1. Logic, proof paradigms and formal languages

- **Q1:** B. Either p implies q or q implies p in every row; the others fail for some assignment.
- **Q2:** ABD. The converse q -> p is not equivalent; the other three are the standard equivalent forms.
- **Q3:** 256 functions (tolerance ±0). Each of the 8 input rows independently takes value 0 or 1, so 2^8.
- **Q4 (marking outline):** Base n=1; assume for n; add n+1 to both sides and factor to (n+1)(n+2)/2.
- **Q5 (what a passing submission shows):** 64 rows enumerated; all stated tests pass; the DFA has two states.

## A1.2. Counting, generating functions and combinatorics

- **Q1:** C. 6!/(3! 2!) = 60.
- **Q2:** ABC. D omits the (n-k)! in the denominator.
- **Q3:** 44 permutations (tolerance ±0). Inclusion-exclusion: 5! (1 - 1 + 1/2 - 1/6 + 1/24 - 1/120) = 44.
- **Q4 (marking outline):** Set x=y=1 in (x+y)^n; each subset of an n-set corresponds to its indicator string of length n.
- **Q5 (what a passing submission shows):** 49 ways by generating-function product and by brute force.

## A1.3. Posets, lattices, Boolean algebra and switching circuits

- **Q1:** B. Antichain means pairwise incomparable.
- **Q2:** ABD. x x' = 0, so C is false.
- **Q3:** 8 cells (tolerance ±0). A single literal fixes one variable, leaving 3 free: 2^3 cells.
- **Q4 (marking outline):** Show (x+y)+x'y' = 1 and (x+y)x'y' = 0 by distributivity; uniqueness gives the result.
- **Q5 (what a passing submission shows):** Six: 00-, 0-0, -01, 1-1, 11-, -10.

## A1.4. Graph theory

- **Q1:** C. Euler: V - E + F = 2 gives F = 5.
- **Q2:** ABC. An Euler circuit needs all degrees even.
- **Q3:** 28 edges (tolerance ±0). C(8,2) = 28.
- **Q4 (marking outline):** Each edge contributes 2 to the degree sum; an even sum forces an even count of odd terms.
- **Q5 (what a passing submission shows):** C5 False, C6 True, K3,3 True; K4 False, C6 True.

## A1.5. Number theory and cryptography

- **Q1:** C. 3^6 = 1 mod 7 and 100 = 4 mod 6, so 3^4 = 81 = 4 mod 7.
- **Q2:** ABD. phi(n) = n - 1 only for prime n.
- **Q3:** 12 (tolerance ±0). Count integers up to 36 coprime to 36: 12.
- **Q4 (marking outline):** a, 2a, ..., (p-1)a is a permutation of 1..p-1 mod p; equate the products and cancel (p-1)!.
- **Q5 (what a passing submission shows):** modinv(3,11)=4; 561 (a Carmichael number) is rejected; RSA round trip succeeds.

## A1.6. Algebra: finite fields, codes, groups and orbit counting

- **Q1:** D. Lagrange: the subgroup order must divide 12; only 6 does.
- **Q2:** ACD. Finite field orders are prime powers, so 6 is impossible.
- **Q3:** 6 necklaces (tolerance ±0). Rotations fix 16, 2, 4, 2 colourings; the average is 6.
- **Q4 (marking outline):** The map gStab -> g.x is a bijection from left cosets of the stabilizer to the orbit.
- **Q5 (what a passing submission shows):** gf8_mul(3,5)=4 and 16 x 7 = 112 single-bit errors are all corrected.

## A1.7. An invitation to mathematics: polynomials, functions, matrices, conservation laws

- **Q1:** B. The Vandermonde system is nonsingular for distinct nodes.
- **Q2:** ABD. Continuity does not imply differentiability.
- **Q3:** 6 (tolerance ±0). Product over pairs of (xj - xi) = 1*3*2 = 6.
- **Q4 (marking outline):** g(0) >= 0 and g(1) <= 0; IVT gives a zero of g.
- **Q5 (what a passing submission shows):** Error first falls then grows near the ends (Runge); condition number grows exponentially with n.


---

# D2. Single-Variable Calculus and Real Analysis

## A2.1. Numbers, countability, functions, limits and continuity

- **Q1:** C. Cantor's diagonal argument; the others are countable.
- **Q2:** ABD. Bounded sequences such as (-1)^n need not converge.
- **Q3:** 0.02 (tolerance ±0.001). abs(f(x) - 7) = 3 abs(x - 2) < 0.06 iff abs(x - 2) < 0.02.
- **Q4 (marking outline):** Assume a list of decimal expansions; build a number differing from the nth in the nth digit (avoiding 0 and 9 runs); it is missing from the list.
- **Q5 (what a passing submission shows):** About 2 for Newton and about 1 for bisection.

## A2.2. Differentiation and mean value theorems

- **Q1:** B. x1 = 1 - (1 - 2)/2 = 1.5.
- **Q2:** ABD. f(x)=x^3 has f'(0)=0 without an extremum.
- **Q3:** 1.417 (tolerance ±0.0001). x2 = 1.5 - 0.25/3 = 1.41667.
- **Q4 (marking outline):** g(a)=g(b)=0, so g'(c)=0 which rearranges to the MVT.
- **Q5 (what a passing submission shows):** Newton about 4-5, secant about 6, bisection about 34 iterations for 1e-10.

## A2.3. Integration, applications and transcendental functions

- **Q1:** A. Integrate by parts: [x e^x - e^x] from 0 to 1 = 0 - (-1) = 1.
- **Q2:** ABC. e^(-x^2) is continuous with no elementary antiderivative.
- **Q3:** 0.3438 (tolerance ±0.0001). h/2 (f0 + 2 f1 + 2 f2 + 2 f3 + f4) = 0.34375.
- **Q4 (marking outline):** G(x)=integral from a to x of f has G'=f; F-G is constant; evaluate at a and b.
- **Q5 (what a passing submission shows):** Ratios near 4 and 16.

## A2.4. Taylor expansion, sequences, series and power series

- **Q1:** D. The ratio of consecutive terms tends to 0 for every x.
- **Q2:** ACD. The harmonic series diverges; the alternating harmonic series converges conditionally.
- **Q3:** 1.646 (tolerance ±0.0001). 1 + 0.5 + 0.125 + 0.0208333 = 1.64583.
- **Q4 (marking outline):** Pick r with L<r<1; eventually abs(a_{n+1}) <= r abs(a_n), so terms are dominated by a geometric series.
- **Q5 (what a passing submission shows):** Degree 9 (error about 2.8e-6 for degree 7, below 1e-6 at degree 9).

## A2.5. Improper integrals, Gamma and Beta functions, integrals dependent on parameters

- **Q1:** B. Gamma(1/2) equals the Gaussian integral over the half-line scaled to sqrt(pi).
- **Q2:** AC. The 1/x integrals diverge logarithmically.
- **Q3:** 0.08333 (tolerance ±0.0001). Gamma(2)Gamma(3)/Gamma(5) = 1*2/24 = 1/12.
- **Q4 (marking outline):** Integrate t^n e^-t by parts; the boundary term vanishes and the remaining integral is n Gamma(n).
- **Q5 (what a passing submission shows):** x = 0.5 is hardest because of the integrable singularity at 0.


---

# D3. Multivariable and Vector Calculus

## A3.1. Functions of several variables, partial derivatives and differentiability

- **Q1:** B. (2xy, x^2) = (4, 1).
- **Q2:** ABD. Partials can exist at a point where the function is not even continuous.
- **Q3:** 3.2 (tolerance ±0.0001). Gradient (4,1) dotted with (0.6, 0.8) = 3.2.
- **Q4 (marking outline):** Apply the chain rule to g(t) = f(a + t u) at t = 0.
- **Q5 (what a passing submission shows):** Gradient (2 cos 2, cos 2 + 4) = about (-0.832, 3.584).

## A3.2. Taylor expansion in several variables, maxima, minima and Lagrange multipliers

- **Q1:** C. The Hessian diag(2,-2) is indefinite.
- **Q2:** ABD. PSD alone is inconclusive (x^3 at 0).
- **Q3:** 2 (tolerance ±0.001). Lagrange: x = y = 1 gives the maximum 2.
- **Q4 (marking outline):** Along any feasible curve, d/dt f = grad f . velocity = 0; tangents span the null space of grad g, so grad f is in the span of grad g.
- **Q5 (what a passing submission shows):** Eigenvalues 6 and 2 at (1,0); -6 and 2 at (-1,0).

## A3.3. Multiple integrals and their applications

- **Q1:** A. (1/2)(1/2) = 1/4.
- **Q2:** ABD. Order can matter if the function is not absolutely integrable.
- **Q3:** 1.571 (tolerance ±0.001). Integral of r^2 * r dr dtheta = 2 pi * 1/4 = pi/2.
- **Q4 (marking outline):** det of [[cos t, -r sin t],[sin t, r cos t]] = r.
- **Q5 (what a passing submission shows):** Error about 1e-3; value about 0.785.

## A3.4. Vector calculus: fields, line and surface integrals, Green, Gauss and Stokes

- **Q1:** B. curl grad f = 0 for twice continuously differentiable f.
- **Q2:** ABC. Gauss' theorem uses the divergence, not the curl.
- **Q3:** 12 (tolerance ±0.001). 2x + 2y + 2z = 12.
- **Q4 (marking outline):** Split into the integral of Q_x (x outer) and of -P_y; apply the fundamental theorem in one variable; match boundary segments.
- **Q5 (what a passing submission shows):** 2 pi = 6.283 on both sides.

## A3.5. Matrix calculus, Jacobians and Hessians for machine learning

- **Q1:** B. It equals 2Ax only for symmetric A.
- **Q2:** ABD. The derivative of trace(AX) is A^T.
- **Q3:** 12 (tolerance ±0.001). (A + A^T) x = (5,7), sum 12.
- **Q4 (marking outline):** Expand to w^T X^T X w - 2 w^T X^T y + y^T y; gradient 2 X^T (X w - y); set to zero.
- **Q5 (what a passing submission shows):** All three pass; the log det gradient is checked with symmetric perturbations.


---

# D4. Linear Algebra: Core, Abstract, Numerical and Applied

## A4.1. Systems of linear equations, matrices, elimination, rank and inverses

- **Q1:** B. The second row is twice the first.
- **Q2:** ABC. Determinant zero means singular.
- **Q3:** 5 (tolerance ±0.001). x = 2, y = 1, so 5.
- **Q4 (marking outline):** Each operation is reversible, so solutions of one system are solutions of the other.
- **Q5 (what a passing submission shows):** Hilbert(5) condition about 4.8e5; error about 1e-10 despite tiny residual.

## A4.2. Vectors, vector spaces, subspaces, bases and dimension

- **Q1:** B. One independent linear constraint removes one dimension.
- **Q2:** ABD. The unit sphere is not closed under scaling.
- **Q3:** 5 (tolerance ±0). Dimension formula: 5.
- **Q4 (marking outline):** Replace spanning vectors one at a time by the independent vectors; after n exchanges the (n+1)th is a combination.
- **Q5 (what a passing submission shows):** Exact rank 3; tolerance 1e-9 still reports 3 for 1e-12 noise but 5 for 1e-6 noise.

## A4.3. Linear maps, representation by matrices, duality and quotient spaces

- **Q1:** B. Rank-nullity: 8 - 3 = 5.
- **Q2:** ABD. Change-of-basis matrices are invertible.
- **Q3:** 4 (tolerance ±0). Nullity = columns - rank = 4.
- **Q4 (marking outline):** Extend a basis of the kernel to a basis of V; the images of the added vectors form a basis of the image.
- **Q5 (what a passing submission shows):** Standard matrix [[0,1],[1,0]]; in the new basis diag(1,-1).

## A4.4. Inner products, norms, orthogonality, projections and Gram–Schmidt

- **Q1:** B. Keep the component along (1,0).
- **Q2:** ABC. Orthogonal matrices preserve length.
- **Q3:** 0.8889 (tolerance ±0.001). Dot product 8 over norms 3 and 3.
- **Q4 (marking outline):** For w in W, norm(b-w)^2 = norm(b-p)^2 + norm(p-w)^2 because b-p is orthogonal to W.
- **Q5 (what a passing submission shows):** Classical GS loses orthogonality badly, modified GS is better, Householder is near machine epsilon.

## A4.5. Determinants, multilinear forms and permutations

- **Q1:** A. 1*4 - 2*3.
- **Q2:** ABD. The determinant is not additive.
- **Q3:** 3 (tolerance ±0.001). Expand along row 1: 2(3-2) + 1(1-0) = 3.
- **Q4 (marking outline):** Apply the alternating property to the sum of the two rows placed in both positions and expand by multilinearity.
- **Q5 (what a passing submission shows):** Permutation and cofactor grow about n times per extra row factorially (about 7-8x per step); LU grows as n^3.

## A4.6. Eigenvalues, eigenvectors, similarity and diagonalization

- **Q1:** B. They sum to 5 and multiply to 6.
- **Q2:** ABD. Defective matrices exist.
- **Q3:** 3 (tolerance ±0.001). Eigenvalues 3 and 1.
- **Q4 (marking outline):** Assume a minimal dependent set, apply A and subtract a multiple to get a shorter dependency, contradiction.
- **Q5 (what a passing submission shows):** Observed rate matches abs(lambda2/lambda1) within 5 percent.

## A4.7. Canonical forms: minimal polynomial, invariant subspaces, Jordan and rational forms

- **Q1:** A. I satisfies A - I = 0.
- **Q2:** ABD. Jordan forms can have off-diagonal ones.
- **Q3:** 1 blocks (tolerance ±0). Nullity of [[0,1],[0,0]] is 1.
- **Q4 (marking outline):** Write A = P D P^-1; p(A) = P p(D) P^-1 and p(lambda_i) = 0 for each diagonal entry.
- **Q5 (what a passing submission shows):** One block of size 3; eigenvalue shift about the cube root of 1e-10, roughly 5e-4.

## A4.8. Spectral theory: normal operators, symmetric matrices, quadratic forms, PSD matrices and kernels

- **Q1:** B. Spectral theorem.
- **Q2:** ABC. Positive diagonal alone is not enough.
- **Q3:** 1 (tolerance ±0.001). Eigenvalues 1 and 3.
- **Q4 (marking outline):** Use conjugate transpose to show lambda equals its conjugate; for orthogonality compare x^T A y computed two ways.
- **Q5 (what a passing submission shows):** Smallest eigenvalue is nonnegative up to about -1e-12; Cholesky succeeds after adding a tiny jitter.

## A4.9. LU, QR, conditioning, SVD, pseudo-inverse and low-rank approximation

- **Q1:** A. Rank is the count of nonzero singular values.
- **Q2:** ABD. Singular values are square roots of eigenvalues of A^T A.
- **Q3:** 2.236 (tolerance ±0.001). Discard singular values 2 and 1: sqrt(5).
- **Q4 (marking outline):** A^T A is symmetric PSD; the maximum of norm(Ax)/norm(x) is the square root of its top eigenvalue.
- **Q5 (what a passing submission shows):** Error equals the square root of the sum of squares of discarded singular values to 1e-10.

## A4.10. Least squares, regularized and constrained least squares

- **Q1:** B. Setting the gradient of the squared error to zero.
- **Q2:** ABD. Rank-deficient X gives non-unique solutions.
- **Q3:** 0.5 (tolerance ±0.001). Sxy/Sxx = 1/2.
- **Q4 (marking outline):** Substitute X = U S V^T into the ridge normal equations and simplify.
- **Q5 (what a passing submission shows):** cond(X^T X) is about cond(X)^2; the normal equations lose about twice the digits.

## A4.11. Applications of linear algebra: PageRank, sparsity, dynamical systems, Markov chains, signal processing and data analytics

- **Q1:** B. It makes the chain irreducible and aperiodic.
- **Q2:** ABD. OMP is greedy and can fail.
- **Q3:** 0.8333 (tolerance ±0.001). pi1 = 0.9 pi1 + 0.5 pi2 gives pi1 = 5 pi2, so 5/6.
- **Q4 (marking outline):** Entries are roots of unity; distinct columns are orthogonal because of the geometric sum identity.
- **Q5 (what a passing submission shows):** PageRank vectors agree to 1e-8; OMP success in the high 80s to 90s percent.


---

# D5. Probability and Stochastic Models

## A5.1. Probability foundations: from events to Bayes' theorem

- **Q1:** B. 6 of 36 outcomes.
- **Q2:** ABD. Exclusive events with positive probability are dependent.
- **Q3:** 0.1538 (tolerance ±0.001). Bayes: 0.009/0.0585 = 0.1538.
- **Q4 (marking outline):** P(A and B) = P(A given B)P(B) = P(B given A)P(A); sum over a partition for the denominator.
- **Q5 (what a passing submission shows):** About 2/3 and about 0.507.

## A5.2. Random variables, distributions and moments

- **Q1:** A. Standard variance identity.
- **Q2:** ABC. That product rule needs uncorrelated variables.
- **Q3:** 2.917 (tolerance ±0.001). E[X^2] = 91/6, mean 3.5: variance 35/12.
- **Q4 (marking outline):** Centre by the mean a E[X] + b; the shift cancels and a squares.
- **Q5 (what a passing submission shows):** Skewness about 2 and excess kurtosis about 6.

## A5.3. Special discrete distributions and the Poisson process

- **Q1:** A. Mean = variance = lambda.
- **Q2:** ABC. The variance is p(1 - p).
- **Q3:** 0.1804 (tolerance ±0.0005). e^-2 * 8/6 = 0.1804.
- **Q4 (marking outline):** Write C(n,k)(lambda/n)^k(1-lambda/n)^(n-k) and take limits term by term.
- **Q5 (what a passing submission shows):** Mean and variance both near 30.

## A5.4. Special continuous distributions and the normal distribution

- **Q1:** C. Standard 95 percent interval.
- **Q2:** ABC. It is unimodal.
- **Q3:** 0.6827 (tolerance ±0.0005). erf(1/sqrt 2) = 0.6827.
- **Q4 (marking outline):** Square the integral, switch to polar, integrate r exp(-r^2/2) to get 2 pi.
- **Q5 (what a passing submission shows):** About 1/sqrt(N) scale, near 0.003.

## A5.5. Functions of random variables, transformations and order statistics

- **Q1:** B. P(-ln U > t) = e^-t.
- **Q2:** ABC. Order statistics are dependent.
- **Q3:** 0.75 (tolerance ±0.001). The maximum has density 3x^2, mean 3/4.
- **Q4 (marking outline):** F_Y(y) = F_X(g^-1(y)); differentiate with the chain rule.
- **Q5 (what a passing submission shows):** 5/6 = 0.833 for the maximum and 1/6 for the minimum.

## A5.6. Joint distributions, conditioning, covariance and multivariate normal

- **Q1:** C. True only for jointly Gaussian pairs.
- **Q2:** ABC. Joint normality needs more than normal marginals.
- **Q3:** 1 (tolerance ±0.001). rho sigma_y/sigma_x times x = 1.
- **Q4 (marking outline):** Sum over x of E[Y given X=x] P(X=x) and swap sums.
- **Q5 (what a passing submission shows):** Agreement within sampling error about 1/sqrt(N).

## A5.7. Limit theorems and concentration inequalities

- **Q1:** B. Standard form.
- **Q2:** ABC. Markov needs nonnegativity.
- **Q3:** 0.1111 (tolerance ±0.001). 1/k^2 with k = 3.
- **Q4 (marking outline):** P((X-mu)^2 >= a^2) <= E[(X-mu)^2]/a^2 = sigma^2/a^2.
- **Q5 (what a passing submission shows):** About 0.14.

## A5.8. Markov chains, queueing theory and reliability

- **Q1:** B. rho = lambda/mu.
- **Q2:** ABC. It is a probability.
- **Q3:** 2 (tolerance ±0.001). L = rho/(1 - rho) = 2.
- **Q4 (marking outline):** Balance across cuts: lambda pi_n = mu pi_{n+1}; normalize the geometric series.
- **Q5 (what a passing submission shows):** 1/(mu - lambda) = 1 time unit.

## A5.9. Conditional expectation and martingales

- **Q1:** A. Averaging the conditional expectation recovers the mean.
- **Q2:** ABD. Submartingales only satisfy an inequality.
- **Q3:** 6.5 (tolerance ±0.001). 3 + E[second die] = 6.5.
- **Q4 (marking outline):** Condition on each partition cell and sum with the cell probabilities.
- **Q5 (what a passing submission shows):** The limit is uniform on [0,1].


---

# D6. Statistics and Statistical Inference

## A6.1. Data, descriptive statistics and measures of association

- **Q1:** C. The median depends on order, not magnitude.
- **Q2:** ABC. Variance has squared units.
- **Q3:** 3.5 (tolerance ±0.001). Q3 = 6.25, Q1 = 2.75.
- **Q4 (marking outline):** Differentiate sum (x_i - c)^2 in c and set to zero; the second derivative is positive.
- **Q5 (what a passing submission shows):** The variance (and kurtosis) change most; the median barely moves.

## A6.2. Sampling distributions and point estimation

- **Q1:** B. Maximize p^s (1-p)^(n-s).
- **Q2:** ABD. The MLE of normal variance is biased.
- **Q3:** 3 (tolerance ±0.001). The sample mean, 3.
- **Q4 (marking outline):** Set derivatives of the log-likelihood to zero; E[S_MLE^2] = (n-1)/n sigma^2.
- **Q5 (what a passing submission shows):** Bias is positive for small n and shrinks like 1/n.

## A6.3. Confidence intervals and hypothesis testing

- **Q1:** B. It is conditional on the null.
- **Q2:** ABD. C confuses p-values with posteriors.
- **Q3:** 2 (tolerance ±0.001). z = 2/(10/10) = 2.
- **Q4 (marking outline):** Pivot (xbar - mu)/(sigma/sqrt n) is standard normal; mu0 is in the interval iff the test fails to reject at 5 percent.
- **Q5 (what a passing submission shows):** About 0.05 within 0.005.

## A6.4. Correlation, regression and multivariate analysis

- **Q1:** A. 1 minus SSE/SST.
- **Q2:** ABC. Adjusted R-squared can decrease.
- **Q3:** 0.98 (tolerance ±0.001). SSE = 0.10 and SST = 5 give 0.98.
- **Q4 (marking outline):** beta_hat = beta + (X^T X)^-1 X^T eps; take expectation and covariance.
- **Q5 (what a passing submission shows):** Lasso keeps the true support with small shrinkage bias.

## A6.5. Bayesian inference and MCMC

- **Q1:** A. Bayes' rule.
- **Q2:** ABC. MCMC samples are correlated.
- **Q3:** 0.6429 (tolerance ±0.001). Posterior Beta(9,5) has mean 9/14.
- **Q4 (marking outline):** Multiply p^(a-1)(1-p)^(b-1) by p^s(1-p)^(n-s); recognize Beta(a+s, b+n-s).
- **Q5 (what a passing submission shows):** About 0.643 with acceptance 30-60 percent for a well-tuned proposal.

## A6.6. Forecasting with statistical and machine-learning models: hydrology and water-resources applications

- **Q1:** A. Constant mean and autocovariance.
- **Q2:** ABC. MAE has the units of the data.
- **Q3:** 2.778 (tolerance ±0.001). sigma^2/(1 - phi^2) = 2.778.
- **Q4 (marking outline):** gamma(h) = phi^h gamma(0) by multiplying the recursion by x_(t-h) and taking expectations.
- **Q5 (what a passing submission shows):** Positive skill, since the AR model beats persistence on autocorrelated data.


---

# D7. Differential Equations, Dynamical Systems, Numerical Methods, Complex Analysis and Transforms

## A7.1. First- and higher-order ordinary differential equations

- **Q1:** A. Separate variables.
- **Q2:** ABC. Euler is first order.
- **Q3:** 0.406 (tolerance ±0.0005). 3 e^-2 = 0.406.
- **Q4 (marking outline):** Roots -1 and -2; y = 2e^-x - e^-2x; uniqueness from the Wronskian being nonzero.
- **Q5 (what a passing submission shows):** Slopes about 1, 2 and 4.

## A7.2. Numerical analysis: iteration, root finding, interpolation and quadrature

- **Q1:** B. Diagonal dominance gives contraction.
- **Q2:** ABC. Newton can diverge.
- **Q3:** 2.667 (tolerance ±0.001). h/3 (f0 + 4 f1 + f2) = 8/3.
- **Q4 (marking outline):** Iterates form a Cauchy sequence by geometric decay; the limit is a fixed point and is unique.
- **Q5 (what a passing submission shows):** Gauss-Seidel needs about half the iterations of Jacobi.

## A7.3. Complex variables: analytic functions and complex integration

- **Q1:** B. Cauchy-Riemann fails everywhere.
- **Q2:** ABC. Continuity is weaker.
- **Q3:** 6.283 (tolerance ±0.001). The integral equals 2 pi i.
- **Q4 (marking outline):** Differentiate the Cauchy-Riemann equations and use equality of mixed partials.
- **Q5 (what a passing submission shows):** Error falls geometrically with the number of points for analytic integrands.

## A7.4. Series, singularities, residues, real integrals and conformal mapping

- **Q1:** B. Coefficient of 1/z.
- **Q2:** ABC. Its proof is deferred.
- **Q3:** 3.142 (tolerance ±0.001). Residue at i is 1/(2i), giving 2 pi i/(2i) = pi.
- **Q4 (marking outline):** Close in the upper half plane; the arc contribution vanishes; residue at i gives pi.
- **Q5 (what a passing submission shows):** About 2/1000 = 0.002 from the tails.

## A7.5. Laplace, Z, Fourier and discrete Fourier transforms

- **Q1:** A. Integrate e^-(s-a)t.
- **Q2:** ABC. It costs O(n^2).
- **Q3:** 0.25 (tolerance ±0.001). 1/s^2 = 0.25.
- **Q4 (marking outline):** Write the product of two integrals as a double integral and change variables to tau and t - tau.
- **Q5 (what a passing submission shows):** u(x,1) = e^-1 sin x.

## A7.6. Mathematical modelling: discrete and continuous dynamical systems

- **Q1:** B. Solve x = r x (1 - x).
- **Q2:** ABC. Zero real parts are inconclusive.
- **Q3:** 0.6 (tolerance ±0.001). 1 - 1/r = 0.6.
- **Q4 (marking outline):** Linearize; stable iff abs(f'(x*)) < 1; f'(x*) = 2 - r.
- **Q5 (what a passing submission shows):** About r = 3 and r = 3.449.

## A7.7. ODE theory for dynamical systems: Gronwall, limit sets, invariant sets and chain transitivity

- **Q1:** A. Integrate the differential inequality.
- **Q2:** ABD. Limit cycles are limit sets that are not points.
- **Q3:** 7.389 (tolerance ±0.001). u(1) <= e^2 = 7.389.
- **Q4 (marking outline):** Multiply by e^(-L t); the product has non-positive derivative.
- **Q5 (what a passing submission shows):** About 2.


---

# D8. Optimization: Theory, Algorithms and Applications

## A8.1. Optimization problems: formulation, history, transformations and basic facts

- **Q1:** B. The maximizers of -f are the minimizers of f.
- **Q2:** ABD. Local minima are global only under convexity.
- **Q3:** -5 (tolerance ±0.001). Stationary point (1,2) gives -5.
- **Q4 (marking outline):** At the optimum t = f(x); any feasible (x,t) has t >= f(x), so the optimal values coincide.
- **Q5 (what a passing submission shows):** Minimizer (1,1) with value 0.

## A8.2. Convex sets, cones, polyhedra and separation

- **Q1:** A. Convex combinations stay in every member.
- **Q2:** ACD. Disjoint intervals are not convex together.
- **Q3:** 4 (tolerance ±0.001). Norm 5 minus radius 1.
- **Q4 (marking outline):** Let p be the projection; the vector x0 - p separates because (c - p).(x0 - p) <= 0 for all c in C.
- **Q5 (what a passing submission shows):** (0, 0, 1).

## A8.3. Convex functions and their calculus

- **Q1:** C. Its second derivative is positive everywhere.
- **Q2:** ABC. Composition needs monotonicity conditions.
- **Q3:** 2 (tolerance ±0.001). The subdifferential is [-1, 1].
- **Q4 (marking outline):** One direction by the limit of the convexity inequality along a segment; the other by combining two supporting lines at a convex combination.
- **Q5 (what a passing submission shows):** Not convex: second derivative is negative near 0.

## A8.4. Unconstrained optimization theory

- **Q1:** B. Fermat's condition.
- **Q2:** ABC. Saddles are stationary but not minima.
- **Q3:** -3 (tolerance ±0.001). f' = 4x^3 - 4 = 0 at x = 1, f = -3.
- **Q4 (marking outline):** Taylor expand along any direction d: f(x*+td) - f(x*) = (t^2/2) d^T H d + o(t^2) >= 0.
- **Q5 (what a passing submission shows):** Four minima, one maximum, four saddle points.

## A8.5. Constrained optimization theory: Lagrange, cones, Fritz John and KKT

- **Q1:** B. Plus complementary slackness lambda g = 0.
- **Q2:** ABC. They must be nonnegative.
- **Q3:** 2 (tolerance ±0.001). 2x - lambda = 0 with x = 1 gives lambda = 2.
- **Q4 (marking outline):** The Lagrangian is convex in x, so stationarity gives its global minimum; weak duality and complementary slackness equate the values.
- **Q5 (what a passing submission shows):** At most 2^3 = 8 candidate active sets; residual below 1e-9.

## A8.6. Lagrangian duality, saddle points and minimax

- **Q1:** A. Any dual function value lower-bounds the primal optimum.
- **Q2:** ABC. Gaps can be positive for nonconvex problems.
- **Q3:** 8 (tolerance ±0.001). The dual max 4 y s.t. y <= 3, y <= 2 gives 8.
- **Q4 (marking outline):** For feasible x and lambda >= 0, L(x, lambda) <= f(x), and the dual function is the infimum of L over x.
- **Q5 (what a passing submission shows):** Value 1; fictitious play empirical value approaches 1.

## A8.7. Linear programming: simplex, duality, sensitivity and interior-point methods

- **Q1:** B. Fundamental theorem of linear programming.
- **Q2:** ABC. It maintains dual feasibility.
- **Q3:** 10 (tolerance ±0.001). Vertex (2,2) gives 10.
- **Q4 (marking outline):** Take an optimal solution with the fewest positive entries; if its columns were dependent, move along the null direction without worsening the cost, reducing support.
- **Q5 (what a passing submission shows):** Optimum 10 at (2,2); duals 2 for the sum constraint and 1 for x <= 2.

## A8.8. Unconstrained descent methods: line search, gradient, Newton, quasi-Newton, conjugate gradient, trust region

- **Q1:** A. Rate is governed by the condition number.
- **Q2:** ABC. Large steps diverge.
- **Q3:** 0.5 (tolerance ±0.001). Each step multiplies x by 0.5.
- **Q4 (marking outline):** Error update e <- (I - A/L) e; eigenvalues of I - A/L lie in [0, 1 - mu/L].
- **Q5 (what a passing submission shows):** At most 20 iterations in exact arithmetic; GD needs hundreds for condition 1000.

## A8.9. Constrained optimization algorithms: QP, projected and reduced gradient, penalty, augmented Lagrangian, SQP

- **Q1:** A. Conditioning degrades as mu grows.
- **Q2:** ABC. They approach feasibility from outside.
- **Q3:** 0.9 (tolerance ±0.001). Derivative: 2x + 18 (x - 1) = 0 gives x = 0.9.
- **Q4 (marking outline):** Set 2x + 2 mu (x - 1) = 0 so x = mu/(1+mu), which tends to 1.
- **Q5 (what a passing submission shows):** (0.5, 0.5); augmented Lagrangian reaches it with a bounded penalty.

## A8.10. First-order methods for ML: stochastic, accelerated, proximal, adaptive, and the dynamical-systems view

- **Q1:** B. Gradient noise keeps it from converging exactly.
- **Q2:** ABC. It shrinks.
- **Q3:** 0.001 (tolerance ±0.0001). Bias-corrected m = 1 and v = 1 give about the learning rate.
- **Q4 (marking outline):** d/dt f(x(t)) = grad f . x' = -norm(grad f)^2.
- **Q5 (what a passing submission shows):** Adam and RMSProp are least sensitive because they rescale per coordinate.

## A8.11. Conic and structured convex programs: QCQP, SOCP, SDP, geometric programs

- **Q1:** B. A convex quadratic constraint is a cone constraint.
- **Q2:** ABC. SDP gives relaxations, not exact solutions in general.
- **Q3:** 1 (tolerance ±0.001). Eigenvalues 1 plus or minus x need to be nonnegative.
- **Q4 (marking outline):** The constraint is membership of (Ax+b, c^T x + d) in the Lorentz cone.
- **Q5 (what a passing submission shows):** Optimal value -5 at x = -c/norm(c).

## A8.12. Applications of optimization: signal estimation, compressive sensing, radar, big data and finance

- **Q1:** A. Level sets of the loss often first touch corners.
- **Q2:** ABC. It exploits sparsity.
- **Q3:** 1.5 (tolerance ±0.001). sign(x) max(abs(x) - 1, 0) = 1.5.
- **Q4 (marking outline):** Minimize 0.5 (z - x)^2 + lambda abs(z); case on the sign of z.
- **Q5 (what a passing submission shows):** Water level between the channel noise levels; the weakest channel gets zero power if its level exceeds the water level.

## A8.13. Non-smooth and difference-of-convex optimization

- **Q1:** A. Subgradient optimality.
- **Q2:** AB. Subgradient steps need not descend.
- **Q3:** 1 (tolerance ±0.001). The subdifferential is [0,1].
- **Q4 (marking outline):** Subgradient inequality f(y) >= f(x*) + 0.(y - x*) is exactly minimality.
- **Q5 (what a passing submission shows):** Noisy non-monotone objective for the subgradient method; monotone decrease for DCA.

## A8.14. Distributed optimization: graphs, consensus, ADMM and dual decomposition

- **Q1:** B. With symmetric doubly stochastic weights.
- **Q2:** ABC. Components never mix.
- **Q3:** 1 (tolerance ±0.001). Eigenvalues 0, 1, 3.
- **Q4 (marking outline):** 1^T L = 0 preserves the sum; other eigenmodes contract by abs(1 - eps lambda_i) < 1.
- **Q5 (what a passing submission shows):** The complete graph; the ring needs far more iterations.

## A8.15. Dynamic optimization and complementarity problems

- **Q1:** A. Substructure.
- **Q2:** ABC. Greedy fails without special structure.
- **Q3:** 4 (tolerance ±0.001). The path A-B-C-D costs 4.
- **Q4 (marking outline):** If a tail were improvable, replacing it would improve the whole path.
- **Q5 (what a passing submission shows):** A base-stock (order-up-to) policy.

## A8.16. Stochastic approximation: algorithms, step sizes and the ODE method

- **Q1:** A. They average out the noise while still reaching the target.
- **Q2:** ABD. Constant steps leave a noise floor.
- **Q3:** 4 (tolerance ±0.001). The recursion is the running mean, 4.
- **Q4 (marking outline):** Induction on n for the mean; the harmonic series diverges and the sum of 1/n^2 converges.
- **Q5 (what a passing submission shows):** 1/n gives the lowest error; the constant step has a noise floor.

## A8.17. Convergence rates, stability, two-timescale algorithms and stochastic recursive inclusions

- **Q1:** A. Time-scale separation.
- **Q2:** ABC. Boundedness must be proved.
- **Q3:** 1.333 (tolerance ±0.001). 4/3.
- **Q4 (marking outline):** Expand the squared error; substitute n v_n = w_n and analyse the fixed point.
- **Q5 (what a passing submission shows):** c = 0.4, which is below 1/2.


---

# D9. Machine Learning Foundations: Supervised, Unsupervised, Probabilistic, Data Mining and Learning Theory

## A9.0. History of AI, symbolic AI and the machine-learning workflow

- **Q1:** B. Turing's 1950 paper; Dartmouth was 1956.
- **Q2:** ABC. Accuracy misleads on imbalanced data.
- **Q3:** 0.7273 (tolerance ±0.001). Precision 0.8, recall 0.667, F1 0.727.
- **Q4 (marking outline):** F1 = 2PR/(P+R); AM-HM inequality.
- **Q5 (what a passing submission shows):** Accuracy is high on imbalanced data while recall of the minority class is 0.

## A9.1. What machine learning is: paradigms, data, hypothesis spaces and the statistical framework

- **Q1:** A. Argmax of P(y given x).
- **Q2:** ABC. Test error is typically above training error.
- **Q3:** 0.3 (tolerance ±0.001). The error of the argmax rule is the smaller posterior.
- **Q4 (marking outline):** Conditional on x, choosing the class with the larger posterior leaves the smaller error probability; integrate over x.
- **Q5 (what a passing submission shows):** kNN reaches above 90 percent versus about 50 percent for majority.

## A9.2. Model evaluation and selection: bias–variance, validation, tuning and metrics

- **Q1:** B. It tracks noise.
- **Q2:** ABC. Use precision-recall or AUC.
- **Q3:** 0.8333 (tolerance ±0.001). 5 of 6 pairs are ordered correctly.
- **Q4 (marking outline):** Add and subtract the expected prediction; cross terms vanish.
- **Q5 (what a passing submission shows):** It explores more distinct values of the important hyperparameters per trial.

## A9.3. Linear regression and linear classification: estimation, logistic and softmax regression, surrogate losses

- **Q1:** A. Negative log-likelihood of a log-linear model.
- **Q2:** ABD. It is convex.
- **Q3:** 0.7311 (tolerance ±0.001). sigma(1) = 0.731.
- **Q4 (marking outline):** Gradient X^T (p - y); Hessian X^T diag(p(1-p)) X, positive semidefinite.
- **Q5 (what a passing submission shows):** Newton converges in 5-8 iterations versus hundreds for GD.

## A9.4. Regularization and implicit regularization

- **Q1:** B. Corners of the L1 ball.
- **Q2:** ABC. They shrink toward zero.
- **Q3:** 0.5 (tolerance ±0.001). w = sum xy/(sum x^2 + lambda) = 0.5.
- **Q4 (marking outline):** Decouple coordinates; solve 0.5 (z - b)^2 + lambda abs(z).
- **Q5 (what a passing submission shows):** Zero.

## A9.5. Perceptron, support vector machines and kernel methods

- **Q1:** A. Maximum-margin principle.
- **Q2:** ABC. The dual has one variable per sample.
- **Q3:** 16 (tolerance ±0.001). 16 mistakes.
- **Q4 (marking outline):** Weight inner product with the separator grows linearly; weight norm grows like sqrt of mistakes; combine.
- **Q5 (what a passing submission shows):** All four points are support vectors.

## A9.6. Bayes decision theory, density estimation and probabilistic classifiers

- **Q1:** A. Factorization of the likelihood.
- **Q2:** ABC. Zero counts need Laplace smoothing.
- **Q3:** 0.7692 (tolerance ±0.001). 0.2/0.26 = 0.769.
- **Q4 (marking outline):** The log-odds is linear because the quadratic terms cancel.
- **Q5 (what a passing submission shows):** kNN and Parzen.

## A9.7. Decision trees and ensembles: bagging, boosting, random forests

- **Q1:** B. Averaging decorrelated predictors.
- **Q2:** ABC. Trees are high variance.
- **Q3:** 0.48 (tolerance ±0.001). 1 - 0.36 - 0.16 = 0.48.
- **Q4 (marking outline):** Parent impurity is concave in class proportions; Jensen gives parent >= weighted children.
- **Q5 (what a passing submission shows):** Boosting and forest beat a single tree; the single tree overfits.

## A9.8. Dimensionality reduction and feature learning

- **Q1:** A. Top eigenvector of the covariance.
- **Q2:** ABD. t-SNE preserves local neighbourhoods.
- **Q3:** 0.6667 (tolerance ±0.001). 2/(2+1).
- **Q4 (marking outline):** Maximize w^T C w subject to norm(w) = 1 by a Lagrange multiplier.
- **Q5 (what a passing submission shows):** Components agree up to sign.

## A9.9. Clustering, mixture models and the EM algorithm

- **Q1:** A. Assignment and update steps each reduce it.
- **Q2:** ABC. It uses soft assignments.
- **Q3:** 1 (tolerance ±0.001). Centres 1.5 and 10.5, each point 0.5 away.
- **Q4 (marking outline):** Assignment minimizes distance for fixed centres; the mean minimizes squared distance for fixed assignments.
- **Q5 (what a passing submission shows):** k-means and a spherical GMM fail; DBSCAN succeeds.

## A9.10. Probabilistic graphical models, hidden Markov models, inference and Gaussian processes

- **Q1:** A. Dynamic programming over paths.
- **Q2:** ABC. Variance shrinks near observed inputs.
- **Q3:** 0.6065 (tolerance ±0.001). k(1,0)/k(0,0) * 1 = 0.6065.
- **Q4 (marking outline):** alpha_t(j) = sum_i alpha_{t-1}(i) a_ij b_j(o_t): N^2 work per step.
- **Q5 (what a passing submission shows):** Monotone non-decreasing.

## A9.11. Instance-based learning, collaborative filtering and recommendation

- **Q1:** A. Similarity between rating columns.
- **Q2:** ABC. It is only a baseline.
- **Q3:** 0.973 (tolerance ±0.001). 26/26.72 = 0.973.
- **Q4 (marking outline):** Minimize the sum of squared errors over rated items plus lambda times norm squared.
- **Q5 (what a passing submission shows):** RMSE drops sharply at the true rank 3.

## A9.12. Data mining: preprocessing, association rules, sequence mining, outliers and case studies

- **Q1:** A. Subsets of frequent sets are frequent.
- **Q2:** ABC. Lift divides confidence by consequent support.
- **Q3:** 1.5 (tolerance ±0.001). 1.5.
- **Q4 (marking outline):** Any transaction containing the superset also contains each subset, so support(subset) >= support(superset).
- **Q5 (what a passing submission shows):** All supersets of infrequent itemsets are pruned.

## A9.13. Learning theory: PAC, VC dimension, generalization and modern overparametrization

- **Q1:** B. Radon's theorem.
- **Q2:** ABC. It tends to enlarge the gap.
- **Q3:** 99.03 (tolerance ±0.5). (6.908 + 2.996)/0.1 = 99.0.
- **Q4 (marking outline):** Union bound over bad hypotheses with true error above eps, each surviving m samples with probability at most (1 - eps)^m.
- **Q5 (what a passing submission shows):** Test error peaks near p = n.

## A9.14. Symbolic and knowledge-based machine learning, tools and cognitive-science influences

- **Q1:** A. Candidate-elimination definition.
- **Q2:** ABC. It uses a domain theory.
- **Q3:** 0.9403 (tolerance ±0.001). 0.940.
- **Q4 (marking outline):** H' = log((1-p)/p) is zero at 1/2 and H is concave.
- **Q5 (what a passing submission shows):** Outlook.


---

# D10. Sequential Decision Making: Bandits and Reinforcement Learning

## A10.1. From batch to online learning: adversarial full-information and bandit settings

- **Q1:** B. Standard bound for N experts.
- **Q2:** ABC. Exp3 uses importance-weighted estimates.
- **Q3:** 10 (tolerance ±0.001). log2(1024) = 10.
- **Q4 (marking outline):** Each mistake removes at least half the hypotheses.
- **Q5 (what a passing submission shows):** About 0.5.

## A10.2. Stochastic bandits: regret notions, UCB, KL-UCB and lower bounds

- **Q1:** A. Optimism in the face of uncertainty.
- **Q2:** ABD. Fixed epsilon explores forever and has linear regret.
- **Q3:** 1.46 (tolerance ±0.001). 0.5 + 0.960 = 1.460.
- **Q4 (marking outline):** Hoeffding: P(mean - mu >= r) <= exp(-2 n r^2); set equal to delta.
- **Q5 (what a passing submission shows):** UCB1 and Thompson sampling grow logarithmically; epsilon-greedy grows linearly.

## A10.3. Contextual bandits and pure exploration

- **Q1:** A. Ridge estimate plus an ellipsoidal bonus.
- **Q2:** ABC. It minimizes simple regret or identification error.
- **Q3:** 2.5 (tolerance ±0.001). 0.5 * 5 = 2.5.
- **Q4 (marking outline):** Minimize squared error plus norm squared; set the gradient to zero.
- **Q5 (what a passing submission shows):** Smaller gaps need quadratically more samples.

## A10.4. Markov decision processes, dynamic programming and temporal-difference learning

- **Q1:** A. Banach fixed-point theorem.
- **Q2:** ABC. TD learns from samples.
- **Q3:** 10 (tolerance ±0.001). 1/(1 - gamma) = 10.
- **Q4 (marking outline):** abs(max_a x_a - max_a y_a) <= max_a abs(x_a - y_a); transitions average.
- **Q5 (what a passing submission shows):** The agent avoids stepping toward the pit.

## A10.5. Policy gradient, actor–critic and proximal policy optimization

- **Q1:** A. Score-function form.
- **Q2:** ABC. Baselines independent of the action leave it unbiased.
- **Q3:** 1.2 (tolerance ±0.001). min(1.5, clip(1.5) = 1.2) = 1.2.
- **Q4 (marking outline):** E[grad log pi * b(s)] = b(s) grad sum_a pi = 0.
- **Q5 (what a passing submission shows):** PPO.

## A10.6. Stochastic approximation in reinforcement learning

- **Q1:** A. Noisy sample of the Bellman equation drives the update.
- **Q2:** ABD. Off-policy linear TD can diverge.
- **Q3:** 0.622 (tolerance ±0.001). delta = 1.22; V(s) becomes 0.622.
- **Q4 (marking outline):** Take the expectation of the TD update over the stationary state distribution D.
- **Q5 (what a passing submission shows):** It shrinks to the sampling noise level with decaying steps.


---

# D11. Deep Learning Foundations

## A11.1. Perceptron, multilayer networks, activations and loss functions

- **Q1:** C. XOR is not linearly separable.
- **Q2:** ABC. Depth is not a guarantee.
- **Q3:** 101770 parameters (tolerance ±0). 100,352 + 128 + 1,280 + 10 = 101,770.
- **Q4 (marking outline):** Four inequalities on w1, w2, b are inconsistent: w1 + b > 0, w2 + b > 0, b <= 0, w1 + w2 + b <= 0.
- **Q5 (what a passing submission shows):** Two hidden units suffice.

## A11.2. Backpropagation and training deep networks

- **Q1:** A. Reverse-mode differentiation.
- **Q2:** ABC. That is finite differences, not backpropagation.
- **Q3:** 9.537e-07 (tolerance ±1e-9). 0.25^10 = 9.54e-7.
- **Q4 (marking outline):** delta2 = yhat - y; grad W2 = delta2 h^T; delta1 = (W2^T delta2) * (1 - h^2); grad W1 = delta1 x^T.
- **Q5 (what a passing submission shows):** ln 2 = 0.693.

## A11.3. Overfitting, regularization and generalization in deep networks

- **Q1:** A. The gradient of lambda/2 norm(w)^2 is lambda w.
- **Q2:** ABC. L1 produces sparsity.
- **Q3:** 1.25 (tolerance ±0.001). Divide kept activations by the keep probability.
- **Q4 (marking outline):** Differentiate the penalty and substitute.
- **Q5 (what a passing submission shows):** Each reduces the gap; early stopping halts near the validation minimum.

## A11.4. Convolutional neural networks and image representation

- **Q1:** B. (32 - 5)/1 + 1 = 28.
- **Q2:** ABC. Weights are shared across positions.
- **Q3:** 448 parameters (tolerance ±0). 432 weights + 16 biases.
- **Q4 (marking outline):** Write the output as a sum over kernel taps and apply the chain rule per input position.
- **Q5 (what a passing submission shows):** 13 x 13 spatial size.

## A11.5. Explainable AI for deep models

- **Q1:** A. They fully distribute the payoff.
- **Q2:** ABC. Handling correlation is an open issue.
- **Q3:** 3 (tolerance ±0.001). Average marginal contribution: (2 + 4)/2 = 3.
- **Q4 (marking outline):** phi1 + phi2 = 0.5(v1 + v12 - v2) + 0.5(v2 + v12 - v1) = v12.
- **Q5 (what a passing submission shows):** 2^4 = 16.

## A11.6. Segmentation and object detection

- **Q1:** A. Standard definition.
- **Q2:** ABC. IoU lies between 0 and 1.
- **Q3:** 0.1429 (tolerance ±0.001). Intersection 1, union 4 + 4 - 1 = 7.
- **Q4 (marking outline):** Intersection is a subset of the union; equality of measures forces equal sets up to null sets.
- **Q5 (what a passing submission shows):** Above 0.9 on circles versus a background.

## A11.7. Recurrent networks: RNN, LSTM, GRU, backpropagation through time and attention in RNNs

- **Q1:** A. The forget-gated linear path carries gradient.
- **Q2:** ABC. The recurrence is sequential.
- **Q3:** 0.1216 (tolerance ±0.001). 0.9^20 = 0.1216.
- **Q4 (marking outline):** dL/dh_k contains the product of W^T diag(f'); behaviour depends on the largest singular value relative to 1.
- **Q5 (what a passing submission shows):** Clipping removes the rare loss explosions.

## A11.8. Autoencoders and representation learning

- **Q1:** A. Low-dimensional code.
- **Q2:** AB. A VAE adds a probabilistic prior; overcomplete codes can learn the identity.
- **Q3:** 24.5 (tolerance ±0.001). 24.5.
- **Q4 (marking outline):** Reconstruction error is the Frobenius distance to a rank-k matrix, minimized by truncated SVD.
- **Q5 (what a passing submission shows):** Equal up to optimization error.


---

# D12. Natural Language Processing, the Transformer and Large Language Models

## A12.1. NLP foundations and the classical NLP pipeline

- **Q1:** A. P(w1..wn) = product of P(wi given earlier words).
- **Q2:** ABC. Order is discarded.
- **Q3:** 8 (tolerance ±0.001). exp(-log(1/8)) = 8.
- **Q4 (marking outline):** Definition; uniform gives exp(log V) = V.
- **Q5 (what a passing submission shows):** Bigram perplexity is lower on training text.

## A12.2. Word representations and multilingual embeddings

- **Q1:** A. Standard definition.
- **Q2:** ABC. fastText adds character n-grams.
- **Q3:** 0.7071 (tolerance ±0.001). 1/sqrt 2 = 0.707.
- **Q4 (marking outline):** Loss = -log sigma(u_o.v_c) - sum log sigma(-u_k.v_c); differentiate.
- **Q5 (what a passing submission shows):** Rare words, because they receive few updates.

## A12.3. Attention and the Transformer architecture

- **Q1:** A. The variance of q.k grows with d_k.
- **Q2:** ABC. Cost is quadratic.
- **Q3:** 0.8808 (tolerance ±0.001). e^2/(e^2 + 1) = 0.881.
- **Q4 (marking outline):** Sum of d independent products each with variance 1.
- **Q5 (what a passing submission shows):** 6 x 6 lower-triangular after masking.

## A12.4. Pretraining, self-supervised learning and the LLM landscape

- **Q1:** A. Masked-token prediction.
- **Q2:** ABD. BERT is bidirectional and not autoregressive.
- **Q3:** 7.389 (tolerance ±0.001). e^2 = 7.389.
- **Q4 (marking outline):** Take the negative log of the product of conditionals.
- **Q5 (what a passing submission shows):** ln 64 = 4.159.

## A12.5. Scaling laws, LLM architectures and long context

- **Q1:** A. Empirical power laws.
- **Q2:** ABD. Without enough data, big models overfit.
- **Q3:** 0.9487 (tolerance ±0.001). 0.9487.
- **Q4 (marking outline):** Substitute D = C/(6N); by symmetry and convexity the minimum is at N = D.
- **Q5 (what a passing submission shows):** Within a few percent for low noise.

## A12.6. Decoding strategies and sampling

- **Q1:** A. The softmax concentrates on the argmax.
- **Q2:** ACD. Beam search is a heuristic.
- **Q3:** 0.6652 (tolerance ±0.001). 0.665.
- **Q4 (marking outline):** Divide numerator and denominator by the largest term; take limits.
- **Q5 (what a passing submission shows):** Greedy decoding.

## A12.7. Prompting: fundamentals, APIs and advanced techniques

- **Q1:** A. In-context examples.
- **Q2:** ABC. It uses several linked prompts.
- **Q3:** 0.6826 (tolerance ±0.001). 0.6826.
- **Q4 (marking outline):** P(majority) = 3p^2 - 2p^3; compare with p.
- **Q5 (what a passing submission shows):** Three calls: two tool requests and a final answer.

## A12.8. Instruction tuning, RLHF and alignment: PPO and DPO

- **Q1:** A. It optimizes a closed-form objective on preference pairs.
- **Q2:** ABC. DPO is offline.
- **Q3:** 0.7311 (tolerance ±0.001). sigma(1) = 0.731.
- **Q4 (marking outline):** Lagrangian over the simplex; stationarity gives the exponential tilt.
- **Q5 (what a passing submission shows):** It increases the preferred response's relative log-probability.

## A12.9. Parameter-efficient fine-tuning: LoRA and QLoRA

- **Q1:** A. Delta W = B A.
- **Q2:** ABC. The update can be merged into the base weights.
- **Q3:** 64 (tolerance ±0.001). 1,048,576 / 16,384 = 64.
- **Q4 (marking outline):** rank(BA) <= min(rank B, rank A) <= r; parameters 2 d r.
- **Q5 (what a passing submission shows):** About 64x fewer trainable parameters at rank 8 and width 1024.

## A12.10. Prompt optimization, compression and prompt security

- **Q1:** A. Instructions hidden in data.
- **Q2:** ABC. Leaked prompts can expose secrets.
- **Q3:** 4 (tolerance ±0.001). 4x.
- **Q4 (marking outline):** Two-sided Hoeffding: 2 exp(-2 n eps^2) <= delta.
- **Q5 (what a passing submission shows):** About 738 samples.


---

# D13. Deep Generative Models

## A13.1. Probabilistic deep generative modelling: foundations and taxonomy

- **Q1:** A. Equivalent up to a constant.
- **Q2:** ABC. Many can.
- **Q3:** 0.1438 (tolerance ±0.001). 0.1438.
- **Q4 (marking outline):** KL = E log p_data - E log p_theta; the first term is constant.
- **Q5 (what a passing submission shows):** Large reduction when the proposal covers the rare region.

## A13.2. Generative modelling via variational divergence minimization

- **Q1:** A. JS of two distributions is at most ln 2 nats.
- **Q2:** ABC. TV is at most 1.
- **Q3:** 0.5 (tolerance ±0.001). TV = half the L1 distance = 0.5.
- **Q4 (marking outline):** JS is the average of two KLs to the mixture, each at most ln 2 by log-sum bounds on mixture ratios.
- **Q5 (what a passing submission shows):** KL grows quadratically; JS saturates at ln 2; TV saturates at 1.

## A13.3. Generative adversarial networks: formulation, training, WGAN and applications

- **Q1:** A. Derived in the original GAN paper.
- **Q2:** ABC. They are implicit models.
- **Q3:** 0.75 (tolerance ±0.001). 0.75.
- **Q4 (marking outline):** Differentiate in D and set to zero: D = p/(p + q).
- **Q5 (what a passing submission shows):** Vanishing generator gradients with the saturating loss.

## A13.4. Variational autoencoders, improvements and VQ-VAE

- **Q1:** A. Standard decomposition.
- **Q2:** ABC. They maximize a bound.
- **Q3:** 2 (tolerance ±0.001). mu^2/2 = 2.
- **Q4 (marking outline):** log p(x) = log E_q[p(x,z)/q(z)] >= E_q[log p(x,z) - log q(z)].
- **Q5 (what a passing submission shows):** Near zero.

## A13.5. Autoregressive models

- **Q1:** A. Product of conditionals.
- **Q2:** ABC. Sampling is sequential.
- **Q3:** -2.079 (tolerance ±0.001). ln(0.125) = -2.079.
- **Q4 (marking outline):** Repeated application of P(A, B) = P(A) P(B given A).
- **Q5 (what a passing submission shows):** Trigram on large text; bigram can win on tiny text because of sparsity.

## A13.6. Energy-based and score-based models; Langevin sampling

- **Q1:** A. grad log p(x).
- **Q2:** ABC. It avoids the partition function.
- **Q3:** -2 (tolerance ±0.001). -(x - mu)/sigma^2 = -2.
- **Q4 (marking outline):** Differentiate the log-density.
- **Q5 (what a passing submission shows):** Samples drift past modes and become unstable.

## A13.7. Denoising diffusion probabilistic models, conditional diffusion and Stable Diffusion

- **Q1:** A. Closed form from a product of Gaussians.
- **Q2:** ABC. The reverse mean is learned.
- **Q3:** 0.729 (tolerance ±0.0005). (1 - beta)^3 = 0.729.
- **Q4 (marking outline):** Compose Gaussian steps; means multiply and variances add appropriately.
- **Q5 (what a passing submission shows):** Quality degrades, a deterministic DDIM-style sampler degrades less.

## A13.8. Normalizing flows (gap-fill from the references)

- **Q1:** A. With the Jacobian determinant.
- **Q2:** ABC. Sampling is one pass.
- **Q3:** -1.612 (tolerance ±0.001). z = 0, log p_z(0) = -0.919, minus log 2: -1.612.
- **Q4 (marking outline):** P(X <= x) = P(Z <= g^-1(x)) for monotone increasing g; differentiate.
- **Q5 (what a passing submission shows):** Zero.


---

# D14. Retrieval-Augmented Generation and Agentic Systems

## A14.1. Why RAG, RAG architecture and classical retrievers

- **Q1:** A. The answer is conditioned on evidence.
- **Q2:** ABC. Dense retrieval compares embeddings.
- **Q3:** 4.605 (tolerance ±0.001). ln 100 = 4.605.
- **Q4 (marking outline):** Divide numerator and denominator by tf and let tf go to infinity.
- **Q5 (what a passing submission shows):** BM25 on exact keyword queries.

## A14.2. RAG failure modes, types of RAG and assessment

- **Q1:** A. The needed evidence never reaches the generator.
- **Q2:** ABC. RAGAS uses LLM or embedding judgements.
- **Q3:** 0.75 (tolerance ±0.001). 0.75.
- **Q4 (marking outline):** Law of total probability; derivative equals a1 - a0.
- **Q5 (what a passing submission shows):** Dropping the gold chunk.

## A14.3. Sparse retrieval limits and dense representations

- **Q1:** B. Cosine of the angle between vectors.
- **Q2:** ABC. Synonyms are close, not orthogonal.
- **Q3:** 3 (tolerance ±0.001). (2 + 4)/2 = 3.
- **Q4 (marking outline):** Expand the squared norm.
- **Q5 (what a passing submission shows):** Embeddings win on paraphrases; TF-IDF on exact terms.

## A14.4. Learning retrieval-oriented embeddings and choosing an embedding model

- **Q1:** A. They are free negatives.
- **Q2:** ABC. They are designed to truncate gracefully.
- **Q3:** 1.386 (tolerance ±0.001). ln N = 1.386.
- **Q4 (marking outline):** The softmax probability of the positive is 1/N; take the negative log.
- **Q5 (what a passing submission shows):** Recall@1 improves, with some risk from false negatives.

## A14.5. Document processing and chunking

- **Q1:** A. Context spans boundaries.
- **Q2:** ABC. It has a large effect.
- **Q3:** 7 chunks (tolerance ±0). Stride 150; windows start at 0, 150, ..., 900 (the last is shorter).
- **Q4 (marking outline):** Windows start at multiples of s until the end is covered.
- **Q5 (what a passing submission shows):** Structure-aware chunking by headings.

## A14.6. Vector databases and indexes: KNN, IVF, PQ, HNSW, FAISS and ChromaDB

- **Q1:** B. Navigable small-world layers.
- **Q2:** ABC. Brute force is linear.
- **Q3:** 32 (tolerance ±0.001). 32x.
- **Q4 (marking outline):** Set the derivative in nlist to zero.
- **Q5 (what a passing submission shows):** About 1000.

## A14.7. The retrieval pipeline: bi-encoder, cross-encoder, ColBERT and two-stage retrieval

- **Q1:** A. Recall first, precision second.
- **Q2:** ABC. It is prohibitively expensive.
- **Q3:** 0.03227 (tolerance ±0.0001). 0.0323.
- **Q4 (marking outline):** Compare total costs and rearrange.
- **Q5 (what a passing submission shows):** Typically yes on mixed query types.

## A14.8. Production RAG: request shaping, query transformation, routing, security, cost and observability

- **Q1:** A. Precision-recall trade-off.
- **Q2:** ABC. Rule or classifier routers exist.
- **Q3:** 0.015 (tolerance ±0.0001). 0.014 + 0.001 = 0.015.
- **Q4 (marking outline):** Savings h c_llm equal the lookup cost.
- **Q5 (what a passing submission shows):** Hit rate falls and wrong-hit rate falls as the threshold rises.

## A14.9. Limits of single-shot RAG and the move to agents

- **Q1:** A. Intermediate answers feed later retrieval.
- **Q2:** ABC. Branch logic cannot anticipate every question.
- **Q3:** 0.64 (tolerance ±0.001). 0.64.
- **Q4 (marking outline):** Product rule for independent events.
- **Q5 (what a passing submission shows):** Roughly multiplicative decay.

## A14.10. Agent basics, tool calling and orchestration

- **Q1:** A. It is the interface contract.
- **Q2:** ABC. Agents loop until done or a budget runs out.
- **Q3:** 8 calls (tolerance ±0). 1 + 6 + 1 = 8.
- **Q4 (marking outline):** The loop counter increases each iteration and the loop exits at B.
- **Q5 (what a passing submission shows):** Eight calls for the example in Q3.

## A14.11. Planning with ReAct

- **Q1:** A. Reason, act, observe.
- **Q2:** ABC. It does not.
- **Q3:** 3500 tokens (tolerance ±0). 3500.
- **Q4 (marking outline):** Sum of an arithmetic series c0 + k d.
- **Q5 (what a passing submission shows):** The hierarchical version.

## A14.12. State machines and LangGraph

- **Q1:** A. Control flow.
- **Q2:** ABC. State can bloat.
- **Q3:** 15 executions (tolerance ±0). 15.
- **Q4 (marking outline):** The counter strictly increases and the guard fails at B.
- **Q5 (what a passing submission shows):** Equal traces; length equals node executions.

## A14.13. Agentic memory

- **Q1:** A. Event-level records.
- **Q2:** ABC. It needs pruning and conflict handling.
- **Q3:** 0.85 (tolerance ±0.001). 0.85.
- **Q4 (marking outline):** A newer but wrong statement replaces an older correct fact; the policy has no notion of reliability.
- **Q5 (what a passing submission shows):** Fewer wrong overwrites.

## A14.14. Provenance and citations

- **Q1:** A. Traceability.
- **Q2:** ABC. Models can fabricate citations.
- **Q3:** 0.8 (tolerance ±0.001). 0.8.
- **Q4 (marking outline):** F1 = 2 P R/(P + R) = 1/1.5.
- **Q5 (what a passing submission shows):** It accepts spans that overlap lexically but do not entail the claim.

## A14.15. Multi-agent architecture summary, error handling and best practices

- **Q1:** A. Explicit error policy.
- **Q2:** ABC. Logging is essential for debugging.
- **Q3:** 0.8574 (tolerance ±0.001). 0.857.
- **Q4 (marking outline):** Independent attempts; the failure probability squares.
- **Q5 (what a passing submission shows):** About 0.9975^3 = 0.9925.


---

# D15. Evaluation, Safety and Responsible AI

## A15.1. LLM evaluation: metric architecture and reference-based metrics

- **Q1:** A. With a brevity penalty.
- **Q2:** ABC. BLEU is precision-oriented.
- **Q3:** 0.6667 (tolerance ±0.001). The word 'the' is clipped to 1 match (the reference has one); 'cat' matches once; 2 of 3.
- **Q4 (marking outline):** Count matches with and without the clip at the reference count.
- **Q5 (what a passing submission shows):** The embedding-based score.

## A15.2. LLM-as-a-judge and factuality

- **Q1:** A. Order effects.
- **Q2:** ABC. Agreement is imperfect.
- **Q3:** 0.7 (tolerance ±0.001). 0.7.
- **Q4 (marking outline):** Substitute p_o = 1 and p_o = p_e.
- **Q5 (what a passing submission shows):** Kappa rises after debiasing.

## A15.3. AI safety foundations and threat models

- **Q1:** A. Overfitting leaks membership.
- **Q2:** ABC. Black-box attacks exist.
- **Q3:** 0.3 (tolerance ±0.001). 0.3.
- **Q4 (marking outline):** TPR(t) = FPR(t) for every threshold.
- **Q5 (what a passing submission shows):** Advantage falls.

## A15.4. White-box attacks and prompt injection

- **Q1:** A. White-box discrete optimization.
- **Q2:** ABC. Black-box attacks use only queries.
- **Q3:** 0.24 (tolerance ±0.001). 0.24.
- **Q4 (marking outline):** CLT for a binomial proportion.
- **Q5 (what a passing submission shows):** About 0.118.

## A15.5. Black-box attacks and the jailbreak taxonomy

- **Q1:** A. Prompt Automatic Iterative Refinement.
- **Q2:** ABC. Multi-turn attacks exist.
- **Q3:** 10 (tolerance ±0.001). Geometric mean 10.
- **Q4 (marking outline):** Sum k (1-p)^(k-1) p = 1/p.
- **Q5 (what a passing submission shows):** About plus or minus 0.078.

## A15.6. Defense, interpretability and ethics

- **Q1:** A. Find failures before attackers do.
- **Q2:** ABC. Single layers fail.
- **Q3:** 0.027 (tolerance ±0.0005). 0.027.
- **Q4 (marking outline):** Independent: product; perfectly correlated layers fail together, so residual equals one layer's.
- **Q5 (what a passing submission shows):** Some attacks still succeed; the defect list drives round two.


---

# D16. ML Systems, Efficiency and Distributed and Federated Learning

## A16.1. CNN computation and accelerators

- **Q1:** A. min(peak, bandwidth x intensity).
- **Q2:** ABC. Small layers can be memory-bound.
- **Q3:** 170.7 FLOP/byte (tolerance ±0.01). 2 N^3 FLOPs over 3 N^2 values of 4 bytes.
- **Q4 (marking outline):** Each output element needs K^2 Cin MACs.
- **Q5 (what a passing submission shows):** Roughly the tile reuse factor.

## A16.2. Parallelism for training, communication and fault tolerance

- **Q1:** A. Gradients are averaged.
- **Q2:** ABC. It stays near 2n.
- **Q3:** 1.75 GB (tolerance ±0.001). 2 (p - 1)/p times n = 1.75.
- **Q4 (marking outline):** Each phase sends (p - 1) chunks of size n/p.
- **Q5 (what a passing submission shows):** 1.75 n per worker.

## A16.3. LLM decoding, memory management and serving infrastructure

- **Q1:** A. Avoids recomputation in decoding.
- **Q2:** ABC. It is memory-bandwidth-bound.
- **Q3:** 524288 bytes (tolerance ±0). 2 (K and V) x L x H x d_head x bytes = 524,288.
- **Q4 (marking outline):** One K and one V vector of size H d_head per layer per token.
- **Q5 (what a passing submission shows):** Throughput rises with batch size until compute saturates.

## A16.4. Model compression and quantization

- **Q1:** A. Maps the largest magnitude to 127.
- **Q2:** ABC. Rounding introduces error.
- **Q3:** 0.02 (tolerance ±0.0001). 0.02.
- **Q4 (marking outline):** The nearest grid point is within scale/2.
- **Q5 (what a passing submission shows):** Around 3-4 bits without calibration.

## A16.5. Graph neural network inference systems

- **Q1:** A. A_hat H W.
- **Q2:** ABC. Sparse formats scale better.
- **Q3:** 0.4082 (tolerance ±0.001). 1/sqrt 6 = 0.408.
- **Q4 (marking outline):** Relabeling nodes permutes rows and columns of A and rows of H consistently; the output rows permute equally.
- **Q5 (what a passing submission shows):** Sparse storage is far smaller at 1 percent density; index arrays dominate its size.

## A16.6. Federated learning

- **Q1:** A. Weighted averaging.
- **Q2:** ABC. Communication is the bottleneck.
- **Q3:** 2.5 (tolerance ±0.001). 2.5.
- **Q4 (marking outline):** Averaging the updated weights averages the gradient steps with the same weights.
- **Q5 (what a passing submission shows):** The coordinate-wise median.


---

# D17. Approximation Algorithms and Computational Complexity

## A17.1. Review of NP-completeness and the approximation framework

- **Q1:** A. Every edge must have an endpoint outside S.
- **Q2:** ABC. Many NP-hard problems provably do not.
- **Q3:** 5 vertices (tolerance ±0). The complement of a maximum independent set is a minimum vertex cover.
- **Q4 (marking outline):** An edge has both endpoints in S exactly when it is uncovered by V minus S.
- **Q5 (what a passing submission shows):** The identity holds on every instance.

## A17.2. Approximation for vertex cover, set cover and the traveling salesman problem

- **Q1:** A. Take both endpoints of every matching edge.
- **Q2:** ABD. General TSP has none unless P = NP.
- **Q3:** 2.929 (tolerance ±0.001). 1 + 1/2 + ... + 1/10 = 2.929.
- **Q4 (marking outline):** Matching edges are disjoint, so OPT needs one endpoint per edge; the algorithm takes two per edge.
- **Q5 (what a passing submission shows):** Exactly 2.

## A17.3. Approximation for the knapsack problem and job scheduling

- **Q1:** A. Rounding profits keeps the table small.
- **Q2:** ABD. Knapsack is only weakly NP-hard.
- **Q3:** 1.75 (tolerance ±0.001). 1.75.
- **Q4 (marking outline):** The last job finishes at average load of the others plus its length; both are bounded by OPT.
- **Q5 (what a passing submission shows):** LPT.

## A17.4. Linear programming basics and deterministic rounding

- **Q1:** A. Shown by the complete graph.
- **Q2:** ABC. The relaxation can only lower the minimum.
- **Q3:** 1.8 (tolerance ±0.001). 9/5 = 1.8.
- **Q4 (marking outline):** Each edge constraint requires x_u + x_v >= 1, which equals 1.
- **Q5 (what a passing submission shows):** At most 2, usually about 1.1 to 1.3 on random graphs.

## A17.5. Randomized rounding

- **Q1:** A. Only the all-false assignment of its literals fails.
- **Q2:** ABC. It is not optimal.
- **Q3:** 0.875 (tolerance ±0.001). 7/8.
- **Q4 (marking outline):** Each clause is satisfied with probability at least 1/2; sum over clauses.
- **Q5 (what a passing submission shows):** Random assignment alone gets about 7/8.

## A17.6. The primal–dual method

- **Q1:** A. f is the maximum element frequency.
- **Q2:** ABC. It builds a feasible primal and dual, not an exact LP solution.
- **Q3:** 1.867 (tolerance ±0.001). OPT >= 7.5 so cost/OPT <= 1.867.
- **Q4 (marking outline):** Each chosen set is tight; cost <= sum over elements of y_e times frequency <= f times dual <= f OPT.
- **Q5 (what a passing submission shows):** At most f, usually well below it.

## A17.7. Semidefinite programming for max cut, and hardness of approximation

- **Q1:** A. Random hyperplane rounding of the SDP.
- **Q2:** ABD. Metric TSP has a 3/2 approximation.
- **Q3:** 0.3333 (tolerance ±0.001). theta/pi = 1/3.
- **Q4 (marking outline):** Project onto the plane they span; the normal direction is uniform; the separating arcs have measure 2 theta of 2 pi.
- **Q5 (what a passing submission shows):** At least 0.878 on average, usually 0.95 or more on random graphs.
