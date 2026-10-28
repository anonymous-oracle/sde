# Part 24 · Cloud Providers: Google Cloud, AWS, Azure & Certifications (part 2 of 2) · TOPIC LIST

Rules and directives for this part: `index/part24_cloud_providers_2of2.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Cloud Providers: Google Cloud, AWS, Azure & Certifications (part 2 of 2)

### Google Cloud — mapping system-design components

- DNS → Cloud DNS; CDN → Cloud CDN or Media CDN; load balancer → Cloud Load Balancing; reverse proxy → the global Application LB, NGINX on Compute Engine or GKE, or Cloud Run's front end
- Application servers → Cloud Run, GKE, MIGs, App Engine; workers → Cloud Run jobs, GKE, Cloud Run functions
- Object store → Cloud Storage; SQL with replicas → Cloud SQL, AlloyDB, Spanner; wide-column → Bigtable; documents → Firestore; cache → Memorystore
- Message queue → Pub/Sub or Managed Kafka; task queue and scheduler → Cloud Tasks and Cloud Scheduler; warehouse → BigQuery; batch → Dataflow, Dataproc, BigQuery SQL
- Search → Elasticsearch or OpenSearch on GKE, Elastic Cloud, Agent Search; a search index is an inverted index from terms to documents, with analyzers that split and normalize text and a relevance score such as BM25; Elasticsearch and OpenSearch spread an index over shards with replicas, and on GKE the team sizes and upgrades the cluster itself, while Elastic Cloud is hosted by the vendor; Agent Search is a managed retrieval service for grounded answers over documents, suited to teams that would rather not operate shards
- Service discovery → Service Directory, GKE DNS, Cloud Service Mesh; autoscaling → MIG autoscaler, Cloud Run, GKE autoscalers
- Monitoring → Cloud Monitoring, Logging, Trace, Error Reporting; push notifications → Pub/Sub, Cloud Run and Firebase Cloud Messaging; email through a partner relay
- Secrets → Secret Manager and Cloud KMS; WAF and DDoS → Cloud Armor; private networking → VPC, firewall rules, Cloud NAT, Private Google Access, IAP
- Paper systems to products: MapReduce → Dataflow and Dataproc; Spark → Dataproc; Storm → Dataflow streaming; Bigtable and HBase → Bigtable; Cassandra → Bigtable; Dynamo → Firestore, Bigtable or Spanner; MongoDB → Firestore with MongoDB compatibility or Atlas; Memcached and Redis → Memorystore; GFS → Colossus beneath Cloud Storage; HDFS → Cloud Storage; Dapper → Cloud Trace; Kafka → Pub/Sub or Managed Kafka; Chubby and ZooKeeper → no managed equivalent (etcd behind the GKE API server)

### AWS

- Compute: EC2, Lambda, ECS and EKS (managed node groups, IRSA) with Fargate, App Runner, Elastic Beanstalk
- Storage and databases: S3, EBS, RDS, Aurora and Aurora Global Database, DynamoDB, Keyspaces, ElastiCache
- Networking: VPC, ELB (ALB, NLB, GWLB), Route 53, CloudFront, Direct Connect, Transit Gateway, Site-to-Site VPN
- Data: Kinesis, Glue, Redshift, EMR, MWAA, QuickSight; Kinesis Data Streams is a sharded, ordered stream of records for real-time ingestion; Glue is serverless ETL with a shared data catalog; Redshift is a columnar, massively parallel SQL warehouse; EMR runs Spark, Hadoop and similar open-source clusters; MWAA is managed Apache Airflow for pipeline orchestration; QuickSight is the business-intelligence dashboard service
- AI and ML: SageMaker, Bedrock; SageMaker is a managed platform to build, train, tune and deploy machine learning models on managed training and hosting infrastructure; Bedrock is a managed API to foundation models from several providers, so the team runs no model servers itself
- Security: IAM, Organizations and service control policies, KMS, Secrets Manager, GuardDuty, Security Hub, Macie, WAF, Shield, Network Firewall; Zelkova-style automated policy reasoning
- DevOps: CodeBuild, CodePipeline, CodeDeploy, CloudFormation, CDK, ECR, CloudWatch, X-Ray

### AWS command line

- **Setup and credentials**
  - AWS CLI version 2; `aws configure` writing `~/.aws/credentials` and `~/.aws/config`; named profiles with `--profile` or `AWS_PROFILE`; `--region` or `AWS_REGION`
  - IAM Identity Center sign-in: `aws configure sso` and `aws sso login`; short-lived credentials instead of long-lived access keys
  - The credential provider chain: command-line options, environment variables, SSO and assumed-role profiles, shared files, container and instance metadata roles
  - `aws sts get-caller-identity` to confirm who you are; `aws sts assume-role --role-arn --role-session-name`; `role_arn` and `source_profile` in profiles
- **Command structure and output**
  - `aws service operation --parameters`; high-level `aws s3` commands versus API-shaped `aws s3api`
  - `--output json`, `yaml`, `text` or `table`; `--query` with JMESPath (`Reservations[].Instances[].[InstanceId,State.Name]`); server-side `--filters Name=…,Values=…`
  - Pagination: automatic by default; `--max-items`, `--starting-token`, `--page-size`, `--no-paginate`
  - `--dry-run` permission checks for EC2; waiters such as `aws ec2 wait instance-running`; `--cli-input-json` with `--generate-cli-skeleton`; `file://` and `fileb://` arguments; `--debug`; `aws help`
- **Common services**
  - S3: `aws s3 ls`, `mb`, `cp --recursive`, `sync --delete`, `mv`, `rm`, `presign --expires-in`; `aws s3api put-bucket-versioning`, `put-public-access-block`, `put-bucket-lifecycle-configuration`, `put-bucket-policy`, `get-object --range`
  - EC2 and VPC: `aws ec2 run-instances --image-id --instance-type --subnet-id --security-group-ids --iam-instance-profile --user-data`; `describe-instances`; `stop-instances` and `terminate-instances`; `create-vpc`, `create-subnet`, `create-security-group`, `authorize-security-group-ingress`
  - Systems Manager: `aws ssm start-session --target` instead of SSH; `aws ssm get-parameter --with-decryption`; `aws ssm send-command`
  - IAM: `aws iam create-role --assume-role-policy-document file://trust.json`; `attach-role-policy` and `put-role-policy`; `create-instance-profile`; `aws iam simulate-principal-policy`; `aws accessanalyzer validate-policy`
  - Lambda: `aws lambda create-function --runtime --handler --role --zip-file fileb://`; `update-function-code`; `invoke --payload` with `--cli-binary-format raw-in-base64-out`; `publish-version` and aliases
  - Containers: `aws ecr create-repository`; `aws ecr get-login-password | docker login --username AWS --password-stdin ACCOUNT.dkr.ecr.REGION.amazonaws.com`; `aws ecs update-service --force-new-deployment`; `aws eks update-kubeconfig --name`; `eksctl create cluster`
  - CloudFormation: `aws cloudformation deploy --template-file --stack-name --capabilities CAPABILITY_IAM --parameter-overrides`; `create-change-set` and `describe-change-set`; `describe-stack-events`; `aws cloudformation validate-template`
  - Data: `aws dynamodb create-table --billing-mode PAY_PER_REQUEST`, `put-item`, `get-item`, `query --key-condition-expression`; `aws rds create-db-instance`, `describe-db-instances`, `generate-db-auth-token`; `aws sqs send-message` and `receive-message`; `aws sns publish`
  - Security: `aws secretsmanager create-secret` and `get-secret-value`; `aws kms create-key`, `encrypt`, `decrypt`, `generate-data-key`
  - Observability and cost: `aws logs tail --follow`; `aws logs start-query` for Logs Insights; `aws cloudwatch put-metric-alarm`; `aws ce get-cost-and-usage`
  - Foundation models: `aws bedrock list-foundation-models`; `aws bedrock-runtime converse --model-id`
  - Related tools: AWS SAM CLI (`sam build`, `sam deploy --guided`, `sam local invoke`); the CDK CLI (`cdk bootstrap`, `synth`, `diff`, `deploy`)

### Azure

- Compute: Virtual Machines and scale sets, AKS (virtual nodes, workload identity), Container Apps, Container Instances, Functions, App Service with deployment slots
- Storage and databases: Blob Storage, Azure Files, Managed Disks, Azure SQL Database, Cosmos DB (including its Cassandra API), Azure Cache for Redis
- Networking: VNet, network and application security groups, Azure Load Balancer, Application Gateway, Front Door, Azure CDN, Azure DNS, ExpressRoute, VPN Gateway, Bastion, private and service endpoints
- Data: Synapse Analytics, Data Factory, Stream Analytics, HDInsight, Power BI; Synapse Analytics combines a SQL data warehouse with Spark pools over the same data; Data Factory runs ETL and ELT pipelines built from activities through a visual designer; Stream Analytics runs SQL-like queries with time windows over event streams; HDInsight runs managed open-source clusters such as Hadoop, Spark and Kafka; Power BI builds reports and dashboards over semantic models
- AI and ML: Azure Machine Learning, Azure AI Foundry; Azure Machine Learning is the workspace for training jobs, pipelines, registered models and managed online endpoints; Azure AI Foundry is the platform for building generative AI applications, with a model catalog, deployments, evaluation and agent tooling
- Identity and security: Microsoft Entra ID (Conditional Access, PIM, entitlement management, B2B, Agent ID), Azure RBAC, Key Vault, Microsoft Defender for Cloud, Defender XDR, Microsoft Sentinel, Microsoft Purview, Azure Policy, management groups
- DevOps: Azure Pipelines, Azure Repos, Azure Artifacts, Azure Boards, ARM templates and Bicep, Azure Monitor and Application Insights, Kusto Query Language

### Azure command line

- **Setup and context**
  - `az login` interactively, with `--use-device-code`, as a service principal or with `--identity` (managed identity); `az logout`
  - Subscriptions: `az account list`, `az account set --subscription`, `az account show`
  - Defaults: `az config set defaults.group=… defaults.location=…`; `az extension add` and `list`; `az upgrade`; `az version`
- **Command structure and output**
  - `az group subgroup command --parameters`; resource groups as the deployment and deletion unit (`az group create`, `az group delete --yes --no-wait`)
  - `--output` (`-o`) as `json`, `jsonc`, `yaml`, `table`, `tsv` or `none`; `--query` with JMESPath; `tsv` output into shell variables
  - `--only-show-errors`, `--debug`, `--verbose`; `az find` for examples; `az rest` for any ARM endpoint; `az resource list`, `show` and `delete --ids`
- **Common services**
  - Compute: `az vm create --image --size --admin-username --generate-ssh-keys --assign-identity`; `az vm open-port`; `az vm run-command invoke`; `az vm deallocate` versus `stop`; `az vmss create` and `scale`
  - Networking: `az network vnet create --subnet-name --subnet-prefixes`; `az network nsg create` and `nsg rule create`; `az network public-ip create`; `az network private-endpoint create`; `az network bastion ssh`
  - Storage: `az storage account create --sku Standard_LRS --kind StorageV2`; `az storage container create --auth-mode login`; `az storage blob upload`, `upload-batch`, `download` and `list`; `az storage blob generate-sas`
  - Containers: `az acr create`, `az acr login`, `az acr build`; `az aks create --enable-managed-identity --enable-oidc-issuer --enable-workload-identity --node-count`; `az aks get-credentials`; `az aks nodepool add`; `az aks upgrade`; `az containerapp up` and `create`
  - App platforms: `az webapp up`; `az webapp deployment slot create` and `swap`; `az functionapp create`; `az webapp log tail`
  - Identity and access: `az ad sp create-for-rbac`; `az ad app federated-credential create` for workload identity federation from CI; `az identity create`; `az role assignment create --assignee --role --scope`; `az role definition create`
  - Key Vault: `az keyvault create --enable-rbac-authorization`; `az keyvault secret set` and `show`; `az keyvault key create`
  - Deployments: `az deployment group create --template-file main.bicep --parameters`; `az deployment group what-if`; `az deployment sub create` for subscription scope; `az bicep build`; `az policy assignment create`
  - Data: `az sql server create` and `az sql db create`; `az cosmosdb create`; a logical SQL server holds databases with a server-level firewall and admin login, and a database is then created on it with a chosen service tier and size; `az cosmosdb create` makes the account, under which databases and containers are created, and a container's partition key is fixed when the container is created, so it must be chosen from the access pattern
  - Monitoring: `az monitor log-analytics query --workspace --analytics-query` with Kusto; `az monitor metrics alert create`; `az monitor activity-log list`

### AWS and Azure — what differs at depth

- **Networks**: AWS VPCs and Azure VNets are regional, where a Google Cloud VPC is global; AWS subnets live in one Availability Zone while Azure subnets span the zones of a region; regions are joined by peering or a hub (Transit Gateway, Virtual WAN)
- **AWS IAM evaluation**: an explicit deny anywhere wins; an action needs an allow from an identity-based or resource-based policy; service control policies, permission boundaries and session policies only cap what can be allowed; roles are assumed through STS, and cross-account access needs both accounts to agree
- **Azure identity**: Entra ID roles govern the directory, Azure RBAC governs resources at management-group, subscription, resource-group or resource scope and is inherited downward; deny assignments; system- and user-assigned managed identities
- **Key-value and document stores**: DynamoDB partition and sort keys, on-demand versus provisioned read and write capacity, eventually consistent global secondary indexes, single-table design; Cosmos DB request units, partition keys and logical-partition limits, and five consistency levels (strong, bounded staleness, session, consistent prefix, eventual)
- **Object storage**: S3 strong read-after-write consistency, storage classes and lifecycle rules, bucket policies and Block Public Access; Azure storage accounts with LRS, ZRS, GRS and GZRS redundancy and hot, cool, cold and archive tiers
- **Functions**: Lambda execution-environment reuse and cold starts, reserved and provisioned concurrency, the 15-minute limit, event source mappings; Azure Functions hosting plans and Durable Functions orchestrations
- **Governance**: AWS Organizations with Control Tower landing zones, service control policies and resource control policies; Azure management groups, Azure Policy effects (deny, audit, modify, deployIfNotExists) and Cloud Adoption Framework landing zones
- **Commitments and discounts**: AWS Savings Plans, Reserved Instances and Spot; Azure reservations, savings plans, Spot VMs and Hybrid Benefit

### Cross-provider concept map

- Virtual machines: Compute Engine · EC2 · Virtual Machines; a VM is a guest operating system on a hypervisor, sized by an instance or machine family, with attached disks and an identity the workload uses to call APIs; Compute Engine's VPC is global while EC2 and Azure VNets are regional, so the same network design needs different subnet layouts
- Managed Kubernetes: GKE · EKS · AKS; the provider runs the Kubernetes API server and control plane, and the team's workloads run on node pools it manages, or on capacity the provider manages in GKE Autopilot; the pod-to-cloud identity mechanisms differ (Workload Identity on GKE, IRSA on EKS, workload identity on AKS), so access set up on one cluster does not transfer as is
- Serverless containers: Cloud Run · App Runner and Fargate · Container Apps; the team supplies a container image and the platform runs it without managing nodes; Cloud Run and Container Apps can scale to zero, while a Fargate task runs until it is stopped or replaced, so cost and cold-start behaviour differ
- Functions: Cloud Run functions · Lambda · Azure Functions; code runs per event or request, is billed per invocation and duration, and the platform manages scaling; execution limits, reuse of the runtime environment and cold-start behaviour differ among the three, so a handler built around one provider's limits must be rechecked before a move
- PaaS hosting: App Engine · Elastic Beanstalk · App Service; the platform builds, runs, patches and scales a web application from code or a container, so the team manages the application rather than the servers; visibility of the underlying VMs differs, since Elastic Beanstalk provisions EC2 instances in the account, and App Service offers deployment slots for staged releases
- Object storage: Cloud Storage · S3 · Blob Storage; a flat namespace of objects addressed by key inside buckets or containers and reached over HTTP, with durability from replication; the three differ in consistency and redundancy choices, such as strong read-after-write consistency in Amazon Simple Storage Service and the LRS, ZRS, GRS and GZRS redundancy options of Azure storage accounts
- Block storage: Persistent Disk · EBS · Managed Disks; a network-attached block device usually attached to one VM at a time, with snapshots for backup; an EBS volume is bound to one Availability Zone, Persistent Disk is zonal or regional with synchronous replication across two zones, and Managed Disks have their own redundancy choices, so a disk cannot always follow a VM to another zone
- Managed relational: Cloud SQL · RDS · Azure SQL Database; the provider runs the database engine with automated backups, patching and failover, while the team chooses the engine version, size and replication; failover mechanics differ (Cloud SQL's regional HA uses a synchronous standby, not a read replica), so the recovery point and recovery time must be checked for each product rather than assumed equal
- Globally distributed database: Spanner · Aurora Global and DynamoDB · Cosmos DB; replicas across several regions under a stated consistency model; Spanner provides external consistency through TrueTime and Paxos; Aurora Global Database has one primary region for writes and promotes a secondary region on failover; DynamoDB global tables accept writes in every region and resolve conflicts by last writer wins; Cosmos DB offers five consistency levels, so the guarantee has to be chosen explicitly rather than assumed
- Wide-column: Bigtable · DynamoDB and Keyspaces · Cosmos DB for Cassandra; rows are kept in key order (Bigtable) or spread across partitions by a hash of the partition key (DynamoDB, Keyspaces, Cosmos DB for Cassandra), so key design decides hotspots; range scans over sorted keys are native in Bigtable but are not offered across partitions in DynamoDB, so the access pattern must be fixed before the key is chosen
- Document: Firestore · DynamoDB · Cosmos DB; a document is a nested record stored under a key and indexed by chosen fields; Firestore indexes every single field automatically and creates composite indexes on demand, while DynamoDB items are fetched by primary key and need indexes designed for each access pattern, so query flexibility differs by provider
- In-memory cache: Memorystore · ElastiCache · Azure Cache for Redis; an in-memory key-value store used for caching, sessions and counters, with TTLs and an eviction policy that decides what is lost when memory fills; a cache is not a system of record, so its contents must be rebuildable from the source; engine versions, cluster modes and replica options differ by product, so each is checked on its own
- Warehouse: BigQuery · Redshift · Synapse Analytics; a columnar, massively parallel store that runs SQL over large tables; BigQuery is serverless and bills by bytes scanned or by reserved capacity, Redshift is sized in nodes or serverless capacity, and Synapse dedicated pools are sized in data warehouse units, so cost planning uses different units
- Messaging: Pub/Sub · SNS and SQS · Service Bus and Event Grid; a durable queue or topic decouples producers from consumers, so a slow consumer does not block a producer; an SQS queue delivers each message to one consumer, SNS fans a message out to subscribers, Pub/Sub topics fan out to subscriptions natively, Service Bus offers queues and topics with sessions, and Event Grid pushes events to handlers, so delivery, ordering and retention guarantees must be compared before a choice
- Stream and batch processing: Dataflow · Kinesis and Glue · Stream Analytics; Dataflow runs Apache Beam pipelines that use one programming model for streaming and batch; Kinesis is a stream log for ingesting records in real time and Glue is batch ETL, so a team often pairs them; Stream Analytics runs SQL-like queries with time windows over event streams; the choice depends on whether one program must serve both modes and who operates the runtime
- Managed Spark and Hadoop: Dataproc · EMR · HDInsight; each runs open-source clusters such as Spark and Hadoop, with the team choosing versions and node counts; Dataproc also offers a serverless batch mode with no cluster to size; when a cluster is used, its sizing and patching stay with the team
- Pipeline orchestration: Cloud Composer · MWAA · Data Factory; a scheduler runs tasks in dependency order with retries, backfills and monitoring; Cloud Composer and MWAA are managed Apache Airflow, where pipelines are Python DAGs, while Data Factory defines pipelines as activities through a visual designer and JSON, so the same workflow is written differently in each
- BI: Looker · QuickSight · Power BI; each tool connects to a warehouse, defines a semantic layer or data model, and publishes dashboards and reports to users; Looker's LookML is code that defines measures once, while QuickSight and Power BI each have their own dataset and calculation model, so a metric defined in one does not carry over to another
- Virtual network: VPC · VPC · VNet; a private address space divided into subnets, with routes and firewall rules controlling traffic; a Google Cloud VPC is global with regional subnets, an AWS VPC is regional with subnets each inside one Availability Zone, and an Azure VNet is regional with subnets that span the zones of a region, so cross-region designs need different peering or hub choices on each
- Load balancing: Cloud Load Balancing · ELB · Load Balancer and Application Gateway
- CDN: Cloud CDN · CloudFront · Azure CDN and Front Door; a CDN caches content at edge locations near users so that repeat requests skip the origin; Cloud CDN is a pull cache attached to a global Application Load Balancer backend, CloudFront pulls from configured origins through distributions, and Azure Front Door combines CDN caching with global HTTP load balancing, so cache keys, TTLs and origins are configured in each product's own terms
- DNS: Cloud DNS · Route 53 · Azure DNS; authoritative zones hold record sets, and resolvers cache each answer for its TTL; Cloud DNS and Route 53 both offer routing policies that answer by weight, geography or health, while Azure DNS hosts zones and records and health-based routing is a separate Azure service, so the same failover design is built from different parts
- Hybrid connectivity: Cloud Interconnect and VPN · Direct Connect and VPN · ExpressRoute and VPN Gateway
- Identity and access: Cloud IAM · AWS IAM · Entra ID and Azure RBAC; a principal is granted roles on resources through policies; Cloud IAM and AWS IAM both evaluate policies bound to principals and resources, while Entra ID governs the directory and Azure RBAC governs Azure resources, so a permission can live in a different system from the one that shows the denial; check which system holds the permission before debugging
- Keys: Cloud KMS · AWS KMS · Key Vault; a key is managed by a service that encrypts and signs on the caller's behalf, with key material kept in tamper-resistant hardware; envelope encryption uses a key to wrap a data key, which encrypts the data; Key Vault also stores secrets and certificates, while Cloud KMS and AWS KMS manage keys only, so a secret needs a separate store
- Secrets: Secret Manager · Secrets Manager · Key Vault; versioned secret values read by IAM-authorized callers at start-up or run time, with rotation and audit logging; Secret Manager keeps versions per secret, AWS Secrets Manager adds managed rotation for supported databases, and Key Vault holds secrets, keys and certificates in one service, so where a secret lives differs by provider
- WAF and DDoS: Cloud Armor · AWS WAF and Shield · Azure WAF and DDoS Protection; rules inspect HTTP requests before they reach the origin, with managed rule sets, custom rules and rate limits, and DDoS protection absorbs volumetric attacks; Cloud Armor attaches to load balancer backends and offers OWASP Core Rule Set rules; AWS WAF attaches to CloudFront and load balancers, and Shield provides DDoS protection; Azure WAF runs on Application Gateway or Front Door
- Container registry: Artifact Registry · ECR · Azure Container Registry; images are stored by digest, access is governed by IAM, and scanning reports vulnerabilities in each image; Artifact Registry also stores language packages alongside images, so it covers more formats than images alone; the login step for pushes and pulls differs by product
- CI build: Cloud Build · CodeBuild · Azure Pipelines; a build runs its steps in an isolated environment triggered by a repository event and produces an image or artifact for a registry; each product reads its own config file (`cloudbuild.yaml`, `buildspec.yml` for CodeBuild, `azure-pipelines.yml`), so a pipeline moves across only when its commands do
- CD and release: Cloud Deploy · CodePipeline and CodeDeploy · Azure Pipelines releases
- Native IaC: Infrastructure Manager and Config Connector · CloudFormation and CDK · ARM and Bicep
- Metrics: Cloud Monitoring · CloudWatch · Azure Monitor; time series with labels or dimensions, alerting on thresholds, and dashboards; Cloud Monitoring adds SLO monitoring and alerts on log-based metrics, CloudWatch organizes metrics in namespaces with dimensions, and Azure Monitor metrics are scoped to the resource that emits them, so cardinality and naming choices carry over differently
- Logs: Cloud Logging · CloudWatch Logs · Azure Monitor Logs; centralized log storage with retention, query and export; Cloud Logging stores entries in log buckets and routes them with sinks, CloudWatch Logs organizes them into log groups and streams, and Azure Monitor Logs keeps them in a Log Analytics workspace queried with Kusto, so retention and export are set up separately in each product
- Tracing: Cloud Trace · X-Ray · Application Insights; spans carry trace and parent identifiers in request headers, so one request can be followed across services; Cloud Trace accepts OpenTelemetry export, X-Ray traces requests through AWS services and its own SDK, and Application Insights is part of Azure Monitor, so instrumentation written against OpenTelemetry moves between them more easily than vendor SDK calls
- ML platform: Gemini Enterprise Agent Platform · SageMaker · Azure Machine Learning
- Foundation models: Model Garden and Gemini · Bedrock · Azure AI Foundry; hosted models called through a managed API with quotas, regional endpoints and per-token billing; which models each provider offers, and in which regions, changes often, so the catalog must be checked in the provider's own listing before a design depends on a model
- Organization hierarchy: organization → folder → project · organization → OU → account · management group → subscription → resource group
- Organization-wide policy: Organization Policy · service control policies · Azure Policy
- SIEM and SecOps: Google SecOps · Security Hub and GuardDuty · Microsoft Sentinel and Defender

### Certifications — Google Cloud

- **Professional Cloud Architect**: designing and planning a cloud solution architecture; managing and provisioning the infrastructure; designing for security and compliance; analyzing and optimizing technical and business processes; managing implementation; ensuring solution and operations excellence
  - Case studies: Altostrat Media, Cymbal Retail, EHR Healthcare, KnightMotives Automotive
  - Migration planning: the six Rs mapped to landings; Migrate to Virtual Machines; Migration Center discovery, dependency mapping and wave planning; licence impact; Database Migration Service, Datastream, Storage Transfer Service, Transfer Appliance; wave-zero connectivity; cutover with a written rollback
- **Professional Machine Learning Engineer**: architecting low-code AI solutions; collaborating across teams to manage data and models; scaling prototypes into ML models; serving and scaling models; automating and orchestrating ML pipelines; monitoring AI solutions
- **Professional Data Engineer**: designing data processing systems; ingesting and processing data; storing data; preparing and using data for analysis; maintaining and automating data workloads
- **Professional Cloud Developer**: designing scalable, secure, reliable cloud-native applications; building and testing; configuring for deployment; integrating with Google Cloud services; generative AI APIs and AI coding assistants
- **Professional Cloud DevOps Engineer**: bootstrapping and maintaining an organization; applying SRE practices; building CI/CD pipelines (including for infrastructure and ML workloads); observability and troubleshooting; optimizing performance and cost
- **Professional Cloud Security Engineer**: configuring access; securing communications and boundary protection; data protection; managing operations; supporting compliance requirements
- **Professional Cloud Network Engineer**: designing and planning VPC networks; implementing VPCs; configuring managed network services; hybrid and multicloud interconnectivity; managing, monitoring and troubleshooting; network security (Cloud NGFW, Secure Web Proxy, VPC Service Controls, Cloud Armor)
- **Professional Cloud Database Engineer**: designing scalable, highly available database solutions; managing multi-database solutions; migrating data solutions; deploying databases on Google Cloud
- **Professional Security Operations Engineer**: platform operations; data management; threat hunting; detection engineering; incident response; observability
- **Professional Agentic Architect**: building agents with low-code tools; using coding agents for application development (MCP servers, skills, sandboxes); developing custom agents (model selection, ADK, sessions and memory, RAG and vector retrieval, agent permissions, MCP and A2A orchestration, multi-agent handoffs); evaluating and deploying agentic workflows; securing and governing agentic workflows (OAuth 2.0 tool calls, principal access boundaries)

### Certifications — AWS

- **Solutions Architect – Professional (SAP-C03)**: cloud-native architecture design and implementation; security, compliance and governance; cost-optimized architecture design; resilience, migration and business continuity; operational excellence and automation
- **Solutions Architect – Professional (SAP-C02)**: design for organizational complexity; design for new solutions; continuous improvement for existing solutions; accelerate workload migration and modernization
- **DevOps Engineer – Professional (DOP-C02)**: SDLC automation; configuration management and IaC; resilient cloud solutions; monitoring and logging; incident and event response; security and compliance
- **Generative AI Developer – Professional (AIP-C01)**: foundation model integration, data management and compliance; implementation and integration; AI safety, security and governance; operational efficiency and optimization; testing, validation and troubleshooting
- **Security – Specialty (SCS-C03)**: detection; incident response; infrastructure security; identity and access management; data protection; security foundations and governance
- **Advanced Networking – Specialty (ANS-C01)**: network design; network implementation; network management and operation; network security, compliance and governance

### Certifications — Microsoft Azure

- **Azure Administrator (AZ-104)**: identities and governance; storage; compute; virtual networking; monitoring and maintenance
- **Azure Solutions Architect Expert (AZ-305)**: identity, governance and monitoring solutions; data storage solutions; business continuity solutions; infrastructure solutions (compute, application architecture, migrations, networking)
- **DevOps Engineer Expert (AZ-400)**: processes and communications; source control strategy; build and release pipelines (packages, testing, pipelines, deployments, IaC); security and compliance plans; instrumentation strategy
- **Cybersecurity Architect Expert (SC-100)**: aligning with security best practices (ransomware resiliency, MCRA, MCSB, Zero Trust, CAF and WAF); security operations, identity and compliance; infrastructure security (posture management, endpoints, SaaS/PaaS/IaaS, Security Service Edge); application and data security (Microsoft 365, applications, data, AI workloads)
- Expert-level prerequisites: AZ-305 requires the Azure Administrator Associate; AZ-400 requires AZ-104 or AZ-204; SC-100 requires a security associate certification

### Certifications — Anthropic

- **Claude Certified Developer – Foundations (CCDV-F)**: applications and integration; model selection and optimization; agents and workflows; prompt and context engineering; tools and MCP; security and safety; Claude Code; evaluation, testing and debugging

### Exercises

- The four Professional Cloud Architect case studies, each designed with a one-line defence of every trade-off
- A zero-cost build on always-free services (Compute Engine, Cloud Run, Cloud Run functions, Cloud Storage, Firestore, Pub/Sub), provisioned entirely with `gcloud` in an idempotent shell script and torn down by the same script
- A private-IP Cloud SQL instance reached from Cloud Run with a connection budget
- Spanner, Bigtable and Firestore key designs with hotspot detection, run against the local emulators first
- A global Application Load Balancer with Cloud CDN, Cloud Armor and IAP in front of a serverless backend, built resource by resource from the command line, then expressed in Terraform
- IAP and Identity Platform in front of an admin console
- Workload Identity Federation from CI with negative tests
- A VPC Service Controls perimeter and organization policies, planned in Terraform
- A store-selection table across the system-design problems, with a managed product per component
- The same three-tier service deployed with `gcloud`, the AWS CLI and the Azure CLI, comparing identity, networking and output querying
- Multi-account AWS and multi-subscription Azure landing zones planned in Terraform
- An inventory and cost report built from `--format`, `--filter` and `--query` output piped into `jq`
- **Reasoning drills**
  - Choose a managed service for each requirement from the constraints alone, then check the provider's limits and quotas
  - Estimate quota, cost and latency for a multi-region design before building it
  - Translate a design across Google Cloud, AWS and Azure and name what does not map cleanly
  - Diagnose an IAM denial from the policy alone, then confirm it with the troubleshooter
