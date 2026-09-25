# registry_manager.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports json/logging/Path/os plus requests/config.

## Lines 9-16
- Imports NASIKO_API_URL/AGENTS_DIRECTORY and get_kong_agent_url helper.

## Lines 17-24
- Initializes logger and defines RegistryManager class with agents_dir.

## Lines 25-32
- Starts update_agent_registry signature and return-shape docstring.

## Lines 33-40
- Builds AgentCard.json path and handles missing card warning.

## Lines 41-48
- Opens AgentCard.json and loads card data.

## Lines 49-56
- Gets Kong URL for agent folder and starts registry_data setup.

## Lines 57-64
- Sets URL/id and applies owner_id when provided.

## Lines 65-72
- Logs registry data and begins upsert branch.

## Lines 73-80
- Runs upsert and optional permission creation for owner_id.

## Lines 81-88
- Returns upsert result payload with success/url/registry_id.

## Lines 89-96
- Handles delete action or unknown action failure.

## Lines 97-104
- Logs errors and starts _upsert_agent docstring.

## Lines 105-112
- Builds registry URL and logs payload for debugging.

## Lines 113-120
- Sends PUT request and handles successful 200 response.

## Lines 121-128
- Parses registry response JSON and extracts registry_id.

## Lines 129-136
- Logs parse errors and handles non-200 error response.

## Lines 137-144
- Logs failed upsert and handles request exceptions.

## Lines 145-152
- Starts _delete_agent, calls DELETE, and handles success.

## Lines 153-160
- Logs delete failure responses and request errors.

## Lines 161-168
- Starts _create_agent_permissions and builds auth service URL.

## Lines 169-176
- Logs permission creation and sends POST with owner_id param.

## Lines 177-184
- Handles success vs failure for permission creation.

## Lines 185-192
- Logs network or generic errors in permission creation.

## Lines 193-200
- Starts get_agent_api_key and builds LangTrace URL/params.

## Lines 201-208
- Logs retrieval attempt and sends GET to LangTrace.

## Lines 209-216
- Parses API key/project_id and logs success, returns key.

## Lines 217-224
- Handles 400 not found and other error responses.

## Lines 225-232
- Logs network/general errors and starts create_or_get_agent.

## Lines 233-240
- Builds LangTrace agents URL and logs create/retrieve action.

## Lines 241-248
- Sends POST request and parses api_key/project_id/name.

## Lines 249-256
- Logs success and returns success payload dict.

## Lines 257-264
- Logs failure response and returns error payload.

## Lines 265-272
- Handles request/general errors and returns error dicts.

## Lines 273-280
- Starts store_agent_credentials and builds update URL.

## Lines 281-288
- Builds credentials payload and merges additional info.

## Lines 289-296
- Sends PUT request and handles success vs failure.

## Lines 297-304
- Logs network/general errors and returns False.

## Lines 305-305
- End of file.
