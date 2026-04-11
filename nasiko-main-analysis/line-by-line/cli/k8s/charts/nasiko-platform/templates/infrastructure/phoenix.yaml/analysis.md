# phoenix.yaml — line-by-line analysis

## Lines 1-8
- Defines PVC metadata for Phoenix storage and labels.

## Lines 9-16
- Sets access mode, storage request, and starts Phoenix Deployment.

## Lines 17-24
- Deployment metadata, labels, replicas, and selector.

## Lines 25-32
- Pod template labels and starts container list.

## Lines 33-40
- Phoenix container image and web/OTLP port declarations.

## Lines 41-48
- Adds OTLP ports and begins environment variable settings.

## Lines 49-56
- Sets Phoenix host and port env vars.

## Lines 57-64
- Defines resource requests/limits and volume mount.

## Lines 65-72
- Configures readiness probe for HTTP root.

## Lines 73-80
- Configures liveness probe and starts volumes section.

## Lines 81-88
- Mounts PVC and starts Service definition.

## Lines 89-96
- Service metadata, selector, and web port mapping.

## Lines 97-104
- Adds OTLP ports and sets ClusterIP service type.

## Lines 105-112
- Starts Ingress definition with metadata and annotations.

## Lines 113-120
- Defines ingress rules and host configuration.

## Lines 121-128
- Maps ingress path to phoenix-service on port 6006.

## Lines 129-136
- Starts ConfigMap metadata and labels.

## Lines 137-144
- Provides Phoenix endpoint values and tracing flags.

## Lines 145-146
- Sets injection and log level config entries.
