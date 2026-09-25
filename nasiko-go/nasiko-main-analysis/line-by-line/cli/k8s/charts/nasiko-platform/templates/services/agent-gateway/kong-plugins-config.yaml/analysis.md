# kong-plugins-config.yaml — line-by-line analysis

## Lines 1-8
- Defines ConfigMap metadata and starts nasiko-auth handler Lua source.

## Lines 9-16
- Imports cjson and declares NasikoAuthHandler plus validate_token signature.

## Lines 17-24
- Creates HTTP client, sets timeout, and builds auth/validate request.

## Lines 25-32
- Sends JSON body, handles request failure logging.

## Lines 33-40
- Returns decoded body on 200 or falls through to warning.

## Lines 41-48
- Logs auth failure and starts access handler with path lookup.

## Lines 49-56
- Skips auth for health/status and OPTIONS preflight.

## Lines 57-64
- Skips auth for login/register/GitHub/callback/check endpoints.

## Lines 65-72
- Reads authorization header and returns 401 if missing.

## Lines 73-80
- Extracts Bearer token and returns 401 on invalid format.

## Lines 81-88
- Builds auth service URL and calls validate_token.

## Lines 89-96
- Returns 401 if token invalid or expired.

## Lines 97-104
- Adds token validation data into downstream request headers.

## Lines 105-112
- Forwards Authorization header and logs auth success.

## Lines 113-120
- Returns auth handler and starts nasiko-auth schema definition.

## Lines 121-128
- Defines auth_service_url field in schema with requirements.

## Lines 129-136
- Defines timeout field and closes schema record.

## Lines 137-144
- Ends auth schema and starts chat-logger handler Lua source.

## Lines 145-152
- Defines ChatLoggerHandler and starts log_chat_interaction helper.

## Lines 153-160
- Sends POST to /log-chat with JSON payload.

## Lines 161-168
- Handles request failure and non-200/201 status warnings.

## Lines 169-176
- Returns success and starts is_chat_request helper.

## Lines 177-184
- Checks agent path and JSON-RPC message/send payloads.

## Lines 185-192
- Returns match status and starts access handler.

## Lines 193-200
- Reads request context and skips non-chat requests.

## Lines 201-208
- Stores request metadata for logging (time, method, user).

## Lines 209-216
- Adds request body/IP and begins header_filter handler.

## Lines 217-224
- Stores response status/time in shared context.

## Lines 225-232
- body_filter captures response body chunk for logging.

## Lines 233-240
- Saves response body and starts log handler.

## Lines 241-248
- Initializes request/response data structures for parsing.

## Lines 249-256
- Parses JSON-RPC request and builds request_data metadata.

## Lines 257-264
- Adds request metadata fields and closes request parse branch.

## Lines 265-272
- Handles non-JSON requests and begins response parsing.

## Lines 273-280
- Parses JSON-RPC response and builds response_data metadata.

## Lines 281-288
- Adds response status/timestamp or raw body fallback.

## Lines 289-296
- Builds log entry with request/response/timestamp.

## Lines 297-304
- Uses ngx.timer.at to send log asynchronously.

## Lines 305-312
- Calls log_chat_interaction with configured URL/timeout.

## Lines 313-320
- Logs success/failure and ends log handler.

## Lines 321-328
- Returns ChatLoggerHandler and starts chat-logger schema.

## Lines 329-336
- Defines schema record and chat_service_url field.

## Lines 337-344
- Defines timeout field and closes schema structure.

## Lines 345-349
- Ends schema and ConfigMap data.
