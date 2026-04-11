# traces_handler.py — line-by-line analysis

## Lines 1-8
- Imports HTTPException/status, settings, request models, BaseHandler, requests, and json.

## Lines 9-16
- fully_parse_json helper begins with docstring and nested decode function setup.

## Lines 17-24
- decode handles string parsing with json.loads and falls back on JSONDecodeError.

## Lines 25-32
- decode handles dict/list recursion and default passthrough; ends helper body.

## Lines 33-40
- Strips outer quotes, unescapes backslashes, and prepares to parse outer JSON.

## Lines 41-48
- Parses outer JSON or returns raw input; returns decoded structure and exits helper.

## Lines 49-56
- TracesHandler class starts; __init__ uses BaseHandler without service; get_traces begins.

## Lines 57-64
- Builds agent lookup URL/params, logs, performs GET, and checks for 400 status.

## Lines 65-72
- Raises 404 for missing agent and 502 for other non-200 responses.

## Lines 73-80
- Parses agent response, extracts api_key/project_id, and validates presence.

## Lines 81-88
- Raises 502 on invalid agent data; sets traces endpoint URL and headers.

## Lines 89-96
- Builds traces payload and logs intent to fetch traces for agent/project.

## Lines 97-104
- Sends POST request to traces endpoint and raises 502 on non-200 response.

## Lines 105-112
- Parses traces JSON and logs full response payload for debugging.

## Lines 113-120
- If traces exist, logs count and processes nodes with _process_trace_nodes.

## Lines 121-128
- Logs processing errors but returns response; wraps data in GetTracesResponse.

## Lines 129-136
- Handles network errors with 502; re-raises HTTPException as-is.

## Lines 137-144
- Handles unexpected errors with 500; ends get_traces method.

## Lines 145-152
- _process_trace_nodes initializes list and copies each node in a try block.

## Lines 153-160
- Attempts to escape nested trace JSON fields; logs warnings on failure.

## Lines 161-168
- Prepares to recurse into children and invokes recursive processing when present.

## Lines 169-176
- Logs warnings if child processing fails and keeps original children data.

## Lines 177-184
- Appends processed nodes; on failure keeps original node and returns list.

## Lines 185-192
- _escape_trace_json_fields copies trace data and defines JSON-string fields list.

## Lines 193-200
- Iterates fields, checks for string values, and parses nested JSON.

## Lines 201-208
- Serializes normalized JSON and logs when transformed.

## Lines 209-214
- Logs warning on parse failure and returns processed_trace.
