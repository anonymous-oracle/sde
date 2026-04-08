# docker-compose.local.yml — line-by-line analysis

## Lines 1-8
- Header comments, services root, and mongodb service with image definition.

## Lines 9-16
- mongodb container name/restart, port mapping, env credentials, and volume start.

## Lines 17-24
- mongodb volumes/networks and healthcheck test/interval/timeout.

## Lines 25-32
- mongodb retries and redis service definition with image, container, and ports.

## Lines 33-40
- redis command, volumes, networks, and healthcheck test/interval.

## Lines 41-48
- redis healthcheck timeout/retries and start of core backend service.

## Lines 49-56
- nasiko-backend build context/dockerfile, container/restart, ports, depends_on mongodb.

## Lines 57-64
- backend depends_on redis and environment with Mongo user/pass/host/port.

## Lines 65-72
- backend environment adds DB name, Redis, encryption key, OpenAI, GitHub, and auth URL.

## Lines 73-80
- backend env Phoenix/K8S/buildkit/pull secret and mounts volumes/networks.

## Lines 81-88
- backend networks and healthcheck test/interval/timeout/retries.

## Lines 89-96
- Auth layer comment and nasiko-auth-service image/platform/container/restart.

## Lines 97-104
- auth depends_on mongodb/redis and environment for NODE_ENV/MONGO_URL.

## Lines 105-112
- auth env Redis/JWT/auth db/port plus ports and networks.

## Lines 113-120
- auth healthcheck and gateway layer comment start.

## Lines 121-128
- kong-database image/container/restart and environment for postgres settings.

## Lines 129-136
- kong-database volumes/networks and healthcheck test/interval.

## Lines 137-144
- kong-database healthcheck timeout/retries and kong-migrations service start.

## Lines 145-152
- kong-migrations depends_on and environment for Kong postgres config.

## Lines 153-160
- kong-migrations networks/command and start kong-gateway service.

## Lines 161-168
- kong-gateway depends_on and environment for Kong DB configuration.

## Lines 169-176
- kong-gateway environment sets DB user/pass and access/error logs/listeners.

## Lines 177-184
- kong-gateway GUI settings, plugin paths, and volume mount for plugins.

## Lines 185-192
- kong-gateway ports and networks configuration.

## Lines 193-200
- kong-gateway healthcheck and chat-history-service build section start.

## Lines 201-208
- chat-history-service build context/dockerfile, container/restart, depends_on mongodb.

## Lines 209-216
- chat-history-service environment, ports, networks, and healthcheck.

## Lines 217-224
- chat-history healthcheck and kong-service-registry build section start.

## Lines 225-232
- registry container/restart, depends_on, and environment for Kong admin and socket.

## Lines 233-240
- registry env for interval/network/host mapping and volumes mount.

## Lines 241-248
- registry ports/networks and healthcheck test.

## Lines 249-256
- registry healthcheck and router layer comment with nasiko-router build start.

## Lines 257-264
- nasiko-router container/restart, depends_on backend, and environment start.

## Lines 265-272
- router env for LLM endpoints/keys and provider/model defaults.

## Lines 273-280
- router ports/networks and healthcheck test/interval/timeout.

## Lines 281-288
- router healthcheck retries and observability layer comment with phoenix service start.

## Lines 289-296
- phoenix image/container/restart, port mappings, and environment start.

## Lines 297-304
- phoenix environment values, volume mount, networks, and healthcheck test.

## Lines 305-312
- phoenix healthcheck and web frontend layer comment with nasiko-web image.

## Lines 313-320
- nasiko-web platform/container/restart, depends_on kong, and ports.

## Lines 321-328
- nasiko-web environment for API/chat/router/auth/agents base URLs.

## Lines 329-336
- nasiko-web env IS_DEVELOPMENT, networks, and healthcheck config.

## Lines 337-344
- web healthcheck and superuser init job build definition.

## Lines 345-352
- superuser-init dockerfile/container, depends_on services, and env start.

## Lines 353-360
- superuser env credentials/auth URL, networks, volumes, and entrypoint.

## Lines 361-368
- superuser command/restart and redis listener build start.

## Lines 369-376
- redis listener container/restart, depends_on redis/backend, and env start.

## Lines 377-384
- redis listener env for Redis, networks, gateway, K8S, and OpenAI key.

## Lines 385-392
- redis listener volumes and networks configuration.

## Lines 393-400
- redis listener command and top-level volumes definitions.

## Lines 401-407
- Top-level networks definitions for app-network and agents-net.
