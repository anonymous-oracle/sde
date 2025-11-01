# tests/test_crypto.py
import sys
from pathlib import Path

# Ensure project root is on sys.path when running this file directly.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.crypto import rand_token, hmac_sha256, constant_time_eq

def test_rand_token_uniqueness():
    a = rand_token()
    b = rand_token()
    assert a != b and len(a) >= 43  # ~32 bytes → 43+ chars base64url

def test_constant_time_eq():
    a = b"same"
    b = b"same"
    c = b"diff"
    assert constant_time_eq(a, b)
    assert not constant_time_eq(a, c)
