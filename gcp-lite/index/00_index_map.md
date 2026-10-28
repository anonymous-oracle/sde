# Index map: what every file holds

This is the entry file for the split Consolidated Topic Index. Read it first in any session, then `index/00_ingest_progress.md` to see which part is current, then `index/00_learning_method.md` (the single copy of the teaching method), then open only the two files of that part. Everything else stays closed until the learner moves on.

## How to use it in a session

1. Read this file (the map) and `index/00_ingest_progress.md` (current part and each part's status).
2. Read `index/00_learning_method.md` once (about 5,500 tokens). It is the only copy of the teaching method.
3. Open the current part's **rules file** (`.rules.md`, about 400 tokens: that domain's prerequisites, depth bar and capstone) and its **topic list** (`.topics.md`). Together with the method they are about 6,500 to 30,000 tokens; the master index is about 110,000.
4. Teach from the topic list. Do not open other parts, except to look up a prerequisite: use the map below to find which part holds it, and read only that group's section.
5. When the learner has been taught and has passed a part's groups, mark it `done` in the progress file, set the next part as current, and open only that part.
6. A topic that depends on a later part is taught just in time and noted in the learner's record, as the method already says.

## What is in each kind of file

| File | Contents | When to read |
|---|---|---|
| `index/00_index_map.md` | This map: every file, what it holds, its groups and size | Start of every session |
| `index/00_learning_method.md` | The Learning method, kept once: aim and standard, the learner's preferences, how a topic is taught, depth and capstones, lab safety, the problem-solving philosophy | Once per session, and again after any compaction |
| `index/00_ingest_progress.md` | Current part and a status for each part | Start of every session; update at the close of a part |
| `index/partNN_<name>.rules.md` | A pointer to the Learning method, then that domain's prerequisites, depth bar and capstone, which are stated only there (for the case studies, the note on how entries are written) | Once, when a part becomes current |
| `index/partNN_<name>.topics.md` | The topic groups and exercises only, with the original headings and wording | While teaching that part |

The Learning method lives once, in `index/00_learning_method.md`, cut from the master without changes. If a rule must change, change it there only; the rules files hold domain directives and a pointer.

## Other project documents (not part of the split)

| Document | What it holds | When to read |
|---|---|---|
| `Consolidated_Topic_Index_GCP.md` | The master copy of the whole index (about 434 KB). The parts were cut from it; every part except 01 and 25 to 29 has since been extended from gcp/unified-curriculum.md, and Part 03d was added, so they no longer match it line for line | Only to check a part against its source |
| `Exercise Rules` | The rule that separates predictions (read-only) from exercises (written by the learner) | Before setting any prediction or exercise |
| `learn-SKILL.md` | The tutoring skill: diagnose first, one scaffold and one question per turn, hold the line, no hidden answers | Start of a teaching stretch |
| `claude/learning_handoff_and_tracker.md` | The handoff (Part A) and the tracker (Part B) | Resuming after a break |
| `Rust_Track_AI_Infrastructure.md` | The Rust track (21 projects), which starts only after the first two or three Go groups are mastered | When Go is well under way |
| `pending_tracker.md` | The working record of overrides, retries, the resume point and the log. Refreshed 24 Oct 2026 through concept 36. Lives at the repo root as `pending_tracker.md` | Resuming, and when closing a part |

## Parts at a glance

| Part | Domain | Groups | Topic list | Rules file |
|---|---|---|---|---|
| 01 | School-level foundations | 1 | 18 KB | 1.6 KB |
| 02 | Computer Organization & Data Representation | 4 | 8 KB | 1.3 KB |
| 03 | Mathematics, Probability, Statistics, Queueing & Performance Modelling | 11 | 67 KB | 1.6 KB |
| 03b | Calculus, Analysis, Coordinate Geometry & Number Theory | 6 | 36 KB | 1.8 KB |
| 03c | Signals, Systems & Communications | 6 | 21 KB | 1.7 KB |
| 03d | Pure Mathematics: Algebra, Topology, Geometry, Logic & Rigorous Analysis | 9 | 40 KB | 1.8 KB |
| 04 | Problem Solving, Reasoning & Research Method | 10 | 12 KB | 1.5 KB |
| 05 | Programming Languages & Language Theory (part 1 of 3) | 3 | 8 KB | 1.4 KB |
| 06 | Programming Languages & Language Theory (part 2 of 3) | 7 | 26 KB | 1.6 KB |
| 07 | Programming Languages & Language Theory (part 3 of 3) | 5 | 15 KB | 1.4 KB |
| 08 | Data Structures, Algorithms & Computational Complexity | 11 | 20 KB | 1.7 KB |
| 09 | Computer Networking & Web Protocols | 13 | 13 KB | 1.6 KB |
| 10 | Operating Systems & Linux | 9 | 7 KB | 1.5 KB |
| 11 | Software Architecture, APIs, Design Patterns & Clean Architecture | 15 | 18 KB | 1.8 KB |
| 12 | Databases, SQL, Relational Theory & Data Modelling | 12 | 20 KB | 1.8 KB |
| 13 | Distributed Systems & Large-Scale System Design | 14 | 14 KB | 1.8 KB |
| 14 | Security, Cryptography, Privacy & Compliance | 21 | 45 KB | 2.0 KB |
| 15 | Software Delivery & Version Control | 4 | 4 KB | 1.2 KB |
| 16 | Cloud Computing Core: Virtualization, Well-Architected, Economics & IAM | 7 | 7 KB | 1.6 KB |
| 17 | The Architect's Practice: Decisions, Strategy & Career | 10 | 5 KB | 1.6 KB |
| 18 | DevOps & SRE: Docker, Kubernetes, NGINX, CI/CD, Infrastructure as Code, Observability | 8 | 16 KB | 1.6 KB |
| 19 | Machine Learning, MLOps & Production ML System Design | 11 | 87 KB | 2.1 KB |
| 19b | Speech & ASR, Computer Vision, Information Retrieval & NLP Toolkits | 7 | 54 KB | 2.1 KB |
| 20 | Generative AI, LLMs, Agents & Claude Applications (part 1 of 3) | 5 | 40 KB | 2.0 KB |
| 21 | Generative AI, LLMs, Agents & Claude Applications (part 2 of 3) | 4 | 18 KB | 2.0 KB |
| 22 | Generative AI, LLMs, Agents & Claude Applications (part 3 of 3) | 7 | 33 KB | 2.1 KB |
| 23 | Cloud Providers: Google Cloud, AWS, Azure & Certifications (part 1 of 2) | 8 | 24 KB | 2.0 KB |
| 24 | Cloud Providers: Google Cloud, AWS, Azure & Certifications (part 2 of 2) | 12 | 22 KB | 2.0 KB |
| 25 | Published ML System-Design Case Studies (part 1 of 5) | 1 | 31 KB | 1.3 KB |
| 26 | Published ML System-Design Case Studies (part 2 of 5) | 1 | 16 KB | 1.3 KB |
| 27 | Published ML System-Design Case Studies (part 3 of 5) | 2 | 22 KB | 1.3 KB |
| 28 | Published ML System-Design Case Studies (part 4 of 5) | 7 | 23 KB | 1.4 KB |
| 29 | Published ML System-Design Case Studies (part 5 of 5) | 1 | 42 KB | 1.3 KB |
| 30 | Supplementary Applied Domains: Corporate Finance, Marketing, Learning Analytics & Game Engines | 5 | 15 KB | 2.5 KB |

Total: 34 parts, 257 topic groups, 2,575 top-level topic lines. A topic list is 4 KB to 87 KB (roughly 1,000 to 22,000 tokens); a rules file is 1 to 2.5 KB (roughly 400 tokens); the method file is 22 KB (roughly 5,500 tokens).

## Part by part

### Part 01 · School-level foundations

- Files: `index/part01_school_foundations.rules.md` and `index/part01_school_foundations.topics.md`
- Size: topic list 18 KB (about 4,689 tokens); rules file 1.6 KB
- Groups in the topic list:
  - (topics directly under the domain heading) (22 topics)
- Remedial and on demand: opened only when the learner struggles with a basic skill; see the placement note in its rules file.

### Part 02 · Computer Organization & Data Representation

- Files: `index/part02_computer_organization.rules.md` and `index/part02_computer_organization.topics.md`
- Size: topic list 8 KB (about 1,969 tokens); rules file 1.3 KB
- Groups in the topic list:
  - Data representation (5 topics)
  - Digital logic (3 topics)
  - Machine organization (8 topics)
  - Exercises (11 topics)

### Part 03 · Mathematics, Probability, Statistics, Queueing & Performance Modelling

- Files: `index/part03_mathematics.rules.md` and `index/part03_mathematics.topics.md`
- Size: topic list 67 KB (about 17,082 tokens); rules file 1.6 KB
- Groups in the topic list:
  - Proof and discrete mathematics (10 topics)
  - Probability (14 topics)
  - Statistics and experimental design (24 topics)
  - Queueing and performance modelling (3 topics)
  - Linear algebra (19 topics)
  - Calculus and optimization (18 topics)
  - Numerical computing (8 topics)
  - Information theory (14 topics)
  - Signals and sequences (9 topics)
  - Decision mathematics (4 topics)
  - Exercises (20 topics)

### Part 03b · Calculus, Analysis, Coordinate Geometry & Number Theory

- Files: `index/part03b_analysis_calculus_and_number_theory.rules.md` and `index/part03b_analysis_calculus_and_number_theory.topics.md`
- Size: topic list 36 KB (about 9,100 tokens); rules file 1.8 KB
- Groups in the topic list:
  - Calculus and differential equations (29 topics)
  - Coordinate geometry and conics (12 topics)
  - Real analysis (20 topics)
  - Complex and functional analysis (8 topics)
  - Number theory (32 topics)
  - Exercises (9 topics)

### Part 03c · Signals, Systems & Communications

- Files: `index/part03c_signals_systems_and_communications.rules.md` and `index/part03c_signals_systems_and_communications.topics.md`
- Size: topic list 21 KB (about 5,477 tokens); rules file 1.7 KB
- Groups in the topic list:
  - Signals and linear time-invariant systems (9 topics)
  - Transforms and system analysis (7 topics)
  - Digital filters and multirate processing (7 topics)
  - Practical spectral analysis (9 topics)
  - Digital communications (9 topics)
  - Exercises (10 topics)

### Part 03d · Pure Mathematics: Algebra, Topology, Geometry, Logic & Rigorous Analysis

- Files: `index/part03d_pure_mathematics.rules.md` and `index/part03d_pure_mathematics.topics.md`
- Size: topic list 40 KB (about 10,181 tokens); rules file 1.8 KB
- Groups in the topic list:
  - Abstract algebra (19 topics)
  - Point-set and algebraic topology (15 topics)
  - Pure complex analysis (10 topics)
  - Measure theory and functional analysis (13 topics)
  - Differential geometry (10 topics)
  - Mathematical logic and axiomatic set theory (11 topics)
  - Pure combinatorics and graph theory (16 topics)
  - Rigorous partial differential equations (10 topics)
  - Exercises (9 topics)
- Graduate depth: proof-based pure mathematics; it builds on Parts 03 and 03b and is taken after them.

### Part 04 · Problem Solving, Reasoning & Research Method

- Files: `index/part04_problem_solving.rules.md` and `index/part04_problem_solving.topics.md`
- Size: topic list 12 KB (about 2,993 tokens); rules file 1.5 KB
- Groups in the topic list:
  - Problem-solving strategy (4 topics)
  - Contest mathematics toolkit (9 topics)
  - Physical and quantitative intuition (7 topics)
  - Speed and accuracy under time (5 topics)
  - Proof craft and mathematical maturity (5 topics)
  - Research method (8 topics)
  - Systems thinking (5 topics)
  - Learning science and deliberate practice (7 topics)
  - Social choice and fair division (3 topics)
  - Exercises (6 topics)

### Part 05 · Programming Languages & Language Theory (part 1 of 3)

- Files: `index/part05_programming_languages_python_and_shell.rules.md` and `index/part05_programming_languages_python_and_shell.topics.md`
- Size: topic list 8 KB (about 1,969 tokens); rules file 1.4 KB
- Groups in the topic list:
  - Python (4 topics)
  - R for data science (3 topics)
  - Shell and working with APIs from code (2 topics)

### Part 06 · Programming Languages & Language Theory (part 2 of 3)

- Files: `index/part06_programming_languages_go.rules.md` and `index/part06_programming_languages_go.topics.md`
- Size: topic list 26 KB (about 6,576 tokens); rules file 1.6 KB
- Groups in the topic list:
  - Go — toolchain and program structure (6 topics)
  - Go — composite data, functions, errors and text (4 topics)
  - Go — memory, types with behaviour and generics (4 topics)
  - Go — the everyday standard library (3 topics)
  - Go — concurrency (5 topics)
  - Go — engineering (10 topics)
  - Go — cross-language contrasts (6 topics)

### Part 07 · Programming Languages & Language Theory (part 3 of 3)

- Files: `index/part07_programming_languages_typescript_wire_theory_exercises.rules.md` and `index/part07_programming_languages_typescript_wire_theory_exercises.topics.md`
- Size: topic list 15 KB (about 3,750 tokens); rules file 1.4 KB
- Groups in the topic list:
  - TypeScript, Node and the web client (2 topics)
  - Java and the JVM (5 topics)
  - Wire formats (5 topics)
  - Language theory (13 topics)
  - Exercises (35 topics)

### Part 08 · Data Structures, Algorithms & Computational Complexity

- Files: `index/part08_data_structures_algorithms.rules.md` and `index/part08_data_structures_algorithms.topics.md`
- Size: topic list 20 KB (about 5,188 tokens); rules file 1.7 KB
- Groups in the topic list:
  - Analysis (5 topics)
  - Linear structures and techniques (8 topics)
  - Hashing (5 topics)
  - Trees and heaps (9 topics)
  - Sorting, searching and strings (9 topics)
  - Graph algorithms (12 topics)
  - Greedy algorithms and dynamic programming (4 topics)
  - Randomized and probabilistic structures (6 topics)
  - Computability and complexity (16 topics)
  - Algorithms at scale (4 topics)
  - Exercises (12 topics)

### Part 09 · Computer Networking & Web Protocols

- Files: `index/part09_networking.rules.md` and `index/part09_networking.topics.md`
- Size: topic list 13 KB (about 3,311 tokens); rules file 1.6 KB
- Groups in the topic list:
  - Architecture principles (6 topics)
  - Addressing and the link layer (6 topics)
  - Routing (6 topics)
  - Transport (5 topics)
  - DNS (7 topics)
  - HTTP and the web (8 topics)
  - TLS mechanics (2 topics)
  - Middleboxes, proxies and load balancing (3 topics)
  - Private connectivity (3 topics)
  - Data-centre networks (3 topics)
  - IoT and constrained-device networking (7 topics)
  - Measurement (4 topics)
  - Exercises (10 topics)

### Part 10 · Operating Systems & Linux

- Files: `index/part10_operating_systems.rules.md` and `index/part10_operating_systems.topics.md`
- Size: topic list 7 KB (about 1,760 tokens); rules file 1.5 KB
- Groups in the topic list:
  - Linux practice (8 topics)
  - Processes and threads (9 topics)
  - CPU scheduling (7 topics)
  - Virtual memory (9 topics)
  - Concurrency (13 topics)
  - Persistence (7 topics)
  - Isolation (5 topics)
  - I/O models and performance (5 topics)
  - Exercises (11 topics)

### Part 11 · Software Architecture, APIs, Design Patterns & Clean Architecture

- Files: `index/part11_software_architecture.rules.md` and `index/part11_software_architecture.topics.md`
- Size: topic list 18 KB (about 4,541 tokens); rules file 1.8 KB
- Groups in the topic list:
  - Architecture fundamentals (4 topics)
  - API design (6 topics)
  - Object-oriented foundations (5 topics)
  - Design principles (3 topics)
  - Design by contract and behavioural subtyping (3 topics)
  - Gang of Four patterns (4 topics)
  - Application architecture (8 topics)
  - Domain-driven design (5 topics)
  - Distributed application patterns (4 topics)
  - Anti-patterns (8 topics)
  - Quality attributes and evaluation (6 topics)
  - Architecture documentation (8 topics)
  - Formal methods (4 topics)
  - Software testing at depth (5 topics)
  - Exercises (13 topics)

### Part 12 · Databases, SQL, Relational Theory & Data Modelling

- Files: `index/part12_databases.rules.md` and `index/part12_databases.topics.md`
- Size: topic list 20 KB (about 5,235 tokens); rules file 1.8 KB
- Groups in the topic list:
  - Pre-SQL foundations (7 topics)
  - Relational theory (7 topics)
  - The SQL language (15 topics)
  - Storage and access methods (3 topics)
  - Query processing (3 topics)
  - Transactions and concurrency control (12 topics)
  - Recovery and replication (11 topics)
  - Data modelling and design (13 topics)
  - Operating databases (9 topics)
  - NoSQL and choosing a store (7 topics)
  - Analytics and other engines (6 topics)
  - Exercises (12 topics)

### Part 13 · Distributed Systems & Large-Scale System Design

- Files: `index/part13_distributed_systems.rules.md` and `index/part13_distributed_systems.topics.md`
- Size: topic list 14 KB (about 3,685 tokens); rules file 1.8 KB
- Groups in the topic list:
  - Foundations (4 topics)
  - Consensus and coordination (6 topics)
  - Replication (7 topics)
  - Availability (4 topics)
  - Partitioning (5 topics)
  - Distributed transactions (6 topics)
  - Caching at scale (6 topics)
  - Asynchronism and flow control (5 topics)
  - Stream and batch processing (7 topics)
  - Performance at scale (5 topics)
  - Testing and verification (3 topics)
  - System design method (7 topics)
  - Design techniques (10 topics)
  - Exercises (7 topics)

### Part 14 · Security, Cryptography, Privacy & Compliance

- Files: `index/part14_security.rules.md` and `index/part14_security.topics.md`
- Size: topic list 45 KB (about 11,403 tokens); rules file 2.0 KB
- Groups in the topic list:
  - Principles and economics (6 topics)
  - Threat modelling (8 topics)
  - Access-control models (7 topics)
  - Cryptography (16 topics)
  - Authentication and sessions (24 topics)
  - Authorization flaws (6 topics)
  - API abuse (8 topics)
  - Denial of service (9 topics)
  - Web application security (21 topics)
  - Cloud-specific attacks (7 topics)
  - Ethical hacking and offensive techniques (8 topics)
  - Network security and zero trust (10 topics)
  - Containers and Kubernetes security (7 topics)
  - Supply chain (6 topics)
  - Security management, risk and governance (6 topics)
  - Detection and incident response (6 topics)
  - AI and LLM application threats (15 topics)
  - Isolation classes (2 topics)
  - Privacy (10 topics)
  - Compliance (2 topics)
  - Exercises (18 topics)

### Part 15 · Software Delivery & Version Control

- Files: `index/part15_software_delivery.rules.md` and `index/part15_software_delivery.topics.md`
- Size: topic list 4 KB (about 1,017 tokens); rules file 1.2 KB
- Groups in the topic list:
  - Git (3 topics)
  - Delivery models (6 topics)
  - The profession (3 topics)
  - Exercises (5 topics)

### Part 16 · Cloud Computing Core: Virtualization, Well-Architected, Economics & IAM

- Files: `index/part16_cloud_core.rules.md` and `index/part16_cloud_core.topics.md`
- Size: topic list 7 KB (about 1,672 tokens); rules file 1.6 KB
- Groups in the topic list:
  - What cloud computing is (7 topics)
  - Virtualization and containers (7 topics)
  - Architecture patterns and well-architected frameworks (6 topics)
  - Cloud economics and FinOps (9 topics)
  - Cloud IAM concepts (9 topics)
  - Resource management, edge and cloud paradigms (4 topics)
  - Exercises (6 topics)

### Part 17 · The Architect's Practice: Decisions, Strategy & Career

- Files: `index/part17_architects_practice.rules.md` and `index/part17_architects_practice.topics.md`
- Size: topic list 5 KB (about 1,226 tokens); rules file 1.6 KB
- Groups in the topic list:
  - Making decisions (5 topics)
  - Decision theory (6 topics)
  - Build, buy, rent or adopt (4 topics)
  - Evolutionary architecture and migration (3 topics)
  - Sociotechnical architecture (3 topics)
  - Strategy, writing and review (6 topics)
  - Learning from failure (1 topics)
  - Keeping current (2 topics)
  - The road to the role (4 topics)
  - Exercises (6 topics)

### Part 18 · DevOps & SRE: Docker, Kubernetes, NGINX, CI/CD, Infrastructure as Code, Observability

- Files: `index/part18_devops_sre.rules.md` and `index/part18_devops_sre.topics.md`
- Size: topic list 16 KB (about 4,013 tokens); rules file 1.6 KB
- Groups in the topic list:
  - Docker (11 topics)
  - Kubernetes (10 topics)
  - NGINX and API gateways (8 topics)
  - CI/CD (13 topics)
  - Infrastructure as code (9 topics)
  - Observability (7 topics)
  - Site reliability engineering (12 topics)
  - Exercises (14 topics)

### Part 19 · Machine Learning, MLOps & Production ML System Design

- Files: `index/part19_machine_learning.rules.md` and `index/part19_machine_learning.topics.md`
- Size: topic list 87 KB (about 22,160 tokens); rules file 2.1 KB
- Groups in the topic list:
  - Foundations of AI (3 topics)
  - Classical AI: search, knowledge and reasoning (16 topics)
  - Classical machine learning (27 topics)
  - Deep learning (27 topics)
  - Natural language processing foundations (18 topics)
  - Machine learning in Python (9 topics)
  - Specialised learning areas (17 topics)
  - Classical computer vision and geometry (13 topics)
  - Applied problem families (19 topics)
  - MLOps (27 topics)
  - Exercises (21 topics)

### Part 19b · Speech & ASR, Computer Vision, Information Retrieval & NLP Toolkits

- Files: `index/part19b_speech_vision_retrieval_and_nlp_toolkits.rules.md` and `index/part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md`
- Size: topic list 54 KB (about 13,789 tokens); rules file 2.1 KB
- Groups in the topic list:
  - Speech science and analysis (11 topics)
  - Speech recognition: from HMMs to Kaldi (19 topics)
  - Speech synthesis, speakers and spoken-language systems (5 topics)
  - Computer vision: images, motion and multi-view geometry (32 topics)
  - Information retrieval engines (12 topics)
  - Classical NLP and toolkits (28 topics)
  - Exercises (11 topics)

### Part 20 · Generative AI, LLMs, Agents & Claude Applications (part 1 of 3)

- Files: `index/part20_generative_ai_1of3.rules.md` and `index/part20_generative_ai_1of3.topics.md`
- Size: topic list 40 KB (about 10,207 tokens); rules file 2.0 KB
- Groups in the topic list:
  - How LLMs work (18 topics)
  - Fine-tuning and adaptation (20 topics)
  - Multimodal models (9 topics)
  - Generative models beyond autoregression (8 topics)
  - Embeddings and retrieval (10 topics)

### Part 21 · Generative AI, LLMs, Agents & Claude Applications (part 2 of 3)

- Files: `index/part21_generative_ai_2of3.rules.md` and `index/part21_generative_ai_2of3.topics.md`
- Size: topic list 18 KB (about 4,547 tokens); rules file 2.0 KB
- Groups in the topic list:
  - Retrieval-augmented generation (18 topics)
  - Model APIs (7 topics)
  - Prompt, context and output engineering (8 topics)
  - Tools and the Model Context Protocol (5 topics)

### Part 22 · Generative AI, LLMs, Agents & Claude Applications (part 3 of 3)

- Files: `index/part22_generative_ai_3of3.rules.md` and `index/part22_generative_ai_3of3.topics.md`
- Size: topic list 33 KB (about 8,410 tokens); rules file 2.1 KB
- Groups in the topic list:
  - Agents and workflows (15 topics)
  - Claude Code (6 topics)
  - Security and safety of LLM applications (12 topics)
  - Evaluation, testing and debugging (13 topics)
  - Application architecture and LLMOps (12 topics)
  - The forward-deployed engineer's craft (4 topics)
  - Exercises (36 topics)

### Part 23 · Cloud Providers: Google Cloud, AWS, Azure & Certifications (part 1 of 2)

- Files: `index/part23_cloud_providers_1of2.rules.md` and `index/part23_cloud_providers_1of2.topics.md`
- Size: topic list 24 KB (about 6,231 tokens); rules file 2.0 KB
- Groups in the topic list:
  - Google Cloud — compute (5 topics)
  - Google Cloud — storage and databases (11 topics)
  - Google Cloud — networking (10 topics)
  - Google Cloud — data and analytics (8 topics)
  - Google Cloud — AI and ML (8 topics)
  - Google Cloud — security (13 topics)
  - Google Cloud — operations, DevOps and cost (5 topics)
  - Google Cloud — command line (15 topics)

### Part 24 · Cloud Providers: Google Cloud, AWS, Azure & Certifications (part 2 of 2)

- Files: `index/part24_cloud_providers_2of2.rules.md` and `index/part24_cloud_providers_2of2.topics.md`
- Size: topic list 22 KB (about 5,694 tokens); rules file 2.0 KB
- Groups in the topic list:
  - Google Cloud — mapping system-design components (9 topics)
  - AWS (7 topics)
  - AWS command line (3 topics)
  - Azure (7 topics)
  - Azure command line (3 topics)
  - AWS and Azure — what differs at depth (8 topics)
  - Cross-provider concept map (39 topics)
  - Certifications — Google Cloud (10 topics)
  - Certifications — AWS (6 topics)
  - Certifications — Microsoft Azure (5 topics)
  - Certifications — Anthropic (1 topics)
  - Exercises (13 topics)

### Part 25 · Published ML System-Design Case Studies (part 1 of 5)

- Files: `index/part25_ml_case_studies_1of5.rules.md` and `index/part25_ml_case_studies_1of5.topics.md`
- Size: topic list 31 KB (about 7,860 tokens); rules file 1.3 KB
- Groups in the topic list:
  - Recommend / personalize / feed (62 topics)

### Part 26 · Published ML System-Design Case Studies (part 2 of 5)

- Files: `index/part26_ml_case_studies_2of5.rules.md` and `index/part26_ml_case_studies_2of5.topics.md`
- Size: topic list 16 KB (about 3,990 tokens); rules file 1.3 KB
- Groups in the topic list:
  - Search / rank / ads (36 topics)

### Part 27 · Published ML System-Design Case Studies (part 3 of 5)

- Files: `index/part27_ml_case_studies_3of5.rules.md` and `index/part27_ml_case_studies_3of5.topics.md`
- Size: topic list 22 KB (about 5,692 tokens); rules file 1.3 KB
- Groups in the topic list:
  - Forecast / ETA / demand (25 topics)
  - Fraud / trust & safety (23 topics)

### Part 28 · Published ML System-Design Case Studies (part 4 of 5)

- Files: `index/part28_ml_case_studies_4of5.rules.md` and `index/part28_ml_case_studies_4of5.topics.md`
- Size: topic list 23 KB (about 6,013 tokens); rules file 1.4 KB
- Groups in the topic list:
  - LLM / genAI apps (19 topics)
  - NLP / text / support (7 topics)
  - CV / video / OCR (6 topics)
  - Speech / audio (3 topics)
  - Marketing / churn / CLV / notify (14 topics)
  - Availability / inventory (3 topics)
  - ML platform / infra (2 topics)

### Part 29 · Published ML System-Design Case Studies (part 5 of 5)

- Files: `index/part29_ml_case_studies_5of5.rules.md` and `index/part29_ml_case_studies_5of5.topics.md`
- Size: topic list 42 KB (about 10,687 tokens); rules file 1.3 KB
- Groups in the topic list:
  - Other (pricing, classification, routing, dimensions and more) (95 topics)

### Part 30 · Supplementary Applied Domains: Corporate Finance, Marketing, Learning Analytics & Game Engines

- Files: `index/part30_supplementary_applied_domains.rules.md` and `index/part30_supplementary_applied_domains.topics.md`
- Size: topic list 15 KB (about 3,782 tokens); rules file 2.5 KB
- Groups in the topic list:
  - Corporate finance (11 topics)
  - Marketing and digital marketing (5 topics)
  - Learning analytics (6 topics)
  - Game engines and real-time rendering (22 topics)
  - Exercises (4 topics)
- Optional and supplementary: added from the NPTEL 2026 courses; taught on request, after the core engineering path.

**NPTEL 2026 additions (25 Oct 2026).** The topics of 22 NPTEL courses were merged, deduplicated and inserted into the existing groups or into new ones: Classical AI and Classical computer vision (part 19), Generative models beyond autoregression (part 20), R for data science (part 05), Java and the JVM (part 07), IoT and constrained-device networking (part 09), Ethical hacking and Security management (part 14), Resource management, edge and cloud paradigms (part 16), and part 30. Smaller additions sit in parts 03, 05, 08, 10, 11, 12, 14, 16, 19 and 20.

**Unified-curriculum additions (27 Oct 2026).** The missing topics found by the topic diff in `gcp/topic-diff/README.md` (at the repo root, outside gcp-lite) were deduplicated and integrated. Three new parts were created: Part 03b (calculus, analysis, coordinate geometry and number theory), Part 03c (signals, systems and communications) and Part 19b (speech and ASR, computer vision, information retrieval and NLP toolkits). The other changed parts received topics in their existing groups, and Part 30 gained a game-engines group and an Exercises group; Part 01 also received the missing school-level topics and is now remedial: it is taught only when the learner struggles with the basics.

**Full-depth pass (29 Oct 2026).** A second topic diff (`gcp/topic-diff/v2/README.md`, at the repo root) checked every topic of gcp/unified-curriculum.md against the split files. Every missing topic was added and every partial one was deepened to full depth (mechanism, theorem or formula, algorithm, cost and subtopics) in its owning part, with at most one from-scratch build and two drills added per file. The graduate-level pure mathematics went into a new Part 03d; graduate computer-science topics went into Parts 02, 07, 08 and 14.

## Where to find common subjects

| Subject | Part |
|---|---|
| Python | 05 |
| Shell and working with APIs from code | 05 |
| Go (toolchain, data, memory, standard library, concurrency, engineering, cross-language contrasts) | 06 |
| TypeScript, wire formats, language theory, and the Programming exercises (including the Python ones) | 07 |
| Data representation, IEEE 754 floating point, UTF-8, caches | 02 |
| Proof, probability, statistics, queueing, numerical computing | 03 |
| Data structures and algorithms | 08 |
| Networking, DNS, HTTP, TLS, load balancing | 09 |
| Operating systems, processes, virtual memory, I/O | 10 |
| Design patterns, APIs, clean architecture, testing | 11 |
| SQL, relational theory, storage, transactions, recovery | 12 |
| Consensus, replication, partitioning, system design method | 13 |
| Cryptography, authentication, web and cloud security, privacy | 14 |
| Git and delivery | 15 |
| Cloud core, virtualization, IAM, economics | 16 |
| Docker, Kubernetes, NGINX, CI/CD, infrastructure as code, observability | 18 |
| Machine learning and MLOps | 19 |
| LLMs, retrieval, agents, Claude applications | 20 to 22 |
| Google Cloud, AWS and Azure services and certifications | 23 and 24 |
| Published ML system-design case studies | 25 to 29 |
| Classical AI (search, logic, planning, Bayesian networks, fuzzy logic) | 19 |
| Classical computer vision and geometry; NLP parsing, tagging, topic models, knowledge graphs | 19 |
| Generative models (VAE, GAN, diffusion, flow matching); interpretability | 20 |
| Java and the JVM | 07 |
| R for data science | 05 |
| IoT protocols and constrained networking; software-defined networking | 09 |
| Ethical hacking, security management and risk, privacy regulation | 14 |
| Edge, fog and mobile cloud; OpenStack; SLAs | 16 |
| Corporate finance, marketing, learning analytics (optional) | 30 |
| Calculus, ODEs, coordinate geometry and conics, real and complex analysis, number theory | 03b |
| Signals and LTI systems, Laplace and z-transforms, filter design, multirate DSP, digital communications | 03c |
| Abstract algebra (groups, rings, fields, Galois theory), point-set and algebraic topology | 03d |
| Measure theory, Lebesgue integration, functional analysis, pure complex analysis | 03d |
| Differential geometry, mathematical logic and set theory, pure combinatorics, rigorous PDE | 03d |
| Speech recognition and synthesis, Kaldi, multi-view geometry and motion, information-retrieval engines, NLTK and spaCy | 19b |
| Game engines and real-time rendering (optional) | 30 |
