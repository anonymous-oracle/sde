# agent_client.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports logging/typing plus httpx/settings/UserRequest.

## Lines 9-16
- Initializes logger and defines AgentClientError exception class.

## Lines 17-24
- Starts AgentClient class and sets HTTP timeout in __init__.

## Lines 25-32
- Begins _translate_agent_url docstring explaining localhost/Kong mapping.

## Lines 33-40
- Describes arguments/returns and checks for localhost:9100.

## Lines 41-48
- Rewrites localhost URL to kong-gateway and returns original otherwise.

## Lines 49-56
- Starts send_request signature and documents args/returns/errors.

## Lines 57-64
- Continues docstring and begins try block for request handling.

## Lines 65-72
- Translates URL, builds payload, and logs target/payload.

## Lines 73-80
- Builds headers with optional Authorization token.

## Lines 81-88
- Sends async POST request and raises on HTTP errors.

## Lines 89-96
- Parses response JSON and validates error/result fields.

## Lines 97-104
- Logs success and handles HTTPStatusError with custom message.

## Lines 105-112
- Handles request errors and unexpected exceptions.

## Lines 113-120
- Starts _construct_payload docstring and notes circular import.

## Lines 121-128
- Calls construct_payload helper and returns payload.

## Lines 129-136
- Starts extract_response_content docstring and extracts result field.

## Lines 137-144
- Validates result and inspects response kind for message/task.

## Lines 145-152
- Extracts text from message or last task artifact; errors on kind.

## Lines 153-160
- Handles extraction errors and raises AgentClientError.

## Lines 161-168
- Starts _extract_text_from_message docstring and imports helper.

## Lines 169-176
- Calls extract_text_from_message and begins health_check signature.

## Lines 177-184
- Documents health_check arguments/returns.

## Lines 185-192
- Translates URL, constructs health endpoint, and sends GET request.

## Lines 193-200
- Returns status or logs warning on failure.

## Lines 201-208
- Returns False on exception and ends method.

## Lines 209-212
- End of file.
