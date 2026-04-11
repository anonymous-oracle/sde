# payload_utils.py — line-by-line analysis

## Lines 1-8
- Imports uuid/typing, UserRequest, file utils, and defines construct_payload.

## Lines 9-16
- Lists function parameters and begins docstring for JSON-RPC payload.

## Lines 17-24
- Docstring details args for request/files/url/output modes/history.

## Lines 25-32
- Docstring returns payload and builds parts list with text/file parts.

## Lines 33-40
- Builds message dict with role, parts, messageId, and contextId.

## Lines 41-48
- Builds configuration block for output modes/history/blocking.

## Lines 49-56
- Removes None entries and starts JSON-RPC payload object.

## Lines 57-64
- Sets JSON-RPC fields, params, and route metadata.

## Lines 65-66
- Returns payload.
