# chat_history.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports Optional, typer, and Rich console helpers.

## Lines 9-16
- Imports Panel/Table, API endpoints, API client, and initializes console.

## Lines 17-24
- Starts create_session and gets API client; prepares to send agent_id.

## Lines 25-32
- Posts to chat session endpoint, handles response, and checks errors.

## Lines 33-40
- Extracts session data, prints session ID, created time, and title.

## Lines 41-48
- Handles typer exit and generic exception with error output.

## Lines 49-56
- Begins list_sessions signature and docstring for pagination.

## Lines 57-64
- Builds params, calls list endpoint, and validates result.

## Lines 65-72
- Extracts data and prints header when sessions exist.

## Lines 73-80
- Builds results table and adds session ID/title columns.

## Lines 81-88
- Populates rows and prints the table; pagination note commented.

## Lines 89-96
- Handles no sessions and starts exception handling.

## Lines 97-104
- Ends list_sessions errors and begins get_chat_history signature.

## Lines 105-112
- Sets params, optional cursor, and builds session-specific URL.

## Lines 113-120
- Calls API, handles response, and validates result.

## Lines 121-128
- Prints chat history heading and message count.

## Lines 129-136
- Iterates messages, extracts role/content/timestamp, and sets role color.

## Lines 137-144
- Completes role-color logic and starts formatted message prefix.

## Lines 145-152
- Adds message content (no truncation) and prints panel.

## Lines 153-160
- Pagination note commented and handles no messages case.

## Lines 161-168
- Handles typer exit and generic error for chat history.

## Lines 169-176
- Starts delete_session and prints confirmation warning text.

## Lines 177-184
- Confirms deletion or returns; starts API delete request.

## Lines 185-192
- Sends delete request, handles response, and checks for failure.

## Lines 193-198
- Handles typer exit and generic delete errors.
