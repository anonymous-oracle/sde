# postgresql.yaml — line-by-line analysis

## Lines 1-8
- Defines Helm hook job to install PostgreSQL for Kong.

## Lines 9-16
- Sets hook policies, SA, restart policy, and Helm container setup.

## Lines 17-24
- Helm command installs PostgreSQL with Kong credentials.

## Lines 25-32
- Pins image registry/repo/tag and waits for install completion.
