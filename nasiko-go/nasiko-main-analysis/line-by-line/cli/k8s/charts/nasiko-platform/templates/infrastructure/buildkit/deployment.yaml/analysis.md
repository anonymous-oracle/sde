# deployment.yaml — line-by-line analysis

## Lines 1-8
- Defines buildkitd Deployment metadata, namespace, labels, and selector.

## Lines 9-16
- Sets pod labels and annotations for apparmor/seccomp unconfined.

## Lines 17-24
- Specifies service account and pod security context.

## Lines 25-32
- Configures container image and args for TCP listener and sandbox flag.

## Lines 33-40
- Exposes port 1234 and sets security context/runAs user/group.

## Lines 41-48
- Defines resource requests/limits and volume mounts for cache/docker config.

## Lines 49-56
- Liveness probe executes buildctl workers command.

## Lines 57-64
- Readiness probe executes buildctl workers command.

## Lines 65-72
- Defines PVC volume for buildkit-cache.

## Lines 73-79
- Defines docker-config secret volume with config.json item mapping.
