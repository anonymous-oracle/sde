# service-registry-deployment.yaml — line-by-line analysis

## Lines 1-8
- Defines k8s-service-registry Deployment metadata and selector.

## Lines 9-16
- Sets pod labels/spec, service account, and starts container.

## Lines 17-24
- Configures image, pull policy, and KONG/interval env vars.

## Lines 25-32
- Sets namespace env vars, port 8080, and liveness probe.

## Lines 33-40
- Configures readiness probe and begins Service definition.

## Lines 41-48
- Sets Service name/namespace and ClusterIP selector.

## Lines 49-56
- Defines service port mapping to 8080.
