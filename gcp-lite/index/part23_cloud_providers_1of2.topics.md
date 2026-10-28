# Part 23 · Cloud Providers: Google Cloud, AWS, Azure & Certifications (part 1 of 2) · TOPIC LIST

Rules and directives for this part: `index/part23_cloud_providers_1of2.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Cloud Providers: Google Cloud, AWS, Azure & Certifications (part 1 of 2)

### Google Cloud — compute

- **Compute Engine**: machine families and types; instance templates and machine images; regional managed instance groups with autohealing health checks and autoscaling; Spot VMs; sole-tenant nodes; Shielded and Confidential VMs; Container-Optimized OS; the metadata server; outbound port 25 blocked
- **Google Kubernetes Engine**: Autopilot and Standard modes; node auto-provisioning; Workload Identity; Policy Controller; Dataplane networking and NetworkPolicy; Backup for GKE; Confidential GKE nodes; Agones for game servers
- **Cloud Run**
  - Services and jobs; revisions and traffic splitting for canaries and instant rollback
  - Per-instance concurrency, minimum and maximum instances, CPU and memory limits, request timeouts
  - The container contract: listen on `PORT`; SIGTERM then a 10-second grace period; TLS terminated at the front end; HTTP/2 end to end (h2c), gRPC, WebSockets and streamed responses; no raw UDP
  - Service identity and invoker IAM; service-to-service ID tokens whose audience is the receiver URL
  - Source deploys with buildpacks; `gcloud run deploy --source` uploads the source folder, Cloud Build builds it with Google Cloud's buildpacks, which detect the language and produce a container image without a Dockerfile; a Dockerfile takes over when the team needs control over the base image or system packages
- **Cloud Run functions** (Cloud Functions) and **App Engine**: Cloud Run functions deploy one handler function in a supported language runtime, which runs as a Cloud Run service with the same invoker and identity controls; App Engine deploys a whole web application in a managed runtime, where each deployed version can be given a share of traffic for gradual rollouts
- **Eventarc**: events from many sources delivered as CloudEvents; a trigger matches events by type and attributes and routes them to a destination such as a Cloud Run service or a Workflows run; events from Google Cloud audit logs arrive through the same path; delivery is at least once, so the receiving handler must be idempotent

### Google Cloud — storage and databases

- **Cloud Storage**: strong consistency; Standard, Nearline, Coldline and Archive classes; lifecycle rules; object versioning; retention policies; signed URLs; resumable uploads; backend buckets behind Cloud CDN; public access prevention
- **Block and file**: Persistent Disk and Hyperdisk, Local SSD, snapshots; Filestore for shared NFS
- **Backup and DR Service**
- **Cloud SQL**: MySQL, PostgreSQL and SQL Server; editions; backups and point-in-time recovery; regional HA with a synchronous standby (not a read replica); same- and cross-region read replicas and their promotion; private IP; the Cloud SQL Auth Proxy and language connectors; IAM database authentication; Query Insights; database flags; maintenance windows; storage autosizing; instance count × pool size against `max_connections`
- **AlloyDB**: PostgreSQL-compatible; read pool instances; columnar engine; managed connection pooling
- **Spanner**: horizontally scaled relational database with external consistency (TrueTime, Paxos); regional and multi-region configurations; interleaved tables; split by key range and load; key design against hotspots (UUIDv4, bit-reversed sequences); stale reads (exact and bounded staleness); read-only replicas; row-deletion (TTL) policies; Spanner Graph; GoogleSQL and PostgreSQL dialects; the emulator
- **Bigtable**: HBase-compatible wide-column store; row keys sorted lexicographically; tablets; throughput scaling with nodes; multi-cluster replication with app profiles and last-write-wins; per-column-family garbage-collection policies; row-key design (no timestamp-leading keys, salting, reversed domains); Key Visualizer; the emulator
- **Firestore**: Native mode (strong consistency, ACID transactions, real-time listeners, offline SDKs, automatic single-field and on-demand composite indexes), Datastore mode, MongoDB compatibility; Standard and Enterprise editions; TTL policies; multi-region locations; no full-text search
- **Memorystore**: Valkey, Redis, Redis Cluster and Memcached; eviction policies; zonal HA replicas; cluster mode hash slots; approximate LRU
- **BigQuery**: serverless warehouse with Dremel-style execution; partitioning and clustering; nested and repeated fields; materialized and authorized views; result cache; `INFORMATION_SCHEMA` job statistics; dry-run byte estimates and cost controls; streaming inserts versus batch loads; federated queries; search indexes; BigQuery ML (CREATE MODEL to train a model in SQL where the data already lives, ML.PREDICT to score rows and ML.EVALUATE to report metrics on a held-out split, so that training data does not leave the warehouse); the sandbox
- **Choosing a store**
  - Relational single-region OLTP → Cloud SQL; high-performance PostgreSQL with mixed analytics → AlloyDB; global relational with strong consistency → Spanner
  - High-throughput time series and wide-column → Bigtable; documents and mobile sync → Firestore; caches, sessions and leaderboards → Memorystore
  - Analytics → BigQuery; blobs → Cloud Storage; shared POSIX files → Filestore
  - Anti-choices: a cache as system of record; a warehouse on the checkout path; object or file storage as a database; Bigtable for ad-hoc joins
  - Native TTL (Firestore TTL, Spanner row deletion, Bigtable GC, Cloud Storage lifecycle) over scheduled sweepers
  - Multi-writer options: Spanner multi-region, Bigtable multi-cluster routing, Firestore multi-region; Cloud SQL has no multi-primary mode and does not shard itself
  - **Multi-region serving design**: a read path served from the region nearest the user with a stated staleness bound, and a write path either with one leader region and failover or with writes accepted in every region under a conflict rule; the cost of a cross-region commit set by the round-trip time between regions, so the latency target fixes how many regions a write can span; the choice recorded as a decision with its failure mode during a regional outage

### Google Cloud — networking

- **VPC**: global VPCs with regional subnets; firewall rules and Cloud NGFW; routes and Cloud Router; Shared VPC host and service projects; VPC peering; Private Google Access; Private Service Connect; Network Connectivity Center; reserved static IPs
- **Cloud NAT** for egress with static IPs; Secure Web Proxy; Cloud NAT is configured on a Cloud Router per region and translates the private addresses of instances with no external IP into a shared set of external addresses for outbound connections only, so it accepts no unsolicited inbound traffic; Secure Web Proxy is a managed forward proxy that applies destination hostname and URL policies to egress traffic, with optional TLS inspection, and clients must be configured to send their requests through it
- **Hybrid connectivity**: Cloud VPN and HA VPN; Dedicated and Partner Interconnect
- **Cloud Load Balancing**
  - Application Load Balancers (L7): global external, regional external, internal, cross-region internal; URL maps with host and path rules; backend services; health checks; backends as MIGs and NEGs (zonal, serverless, internet)
  - Network Load Balancers (L4): proxy (TCP termination) and passthrough (preserving clients, UDP)
  - One anycast IP steering users to the nearest healthy region; HTTP/1.1, HTTP/2 and HTTP/3 to clients
  - Locality policies including ring hash and Maglev for cache affinity; ring hash places backends on a hash ring so that each key maps to a stable backend, and removing one backend remaps only the keys on its arc; Maglev builds a fixed lookup table that spreads keys almost evenly with little disruption when backends change; affinity trades even load for cache hits, so a hot key still concentrates on one backend
  - Google-managed certificates; Certificate Manager; SSL policies setting minimum TLS versions
- **Cloud DNS**: public and private zones; DNSSEC; routing policies (weighted round robin, geolocation with geofencing, failover) with health checks; DNS logging; Cloud Domains
- **Cloud CDN**: pull CDN on the global Application LB; origins as backend buckets, instance groups and external origins; cache modes (`CACHE_ALL_STATIC`, `USE_ORIGIN_HEADERS`, `FORCE_CACHE_ALL`); TTLs and cache keys; signed URLs and cookies; invalidation; serve-while-stale; GET and HEAD only
- **Media CDN** for large video and downloads; **Firebase Hosting** for static and web front ends with custom headers
- **Service Directory**; **Cloud Service Mesh** (managed Istio and Envoy) for mTLS, retries and traffic management; mesh concepts: a sidecar Envoy proxy beside each workload carrying its traffic, a control plane pushing routes and certificates to the proxies, and a workload identity per service behind each mTLS connection
- **API Gateway, Cloud Endpoints and Apigee**: OpenAPI and gRPC with transcoding; keys, quotas, analytics, spike arrest
- **Network Intelligence Center** and Connectivity Tests; Network Intelligence Center bundles network observability, including Network Analyzer insights into misconfigurations and Network Topology views of traffic; Connectivity Tests analyze a configured source and destination, trace the path a packet would take through routes, firewall rules and forwarding rules, and report the first rule that blocks it, so a reachability question can be answered from configuration alone

### Google Cloud — data and analytics

- **Pub/Sub**: topics and subscriptions; push and pull; at-least-once delivery; ordering keys; dead-letter topics; retry with exponential backoff; exactly-once delivery for pull subscriptions; message retention and seek; Avro and Protobuf schemas
- **Managed Service for Apache Kafka**
- **Cloud Tasks** (HTTP targets, per-queue rate and concurrency limits, scheduled tasks) and **Cloud Scheduler**
- **Workflows** for serverless orchestration with callbacks; **Cloud Composer** (Apache Airflow)
- **Dataflow** (Apache Beam: pipelines, `DoFn` lifecycle, windows and watermarks, streaming and batch); **Dataproc** and Dataproc Serverless (Spark, Hadoop, the Cloud Storage connector)
- **Datastream**, **Data Fusion**, **Dataplex**, **BigLake**, **Analytics Hub**: Datastream streams change data capture from operational databases into BigQuery or Cloud Storage; Data Fusion is a visual service for building ETL and data integration pipelines; Dataplex organizes data across Cloud Storage and BigQuery into governed lakes with metadata and data quality checks; BigLake gives BigQuery and open engines one access layer over files in Cloud Storage with fine-grained access control; Analytics Hub publishes and subscribes to shared datasets across organizations
- **Looker** and **Looker Studio**: Looker is an enterprise BI platform whose LookML semantic model defines each metric once for every report built on it; Looker Studio is a self-service dashboard tool that connects to many data sources for reports that business users can edit
- Log sinks into BigQuery and Log Analytics; billing export to BigQuery; a log sink filters entries by query and routes the matches to a destination, with exclusion filters that keep chosen entries out; Log Analytics runs SQL over log buckets; billing export writes detailed cost rows to a dataset, the usual basis for cost queries and dashboards

### Google Cloud — AI and ML

- **Gemini Enterprise Agent Platform** (formerly Vertex AI): Workbench, custom training with accelerators, Pipelines, Feature Store, Model Registry, Experiments, endpoints, Model Monitoring, Vizier hyperparameter tuning, AutoML, Evals (formerly the Gen AI evaluation service); distributed training as worker pools (a chief, workers and optional parameter servers) with gradient all-reduce across accelerators, submitted as a `workerPoolSpecs` list with `gcloud ai custom-jobs create --region=REGION --display-name=NAME --config=config.yaml`
- Model Garden (Gemini, Claude and open models); Agent Studio; Model Garden is a catalog where each model is listed with its terms, regions and deployment options, so a team can call a managed model API or deploy an open model to its own endpoint; Agent Studio is a visual environment for building agents, where instructions, tools and the model are set in one place
- Agent Development Kit (ADK); Agent Runtime (Agent Engine); managed sessions and Memory Bank; Agent Identity and principal access boundary policies; Agent Registry; Google Cloud MCP servers; Agents CLI
- Vector Search; Agent Retrieval (formerly Vector Search 2.0); Agent Search (formerly Vertex AI Search); RAG Engine; text-embedding models
- Claude on Google Cloud: a regional or global endpoint with the model in the URL; Application Default Credentials instead of API keys; per-region quotas; billing through the Google Cloud account
- Gemini Enterprise, Agent Designer and Customer Experience Agent Studio for low-code agents
- Pre-built AI APIs: Vision, Video Intelligence, Speech-to-Text, Natural Language, Translation, Document AI
- Model Armor for prompt and response screening; a screening configuration sets which checks run on a prompt and on a response, such as prompt-injection and jailbreak detection, harmful content and sensitive data; the screen runs before the prompt reaches the model and before the response reaches the user, so a flagged request can be blocked or logged; it reduces risk but does not replace least-privilege tool access or output validation in the application

### Google Cloud — security

- **IAM**: principals, basic, predefined and custom roles; allow and deny policies; IAM Conditions in CEL; service accounts and the `actAs` path; disabling service-account key creation; Workload Identity Federation (for example GitHub OIDC); Workforce Identity Federation; Policy Analyzer and the IAM recommender
- **Organization Policy Service**: resource-location restrictions, public access prevention, key-creation bans
- **Cloud KMS**: key rings and keys; key purposes (symmetric encryption, asymmetric signing and decryption); CMEK; key versions, disabling and scheduled destruction; Cloud HSM and Cloud EKM; envelope encryption; Tink for application-layer AEAD
- **Secret Manager**: versions, rotation, access at start-up, integration with GKE
- **Identity-Aware Proxy**: OAuth consent, the accessor role, signed headers the app must validate; IAP is not object-level authorization
- **Identity Platform**: email/password, OIDC and SAML providers, MFA factors, multi-tenancy, session policies; reCAPTCHA Enterprise
- **VPC Service Controls** perimeters against data exfiltration; a service perimeter around projects restricts the listed Google APIs, so a request from outside the perimeter is denied even with valid credentials, which limits copying data to a project the attacker controls; ingress and egress rules admit named identities or networks through; dry-run mode logs the requests a perimeter would deny before it is enforced; it complements IAM rather than replacing it, and it blocks legitimate callers that are not on the list
- **Cloud Armor**: preconfigured WAF rules based on the OWASP Core Rule Set; custom rules in CEL; rate-based rules; Adaptive Protection; edge DDoS defence
- **Binary Authorization** with attestations; **Artifact Registry** (remote repositories, vulnerability scanning, Artifact Analysis); Cloud Build provenance
- **Security Command Center** findings; Web Security Scanner; **Google SecOps** (SIEM and SOAR); Cloud IDS
- **Sensitive Data Protection**: infoTypes, inspection and de-identification (deterministic and format-preserving tokens)
- **Cloud Audit Logs**: Admin Activity and Data Access logs; sinks to protected buckets and BigQuery
- Confidential VMs, Confidential GKE nodes and Confidential Space; Assured Workloads; Certificate Manager; Cloud Asset Inventory; Compliance Reports Manager

### Google Cloud — operations, DevOps and cost

- Cloud Build (multi-stage builds, provenance, private pools); Cloud Deploy; Artifact Registry
- Infrastructure Manager and Config Connector; Infrastructure Manager runs Terraform configurations as a managed deployment that stores state and applies a plan from a deployment resource; Config Connector declares Google Cloud resources as Kubernetes custom resources that a controller reconciles continuously, so drift is corrected in the cluster; choose Terraform for whole-environment provisioning and Config Connector when the platform already runs GitOps on Kubernetes
- Cloud Monitoring (distribution metrics, SLO monitoring, alerting on log-based metrics), Cloud Logging (`jsonPayload`, severity), Cloud Trace (OpenTelemetry export), Cloud Profiler, Error Reporting, Managed Service for Prometheus, Service Health
- Cloud client libraries: one client per process; Application Default Credentials; functional options; REST and gRPC transports; page iterators; pluggable retry policies
- Cloud Billing reports, budgets and alerts, labels; the Pricing Calculator; Recommender (Active Assist); Cloud Quotas; Carbon Footprint

### Google Cloud — command line

- **Installing and configuring `gcloud`**
  - The Google Cloud CLI and its bundled tools (`gcloud`, `bq`, the legacy `gsutil`); Cloud Shell with the CLI preinstalled; `gcloud components install` and `update` (not available when installed by a system package manager)
  - `gcloud init`; `gcloud auth login` for a person versus `gcloud auth application-default login` for client libraries (Application Default Credentials); `gcloud auth list`; `gcloud auth revoke`
  - Named configurations: `gcloud config configurations create`, `activate` and `list`; `gcloud config set project`, `compute/region` and `compute/zone`; `gcloud config list`; `CLOUDSDK_CORE_PROJECT`-style environment overrides
  - Acting as a service account without keys: `--impersonate-service-account` per command or `auth/impersonate_service_account` in a configuration
  - Tokens for scripts: `gcloud auth print-access-token`; `gcloud auth print-identity-token --audiences` for calling private Cloud Run services
- **Command structure and output**
  - Grammar: `gcloud [release track] component entity operation positional --flags`; release tracks `alpha` and `beta` beside GA
  - Global flags: `--project`, `--quiet` (`-q`) for non-interactive runs, `--verbosity=debug`, `--log-http`, `--billing-project`
  - `--format` as `json`, `yaml`, `csv`, `table(name, status)` or `value(name)`, with projections and transforms; `--filter` expressions (`status=RUNNING AND zone:us-central1`); `--sort-by`, `--limit`, `--page-size`; `--uri`
  - Help: `gcloud help`, `--help`, `gcloud topic filters`, `formats` and `configurations`; `gcloud cheat-sheet`
  - Scripting: `value()` output into shell variables; `describe … --format=json` piped into `jq`; idempotent create-or-describe checks; non-zero exit codes on failure
- **Projects, APIs, billing and hierarchy**
  - `gcloud projects create`, `list` and `describe`; `gcloud resource-manager folders create`; `gcloud organizations list`
  - `gcloud services enable` and `list --enabled`; an API must be enabled in a project before its calls succeed, and a call to a disabled API fails with a service-disabled error; `gcloud services list --enabled` shows what the project has on, so it is the first check when a call fails that way; enabling can be repeated safely, while disabling can break services that depend on the API
  - `gcloud billing accounts list`; `gcloud billing projects link`; `gcloud billing budgets create` with threshold rules
- **IAM**
  - `gcloud iam service-accounts create`, `list` and `keys list`; avoiding `keys create`
  - Project bindings: `gcloud projects add-iam-policy-binding --member=serviceAccount:… --role=roles/…` with `--condition`; `remove-iam-policy-binding`; `get-iam-policy --flatten=bindings[].members --filter --format` to list who holds what
  - Resource-level bindings: `gcloud iam service-accounts add-iam-policy-binding` granting `roles/iam.serviceAccountUser` or `roles/iam.workloadIdentityUser`; the same verb on buckets, secrets, Cloud Run services and IAP
  - `gcloud iam roles create --permissions` and `describe`; `gcloud iam list-testable-permissions`
  - Workload Identity Federation: `gcloud iam workload-identity-pools create`, `providers create-oidc` with an attribute mapping and condition, `create-cred-config`
  - Auditing: `gcloud asset search-all-iam-policies`, `gcloud asset search-all-resources`; `gcloud policy-intelligence troubleshoot-policy iam`
  - Organization policies: `gcloud org-policies describe`, `set-policy` and `list`; a constraint is set on an organization, folder or project and is inherited by the resources beneath it; `describe` shows the policy for one constraint on a resource, `set-policy` applies a policy file and `list` shows the policies set on a resource; a boolean constraint enforces or does not, while a list constraint allows or denies named values
- **Compute Engine**
  - `gcloud compute instances create` with `--machine-type`, `--image-family` and `--image-project`, `--subnet`, `--no-address`, `--service-account` and `--scopes=cloud-platform`, `--metadata-from-file=startup-script=`, `--shielded-secure-boot`, `--provisioning-model=SPOT`
  - `gcloud compute instances list`, `describe`, `stop`, `start`, `delete`; `add-metadata`; `get-serial-port-output`
  - `gcloud compute ssh` with `--tunnel-through-iap`; `gcloud compute start-iap-tunnel` for other ports; OS Login
  - `gcloud compute instance-templates create`; `gcloud compute instance-groups managed create`, `set-autoscaling` and `rolling-action start-update` with `--max-surge` and `--max-unavailable`; health checks with `gcloud compute health-checks create`
  - Disks, images and snapshots: `gcloud compute disks create` and `snapshot`; `gcloud compute images create`; snapshot schedules as resource policies
- **Networking**
  - `gcloud compute networks create --subnet-mode=custom`; `gcloud compute networks subnets create --range --enable-private-ip-google-access`
  - `gcloud compute firewall-rules create` with `--direction`, `--allow`, `--source-ranges`, `--target-tags` or `--target-service-accounts`, `--priority`; `list --format=table(…)`
  - `gcloud compute routers create`; `gcloud compute routers nats create --auto-allocate-nat-external-ips --nat-all-subnet-ip-ranges`
  - `gcloud compute addresses create` (`--global` or `--region`); reserves a static IP address that stays with the project when the resource using it is replaced; `--global` is for global load balancer frontends and `--region` for regional resources; a reserved external address that no resource uses is billed, so release those that are no longer attached
  - Load balancer pieces in order: `health-checks`, `backend-services create` and `add-backend`, `url-maps create`, `ssl-certificates create --domains` (Google-managed), `target-https-proxies create`, `forwarding-rules create`; `backend-services update --enable-cdn`; serverless NEGs with `network-endpoint-groups create --network-endpoint-type=serverless`
  - `gcloud compute security-policies create` and `rules create --expression --action` for Cloud Armor
  - `gcloud dns managed-zones create` (public or `--visibility=private`); `gcloud dns record-sets create --type --ttl --rrdatas`
  - `gcloud compute vpn-gateways` and `vpn-tunnels`; `gcloud compute networks peerings create`
- **Cloud Run and serverless**
  - `gcloud run deploy` with `--image` or `--source`, `--region`, `--service-account`, `--no-allow-unauthenticated`, `--set-env-vars`, `--set-secrets=ENV=secret:latest`, `--min-instances`, `--max-instances`, `--concurrency`, `--cpu`, `--memory`, `--timeout`, `--vpc-egress`
  - Functions on Cloud Run: `gcloud run deploy --function` with `--base-image`; the older `gcloud functions deploy`
  - Canary releases: `gcloud run deploy --no-traffic --tag`; `gcloud run services update-traffic --to-revisions=REVISION=10` or `--to-latest`; `gcloud run revisions list`
  - `gcloud run services describe` and `list`; `gcloud run services logs read`; `gcloud run services add-iam-policy-binding --role=roles/run.invoker`; `gcloud run services proxy` for local testing of private services
  - Jobs: `gcloud run jobs create`, `execute --wait`, `executions list`; a job runs a container to completion instead of serving requests, with a set number of tasks that can run in parallel; each run is an execution, and `execute --wait` blocks until it ends so a script or pipeline can act on the result; a failed task is retried up to a configured limit, and a scheduler can start the job on a timetable
  - `gcloud app deploy` for App Engine; `gcloud eventarc triggers create`; `app deploy` reads the app's configuration file and creates a new version that can receive a share of traffic; `eventarc triggers create` names the event filters, the destination and the service account the trigger uses, and that account must be allowed to invoke the destination
- **Kubernetes Engine**
  - `gcloud container clusters create-auto` (Autopilot) versus `clusters create` (Standard) with `--release-channel`, `--enable-private-nodes`, `--workload-pool=PROJECT_ID.svc.id.goog`, `--enable-ip-alias`
  - `gcloud container clusters get-credentials` to write a kubeconfig context; `clusters upgrade`; `clusters resize`
  - `gcloud container node-pools create` with machine types, autoscaling bounds, Spot nodes and taints
- **Storage and databases**
  - Cloud Storage: `gcloud storage buckets create gs://bucket --location --uniform-bucket-level-access --public-access-prevention`; `gcloud storage cp` (`--recursive`), `mv`, `rm`, `ls`, `cat`, `du`; `gcloud storage rsync --recursive --delete-unmatched-destination-objects --dry-run`; `gcloud storage buckets update` for versioning, lifecycle files and default storage class; `gcloud storage objects update --storage-class`; `gcloud storage sign-url --duration`; `gcloud storage buckets add-iam-policy-binding`; `gcloud storage restore` for soft-deleted objects
  - Legacy `gsutil` equivalents (`gsutil -m cp`, `gsutil rsync`, `gsutil signurl`) recognized in older scripts
  - Cloud SQL: `gcloud sql instances create --database-version=POSTGRES_… --tier --region --availability-type=REGIONAL --no-assign-ip --network`; `gcloud sql databases create`; `gcloud sql users create`; `gcloud sql instances patch`; `gcloud sql backups create` and `list`; `gcloud sql instances clone --point-in-time`; `gcloud sql instances promote-replica`; `gcloud sql connect`
  - Spanner: `gcloud spanner instances create --config --processing-units`; `gcloud spanner databases create --ddl` and `execute-sql`
  - Bigtable: `gcloud bigtable instances create`; the `cbt` tool (`cbt createtable`, `createfamily`, `set`, `read`, `count`) with a `.cbtrc`
  - Firestore: `gcloud firestore databases create --location`; `gcloud firestore indexes composite create`; `gcloud firestore export` and `import`
  - Memorystore: `gcloud redis instances create --tier --size`; `gcloud redis instances describe` and `delete`; then with `redis-cli` against the instance's host, `SET key value EX seconds`, `GET` and `TTL`, with a cache-aside read that refills on a miss
  - Local emulators: `gcloud emulators firestore start` and `gcloud emulators spanner start`; `gcloud beta emulators pubsub start` and `bigtable start`; `env-init` for client environment variables
- **BigQuery with `bq`**
  - `bq mk --dataset --location`; `bq mk --table` with a schema, `--time_partitioning_field`, `--clustering_fields` and expiration
  - `bq load --source_format=CSV` or `NEWLINE_DELIMITED_JSON`, `PARQUET` and `AVRO` with `--autodetect` or an explicit schema; `--replace`
  - `bq query --use_legacy_sql=false` with `--dry_run` for byte estimates, `--maximum_bytes_billed` as a guard, `--parameter` for parameterized queries and `--destination_table`
  - `bq ls`, `bq show --schema --format=prettyjson`, `bq head`, `bq cp`, `bq extract --destination_format`, `bq update`, `bq rm -r -f`; `bq ls -j` and `bq show -j` for jobs
- **Messaging, scheduling and pipelines**
  - Pub/Sub: `gcloud pubsub topics create` and `publish --message --attribute`; `gcloud pubsub subscriptions create` with `--ack-deadline`, `--push-endpoint`, `--dead-letter-topic`, `--max-delivery-attempts`, `--enable-message-ordering`, `--enable-exactly-once-delivery`; `subscriptions pull --auto-ack --limit`; `subscriptions seek --time`
  - `gcloud scheduler jobs create http --schedule --uri --oidc-service-account-email`; `gcloud tasks queues create --max-dispatches-per-second --max-concurrent-dispatches`; `gcloud tasks create-http-task`
  - `gcloud workflows deploy --source` and `run`; `gcloud dataflow jobs run`, `list` and `cancel`; `gcloud dataproc clusters create` and `jobs submit`; `gcloud dataproc batches submit pyspark`; `gcloud composer environments run`
- **Security services**
  - Secret Manager: `gcloud secrets create --replication-policy`; `gcloud secrets versions add --data-file=-`; `gcloud secrets versions access latest`; `versions disable` and `destroy`
  - Cloud KMS: `gcloud kms keyrings create`; `gcloud kms keys create --purpose=encryption --rotation-period --next-rotation-time`; `gcloud kms encrypt` and `decrypt` with `--plaintext-file` and `--ciphertext-file`; `gcloud kms keys versions destroy`
  - `gcloud access-context-manager perimeters create` and `dry-run` for VPC Service Controls; `gcloud iap web add-iam-policy-binding`
- **Build, deploy and artifacts**
  - `gcloud artifacts repositories create --repository-format=docker --location`; `gcloud auth configure-docker REGION-docker.pkg.dev`; `gcloud artifacts docker images list` and `describe` with vulnerability findings
  - `gcloud builds submit --tag` or `--config=cloudbuild.yaml` with `--substitutions`; `gcloud builds triggers create github`; `gcloud builds log --stream`
  - `gcloud deploy apply --file=clouddeploy.yaml`; `gcloud deploy releases create`; `gcloud deploy releases promote`; `gcloud deploy rollouts approve`
  - `gcloud infra-manager deployments apply` for Terraform through Infrastructure Manager
- **Operations**
  - `gcloud logging read` with a filter (`resource.type`, `severity>=ERROR`, `jsonPayload.field`), `--freshness`, `--limit` and `--format`; `gcloud logging sinks create` to BigQuery, Cloud Storage or Pub/Sub with exclusions; `gcloud logging metrics create`
  - `gcloud monitoring policies create --policy-from-file`; `gcloud monitoring dashboards create`; `gcloud monitoring uptime create`
  - `gcloud compute operations list` and `gcloud container operations wait` for long-running operations; a long-running call returns an operation resource with a name, a done field that becomes true when the work ends, an error field if it failed and a response field carrying the result; poll the operation with exponential backoff and a cap rather than in a tight loop, or use `gcloud compute operations wait` or `gcloud container operations wait` to block until it is done in a script
- **AI services**: `gcloud ai models upload`; `gcloud ai endpoints create`, `deploy-model` and `predict`; `gcloud ai custom-jobs create`; `gcloud ai indexes` and `index-endpoints` for Vector Search; `gcloud ai model-garden`
