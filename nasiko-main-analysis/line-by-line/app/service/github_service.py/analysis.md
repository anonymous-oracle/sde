# github_service.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports for httpx/asyncio/shutil/tempfile/os/base64.

## Lines 9-16
- Imports hashlib/hmac/json/secrets/typing and datetime/timezone utilities.

## Lines 17-24
- Imports urlencode and GitHub credential enums.

## Lines 25-32
- Declares GitHubService class, constants, and __init__ signature start.

## Lines 33-40
- Stores repo/logger and attempts to load app settings.

## Lines 41-48
- Loads settings or falls back; begins client_id resolution.

## Lines 49-56
- Completes client_id resolution and starts client_secret resolution.

## Lines 57-64
- Completes client_secret resolution and warns if missing.

## Lines 65-72
- get_github_auth_url starts, validates client_id, and derives base_url/state.

## Lines 73-80
- Builds OAuth params including scope and redirect_uri.

## Lines 81-88
- Constructs auth URL, logs, and returns it.

## Lines 89-96
- resolve_oauth_state signature and docstring describing return format.

## Lines 97-104
- Validates state presence and parses signed state prefix.

## Lines 105-112
- Handles signed connect flow and validates user_id.

## Lines 113-120
- Handles signed login flow and rejects unknown flow.

## Lines 121-128
- Supports legacy connect/login prefixes and raw user_id fallback.

## Lines 129-136
- handle_github_callback starts and exchanges code for token.

## Lines 137-144
- Extracts access_token/scopes and fetches user info.

## Lines 145-152
- Builds credential_data with user details and token info.

## Lines 153-160
- Stores credentials via upsert and logs success.

## Lines 161-168
- Returns success payload with user_info.

## Lines 169-176
- Logs callback error and returns failure payload.

## Lines 177-184
- get_github_access_token starts and fetches credential record.

## Lines 185-192
- Returns not_connected when missing and loads decrypted token.

## Lines 193-200
- Tests token validity and updates connection status to ACTIVE.

## Lines 201-208
- Returns connected status with username/avatar/last_tested.

## Lines 209-216
- Updates status to ERROR for invalid token and returns token_expired.

## Lines 217-224
- Returns invalid_credential when token missing in decrypted data.

## Lines 225-232
- Logs errors and returns error status payload.

## Lines 233-240
- github_logout starts and deletes stored credentials.

## Lines 241-248
- Returns success or "not found" response.

## Lines 249-256
- Logs errors and returns failure payload.

## Lines 257-264
- list_github_repositories starts and loads decrypted credentials.

## Lines 265-272
- Validates access_token and fetches repositories via API.

## Lines 273-280
- Logs count and returns repositories list and total.

## Lines 281-288
- Logs errors and re-raises exceptions.

## Lines 289-296
- clone_github_repository starts and loads decrypted credentials.

## Lines 297-304
- Validates access_token and clones repo to temp dir.

## Lines 305-312
- Imports AgentUploadTrackingService and initializes upload service.

## Lines 313-320
- Processes GitHub upload with metadata and returns result.

## Lines 321-328
- Cleans temp directory and returns upload result.

## Lines 329-336
- Logs clone errors and re-raises.

## Lines 337-344
- _exchange_code_for_token starts with token URL/data and headers.

## Lines 345-352
- Posts token exchange request and returns JSON on success.

## Lines 353-360
- Logs errors and raises ValueError on failure.

## Lines 361-368
- _get_github_user_info builds headers and calls GitHub user API.

## Lines 369-376
- Returns JSON on 200 or logs error and raises.

## Lines 377-384
- _test_github_token sends request and returns True on 200.

## Lines 385-392
- Returns False on exceptions.

## Lines 393-400
- _fetch_github_repositories builds headers and params.

## Lines 401-408
- Calls GitHub repos endpoint and handles 200 response.

## Lines 409-416
- Transforms repository fields to internal schema.

## Lines 417-424
- Adds repo fields and appends to transformed list.

## Lines 425-432
- Returns transformed list; logs and raises on errors.

## Lines 433-440
- _clone_repository starts, creates temp dir, builds authenticated clone URL.

## Lines 441-448
- Builds git clone command with depth/branch and target dir.

## Lines 449-456
- Executes git clone subprocess and captures stdout/stderr.

## Lines 457-464
- Logs success, removes .git, and returns temp_dir.

## Lines 465-472
- Handles clone errors, cleans up, and raises ValueError.

## Lines 473-480
- Cleans up on exception and re-raises.

## Lines 481-488
- authenticate_with_github_oauth docstring and starts flow with token exchange.

## Lines 489-496
- Fetches GitHub user info and handles private email fallback.

## Lines 497-504
- Determines auth service URL and calls authenticate endpoint.

## Lines 505-512
- Validates auth response and extracts user_id/token.

## Lines 513-520
- Stores GitHub credentials for repo cloning.

## Lines 521-528
- Returns auth payload with token/user info.

## Lines 529-536
- Logs authentication errors and returns failure payload.

## Lines 537-544
- _store_github_credentials_for_repos builds credential_data.

## Lines 545-552
- Sets token/scopes/status/timestamp and upserts credentials.

## Lines 553-560
- get_github_auth_url_for_login starts and validates client_id.

## Lines 561-568
- Builds login flow state and OAuth params for user:email scope.

## Lines 569-576
- Constructs login auth URL, logs, and returns.

## Lines 577-584
- _get_github_callback_url returns callback URL.

## Lines 585-592
- _build_oauth_state builds payload with flow/iat/nonce/user_id.

## Lines 593-600
- Serializes payload, base64 encodes, and computes signature.

## Lines 601-608
- Fallbacks when signing secret missing and returns legacy state.

## Lines 609-616
- Builds HMAC signature and returns signed state token.

## Lines 617-624
- _decode_oauth_state parses state/version and handles errors.

## Lines 625-632
- Loads state secret and validates HMAC signature.

## Lines 633-640
- Decodes payload, validates iat and max age.

## Lines 641-648
- Returns decoded payload or raises expiration/signature errors.

## Lines 649-656
- _get_oauth_state_secret returns key from env/client_secret/session key.

## Lines 657-664
- _get_base_url_from_request starts with fallback base when no request.

## Lines 665-672
- Logs request headers and resolves host header.

## Lines 673-680
- Determines proto from Cloudflare or x-forwarded-proto.

## Lines 681-688
- Falls back to request.scheme and logs resolved host/proto.

## Lines 689-696
- Handles localhost fallback and returns constructed base URL.

## Lines 697-704
- Returns base URL for host or fallback when host missing.

## Lines 705-712
- Closes state secret return and handles request None fallback with debug log.

## Lines 713-720
- Logs headers, resolves host, initializes proto, and reads cf-visitor.

## Lines 721-728
- Parses cf-visitor scheme or logs parse failure; starts x-forwarded-proto fallback.

## Lines 729-736
- Sets proto from x-forwarded-proto or request.scheme and logs choice.

## Lines 737-744
- Logs resolved host/proto and handles localhost fallback base URL.

## Lines 745-752
- Returns constructed base for host or fallback when host missing.

## Lines 753-753
- Returns base URL and ends file.
