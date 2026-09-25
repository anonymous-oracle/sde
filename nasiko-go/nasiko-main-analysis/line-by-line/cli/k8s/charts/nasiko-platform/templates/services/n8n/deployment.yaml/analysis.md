# deployment.yaml — line-by-line analysis

## Lines 1-8
- Defines n8n Deployment metadata, namespace, and labels.

## Lines 9-16
- Sets replicas, selector, pod labels, and starts container spec.

## Lines 17-24
- Configures image, port 5678, and timezone env vars.

## Lines 25-32
- Sets N8N_PATH/editor/webhook URLs and permission enforcement env vars.

## Lines 33-40
- Sets runner, host/port/protocol env vars and basic auth flags.

## Lines 41-48
- Sets basic auth user/pass and volumeMount for n8n data.

## Lines 49-56
- Configures resource requests/limits and liveness probe.

## Lines 57-64
- Defines readiness probe settings.

## Lines 65-72
- Configures volumes with PVC and starts security context.

## Lines 73-84
- Sets fsGroup/runAsUser for file permissions.
