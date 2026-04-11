# handler.lua — line-by-line analysis

## Lines 1-8
- Defines handler table, imports cjson/http, sets priority/version, and starts access hook.

## Lines 9-16
- Stores request body/start time and begins body_filter with chunk/eof.

## Lines 17-24
- Initializes response buffer when missing and prepares to append chunks.

## Lines 25-32
- Appends chunk data and stores complete response on final chunk.

## Lines 33-40
- Starts log hook, loads request/response bodies, and skips if missing.

## Lines 41-48
- Logs skip, declares parsed bodies, and wraps JSON decoding in pcall.

## Lines 49-56
- Decodes request/response JSON and logs parsing errors.

## Lines 57-64
- Validates JSON-RPC method is message/send and that id exists.

## Lines 65-72
- Builds log payload with request/response data and timestamp.

## Lines 73-80
- Adds processing time and schedules async send; logs timer failure.

## Lines 81-88
- Ends log hook and starts send_to_chat_service with premature check.

## Lines 89-96
- Creates HTTP client, timeout, and request endpoint URL.

## Lines 97-104
- Sends POST request with JSON body and handles missing response.

## Lines 105-112
- Logs error or success and closes HTTP client.

## Lines 113-115
- Ends helper and returns ChatLoggerHandler.
