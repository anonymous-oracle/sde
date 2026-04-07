# service.py — line-by-line analysis

## Lines 1-8
- Imports repository/entities, datetime, typing, K8sService, and get_github_access_token.

## Lines 9-16
- Defines convert_objectid_to_str helper to normalize Mongo ObjectId fields.

## Lines 17-24
- Starts extract_and_deduplicate_tags_from_skills, initializes tag collection loop.

## Lines 25-32
- Extends tags list, prepares de-duplication with seen set and loop.

## Lines 33-40
- Finishes deduped tags and starts Service class with __init__ signature.

## Lines 41-48
- Stores repo/logger, initializes K8sService, and begins create_registry.

## Lines 49-56
- Builds registry_dict with timestamps and starts skills tag extraction.

## Lines 57-64
- Collects skills dicts, assigns tags, and prepares duplicate name check.

## Lines 65-72
- Validates uniqueness by name, creates registry, and converts ObjectId.

## Lines 73-80
- Returns RegistryInDB or None and lists all registries via repo.

## Lines 81-88
- Implements get_registry_by_name and starts get_registry_by_agent_id.

## Lines 89-96
- Returns registry by agent_id or None and exposes GitHub access token.

## Lines 97-104
- Starts upload status service method and logs request.

## Lines 105-112
- Fetches upload statuses, logs count, and handles exceptions.

## Lines 113-120
- Logs errors, re-raises, and begins upsert_registry_by_name.

## Lines 121-128
- Logs upsert request and documents deprecated agent.id lookup.

## Lines 129-136
- Uses top-level id when present and resolves existing registry by id.

## Lines 137-144
- Falls back to name lookup and starts update path for existing registry.

## Lines 145-152
- Builds update_dict with timestamps and skills tags.

## Lines 153-160
- Updates registry by ObjectId and prepares to return updated entry.

## Lines 161-168
- Returns updated registry or begins creation path when missing.

## Lines 169-176
- Builds new registry dict with timestamps and starts tag extraction.

## Lines 177-184
- Extracts skills tags and finalizes registry_dict for creation.

## Lines 185-192
- Creates registry, logs success, or logs failure when no result.

## Lines 193-200
- Logs upsert exceptions, prints traceback, and re-raises.

## Lines 201-208
- Starts delete_agent_completely and initializes deletion_results.

## Lines 209-216
- Populates deletion_results structure for registry/K8s/permissions/DB errors.

## Lines 217-224
- Fetches registry to aid deletion and logs findings.

## Lines 225-232
- Logs missing registry and handles errors while fetching.

## Lines 233-240
- Sets registry to None and starts K8s resource deletion.

## Lines 241-248
- Logs K8s deletion failures and moves to permissions deletion step.

## Lines 249-256
- Deletes permissions, stores result, and logs success.

## Lines 257-264
- Logs permission deletion failures and captures error details.

## Lines 265-272
- Starts database cleanup, deletes build and deployment records.

## Lines 273-280
- Deletes upload records and logs cleanup totals.

## Lines 281-288
- Handles DB cleanup errors and begins registry deletion.

## Lines 289-296
- Deletes registry entry when present and logs success.

## Lines 297-304
- Logs registry deletion failures or absence of registry entry.

## Lines 305-312
- Collects registry deletion errors and computes critical error state.

## Lines 313-320
- Determines overall success and logs completion summary.

## Lines 321-328
- Returns deletion summary and handles unexpected exceptions with traceback.

## Lines 329-336
- Returns failure payload and starts _delete_agent_k8s_resources helper.

## Lines 337-344
- Lists deployments for agent and prepares deletion loop.

## Lines 345-352
- Deletes each K8s deployment, logs success, and tracks deletions.

## Lines 353-360
- Logs deletion failures and errors per deployment.

## Lines 361-368
- Returns deleted resources or empty list and starts permissions helper.

## Lines 369-376
- Imports auth dependencies and validates AUTH_SERVICE_URL for permissions.

## Lines 377-384
- Builds permissions URL and opens aiohttp session/delete request.

## Lines 385-392
- Accepts 200/204/404 as success and returns True.

## Lines 393-400
- Logs non-success responses and handles exceptions.

## Lines 401-408
- Logs permission deletion errors and starts build records cleanup.

## Lines 409-416
- Deletes build records and logs errors on failure.

## Lines 417-424
- Deletes deployment records and logs errors on failure.

## Lines 425-432
- Deletes upload records and logs errors on failure.

## Lines 433-435
- Returns 0 on upload record deletion failure and ends file.
