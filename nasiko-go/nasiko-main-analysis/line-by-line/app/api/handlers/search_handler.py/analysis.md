# search_handler.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports for BaseHandler plus search response/result models begin.

## Lines 9-16
- Completes model imports, imports RedisSearchService, and declares SearchHandler with docstring.

## Lines 17-24
- __init__ stores service/logger and creates RedisSearchService; initialize_search starts.

## Lines 25-32
- initialize_search awaits Redis init, logs success, triggers initial sync, or logs warning.

## Lines 33-40
- Returns success, logs init errors, and defines _sync_initial_data.

## Lines 41-48
- _sync_initial_data logs start and calls user/agent sync helpers.

## Lines 49-56
- Logs sync failures; defines _sync_users with docstring and try block.

## Lines 57-64
- _sync_users imports httpx/os, reads AUTH_SERVICE_URL, and creates AsyncClient.

## Lines 65-72
- Calls auth service users-for-search endpoint and parses response on 200.

## Lines 73-80
- Builds formatted_users list with id/username/display_name/email/role fields.

## Lines 81-88
- Adds avatar_url/is_active/created_at/updated_at to each user entry.

## Lines 89-96
- Bulk indexes users and logs count; logs when no users found.

## Lines 97-104
- Logs warning on non-200 response; logs user sync failure on exception.

## Lines 105-112
- Defines _sync_agents, fetches registries, and starts formatted_agents list/loop.

## Lines 113-120
- Extracts tags from registry tags or capabilities, handling model_dump/dict.

## Lines 121-128
- Normalizes capabilities to dict and checks for tags inside capabilities.

## Lines 129-136
- Builds agent record with id/name/description/tags/icon_url/owner_id.

## Lines 137-144
- Adds version/url/created_at/updated_at and appends to formatted_agents.

## Lines 145-152
- Bulk indexes agents, logs count, and logs sync errors on exception.

## Lines 153-160
- search_users begins, logs query, and validates minimum length.

## Lines 161-168
- Returns early UserSearchResponse when query is too short.

## Lines 169-176
- Executes Redis user search and handles error responses with warning.

## Lines 177-184
- Continues error response and begins converting results to UserSearchResult list.

## Lines 185-192
- Populates UserSearchResult with id/username/display_name/email fields.

## Lines 193-200
- Adds role/avatar_url/score, computes totals, and prepares to log completion.

## Lines 201-208
- Logs completion details before building the response payload.

## Lines 209-216
- Returns UserSearchResponse with data, totals, and message.

## Lines 217-224
- Handles search_users errors and starts search_agents with logging.

## Lines 225-232
- Validates agent query and returns early response for short queries.

## Lines 233-240
- Runs Redis agent search and checks for error result.

## Lines 241-248
- Logs warning and returns AgentSearchResponse when search fails.

## Lines 249-256
- Builds AgentSearchResult list with agent_id/name/description/tags/icon_url.

## Lines 257-264
- Adds owner_id/version/score and computes totals/showing.

## Lines 265-272
- Logs completion and starts AgentSearchResponse return.

## Lines 273-280
- Returns AgentSearchResponse with totals/message and falls into exception handling.

## Lines 281-288
- Handles search_agents errors via handle_service_error.

## Lines 289-296
- Indexing section begins; index_user calls Redis index and logs success.

## Lines 297-304
- Returns success dict or logs failure and returns error response.

## Lines 305-312
- Logs index_user exceptions; index_agent wraps Redis indexing.

## Lines 313-320
- Logs index_agent failures; delete_user_from_search delegates delete call.

## Lines 321-328
- Logs delete_user failures; delete_agent_from_search delegates delete call.

## Lines 329-336
- Logs delete_agent failures; update_agent_in_search method begins.

## Lines 337-344
- Fetches registry by agent_id; warns and returns False if missing.

## Lines 345-352
- Initializes tags list and begins agent_data construction.

## Lines 353-360
- Populates agent_data with id/name/description/tags/icon_url/owner_id/version/url.

## Lines 361-368
- Adds created_at/updated_at and re-indexes agent; logs errors on exception.

## Lines 369-369
- Returns False on update errors and ends file.
