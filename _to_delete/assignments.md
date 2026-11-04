# Assignments: unified curriculum

Companion to `unified_curriculum.md`. One assignment per content unit (148 assignments, A1.1–A17.7), in the style of an NPTEL course: multiple-choice (MCQ), multiple-select (MSQ) and numerical-answer (NAT) questions, plus a derivation and a programming question. The capstones (U18.1–U18.7) are projects with their own acceptance criteria in the curriculum and have no assignment. Answer keys are in `assignments_key.md`; open a key only after you have submitted an attempt.

## How the assignments work

| Item | Rule |
|---|---|
| **Format** | Q1 MCQ (1 mark) · Q2 MSQ (2) · Q3 NAT (2) · Q4 prove or derive (2) · Q5 NumPy programming (3). Total 10 marks. |
| **Pass mark and gates** | A unit's assignment is passed at 7/10, and Q4 and Q5 must each be accepted: a unit is not closed while its derivation or its code is missing (Master Rules 6.12: evidence by doing). |
| **Attempts** | Attempt before any hint. Hints escalate one notch at a time and only when asked: what structure do you see → a smaller case → the smallest useful hint → only then the key (Master Rules 5.7). A missed question gets one smaller, reworded retry of the same kind (Master Rules 6.5). |
| **Predict first** | Before running Q5, write a one-line prediction of its outcome, then report prediction, code and result (Master Rules 6.1, 6.4). |
| **Source alignment** | Each assignment lists the source course weeks its unit absorbs (for example "MFML W3"), so it can be set beside the matching official NPTEL weekly assignment when you fetch those. Official NPTEL assignments are not included here: none were downloaded. |
| **Who writes what** | The tutor writes the questions and keys. You write every answer, proof and line of code; the tutor reviews and points at what to reconsider, and never writes your solution (Master Rules 2.10, 6.13). |
| **Domain exit** | After the last unit of a domain, a qualifying-style problem set drawn from that domain's assignments is run before its capstone (Master Rules 8.7, 9.5). |
| **Recall** | Missed questions are re-attempted cold at about 1, 3 and 7 days; mastered units get a one-question recall at about 1, 3, 7 and 21 sessions (Master Rules 8.2). |

## The from-scratch tooling guideline (NumPy-first, flexible)

You asked to learn from-scratch Python implementations with NumPy at most, and then clarified that NumPy-only is "more of a suggestion" and I may "design as needed". So this is a guideline with one fixed aim:

1. **Fixed aim:** the algorithm you are learning is written by you first, with a hand-derived gradient where one exists, checked by finite differences.
2. **Default tools:** the Python standard library and NumPy, with Matplotlib for plots. They keep every step visible, which is why they are the default.
3. **Flexible by design:** where another library serves the learning goal, the unit's Build line says so. Examples already chosen: PyTorch for transfer learning on pretrained networks (A11.4), pretrained fine-tuning (A12.4) and distributed data parallel (A16.2); FAISS for the scale comparison (A14.6); LangGraph where the framework is the topic (A14.12); `cvxpy` or SciPy where a solver is not the thing being learned (A8.11, A17.4, A17.7). None of these is a breach: they are design choices.
4. **Oracles:** libraries that implement the same algorithm (scikit-learn, SciPy, PyTorch autograd) are normally used in a separate `tests/oracle/` file to check your result after your own version passes.
5. **Each Q5** states its default tooling in its wording; if a question's wording and the unit's Build line differ, the Build line wins.
6. **Toy size:** keep models small enough to train in minutes on a CPU. Scale effects are studied by fitting curves to toy runs.

### A0. Environment (optional first task; not scored)

Create the repository layout `scratch/` (sub-packages such as `linalg`, `calculus`, `prob`, `optim`, `ml`, `nn`, `nlp`, `gen`, `rag`, `systems`) and `tests/oracle/`. Write, yourself, (a) a finite-difference gradient checker `grad_check(f, x)` returning the maximum relative error, and (b) if you want it, an import report that walks every `.py` file in `scratch/` with the `ast` module and lists imports outside the standard library, NumPy and Matplotlib, so that each is a conscious choice. The report informs and never blocks. Acceptance: `grad_check` returns below 1e-6 on f(x) = sum(x**3).


---

# D1. Discrete Mathematics and Mathematical Reasoning

## A1.1. Logic, proof paradigms and formal languages
*Covers unit U1.1. Source weeks absorbed: DM W1, o; HEM W1–2, o; IM o.* *Total: 10 marks.*

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

## A1.2. Counting, generating functions and combinatorics
*Covers unit U1.2. Source weeks absorbed: DM W2–3; IM A.* *Total: 10 marks.*

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

## A1.3. Posets, lattices, Boolean algebra and switching circuits
*Covers unit U1.3. Source weeks absorbed: DM W4; HEM W2–5.* *Total: 10 marks.*

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

## A1.4. Graph theory
*Covers unit U1.4. Source weeks absorbed: DM W5–7; HEM W5–8.* *Total: 10 marks.*

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

## A1.5. Number theory and cryptography
*Covers unit U1.5. Source weeks absorbed: DM W8–9; IM A.* *Total: 10 marks.*

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

## A1.6. Algebra: finite fields, codes, groups and orbit counting
*Covers unit U1.6. Source weeks absorbed: DM W10–12.* *Total: 10 marks.*

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

## A1.7. An invitation to mathematics: polynomials, functions, matrices, conservation laws
*Covers unit U1.7. Source weeks absorbed: IM o, A.* *Total: 10 marks.*

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


---

# D2. Single-Variable Calculus and Real Analysis

## A2.1. Numbers, countability, functions, limits and continuity
*Covers unit U2.1. Source weeks absorbed: CAL1 W1–2, o; PMO W1–2; OFF W1.* *Total: 10 marks.*

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

## A2.2. Differentiation and mean value theorems
*Covers unit U2.2. Source weeks absorbed: CAL1 W3–4; EM1 W1, o; AEMK W1; PMO W2.* *Total: 10 marks.*

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

## A2.3. Integration, applications and transcendental functions
*Covers unit U2.3. Source weeks absorbed: CAL1 W4–7; EM1 o; AEMK W2.* *Total: 10 marks.*

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

## A2.4. Taylor expansion, sequences, series and power series
*Covers unit U2.4. Source weeks absorbed: CAL1 W7–8; EM1 o; AEMK W1; MFML W9; PMO W2.* *Total: 10 marks.*

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

## A2.5. Improper integrals, Gamma and Beta functions, integrals dependent on parameters
*Covers unit U2.5. Source weeks absorbed: EM1 W5, o; AEMK W2.* *Total: 10 marks.*

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


---

# D3. Multivariable and Vector Calculus

## A3.1. Functions of several variables, partial derivatives and differentiability
*Covers unit U3.1. Source weeks absorbed: EM1 W2–3, o; AEMK W1, o; MFML W9; EMML W7; PMO W1–2; OMLH W1–2.* *Total: 10 marks.*

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

## A3.2. Taylor expansion in several variables, maxima, minima and Lagrange multipliers
*Covers unit U3.2. Source weeks absorbed: EM1 W4, o; AEMK W1; MFML W9.* *Total: 10 marks.*

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

## A3.3. Multiple integrals and their applications
*Covers unit U3.3. Source weeks absorbed: EM1 W6–7, o; AEMK W2.* *Total: 10 marks.*

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

## A3.4. Vector calculus: fields, line and surface integrals, Green, Gauss and Stokes
*Covers unit U3.4. Source weeks absorbed: EM2 W1–2, o; AEMK W9–11.* *Total: 10 marks.*

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

## A3.5. Matrix calculus, Jacobians and Hessians for machine learning
*Covers unit U3.5. Source weeks absorbed: MFML W10; EMML W7–8.* *Total: 10 marks.*

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


---

# D4. Linear Algebra: Core, Abstract, Numerical and Applied

## A4.1. Systems of linear equations, matrices, elimination, rank and inverses
*Covers unit U4.1. Source weeks absorbed: LAR W1–4, o; LAP W2,9; ALAB o, P1; EM1 W8, o; AEMK W6–7; EMML W1, o; MFML W1, o; ALAK W2; MLE W1; MLESA W0.* *Total: 10 marks.*

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

## A4.2. Vectors, vector spaces, subspaces, bases and dimension
*Covers unit U4.2. Source weeks absorbed: LAP W1–4, o; LAR W3; ALAB P1, P2; EM1 W8, o; AEMK W6; EMML W1; MFML W1; ALAK W1; ALAJ W1; PMO W1; OMLH W1–2.* *Total: 10 marks.*

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

## A4.3. Linear maps, representation by matrices, duality and quotient spaces
*Covers unit U4.3. Source weeks absorbed: LAP W5–8; LAR W5; ALAB P1, P2, o; EM1 W9, o; AEMK W6; MFML W2; EMML W2; PMO W1; ALAK W1.* *Total: 10 marks.*

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

## A4.4. Inner products, norms, orthogonality, projections and Gram–Schmidt
*Covers unit U4.4. Source weeks absorbed: LAR W6; ALAB P4; MFML W3; EMML W2,6; ALAK W1,3; ALAJ W1; PMO W1; AOW W1.* *Total: 10 marks.*

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

## A4.5. Determinants, multilinear forms and permutations
*Covers unit U4.5. Source weeks absorbed: LAP W10–12, o; LAR W4.* *Total: 10 marks.*

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

## A4.6. Eigenvalues, eigenvectors, similarity and diagonalization
*Covers unit U4.6. Source weeks absorbed: LAR W7–8; EM1 W10, o; AEMK W8; MFML W2; EMML W2; ALAJ W3; ALAB P3; LAP o.* *Total: 10 marks.*

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

## A4.7. Canonical forms: minimal polynomial, invariant subspaces, Jordan and rational forms
*Covers unit U4.7. Source weeks absorbed: ALAB o, P3; EMML W6; LAP W10.* *Total: 10 marks.*

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

## A4.8. Spectral theory: normal operators, symmetric matrices, quadratic forms, PSD matrices and kernels
*Covers unit U4.8. Source weeks absorbed: ALAB o, P4; MFML W3; EMML W3; PMO W1; OMLH W1–2; AOW W1; AEMK W8; ALAK W8, o.* *Total: 10 marks.*

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

## A4.9. LU, QR, conditioning, SVD, pseudo-inverse and low-rank approximation
*Covers unit U4.9. Source weeks absorbed: ALAK W2–4,9,12, o; ALAB P4, o; EMML W3,6; MFML W4; ALAJ W4; PMO W1; OMLH W1–2.* *Total: 10 marks.*

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

## A4.10. Least squares, regularized and constrained least squares
*Covers unit U4.10. Source weeks absorbed: ALAK W5–7, o; ALAJ W5–6; EMML W5; MFML W10.* *Total: 10 marks.*

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

## A4.11. Applications of linear algebra: PageRank, sparsity, dynamical systems, Markov chains, signal processing and data analytics
*Covers unit U4.11. Source weeks absorbed: ALAK W10–12, o; ALAJ W2–4,7–12, o; EMML W6; LAP o.* *Total: 10 marks.*

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


---

# D5. Probability and Stochastic Models

## A5.1. Probability foundations: from events to Bayes' theorem
*Covers unit U5.1. Source weeks absorbed: IPS W1–2, o; PSS W3, o; MFML W5, o; AEMA W9, o; EMML W10; SMLM W2; MLE W2; MLESA W0; S50 D2.* *Total: 10 marks.*

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

## A5.2. Random variables, distributions and moments
*Covers unit U5.2. Source weeks absorbed: IPS W2–3, o; MFML W6; PSS W4; SMLM W2; EMML W10–11; S50 D1, D3.* *Total: 10 marks.*

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

## A5.3. Special discrete distributions and the Poisson process
*Covers unit U5.3. Source weeks absorbed: IPS W3–4; AEMA W9–10; PSS W4; EMML W11; SMLM W3; S50 D3.* *Total: 10 marks.*

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

## A5.4. Special continuous distributions and the normal distribution
*Covers unit U5.4. Source weeks absorbed: IPS W4–5; AEMA W10–11; PSS W4; SMLM W3; EMML W11; S50 D3.* *Total: 10 marks.*

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

## A5.5. Functions of random variables, transformations and order statistics
*Covers unit U5.5. Source weeks absorbed: IPS W6–7.* *Total: 10 marks.*

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

## A5.6. Joint distributions, conditioning, covariance and multivariate normal
*Covers unit U5.6. Source weeks absorbed: IPS W6–7; MFML W7–8; AEMA W11, o; SMLM W4–5; EMML W11; MLCE W2; S50 D2, D6; AOW W1.* *Total: 10 marks.*

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

## A5.7. Limit theorems and concentration inequalities
*Covers unit U5.7. Source weeks absorbed: MFML W8; BAN W6; S50 D4.* *Total: 10 marks.*

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

## A5.8. Markov chains, queueing theory and reliability
*Covers unit U5.8. Source weeks absorbed: HEM W11–12, o; AEMA W12, o; ALAJ W12; DOML W8.* *Total: 10 marks.*

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

## A5.9. Conditional expectation and martingales
*Covers unit U5.9. Source weeks absorbed: SA W2–3, o.* *Total: 10 marks.*

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


---

# D6. Statistics and Statistical Inference

## A6.1. Data, descriptive statistics and measures of association
*Covers unit U6.1. Source weeks absorbed: PSS W1–2, o; IPS W8–9; SMLM W1, o; MLCE W1; S50 D1.* *Total: 10 marks.*

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

## A6.2. Sampling distributions and point estimation
*Covers unit U6.2. Source weeks absorbed: IPS W8–10; S50 D4.* *Total: 10 marks.*

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

## A6.3. Confidence intervals and hypothesis testing
*Covers unit U6.3. Source weeks absorbed: IPS W10–12; AEMA W12, o; S50 D4, D5.* *Total: 10 marks.*

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

## A6.4. Correlation, regression and multivariate analysis
*Covers unit U6.4. Source weeks absorbed: AEMA W11–12; SMLM W6–7; MLCE W2; MLESA W2; S50 D6, D7; MFML W8.* *Total: 10 marks.*

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

## A6.5. Bayesian inference and MCMC
*Covers unit U6.5. Source weeks absorbed: S50 D8, D9; MLESA W5; MLE W4,11; SMLM o.* *Total: 10 marks.*

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

## A6.6. Forecasting with statistical and machine-learning models: hydrology and water-resources applications
*Covers unit U6.6. Source weeks absorbed: SMLM W1,12, o.* *Total: 10 marks.*

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


---

# D7. Differential Equations, Dynamical Systems, Numerical Methods, Complex Analysis and Transforms

## A7.1. First- and higher-order ordinary differential equations
*Covers unit U7.1. Source weeks absorbed: EM1 W11–12, o; AEMK W3; MM W3.* *Total: 10 marks.*

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

## A7.2. Numerical analysis: iteration, root finding, interpolation and quadrature
*Covers unit U7.2. Source weeks absorbed: EM2 W5–6, o; AEMK W4–5.* *Total: 10 marks.*

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

## A7.3. Complex variables: analytic functions and complex integration
*Covers unit U7.3. Source weeks absorbed: EM2 W3–4, o; AEMK W12; AEMA W1–3, o.* *Total: 10 marks.*

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

## A7.4. Series, singularities, residues, real integrals and conformal mapping
*Covers unit U7.4. Source weeks absorbed: EM2 W4, o; AEMK W12; AEMA W3–7, o.* *Total: 10 marks.*

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

## A7.5. Laplace, Z, Fourier and discrete Fourier transforms
*Covers unit U7.5. Source weeks absorbed: EM2 W7–12, o; AEMA W7–9, o; ALAJ W8.* *Total: 10 marks.*

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

## A7.6. Mathematical modelling: discrete and continuous dynamical systems
*Covers unit U7.6. Source weeks absorbed: MM W1–4, o; LAR W7.* *Total: 10 marks.*

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

## A7.7. ODE theory for dynamical systems: Gronwall, limit sets, invariant sets and chain transitivity
*Covers unit U7.7. Source weeks absorbed: SA W4, o.* *Total: 10 marks.*

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


---

# D8. Optimization: Theory, Algorithms and Applications

## A8.1. Optimization problems: formulation, history, transformations and basic facts
*Covers unit U8.1. Source weeks absorbed: PMO W1, o; OAT W1–3, o; OFF W1–4, o; OMLH W3, o; MFML W10; MLE W3; EMML W8–10, o; CVX o; MLESA W0.* *Total: 10 marks.*

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

## A8.2. Convex sets, cones, polyhedra and separation
*Covers unit U8.2. Source weeks absorbed: PMO W3; CVX o, L1-9; AOW W2; EMML W8; LPCS W1–5, o; OFF W4; DOML W1.* *Total: 10 marks.*

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

## A8.3. Convex functions and their calculus
*Covers unit U8.3. Source weeks absorbed: PMO W3–4; CVX L1-9, L10-19; AOW W3; EMML W8; DOML W1–2; OMLH W3; MLESA W0.* *Total: 10 marks.*

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

## A8.4. Unconstrained optimization theory
*Covers unit U8.4. Source weeks absorbed: PMO W4–5; OMLH W3; OFF W2–3; CVX L20-26.* *Total: 10 marks.*

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

## A8.5. Constrained optimization theory: Lagrange, cones, Fritz John and KKT
*Covers unit U8.5. Source weeks absorbed: PMO W8–9; CVX L10-19, o; DOML W2–3; AOW W6; EMML W12; MFML W10.* *Total: 10 marks.*

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

## A8.6. Lagrangian duality, saddle points and minimax
*Covers unit U8.6. Source weeks absorbed: PMO W10; CVX o, L10-19; DOML W2–3,7; AOW W6; EMML W12; LPCS W4–6; OFF W6–7.* *Total: 10 marks.*

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

## A8.7. Linear programming: simplex, duality, sensitivity and interior-point methods
*Covers unit U8.7. Source weeks absorbed: CVX L10-19, L20-26, L27-33, o; HEM W9–10, o; LPCS W1–3,7–8, o; OFF W5–7; OAT W9–11; AOW W4; EMML W11; MFML W10.* *Total: 10 marks.*

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

## A8.8. Unconstrained descent methods: line search, gradient, Newton, quasi-Newton, conjugate gradient, trust region
*Covers unit U8.8. Source weeks absorbed: PMO W5–8; OAT W3–6; OMLH W4,7–8; OFF W10–11; EMML W9–10; MFML W10; FML W4; DOML W3.* *Total: 10 marks.*

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

## A8.9. Constrained optimization algorithms: QP, projected and reduced gradient, penalty, augmented Lagrangian, SQP
*Covers unit U8.9. Source weeks absorbed: PMO W11–12; OAT W7–8; OFF W10–11; DOML W6; OMLH W5–6.* *Total: 10 marks.*

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

## A8.10. First-order methods for ML: stochastic, accelerated, proximal, adaptive, and the dynamical-systems view
*Covers unit U8.10. Source weeks absorbed: OMLH W5–8; DOML W3–6; FML W4–5; MLCE W5; FDL W2; OAT W12; MFML W10; MLESA W5.* *Total: 10 marks.*

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

## A8.11. Conic and structured convex programs: QCQP, SOCP, SDP, geometric programs
*Covers unit U8.11. Source weeks absorbed: AOW W4–6,9, o; CVX o, L34-40; MLESA W0.* *Total: 10 marks.*

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

## A8.12. Applications of optimization: signal estimation, compressive sensing, radar, big data and finance
*Covers unit U8.12. Source weeks absorbed: AOW W2–12, o; EMML o; MLCE W4.* *Total: 10 marks.*

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

## A8.13. Non-smooth and difference-of-convex optimization
*Covers unit U8.13. Source weeks absorbed: CVX o, L34-40.* *Total: 10 marks.*

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

## A8.14. Distributed optimization: graphs, consensus, ADMM and dual decomposition
*Covers unit U8.14. Source weeks absorbed: DOML W1,7–10, o; MFML o.* *Total: 10 marks.*

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

## A8.15. Dynamic optimization and complementarity problems
*Covers unit U8.15. Source weeks absorbed: OFF W8–9,12, o.* *Total: 10 marks.*

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

## A8.16. Stochastic approximation: algorithms, step sizes and the ODE method
*Covers unit U8.16. Source weeks absorbed: SA W1,5–6, o.* *Total: 10 marks.*

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

## A8.17. Convergence rates, stability, two-timescale algorithms and stochastic recursive inclusions
*Covers unit U8.17. Source weeks absorbed: SA W7–10, o.* *Total: 10 marks.*

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


---

# D9. Machine Learning Foundations: Supervised, Unsupervised, Probabilistic, Data Mining and Learning Theory

## A9.0. History of AI, symbolic AI and the machine-learning workflow
*Covers unit U9.0. Source weeks absorbed: GEN 2.1, 2.2, 2.3, 2.4, 2.5, 2.6.* *Total: 10 marks.*

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

## A9.1. What machine learning is: paradigms, data, hypothesis spaces and the statistical framework
*Covers unit U9.1. Source weeks absorbed: MLCE W1, o; MLDL W1, o; MLK W1–3, o; MLE W1–3, o; MLESA W1, o; FML W1, o; IMLK W1, o; SMLM W8–9; MFML W12; DMIN W1, o.* *Total: 10 marks.*

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

## A9.2. Model evaluation and selection: bias–variance, validation, tuning and metrics
*Covers unit U9.2. Source weeks absorbed: MLCE W3,6, o; MLDL W1; MLESA W1,7; MLE W4; IMLK W1; EMML W6; DMIN W7; SMLM W8.* *Total: 10 marks.*

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

## A9.3. Linear regression and linear classification: estimation, logistic and softmax regression, surrogate losses
*Covers unit U9.3. Source weeks absorbed: MLCE W2–4, o; MLDL W1,5; MLESA W2–3; MLE W4; FML W2–3; IMLK W2,5; SMLM W6; EMML W5; S50 D7.* *Total: 10 marks.*

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

## A9.4. Regularization and implicit regularization
*Covers unit U9.4. Source weeks absorbed: MLCE W3; MLDL W1; MLE W4; FML W6; MLESA W2; ALAK W7.* *Total: 10 marks.*

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

## A9.5. Perceptron, support vector machines and kernel methods
*Covers unit U9.5. Source weeks absorbed: MLDL W4; MLESA W4; FML W7–8; IMLK W5; MLCE W9–10; DMIN W4; MFML W4; EMML W11–12; MLE W9; ALAJ W5,11; SMLM W11.* *Total: 10 marks.*

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

## A9.6. Bayes decision theory, density estimation and probabilistic classifiers
*Covers unit U9.6. Source weeks absorbed: MLDL W2–3; MLESA W3,5,8; MLE W9; IMLK W4; DMIN W3; MLK W4; FML W12.* *Total: 10 marks.*

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

## A9.7. Decision trees and ensembles: bagging, boosting, random forests
*Covers unit U9.7. Source weeks absorbed: MLCE W8–10; MLDL W5–6; MLESA W6–8; MLE W9; IMLK W2,7; SMLM W10; DMIN W3; FML W12; MLK W4.* *Total: 10 marks.*

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

## A9.8. Dimensionality reduction and feature learning
*Covers unit U9.8. Source weeks absorbed: MLCE W7–8; MLDL W7; IMLK W3; EMML W3–4; MFML W4,10; MLESA W2; SMLM W7; DMIN W1; MLE o.* *Total: 10 marks.*

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

## A9.9. Clustering, mixture models and the EM algorithm
*Covers unit U9.9. Source weeks absorbed: MLCE W7–8; MLDL W8–9; MLESA W10–11; MLE W10; IMLK W8; DMIN W5; ALAJ W10; SMLM W11.* *Total: 10 marks.*

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

## A9.10. Probabilistic graphical models, hidden Markov models, inference and Gaussian processes
*Covers unit U9.10. Source weeks absorbed: MLESA W5,8–9; MLDL W2,5; MLE W11; MLCE W10; FML W11–12.* *Total: 10 marks.*

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

## A9.11. Instance-based learning, collaborative filtering and recommendation
*Covers unit U9.11. Source weeks absorbed: IMLK W3; DMIN W3; ALAJ W7.* *Total: 10 marks.*

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

## A9.12. Data mining: preprocessing, association rules, sequence mining, outliers and case studies
*Covers unit U9.12. Source weeks absorbed: DMIN W1–2,5–8, o.* *Total: 10 marks.*

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

## A9.13. Learning theory: PAC, VC dimension, generalization and modern overparametrization
*Covers unit U9.13. Source weeks absorbed: IMLK W7, o; MLESA W12; FML W1,3,5,8–10,12; MLE o.* *Total: 10 marks.*

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

## A9.14. Symbolic and knowledge-based machine learning, tools and cognitive-science influences
*Covers unit U9.14. Source weeks absorbed: MLK W4–8, o.* *Total: 10 marks.*

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


---

# D10. Sequential Decision Making: Bandits and Reinforcement Learning

## A10.1. From batch to online learning: adversarial full-information and bandit settings
*Covers unit U10.1. Source weeks absorbed: BAN W1–4, o.* *Total: 10 marks.*

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

## A10.2. Stochastic bandits: regret notions, UCB, KL-UCB and lower bounds
*Covers unit U10.2. Source weeks absorbed: BAN W5–8, o.* *Total: 10 marks.*

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

## A10.3. Contextual bandits and pure exploration
*Covers unit U10.3. Source weeks absorbed: BAN W9–12, o.* *Total: 10 marks.*

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

## A10.4. Markov decision processes, dynamic programming and temporal-difference learning
*Covers unit U10.4. Source weeks absorbed: MLESA W12; MLK o; OFF W12.* *Total: 10 marks.*

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

## A10.5. Policy gradient, actor–critic and proximal policy optimization
*Covers unit U10.5. Source weeks absorbed: FDL W12; MFGAI W12.* *Total: 10 marks.*

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

## A10.6. Stochastic approximation in reinforcement learning
*Covers unit U10.6. Source weeks absorbed: SA W11–12, o.* *Total: 10 marks.*

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


---

# D11. Deep Learning Foundations

## A11.1. Perceptron, multilayer networks, activations and loss functions
*Covers unit U11.1. Source weeks absorbed: FDL W1, o; MFML W11; MLDL W10; MLE W5; MLESA W5; IMLK W6; MLCE W11; FML W9; MLK W6; GEN 2.7, 3.1, 3.2; SMLM W9,11.* *Total: 10 marks.*

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

## A11.2. Backpropagation and training deep networks
*Covers unit U11.2. Source weeks absorbed: FDL W2; MFML W11; GEN 2.7, 3.3; MLE W5; MLESA W5; MLDL W10; MLCE W11; FML W10.* *Total: 10 marks.*

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

## A11.3. Overfitting, regularization and generalization in deep networks
*Covers unit U11.3. Source weeks absorbed: FDL W2; GEN 2.8, 3.3; MLESA W5.* *Total: 10 marks.*

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

## A11.4. Convolutional neural networks and image representation
*Covers unit U11.4. Source weeks absorbed: FDL W3–4; MLE W6–7; MLDL W11; MLCE W11–12; CSO W1.* *Total: 10 marks.*

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

## A11.5. Explainable AI for deep models
*Covers unit U11.5. Source weeks absorbed: FDL W5.* *Total: 10 marks.*

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

## A11.6. Segmentation and object detection
*Covers unit U11.6. Source weeks absorbed: FDL W6; MLDL W12.* *Total: 10 marks.*

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

## A11.7. Recurrent networks: RNN, LSTM, GRU, backpropagation through time and attention in RNNs
*Covers unit U11.7. Source weeks absorbed: FDL W7–8; MLE W8; MLCE W12; MLDL W12; MLK W6; DLNLP W4.* *Total: 10 marks.*

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

## A11.8. Autoencoders and representation learning
*Covers unit U11.8. Source weeks absorbed: FDL W10; MLDL W12; MLE W12; MLCE W8; GEN 2.6.* *Total: 10 marks.*

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


---

# D12. Natural Language Processing, the Transformer and Large Language Models

## A12.1. NLP foundations and the classical NLP pipeline
*Covers unit U12.1. Source weeks absorbed: GEN 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7; DLNLP W1, o; FDL W9.* *Total: 10 marks.*

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

## A12.2. Word representations and multilingual embeddings
*Covers unit U12.2. Source weeks absorbed: DLNLP W2–3; FDL W9; GEN 1.2; MFGAI o.* *Total: 10 marks.*

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

## A12.3. Attention and the Transformer architecture
*Covers unit U12.3. Source weeks absorbed: GEN 3.4, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7; DLNLP W5; FDL W11; FML W9.* *Total: 10 marks.*

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

## A12.4. Pretraining, self-supervised learning and the LLM landscape
*Covers unit U12.4. Source weeks absorbed: GEN 5.1; DLNLP W6–7, o; FDL W11–12; MFGAI W10, o.* *Total: 10 marks.*

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

## A12.5. Scaling laws, LLM architectures and long context
*Covers unit U12.5. Source weeks absorbed: DLNLP W9,11; CSO W5.* *Total: 10 marks.*

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

## A12.6. Decoding strategies and sampling
*Covers unit U12.6. Source weeks absorbed: GEN 5.3, 6.2; MFGAI W11.* *Total: 10 marks.*

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

## A12.7. Prompting: fundamentals, APIs and advanced techniques
*Covers unit U12.7. Source weeks absorbed: GEN 5.2, 5.4, 6.1, 6.3, 6.4; DLNLP W9; FDL W11.* *Total: 10 marks.*

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

## A12.8. Instruction tuning, RLHF and alignment: PPO and DPO
*Covers unit U12.8. Source weeks absorbed: DLNLP W8, o; MFGAI W12; FDL W12; GEN 5.1.* *Total: 10 marks.*

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

## A12.9. Parameter-efficient fine-tuning: LoRA and QLoRA
*Covers unit U12.9. Source weeks absorbed: DLNLP W10; FDL W11.* *Total: 10 marks.*

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

## A12.10. Prompt optimization, compression and prompt security
*Covers unit U12.10. Source weeks absorbed: GEN 7.1, 7.2, 7.4, 7.5.* *Total: 10 marks.*

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


---

# D13. Deep Generative Models

## A13.1. Probabilistic deep generative modelling: foundations and taxonomy
*Covers unit U13.1. Source weeks absorbed: MFGAI W1, o; FML W11, o; MLE W11.* *Total: 10 marks.*

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

## A13.2. Generative modelling via variational divergence minimization
*Covers unit U13.2. Source weeks absorbed: MFGAI W2.* *Total: 10 marks.*

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

## A13.3. Generative adversarial networks: formulation, training, WGAN and applications
*Covers unit U13.3. Source weeks absorbed: MFGAI W3–4, o; MLDL W12; MLE W12; FDL W12.* *Total: 10 marks.*

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

## A13.4. Variational autoencoders, improvements and VQ-VAE
*Covers unit U13.4. Source weeks absorbed: MFGAI W5–6; FDL W12; MLE W12.* *Total: 10 marks.*

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

## A13.5. Autoregressive models
*Covers unit U13.5. Source weeks absorbed: MFGAI W10, o.* *Total: 10 marks.*

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

## A13.6. Energy-based and score-based models; Langevin sampling
*Covers unit U13.6. Source weeks absorbed: FML W11; MFGAI W9; MLE W11.* *Total: 10 marks.*

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

## A13.7. Denoising diffusion probabilistic models, conditional diffusion and Stable Diffusion
*Covers unit U13.7. Source weeks absorbed: MFGAI W7–9, o; FDL W12.* *Total: 10 marks.*

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

## A13.8. Normalizing flows (gap-fill from the references)
*Covers unit U13.8. Source weeks absorbed: gap-fill unit (references).* *Total: 10 marks.*

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


---

# D14. Retrieval-Augmented Generation and Agentic Systems

## A14.1. Why RAG, RAG architecture and classical retrievers
*Covers unit U14.1. Source weeks absorbed: GEN 8.1, 8.2, 8.3; DLNLP W11.* *Total: 10 marks.*

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

## A14.2. RAG failure modes, types of RAG and assessment
*Covers unit U14.2. Source weeks absorbed: GEN 8.4, 8.5, 8.6.* *Total: 10 marks.*

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

## A14.3. Sparse retrieval limits and dense representations
*Covers unit U14.3. Source weeks absorbed: GEN 9.1, 9.2.* *Total: 10 marks.*

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

## A14.4. Learning retrieval-oriented embeddings and choosing an embedding model
*Covers unit U14.4. Source weeks absorbed: GEN 9.3, 9.4.* *Total: 10 marks.*

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

## A14.5. Document processing and chunking
*Covers unit U14.5. Source weeks absorbed: GEN 9.5, 9.6.* *Total: 10 marks.*

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

## A14.6. Vector databases and indexes: KNN, IVF, PQ, HNSW, FAISS and ChromaDB
*Covers unit U14.6. Source weeks absorbed: GEN 9.7, 10.1, 10.2.* *Total: 10 marks.*

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

## A14.7. The retrieval pipeline: bi-encoder, cross-encoder, ColBERT and two-stage retrieval
*Covers unit U14.7. Source weeks absorbed: GEN 10.3.* *Total: 10 marks.*

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

## A14.8. Production RAG: request shaping, query transformation, routing, security, cost and observability
*Covers unit U14.8. Source weeks absorbed: GEN 10.4, 10.5, 10.6, 10.7.* *Total: 10 marks.*

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

## A14.9. Limits of single-shot RAG and the move to agents
*Covers unit U14.9. Source weeks absorbed: GEN 10.8, 11.1.* *Total: 10 marks.*

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

## A14.10. Agent basics, tool calling and orchestration
*Covers unit U14.10. Source weeks absorbed: GEN 11.2, 11.3.* *Total: 10 marks.*

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

## A14.11. Planning with ReAct
*Covers unit U14.11. Source weeks absorbed: GEN 11.4.* *Total: 10 marks.*

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

## A14.12. State machines and LangGraph
*Covers unit U14.12. Source weeks absorbed: GEN 11.5.* *Total: 10 marks.*

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

## A14.13. Agentic memory
*Covers unit U14.13. Source weeks absorbed: GEN 11.6.* *Total: 10 marks.*

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

## A14.14. Provenance and citations
*Covers unit U14.14. Source weeks absorbed: GEN 11.7.* *Total: 10 marks.*

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

## A14.15. Multi-agent architecture summary, error handling and best practices
*Covers unit U14.15. Source weeks absorbed: GEN 11.8.* *Total: 10 marks.*

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


---

# D15. Evaluation, Safety and Responsible AI

## A15.1. LLM evaluation: metric architecture and reference-based metrics
*Covers unit U15.1. Source weeks absorbed: GEN 7.3, 12.1, 12.2; FDL W12.* *Total: 10 marks.*

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

## A15.2. LLM-as-a-judge and factuality
*Covers unit U15.2. Source weeks absorbed: GEN 12.3.* *Total: 10 marks.*

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

## A15.3. AI safety foundations and threat models
*Covers unit U15.3. Source weeks absorbed: GEN 12.4, 12.5, 12.6.* *Total: 10 marks.*

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

## A15.4. White-box attacks and prompt injection
*Covers unit U15.4. Source weeks absorbed: GEN 12.7.* *Total: 10 marks.*

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

## A15.5. Black-box attacks and the jailbreak taxonomy
*Covers unit U15.5. Source weeks absorbed: GEN 12.8, 12.9.* *Total: 10 marks.*

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

## A15.6. Defense, interpretability and ethics
*Covers unit U15.6. Source weeks absorbed: GEN 12.10; DLNLP W12; FDL W5.* *Total: 10 marks.*

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


---

# D16. ML Systems, Efficiency and Distributed and Federated Learning

## A16.1. CNN computation and accelerators
*Covers unit U16.1. Source weeks absorbed: CSO W1–3,10–12, o.* *Total: 10 marks.*

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

## A16.2. Parallelism for training, communication and fault tolerance
*Covers unit U16.2. Source weeks absorbed: CSO W4,8; DOML W10.* *Total: 10 marks.*

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

## A16.3. LLM decoding, memory management and serving infrastructure
*Covers unit U16.3. Source weeks absorbed: CSO W5–7, o; MFGAI W11.* *Total: 10 marks.*

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

## A16.4. Model compression and quantization
*Covers unit U16.4. Source weeks absorbed: FDL W12; MFGAI W11; CSO o.* *Total: 10 marks.*

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

## A16.5. Graph neural network inference systems
*Covers unit U16.5. Source weeks absorbed: CSO W9, o.* *Total: 10 marks.*

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

## A16.6. Federated learning
*Covers unit U16.6. Source weeks absorbed: DOML W11–12.* *Total: 10 marks.*

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


---

# D17. Approximation Algorithms and Computational Complexity

## A17.1. Review of NP-completeness and the approximation framework
*Covers unit U17.1. Source weeks absorbed: AA W1, o.* *Total: 10 marks.*

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

## A17.2. Approximation for vertex cover, set cover and the traveling salesman problem
*Covers unit U17.2. Source weeks absorbed: AA W2.* *Total: 10 marks.*

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

## A17.3. Approximation for the knapsack problem and job scheduling
*Covers unit U17.3. Source weeks absorbed: AA W3.* *Total: 10 marks.*

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

## A17.4. Linear programming basics and deterministic rounding
*Covers unit U17.4. Source weeks absorbed: AA W4–6.* *Total: 10 marks.*

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

## A17.5. Randomized rounding
*Covers unit U17.5. Source weeks absorbed: AA W7–8.* *Total: 10 marks.*

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

## A17.6. The primal–dual method
*Covers unit U17.6. Source weeks absorbed: AA W9–10.* *Total: 10 marks.*

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

## A17.7. Semidefinite programming for max cut, and hardness of approximation
*Covers unit U17.7. Source weeks absorbed: AA W11–12.* *Total: 10 marks.*

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
