# api_client.py — line-by-line analysis

## Lines 1-8
- Module docstring plus json/typing/requests imports.

## Lines 9-16
- Imports typer/retry adapters, sets up sys/os, and appends CLI path.

## Lines 17-24
- Imports auth manager and cluster URL helper; defines APIClient class.

## Lines 25-32
- Starts APIClient initializer with base URL/cluster arguments.

## Lines 33-40
- Determines base URL using explicit base_url or cluster_name.

## Lines 41-48
- Resolves cluster URL or exits with guidance if unknown.

## Lines 49-56
- Falls back to NASIKO_API_URL or NASIKO_CLUSTER_NAME env vars.

## Lines 57-64
- Resolves env cluster URL or defaults to localhost.

## Lines 65-72
- Sets api_url to `/api/v1` on resolved base URL.

## Lines 73-80
- Initializes auth manager and a requests session.

## Lines 81-88
- Configures retry strategy and mounts HTTP adapter.

## Lines 89-96
- Mounts HTTPS adapter and starts `_get_full_url`.

## Lines 97-104
- Normalizes endpoint path and routes auth endpoints to base URL.

## Lines 105-112
- Routes standard endpoints to api_url and starts `_require_auth`.

## Lines 113-120
- Enforces login and refreshes token, prompting on failure.

## Lines 121-128
- `_make_request` signature and auth header injection.

## Lines 129-136
- Builds full URL and default headers for JSON requests.

## Lines 137-144
- Applies default headers/timeout and begins request attempt.

## Lines 145-152
- Sends request and handles 401 by logging out and exiting.

## Lines 153-160
- Returns response or exits on request exceptions.

## Lines 161-168
- GET wrapper and POST wrapper signature.

## Lines 169-176
- POST sets JSON payload; PUT wrapper signature.

## Lines 177-184
- PUT sets JSON payload; PATCH wrapper signature.

## Lines 185-192
- PATCH sets JSON payload; DELETE wrapper signature.

## Lines 193-200
- DELETE calls request; begins JSON convenience methods.

## Lines 201-208
- get_json returns JSON on 200; starts post_json signature.

## Lines 209-216
- post_json returns JSON on success; starts upload_file signature.

## Lines 217-224
- Upload file parameters and docstring.

## Lines 225-232
- Ensures auth, strips content-type, and computes upload URL.

## Lines 233-240
- Opens file and posts multipart upload with timeout.

## Lines 241-248
- Handles upload 401 by logging out and exiting.

## Lines 249-256
- Catches request errors and missing file errors.

## Lines 257-264
- handle_response signature and response-handling docstring.

## Lines 265-272
- Handles success responses and 404 cases.

## Lines 273-280
- Prints not-found errors and handles 400 responses.

## Lines 281-288
- Handles 403 errors and begins 422 handling.

## Lines 289-296
- Prints validation errors and returns None.

## Lines 297-304
- Handles other error statuses and JSON decoding failures.

## Lines 305-312
- Prints invalid response format and starts auth methods section.

## Lines 313-320
- auth_post wrapper and auth_get signature.

## Lines 321-328
- auth_get wrapper and auth_delete signature.

## Lines 329-336
- auth_delete JSON payload support and global client singleton.

## Lines 337-344
- get_api_client docstring for singleton creation.

## Lines 345-352
- Returns new client for explicit cluster; otherwise builds singleton.

## Lines 353-360
- Creates singleton using env cluster and returns instance.

## Lines 361-368
- require_login decorator builds client and enforces auth.

## Lines 369-374
- Wrapper calls original function and returns decorator.
