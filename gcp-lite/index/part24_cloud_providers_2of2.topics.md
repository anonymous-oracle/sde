# Part 24 · Cloud Providers: Google Cloud, AWS, Azure & Certifications (part 2 of 2) · TOPIC LIST

Rules and directives for this part: `index/part24_cloud_providers_2of2.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Cloud Providers: Google Cloud, AWS, Azure & Certifications (part 2 of 2)

### Google Cloud — mapping system-design components

- DNS → Cloud DNS; CDN → Cloud CDN or Media CDN; load balancer → Cloud Load Balancing; reverse proxy → the global Application LB, NGINX on Compute Engine or GKE, or Cloud Run's front end
- Application servers → Cloud Run, GKE, MIGs, App Engine; workers → Cloud Run jobs, GKE, Cloud Run functions
- Object store → Cloud Storage; SQL with replicas → Cloud SQL, AlloyDB, Spanner; wide-column → Bigtable; documents → Firestore; cache → Memorystore
- Message queue → Pub/Sub or Managed Kafka; task queue and scheduler → Cloud Tasks and Cloud Scheduler; warehouse → BigQuery; batch → Dataflow, Dataproc, BigQuery SQL
- Search → Elasticsearch or OpenSearch on GKE, Elastic Cloud, Agent Search
- Service discovery → Service Directory, GKE DNS, Cloud Service Mesh; autoscaling → MIG autoscaler, Cloud Run, GKE autoscalers
- Monitoring → Cloud Monitoring, Logging, Trace, Error Reporting; push notifications → Pub/Sub, Cloud Run and Firebase Cloud Messaging; email through a partner relay
- Secrets → Secret Manager and Cloud KMS; WAF and DDoS → Cloud Armor; private networking → VPC, firewall rules, Cloud NAT, Private Google Access, IAP
- Paper systems to products: MapReduce → Dataflow and Dataproc; Spark → Dataproc; Storm → Dataflow streaming; Bigtable and HBase → Bigtable; Cassandra → Bigtable; Dynamo → Firestore, Bigtable or Spanner; MongoDB → Firestore with MongoDB compatibility or Atlas; Memcached and Redis → Memorystore; GFS → Colossus beneath Cloud Storage; HDFS → Cloud Storage; Dapper → Cloud Trace; Kafka → Pub/Sub or Managed Kafka; Chubby and ZooKeeper → no managed equivalent (etcd behind the GKE API server)

### AWS

- Compute: EC2, Lambda, ECS and EKS (managed node groups, IRSA) with Fargate, App Runner, Elastic Beanstalk
- Storage and databases: S3, EBS, RDS, Aurora and Aurora Global Database, DynamoDB, Keyspaces, ElastiCache
- Networking: VPC, ELB (ALB, NLB, GWLB), Route 53, CloudFront, Direct Connect, Transit Gateway, Site-to-Site VPN
- Data: Kinesis, Glue, Redshift, EMR, MWAA, QuickSight
- AI and ML: SageMaker, Bedrock
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
- Data: Synapse Analytics, Data Factory, Stream Analytics, HDInsight, Power BI
- AI and ML: Azure Machine Learning, Azure AI Foundry
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
  - Data: `az sql server create` and `az sql db create`; `az cosmosdb create`
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

- Virtual machines: Compute Engine · EC2 · Virtual Machines
- Managed Kubernetes: GKE · EKS · AKS
- Serverless containers: Cloud Run · App Runner and Fargate · Container Apps
- Functions: Cloud Run functions · Lambda · Azure Functions
- PaaS hosting: App Engine · Elastic Beanstalk · App Service
- Object storage: Cloud Storage · S3 · Blob Storage
- Block storage: Persistent Disk · EBS · Managed Disks
- Managed relational: Cloud SQL · RDS · Azure SQL Database
- Globally distributed database: Spanner · Aurora Global and DynamoDB · Cosmos DB
- Wide-column: Bigtable · DynamoDB and Keyspaces · Cosmos DB for Cassandra
- Document: Firestore · DynamoDB · Cosmos DB
- In-memory cache: Memorystore · ElastiCache · Azure Cache for Redis
- Warehouse: BigQuery · Redshift · Synapse Analytics
- Messaging: Pub/Sub · SNS and SQS · Service Bus and Event Grid
- Stream and batch processing: Dataflow · Kinesis and Glue · Stream Analytics
- Managed Spark and Hadoop: Dataproc · EMR · HDInsight
- Pipeline orchestration: Cloud Composer · MWAA · Data Factory
- BI: Looker · QuickSight · Power BI
- Virtual network: VPC · VPC · VNet
- Load balancing: Cloud Load Balancing · ELB · Load Balancer and Application Gateway
- CDN: Cloud CDN · CloudFront · Azure CDN and Front Door
- DNS: Cloud DNS · Route 53 · Azure DNS
- Hybrid connectivity: Cloud Interconnect and VPN · Direct Connect and VPN · ExpressRoute and VPN Gateway
- Identity and access: Cloud IAM · AWS IAM · Entra ID and Azure RBAC
- Keys: Cloud KMS · AWS KMS · Key Vault
- Secrets: Secret Manager · Secrets Manager · Key Vault
- WAF and DDoS: Cloud Armor · AWS WAF and Shield · Azure WAF and DDoS Protection
- Container registry: Artifact Registry · ECR · Azure Container Registry
- CI build: Cloud Build · CodeBuild · Azure Pipelines
- CD and release: Cloud Deploy · CodePipeline and CodeDeploy · Azure Pipelines releases
- Native IaC: Infrastructure Manager and Config Connector · CloudFormation and CDK · ARM and Bicep
- Metrics: Cloud Monitoring · CloudWatch · Azure Monitor
- Logs: Cloud Logging · CloudWatch Logs · Azure Monitor Logs
- Tracing: Cloud Trace · X-Ray · Application Insights
- ML platform: Gemini Enterprise Agent Platform · SageMaker · Azure Machine Learning
- Foundation models: Model Garden and Gemini · Bedrock · Azure AI Foundry
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
