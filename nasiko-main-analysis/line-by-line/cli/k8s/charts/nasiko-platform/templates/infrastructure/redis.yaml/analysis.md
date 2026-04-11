# redis.yaml — line-by-line analysis

## Lines 1-8
- Defines Helm hook job to install Redis via Bitnami OCI chart in nasiko.

## Lines 9-16
- Configures hook policies, SA, restart policy, and Helm container.

## Lines 17-24
- Helm command installs Redis with standalone architecture and auth disabled.

## Lines 25-27
- Waits for Helm install completion.
