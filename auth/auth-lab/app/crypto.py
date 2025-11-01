# app/crypto.py
from __future__ import annotations
import secrets
import hmac
import hashlib
from typing import Tuple
from base64 import urlsafe_b64encode, urlsafe_b64decode


def rand_token(nbytes: int = 32) -> str:
    """
    Returns a URL-safe random token (base64url). Good for CSRF, session IDs, etc.
    """
    return secrets.token_urlsafe(nbytes)

def hmac_sha256(key: bytes, message: bytes) -> bytes:
    """
    Computes HMAC-SHA256(key, message). Use for MACing tokens or small blobs.
    """
    return hmac.new(key, message, hashlib.sha256).digest()

def constant_time_eq(a: bytes, b: bytes) -> bool:
    """
    Constant-time compare to avoid timing leaks in equality checks.
    """
    return hmac.compare_digest(a, b)

def pbkdf2_hash(password: str, salt: bytes | None = None, *, rounds: int = 210_000) -> Tuple[bytes, bytes]:
    """
    Derive a slow hash from a password using PBKDF2-HMAC-SHA256.
    Returns (salt, derived_key). We'll wrap this with a serializer later.
    """
    if salt is None:
        salt = secrets.token_bytes(16)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, rounds, dklen=32)
    return salt, dk

def encode_record(alg: str, rounds: int, salt: bytes, dk: bytes) -> str:
    """
    Serialize a password hash record as a compact string:
    format: alg$rounds$base64url(salt)$base64url(derived_key)
    """
    return f"{alg}${rounds}${urlsafe_b64encode(salt).decode()}${urlsafe_b64encode(dk).decode()}"

def decode_record(record: str):
    alg, rounds, salt_b64, dk_b64 = record.split("$", 3) # ensuring strict record interpretation format by restricting beyond 3 splits
    return alg, int(rounds), urlsafe_b64decode(salt_b64), urlsafe_b64decode(dk_b64)

def hash_password(password: str, *, rounds: int = 210_000, pepper: str | None = None) -> str:
    """
    Hash a password with PBKDF2-HMAC-SHA256, optionally MAC it with a pepper, which could be an application specific secret sitting outside the DB,
    """
    # 1) Derive key from password+salt
    salt, dk = pbkdf2_hash(password, rounds=rounds)
    # 2) Optionally bind to a pepper (app secret) using HMAC
    if pepper:
        dk = hmac_sha256(pepper.encode("utf-8"), dk)
    return encode_record("pbkdf2_sha256", rounds, salt, dk)

def verify_password(password: str, record: str, *, pepper: str | None = None) -> bool:
    """
    Verify password against the stored record.
    """
    alg, rounds, salt, expected = decode_record(record)
    if alg != "pbkdf2_sha256":
        return False # we'll support migrations later
    # Recompute
    _, dk = pbkdf2_hash(password, salt=salt, rounds=rounds)
    if pepper:
        dk = hmac_sha256(pepper.encode("utf-8"), dk)
    # Constant-time check
    return constant_time_eq(dk, expected)

if __name__ == "__main__":
    random_token = rand_token()
    print(f"Random token: {random_token}")

    random_token_bytes = random_token.encode("utf-8")
    msg_bytes = "This is a test message".encode("utf-8")

    hmac_sha256_digest = hmac_sha256(random_token_bytes, msg_bytes)
    print(f"HMAC-SHA256: {hmac_sha256_digest.hex()}")

    pwd = "correct horse battery staple password"
    salt, pwd_hash = pbkdf2_hash(pwd)
    print(f"PBKDF2 Hash: salt={salt.hex()} hash={pwd_hash.hex()}")

    pwd = "CorrectHorseBatteryStaple"
    pepper = "dev-pepper"
    record = hash_password(pwd, pepper=pepper)
    print(f"Record: {record}")

    print(f"Password verification - True case {verify_password(pwd, record, pepper=pepper)}")
    print(f"Password verification - False case {verify_password("wrong", record, pepper=pepper)}")
