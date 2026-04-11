# mongodb.yaml — line-by-line analysis

## Lines 1-8
- Defines Helm hook job to install MongoDB via Bitnami OCI chart.

## Lines 9-16
- Sets hook policies, SA, restart policy, and Helm container setup.

## Lines 17-24
- Helm command installs MongoDB with auth enabled and root password.

## Lines 25-31
- Configures resource requests/limits and waits for install.
