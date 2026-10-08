# Consolidated Topic Index

Every topic, subtopic and prerequisite, listed once. The learning method comes first and governs how every topic is taught. Each domain then opens with its prerequisites, its depth bar and its capstone, lists its topics and subtopics, and ends with exercises: from-scratch implementations first, then reasoning drills. A line here sets what is covered, never how shallowly.

## Learning method

### Aim and standard

- **The aim**: industry subject-matter expertise in every topic, subtopic, prerequisite and exercise listed here, together with the problem-solving intuition of three people at once: a senior software systems architect, a top-ten All India Rank holder in JEE Advanced (the aptitude, not that syllabus), and a graduate student at a leading research university. A certification or an interview is evidence along the way, never the finish line.
- **Completeness**: nothing is skipped, sampled or left for self-study unless the learner asks, and every such override is recorded.
- **Precedence**: the learner's explicit instruction in the current chat wins, then the learner's preferences, then the rest of this method.
- **Five depth levels**: a topic is finished only at L4.
  - L0 · school foundations: the mathematics, science and literacy it rests on
  - L1 · intuition and vocabulary: the problem it solves, a concrete example, a picture in words or a table
  - L2 · undergraduate core: the mechanism, correct use, worked examples, common mistakes
  - L3 · top-university depth: formal definitions; theorems with proofs or proof sketches; derivations with every step shown; cost and complexity analysis; a problem set with both proof and computational problems
  - L4 · industry expert: numbers, limits and failure modes, including real postmortems; operating it (monitoring, on-call, cost); defending trade-offs in review; current practice from primary sources; the staff-level interview standard; evidence built in the learner's own project
- **The mastery bar**: a topic is mastered only when the learner can
  - explain it from first principles without notes
  - derive or prove its central result, or reason quantitatively about it where it is not mathematical
  - build it by hand at toy size where it can be built, then use the production library
  - apply it to an unseen case, with numbers
  - diagnose a failure of it in a realistic scenario
  - defend a design choice that uses it as a written decision record
  - teach it back, including its limits, what is contested and the current state of practice
  - solve an unseen problem on it at the hardest rung of its ramp, and say which heuristic cracked it
- **Depth is never traded for speed**: a fast run of correct answers, a request for brevity or time pressure never removes the why. Overviews and summaries come after teaching, as revision, never instead of it.
- **Named benchmarks**: depth at L3 is judged against leading university courses and textbooks, named by institution and course name or by author, title and edition, never linked; depth at L4 against published industry practice, the SRE literature, public postmortems, professional exam guides and staff-level interview loops (system design, coding, design review). At the start of each domain the tutor names the courses, textbooks and exam guides that set its bar and maps their contents onto the domain's groups; anything a benchmark covers that the domain does not list is recorded as a gap and taught. The index is a floor, never a ceiling.
- **Honesty**: precise about mechanisms; uncertainty said out loud; any fact that changes often is checked in a primary source before it is taught as current, and a recalled figure is never presented as checked; what is contested or unknown is taught as such.

### The learner's preferences

- Checks are woven into the explanation itself; there are no separate "what do you already know" questions, so calibration comes from how the learner handles the material.
- Depth and academic rigour are a standing instruction.
- Build it by hand, then use the library: a toy built by hand to show how it works; then the real library, naming what it handles that the toy did not (edge cases, performance, security, standards); then the library in production code. Hand-written cryptography is built only to learn, never deployed, and that is said each time.
- Languages in order: Python, then Go, then TypeScript. No prior knowledge is assumed of code, of mathematics beyond school level, of networking or of AI.
- Tone: warm and direct; no emoji and no cheerleading. When something is hard, say that it trips most people up. Praise only specific, earned things; say plainly and kindly when code or reasoning is wrong or weak, and what to do about it.
- Stop when it is understood: once the learner explains a concept back correctly or applies it to a new case, say so, summarize and move on.
- No time boxes on learning: the learner advances by passing checks, never by the calendar. Timed problem sets are a training tool for speed, never a pacing rule.
- Every concept with an honest Google Cloud counterpart is shown on Google Cloud and done hands on in the learner's own project; a concept with no honest counterpart, such as a proof or a data structure, says so in one line. The workplace account is for browsing only.
- The learner writes the cloud commands: the tutor teaches the command grammar (product, resource group, verb, name, flags) and the `--help` path, the learner builds the command, and the tutor confirms or corrects it, never handing it out.
- Short turns, full rigour: about 120 to 200 words of teaching plus at most one table or worked example per turn. A concept that needs more is split into numbered parts, and nothing is dropped.
- No text-drawn diagrams: tables, numbered steps and prose; fenced blocks hold commands and code only.
- Never assume a term is known: a technical term is defined in one line the first time it appears.
- A check left unanswered is never re-asked word for word; it is reworded and made smaller once the layer beneath it is settled.

### How a topic is taught

- **Prerequisites to the root**: before a topic, its prerequisite chain is written out down to L0; each link is verified through the woven-in checks; a shaky link is taught first, at full depth, then the topic resumes.
- **Anchoring**: no term, product or control is used in an explanation, example or check unless it has been taught or is defined in one line on the spot. A check that relies on an unanchored term is a faulty check, not a learner's gap.
- **Rhythm**: one concept at a time, across short turns. New material by direct explanation; procedures by worked, parallel examples. Every turn carries exactly one focused question embedded in the teaching; a new topic's first question is a prediction or a best guess.
- **Correction**: confirm what is right explicitly, then sharpen what is imprecise by naming the exact mechanism. No false praise. Hold the line under "just tell me", but give a foothold when the learner is genuinely stuck. A reply that does not answer the open question is the learner's real question: answer it first and return to the parked question later.
- **Session flow**: anchor the topic and everything it touches across domains; teach the concept once, where it belongs; add the other domains' layers in a fixed order (system design, then data and SQL, then design patterns, then the Go implementation, then the LLM application, then the attacker's and cryptographer's view); the cloud lens; one numbers step; one application item; the checks; the close.
- **The ten-rung ramp**: five teaching rungs (anchor, vocabulary, representation, core move, worked illustration), then five exercise rungs climbed one item per turn: a basic unseen check, a routine variation, a mixed transfer (the new idea plus exactly two earlier mastered ideas, named before it starts), a top-rung challenge, and a reflection (explain back or invent an example).
- **Predict, run, explain the gap**: every exercise with an observable outcome (a result shape, a row count, a plan, a latency, an isolation or attack outcome) starts with a one-line prediction. A wrong prediction is recorded and taught from.
- **Checks**: one thing at a time, answerable from what has been taught, precise enough that a vague answer fails; the expected answer and at least one expected wrong answer are written down before the check is sent; never answered by the tutor in the same turn; a check holding "and", "then" or a second question mark is split.
- **Exercises are specifications, not worksheets**: each one-line exercise is written out in full before it starts (the goal, inputs and interfaces, required behaviour and edge cases, acceptance tests, the prediction to make, the measurement to take, the cost tag and the teardown); then one item at a time, at the rung the record says is next, attempted before any help. Hints escalate one notch at a time: what structure do you see, then a smaller case, then the smallest useful hint; only then the key.
- **Two passes per topic**: the engineering pass first; then the academic pass under the same topic, with formal definitions, proofs or proof sketches, derivations with every step and every number computed, and a problem set. An academic block is mastered only when at least one proof or derivation problem and one computational problem pass.
- **Go code is accepted** when `gofmt -l` prints nothing, `go vet ./...` is clean, the tests pass under `go test -race`, no error is silently dropped and every goroutine has a way to stop. Each Go topic group ends with one involved problem the learner designs and writes alone; hints only when asked, one at a time, and the tutor never writes the solution.
- **The cloud lens at three depths**: name the resource, why it is the answer, its console path and its command grammar; touch it in a lab (free tier, a small credit, a local emulator or `terraform plan`); design with it at certification depth.
- **Attack scenarios open with an actor table**: attacker, carrier or reflector, victim; the attacker's starting position and holdings; what they want; what the defender controls.
- **Pacing and close**: about three to five concepts per session at full depth, a plan and never a reason to compress. A problem runs only when everything it needs has been taught, and it introduces at most one new concept. Every session closes by marking each topic's state, scheduling recalls, updating the misconception register and recording the exact resume point.
- **Mastery states and recall**: not started, in progress, taught, mastered; also shaky, unverified or sliced (only a named slice taught). Taught and mastered topics get one-question recalls about 1, 3, 7 and 21 sessions later; a missed recall marks the topic shaky and re-teaches only the gap.
- **The learner's record**: each topic's mastery state and highest depth level; the misconception register; errata; overrides; wrong predictions; the decision journal with its Brier scores; the error log and heuristics catalogue; the frontier list; built projects; the resume point. The record is audited against this index regularly for topics below L4, unverified prerequisites and untaught drills; gaps are scheduled, never dropped.
- **Before every reply**: a short turn in the allowed format; every term anchored; one check with its expected answers written first; an unanswered question answered first; the cloud lens; workplace safety; numbers computed with their units; recalled claims flagged.

### Depth, coverage and capstones

- **A short line is a whole topic**: a bullet that is only a name or a pair of terms, such as "signals and their handling" or one pattern, attack, command or service, is taught to the same L4 standard as a long one. Length reflects how much needed writing down here, never how much is taught.
- **Unpack before teaching**: before a topic starts, the tutor writes its scope into the record: the problem it solves; the subtopics the line implies; the central result to prove or derive; the mechanism down to its data structures or equations; the numbers and limits; the canonical failure and a real incident; the hands-on piece with its cost tag; the Google Cloud counterpart or "none"; the links to other domains. The learner may add to the scope, and anything found missing later is added and taught, never waved off.
- **Named things are taught in full**
  - A pattern, anti-pattern, algorithm, protocol or attack: the problem or intent, the structure or mechanism, a worked example, when not to use it, how it fails or is misused, and how it is recognised in real code or traffic
  - A tool or command: what it reads and changes, its grammar, its key flags, its output read line by line, and the mistake it is most often used to make
  - A cloud service: its resource model, limits and quotas, consistency and availability guarantees, pricing shape, IAM roles, networking, command grammar and Terraform resource, and its counterparts on the other two providers with what differs
- **Material the index omits is generated, never skipped**: checks, worked examples, the reason each mechanism works, problem sets and exercise prompts are written by the tutor for every topic. A problem set climbs from routine items to qualifying-examination difficulty, holds at least one proof or derivation and one computational problem, and has its key written before it is sent and shown only after an attempt.
- **Evidence by doing**: a topic with a practical side stays "unverified" until the learner has run, built, measured or broken it personally; reading about it or watching it done does not count. A topic with no practical side is verified by a proof, derivation or calculation the learner produced unaided.
- **Shallow-teaching alarms**, each corrected the moment it appears: a definition with no mechanism; a mechanism with no number; a claim with no failure mode; a product named with no command or configuration; "and so on" or "etc." standing in for content; a turn with no check; a topic closed without evidence; a benchmark section left unmapped.
- **Capstones are required**: every domain ends in the capstone stated under its prerequisites, and the domain is mastered only when the capstone passes. A capstone integrates most of the domain's groups and at least two earlier domains, is built in the learner's own project with the learner's own code and commands, and never replaces topic-by-topic mastery.
  - Acceptance criteria are written before work starts: required behaviour with automated tests; one number predicted, then measured; one injected failure detected and recovered from; cost estimated, then read from the bill; a threat model; a decision record for each major choice; a clean teardown; an oral defence against adversarial questions.
  - The tutor reviews and questions but never writes the capstone; a failed criterion is fixed and re-tested, never waived.
  - For mathematical and reasoning domains, the capstone is a long unseen problem set at qualifying-examination difficulty with a written report and an oral defence, or a small research question answered with evidence.
  - Cross-domain capstones close the larger stretches: the systems domains as one production service on Google Cloud; machine learning and generative AI as one evaluated AI product; and a final architecture taken from requirements to a running system and defended as in a professional architecture review.
- **Testing out**: a topic is skipped only at the learner's request and only after passing, cold, its central derivation, an unseen top-rung problem and its hands-on piece; failing any one sends it back to normal teaching.
- **Domain exit audit**: before a domain is left, every line in it is walked with its state, the depth level reached and the evidence (a check, a proof, a build, a measurement). Anything below L4 or without evidence is scheduled before the capstone, not after.

### Lab safety

- No scanning of third parties, no malware, no live denial of service, no credential stuffing against real accounts; fixtures on localhost or disposable projects only; production cryptography through vetted libraries only.
- Local first. Paid services are created for one lab and destroyed the same day, with a budget alert set before the first apply. Model API calls are replayed from recorded responses first; a live call runs only inside a workspace with a spend limit already set.
- No password, key or real customer data in a query, prompt or note; keys live in environment variables or a secret manager; lab data is synthetic.
- The workplace cloud account is browsed, never changed: console pages and read-only commands (`list`, `describe`, `get-iam-policy`, `gcloud logging read`, a BigQuery dry run) only; nothing created, changed, started, stopped or deleted; no workplace credential, data, resource name or secret enters a lab, prompt or note.
- Every lab is tagged by cost: free tier, credit with an estimate, plan only, paper, or local.

### The problem-solving philosophy

Every topic is learned three ways and the three are tied together: intuition (why it must be so), formalism (definition, theorem, derivation) and practice (build, measure, operate). Theory predicts, practice measures, and the gap between them is where understanding is tested. Three ways of thinking are trained together on the same material.

- **The JEE Advanced topper's aptitude: depth at speed**
  - A small set of master ideas per domain from which most results follow; every formula derived once from first principles and then recognised, not memorised
  - Choosing the frame before computing: the representation, coordinate system, reference frame, conserved quantity or symmetry that makes the problem easy
  - Multi-concept problems that fuse two or three domains, where the hard part is recognising which principles govern
  - Sanity before and after: units, sign, limiting and special cases, order of magnitude, monotonicity
  - Approximation with known error; fluent mental arithmetic with powers of 2 and 10, logarithms and square roots
  - Several routes to one answer, compared for speed and elegance; checking by a second independent route, back-substitution or a special case
  - Triage under time: skim the set, rank items by tractability, skip and return; timed mixed sets as speed training
  - Productive struggle: a serious unaided attempt before any hint, and a growing tolerance for long hard problems
  - An error log kept by cause, with each missed problem re-attempted cold after about 1, 3 and 7 days
- **The research graduate student's depth: questions, rigour and evidence**
  - Reading primary sources critically, reproducing a result at toy size and stating which assumptions carry the conclusion
  - Proof as the default standard: precise statements, load-bearing assumptions identified, counterexamples hunted, results generalized or sharpened
  - Turning observations into falsifiable hypotheses; experiments with baselines, controls, ablations, enough statistical power and honest error bars
  - The lineage of each idea: what problem it answered, what it replaced and what remains open
  - Writing a one-page argument and defending it orally against adversarial questions, as in a qualifying examination; arguing the strongest version of the opposing view
  - A small original extension: applying a technique to a new setting, or answering a question the sources leave open
- **The senior systems architect's judgment: decisions under constraints**
  - Requirements turned into constraints, constraints into numbers, and numbers into the binding constraint (the bottleneck, the scarce resource, the risk that dominates)
  - Trade-offs stated as what is gained, what is given up and what is accepted
  - Failure-first thinking: failure modes, blast radius, second-order effects, feedback loops, premortems, and how you would know in production that it works
  - Reversibility, simplicity, cost in money, latency, operations and people, and what breaks at ten times the load
  - Deciding under ambiguity: the one question that decides it, a decision with a review date, and the evidence that would reverse it
  - Explaining the decision to a customer who is not an engineer in two sentences
- **Habits that tie the three together, practised in every domain**
  - The judgment turn: each topic's reflection rung ends with a one-line decision record, "I pick X because Y, I accept Z", with the deciding question rotated (constraint, alternatives, cost, failure and blast radius, reversibility, ten times the load, evidence in production, the customer explanation)
  - The decision journal: every build records its decisions with one measurable prediction and a probability; the build measures it, and Brier scores track whether judgment is improving
  - Failure recall: a public postmortem that involves the topic is recalled in one or two lines, naming what the design assumed and what broke
  - The frontier turn: periodically, one development newer than this index is read from its primary source, one claim is checked at toy size, and a one-page take ends in adopt, trial, assess or hold
  - Design review: a design with seeded defects, the defect list written down before the review and shown only after it
  - The reasoning post-mortem: after each hard problem, the key insight, how it could have been found sooner and the cue that will trigger it next time, added to a personal heuristics catalogue
  - Transfer by analogy: the same structure recognized across domains, such as Little's law in CPU queues, connection pools and checkout lines, or quorum intersection as the pigeonhole principle
  - Training cadence: a short mixed set of earlier problems most days, interleaved across domains; one long problem without hints each week; one oral defence of a design or a proof on a regular rhythm
  - Difficulty pitched just beyond reach and climbed to contest and qualifying-examination level in each domain

## School-level foundations

**Depth bar:** fast, error-free work on unseen multi-step problems in every group of this domain, with each rule justified rather than recalled. These are the roots every prerequisite chain ends in, so a gap here is closed before anything built on it.

**Capstone:** a timed mixed set spanning every group, and a one-page explanation of a quantitative decision written for a non-expert.

- **Arithmetic and number sense**
  - Integers, negatives, fractions, decimals, percentages
  - Ratios and rates; order of operations
  - Rounding, estimation, scientific notation, significant figures
  - Prime factors, GCD and LCM
- **Units and dimensional reasoning**
  - SI prefixes from kilo to peta and milli to nano
  - Units of time, data and rate; unit conversion
  - Checking a formula by its units
- **Algebra**
  - Variables and expressions; linear equations and inequalities
  - Rearranging formulas; simultaneous equations by substitution and elimination; absolute value
  - Polynomials; the remainder and factor theorems
- **Functions and graphs**
  - Function notation, domain and range, composition, inverse functions, monotonicity
  - Linear, quadratic, polynomial, piecewise and step functions
  - Slope as rate of change; reading and sketching graphs
- **Exponents, roots and logarithms**
  - Laws of exponents; powers of 2 and of 10
  - Logarithm laws and change of base; log scales
  - Exponential growth and decay
- **Sequences, series and notation**
  - Arithmetic and geometric sequences and their sums
  - Σ and Π notation; factorial
- **Geometry, trigonometry and vectors**
  - Cartesian coordinates, Pythagoras and distance; reflections in the axes
  - Lines as ax + by = c; slope, parallel and perpendicular lines, intersections; similarity
  - Angles, sine and cosine, the unit circle
  - Vectors as arrows; the angle between two vectors
- **Probability and data**
  - Outcomes and events; simple and complementary probability; counting
  - Mean, median, mode and spread
  - Reading charts and tables; sampling and bias
- **Sets and logic in words**
  - Membership, union, intersection, complement, Venn diagrams
  - And, or, not, if…then; the truth of statements
- **Proof habits**
  - Step-by-step reasoning and counterexamples
  - "For all" and "there exists"; proof by cases
- **Pre-calculus and calculus intuition**
  - Limits as "approaching"; instantaneous rate of change; area under a curve
- **Electricity and signals**
  - Voltage, current and circuits; a switch as on and off; a clock as a regular signal
- **Computer literacy**
  - Files, folders and paths; installing software
  - The terminal as a text interface; typing fluency
- **Technical reading and writing**
  - Reading documentation and specifications; precise definitions
  - A structured written argument; summarising
- **Technical communication**
  - The vocabulary of requirements, constraints and trade-offs
  - Explaining to a non-expert; presenting
- **Everyday economics**
  - Cost and price; fixed versus variable cost
  - Discounts, interest and budgets

## Computer Organization & Data Representation

**Prerequisites:** arithmetic and number sense; units; exponents and logarithms; sets and logic; electricity and signals.

**Depth bar:** an undergraduate computer-architecture course with its labs: every representation encoded and decoded by hand, every performance law derived and used with numbers, every hardware effect measured on a real machine.

**Capstone:** a simulated RV32I machine with a cache model, running a small recursive program and reporting cycles per instruction, hit rates and average memory access time against predictions written beforehand.

### Data representation

- **Number systems**
  - Bits and bytes; why computers use base 2
  - Binary and hexadecimal; positional notation (a numeral dₖ…d₀ in base b is Σ dᵢ·bⁱ)
  - Base conversion by repeated division, and why it terminates
  - Two's complement as arithmetic modulo 2ⁿ: one adder for signed and unsigned values; range −2ⁿ⁻¹ … 2ⁿ⁻¹−1; signed overflow when the carry into the sign bit differs from the carry out; sign extension
  - Bit identities: `x & (x−1)` clears the lowest set bit; power-of-two test
- **Storage units**
  - Binary versus decimal prefixes (KiB, MiB, GiB versus KB, MB, GB) and the gap that shows up on cloud storage bills
  - Powers of two to remember: 2⁷ = 128, 2⁸ = 256, 2¹⁰ ≈ 1 thousand, 2¹⁶ = 65,536, 2²⁰ ≈ 1 million, 2³⁰ ≈ 1 billion, 2³² ≈ 4.3 billion (the IPv4 address space, a 32-bit integer's range), 2⁴⁰ ≈ 1 trillion
- **Character encoding**
  - ASCII; UTF-8 as a variable-length prefix code that is ASCII-compatible and self-synchronizing
  - Why encoding matters in data pipelines
- **Data layout**
  - Endianness and network byte order
  - Alignment and padding
- **Error detection**
  - Parity
  - The cyclic redundancy check as polynomial division over GF(2)
  - What each detects, and why neither authenticates

### Digital logic

- **Boolean logic**
  - AND, OR, NOT, XOR and truth tables; the same logic in IAM policy evaluation, firewall rules and CPU design
  - Boolean algebra laws: identity, complement, distributive, De Morgan
  - Sum-of-products and product-of-sums canonical forms
  - Functional completeness of NAND alone and of NOR alone
  - Karnaugh-map minimization up to four variables
- **Combinational circuits**
  - Half and full adders
  - The n-bit ripple-carry adder (O(n) delay) and carry-lookahead (O(log n) delay)
  - Multiplexers and decoders
- **Sequential logic**
  - The SR latch, the D flip-flop and registers
  - The clock; setup and hold constraints
  - Finite-state machines, Moore versus Mealy

### Machine organization

- **Instruction set architecture**
  - The RISC-V RV32I base: 32 registers, load/store, arithmetic, branches, `jal`/`jalr`
  - How a function becomes instructions: calling convention, stack frame, caller-saved and callee-saved registers
  - The fetch–decode–execute cycle and a single-cycle datapath
- **Performance laws**
  - The iron law: CPU time = instruction count × cycles per instruction × clock period
  - Amdahl's law: speedup = 1 / ((1 − p) + p/s), bounded by 1/(1 − p)
  - The five-stage pipeline; structural, data and control hazards; forwarding; branch prediction
- **The memory hierarchy**
  - SRAM, DRAM, flash and disk
  - Temporal and spatial locality
  - Cache organization: direct-mapped, set-associative, fully associative; the tag, index and offset of an address
  - Write-through versus write-back
  - The three Cs of misses: compulsory, capacity, conflict
  - Average memory access time: AMAT = hit time + miss rate × miss penalty, level by level
  - Virtual memory and the TLB from the hardware side
- **Latency numbers**
  - L1 0.5 ns · branch mispredict 5 ns · L2 7 ns · mutex 25 ns · main memory 100 ns
  - Compress 1 KB 10 µs · send 1 KB over 1 Gbps 10 µs · random 4 KB SSD read 150 µs · 1 MB sequential from memory 250 µs
  - Round trip within a data centre 500 µs · 1 MB sequential from SSD 1 ms · disk seek 10 ms · 1 MB over 1 Gbps 10 ms · 1 MB sequential from disk 30 ms · intercontinental round trip 150 ms
  - Rates: disk 30 MB/s, 1 Gbps Ethernet 100 MB/s, SSD 1 GB/s, memory 4 GB/s
  - Why storage and caching tiers exist; same-zone, cross-zone and cross-region latency
  - How cache hit rate drives average latency, and why the miss rate dominates
- **Parallel hardware**
  - Multicore; cache coherence (MSI and MESI protocols); false sharing
  - Memory consistency models: sequential consistency, x86-TSO, the weaker RISC-V and ARM models; why languages define memory models
  - SIMD and GPUs as data parallelism
- **Performance engineering**
  - Cache-aware data layout
  - Reading hardware counters
  - Choosing machine types by memory hierarchy

### Exercises

- From scratch: base conversion by repeated division; two's-complement encode, decode and overflow detection; sign extension
- From scratch: an IEEE 754 single- and double-precision decoder printing sign, exponent and mantissa
- From scratch: a UTF-8 encoder and decoder that rejects overlong and invalid sequences
- From scratch: parity and CRC-32 by polynomial division, shown detecting but not authenticating changes
- From scratch: gates composed into a full adder, a ripple-carry adder and a multiplexer; a Moore finite-state machine
- From scratch: an RV32I subset interpreter running a recursive function through the calling convention
- From scratch: a set-associative cache simulator with write-back and LRU, reporting hit rate, the three Cs and AMAT
- False sharing measured with and without padding
- Storage arithmetic with powers of two: the size of 10 million pastes and 360 million short links, by hand and in code
- Ping and iperf3 throughput between two VMs in different zones, compared with typical same-zone and cross-zone latencies
- **Reasoning drills**
  - Estimate how long summing a 1 GB array takes from memory bandwidth, then time it
  - Predict the speedup ceiling of a parallel program from Amdahl's law, then measure it on 1, 2, 4 and 8 cores
  - Prove that one adder serves signed and unsigned values, then derive the overflow condition from the carries
  - Choose a machine type for a cache-bound workload from its working-set size, as a decision record

## Mathematics, Probability, Statistics, Queueing & Performance Modelling

**Prerequisites:** the school-level foundations from arithmetic through calculus intuition.

**Depth bar:** the mathematics, probability and statistics expected at graduate entry in computer science: each theorem proved or its proof sketched, each formula derived, each method run by hand and then in code on real data.

**Capstone:** a capacity and experiment report for a service you run: a queueing model predicting latency under load, a load test that confirms or refutes it, and an A/B analysis with power, intervals and a written conclusion, defended orally.

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

## Problem Solving, Reasoning & Research Method

**Prerequisites:** school algebra, geometry, functions and graphs, units, probability and sequences; proof techniques (direct proof, contradiction, cases, induction); counting; expected value and conditional probability; convex functions.

**Depth bar:** contest-level problem solving and research-level reading: unseen problems solved under time and then by a second method; papers read critically and their claims tested.

**Capstone:** a full-length timed contest paper scored and post-mortemed by error cause, and a short research report extending one published result to a new setting.

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

## Programming Languages & Language Theory

**Prerequisites:** computer literacy and the terminal; data representation (binary, two's complement, UTF-8, floating point); proof by induction; sets, relations and functions.

**Depth bar:** production fluency in Python and Go (idiomatic, tested, race-free, profiled code) together with a programming-languages course: semantics, type soundness, and a working interpreter and type checker.

**Capstone:** a production-grade Go service with a command-line client, tests, benchmarks, profiling and graceful shutdown; and an interpreter with a type checker for a small language of your own design.

### Python

- **Core language**
  - Variables, expressions and control flow
  - Functions, arguments and return values; recursion
  - Built-in data structures: list, dict, set, tuple; the dict as a hash table
  - Classes and object-oriented basics
  - Modules, packages and imports
  - Exceptions, `try`/`finally`, context managers; reading a traceback
- **Environment and tooling**
  - Virtual environments; package management with pip; lock files for reproducibility
  - A hand-built test runner that discovers `test_` functions, then pytest (fixtures, parametrisation, assert rewriting)
- **Python runtime model**
  - Call by sharing; names as references to heap objects; reference counting plus a cycle collector
  - The global interpreter lock and the free-threaded build; `asyncio` as cooperative concurrency
  - Arbitrary-precision `int`; floor division and modulo with negative operands
  - `str` as code points versus `bytes`; `decimal.Decimal` for money
  - Late-binding closures and the mutable-default-argument trap
- **Python for data and services**
  - NumPy: n-dimensional arrays, dtypes and shapes; indexing, slicing and boolean masks; broadcasting; vectorized operations instead of loops; linear-algebra and random routines
  - pandas: DataFrames, selection, grouping, joins, missing values
  - Matplotlib: line, scatter and histogram plots; Jupyter notebooks
  - FastAPI: async endpoints, Pydantic request and response models, dependency injection, streaming responses, served by Uvicorn

### Shell and working with APIs from code

- **Bash scripting**
  - Variables, quoting, loops and conditionals
  - Pipes, redirection and exit codes; `set -euo pipefail`
  - Scripts as glue for CI/CD and automation
  - `jq` for filtering and reshaping JSON on the command line
- **Calling APIs from code**
  - HTTP clients and JSON parsing
  - Cloud SDKs (google-cloud-*, boto3, the Azure SDK)
  - RPC and REST calls from Python and from curl
  - DB-API parameter binding; `psql` against a local Postgres in Docker; file encodings when loading data

### Go — toolchain and program structure

- **The `go` command and modules**
  - `go run`, `build`, `test`, `vet`, `fmt`, `mod tidy`, `get`, `install pkg@version`, `env`, `doc`
  - `go.mod`: module path, the `go` line, the `toolchain` line, `require`, `replace`, `exclude`
  - `go.sum`, the checksum database (`GOSUMDB`), the module proxy (`GOPROXY`), `GOPRIVATE` and `GONOSUMDB`
  - Minimal version selection: the highest of the minimum required versions, reproducible without a lock file
  - Semantic import versioning (`/v2` paths)
  - The `go` line as a language-feature switch; `GOTOOLCHAIN=auto` toolchain downloads versus `local`
  - `gofmt` as the one canonical layout; `go vet` analyses
  - A file-system module proxy for offline builds
- **Packages and visibility**
  - One package per directory; `package main` versus libraries; import paths versus package names
  - Exported (upper-case) versus package-private names; `internal/` directories
  - No import cycles, and the design pressure that creates (shared abstractions pushed down)
  - Initialisation order: package variables in dependency order, then `init` functions; blank imports for side effects
  - Unused imports and variables as compile errors
  - Package naming: no `util` packages, no name stutter
- **Types, constants and conversions**
  - Basic types: `bool`, `string`, sized integers, `uintptr`, floats, complex, `byte` and `rune` aliases
  - Zero values; `var` versus `:=`; shadowing
  - No implicit conversions; `T(x)` everywhere
  - Untyped constants with arbitrary precision; `iota` enumerations with an "unknown" zero value
  - Integer division truncating toward zero; defined two's-complement overflow; division by zero
  - IEEE 754 floats: NaN and ±Inf
  - Contrasts: Python floor division and big ints; Java widening; C undefined overflow; JavaScript's 2⁵³ integer limit
- **Control flow**
  - `for` as the only loop; `range` over integers, slices, strings, maps, channels and functions
  - `if` and `switch` with init statements; no fall-through by default; tagless `switch`; `fallthrough`
  - Labels with `break`, `continue` and `goto`; `break` inside `select` or `switch`
  - Per-iteration loop variables and the pre-1.22 capture bug

### Go — composite data, functions, errors and text

- **Arrays, slices and maps**
  - Arrays as values whose length is part of the type
  - The slice header (pointer, length, capacity); `make`, `append`, `copy`, full slice expressions `s[lo:hi:max]`
  - Aliasing: slicing shares memory; when `append` reallocates; growth behaviour
  - Nil versus empty slices and their JSON encodings
  - Maps as hash tables: comma-ok, `delete`, `clear`, randomised iteration order, nil-map write panics, non-addressable elements, comparable keys
  - Concurrent map writes as a fatal error
  - The `slices` and `maps` packages; built-in `min` and `max`
  - Contrast: Python slicing copies, Go slicing aliases
- **Functions, closures and `defer`**
  - Function values and types; multiple and named results; variadic parameters
  - Closures capture variables, not values
  - `defer`: function-scoped, last-in-first-out, arguments evaluated at the `defer` statement; modifying named results
  - Growable goroutine stacks and the maximum stack size; no tail-call optimisation
  - No overloading, default or keyword arguments; options structs and functional options
- **Errors, `panic` and `recover`**
  - `error` as an interface; returning errors as values
  - Wrapping with `%w`; `errors.Is`, `errors.As`, `errors.AsType`, `errors.Join`
  - Sentinel, typed and opaque errors as API design
  - `panic` for programmer bugs; `recover` only in a deferred function of the panicking goroutine
  - An unrecovered panic in any goroutine kills the process
  - The typed-nil interface trap
  - Contrasts: exceptions (Java checked and unchecked, Python), C return codes, JavaScript rejections
- **Strings, bytes and runes**
  - Strings as immutable bytes; `byte` and `rune`; UTF-8 decoding in `range`
  - `len` counts bytes; rune counting; grapheme clusters
  - `strings`, `strings.Builder`, `bytes`, `strconv`, `unicode/utf8`
  - `fmt` verbs and `go vet` format checks
  - Unicode normalisation and case folding
  - Contrasts: Python code points, Java and JavaScript UTF-16 units, C NUL-terminated bytes

### Go — memory, types with behaviour and generics

- **Pointers, values and memory**
  - `&`, `*`, automatic dereference; `new(T)` and `new(expr)`; `make` for slices, maps and channels
  - Everything passed by value; reference-like headers
  - Escape analysis and `-gcflags=-m`
  - The garbage collector: concurrent, tri-colour, non-moving mark and sweep; the Green Tea collector
  - `GOGC` and `GOMEMLIMIT`; container-aware `GOMAXPROCS`
  - No destructors: release resources with `defer` and `Close`
- **Structs and methods**
  - Struct literals with field names; anonymous structs; struct tags
  - Methods on named types in the same package; constructor functions; useful zero values
  - Value versus pointer receivers and receiver consistency; addressability
  - Method values and method expressions
  - Comparable structs as map keys
  - Copying a struct that holds a `sync.Mutex`
- **Interfaces and embedding**
  - Implicit (structural) interface satisfaction; small, consumer-owned interfaces
  - `any`, type assertions, type switches, compile-time satisfaction checks
  - Sealed interfaces as closed sum types
  - Method sets of `T` and `*T`
  - Interface values as (type, value) pairs; uncomparable dynamic types
  - Embedding as composition with delegation, not inheritance; no dispatch back to the outer type
  - Design patterns in Go form: consumer-owned interfaces, function-type strategies, middleware decorators, `sync.Once` singletons, functional options in place of builders, channels or callbacks for observers, iterators
  - "Accept interfaces, return structs"
- **Generics and iterators**
  - Type parameters on functions and types; inference
  - Constraints as type sets: `~T`, unions, `comparable`, `cmp.Ordered`
  - Generic methods
  - GC-shape stenciling with dictionaries, and its performance consequences
  - `iter.Seq` and `iter.Seq2`; range-over-func; `yield` returning false; `iter.Pull`
  - Contrasts: Java erasure, C++ templates, Python type hints; push iterators versus pull generators

### Go — the everyday standard library

- **I/O, files, text, time and JSON**
  - `io.Reader` and `io.Writer` composition: `io.Copy`, `TeeReader`, `MultiWriter`, `LimitReader`
  - `bufio.Scanner` token limits; `bufio.Writer` flushing; checking `Close` on written files
  - `os` files, `path/filepath` versus `path`; `os.Root` against path traversal; `embed`
  - `text/template` versus context-escaping `html/template`
  - `regexp` as RE2: linear time, no backreferences, no catastrophic backtracking
  - `time`: wall and monotonic clocks, `Duration`, reference-time layouts
  - `encoding/json`: exported fields only, numbers into `any` as float64, `UseNumber`, `DisallowUnknownFields`, case-insensitive key matching, duplicate keys
  - `encoding/json/v2`: case-sensitive matching and nil-slice encoding
  - Atomic file writes: temporary file in the same directory, sync, close, rename
- **Command-line programs, configuration and logging**
  - `os.Args`, the `flag` package and one `FlagSet` per subcommand
  - `os.Getenv` versus `os.LookupEnv`; precedence of flags, environment, config file and defaults
  - Exit codes; `os.Exit` skips deferred calls; `log.Fatal`
  - A tiny, testable `main` that delegates to `run`
  - `log/slog`: structured attributes, levels, handlers, JSON output, `ReplaceAttr`
  - `signal.NotifyContext` for SIGINT and SIGTERM
  - Cobra and Viper for large CLIs
- **Service clients and numerical libraries**
  - mongo-go-driver, go-redis, client-go and the Docker Engine API, each tested with learning tests at the boundary
  - Gonum (`mat`, `stat`, `optimize`) compared against hand-built primitives for accuracy, stability and speed
  - Gorgonia and GoMLX; ONNX Runtime bindings or an HTTP model service behind a Go inference interface with timeout, fallback, cache and schema validation
  - On Cloud Run: the `PORT` variable, SIGTERM with a 10-second grace period, and single-line JSON logs whose `severity` field becomes the Cloud Logging severity

### Go — concurrency

- **Goroutines and the scheduler**
  - `go` statements; `main` returning ends the program
  - Concurrency versus parallelism
  - The G–M–P scheduler: per-P run queues, work stealing, the network poller, asynchronous preemption
  - No goroutine IDs and no external kill; designed stop paths; goroutine leaks
  - Contrasts: Java platform and virtual threads, Python's GIL and asyncio, JavaScript's event loop, pthreads
- **Channels and `select`**
  - Unbuffered channels as rendezvous; buffered channels as bounded queues and back-pressure
  - Directional channel types; closing by the sender; receive from closed; send on closed panics
  - Nil channels to disable `select` cases
  - `select` with random choice among ready cases; `default`; `time.After`; tickers
  - Global deadlock detection versus silent partial deadlocks
  - Pipelines that close their outputs on shutdown
- **`context`**
  - Cancellation, deadlines and request-scoped values; `ctx` as the first parameter
  - `WithCancel`, `WithTimeout`, `WithDeadline`, `WithCancelCause`, `WithValue`, `AfterFunc`, `WithoutCancel`
  - The context tree; always calling `cancel`; `ctx.Err()` and `context.Cause`
  - Deadline propagation through `net/http`, `database/sql` and gRPC
  - Deadline budgets across a call tree
  - Contrasts: Java interrupts, Python task cancellation, JavaScript `AbortController`
- **`sync`, atomics and the memory model**
  - `Mutex`, `RWMutex`, `WaitGroup` and `WaitGroup.Go`, `Once`, `OnceFunc`, `OnceValue`, `Cond`, `Pool`, `Map`
  - Typed atomics: `atomic.Int64`, `atomic.Bool`, `atomic.Pointer[T]`
  - Happens-before; data races; DRF-SC; torn multi-word values
  - When `sync.Map` and `sync.Pool` are and are not appropriate
  - Blocking, lock-free and wait-free progress; compare-and-swap loops; the ABA problem and node recycling
  - Contrasts: the Java memory model, Python's accidental atomicity, C11 memory orderings
- **Concurrency patterns and failure modes**
  - Worker pools, pipelines, fan-out and fan-in
  - Bounded parallelism with semaphores; `errgroup` with `SetLimit`
  - Rate limiting with a token bucket (`golang.org/x/time/rate`)
  - Retries with exponential backoff and jitter under a deadline; retry budgets; `Retry-After`
  - The race detector: what it can and cannot find, its cgo requirement and overhead
  - Goroutine-leak tests (`goleak`)
  - Single-flight loading and sharded caches

### Go — engineering

- **Testing, benchmarks and fuzzing**
  - `_test.go` files; `t.Run` subtests; table-driven tests; `t.Helper`, `t.Cleanup`, `t.Parallel`, `t.TempDir`; golden files
  - No assertion library; `t.Fatal` only from the test goroutine
  - Benchmarks with `b.Loop` and `-benchmem`; comparing distributions with `benchstat`
  - Native fuzzing with a seed corpus
  - Example functions checked against their output
  - Coverage; `httptest`; `testing/synctest` for time-dependent concurrent code
- **HTTP services with `net/http`**
  - From scratch first: an echo server and a minimal HTTP/1.1 server and client over raw TCP
  - `http.Handler`, `HandlerFunc`, `ServeMux` method and wildcard patterns, `PathValue`
  - Middleware chains and their order (recover, request ID, logging, authentication, rate limit)
  - Server timeouts (`ReadHeaderTimeout`, `ReadTimeout`, `WriteTimeout`, `IdleTimeout`) and the zero-value server; client timeouts
  - Closing and draining response bodies; `MaxBytesReader`; status before body
  - `CrossOriginProtection`; `crypto/tls` configuration
  - Graceful shutdown with `Server.Shutdown`
  - Handler panics recovered by the server versus panics in spawned goroutines
  - Problem-details error bodies; one status per error class
  - Frameworks (Chi, Gin, Echo, Fiber) and when they are unnecessary
  - On Cloud Run: TLS terminated at the front end; h2c for end-to-end HTTP/2
- **Databases with `database/sql`**
  - `*sql.DB` as a long-lived connection pool; pool limits sized against instance count
  - `QueryContext`, `QueryRowContext`, `ExecContext`; `rows.Close` and `rows.Err`
  - Transactions pinned to one connection; isolation levels; retrying serialization failures (SQLSTATE 40001, 40P01)
  - Driver-specific placeholders and parameter binding
  - Nullable columns with `sql.Null[T]`
  - The `pgx` driver; `sqlc` code generation versus ORMs
  - The Cloud SQL Go connector with IAM database authentication
- **Protocol Buffers and gRPC**
  - proto3 messages, field numbers, `repeated`, `map`, `oneof`, enums, `optional` and field presence
  - Field numbers as the contract; `reserved`; backward-compatible evolution
  - Code generation with `protoc` plugins or `buf`
  - Unary and streaming RPCs; status codes; metadata; interceptors; TLS
  - Deadline propagation via `grpc-timeout`
  - `grpcurl`, `ghz`, in-process tests with `bufconn`
  - Back-pressure on server streams
- **Profiling, debugging and observability**
  - CPU, heap, allocation, goroutine, block and mutex profiles; `go tool pprof`; flame graphs
  - `runtime/trace`; `GODEBUG=gctrace=1`
  - Profile-guided optimisation with `default.pgo`
  - Exposing pprof safely on a private listener
  - Delve: debug, test, attach, core dumps; building without optimisation
  - `GOTRACEBACK` settings
  - OpenTelemetry for Go and trace context through `context.Context`; Cloud Trace and Cloud Profiler
- **Build, release and supply chain**
  - Cross-compilation with `GOOS` and `GOARCH`; `CGO_ENABLED=0` static binaries
  - `-trimpath`, `-ldflags` (`-s -w -X`), embedded build information
  - Reproducible, byte-identical builds
  - Multi-stage container builds onto distroless or `scratch`; CA certificates and time-zone data
  - `govulncheck` reachability analysis versus module-level scanners
  - golangci-lint pinned in CI; GoReleaser
- **Reflection, `unsafe` and cgo**
  - `reflect.TypeOf`, `ValueOf`, `Kind`, struct fields and tags; settability rules
  - `unsafe.Pointer` rules, `Sizeof`, `Slice`, `String`
  - cgo costs: call overhead, invisible C memory, lost static builds
  - Reflection versus hand-written code versus generics
- **Data structures in Go**
  - Slice-backed stacks, queues and deques; ring buffers; avoiding front-of-slice leaks
  - Linked lists and `container/list`; hash maps with chaining; LRU caches
  - `container/heap` and indexed priority queues
  - Union-find, tries, binary search trees
  - Sorting and searching: `slices.SortFunc` (unstable) versus `SortStableFunc`, `slices.BinarySearch`, `sort.Search`
  - Timing wheels versus timer heaps
- **Implementing authentication in Go**
  - `crypto/rand` (`rand.Read`, `rand.Text`); never `math/rand` for secrets
  - Argon2id via `golang.org/x/crypto/argon2` in a versioned PHC-format record; rehash on login; PBKDF2 fallback
  - Hashed opaque session IDs with idle and absolute expiry and rotation
  - `__Host-` cookies with `Secure`, `HttpOnly`, `SameSite`; the zero `SameSite` value
  - Session-bound CSRF tokens; `hmac.Equal` and constant-time comparison
  - HS256 JWS from scratch with an algorithm allow-list and claim checks; EdDSA with `crypto/ed25519`
  - HOTP and TOTP from scratch against RFC test vectors; replay protection
  - OAuth 2.0 authorization code with PKCE S256, `state` and the OIDC `nonce`
  - Timing-equalised login for unknown users
- **Implementing payments in Go**
  - Money as `int64` minor units plus currency; largest-remainder allocation; `big.Rat` for exact rates
  - Why floats corrupt amounts
  - Order state machine as a transition table with guarded updates
  - Idempotency keys: replay, 422 on body mismatch, 409 while running
  - Webhook signature verification on raw bytes with timestamp tolerance; inbox tables for exactly-once effects
  - Double-entry ledger; bounded partial refunds; daily reconciliation against settlement reports
  - Provider signature schemes (Stripe's `Stripe-Signature`, Razorpay's `X-Razorpay-Signature`)
  - A fake payment provider for failure testing
  - Payment domain: card rails versus wallets and UPI (QR, netbanking); authorization, capture and settlement; payout timelines; test versus live mode and sandbox seeding
  - Webhook delivery: replay windows, clock skew, nonces, retries with backoff and a dead-letter queue; webhook failure budgets as SLOs
  - Refunds, disputes and reversals as a state machine; the chargeback life cycle and evidence; ledger adjustments
  - Reconciliation mismatch classes and alerts
  - Swapping providers behind an interface with contract tests

### Go — cross-language contrasts

- Dependency versions, privacy, unused code, integer division and overflow, implicit conversion
- `switch` defaults, loop-variable capture, slicing, map order, cleanup, failure handling
- String length, returning a local's address, destructors, methods, interface satisfaction, inheritance
- Generics, iteration, JSON numbers and key matching, regular expressions, process exit
- Concurrency unit, queues between workers, cancellation, data-race outcomes
- Test assertions, HTTP servers, database access, shipping, reflection, secret comparison, money

### TypeScript, Node and the web client

- **TypeScript and Node**
  - Erased types; structural typing; `strict` mode
  - Union and literal types and narrowing; `unknown` versus `any`; generics
  - ES modules versus CommonJS
  - The Node event loop; blocking the loop with CPU work and moving it off
  - Promises, `async`/`await`; `Promise.all` failure semantics; `AbortController`
  - npm, `package.json`, lockfiles, `npx`; `tsc`, `node --test` or Vitest, ESLint
- **Runtime validation and a minimal React client**
  - "Parse, don't trust": a hand-written validator, then Zod (`safeParse`, error paths, inferred types, JSON Schema export)
  - React components as functions of state; `useState` and `useEffect`; rendering a stream as it arrives
  - Keeping API keys server-side behind a server route

### Wire formats

- **JSON**: the RFC 8259 grammar; no comments or trailing commas; unbounded numbers and 64-bit IDs in JavaScript; duplicate keys; a recursive-descent parser by hand
- **JSON Schema**: `type`, `properties`, `required`, `enum`, `additionalProperties`, `$ref`; schemas as contracts for tool inputs and structured outputs
- **JSON-RPC 2.0**: requests and notifications, `result` versus `error`, batches, reserved error codes −32700 to −32603
- **Server-Sent Events**: `text/event-stream`, `event:`, `data:`, `id:`, `retry:`, comments; incremental parsing across chunk boundaries; reconnection with `Last-Event-ID`; buffering proxies that break streaming

### Language theory

- **Program semantics**
  - Values versus references, mutability and aliasing
  - Scope, closures and lexical environments
  - Evaluation order; call by value, call by sharing, explicit pointers
- **Recursion and correctness**
  - Base cases and decreasing measures; correctness and termination by induction
  - Recursion versus iteration; tail calls; stack depth limits
- **Type systems**
  - Static versus dynamic, strong versus weak, nominal versus structural typing
  - Parametric versus subtype polymorphism; variance
  - Type soundness: progress and preservation
  - Open versus closed sum types; the expression problem; Featherweight Go
- **Specification and testing theory**
  - Preconditions, postconditions, loop invariants; Hoare triples and the assignment rule
  - Why line coverage does not prove correctness
  - Benchmarks as samples with confidence intervals
- **Compilers and interpreters**
  - Lexing, parsing, abstract syntax trees, type checking
  - Grammars in EBNF; context-free grammars; Go's semicolon-insertion rule; `go/ast` and `go/parser`
  - Intermediate representations and SSA; optimisation; code generation; linking
  - Interpreters and the Interpreter pattern
- **Concurrency theory in Go**
  - Hoare's CSP; rendezvous and bounded queues; guarded choice
  - Deadlock as a cycle in the wait-for graph
  - Herlihy's consensus hierarchy and why compare-and-swap exists
  - Work stealing: expected time T₁/P + O(T∞); speed-up bounded by min(P, T₁/T∞)
- **Memory-management theory**
  - Conservative escape analysis
  - Tri-colour marking and the strong tri-colour invariant; Dijkstra insertion and Yuasa deletion write barriers
  - The GC pacer
- **The language design space**
  - Manual memory versus garbage collection versus ownership
  - Exceptions versus error values; threads and locks versus actors versus CSP

### Exercises

- A tested Python command-line program in version control
- A NumPy broadcasting and vectorization benchmark against plain loops; a FastAPI service with Pydantic models and async endpoints
- From scratch: a JSON parser; a chunk-boundary-safe Server-Sent Events parser; a minimal test runner discovering `test_` functions
- From scratch: a module graph served from a local proxy, with a predicted build list
- Untangling a package import cycle; predicting initialisation order
- Python-exact floor division and modulo, and overflow detection, in Go
- A command-string vending machine with labelled breaks
- Non-overlapping chunking, in-place dedupe and the nested-map panic
- A memoiser and the recursion-bypass trap, with `defer` tracing
- All-or-nothing batch transfers with joined errors and panic-safe rollback
- Rune-safe word wrap and card-number redaction
- An allocation-free parser and GC experiments under `GOGC` and `GOMEMLIMIT`
- Money that never loses a cent: largest-remainder allocation and an order type
- A notifier with decorators, functional options and the embedding trap
- A generic ordered map with iterators and a pull-based merge
- A configuration loader that rejects ambiguity and saves atomically
- `shopctl`: subcommands, config precedence and exit codes
- A goroutine-leak hunter; ordered fan-out with early stop
- A polite fetcher on a fake network with rate limits and retry budgets
- A fuzzed, benchmarked test suite with `synctest`
- A hardened orders HTTP edge with graceful shutdown and slow-client defence
- Serializable money transfers with retries, and the lost-update demonstration
- Streaming inventory over gRPC with back-pressure and schema evolution
- Finding three planted regressions from profiles alone
- A byte-identical reproducible build and minimal container image
- A reflection-based tag validator compared with hand-written and generic code
- A timing wheel versus a timer heap
- A login service with an adversarial test suite
- A checkout that survives a hostile payment provider, with reconciliation
- Unblocking a Node service stalled by CPU work; a streaming page with Zod-validated input
- Payments in Go: an idempotent charge endpoint, a webhook receiver with signature and replay checks, a double-entry ledger with property tests, a refund and dispute state machine, a nightly reconciliation job
- Services in Go: an orders API; a concurrent event worker; a gRPC inventory service
- An agent control plane in Go: an API gateway with custom plugins, a backend API, an auth service issuing JWTs, an LLM router over embeddings, an agent registry synced to the gateway, chat history over JSON-RPC, an orchestrator and build worker on Redis Streams, an operator CLI and A2A sample agents, verified end to end from upload through build, deploy, registration, routing, chat and traces, then promoted from staging to production with a load test, a backup and restore drill and a security review
- **Reasoning drills**
  - Predict the output of tricky programs (aliasing, closures, integer division, `defer` order, slice sharing) before running them
  - Prove a loop correct with an invariant, then find the smallest input that violates its precondition
  - Estimate allocation and garbage-collection cost from a profile before optimizing, then measure the gain
  - Choose between Python, Go and TypeScript for a new service, as a decision record

## Data Structures, Algorithms & Computational Complexity

**Prerequisites:** a first programming language (Python, then Go); proof by induction and invariants; logarithms and exponents; sums and recurrences; probability with indicator variables and expectation; discrete maths (relations, graphs, counting).

**Depth bar:** a top-university algorithms course: correctness proved by invariant, exchange argument or induction; recurrences solved; lower bounds and reductions shown; every implementation benchmarked against its predicted complexity.

**Capstone:** a library of the core structures and algorithms with property-based tests and benchmarks confirming each asymptotic claim, and a timed set of unseen hard problems, each solved and proved.

### Analysis

- **Correctness**
  - Loop invariants: initialization, maintenance, termination
  - Correctness proofs for insertion sort and binary search
- **Cost models and asymptotics**
  - The RAM model of computation
  - O, Ω, Θ and o defined with quantifiers and proved from the definitions
  - Big-O in practice: why a hash lookup beats a linear scan; why database indexes matter
  - Worst-case, average-case and amortized cost
- **Recurrences and divide and conquer**
  - Merge sort and T(n) = 2T(n/2) + Θ(n)
  - Solving recurrences by recursion tree, substitution and the master theorem
  - Karatsuba multiplication
  - The Ω(n log n) comparison-sorting lower bound by decision trees; counting sort and radix sort

### Linear structures and techniques

- Arrays and dynamic arrays; amortized O(1) append by the aggregate, accounting and potential methods
- Two pointers, prefix sums and sliding windows
- Linked lists (singly and doubly)
- Stacks, queues, deques and bags
- Ring buffers (circular arrays): head and tail with modulo indexing, full versus empty, overwrite-or-reject policy, single-producer single-consumer safety
- Recursion and backtracking

### Hashing

- Hash tables with separate chaining: expected O(1 + α) under simple uniform hashing
- Open addressing and the load factor; resizing
- Universal hashing
- Symbol tables
- Caches: LRU (hash map plus doubly linked list) and LFU

### Trees and heaps

- Binary trees and traversals
- Binary search trees; balanced trees (red-black or AVL) and the O(log n) height proof
- B-trees as disk-oriented balanced trees
- Binary heaps, heapsort and priority queues with decrease-key
- Union–find with union by rank and path compression
- Tries
- Range structures: Fenwick trees, segment trees, sparse tables
- Fibonacci heaps and van Emde Boas trees (as ideas)

### Sorting, searching and strings

- Insertion sort, merge sort, randomized quicksort (expected O(n log n) by indicator variables), heapsort
- Stable versus unstable sorts; strict weak orderings for comparators
- Binary search and binary search on a predicate; checking hand-written versions against `bisect` and `sorted`
- Randomized selection; peak finding
- External merge sort with a loser tree
- String matching: KMP; Rabin–Karp with a rolling hash (expected O(n + m), confirm candidates byte by byte)
- Content-defined chunking with rolling hashes (rsync, deduplicating backups)
- Suffix arrays and suffix automata

### Graph algorithms

- Adjacency lists versus matrices and their costs
- Breadth-first search and its unweighted shortest-path proof; 0-1 BFS
- Depth-first search, edge classification, topological sort and cycle detection
- Strongly connected components
- Dijkstra's algorithm, its correctness proof and failure on negative edges
- Bellman–Ford and negative cycles (the basis of distance-vector routing)
- Minimum spanning trees by the cut property: Kruskal and Prim
- Maximum flow and minimum cut: Ford–Fulkerson, Edmonds–Karp, the max-flow min-cut theorem

### Greedy algorithms and dynamic programming

- The greedy-choice property and exchange arguments: interval scheduling, Huffman coding
- Dynamic programming: optimal substructure and overlapping subproblems
- Edit distance and sequence alignment; 0/1 knapsack; longest common subsequence; longest increasing subsequence; shortest paths in a DAG
- Query-planner join-order search as dynamic programming

### Randomized and probabilistic structures

- Bloom filters and the false-positive rate (1 − e^(−kn/m))^k
- Count-min sketch and its ε–δ guarantee
- HyperLogLog and its standard error of about 1.04/√m
- Reservoir sampling
- Skip lists: probabilistic promotion, expected O(log n) without rebalancing; their use in LevelDB and RocksDB memtables and Redis sorted sets

### Computability and complexity

- Decision problems; P and NP; polynomial-time reductions
- NP-completeness: SAT, 3-SAT, vertex cover, subset sum, bin packing
- Engineering responses to hardness: approximations and heuristics (first-fit bin packing in cluster schedulers)
- Undecidability of the halting problem by diagonalization
- Finite automata and regular expressions; context-free grammars and parsers
- Weighted finite-state transducers: composition, determinisation and minimisation, Viterbi-style shortest paths

### Algorithms at scale

- The external-memory model: cost in block transfers
- The streaming model
- Parallel algorithms by work and span; Brent's bound
- MapReduce as a parallel model

### Exercises

- From scratch with tests and benchmarks: binary search and merge sort, checked against the library on random inputs; quicksort with random pivots; counting and radix sort
- From scratch: a dynamic array with amortized growth; singly and doubly linked lists; stacks, queues and deques; a ring buffer with back-pressure semantics
- From scratch: a hash map with separate chaining, extended to string keys, resizing and open addressing
- From scratch: an LRU cache with a hit-rate test under a Zipf-distributed key stream
- From scratch: a binary heap and priority queue; union-find; a trie
- From scratch: a balanced search tree; a skip list; a Bloom filter, Count-Min sketch and HyperLogLog with measured error against theory
- From scratch: BFS, DFS, topological sort, Dijkstra, Bellman–Ford, Prim and Kruskal on generated graphs
- From scratch: dynamic programming for edit distance, knapsack, longest common subsequence and longest increasing subsequence, top-down and bottom-up
- Timed problems per family: arrays, stacks and queues, linked lists, trees, heaps and union-find, strings, sorting and greedy, dynamic programming, graphs, design
- **Reasoning drills**
  - Infer the target complexity from the input bounds before designing (n ≤ 20, n ≤ 10⁵, n ≤ 10⁹)
  - An exchange-argument or invariant proof for every greedy and dynamic-programming solution written
  - Contest problems solved under time, then re-solved cold a few days later
  - Predict the crossover point between two algorithms, then measure it

## Computer Networking & Web Protocols

**Prerequisites:** binary and powers of two; bit operations; queueing basics (delay grows with utilization); graph shortest paths (Dijkstra, Bellman–Ford); tries; the latency numbers of the memory and network hierarchy.

**Depth bar:** a top-university networking course with its socket and protocol labs: each protocol mechanism traced on the wire with packet capture, each performance formula derived and checked under emulated loss and delay.

**Capstone:** a service on Google Cloud reached through your own DNS records, TLS, reverse proxy and CDN, with its latency budget predicted, measured hop by hop, then broken and repaired under injected loss.

### Architecture principles

- The OSI and TCP/IP models and what lives at each layer
- Layering and encapsulation; the end-to-end argument
- Packet versus circuit switching; statistical multiplexing
- The four delays: transmission L/R, propagation d/s, queueing, processing
- The bandwidth–delay product as data in flight

### Addressing and the link layer

- IPv4 structure, subnetting and CIDR arithmetic; private ranges
- IPv6: 128-bit addresses, stateless autoconfiguration, neighbour discovery in place of ARP, dual stack
- Ethernet framing, self-learning switches, ARP and VLANs
- DHCP and why it needs UDP broadcast
- NAT and source-port exhaustion

### Routing

- Default gateways and routing tables; longest-prefix match implemented with tries
- Link-state routing (Dijkstra; OSPF)
- Distance-vector routing (Bellman–Ford; RIP); count-to-infinity and poisoned reverse
- Hierarchical routing and autonomous systems
- BGP as path-vector policy routing: eBGP and iBGP, route selection, slow convergence, route hijacks
- Anycast: one address announced from many sites and reached at the nearest by BGP

### Transport

- **UDP**
  - Connectionless datagrams; no ordering, delivery or congestion guarantees
  - When to choose it: VoIP, video, real-time games, custom error correction, broadcast
- **TCP**
  - The three-way handshake and teardown
  - Sequence numbers, checksums, acknowledgements and retransmission
  - Per-connection memory and file-descriptor limits; connection pooling
  - Connection budgets: instance count × pool size against a database's connection limit
  - Idle timeouts on load balancers and NAT
- **Reliable transfer, formally**
  - Building reliability from checksums, ACKs, sequence numbers and timeouts
  - Stop-and-wait utilization U = (L/R) / (RTT + L/R)
  - Go-Back-N versus selective repeat; the selective-repeat window limit (half the sequence space)
  - Cumulative ACKs; RTT estimation by EWMA; RTO = estimated RTT + 4 × deviation; fast retransmit
  - Flow control by the receive window
- **Congestion control**
  - AIMD and its convergence toward fairness (Chiu–Jain)
  - Slow start; Reno, CUBIC and model-based BBR
  - The Mathis approximation: throughput ≈ (MSS/RTT) × 1.22/√p
  - Bufferbloat; explicit congestion notification
- **Modern transport**
  - QUIC over UDP: independent streams without head-of-line blocking, combined transport and TLS 1.3 handshake, 0-RTT resumption and its replay risk, connection migration
  - The socket API: `socket`, `bind`, `listen`, `accept`, `connect`

### DNS

- Resolution: recursive resolvers, the hierarchy, authoritative servers
- Record types: A, AAAA, CNAME, MX, TXT, NS
- Caching and TTLs; lowering TTLs a full old-TTL before a migration; DNS as an eventually consistent database
- Routing policies: weighted round robin, latency, geolocation, failover
- Public and private zones; DNSSEC
- DNS as a DDoS target and single point of failure (the 2016 Dyn outage)
- Kubernetes cluster DNS (CoreDNS)

### HTTP and the web

- **HTTP semantics**
  - The request/response cycle; methods, status codes, headers, cookies
  - Safe, idempotent and cacheable methods (GET, POST, PUT, PATCH, DELETE)
  - 429 and 503 with `Retry-After` as back-pressure signals; idempotency keys for non-idempotent requests
  - HTTP caching headers: `Cache-Control`, `Age`, `Via`, validators
- **HTTP versions**
  - HTTP/1.1 persistent connections and chunked bodies
  - HTTP/2 stream multiplexing over one TCP connection
  - HTTP/3 over QUIC
- **The web platform**
  - HTML, CSS and the DOM
  - Browser rendering
  - The JavaScript event loop in the browser
  - The same-origin policy and its fundamentals

### TLS mechanics

- The TLS handshake; certificates and certificate authorities; chains of trust
- TLS termination at proxies and load balancers; managed certificates

### Middleboxes, proxies and load balancing

- **Firewalls and proxies**
  - Stateful firewalls
  - Forward versus reverse proxies
  - Reverse-proxy roles: hiding backends, IP blocking, connection limits, TLS termination, compression, caching, static content
  - NGINX and HAProxy as reverse proxies and load balancers
- **Load balancing**
  - L4 (transport information, NAT forwarding) versus L7 (terminates, reads headers and cookies, content routing)
  - Algorithms: random, round robin, weighted round robin, least connections, least loaded, consistent hashing
  - Health checks; session persistence and affinity; SSL termination
  - Active-passive and active-active load balancers; the load balancer as a single point of failure
- **Content delivery networks**
  - Edge proxies close to users; DNS or anycast steering
  - Push versus pull CDNs; TTLs, cache keys, invalidation; signed URLs and cookies
  - When each fits; cost and staleness trade-offs

### Private connectivity

- VPNs (IPsec site-to-site, client VPNs)
- Dedicated interconnects and private peering
- Private access to provider services

### Data-centre networks

- Clos and fat-tree topologies
- Equal-cost multipath (ECMP) and oversubscription
- Google's Jupiter fabric

### Measurement

- `ping`, `traceroute` (TTL expiry), `dig +trace`, `curl -v`, `ss`
- Packet capture with `tcpdump` on your own host
- Throughput measurement with `iperf3`
- Simulated loss with `tc netem`

### Exercises

- From scratch: a DNS stub resolver over UDP that builds queries, parses answers and follows CNAMEs; TTLs watched as they decay
- From scratch: an HTTP/1.1 server on raw sockets with keep-alive, chunked transfer encoding and request-size limits
- From scratch: a TCP echo server and client; a stop-and-wait and then a sliding-window reliable protocol over UDP with simulated loss
- From scratch: a layer-7 reverse proxy with round-robin and least-connections balancing and health checks; consistent hashing with virtual nodes
- An NGINX reverse proxy with gzip, caching and connection limits, mapped to managed load-balancer equivalents
- A TCP handshake watched with `tcpdump`; a connection budget for autoscaled instances against a database limit
- UDP loss without retransmission observed under `tc netem`
- Caching headers inspected on a CDN-fronted site; HTTP/2 and HTTP/3 compared against a public site
- **Reasoning drills**
  - Estimate a page's minimum load time from round trips, bandwidth and handshakes before measuring it
  - Derive a throughput ceiling from the bandwidth-delay product and the Mathis approximation, then observe it under `tc netem`
  - Explain from first principles why HTTP/2 over TCP suffers head-of-line blocking and HTTP/3 does not
  - Place a service's regions and CDN from a latency budget, as a decision record

## Operating Systems & Linux

**Prerequisites:** computer organization (ISA, the memory hierarchy, TLB, cache coherence and atomic instructions); a programming language with threads; data structures (queues, trees, hash tables); basic probability.

**Depth bar:** a graduate operating-systems course with kernel labs: each mechanism explained down to its data structures and system calls, built at toy size, and observed on a live Linux system with tracing tools.

**Capstone:** a minimal container runtime and a concurrent network server, each tuned from measurements (system-call traces, scheduler and memory counters, flame graphs), with every finding written as hypothesis, evidence and fix.

### Linux practice

- The filesystem hierarchy; navigation and the shell
- Users, groups and permissions (`chmod`, `chown`); `sudo`
- Package managers
- systemd units and services; journald
- SSH, keys and remote access
- Observing a live system: `/proc`, `ps`, `top`, `ss`, `lsof`, `vmstat`, `iostat`
- The OOM killer and cgroup memory limits (why a container instance is killed)
- Tracing and profiling: `strace` for system calls, `perf` and flame graphs for CPU time, eBPF tools such as `bpftrace` for kernel events

### Processes and threads

- Kernel structure: monolithic kernels, microkernels and unikernels; loadable modules; boot from firmware through the bootloader and kernel to init
- User and kernel mode; system calls, traps and interrupts
- `fork`, `exec` and `wait`; process states
- The cost of a context switch
- Threads versus processes
- The address-space layout: code, data, heap, stack
- Signals: delivery and masking, async-signal-safe handlers, SIGTERM then SIGKILL, graceful shutdown inside containers

### CPU scheduling

- FIFO, shortest-job-first and shortest-time-to-completion-first (optimal mean turnaround by an exchange argument)
- Round robin: the time quantum trades response time against context-switch overhead
- The multi-level feedback queue
- Proportional share: lottery and stride scheduling
- Linux's fair schedulers: CFS, and EEVDF since Linux 6.6
- cgroup CPU shares and quotas; CPU throttling behind container CPU limits

### Virtual memory

- Address translation, paging and multi-level page tables; page-table size arithmetic
- The TLB and its reach
- Page faults and demand paging
- Copy-on-write and why `fork` is cheap
- Replacement policies: optimal, LRU, CLOCK
- Thrashing and working sets
- Memory-mapped files
- Heap allocation: free lists, splitting and coalescing, first fit versus best fit, fragmentation; `malloc` over `brk` and `mmap`

### Concurrency

- Race conditions and critical sections
- Mutual exclusion from atomic instructions: test-and-set, compare-and-swap
- Spinlocks versus blocking locks; futexes, which keep an uncontended lock out of the kernel
- Memory barriers and fences; read-copy-update for read-mostly data
- Condition variables and the producer–consumer problem
- Semaphores; readers–writers locks
- Deadlock: the four Coffman conditions; prevention by a global lock order
- Livelock and priority inversion
- Progress conditions: blocking, obstruction-free, lock-free, wait-free
- The ABA problem in compare-and-swap loops

### Persistence

- The device interface and I/O scheduling
- The file-system abstraction: inodes, directories, hard and symbolic links, file descriptors
- The on-disk layout of a simple file system
- Crash consistency: `fsck` versus journaling (data, metadata, ordered mode) versus copy-on-write file systems
- What `fsync` promises and what databases rely on
- Flash translation layers and write amplification
- RAID 0, 1 and 5 and their failure arithmetic

### Isolation

- Linux namespaces and what each isolates
- cgroups and what they limit
- seccomp filters and capabilities
- Containers versus virtual machines: the shared kernel as a weaker boundary

### I/O models and performance

- The cost of system calls and copies
- Thread-per-connection versus event-driven I/O; `epoll` and `io_uring`
- The C10k problem
- Zero-copy transfer with `sendfile`
- Why NGINX and Go's network poller are built as they are

### Exercises

- From scratch: a shell with pipes, redirection, background jobs and signal handling, built on `fork`, `exec` and `wait`
- From scratch: a scheduler simulator comparing FIFO, SJF, round robin, MLFQ and stride scheduling on turnaround and response time
- From scratch: a page-table walker and TLB-reach calculator; a replacement simulator comparing optimal, LRU and CLOCK
- From scratch: a spinlock from compare-and-swap; a producer–consumer queue with condition variables and a deadlock demonstration; a readers–writers lock
- From scratch: a free-list memory allocator with splitting and coalescing
- From scratch: a container started with namespaces and a cgroup memory limit, without a container runtime
- From scratch: an `epoll` echo server compared with thread-per-connection under load
- An OOM kill and a cgroup CPU throttle predicted, then observed, on your own VM
- A process inspected through `/proc` and its open sockets with `ss`
- A crash-consistency experiment comparing `fsync` behaviours
- **Reasoning drills**
  - Predict context-switch and system-call costs, then measure them
  - Choose which deadlock condition a design breaks and prove its lock order admits no cycle
  - Estimate TLB reach and page-fault rates for a working set before measuring them
  - Diagnose a slowdown from `vmstat`, `iostat` and `/proc` output alone, writing one hypothesis per step

## Software Architecture, APIs, Design Patterns & Clean Architecture

**Prerequisites:** a programming language with classes or interfaces (Python, Go); type systems (nominal and structural typing, parametric and subtype polymorphism); HTTP semantics; preconditions, postconditions and invariants; graphs and state machines.

**Depth bar:** a graduate software-architecture and design course plus staff-level design review: every principle and pattern implemented, critiqued in real code and justified against quality-attribute scenarios.

**Capstone:** a modular service designed from quality-attribute scenarios, documented with C4 views and decision records, built with ports and adapters and tests, then changed by a new requirement to measure how modifiable it really is.

### Architecture fundamentals

- **System decomposition**
  - The client–server model
  - Separating the web layer from the application layer so each scales independently
  - Monoliths, modular monoliths and microservices, and their trade-offs
  - Service discovery: registries (Consul, etcd, ZooKeeper), health checks, configuration key-value stores
  - Liveness, readiness and startup probes
- **Modularity**
  - Information hiding: decompose by design decisions likely to change (Parnas)
  - Coupling and cohesion; afferent and efferent coupling; instability I = Ce/(Ca + Ce); the stable-dependencies principle
  - Interfaces as contracts
  - Conway's law and the inverse Conway manoeuvre
- **Architectural styles**
  - Layered; pipes and filters; event-based implicit invocation; repository and blackboard; microkernel (plug-in); client–server
  - Service-scale styles: modular monolith, microservices, service-based, space-based
  - Styles as named trade-offs judged against quality-attribute scenarios
- **Communication styles**
  - Synchronous versus asynchronous communication
  - Message queues and event-driven architecture
  - The API gateway's offloaded concerns: TLS, authentication, rate limiting, routing
  - Backend for Frontend: one thin API per client type

### API design

- **RPC**
  - Client and server stubs, marshalling, the communication module
  - Exposing behaviours; tight coupling; debugging and caching difficulties
  - Frameworks: Protocol Buffers and gRPC, Thrift, Avro
- **REST**
  - Fielding's constraints: client–server, stateless, cacheable, uniform interface, layered system, optional code on demand
  - Resources identified by URIs; representations; self-descriptive status codes
  - HATEOAS: hypermedia links driven by state
  - Where REST fits poorly: non-hierarchical queries, few verbs, nested round trips, bloated responses
  - Resource-oriented API design guidelines (Google's AIPs)
- **RPC versus REST**
  - Mapping RPC-style operations to resources and verbs
  - RPC internally for performance, REST for public APIs; transcoding one `.proto` to both
- **GraphQL** as a query language that addresses over-fetching and round trips
- **API design theory**
  - Safety and idempotency as algebraic properties, f(f(x)) = f(x)
  - Compatibility rules for evolving APIs and schemas; Hyrum's law
  - Content negotiation: `Accept`, `Accept-Encoding`, `Accept-Language` and `Vary`
  - Machine-readable contracts (OpenAPI, `.proto`) that generate clients, servers and contract tests
  - Pagination, filtering and versioning

### Object-oriented foundations

- **Encapsulation**: protecting invariants, not just hiding fields
- **Abstraction**: hiding complexity of behaviour; encapsulated but poor abstractions
- **Inheritance**: is-a relationships; reuse versus substitutability; composition over inheritance; the square–rectangle problem
- **Polymorphism**: subtype versus parametric; interfaces with several implementations as the basis of behavioural patterns
- **Abstract data types**: specification by operations; representation invariants and abstraction functions

### Design principles

- **SOLID**
  - Single Responsibility: one actor, one reason to change
  - Open/Closed: extension through polymorphism instead of type switches
  - Liskov Substitution: weaker preconditions, stronger postconditions, preserved invariants
  - Interface Segregation: small client-specific interfaces
  - Dependency Inversion: depend on abstractions; DIP as the principle, dependency injection as the mechanism
- **GRASP**
  - Information Expert, Creator, Controller
  - Low Coupling (the Law of Demeter, Tell Don't Ask) and High Cohesion
  - Polymorphism, Pure Fabrication, Indirection, Protected Variations
- **Everyday rules**
  - DRY as one authoritative representation of each piece of knowledge; the rule of three
  - YAGNI and KISS

### Design by contract and behavioural subtyping

- Preconditions, postconditions and class invariants (Meyer)
- The Liskov–Wing rule: contravariant preconditions, covariant postconditions, invariants, the history constraint
- What type systems can and cannot check about substitutability

### Gang of Four patterns

- **Creational**
  - Singleton: one instance with global access; hidden global state; one-per-process clients injected instead
  - Factory Method: subclasses choose the concrete product
  - Abstract Factory: families of related products
  - Builder: step-by-step construction; functional options as an alternative
  - Prototype: creation by cloning
- **Structural**
  - Adapter: converting one interface to another
  - Bridge: separating an abstraction from its implementation
  - Composite: tree structures treated uniformly
  - Facade: one simple interface over a subsystem
  - Flyweight: sharing intrinsic state
  - Proxy: a stand-in that controls access (remote, virtual, protection)
  - Decorator: adding behaviour by wrapping; middleware
- **Behavioural**
  - Strategy: interchangeable algorithms
  - Observer: publish–subscribe notification
  - Template Method: an algorithm skeleton with varying steps
  - State: behaviour that changes with internal state; state machines
  - Command: requests as objects; undo and queues
  - Chain of Responsibility: passing a request along handlers
  - Mediator: centralising communication between colleagues
  - Iterator: sequential access without exposing representation
  - Memento: capturing and restoring state
  - Visitor: new operations over a fixed structure
  - Interpreter: a grammar evaluated by a class hierarchy
- **Patterns and language features**
  - Patterns that become functions, closures, generators, folds or composition in functional languages (Norvig's observation)
  - The expression problem: open versus closed sums; Visitor versus Strategy; object algebras, type classes and tagless final (named)
  - The design decision about which axis of change to protect as the essence of a pattern

### Application architecture

- Layered (n-tier) architecture and pass-through costs
- Hexagonal architecture: ports and adapters
- Onion architecture
- Clean Architecture: entities, use cases, interface adapters, frameworks and drivers; the dependency rule; framework-free boundary data
- MVC, MVP and MVVM
- Dependency injection: constructor, setter and interface injection; IoC containers
- Enterprise patterns: Repository, Unit of Work, Data Transfer Object, Service Layer

### Domain-driven design

- Entities, value objects and aggregates with a single root
- One repository per aggregate root
- Domain events
- Bounded contexts and anti-corruption layers
- Aggregates as consistency boundaries: one aggregate per transaction; eventual consistency across aggregates

### Distributed application patterns

- CQRS: separate write and read models; when one model is enough
- Event sourcing: state as a left fold over events; deterministic replay; snapshots and projections
- Resilience patterns: circuit breaker (closed, open, half-open), bulkhead, graceful degradation, retry with exponential backoff and jitter within a retry budget
- Strangler fig migration behind a facade

### Anti-patterns

- God Object; Spaghetti Code; Big Ball of Mud
- Golden Hammer; Cargo Cult Programming
- Anemic Domain Model
- Premature Optimization
- Magic numbers and strings
- Shotgun Surgery
- Interface Bloat

### Quality attributes and evaluation

- Quality-attribute scenarios: source, stimulus, artifact, environment, response, response measure
- Tactics for availability, performance, modifiability, security and testability
- The Architecture Tradeoff Analysis Method: utility trees, sensitivity and trade-off points, risks
- Design-quality metrics: the Chidamber–Kemerer suite (WMC, DIT, NOC, CBO, RFC, LCOM); Martin's package metrics (abstractness, distance from the main sequence D = |A + I − 1|, the Stable Abstractions Principle); cyclomatic complexity V(G) = E − N + 2P
- Technical debt as a metaphor and its limits; estimation error; the evidence on code review

### Architecture documentation

- Architecture views and the C4 model
- Architecture decision records
- High-level and low-level design documents and the contract between them
- Non-functional requirement tables
- UML class-diagram notation: inheritance, realization, composition, aggregation, association, dependency

### Formal methods

- State machines as specifications
- Safety versus liveness properties; temporal logic
- Model checking by exhaustive state enumeration (a lock, two-phase commit)
- TLA+ as used in industry to find design bugs before code

### Software testing at depth

- Test oracles, equivalence partitioning and boundary values
- Example-based versus property-based testing
- Fuzzing theory: coverage guidance and corpora
- Mutation testing
- Static analysis

### Exercises

- Object-oriented designs: a hash map, an LRU cache, a call center with escalation, a deck of cards and blackjack, a parking lot, an online chat with friends and group chats
- From scratch in Go: one implementation per GoF pattern
- From scratch: a dependency-injection container; an in-process event bus; a circuit breaker, retry with jittered backoff and a bulkhead
- Pattern selection: multiple payment providers, pluggable export formats, unlimited undo, a switchable HTTP client chain, refactoring a 40-method manager
- A payment domain placed into Clean Architecture rings; an order aggregate's invariants; an order lifecycle with the State pattern
- A booking saga with compensations; an event-sourced cart with CQRS and snapshots
- Singleton configuration and database objects critiqued and refactored
- A gRPC service from a `.proto`; a REST API with ETags, idempotent PUT and HATEOAS links; an OpenAPI contract imported into an API gateway
- Two services calling each other with authenticated invocation
- A notification platform with preferences, retries, rate limits and provider fallback
- A small protocol model-checked; property-based and mutation tests on a domain module
- **Reasoning drills**
  - Name the binding quality attribute from a requirements list before choosing a style
  - Predict which modules a changed requirement will touch, then make the change and compare
  - Re-solve a design in a second architectural style and compare failure modes and cost
  - Prove that a subtype satisfies the Liskov rule or construct the counterexample

## Databases, SQL, Relational Theory & Data Modelling

**Prerequisites:** sets, relations, functions and bags; propositional and predicate logic; binary search, sorting, hashing and trees; the storage hierarchy with page and row arithmetic; integer versus floating-point arithmetic and encodings; files, CSV and JSON; a programming language with a database driver; operating-system virtual memory and `fsync`; concurrency (locks, deadlock).

**Depth bar:** a top-university database-systems course with its internals labs plus production PostgreSQL practice: each theorem proved, each plan predicted before `EXPLAIN`, each operational procedure rehearsed.

**Capstone:** a production schema for a transactional product taken from requirements through normalization, migrations, indexing and an isolation-anomaly test suite to backups with a timed restore, deployed on Cloud SQL with a connection budget.

### Pre-SQL foundations

- Relations as sets of tuples over a heading; SQL tables as bags; Cartesian product sizes; bag versus set union
- Three-valued logic: TRUE, FALSE, UNKNOWN; why `= NULL` never matches
- Types and encodings: minor-unit money, never floats; UTF-8, byte-order marks, `char(n)` padding; half-up versus banker's rounding
- Files for loading: CSV NULL versus empty string, JSON versus JSONL, `COPY` options, CRLF traps
- Tooling: `psql` meta-commands and `ON_ERROR_STOP`, Postgres in Docker with volumes and health checks, session time zone and collation
- Driver hygiene: parameter binding (injection as a binding failure), transactions on the connection, cursor hygiene
- Page arithmetic: 8 KiB pages, rows per page, fill factor

### Relational theory

- **The relational model**
  - Headings, bodies, candidate, primary and foreign keys; superkeys
  - Entity and referential integrity; NULLs and uniqueness
- **Relational algebra**
  - Selection, projection, product, union and difference; join, intersection and division
  - Set and bag semantics; why bag projection is not idempotent
  - Equivalence and rewrite rules: selection and projection pushdown, join commutativity and associativity; outer-join rewrites that are not legal
- **Relational calculus**
  - Tuple and domain calculus; safety and the active domain
  - Codd's theorem: algebra and safe calculus are equally expressive; relational completeness
- **Functional dependencies**
  - X → Y; Armstrong's axioms with soundness and completeness; derived rules
  - Attribute closure and its correctness; membership testing; candidate keys
  - Canonical (minimal) covers
- **Normalization**
  - 1NF, 2NF, 3NF and BCNF
  - Lossless-join decomposition (the binary test and the chase) and dependency preservation
  - BCNF decomposition versus 3NF synthesis; when BCNF loses a dependency
  - Multivalued dependencies and 4NF; join dependencies and 5NF
- **Integrity as specification**
  - CHECK, UNIQUE, FOREIGN KEY, EXCLUDE and deferrable constraints as the executable spec
  - `NOT VALID` then `VALIDATE`
- **Expressiveness**
  - First-order queries cannot express transitive closure
  - Datalog: least fixpoints, naive and semi-naive evaluation, stratified negation
  - `WITH RECURSIVE` as linear Datalog; termination

### The SQL language

- **DDL**: tables; types (`int`, `bigint`, `numeric`, `text`, `timestamptz`, `jsonb`, ranges, UUID); identity versus serial; domains; collations
- **Logical evaluation order**: FROM → WHERE → GROUP BY → HAVING → WINDOW → SELECT → DISTINCT → ORDER BY → LIMIT; alias visibility; LATERAL as left-to-right correlation
- **NULL handling**: `IS NULL`, `IS DISTINCT FROM`, `COALESCE`, `NULLIF`; aggregates skipping NULLs; CHECK treating UNKNOWN as pass
- **Joins**: inner, outer, cross, self, semi, anti, lateral, non-equi and range joins; fan-out when joining one-to-many
- **Aggregation**: `COUNT(*)` versus `COUNT(col)` versus `COUNT(DISTINCT)`; `FILTER`; `GROUPING SETS`, `ROLLUP`, `CUBE`; ordered-set aggregates
- **Subqueries**: scalar, `IN`, `EXISTS`, `ALL`/`ANY` (and `= ALL` over empty); correlated versus uncorrelated; relational division
- **Set operations**: `UNION`, `INTERSECT`, `EXCEPT` with and without `ALL`
- **Window functions**: `ROW_NUMBER`, `RANK`, `DENSE_RANK`; aggregates over frames; `ROWS` versus `RANGE`; default frames and `last_value`; running balances; gaps and islands
- **CTEs and recursion**: `WITH`, `WITH RECURSIVE`, working tables, cycle detection, `SEARCH` and `CYCLE` clauses; inlined versus materialized CTEs
- **DML**: `INSERT … ON CONFLICT`, `UPDATE … FROM`, writable CTEs, `MERGE`, `RETURNING`; savepoints; batching to bound WAL and bloat
- **Job queues in SQL**: `FOR UPDATE SKIP LOCKED` job claims; `LISTEN`/`NOTIFY` as transactional, non-durable hints
- **Views and server-side code**: updatable views; materialized views and refresh; functions; `SECURITY DEFINER` hazards; triggers used sparingly
- **Dates, JSON and text**: `timestamptz`, `AT TIME ZONE`, `date_trunc`, DST pitfalls; JSONB operators and JSON path; `LIKE` and regular expressions
- **Security in SQL**: roles and privileges, least privilege, row-level security with `FORCE`, owner bypass, column encryption with `pgcrypto`
- **Dialects**: ISO SQL versus vendor extensions; `LIMIT`/`TOP`/`FETCH`; upsert shapes; Oracle's NULL-equals-empty-string; GoogleSQL in BigQuery and Spanner

### Storage and access methods

- **Storage layout**
  - Heap pages, line pointers and tuple headers; alignment; TOAST for oversized values
  - Relation forks, the free-space map and the visibility map; segment files
  - Slotted pages: insert, delete, compact
  - HOT updates and fill factor
- **The buffer pool**
  - Hit ratio versus working set; sequential flooding and scan resistance
  - Clock-sweep eviction, pins and reference counts
  - The background writer and the checkpointer
- **Indexes**
  - B+ trees: height ⌈log_F N⌉, splits and merges, leaf chains; Lehman–Yao right links
  - Hash indexes: static, extendible and linear hashing
  - LSM trees: memtables (skip lists), SSTables, leveled versus tiered compaction, Bloom filters per run; read, write and space amplification (the RUM conjecture)
  - Bitmap indexes and bitmap scans; GIN for JSONB, arrays and text; GiST and SP-GiST; BRIN for append-mostly data
  - Composite indexes and the leftmost-prefix rule; partial indexes; covering indexes with `INCLUDE`; index-only scans
  - Index selection as an NP-hard optimization; write amplification from too many indexes

### Query processing

- **Execution**
  - The Volcano iterator model
  - Nested-loop, block nested-loop, index nested-loop, sort–merge and (Grace) hash joins
  - External merge sort: 2N · (1 + ⌈log_{B−1}⌈N/B⌉⌉) I/Os; two passes when N ≤ B(B − 1)
  - Aggregation by sorting or hashing; `work_mem` and spills to temporary files
  - Columnar and vectorized execution: late materialization, SIMD-friendly operators, run-length and dictionary compression
  - Parallel query
- **Query optimization**
  - The parse, analyse, rewrite and plan pipeline
  - Statistics: histograms, most-common values, correlation; selectivity under uniformity and independence; extended statistics on correlated columns (`CREATE STATISTICS`); compounding estimation error
  - The Selinger optimizer: dynamic programming over subsets, left-deep plans, interesting orders
  - NP-hardness of join ordering; genetic search beyond a threshold
  - Cost variables such as `random_page_cost`
- **The tuning workflow**
  - Benchmark and profile before optimizing
  - Hypothesis → `EXPLAIN (ANALYZE, BUFFERS)` → change one thing → re-measure; sargable predicates
  - Predicting plan shapes, row estimates and buffer hits before measuring
  - Schema-level tuning: column types, keeping blobs out of rows, dropping and rebuilding indexes for bulk loads

### Transactions and concurrency control

- ACID: atomicity, consistency, isolation, durability
- Schedules, conflicts and conflict serializability; the precedence-graph theorem; view serializability (NP-complete to test)
- Two-phase locking and strict 2PL; recoverable and cascadeless schedules
- Deadlocks: waits-for graph detection; wait-die and wound-wait prevention
- Timestamp ordering and the Thomas write rule
- MVCC: tuple versioning, snapshots, visibility rules, the commit log
- Isolation levels: read committed, repeatable read, serializable; dirty reads, non-repeatable reads, phantoms, lost updates and write skew
- Snapshot isolation and serializable snapshot isolation (dangerous structures)
- Critiques of the ANSI isolation definitions; Adya's graph-based definitions
- Row and table locks; lightweight versus heavyweight locks
- Vacuum: dead tuples, autovacuum, bloat, transaction-ID wraparound and freezing; long transactions as vacuum poison

### Recovery and replication

- Buffer policies: steal and no-force, and why they require undo and redo
- The write-ahead-logging rule
- ARIES: LSNs, pageLSN, dirty-page and transaction tables, analysis, redo and undo passes, compensation log records
- Checkpoints; full-page writes; synchronous commit
- Physical streaming replication and WAL archiving; point-in-time recovery
- Logical replication: publications, subscriptions, decoding across major versions
- Change data capture through replication slots, and the disk risk of a dead consumer
- Replica lag as an SLI; read-your-writes through sticky sessions or primary reads; failover caveats
- Two-phase commit in databases: prepared transactions holding locks
- External consistency with TrueTime and commit-wait
- Deterministic databases (Calvin)

### Data modelling and design

- Conceptual → logical → physical design; ER diagrams; weak entities; ISA hierarchies; foreign-key placement for 1:N and N:M
- Keys: natural, surrogate, UUID (random versus time-ordered), snowflake IDs; client versus database generation
- Money, units and time: integer minor units with explicit currency; `timestamptz` for instants; `date` for civil dates
- Hierarchies and graphs: adjacency lists, closure tables, path enumeration, nested sets
- Temporal data: valid time versus transaction time; slowly changing dimensions (type 2); as-of joins; preventing label leakage in feature queries
- JSONB versus columns, and the hybrid
- Soft delete, history tables, append-only audit; partial unique indexes
- Denormalization: trading write cost for reads; cache columns, aggregate tables, counters; refresh rules recorded in decision records
- Multi-tenancy: shared tables with `tenant_id`, schema or database per tenant; composite foreign keys; RLS as defence in depth; hot tenants
- Partitioning: range, list and hash; pruning; shard keys as locality keys; hot-key skew and sequential hotspots
- Schema evolution by expand and contract: add nullable, backfill, constrain, switch reads, drop; lock levels; concurrent index creation
- Data quality as constraints; deferral for cyclic foreign keys; EXCLUDE for ranges

### Operating databases

- Slow-query observability: `pg_stat_statements`, `auto_explain`, wait events; live triage with `pg_stat_activity`, `pg_blocking_pids`, cancel and terminate; idle-in-transaction sessions
- Connection pooling: session, transaction and statement modes and what transaction mode breaks; pool math (instances × pool ≤ `max_connections` minus reserved slots, with failover headroom)
- Backups: logical (`pg_dump`/`pg_restore`) versus physical with WAL archiving; restore drills to a new instance; RPO and RTO; HA and replicas are not backups
- Retention: dropping partitions versus mass deletes; cold-storage export
- Migrations as jobs: dirty state, advisory locks, expand/contract in CI, rollback plans; online index builds with `CREATE INDEX CONCURRENTLY` and lock timeouts on DDL
- Application data access: N+1 queries, ORM pitfalls, prepared statements, transaction boundaries, keyset pagination with unique tiebreakers and signed cursors, repositories
- Testing SQL: Postgres service containers, seeded fixtures, fingerprint and golden assertions, migration up and down tests
- Managed relational databases: provisioning, private connectivity, connectors and proxies, IAM database authentication, backups and PITR, HA standbys and read replicas, flags

### NoSQL and choosing a store

- BASE versus ACID; the modern reality of multi-item transactions in NoSQL stores
- Key-value stores: hash-table abstraction, ordered keys for range scans, caches
- Document stores: collections, flexible fields, queries over structure; joins in application code
- Wide-column stores: column families, timestamps and versions, row-key design, salting, garbage-collection policies
- Graph databases: nodes and edges for many-to-many data; sharding difficulty; adjacency lists in other stores
- NoSQL query models versus SQL: access patterns first; joins as application fan-out; outboxes instead of dual writes
- SQL or NoSQL: structured, relational, transactional data versus semi-structured, high-volume, high-IOPS data; polyglot persistence; anti-choices (a cache as the system of record, a warehouse on the checkout path, object or file storage as a database, ad-hoc joins on a wide-column store)

### Analytics and other engines

- OLTP versus OLAP; star and snowflake schemas; facts, dimensions, grain, conformed dimensions
- Warehouse cost shapes: bytes scanned, partitioning and clustering, column projection, required partition filters, on-demand versus reserved capacity, authorized views
- Cohorts, funnels, sessionization and retention with windowed SQL; half-open intervals
- Approximate aggregation: HyperLogLog and quantile sketches with error bars
- Globally distributed SQL dialects: interleaved tables, limits
- Full-text search with `tsvector` and `tsquery`; vector similarity with `pgvector`; hybrid lexical and vector ranking; isolating search from OLTP

### Exercises

- From scratch in Go: bag relations with NULL logic; a schema registry with constraints; window functions as framed iterators; slotted pages with out-of-line storage; a clock-sweep buffer pool; a B-tree and an inverted index; iterator-model executor nodes with spills; histograms and selectivity estimates; an MVCC visibility simulator with a deadlock detector; a mini WAL with replay
- From scratch: an LSM-tree key-value store with a memtable, sorted runs, compaction and a Bloom filter per run
- Plan prediction: predict, then `EXPLAIN`, for joins, indexes, spills, warm and cold caches, skewed statistics and isolation anomalies
- Proofs: Armstrong completeness, the lossless-join test, the precedence-graph theorem, the 2PL theorem
- A checkout schema that cannot oversell under concurrency, with idempotency keys, minor-unit money and an isolation-level decision record
- Audit invariants under fault injection; cash-basis monthly revenue in SQL
- Keyset pagination, covering indexes and N+1 detection; a slow query rescued from its plan
- Primary and standby locally; replica lag; backup, restore and PITR drills
- A connection-pool sizing check with a failing test for over-subscription
- A migration run as a one-off job with an advisory lock
- Store selection for clickstreams, leaderboards, carts and lookup tables
- **Reasoning drills**
  - Predict plan shape, row counts and run time before `EXPLAIN ANALYZE`
  - Prove or refute a schedule's serializability from its precedence graph
  - Estimate table, index and buffer-pool sizes for a billion-row table
  - Choose an isolation level by the anomalies the workload can tolerate, as a decision record

## Distributed Systems & Large-Scale System Design

**Prerequisites:** networking (TCP, DNS, load balancing, latency numbers); databases (transactions, isolation, replication, indexes); concurrency (locks, happens-before, memory models); probability (order statistics, balls into bins, the birthday bound); queueing (Little's law, utilization); partial orders; hashing and consistent hashing basics.

**Depth bar:** a graduate distributed-systems course with replication and consensus labs plus staff-level system-design interviews: impossibility results proved, protocols implemented and tested under injected faults, designs sized with numbers.

**Capstone:** a replicated, partitioned key-value store with consensus and a client library, tested under partitions, crashes and clock skew with a linearizability checker, and its design written up and defended with capacity numbers.

### Foundations

- **System models**
  - Synchronous, partially synchronous and asynchronous timing
  - Crash-stop, crash-recovery, omission and Byzantine failures
  - Fair-loss versus reliable links
  - Failure detectors: perfect versus eventually perfect; a timeout means only "suspected"
  - The eight fallacies of distributed computing
- **Time and order**
  - Happens-before as a partial order
  - Lamport clocks; vector clocks capture causality exactly
  - Physical clock synchronization (NTP); bounded uncertainty with TrueTime and commit-wait
  - Consistent snapshots (Chandy–Lamport)
- **Consistency**
  - Weak, eventual and strong consistency
  - Linearizability versus sequential, causal and eventual consistency
  - Serializability versus strict serializability
  - Session guarantees: read-your-writes, monotonic reads
  - CAP as proved by Gilbert and Lynch, with what it does not say; PACELC; choosing CP or AP
- **Impossibility results**
  - The Two Generals problem
  - FLP: no deterministic asynchronous consensus with one crash; bivalence; escapes via partial synchrony, randomization and failure detectors

### Consensus and coordination

- The consensus problem: agreement, validity, termination
- Single-decree Paxos (prepare/promise, accept/accepted) and Multi-Paxos
- Raft: terms and leader election, log replication, log matching and leader completeness, the commit rule, membership change
- State-machine replication
- Coordination services built on consensus: Chubby, ZooKeeper, etcd; leader election and distributed locks; fencing
- Byzantine fault tolerance: n ≥ 3f + 1; PBFT's three phases; why cloud control planes use crash-fault consensus

### Replication

- Primary–replica replication; read replicas; promotion on primary failure
- Multi-primary replication and write conflicts
- Chain replication
- Leaderless, Dynamo-style replication: read repair, hinted handoff, Merkle-tree anti-entropy, sloppy quorums
- Quorums: R + W > N by pigeonhole; W > N/2 against conflicting writes; majority-quorum availability Σ C(N,k)pᵏ(1 − p)^(N−k)
- CRDTs as join-semilattices: G-Counter, PN-Counter, OR-Set; operational transformation
- Durability: probability of losing all r copies within a repair window; re-replication speed

### Availability

- Active-passive (hot and cold standby) and active-active fail-over
- Availability in nines: downtime per year, month, week and day for 99.9% and 99.99%
- Series availability (multiply availabilities) and parallel availability (multiply unavailabilities)
- Correlated failures and failure domains (zones, regions, releases)

### Partitioning

- Federation (functional partitioning) by domain
- Sharding: shard keys, hot keys, rebalancing, cross-shard queries, replication per shard
- Denormalization to avoid distributed joins
- Consistent hashing: expected 1/(n + 1) key movement; Θ(log n / n) arcs and virtual nodes; rendezvous hashing; jump consistent hash
- Scatter-gather queries

### Distributed transactions

- Two-phase commit and its blocking window; why three-phase commit fails under partitions
- Two-phase commit over Paxos groups
- Sagas: local transactions with compensating transactions; choreography versus orchestration; no isolation between steps
- Exactly-once delivery as effectively-once: idempotence plus deduplication
- The transactional outbox and inbox; idempotent consumers

### Caching at scale

- Where to cache: client, CDN, reverse proxy, web server, database, application
- What to cache: rows, query results, serialized objects, rendered HTML; query-level versus object-level invalidation
- Update strategies: cache-aside, write-through, write-behind, refresh-ahead
- Cache internals: TTLs, sampled LRU approximation; sharded caches by consistent hashing
- Caching theory: effective latency T = h·t_hit + (1 − h)·t_miss; Belady's optimum; LRU's k-competitiveness; Zipf popularity; working sets
- Consistency: TTLs bound staleness; leases against thundering herds and stale sets

### Asynchronism and flow control

- Message queues versus task queues; workers; scheduled tasks
- Back-pressure with bounded queues and 503s
- Load shedding versus queueing; Little's law for queue bounds
- Token-bucket arrival curves (at most b + r·t over any interval) and network-calculus delay bounds
- When not to queue: cheap or real-time work

### Stream and batch processing

- MapReduce and dataflow; lineage-based recovery
- MapReduce job patterns: count by key, dedup, group-and-filter, sort by moving the count into the key
- Event time versus processing time
- Windows: tumbling, sliding, session
- Watermarks and late data
- Exactly-once processing
- Heavy hitters and approximate counting with bounded memory

### Performance at scale

- Performance versus scalability; latency versus throughput
- Vertical versus horizontal scaling; stateless clones with external session stores
- The tail at scale: fan-out amplification; hedged and tied requests
- The iterative scaling loop: load test → profile → fix the bottleneck → repeat
- Back-of-the-envelope estimation: users, requests per second, read:write ratio, storage per year

### Testing and verification

- Fault injection in the Jepsen style
- Deterministic simulation testing
- Linearizability checking of recorded histories (NP-complete in general; per-key partitioning)

### System design method

- The four-step interview method: use cases and constraints, high-level design, core components, scaling
- Scaling a web service from one box to millions of users: single box; static content to object storage and a managed database on private networking; load balancer, multi-zone web tier and database fail-over; read caches, stateless sessions and read replicas; autoscaling, configuration management and monitoring; warehousing, NoSQL, sharding and asynchronous workers
- Real-world systems and their lessons: MapReduce, Spark, Storm, Bigtable, HBase, Cassandra, Dynamo, MongoDB, Spanner, Memcached, Redis, GFS, HDFS, Chubby, Dapper, Kafka, ZooKeeper
- Company architectures as case studies: Amazon (service-oriented decomposition), Dropbox (metadata versus block storage), Facebook (memcached at scale, TAO, photo storage, live fan-out), Flickr and Pinterest (sharded MySQL and caching), Instagram (sharded PostgreSQL and Redis), Netflix (CDN and resilient microservices), Twitter (timelines and the firehose), Tumblr (dashboard fan-out), WhatsApp (persistent connections), YouTube (video storage and sharding), Uber (microservice sprawl), Stack Overflow (few large machines plus caching), PlentyOfFish (vertical database scaling), Salesforce (multi-tenant relational scale), TripAdvisor (read-heavy caching), DataSift (stream filtering), ESPN (spiky traffic), Justin.tv (live video ingest), Mailbox (queues under sudden growth), Cinchcast (media pipelines), Playfish (social-gaming load)

### Design techniques

- Blob storage with only locations in the database
- Short links and unique IDs: Base62 encodings, collision probability, counters and range allocators, Snowflake-style IDs and clock skew
- Log analytics into a warehouse
- Expiry and cleanup with native TTLs or sweepers
- Fan-out on write versus on read; the celebrity problem; active-user timelines
- Search: tokenization, inverted indexes, ranking, in-memory hot indexes
- Crawler frontiers, URL and content dedup with signatures, freshness, politeness
- Categorization dictionaries and budget alerts
- Graph traversal at scale: sharded adjacency, bidirectional BFS, precomputation
- Notification services through queues

### Exercises

- From scratch in Go: MapReduce; a linearizable key/value server; Raft (election, log replication, persistence, snapshots); a fault-tolerant key/value service on Raft; a sharded key/value service
- From scratch: Lamport and vector clocks; consistent hashing with virtual nodes and measured key movement; a quorum-replicated register with read repair; a Merkle-tree anti-entropy sync
- From scratch: a distributed rate limiter; an outbox relay with idempotent consumers; a Snowflake-style ID generator
- Designs: Pastebin or a URL shortener; a Twitter timeline and search; a web crawler; a personal-finance aggregator; social-network shortest paths; a key-value cache for search queries; sales rank by category; a service scaled from one box to millions of users
- Designs: file sync (chunking, content-hash dedup, delta sync), a search engine, collaborative documents (OT and CRDTs), a Redis-like store, a Memcached-like cache, a recommendation system, a chat app with presence, photo sharing, a news feed, graph search, a CDN, trending topics, random-ID generation, top-k requests in an interval, multi-datacentre serving, an online multiplayer card game, a garbage-collection service, an API rate limiter, a stock-exchange matching engine
- Proofs: quorum intersection, CAP's two-node argument, consistent-hashing movement
- **Reasoning drills**
  - Back-of-the-envelope capacity for every design before drawing it
  - Prove safety properties (quorum intersection, log matching) and build failure schedules that break weakened variants
  - Predict behaviour under partitions, clock skew and message loss, then inject the faults and compare
  - Find the assumption each design leans on most and show what breaks without it

## Security, Cryptography, Privacy & Compliance

**Prerequisites:** number theory (modular arithmetic, Euler's theorem, discrete logarithms); probability (the birthday bound, negligible advantage); networking (HTTP, cookies, TLS, DNS, BGP); operating-system isolation (namespaces, cgroups, capabilities); databases (SQL, row-level security); distributed systems (consensus, replication); an HTTP service in a programming language.

**Depth bar:** a top-university computer-security and applied-cryptography course with attack labs plus a cloud-security professional exam: every attack reproduced on your own fixtures, every defence explained by the property it restores, every primitive's security notion stated.

**Capstone:** a threat-modelled application on Google Cloud with least-privilege IAM, managed secrets, perimeter controls, audit logging and detections, attacked by your own scripted tests and closed with an incident-response exercise and written report.

### Principles and economics

- Confidentiality, integrity, availability; least privilege; defence in depth; assume breach; zero trust
- Saltzer and Schroeder's principles: economy of mechanism, fail-safe defaults, complete mediation, open design, separation of privilege, least privilege, least common mechanism, psychological acceptability
- The reference monitor and the trusted computing base
- Shared responsibility across IaaS, PaaS, SaaS and serverless
- Security economics: residual risk in decisions, attacker cost versus user friction, MTTD and MTTR
- Privacy versus security tensions: retention, employee monitoring, minimization

### Threat modelling

- Attacker models: web, network, cloud administrator, co-tenant, insider
- Trust boundaries, planes (front end, API, admin, service-to-service, data, CI) and asset inventories with data classes
- STRIDE mapped to the property each threat violates, applied per data-flow element and trust boundary
- Attack trees: OR as minimum cost, AND as sum; probabilities; raising the cost of the cheapest path
- Abuse cases converted into deny tests
- MITRE ATT&CK cloud techniques (including cloud instance metadata credential access) mapped to detections
- Distributed-system threats: operator honesty, poisoned configuration across regions, the control plane as its own threat model
- Risk as likelihood × impact: an ordinal heuristic, not arithmetic

### Access-control models

- The access-control matrix; ACLs versus capabilities
- Discretionary versus mandatory access control
- Bell–LaPadula (no read up, no write down) and Biba
- Clark–Wilson: well-formed transactions, separation of duty
- RBAC (users, roles, permissions, sessions, hierarchies), ABAC and ReBAC
- Relationship-based authorization at scale: Zanzibar-style tuples and consistency tokens

### Cryptography

- **Foundations and hygiene**
  - Goals (confidentiality, integrity, authenticity) and security games: IND-CPA, IND-CCA, EUF-CMA
  - Kerckhoffs's principle; why roll-your-own fails (ECB patterns, XOR stream reuse, Base64 as "encryption", compress-then-encrypt)
  - Provable security: efficient adversaries, advantage, negligible functions, reductions, the hybrid argument
  - Perfect secrecy and the one-time pad; Shannon's |K| ≥ |M|; the two-time pad
- **Symmetric encryption**
  - PRGs, PRFs and PRPs; AES as a PRP; the PRP/PRF switching lemma and retiring 64-bit blocks
  - Modes: ECB, CBC, CTR; deterministic schemes cannot be CPA-secure
  - Padding oracles and CTR nonce reuse
  - Authenticated encryption: AES-GCM and ChaCha20-Poly1305; associated data; nonce-reuse catastrophe; tag truncation; XChaCha nonces
- **Hashes and MACs**
  - Collision, second-preimage and preimage resistance; the 2^(n/2) birthday attack
  - SHA-2 and SHA-3; Merkle–Damgård and length extension; sponges; the random-oracle model
  - HMAC, KMAC and Poly1305; CBC-MAC's fixed-length limit
  - Encrypt-then-MAC versus MAC-then-encrypt (generic composition)
  - HKDF extract-and-expand with explicit `info`
- **Randomness**
  - OS CSPRNGs (`getrandom`, `SecureRandom`); entropy; nonces and IVs
  - VM snapshot cloning of PRNG state; low-entropy boots
- **Public-key cryptography**
  - Groups, generators; discrete log, CDH and DDH assumptions
  - Diffie–Hellman and ECDH; forward secrecy; small-subgroup and invalid-curve attacks
  - ElGamal; RSA as a trapdoor permutation; textbook RSA's malleability; RSA-OAEP
  - Hybrid encryption (KEM/DEM)
- **Signatures**
  - Hash-and-sign; RSA-PSS, ECDSA, Schnorr via Fiat–Shamir, EdDSA/Ed25519
  - ECDSA nonce reuse revealing the key; deterministic nonces
  - Algorithm-confusion and agility attacks
- **Key exchange and protocols**
  - Authenticated key exchange; SIGMA; the TLS 1.3 key schedule
  - The Dolev–Yao attacker; nonces and freshness; replay and reflection; Lowe's attack on Needham–Schroeder
  - Formal protocol verification (Tamarin, ProVerif) and TLS 1.3's co-design with analysis
- **PKI and TLS**
  - X.509 certificates, chains, hostname verification, revocation, Certificate Transparency, pinning trade-offs, ACME
  - TLS 1.2 versus 1.3; downgrade attacks; 0-RTT replay; HSTS
  - mTLS; application-layer AEAD and field-level encryption
  - TLS interception and its risks
- **Password cryptography**
  - Online versus offline guessing; guessing entropy
  - Memory-hard KDFs (Argon2id, scrypt) and bcrypt; area × time cost
  - Salts, peppers held in a key manager, versioned records and rehashing
- **Key management**
  - Key hierarchies and envelope encryption (DEKs and KEKs); rewrap versus re-encrypt
  - Rotation with dual-key overlap; key-purpose separation; separation of duty
  - KMS, HSM, external key managers; customer-managed versus customer-supplied versus provider-managed keys
  - Key compromise response and crypto agility; key inventories; JWT cutoff timestamps
- **Side channels**
  - Timing attacks on comparisons; constant-time APIs; uniform errors
  - Cache and speculative-execution side channels on shared hardware
- **Privacy-enhancing cryptography (survey)**: trusted execution environments, multi-party computation, homomorphic encryption, zero-knowledge proofs
- **Post-quantum cryptography**
  - Shor and Grover; AES-256 under Grover
  - ML-KEM (FIPS 203), ML-DSA (FIPS 204), SLH-DSA (FIPS 205)
  - Hybrid key exchange in TLS; harvest now, decrypt later; inventories of long-lived keys
- **Engineering checklist**: vetted libraries (Tink, libsodium, standard libraries), AEAD, CSPRNG, KMS-held KEKs, no tokens in URLs, verification on, algorithm allow-lists, versioned password records, inventories

### Authentication and sessions

- Authentication versus authorization
- Session hijacking; session fixation and ID rotation; idle and absolute timeouts
- Cookie attributes and theft vectors: `Secure`, `HttpOnly`, `SameSite`, `Path`, host-only cookies, the `__Host-` prefix, subdomain injection
- CSRF: synchronizer and HMAC double-submit tokens, Origin checks, SameSite as defence in depth
- JWT pitfalls: `alg=none`, RS256-to-HS256 confusion, attacker-controlled `kid`/`jku`; claim validation (iss, aud, exp, nbf, jti)
- OAuth 2.0 as delegation: authorization code with PKCE, exact redirect allow-lists, bound `state`, mix-up defences, no implicit grant
- OpenID Connect ID tokens and nonces
- SAML and XML signature wrapping; XXE in SAML parsers
- Kerberos: tickets, ticket-granting service, pass-the-ticket and offline cracking of service tickets
- Credential stuffing and password spraying: breach blocklists, rate limits, bot signals, generic errors
- MFA: TOTP, push fatigue and number matching, SIM swap, phishing-resistant WebAuthn and passkeys
- Account recovery as strong as login: hashed single-use tokens, out-of-band notification, step-up
- Unguessable session tokens: success probability s / 2ᵏ
- Identity federation and SSO

### Authorization flaws

- IDOR/BOLA: server-side checks on every object; tenant in every query
- Broken function-level authorization: deny by default, explicit permissions
- Mass assignment: allow-listed DTO fields; server-side prices and roles
- Confused deputies: audience-restricted tokens, capability tokens, per-service least privilege
- Object-level authorization as a predicate over principal, action and object

### API abuse

- Rate-limit algorithms: token bucket, leaky bucket, fixed and sliding windows; 429 with `Retry-After`; layered keys (tenant, user, IP); explicit fail modes
- Where to place limits: edge, gateway and application
- Bot management and scraping; risk scores and device signals
- GraphQL depth and cost limits, persisted queries, introspection off in production
- Pagination and enumeration abuse
- Business-logic abuse: coupon stacking, negative quantities, wallet races, loyalty farming
- Inventory hoarding and checkout abuse
- Expensive exports and fan-out abuse

### Denial of service

- L3/L4 volumetric floods (UDP, SYN) and anycast edge absorption
- Amplification and reflection; bandwidth amplification factors; ingress filtering (BCP 38)
- L7 floods on expensive endpoints
- Adaptive, ML-based protection and its learning period
- Slowloris, slow POST and slow read; server timeouts and connection limits
- Resource exhaustion: zip bombs, huge bodies, unbounded uploads, ReDoS
- Economic DoS: forced egress, logging, LLM tokens; budgets and kill switches; max instances × price as a bound
- Cache stampedes and retry storms: jittered TTLs, request coalescing, soft TTLs
- SYN cookies; attacker-versus-defender cost asymmetry

### Web application security

- The same-origin policy as a formal model: origins, reading versus sending, why CORS is not a CSRF defence
- CORS pitfalls and `postMessage` origin checks
- XSS (stored, reflected, DOM) and context-aware encoding
- Content Security Policy (nonces, hashes, report-only rollout) and Trusted Types
- Clickjacking and `frame-ancestors`
- Injection as data becoming syntax: SQL, command, path traversal; parameterized queries
- XXE and server-side template injection
- Unsafe deserialization
- Open redirects and header (CRLF) injection
- Log injection and forensic pollution
- Memory-safety bugs (buffer overflows, use-after-free) and mitigations (canaries, ASLR, NX, CFI); memory-safe languages; privilege separation and sandboxing
- WAF rules, bypasses and preview modes
- File uploads: type allow-lists, size limits, scanning, re-encoding, storage outside the web root
- The OWASP Top 10:2025: broken access control (including SSRF), security misconfiguration, software supply chain failures, cryptographic failures, injection, insecure design, authentication failures, software or data integrity failures, security logging and alerting failures, mishandling of exceptional conditions

### Cloud-specific attacks

- SSRF to instance metadata; DNS rebinding; metadata-header protections
- Public buckets and ACL mistakes; uniform bucket-level access; public-access prevention
- IAM privilege-escalation paths (acting as service accounts, broad owner roles); effective-policy analysis; deny policies; just-in-time break-glass
- Service-account key theft and sprawl; keyless workload identity federation
- Tenant isolation failures in queries, caches, jobs and logs
- VPC peering and shared-VPC trust mistakes; private service connections
- Serverless event injection; hypervisor-escape residual risk

### Network security and zero trust

- Perimeter myths; authenticated east-west traffic; micro-segmentation
- Lateral movement as graph reachability; attack graphs
- Egress exfiltration and DNS tunnelling; egress allow-lists and DNS monitoring
- BGP hijacks, DNS cache poisoning, dangling records and subdomain takeover; DNSSEC and RPKI
- Email authentication: SPF, DKIM and DMARC
- Identity-aware proxies versus VPNs
- Data-exfiltration perimeters around cloud APIs
- Control placement along the packet path
- Zero Trust Architecture (NIST SP 800-207): policy engine, administrator and enforcement point; BeyondCorp

### Containers and Kubernetes security

- Container escape patterns: privileged containers, `docker.sock` mounts, kernel exploits
- Privileged pods, `hostPath` and Pod Security Standards
- RBAC wildcards; per-workload service accounts
- Secrets in etcd, environment variables and image layers; CSI secret drivers; etcd encryption
- Admission control and supply-chain gates: digest pins, signed images, vulnerability gates
- Default-deny NetworkPolicy; service-mesh mTLS

### Supply chain

- Poisoned images, typosquatting and dependency confusion
- Poisoned CI/CD pipelines: fork PRs, self-hosted runners, secrets in logs
- SBOMs: meaning and limits
- Image signing, attestations and admission enforcement
- Secret sprawl in repositories, images, logs, traces and prompts; pre-commit scanning
- Build provenance and SLSA levels; hermetic builds

### Detection and incident response

- Log coverage and trail integrity: admin and data-access logs, immutable sinks in a separate project, retention, time sync
- Alert design: few high-precision detections, owners and runbooks
- Detection engineering for cloud techniques: key creation, anomalous IAM changes, honeytokens, public bindings, metadata access
- Containment on ephemeral compute: disable identities, revoke tokens, pin known-good revisions, preserve logs
- Playbooks: compromised service account or leaked key; public data exposure; ransomware and backup integrity
- Tabletop exercises: clocks, injects, scribes, time-to-contain

### AI and LLM application threats

- Security goals for ML systems: confidentiality, integrity and availability plus authentication, authorization and non-repudiation; trustworthy-ML dimensions (fairness, toxicity, safety, sustainability, explainability); threat models by attacker knowledge (white-box, black-box) and goal
- Prompt safety (harmful outputs) versus prompt security (attacks on the application)
- Direct and indirect prompt injection; separating instructions from data; output as untrusted input
  - Indirect channels: poisoned documents, emails and calendar invites, API responses, résumés
  - Impacts: data exfiltration, remote tool execution, denial of service, social engineering
- Prompt leaking: exposure of system prompts, intellectual property and reconnaissance for further attacks
- **Jailbreaking**
  - Taxonomy: language strategies (payload smuggling, modified instructions, stylized prompts and responses); rhetoric (innocent purpose, persuasion, alignment hacking, conversational coercion, Socratic questioning); imaginary worlds (hypotheticals, storytelling, role-play, world building); operational exploitation (many-shot examples, "unrestricted model" personas, meta-prompting)
  - White-box attacks: HotFlip gradient-guided flips; TextFooler synonym substitution; greedy coordinate gradient (GCG) adversarial suffixes optimized toward an affirmative reply, transferring across models, measured by attack success rate on AdvBench; AutoDAN readable suffixes
  - Black-box attacks: translation into low-resource languages; past-tense reformulation; context contamination with harmful in-context demonstrations; DeepWordBug character perturbations; PAIR (an attacker model refining prompts against a judge in a few dozen queries); instruction-centric harmful requests
  - Red teaming versus blue teaming
- Tool and agent abuse; excessive agency
- RAG data leakage; authorization at retrieval; per-tenant indexes
- Model and data poisoning, including poisoned federated updates; backdoors and trojan triggers; model hijacking; malicious serialized model files; signed models and private registries
- Model extraction by query-based distillation
- Shadow AI and sensitive pastes; secrets exposed to code assistants; legal and intellectual-property risk
- Adversarial examples (FGSM and optimization attacks) and robust training
- Membership inference and differentially private training
- The OWASP Top 10 for LLM Applications

### Isolation classes

- Noisy neighbours and isolation classes matched to sensitivity
- Confidential computing: what TEEs protect (memory from privileged observers) and what they do not

### Privacy

- Data classification (public, internal, confidential, restricted) and handling rules
- DLP and de-identification before analytics and prompts; purpose limitation
- Tokenization versus encryption; tokenizing card numbers to shrink PCI DSS scope
- Residency and sovereignty controls
- Re-identification through quasi-identifiers and linkage
- k-anonymity and its homogeneity and background-knowledge failures
- Differential privacy: ε-DP, the Laplace mechanism, composition, post-processing

### Compliance

- The CSA Cloud Controls Matrix as a coverage checklist with evidence paths
- PCI DSS, HIPAA, SOC 2 and FedRAMP: obligation → control → product → artifact; business associate agreements; regulated-workload controls

### Exercises

- From scratch: SHA-256 and HMAC checked against test vectors; HKDF; constant-time comparison
- From scratch: textbook RSA and Diffie–Hellman with small numbers, then the attacks that make them unsafe without padding and authentication
- From scratch: a JWT signer and verifier that rejects `alg: none` and algorithm confusion; TOTP codes per RFC 6238
- From scratch: a Merkle tree with inclusion proofs; Shamir secret sharing over a prime field
- From scratch: a token-bucket limiter with a proof of its arrival bound
- Attacks on purpose-built toys: a padding oracle, CTR nonce reuse, ECDSA nonce reuse, length extension
- Password storage with Argon2id records, rehashing and peppers
- Envelope encryption with customer-managed keys and a rotation drill
- A threat model for an order-placement flow: diagram, STRIDE table, abuse case, residual risk; attack trees converted into table-driven deny tests
- Session fixation, CSRF, JWT and OAuth attacks replayed against a deliberately vulnerable shop application, then fixed
- Server timeouts against slow-client attacks; SSRF-to-metadata defences; a public-bucket exposure response
- An abuse-resistant public API with quotas, bot signals and idempotent writes
- A leaked service-account key incident worked through a runbook; an incident-response tabletop
- An AI-gateway threat model; prompt-injection and RAG-leakage defences for an LLM application; a red-team harness of jailbreak and injection suites scored by attack success rate
- Proofs: one-time-pad secrecy, |K| ≥ |M|, deterministic encryption is not CPA-secure
- **Reasoning drills**
  - Name the cheapest attack on a design before listing its defences
  - Reduce a protocol's security to a stated assumption, then find the attack when that assumption is dropped
  - Estimate the cost in money and time of brute-forcing a key or password space
  - Decide the residual risk to accept, as a decision record with review triggers

## Software Delivery & Version Control

**Prerequisites:** the shell; hashing and Merkle structures; directed acyclic graphs and lowest common ancestors; queueing intuition (batch size and waiting time).

**Depth bar:** Git understood as data structures, and delivery practised at the level of a team that owns its production releases.

**Capstone:** a repository with branch protection, signed commits and CI, carrying one change through review, release, a failed rollout and a rollback.

### Git

- **Everyday Git**
  - Commits, branches, merges, rebases and tags
  - Conflict resolution
  - Remotes, pushing and pulling; pull requests
- **Git's data model**
  - Content-addressed objects: blobs, trees, commits, tags
  - The commit graph as a DAG and a Merkle structure: one hash authenticates the whole history
  - Refs and branches as pointers
  - Three-way merge against the merge base (a lowest common ancestor)
  - Rebase as replay that creates new commits
  - Object IDs as SHA-1 hashes (with a SHA-256 object format); zlib-compressed loose objects and delta-compressed packfiles; the index (staging area)
- **The Git command line**
  - Setup and inspection: `git config --global`, `git init`, `git clone`, `git status`, `git log --oneline --graph --all`, `git show`, `git diff` and `git diff --staged`, `git blame`
  - Recording: `git add -p`, `git commit --amend`, `git restore` and `git restore --staged`, `git rm`, `git mv`, `.gitignore`
  - Branching: `git switch -c`, `git branch -d`, `git merge --no-ff`, `git rebase` and `git rebase --onto`, `git cherry-pick`, `git revert`, `git reset --soft`, `--mixed` and `--hard`, `git stash push` and `pop`
  - Remotes: `git remote -v`, `git fetch --prune`, `git pull --rebase`, `git push -u`, `git push --force-with-lease` instead of `--force`, `git tag -a` and pushing tags
  - Recovery and search: `git reflog`, `git bisect start`, `good`, `bad` and `run`, `git grep`, `git worktree add`
  - Plumbing: `git hash-object -w`, `git cat-file -t` and `-p`, `git ls-tree`, `git update-index`, `git write-tree`, `git commit-tree`, `git update-ref`, `git rev-parse`, `git merge-base`

### Delivery models

- SDLC models; Agile and Scrum basics
- Trunk-based development versus GitFlow
- Code-review culture and the evidence on review
- Small batches read as queueing: smaller batches wait less
- The four DORA metrics: deployment frequency, lead time for changes, change failure rate, time to restore service

### The profession

- The ACM Code of Ethics and Professional Conduct
- Permissive versus copyleft licences and why a dependency's licence matters
- Responsibility for privacy in system design

### Exercises

- From scratch: a mini Git storing blobs, trees and commits as zlib-compressed, SHA-1-addressed objects, with `log`, refs and a merge-base finder
- A commit reconstructed by hand with plumbing commands, then checked with `git cat-file`
- A three-way merge conflict resolved and its merge base explained
- The four DORA metrics measured for a small project
- **Reasoning drills**
  - Predict merge and rebase outcomes on a commit graph before running them
  - Reason about batch size and lead time with Little's law
  - Recover from a mistaken hard reset using only the reflog, predicting each step first

## Cloud Computing Core: Virtualization, Well-Architected, Economics & IAM

**Prerequisites:** operating systems (virtual memory, page tables, the TLB, privileged instructions, namespaces and cgroups); probability (means and standard deviations of sums, the exponential distribution); availability arithmetic; access-control models; OAuth and OIDC tokens.

**Depth bar:** cloud architecture at professional-certification depth together with the virtualization mechanisms beneath it: every service model explained down to the isolation it rests on, every cost claim computed.

**Capstone:** a well-architected review of a workload you built: a pillar-by-pillar assessment, an IAM model with no basic roles, a cost model checked against the bill, and a remediation plan carried out.

### What cloud computing is

- The NIST definition: on-demand self-service, broad network access, resource pooling, rapid elasticity, measured service
- Service models: IaaS, PaaS, SaaS, and FaaS placed against the definition
- Deployment models: public, private, community, hybrid, multi-cloud
- Resource pooling as statistical multiplexing: pooled capacity nμ + zσ√n versus n(μ + zσ); correlated demand removes the saving
- The economics of elasticity: fixed cost to variable cost; utilization-adjusted break-even; asymmetric under- and over-provisioning costs
- Serverless: compute decoupled from storage, scale to zero, per-use billing; no addressable state, cold starts, communication through storage
- Shared responsibility as a partition of controls that moves up the stack while identity and data stay with the customer

### Virtualization and containers

- Type 1 and type 2 hypervisors; how a VM works
- Popek and Goldberg's requirements and trap-and-emulate theorem; x86's failure and binary translation, paravirtualization and hardware support (VT-x, AMD-V)
- Memory virtualization: shadow page tables versus nested paging; (g + 1)(h + 1) − 1 references per nested walk; huge pages
- MicroVMs and user-space kernels (Firecracker, gVisor)
- Containers as namespaces and cgroups; image layering and immutability
- Isolation classes and attack surface: process, container, sandbox, microVM, VM, dedicated host

### Architecture patterns and well-architected frameworks

- High availability, fault tolerance, horizontal versus vertical scaling
- Disaster recovery patterns: backup and restore, pilot light, warm standby, multi-site active-active; RTO and RPO
- Reliability mathematics: MTBF, MTTR, A = MTBF / (MTBF + MTTR); exponential failures; durability of r replicas
- k-out-of-n redundancy; common-mode failures and failure domains
- Well-architected frameworks compared
  - Google Cloud Well-Architected Framework: operational excellence; security, privacy and compliance; reliability; cost optimization; performance optimization; sustainability; cross-pillar perspectives for AI and ML and for financial services
  - AWS Well-Architected: operational excellence, security, reliability, performance efficiency, cost optimization, sustainability
  - Azure Well-Architected: reliability, security, cost optimization, operational excellence, performance efficiency
- Pillars as quality attributes; design reviews as quality-attribute scenarios

### Cloud economics and FinOps

- On-demand, committed-use and reserved pricing; sustained-use discounts; spot and preemptible capacity
- Commitment break-even: pays off when utilization exceeds 1 − d
- Spot as expected cost (1 − d)(1 + w); checkpointing and Young's optimal interval τ ≈ √(2δM)
- Total cost of ownership; marginal versus average cost; forecasting spend with confidence intervals
- Unit economics: cost per request, tenant or transaction; idle-capacity cost; cost curves that outgrow traffic as architecture defects
- Cost visibility tooling, budgets and alerts, labels and tags for allocation, billing exports
- Three budgets per system: money, errors and quota
- Carbon as a cost-adjacent signal: region choice and footprint reports

### Cloud IAM concepts

- Principals, roles and policies; resource hierarchies (organization, folder or OU, project or account)
- Role types: basic, predefined, custom
- Policy inheritance as a union of grants; default deny; explicit deny overriding allow
- Conditional bindings and attribute-based control
- Least privilege as a minimization problem; automated policy reasoning with SMT solvers
- The safety problem: undecidable in the general access-matrix model; why restricted IAM models are analysable
- Service accounts, managed identities and attached identities
- Workload identity federation as a trust statement exchanging external OIDC tokens for short-lived credentials; workforce federation for people
- Confused deputies and capabilities

### Exercises

- A shared-responsibility matrix per service model
- Pooled versus separate capacity computed for independent tenants
- From scratch: a cost model for on-demand, committed and spot capacity with checkpointing and interruption rates
- An RTO/RPO plan for each disaster-recovery pattern
- From scratch: an IAM policy evaluator (allow, deny, conditions, inheritance) that finds least-privilege violations and escalation paths
- **Reasoning drills**
  - Estimate a workload's monthly bill from first principles before using a pricing calculator
  - Find the minimum permissions for a task and argue that no escalation path exists
  - Name the binding constraint (cost, compliance, latency or skills) in a migration decision before comparing options

## The Architect's Practice: Decisions, Strategy & Career

**Prerequisites:** architecture documentation (decision records, C4 views, quality-attribute scenarios); cost modelling; expected value and probability; delivery practices (canaries, feature flags, expand/contract migrations); SLOs and postmortems; technical reading and writing.

**Depth bar:** staff and principal engineer practice: decisions written, reviewed and revisited against outcomes; strategy defended to engineers and to executives.

**Capstone:** a technical strategy and migration plan for a realistic system, with decision records, a premortem, a build-or-buy analysis and a review held under adversarial questions.

### Making decisions

- Framing: requirement, constraints, the quality-attribute scenario served
- At least three options, always including doing nothing and buying
- Judging against scenarios and cost; premortems; review dates and reversal evidence
- Reversibility: one-way and two-way doors; making a one-way door two-way with flags, ports and adapters, expand/contract changes or rehearsed rollbacks
- Second-order effects: who operates it, what it makes easy or hard next, what the team must learn

### Decision theory

- Decision trees: choice nodes, chance nodes, payoffs, folding back
- Expected utility and risk aversion; paying for redundancy
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

## DevOps & SRE: Docker, Kubernetes, NGINX, CI/CD, Infrastructure as Code, Observability

**Prerequisites:** Linux (processes, namespaces, cgroups, capabilities, seccomp, file systems); networking (HTTP, TLS, load balancing, DNS); Git; Raft and replicated key-value stores; bin packing and DAGs; queueing (Little's law); percentiles and histograms; availability arithmetic.

**Depth bar:** SRE practice at the level of owning an on-call service: every component deployed from your own manifests and pipelines, every alert tied to an SLO, every failure mode drilled.

**Capstone:** a service on GKE or Cloud Run deployed by Terraform through a CI/CD pipeline with progressive delivery, SLOs with burn-rate alerts, dashboards and traces, and a game-day failure written up as a blameless postmortem.

### Docker

- Images versus containers; the union filesystem (overlay lower and upper layers, copy-up, whiteouts) and why deleted files persist in earlier layers
- Images as content-addressed Merkle structures: manifests, configs, layer digests; tags as mutable pointers, digests as pins
- Dockerfiles: `FROM`, `RUN`, `COPY`, `ENTRYPOINT` versus `CMD`; multi-stage builds
- Layer caching as memoization: cache keys and instruction ordering
- Reproducible images: digest-pinned bases, fixed timestamps, stable file order
- Container networking modes (bridge, host, none); volumes, bind mounts and tmpfs
- Docker Compose for local multi-container development
- Registries, tagging strategy and image scanning
- Container security: non-root users, minimal and distroless bases, secrets anti-patterns; the shared kernel in every container's TCB
- BuildKit daemon builds; the Docker Engine API from code
- **The Docker command line**
  - Building: `docker build -t name:tag -f Dockerfile --target stage --build-arg KEY=value .`; `docker buildx build --platform linux/amd64,linux/arm64 --push`; build secrets with `--secret`; cache import and export with `--cache-from` and `--cache-to`
  - Running: `docker run -d --rm --name -p host:container -e KEY=value --env-file -v volume:/path --mount --network --memory --cpus --read-only --user --cap-drop ALL`
  - Inspecting: `docker ps -a`, `docker logs -f`, `docker exec -it container sh`, `docker inspect` with `--format` Go templates, `docker stats`, `docker top`, `docker history`, `docker image ls`, `docker system df`
  - Distributing: `docker login`, `docker tag`, `docker push`, `docker pull` by digest (`image@sha256:…`), `docker buildx imagetools inspect` for multi-platform manifests
  - Cleaning up: `docker stop`, `docker rm`, `docker image prune`, `docker system prune`; `docker network create` and `ls`; `docker volume create` and `ls`
  - Compose: `docker compose up -d --build`, `docker compose ps`, `docker compose logs -f service`, `docker compose exec`, `docker compose down -v`; profiles and override files

### Kubernetes

- **Architecture**
  - Control plane: API server, etcd, scheduler, controller manager; worker nodes: kubelet, kube-proxy, container runtime
  - etcd replicated by Raft: 2f + 1 members tolerate f failures; revision history, compaction and re-listing
  - Level-triggered reconciliation (observe, diff, act) versus edge-triggered handlers
  - The Borg → Omega → Kubernetes lineage
- **Workloads**: Pods, ReplicaSets, Deployments, StatefulSets, DaemonSets, Jobs and CronJobs
- **Networking**: Services (ClusterIP, NodePort, LoadBalancer), Ingress and Ingress controllers, the CNI model, NetworkPolicies
- **Configuration and storage**: ConfigMaps, Secrets, environment injection; PersistentVolumes, PersistentVolumeClaims, StorageClasses, dynamic provisioning
- **Scheduling and scaling**
  - Scheduling as NP-hard bin packing solved by filter-and-score; the lower bound ⌈Σ requests ÷ node capacity⌉
  - Node affinity, taints and tolerations, pod anti-affinity, topology spread constraints
  - Requests versus limits: CFS quota throttling per period; OOM kills over the memory limit
  - Horizontal and Vertical Pod Autoscalers; Cluster Autoscaler; PodDisruptionBudgets
- **Security**: RBAC, Pod Security Standards, admission controllers
- **Extending**: Helm charts, templating and releases; CustomResourceDefinitions and Operators
- **The kubectl command line**
  - Contexts and namespaces: `kubectl config get-contexts`, `kubectl config use-context`, `kubectl config set-context --current --namespace`; the kubeconfig file
  - Reading: `kubectl get` with `-o wide`, `-o yaml`, `-o json`, `-o jsonpath` and `custom-columns`, `-l` label selectors, `-A` for all namespaces, `--watch`; `kubectl describe`; `kubectl get events --sort-by=.lastTimestamp`; `kubectl explain`; `kubectl api-resources`
  - Changing: `kubectl apply -f` and `-k` (Kustomize); `kubectl diff -f`; `kubectl create deployment --dry-run=client -o yaml` to generate manifests; `kubectl expose`; `kubectl delete`; `kubectl label`, `annotate` and `patch`
  - Rollouts and scaling: `kubectl rollout status`, `history`, `undo` and `restart`; `kubectl set image`; `kubectl scale --replicas`; `kubectl autoscale`
  - Debugging: `kubectl logs -f -c container --previous`; `kubectl exec -it pod -- sh`; `kubectl port-forward svc/name 8080:80`; `kubectl debug` with ephemeral containers; `kubectl cp`; `kubectl top pods` and `nodes`
  - Nodes and access: `kubectl cordon`, `kubectl drain --ignore-daemonsets`, `kubectl uncordon`, `kubectl taint`; `kubectl auth can-i --as`
- **The Helm command line**: `helm repo add` and `update`; `helm search repo`; `helm show values`; `helm install` and `helm upgrade --install` with `-f values.yaml`, `--set`, `--atomic` and `--wait`; `helm template` and `helm lint`; `helm list`, `helm history`, `helm rollback`, `helm uninstall`; `helm create`, `helm package`, `helm dependency update`
- **Managed Kubernetes**: provider-run control planes; fully managed versus self-managed node modes; node auto-provisioning; cloud identity for pods; DigitalOcean Kubernetes

### NGINX and API gateways

- Configuration: server blocks, location matching, directives
- Upstreams and load-balancing methods: round robin, `least_conn`, `ip_hash`
- TLS termination, HTTP-to-HTTPS redirects, HTTP/2
- Caching and static content; stale-while-revalidate
- NGINX as a Kubernetes Ingress controller
- Server architectures: Flash's AMPED design; SEDA; NGINX's worker event loops
- A proxy as a queue: Little's law for upstream and client connections
- The Kong API gateway: services, routes, consumers, plugins, its Postgres store and admin API, Lua plugins

### CI/CD

- Pipeline stages: build → test → package → deploy; artifact repositories
- Deployment strategies: rolling (surge and unavailable settings), blue-green, canary; choosing from a scenario
- Progressive delivery as risk control: canary fraction and the error count as a test statistic
- Continuous delivery: every commit a release candidate
- GitOps: declarative state, Git as source of truth, reconciliation loops; Argo CD and Flux
- Tooling: GitHub Actions, Jenkins, GitLab CI
- Build-system theory: schedulers (topological, restarting, suspending) and rebuilders (dirty bits, trace checking, constructive traces); correctness and minimality; timestamp versus hash rebuilders; shared remote caches
- Pipelines as DAGs: the critical path bounds lead time
- Supply-chain integrity in the pipeline: reproducible builds; SLSA v1.0 Build levels L1–L3
- Platform engineering: golden-path service templates; preview environments destroyed on merge
- Database changes in deploys: expand/contract and migrations as jobs; SQL tests in CI

### Infrastructure as code

- Declarative versus imperative provisioning
- Declarative convergence: plan as diff(desired, observed); idempotent and convergent applies; convergent operators and promise theory
- Plans as graph walks: topological creation, reverse destruction, parallelism, cycles as errors
- State files: mapping addresses to real IDs; drift; locking against lost updates; remote state
- Terraform: providers, resources, data sources, variables and outputs, modules, workspaces, `count` and `for_each`, references and `depends_on`; `import` and `moved` blocks; the dependency lock file
- **The Terraform command line**
  - `terraform init` with `-backend-config` and `-upgrade`; `terraform fmt -recursive`; `terraform validate`
  - `terraform plan -out=tfplan` with `-var` and `-var-file`; `terraform show -json tfplan` for policy checks; `terraform apply tfplan`; `terraform destroy`
  - `-replace` to recreate one resource; `-refresh-only` to reconcile drift into state; `-target` as an emergency tool only
  - State: `terraform state list`, `show`, `mv` and `rm`; `terraform import`; `terraform force-unlock`
  - `terraform output -json`; `terraform workspace new` and `select`; `terraform providers lock`; `terraform console`; `terraform graph`
- Static IaC scanning (Checkov, tfsec, Trivy) before plan
- Policy as code evaluated over the plan
- Immutable versus mutable infrastructure; snowflake servers

### Observability

- Metrics, logs and traces
- Counters, gauges and histograms; mergeable histograms versus unmergeable percentiles
- Head-based versus tail-based trace sampling and their biases
- Label cardinality and its cost; high-cardinality values in logs and trace attributes
- Structured logging
- OpenTelemetry; Prometheus and Grafana; Jaeger; Grafana Loki; LLM-trace UIs (Phoenix)
- Streams as infrastructure: Redis Streams consumer groups, acknowledgement after writes, pending-entry recovery, at-least-once delivery with idempotent consumers, lag as an SLI

### Site reliability engineering

- SLIs, SLOs and SLAs
- Error budgets: (1 − SLO) × window; burn rate; multi-window, multi-burn-rate alerts
- Alerting as classification: precision versus recall; time to exhaustion at a burn rate
- Composed availability of services
- Toil: definition, measurement and budgeting
- Incident management and on-call
- Blameless postmortems; complex-system failure as multiple contributing conditions
- Proving reliability: load tests against the SLO; chaos experiments with an error-budget cost
- Public postmortems as case studies: Knight Capital (2012), GitLab.com database deletion (2017), Amazon S3 us-east-1 (2017), Cloudflare regex CPU exhaustion (2019), Facebook backbone and BGP withdrawal (2021), CrowdStrike content update (2024), Google Cloud Service Control policy replication (2025), Moffatt v. Air Canada chatbot liability (2024)
- Open-source systems as architecture specimens, with their constraints and trade-offs: Kubernetes, Envoy, Kong, NGINX, etcd, Redis, Kafka and Redpanda, Temporal, CockroachDB, PostgreSQL, Prometheus, Loki, Jaeger, OpenTelemetry, MinIO

### Exercises

- From scratch: a container runtime toy using namespaces, a cgroup and an overlay root filesystem
- From scratch: an image-layer builder producing content-addressed tarballs and a manifest
- From scratch: a reconciliation-loop controller over a fake API that converges after injected failures
- From scratch: a pod scheduler placing a generated workload, measured against the node-count lower bound
- From scratch: a DAG build runner with content-hash caching; a plan-and-apply engine that diffs desired against observed state with topological creation and reverse destruction
- From scratch: a Prometheus-format metrics exporter with counters, gauges and mergeable histograms; a multi-window burn-rate alert evaluator
- A multi-stage, reproducible container image with a digest-pinned base
- A Kubernetes deployment with probes, autoscaling, spread constraints and a disruption budget; CPU throttling observed at a limit
- An NGINX reverse proxy and Ingress with TLS, caching and upstream balancing
- A hand-written CI script, then a hosted pipeline with canary deployment and GitOps reconciliation
- Terraform for a multi-tier architecture, checked with `plan`, scanned and policy-checked
- OpenTelemetry instrumentation with sampled traces, histograms and structured logs
- SLOs with burn-rate alerts, a load test and a chaos experiment with its postmortem
- **Reasoning drills**
  - Predict pod placement, throttling and OOM kills from requests and limits before applying them
  - Compute the error budget and burn-rate thresholds for an SLO and justify the alert windows
  - Diagnose an incident from metrics, logs and traces with a written hypothesis per step
  - Predict image size and rebuild time from layer order, then rebuild and compare

## Machine Learning, MLOps & Production ML System Design

**Prerequisites:** sets and propositional logic; coordinate geometry and lines; linear algebra (vectors, matrices, transposes, determinants, cosine similarity, eigen-decomposition, PCA); multivariable calculus and the chain rule; convex optimization and gradient descent; probability (joint, marginal and conditional), Bayes' rule, distributions, maximum likelihood, hypothesis tests and sample size; information theory (entropy, cross-entropy, KL divergence); numerical stability (log-sum-exp, stable softmax); Python with NumPy, pandas and Matplotlib; SQL including window functions and as-of joins; graph search; queues and Little's law; cloud data services (warehouse, object storage, pub/sub).

**Depth bar:** a graduate machine-learning course (losses, gradients and generalization derived) plus production ML system design: every model built from scratch at toy size before the library, every pipeline monitored.

**Capstone:** an end-to-end ML system: the problem framed with its metric, point-in-time-correct features, a model evaluated with ablations, a served endpoint with drift monitoring, and an online experiment measuring its effect.

### Foundations of AI

- **History and definitions**: the Dartmouth workshop (1956); the Turing test; four views of AI (thinking or acting, humanly or rationally); symbolic AI (logic, rules, semantic networks, expert systems); the AI winters and why rule systems failed; learning from data instead of hand-written rules; Mitchell's definition (experience E, task T, performance measure P)
- **Data types**: categorical (nominal), ordinal and continuous features; structured versus unstructured data
- **The supervised workflow**: problem first, then data, split, fit, predict and evaluate

### Classical machine learning

- **Learning paradigms**: supervised, unsupervised and reinforcement learning; regression, classification and clustering, and when to use which
- **Learning theory**
  - Empirical risk minimization
  - The bias–variance decomposition of squared error (bias² + variance + irreducible noise); overfitting and underfitting
  - Regularization as a constraint: ridge (L2, a circular constraint region, closed-form solution, shrunken weights) and lasso (L1, a diamond-shaped region whose corners give sparse weights, fitted by coordinate descent); polynomial features with ridge in one pipeline
  - Maximum likelihood; minimizing cross-entropy as maximum likelihood for a classifier
  - Train, validation and test splits; cross-validation as an estimator with its own variance; the test set touched once
  - Splits that give an honest estimate: transforms fitted on the training split only; stratified splits for skewed classes; time-based splits for temporal data; group-aware splits keeping one user, patient or device on one side; near-duplicates removed across splits
  - Generalization from a test set: Hoeffding's bound P(|test error − true error| > ε) ≤ 2e^(−2mε²) for a fixed classifier; reusing a test set for model selection spends its guarantee
- **Linear models**
  - Least squares: minimizing ‖Xθ − y‖²; normal equations XᵀXθ = Xᵀy; convexity and convergence of gradient descent
  - Logistic regression with cross-entropy loss; generalized linear models
- **Other supervised models**: k-nearest neighbours; naive Bayes; linear and quadratic discriminant analysis; support vector machines and margins; class weights
- **Trees and ensembles**: decision trees and impurity (Gini, entropy); CART; random forests; gradient boosting and boosted stumps; feature importance; monotonic constraints
- **Unsupervised learning and anomaly detection**: k-means; DBSCAN; Gaussian mixtures fitted by expectation–maximization; association rules (support, confidence, lift); robust statistics (z-score, median absolute deviation); isolation forests; reconstruction-error anomaly scores
- **Dimensionality reduction**: the curse of dimensionality; PCA to compress features, with components chosen by explained variance; t-SNE for visualization only
- **Evaluation**
  - The confusion matrix; accuracy and why it misleads on imbalanced data (base rates)
  - Precision, recall, F1, macro-F1 for multiclass problems; choosing precision or recall by the cost of false positives against false negatives
  - ROC curves and AUC as the probability a random positive outranks a random negative; PR curves and PR-AUC
  - Calibration and reliability bins
  - Ranking measures: precision@k, recall@k, MAP, MRR, nDCG@k = DCG@k ÷ IDCG@k
  - Forecast errors: MAE, percentage errors and their instability near zero, interval coverage
  - Business guardrail metrics beside model metrics
- **Feature engineering**
  - Scaling and normalization; encoding categoricals; the hashing trick; target encoding with time-aware folds
  - Missing values; imbalanced datasets (SMOTE, class weighting, focal loss, negative sampling) and the accuracy paradox, where always predicting the majority class scores high and detects nothing
  - Text, time, window, session and graph features
  - Schema validation and golden tests for feature pipelines

### Deep learning

- Biological and artificial neurons; the perceptron and its limit to linearly separable data (XOR); multilayer perceptrons; width versus depth
- Activation functions: step, sigmoid, tanh, ReLU, softmax; the forward pass
- Loss functions: mean squared error for regression, cross-entropy for classification
- Tensors and computational graphs
- Backpropagation as reverse-mode automatic differentiation over the computation graph; its cost as a small multiple of the forward pass; gradient checking by finite differences
- Vanishing and exploding gradients; residual connections; batch and layer normalization
- Optimizers: batch, mini-batch and stochastic gradient descent, momentum, RMSProp, Adam; learning-rate schedules
- **Learning-rate schedules**: large steps early and small steps late; four knobs (warmup length, peak rate, decay shape, floor); linear warmup from near zero; constant, linear decay, cosine decay, step decay and reduce-on-plateau, cosine with restarts, and warmup–stable–decay for runs of unknown length; lengthening warmup and lowering the peak before changing the shape
- **Training instability**: loss spikes, gradient explosion and divergence as one feedback loop (an oversized update raises the loss, which enlarges the next gradient); sharp minima, outlier batches and depth as causes; gradient-norm clipping that rescales to a cap and keeps the direction, with the pre-clip norm logged; float16 overflow near 65,504 turning into Inf and NaN, and bfloat16 as the remedy; alerts on the gradient norm; checkpoints every N steps
- **Batch size**: effective batch = micro-batch × gradient-accumulation steps × devices; filling device memory, then accumulating; small batches (noisy gradients, more updates, often better generalization) versus large ones (stable gradients, higher throughput, fewer updates); the linear scaling rule tying learning rate to effective batch; too few optimizer steps showing as underfitting
- **Reading loss curves**: both losses high and flat early (underfitting); training loss falling while validation loss turns up (overfitting); both flat at the starting value (nothing is updating); persistent jitter (batch too small or rate too high); both falling with a small stable gap (healthy), checkpointed at the validation minimum
- Initialization that preserves activation variance: Glorot (Xavier) initialization Var(w) = 2 ÷ (n_in + n_out); He initialization Var(w) = 2 ÷ n_in for ReLU units
- Regularization in deep networks: weight decay, dropout, data augmentation, early stopping with patience
- Architecture as inductive bias: convolutions sharing one kernel across positions, so parameter count is independent of image size; CNNs for images
- Sequence models before attention: RNNs and LSTMs; encoder–decoder (sequence-to-sequence) models and their fixed-length context bottleneck; weak long-range dependencies; no parallelism across time steps; Bahdanau (additive) attention over encoder states

### Natural language processing foundations

- NLP as the interface between people and software; tasks (classification, named entities, translation, summarization, question answering)
- The classical pipeline: cleaning and Unicode normalization, tokenization, stop-word removal, stemming and lemmatization, feature extraction, a classifier
- Representations: one-hot vectors and bag of words and their limits (sparsity, lost word order, no semantics, out-of-vocabulary words, orthogonal vectors for related words); n-gram features; TF-IDF weighting tf × log(N ÷ df)
- Distributional semantics: meaning from context windows; dense static embeddings (Word2Vec skip-gram and CBOW with negative sampling, GloVe); vector analogies; contextual embeddings (ELMo) and then transformers
- Limits of classical NLP, and the progression from rules to statistical models, deep learning, LLMs and agents

### Machine learning in Python

- scikit-learn: the estimator API (`fit`, `transform`, `predict`); `Pipeline` and `ColumnTransformer`; `StandardScaler`, `MinMaxScaler`, `OneHotEncoder`, `SimpleImputer`, `PolynomialFeatures`; `train_test_split`, `cross_val_score`, `GridSearchCV`, `RandomizedSearchCV`; metrics and classification reports
- PyTorch: tensors and autograd; `nn.Module` with `Linear`, `Embedding`, `Dropout`, `LayerNorm`; loss functions and optimizers; the training loop (forward, loss, backward, step, zero gradients); evaluation mode; devices
- NLTK for tokenizers, stop words, stemmers and lemmatizers

### Specialised learning areas

- **Reinforcement learning**: Markov decision processes, value functions, policy gradients, PPO
- **Graph learning**: PageRank, random walks and random-walk embeddings, bipartite graphs, label propagation, node and edge anomaly scores, graph neural networks
- **Entity resolution**: blocking, candidate generation, pairwise matching
- **Computer vision**: pixels and image representation, 2D convolution and image filters, image embeddings, perceptual hashing, OCR and document extraction, segmentation; vision at research depth
- **Audio and speech**: audio frames, windowing, spectrograms and MFCCs, word error rate per locale; speech at research depth
- **Multimodal retrieval** across text, image and audio embeddings
- **Contrastive (metric) learning** for retrieval; on-device models bounded by memory, power and privacy
- **Operations research**: linear and integer programming, assignment, constrained scheduling; forecasts as inputs to capacity, pricing and dispatch constraints
- **Game theory and auctions**: equilibria; second-price and generalized second-price auctions; incentive compatibility; mechanism design
- **Click models**: deep click-rate models and click-model research

### Applied problem families

- **Problem framing**: prediction, ranking, retrieval, generation and optimization problems; the target action, labels, input entities, metric and failure modes; cold start; feedback loops; delayed labels
- **The case-study method**: problem and business measure → data and labels (implicit, explicit, delayed, weak) → leakage against what is known at decision time → derived metric or estimator → offline evaluation → serving (batch or online) and latency budget → monitoring, rollback and retraining → cost → a named company's design read against the same steps
- **Leakage and point-in-time correctness**: as-of joins; leakage, training–serving skew and online–offline feature drift as three distinct failures; one feature definition for both paths with a parity test
- **Recommendation and feeds**
  - Candidate generation (two-tower retrieval, approximate nearest neighbours, judged by recall@k) separated from ranking and re-ranking
  - Collaborative filtering (item–item), matrix factorization
  - Diversity, coverage and multiple objectives; popularity feedback loops; catalogue coverage
  - Labels from impressions, plays, dwell and hides; leakage from future popularity and same-session targets
- **Search, learning to rank and ads**
  - Inverted indexes, BM25, semantic and hybrid retrieval with rank fusion
  - Learning to rank: pointwise, pairwise and listwise; sampled pairs
  - Position bias: the position-based click model; inverse-propensity scoring (Horvitz–Thompson) unbiased under positivity; propensity clipping trading bias for variance; propensities from randomized slices; off-policy evaluation of a new ranker from old logs
  - Ads ranked by bid × predicted quality; calibrated click and conversion rates
  - Wide & deep models: memorized feature crosses plus generalizing embeddings
- **Explore and exploit**
  - The K-armed bandit; regret R_T = Tμ* − E[Σ rₜ]
  - Greedy lock-in; ε-greedy's linear regret; UCB1 (x̄ᵢ + √(2 ln t ÷ nᵢ)) and Thompson sampling with logarithmic regret; the Lai–Robbins lower bound
  - Contextual and cascade bandits; offline replay evaluation; policy constraints
  - A/B test versus bandit versus feature flag
- **Forecasting, ETA, demand and availability**
  - Trend, seasonality and holiday decomposition; moving averages, exponential smoothing, autoregressive intuition; backtesting
  - Covariates as known at forecast time; censored observations
  - The pinball (quantile) loss L_τ and why its minimizer is the τ-quantile; prediction intervals judged by coverage and width together
  - Availability probabilities, calibration and the cost of a false "in stock"
- **Fraud, abuse, risk and trust and safety**
  - Cost-weighted thresholds: flag when p > C_FP ÷ (C_FP + C_FN); expected cost C_FP·FP + C_FN·FN as the measure
  - Review-queue capacity setting the threshold; recall at a fixed false-positive rate
  - Weak, delayed (chargeback) and semi-supervised labels
  - Fraud rings as connected components of shared-device and shared-card graphs
  - Synchronous scoring beside an asynchronous review queue; fail-open versus fail-closed decisions
  - Adversarial drift
- **Language and support**
  - Ticket routing and classification; macro-F1 and misroute cost; handle time and deflection
  - Sequence labelling scored by entity-level F1
  - Grammatical error correction as structured prediction
  - Suggested replies sent by a human; masking personal data before a model sees text
- **Vision, documents and speech in production**: buying a perception API versus building a model; batch versus GPU-endpoint serving; near-duplicate leakage across splits; mean average precision; image search with batch embedding and an online nearest-neighbour index
- **Marketing, churn, lifetime value and notifications**
  - Potential outcomes; randomization versus confounding; average and segment (uplift) effects; targeting the persuadable
  - Holdouts and incremental lift instead of raw click rate
  - Survival analysis and churn hazard; censoring
  - Customer lifetime value: CLV = m r ÷ (1 + d − r) for constant retention r, margin m and discount rate d
  - Lookalike audiences; send time under frequency caps; notification fatigue
- **Causal inference**: causal graphs, instrumental variables, difference in differences, synthetic control; propensity weighting; observational bias
- **Marketplace pricing** as an applied family

### MLOps

- The ML lifecycle: data → features → training → evaluation → deployment → monitoring → retraining
- **Technical debt in ML systems**: entanglement; hidden feedback loops; undeclared consumers; data dependencies; glue code and pipeline jungles; the model as a small part of the system
- **Data and feature platforms**: event contracts; batch versus streaming features; freshness and backfills; point-in-time correctness; schema evolution; feature stores with online and offline parity; fresh features streamed from user-action and inventory events; per-entity features cached with a TTL
- **Training pipelines**: dataset snapshots and versions; reproducible training (pinned data, code, environment, seeds); experiment tracking; hyperparameter search; model registries with lineage, aliases and approval status; model cards
- **Production readiness**: the ML Test Score rubric across data, model, infrastructure and monitoring
- **CI/CD/CT**: continuous training; continuous evaluation triggered from CI
- **Serving architectures**: online, batch, near-real-time, embedded, sidecar and asynchronous inference; caches, fallbacks and timeout budgets; batch scores delivered by schedulers and task queues
- **Experimentation and rollout**: A/B tests as two-sample hypothesis tests; holdouts; assignment bucketing and exposure logs; bootstrap intervals; segment analysis; metric guardrails; shadow, canary and ramp deployments of models as a dial separate from the application canary; rollback gates
- **Monitoring and drift**
  - Covariate shift (P(x) changes), prior or label shift (P(y) changes) and concept drift (P(y | x) changes)
  - Two-sample detection: the Kolmogorov–Smirnov statistic D = supₓ |F₁(x) − F₂(x)|; the population stability index PSI = Σ (aᵢ − eᵢ) ln(aᵢ ÷ eᵢ) and its conventional 0.1 and 0.25 thresholds
  - Training–serving skew as a pipeline defect that retraining does not fix
  - Calibration drift; data-quality and freshness checks; a written retraining policy; incident runbooks
- **Governance and responsible ML**: privacy and PII minimization; consent, retention and deletion; bias and fairness; explanations; human-in-the-loop review and human override; audit logs; non-destructive, undoable AI actions; abuse resistance and red-team tests; data-loss prevention on logs
- **Scale and cost**: hot keys and fan-out; approximate retrieval; request batching; concurrency limits; accelerators as remote services; cost per prediction and per successful decision; cost at ten times the traffic
- **ML platforms**: shared features, training, registry, serving and monitoring across teams; platform-enforced point-in-time joins; measured by time to train, failed deploys, skew incidents and cost per training hour

### Exercises

- From scratch in Go: a metrics library and evaluator CLI; linear and logistic regression with gradient checks; a CART tree and boosted stumps; k-means, a robust anomaly detector and a Gaussian-mixture EM trainer; BM25, item–item collaborative filtering, matrix factorization, exact k-NN with heap top-k, a pairwise ranker and a diversity re-ranker; a tokenizer, TF-IDF and edit distance; image convolution filters, a perceptual hash and spectral audio features; entity-resolution blocking, PageRank and random-walk embeddings; forecast baselines with backtests and an assignment scheduler; a bandit simulator with offline replay and propensity weighting; a tiny tensor type, an MLP forward and backward pass, optimizer variants (SGD, momentum, RMSProp, Adam), dropout and batch normalization
- From scratch: a perceptron failing on XOR and a two-layer network solving it; PCA by power iteration; a Word2Vec skip-gram trainer with negative sampling and analogy tests
- A breast-cancer classifier in scikit-learn: a scaled logistic-regression pipeline, cross-validated tuning and a confusion-matrix report, then a polynomial-ridge regression showing L1 against L2
- A text classifier comparing an NLTK and TF-IDF pipeline with sentence embeddings
- A ranker for a shop's home page and search: sampled negatives, cold-start flags, time-aware target encoding, recall@k and nDCG@k, an exploration policy, a CPU ranker served online with skew and latency monitoring
- A delivery-ETA window: quote-time features only, a quantile model fitted by gradient descent from scratch, coverage against width, residual bias by city and hour
- Fraud scoring on payment tokens: delayed chargeback labels, a cost- and capacity-set threshold, a synchronous score with a timeout and a review queue, chargebacks returned as labels
- A published ML system design redone end to end: metric derived, leakage risks listed, cost at ten times the traffic
- A feature-store facade over PostgreSQL and Redis with online and offline parity tests
- A local trainer and evaluator CLI writing artifacts, metrics, lineage and approval status
- A model served over REST and gRPC with cache, fallback, shadow mode and latency SLOs
- An experiment service: assignment bucketing, exposure logs, a CUPED and bootstrap report, a rollback gate
- A drift detector with OpenTelemetry metrics, data-quality alerts and a runbook drill
- Governance tooling: policy checks, red-team tests, reversible actions, an audit log and a review-dashboard API
- A batching, rate-limiting and caching layer comparing exact and approximate retrieval, with cost per successful decision
- **Reasoning drills**
  - Predict the bias–variance effect of a model change before training it
  - Derive a loss gradient by hand and check it numerically
  - Find the leakage in a feature set before training
  - Reproduce one result of a classic machine-learning paper at toy size and critique its evaluation

## Generative AI, LLMs, Agents & Claude Applications

**Prerequisites:** probability (joint, marginal and conditional) and the chain rule of probability; cross-entropy, maximum likelihood and perplexity; linear algebra (matrix multiplication, transposes, projections) and cosine similarity; backpropagation, gradient descent and neural-network training; classical NLP, word embeddings and recurrent sequence models; ranking measures (recall@k, MRR, nDCG); binomial proportions, confidence intervals and paired tests; Python with NumPy and PyTorch, Go and TypeScript; HTTP, JSON Schema, JSON-RPC 2.0 and Server-Sent Events; OAuth 2.0 with PKCE; containers; queues, idempotency, retries with backoff, sagas and rate limiting; prompt-injection, jailbreak and AI-application threats; observability and SLOs.

**Depth bar:** a graduate course on large language models (the transformer derived, training and inference costs computed) plus production LLM engineering: every application measured by an evaluation suite before and after each change.

**Capstone:** an agentic retrieval application over your own documents with tools, guardrails, an evaluation suite gating regressions, cost and latency budgets and a red-team pass, deployed on Google Cloud.

### How LLMs work

- **Language modelling as probability**
  - Autoregressive factorization P(x₁ … x_T) = Πₜ P(xₜ | x₁ … xₜ₋₁); next-token cross-entropy as the training loss
  - Perplexity; bits per byte for comparing models with different tokenizers
- **Tokenization**
  - Characters versus subwords versus bytes; subwords removing out-of-vocabulary words
  - Byte-pair encoding as a greedy dictionary compressor: training (count pairs, merge the most frequent, record merges) and encoding in learned merge order; special tokens; the round-trip property
  - WordPiece (likelihood-scored merges, continuation markers, used by BERT); SentencePiece (language-independent tokenization of raw text with whitespace as a symbol, by BPE or a unigram language model)
  - Why token counts vary by language, code and numbers; tokens as the unit of price, limits and latency
- **N-gram and bigram models**: counting, smoothing, sampling; the same model as a trained linear layer
- **The Transformer**
  - Attention as a soft lookup table: queries, keys and values as learned projections of each token; a worked Q, K, V example
  - Scaled dot-product attention softmax(QKᵀ ÷ √d_k)V and why √d_k keeps logits at unit variance
  - Self-attention versus cross-attention (queries from the decoder, keys and values from the encoder output, a target × source weight matrix)
  - Multi-head attention: h heads of width d_k = d_model ÷ h, concatenated and projected by Wᴼ
  - Token embeddings; positional information by sinusoidal encodings (deterministic, unique per position, offsets as linear maps, extending beyond trained lengths) or by learned position tables
  - The causal mask: a lower-triangular mask setting future positions to −∞ before the softmax
  - The residual stream with add-and-norm; layer normalization; the position-wise feed-forward block with inner width about 4 × d_model
  - The autoregressive loop: begin- and end-of-sequence tokens, each output fed back as input
  - Encoder-only (BERT), decoder-only (GPT) and encoder–decoder (T5, BART) architectures; the same blocks over image patches and audio (Vision Transformer, Whisper); pre-training as learning the projections
  - The context window as the fixed length of the position table; O(n²d) attention cost per layer
  - The key–value cache during generation
- **Model lineage and benchmarks**
  - BERT: masked language modelling over 15% of tokens and next-sentence prediction; fine-tuning for downstream tasks; the GLUE tasks (CoLA, SST-2, MRPC, STS-B, QQP, MNLI, QNLI, RTE, WNLI)
  - GPT-1 pre-training then fine-tuning; GPT-2 zero-shot task transfer measured on LAMBADA; T5 text-to-text training by span corruption on C4; BART as a denoising autoencoder
  - GPT-3 and in-context learning (zero-, one- and few-shot); abilities that emerge with scale
  - Open-weight families (LLaMA, Mistral, Mixtral, Falcon, Qwen, DeepSeek); mixture-of-experts layers routing each token to a few experts; MMLU across 57 subjects
  - Reasoning models trained to think before answering, and inference-time compute as a scaling axis
- **Decoding**
  - Greedy decoding as locally rather than globally optimal; beam search keeping the best partial sequences
  - Temperature softmax(z ÷ T): entropy rising with T, T → 0 as greedy; top-k; nucleus (top-p) sampling as a dynamic cutoff; avoiding extreme top-k and top-p together
  - Repetition, frequency and presence penalties; stop sequences and maximum length; seeded reproducibility
  - Why sampling makes answers vary and lets a model state falsehoods fluently
- **Scaling**: training compute ≈ 6ND FLOPs; power-law loss in parameters, data and compute; compute-optimal training (Chinchilla: 70B parameters on 1.4T tokens, about 20 tokens per parameter)
- **Alignment**: instruction tuning by supervised fine-tuning, a reward model from pairwise human preferences and PPO with a KL penalty for drifting from the tuned model (RLHF, the InstructGPT recipe); Constitutional AI and AI feedback against written principles
- **Frontier model behaviour**: thinking before answering (adaptive thinking controlled by an effort setting); multimodal inputs (images and PDFs); latency ≈ time to first token + output tokens ÷ throughput; larger models are slower per token; streaming changes perceived, not total, latency
- **Long context**: the hard limit of the window versus degraded retrieval inside it ("lost in the middle"); quality falling as irrelevant context grows
- **Choosing an approach**: prompt engineering versus retrieval-augmented generation versus fine-tuning
- **Responsible AI**: bias, fairness, safety evaluation; explainability through attention visualization and feature attributions (LIME, SHAP)

### Fine-tuning and adaptation

- Full fine-tuning versus parameter-efficient fine-tuning; memory for weights, gradients and optimizer states; one full copy of the model per task
- Cheaper full fine-tuning: layer-wise, block-wise and progressive unfreezing; tuning only the top blocks with embeddings and lower blocks frozen
- Fine-tuning hyperparameters: a peak learning rate near 1e-5 to 2e-5 for full fine-tuning and 1e-4 to 2e-4 for LoRA; one or two epochs; a few percent of warmup with cosine decay; early stopping on held-out task and general evaluations, not on training loss
- **Catastrophic forgetting**
  - Why it happens: knowledge superimposed in shared weights, a narrow gradient signal, drift away from the pretrained optimum, and no replay of old data
  - Measuring it: a fixed general suite (reasoning, code, mathematics, instruction following) run before and after every fine-tune, since task metrics rise while general ability falls silently
  - Rehearsal: mixing 1–10% general instruction data into every batch
  - Regularizing toward the pretrained weights: L2-SP with penalty λ‖θ − θ₀‖²; elastic weight consolidation weighting each parameter's penalty by its Fisher information
  - Weight interpolation after training, θ = (1 − α)·θ_base + α·θ_tuned, with α chosen at the knee of the task-versus-general curve (WiSE-FT)
  - Choosing mitigations by cause: conservative hyperparameters always; rehearsal when general data exists; penalties when it does not; interpolation for a model already degraded; freezing for small data or tight compute
- **Fine-tuning data**
  - Quality: extraction boilerplate, spam and machine-generated text, OCR errors; wrong content learned as fact; duplicates driving memorization; benchmark test sets leaking into training data; inconsistent formatting, encodings and whitespace; stale and contradictory snapshots
  - Too little data: augmentation by back-translation and paraphrase; synthetic data that is validated before use; a smaller model with stronger regularization
  - Missing edge cases and narrow coverage: targeted collection, simulation, active learning on uncertain production samples, stratified sourcing, metrics reported per subgroup, datasheets and model cards
  - Shift between training and deployment: usage shift (documents to dialogue), temporal shift (the world after the cutoff) and domain shift (general to specialist), met by instruction tuning, domain-adaptive pre-training with replay, retrieval and production monitoring
- **LoRA**: frozen weights plus a trainable low-rank update ΔW = BA of rank r much smaller than the layer width, scaled by α ÷ r; B initialized to zero so training starts from the base model; choosing target modules (attention and MLP projections); merging adapters into the weights or swapping adapters per task
- **QLoRA**: a frozen base quantized to 4-bit NormalFloat (NF4); double quantization of the quantization constants; paged optimizers absorbing memory spikes; adapters trained in higher precision
- **The PEFT families**: additive (adapters), reparameterized (LoRA, QLoRA), soft prompts, and selective tuning of existing weights (BitFit training only biases; diff pruning learning a sparse difference)
- **Adapters**
  - A bottleneck block with a residual connection, h′ = h + f(h): down-projection from width d to m, a non-linearity, up-projection back to d; 2dm + m + d added parameters per adapter
  - Near-identity initialization so the adapted model starts as the base model; the base frozen and only adapters trained
  - Sequential adapters after each sub-layer versus parallel (residual) adapters beside the feed-forward block; added inference latency that a merged LoRA update avoids
  - One adapter per task as a defence against forgetting; routing among adapters by task; AdapterFusion combining several task adapters with learned attention
- **Soft prompts**
  - Trainable virtual-token embeddings in place of hand-written discrete prompts; prompt tuning at the input layer versus prefix tuning, which prepends trainable key and value vectors at every attention layer
  - Cost: longer sequences in every layer; refinements that choose shorter prompts through a router (SMoP), vary prefix length by layer with gates (adaptive prefix tuning), generate the prompt from each input (instance-dependent prompts), or insert prompts only at selected layers
- Training data as instruction–response pairs in the model's chat template; held-out evaluation of the tuned model against the base model for gains and regressions
- Weight quantization (8-bit, 4-bit) for inference and its accuracy cost
- Knowledge distillation: a small student trained on a large teacher's outputs or soft labels
- Libraries: Hugging Face Transformers, PEFT, bitsandbytes and TRL

### Multimodal models

- **Foundations**
  - Three paradigms by input and output: contrastive (image and text to a similarity score), generative (image and instruction to free text) and promptable dense prediction (image and spatial prompt to a mask)
  - The shared anatomy: a vision encoder, a connector, and a consumer of the fused representation; where fusion happens (a final dot product between two towers, self-attention over mixed tokens, or a dedicated cross-attention module)
  - Vision Transformer: an image cut into 16 × 16 patches, each flattened and linearly projected like a word embedding, with position embeddings and a [CLS] token whose output summarizes the image
- **CLIP**
  - Two independent encoders (a ResNet with attention pooling or a ViT; a text Transformer read at its end-of-sequence token), each linearly projected and L2-normalized into one space
  - The symmetric InfoNCE loss: an N × N similarity matrix with matching pairs on the diagonal, cross-entropy over rows and over columns, and a learned temperature controlling the softmax's sharpness
  - Very large batches as the source of in-batch negatives; training on hundreds of millions of noisy web image–text pairs
  - Zero-shot classification by embedding one sentence per class name; template ensembling; linear probing versus zero-shot transfer as two ways to judge an encoder
  - Limits: counting, spatial relations, fine text, prompt sensitivity, web-data bias, and no text generation
- **LLaVA-style generative models**
  - A frozen CLIP vision tower whose patch features pass through a projector (one linear layer, later a two-layer MLP) into the language model's embedding space; visual tokens placed in the sequence as a foreign language, fused by ordinary self-attention
  - Why a projector is needed: two embedding spaces of equal width with unrelated geometry
  - Instruction data produced by a text-only model from captions and bounding boxes: conversation, detailed description and complex reasoning
  - Two-stage training: projector-only feature alignment with both towers frozen, then instruction tuning of projector and language model, with the loss on assistant tokens only
  - Higher resolution by tiling an image, encoding each tile and adding a downsampled global view, at the cost of more visual tokens
  - Limits: object hallucination, a resolution bottleneck, weak localization and counting, inherited encoder blind spots
- **Grounded models (Qwen-VL)**
  - A cross-attention adapter in which a fixed set of learnable queries attends over all patch features, giving a constant visual-token budget at any resolution; 2D position encodings preserving layout
  - Grounding as generated text: reference phrases and bounding boxes wrapped in special tokens, with coordinates normalized to a fixed range; several images in one sequence
  - Three-stage training: low-resolution pre-training on weak pairs with the language model frozen, higher-resolution multi-task pre-training (captioning, question answering, grounding, OCR), then instruction tuning
  - Successors: dynamic resolution with a variable token count, and rotary position embeddings unified across text, space and time
- **Promptable segmentation (SAM)**
  - The task: any point, box or rough mask returns a valid mask
  - A heavy masked-autoencoder-pretrained ViT run once per image and cached; a light prompt encoder (positional encodings for points and boxes, convolutions for masks); a small mask decoder with two-way attention between prompt and image tokens
  - Ambiguity resolved by three candidate masks (whole, part, sub-part) ranked by a predicted-IoU head
  - Mask loss as focal loss (pixel imbalance) plus Dice loss, 1 − 2|X∩Y| ÷ (|X| + |Y|) (region overlap)
  - The data engine: assisted-manual, semi-automatic, then fully automatic labelling from a grid of point prompts, yielding over a billion masks
  - No class labels or language; composition with a detector that names and boxes objects; extension to video with a memory of earlier frames
- **Design trade-offs**: frozen versus fine-tuned vision backbones; visual-token count versus spatial fidelity; web-scale noisy data versus small engineered datasets; one task done very well versus breadth; self-supervised (DINO-family) and sigmoid-loss contrastive (SigLIP) encoders as alternatives to CLIP
- **Applications**
  - Captioning: a contrastive model for tags, a generative one for sentences; fixed, scoped, length-limited templates at catalogue scale; n-gram metrics (BLEU, ROUGE, METEOR, CIDEr), scene-graph SPICE and CLIPScore, and their weak agreement with human judgment; cleaning noisy web captions with a jointly trained captioner and filter
  - Visual question answering: yes/no, multiple-choice, counting and open-ended forms; listing objects before counting; presupposition hallucination and an explicit "not present" answer; testing whether answers depend on the image by blurring it; strict-match accuracy penalizing correct verbose answers
  - Document intelligence: OCR precision, layout understanding and relations between fields together; the exact JSON schema shown in the prompt, with every field named and nulls for missing values; resolution as the largest lever; dedicated OCR pipelines for bulk text versus a vision-language model for layout-aware extraction; document-specific vision encoders and OCR-plus-layout encoders compressed into learned queries; human verification of financial and legal fields
  - Visual reasoning and chart questions: reasoning strength set mostly by the language model; observations listed before conclusions; values extracted before reasoning; compounding errors and a self-check pass
  - Preference tuning against hallucination with synthetic negatives: random answers, mismatched questions, and images with the relevant objects masked
  - Benchmarks by task: COCO Captions and NoCaps; VQAv2, GQA, OK-VQA, TextVQA and VizWiz; DocVQA (scored by normalized edit similarity), FUNSD and ChartQA; POPE for object hallucination; MMMU, MathVista, ScienceQA, NLVR2 and Winoground; contamination as a caveat on reported gains

### Embeddings and retrieval

- Embeddings as vectors whose geometry encodes similarity; embedding models from a provider
- Cosine, dot product and Euclidean distance agree on unit vectors (‖a − b‖² = 2 − 2 cos θ); normalizing once; an index metric that must match the metric the model was trained for
- Lexical retrieval: the vector-space model; BM25 with term-frequency saturation k₁ and length normalization b; IDF
- Hybrid retrieval: reciprocal rank fusion RRF(d) = Σ 1 ÷ (k + rank_r(d)) with k = 60
- Why embedding search misses exact codes that BM25 finds; negation and numbers that embed deceptively alike; topical relevance that does not answer the question
- Retrieval benchmarks: MS MARCO for passage ranking, BEIR for zero-shot transfer across domains
- **Training embedding models**
  - Why raw BERT [CLS] or mean-pooled vectors are poor for cosine similarity; Sentence-BERT siamese training
  - Contrastive and margin losses; in-batch negatives; hard negatives mined with BM25
  - Bi-encoders (texts encoded independently, so documents can be indexed) versus cross-encoders (query and document encoded jointly, accurate but not indexable); ColBERT late interaction scoring per-token maximum similarity
  - Small encoders distilled from large ones (MiniLM)
  - Matryoshka representation learning: a loss on nested prefixes so vectors can be truncated to fewer dimensions
- **Choosing an embedding model**: measuring on your own queries rather than trusting a public leaderboard (MTEB); hosted APIs versus open-weight models (BGE, E5, Nomic, MiniLM); dimensions and storage cost; multilingual coverage; code and logs that need hybrid search; maximum sequence length against document length; truncatable embeddings for very large corpora; asymmetric query and passage prefixes; corpora small enough to need no retrieval
- **Vector-database internals**
  - Exact search at O(n·d) per query; the curse of dimensionality for tree indexes
  - IVF: k-means centroids partition the space into Voronoi cells with inverted lists; `nlist` near √N as a starting point; `nprobe` cells searched, costing about `nprobe` × N ÷ `nlist` comparisons; training on many points per centroid
  - Product quantization: a vector split into m sub-vectors, each replaced by a one-byte code from a 256-centroid codebook (768 float32 dimensions to 8 bytes); asymmetric distance computation from per-query lookup tables; IVF-PQ coding residuals from the cell centroid
  - HNSW layered proximity graphs: greedy descent from sparse upper layers; `M`, `efConstruction`, `efSearch`; roughly logarithmic search with memory growing with N·M
  - Scalar and binary quantization; ScaNN and DiskANN for collections larger than memory
  - The recall–latency–memory trade-off tuned against a flat baseline
  - Filtered search: pre-filter, post-filter, filter during traversal; selective filters collapsing recall
  - Inserts and deletes on a built index; rebuilds and compaction; sharding and replication; hybrid dense-plus-sparse search; multi-tenancy by namespace or partition
  - Embedding versioning: a new embedding model means re-embedding and re-indexing
  - FAISS index types (flat L2 and inner product, IVF-Flat, IVF-PQ, HNSW) as a library without a document store, so the application keeps the ID-to-text map; Chroma storing documents, metadata and embeddings together with metadata `where` filters over an HNSW index
  - Store selection: pgvector in PostgreSQL versus dedicated vector stores (Qdrant, Weaviate, Chroma, Vespa, Pinecone) versus libraries (FAISS) versus managed indexes

### Retrieval-augmented generation

- Why retrieval: hallucination, unverifiable answers, the knowledge cutoff and private data; indexing, retrieval and generation conditioned on retrieved passages
- Naive, advanced (pre-retrieval query rewriting; post-retrieval reranking, filtering and compression) and modular pipelines
- **Document parsing**
  - PDF versus DOCX versus HTML; probing for a text layer before OCR (Tesseract over rendered pages) for scans
  - Tables extracted as HTML or Markdown (pdfplumber, Camelot); layout-aware parsers (Unstructured, Docling, GROBID, document-AI services, vision-language models)
  - HTML boilerplate removal (BeautifulSoup versus readability-style extractors); metadata captured with each chunk
- **Chunking**
  - Fixed-size token windows with 10–20% overlap; sentence and paragraph boundaries
  - Structure-aware splitting by headings, clauses or code syntax trees; recursive splitters
  - Semantic chunking at topic shifts with a maximum size
  - Hierarchical parent–child chunks: retrieve small, return the larger parent
  - Starting near a few hundred tokens and tuning by evaluation
- Contextual retrieval: prepending a generated description of each chunk's place before embedding and indexing
- **Query transformation**: rewriting; follow-up questions made standalone from the conversation; multi-query expansion; HyDE (embedding a hypothetical answer); step-back questions; request shaping before retrieval
- **Query routing**: rules and regular expressions; embedding similarity to route profiles; trained classifiers; LLM routers returning JSON; hybrid waterfalls from cheap to expensive; routing among data sources, models and workflows, prompts and indexes
- Two-stage retrieval: hybrid search for a shortlist, then cross-encoder reranking
- **Citations and provenance**
  - Inline citation by prompting; structured tool output forcing exact quotes; post-hoc attribution by entailment (NLI); provenance carried in agent state
  - Their trade-offs in accuracy, latency and cost; verifying every cited quote against retrieved text; citations linking back to source systems
- **Failure modes**
  - Retrieval: vocabulary mismatch, incomplete recall, multi-hop questions, stale indexes, single-vector dilution of multi-part questions
  - Context: lost in the middle, overload, irrelevant passages
  - Generation: hallucination despite retrieval, conflicts between retrieved and parametric knowledge, wrong attribution
  - Silent pipeline failures: empty chunks from scanned PDFs, missing query and passage prefixes, an L2 index over a cosine-trained model, a lost ID-to-text map
- **Variants**: stateless retrieval; conversational retrieval with history-aware rewriting; agentic retrieval in observe–think–act loops; Chain-of-RAG (retrieval chains learned by rejection sampling and decoded greedily, best-of-N or by tree search)
- Permissions enforced at retrieval time as role-based metadata filters inside the vector store
- **Multimodal RAG**
  - Retrieved content as images, tables, charts or whole pages, because the answer often sits in a figure that text extraction discards
  - Image search: text-to-image and image-to-image over a shared embedding space, on the same approximate-nearest-neighbour indexes as text; weak on compositional and fine-grained queries
  - Parse-then-embed (OCR and layout analysis, then text embeddings) versus retrieval in vision space (a page image embedded directly by a vision-language model)
  - ColPali: one low-dimensional vector per image patch and per query token; the late-interaction score Σ over query tokens of the maximum similarity to any patch; in-batch contrastive training on query–page pairs; page-level indexing; larger indexes than single-vector retrieval
  - Storage choices: one unified embedding space, original modalities kept with cross-modal search, or separate indexes searched separately
  - Fusion of retrieved evidence: similarity-score fusion in a shared space, cross-attention against the query, or conversion to one representation such as captions
  - Generation by a vision-language model over retrieved pages; answers restricted to retrieved content with a page or region citation and a permitted "not found"; a citation that does not prove the answer came from the page
  - Page-retrieval evaluation with ViDoRe and nDCG@5; multi-page reasoning and faithfulness evaluation as open problems
  - Choosing the level: text search for plain text, image search for photo and product corpora, vision-space retrieval for documents mixing text, tables and charts
- **Training retriever and generator together**: the right documents as a latent variable, marginalized over the top-k retrieved (the original RAG and REALM formulations) in an alternation resembling expectation–maximization; contrastive alignment loss with hard negatives; robustness training that injects irrelevant passages so the generator learns to ignore them; in practice, separate pre-training followed by joint fine-tuning
- Evaluation: context precision and context recall for retrieval; faithfulness (claims supported by the context) and answer relevancy; RAGAS and TruLens
- Ingestion by an idempotent, event-triggered embedding worker; scheduled re-embedding

### Model APIs

- **The Messages API by hand**
  - `POST /v1/messages`; headers `x-api-key`, `anthropic-version`, `content-type`
  - Body: `model`, `max_tokens`, alternating `user` and `assistant` turns, top-level `system`, content blocks (`text`, `image`, `document`, `tool_use`, `tool_result`, thinking blocks)
  - Response: `content` blocks, `stop_reason` (`end_turn`, `max_tokens`, `stop_sequence`, `tool_use`, `pause_turn`, `refusal`), `usage` including cache counters
  - Streaming events: `message_start`, `content_block_start`, `content_block_delta` (`text_delta`, `input_json_delta`), `content_block_stop`, `message_delta`, `message_stop`, `ping`, and mid-stream `error` events
  - Error types: 400 `invalid_request_error`, 401 `authentication_error`, 402 `billing_error`, 403 `permission_error`, 404 `not_found_error`, 409 `conflict_error`, 413 `request_too_large`, 429 `rate_limit_error`, 500 `api_error`, 504 `timeout_error`, 529 `overloaded_error`; request IDs
  - Retrying 429, 529 and 5xx with exponential backoff and full jitter honouring `retry-after`; never retrying 400, 401, 403 or 413
  - Rate limits per organization tier and per model, reported in response headers; spend limits
  - A cost calculator from `usage` and a configurable price table
- **The SDKs**: Python, TypeScript and Go SDKs; typed requests, responses and errors; stream helpers that assemble the final message; built-in retries (two by default) and timeouts
- **Request anatomy on current models**
  - No prefilled assistant turns; structure comes from structured outputs instead
  - Adaptive thinking with an effort setting; thinking blocks passed back unchanged in multi-turn tool use
  - `max_tokens` as a hard output cap set from the task
  - Which sampling parameters a model accepts
- **Documents, images and citations**: image and PDF blocks and their token cost; the Files API (`file_id` reuse); citation blocks pointing into documents; what vision is bad at (small text, counting, geometry)
- **Cost, caching, batches and model choice**
  - Token counting before sending
  - Prompt caching: `cache_control` breakpoints (up to four), prefix order tools → system → messages, automatic caching, model-dependent minimum lengths, a five-minute default lifetime refreshed on hits and a one-hour option, writes priced above and reads far below base input, invalidation by any earlier change, `cache_read_input_tokens` and `cache_creation_input_tokens`
  - Message Batches: half price, results within 24 hours, matched by `custom_id` because order is not guaranteed
  - Model choice on quality, latency and price; routing easy requests to small models and escalating; pinned model IDs versus moving aliases; deprecations and migrations; listing models through the Models API
  - Claude through Gemini Enterprise Agent Platform and Amazon Bedrock: different endpoints, credentials and model-ID forms; features that can lag the first-party API
- **OpenAI-compatible chat APIs**: Chat Completions roles (system, developer, user, assistant, tool); JSON mode versus strict schema-constrained outputs; `tools` with `tool_choice` (auto, none, required or a named function) and the two-call tool flow; sampling parameters per request
- **Local models**: Ollama with Modelfiles built from GGUF files and context-length settings

### Prompt, context and output engineering

- **Prompt engineering**: prompt elements (instruction, context, input data, output indicator); clear, direct instructions with the context a new colleague would need; role prompting and rules in the system prompt; zero-shot versus few-shot (multishot) examples, varied and tagged; XML tags separating instructions, data and examples; reasoning before answering; prompt chaining; long documents before the question; saying what to do rather than what not to do
- **Reasoning techniques**
  - Chain of thought: few-shot reasoning exemplars and zero-shot "think step by step"; Auto-CoT (clustering questions, then sampling generated demonstrations)
  - Self-consistency: a majority vote over sampled reasoning paths
  - Tree of Thoughts: breadth- or depth-first search over self-evaluated intermediate thoughts
  - ReAct: interleaved thoughts, actions and observations grounded by tools
  - Meta prompting: structure- and syntax-focused templates rather than content examples
  - Directional stimulus prompting: a small policy model, fine-tuned then trained by reinforcement learning, generating hints for the large model
- **Prompt optimization**
  - Objectives: accuracy, robustness, faithfulness, format adherence, tool use, safety, latency and cost
  - Prompts as versioned artifacts: semantic versions, changelogs, examples, evals, metrics and rationale tracked together; an eval on every change
  - Branching experiments, regression tests, A/B tests, deployment and monitoring
  - Manual refinement versus automatic optimization loops (generate candidates, evaluate, select): APE; ProTeGi textual gradients with beam selection; evolutionary search; reinforcement learning; DSPy programs whose prompts are compiled against a metric
- **Mode collapse and verbalized sampling**: preference tuning sharpening outputs toward the most typical answer; asking for several responses with stated probabilities to recover diversity
- **Prompt compression**: extractive selection, summarization and token-level pruning; LLMLingua (a budget controller, iterative token-level compression scored by a small model, distribution alignment); LLMLingua-2 (token classification trained on distilled compression data)
- **Context engineering**: the context window as a budget; just-in-time retrieval through tools versus loading everything; compaction of old turns; memory written and read across sessions; subagents returning summaries; stable prompt order to keep caches hitting; conversation state in an application-owned store with retention rules
- **Output handling**: structured outputs constrained by JSON Schema; constrained decoding that masks tokens a grammar forbids; strict tool definitions; validating anyway; detecting truncation and refusal from `stop_reason` before parsing; one repair-and-retry then visible failure; prompt versions recorded in every log line

### Tools and the Model Context Protocol

- **The tool loop**: tools declared by `name`, `description` and `input_schema`; `tool_use` blocks and `stop_reason: "tool_use"`; one user turn of `tool_result` blocks matched by `tool_use_id`, all parallel results together, `is_error` on failure; `tool_choice` modes and the models that reject forced tool use; disabling parallel calls; server tools (web search, web fetch, code execution) and `pause_turn`; the SDK tool runner with approval and logging hooks
- **Tool design**: descriptions as prompts; fewer, task-shaped tools rather than one per endpoint, since selection errors grow with the number of tools; namespacing; token-frugal results with paging and summary modes; actionable error messages returned verbatim so the model can correct itself; idempotent tools; evaluating tools by success rate and tokens per task; least-privilege service accounts behind tools
- **MCP fundamentals**: hosts, clients and servers; server primitives (tools, resources addressed by URI, prompts) and client primitives (sampling, roots, elicitation); JSON-RPC lifecycle (`initialize`, `notifications/initialized`, `tools/list`, `tools/call`, `resources/read`, change notifications); capability negotiation, cancellation, progress, pagination; the stdio transport (stdout for messages, stderr for logs); a date-versioned specification; official SDKs; an MCP server in Go by hand
- **MCP in production**: Streamable HTTP with JSON or SSE responses and session headers; remote servers as OAuth 2.0 protected resources advertising their authorization server (RFC 9728); authorization code with PKCE; audience-checked tokens; the MCP Inspector; servers as code that runs with your permissions; remote servers behind an identity-aware proxy with secrets in a secret manager
- **Customizing Claude beyond MCP**: Agent Skills, subagents, slash commands and plugins, and when each is the right artifact

### Agents and workflows

- An agent as a model using tools in a loop until a stop condition; loop, tools, context, memory, planning, subagents and a budget of turns, tokens, time and money
- Workflows (code-fixed paths) versus agents (model-chosen paths); the simplest thing that works first
- The capability ladder, each rung keeping those beneath it: a model, plus retrieval, plus conversation state, plus tools, plus model-chosen control flow, plus delegation; question answering (one retrieval, one generation, text out) versus task completion (a goal with constraints, steps ordered at run time, a change in the world)
- Choosing between them: a workflow when the steps are the same for every input, the path must be auditable, cost and latency must be bounded exactly, or a wrong call is irreversible; an agent when the number of steps depends on the data, a later step can invalidate an earlier one, or recovery must be dynamic; the test of whether the flowchart can be drawn before the request arrives; a workflow with an agent embedded at the one uncertain step
- What the loop costs: a stateless model re-reads the goal, tool schemas and every earlier step on each turn, so cost grows faster than the step count; observations truncated, superseded steps summarized, only the last few kept in full
- Workflow patterns: prompt chaining with gates, routing, parallelization (sectioning and voting), orchestrator–workers, evaluator–optimizer
- **Planning and reasoning loops**
  - Plan, act, observe and track; the ReAct trace (task, thoughts, actions, observations) as the growing context
  - Closed-book reasoning drifting into hallucination as chains lengthen
  - Planner–executor separation: a planner emitting a task graph, cheaper executor models, re-planning on failure, for accuracy, cost and fault tolerance
  - Hierarchical ReAct: a triage meta-planner delegating to specialist agents
  - Reflection: draft, critique, revise, looping on the output rather than the task, at two to three times the tokens
  - Choosing a shape: ReAct for cheap, debuggable short tasks; plan-then-execute for parallel steps and predictable cost; reflection for written output
  - Retrieval as one tool among several: the agent decides whether to retrieve, rewrites the query, retrieves again mid-task, and re-retrieves to verify a draft against its source
- The Claude Agent SDK: the Claude Code harness as a library; `query()` and its message stream; built-in file, shell and search tools; permissions and permission modes; hooks for deterministic enforcement; the difference between an SDK tool runner, the Agent SDK and provider-hosted agents
- **LangChain and LangGraph**
  - Chains as fixed pipelines versus graphs with cycles
  - Typed state, nodes, conditional edges and compilation (`StateGraph`, `add_node`, `add_edge`, `add_conditional_edges`, `compile`)
  - LangChain's components: one model interface across providers; tools declared with `@tool` from a function's type hints and docstring; messages; structured output validated against a schema, enforced by the provider in strict mode; retrievers, MCP servers and other agents plugged in as tools
  - Runnables composed with `|` into prompt, model and parser chains, each supporting `invoke`, `batch` and `stream`; chains as one-way data flow with no loops, pauses or saved state
  - State reducers: each field's merge rule (overwrite, append, add) so that nodes writing the same field never clobber each other; nodes returning only what changed
  - Execution in super-steps: run the active nodes, merge their updates through the reducers, save a checkpoint, follow the edges; termination at `END` or the recursion limit
  - Thread checkpointers (SQLite, PostgreSQL) keyed by `thread_id`, so a run outlives its process; time travel by rewinding to an earlier checkpoint and re-running; human-in-the-loop interrupts that pause before a write and resume later; streaming of tokens, per-node state updates or custom events; summarization nodes against state growth
  - Multi-agent graphs: each specialist a subgraph added as one node, sharing state or returning a summary; handoffs in which a node returns both the next node and a state update (`Command`); fan-out with the number of parallel branches decided at run time (`Send`)
  - The prebuilt `create_agent` loop and middleware for summarization, approval and call limits; tracing runs as a tree of spans with latency, cost and retries (LangSmith, Langfuse)
  - Explicit state machines versus hidden prompts and hard debugging
- **Agent memory**
  - Three lifetimes: conversation state for one thread, task state for one run (what is done, what remains, what must be re-checked), and long-term memory across sessions
  - Short-term thread state versus long-term semantic memory in a vector store, written through save and update tools
  - Timestamps, pruning and conflict resolution against contradictory memories; retrieving only the most relevant memories
  - Memory as persistence across stateless model calls
- **Workflow orchestration and durable execution**
  - Data-pipeline schedulers (Airflow: DAGs, operators, sensors, retries, backfill and catch-up)
  - Serverless step orchestrators (steps in YAML or JSON, retries with backoff, callbacks, parallel branches, long-held state)
  - Queues with per-task retry and rate control
  - Durable-execution engines (Temporal): deterministic replay from event history; side effects in activities
  - Idempotency keys, bounded retries, timeouts at every level, compensating steps, human approval as a paused workflow, timers and callbacks instead of sleeping processes, checkpointed agent state
  - Long-running agents as jobs rather than inside requests
- **Reliability of a deployed agent**
  - Six failure modes: a tool that hangs; a tool that fails (transient or permanent); a tool that correctly returns nothing; a call with wrong arguments; a loop that does not converge; a world that changed between steps
  - Infrastructure failures retried with backoff; semantic failures returned to the model as observations to plan around; a run that never crashes silently, since an uninformed model may invent a result
  - Retry safety by action type: searches repeated freely; a booking whose reply was lost repeated only under an idempotency key, so the provider answers "already booked" with the same ticket
  - Three nested clocks: a tool-call timeout inside a node or model-call timeout inside a whole-run deadline, so the innermost names the stalled dependency
  - Tool fallback order: live data, then cached data labelled stale, then asking the user; a degraded answer that declares itself rather than a confident figure no tool returned; failing loudly with what was and was not done
- **Multi-agent systems**
  - Topologies: supervisor with workers, a triage agent with specialists, hierarchical teams, handoffs between specialists, pipelines, debate and critic pairs, shared task boards
  - Message passing versus shared state
  - When splitting pays (breadth-first, independent sub-questions exceeding one context, too many tools for one agent) and when it does not (tightly coupled edits)
  - Token cost: agents use about 4× the tokens of a chat and multi-agent systems about 15×
  - Failures: lost context, duplicated work, runaway cost, mutual agreement with mistakes, conflicting merges, endless delegation, parallel writes, goals lost across handoffs
  - Controls: per-agent system prompts as guardrails, typed hand-off messages carrying claim sources, per-agent and total budgets, hard stops, one writer per resource, verifiers
  - Where one agent breaks: several goals traded off invisibly in one prompt; sub-task results that conflict with nothing comparing them; one context crowded by every tool and document
  - An agent's contract: its role, model, permitted tools, state, input and output schema, and limits; precise, non-overlapping roles that a coordinator can choose between
  - The hand-off payload: task ID, goal, constraints and return format rather than the whole conversation; who may change a decision and who only recommends
  - The coordination cycle: decompose into bounded tasks, execute (in parallel when independent, in sequence when one needs another's result), attribute each result to its agent and task, reconcile and re-plan
  - Bounding the loop: a round limit, a token budget, a deadlock check for the same conflict recurring, and escalation of the partial plan to a person
  - Results validated against schema, required fields and hard constraints before entering shared state; failures recorded as structured errors, then retried, reassigned or raised to the user
  - Supervisor (simple governance and tracing, one hub for all messages) versus peer-to-peer (fewer hops, harder-to-control paths)
  - Permissions: read and analyse agents run automatically within limits; write actions are proposed by the coordinator and confirmed by a person
  - Messages between agents as untrusted input: tagged as data, checked against constraints, flagged and logged, never obeyed as instructions
  - Logging at every hand-off: the delegation and its context, tool call and arguments, raw result, validation outcome, latency and retries, approvals of writes
  - Evaluation: agent and tool selection accuracy, argument correctness, task completion or a clear refusal, groundedness of every figure in a tool result, conflicts caught before acting, rounds and cost to finish
  - The agent-framework landscape (Claude Agent SDK, OpenAI Agents SDK, Google ADK, Microsoft Agent Framework, Pydantic AI, Strands, Mastra, Agno): chosen by stack; the loop is portable, the state store is not, and the protocol layer outlives any one of them
  - Interoperability standards: MCP for agents reaching tools and data, A2A for agents reaching agents, and proposals for decentralized agent identity, discovery and messaging (ANP, AGNTCY)
  - Cross-boundary agents with Google's Agent Development Kit and A2A
- **Agent-to-agent protocol (A2A)**
  - JSON-RPC 2.0 `message/send` with message parts and session and context IDs; standard JSON-RPC errors
  - Task tracking: submitted, working, artifacts, streaming, terminal states
  - AgentCards: identity, URL, transport, provider, version, capabilities, security schemes, input and output modes, skills, signatures; validation and versioning
  - Tool errors mapped to task failure rather than a hang
- **LLM routing across agents**
  - Retrieving a shortlist of agents by embedding, lexical and metadata features, then reranking
  - A schema-constrained pick (agent ID, confidence, reason) with an explicit fallback policy and no silent pick
  - An evaluation event per decision: candidates, versions, choice, confidence, fallback reason, latency, cost, later success label
  - Edge cases: empty registry, embedding timeouts, near-zero scores, unroutable agents, oversized queries, injection attempts, stale versions, cold-start agents

### Claude Code

- Memory files (`CLAUDE.md`) and their hierarchy: enterprise policy, user, project, local
- Settings files (`settings.json`, `settings.local.json`) and managed settings that cannot be overridden
- Permission rules (allow, ask, deny); skills, slash commands and subagents as project files; hooks on tool events that can block; project MCP configuration (`.mcp.json`); plan mode and auto-accept modes
- Shared project configuration in the repository versus personal local files
- Headless runs (`claude -p`) with JSON or streamed JSON output; exit codes; restricted tools and permissions for unattended runs; CI integrations; keys as CI secrets; cost and time limits per run
- Running against Claude on Gemini Enterprise Agent Platform or Amazon Bedrock to keep traffic and billing in the customer's cloud

### Security and safety of LLM applications

- The lethal trifecta: private data, untrusted content and an exfiltration channel in one agent; removing one leg
- Least-privilege tools; sandboxing (no network, one directory); human approval before irreversible actions
- System prompts as guardrails (scope, refusal rules, output limits); input and output guardrail classifiers and their false-positive cost
- Hooks as deterministic enforcement; staged rollouts, feature flags and kill switches
- Handling refusals in code
- API keys scoped to workspaces with spend limits; rotation; no keys in browsers or mobile apps; keys in a secret manager
- Per-user identity carried through MCP so actions are attributable
- Enterprise data questions: retention, training on inputs, processing location, compliance reports; minimizing personal data before sending
- Egress controls and service perimeters removing the exfiltration leg

### Evaluation, testing and debugging

- Success criteria agreed before building: specific, measurable, tied to business outcomes (accuracy, latency, cost per task, refusal rate)
- Output quality versus system performance; golden datasets with hard and adversarial cases
- Code-graded, model-graded and human grading; agreement among humans and graders by Cohen's κ, Fleiss' κ and Krippendorff's α
- **Reference-based text metrics**
  - Word-overlap precision and recall; ROUGE-N and ROUGE-L (longest common subsequence, optional stemming)
  - BLEU: clipped n-gram precision, brevity penalty exp(1 − r ÷ c), corpus-level aggregation
  - METEOR: recall-weighted harmonic mean over exact, stem and synonym matches with a fragmentation penalty
  - Levenshtein distance; BERTScore greedy matching of contextual embeddings into precision, recall and F1; BLEURT as a learned metric
  - Blind spots for paraphrase, factuality and open-ended answers
- **Model graders (LLM as a judge)**
  - Pointwise scores versus pairwise preferences (MT-Bench, Chatbot Arena)
  - Rubrics with concrete levels, reasoning before verdict, one criterion per call; G-Eval (generated evaluation steps, form filling, probability-weighted scores)
  - Dimensions: helpfulness, factuality, relevance, tone, style, safety; task completion and tool-call correctness for agents
  - Validation against humans; position, length and self-preference biases and their controls
- **Factuality and hallucination detection**: entailment (NLI) scoring against sources; importance-weighted atomic-fact scoring; groundedness checks against retrieved context; agreement across samples; real-time output filters
- Pass rates as binomial proportions with Wilson score intervals; sample size n ≈ 1.96² p(1 − p) ÷ E² (at most 385 for E = 0.05)
- Comparing prompts or models on the same items with McNemar's test χ² = (b − c)² ÷ (b + c)
- Regression suites in CI on every prompt or model change; offline golden sets before release, A/B tests and feedback after
- Systematic debugging: reproduce with the recorded request; read `stop_reason`, `usage`, raw blocks, tool calls and results before touching the prompt
- Common failures: silent truncation, malformed tool calls, misread tool results, refusals, context overflow, caches that never hit, retry storms
- Tracing LLM applications: one trace per request, spans per model and tool call with prompt version, model ID, tokens, cost and latency; redacted logs

### Application architecture and LLMOps

- Synchronous versus asynchronous calls; queues for work that can wait
- Caching at three levels: prompt caching, response caching, retrieval caching
- **Semantic caching**: similarity-threshold lookup as a precision decision set from labelled same/different question pairs, biased high because a false hit costs more than a miss; savings as hit rate × cost per call; keys including tenant, permission scope, prompt version and model; expiry when sources change
- **The LLM (AI) gateway**: authentication and per-team keys, rate limits and spend budgets in tokens, throttling and fallback models, failover across models and providers, model cascades, logging with redaction, guardrail hooks, enforcement of pinned model IDs
- **Self-hosted model serving**
  - vLLM: PagedAttention storing the key–value cache in fixed-size blocks to cut fragmentation; continuous batching; prefix caching; an OpenAI-compatible server
  - GPU memory budgeting for weights plus key–value cache; throughput versus latency
  - Asynchronous API front ends (FastAPI) streaming tokens; slim container images with weights mounted rather than baked in
- Fallbacks (smaller model, cached answer, human) and graceful degradation; latency budgets split across retrieval, model and tools; streaming for perceived latency
- Prototype → pilot → production and what each adds (evals, monitoring, cost controls, on-call)
- Model deprecation and migration: evals on the new model, a flag to switch back
- **LLMOps**
  - Releasing prompt, model ID, tool definitions, retrieval index, embedding model and configuration together as one versioned set
  - Eval gates in CI, shadow traffic, canary by traffic split, A/B tests, rollback by flag
  - Monitoring: scheduled golden-set scores; online grading of sampled traffic; time to first token, latency percentiles, tokens and cost per request and tenant, error classes, cache hit rates, retrieval health (empty results, citation share)
  - Drift in hosted-model systems: input-mix shift, provider model changes, stale corpora
  - The feedback flywheel: thumbs, edits and escalations turned into golden-set cases under privacy rules
  - SLOs and error budgets for latency, quality and cost; per-tenant budgets and quotas; kill switches

### The forward-deployed engineer's craft

- The FDE role: building and running production LLM applications inside a customer's systems
- Discovery: stakeholder mapping (who asks, pays, uses, can block); shadowing the workflow; five whys; the job to be done versus the proposed solution; scoping by value against feasibility; ROI against a measured baseline; explaining non-determinism to executives
- Delivering inside an enterprise: demos with real data and failure cases; design documents and decision memos; SSO, private networks, egress rules, security reviews, procurement and legal met early; hand-off with runbooks, dashboards, eval suites and training; feeding field learning back to product

### Exercises

- From scratch: a byte-level BPE tokenizer with a round-trip property test, measuring tokens per character across languages and code
- From scratch: a bigram model by counting and by gradient descent
- From scratch: a scalar autodiff engine and a small network, gradients checked by finite differences
- From scratch: scaled dot-product and multi-head attention, sinusoidal positions and a masked decoder block with cross-attention in NumPy, then in PyTorch
- From scratch: a tiny character-level GPT and a sampler with temperature, top-k, top-p, beam search, repetition penalties and stop sequences
- From scratch: a LoRA layer wrapped around a frozen linear layer, then a LoRA and a QLoRA fine-tune of a small open model with libraries, evaluated against the base model
- From scratch: BM25, brute-force cosine search and reciprocal rank fusion with recall@10 on labelled queries
- From scratch: IVF with k-means cells, product quantization with asymmetric distance tables and a small HNSW graph, measured for recall against a flat index and compared with FAISS and Chroma
- From scratch: BLEU, ROUGE-L and edit distance, compared with BERTScore and an LLM judge on the same outputs
- From scratch: a Messages API client with streaming, retries and a cost calculator; then the SDK
- From scratch: an agent loop with tools, then the Agent SDK, attacked with indirect prompt injection and defended
- From scratch: an MCP server in Go over stdio, then over Streamable HTTP with OAuth
- From scratch: a semantic cache and an LLM gateway with budgets, failover and redaction
- From scratch: a durable workflow runner with replay, compensation and human approval
- From scratch: a fine-tuning loop with warmup and cosine decay, gradient clipping and gradient accumulation, run with and without each to reproduce a loss spike and a divergence
- From scratch: a bottleneck adapter and a prompt-tuning layer on a frozen model, compared with LoRA on trainable parameters, accuracy and inference latency
- A forgetting experiment: a general suite scored before and after a narrow fine-tune, then recovered with rehearsal, an L2-SP penalty and weight interpolation across α
- From scratch: a toy CLIP with two encoders and the symmetric InfoNCE loss, used for zero-shot classification and text-to-image search with Recall@K
- A vision-encoder-to-language-model prototype for captioning or visual question answering: a projector trained with both towers frozen, then tested for hallucination against a blurred-image baseline
- Structured extraction from invoices with a vision-language model: a JSON schema, missing-field handling and a field-level accuracy report against an OCR-only pipeline
- From scratch: late-interaction scoring over patch embeddings, then page-image retrieval compared with parse-then-embed on documents containing charts and tables
- A LangGraph travel-planning agent: typed state with reducers, a tool loop, a policy check that forces a re-plan, a PostgreSQL checkpointer, an approval interrupt before the booking tool, an idempotent retry, nested timeouts and a traced run
- A coordinator with three specialist agents: contracts, schema-validated hand-offs, a round limit, a poisoned tool result rejected as untrusted data, and the six multi-agent evaluation measures reported
- A long-context position experiment with Wilson intervals
- A support assistant with tools, guardrails and a 50-case golden set graded by a κ-validated model grader in CI
- A RAG pipeline with document parsing, contextual retrieval, query rewriting, hybrid search, reranking, verified citations and permission-aware retrieval, scored with RAGAS
- A multi-agent DevOps assistant in LangGraph: triage and specialist agents, checkpointed state, long-term memory and a retrieval gateway
- A prompt-optimization and compression experiment scored on a golden set
- A vLLM and FastAPI serving stack in containers with latency and token-cost logging and a groundedness filter
- An LLM routing service choosing agents from a shortlist, with A2A sample agents
- An authenticated remote MCP server; Claude Code run headless in CI
- A customer engagement simulated from discovery conversation to scoped design document and hand-off
- **Reasoning drills**
  - Estimate tokens, latency and cost for a workload before calling a model
  - Predict how a prompt or retrieval change moves an evaluation metric, then measure it with intervals
  - Derive attention's cost and the key–value cache memory for a given model size and context length
  - Estimate the quality gain that would justify a larger model's extra cost, then test it on a golden set
  - Predict an adapter's parameter count from d and m, and a run's optimizer steps from dataset size and effective batch, before training
  - Estimate how an agent's token bill grows with its step budget, then measure it with and without context trimming
  - Decide from a task description alone whether it needs a workflow, one agent or several, as a decision record

## Cloud Providers: Google Cloud, AWS, Azure & Certifications

**Prerequisites:** cloud computing concepts (service and deployment models, shared responsibility, well-architected pillars, FinOps, IAM models); virtualization and containers; networking (VPCs, subnets, routing, BGP, DNS, TLS, load balancing, CDNs); databases (relational, key-value, wide-column, document, warehouse) and their consistency models; distributed systems (replication, sharding, queues, consensus); security (cryptography, identity, zero trust); DevOps (CI/CD, IaC, observability, SRE); Bash scripting, JSON and `jq`; machine learning and LLM applications.

**Depth bar:** professional-certification depth on Google Cloud first, then on AWS and Azure by mapping each service and teaching what differs; every command is built by the learner.

**Capstone:** one multi-tier production workload built on Google Cloud end to end from the command line and Terraform, then ported to AWS and Azure, with a written comparison of identity, networking, operations and cost.

### Google Cloud — compute

- **Compute Engine**: machine families and types; instance templates and machine images; regional managed instance groups with autohealing health checks and autoscaling; Spot VMs; sole-tenant nodes; Shielded and Confidential VMs; Container-Optimized OS; the metadata server; outbound port 25 blocked
- **Google Kubernetes Engine**: Autopilot and Standard modes; node auto-provisioning; Workload Identity; Policy Controller; Dataplane networking and NetworkPolicy; Backup for GKE; Confidential GKE nodes; Agones for game servers
- **Cloud Run**
  - Services and jobs; revisions and traffic splitting for canaries and instant rollback
  - Per-instance concurrency, minimum and maximum instances, CPU and memory limits, request timeouts
  - The container contract: listen on `PORT`; SIGTERM then a 10-second grace period; TLS terminated at the front end; HTTP/2 end to end (h2c), gRPC, WebSockets and streamed responses; no raw UDP
  - Service identity and invoker IAM; service-to-service ID tokens whose audience is the receiver URL
  - Source deploys with buildpacks
- **Cloud Run functions** (Cloud Functions) and **App Engine**
- **Eventarc**: events from many sources delivered as CloudEvents

### Google Cloud — storage and databases

- **Cloud Storage**: strong consistency; Standard, Nearline, Coldline and Archive classes; lifecycle rules; object versioning; retention policies; signed URLs; resumable uploads; backend buckets behind Cloud CDN; public access prevention
- **Block and file**: Persistent Disk and Hyperdisk, Local SSD, snapshots; Filestore for shared NFS
- **Backup and DR Service**
- **Cloud SQL**: MySQL, PostgreSQL and SQL Server; editions; backups and point-in-time recovery; regional HA with a synchronous standby (not a read replica); same- and cross-region read replicas and their promotion; private IP; the Cloud SQL Auth Proxy and language connectors; IAM database authentication; Query Insights; database flags; maintenance windows; storage autosizing; instance count × pool size against `max_connections`
- **AlloyDB**: PostgreSQL-compatible; read pool instances; columnar engine; managed connection pooling
- **Spanner**: horizontally scaled relational database with external consistency (TrueTime, Paxos); regional and multi-region configurations; interleaved tables; split by key range and load; key design against hotspots (UUIDv4, bit-reversed sequences); stale reads (exact and bounded staleness); read-only replicas; row-deletion (TTL) policies; Spanner Graph; GoogleSQL and PostgreSQL dialects; the emulator
- **Bigtable**: HBase-compatible wide-column store; row keys sorted lexicographically; tablets; throughput scaling with nodes; multi-cluster replication with app profiles and last-write-wins; per-column-family garbage-collection policies; row-key design (no timestamp-leading keys, salting, reversed domains); Key Visualizer; the emulator
- **Firestore**: Native mode (strong consistency, ACID transactions, real-time listeners, offline SDKs, automatic single-field and on-demand composite indexes), Datastore mode, MongoDB compatibility; Standard and Enterprise editions; TTL policies; multi-region locations; no full-text search
- **Memorystore**: Valkey, Redis, Redis Cluster and Memcached; eviction policies; zonal HA replicas; cluster mode hash slots; approximate LRU
- **BigQuery**: serverless warehouse with Dremel-style execution; partitioning and clustering; nested and repeated fields; materialized and authorized views; result cache; `INFORMATION_SCHEMA` job statistics; dry-run byte estimates and cost controls; streaming inserts versus batch loads; federated queries; search indexes; BigQuery ML; the sandbox
- **Choosing a store**
  - Relational single-region OLTP → Cloud SQL; high-performance PostgreSQL with mixed analytics → AlloyDB; global relational with strong consistency → Spanner
  - High-throughput time series and wide-column → Bigtable; documents and mobile sync → Firestore; caches, sessions and leaderboards → Memorystore
  - Analytics → BigQuery; blobs → Cloud Storage; shared POSIX files → Filestore
  - Anti-choices: a cache as system of record; a warehouse on the checkout path; object or file storage as a database; Bigtable for ad-hoc joins
  - Native TTL (Firestore TTL, Spanner row deletion, Bigtable GC, Cloud Storage lifecycle) over scheduled sweepers
  - Multi-writer options: Spanner multi-region, Bigtable multi-cluster routing, Firestore multi-region; Cloud SQL has no multi-primary mode and does not shard itself

### Google Cloud — networking

- **VPC**: global VPCs with regional subnets; firewall rules and Cloud NGFW; routes and Cloud Router; Shared VPC host and service projects; VPC peering; Private Google Access; Private Service Connect; Network Connectivity Center; reserved static IPs
- **Cloud NAT** for egress with static IPs; Secure Web Proxy
- **Hybrid connectivity**: Cloud VPN and HA VPN; Dedicated and Partner Interconnect
- **Cloud Load Balancing**
  - Application Load Balancers (L7): global external, regional external, internal, cross-region internal; URL maps with host and path rules; backend services; health checks; backends as MIGs and NEGs (zonal, serverless, internet)
  - Network Load Balancers (L4): proxy (TCP termination) and passthrough (preserving clients, UDP)
  - One anycast IP steering users to the nearest healthy region; HTTP/1.1, HTTP/2 and HTTP/3 to clients
  - Locality policies including ring hash and Maglev for cache affinity
  - Google-managed certificates; Certificate Manager; SSL policies setting minimum TLS versions
- **Cloud DNS**: public and private zones; DNSSEC; routing policies (weighted round robin, geolocation with geofencing, failover) with health checks; DNS logging; Cloud Domains
- **Cloud CDN**: pull CDN on the global Application LB; origins as backend buckets, instance groups and external origins; cache modes (`CACHE_ALL_STATIC`, `USE_ORIGIN_HEADERS`, `FORCE_CACHE_ALL`); TTLs and cache keys; signed URLs and cookies; invalidation; serve-while-stale; GET and HEAD only
- **Media CDN** for large video and downloads; **Firebase Hosting** for static and web front ends with custom headers
- **Service Directory**; **Cloud Service Mesh** (managed Istio and Envoy) for mTLS, retries and traffic management
- **API Gateway, Cloud Endpoints and Apigee**: OpenAPI and gRPC with transcoding; keys, quotas, analytics, spike arrest
- **Network Intelligence Center** and Connectivity Tests

### Google Cloud — data and analytics

- **Pub/Sub**: topics and subscriptions; push and pull; at-least-once delivery; ordering keys; dead-letter topics; retry with exponential backoff; exactly-once delivery for pull subscriptions; message retention and seek; Avro and Protobuf schemas
- **Managed Service for Apache Kafka**
- **Cloud Tasks** (HTTP targets, per-queue rate and concurrency limits, scheduled tasks) and **Cloud Scheduler**
- **Workflows** for serverless orchestration with callbacks; **Cloud Composer** (Apache Airflow)
- **Dataflow** (Apache Beam: pipelines, `DoFn` lifecycle, windows and watermarks, streaming and batch); **Dataproc** and Dataproc Serverless (Spark, Hadoop, the Cloud Storage connector)
- **Datastream**, **Data Fusion**, **Dataplex**, **BigLake**, **Analytics Hub**
- **Looker** and **Looker Studio**
- Log sinks into BigQuery and Log Analytics; billing export to BigQuery

### Google Cloud — AI and ML

- **Gemini Enterprise Agent Platform** (formerly Vertex AI): Workbench, custom training with accelerators, Pipelines, Feature Store, Model Registry, Experiments, endpoints, Model Monitoring, Vizier hyperparameter tuning, AutoML, Evals (formerly the Gen AI evaluation service)
- Model Garden (Gemini, Claude and open models); Agent Studio
- Agent Development Kit (ADK); Agent Runtime (Agent Engine); managed sessions and Memory Bank; Agent Identity and principal access boundary policies; Agent Registry; Google Cloud MCP servers; Agents CLI
- Vector Search; Agent Retrieval (formerly Vector Search 2.0); Agent Search (formerly Vertex AI Search); RAG Engine; text-embedding models
- Claude on Google Cloud: a regional or global endpoint with the model in the URL; Application Default Credentials instead of API keys; per-region quotas; billing through the Google Cloud account
- Gemini Enterprise, Agent Designer and Customer Experience Agent Studio for low-code agents
- Pre-built AI APIs: Vision, Video Intelligence, Speech-to-Text, Natural Language, Translation, Document AI
- Model Armor for prompt and response screening

### Google Cloud — security

- **IAM**: principals, basic, predefined and custom roles; allow and deny policies; IAM Conditions in CEL; service accounts and the `actAs` path; disabling service-account key creation; Workload Identity Federation (for example GitHub OIDC); Workforce Identity Federation; Policy Analyzer and the IAM recommender
- **Organization Policy Service**: resource-location restrictions, public access prevention, key-creation bans
- **Cloud KMS**: key rings and keys; key purposes (symmetric encryption, asymmetric signing and decryption); CMEK; key versions, disabling and scheduled destruction; Cloud HSM and Cloud EKM; envelope encryption; Tink for application-layer AEAD
- **Secret Manager**: versions, rotation, access at start-up, integration with GKE
- **Identity-Aware Proxy**: OAuth consent, the accessor role, signed headers the app must validate; IAP is not object-level authorization
- **Identity Platform**: email/password, OIDC and SAML providers, MFA factors, multi-tenancy, session policies; reCAPTCHA Enterprise
- **VPC Service Controls** perimeters against data exfiltration
- **Cloud Armor**: preconfigured WAF rules based on the OWASP Core Rule Set; custom rules in CEL; rate-based rules; Adaptive Protection; edge DDoS defence
- **Binary Authorization** with attestations; **Artifact Registry** (remote repositories, vulnerability scanning, Artifact Analysis); Cloud Build provenance
- **Security Command Center** findings; Web Security Scanner; **Google SecOps** (SIEM and SOAR); Cloud IDS
- **Sensitive Data Protection**: infoTypes, inspection and de-identification (deterministic and format-preserving tokens)
- **Cloud Audit Logs**: Admin Activity and Data Access logs; sinks to protected buckets and BigQuery
- Confidential VMs, Confidential GKE nodes and Confidential Space; Assured Workloads; Certificate Manager; Cloud Asset Inventory; Compliance Reports Manager

### Google Cloud — operations, DevOps and cost

- Cloud Build (multi-stage builds, provenance, private pools); Cloud Deploy; Artifact Registry
- Infrastructure Manager and Config Connector
- Cloud Monitoring (distribution metrics, SLO monitoring, alerting on log-based metrics), Cloud Logging (`jsonPayload`, severity), Cloud Trace (OpenTelemetry export), Cloud Profiler, Error Reporting, Managed Service for Prometheus, Service Health
- Cloud client libraries: one client per process; Application Default Credentials; functional options; REST and gRPC transports; page iterators; pluggable retry policies
- Cloud Billing reports, budgets and alerts, labels; the Pricing Calculator; Recommender (Active Assist); Cloud Quotas; Carbon Footprint

### Google Cloud — command line

- **Installing and configuring `gcloud`**
  - The Google Cloud CLI and its bundled tools (`gcloud`, `bq`, the legacy `gsutil`); Cloud Shell with the CLI preinstalled; `gcloud components install` and `update` (not available when installed by a system package manager)
  - `gcloud init`; `gcloud auth login` for a person versus `gcloud auth application-default login` for client libraries (Application Default Credentials); `gcloud auth list`; `gcloud auth revoke`
  - Named configurations: `gcloud config configurations create`, `activate` and `list`; `gcloud config set project`, `compute/region` and `compute/zone`; `gcloud config list`; `CLOUDSDK_CORE_PROJECT`-style environment overrides
  - Acting as a service account without keys: `--impersonate-service-account` per command or `auth/impersonate_service_account` in a configuration
  - Tokens for scripts: `gcloud auth print-access-token`; `gcloud auth print-identity-token --audiences` for calling private Cloud Run services
- **Command structure and output**
  - Grammar: `gcloud [release track] component entity operation positional --flags`; release tracks `alpha` and `beta` beside GA
  - Global flags: `--project`, `--quiet` (`-q`) for non-interactive runs, `--verbosity=debug`, `--log-http`, `--billing-project`
  - `--format` as `json`, `yaml`, `csv`, `table(name, status)` or `value(name)`, with projections and transforms; `--filter` expressions (`status=RUNNING AND zone:us-central1`); `--sort-by`, `--limit`, `--page-size`; `--uri`
  - Help: `gcloud help`, `--help`, `gcloud topic filters`, `formats` and `configurations`; `gcloud cheat-sheet`
  - Scripting: `value()` output into shell variables; `describe … --format=json` piped into `jq`; idempotent create-or-describe checks; non-zero exit codes on failure
- **Projects, APIs, billing and hierarchy**
  - `gcloud projects create`, `list` and `describe`; `gcloud resource-manager folders create`; `gcloud organizations list`
  - `gcloud services enable` and `list --enabled`
  - `gcloud billing accounts list`; `gcloud billing projects link`; `gcloud billing budgets create` with threshold rules
- **IAM**
  - `gcloud iam service-accounts create`, `list` and `keys list`; avoiding `keys create`
  - Project bindings: `gcloud projects add-iam-policy-binding --member=serviceAccount:… --role=roles/…` with `--condition`; `remove-iam-policy-binding`; `get-iam-policy --flatten=bindings[].members --filter --format` to list who holds what
  - Resource-level bindings: `gcloud iam service-accounts add-iam-policy-binding` granting `roles/iam.serviceAccountUser` or `roles/iam.workloadIdentityUser`; the same verb on buckets, secrets, Cloud Run services and IAP
  - `gcloud iam roles create --permissions` and `describe`; `gcloud iam list-testable-permissions`
  - Workload Identity Federation: `gcloud iam workload-identity-pools create`, `providers create-oidc` with an attribute mapping and condition, `create-cred-config`
  - Auditing: `gcloud asset search-all-iam-policies`, `gcloud asset search-all-resources`; `gcloud policy-intelligence troubleshoot-policy iam`
  - Organization policies: `gcloud org-policies describe`, `set-policy` and `list`
- **Compute Engine**
  - `gcloud compute instances create` with `--machine-type`, `--image-family` and `--image-project`, `--subnet`, `--no-address`, `--service-account` and `--scopes=cloud-platform`, `--metadata-from-file=startup-script=`, `--shielded-secure-boot`, `--provisioning-model=SPOT`
  - `gcloud compute instances list`, `describe`, `stop`, `start`, `delete`; `add-metadata`; `get-serial-port-output`
  - `gcloud compute ssh` with `--tunnel-through-iap`; `gcloud compute start-iap-tunnel` for other ports; OS Login
  - `gcloud compute instance-templates create`; `gcloud compute instance-groups managed create`, `set-autoscaling` and `rolling-action start-update` with `--max-surge` and `--max-unavailable`; health checks with `gcloud compute health-checks create`
  - Disks, images and snapshots: `gcloud compute disks create` and `snapshot`; `gcloud compute images create`; snapshot schedules as resource policies
- **Networking**
  - `gcloud compute networks create --subnet-mode=custom`; `gcloud compute networks subnets create --range --enable-private-ip-google-access`
  - `gcloud compute firewall-rules create` with `--direction`, `--allow`, `--source-ranges`, `--target-tags` or `--target-service-accounts`, `--priority`; `list --format=table(…)`
  - `gcloud compute routers create`; `gcloud compute routers nats create --auto-allocate-nat-external-ips --nat-all-subnet-ip-ranges`
  - `gcloud compute addresses create` (`--global` or `--region`)
  - Load balancer pieces in order: `health-checks`, `backend-services create` and `add-backend`, `url-maps create`, `ssl-certificates create --domains` (Google-managed), `target-https-proxies create`, `forwarding-rules create`; `backend-services update --enable-cdn`; serverless NEGs with `network-endpoint-groups create --network-endpoint-type=serverless`
  - `gcloud compute security-policies create` and `rules create --expression --action` for Cloud Armor
  - `gcloud dns managed-zones create` (public or `--visibility=private`); `gcloud dns record-sets create --type --ttl --rrdatas`
  - `gcloud compute vpn-gateways` and `vpn-tunnels`; `gcloud compute networks peerings create`
- **Cloud Run and serverless**
  - `gcloud run deploy` with `--image` or `--source`, `--region`, `--service-account`, `--no-allow-unauthenticated`, `--set-env-vars`, `--set-secrets=ENV=secret:latest`, `--min-instances`, `--max-instances`, `--concurrency`, `--cpu`, `--memory`, `--timeout`, `--vpc-egress`
  - Functions on Cloud Run: `gcloud run deploy --function` with `--base-image`; the older `gcloud functions deploy`
  - Canary releases: `gcloud run deploy --no-traffic --tag`; `gcloud run services update-traffic --to-revisions=REVISION=10` or `--to-latest`; `gcloud run revisions list`
  - `gcloud run services describe` and `list`; `gcloud run services logs read`; `gcloud run services add-iam-policy-binding --role=roles/run.invoker`; `gcloud run services proxy` for local testing of private services
  - Jobs: `gcloud run jobs create`, `execute --wait`, `executions list`
  - `gcloud app deploy` for App Engine; `gcloud eventarc triggers create`
- **Kubernetes Engine**
  - `gcloud container clusters create-auto` (Autopilot) versus `clusters create` (Standard) with `--release-channel`, `--enable-private-nodes`, `--workload-pool=PROJECT_ID.svc.id.goog`, `--enable-ip-alias`
  - `gcloud container clusters get-credentials` to write a kubeconfig context; `clusters upgrade`; `clusters resize`
  - `gcloud container node-pools create` with machine types, autoscaling bounds, Spot nodes and taints
- **Storage and databases**
  - Cloud Storage: `gcloud storage buckets create gs://bucket --location --uniform-bucket-level-access --public-access-prevention`; `gcloud storage cp` (`--recursive`), `mv`, `rm`, `ls`, `cat`, `du`; `gcloud storage rsync --recursive --delete-unmatched-destination-objects --dry-run`; `gcloud storage buckets update` for versioning, lifecycle files and default storage class; `gcloud storage objects update --storage-class`; `gcloud storage sign-url --duration`; `gcloud storage buckets add-iam-policy-binding`; `gcloud storage restore` for soft-deleted objects
  - Legacy `gsutil` equivalents (`gsutil -m cp`, `gsutil rsync`, `gsutil signurl`) recognized in older scripts
  - Cloud SQL: `gcloud sql instances create --database-version=POSTGRES_… --tier --region --availability-type=REGIONAL --no-assign-ip --network`; `gcloud sql databases create`; `gcloud sql users create`; `gcloud sql instances patch`; `gcloud sql backups create` and `list`; `gcloud sql instances clone --point-in-time`; `gcloud sql instances promote-replica`; `gcloud sql connect`
  - Spanner: `gcloud spanner instances create --config --processing-units`; `gcloud spanner databases create --ddl` and `execute-sql`
  - Bigtable: `gcloud bigtable instances create`; the `cbt` tool (`cbt createtable`, `createfamily`, `set`, `read`, `count`) with a `.cbtrc`
  - Firestore: `gcloud firestore databases create --location`; `gcloud firestore indexes composite create`; `gcloud firestore export` and `import`
  - Memorystore: `gcloud redis instances create --tier --size`
  - Local emulators: `gcloud emulators firestore start` and `gcloud emulators spanner start`; `gcloud beta emulators pubsub start` and `bigtable start`; `env-init` for client environment variables
- **BigQuery with `bq`**
  - `bq mk --dataset --location`; `bq mk --table` with a schema, `--time_partitioning_field`, `--clustering_fields` and expiration
  - `bq load --source_format=CSV` or `NEWLINE_DELIMITED_JSON`, `PARQUET` and `AVRO` with `--autodetect` or an explicit schema; `--replace`
  - `bq query --use_legacy_sql=false` with `--dry_run` for byte estimates, `--maximum_bytes_billed` as a guard, `--parameter` for parameterized queries and `--destination_table`
  - `bq ls`, `bq show --schema --format=prettyjson`, `bq head`, `bq cp`, `bq extract --destination_format`, `bq update`, `bq rm -r -f`; `bq ls -j` and `bq show -j` for jobs
- **Messaging, scheduling and pipelines**
  - Pub/Sub: `gcloud pubsub topics create` and `publish --message --attribute`; `gcloud pubsub subscriptions create` with `--ack-deadline`, `--push-endpoint`, `--dead-letter-topic`, `--max-delivery-attempts`, `--enable-message-ordering`, `--enable-exactly-once-delivery`; `subscriptions pull --auto-ack --limit`; `subscriptions seek --time`
  - `gcloud scheduler jobs create http --schedule --uri --oidc-service-account-email`; `gcloud tasks queues create --max-dispatches-per-second --max-concurrent-dispatches`; `gcloud tasks create-http-task`
  - `gcloud workflows deploy --source` and `run`; `gcloud dataflow jobs run`, `list` and `cancel`; `gcloud dataproc clusters create` and `jobs submit`; `gcloud dataproc batches submit pyspark`; `gcloud composer environments run`
- **Security services**
  - Secret Manager: `gcloud secrets create --replication-policy`; `gcloud secrets versions add --data-file=-`; `gcloud secrets versions access latest`; `versions disable` and `destroy`
  - Cloud KMS: `gcloud kms keyrings create`; `gcloud kms keys create --purpose=encryption --rotation-period --next-rotation-time`; `gcloud kms encrypt` and `decrypt` with `--plaintext-file` and `--ciphertext-file`; `gcloud kms keys versions destroy`
  - `gcloud access-context-manager perimeters create` and `dry-run` for VPC Service Controls; `gcloud iap web add-iam-policy-binding`
- **Build, deploy and artifacts**
  - `gcloud artifacts repositories create --repository-format=docker --location`; `gcloud auth configure-docker REGION-docker.pkg.dev`; `gcloud artifacts docker images list` and `describe` with vulnerability findings
  - `gcloud builds submit --tag` or `--config=cloudbuild.yaml` with `--substitutions`; `gcloud builds triggers create github`; `gcloud builds log --stream`
  - `gcloud deploy apply --file=clouddeploy.yaml`; `gcloud deploy releases create`; `gcloud deploy releases promote`; `gcloud deploy rollouts approve`
  - `gcloud infra-manager deployments apply` for Terraform through Infrastructure Manager
- **Operations**
  - `gcloud logging read` with a filter (`resource.type`, `severity>=ERROR`, `jsonPayload.field`), `--freshness`, `--limit` and `--format`; `gcloud logging sinks create` to BigQuery, Cloud Storage or Pub/Sub with exclusions; `gcloud logging metrics create`
  - `gcloud monitoring policies create --policy-from-file`; `gcloud monitoring dashboards create`; `gcloud monitoring uptime create`
  - `gcloud compute operations list` and `gcloud container operations wait` for long-running operations
- **AI services**: `gcloud ai models upload`; `gcloud ai endpoints create`, `deploy-model` and `predict`; `gcloud ai custom-jobs create`; `gcloud ai indexes` and `index-endpoints` for Vector Search; `gcloud ai model-garden`

### Google Cloud — mapping system-design components

- DNS → Cloud DNS; CDN → Cloud CDN or Media CDN; load balancer → Cloud Load Balancing; reverse proxy → the global Application LB, NGINX on Compute Engine or GKE, or Cloud Run's front end
- Application servers → Cloud Run, GKE, MIGs, App Engine; workers → Cloud Run jobs, GKE, Cloud Run functions
- Object store → Cloud Storage; SQL with replicas → Cloud SQL, AlloyDB, Spanner; wide-column → Bigtable; documents → Firestore; cache → Memorystore
- Message queue → Pub/Sub or Managed Kafka; task queue and scheduler → Cloud Tasks and Cloud Scheduler; warehouse → BigQuery; batch → Dataflow, Dataproc, BigQuery SQL
- Search → Elasticsearch or OpenSearch on GKE, Elastic Cloud, Agent Search
- Service discovery → Service Directory, GKE DNS, Cloud Service Mesh; autoscaling → MIG autoscaler, Cloud Run, GKE autoscalers
- Monitoring → Cloud Monitoring, Logging, Trace, Error Reporting; push notifications → Pub/Sub, Cloud Run and Firebase Cloud Messaging; email through a partner relay
- Secrets → Secret Manager and Cloud KMS; WAF and DDoS → Cloud Armor; private networking → VPC, firewall rules, Cloud NAT, Private Google Access, IAP
- Paper systems to products: MapReduce → Dataflow and Dataproc; Spark → Dataproc; Storm → Dataflow streaming; Bigtable and HBase → Bigtable; Cassandra → Bigtable; Dynamo → Firestore, Bigtable or Spanner; MongoDB → Firestore with MongoDB compatibility or Atlas; Memcached and Redis → Memorystore; GFS → Colossus beneath Cloud Storage; HDFS → Cloud Storage; Dapper → Cloud Trace; Kafka → Pub/Sub or Managed Kafka; Chubby and ZooKeeper → no managed equivalent (etcd behind the GKE API server)

### AWS

- Compute: EC2, Lambda, ECS and EKS (managed node groups, IRSA) with Fargate, App Runner, Elastic Beanstalk
- Storage and databases: S3, EBS, RDS, Aurora and Aurora Global Database, DynamoDB, Keyspaces, ElastiCache
- Networking: VPC, ELB (ALB, NLB, GWLB), Route 53, CloudFront, Direct Connect, Transit Gateway, Site-to-Site VPN
- Data: Kinesis, Glue, Redshift, EMR, MWAA, QuickSight
- AI and ML: SageMaker, Bedrock
- Security: IAM, Organizations and service control policies, KMS, Secrets Manager, GuardDuty, Security Hub, Macie, WAF, Shield, Network Firewall; Zelkova-style automated policy reasoning
- DevOps: CodeBuild, CodePipeline, CodeDeploy, CloudFormation, CDK, ECR, CloudWatch, X-Ray

### AWS command line

- **Setup and credentials**
  - AWS CLI version 2; `aws configure` writing `~/.aws/credentials` and `~/.aws/config`; named profiles with `--profile` or `AWS_PROFILE`; `--region` or `AWS_REGION`
  - IAM Identity Center sign-in: `aws configure sso` and `aws sso login`; short-lived credentials instead of long-lived access keys
  - The credential provider chain: command-line options, environment variables, SSO and assumed-role profiles, shared files, container and instance metadata roles
  - `aws sts get-caller-identity` to confirm who you are; `aws sts assume-role --role-arn --role-session-name`; `role_arn` and `source_profile` in profiles
- **Command structure and output**
  - `aws service operation --parameters`; high-level `aws s3` commands versus API-shaped `aws s3api`
  - `--output json`, `yaml`, `text` or `table`; `--query` with JMESPath (`Reservations[].Instances[].[InstanceId,State.Name]`); server-side `--filters Name=…,Values=…`
  - Pagination: automatic by default; `--max-items`, `--starting-token`, `--page-size`, `--no-paginate`
  - `--dry-run` permission checks for EC2; waiters such as `aws ec2 wait instance-running`; `--cli-input-json` with `--generate-cli-skeleton`; `file://` and `fileb://` arguments; `--debug`; `aws help`
- **Common services**
  - S3: `aws s3 ls`, `mb`, `cp --recursive`, `sync --delete`, `mv`, `rm`, `presign --expires-in`; `aws s3api put-bucket-versioning`, `put-public-access-block`, `put-bucket-lifecycle-configuration`, `put-bucket-policy`, `get-object --range`
  - EC2 and VPC: `aws ec2 run-instances --image-id --instance-type --subnet-id --security-group-ids --iam-instance-profile --user-data`; `describe-instances`; `stop-instances` and `terminate-instances`; `create-vpc`, `create-subnet`, `create-security-group`, `authorize-security-group-ingress`
  - Systems Manager: `aws ssm start-session --target` instead of SSH; `aws ssm get-parameter --with-decryption`; `aws ssm send-command`
  - IAM: `aws iam create-role --assume-role-policy-document file://trust.json`; `attach-role-policy` and `put-role-policy`; `create-instance-profile`; `aws iam simulate-principal-policy`; `aws accessanalyzer validate-policy`
  - Lambda: `aws lambda create-function --runtime --handler --role --zip-file fileb://`; `update-function-code`; `invoke --payload` with `--cli-binary-format raw-in-base64-out`; `publish-version` and aliases
  - Containers: `aws ecr create-repository`; `aws ecr get-login-password | docker login --username AWS --password-stdin ACCOUNT.dkr.ecr.REGION.amazonaws.com`; `aws ecs update-service --force-new-deployment`; `aws eks update-kubeconfig --name`; `eksctl create cluster`
  - CloudFormation: `aws cloudformation deploy --template-file --stack-name --capabilities CAPABILITY_IAM --parameter-overrides`; `create-change-set` and `describe-change-set`; `describe-stack-events`; `aws cloudformation validate-template`
  - Data: `aws dynamodb create-table --billing-mode PAY_PER_REQUEST`, `put-item`, `get-item`, `query --key-condition-expression`; `aws rds create-db-instance`, `describe-db-instances`, `generate-db-auth-token`; `aws sqs send-message` and `receive-message`; `aws sns publish`
  - Security: `aws secretsmanager create-secret` and `get-secret-value`; `aws kms create-key`, `encrypt`, `decrypt`, `generate-data-key`
  - Observability and cost: `aws logs tail --follow`; `aws logs start-query` for Logs Insights; `aws cloudwatch put-metric-alarm`; `aws ce get-cost-and-usage`
  - Foundation models: `aws bedrock list-foundation-models`; `aws bedrock-runtime converse --model-id`
  - Related tools: AWS SAM CLI (`sam build`, `sam deploy --guided`, `sam local invoke`); the CDK CLI (`cdk bootstrap`, `synth`, `diff`, `deploy`)

### Azure

- Compute: Virtual Machines and scale sets, AKS (virtual nodes, workload identity), Container Apps, Container Instances, Functions, App Service with deployment slots
- Storage and databases: Blob Storage, Azure Files, Managed Disks, Azure SQL Database, Cosmos DB (including its Cassandra API), Azure Cache for Redis
- Networking: VNet, network and application security groups, Azure Load Balancer, Application Gateway, Front Door, Azure CDN, Azure DNS, ExpressRoute, VPN Gateway, Bastion, private and service endpoints
- Data: Synapse Analytics, Data Factory, Stream Analytics, HDInsight, Power BI
- AI and ML: Azure Machine Learning, Azure AI Foundry
- Identity and security: Microsoft Entra ID (Conditional Access, PIM, entitlement management, B2B, Agent ID), Azure RBAC, Key Vault, Microsoft Defender for Cloud, Defender XDR, Microsoft Sentinel, Microsoft Purview, Azure Policy, management groups
- DevOps: Azure Pipelines, Azure Repos, Azure Artifacts, Azure Boards, ARM templates and Bicep, Azure Monitor and Application Insights, Kusto Query Language

### Azure command line

- **Setup and context**
  - `az login` interactively, with `--use-device-code`, as a service principal or with `--identity` (managed identity); `az logout`
  - Subscriptions: `az account list`, `az account set --subscription`, `az account show`
  - Defaults: `az config set defaults.group=… defaults.location=…`; `az extension add` and `list`; `az upgrade`; `az version`
- **Command structure and output**
  - `az group subgroup command --parameters`; resource groups as the deployment and deletion unit (`az group create`, `az group delete --yes --no-wait`)
  - `--output` (`-o`) as `json`, `jsonc`, `yaml`, `table`, `tsv` or `none`; `--query` with JMESPath; `tsv` output into shell variables
  - `--only-show-errors`, `--debug`, `--verbose`; `az find` for examples; `az rest` for any ARM endpoint; `az resource list`, `show` and `delete --ids`
- **Common services**
  - Compute: `az vm create --image --size --admin-username --generate-ssh-keys --assign-identity`; `az vm open-port`; `az vm run-command invoke`; `az vm deallocate` versus `stop`; `az vmss create` and `scale`
  - Networking: `az network vnet create --subnet-name --subnet-prefixes`; `az network nsg create` and `nsg rule create`; `az network public-ip create`; `az network private-endpoint create`; `az network bastion ssh`
  - Storage: `az storage account create --sku Standard_LRS --kind StorageV2`; `az storage container create --auth-mode login`; `az storage blob upload`, `upload-batch`, `download` and `list`; `az storage blob generate-sas`
  - Containers: `az acr create`, `az acr login`, `az acr build`; `az aks create --enable-managed-identity --enable-oidc-issuer --enable-workload-identity --node-count`; `az aks get-credentials`; `az aks nodepool add`; `az aks upgrade`; `az containerapp up` and `create`
  - App platforms: `az webapp up`; `az webapp deployment slot create` and `swap`; `az functionapp create`; `az webapp log tail`
  - Identity and access: `az ad sp create-for-rbac`; `az ad app federated-credential create` for workload identity federation from CI; `az identity create`; `az role assignment create --assignee --role --scope`; `az role definition create`
  - Key Vault: `az keyvault create --enable-rbac-authorization`; `az keyvault secret set` and `show`; `az keyvault key create`
  - Deployments: `az deployment group create --template-file main.bicep --parameters`; `az deployment group what-if`; `az deployment sub create` for subscription scope; `az bicep build`; `az policy assignment create`
  - Data: `az sql server create` and `az sql db create`; `az cosmosdb create`
  - Monitoring: `az monitor log-analytics query --workspace --analytics-query` with Kusto; `az monitor metrics alert create`; `az monitor activity-log list`

### AWS and Azure — what differs at depth

- **Networks**: AWS VPCs and Azure VNets are regional, where a Google Cloud VPC is global; AWS subnets live in one Availability Zone while Azure subnets span the zones of a region; regions are joined by peering or a hub (Transit Gateway, Virtual WAN)
- **AWS IAM evaluation**: an explicit deny anywhere wins; an action needs an allow from an identity-based or resource-based policy; service control policies, permission boundaries and session policies only cap what can be allowed; roles are assumed through STS, and cross-account access needs both accounts to agree
- **Azure identity**: Entra ID roles govern the directory, Azure RBAC governs resources at management-group, subscription, resource-group or resource scope and is inherited downward; deny assignments; system- and user-assigned managed identities
- **Key-value and document stores**: DynamoDB partition and sort keys, on-demand versus provisioned read and write capacity, eventually consistent global secondary indexes, single-table design; Cosmos DB request units, partition keys and logical-partition limits, and five consistency levels (strong, bounded staleness, session, consistent prefix, eventual)
- **Object storage**: S3 strong read-after-write consistency, storage classes and lifecycle rules, bucket policies and Block Public Access; Azure storage accounts with LRS, ZRS, GRS and GZRS redundancy and hot, cool, cold and archive tiers
- **Functions**: Lambda execution-environment reuse and cold starts, reserved and provisioned concurrency, the 15-minute limit, event source mappings; Azure Functions hosting plans and Durable Functions orchestrations
- **Governance**: AWS Organizations with Control Tower landing zones, service control policies and resource control policies; Azure management groups, Azure Policy effects (deny, audit, modify, deployIfNotExists) and Cloud Adoption Framework landing zones
- **Commitments and discounts**: AWS Savings Plans, Reserved Instances and Spot; Azure reservations, savings plans, Spot VMs and Hybrid Benefit

### Cross-provider concept map

- Virtual machines: Compute Engine · EC2 · Virtual Machines
- Managed Kubernetes: GKE · EKS · AKS
- Serverless containers: Cloud Run · App Runner and Fargate · Container Apps
- Functions: Cloud Run functions · Lambda · Azure Functions
- PaaS hosting: App Engine · Elastic Beanstalk · App Service
- Object storage: Cloud Storage · S3 · Blob Storage
- Block storage: Persistent Disk · EBS · Managed Disks
- Managed relational: Cloud SQL · RDS · Azure SQL Database
- Globally distributed database: Spanner · Aurora Global and DynamoDB · Cosmos DB
- Wide-column: Bigtable · DynamoDB and Keyspaces · Cosmos DB for Cassandra
- Document: Firestore · DynamoDB · Cosmos DB
- In-memory cache: Memorystore · ElastiCache · Azure Cache for Redis
- Warehouse: BigQuery · Redshift · Synapse Analytics
- Messaging: Pub/Sub · SNS and SQS · Service Bus and Event Grid
- Stream and batch processing: Dataflow · Kinesis and Glue · Stream Analytics
- Managed Spark and Hadoop: Dataproc · EMR · HDInsight
- Pipeline orchestration: Cloud Composer · MWAA · Data Factory
- BI: Looker · QuickSight · Power BI
- Virtual network: VPC · VPC · VNet
- Load balancing: Cloud Load Balancing · ELB · Load Balancer and Application Gateway
- CDN: Cloud CDN · CloudFront · Azure CDN and Front Door
- DNS: Cloud DNS · Route 53 · Azure DNS
- Hybrid connectivity: Cloud Interconnect and VPN · Direct Connect and VPN · ExpressRoute and VPN Gateway
- Identity and access: Cloud IAM · AWS IAM · Entra ID and Azure RBAC
- Keys: Cloud KMS · AWS KMS · Key Vault
- Secrets: Secret Manager · Secrets Manager · Key Vault
- WAF and DDoS: Cloud Armor · AWS WAF and Shield · Azure WAF and DDoS Protection
- Container registry: Artifact Registry · ECR · Azure Container Registry
- CI build: Cloud Build · CodeBuild · Azure Pipelines
- CD and release: Cloud Deploy · CodePipeline and CodeDeploy · Azure Pipelines releases
- Native IaC: Infrastructure Manager and Config Connector · CloudFormation and CDK · ARM and Bicep
- Metrics: Cloud Monitoring · CloudWatch · Azure Monitor
- Logs: Cloud Logging · CloudWatch Logs · Azure Monitor Logs
- Tracing: Cloud Trace · X-Ray · Application Insights
- ML platform: Gemini Enterprise Agent Platform · SageMaker · Azure Machine Learning
- Foundation models: Model Garden and Gemini · Bedrock · Azure AI Foundry
- Organization hierarchy: organization → folder → project · organization → OU → account · management group → subscription → resource group
- Organization-wide policy: Organization Policy · service control policies · Azure Policy
- SIEM and SecOps: Google SecOps · Security Hub and GuardDuty · Microsoft Sentinel and Defender

### Certifications — Google Cloud

- **Professional Cloud Architect**: designing and planning a cloud solution architecture; managing and provisioning the infrastructure; designing for security and compliance; analyzing and optimizing technical and business processes; managing implementation; ensuring solution and operations excellence
  - Case studies: Altostrat Media, Cymbal Retail, EHR Healthcare, KnightMotives Automotive
  - Migration planning: the six Rs mapped to landings; Migrate to Virtual Machines; Migration Center discovery, dependency mapping and wave planning; licence impact; Database Migration Service, Datastream, Storage Transfer Service, Transfer Appliance; wave-zero connectivity; cutover with a written rollback
- **Professional Machine Learning Engineer**: architecting low-code AI solutions; collaborating across teams to manage data and models; scaling prototypes into ML models; serving and scaling models; automating and orchestrating ML pipelines; monitoring AI solutions
- **Professional Data Engineer**: designing data processing systems; ingesting and processing data; storing data; preparing and using data for analysis; maintaining and automating data workloads
- **Professional Cloud Developer**: designing scalable, secure, reliable cloud-native applications; building and testing; configuring for deployment; integrating with Google Cloud services; generative AI APIs and AI coding assistants
- **Professional Cloud DevOps Engineer**: bootstrapping and maintaining an organization; applying SRE practices; building CI/CD pipelines (including for infrastructure and ML workloads); observability and troubleshooting; optimizing performance and cost
- **Professional Cloud Security Engineer**: configuring access; securing communications and boundary protection; data protection; managing operations; supporting compliance requirements
- **Professional Cloud Network Engineer**: designing and planning VPC networks; implementing VPCs; configuring managed network services; hybrid and multicloud interconnectivity; managing, monitoring and troubleshooting; network security (Cloud NGFW, Secure Web Proxy, VPC Service Controls, Cloud Armor)
- **Professional Cloud Database Engineer**: designing scalable, highly available database solutions; managing multi-database solutions; migrating data solutions; deploying databases on Google Cloud
- **Professional Security Operations Engineer**: platform operations; data management; threat hunting; detection engineering; incident response; observability
- **Professional Agentic Architect**: building agents with low-code tools; using coding agents for application development (MCP servers, skills, sandboxes); developing custom agents (model selection, ADK, sessions and memory, RAG and vector retrieval, agent permissions, MCP and A2A orchestration, multi-agent handoffs); evaluating and deploying agentic workflows; securing and governing agentic workflows (OAuth 2.0 tool calls, principal access boundaries)

### Certifications — AWS

- **Solutions Architect – Professional (SAP-C03)**: cloud-native architecture design and implementation; security, compliance and governance; cost-optimized architecture design; resilience, migration and business continuity; operational excellence and automation
- **Solutions Architect – Professional (SAP-C02)**: design for organizational complexity; design for new solutions; continuous improvement for existing solutions; accelerate workload migration and modernization
- **DevOps Engineer – Professional (DOP-C02)**: SDLC automation; configuration management and IaC; resilient cloud solutions; monitoring and logging; incident and event response; security and compliance
- **Generative AI Developer – Professional (AIP-C01)**: foundation model integration, data management and compliance; implementation and integration; AI safety, security and governance; operational efficiency and optimization; testing, validation and troubleshooting
- **Security – Specialty (SCS-C03)**: detection; incident response; infrastructure security; identity and access management; data protection; security foundations and governance
- **Advanced Networking – Specialty (ANS-C01)**: network design; network implementation; network management and operation; network security, compliance and governance

### Certifications — Microsoft Azure

- **Azure Administrator (AZ-104)**: identities and governance; storage; compute; virtual networking; monitoring and maintenance
- **Azure Solutions Architect Expert (AZ-305)**: identity, governance and monitoring solutions; data storage solutions; business continuity solutions; infrastructure solutions (compute, application architecture, migrations, networking)
- **DevOps Engineer Expert (AZ-400)**: processes and communications; source control strategy; build and release pipelines (packages, testing, pipelines, deployments, IaC); security and compliance plans; instrumentation strategy
- **Cybersecurity Architect Expert (SC-100)**: aligning with security best practices (ransomware resiliency, MCRA, MCSB, Zero Trust, CAF and WAF); security operations, identity and compliance; infrastructure security (posture management, endpoints, SaaS/PaaS/IaaS, Security Service Edge); application and data security (Microsoft 365, applications, data, AI workloads)
- Expert-level prerequisites: AZ-305 requires the Azure Administrator Associate; AZ-400 requires AZ-104 or AZ-204; SC-100 requires a security associate certification

### Certifications — Anthropic

- **Claude Certified Developer – Foundations (CCDV-F)**: applications and integration; model selection and optimization; agents and workflows; prompt and context engineering; tools and MCP; security and safety; Claude Code; evaluation, testing and debugging

### Exercises

- The four Professional Cloud Architect case studies, each designed with a one-line defence of every trade-off
- A zero-cost build on always-free services (Compute Engine, Cloud Run, Cloud Run functions, Cloud Storage, Firestore, Pub/Sub), provisioned entirely with `gcloud` in an idempotent shell script and torn down by the same script
- A private-IP Cloud SQL instance reached from Cloud Run with a connection budget
- Spanner, Bigtable and Firestore key designs with hotspot detection, run against the local emulators first
- A global Application Load Balancer with Cloud CDN, Cloud Armor and IAP in front of a serverless backend, built resource by resource from the command line, then expressed in Terraform
- IAP and Identity Platform in front of an admin console
- Workload Identity Federation from CI with negative tests
- A VPC Service Controls perimeter and organization policies, planned in Terraform
- A store-selection table across the system-design problems, with a managed product per component
- The same three-tier service deployed with `gcloud`, the AWS CLI and the Azure CLI, comparing identity, networking and output querying
- Multi-account AWS and multi-subscription Azure landing zones planned in Terraform
- An inventory and cost report built from `--format`, `--filter` and `--query` output piped into `jq`
- **Reasoning drills**
  - Choose a managed service for each requirement from the constraints alone, then check the provider's limits and quotas
  - Estimate quota, cost and latency for a multi-region design before building it
  - Translate a design across Google Cloud, AWS and Azure and name what does not map cleanly
  - Diagnose an IAM denial from the policy alone, then confirm it with the troubleshooter

## Published ML System-Design Case Studies

**Prerequisites:** the case-study method; leakage and point-in-time correctness; the applied problem families (recommendation, search and ads, forecasting, fraud, language, vision, speech, marketing, availability, ML platforms); evaluation metrics and online experiments; MLOps serving and monitoring.

Each entry names the company, the problem and the year, then summarizes the data, model, serving approach and outcome, so it can be read without opening the source. The source article follows, with an archived copy where the original may move.

### Recommend / personalize / feed

- **Walmart — Recommend complementary items (2023)** — Complete-the-look outfits built around the item being viewed: complementary-item candidates (co-purchase and co-view) are filtered by age, gender, season and a blocklist, assembled into looks from product-type templates, matched for visual style, ranked, then expanded to variants; impressions, clicks and add-to-carts feed back into the model. Source: [article](https://medium.com/walmartglobaltech/personalized-complete-the-look-model-ea093aba0b73)
- **Swiggy — Recommend items to order (2023)** — Easing choice overload for undecided food customers: instead of endless restaurant and menu scrolling, the app recommends a small set of ready-made carts (dishes from one restaurant) built from order history, with embeddings, nearest-neighbour retrieval and bandits planned next. Source: [article](https://bytes.swiggy.com/building-a-mind-reader-at-swiggy-using-data-science-5a5c38aa6c17) ([archived copy](https://web.archive.org/web/2024/https://bytes.swiggy.com/building-a-mind-reader-at-swiggy-using-data-science-5a5c38aa6c17))
- **Lyft — Recommend content in app (2023)** — Ride-mode recommendation in the request flow: models choose which 3–4 modes appear above the fold and which is preselected, tackling choice overload, cold start for new modes and shifting business goals, with reinforcement learning planned. Source: [article](https://eng.lyft.com/the-recommendation-system-at-lyft-67bc9dcc1793)
- **Etsy — Recommend relevant marketplace items (2023)** — One multi-task canonical ranker for hundreds of recommendation modules: rather than a ranker per module, a shared model is trained on engagement and purchase objectives over contextual and item features after candidate selection, and launched through experiments. Source: [article](https://www.etsy.com/uk/codeascraft/how-we-built-a-multi-task-canonical-ranker-for-recommendations-at-etsy)
- **Airbnb — Personalized listing search (2023)** — The pairwise listing ranker learned 'cheaper is better' and so filled each page with near-identical listings; the fix scores each next slot by its similarity to listings already placed, so the page as a whole is diversified rather than each listing ranked alone. Source: [article](https://medium.com/airbnb-engineering/learning-to-rank-diversely-add6b1929621)
- **Twitter — Recommend interesting tweets (2023)** — The open-sourced home-timeline recommender: about 500 million daily posts pass through candidate sources (in-network, and out-of-network through the social graph and embedding spaces), a neural ranker, then heuristics, filters and mixing before serving. Source: [article](https://blog.twitter.com/engineering/en_us/topics/open-source/2023/twitter-recommendation-algorithm) ([archived copy](https://web.archive.org/web/2024/https://blog.twitter.com/engineering/en_us/topics/open-source/2023/twitter-recommendation-algorithm))
- **LinkedIn — Personalize the homepage feed (2023)** — Feed ranker grown to sparse ID embeddings for members, hashtags and posts (hundreds of millions of parameters, billions of daily records), trained with model parallelism and corrected for position by inverse propensity scoring; moved to in-memory serving so a 500× larger model kept its latency, with an engagement gain. Source: [article](https://www.linkedin.com/blog/engineering/feed/enhancing-homepage-feed-relevance-by-harnessing-the-power-of-lar)
- **Netflix — Personalize video clips (2023)** — Personalised sizzle reels: clips from a pre-built master asset are chosen per member and stitched at playback by timecode, with work on player delivery; editors produce many variants for far less time and cost than hand-made reels. Source: [article](https://netflixtechblog.com/the-next-step-in-personalization-dynamic-sizzles-4dc4ce2011ef)
- **Instacart — Personalize user experience by recommending relevant products (2023)** — Contextual bandits for search ranking and retrieval with a huge action space: actions are described by embedded features (such as average score and price of the top items), and trained policies are checked by counterfactual off-policy evaluation before any live test. Source: [article](https://tech.instacart.com/using-contextual-bandit-models-in-large-action-spaces-at-instacart-cb7ab4d8fa4f)
- **Pinterest — Recommend similar visual content (2023)** — Training foundations for a related-items ranker: hybrid logging of features at serving time, a slice of randomised traffic for unbiased data, revised negative sampling, and an automatic retraining framework that validates each refreshed model by offline replay before it ships. Source: [article](https://medium.com/pinterest-engineering/training-foundation-improvements-for-closeup-recommendation-ranker-67d90603426e)
- **Spotify — Recommend new complementary music (2023)** — A student project on the public million-playlist data: a graph neural network (LightGCN) over the playlist–track graph learns embeddings, trained with a ranking loss on sampled negatives and scored by recall at K. Source: [article](https://medium.com/stanford-cs224w/spotify-track-neural-recommender-system-51d266e31e16)
- **Dailymotion — Recommend diversified video content (2022, 2023)** — A vertical-video home feed that deliberately shows opposing views: videos are embedded from their text, a vector database (Qdrant) returns nearest neighbours as candidates, and a re-ranker mixes in content expressing other opinions. A mobile video feed rebuilt quickly: several candidate generators (fresh, top-performing, interest-based, exploration of new content) are combined by a multi-armed-bandit ranker so users always see something new. Source: [article](https://medium.com/dailymotion/reinvent-your-recommender-system-using-vector-database-and-opinion-mining-a4fadf97d020) · [article](https://medium.com/dailymotion/optimizing-video-feed-recommendations-with-diversity-machine-learning-first-steps-4cf9abdbbffd)
- **New York Times — Recommend recipes to readers (2023)** — Personalised recipe recommendation beside editorial curation: each carousel draws an eligible content pool (curated, or queried by rules), then algorithms such as collaborative filtering and content-based models rank recipes from past engagement. Source: [article](https://open.nytimes.com/how-the-new-york-times-cooking-team-makes-personalized-recipe-recommendations-7b86df9b22ec) ([archived copy](https://web.archive.org/web/2024/https://open.nytimes.com/how-the-new-york-times-cooking-team-makes-personalized-recipe-recommendations-7b86df9b22ec))
- **Expedia — Suggest diverse travel recommendations (2023)** — Diversity in travel recommendations: a diversity measure is defined beside NDCG, and re-ranking by embedding clusters or by neighbourhood cosine distance spreads results across price points and property types, shown on a public research dataset. Source: [article](https://medium.com/expedia-group-tech/generating-diverse-travel-recommendations-76688f49c812)
- **Stitch Fix — Personalize styling recommendations (2023)** — Multi-GPU data-parallel training (PyTorch DDP) of the client time-series recommender: training time fell to 0.55× of one GPU, with hyperparameters retuned to hold model quality. Source: [article](https://multithreaded.stitchfix.com/blog/2023/06/08/distributed-model-training/)
- **Netflix — Generate content recommendations for users (2023)** — Consolidating separate models for notifications, related items, search and category exploration into one multi-task model: after use-case-specific label preparation the pipeline is shared, which improved quality and cut maintenance and technical debt. Source: [article](https://netflixtechblog.medium.com/lessons-learnt-from-consolidating-ml-models-in-a-large-scale-recommendation-system-870c5ea5eb4a)
- **Delivery Hero — Recommend restaurants, including for new customers (2023)** — Personalised restaurant models for returning customers: explicit feedback (ratings) is rare, so implicit signals (clicks, orders) drive the recommender, with the usual trade-offs of implicit feedback. Ranking restaurants for new users: with no personal history, scores come from cuisine, budget, time of day and location signals plus collaborative filtering from similar users, so first sessions are still tailored. Source: [article](https://tech.deliveryhero.com/dont-worry-we-got-you-personalised-model-2/) ([archived copy](https://web.archive.org/web/2024/https://tech.deliveryhero.com/dont-worry-we-got-you-personalised-model-2/)) · [article](https://tech.deliveryhero.com/personalisation-delivery-hero-ranking-restaurants-for-new-users/) ([archived copy](https://web.archive.org/web/2024/https://tech.deliveryhero.com/personalisation-delivery-hero-ranking-restaurants-for-new-users/))
- **Salesforce — Recommend apps in the marketplace (2023)** — Enterprise app recommendation made diverse and explainable: denoising autoencoder recommenders are paired with separate explanation models, so each recommended app comes with a focused reason. Source: [article](https://blog.salesforceairesearch.com/diversity-explainability-enterprise-app-recommendation-systems/) ([archived copy](https://web.archive.org/web/2024/https://blog.salesforceairesearch.com/diversity-explainability-enterprise-app-recommendation-systems/))
- **eBay — Recommend relevant e-commerce items (2022)** — Personalised recommendations from click history: a two-tower model embeds users and items, approximate nearest-neighbour search (HNSW, ScaNN) retrieves candidates, and serving moved from offline batch to near-real-time streaming (Kafka, Flink, Triton). Source: [article](https://innovation.ebayinc.com/stories/building-a-deep-learning-based-retrieval-system-for-personalized-recommendations/)
- **DoorDash — Recommend substitute items (2022)** — Substitution recommendations for out-of-stock grocery items, in three phases: an unsupervised similarity approach, then binary classification with LightGBM on accepted substitutions, then a deep recommendation model, each measured by acceptance and customer impact. Source: [article](https://careersatdoordash.com/blog/evolving-doordashs-substitution-recommendations-algorithm/)
- **Pinterest — Personalize homepage contents (2022)** — TransAct: a transformer encoder over each user's most recent real-time actions joins the long-term user embedding in the home-feed ranker; the post covers engagement decay as the model ages and serving a large model at full scale, with gains offline, in A/B tests and in production. Source: [article](https://medium.com/pinterest-engineering/how-pinterest-leverages-realtime-user-actions-in-recommendation-to-boost-homefeed-engagement-volume-165ae2e8cde8)
- **Expedia — Categorize customer feedback (2022)** — Routing thousands of daily customer messages to teams with no labelled data: after supervised and synonym attempts failed, pretrained word embeddings place each message in the nearest topic bucket of a multi-label taxonomy. Source: [article](https://medium.com/expedia-group-tech/categorising-customer-feedback-using-unsupervised-learning-8608c1e62d48)
- **eBay — Recommend products and content (2022)** — Similar-item ads on the item page ranked by a gradient-boosted tree with a pairwise loss, whose labels weight clicks, watchlist adds, cart adds, offers and purchases by how often each converts; A/B test: purchases +2.97%, ad revenue +2.66% on mobile. Source: [article](https://innovation.ebayinc.com/stories/multi-relevance-ranking-model-for-similar-item-recommendation/)
- **Yelp — Personalize recommendations (2022)** — User–business recommendations moved beyond matrix factorisation (ALS): collaborative scores plus content features (categories, ratings, text similarity) ranked by XGBoost optimising nDCG on implicit labels graded by interaction strength; nDCG +5–14% and twice the coverage for tail users. Source: [article](https://engineeringblog.yelp.com/2022/04/beyond-matrix-factorization-using-hybrid-features-for-user-business-recommendations.html)
- **Gousto — Recommend food items and recipes (2021, 2022)** — Cold start for customers after their first box: the recommender changed how a new customer is represented (from the few recipes they chose) and made recommendations synchronous, so new customers see personalised recipes at once. A recipe-kit company's recommender family: one model chooses the menu showcased to prospective customers, one serves new customers, and one serves established customers, each matched to a stage of the customer journey. Source: [article](https://medium.com/gousto-engineering-techbrunch/gousto-r-series-vol-2-tackling-the-cold-start-problem-in-recipe-recommendation-engine-af92a434805f) · [article](https://medium.com/gousto-engineering-techbrunch/gousto-r-series-vol-1-three-tales-of-the-rouxcommender-family-a3555a93edea)
- **Meta — Personalize daily digest notifications (2022)** — Daily-digest notifications filtered by a neural uplift model trained on randomised experiments, predicting each send's incremental engagement; online, a dynamically computed quantile threshold holds a target send rate, cutting volume without losing engagement. Source: [article](https://engineering.fb.com/2022/10/31/ml-applications/instagram-notification-management-machine-learning/)
- **Instacart — Recommend relevant food items (2022)** — Research on recommending to a user who is still learning their own preferences: an explore-then-eliminate bandit (best-arm identification with confidence bounds) that drops rejected items; a theoretical result rather than a deployed system. Source: [article](https://company.instacart.com/tech-innovation/personalizing-recommendations-for-a-learning-user)
- **DoorDash — Personalize recommendations on homepage (2022)** — Home-page recommendation that balances exploitation and exploration: stores, dishes and carousels are compared on one calibrated scale, and an upper-confidence-bound style exploration term gives new content exposure. Source: [article](https://careersatdoordash.com/blog/homepage-recommendation-with-exploitation-and-exploration/)
- **Autotrader — Personalize automotive search results (2022)** — Real-time personalisation of vehicle search results: a real-time customer data platform builds profiles from browsing behaviour, segments customers, and feeds the segments into search ranking, proven by A/B test and then monitored. Source: [article](https://engineering.autotrader.co.uk/2022/11/23/real-time-personalisation-of-search-results-with-auto-traders-customer-data-platform.html) ([archived copy](https://web.archive.org/web/2024/https://engineering.autotrader.co.uk/2022/11/23/real-time-personalisation-of-search-results-with-auto-traders-customer-data-platform.html))
- **Peloton — Recommend fitness training videos (2022)** — Choosing the model for a fitness platform's daily class picks: batch compute and cache, speed of development against model performance, a sequence model (LSTM) and its drawbacks, and the difficulty of generating test data and evaluating continuously. Source: [article](https://www.onepeloton.com/press/articles/how-we-built-machine-learning) ([archived copy](https://web.archive.org/web/2024/https://www.onepeloton.com/press/articles/how-we-built-machine-learning))
- **New York Times — Personalize paywall limits (2022)** — A dynamic paywall meter: instead of a fixed monthly article limit, a prescriptive model sets each reader's limit to trade subscriptions against engagement, back-tested on past data. Source: [article](https://open.nytimes.com/how-the-new-york-times-uses-machine-learning-to-make-its-paywall-smarter-e5771d5f46f8) ([archived copy](https://web.archive.org/web/2024/https://open.nytimes.com/how-the-new-york-times-uses-machine-learning-to-make-its-paywall-smarter-e5771d5f46f8))
- **Netflix — Recommend content to view (2022)** — Slate recommendation when the user has a finite time budget to choose: framed like a 0/1 knapsack and then as a Markov decision process, with value functions learned by reinforcement learning, compared on and off policy in a simulator by play rate. Source: [article](https://netflixtechblog.com/reinforcement-learning-for-budget-constrained-recommendations-6cbc5263a32a)
- **Stitch Fix — Recommend e-commerce items and inventory (2021, 2022)** — One client time-series model predicts purchase probability for every client–item pair across business lines and regions: timestamped client events pass through a temporally masked encoder with gated updates, scored by a dot product with item embeddings; gains in revenue, retention and satisfaction with less compute. Merchandise buyers get predictions of how items will perform per client segment from over 500 features (categories, images, fabric, text), visualised with UMAP; checked by simulating past buying decisions against actual performance. Source: [article](https://multithreaded.stitchfix.com/blog/2022/10/14/client-time-series-model/) · [article](https://multithreaded.stitchfix.com/blog/2021/05/12/algorithm-assisted-inventory-curation/)
- **Walmart — Curate e-commerce product recommendations (2022)** — Basket analysis for curated product bundles: propensity models over millions of in-store and online transactions find items bought together, scaled across every department to find cross-buying opportunities. Source: [article](https://medium.com/walmartglobaltech/scaling-product-recommendations-using-basket-analysis-part-1-8434d4f8756f)
- **Twitter — Recommend accounts to follow (2022)** — Who-to-follow candidate generation: dozens of narrow candidate sources (collaborative filtering, graph expansion) are replaced by a model-based retrieval stage that uses much more of the member's information before real-time ranking. Source: [article](https://blog.twitter.com/engineering/en_us/topics/insights/2022/model-based-candidate-generation-for-account-recommendations) ([archived copy](https://web.archive.org/web/2024/https://blog.twitter.com/engineering/en_us/topics/insights/2022/model-based-candidate-generation-for-account-recommendations))
- **Glassdoor — Recommend interesting posts to users (2022)** — Part 1 moves a community feed from global rankings to personalised ones: Doc2Vec on post text, a graph Doc2Vec and DeepWalk over user–post interactions, with users represented from their history and posts served by embedding similarity. Part 2 compares ways to embed posts for a professional community's feed: GloVe and BERT text embeddings, contrastive and Siamese-network embeddings, and graph convolutional embeddings, with offline results for each. Source: [part 1](https://medium.com/glassdoor-engineering/personalized-fishbowl-recommendations-with-learned-embeddings-part-1-6031abe84661) · [part 2](https://medium.com/glassdoor-engineering/personalized-fishbowl-recommendations-with-learned-embeddings-part-2-78a16b04d396)
- **LinkedIn — Deliver more relevant job recommendations (2022)** — Job recommendations gained learned activity features: 28 days of a member's applies, saves and dismissals are pooled into an embedding (averaging, CNN, LSTM and Transformer variants compared), recomputed daily; four A/B iterations raised applies by over 10% and confirmed hires by 5%. Source: [article](https://www.linkedin.com/blog/engineering/machine-learning/improving-job-matching-with-machine-learned-activity-features-)
- **Cookidoo — Personalize recipe recommendations (2022)** — Recipe recommendations for 5 million users over 80,000 recipes by matrix factorisation (LightFM) on implicit signals (cooked, listed, viewed), one model per language; judged offline by nDCG, precision@k and MRR, then by A/B test. Source: [article](https://www.alexanderthamm.com/en/blog/building-a-recipe-recommender-system-for-the-thermomix-on-cookidoo/)
- **Pinterest — Recommend bids for advertizers (2021)** — Recommendations to advertisers: suggested bids, budgets and wider targeting, each generated from auction and campaign data, then ordered by a ranker that predicts which recommendation an advertiser will adopt. Source: [article](https://medium.com/pinterest-engineering/advertiser-recommendation-systems-at-pinterest-ccb255fbde20)
- **OLX — Recommend e-commerce items (2021)** — Item2Vec for classified-ads recommendations: embeddings learned from sequences of items viewed together (word2vec style) give item-to-item similar-ad recommendations, and user-to-item by treating a user's history as items. Source: [article](https://tech.olx.com/item2vec-neural-item-embeddings-to-enhance-recommendations-1fd948a6f293) ([archived copy](https://web.archive.org/web/2024/https://tech.olx.com/item2vec-neural-item-embeddings-to-enhance-recommendations-1fd948a6f293))
- **Spotify — Personalize homepage content (podcasts, playlist, music) (2021)** — Home-page shelves (podcasts, shortcuts, playlists for new listeners) use candidate generation and ranking, served in real time with features logged at serving time; weekly Kubeflow retraining, and feature drift caught by data validation using a Chebyshev distance. The same models' evaluation: nDCG@k and diversity metrics against heuristic baselines, then A/B tests; a pipeline promotes a weekly retrained model only when it beats configured thresholds. Source: [part 1](https://engineering.atspotify.com/2021/11/the-rise-and-lessons-learned-of-ml-models-to-personalize-content-on-home-part-i) · [part 2](https://engineering.atspotify.com/2021/11/the-rise-and-lessons-learned-of-ml-models-to-personalize-content-on-home-part-ii)
- **Stitch Fix — Recommend looks (2021)** — Recommendations from inspiration images: objects detected in community photos are matched to catalogue anchor items, images scored for the client, and candidates ranked by a weighted multi-objective blend of similarity and personalisation with diversity-aware selection. Source: [article](https://multithreaded.stitchfix.com/blog/2021/08/13/stitching-together-spaces-for-query-based-recommendations/)
- **Walmart — Recommend learning content (2021)** — Recommending task guides to store associates: candidates from collaborative filtering and from content similarity (TextRank keywords), then a wide-and-deep ranker (DeepFM) over skip-gram content embeddings. Source: [article](https://medium.com/walmartglobaltech/mozrt-a-deep-learning-recommendation-system-empowering-walmart-store-associates-with-a-5d42c08d88da)
- **New York Times — Recommend content to read (2021)** — Matching articles to reader-chosen interests: editor tags and topic modelling gave way to classifiers for explicit interests, with human-in-the-loop workflows where the models misclassify. Source: [article](https://open.nytimes.com/we-recommend-articles-with-a-little-help-from-our-friends-machine-learning-and-reader-input-e17e85d6cf04) ([archived copy](https://web.archive.org/web/2024/https://open.nytimes.com/we-recommend-articles-with-a-little-help-from-our-friends-machine-learning-and-reader-input-e17e85d6cf04))
- **PayPal — Recommend financial products (2021)** — Choosing business actions with a classifier trained on a custom loss that carries each action's cost and benefit; compared with the same network trained on plain cross-entropy, it chose actions with higher expected value. Source: [article](https://medium.com/paypal-tech/a-deep-learning-based-approach-to-optimizing-actions-e1ae9d1df152)
- **Scribd — Recommend content to read (2021)** — Transformer-based user and item embeddings stored in Elasticsearch; retrieval by dot product with faceted filters applied at query time; an A/B test with over a million users raised clicks and reading. Source: [article](https://tech.scribd.com/blog/2021/embedding-based-retrieval-scribd.html)
- **Wayfair — Recommend furniture items (2021)** — Sequential recommendation from browsing history with a Transformer (item and position embeddings, binary cross-entropy); recall of the top 6 rose 67% over the matrix-factorisation baseline. Source: [article](https://www.aboutwayfair.com/careers/tech-blog/mars-transformer-networks-for-sequential-recommendation)
- **Zillow — Recommend similar homes (2021)** — Adding listing-description text to home recommendations: a scalable system generates text embeddings for every listing, and adding them to the similar-homes recommender lifted offline retrieval metrics. Source: [article](https://www.zillow.com/tech/improve-quality-listing-text/) ([archived copy](https://web.archive.org/web/2024/https://www.zillow.com/tech/improve-quality-listing-text/))
- **Expedia — Personalize travel search results (2021)** — Personalised hotel ranking for business travellers: features from a traveller's and their company's past bookings and preferred hotels feed a learning-to-rank model, measured by where the booked hotel lands in the list. Source: [article](https://medium.com/expedia-group-tech/personalized-ranking-model-for-lodging-5be43ae975fe)
- **Meta — Personalize the newsfeed content (2021)** — Feed ranking for over 2 billion users: multitask neural networks predict several engagement probabilities per post, which a weighted linear formula combines into one score aimed at long-term value, scored in real time over thousands of candidates. Source: [article](https://engineering.fb.com/2021/01/26/ml-applications/news-feed-ranking/)
- **LinkedIn — Serve personalized learning recommendations (2020)** — Course recommendations for 23 million subscribers over 16,000 courses: a response-prediction model on profile and course features and a collaborative-filtering model, blended online by fixed probabilities, labels from historical engagement. Adding course-watch behaviour, filtered by a watch-time threshold to drop noise, to neural collaborative filtering and GLMix mixed models raised engagement. Source: [part 1](https://www.linkedin.com/blog/engineering/learning/course-recommendations-ai-part-one) · [part 2](https://www.linkedin.com/blog/engineering/learning/course-recommendations-ai-part-two)
- **Etsy — Personalize e-commerce search (2020)** — Personalised search ranking over 80 million handmade listings: user representations built from recent interactions (clicks, favourites, purchases) and contextual features re-order relevant results to each shopper's taste without hurting overall performance. Source: [article](https://www.etsy.com/codeascraft/bringing-personalized-search-to-etsy/)
- **Zynga — Personalize push notification timing (2020)** — Push-notification timing for a mobile game chosen by an offline deep Q-network trained daily on state–action–reward histories (TF-Agents); click rate +10% relative. Source: [article](https://towardsdatascience.com/deep-reinforcement-learning-in-production-part-2-personalizing-user-notifications-812a68ce2355/)
- **Spotify — Recommend shortcuts for homepage (2020)** — Shortcuts, six familiar items atop Home, picked from 90 days of listening by a neural model over sequential listening data; +26.7% relative over decayed-count heuristics offline, served to hundreds of millions through batch pipelines. Source: [article](https://engineering.atspotify.com/2020/04/reach-for-the-top-how-spotify-built-shortcuts-in-just-six-months)
- **Wayfair — Recommend complementary products (2020)** — Complementary furniture recommendations from images: a Siamese ResNet-50 trained with a triplet loss embeds products so that pieces that match in style sit close together; labels come from a style model, artist-curated 3D scenes and co-purchases; nearest-neighbour search serves the complements. Source: [article](https://www.aboutwayfair.com/tech-innovation/the-visual-complements-model-vics-complementary-product-recommendations-from-visual-cues)
- **Airbnb — Recommend marketplace items (2019)** — Ranking for a new activities marketplace grown in stages: a small-data baseline, then personalisation from booked stays and clicks, then online scoring, then business rules; each stage was proven in an A/B test on bookings. Source: [article](https://medium.com/airbnb-engineering/machine-learning-powered-search-ranking-of-airbnb-experiences-110b4b1a0789)
- **Gojek — Personalize search results (2019)** — Personalised restaurant search: rather than distance order alone, restaurants are ranked by each user's affinity from order history, cutting scrolling and indecision. Source: [article](https://www.gojek.io/blog/the-secret-sauce-behind-search-personalisation) ([archived copy](https://web.archive.org/web/2024/https://www.gojek.io/blog/the-secret-sauce-behind-search-personalisation))
- **Lyft — Personalize marketing offers (2018)** — Personalised coupons framed as the right question (who would ride more because of a coupon): models predict the incremental effect per rider, and an optimiser allocates coupons under budget, allowing for uncertainty in the predictions. Source: [article](https://eng.lyft.com/empowering-personalized-marketing-with-machine-learning-fd36e6bdeca6)

### Search / rank / ads

- **Pinterest — Prevent advertiser churn (2023)** — Proactive churn prevention for small advertisers: a model predicts churn weeks ahead from spend and performance features; sales teams contacted the high-risk accounts in an experiment and retained more of them. Source: [article](https://medium.com/pinterest-engineering/an-ml-based-approach-to-proactive-advertiser-churn-prevention-3a7c0c335016)
- **Airbnb — Improve travel search experience (2022, 2023)** — Categories part 2: listing signals (text, images, reviews, and outside data such as satellite and points of interest) feed rule-based candidates; human reviewers label them, and those labels train classifiers for category membership, cover image and quality. Categories part 1: listings are grouped into themed categories by rules, human review and models trained on the reviewed labels, and two new ranking algorithms order the categories and the listings inside each. Source: [article](https://medium.com/airbnb-engineering/building-airbnb-categories-with-ml-human-in-the-loop-35b78a837725) · [article](https://medium.com/airbnb-engineering/building-airbnb-categories-with-ml-and-human-in-the-loop-e97988e70ebb)
- **Algolia — Suggest relevant search queries (2023)** — Query suggestions for search autocomplete built from logged click and conversion events into a dedicated suggestions index, with filters for inappropriate terms and a minimum-frequency threshold; no measured result given. Source: [article](https://www.algolia.com/blog/product/feature-spotlight-query-suggestions)
- **Netflix — In-video search (2023)** — In-video search for editors building trailers and promos: contrastive image–text models learn one embedding space for objects, scenes, emotions and actions, so editors can find moments across the catalogue by text query. Source: [article](https://netflixtechblog.com/building-in-video-search-936766f0017c)
- **Etsy — Show relevant ads (2023)** — Click-rate and post-click conversion prediction for sponsored search ads from short, variable-length sequences of recent user actions, encoded by a Transformer with visual and pretrained item representations; offline ROC-AUC +2.66% and +2.42%, shipped to all traffic in February 2023. Source: [article](https://arxiv.org/pdf/2302.01255)
- **Swiggy — Conversational and open-ended search (2023)** — Generative AI plans at a food and grocery app: neural search with an LLM adapted to a catalogue of 50 million+ items answers open-ended conversational queries, plus a dining-out assistant and LLM tools for restaurant partners. Source: [article](https://bytes.swiggy.com/swiggys-generative-ai-journey-a-peek-into-the-future-2193c7166d9a) ([archived copy](https://web.archive.org/web/2024/https://bytes.swiggy.com/swiggys-generative-ai-journey-a-peek-into-the-future-2193c7166d9a))
- **Etsy — Search by image (2023)** — Search by image: a multitask vision model trained on several classification objectives produces listing-image embeddings, and nearest-neighbour search over about 100 million listings returns visually similar items within a fraction of a second. Source: [article](https://www.etsy.com/codeascraft/from-image-classification-to-multitask-modeling-building-etsys-search-by-image-feature)
- **LinkedIn — Show relevant jobs in search (2023)** — Embedding-based retrieval at scale for job search and job recommendations: the infrastructure to generate, index and serve embeddings so searches match members to jobs by meaning, not only keywords. Source: [article](https://engineering.linkedin.com/blog/2023/how-linkedin-is-using-embeddings-to-up-its-match-game-for-job-se) ([archived copy](https://web.archive.org/web/2024/https://engineering.linkedin.com/blog/2023/how-linkedin-is-using-embeddings-to-up-its-match-game-for-job-se))
- **Instacart — Search food and grocery items (2022)** — A two-tower embedding model of queries and products trained on search impression logs, with data augmentation and multi-task learning; it lifts search relevance and supports semantic de-duplication for more diverse results (a published paper). Source: [article](https://tech.instacart.com/how-instacart-uses-embeddings-to-improve-search-relevance-e569839c3c36)
- **Spotify — Search for podcasts (2022)** — Semantic podcast-episode search: dense retrieval with a Transformer sentence encoder trained on query–episode pairs with in-batch and hard negatives, served by approximate nearest-neighbour search beside lexical search; A/B tests showed engagement gains. Source: [article](https://engineering.atspotify.com/2022/03/introducing-natural-language-search-for-podcast-episodes)
- **PayPal — Prioritize sales leads (2022)** — Sales pipeline prediction: a lightweight two-layer ensemble gives progressively updated win-probability scores as an opportunity moves through stages, not one static score. Source: [article](https://medium.com/paypal-tech/sales-pipeline-management-with-machine-learning-15398bab913b)
- **Trivago — Optimize accommodation ranking (2022)** — Hotel ranking exposes little-seen inventory by scoring items with a beta-binomial posterior whose tunable weight sets how much to explore; low-impression items were explored with no short-term revenue loss and advertisers' click shares stayed stable. Source: [article](https://tech.trivago.com/post/2022-11-04-explore-exploit-dilemma-in-ranking-model)
- **Expedia — Rank relevant travel deals (2022)** — Ranking home-page components with cascade bandits: the cascade click model treats a list as scanned top-down, and cascade linear Thompson sampling learns the order from click feedback while still exploring. Source: [article](https://medium.com/expedia-group-tech/how-to-optimise-rankings-with-cascade-bandits-5d92dfa0f16b)
- **LinkedIn — Improve post search functionality (2022)** — Post search rebuilt apart from the feed stack as layers: embedding-based retrieval, a first-pass ranker, a second-pass ranker and a diversity re-ranker, with crowdsourced relevance labels; click rate +6.2%, messages +21%, 62 ms faster on Android. Source: [article](https://www.linkedin.com/blog/engineering/search/improving-post-search-at-linkedin)
- **Snap — Rank relevant ads (2022)** — Ad ranking predicts conversion probabilities and ad utility for real-time auctions over millions of ads with multitask models (MMoE, PLE, Deep & Cross v2), calibrated by Platt scaling or isotonic regression, judged by normalised cross-entropy on future data. Source: [article](https://eng.snap.com/machine-learning-snap-ad-ranking)
- **Instacart — Autocomplete user searches in e-commerce (2022)** — Autocomplete for grocery search: suggestions come from past queries and the catalogue (for cold start), fuzzy matching handles typos (a small engagement gain), semantic de-duplication removes near-repeats, and an engagement model with multi-objective ranking orders the list. Source: [article](https://tech.instacart.com/how-instacart-uses-machine-learning-driven-autocomplete-to-help-people-fill-their-carts-9bc56d22bafb)
- **DoorDash — Search food and grocery items (2022)** — Expanding product search beyond food: new indexing and a federated search across verticals, better query and document understanding from an extended taxonomy, human-annotated labels to bootstrap new domains, and NLP to enrich queries. Source: [article](https://careersatdoordash.com/blog/3-changes-to-expand-doordashs-product-search/)
- **Faire — Rank e-commerce items (feature store) (2022)** — Part 2 of real-time ranking at a wholesale marketplace: the feature store combines batch-computed and real-time features, and a log-and-wait approach records served features for training (feature fidelity, plug-and-play models). Source: [article](https://craft.faire.com/real-time-ranking-at-faire-part-2-the-feature-store-3f1013d3fe5d) ([archived copy](https://web.archive.org/web/2024/https://craft.faire.com/real-time-ranking-at-faire-part-2-the-feature-store-3f1013d3fe5d))
- **LinkedIn — Predict ad click-through rate (2022)** — Ads click-rate model moved from GLMix to three towers: a deep tower for feature interactions, a wide tower on sparse IDs retrained hourly, and a shallow tower for calibration (with isotonic regression); click rate +8.5%. Source: [article](https://www.linkedin.com/blog/engineering/machine-learning/challenges-and-practical-lessons-from-building-a-deep-learning-b)
- **Etsy — Rank marketplace search results (2022)** — Moving second-pass search ranking from gradient-boosted trees (plateaued on hand-engineered features) to a unified deep model using embeddings and multi-modal inputs: a year of iteration on pipelines and serving before launch. Source: [article](https://www.etsy.com/uk/codeascraft/deep-learning-for-search-ranking-at-etsy)
- **Faire — Search and navigate marketplace items (2021)** — Rebuilding a wholesale marketplace's ranking infrastructure across search, category and recommendation surfaces: offline and online feature computation, training and real-time model serving. Source: [article](https://craft.faire.com/building-faires-new-marketplace-ranking-infrastructure-a53bf938aba0) ([archived copy](https://web.archive.org/web/2024/https://craft.faire.com/building-faires-new-marketplace-ranking-infrastructure-a53bf938aba0))
- **Dropbox — Search by image content (2021)** — Image search without captions: a classifier (EfficientNet on OpenImages) scores about 8,500 categories per image, queries map into the same category space through word vectors, and images rank by cosine similarity, stored sparsely (top 50 image and top 10 query categories) in an inverted index. Source: [article](https://dropbox.tech/machine-learning/how-image-search-works-at-dropbox)
- **Microsoft — Rank customer support cases (2021)** — Measuring support success beyond sparse and biased surveys: a model trained on survey responses predicts satisfaction for every case, and the predictions were back-tested before production use. Source: [article](https://medium.com/data-science-at-microsoft/ml-and-customer-support-part-1-using-machine-learning-to-enable-world-class-customer-support-c90b3b02f6a3)
- **Swiggy — Rank restaurants in search (2021)** — No readable copy was found; linked only. Source: [article](https://bytes.swiggy.com/learning-to-rank-restaurants-c6a69ba4b330)
- **Swiggy — Rank food dishes in search (2021)** — Dish search in two steps: retrieval (millions of dishes narrowed to hundreds, including a semantic model for misspelt and vague queries), then ranking that combines semantic, restaurant, popularity and distance–time models into a final score. Source: [article](https://bytes.swiggy.com/using-deep-learning-for-ranking-in-dish-search-4df2772dddce) ([archived copy](https://web.archive.org/web/2024/https://bytes.swiggy.com/using-deep-learning-for-ranking-in-dish-search-4df2772dddce))
- **Wayfair — Automate ads placement and bidding (2021)** — Search-ad bidding for millions of keywords and catalogue items on Google and Bing, moving from rules to models that predict each keyword's future return, with bandits and A/B tests to set bids for return on ad spend. Source: [article](https://www.aboutwayfair.com/careers/tech-blog/evolution-of-ads-bidding-at-wayfair)
- **Dailymotion — Target contextual advertising (2021)** — Contextual advertising without cookies: videos are classified into the industry ad-content taxonomy using text embeddings with cross-lingual transfer to new languages, plus visual models trained end to end. Source: [article](https://medium.com/dailymotion/how-deep-learning-can-boost-contextual-advertising-capabilities-c9ca7c8fc4e9)
- **Wayfair — Optimize digital ads (2021)** — A marketing platform scores customers with propensity and uplift models, applies decision rules or reinforcement learning to pick a treatment per channel, and feeds engagement back; the target is 60-day revenue and lifetime-value change, reported as return on ad spend. Source: [article](https://www.aboutwayfair.com/careers/tech-blog/building-scalable-and-performant-marketing-ml-systems-at-wayfair)
- **Airbnb — Rank travel search results (2020)** — Three lessons from a deep listing ranker: correct position bias in training, handle cold start for new listings by estimating their engagement, and diversify results rather than repeat similar listings. Source: [article](https://medium.com/airbnb-engineering/improving-deep-learning-for-ranking-stays-at-airbnb-959097638bde)
- **Wayfair — Improve search experience for new customers (2020)** — Product ranking by intrinsic appeal across 14 million items: a logistic model separates the effect of position from the product's own appeal, combining clicks, cart adds and purchases with empirical-Bayes priors (MAP estimate, Laplace approximation) and Thompson sampling to explore. Source: [article](https://www.aboutwayfair.com/tech-innovation/bayesian-product-ranking-at-wayfair)
- **Zillow — Rank homes to buy (2020)** — Guided search for homes: with about 50 filters hidden in menus, a model suggests a few personalised search-refinement buttons ranked by relevance to the shopper's context. Source: [article](https://www.zillow.com/tech/personalized-search-refinements/) ([archived copy](https://web.archive.org/web/2024/https://www.zillow.com/tech/personalized-search-refinements/))
- **DoorDash — Search for restaurants and dishes (2020)** — Better recall for ambiguous and concept searches: an out-of-the-box engine failed on queries naming a concept rather than a store, so the recall step was redesigned with query standardisation, item-level indexing and a base evaluation dataset. Source: [article](https://careersatdoordash.com/blog/understanding-search-intent-with-better-recall/)
- **Dropbox — Predict files users search for (2019)** — Suggested files on the home page ranked from activity signals (recency, frequency, access history), moving from frecency heuristics through an SVM to a neural learning-to-rank model trained on past file opens; judged by click rate and hit ratio. Source: [article](https://dropbox.tech/machine-learning/content-suggestions-machine-learning)
- **Gojek — Analyse the relevance of search results (2019)** — Using nDCG in practice for food search (over a million daily orders come through search): how relevance is labelled, measured and interpreted, and how it links to conversion and customer satisfaction. Source: [article](https://www.gojek.io/blog/is-this-what-you-were-looking-for) ([archived copy](https://web.archive.org/web/2024/https://www.gojek.io/blog/is-this-what-you-were-looking-for))
- **Airbnb — ML Powered search ranking (2019)** — The same article as M.1's “Airbnb — Recommend marketplace items (2019)”; its summary is there. Source: [article](https://medium.com/airbnb-engineering/machine-learning-powered-search-ranking-of-airbnb-experiences-110b4b1a0789)

### Forecast / ETA / demand

- **Uber — Forecast demand for airport rides (2023)** — Airport driver-queue wait times: gradient-boosted trees forecast demand, a simulation depletes the queue from each driver's position, and the wait is shown in the driver app as short, medium or long. Source: [article](https://www.uber.com/GB/en/blog/demand-and-etr-forecasting-at-airports/)
- **Wayfair — Predict delivery times (2023)** — End-to-end delivery-date promise from supplier lead times, distance, time features and supplier IDs, by gradient-boosted trees with quantile regression and recency weighting, served under 50 ms for 99.99% of requests; the gap between promised and actual days roughly halved at the same on-time rate. Source: [article](https://www.aboutwayfair.com/careers/tech-blog/delivery-date-prediction)
- **Zalando — Forecast demand in fashion e-commerce (2023)** — Demand forecasting for an online fashion catalogue that is large, irregular and bound by fixed inventory, with deep-learning models (a case study paper; only the abstract was readable). Source: [article](https://arxiv.org/abs/2305.14406)
- **DoorDash — Forecast order volumes and deliveries (2023)** — An ensemble forecasting system (stacking): several fast base learners are combined by an ensemble learner chosen with temporal k-fold cross-validation, balancing accuracy against compute cost and making the system modular. Source: [article](https://careersatdoordash.com/blog/how-doordash-built-an-ensemble-learning-model-for-time-series-forecasting/)
- **Expedia — Forecast flight prices (2023)** — Flight price forecasting trained on synthetic searches (automated queries with fixed parameters on chosen routes), which give steady, complete series; the trade-off is coverage of the routes not searched. Source: [article](https://medium.com/expedia-group-tech/using-synthetic-search-data-for-flights-price-forecasting-4cf3277afdaf)
- **DoorDash — Accurately forecast demand during holidays (2023)** — Holiday forecasting by cascade: tree models handle holidays poorly with little data, so a holiday-impact estimator first adjusts the series and the usual model forecasts the rest, feeding driver-mobilisation plans. Source: [article](https://careersatdoordash.com/blog/how-doordash-improves-holiday-predictions-via-cascade-ml-approach/)
- **Swiggy — Predict food delivery time (2023)** — Post-order ETA, part 1: four models for four legs of the order journey (order to assignment, first mile, wait at the restaurant, last mile) use real-time signals such as restaurant stress and driver location to update the estimate smoothly. Post-order ETA, part 2: the last-mile model, the evaluation metrics, and the move from gradient-boosted trees to neural networks for the leg estimates. The promised delivery time at checkout: too optimistic and customers are unhappy when late, too conservative and they don't order; the model must land in between, with a custom loss and handling of sparse cohorts to come. Source: [part 1](https://bytes.swiggy.com/how-ml-powers-when-is-my-order-coming-part-i-4ef24eae70da) ([archived copy](https://web.archive.org/web/2024/https://bytes.swiggy.com/how-ml-powers-when-is-my-order-coming-part-i-4ef24eae70da)) · [part 2](https://bytes.swiggy.com/how-ml-powers-when-is-my-order-coming-part-ii-eae83575e3a9) ([archived copy](https://web.archive.org/web/2024/https://bytes.swiggy.com/how-ml-powers-when-is-my-order-coming-part-ii-eae83575e3a9)) · [part 3](https://bytes.swiggy.com/predicting-food-delivery-time-at-cart-cda23a84ba63) ([archived copy](https://web.archive.org/web/2024/https://bytes.swiggy.com/predicting-food-delivery-time-at-cart-cda23a84ba63))
- **OLX — Predict order delivery time (2023)** — Delivery-time estimation for a classifieds marketplace: the baseline, success criteria, differences between sellers and carriers, batch against online prediction, and a CatBoost model. Source: [article](https://tech.olx.com/machine-learning-for-delivery-time-estimation-1-591c8df849a0) ([archived copy](https://web.archive.org/web/2024/https://tech.olx.com/machine-learning-for-delivery-time-estimation-1-591c8df849a0))
- **Grubhub — Forecast order volume (2021, 2022)** — Forecasting order volume for every half hour in every region (millions of timeslots daily) so courier shifts are neither short nor idle; the post covers running these forecasts at scale. An introduction to order-volume forecasting: from naive last-period guesses to models on historical volume plus predictors such as weekday and weather, forecasting half-hour demand per area. Source: [article](https://bytes.grubhub.com/forecasting-grubhub-order-volume-at-scale-a966c2f901d2) ([archived copy](https://web.archive.org/web/2024/https://bytes.grubhub.com/forecasting-grubhub-order-volume-at-scale-a966c2f901d2)) · [article](https://bytes.grubhub.com/i-see-tacos-in-your-future-order-volume-forecasting-at-grubhub-44d47ad08d5b) ([archived copy](https://web.archive.org/web/2024/https://bytes.grubhub.com/i-see-tacos-in-your-future-order-volume-forecasting-at-grubhub-44d47ad08d5b))
- **Gojek — Predict food delivery times (2022)** — Food-delivery ETA framed as setting expectations: the actual time is split into components (restaurant preparation, pickup, travel) and each is predicted from merchant, order and traffic features, judged offline against a benchmark and online by customer outcomes. Source: [article](https://www.gojek.io/blog/food-debarkation-tensoba) ([archived copy](https://web.archive.org/web/2024/https://www.gojek.io/blog/food-debarkation-tensoba))
- **Uber — Predict estimated time of arrival (2022)** — DeepETA predicts the residual of the routing engine's ETA with an encoder–decoder Transformer (linear attention) over discretised, embedded and hashed features, trained with an asymmetric Huber loss and a bias-adjusting decoder; it beat the earlier XGBoost model on mean absolute error, serving mobility and delivery worldwide. Source: [article](https://www.uber.com/GB/en/blog/deepeta-how-uber-predicts-arrival-times/)
- **Spotify — Forecast user activity metrics (2022)** — User forecasts run weekly and on demand: time-series models for mature markets, clustering proxies for new ones, business input for special cases; infrastructure cut hyperparameter tuning from months to hours. Source: [article](https://engineering.atspotify.com/2022/06/how-we-built-infrastructure-to-run-user-forecasts-at-spotify)
- **Walmart — Forecast anomalies in refrigeration (2022)** — Refrigeration anomaly detection: a Prophet forecast per sensor, run in parallel on Spark, flags readings outside the forecast band so failures are caught before food spoils. Source: [article](https://medium.com/walmartglobaltech/forecast-anomalies-in-refrigeration-with-pyspark-sensor-data-195f23ae24e2)
- **Gojek — Predict estimated time of delivery (2022)** — The same article as M.3's “Gojek — Predict food delivery times (2022)”; its summary is there. Source: [article](https://medium.com/gojekengineering/how-we-estimate-food-debarkation-time-with-tensoba-da05674cb758)
- **Lyft — Make causally valid forecasts (2022)** — Causal forecasting, part 1: marketplace levers (rider coupons, driver bonuses, pricing) move downstream metrics, and the data is confounded by past decisions, so causal models of each lever are combined and optimised to plan spend. Causal forecasting, part 2: the software behind it (indexed tensors, a model collection and a loss that keeps forecasts consistent with experiment results), plus evaluation and the optimisation built on top. Source: [part 1](https://eng.lyft.com/causal-forecasting-at-lyft-part-1-14cca6ff3d6d) · [part 2](https://eng.lyft.com/causal-forecasting-at-lyft-part-2-418f1febca5a)
- **DoorDash — Predict delivery supply and demand (2021)** — Supply–demand balance: local forecasts of delivery-driver supply and order demand, with requirements for multivariate forecasts, extrapolation and counterfactuals, drive pay incentives in expected shortfalls. Source: [article](https://careersatdoordash.com/blog/managing-supply-and-demand-balance-through-machine-learning/)
- **Scribd — Extract metadata from documents (2021)** — Keyphrase and named-entity extraction from long documents to enrich metadata: unsupervised n-gram and part-of-speech filtering with tf-idf, entities normalised by aliases and linked to Wikidata, feeding discovery and recommendation. Source: [article](https://tech.scribd.com/blog/2021/information-extraction-at-scribd.html)
- **Twitter — Forecast resource usage and cost (2021)** — Predicting each SQL query's CPU time and memory from its text before it runs (not from query plans), to schedule queries and scale clusters ahead of heavy queries on a petabyte-scale federated SQL system. Source: [article](https://blog.twitter.com/engineering/en_us/topics/insights/2021/forecasting-sql-query-resource-usage-with-machine-learning) ([archived copy](https://web.archive.org/web/2024/https://blog.twitter.com/engineering/en_us/topics/insights/2021/forecasting-sql-query-resource-usage-with-machine-learning))
- **Ocado — Forecast e-commerce grocery demand (2021)** — Retail demand forecasting for grocery stock from sales history, pre-orders and external factors, moving from heuristics to feed-forward and sequence-to-sequence networks, balancing availability against waste. Source: [article](https://careers.ocadogroup.com/blogs/finding-the-sweet-spot)
- **Mercado Libre — Forecast demand for e-commerce items (2021)** — Global time-series models (one model across all items) forecast item-level sales and demand for a marketplace's first-party stock; demand is estimated even for items with no recorded sales, such as those out of stock. Source: [article](https://medium.com/mercadolibre-tech/global-time-series-forecasting-models-for-item-level-demand-and-sales-forecasts-in-our-marketplace-aee2956957ae)
- **Instacart — Spot lost demand (2019)** — Estimating lost demand when delivery slots are scarce: conversion models give the demand that would have occurred with full availability (a counterfactual) against the demand observed, validated offline and online, replacing earlier visit-count heuristics. Source: [article](https://tech.instacart.com/modeling-the-unseen-6a51c9a02430)
- **Gojek — Accurately forecast demand (2019)** — An automated, democratised forecasting tool for a super-app: it replaces spreadsheets and plain ARIMA or ETS with models that take outside variables, such as the moving Ramadan season. Source: [article](https://www.gojek.io/blog/under-the-hood-of-gojeks-automated-forecasting-tool) ([archived copy](https://web.archive.org/web/2024/https://www.gojek.io/blog/under-the-hood-of-gojeks-automated-forecasting-tool))
- **Uber — 100+ Petabytes with Minute Latency (2018)** — Four generations of a big-data platform: from early warehouses to Hadoop to incremental ingestion and modelling with Hudi, then work on data quality, latency and efficiency (the data foundation beneath the ML systems). Source: [article](https://eng.uber.com/uber-big-data-platform/) ([archived copy](https://web.archive.org/web/2024/https://eng.uber.com/uber-big-data-platform/))

### Fraud / trust & safety

- **Stripe — Prevent fraudulent transactions (2023)** — Radar scores every payment in under 100 ms from over 1,000 features on a network where about 0.1% is fraud; the model evolved from logistic regression to a wide & deep ensemble to a pure deep network (ResNeXt-inspired), cutting training time 85%, while blocking only about 0.1% of legitimate payments. Source: [article](https://stripe.dev/blog/how-we-built-it-stripe-radar)
- **LinkedIn — Detect viral spam (2023)** — Viral spam: proactive deep classifiers act when content is posted and reactive boosted trees act on engagement signals as it spreads; spam views −7.3% and policy-violating views −12%. Source: [article](https://www.linkedin.com/blog/engineering/trust-and-safety/viral-spam-content-detection-at-linkedin)
- **Wayfair — Detect fraud with embeddings (2023)** — Customer-journey embeddings for fraud and scam detection, learned self-supervised by predicting the next page in a session, run in Vertex AI Pipelines; downstream fraud models gained up to 18% relative PR-AUC. Source: [article](https://www.aboutwayfair.com/careers/tech-blog/introducing-melange-a-customer-journey-embedding-system-for-improving-fraud-and-scam-detection)
- **Zillow — Identify and block unwanted callers (2023)** — No readable copy was found; linked only. Source: [article](https://www.zillow.com/tech/spectrobrain-detecting-phone-spam-with-semi-supervised-learning/)
- **BlaBlaCar — Prevent phishing and payment fraud (2023)** — Fighting phishing and payment scams on a ride-sharing platform, part 1: define the problem and the metrics first, get a simple version working before scaling it, and prefer a learned model to an ever more complex heuristic. Part 2, the first fraud pipeline: infrastructure first; serving-time features are stored inside the fraud-score event so training uses exactly what serving saw (no skew), and labels are checked for correctness at training time. Source: [part 1](https://medium.com/blablacar/how-we-used-machine-learning-to-fight-fraud-at-blablacar-part-1-3b976c9dcdf6) · [part 2](https://medium.com/blablacar/how-we-built-our-machine-learning-pipeline-to-fight-fraud-at-blablacar-part-2-476335f459b4)
- **Uber — Detect potential fraudulent entities (2023)** — Risk Entity Watch flags accounts behaving anomalously without labels: thousands of per-entity features over several time windows, normalised, scored by tree- and network-based anomaly detectors (with histogram analysis), and routed to reviewers before any action. Source: [article](https://www.uber.com/IN/en/blog/risk-entity-watch/?uclick_id=9c4355d3-795f-4b1d-b18e-4b8b4c8ed29f)
- **Grab — Automatically detect new fraud types (2023)** — Unlabelled fraud detection on the consumer–merchant bipartite graph: a graph autoencoder (GraphBEAN) scores interactions by reconstruction error, tags the suspected fraud type and routes cases to analysts and automated actions. Source: [article](https://engineering.grab.com/graph-anomaly-model)
- **Whatnot — Detect marketplace spam (2023)** — Trust and safety on a live-shopping marketplace: a central rule engine over events, model scores and logs was extended with LLM calls, so message scams are detected by an LLM judging conversation context and then enforced by rules. Source: [article](https://medium.com/whatnot-engineering/how-whatnot-utilizes-generative-ai-to-enhance-trust-and-safety-c7968eb6315e)
- **Uber — Detect payment fraud (2022)** — RADAR catches payment-fraud attacks early: activity time series are decomposed with a Bayesian time-varying regression (Orbit KTR) to spot anomalies, pattern mining (FP-Growth) proposes rules, and analysts approve them before a rule engine deploys them. Source: [article](https://www.uber.com/GB/en/blog/project-radar-intelligent-early-fraud-detection/)
- **Netflix — Detect account or content fraud (2022)** — Anomaly detection for account and content abuse on a streaming service: heuristic-aware labels on about a million benign and 28,000 anomalous accounts, handling of label imbalance, and semi-supervised against supervised models compared. Source: [article](https://netflixtechblog.medium.com/machine-learning-for-fraud-detection-in-streaming-services-b0b4ef3be3f6)
- **Grab — Detect fraud with graph models (2022)** — Fraud probability for nodes in a graph of millions of users, merchants and devices, by a relational graph convolutional network trained semi-supervised on few labels; near-perfect AUROC reported, and it finds unseen patterns. Source: [article](https://engineering.grab.com/graph-for-fraud-detection)
- **Slack — Detect spam invites (2021)** — Invite spam blocked by sparse logistic regression over about 60 million features (IDs, email, IP, word stems, character n-grams, team age); labels from whether an invite is accepted within 4 days; served as a Kubernetes microservice; invites it flags are accepted 3% of the time, against 70% for the old rules. Source: [article](https://slack.engineering/blocking-slack-invite-spam-with-machine-learning/)
- **Pinterest — Detect spam users (2021)** — Fighting spam by clustering: anomalous groups of accounts that share dominant feature values (the same IP, domain or text pattern) become automatically generated patch rules, reviewed by agents and archived after a time, so rules can follow mutating spammers. Source: [article](https://medium.com/pinterest-engineering/fighting-spam-using-clustering-and-automated-rule-creation-1c01d8c11a05)
- **PayPal — Detect payment fraud (2020, 2021)** — A shadow platform for a large fleet of fraud models: continuous integration and deployment of models, a shadow mode that scores live traffic without acting on it, and self-service tools to compare challengers with the champion. Detecting several account-takeover fraud patterns with one multi-task deep model, tuned for catch rate across tasks while keeping good-customer declines low, with robust feature learning so performance holds when data shifts after deployment. Source: [article](https://medium.com/paypal-tech/machine-learning-model-ci-cd-and-shadow-platform-8c4f44998c78) · [article](https://medium.com/paypal-tech/multi-domain-fraud-detection-while-reducing-good-user-declines-part-i-e8bba5b07da8)
- **Swiggy — Detect fraud in online food delivery (2021)** — Weak supervision for fraud in food delivery: experts' labelling heuristics become labelling functions that label data at scale, feeding a model that improves on a baseline trained only on scarce expert labels; graph connectedness adds signal. Source: [article](https://bytes.swiggy.com/defraudnet-an-end-to-end-weak-supervision-framework-to-detect-fraud-in-online-food-delivery-22366ddce461) ([archived copy](https://web.archive.org/web/2024/https://bytes.swiggy.com/defraudnet-an-end-to-end-weak-supervision-framework-to-detect-fraud-in-online-food-delivery-22366ddce461))
- **Stripe — Detect fraud in online payments (2020, 2021)** — A primer on fraud models: each payment gets a fraud probability from hundreds of network features, high-risk ones are blocked, and the operating point is judged by precision, recall and false-positive rate. Fraud rings: candidate account pairs that share attributes are scored by a gradient-boosted similarity model trained on analyst-compiled rings, pairs above a threshold become edges, and connected components are the clusters sent for review or blocking. Source: [article](https://stripe.com/en-mx/guides/primer-on-machine-learning-for-fraud-protection) · [article](https://stripe.com/blog/similarity-clustering)
- **PayPal — Prevent repeated payment fraud (2021)** — A real-time graph database for fraud: accounts, devices and payment instruments linked in a graph queried with Gremlin, a graph viewer for analysts, and graph embeddings used to catch repeat fraudsters who return with new accounts. Source: [article](https://medium.com/paypal-tech/how-paypal-uses-real-time-graph-database-and-graph-analysis-to-fight-fraud-96a2b918619a)
- **Wayfair — Detect payment fraud (2020)** — Order fraud (stolen cards) sorted into fraudulent, legitimate or uncertain, with the uncertain sent to reviewers; explanations for reviewers from permutation importance, LIME and SHAP. Source: [article](https://www.aboutwayfair.com/tech-innovation/explainable-fraud-detection)
- **Lyft — Predict fraudulent activity (2018)** — Fingerprinting fraud from user-action sequences: instead of hand-built features, an action-embedding layer feeds convolutional and recurrent networks that learn behaviour patterns such as social-engineering account takeovers. Source: [article](https://eng.lyft.com/fingerprinting-fraudulent-behavior-6663d0264fad)
- **Lyft — Identify user fraud (2018)** — From hand-coded logistic regression to gradient-boosted trees and deep models in fraud decisions; the move required consistent feature and model definitions between notebook prototypes and the production service. Source: [article](https://eng.lyft.com/from-shallow-to-deep-learning-in-fraud-9dafcbcef743)
- **Lyft — Shallow to deep learning in fraud (2018)** — The same article as M.4's “Lyft — Identify user fraud (2018)”; its summary is there. Source: [article](https://eng.lyft.com/from-shallow-to-deep-learning-in-fraud-9dafcbcef743)

### LLM / genAI apps

- **Stitch Fix — Generate ad headlines (2023)** — Expert-in-the-loop generation: ad headlines from GPT-3 prompted with style keywords, reviewed by copywriters; product descriptions from a model fine-tuned on expert-written examples, rated higher than human copy in blind comparison. Source: [article](https://multithreaded.stitchfix.com/blog/2023/03/06/expert-in-the-loop-generative-ai-at-stitch-fix/)
- **Microsoft — Diagnose production incidents with LLM (2023)** — Root cause and mitigation suggestions for cloud incidents from GPT-3 and GPT-3.5 fine-tuned on over 40,000 incidents; GPT-3.5 gained 15–42% on lexical and semantic metrics, and over 70% of on-call engineers rated suggestions useful. Source: [article](https://www.microsoft.com/en-us/research/blog/large-language-models-for-automatic-cloud-incident-management/)
- **GitHub — Generate code and code suggestions (2023)** — Code completion from OpenAI models (GPT-3, then Codex), improved by prompt crafting that pulls context from neighbouring editor tabs, file paths and similar open text; success measured by acceptance rate and how much suggested code is kept. Source: [article](https://github.blog/engineering/inside-github-working-with-the-llms-behind-github-copilot/)
- **Honeycomb — Generate queries with natural language (2023)** — A natural-language-to-query assistant for an observability product, using LLMs with few-shot prompts and the customer's schema; the hard parts were context-window limits, latency, prompt injection and judging correctness. Source: [article](https://www.honeycomb.io/blog/hard-stuff-nobody-talks-about-llm)
- **Spotify — Automatically generate ad content (2023)** — Automated artist ads for user acquisition: XGBoost predicts registration and subscription rates and cost ratios from campaign metadata and artist popularity to rank which artists to feature; cost per registration 4–14% lower than the heuristic, click rate 11–12% higher. Source: [article](https://engineering.atspotify.com/2023/11/how-we-automated-content-marketing-to-acquire-users-at-scale)
- **Nextdoor — Generate engaging email subject lines (2023)** — AI-generated notification subject lines tuned for engagement: an LLM generates candidate subject lines, a reward model predicts engagement, and rejection sampling picks the best candidate. Source: [article](https://engblog.nextdoor.com/let-ai-entertain-you-increasing-user-engagement-with-generative-ai-and-rejection-sampling-50a402264f56) ([archived copy](https://web.archive.org/web/2024/https://engblog.nextdoor.com/let-ai-entertain-you-increasing-user-engagement-with-generative-ai-and-rejection-sampling-50a402264f56))
- **Meta — Generate code with LLM (2023)** — Code Llama: Llama 2 further trained on 500 billion tokens of code (1 trillion for 70B), with fill-in-the-middle and instruction tuning, at 7B–70B parameters and contexts up to 100,000 tokens; the 34B model scored 53.7% on HumanEval and 56.2% on MBPP. Source: [article](https://ai.meta.com/blog/code-llama-large-language-model-coding/)
- **GitHub — AI copilot for code generation (2023)** — Lessons from building Copilot: find a problem an LLM fits, iterate against acceptance and retention of suggestions, then scale with caching, tuned sampling, filtering of insecure or unwanted output and responsible-AI review; users reported coding 55% faster. Source: [article](https://github.blog/ai-and-ml/github-copilot/how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/)
- **DoorDash — Areas for using Generative AI (2023)** — Five areas for generative AI in food delivery: helping customers complete tasks, interactive discovery, personalised content and merchandising, extracting structured information, and boosting employee productivity. Source: [article](https://careersatdoordash.com/blog/doordash-identifies-five-big-areas-for-using-generative-ai/)
- **Spotify — Generate audio podcast previews (2023)** — Sixty-second podcast previews for millions of episodes from an ensemble of text and audio models (transcripts, sound-event detection) moved from a batch job to a streaming Dataflow pipeline on GPUs: median latency fell from about two hours to 3.7 minutes. Source: [article](https://engineering.atspotify.com/2023/04/large-scale-generation-of-ml-podcast-previews-at-spotify-with-google-dataflow)
- **Thoughtworks — AI copilot for product strategy (2023)** — A product-strategy co-pilot on GPT-3.5/4: prompt templates, chain-of-thought, structured JSON output, web search and embeddings for grounding, streamed into purpose-built UI components; a catalogue of LLM application patterns rather than a metric. Source: [article](https://martinfowler.com/articles/building-boba.html)
- **Salesforce — Summarize Slack conversations (2023)** — Summarising chat conversations and channels on demand or on a schedule with conversational AI, to cut information overload, with attention to data privacy. Source: [article](https://blog.salesforceairesearch.com/ai-summarist-slack-productivity) ([archived copy](https://web.archive.org/web/2024/https://blog.salesforceairesearch.com/ai-summarist-slack-productivity))
- **Instacart — Build an internal AI assistant (2023)** — An internal AI assistant on GPT-4 grown from a hackathon: used by over half of employees monthly, with conversation search, automatic model upgrades and a prompt exchange for sharing prompts. Source: [article](https://tech.instacart.com/scaling-productivity-with-ava-instacarts-internal-ai-assistant-ed7f02558d84)
- **Vimeo — Customer support AI assistant (2023)** — A generative-AI help desk prototype: support articles indexed in a vector store feed retrieval-augmented chat, and alternative models and vector stores are compared on quality, performance and price. Source: [article](https://medium.com/vimeo-engineering-blog/from-idea-to-reality-elevating-our-customer-support-through-generative-ai-101a2c5ea680) ([archived copy](https://web.archive.org/web/2024/https://medium.com/vimeo-engineering-blog/from-idea-to-reality-elevating-our-customer-support-through-generative-ai-101a2c5ea680))
- **Google — Generate summaries (2022)** — One- or two-sentence summaries of documents from a Pegasus-pretrained Transformer encoder with an RNN decoder, fine-tuned on hand-written summaries and distilled so it serves on TPUs with the original's quality at lower latency. Source: [article](https://research.google/blog/auto-generated-summaries-in-google-docs/)
- **Google — Summarize conversations (2022)** — Conversation summaries in a team chat product: an abstractive summarisation model (Pegasus), adapted to chat data, shows a card of topic summaries when a user returns to unread messages. Source: [article](https://research.google/blog/conversation-summaries-in-google-chat/) ([archived copy](https://web.archive.org/web/2024/https://ai.googleblog.com/2022/11/conversation-summaries-in-google-chathtml))
- **Nordstrom — Generate outfit combinations (2021)** — Outfit generation to help human stylists scale: a model scores how well items go together (from images and product attributes) to assemble complete outfits, evaluated partly by stylist review. Source: [article](https://medium.com/tech-at-nordstrom/ai-created-outfits-9529300a1af3)
- **Gojek — Generate names for pickup points (2020)** — Naming pickup points from booking chat logs: a BERT model pre-trained on the company's booking text is fine-tuned to extract the place names that customers and drivers actually use for each clustered pickup location. Source: [article](https://www.gojek.io/blog/nlp-cartobert) ([archived copy](https://web.archive.org/web/2024/https://www.gojek.io/blog/nlp-cartobert))
- **Zillow — Generate floor plans from photos (2020)** — Detecting windows, doors and openings in 360-degree indoor panoramas with bounding boxes, a step toward generating floor plans automatically from captured panoramas. Source: [article](https://www.zillow.com/tech/training-models-to-detect-windows-doors-in-panos/) ([archived copy](https://web.archive.org/web/2024/https://www.zillow.com/tech/training-models-to-detect-windows-doors-in-panos/))

### NLP / text / support

- **Grab — Automatically tag sensitive data (2023)** — Column-level classification of over 20,000 data entities a month (personal data and business metrics) by an orchestration service calling GPT-3.5 with few-shot prompts and a schema, batched through queues with rate limits; owners confirm tags, about 80% positive, saving an estimated 360 person-days a year. Source: [article](https://engineering.grab.com/llm-powered-data-classification)
- **Salesforce — Extract relevant information from a knowledge article (2023)** — Search answers for customer-service agents: search returns the exact answer passage extracted from a knowledge article, so agents can act on or copy it at once. Source: [article](https://blog.salesforceairesearch.com/einstein-search-answers/) ([archived copy](https://web.archive.org/web/2024/https://blog.salesforceairesearch.com/einstein-search-answers/))
- **Dropbox — Identify date formats in file names (2023)** — Dates found in file names by tagging characters with inside-outside-begin labels using a pruned, quantised DistilRoBERTa trained on annotated and synthesised names; 40% more files renamed than with rules, over a million in the first weeks. Source: [article](https://dropbox.tech/machine-learning/using-ml-to-identify-date-formats-in-file-names)
- **Meta — Translate and transcribe across speech and text (2023)** — SeamlessM4T: one multitask model for speech recognition and speech and text translation in both directions across nearly 100 languages (w2v-BERT encoder, UnitY, distillation), with 37% and 48% better robustness to noise and speaker variation. Source: [article](https://ai.meta.com/blog/seamless-m4t/)
- **Nextdoor — Predict harmful comments (2022)** — Nudging kinder conversations: most abusive comments appear in threads with other abusive comments, so a thread-level model predicts contentious conversations and triggers reminders before replies are posted. Source: [article](https://engblog.nextdoor.com/using-predictive-technology-to-foster-constructive-conversations-4af437942bd4) ([archived copy](https://web.archive.org/web/2024/https://engblog.nextdoor.com/using-predictive-technology-to-foster-constructive-conversations-4af437942bd4))
- **Wayfair — Predict intent in customer support messages (2022)** — Customer-service intent detection for a virtual assistant: a two-level taxonomy (11 broad, 70 specific intents) learned from about 200,000 labelled chats by fine-tuned DistilBERT as multi-label classification; over 90% accuracy at 88 ms. Source: [article](https://www.aboutwayfair.com/careers/tech-blog/building-wayfairs-first-virtual-assistant-automating-customer-service-by-text-based-intent-prediction)
- **Pinterest — Detect policy-violating comments (2021)** — Comment quality on creator content: a multi-task classifier trained on labelled comments scores each comment for several facets (spam, hostility, quality), served for filtering and ranking comments. Source: [article](https://medium.com/pinterest-engineering/how-pinterest-powers-a-healthy-comment-ecosystem-with-machine-learning-9e5c3414c8ad)

### CV / video / OCR

- **Apple — Identify objects on images (2023)** — On-device salient-object segmentation: an EfficientNetV2 encoder with a convolutional decoder, trained on real and synthetic composites, produces a 512×512 alpha matte in under 10 ms on the Neural Engine; judged by crowd ratings and segmentation metrics. Source: [article](https://machinelearning.apple.com/research/salient-object-segmentation)
- **Netflix — Improve video quality at scale (2022)** — Neural networks for video downscaling in the encoding pipeline: a learned downscaler replaces conventional filters to raise perceived video quality, applied efficiently at catalogue scale. Source: [article](https://netflixtechblog.com/for-your-eyes-only-improving-netflix-video-quality-with-neural-networks-5b8d032da09c)
- **DoorDash — Extract information from images (2021)** — A lightweight in-house image pipeline for photos from drivers (pizza bags, closed stores, catering set-ups): a reusable deep-network pipeline quickly serves new image-recognition cases more cheaply than outside services. Source: [article](https://careersatdoordash.com/blog/how-doordash-quickly-spins-up-multiple-image-recognition-use-cases/)
- **Bumble — Derive information from images (2020)** — Image detection as a service for two dating apps: classification, captioning and object detection models behind a single web API (Flask), so product teams can call content understanding on millions of daily photos. Source: [article](https://medium.com/bumble-tech/image-detection-as-a-service-9bd463f74f43)
- **Dailymotion — Automatically categorize videos (2020)** — Categorising videos in 20+ languages: an existing bag-of-words classifier was extended with multilingual pretrained embeddings aligned across languages, so a classifier trained on English and French transfers to new languages. Source: [article](https://medium.com/dailymotion/how-we-used-cross-lingual-transfer-learning-to-categorize-our-content-c8e0f9c1c6c3)
- **Dropbox — Modern OCR with CV and DL (2017)** — OCR for phone-scanned documents (shadows, blur, curved pages): a region-based word detector plus a word recogniser (convolutional layers, bidirectional LSTMs, CTC decoding) trained largely on over 10 million synthetic rendered words, reaching accuracy comparable to commercial engines. Source: [article](https://dropbox.tech/machine-learning/creating-a-modern-ocr-pipeline-using-computer-vision-and-deep-learning)

### Speech / audio

- **Netflix — Detect speech and music in audio (2023)** — Detecting speech and music frame by frame in soundtracks, with a curated dataset across genres and languages and a neural model; used for dialogue analysis, music retrieval, localisation and dubbing. Source: [article](https://netflixtechblog.com/detecting-speech-and-music-in-audio-content-afd64e6a5bf8)
- **Walmart — Fill shopping cart via voice dialog (2022)** — Voice reordering of several products in one utterance: a transformer encoder with a conditional random field on top labels multiple product-name entities in the spoken order. Source: [article](https://medium.com/walmartglobaltech/voice-reorder-experience-add-multiple-product-items-to-your-shopping-cart-59d20fc61797)
- **Amazon — Suggest music to listen to (2022)** — Conversational music discovery on voice devices chooses the next follow-up prompt with an offline reinforcement-learning dialogue policy, rewarded when the conversation ends in playback; successful outcomes +8% and turns −20%, then +4% more with listening history. Source: [article](https://www.amazon.science/latest-news/how-amazon-music-uses-recommendation-system-machine-learning)

### Marketing / churn / CLV / notify

- **Monzo — Select relevant marketing messages (2023)** — Choosing which marketing message each customer gets under a contact limit: uplift models predict each campaign's incremental effect per customer, an optimiser assigns campaigns, and a controlled experiment measured the gain. Source: [article](https://medium.com/data-monzo/optimising-marketing-messages-for-monzo-users-3fe805f24572)
- **Expedia — Predict Customer Lifetime Value (CLV) (2023)** — Customer lifetime value at a travel group: machine-learning models predict value over a year and beyond from booking behaviour, with handling for a heavily skewed target, evaluation by segment, and deployment on the group's ML platform. Source: [article](https://medium.com/expedia-group-tech/expedia-groups-customer-lifetime-value-prediction-model-7927cdd44342)
- **Grab — Create scalable lookalike audiences (2023)** — Lookalike audiences for advertisers: users and seed audiences are embedded, compressed by hashing and kept in memory, and matched by cosine similarity; campaigns activate in 15 minutes with doubled impressions and clicks at 98% lower cost. Source: [article](https://engineering.grab.com/scalable-lookalike-audiences)
- **Grab — Optimize promotional campaigns (2023)** — Promotion assignment for merchants: users segmented as active, churned or new, response to each promotion modelled per customer, and offers assigned by Spark jobs; sales rose while promotion spend fell. Source: [article](https://engineering.grab.com/scaling-marketing-for-merchants)
- **Gousto — Predict subscription churn (2022)** — Churn prediction for a recipe-kit subscription: a gradient-boosted tree on behavioural data predicts who is about to leave, with SHAP values to explain which features drive each prediction for the retention team. Source: [article](https://medium.com/gousto-engineering-techbrunch/using-data-science-to-retain-customers-63f19a03a0b6)
- **Uber — Send timely push notifications (2022)** — Push timing: XGBoost predicts the chance each buffered notification converts within 24 hours at each candidate send time, and an integer linear program assigns sends over a 7-day horizon under frequency caps and expiry; opt-outs fell. Source: [article](https://www.uber.com/US/en/blog/how-uber-optimizes-push-notifications-using-ml/)
- **Artefact — Evaluate success of past promotions (2022)** — Measuring past promotions by counterfactual forecasting: a model (Prophet, then XGBoost) trained on non-promotion periods predicts baseline sales for promotion weeks, and actual minus baseline gives each promotion's uplift. Source: [article](https://medium.com/artefact-engineering-and-data-science/forecasting-something-that-never-happened-how-we-estimated-past-promotions-profitability-5f55cfa1d477)
- **LinkedIn — Predict churn and upsell products (2022)** — Sales-account prioritisation: XGBoost predicts upsell and churn per account from purchases, engagement, hiring and firmographics, explained with SHAP and LIME inside the CRM; precision and recall 0.73–0.81, renewals +8% in an A/B test. Source: [article](https://www.linkedin.com/blog/engineering/recommendations/the-journey-to-build-an-explainable-ai-driven-recommendation-sys)
- **Wayfair — Optimize email sending time and frequency (2022)** — Daily email frequency (1–7 a week) chosen per customer from calibrated random-forest probabilities of converting, unsubscribing or ignoring, weighed by revenue and the cost of an unsubscribe; unsubscribe cost −7% with revenue unchanged. Source: [article](https://www.aboutwayfair.com/careers/tech-blog/nightingale-scalable-daily-email-sending-decision-model)
- **Netflix — Apply causality in experiments and marketing (2022)** — A survey of causal inference in practice: the incremental impact of localisation, holdback experiments for long-term effects, a causal adaptation of recommendation models, and incremental account lifetime valuation. Source: [article](https://netflixtechblog.com/a-survey-of-causal-inference-applications-at-netflix-b62d25175e6f)
- **Pinterest — Find lookalike users for ad targeting (2021)** — Lookalike audiences for ads: user embeddings plus MLP classifiers score how similar each user is to an advertiser's seed list, evaluated offline and then online in production. Source: [article](https://medium.com/pinterest-engineering/the-machine-learning-behind-delivering-relevant-ads-8987fc5ba1c0)
- **Wayfair — Optimize paid media marketing (2021)** — Which customers get which paid-marketing treatment, chosen by contextual bandits that log propensities so rewards can be debiased (inverse propensity and doubly robust estimates), with ε-greedy, softmax, SquareCB and bootstrap Thompson exploration compared. Source: [article](https://www.aboutwayfair.com/careers/tech-blog/contextual-bandit-for-marketing-treatment-optimization)
- **DoorDash — Optimize marketing spending (2020)** — Marketing automation: attribution data and cost curves (spend against acquisitions) per channel and campaign, one ML model per channel to build better curves, and a parallel grid search that allocates budget across thousands of campaigns. Source: [article](https://careersatdoordash.com/blog/optimizing-marketing-spend-with-ml/)
- **Lyft — Build a marketing automation platform (2019)** — Automating user-acquisition marketing: a lifetime-value forecaster predicts each new user's value, a budget allocator spreads spend across channels, and automated bidders place bids in each channel. Source: [article](https://eng.lyft.com/lyft-marketing-automation-b43b7b7537cc)

### Availability / inventory

- **DoorDash — Predict if a store is open (2023)** — Replacing a heuristic with ML when drivers report a store closed: a model decides whether the store is truly closed, saving thousands of cancelled orders; next, a loss function weighted by the cost of each error. Source: [article](https://careersatdoordash.com/blog/how-doordash-upgraded-a-heuristic-with-ml-to-save-thousands-of-canceled-orders/)
- **Instacart — Predict availability of food items (2023)** — Part 2 of item availability: the model predicting whether each of hundreds of millions of items is in stock was rebuilt as three scores (general patterns, trending deviations and real-time last-known status) for interpretability and sparse data. Part 3 of item availability: the serving architecture, with an experimentation framework for several models, delta updates, and lazy score refresh triggered when an item appears in search results. Source: [part 1](https://tech.instacart.com/how-instacart-modernized-the-prediction-of-real-time-availability-for-hundreds-of-millions-of-items-59b2a82c89fe) · [part 2](https://tech.instacart.com/instacarts-item-availability-architecture-solving-for-scale-and-consistency-f5661acb20a6)
- **Instacart — Predict grocery item availability (2018, 2023)** — Item availability at over 80,000 stores predicted from shoppers' found and not-found scans plus inventory signals, with thresholds adjusted as the pandemic changed stock; it decides what customers can select, judged by found rate (perfect found rates double reorders). Predicting real-time availability of 200 million items from shoppers' scans and not-found marks: item and time features, plus features from item metadata that help long-tail items, with care for high-cardinality categorical features. Source: [article](https://company.instacart.com/tech-innovation/how-instacarts-item-availability-evolved-over-the-pandemic) · [article](https://tech.instacart.com/predicting-real-time-availability-of-200-million-grocery-items-in-us-canada-stores-61f43a16eafe)

### ML platform / infra

- **King — Automate playtesting pipeline (2019)** — Human-like automated playtesting: a deep network trained on human moves plays new puzzle levels (thousands of levels, many new each week) to estimate difficulty before release, served as an internal tool. Source: [article](https://medium.com/techking/human-like-playtesting-with-deep-learning-92adafffe921) ([archived copy](https://web.archive.org/web/2024/https://medium.com/techking/human-like-playtesting-with-deep-learning-92adafffe921))
- **Uber — Scaling ML with Michelangelo (2019)** — Scaling an internal ML platform to hundreds of use cases and thousands of production models: lessons in organisation, process and technology, ML treated as software engineering, developer velocity and tiered offerings. Source: [article](https://eng.uber.com/scaling-michelangelo/) ([archived copy](https://web.archive.org/web/2024/https://eng.uber.com/scaling-michelangelo/))

### Other (pricing, classification, routing, dimensions and more)

- **Foodpanda — Optimize menu sorting order (2023)** — Menu ranking for a food-delivery platform: the order of categories and items in each vendor's menu is chosen by A/B testing, and the post covers the data pipeline and its failures when vendors change menus mid-ingestion. Source: [article](https://medium.com/foodpanda-data/menu-ranking-422ad21f381e)
- **Zillow — Estimate the house market value (2023)** — The neural home-value estimate: a pipeline of separate county-level models (regional appreciation, adjusted past sales, then valuation) was replaced by one national deep network over property facts, transactions and listing signals; it covers 100 million+ homes, reacts faster to market trends, is simpler to maintain and is more accurate. Source: [article](https://www.zillow.com/tech/building-the-neural-zestimate/)
- **Airbnb — Identify user interests (2023)** — Mining guest reviews and messages with entity extraction to learn what guests care about, then recommending to hosts which home attributes to add or highlight. Source: [article](https://medium.com/airbnb-engineering/prioritizing-home-attributes-based-on-guest-interest-3c49b827e51a)
- **DoorDash — Optimize courier waiting time (2023)** — The life cycle of an ML product that cut driver waiting time at restaurants: a heuristic test first, then a model predicting food preparation time to release orders to restaurants at the right moment, built with cross-team milestones. Source: [article](https://careersatdoordash.com/blog/lifecycle-of-a-successful-ml-product-reducing-dasher-wait-times/)
- **LinkedIn — Select best payment gateway (2023)** — Payment routing: a multiclass logistic regression picks the gateway most likely to approve a subscription charge from transaction type, card type and network, with inverse-probability weighting to correct for the old routing's bias; approval rate rose significantly in an A/B test. Source: [article](https://www.linkedin.com/blog/engineering/product-design/improving-the-customer-s-experience-via-ml-driven-payment-routin)
- **Yelp — Organize e-commerce content using embeddings (2023)** — Shared embeddings of reviews, business data and photos (Universal Sentence Encoder for text, CLIP for images) reused by downstream tagging, sentiment and recommendation tasks, including zero-shot classification. Source: [article](https://engineeringblog.yelp.com/2023/04/yelp-content-as-embeddings.html)
- **Monzo — Detect patterns in text data (2023)** — Topic modelling of 800,000 free-text savings-pot names (many one word, some with emoji) to understand what customers save for. Source: [article](https://medium.com/data-monzo/using-topic-modelling-to-understand-customer-saving-goals-2bb06f00ce2d)
- **Wayfair — Predict new product’s sales potential (2023)** — Predicting which new products will win: embeddings, LSTMs over early engagement and sales, and count distributions (negative binomial, log-normal) forecast long-run sales so winners get better placement. Source: [article](https://www.aboutwayfair.com/careers/tech-blog/how-wayfair-uses-predicted-winners-models-to-accelerate-success-for-new-products)
- **Wayfair — Identify business customers (2023)** — Business-customer identification: XGBoost over 100+ browsing, order and third-party features (with record linkage and model-generated labels), threshold set on the precision–recall curve, served in real time from Aerospike and Vertex AI Feature Store; twice as effective as rules. Source: [article](https://www.aboutwayfair.com/careers/tech-blog/hamlet)
- **Criteo — Figure out users' preferences (2023)** — An essay arguing that recommender systems rely on unstated user-choice models; making them explicit would link offline and online metrics and relate recommendation to the incrementality of advertising. Source: [article](https://medium.com/criteo-engineering/recommender-systems-need-a-user-model-c3b3790311bf)
- **Grammarly — Suggest gender-inclusive grammatical error corrections (2023)** — Gender bias in grammatical error correction measured on parallel sentences varying masculine, feminine and singular they, then reduced by data augmentation without losing correction quality (a research paper). Source: [article](https://arxiv.org/abs/2306.07415)
- **Delivery Hero — Better understand user behavior (2023)** — Understanding customers before personalising: exploratory analysis of behaviour, motivations and preferences, and segmentation, which shapes which signals the recommendation models use. Source: [article](https://tech.deliveryhero.com/personalisation-at-delivery-hero-understanding-customers/) ([archived copy](https://web.archive.org/web/2024/https://tech.deliveryhero.com/personalisation-at-delivery-hero-understanding-customers/))
- **Expedia — Alert users about optimal deals (2023)** — Flight price alerts for subscribed searches: a message-relevance model predicts which price-change alerts a traveller will find useful, so fewer, better notifications are sent. Source: [article](https://medium.com/expedia-group-tech/increasing-travelers-engagement-through-relevant-price-alerts-at-expedia-group-75aa6a377864)
- **Walmart — Resolve entities and detect relationships (2023)** — An entity resolution framework compared on several use cases: transparent rule-based matching (useful where regulation demands explainability) against machine-learning matching with a feedback loop. Source: [article](https://medium.com/walmartglobaltech/exploring-an-entity-resolution-framework-across-various-use-cases-cb172632e4ae)
- **Wayfair — Send relevant communications to customers (2023)** — Send or skip decisions for millions of daily emails and pushes by contextual bandits rewarded on engagement, with new policies checked by offline policy evaluation before launch. Source: [article](https://www.aboutwayfair.com/careers/tech-blog/griffin-how-wayfair-leverages-reinforcement-learning-to-send-customers-relevant-communications)
- **Meta — Show users relevant content at scale (2023)** — Explore runs four stages (two-tower retrieval with approximate nearest neighbours, a first-stage ranker distilled from the second, a multitask second-stage ranker, a final re-rank); predicted clicks, likes and see-less actions are weighted into one expected-value score, with weights tuned by Bayesian optimisation. Source: [article](https://engineering.fb.com/2023/08/09/ml-applications/scaling-instagram-explore-recommendations-system/)
- **GitHub — Automated code reviews and PR tagging (2023)** — Generative AI for compliance in code review: suggested pull-request descriptions and review comments to keep separation of duties without slowing developers; a product announcement without metrics. Source: [article](https://github.blog/enterprise-software/governance-and-compliance/generative-ai-enabled-compliance-for-software-development/)
- **Spotify — Target in-app messaging (2023)** — In-app messages sent only where they help: a multiheaded network (shared layers, one head per treatment) trained on a random holdout estimates each user's uplift in retention, and users with positive uplift get the message; A/B test showed significant retention gains. Source: [article](https://engineering.atspotify.com/2023/06/experimenting-with-machine-learning-to-target-in-app-messaging)
- **Nubank — Automatically route customer phone calls (2023)** — Support-call routing from app clickstreams: events become text-like tokens embedded by contrastive and sequence methods borrowed from NLP, predicting the customer's need before they speak; correct routing without customer input improved over 50%. Source: [article](https://building.nu.com/presenting-precog-nubanks-real-time-event-ai/)
- **Mercado Libre — Predict product dimensions for delivery (2022)** — Predicting package dimensions and weight for shipping cost and warehouse occupancy: each item is embedded, its nearest neighbours with known dimensions are found in an Annoy index, those beyond a distance threshold are dropped, and the rest give the estimate. Source: [article](https://medium.com/mercadolibre-tech/predicting-package-dimensions-based-on-a-similarity-model-at-mercado-libre-d64a9dd4351d)
- **Walmart — Assist in e-commerce shopping (2022)** — One multi-task language-understanding model serving several virtual assistants (shopping, customer care, store associates): joint intent classification and slot filling across domains replace separate models. Source: [article](https://medium.com/walmartglobaltech/a-unified-multi-task-model-for-supporting-multiple-virtual-assistants-in-walmart-2b077c2c96e)
- **Foodpanda — Classify restaurants and cuisines (2022)** — Cuisine labels are subjective and differ by country: labels are derived from what customers search for and order, then extended semi-supervised through restaurant embeddings, validated and evaluated for search. Source: [article](https://medium.com/foodpanda-data/classifying-restaurant-cuisines-with-subjective-labels-fa10012d18a9)
- **GitHub — Detect vulnerabilities in code (2022)** — Code-scanning alerts from a deep classifier trained on tens of millions of snippets that hand-written CodeQL queries labelled, run on standard Actions runners; on new alerts the queries missed, about 80% recall and 60% precision. Source: [article](https://github.blog/security/vulnerability-research/leveraging-machine-learning-find-security-vulnerabilities/)
- **DoorDash — Find high-value merchants (2022)** — Choosing which merchants to bring onto the platform: a feature store and models estimate each prospective merchant's value to the market, generate daily predictions, and are judged by their business value. Source: [article](https://careersatdoordash.com/blog/building-merchant-selection/)
- **Grammarly — Suggest text edits (2022)** — How the editor applies suggestions safely: each suggestion is a Delta (operational transformation) rebased as the user types and composed with other suggestions before applying, so the UI never freezes; engineering, not a model. Source: [article](https://www.grammarly.com/blog/engineering/how-suggestions-work-grammarly-editor/)
- **Zillow — Select tags for product listings (2022)** — No readable copy was found; linked only. Source: [article](https://www.zillow.com/tech/helping-shoppers-find-a-home-using-home-insights/)
- **Airbnb — Improve customer support (2022)** — Text-generation models trained on years of agent–guest support records: they power content recommendation, a real-time agent assistant that suggests replies, and a paraphrase model that confirms understanding in the chatbot. Source: [article](https://medium.com/airbnb-engineering/how-ai-text-generation-models-are-reshaping-customer-support-at-airbnb-a851db0b4fa3)
- **Walmart — Categorize e-commerce products (2021, 2022)** — Product categorisation across tens of thousands of categories: semantic label representations make wrong predictions land near the true category, so mistakes become less severe even when accuracy is unchanged; applied to text and image inputs. Assigning each product to the right place in the category hierarchy so it appears on the right shelf and in search: the problem is split into predicting product type, then family and hierarchy, with deep text models. Source: [article](https://medium.com/walmartglobaltech/semantic-label-representation-with-an-application-on-multimodal-product-categorization-63d668b943b7) · [article](https://medium.com/walmartglobaltech/deep-learning-product-categorization-and-shelving-630571e81e96)
- **Zillow — Identify customers that are likely to convert (2022)** — Identifying visitors with high intent to buy a home soon, among tens of millions of monthly visitors with varied goals, so product features can guide them toward offers, financing and agents. Source: [article](https://www.zillow.com/tech/identifying-high-intent-buyers/) ([archived copy](https://web.archive.org/web/2024/https://www.zillow.com/tech/identifying-high-intent-buyers/))
- **Zillow — Extract text features (2022)** — No readable copy was found; linked only. Source: [article](https://www.zillow.com/tech/incorporating-listing-descriptions-into-the-zestimate/)
- **Lyft — Optimize trip price (2022)** — Pricing system design for a two-sided marketplace: prices should be reliable, fair and balance supply and demand; covers pricing orchestration, operations, algorithmic pricing and online price learning with reinforcement learning. Source: [article](https://eng.lyft.com/pricing-at-lyft-8a4022065f8b)
- **Grammarly — Detect and correct grammatical errors (2021, 2022)** — GECToR corrects grammar by tagging, not rewriting: a BERT-like encoder assigns one of about 5,000 edit tags per token, applied over a few iterations; F0.5 of 65.3 on CoNLL-2014 and 72.4 on BEA-2019, about ten times faster than Transformer translation models. Grammatical error correction from three parts: sequence-to-sequence translation, sequence tagging for local edits and syntactic pattern rules, ensembled and distilled; judged by precision and recall on linguist-built sets, then by user acceptance. Adversarial training for grammar correction: a sequence-to-sequence generator proposes rewrites and a sentence-pair discriminator judges them, trained with policy gradients; beat conventionally trained RNN and Transformer models on standard sets (research). Source: [article](https://www.grammarly.com/blog/engineering/gec-tag-not-rewrite/) · [article](https://www.grammarly.com/blog/engineering/innovating-the-basics/) · [article](https://www.grammarly.com/blog/engineering/adversarial-grammatical-error-correction/)
- **Airbnb — Improve customer travel experience (2022)** — The platform behind conversational AI and agent automation in customer support: an event orchestrator, a workflow engine, a store of reusable actions and a flow builder let teams compose automated support flows. Source: [article](https://medium.com/airbnb-engineering/intelligent-automation-platform-empowering-conversational-ai-and-beyond-at-airbnb-869c44833ff2)
- **Swiggy — Flag incorrectly captured locations (2022)** — Flagging addresses where the captured GPS point disagrees with the typed address: a deep binary classifier, with correct and incorrect training labels synthesised by perturbing good examples. Source: [article](https://bytes.swiggy.com/using-deep-learning-to-detect-dissonance-between-address-text-and-location-4b228bc2c3fb) ([archived copy](https://web.archive.org/web/2024/https://bytes.swiggy.com/using-deep-learning-to-detect-dissonance-between-address-text-and-location-4b228bc2c3fb))
- **Uber — Validate identity documents (2022)** — Rider identity checks: uploaded IDs are verified by vendors plus in-house multitask deep models (OCR, object detection, fraud signals), quantised with TensorFlow Lite, with human review for doubtful cases; over a million IDs in 11+ countries since 2019. Source: [article](https://www.uber.com/GB/en/blog/ubers-real-time-document-check/)
- **Didact AI — Predict stock prices (2022)** — A stock-picking engine: XGBoost retrained daily on about 1,000 engineered features over 4,000 US equities, with unsupervised market-regime models and SHAP explanations, predicting which stocks will beat the market on risk-adjusted return (a personal project). Source: [article](https://principiamundi.com/posts/didact-anatomy/)
- **Wayfair — Identify specific entities within a text (2022)** — Aspect-based sentiment in reviews: a BERT model extracts product aspects and their sentiment to fill long-tail pages (such as a sofa good for pets); macro-F1 nearly doubled. Source: [article](https://www.aboutwayfair.com/careers/tech-blog/wayfairs-new-approach-to-aspect-based-sentiment-analysis-helps-customers-easily-find-long-tail-products)
- **Oda — Predict driver's non-driving time (2021, 2022)** — Part 2: an ML model predicts delivery service time from order, customer and address features (half of a driver's day is non-driving service time, measured by geofence); a six-week field test in one region checked it in real routes. Part 1: service time (the non-driving time per stop, about half of route time) is measured with geofencing on drivers' phones, chosen and tested with drivers and with care for their privacy. Source: [article](https://medium.com/oda-product-tech/how-we-went-from-zero-insight-to-predicting-service-time-with-a-machine-learning-model-part-2-2-ad8b0c3e4838) · [article](https://medium.com/oda-product-tech/how-we-went-from-zero-insight-to-predicting-service-time-with-a-machine-learning-model-part-1-516b9545d02f)
- **LinkedIn — Estimate the impact of product changes (2022)** — A platform for observational causal inference when experiments are impossible: automated pipelines apply coarsened exact matching, doubly robust estimation, instrumental variables, fixed effects or Bayesian structural time series, with robustness checks and a review committee. Source: [article](https://www.linkedin.com/blog/engineering/data-science/ocelot-scaling-observational-causal-inference-at-linkedin)
- **Siemens Healthineers — Optimize software testing (2022)** — Test outcomes predicted at commit time by decision trees on source-control and test logs (78% mean accuracy over 79,361 tests); ordering tests by failure probability found the first failure sooner and cut total run time about 10%; defects routed to teams with 75% recall. Source: [article](https://www.infoq.com/articles/machine-learning-test-feedback-optimization/)
- **LinkedIn — Improve ML model performance with multitask learning (2022)** — Multitask learning across job recommendation, search and recruiter matching: a shared-bottom model with task-specific heads, trained jointly or iteratively with distillation, so related tasks share representations despite different data and features. Source: [article](https://www.linkedin.com/blog/engineering/data-modeling/applying-multitask-learning-to-ai-models-at-linkedin)
- **Google — Suggest past photos to look at (2021)** — Design notes on AI-curated photo memories: models select and group meaningful photos from huge libraries, with filters that avoid painful memories and controls that let people hide people or dates. Source: [article](https://medium.com/people-ai-research/a-snapshot-of-ai-powered-reminiscing-in-google-photos-5a05d2f2aa46)
- **Uber — Identify cash intermediaries (2021)** — Internal audit finds cash-intermediary vendors: a random forest scores transactions and an SVM classifies vendors from the aggregated scores and vendor features, trained on just 47 known agents among 477 vendors; about 90% recall and 89% precision on validation, and unknown networks found. Source: [article](https://www.uber.com/GB/en/blog/ml-internal-audit/)
- **Microsoft — Cluster customer support issues by similarity (2021)** — Part 2 finds the top investment areas in support data by topic modelling: TF-IDF with LDA compared with BERT embeddings clustered by HDBSCAN, and the transformer approach put into production. Source: [article](https://medium.com/data-science-at-microsoft/ml-and-customer-support-part-2-leveraging-topic-modeling-to-identify-the-top-investment-areas-in-f0348382c251)
- **Apple — Recognize people in photos (2021)** — People recognition on device: face and upper-body embeddings from a small network (under 4 ms on the Neural Engine) are clustered into galleries of known people and new photos assigned by sparse coding; training data chosen and augmented for consistent accuracy across age, gender and skin tone. Source: [article](https://machinelearning.apple.com/research/recognizing-people-photos)
- **Datto — Predict hard drive failures (2021)** — Predicting hard-drive failure from daily SMART reports across storage servers, so drives are replaced before data is lost; raw values are discarded because manufacturers report them inconsistently. Source: [article](https://datto.engineering/post/predicting-hard-drive-failure-with-machine-learning) ([archived copy](https://web.archive.org/web/2024/https://datto.engineering/post/predicting-hard-drive-failure-with-machine-learning))
- **Bumble — Detect rude messages (2021)** — Part 1: the rude-message detector fine-tunes a multilingual transformer (XLM-RoBERTa) to flag abusive messages in many languages, validated per language and served in production to protect users. Part 2 examines the multilingual toxicity model's embedding space: sentence embeddings are similar across languages, so the model generalises cross-lingually, and a reduced embedding even separates languages. Source: [part 1](https://medium.com/bumble-tech/multilingual-message-content-moderation-at-scale-ddd0da1e23ed) · [part 2](https://medium.com/bumble-tech/multilingual-message-content-moderation-at-scale-7ea562e29e25)
- **Nextdoor — Send relevant and timely updates (2021)** — New-post and trending-post notifications: models decide which neighbour gets which notification at what volume, using approximate quantiles (t-digest) for thresholds, with lessons from production. Source: [article](https://engblog.nextdoor.com/nextdoor-notifications-how-we-use-ml-to-keep-neighbors-informed-57d8f707aab0) ([archived copy](https://web.archive.org/web/2024/https://engblog.nextdoor.com/nextdoor-notifications-how-we-use-ml-to-keep-neighbors-informed-57d8f707aab0))
- **Dropbox — Identify best time for renewal charge (2021)** — Retrying failed subscription payments at the best time: a gradient-boosted ranking model over failure type, account usage and payment details picks when to charge, served in under 300 ms; approval rates rose and collection time fell against the old rules. Source: [article](https://dropbox.tech/machine-learning/optimizing-payments-with-machine-learning)
- **Brex — Classify bank transactions (2021)** — Classifying card merchants from cryptic transaction strings: a places-lookup service identifies the merchant, an ML model classifies it with acceptance criteria per component, and crowd workers handle what the models cannot. Source: [article](https://medium.com/brexeng/how-we-built-a-mostly-automated-system-to-solve-credit-card-merchant-classification-f9108029e59b)
- **Grammarly — Capture what readers pay attention to (2021)** — Which email sentences readers attend to, learned from ten readers per email on a sentence-by-sentence reading interface normalised for reading speed; a cost–value model over 40+ linguistic features ranks sentences by information against effort. Source: [article](https://www.grammarly.com/blog/engineering/readers-attention/)
- **Apple — Identify best user experience (2021)** — Product-page experiments (icons, screenshots) that adapt traffic: empirical-Bayes (James–Stein) shrinkage, Thompson sampling, windowed smoothing for delayed feedback and sequential tests with Bayes factors give fewer false positives than maximum likelihood and allow early, valid stopping. Source: [article](https://machinelearning.apple.com/research/interpretable-adaptive-optimization)
- **Airbnb — Data privacy and security (2021)** — Automated data protection: a classification service samples data stores and detects personal and sensitive data with rules and ML models, measures its own quality with labelled samples and retrains; a separate scanner finds secrets in code. Source: [article](https://medium.com/airbnb-engineering/automating-data-protection-at-scale-part-2-c2b8d2068216)
- **Capital One — Identify suspicious account activity (2021)** — Anti-money-laundering alerts scored by a random forest trained on over 100,000 past investigations so investigators work the riskiest cases first; fewer false positives than rules. Source: [article](https://www.capitalone.com/tech/machine-learning/how-machine-learning-can-help-fight-money-laundering/)
- **Wayfair — Assign color names to products (2021)** — Colour names for products: mini-batch k-means extracts dominant RGB colours from images, and a four-level taxonomy of about 4,055 named colour groups, built by clustering under a perceptual (delta-E) distance, maps them to words; 88% of tags accepted on review. Source: [article](https://www.aboutwayfair.com/careers/tech-blog/from-rgb-to-descriptive-color-names-wayfairs-in-house-color-algorithms-to-improve-customer-shopping-experience)
- **Capital One — Automate incident management (2021)** — Application failures: time-series anomaly detection on API volumes, errors and latency, then a Bayesian network over the dependency graph names the likely failing component; incident resolution up to 50% faster. Source: [article](https://www.capitalone.com/tech/machine-learning/automated-detection-diagnosis-remediation-of-application-failure/)
- **Walmart — Identify refrigeration defrost (2021)** — Detecting defrost cycles in store refrigeration sensor data with the Fourier transform, since periodic defrosts must be separated from real anomalies in temperature readings. Source: [article](https://medium.com/walmartglobaltech/predicting-defrost-in-refrigeration-cases-at-walmart-using-fourier-transform-e64c0c59323)
- **Capital One — Improve cardholder experience (2021)** — Edge ML in the browser extension that fills virtual card numbers: a model running locally on the page (from its DOM and pixel positions) finds the payment fields, so customer data never leaves the device. Source: [article](https://www.capitalone.com/tech/machine-learning/edge-machine-learning-eno-virtual-card-numbers/) ([archived copy](https://web.archive.org/web/2024/https://www.capitalone.com/tech/machine-learning/edge-machine-learning-eno-virtual-card-numbers/))
- **Shopify — Categorize e-commerce products (2020, 2021)** — Product categorisation into over 5,500 Google taxonomy categories from images (MobileNetV2) and text (multilingual BERT) in one multitask model with class weighting; leaf precision +8% with coverage doubled. Categorising over a billion products into 5,000+ Google taxonomy categories from text (title, description, tags, vendor) with hashed features and logistic regression using Kesler's construction, evaluated with hierarchical metrics. Source: [article](https://shopify.engineering/using-rich-image-text-data-categorize-products) · [article](https://shopify.engineering/categorizing-products-at-scale)
- **Amazon — Predict coordinates of delivery location (2021)** — Exact delivery spots from noisy GPS: candidate points come from clusters of past drop-offs and map data, and a pairwise random-forest ranker picks the best; lower error than centroid and kernel-density baselines in New York and Washington. Source: [article](https://www.amazon.science/blog/using-learning-to-rank-to-precisely-locate-where-to-deliver-packages)
- **PayPal — Predict declined transactions (2021)** — Predicting issuer declines to raise card authorisation rates: features on card type, merchandise, timing and the card's approval history feed a model, and predicted declines are handled before the request is sent. Source: [article](https://medium.com/paypal-tech/using-machine-learning-to-improve-payment-authorization-rates-bc3b2cbf4999)
- **Slack — Predict Slack connect invites (2021)** — Is an email address a colleague or an outsider? A rule on how often each domain appears among team members by role, with a tunable threshold, kept eventually consistent in Vitess, decides whether to suggest an invite or a shared channel; a heuristic, not a trained model. Source: [article](https://slack.engineering/email-classification/)
- **DoorDash — Deliver orders on time (2021)** — The dispatch system: ML predictions (preparation time, travel time, driver acceptance) feed an optimiser that assigns orders to drivers across the marketplace, with continuous experiments to improve it. Source: [article](https://careersatdoordash.com/blog/using-ml-and-optimization-to-solve-doordashs-dispatch-problem/)
- **Lifen — Recognize PDF layout (2021)** — Fast layout detection for medical PDFs: most documents carry clean text, so OCR is skipped where possible; words become a graph, each edge gets a should-merge score, and edges are merged in score order into reading-order blocks for downstream language models. Source: [article](https://medium.com/lifen-engineering/fast-graph-based-layout-detection-19fc7ab11b17)
- **Swiggy — Estimate travel distance (2021)** — Predicting two-wheeler travel distance where map services fall short: ground-truth distances are synthesised from noisy GPS trajectories of delivery partners and used as labels and features for a random-forest model over geohash cells. Source: [article](https://bytes.swiggy.com/learning-to-predict-two-wheeler-travel-distance-752d836d741d) ([archived copy](https://web.archive.org/web/2024/https://bytes.swiggy.com/learning-to-predict-two-wheeler-travel-distance-752d836d741d))
- **Google — Correct grammatical errors (2021)** — Grammar correction while typing on a phone: a 20 MB hybrid Transformer-encoder, LSTM-decoder model, quantised and trained by distillation from a cloud model on sentence prefixes, corrects 60 characters in under 22 ms on device. Source: [article](https://research.google/blog/grammar-correction-as-you-type-on-pixel-6/)
- **Nubank — Predict conversions and attract new customers (2021)** — Why prediction is not enough for decisions such as credit limits, interest rates or coupons: the question is how a customer responds to an intervention, which needs randomised trials or natural experiments rather than a conversion model. Source: [article](https://building.nu.com/beyond-prediction-machines/)
- **Scribd — Classify user-uploaded documents (2021)** — Document type (sheet music, text-heavy, comics, tables and others) from page images: SqueezeNet, chosen for accuracy per unit of inference time, classifies four sampled pages, ensembled with metadata; overconfidence reduced by adversarial retraining, over hundreds of millions of documents. User-uploaded documents sorted into a two-level taxonomy: topics discovered by clustering embeddings (t-SNE, HDBSCAN), then supervised text classifiers over key phrases and entities trained with labels grown by active learning; drives browsing and recommendations. Source: [article](https://tech.scribd.com/blog/2021/identifying-document-types.html) · [article](https://tech.scribd.com/blog/2021/categorizing-user-uploaded-documents.html)
- **Mercado Libre — Predict customer engagement and LTV (2021)** — Measuring the long-term effect of retention actions on high-value users predicted to decline: causal inference estimates the lifetime-value gain generated by the interventions. Source: [article](https://medium.com/mercadolibre-tech/causal-inference-estimating-long-term-engagement-fac517929073)
- **Wayfair — Show relevant content to new customers (2021)** — Homepage placements assigned to product messages per customer by a constrained optimisation (a generalised assignment problem) that maximises purchase propensity while meeting marketing targets, solved daily in batches over billions of combinations and served by API. Source: [article](https://www.aboutwayfair.com/careers/tech-blog/share-of-voice-optimization-engine)
- **Microsoft — Classify cloud workload types (2021)** — Detecting which cloud customers are migrating workloads, with few true labels: heuristic rules label the data, and an ML model trained on those labels finds migration workloads so teams can help. Source: [article](https://medium.com/data-science-at-microsoft/how-we-used-ml-and-heuristic-data-labeling-to-help-customers-with-their-cloud-migration-d3af7ff020fc)
- **GitHub — Help users find contribution opportunities (2020)** — Good first issues: classifiers (tf-idf random forest, 1D CNN, RNN) over issue titles and bodies trained on weak labels from curated labels and pull-request patterns, ranked by confidence with an age penalty, inferred daily; about 70% of repositories covered at high precision. Source: [article](https://github.blog/open-source/maintainers/how-we-built-good-first-issues/)
- **Mozilla — Predict the outcome of software tests (2020)** — Which tests to run for a patch: XGBoost over (test, patch) pairs trained on historical regressions across 85,000 test files, with itemset mining and an optimisation to choose the set; 70% fewer test tasks on integration branches. Source: [article](https://hacks.mozilla.org/2020/07/testing-firefox-more-efficiently-with-machine-learning/)
- **Adyen — Predict probability of transaction success (2020)** — No readable copy was found; linked only. Source: [article](https://www.adyen.com/blog/optimizing-payment-conversion-rates-with-contextual-multi-armed-bandits)
- **Lyft — Provide location suggestions (2020)** — Destination prediction when the app opens: candidates are places the rider has travelled to or from before, and a joint self-attention network ranks them for the current session; trained on 16 million rides. Source: [article](https://eng.lyft.com/how-lyft-predicts-your-destination-with-attention-791146b0a439)
- **Twitter — Predict value of ad requests (2020)** — Prioritising ad requests between owned-and-operated inventory and a third-party exchange: a heuristic value score was replaced by a simple ML model predicting each request's value, which raised revenue; the lesson is that simple models in the right place pay off. Source: [article](https://blog.twitter.com/engineering/en_us/topics/insights/2020/using-machine-learning-to-predict-the-value-of-ad-requests) ([archived copy](https://web.archive.org/web/2024/https://blog.twitter.com/engineering/en_us/topics/insights/2020/using-machine-learning-to-predict-the-value-of-ad-requests))
- **Picnic — Predict delivery drop times (2020)** — Predicting drop time (service time per delivery) for vehicle routing: better estimates let each hub trade efficiency against the share of deliveries inside the customer's 20-minute window; now in production in two countries. Source: [article](https://blog.picnic.nl/the-trade-off-between-efficiency-and-being-on-time-optimizing-drop-times-using-machine-learning-d3f6fb1b0f31) ([archived copy](https://web.archive.org/web/2024/https://blog.picnic.nl/the-trade-off-between-efficiency-and-being-on-time-optimizing-drop-times-using-machine-learning-d3f6fb1b0f31))
- **Gojek — Target cross-sell to existing users (2020)** — Cross-selling services in a super-app: after a classifier, matrix factorisation over the user–service matrix (implicit feedback, ALS against SGD) finds non-users most likely to adopt a service; field tests against a random control showed a large uplift. Source: [article](https://www.gojek.io/blog/how-we-built-a-matchmaking-algorithm-to-cross-sell-products) ([archived copy](https://web.archive.org/web/2024/https://www.gojek.io/blog/how-we-built-a-matchmaking-algorithm-to-cross-sell-products))
- **OLX — Detect stolen photos (2020)** — Catching fraudulent ads that reuse stolen photos: a Siamese network trained with triplet loss (easy, semi-hard and hard triplets, transfer learning) embeds images so near-duplicates are found even after edits. Source: [article](https://tech.olx.com/fighting-fraud-with-triplet-loss-86e5f79c7a3e) ([archived copy](https://web.archive.org/web/2024/https://tech.olx.com/fighting-fraud-with-triplet-loss-86e5f79c7a3e))
- **Duolingo — Teaching foreign languages (2020)** — AI throughout a language app: over half a billion daily exercises train models that estimate each learner's recall and each exercise's difficulty (spaced repetition, logistic models) to personalise sessions (a news feature). Source: [article](https://venturebeat.com/ai/how-duolingo-uses-ai-in-every-part-of-its-app/)
- **Firefox — Automatically assign new untriaged bugs (2019)** — New Firefox bugs assigned a product and component by XGBoost over titles, comments and keywords, trained on 100,000+ historical bugs; over 80% precision when confidence exceeds 60%. Source: [article](https://hacks.mozilla.org/2019/04/teaching-machines-to-triage-firefox-bugs/)
- **ZoomInfo — Predict data accuracy (2019)** — A 70–99 accuracy score per business contact from 12 fields (update recency, email verification method, source diversity) by logistic regression and tree models, predicting that email will not bounce and the person still works there; accuracy rose steeply with score on 200,000 records. Source: [article](https://engineering.zoominfo.com/machine-learning-accuracy-scores)
- **Lyft — Predict location of traffic control elements (2019)** — Finding stop signs and traffic signals from anonymised driver telemetry: speed and GPS traces near each intersection become kernel density images, a convolutional network classifies them, and the model trained on San Francisco was tested on Palo Alto. Source: [article](https://eng.lyft.com/detecting-stop-signs-and-traffic-signals-deep-learning-at-lyft-mapping-75bac609c231)
- **Apple — Identify text language (2019)** — Language identification from strings of only 10–50 characters with a character-level bidirectional LSTM; 15–60% fewer errors than the old n-gram models at 40–80% of the size, used by the keyboard and smart replies on device. Source: [article](https://machinelearning.apple.com/research/language-identification-from-very-short-strings)
- **Stitch Fix — Extract information from customer notes (2019)** — Free-text client notes turned into 500-dimensional BERT features that predict which items a stylist will pick, fed into the styling algorithm. Source: [article](https://multithreaded.stitchfix.com/blog/2019/07/15/give-me-jeans/)
- **Lyft — Detect errors in maps (2019)** — Finding map errors from driver localisation: comparing real-time driver traces with OpenStreetMap exposed thousands of road-network errors in cities, fixed to give accurate routes and ETAs, and shared back with the map community. Source: [article](https://eng.lyft.com/how-lyft-creates-hyper-accurate-maps-from-open-source-maps-and-real-time-data-8dcf9abdd46a) ([archived copy](https://web.archive.org/web/2024/https://eng.lyft.com/how-lyft-creates-hyper-accurate-maps-from-open-source-maps-and-real-time-data-8dcf9abdd46a))
- **Wayfair — Model uplift (2019)** — Uplift modelled directly for display-ad targeting: decision trees and random forests that split on the divergence (KL or Euclidean) between treatment and control outcome distributions, compared with two-model and transformed-outcome approaches in backtests and live A/B tests. Source: [article](https://www.aboutwayfair.com/tech-innovation/modeling-uplift-directly-uplift-decision-tree-with-kl-divergence-and-euclidean-distance-as-splitting-criteria)
- **Lyft — Predict rides and driver hours (2019)** — Long-term (up to 52-week) forecasts of rides and driver hours by cohort: each cohort's retention curve is modelled with two functional forms joined smoothly at a knot (a spline), then summed across cohorts. Source: [article](https://eng.lyft.com/making-long-term-forecasts-at-lyft-fac475b3ba52)
- **Netflix — Improve streaming quality (2018)** — Where ML improves streaming quality: predicting network quality, adapting video quality during playback, predictive caching of likely next content, and detecting device anomalies. Source: [article](https://netflixtechblog.com/using-machine-learning-to-improve-streaming-quality-at-netflix-9651263ef09f)
- **Instacart — Optimize food delivery logistics (2017)** — Grocery-delivery logistics seen through GPS data: datashader visualisations of shopper traces reveal accuracy, speed, direction and store-location patterns that guide routing improvements. Source: [article](https://tech.instacart.com/space-time-and-groceries-a315925acf3a)
- **Airbnb — Predict Value of Homes (2017)** — Predicting the lifetime value of listings: a machine-learning workflow (feature engineering, pipelines, automated model selection) turns prototypes into production models faster. Source: [article](https://medium.com/airbnb-engineering/using-machine-learning-to-predict-value-of-homes-on-airbnb-9272d3d4739d)
- **Booking.com — 150 Successful Machine Learning Models (2019)** — Lessons from about 150 customer-facing models at a travel site: offline accuracy did not predict business gains, so every model is judged by randomised experiment; added latency measurably cost conversion; problem framing mattered most (a paper summary). Source: [article](https://blog.acolyer.org/2019/10/07/150-successful-machine-learning-models/)
- **Chicisimo — Grow User base using vertical ML approach (2019)** — A fashion outfit-advice app grown to 4 million users: first capturing how people describe their needs, then a data platform that learns fashion needs, then algorithms on top; the app closed in 2020. Source: [article](https://medium.com/hackernoon/how-we-grew-from-0-to-4-million-women-on-our-fashion-app-with-a-vertical-machine-learning-approach-f8b7fc0a89d7)

