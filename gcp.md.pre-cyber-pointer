The Consolidated Cloud Mastery Curriculum
Fundamentals → GCP + AWS + Azure Professional/Expert Certifications → DevOps/Docker/K8s/NGINX/CI-CD
Built September 16, 2026. This is our shared syllabus — I'll teach from it session by session.
 
0. Read this first
Scope, honestly. Fifteen professional-tier certifications, three providers, plus the full engineering stack underneath them, is not a weekend, a month, or even a semester. Treated seriously — with real understanding, not memorized dumps — this is 18–30 months of consistent study for someone starting from true fundamentals. I'm telling you this not to discourage you but so we plan like adults: we go in phases, we build real skill that transfers across providers (so cert #2 through #15 get progressively faster), and we don't burn your $300 GCP credit or your motivation in week one.
 
Two time-sensitive corrections to your list, found while researching today:
 
Agentic Architect (Beta) — registration is open now and the beta window closes September 30, 2026 — about two weeks from today. Realistically, you cannot go from zero to exam-ready in two weeks while also learning fundamentals. My recommendation: let the beta window pass. The certification will reach General Availability afterward and you'll sit it properly, later, once you have the ADK/agent-building foundation (Track D4) and general GCP experience. Chasing the beta discount now would mean skipping comprehension for speed — exactly what you told me not to do.
AWS Security Specialty — your list says SCS-C02. That exam was decommissioned December 1, 2025; it's been replaced by SCS-C03 (restructured domains, new question types, added GenAI-security content). I've planned around SCS-C03.
One item on your list is confirmed accurate as stated: AWS Advanced Networking Specialty (ANS-C01) — official AWS page confirms last exam day is December 31, 2026. That's tight (3.5 months) and it's a five-year-experience-recommended exam with no announced successor. We'll revisit whether to chase it or let it lapse once you see how the rest of the pace goes — I'd rather you have real distributed-networking skill than a rushed cert for an exam being retired anyway.
 
Your hands-on reality (given $300 GCP credit, permanent free tier, a workplace GCP account you can look in but not touch, and AWS/Azure free tier only) is threaded through every module below as an explicit "Lab Reality" note. Short version: we'll do real hands-on work for anything that fits free tier or a small slice of the $300; for expensive/enterprise-only services (Spanner multi-region, BigQuery at scale, multi-region GKE, Anthos, etc.) we'll write real Terraform/gcloud/kubectl that we validate with plan/dry-run but don't apply, and use your workplace console read-only, as a museum, never to create or change anything there. That combination genuinely builds real, defensible skill — architects are hired for judgment about services they've read deeply and reasoned about, not just ones they've clicked.
 
1. The Phase Plan
Phase 0  Universal Fundamentals (Track A)              ─┐
Phase 1  Cloud Core Concepts (Track B)                   ├─ run mostly in parallel,
Phase 2  DevOps/Containers/K8s/NGINX/CI-CD spine (Track C)│  woven together — this is
Phase 3  ML/AI Foundations (Track D)                    ─┘  the "consolidate common concepts" layer
 
Phase 4  GCP deep dive  →  sit PCA, then PMLE first (your named priorities)
Phase 5  Remaining GCP Professional certs (pick 2–4 that match your goals, not all 8)
Phase 6  AWS deep dive  →  SAP-C02, DOP-C02, AIP-C01, (SCS-C03, ANS-C01 if time allows)
Phase 7  Azure deep dive → AZ-305, AZ-400, SC-100
Phase 8  Agentic Architect (GA) once ADK/agent material is solid
Why this order: everything in Phases 0–3 is provider-agnostic and is tested, in some form, on every single one of your fifteen certs. Front-loading it means each subsequent cert is 60–70% "same concepts, new console." GCP goes first because you named PCA/PMLE explicitly and have a workplace GCP account to look around in. AWS and Azure then go faster because you already know what a load balancer, an IAM policy, and a Kubernetes pod are — you're just learning new names and new console layouts for concepts you already own.
 
PART I — Universal Foundations (Track A)
High-school-accessible, zero assumed background. This is what makes everything downstream make sense instead of feeling like memorized trivia.
 
A1. Digital Logic & Data Representation
Bits, bytes, binary and hexadecimal number systems; why computers use base-2
Boolean logic (AND/OR/NOT/XOR) and truth tables — the literal basis of IAM policy evaluation, firewall rules, and CPU design
Binary vs. decimal storage prefixes (KiB/MiB/GiB vs KB/MB/GB) — directly relevant to cloud storage billing
Character encoding (ASCII, UTF-8) and why it matters for data pipelines
→ We start here, today, below.
A2. Math for Cloud & Machine Learning
Algebra refresher: functions, exponents, logarithms (logs matter for scaling, entropy, and Big-O)
Linear algebra essentials: vectors, matrices, dot products, matrix multiplication (the literal computation inside every neural network)
Probability & statistics: distributions, mean/variance/std-dev, conditional probability, Bayes' theorem, correlation vs causation
Calculus intuition: derivatives as "rate of change," gradients, why gradient descent trains ML models (no need for proof-level rigor — engineering intuition is the target)
Big-O notation for algorithm/cost reasoning
A3. Programming Foundations
Python: variables, control flow, functions, data structures (list/dict/set/tuple), OOP basics, virtual environments, package management (pip)
Bash/shell scripting: variables, loops, conditionals, pipes, redirection, exit codes — essential for CI/CD scripts and automation everywhere
Working with APIs from code: HTTP clients, JSON parsing, SDKs (google-cloud-*, boto3, azure-sdk)
Git fundamentals (deep dive lives in A11)
A4. Data Structures & Algorithms (engineering-practical depth, not competitive-programming depth)
Arrays, linked lists, hash maps, stacks/queues, trees, graphs
Big-O in practice: why a hash lookup beats a linear scan, why indexes matter in databases
Sorting/searching intuition (enough to reason about algorithmic choices, not to implement red-black trees from memory)
A5. Computer Networking (heavily tested across every cloud architect/network/security cert)
The OSI model and TCP/IP model — what actually lives at each layer
IP addressing: IPv4 structure, subnetting and CIDR notation (binary math from A1 comes back here), IPv6 basics
Routing fundamentals: how packets find their way, default gateways, routing tables
TCP vs UDP: three-way handshake, reliability vs speed trade-offs
DNS: how domain resolution works, record types (A, AAAA, CNAME, MX, TXT, NS)
HTTP/HTTPS: request/response cycle, methods, status codes, headers, cookies
TLS/SSL: the handshake, certificates, certificate authorities (ties into A10 security)
NAT, firewalls, proxies vs reverse proxies (sets up NGINX in Track C)
Load balancing concepts: L4 vs L7, algorithms (round robin, least connections, consistent hashing)
VPNs and private connectivity concepts
A6. Linux & Operating Systems
Processes, threads, memory management, the filesystem hierarchy
Linux shell essentials: navigation, permissions (chmod/chown), package managers, systemd/services
Containers vs VMs at the OS level: namespaces and cgroups (sets up Docker)
SSH and remote access
A7. Software Architecture & APIs
Client-server model, monoliths vs microservices, trade-offs of each
REST principles, gRPC, GraphQL (awareness-level)
Synchronous vs asynchronous communication; message queues and event-driven architecture (sets up Pub/Sub, SQS/SNS, Service Bus)
API authentication patterns: API keys, OAuth 2.0, JWTs, service accounts
A8. Databases & Data Modeling
Relational model, SQL fundamentals (SELECT/JOIN/GROUP BY, normalization)
ACID properties and transactions
NoSQL families: key-value, document, wide-column, graph — and when each fits
CAP theorem and its real engineering trade-offs
Data warehousing basics: OLTP vs OLAP, star schemas
A9. Distributed Systems Theory
Consistency models (strong, eventual), replication strategies
Partitioning/sharding, consensus (Raft/Paxos at a conceptual level — Spanner, etcd, and Kubernetes all depend on this)
Availability vs durability, failure modes, idempotency
Why "the network is reliable" is the first fallacy of distributed computing (and the other seven)
A10. Security & Cryptography Fundamentals
Symmetric vs asymmetric encryption, hashing vs encryption, digital signatures
The TLS handshake in detail, PKI and certificate chains
Authentication vs authorization; identity federation, SSO, MFA
Common attack classes: injection, XSS, CSRF, DDoS, privilege escalation
Principle of least privilege, defense in depth, zero trust — the conceptual spine of every cloud IAM system
A11. Software Delivery & Version Control
Git deep dive: branches, merges, rebases, conflict resolution, tagging
SDLC models, Agile/Scrum basics
Code review culture, trunk-based development vs GitFlow (relevant to CI/CD design choices later)
PART II — Cloud Computing Core Concepts (Track B)
B1. What Is Cloud Computing
Service models: IaaS, PaaS, SaaS, FaaS — and where each provider's services sit
Deployment models: public, private, hybrid, multi-cloud
The shared responsibility model (security "of" the cloud vs "in" the cloud) — appears on nearly every security-adjacent exam
B2. Virtualization & Containers
Hypervisors (Type 1 vs Type 2), how a VM actually works
Containers: why they're lighter than VMs, the namespace/cgroup mechanics from A6
Image layering and immutability as a concept
B3. Architecture Patterns & the Well-Architected Frameworks
High availability, fault tolerance, horizontal vs vertical scaling
Disaster recovery patterns: backup/restore, pilot light, warm standby, multi-site active-active — and RTO/RPO math
Provider-specific framework nuance: GCP's Architecture Framework (Operational Excellence, Security, Reliability, Performance/Cost) vs AWS's Well-Architected Framework (6 pillars incl. Sustainability) vs Azure's Well-Architected Framework (5 pillars). Same ideas, different names — we'll map them directly.
B4. Cloud Economics & FinOps
Pay-as-you-go vs reserved/committed-use pricing, spot/preemptible instances
Cost visibility and optimization tooling per provider
Budget alerts, tagging/labeling for cost allocation
B5. Cloud IAM Concepts (deep provider dives happen later; the model is universal)
Principals, roles/policies, resource hierarchies (org → folder/OU → project/account)
RBAC vs ABAC, policy inheritance, least-privilege design
Service accounts / managed identities and workload identity federation
PART III — The DevOps / Containers / CI-CD Spine (Track C)
This is the cross-cutting engineering core you asked to be taught "in parallel" and "exhaustively." It underlies the DevOps Engineer, Cloud Developer, Cloud Architect, and DOP-C02/AZ-400 certs directly, and shows up as scenario content everywhere else.
 
C1. Docker — full depth
Images vs containers, the union filesystem and layer caching
Writing Dockerfiles: FROM, RUN, COPY, ENTRYPOINT vs CMD, multi-stage builds for small production images
Container networking modes (bridge, host, none), volumes vs bind mounts vs tmpfs
Docker Compose for multi-container local dev
Registries: pushing/pulling, tagging strategy, image scanning for vulnerabilities
Security: running as non-root, minimal base images (distroless/alpine), secrets handling anti-patterns
C2. Kubernetes — full depth
Architecture: control plane (API server, etcd, scheduler, controller manager) vs worker nodes (kubelet, kube-proxy, container runtime)
Core objects: Pods, ReplicaSets, Deployments, StatefulSets, DaemonSets, Jobs/CronJobs
Networking: Services (ClusterIP/NodePort/LoadBalancer), Ingress and Ingress controllers (NGINX Ingress lands here), Network Policies, the CNI model
Configuration: ConfigMaps, Secrets, environment injection
Storage: PersistentVolumes, PersistentVolumeClaims, StorageClasses, dynamic provisioning
Scheduling & scaling: node affinity/taints/tolerations, Horizontal Pod Autoscaler, Vertical Pod Autoscaler, Cluster Autoscaler
RBAC in Kubernetes, Pod Security Standards, admission controllers
Helm: charts, templating, releases
Operators and the Operator pattern (brief — enough for exam recognition)
Managed Kubernetes nuance: GKE (Autopilot vs Standard, node auto-provisioning, Workload Identity) vs EKS (Fargate vs managed node groups, IRSA) vs AKS (virtual nodes, Azure AD pod identity) — same primitives, different managed-service ergonomics
C3. NGINX — full depth
Reverse proxy and forward proxy concepts (ties back to A5)
Core config syntax: server blocks, location matching, directives
Load balancing algorithms in NGINX (round robin, least_conn, ip_hash) and upstream blocks
TLS termination, HTTP→HTTPS redirects, HTTP/2
Caching and static content serving
NGINX as a Kubernetes Ingress Controller — how it fits into the C2 picture concretely
C4. CI/CD — full depth
Concepts: build → test → package → deploy pipeline stages, artifact repositories
Deployment strategies: rolling, blue-green, canary — and how to pick one from a scenario
GitOps as a philosophy (declarative, git-as-source-of-truth, reconciliation loops) — ArgoCD/Flux at a working level
Provider-native tooling, mapped side by side:
Build: Cloud Build (GCP) ↔ CodeBuild (AWS) ↔ Azure Pipelines (build stage)
Deploy: Cloud Deploy (GCP) ↔ CodePipeline/CodeDeploy (AWS) ↔ Azure Pipelines/Release (Azure)
Universal/cross-cloud: GitHub Actions, Jenkins, GitLab CI
C5. Infrastructure as Code
Declarative vs imperative provisioning, state management, drift detection
Terraform as our primary cross-cloud tool: providers, resources, modules, plan/apply/destroy, remote state, workspaces — this is what lets us build real GCP/AWS/Azure architectures without necessarily paying for them (we lean hard on terraform plan)
Native IaC per provider (recognize, don't need mastery of all): Deployment Manager / Config Connector / Infrastructure Manager (GCP), CloudFormation / CDK (AWS), ARM templates / Bicep (Azure)
C6. Observability
The three pillars: metrics, logs, traces
Provider-native stacks: Cloud Monitoring/Logging/Trace (GCP) ↔ CloudWatch/X-Ray (AWS) ↔ Azure Monitor/Application Insights (Azure)
Open standards: Prometheus + Grafana, OpenTelemetry — increasingly tested because they're the multi-cloud-portable answer
C7. SRE Principles
SLIs, SLOs, SLAs and how they relate; error budgets and burn-rate alerting
Toil and why eliminating it is an SRE's actual job
Incident management, on-call, postmortem culture (blameless postmortems)
This shows up explicitly and heavily on the PCA exam's Reliability domain and on DOP-C02/AZ-400 — it is not optional reading.
PART IV — Machine Learning & AI Foundations (Track D)
Required for PMLE, AIP-C01, and Agentic Architect specifically — but every architect-level cert now touches "how do I put AI in this design" too.
 
D1. Classical Machine Learning
Supervised vs unsupervised vs reinforcement learning
Regression, classification, clustering — core algorithms and when to use which
Train/validation/test splits, cross-validation
Evaluation metrics: accuracy, precision, recall, F1, ROC/AUC, confusion matrices — and why accuracy alone lies to you on imbalanced data
Overfitting/underfitting, the bias-variance tradeoff, regularization
Feature engineering: scaling, encoding categoricals, handling missing data, imbalanced datasets (SMOTE, class weighting)
D2. Deep Learning
Neural network basics: neurons, layers, activation functions, forward pass
Backpropagation intuition (built on the calculus from A2)
CNNs (images), RNNs/LSTMs (sequences, mostly historical context now)
Transformers and attention — the architecture behind every modern LLM; this is a must-understand-deeply topic, not a footnote
D3. MLOps
The end-to-end ML lifecycle: data → features → train → evaluate → deploy → monitor → retrain
Feature stores, model registries, experiment tracking
CI/CD/CT (continuous training) for ML pipelines
Model monitoring: drift, training-serving skew, performance decay
A/B testing and canary rollouts for models specifically
D4. Generative AI, LLMs & Agents
How LLMs actually generate text (autoregressive next-token prediction, sampling, temperature)
Prompting techniques, few-shot vs zero-shot, system prompts
Embeddings and vector databases; Retrieval-Augmented Generation (RAG) architecture end to end
Fine-tuning vs prompt engineering vs RAG — when each is the right tool
Agentic patterns: tool use, planning/reasoning loops, multi-agent orchestration, agent-to-agent protocols (A2A) — directly relevant to the Agentic Architect cert
Responsible AI: bias, fairness, explainability, safety evaluation
PART V — Google Cloud Platform
Service map by category (the vocabulary we'll build fluency in)
Compute: Compute Engine, GKE, Cloud Run, App Engine, Cloud Functions
Storage/DB: Cloud Storage, Cloud SQL, Spanner, Bigtable, Firestore, Memorystore, AlloyDB
Networking: VPC, Cloud Load Balancing, Cloud CDN, Cloud Interconnect/VPN, Cloud DNS, Cloud Armor
Data/Analytics: BigQuery, Pub/Sub, Dataflow, Dataproc, Cloud Composer, Looker
AI/ML: Vertex AI (full suite: Workbench, Training, Pipelines, Feature Store, Model Registry, Endpoints, Vizier), Model Garden, Gemini Enterprise/Agent Platform, AutoML, BigQuery ML
Security: IAM, Cloud KMS, VPC Service Controls, Binary Authorization, Security Command Center, Google SecOps (Chronicle)
Ops/DevOps: Cloud Build, Cloud Deploy, Artifact Registry, Cloud Monitoring/Logging
Certification-by-certification breakdown
(Domain weights below are from the current official exam guides where I verified them directly; where I didn't verify exact percentages, I've given you the topic structure and flagged it — always cross-check the live guide a few weeks before you actually schedule.)
 
1. Professional Cloud Architect (PCA) — your named priority #1
 
Format: 50 scenario-based questions, 2 hours, includes 4 published case studies you study in advance
Domains (verified): Designing (24%) · Provisioning (15%) · Security & Securing AI (20%) · Optimization (18%) · Implementation (11%) · Reliability & Well-Architected Framework (12%)
What makes it hard: it's not "what does this service do," it's "given these constraints, which trade-off is correct" — architectural judgment, tested through the case studies
2. Professional Machine Learning Engineer (PMLE) — your named priority #2
 
6 domains covering the full ML lifecycle: framing business problems as ML problems · architecting low-code/AutoML/BigQuery ML solutions · building with Google's AI APIs and foundation models (Gemini, Model Garden) · developing/scaling custom models (Vertex AI Training, distributed training, hyperparameter tuning) · automating MLOps pipelines (Vertex AI Pipelines, CI/CD/CT) · monitoring, responsible AI, and maintaining solutions in production
Heavy 2026 emphasis on GenAI: Vertex AI Studio, Model Garden, RAG architectures
3. Data Engineer
 
Designing data processing systems · building/operationalizing data pipelines (Dataflow, Dataproc, Pub/Sub, BigQuery, Composer) · operationalizing ML models · ensuring reliability, security, and compliance of data solutions
4. Cloud Developer
 
Designing highly scalable/available cloud-native apps · building and testing applications · deploying (Cloud Build, Cloud Deploy, Cloud Run/GKE/App Engine) · integrating with GCP managed services and APIs · monitoring application performance
5. Cloud DevOps Engineer
 
Applying SRE principles to service design and operations (Track C7 directly) · building CI/CD pipelines · implementing observability · optimizing performance · managing releases and incidents
6. Cloud Security Engineer
 
Configuring access (IAM design) · configuring network security (VPC-SC, firewall, Cloud Armor) · ensuring data protection (KMS, DLP) · managing security operations · ensuring regulatory compliance
7. Cloud Network Engineer
 
Designing/planning GCP network architecture · implementing VPC · configuring network services (load balancing, DNS, CDN) · implementing hybrid connectivity (Interconnect/VPN) · implementing network security · managing/monitoring networks
8. Cloud Database Engineer
 
Designing scalable/secure database solutions (choosing the right DB from the whole storage list) · managing solutions (migration, provisioning) · designing for security/compliance · optimizing performance and monitoring
9. Security Operations Engineer (newer cert — verify current exam guide closer to study time)
 
Threat detection and hunting · SIEM/SOAR configuration and use (Google SecOps/Chronicle) · incident response · threat intelligence · using Gemini-assisted security operations tooling
10. Agentic Architect (Beta → GA) — we're deliberately doing this last, per the plan above
 
Two-part exam: proctored multiple-choice (conceptual/design) plus hands-on coding labs on Google Skills
~5 sections; roughly a third of the exam is writing actual agent code
Built around: Agent Development Kit (ADK), Agent Registry, Agent Gateway, the A2A (agent-to-agent) protocol, LLM/agent design patterns, reliability/cost/security/scalability of agentic systems
Lab Reality (GCP): Compute Engine (e2-micro), Cloud Run, Cloud Functions, Cloud Storage, Firestore, and Pub/Sub all have genuine always-free tiers — we'll build real projects on these at zero cost. Your $300 credit is the right budget for: a short-lived GKE cluster, a small BigQuery dataset, and Vertex AI training/prediction experiments — we'll timebox these deliberately. Spanner, multi-region deployments, and Anthos we'll study via architecture + Terraform-plan only, and via read-only tours of your workplace console (never creating/modifying resources there).
 
PART VI — AWS
Service map by category (cross-referenced to GCP — see Part VIII for the full table)
Compute: EC2, Lambda, ECS/EKS, Fargate, App Runner · Storage/DB: S3, EBS, RDS, DynamoDB, Aurora · Networking: VPC, ELB (ALB/NLB), Route 53, CloudFront, Direct Connect · Data: Kinesis, Glue, Redshift, EMR · AI/ML: SageMaker, Bedrock · Security: IAM, KMS, GuardDuty, Security Hub, Macie · DevOps: CodeBuild/CodePipeline/CodeDeploy, CloudFormation/CDK
 
1. Solutions Architect – Professional (SAP-C02)
 
4 domains: Design for Organizational Complexity (~26%) · Design for New Solutions (~29%) · Continuous Improvement for Existing Solutions (~25%) · Accelerate Workload Migration and Modernization (~20%) (check current guide for exact figures)
Heavy on multi-account strategy (AWS Organizations, SCPs), the 6 R's of migration, and cost/resilience trade-offs at enterprise scale
2. DevOps Engineer – Professional (DOP-C02)
 
~6 domains: SDLC Automation · Configuration Management & IaC · Resilient Cloud Solutions · Monitoring & Logging · Incident & Event Response · Security & Compliance
Direct extension of Track C — you'll recognize nearly everything, just under AWS-native tool names
3. Generative AI Developer – Professional (AIP-C01) — genuinely new (2025/2026), one of AWS's hardest exams by reputation
 
Domains cover: selecting/architecting with foundation models (Bedrock) · building resilient, provider-flexible GenAI architectures · RAG, vector stores, and knowledge base design · data security, privacy, and responsible-AI governance for GenAI systems · cost/latency/performance optimization
Recommendation candidates already hold AWS ML/Data Engineer associate-level knowledge — we'll build that via Track D first
4. Security – Specialty (SCS-C03) (corrected from your SCS-C02 — that version retired Dec 1, 2025)
 
Current domains (Dec 2025 refresh): Identity & Access Management (~20%) · Data Protection (~18%) · Infrastructure Security (~18%) · Detection (~16%, now its own domain) · Incident Response (~14%) · Management & Security Governance
New emphasis on GenAI-application security guardrails
5. Advanced Networking – Specialty (ANS-C01) — last exam day Dec 31, 2026 per AWS, no announced successor
 
Hybrid IT network architecture at scale: BGP, Direct Connect, Transit Gateway, multi-region networking, network security (WAF/Shield/Network Firewall), automation
Five-year-networking-experience recommended candidate; we'll fold the concepts into Track A5/C naturally either way — the cert itself is optional depending on how our timeline looks by mid-2026
Lab Reality (AWS): Free tier covers EC2 t2/t3.micro (750 hrs/mo for 12 months on new accounts — check current status of your account), Lambda (1M requests/mo, always-free), S3 (5GB), DynamoDB (25GB, always-free). For VPC/networking/multi-account work we'll build with Terraform and validate via plan, since Organizations/Transit Gateway/multi-account labs cost real money fast.
 
PART VII — Azure
Service map by category
Compute: Virtual Machines, AKS, Container Apps, Functions, App Service · Storage/DB: Blob Storage, Azure SQL Database, Cosmos DB, Managed Disks · Networking: VNet, Azure Load Balancer, Application Gateway, Front Door, Azure DNS, ExpressRoute · Data: Synapse Analytics, Data Factory, Stream Analytics · AI/ML: Azure Machine Learning, Azure AI Foundry (OpenAI Service) · Security: Microsoft Entra ID, Key Vault, Microsoft Defender, Microsoft Sentinel · DevOps: Azure Pipelines, Azure Repos, ARM/Bicep
 
Provider-specific nuance to know up front: unlike GCP and AWS, Azure's Expert-tier exams have real prerequisites — AZ-305 requires an active AZ-104; AZ-400 requires AZ-104 or AZ-204; SC-100 requires one of AZ-500/SC-200/SC-300. This means your Azure path structurally requires associate-level certs first even though you only named the Expert ones — we'll fold AZ-104-equivalent knowledge into Track G teaching either way, whether or not you sit that exact exam.
 
1. Solutions Architect Expert (AZ-305) (English version last updated April 17, 2026 — current)
 
Scenario-heavy, spans identity, data, infrastructure, and governance design decisions
No live labs (unlike AZ-104); rewards architectural judgment over recall — closest Azure analog to the GCP PCA
2. DevOps Engineer Expert (AZ-400)
 
Source control strategy, CI/CD pipeline design (Azure Pipelines + GitHub Actions), IaC (ARM/Bicep/Terraform), release/deployment strategies, security & compliance in the pipeline, monitoring feedback loops
The direct Track C capstone for Azure
3. Cybersecurity Architect Expert (SC-100) (English version updated July 28, 2026 — current)
 
Designing Zero Trust strategy, security operations/identity/compliance architecture across hybrid environments
Growing AI-governance content share (10–12%+ by mid-2026 per Microsoft's own roadmap signals)
Lab Reality (Azure): Free account gives $200 credit for 30 days plus always-free services (small VM instances, limited Functions executions, Cosmos DB free tier). Because that initial credit window is short, we'll time our Azure phase deliberately and lean on Terraform-plan + architecture design work for anything beyond the always-free slice.
 
PART VIII — Cross-Provider Concept Map
The "don't learn it three times" table. Same underlying idea, three names.
 
Concept	GCP	AWS	Azure
Virtual machines	Compute Engine	EC2	Virtual Machines
Managed Kubernetes	GKE	EKS	AKS
Serverless containers	Cloud Run	App Runner / Fargate	Container Apps
Functions-as-a-service	Cloud Functions	Lambda	Azure Functions
PaaS app hosting	App Engine	Elastic Beanstalk	App Service
Object storage	Cloud Storage	S3	Blob Storage
Block storage	Persistent Disk	EBS	Managed Disks
Managed relational DB	Cloud SQL	RDS	Azure SQL Database
Globally distributed DB	Spanner	Aurora Global/DynamoDB	Cosmos DB
Wide-column NoSQL	Bigtable	DynamoDB / Keyspaces	Cosmos DB (Cassandra API)
Document NoSQL	Firestore	DynamoDB	Cosmos DB
In-memory cache	Memorystore	ElastiCache	Azure Cache for Redis
Data warehouse	BigQuery	Redshift	Synapse Analytics
Pub/Sub messaging	Pub/Sub	SNS + SQS	Service Bus / Event Grid
Stream/batch data processing	Dataflow (Apache Beam)	Kinesis / Glue	Stream Analytics
Managed Spark/Hadoop	Dataproc	EMR	HDInsight
Data pipeline orchestration	Cloud Composer (Airflow)	MWAA (Airflow)	Data Factory
BI/visualization	Looker / Looker Studio	QuickSight	Power BI
Virtual network	VPC	VPC	VNet
Load balancing	Cloud Load Balancing	ELB (ALB/NLB/GLB)	Load Balancer / App Gateway
CDN	Cloud CDN	CloudFront	Azure CDN / Front Door
DNS	Cloud DNS	Route 53	Azure DNS
Hybrid connectivity	Cloud Interconnect/VPN	Direct Connect/VPN	ExpressRoute/VPN Gateway
Identity & access	Cloud IAM	AWS IAM	Microsoft Entra ID + Azure RBAC
Key management	Cloud KMS	AWS KMS	Key Vault
Secrets management	Secret Manager	Secrets Manager	Key Vault
WAF / DDoS protection	Cloud Armor	AWS WAF / Shield	Azure WAF / DDoS Protection
Container registry	Artifact Registry	ECR	Azure Container Registry
CI build service	Cloud Build	CodeBuild	Azure Pipelines
CD/release service	Cloud Deploy	CodePipeline/CodeDeploy	Azure Pipelines/Release
Native IaC	Deployment Manager / Config Connector	CloudFormation / CDK	ARM / Bicep
Metrics/monitoring	Cloud Monitoring	CloudWatch	Azure Monitor
Logging	Cloud Logging	CloudWatch Logs	Azure Monitor Logs
Distributed tracing	Cloud Trace	X-Ray	Application Insights
ML platform	Vertex AI	SageMaker	Azure Machine Learning
GenAI/foundation models	Model Garden / Gemini	Bedrock	Azure AI Foundry (OpenAI Service)
Org hierarchy	Org → Folder → Project	Organization → OU → Account	Management Group → Subscription
Org-wide policy	Organization Policy	Service Control Policies	Azure Policy
SIEM/SecOps	Google SecOps (Chronicle)	Security Hub / GuardDuty	Microsoft Sentinel / Defender
PART IX — Time-Sensitive Notes Recap
Agentic Architect beta closes Sept 30, 2026 — we're intentionally skipping the beta window and targeting GA later.
AWS ANS-C01 last exam Dec 31, 2026 — decide later, once we see real progress against the plan; no shame either way.
AWS Security Specialty is now SCS-C03, not SCS-C02 — already corrected in this plan.
Check every exam guide's live PDF ~4–6 weeks before you actually schedule — Google, AWS, and Microsoft all revise domain weights and content periodically (several did so earlier this year), and I'll flag anything relevant I notice as we go, but I can't watch it continuously between our sessions.
PART X — How We'll Actually Work
Each session, we take one module from the plan above, I teach it properly (explanations, worked examples, real config/code where it applies, checks for understanding), and we mark it done. Tell me any time you want to:
 
Skip ahead on something you already know (say so — no need to sit through material you've got)
Jump to a specific cert's material directly instead of following the phase order
Go hands-on on something — I'll tell you honestly whether it fits free tier, needs a slice of your $300, or should stay as a Terraform-plan/console-read exercise
We start with A1: Digital Logic & Data Representation below, right now.
