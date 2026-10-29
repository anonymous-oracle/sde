# Part 17 · The Architect's Practice: Decisions, Strategy & Career · TOPIC LIST

Rules and directives for this part: `index/part17_architects_practice.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: The Architect's Practice: Decisions, Strategy & Career

### Making decisions

- Framing: requirement, constraints, the quality-attribute scenario served; state the decision in one sentence with the date it must be made; separate the fixed requirements from the wishes; list the constraints (budget, team skills, regulation, existing contracts) with their numbers; name the quality-attribute scenario the choice must satisfy, with its response measure, so every option is judged against the same test
- At least three options, always including doing nothing and buying; two options hide a third that often wins; doing nothing is the baseline whose cost (ongoing risk, lost opportunity) every other option must beat, and buying means a managed or SaaS product that trades build effort for recurring cost and lock-in; write each option's cost, risk and the scenario it meets in one table
- Judging against scenarios and cost; premortems; review dates and reversal evidence; blast radius of each option: the users, tenants and regions a failure reaches, and the cell or partition that bounds it
- Reversibility: one-way and two-way doors; making a one-way door two-way with flags, ports and adapters, expand/contract changes or rehearsed rollbacks
- Second-order effects: who operates it, what it makes easy or hard next, what the team must learn

### Decision theory

- Decision trees: choice nodes, chance nodes, payoffs, folding back; draw the tree left to right, with choice nodes (decisions the team controls; the best branch is taken), chance nodes (outcomes the team does not control, each branch weighted by a probability, the weights summing to one) and leaves holding payoffs; fold back from the leaves, where a chance node takes the probability-weighted average of its branches and a choice node takes the best one; the root value is the expected payoff of the best plan, and the path of best choices is that plan
- Expected utility and risk aversion; paying for redundancy; Bayes risk as the expected loss of a decision rule under a prior, and asymmetric losses moving the threshold: act when P(event) exceeds c_FP ÷ (c_FP + c_FN), the costs of a false alarm and a miss; a concave utility's certainty equivalent, the sure amount preferred to a gamble, and the risk premium as the gap below its expected value
- The expected value of perfect information and when a spike, prototype or benchmark is worth running
- Flexibility as an option: value of the switch, its price, modularity as a portfolio of options
- Calibration: the Brier score as a proper scoring rule; reliability, resolution and uncertainty
- The planning fallacy; reference-class forecasting; right-skewed task durations; the planning fallacy is forecasting from the inside view (the steps of this plan) and underestimating time, cost and risk; reference-class forecasting instead takes the distribution of actual outcomes of similar past projects and places the new one within it; task durations are right-skewed, with a long tail of delays, so the mean sits well above the median, and a commitment is best set at a high percentile of that distribution (P80 or P90), not at the typical case

### Build, buy, rent or adopt

- Self-run versus managed service versus SaaS versus open source, by total cost of ownership including people
- Lock-in as a priced switching cost: data to move, API surface to rewrite, skills to relearn
- Multi-cloud only for a named benefit; running two providers costs duplicated skills, tooling and pipelines, data transfer charges between them, and a design limited to the APIs they share; a named benefit is a concrete requirement, such as a regulation that restricts where data may be hosted, a service that only one provider offers, or a failover to a second provider that has been tested after a provider-wide outage; without one, a single provider used well is the cheaper choice
- "Choose boring technology": spending novelty where it creates advantage; each team can run only a limited number of unfamiliar technologies safely, so spend that budget only where the new tool creates advantage for the business, and pick mature, well-understood tools elsewhere, counting the operational knowledge the team already has, the hiring pool, and the documentation available when something breaks at night

### Evolutionary architecture and migration

- Fitness functions in CI and production: dependency-rule tests, latency budgets, cost-per-request alerts, schema-compatibility checks
- Migrating a running system by reversible steps: strangler fig, canaries, parallel runs, shadow traffic, dark launches, the named point of no return
- The six Rs of cloud migration: rehost, replatform, refactor, repurchase, retire, retain

### Sociotechnical architecture

- Team cognitive load as a design constraint: a team can own only what it can hold in mind, so count the systems, services, on-call duties and tools a team must understand to ship one change; intrinsic load is the problem domain itself, while extraneous load comes from tooling, unclear ownership and poor interfaces, and a design should cut extraneous load so the team's capacity goes to the intrinsic problem; boundaries are drawn so each stream-aligned team owns an area it can reason about, with shared work absorbed by a platform
- Team Topologies: stream-aligned, platform, enabling and complicated-subsystem teams; collaboration, X-as-a-service and facilitating modes
- The platform as a product with a golden path; an internal platform team treats its developers as customers, measures adoption and satisfaction, and offers self-service templates, pipelines and runtimes; the golden path is the paved default route (a standard language, service template, deployment pipeline and observability setup) that makes the supported choice the easy one, while a team that needs to leave it can, and carries the operating cost of doing so

### Strategy, writing and review

- Technical strategy as diagnosis, guiding policy and coherent actions; the diagnosis names the critical obstacle or the structure of the situation; the guiding policy is the approach chosen to overcome that obstacle; the coherent actions are the concrete steps that carry out the policy and reinforce each other; a diagnosis with no policy is a list of goals, and a policy with no diagnosis is a wish; a strategy is tested by whether a reader can point to the obstacle it claims to address
- Design documents: context, goals and non-goals, design, alternatives, cross-cutting concerns (security, privacy, cost, operations, migration)
- One-page decision memos with the recommendation first; the opening lines state the decision needed, the recommendation and the one reason it rests on; then the options with their costs, risks and the scenario each meets; then what evidence would change the recommendation and the review date; the one-page limit forces the writer to rank the options rather than list them
- Giving and receiving design reviews; asking for evidence, not confidence; the author states the goal, the constraints, the decision and the evidence behind each claim before the review; reviewers ask which measurement, incident or prototype supports a claim, name the failure they expect to see, and separate blocking concerns from suggestions; a design is accepted when its risks have been tested, not when its presenter sounds sure
- Disagree and commit; escalating with options; state the disagreement in writing with the evidence and the consequence you expect; once the accountable owner decides, carry out the chosen option fully rather than working against it; escalate with two or three options, each with its cost, its risk and a recommendation, rather than with the problem alone, so the owner can decide quickly
- Requirements, estimation, stakeholders and scoping: turn each requirement into a number with a unit and a named owner; estimate as a range with percentiles rather than a single figure, using reference-class data where it exists; map stakeholders by influence and interest and agree with each which decisions they own; scope the first delivery to the smallest slice that tests the riskiest assumption, and write down what is out of scope

### Learning from failure

- Public postmortems as design reviews in hindsight: assumptions, blast radius, architectural fixes

### Keeping current

- Sources ranked by distance from evidence: papers and specifications, release notes, engineering blogs, commentary
- Adoption decisions: adopt, trial, assess, hold; adopt makes the technology the default for a named class of problem, with an owner and support; trial is a bounded use on a real but non-critical workload with exit criteria written first; assess means reading primary sources and building a toy to check the claims; hold means not now, with the reason and the trigger that would reopen the question

### The road to the role

- Staff-level archetypes: tech lead, architect, solver, right hand; a tech lead drives the direction and delivery of one team's work; an architect owns the structure and decisions across several teams over time; a solver is sent to the hardest technical problem and takes it end to end; a right hand extends a senior leader's reach by carrying their decisions and context across the organisation; the archetypes differ in scope of impact, and most staff engineers lean toward one of them
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
