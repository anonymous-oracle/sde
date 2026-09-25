# chat_send.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports for typer/requests/uuid/json.

## Lines 9-16
- Imports Rich UI helpers and auth manager, creates console.

## Lines 17-24
- Defines send_message_command, starts auth checks.

## Lines 25-32
- Validates login and refreshes auth token.

## Lines 33-40
- Sets request/session IDs and generates context/message UUIDs.

## Lines 41-48
- Builds JSON-RPC payload with message parts.

## Lines 49-56
- Prints request info and begins progress spinner block.

## Lines 57-64
- Configures spinner task and prepares headers.

## Lines 65-72
- Adds auth headers and sends POST request with timeout.

## Lines 73-80
- Removes task and starts response handling for success path.

## Lines 81-88
- Parses JSON response and delegates to display handler.

## Lines 89-96
- Handles JSON decode errors and non-200 responses.

## Lines 97-104
- Handles connection and timeout errors.

## Lines 105-112
- Handles generic exceptions and starts display_agent_response.

## Lines 113-120
- Extracts result and handles missing result case.

## Lines 121-128
- Iterates artifacts and starts scanning parts for text.

## Lines 129-136
- Extracts text and prints response panel for artifacts.

## Lines 137-144
- Marks response found and starts fallback to message parts.

## Lines 145-152
- Iterates message parts and prints text responses.

## Lines 153-160
- Sets response found and handles no-text warning.

## Lines 161-168
- Continues no-text handling and enters exception block.

## Lines 169-173
- Logs parse error and prints raw JSON response.
