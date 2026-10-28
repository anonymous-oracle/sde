# Part 04 · Problem Solving, Reasoning & Research Method · TOPIC LIST

Rules and directives for this part: `index/part04_problem_solving.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Problem Solving, Reasoning & Research Method

### Problem-solving strategy

- **Pólya's four phases**: understand the problem (the unknown, the data, the condition); devise a plan; carry it out; look back (check the result, find a second route, reuse the method)
- **Heuristics for getting unstuck**
  - Work backwards from the goal; assume an intermediate lemma and prove it afterwards
  - Solve a smaller, simpler or special case; specialize, spot the pattern, then generalize
  - Introduce an auxiliary element, variable or construction
  - Draw a figure or build a table of small cases
  - Restate the problem in other words; drop or relax one condition and see what changes
  - Split into cases; find a related problem already solved and reuse its method or result
  - Guess, then verify or refute
- **Choosing the representation**: algebraic, geometric, graphical, combinatorial and probabilistic views of one problem; choosing coordinates or a frame of reference; transforming a problem into an equivalent easier one
- **Recognizing structure**: naming the governing principle before computing; problem archetypes and their standard moves; noticing what is unusual in the givens, since every given is usually needed

### Contest mathematics toolkit

- **Invariants and monovariants**: quantities preserved, or changing in one direction, under the allowed moves; colouring and parity arguments; termination proved by a strictly decreasing measure
- **The extremal principle**: reasoning from the largest, smallest or first object, or from a minimal counterexample
- **Symmetry**: reducing cases by symmetry; symmetric expressions; reflection arguments
- **Counting techniques**: double counting; counting by bijection; complementary counting; stars and bars; n identical objects into k boxes in C(n + k − 1, k − 1) ways, and C(n − 1, k − 1) ways when every box must hold at least one
- **Inequalities**: AM–GM, Cauchy–Schwarz, Jensen's inequality for convex functions, the rearrangement inequality; inequalities as tools for bounding and estimating; information inequalities: Gibbs' inequality D(p ‖ q) ≥ 0 for distributions p and q, the bound H(X) ≤ log n for n outcomes, and the data processing inequality I(X; Z) ≤ I(X; Y) along a Markov chain X → Y → Z
- **Sums and recurrences**: telescoping sums; generating functions; guessing a closed form from small cases and proving it by induction; the method of differences: write f(k) = g(k + 1) − g(k) so that Σf(k) telescopes to g(n + 1) − g(1), and build a difference table to sum a polynomial sequence
- **Functions and graphs in puzzles**: iterating a function; fixed points; modelling a puzzle as a graph
- **Probability reasoning**: conditioning traps (Monty Hall, base-rate neglect, Simpson's paradox); symmetry and linearity shortcuts for expectation; geometric probability
- **Power of a point**: for a point P and a circle with centre O and radius r, the power of P is OP² − r²; every line through P that meets the circle at A and B has PA · PB equal to the power, with signed lengths so that the sign shows whether P lies inside (negative) or outside (positive); from an external point the tangent length satisfies PT² = power; the locus of points with equal power to two circles is their radical axis, a line perpendicular to the line of centres, and the three radical axes of three circles meet at one point or are all parallel

### Physical and quantitative intuition

- **Dimensional analysis as a solution method**: deriving the form of a relation from the units of its inputs; dimensionless groups
- **Limiting and special cases**: zero, infinity, symmetric and degenerate configurations, used both to check an answer and to find it
- **Conservation and balance**: conserved quantities; flow balance (what enters equals what leaves at steady state) as the first equation to write
- **Approximation with known error**: (1 + x)ⁿ ≈ 1 + nx, ln(1 + x) ≈ x and √(1 + x) ≈ 1 + x/2 for small x; keeping track of the size of the neglected term
- **Scaling**: how an output changes when an input doubles; power laws as straight lines on log–log axes; doubling time and the rule of 72
- **Sketching before computing**: a function's graph from its zeros, asymptotes, monotonicity and convexity; singular points (cusps, corners and self-crossings), and tracing the full curve through its symmetry, asymptotes and the sign changes of f′ and f″
- **Mental arithmetic**: log₁₀ 2 ≈ 0.301, log₁₀ 3 ≈ 0.477, ln 2 ≈ 0.693, ln 10 ≈ 2.303, √2 ≈ 1.414, e ≈ 2.718; about 86,400 seconds in a day and 3.15 × 10⁷ in a year; multiplying by rounding and then correcting

### Speed and accuracy under time

- Triage: reading the whole set first; ranking items by tractability and payoff; two passes; knowing when to abandon an approach
- Checking an answer: special values, units and limits, back-substitution, an estimate of the answer's size made in advance
- Eliminating options in objective questions: extreme cases, dimensional mismatch, symmetry, sign
- Error analysis: an error log by cause (conceptual, misread, slip, strategic) and the practice that removes each cause
- Stamina and focus: long timed sets; recovering composure after a bad question

### Proof craft and mathematical maturity

- Writing a proof for a reader: the statement, the strategy, lemmas, the main argument, and what was used where
- Checking a proof: every step justified, every case covered, every hypothesis used; testing it on examples
- Counterexamples: built to refute a claim or to show that a hypothesis is needed
- Generalizing and sharpening: weaker hypotheses, stronger conclusions, the tight constant
- Reading a definition actively: examples, non-examples and edge cases

### Research method

- Reading a paper in three passes; annotating its claims, evidence and assumptions
- Mapping a literature: the lineage of ideas, the key results, the open problems
- Formulating a research question: novelty, significance and tractability; falsifiable hypotheses
- Experimental design and benchmark pitfalls: baselines, controls and ablations; confounders; variance across seeds and runs; error bars; leakage between training and test data; overfitting to a benchmark; cherry-picked results; unfair baselines
- Reproducing a claim at toy size or against one's own evaluation suite; reporting negative results
- Research writing: contribution statements, related work, threats to validity; giving a talk; peer review as reviewer and as author
- The qualifying-examination oral: defending a result under adversarial questions; saying "I don't know" and then reasoning toward an answer
- Domain-expert validation of outputs: an output is valid when the people who own the domain judge it correct under a written rubric fixed before judging; a sample drawn to cover the strata that matter, such as rare cases and each user group, not only at random; two or more experts rating blind; agreement between raters measured by Cohen's kappa for two raters or Fleiss' kappa for more, with disagreements settled by a named adjudicator; the error rate reported with its confidence interval and its failure categories shown with examples; the experts' own bias and time cost recorded as limits of the evidence

### Systems thinking

- Stocks and flows; reinforcing and balancing feedback loops; delays and the oscillation they cause
- Bottlenecks and the theory of constraints: the throughput of the whole is set by its tightest constraint
- Emergent behaviour and leverage points
- First-principles decomposition: reducing a problem to its fundamental constraints (physics, information, money, people) and rebuilding from them
- Inversion: asking what would guarantee failure, then avoiding it

### Learning science and deliberate practice

- Retrieval practice and the testing effect; spaced repetition and the forgetting curve; interleaved versus blocked practice; desirable difficulties
- Deliberate practice: specific goals, immediate feedback, work at the edge of ability
- Worked examples, cognitive load and the expertise-reversal effect
- Chunking and the pattern libraries of experts
- Self-explanation and the Feynman technique: explaining simply in order to find the gaps
- Metacognition: monitoring understanding; the illusion of competence; judging readiness by unaided performance
- Code reading and program comprehension: tracing a function's values line by line on a small input; reading top-down from the purpose to the code or bottom-up from the lines to the purpose; recognizing programming plans and beacons, the familiar idioms whose presence signals a known purpose; the load of a fragment measured by the variables held at once and the nesting depth; predicting the output before running the code as the check that the reading was right

### Social choice and fair division

- **Voting methods**: plurality, which elects the candidate with the most first-place votes; the Borda count, which gives a candidate n − p points for rank p among n candidates; the Condorcet winner, who beats every rival in a pairwise majority, when one exists; approval voting; instant runoff, which eliminates the lowest first-place count in rounds; the rules can name different winners on the same ballots, and each can be manipulated by strategic ballots
- **Arrow's impossibility theorem**: over an unrestricted domain with three or more alternatives, no rule that turns each profile of ranked ballots into a complete social ranking satisfies unanimity (if every voter ranks a above b, so does society) and independence of irrelevant alternatives, and is also not a dictatorship; the standard proof follows a pivotal voter whose ranking of one pair decides the social ranking of that pair
- **Fair division**: divide and choose for two agents, in which one cuts and the other picks; the last-diminisher procedure of Steinhaus and Banach–Knaster, giving a proportional division of a divisible good among n agents, each receiving at least 1/n of what they value; envy-freeness as the stronger requirement, with the Selfridge–Conway procedure giving an envy-free division for three agents

### Exercises

- From scratch: a brute-force explorer that tests conjectures and searches for invariants on small cases of move games and tilings
- From scratch: a Monte Carlo checker for probability puzzles (Monty Hall, the birthday problem, Simpson's paradox on generated data)
- From scratch: a units-aware calculator that rejects dimensionally inconsistent formulas
- From scratch: a spaced-repetition scheduler driving re-attempts from the error log
- From scratch: a voting tallier for plurality, Borda count, Condorcet comparison and instant runoff, run on generated ballots, reporting each profile on which the rules name different winners
- **Reasoning drills**
  - Timed mixed sets of contest-style problems across algebra, combinatorics, probability, geometry and physics-style estimation, scored for speed and accuracy and logged by error cause
  - Invariant and extremal puzzles: chessboard tilings, token and coin games, termination of processes
  - Every solved problem re-solved by a second method, then generalized or sharpened
  - One long problem each week with no hints
  - A paper read in three passes, one claim reproduced at toy size, and a one-page critique
  - A proof or a design defended orally against adversarial questions
  - A stocks-and-flows map of a familiar system, naming its feedback loops and its binding constraint
  - Given a three-candidate ballot profile, predict the winner under each voting rule, then name the fairness axiom that each rule breaks
