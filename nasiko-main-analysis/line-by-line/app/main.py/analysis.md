# main.py — line-by-line analysis

## Lines 1-8
- Imports FastAPI, SessionMiddleware, asynccontextmanager, Mongo client, settings, repository, service, handlers, and router.

## Lines 9-16
- Imports logging/secrets and configures logging level, format, and stream handler.

## Lines 17-24
- Finishes logging setup, silences pymongo, and sets app logger levels.

## Lines 25-32
- Initializes module logger, logs startup, and defines init_db with AsyncIOMotorClient.

## Lines 33-40
- init_db returns database; lifespan context manager starts and initializes db/repo.

## Lines 41-48
- Ensures collections, builds service/handlers, and prepares search init.

## Lines 49-56
- Initializes Redis search with logging and includes API router under /api/v1.

## Lines 57-64
- Yields control, logs shutdown, and starts FastAPI app definition.

## Lines 65-72
- Sets app metadata/URLs and adds SessionMiddleware with secret key.

## Lines 73-80
- Configures session max_age, same_site, and https_only; notes CORS is handled by Kong.

## Lines 81-86
- Leaves commented OPTIONS handler placeholder for preflight handling.
