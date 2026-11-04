# Unified Cloud Curriculum: Networks → Cloud Compute → Cryptography and Security → Distributed Systems → Storage → Big Data → Cloud Operations

**Built:** 2026-11-04 (UTC), from `cloud-computing.txt` (13 NPTEL course outlines: GCF, CN, ACN, PCS, CSP, EH, CNS, TPMC, FOC, ADS, CCDS, DS, BDC), under `Master_Rules.md`, Part III.1 (starting a course: generate the full structure first).
**Status:** one unified document: the curriculum structure with, inside every content unit, an NPTEL-style assignment and its key (collapsed), and a from-scratch Python guideline (default, not a prohibition). It follows the same method as the earlier `unified_curriculum.md` (mathematics, machine learning, deep learning, LLMs) and is a **separate file**; the two can be merged later (see Appendix D). Coverage was checked by script: all 154 source cells (course weeks and outlines) are cited by at least one unit and the words of each cell occur in the units that cite it; the few atoms the script still flags are listed and reviewed in Appendix E.

---

## How to read this document

1. **Parts and domains.** Five parts, 13 domains (D1–D13). Each domain has an aim, named benchmarks and units.
2. **Units.** A unit (`U<domain>.<n>`) is a group of related topics. Each has: **Sources** (generated: which source course weeks or outline cells it absorbs), **Topics** (every topic and subtopic, merged across sources and kept close to the sources' own words), **Results** (the theorems and formulas it teaches, each with a proof status), **Build** (the from-scratch implementation, with a cost tag) and **Gap-fills** (what a unit adds that no source names, marked *inferred* with the reference). Bridge units start with a **Bridge for:** line naming the units that need them.
3. **Assignments.** Each content unit ends with its **Assignment** (`A<domain>.<n>`): five questions, with the key in a collapsed block that you open only after an attempt. The six capstones (D13) are projects with their own acceptance criteria and carry no assignment.
4. **Proof-status tags** on results: **[P]** prove in full; **[D]** derive with every step; **[S]** proof sketch (the reason a full proof is not given is stated); **[X]** stated, proof deferred (the unit that will prove it, or "beyond course scope", is named); **[Def]** definition, not proved; **[check]** verified by a script in the unit's Build.
5. **Source keys** (for example `GCF`, `CNS`) are listed in Appendix A. `W3` means Week 3 of that course; `o` means the course's outline or about-text.
6. **Merging rule.** Where several courses cover the same ground (three cryptography courses, four distributed-systems courses, three networking courses, four security and privacy courses), they are merged into one unit at the deepest source level and every source week is cited. The overlap is the point of unifying.
7. **Honesty conventions.** *Recalled, not checked* marks a claim from memory (benchmark titles, formulas of standard results). *Inferred* marks a gap-fill with its reference. Facts checked on the web are named as such, with what was checked (Appendix F).

## Course profile (Master Rules II.1)

| Item | Value |
|---|---|
| **Aim** | Expert-level command of how the cloud works from the wire to the data centre and the managed service: networks and Internet protocols, virtualization and cloud compute, cryptography and its provable security, ethical hacking and defence, security governance, risk and privacy, distributed-systems theory and the industrial systems built on it, cloud storage and databases, big-data engines, and cloud operations and machine learning on Google Cloud. Every mechanism is also implemented from scratch at toy scale. |
| **Starting level** | School mathematics, one programming language (Python), and basic IT. Everything else, including probability, queueing, graph algorithms, coding theory, number theory, operating-system fundamentals, SQL and machine-learning basics, is taught by bridge units placed just before the topic that needs it (Master Rules 3.3). Appendix C maps each prerequisite the sources state to where it is handled. |
| **Benchmarks** | Named per domain in each domain's intro. Titles marked *recalled, not checked* have not been verified against the book itself. Appendix F lists what was checked. |
| **Learner's standing instructions (recorded as overrides, Master Rules 0.3)** | (1) Build a unified curriculum from the source file in the same way as the earlier one, with the prerequisites wired in. (2) A prerequisite bridge is taught just before the concept that demands it begins, in academic depth. (3) Weekly assignments, with from-scratch Python implementations where necessary. (4) Unify all topics and concepts into a single file. (5) Carried over from the earlier work: NPTEL-style assignments (MCQ, multiple select, numerical, prove or derive, programming; 10 marks; pass at 7/10) and from-scratch Python as the default, where NumPy-first is "not strict ... more of a suggestion. Feel free to design as needed." (6) Nothing may be omitted: every source topic and subtopic is covered. |
| **Acceptance gates (6.7)** | Formatter clean (`ruff format --check`), linter clean (`ruff check`), `pytest` passes, known-answer tests pass where standards publish them (hash, cipher and checksum vectors), results within stated tolerance of an oracle (a library, a closed form or a brute-force check), and every simulation is deterministic for a given seed and checked by invariants (DSim). No hidden failure. |
| **Layer order for a topic (3.6)** | Concept and intuition → formal statement and derivation → from-scratch build → professional tool → real-world application and limits → check and close. A tool is used after the thing it automates has been built by hand (6.8). |
| **Real-world lens (II.6)** | Name it, touch it in a lab, design with it. Every Build line carries a cost tag: **[local]** runs on your machine with no cloud spend; **[local VM]** runs in a local virtual machine or container, and for any security lab on a host-only network that you own; **[credit]** spends cloud credit and is optional, with a budget alert set first and the teardown script written before the create script; **[plan only]** write the plan and the scripts but do not run them (they would spend money or touch systems that are not yours); **[learning only]** hand-built security code that is never deployed. |
| **Safety and cost (Master Rules 11)** | Lab-only. No scanning, probing or attacking anything you do not own or have written permission to test. No malware or exploit authoring: offensive topics appear as Python models, simulations or standard tools inside an isolated host-only lab. Local first. No secrets in code, notes or history. A work account is never used for labs (11.4); use a temporary lab project or a personal account with a budget alert. Hand-built cryptographic and security code is for learning and is never deployed. The legal-and-regulatory units (U8.9) are teaching tools and are not legal advice. |
| **Pacing (2.7, 8.5)** | The sources' durations (8 or 12 weeks) describe their own pacing only. Here the learner advances by passing checks, never by the calendar. |
| **Default tooling (from-scratch guideline, flexible)** | (1) Write the mechanism you are learning by hand first. (2) The default toolbox is the Python standard library (sockets, `subprocess`, `struct`, `hashlib` for oracles only, `multiprocessing`) plus NumPy and Matplotlib, because they keep every step visible. (3) This is a **guideline, not a prohibition**: where another tool serves the learning goal, use it, and the unit's Build line names it (for example Wireshark and `tcpdump` for packet work, Mininet or network namespaces for topologies, `nmap` and Metasploit only inside the isolated lab, PySpark and Kafka in the local lab, `gcloud` for the cloud steps). (4) Libraries serve as **oracles** in tests of the from-scratch version (`cryptography`, `networkx`, SQLite, `re`, PySpark, scikit-learn). |
| **Assignments (NPTEL style)** | One per content unit (132, A1.1–A12.3). Five questions: MCQ (1 mark), multiple select (2; all correct options and none wrong), numerical answer (2), prove or derive (2), programming (3); 10 marks. **Pass** at 7/10 with the derivation and the code both accepted (Master Rules 6.12). **Attempt before any hint.** The tutor never writes graded work (6.13). Every numerical key was computed by running its expression. |
| **Capstones (9.6)** | U13.1–U13.6: a user-space TCP/IP stack, a secure channel from your own primitives, a replicated sharded key-value store, an end-to-end data platform, a small service on Google Cloud, and a security programme for a synthetic organisation. |
| **Shared simulator** | **DSim**, a deterministic discrete-event distributed-systems simulator (seeded delays, loss, duplication, crashes, partitions, an invariant checker), is built in U9.1 and reused through D9, D10, D11 and the capstones. Network and security units before U9.1 use smaller purpose-built simulators. |
| **Record** | The list of units in this document is the record template. Initial state: every unit not started, no evidence; resume point U1.1. The live record (mastery states, misconception register, error log, decision journal) belongs in your tracker file (Master Rules 8.3). |

## Domain map

| Part | Domain | Units | Absorbs mainly |
|---|---|---|---|
| A. Foundations | D1 Orientation | U1.1–U1.3 | GCF, CCDS |
|  | D2 Computer networks and the Internet protocols | U2.1–U2.14 | CN, EH |
|  | D3 Advanced networking | U3.1–U3.12 | ACN |
|  | D4 Cloud compute | U4.1–U4.8 | CCDS, GCF |
| B. Cryptography and security | D5 Cryptography | U5.1–U5.25 | TPMC, CNS, FOC, EH |
|  | D6 Ethical hacking and technical security | U6.1–U6.10 | EH, CSP |
|  | D7 Security operations frameworks and cloud security | U7.1–U7.7 | PCS, CSP |
|  | D8 Governance, risk, resilience and privacy | U8.1–U8.10 | CSP, PCS |
| C. Distributed systems and storage | D9 Distributed systems | U9.1–U9.22 | DS, ADS, CCDS |
|  | D10 Cloud storage and databases | U10.1–U10.7 | BDC, ADS, CCDS |
| D. Big data and cloud operations | D11 Big data and cloud analytics | U11.1–U11.11 | BDC, CCDS, DS |
|  | D12 Cloud operations and machine learning on Google Cloud | U12.1–U12.3 | GCF |
| E. Capstones | D13 Capstones | U13.1–U13.6 | none (assembles all) |

## Default order (a plan, not a cage: Master Rules 3.3)

Three spines run side by side after the orientation; take them in any interleaving that respects the arrows. The bridges are placed so that no unit meets a prerequisite before it has been taught.

| Stage | Units | Why here |
|---|---|---|
| 1 | D1 (U1.1–U1.3) | What the cloud is, the Google Cloud resource hierarchy, billing and the lab protocol. U1.2 (shell, Python, regular expressions, Git) is the toolbox for every later lab. |
| 2 | U2.1 → U2.14 | The Internet protocol stack. U2.1 (probability and queueing), U2.7 (graph algorithms) and U2.11 (coding theory) are bridges placed before the delay, routing and error-control units that use them. |
| 3 | U3.1 → U3.12, U4.1 → U4.8 | High-performance routers, QoS, SDN, NFV, data centres and named-data networking; then operating-system and architecture foundations (U4.1), virtualization, containers, cloud networks (U4.8), autoscaling. U3.1 (lookup structures), U3.2 (matching) and U4.5 (flows and LP) are bridges. |
| 4 | U5.1 → U5.25 | Cryptography from classical ciphers to provable security and protocols. Bridges: probability and entropy (U5.1), number theory (U5.12), complexity and reductions (U5.8). |
| 5 | U6.1 → U6.10, U7.1 → U7.7, U8.1 → U8.10 | Ethical hacking in the isolated lab, defence frameworks and cloud IAM, governance, risk, resilience and privacy. U8.2 (quantitative risk) is a bridge. |
| 6 | U9.1 → U9.22 | Distributed systems: DSim, gossip, peer-to-peer, time, snapshots, mutual exclusion, election, consensus, consistency, transactions, recovery, ordering, blockchains. U9.1, U9.2 and U9.17 are bridges. |
| 7 | U10.1 → U10.7, U11.1 → U11.11 | Storage and databases (U10.1 is the SQL bridge), then big-data engines, messaging, streaming and graph processing. U11.8 (machine learning) and U11.10 (Markov chains and PageRank) are bridges. |
| 8 | U12.1 → U12.3, U13.1 → U13.6 | Cloud operations and machine learning on Google Cloud, then the capstones. |

Stages 4 to 5 (security) and stage 6 to 7 (systems and data) can be interleaved with stage 3 once stage 2 is done, if you prefer to reach distributed systems sooner. Within a stage, follow the unit order.


# PART A. FOUNDATIONS: THE CLOUD, NETWORKS AND CLOUD COMPUTE

## D1. Orientation: the cloud, Google Cloud Platform and the lab protocol

Aim: a precise picture of what "the cloud" is, how it is priced and operated, and a safe, cost-controlled way to practise on it. Later domains replace each black box with its mechanism (networks D2–D3, virtualization D4, security D5–D8, distributed systems D9–D10, data systems D11–D12). Benchmarks (recalled, not checked): NIST SP 800-145 (cloud definition); Armbrust et al., *A View of Cloud Computing* (CACM 2010); Barroso, Clidaras, Hölzle, *The Datacenter as a Computer*; Google Cloud documentation and the *Google Cloud Fundamentals: Core Infrastructure* course.

### U1.1 What the cloud is: history, service models, deployment models and economics
**Sources:** GCF W0–1, o; CCDS W1, o
- **Topics:** Course introduction (Week 0): aims, structure, hands-on labs, assessment. *So, What's the Cloud anyway? Start with a Solid Platform.* Cloud basics, big data and machine learning, and where and how the Google Cloud Platform fits in. Cloud computing as on-demand delivery of computations, storage, applications and other IT resources through a cloud services platform over the internet with a pay-as-you-go business model. Why clouds, what is a cloud, what's new in today's clouds; cloud computing versus distributed computing; utility computing; features of today's clouds: massive scale. X-as-a-service (the source writes "AAS") classification: HaaS, IaaS, PaaS, SaaS. Data-intensive computing; new cloud paradigms. Categories of clouds: private clouds, public clouds (and hybrid, community, multi-cloud). History and evolution of cloud: time-sharing, clusters and grids, utility computing, virtualization, web services, hyperscale data centers. Types of cloud computing and who operates what in each service model. Outline map of the cloud-and-distributed-systems course (named topics and where taught): an in-depth understanding of distributed computing concepts, distributed algorithms and the techniques that underlie today's cloud computing technologies; virtualization (U4.2), cloud storage with key-value/NoSQL stores (U10.3 to U10.6), cloud networking (U4.4, U4.6, U4.8), fault-tolerance cloud using PAXOS (U9.14), peer-to-peer systems (U9.4, U9.5), classical distributed algorithms such as leader election (U9.10), time and ordering in distributed systems (U9.6), distributed mutual exclusion (U9.8), distributed algorithms for failures and recovery approaches (U9.19), emerging areas of big data (D11) and many others; industry systems such as Apache Spark (U11.4), Google's Chubby and Apache Zookeeper (U9.15), HBase (U10.5), MapReduce (U11.3), Apache Cassandra (U10.4), Google's B4 and Microsoft's Swan (U4.6), and the intimate knowledge of the internals of cloud computing and of how distributed-systems concepts work inside clouds that the course promises.
- **Results:** Statistical-multiplexing economy: for n independent demands with mean μ and standard deviation σ, pooled capacity μn + kσ√n versus n(μ + kσ) when dedicated, so the saving per tenant grows like σk(1 − 1/√n) [D]. Break-even utilisation between on-demand and owned capacity (cost per used hour = price ÷ utilisation) [D]. Elasticity as a queueing statement: a fixed fleet is stable only while demand rate < capacity [D, from U2.1]. NIST essential characteristics are a definition [Def].
- **Build:** a cost model in Python: owned versus on-demand versus committed capacity as utilisation varies; Monte Carlo of pooled versus dedicated capacity for 1…1000 tenants to reproduce the √n law; decision record stating the utilisation above which owning wins. [local]
- **Gap-fills:** *[inferred: NIST SP 800-145; Armbrust 2010, recalled, not checked]* five essential characteristics (on-demand self-service, broad network access, resource pooling, rapid elasticity, measured service), three service models, four deployment models; the shared-responsibility model (taught properly in U7.7); edge computing (taught in U4.4).

**Assignment A1.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Which change best describes the economic shift that the pay-as-you-go cloud model brings compared with owning a data centre?

(A) Fixed capital spending becomes a variable operating cost that can follow demand  
(B) Operating costs become fixed for three years  
(C) Hardware is bought but never maintained  
(D) Capacity can only be added in whole racks

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which of the following are essential characteristics of cloud computing in the usual NIST definition?

(A) On-demand self-service  
(B) Resource pooling  
(C) Measured service  
(D) A mandatory multi-year contract

**Q3 (2 marks, numerical answer (units)).** Each of n = 100 tenants has independent demand with standard deviation sigma = 10 units and wants headroom k = 2 standard deviations. Dedicated capacity gives each tenant headroom k times sigma; a pooled fleet needs headroom k times sigma times the square root of n in total. What is the headroom saved per tenant by pooling?

**Q4 (2 marks, prove or derive; every step with its reason).** For n independent tenants with demand mean mu and standard deviation sigma, derive the pooled capacity needed to cover demand with k standard deviations of headroom and compare it with dedicated capacity. Show that the saving per tenant is k sigma (1 - 1/sqrt n) and state its limit as n grows.

**Q5 (3 marks, programming).** Write a Monte Carlo simulation of n tenants with independent non-negative demand. For n from 1 to 200 estimate the capacity that covers 99 percent of the time when pooled and when dedicated, plot the saving per tenant against the closed-form k sigma (1 - 1/sqrt n), and report the discrepancy.

<details><summary>Key for A1.1 (open only after your attempt)</summary>

- **Q1:** A. The defining shift is from capital to operating expenditure with capacity that follows demand; the other options describe owned or leased fixed capacity.
- **Q2:** A, B, C. On-demand self-service, broad network access, resource pooling, rapid elasticity and measured service are the five; a long contract is not part of the definition.
- **Q3:** 18 units (tolerance ±0.01). Dedicated headroom per tenant is 20; pooled headroom per tenant is 20/10 = 2; the saving is 18, which equals k times sigma times (1 minus 1 over root n).
- **Q4 (marking outline):** Independence gives variance n sigma squared so the total has mean n mu and deviation sigma root n; pooled capacity is n mu plus k sigma root n; dedicated is n times (mu plus k sigma); subtract and divide by n; the limit is k sigma, so the benefit saturates and never exceeds the dedicated headroom.
- **Q5 (what a passing submission shows):** A script with a seeded generator, an empirical 99th-percentile capacity for both cases, a plot or table showing the empirical saving tracking the formula, and a short note on why clipping demand at zero causes small deviations.

</details>

### U1.2 Bridge: Linux shell, scripting, Python for systems work, regular expressions and Git
**Sources:** none (prerequisite bridge, added so that later units rest on taught ground)
Bridge for: every lab from U1.3 on, the byte-level work of U2.3, and the shell and language prerequisites listed for the Google Cloud course (shell scripting, one programming language, SQL; SQL itself is bridged in U10.1).
- **Topics:** Processes and file descriptors, pipes and redirection, exit status, signals, job control; shell grammar: quoting, parameter expansion, globbing, here-documents, functions, `set -euo pipefail`; the core toolbox (`find`, `grep`, `sed`, `awk`, `xargs`, `curl`, `ssh`, `scp`, `tar`); environment variables and secret hygiene (no secret in code, notes or history); regular expressions as regular languages: concatenation, union, Kleene star, NFA and DFA, Thompson construction, why `grep` matching is linear time; Python for systems work: bytes versus str, files, `subprocess`, `argparse`, `json`, virtual environments, threads versus `asyncio`; Git: the commit DAG, content-addressed objects, branches, three-way merge, `.gitignore` for secrets.
- **Results:** Regular expressions and NFAs recognise the same languages (Thompson construction) [P]; NFA simulation runs in O(|text|·|regex|) [D]; a pipeline is a producer–consumer chain whose exit status is the last stage's unless `pipefail` is set [Def]; Git history is a Merkle DAG so a commit hash commits to its whole ancestry [D].
- **Build:** a regex engine (concatenation, `|`, `*`, `+`, `?`, classes) by Thompson NFA simulation, tested against `re`; a small shell that runs pipelines with `os.fork`, `os.pipe`, `os.dup2`, `os.execvp`. [local]
- **Gap-fills:** *[inferred: Kerrisk, The Linux Programming Interface; Sipser Ch.1, recalled, not checked]* POSIX signals semantics, `trap`-based cleanup (used in teardown scripts), shellcheck as the linter.

**Assignment A1.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** In bash, which setting makes a pipeline return a failure status if any stage of it fails?

(A) set -x  
(B) set -o pipefail  
(C) set -u  
(D) set -f

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements about Git are correct?

(A) A commit identifier is a hash that covers the identifiers of its parent commits  
(B) The history forms a directed acyclic graph of hashed objects  
(C) Rewriting an old commit changes the identifiers of all its descendants  
(D) A branch is a full copy of the working directory

**Q3 (2 marks, numerical answer (state visits)).** A Thompson-construction NFA has m states and is simulated on a text of 1,000,000 characters by keeping the set of active states. What is the upper bound on the number of state visits when m = 40?

**Q4 (2 marks, prove or derive; every step with its reason).** Describe the Thompson construction for concatenation, alternation and star and prove that an NFA built for a regular expression with m symbols and operators has at most 2m states and at most two outgoing transitions from every state.

**Q5 (3 marks, programming).** Implement a regular-expression matcher from scratch that builds a Thompson NFA for concatenation, alternation, star, plus and question mark, and simulates it in time proportional to text length times expression size. Test against Python's re.fullmatch on at least 1000 random expression and string pairs.

<details><summary>Key for A1.2 (open only after your attempt)</summary>

- **Q1:** B. pipefail makes the pipeline status that of the last non-zero stage; without it the status is that of the last stage only.
- **Q2:** A, B, C. Hashing the parents makes history a Merkle DAG so a change propagates to descendants; a branch is only a movable pointer, not a copy.
- **Q3:** 40000000 state visits (tolerance ±0). Each character causes at most one visit to each of the m states, giving n times m = 40 million.
- **Q4 (marking outline):** By induction on the expression: a symbol uses two states; alternation and star add two new states and epsilon edges; concatenation merges two states; so states are at most twice the size; each new state has two out-edges and old states gain none beyond their one extra edge, so the bound holds.
- **Q5 (what a passing submission shows):** A matcher with a parser, an NFA builder and a state-set simulation, a randomised differential test that finds no disagreement, and a timing plot showing linear growth in text length.

</details>

### U1.3 Google Cloud Platform core infrastructure and the lab protocol
**Sources:** GCF W1, o
- **Topics:** Google Cloud Platform overview; core infrastructure; the resource hierarchy (organization, folders, projects), project name, ID and number; billing accounts, budgets and alerts; regions and zones; the Cloud Console, Cloud Shell and the `gcloud` grammar (`gcloud <group> <command> --flags`, `--format=json`, configurations); enabling APIs, quotas; a first look at IAM members, roles and policies (taught in U7.7); the 26 labs on Qwiklabs that are part of the course: lab protocol (temporary lab project and credentials, never a work account), cost tag per lab, budget alert before any paid resource, same-day teardown; free tier, credits and student programmes.
- **Results:** IAM policy inheritance down the hierarchy is a union of allows [Def]; per-second billing arithmetic and cost of an idle resource over a month [D]; teardown-first rule: every create has a recorded delete [Def].
- **Build:** a cost report script that parses recorded `gcloud billing`/pricing JSON (replay-first) and flags idle spend; write the teardown script before the create script for the first lab. [plan only + local]
- **Gap-fills:** *[checked against press and Google pages this session]* Qwiklabs was acquired by Google in November 2016, became Google Cloud Skills Boost in October 2021 and is now part of Google Skills (announced October 2025), with a monthly free credit allowance that changes; the course's own lab list is not in the source (Appendix F). Product names change often (Stackdriver became the operations suite in 2020; Cloud AI Platform and AutoML became Vertex AI in 2021; AI Platform access ended 31 January 2025): verify names in the console before relying on them.

**Assignment A1.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** An IAM allow policy is attached to a folder in the Google Cloud resource hierarchy. To which resources does it apply?

(A) Only the folder object itself  
(B) Every project and resource beneath that folder  
(C) Only the organisation node  
(D) Nothing until it is copied to each project

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which of these belong to the lab protocol of this curriculum?

(A) Set a budget alert before creating billable resources  
(B) Tear down all resources on the same day  
(C) Use a work account for convenience  
(D) Record a delete action for every create action

**Q3 (2 marks, numerical answer (currency units)).** An idle virtual machine is billed at a hypothetical rate of 0.04 currency units per hour. What does it cost if left running for 30 days?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that, with allow policies that are inherited as a union and no deny rules, granting a role at a parent can never reduce the permissions a principal has on any descendant resource.

**Q5 (3 marks, programming).** Write a script that reads a JSON plan listing create and delete actions with resource names and hourly rates and checks that every create has a matching delete, then reports the worst-case cost if the deletes were delayed by 24 hours.

<details><summary>Key for A1.3 (open only after your attempt)</summary>

- **Q1:** B. Allow policies are inherited down the hierarchy and the effective set is the union of the allows on the path.
- **Q2:** A, B, D. The protocol requires budget alerts, same-day teardown and a recorded delete for each create; work accounts must never be used.
- **Q3:** 28.8 currency units (tolerance ±0.05). There are 720 hours in 30 days and 720 times 0.04 is 28.8.
- **Q4 (marking outline):** The effective set at a descendant is the union of the bindings at every ancestor and at the resource; adding a binding at a parent adds a set to that union; union is monotone, so the permission set can only grow.
- **Q5 (what a passing submission shows):** A validator that rejects an unmatched create, a cost calculation from the rates, test plans that pass and fail, and a clear report; no real credentials or cloud calls are used.

</details>

## D2. Computer networks and the Internet protocols

Aim: command of the TCP/IP stack top to bottom: every protocol built, simulated and measured at toy scale, with the mathematics (queueing, graph algorithms, coding theory, probability) taught as bridges just before the topic that uses it. Benchmarks (recalled, not checked): Kurose and Ross, *Computer Networking: A Top-Down Approach*; Peterson and Davie, *Computer Networks: A Systems Approach*; Tanenbaum and Wetherall, *Computer Networks*; Stevens, *TCP/IP Illustrated*; Forouzan, *Data Communications and Networking* and *TCP/IP Protocol Suite* (named in the Ethical Hacking source); Stallings, *Data and Computer Communications*; Bertsekas and Gallager, *Data Networks*; Kleinrock, *Queueing Systems*.

### U2.1 Bridge: probability, random processes and queueing for networks
**Sources:** none (prerequisite bridge, added so that later units rest on taught ground)
Bridge for: U2.2 (statistical multiplexing, delay), U2.13 (ALOHA), U3.3 (head-of-line blocking), U3.6 (scheduling), U4.7 (autoscaling), U12.1 (SLO arithmetic).
- **Topics:** Sample spaces, events, conditional probability, Bayes' rule, independence; random variables, expectation, variance, linearity of expectation; binomial, geometric, Poisson and exponential distributions; the memoryless property; the Poisson process (three equivalent definitions, superposition, thinning); continuous-time Markov chains and birth–death chains; the M/M/1 queue: stationary distribution, mean number in system, mean delay, utilisation; Little's law; M/M/c and Erlang C; M/M/1/K and blocking; M/G/1 and the Pollaczek–Khinchine formula; bandwidth–delay product as the "pipe" volume.
- **Results:** Exponential is the only memoryless continuous distribution [P]; superposition of independent Poisson processes is Poisson [P]; M/M/1 stationary law π_n = (1−ρ)ρⁿ [D]; mean number ρ/(1−ρ) and delay 1/(μ−λ) [D]; Little's law L = λW for any stable system [P]; Erlang C waiting probability [D]; Pollaczek–Khinchine mean wait [S, proof needs residual-life argument].
- **Build:** a discrete-event simulator (event heap) for M/M/1 and M/M/c, with confidence intervals checked against the formulas; a Little's-law auditor that recomputes L, λ, W from event logs. [local]
- **Gap-fills:** *[inferred: Kleinrock; Bertsekas–Gallager; recalled, not checked]* PASTA (statement), Jackson networks (statement), heavy-tail traffic and self-similarity as a caveat to Poisson models.

**Assignment A2.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Which continuous distribution is memoryless?

(A) Uniform  
(B) Exponential  
(C) Normal  
(D) Pareto

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are true?

(A) The superposition of independent Poisson processes is a Poisson process  
(B) Little's law needs exponential service times  
(C) Little's law L = lambda W holds for any stable system  
(D) The mean delay of an M/M/1 queue grows without bound as the load tends to one

**Q3 (2 marks, numerical answer (s)).** An M/M/1 queue has arrival rate 8 packets per second and service rate 10 packets per second. What is the mean time a packet spends in the system?

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the stationary distribution of an M/M/1 queue from the global balance equations and use it to show that the mean number in system is rho/(1-rho).

**Q5 (3 marks, programming).** Write an event-driven M/M/1 simulator and compare the estimated mean number in system and mean delay with the formulas for load 0.5, 0.8 and 0.95, with confidence intervals. Check Little's law on the simulated trace.

<details><summary>Key for A2.1 (open only after your attempt)</summary>

- **Q1:** B. Only the exponential law satisfies the conditional probability of exceeding s+t given exceeding s equals the probability of exceeding t among continuous distributions.
- **Q2:** A, C, D. Superposition and Little's law hold in general; Little's law does not need exponential service; M/M/1 delay is 1/(mu - lambda) which diverges as the load tends to 1.
- **Q3:** 0.5 s (tolerance ±0.001). The mean delay is 1/(mu minus lambda) = 0.5 seconds.
- **Q4 (marking outline):** Cut equations lambda pi_n = mu pi_{n+1} give pi_n = rho^n pi_0; normalise with the geometric series to get pi_0 = 1 - rho; the mean is the sum of n pi_n which equals rho/(1-rho).
- **Q5 (what a passing submission shows):** A seeded simulator with warm-up removal and batch means, a table of estimates against formulas with intervals, Little's law verified within error, and a note on why the estimates degrade at load 0.95.

</details>

### U2.2 Introduction to computer networks: history, circuit switching and packet switching
**Sources:** CN W1, o
- **Topics:** Objectives: (i) architecture and principles of today's computer networks, (ii) protocols and their functionalities, (iii) requirements for the future Internet and its impact on network architecture; growth of the Internet from traditional circuit-switched and packet-switched small-scale networks to modern high-speed mobile and wireless Internet; methods, architectures and designs at every protocol level for a secure and highly dependable information technology infrastructure; the top-down approach. *Introduction to Computer Networks History:* ARPANET, packet switching (Baran, Davies, Kleinrock), TCP/IP adoption, NSFNET, the Web. Network edge, access networks and the core. *Circuit Switching and Packet Switching:* FDM and TDM circuits, store-and-forward packet switching, statistical multiplexing, datagram versus virtual-circuit service. Delays: nodal processing, queuing, transmission and propagation; loss; throughput and bottleneck links; bandwidth–delay product; traceroute as a delay probe. Outline map of the networks course: a top-down approach covering the different protocols of the TCP/IP protocol stack, and touching on the next generation computer networks (the future Internet, U2.14 and D3), where a large number of methods are surveyed and the broad objective is to understand how the layers fit together.
- **Results:** End-to-end store-and-forward delay over N links of rate R for a packet of L bits: N·L/R plus propagation [D]; pipelining gain of splitting a message into packets [D]; capacity of a circuit versus packet network for bursty users: P(more than c of n users active) by the binomial law [D]; queueing delay grows without bound as traffic intensity La/R → 1 [D, from U2.1].
- **Build:** a store-and-forward link model validated against the delay formula; a binomial calculator showing how many bursty users a packet-switched link supports versus a circuit-switched one; a traceroute-output parser that reconstructs per-hop delay. [local]
- **Gap-fills:** *[inferred: Kurose–Ross Ch.1; Peterson–Davie Ch.1]* access technologies (DSL, cable, fibre, cellular, Wi-Fi), protocol layering preview, brief network-security threat overview (taught in D6).

**Assignment A2.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** A message of L bits crosses N links, each of rate R, using store-and-forward without queueing and ignoring propagation delay. What is the end-to-end delay?

(A) L/R  
(B) N L/R  
(C) L/(N R)  
(D) N R/L

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which are advantages of packet switching over circuit switching for bursty traffic?

(A) Statistical multiplexing of the link  
(B) No call set-up is needed  
(C) A guaranteed fixed bandwidth for every call  
(D) Efficient use when sources are idle part of the time

**Q3 (2 marks, numerical answer).** Ten users each transmit with probability 0.1 independently at any instant. A packet-switched link can carry three simultaneous transmitters. What is the probability that more than three are active?

**Q4 (2 marks, prove or derive; every step with its reason).** A message of M bits is split into P packets of M/P bits and sent over N store-and-forward links of rate R. Derive the delay and show that it is smaller than N M/R when P is greater than one.

**Q5 (3 marks, programming).** Simulate on-off sources sharing a packet-switched link and the same sources on a circuit-switched link with the same capacity, and estimate the blocking probability for circuits and the overflow probability for packets as the number of users grows.

<details><summary>Key for A2.2 (open only after your attempt)</summary>

- **Q1:** B. Each of the N links must receive the whole message before forwarding it, so the delays add up to N L/R.
- **Q2:** A, B, D. Packet switching shares the link and needs no set-up; guaranteed bandwidth is a property of circuit switching.
- **Q3:** 0.0128 (tolerance ±0.0005). The probability is one minus the binomial sum for 0 to 3 active users, about 0.0128.
- **Q4 (marking outline):** The first packet needs N (M/P)/R to arrive; each remaining packet arrives one packet-time later; total is (N + P - 1) M/(P R); this is less than N M/R because (N + P - 1)/P is less than N when P exceeds 1 and N exceeds 1.
- **Q5 (what a passing submission shows):** A seeded simulator, estimated probabilities with confidence intervals compared with the binomial formula, and a plot showing where packet switching supports more users.

</details>

### U2.3 The TCP/IP protocol stack: layering, encapsulation, bytes and sockets
**Sources:** CN W2; EH W1
- **Topics:** TCP/IP protocol stack, basic overview: application, transport, network, link and physical layers; comparison with the OSI reference model; protocols, services, interfaces and service access points; encapsulation and decapsulation of protocol data units; header formats for Ethernet, IPv4, UDP and TCP; port numbers and the socket API; network byte order. Introduction to ethical hacking: what it is, scope, legality and rules of engagement (developed in U6.1). Fundamentals of computer networking; TCP/IP protocol stack.
- **Results:** Layering as information hiding with a cost: header overhead arithmetic for a TCP/IPv4/Ethernet stack [D]; the Internet checksum (one's-complement sum) is independent of byte order and can be updated incrementally [P]; a socket pair identifies a connection [Def].
- **Build:** an encoder and decoder for Ethernet, IPv4, UDP, TCP and ICMP headers with `struct`; the Internet checksum; a synthetic-capture writer and a pcap-style reader; loopback echo servers over TCP and UDP. Then Wireshark or `tcpdump` on loopback as the professional tool, naming what it decodes that the toy did not. [local]
- **Gap-fills:** *[inferred: Stevens, TCP/IP Illustrated; Tanenbaum]* OSI versus Internet critique, socket options, loopback and namespaces for lab isolation (used from U2.12).

**Assignment A2.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** How many header bytes does a TCP segment without options carry over IPv4 over Ethernet, excluding preamble and frame check sequence?

(A) 40  
(B) 54  
(C) 58  
(D) 74

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which properties does the Internet checksum have?

(A) It is a one's-complement sum of 16-bit words  
(B) It does not depend on byte order  
(C) It can be updated incrementally when a field changes  
(D) It detects every possible two-bit error

**Q3 (2 marks, numerical answer).** A TCP segment carries 1460 bytes of payload with 54 bytes of headers. What fraction of the transmitted bytes is payload?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that the Internet checksum is independent of byte order, in the sense that computing it on byte-swapped words gives the byte-swapped checksum.

**Q5 (3 marks, programming).** Implement the Internet checksum and the incremental update of RFC 1624, check them against random packets, and write a length-prefixed echo server and client using sockets on loopback.

<details><summary>Key for A2.3 (open only after your attempt)</summary>

- **Q1:** B. TCP 20 plus IP 20 plus the Ethernet header 14 gives 54 bytes.
- **Q2:** A, B, C. The first three hold; two compensating bit flips in the same bit position of different words are not detected, so the last is false.
- **Q3:** 0.9643 (tolerance ±0.001). The efficiency is 1460 divided by 1514, about 0.964.
- **Q4 (marking outline):** End-around-carry addition is commutative and associative; swapping the bytes of every word multiplies each word by 256 modulo 65535 and so does the sum; hence the swapped inputs give the swapped sum and the complement is swapped too.
- **Q5 (what a passing submission shows):** Functions with tests showing the incremental update equals a full recomputation, and a socket pair that echoes framed messages including partial reads and several messages in one segment.

</details>

### U2.4 Application layer services: HTTP, FTP, email and DNS
**Sources:** CN W3
- **Topics:** Application layer services. HTTP: request and response format, methods, status codes, persistent connections and pipelining (HTTP/1.1), cookies, web caching with conditional GET, proxies; HTTP/2 multiplexing and HTTP/3 over QUIC. FTP: separate control and data connections, active versus passive mode. Email: SMTP, POP3, IMAP, MIME. DNS: hierarchy of root, TLD and authoritative servers, recursive versus iterative resolution, resource records (A, AAAA, CNAME, NS, MX, TXT), caching and TTL, message format. Client–server versus peer-to-peer architectures; the socket programming interface.
- **Results:** Page-load time model: non-persistent costs 2 RTT per object plus transmission, persistent with pipelining about one RTT for all objects [D]; cache hit-rate effect on average delay and on access-link utilisation [D]; DNS iterative resolution cost in RTTs with and without caching [D].
- **Build:** an HTTP/1.1 server and client from sockets (Content-Length, chunked transfer, keep-alive, conditional GET); a DNS wire-format encoder and decoder with name compression and an iterative resolver over a local fake hierarchy; an SMTP dialogue state machine on loopback. [local]
- **Gap-fills:** *[inferred: Kurose–Ross Ch.2; RFC 9110/9114/9000 recalled, not checked]* CDNs and DNS redirection (revisited in U3.11), TLS on top of HTTP (U5.18), DNS and email security (U6.5).

**Assignment A2.4** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Which DNS record type maps a host name to an IPv4 address?

(A) A  
(B) MX  
(C) NS  
(D) CNAME

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements about HTTP/1.1 are correct?

(A) Persistent connections reuse one TCP connection for several objects  
(B) Pipelining reduces the number of round trips  
(C) Persistent connections remove the need for DNS lookups  
(D) Every object requires a new handshake

**Q3 (2 marks, numerical answer (s)).** A page has one base file and 10 embedded objects. With non-persistent HTTP, each object costs two round trips and no parallelism is used; the round-trip time is 50 ms. Ignoring transmission time, what is the page load time?

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the page-load time of a page with n objects of size S on a link of rate R and round-trip time T for non-persistent HTTP without parallel connections and for persistent HTTP with pipelining.

**Q5 (3 marks, programming).** Implement a small HTTP server and client over loopback with an injected delay of 50 ms per round trip and measure the time to fetch 20 objects with new connections, with a persistent connection and with pipelining.

<details><summary>Key for A2.4 (open only after your attempt)</summary>

- **Q1:** A. The A record holds an IPv4 address; MX names mail servers, NS name servers and CNAME an alias.
- **Q2:** A, B. Reuse and pipelining save round trips; DNS is still needed and a new handshake per object is the non-persistent mode.
- **Q3:** 1.1 s (tolerance ±0.001). There are 11 objects at 2 round trips each, which is 22 round trips of 0.05 s, or 1.1 s.
- **Q4 (marking outline):** Non-persistent: n+1 objects each cost 2T plus S/R, total (n+1)(2T + S/R); persistent with pipelining: one connection set-up 2T for the base and about one T for the rest plus the transmission time, roughly 2T + T + (n+1)S/R; subtract to show the saving.
- **Q5 (what a passing submission shows):** Measurements showing the predicted ordering and magnitudes, a table against the model, and a note on head-of-line blocking in pipelining.

</details>

### U2.5 Transport layer I: connection establishment and closure, reliable transfer and flow control
**Sources:** CN W4–5; EH W2
- **Topics:** Transport layer primitives; multiplexing and demultiplexing; UDP and its checksum; TCP and UDP compared; connection establishment (three-way handshake, initial sequence numbers, delayed duplicates) and closure (four-way close, half-close, TIME_WAIT, reset); principles of reliable data transfer: rdt1.0 to rdt3.0, stop-and-wait, pipelining, Go-Back-N and Selective Repeat; sliding windows and flow control (receiver window); utilisation of pipelined protocols. *Flow Control and Congestion Control at the Transport Layer* (flow control here, congestion control in U2.6).
- **Results:** Stop-and-wait utilisation (L/R)/(RTT + L/R) and window needed to fill the pipe [D]; Selective Repeat needs window ≤ half the sequence space and Go-Back-N window ≤ N−1 [P]; three-way handshake rejects old duplicate SYNs [D]; TIME_WAIT lasts 2·MSL to protect a new incarnation from stray segments [D].
- **Build:** stop-and-wait, Go-Back-N and Selective Repeat over a simulated lossy, reordering, duplicating link with a property test (in order, exactly once, nothing invented); throughput versus loss and window; the TCP connection state machine as a table-driven checker of segment traces. [local]
- **Gap-fills:** *[inferred: Kurose–Ross Ch.3; Peterson–Davie Ch.5]* the Two Generals problem (revisited as an impossibility in U9.12); SYN flood preview (U6.5).

**Assignment A2.5** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** With k-bit sequence numbers, what is the largest safe window for Go-Back-N?

(A) 2^k  
(B) 2^k - 1  
(C) 2^(k-1)  
(D) 2^k - 2

**Q2 (2 marks, multiple select; all correct options and no wrong option).** What does the three-way handshake accomplish?

(A) It synchronises initial sequence numbers  
(B) It prevents an old duplicate SYN from creating a connection  
(C) It encrypts the data  
(D) It confirms that both ends are ready

**Q3 (2 marks, numerical answer (segments)).** A path has rate 1 Gbit/s and a round-trip time of 30 ms; segments are 1500 bytes. How many segments must be in flight to keep the path full?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that Selective Repeat needs a window of at most half the sequence-number space, by constructing the ambiguity that arises when the window is larger.

**Q5 (3 marks, programming).** Implement Go-Back-N and Selective Repeat over a simulated channel with loss and delay and measure goodput against loss rate and window size, verifying that the delivered stream equals the sent stream.

<details><summary>Key for A2.5 (open only after your attempt)</summary>

- **Q1:** B. Go-Back-N needs the window to be at most 2^k - 1 so that a full window of lost acknowledgements is not mistaken for new data.
- **Q2:** A, B, D. The handshake agrees sequence numbers and rejects stale duplicates; it provides no encryption.
- **Q3:** 2500 segments (tolerance ±1). The bandwidth-delay product is 30 million bits, which is 3.75 million bytes or 2500 segments.
- **Q4 (marking outline):** Take a window W and sequence space S with W greater than S/2; if all acknowledgements for a window are lost the sender retransmits the old packets while the receiver expects the next window; the sequence numbers overlap so old and new packets are indistinguishable; therefore W is at most S/2.
- **Q5 (what a passing submission shows):** A simulator with both protocols, goodput curves against the analytic utilisation, and an equality check on the delivered byte stream under reordering and loss.

</details>

### U2.6 Transport layer II: TCP, congestion control and fairness
**Sources:** CN W5–6
- **Topics:** Transmission Control Protocol, basic features: byte-stream service, segment structure, cumulative and delayed acknowledgements, RTT estimation and timeout (Jacobson and Karels, Karn's rule), fast retransmit, flow control. Congestion control principles: causes and costs of congestion, end-to-end versus network-assisted control, ECN. TCP congestion control: slow start, congestion avoidance, AIMD, Tahoe, Reno, NewReno, SACK, CUBIC and BBR; fairness; TCP over long fat networks; QUIC's transport.
- **Results:** AIMD converges to the fair, efficient point (Chiu–Jain two-flow argument) while MIAD, AIAD and MIMD do not [P]; slow start doubles the window each RTT [D]; steady-state throughput ≈ (MSS/RTT)·√(3/2)/√p from the sawtooth [D]; RTO = SRTT + 4·RTTVAR with EWMA gains 1/8 and 1/4 [Def].
- **Build:** a TCP Reno/NewReno simulator on a drop-tail bottleneck with the sawtooth, validated against the throughput formula; two-flow fairness trajectories; an RTO estimator replayed on RTT traces. Then `iperf3`, `ss -i` and `tc netem` in a Linux VM as the professional tools. [local VM]
- **Gap-fills:** *[inferred: Peterson–Davie Ch.6; RFC 5681 and RFC 6298, recalled, not checked]* delay-based and model-based control (Vegas, BBR), data-center transport (DCTCP, revisited in U3.10).

**Assignment A2.6** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Which increase and decrease rule pair converges to a fair and efficient allocation for two competing flows?

(A) Multiplicative increase, multiplicative decrease  
(B) Additive increase, additive decrease  
(C) Additive increase, multiplicative decrease  
(D) Multiplicative increase, additive decrease

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements about TCP are correct?

(A) Slow start doubles the window each round trip  
(B) Three duplicate acknowledgements trigger fast retransmit  
(C) The retransmission timeout is the smoothed RTT plus four times the RTT variation  
(D) Reno never reduces its window

**Q3 (2 marks, numerical answer (Mbit/s)).** The steady-state throughput of a TCP flow is approximately (MSS/RTT) times the square root of 1.5 divided by the square root of p. With MSS 1460 bytes, RTT 100 ms and loss probability 0.01, what is it in Mbit/s?

**Q4 (2 marks, prove or derive; every step with its reason).** Using the Chiu-Jain two-flow argument, show that additive increase with multiplicative decrease converges to the point of equal and fully used allocation.

**Q5 (3 marks, programming).** Simulate two flows with AIMD sharing a bottleneck and plot their trajectory in the rate plane, then do the same for AIAD, MIMD and MIAD. Compare the steady-state throughput of one flow with random loss to the square-root formula.

<details><summary>Key for A2.6 (open only after your attempt)</summary>

- **Q1:** C. Additive increase moves along the 45-degree line while multiplicative decrease shrinks toward the origin, so the pair approaches the fairness line.
- **Q2:** A, B, C. The first three are standard; Reno halves its window on loss.
- **Q3:** 1.431 Mbit/s (tolerance ±0.02). The first factor is 0.1168 Mbit/s per unit; multiplying by 1.2247 and dividing by 0.1 gives about 1.43 Mbit/s.
- **Q4 (marking outline):** In the plane of the two rates, additive increase moves along a 45-degree line keeping the difference fixed; multiplicative decrease by factor b scales both rates and shrinks the difference by b; the difference therefore shrinks at each decrease and the total oscillates around capacity, converging to the intersection of the fairness and efficiency lines.
- **Q5 (what a passing submission shows):** Trajectory plots that converge only for AIMD, a table comparing measured throughput and the formula within a constant, and a short explanation of the discrepancy.

</details>

### U2.7 Bridge: graph algorithms for routing — shortest paths, spanning trees and distributed relaxation
**Sources:** none (prerequisite bridge, added so that later units rest on taught ground)
Bridge for: U2.9 (routing protocols), U2.12 (spanning tree protocol), U3.7 (controller path computation), U4.6 (traffic engineering), U9.11 (distributed minimum spanning tree).
- **Topics:** Graphs, weighted paths, optimal substructure and the triangle inequality; Dijkstra's algorithm and its correctness; Bellman–Ford and negative cycles; Floyd–Warshall; breadth-first search; spanning trees; minimum spanning trees: cut property, cycle property, Kruskal and Prim; running times with heaps; distributed asynchronous Bellman–Ford and its convergence.
- **Results:** Dijkstra's algorithm is correct for non-negative weights [P]; Bellman–Ford after k rounds gives shortest paths of at most k hops [P]; cut property and cycle property of MSTs [P]; Kruskal and Prim are correct [P]; synchronous distance-vector reaches the fixed point in at most n−1 rounds, but count-to-infinity can occur after a cost increase [D].
- **Build:** all of the above with a binary heap and union–find; a property-test suite using `networkx` only as an oracle. [local]
- **Gap-fills:** *[inferred: CLRS Ch.22–24]* incremental shortest-path updates; ECMP path enumeration.

**Assignment A2.7** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** After k rounds of the Bellman-Ford algorithm, the estimates equal the lengths of which paths?

(A) Shortest paths using at most k edges  
(B) Shortest paths using exactly k edges  
(C) Paths of length k  
(D) All shortest paths

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are true?

(A) Dijkstra's algorithm requires non-negative edge weights  
(B) Prim's algorithm builds a minimum spanning tree  
(C) Kruskal's algorithm needs non-negative weights to be correct  
(D) Distance-vector routing can suffer count-to-infinity after a cost increase

**Q3 (2 marks, numerical answer (links)).** A connected network of 50 routers is connected by a spanning tree. How many links does the spanning tree contain?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove the cut property of minimum spanning trees: for any cut, the lightest edge crossing it belongs to some minimum spanning tree.

**Q5 (3 marks, programming).** Implement Dijkstra, Bellman-Ford, Prim and Kruskal and test them against a library on random graphs. Simulate distance-vector routing on a line of routers after a link cost increase and show count-to-infinity and the effect of split horizon.

<details><summary>Key for A2.7 (open only after your attempt)</summary>

- **Q1:** A. Each round relaxes every edge once, so after k rounds the best path with at most k edges is known.
- **Q2:** A, B, D. Kruskal works with negative weights as well.
- **Q3:** 49 links (tolerance ±0). A spanning tree of n nodes has n minus 1 edges.
- **Q4 (marking outline):** Take an MST T not containing the lightest crossing edge e; add e to create a cycle that crosses the cut again at another edge f; f is not lighter than e; replacing f by e gives a spanning tree of no greater weight, hence also an MST containing e.
- **Q5 (what a passing submission shows):** Four algorithms agreeing with the library on 500 random graphs, a distance-vector simulator that reproduces the slow convergence and shows it removed or reduced by split horizon with poison reverse.

</details>

### U2.8 Network layer: IP addressing, IPv6, NAT, DHCP and ICMP
**Sources:** CN W7; EH W2–3
- **Topics:** Network layer primitives: forwarding versus routing, datagram versus virtual-circuit service; IP addressing: IPv4 format, classful addressing, subnetting and IP subnets, CIDR and VLSM, longest-prefix match, private ranges, NAT and PAT, DHCP, ICMP (ping, traceroute, unreachable), fragmentation and reassembly with path-MTU discovery; IP version 6: 128-bit addresses, fixed header and extension headers, address types and scopes, stateless autoconfiguration, transition by dual stack, tunnelling and translation. IP addressing and routing (EH Week 2 and Week 3 networking part).
- **Results:** CIDR aggregation: the most specific matching prefix wins and summarisation is correct only if the covering prefix contains no foreign address [D]; subnet and host counts 2^k − 2 and VLSM allocation by descending size [D]; fragment offset arithmetic in 8-byte units [D]; IPv6 address space counting [D].
- **Build:** a subnet and VLSM calculator with a minimal route-summarisation algorithm; an IPv6 parser and compressor; a NAT table simulator; fragmentation and reassembly with loss; checked against Python's `ipaddress` as the oracle. [local]
- **Gap-fills:** *[inferred: Kurose–Ross Ch.4; RFC 8200, recalled, not checked]* ICMPv6 and neighbour discovery, DHCPv6, carrier-grade NAT.

**Assignment A2.8** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What is the fixed length in bytes of the IPv6 base header?

(A) 20  
(B) 40  
(C) 60  
(D) 128

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements about IPv4 fragmentation are correct?

(A) The fragment offset field is measured in 8-byte units  
(B) The offset field is 13 bits long  
(C) The more-fragments flag is clear only on the last fragment  
(D) The offset field is measured in single bytes

**Q3 (2 marks, numerical answer (hosts)).** A /26 subnet is carved out of a 32-bit IPv4 space. How many usable host addresses does it hold?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that allocating variable-length subnets in descending order of required size, each aligned on a boundary of its own size, produces non-overlapping blocks that fit in the parent prefix whenever the sum of the rounded-up sizes does not exceed the parent size.

**Q5 (3 marks, programming).** Write a CIDR aggregator and a VLSM allocator and test them against Python's ipaddress module on randomly generated prefix lists and host requirements. Include a case where aggregation would cover a foreign address and show that your code refuses it.

<details><summary>Key for A2.8 (open only after your attempt)</summary>

- **Q1:** B. The IPv6 base header is fixed at 40 bytes; extension headers are chained after it.
- **Q2:** A, B, C. Offsets count 8-byte units in a 13-bit field and the last fragment has the more-fragments flag cleared.
- **Q3:** 62 hosts (tolerance ±0). There are 2^6 = 64 addresses and two are reserved for the network and broadcast addresses, leaving 62.
- **Q4 (marking outline):** Each block size is a power of two and each start address is a multiple of its size; sizes are non-increasing so each later start is a multiple of every later size; consecutive blocks therefore abut without gaps or overlap; the total is the sum of the block sizes, which fits if it does not exceed the parent.
- **Q5 (what a passing submission shows):** Code that matches the ipaddress oracle on random cases, correct refusal of unsafe summaries, and allocation results with no overlap verified by a checker.

</details>

### U2.9 IP routing: intra-domain protocols and inter-domain routing with BGP
**Sources:** CN W8; EH W2–3
- **Topics:** IP routing; intra-domain routing protocols: distance-vector (RIP) and link-state (OSPF, IS-IS), areas and hierarchy; autonomous systems; inter-domain routing protocols (BGP): eBGP and iBGP, path-vector routing, AS_PATH, LOCAL_PREF, MED and NEXT_HOP, the decision process, business relationships (customer, provider, peer) and export policy, route reflectors, hijacks and leaks, RPKI route-origin validation. Routing protocols (EH Week 3); IP addressing and routing (EH Week 2).
- **Results:** Distance-vector count-to-infinity and the partial cure of split horizon with poison reverse [D]; link-state flooding gives every router the same graph so Dijkstra yields loop-free routes [P]; the Gao–Rexford conditions guarantee BGP convergence [S]; the stable paths problem can have no stable solution or several (BAD GADGET and DISAGREE) [D].
- **Build:** distance-vector and link-state routers on an event simulator; a path-vector simulator with customer/provider/peer policies; detect oscillation on BAD GADGET. Then FRRouting or BIRD in Linux network namespaces as the professional tools. [local VM]
- **Gap-fills:** *[inferred: Peterson–Davie Ch.4; Griffin–Shepherd–Wilfong on stable paths, recalled, not checked]* documented BGP hijack and leak incidents should be read from primary operator reports (RIPE, Cloudflare, the networks involved).

**Assignment A2.9** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Which set of conditions on commercial routing policy is known to guarantee that BGP converges?

(A) Shortest-path first  
(B) The Gao-Rexford conditions  
(C) Hot-potato routing  
(D) Random tie-breaking

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Split horizon with poison reverse prevents two-node routing loops  
(B) It rules out count-to-infinity in every topology  
(C) Link-state flooding gives all routers the same topology graph  
(D) The BAD GADGET instance of the stable paths problem has no stable solution

**Q3 (2 marks, numerical answer (operations)).** Dijkstra's algorithm with a binary heap on a network of 100 routers and 300 links takes about (E plus V) times log base 2 of V basic operations. What is that figure?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that link-state routing is loop-free when every router has the same graph and uses shortest-path next hops with a consistent tie-break.

**Q5 (3 marks, programming).** Implement link-state flooding with sequence numbers and Dijkstra route computation, and a distance-vector protocol with split horizon, on a simulated network of routers with link failures. Verify loop-freedom after convergence.

<details><summary>Key for A2.9 (open only after your attempt)</summary>

- **Q1:** B. Gao-Rexford conditions on customer, peer and provider preferences and export rules guarantee convergence to a stable state.
- **Q2:** A, C, D. Poison reverse only helps for two-node loops, so the second option is false.
- **Q3:** 2658 operations (tolerance ±5). The sum E plus V is 400 and log2 of 100 is about 6.64, giving about 2657.
- **Q4 (marking outline):** Each router's next hop toward a destination lies on a shortest path in the common graph; the distance from the next hop to the destination is strictly smaller when weights are positive; following next hops therefore gives a strictly decreasing sequence of distances, which cannot revisit a node.
- **Q5 (what a passing submission shows):** Both protocols running in a simulator, a convergence-time comparison after a link failure, and a checker that follows next hops for every pair and finds no loop after convergence.

</details>

### U2.10 IP services: ARP and SNMP
**Sources:** CN W9
- **Topics:** IP services: ARP request and reply, ARP cache and timeout, proxy ARP, gratuitous ARP, neighbour discovery in IPv6; SNMP: manager, agent and MIB, SMI and ASN.1 with BER encoding, PDUs (Get, GetNext, GetBulk, Set, Trap, Inform), SNMPv1, v2c and v3 (USM authentication and privacy), RMON; the FCAPS network-management model; DHCP and ICMP revisited as management signals.
- **Results:** BER's tag–length–value encoding is unambiguous and self-delimiting [Def]; ARP has no authentication so any host on the segment can answer for any address [D] (defences in U6.4).
- **Build:** a BER encoder and decoder; an SNMP GET responder for a toy MIB over UDP on loopback; an ARP resolver with cache and timeouts on a simulated LAN. [local]
- **Gap-fills:** *[inferred: Stallings, SNMP, SNMPv2, SNMPv3, and RMON; RFC 3411–3418, recalled, not checked]* NETCONF and YANG, streaming telemetry (links to U3.7).

**Assignment A2.10** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Why can ARP cache poisoning work?

(A) ARP replies are encrypted  
(B) ARP has no authentication so any host can answer for any address  
(C) ARP runs over TCP  
(D) ARP uses digital signatures

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements about BER encoding in SNMP are correct?

(A) It uses tag, length and value triples  
(B) It is self-delimiting  
(C) Its decoding is ambiguous without outside information  
(D) SNMP messages are encoded with it

**Q3 (2 marks, numerical answer (bytes)).** In definite long-form BER, a content length of 300 bytes is encoded as one initial byte announcing the number of length bytes followed by the length itself. How many bytes does the length field occupy in total?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that definite-length tag-length-value encoding is uniquely decodable: any byte string that is a concatenation of encoded values decodes in exactly one way.

**Q5 (3 marks, programming).** Write a BER encoder and decoder for integers, octet strings, object identifiers and sequences, build an SNMP GET request with it, and write an ARP request and reply builder and parser. Test the round trip on random values.

<details><summary>Key for A2.10 (open only after your attempt)</summary>

- **Q1:** B. ARP has no authentication; a spoofed reply simply overwrites the cache entry.
- **Q2:** A, B, D. Definite-length BER is unambiguous and self-delimiting, and SNMP uses it.
- **Q3:** 3 bytes (tolerance ±0). 300 needs two bytes, so with the initial byte 0x82 the length field takes three bytes.
- **Q4 (marking outline):** Read the tag, then the length, then exactly that many bytes; the next value starts immediately after; by induction on the number of values there is exactly one parse because every step is determined by the bytes already read.
- **Q5 (what a passing submission shows):** A codec whose round trip is exact on random inputs, a correctly formed SNMP GET checked against a reference parser or a capture, and ARP packets that parse back to the same fields.

</details>

### U2.11 Bridge: coding theory — GF(2), polynomial division, CRC and Hamming codes
**Sources:** none (prerequisite bridge, added so that later units rest on taught ground)
Bridge for: U2.12 (error control); reused in U5.5 (GF(2⁸)) and U5.6 (LFSR as polynomial division).
- **Topics:** The field GF(2); polynomials over GF(2); the division algorithm; irreducible polynomials; linear block codes: generator and parity-check matrices, syndromes, Hamming distance, minimum distance d_min, detecting d−1 and correcting ⌊(d−1)/2⌋ errors; Hamming codes [7,4,3]; CRC as the remainder of polynomial division; error-detection guarantees for CRCs; checksum versus CRC; sphere-packing and Singleton bounds; interleaving for burst errors.
- **Results:** A code with minimum distance d detects d−1 and corrects ⌊(d−1)/2⌋ errors [P]; Hamming(7,4) corrects every single-bit error [P]; an r-bit CRC detects every burst of length ≤ r, every odd number of errors if (x+1) divides the generator, and all double errors for a suitable generator [P]; sphere-packing bound and perfection of Hamming codes [D].
- **Build:** GF(2) polynomial arithmetic; CRC-8, CRC-16 and CRC-32 (checked against `zlib.crc32`); Hamming(7,4) encoder and syndrome decoder; exhaustive measurement of undetected-error rate for a small CRC. [local]
- **Gap-fills:** *[inferred: MacWilliams–Sloane; Lin–Costello, recalled, not checked]* Reed–Solomon over GF(2⁸) (deferred to U10.2 erasure coding), convolutional codes (mention).

**Assignment A2.11** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** A code has minimum distance 7. How many errors can it correct?

(A) 2  
(B) 3  
(C) 6  
(D) 7

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements about cyclic redundancy checks are correct?

(A) A CRC with r check bits detects every burst of length at most r  
(B) If the generator has the factor x plus 1, every odd number of bit errors is detected  
(C) A CRC can correct all single-bit errors in any message length  
(D) The check is computed by polynomial division over GF(2)

**Q3 (2 marks, numerical answer (words)).** The Hamming (7,4) code has 2^4 codewords and each is surrounded by a sphere of radius one containing 1 plus 7 words. What is the total number of words covered?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that the Hamming (7,4) code corrects every single-bit error by showing that the syndrome identifies the position of the error.

**Q5 (3 marks, programming).** Implement CRC-16 and CRC-32 bitwise and with a table, checking against zlib.crc32, and implement Hamming (7,4) encoding and decoding. Test by injecting every single-bit error and every double-bit error.

<details><summary>Key for A2.11 (open only after your attempt)</summary>

- **Q1:** B. It corrects floor((d-1)/2) = 3 errors and detects up to 6.
- **Q2:** A, B, D. CRC detects but does not correct errors in general.
- **Q3:** 128 words (tolerance ±0). 16 times 8 equals 128, which is exactly 2^7, so the code is perfect.
- **Q4 (marking outline):** Take the parity-check matrix whose columns are the binary numbers 1 to 7; a codeword has zero syndrome; a single error at position i adds column i to the syndrome, so the syndrome equals the binary representation of i; flip that bit.
- **Q5 (what a passing submission shows):** CRC-32 equal to zlib on random data, all 7 single-bit errors per word corrected, and a report of what happens for double errors (miscorrection) with counts.

</details>

### U2.12 Data link layer: forwarding, flow control, error control, switching and spanning tree
**Sources:** CN W10
- **Topics:** Data link layer service primitives: framing, addressing, reliable delivery, flow control and error control; error detection and correction (parity, checksums, CRC, Hamming); link-layer flow control (stop-and-wait, sliding window, HDLC); forwarding: Ethernet frames and MAC addresses, self-learning switches, flooding, table ageing; the spanning tree protocol (root election, root and designated ports, BPDUs, RSTP); VLANs and 802.1Q; switch versus router; PPP.
- **Results:** STP elects the bridge with the lowest ID as root and every other bridge keeps its lowest-cost root port, producing a loop-free tree [D]; a learning switch on a tree topology delivers each frame to its destination and never loops [P]; on a topology with a cycle, flooding creates a broadcast storm [D].
- **Build:** a learning switch and an STP implementation on a simulated LAN with loops (storm first, tree after); CRC reuse from U2.11. Then Linux bridges in network namespaces as the professional tool. [local VM]
- **Gap-fills:** *[inferred: Kurose–Ross Ch.6; Perlman, Interconnections, recalled, not checked]* Perlman's STP as a distributed spanning-tree algorithm (compare U9.11), TRILL and shortest-path bridging.

**Assignment A2.12** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** In the spanning tree protocol, which bridge becomes the root?

(A) The one with the highest identifier  
(B) The one with the lowest identifier  
(C) The one with the most ports  
(D) The one chosen at random

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements about learning switches are correct?

(A) They record the source address with the arrival port  
(B) They flood frames for unknown destinations  
(C) On a topology with a cycle, flooding can cause a broadcast storm  
(D) On a tree topology they loop frames forever

**Q3 (2 marks, numerical answer (links)).** A network of 6 switches is connected by 9 links. How many links does the spanning tree protocol block to obtain a loop-free topology?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that on a tree topology a learning switch network delivers each unicast frame to its destination exactly once and never loops.

**Q5 (3 marks, programming).** Simulate learning bridges and spanning tree (BPDU exchange) on random graphs. Verify that the active topology is a spanning tree and that frames are delivered, and show a broadcast storm when spanning tree is disabled.

<details><summary>Key for A2.12 (open only after your attempt)</summary>

- **Q1:** B. The bridge with the lowest bridge identifier wins the root election.
- **Q2:** A, B, C. On a tree no loop is possible, so the last statement is false.
- **Q3:** 4 links (tolerance ±0). A spanning tree uses 5 links, so 9 minus 5 equals 4 links are blocked.
- **Q4 (marking outline):** In a tree there is a unique path between any two switches; flooding sends a frame away from the arrival port, and since the graph has no cycle the frame can never return to a node it has visited; after learning, forwarding follows the unique path; flooding reaches every node exactly once.
- **Q5 (what a passing submission shows):** A simulator that elects a root and blocks the right ports, tests on random graphs for tree structure and delivery, and a storm demonstration with a frame count growing without bound.

</details>

### U2.13 Media access control: channel access protocols and framing
**Sources:** CN W11
- **Topics:** Media access control; channel access protocols: ALOHA and slotted ALOHA, CSMA, CSMA/CD and binary exponential backoff, CSMA/CA, taking turns (polling, token passing), channel partitioning (TDMA, FDMA, CDMA); Ethernet and its minimum frame size; 802.11 DCF, hidden and exposed terminals, RTS/CTS; framing: character count, byte stuffing, bit stuffing and physical-layer coding violations; HDLC and PPP framing.
- **Results:** slotted ALOHA throughput S = G·e^{−G}, maximum 1/e at G = 1 [D]; pure ALOHA S = G·e^{−2G}, maximum 1/(2e) at G = 0.5 [D]; CSMA/CD needs frame time ≥ 2·propagation delay, giving the 64-byte minimum for 10 Mbit/s over 2.5 km [D]; bit stuffing is uniquely decodable [P].
- **Build:** slotted ALOHA, CSMA and binary-exponential-backoff simulators compared with the formulas; a bit-stuffing framer with a round-trip property test. [local]
- **Gap-fills:** *[inferred: Tanenbaum Ch.4; IEEE 802.3 and 802.11 standards, recalled, not checked]* OFDMA and Wi-Fi 6 scheduling, cellular MAC (overview).

**Assignment A2.13** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What is the maximum throughput of slotted ALOHA?

(A) 0.184  
(B) 0.368  
(C) 0.5  
(D) 1.0

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Pure ALOHA has maximum throughput 1/(2e) at G = 0.5  
(B) CSMA/CD requires the frame time to be at least twice the propagation delay  
(C) Bit stuffing keeps a frame uniquely decodable  
(D) Slotted ALOHA has lower maximum throughput than pure ALOHA

**Q3 (2 marks, numerical answer (bytes)).** The slot time of classic Ethernet at 10 Mbit/s is 51.2 microseconds. What is the minimum frame length in bytes needed to detect a collision?

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the throughput of slotted ALOHA as a function of the offered load G, and find its maximum.

**Q5 (3 marks, programming).** Simulate slotted ALOHA, pure ALOHA and CSMA with binary exponential backoff, and plot throughput against offered load with the analytic ALOHA curves.

<details><summary>Key for A2.13 (open only after your attempt)</summary>

- **Q1:** B. S = G e^{-G} is maximal at G = 1 with value 1/e which is about 0.368.
- **Q2:** A, B, C. Slotting doubles the maximum throughput, so the last statement is false.
- **Q3:** 64 bytes (tolerance ±0). 51.2 microseconds at 10 Mbit/s is 512 bits, which is 64 bytes.
- **Q4 (marking outline):** With Poisson offered load G per slot a slot succeeds if exactly one frame is sent, with probability G e^{-G}; differentiate to get e^{-G}(1 - G) = 0 so G = 1; the maximum is e^{-1}.
- **Q5 (what a passing submission shows):** Simulated curves that follow the formulas for ALOHA with peaks near 0.368 and 0.184, and a CSMA curve with a higher peak; seeded runs and confidence bands.

</details>

### U2.14 End-to-end principles of computer networks and the future Internet
**Sources:** CN W12
- **Topics:** End-to-end principles of computer networks: the end-to-end argument (Saltzer, Reed and Clark), fate-sharing, smart edge and simple core, the narrow waist; reliability at the ends versus in the network; Internet design goals and their priority; pressures on the architecture: middleboxes, NAT, firewalls and ossification; requirements for the future Internet and their impact on the architecture (security, mobility, content, programmability), as taken up in D3; next-generation networks, mobile and wireless Internet. Wrap-up of the TCP/IP stack and how each layer's guarantees compose.
- **Results:** End-to-end reliability of a file transfer needs an end-to-end check even if every hop is reliable [D]; hop-by-hop recovery versus end-to-end recovery cost: with n hops and independent per-hop loss p, the expected number of hop transmissions per delivered packet is n/(1−p) with hop-by-hop recovery and (1 − (1−p)ⁿ)/(p(1−p)ⁿ) with end-to-end retransmission [D].
- **Build:** a cost-model script comparing hop-by-hop and end-to-end retransmission over n and p; a design-review decision record placing a function (compression, reliability, security, caching) at the edge or in the network. [local]
- **Gap-fills:** *[inferred: Clark 1988 design philosophy, recalled, not checked]* QUIC and HTTP/3 as end-to-end evolution, 5G core as a cloud-native network (links to U4.4).

**Assignment A2.14** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What is the central claim of the end-to-end argument?

(A) Every router must guarantee reliability  
(B) Correct delivery can only be fully guaranteed by checks at the endpoints  
(C) Reliability should never be built into lower layers  
(D) Encryption belongs in the network core

**Q2 (2 marks, multiple select; all correct options and no wrong option).** A path has n lossy hops with independent loss probability p per hop. Which statements are correct?

(A) End-to-end success probability of one attempt is (1 - p)^n  
(B) With hop-by-hop retransmission each hop needs 1/(1 - p) expected transmissions  
(C) An end-to-end check is still needed after hop-by-hop recovery  
(D) Hop-by-hop recovery alone guarantees data integrity

**Q3 (2 marks, numerical answer).** A path has 10 hops and each drops a packet with probability 0.1 independently. What is the probability that a single end-to-end attempt succeeds?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that the expected number of end-to-end attempts for a packet over n lossy hops is 1/(1-p)^n, and compare the expected number of transmissions with hop-by-hop recovery.

**Q5 (3 marks, programming).** Simulate a chain of n lossy hops with hop-by-hop acknowledgement and with only end-to-end retransmission, and count the transmissions for a range of n and p. Add a hop that occasionally corrupts a byte and show that only an end-to-end checksum catches it.

<details><summary>Key for A2.14 (open only after your attempt)</summary>

- **Q1:** B. Lower-layer reliability may help performance but cannot by itself guarantee end-to-end correctness.
- **Q2:** A, B, C. Hops can corrupt data or fail in memory even if they recover from loss, so the last statement is false.
- **Q3:** 0.3487 (tolerance ±0.001). The success probability is 0.9 to the power 10, which is about 0.349.
- **Q4 (marking outline):** Attempts are geometric with success probability (1-p)^n so the mean is 1/(1-p)^n; hop-by-hop needs 1/(1-p) transmissions per hop, n/(1-p) in total, which is smaller than the end-to-end count of transmissions when n is large or p not tiny.
- **Q5 (what a passing submission shows):** Measured transmission counts agreeing with the formulas, and a demonstration that the end-to-end check detects the corruption that hop-level recovery missed.

</details>

## D3. Advanced networking: high-performance routers, QoS, SDN, NFV, P4, data centers and information-centric networking

Aim: how high-performance networks are designed (algorithms and implementations), and the four contemporary topics of the advanced course: data center networking, information-centric networking and network softwarization (software-defined networking, network virtualization, programmable networks). Prerequisites taken from the source: a networks course (here D2) and Computer Architecture, plus working proficiency with Unix/Linux (U1.2). Benchmarks (recalled, not checked): Varghese, *Network Algorithmics*; McKeown's switching lectures and papers (iSLIP, 1999); Keshav, *An Engineering Approach to Computer Networking*; Kreutz et al., "Software-Defined Networking: A Comprehensive Survey"; Bosshart et al., "P4: Programming Protocol-Independent Packet Processors"; Al-Fares et al. (fat-tree); Zhang et al., "Named Data Networking"; Jacobson et al., "Networking Named Content".

### U3.1 Bridge: lookup data structures — tries, hashing and Bloom filters
**Sources:** none (prerequisite bridge, added so that later units rest on taught ground)
Bridge for: U3.4 (IP lookup), U3.5 (classification), U3.11–U3.12 (NDN tables); reused in U10.4 (Cassandra) and U10.5 (HBase).
- **Topics:** The cost model of lookups (memory accesses, not instructions); binary tries, path-compressed (Patricia) tries and level-compressed tries; hashing, universal hash families, collision handling; perfect hashing (idea); Bloom filters: bit array, k hash functions, false-positive rate, optimal k, counting Bloom filters; content-addressable memory and TCAM as parallel match; Zipf-distributed access and caching.
- **Results:** A binary trie lookup costs at most W memory accesses for W-bit keys [P]; Patricia trie has at most n−1 branching nodes [P]; Bloom filter false-positive rate (1 − e^{−kn/m})^k and optimal k = (m/n)ln 2 giving ≈ 2^{−k} [D]; a universal family gives collision probability ≤ 1/m [P].
- **Build:** binary and Patricia tries; a Bloom filter and counting Bloom filter, with the measured false-positive rate against the formula; a universal hash family. [local]
- **Gap-fills:** *[inferred: Varghese Ch.11; Broder–Mitzenmacher survey on Bloom filters, recalled, not checked]* cuckoo hashing, cuckoo filters.

**Assignment A3.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What kind of error can a Bloom filter make?

(A) False negatives only  
(B) False positives only  
(C) Both false positives and false negatives  
(D) Neither

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) A binary trie lookup on W-bit keys costs at most W memory accesses  
(B) A Patricia trie with n keys has at most n minus 1 branching nodes  
(C) A universal hash family gives collision probability at most 1/m for distinct keys  
(D) A plain Bloom filter supports deletion without error

**Q3 (2 marks, numerical answer).** A Bloom filter has m/n = 10 bits per key and uses k = 7 hash functions. What is the false-positive rate?

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the false-positive rate of a Bloom filter with m bits, n keys and k hash functions under independent uniform hashing, and show that it is minimised at k = (m/n) ln 2.

**Q5 (3 marks, programming).** Implement a binary trie, a Patricia trie and a Bloom filter with a universal hash family, and measure the Bloom false-positive rate against the formula for several values of m/n and k.

<details><summary>Key for A3.1 (open only after your attempt)</summary>

- **Q1:** B. A plain Bloom filter never forgets an inserted key but can report a key that was not inserted.
- **Q2:** A, B, C. Deleting from a plain Bloom filter can remove bits shared with other keys.
- **Q3:** 0.008194 (tolerance ±0.0005). The rate is (1 minus e^{-0.7}) to the 7th power which is about 0.0082.
- **Q4 (marking outline):** A given bit is still zero with probability (1 - 1/m)^{kn} which is about e^{-kn/m}; a false positive needs all k probed bits set, probability (1 - e^{-kn/m})^k; set the derivative of k ln(1 - e^{-kn/m}) to zero to find the symmetric point where half the bits are set, k = (m/n) ln 2.
- **Q5 (what a passing submission shows):** Tries agreeing with a dictionary-based longest-prefix oracle, a Bloom filter whose measured rate follows the formula within sampling error, and a plot of rate against k with the minimum near the predicted value.

</details>

### U3.2 Bridge: bipartite matching, Hall's theorem and Birkhoff–von Neumann decomposition
**Sources:** none (prerequisite bridge, added so that later units rest on taught ground)
Bridge for: U3.3 (switch scheduling) and U3.10 (Clos networks).
- **Topics:** Bipartite graphs, matchings, maximal versus maximum matching; augmenting paths and Berge's theorem; Hall's marriage theorem; König's theorem; regular bipartite multigraphs and edge colouring; doubly stochastic matrices and permutation matrices; the Birkhoff–von Neumann theorem; Hopcroft–Karp (statement) and simple parallel heuristics (PIM, iSLIP).
- **Results:** Hall's condition is necessary and sufficient for a perfect matching [P]; a maximal matching has at least half the size of a maximum matching [P]; every k-regular bipartite multigraph decomposes into k perfect matchings [P]; every doubly stochastic matrix is a convex combination of permutation matrices [P].
- **Build:** augmenting-path maximum matching; Birkhoff decomposition of a random doubly stochastic matrix; checked against `scipy.optimize.linear_sum_assignment` as the oracle. [local]
- **Gap-fills:** *[inferred: Lovász–Plummer; Diestel Ch.2, recalled, not checked]* the max-flow view of matching (formalised in U4.5).

**Assignment A3.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What does Hall's condition require for a bipartite graph to have a matching saturating the left side?

(A) Every left vertex has the same degree  
(B) For every subset S of the left side the neighbourhood has at least as many vertices as S  
(C) The graph is complete  
(D) The graph has no cycles

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) A maximal matching has at least half the size of a maximum matching  
(B) Every k-regular bipartite multigraph decomposes into k perfect matchings  
(C) Every doubly stochastic matrix is a convex combination of permutation matrices  
(D) A greedy maximal matching is always maximum

**Q3 (2 marks, numerical answer (edges)).** A maximum matching of a bipartite graph has 100 edges. What is the smallest possible size of a maximal matching?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that a maximal matching M has at least half the size of a maximum matching M-star.

**Q5 (3 marks, programming).** Implement augmenting-path bipartite matching, check Hall's condition by brute force on small graphs, and implement a Birkhoff-von Neumann decomposition of a doubly stochastic matrix by repeatedly extracting perfect matchings. Verify by recomposing the matrix.

<details><summary>Key for A3.2 (open only after your attempt)</summary>

- **Q1:** B. Hall's condition is that every subset of the left side has a neighbourhood at least as large as itself.
- **Q2:** A, B, C. A maximal matching need not be maximum.
- **Q3:** 50 edges (tolerance ±0). A maximal matching has at least half the edges of a maximum matching, so at least 50.
- **Q4 (marking outline):** Every edge of M* shares an endpoint with some edge of M because M is maximal; each edge of M covers at most two edges of M*; hence the size of M* is at most twice the size of M.
- **Q5 (what a passing submission shows):** Matching agreeing with brute force on small cases, a decomposition whose weighted sum reproduces the matrix to numerical tolerance, and the number of permutation matrices reported.

</details>

### U3.3 High-performance switching and routing: router architecture, switch fabrics and performance
**Sources:** ACN W1, o
- **Topics:** High performance switching and routing: introduction and performance considerations; four contemporary topics and how high-performance networks are designed, covering algorithms and implementations; router architecture (line cards, route processor, forwarding engine, switch fabric); switch fabrics (shared memory, shared bus, crossbar); input queueing, head-of-line blocking, virtual output queues, output queueing, speedup; scheduling as bipartite matching (PIM, iSLIP); throughput limits; IP address lookup as the forwarding bottleneck (continued in U3.4); the practical component with programming assignments and Unix/Linux proficiency. Outline map of the advanced networking course (named topics and where taught): data center networking (U3.10 and U4.6), information centric networking (U3.11 and U3.12) and network softwarization (U3.7 to U3.9), software defined networking (U3.7), a basic programming assumption met in the labs, and the programming assignments that give hands-on practice to the students in each unit's Build.
- **Results:** Input-queued crossbar with FIFO queues saturates at 2 − √2 ≈ 0.586 for large N [S, derivation by the saturated-queue Markov argument]; VOQs with maximum matching reach 100% throughput for admissible i.i.d. traffic [S]; output queueing needs speedup N [D]; iSLIP converges in at most N iterations [D].
- **Build:** a discrete-event input-queued switch comparing FIFO input queueing, VOQ with iSLIP and output queueing; reproduce 0.586. [local]
- **Gap-fills:** *[inferred: Karol–Hluchyj–Morgan 1987; McKeown 1999, recalled, not checked]* buffer sizing (the rule of thumb RTT·C versus RTT·C/√n), multicast switching.

**Assignment A3.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What is the saturation throughput of an input-queued crossbar switch with FIFO queues under uniform traffic for large N?

(A) 1.0  
(B) 0.586  
(C) 0.368  
(D) 0.5

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements about switch architectures are correct?

(A) Virtual output queues remove head-of-line blocking  
(B) An output-queued switch needs a speedup of N in the worst case  
(C) iSLIP converges within N iterations  
(D) FIFO input queueing has no head-of-line blocking

**Q3 (2 marks, numerical answer).** What is the limiting saturation throughput of a FIFO input-queued switch for large N, given by 2 minus the square root of 2?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that an output-queued switch with N inputs needs an internal speedup of N to avoid loss in the worst case.

**Q5 (3 marks, programming).** Simulate an input-queued switch with FIFO queues and with virtual output queues and an iSLIP matching under uniform Bernoulli traffic. Measure the saturation throughput and mean delay.

<details><summary>Key for A3.3 (open only after your attempt)</summary>

- **Q1:** B. Head-of-line blocking limits throughput to 2 minus root 2, about 0.586.
- **Q2:** A, B, C. FIFO input queues suffer head-of-line blocking.
- **Q3:** 0.5858 (tolerance ±0.001). The value is 0.5858.
- **Q4 (marking outline):** In one slot all N inputs may have a packet for the same output; the output queue must accept all N packets in that slot; each slot lasts one packet time so the switch fabric must run N times faster than a line.
- **Q5 (what a passing submission shows):** FIFO throughput saturating near 0.586 for a large switch, VOQ with iSLIP reaching near 1 with more delay at high load, and curves of delay against load.

</details>

### U3.4 IP address lookup: algorithms, optimisation and hardware implementation
**Sources:** ACN W1–2
- **Topics:** IP address lookup; algorithms for IP address lookup and optimisation: binary trie, path compression, multibit tries with controlled prefix expansion, Lulea compression, DIR-24-8 style direct tables, binary search on prefix lengths, hash-based lookup with Bloom filters; hardware implementation of address lookup: TCAM, pipelined SRAM, memory-access budget at line rate; update cost and route-flap handling; IPv6 lookup challenges.
- **Results:** Multibit trie with stride k: lookup W/k accesses, memory trade-off [D]; controlled prefix expansion cost bound [D]; binary search on lengths needs O(log W) hash probes with markers [P]; TCAM entry ordering by prefix length implements longest-prefix match [P].
- **Build:** binary trie, multibit trie, DIR-24-8-like table and binary search on lengths on a synthetic routing table; memory and access counts compared; checked against a naive scan. [local]
- **Gap-fills:** *[inferred: Varghese Ch.11; Degermark et al. 1997, recalled, not checked]* the size of today's global routing table must be checked from a current source (for example RIPE or CIDR Report).

**Assignment A3.4** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** A multibit trie uses a stride of 4 bits on 32-bit addresses. What is the worst-case number of memory accesses per lookup?

(A) 4  
(B) 8  
(C) 16  
(D) 32

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements about IP lookup are correct?

(A) Ordering TCAM entries by decreasing prefix length gives longest-prefix match  
(B) Binary search on prefix lengths with markers needs O(log W) hash probes  
(C) Controlled prefix expansion can increase the number of stored entries  
(D) A Patricia trie always needs more than W accesses

**Q3 (2 marks, numerical answer (accesses)).** A multibit trie with stride k = 4 is used for IPv4 addresses of W = 32 bits. How many memory accesses does a lookup need in the worst case?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that a TCAM that stores prefixes in order of decreasing length and returns the first match implements longest-prefix matching.

**Q5 (3 marks, programming).** Implement a binary trie, a multibit trie with controlled prefix expansion and binary search on prefix lengths with markers, and compare them with a brute-force longest-prefix match on random tables of at least 10,000 prefixes.

<details><summary>Key for A3.4 (open only after your attempt)</summary>

- **Q1:** B. The worst case is W divided by k, which is 32/4 = 8.
- **Q2:** A, B, C. A Patricia trie never needs more than W bit tests.
- **Q3:** 8 accesses (tolerance ±0). Each level consumes 4 bits, giving 8 levels.
- **Q4 (marking outline):** If an address matches several stored prefixes the matching ones are nested, so a longer one appears earlier in the order; the first match is therefore the longest matching prefix; if only one matches it is returned as well.
- **Q5 (what a passing submission shows):** All structures agreeing with brute force on random addresses, and measured memory and lookup counts compared with the formulas.

</details>

### U3.5 Packet classification
**Sources:** ACN W3
- **Topics:** Packet classification: need for packet classification (firewalls, QoS, routing policy) and methods for packet classification; the d-dimensional matching problem; lower bounds; linear search; hierarchical tries and set-pruning tries; grid of tries; cross-producting; recursive flow classification; decision-tree methods (HiCuts, HyperCuts); TCAM-based classification and range expansion; tuple-space search.
- **Results:** For N rules in d dimensions, either O(log^{d−1} N) time with O(N) space or O(log N) time with O(N^d) space [S, lower-bound statement, recalled, not checked]; set-pruning tries trade memory O(N^d·W) for single-path lookup [D]; range-to-prefix expansion needs up to 2W−2 prefixes per range [P].
- **Build:** hierarchical tries, cross-producting and a HiCuts-style decision tree on a synthetic ruleset; memory and lookup depth measured. [local]
- **Gap-fills:** *[inferred: Gupta–McKeown 2001, recalled, not checked]* ruleset structure (overlap, specificity), P4 match-action tables as classification (U3.9).

**Assignment A3.5** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** In the worst case, into how many prefixes can an arbitrary range on W-bit values be expanded?

(A) W  
(B) 2W - 2  
(C) 2^W  
(D) W/2

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements about packet classification are correct?

(A) Set-pruning tries avoid backtracking at the cost of memory  
(B) Hierarchical tries may need backtracking  
(C) A TCAM stores ranges directly without any expansion  
(D) For N rules in d dimensions there is a trade-off between time and space

**Q3 (2 marks, numerical answer (prefixes)).** What is the maximum number of prefixes needed to represent one range of 16-bit port numbers?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that any interval of W-bit integers can be written as the union of at most 2W minus 2 prefixes.

**Q5 (3 marks, programming).** Implement linear search, a hierarchical trie and a set-pruning trie for two-field rules, check them against each other on random rule sets, and measure memory and lookup time.

<details><summary>Key for A3.5 (open only after your attempt)</summary>

- **Q1:** B. A range on W bits needs at most 2W minus 2 prefixes.
- **Q2:** A, B, D. TCAMs store prefixes or ternary patterns, so ranges must be expanded.
- **Q3:** 30 prefixes (tolerance ±0). The worst case is 2W minus 2 = 30.
- **Q4 (marking outline):** Split the interval at the highest bit where the endpoints differ into a left part and a right part; each part is a suffix-closed or prefix-closed interval needing at most one prefix per bit position below the split; the two parts need at most W minus 1 prefixes each.
- **Q5 (what a passing submission shows):** Three classifiers returning the same highest-priority rule on random packets, and a table showing the memory and time trade-off.

</details>

### U3.6 DiffServ, quality of service, traffic policing and shaping
**Sources:** ACN W4
- **Topics:** Differentiated Service, Quality of Service, traffic policing (the source writes "Traffic Polishing") and traffic shaping; QoS requirements by application; IntServ and RSVP versus DiffServ; DSCP and per-hop behaviours (EF, AF); classifier, marker, meter, shaper, dropper; token bucket and leaky bucket; schedulers: FIFO, strict priority, round robin, weighted fair queueing, deficit round robin; active queue management (RED).
- **Results:** Token bucket (σ, ρ) bounds traffic in any interval t by σ + ρt [P]; max–min fairness has a unique water-filling solution [P]; GPS/WFQ guarantees a flow with weight share g a delay bound near σ/g plus a packet time [S]; DRR gives long-run fairness in O(1) per packet [D].
- **Build:** token bucket, WFQ with virtual finish times and DRR; check the delay bound on adversarial arrivals. [local]
- **Gap-fills:** *[inferred: Parekh–Gallager 1993; RFC 2475, recalled, not checked]* network neutrality and QoS (mention), data-center QoS (U3.10).

**Assignment A3.6** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** A token bucket with depth sigma and rate rho bounds the traffic sent in any interval of length t by which quantity?

(A) rho t  
(B) sigma + rho t  
(C) sigma rho t  
(D) sigma - rho t

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Max-min fair allocation is unique and given by water-filling  
(B) Weighted fair queueing gives a delay bound close to sigma divided by the flow's guaranteed rate plus a packet time  
(C) Deficit round robin does O(1) work per packet  
(D) A token bucket allows unlimited bursts

**Q3 (2 marks, numerical answer (bytes)).** A token bucket has depth 3000 bytes and rate 1000 bytes per second. What is the maximum number of bytes that can be sent in a 2 second interval?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that traffic conforming to a token bucket with depth sigma and rate rho sends at most sigma + rho t bytes in any interval of length t.

**Q5 (3 marks, programming).** Implement a token bucket policer and shaper, a deficit round robin scheduler and weighted fair queueing, and verify the token bucket bound and the long-run shares on simulated traffic.

<details><summary>Key for A3.6 (open only after your attempt)</summary>

- **Q1:** B. The bucket can supply its depth immediately and then refills at rate rho.
- **Q2:** A, B, C. The bucket depth limits the burst.
- **Q3:** 5000 bytes (tolerance ±0). The bound is sigma plus rho t = 3000 + 2000 = 5000.
- **Q4 (marking outline):** At the start of the interval the bucket holds at most sigma tokens; during the interval at most rho t further tokens arrive; each byte sent consumes one token; so at most sigma + rho t bytes can be sent.
- **Q5 (what a passing submission shows):** Code with tests showing that conforming traffic is never dropped, the bound holds on a randomised trace, and DRR shares converge to the weights.

</details>

### U3.7 Network softwarization: software-defined networking, controllers, southbound and northbound interfaces
**Sources:** ACN W5–6
- **Topics:** Network softwarization, introduction; software defined networking (SDN) deep dive: control plane and data plane separation, OpenFlow match–action tables and flow entries, southbound interface (OpenFlow, NETCONF, P4Runtime), northbound interface (REST APIs, intents), controllers (ONOS, OpenDaylight, Ryu), reactive versus proactive flow installation, consistent updates; working with Mininet; lab exercises with Mininet.
- **Results:** Per-packet consistent updates avoid transient loops and blackholes via two-phase update [S]; controller placement as a k-median problem [D]; reactive setup latency model [D].
- **Build:** a minimal OpenFlow-like switch with a flow table and a learning-switch controller from scratch; then Mininet with Ryu or ONOS. [local VM]
- **Gap-fills:** *[inferred: Kreutz et al. 2015; McKeown et al. 2008, recalled, not checked]* verification (VeriFlow, Header Space Analysis).

**Assignment A3.7** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** In SDN terminology, which interface connects the controller to the switches?

(A) Northbound interface  
(B) Southbound interface  
(C) East-west interface only  
(D) Management plane only

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Two-phase update gives per-packet consistency during a policy change  
(B) Controller placement can be modelled as a k-median problem  
(C) The northbound interface connects switches to the controller  
(D) In reactive mode the first packet of a flow incurs extra latency

**Q3 (2 marks, numerical answer (ms)).** In reactive flow set-up the first packet travels 5 ms to the controller, waits 2 ms for processing and returns a rule in 5 ms. How long is the extra delay for the first packet in ms?

**Q4 (2 marks, prove or derive; every step with its reason).** Explain the two-phase update protocol and show that no packet sees a mixture of old and new rules.

**Q5 (3 marks, programming).** Simulate a network of flow-table switches with a controller in reactive and proactive modes, and implement a two-phase update. Check for loops and black holes during the transition with and without the two-phase protocol.

<details><summary>Key for A3.7 (open only after your attempt)</summary>

- **Q1:** B. Southbound interfaces such as OpenFlow connect the controller to the data plane.
- **Q2:** A, B, D. The northbound interface connects applications to the controller.
- **Q3:** 12 ms (tolerance ±0). The delay is the sum of the legs, 12 ms.
- **Q4 (marking outline):** Install the new rules in the interior switches tagged with a new version; only then flip the ingress to stamp the new version; packets carry one version and are matched by rules of that version only; after in-flight old packets drain remove the old rules.
- **Q5 (what a passing submission shows):** A simulator showing higher first-packet latency in reactive mode, an update that produces transient loops or drops when done naively and none when two-phase, and a checker that traces packets.

</details>

### U3.8 Network function virtualization: architecture and concepts
**Sources:** ACN W7
- **Topics:** Network Function Virtualization (NFV): architecture and concepts; VNFs, NFV infrastructure, management and orchestration (ETSI NFV MANO); service function chaining; VNF placement and scaling; NFV and SDN together; virtual switches and fast packet I/O; middlebox examples (firewall, NAT, load balancer, DPI).
- **Results:** VNF placement with capacity constraints is a bin-packing variant, NP-hard, with first-fit-decreasing within 11/9·OPT + 6/9 [S]; chain latency is the sum of per-VNF service and queueing delays [D].
- **Build:** a service-chain simulator with M/M/1 stages and a greedy VNF placement heuristic; compare simulated latency with the formula. [local]
- **Gap-fills:** *[inferred: ETSI GS NFV 002, recalled, not checked]* cloud-native network functions (5G core).

**Assignment A3.8** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Placing VNFs with capacity limits onto servers is a variant of which classic problem?

(A) Shortest path  
(B) Bin packing  
(C) Minimum spanning tree  
(D) Maximum flow

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) First-fit decreasing uses at most 11/9 of the optimal number of bins plus 6/9  
(B) The latency of a service chain is the sum of the per-function delays  
(C) NFV replaces dedicated appliances with software on commodity hardware  
(D) The order of functions in a chain never affects the result

**Q3 (2 marks, numerical answer (ms)).** A service chain has three virtual functions whose service plus queueing delays are 1.2 ms, 0.8 ms and 2.0 ms. What is the chain latency?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that virtual network function placement with capacity constraints is NP-hard by reduction from bin packing.

**Q5 (3 marks, programming).** Implement first-fit, first-fit decreasing and best-fit placement and compare them with an exact solver on small random instances, and simulate the end-to-end latency of a chain with queueing at each function.

<details><summary>Key for A3.8 (open only after your attempt)</summary>

- **Q1:** B. Packing functions with resource demands into servers with capacity is bin packing.
- **Q2:** A, B, C. Order often matters, for example a firewall before or after NAT.
- **Q3:** 4 ms (tolerance ±0.001). Delays add along a chain, giving 4.0 ms.
- **Q4 (marking outline):** Given bin packing items with sizes and bins with capacity, create one function per item with that demand and one server per bin with that capacity; a feasible placement of all functions exists iff the items can be packed into the bins; so the placement problem is at least as hard as bin packing.
- **Q5 (what a passing submission shows):** Heuristics compared with the optimum on at least 200 instances with the worst ratio reported, and a chain simulation whose mean latency matches the sum of the per-stage delays.

</details>

### U3.9 Programmable networks: P4, SmartNICs and P4 switches
**Sources:** ACN W8
- **Topics:** Programmable Networks: introduction to P4, SmartNICs and P4 switches; the protocol-independent switch architecture (parser, match–action pipeline, deparser); P4 language elements (headers, parsers, tables, actions, controls); the v1model and BMv2; P4Runtime; in-band network telemetry; SmartNIC offload; lab exercise with Mininet and BMv2 switches.
- **Results:** A PISA pipeline executes a bounded number of table lookups per packet, so its latency is fixed [Def]; parser state machine terminates as a DAG without loops [Def].
- **Build:** a Python PISA emulator (parser, tables, actions, deparser) running a small router and a firewall program; then the same program on BMv2 with Mininet. [local VM]
- **Gap-fills:** *[inferred: Bosshart et al. 2014, recalled, not checked]* P4 compiler targets and the current P4_16 specification.

**Assignment A3.9** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Why is the latency of a PISA switch pipeline fixed?

(A) It uses a global lock  
(B) The pipeline executes a bounded number of match-action stages per packet  
(C) Packets are cached  
(D) It has no memory

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) A P4 parser is a state machine with no loops over packet bytes in its basic form  
(B) Match-action tables are the main processing construct  
(C) A P4 program can loop an unbounded number of times per packet  
(D) SmartNICs can offload packet processing from the host

**Q3 (2 marks, numerical answer (ns)).** A pipeline has 12 stages and each stage takes 1 ns. What is the pipeline latency in ns?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that a parser whose state graph is a directed acyclic graph and whose every transition consumes at least one bit terminates on any packet.

**Q5 (3 marks, programming).** Write a simulator of a match-action pipeline with a parser state machine described in JSON and tables for Ethernet and IPv4 forwarding, and test it on generated packets.

<details><summary>Key for A3.9 (open only after your attempt)</summary>

- **Q1:** B. A fixed number of stages gives a bounded, constant processing time per packet.
- **Q2:** A, B, D. The pipeline has no unbounded loops.
- **Q3:** 12 ns (tolerance ±0). With a fixed number of stages the latency is 12 ns.
- **Q4 (marking outline):** Every path through the graph has bounded length; each transition consumes input so the position strictly increases; the parser reaches an accept or reject state after at most the number of states steps.
- **Q5 (what a passing submission shows):** A simulator that parses packets and forwards them by tables, tests with malformed packets handled by a reject state, and a check that the number of table lookups per packet is bounded.

</details>

### U3.10 Data center networking: topologies, routing, transport and container network interfaces
**Sources:** ACN W9–10
- **Topics:** Data Center Networking (DCN) introduction; deep dive: network topologies (three-tier, fat-tree, Clos and leaf–spine, BCube, DCell, Jellyfish), oversubscription and bisection bandwidth, ECMP and load balancing, incast and DCTCP, RDMA over converged Ethernet (overview); container network interfaces: the CNI model, Kubernetes pod networking, overlay networks (VXLAN), network policy.
- **Results:** A fat-tree built of k-port switches supports k³/4 hosts with full bisection bandwidth [D]; a Clos network with m ≥ 2n−1 middle switches is strictly non-blocking and m ≥ n is rearrangeably non-blocking [P, via Hall in U3.2]; ECMP hash collisions leave flows on shared links [D].
- **Build:** a fat-tree generator with ECMP path counting and bisection computation; a flow-level simulator showing hash collision loss; a toy CNI plug-in that wires two network namespaces. [local VM]
- **Gap-fills:** *[inferred: Al-Fares et al. 2008; Alizadeh et al. 2010 (DCTCP), recalled, not checked]* container networking continues in U4.4.

**Assignment A3.10** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** How many hosts does a fat-tree built from k-port switches support?

(A) k^2  
(B) k^3/4  
(C) 2^k  
(D) k log k

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) A Clos network with m at least 2n - 1 middle switches is strictly non-blocking  
(B) With m at least n it is rearrangeably non-blocking  
(C) A fat-tree offers full bisection bandwidth  
(D) ECMP guarantees that no two flows share a link

**Q3 (2 marks, numerical answer (hosts)).** How many hosts does a fat-tree of 48-port switches support?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that a three-stage Clos network with m at least n middle switches is rearrangeably non-blocking, using Hall's theorem.

**Q5 (3 marks, programming).** Build a fat-tree topology, route random permutation traffic with ECMP hashing and with an ideal splitter, and measure the maximum link load and flow completion times.

<details><summary>Key for A3.10 (open only after your attempt)</summary>

- **Q1:** B. A k-ary fat-tree supports k^3/4 hosts with full bisection bandwidth.
- **Q2:** A, B, C. ECMP hashing can still collide flows onto the same link.
- **Q3:** 27648 hosts (tolerance ±0). The count is k^3/4 = 110592/4 = 27648.
- **Q4 (marking outline):** View input switches and output switches as two sides of a bipartite multigraph with one edge per call; every vertex has degree at most n; the graph decomposes into n matchings by Hall; assign each matching to a distinct middle switch; so m at least n suffices.
- **Q5 (what a passing submission shows):** A generator for the topology, ECMP showing visible collisions and higher maximum load than the ideal, and plots across several random seeds.

</details>

### U3.11 Content distribution on the Internet and architectures for information-centric networking
**Sources:** ACN W11
- **Topics:** Content distribution on the Internet: CDNs, DNS redirection and anycast, web caching, peer-to-peer distribution; architectures for information-centric networking (ICN): CCN and NDN, DONA, PURSUIT, NetInf; name-based forwarding, Interest and Data packets, Pending Interest Table, FIB and Content Store; forwarding strategies; Zipf popularity and cache hit ratio.
- **Results:** LRU hit probability under the independent reference model by Che's approximation 1 − e^{−λ_i T_C} with T_C solving Σ(1 − e^{−λ_i T_C}) = C [D]; PIT aggregation removes duplicate upstream requests [D].
- **Build:** an NDN forwarder (PIT, FIB, CS) in Python with caching; measure hit ratio under Zipf and compare with Che. [local]
- **Gap-fills:** *[inferred: Jacobson et al. 2009; Che–Tung–Wang 2002, recalled, not checked]* CDN request routing as consistent hashing (U9.5).

**Assignment A3.11** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Under Che's approximation for an LRU cache, what is the hit probability of item i with request rate lambda_i and characteristic time T?

(A) e^(-lambda_i T)  
(B) 1 - e^(-lambda_i T)  
(C) lambda_i T  
(D) 1/T

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) CDNs often direct clients to a nearby server by DNS redirection  
(B) In information-centric networking a request names the content and not the host  
(C) Pending-interest aggregation prevents duplicate upstream requests  
(D) Caching at every router always improves performance

**Q3 (2 marks, numerical answer).** Two items have equal request rate 1 per second and an LRU cache holds one item on average. The characteristic time solves 2 times (1 - e^{-T}) = 1. What is the hit probability of each item?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that pending-interest aggregation reduces the upstream requests for k identical requests arriving within one round-trip time from k to one.

**Q5 (3 marks, programming).** Simulate an LRU cache under a Zipf request distribution and compare the measured hit ratio with Che's approximation, and implement a pending-interest table with aggregation, showing the saving in upstream requests.

<details><summary>Key for A3.11 (open only after your attempt)</summary>

- **Q1:** B. The item is in the cache if it was requested within the characteristic time, which has probability 1 minus e^{-lambda T}.
- **Q2:** A, B, C. Redundant caches can waste capacity, so the last statement is false.
- **Q3:** 0.5 (tolerance ±0.001). T equals ln 2, so the hit probability is 1 minus 1/2 = 0.5.
- **Q4 (marking outline):** The first request creates a table entry for the name with the arrival interface; later requests for the same name find the entry and only add their interface; one request goes upstream; when the data returns it is sent on all recorded interfaces.
- **Q5 (what a passing submission shows):** Hit ratio curves against cache size agreeing with the approximation within a few percent, and a count of upstream requests with and without aggregation.

</details>

### U3.12 NDN content naming, routing, caching and security
**Sources:** ACN W12
- **Topics:** Content naming, routing and caching, security in Named Data Networking: hierarchical names, name aggregation and FIB size; name-based routing (link-state, NLSR); caching policies (LRU, LFU, leave-copy-everywhere, leave-copy-down, probabilistic); security: signed data, producer authentication, trust schemas, content poisoning, interest flooding, cache-privacy attacks.
- **Results:** Data-centric security: a signature binds name to content so integrity holds wherever the data was cached [Def]; probabilistic caching reduces redundancy at the cost of hit ratio [D].
- **Build:** caching-policy comparison on a tree topology; a signed-data verifier with a toy trust schema; an interest-flooding scenario with rate limiting. [local]
- **Gap-fills:** *[inferred: NDN project reports, recalled, not checked]* NDN in IoT and vehicular settings.

**Assignment A3.12** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** In named-data networking, what provides security for content independent of where it is cached?

(A) The channel encryption of each link  
(B) A signature that binds the name to the content  
(C) The router's firewall  
(D) The routing protocol

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) NDN names are hierarchical  
(B) Forwarding uses longest-prefix matching on name components  
(C) Security requires trusting every cache that held the data  
(D) Content can be verified by a signature regardless of the path

**Q3 (2 marks, numerical answer).** Each of 5 routers on a path caches a passing object independently with probability 0.3. What is the probability that at least one router caches it?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that data-centric security gives integrity wherever the data was cached, assuming an unforgeable signature scheme.

**Q5 (3 marks, programming).** Implement hierarchical names with longest-prefix forwarding, a pending-interest table and a content store with signature verification using your own signature from the cryptography units or a library, and show that tampered cached data is rejected.

<details><summary>Key for A3.12 (open only after your attempt)</summary>

- **Q1:** B. The producer signs name and content together so any cache can serve it and consumers can verify it.
- **Q2:** A, B, D. Verification of the signature removes the need to trust caches.
- **Q3:** 0.8319 (tolerance ±0.001). The probability is one minus 0.7 to the power 5 which is about 0.832.
- **Q4 (marking outline):** A consumer verifies the signature over name and content with the producer's public key; a cache cannot alter the content without invalidating the signature unless it can forge; therefore any content that verifies is the producer's content for that name.
- **Q5 (what a passing submission shows):** A forwarder passing Interests and Data, a content store that serves hits, and a test in which a modified cached object fails verification and is not delivered.

</details>

## D4. Cloud compute: virtualization, containers, cloud networks and Google Cloud compute services

Aim: how a cloud turns physical servers and networks into elastic virtual resources, derived from first principles (privilege levels, memory mapping, migration dynamics, flows), then the Google Cloud services that deliver them. Benchmarks (recalled, not checked): Popek and Goldberg (1974); Smith and Nair, *Virtual Machines*; Barham et al. (Xen, 2003); Wood et al., Sandpiper (NSDI 2007); Clark et al., live migration (NSDI 2005); Greenberg et al., VL2 (2009); Koponen et al., NVP (2014); Jain et al., B4 (2013); Hong et al., SWAN (2013); Burns et al., "Borg, Omega and Kubernetes"; Misra and Patel, *Cloud and Distributed Computing: Algorithms and Systems* (table of contents checked this session; see Appendix D).

### U4.1 Bridge: operating systems and computer architecture for virtualization
**Sources:** none (prerequisite bridge, added so that later units rest on taught ground)
Bridge for: U4.2 (virtualization), U4.4 (containers), U9.x (process and thread models).
- **Topics:** Privilege levels and protection rings; system calls, traps, interrupts and exceptions; the instruction set as a contract; processes, threads and scheduling (round robin, priority, fair-share, completely fair scheduler weights); virtual memory: paging, page tables, multi-level page tables, TLB, page faults and replacement; I/O devices, DMA and interrupts; file systems and block devices (overview); inter-process communication and synchronization basics.
- **Results:** Address translation with a k-level table costs k extra memory references on a TLB miss and the effective access time is hit·t + (1−hit)·(t + k·t) [D]; a context switch must change the page-table base and flush or tag the TLB [Def]; priority inversion arises with locks and priorities [D].
- **Build:** a toy CPU with user and kernel modes, traps and a page-table MMU with TLB; measure effective access time against the formula. [local]
- **Gap-fills:** *[inferred: Tanenbaum, Modern Operating Systems; Hennessy–Patterson; Silberschatz, recalled, not checked]* cgroups and namespaces (U4.4 builds on them).

**Assignment A4.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What must a context switch between processes change so that the new process sees its own address space?

(A) The page-table base register  
(B) The disk controller  
(C) The network address  
(D) The instruction set

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) A TLB miss in a k-level page table costs k extra memory references  
(B) A TLB can be tagged with address-space identifiers to avoid flushing  
(C) Priority inversion can occur when a low-priority task holds a lock needed by a high-priority task  
(D) Virtual memory removes the need for page tables

**Q3 (2 marks, numerical answer (ns)).** A memory access takes 100 ns. A four-level page table is walked on a TLB miss, costing four extra references. The TLB hit ratio is 0.98. What is the effective access time in ns?

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the effective memory access time with TLB hit ratio h, memory access time t and a k-level page-table walk on a miss.

**Q5 (3 marks, programming).** Simulate a TLB with LRU replacement and a multi-level page-table walk over a synthetic address trace, and plot the effective access time against hit ratio, comparing with the formula.

<details><summary>Key for A4.1 (open only after your attempt)</summary>

- **Q1:** A. The page-table base is reloaded and the TLB is flushed or tagged.
- **Q2:** A, B, C. Page tables are how virtual memory is implemented.
- **Q3:** 108 ns (tolerance ±0.5). 0.98 times 100 plus 0.02 times 500 gives 98 plus 10 equals 108 ns.
- **Q4 (marking outline):** A hit costs t; a miss costs the k table references plus the data access, which is t + k t; weight by probability: h t + (1 - h)(t + k t).
- **Q5 (what a passing submission shows):** A simulator reporting measured hit ratio and references, an effective access time curve that matches the derived formula, and an experiment showing the effect of locality.

</details>

### U4.2 Virtualization: models, types and the Popek–Goldberg theorem
**Sources:** CCDS W1
- **Topics:** Virtualization (lecture 2): what's virtualization, benefits of virtualization, virtualization models: bare metal and hosted hypervisor; types of virtualization: processor virtualization, memory virtualization, full virtualization, para virtualization (paravirtualization), device virtualization; trap-and-emulate, binary translation, hardware-assisted virtualization (VT-x, AMD-V), shadow page tables and nested paging (EPT/NPT), memory ballooning and page sharing, I/O virtualization (emulation, virtio, passthrough).
- **Results:** Popek–Goldberg: a VMM can be built for a machine if every sensitive instruction is privileged [P]; trap-and-emulate preserves equivalence, resource control and efficiency [D]; shadow paging costs a trap per guest page-table update while nested paging makes a TLB miss cost up to (n+1)(m+1)−1 references for n-level guest and m-level host tables [D].
- **Build:** a toy ISA with privileged instructions and a trap-and-emulate hypervisor that runs a guest kernel and user program; a shadow page-table and nested-walk cost counter. [local]
- **Gap-fills:** *[inferred: Popek–Goldberg 1974; Barham et al. 2003; Smith–Nair, recalled, not checked]* Firecracker-style microVMs, gVisor-style sandboxes, confidential computing (overview).

**Assignment A4.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** According to the Popek-Goldberg theorem, a virtual machine monitor can be built for a machine if which condition holds?

(A) Every instruction is privileged  
(B) The set of sensitive instructions is a subset of the privileged instructions  
(C) There are no privileged instructions  
(D) The machine has paging

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Trap-and-emulate preserves equivalence, resource control and efficiency under the theorem's condition  
(B) Shadow paging traps on guest page-table updates  
(C) Nested paging removes the need for shadow page tables  
(D) Full virtualization always requires modifying the guest operating system

**Q3 (2 marks, numerical answer (references)).** With nested paging, a TLB miss costs up to (n+1)(m+1)-1 references for an n-level guest and an m-level host page table. What is the worst case for n = 4 and m = 4?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove the sufficiency direction of the Popek-Goldberg theorem: if all sensitive instructions are privileged, a monitor exists that is equivalent, controls resources and runs most instructions natively.

**Q5 (3 marks, programming).** Write a toy instruction set with user and supervisor modes and a trap-and-emulate monitor. Run a guest program on it, then add a sensitive but unprivileged instruction and show that the guest behaves differently under the monitor.

<details><summary>Key for A4.2 (open only after your attempt)</summary>

- **Q1:** B. If every sensitive instruction traps in user mode, trap-and-emulate works.
- **Q2:** A, B, C. Paravirtualization modifies the guest; full virtualization does not.
- **Q3:** 24 references (tolerance ±0). The formula gives 5 times 5 minus 1 equals 24.
- **Q4 (marking outline):** Run the guest in user mode; innocuous instructions execute directly; privileged instructions trap to the monitor which emulates them on virtual state; since all sensitive instructions are privileged they all trap, so the guest sees the same behaviour as on bare metal and cannot touch real resources.
- **Q5 (what a passing submission shows):** A monitor passing equivalence tests on a set of guest programs, and a failing test after adding the unprivileged sensitive instruction that explains why binary translation or hardware support is needed.

</details>

### U4.3 Hotspot mitigation and live VM migration
**Sources:** CCDS W1
- **Topics:** Hotspot mitigation for virtual machine migration: enterprise data centers, data center workloads, provisioning methods, the Sandpiper (the source writes "Sandipiper") architecture, resource provisioning, black-box approach, gray-box approach, live VM migration stages (push, stop-and-copy, pull, pre-copy, post-copy), hotspot mitigation: detection by k out of n samples over threshold, volume and volume-to-size ratio, swap versus migrate.
- **Results:** Pre-copy with dirty rate d and bandwidth B (ρ = d/B < 1) transfers V·ρ^i in round i, so total time V/(B(1−ρ)) and downtime V·ρⁿ/B after n rounds [D]; migration cannot converge when ρ ≥ 1, forcing stop-and-copy or throttling [D]; volume = 1/((1−cpu)(1−net)(1−mem)) ranks load nonlinearly [Def].
- **Build:** a pre-copy migration simulator measuring downtime versus dirty rate; a Sandpiper-style detector and migration planner on synthetic utilisation traces. [local]
- **Gap-fills:** *[inferred: Clark et al. 2005; Wood et al. 2007, recalled, not checked]* post-copy, auto-converge and compression in production hypervisors; GCP live migration (U4.7).

**Assignment A4.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** When does pre-copy live migration converge, with dirty rate d and bandwidth B?

(A) When d is greater than B  
(B) When d is less than B  
(C) Only when d equals zero  
(D) Never

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements about live migration are correct?

(A) Round i of pre-copy transfers V times rho to the i  
(B) The total time is V divided by B times (1 - rho) in the limit  
(C) If rho is at least one, pre-copy cannot converge by itself  
(D) Post-copy transfers state before the virtual machine resumes

**Q3 (2 marks, numerical answer (s)).** A virtual machine has V = 8000 MB of memory, the link bandwidth is B = 1000 MB/s and the dirty rate is d = 250 MB/s. What is the total migration time in seconds, in the limit of many rounds?

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the pre-copy rounds as a geometric series, giving total time and downtime after n rounds.

**Q5 (3 marks, programming).** Simulate pre-copy migration with a page dirtying process and measure total time and downtime for several dirty rates, against the formulas. Show the behaviour when the dirty rate exceeds the bandwidth.

<details><summary>Key for A4.3 (open only after your attempt)</summary>

- **Q1:** B. Each round transfers a fraction rho = d/B of the previous round, which shrinks only if rho is below one.
- **Q2:** A, B, C. Post-copy resumes the machine first and fetches pages on demand.
- **Q3:** 10.67 s (tolerance ±0.05). With rho = 0.25 the total is V/(B(1 - rho)) = 8000/750 which is about 10.67 s.
- **Q4 (marking outline):** Round 0 sends V taking V/B; during it V rho dirty pages appear so round 1 sends V rho; round i sends V rho^i; sum of the series is V/(1 - rho); divide by B for time; the stop-and-copy after n rounds sends V rho^n taking V rho^n/B downtime.
- **Q5 (what a passing submission shows):** Measured time and downtime following the geometric-series formulas, a non-convergence case that forces stop-and-copy, and a plot of downtime against dirty rate.

</details>

### U4.4 Containers, Docker, Linux containers, networking of VMs, Kubernetes and edge computing
**Sources:** CCDS W2; ACN W10
- **Topics:** Server virtualization: methods of virtualization using Docker and using Linux containers (namespaces, cgroups, union file systems, images and layers, registries); approaches for networking of VMs: hardware approach (single-root I/O virtualization, SR-IOV) and software approach (Open vSwitch); Mininet and its applications; container network interfaces; microservices; Kubernetes (pods, services, controllers, scheduler, declarative reconciliation); introduction to edge computing and its classification.
- **Results:** A reconcile loop (observe, diff, act) converges when actions are idempotent and monotone toward the desired state [D]; CFS gives each runnable task CPU share weight_i/Σweight [Def]; a container shares the host kernel so its isolation is weaker than a VM's [Def].
- **Build:** a container-lite using `unshare`, a private root and cgroup v2 limits inside a disposable VM; a Kubernetes-style controller (desired versus actual replicas) and a filter-and-score scheduler in Python. [local VM]
- **Gap-fills:** *[inferred: Misra–Patel Ch.9; Burns et al. 2016, recalled, not checked]* hand-built isolation is never trusted with untrusted input (Master Rules 11.1); service meshes (overview).

**Assignment A4.4** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What is the main reason a container is less isolated than a virtual machine?

(A) Containers have no memory limit  
(B) Containers share the host kernel  
(C) Containers cannot use the network  
(D) Containers always run as root

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Namespaces give a container its own view of processes and network  
(B) Control groups limit resource use  
(C) A reconcile loop works by observing, comparing with the desired state and acting  
(D) Containers provide stronger isolation than hypervisor-based machines

**Q3 (2 marks, numerical answer).** Three runnable tasks have scheduler weights 1024, 512 and 512. What fraction of the processor does the first task receive under proportional sharing?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that a reconcile loop whose actions are idempotent and each move the state strictly closer to the desired state converges, absent outside disturbance, in at most as many steps as the initial distance.

**Q5 (3 marks, programming).** Write a simulated controller that maintains a desired number of replicas under random replica crashes and slow starts, and check convergence time against the model. Add a calculator for proportional processor shares and test it.

<details><summary>Key for A4.4 (open only after your attempt)</summary>

- **Q1:** B. All containers on a host share one kernel, so a kernel flaw affects all of them.
- **Q2:** A, B, C. Hypervisors normally give stronger isolation.
- **Q3:** 0.5 (tolerance ±0.001). The share is weight over total weight: 1024/2048 = 0.5.
- **Q4 (marking outline):** Define the distance as the number of differences between actual and desired state; each action reduces it by at least one and never increases it; idempotence means repeating an action does not undo progress; distance is a non-negative integer so it reaches zero in at most the initial value of steps.
- **Q5 (what a passing submission shows):** A reconcile loop with idempotent actions that returns to the desired state after failures, a convergence-time measurement, and unit tests for the share calculator.

</details>

### U4.5 Bridge: network flows and linear programming
**Sources:** none (prerequisite bridge, added so that later units rest on taught ground)
Bridge for: U4.6 (B4 and SWAN allocation), U3.6 (max–min fairness), U11.9 (optimisation in ML).
- **Topics:** Flow networks, capacities, max-flow and min-cut; Ford–Fulkerson and augmenting paths; max-flow min-cut theorem; multicommodity flow; linear programs in standard form; feasible region, vertices; the simplex method; duality and complementary slackness; max–min fair allocation by water-filling and its LP characterisation; integrality for flow problems.
- **Results:** Max-flow equals min-cut [P]; integral capacities give integral max-flow [P]; weak duality [P] and strong duality [S]; water-filling gives the unique max–min fair allocation [P].
- **Build:** Edmonds–Karp; a simplex solver on small LPs; water-filling allocation; checked against `scipy.optimize.linprog` and `networkx`. [local]
- **Gap-fills:** *[inferred: CLRS Ch.26; Bertsimas–Tsitsiklis, recalled, not checked]* interior-point methods (statement).

**Assignment A4.5** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What does the max-flow min-cut theorem state?

(A) Maximum flow equals the number of edges  
(B) The maximum flow value equals the capacity of a minimum cut  
(C) Maximum flow is always an integer  
(D) Minimum cut is always a single edge

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) With integer capacities there is an integer maximum flow  
(B) Weak duality says any dual feasible solution bounds the primal optimum  
(C) Max-min fair allocation is given by water-filling  
(D) The simplex method is proved to run in polynomial time in the worst case

**Q3 (2 marks, numerical answer (units)).** A network has edges s to a (capacity 3), s to b (2), a to t (2), b to t (3) and a to b (1). The cut that separates the source alone has capacity 5 and the cut that separates the sink alone has capacity 5. What is the maximum flow value?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove weak duality for a linear program: for a primal maximisation with constraints Ax at most b, x at least 0 and its dual, any dual feasible y gives an upper bound b times y on every primal feasible x.

**Q5 (3 marks, programming).** Implement the Edmonds-Karp max-flow algorithm and check it against a library on random graphs, and implement water-filling max-min fairness for flows over shared links, verifying that no flow can be increased without decreasing a smaller one.

<details><summary>Key for A4.5 (open only after your attempt)</summary>

- **Q1:** B. The value of a maximum flow equals the minimum capacity of a cut separating source and sink.
- **Q2:** A, B, C. Simplex can take exponential time in the worst case on some constructed instances.
- **Q3:** 5 units (tolerance ±0). Both of those cuts have capacity 5 and a flow of 5 is achievable, so the maximum flow is 5.
- **Q4 (marking outline):** For primal feasible x and dual feasible y, c x is at most (A transpose y) x because A transpose y is at least c and x is non-negative; this equals y (A x) which is at most y b since y is non-negative and A x is at most b.
- **Q5 (what a passing submission shows):** Max-flow equal to the library on random graphs with the min cut extracted, and a max-min allocation that passes a bottleneck-property check.

</details>

### U4.6 Network virtualization and geo-distributed clouds: SDN in the data center, VL2, NVP, MPLS, B4 and SWAN
**Sources:** CCDS W2
- **Topics:** Software defined network: key ideas of SDN, evolution of SDN, SDN challenges; multi-tenant data centers: the challenges; network virtualization; case study: VL2 (Clos topology, valiant load balancing, flat application addresses versus location addresses, directory system) and NVP (logical switches, tunnels, Open vSwitch, controller cluster); geo-distributed cloud data centers: inter-data-center networking, data center interconnection techniques: MPLS (labels, LSPs), Google's B4 and Microsoft's SWAN (centralized traffic engineering, bandwidth allocation, congestion-free updates).
- **Results:** Valiant load balancing makes any hose-model traffic matrix routable with each link loaded below capacity [S]; with scratch capacity s a SWAN update can be made congestion-free in at most ⌈1/s⌉−1 steps [S, recalled, not checked]; max–min allocation over paths is solved by repeated water-filling [D].
- **Build:** a TE allocator: max–min fair path allocation on a B4-like WAN graph and an LP-based allocation as in SWAN, compared; a logical-switch mapping table for multi-tenant isolation. [local]
- **Gap-fills:** *[inferred: Misra–Patel Ch.2, Ch.10 (checked)]* network slicing and ongoing SDN/NFV research directions.

**Assignment A4.6** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What does Valiant load balancing do in a data-centre network?

(A) It sends each flow on the shortest path only  
(B) It first sends traffic to a random intermediate node and then to the destination  
(C) It drops excess traffic  
(D) It requires a central scheduler for every packet

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) VL2 uses Valiant load balancing and ECMP  
(B) Network virtualization platforms build tenant networks with overlay tunnels  
(C) B4 applies centralised traffic engineering over SDN  
(D) MPLS requires a full IP lookup at every hop

**Q3 (2 marks, numerical answer (steps)).** With scratch capacity s = 0.1 on every link, a SWAN update can be made congestion-free in at most the ceiling of 1/s minus 1 steps. How many steps is that bound?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that on a full mesh of N nodes where each node sends and receives at most R in total, two-phase load balancing loads every link with at most 2R/N.

**Q5 (3 marks, programming).** Simulate flows over a topology and compute max-min fair rates by water-filling. Compare direct routing and Valiant load balancing under an adversarial permutation traffic matrix and report maximum link load.

<details><summary>Key for A4.6 (open only after your attempt)</summary>

- **Q1:** B. Two-phase randomised routing spreads any admissible traffic matrix evenly over the links.
- **Q2:** A, B, C. MPLS forwards by swapping labels.
- **Q3:** 9 steps (tolerance ±0). The ceiling of 10 is 10 and the bound is 9.
- **Q4 (marking outline):** In phase one each node splits its traffic equally over N intermediates so the load on link i to k is at most R/N; in phase two each intermediate sends to a destination whose total inbound traffic is at most R, split equally over its N sources, so each link carries at most R/N; the sum is 2R/N.
- **Q5 (what a passing submission shows):** Max-min rates verified by a bottleneck check and a comparison where load balancing lowers the maximum link load in the adversarial case at the cost of path length.

</details>

### U4.7 Google Cloud compute services: Compute Engine, App Engine, containers and Kubernetes, Cloud Functions
**Sources:** GCF W2
- **Topics:** *Use GCP to build your Apps.* Compute Engine (machine families and types, custom machine types, preemptible/Spot VMs, images, disks, startup scripts, managed instance groups and autoscaling); App Engine (standard versus flexible); containers and Kubernetes (Google Kubernetes Engine: clusters, node pools, workloads, services); Cloud Functions and event-driven functions (and Cloud Run); building applications on GCP; hands-on labs (cost tags in the lab list).
- **Results:** Autoscaling to a target utilisation u makes replicas = ⌈load/(u·capacity)⌉ and the M/M/c Erlang C formula gives the wait for a chosen c [D, from U2.1]; serverless cold-start adds a latency tail proportional to the cold fraction [D].
- **Build:** an autoscaler simulator (target tracking with cooldown) driven by a diurnal trace; plan and cost a three-tier deployment; the lab itself in a disposable project with a budget alert and same-day teardown. [local + credit]
- **Gap-fills:** *[inferred: week list on the NPTEL companion page, not the NPTEL syllabus; Google Cloud documentation]* product names and limits must be re-checked in the documentation before use.

**Assignment A4.7** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** An autoscaler targets utilisation u with per-replica capacity c. How many replicas does it need for load L?

(A) L divided by c  
(B) The ceiling of L divided by u times c  
(C) L times u times c  
(D) u divided by L

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) The Erlang C formula gives the probability of waiting in an M/M/c queue  
(B) Cold starts add a latency tail proportional to the fraction of cold requests  
(C) A target utilisation below one leaves headroom for bursts  
(D) Serverless functions never have cold starts

**Q3 (2 marks, numerical answer (replicas)).** The load is 900 requests per second, one replica handles 100 requests per second and the target utilisation is 0.6. How many replicas are required?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that with replicas at least L/(u c) the steady-state utilisation is at most u, and explain why the fleet is stable only if utilisation is below one.

**Q5 (3 marks, programming).** Simulate an autoscaler with a provisioning delay under a time-varying load and measure the fraction of time the response time exceeds an objective for several target utilisations. Compare with the M/M/c prediction at steady load.

<details><summary>Key for A4.7 (open only after your attempt)</summary>

- **Q1:** B. Replicas equal ceil(L/(u c)) so that each replica runs at about the target utilisation.
- **Q2:** A, B, C. Serverless platforms have cold starts that depend on scaling to zero and idle time.
- **Q3:** 15 replicas (tolerance ±0). Each replica should carry 60 requests per second so 900/60 = 15 replicas.
- **Q4 (marking outline):** Utilisation is load divided by total capacity, L/(n c); with n at least L/(u c) this is at most u; a queue is stable when arrival rate is less than service rate, which means utilisation below one; otherwise the backlog grows without bound.
- **Q5 (what a passing submission shows):** A simulator showing the trade between cost and objective violations as the target utilisation changes, and a steady-load check against the Erlang C formula.

</details>

### U4.8 Cloud networking on GCP: VPC networks, subnets, firewall rules, load balancing and hybrid connectivity
**Sources:** GCF W5–6
- **Topics:** It helps to network! and It helps to network (continued) (the two networking weeks of the cloud-platform course, whose published outline gives titles only, so the content below is *inferred* from the platform's own networking documentation and the networks of D2 and D3): the virtual private cloud (VPC) as a global software-defined network, regional subnets with CIDR ranges (the subnet arithmetic of U2.8 now applied), routes and next hops, internal and external addresses, firewall rules as stateful, prioritised allow and deny rules matched on tags or service accounts (policy ideas continue in U7.1), VPC peering and shared VPC, Cloud NAT, Cloud DNS (U6.2 records now managed), load balancing: layer 4 versus layer 7, global versus regional, health checks, connection draining, and the hashing that keeps a flow on one backend (consistent hashing and Maglev-style lookup, from U3.1 and U9.5); content delivery and anycast (U3.11); hybrid connectivity by IPsec VPN and by dedicated interconnect, with the bandwidth, latency and availability trade-offs; network tiers and egress cost; the monitoring of networks (flow logs, connectivity tests) that U12.1 takes up.
- **Results:** A CIDR planner must produce non-overlapping prefixes whose sizes are powers of two aligned on their own size, and a set of required host counts fits in an address block iff the sum of their rounded-up powers of two does [P]; with a firewall evaluated by priority, the first matching rule decides, so the effective policy is a decision list and shadowed rules are dead [D]; consistent hashing moves only about 1/n of the flows when one of n backends is added or removed [P]; the availability of two independent links in parallel is 1 − (1 − a)² [D].
- **Build:** a subnet planner that allocates and validates CIDR blocks and flags overlaps; a firewall-rule evaluator with priorities, stateful return traffic and a shadowed-rule detector; a Maglev-style lookup table with measured disruption on backend change against 1/n and with health-check ejection; a plan-only description of a two-region VPC with an HTTP load balancer, hybrid VPN and firewall policy, validated by your own checker and applied in a lab project only if the budget allows. [local; plan only; credit if applied]
- **Gap-fills:** *[inferred: the platform's VPC and load-balancing documentation; Eisenbud et al., Maglev, NSDI 2016, recalled, not checked]* Google's Andromeda network virtualisation (read the primary paper).

**Assignment A4.8** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** In a firewall evaluated by priority, which rule decides the action for a packet?

(A) The last matching rule  
(B) The highest-priority matching rule  
(C) All matching rules combined  
(D) A random matching rule

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Consistent hashing moves about one in n of the keys when one of n backends changes  
(B) CIDR blocks must be aligned on a multiple of their own size  
(C) Two independent links in parallel have availability 1 minus the product of their failure probabilities  
(D) A firewall rule that is shadowed by a higher-priority rule can still take effect

**Q3 (2 marks, numerical answer).** Two independent links each have availability 0.99. What is the availability of the pair when either one suffices?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that adding an (n+1)-th backend to a consistent-hash ring moves each key with probability 1/(n+1) in expectation, and that all moved keys go to the new backend.

**Q5 (3 marks, programming).** Write a subnet planner that allocates and validates CIDR blocks, a firewall rule evaluator with priorities and shadowed-rule detection, and a consistent-hash or Maglev-style table. Measure the fraction of flows that move when a backend is added or removed.

<details><summary>Key for A4.8 (open only after your attempt)</summary>

- **Q1:** B. The first match in priority order decides.
- **Q2:** A, B, C. A shadowed rule is dead.
- **Q3:** 0.9999 (tolerance ±0.00001). The pair fails only if both fail, probability 0.0001, so availability is 0.9999.
- **Q4 (marking outline):** By symmetry the new backend's arcs cover an expected fraction 1/(n+1) of the ring; a key moves exactly when it falls in one of those arcs; keys outside the arcs keep their owner; so every moved key moves to the new backend and the expected fraction moved is 1/(n+1).
- **Q5 (what a passing submission shows):** A planner that detects overlaps, an evaluator that reports shadowed rules, and measured disruption close to 1/n.

</details>


# PART B. CRYPTOGRAPHY, SECURITY, RISK AND PRIVACY

## D5. Cryptography: from classical ciphers to provable security, public-key systems, advanced primitives and post-quantum cryptography

Aim: three source courses (a practical-and-mathematical course, an application-oriented modern course and a provable-security course) merged into one sequence: every primitive built at toy size, its security notion stated precisely, and its central theorem proved or its deferral named. The mathematics (probability, modular arithmetic, algebra, complexity, number theory) is taught as bridges immediately before the first primitive that needs it. Hand-built cryptography here is for learning only and is never deployed (Master Rules 6.8 and 11.1); production work uses vetted libraries. Benchmarks (recalled, not checked): Katz and Lindell, *Introduction to Modern Cryptography* (named in the source); Stinson, *Cryptography: Theory and Practice* (named in the source); Stanoyevitch, *Introduction to Cryptography* (named in the source); Stallings, *Cryptography and Network Security* (named in the Ethical Hacking source); Boneh and Shoup, *A Graduate Course in Applied Cryptography*; Menezes, van Oorschot and Vanstone, *Handbook of Applied Cryptography*; Paar and Pelzl, *Understanding Cryptography*; Goldreich, *Foundations of Cryptography*; Hoffstein, Pipher and Silverman, *An Introduction to Mathematical Cryptography*; Washington, *Elliptic Curves*.

### U5.1 Bridge: probability, entropy and asymptotics for cryptography
**Sources:** none (prerequisite bridge, added so that later units rest on taught ground)
Bridge for: U5.3 (perfect secrecy, entropy of language), U5.9 (advantage and distinguishers), U5.10 (birthday bound), U5.12 onward (error probabilities).
- **Topics:** Discrete probability spaces, conditional probability, Bayes' rule, independence; union bound; random variables and expectation; Markov and Chebyshev inequalities; the birthday problem; statistical distance and distinguishing advantage; Shannon entropy, joint and conditional entropy, min-entropy, mutual information; asymptotic notation, polynomial and exponential functions, negligible versus noticeable functions; probabilistic algorithms (Las Vegas versus Monte Carlo, error amplification).
- **Results:** Union bound [P]; Markov and Chebyshev [P]; with k samples from N values the collision probability is at least 1 − e^{−k(k−1)/(2N)} so k ≈ 1.18√N gives 1/2 [D]; the expected number of draws to first collision is about √(πN/2) [D]; entropy is at most log|X| with equality for the uniform law [P]; statistical distance equals the best distinguisher's advantage [P]; sums and polynomial multiples of negligible functions are negligible [P].
- **Build:** Monte Carlo birthday experiments against the formulas; an entropy and index-of-coincidence estimator for any plain text you supply; a distinguisher-advantage estimator with confidence intervals. [local]
- **Gap-fills:** *[inferred: Katz–Lindell Appendix A; Mitzenmacher–Upfal Ch.1–3, recalled, not checked]* Chernoff bounds are added later in U9.2.

**Assignment A5.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** About how many random values from a set of size N must be drawn before a collision becomes likely?

(A) N  
(B) The square root of N  
(C) log N  
(D) N squared

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) The union bound gives the probability of a union as at most the sum of the probabilities  
(B) Markov's inequality bounds the probability that a non-negative variable exceeds a multiple of its mean  
(C) The statistical distance of two distributions equals the best distinguisher's advantage  
(D) Entropy is largest for a very skewed distribution

**Q3 (2 marks, numerical answer (bits)).** A source emits four symbols with probabilities 1/2, 1/4, 1/8 and 1/8. What is its Shannon entropy in bits?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that the entropy of a distribution on a finite set X is at most log2 of the size of X, with equality for the uniform distribution.

**Q5 (3 marks, programming).** Run Monte Carlo experiments for the birthday problem, estimating the number of draws to first collision for several N and comparing with the formula. Write an entropy and index-of-coincidence estimator for a plain text file.

<details><summary>Key for A5.1 (open only after your attempt)</summary>

- **Q1:** B. The birthday bound is about 1.18 times the square root of N for probability one half.
- **Q2:** A, B, C. Entropy is maximal for the uniform distribution.
- **Q3:** 1.75 bits (tolerance ±0.001). The sum is 0.5 + 0.5 + 0.375 + 0.375 = 1.75 bits.
- **Q4 (marking outline):** Entropy is the expected value of log2 of 1/p; by Jensen's inequality for the concave logarithm the expectation is at most log2 of the expectation of 1/p, which is log2 of the number of outcomes with positive probability; equality in Jensen holds only when 1/p is constant, i.e. uniform.
- **Q5 (what a passing submission shows):** Estimated collision counts close to the square root of pi N over two, a table against the formula, and an estimator that returns about 4.1 bits of letter entropy and an index of coincidence near 0.066 for English text, against 0.0385 for uniformly random letters.

</details>

### U5.2 Bridge: integers modulo n — divisibility, gcd, extended Euclid, inverses and fast exponentiation
**Sources:** CNS W3–4
- **Topics:** Mathematical background and number theory, first part: divisibility and the division algorithm; gcd and Euclid's algorithm with its running time (Lamé); Bézout's identity and the extended Euclid algorithm; modular inverse and when it exists; congruences and the ring Z_n; solving linear congruences; the unit group Z_n^* (counting continues in U5.12 with Fermat's little theorem, the Euler phi-function and Euler's theorem); modular exponentiation by square-and-multiply and its cost in bit operations.
- **Results:** gcd(a, b) = gcd(b, a mod b) [P]; Bézout's identity [P]; Euclid's algorithm takes O(log b) steps and at most about 4.8·log₁₀b divisions by Lamé [P]; a has an inverse mod n iff gcd(a, n) = 1 [P]; square-and-multiply computes a^e mod n with O(log e) multiplications [P].
- **Build:** gcd, extended gcd, modular inverse, linear congruence solver and square-and-multiply, all checked against `math.gcd` and `pow(a, -1, n)`; bit-operation counter. [local]
- **Gap-fills:** *[inferred: Stinson Ch.2; Niven–Zuckerman–Montgomery, recalled, not checked]* binary gcd, Montgomery multiplication (idea only).

**Assignment A5.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** When does an integer a have an inverse modulo n?

(A) When a is odd  
(B) When gcd(a, n) = 1  
(C) When a is less than n  
(D) When n is prime only

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Euclid's algorithm takes O(log b) division steps  
(B) Bezout's identity expresses gcd(a, b) as an integer combination of a and b  
(C) Square-and-multiply uses O(log e) multiplications to compute a to the e modulo n  
(D) Every integer has an inverse modulo every n

**Q3 (2 marks, numerical answer).** What is the inverse of 7 modulo 40?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that the extended Euclidean algorithm returns integers x and y with a x + b y = gcd(a, b).

**Q5 (3 marks, programming).** Implement gcd, extended gcd, modular inverse and square-and-multiply, check them against math.gcd and pow, and count bit operations for increasing sizes to confirm the predicted growth.

<details><summary>Key for A5.2 (open only after your attempt)</summary>

- **Q1:** B. Bezout's identity gives an inverse exactly when a and n are coprime.
- **Q2:** A, B, C. Only units modulo n have inverses.
- **Q3:** 23 (tolerance ±0). 7 times 23 is 161 which is 4 times 40 plus 1, so the inverse is 23.
- **Q4 (marking outline):** Maintain the invariant that each remainder r_i is an integer combination of a and b; the initial remainders a and b are; each new remainder is r_{i-1} minus a quotient times r_i, again a combination; the last non-zero remainder is the gcd, so it is a combination.
- **Q5 (what a passing submission shows):** Functions agreeing with the library on random inputs up to 2048 bits, and a plot where the number of multiplications for modular exponentiation grows linearly in the exponent bit length.

</details>

### U5.3 Introduction to cryptography and classical ciphers, cryptanalysis and perfect secrecy
**Sources:** CNS W1, o; TPMC W1–2, o; FOC W1, o; EH W6
- **Topics:** Introduction to cryptography: goals (confidentiality, integrity, authentication, non-repudiation), Kerckhoffs' principle, attacker models (ciphertext-only, known-plaintext, chosen-plaintext, chosen-ciphertext). Classical cryptosystems: shift, affine, monoalphabetic and polyalphabetic ciphers (Vigenère, autokey, Playfair, Hill), transposition. More on classical cryptosystems and various analysis: frequency analysis, index of coincidence, Kasiski examination, Friedman's test. Symmetric key cryptography and symmetric-key encryption (Gen, Enc, Dec); historical ciphers; private-key encryption and public-key encryption introduced (Ethical Hacking Week 6). Perfect security and its limitations: Shannon's theorem, the one-time pad, the key-length barrier. Course overview. Outline map of the cryptography courses (named topics and where taught): block and stream ciphers (U5.4, U5.6, U5.7), elliptic curve cryptography (U5.15), zero-knowledge proofs (U5.24), homomorphic encryption (U5.23), identity-based, attribute-based and functional encryption (U5.22), two-party and multi-party computation (U5.21), bitcoin and crypto-currency (U9.21), post-quantum cryptography (U5.25); real-world applications in secure communications and digital payments (the channel of U13.2, the signatures of U5.17 and the blockchain of U9.21); the evolving landscape of cyber threats and the cybersecurity challenges the cryptanalysis part addresses: network security, data security, mobile security, cloud security (U7.7) and endpoint security (U6.4); careers in cybersecurity, software engineering and digital forensics (evidence handling in U8.4); the aim of the provable-security course to let you read current research papers and standards.
- **Results:** Shannon's theorem: for |M| = |K| = |C| a scheme is perfectly secret iff keys are uniform and each (m, c) pair has exactly one key [P]; perfect secrecy forces |K| ≥ |M| [P]; the one-time pad is perfectly secret and two-time pad reveals m₁ ⊕ m₂ [P]; the index of coincidence is about 0.066 for English and 1/26 for uniform text, which gives the Vigenère key length [D]; the affine cipher key space is φ(26)·26 = 312 [D].
- **Build:** shift, affine, substitution, Vigenère and Hill ciphers (Hill inverse by the U5.2 inverse and U5.5 matrix inversion); automatic breakers (frequency, IC, Kasiski, hill-climbing with n-gram scores built from a text you supply); exhaustive check of perfect secrecy for a toy one-time pad; a two-time-pad crib-dragging tool. [local]
- **Gap-fills:** *[inferred: Stinson Ch.1; Katz–Lindell Ch.1–2]* Enigma and rotor machines, Bletchley-era cryptanalysis (history).

**Assignment A5.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What does perfect secrecy require of the key length relative to the message length?

(A) The key must be shorter  
(B) The key must be at least as long as the message  
(C) The key length is irrelevant  
(D) The key must be exactly one byte

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements about Shannon's theorem and the one-time pad are correct?

(A) Keys must be uniformly distributed  
(B) For each message and ciphertext exactly one key maps one to the other  
(C) The key space must be at least as large as the message space  
(D) Reusing a one-time pad key is safe

**Q3 (2 marks, numerical answer (keys)).** How many keys does the affine cipher on a 26-letter alphabet have?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that a perfectly secret encryption scheme must have at least as many keys as messages.

**Q5 (3 marks, programming).** Implement shift, affine, Vigenere and Hill ciphers and a breaker for Vigenere using the index of coincidence and Kasiski examination. Test on texts you supply.

<details><summary>Key for A5.3 (open only after your attempt)</summary>

- **Q1:** B. Shannon showed that perfect secrecy forces the key space to be at least as large as the message space.
- **Q2:** A, B, C. Two ciphertexts under the same pad reveal the XOR of the plaintexts.
- **Q3:** 312 keys (tolerance ±0). There are phi(26) = 12 valid multipliers and 26 shifts, giving 312.
- **Q4 (marking outline):** Fix a ciphertext c with positive probability; the set of messages decrypting c under some key has size at most the number of keys; perfect secrecy means every message has positive probability of producing c; so every message is in that set; therefore the number of keys is at least the number of messages.
- **Q5 (what a passing submission shows):** Ciphers with round-trip tests, a breaker that recovers the key length and key on at least 20 test texts, and a two-time-pad crib-dragging demonstration.

</details>

### U5.4 Block ciphers: design principles, SPN, Feistel networks, DES, Triple DES and modes of operation
**Sources:** CNS W1–2; TPMC W3–4; FOC W4–5
- **Topics:** Block cipher: design principles of confusion and diffusion; substitution–permutation network (SPN) and Feistel structure; Data Encryption Standard (DES): initial and final permutations, 16 rounds, expansion, S-boxes, P-box, key schedule, weak and semi-weak keys, the avalanche effect, complementation property, brute-force attack; Triple DES (EDE with two or three keys), the meet-in-the-middle attack on double encryption; modes of operation: ECB, CBC, CFB, OFB and CTR, padding, IV and nonce requirements, malleability; practical constructions of block ciphers (DES, AES and message authentication codes are split: MACs in U5.11, AES in U5.7).
- **Results:** A Feistel network is invertible whatever the round function [P]; DES decryption is encryption with the key schedule reversed [P]; DES(k̄, m̄) = complement of DES(k, m) [P]; meet-in-the-middle on double encryption costs about 2^{n+1} operations and 2^n memory [D]; ECB leaks block equality, CBC with a predictable IV and CTR with a repeated nonce are broken [D].
- **Build:** DES from scratch checked on the standard vector (key 133457799BBCDFF1, plaintext 0123456789ABCDEF, ciphertext 85E813540F0AB405), Triple DES, and the five modes; avalanche statistics; a block-equality leak on a tiny synthetic bitmap; meet-in-the-middle on a reduced toy double cipher. [local; learning only]
- **Gap-fills:** *[inferred: Stallings Ch.3–6; Katz–Lindell Ch.6]* Skipjack, Blowfish and the 64-bit-block birthday limit (the SWEET32 result, read from its primary paper).

**Assignment A5.4** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What is the key property of a Feistel network?

(A) It requires an invertible round function  
(B) It is invertible whatever the round function is  
(C) It needs 16 rounds  
(D) It cannot be used for encryption

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) DES has a complementation property  
(B) A meet-in-the-middle attack on double encryption needs about 2 to the n plus 1 operations  
(C) ECB mode leaks which plaintext blocks are equal  
(D) CBC with a fixed predictable IV is a good design

**Q3 (2 marks, numerical answer).** A meet-in-the-middle attack on double encryption with an n-bit key needs about 2 to the power n plus 1 operations. What is the exponent for n = 56?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that a Feistel network with any round functions is invertible, and that decryption is encryption with the round keys reversed.

**Q5 (3 marks, programming).** Implement DES from scratch and check it on the standard vector key 133457799BBCDFF1, plaintext 0123456789ABCDEF, ciphertext 85E813540F0AB405, then add Triple DES and ECB, CBC, CFB, OFB and CTR modes. For learning only.

<details><summary>Key for A5.4 (open only after your attempt)</summary>

- **Q1:** B. The structure inverts by running the rounds in reverse order, regardless of whether F is invertible.
- **Q2:** A, B, C. A predictable IV breaks chosen-plaintext security.
- **Q3:** 57 (tolerance ±0). The exponent is 57, so about 2^57 operations.
- **Q4 (marking outline):** One round maps (L, R) to (R, L xor F(R)); given the output (L', R') recover R = L' and L = R' xor F(L'); so each round is invertible; composition of invertible rounds is invertible, applying inverse rounds in reverse order, which equals running the same structure with keys reversed.
- **Q5 (what a passing submission shows):** The known ciphertext reproduced, mode round trips on random messages, avalanche statistics near half the bits, and a documented statement that the code is for learning.

</details>

### U5.5 Bridge: groups, rings, fields, finite fields and linear algebra over them
**Sources:** CNS W3; TPMC W5
- **Topics:** Mathematical backgrounds: abstract algebra, group theory, field theory, linear algebra. Groups, subgroups, cosets, Lagrange's theorem, cyclic groups, generators, orders of elements; homomorphisms; rings, ideals and integral domains; fields; the field Z_p; polynomial rings over a field and irreducible polynomials; finite fields GF(pⁿ) and the construction of GF(2⁸) = GF(2)[x]/(x⁸ + x⁴ + x³ + x + 1); primitive elements; vector spaces over finite fields; matrices, rank, determinants and inversion mod n; Gaussian elimination over GF(p); number theory introduced as the arithmetic of these structures.
- **Results:** Lagrange's theorem [P]; the order of an element divides the group order [P]; a degree-d polynomial over a field has at most d roots [P]; every finite subgroup of the multiplicative group of a field is cyclic [P]; existence and uniqueness of GF(pⁿ) [X, proof beyond course scope]; a matrix is invertible over Z_n iff its determinant is a unit mod n [P].
- **Build:** GF(p) and GF(2⁸) arithmetic (xtime multiplication, log/antilog tables), polynomial arithmetic over a field, matrix inverse mod n, brute-force group-axiom checker. [local]
- **Gap-fills:** *[inferred: Lidl–Niederreiter; Hoffstein–Pipher–Silverman Ch.2, recalled, not checked]* Galois theory beyond finite fields is not needed.

**Assignment A5.5** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What does Lagrange's theorem say about a subgroup H of a finite group G?

(A) The order of H divides the order of G  
(B) The order of H equals that of G  
(C) The order of H is prime  
(D) H is always cyclic

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) A polynomial of degree d over a field has at most d roots  
(B) Every finite subgroup of the multiplicative group of a field is cyclic  
(C) GF(2^8) has 256 elements  
(D) Z_n is a field for every n greater than one

**Q3 (2 marks, numerical answer (generators)).** How many generators does the multiplicative group modulo the prime 23 have?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove Lagrange's theorem: the order of a subgroup of a finite group divides the order of the group.

**Q5 (3 marks, programming).** Implement arithmetic in GF(2^8) modulo x^8 + x^4 + x^3 + x + 1 with log and antilog tables, verify that every non-zero element has an inverse, and implement matrix inversion modulo n with a check.

<details><summary>Key for A5.5 (open only after your attempt)</summary>

- **Q1:** A. Cosets partition G into pieces of equal size, so the order of G is a multiple of the order of H.
- **Q2:** A, B, C. Z_n is a field only when n is prime.
- **Q3:** 10 generators (tolerance ±0). The group is cyclic of order 22, and phi(22) = 10 elements generate it.
- **Q4 (marking outline):** Left cosets g H have the same size as H because x to g x is a bijection; two cosets are equal or disjoint; the cosets cover the group; so the group order is the number of cosets times the order of H.
- **Q5 (what a passing submission shows):** Field axioms verified exhaustively, inverses found for all 255 elements, and a matrix inverse modulo n that multiplies back to the identity.

</details>

### U5.6 Stream ciphers: one-time pad, autokey, LFSRs, Berlekamp–Massey and modern stream ciphers
**Sources:** CNS W2–3,11; TPMC W4; FOC W3
- **Topics:** Stream cipher (CNS Week 2, TPMC Week 4 "Stream Cipher One-time Pad", Autokey Cipher); LFSR-based stream cipher: feedback polynomial, state, period, maximal-length sequences and primitive polynomials, linear complexity, Berlekamp–Massey algorithm; nonlinear filter and combiner generators and clock-controlled generators (A5/1); modern stream ciphers: RC4 and its biases, Salsa20 and ChaCha20, eSTREAM designs (Trivium, Grain); stream ciphers in the provable-security course (security of PRG-based design is in U5.9).
- **Results:** An n-stage LFSR with a primitive feedback polynomial has period 2ⁿ − 1 [P]; Berlekamp–Massey recovers the shortest LFSR from 2L keystream bits [P]; keystream reuse is catastrophic [P]; ChaCha's quarter-round is invertible [D].
- **Build:** an LFSR with arbitrary taps, Berlekamp–Massey, a known-plaintext attack recovering an LFSR key; ChaCha20 from scratch checked against its RFC 8439 vectors and a library. [local; learning only]
- **Gap-fills:** *[inferred: Paar–Pelzl Ch.2; RFC 8439, recalled, not checked]* Grain and Trivium details, RC4 prohibition in TLS (RFC 7465).

**Assignment A5.6** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What is the maximum period of an LFSR with n stages?

(A) 2^n  
(B) 2^n - 1  
(C) n  
(D) n squared

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) The Berlekamp-Massey algorithm finds the shortest LFSR from 2L keystream bits  
(B) Reusing keystream reveals the XOR of two plaintexts  
(C) A plain LFSR keystream is secure against known-plaintext attacks  
(D) The ChaCha quarter-round is invertible

**Q3 (2 marks, numerical answer (steps)).** What is the period of a maximal-length 16-stage LFSR?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that if two messages are encrypted with the same stream-cipher keystream, the XOR of the ciphertexts equals the XOR of the plaintexts, and explain why this breaks confidentiality.

**Q5 (3 marks, programming).** Implement an LFSR with arbitrary taps and Berlekamp-Massey, mount a known-plaintext attack recovering the register, and implement ChaCha20 checked against the RFC 8439 test vectors. For learning only.

<details><summary>Key for A5.6 (open only after your attempt)</summary>

- **Q1:** B. The all-zero state is a fixed point, so the maximum period is 2^n - 1, reached with a primitive feedback polynomial.
- **Q2:** A, B, D. A known-plaintext attack recovers an LFSR by Berlekamp-Massey.
- **Q3:** 65535 steps (tolerance ±0). The maximum period is 2^16 - 1 = 65535.
- **Q4 (marking outline):** Ciphertexts are m1 xor k and m2 xor k; xor them to get m1 xor m2 because k xor k is zero; the result leaks relations between the plaintexts, and with redundancy in natural language (crib dragging) both can often be recovered.
- **Q5 (what a passing submission shows):** A correct recovery of taps and state from 2L bits, ChaCha20 matching the library output, and a note that the code is not for deployment.

</details>

### U5.7 The Advanced Encryption Standard (Rijndael)
**Sources:** CNS W5; TPMC W3–4; FOC W5
- **Topics:** Advanced Encryption Standard (AES), Rijndael: the state as a 4×4 byte matrix over GF(2⁸); SubBytes (field inverse followed by an affine map), ShiftRows, MixColumns (an MDS matrix), AddRoundKey; key schedule for 128, 192 and 256-bit keys; 10, 12 or 14 rounds; decryption; the wide-trail design strategy and branch number 5; table implementations and cache-timing exposure; hardware support (AES-NI); AES in the modes of U5.4.
- **Results:** The AES S-box has maximum differential probability 4/256 and nonlinearity 112 [D by exhaustive computation]; MixColumns is MDS with branch number 5 [P by exhaustive check]; in four rounds there are at least 25 active S-boxes [S]; the FIPS-197 C.1 example vector is reproduced [check].
- **Build:** AES-128 from scratch generating the S-box algorithmically and checked on the FIPS-197 vector (key 000102…0f, plaintext 00112233…ff, ciphertext 69c4e0d86a7b0430d8cdb78070b4c55a) and against a library. [local; learning only]
- **Gap-fills:** *[inferred: Daemen–Rijmen, The Design of Rijndael; FIPS 197, recalled, not checked]* related-key attacks on AES-192 and AES-256 (read the primary paper), AES-based hashing.

**Assignment A5.7** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** How many rounds does AES-256 use?

(A) 10  
(B) 12  
(C) 14  
(D) 16

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) The AES S-box is built from inversion in GF(2^8) followed by an affine map  
(B) MixColumns has branch number five  
(C) AES is a Feistel cipher  
(D) AES-128 uses 10 rounds

**Q3 (2 marks, numerical answer (keys)).** How many 128-bit round keys does AES-128 need, including the initial whitening key?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that the AES S-box is a permutation of the 256 byte values.

**Q5 (3 marks, programming).** Implement AES-128 from scratch, generate the S-box algorithmically, and check against the FIPS-197 vector with key 000102030405060708090a0b0c0d0e0f, plaintext 00112233445566778899aabbccddeeff and ciphertext 69c4e0d86a7b0430d8cdb78070b4c55a, and against a library. For learning only.

<details><summary>Key for A5.7 (open only after your attempt)</summary>

- **Q1:** C. AES uses 10, 12 and 14 rounds for 128, 192 and 256-bit keys.
- **Q2:** A, B, D. AES is a substitution-permutation network.
- **Q3:** 11 keys (tolerance ±0). There are 10 rounds plus the initial AddRoundKey, so 11 round keys.
- **Q4 (marking outline):** The map x to x inverse in GF(2^8), with 0 mapped to 0, is a bijection since every non-zero element has a unique inverse; the affine map is an invertible linear map plus a constant on bytes; the composition of two bijections is a bijection.
- **Q5 (what a passing submission shows):** The known ciphertext reproduced, decryption round trips, random-key comparison with the library, and an S-box generated rather than typed in.

</details>

### U5.8 Bridge: computational complexity, one-way functions and the reduction method
**Sources:** none (prerequisite bridge, added so that later units rest on taught ground)
Bridge for: U5.9 onward (every proof of security is a reduction). Addresses the stated prerequisite of the provable-security course: exposure to discrete mathematics, algorithms and theory of computation.
- **Topics:** Turing machines and polynomial time; P, NP, co-NP, BPP, RP; reductions between problems; probabilistic polynomial-time adversaries; negligible functions; one-way functions, one-way permutations and trapdoor functions; hard-core predicates; computational indistinguishability and the hybrid argument; security games, advantage and the reduction template ("if A breaks the scheme then B breaks the assumption"); concrete versus asymptotic security.
- **Results:** If one-way functions exist then P ≠ NP [P]; computational indistinguishability is transitive over polynomially many hybrids [P]; advantage loss accumulates additively along a chain of reductions [D]; Goldreich–Levin hard-core bit [X, beyond course scope].
- **Build:** a generic security-game harness (challenger, adversary interface, trial runner with confidence intervals) reused in U5.9–U5.16. [local]
- **Gap-fills:** *[inferred: Sipser; Goldreich Ch.2; Katz–Lindell Ch.3, recalled, not checked]* the P versus NP status of the assumptions used later (factoring, discrete log are not known to be NP-complete).

**Assignment A5.8** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What does a security proof by reduction show?

(A) That the scheme is unconditionally secure  
(B) That any adversary breaking the scheme yields an adversary breaking the assumption  
(C) That the scheme runs in polynomial time  
(D) That the key is short

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Negligible functions are closed under addition  
(B) A polynomial times a negligible function is negligible  
(C) If one-way functions exist then P is not equal to NP  
(D) Factoring is known to be NP-complete

**Q3 (2 marks, numerical answer).** A chain of 5 hybrid distributions has each adjacent pair distinguishable with advantage at most 2 to the power minus 40. What is the bound on the advantage between the ends of the chain?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove the hybrid argument: if D distinguishes distributions H0 and Hk with advantage eps, then for some i it distinguishes Hi and H(i+1) with advantage at least eps over k.

**Q5 (3 marks, programming).** Write a generic security-game harness with a challenger, adversary interface and trial runner with confidence intervals, and test it with a toy scheme and a simple adversary with known advantage.

<details><summary>Key for A5.8 (open only after your attempt)</summary>

- **Q1:** B. A reduction transforms an adversary against the scheme into one against the underlying hard problem.
- **Q2:** A, B, C. Factoring is not known to be NP-complete.
- **Q3:** 0 (tolerance ±1e-13). Advantages add along a hybrid chain, giving at most 5 times 2^-40 which is about 4.5e-12.
- **Q4 (marking outline):** By the triangle inequality the advantage between H0 and Hk is at most the sum of the advantages between consecutive hybrids; if all k were smaller than eps over k the sum would be smaller than eps; so some consecutive pair has at least eps over k.
- **Q5 (what a passing submission shows):** A harness that estimates advantage with a confidence interval, validated against a scheme whose advantage is known analytically, to be reused in later units.

</details>

### U5.9 Provable security for symmetric encryption: computational security, PRGs, PRFs and CPA security
**Sources:** FOC W2–4; TPMC W2
- **Topics:** Computational security and semantic security; pseudorandom generators (PRGs); stream ciphers from PRGs; provably-secure instantiation of a PRG (one-way permutation plus hard-core bit, Blum–Micali) and practical instantiation of a PRG (AES-CTR, ChaCha; why LFSRs fail); CPA-security and pseudorandom functions (PRFs); pseudorandom permutations; CPA-secure ciphers from a PRF; security of the modes of operation of block ciphers (CBC, CTR); theoretical constructions of block ciphers (GGM tree from a PRG, Luby–Rackoff three-round and four-round Feistel) and practical constructions of block ciphers; the PRP/PRF switching lemma.
- **Results:** PRG expansion by hybrid argument [P]; PRG plus one-time pad is computationally secure encryption [P]; Enc_k(m) = (r, F_k(r) ⊕ m) is CPA-secure when F is a PRF [P]; PRP/PRF switching lemma with gap ≤ q²/2^{n+1} [P]; CBC and CTR are CPA-secure up to a birthday term q²/2ⁿ [S]; Luby–Rackoff [S].
- **Build:** the U5.8 harness breaking ECB, CBC with a fixed IV and CTR with repeated counters; measured advantage versus number of queries for CBC against its birthday bound; a GGM PRF from a PRG. [local]
- **Gap-fills:** *[inferred: Boneh–Shoup Ch.3–5; Katz–Lindell Ch.3–4, recalled, not checked]* formal definitions of IND-CPA by left-or-right and real-or-random games.

**Assignment A5.9** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Which encryption is CPA-secure when F is a pseudorandom function and r is fresh and random?

(A) Enc(m) = F_k(m)  
(B) Enc(m) = (r, F_k(r) xor m)  
(C) Enc(m) = m xor k with a fixed k  
(D) Enc(m) = m

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) The PRP/PRF switching lemma bounds the gap by about q squared over 2 to the n plus 1  
(B) CBC with a fixed IV is CPA-secure  
(C) CTR mode with repeated counters is insecure  
(D) The three-round Luby-Rackoff Feistel network gives a pseudorandom permutation

**Q3 (2 marks, numerical answer).** The switching lemma bounds the distinguishing gap between a random permutation and a random function on 128-bit blocks by q squared over 2 to the 129. What is the bound for q = 2^20 queries?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that doubling the output length of a length-expanding PRG by one more step gives a PRG, using the hybrid argument.

**Q5 (3 marks, programming).** Using your harness, break ECB, CBC with a fixed IV and CTR with repeated counters, measure the advantage of a distinguisher against CBC as the number of queries approaches the birthday bound, and build a GGM PRF from a PRG.

<details><summary>Key for A5.9 (open only after your attempt)</summary>

- **Q1:** B. Randomised encryption from a PRF with a fresh nonce is CPA-secure.
- **Q2:** A, C, D. A fixed IV makes CBC deterministic in its first block and breaks CPA security.
- **Q3:** 0 (tolerance ±1e-28). The bound is 2^40/2^129 = 2^-89 which is about 1.6e-27.
- **Q4 (marking outline):** Define hybrids replacing the first output with a random string and then the second; adjacent hybrids differ by one application of the original PRG on a seed or a random string; a distinguisher between the ends gives one between adjacent hybrids by the hybrid argument, so the advantage loss is at most a factor of two.
- **Q5 (what a passing submission shows):** Attacks achieving advantage near one on the broken modes, a plot of advantage against queries tracking the q squared over 2 to the n term, and a PRF built by tree expansion.

</details>

### U5.10 Cryptographic hash functions: Merkle–Damgård, Davies–Meyer, SHA-2, SHA-3, birthday attacks and the random-oracle model
**Sources:** CNS W8–9; TPMC W8–9; FOC W6–7; EH W7
- **Topics:** Hash function and cryptographic hash function: compression versus hashing, the three security notions (preimage, second-preimage and collision resistance) and how they are ordered; the ideal-cipher model and the Davies–Meyer construction of a compression function from a block cipher; the Merkle–Damgård paradigm with length padding and its collision-resistance reduction; length-extension and how it is avoided (truncation, HMAC, sponge); Secure Hash Algorithm (SHA): SHA-1 structure and its collision history, SHA-2 (SHA-256 and SHA-512 round functions and message schedule), SHA-3 (Keccak sponge: rate, capacity, the permutation f); birthday attacks on cryptographic hash functions (generic collision search, Pollard-rho cycle-finding with negligible memory); applications of hash functions (integrity, commitment, password storage and key stretching, Merkle trees, proof of work, fingerprints); the random-oracle model, what a proof in it does and does not show (Canetti–Goldreich–Halevi, recalled, not checked), and the standard-model alternatives.
- **Results:** If the compression function is collision-resistant then Merkle–Damgård with length padding is collision-resistant [P]; Davies–Meyer is collision-resistant in the ideal-cipher model, with the birthday bound tight [S]; with an n-bit output a generic collision costs about 2^{n/2} evaluations and a preimage about 2ⁿ [D]; a length-extension attack on H(k ‖ m) forges H(k ‖ m ‖ pad ‖ m′) without k [D]; collision resistance implies second-preimage resistance but not conversely under standard assumptions [P, via a contrived hash].
- **Build:** SHA-256 from scratch, checked on SHA-256("abc") = ba7816bf…15ad and against `hashlib`; Keccak-f[1600] and SHA3-256 from scratch, checked on SHA3-256("") = a7ffc6f8…434a; Davies–Meyer on the toy cipher of U5.4; a length-extension demo on your own toy Merkle–Damgård hash; collision search on a truncated 40-bit SHA-256 by birthday and by Floyd cycle finding, with measured costs against 2^{n/2}; a Merkle tree with inclusion proofs. [local; learning only]
- **Gap-fills:** *[inferred: Boneh–Shoup Ch.8; Katz–Lindell Ch.5 and Ch.6, recalled, not checked]* the SHAttered collision and chosen-prefix attacks on SHA-1 (read from the primary papers), BLAKE2/BLAKE3 as modern alternatives.

**Assignment A5.10** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** For an n-bit hash function, about how many evaluations does a generic collision search need?

(A) 2^n  
(B) 2^(n/2)  
(C) n^2  
(D) 2n

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Merkle-Damgard with length padding is collision-resistant if the compression function is  
(B) H(key concatenated with message) is open to length extension for plain Merkle-Damgard hashes  
(C) SHA-3 is built as a sponge  
(D) SHA-256 is built as a sponge

**Q3 (2 marks, numerical answer).** A 64-bit hash is evaluated on 2^32 distinct inputs. Using the approximation 1 minus e to the power of minus k squared over 2N, what is the probability of at least one collision?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that if the compression function is collision-resistant then Merkle-Damgard with length padding is collision-resistant: a collision for the hash yields one for the compression function.

**Q5 (3 marks, programming).** Implement SHA-256 from scratch and check SHA-256 of abc, implement Keccak-f and SHA3-256 and check the empty-string value, and find collisions on a 40-bit truncation by birthday search and by Floyd cycle finding, comparing costs with 2^20.

<details><summary>Key for A5.10 (open only after your attempt)</summary>

- **Q1:** B. The birthday bound makes a collision likely after about 2^(n/2) evaluations.
- **Q2:** A, B, C. SHA-256 uses the Merkle-Damgard construction with a Davies-Meyer compression function.
- **Q3:** 0.3935 (tolerance ±0.001). The exponent is 2^64/2^65 = 0.5 so the probability is 1 minus e^-0.5, about 0.393.
- **Q4 (marking outline):** Suppose two different messages hash to the same value; if their lengths differ the final blocks include different lengths so the last compression calls collide on different inputs; if the lengths are equal, walk back from the last block until the inputs to the compression function differ, which must happen since the messages differ, giving a collision of the compression function.
- **Q5 (what a passing submission shows):** Digests equal to hashlib on random inputs, truncated collisions found in about 2^20 evaluations, and a length-extension demonstration on a toy hash of your own.

</details>

### U5.11 Message authentication and authenticated encryption: MACs, HMAC, CBC-MAC, universal hashing and AEAD
**Sources:** CNS W8; TPMC W8; FOC W5–8
- **Topics:** Message authentication and Message Authentication Codes (MAC): the forgery game (existential unforgeability under chosen-message attack, with and without verification queries); information-theoretic secure MAC: pairwise-independent hash families, one-time MACs and Carter–Wegman universal hashing (Poly1305 as an instance); computational MACs from a PRF; CBC-MAC and why variable-length messages break it, CMAC and prefix-free fixes; HMAC and its nested construction; authenticated encryption: the three generic compositions (encrypt-and-MAC, MAC-then-encrypt, encrypt-then-MAC), generic constructions of authenticated encryption schemes, CCA security and ciphertext integrity, and why the order matters in practice (padding-oracle failures); AEAD modes (GCM, CCM, ChaCha20-Poly1305, OCB) with associated data, nonce-misuse behaviour and the repeated-nonce catastrophe in GCM; MACs in the random-oracle model (applications of hash functions, continuing U5.10).
- **Results:** A one-time MAC from a pairwise-independent family has forgery probability 1/p, so it is information-theoretically secure, and it cannot be reused [P]; a PRF is a secure fixed-length MAC with forgery advantage at most q/2ⁿ plus the PRF advantage [P]; plain CBC-MAC is forgeable on variable-length messages by a three-query splice [D]; encrypt-then-MAC with independent keys is CCA-secure when the cipher is CPA-secure and the MAC is strongly unforgeable [P]; HMAC security from the compression function as a PRF [X, beyond course scope].
- **Build:** HMAC-SHA-256 from scratch checked against `hmac`; CBC-MAC and the splice forgery; a polynomial-evaluation MAC over GF(p) with the 1/p forgery bound measured; Poly1305 from scratch against a library vector; encrypt-then-MAC from your own AES and HMAC; a padding-oracle attack against your own unauthenticated CBC server on loopback, then the same attack failing against encrypt-then-MAC. [local; learning only]
- **Gap-fills:** *[inferred: Boneh–Shoup Ch.6–9; RFC 8439, RFC 5116, recalled, not checked]* GHASH and the GCM forbidden attack on repeated nonces, SIV-style nonce-misuse-resistant AE (AES-GCM-SIV).

**Assignment A5.11** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Which composition of encryption and a MAC with independent keys gives CCA security when the cipher is CPA-secure and the MAC strongly unforgeable?

(A) MAC-then-encrypt  
(B) Encrypt-and-MAC  
(C) Encrypt-then-MAC  
(D) Encrypt only

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) A one-time MAC built from a pairwise independent hash family is information-theoretically secure for one message  
(B) Plain CBC-MAC is forgeable on variable-length messages  
(C) HMAC uses a nested hash construction  
(D) MAC-then-encrypt is always CCA-secure in practice

**Q3 (2 marks, numerical answer).** A one-time MAC over the prime field with p = 2^61 - 1 has forgery probability 1/p. What is that probability?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that the one-time MAC tag = a m + b mod p with uniform secret key (a, b) cannot be forged with probability better than 1/p after seeing one message and tag.

**Q5 (3 marks, programming).** Implement HMAC-SHA-256 and check it against hmac, show the CBC-MAC splice forgery on variable-length messages, implement Poly1305, and run a padding-oracle attack against your own unauthenticated CBC server on loopback and then against encrypt-then-MAC. For learning only.

<details><summary>Key for A5.11 (open only after your attempt)</summary>

- **Q1:** C. Authenticating the ciphertext makes any modified ciphertext fail verification before decryption.
- **Q2:** A, B, C. Padding-oracle attacks have broken MAC-then-encrypt implementations.
- **Q3:** 0 (tolerance ±1e-20). The probability is about 4.3e-19.
- **Q4 (marking outline):** Given one pair (m, t), for every candidate tag t' on a new message m' there is exactly one key (a, b) consistent with both pairs because the two linear equations have a unique solution when m differs from m'; keys are uniform so each t' is equally likely; the success probability is 1/p.
- **Q5 (what a passing submission shows):** HMAC equal to the library, a working forgery for CBC-MAC, a padding oracle that recovers a message from your own server, and the same attack failing against the authenticated version.

</details>

### U5.12 Bridge: number theory for public-key cryptography — Fermat, Euler, CRT, quadratic residues, Legendre and Jacobi symbols, primality testing and factoring
**Sources:** CNS W4,6; TPMC W7; FOC W12
Bridge for: U5.13 (discrete log and DDH), U5.14 (RSA, Rabin, ElGamal), U5.15 (curve point counting), U5.17 onward. Continues U5.2 (Euclid and inverses) and U5.5 (groups).
- **Topics:** Fermat's little theorem; the Euler phi-function and its multiplicativity; Euler's theorem; the Chinese remainder theorem and its use as an isomorphism Z_{mn} ≅ Z_m × Z_n; primitive roots and the structure of Z_p^* (cyclic, φ(p − 1) generators); quadratic residues, Euler's criterion; the Legendre symbol and the Jacobi symbol, quadratic reciprocity and the fast Jacobi algorithm; square roots modulo p (direct for p ≡ 3 mod 4, Tonelli–Shanks in general) and modulo pq; primality testing (the source writes "Primarily Testing", meaning primality testing): trial division, the Fermat test and Carmichael numbers, Solovay–Strassen, Miller–Rabin with its one-quarter error bound, the AKS result (stated), the prime number theorem and the density of primes for key generation; factoring algorithms: trial division, Pollard rho, Pollard p − 1, the quadratic sieve idea, the number field sieve (stated with its sub-exponential cost).
- **Results:** Fermat's little theorem and Euler's theorem [P]; CRT [P]; Euler's criterion [P]; Legendre multiplicativity [P]; quadratic reciprocity [X, proof beyond course scope]; for composite n at most a quarter of the bases in Z_n^* are Miller–Rabin non-witnesses [P, in the form: at most 1/2 by the subgroup argument, with 1/4 stated]; a Carmichael number passes the Fermat test for all coprime bases and 561 is the smallest [D]; if n = pq and the four square roots of a mod n are known then n factors [P].
- **Build:** CRT solver, Tonelli–Shanks, Jacobi symbol, Fermat, Solovay–Strassen and Miller–Rabin tests with a measured error rate on Carmichael numbers, Pollard rho and p − 1 factoring, a random prime and safe-prime generator with timing, all checked against `sympy` or `pow`. [local]
- **Gap-fills:** *[inferred: Stinson Ch.5; Niven–Zuckerman–Montgomery, recalled, not checked]* Lucas–Lehmer and Baillie–PSW testing, Gauss's lemma for the Legendre symbol.

**Assignment A5.12** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What is the error probability bound of one round of Miller-Rabin on a composite number?

(A) At most 1/2  
(B) At most 1/4  
(C) At most 1/8  
(D) Exactly 0

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Euler's criterion decides whether a number is a quadratic residue modulo an odd prime  
(B) 561 is a Carmichael number  
(C) The Fermat test never errs on composites  
(D) If n is a product of two odd primes then a quadratic residue coprime to n has four square roots modulo n

**Q3 (2 marks, numerical answer (rounds)).** How many Miller-Rabin rounds are sufficient to push the error below 2 to the minus 80 when each round errs with probability at most 1/4?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that if n = p q and two square roots x and y of the same number modulo n satisfy x not congruent to plus or minus y, then gcd(x - y, n) is a non-trivial factor of n.

**Q5 (3 marks, programming).** Implement the Chinese remainder theorem, Tonelli-Shanks, the Jacobi symbol, the Fermat, Solovay-Strassen and Miller-Rabin tests, and Pollard rho and p minus 1 factoring. Measure error rates on Carmichael numbers and check against sympy.

<details><summary>Key for A5.12 (open only after your attempt)</summary>

- **Q1:** B. At most one quarter of the bases are non-witnesses for an odd composite.
- **Q2:** A, B, D. Carmichael numbers pass the Fermat test for every coprime base.
- **Q3:** 40 rounds (tolerance ±0). Each round gives a factor of 2^-2, so 40 rounds give 2^-80.
- **Q4 (marking outline):** The squares agree so n divides x squared minus y squared, which equals (x - y)(x + y); n does not divide x - y or x + y individually because of the assumption; so the prime p divides one factor and q the other, and gcd(x - y, n) equals p or q.
- **Q5 (what a passing submission shows):** Tests agreeing with the library, a table showing Fermat failing on Carmichael numbers while Miller-Rabin does not, and factoring routines that split semiprimes of at least 60 bits.

</details>

### U5.13 Key exchange, cyclic groups and the Diffie–Hellman family: discrete log, CDH, DDH and the attacks on them
**Sources:** CNS W5; TPMC W7,12; FOC W8–9
- **Topics:** Introduction to public-key cryptosystems and the key-exchange problem; one-way trapdoor functions and cyclic groups; Diffie–Hellman key exchange in Z_p^*, the man-in-the-middle failure and authenticated variants (station-to-station); key management and exchange protocols at the level of agreement (certificates and PKI are in U5.18); the Discrete-Logarithm Problem (DLP), the Computational Diffie–Hellman problem (CDH) and the Decisional Diffie–Hellman problem (DDH) and the implications between them; generic algorithms (baby-step giant-step, Pollard rho for logarithms, Pohlig–Hellman and why group order must have a large prime factor); index calculus (outline) and why Z_p^* needs larger parameters than elliptic curves; safe primes, subgroup-confinement and small-subgroup attacks, the Logjam downgrade (read from the primary paper).
- **Results:** Baby-step giant-step finds a logarithm in O(√n) time and space [P]; Pohlig–Hellman reduces the logarithm in a group of smooth order to prime-order subgroups [P]; DDH is false in Z_p^* (the Legendre symbol of g^{ab} leaks) but plausible in a prime-order subgroup [P]; DH key exchange is secure against a passive eavesdropper under CDH, with key indistinguishability under DDH [P]; unauthenticated DH is broken by an active man in the middle [D].
- **Build:** DH over a toy and a 512-bit group; BSGS, Pollard rho and Pohlig–Hellman logarithms against measured group sizes; a DDH distinguisher in Z_p^* by the Legendre symbol with its advantage measured; a small-subgroup key-recovery against your own sloppy DH implementation; an active MITM on your own loopback exchange. [local; learning only]
- **Gap-fills:** *[inferred: Boneh–Shoup Ch.10; Katz–Lindell Ch.9, recalled, not checked]* generic-group lower bound (Shoup) as the sense in which √n is optimal.

**Assignment A5.13** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What is the time and space cost of the baby-step giant-step algorithm in a group of order n?

(A) O(n)  
(B) O(square root of n)  
(C) O(log n)  
(D) O(n squared)

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) The decisional Diffie-Hellman problem is easy in Z_p^* when the full group is used  
(B) Unauthenticated Diffie-Hellman is open to a man in the middle  
(C) Pohlig-Hellman is effective when the group order has only small prime factors  
(D) Diffie-Hellman key exchange needs no assumption at all

**Q3 (2 marks, numerical answer (steps)).** A baby-step giant-step search in a group of order 2^40 uses about the square root of the group order baby steps. How many?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that DDH is false in the full group Z_p^* by building a distinguisher that uses the Legendre symbol.

**Q5 (3 marks, programming).** Implement Diffie-Hellman over a toy and a 512-bit group, baby-step giant-step, Pollard rho and Pohlig-Hellman, a Legendre-symbol DDH distinguisher, a small-subgroup attack on your own sloppy implementation and a loopback man in the middle. For learning only.

<details><summary>Key for A5.13 (open only after your attempt)</summary>

- **Q1:** B. It stores about sqrt(n) baby steps and takes about sqrt(n) giant steps.
- **Q2:** A, B, C. Security of the exchange rests on computational Diffie-Hellman.
- **Q3:** 1048576 steps (tolerance ±0). The square root of 2^40 is 2^20 = 1,048,576.
- **Q4 (marking outline):** The Legendre symbol of g^x is determined by the parity of x for a generator g, so the symbols of g^a and g^b give the parities of a and b; the parity of ab is then known and so is the symbol of g^{ab}; a random third element matches this prediction only half the time, so the distinguisher has advantage one half.
- **Q5 (what a passing submission shows):** Logarithms recovered in toy groups with measured costs against the square-root prediction, a DDH distinguisher with advantage about one half, and an active attack that is stopped by authentication.

</details>

### U5.14 Public-key encryption I: RSA, Rabin and ElGamal, generalized ElGamal and their textbook attacks
**Sources:** CNS W5–7; TPMC W6–7; FOC W10
- **Topics:** Public Key Cryptography, trapdoor permutations and the RSA assumption; the RSA Cryptosystem: key generation, correctness by Euler's theorem and CRT, CRT-RSA decryption speed-up; textbook RSA attacks (small e and message, common modulus, Håstad broadcast, Wiener's small-d attack, multiplicative malleability, fault attacks on CRT-RSA); the Rabin Cryptosystem (the course lists "Rabinson", meaning Rabin) and its factoring equivalence and four-root ambiguity; the ElGamal Cryptosystem (the source also writes "El Gamal Encryption Scheme") in Z_p^* and its multiplicative homomorphism; Generalized ElGamal over any cyclic group, including an elliptic-curve group (curve arithmetic in U5.15); comparison of costs and key sizes.
- **Results:** RSA correctness: (m^e)^d ≡ m mod n including when gcd(m, n) ≠ 1 [P]; recovering d from (n, e) is equivalent to factoring n in the probabilistic sense [S]; breaking Rabin decryption is equivalent to factoring [P]; ElGamal decryption is correct and the scheme is IND-CPA under DDH [P, the latter in U5.16]; Håstad's broadcast attack succeeds with e ciphertexts of the same message under e different moduli [P]; Wiener's attack succeeds when d < n^{1/4}/3 [X, proof via continued fractions beyond course scope].
- **Build:** textbook RSA on the toy numbers p = 61, q = 53, e = 17, d = 2753 and then on a 1024-bit key; CRT-RSA with a simulated fault that exposes p; Rabin encryption with disambiguation by redundancy; ElGamal over Z_p and over the U5.15 curve; the common-modulus, Håstad and Wiener attacks against your own keys. [local; learning only]
- **Gap-fills:** *[inferred: Stinson Ch.5–6; Katz–Lindell Ch.11, recalled, not checked]* Coppersmith's small-root method (stated), the ROCA key-generation flaw as a case study.

**Assignment A5.14** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** With p = 61, q = 53 and e = 17 for textbook RSA, which private exponent is correct?

(A) 2753  
(B) 1023  
(C) 17  
(D) 3233

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Hastad's broadcast attack works when the same message is sent to e recipients with e different moduli  
(B) Textbook RSA is multiplicatively malleable  
(C) Breaking Rabin decryption is as hard as factoring  
(D) RSA decryption works only if the message is coprime to the modulus

**Q3 (2 marks, numerical answer).** With n = 3233, e = 17 and d = 2753, what plaintext does the ciphertext 2790 decrypt to?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that RSA decryption is correct: for n = p q, e d congruent to 1 modulo phi(n), every message m satisfies m to the e d congruent to m modulo n, including when m is divisible by p or q.

**Q5 (3 marks, programming).** Implement textbook RSA on the toy numbers and on 1024-bit keys, Rabin encryption with disambiguation, ElGamal, and the common-modulus, Hastad and Wiener attacks against your own keys. For learning only.

<details><summary>Key for A5.14 (open only after your attempt)</summary>

- **Q1:** A. d is the inverse of 17 modulo phi(n) = 3120 and equals 2753.
- **Q2:** A, B, C. RSA decryption is correct for every message modulo n, including non-coprime ones.
- **Q3:** 65 (tolerance ±0). Modular exponentiation of 2790 to the power 2753 modulo 3233 gives 65.
- **Q4 (marking outline):** Show it modulo p and modulo q separately and combine by the Chinese remainder theorem; if p does not divide m use Fermat's little theorem with e d = 1 plus k (p minus 1); if p divides m both sides are zero modulo p; the same holds for q; so equality holds modulo n.
- **Q5 (what a passing submission shows):** Toy values reproduced, correct encryption round trips, attacks recovering plaintext or key in the vulnerable settings, and refusals when the conditions fail.

</details>

### U5.15 Elliptic curves: groups over the reals and finite fields, scalar multiplication, ECDH and the elliptic-curve discrete log
**Sources:** CNS W6; TPMC W8; FOC W9
- **Topics:** Elliptic curve over the reals: Weierstrass form, discriminant, the chord-and-tangent law and the point at infinity; elliptic curve modulo a prime: the group E(F_p), counting points and the Hasse interval, curve order and cofactor; Elliptic-Curve Cryptography and elliptic-curve based public-key encryption: scalar multiplication by double-and-add and the Montgomery ladder, affine versus projective and Jacobian coordinates, point compression; ECDH; ECIES; standard curves (NIST P-256, secp256k1, Curve25519 and Edwards curves); the ECDLP and why no sub-exponential attack is known for generic curves, MOV/anomalous-curve exceptions and invalid-curve attacks.
- **Results:** Chord-and-tangent defines an abelian group [S: closure and inverses shown, associativity verified by computation and stated in general, X]; |E(F_p)| lies in [p + 1 − 2√p, p + 1 + 2√p] [X, Hasse]; double-and-add computes kP in O(log k) group operations and the ladder does so with a regular operation pattern [P]; Pollard rho on a group of prime order n costs O(√n) [S]; an invalid-curve point of small order leaks the key bits modulo that order [D].
- **Build:** affine and Jacobian curve arithmetic over F_p, a Montgomery ladder, ECDH over secp256k1 with 2G checked against the `cryptography` library, X25519 checked on its RFC 7748 vector, a naive point-counting routine for toy primes tested against the Hasse interval, and an invalid-curve attack on a deliberately unchecked toy ECDH server on loopback. [local; learning only]
- **Gap-fills:** *[inferred: Washington, Elliptic Curves; Hankerson–Menezes–Vanstone, recalled, not checked]* Schoof's point-counting algorithm (stated), Edwards-curve complete addition formulas.

**Assignment A5.15** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Hasse's theorem places the number of points on an elliptic curve over F_p within which interval?

(A) [p - 1, p + 1]  
(B) [p + 1 - 2 sqrt p, p + 1 + 2 sqrt p]  
(C) [0, 2p]  
(D) [p, 2p]

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Double-and-add computes kP with O(log k) group operations  
(B) The Montgomery ladder has a regular operation pattern  
(C) An invalid-curve point of small order can leak key bits modulo that order  
(D) Pollard rho on a curve group of prime order n costs about n steps

**Q3 (2 marks, numerical answer (points)).** What is the largest possible number of points on an elliptic curve over F_101 according to Hasse's bound?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that the double-and-add method computes kP using at most 2 times floor(log2 k) group operations.

**Q5 (3 marks, programming).** Implement affine and Jacobian arithmetic on secp256k1, a Montgomery ladder, ECDH, and X25519, check 2G and the RFC 7748 vector against the cryptography library, and write an invalid-curve attack against your own unchecked toy server on loopback. For learning only.

<details><summary>Key for A5.15 (open only after your attempt)</summary>

- **Q1:** B. The deviation from p plus 1 is at most twice the square root of p.
- **Q2:** A, B, C. Pollard rho costs about the square root of n.
- **Q3:** 122 points (tolerance ±0). 2 sqrt 101 is about 20.1, so the bound is 102 plus 20.1, floor 122.
- **Q4 (marking outline):** Process the bits of k from the most significant: one doubling per remaining bit, which is floor(log2 k) doublings, and at most one addition per bit after the first, which is at most floor(log2 k) additions; total at most twice that.
- **Q5 (what a passing submission shows):** Points and shared secrets equal to the library, X25519 matching the RFC vector, and an attack that fails once point validation is added.

</details>

### U5.16 Public-key encryption II: IND-CPA and IND-CCA security, the KEM–DEM paradigm and CCA-secure hybrid ciphers
**Sources:** FOC W9–11; TPMC W6
- **Topics:** Security games for public-key encryption (IND-CPA, IND-CCA); why deterministic encryption cannot be CPA-secure; textbook RSA and ElGamal in those games; CCA-security in the public-key domain; the KEM–DEM paradigm (hybrid encryption: a key-encapsulation mechanism plus a symmetric DEM); CCA-secure public-key hybrid ciphers based on Diffie–Hellman problems (DHIES, Cramer–Shoup idea) and on the RSA assumption (RSA-KEM and RSA-OAEP idea); padding-oracle attacks on RSA PKCS#1 v1.5 (Bleichenbacher) as the motivating failure, studied against your own toy lab server.
- **Results:** Any deterministic public-key scheme is not IND-CPA [P]; ElGamal is IND-CPA iff DDH holds in the group [P]; textbook ElGamal is malleable and hence not IND-CCA [D]; if a KEM is CCA-secure and the DEM is one-time authenticated then the hybrid is IND-CCA [P]; Bleichenbacher's oracle recovers a plaintext in about 10^4 to 10^6 queries on 1024-bit keys [recalled, not checked].
- **Build:** the U5.8 game harness for IND-CPA and IND-CCA with textbook RSA and ElGamal losing, an ElGamal-based KEM plus AES-GCM DEM from your own parts, and an RSA-KEM; a Bleichenbacher oracle attack on a toy 128-bit RSA server with PKCS#1 v1.5 padding on loopback, then the constant-time fix. [local; learning only]
- **Gap-fills:** *[inferred: Boneh–Shoup Ch.11–12; Shoup, ISO 18033-2, recalled, not checked]* OAEP's plaintext awareness (stated).

**Assignment A5.16** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Why can a deterministic public-key encryption scheme not be IND-CPA secure?

(A) The adversary can encrypt guesses itself and compare with the challenge  
(B) The keys are too short  
(C) It uses a hash  
(D) It has no decryption

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Textbook ElGamal is malleable  
(B) A KEM-DEM hybrid is IND-CCA if the KEM is CCA-secure and the DEM one-time authenticated  
(C) Textbook RSA is IND-CPA secure  
(D) ElGamal is IND-CPA secure exactly when DDH holds in the group

**Q3 (2 marks, numerical answer (bytes)).** A hybrid scheme sends a 33-byte compressed curve point, a 12-byte nonce and a 16-byte authentication tag in addition to the encrypted data. What is the overhead in bytes?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that any deterministic public-key encryption scheme is not IND-CPA secure.

**Q5 (3 marks, programming).** Using your game harness, show textbook RSA and ElGamal losing the IND-CPA and IND-CCA games, build an ElGamal-based KEM with an AES-GCM DEM from your own parts, and run a Bleichenbacher-style padding-oracle attack on a toy server on loopback followed by the constant-time fix. For learning only.

<details><summary>Key for A5.16 (open only after your attempt)</summary>

- **Q1:** A. With the public key the adversary encrypts both candidate messages and compares with the challenge ciphertext.
- **Q2:** A, B, D. Textbook RSA is deterministic and so not IND-CPA.
- **Q3:** 61 bytes (tolerance ±0). The overhead is 61 bytes.
- **Q4 (marking outline):** The adversary picks two distinct messages, asks for the encryption of one of them, then encrypts both itself with the public key; because encryption is deterministic exactly one result equals the challenge; the adversary wins with probability one.
- **Q5 (what a passing submission shows):** Games with advantage near one for the broken schemes, a hybrid scheme that resists the attacks, and an oracle attack that works on the toy server and fails after the fix.

</details>

### U5.17 Digital signatures: RSA signatures, Schnorr, DSA and ECDSA, group and ring signatures, hash-based signatures
**Sources:** CNS W8–9; TPMC W8–9; FOC W11–12; EH W7
- **Topics:** Digital signature: syntax and the existential-unforgeability game (EUF-CMA); forgeries on textbook RSA signatures and the hash-and-sign remedy (full-domain hash, PSS idea); RSA signatures; the Schnorr Identification Scheme (the interactive protocol itself is proved in U5.24) and Schnorr Signature by Fiat–Shamir; Digital Signature Standard (DSS): the DSA algorithm, ECDSA over the U5.15 curves, the role of the per-signature nonce, and EdDSA/Ed25519 with deterministic nonces; digital signatures in the TPMC Week 9 sense: group signature (anonymity within a group, traceable by a manager) and ring signature (ad hoc anonymity, no manager); one-time signatures from one-way functions (Lamport) and Merkle trees to many-time signatures, as a bridge to U5.25.
- **Results:** Textbook RSA signatures are existentially forgeable and multiplicatively homomorphic [D]; DSA verification is correct [P]; two DSA or ECDSA signatures with the same nonce reveal the private key [D]; a biased nonce with a few leaked bits breaks ECDSA through a lattice (stated) [X]; Lamport signatures are one-time unforgeable if the hash is one-way [P]; Schnorr signatures are secure in the random-oracle model under DLP [S].
- **Build:** RSA hash-and-sign with the textbook forgery against the unhashed version; Schnorr, DSA and ECDSA from scratch checked against `cryptography`; the repeated-nonce key recovery on your own toy ECDSA keys; a Lamport signer and a Merkle signature scheme; a Schnorr-style ring signature for three members. [local; learning only]
- **Gap-fills:** *[inferred: Katz–Lindell Ch.12; Boneh–Shoup Ch.13–14, recalled, not checked]* blind signatures, BLS aggregation (needs pairings from U5.22).

**Assignment A5.17** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What happens if the same nonce is used for two different DSA or ECDSA signatures with the same key?

(A) Nothing  
(B) The private key can be recovered  
(C) The signatures become longer  
(D) The public key changes

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Textbook RSA signatures are existentially forgeable  
(B) Lamport signatures are one-time signatures from a one-way function  
(C) A Schnorr signature is obtained from the identification protocol by the Fiat-Shamir transform  
(D) Ring signatures require a trusted group manager

**Q3 (2 marks, numerical answer (bytes)).** A Lamport signature for a 256-bit hash reveals one of two 32-byte secrets per bit. How many bytes long is the signature?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that two ECDSA signatures with the same nonce k on messages with hashes h1 and h2 reveal k and the private key d.

**Q5 (3 marks, programming).** Implement hash-and-sign RSA with the textbook forgery against the unhashed version, Schnorr, DSA and ECDSA checked against the cryptography library, the repeated-nonce key recovery on your own toy keys, a Lamport signer, a Merkle signature scheme and a ring signature for three members. For learning only.

<details><summary>Key for A5.17 (open only after your attempt)</summary>

- **Q1:** B. Subtracting the two signature equations gives the nonce and then the private key.
- **Q2:** A, B, C. Group signatures have a manager; ring signatures do not.
- **Q3:** 8192 bytes (tolerance ±0). The signature has 256 revealed values of 32 bytes each, 8192 bytes.
- **Q4 (marking outline):** The signatures share r and satisfy s1 = (h1 + r d)/k and s2 = (h2 + r d)/k modulo the group order; subtract to get s1 minus s2 = (h1 - h2)/k so k = (h1 - h2)/(s1 - s2); then d = (s1 k - h1)/r.
- **Q5 (what a passing submission shows):** Signatures verified by the library, a key recovered from two reused-nonce signatures, a Lamport and a Merkle scheme that verify, and a ring signature that hides which member signed.

</details>

### U5.18 Key management, certificates and PKI, TLS/SSL and PGP: the protocols that assemble the primitives
**Sources:** CNS W8,12; TPMC W7,12; FOC W12; CSP W8; EH W7
- **Topics:** Key management and key exchange at the system level: symmetric key distribution with a key-distribution centre (Needham–Schroeder, Kerberos-style tickets), key hierarchies, key derivation (HKDF, PBKDF2, scrypt, Argon2), key rotation and destruction; public-key infrastructure: X.509 certificates, certificate authorities and chains, revocation (CRL, OCSP) and Certificate Transparency; the web of trust and Pretty Good Privacy (PGP); an overview of TLS/SSL (the Secure Sockets Layer and its successors): the record layer, the TLS 1.2 handshake, the TLS 1.3 handshake with forward secrecy and key schedule, downgrade and renegotiation attacks (POODLE, BEAST, Heartbleed read as case studies, not reproduced); cryptography as one of the security controls in the privacy and security course (CSP Week 8, cryptographic protection of data at rest and in transit); where cloud services apply it (customer-managed keys in U10.7 and U7.7).
- **Results:** Forward secrecy holds when session keys come from ephemeral DH and the long-term key only signs [P]; the Needham–Schroeder symmetric protocol is open to replay of an old ticket [D]; an X.509 chain is valid iff each certificate verifies under its parent up to a trusted root and none is expired or revoked [Def]; HKDF extract-then-expand is a PRF-based KDF under standard assumptions [X].
- **Build:** HKDF from scratch against RFC 5869 and a library; a private root and intermediate CA with `cryptography`, issuing and verifying certificates in the lab only; a TLS-like handshake (ephemeral ECDH, signature, HKDF, AEAD records) between two loopback processes using your own primitives from U5.4 to U5.17, labelled learning only and not deployed; `openssl s_client` against your own local server to read a real handshake. [local; learning only]
- **Gap-fills:** *[inferred: Rescorla, SSL and TLS; RFC 8446, recalled, not checked]* TLS 1.3 0-RTT replay risk, encrypted client hello.

**Assignment A5.18** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Which property do ephemeral Diffie-Hellman keys in a handshake give?

(A) Faster hashing  
(B) Forward secrecy  
(C) Smaller certificates  
(D) Compression

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) An X.509 chain is valid if each certificate verifies under its parent up to a trusted root and none is expired or revoked  
(B) Certificate Transparency logs certificates publicly  
(C) PGP uses a web of trust  
(D) The TLS 1.3 handshake relies on RSA key transport

**Q3 (2 marks, numerical answer (bytes)).** HKDF-Expand with SHA-256 can output at most 255 times the hash length in bytes. What is that maximum in bytes?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that a protocol with ephemeral Diffie-Hellman keys deleted after use gives forward secrecy against an adversary who later learns the long-term signing keys.

**Q5 (3 marks, programming).** Implement HKDF checked against RFC 5869 vectors, create a private root and intermediate certificate authority with the cryptography library in the lab, and build a TLS-like handshake between two loopback processes from your own primitives. For learning only and never deployed.

<details><summary>Key for A5.18 (open only after your attempt)</summary>

- **Q1:** B. Past session keys stay safe even if the long-term signing key is later compromised.
- **Q2:** A, B, C. TLS 1.3 removed static RSA key transport.
- **Q3:** 8160 bytes (tolerance ±0). The limit is 255 times 32 = 8160 bytes.
- **Q4 (marking outline):** Session keys are derived only from the ephemeral shared secret; the long-term key signs but is not used to derive keys; the adversary who records the traffic and later holds the long-term key still lacks the deleted ephemeral exponents, so computing the key needs solving a Diffie-Hellman problem.
- **Q5 (what a passing submission shows):** HKDF equal to the RFC vectors, a certificate chain that verifies, a handshake with ephemeral keys and authenticated records that rejects tampering and replay, and an explicit note that it is not for deployment.

</details>

### U5.19 Cryptanalysis I: attack models, time–memory trade-off, differential and linear cryptanalysis
**Sources:** CNS W10; TPMC W10
- **Topics:** Cryptanalysis as a discipline (the aim, in the source's words, is to understand past attacks in order to prevent future ones); attack models and cost metrics (time, memory, data); Time–Memory Trade-off attack: Hellman tables, chains and merges, the T·M² = N² trade-off, rainbow tables and why salting defeats them; Differential cryptanalysis: difference distribution tables, differential characteristics and their probabilities, key recovery on a few last rounds of a toy SPN, the same idea against reduced-round DES; Linear cryptanalysis: linear approximation tables, Matsui's piling-up lemma, linear trails, bias and the data requirement; design criteria these attacks motivated (S-box choice, branch number, round count); advanced cryptanalysis (TPMC) pointers: integral and related-key attacks (stated).
- **Results:** Piling-up lemma: for independent approximations with biases ε_i the combined bias is 2^{k−1}·∏ε_i [P]; a differential attack on a characteristic with probability p needs about c/p chosen pairs [D]; Hellman's method with m tables of t chains of length t covers a fraction of the space of about m·t²/N and succeeds with high probability when m = t = N^{1/3} [D, heuristic with the merge correction stated]; the DES key recovery by linear cryptanalysis needs about 2^{43} known plaintexts [recalled, not checked].
- **Build:** the difference distribution table and linear approximation table of the AES S-box and of a 4-bit toy S-box; a full differential and a full linear key-recovery attack on a 4-round toy SPN of your own, with measured data complexity against the predicted; a Hellman table and a rainbow table for a toy 24-bit function, with success rate measured. [local; learning only]
- **Gap-fills:** *[inferred: Heys, A tutorial on linear and differential cryptanalysis; Stinson Ch.3–4, recalled, not checked]* Matsui's 1993 DES attack (read from the primary paper), boomerang attack (stated).

**Assignment A5.19** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What does the piling-up lemma compute?

(A) The bias of the XOR of independent biased bits  
(B) The key length of a cipher  
(C) The period of an LFSR  
(D) The size of a rainbow table

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Salting defeats precomputed rainbow tables  
(B) A difference distribution table records output differences for each input difference of an S-box  
(C) Hellman's trade-off with m tables of t chains of length t works best near m = t = N to the one third  
(D) Differential cryptanalysis works with known plaintexts only and needs no chosen pairs

**Q3 (2 marks, numerical answer).** Two independent linear approximations have biases 0.1 and 0.2. What is the bias of their combination by the piling-up lemma?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove the piling-up lemma for two independent binary variables with P(X = 0) = 1/2 + e1 and P(Y = 0) = 1/2 + e2: the XOR has P(X xor Y = 0) = 1/2 + 2 e1 e2.

**Q5 (3 marks, programming).** Compute the difference distribution table and linear approximation table of the AES S-box and a 4-bit toy S-box, and mount a differential attack and a linear attack on a 4-round toy SPN of your own, comparing measured data complexity with the prediction. For learning only.

<details><summary>Key for A5.19 (open only after your attempt)</summary>

- **Q1:** A. For independent approximations the biases multiply, with a factor of 2 to the k minus 1 for k terms.
- **Q2:** A, B, C. Differential attacks use chosen plaintext pairs with a chosen difference.
- **Q3:** 0.04 (tolerance ±0.0001). The combined bias is 2 times 0.1 times 0.2 = 0.04.
- **Q4 (marking outline):** X xor Y equals zero when both are zero or both one; the probability is (1/2 + e1)(1/2 + e2) + (1/2 - e1)(1/2 - e2) = 1/2 + 2 e1 e2 after expanding and cancelling the cross terms.
- **Q5 (what a passing submission shows):** Tables matching the known maximum entries for the AES S-box, last-round key bits recovered by both attacks, and data counts close to the predicted values.

</details>

### U5.20 Cryptanalysis II: attacks on stream ciphers and side-channel attacks
**Sources:** CNS W11–12; TPMC W10,12; EH W10
- **Topics:** Cryptanalysis on stream cipher: correlation attacks on combiner generators (Siegenthaler), fast correlation attacks, algebraic attacks, Berlekamp–Massey linear-complexity attack (continuing U5.6), the RC4 key-scheduling bias and its break of WEP (Fluhrer–Mantin–Shamir) and the modern stream ciphers' design response (Salsa/ChaCha, eSTREAM); side-channel attack: the leakage model (timing, cache, power, electromagnetic, acoustic, fault), simple and differential power analysis, correlation power analysis, timing attack on square-and-multiply and the cache-timing exposure of table-based AES, fault attacks (the CRT-RSA fault of U5.14), countermeasures (constant-time code, blinding, masking, shuffling, redundancy). Hardware-level side channels, physical unclonable functions and trojans are continued in U6.9 (the source writes "physical inclinable functions"; this is the PUF topic).
- **Results:** A combiner whose output correlates with one LFSR with probability 1/2 + ε is broken by exhaustive search over that LFSR alone in about 2^{L}·ε^{-2} work [D]; the Geffe generator has correlation 3/4 with two of its three registers [D]; in a Hamming-weight leakage model with Gaussian noise the correlation between a key-guess prediction and the traces is maximised at the true key and the traces needed grow like σ²/ρ² [D]; message blinding removes the dependence of the timing leak on the ciphertext [P].
- **Build:** a correlation attack on a Geffe generator; the Fluhrer–Mantin–Shamir first-byte bias measured on RC4 samples you generate; a timing attack against a simulated square-and-multiply with synthetic noisy timings; a correlation power analysis on synthetic Hamming-weight traces of your own AES S-box output, with trace count against noise; a masked S-box and the attack failing. Simulation only: no probing of real devices. [local; learning only]
- **Gap-fills:** *[inferred: Mangard–Oswald–Popp, Power Analysis Attacks; Kocher et al., recalled, not checked]* Spectre-class microarchitectural leakage (conceptual, read from the primary papers).

**Assignment A5.20** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** With the Geffe generator, with what probability does the output equal the first register's output?

(A) 1/2  
(B) 3/4  
(C) 1/4  
(D) 1

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Message blinding removes the dependence of a timing leak on the ciphertext  
(B) Correlation power analysis uses the correlation between predicted leakage and measured traces  
(C) Masking splits sensitive values into random shares  
(D) Constant-time code makes power analysis impossible

**Q3 (2 marks, numerical answer).** In the Geffe generator the output copies register 1 when the selector bit is 1 and register 3 otherwise. The selector bit is 1 with probability 1/2. When the selector picks the other register the two agree with probability 1/2. What is the probability that the output equals register 1?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that the Geffe combiner output agrees with its first input register with probability 3/4 when the registers are independent uniform bit streams.

**Q5 (3 marks, programming).** Mount a correlation attack on a Geffe generator, measure the first-byte bias of RC4 on samples you generate, and run a correlation power analysis on synthetic Hamming-weight traces of an AES S-box output with a masked version. Simulation only.

<details><summary>Key for A5.20 (open only after your attempt)</summary>

- **Q1:** B. When the selector chooses the first register (probability 1/2) they agree; otherwise they agree half the time, giving 3/4.
- **Q2:** A, B, C. Constant-time code removes timing leaks but not power leakage.
- **Q3:** 0.75 (tolerance ±0.001). The probability is 1/2 plus 1/4 = 3/4.
- **Q4 (marking outline):** Condition on the selector: with probability 1/2 the output equals register 1 exactly; with probability 1/2 it equals register 3 which is independent of register 1 and agrees with probability 1/2; total 1/2 + 1/4.
- **Q5 (what a passing submission shows):** The registers recovered separately by correlation, RC4 first-byte bias observed, key byte recovered from traces with the trace count against noise, and the masked version resisting the first-order attack.

</details>

### U5.21 Secret sharing and secure multiparty computation
**Sources:** CNS W11; TPMC W11; FOC W12
- **Topics:** Shamir's secret sharing: (t, n) threshold by polynomial evaluation over a field, reconstruction by Lagrange interpolation, perfect privacy, additive sharing and its homomorphism, verifiable secret sharing (Feldman and Pedersen); secure multiparty computation (SMPC): the ideal–real simulation paradigm, semi-honest versus malicious adversaries, honest majority versus dishonest majority; oblivious transfer; Yao's garbled circuits for two parties; the GMW and BGW approaches with Beaver triples for multiplication; interactive protocols as the common abstraction (the final week of the provable-security course) and threshold cryptography (threshold signatures and decryption).
- **Results:** Any t shares of a degree-(t−1) Shamir sharing are independent of the secret, and any t reconstruct it [P]; Lagrange coefficients depend only on the evaluation points [P]; an additive-share multiplication needs interaction, and a Beaver triple makes it local plus two openings [D]; BGW is secure against t < n/2 semi-honest parties [S]; garbled-circuit security of one gate by a PRF-based double encryption [S].
- **Build:** Shamir sharing over GF(p) with a reconstruction test for every t-subset; Feldman verifiable shares; additive secure-sum for the salary-averaging problem; a garbled AND gate and a small adder circuit with 1-out-of-2 oblivious transfer from your own ElGamal; Beaver-triple multiplication across three simulated parties. [local; learning only]
- **Gap-fills:** *[inferred: Evans–Kolesnikov–Rosulek, A Pragmatic Introduction to Secure MPC; Cramer–Damgård–Nielsen, recalled, not checked]* SPDZ-style preprocessing, GMW with malicious security (stated).

**Assignment A5.21** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** How many shares are needed to reconstruct the secret in a (t, n) Shamir scheme?

(A) t - 1  
(B) t  
(C) n  
(D) 1

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Any t minus 1 shares reveal nothing about the secret  
(B) Beaver triples allow multiplication of shared values with two openings  
(C) Lagrange coefficients depend only on the evaluation points  
(D) Additive sharing needs interaction to add two shared values

**Q3 (2 marks, numerical answer).** In a (3, 5) Shamir scheme over the integers modulo 11 three shares are (1, 0), (2, 3) and (3, 3). What is the secret?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that any t minus 1 shares of a degree t minus 1 Shamir sharing are independent of the secret.

**Q5 (3 marks, programming).** Implement Shamir sharing over GF(p) with reconstruction tested on every t-subset, Feldman verifiable shares, secure summation by additive shares, a garbled AND gate with oblivious transfer from your own ElGamal, and Beaver-triple multiplication across three simulated parties. For learning only.

<details><summary>Key for A5.21 (open only after your attempt)</summary>

- **Q1:** B. A polynomial of degree t minus 1 is determined by t points.
- **Q2:** A, B, C. Addition of additively shared values is local.
- **Q3:** 5 (tolerance ±0). Lagrange interpolation at zero over the field of 11 elements gives 5.
- **Q4 (marking outline):** Fix t minus 1 share points; for each candidate secret s there is exactly one polynomial of degree at most t minus 1 passing through those shares and (0, s), because the Vandermonde system on t distinct points is invertible; the number of consistent polynomials is the same for every s, so the shares carry no information.
- **Q5 (what a passing submission shows):** All subsets reconstructing the secret and fewer failing, a verification that rejects a bad share, correct outputs for the garbled gate and the multiplication, and no party's view revealing the inputs.

</details>

### U5.22 Broadcast, identity-based, attribute-based and functional encryption; bilinear pairings
**Sources:** CNS W11, o; TPMC W11–12, o; FOC W12
- **Topics:** Broadcast encryption (BE): the naive, the complete-subtree and the subset-cover methods and the trade between header length and user storage; identity-based encryption (IBE): Shamir's problem, the Boneh–Franklin scheme and the role of the bilinear pairing; the pairing as a bilinear map e: G₁ × G₂ → G_T, the Weil and Tate pairings (stated), the BDH assumption; attribute-based encryption (ABE): key-policy and ciphertext-policy ABE, access trees realised by secret sharing in the exponent (U5.21 used inside the scheme); functional encryption (FE): the definition, inner-product FE as an instance, and the relationship IBE ⊂ ABE ⊂ FE; collusion resistance as the central design difficulty.
- **Results:** Complete-subtree broadcast revokes r users with a header of at most r·log(N/r) ciphertexts [S]; Boneh–Franklin decryption is correct by bilinearity [P]; a bilinear map implies that DDH is easy in G₁ and therefore the schemes rely on BDH instead [P]; naive combination of ABE keys from different users breaks policies unless keys are randomised per user [D].
- **Build:** a complete-subtree broadcast scheme on N = 16 users; Boneh–Franklin IBE on a deliberately insecure "pairing in the exponent" toy group (e(g^a, g^b) = g_T^{ab} computed from exponents) to test correctness only; a CP-ABE access tree with a threshold gate on the same toy; `py_ecc`'s BN128 pairing as the oracle for real bilinearity. The toy group is not secure and is never deployed. [local; learning only]
- **Gap-fills:** *[inferred: Boneh–Franklin 2001; Goyal–Pandey–Sahai–Waters 2006; Katz, Functional encryption survey, recalled, not checked]* pairing-friendly curves and their parameter ageing (read the current literature).

**Assignment A5.22** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What does a bilinear map e satisfy?

(A) e(g^a, g^b) = e(g, g)^(ab)  
(B) e(x, y) = x + y  
(C) e is injective  
(D) e(g^a, g^b) = e(g, g)^(a+b)

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Boneh-Franklin decryption is correct by bilinearity  
(B) With a symmetric pairing DDH is easy in the source group  
(C) Collusion resistance is a central difficulty in attribute-based encryption  
(D) Identity-based encryption is a generalisation of functional encryption

**Q3 (2 marks, numerical answer (ciphertexts)).** Complete-subtree broadcast revokes r users among N with a header of at most r times log2 of N over r ciphertexts. What is the bound for r = 4 and N = 1024?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that Boneh-Franklin IBE decryption recovers the message using bilinearity.

**Q5 (3 marks, programming).** Implement a complete-subtree broadcast scheme for 16 users, Boneh-Franklin IBE and a ciphertext-policy ABE access tree on a deliberately insecure pairing-in-the-exponent toy group to test correctness, and check bilinearity against py_ecc. For learning only and never deployed.

<details><summary>Key for A5.22 (open only after your attempt)</summary>

- **Q1:** A. Bilinearity moves exponents out of the arguments, which makes the Boneh-Franklin scheme work.
- **Q2:** A, B, C. Identity-based encryption is a special case of attribute-based encryption which is a special case of functional encryption.
- **Q3:** 32 ciphertexts (tolerance ±0). log2 of 256 is 8, so the bound is 32.
- **Q4 (marking outline):** The ciphertext holds U = r P and the masked message using e(Q_id, P_pub)^r where P_pub = s P; the private key is s Q_id; decryption computes e(s Q_id, U) = e(Q_id, P)^(s r) which equals e(Q_id, P_pub)^r; both sides compute the same mask.
- **Q5 (what a passing submission shows):** Revocation working for chosen subsets, IBE and ABE decrypting under the right keys and failing otherwise on the toy group, and an explicit note that the toy group is insecure.

</details>

### U5.23 Homomorphic encryption: partially, somewhat and fully homomorphic schemes
**Sources:** TPMC W12
- **Topics:** HE (homomorphic encryption): what a homomorphism of ciphertexts means; the multiplicative homomorphism of textbook RSA and ElGamal; additive homomorphism of Paillier and the decisional composite residuosity assumption; the Goldwasser–Micali XOR-homomorphic scheme; somewhat-homomorphic and leveled schemes, noise growth (additive for addition, multiplicative for multiplication) and the depth limit; Gentry's bootstrapping idea; the learning-with-errors (LWE) problem in the form needed here (the full lattice treatment is in U5.25) and the BGV, BFV and CKKS families (stated); applications (private tallies, encrypted queries) and their cost.
- **Results:** Paillier decryption is correct, using L(x) = (x − 1)/n and λ = lcm(p − 1, q − 1) [P]; E(m₁)·E(m₂) decrypts to m₁ + m₂ for Paillier [P]; in LWE-based encryption the noise adds under addition and multiplies under multiplication, so the supported depth is about log of the modulus-to-noise ratio [D]; no scheme can be both IND-CCA and homomorphic [P].
- **Build:** Paillier from scratch with an e-voting tally; ElGamal and RSA homomorphic products; a Goldwasser–Micali XOR scheme; a toy LWE-style symmetric scheme with noise tracked across additions and multiplications until decryption fails, matching the predicted depth; a library (`tenseal` or `pyfhel`, where installable) as the oracle for a real CKKS dot product. [local; learning only]
- **Gap-fills:** *[inferred: Gentry 2009; Halevi–Shoup HElib papers, recalled, not checked]* bootstrapping cost trends (read the current benchmarks).

**Assignment A5.23** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Which scheme is additively homomorphic?

(A) Textbook RSA  
(B) Textbook ElGamal  
(C) Paillier  
(D) AES

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) ElGamal is multiplicatively homomorphic  
(B) In Paillier the product of two ciphertexts decrypts to the sum of the plaintexts  
(C) In noisy lattice schemes noise grows with homomorphic operations  
(D) A scheme that is IND-CCA secure can also be homomorphic

**Q3 (2 marks, numerical answer).** With the Paillier toy parameters n = 15 and g = 16, what is the ciphertext of m = 4 using randomness r = 2, computed as g^m r^n modulo n squared?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that with g = n + 1 Paillier decryption is correct: with c = (1 + n)^m r^n modulo n squared, the function L(c^lambda mod n^2) times the inverse of lambda recovers m, where lambda = lcm(p - 1, q - 1) and L(x) = (x - 1)/n.

**Q5 (3 marks, programming).** Implement Paillier with an e-voting tally, the multiplicative homomorphisms of RSA and ElGamal, and a toy LWE-style symmetric scheme tracking noise through additions and multiplications until decryption fails, matching the predicted depth. For learning only.

<details><summary>Key for A5.23 (open only after your attempt)</summary>

- **Q1:** C. Multiplying two Paillier ciphertexts gives an encryption of the sum.
- **Q2:** A, B, C. Homomorphism implies malleability, which contradicts IND-CCA.
- **Q3:** 173 (tolerance ±0). The product of 16^4 and 2^15 modulo 225 gives the ciphertext.
- **Q4 (marking outline):** Expand (1 + n)^m = 1 + m n modulo n squared; r^(n lambda) is 1 modulo n squared by Carmichael's theorem; hence c^lambda = 1 + m lambda n modulo n squared; L gives m lambda modulo n; multiply by lambda inverse.
- **Q5 (what a passing submission shows):** A tally decrypted correctly from encrypted votes, products matching in the multiplicative schemes, and a noise experiment whose failure depth matches the predicted value.

</details>

### U5.24 Zero-knowledge proofs and interactive protocols
**Sources:** FOC W11–12; TPMC W12
- **Topics:** Interactive proofs (the final-week topic of the provable-security course): prover and verifier, completeness, soundness and the zero-knowledge property via the simulator; the Schnorr identification scheme as a sigma protocol (commit, challenge, response), honest-verifier zero knowledge and special soundness; the Fiat–Shamir transform to a non-interactive proof and its link to Schnorr signatures (U5.17); the Chaum–Pedersen equality-of-discrete-logs proof; commitment schemes (hash-based and Pedersen: hiding versus binding); zero knowledge for graph isomorphism and three-colouring (Goldreich–Micali–Wigderson) with repetition to reduce soundness error; succinct non-interactive arguments (zk-SNARK, zk-STARK) at the level of the pipeline (computation, R1CS, polynomial encoding) with the soundness argument stated; closing with a farewell reading map to Goldreich, Boneh–Shoup and Katz–Lindell for further study, as the TPMC "more advanced topics" for payments and blockchain.
- **Results:** Schnorr's protocol is complete, has special soundness (two accepting transcripts with the same commitment and different challenges reveal the witness) and is HVZK [P]; sequential repetition of a protocol with soundness error 1/2 gives error 2^{−k} [P]; Pedersen commitments are perfectly hiding and computationally binding under DLP [P]; every language in NP has a computational zero-knowledge proof given one-way functions [X, stated with the three-colouring protocol as the witness].
- **Build:** Schnorr identification with a transcript simulator and a witness extractor; its Fiat–Shamir form; Chaum–Pedersen; a Pedersen commitment; an interactive zero-knowledge proof of graph isomorphism with a simulator; a Merkle-based commitment. [local; learning only]
- **Gap-fills:** *[inferred: Goldreich, Foundations Vol. 1 Ch.4; Thaler, Proofs, Arguments, and Zero-Knowledge, recalled, not checked]* Groth16 and PLONK arithmetisations (stated), the weak Fiat–Shamir pitfall.

**Assignment A5.24** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What does special soundness of a sigma protocol allow?

(A) Extraction of the witness from two accepting transcripts with the same commitment and different challenges  
(B) Faster proofs  
(C) Shorter keys  
(D) Encryption of the witness

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Schnorr's identification protocol is honest-verifier zero-knowledge  
(B) The Fiat-Shamir transform makes a sigma protocol non-interactive in the random-oracle model  
(C) Repeating a protocol with soundness error 1/2 sequentially k times gives soundness error 2 to the minus k  
(D) Pedersen commitments are perfectly binding

**Q3 (2 marks, numerical answer).** A graph isomorphism proof with soundness error 1/2 per round is repeated 20 times. What is the soundness error?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that Schnorr's protocol has special soundness: from two accepting transcripts (a, c, z) and (a, c', z') with c different from c' one computes the discrete logarithm x of the public key y = g^x.

**Q5 (3 marks, programming).** Implement Schnorr identification with a transcript simulator and a witness extractor, its Fiat-Shamir form, Chaum-Pedersen equality of logarithms, a Pedersen commitment and a zero-knowledge proof of graph isomorphism with a simulator. For learning only.

<details><summary>Key for A5.24 (open only after your attempt)</summary>

- **Q1:** A. Two accepting transcripts with different challenges let an extractor compute the witness.
- **Q2:** A, B, C. Pedersen commitments are perfectly hiding and computationally binding.
- **Q3:** 9.537e-07 (tolerance ±1e-8). The error is 2^-20, about 9.5e-7.
- **Q4 (marking outline):** The verification equations are g^z = a y^c and g^z' = a y^c'; dividing gives g^(z - z') = y^(c - c'); so x = (z - z')/(c - c') modulo the group order, which exists because c differs from c'.
- **Q5 (what a passing submission shows):** Honest transcripts accepted, simulator transcripts indistinguishable in distribution on the checked statistics, an extractor that recovers the witness from two transcripts, and a cheating prover caught at rate about one half per round.

</details>

### U5.25 Quantum and post-quantum cryptography
**Sources:** CNS W12, o; TPMC W12, o
- **Topics:** Introduction to quantum cryptography: qubits, measurement, no-cloning and the BB84 key-distribution protocol with its eavesdropping signature, reconciliation and privacy amplification; Shor's algorithm (period finding by the quantum Fourier transform and the classical reduction from factoring, and the discrete-log analogue) and Grover's algorithm (quadratic speed-up, hence doubling symmetric key length and hash output); post-quantum cryptography: lattice problems (SVP, LWE and module-LWE), Regev encryption, ring and module structure with the number-theoretic transform, the standardised ML-KEM and ML-DSA, hash-based signatures (SLH-DSA, building on U5.17), code-based (McEliece, and the selected HQC), multivariate and isogeny families and their break history (Rainbow and SIKE fell, from the primary papers), migration strategy (hybrid key exchange, crypto-agility, "harvest now, decrypt later"). As of this curriculum's date (November 2026), NIST published FIPS 203 (ML-KEM), FIPS 204 (ML-DSA) and FIPS 205 (SLH-DSA) on 13 August 2024, selected HQC for standardisation on 11 March 2025, and lists FN-DSA (FIPS 206) as still in development on its project page, checked on the web while building this curriculum. The source course names blockchain and bitcoin in the same final week; those are taught in U9.21 where consensus is available.
- **Results:** BB84 with an intercepting attacker in the intercept-resend strategy introduces 25% error in the sifted key [D]; Shor's classical post-processing: given the order r of a mod N, with r even and a^{r/2} ≢ −1, gcd(a^{r/2} ± 1, N) is a non-trivial factor, succeeding with probability at least 1/2 over random a [P]; Grover needs about (π/4)√N queries [S]; Regev's scheme is correct when the accumulated noise is below q/4 [P]; LWE hardness from worst-case lattice problems [X].
- **Build:** a BB84 simulator with and without an eavesdropper and the 25% error measured; Shor's algorithm with a classical order-finder standing in for the quantum step (labelled so) and a small state-vector (NumPy) quantum simulator running Grover on 4 qubits and period finding for N = 15; a Regev-style LWE encryption with parameters from correctness; a polynomial-ring NTT with a toy module-LWE KEM labelled learning only; the library `liboqs-python` or the `cryptography` library's ML-KEM where available as the oracle for the standardised algorithm. [local; learning only]
- **Gap-fills:** *[inferred: Regev 2009; Peikert, A decade of lattice cryptography; NIST FIPS 203–205, checked on the web as above]* crypto-agility and inventory (links to U8.1 and U8.3).

**Assignment A5.25** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Which algorithm breaks RSA and elliptic-curve cryptography on a large quantum computer?

(A) Grover's algorithm  
(B) Shor's algorithm  
(C) Dijkstra's algorithm  
(D) Berlekamp-Massey

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) In BB84 an intercept-resend eavesdropper introduces about 25 percent errors in the sifted key  
(B) ML-KEM is specified in FIPS 203  
(C) Grover's algorithm motivates doubling symmetric key lengths  
(D) SIKE remains a recommended post-quantum standard

**Q3 (2 marks, numerical answer (queries)).** Grover's algorithm needs about pi over 4 times the square root of N queries. How many queries are needed for a search space of N = 2^40?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that an intercept-resend attacker who measures every qubit in a random basis introduces an error rate of 25 percent in the positions where Alice and Bob's bases agree.

**Q5 (3 marks, programming).** Write a BB84 simulator with and without an eavesdropper, an order-finding stand-in for Shor's quantum step with the classical post-processing, a small NumPy state-vector simulator running Grover on 4 qubits, and a Regev-style LWE encryption. For learning only.

<details><summary>Key for A5.25 (open only after your attempt)</summary>

- **Q1:** B. Shor's algorithm finds the period needed to factor integers and compute discrete logarithms.
- **Q2:** A, B, C. SIKE was broken by a classical attack in 2022.
- **Q3:** 8.235e+05 queries (tolerance ±1000). The square root of 2^40 is 2^20 and pi/4 times 1,048,576 is about 823,550.
- **Q4 (marking outline):** When the attacker's basis matches (probability 1/2) she learns the bit and resends it correctly, no error; when it differs (probability 1/2) she resends a random-basis state, so Bob in the matching basis gets the wrong bit with probability 1/2; the overall error is 1/2 times 1/2 = 1/4.
- **Q5 (what a passing submission shows):** An observed error rate near 25 percent under attack and near zero without, a factorisation of 15 and 21 by the classical post-processing, Grover finding the marked item with high probability, and an LWE scheme that decrypts correctly under the noise bound.

</details>

## D6. Ethical hacking and technical security: reconnaissance, scanning, system and network attacks, web, memory safety and hardware

Aim: the attacker's view, taught so that defenders can reason about it, in an environment you own. Every offensive technique appears in one of three forms: a model you build in Python (simulated stack, simulated switch, simulated traces), a standard tool used in an isolated host-only laboratory against machines built to be attacked, or a detector and a fix. The domain does not teach exploit authoring, malware writing, evasion, or anything to be pointed at a network you do not own (Master Rules 11). The domain follows the Ethical Hacking course and the technical halves of the two security-management courses, and uses the networks (D2, D3) and the cryptography (D5) already built. Benchmarks (recalled, not checked): Stallings, *Cryptography and Network Security*, Forouzan, *TCP/IP Protocol Suite*, Wu and Irwin, *Introduction to Computer Networks and Cybersecurity* (all named in the source); Whitman and Mattord, *Principles of Information Security* (named in the source); Anderson, *Security Engineering*; Stuttard and Pinto, *The Web Application Hacker's Handbook*; Erickson, *Hacking: The Art of Exploitation*; Sikorski and Honig, *Practical Malware Analysis*.

### U6.1 Foundations of security and ethical hacking: CIA, threats, attack trees, ethics and rules of engagement
**Sources:** CSP W1–2; EH W1, o
- **Topics:** Introduction to cyber security and from information security to cyber security (the source's first reference); confidentiality, integrity and availability (CIA) and the CIA triangle; extensions (authenticity, non-repudiation, accountability); assets, threats, vulnerabilities, exploits, attack surface, risk as a relation among them; fundamental concepts and the Target data breach as the worked case (a supplier credential, network segmentation, alerts not acted upon; read from the public case write-ups, not from memory); attacker taxonomy (script kiddies, insiders, criminals, state actors); introduction to ethical hacking: the phases of a penetration test, scoping, written authorisation and rules of engagement, responsible and coordinated disclosure; law and ethics at the level of principles (computer-misuse statutes, for India the Information Technology Act 2000 sections on unauthorised access, recalled, not checked); the laboratory protocol of this course (own machines, host-only networks, snapshots, no scanning of anything not owned); attack trees and STRIDE as threat-modelling tools. Outline map of the ethical-hacking course: starting from the basic topics of networking, network security and cryptography (D2, D5), with hands-on demonstrations that participants are encouraged to replicate, which in this curriculum happens only inside your own isolated laboratory.
- **Results:** The minimum cost of an attack tree with AND and OR nodes is computed bottom-up (sum at AND, minimum at OR) [P]; for independent success probabilities the success probability of the tree is the product at AND and one minus the product of failures at OR [D]; defence in depth multiplies the attacker's failure probabilities only when layers are independent, and independence fails for a shared credential [D].
- **Build:** an attack-tree evaluator (cost, probability, and the cheapest cut) on a tree you write for the Target case; a STRIDE worksheet generator from a data-flow description in JSON; a one-page rules-of-engagement and laboratory-protocol template that every later lab in D6 must reference. [local]
- **Gap-fills:** *[inferred: Shostack, Threat Modeling; PTES, recalled, not checked]* the five phases of the NIST SP 800-115 testing methodology.

**Assignment A6.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** In an attack tree, how is the cost of an AND node computed from its children?

(A) The minimum of the child costs  
(B) The sum of the child costs  
(C) The maximum of the child costs  
(D) The product of the child costs

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Confidentiality, integrity and availability form the classic security triad  
(B) Written authorisation and rules of engagement are required before a penetration test  
(C) Layers of defence multiply the attacker's failure probability only if they are independent  
(D) Scanning a network you do not own is acceptable if you do not exploit anything

**Q3 (2 marks, numerical answer (units)).** An attack needs two steps costing 3 and 4 units (an AND node) or, alternatively, a single step costing 9 (an OR with the first). What is the minimum cost of the attack?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that bottom-up evaluation computes the minimum attack cost of an attack tree, with sum at AND nodes and minimum at OR nodes.

**Q5 (3 marks, programming).** Write an attack-tree evaluator that computes minimum cost, success probability and the cheapest cut for a tree stored in JSON, apply it to a tree you write for the public account of the Target breach, and write a STRIDE worksheet generator for a data-flow description. Lab only.

<details><summary>Key for A6.1 (open only after your attempt)</summary>

- **Q1:** B. An AND node needs every child attack, so the costs add; an OR node needs only the cheapest child.
- **Q2:** A, B, C. Scanning networks you do not own can be unlawful; the laboratory protocol forbids it.
- **Q3:** 7 units (tolerance ±0). The AND branch costs 7 and the alternative costs 9, so the minimum is 7.
- **Q4 (marking outline):** By induction on tree height: leaves have their own cost; an OR node is satisfied by any one child, so the cheapest way is the cheapest child; an AND node needs all children, whose sub-attacks are independent subtrees, so the cheapest total is the sum of their cheapest costs.
- **Q5 (what a passing submission shows):** An evaluator with tests on hand-checked trees, a tree for the case with sources named for each node, and a worksheet generator that outputs threats per element and flow.

</details>

### U6.2 Laboratory set-up and reconnaissance: attacker and victim machines, open-source intelligence, DNS and the nmap host-discovery stage
**Sources:** EH W4
- **Topics:** Installation of attacker and victim system: hypervisors (VirtualBox, KVM), host-only and internal networks (never bridged to a real network), snapshots, a Linux attack distribution and intentionally vulnerable targets (Metasploitable, DVWA, OWASP Juice Shop) with their licences and warnings; information gathering: advanced Google search operators (dorking at the level of operator syntax on your own pages), archive.org (the Wayback Machine) for historical content, Netcraft for hosting and technology fingerprints, whois (RFC 3912) records, host, dig, dnsenum and the DNS record types (A, AAAA, MX, NS, TXT, SOA, CNAME), zone transfers, subdomain enumeration, and the NMAP tool for host discovery (ping sweep, ARP discovery on the local segment); passive versus active reconnaissance and what each leaves in logs; defensive reading of the same facts (what an organisation leaks and how to reduce it).
- **Results:** An AXFR response from a mis-configured name server reveals the entire zone, so zone transfers must be restricted to named secondaries [D]; passive reconnaissance generates no traffic at the target while active discovery produces a countable number of probes (a /24 sweep sends 254 probes) [D].
- **Build:** a DNS stub resolver from scratch over UDP (header and question encoding, name compression in the answer parser) tested against your own lab name server; a dnsenum-style subdomain enumerator limited by a hard-coded allowlist of your lab domain; an AXFR client for your own lab zone; a whois protocol client and a record parser used on domains you own or on `example.com`; the lab built and a snapshot taken. [local VM; lab only]
- **Gap-fills:** *[inferred: RFC 1035; PTES intelligence-gathering section, recalled, not checked]* certificate-transparency search as a passive source (links to U5.18).

**Assignment A6.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What does a successful DNS zone transfer (AXFR) from a mis-configured server reveal?

(A) Only the server's version  
(B) The whole set of records of the zone  
(C) Only MX records  
(D) The administrator's password

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Passive reconnaissance sends no traffic to the target  
(B) A ping sweep of a /24 network sends probes to many addresses  
(C) Reconnaissance tools may only be used on systems you own or are authorised to test  
(D) Host-only networks are a poor choice for an attack laboratory

**Q3 (2 marks, numerical answer (addresses)).** How many usable host addresses does a ping sweep of a /24 network probe?

**Q4 (2 marks, prove or derive; every step with its reason).** A DNS message parser follows compression pointers. Show that requiring every pointer to refer to an offset strictly smaller than the position where it appears guarantees that the parser terminates.

**Q5 (3 marks, programming).** Write a DNS stub resolver from scratch over UDP, with name compression handled safely, an AXFR client and a subdomain enumerator that refuses any domain outside an allowlist, and test them against a name server you run in your own lab. Lab only.

<details><summary>Key for A6.2 (open only after your attempt)</summary>

- **Q1:** B. AXFR transfers the entire zone, which should be restricted to the secondary servers.
- **Q2:** A, B, C. A host-only network keeps the lab isolated and is the recommended choice.
- **Q3:** 254 addresses (tolerance ±0). A /24 has 256 addresses minus network and broadcast, 254 probes.
- **Q4 (marking outline):** Each followed pointer strictly decreases the offset being read; offsets are non-negative integers; so a chain of pointers has bounded length and cannot loop; reading plain labels advances forward for a bounded message length.
- **Q5 (what a passing submission shows):** Queries and responses parsed correctly, a pointer-loop test message rejected, an allowlist that blocks other domains, and a lab zone enumerated and transferred.

</details>

### U6.3 Scanning and vulnerability assessment: port scanning, nmap and Nessus, CVE, CWE and CVSS, and the secure hacking environment
**Sources:** EH W5
- **Topics:** Vulnerability scanning using NMAP and Nessus: TCP connect, SYN (half-open), FIN, NULL, Xmas and UDP scans and what each reveals about the target's TCP/IP stack (connecting to U2.5 and U2.6); service and version detection, OS fingerprinting, the NMAP scripting engine; vulnerability scanners (Nessus and the open-source alternatives), authenticated versus unauthenticated scans, false positives and negatives; the identifiers CVE, CWE and CPE and the NVD; scoring: CVSS v3.1 base metrics (attack vector, complexity, privileges, user interaction, scope, confidentiality, integrity, availability) and why v4.0 exists; prioritisation beyond severity (exploit prediction, asset value, reachability); creating a secure hacking environment: isolation, tool provenance, and keeping offensive tooling off work and production networks.
- **Results:** The CVSS v3.1 base score is computed by the specification's formulas with roundup to one decimal [Def]; the vector AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H scores 9.8 [check by script]; a full-port scan of one host needs 65 535 probes per protocol and scales linearly with timing templates [D].
- **Build:** a TCP connect scanner and a SYN scanner (raw sockets or `scapy`, if available) whose first line refuses any address outside the loopback and the lab host-only range; a banner grabber; a CVSS v3.1 base-score calculator checked on published vectors (including the 9.8 example); a prioritisation function that combines score, exposure and asset value and is tested against a hand-ranked list. [local VM; lab only]
- **Gap-fills:** *[inferred: FIRST CVSS v3.1 specification; Lyon, Nmap Network Scanning, recalled, not checked]* CVSS v4.0 metric groups (read the FIRST document), SSVC as an alternative.

**Assignment A6.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Which CVSS v3.1 base score does the vector AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H have?

(A) 7.5  
(B) 8.8  
(C) 9.8  
(D) 10.0

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements about scanning are correct?

(A) A SYN scan sends a SYN and does not complete the handshake  
(B) A connect scan completes the full handshake  
(C) UDP scans are usually faster and more reliable than TCP scans  
(D) A scanner you write should refuse targets outside your lab range

**Q3 (2 marks, numerical answer).** Compute the CVSS v3.1 base score for AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H using weights 0.85, 0.77, 0.85, 0.85 and 0.56 for each of C, I and A: impact = 6.42 times the impact subscore ISS = 1 minus (1 - 0.56)^3, exploitability = 8.22 times the four weights, base = roundup of the sum to one decimal.

**Q4 (2 marks, prove or derive; every step with its reason).** Show that a full port scan of one host needs 65,535 probes per protocol and that the time scales linearly with the probe rate.

**Q5 (3 marks, programming).** Write a TCP connect scanner and a SYN scanner whose first action is to reject any address outside loopback and the lab host-only range, a banner grabber, a CVSS v3.1 calculator tested on published vectors, and a prioritisation function combining score, exposure and asset value. Lab only.

<details><summary>Key for A6.3 (open only after your attempt)</summary>

- **Q1:** C. A network-exploitable flaw with no privileges and high impact on all three properties scores 9.8.
- **Q2:** A, B, D. UDP scanning is slow because closed ports often answer with rate-limited ICMP messages.
- **Q3:** 9.8 (tolerance ±0.05). Impact is about 5.87 and exploitability about 3.89; the sum 9.76 rounds up to 9.8.
- **Q4 (marking outline):** There are 65,535 usable port numbers; one probe per port gives that count; at a rate of r probes per second the time is 65,535 divided by r, which is linear in 1/r; retransmissions multiply by a constant factor.
- **Q5 (what a passing submission shows):** A scanner that refuses outside targets in a unit test, correct ports found on your lab VM, a calculator reproducing at least ten published scores including 9.8, and a ranked list matching a hand ranking.

</details>

### U6.4 System hacking, malware and link-layer attacks: passwords, privilege escalation, malware taxonomy and analysis, ARP spoofing and MAC attacks
**Sources:** EH W5
- **Topics:** System hacking: password cracking (hash storage, salting, dictionary, mask and rule-based guessing, rainbow tables with the link to U5.19, work factors of bcrypt, scrypt and Argon2 against MD5 and SHA-1 and the unsalted-hash disaster), privilege escalation (the classes: misconfigured services, weak file permissions, set-user-ID binaries, stored credentials; demonstrated on a deliberately vulnerable lab VM and remedied), application execution and persistence at the level of detection; malware and virus: taxonomy (virus, worm, trojan, ransomware, rootkit, botnet), lifecycle, static and dynamic analysis methodology in a sandbox, signature and heuristic detection and their limits, epidemic dynamics; ARP spoofing: the ARP protocol, cache poisoning, the man-in-the-middle position and its detection and prevention (static entries, dynamic ARP inspection); MAC attack: switch CAM-table flooding (MAC flooding) and port security, DHCP snooping.
- **Results:** The expected time to exhaust a password space of N guesses at rate R is N/(2R) on average [D]; a per-user random salt makes precomputation per password impossible and forces per-target work [P]; in a random-scanning worm model the infected fraction obeys a logistic equation with rate β [D]; flooding a CAM table of capacity C needs C distinct source addresses [D].
- **Build:** a password-guessing model on hashes you generate yourself (dictionary, mask, rules) with measured guesses per second for MD5 against bcrypt, and an entropy estimator; a file-entropy and signature scanner on synthetic benign samples (no malware is written or collected); a worm-propagation simulation on a random graph against the logistic prediction; a Python model of a learning switch with a CAM table, the flooding attack on the model and a dynamic-ARP-inspection defence on the model; an ARP-anomaly detector over a capture taken in your own lab. [local VM; lab only]
- **Gap-fills:** *[inferred: Sikorski–Honig; Moore et al., Inside the Slammer Worm, recalled, not checked]* credential stuffing and password-manager defences, EICAR as the benign antivirus test file.

**Assignment A6.4** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What does a per-user random salt achieve for stored password hashes?

(A) It makes the hash shorter  
(B) It forces precomputation to be repeated for every user  
(C) It encrypts the password  
(D) It speeds up login

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) An unsalted fast hash makes mass password cracking cheap  
(B) bcrypt, scrypt and Argon2 are designed to be slow or memory-hard  
(C) Flooding a switch's address table needs as many distinct source addresses as its capacity  
(D) Dynamic ARP inspection validates ARP packets against trusted bindings

**Q3 (2 marks, numerical answer (s)).** A random 6-character password over 62 symbols is guessed at 10^10 guesses per second. What is the average time to find it, in seconds, taken as the space divided by twice the rate?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that per-user salts force an attacker to spend work proportional to the number of users, compared with a single shared precomputed table.

**Q5 (3 marks, programming).** Build a password-guessing model on hashes you generate yourself, comparing guesses per second for MD5 against bcrypt; a file-entropy and signature scanner on synthetic benign samples; a worm-propagation simulation against the logistic prediction; and a simulated learning switch with a MAC flooding attack and a defence. Lab only; no malware is written.

<details><summary>Key for A6.4 (open only after your attempt)</summary>

- **Q1:** B. The attacker cannot reuse a single precomputed table across users.
- **Q2:** A, B, C, D. All four statements are correct.
- **Q3:** 2.84 s (tolerance ±0.01). The space is 5.68e10, so the average is 2.84 s.
- **Q4 (marking outline):** Without salts one table of hashes of candidate passwords serves all users, cost independent of the number of users; with a unique salt per user each candidate must be hashed separately for each user; the work for covering a dictionary of size D is D times the number of users.
- **Q5 (what a passing submission shows):** Measured rates differing by orders of magnitude, an entropy scanner that flags packed synthetic data, a simulation that follows the logistic curve, and a switch model that fails open under flooding and is protected by port security.

</details>

### U6.5 Network attacks and defences: sniffing, session attacks, denial of service, DNS and email security
**Sources:** EH W8–9
- **Topics:** Network-based attacks: sniffing and packet capture (promiscuous mode, why a switch limits it, capture filters), packet sniffing using Wireshark (display filters, following a stream, decrypting your own TLS with a key log), TCP session hijacking and spoofing and why unpredictable sequence numbers matter; Denial of service attacks: resource exhaustion, SYN flood and SYN cookies, reflection and amplification (DNS, NTP, memcached; the amplification factor), distributed attacks and botnets, mitigation by rate limiting, anycast and scrubbing; DNS security: cache poisoning and the Kaminsky attack, source-port randomisation, DNSSEC's chain of trust (using U5.17 signatures), DNS over TLS and over HTTPS; email security: SMTP and its spoofing problem, SPF, DKIM, DMARC, phishing, S/MIME and PGP (with U5.18).
- **Results:** With a 16-bit transaction ID and k forged answers per attempt the success probability in one race is about k/65536, and adding source-port randomisation multiplies the search space by about 2^{16} [D]; a SYN-cookie encodes the connection state in the sequence number so a half-open connection costs no memory [D]; the amplification factor is response bytes over request bytes and a reflector with factor 50 turns 1 Gbit/s into 50 Gbit/s [D].
- **Build:** a pcap file reader and an Ethernet, IP, TCP and UDP dissector from scratch, applied to a capture you take in your lab; a listen-queue model of a server with and without SYN cookies under a simulated flood; the Kaminsky success-probability calculation against a Monte Carlo of the race; an SPF checker and a DKIM verifier (relaxed canonicalisation, RSA from U5.14) run on synthetic messages. [local VM; lab only]
- **Gap-fills:** *[inferred: Kaminsky 2008; RFC 7208, 6376 and 7489, recalled, not checked]* the Mirai botnet and the 2016 DNS-provider attack as the standard DDoS case (in U6.10).

**Assignment A6.5** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What makes the Kaminsky attack on a DNS resolver harder once source-port randomisation is added?

(A) The transaction ID becomes longer  
(B) The attacker must also guess the source port, enlarging the search space by about 2^16  
(C) DNS uses TCP only  
(D) Responses are encrypted

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) A SYN cookie encodes connection state in the sequence number  
(B) The amplification factor is the response size divided by the request size  
(C) Reflection attacks send requests with the victim's spoofed source address  
(D) DNSSEC encrypts DNS queries

**Q3 (2 marks, numerical answer).** A forged-answer race gives the attacker k = 100 forged responses with random 16-bit identifiers against a resolver that accepts the first match. What is the approximate success probability of one race?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that a SYN-cookie server needs no memory per half-open connection and explain how the final acknowledgement is validated.

**Q5 (3 marks, programming).** Write a pcap reader and Ethernet, IP, TCP and UDP dissector from scratch for a capture taken in your lab, a listen-queue model with and without SYN cookies under a simulated flood, the Kaminsky success calculation against a Monte Carlo race, and SPF and DKIM verifiers for synthetic messages. Lab only.

<details><summary>Key for A6.5 (open only after your attempt)</summary>

- **Q1:** B. Both the 16-bit identifier and the source port must be matched.
- **Q2:** A, B, C. DNSSEC signs records for authenticity and does not encrypt.
- **Q3:** 0.001526 (tolerance ±0.00001). The probability is about k over 65536 = 0.0015.
- **Q4 (marking outline):** The server computes the initial sequence number as a keyed hash of the connection tuple, a coarse timestamp and the client's MSS; it stores nothing; when the ACK arrives it recomputes the hash for recent timestamps and checks that the acknowledged number minus one matches, then creates the connection.
- **Q5 (what a passing submission shows):** A dissector matching tshark on the sample capture, a model in which cookies keep legitimate connections served under flood, a probability estimate agreeing with the formula, and verifiers that accept valid and reject altered messages.

</details>

### U6.6 Steganography, biometric authentication and social engineering
**Sources:** EH W8–9
- **Topics:** Steganography: carriers, least-significant-bit embedding in images and audio, capacity, the difference from watermarking and from encryption, steganalysis (chi-square and RS analysis), information-theoretic security of steganography (Cachin's relative-entropy condition, using U5.1); biometric authentication: enrolment and matching, false accept and false reject rates, the ROC curve and equal error rate, template protection and why biometrics cannot be revoked, presentation attacks (spoofing); social engineering attacks: pretexting, phishing, vishing, baiting, tailgating, and the psychological levers (authority, urgency, reciprocity); defences (multi-factor authentication, verification procedures, training) and the ethics of phishing simulations (consent, scope, no real credentials).
- **Results:** LSB replacement with a random message of n bits changes about n/2 of the carrier bits, which shifts the histogram pair-equalisation in a way the chi-square test detects [D]; FAR falls and FRR rises as the threshold rises, and the EER is the crossing point [Def]; a score-fusion of independent biometric traits reduces the error under the likelihood-ratio rule [S].
- **Build:** LSB embedding and extraction on a synthetic image array, with chi-square steganalysis and its detection rate against embedding rate; FAR, FRR and EER computed from two synthetic score distributions with an ROC plot; a Naive-Bayes message scorer for a synthetic phishing corpus you generate. No real people or real credentials are targeted. [local]
- **Gap-fills:** *[inferred: Cachin 1998; Jain–Ross–Nandakumar, Introduction to Biometrics, recalled, not checked]* fuzzy extractors for biometric key derivation (continued in U6.9).

**Assignment A6.6** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** How many carrier bits does LSB replacement of a random n-bit message change on average?

(A) n  
(B) n over 2  
(C) 2n  
(D) None

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) The equal error rate is where false accepts equal false rejects  
(B) Biometric templates are hard to revoke  
(C) The chi-square test can detect LSB replacement  
(D) Steganography and encryption are the same thing

**Q3 (2 marks, numerical answer (bits)).** A random 10,000-bit message is embedded by LSB replacement. How many carrier bits change on average?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that raising the matching threshold of a biometric system lowers the false accept rate and raises the false reject rate, and define the equal error rate.

**Q5 (3 marks, programming).** Implement LSB embedding on a synthetic image with chi-square steganalysis, compute false accept and false reject rates and the equal error rate from two synthetic score distributions with a curve, and write a Naive-Bayes scorer on a synthetic phishing corpus. No real people or credentials.

<details><summary>Key for A6.6 (open only after your attempt)</summary>

- **Q1:** B. Each carrier bit already equals the message bit half of the time, so about half change.
- **Q2:** A, B, C. Steganography hides the existence of a message; encryption hides its content.
- **Q3:** 5000 bits (tolerance ±0). About half, 5000.
- **Q4 (marking outline):** Accepting only scores above a threshold t: increasing t removes impostor scores from the accepted region so the false accept rate does not increase, and removes genuine scores so false rejects do not decrease; both are monotone and continuous for continuous scores, so they cross at a threshold, whose common rate is the equal error rate.
- **Q5 (what a passing submission shows):** Detection rates against embedding rate, an ROC curve with a computed EER, and a scorer evaluated on held-out synthetic messages.

</details>

### U6.7 Web application attacks and secure coding: HTTP state, SQL injection, XSS, CSRF, authentication and access control
**Sources:** EH W9,11
- **Topics:** Packet sniffing using Wireshark and Burp Suite as the interception-proxy workflow, and password attack using Burp Suite (brute force, credential stuffing, and the lockout and rate-limit defences); attack on web servers: password attack, SQL injection, cross site scripting; the web model (HTTP, cookies and sessions, the same-origin policy, CORS), injection and its root cause in mixing code and data, SQL injection (in-band, blind and time-based) and parameterised queries, XSS (reflected, stored and DOM-based) with output encoding and Content Security Policy, cross-site request forgery and anti-CSRF tokens and SameSite cookies, broken access control (insecure direct object references), server-side request forgery, software supply chain and exceptional-condition failures. The current OWASP Top 10 is the 2025 edition (released November 2025: broken access control first, with SSRF merged into it; security misconfiguration second; software supply-chain failures third; cryptographic failures fourth; injection fifth; insecure design sixth; mishandling of exceptional conditions tenth), read from secondary reports while building this curriculum and to be checked against the OWASP project site.
- **Results:** A query built by string concatenation lets the attacker change its parse tree, while a parameterised query fixes the parse tree before the data arrives, so injection is impossible for the parameter positions [P]; the expected number of attempts for a rate-limited online guess of a password from a space of size N at q guesses per window is N/(2q) windows [D]; a CSRF token bound to the session and checked server-side defeats cross-origin form posts [P].
- **Build:** a small vulnerable web application written in the standard library with SQLite on loopback only, an automated test harness that demonstrates SQL injection and XSS against your own application, and the fixed versions (parameterised queries, output encoder, CSRF token, token-bucket login limiter, secure cookie flags); a Burp Suite or `mitmproxy` session against your own application and DVWA in the isolated lab. [local VM; lab only]
- **Gap-fills:** *[inferred: OWASP ASVS; Stuttard–Pinto, recalled, not checked]* deserialisation flaws, template injection, API security (OWASP API list, check the current edition).

**Assignment A6.7** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Which fix removes SQL injection in the parameter positions of a query?

(A) Escaping quotes manually  
(B) Parameterised queries  
(C) Hiding error messages  
(D) Using a longer password

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Output encoding and a content security policy are defences against cross-site scripting  
(B) An anti-CSRF token bound to the session blocks cross-origin form posts  
(C) Rate limiting and lockout reduce online password guessing  
(D) Hiding the login URL removes the need for access control

**Q3 (2 marks, numerical answer (windows)).** A login allows 5 guesses per window and the secret is a 6-digit PIN with 10^6 possibilities chosen uniformly. What is the expected number of windows needed to find it, taken as the space divided by twice the guesses per window?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that a query built with parameters cannot be changed in structure by the data supplied, in contrast to concatenation.

**Q5 (3 marks, programming).** Write a small vulnerable web application with SQLite on loopback only, a test harness that demonstrates SQL injection and XSS against your own application, and the fixed versions with parameterised queries, output encoding, a CSRF token, a token-bucket login limiter and secure cookie flags. Lab only.

<details><summary>Key for A6.7 (open only after your attempt)</summary>

- **Q1:** B. A parameterised query fixes the parse tree before the data arrives.
- **Q2:** A, B, C. Obscurity is not a control.
- **Q3:** 100000 windows (tolerance ±0). The expected number is 10^6/10 = 100,000 windows.
- **Q4 (marking outline):** The query text is parsed into a tree with placeholders before any data is bound; bound values are inserted as leaf values of the tree and are never parsed as SQL; therefore their content cannot create new operators or clauses, whereas concatenation parses the data as part of the query.
- **Q5 (what a passing submission shows):** Exploits succeeding against the vulnerable version only, fixed versions passing the same tests, and a limiter whose measured guess rate matches the configuration.

</details>

### U6.8 Exploitation frameworks and memory safety: Metasploit as a lab tool, memory-corruption models, and mitigations
**Sources:** EH W11
- **Topics:** Different types of attacks using the Metasploit framework: password cracking, privilege escalation, remote code execution: the framework's architecture (exploit, payload, auxiliary and post modules), the msfconsole workflow, and Meterpreter, used only as a tool in the isolated laboratory against Metasploitable-class machines, with the corresponding patch or mitigation recorded for each finding; memory-safety bug classes (stack buffer overflow, heap overflow, use-after-free, format string, integer overflow) taught through a Python memory model of a stack frame and not through real exploits; mitigations: stack canaries, non-executable memory (DEP and NX), address-space layout randomisation, control-flow integrity, shadow stacks, bounds-checked and memory-safe languages; vulnerability lifecycle (discovery, CVE assignment, patch, disclosure). No exploit is written or adapted here.
- **Results:** An n-bit-entropy ASLR makes a blind guess succeed with probability 2^{−n} per attempt, and if the target restarts with fresh randomisation the expected attempts are 2ⁿ [D]; a canary of b random bits detects a linear overflow except with probability 2^{−b} [D]; a spatially memory-safe language removes the overflow class but not logic errors [Def].
- **Build:** a Python model of a stack frame (buffer, saved frame pointer, return address) showing a linear overwrite hijacking a simulated return, then the same program with a canary and a bounds check; an ASLR guessing simulator against the 2ⁿ prediction; a Metasploit-assisted assessment of a Metasploitable VM on a host-only network with a findings table giving the weakness, CVE and fix. [local VM; lab only]
- **Gap-fills:** *[inferred: Erickson, Hacking; the Rust ownership model, recalled, not checked]* return-oriented programming (named only), the vulnerability-disclosure norms of CERT/CC.

**Assignment A6.8** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** If address-space layout randomisation has 16 bits of entropy and the target restarts with fresh randomisation after every failed guess, what is the expected number of attempts?

(A) 16  
(B) 256  
(C) 65,536  
(D) 1

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) A stack canary detects a linear overflow with high probability  
(B) Non-executable memory prevents running injected data as code in the simplest form  
(C) A memory-safe language removes the class of spatial memory errors but not logic errors  
(D) Metasploit may be pointed at any host that looks vulnerable

**Q3 (2 marks, numerical answer (attempts)).** With 16 bits of ASLR entropy and a target that re-randomises after each failed attempt, what is the expected number of attempts to guess correctly?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that a b-bit random canary detects a linear overflow that overwrites the saved return address except with probability 2^-b.

**Q5 (3 marks, programming).** Write a Python model of a stack frame showing a linear overwrite hijacking a simulated return, then the same program with a canary and a bounds check, an ASLR guessing simulator against the 2^n prediction, and a findings table from a Metasploit-assisted assessment of a Metasploitable VM on a host-only network. Lab only; no exploit code is written.

<details><summary>Key for A6.8 (open only after your attempt)</summary>

- **Q1:** C. Each attempt succeeds with probability 2^-16, so about 2^16 attempts are expected.
- **Q2:** A, B, C. Offensive tools are used only against systems you own or are authorised to test.
- **Q3:** 65536 attempts (tolerance ±0). The geometric distribution with success probability 2^-16 has mean 2^16 = 65536.
- **Q4 (marking outline):** A linear overflow must overwrite the canary before reaching the return address; the overflow bytes are chosen without knowing the random canary; the chance that they reproduce it is 2^-b; otherwise the check at function exit fails.
- **Q5 (what a passing submission shows):** The model attack succeeding without defences and detected with them, simulated guess counts near 2^n, and a findings table with weakness, CVE and fix for each item.

</details>

### U6.9 Hardware security: side channels in hardware, physical unclonable functions and hardware trojans
**Sources:** EH W10
- **Topics:** Elements of hardware security: side-channel attacks (the leakage models of U5.20 now seen as physical effects), physical unclonable functions (the source writes "physical inclinable functions"): the arbiter PUF with its additive delay model, ring-oscillator and SRAM PUFs, the metrics uniqueness, uniformity and reliability, modelling attacks by machine learning, and key derivation by a fuzzy extractor with helper data; hardware trojans: trigger and payload, taxonomy by insertion stage, detection (logic testing, side-channel fingerprinting), supply-chain and trusted-fabrication issues; trusted platform modules, secure boot, trusted execution environments; Rowhammer and fault injection as hardware-induced faults (conceptual).
- **Results:** The response of an arbiter PUF is a linear threshold function of a parity feature vector, so logistic regression learns it from a modest number of challenge–response pairs [D]; a repetition code of length n corrects up to (n − 1)/2 flips per block and a fuzzy extractor built on it leaks at most the helper data's redundancy [S]; an ideal PUF has inter-chip Hamming distance near 50% and intra-chip distance near 0% [Def].
- **Build:** an arbiter-PUF simulator with process variation and noise, the three metrics measured, a logistic-regression modelling attack and its accuracy against the number of challenge–response pairs, and a fuzzy extractor with a repetition code; a trojan-detection test on simulated per-chip power fingerprints. Everything is simulated. [local]
- **Gap-fills:** *[inferred: Maes, Physically Unclonable Functions; Bhunia–Tehranipoor, Hardware Security, recalled, not checked]* TPM attestation, the Meltdown and Spectre class (read the primary papers).

**Assignment A6.9** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What does a physical unclonable function provide?

(A) A device-unique response derived from manufacturing variation  
(B) A faster processor  
(C) A longer key  
(D) An encrypted channel

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) An arbiter PUF's response is a linear threshold function of a parity feature vector  
(B) A modelling attack can learn an arbiter PUF from challenge-response pairs  
(C) Helper data and error correction are used to derive stable keys from noisy PUF responses  
(D) Hardware trojans are always detectable by logic testing alone

**Q3 (2 marks, numerical answer (bits)).** A repetition code of length 5 decodes by majority. How many flipped bits per block can it correct?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that a majority-vote repetition code of odd length n corrects up to (n - 1)/2 bit flips and no more in the worst case.

**Q5 (3 marks, programming).** Write an arbiter-PUF simulator with process variation and noise, measure uniqueness, uniformity and reliability, mount a logistic-regression modelling attack and plot accuracy against the number of challenge-response pairs, and implement a fuzzy extractor with a repetition code. Simulation only.

<details><summary>Key for A6.9 (open only after your attempt)</summary>

- **Q1:** A. Uncontrollable process variation makes the challenge-response behaviour unique per chip.
- **Q2:** A, B, C. Trojans may be rare-triggered and need side-channel fingerprinting as well.
- **Q3:** 2 bits (tolerance ±0). It corrects up to (n minus 1)/2 = 2 flips.
- **Q4 (marking outline):** With at most (n - 1)/2 flips the correct value still has a strict majority; with (n + 1)/2 flips the wrong value has the majority so decoding fails; so the guaranteed correction radius is exactly (n - 1)/2.
- **Q5 (what a passing submission shows):** Metrics near 50 percent for inter-chip distance, an attack reaching high accuracy with enough pairs, and a key reproduced after noise with helper data.

</details>

### U6.10 Case studies: attack scenarios, their root causes and remedies
**Sources:** EH W12
- **Topics:** Case studies: various attack scenarios and their remedies, using a fixed analytical template: timeline, adversary and goal, initial access, path through the environment, controls that failed, detection (or not), impact, remedy, and a root-cause statement; cases from public post-mortems and official reports: Heartbleed (a missing bounds check in a TLS extension, 2014), Mirai (default credentials on IoT devices and the 2016 DNS-provider outage), WannaCry (an unpatched SMB flaw, 2017), the Equifax breach (an unpatched web framework, 2017), SolarWinds (software supply chain, 2020), Log4Shell (a logging library, 2021), the Colonial Pipeline ransomware incident (2021), and the Target breach already met in U6.1; mapping each case to the kill-chain and ATT&CK vocabulary of D7 and to the controls of D8.
- **Results:** None are proved; the deliverable is a defensible root-cause chain for each case, stating which of the assumptions of U6.1 to U6.9 failed.
- **Build:** a structured case record (JSON schema) and an analyser that checks completeness of each record and computes a first-order control-failure count per case across the set, and a comparison table that links each case to a unit of D6, D7 or D8; the facts for each case are entered from the cited post-mortem, with the source named for every fact. [local]
- **Gap-fills:** *[inferred: public post-mortems; CISA advisories and the Cyber Safety Review Board reports, recalled, not checked]* dates and figures for each case are to be read from the report and not from this unit.

**Assignment A6.10** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What is the purpose of a fixed template when analysing a security incident?

(A) To make every case look the same  
(B) To make analyses comparable and to expose missing facts  
(C) To avoid reading the report  
(D) To hide the root cause

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Each fact in a case record should carry its source  
(B) A root-cause statement should name the control or assumption that failed  
(C) Dates and figures should be taken from the cited post-mortem, not from memory  
(D) A case record is complete if the timeline is missing

**Q3 (2 marks, numerical answer).** A case-record schema has 9 mandatory fields and 7 records together miss 7 fields in total. What is the completeness fraction of the whole set?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that a completeness metric defined as the fraction of mandatory fields filled across all records is between 0 and 1 and equals 1 exactly when no record has a missing field.

**Q5 (3 marks, programming).** Write a JSON schema for a case record and an analyser that checks completeness, computes the number of failed controls per case across a set, and links each case to a unit of D6, D7 or D8; fill in two cases from public post-mortems with the source named for every fact.

<details><summary>Key for A6.10 (open only after your attempt)</summary>

- **Q1:** B. A fixed template makes cases comparable and shows where facts are missing.
- **Q2:** A, B, C. Completeness includes the timeline.
- **Q3:** 0.8889 (tolerance ±0.001). There are 63 required entries and 7 are missing, so 56/63 = 0.889.
- **Q4 (marking outline):** The numerator counts filled fields and is at most the total number of mandatory fields, which is the denominator, and at least zero; equality with the denominator holds exactly when every mandatory field of every record is filled.
- **Q5 (what a passing submission shows):** A validator rejecting an incomplete record, a table across cases with sources, and a comparison that identifies the controls that recur.

</details>

## D7. Security operations frameworks and cloud security: defence technology, ATT&CK, kill chains, D3FEND, STIG, STIX/TAXII and cloud IAM

Aim: the defender's working vocabulary. Each framework is treated as a data model plus an algorithm over it (coverage as set cover, kill-chain defence as a probability product, compliance as a weighted score, intelligence as typed objects and a matching engine), so that it can be implemented, tested and then used in the capstone of U13.6. The frameworks' catalogues change on a release schedule of their own; every version named here was current in the author's reading and is to be re-checked at the time of study (recalled, not checked unless stated). Benchmarks (recalled, not checked): Whitman and Mattord, *Principles of Information Security* (the textbook of the source course); Anderson, *Security Engineering*; Bejtlich, *The Practice of Network Security Monitoring*; Strom et al., *MITRE ATT&CK: Design and Philosophy*; OASIS STIX 2.1 and TAXII 2.1 specifications.

### U7.1 Defence technologies and access control: firewalls, intrusion detection, access-control models and active defence
**Sources:** CSP W7–8
- **Topics:** Cyber security: industry perspective, defense technologies, attack, exploits (Text-Chapter 6–7, security technology): packet-filter, stateful and application-proxy firewalls and their rule semantics, network intrusion detection and prevention (signature versus anomaly detection, rule languages), virtual private networks, segmentation and the demilitarised zone, honeypots, log aggregation and security information and event management, endpoint detection; cyber security technologies: access control, encryption, standards: authentication factors and multi-factor authentication, access-control models (the access matrix with ACLs and capabilities; discretionary and mandatory control; the Bell–LaPadula and Biba lattice models; role-based and attribute-based control), the reference monitor, Kerberos-style single sign-on (continued from U5.18); the encryption chapter (Text-Chapter 8, cryptography) is taught in D5 and applied in U5.18; standards (ISO/IEC 27001 family, NIST publications, PCI DSS) are listed here and compared in U8.1; active defense and hacking back: a primer (an HBR piece in the series The end of cyber security): what is lawful, what is not, and why unauthorised counter-attack is excluded from this curriculum.
- **Results:** Bell–LaPadula basic security theorem: a system whose every transition preserves the simple-security and *-properties stays secure [P]; the base-rate fallacy: with detector true-positive rate r, false-positive rate f and attack prevalence p, P(attack | alert) = rp / (rp + f(1 − p)), which is tiny when p is small [D]; safety of a general access matrix (the HRU result) is undecidable [X]; a stateful firewall's connection table makes return traffic implicitly allowed and bounds state by the number of live flows [D].
- **Build:** a stateful firewall engine (rule list, connection tracking, timeouts) tested on synthetic packet traces; a signature IDS using Aho–Corasick multi-pattern matching (a trie with failure links, extending the tries of U3.1) with a measured alert precision against prevalence; a Bell–LaPadula reference monitor over a lattice of labels with a proof-by-test of the theorem on random transition sequences; RBAC and ABAC engines that return an allow or deny with the decision trace. [local]
- **Gap-fills:** *[inferred: Biba 1977; Sandhu et al., Role-Based Access Control Models, recalled, not checked]* zero-trust architecture (NIST SP 800-207, recalled, not checked), mandatory access control as implemented by SELinux.

**Assignment A7.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** An intrusion detector has a high true-positive rate and a low false-positive rate, but attacks are rare. Why can most of its alerts still be false?

(A) The detector is broken  
(B) The base rate of attacks is low so false alarms outnumber real ones  
(C) Alerts are encrypted  
(D) Analysts ignore them

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Bell-LaPadula prevents reading up and writing down in its basic form  
(B) A stateful firewall tracks connections so that return traffic can be allowed implicitly  
(C) Role-based access control assigns permissions to roles and roles to users  
(D) Safety of a general access matrix model is decidable in every case

**Q3 (2 marks, numerical answer).** A detector has true-positive rate 0.99 and false-positive rate 0.01, and 1 in 1000 events is an attack. What is the probability that an alert is a real attack?

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the probability that an event is an attack given an alert, in terms of the true-positive rate r, false-positive rate f and prevalence p, and show that it tends to zero as p tends to zero for fixed r and f.

**Q5 (3 marks, programming).** Implement a stateful firewall engine with a rule list and connection tracking, a signature intrusion detector using Aho-Corasick, a Bell-LaPadula reference monitor on a label lattice, and RBAC and ABAC engines returning the decision trace. Test with synthetic traces.

<details><summary>Key for A7.1 (open only after your attempt)</summary>

- **Q1:** B. Bayes' rule shows the share of true alerts depends strongly on the prevalence of attacks.
- **Q2:** A, B, C. The HRU safety problem is undecidable in general.
- **Q3:** 0.09016 (tolerance ±0.001). The numerator is 0.00099 and the denominator 0.01098, giving about 0.09.
- **Q4 (marking outline):** By Bayes: P(attack given alert) = r p over (r p + f (1 minus p)); as p goes to zero the numerator goes to zero while the denominator tends to f which is positive, so the ratio tends to zero.
- **Q5 (what a passing submission shows):** Rules enforced on synthetic packet traces, precision of the detector measured against prevalence, a reference monitor that refuses read-up and write-down on random sequences, and engines that explain each decision.

</details>

### U7.2 Knowing your attacker: the MITRE ATT&CK framework
**Sources:** PCS W2–3
- **Topics:** Knowing your attacker: MITRE ATT&CK Framework: knowledge base of adversary behaviour built from public reporting; the matrices (Enterprise, Mobile, ICS), tactics as the attacker's goal at a stage (reconnaissance through impact, 14 in the Enterprise matrix in the author's reading), techniques and sub-techniques with their identifiers, procedures, groups, software, mitigations and data sources; week 2 of the source: structure and navigation of the matrix; week 3: use of the framework: mapping a report to techniques, ATT&CK Navigator layers, gap analysis of a defender's detections against the techniques that matter, adversary emulation plans, detection engineering; versioned releases and deprecations, and why a score computed against one release is not comparable to another; the framework as STIX data (continued in U7.6).
- **Results:** Choosing the fewest detections that cover a set of techniques is set cover, NP-hard, and the greedy rule that always takes the detection covering most uncovered techniques is within a factor H(n) ≈ ln n + 1 of optimal [P]; the Jaccard similarity of two groups' technique sets is a bounded, symmetric measure of overlap, and 1 minus Jaccard is a metric [P]; a coverage score that counts a technique as covered by any one detection overstates assurance when detections fail independently with probability q: expected uncovered fraction is q^k with k detections [D].
- **Build:** a loader and validator for a locally-defined technique-layer JSON (tactic, technique, score, comment) modelled on Navigator layers; a coverage calculator; a greedy and an exact (small-instance) set-cover detection planner; a group-similarity matrix on a technique set you enter by hand from a public report with the source named; a Sigma-style rule evaluator that tags events with technique identifiers. [local]
- **Gap-fills:** *[inferred: the ATT&CK release notes; Sigma rule specification, recalled, not checked]* the current matrix version and tactic count must be read from the ATT&CK site at study time.

**Assignment A7.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** In the ATT&CK framework, what does a tactic represent?

(A) A specific tool  
(B) The adversary's tactical goal at a stage of an attack  
(C) A vulnerability identifier  
(D) A malware family

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Choosing the fewest detections covering a set of techniques is a set cover problem  
(B) The greedy rule is within a logarithmic factor of optimal  
(C) One minus the Jaccard similarity of two sets is a metric  
(D) ATT&CK scores computed for different releases are always comparable

**Q3 (2 marks, numerical answer).** Greedy set cover over n = 100 techniques is within the n-th harmonic number of optimal. What is H(100) to two decimals?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that the greedy set-cover algorithm covers all elements and that its cost is at most H(n) times the optimum for unit costs.

**Q5 (3 marks, programming).** Write a loader and validator for a technique-layer JSON, a coverage calculator, greedy and exact set-cover planners for detections, and a group-similarity matrix on technique sets you enter by hand from public reports with sources named.

<details><summary>Key for A7.2 (open only after your attempt)</summary>

- **Q1:** B. Tactics are the why of an action, such as persistence or credential access; techniques are the how.
- **Q2:** A, B, C. Releases add, split and deprecate techniques, so scores are not directly comparable.
- **Q3:** 5.187 (tolerance ±0.01). The sum 1 + 1/2 + ... + 1/100 is about 5.19.
- **Q4 (marking outline):** Each step picks the set covering most uncovered elements; the algorithm ends when everything is covered, which is possible if a cover exists; assign each element the price 1 over the number newly covered in its step; the optimum's sets cover everything, so by charging argument the total price is at most H(n) times the optimum.
- **Q5 (what a passing submission shows):** A validated layer format, coverage figures that match hand counts, a greedy plan compared with the exact optimum on small cases, and a similarity matrix that is symmetric with unit diagonal.

</details>

### U7.3 Cyber kill chains: the Lockheed Martin Cyber Kill Chain and the Unified Kill Chain
**Sources:** PCS W4
- **Topics:** Cyber Kill Chains: the Lockheed Martin Cyber Kill Chain (reconnaissance, weaponization, delivery, exploitation, installation, command and control, actions on objectives) and its intelligence-driven defence reading with the courses-of-action matrix (detect, deny, disrupt, degrade, deceive, destroy); the Unified Kill Chain (a phase model organised into initial foothold, network propagation and actions on objectives, with 18 phases in the author's reading); mapping both to ATT&CK tactics (U7.2); strengths and criticisms (linear, perimeter-centric, weak against insiders and supply-chain attacks); indicators and the pyramid of pain; the Diamond Model as a companion.
- **Results:** If an attacker must pass n stages and a defence stops it at stage i with independent probability d_i, the attack completes with probability ∏(1 − d_i), so stopping early and stopping late are equal in probability but not in damage [D]; with a budget B and detection function d_i(b_i), the allocation that minimises ∏(1 − d_i) when each (1 − d_i) = exp(−λ_i b_i) is the one that equalises λ_i across funded stages, a linear programme in the exponents (U4.5) [P]; a kill chain broken at any single stage ends the attack, so the cheapest cut equals the cheapest single stage to harden [D].
- **Build:** a Monte Carlo kill-chain simulator with per-stage detection and a time dimension (damage grows with the stage reached); a budget allocation by linear programming against the closed form; a table linking each kill-chain stage to ATT&CK tactics; a scenario worksheet for the Target case of U6.1. [local]
- **Gap-fills:** *[inferred: Hutchins, Cloppert and Amin 2011; Pols, The Unified Kill Chain, recalled, not checked]* attack graphs and the MulVAL approach (named only).

**Assignment A7.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Which stage comes first in the Lockheed Martin Cyber Kill Chain?

(A) Delivery  
(B) Reconnaissance  
(C) Exploitation  
(D) Installation

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) If the attack must pass every stage, defence at any single stage can stop it  
(B) The courses-of-action matrix includes detect, deny, disrupt, degrade, deceive and destroy  
(C) The Unified Kill Chain groups phases into initial foothold, network propagation and actions on objectives  
(D) The kill chain handles insider threats and supply-chain attacks without modification

**Q3 (2 marks, numerical answer).** An attack must pass seven stages, and each stage is independently stopped by the defender with probability 0.2. What is the probability that the attack completes?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that when stages are stopped independently with probabilities d_i the attack completes with probability the product of (1 - d_i), and that raising any single d_i lowers the completion probability.

**Q5 (3 marks, programming).** Write a Monte Carlo kill-chain simulator with per-stage detection probabilities and a damage measure that grows with the stage reached, allocate a fixed budget across stages by linear programming and by the closed form, and tabulate the mapping of stages to ATT&CK tactics.

<details><summary>Key for A7.3 (open only after your attempt)</summary>

- **Q1:** B. The seven stages begin with reconnaissance and end with actions on objectives.
- **Q2:** A, B, C. Its perimeter-centred linear model fits those threats poorly.
- **Q3:** 0.2097 (tolerance ±0.001). The completion probability is 0.8 to the power 7, about 0.21.
- **Q4 (marking outline):** Completion requires passing every stage, which are independent events with probability 1 minus d_i; the joint probability is the product; the product is strictly decreasing in each factor when the other factors are positive.
- **Q5 (what a passing submission shows):** A simulator agreeing with the product formula, an allocation that equalises the marginal return, and a table linking stages to tactics.

</details>

### U7.4 Defending yourself: the MITRE D3FEND framework
**Sources:** PCS W5
- **Topics:** Defending Yourself: MITRE DEF3ND Framework (the source writes "DEF3ND"; the framework is MITRE D3FEND): a knowledge graph of defensive countermeasures: the tactic columns (Model, Harden, Detect, Isolate, Deceive, Evict, and Restore in later releases, in the author's reading), the digital-artifact ontology that links defensive techniques to the artifacts they act on, and the mapping from ATT&CK offensive techniques to D3FEND countermeasures; using the matrix to choose controls for a threat profile, to compare products and to explain a control's purpose; cost-aware selection of countermeasures.
- **Results:** Selecting a minimum-cost set of countermeasures that together cover all techniques of a threat profile is weighted set cover, NP-hard by reduction from set cover, with a greedy cost-per-new-element rule within H(n) of optimal [P]; the mapping from attacks to defences is a bipartite graph, and a countermeasure's marginal value is the number of still-uncovered techniques it adds [Def].
- **Build:** a bipartite attack-to-countermeasure mapping stored as JSON (entered by hand from the public D3FEND pages, with identifiers copied exactly and each source URL named); a greedy and an exact weighted set-cover selector with the NP-hardness reduction coded as a generator of hard instances; a report that, for a given threat profile from U7.2, lists a recommended control set with its coverage and cost. [local]
- **Gap-fills:** *[inferred: Kaloroumakis and Smith, Toward a Knowledge Graph of Cybersecurity Countermeasures, recalled, not checked]* the current tactic list and artifact ontology must be read from the D3FEND site.

**Assignment A7.4** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What does D3FEND catalogue?

(A) Vulnerabilities  
(B) Defensive countermeasure techniques  
(C) Malware samples  
(D) Compliance laws

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Weighted set cover is NP-hard  
(B) The mapping from attack techniques to defences can be stored as a bipartite graph  
(C) The greedy cost-per-new-element rule has a logarithmic approximation guarantee  
(D) The framework's tactic list never changes between releases

**Q3 (2 marks, numerical answer (subsets)).** An exact search for the cheapest cover among 20 candidate countermeasures by trying all subsets examines how many subsets?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that the decision version of weighted set cover is NP-hard by reduction from unweighted set cover.

**Q5 (3 marks, programming).** Store a hand-entered attack-to-countermeasure mapping as JSON with identifiers copied exactly and sources named, and write greedy and exact weighted set-cover selectors and a report that lists a recommended control set with coverage and cost for a threat profile.

<details><summary>Key for A7.4 (open only after your attempt)</summary>

- **Q1:** B. D3FEND is a knowledge graph of defensive techniques linked to the digital artifacts they act on.
- **Q2:** A, B, C. The list has been extended in later releases, so it must be read at study time.
- **Q3:** 1048576 subsets (tolerance ±0). There are 2^20 = 1,048,576 subsets.
- **Q4 (marking outline):** Given a set cover instance, give every set weight 1; a cover of size at most k exists iff a cover of weight at most k exists in the weighted instance; the reduction is polynomial; so the weighted problem is at least as hard.
- **Q5 (what a passing submission shows):** A selector whose greedy answer is compared with the exact optimum on small instances, a hard-instance generator based on the reduction, and a clear report.

</details>

### U7.5 Securing your configurations: STIG benchmarking
**Sources:** PCS W6
- **Topics:** Securing your Configurations: STIG Benchmarking: Security Technical Implementation Guides as vendor-specific hardening requirements, their severity categories (CAT I, II and III), rule identifiers and check and fix text, the checklist file and a viewer; the Security Content Automation Protocol with its XCCDF benchmark language and OVAL checks, OpenSCAP as the open-source scanner; community benchmarks with similar roles (CIS Benchmarks); typical Linux hardening checks (SSH daemon options, password and lockout policy, file permissions, audit rules, unused services); compliance scoring, exceptions and compensating controls, configuration drift and continuous compliance in cloud (policy checks in infrastructure code); the limits of benchmarks (compliance is not security).
- **Results:** A weighted compliance score is Σ w_i·pass_i / Σ w_i and depends on the weights, so scores from different weightings must not be compared [Def]; a drift check is a diff between a baseline set of (rule, value) pairs and the current set, with cost linear in the number of rules [D].
- **Build:** a mini rules engine in Python that reads rules in a small XCCDF-like format and audits configuration files in a directory (synthetic files in the unit, a lab VM's files if you have one) in read-only mode, generating a remediation script that is only ever shown and never run automatically; a weighted score and a drift report. Real benchmark content is downloaded from the publisher's page after checking the current release. [local; lab VM optional]
- **Gap-fills:** *[inferred: DISA STIG documentation; the SCAP 1.3 specification, recalled, not checked]* policy-as-code (continued in U8.6) and cloud configuration baselines (U7.7).

**Assignment A7.5** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** In the STIG severity scheme, which category is the most severe?

(A) CAT I  
(B) CAT II  
(C) CAT III  
(D) CAT IV

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) XCCDF describes benchmarks and OVAL describes checks  
(B) A compliance score depends on the weights chosen  
(C) Remediation scripts should be shown and reviewed rather than run automatically on a production host  
(D) A high compliance score proves the system is secure

**Q3 (2 marks, numerical answer).** A benchmark weights CAT I rules 10, CAT II rules 4 and CAT III rules 1. A system passes 8 of 10 CAT I rules, 30 of 40 CAT II rules and 20 of 20 CAT III rules. What is the weighted compliance score as a fraction?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that two different weightings can order two systems differently by giving a numerical example, and explain what this means for reporting.

**Q5 (3 marks, programming).** Write a small rules engine in a format like XCCDF that audits configuration files in a directory in read-only mode, produces a weighted score and a drift report against a baseline, and generates a remediation script that is only printed. Use synthetic files or a lab VM.

<details><summary>Key for A7.5 (open only after your attempt)</summary>

- **Q1:** A. CAT I findings are the most serious and are weighted highest.
- **Q2:** A, B, C. Compliance is not security.
- **Q3:** 0.7857 (tolerance ±0.001). The numerator is 220 and the denominator is 280, giving 0.786.
- **Q4 (marking outline):** System X passes all CAT I and no CAT III rules, system Y the opposite; with weight 10 on CAT I and 1 on CAT III X scores higher; with equal weights Y can score higher if it has more CAT III rules; so rankings depend on weights and the weights must be stated with the score.
- **Q5 (what a passing submission shows):** An audit that finds planted violations, a score and drift diff that match hand calculation, and a generated script that is never executed by the tool.

</details>

### U7.6 Sharing threat intelligence: STIX and TAXII
**Sources:** PCS W7
- **Topics:** Sharing Threat Intelligence: STIX and TAXII 2.0 (the source's version; the OASIS standards have moved on to 2.1, so differences are listed): STIX objects (domain objects such as indicator, malware, attack-pattern, threat-actor, intrusion-set, campaign, vulnerability, identity; relationship and sighting objects), the pattern language of indicators, bundles, object markings and the Traffic Light Protocol; TAXII: discovery, API roots, collections, objects and status resources over HTTP and JSON, producer and consumer roles; intelligence levels (strategic, operational, tactical, technical), indicators of compromise and their short life, quality, confidence and sharing rules (privacy and legal limits connect to U8.9).
- **Results:** Matching n indicators against a stream of events by hash set is O(1) per event for exact values and by a prefix trie is O(address length) for network ranges [D]; the expected number of false alerts per day from indicator matching is the event rate times the per-event false-match probability, which grows with the age and breadth of an indicator [D].
- **Build:** a bundle builder and a hand-coded validator for the STIX object subset above, cross-checked with the `stix2` library as an oracle where it can be installed; a minimal TAXII 2.0 server and client on loopback serving one collection from the standard library; an indicator-matching engine for file hashes, domains and CIDR ranges; a TLP-aware sharing filter. Only synthetic indicators are used. [local]
- **Gap-fills:** *[inferred: OASIS STIX 2.1 and TAXII 2.1 standards, recalled, not checked]* MISP and OpenCTI as platforms (named only).

**Assignment A7.6** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Which protocol carries STIX objects between a producer and a consumer?

(A) SMTP  
(B) TAXII  
(C) SNMP  
(D) NTP

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) STIX has domain objects such as indicator and malware and relationship objects that link them  
(B) The Traffic Light Protocol labels sharing restrictions  
(C) Matching exact hashes against an event stream can be done with a hash set  
(D) Indicators of compromise stay valid forever

**Q3 (2 marks, numerical answer (alerts)).** An indicator list is matched against 1,000,000 events per day and each event falsely matches with probability 10^-6. How many false alerts are expected per day?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that the expected number of false alerts per day equals the event rate times the per-event false-match probability, and that doubling the number of independent indicators roughly doubles it when the probabilities are small.

**Q5 (3 marks, programming).** Write a STIX bundle builder and validator for a subset of object types, a minimal TAXII 2.0 server and client on loopback serving one collection, an indicator matcher for hashes, domains and CIDR ranges, and a filter that respects Traffic Light Protocol markings. Use synthetic indicators only.

<details><summary>Key for A7.6 (open only after your attempt)</summary>

- **Q1:** B. TAXII defines the HTTP API for exchanging STIX content.
- **Q2:** A, B, C. Indicators age quickly as infrastructure changes.
- **Q3:** 1 alerts (tolerance ±0.001). The expected number is the product, 1 per day.
- **Q4 (marking outline):** By linearity of expectation the expected count is the sum over events of the match probability, which is rate times probability; with m independent indicators the per-event probability is 1 minus (1 - q)^m which is about m q for small m q, so it grows linearly in m.
- **Q5 (what a passing submission shows):** A bundle that validates against the library oracle, a client that discovers and fetches the collection from your server, matches on a test stream, and a filter that withholds restricted objects.

</details>

### U7.7 Cloud security and identity: APIs, IAM, service accounts, keys and the shared-responsibility model
**Sources:** GCF W4
- **Topics:** There's an API for that! You can't secure the Cloud right? (the published outline gives this title only, so the content is *inferred* from the platform's documentation): programmatic access through REST APIs and client libraries, API authentication by OAuth 2.0 (authorization-code flow with PKCE, client-credentials flow, access tokens as signed JWTs, scopes), API management and quotas; the shared-responsibility model; identity and access management (IAM): principals (users, groups, service accounts), roles as sets of permissions, policies as bindings on a resource hierarchy (organisation, folder, project, resource) with inheritance, deny policies and conditions, least privilege, short-lived credentials over long-lived keys; audit logs; encryption keys managed by the provider or by the customer (the key hierarchy of U5.18 in a managed service) and secret management; private service access and perimeters; the connection to the access-control models of U7.1.
- **Results:** The effective permission set of a principal on a resource is the union of its bindings along the path to the root minus matching deny rules, and evaluation is monotone in the allow set [P]; PKCE binds the authorization code to the client that began the flow, so an intercepted code is useless without the verifier [S]; the smallest set of roles that covers the permissions a workload has actually used is a set-cover problem and role recommendation is its greedy approximation [P].
- **Build:** an IAM policy evaluator with hierarchy inheritance, groups, conditions and deny rules, tested against a table of cases; an OAuth 2.0 authorization-code-with-PKCE server and client on loopback, with JWT signing and verification from the U5 primitives (HMAC and RSA, learning only) and an API behind a token-bucket quota; an audit-log analyser flagging over-broad bindings and service-account keys older than a threshold; a plan-only IAM design for the capstone project. [local; plan only]
- **Gap-fills:** *[inferred: RFC 6749, RFC 7636, RFC 7519; the platform's IAM documentation, recalled, not checked]* workload identity federation and the service-account-key incident pattern (read the provider's guidance).

**Assignment A7.7** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** How are effective IAM permissions on a resource determined when allow policies are inherited?

(A) Only by the policy on the resource itself  
(B) By the union of allows on the resource and its ancestors, minus matching denies  
(C) By the first policy found  
(D) By the oldest policy

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) PKCE binds an authorization code to the client that started the flow  
(B) Short-lived credentials are preferable to long-lived service-account keys  
(C) Least privilege means granting only the permissions needed  
(D) A service-account key committed to a public repository is harmless if the repository is private later

**Q3 (2 marks, numerical answer (characters)).** A PKCE S256 code challenge is the unpadded base64url encoding of a 32-byte SHA-256 digest. How many characters is it?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that evaluation of allow policies up a resource hierarchy is monotone: adding a binding at any node never removes a permission at any resource.

**Q5 (3 marks, programming).** Write an IAM policy evaluator with hierarchy inheritance, groups, conditions and deny rules, an OAuth 2.0 authorization-code with PKCE server and client on loopback with JWT signing, an API with token-bucket quotas, and an audit-log analyser that flags over-broad bindings. For learning only.

<details><summary>Key for A7.7 (open only after your attempt)</summary>

- **Q1:** B. Inherited allows are unioned and deny rules take precedence.
- **Q2:** A, B, C. A leaked key must be revoked; making the repository private does not undo exposure.
- **Q3:** 43 characters (tolerance ±0). 256 bits at 6 bits per character gives 42.67, so 43 characters.
- **Q4 (marking outline):** The permission set at a resource is the union of the sets granted at the resource and each ancestor; adding a binding adds a set to the union at the nodes below it and changes nothing elsewhere; union is monotone, so the set can only grow.
- **Q5 (what a passing submission shows):** An evaluator passing a table of cases, an OAuth flow that rejects a wrong verifier, quota enforcement that matches the configured rate, and an analyser that flags planted risky bindings.

</details>

## D8. Governance, risk, resilience and privacy

Aim: the managerial half of the security-and-privacy courses, made computational where it can be. A bridge on quantitative risk is taught first because risk management, resilience assessment and the capstone all depend on it. Privacy is treated as three layers: a conceptual layer (what privacy is and how it is measured), a technical layer (anonymisation and differential privacy, which the source does not list and which is supplied as a labelled gap-fill) and a legal and economic layer (regulation and the value of privacy). Nothing in this domain is legal advice. Benchmarks (recalled, not checked): Whitman and Mattord (named in the source); Hubbard and Seiersen, *How to Measure Anything in Cybersecurity Risk*; Freund and Jones, *Measuring and Managing Information Risk* (FAIR); Dwork and Roth, *The Algorithmic Foundations of Differential Privacy*; Solove, *Understanding Privacy*; Nissenbaum, *Privacy in Context*.

### U8.1 Security posture, governance, risk and compliance and maturity
**Sources:** CSP W3, o; PCS W1, o
- **Topics:** Introduction: cyber security posture, maturity and continuous improvement strategies; security management, governance, risk and compliance (GRC): the GRC framework, security standards (Text-Chapter 4, planning for security, pp. 171–176), the taking of a managerial and organisational view of cyber security with the human, legal and policy issues that the course outline names; frameworks and standards compared: ISO/IEC 27001 and 27002, the NIST Cybersecurity Framework (version 2.0 added a Govern function in the author's reading), the CIS Controls, PCI DSS and SOC 2; maturity models and their level scales, continuous improvement as plan–do–check–act, metrics and key performance indicators, roles (the board, the chief information security officer), and the practical-operations gap that motivates the practitioner course. Outline map of the two security-management courses: the course's learning objectives (to recognise cyber security from technological and administrative perspectives; to articulate cyber security governance, risks and compliance in the current business environment) are taught in this unit and U8.3; the practitioner course's complaint that academic courses give the fundamentals of cyber security but not the practical issues of running a cyber security operation in a real organisation, and its call for methods, methodologies and decision processes that simplify cyber operations and for reasoning in place of ad hoc decisions, is the reason for the quantitative and algorithmic treatment in U7.2 to U8.6; the human cognition of the inputs operators and leaders receive from tools and dashboards is taken up in the metrics dashboard of this unit.
- **Results:** Maturity levels form an ordinal scale, so averaging them is meaningful only under an explicit interval assumption, and a weighted average can reverse the ranking of two organisations when weights change [D]; the best next improvement under a budget maximises gap-times-weight per unit cost, which is optimal when improvements are independent and divisible and heuristic otherwise (continues in U8.3) [S].
- **Build:** a posture scorecard (controls by maturity level, weights, target, gaps) with a roadmap generator ranking improvements by weighted gap per cost; a control crosswalk between two frameworks entered by hand from the public documents with the source named, and a coverage report; a metrics dashboard specification for the capstone. [local]
- **Gap-fills:** *[inferred: NIST CSF 2.0; ISO/IEC 27001:2022; the CIS Controls v8, recalled, not checked]* the current editions are to be read from the publishers.

**Assignment A8.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Why should maturity levels not be averaged without care?

(A) They are ordinal and averaging assumes equal spacing  
(B) They are secret  
(C) They are continuous  
(D) They cannot be recorded

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) ISO/IEC 27001 specifies an information security management system  
(B) The NIST Cybersecurity Framework 2.0 added a Govern function  
(C) Continuous improvement is described by plan-do-check-act  
(D) Maturity scores computed with different weights are directly comparable

**Q3 (2 marks, numerical answer).** Three control areas have maturity scores 2, 3 and 4 with weights 0.5, 0.3 and 0.2. What is the weighted average maturity?

**Q4 (2 marks, prove or derive; every step with its reason).** Give a numerical example showing that a weighted average of ordinal maturity scores can reverse the ranking of two organisations when the weights change.

**Q5 (3 marks, programming).** Write a posture scorecard that takes controls with maturity levels, weights and targets and produces gaps and a roadmap ranked by weighted gap per cost, and a crosswalk between two frameworks entered by hand with sources named.

<details><summary>Key for A8.1 (open only after your attempt)</summary>

- **Q1:** A. Ordinal scales have no guaranteed equal intervals, so means can mislead and weights can reverse rankings.
- **Q2:** A, B, C. Different weightings are not comparable.
- **Q3:** 2.7 (tolerance ±0.001). The weighted sum is 1.0 + 0.9 + 0.8 = 2.7.
- **Q4 (marking outline):** Organisation A scores (4, 1) and B scores (2, 3) on two areas; with weights (0.8, 0.2) A has 3.4 and B has 2.2 so A ranks higher; with weights (0.2, 0.8) A has 1.6 and B has 2.8 so B ranks higher; the ranking reverses.
- **Q5 (what a passing submission shows):** A scorecard with tests on hand-computed cases, a roadmap order that follows the ratio, and a crosswalk coverage report.

</details>

### U8.2 Bridge: quantitative risk — frequency and severity models, Monte Carlo loss exceedance, Bayesian updating and decision under uncertainty
**Sources:** none (prerequisite bridge, added so that later units rest on taught ground)
Bridge for: U8.3 (risk management), U8.5 (resilience assessment), U13.6 (security programme capstone). Builds on U5.1.
- **Topics:** Risk as likelihood and impact and its pitfalls; single-loss expectancy, annualised rate of occurrence and annualised loss expectancy; frequency–severity models: Poisson counts, lognormal and Pareto severities, the compound Poisson total loss and its moments; Monte Carlo estimation of the loss-exceedance curve, value at risk and expected shortfall; the failure of ordinal risk matrices and the rank-reversal examples; Bayesian estimation of an event frequency with a gamma prior; calibrated estimation and expert elicitation; return on security investment, expected utility, risk aversion, and the value of information.
- **Results:** For compound Poisson S = X₁ + … + X_N with N ~ Poisson(λ), E[S] = λE[X] and Var[S] = λE[X²] [P]; for lognormal(μ, σ²), E[X] = exp(μ + σ²/2) [D]; with a gamma(a, b) prior and k events in t years the posterior is gamma(a + k, b + t) [P]; two risks can be ranked in opposite order by a 5-by-5 matrix and by expected annual loss [D, by example].
- **Build:** a Monte Carlo loss-exceedance engine with value at risk and expected shortfall, checked against the closed-form moments; a gamma–Poisson updater; a return-on-security-investment calculator with a sensitivity sweep; the rank-reversal example reproduced in code. [local]
- **Gap-fills:** *[inferred: Hubbard–Seiersen; Cox, What's wrong with risk matrices, recalled, not checked]* copulas for dependent losses (named only).

**Assignment A8.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** For a compound Poisson loss with frequency lambda and mean severity E[X], what is the expected total loss?

(A) lambda plus E[X]  
(B) lambda times E[X]  
(C) E[X] divided by lambda  
(D) lambda squared

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) The variance of a compound Poisson total is lambda E[X squared]  
(B) A gamma prior is conjugate to a Poisson frequency  
(C) Ordinal risk matrices can rank two risks opposite to their expected annual loss  
(D) Value at risk is always the worst possible loss

**Q3 (2 marks, numerical answer (currency units)).** An organisation expects 2 incidents per year with mean loss 50,000 per incident. What is the expected annual loss?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that for S equal to the sum of N independent copies of X with N Poisson with mean lambda, the mean of S is lambda E[X] and the variance is lambda E[X squared].

**Q5 (3 marks, programming).** Write a Monte Carlo loss-exceedance engine with value at risk and expected shortfall checked against the closed-form moments, a gamma-Poisson updater, a return-on-security-investment calculator with a sensitivity sweep, and reproduce a rank-reversal example.

<details><summary>Key for A8.2 (open only after your attempt)</summary>

- **Q1:** B. Wald's identity gives E[S] = lambda E[X].
- **Q2:** A, B, C. Value at risk is a quantile of the loss distribution, not its maximum.
- **Q3:** 100000 currency units (tolerance ±0). Expected annual loss is 2 times 50,000 = 100,000.
- **Q4 (marking outline):** Condition on N: E[S given N] = N E[X] so E[S] = E[N] E[X]; by the law of total variance Var(S) = E[N] Var(X) + Var(N) E[X]^2 = lambda Var(X) + lambda E[X]^2 = lambda E[X squared].
- **Q5 (what a passing submission shows):** Simulated mean and variance within sampling error of the formulas, an exceedance curve, a posterior that updates with data, and an example where the matrix ranking and expected loss disagree.

</details>

### U8.3 Cyber security risk management: identification, assessment, control and treatment
**Sources:** CSP W6; PCS W8
- **Topics:** Cyber Security Risk Management: cyber risk identification, assessment and control (Text-Chapter 5, risk management: identifying and assessing risk); the risk register, qualitative and quantitative assessment (the methods of U8.2), the treatment options (mitigate, accept, transfer, avoid), residual risk, risk appetite and tolerance, control selection and its cost, cyber insurance as transfer; process models (NIST SP 800-30 and the risk management framework, ISO/IEC 27005, FAIR); third-party and supply-chain risk; the case study of a company's protection of its core assets (the Harvard Business Review case in the source, Protecting the Cheddar, from the HBR series The end of cyber security, read as a case and not summarised here).
- **Results:** Choosing controls to minimise residual expected loss under a budget is a 0/1 knapsack, NP-hard, with an O(nB) pseudo-polynomial dynamic programme [P]; when controls reduce loss multiplicatively (independent failure factors) the marginal benefit of the next control falls and the greedy rule by benefit per cost is a good heuristic but not optimal [D]; a premium is worth paying exactly when it is below expected transferred loss plus the risk-aversion premium [D].
- **Build:** a risk register with annualised loss estimates and Monte Carlo ranges from U8.2; a knapsack optimiser for control selection compared with greedy on random instances, with the optimality gap measured; a sensitivity and tornado analysis; a worked register for the synthetic organisation used in U13.6. [local]
- **Gap-fills:** *[inferred: NIST SP 800-30 Rev. 1; ISO/IEC 27005, recalled, not checked]* risk aggregation across the enterprise (continued in U13.6).

**Assignment A8.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Selecting controls to minimise residual loss under a budget is which classic problem?

(A) Shortest path  
(B) 0/1 knapsack  
(C) Minimum spanning tree  
(D) Bipartite matching

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Risk treatment options include mitigate, accept, transfer and avoid  
(B) Residual risk is the risk that remains after controls  
(C) The knapsack problem has a pseudo-polynomial dynamic programme  
(D) Insurance removes risk entirely

**Q3 (2 marks, numerical answer (entries)).** A dynamic programme for choosing among 20 controls with an integer budget of 100 fills a table with n times B entries. How many entries?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that the greedy rule by benefit per cost is not optimal for the 0/1 knapsack by giving a counterexample.

**Q5 (3 marks, programming).** Write a risk register with annualised loss estimates and Monte Carlo ranges, a knapsack optimiser for control selection compared with greedy on random instances with the optimality gap measured, and a tornado sensitivity analysis, for the synthetic organisation.

<details><summary>Key for A8.3 (open only after your attempt)</summary>

- **Q1:** B. Each control is taken or not, with a cost and a benefit, under a total budget.
- **Q2:** A, B, C. Insurance transfers financial loss but not the incident.
- **Q3:** 2000 entries (tolerance ±0). 20 times 100 gives 2000 entries.
- **Q4 (marking outline):** Budget 10; item A costs 6 with benefit 7, item B costs 5 with benefit 5.5, item C costs 5 with benefit 5.5; greedy by ratio takes A (1.17) then cannot take B or C within budget 4 left, total 7; the optimum takes B and C for 11.
- **Q5 (what a passing submission shows):** A register whose totals match a hand check, an optimiser that matches brute force on small cases, and a gap statistic for greedy.

</details>

### U8.4 Contingency planning and cyber crisis management: incident response, disaster recovery and business continuity
**Sources:** CSP W4; PCS W12
- **Topics:** Contingency planning: Incidence response (the source's spelling; incident response), Disaster Recovery and the business continuity plan (BCP) (Text-Chapter 4, planning for security, pp. 214–251); Cyber Crisis Management Plan and Cyber Incident Management Plan: the incident lifecycle (preparation, detection and analysis, containment, eradication and recovery, post-incident review), roles and communication, business impact analysis, recovery time and recovery point objectives, maximum tolerable downtime, backup strategy (3-2-1), disaster-recovery tiers (cold, warm, hot), notification duties to regulators (the CERT-In reporting direction of 2022, recalled, not checked), tabletop exercises, digital forensics at the level of evidence handling and chain of custody (hashing from U5.10); how cloud regions and zones implement recovery (continued in U10 and U12).
- **Results:** The steady-state availability of a repairable component is MTBF / (MTBF + MTTR) [D]; availability composes as the product for components in series and 1 − ∏(1 − a_i) for components in parallel [P]; worst-case data loss under periodic backup plus asynchronous replication is the backup interval plus the replication lag, which must not exceed the recovery point objective [D]; the cost-minimising disaster-recovery tier equates marginal standby cost with expected downtime cost [D].
- **Build:** an availability calculator for series-parallel and k-of-n structures and a two-state Markov model checked by simulation; an incident-log analyser that computes time to detect and time to recover; an incident-response playbook as an executable state machine that enforces ordering and records decisions; a hash-chained evidence ledger. [local]
- **Gap-fills:** *[inferred: NIST SP 800-61 Rev. 2 and its successor; NIST SP 800-34, recalled, not checked]* the tabletop-exercise design guide of CISA (read from the publisher).

**Assignment A8.4** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What is the steady-state availability of a repairable component with mean time between failures M and mean time to repair R?

(A) M divided by R  
(B) M over (M plus R)  
(C) R over (M plus R)  
(D) M times R

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Components in series have availability equal to the product of their availabilities  
(B) Components in parallel have availability one minus the product of unavailabilities  
(C) Worst-case data loss is bounded by the backup interval plus the replication lag in the combined scheme described  
(D) A business continuity plan has no need of tabletop exercises

**Q3 (2 marks, numerical answer).** A service has a mean time between failures of 1000 hours and a mean time to repair of 2 hours. What is its steady-state availability?

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the availability of two independent components in parallel, each with availability a, and compare with a single component.

**Q5 (3 marks, programming).** Write an availability calculator for series-parallel and k-of-n structures checked against a two-state Markov simulation, an incident-log analyser computing time to detect and recover, an incident-response playbook as an executable state machine, and a hash-chained evidence ledger.

<details><summary>Key for A8.4 (open only after your attempt)</summary>

- **Q1:** B. Availability is the fraction of time up, M/(M + R).
- **Q2:** A, B, C. Exercises are how plans are tested.
- **Q3:** 0.998 (tolerance ±0.00001). The availability is 1000/1002, about 0.998.
- **Q4 (marking outline):** The system is down only when both are down, probability (1 minus a) squared; availability is 1 minus (1 minus a) squared = a (2 minus a), which exceeds a for 0 below a below 1.
- **Q5 (what a passing submission shows):** Calculated and simulated availability agreeing, correct time metrics on a sample log, a playbook that enforces step order, and a ledger that detects tampering.

</details>

### U8.5 Cyber resilience assessment
**Sources:** PCS W9
- **Topics:** Cyber Resilience Assessment: resilience defined as the ability to anticipate, withstand, recover from and adapt to adverse conditions; measuring it through performance-over-time curves (the depth and duration of the loss and the area between nominal and actual performance, the resilience-triangle idea), time to detect and time to recover, redundancy and diversity, graceful degradation; assessment methods (self-assessment questionnaires, exercises, cyber ranges, controlled fault injection, whose operational form is chaos engineering in U12.1); stress-scenario design; dependencies among services as a graph and their cascading failures.
- **Results:** For a linear drop to depth D followed by linear recovery over time T the lost performance is DT/2 [D]; with independent exponential repairs at rate μ and failures at rate λ, a k-replica service is up with probability 1 − (λ/(λ + μ))^k [D]; correlated failures from a shared dependency cap the benefit of replication at the dependency's own availability [D].
- **Build:** a Monte Carlo resilience simulator for a service-dependency graph under random node failures and repairs, computing the resilience curve, area lost and recovery time; a comparison of a single-instance, a replicated and a diversified architecture, with the correlated-failure ceiling shown; a resilience scorecard from assessment answers. [local]
- **Gap-fills:** *[inferred: NIST SP 800-160 Vol. 2; Bruneau et al. 2003, recalled, not checked]* the CERT Resilience Management Model (named only).

**Assignment A8.5** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** In the resilience-triangle idea, what quantity measures the loss of performance?

(A) The area between nominal and actual performance over time  
(B) The peak performance  
(C) The number of users  
(D) The code size

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Resilience includes anticipating, withstanding, recovering and adapting  
(B) A shared dependency caps the benefit of replication  
(C) Controlled fault injection is a way to assess resilience  
(D) Replication always removes correlated failures

**Q3 (2 marks, numerical answer (percentage-point hours)).** Performance drops by 60 percentage points and then recovers linearly over 10 hours. What is the lost performance in percentage-point hours using half the depth times the duration?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that for a linear drop to depth D at time zero followed by linear recovery over a time T the area lost is D T / 2.

**Q5 (3 marks, programming).** Write a Monte Carlo resilience simulator for a service-dependency graph under random failures and repairs that outputs the resilience curve, area lost and recovery time, and compare single-instance, replicated and diversified architectures including the shared-dependency ceiling.

<details><summary>Key for A8.5 (open only after your attempt)</summary>

- **Q1:** A. Loss is the integral of the shortfall, which for a linear drop and recovery is half depth times duration.
- **Q2:** A, B, C. Correlated failures are not removed by replicas that share a dependency.
- **Q3:** 300 percentage-point hours (tolerance ±0). The triangle area is 60 times 10 divided by 2 = 300.
- **Q4 (marking outline):** The shortfall is a triangle with height D and base T; the area of a triangle is half base times height; so the loss equals D T over 2.
- **Q5 (what a passing submission shows):** Curves that reproduce the predicted ceiling, comparisons across architectures with confidence intervals, and a scorecard from assessment answers.

</details>

### U8.6 Cyber security policy formulation
**Sources:** CSP W5; PCS W10–11
- **Topics:** Cyber Security Policy Formulation (two weeks in the source) and Cyber security policy: ESSP, ISSP, SYSSP (enterprise, issue-specific and system-specific policy; Text-Chapter 4, information security policy, pp. 177–213): the hierarchy of policy, standard, procedure and guideline, the elements of a policy (purpose, scope, roles, requirements, sanctions, review), the lifecycle of development, dissemination, enforcement and review, acceptable use, remote work and personal devices, access-control policy tied to U7.1, third-party and data-handling policy; the argument of the Harvard Business Review reading on internet insecurity, from its series The end of cyber security (HBR); national and sectoral policy (India's National Cyber Security Policy of 2013 and the CERT-In role, recalled, not checked); policy as code and the detection of conflicts among rules.
- **Results:** Two rules in an ordered list are in conflict if their conditions overlap and their decisions differ, and a later rule is shadowed if an earlier rule covers it entirely with the same or opposite decision [Def]; detecting shadowing among n rules of d fields is O(n²d) by pairwise containment and the unit's checker reports every anomaly class [D]; RFC 2119 keywords (MUST, SHOULD, MAY) give a policy statement a checkable strength [Def].
- **Build:** a policy-as-code engine with rules in a small declarative format, with shadowing, redundancy and conflict detection; a linter for policy documents that flags weak or ambiguous requirement language and missing elements; a mapping from policy statements to the controls of U8.1. [local]
- **Gap-fills:** *[inferred: Bellovin and Bush; Al-Shaer and Hamed on firewall policy anomalies, recalled, not checked]* policy verification by satisfiability solving (named only).

**Assignment A8.6** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Which kind of policy is system-specific in the ESSP, ISSP, SYSSP scheme?

(A) Enterprise information security policy  
(B) Issue-specific policy  
(C) Policy for one particular system  
(D) National policy

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) A rule is shadowed if an earlier rule matches every packet it would match  
(B) RFC 2119 keywords give requirement strength  
(C) Policy conflict detection compares overlap and differing decisions  
(D) A policy needs no review once published

**Q3 (2 marks, numerical answer (pairs)).** A rule set has 200 rules. How many pairs of rules must be compared by a pairwise anomaly check?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that detecting all shadowed rules in an ordered list of n rules by pairwise containment takes O(n squared d) time for rules with d fields.

**Q5 (3 marks, programming).** Write a policy-as-code engine with a declarative rule format and detection of shadowing, redundancy and conflict, a linter for policy documents that flags weak language and missing elements, and a mapping from policy statements to controls.

<details><summary>Key for A8.6 (open only after your attempt)</summary>

- **Q1:** C. SYSSP governs configuration and use of a particular system.
- **Q2:** A, B, C. Policies need periodic review.
- **Q3:** 19900 pairs (tolerance ±0). There are n(n - 1)/2 = 19,900 pairs.
- **Q4 (marking outline):** For each rule compare against every earlier rule: n(n - 1)/2 pairs; each containment test checks d fields in O(1) each; total O(n squared d).
- **Q5 (what a passing submission shows):** An engine that finds planted anomalies, a linter with tests on good and bad documents, and a mapping report.

</details>

### U8.7 Foundations of privacy: concepts, theories and measurement
**Sources:** CSP W9
- **Topics:** Foundations of privacy: information privacy, measurement, theories: privacy as the right to be let alone, as control over information (Westin), as restricted access, as contextual integrity (information flows judged against the norms of a context), Solove's taxonomy of harms; the Stanford Encyclopedia of Philosophy entry on privacy and the HBR Online piece We Googled you (on searching for people online) as the course's readings; how information privacy is measured (concern instruments, the privacy calculus, the personalisation–privacy paradox) with the standard reliability and validity tools; stakeholders from the origin of data to its end use.
- **Results:** Cronbach's alpha for k items is k/(k − 1) · (1 − Σσ²_i / σ²_total) and rises with the mean inter-item correlation [D]; a contextual-integrity norm is a predicate over (data type, sender, recipient, subject, transmission principle) and a flow violates the norm iff the predicate is false [Def].
- **Build:** a survey-scoring pipeline on synthetic privacy-concern data: item scoring, Cronbach's alpha, and a principal-component factor check with NumPy; a contextual-integrity checker that evaluates information flows against norms you write for a clinic, a school and a retailer. [local]
- **Gap-fills:** *[inferred: Smith, Dinev and Xu 2011 (listed in the source's references); Nissenbaum 2004, recalled, not checked]* privacy by design (Cavoukian) principles.

**Assignment A8.7** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** In contextual integrity, when does an information flow violate privacy norms?

(A) When it is encrypted  
(B) When it breaks the norms of the context in which the information was shared  
(C) When it is large  
(D) When it is fast

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Cronbach's alpha measures internal consistency of a scale  
(B) Alpha tends to rise with the average inter-item correlation  
(C) Privacy has been defined as control over information about oneself  
(D) A high alpha proves that the scale is valid

**Q3 (2 marks, numerical answer).** A scale has k = 4 items, the sum of the item variances is 4.0 and the total score variance is 10.0. What is Cronbach's alpha?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that if all k items are perfectly correlated and have equal variance then Cronbach's alpha equals 1.

**Q5 (3 marks, programming).** Write a survey-scoring pipeline on synthetic privacy-concern data with Cronbach's alpha and a principal-component check, and a contextual-integrity checker that evaluates flows against norms you write for a clinic, a school and a retailer.

<details><summary>Key for A8.7 (open only after your attempt)</summary>

- **Q1:** B. Flows are judged against the norms of sender, recipient, subject, type and transmission principle for the context.
- **Q2:** A, B, C. Reliability does not establish validity.
- **Q3:** 0.8 (tolerance ±0.001). Alpha = 4/3 times (1 - 0.4) = 0.8.
- **Q4 (marking outline):** Total variance is k squared times the item variance, since the sum of k identical copies; sum of item variances is k times the item variance; alpha = k/(k - 1) times (1 minus 1/k) = k/(k - 1) times (k - 1)/k = 1.
- **Q5 (what a passing submission shows):** Alpha matching a library or manual computation, a factor structure recovered from synthetic data, and a checker that flags planted norm violations.

</details>

### U8.8 Anonymity and privacy-enhancing technologies: re-identification, k-anonymity, differential privacy and anonymous communication
**Sources:** CSP W10
- **Topics:** Privacy, anonymity, regulation, data breach (the anonymity and breach parts; regulation continues in U8.9): anonymity, pseudonymity and unlinkability; re-identification by linking quasi-identifiers and why removing names is not anonymisation; technical remedies that the source course does not list and that are supplied as a labelled gap-fill, *inferred* from the privacy literature it cites: k-anonymity by generalisation and suppression, l-diversity and t-closeness, differential privacy (the ε definition, sensitivity, the Laplace and randomised-response mechanisms, composition and a privacy budget); anonymous communication by mixes and onion routing; secure computation and homomorphic encryption (U5.21, U5.23) as privacy-enhancing technologies; the anatomy of a data breach and its handling (detection, scope, notification).
- **Results:** The Laplace mechanism with scale Δf/ε satisfies ε-differential privacy [P]; sequential composition adds the ε's and parallel composition on disjoint data takes the maximum [P]; randomised response with truth probability p gives ε = ln(p/(1 − p)) and an unbiased estimator with variance that grows as ε shrinks [D]; k-anonymity is broken by a homogeneity or background-knowledge attack even when every class has at least k rows [D].
- **Build:** a k-anonymiser over a generalisation lattice and a linkage attack on a synthetic population against a synthetic public register; the Laplace mechanism, randomised response and a privacy-budget accountant with measured error against ε; a layered-encryption onion routing toy on loopback using your own primitives, learning only. [local]
- **Gap-fills:** *[inferred: Sweeney 2002; Dwork and Roth 2014, recalled, not checked]* local versus central differential privacy, the privacy-utility trade-off in practice.

**Assignment A8.8** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What does the Laplace mechanism add to a query result to give epsilon-differential privacy?

(A) Gaussian noise of fixed size  
(B) Laplace noise with scale sensitivity divided by epsilon  
(C) A constant  
(D) A hash

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Sequential composition adds the epsilons  
(B) k-anonymity can be broken by a homogeneity attack  
(C) Removing names from a dataset is enough for anonymity  
(D) Randomised response gives plausible deniability for each answer

**Q3 (2 marks, numerical answer).** A randomised-response scheme answers truthfully with probability p = 0.75 and lies otherwise. What epsilon does it satisfy, as the natural logarithm of p/(1 - p)?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that the Laplace mechanism with scale b = Delta/epsilon satisfies epsilon-differential privacy for a query with sensitivity Delta.

**Q5 (3 marks, programming).** Write a k-anonymiser over a generalisation lattice and a linkage attack on a synthetic population, implement the Laplace mechanism, randomised response and a privacy-budget accountant, and a layered-encryption onion routing toy on loopback. Synthetic data only; for learning only.

<details><summary>Key for A8.8 (open only after your attempt)</summary>

- **Q1:** B. The scale b = sensitivity over epsilon gives epsilon-differential privacy.
- **Q2:** A, B, D. Quasi-identifiers allow linking even after names are removed.
- **Q3:** 1.099 (tolerance ±0.005). The ratio is 3 and ln 3 is about 1.0986.
- **Q4 (marking outline):** The output density at value y is proportional to exp(minus the absolute value of (y minus f(D)) over b); for neighbouring datasets f changes by at most Delta, so the ratio of densities is at most exp(Delta/b) = exp(epsilon) for every y.
- **Q5 (what a passing submission shows):** A linkage attack that succeeds before anonymisation and fails after, an error against epsilon curve, an accountant refusing to exceed the budget, and an onion toy that peels layers correctly.

</details>

### U8.9 Privacy regulation: GDPR in Europe, privacy in India (DPDP, Aadhaar) and breach duties
**Sources:** CSP W10–11
- **Topics:** Privacy regulation (Text-Chapter 3, law and ethics; the UNCTAD survey of data-protection and privacy legislation worldwide as the global map), Privacy regulation in Europe, Privacy: The Indian Way: Data Protection, GDPR, DPDP, Aadhar (also spelled Aadhaar in the readings, with the IIT Delhi analysis of its privacy and security from A Computer Science perspective): the GDPR's principles (lawfulness, fairness and transparency; purpose limitation; data minimisation; accuracy; storage limitation; integrity and confidentiality; accountability), lawful bases including consent, the rights of data subjects, data protection impact assessment, breach notification within 72 hours to the regulator, cross-border transfer rules; India: the constitutional recognition of privacy (the 2017 Puttaswamy judgment, recalled, not checked), the Digital Personal Data Protection Act, 2023 (the 2023 bill is the reading in the source; it became an Act), and the DPDP Rules, 2025, which MeitY notified on 13 November 2025 with a phased commencement: the Data Protection Board provisions immediately, consent-manager provisions after about 12 months (that is, from about November 2026) and the remaining substantive duties after about 18 months (about May 2027), as read from law-firm summaries while building this curriculum and to be checked against the Gazette; the concepts data fiduciary, data principal and significant data fiduciary; the security and privacy discussion of the national identity system.
- **Results:** A consent record is valid for a stated purpose only and withdrawal must be as easy as giving it, so a consent ledger is an append-only log of grant and withdraw events whose current state is a fold over the log [Def]; a 72-hour clock runs from awareness, so the deadline is a function of the earliest detection timestamp [Def]; minimisation turns into a checkable property: every collected field is mapped to at least one declared purpose [Def].
- **Build:** a data-flow record format and an obligation mapper that, for a processing activity, lists the GDPR and DPDP obligations triggered under a rule table you write from the statutes' text with section references; a breach-clock calculator for the two regimes; a hash-chained consent ledger with grant, withdraw and purpose-change events; a records-of-processing generator. This is a teaching tool and not legal advice. [local]
- **Gap-fills:** *[inferred: GDPR text; DPDP Act 2023 and Rules 2025, checked on secondary summaries as above]* sectoral rules (health, finance) and cross-border mechanisms at the level of names only.

**Assignment A8.9** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Within which time after becoming aware must a controller notify the supervisory authority of a personal data breach under the GDPR?

(A) 24 hours  
(B) 72 hours  
(C) 7 days  
(D) 30 days

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) GDPR principles include purpose limitation and data minimisation  
(B) The DPDP Rules 2025 were notified on 13 November 2025 with phased commencement  
(C) A consent ledger can be modelled as an append-only log of grant and withdraw events  
(D) This curriculum's tools give legal advice

**Q3 (2 marks, numerical answer (months)).** The DPDP Rules were notified in November 2025 and full commencement is planned about May 2027. How many months is that?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that a consent ledger whose state is the fold of an append-only log of grant and withdraw events always yields the current consent status and an audit trail of past states.

**Q5 (3 marks, programming).** Write a data-flow record format with an obligation mapper for GDPR and DPDP rules you write from the statutes' text with section references, a breach-clock calculator, a hash-chained consent ledger and a records-of-processing generator. A teaching tool, not legal advice.

<details><summary>Key for A8.9 (open only after your attempt)</summary>

- **Q1:** B. The GDPR sets 72 hours where feasible after becoming aware of the breach.
- **Q2:** A, B, C. They are teaching tools and not legal advice.
- **Q3:** 18 months (tolerance ±0). Two years is 24 months minus 6 months gives 18.
- **Q4 (marking outline):** The status after each event is a function of the previous status and the event; folding the log in order gives the final status; since earlier entries are never changed the intermediate statuses can be recomputed at any prefix, giving the audit trail.
- **Q5 (what a passing submission shows):** A mapper that returns different obligations for different processing records, a clock that handles both regimes, and a ledger that detects alteration.

</details>

### U8.10 Information privacy: economics and strategy
**Sources:** CSP W12
- **Topics:** Information privacy: economics and strategy: the economic value of privacy, privacy valuation, WTA and WTC (the source's abbreviations; the willingness-to-accept and willingness-to-pay measures of the cited literature, where the second is usually written WTP, so WTC is flagged in Appendix E), the endowment effect that makes willingness to accept exceed willingness to pay for the same data, business strategy and privacy (personalisation benefits against customer concern, the dark side of customer analytics read as an HBR Case), espionage and corporate secrets, privacy versus safety (the Apple dilemma case in the readings); markets for personal data and externalities; behavioural findings that stated and revealed preferences diverge.
- **Results:** In a model where a consumer discloses if the expected personalisation benefit exceeds the expected privacy cost, the disclosure threshold falls when the firm commits to protection, so protection can raise both disclosure and revenue [D]; the endowment effect is detected by a two-sample test on elicited WTA and WTP and its effect size is the mean difference over the pooled deviation [Def].
- **Build:** a consumer-disclosure utility model simulated with heterogeneous types; a WTA and WTP elicitation simulation with a built-in endowment bias, the two-sample test and effect size; a firm-strategy simulation of personalisation against churn after a breach. All data synthetic. [local]
- **Gap-fills:** *[inferred: Acquisti, John and Loewenstein 2013 (in the source's references); Acquisti, Taylor and Wagman 2016, recalled, not checked]* the privacy paradox literature.

**Assignment A8.10** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What does the endowment effect predict about willingness to accept (WTA) and willingness to pay (WTP) for the same data?

(A) WTA is below WTP  
(B) WTA exceeds WTP  
(C) They are equal  
(D) Neither can be measured

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Stated and revealed privacy preferences often diverge  
(B) A two-sample test can compare elicited WTA and WTP  
(C) Effect size can be summarised as the mean difference over the pooled standard deviation  
(D) Firms never gain from committing to privacy protection

**Q3 (2 marks, numerical answer).** Mean WTA is 40 and mean WTP is 25 with a pooled standard deviation of 20. What is the standardised effect size?

**Q4 (2 marks, prove or derive; every step with its reason).** Show in a simple model that if the benefit of personalisation is b and the expected privacy cost is c(q) which falls when the firm's protection level q rises, the set of consumers who disclose grows with q.

**Q5 (3 marks, programming).** Simulate a consumer-disclosure model with heterogeneous types, a WTA and WTP elicitation with a built-in endowment bias with the test and effect size, and a firm-strategy simulation of personalisation against churn after a breach. All data synthetic.

<details><summary>Key for A8.10 (open only after your attempt)</summary>

- **Q1:** B. People value what they hold more than what they would buy.
- **Q2:** A, B, C. Commitment to protection can raise disclosure and revenue in simple models.
- **Q3:** 0.75 (tolerance ±0.001). The effect size is 15 over 20 = 0.75.
- **Q4 (marking outline):** A consumer discloses when b exceeds c(q); as q rises c(q) falls, so any consumer who disclosed at the lower q still discloses and more consumers satisfy b greater than c; the disclosing set is monotone in q.
- **Q5 (what a passing submission shows):** A model whose disclosure rate rises with protection, a test that detects the planted bias, and a strategy comparison with sensitivity.

</details>


# PART C. DISTRIBUTED SYSTEMS, STORAGE AND DATABASES

## D9. Distributed systems: models, randomised and peer-to-peer algorithms, time, coordination, consensus, consistency, transactions, recovery and blockchains

Aim: four source courses (an advanced course that starts from gossip, a cloud-and-distributed-systems course, a classical-algorithms course and the distributed halves of the big-data course) merged into one dependency-ordered sequence. Every algorithm is run, not only analysed: a single deterministic discrete-event simulator (DSim, built in U9.1) provides message delay, loss, reordering, crashes and partitions with a seeded random number generator, so that safety properties are checked as invariants over thousands of random schedules and liveness is measured. The bridges (models and partial orders, tail bounds, transactions) appear just before the first unit that needs them. Benchmarks (recalled, not checked): Lynch, *Distributed Algorithms*; Attiya and Welch, *Distributed Computing*; Tel, *Introduction to Distributed Algorithms*; Kshemkalyani and Singhal, *Distributed Computing: Principles, Algorithms and Systems*; Coulouris et al., *Distributed Systems: Concepts and Design*; Raynal, *Distributed Algorithms for Message-Passing Systems*; Kleppmann, *Designing Data-Intensive Applications*; Mitzenmacher and Upfal, *Probability and Computing*. The source for ADS lists "classic research papers" as its references, so each unit that cites an industry system names the paper to read.

### U9.1 Bridge: models of distributed computation, partial orders and the DSim simulator
**Sources:** DS W1, o; ADS o
- **Topics:** What a distributed system is: components on networked computers that coordinate only by passing messages, with no shared memory and no common clock; the introduction to distributed systems and message passing as the programming model; distributed models: synchronous, asynchronous and partially synchronous timing; reliable, FIFO and lossy channels; crash, omission and Byzantine failure; the safety versus liveness distinction and invariants; executions as event sequences, the happened-before relation as a partial order, linear extensions, consistent cuts and the lattice of cuts (the order theory needed for U9.6 and U9.7); the course arc of the advanced course (epidemic and gossip algorithms, peer-to-peer networks and distributed hash tables, then the theory of time, consensus and consistency, then industry systems) and its stated assumption of data structures and operating systems. Outline map (the named topics of the course outlines and where this curriculum teaches them): distributed hash tables (U9.5), the Google File System and HDFS (U10.2), Spark (U11.4), vector clocks (U9.6), distributed leader election (U9.10), the FLP result (U9.12), the CAP theorem (U9.16), commit protocols (U9.18), Bitcoin and blockchains (U9.21), distributed file systems (U10.2), and distributed programming languages, treated here: the actor model (Erlang and Akka style), communicating-sequential-process channels, remote procedure call and dataflow languages, with a small actor runtime built on DSim as the exercise. The common goal of the components in a distributed application, and the intimate knowledge of how things work in a distributed environment, are the stated outcomes.
- **Results:** The happened-before relation is a strict partial order [P]; the consistent cuts of an execution form a distributive lattice under union and intersection [P]; in an asynchronous model no algorithm can distinguish a crashed process from a slow one [D]; a safety property is violated by a finite prefix while a liveness property cannot be [Def].
- **Build:** DSim: an event-heap simulator with seeded delay distributions, message loss and duplication, process crash and restart, network partition schedules and a trace recorder; an invariant checker run after every event; a test algorithm (echo with termination) with a trace printer that draws the space-time diagram. [local]
- **Gap-fills:** *[inferred: Lynch Ch.2; Lamport 1978, recalled, not checked]* the I/O-automaton formalism (named only); model-checking small protocols with TLA+ (read-only tooling, optional).

**Assignment A9.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** In an asynchronous system with crash failures, why can a process not tell a crashed peer from a slow one?

(A) Messages are always lost  
(B) There is no bound on message delay or processing speed, so silence proves nothing  
(C) Clocks are perfectly synchronised  
(D) Crashed processes send a final message

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) The happened-before relation is a strict partial order  
(B) Two events can be concurrent  
(C) A safety property can be violated by a finite prefix of an execution  
(D) A liveness property can be violated by a finite prefix

**Q3 (2 marks, numerical answer (cuts)).** Two processes have no messages between them and each has 3 events. How many consistent cuts does the execution have?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that the happened-before relation is a strict partial order: it is irreflexive and transitive.

**Q5 (3 marks, programming).** Build DSim: a seeded discrete-event simulator with a priority queue of events, per-link delay, loss and duplication models, crash and partition injection, and an invariant checker. Test it on an echo protocol and show that equal seeds give identical traces.

<details><summary>Key for A9.1 (open only after your attempt)</summary>

- **Q1:** B. With no timing bound, no finite wait distinguishes the two.
- **Q2:** A, B, C. A liveness property cannot be violated by any finite prefix since it can always still be satisfied later.
- **Q3:** 16 cuts (tolerance ±0). With no messages any pair of prefixes is consistent, giving 4 times 4 = 16.
- **Q4 (marking outline):** Happened-before is the transitive closure of program order and send-before-receive; transitivity holds by construction; irreflexivity holds because an execution is a real sequence in which each step follows the earlier ones, so an event cannot precede itself (a cycle would require an event to occur before its own occurrence).
- **Q5 (what a passing submission shows):** A deterministic simulator whose traces are identical for equal seeds, injection that changes traces as configured, and an invariant checker that reports a planted violation.

</details>

### U9.2 Bridge: tail bounds, balls into bins and randomised-algorithm analysis
**Sources:** DS W6
- **Topics:** Distributed randomized algorithms (the randomisation half of the source's Week 6): Chernoff bounds for sums of independent indicators (multiplicative and additive forms); the balls-into-bins model, maximum load with n balls in n bins (Θ(log n / log log n)) and the two-choices improvement (Θ(log log n)); coupon collector; expectation by linearity; Markov chains for random walks on graphs and their mixing (introduced here, used in U9.3 and U11.10); randomised symmetry breaking and its use in leader election and in load balancing; with-high-probability statements.
- **Results:** Chernoff: for X a sum of independent Bernoulli variables with mean μ, P[X ≥ (1 + δ)μ] ≤ exp(−δ²μ/(2 + δ)) [P]; the coupon collector needs about n ln n draws in expectation [P]; with n balls in n bins the maximum load is at most 3 ln n / ln ln n with high probability [P]; with two random choices per ball the maximum load is ln ln n / ln 2 + O(1) [X, stated with simulation].
- **Build:** Monte Carlo for balls-into-bins with one and two choices against the predicted loads; coupon-collector estimates; a random-walk mixing-time estimator on a ring, a grid and an expander-like random regular graph. [local]
- **Gap-fills:** *[inferred: Mitzenmacher–Upfal Ch.3–5, recalled, not checked]* power of two choices as the basis of load-balancing in cloud schedulers.

**Assignment A9.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Roughly how many draws does the coupon collector need in expectation to see all n coupons?

(A) n  
(B) n ln n  
(C) n squared  
(D) ln n

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Chernoff bounds give exponentially small tails for sums of independent indicators  
(B) With n balls in n bins the maximum load is of order log n over log log n with high probability  
(C) Two random choices per ball reduce the maximum load to order log log n  
(D) Chernoff bounds hold for arbitrarily dependent indicators

**Q3 (2 marks, numerical answer (draws)).** What is the expected number of draws for the coupon collector with n = 100 coupons (to the nearest whole number)?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that the expected number of draws for the coupon collector with n coupons is n times the n-th harmonic number.

**Q5 (3 marks, programming).** Simulate the coupon collector, balls into bins with one and with two choices, and a Chernoff bound check on binomial tails. Plot or tabulate the measured maximum load against the predicted orders and the empirical tail against the bound.

<details><summary>Key for A9.2 (open only after your attempt)</summary>

- **Q1:** B. The expectation is n times the n-th harmonic number, about n ln n.
- **Q2:** A, B, C. Independence, or a suitable negative dependence, is needed.
- **Q3:** 518.7 draws (tolerance ±1). n times H(100) is 100 times 5.187, about 519.
- **Q4 (marking outline):** When i coupons are already held, the next new coupon appears with probability (n minus i)/n, so the wait is geometric with mean n/(n minus i); summing over i from 0 to n minus 1 and using linearity gives n times the sum of 1/k for k from 1 to n.
- **Q5 (what a passing submission shows):** Measured expectations close to n H(n), maximum loads that follow the predicted growth, and bounds that always lie above the empirical tail.

</details>

### U9.3 Epidemic and gossip-based algorithms
**Sources:** ADS W1
- **Topics:** Epidemic and gossip based algorithms: push, pull and push-pull rumour spreading, anti-entropy and rumour mongering, the SI and SIR epidemic models, membership and failure detection by gossip (SWIM-style), aggregation by gossip (averaging, counting), gossip in industry (Cassandra's membership, Amazon's anti-entropy), message cost and the fan-out parameter.
- **Results:** Push gossip informs all n nodes in log₂ n + ln n + O(1) rounds with high probability [S]; in pull, once half the nodes are informed the uninformed fraction squares each round, so the tail takes O(log log n) rounds [D]; push–pull needs O(log log n) message-rounds per node [S]; gossip averaging converges geometrically at a rate set by the second-largest eigenvalue of the mixing matrix [D].
- **Build:** push, pull and push-pull simulators in DSim with the round counts measured against n; a gossip-averaging experiment on three topologies; a SWIM-style failure detector with a measured false-positive rate against the probe parameters. [local]
- **Gap-fills:** *[inferred: Demers et al. 1987; Das–Gupta–Motivala, SWIM 2002, recalled, not checked]* Cassandra's gossiper described in the primary system paper (continues in U10.4).

**Assignment A9.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** In push gossip, roughly how many rounds are needed to inform all n nodes with high probability?

(A) log2 n plus ln n  
(B) n  
(C) square root of n  
(D) a constant

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) In pull gossip, once half the nodes are informed the uninformed fraction roughly squares each round  
(B) Gossip averaging converges at a rate set by the second-largest eigenvalue modulus of the mixing matrix  
(C) The fan-out parameter trades message cost against speed  
(D) Gossip needs a global coordinator

**Q3 (2 marks, numerical answer (rounds)).** Using log2 n plus ln n, how many rounds does push gossip need for n = 1024 nodes (two decimals)?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that in pull gossip, if a fraction u of nodes is uninformed at the start of a round, the expected uninformed fraction after the round is u squared.

**Q5 (3 marks, programming).** Implement push, pull and push-pull gossip in DSim, a gossip averaging experiment on a ring, a random graph and a complete graph, and a SWIM-style failure detector with indirect probes. Measure rounds against n and the false-positive rate against the probe parameters.

<details><summary>Key for A9.3 (open only after your attempt)</summary>

- **Q1:** A. Push gossip needs about log2 n + ln n + O(1) rounds.
- **Q2:** A, B, C. Gossip is decentralised.
- **Q3:** 16.93 rounds (tolerance ±0.01). 10 + 6.93 = 16.93.
- **Q4 (marking outline):** A node stays uninformed only if the node it contacts is uninformed; that has probability u; so the expected uninformed fraction is u times u.
- **Q5 (what a passing submission shows):** Round counts that follow the predicted growth, convergence rates ordered by topology, and a detector whose false positives fall as indirect probes are added.

</details>

### U9.4 Unstructured peer-to-peer systems: Napster, Gnutella, FastTrack and BitTorrent
**Sources:** ADS W2–3; CCDS W7; DS W6
- **Topics:** Napster and Gnutella; Peer to Peer systems in cloud computing: Napster, Gnutella, FastTrack, BitTorrent (the P2P half of Week 6 in the classical-algorithms course); the architecture of a central index versus flooding, TTL-limited flooding, random walks and their message cost, super-peers (FastTrack), the incentives problem and free riding; BitTorrent: torrent files, trackers, piece selection (rarest first), choking and optimistic unchoking (tit-for-tat), and the swarm's throughput and fairness.
- **Results:** A TTL-limited flood on a graph of average degree d reaches up to d^TTL nodes at message cost proportional to the edges visited, so the cost per found item rises with network size [D]; random walks find an item replicated on r of n nodes in about n/r expected steps and k parallel walks divide that by k [D]; rarest-first maximises the minimum piece replication in a closed swarm [S].
- **Build:** a Gnutella-style flooding and random-walk search on a random graph in DSim with message counts against replication; a BitTorrent swarm model with rarest-first versus random piece selection and tit-for-tat unchoking, comparing download time and fairness. [local]
- **Gap-fills:** *[inferred: Cohen 2003; Lv et al., Search and replication in unstructured peer-to-peer networks, recalled, not checked]* the legal and design history of the first systems (context only).

**Assignment A9.4** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Why does Gnutella-style flooding scale poorly?

(A) It uses a central index  
(B) The message cost grows with the number of edges visited for each query  
(C) It encrypts all messages  
(D) It cannot find popular items

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) A random walk finds an item replicated on r of n nodes in about n/r expected steps  
(B) k independent walks divide the expected time by about k  
(C) Rarest-first piece selection helps keep every piece available in a swarm  
(D) Napster stored the files on the central server

**Q3 (2 marks, numerical answer (steps)).** An item is replicated on 50 of 10000 nodes. How many expected steps does one random walk need, and so how many for 10 parallel walks?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that a random walk that lands on a uniformly random node at each step finds an item replicated on r of n nodes in n/r expected steps.

**Q5 (3 marks, programming).** Build a peer-to-peer simulator in DSim with flooding with TTL, random walks, and a BitTorrent-style swarm with rarest-first and random piece selection. Compare message cost per hit and swarm completion times.

<details><summary>Key for A9.4 (open only after your attempt)</summary>

- **Q1:** B. Cost per query grows with the visited part of the network.
- **Q2:** A, B, C. Napster used a central index while files stayed at peers.
- **Q3:** 20 steps (tolerance ±0.5). One walk needs 200 steps, ten walks about 20.
- **Q4 (marking outline):** Each step succeeds with probability r/n independently, so the number of steps is geometric with mean n/r.
- **Q5 (what a passing submission shows):** Costs that grow with network size for flooding, walk times that follow n/r, and rarest-first finishing sooner than random selection on skewed starts.

</details>

### U9.5 Distributed hash tables: Chord, Pastry and Kelips
**Sources:** ADS W3; CCDS W7; DS W6
- **Topics:** DHTs: Chord, Pastry and BitTorrent (the DHT part of the third week of the advanced course); DHT, Chord, Pastry and Kelips (the cloud-course week on P2P systems in industry); consistent hashing and its virtual nodes; the Chord ring, finger tables, lookup, join, stabilisation and failure handling by successor lists; Pastry's prefix routing tables and leaf sets; Kelips' affinity groups with constant-hop lookup and gossip-maintained tables (the gossip of U9.3 reused); the trade between routing state, hop count and maintenance traffic; DHT and P2P computing as the source's Week 6 title.
- **Results:** In Chord, a lookup takes O(log n) hops with high probability, and with log n virtual nodes per server the load imbalance is O(1) [P]; the ring stays correct if every node's successor pointer is right, and stabilisation repairs concurrent joins [S]; a node's departure moves only the keys it owned, about 1/n of the total [P]; Kelips uses O(√n) state per node for one-hop lookups [D].
- **Build:** consistent hashing with virtual nodes and the measured imbalance; Chord with finger tables, joins, leaves and crashes in DSim, with the O(log n) hop count measured; a Pastry-style prefix router; a Kelips table with gossip. [local]
- **Gap-fills:** *[inferred: Stoica et al., Chord 2001; Rowstron–Druschel 2001; Gupta et al., Kelips 2003, recalled, not checked]* Kademlia and its use in BitTorrent's DHT.

**Assignment A9.5** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** In Chord, about how many hops does a lookup take with high probability in a network of n nodes?

(A) O(1)  
(B) O(log n)  
(C) O(n)  
(D) O(n squared)

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) When a node leaves, only the keys it owned move, about 1/n of the total  
(B) Virtual nodes reduce load imbalance  
(C) The ring is correct if every successor pointer is correct  
(D) Kelips needs only logarithmic state per node

**Q3 (2 marks, numerical answer (keys)).** A Chord ring of 100 nodes holds 1,000,000 keys uniformly. How many keys move in expectation when one node leaves?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that if the successor pointers of all nodes are correct then a lookup by successor-walking returns the correct owner of a key, and that finger tables only shorten the path.

**Q5 (3 marks, programming).** Implement Chord in DSim with finger tables, join, stabilisation and virtual nodes, test lookups under churn, and implement a Kelips-style grouped lookup. Measure hop counts, load imbalance and the effect of virtual nodes.

<details><summary>Key for A9.5 (open only after your attempt)</summary>

- **Q1:** B. Finger tables halve the remaining distance at each hop.
- **Q2:** A, B, C. Kelips uses about the square root of n state per node for one-hop lookups.
- **Q3:** 10000 keys (tolerance ±0.5). The leaving node held about 1/100 of the keys, 10,000.
- **Q4 (marking outline):** The owner of a key is the first node clockwise at or after the key; stepping to successors passes each node in ring order and stops at the first node whose identifier is at or beyond the key, which is the owner; fingers only skip over nodes that precede the key, so they never overshoot.
- **Q5 (what a passing submission shows):** Hop counts that grow as log n, a ring that repairs after concurrent joins, load imbalance that falls with virtual nodes, and Kelips lookups that complete in one hop.

</details>

### U9.6 Time, clocks and causality: synchronisation, Lamport clocks and vector clocks
**Sources:** DS W1–2; CCDS W4; ADS W4
- **Topics:** Causality and logical time; Logical time (Week 2); Logical clocks (the advanced course's Week 4); Time and clock synchronization in cloud data centers: synchronization in the cloud and its key challenges, clock skew and clock drift, external and internal synchronisation, Cristian's algorithm (the source spells it Christians algorithm) and its error bound, the Network Time Protocol (NTP), Berkeley's algorithm (the source: Berkley's), the Datacenter time protocol (DTP); logical (Lamport) ordering, Lamport timestamps and the clock condition, vector timestamps and their characterisation of causality, matrix clocks (named), version vectors for replicated data (the form used in U10.3).
- **Results:** Cristian's algorithm has error at most half the round-trip time minus the minimum one-way delay [D]; for Lamport clocks, e → e′ implies L(e) < L(e′) but not conversely [P]; vector clocks satisfy e → e′ iff V(e) < V(e′) componentwise [P]; any clock that characterises causality needs at least n entries in the worst case (Charron-Bost) [X].
- **Build:** a drifting-clock model with Cristian, Berkeley and an NTP-like filter, measuring the error against delay asymmetry; Lamport and vector clocks in DSim with a causality-checker over random executions; a version-vector conflict detector. [local]
- **Gap-fills:** *[inferred: Lamport 1978; Mattern 1989 and Fidge 1988, recalled, not checked]* hybrid logical clocks (named, used in some databases).

**Assignment A9.6** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** If event a happened before event b, what do Lamport clocks guarantee?

(A) L(a) is less than L(b)  
(B) L(a) equals L(b)  
(C) L(b) is less than L(a)  
(D) Nothing

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Vector clocks characterise causality exactly  
(B) Lamport clocks cannot tell concurrency from order  
(C) A clock that characterises causality needs at least n entries in the worst case  
(D) Cristian's algorithm gives exact time

**Q3 (2 marks, numerical answer (ms)).** Cristian's algorithm has a round trip of 40 ms and the minimum one-way delay is 8 ms. What is the largest possible error in ms?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that for vector clocks event e happened before f if and only if V(e) is componentwise at most V(f) and different from it.

**Q5 (3 marks, programming).** Implement Cristian's and Berkeley's algorithms, Lamport clocks and vector clocks in DSim with drifting clocks, and a checker that compares each clock's verdict with the true happened-before order on random executions.

<details><summary>Key for A9.6 (open only after your attempt)</summary>

- **Q1:** A. But L(a) less than L(b) does not imply that a happened before b.
- **Q2:** A, B, C. It only bounds the error.
- **Q3:** 12 ms (tolerance ±0.1). The bound is half the round trip minus the minimum one-way delay: 20 minus 8 = 12.
- **Q4 (marking outline):** If e precedes f then every update chain that reached e is also seen by f, so each entry of V(f) is at least that of V(e), and the entry of e's process is strictly larger since f has seen e or a later event; conversely if V(e) is at most V(f) and differs, the entry of e's process is at least the value at e, which can only have reached f through a message chain from e.
- **Q5 (what a passing submission shows):** Bounded synchronisation error, Lamport clocks that miss concurrency, and vector clocks that agree with the ground truth on every pair.

</details>

### U9.7 Global state and termination detection: the Chandy–Lamport snapshot
**Sources:** DS W2,5; CCDS W4
- **Topics:** Global State & Snapshot; Global state and snapshot recording algorithms: the issues in recording a global state, the model of communication (FIFO channels), consistent and inconsistent cuts, the Chandy–Lamport snapshot algorithm with markers; use cases (stable-property detection, checkpointing); termination detection (Week 5): the diffusing-computation model, the Dijkstra–Scholten algorithm, the weight-throwing algorithm, and a termination detector by snapshot.
- **Results:** The state recorded by Chandy–Lamport is a consistent global state, reachable from the initial state and from which the final state is reachable, although it may never have occurred [P]; a stable property true in the recorded state remains true thereafter [P]; Dijkstra–Scholten detects termination with one control message per basic message [D].
- **Build:** Chandy–Lamport on a token-passing bank-transfer system in DSim with the conservation invariant checked on every snapshot; Dijkstra–Scholten and weight-throwing detectors with a test that they never announce early. [local]
- **Gap-fills:** *[inferred: Chandy–Lamport 1985; Dijkstra–Scholten 1980, recalled, not checked]* snapshots with non-FIFO channels (named).

**Assignment A9.7** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What does the Chandy-Lamport snapshot require of channels?

(A) They must be non-FIFO  
(B) They must be FIFO  
(C) They must be lossy  
(D) They must be synchronous

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) The recorded state is consistent and reachable from the initial state  
(B) The recorded state may never have occurred in the actual execution  
(C) A stable property true in the snapshot stays true afterwards  
(D) The algorithm halts the computation to record the state

**Q3 (2 marks, numerical answer (messages)).** In a complete network of 6 processes, how many marker messages does a Chandy-Lamport snapshot send (one on each directed channel)?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that the Chandy-Lamport snapshot never records a message as received without also recording it as sent.

**Q5 (3 marks, programming).** Implement the Chandy-Lamport snapshot on a token-passing bank transfer simulation with FIFO channels in DSim and check conservation of total money in every snapshot, then implement Dijkstra-Scholten termination detection and count control messages.

<details><summary>Key for A9.7 (open only after your attempt)</summary>

- **Q1:** B. Marker placement relies on FIFO order.
- **Q2:** A, B, C. The computation continues during the snapshot.
- **Q3:** 30 messages (tolerance ±0). Each of the n(n minus 1) directed channels carries one marker: 30.
- **Q4 (marking outline):** A process records its state before sending a marker on a channel, and the receiver records the channel as the messages arriving before the marker; a message received before the receiver's own recording was sent before the sender recorded, because FIFO delivers it ahead of the marker that follows; so it is part of the sender's recorded sent set.
- **Q5 (what a passing submission shows):** Snapshots whose recorded balances plus in-channel amounts always sum to the total, and termination detection with control messages equal to basic messages.

</details>

### U9.8 Distributed mutual exclusion: permission-based, quorum-based and token-based algorithms
**Sources:** DS W2–3; CCDS W4; ADS W4
- **Topics:** Distributed Mutual Exclusion, non-token and quorum-based approaches (Week 2) and token-based approaches (Week 3); Mutual Exclusion in Cloud (the cloud course's Week 4): the central algorithm, ring-based, Lamport's algorithm, the Ricart–Agrawala algorithm, quorum-based mutual exclusion and Maekawa's algorithm with the problem of handling deadlocks, token-based algorithms (Suzuki–Kasami broadcast, Raymond's tree), and industry mutual exclusion: Chubby (continued in U9.15); Mutual Exclusion Algorithms as the advanced course lists them; performance measures (messages per entry, synchronisation delay, fairness).
- **Results:** Lamport's algorithm uses 3(n − 1) messages per entry and Ricart–Agrawala 2(n − 1) [D]; Ricart–Agrawala satisfies mutual exclusion and is deadlock-free by timestamp order [P]; Maekawa's algorithm uses quorums of size about √n, with 3√n to 5√n messages, any two of which intersect [P, intersection by projective-plane or grid construction]; Suzuki–Kasami uses at most n messages per entry [D]; Raymond's algorithm uses O(log n) messages on a balanced tree [D].
- **Build:** all of the above in DSim with the safety invariant (never two in the critical section) checked over randomised schedules and the message counts compared with the formulas; a grid-quorum generator with an intersection test; Maekawa's deadlock reproduced and then fixed by the inquire and relinquish messages. [local]
- **Gap-fills:** *[inferred: Ricart–Agrawala 1981; Maekawa 1985; Raymond 1989, recalled, not checked]* mutual exclusion with leases in industry (U9.15).

**Assignment A9.8** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** How many messages does Ricart-Agrawala use per critical-section entry among n processes?

(A) n  
(B) 2(n minus 1)  
(C) 3(n minus 1)  
(D) n squared

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Lamport's algorithm uses 3(n minus 1) messages per entry  
(B) Maekawa's algorithm uses quorums of size about the square root of n  
(C) Suzuki-Kasami uses at most n messages per entry  
(D) Any two quorums in Maekawa's scheme may be disjoint

**Q3 (2 marks, numerical answer (messages)).** With n = 8 processes, how many messages does Ricart-Agrawala send in total for 20 critical-section entries?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that Ricart-Agrawala guarantees mutual exclusion.

**Q5 (3 marks, programming).** Implement Lamport, Ricart-Agrawala, Maekawa with a grid quorum, Suzuki-Kasami and Raymond algorithms in DSim with a safety checker for mutual exclusion and measure messages per entry against n.

<details><summary>Key for A9.8 (open only after your attempt)</summary>

- **Q1:** B. Each entry sends n minus 1 requests and receives n minus 1 replies.
- **Q2:** A, B, C. Quorums must intersect.
- **Q3:** 280 messages (tolerance ±0). Each entry costs 2 times 7 = 14 messages, so 280.
- **Q4 (marking outline):** Suppose two processes are in the critical section at once; each must have received a reply from the other; a process replies to a request only if it is not requesting or has a larger timestamp; of the two requests one timestamp is smaller, and the process with the larger timestamp would have deferred its reply, a contradiction.
- **Q5 (what a passing submission shows):** No violation on random schedules, message counts that match the formulas, and a plot or table of the growth in n.

</details>

### U9.9 Distributed deadlock detection and distributed shared memory
**Sources:** DS W4
- **Topics:** Deadlock detection: the wait-for graph and the resource, AND and OR request models, distributed detection by edge chasing (Chandy–Misra–Haas) and by global snapshot, false deadlocks (phantoms) and why they arise; DSM: distributed shared memory: the abstraction, page-based and object-based designs, coherence protocols (write-invalidate versus write-update), consistency models for shared memory (sequential, release, causal), false sharing, and the link to the consistency models of U9.16.
- **Results:** In the AND model a deadlock exists iff the wait-for graph has a cycle [P]; Chandy–Misra–Haas edge chasing detects a cycle when a probe returns to its initiator, with at most m(n − 1)/2 messages for m processes spread over n sites (bound recalled, not checked) [D]; sequential consistency of a page protocol follows from single-writer–multiple-reader invariants [S].
- **Build:** a distributed wait-for-graph simulator with edge-chasing probes and a test that never reports a false cycle in a consistent snapshot; an IVY-style page-ownership protocol in DSim with a coherence checker. [local]
- **Gap-fills:** *[inferred: Chandy–Misra–Haas 1983; Li–Hudak 1989, recalled, not checked]* deadlock handling in database lock managers (U9.17).

**Assignment A9.9** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** In the AND model, when is a distributed system deadlocked?

(A) When the wait-for graph has a cycle  
(B) When any process waits  
(C) When there are no resources  
(D) When a message is lost

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Edge chasing detects a cycle when a probe returns to its initiator  
(B) Probe messages carry the initiator, sender and receiver identifiers  
(C) Phantom deadlocks can arise from inconsistent snapshots of the wait-for graph  
(D) Distributed shared memory requires no coherence protocol

**Q3 (2 marks, numerical answer (messages)).** Using the bound m(n minus 1)/2 for m processes over n sites, what is the most messages Chandy-Misra-Haas needs for m = 10 processes over n = 4 sites?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that in the AND model a deadlock exists if and only if the wait-for graph contains a cycle.

**Q5 (3 marks, programming).** Implement Chandy-Misra-Haas edge chasing in DSim over random wait-for graphs spread over sites and compare with a central detector, then implement a single-writer multiple-reader page-based distributed shared memory and test sequential consistency on random access patterns.

<details><summary>Key for A9.9 (open only after your attempt)</summary>

- **Q1:** A. A cycle in the wait-for graph is necessary and sufficient in the AND model.
- **Q2:** A, B, C. A coherence protocol is needed.
- **Q3:** 15 messages (tolerance ±0). The bound gives 10 times 3 over 2 = 15.
- **Q4 (marking outline):** If there is a cycle, each process in it waits for the next, none can proceed, so all are deadlocked; if processes are deadlocked each waits for another deadlocked one, so following wait-for edges from a deadlocked process never ends in a running process, and in a finite graph a walk that never stops must repeat a node, which closes a cycle.
- **Q5 (what a passing submission shows):** Deadlocks detected exactly where the cycles exist, no false detections on acyclic graphs, and shared memory histories that pass a sequential-consistency check.

</details>

### U9.10 Leader election: rings, the bully algorithm and their industry use
**Sources:** DS W1; ADS W5; CCDS W3
- **Topics:** Leader Election (the first week of the classical-algorithms course); Distributed Leader Election (the advanced course's fifth week); Leader Election in Rings: the LeLann–Chang–Roberts (LCR) algorithm and the Hirschberg and Sinclair (HS) algorithm; Ring based and Bully based leader election and the leader election problem statement; leader election in industry systems: Google's Chubby and Apache Zookeeper (taught in U9.15); election under failure and the role of a failure detector; lower bound for comparison-based election on a ring.
- **Results:** LCR elects the maximum-identifier node with O(n²) messages in the worst case (n(n + 1)/2 on a decreasing ring) and 2n − 1 on an increasing ring (each identifier smaller than its successor's: n − 1 messages swallowed at once plus n for the maximum), in n rounds [D]; HS uses O(n log n) messages [P]; any comparison-based election on a ring needs Ω(n log n) messages [X]; the bully algorithm elects the highest live identifier with O(n²) messages in the worst case [D].
- **Build:** LCR, HS and bully in DSim with message counts against n and the worst-case input; a failure-detector-assisted election with a stability measure after repeated crashes. [local]
- **Gap-fills:** *[inferred: LeLann 1977; Chang–Roberts 1979; Hirschberg–Sinclair 1980, recalled, not checked]* Franklin's and Peterson's algorithms (named).

**Assignment A9.10** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** How many messages does LCR need on a ring of n nodes whose identifiers decrease around the ring in the direction of sending?

(A) n  
(B) n(n plus 1)/2  
(C) n log n  
(D) 2n

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) LCR elects the node with the maximum identifier  
(B) The HS algorithm uses O(n log n) messages  
(C) Any comparison-based election on a ring needs on the order of n log n messages in the worst case  
(D) The bully algorithm uses O(n) messages in the worst case

**Q3 (2 marks, numerical answer (messages)).** In the worst case, how many messages does LCR use on a ring of 20 nodes?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that LCR elects exactly one leader, the node with the largest identifier.

**Q5 (3 marks, programming).** Implement LCR, HS, the bully algorithm and a lease-based leader election in DSim, count messages on worst-case and random rings, test with crashes during election, and compare with the counts predicted.

<details><summary>Key for A9.10 (open only after your attempt)</summary>

- **Q1:** B. Each identifier travels until it meets a larger one; the sum is n(n plus 1)/2 in the worst case.
- **Q2:** A, B, C. The bully algorithm uses O(n squared) messages in the worst case.
- **Q3:** 210 messages (tolerance ±0). n(n plus 1)/2 = 210.
- **Q4 (marking outline):** A node forwards an identifier only if it is larger than its own, so the maximum identifier is never swallowed and travels the whole ring back to its owner who declares itself leader; every other identifier is dropped by the maximum's owner at the latest, so no other node sees its own identifier return.
- **Q5 (what a passing submission shows):** Message counts matching n(n plus 1)/2 on the worst case and growing as n log n for HS, and exactly one leader on every run.

</details>

### U9.11 Distributed minimum spanning tree: the Gallager–Humblet–Spira algorithm
**Sources:** DS W4; ADS W6
- **Topics:** Distributed MST (Week 4 of the classical-algorithms course) and Distributed minimum spanning tree (the advanced course's Week 6, with the FLP result, which follows in U9.12): the MST problem, the cut and cycle properties, Borůvka-style fragment merging, the Gallager–Humblet–Spira (GHS) algorithm: fragments, levels, cores, the Connect, Initiate, Test, Accept, Reject, Report and Change-root messages; why unique edge weights are assumed.
- **Results:** The cut property: the lightest edge crossing any cut belongs to the MST when weights are distinct [P]; GHS builds the MST using at most 5n log₂ n + 2m messages [D]; every GHS level-L fragment has at least 2^L nodes [P].
- **Build:** GHS in DSim on random weighted graphs, with the MST compared against Kruskal and the message count against the bound. [local]
- **Gap-fills:** *[inferred: Gallager–Humblet–Spira 1983, recalled, not checked]* MST in the CONGEST model (named).

**Assignment A9.11** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What does the cut property say about the minimum spanning tree when edge weights are distinct?

(A) The heaviest edge across any cut is in the tree  
(B) The lightest edge across any cut is in the tree  
(C) No edge across a cut is in the tree  
(D) All edges across a cut are in the tree

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) GHS builds fragments that merge by their minimum outgoing edges  
(B) GHS uses at most about 5 n log n plus 2 m messages  
(C) A level-L fragment contains at least 2 to the power L nodes  
(D) GHS needs a global clock

**Q3 (2 marks, numerical answer (messages)).** What is the GHS message bound 5 n log2 n plus 2 m for n = 16 nodes and m = 40 edges?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove the cut property for distinct weights.

**Q5 (3 marks, programming).** Implement GHS in DSim on random weighted graphs, compare the tree with Kruskal's, check the fragment-size lemma on every run and compare the message counts with the bound.

<details><summary>Key for A9.11 (open only after your attempt)</summary>

- **Q1:** B. The lightest edge crossing a cut belongs to the unique minimum spanning tree.
- **Q2:** A, B, C. GHS is asynchronous and needs no global clock.
- **Q3:** 400 messages (tolerance ±0). 5 times 16 times 4 = 320, plus 80, gives 400.
- **Q4 (marking outline):** Let e be the lightest edge across a cut and suppose a minimum spanning tree T lacks e; adding e to T creates a cycle that crosses the cut at another edge f; f is heavier than e; removing f gives a spanning tree of smaller weight, contradicting the minimality of T.
- **Q5 (what a passing submission shows):** A tree identical to Kruskal's on every graph, fragments of level L never smaller than 2 to the L, and counts below the bound.

</details>

### U9.12 Agreement and consensus, and the FLP impossibility result
**Sources:** ADS W6; DS W3; CCDS W5
- **Topics:** The FLP result (the advanced course's Week 6); Consensus & Agreement (Week 3 of the classical course); Consensus in Cloud Computing and Paxos, the issues in consensus: the consensus problem (agreement, validity, termination), consensus in synchronous and asynchronous systems, the Fischer–Lynch–Paterson (FLP) impossibility, the escape routes (randomisation, partial synchrony and failure detectors, weaker problems), the synchronous crash-fault algorithm and its f + 1 round bound, reliable broadcast as a building block.
- **Results:** FLP: no deterministic protocol solves consensus in an asynchronous system if even one process may crash [P, via bivalent initial configuration and the extension lemma]; synchronous crash-tolerant consensus needs f + 1 rounds and flooding achieves it [P]; Ben-Or's randomised protocol terminates with probability 1 when f < n/2 [S].
- **Build:** a synchronous flooding consensus under crashes; a DSim adversary that keeps a two-process protocol bivalent forever against the FLP argument; Ben-Or's randomised consensus with the expected number of rounds measured. [local]
- **Gap-fills:** *[inferred: Fischer–Lynch–Paterson 1985; Ben-Or 1983; Chandra–Toueg 1996, recalled, not checked]* unreliable failure detectors and the weakest detector for consensus (named).

**Assignment A9.12** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What does the FLP result say?

(A) Consensus is impossible in any system  
(B) No deterministic protocol solves consensus in an asynchronous system if even one process may crash  
(C) Consensus needs a majority to be up  
(D) Randomised protocols cannot terminate

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Synchronous crash-tolerant consensus with f crashes needs f plus 1 rounds  
(B) Flooding achieves the f plus 1 round bound  
(C) Ben-Or's protocol uses randomisation to terminate with probability 1  
(D) FLP also applies to synchronous systems

**Q3 (2 marks, numerical answer (messages)).** Flooding consensus runs for f plus 1 rounds. With n = 5 processes and f = 2, and every live process sending to all others each round, what is the maximum number of messages (n(n minus 1) per round)?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that in synchronous flooding with f plus 1 rounds at most f of which can contain a crash, all surviving processes end with the same set of values.

**Q5 (3 marks, programming).** Implement flooding consensus in DSim with crash injection at arbitrary points and verify agreement and validity with every f up to n minus 1; implement Ben-Or's protocol and measure the number of rounds to terminate against n.

<details><summary>Key for A9.12 (open only after your attempt)</summary>

- **Q1:** B. FLP is for deterministic protocols in the asynchronous crash model; randomisation and partial synchrony escape it.
- **Q2:** A, B, C. In a synchronous system consensus is solvable.
- **Q3:** 60 messages (tolerance ±0). Three rounds of 20 messages gives 60.
- **Q4 (marking outline):** With at most f crashes and f plus 1 rounds, at least one round has no crash; in that round every live process sends its whole set to all, and all live processes receive the same union, so the sets are identical after that round; later rounds add nothing different since all live processes have the same set to send; so all live processes decide on the same function of the set.
- **Q5 (what a passing submission shows):** Agreement and validity on every schedule tested, f plus 1 rounds exactly in the worst case and an observed termination distribution for Ben-Or.

</details>

### U9.13 Byzantine agreement, reliability measures: SLIs, SLOs and SLAs
**Sources:** ADS W9; CCDS W5
- **Topics:** Byzantine Agreement: agreement, faults, tolerance, measuring reliability and performance, SLIs, SLOs, SLAs, TLAs (the source's list ends with this abbreviation without expanding it; it is flagged in Appendix E and not interpreted here); Byzantine failure and the Byzantine Generals Problem; the Lamport–Shostak–Pease algorithm (oral messages OM(m)) and signed messages; the n ≥ 3f + 1 bound; practical Byzantine fault tolerance (PBFT) in outline; service-level indicators, objectives and agreements: how reliability is defined, measured and contracted, error budgets and nines of availability (the operational use is in U12.1).
- **Results:** Byzantine agreement among n processes with f traitors is impossible for n ≤ 3f in the oral-messages model [P]; OM(m) solves it for n ≥ 3m + 1, sending (n − 1) + (n − 1)(n − 2) + … + (n − 1)…(n − m − 1) messages in total, which is O(n^(m+1)) [P]; with unforgeable signatures any number of traitors can be tolerated in synchronous rounds with f + 1 rounds [S]; an availability of 99.9% allows about 8.76 hours of downtime a year and 99.99% about 52.6 minutes [D].
- **Build:** the OM(m) algorithm in DSim with traitorous behaviours, checking agreement and validity for all small (n, f) and showing the failure at n = 3f; a signed-messages version using your own signature from U5.17; an SLI computation over request logs with the SLO and error-budget calculation. [local]
- **Gap-fills:** *[inferred: Lamport–Shostak–Pease 1982; Castro–Liskov 1999, recalled, not checked]* the blockchain use of Byzantine tolerance (U9.21).

**Assignment A9.13** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** With oral messages and n processes among which f may be traitors, when is Byzantine agreement impossible?

(A) When n is at most 3f  
(B) When n exceeds 3f  
(C) When f is zero  
(D) When messages are signed

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) OM(m) solves agreement for n of at least 3m plus 1  
(B) With unforgeable signatures agreement can be reached with any number of traitors in a synchronous system  
(C) An SLO is an internal target for a service level indicator  
(D) An SLA has no consequences for the provider

**Q3 (2 marks, numerical answer (minutes)).** An SLO of 99.95 percent availability allows how many minutes of downtime in a 365-day year?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that three generals cannot reach Byzantine agreement with oral messages if one is a traitor.

**Q5 (3 marks, programming).** Implement OM(m) in DSim with traitors that send arbitrary values, check agreement and validity for n of at least 3m plus 1 on all traitor assignments, show the failure at n = 3 and count messages. Add an SLO error-budget calculator from an availability log.

<details><summary>Key for A9.13 (open only after your attempt)</summary>

- **Q1:** A. Oral-message agreement needs n of at least 3f plus 1.
- **Q2:** A, B, C. An SLA is a contract that usually specifies penalties.
- **Q3:** 262.8 minutes (tolerance ±0.5). 0.0005 times 525,600 minutes = 262.8.
- **Q4 (marking outline):** With a commander and two lieutenants, lieutenant 1 receives attack from the commander and hears that lieutenant 2 was told retreat; this is the same for lieutenant 1 whether the commander is a traitor who told different things or lieutenant 2 is a traitor who lies about what he was told; lieutenant 1 must obey a loyal commander so must attack in the second case, and by symmetry the same view in the first case forces attack while lieutenant 2 retreats, breaking agreement.
- **Q5 (what a passing submission shows):** Agreement and validity in all tested cases for n of at least 3m plus 1, a reproduced failure for n of 3, total messages matching the sum formula, and a correct budget report.

</details>

### U9.14 Replicated state machines: Paxos and Raft
**Sources:** ADS W8; CCDS W5
- **Topics:** Paxos and Raft (the advanced course's Week 8); Consensus, Paxos and Recovery in Clouds, Paxos Algorithm: replicated state machines and the replicated log; single-decree Paxos (proposers, acceptors, learners; prepare/promise and accept/accepted phases; ballot numbers), Multi-Paxos with a stable leader; Raft: terms, leader election by randomised timeouts, log replication with the AppendEntries consistency check, the commit rule, the election restriction, membership changes, log compaction by snapshots; the relation between the two protocols and the fault-tolerant cloud services that use them.
- **Results:** Paxos safety: once a value is chosen every higher-numbered proposal proposes it [P]; Raft's Log Matching property and Leader Completeness together imply State Machine Safety [P]; Raft makes progress when a majority is up and messages are eventually timely, and randomised timeouts make split votes improbable [S]; the quorum intersection argument shows any two majorities share a node [P].
- **Build:** single-decree Paxos and Multi-Paxos in DSim with safety checked over thousands of randomised schedules with message loss, duplication and leader changes; Raft with leader election, log replication, crash and partition tests and a linearizability checker for the key-value state machine built on it (the checker reused in U9.16 and the capstone U13.3). [local]
- **Gap-fills:** *[inferred: Lamport, Paxos Made Simple; Ongaro–Ousterhout, Raft 2014, recalled, not checked]* Viewstamped Replication and Zab as relatives (named).

**Assignment A9.14** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Why do any two majorities of the same group of n nodes share a node?

(A) They are the same set  
(B) Together they have more than n members, so they overlap  
(C) Each includes the leader  
(D) They are chosen at random

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Raft elects a leader using randomised election timeouts  
(B) Paxos safety depends on quorum intersection  
(C) A cluster of five nodes tolerates two crashes while keeping a majority  
(D) Raft can commit with a minority of nodes

**Q3 (2 marks, numerical answer (nodes)).** How many node crashes can a cluster of 7 nodes tolerate while still having a majority?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that if a value v is chosen by a majority in ballot b of single-decree Paxos, then every proposer that completes phase 1 in a higher ballot proposes v, assuming the rule that a proposer proposes the value of the highest-numbered accepted proposal among its responses.

**Q5 (3 marks, programming).** Implement single-decree Paxos and multi-Paxos in DSim, a Raft node with election, log replication and commit, a linearisable key-value store on top, and test under message loss, crashes and partitions with a checker for the state machine safety property.

<details><summary>Key for A9.14 (open only after your attempt)</summary>

- **Q1:** B. Two sets each with more than n/2 members cannot be disjoint.
- **Q2:** A, B, C. A commit needs a majority.
- **Q3:** 3 nodes (tolerance ±0). A majority is 4, so up to 3 can be down.
- **Q4 (marking outline):** The accepting majority and the responding majority intersect in some acceptor, which reports a proposal accepted in ballot b or later; by induction on the ballot number every proposal numbered between b and the new ballot has value v, so the highest numbered reported proposal has value v and the rule makes the proposer propose it.
- **Q5 (what a passing submission shows):** No two nodes ever apply different commands at one index, progress when a majority can talk, and a recorded history that passes a linearizability check.

</details>

### U9.15 Coordination services in industry: Google Chubby and Apache ZooKeeper
**Sources:** CCDS W3–4
- **Topics:** Leader Election in Industry Systems: Google's Chubby and Apache Zookeeper; Design of Zookeeper: race condition, deadlock, coordination, Zookeeper design goals, data model, Zookeeper architecture, sessions, states, usecases, operations, Access Control List (ACL), Zookeeper applications: Katta, Yahoo! Message Broker (the content list of the cloud course's Week 3); Industry Mutual Exclusion: Chubby (Week 4): Chubby's coarse-grained lock service with a Paxos-replicated cell, sessions and leases with keep-alives, events and caching; ZooKeeper's znodes (persistent, ephemeral, sequential), watches, the atomic-broadcast protocol that orders writes, the guarantees (sequential consistency, atomicity, single system image, durability, timeliness) and the recipes (lock, barrier, leader election, group membership, configuration).
- **Results:** A lock recipe by ephemeral sequential znodes grants the lock to the lowest sequence number and avoids the herd effect when each client watches only its predecessor [D]; a lease of duration T with clock-drift bound ρ is safe if the holder stops using it after T(1 − ρ) of its own clock [D]; reads from a follower may be stale unless synced, so ZooKeeper's reads are sequentially and not linearly consistent [D].
- **Build:** a small coordination service on top of your Raft of U9.14 with sessions, ephemeral and sequential nodes and watches; the lock, barrier and election recipes, tested under client crashes and a partition with the lease bound shown to prevent split-brain. [local]
- **Gap-fills:** *[inferred: Burrows, The Chubby lock service, OSDI 2006; Hunt et al., ZooKeeper, USENIX ATC 2010, recalled, not checked]* etcd and Consul as present-day equivalents (named).

**Assignment A9.15** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** In the ZooKeeper lock recipe, which client holds the lock?

(A) The client with the highest sequence number  
(B) The client with the lowest sequence number among the sequential ephemeral znodes  
(C) A random client  
(D) The first to connect

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Watching only the predecessor znode avoids the herd effect  
(B) An ephemeral znode vanishes when its session ends  
(C) Reads from a follower may be stale unless a sync is issued  
(D) ZooKeeper reads are always linearisable

**Q3 (2 marks, numerical answer (seconds)).** A holder with a lease of T = 10 s and a drift bound of 0.01 stops using it after T(1 minus the bound) of its own clock. How many seconds is that?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that in the predecessor-watching lock recipe exactly one client is woken when the lock is released.

**Q5 (3 marks, programming).** Build a small coordination service in DSim with a replicated tree of znodes using your Raft, with sessions, ephemeral and sequential nodes and watches; implement the lock, leader election and barrier recipes and a lease service with a drift bound. Test with a client that pauses.

<details><summary>Key for A9.15 (open only after your attempt)</summary>

- **Q1:** B. Clients wait for the lowest-numbered znode to disappear.
- **Q2:** A, B, C. Reads are sequentially consistent.
- **Q3:** 9.9 seconds (tolerance ±0.01). 10 times 0.99 = 9.9.
- **Q4 (marking outline):** Each client creates a sequential znode and watches only the znode with the next smaller number; when the holder deletes its znode only the client whose predecessor it was is notified; every other client's predecessor still exists so its watch does not fire.
- **Q5 (what a passing submission shows):** Recipes that keep mutual exclusion under crashes, a lease that is never used past expiry in simulation and a demonstration of a stale lock holder that fencing tokens catch.

</details>

### U9.16 Consistency models and the CAP theorem
**Sources:** ADS W7; CCDS W6
- **Topics:** Consistency models and the CAP theorem (the advanced course's Week 7); CAP Theorem, Eventual Consistency, Consistency levels in Cassandra, Consistency Solutions (the cloud course's key-value week); the consistency spectrum: linearizability, sequential, causal, session guarantees (read-your-writes, monotonic reads and writes), eventual consistency and convergent replicated data types; the CAP theorem and its precise statement, the latency–consistency trade-off in the absence of partitions (PACELC); quorum reads and writes with R + W > N; conflict resolution (last-writer-wins, vector clocks, CRDTs).
- **Results:** CAP: no implementation of an atomic read-write register can be available and consistent in every execution of an asynchronous network that may partition [P]; with N replicas, R + W > N makes every read quorum intersect every write quorum so a read sees the latest acknowledged write in the absence of concurrent writes [P]; a state-based CRDT whose merge is a join in a semilattice converges under any delivery order [P]; last-writer-wins loses concurrent updates [D].
- **Build:** a linearizability checker (Wing–Gong search with pruning) used on histories from the Raft store and from a sloppy-quorum store; quorum register simulation showing stale reads for R + W ≤ N; G-counter, PN-counter and OR-set CRDTs with a randomised convergence test. [local]
- **Gap-fills:** *[inferred: Brewer 2000; Gilbert–Lynch 2002; Abadi 2012; Shapiro et al. 2011, recalled, not checked]* Jepsen-style testing of real databases (read the public reports).

**Assignment A9.16** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** With N replicas, a write quorum W and a read quorum R, which condition makes reads see the latest acknowledged write when there are no concurrent writes?

(A) R plus W at most N  
(B) R plus W greater than N  
(C) R equals 1  
(D) W equals 1

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) The CAP theorem says an atomic register cannot be both available and consistent in every execution that includes a partition  
(B) A state-based CRDT with a join-semilattice merge converges under any delivery order  
(C) Last-writer-wins can lose concurrent updates  
(D) Quorum reads and writes alone always give linearizability

**Q3 (2 marks, numerical answer (replicas)).** With N = 7 replicas and a write quorum of W = 3, what is the smallest read quorum R that guarantees intersection?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that if R plus W is greater than N, every read quorum and every write quorum share at least one replica.

**Q5 (3 marks, programming).** Implement a replicated register with configurable N, R and W, version vectors and read repair in DSim; a G-counter, PN-counter and OR-set; and a checker that finds stale reads, lost updates and linearizability violations under partitions. Show the CAP trade-off by running both a CP and an AP mode.

<details><summary>Key for A9.16 (open only after your attempt)</summary>

- **Q1:** B. Then every read quorum intersects every write quorum.
- **Q2:** A, B, C. Sloppy quorums and concurrent writes can still give anomalies.
- **Q3:** 5 replicas (tolerance ±0). R must exceed N minus W = 4, so R = 5.
- **Q4 (marking outline):** The sets have sizes R and W among N replicas; if they were disjoint their union would have R plus W members, which exceeds N and is impossible; so they intersect.
- **Q5 (what a passing submission shows):** Stale reads absent when R plus W exceeds N and no concurrent writes, CRDT replicas that converge under random delivery, and clearly different behaviour in the two modes during a partition.

</details>

### U9.17 Bridge: transactions — ACID, serializability, locking, logging and recovery
**Sources:** none (prerequisite bridge, added so that later units rest on taught ground)
Bridge for: U9.18 (atomic commit, Percolator, Spanner), U10.5 (Bigtable), U10.7 (managed databases). Builds on U10.1's relational view if read in order, and is self-contained otherwise.
- **Topics:** Transactions and the ACID properties; histories and conflict serializability, the precedence graph; two-phase locking and strictness; deadlock handling in a lock manager; multiversion concurrency control and snapshot isolation with its write-skew anomaly; isolation levels and anomalies (dirty read, non-repeatable read, phantom); write-ahead logging, undo and redo, checkpoints and the ARIES recovery idea; the central assumption that failures are fail-stop.
- **Results:** A history is conflict-serializable iff its precedence graph is acyclic [P]; strict two-phase locking yields conflict-serializable and recoverable histories [P]; snapshot isolation allows write skew, which is not conflict-serializable [D, by example]; write-ahead logging with redo and undo restores atomicity and durability after a crash [S].
- **Build:** a precedence-graph checker; a strict-2PL lock manager with deadlock detection; a multiversion store with snapshot isolation and a write-skew reproduction; a write-ahead log with crash and recovery tests. [local]
- **Gap-fills:** *[inferred: Bernstein–Hadzilacos–Goodman; Gray–Reuter, recalled, not checked]* serializable snapshot isolation (named).

**Assignment A9.17** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** When is a schedule conflict-serializable?

(A) When its precedence graph has no cycle  
(B) When it has no writes  
(C) When it is serial  
(D) When every transaction commits

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Strict two-phase locking gives conflict-serializable and recoverable histories  
(B) Snapshot isolation can allow write skew  
(C) Write-ahead logging requires the log record to reach stable storage before the data page  
(D) Serializability implies that transactions never wait

**Q3 (2 marks, numerical answer (orders)).** How many serial orders are there for 4 transactions?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that if the precedence graph of a schedule is acyclic then the schedule is conflict-equivalent to a serial schedule.

**Q5 (3 marks, programming).** Implement a precedence-graph tester, a strict 2PL lock manager with deadlock detection, a snapshot-isolation engine that exhibits write skew, a write-ahead log with ARIES-style redo and undo and crash tests at every log position.

<details><summary>Key for A9.17 (open only after your attempt)</summary>

- **Q1:** A. Acyclic precedence graph means an equivalent serial order exists.
- **Q2:** A, B, C. Locking makes transactions wait.
- **Q3:** 24 orders (tolerance ±0). 4 factorial is 24.
- **Q4 (marking outline):** Take a topological order of the transactions; for any conflicting pair of operations the earlier transaction in the schedule precedes the other in the graph and so in the topological order; thus the serial schedule in that order has every conflicting pair in the same order as the original, so they are conflict-equivalent.
- **Q5 (what a passing submission shows):** Correct verdicts on a table of schedules, write skew reproduced under snapshot isolation and prevented under 2PL, and recovery that restores the committed state after a crash at any point.

</details>

### U9.18 Distributed transactions: atomic commit, Percolator and Spanner
**Sources:** ADS W11
- **Topics:** Google Percolator (the third item in the advanced course's Week 11, which pairs Amazon Dynamo, Facebook Cassandra and Google Percolator; Dynamo and Cassandra are taught in U10.3 and U10.4): the atomic-commit problem, two-phase commit and its blocking behaviour, three-phase commit, Paxos Commit; Percolator: incremental processing over Bigtable with snapshot-isolated multi-row transactions, the timestamp oracle, the primary-lock and secondary-lock protocol, lock cleanup by observers, notifications; Spanner as the gap-fill that completes the story: TrueTime, externally consistent distributed transactions and Paxos groups per shard.
- **Results:** Two-phase commit is atomic but blocks if the coordinator fails after all participants vote yes [P]; no non-blocking atomic commit protocol exists in an asynchronous system with partitions [S, a consequence of FLP]; Percolator's single-primary commit point makes a multi-row commit atomic, as the decision is recorded in one row [P]; commit-wait in Spanner guarantees that the order of timestamps matches real-time order given the TrueTime bound ε [P].
- **Build:** two-phase commit in DSim with coordinator crash and blocking measured; a Percolator-style transaction layer over an in-memory multiversion store with a timestamp oracle and lock cleanup, tested for snapshot isolation and for atomicity under crashes; a TrueTime-like uncertainty clock and commit-wait demonstration. [local]
- **Gap-fills:** *[inferred: Peng–Dabek, OSDI 2010; Corbett et al., Spanner, OSDI 2012, recalled, not checked]* Spanner is inferred as the gap-fill and links to the cloud database products in U10.7.

**Assignment A9.18** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** When does two-phase commit block?

(A) When the coordinator fails after all participants have voted yes and before any has learned the decision  
(B) When one participant votes no  
(C) When messages are fast  
(D) When there is one participant

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Two-phase commit is atomic  
(B) Percolator commits a multi-row transaction by recording the decision in a single primary row  
(C) Spanner commit-wait ensures timestamp order matches real-time order given the TrueTime bound  
(D) Three-phase commit is non-blocking under partitions

**Q3 (2 marks, numerical answer (ms)).** With a TrueTime uncertainty half-width of 7 ms, commit-wait takes about twice that. How many ms?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that two-phase commit is atomic: no participant commits while another aborts.

**Q5 (3 marks, programming).** Implement two-phase commit in DSim with coordinator and participant crashes, a cooperative termination protocol, a Percolator-style transaction layer over your key-value store with primary-lock recovery, and a simulated TrueTime clock with commit-wait. Check atomicity and external consistency.

<details><summary>Key for A9.18 (open only after your attempt)</summary>

- **Q1:** A. The participants are uncertain and cannot decide alone.
- **Q2:** A, B, C. Three-phase commit assumes bounded delays and no partitions.
- **Q3:** 14 ms (tolerance ±0.1). The wait is about 2 times 7 = 14.
- **Q4 (marking outline):** A participant commits only on receiving a commit decision, which the coordinator sends only if every participant voted yes; abort is sent otherwise, and the decision is logged before being sent so a recovered coordinator repeats the same decision; a participant never changes its vote after voting yes, so no run has both outcomes.
- **Q5 (what a passing submission shows):** Atomicity in every injected failure, blocking shown in the uncertain window, recovery by rolling the primary lock forward or back, and timestamp order matching real-time order with commit-wait.

</details>

### U9.19 Failures and recovery: checkpointing, rollback recovery, fault tolerance and self-stabilization
**Sources:** DS W3,5; CCDS W5
- **Topics:** Checkpointing & Rollback Recovery (Week 3); Failures & Recovery Approaches in Distributed Systems: local checkpoints, consistent states, interaction with the outside world, messages (in-transit, orphan), the domino effect, the problem of livelock, rollback recovery schemes, checkpointing and recovery algorithms: the Koo–Toueg coordinated checkpointing algorithm; uncoordinated and communication-induced checkpointing, message logging (pessimistic, optimistic, causal); Fault Tolerance and Self-Stabilization (Week 5): fault models, redundancy, and self-stabilisation: legitimate states, convergence and closure, Dijkstra's K-state token ring.
- **Results:** A set of local checkpoints is a consistent global checkpoint iff no message is orphaned, equivalently no checkpoint depends causally on another's later state [P]; uncoordinated checkpointing can cascade to the initial state (domino effect) [D, by example]; Koo–Toueg's two-phase protocol yields a consistent global checkpoint with a minimal set of participating processes [S]; Dijkstra's K-state ring stabilises from every initial state when K ≥ n [P].
- **Build:** a recovery-line calculator over a space-time diagram that finds the maximum consistent cut and exhibits the domino effect; Koo–Toueg in DSim; Dijkstra's token ring started from random states with the stabilisation time measured. [local]
- **Gap-fills:** *[inferred: Elnozahy et al., A survey of rollback-recovery protocols, 2002; Dijkstra 1974, recalled, not checked]* checkpointing in large-scale machine-learning training (links to U12.3).

**Assignment A9.19** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** When is a set of local checkpoints one from each process a consistent global checkpoint?

(A) When no message is received before one checkpoint and sent after the other  
(B) When all checkpoints are taken at once  
(C) When there are no messages  
(D) When each process has one checkpoint

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Uncoordinated checkpointing can suffer from the domino effect  
(B) Koo-Toueg checkpointing involves only processes that have communicated with the initiator, directly or indirectly  
(C) Dijkstra's K-state ring stabilises from every initial state when K is at least n  
(D) A self-stabilising algorithm needs a correct initial state

**Q3 (2 marks, numerical answer (candidates)).** Three processes each have 4 checkpoints. How many candidate global checkpoints (one from each) must be examined?

**Q4 (2 marks, prove or derive; every step with its reason).** Construct a three-process example with uncoordinated checkpoints in which the domino effect rolls all processes back to the initial state, and explain why.

**Q5 (3 marks, programming).** Implement uncoordinated, coordinated blocking and message-logging recovery in DSim, a recovery-line finder using the checkpoint dependency graph, Koo-Toueg checkpointing, and Dijkstra's K-state ring with fault injection and a convergence-time measurement.

<details><summary>Key for A9.19 (open only after your attempt)</summary>

- **Q1:** A. No orphan messages: the receipt must not be recorded without the send.
- **Q2:** A, B, C. Self-stabilisation works from any state.
- **Q3:** 64 candidates (tolerance ±0). 4 to the power 3 is 64.
- **Q4 (marking outline):** Arrange the messages so that between each pair of consecutive checkpoints of the processes there is a message sent after one checkpoint and received before the next checkpoint of another; rolling process P back to its last checkpoint orphans a message to Q, forcing Q back, which orphans a message to R, which orphans a message back to P and so on until every process reaches its initial state.
- **Q5 (what a passing submission shows):** A recovery line that never contains an orphan message, a domino effect reproduced in the uncoordinated case, and convergence from random states for K at least n.

</details>

### U9.20 Message ordering, group communication and virtual synchrony
**Sources:** DS W5; ADS W9
- **Topics:** Message Ordering & Group Communication (Week 5); Virtual synchrony (the advanced course's Week 9): FIFO, causal and total-order multicast, implementing causal order with vector clocks, total order by a sequencer and by agreed timestamps (the ISIS ABCAST idea), reliable multicast, group membership and view changes, the virtual-synchrony guarantee that messages are delivered in the same view at all surviving members, and its relation to state-machine replication (U9.14).
- **Results:** Causal broadcast by vector-clock buffering delivers a message when it is the next from its sender and all its causal predecessors have been delivered [P]; total-order broadcast is equivalent to consensus in an asynchronous crash model [S]; virtual synchrony makes the set of messages delivered before a view change identical at the members that survive it [Def].
- **Build:** FIFO, causal and total-order multicast in DSim with an order-checker; a view-synchronous group with a join, a leave and a crash, with a test that survivors agree on the delivered set before every view. [local]
- **Gap-fills:** *[inferred: Birman and Joseph 1987; Défago–Schiper–Urbán, total order broadcast survey, recalled, not checked]* Kafka's partition-ordering guarantee (U11.6).

**Assignment A9.20** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** When does vector-clock causal broadcast deliver a message m from sender s?

(A) On arrival  
(B) When m is the next message from s and every message that causally precedes it has been delivered  
(C) After a timeout  
(D) When all processes acknowledge

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Total-order broadcast is equivalent to consensus in an asynchronous crash model  
(B) Virtual synchrony makes surviving members deliver the same messages before a view change  
(C) Causal order implies total order  
(D) FIFO order is weaker than causal order

**Q3 (2 marks, numerical answer (bytes)).** A causal broadcast tags each message with a vector of 50 entries of 4 bytes. How many bytes of metadata do 1,000 messages carry?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that the vector-clock delivery rule ensures that if broadcast m precedes broadcast m prime causally then every process delivers m before m prime.

**Q5 (3 marks, programming).** Implement FIFO, causal and total-order broadcast in DSim with a sequencer and with Lamport-timestamp agreement, a view-synchronous group membership layer and checkers for each ordering property under random delays and crashes.

<details><summary>Key for A9.20 (open only after your attempt)</summary>

- **Q1:** B. Messages are buffered until their causal predecessors are delivered.
- **Q2:** A, B, D. Concurrent messages may be delivered in different orders under causal order.
- **Q3:** 200000 bytes (tolerance ±0). 200 bytes per message gives 200,000.
- **Q4 (marking outline):** Suppose process p delivers m prime; by the rule p has delivered all messages that causally precede m prime, among them m, since the vector of m prime records that its sender had delivered or sent m; so m is delivered at p before m prime.
- **Q5 (what a passing submission shows):** Checkers that pass for the implemented property and fail for a weaker one on adversarial schedules, and identical delivery sets across a view change.

</details>

### U9.21 Bitcoin and blockchains
**Sources:** ADS W10; CNS W12
- **Topics:** Bitcoin and Blockchains (the advanced course's Week 10); the cryptocurrency and blockchain item that closes the cryptography course's final week: hash-linked blocks and Merkle trees (U5.10), proof of work and difficulty adjustment, the longest-chain rule and forks, transactions with digital signatures (U5.17, ECDSA over secp256k1) and the UTXO model, the Nakamoto consensus protocol as probabilistic consensus without membership, double spending and the 51% attack, selfish mining, incentives; the comparison with classical Byzantine agreement (U9.13); proof of stake and smart contracts as a labelled gap-fill, *inferred*; blockchain and bitcoin as the application context of TPMC's final themes.
- **Results:** Nakamoto's double-spend probability for an attacker with fraction q of the hash power against a merchant waiting z confirmations is the Poisson-weighted sum of catch-up probabilities (q/p)^{z − k}, and falls exponentially in z when q < 1/2 [D]; with q = 0.1 and z = 5 the value is about 0.0009 (the exact figure is computed by the unit's script, not recalled) [check]; if q ≥ 1/2 the attacker eventually wins with probability 1 [P]; the expected time to find a block is the difficulty over the total hash rate [D].
- **Build:** a toy blockchain with Merkle trees, proof of work at adjustable difficulty, signed UTXO transactions from your own ECDSA of U5.17 and fork choice; a mining race simulation under network delay estimating the orphan rate; the double-spend probability formula against a Monte Carlo of the attacker's random walk; a selfish-mining simulation. [local; learning only]
- **Gap-fills:** *[inferred: Nakamoto 2008; Eyal–Sirer 2014; Buterin et al. on proof of stake, recalled, not checked]* the present state of any particular network is not claimed here.

**Assignment A9.21** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** If an attacker controls less than half of the hash power, what happens to the probability that a double spend succeeds as the merchant waits for more confirmations?

(A) It falls exponentially  
(B) It rises  
(C) It stays constant  
(D) It becomes 1

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) An attacker with at least half of the hash power eventually overtakes the honest chain with probability 1  
(B) The expected time to find a block is the difficulty divided by the network hash rate in the simplified model  
(C) Each block commits to its predecessor by hash  
(D) Proof of work prevents all attacks

**Q3 (2 marks, numerical answer (probability)).** Compute the Nakamoto double-spend success probability for q = 0.1 and z = 5, using the Poisson-weighted sum (to four decimals).

**Q4 (2 marks, prove or derive; every step with its reason).** Show that an attacker with fraction q less than one half of the hash power starting z blocks behind ever catches up with probability (q/p) to the power z, where p equals 1 minus q.

**Q5 (3 marks, programming).** Build a toy blockchain with proof of work and a longest-chain rule, a mining race simulator with honest and attacking miners, a Monte Carlo estimate of double-spend success against the formula, and a selfish-mining experiment for learning. No real network connections.

<details><summary>Key for A9.21 (open only after your attempt)</summary>

- **Q1:** A. The catch-up probability is (q/p) to the power of the deficit.
- **Q2:** A, B, C. Proof of work does not prevent every attack, such as a majority attack.
- **Q3:** 0.0009137 probability (tolerance ±0.0001). The value is about 0.0009.
- **Q4 (marking outline):** Let a_z be the catch-up probability from deficit z; each step the deficit falls by one with probability q and rises by one with probability p, so a_z = q a_(z minus 1) plus p a_(z plus 1) with a_0 = 1 and a_z bounded; the solutions of this recurrence are combinations of 1 and (q/p) to the z; boundedness and a_0 = 1 select (q/p) to the z.
- **Q5 (what a passing submission shows):** A chain that rejects tampering, a simulated success rate matching the formula within sampling error and a measured threshold for selfish mining.

</details>

### U9.22 Security in distributed systems and sensor networks
**Sources:** DS W8
- **Topics:** Case Studies: Sensor Networks, Authentication & Security in DS (the last week of the classical course): wireless sensor networks (constraints on energy, memory and radio; the tree and cluster architectures, data aggregation, localisation and time synchronisation at the level of names); security in distributed systems: authentication (the Needham–Schroeder and Kerberos ideas of U5.18), authorisation and capability use, secure channels, replay and reflection attacks, trust and key distribution in sensor networks (random key pre-distribution, the Eschenauer–Gligor scheme, SPINS-style broadcast authentication by delayed key disclosure), attacks specific to sensor networks (Sybil, wormhole, sinkhole, node capture), and the link back to Byzantine tolerance (U9.13).
- **Results:** In random key pre-distribution, each node holds k keys from a pool of P, and two nodes share a key with probability 1 − C(P − k, k)/C(P, k) [D]; delayed key disclosure authenticates broadcasts under loose time synchronisation if keys are disclosed after the latest possible reception time [P]; a Sybil attacker who forges identities defeats any voting scheme based on identities alone [D].
- **Build:** an Eschenauer–Gligor key pre-distribution simulator with the connectivity probability against pool and ring size and the effect of node capture on link compromise; a delayed-disclosure broadcast authenticator (a one-way hash chain, from U5.10) with a test that rejects early-disclosed forgeries; a Needham–Schroeder replay attack and its fix with nonces. [local; learning only]
- **Gap-fills:** *[inferred: Eschenauer–Gligor 2002; Perrig et al., SPINS 2002, recalled, not checked]* energy-aware routing (named only).

**Assignment A9.22** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** In random key pre-distribution each sensor holds k keys from a pool of P. What is the probability that two nodes share no key?

(A) C(P minus k, k) over C(P, k)  
(B) k over P  
(C) 1 over P  
(D) 0

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Delayed key disclosure authenticates broadcasts under loose time synchronisation  
(B) A Sybil attacker who can forge identities defeats voting on identities alone  
(C) Key pre-distribution gives connectivity only with some probability  
(D) Sensor networks have unlimited energy

**Q3 (2 marks, numerical answer (probability)).** With a pool of P = 1000 keys and k = 50 keys per node, what is the probability that two nodes share at least one key (three decimals)?

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the probability that two nodes, each holding k keys drawn without replacement from a pool of P, share at least one key.

**Q5 (3 marks, programming).** Simulate random key pre-distribution on a random geometric sensor field, measure the connectivity against k, implement a TESLA-style delayed-disclosure broadcast authenticator and a Sybil attack against identity voting with a resource-testing defence. Simulation only.

<details><summary>Key for A9.22 (open only after your attempt)</summary>

- **Q1:** A. The second node's k keys must all come from the P minus k keys the first does not hold.
- **Q2:** A, B, C. Sensor nodes are resource-limited.
- **Q3:** 0.928 probability (tolerance ±0.005). The probability is about 0.92.
- **Q4 (marking outline):** The number of ways for the second node to choose k keys is C(P, k); the number that avoid the k keys of the first node is C(P minus k, k); so the probability of no common key is the ratio and the probability of at least one is one minus that ratio.
- **Q5 (what a passing submission shows):** A connectivity curve that matches the formula, a broadcast authenticator that rejects forged packets, and a Sybil attack defeated by the defence in the model.

</details>

## D10. Cloud storage and databases: relational foundations, distributed file systems, key-value and wide-column stores, in-memory NoSQL and Google Cloud storage

Aim: storage as the place where the distributed-systems theory of D9 meets disks, memory and money. A short bridge on the relational model and SQL comes first because the surrounding courses assume it (the cloud-platform course lists SQL as a prerequisite, and the big-data course lists database management systems). Each system is rebuilt in miniature on the DSim harness or as a local engine, then compared with the cloud product that implements the same idea. Benchmarks (recalled, not checked): Kleppmann, *Designing Data-Intensive Applications*; Garcia-Molina, Ullman and Widom, *Database Systems: The Complete Book*; Petrov, *Database Internals*; and the system papers named in each unit (the advanced-course source lists classic research papers as its references).

### U10.1 Bridge: the relational model, SQL, indexing and query processing
**Sources:** none (prerequisite bridge, added so that later units rest on taught ground)
Bridge for: U10.4 onward (every store here is defined by what it gives up relative to a relational database), U12.2 (BigQuery). Addresses the SQL prerequisite stated in the cloud-platform source and the database prerequisite stated in the big-data source.
- **Topics:** Relations, keys and integrity constraints; relational algebra (selection, projection, product, join, union, difference, aggregation) and its correspondence to SQL (SELECT, FROM, WHERE, GROUP BY, HAVING, joins, subqueries, window functions); functional dependencies, normal forms (3NF, BCNF) and lossless decomposition; indexes: B+-trees (height, fan-out, range scans), hash indexes; join algorithms (nested loop, hash join, sort-merge) and their costs; a cost-based optimiser's logic (selectivity, join order); the row store versus column store layout (continued in U12.2).
- **Results:** A B+-tree with fan-out b over n keys has height ⌈log_b n⌉ [P]; a BCNF decomposition obtained by repeatedly splitting on a violating dependency is lossless [P]; a hash join costs about |R| + |S| page reads when the smaller input fits in memory, and 3(|R| + |S|) with one partitioning pass [D]; the join of R and S on a key of S has at most |R| tuples [P].
- **Build:** a small relational engine in Python (tables, selection, projection, hash join, sort-merge join, group-by aggregation and a tiny SQL parser for a SELECT subset) checked against `sqlite3` on random data; a B+-tree with insert, delete and range scan; an FD closure and BCNF decomposer. [local]
- **Gap-fills:** *[inferred: Garcia-Molina–Ullman–Widom, Ch.2–7; Selinger et al. 1979, recalled, not checked]* query optimisation by dynamic programming over join orders (named).

**Assignment A10.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** A B-plus tree with fan-out b holds n keys. What is its height?

(A) About log base b of n, rounded up  
(B) About n  
(C) About b times n  
(D) Always 2

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Repeatedly splitting a relation on a BCNF-violating dependency gives a lossless decomposition  
(B) A hash join reads each input about once when the smaller input fits in memory  
(C) The join of R and S on a key of S has at most as many tuples as R  
(D) A secondary index always makes every query faster

**Q3 (2 marks, numerical answer (levels)).** A B-plus tree has fan-out 100 and holds 1,000,000 keys. What is the height in levels?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that splitting R on a dependency X to Y that violates BCNF into R1 = X together with Y and R2 = R minus (Y minus X) is lossless.

**Q5 (3 marks, programming).** Write a B-plus tree with insert, delete and range scan and test it against a sorted list, hash join and sort-merge join with page-read counting, and a BCNF decomposition routine from functional dependencies with a lossless-join test (tableau). Use SQLite as the oracle for the join outputs.

<details><summary>Key for A10.1 (open only after your attempt)</summary>

- **Q1:** A. Each level multiplies the reach by b, so the height is the ceiling of log base b of n.
- **Q2:** A, B, C. An index also costs on writes and may not help low-selectivity queries.
- **Q3:** 3 levels (tolerance ±0). 100 cubed is 1,000,000, so 3 levels.
- **Q4 (marking outline):** The attributes common to R1 and R2 are X, and in R1 the dependency X to Y makes X a key of R1; the natural join of the projections on a key of one side adds no tuples that are not in R: any tuple of the join agrees on X with a tuple of R2 and with the single Y value that X determines in R1, which is the Y value of that tuple of R; so the join equals R.
- **Q5 (what a passing submission shows):** A tree whose height matches the formula, join outputs identical to SQLite, page counts that match the cost formulas, and decompositions that pass the lossless-join test.

</details>

### U10.2 Distributed file systems: the Google File System and HDFS, with erasure coding
**Sources:** DS W7; BDC W4
- **Topics:** Case Studies: GFS, HDFS (the seventh week of the classical course); Big Data Storage Platforms for large-scale data storage (the fourth week of the big-data course): the design assumptions of GFS (commodity failures, huge files, append-heavy workloads), the single master with chunkservers, 64-MB chunks (128 MB default in HDFS), the control and data flows of read, write and record append, leases and the replica pipeline, re-replication and rack awareness, the NameNode and DataNodes in HDFS, the edit log and checkpoint, high availability with standby nodes and quorum journals (U9.14), the small-files problem; erasure coding as the storage-efficient alternative to triple replication: a Reed–Solomon (k, m) code over GF(2⁸) (the field built in U5.5), its storage overhead (k + m)/k against 3×, and the repair-traffic cost.
- **Results:** A Reed–Solomon code from a Vandermonde generator is maximum-distance-separable: any k of the k + m coded blocks recover the data [P]; (6, 3) coding stores 1.5× the data and survives any 3 losses, while 3× replication stores 3× and survives any 2 [D]; the probability that a given block is lost in a year under replication factor r and independent annual disk failure probability p with no repair is p^r [D]; with repair, the loss rate falls with the ratio of repair rate to failure rate [D, by Markov chain].
- **Build:** a chunked file store with a master, chunkservers, a replica pipeline, re-replication on failure and rack-aware placement in DSim; a Reed–Solomon (k, m) codec over GF(2⁸) with an erasure-recovery test for every loss pattern of a small code; the durability model checked by simulation. [local]
- **Gap-fills:** *[inferred: Ghemawat–Gobioff–Leung, SOSP 2003; Shvachko et al., HDFS, MSST 2010, recalled, not checked]* Colossus as GFS's successor (named only) and locally repairable codes.

**Assignment A10.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What does maximum-distance-separable mean for a Reed-Solomon code with k data and m parity blocks?

(A) Any k of the k plus m blocks recover the data  
(B) Only the data blocks recover the data  
(C) Any m blocks recover the data  
(D) Any single block recovers the data

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Erasure coding with 6 data and 3 parity blocks stores 1.5 times the data  
(B) Three-way replication tolerates the loss of any 2 copies  
(C) With independent failures and no repair the probability that all r replicas of a block fail in a year is p to the power r  
(D) Erasure coding always repairs faster than replication

**Q3 (2 marks, numerical answer (probability)).** A block has 3 replicas on disks that each fail in a year with probability 0.02, independently, with no repair. What is the probability that all three are lost in a year?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that a Reed-Solomon code built from a Vandermonde generator with distinct evaluation points recovers the data from any k of the k plus m blocks.

**Q5 (3 marks, programming).** Implement Reed-Solomon coding over GF(256) from scratch with encode and decode for any erasure pattern, a Markov-chain model of durability with repair, a toy distributed file system with chunk servers, a master, replication and re-replication after a failure, and compare storage overhead and durability for replication and coding.

<details><summary>Key for A10.2 (open only after your attempt)</summary>

- **Q1:** A. An MDS code recovers from any k surviving blocks.
- **Q2:** A, B, C. Repair of an erasure-coded block reads several surviving blocks, so it is usually more expensive.
- **Q3:** 8e-06 probability (tolerance ±0.0000001). 0.02 cubed is 0.000008.
- **Q4 (marking outline):** Each block is a polynomial of degree below k evaluated at a distinct point; the data are the coefficients; any k surviving blocks give k equations whose matrix is a square Vandermonde matrix with distinct points, whose determinant is the product of differences of the points, which is non-zero; so the system has a unique solution.
- **Q5 (what a passing submission shows):** Decoding that succeeds for every pattern of at most m erasures and fails beyond, a durability model whose loss rate falls with the repair rate, and a toy file system that restores the replication factor after failures.

</details>

### U10.3 Amazon Dynamo and LinkedIn Voldemort: highly available key-value stores
**Sources:** ADS W11–12
- **Topics:** Amazon Dynamo (Week 11 of the advanced course); Voldemort (LinkedIn) (Week 12): the always-writable design goal and its trade of consistency for availability; partitioning by consistent hashing with virtual nodes (U9.5); replication to N successors, quorum parameters N, R, W and sloppy quorums with hinted handoff; versioning by vector clocks and application-assisted reconciliation (U9.6); failure detection by gossip and anti-entropy by Merkle trees; Voldemort's layered architecture (pluggable storage engines, client-side or server-side routing, read repair, version resolution) as the open-source realisation and its read-only stores built offline in Hadoop.
- **Results:** With R + W > N a read quorum intersects the last write quorum, but with sloppy quorums and hinted handoff the intersection is not guaranteed [D]; two Merkle trees over the same key range locate differing keys in O(d log n) hash comparisons for d differences [D]; the vector clock of a reconciled value dominates all its parents [P].
- **Build:** a Dynamo-style store in DSim (ring, N-R-W quorums, hinted handoff, vector clocks, Merkle anti-entropy, read repair) with fault injection and a measurement of the stale-read rate against R and W; a Voldemort-style pluggable-engine interface with a client-side router. [local]
- **Gap-fills:** *[inferred: DeCandia et al., SOSP 2007; Sumbaly et al., Serving large-scale batch computed data with Project Voldemort, FAST 2012, recalled, not checked]* DynamoDB as the managed descendant (named only).

**Assignment A10.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Under a sloppy quorum with hinted handoff in a Dynamo-style store, is it guaranteed that R plus W greater than N makes a read see the latest write?

(A) Yes always  
(B) No, because the write may have gone to stand-in nodes outside the preference list  
(C) Only for reads  
(D) Only for deletes

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Merkle trees let replicas find differing keys by comparing hashes top-down  
(B) The vector clock of a reconciled value dominates its parents  
(C) Dynamo can return several conflicting versions to the client  
(D) Dynamo guarantees linearizability

**Q3 (2 marks, numerical answer (comparisons)).** Two replicas holding 1024 keys differ in 3 keys. About how many hash comparisons does a Merkle-tree synchronisation make, using d times log2 n?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that the vector clock formed by taking the componentwise maximum of two conflicting versions' clocks and incrementing the reconciling node's entry dominates both.

**Q5 (3 marks, programming).** Implement a Dynamo-style ring store in DSim with consistent hashing, preference lists, sloppy quorums, hinted handoff, vector-clock versions with client reconciliation and Merkle-tree anti-entropy. Measure stale reads and divergent versions under failures and show repair converging.

<details><summary>Key for A10.3 (open only after your attempt)</summary>

- **Q1:** B. Hinted writes may be held by nodes that a later read quorum does not contact.
- **Q2:** A, B, C. Dynamo favours availability and offers eventual consistency.
- **Q3:** 30 comparisons (tolerance ±0). 3 times 10 = 30.
- **Q4 (marking outline):** The componentwise maximum is at least each parent entry-wise; incrementing one entry makes it strictly greater than each parent in at least that entry; so the new clock is at least as large as both everywhere and different from both, which is domination.
- **Q5 (what a passing submission shows):** A store that remains writable under node failures, conflicts surfaced as siblings, and anti-entropy that brings replicas to equality with comparisons near the formula.

</details>

### U10.4 Apache Cassandra: a wide-column store on Dynamo's ring and Bigtable's engine
**Sources:** ADS W11; CCDS W6
- **Topics:** Facebook Cassandra (Week 11 of the advanced course); Design of Key-Value Stores and Design of Apache Cassandra (Week 6 of the cloud course): the key-value abstraction and the NoSQL data model (rows, columns, column families, keyspaces), data placement strategies and snitches, the write path (commit log, memtable, flush to immutable SSTables), the read path with Bloom filters, compaction, deletes by tombstones, membership by gossip (U9.3), consistency levels and read repair, and how Cassandra combines Dynamo's distribution with Bigtable's storage engine.
- **Results:** A Bloom filter with m bits, n keys and k hash functions has false-positive rate (1 − e^{−kn/m})^k, minimised at k = (m/n) ln 2 giving about 0.6185^{m/n} [P]; a tombstone must outlive the gossip-repair window or deleted data can resurrect [D]; size-tiered compaction trades write amplification against read amplification and space amplification [D].
- **Build:** an LSM-tree store with commit log, memtable, SSTables, Bloom filters, tombstones and size-tiered and leveled compaction with measured amplification; a Cassandra-like ring in DSim with tunable consistency levels, read repair and a deleted-key resurrection test. [local]
- **Gap-fills:** *[inferred: Lakshman–Malik, Cassandra, LADIS 2009; O'Neil et al., the LSM-tree, 1996, recalled, not checked]* lightweight transactions by Paxos (links to U9.14).

**Assignment A10.4** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Which choice of the number of hash functions k minimises the Bloom filter false-positive rate for m bits and n keys?

(A) k = (m/n) times ln 2  
(B) k = 1  
(C) k = m  
(D) k = n

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) A Bloom filter has no false negatives  
(B) A tombstone must be kept longer than the repair window or deleted data can reappear  
(C) Size-tiered compaction has lower write amplification than leveled compaction  
(D) A Bloom filter can be deleted from by clearing bits without side effects

**Q3 (2 marks, numerical answer (probability)).** A Bloom filter uses 10 bits per key and 7 hash functions. What is the approximate false-positive rate (1 minus e to the power minus kn/m) to the power k?

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the Bloom filter false-positive rate (1 minus e to the power minus kn over m) to the power k.

**Q5 (3 marks, programming).** Implement a log-structured storage engine with a commit log, memtable, SSTables with index and Bloom filter, size-tiered and leveled compaction and tombstones, with a Cassandra-style gossip membership and hinted handoff in DSim. Measure write, read and space amplification and the resurrection of deleted data when the tombstone is dropped too early.

<details><summary>Key for A10.4 (open only after your attempt)</summary>

- **Q1:** A. This gives a rate of about 0.6185 to the power m/n.
- **Q2:** A, B, C. Clearing bits can create false negatives for other keys.
- **Q3:** 0.008194 probability (tolerance ±0.0005). The value is about 0.008.
- **Q4 (marking outline):** After n keys are inserted with k hashes each, a given bit is still zero with probability (1 minus 1/m) to the power kn which is about e to the power minus kn/m; a non-member is reported present if all k of its bit positions are one, with probability about (1 minus e to the power minus kn/m) to the power k, treating positions as independent.
- **Q5 (what a passing submission shows):** A store matching a dictionary oracle, measured false positives close to the formula, amplification trade-offs between the two compaction strategies, and a reproduced resurrection.

</details>

### U10.5 HBase and Bigtable: sorted wide-column storage over a distributed file system
**Sources:** CCDS W6; BDC W4
- **Topics:** Design of HBase (Week 6 of the cloud course): what HBase is, its architecture and components (HMaster, region servers, regions, ZooKeeper, HDFS underneath), the data model of Bigtable (rows sorted by key, column families, timestamped versions), the storage hierarchy (write-ahead log, MemStore, HFiles), auto sharding and distribution by region splits, Bloom filters in reads, cross-datacenter replication; the slide topic the source lists as "Fold, Store, and Shift" is not a term this curriculum could identify, and it is flagged in Appendix E for resolution from the lecture; Bigtable's tablet location by a three-level hierarchy; atomicity at row level and the link to the multi-row transactions of U9.18; hot-spotting and row-key design.
- **Results:** Write amplification of leveled compaction with size ratio T over L levels is about T·L in the worst case, against about L for size-tiered [D]; a row-key design that begins with a monotonically increasing timestamp sends all writes to one region [D]; an HBase read touches the MemStore plus at most the HFiles whose Bloom filters answer positive [D].
- **Build:** a tablet store with a sorted memtable, write-ahead log, immutable files, region split at a size threshold and a master that assigns regions to servers via your ZooKeeper-like service of U9.15; a hot-spot experiment with sequential versus salted keys. [local]
- **Gap-fills:** *[inferred: Chang et al., Bigtable, OSDI 2006; George, HBase: The Definitive Guide, recalled, not checked]* Cloud Bigtable as the managed product (U10.7).

**Assignment A10.5** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Why does a row key starting with a monotonically increasing timestamp cause trouble in HBase or Bigtable?

(A) All new writes land in the region holding the highest keys, making a hot spot  
(B) It uses too much space  
(C) It disables Bloom filters  
(D) It prevents compaction

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Leveled compaction has higher write amplification than size-tiered  
(B) An HBase read consults the memstore and the store files that may contain the row  
(C) Bloom filters reduce the number of store files read for point lookups  
(D) Bigtable stores data in unsorted order

**Q3 (2 marks, numerical answer (times)).** With size ratio T = 10 and L = 4 levels, what is the worst-case write amplification of leveled compaction, taking T times L?

**Q4 (2 marks, prove or derive; every step with its reason).** Explain with an argument why salting or reversing a monotonically increasing row key spreads writes across regions but makes range scans more costly.

**Q5 (3 marks, programming).** Build a sorted wide-column store on top of your toy distributed file system with tablets, splits, a master that assigns tablets, and a compaction policy; add an HBase-style row-key design experiment with a timestamp key, a salted key and a reversed key, and measure the load per tablet server.

<details><summary>Key for A10.5 (open only after your attempt)</summary>

- **Q1:** A. Rows are range-partitioned by key, so ordered keys concentrate the load.
- **Q2:** A, B, C. Bigtable stores rows sorted by key.
- **Q3:** 40 times (tolerance ±0). T times L = 40, against about L = 4 for size-tiered.
- **Q4 (marking outline):** Regions own contiguous key ranges; consecutive timestamps are consecutive keys, so all new keys fall in the last range; a salt or reversal spreads consecutive keys across the key space and thus across regions; but a scan of a time range now has to touch every salt bucket and merge, which multiplies the number of scans.
- **Q5 (what a passing submission shows):** Tablets that split as they grow, a hot-spot measured for monotone keys, balanced load with salting, and the scan-cost trade-off.

</details>

### U10.6 In-memory key-value stores and the families of NoSQL databases
**Sources:** BDC W4
- **Topics:** Introduction to Big Data Storage Platforms for Large Scale Data Storage (the remainder of Week 4 beyond the file-system and column-store systems of U10.2 and U10.5; the published outline gives no sub-list, so the families below are *inferred* from the field's standard taxonomy): key-value stores and in-memory stores (Redis-style data structures, expiry, persistence by snapshot and append-only file, replication), document stores (JSON documents, secondary indexes, aggregation pipelines), column-family stores (U10.4 and U10.5), graph databases (property graph, traversal); the CAP and PACELC placement of each family; choosing a store by access pattern, consistency need and scale; polyglot persistence.
- **Results:** An LRU cache with a hash map and a doubly-linked list performs get and put in O(1) [P]; an append-only file with periodic rewrite bounds recovery time at the log length since the last snapshot [D]; the hit ratio of a cache under a Zipf(s) workload of N items and capacity C is well approximated by the ratio of generalised harmonic sums H(C, s)/H(N, s) for an ideal frequency-based policy [D].
- **Build:** a Redis-style in-memory server on sockets speaking a simple text protocol with strings, lists, hashes, expiry, snapshot and append-only persistence and crash recovery; an LRU and an LFU cache against a Zipf workload with the hit ratio against the formula; a document store with a secondary index; a decision table placing each family on CAP. [local]
- **Gap-fills:** *[inferred: Sadalage–Fowler, NoSQL Distilled; the Redis documentation, recalled, not checked]* vector databases for embeddings as the family that postdates the source.

**Assignment A10.6** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Which pair of structures gives O(1) get and put for an LRU cache?

(A) A hash map and a doubly-linked list  
(B) A sorted array  
(C) A binary heap  
(D) A stack

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) An append-only file with periodic rewrite bounds recovery time by the log since the last snapshot  
(B) A Zipf workload gives a high hit ratio from a small cache  
(C) Consistent hashing lets a cache cluster add a node with only a fraction of the keys moving  
(D) Cache-aside never serves stale data

**Q3 (2 marks, numerical answer (ratio)).** Under Zipf with exponent 1, an ideal cache holds the 100 most popular of 1000 items. What is the hit ratio, the ratio of the harmonic sums H(100) to H(1000) (two decimals)?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that an LRU cache built from a hash map and a doubly-linked list performs get and put in constant time.

**Q5 (3 marks, programming).** Implement an LRU cache and an LFU cache, a Redis-style store with a snapshot and an append-only log with recovery, a consistent-hash cluster, and measure hit ratios under Zipf workloads against the formula. Add a memcached-style cache-aside experiment with invalidation and stale reads.

<details><summary>Key for A10.6 (open only after your attempt)</summary>

- **Q1:** A. The map finds the node and the list moves it to the front in constant time.
- **Q2:** A, B, C. Cache-aside can serve stale data until expiry or invalidation.
- **Q3:** 0.693 ratio (tolerance ±0.005). 5.187 over 7.485 is about 0.69.
- **Q4 (marking outline):** The map from key to node finds any entry in expected constant time; on a hit the node is unlinked from the list and relinked at the head, which takes constant time given the node's neighbour pointers; on a put into a full cache the tail node is removed, its key deleted from the map and the new node inserted at the head, all constant-time operations.
- **Q5 (what a passing submission shows):** O(1) operations verified by timing, hit ratios close to the harmonic-sum estimate, correct recovery after a crash from log and snapshot, and measured staleness windows.

</details>

### U10.7 Google Cloud storage and database options
**Sources:** GCF W3
- **Topics:** Where do I store this stuff? (the published outline gives this title only, so the content is *inferred* from the platform's storage documentation): object storage (buckets and objects, storage classes ordered by access frequency and by minimum storage duration, lifecycle rules, versioning, signed URLs, access control by IAM from U7.7, customer-managed encryption keys from U5.18, consistency model, data transfer), block storage (persistent disks) and file storage, managed relational databases (the SQL service with replicas and failover, and the horizontally scalable globally consistent database of U9.18), the wide-column service (U10.5), the document database, the in-memory service (U10.6), the analytics warehouse (U12.2); a decision procedure for choosing among them by data shape, access pattern, consistency, latency, scale and cost; backup, replication across regions and the recovery objectives of U8.4.
- **Results:** The cheapest storage class for an object with monthly reads r, size s, and per-class storage price a_c, retrieval price b_c and minimum duration d_c is the minimiser of a piecewise-linear cost over classes, with break-even read rates found by equating costs [D]; egress and operation charges can dominate for small objects [D].
- **Build:** a cost model parametrised by prices you enter from the current price list (no prices are asserted here) that picks a class and finds the break-even access rates; a rule-based store selector tested on ten scenario descriptions; a lifecycle-policy simulator. A real bucket and database can be created in a lab project at the free tier or with credit, with budget alerts and teardown. [local; credit]
- **Gap-fills:** *[inferred: the platform's storage-options documentation, recalled, not checked]* product names and tiers change; read the live documentation before relying on any limit.

**Assignment A10.7** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** When is a colder storage class the cheaper choice for an object?

(A) When it is read rarely enough that lower storage cost outweighs the retrieval charges  
(B) Always  
(C) Never  
(D) When the object is small and read often

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Egress and operation charges can dominate for small objects  
(B) Minimum storage durations create a cost for early deletion  
(C) The cheapest class depends on the expected read rate  
(D) A managed database removes the need to choose a consistency model

**Q3 (2 marks, numerical answer (GB per GB-month)).** With illustrative prices, Nearline costs 0.010 per GB-month plus 0.010 per GB retrieved and Coldline costs 0.004 per GB-month plus 0.020 per GB retrieved. At how many GB retrieved per GB stored per month are they equal?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that for two storage classes with monthly cost a1 plus b1 r and a2 plus b2 r, where a1 is greater than a2 and b1 is less than b2, there is a unique read rate at which they cost the same and the second class is cheaper below it.

**Q5 (3 marks, programming).** Write a cost model for a storage lifecycle policy with classes, minimum durations, retrieval and operation charges, given a trace of object accesses, and find the best policy by dynamic programming; map your toy store, key-value store and wide-column store to the Google Cloud options in a table that names the consistency and scaling properties.

<details><summary>Key for A10.7 (open only after your attempt)</summary>

- **Q1:** A. The cost is piecewise linear in the read rate; the break-even is where the lines cross.
- **Q2:** A, B, C. You still choose the consistency and availability configuration.
- **Q3:** 0.6 GB per GB-month (tolerance ±0.01). Equating gives 0.010 plus 0.010 r equals 0.004 plus 0.020 r, so r = 0.6. Prices are for the exercise, not current.
- **Q4 (marking outline):** The difference of the costs is a linear function of r equal to (a1 minus a2) minus (b2 minus b1) r, positive at r = 0 and decreasing, so it crosses zero once at r equal to (a1 minus a2) over (b2 minus b1); below that rate the second class costs less.
- **Q5 (what a passing submission shows):** A cost calculator whose output matches a hand calculation on small traces, a policy that beats fixed classes on a skewed trace, and a mapping table with sources named.

</details>


# PART D. BIG DATA, CLOUD OPERATIONS AND MACHINE LEARNING ON THE CLOUD

## D11. Big data and cloud analytics: batch, dataflow, messaging, streaming, machine learning at scale and graph processing

Aim: the data-processing half of the big-data course and the cloud-course weeks on MapReduce, Spark and Kafka, merged and reordered so that each engine is built in miniature before it is compared with the real system: first the batch model (MapReduce), then the in-memory dataflow model (Spark), then the other dataflow systems of the advanced course (Condor, DryadLINQ), then messaging and streaming, then machine learning on top of the engines, then graph processing. Two bridges, on machine learning and on Markov chains and PageRank, are taught immediately before the units that need them. The depth of machine learning itself is in the earlier unified curriculum; this domain takes only what the engines need. Benchmarks (recalled, not checked): Baesens, *Analytics in a Big Data World* and Leskovec, Rajaraman and Ullman, *Mining of Massive Datasets* (both named in the source); Lam, *Hadoop in Action*; Deroos et al., *Hadoop for Dummies* (named in the source); Witten and Frank, *Data Mining* (named in the source); Karau et al., *Learning Spark*; Kleppmann, *Designing Data-Intensive Applications*; and the primary papers (MapReduce, Spark RDDs, Pregel, Kafka) named in each unit.

### U11.1 Introduction to big data
**Sources:** BDC W1, o
- **Topics:** Introduction to Big Data, and the course outline: the explosion of data generated by sensors (climate data), social-media posts, digital pictures and videos, purchase transactions and GPS signals; the characteristics of big data (volume, velocity, variety and, in the common extended lists, veracity and value) and why conventional single-machine tools stop working; the data-science pipeline (acquisition, storage, processing, analysis, visualisation, decision); batch versus interactive versus streaming workloads; scale-up versus scale-out; the course's stated prerequisites (data structures and algorithms, computer architecture, operating systems, database management systems) revisited in the bridges U1.2, U4.1 and U10.1; analytics for business (the textbook's view). The big-data outline's own examples of data growth are sensors, social media, digital pictures and videos, purchase transaction records and GPS signals from cell phones, and its industry list names Amazon, Microsoft, Google, IBM and Facebook.
- **Results:** Amdahl: with serial fraction s the speed-up on p processors is at most 1/(s + (1 − s)/p) [P]; Gustafson's scaled speed-up is p − s(p − 1) [D]; reading 1 TB at a sequential rate of 150 MB/s takes about 1.9 hours on one disk and about 4 minutes on 30 disks in parallel, the arithmetic that motivates scale-out [D, by computation].
- **Build:** a back-of-envelope scale calculator (data size, bandwidth, parallelism, cost per node, failure rate) with the Amdahl and Gustafson curves and a table of how many machines a given job needs; a synthetic data generator (sensor, click-stream and transaction schemas) used by the later units in this domain. [local]
- **Gap-fills:** *[inferred: Dean–Ghemawat; the Hadoop-era literature on the 3 Vs, recalled, not checked]* the data-lake and lakehouse idioms (named).

**Assignment A11.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** With serial fraction s of a program, what is the maximum speed-up on p processors by Amdahl's law?

(A) 1 over (s plus (1 minus s)/p)  
(B) p  
(C) s times p  
(D) 1 minus s

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Amdahl's law bounds the speed-up by 1 over the serial fraction  
(B) Gustafson's scaled speed-up is p minus s(p minus 1)  
(C) Scale-out is motivated by the time to read data sequentially from one disk  
(D) Gustafson's and Amdahl's laws answer the same question with the same assumptions

**Q3 (2 marks, numerical answer (times)).** A job has a serial fraction of 0.1 and runs on 10 processors. What is the Amdahl speed-up (two decimals)?

**Q4 (2 marks, prove or derive; every step with its reason).** Derive Amdahl's law and show that the speed-up can never exceed 1/s however many processors are used.

**Q5 (3 marks, programming).** Write a scaling calculator for Amdahl, Gustafson and the universal scalability law, fit the serial and contention parameters to measured timings of a parallel word-count run with multiprocessing, and tabulate the time to read 1 TB on d disks at stated rates.

<details><summary>Key for A11.1 (open only after your attempt)</summary>

- **Q1:** A. The serial part is not sped up, so the speed-up is bounded by 1/s.
- **Q2:** A, B, C. Amdahl fixes the problem size; Gustafson scales it with the machine.
- **Q3:** 5.263 times (tolerance ±0.01). 1 over (0.1 plus 0.09) is about 5.26.
- **Q4 (marking outline):** Let the single-processor time be T; the serial part takes sT and the parallel part (1 minus s)T divided by p on p processors; the speed-up is T over the sum, 1/(s plus (1 minus s)/p); as p grows the second term falls toward zero, so the speed-up approaches but never exceeds 1/s.
- **Q5 (what a passing submission shows):** A fit whose predicted speed-ups match measurements within error, curves showing the ceilings, and arithmetic that matches a hand calculation.

</details>

### U11.2 Enabling technologies for big data: clusters, virtualisation, containers and orchestration
**Sources:** BDC W2
- **Topics:** Introduction to Enabling Technologies for Big Data (the published outline gives this title only, so the content below is *inferred* from the field's usual list and from the cloud-computing units already taught): commodity clusters and the data-centre as a computer, cloud computing service and deployment models (U1.1), virtualisation and containers (U4.2 to U4.4) as the way clusters are shared, cluster resource management and scheduling (the provisioning ideas of U4.3 and the placement problems of U4.5) applied to data-processing jobs, the storage hierarchy and its bandwidth and latency numbers, data locality and moving computation to data, parallel and distributed programming models and what each hides, and the economics of renting versus owning.
- **Results:** First-fit decreasing bin-packing uses at most 11/9·OPT + 6/9 bins [X]; the cost of moving computation to the data is the ratio of code size to data size, which is why locality-aware schedulers pay off whenever data dwarfs code [D]; the latency-numbers hierarchy spans about seven orders of magnitude from cache to wide-area network [Def, from the figures in the unit's table].
- **Build:** a cluster scheduler simulation placing jobs with locality constraints by first-fit, best-fit and a delay-scheduling rule, measuring the fraction of data-local tasks and the makespan; a latency-and-bandwidth table you fill from your own micro-benchmarks of memory, local disk and loopback network. [local]
- **Gap-fills:** *[inferred: Barroso–Clidaras–Hölzle, The Datacenter as a Computer; Zaharia et al., delay scheduling, EuroSys 2010, recalled, not checked]* Kubernetes as the present-day orchestrator (named; its use in the capstone U13.5 is optional).

**Assignment A11.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Which bin-packing heuristic sorts items by decreasing size before placing each in the first bin that fits?

(A) Next-fit  
(B) First-fit decreasing  
(C) Best-fit increasing  
(D) Random-fit

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Containers share the host kernel while virtual machines run their own kernels  
(B) Moving computation to data pays off when data is much larger than code  
(C) An orchestrator reconciles desired state with observed state in a loop  
(D) A container gives the same isolation as a hardware virtual machine

**Q3 (2 marks, numerical answer (bins)).** First-fit decreasing uses at most 11/9 times OPT plus 6/9 bins. For OPT = 9, what is the largest whole number of bins it can use?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that first-fit never leaves two bins that are each at most half full, and hence uses fewer than 2 OPT plus 1 bins.

**Q5 (3 marks, programming).** Write a cluster scheduler simulator with first-fit, best-fit and first-fit decreasing placement and measure bins used against a lower bound, a locality-aware task placement experiment, and a small reconciliation-loop controller for desired replicas. For learning only, local containers as in the bridge labs.

<details><summary>Key for A11.2 (open only after your attempt)</summary>

- **Q1:** B. First-fit decreasing is the standard tight heuristic.
- **Q2:** A, B, C. Containers share the kernel and so isolate less strongly.
- **Q3:** 11 bins (tolerance ±0). 11 plus 0.67 is 11.67, so at most 11 bins.
- **Q4 (marking outline):** If two bins were each at most half full, an item of the later bin would have fitted in the earlier one, contradicting first-fit; so at most one bin is at most half full and the others are more than half full; the total size is therefore more than (B minus 1)/2 for B bins, and the optimum is at least the total size, so B is less than 2 OPT plus 1.
- **Q5 (what a passing submission shows):** Bin counts within the stated guarantees, a locality experiment showing reduced data movement and a controller that heals killed replicas.

</details>

### U11.3 Big data platforms I: Hadoop and the MapReduce model
**Sources:** BDC W3; DS W7; CCDS W8
- **Topics:** Introduction to Big Data Platforms (Week 3) and the MapReduce lecture of the cloud course's Week 8; Case Studies: Map Reduce (Week 7 of the classical course): the paradigm and the programming model (map, shuffle and sort, reduce, with combiners and partitioners), applications (word count, inverted index, join, grep, sort, PageRank iteration), scheduling and locality, fault tolerance by re-execution and speculative execution of stragglers, an implementation overview (master, workers, intermediate files), the Hadoop ecosystem around it (HDFS from U10.2, the resource manager, Hive and Pig as higher-level languages); design of joins (reduce-side, map-side, broadcast) and of skew handling.
- **Results:** The map-reduce tradeoff for the all-pairs similarity job is that reducer size q and replication rate r satisfy r ≥ n/q for n inputs [S]; the total communication of word count is bounded by the number of distinct (word, mapper) pairs when a combiner is used [D]; with p workers, per-task failure probability f and re-execution, the expected number of task executions is 1/(1 − f) per task [D]; speculative execution cuts expected completion when the straggler tail is heavy [D].
- **Build:** a mini-MapReduce engine on Python's `multiprocessing` with a partitioner, combiner, sorted shuffle, worker-failure injection and speculative re-execution; word count, inverted index, reduce-side join, matrix multiplication in two passes and one PageRank iteration on it, each checked against a single-process version and timed. [local]
- **Gap-fills:** *[inferred: Dean–Ghemawat, MapReduce, OSDI 2004; Afrati–Ullman on the cost model of MapReduce algorithms, recalled, not checked]* YARN's separation of resource management from the programming model.

**Assignment A11.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** In MapReduce, what is the purpose of a combiner?

(A) To reduce the amount of data sent over the network by aggregating map output locally  
(B) To sort the final output  
(C) To start the reducers  
(D) To encrypt data

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Re-executing failed tasks costs on average 1/(1 minus f) executions per task for failure probability f  
(B) Speculative execution helps when a few stragglers dominate completion time  
(C) The reducer size q and replication rate r obey r at least n/q in the all-pairs example  
(D) MapReduce guarantees exactly-once side effects in mapper code

**Q3 (2 marks, numerical answer (executions)).** Each task fails independently with probability 0.2 and is re-run until it succeeds. How many task executions are expected for 1000 tasks?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that the expected number of executions of a task that fails independently with probability f on each attempt is 1/(1 minus f).

**Q5 (3 marks, programming).** Write a MapReduce engine in Python with map, combine, partition, shuffle and reduce phases, failure injection and speculative execution in DSim, then run word count, inverted index, a join and PageRank-style iteration on it, and compare with a Hadoop streaming run in the local lab if you install it.

<details><summary>Key for A11.3 (open only after your attempt)</summary>

- **Q1:** A. A combiner pre-aggregates before the shuffle.
- **Q2:** A, B, C. Re-execution can repeat side effects.
- **Q3:** 1250 executions (tolerance ±1). Each task needs 1/(1 minus 0.2) = 1.25 executions on average, so 1250.
- **Q4 (marking outline):** The number of attempts is geometric: success on attempt k has probability f to the power (k minus 1) times (1 minus f); its mean is the sum over k of k f^(k minus 1)(1 minus f), which equals 1/(1 minus f) by the series for the derivative of 1/(1 minus f).
- **Q5 (what a passing submission shows):** Outputs identical to a single-process reference, retries matching the expected executions, and a measured effect of speculation under stragglers.

</details>

### U11.4 Big data platforms II: Apache Spark and resilient distributed datasets
**Sources:** BDC W3; CCDS W8; DS W7
- **Topics:** Introduction to Spark: Resilient Distributed Datasets (RDDs), RDD Operations (Week 8 of the cloud course); Case Studies: Spark (Week 7 of the classical course); platform comparison with MapReduce: in-memory reuse, lazy evaluation, the lineage graph, transformations and actions, narrow versus wide dependencies, the DAG scheduler, stage boundaries at shuffles, caching and persistence levels, fault tolerance by recomputing lost partitions from lineage, shared variables (broadcast and accumulators), the DataFrame and SQL layers and their optimiser; Spark applications as the source lists them (PageRank, with GraphX in U11.11).
- **Results:** A stage boundary exists exactly at each wide dependency [Def]; recovering a lost partition recomputes only its ancestors through narrow dependencies, at cost proportional to the lineage depth [D]; for an iterative algorithm of T passes over a dataset that fits in memory, caching reduces I/O from T full reads to one [D]; a wide dependency on a hash-partitioned key shuffles each record to exactly one destination partition [Def].
- **Build:** a mini-Spark in Python: an RDD class with lazy transformations (map, filter, flatMap, reduceByKey, join, groupByKey), a lineage graph, a DAG scheduler that cuts stages at shuffles, caching, and partition-loss recovery by recomputation, with a test that kills partitions and compares the result; the same jobs run on PySpark in local mode as an oracle where it can be installed. [local]
- **Gap-fills:** *[inferred: Zaharia et al., NSDI 2012; the Spark documentation, recalled, not checked]* Catalyst and Tungsten (named), structured streaming (U11.7).

**Assignment A11.4** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Where does Spark place a stage boundary?

(A) At every operator  
(B) At each wide dependency that needs a shuffle  
(C) Only at the end  
(D) At each action

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Recovering a lost partition re-runs its lineage from the ancestors  
(B) Caching helps iterative algorithms by reading input once  
(C) A wide dependency shuffles records to the partition chosen by the key  
(D) Lineage recovery cost does not depend on the length of the lineage

**Q3 (2 marks, numerical answer (reads)).** An iterative algorithm makes 20 passes over a dataset that fits in memory. How many full disk reads does caching save compared with no caching?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that recomputing a lost partition under narrow dependencies requires recomputing exactly one partition at each ancestor level, and so costs time proportional to the lineage depth.

**Q5 (3 marks, programming).** Implement a small RDD engine with lazy transformations, narrow and wide dependencies, stage construction, lineage-based recovery by killing a worker mid-job and caching, and compare with PySpark in the local lab on word count and iterative PageRank for output equality.

<details><summary>Key for A11.4 (open only after your attempt)</summary>

- **Q1:** B. Narrow dependencies pipeline within a stage.
- **Q2:** A, B, C. Longer lineage means more recomputation, which is why checkpoints help.
- **Q3:** 19 reads (tolerance ±0). Without caching there are 20 full reads and with caching one, saving 19.
- **Q4 (marking outline):** A narrow dependency makes each child partition depend on a bounded number of parent partitions, here one; so the lost partition depends on one partition at the previous level, which depends on one at the level before, and so on; the chain has as many partitions as the lineage depth, each recomputed once.
- **Q5 (what a passing submission shows):** Outputs equal to PySpark, recovery recomputing only the lost partitions, and measured speed-ups from caching.

</details>

### U11.5 Dataflow systems beyond MapReduce: Condor and DryadLINQ
**Sources:** ADS W12
- **Topics:** Condor, and Microsoft DryadLINQ (the last week of the advanced course, which also lists Voldemort, taught in U10.3): high-throughput computing on idle workstations, the ClassAd language and matchmaking of jobs to machines by requirements and rank, checkpointing and remote system calls for migration, the master-worker pattern; Dryad as a general dataflow DAG engine (vertices, channels, a job manager that schedules vertices and re-runs failed ones), DryadLINQ as the compiler from LINQ queries in a host language to a Dryad plan, and how this generalises the two-stage MapReduce graph.
- **Results:** The ClassAd matchmaking problem is bipartite matching with predicate edges and a rank order, solvable by greedy matching only if ranks are consistent, and by maximum-weight matching in general (U3.2) [D]; the completion time of a DAG job on unlimited machines is the length of its critical path, and on p machines is at least max(critical path, work/p) [P]; a vertex that fails can be re-run from its deterministic inputs without restarting the job [D].
- **Build:** a ClassAd-style matchmaker with its own small expression parser and evaluator (no `eval` of untrusted text) and rank-based matching with a checker against a maximum-weight matching; a LINQ-like query builder that compiles to a DAG, a scheduler that runs it with vertex-failure injection, and a comparison with your MapReduce engine on a multi-stage query. [local]
- **Gap-fills:** *[inferred: Litzkow–Livny–Mutka 1988; Isard et al., Dryad, EuroSys 2007; Yu et al., DryadLINQ, OSDI 2008, recalled, not checked]* Apache Beam's model as the present-day heir (U12.2).

**Assignment A11.5** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** On p identical machines, what is a lower bound on the completion time of a DAG job with critical path length C and total work W?

(A) The larger of C and W/p  
(B) The smaller of C and W/p  
(C) C plus W  
(D) W times p

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Matchmaking in Condor can be viewed as bipartite matching with predicate edges  
(B) A failed vertex in a deterministic dataflow can be re-run from its inputs  
(C) A DAG engine can optimise across stages unlike plain MapReduce  
(D) The critical path is the shortest path through the DAG

**Q3 (2 marks, numerical answer (seconds)).** A DAG job has a critical path of 12 s and total work of 60 s. What is the lower bound on its completion time on 4 machines?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove that the completion time of a DAG job on p machines is at least the maximum of the critical path length and work divided by p.

**Q5 (3 marks, programming).** Write a ClassAd-style matchmaker with requirements and rank expressions over job and machine records compared against maximum-weight matching from the bridge unit, and a DAG executor with a list scheduler that handles vertex failure and compares its makespan with the lower bound on random DAGs.

<details><summary>Key for A11.5 (open only after your attempt)</summary>

- **Q1:** A. No schedule can beat the critical path or the average work per machine.
- **Q2:** A, B, C. The critical path is the longest path.
- **Q3:** 15 seconds (tolerance ±0.01). The bound is the larger of 12 and 15, which is 15.
- **Q4 (marking outline):** The tasks along a critical path depend on each other and must run in sequence, so the time is at least its length; the p machines can do at most p units of work per unit time, so finishing total work W takes at least W over p; both bounds hold at once, so the time is at least their maximum.
- **Q5 (what a passing submission shows):** Matches that satisfy all requirements, a makespan never below the lower bound, and failed vertices re-run without restarting the job.

</details>

### U11.6 Apache Kafka: the distributed commit log and messaging systems
**Sources:** BDC W5; CCDS W8
- **Topics:** Introduction to Kafka: what Kafka is, use cases for Kafka, data model, architecture, types of messaging systems, importance of brokers (Week 8 of the cloud course) and the streaming-platforms week of the big-data course; the log abstraction, topics and partitions, offsets, segments and indexes, producers and partitioning keys, consumers and consumer groups with partition assignment and rebalancing, replication with leader and in-sync replicas (the protocol of U9.14 in spirit), retention and log compaction, delivery semantics (at-most-once, at-least-once, exactly-once by idempotent producers and transactions), why sequential disk I/O and the page cache give throughput, and the contrast between queueing and publish–subscribe models.
- **Results:** Order is guaranteed within a partition and not across partitions [Def]; with replication factor r and in-sync-replica minimum m, writes with full acknowledgment survive r − m broker losses without losing acknowledged data, and the topic stays writable while at least m replicas are in sync [D]; exactly-once effect is at-least-once delivery plus idempotent processing keyed by a producer identity and sequence number [P]; the rebalance protocol assigns each partition to exactly one consumer in a group [Def].
- **Build:** a mini-Kafka: an append-only segmented log with an offset index, a broker with partitions and leader–follower replication over DSim with an in-sync-replica set, producers with keyed partitioning, consumer groups with rebalancing and committed offsets, an idempotent producer with sequence numbers, crash tests checking no acknowledged message is lost and none is delivered twice to the effect of the consumer. [local]
- **Gap-fills:** *[inferred: Kreps–Narkhede–Rao, Kafka, NetDB 2011; the Kafka documentation, recalled, not checked]* the managed equivalent on the cloud platform (Pub/Sub, U12.2).

**Assignment A11.6** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What ordering does a Kafka topic guarantee?

(A) A total order across all partitions  
(B) Order within a partition only  
(C) No order at all  
(D) Order by message size

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) A consumer group assigns each partition to exactly one consumer  
(B) With replication factor r and minimum in-sync replicas m, full acknowledgement survives r minus m broker losses without losing acknowledged data  
(C) Exactly-once effect can be built from at-least-once delivery with idempotent processing  
(D) Kafka removes messages as soon as a consumer reads them

**Q3 (2 marks, numerical answer (brokers)).** A topic has replication factor 5 and the minimum in-sync replica count is 3. How many broker losses can acknowledged data survive?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that at-least-once delivery combined with a consumer that ignores any message whose producer identity and sequence number it has already processed gives exactly-once effect.

**Q5 (3 marks, programming).** Implement a partitioned replicated commit log in DSim with leaders, followers, in-sync replicas, offsets, consumer groups with rebalance and an idempotent producer. Test with broker crashes and verify no loss of acknowledged messages and no duplicates in the output.

<details><summary>Key for A11.6 (open only after your attempt)</summary>

- **Q1:** B. Order is guaranteed within a partition and not across partitions.
- **Q2:** A, B, C. Kafka retains messages by a retention policy, not by consumption.
- **Q3:** 2 brokers (tolerance ±0). The bound is r minus m = 2.
- **Q4 (marking outline):** At-least-once delivery ensures every message arrives one or more times; the consumer applies a message only the first time its pair of producer identity and sequence number is seen, since later duplicates are recognised and dropped; the effect is therefore applied once; this needs the record of seen sequence numbers to be persisted atomically with the effect.
- **Q5 (what a passing submission shows):** No acknowledged message lost within the replica bound, per-partition order preserved, and duplicates suppressed.

</details>

### U11.7 Stream processing and approximate algorithms: windows, event time and sketches
**Sources:** BDC W5
- **Topics:** Introduction to Big Data Streaming Platforms for Fast Data (Week 5; the sub-topics are *inferred* from the field's standard content): the data-stream model with one pass and sublinear memory; windows (tumbling, sliding, session), event time versus processing time, watermarks and late data, micro-batch versus record-at-a-time engines (Spark Streaming and its successors, Storm, Flink), state, checkpointing and exactly-once; synopsis structures for streams: reservoir sampling, the Bloom filter (U10.4), the Count-Min sketch, the Misra–Gries heavy hitters, Flajolet–Martin and HyperLogLog cardinality estimators, and the lambda and kappa architectures.
- **Results:** Reservoir sampling keeps each of n items with probability k/n [P]; the Count-Min sketch with width ⌈e/ε⌉ and depth ⌈ln(1/δ)⌉ overestimates any count by at most εN with probability at least 1 − δ and never underestimates [P]; Misra–Gries with k counters finds every item of frequency above N/(k + 1) [P]; HyperLogLog with m registers has relative standard error about 1.04/√m [recalled, not checked; the unit's script measures it].
- **Build:** a windowed aggregation engine with event-time windows, watermarks and late-data handling on a synthetic disordered stream; reservoir sampling, Count-Min, Misra–Gries, Flajolet–Martin and HyperLogLog against exact answers with the error bounds measured; a checkpointed stateful operator with a crash test. [local]
- **Gap-fills:** *[inferred: Cormode–Muthukrishnan 2005; Flajolet et al. 2007; Akidau et al., the Dataflow model, VLDB 2015, recalled, not checked]* Beam and the cloud dataflow service (U12.2).

**Assignment A11.7** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** In reservoir sampling with reservoir size k over a stream of n items, what is the probability that each item is in the sample at the end?

(A) k over n  
(B) 1 over n  
(C) 1 over k  
(D) 1

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Count-Min never underestimates a count  
(B) Misra-Gries with k counters finds every item of frequency above N/(k plus 1)  
(C) HyperLogLog estimates the number of distinct items with a standard error near 1.04 over the square root of m  
(D) Count-Min can underestimate counts

**Q3 (2 marks, numerical answer (counters)).** A Count-Min sketch is built with error parameter 0.001 and failure probability 0.01, with width the ceiling of e/epsilon and depth the ceiling of ln(1/delta). How many counters does it hold?

**Q4 (2 marks, prove or derive; every step with its reason).** Prove by induction that reservoir sampling keeps each of the first n items with probability k/n.

**Q5 (3 marks, programming).** Implement reservoir sampling, a sliding-window counter, Count-Min, Misra-Gries and HyperLogLog, test them on Zipf streams for error against the bounds, and write a windowed event-time aggregator with watermarks in DSim.

<details><summary>Key for A11.7 (open only after your attempt)</summary>

- **Q1:** A. Each item ends up in the sample with probability k/n.
- **Q2:** A, B, C. Count-Min only overestimates because collisions add counts.
- **Q3:** 13595 counters (tolerance ±0). The width is 2719 and the depth 5, so 13,595.
- **Q4 (marking outline):** For n = k all items are kept; assume each of n minus 1 items is in the reservoir with probability k/(n minus 1); the n-th item enters with probability k/n; an earlier item stays if it was there and was not evicted: it is evicted with probability (k/n)(1/k) = 1/n, so it stays with probability k/(n minus 1) times (n minus 1)/n = k/n.
- **Q5 (what a passing submission shows):** Errors within the bounds with the stated probability, no false negatives for heavy hitters, and late events handled by the watermark rule.

</details>

### U11.8 Bridge: machine-learning foundations for scalable learning
**Sources:** none (prerequisite bridge, added so that later units rest on taught ground)
Bridge for: U11.9 (machine learning on the engines), U12.3 (machine learning on the cloud platform). A compact version of the foundations; the full treatment is in the earlier unified machine-learning curriculum.
- **Topics:** Supervised and unsupervised learning; empirical risk and loss functions; linear and logistic regression and the normal equations; gradient descent, mini-batches and learning-rate behaviour; regularisation and the bias–variance trade-off; evaluation (train, validation and test splits, cross-validation, precision, recall, ROC and AUC); k-means and Lloyd's algorithm; nearest-neighbour methods; decision trees and ensembles; matrix factorisation for recommendation.
- **Results:** The least-squares solution satisfies XᵀXw = Xᵀy [D]; the logistic-loss gradient is Xᵀ(σ(Xw) − y) [D]; Lloyd's algorithm never increases the k-means objective and terminates [P]; expected squared error decomposes into bias squared, variance and noise [P].
- **Build:** NumPy implementations of linear and logistic regression (closed form and gradient descent), k-means, k-nearest neighbours and a decision stump ensemble on synthetic data, with a train/validation/test harness and cross-validation, each checked against a reference library. [local]
- **Gap-fills:** *[inferred: Hastie–Tibshirani–Friedman; Witten–Frank (named in the source), recalled, not checked]* stochastic gradient descent theory is in the earlier curriculum.

**Assignment A11.8** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What equations does the least-squares solution satisfy?

(A) X transpose X w equals X transpose y  
(B) X w equals 0  
(C) w equals y  
(D) X transpose w equals y

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) The gradient of the logistic loss is X transpose times (sigma of Xw minus y)  
(B) Lloyd's algorithm never increases the k-means objective  
(C) Expected squared error decomposes into bias squared, variance and noise  
(D) More features always lower the test error

**Q3 (2 marks, numerical answer).** Fit y = w0 plus w1 x by least squares to the points (0, 1), (1, 2), (2, 4). What is the slope w1?

**Q4 (2 marks, prove or derive; every step with its reason).** Derive the normal equations for least squares.

**Q5 (3 marks, programming).** Implement linear and logistic regression with gradient descent, k-means with Lloyd's algorithm and a bias-variance experiment from scratch in NumPy, checking against scikit-learn as an oracle.

<details><summary>Key for A11.8 (open only after your attempt)</summary>

- **Q1:** A. These are the normal equations.
- **Q2:** A, B, C. Extra features can raise test error through variance.
- **Q3:** 1.5 (tolerance ±0.001). The normal equations give w0 = 5/6 and w1 = 1.5.
- **Q4 (marking outline):** The loss is the squared norm of y minus Xw; its gradient with respect to w is minus 2 X transpose (y minus Xw); setting it to zero gives X transpose X w equals X transpose y; the loss is convex, so a stationary point is a minimiser.
- **Q5 (what a passing submission shows):** Parameters matching the closed form and the library within tolerance, a non-increasing k-means objective, and a plotted or tabulated bias-variance curve.

</details>

### U11.9 Big data applications: machine learning with Spark
**Sources:** BDC W6–7
- **Topics:** Introduction to Big Data Applications (Machine Learning) (Week 6) and Introduction of Big Data Machine Learning with Spark (Week 7): the algorithms of U11.8 expressed as passes over distributed data: data-parallel gradient descent with gradient aggregation (tree aggregation), distributed k-means where each iteration is a map (assign) and a reduce (recompute centres), the alternating-least-squares algorithm for collaborative filtering, distributed decision trees and random forests, the Spark MLlib pipeline abstraction (transformers, estimators, pipelines, parameter grids), feature engineering at scale, the parameter-server architecture as an alternative, and the communication cost model.
- **Results:** The gradient of a sum of per-example losses is the sum of per-example gradients, so it decomposes over partitions and aggregates with an associative, commutative reduce [P]; each distributed gradient step communicates O(d) values per worker against O(nd/p) local computation, so speed-up holds while computation dominates communication [D]; in ALS each user's factor solves a d-by-d regularised normal equation given the item factors, so users can be updated in parallel [D].
- **Build:** data-parallel logistic regression, k-means and ALS on your mini-Spark of U11.4 with weak and strong scaling measured, each compared to PySpark MLlib in local mode as an oracle where installable; a communication-cost model compared with the measured times. [local]
- **Gap-fills:** *[inferred: Meng et al., MLlib, JMLR 2016; Li et al., the parameter server, OSDI 2014, recalled, not checked]* large-scale deep-learning training (links to U12.3).

**Assignment A11.9** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Why can a gradient be computed in parallel over data partitions?

(A) The gradient of a sum of per-example losses is the sum of per-example gradients  
(B) The loss is zero  
(C) The data is sorted  
(D) Gradients are random

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Each distributed gradient step communicates about d values per worker  
(B) In ALS each user's factor solves a regularised normal equation given the item factors  
(C) Speed-up of distributed gradient descent holds while computation dominates communication  
(D) ALS updates must be done one user at a time

**Q3 (2 marks, numerical answer (values)).** With 50 workers each sending a gradient of d = 1000 values per step, how many values are gathered per step?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that the gradient of a sum of per-example losses over data partitioned into p parts can be computed as the sum over partitions of the gradient on each part.

**Q5 (3 marks, programming).** Implement data-parallel gradient descent over partitions using your RDD engine, ALS matrix factorisation on a synthetic ratings matrix, and k-means on partitions, then compare with Spark MLlib in the local lab for output agreement and measure speed-up against workers.

<details><summary>Key for A11.9 (open only after your attempt)</summary>

- **Q1:** A. Partial sums computed per partition can be added by an associative, commutative reduce.
- **Q2:** A, B, C. Users can be updated in parallel given the item factors.
- **Q3:** 50000 values (tolerance ±0). 50 times 1000 = 50,000.
- **Q4 (marking outline):** Differentiation is linear, so the gradient of a sum is the sum of the gradients; grouping the examples by partition, the total is the sum over partitions of the partial sums; the sum is associative and commutative, so the partials can be combined in any order in a tree reduce.
- **Q5 (what a passing submission shows):** Results equal to the single-machine versions, a speed-up curve that flattens as communication grows, and ALS reconstruction error falling per iteration.

</details>

### U11.10 Bridge: Markov chains, eigenvectors and PageRank
**Sources:** none (prerequisite bridge, added so that later units rest on taught ground)
Bridge for: U11.11 (graph processing). Builds on the random-walk material of U9.2.
- **Topics:** Finite Markov chains, transition matrices, stationary distributions, irreducibility and aperiodicity, the Perron–Frobenius theorem (stated), mixing and the second eigenvalue, the random-surfer model of the web, PageRank with damping and the teleport vector, dangling nodes, power iteration, personalised PageRank, and the convergence rate.
- **Results:** An irreducible aperiodic finite chain has a unique stationary distribution and converges to it [X, Perron–Frobenius]; the PageRank matrix with damping α has second eigenvalue of modulus at most α, so power iteration reaches error ε in about ln ε / ln α iterations [P]; the stationary distribution of a random walk on an undirected graph is proportional to degree [P].
- **Build:** power iteration for PageRank on a synthetic web graph with dangling-node handling, the convergence rate against α, personalised PageRank, and a comparison with the dense eigenvector computed by NumPy. [local]
- **Gap-fills:** *[inferred: Page et al. 1999; Langville–Meyer; Levin–Peres–Wilmer, recalled, not checked]* HITS (named).

**Assignment A11.10** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What is the stationary distribution of a random walk on a connected undirected graph?

(A) Uniform over vertices  
(B) Proportional to vertex degree  
(C) Proportional to the inverse degree  
(D) Concentrated on one vertex

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) An irreducible aperiodic finite chain has a unique stationary distribution  
(B) The PageRank matrix with damping alpha has second eigenvalue of modulus at most alpha  
(C) Power iteration converges geometrically at the rate of the second eigenvalue  
(D) PageRank needs the damping factor to be 1

**Q3 (2 marks, numerical answer (iterations)).** How many power iterations does PageRank with damping 0.85 need to reach error 10 to the minus 6, using ln eps over ln alpha?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that on a connected undirected graph with m edges the distribution proportional to degree is stationary for the simple random walk.

**Q5 (3 marks, programming).** Implement power iteration for PageRank with damping and dangling nodes on sparse matrices from scratch, compare eigenvalues with numpy, check the convergence rate against alpha and verify the degree-proportional stationary distribution on an undirected graph.

<details><summary>Key for A11.10 (open only after your attempt)</summary>

- **Q1:** B. The stationary probability of vertex i is its degree over twice the number of edges (the graph must be non-bipartite for convergence).
- **Q2:** A, B, C. Damping of 1 removes the guarantee of convergence.
- **Q3:** 85.01 iterations (tolerance ±1). ln 10 to the minus 6 is minus 13.8 and ln 0.85 is minus 0.1625, giving about 85.
- **Q4 (marking outline):** From vertex i the walk moves to a neighbour j with probability 1/d_i; take pi_i = d_i/(2m); then pi_i P_ij = (d_i/2m)(1/d_i) = 1/(2m) which equals pi_j P_ji; this detailed balance summed over i gives the sum of pi_i P_ij equal to pi_j, so pi is stationary.
- **Q5 (what a passing submission shows):** PageRank equal to the eigenvector oracle, an observed convergence rate near alpha, and the degree law confirmed.

</details>

### U11.11 Big data applications: graph processing
**Sources:** BDC W8; CCDS W8
- **Topics:** Introduction to Big Data Applications (Graph Processing) (Week 8) and the Spark applications of Week 8 of the cloud course: the Page Rank Algorithm on Spark with GraphX, the GraphX API and GraphX working (how GraphX executes graph operations as joins); the bulk-synchronous vertex-centric model of Pregel (supersteps, messages, vote to halt), programs for PageRank, connected components and single-source shortest paths, the property-graph representation as two tables and the join-based execution in GraphX, graph partitioning (edge-cut versus vertex-cut) and the effect of power-law degree distributions, triangle counting and community structure, and the limits of the vertex-centric model.
- **Results:** Single-source shortest paths in the vertex-centric model terminates in at most D + 1 supersteps for a graph of weighted diameter D in hops [D]; vertex-cut partitioning of a power-law graph replicates each high-degree vertex across machines, so the expected replication factor is far below the edge-cut communication on the same graph [D, by simulation]; PageRank reaches accuracy ε in about ln ε / ln α supersteps (from U11.10) [P].
- **Build:** a mini-Pregel BSP engine with PageRank, connected components and SSSP, checked against single-machine implementations; edge-cut versus vertex-cut partitioning experiments on a synthetic power-law graph with the replication factor and communication volume measured; the same algorithms written as join-based operations on your mini-Spark to mirror GraphX. [local]
- **Gap-fills:** *[inferred: Malewicz et al., Pregel, SIGMOD 2010; Gonzalez et al., PowerGraph, OSDI 2012 and GraphX, OSDI 2014, recalled, not checked]* graph neural networks as the successor family (named).

**Assignment A11.11** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** In a vertex-centric (Pregel) computation, what ends a run?

(A) All vertices have voted to halt and no messages are in flight  
(B) A fixed time  
(C) The first message  
(D) The first vertex

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Single-source shortest paths in Pregel needs at most about the hop diameter plus 1 supersteps  
(B) Vertex-cut partitioning replicates high-degree vertices across machines  
(C) Edge-cut communication on power-law graphs can be much larger than vertex-cut communication  
(D) Random hash partitioning keeps most edges within a machine

**Q3 (2 marks, numerical answer (fraction)).** A graph is hash-partitioned at random over 8 machines. What fraction of edges is cut in expectation (endpoints on different machines)?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that for random hash partitioning over p machines the expected fraction of cut edges is 1 minus 1/p.

**Q5 (3 marks, programming).** Implement a Pregel-style engine with supersteps, messages and combiners; run shortest paths, connected components and PageRank; compare edge-cut and vertex-cut partitioning on a power-law graph; and check results against NetworkX.

<details><summary>Key for A11.11 (open only after your attempt)</summary>

- **Q1:** A. Computation proceeds in supersteps until every vertex is inactive and there are no messages.
- **Q2:** A, B, C. Random hashing cuts most edges.
- **Q3:** 0.875 fraction (tolerance ±0.001). Both endpoints land together with probability 1/8, so the cut fraction is 7/8 = 0.875.
- **Q4 (marking outline):** The two endpoints of an edge are placed independently and uniformly; the probability that the second lands on the machine of the first is 1/p; so the edge is cut with probability 1 minus 1/p, and by linearity of expectation the expected cut fraction equals that value.
- **Q5 (what a passing submission shows):** Outputs equal to NetworkX, supersteps near the diameter for shortest paths, and a measured communication advantage for vertex cuts on skewed graphs.

</details>

## D12. Cloud operations and machine learning on Google Cloud: observability and reliability engineering, analytics services, managed machine learning and responsible AI

Aim: the last three weeks of the cloud-platform course, taught as the operational and analytical layer on top of everything built before. The published outline gives week titles only, and the course's labs are not listed in the source, so the product-level content here is *inferred* from the platform's documentation and is labelled as such; the concepts underneath (service-level objectives, columnar scans, dataflow windows, model drift, fairness) are taught with their own derivations and from-scratch builds, so that the product names are the replaceable part. Product names change (the monitoring and logging products were rebranded as the cloud operations suite in 2020, and the machine-learning products were consolidated under Vertex AI in 2021, in the author's reading; one unverified report of a further rebranding in 2026 was seen and should be checked on the live product pages before the labs). Benchmarks (recalled, not checked): Beyer et al., *Site Reliability Engineering* and *The Site Reliability Workbook*; Melnik et al., *Dremel*, VLDB 2010; Akidau et al., the Dataflow model; Barocas, Hardt and Narayanan, *Fairness and Machine Learning*; Mitchell et al., *Model Cards for Model Reporting*.

### U12.1 Observability and site reliability engineering: metrics, logs, traces, SLOs and error budgets
**Sources:** GCF W7
- **Topics:** Let Google keep an eye on things (the first half of Week 7): the three pillars of observability (metrics, logs, traces) and what each answers; metric types (gauge, counter, histogram, distribution), labels and cardinality, aggregation and percentiles; dashboards and alerting policies, notification channels, uptime checks; structured logging, log sinks and log-based metrics, the audit logs of U7.7; distributed tracing and the context propagated through requests, error reporting and profiling; the SRE vocabulary of U9.13 made operational: service-level indicators, objectives and error budgets, burn-rate alerting with multiple windows, toil and postmortems; chaos engineering as the controlled fault injection that resilience assessment (U8.5) calls for; on-call and incident command (U8.4).
- **Results:** The error budget of an SLO s over a window W is (1 − s)W, and with observed error rate e the burn rate is e/(1 − s) and the time to exhaust the budget is W divided by the burn rate [D]; a burn rate of 14.4 sustained for one hour consumes 2% of a 30-day budget, since 14.4/720 = 0.02 [check by script]; a multi-window rule (a long and a short window both above threshold) cuts the false-alert rate at a small cost in detection time [D]; percentiles of a mixture cannot be computed from percentiles of its parts, so histograms must be aggregated by bucket [P].
- **Build:** a time-series store with label matching, rate and histogram-quantile functions and a small query language; an alert evaluator implementing the multi-window burn-rate rule, replayed over a simulated incident to measure detection delay and false alerts; a structured-log parser with log-based metrics; a trace collector that assembles spans into a tree and finds the critical path. A monitoring workspace on the cloud platform can mirror it in a lab project at the free tier or with credit. [local; credit]
- **Gap-fills:** *[inferred: the cloud operations suite documentation; Beyer et al. 2016, recalled, not checked]* OpenTelemetry as the vendor-neutral standard (named only).

**Assignment A12.1** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** For an SLO of s over a window W, what is the error budget?

(A) (1 minus s) times W  
(B) s times W  
(C) W divided by s  
(D) 1 minus W

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) The burn rate is the observed error rate divided by (1 minus s)  
(B) A multi-window alert fires only when both a long and a short window exceed the threshold  
(C) Percentiles from separate histograms can be combined by adding bucket counts  
(D) The median of a union can be computed from the medians of its parts

**Q3 (2 marks, numerical answer (days)).** An SLO of 99.9 percent has an observed error rate of 0.5 percent. At that burn rate how many days does a 30-day budget last?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that two data sets can have the same part medians but different medians of their union, so medians cannot be combined.

**Q5 (3 marks, programming).** Write a metrics pipeline with counters, gauges and histograms, an SLO burn-rate alerter with multi-window rules tested on synthetic incidents, a tracing context propagator across simulated services, and a log parser with structured fields. Compute alert precision and detection delay.

<details><summary>Key for A12.1 (open only after your attempt)</summary>

- **Q1:** A. With a 99.9 percent SLO over 30 days the budget is 0.1 percent of the time.
- **Q2:** A, B, C. It cannot; counts or histograms must be kept.
- **Q3:** 6 days (tolerance ±0.01). The burn rate is 5, so the budget lasts 30/5 = 6 days.
- **Q4 (marking outline):** Part A is 1, 2, 3 with median 2 and part B is 10, 11, 12 with median 11, giving a union median of 6.5; part B prime is 4, 11, 12 with the same median 11 but a union with A of 1, 2, 3, 4, 11, 12 whose median is 3.5; so the part medians do not determine the union median.
- **Q5 (what a passing submission shows):** A histogram merge that equals the percentile of the pooled data, alerts firing on planted incidents with measured delay, and fewer false alarms with the multi-window rule.

</details>

### U12.2 Data analytics on Google Cloud: the warehouse, dataflow pipelines and managed clusters
**Sources:** GCF W7
- **Topics:** You have the data, but what are you doing with it? (the second half of Week 7): a serverless analytics warehouse and the architecture behind it (columnar storage, a tree of execution servers that aggregates partial results, separation of storage from compute, slots, and the two pricing styles: bytes scanned and reserved capacity), partitioned and clustered tables and how they cut scanned bytes, loading and streaming ingestion, SQL on nested data; the managed dataflow service and the programming model it runs (collections, transforms, windows, triggers and watermarks from U11.7), the managed Hadoop and Spark service (U11.3, U11.4), the managed messaging service (the counterpart of U11.6), and visualisation tools; ETL and ELT patterns, data quality and cost control (dry runs, partition pruning, avoiding SELECT star).
- **Results:** The bytes scanned by a columnar query equal the sum over referenced columns of rows × width after compression, independent of unreferenced columns, whereas a row store scans all columns [D]; partition pruning reduces scanned bytes to the fraction of partitions that match the filter [D]; a tree of fan-out f aggregates n leaf servers in depth ⌈log_f n⌉ [D].
- **Build:** a column store with dictionary and run-length encoding, column pruning, predicate push-down, partition pruning and a cost estimate of bytes scanned, checked against SQLite on the same queries; a Beam-style pipeline model with event-time windows and triggers over the stream of U11.7; a cost-control linter flagging unpartitioned scans and SELECT-star queries. A dry run on the cloud warehouse can serve as the oracle for scanned bytes when a lab project is used. [local; credit]
- **Gap-fills:** *[inferred: Melnik et al., Dremel, VLDB 2010; the warehouse documentation, recalled, not checked]* lakehouse table formats (named only).

**Assignment A12.2** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** Why does a columnar warehouse scan fewer bytes than a row store for a query touching few columns?

(A) It reads only the referenced columns  
(B) It uses more memory  
(C) It sorts the data  
(D) It encrypts the data

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Partition pruning reduces the bytes scanned by skipping non-matching partitions  
(B) A serving tree of fan-out f aggregates n leaves in about log base f of n levels  
(C) Bytes scanned for a columnar query depend on the referenced columns  
(D) A SELECT star query is as cheap as selecting one column in a columnar store

**Q3 (2 marks, numerical answer (GB)).** A table has 1 billion rows. A query references three columns of widths 8, 8 and 4 bytes. How many gigabytes does a columnar scan read, ignoring compression?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that for a table with C equal-width columns and a query that references c of them, a columnar scan reads the fraction c/C of the bytes a row-store scan reads, and that partition pruning multiplies this by the fraction of partitions matched.

**Q5 (3 marks, programming).** Implement a columnar file with dictionary and run-length encoding, a scan with predicate and partition pruning measured in bytes, a tree-shaped aggregation in DSim, and a small streaming pipeline with windows and watermarks; compare the query on the managed warehouse in a free-tier or sandbox project only if you choose to use credit.

<details><summary>Key for A12.2 (open only after your attempt)</summary>

- **Q1:** A. Columns are stored separately, so unreferenced columns are not read.
- **Q2:** A, B, C. Selecting all columns scans all of them.
- **Q3:** 20 GB (tolerance ±0.1). 1e9 rows times 20 bytes is 20 GB.
- **Q4 (marking outline):** A row store reads every column of every row, so R C w bytes for R rows and width w; a column store reads R c w bytes; the ratio is c/C; pruning removes the partitions that do not match the filter, leaving the matched fraction of the rows to read.
- **Q5 (what a passing submission shows):** Bytes scanned matching the formula, correct query results against SQLite, and a tree depth of about log base f of n. Any cloud steps are optional and tagged credit.

</details>

### U12.3 Machine learning on Google Cloud: managed training and prediction, pre-trained APIs and responsible AI
**Sources:** GCF W8
- **Topics:** Let machines do the work (Week 8): the managed machine-learning platform as a whole (datasets, training jobs on CPUs, GPUs and TPUs, hyperparameter tuning, a model registry, online and batch prediction endpoints, pipelines and monitoring), automated machine learning as a search over models and features, machine learning inside the warehouse by SQL, the pre-trained application programming interfaces (vision, language, speech, translation) and when to use one rather than train a model; the MLOps loop (reproducible training, deployment, drift detection and retraining); responsible AI: fairness metrics (demographic parity, equalised odds, calibration), explainability by feature attribution, model cards and data documentation, privacy in training (U8.8) and the cost and carbon footprint of training.
- **Results:** The population stability index of a feature is Σ (a_i − e_i) ln(a_i/e_i) over bins and a value above about 0.25 is conventionally treated as a major shift [Def, threshold recalled, not checked]; except in degenerate cases a classifier cannot be both calibrated and have equal false-positive and false-negative rates across groups with different base rates [X, Kleinberg et al. and Chouldechova, stated]; for a linear model the contribution of feature j to a prediction relative to a baseline is w_j(x_j − x̄_j) and these contributions sum to the prediction difference [D].
- **Build:** a small multilayer perceptron trained from scratch in NumPy on synthetic data; a drift monitor using the population stability index and a Kolmogorov–Smirnov test on a shifted stream; fairness metrics and a threshold-adjustment experiment on a synthetic population with a measured accuracy cost; a model-card generator; an inference server on loopback with a measured latency percentile checked against an SLO from U12.1. Managed training and an endpoint are described as a plan and run only in a lab project at the free tier or with credit. [local; plan only; credit if applied]
- **Gap-fills:** *[inferred: the platform's machine-learning documentation; Mitchell et al. 2019; Barocas et al., recalled, not checked]* generative-model services and their evaluation (the earlier unified curriculum treats the models; this unit names only the service layer).

**Assignment A12.3** (10 marks; pass at 7/10 with Q4 and Q5 accepted)

**Q1 (1 mark, multiple choice).** What does the population stability index measure?

(A) The drift between the expected and actual distributions of a feature  
(B) The accuracy of a model  
(C) The size of a data set  
(D) The latency of a service

**Q2 (2 marks, multiple select; all correct options and no wrong option).** Which statements are correct?

(A) Except in degenerate cases a classifier cannot be calibrated and have equal error rates across groups with different base rates  
(B) For a linear model the per-feature contributions relative to a baseline sum to the prediction difference  
(C) A high overall accuracy proves the model is fair  
(D) A model card documents intended use and evaluation results

**Q3 (2 marks, numerical answer).** Expected bin shares are 0.5, 0.3, 0.2 and actual shares are 0.3, 0.4, 0.3. What is the population stability index (three decimals)?

**Q4 (2 marks, prove or derive; every step with its reason).** Show that for a linear model f(x) equal to w dot x plus b the contributions w_j (x_j minus baseline_j) sum exactly to f(x) minus f(baseline).

**Q5 (3 marks, programming).** Train a classifier on synthetic data from scratch, compute calibration curves, error rates by group, a drift monitor with PSI and a linear explanation report, and write a model card from a template. Compare with a managed AutoML or prediction service only through its free tier or documentation, tagged credit or learning only.

<details><summary>Key for A12.3 (open only after your attempt)</summary>

- **Q1:** A. It sums (a minus e) ln(a/e) over bins.
- **Q2:** A, B, D. Overall accuracy can hide large group differences.
- **Q3:** 0.1715 (tolerance ±0.001). The terms are 0.102, 0.029 and 0.041, giving about 0.172.
- **Q4 (marking outline):** Subtract f(baseline) from f(x): the intercept cancels and what remains is the sum over j of w_j x_j minus the sum over j of w_j baseline_j, which is the sum of w_j times (x_j minus baseline_j).
- **Q5 (what a passing submission shows):** Calibration and group error tables that reveal a planted disparity, a drift alert on shifted data, explanations that sum correctly, and a complete model card.

</details>


# PART E. CAPSTONES

## D13. Capstones

Aim: six integrating projects, each one drawing on units from several domains, each built from your own components first and then checked against standard tools. A capstone has no weekly assignment; it is accepted against the listed criteria, with the Master Rules' tutor stance applied (the tutor does not write graded work). Each is local first, labelled with its cost, and, wherever it touches security, confined to the laboratory rules of U6.1.

### U13.1 Capstone: a user-space TCP/IP stack over a lossy virtual link
**Sources:** none (capstone; assembles earlier units)
- **Topics:** Scope: Ethernet framing, ARP, IPv4 with checksum and optional fragmentation, ICMP echo, UDP, a DNS stub, and TCP with the three-way handshake, cumulative acknowledgments, a sliding window, retransmission with the RFC 6298 timer, fast retransmit, Reno-style congestion control, and a socket-like API; the virtual link in DSim has configurable delay, loss, reordering, duplication and bandwidth. Draws on U2.2 to U2.14, U3.3 to U3.5 and U9.1.
- **Results:** The measured throughput on a lossy link is consistent with the Mathis estimate MSS/(RTT·√(2p/3))·C up to a constant [D, to be shown by experiment]; the stack passes a conformance suite of at least thirty scripted scenarios, including simultaneous open and close, window probes, and recovery from a lost final ACK [Def].
- **Build:** the stack, the scenario suite, a throughput-versus-loss experiment with a plot, a packet-capture writer producing a file readable by Wireshark, and a ten-line report on where the stack departs from the RFCs. [local]
- **Gap-fills:** *[inferred: Stevens, TCP/IP Illustrated; RFC 9293, recalled, not checked]* acceptance: your stack interoperates with the operating system's TCP through a loopback tunnel in the lab only.

### U13.2 Capstone: a secure channel from your own primitives (never deployed)
**Sources:** none (capstone; assembles earlier units)
- **Topics:** Scope: an authenticated key exchange (ephemeral ECDH from U5.15, signatures from U5.17, HKDF from U5.18) followed by an AEAD record layer (U5.7 and U5.11) with sequence numbers, replay protection, key rotation and a downgrade-resistant version field, running over your stack of U13.1 or over loopback sockets. Draws on D5 and D2.
- **Results:** The channel resists a scripted adversary that tampers, replays, reorders, truncates and downgrades, and the negative test suite shows each rejection [Def]; a written threat model states what the channel does not protect (metadata, traffic analysis, side channels) [Def].
- **Build:** the implementation, the negative test suite, a comparison of handshake cost and record overhead with TLS 1.3 from the `ssl` module on loopback, and the explicit statement that the code is for learning and is never deployed (Master Rules 6.8 and 11.1). [local; learning only]
- **Gap-fills:** *[inferred: Noise Protocol Framework; RFC 8446, recalled, not checked]* acceptance includes one real flaw you introduce on purpose and then find with your own tests.

### U13.3 Capstone: a replicated, sharded key-value store with fault injection
**Sources:** none (capstone; assembles earlier units)
- **Topics:** Scope: shards by consistent hashing (U9.5), each shard a Raft group (U9.14), a router, optional multi-shard transactions by two-phase commit (U9.18), a Jepsen-style nemesis (partitions, crashes, clock skew, message loss) in DSim, a linearizability checker (U9.16), and metrics with an SLO (U12.1). Draws on D9, D10 and D12.
- **Results:** No linearizability violation appears over at least 10,000 randomised schedules with the nemesis active; availability under a minority partition is measured and reported against the theory [Def]; a deliberately broken variant (for example a stale-read optimisation) is caught by the checker [Def].
- **Build:** the store, the nemesis, the checker run, a latency and availability report, and a design note on what would change for geo-distribution. [local]
- **Gap-fills:** *[inferred: Kingsbury's Jepsen reports; Ongaro's thesis, recalled, not checked]* acceptance: the report states the exact seeds so any failure replays.

### U13.4 Capstone: an end-to-end data platform from your own engines
**Sources:** none (capstone; assembles earlier units)
- **Topics:** Scope: ingestion into your Kafka-like log (U11.6), a stream job with event-time windows and sketches (U11.7), a batch job on your mini-MapReduce or mini-Spark (U11.3, U11.4) computing aggregates and PageRank (U11.11) from the same log, a serving store (U10.4 or U10.5), lineage, data-quality checks, and a cost model. Draws on D10 and D11.
- **Results:** The end-to-end effect is exactly-once across a crash of any single component, shown by an invariant such as the conservation of a sum; skew in the key distribution is detected and mitigated; the streaming and batch answers agree after late data is accounted for [Def].
- **Build:** the pipeline, the crash and skew experiments, the reconciliation report, and a comparison of one stage with its cloud counterpart (U12.2) by cost and latency. [local]
- **Gap-fills:** *[inferred: Kleppmann Ch.10–12; the kappa architecture, recalled, not checked]* acceptance: a single command reproduces the run from a seed.

### U13.5 Capstone: a small service on Google Cloud with identity, networking, reliability and cost controls
**Sources:** none (capstone; assembles earlier units)
- **Topics:** Scope: a reference architecture for a small web service: a virtual network with subnets and firewall rules (U4.8), least-privilege identities (U7.7), an HTTP load balancer, managed compute (U4.7), object storage and a database (U10.7), monitoring with SLOs and burn-rate alerts (U12.1), a budget alert, labels, and a verified teardown; infrastructure described as code and checked by a policy linter built from U7.5 and U8.6. Draws on D4, D7, D10 and D12.
- **Results:** The plan passes your policy linter (no public storage, no wildcard roles, no unrestricted ingress except the load balancer's port) and your cost estimate from the live price list stays below the lab budget; the SLO and its alerts are validated against a simulated load [Def].
- **Build:** the design document, the infrastructure code, the linter report, the cost estimate, and, only if the budget allows and a personal lab project is used (never a work account), an applied deployment with a screenshot-free teardown log showing the project returned to zero resources. [plan only; credit if applied]
- **Gap-fills:** *[inferred: the platform's architecture framework, recalled, not checked]* acceptance: the same-day teardown rule of the course profile is met.

### U13.6 Capstone: a security programme for a synthetic organisation
**Sources:** none (capstone; assembles earlier units)
- **Topics:** Scope: for a fictional company you define, produce: a quantitative risk register with Monte Carlo loss exceedance (U8.2 and U8.3), an ATT&CK coverage map and a D3FEND control selection (U7.2, U7.4), a kill-chain analysis of two scenarios (U7.3), a STIX bundle of synthetic indicators shared over your TAXII server (U7.6), a STIG-style baseline and compliance report (U7.5), policies with a conflict check (U8.6), an incident-response plan and business-continuity plan with recovery objectives (U8.4), a resilience simulation (U8.5), a privacy section with a data map, a GDPR and DPDP obligation map and a differentially private release of one statistic (U8.8 and U8.9), a cryptographic inventory and a post-quantum migration plan (U5.25), and a one-page board summary. Draws on D5 to D8.
- **Results:** The programme's numbers trace to code (every figure in the board summary is produced by a script from the register); the control portfolio is justified by the knapsack optimiser of U8.3; every external statement (a law, a standard, a framework version) carries its source and the date it was checked [Def].
- **Build:** the artefacts above, a reproducible build script, and a short critique of the programme's weakest assumption. All data is synthetic and no real organisation or person is analysed. [local]
- **Gap-fills:** *[inferred: NIST CSF 2.0 profiles; ISO/IEC 27001 Annex A, recalled, not checked]* acceptance: the board summary is readable by a non-specialist in five minutes.


---

# APPENDICES

## Appendix A. Source course index

| Key | Course | Instructor / institution (course id) | Source lines in `cloud-computing.txt` | Cells |
|---|---|---|---|---|
| GCF | Google Cloud Computing Foundations | Soumya Kanti Ghosh, IIT Kharagpur (NPTEL 106105223); file header says IIT Guwahati | 8–24 | 10 |
| CN | Computer Networks and Internet Protocol | Soumya Kanti Ghosh and Sandip Chakraborty, IIT Kharagpur (NPTEL 106105183) | 69–90 | 13 |
| ACN | Advanced Computer Networks | Neminath Hubballi, IIT Indore and Sameer G. Kulkarni, IIT Gandhinagar | 105–123 | 13 |
| PCS | Practical Cyber Security for Cyber Security Practitioners | Sandeep K. Shukla, IIT Kanpur | 135–159 | 13 |
| CSP | Cyber Security and Privacy | Saji K. Mathew, IIT Madras (NPTEL 106106248) | 178–207 | 13 |
| EH | Ethical Hacking | Indranil Sengupta, IIT Kharagpur (NPTEL 106105217) | 251–274 | 13 |
| CNS | Cryptography and Network Security | Sourav Mukhopadhyay, IIT Kharagpur | 290–317 | 13 |
| TPMC | Theory and Practice of Modern Cryptography | Sourav Mukhopadhyay, IIT Kharagpur (NPTEL 106105002) | 336–359 | 13 |
| FOC | Foundations of Cryptography | Ashish Choudhury, IIIT Bangalore | 377–408 | 13 |
| ADS | Advanced Distributed Systems | Smruti Ranjan Sarangi, IIT Delhi (NPTEL 106102237) | 428–451 | 13 |
| CCDS | Cloud Computing and Distributed Systems | Rajiv Misra, IIT Patna | 468–541 | 9 |
| DS | Distributed Systems | Rajiv Misra, IIT Patna (NPTEL 106106168) | 560–579 | 9 |
| BDC | Big Data Computing | Rajiv Misra, IIT Patna (NPTEL 106104189) | 598–616 | 9 |

## Appendix B. Coverage matrix: every source cell and the units that teach it

Each entry is `cell → units`. A cell may feed several units because one source week often spans several topics (for example, the CCDS and DS weeks on consensus feed the agreement, replication and coordination units).

**GCF** (Google Cloud Computing Foundations): o → U1.1, U1.3; W0 → U1.1; W1 → U1.1, U1.3; W2 → U4.7; W3 → U10.7; W4 → U7.7; W5 → U4.8; W6 → U4.8; W7 → U12.1, U12.2; W8 → U12.3

**CN** (Computer Networks and Internet Protocol): o → U2.2; W1 → U2.2; W2 → U2.3; W3 → U2.4; W4 → U2.5; W5 → U2.5, U2.6; W6 → U2.6; W7 → U2.8; W8 → U2.9; W9 → U2.10; W10 → U2.12; W11 → U2.13; W12 → U2.14

**ACN** (Advanced Computer Networks): o → U3.3; W1 → U3.3, U3.4; W2 → U3.4; W3 → U3.5; W4 → U3.6; W5 → U3.7; W6 → U3.7; W7 → U3.8; W8 → U3.9; W9 → U3.10; W10 → U3.10, U4.4; W11 → U3.11; W12 → U3.12

**PCS** (Practical Cyber Security for Cyber Security Practitioners): o → U8.1; W1 → U8.1; W2 → U7.2; W3 → U7.2; W4 → U7.3; W5 → U7.4; W6 → U7.5; W7 → U7.6; W8 → U8.3; W9 → U8.5; W10 → U8.6; W11 → U8.6; W12 → U8.4

**CSP** (Cyber Security and Privacy): o → U8.1; W1 → U6.1; W2 → U6.1; W3 → U8.1; W4 → U8.4; W5 → U8.6; W6 → U8.3; W7 → U7.1; W8 → U5.18, U7.1; W9 → U8.7; W10 → U8.8, U8.9; W11 → U8.9; W12 → U8.10

**EH** (Ethical Hacking): o → U6.1; W1 → U2.3, U6.1; W2 → U2.5, U2.8, U2.9; W3 → U2.8, U2.9; W4 → U6.2; W5 → U6.3, U6.4; W6 → U5.3; W7 → U5.10, U5.17, U5.18; W8 → U6.5, U6.6; W9 → U6.5, U6.6, U6.7; W10 → U5.20, U6.9; W11 → U6.7, U6.8; W12 → U6.10

**CNS** (Cryptography and Network Security): o → U5.3, U5.22, U5.25; W1 → U5.3, U5.4; W2 → U5.4, U5.6; W3 → U5.2, U5.5, U5.6; W4 → U5.2, U5.12; W5 → U5.7, U5.13, U5.14; W6 → U5.12, U5.14, U5.15; W7 → U5.14; W8 → U5.10, U5.11, U5.17, U5.18; W9 → U5.10, U5.17; W10 → U5.19; W11 → U5.6, U5.20, U5.21, U5.22; W12 → U5.18, U5.20, U5.25, U9.21

**TPMC** (Theory and Practice of Modern Cryptography): o → U5.3, U5.22, U5.25; W1 → U5.3; W2 → U5.3, U5.9; W3 → U5.4, U5.7; W4 → U5.4, U5.6, U5.7; W5 → U5.5; W6 → U5.14, U5.16; W7 → U5.12, U5.13, U5.14, U5.18; W8 → U5.10, U5.11, U5.15, U5.17; W9 → U5.10, U5.17; W10 → U5.19, U5.20; W11 → U5.21, U5.22; W12 → U5.13, U5.18, U5.20, U5.22, U5.23, U5.24, U5.25

**FOC** (Foundations of Cryptography): o → U5.3; W1 → U5.3; W2 → U5.9; W3 → U5.6, U5.9; W4 → U5.4, U5.9; W5 → U5.4, U5.7, U5.11; W6 → U5.10, U5.11; W7 → U5.10, U5.11; W8 → U5.11, U5.13; W9 → U5.13, U5.15, U5.16; W10 → U5.14, U5.16; W11 → U5.16, U5.17, U5.24; W12 → U5.12, U5.17, U5.18, U5.21, U5.22, U5.24

**ADS** (Advanced Distributed Systems): o → U9.1; W1 → U9.3; W2 → U9.4; W3 → U9.4, U9.5; W4 → U9.6, U9.8; W5 → U9.10; W6 → U9.11, U9.12; W7 → U9.16; W8 → U9.14; W9 → U9.13, U9.20; W10 → U9.21; W11 → U9.18, U10.3, U10.4; W12 → U10.3, U11.5

**CCDS** (Cloud Computing and Distributed Systems): o → U1.1; W1 → U1.1, U4.2, U4.3; W2 → U4.4, U4.6; W3 → U9.10, U9.15; W4 → U9.6, U9.7, U9.8, U9.15; W5 → U9.12, U9.13, U9.14, U9.19; W6 → U9.16, U10.4, U10.5; W7 → U9.4, U9.5; W8 → U11.3, U11.4, U11.6, U11.11

**DS** (Distributed Systems): o → U9.1; W1 → U9.1, U9.6, U9.10; W2 → U9.6, U9.7, U9.8; W3 → U9.8, U9.12, U9.19; W4 → U9.9, U9.11; W5 → U9.7, U9.19, U9.20; W6 → U9.2, U9.4, U9.5; W7 → U10.2, U11.3, U11.4; W8 → U9.22

**BDC** (Big Data Computing): o → U11.1; W1 → U11.1; W2 → U11.2; W3 → U11.3, U11.4; W4 → U10.2, U10.5, U10.6; W5 → U11.6, U11.7; W6 → U11.9; W7 → U11.9; W8 → U11.11

Total: 154 cells, every one cited.

## Appendix C. Prerequisite bridges and the prerequisites the sources state

### C.1 Bridge units (each is taught immediately before the first unit that needs it)

| Bridge | Concept taught | Needed by |
|---|---|---|
| U1.2 | Linux shell, scripting, Python for systems work, regular expressions and Git | every lab from U1.3 on, the byte-level work of U2.3, and the shell and language prerequisites listed for the Google Cloud course (shell scripting, one programming language, SQL; SQL itself is bridged in U10.1) |
| U2.1 | probability, random processes and queueing for networks | U2.2 (statistical multiplexing, delay), U2.13 (ALOHA), U3.3 (head-of-line blocking), U3.6 (scheduling), U4.7 (autoscaling), U12.1 (SLO arithmetic) |
| U2.7 | graph algorithms for routing — shortest paths, spanning trees and distributed relaxation | U2.9 (routing protocols), U2.12 (spanning tree protocol), U3.7 (controller path computation), U4.6 (traffic engineering), U9.11 (distributed minimum spanning tree) |
| U2.11 | coding theory — GF(2), polynomial division, CRC and Hamming codes | U2.12 (error control); reused in U5.5 (GF(2⁸)) and U5.6 (LFSR as polynomial division) |
| U3.1 | lookup data structures — tries, hashing and Bloom filters | U3.4 (IP lookup), U3.5 (classification), U3.11–U3.12 (NDN tables); reused in U10.4 (Cassandra) and U10.5 (HBase) |
| U3.2 | bipartite matching, Hall's theorem and Birkhoff–von Neumann decomposition | U3.3 (switch scheduling) and U3.10 (Clos networks) |
| U4.1 | operating systems and computer architecture for virtualization | U4.2 (virtualization), U4.4 (containers), U9.x (process and thread models) |
| U4.5 | network flows and linear programming | U4.6 (B4 and SWAN allocation), U3.6 (max–min fairness), U11.9 (optimisation in ML) |
| U5.1 | probability, entropy and asymptotics for cryptography | U5.3 (perfect secrecy, entropy of language), U5.9 (advantage and distinguishers), U5.10 (birthday bound), U5.12 onward (error probabilities) |
| U5.8 | computational complexity, one-way functions and the reduction method | U5.9 onward (every proof of security is a reduction). Addresses the stated prerequisite of the provable-security course: exposure to discrete mathematics, algorithms and theory of computation |
| U5.12 | number theory for public-key cryptography — Fermat, Euler, CRT, quadratic residues, Legendre and Jacobi symbols, primality testing and factoring | U5.13 (discrete log and DDH), U5.14 (RSA, Rabin, ElGamal), U5.15 (curve point counting), U5.17 onward. Continues U5.2 (Euclid and inverses) and U5.5 (groups) |
| U8.2 | quantitative risk — frequency and severity models, Monte Carlo loss exceedance, Bayesian updating and decision under uncertainty | U8.3 (risk management), U8.5 (resilience assessment), U13.6 (security programme capstone). Builds on U5.1 |
| U9.17 | transactions — ACID, serializability, locking, logging and recovery | U9.18 (atomic commit, Percolator, Spanner), U10.5 (Bigtable), U10.7 (managed databases). Builds on U10.1's relational view if read in order, and is self-contained otherwise |
| U10.1 | the relational model, SQL, indexing and query processing | U10.4 onward (every store here is defined by what it gives up relative to a relational database), U12.2 (BigQuery). Addresses the SQL prerequisite stated in the cloud-platform source and the database prerequisite stated in the big-data source |
| U11.8 | machine-learning foundations for scalable learning | U11.9 (machine learning on the engines), U12.3 (machine learning on the cloud platform). A compact version of the foundations; the full treatment is in the earlier unified machine-learning curriculum |
| U11.10 | Markov chains, eigenvectors and PageRank | U11.11 (graph processing). Builds on the random-walk material of U9.2 |

16 bridge units in all. Several other units (U5.2 modular arithmetic, U5.5 algebra, U9.1 models and the simulator, U9.2 tail bounds) also begin from first principles and carry source citations as well.

### C.2 What the sources state as prerequisites, and where each is handled

| Course | Prerequisite line(s) in the source | Handled in |
|---|---|---|
| GCF | Those enrolling for the course should ideally: ● Have basic IT knowledge and be interested in learning more about Cloud and ML. ● Have competency in at least one language (such as Python, Java). ● Be familiar with the basics of shell scripting, SQL. | Basic IT assumed. One programming language: Python, with U1.2 as the toolbox. Shell scripting: U1.2. SQL: U10.1. |
| ACN | PRE-REQUISITES : Computer Networks and Computer Architecture Courses are Prerequisites (undergraduate level course) Computer Networks and Internet Protocol - https://nptel.ac.in/courses/106105183 | Computer networks: D2 from first principles. Computer architecture: U4.1. |
| PCS | PRE-REQUISITES : A previous course on fundamentals of Cyber Security is desirable, if not, courses in Operating System, Networking, Software Engineering, and Programming will be desirable | Cyber-security fundamentals: D6 and D7 start from the basics. Operating systems and architecture: U4.1. Networking: D2. Programming: U1.2. |
| CSP | Prerequisites A core course on Management Information Systems desirable (not mandatory) | Management information systems is desirable, not required: U8.1 to U8.10 introduce what is needed. |
| EH | Prerequisites Basic concepts in programming and networking | Programming: U1.2. Networking: D2. |
| TPMC | Prerequisites Higher Secondary Mathematics knowledge | Higher-secondary mathematics: U5.1, U5.2 and U5.5 start there; number theory is built in U5.12. |
| FOC | PRE-REQUISITES : There are no pre-requisites for this course. However it is expected that the students who are interested to take this course have had some exposure to a basic course on discrete mathematics, algorithms, or theory of computation. Having said that, I ensure that a significant effort w | Discrete mathematics, algorithms and theory of computation: probability and entropy U5.1, complexity and reductions U5.8, number theory U5.12. |
| ADS | Data structures (2nd year level), Operating SystemsINTENDED AUDIENCE: UG and PG students (Computer Science and Electrical Engineering) | Data structures at second-year level is assumed and reinforced by the bridges U3.1 (lookup structures) and U2.7 (graph algorithms). Operating systems: U4.1. |
| CCDS | PREREQUISITES : Minimum: Data Structures and Algorithms Ideal: Computer Architecture, Basic OS and Networking concepts Programming, Data Structures and Algorithms - https://nptel.ac.in/courses/106106127 Demystifying networking - https://nptel.ac.in/courses/106101209 Computer Architecture - https://n | Data structures and algorithms assumed as above. Computer architecture, OS, networking: U4.1 and D2. Programming: Python (U1.2). |
| DS | Prerequisites Minimum: Data Structures and AlgorithmsIdeal: Basic networking concepts, Basic OS concepts (e.g., processes, threads, synchronization, file systems, scheduling etc.), Advanced Programming (Good knowledge in C and C++). | Data structures and algorithms assumed as above. Networking: D2. OS concepts (processes, threads, synchronisation, file systems, scheduling): U4.1. The source asks for good C and C++; this curriculum uses Python throughout, so that requirement is replaced, not met (inferred; say if you want C ports). |
| BDC | PREREQUISITES : Data Structure & Algorithms, Computer Architecture, Operating System, Database Management Systems | Data structures and algorithms assumed as above. Architecture and OS: U4.1. Database management systems: U10.1. |

## Appendix D. Gap-fills, candidates not added, and decisions needed

### D.1 What was added beyond the outlines (and why)

- **Prerequisite bridges** (Appendix C.1): required by the instruction to wire prerequisites in just before the concept that demands them.
- **U4.8** (cloud networking on Google Cloud): the thin GCF weeks 5 and 6 name networking products; the concepts underneath are derived from scratch so the product names are replaceable.
- **GCF weeks with title-only outlines** are treated as *inferred*: the concepts under each product name are taught from first principles and the product lens sits next to the concept it implements (compute D4, networking U4.8, identity U7.7, storage U10.7, operations and analytics D12).
- **Capstones** (D13) assemble the earlier units and are not sourced.

### D.2 Gap candidates (not added; need your agreement per Master Rules 7.4)

These are adjacent subjects that no outline names, or that a unit mentions only in passing. They are **not** in the structure above until you agree.

| Candidate | Why it is adjacent | Would sit in |
|---|---|---|
| Infrastructure as code and CI/CD pipelines | Standard practice for the Google Cloud labs; not in any outline | D12 |
| Serverless platforms in depth (functions, managed containers) and event-driven design | Mentioned only in passing in the compute and operations units | D4 or D12 |
| Service meshes and Kubernetes internals beyond the orchestration loop | U4.4 and U11.2 teach the control loop; the rest is operations practice | D4 |
| Formal specification and model checking of protocols (for example TLA+) | Natural companion to D9; mentioned only in passing | D9 |
| Accelerator computing (GPUs and TPUs) for ML on the cloud | Adjacent to U12.3; no outline covers hardware | D12 |
| Full machine-learning course | U11.8 is a compact bridge; the full treatment is in the earlier unified curriculum | link to the earlier file |

### D.3 Decisions I need from you

1. **Labs list.** The GCF outline says the course has 26 labs on Qwiklabs but does not list them. The Build lines give a lab for each concept instead. If you can supply the list, I will map each lab to a unit.
2. **Gap candidates** in D.2: add any, none or all.
3. **Merging with the earlier file.** `unified_curriculum.md` (mathematics, machine learning, deep learning, LLMs) and this file share a method. Merge into one document, or keep two linked by U11.8, U9.2 and U5.1?
4. **Institution of the GCF course.** The file's header says IIT Guwahati while the course block names IIT Kharagpur (Appendix E). Which should the record carry?
5. **Lab environment.** The security units assume an isolated host-only VM network you own. Tell me your setup (laptop OS, VM tool) and I will adjust the Build lines and cost tags.
6. **C and C++ for DS.** The source asks for C or C++; the curriculum uses Python. Say if you want selected builds ported.
7. **Tooling choices.** The from-scratch guideline leaves tools to the unit; each Build line names its choice. Tell me if any should change.

## Appendix E. Source anomalies, typos and residual flagged atoms

### E.1 Anomalies in the sources (kept visible, not silently fixed)

| Source | Issue | Handling |
|---|---|---|
| GCF | The file header attributes the course to IIT Guwahati; the course block names IIT Kharagpur. Lines 1–28 are repeated verbatim at lines 30–57 | Cited once; nothing double-counted. See D.3 item 4. |
| GCF | 26 Qwiklabs labs are mentioned but not listed; several weeks give only a title | Thin weeks are marked *inferred* in the units that cite them (for example U1.3 and U4.7). |
| CCDS | Eight weeks in the source (the outline cells W1–W8) | Taken as given. |
| CNS, TPMC, FOC | Overlap heavily on number theory, public-key schemes and provable security | Merged in D5; every week cited. |
| Typos taken from context | 'Christians algorithm', 'Berkley's', 'El Gamal', 'DEF3ND', 'Incidence response', 'Primarily Testing', 'Rabinson', 'physical inclinable functions', 'WTC' | The unit text quotes the source spelling in parentheses where the check needs it and uses the standard name otherwise. |
| ADS (U9.13) | 'TLAs' appears without an expansion | Left unexpanded in U9.13 rather than guessed. |
| CSP | Weeks carry reading-list entries: labels R3 to R21, URLs, years and 'accessible at' | Case titles and readings are treated as cases (the Target breach in U6.1, active defense in U7.1, the HBR case on Cheddar in U8.3); the labels and URLs are not content. |

### E.2 Atoms the word-level check still flags, reviewed by hand

- **Outline-prose atoms flagged:** 114. They are audience statements, marketing sentences and connective phrases (for example 'to practice the learning'); every topic named in an outline appears in the units that cite it, with the outline map sentences in U1.1, U2.2, U3.3, U5.3, U6.1, U8.1, U9.1 and U11.1 where an outline names many topics.
- **Non-outline atoms flagged:** 35. All were reviewed one by one: URLs and URL fragments, years, reading labels (R11 to R21), the phrase 'accessible at', one section label ('Examples'), and the titles of cases or articles that are covered under their topic.

<details><summary>Full list of non-outline flagged atoms</summary>

- `CSP:W8` R11
- `CSP:W8` https
- `CSP:W1` https
- `CSP:W1` //www.sciencedirect.com/science/article/pii/S0167404813000801
- `CSP:W2` Chapter 1- Text R3
- `CSP:W2` https
- `CSP:W7` Exploits R10
- `CSP:W6` accessible at
- `CSP:W6` https
- `CSP:W5` https
- `CSP:W5` //hbr.org/2018/05/internet-insecurity
- `CSP:W9` R13
- `CSP:W9` https
- `CSP:W9` //plato.stanford.edu/entries/privacy/ R14
- `CSP:W9` //hbr.org/2007/06/we-googled-you-2
- `CSP:W10` R15
- `CSP:W10` accessible at
- `CSP:W10` https
- `CSP:W11` R17
- `CSP:W11` https
- `CSP:W11` //gdpr-info.eu
- `CSP:W11` R18
- `CSP:W11` accessible at
- `CSP:W11` 2023 https
- `CSP:W12` R20
- `CSP:W12` accessible at
- `CSP:W12` https
- `CSP:W8` //hbr.org/2018/05/active-defense-and-hacking-back-a-primer?ab=seriesnav-bigidea
- `CSP:W2` Why you should care about the Target data breach? Business Horizons
- `CSP:W2` //www.sciencedirect.com/science/article/abs/pii/S0007681316000033
- `CSP:W6` //hbr.org/2018/05/case-study-protecting-the-cheddar
- `CSP:W11` //www.jstor.org/stable/pdf/26697657.pdf R19
- `CSP:W11` //www.meity.gov.in/writereaddata/files/Digital%20Personal%20Data%20Protection%20Protection%202023.pdf
- `CSP:W12` //www.pomsmeetings.org/ConfPapers/052/052-0002.pdf R21
- `CSP:W12` //hbswk.hbs.edu/item/cold-call-apples-dilemma-balancing-privacy-and-safety-responsibilities

</details>

## Appendix F. Verification register and safety notes

**Checked on the web during this work** (the unit that uses each says so):

| Fact | Source type | Where used |
|---|---|---|
| NIST published FIPS 203 (ML-KEM), FIPS 204 (ML-DSA) and FIPS 205 (SLH-DSA) on 13 August 2024; HQC was selected on 11 March 2025; FIPS 206 (FN-DSA) was still in development | NIST pages | U5.25 |
| OWASP Top 10:2025 | Secondary reports, not the OWASP page itself | U6.2, U6.7 |
| Digital Personal Data Protection Rules 2025 notified 13 November 2025 with phased commencement | Law-firm summaries, not the official gazette text | U8.9 |
| Qwiklabs history: acquired by Google in November 2016, became Google Cloud Skills Boost in October 2021, now part of Google Skills (announced October 2025) | Press and Google pages | U1.3 |
| Product renames (operations suite, Vertex AI, end of AI Platform access on 31 January 2025) | Google pages | U1.3 |

**Everything else** that is a recalled reference, a benchmark title or a standard result is marked *recalled, not checked* where it appears. Prices in U10.7 are illustrative numbers for an exercise, not current Google Cloud prices. Product names and limits change often: verify them in the console or the documentation before relying on them.

**Safety notes.** Nothing in this document asks you to scan, probe, attack or access a system you do not own. The ethical-hacking and security units use an isolated host-only lab, standard tools and Python models of the mechanisms; no exploit or malware is authored. Cryptographic code built here is for learning and is never deployed. No assignment asks for credentials, keys or personal data; use synthetic data throughout.
