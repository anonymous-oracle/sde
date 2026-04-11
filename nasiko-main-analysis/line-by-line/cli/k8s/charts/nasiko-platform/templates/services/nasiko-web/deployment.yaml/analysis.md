# deployment.yaml — line-by-line analysis

## Lines 1-8
- Defines nasiko-web Deployment metadata, namespace, selector, and replicas.

## Lines 9-16
- Sets pod labels/spec and starts web container definition.

## Lines 17-24
- Configures image, port 4000, NODE_ENV, and API/CHAT base URLs.

## Lines 25-32
- Sets router/auth/agents URLs and development flag env vars.

## Lines 33-40
- Starts Service definition with name/namespace.

## Lines 41-48
- Defines ClusterIP service selector and port mapping to 4000.

## Lines 49-49
- Sets targetPort 4000 for the service.
# deployment.yaml — line-by-line analysis

## Lines 1-8
- Defines nasiko-web Deployment metadata, namespace, selector, and replicas.

## Lines 9-16
- Sets pod labels/spec and starts web container definition.

## Lines 17-24
- Configures image, port 4000, NODE_ENV, and API/CHAT base URLs.

## Lines 25-32
- Sets router/auth/agents URLs and development flag env vars.

## Lines 33-40
- Starts Service definition with name/namespace.

## Lines 41-48
- Defines ClusterIP service selector and port mapping to 4000.

## Lines 49-49
- Sets targetPort 4000 for the service.
