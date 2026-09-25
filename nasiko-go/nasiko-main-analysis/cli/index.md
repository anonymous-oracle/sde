CLI and Infra Analysis
======================

Top-level CLI
-------------
main.py
- Type: Typer entrypoint
- Purpose: Register commands and groups, handle env loading, CLI callbacks.

pyproject.toml
- Type: Packaging config
- Purpose: Defines `nasiko` console script, deps (typer, requests, kubernetes, docker).

pytest.ini
- Type: Test config
- Purpose: Pytest configuration for CLI tests.

uv.lock
- Type: Dependency lock (uv)
- Purpose: Pinned dependencies; not exhaustively parsed.

pyoxidizer.bzl
- Type: Build config
- Purpose: PyOxidizer build rules for CLI binary packaging.

BINARY_BUILD_GUIDE.md
- Type: Documentation
- Purpose: Instructions for building CLI binaries (PyInstaller / PyOxidizer).

__init__.py
- Type: Package marker.

core/
------
core/__init__.py
- Package marker.

core/settings.py
- Purpose: CLI config resolution and defaults.

core/api_client.py
- Purpose: HTTP client for backend and auth endpoints (Bearer token handling).

auth/
-----
auth/__init__.py
- Package marker.

auth/auth_manager.py
- Purpose: Manage JWT storage, keyring or encrypted file fallback.

auth/auth_commands.py
- Purpose: Login/logout command helpers and validations.

utils/
------
utils/__init__.py
- Package marker.

utils/utils.py
- Purpose: Utility helpers (printing, file operations, formatting).

groups/
-------
groups/__init__.py
- Purpose: Registers CLI command groups.

groups/agent_group.py
- Purpose: Agent upload/list/get commands.

groups/github_group.py
- Purpose: GitHub OAuth and repo operations.

groups/access_group.py
- Purpose: Access control grant/revoke commands.

groups/n8n_group.py
- Purpose: N8N credential/workflow commands.

groups/search_group.py
- Purpose: Search users/agents commands.

groups/observability_group.py
- Purpose: Observability query commands.

groups/images_group.py
- Purpose: Image build/push helpers.

groups/local_group.py
- Purpose: Local Docker Compose helper commands.

groups/chat_group.py
- Purpose: Chat session create/list/history commands.

groups/user_group.py
- Purpose: Superuser and user management commands.

commands/
---------
commands/__init__.py
- Package marker.

commands/registry.py
- Purpose: Registry list/get/docs commands.

commands/n8n.py
- Purpose: N8N registration and workflow interactions.

commands/access.py
- Purpose: Access control API calls.

commands/observability.py
- Purpose: Observability API calls (sessions, traces, stats).

commands/chat_send.py
- Purpose: Send message to agent via API.

commands/search.py
- Purpose: Search endpoints for users and agents.

commands/github.py
- Purpose: GitHub OAuth + repo operations.

commands/user_management.py
- Purpose: Create/list/revoke users.

commands/upload_agent.py
- Purpose: Agent upload (zip/dir) helpers.

commands/chat_history.py
- Purpose: Chat session list/history/delete helpers.

setup/
------
setup/__init__.py
- Package marker.

setup/setup.py
- Purpose: Top-level `nasiko setup` command group and bootstrap orchestration.

setup/config.py
- Purpose: Load and validate setup configuration (env + CLI).

setup/utils.py
- Purpose: Tooling checks (terraform, kubectl, helm), helpers.

setup/terraform_state.py
- Purpose: Terraform working dir setup, backend config generation.

setup/k8s_setup.py
- Purpose: Provision clusters via Terraform and manage kubeconfig.

setup/harbor_setup.py
- Purpose: Harbor registry deployment via Helm.

setup/container_registry_setup.py
- Purpose: Configure cloud registries (ECR/DO).

setup/buildkit_setup.py
- Purpose: Deploy BuildKit resources.

setup/app_setup.py
- Purpose: Deploy core Nasiko services via Helm templates.

setup/terraform/
----------------
terraform/__init__.py
- Package marker.

terraform/aws/__init__.py
- Package marker.

terraform/aws/main.tf
- Purpose: AWS VPC + EKS module definitions.

terraform/aws/versions.tf
- Purpose: Terraform and provider version constraints.

terraform/aws/variables.tf
- Purpose: Terraform variables for AWS module.

terraform/aws/outputs.tf
- Purpose: EKS outputs (endpoint, cluster name, region).

terraform/digitalocean/__init__.py
- Package marker.

terraform/digitalocean/doks.tf
- Purpose: DigitalOcean Kubernetes cluster definition.

terraform/digitalocean/variables.tf
- Purpose: Terraform variables for DO module.

terraform/digitalocean/provider.tf
- Purpose: DigitalOcean provider configuration.

terraform/digitalocean/outputs.tf
- Purpose: DOKS outputs (endpoint, kubeconfig values).

k8s/
----
k8s/__init__.py
- Package marker.

k8s/README.md
- Purpose: K8s setup instructions for CLI users.

k8s/utils.py
- Purpose: Helper utilities for kubectl/helm operations.

k8s/agent-rbac.yaml
- Purpose: RBAC for agents or operator roles.

k8s/kube-dashboard.yaml
- Purpose: Kubernetes dashboard deployment manifest.

k8s/dashboard-admin.yaml
- Purpose: Admin role binding for dashboard.

k8s/charts/nasiko-platform/Chart.yaml
- Purpose: Helm chart metadata.

k8s/charts/nasiko-platform/values.yaml
- Purpose: Helm values (may be placeholder in this repo).

k8s/charts/nasiko-platform/environments/dev.yaml
k8s/charts/nasiko-platform/environments/staging.yaml
k8s/charts/nasiko-platform/environments/prod.yaml
- Purpose: Environment-specific overrides (placeholders unless populated).

k8s/charts/nasiko-platform/templates/_helpers.tpl
- Purpose: Helm template helpers.

RBAC templates
--------------
k8s/charts/nasiko-platform/templates/rbac/serviceaccount.yaml
k8s/charts/nasiko-platform/templates/rbac/clusterrole.yaml
k8s/charts/nasiko-platform/templates/rbac/clusterrolebinding.yaml
- Purpose: Permissions for core services and worker.

Config and secrets templates
----------------------------
k8s/charts/nasiko-platform/templates/configmaps/app-config.yaml
- Purpose: App config env values (backend, router, auth, registry).

k8s/charts/nasiko-platform/templates/secrets/registry-secret.yaml
- Purpose: Registry credentials for image pulls/pushes.

Networking templates
--------------------
k8s/charts/nasiko-platform/templates/networking/ingress.yaml
k8s/charts/nasiko-platform/templates/networking/networkpolicies.yaml
- Purpose: Ingress routing and network policies.

Initialization templates
------------------------
k8s/charts/nasiko-platform/templates/initialization/superuser-init.yaml
- Purpose: K8s job to create superuser in auth service.

Namespace
---------
k8s/charts/nasiko-platform/templates/namespace.yaml
- Purpose: Create Nasiko namespace.

Infrastructure templates
------------------------
k8s/charts/nasiko-platform/templates/infrastructure/mongodb.yaml
k8s/charts/nasiko-platform/templates/infrastructure/redis.yaml
k8s/charts/nasiko-platform/templates/infrastructure/postgresql.yaml
- Purpose: Core data services for backend and Kong.

k8s/charts/nasiko-platform/templates/infrastructure/ollama.yaml
- Purpose: Optional local LLM provider.

k8s/charts/nasiko-platform/templates/infrastructure/phoenix.yaml
- Purpose: Observability service.

BuildKit templates
------------------
k8s/charts/nasiko-platform/templates/infrastructure/buildkit/namespace.yaml
k8s/charts/nasiko-platform/templates/infrastructure/buildkit/deployment.yaml
k8s/charts/nasiko-platform/templates/infrastructure/buildkit/service.yaml
k8s/charts/nasiko-platform/templates/infrastructure/buildkit/pvc.yaml
k8s/charts/nasiko-platform/templates/infrastructure/buildkit/serviceaccount.yaml
k8s/charts/nasiko-platform/templates/infrastructure/buildkit/regcred-secret.yaml
- Purpose: BuildKit build service and credentials.

Service templates
-----------------
k8s/charts/nasiko-platform/templates/services/nasiko-backend/deployment.yaml
- Purpose: Backend API deployment and env wiring.

k8s/charts/nasiko-platform/templates/services/nasiko-web/deployment.yaml
- Purpose: Web UI deployment.

k8s/charts/nasiko-platform/templates/services/nasiko-router/deployment.yaml
- Purpose: Router service deployment.

k8s/charts/nasiko-platform/templates/services/auth-service/deployment.yaml
- Purpose: Auth service deployment.

k8s/charts/nasiko-platform/templates/services/agent-gateway/deployment.yaml
- Purpose: Kong gateway deployment.

k8s/charts/nasiko-platform/templates/services/agent-gateway/kong-migrations.yaml
- Purpose: Kong DB migrations job.

k8s/charts/nasiko-platform/templates/services/agent-gateway/kong-plugins-config.yaml
- Purpose: Plugin config (chat-logger, auth, cors).

k8s/charts/nasiko-platform/templates/services/agent-gateway/service-registry-deployment.yaml
- Purpose: Kong service registry sidecar deployment.

k8s/charts/nasiko-platform/templates/services/n8n/deployment.yaml
k8s/charts/nasiko-platform/templates/services/n8n/service.yaml
k8s/charts/nasiko-platform/templates/services/n8n/pvc.yaml
- Purpose: N8N workflow engine (optional).

k8s/charts/nasiko-platform/templates/services/nasiko-k8s-build-worker/deployment.yaml
- Purpose: K8s worker that consumes orchestration stream.
