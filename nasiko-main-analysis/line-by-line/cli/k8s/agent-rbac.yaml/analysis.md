# agent-rbac.yaml — line-by-line analysis

## Lines 1-8
- Creates nasiko-agents namespace and begins Role definition.

## Lines 9-16
- Defines agent-manager role metadata and rules start.

## Lines 17-24
- Grants job and deployment permissions for builds and deployments.

## Lines 25-32
- Grants service permissions for agent services.

## Lines 33-40
- Grants pod/log access and configmap/secret permissions.

## Lines 41-48
- Starts RoleBinding tying role to nasiko-backend-sa.

## Lines 49-56
- Defines roleRef and subject service account details.

## Lines 57-58
- (No additional code; file ends after RoleBinding.)
