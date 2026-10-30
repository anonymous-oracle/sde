# The Math of ML strand: roadmap, school bridge and record

Opened 27 Oct 2026 on the learner's instructions in chat. Restored 29 Oct 2026 after a project resync removed the first copy.

**Read first, every session in this strand and after any compaction:** `gcp-lite/ml-math/Rule_bridge_before_ml.md` (the standing rule: the school bridge is taught right before the ML topic that needs it), then `index/00_learning_method.md`, then this file.

1. (27 Oct) "start teaching the math of ml using the teaching philosophy provided. I require from the scratch implementation exercises in python too wherever appropriate."
2. (27 Oct) "You would need to consolidate high school, 11th and 12th grade basics required for each of these concepts and teach them together. But all of this with the philosophy of developing JEE advanced level intuition and problem solving capabilities - I do not mean the JEE advanced syllabus, but the problem solving capacity that is required/built for it. Ensure you understand the teaching philosophy present in the by ingesting them."
3. (29 Oct) "How about teaching the required bridge right before the ML topic. That way we will be doing both. In fact record create a single file for this rule so that it can stick to the session." Recorded in the rule file above.

Precedence applies (explicit instruction, then preferences, then `index/00_learning_method.md`). This strand **pauses Python concept 48** (parameters and scope); the tracker's resume point is unchanged. **Override recorded for Part 01:** its rules file makes school foundations remedial and on demand; for this strand the learner has asked for them to be taught systematically, so the Class 9 to 12 content each unit needs is taught in a bridge right before the ML topic that uses it (a diagnostic is still woven in, and a fluently handled topic is not re-taught). Fold both into the tracker (override 15 and an "On hold" line) at the close of Unit 1, per override 10.

## What was ingested, and how it operates here

Read: the Learning method; Parts 01, 03, 03b, 04 and 19 (rules and topic lists); the index map and progress file; the tracker; the Exercise Rules; the `learn` skill.

- **Three ways at once, tied together**: intuition (why it must be so), formalism (definition, theorem, derivation), practice (build, measure). Theory predicts, practice measures, the gap is where understanding is tested.
- **The JEE-aptitude strand of the method (Part 04 and the method's problem-solving philosophy)**, which is what the learner asked for: a few master ideas per domain with formulas derived once, then recognised; choose the frame before computing; multi-concept problems where the hard part is recognising the governing principle; sanity before and after (units, sign, limiting and special cases, order of magnitude, monotonicity); approximation with known error; several routes to one answer, with a second independent route as the check; triage under time; productive struggle before any hint; an error log by cause (conceptual, misread, slip, strategic) with cold re-attempts at about 1, 3 and 7 days; a heuristics catalogue (the tracker holds nine entries; entries here continue from 10).
- **Not the JEE syllabus.** The strand teaches the part of Class 9 to 12 mathematics that machine learning consumes, trained at JEE Advanced difficulty. Syllabus items with no ML use (for example hyperbola chord properties, skew-line shortest distance, circular permutations) are not pulled in here; they stay in Part 01 and Part 03b and are reached in index order.
- **Method rules that bind every turn**: short turns (about 120 to 200 words of teaching and at most one table or worked example); exactly one check, with expected right and wrong answers written first and never answered in the same turn; every term defined in one line the first time; no text-drawn diagrams; no ready-made code (override 6); exercises one per 3 to 5 concepts, judged on functional logic, no prediction needed (overrides 9 and 14); predict, run, explain the gap; an unanswered check is reworded and made smaller, never repeated word for word; stop when it is understood.

## How a unit runs (the braid)

Each ML unit is one braid, in this order, so the school mathematics arrives exactly when its first use is a step away and is never taught cold (standing rule in `Rule_bridge_before_ml.md`).

1. **Bridge**: the Class 9 to 12 topics the next ML concept needs, written as a prerequisite chain down to L0, each link verified through the woven checks. Taught with the JEE habit named for that block, so the topic is learned as a tool.
2. **ML concept**: the mechanism, the central result derived with every step.
3. **Build**: one small from-scratch exercise in pure Python (rule 1 below).
4. **Academic pass**: formal statements, the central proof, a problem set with one proof or derivation problem and one computational problem (key written before it is sent).
5. **The ramp**: rungs 6 to 10 of the ten-rung ramp. Rung 8 (mixed transfer) uses the new idea plus exactly two earlier mastered ideas, named in advance. **Rung 9 is a JEE Advanced style multi-concept problem fusing a bridge topic with the ML idea**; after it, the key insight, how it could have been found sooner and the cue that will trigger it next time go into the heuristics catalogue. Rung 10 is a reflection ending in a one-line decision record.

Training cadence across units: a short mixed set of earlier problems most sessions, interleaved; one long problem with no hints each week; timed mixed sets as speed training only (never a pacing rule); every solved problem re-solved by a second route.

## The school bridge matrix

Classes are NCERT-style placements recalled from memory, not checked against a current syllabus; they are labels for depth, not a pacing rule. The matrix is a default order; the standing rule lets a topic move earlier when it is needed earlier.

| School topic (Class) | First needed in | The ML use | JEE-style move trained |
|---|---|---|---|
| Linear and simultaneous equations (9, 10) | U1 | finding w and b from two points | elimination against substitution; check by plugging back |
| Functions, graphs, transformations, composition, inverse, even and odd, periodic (11) | U1 onward | a model is a function; a network is composition; sigmoid symmetry | sketch before computing; read symmetry first |
| Straight lines: slope forms, angle between lines, distance from a point to a line (10, 11) | U1 | rate of change; decision boundary in 2-D | choose the frame; special cases |
| Coordinate geometry: distance, section, midpoint, centroid (9, 10, 11) | U1 | Euclidean norm; interpolation | choose coordinates that kill terms |
| Trigonometry: ratios, unit circle, identities, addition formulas, cosine rule (10, 11) | U1, U2 | a·b = ‖a‖‖b‖cos θ; rotation matrices | special angles and limits as checks; identity as invariant |
| Vectors and 3-D geometry: dot and cross products, projection, direction cosines, triple product, lines and planes, point-to-plane distance (12) | U1, U3 | hyperplanes, margins, projection as regression | two routes: coordinates against vectors |
| Σ notation, AP and GP, infinite geometric series (10, 11) | U1, U4 | sums over data; gradient-descent error shrinking by a ratio r each step | closed form from small cases; convergence needs \|r\| < 1 |
| Inequalities, modulus; AM–GM, Cauchy–Schwarz, triangle inequality (11, and JEE standard) | U1, U9 | cosine similarity lies in [−1, 1]; convexity bounds | bound first, then find the equality case |
| Quadratics: completing the square, vertex, discriminant (10, 11) | U3 | one-parameter least squares is a parabola | D ≥ 0 as a bound; vertex without calculus |
| Polynomials, remainder and factor theorems, Vieta (10, 11) | U8 | characteristic polynomial: trace is the sum of roots, determinant the product | symmetric functions of roots |
| Sets, relations and functions; one-one and onto (11, 12) | U5 | events; invertibility | counting by bijection |
| Permutations, combinations, binomial theorem (11) | U5, U4 | counting outcomes; binomial law; (1 + x)ⁿ ≈ 1 + nx | complementary counting; approximation with known error |
| Mathematical induction (11) | U2, U10 | Aⁿ; layer-by-layer recursion | guess from small cases, then prove |
| Complex numbers: modulus, argument, Argand plane, de Moivre (11) | U2, U8 | multiplication as rotate-and-scale; eigenvalues of rotations | geometric reading of an algebraic identity |
| Conics: ellipse, axes, tangency (11) | U8, U9 | loss level sets and covariance ellipses; principal axes | tangency as a double root |
| Matrices and determinants: operations, transpose, symmetric and skew, 2 × 2 and 3 × 3 determinants, adjoint, inverse, Cramer's rule, consistency of linear systems (12) | U2, U3 | layers as matrices; solving the normal equations | use properties to avoid expanding |
| Limits, continuity, differentiability (11, 12) | U4 | the derivative as the object gradient descent uses | standard limits; one-sided checks |
| Derivatives: product, quotient, chain, implicit, parametric, higher order (12) | U4, U10 | gradients, backpropagation | structure of a composition before differentiating |
| Applications: tangent and normal, monotonicity, extrema, Rolle and the mean value theorem, differentials and linear approximation (12) | U4, U9 | a small step against the gradient lowers a smooth function (first-order Taylor); minima | sketch from f′ and f″; approximation with known error |
| Exponential and logarithm: laws, e, derivatives (11, 12) | U4, U6, U7 | sigmoid; log-likelihood; entropy | the log turns products into sums |
| Integration: definite integrals, area (12) | U5 | probability densities; expectation | symmetry to avoid integrating |
| First-order differential equations: separable, linear (12) | U4, U9 | gradient flow; learning rate as an Euler step | model the process, then solve |
| Statistics: mean, variance, standard deviation (11) | U3, U5 | regression slope as covariance over variance | invariance under shift and scale |
| Probability: conditional, total probability, Bayes, independence, random variable, mean, variance, binomial (11, 12) | U5, U6 | Bayes classifier; expected loss | conditioning traps; indicator variables; recursion on states; simulate to check |
| Series: e^x, ln(1 + x), binomial series (11, 12) | U11, U4 | log1p and cancellation; local approximations | keep the size of the neglected term |
| Number systems (done in Computer Organization: binary, two's complement) | U11 | floating point builds on it | none new |

Beyond school and taught inside the unit: partial derivatives, gradient, Jacobian and Hessian; Lagrange multipliers; eigen-decomposition and SVD; the multivariate Gaussian; maximum likelihood; Jensen's inequality in general form; matrix calculus.

## Rules specific to this strand

1. **From-scratch Python, pure first.** Exercises use only what has been taught in Python (lists, loops, functions, classes, exceptions, strings). Comprehensions, `lambda`, generators and NumPy are not yet taught; each is introduced just in time with a one-line definition. NumPy enters only as the oracle the learner's own code is checked against (hand-built first, then the library, naming what it handled that the toy did not). The learner's `.ml-venv` already holds NumPy, SciPy, scikit-learn and Matplotlib. Exercise files go in `ml-math/` beside `language-theory/`, one folder per exercise.
2. **Exercise rule (overrides 6, 9, 14).** One small exercise per 3 to 5 concepts; the task is described in words; no runnable code from the tutor, syntax only as a pattern with blanks; no written prediction needed; judged on functional logic, never on print wording. Derivations and concept checks keep their predictions.
3. **Two passes per unit**: engineering, then academic (item 4 of "How a unit runs").
4. **One running thread**: fit a line to data. Each unit extends it.
5. **Floating point** is pulled forward the first time a float result surprises the learner (the tracker's standing item).
6. **Cloud lens**: none for pure mathematics. Honest counterparts later: BigQuery ML linear and logistic regression after Units 3 and 6 (verify in current documentation; billing-gated, parked).
7. **Numbering**: concepts in this strand are numbered M1, M2, ... so the Python numbering (next: 48) is untouched.
8. Pacing: about 3 to 5 concepts per session at full depth; every session closes with states, recalls scheduled, misconception register and the exact resume point.
9. **Benchmarks (named, not linked; titles recalled, not checked)**: Deisenroth, Faisal and Ong, *Mathematics for Machine Learning* (2020); Strang, *Introduction to Linear Algebra* and MIT 18.06; Boyd and Vandenberghe, *Convex Optimization* (2004); Bishop, *Pattern Recognition and Machine Learning* (2006), chapters 1 and 2; Murphy, *Probabilistic Machine Learning: An Introduction* (2022); Goodfellow, Bengio and Courville, *Deep Learning* (2016), Part I; Cover and Thomas, *Elements of Information Theory*, 2nd edition; Stanford CS229 review notes. For the JEE-style layer the bar is the course's own Part 04 contest toolkit and the Part 03b depth bar (JEE Advanced problem fluency in calculus and coordinate geometry).

## Units

| # | Unit | Central result to derive | From-scratch build (pure Python) | Library afterwards |
|---|---|---|---|---|
| 1 | Vectors | a·b = ‖a‖‖b‖cos θ; Cauchy–Schwarz; a linear model's prediction is a dot product; distance from a point to a hyperplane | vector add, scale, dot, norm, cosine similarity; brute-force nearest neighbour | NumPy arrays |
| 2 | Matrices as maps | composition of linear maps is the matrix product; (AB)ᵀ = BᵀAᵀ; rank; inverse; determinant as volume scale | matmul by three loops; transpose; a Matrix class; determinant by elimination | NumPy `@`, broadcasting |
| 3 | Systems and least squares | normal equations XᵀXθ = Xᵀy derived two ways (projection and calculus) | Gaussian elimination with pivoting; regression through the normal equations | `numpy.linalg.lstsq`, scikit-learn |
| 4 | Calculus for learning | chain rule; first-order Taylor, so a small step against the gradient lowers a smooth function; gradient, Jacobian, Hessian | finite-difference gradient check; gradient descent in 1-D then 2-D; regression by gradient descent matching Unit 3 | none (autodiff arrives in Unit 10) |
| 5 | Probability | Bayes' rule from the definition; linearity of expectation; variance; LLN and CLT (statements, proof sketches) | samplers, Monte Carlo, naive Bayes | NumPy random |
| 6 | Likelihood | Gaussian noise makes maximum likelihood equal least squares; Bernoulli makes it cross-entropy; the logistic gradient σ(z) − y; ridge as MAP; bias-variance | logistic regression by gradient descent with a gradient check; ridge polynomial fit | scikit-learn |
| 7 | Information | entropy, cross-entropy, KL; Gibbs' inequality | entropy, cross-entropy, KL, calibration bins | none |
| 8 | Eigen and SVD | spectral theorem; PCA as variance maximization; SVD and low-rank approximation | power iteration, deflation, PCA | `numpy.linalg.eigh`, `svd`, scikit-learn PCA |
| 9 | Optimization | convexity (local = global); gradient-descent rate against the condition number; SGD, momentum, Adam; Lagrange and KKT; Newton | SGD, momentum, Adam, coordinate descent for the lasso | scikit-learn, SciPy |
| 10 | Backpropagation | chain rule over a computation graph; matrix-calculus gradients of an MLP | scalar autodiff engine; an MLP that solves XOR, gradient-checked | PyTorch autograd |
| 11 | Numerical computing | IEEE 754; cancellation; log-sum-exp; stable softmax; conditioning | Kahan sum; stable softmax and cross-entropy; ill-conditioned (Hilbert) system | NumPy, SciPy |
| C | Capstone | long unseen problem set at qualifying-examination level, a written report and an oral defence; or one classic result reproduced at toy size with its evaluation critiqued | by the learner alone; the tutor reviews, never writes | |

Order is a dependency order. Units 2 to 11 are unpacked into sub-blocks when reached (method: "unpack before teaching").

## Unit 1 unpacked (scope written before teaching)

Problem it solves: a prediction is a weighted sum, and "how alike are two things" is an angle. Both are dot products; the geometry that makes that true is Class 10 to 12 mathematics.

| Block | Bridge (school), taught right before the concept | Concept | JEE habit named | Build |
|---|---|---|---|---|
| 1a | functions, graphs, lines, slope as rate of change, two-point form | M1: a model is a rule with adjustable numbers; weight and bias; signed error; why one line must be chosen among many | read the structure of the data before computing; second point as the check | `predict` as a function; fit a line through two points |
| 1b | coordinates, distance, midpoint and section formulas | distance in 2-D and then n-D; the norm | choose the frame | norm |
| 1c | right-triangle ratios, unit circle, sin²θ + cos²θ = 1, cos(A − B), cosine rule, radians | angle between two directions | special angles and limits as checks | none |
| 1d | vectors in 2-D and 3-D: components, addition, scaling | dot product defined by components and by ‖a‖‖b‖cos θ, and the proof that they agree; projection; perpendicular means zero | two routes to one answer | dot, projection |
| 1e | lines and planes in 3-D, distance from a point to a plane | hyperplane w·x + b = 0 as a linear classifier; signed distance | sanity by special cases (a plane through the origin) | signed distance |
| 1f | inequalities: AM–GM, Cauchy–Schwarz by two proofs (the dot product, and the discriminant of a quadratic), triangle inequality | cosine similarity lies in [−1, 1]; when equality holds | bound first, then find the equality case | cosine similarity |
| 1g | none new | assemble: linear model as a dot product; nearest neighbour; the academic pass and the ramp | triage and a second method | vector library and brute-force nearest neighbour (the one exercise for 1d to 1g) |

Central result for the academic pass: a·b = ‖a‖‖b‖cos θ, derived two ways; Cauchy–Schwarz, proved two ways.

## Record

| Unit | State | Depth | Evidence |
|---|---|---|---|
| 1 | in progress (block 1a) | L1 | M1 passed; see below |
| 2 to 11, C | not started | none | none |

- **M1 (27 to 29 Oct), passed.** From an exact table, w = 3 and b = 10, with b given unasked (stepped back from area 1 to area 0). Linear equations (simultaneous) used unprompted for a line through two points: area-3 prediction 21 (correct). Second route (rate of change per unit area) shown by the tutor. Signed error defined as actual − predicted; for the line through rows 1 and 3 the miss at area 2 was given as "off by one" (size right; the sign, +1, was supplied). Woven L0 links verified: variables and a linear formula, solving two linear equations.
- **Learner's stated difficulty (28 Oct):** could not decide between techniques for a line through two points. Treated as a gap in the Class 10 to 11 straight-lines bridge, taught on 28 Oct (slope as rise over run, b = y₁ − w·x₁, choose by the x-gap, equations as the fallback).
- Misconception register: none yet. Wrong predictions: none. Error log for this strand: sign omitted on a signed error (slip; watch). Heuristics: none new yet (second route: rate of change against equations).
- **Open check (reworded and made smaller):** a line passes through (2, 7) and (6, 19); by how much does the price rise per extra unit of area? Expected: 3. Expected wrong: 4 (the x-gap), 12 (the rise, undivided), 1/3 (inverted).
- **Next ML step after the bridge:** the three pairs of rows (1,2), (1,3), (2,3) give three different lines, each missing a different row (signed misses −2, +1, −2); a rule is needed to choose among them. This leads toward least squares (Unit 3) and is the reason the line bridge was needed first.
- Resume point: Block 1a, the open check above.
