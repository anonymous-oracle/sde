# github_repository.py — line-by-line analysis

## Lines 1-8
- Module docstring identifies GitHub credentials repository.
- Imports datetime utilities and base repository.

## Lines 9-16
- Defines `GitHubRepository` and constructor.
- Sets Mongo collection `user-github-credentials`.

## Lines 17-24
- `ensure_indexes` creates indexes for user_id and credential metadata.
- Includes `credential_type`, `is_active`, `connection_status`.

## Lines 25-32
- Adds `last_tested` and `created_at` indexes.
- Logs success or warns on error.

## Lines 33-40
- `get_user_github_credential_by_user_id` fetches by user_id.
- `get_user_github_credential_decrypted` starts.

## Lines 41-48
- Decrypts `encrypted_access_token` to `access_token` and removes encrypted field.
- Returns cleaned credential.

## Lines 49-56
- `upsert_user_github_credential` starts; encrypts access token.
- Removes plaintext `access_token` and sets `updated_at`.

## Lines 57-64
- Removes `created_at` if present to avoid conflicts.
- Performs upsert with `$setOnInsert`.

## Lines 65-72
- Returns credential by user_id after upsert.
- `delete_user_github_credential` begins.

## Lines 73-80
- Deletes credential by user_id and returns boolean.
- `update_github_credential_test_result` begins.

## Lines 81-88
- Builds update payload with last_tested, status, updated_at.
- Prepares to update optional GitHub user info.

## Lines 89-96
- If user info provided, adds username, id, avatar_url fields.
- Executes update_one.

## Lines 97-104
- Returns updated credential if modified; else None.

## Lines 105-110
- End of repository class.
