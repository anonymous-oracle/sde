# deployment.yaml — line-by-line analysis

## Lines 1-8
- Defines nasiko-backend Deployment metadata, namespace, selector, replicas.

## Lines 9-16
- Sets pod labels/spec, serviceAccountName, and starts backend container.

## Lines 17-24
- Configures image, port 8000, Mongo user/password env vars.

## Lines 25-32
- Sets Mongo host/port/db and Redis host env vars.

## Lines 33-40
- Configures BuildKit host, image pull secret, and auth service URL.

## Lines 41-48
- Sets OpenAI/GitHub creds and encryption key env vars.

## Lines 49-56
- Sets Phoenix/Nasiko URLs and begins Service definition.

## Lines 57-64
- Service metadata, selector, and port definition start.

## Lines 65-67
- Completes service port mapping to 8000.
