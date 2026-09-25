# main.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports logging, BytesIO, typing helpers.

## Lines 9-16
- Imports FastAPI, CORS, auth security, and router settings/entities.

## Lines 17-24
- Imports orchestrator and configures logging format/level.

## Lines 25-32
- Initializes logger, security scheme, and FastAPI app metadata.

## Lines 33-40
- Adds CORS middleware using configured origins and headers.

## Lines 41-48
- Instantiates RouterOrchestrator and defines /health endpoint.

## Lines 49-56
- Runs orchestrator health check with error handling.

## Lines 57-64
- Adds /router/health endpoint and starts /router POST signature.

## Lines 65-72
- Defines form fields, optional files, and bearer credentials.

## Lines 73-80
- Describes router processing endpoint with args/returns.

## Lines 81-88
- Continues docstring and begins processing with validation.

## Lines 89-96
- Validates inputs, logs error, and processes uploaded files.

## Lines 97-104
- Builds UserRequest, logs request and file count.

## Lines 105-112
- Extracts token and returns StreamingResponse from orchestrator.

## Lines 113-120
- Handles HTTPException pass-through and unexpected errors.

## Lines 121-128
- Defines /metrics endpoint with placeholder metrics.

## Lines 129-136
- Returns metrics dict and starts _validate_inputs helper.

## Lines 137-144
- Documents validation arguments and checks session_id.

## Lines 145-152
- Logs session id and checks empty query.

## Lines 153-160
- Returns None on success and starts _process_files helper.

## Lines 161-168
- Documents file processing and handles missing files.

## Lines 169-176
- Iterates uploads, enforces size limit, reads bytes.

## Lines 177-184
- Builds file tuple with filename/content type and handles errors.

## Lines 185-192
- Raises HTTPException on read errors and returns file list.

## Lines 193-200
- Ends file processing and starts __main__ guard.

## Lines 201-208
- Runs uvicorn with host/port/reload/log settings.

## Lines 209-216
- Continues uvicorn config and ends run call.

## Lines 217-218
- End of file.
