# ollama.yaml — line-by-line analysis

## Lines 1-8
- Defines ollama Deployment metadata, namespace, selector, replicas.

## Lines 9-16
- Sets pod labels/spec and starts ollama container.

## Lines 17-24
- Configures image, port, and resource requests.

## Lines 25-32
- Sets resource limits and OLLAMA_HOST env var.

## Lines 33-40
- Defines liveness and readiness probes for /api/tags.

## Lines 41-48
- Starts Service definition with name/namespace and ClusterIP.

## Lines 49-56
- Defines service selector and port mapping to 11434.
