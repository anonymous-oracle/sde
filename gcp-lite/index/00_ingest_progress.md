# Index ingest progress

Start with `index/00_index_map.md`, which describes every file. How this works: the Consolidated Topic Index is split into 29 parts. The teaching method is kept once in `index/00_learning_method.md`. Each part has a rules file (`index/partNN_<name>.rules.md`: that domain's prerequisites, depth bar and capstone, with a pointer to the method) and a separate topic list (`index/partNN_<name>.topics.md`). Only the current part is ingested. A part moves to `done` only when the learner has been taught and has passed through its groups (exercises included); only then is the next part opened. The original `Consolidated_Topic_Index_GCP.md` stays as the master copy; these parts are cut from it without changes to the wording.

Current part: **05** (Python and shell). Parts 01 to 04 are not walked in index order: Mathematics and Problem Solving are taught just in time, School foundations were used as tools, and Computer Organization is paused (see `pending_tracker.md`).
Status values: not started, ingesting, in progress, done, paused.

| Part | Domain | Groups | Topic list | Status |
|---|---|---|---|---|
| 01 | School-level foundations | topics | 2 KB | not walked (used as tools) |
| 02 | Computer Organization & Data Representation | Data representation; Digital logic; Machine organization; Exercises | 5 KB | paused (partly taught; alignment and padding paused) |
| 03 | Mathematics, Probability, Statistics, Queueing & Performance Modelling | Proof and discrete mathematics; Probability; Statistics and experimental design; Queueing and performance mode | 11 KB | just in time |
| 04 | Problem Solving, Reasoning & Research Method | Problem-solving strategy; Contest mathematics toolkit; Physical and quantitative intuition; Speed and accuracy | 7 KB | just in time |
| 05 | Programming Languages & Language Theory (1/3) | Python; Shell and working with APIs from code | 2 KB | in progress (Python runtime model) |
| 06 | Programming Languages & Language Theory (2/3) | Go — toolchain and program structure; Go — composite data, functions, errors and text; Go — memory, types with | 17 KB | not started |
| 07 | Programming Languages & Language Theory (3/3) | TypeScript, Node and the web client; Wire formats; Language theory; Exercises | 7 KB | not started |
| 08 | Data Structures, Algorithms & Computational Complexity | Analysis; Linear structures and techniques; Hashing; Trees and heaps; Sorting, searching and strings; Graph al | 6 KB | not started |
| 09 | Computer Networking & Web Protocols | Architecture principles; Addressing and the link layer; Routing; Transport; DNS; HTTP and the web; TLS mechani | 6 KB | not started |
| 10 | Operating Systems & Linux | Linux practice; Processes and threads; CPU scheduling; Virtual memory; Concurrency; Persistence; Isolation; I/ | 5 KB | not started |
| 11 | Software Architecture, APIs, Design Patterns & Clean Architecture | Architecture fundamentals; API design; Object-oriented foundations; Design principles; Design by contract and  | 10 KB | not started |
| 12 | Databases, SQL, Relational Theory & Data Modelling | Pre-SQL foundations; Relational theory; The SQL language; Storage and access methods; Query processing; Transa | 14 KB | not started |
| 13 | Distributed Systems & Large-Scale System Design | Foundations; Consensus and coordination; Replication; Availability; Partitioning; Distributed transactions; Ca | 9 KB | not started |
| 14 | Security, Cryptography, Privacy & Compliance | Principles and economics; Threat modelling; Access-control models; Cryptography; Authentication and sessions;  | 18 KB | not started |
| 15 | Software Delivery & Version Control | Git; Delivery models; The profession; Exercises | 3 KB | not started |
| 16 | Cloud Computing Core: Virtualization, Well-Architected, Economics & IAM | What cloud computing is; Virtualization and containers; Architecture patterns and well-architected frameworks; | 5 KB | not started |
| 17 | The Architect's Practice: Decisions, Strategy & Career | Making decisions; Decision theory; Build, buy, rent or adopt; Evolutionary architecture and migration; Sociote | 4 KB | not started |
| 18 | DevOps & SRE: Docker, Kubernetes, NGINX, CI/CD, Infrastructure as Code, Observability | Docker; Kubernetes; NGINX and API gateways; CI/CD; Infrastructure as code; Observability; Site reliability eng | 12 KB | not started |
| 19 | Machine Learning, MLOps & Production ML System Design | Foundations of AI; Classical machine learning; Deep learning; Natural language processing foundations; Machine | 20 KB | not started |
| 20 | Generative AI, LLMs, Agents & Claude Applications (1/3) | How LLMs work; Fine-tuning and adaptation; Multimodal models; Embeddings and retrieval | 19 KB | not started |
| 21 | Generative AI, LLMs, Agents & Claude Applications (2/3) | Retrieval-augmented generation; Model APIs; Prompt, context and output engineering; Tools and the Model Contex | 13 KB | not started |
| 22 | Generative AI, LLMs, Agents & Claude Applications (3/3) | Agents and workflows; Claude Code; Security and safety of LLM applications; Evaluation, testing and debugging; | 23 KB | not started |
| 23 | Cloud Providers: Google Cloud, AWS, Azure & Certifications (1/2) | Google Cloud — compute; Google Cloud — storage and databases; Google Cloud — networking; Google Cloud — data a | 23 KB | not started |
| 24 | Cloud Providers: Google Cloud, AWS, Azure & Certifications (2/2) | Google Cloud — mapping system-design components; AWS; AWS command line; Azure; Azure command line; AWS and Azu | 22 KB | not started |
| 25 | Published ML System-Design Case Studies (1/5) | Recommend / personalize / feed | 29 KB | not started |
| 26 | Published ML System-Design Case Studies (2/5) | Search / rank / ads | 15 KB | not started |
| 27 | Published ML System-Design Case Studies (3/5) | Forecast / ETA / demand; Fraud / trust & safety | 20 KB | not started |
| 28 | Published ML System-Design Case Studies (4/5) | LLM / genAI apps; NLP / text / support; CV / video / OCR; Speech / audio; Marketing / churn / CLV / notify; Av | 23 KB | not started |
| 29 | Published ML System-Design Case Studies (5/5) | Other (pricing, classification, routing, dimensions and more) | 41 KB | not started |

Notes
- Part 05 holds only the Python and shell topic groups. The Programming exercises (a tested Python command-line program, the NumPy and FastAPI items, the from-scratch test runner) sit in the Exercises group of part 07, and the Programming capstone is stated in each Programming part's rules file.
- Where a domain is split, each part's rules file repeats that domain's prerequisites, depth bar and capstone (short). The Learning method is not repeated; it is in `index/00_learning_method.md`.
- The learning record (mastery states, overrides, resume point) stays in `pending_tracker.md` and the handoff; this file only says which part of the index is currently ingested.
