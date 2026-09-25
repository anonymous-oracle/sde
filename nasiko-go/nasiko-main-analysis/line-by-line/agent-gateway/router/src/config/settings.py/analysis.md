# settings.py — line-by-line analysis

## Lines 1-8
- Module docstring, imports typing/BaseSettings/field_validator.

## Lines 9-16
- Defines RouterConfig class and environment settings.

## Lines 17-24
- Defines backend and API key settings plus default Minimax/Ollama URLs.

## Lines 25-32
- Configures LLM provider/model and vector store settings.

## Lines 33-40
- Sets request limits and server host/port/reload options.

## Lines 41-48
- Defines CORS origins string and log level config.

## Lines 49-56
- cors_origins_list property parses comma-separated origins.

## Lines 57-64
- Validates NASIKO_BACKEND URL starts with http/https.

## Lines 65-72
- Validates log level and normalizes to uppercase.

## Lines 73-80
- Defines model_config env files and case sensitivity; instantiates settings.

## Lines 81-81
- Exposes global settings instance.
