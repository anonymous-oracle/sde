import os
import secrets
import hashlib
import hmac
import base64

# Configuration loaded from environment (Mental Model: 12-Factor App)
# Default provided for local dev/learning ONLY.
SECRET_KEY = os.environ.get("APP_SECRET_KEY", "student-local-secret-key-change-me")

def generate_secure_token(n_bytes: int = 32) -> str:
    """
    Generates a URL-safe, high-entropy string for session IDs or CSRF tokens.
    
    Args:
        n_bytes: Number of random bytes to generate (not string length).
                 32 bytes = 256 bits of entropy (Standard for modern auth).
    
    Returns:
        A URL-safe text string.
    """
    # 1. GET RANDOMNESS: Pull 32 bytes from OS CSPRNG.
    #    Never use random.getrandbits() or random.choice() here.
    random_bytes = secrets.token_bytes(n_bytes)
    
    # 2. ENCODE: Convert raw binary -> ASCII string safe for HTTP headers/URLs.
    #    urlsafe_b64encode replaces standard '+' and '/' with '-' and '_'.
    #    rstrip("=") removes padding characters which are often unnecessary for tokens.
    token = base64.urlsafe_b64encode(random_bytes).decode('utf-8').rstrip("=")
    
    return token

def hash_data(data: str) -> str:
    """
    Creates a SHA-256 fingerprint of the data. 
    Useful for integrity checks, NOT for password storage (too fast).
    """
    # 1. ENCODE INPUT: Hashing requires bytes, not strings.
    payload_bytes = data.encode('utf-8')
    
    # 2. HASH: Compute digest.
    digest = hashlib.sha256(payload_bytes).hexdigest()
    
    return digest

def verify_token_safe(user_input: str, expected_token: str) -> bool:
    """
    Compares two tokens in constant time to prevent timing attacks.
    
    Args:
        user_input: The token provided by the user (untrusted).
        expected_token: The real token stored in DB/Session (trusted).
    """
    # 1. CONSTANT TIME CHECK:
    #    Iterates through the entire length of the strings.
    #    Does not short-circuit on the first mismatch.
    return hmac.compare_digest(user_input, expected_token)

# --- Intuition Test ---
if __name__ == "__main__":
    # Simulate a user login session creation
    session_id = generate_secure_token()
    print(f"[Log] Generated Session ID: {session_id} (Length: {len(session_id)})")
    
    # Simulate an attacker trying to guess it
    attacker_guess = "A" * len(session_id)
    
    # Insecure check (Mental Model: DON'T DO THIS)
    # if session_id == attacker_guess: ... 
    
    # Secure check
    is_valid = verify_token_safe(attacker_guess, session_id)
    print(f"[Log] Attacker guess valid? {is_valid}")