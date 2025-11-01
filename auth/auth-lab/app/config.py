import os

def env_str(key: str, default: str | None = None) -> str:
    """Fetch a string from environment, or default. Crash if required missing."""
    val = os.environ.get(key, default)
    if val is None:
        raise RuntimeError(f"Missing required env var: {key}")
    return val

def env_int(key: str, default: int | None = None) -> int:
    val = os.environ.get(key)
    if val is None:
        if default is None:
            raise RuntimeError(f"Missing required env var: {key}")
        return default
    return int(val)

# Example "mock secret" for dev; production would set a real secret
AUTHLAB_SECRET = env_str("AUTHLAB_SECRET", default="dev-only-not-for-prod") 
SESSION_TTL_SECONDS = env_int("SESSION_TTL_SECONDS", default=1800) # 30m
