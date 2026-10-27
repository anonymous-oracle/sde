# Part 08 · Data Structures, Algorithms & Computational Complexity · TOPIC LIST

Rules and directives for this part: `index/part08_data_structures_algorithms.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Data Structures, Algorithms & Computational Complexity

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
  - Solving recurrences by recursion tree, substitution, the master theorem and the Akra–Bazzi method for unequal subproblem sizes, with the exponent p fixed by Σ aᵢ·bᵢᵖ = 1
  - Karatsuba multiplication
  - Strassen matrix multiplication: seven half-size products instead of eight; T(n) = 7T(n/2) + Θ(n²) gives O(n^log₂7), about n^2.81; the extra additions and constant factor that set the crossover with the naive method
  - The Ω(n log n) comparison-sorting lower bound by decision trees; counting sort, radix sort and bucket sort (expected linear time for keys uniform on an interval)

### Linear structures and techniques

- Arrays and dynamic arrays; amortized O(1) append by the aggregate, accounting and potential methods
- Two pointers, prefix sums and sliding windows
- Linked lists (singly and doubly)
- Stacks, queues, deques and bags
- Ring buffers (circular arrays): head and tail with modulo indexing, full versus empty, overwrite-or-reject policy, single-producer single-consumer safety
- Recursion and backtracking
- **Clever linear-time problems**: the maximum-sum subarray in one pass; a local minimum in a 1-D array by binary search and in a 2-D array by divide and conquer; range-minimum queries; the majority element by the pairing (Boyer–Moore) argument

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
- **Order statistics**: the i-th smallest element by randomized quickselect in expected linear time; median of medians for worst-case linear time; approximate median

### Graph algorithms

- Adjacency lists versus matrices and their costs
- Breadth-first search and its unweighted shortest-path proof; 0-1 BFS
- Depth-first search, edge classification, topological sort and cycle detection
- Strongly connected components
- Dijkstra's algorithm, its correctness proof and failure on negative edges
- Bellman–Ford and negative cycles (the basis of distance-vector routing)
- All-pairs shortest paths by Floyd–Warshall: dynamic programming over the highest allowed intermediate vertex; O(V³) time and O(V²) space; a negative diagonal entry reveals a negative cycle; compared with V runs of Dijkstra on non-negative weights
- Minimum spanning trees by the cut property: Kruskal and Prim
- Maximum flow and minimum cut: Ford–Fulkerson, Edmonds–Karp, the max-flow min-cut theorem
- Depth-first search trees: tree, back, forward and cross edges; articulation points, bridges and biconnected components by low-link values

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
- Traveling salesman and set cover: metric TSP by the double-tree 2-approximation and Christofides' 3/2-approximation; greedy set cover within the harmonic number H(n), about ln n, and no polynomial algorithm does better unless P = NP
- Undecidability of the halting problem by diagonalization
- Finite automata and regular expressions; context-free grammars and parsers
- Weighted finite-state transducers: composition, determinisation and minimisation, Viterbi-style shortest paths
- Universal source coding and Lempel–Ziv: prefix codes and the Kraft inequality; entropy as the limit on lossless rate; Lempel–Ziv phrase parsing that approaches the entropy rate of any stationary ergodic source without knowing its distribution
- Kolmogorov complexity: the length of the shortest program that prints a string; invariance up to an additive constant across universal machines; incompressible strings as the random ones; uncomputability by a diagonal argument like the halting problem's

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
- **Reasoning drills**
  - Infer the target complexity from the input bounds before designing (n ≤ 20, n ≤ 10⁵, n ≤ 10⁹)
  - An exchange-argument or invariant proof for every greedy and dynamic-programming solution written
  - Contest problems solved under time, then re-solved cold a few days later
  - Predict the crossover point between two algorithms, then measure it
  - Predict the solution of a divide-and-conquer recurrence with unequal splits by Akra–Bazzi, then count the operations of the implementation to check it
