# auth.py — line-by-line analysis

## Lines 1-8
- Module docstring for JWT auth via auth service.
- Imports httpx, logging, FastAPI auth utilities, typing, os.

## Lines 9-16
- Sets logger and AUTH_SERVICE_URL from env with default.
- Initializes HTTPBearer security scheme.

## Lines 17-24
- Defines AuthUser class and constructor.
- Stores user_id and subject_type.

## Lines 25-32
- validate_token_with_auth_service signature and docstring.
- Opens httpx.AsyncClient and calls /auth/validate.

## Lines 33-40
- Sends Authorization header and JSON content-type.
- If 200 and valid, returns validation data.

## Lines 41-48
- Logs validation failure and raises HTTP 401 with WWW-Authenticate header.

## Lines 49-56
- Handles auth service request errors with 503.
- Reraises HTTPException and handles generic errors.

## Lines 57-64
- Returns 401 on token validation failure.
- Starts get_current_user dependency.

## Lines 65-72
- Extracts token, validates, reads subject_id/type.
- Returns 401 if user_id missing.

## Lines 73-80
- Returns AuthUser instance.
- Starts get_current_user_optional dependency.

## Lines 81-88
- Returns None if no credentials.
- Validates token and extracts user_id/type.

## Lines 89-96
- Returns AuthUser or None on invalid payload.
- Catches HTTPException and returns None.

## Lines 97-104
- Defines get_user_id_from_token dependency.
- Calls get_current_user and returns user_id.

## Lines 105-112
- Defines verify_token_header dependency with Authorization header.
- Validates Bearer prefix.

## Lines 113-120
- Splits token and validates via auth service.
- Returns 401 if subject_id missing.

## Lines 121-128
- Returns user_id on success.
- Starts get_super_user dependency.

## Lines 129-136
- Validates token; extracts user_id, subject_type, is_super_user.
- Returns 401 if user_id missing.

## Lines 137-144
- Enforces superuser flag; raises 403 if not.
- Returns AuthUser for superuser.
