# deployment.yaml — line-by-line analysis

## Lines 1-8
- Declares Kong gateway Deployment metadata, namespace, replicas, and selector.

## Lines 9-16
- Sets match labels, pod template labels, and starts container list.

## Lines 17-24
- Defines Kong container image and database env settings.

## Lines 25-32
- Continues Kong env settings for DB user/password and logging paths.

## Lines 33-40
- Configures Kong log streams and proxy/admin listen addresses.

## Lines 41-48
- Configures admin GUI URL and plugin/Lua path settings.

## Lines 49-56
- Sets Lua package path and begins exposing proxy/admin ports.

## Lines 57-64
- Adds remaining ports and mounts custom plugin volume.

## Lines 65-72
- Defines Kong liveness probe using `kong health`.

## Lines 73-80
- Starts chat-history container, image, and Mongo env vars.

## Lines 81-88
- Exposes chat API port and defines liveness probe.

## Lines 89-96
- Sets chat-history readiness probe configuration.

## Lines 97-104
- Defines configMap volume and mounts nasiko-auth plugin files.

## Lines 105-112
- Mounts chat-logger plugin files and starts Service definition.

## Lines 113-120
- Service metadata, LoadBalancer type, and selector.

## Lines 121-128
- Service ports for proxy and proxy-ssl.

## Lines 129-136
- Service ports for admin and manager.

