# Part 16 · Cloud Computing Core: Virtualization, Well-Architected, Economics & IAM · TOPIC LIST

Rules and directives for this part: `index/part16_cloud_core.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Cloud Computing Core: Virtualization, Well-Architected, Economics & IAM

### What cloud computing is

- The NIST definition: on-demand self-service, broad network access, resource pooling, rapid elasticity, measured service
- Service models: IaaS, PaaS, SaaS, and FaaS placed against the definition; IaaS rents virtual machines, disks and networks, and the customer manages the operating system and everything above it; PaaS runs the customer's code on a managed runtime, so the customer manages only the code and its data; SaaS is a finished application the customer configures; FaaS runs single functions per event, with the platform owning servers and scaling
- Deployment models: public, private, community, hybrid, multi-cloud; public means capacity shared across tenants on a provider's infrastructure; private means capacity dedicated to one organization; community means capacity shared by organizations with common requirements; hybrid joins private and public capacity, with data and workloads moved between them; multi-cloud uses more than one public provider, trading lock-in for the cost of two sets of tooling
- Resource pooling as statistical multiplexing: pooled capacity nμ + zσ√n versus n(μ + zσ); correlated demand removes the saving
- The economics of elasticity: fixed cost to variable cost; utilization-adjusted break-even; asymmetric under- and over-provisioning costs
- Serverless: compute decoupled from storage, scale to zero, per-use billing; no addressable state, cold starts, communication through storage
- Shared responsibility as a partition of controls that moves up the stack while identity and data stay with the customer

### Virtualization and containers

- Type 1 and type 2 hypervisors; how a VM works; a type 1 hypervisor runs directly on the hardware and hosts guests (Xen, VMware ESXi); a type 2 hypervisor runs as an application on a host operating system (VirtualBox); a VM presents virtual CPUs, memory, disks and network cards to a guest kernel, and privileged instructions from the guest trap to the hypervisor, which emulates them or permits them
- Popek and Goldberg's requirements and trap-and-emulate theorem; x86's failure and binary translation, paravirtualization and hardware support (VT-x, AMD-V)
- Memory virtualization: shadow page tables versus nested paging; (g + 1)(h + 1) − 1 references per nested walk; huge pages
- MicroVMs and user-space kernels (Firecracker, gVisor); a microVM is a minimal virtual machine on KVM with a small device model, so a short-lived workload gets its own kernel with a small attack surface; gVisor implements the Linux system-call interface in a user-space kernel, so most guest system calls never reach the host kernel, at the cost of call overhead and gaps in compatibility
- Containers as namespaces and cgroups; image layering and immutability; namespaces give a process its own view of process IDs, mounts, network, hostname, IPC and users; cgroups count and limit its CPU, memory and I/O; an image is stacked read-only layers with a writable layer on top for each container; immutability means a change ships as a new image rather than an edit to a running container
- Isolation classes and attack surface: process, container, sandbox, microVM, VM, dedicated host; multi-tenant systems: tenant isolation at the data layer (a tenant key on every query, or a schema or database per tenant), per-tenant limits so one noisy neighbour cannot starve the rest, and the cost of each isolation level
- OpenStack as the open-source IaaS reference: Nova, Neutron, Cinder, Swift, Glance, Keystone and Horizon

### Architecture patterns and well-architected frameworks

- High availability, fault tolerance, horizontal versus vertical scaling; high availability keeps service up by reducing downtime through redundancy and fast failover, while fault tolerance keeps operating correctly through a component failure with no visible interruption; horizontal scaling adds instances behind a load balancer and needs state kept outside them, while vertical scaling adds size to one instance and stops at the largest machine available
- Disaster recovery patterns: backup and restore, pilot light, warm standby, multi-site active-active; RTO and RPO; RTO as the longest tolerable time from the disaster to restored service, RPO as the most data loss the business accepts, measured back in time from the disaster; RPO is set by the replication lag or the backup interval, RTO by the restore and failover time, and each pattern is placed by the RTO and RPO it can meet
- Reliability mathematics: MTBF, MTTR, A = MTBF / (MTBF + MTTR); exponential failures; durability of r replicas
- k-out-of-n redundancy; common-mode failures and failure domains; a k-out-of-n system works while at least k of its n components work, so with independent failure probability q per component its reliability is the sum over i ≥ k of C(n, i)(1 − q)^i q^(n−i); common-mode failures (shared power, a bad deploy, a shared dependency) break that independence, so replicas are spread across failure domains such as racks, zones and regions
- Well-architected frameworks compared
  - Google Cloud Well-Architected Framework: operational excellence; security, privacy and compliance; reliability; cost optimization; performance optimization; sustainability; cross-pillar perspectives for AI and ML and for financial services
  - AWS Well-Architected: operational excellence, security, reliability, performance efficiency, cost optimization, sustainability
  - Azure Well-Architected: reliability, security, cost optimization, operational excellence, performance efficiency
- Pillars as quality attributes; design reviews as quality-attribute scenarios; a quality-attribute scenario names a source, a stimulus, an artifact, an environment, a response and a response measure, so each pillar is judged by a number a reviewer can check rather than by opinion, such as the recovery time after a zone failure

### Cloud economics and FinOps

- On-demand, committed-use and reserved pricing; sustained-use discounts; spot and preemptible capacity
- Commitment break-even: pays off when utilization exceeds 1 − d; with on-demand price p per hour and committed price (1 − d)p paid for every hour of the term, the commitment costs less per hour used only when the fraction of hours in use exceeds 1 − d, so a 30% discount (d = 0.3) breaks even at 70% utilization; below that, pay-as-you-go is cheaper
- Spot as expected cost (1 − d)(1 + w); checkpointing and Young's optimal interval τ ≈ √(2δM)
- Spot reclaim: the provider may stop a spot instance at short notice, after a brief warning, so work since the last checkpoint is lost and the job restarts from its last saved state; in the expected-cost formula d is the discount against on-demand and w is the fraction of work redone after interruptions, so the cost per unit of useful work is (1 − d)(1 + w) times the on-demand price, and spot is cheaper only while that product stays below one
- Total cost of ownership; marginal versus average cost; forecasting spend with confidence intervals
- Unit economics: cost per request, tenant or transaction; idle-capacity cost; cost curves that outgrow traffic as architecture defects
- Cost visibility tooling, budgets and alerts, labels and tags for allocation, billing exports
- Three budgets per system: money, errors and quota; the money budget is a spend limit with alerts on actual and forecast cost; the error budget is the share (1 − SLO) of requests allowed to fail in the window; the quota budget is the provider's cap on resources such as CPUs or addresses in a region; each is watched separately, because a cheap system can still exhaust its quota or its error budget
- Carbon as a cost-adjacent signal: region choice and footprint reports; grid carbon intensity differs by region and by hour, so moving flexible batch work to a lower-carbon region or time can cut emissions; footprint reports estimate emissions from metered usage and are estimates, not measurements; the trade-off is latency and data-residency rules, which may rule a region out
- SLAs: availability percentages as downtime per month; composite availability of serial dependencies (a product) and of redundancy; service credits; SLA versus SLO versus the customer's real loss

### Cloud IAM concepts

- Principals, roles and policies; resource hierarchies (organization, folder or OU, project or account)
- Role types: basic, predefined, custom; basic roles (owner, editor, viewer) are broad across a whole project and predate fine-grained roles, so grant them sparingly; predefined roles are bundles of permissions maintained by the provider for one product; custom roles are sets of individual permissions the organization chooses and must maintain as products change
- Policy inheritance as a union of grants; default deny; explicit deny overriding allow
- Conditional bindings and attribute-based control; a binding grants a role to a member with an optional condition expression evaluated on request attributes such as resource name, resource tags or time of day; attribute-based control decides from attributes of the caller, the resource and the environment rather than enumerating each identity; the trade-off is that conditions are harder to review than static bindings, and a mistake in one can silently widen access
- Least privilege as a minimization problem; automated policy reasoning with SMT solvers
- Deriving a minimum role set: list the API calls the workload makes, from its code paths and from the audit log over a representative period; map each call to the permission it needs; grant those through a custom role or the narrowest predefined role that covers them; then compare the granted permissions with those the audit log shows in use and remove any grant unused over the period; repeat after each release, since new code adds calls
- The safety problem: undecidable in the general access-matrix model; why restricted IAM models are analysable
- Service accounts, managed identities and attached identities; a service account is a principal for a workload, used through impersonation or a key; a managed identity is an identity the platform creates and rotates for a resource; an attached identity is bound to a compute instance and read from its metadata server, so no long-lived key sits in code; each still needs its roles limited to what the workload does
- Workload identity federation as a trust statement exchanging external OIDC tokens for short-lived credentials; workforce federation for people
- Confused deputies and capabilities; a confused deputy is a program with more authority than the requester, tricked into using that authority on the requester's behalf, for example a service writing to a target the caller named without checking the caller's own permission; the defence is to check the caller's authority, and to pass the target as a capability so the deputy never chooses it

### Resource management, edge and cloud paradigms

- **Resource management**: VM allocation and placement as bin packing; consolidation, over-commitment and live migration; cloud brokers and marketplaces; cloud federation and inter-cloud
- **Mobile cloud computing**: offloading computation from a device when saved energy and time exceed transfer cost; cloudlets
- **Fog, edge and dew computing**: the cloud–fog–edge continuum; latency, bandwidth, privacy and autonomy as drivers; dew computing as on-premises, offline-first; placement of analytics across tiers
- **Cloud and cyber-physical systems**: sensor-cloud and IoT-cloud platforms; 5G and multi-access edge computing; geo-spatial and healthcare clouds

### Exercises

- A shared-responsibility matrix per service model
- Pooled versus separate capacity computed for independent tenants
- From scratch: a cost model for on-demand, committed and spot capacity with checkpointing and interruption rates
- An RTO/RPO plan for each disaster-recovery pattern
- From scratch: an IAM policy evaluator (allow, deny, conditions, inheritance) that finds least-privilege violations and escalation paths
- **Reasoning drills**
  - Estimate a workload's monthly bill from first principles before using a pricing calculator
  - Find the minimum permissions for a task and argue that no escalation path exists
  - Name the binding constraint (cost, compliance, latency or skills) in a migration decision before comparing options
