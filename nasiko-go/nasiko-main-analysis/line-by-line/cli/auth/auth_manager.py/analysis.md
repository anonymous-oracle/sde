# auth_manager.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports for json/typing/requests.

## Lines 9-16
- Imports typer and attempts keyring import with availability flag.

## Lines 17-24
- Handles missing keyring warning and starts crypto fallback import.

## Lines 25-32
- Imports base64/hashlib, sets crypto availability, imports sys.

## Lines 33-40
- Imports os, adds CLI path to sys.path, and imports CONFIG_DIR.

## Lines 41-48
- Imports cluster URL helper and defines AuthManager constants.

## Lines 49-56
- AuthManager init creates config dir and begins base URL resolution.

## Lines 57-64
- Resolves cluster URL or falls back to localhost for unknown cluster.

## Lines 65-72
- Falls back to NASIKO_API_URL or checks default cluster env var.

## Lines 73-80
- Resolves default cluster URL or defaults to localhost.

## Lines 81-88
- Sets auth_url and file paths for token/credentials storage.

## Lines 89-96
- _get_encryption_key docstring and crypto availability guard.

## Lines 97-104
- Builds user info string and derives PBKDF2 key.

## Lines 105-112
- _encrypt_data returns plain bytes if no crypto, otherwise Fernet encrypt.

## Lines 113-120
- _decrypt_data handles non-crypto case and begins decrypt try.

## Lines 121-128
- Decrypts or raises error; starts _store_secure method.

## Lines 129-136
- Attempts keyring storage then falls back to file-based storage.

## Lines 137-144
- Chooses token/creds file, encrypts, writes, and chmods it.

## Lines 145-152
- Returns success or prints storage error; starts _retrieve_secure.

## Lines 153-160
- Reads from keyring if available; falls back to file storage.

## Lines 161-168
- Chooses file path, reads bytes, and decrypts if present.

## Lines 169-176
- Handles retrieval errors, returns None, and starts _delete_secure.

## Lines 177-184
- Attempts keyring delete and initializes success flag.

## Lines 185-192
- Deletes file-based token/creds files if they exist.

## Lines 193-200
- Handles deletion errors, returns success, and starts login.

## Lines 201-208
- Builds login URL and posts access key/secret payload.

## Lines 209-216
- Parses successful response and extracts JWT token.

## Lines 217-224
- Stores token, prints success, and optionally stores credentials.

## Lines 225-232
- Finishes credential storage, returns success, or reports failure.

## Lines 233-240
- Extracts error detail on login failure and returns False.

## Lines 241-248
- Handles request/other exceptions and starts get_auth_headers.

## Lines 249-256
- Returns Authorization header if token exists; starts is_logged_in.

## Lines 257-264
- is_logged_in uses headers; logout deletes token and optional creds.

## Lines 265-272
- Prints logout status messages and returns, with exception handling.

## Lines 273-280
- Handles logout errors; begins refresh_token_if_needed.

## Lines 281-288
- Calls healthcheck and triggers auto-renewal on 401.

## Lines 289-296
- Returns healthcheck status or auto-renews on errors.

## Lines 297-304
- _auto_renew_token loads stored creds and parses JSON.

## Lines 305-312
- Logs renewal, deletes token, and re-runs login.

## Lines 313-320
- Handles auto-renew failure and starts get_user_info.

## Lines 321-328
- Calls /auth/user endpoint and returns JSON on success.

## Lines 329-336
- Returns None on failure and starts clear_all_data.

## Lines 337-344
- Deletes secure tokens and enumerates legacy token files.

## Lines 345-352
- Deletes legacy files, prints success, and returns.

## Lines 353-360
- Handles clear-all errors and defines auth manager cache.

## Lines 361-368
- get_auth_manager docstring and global cache usage.

## Lines 369-376
- Chooses cache key from cluster/base_url/env default.

## Lines 377-381
- Creates cached AuthManager if missing and returns it.
