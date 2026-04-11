# deployment.yaml — line-by-line analysis

## Lines 1-8
- Declares Deployment metadata, namespace, replica count, and selector start.

## Lines 9-16
- Defines match labels, pod template metadata, and service account.

## Lines 17-24
- Starts container spec with image, command, and resource requests.

## Lines 25-32
- Defines resource limits and begins MongoDB environment variables.

## Lines 33-40
- Completes MongoDB env vars and starts Auth/Redis settings.

## Lines 41-48
- Adds auth service URL and Redis host/port values.

## Lines 49-56
- Sets Redis DB and BuildKit address settings.

## Lines 57-64
- Adds registry URL and DigitalOcean token placeholders.

## Lines 65-72
- Sets environment, Phoenix collector endpoint, and tracing flags.

## Lines 73-80
- Finishes observability env vars and starts liveness probe.

## Lines 81-88
- Defines liveness probe exec command and timing thresholds.

## Lines 89-96
- Starts readiness probe exec command and timing settings.

## Lines 97-101
- Completes readiness probe settings.
