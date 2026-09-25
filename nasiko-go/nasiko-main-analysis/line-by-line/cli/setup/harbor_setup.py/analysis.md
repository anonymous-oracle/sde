# harbor_setup.py — line-by-line analysis

## Lines 1-8
- Imports stdlib, subprocess, typer, Kubernetes client/config, and Rich helpers.

## Lines 9-16
- Defines Typer app/console and starts CHARTS config for ingress-nginx.

## Lines 17-24
- Specifies ingress-nginx chart metadata and LoadBalancer values.

## Lines 25-32
- Closes ingress chart and begins cert-manager chart config.

## Lines 33-40
- Finishes cert-manager settings and starts harbor chart config.

## Lines 41-48
- Completes CHARTS dict and starts run_helm helper definition.

## Lines 49-56
- Ensures helm availability, builds command, and opens progress spinner.

## Lines 57-64
- Runs helm command, updates spinner, returns stdout on success.

## Lines 65-72
- Handles helm error, prints stderr, exits; starts add_repos.

## Lines 73-80
- Iterates charts, adds repos, and updates repo cache.

## Lines 81-88
- Begins deploy_chart: fetches chart config and merges values.

## Lines 89-96
- Flattens values into --set args and builds helm upgrade command.

## Lines 97-104
- Adds namespace/version/wait flags and runs helm command.

## Lines 105-112
- Defines flatten_dict recursion helper for nested values.

## Lines 113-120
- Handles dict recursion and returns flattened mapping.

## Lines 121-128
- Starts get_ingress_ip, loads kube config, handles failures.

## Lines 129-136
- Sets namespace/service and begins status polling loop.

## Lines 137-144
- Reads service status and returns IP/hostname when assigned.

## Lines 145-152
- Sleeps between retries and returns pending message; starts ClusterIssuer.

## Lines 153-160
- Builds ClusterIssuer YAML manifest header for cert-manager.

## Lines 161-168
- Completes ACME solver configuration and starts kubectl apply.

## Lines 169-176
- Pipes manifest to kubectl and captures stdout/stderr.

## Lines 177-184
- Reports ClusterIssuer creation success/failure and defines deploy command.

## Lines 185-192
- Defines deploy CLI options and docstring.

## Lines 193-200
- Adds repos and begins deploying ingress/infra charts.

## Lines 201-208
- Deploys ingress and cert-manager, starts harbor deployment section.

## Lines 209-216
- Builds base Harbor values with admin credentials.

## Lines 217-224
- For domain mode, sets ingress/TLS and annotation values.

## Lines 225-232
- Continues ingress configuration and TLS secret reference.

## Lines 233-240
- Sets external URL for domain mode or begins local NodePort config.

## Lines 241-248
- Defines NodePort ports and TLS disablement for local mode.

## Lines 249-256
- Sets registry NodePort/externalURL and deploys Harbor chart.

## Lines 257-264
- For local mode, starts creation of registry NodePort service.

## Lines 265-272
- Runs kubectl expose command for harbor-registry service.

## Lines 273-280
- Patches service to fixed NodePort and handles errors.

## Lines 281-288
- Logs NodePort creation success or warns on failure.

## Lines 289-296
- Prints manual guidance and branches to domain finalization.

## Lines 297-304
- Creates ClusterIssuer and retrieves ingress IP for domain setup.

## Lines 305-312
- Prints external DNS/access instructions for domain mode.

## Lines 313-320
- Prints local access info (ports/credentials) for local mode.

## Lines 321-328
- Ends deploy function output and returns.

## Lines 329-332
- __main__ guard runs the Typer app.
