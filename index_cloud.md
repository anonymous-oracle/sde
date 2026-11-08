# Unified Cloud Curriculum: index (merged with the machine-learning curriculum, folded by subject)

Index of `unified_cloud_curriculum.md`, the primary curriculum. Built from the cloud sources (`cloud-computing.txt`, `cloud-computing2.txt`, `dbms.txt`, the System Design Primer, python-patterns and the Gang of Four catalogue, `data-analytics.txt`, `software-engineering.txt`) on 2026-11-05 and 2026-11-06, and, on 2026-11-06, merged completely with the earlier machine-learning curriculum (`unified_curriculum.md`, from `nptel.txt` and `iit-genai.md`) and folded in by subject: its pre-calculus and discrete mathematics are inside D21, its algorithms and complexity inside D17, its linear algebra inside D18, its probability and statistics inside D19; calculus and analysis form D24, optimization D25, and machine learning, reinforcement learning, deep learning, language models, generative models, retrieval and agents, evaluation and safety, and ML systems are D26 to D33 at the start of Part E; its capstones are U13.11 to U13.17. 33 domains, 450 units, 433 assignments (A<d>.<n>, five questions, key collapsed), 150 prerequisite bridges and on-demand units that other units call on, 17 capstones. All 1,042 source cells from 79 courses are cited (478 cloud, 564 machine-learning). The merged units are never read as a block: each cloud unit that needs one carries an *On demand* line, and each merged unit that is called on starts with a *Bridge for:* line (map in Appendix H.3 of the file). Cloud identifiers did not change. Where a domain holds both cloud and merged units, the units are printed on a reading ladder (in the domain introduction), so unit numbers inside such a domain are not in print order: D17, D18, D19 and D21 list their units below in the order printed. D15 (database systems) is printed between D9 and D10; D21, D24, D17, D23, D18, D19 and D25 between D10 and Part E; D26 to D33 before D11; D20 after D11; D22 and D16 after D12; D14 before the capstones (D13), which stay together at the end. The old identifiers of the merged units are shown as (old …); the full map is Appendix H.2.

Bridge units are marked (bridge). Merged units are marked (merged, on demand). Capstones carry no assignment.

# Part A. Foundations: the cloud, networks and cloud compute

## D1. Orientation: the cloud, Google Cloud Platform and the lab protocol

- U1.1 What the cloud is: history, service models, deployment models and economics
- U1.2 Bridge: Linux shell, scripting, Python for systems work, regular expressions and Git (bridge)
- U1.3 Google Cloud Platform core infrastructure and the lab protocol

## D2. Computer networks and the Internet protocols

- U2.1 Bridge: probability, random processes and queueing for networks (bridge)
- U2.2 Introduction to computer networks: history, circuit switching and packet switching
- U2.3 The TCP/IP protocol stack: layering, encapsulation, bytes and sockets
- U2.4 Application layer services: HTTP, FTP, email and DNS
- U2.5 Transport layer I: connection establishment and closure, reliable transfer and flow control
- U2.6 Transport layer II: TCP, congestion control and fairness
- U2.7 Bridge: graph algorithms for routing — shortest paths, spanning trees and distributed relaxation (bridge)
- U2.8 Network layer: IP addressing, IPv6, NAT, DHCP and ICMP
- U2.9 IP routing: intra-domain protocols and inter-domain routing with BGP
- U2.10 IP services: ARP and SNMP
- U2.11 Bridge: coding theory — GF(2), polynomial division, CRC and Hamming codes (bridge)
- U2.12 Data link layer: forwarding, flow control, error control, switching and spanning tree
- U2.13 Media access control: channel access protocols and framing
- U2.14 End-to-end principles of computer networks and the future Internet

## D3. Advanced networking: high-performance routers, QoS, SDN, NFV, P4, data centers and information-centric networking

- U3.1 Bridge: lookup data structures — tries, hashing and Bloom filters (bridge)
- U3.2 Bridge: bipartite matching, Hall's theorem and Birkhoff–von Neumann decomposition (bridge)
- U3.3 High-performance switching and routing: router architecture, switch fabrics and performance
- U3.4 IP address lookup: algorithms, optimisation and hardware implementation
- U3.5 Packet classification
- U3.6 DiffServ, quality of service, traffic policing and shaping
- U3.7 Network softwarization: software-defined networking, controllers, southbound and northbound interfaces
- U3.8 Network function virtualization: architecture and concepts
- U3.9 Programmable networks: P4, SmartNICs and P4 switches
- U3.10 Data center networking: topologies, routing, transport and container network interfaces
- U3.11 Content distribution on the Internet and architectures for information-centric networking
- U3.12 NDN content naming, routing, caching and security

## D4. Cloud compute: virtualization, containers, cloud networks and Google Cloud compute services

- U4.1 Bridge: operating systems and computer architecture for virtualization (bridge)
- U4.2 Virtualization: models, types and the Popek–Goldberg theorem
- U4.3 Hotspot mitigation and live VM migration
- U4.4 Containers, Docker, Linux containers, networking of VMs, Kubernetes and edge computing
- U4.5 Bridge: network flows and linear programming (bridge)
- U4.6 Network virtualization and geo-distributed clouds: SDN in the data center, VL2, NVP, MPLS, B4 and SWAN
- U4.7 Google Cloud compute services: Compute Engine, App Engine, containers and Kubernetes, Cloud Functions
- U4.8 Cloud networking on GCP: VPC networks, subnets, firewall rules, load balancing and hybrid connectivity

# Part B. Cryptography, security, risk and privacy

## D5. Cryptography: from classical ciphers to provable security, public-key systems, advanced primitives and post-quantum cryptography

- U5.1 Bridge: probability, entropy and asymptotics for cryptography (bridge)
- U5.2 Bridge: integers modulo n — divisibility, gcd, extended Euclid, inverses and fast exponentiation
- U5.3 Introduction to cryptography and classical ciphers, cryptanalysis and perfect secrecy
- U5.4 Block ciphers: design principles, SPN, Feistel networks, DES, Triple DES and modes of operation
- U5.5 Bridge: groups, rings, fields, finite fields and linear algebra over them
- U5.6 Stream ciphers: one-time pad, autokey, LFSRs, Berlekamp–Massey and modern stream ciphers
- U5.7 The Advanced Encryption Standard (Rijndael)
- U5.8 Bridge: computational complexity, one-way functions and the reduction method (bridge)
- U5.9 Provable security for symmetric encryption: computational security, PRGs, PRFs and CPA security
- U5.10 Cryptographic hash functions: Merkle–Damgård, Davies–Meyer, SHA-2, SHA-3, birthday attacks and the random-oracle model
- U5.11 Message authentication and authenticated encryption: MACs, HMAC, CBC-MAC, universal hashing and AEAD
- U5.12 Bridge: number theory for public-key cryptography — Fermat, Euler, CRT, quadratic residues, Legendre and Jacobi symbols, primality testing and factoring (bridge)
- U5.13 Key exchange, cyclic groups and the Diffie–Hellman family: discrete log, CDH, DDH and the attacks on them
- U5.14 Public-key encryption I: RSA, Rabin and ElGamal, generalized ElGamal and their textbook attacks
- U5.15 Elliptic curves: groups over the reals and finite fields, scalar multiplication, ECDH and the elliptic-curve discrete log
- U5.16 Public-key encryption II: IND-CPA and IND-CCA security, the KEM–DEM paradigm and CCA-secure hybrid ciphers
- U5.17 Digital signatures: RSA signatures, Schnorr, DSA and ECDSA, group and ring signatures, hash-based signatures
- U5.18 Key management, certificates and PKI, TLS/SSL and PGP: the protocols that assemble the primitives
- U5.19 Cryptanalysis I: attack models, time–memory trade-off, differential and linear cryptanalysis
- U5.20 Cryptanalysis II: attacks on stream ciphers and side-channel attacks
- U5.21 Secret sharing and secure multiparty computation
- U5.22 Broadcast, identity-based, attribute-based and functional encryption; bilinear pairings
- U5.23 Homomorphic encryption: partially, somewhat and fully homomorphic schemes
- U5.24 Zero-knowledge proofs and interactive protocols
- U5.25 Quantum and post-quantum cryptography

## D6. Ethical hacking and technical security: reconnaissance, scanning, system and network attacks, web, memory safety and hardware

- U6.1 Foundations of security and ethical hacking: CIA, threats, attack trees, ethics and rules of engagement
- U6.2 Laboratory set-up and reconnaissance: attacker and victim machines, open-source intelligence, DNS and the nmap host-discovery stage
- U6.3 Scanning and vulnerability assessment: port scanning, nmap and Nessus, CVE, CWE and CVSS, and the secure hacking environment
- U6.4 System hacking, malware and link-layer attacks: passwords, privilege escalation, malware taxonomy and analysis, ARP spoofing and MAC attacks
- U6.5 Network attacks and defences: sniffing, session attacks, denial of service, DNS and email security
- U6.6 Steganography, biometric authentication and social engineering
- U6.7 Web application attacks and secure coding: HTTP state, SQL injection, XSS, CSRF, authentication and access control
- U6.8 Exploitation frameworks and memory safety: Metasploit as a lab tool, memory-corruption models, and mitigations
- U6.9 Hardware security: side channels in hardware, physical unclonable functions and hardware trojans
- U6.10 Case studies: attack scenarios, their root causes and remedies

## D7. Security operations frameworks and cloud security: defence technology, ATT&CK, kill chains, D3FEND, STIG, STIX/TAXII and cloud IAM

- U7.1 Defence technologies and access control: firewalls, intrusion detection, access-control models and active defence
- U7.2 Knowing your attacker: the MITRE ATT&CK framework
- U7.3 Cyber kill chains: the Lockheed Martin Cyber Kill Chain and the Unified Kill Chain
- U7.4 Defending yourself: the MITRE D3FEND framework
- U7.5 Securing your configurations: STIG benchmarking
- U7.6 Sharing threat intelligence: STIX and TAXII
- U7.7 Cloud security and identity: APIs, IAM, service accounts, keys and the shared-responsibility model

## D8. Governance, risk, resilience and privacy

- U8.1 Security posture, governance, risk and compliance and maturity
- U8.2 Bridge: quantitative risk — frequency and severity models, Monte Carlo loss exceedance, Bayesian updating and decision under uncertainty (bridge)
- U8.3 Cyber security risk management: identification, assessment, control and treatment
- U8.4 Contingency planning and cyber crisis management: incident response, disaster recovery and business continuity
- U8.5 Cyber resilience assessment
- U8.6 Cyber security policy formulation
- U8.7 Foundations of privacy: concepts, theories and measurement
- U8.8 Anonymity and privacy-enhancing technologies: re-identification, k-anonymity, differential privacy and anonymous communication
- U8.9 Privacy regulation: GDPR in Europe, privacy in India (DPDP, Aadhaar) and breach duties
- U8.10 Information privacy: economics and strategy

# Part C. Distributed systems, storage and databases

## D9. Distributed systems: models, randomised and peer-to-peer algorithms, time, coordination, consensus, consistency, transactions, recovery and blockchains

- U9.1 Bridge: models of distributed computation, partial orders and the DSim simulator
- U9.2 Bridge: tail bounds, balls into bins and randomised-algorithm analysis
- U9.3 Epidemic and gossip-based algorithms
- U9.4 Unstructured peer-to-peer systems: Napster, Gnutella, FastTrack and BitTorrent
- U9.5 Distributed hash tables: Chord, Pastry and Kelips
- U9.6 Time, clocks and causality: synchronisation, Lamport clocks and vector clocks
- U9.7 Global state and termination detection: the Chandy–Lamport snapshot
- U9.8 Distributed mutual exclusion: permission-based, quorum-based and token-based algorithms
- U9.9 Distributed deadlock detection and distributed shared memory
- U9.10 Leader election: rings, the bully algorithm and their industry use
- U9.11 Distributed minimum spanning tree: the Gallager–Humblet–Spira algorithm
- U9.12 Agreement and consensus, and the FLP impossibility result
- U9.13 Byzantine agreement, reliability measures: SLIs, SLOs and SLAs
- U9.14 Replicated state machines: Paxos and Raft
- U9.15 Coordination services in industry: Google Chubby and Apache ZooKeeper
- U9.16 Consistency models and the CAP theorem
- U9.17 Bridge: transactions — ACID, serializability, locking, logging and recovery (bridge)
- U9.18 Distributed transactions: atomic commit, Percolator and Spanner
- U9.19 Failures and recovery: checkpointing, rollback recovery, fault tolerance and self-stabilization
- U9.20 Message ordering, group communication and virtual synchrony
- U9.21 Bitcoin and blockchains
- U9.22 Security in distributed systems and sensor networks

## D15. Database systems: modelling, the relational model and SQL, normalisation, storage and indexing, query processing, transactions and recovery, security, enhanced and distributed models, and NoSQL

- U15.1 Introduction to databases and information systems: concepts, architecture and users
- U15.2 Entity-relationship and enhanced ER modelling: semantic database design
- U15.3 Bridge: sets, relations, functions and first-order logic for the relational model, algebra and calculus (bridge)
- U15.4 The relational model: relations, keys, integrity constraints, updates and the mapping from ER and EER
- U15.5 Relational algebra: basic and additional operators, extended operators and updates
- U15.6 Relational calculus: tuple and domain calculus, safety and Codd's theorem
- U15.7 SQL I: data definition, basic query structure, basic operations, aggregation and grouping
- U15.8 SQL II: nested subqueries and set operations, updates and joins
- U15.9 SQL III: views, triggers, integrity constraints, specifying indexes, embedded SQL and a recap
- U15.10 A commercial case study: IBM DB2, its architecture, data definition and manipulation
- U15.11 Functional dependencies: keys, inference, closure, covers and the anomalies they cause
- U15.12 Normal forms: 1NF, 2NF, 3NF and BCNF, lossless decomposition and dependency preservation
- U15.13 Multivalued, join and inclusion dependencies: fourth and fifth normal forms and other dependencies
- U15.14 Bridge: the external-memory model, disks and the cost of sorting (bridge)
- U15.15 Storage structures and physical design: devices, buffering, file organisation and hashing
- U15.16 Indexing: primary, clustering, secondary and multilevel indexes, ISAM, B-trees and B+-trees
- U15.17 Query processing: selection, sorting, projection and the join algorithms
- U15.18 Query optimisation: equivalent expressions, join ordering, size estimation and semantic optimisation
- U15.19 Bridge: directed graphs, cycles, topological order and partial orders for schedules, deadlocks and timestamps (bridge)
- U15.20 Transactions: OLTP, concurrency problems, the ACID properties and transaction states
- U15.21 Schedules: conflict and view serializability, recoverability, cascading rollbacks and testing
- U15.22 Concurrency control protocols: locking and two-phase locking, timestamps, multiversioning, multiple granularity and deadlocks
- U15.23 Recovery systems: log-based schemes, deferred and immediate update, shadow paging and ARIES
- U15.24 Database security and authorization: discretionary and mandatory control, multilevel security and statistical databases
- U15.25 Enhanced data models: active, temporal, spatial and multimedia databases
- U15.26 Distributed databases: fragmentation, replication, distributed query processing, concurrency and recovery
- U15.27 NoSQL systems, graph databases and big data

## D10. Cloud storage and databases: relational foundations, distributed file systems, key-value and wide-column stores, in-memory NoSQL and Google Cloud storage

- U10.1 Bridge: the relational model, SQL, indexing and query processing (bridge)
- U10.2 Distributed file systems: the Google File System and HDFS, with erasure coding
- U10.3 Amazon Dynamo and LinkedIn Voldemort: highly available key-value stores
- U10.4 Apache Cassandra: a wide-column store on Dynamo's ring and Bigtable's engine
- U10.5 HBase and Bigtable: sorted wide-column storage over a distributed file system
- U10.6 In-memory key-value stores and the families of NoSQL databases
- U10.7 Google Cloud storage and database options

# Part D. Mathematics and data science foundations: prerequisites, calculus, algorithms, linear algebra, statistics and optimization

## D21. On-demand prerequisites: school mathematics, pre-calculus (functions, trigonometry, complex numbers), Python, scientific Python (in place of R), proofs, discrete mathematics, graph theory and probability from first principles

- U21.1 Bridge: Python from scratch — types, control flow, functions, recursion, objects, exceptions, generators, testing, NumPy and the floating-point model (bridge)
- U21.2 Bridge: school mathematics through class 12, consolidated — algebra, functions, trigonometry, coordinate and vector geometry, matrices and determinants, calculus, differential equations, linear programming and probability, with numerical methods built from scratch (bridge)
- U21.7 Functions, exponentials and logarithms (bridge) (merged, on demand) (old U0.1)
- U21.8 Angles and the trigonometric functions (bridge) (merged, on demand) (old U0.2)
- U21.9 Identities, inverse trigonometric functions, equations, polar coordinates and rotations (bridge) (merged, on demand) (old U0.3)
- U21.10 Complex numbers I: algebra, the plane, polar form, powers and roots (bridge) (merged, on demand) (old U0.4)
- U21.11 Complex numbers II: the complex exponential, Euler's formula, roots of unity and phasors (bridge) (merged, on demand) (old U0.5)
- U21.3 Bridge: scientific Python for data analysis — arrays and broadcasting, data frames, distributions, formulas, random numbers and plotting, each built from scratch before the library is used (this replaces the R programming prerequisite of the Bayesian course) (bridge)
- U21.4 Bridge: proofs and discrete reasoning — logic, sets, counting, direct proof, contrapositive and contradiction, induction, the pigeonhole and double counting, and invariants (bridge)
- U21.12 Logic, proof paradigms and formal languages (bridge) (merged, on demand) (old U1.1)
- U21.13 Counting, generating functions and combinatorics (bridge) (merged, on demand) (old U1.2)
- U21.14 Posets, lattices, Boolean algebra and switching circuits (merged, on demand) (old U1.3)
- U21.5 Bridge: graph theory from scratch — definitions, degrees, paths and connectivity, trees, Eulerian and Hamiltonian graphs, bipartite graphs, planarity, colouring, matchings and representations (bridge)
- U21.15 Graph theory (bridge) (merged, on demand) (old U1.4)
- U21.16 Number theory and cryptography (bridge) (merged, on demand) (old U1.5)
- U21.17 Algebra: finite fields, codes, groups and orbit counting (bridge) (merged, on demand) (old U1.6)
- U21.18 An invitation to mathematics: polynomials, functions, matrices, conservation laws (bridge) (merged, on demand) (old U1.7)
- U21.6 Bridge: probability from first principles — sample spaces, random variables, expectation, the standard distributions, limit theorems and simulation by inversion, rejection and Monte Carlo (bridge)

## D24. Calculus and analysis, taught on demand: single-variable and multivariable calculus, differential equations, dynamical systems, numerical methods, complex analysis and transforms

- U24.1 Numbers, countability, functions, limits and continuity (bridge) (merged, on demand) (old U2.1)
- U24.2 Differentiation and mean value theorems (bridge) (merged, on demand) (old U2.2)
- U24.3 Integration, applications and transcendental functions (bridge) (merged, on demand) (old U2.3)
- U24.4 Taylor expansion, sequences, series and power series (merged, on demand) (old U2.4)
- U24.5 Improper integrals, Gamma and Beta functions, integrals dependent on parameters (bridge) (merged, on demand) (old U2.5)
- U24.6 Functions of several variables, partial derivatives and differentiability (bridge) (merged, on demand) (old U3.1)
- U24.7 Taylor expansion in several variables, maxima, minima and Lagrange multipliers (bridge) (merged, on demand) (old U3.2)
- U24.8 Multiple integrals and their applications (bridge) (merged, on demand) (old U3.3)
- U24.9 Vector calculus: fields, line and surface integrals, Green, Gauss and Stokes (merged, on demand) (old U3.4)
- U24.10 Matrix calculus, Jacobians and Hessians for machine learning (merged, on demand) (old U3.5)
- U24.11 First- and higher-order ordinary differential equations (bridge) (merged, on demand) (old U7.1)
- U24.12 Numerical analysis: iteration, root finding, interpolation and quadrature (merged, on demand) (old U7.2)
- U24.13 Complex variables: analytic functions and complex integration (merged, on demand) (old U7.3)
- U24.14 Series, singularities, residues, real integrals and conformal mapping (merged, on demand) (old U7.4)
- U24.15 Laplace, Z, Fourier and discrete Fourier transforms (bridge) (merged, on demand) (old U7.5)
- U24.16 Mathematical modelling: discrete and continuous dynamical systems (bridge) (merged, on demand) (old U7.6)
- U24.17 ODE theory for dynamical systems: Gronwall, limit sets, invariant sets and chain transitivity (bridge) (merged, on demand) (old U7.7)

## D17. Algorithms and data structures, taught on demand: analysis, divide and conquer, sorting, hashing, trees, amortisation, greedy and dynamic programming, graph search, shortest paths, network flow, tries, B-trees, string matching, hard problems, NP-completeness and approximation algorithms

- U17.1 Bridge: discrete mathematics for algorithm analysis: induction, sums, logarithms, recurrences and probability (bridge)
- U17.2 Introduction to algorithms and their analysis: time complexity, asymptotics, merge sort, recurrences and clever linear-time algorithms (bridge)
- U17.3 Divide and conquer: the master method, quicksort, randomised quicksort, half-majority, multiplication and inversions (bridge)
- U17.4 Heaps, sorting in linear time and order statistics (bridge)
- U17.5 Hashing: hash functions, open addressing and perfect hashing (bridge)
- U17.6 Abstract data types, stacks and queues, range queries and the grid-distance problem (bridge)
- U17.7 Search trees: binary search trees, balancing and red-black trees (bridge)
- U17.8 Augmenting data structures, fixed-universe successor and the van Emde Boas tree, with the geometric primitives (bridge)
- U17.9 Disjoint sets, amortised analysis and more computational geometry (bridge)
- U17.10 Greedy algorithms, dynamic programming, graphs and minimum spanning trees (bridge)
- U17.11 Graph search: breadth-first and depth-first search, bipartiteness, DFS trees and articulation points (bridge)
- U17.12 Single-source shortest paths: Dijkstra, Bellman–Ford and their applications (bridge)
- U17.13 All-pairs shortest paths: Floyd–Warshall and Johnson (bridge)
- U17.14 Flow networks, the Ford–Fulkerson method, and an introduction to computational complexity (bridge)
- U17.15 Bridge: arrays, linked lists, recursion, binary search, the elementary sorts and bit tricks — the floor under D17, built from scratch (bridge)
- U17.16 Tries, B-trees, skip lists and string matching: the lookup structures of routers, databases and search engines (bridge)
- U17.17 Backtracking, branch and bound, exact exponential algorithms, approximation and local search: living with hard problems (bridge)
- U17.18 Review of NP-completeness and the approximation framework (bridge) (merged, on demand) (old U17.1)
- U17.19 Approximation for vertex cover, set cover and the traveling salesman problem (bridge) (merged, on demand) (old U17.2)
- U17.20 Approximation for the knapsack problem and job scheduling (bridge) (merged, on demand) (old U17.3)
- U17.21 Linear programming basics and deterministic rounding (bridge) (merged, on demand) (old U17.4)
- U17.22 Randomized rounding (bridge) (merged, on demand) (old U17.5)
- U17.23 The primal–dual method (bridge) (merged, on demand) (old U17.6)
- U17.24 Semidefinite programming for max cut, and hardness of approximation (bridge) (merged, on demand) (old U17.7)

## D23. Go, taught on demand: the language of the system-design, database-coding and cloud-computing exercises

- U23.1 Bridge: Go for the Python programmer — the toolchain, types, slices, maps, errors and tests (bridge)
- U23.2 Interfaces, composition and generics: building typed containers and replacing the object-oriented bridge (bridge)
- U23.3 Concurrency: goroutines, channels, select, context, sync and the race detector (bridge)
- U23.4 Networked services: `net/http`, handlers and middleware, timeouts, retries, circuit breakers and graceful shutdown (bridge)
- U23.5 Database coding: a write-ahead-logged key-value store, crash recovery and the `database/sql` interface (bridge)
- U23.6 System-design building blocks in Go: rate limiters, consistent hashing, Bloom filters and caches (bridge)
- U23.7 Cloud-native Go: reconciliation loops, leases and fencing, backoff, a twelve-factor service and a container image (bridge)
- U23.8 Testing, benchmarking and profiling Go programs: table tests, fuzzing, the race detector, coverage, benchmarks and `pprof` (bridge)

## D18. Linear algebra, core, abstract, numerical and applied: vectors, matrices, vector spaces, eigenvalues, canonical forms, the SVD, least squares, estimation, recommenders, the DFT and OFDM, dynamical systems, clustering, perceptrons, compressive sensing and Markov chains

- U18.1 Bridge: complex numbers, trigonometry and phasors, and the language of vector spaces (bridge)
- U18.14 Systems of linear equations, matrices, elimination, rank and inverses (bridge) (merged, on demand) (old U4.1)
- U18.2 Introduction to vectors, properties and applications: norms, inner products, angles, orthogonality, projection and Gram–Schmidt
- U18.3 Introduction to matrices and applications: subspaces, rank, circuits, graphs, social networks and traffic flow
- U18.15 Vectors, vector spaces, subspaces, bases and dimension (bridge) (merged, on demand) (old U4.2)
- U18.16 Linear maps, representation by matrices, duality and quotient spaces (bridge) (merged, on demand) (old U4.3)
- U18.17 Inner products, norms, orthogonality, projections and Gram–Schmidt (bridge) (merged, on demand) (old U4.4)
- U18.18 Determinants, multilinear forms and permutations (bridge) (merged, on demand) (old U4.5)
- U18.4 Eigenvalue decomposition: properties, diagonalisation, the spectral theorem, PCA and eigenfaces
- U18.19 Eigenvalues, eigenvectors, similarity and diagonalization (bridge) (merged, on demand) (old U4.6)
- U18.20 Canonical forms: minimal polynomial, invariant subspaces, Jordan and rational forms (bridge) (merged, on demand) (old U4.7)
- U18.21 Spectral theory: normal operators, symmetric matrices, quadratic forms, PSD matrices and kernels (bridge) (merged, on demand) (old U4.8)
- U18.5 Singular value decomposition and applications: beamforming in MIMO, dimensionality reduction, rate maximisation and the MUSIC algorithm
- U18.22 LU, QR, conditioning, SVD, pseudo-inverse and low-rank approximation (bridge) (merged, on demand) (old U4.9)
- U18.23 Least squares, regularized and constrained least squares (bridge) (merged, on demand) (old U4.10)
- U18.6 Linear regression and least squares: system identification, ridge regression, support vector machines and kernel SVMs
- U18.7 Optimal linear MMSE estimation: the MMSE receiver, market prediction and forecasting, and ARMA models
- U18.8 Data analytics with matrices: recommender systems, user rating prediction, data completion and the Netflix problem
- U18.24 Applications of linear algebra: PageRank, sparsity, dynamical systems, Markov chains, signal processing and data analytics (bridge) (merged, on demand) (old U4.11)
- U18.9 The DFT and the FFT matrix, OFDM and SC-FDMA: structure, properties and signal processing in OFDM systems
- U18.10 Dynamical systems: modelling robots and chemical plants, autonomous linear systems and systems with inputs and outputs
- U18.11 Unsupervised learning: centroid-based clustering, probabilistic model-based clustering and the EM algorithm
- U18.12 The linear perceptron, compressive sensing and orthogonal matching pursuit: sparse signal estimation
- U18.13 Discrete-time Markov chains and operations research: supply chains, forecasting, and resource and inventory management

## D19. Probability, statistics, data mining and Bayesian analysis: from probability, random variables and limit theorems to sampling, testing, regression, clustering, trees, association rules, classification, Bayesian inference, MCMC, model comparison and forecasting

- U19.1 Bridge: calculus, counting and matrices for statistics (bridge)
- U19.2 Introduction to data analytics and Python fundamentals: the analytics workflow, data types, descriptive statistics and visualisation
- U19.27 Data, descriptive statistics and measures of association (bridge) (merged, on demand) (old U6.1)
- U19.3 Probability and random variables: events, conditional probability, Bayes' rule, distributions, expectation and the limit theorems
- U19.18 Probability foundations: from events to Bayes' theorem (bridge) (merged, on demand) (old U5.1)
- U19.19 Random variables, distributions and moments (bridge) (merged, on demand) (old U5.2)
- U19.20 Special discrete distributions and the Poisson process (bridge) (merged, on demand) (old U5.3)
- U19.21 Special continuous distributions and the normal distribution (bridge) (merged, on demand) (old U5.4)
- U19.22 Functions of random variables, transformations and order statistics (bridge) (merged, on demand) (old U5.5)
- U19.23 Joint distributions, conditioning, covariance and multivariate normal (bridge) (merged, on demand) (old U5.6)
- U19.24 Limit theorems and concentration inequalities (bridge) (merged, on demand) (old U5.7)
- U19.25 Markov chains, queueing theory and reliability (bridge) (merged, on demand) (old U5.8)
- U19.26 Conditional expectation and martingales (merged, on demand) (old U5.9)
- U19.4 Sampling and sampling distributions: the standard error, the t, chi-square and F distributions, confidence intervals and the bootstrap
- U19.28 Sampling distributions and point estimation (bridge) (merged, on demand) (old U6.2)
- U19.5 Hypothesis testing: null and alternative, p-values, errors and power, one- and two-sided tests, and multiple comparisons
- U19.29 Confidence intervals and hypothesis testing (bridge) (merged, on demand) (old U6.3)
- U19.6 Two-sample testing and the analysis of variance: pooled and Welch t tests, paired tests, one-way and two-way ANOVA
- U19.7 Linear regression and multiple regression: least squares, inference, diagnostics and model building
- U19.30 Correlation, regression and multivariate analysis (bridge) (merged, on demand) (old U6.4)
- U19.8 Maximum likelihood, logistic regression and the ROC curve
- U19.9 The chi-square test and cluster analysis: goodness of fit, independence, hierarchical and k-means clustering, density-based clustering and outlier detection
- U19.10 Classification and regression trees (CART): impurity, splitting, overfitting and pruning
- U19.11 Data mining: introduction, data preprocessing, association rule mining and classification basics
- U19.12 Classification: decision trees, the Bayes classifier, nearest neighbours, support vector machines and kernel machines
- U19.13 Evaluation, visualisation, sequence mining and case studies
- U19.14 Bayesian inference: Bayes' theorem, the likelihood, prior and posterior, analytical methods and grid approximation
- U19.31 Bayesian inference and MCMC (bridge) (merged, on demand) (old U6.5)
- U19.15 Markov chain Monte Carlo, Hamiltonian Monte Carlo, the brms package and Stan, taught in Python with PyMC and Bambi
- U19.16 Bayesian regression and hierarchical models
- U19.17 Model comparison, mixture models and multinomial processing trees
- U19.32 Forecasting with statistical and machine-learning models: hydrology and water-resources applications (merged, on demand) (old U6.6)

## D25. Optimization: Theory, Algorithms and Applications

- U25.1 Optimization problems: formulation, history, transformations and basic facts (merged, on demand) (old U8.1)
- U25.2 Convex sets, cones, polyhedra and separation (bridge) (merged, on demand) (old U8.2)
- U25.3 Convex functions and their calculus (bridge) (merged, on demand) (old U8.3)
- U25.4 Unconstrained optimization theory (merged, on demand) (old U8.4)
- U25.5 Constrained optimization theory: Lagrange, cones, Fritz John and KKT (bridge) (merged, on demand) (old U8.5)
- U25.6 Lagrangian duality, saddle points and minimax (bridge) (merged, on demand) (old U8.6)
- U25.7 Linear programming: simplex, duality, sensitivity and interior-point methods (bridge) (merged, on demand) (old U8.7)
- U25.8 Unconstrained descent methods: line search, gradient, Newton, quasi-Newton, conjugate gradient, trust region (bridge) (merged, on demand) (old U8.8)
- U25.9 Constrained optimization algorithms: QP, projected and reduced gradient, penalty, augmented Lagrangian, SQP (bridge) (merged, on demand) (old U8.9)
- U25.10 First-order methods for ML: stochastic, accelerated, proximal, adaptive, and the dynamical-systems view (bridge) (merged, on demand) (old U8.10)
- U25.11 Conic and structured convex programs: QCQP, SOCP, SDP, geometric programs (merged, on demand) (old U8.11)
- U25.12 Applications of optimization: signal estimation, compressive sensing, radar, big data and finance (bridge) (merged, on demand) (old U8.12)
- U25.13 Non-smooth and difference-of-convex optimization (bridge) (merged, on demand) (old U8.13)
- U25.14 Distributed optimization: graphs, consensus, ADMM and dual decomposition (bridge) (merged, on demand) (old U8.14)
- U25.15 Dynamic optimization and complementarity problems (merged, on demand) (old U8.15)
- U25.16 Stochastic approximation: algorithms, step sizes and the ODE method (bridge) (merged, on demand) (old U8.16)
- U25.17 Convergence rates, stability, two-timescale algorithms and stochastic recursive inclusions (merged, on demand) (old U8.17)

# Part E. Machine learning and AI, big data, scalable data science, cloud operations and system design

## D26. Machine Learning Foundations: Supervised, Unsupervised, Probabilistic, Data Mining and Learning Theory

- U26.0 History of AI, symbolic AI and the machine-learning workflow (merged, on demand) (old U9.0)
- U26.1 What machine learning is: paradigms, data, hypothesis spaces and the statistical framework (bridge) (merged, on demand) (old U9.1)
- U26.2 Model evaluation and selection: bias–variance, validation, tuning and metrics (bridge) (merged, on demand) (old U9.2)
- U26.3 Linear regression and linear classification: estimation, logistic and softmax regression, surrogate losses (bridge) (merged, on demand) (old U9.3)
- U26.4 Regularization and implicit regularization (bridge) (merged, on demand) (old U9.4)
- U26.5 Perceptron, support vector machines and kernel methods (bridge) (merged, on demand) (old U9.5)
- U26.6 Bayes decision theory, density estimation and probabilistic classifiers (bridge) (merged, on demand) (old U9.6)
- U26.7 Decision trees and ensembles: bagging, boosting, random forests (bridge) (merged, on demand) (old U9.7)
- U26.8 Dimensionality reduction and feature learning (bridge) (merged, on demand) (old U9.8)
- U26.9 Clustering, mixture models and the EM algorithm (bridge) (merged, on demand) (old U9.9)
- U26.10 Probabilistic graphical models, hidden Markov models, inference and Gaussian processes (bridge) (merged, on demand) (old U9.10)
- U26.11 Instance-based learning, collaborative filtering and recommendation (bridge) (merged, on demand) (old U9.11)
- U26.12 Data mining: preprocessing, association rules, sequence mining, outliers and case studies (bridge) (merged, on demand) (old U9.12)
- U26.13 Learning theory: PAC, VC dimension, generalization and modern overparametrization (merged, on demand) (old U9.13)
- U26.14 Symbolic and knowledge-based machine learning, tools and cognitive-science influences (merged, on demand) (old U9.14)

## D27. Sequential Decision Making: Bandits and Reinforcement Learning

- U27.1 From batch to online learning: adversarial full-information and bandit settings (merged, on demand) (old U10.1)
- U27.2 Stochastic bandits: regret notions, UCB, KL-UCB and lower bounds (merged, on demand) (old U10.2)
- U27.3 Contextual bandits and pure exploration (merged, on demand) (old U10.3)
- U27.4 Markov decision processes, dynamic programming and temporal-difference learning (bridge) (merged, on demand) (old U10.4)
- U27.5 Policy gradient, actor–critic and proximal policy optimization (merged, on demand) (old U10.5)
- U27.6 Stochastic approximation in reinforcement learning (merged, on demand) (old U10.6)

## D28. Deep Learning Foundations

- U28.1 Perceptron, multilayer networks, activations and loss functions (bridge) (merged, on demand) (old U11.1)
- U28.2 Backpropagation and training deep networks (bridge) (merged, on demand) (old U11.2)
- U28.3 Overfitting, regularization and generalization in deep networks (merged, on demand) (old U11.3)
- U28.4 Convolutional neural networks and image representation (bridge) (merged, on demand) (old U11.4)
- U28.5 Explainable AI for deep models (merged, on demand) (old U11.5)
- U28.6 Segmentation and object detection (merged, on demand) (old U11.6)
- U28.7 Recurrent networks: RNN, LSTM, GRU, backpropagation through time and attention in RNNs (merged, on demand) (old U11.7)
- U28.8 Autoencoders and representation learning (merged, on demand) (old U11.8)

## D29. Natural Language Processing, the Transformer and Large Language Models

- U29.1 NLP foundations and the classical NLP pipeline (merged, on demand) (old U12.1)
- U29.2 Word representations and multilingual embeddings (merged, on demand) (old U12.2)
- U29.3 Attention and the Transformer architecture (bridge) (merged, on demand) (old U12.3)
- U29.4 Pretraining, self-supervised learning and the LLM landscape (merged, on demand) (old U12.4)
- U29.5 Scaling laws, LLM architectures and long context (merged, on demand) (old U12.5)
- U29.6 Decoding strategies and sampling (merged, on demand) (old U12.6)
- U29.7 Prompting: fundamentals, APIs and advanced techniques (merged, on demand) (old U12.7)
- U29.8 Instruction tuning, RLHF and alignment: PPO and DPO (bridge) (merged, on demand) (old U12.8)
- U29.9 Parameter-efficient fine-tuning: LoRA and QLoRA (merged, on demand) (old U12.9)
- U29.10 Prompt optimization, compression and prompt security (merged, on demand) (old U12.10)

## D30. Deep Generative Models

- U30.1 Probabilistic deep generative modelling: foundations and taxonomy (merged, on demand) (old U13.1)
- U30.2 Generative modelling via variational divergence minimization (merged, on demand) (old U13.2)
- U30.3 Generative adversarial networks: formulation, training, WGAN and applications (merged, on demand) (old U13.3)
- U30.4 Variational autoencoders, improvements and VQ-VAE (merged, on demand) (old U13.4)
- U30.5 Autoregressive models (merged, on demand) (old U13.5)
- U30.6 Energy-based and score-based models; Langevin sampling (merged, on demand) (old U13.6)
- U30.7 Denoising diffusion probabilistic models, conditional diffusion and Stable Diffusion (merged, on demand) (old U13.7)
- U30.8 Normalizing flows (gap-fill from the references) (merged, on demand) (old U13.8)

## D31. Retrieval-Augmented Generation and Agentic Systems

- U31.1 Why RAG, RAG architecture and classical retrievers (merged, on demand) (old U14.1)
- U31.2 RAG failure modes, types of RAG and assessment (merged, on demand) (old U14.2)
- U31.3 Sparse retrieval limits and dense representations (bridge) (merged, on demand) (old U14.3)
- U31.4 Learning retrieval-oriented embeddings and choosing an embedding model (merged, on demand) (old U14.4)
- U31.5 Document processing and chunking (merged, on demand) (old U14.5)
- U31.6 Vector databases and indexes: KNN, IVF, PQ, HNSW, FAISS and ChromaDB (bridge) (merged, on demand) (old U14.6)
- U31.7 The retrieval pipeline: bi-encoder, cross-encoder, ColBERT and two-stage retrieval (merged, on demand) (old U14.7)
- U31.8 Production RAG: request shaping, query transformation, routing, security, cost and observability (bridge) (merged, on demand) (old U14.8)
- U31.9 Limits of single-shot RAG and the move to agents (merged, on demand) (old U14.9)
- U31.10 Agent basics, tool calling and orchestration (merged, on demand) (old U14.10)
- U31.11 Planning with ReAct (merged, on demand) (old U14.11)
- U31.12 State machines and LangGraph (merged, on demand) (old U14.12)
- U31.13 Agentic memory (merged, on demand) (old U14.13)
- U31.14 Provenance and citations (merged, on demand) (old U14.14)
- U31.15 Multi-agent architecture summary, error handling and best practices (merged, on demand) (old U14.15)

## D32. Evaluation, Safety and Responsible AI

- U32.1 LLM evaluation: metric architecture and reference-based metrics (bridge) (merged, on demand) (old U15.1)
- U32.2 LLM-as-a-judge and factuality (merged, on demand) (old U15.2)
- U32.3 AI safety foundations and threat models (bridge) (merged, on demand) (old U15.3)
- U32.4 White-box attacks and prompt injection (bridge) (merged, on demand) (old U15.4)
- U32.5 Black-box attacks and the jailbreak taxonomy (merged, on demand) (old U15.5)
- U32.6 Defense, interpretability and ethics (bridge) (merged, on demand) (old U15.6)

## D33. ML Systems, Efficiency and Distributed and Federated Learning

- U33.1 CNN computation and accelerators (bridge) (merged, on demand) (old U16.1)
- U33.2 Parallelism for training, communication and fault tolerance (bridge) (merged, on demand) (old U16.2)
- U33.3 LLM decoding, memory management and serving infrastructure (bridge) (merged, on demand) (old U16.3)
- U33.4 Model compression and quantization (bridge) (merged, on demand) (old U16.4)
- U33.5 Graph neural network inference systems (merged, on demand) (old U16.5)
- U33.6 Federated learning (bridge) (merged, on demand) (old U16.6)

## D11. Big data and cloud analytics: batch, dataflow, messaging, streaming, machine learning at scale and graph processing

- U11.1 Introduction to big data
- U11.2 Enabling technologies for big data: clusters, virtualisation, containers and orchestration
- U11.3 Big data platforms I: Hadoop and the MapReduce model
- U11.4 Big data platforms II: Apache Spark and resilient distributed datasets
- U11.5 Dataflow systems beyond MapReduce: Condor and DryadLINQ
- U11.6 Apache Kafka: the distributed commit log and messaging systems
- U11.7 Stream processing and approximate algorithms: windows, event time and sketches
- U11.8 Bridge: machine-learning foundations for scalable learning (bridge)
- U11.9 Big data applications: machine learning with Spark
- U11.10 Bridge: Markov chains, eigenvectors and PageRank (bridge)
- U11.11 Big data applications: graph processing

## D20. Scalable data science: concentration and optimisation background, memory-efficient data structures, sketches, approximate near neighbours, randomised linear algebra, MapReduce and Spark, and distributed machine learning

- U20.1 Scalable data science: the problem, and the background of concentration inequalities, PCA and SVD, convex optimisation and gradient descent, and supervised learning
- U20.2 Memory-efficient data structures I: hash functions, universal and perfect hash families, Bloom filters, sketches for distinct count and the Misra–Gries sketch
- U20.3 Count-Min and Count sketches, and approximate near-neighbour search: kd-trees, locality-sensitive hashing, MinHash for Jaccard and SimHash
- U20.4 Approximate near neighbours: extensions (multi-probe, b-bit hashing, data-dependent variants) and random projection
- U20.5 Randomised numerical linear algebra: CUR decomposition, sparse and subspace random projection and the kitchen-sink features
- U20.6 MapReduce and related paradigms: programming examples (PageRank, k-means, matrix multiplication), moving computation to the data and the Hadoop ecosystem
- U20.7 Scala and Spark, and distributed machine learning and optimisation: stochastic gradient descent with its proof
- U20.8 Distributed optimisation with ADMM and its applications, distributed clustering and conclusion

## D12. Cloud operations and machine learning on Google Cloud: observability and reliability engineering, analytics services, managed machine learning and responsible AI

- U12.1 Observability and site reliability engineering: metrics, logs, traces, SLOs and error budgets
- U12.2 Data analytics on Google Cloud: the warehouse, dataflow pipelines and managed clusters
- U12.3 Machine learning on Google Cloud: managed training and prediction, pre-trained APIs and responsible AI

## D22. Software engineering: the life cycle, process models, planning and estimation, requirements, formal specification, design (structured and object-oriented), testing, debugging, maintenance, agile methods and reliability

- U22.1 Introduction to software engineering: the need, the challenges, the evolution of the development process, system software engineering and the problems of large-scale development
- U22.2 Software development life cycle and the process models: waterfall, modified waterfall, prototyping, incremental, spiral and the others, compared
- U22.3 Project planning: size metrics, function points, cost estimation with COCOMO and Putnam's model, and staffing patterns
- U22.4 Scheduling, organisation structure, risk management, quality management and configuration management, including the Git object model and the merge algorithm
- U22.5 Software requirements: gathering, analysis, the SRS and its characteristics, functional and non-functional requirements, and informal specification
- U22.6 Formal requirement specification: notations, the axiomatic approach (pre- and postconditions, weakest precondition, invariants) and the algebraic approach (abstract data types)
- U22.7 Software design: basics, characteristics of a good design, modularity, cohesion and coupling, layering and the approaches to design
- U22.8 Function-oriented design: structured analysis and design, data flow diagrams, structure charts, HIPO, Jackson's technique and Warnier–Orr diagrams
- U22.9 Object-oriented analysis and design: the concepts, the UML notation (use cases, class, interaction and state diagrams), the OOAD process, and function-oriented against object-oriented development
- U22.10 Coding and testing I: coding standards, reviews and inspections, the Halstead measures, and unit, integration and system testing
- U22.11 Testing II: black-box and white-box test-case design, coverage criteria, cyclomatic complexity and basis paths
- U22.12 Testing III and debugging: mutation testing, regression, property-based testing, debugging strategies, delta debugging and fault localisation
- U22.13 Software maintenance and its models, and an introduction to agile software development
- U22.14 Software reliability: failure models, reliability growth, fault tolerance and the reliability of redundant software (bridge)

## D16. Software and system design: object-oriented design, design patterns and the system design primer

- U16.1 Bridge: object-oriented programming, UML and design principles for the pattern units (bridge)
- U16.2 Design patterns: the catalogue, its principles, and the creational patterns
- U16.3 Structural patterns: adapter, bridge, composite, decorator, facade, flyweight, proxy, and the layered styles
- U16.4 Behavioral patterns I: responsibility, commands, interpretation, traversal, mediation and memory
- U16.5 Behavioral patterns II: observers, states, strategies, templates and visitors
- U16.6 Testability, fundamental and other patterns, anti-patterns, and the Python view
- U16.7 Object-oriented design exercises: hash map, LRU cache, call center, deck of cards, parking lot and chat
- U16.8 How to approach a system design: the four steps, estimation, and the numbers every engineer carries
- U16.9 Scalability and the front of the system: performance, throughput, DNS, CDN, load balancers, reverse proxies and the application layer
- U16.10 Availability and consistency in practice: CAP choices, consistency patterns, fail-over, replication and the arithmetic of nines
- U16.11 Scaling the data tier: replication, federation, sharding, denormalization, SQL tuning, and choosing between SQL and NoSQL
- U16.12 Caching: layers, key choices, and the four update strategies
- U16.13 Asynchronism, communication and security basics: queues, back pressure, HTTP, TCP and UDP, RPC and REST
- U16.14 Worked designs I: a url shortener (Pastebin) and the Twitter timeline and search
- U16.15 Worked designs II: a web crawler, Mint, a social graph, a key-value cache for a search engine, and sales ranking
- U16.16 Scaling a system from one box to millions of users, real-world architectures, and the reading lists

# Part F. Computer architecture and parallel hardware

## D14. Computer architecture and parallel hardware: digital logic, instruction sets, arithmetic, pipelines and speculation, memory hierarchy, I/O, multiprocessors, coherence and consistency, on-chip networks, GPUs and accelerators, power and reliability

- U14.1 Bridge: binary representation, number systems and digital logic (bridge)
- U14.2 Instruction set architecture: addressing modes, encoding, CISC versus RISC, assembly
- U14.3 Performance evaluation and the quantitative principles of design
- U14.4 Computer arithmetic: IEEE 754 floating point, adders, multipliers and dividers
- U14.5 Processor datapath and control unit design: single-cycle, multi-cycle and microprogrammed
- U14.6 Instruction pipelining: hazards, forwarding, stalls and branch prediction
- U14.7 Instruction-level parallelism: scoreboarding, Tomasulo, speculation, reorder buffer, compiler techniques
- U14.8 Superscalar, multithreading, hyperthreading and SIMD
- U14.9 Memory hierarchy I: cache principles, replacement, write policies, design and optimisation
- U14.10 Virtual memory: page tables, TLBs, protection and the hardware-software boundary
- U14.11 Main memory: DRAM organisation, controllers, address mapping and scheduling
- U14.12 Input-output system design: buses, interrupts, DMA and storage interfaces
- U14.13 Parallel architectures and programming models: shared memory, message passing and data parallel
- U14.14 Cache coherence: snooping, directory protocols, MSI, MESI, Dragon, split-transaction buses, Origin and NUMA-Q
- U14.15 Memory consistency models and synchronisation primitives
- U14.16 On-chip networks and interconnects: topologies, routing, flow control, router microarchitecture, deflection and bufferless routing
- U14.17 GPU architecture: streaming multiprocessors, SIMT execution, warp scheduling and divergence, cache hierarchy, graphics pipeline
- U14.18 GPU programming and optimisation: CUDA, thread mapping, synchronisation, coalescing, reductions, kernel fusion
- U14.19 OpenCL and heterogeneous computing
- U14.20 Domain-specific accelerators and efficient neural-network training and inference
- U14.21 Quality of service for caches and networks on chip, and emerging directions
- U14.22 Low-power design, reliability and hardware security

# Part G. Capstones

## D13. Capstones

- U13.1 Capstone: a user-space TCP/IP stack over a lossy virtual link (capstone)
- U13.2 Capstone: a secure channel from your own primitives (never deployed) (capstone)
- U13.3 Capstone: a replicated, sharded key-value store with fault injection (capstone)
- U13.4 Capstone: an end-to-end data platform from your own engines (capstone)
- U13.5 Capstone: a small service on Google Cloud with identity, networking, reliability and cost controls (capstone)
- U13.6 Capstone: a security programme for a synthetic organisation (capstone)
- U13.7 Capstone: a multicore simulator (pipeline, caches, coherence and a NoC) running a parallel kernel (capstone)
- U13.8 Capstone: a small relational database engine checked against sqlite3 (capstone)
- U13.9 Capstone: a design dossier and a working miniature of a large-scale service (capstone)
- U13.10 Capstone: an analytics pipeline from raw data to a decision, with the statistics, the model, the sketches and the distributed run built from scratch (capstone)
- U13.11 Capstone A: the mathematics of machine learning, end to end (capstone) (old U18.1)
- U13.12 Capstone B: a classical-ML library from scratch (capstone) (old U18.2)
- U13.13 Capstone C: a deep-learning framework from scratch (capstone) (old U18.3)
- U13.14 Capstone D: an LLM application platform (RAG + agents + safety) (capstone) (old U18.4)
- U13.15 Capstone E: generative models (capstone) (old U18.5)
- U13.16 Capstone F: ML systems and efficiency (capstone) (old U18.6)
- U13.17 Final integrated capstone: train, align, compress, serve, evaluate and secure a small language model (capstone) (old U18.7)
