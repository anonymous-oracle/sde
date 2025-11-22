import secrets
import random
import os
import hmac
from load_dotenv import load_dotenv


load_dotenv()

# ---------------------------------------------------------
# 1. LOADING CONFIG (No .env libraries)
# ---------------------------------------------------------
def get_config():
    # We default to None to force crash if critical keys are missing in prod
    secret = os.environ.get("APP_SECRET_KEY") 
    if not secret:
        # Fallback ONLY for local dev/learning
        print("WARN: using unsafe default secret")
        return "unsafe-default-key"
    return secret

# ---------------------------------------------------------
# 2. GENERATING TOKENS
# ---------------------------------------------------------
def demonstrate_generators():
    # BAD: Predictable. Do not use for session IDs or reset tokens.
    # An attacker can reconstruct the seed after 624 outputs.
    bad_token = random.randint(0, 100000)
    
    # GOOD: Uses OS entropy (noise from hardware drivers, etc.).
    # Blocking or non-blocking depending on OS implementation, but secure.
    # 32 bytes = 256 bits of entropy.
    secure_token = secrets.token_hex(32) 
    
    print(f"Insecure: {bad_token}")
    print(f"Secure:   {secure_token}")

# ---------------------------------------------------------
# 3. CONSTANT TIME COMPARISON
# ---------------------------------------------------------
def verify_token(input_token, stored_token):
    # BAD: generic equality (==) fails fast.
    # If stored_token = "ABC...", and input is "ABD...", 
    # it returns False immediately after checking 'B'.
    # Attacker measures time to guess character by character.
    # if input_token == stored_token: ...
    
    # GOOD: compare_digest checks every byte regardless of mismatch position.
    # Prevents Timing Attacks.
    is_valid = hmac.compare_digest(input_token, stored_token)
    return is_valid

if __name__ == "__main__":
    demonstrate_generators()
    
    # Example: Timing attack defense
    real_secret = "deadbeef"
    user_attempt = "deadbaaf"
    print(f"Match: {verify_token(user_attempt, real_secret)}")