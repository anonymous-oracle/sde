# Part 18 · DevOps & SRE: Docker, Kubernetes, NGINX, CI/CD, Infrastructure as Code, Observability · TOPIC LIST

Rules and directives for this part: `index/part18_devops_sre.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: DevOps & SRE: Docker, Kubernetes, NGINX, CI/CD, Infrastructure as Code, Observability

### Docker

- Images versus containers; the union filesystem (overlay lower and upper layers, copy-up, whiteouts) and why deleted files persist in earlier layers
- Images as content-addressed Merkle structures: manifests, configs, layer digests; tags as mutable pointers, digests as pins
- Dockerfiles: `FROM`, `RUN`, `COPY`, `ENTRYPOINT` versus `CMD`; multi-stage builds
- Layer caching as memoization: cache keys and instruction ordering; a layer is reused when its cache key matches, where the key covers the instruction text, the parent layer and the checksums of any copied files; a changed input invalidates that layer and every layer after it, so install dependencies before copying frequently changing source; the cache is an exact memo table, so a hit returns the stored layer without rerunning the step
- Reproducible images: digest-pinned bases, fixed timestamps, stable file order; pin the base image by digest so a retagged image cannot change the build; set file timestamps to one fixed value (the SOURCE_DATE_EPOCH convention) so archives do not vary with the clock; sort archive entries because directory listing order varies between machines; pin package versions; verify by building twice and comparing digests
- Container networking modes (bridge, host, none); volumes, bind mounts and tmpfs; bridge gives a container its own network namespace behind a virtual bridge, with address translation for published ports; host shares the host's network namespace with no isolation; none leaves only a loopback interface; a volume is managed by Docker and outlives the container; a bind mount maps a host path into the container; tmpfs lives in memory and is lost when the container stops
- Docker Compose for local multi-container development; a YAML file declares services, networks and volumes; Compose puts services on a shared default network where each resolves the others by service name; depends_on orders start-up but does not wait for readiness, so a healthcheck is needed for that; Compose describes a local stack and is not a production orchestrator
- Registries, tagging strategy and image scanning; a registry stores layers and manifests by digest and maps tags to digests; a tagging strategy pairs an immutable tag such as a commit hash with deploys by digest, and does not deploy a mutable latest tag; a scan compares installed package versions against a vulnerability database, so a clean result is only as current as that database
- Container security: non-root users, minimal and distroless bases, secrets anti-patterns; the shared kernel in every container's TCB
- BuildKit daemon builds; the Docker Engine API from code; BuildKit's solver as a DAG of build steps run in parallel with a content-addressed cache, and `RUN --mount=type=secret` mounts that never enter a layer
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
  - The Borg → Omega → Kubernetes lineage; Borg, Google's internal cluster manager, used a central scheduler with priority and quota across shared machines; Omega explored several schedulers working on shared state with optimistic concurrency; Kubernetes carried over the declarative desired-state API and controllers, storing state in etcd, as an open-source system
- **Workloads**: Pods, ReplicaSets, Deployments, StatefulSets, DaemonSets, Jobs and CronJobs; init containers that run to completion one after another before the app containers start, sharing the pod's volumes and network, and restarted on failure under the pod's restart policy, used to wait for a dependency or to seed a volume
- **Networking**: Services (ClusterIP, NodePort, LoadBalancer), Ingress and Ingress controllers, the CNI model, NetworkPolicies
- **Configuration and storage**: ConfigMaps, Secrets, environment injection; PersistentVolumes, PersistentVolumeClaims, StorageClasses, dynamic provisioning
- **Scheduling and scaling**
  - Scheduling as NP-hard bin packing solved by filter-and-score; the lower bound ⌈Σ requests ÷ node capacity⌉
  - Node affinity, taints and tolerations, pod anti-affinity, topology spread constraints
  - Requests versus limits: CFS quota throttling per period; OOM kills over the memory limit
  - Horizontal and Vertical Pod Autoscalers; Cluster Autoscaler; PodDisruptionBudgets
- **Security**: RBAC, Pod Security Standards, admission controllers; RBAC grants verbs on resources to subjects through Role and RoleBinding objects, checked with `kubectl auth can-i`; Pod Security Standards define three profiles (privileged, baseline, restricted) enforced per namespace by label; admission controllers run after authentication and authorization and can validate or mutate an object before it is stored
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

- Configuration: server blocks, location matching, directives; a server block is selected by listening port and server_name; for a request path, an exact `=` match wins, then the longest prefix match, with regular-expression locations checked in file order unless a `^~` prefix stopped the search; directives such as root, proxy_pass and return set behaviour, and `nginx -t` checks the file before a reload
- Upstreams and load-balancing methods: round robin, `least_conn`, `ip_hash`; round robin rotates through servers in turn, with an optional weight per server; least_conn sends each request to the server with the fewest active connections; ip_hash pins a client address to one server by hash, which skews load when many clients share one address behind NAT; open-source NGINX marks a server unavailable for fail_timeout after max_fails failed attempts
- TLS termination, HTTP-to-HTTPS redirects, HTTP/2; terminating TLS at the proxy means backends receive plain HTTP, so the link between proxy and backend must be trusted or itself encrypted; a redirect returns 301 to the https address of the same request URI; HTTP/2 multiplexes streams over one TCP connection, which removes application-level head-of-line blocking but not TCP-level blocking
- Caching and static content; stale-while-revalidate; proxy_cache stores upstream responses in a key zone, honouring Cache-Control and Expires from the origin, and static files are served straight from disk without a backend; stale-while-revalidate lets a stale entry be served at once while one background request refreshes it, so clients do not wait on the origin during the window
- NGINX as a Kubernetes Ingress controller; an Ingress object declares host and path rules to a Service; the controller watches Ingress objects, renders them into NGINX configuration and reloads it when they change; controller-specific behaviour is set by annotations, which differ between controllers; the Gateway API is the newer model for the same routing job
- Server architectures: Flash's AMPED design; SEDA; NGINX's worker event loops; thread-per-connection blocks a thread for each waiting client; an event loop serves many connections per thread with non-blocking I/O readiness calls such as epoll or kqueue; AMPED adds a few helper processes that take blocking file reads while the event loop stays non-blocking; SEDA splits the service into stages joined by queues, each with its own thread pool and admission limit; NGINX runs one event loop per worker process
- A proxy as a queue: Little's law for upstream and client connections; Little's law L = λW says the average number of connections held equals the arrival rate times the average time each stays; at 500 requests per second with 0.2 s upstream latency, 100 connections are in flight, so a slow upstream fills the proxy's buffers and sockets first; set upstream connection limits and queue timeouts so the proxy sheds load rather than queueing without bound
- The Kong API gateway: services, routes, consumers, plugins, its Postgres store and admin API, Lua plugins; Lua basics for plugins: tables as the only compound type, closures, and a handler whose `access`, `header_filter` and `log` phases run at fixed points of each request

### CI/CD

- Pipeline stages: build → test → package → deploy; artifact repositories; a reproducible repository layout with source, lock files, build scripts and the pipeline definition committed, so a clean checkout produces the same artifact
- Deployment strategies: rolling (surge and unavailable settings), blue-green, canary; choosing from a scenario; a rollback path designed for each: `kubectl rollout undo` for a rolling Deployment, the router switched back for blue-green, and canary traffic drained to zero, with the rollback time measured in a drill
- Progressive delivery as risk control: canary fraction and the error count as a test statistic
- Continuous delivery: every commit a release candidate; each commit that passes the automated pipeline is deployable on demand, and a person or a rule chooses when it ships; this differs from continuous deployment, which ships every passing commit automatically; it needs automated tests, small changes merged to trunk often, and a pipeline that builds the same artifact for every environment
- GitOps: declarative state, Git as source of truth, reconciliation loops; Argo CD and Flux
- Tooling: GitHub Actions, Jenkins, GitLab CI; GitHub Actions runs YAML workflow definitions kept in the repository; Jenkins runs a Jenkinsfile pipeline on a controller that hands work to agents, and is usually self-hosted; GitLab CI reads a YAML pipeline definition committed in the repository and runs its jobs on runners; the three differ in hosting, plugin model and how secrets and approvals are configured
- Build-system theory: schedulers (topological, restarting, suspending) and rebuilders (dirty bits, trace checking, constructive traces); correctness and minimality; timestamp versus hash rebuilders; shared remote caches
- Pipelines as DAGs: the critical path bounds lead time; jobs are nodes and `needs` relations are edges, so jobs with no path between them run in parallel; the longest path weighted by job duration is the critical path, and lead time cannot be shorter than it, so adding parallel jobs does not shorten a chain of dependent ones; shorten lead time by splitting or caching the slowest job on that path
- Supply-chain integrity in the pipeline: reproducible builds; SLSA v1.0 Build levels L1–L3
- Platform engineering: golden-path service templates; preview environments destroyed on merge
- Database changes in deploys: expand/contract and migrations as jobs; SQL tests in CI
- Microservice deployment: each service with its own pipeline and artifact and released independently; version skew between services handled by backward-compatible APIs and events (expand/contract on the wire); rollout ordered by the dependency graph, consumers before producers for additive changes; and a rollback per service that leaves its dependencies on their current versions
- Continual learning and test in production: a production feedback loop with predictions logged and labels joined later; shadow traffic and A/B experiments with a sample size and a stop rule fixed before the run; a retraining trigger from drift metrics; and a candidate model promoted only when its offline and online evaluations both pass, with the previous model kept for rollback

### Infrastructure as code

- Declarative versus imperative provisioning; an imperative script lists steps such as create a machine then attach a disk, so a rerun after a partial failure can duplicate or miss steps; a declarative definition states the end state and the tool computes the actions to reach it from what exists; the cost is that the tool must track state and the order of actions is hidden
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
- Static IaC scanning (Checkov, tfsec, Trivy) before plan; scanners read configuration files without calling the cloud, so they run before a plan and need no credentials; they flag rules such as a public storage bucket or an open security group; they cannot see values that exist only after apply, and a suppressed finding should carry a written reason
- Policy as code evaluated over the plan; rules written in a policy language such as Rego (Open Policy Agent) or Sentinel are evaluated over the JSON from `terraform show -json` of a saved plan, returning deny messages; because the plan includes computed values, they catch cases a static scan misses; a plan that fails policy is not applied
- Immutable versus mutable infrastructure; snowflake servers; a mutable server is patched in place, so its state reflects its history; an immutable server is never changed, and a change means building a new image and replacing instances; a snowflake server is hand-configured and cannot be rebuilt from its record; immutability costs longer build pipelines and more replacement traffic
- Infrastructure testing: unit tests of a single reusable configuration with its variables and outputs checked; plan-based tests that assert on planned values without applying, as `terraform test` does with run blocks in test files; integration tests that apply to a disposable sandbox, check the live resources and destroy them, in the style of Terratest in Go; policy tests that run rules over sample plans; contract tests that pin the variables and outputs a consuming team depends on, so a breaking change fails in CI

### Observability

- Metrics, logs and traces; metrics are numeric aggregates over time, cheap to store and good for alerting; logs are discrete event records with detail, costly at volume; traces follow one request across services as spans sharing a trace ID; each answers a different question: whether something is wrong, what happened, and where the time went
- Counters, gauges and histograms; mergeable histograms versus unmergeable percentiles
- Head-based versus tail-based trace sampling and their biases; head sampling decides at the first span with a probability, which is cheap and simple but drops rare errors and slow requests it did not pick; tail sampling buffers a trace's spans until it completes and keeps errors and slow traces, but needs a collector that holds whole traces; head sampling is unbiased per trace, while tail sampling over-represents failures, so rates must be read with that in mind
- Label cardinality and its cost; high-cardinality values in logs and trace attributes
- Structured logging; each log line is a record of named fields, usually JSON, carrying fields such as time, level, service and trace ID, so queries filter on fields rather than parsing free text; field names and types are kept stable; secrets and personal data are kept out of fields; the cost is larger lines and a schema to maintain
- OpenTelemetry; Prometheus and Grafana; Jaeger; Grafana Loki; LLM-trace UIs (Phoenix); Phoenix showing each request as a trace whose spans carry model and tool calls with token counts, latency and evaluation scores; Phoenix ingesting OpenTelemetry spans over OTLP, so each model call is an instrumented span with attributes for the model, the prompt and completion token counts and the latency, and evaluators attaching scores to the trace
- Streams as infrastructure: Redis Streams consumer groups, acknowledgement after writes, pending-entry recovery, at-least-once delivery with idempotent consumers, lag as an SLI; Kafka and Redpanda clients: idempotent producers with `acks=all`, consumer-group partition assignment, offsets committed after processing, and consumer lag measured per partition; Redis Streams commands: `XREADGROUP` delivers new entries to a named consumer, `XPENDING` lists delivered but unacknowledged entries with their idle time, and `XAUTOCLAIM` moves entries left by a dead consumer to a live one; an orchestrator's build-job queue as a stream with one consumer group per job type

### Site reliability engineering

- SLIs, SLOs and SLAs; an SLI is a measured ratio of good events to valid events, such as requests answered under 300 ms over all requests; an SLO is the target for an SLI over a window, such as 99.9% over 28 days; an SLA is a contract with consequences such as service credits, set looser than the SLO so that the SLO triggers engineering action first
- Error budgets: (1 − SLO) × window; burn rate; multi-window, multi-burn-rate alerts
- Alerting as classification: precision versus recall; time to exhaustion at a burn rate; each alert linked to a runbook with its first checks, mitigation and owner, and to a dashboard showing the SLI, the burn rate and the budget left
- Composed availability of services; overload and cascading failure: retry storms that amplify load, load shedding and circuit breakers that fail fast, and metastable failure, where retries keep an outage going after its trigger has ended; a circuit breaker counts failures over a window, opens when the failure rate crosses a threshold and then fails calls fast, and after an open-state timeout admits a few trial calls in half-open that close it on success or reopen it on failure
- Toil: definition, measurement and budgeting; toil is manual, repetitive, automatable operational work tied to running a service, and it grows with load; measure it as the share of an engineer's time spent on such work, for example from tickets tagged as toil; budget it with a cap, a common one being half of working time, and when the cap is exceeded, engineering work goes to automation first
- Incident management and on-call; an incident is handled through defined roles, such as an incident commander who coordinates, a communications lead who informs stakeholders, and operations leads who act; a rotation names a primary and a secondary responder with an escalation path and a handoff note; mitigate first to restore service, then find the root cause in a review
- AIOps: correlating a trace, the alert it fired and the surrounding signals into one incident note; statistical anomaly detection and its false-positive cost; the note states its evidence and confidence, and a person confirms the cause
- Blameless postmortems; complex-system failure as multiple contributing conditions; blame treated as a signal about the system rather than the person, the timeline written from what each person knew at each moment, and every action item given an owner and a due date
- Proving reliability: load tests against the SLO; chaos experiments with an error-budget cost
- Operational readiness review (ORR): a checklist and evidence review before go-live covering monitoring, alerts and runbooks, load and capacity evidence, rollback and restore drills, failure-mode review and named owners; go or no-go decided against written criteria; a launch plan with staged exposure, a rollback criterion written before launch, a named incident lead for the first days, and a post-launch review scored against the same criteria
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
