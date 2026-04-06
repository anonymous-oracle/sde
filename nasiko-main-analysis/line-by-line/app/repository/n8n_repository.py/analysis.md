# n8n_repository.py — line-by-line analysis

## Lines 1-8
- Module docstring states N8N credential repository.
- Imports datetime utilities and base repository.

## Lines 9-16
- Defines `N8NRepository` and constructor.
- Sets Mongo collection `user-n8n-credentials`.

## Lines 17-24
- `ensure_indexes` creates indexes for user_id and metadata fields.
- Includes `credential_type`, `is_active`, `last_tested`, `created_at`.

## Lines 25-32
- Logs successful index creation or warns on errors.

## Lines 33-40
- `get_user_n8n_credential_by_user_id` fetches by user_id.
- `get_user_n8n_credential_decrypted` begins decryption path.

## Lines 41-48
- Decrypts `encrypted_api_key` to `api_key` and removes encrypted field.
- `update_user_n8n_credential` signature and docstring.

## Lines 49-56
- Encrypts incoming `api_key`, removes plaintext, sets `updated_at`.

## Lines 57-64
- Performs update by user_id; returns updated doc if modified.

## Lines 65-72
- `upsert_user_n8n_credential` starts; encrypts `api_key` and removes plaintext.
- Sets `updated_at`.

## Lines 73-80
- Removes `created_at` to avoid conflicts, performs upsert with `$setOnInsert`.

## Lines 81-88
- Returns credential after upsert; `delete_user_n8n_credential` begins.

## Lines 89-96
- Deletes credential by user_id and returns boolean.
- `update_credential_test_result` begins.

## Lines 97-104
- Builds update payload with last_tested, status, updated_at.
- Executes update_one.

## Lines 105-112
- Returns updated credential if modified, else None.

## Lines 113-115
- End of repository class.
