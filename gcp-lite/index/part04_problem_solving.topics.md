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
- **Counting techniques**: double counting; counting by bijection; complementary counting; stars and bars
- **Inequalities**: AM–GM, Cauchy–Schwarz, Jensen's inequality for convex functions, the rearrangement inequality; inequalities as tools for bounding and estimating
- **Sums and recurrences**: telescoping sums; generating functions; guessing a closed form from small cases and proving it by induction
- **Functions and graphs in puzzles**: iterating a function; fixed points; modelling a puzzle as a graph
- **Probability reasoning**: conditioning traps (Monty Hall, base-rate neglect, Simpson's paradox); symmetry and linearity shortcuts for expectation; geometric probability

### Physical and quantitative intuition

- **Dimensional analysis as a solution method**: deriving the form of a relation from the units of its inputs; dimensionless groups
- **Limiting and special cases**: zero, infinity, symmetric and degenerate configurations, used both to check an answer and to find it
- **Conservation and balance**: conserved quantities; flow balance (what enters equals what leaves at steady state) as the first equation to write
- **Approximation with known error**: (1 + x)ⁿ ≈ 1 + nx, ln(1 + x) ≈ x and √(1 + x) ≈ 1 + x/2 for small x; keeping track of the size of the neglected term
- **Scaling**: how an output changes when an input doubles; power laws as straight lines on log–log axes; doubling time and the rule of 72
- **Sketching before computing**: a function's graph from its zeros, asymptotes, monotonicity and convexity
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

### Exercises

- From scratch: a brute-force explorer that tests conjectures and searches for invariants on small cases of move games and tilings
- From scratch: a Monte Carlo checker for probability puzzles (Monty Hall, the birthday problem, Simpson's paradox on generated data)
- From scratch: a units-aware calculator that rejects dimensionally inconsistent formulas
- From scratch: a spaced-repetition scheduler driving re-attempts from the error log
- **Reasoning drills**
  - Timed mixed sets of contest-style problems across algebra, combinatorics, probability, geometry and physics-style estimation, scored for speed and accuracy and logged by error cause
  - Invariant and extremal puzzles: chessboard tilings, token and coin games, termination of processes
  - Every solved problem re-solved by a second method, then generalized or sharpened
  - One long problem each week with no hints
  - A paper read in three passes, one claim reproduced at toy size, and a one-page critique
  - A proof or a design defended orally against adversarial questions
  - A stocks-and-flows map of a familiar system, naming its feedback loops and its binding constraint
