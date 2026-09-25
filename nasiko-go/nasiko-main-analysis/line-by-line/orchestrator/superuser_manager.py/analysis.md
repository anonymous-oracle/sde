# superuser_manager.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports for env/time/logging/requests.

## Lines 9-16
- Imports json/Optional, sets logger, and declares SuperuserManager class.

## Lines 17-24
- Initializes auth URL and reads superuser email/username env vars.

## Lines 25-32
- Reads password env var and starts wait_for_auth_service.

## Lines 33-40
- Polls auth health endpoint and returns True on success.

## Lines 41-48
- Ignores request errors, logs retry, and sleeps between attempts.

## Lines 49-56
- Logs failure and defines check_user_exists request.

## Lines 57-64
- Posts username to check endpoint and returns exists flag.

## Lines 65-72
- Logs request errors and begins create_superuser logic.

## Lines 73-80
- Posts register payload with username/email/superuser flag.

## Lines 81-88
- Parses response and extracts user_id/access key/secret.

## Lines 89-96
- Saves credentials and returns user_id on success.

## Lines 97-104
- Logs missing fields and handles 400 already-exists case.

## Lines 105-112
- Returns placeholder for existing user and logs other errors.

## Lines 113-120
- Handles request exception and returns None; starts get_superuser_id.

## Lines 121-128
- Posts login request and handles non-200 response.

## Lines 129-136
- Extracts access token and validates presence.

## Lines 137-144
- Fetches profile with token and checks response status.

## Lines 145-152
- Extracts user_id from profile and returns it.

## Lines 153-160
- Logs profile failure and handles request exceptions.

## Lines 161-168
- Starts ensure_superuser, waits for auth, and checks user exists.

## Lines 169-176
- Logs existing user and proceeds to attempt creation.

## Lines 177-184
- Calls create_superuser and logs success details.

## Lines 185-192
- Returns user_id and starts save_credentials_to_file signature.

## Lines 193-200
- Builds credentials dict with IDs, keys, and timestamps.

## Lines 201-208
- Computes credentials file path and opens file for writing.

## Lines 209-216
- Writes JSON, logs file location and access key.

## Lines 217-224
- Logs secret hidden and handles file write errors.

## Lines 225-228
- Returns superuser credential summary dict.
