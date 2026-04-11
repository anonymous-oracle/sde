# base_adapter.py — line-by-line analysis

## Lines 1-8
- Module docstring describes adapter interface pattern.
- Imports ABC, typing helpers, logging, httpx, and response type.

## Lines 9-16
- Defines BaseAdapter class and docstring.
- __init__ signature starts.

## Lines 17-24
- Stores base_url, timeout, logger; initializes AsyncClient cache.

## Lines 25-32
- _get_client creates httpx.AsyncClient with timeout and headers.

## Lines 33-40
- _get_default_headers returns JSON content type and user agent.

## Lines 41-48
- _make_request signature and docstring.
- Prepares method/endpoint/params/data/headers.

## Lines 49-56
- Builds full URL and merges default/custom headers.
- Logs request metadata.

## Lines 57-64
- Executes httpx request with params, json body, headers.
- Logs response status code.

## Lines 65-72
- Returns response object on success.
- Starts timeout exception handling.

## Lines 73-80
- Logs timeout and re-raises.
- Logs request error and re-raises.

## Lines 81-88
- Logs unexpected errors and re-raises.
- Starts _handle_response_error method.

## Lines 89-96
- Attempts to parse error response JSON for message.
- Falls back to HTTP status message on parse failure.

## Lines 97-104
- Returns standardized NANDAApiResponse with error info.
- Starts _sanitize_unicode method.

## Lines 105-112
- Sanitizes strings by replacing invalid unicode.
- Recursively handles dicts and lists.

## Lines 113-120
- Returns sanitized or unchanged object.
- Starts _build_success_response method.

## Lines 121-128
- Sanitizes data then returns success NANDAApiResponse.
- Starts close() method.

## Lines 129-136
- Closes AsyncClient if present and clears reference.
- Declares abstract health_check.

## Lines 137-137
- Health_check abstract method stub (pass).
