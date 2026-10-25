# Part 16 · Cloud Computing Core: Virtualization, Well-Architected, Economics & IAM · TOPIC LIST

Rules and directives for this part: `index/part16_cloud_core.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Cloud Computing Core: Virtualization, Well-Architected, Economics & IAM

### What cloud computing is

- The NIST definition: on-demand self-service, broad network access, resource pooling, rapid elasticity, measured service
- Service models: IaaS, PaaS, SaaS, and FaaS placed against the definition
- Deployment models: public, private, community, hybrid, multi-cloud
- Resource pooling as statistical multiplexing: pooled capacity nμ + zσ√n versus n(μ + zσ); correlated demand removes the saving
- The economics of elasticity: fixed cost to variable cost; utilization-adjusted break-even; asymmetric under- and over-provisioning costs
- Serverless: compute decoupled from storage, scale to zero, per-use billing; no addressable state, cold starts, communication through storage
- Shared responsibility as a partition of controls that moves up the stack while identity and data stay with the customer

### Virtualization and containers

- Type 1 and type 2 hypervisors; how a VM works
- Popek and Goldberg's requirements and trap-and-emulate theorem; x86's failure and binary translation, paravirtualization and hardware support (VT-x, AMD-V)
- Memory virtualization: shadow page tables versus nested paging; (g + 1)(h + 1) − 1 references per nested walk; huge pages
- MicroVMs and user-space kernels (Firecracker, gVisor)
- Containers as namespaces and cgroups; image layering and immutability
- Isolation classes and attack surface: process, container, sandbox, microVM, VM, dedicated host
- OpenStack as the open-source IaaS reference: Nova, Neutron, Cinder, Swift, Glance, Keystone and Horizon

### Architecture patterns and well-architected frameworks

- High availability, fault tolerance, horizontal versus vertical scaling
- Disaster recovery patterns: backup and restore, pilot light, warm standby, multi-site active-active; RTO and RPO
- Reliability mathematics: MTBF, MTTR, A = MTBF / (MTBF + MTTR); exponential failures; durability of r replicas
- k-out-of-n redundancy; common-mode failures and failure domains
- Well-architected frameworks compared
  - Google Cloud Well-Architected Framework: operational excellence; security, privacy and compliance; reliability; cost optimization; performance optimization; sustainability; cross-pillar perspectives for AI and ML and for financial services
  - AWS Well-Architected: operational excellence, security, reliability, performance efficiency, cost optimization, sustainability
  - Azure Well-Architected: reliability, security, cost optimization, operational excellence, performance efficiency
- Pillars as quality attributes; design reviews as quality-attribute scenarios

### Cloud economics and FinOps

- On-demand, committed-use and reserved pricing; sustained-use discounts; spot and preemptible capacity
- Commitment break-even: pays off when utilization exceeds 1 − d
- Spot as expected cost (1 − d)(1 + w); checkpointing and Young's optimal interval τ ≈ √(2δM)
- Total cost of ownership; marginal versus average cost; forecasting spend with confidence intervals
- Unit economics: cost per request, tenant or transaction; idle-capacity cost; cost curves that outgrow traffic as architecture defects
- Cost visibility tooling, budgets and alerts, labels and tags for allocation, billing exports
- Three budgets per system: money, errors and quota
- Carbon as a cost-adjacent signal: region choice and footprint reports
- SLAs: availability percentages as downtime per month; composite availability of serial dependencies (a product) and of redundancy; service credits; SLA versus SLO versus the customer's real loss

### Cloud IAM concepts

- Principals, roles and policies; resource hierarchies (organization, folder or OU, project or account)
- Role types: basic, predefined, custom
- Policy inheritance as a union of grants; default deny; explicit deny overriding allow
- Conditional bindings and attribute-based control
- Least privilege as a minimization problem; automated policy reasoning with SMT solvers
- The safety problem: undecidable in the general access-matrix model; why restricted IAM models are analysable
- Service accounts, managed identities and attached identities
- Workload identity federation as a trust statement exchanging external OIDC tokens for short-lived credentials; workforce federation for people
- Confused deputies and capabilities

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
