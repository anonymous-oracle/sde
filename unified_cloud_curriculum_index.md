# Unified Cloud Curriculum: index

Index of `unified_cloud_curriculum.md` (built 2026-11-04 UTC from `cloud-computing.txt`, 13 NPTEL outlines: GCF, CN, ACN, PCS, CSP, EH, CNS, TPMC, FOC, ADS, CCDS, DS, BDC). 13 domains, 138 units, 132 assignments (A<d>.<n>, five questions, key collapsed), 15 prerequisite bridges, 6 capstones. All 154 source cells are cited. Separate from `unified_curriculum.md`; a merge is an open decision (Appendix D of the file).

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

## D10. Cloud storage and databases: relational foundations, distributed file systems, key-value and wide-column stores, in-memory NoSQL and Google Cloud storage

- U10.1 Bridge: the relational model, SQL, indexing and query processing (bridge)
- U10.2 Distributed file systems: the Google File System and HDFS, with erasure coding
- U10.3 Amazon Dynamo and LinkedIn Voldemort: highly available key-value stores
- U10.4 Apache Cassandra: a wide-column store on Dynamo's ring and Bigtable's engine
- U10.5 HBase and Bigtable: sorted wide-column storage over a distributed file system
- U10.6 In-memory key-value stores and the families of NoSQL databases
- U10.7 Google Cloud storage and database options

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

## D12. Cloud operations and machine learning on Google Cloud: observability and reliability engineering, analytics services, managed machine learning and responsible AI

- U12.1 Observability and site reliability engineering: metrics, logs, traces, SLOs and error budgets
- U12.2 Data analytics on Google Cloud: the warehouse, dataflow pipelines and managed clusters
- U12.3 Machine learning on Google Cloud: managed training and prediction, pre-trained APIs and responsible AI

## D13. Capstones

- U13.1 Capstone: a user-space TCP/IP stack over a lossy virtual link
- U13.2 Capstone: a secure channel from your own primitives (never deployed)
- U13.3 Capstone: a replicated, sharded key-value store with fault injection
- U13.4 Capstone: an end-to-end data platform from your own engines
- U13.5 Capstone: a small service on Google Cloud with identity, networking, reliability and cost controls
- U13.6 Capstone: a security programme for a synthetic organisation

## D14 (planned, not yet authored): Computer architecture and parallel hardware

Ingested 2026-11-04 from `cloud-computing2.txt`: 6 computer-architecture outlines (MCA, CAO, CA, ACA, PCA, GPU), 78 cells, all mapped. Details, cell table and open decisions: `claude/cloud_ingest_2_architecture.md`. Each unit below except the capstone will carry an assignment A14.n like the existing ones. Current file totals are unchanged: 138 units, 132 assignments; after authoring, 161 units and 154 assignments.

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
- U14.23 Capstone: a multicore simulator (pipeline, caches, coherence and a NoC) running a parallel kernel (capstone)
