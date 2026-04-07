# n8n_handler.py — line-by-line analysis

## Lines 1-8
- Module docstring and initial imports (HTTPException/status, BaseHandler, SuccessResponse, n8n entities) begin.

## Lines 9-16
- Completes n8n entity imports for request/response models and workflow list response.

## Lines 17-24
- Imports typing helpers, defines N8nHandler class, and starts __init__.

## Lines 25-32
- __init__ calls BaseHandler; register_workflow_as_agent starts with logging.

## Lines 33-40
- Logs registration context and fetches decrypted N8N credentials for the user.

## Lines 41-48
- Returns failure response when no credentials and prepares to create N8N service.

## Lines 49-56
- Imports N8nService and instantiates it with user base_url/api_key/logger.

## Lines 57-64
- Calls service registration and begins success response handling when result is ok.

## Lines 65-72
- Builds success N8nRegisterResponse with agent identifiers and webhook/upload info.

## Lines 73-80
- Returns failure response on service error and starts credential management method.

## Lines 81-88
- create_or_update_credential logs intent and imports N8nService for connection testing.

## Lines 89-96
- Instantiates N8nService, tests connection, and raises 400 on failure.

## Lines 97-104
- Starts building credential data and imports datetime/timezone utilities.

## Lines 105-112
- Populates credential_data with user, connection, URL/key, type, active state, timestamps.

## Lines 113-120
- Upserts credential and raises 500 when persistence fails.

## Lines 121-128
- Returns simplified connect response with connection_name and status info.

## Lines 129-136
- Re-raises HTTPException and delegates unexpected errors to handle_service_error.

## Lines 137-144
- Starts test_connection method, logs, and begins credential retrieval.

## Lines 145-152
- Returns failure if no credential and instantiates N8nService with stored creds.

## Lines 153-160
- Tests connection and returns UserN8NCredentialResponse with success/message.

## Lines 161-168
- Handles errors in test_connection and starts get_user_credential signature.

## Lines 169-176
- Logs retrieval, fetches credential, and raises 404 when missing.

## Lines 177-184
- Builds UserN8NCredentialSingleResponse with nested response fields.

## Lines 185-192
- Adds is_active/last_tested/created_at/updated_at to credential response payload.

## Lines 193-200
- Re-raises HTTPException and delegates other errors to handle_service_error.

## Lines 201-208
- update_credential logs intent and checks for existing credential.

## Lines 209-216
- Raises 404 if missing and begins connection test when URL/API key changes.

## Lines 217-224
- Resolves test URL and selects API key from request or stored credential.

## Lines 225-232
- Fetches decrypted credential when needed and builds N8nService for testing.

## Lines 233-240
- Tests connection and raises 400 on failure.

## Lines 241-248
- Builds update_data with updated_at and optional URL/key updates.

## Lines 249-256
- Sets is_active flag and updates repository; raises 500 if update fails.

## Lines 257-264
- Starts success response for updated credentials after repository update.

## Lines 265-272
- Completes updated credential response and re-raises HTTPException.

## Lines 273-280
- Populates response fields (user_id/name/url/is_active/last_tested/created_at).

## Lines 281-288
- Closes response and handles update_credential errors via handle_service_error.

## Lines 289-296
- delete_credential begins, logs, and fetches existing credential to validate.

## Lines 297-304
- Raises 404 if credential missing.

## Lines 305-312
- Deletes credential, raises 500 on failure, and returns SuccessResponse.

## Lines 313-320
- Re-raises HTTPException and delegates delete errors to handle_service_error.

## Lines 321-328
- list_workflows signature/docstring and logging for workflow listing request.

## Lines 329-336
- Fetches user credential, raises ValueError if missing, and prepares service.

## Lines 337-344
- Imports and instantiates N8nService with user credentials.

## Lines 345-352
- Retrieves workflows, initializes list, and filters by active_only flag.

## Lines 353-360
- Builds workflow_item dict with ids, names, flags, counts, updated time, and tags.

## Lines 361-368
- Appends items, applies limit, and begins WorkflowListResponse return.

## Lines 369-376
- Fills WorkflowListResponse with list, totals, connection name, and message.

## Lines 377-384
- Starts ValueError handling with a 400 HTTPException for invalid credentials.

## Lines 385-392
- Continues error handling and prepares to delegate generic failures.

## Lines 393-396
- Delegates list_workflows errors to handle_service_error and ends file.
