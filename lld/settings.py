import os

def env(key, default=None, cast=str):
    val = os.environ.get(key)
    if val is None:
        return default
    try:
        return cast(val)
    except Exception:
        return default

# Configs
db_dsn = env("DB_DSN", "sqlite:///:memory:")
port = env("PORT", 8080, int)
debug = env("DEBUG", "false").lower() == "true"
