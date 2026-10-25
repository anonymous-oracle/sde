# Index map: what every file holds

This is the entry file for the split Consolidated Topic Index. Read it first in any session, then `index/00_ingest_progress.md` to see which part is current, then `index/00_learning_method.md` (the single copy of the teaching method), then open only the two files of that part. Everything else stays closed until the learner moves on.

## How to use it in a session

1. Read this file (the map) and `index/00_ingest_progress.md` (current part and each part's status).
2. Read `index/00_learning_method.md` once (about 5,500 tokens). It is the only copy of the teaching method.
3. Open the current part's **rules file** (`.rules.md`, about 400 tokens: that domain's prerequisites, depth bar and capstone) and its **topic list** (`.topics.md`). Together with the method they are about 6,500 to 16,000 tokens; the master index is about 110,000.
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
| `Consolidated_Topic_Index_GCP.md` | The master copy of the whole index (about 434 KB). The parts are cut from it | Only to check a part against its source |
| `Exercise Rules` | The rule that separates predictions (read-only) from exercises (written by the learner) | Before setting any prediction or exercise |
| `learn-SKILL.md` | The tutoring skill: diagnose first, one scaffold and one question per turn, hold the line, no hidden answers | Start of a teaching stretch |
| `claude/learning_handoff_and_tracker.md` | The handoff (Part A) and the tracker (Part B) | Resuming after a break |
| `Rust_Track_AI_Infrastructure.md` | The Rust track (21 projects), which starts only after the first two or three Go groups are mastered | When Go is well under way |
| `nptel_consolidated_topics.md` | The 22 NPTEL 2026 courses merged into one deduplicated topic list: each topic with its source courses, status (covered, extended, added) and where it sits in the index. Course layouts are in `nptel_courses_26.md` | When asking what the NPTEL courses add, or tracing an inserted topic to its source |
| `pending_tracker.md` | The working record of overrides, retries, the resume point and the log. Refreshed 24 Oct 2026 through concept 36. Lives at the repo root as `pending_tracker.md` | Resuming, and when closing a part |

## Parts at a glance

| Part | Domain | Groups | Topic list | Rules file |
|---|---|---|---|---|
| 01 | School-level foundations | 1 | 3 KB | 1.1 KB |
| 02 | Computer Organization & Data Representation | 4 | 6 KB | 1.3 KB |
| 03 | Mathematics, Probability, Statistics, Queueing & Performance Modelling | 11 | 12 KB | 1.6 KB |
| 04 | Problem Solving, Reasoning & Research Method | 9 | 8 KB | 1.5 KB |
| 05 | Programming Languages & Language Theory (part 1 of 3) | 3 | 4 KB | 1.4 KB |
| 06 | Programming Languages & Language Theory (part 2 of 3) | 7 | 18 KB | 1.6 KB |
| 07 | Programming Languages & Language Theory (part 3 of 3) | 5 | 8 KB | 1.4 KB |
| 08 | Data Structures, Algorithms & Computational Complexity | 11 | 7 KB | 1.7 KB |
| 09 | Computer Networking & Web Protocols | 13 | 8 KB | 1.6 KB |
| 10 | Operating Systems & Linux | 9 | 6 KB | 1.5 KB |
| 11 | Software Architecture, APIs, Design Patterns & Clean Architecture | 15 | 11 KB | 1.8 KB |
| 12 | Databases, SQL, Relational Theory & Data Modelling | 12 | 15 KB | 1.8 KB |
| 13 | Distributed Systems & Large-Scale System Design | 14 | 10 KB | 1.8 KB |
| 14 | Security, Cryptography, Privacy & Compliance | 21 | 21 KB | 2.0 KB |
| 15 | Software Delivery & Version Control | 4 | 3 KB | 1.2 KB |
| 16 | Cloud Computing Core: Virtualization, Well-Architected, Economics & IAM | 7 | 6 KB | 1.6 KB |
| 17 | The Architect's Practice: Decisions, Strategy & Career | 10 | 4 KB | 1.6 KB |
| 18 | DevOps & SRE: Docker, Kubernetes, NGINX, CI/CD, Infrastructure as Code, Observability | 8 | 12 KB | 1.6 KB |
| 19 | Machine Learning, MLOps & Production ML System Design | 11 | 29 KB | 2.1 KB |
| 20 | Generative AI, LLMs, Agents & Claude Applications (part 1 of 3) | 5 | 21 KB | 2.0 KB |
| 21 | Generative AI, LLMs, Agents & Claude Applications (part 2 of 3) | 4 | 14 KB | 2.0 KB |
| 22 | Generative AI, LLMs, Agents & Claude Applications (part 3 of 3) | 7 | 24 KB | 2.1 KB |
| 23 | Cloud Providers: Google Cloud, AWS, Azure & Certifications (part 1 of 2) | 8 | 24 KB | 2.0 KB |
| 24 | Cloud Providers: Google Cloud, AWS, Azure & Certifications (part 2 of 2) | 12 | 23 KB | 2.0 KB |
| 25 | Published ML System-Design Case Studies (part 1 of 5) | 1 | 29 KB | 1.3 KB |
| 26 | Published ML System-Design Case Studies (part 2 of 5) | 1 | 15 KB | 1.3 KB |
| 27 | Published ML System-Design Case Studies (part 3 of 5) | 2 | 21 KB | 1.3 KB |
| 28 | Published ML System-Design Case Studies (part 4 of 5) | 7 | 24 KB | 1.4 KB |
| 29 | Published ML System-Design Case Studies (part 5 of 5) | 1 | 41 KB | 1.3 KB |
| 30 | Supplementary Applied Domains: Corporate Finance, Marketing & Learning Analytics | 3 | 3 KB | 2.0 KB |

Total: 30 parts, 226 topic groups, 1,869 top-level topic lines. A topic list is 3 KB to 41 KB (roughly 750 to 10,000 tokens); a rules file is 1 to 2 KB (roughly 400 tokens); the method file is 22 KB (roughly 5,500 tokens).

## Part by part

### Part 01 · School-level foundations

- Files: `index/part01_school_foundations.rules.md` and `index/part01_school_foundations.topics.md`
- Size: topic list 3 KB (about 500 tokens); rules file 1 to 2 KB
- Groups in the topic list:
  - (topics directly under the domain heading) (16 topics)

### Part 02 · Computer Organization & Data Representation

- Files: `index/part02_computer_organization.rules.md` and `index/part02_computer_organization.topics.md`
- Size: topic list 6 KB (about 1,500 tokens); rules file 1 to 2 KB
- Groups in the topic list:
  - Data representation (5 topics)
  - Digital logic (3 topics)
  - Machine organization (6 topics)
  - Exercises (11 topics)

### Part 03 · Mathematics, Probability, Statistics, Queueing & Performance Modelling

- Files: `index/part03_mathematics.rules.md` and `index/part03_mathematics.topics.md`
- Size: topic list 12 KB (about 3,000 tokens); rules file 1 to 2 KB
- Groups in the topic list:
  - Proof and discrete mathematics (5 topics)
  - Probability (6 topics)
  - Statistics and experimental design (5 topics)
  - Queueing and performance modelling (3 topics)
  - Linear algebra (10 topics)
  - Calculus and optimization (3 topics)
  - Numerical computing (7 topics)
  - Information theory (6 topics)
  - Signals and sequences (6 topics)
  - Decision mathematics (2 topics)
  - Exercises (15 topics)

### Part 04 · Problem Solving, Reasoning & Research Method

- Files: `index/part04_problem_solving.rules.md` and `index/part04_problem_solving.topics.md`
- Size: topic list 8 KB (about 2,000 tokens); rules file 1 to 2 KB
- Groups in the topic list:
  - Problem-solving strategy (4 topics)
  - Contest mathematics toolkit (8 topics)
  - Physical and quantitative intuition (7 topics)
  - Speed and accuracy under time (5 topics)
  - Proof craft and mathematical maturity (5 topics)
  - Research method (7 topics)
  - Systems thinking (5 topics)
  - Learning science and deliberate practice (6 topics)
  - Exercises (5 topics)

### Part 05 · Programming Languages & Language Theory (part 1 of 3)

- Files: `index/part05_programming_languages_python_and_shell.rules.md` and `index/part05_programming_languages_python_and_shell.topics.md`
- Size: topic list 4 KB (about 1,000 tokens); rules file 1 to 2 KB
- Groups in the topic list:
  - Python (4 topics)
  - R for data science (3 topics)
  - Shell and working with APIs from code (2 topics)

### Part 06 · Programming Languages & Language Theory (part 2 of 3)

- Files: `index/part06_programming_languages_go.rules.md` and `index/part06_programming_languages_go.topics.md`
- Size: topic list 18 KB (about 4,500 tokens); rules file 1 to 2 KB
- Groups in the topic list:
  - Go — toolchain and program structure (4 topics)
  - Go — composite data, functions, errors and text (4 topics)
  - Go — memory, types with behaviour and generics (4 topics)
  - Go — the everyday standard library (3 topics)
  - Go — concurrency (5 topics)
  - Go — engineering (10 topics)
  - Go — cross-language contrasts (6 topics)

### Part 07 · Programming Languages & Language Theory (part 3 of 3)

- Files: `index/part07_programming_languages_typescript_wire_theory_exercises.rules.md` and `index/part07_programming_languages_typescript_wire_theory_exercises.topics.md`
- Size: topic list 8 KB (about 2,000 tokens); rules file 1 to 2 KB
- Groups in the topic list:
  - TypeScript, Node and the web client (2 topics)
  - Java and the JVM (5 topics)
  - Wire formats (4 topics)
  - Language theory (8 topics)
  - Exercises (34 topics)

### Part 08 · Data Structures, Algorithms & Computational Complexity

- Files: `index/part08_data_structures_algorithms.rules.md` and `index/part08_data_structures_algorithms.topics.md`
- Size: topic list 7 KB (about 1,500 tokens); rules file 1 to 2 KB
- Groups in the topic list:
  - Analysis (3 topics)
  - Linear structures and techniques (7 topics)
  - Hashing (5 topics)
  - Trees and heaps (8 topics)
  - Sorting, searching and strings (9 topics)
  - Graph algorithms (9 topics)
  - Greedy algorithms and dynamic programming (4 topics)
  - Randomized and probabilistic structures (5 topics)
  - Computability and complexity (6 topics)
  - Algorithms at scale (4 topics)
  - Exercises (10 topics)

### Part 09 · Computer Networking & Web Protocols

- Files: `index/part09_networking.rules.md` and `index/part09_networking.topics.md`
- Size: topic list 8 KB (about 2,000 tokens); rules file 1 to 2 KB
- Groups in the topic list:
  - Architecture principles (5 topics)
  - Addressing and the link layer (5 topics)
  - Routing (6 topics)
  - Transport (5 topics)
  - DNS (7 topics)
  - HTTP and the web (3 topics)
  - TLS mechanics (2 topics)
  - Middleboxes, proxies and load balancing (3 topics)
  - Private connectivity (3 topics)
  - Data-centre networks (3 topics)
  - IoT and constrained-device networking (7 topics)
  - Measurement (4 topics)
  - Exercises (9 topics)

### Part 10 · Operating Systems & Linux

- Files: `index/part10_operating_systems.rules.md` and `index/part10_operating_systems.topics.md`
- Size: topic list 6 KB (about 1,500 tokens); rules file 1 to 2 KB
- Groups in the topic list:
  - Linux practice (8 topics)
  - Processes and threads (9 topics)
  - CPU scheduling (7 topics)
  - Virtual memory (8 topics)
  - Concurrency (13 topics)
  - Persistence (7 topics)
  - Isolation (5 topics)
  - I/O models and performance (5 topics)
  - Exercises (11 topics)

### Part 11 · Software Architecture, APIs, Design Patterns & Clean Architecture

- Files: `index/part11_software_architecture.rules.md` and `index/part11_software_architecture.topics.md`
- Size: topic list 11 KB (about 2,500 tokens); rules file 1 to 2 KB
- Groups in the topic list:
  - Architecture fundamentals (4 topics)
  - API design (6 topics)
  - Object-oriented foundations (5 topics)
  - Design principles (3 topics)
  - Design by contract and behavioural subtyping (3 topics)
  - Gang of Four patterns (4 topics)
  - Application architecture (7 topics)
  - Domain-driven design (5 topics)
  - Distributed application patterns (4 topics)
  - Anti-patterns (7 topics)
  - Quality attributes and evaluation (5 topics)
  - Architecture documentation (5 topics)
  - Formal methods (4 topics)
  - Software testing at depth (5 topics)
  - Exercises (12 topics)

### Part 12 · Databases, SQL, Relational Theory & Data Modelling

- Files: `index/part12_databases.rules.md` and `index/part12_databases.topics.md`
- Size: topic list 15 KB (about 4,000 tokens); rules file 1 to 2 KB
- Groups in the topic list:
  - Pre-SQL foundations (7 topics)
  - Relational theory (7 topics)
  - The SQL language (15 topics)
  - Storage and access methods (3 topics)
  - Query processing (3 topics)
  - Transactions and concurrency control (11 topics)
  - Recovery and replication (11 topics)
  - Data modelling and design (13 topics)
  - Operating databases (8 topics)
  - NoSQL and choosing a store (7 topics)
  - Analytics and other engines (6 topics)
  - Exercises (12 topics)

### Part 13 · Distributed Systems & Large-Scale System Design

- Files: `index/part13_distributed_systems.rules.md` and `index/part13_distributed_systems.topics.md`
- Size: topic list 10 KB (about 2,500 tokens); rules file 1 to 2 KB
- Groups in the topic list:
  - Foundations (4 topics)
  - Consensus and coordination (6 topics)
  - Replication (7 topics)
  - Availability (4 topics)
  - Partitioning (5 topics)
  - Distributed transactions (5 topics)
  - Caching at scale (6 topics)
  - Asynchronism and flow control (5 topics)
  - Stream and batch processing (7 topics)
  - Performance at scale (5 topics)
  - Testing and verification (3 topics)
  - System design method (4 topics)
  - Design techniques (10 topics)
  - Exercises (7 topics)

### Part 14 · Security, Cryptography, Privacy & Compliance

- Files: `index/part14_security.rules.md` and `index/part14_security.topics.md`
- Size: topic list 21 KB (about 5,500 tokens); rules file 1 to 2 KB
- Groups in the topic list:
  - Principles and economics (6 topics)
  - Threat modelling (8 topics)
  - Access-control models (6 topics)
  - Cryptography (14 topics)
  - Authentication and sessions (14 topics)
  - Authorization flaws (5 topics)
  - API abuse (8 topics)
  - Denial of service (9 topics)
  - Web application security (14 topics)
  - Cloud-specific attacks (7 topics)
  - Ethical hacking and offensive techniques (8 topics)
  - Network security and zero trust (9 topics)
  - Containers and Kubernetes security (6 topics)
  - Supply chain (6 topics)
  - Security management, risk and governance (3 topics)
  - Detection and incident response (6 topics)
  - AI and LLM application threats (13 topics)
  - Isolation classes (2 topics)
  - Privacy (10 topics)
  - Compliance (2 topics)
  - Exercises (16 topics)

### Part 15 · Software Delivery & Version Control

- Files: `index/part15_software_delivery.rules.md` and `index/part15_software_delivery.topics.md`
- Size: topic list 3 KB (about 1,000 tokens); rules file 1 to 2 KB
- Groups in the topic list:
  - Git (3 topics)
  - Delivery models (5 topics)
  - The profession (3 topics)
  - Exercises (5 topics)

### Part 16 · Cloud Computing Core: Virtualization, Well-Architected, Economics & IAM

- Files: `index/part16_cloud_core.rules.md` and `index/part16_cloud_core.topics.md`
- Size: topic list 6 KB (about 1,500 tokens); rules file 1 to 2 KB
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
- Size: topic list 4 KB (about 1,000 tokens); rules file 1 to 2 KB
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
- Size: topic list 12 KB (about 3,000 tokens); rules file 1 to 2 KB
- Groups in the topic list:
  - Docker (11 topics)
  - Kubernetes (10 topics)
  - NGINX and API gateways (8 topics)
  - CI/CD (11 topics)
  - Infrastructure as code (9 topics)
  - Observability (7 topics)
  - Site reliability engineering (10 topics)
  - Exercises (14 topics)

### Part 19 · Machine Learning, MLOps & Production ML System Design

- Files: `index/part19_machine_learning.rules.md` and `index/part19_machine_learning.topics.md`
- Size: topic list 29 KB (about 7,000 tokens); rules file 1 to 2 KB
- Groups in the topic list:
  - Foundations of AI (3 topics)
  - Classical AI: search, knowledge and reasoning (15 topics)
  - Classical machine learning (12 topics)
  - Deep learning (18 topics)
  - Natural language processing foundations (15 topics)
  - Machine learning in Python (3 topics)
  - Specialised learning areas (11 topics)
  - Classical computer vision and geometry (10 topics)
  - Applied problem families (13 topics)
  - MLOps (12 topics)
  - Exercises (16 topics)

### Part 20 · Generative AI, LLMs, Agents & Claude Applications (part 1 of 3)

- Files: `index/part20_generative_ai_1of3.rules.md` and `index/part20_generative_ai_1of3.topics.md`
- Size: topic list 21 KB (about 5,500 tokens); rules file 1 to 2 KB
- Groups in the topic list:
  - How LLMs work (13 topics)
  - Fine-tuning and adaptation (14 topics)
  - Multimodal models (7 topics)
  - Generative models beyond autoregression (7 topics)
  - Embeddings and retrieval (9 topics)

### Part 21 · Generative AI, LLMs, Agents & Claude Applications (part 2 of 3)

- Files: `index/part21_generative_ai_2of3.rules.md` and `index/part21_generative_ai_2of3.topics.md`
- Size: topic list 14 KB (about 3,500 tokens); rules file 1 to 2 KB
- Groups in the topic list:
  - Retrieval-augmented generation (16 topics)
  - Model APIs (7 topics)
  - Prompt, context and output engineering (7 topics)
  - Tools and the Model Context Protocol (5 topics)

### Part 22 · Generative AI, LLMs, Agents & Claude Applications (part 3 of 3)

- Files: `index/part22_generative_ai_3of3.rules.md` and `index/part22_generative_ai_3of3.topics.md`
- Size: topic list 24 KB (about 6,000 tokens); rules file 1 to 2 KB
- Groups in the topic list:
  - Agents and workflows (15 topics)
  - Claude Code (6 topics)
  - Security and safety of LLM applications (9 topics)
  - Evaluation, testing and debugging (12 topics)
  - Application architecture and LLMOps (9 topics)
  - The forward-deployed engineer's craft (3 topics)
  - Exercises (33 topics)

### Part 23 · Cloud Providers: Google Cloud, AWS, Azure & Certifications (part 1 of 2)

- Files: `index/part23_cloud_providers_1of2.rules.md` and `index/part23_cloud_providers_1of2.topics.md`
- Size: topic list 24 KB (about 6,000 tokens); rules file 1 to 2 KB
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
- Size: topic list 23 KB (about 5,500 tokens); rules file 1 to 2 KB
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
- Size: topic list 29 KB (about 7,500 tokens); rules file 1 to 2 KB
- Groups in the topic list:
  - Recommend / personalize / feed (58 topics)

### Part 26 · Published ML System-Design Case Studies (part 2 of 5)

- Files: `index/part26_ml_case_studies_2of5.rules.md` and `index/part26_ml_case_studies_2of5.topics.md`
- Size: topic list 15 KB (about 4,000 tokens); rules file 1 to 2 KB
- Groups in the topic list:
  - Search / rank / ads (35 topics)

### Part 27 · Published ML System-Design Case Studies (part 3 of 5)

- Files: `index/part27_ml_case_studies_3of5.rules.md` and `index/part27_ml_case_studies_3of5.topics.md`
- Size: topic list 21 KB (about 5,000 tokens); rules file 1 to 2 KB
- Groups in the topic list:
  - Forecast / ETA / demand (23 topics)
  - Fraud / trust & safety (21 topics)

### Part 28 · Published ML System-Design Case Studies (part 4 of 5)

- Files: `index/part28_ml_case_studies_4of5.rules.md` and `index/part28_ml_case_studies_4of5.topics.md`
- Size: topic list 24 KB (about 6,000 tokens); rules file 1 to 2 KB
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
- Size: topic list 41 KB (about 10,500 tokens); rules file 1 to 2 KB
- Groups in the topic list:
  - Other (pricing, classification, routing, dimensions and more) (93 topics)

### Part 30 · Supplementary Applied Domains: Corporate Finance, Marketing & Learning Analytics

- Files: `index/part30_supplementary_applied_domains.rules.md` and `index/part30_supplementary_applied_domains.topics.md`
- Size: topic list 3 KB (about 1,000 tokens); rules file 1 to 2 KB
- Groups in the topic list:
  - Corporate finance (8 topics)
  - Marketing and digital marketing (5 topics)
  - Learning analytics (6 topics)
- Optional and supplementary: added from the NPTEL 2026 course list; taught on request, after the core engineering path. See `nptel_consolidated_topics.md`.

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
