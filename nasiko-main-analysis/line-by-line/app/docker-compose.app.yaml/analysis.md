# docker-compose.app.yaml — line-by-line analysis

## Lines 1-8
- Defines MongoDB service image, container name, restart policy.
- Exposes 27017 and uses env_file.

## Lines 9-16
- Mounts MongoDB data and init scripts.
- Attaches service to app-network.

## Lines 17-24
- Defines Redis service with alpine image and port 6379.
- Connects Redis to app-network.

## Lines 25-32
- Begins nasiko-backend service build config.
- Builds from repo root and app/Dockerfile.

## Lines 33-40
- Exposes port 8000; depends on MongoDB and Redis.
- Uses env_file and sets environment overrides.

## Lines 41-48
- Sets Mongo/Redis/Langtrace/keys/auth env vars.
- Mounts agents and app source volumes.

## Lines 49-56
- Connects backend to app-network and agents-net.
- Defines networks section.

## Lines 57-64
- Declares external networks and Mongo data volume.
