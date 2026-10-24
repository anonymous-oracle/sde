# Part 18 · DevOps & SRE: Docker, Kubernetes, NGINX, CI/CD, Infrastructure as Code, Observability · RULES AND DIRECTIVES

Companion topic list: `index/part18_devops_sre.topics.md`. Ingest `index/00_learning_method.md` once per session, then this file, then the topic list. Mark the part done in `index/00_ingest_progress.md` before opening the next part.

Groups in this part: Docker; Kubernetes; NGINX and API gateways; CI/CD; Infrastructure as code; Observability; Site reliability engineering; Exercises.

---

# A. Standing rules: the Learning method

The full Learning method is kept **once**, in `index/00_learning_method.md`, and applies unchanged to every part. Read it at the start of a session and again after any compaction; it governs how every topic in this part is taught. It is not repeated here.

---

# B. Directives for this domain

## DevOps & SRE: Docker, Kubernetes, NGINX, CI/CD, Infrastructure as Code, Observability

**Prerequisites:** Linux (processes, namespaces, cgroups, capabilities, seccomp, file systems); networking (HTTP, TLS, load balancing, DNS); Git; Raft and replicated key-value stores; bin packing and DAGs; queueing (Little's law); percentiles and histograms; availability arithmetic.

**Depth bar:** SRE practice at the level of owning an on-call service: every component deployed from your own manifests and pipelines, every alert tied to an SLO, every failure mode drilled.

**Capstone:** a service on GKE or Cloud Run deployed by Terraform through a CI/CD pipeline with progressive delivery, SLOs with burn-rate alerts, dashboards and traces, and a game-day failure written up as a blameless postmortem.
