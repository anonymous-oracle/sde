# base_repository.py — line-by-line analysis

## Lines 1-8
- Module docstring declares this as the shared base repository.
- Imports OS access, base64 utilities, Fernet crypto, and ABC for inheritance.

## Lines 9-16
- Defines `BaseRepository` as an abstract base.
- `__init__` stores DB handle and logger references.

## Lines 17-24
- Initializes an encryption key on construction.
- `_get_or_create_encryption_key` reads `USER_CREDENTIALS_ENCRYPTION_KEY` from env.

## Lines 25-32
- If the env var is missing, logs an error and raises `ValueError`.
- Attempts base64 URL-safe decoding of the key; logs/raises on decode failure.

## Lines 33-40
- Continues error reporting for invalid key.
- Starts `_encrypt_data`, with early return on empty input.

## Lines 41-48
- Builds a `Fernet` instance and encrypts the plaintext.
- Base64-encodes the encrypted bytes for storage; logs on failure.

## Lines 49-56
- `_decrypt_data` mirrors encryption: early return if empty.
- Base64-decodes stored ciphertext and constructs `Fernet` for decryption.

## Lines 57-61
- Decrypts bytes to a string and returns it.
- Logs and raises any decryption errors.
