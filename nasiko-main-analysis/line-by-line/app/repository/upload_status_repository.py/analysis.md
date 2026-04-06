# upload_status_repository.py — line-by-line analysis

## Lines 1-8
- Module docstring describes upload tracking repository.
- Imports datetime, ObjectId, and base repository.

## Lines 9-16
- Defines `UploadStatusRepository` and constructor.
- Sets Mongo collection `upload-status`.

## Lines 17-24
- `ensure_indexes` creates indexes for upload metadata fields.
- Includes unique `upload_id` and `agent_name`, `status`, `owner_id`.

## Lines 25-32
- Adds compound indexes for agent_name+created_at and owner_id+created_at.
- Logs success message.

## Lines 33-40
- Warns on index errors.
- `get_upload_status_by_id` fetches by Mongo `_id`.

## Lines 41-48
- `create_upload_status` inserts record and returns by ID.
- `get_upload_status_by_upload_id` fetches by upload_id.

## Lines 49-56
- `update_upload_status` sets `updated_at`, updates by upload_id.
- Returns updated record.

## Lines 57-64
- `update_upload_status_by_agent_name` starts and handles Pydantic v2 models.
- Converts to dict with `exclude_none`.

## Lines 65-72
- Handles Pydantic v1 models or dict inputs.
- Ensures update payload is a plain dict.

## Lines 73-80
- Adds `updated_at` timestamp.
- Fetches latest upload for agent by created_at desc.

## Lines 81-88
- Updates the latest upload if found, returns updated doc.
- Returns None if no upload exists.

## Lines 89-96
- `get_upload_status_by_agent_name` queries and sorts newest first.
- Returns all matching records.

## Lines 97-104
- `get_upload_statuses_by_user` queries by owner_id with limit.
- Sorts by created_at desc and returns list.

## Lines 105-112
- `delete_upload_status_by_agent_id` deletes all records for agent.
- Logs deletion count and returns it.

## Lines 113-120
- Logs errors on delete failures and returns 0.

## Lines 121-122
- End of repository class.
