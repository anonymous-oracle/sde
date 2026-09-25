# config.py — line-by-line analysis

## Lines 1-8
- Imports BaseSettings and defines Config with environment defaults for Mongo credentials.

## Lines 9-16
- Continues defaults for Mongo host/port/db, Redis, Phoenix, and OpenAI/Minimax keys.

## Lines 17-24
- Sets Minimax base URL, BuildKit address, registry/gateway URLs, and DO token.

## Lines 25-32
- Defines K8S_ENABLED, NASIKO_API_URL, and GitHub OAuth settings.

## Lines 33-40
- Adds encryption key and computes MONGO_URI property from config values.

## Lines 41-48
- Exposes MONGO_DB property and configures env file loading/case sensitivity.

## Lines 49-52
- Instantiates the settings object.
