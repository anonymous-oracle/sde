import hashlib, time, os, random

def idem_key(prefix: str="", *parts: str) -> str:
    """Deterministic-ish key for a given logical action."""
    base = "|".join([prefix, *[p or "" for p in parts]])
    return "idem_" + str(hashlib.sha256(base.encode()))

def jittered_key(prefix: str) -> str:
    """Unique key when action has no natural dedupe key."""
    salt = f"{time.time_ns()}_{os.getpid()}_{random.randint(0, 999999)}"
    return idem_key(prefix, salt)
