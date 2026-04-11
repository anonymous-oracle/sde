# deployment.yaml — line-by-line analysis

## Lines 1-8
- Defines nasiko-router Deployment metadata, namespace, selector, replicas.

## Lines 9-16
- Sets pod labels/spec and starts router container definition.

## Lines 17-24
- Configures image, port 8000, and OLLAMA/NASIKO_BACKEND env vars.

## Lines 25-32
- Sets OpenAI/OpenRouter env vars and resource requests.

## Lines 33-40
- Sets resource limits and liveness probe for /router/health.

## Lines 41-48
- Defines readiness probe and begins Service definition.

## Lines 49-56
- Service metadata, selector, and port definition start.

## Lines 57-62
- Completes service port mapping to 8000.
