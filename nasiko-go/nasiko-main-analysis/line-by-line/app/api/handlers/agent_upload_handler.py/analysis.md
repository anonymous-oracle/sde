# agent_upload_handler.py — line-by-line analysis

## Lines 1-8
- Module docstring and initial imports for HTTPException/status/UploadFile and response types begin.

## Lines 9-16
- Completes response type imports and brings in Optional typing.

## Lines 17-24
- Defines AgentUploadHandler class and begins __init__ setup.

## Lines 25-32
- Instantiates AgentUploadTrackingService and starts _serialize_datetime_fields helper.

## Lines 33-40
- Copies upload status dict and converts datetime fields to ISO strings.

## Lines 41-48
- Returns serialized dict and starts list-serialization helper.

## Lines 49-56
- Maps list items through serializer; upload_agent_directory signature begins.

## Lines 57-64
- Logs directory upload request with path, user, and agent name.

## Lines 65-72
- Calls process_directory_upload and starts building AgentUploadResponse payload.

## Lines 73-80
- Completes response fields, sets status_code/message, and returns.

## Lines 81-88
- Handles upload_agent_directory errors and begins upload_agent_zip.

## Lines 89-96
- Logs zip upload request with filename and user context.

## Lines 97-104
- Calls process_zip_upload and starts building response item fields.

## Lines 105-112
- Completes response fields, sets status_code/message, and returns.

## Lines 113-120
- Handles upload_agent_zip errors and begins update_upload_status_by_agent_latest.

## Lines 121-128
- Logs update request and calls upload_service for latest status update.

## Lines 129-136
- Serializes datetime fields and returns UploadStatusSingleResponse on success.

## Lines 137-144
- Raises 404 when missing and converts validation errors to 400.

## Lines 145-152
- Re-raises HTTPException, handles generic errors, and begins update_upload_status.

## Lines 153-160
- Logs update request, calls upload_service, serializes and returns on success.

## Lines 161-168
- Returns response or raises 404 when upload_id not found.

## Lines 169-176
- Handles validation errors and re-raises HTTPException.

## Lines 177-184
- Handles generic errors and begins get_user_upload_agents.

## Lines 185-192
- Logs request, fetches upload statuses, and initializes response list.

## Lines 193-200
- Iterates statuses and initializes fields for simplified agent view.

## Lines 201-208
- Attempts registry lookup to derive agent_id and normalize agent_name.

## Lines 209-216
- Extracts description and URL from registry entry when present.

## Lines 217-224
- Extracts tags and skills list with model_dump fallback.

## Lines 225-232
- Ignores registry lookup errors and starts default description logic.

## Lines 233-240
- Sets description based on status_state (Setting Up/Failed/Active).

## Lines 241-248
- Builds SimpleUserUploadAgentResponse with upload info, tags, description, skills.

## Lines 249-256
- Appends results and returns SimpleUserUploadAgentsResponse with count.

## Lines 257-264
- Handles errors and begins _map_status_to_state helper.

## Lines 265-272
- Detects failed states and returns "Failed" when matched.

## Lines 273-280
- Detects active states and returns "Active" when matched.

## Lines 281-288
- Returns default "Setting Up" and begins download_agent_files docstring.

## Lines 289-296
- Docstring details and imports tarfile/tempfile/Path/FileResponse.

## Lines 297-304
- Starts try block and handles versioned agent path with logging.

## Lines 305-312
- Handles non-version path and begins existence validation.

## Lines 313-320
- Builds error message and raises 404 when agent path is missing.

## Lines 321-328
- Creates a temporary tarball file and captures tar_path.

## Lines 329-336
- Opens tarfile, iterates agent directory, and adds files to tarball.

## Lines 337-344
- Logs tarball creation and computes filename with optional version suffix.

## Lines 345-352
- Finalizes filename and returns FileResponse with tarball metadata.

## Lines 353-360
- Re-raises HTTPException and logs unexpected errors before raising 500.

## Lines 361-368
- Raises HTTP 500 with error detail for tarball creation failures.

## Lines 369-376
- Handles exception block completion and ends download_agent_files flow.

## Lines 377-377
- Closes out the file.
