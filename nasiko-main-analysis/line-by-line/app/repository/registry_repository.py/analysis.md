# registry_repository.py — line-by-line analysis

## Lines 1-8
- Module docstring names this as registry operations.
- Imports `ObjectId` and the base repository class.

## Lines 9-16
- Defines `RegistryRepository` and its constructor.
- Stores Mongo collection handle `registry`.

## Lines 17-24
- `ensure_indexes` begins; creates unique and timestamp indexes.
- Indexes for `name`, `id`, `created_at`, and `updated_at`.

## Lines 25-32
- Adds version-related indexes and compound index on `(id, version)`.
- Logs success or warns on failure.

## Lines 33-40
- `create_registry` starts, using current UTC timestamp.
- Initializes default version if missing from input.

## Lines 41-48
- Normalizes version string by removing a leading `v`.
- Prepares to create `version_history` if missing.

## Lines 49-56
- Builds initial version info: status, timestamps, build/deploy IDs.
- Stores rollback metadata with default values.

## Lines 57-64
- Finalizes `version_history` array.
- Ensures `created_at` and `updated_at` timestamps exist.

## Lines 65-72
- Inserts registry document and returns it by ID.
- `get_all_registries` returns all registry entries.

## Lines 73-80
- `get_registry_by_id` fetches by Mongo `_id`.
- `get_registry_by_name` begins with logging.

## Lines 81-88
- Logs lookup and returns the name-based search result.
- `get_registry_by_agent_id` begins with logging.

## Lines 89-96
- Fetches by agent `id`; normalizes version fields if missing.
- Returns the resulting document.

## Lines 97-104
- `update_registry` updates by `_id` and returns the updated doc.
- `delete_registry_by_agent_id` begins with error handling.

## Lines 105-112
- Executes delete by agent ID and logs success/not found.
- Returns boolean indicating deletion result.

## Lines 113-120
- On exception, logs error and returns False.
- `_normalize_version_fields` begins, imports datetime.

## Lines 121-128
- Copies input dict to avoid mutation.
- Adds default `version` if missing.

## Lines 129-136
- Builds `version_history` if missing; derives current time.
- Normalizes timestamp to ISO format.

## Lines 137-144
- Constructs initial version history payload with defaults.
- Includes rollback info and empty build/deploy lists.

## Lines 145-150
- Attaches `version_history` to result and returns.
