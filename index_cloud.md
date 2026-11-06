# Unified Cloud Curriculum: index

Index of `unified_cloud_curriculum.md` (built 2026-11-05 UTC from `cloud-computing.txt`, 13 NPTEL outlines: GCF, CN, ACN, PCS, CSP, EH, CNS, TPMC, FOC, ADS, CCDS, DS, BDC; `cloud-computing2.txt`, 6 computer-architecture outlines: MCA, CAO, CA, ACA, PCA, GPU; `dbms.txt`, 3 database courses: FDB, DBD, IDB; the System Design Primer, the python-patterns collection and the Gang of Four catalogue: SDP, PYP, GOF; and `data-analytics.txt`, 8 new outlines: DAP, AGDS, SDS, DBMS, BDA, ALA, DM, DSAD, the ninth, BDC, being a duplicate), all added 2026-11-06. 21 domains, 268 units, 258 assignments (A<d>.<n>, five questions, key collapsed), 46 prerequisite bridges, 10 capstones. All 452 source cells from 33 courses are cited. D15 (database systems) is printed between D9 and D10; D21, D17, D18 and D19 (data science foundations) between D10 and D11; D20 after D11; D16 (software and system design) after D12; D14 is printed before the capstones (D13), which stay together at the end. Separate from `unified_curriculum.md`; a merge is an open decision (Appendix D of the file).

Bridge units are marked (bridge). Capstones carry no assignment.

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

## D21. On-demand prerequisites for the data-analytics extension: school mathematics, Python, scientific Python (in place of R), proofs and discrete reasoning, graph theory and probability from first principles

- U21.1 Bridge: Python from scratch — types, control flow, functions, recursion, objects, exceptions, generators, testing, NumPy and the floating-point model (bridge)
- U21.2 Bridge: school mathematics through class 12, consolidated — algebra, functions, trigonometry, coordinate and vector geometry, matrices and determinants, calculus, differential equations, linear programming and probability, with numerical methods built from scratch (bridge)
- U21.3 Bridge: scientific Python for data analysis — arrays and broadcasting, data frames, distributions, formulas, random numbers and plotting, each built from scratch before the library is used (this replaces the R programming prerequisite of the Bayesian course) (bridge)
- U21.4 Bridge: proofs and discrete reasoning — logic, sets, counting, direct proof, contrapositive and contradiction, induction, the pigeonhole and double counting, and invariants (bridge)
- U21.5 Bridge: graph theory from scratch — definitions, degrees, paths and connectivity, trees, Eulerian and Hamiltonian graphs, bipartite graphs, planarity, colouring, matchings and representations (bridge)
- U21.6 Bridge: probability from first principles — sample spaces, random variables, expectation, the standard distributions, limit theorems and simulation by inversion, rejection and Monte Carlo (bridge)

## D17. Algorithms and data structures, taught on demand: analysis, divide and conquer, sorting, hashing, trees, amortisation, greedy and dynamic programming, graph search, shortest paths, network flow, tries, B-trees, string matching and hard problems

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

## D18. Applied linear algebra for data and signals: vectors, matrices, eigenvalues, the SVD, least squares, estimation, recommenders, the DFT and OFDM, dynamical systems, clustering, perceptrons, compressive sensing and Markov chains

- U18.1 Bridge: complex numbers, trigonometry and phasors, and the language of vector spaces (bridge)
- U18.2 Introduction to vectors, properties and applications: norms, inner products, angles, orthogonality, projection and Gram–Schmidt
- U18.3 Introduction to matrices and applications: subspaces, rank, circuits, graphs, social networks and traffic flow
- U18.4 Eigenvalue decomposition: properties, diagonalisation, the spectral theorem, PCA and eigenfaces
- U18.5 Singular value decomposition and applications: beamforming in MIMO, dimensionality reduction, rate maximisation and the MUSIC algorithm
- U18.6 Linear regression and least squares: system identification, ridge regression, support vector machines and kernel SVMs
- U18.7 Optimal linear MMSE estimation: the MMSE receiver, market prediction and forecasting, and ARMA models
- U18.8 Data analytics with matrices: recommender systems, user rating prediction, data completion and the Netflix problem
- U18.9 The DFT and the FFT matrix, OFDM and SC-FDMA: structure, properties and signal processing in OFDM systems
- U18.10 Dynamical systems: modelling robots and chemical plants, autonomous linear systems and systems with inputs and outputs
- U18.11 Unsupervised learning: centroid-based clustering, probabilistic model-based clustering and the EM algorithm
- U18.12 The linear perceptron, compressive sensing and orthogonal matching pursuit: sparse signal estimation
- U18.13 Discrete-time Markov chains and operations research: supply chains, forecasting, and resource and inventory management

## D19. Statistics, data mining and Bayesian analysis: from probability and sampling to testing, regression, clustering, trees, association rules, classification, Bayesian inference, MCMC and model comparison

- U19.1 Bridge: calculus, counting and matrices for statistics (bridge)
- U19.2 Introduction to data analytics and Python fundamentals: the analytics workflow, data types, descriptive statistics and visualisation
- U19.3 Probability and random variables: events, conditional probability, Bayes' rule, distributions, expectation and the limit theorems
- U19.4 Sampling and sampling distributions: the standard error, the t, chi-square and F distributions, confidence intervals and the bootstrap
- U19.5 Hypothesis testing: null and alternative, p-values, errors and power, one- and two-sided tests, and multiple comparisons
- U19.6 Two-sample testing and the analysis of variance: pooled and Welch t tests, paired tests, one-way and two-way ANOVA
- U19.7 Linear regression and multiple regression: least squares, inference, diagnostics and model building
- U19.8 Maximum likelihood, logistic regression and the ROC curve
- U19.9 The chi-square test and cluster analysis: goodness of fit, independence, hierarchical and k-means clustering, density-based clustering and outlier detection
- U19.10 Classification and regression trees (CART): impurity, splitting, overfitting and pruning
- U19.11 Data mining: introduction, data preprocessing, association rule mining and classification basics
- U19.12 Classification: decision trees, the Bayes classifier, nearest neighbours, support vector machines and kernel machines
- U19.13 Evaluation, visualisation, sequence mining and case studies
- U19.14 Bayesian inference: Bayes' theorem, the likelihood, prior and posterior, analytical methods and grid approximation
- U19.15 Markov chain Monte Carlo, Hamiltonian Monte Carlo, the brms package and Stan, taught in Python with PyMC and Bambi
- U19.16 Bayesian regression and hierarchical models
- U19.17 Model comparison, mixture models and multinomial processing trees

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
