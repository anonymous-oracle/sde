# Part 17 · The Architect's Practice: Decisions, Strategy & Career · TOPIC LIST

Rules and directives for this part: `index/part17_architects_practice.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: The Architect's Practice: Decisions, Strategy & Career

### Making decisions

- Framing: requirement, constraints, the quality-attribute scenario served
- At least three options, always including doing nothing and buying
- Judging against scenarios and cost; premortems; review dates and reversal evidence; blast radius of each option: the users, tenants and regions a failure reaches, and the cell or partition that bounds it
- Reversibility: one-way and two-way doors; making a one-way door two-way with flags, ports and adapters, expand/contract changes or rehearsed rollbacks
- Second-order effects: who operates it, what it makes easy or hard next, what the team must learn

### Decision theory

- Decision trees: choice nodes, chance nodes, payoffs, folding back
- Expected utility and risk aversion; paying for redundancy; Bayes risk as the expected loss of a decision rule under a prior, and asymmetric losses moving the threshold: act when P(event) exceeds c_FP ÷ (c_FP + c_FN), the costs of a false alarm and a miss; a concave utility's certainty equivalent, the sure amount preferred to a gamble, and the risk premium as the gap below its expected value
- The expected value of perfect information and when a spike, prototype or benchmark is worth running
- Flexibility as an option: value of the switch, its price, modularity as a portfolio of options
- Calibration: the Brier score as a proper scoring rule; reliability, resolution and uncertainty
- The planning fallacy; reference-class forecasting; right-skewed task durations

### Build, buy, rent or adopt

- Self-run versus managed service versus SaaS versus open source, by total cost of ownership including people
- Lock-in as a priced switching cost: data to move, API surface to rewrite, skills to relearn
- Multi-cloud only for a named benefit
- "Choose boring technology": spending novelty where it creates advantage

### Evolutionary architecture and migration

- Fitness functions in CI and production: dependency-rule tests, latency budgets, cost-per-request alerts, schema-compatibility checks
- Migrating a running system by reversible steps: strangler fig, canaries, parallel runs, shadow traffic, dark launches, the named point of no return
- The six Rs of cloud migration: rehost, replatform, refactor, repurchase, retire, retain

### Sociotechnical architecture

- Team cognitive load as a design constraint
- Team Topologies: stream-aligned, platform, enabling and complicated-subsystem teams; collaboration, X-as-a-service and facilitating modes
- The platform as a product with a golden path

### Strategy, writing and review

- Technical strategy as diagnosis, guiding policy and coherent actions
- Design documents: context, goals and non-goals, design, alternatives, cross-cutting concerns (security, privacy, cost, operations, migration)
- One-page decision memos with the recommendation first
- Giving and receiving design reviews; asking for evidence, not confidence
- Disagree and commit; escalating with options
- Requirements, estimation, stakeholders and scoping

### Learning from failure

- Public postmortems as design reviews in hindsight: assumptions, blast radius, architectural fixes

### Keeping current

- Sources ranked by distance from evidence: papers and specifications, release notes, engineering blogs, commentary
- Adoption decisions: adopt, trial, assess, hold

### The road to the role

- Staff-level archetypes: tech lead, architect, solver, right hand
- The forward-deployed engineer as an architect who builds inside the customer's systems
- The architect's portfolio: design documents with decision records and measured outcomes, a scored decision journal, a postmortem of one's own failure, a public design review or RFC contribution
- The architect interview: a system design, a review of a given design, a decision gotten wrong

### Exercises

- A decision record with three options, a premortem and a review date
- An EVPI calculation that decides whether to run a load test
- A scored decision journal with Brier scores
- A design document and a one-page decision memo
- An architecture review for a full system: C4 views, scored decision records, fitness functions in CI, SLOs with burn-rate alerts, a threat model, a cost model at ten times the traffic, a game day with a chaos experiment and its postmortem, a one-year strategy
- **Reasoning drills**
  - Argue the strongest case for the option you reject before deciding
  - Premortem a plan, giving each failure a probability and a mitigation
  - Turn a vague request into constraints, numbers and one deciding question
