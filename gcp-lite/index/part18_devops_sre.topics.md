# Part 18 · DevOps & SRE: Docker, Kubernetes, NGINX, CI/CD, Infrastructure as Code, Observability · TOPIC LIST

Rules and directives for this part: `index/part18_devops_sre.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: DevOps & SRE: Docker, Kubernetes, NGINX, CI/CD, Infrastructure as Code, Observability

### Docker

- Images versus containers; the union filesystem (overlay lower and upper layers, copy-up, whiteouts) and why deleted files persist in earlier layers
- Images as content-addressed Merkle structures: manifests, configs, layer digests; tags as mutable pointers, digests as pins
- Dockerfiles: `FROM`, `RUN`, `COPY`, `ENTRYPOINT` versus `CMD`; multi-stage builds
- Layer caching as memoization: cache keys and instruction ordering
- Reproducible images: digest-pinned bases, fixed timestamps, stable file order
- Container networking modes (bridge, host, none); volumes, bind mounts and tmpfs
- Docker Compose for local multi-container development
- Registries, tagging strategy and image scanning
- Container security: non-root users, minimal and distroless bases, secrets anti-patterns; the shared kernel in every container's TCB
- BuildKit daemon builds; the Docker Engine API from code
- **The Docker command line**
  - Building: `docker build -t name:tag -f Dockerfile --target stage --build-arg KEY=value .`; `docker buildx build --platform linux/amd64,linux/arm64 --push`; build secrets with `--secret`; cache import and export with `--cache-from` and `--cache-to`
  - Running: `docker run -d --rm --name -p host:container -e KEY=value --env-file -v volume:/path --mount --network --memory --cpus --read-only --user --cap-drop ALL`
  - Inspecting: `docker ps -a`, `docker logs -f`, `docker exec -it container sh`, `docker inspect` with `--format` Go templates, `docker stats`, `docker top`, `docker history`, `docker image ls`, `docker system df`
  - Distributing: `docker login`, `docker tag`, `docker push`, `docker pull` by digest (`image@sha256:…`), `docker buildx imagetools inspect` for multi-platform manifests
  - Cleaning up: `docker stop`, `docker rm`, `docker image prune`, `docker system prune`; `docker network create` and `ls`; `docker volume create` and `ls`
  - Compose: `docker compose up -d --build`, `docker compose ps`, `docker compose logs -f service`, `docker compose exec`, `docker compose down -v`; profiles and override files

### Kubernetes

- **Architecture**
  - Control plane: API server, etcd, scheduler, controller manager; worker nodes: kubelet, kube-proxy, container runtime
  - etcd replicated by Raft: 2f + 1 members tolerate f failures; revision history, compaction and re-listing
  - Level-triggered reconciliation (observe, diff, act) versus edge-triggered handlers
  - The Borg → Omega → Kubernetes lineage
- **Workloads**: Pods, ReplicaSets, Deployments, StatefulSets, DaemonSets, Jobs and CronJobs
- **Networking**: Services (ClusterIP, NodePort, LoadBalancer), Ingress and Ingress controllers, the CNI model, NetworkPolicies
- **Configuration and storage**: ConfigMaps, Secrets, environment injection; PersistentVolumes, PersistentVolumeClaims, StorageClasses, dynamic provisioning
- **Scheduling and scaling**
  - Scheduling as NP-hard bin packing solved by filter-and-score; the lower bound ⌈Σ requests ÷ node capacity⌉
  - Node affinity, taints and tolerations, pod anti-affinity, topology spread constraints
  - Requests versus limits: CFS quota throttling per period; OOM kills over the memory limit
  - Horizontal and Vertical Pod Autoscalers; Cluster Autoscaler; PodDisruptionBudgets
- **Security**: RBAC, Pod Security Standards, admission controllers
- **Extending**: Helm charts, templating and releases; CustomResourceDefinitions and Operators
- **The kubectl command line**
  - Contexts and namespaces: `kubectl config get-contexts`, `kubectl config use-context`, `kubectl config set-context --current --namespace`; the kubeconfig file
  - Reading: `kubectl get` with `-o wide`, `-o yaml`, `-o json`, `-o jsonpath` and `custom-columns`, `-l` label selectors, `-A` for all namespaces, `--watch`; `kubectl describe`; `kubectl get events --sort-by=.lastTimestamp`; `kubectl explain`; `kubectl api-resources`
  - Changing: `kubectl apply -f` and `-k` (Kustomize); `kubectl diff -f`; `kubectl create deployment --dry-run=client -o yaml` to generate manifests; `kubectl expose`; `kubectl delete`; `kubectl label`, `annotate` and `patch`
  - Rollouts and scaling: `kubectl rollout status`, `history`, `undo` and `restart`; `kubectl set image`; `kubectl scale --replicas`; `kubectl autoscale`
  - Debugging: `kubectl logs -f -c container --previous`; `kubectl exec -it pod -- sh`; `kubectl port-forward svc/name 8080:80`; `kubectl debug` with ephemeral containers; `kubectl cp`; `kubectl top pods` and `nodes`
  - Nodes and access: `kubectl cordon`, `kubectl drain --ignore-daemonsets`, `kubectl uncordon`, `kubectl taint`; `kubectl auth can-i --as`
- **The Helm command line**: `helm repo add` and `update`; `helm search repo`; `helm show values`; `helm install` and `helm upgrade --install` with `-f values.yaml`, `--set`, `--atomic` and `--wait`; `helm template` and `helm lint`; `helm list`, `helm history`, `helm rollback`, `helm uninstall`; `helm create`, `helm package`, `helm dependency update`
- **Managed Kubernetes**: provider-run control planes; fully managed versus self-managed node modes; node auto-provisioning; cloud identity for pods; DigitalOcean Kubernetes

### NGINX and API gateways

- Configuration: server blocks, location matching, directives
- Upstreams and load-balancing methods: round robin, `least_conn`, `ip_hash`
- TLS termination, HTTP-to-HTTPS redirects, HTTP/2
- Caching and static content; stale-while-revalidate
- NGINX as a Kubernetes Ingress controller
- Server architectures: Flash's AMPED design; SEDA; NGINX's worker event loops
- A proxy as a queue: Little's law for upstream and client connections
- The Kong API gateway: services, routes, consumers, plugins, its Postgres store and admin API, Lua plugins

### CI/CD

- Pipeline stages: build → test → package → deploy; artifact repositories
- Deployment strategies: rolling (surge and unavailable settings), blue-green, canary; choosing from a scenario
- Progressive delivery as risk control: canary fraction and the error count as a test statistic
- Continuous delivery: every commit a release candidate
- GitOps: declarative state, Git as source of truth, reconciliation loops; Argo CD and Flux
- Tooling: GitHub Actions, Jenkins, GitLab CI
- Build-system theory: schedulers (topological, restarting, suspending) and rebuilders (dirty bits, trace checking, constructive traces); correctness and minimality; timestamp versus hash rebuilders; shared remote caches
- Pipelines as DAGs: the critical path bounds lead time
- Supply-chain integrity in the pipeline: reproducible builds; SLSA v1.0 Build levels L1–L3
- Platform engineering: golden-path service templates; preview environments destroyed on merge
- Database changes in deploys: expand/contract and migrations as jobs; SQL tests in CI

### Infrastructure as code

- Declarative versus imperative provisioning
- Declarative convergence: plan as diff(desired, observed); idempotent and convergent applies; convergent operators and promise theory
- Plans as graph walks: topological creation, reverse destruction, parallelism, cycles as errors
- State files: mapping addresses to real IDs; drift; locking against lost updates; remote state
- Terraform: providers, resources, data sources, variables and outputs, modules, workspaces, `count` and `for_each`, references and `depends_on`; `import` and `moved` blocks; the dependency lock file
- **The Terraform command line**
  - `terraform init` with `-backend-config` and `-upgrade`; `terraform fmt -recursive`; `terraform validate`
  - `terraform plan -out=tfplan` with `-var` and `-var-file`; `terraform show -json tfplan` for policy checks; `terraform apply tfplan`; `terraform destroy`
  - `-replace` to recreate one resource; `-refresh-only` to reconcile drift into state; `-target` as an emergency tool only
  - State: `terraform state list`, `show`, `mv` and `rm`; `terraform import`; `terraform force-unlock`
  - `terraform output -json`; `terraform workspace new` and `select`; `terraform providers lock`; `terraform console`; `terraform graph`
- Static IaC scanning (Checkov, tfsec, Trivy) before plan
- Policy as code evaluated over the plan
- Immutable versus mutable infrastructure; snowflake servers

### Observability

- Metrics, logs and traces
- Counters, gauges and histograms; mergeable histograms versus unmergeable percentiles
- Head-based versus tail-based trace sampling and their biases
- Label cardinality and its cost; high-cardinality values in logs and trace attributes
- Structured logging
- OpenTelemetry; Prometheus and Grafana; Jaeger; Grafana Loki; LLM-trace UIs (Phoenix)
- Streams as infrastructure: Redis Streams consumer groups, acknowledgement after writes, pending-entry recovery, at-least-once delivery with idempotent consumers, lag as an SLI

### Site reliability engineering

- SLIs, SLOs and SLAs
- Error budgets: (1 − SLO) × window; burn rate; multi-window, multi-burn-rate alerts
- Alerting as classification: precision versus recall; time to exhaustion at a burn rate
- Composed availability of services
- Toil: definition, measurement and budgeting
- Incident management and on-call
- Blameless postmortems; complex-system failure as multiple contributing conditions
- Proving reliability: load tests against the SLO; chaos experiments with an error-budget cost
- Public postmortems as case studies: Knight Capital (2012), GitLab.com database deletion (2017), Amazon S3 us-east-1 (2017), Cloudflare regex CPU exhaustion (2019), Facebook backbone and BGP withdrawal (2021), CrowdStrike content update (2024), Google Cloud Service Control policy replication (2025), Moffatt v. Air Canada chatbot liability (2024)
- Open-source systems as architecture specimens, with their constraints and trade-offs: Kubernetes, Envoy, Kong, NGINX, etcd, Redis, Kafka and Redpanda, Temporal, CockroachDB, PostgreSQL, Prometheus, Loki, Jaeger, OpenTelemetry, MinIO

### Exercises

- From scratch: a container runtime toy using namespaces, a cgroup and an overlay root filesystem
- From scratch: an image-layer builder producing content-addressed tarballs and a manifest
- From scratch: a reconciliation-loop controller over a fake API that converges after injected failures
- From scratch: a pod scheduler placing a generated workload, measured against the node-count lower bound
- From scratch: a DAG build runner with content-hash caching; a plan-and-apply engine that diffs desired against observed state with topological creation and reverse destruction
- From scratch: a Prometheus-format metrics exporter with counters, gauges and mergeable histograms; a multi-window burn-rate alert evaluator
- A multi-stage, reproducible container image with a digest-pinned base
- A Kubernetes deployment with probes, autoscaling, spread constraints and a disruption budget; CPU throttling observed at a limit
- An NGINX reverse proxy and Ingress with TLS, caching and upstream balancing
- A hand-written CI script, then a hosted pipeline with canary deployment and GitOps reconciliation
- Terraform for a multi-tier architecture, checked with `plan`, scanned and policy-checked
- OpenTelemetry instrumentation with sampled traces, histograms and structured logs
- SLOs with burn-rate alerts, a load test and a chaos experiment with its postmortem
- **Reasoning drills**
  - Predict pod placement, throttling and OOM kills from requests and limits before applying them
  - Compute the error budget and burn-rate thresholds for an SLO and justify the alert windows
  - Diagnose an incident from metrics, logs and traces with a written hypothesis per step
  - Predict image size and rebuild time from layer order, then rebuild and compare
