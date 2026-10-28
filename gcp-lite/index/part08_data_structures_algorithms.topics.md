# Part 08 · Data Structures, Algorithms & Computational Complexity · TOPIC LIST

Rules and directives for this part: `index/part08_data_structures_algorithms.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Data Structures, Algorithms & Computational Complexity

### Analysis

- **Correctness**
  - Loop invariants: initialization, maintenance, termination
  - Correctness proofs for insertion sort and binary search; the binary search invariant that a target, if present, lies in the window [lo, hi), with hi − lo shrinking at every step so termination follows, and the mid update that moves lo to mid + 1 or hi to mid
- **Cost models and asymptotics**
  - The RAM model of computation
  - O, Ω, Θ and o defined with quantifiers and proved from the definitions
  - Big-O in practice: why a hash lookup beats a linear scan; why database indexes matter
  - Worst-case, average-case and amortized cost
- **Recurrences and divide and conquer**
  - Merge sort and T(n) = 2T(n/2) + Θ(n)
  - Solving recurrences by recursion tree, substitution, the master theorem and the Akra–Bazzi method for unequal subproblem sizes, with the exponent p fixed by Σ aᵢ·bᵢᵖ = 1
  - Karatsuba multiplication
  - Strassen matrix multiplication: seven half-size products instead of eight; T(n) = 7T(n/2) + Θ(n²) gives O(n^log₂7), about n^2.81; the extra additions and constant factor that set the crossover with the naive method
  - The Ω(n log n) comparison-sorting lower bound by decision trees; counting sort, radix sort and bucket sort (expected linear time for keys uniform on an interval); counting sort's prefix-sum placement, which is stable and runs in O(n + k) for keys in 0 to k − 1; LSD radix sort as d stable counting passes costing O(d(n + b)) for d digits in base b; and why these sorts do not contradict the Ω(n log n) bound, since they use key values, not only comparisons
- **Design paradigms and their proof techniques**
  - Brute force, then the reduction of the search space that makes it feasible: pruning, memoization, and meet in the middle, which splits the input so that each half is enumerated in about 2^(n/2) steps
  - Divide and conquer, proved by induction on the input size, with the recurrence giving the bound
  - Greedy, proved by an exchange argument showing that the greedy choice extends to an optimal solution
  - Dynamic programming, proved by optimal substructure and a recurrence over a state space, with cost equal to the number of states times the work per state
  - Backtracking and branch and bound, pruning any subtree whose lower bound from a relaxation cannot beat the best solution found
  - Randomized algorithms, with expected cost by linearity of expectation
  - Approximation, with a ratio proved against a lower bound on the optimum
  - Reduction, proving that one problem is at least as hard as another, the basis of hardness proofs
- **Differential testing**: run an implementation against a trusted reference (a brute-force version or a library) on random and adversarial inputs from a seeded generator, compare outputs exactly or within a stated tolerance, and shrink the first disagreement to a minimal failing input; the reference must not share the implementation's assumptions, and every failure reports its seed so that it can be replayed

### Linear structures and techniques

- Arrays and dynamic arrays; amortized O(1) append by the aggregate, accounting and potential methods
- Two pointers, prefix sums and sliding windows
- Linked lists (singly and doubly)
- Stacks, queues, deques and bags
- Ring buffers (circular arrays): head and tail with modulo indexing, full versus empty, overwrite-or-reject policy, single-producer single-consumer safety
- Recursion and backtracking
- **Clever linear-time problems**: the maximum-sum subarray in one pass; a local minimum in a 1-D array by binary search and in a 2-D array by divide and conquer; range-minimum queries; the majority element by the pairing (Boyer–Moore) argument
- **Monotonic stacks and deques**: next-greater element in O(n) with a stack of indices whose values decrease, sliding-window maximum in O(n) with a deque of indices whose values decrease, and the aggregate argument that each index is pushed and popped at most once; the two-pointer window with a count map for the longest substring with at most k distinct characters

### Hashing

- Hash tables with separate chaining: expected O(1 + α) under simple uniform hashing
- Open addressing and the load factor; resizing
- Universal hashing
- Symbol tables
- Caches: LRU (hash map plus doubly linked list) and LFU

### Trees and heaps

- Binary trees and traversals
- Binary search trees; balanced trees (red-black or AVL) and the O(log n) height proof
- B-trees as disk-oriented balanced trees; search by binary search inside each node and descent between separator keys, insertion that splits a full node at its median key and pushes the median up (height grows only at the root), and deletion that borrows from a sibling or merges with one when a node falls below half full, with the root's removal shrinking the height by one
- Binary heaps, heapsort and priority queues with decrease-key
- Union–find with union by rank and path compression; the amortized bound O(α(n)) per operation, where α is the inverse Ackermann function, proved with a potential function over ranks and the path-compression levels
- Tries
- Range structures: Fenwick trees, segment trees, sparse tables
- Fibonacci heaps and van Emde Boas trees (as ideas)
- **Augmented trees**: a balanced tree whose nodes store subtree sizes, so that select(i) and rank(x) take O(log n); an interval tree keyed by the low endpoint, with the maximum high endpoint kept in each subtree, so that one overlapping interval is found in O(log n) and all k overlaps are reported in O(k log n); the augmentation theorem that a red-black tree can carry any extra field that a node can recompute from itself and its children in O(1) per rotation

### Sorting, searching and strings

- Insertion sort, merge sort, randomized quicksort (expected O(n log n) by indicator variables), heapsort; insertion sort's loop invariant that the prefix is sorted, Θ(n²) time on reversed input, Θ(n) time on sorted input, and its adaptivity, which makes it the finisher for short runs in hybrid sorts
- Stable versus unstable sorts; strict weak orderings for comparators
- Binary search and binary search on a predicate; checking hand-written versions against `bisect` and `sorted`
- Randomized selection; peak finding
- External merge sort with a loser tree
- String matching: KMP; Rabin–Karp with a rolling hash (expected O(n + m), confirm candidates byte by byte)
- Content-defined chunking with rolling hashes (rsync, deduplicating backups)
- Suffix arrays and suffix automata
- **Order statistics**: the i-th smallest element by randomized quickselect in expected linear time; median of medians for worst-case linear time; approximate median

### Graph algorithms

- Adjacency lists versus matrices and their costs
- Breadth-first search and its unweighted shortest-path proof; 0-1 BFS; as the weighted case, edge weights in {0, 1} let a deque replace the priority queue, with a weight-0 edge pushed to the front and a weight-1 edge to the back, giving O(V + E) time and a deque that holds at most two distance values at once
- Depth-first search, edge classification, topological sort and cycle detection
- Strongly connected components; Kosaraju's two DFS passes (finishing order on the graph, then DFS on the transpose in decreasing finish time) and Tarjan's single pass with low-link values, both O(V + E), and the condensation graph, which is a DAG
- Dijkstra's algorithm, its correctness proof and failure on negative edges
- Bellman–Ford and negative cycles (the basis of distance-vector routing); the Bellman equation d(v) = min over edges (u, v) of d(u) + w(u, v) as the fixed point that relaxation iterates, with V − 1 rounds of relaxing every edge giving shortest paths when no negative cycle is reachable from the source, and a V-th round that still relaxes an edge revealing one; O(VE) time
- All-pairs shortest paths by Floyd–Warshall: dynamic programming over the highest allowed intermediate vertex; O(V³) time and O(V²) space; a negative diagonal entry reveals a negative cycle; compared with V runs of Dijkstra on non-negative weights
- Minimum spanning trees by the cut property: Kruskal and Prim; the cycle property as the exchange argument (with distinct weights, the heaviest edge of any cycle lies in no minimum spanning tree), Kruskal's sort then union-find in O(E log E), and Prim's heap-driven growth from one vertex in O(E log V)
- Maximum flow and minimum cut: Ford–Fulkerson, Edmonds–Karp, the max-flow min-cut theorem
- Depth-first search trees: tree, back, forward and cross edges; articulation points, bridges and biconnected components by low-link values
- **Bipartite matching**: maximum matching reduces to max flow with unit capacities, and augmenting paths find it one path at a time, each flipping the matched and unmatched edges along its length; Hall's theorem, under which a bipartite graph has a matching saturating one side if and only if every subset S of that side has at least |S| neighbours; König's theorem that the maximum matching size equals the minimum vertex cover in a bipartite graph; and Hopcroft–Karp, which finds a maximum matching in O(E√V) by finding a maximal set of vertex-disjoint shortest augmenting paths in each phase, with O(√V) phases
- **Social-graph data structures**: adjacency lists stored as sorted arrays of neighbour IDs, so that the mutual neighbours of two users come from one merge in O(d₁ + d₂) time; fan-out on write, which copies each post into every follower's timeline when it is written, versus fan-out on read, which assembles the timeline when it is read; the skew of follower counts, a heavy-tailed degree distribution in which a celebrity's follower list is too large to fan out and is merged at read time instead; and set intersection by hash set or bitset when the lists are dense

### Greedy algorithms and dynamic programming

- The greedy-choice property and exchange arguments: interval scheduling, Huffman coding
- Dynamic programming: optimal substructure and overlapping subproblems
- Edit distance and sequence alignment; 0/1 knapsack; longest common subsequence; longest increasing subsequence; shortest paths in a DAG
- Query-planner join-order search as dynamic programming; System R's dynamic programming over subsets of relations, whose cost grows exponentially with the number of joins, and the genetic query optimizer (GEQO) that PostgreSQL switches to above `geqo_threshold` joins (default 12), searching join orders as permutations with crossover and mutation under a fixed effort budget

### Randomized and probabilistic structures

- Bloom filters and the false-positive rate (1 − e^(−kn/m))^k
- Count-min sketch and its ε–δ guarantee
- HyperLogLog and its standard error of about 1.04/√m
- Reservoir sampling
- Skip lists: probabilistic promotion, expected O(log n) without rebalancing; their use in LevelDB and RocksDB memtables and Redis sorted sets
- **Randomized algorithms**: Las Vegas algorithms, always correct with a random running time (randomized quicksort and randomized select), versus Monte Carlo algorithms, with bounded error and a deterministic running time; Karger's contraction finds a minimum cut with probability at least 2/(n(n − 1)), so about (n²/2)·ln n independent runs drive the failure probability below 1/n; Freivalds' check verifies a matrix product in O(n²) per trial with error at most one half per trial; Markov's and Chernoff's bounds for tail probabilities; Yao's minimax principle, which proves a lower bound for randomized algorithms by fixing a hard input distribution; and the method of conditional expectations for derandomizing an algorithm

### Computability and complexity

- Decision problems; P and NP; polynomial-time reductions
- NP-completeness: SAT, 3-SAT, vertex cover, subset sum, bin packing; the Cook–Levin theorem that SAT is NP-complete, proved by encoding a nondeterministic machine's run on an input as a Boolean formula over tableau variables (cell contents, head positions and states at each step), with a formula of size polynomial in the running time, and the reduction from SAT to 3-SAT by auxiliary variables that split long clauses
- Engineering responses to hardness: approximations and heuristics (first-fit bin packing in cluster schedulers)
- Traveling salesman and set cover: metric TSP by the double-tree 2-approximation and Christofides' 3/2-approximation; greedy set cover within the harmonic number H(n), about ln n, and no polynomial algorithm does better unless P = NP; vertex cover by a maximal matching, taking both endpoints of each matched edge, a 2-approximation because any cover must hit every matched edge; subset sum by trimming a sorted list of reachable sums so that neighbouring values differ by a factor of at most 1 + ε, an FPTAS running in time polynomial in n and 1/ε
- Undecidability of the halting problem by diagonalization; the Turing machine as a finite control with a read–write tape, the universal machine that simulates any other from its encoding, and the diagonal argument that the halting set is not decidable; Rice's theorem, that every non-trivial semantic property of the function a program computes is undecidable, proved by reduction from the halting problem
- Finite automata and regular expressions; context-free grammars and parsers; pushdown automata as a finite control with one stack, recognising exactly the context-free languages
- Weighted finite-state transducers: composition, determinisation and minimisation, Viterbi-style shortest paths; the decoding graph H ∘ C ∘ L ∘ G (HMM states, context dependency, pronunciation lexicon, language model) searched by Viterbi with beam pruning that discards hypotheses whose cost exceeds the best by a fixed beam width; epsilon removal, which replaces epsilon-labelled transitions by direct transitions so that composition does not loop on empty input, and disambiguation symbols, extra labels added to the lexicon so that each output string maps to a unique input path before determinisation
- Universal source coding and Lempel–Ziv: prefix codes and the Kraft inequality; entropy as the limit on lossless rate; Lempel–Ziv phrase parsing that approaches the entropy rate of any stationary ergodic source without knowing its distribution; arithmetic coding as a stream code that maps the whole message to a subinterval of [0, 1) narrowed by each symbol's probability, reaching a code length within two bits of −log₂ P(message)
- Kolmogorov complexity: the length of the shortest program that prints a string; invariance up to an additive constant across universal machines; incompressible strings as the random ones; uncomputability by a diagonal argument like the halting problem's
- Linear block codes: a generator matrix G and a parity-check matrix H over GF(2) with G·Hᵀ = 0; minimum distance d detects d − 1 errors and corrects ⌊(d − 1)/2⌋; syndrome decoding by table lookup, with Hamming(7,4) as the worked case (d = 3, one correction); trellis codes decoded by the Viterbi algorithm over the code's state diagram; convolutional codes as the trellis case, with a shift register whose state and output bits depend on each input bit, and the Viterbi algorithm finding the minimum-metric path through the trellis in O(number of states × n) time, the metric being Hamming distance for hard decisions and squared Euclidean distance for soft ones
- Reducibility: a many-one (Karp) reduction A ≤ B is a computable function f with x ∈ A exactly when f(x) ∈ B, so a decider for B yields a decider for A, and the undecidability of A transfers to B; polynomial-time many-one reductions transfer NP-hardness, and Turing reductions instead query an oracle for the target
- The Church–Turing thesis: every effectively calculable function is computable by a Turing machine; it is a thesis about an informal notion and cannot be proved, and its support is the equivalence of lambda calculus, register machines and the other proposed models, all of which compute the same class of functions
- The polynomial hierarchy: the classes Σₖᵖ and Πₖᵖ defined by k alternating quantifiers over a polynomial-time predicate, with Σ₁ᵖ = NP and Π₁ᵖ = coNP, and the union over k lying inside PSPACE; if Σₖᵖ = Πₖᵖ for some k then the hierarchy collapses to level k, and P = NP would collapse it to P
- Space-bounded computation: L (logarithmic space) ⊆ NL ⊆ P; NL = coNL by the Immerman–Szelepcsényi theorem; Savitch's theorem NSPACE(s) ⊆ DSPACE(s²), by a midpoint search over configuration graphs with recursion depth O(s), each frame holding one configuration of s bits, so that PSPACE = NPSPACE; and TQBF (quantified Boolean formulas) as the canonical PSPACE-complete problem
- Circuit complexity: Boolean circuits of polynomial size as a non-uniform model, with P ⊆ P/poly, and P/poly containing undecidable sets because its advice is unrestricted; AC⁰ (constant depth, unbounded fan-in) and NC (polylogarithmic depth, bounded fan-in); the lower bound that parity is not in AC⁰, proved by Håstad's switching lemma; and the open status of any superpolynomial circuit lower bound for NP
- Probabilistically checkable and interactive proofs: the PCP theorem, NP = PCP[O(log n), O(1)], so every NP statement has a proof that a verifier checks by reading a constant number of proof bits chosen with O(log n) random bits; its gap form gives hardness of approximation, with NP-hardness of satisfying more than a 7/8 + ε fraction of the clauses of a 3-SAT instance, so the random-assignment ratio of 7/8 is optimal unless P = NP; interactive proofs, in which a randomized verifier questions a prover, with IP = PSPACE by the sum-check protocol; and zero-knowledge proofs, in which the verifier learns nothing beyond the truth of the statement

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
- From scratch: Strassen and Floyd–Warshall implemented beside their naive versions, checked on random inputs, with operation counts fitted against n^2.81 and n³
- From scratch: Hopcroft–Karp bipartite matching checked against brute-force matchings on small graphs, with the number of phases recorded against √V
- **Reasoning drills**
  - Infer the target complexity from the input bounds before designing (n ≤ 20, n ≤ 10⁵, n ≤ 10⁹)
  - An exchange-argument or invariant proof for every greedy and dynamic-programming solution written
  - Contest problems solved under time, then re-solved cold a few days later
  - Predict the crossover point between two algorithms, then measure it
  - Predict the solution of a divide-and-conquer recurrence with unequal splits by Akra–Bazzi, then count the operations of the implementation to check it
  - Predict the number of Hopcroft–Karp phases for a generated bipartite graph from its size, then count the phases the implementation runs
  - Derive the failure probability after k independent Karger contractions, then predict the number of runs a stated error bound needs before measuring it
