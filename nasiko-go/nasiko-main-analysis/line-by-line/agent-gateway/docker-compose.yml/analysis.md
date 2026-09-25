# docker-compose.yml — line-by-line analysis

## Lines 1-8
- Defines kong-database service with Postgres image and credentials.

## Lines 9-16
- Adds volume/network settings and starts kong-migrations service.

## Lines 17-24
- Configures kong-migrations command, dependency, and DB env vars.

## Lines 25-32
- Finishes kong-migrations env/networks and begins kong service.

## Lines 33-40
- Configures kong dependencies and DB connection env settings.

## Lines 41-48
- Sets Kong log streams and admin listen/GUI URLs.

## Lines 49-56
- Enables chat-logger plugin, mounts plugins, and exposes ports.

## Lines 57-64
- Adds networks/restart and healthcheck interval/timeout.

## Lines 65-72
- Completes healthcheck and starts Konga dashboard service.

## Lines 73-80
- Configures Konga env/ports/network and restart policy.

## Lines 81-88
- Starts kong-service-registry build config and dependencies.

## Lines 89-96
- Sets registry env vars, docker socket mount, and port mapping.

## Lines 97-104
- Adds registry networks/restart and starts nasiko-router service.

## Lines 105-112
- Configures router build, dependencies, and backend/OLLAMA env.

## Lines 113-120
- Sets router keys, mounts code, exposes port, and networks.

## Lines 121-128
- Finishes router restart and begins nasiko-auth-service build.

## Lines 129-136
- Sets auth service dependencies and Mongo/Redis/JWT env vars.

## Lines 137-144
- Adds backend URL, port mapping, networks, and restart policy.

## Lines 145-152
- Adds auth service healthcheck and starts auth-redis service.

## Lines 153-160
- Configures auth-redis image, port, volume, and command.

## Lines 161-168
- Adds redis networks/restart and starts chat-history-service build.

## Lines 169-176
- Sets chat-history env vars, port mapping, and networks.

## Lines 177-184
- Adds restart policy and healthcheck for chat-history-service.

## Lines 185-192
- Declares named volumes and kong-net bridge network.

## Lines 193-196
- Marks agents-net and app-network as external.
