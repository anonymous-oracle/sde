# kube-dashboard.yaml — line-by-line analysis

## Lines 1-8
- Kubernetes dashboard license header and Apache license URL.

## Lines 9-16
- License disclaimer and begins Namespace definition.

## Lines 17-24
- Namespace metadata name and starts ServiceAccount definition.

## Lines 25-32
- ServiceAccount labels/name/namespace and starts Service definition.

## Lines 33-40
- Service metadata/namespace and begins ports configuration.

## Lines 41-48
- Service port/selector for dashboard and starts cert Secret.

## Lines 49-56
- Defines kubernetes-dashboard-certs Secret metadata/type.

## Lines 57-64
- Starts csrf Secret with labels/name/namespace.

## Lines 65-72
- Defines csrf Secret type/data and starts key-holder Secret.

## Lines 73-80
- Defines key-holder Secret metadata/type.

## Lines 81-88
- Starts ConfigMap for dashboard settings.

## Lines 89-96
- Finishes ConfigMap metadata and starts Role definition.

## Lines 97-104
- Role metadata and secret access rule definition.

## Lines 105-112
- Role rules for configmaps and metrics services proxying.

## Lines 113-120
- Role rules for services/proxy and verbs.

## Lines 121-128
- Starts ClusterRole for metrics access.

## Lines 129-136
- ClusterRole rules for metrics pods/nodes and verbs.

## Lines 137-144
- Starts RoleBinding metadata and roleRef.

## Lines 145-152
- RoleBinding subject service account details.

## Lines 153-160
- Starts ClusterRoleBinding and roleRef configuration.

## Lines 161-168
- ClusterRoleBinding subject service account details.

## Lines 169-176
- Starts dashboard Deployment metadata and spec settings.

## Lines 177-184
- Deployment replica/selector and pod template labels.

## Lines 185-192
- Pod security context and container image/ports.

## Lines 193-200
- Container args for certificates/namespace.

## Lines 201-208
- Volume mounts for certs and tmp storage.

## Lines 209-216
- Liveness probe configuration for HTTPS endpoint.

## Lines 217-224
- Security context for container and starts volumes.

## Lines 225-232
- Volume definitions, service account, and node selector.

## Lines 233-240
- Tolerations for master nodes and starts metrics-scraper Service.

## Lines 241-248
- Metrics-scraper Service metadata and port/selector.

## Lines 249-256
- Starts metrics-scraper Deployment metadata.

## Lines 257-264
- Deployment spec replica/selector/template labels.

## Lines 265-272
- Pod security context and container image/ports.

## Lines 273-280
- Liveness probe HTTP settings for metrics-scraper.

## Lines 281-288
- Volume mount and container security context.

## Lines 289-296
- Service account, node selector, and tolerations.

## Lines 297-304
- Volumes definition for tmp storage.

## Lines 305-307
- End of metrics-scraper deployment.
