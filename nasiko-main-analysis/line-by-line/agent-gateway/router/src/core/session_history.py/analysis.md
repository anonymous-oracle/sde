# session_history.py — line-by-line analysis

## Lines 1-8
- Module docstring, imports logging/typing/httpx, and settings reference.

## Lines 9-16
- Initializes logger and defines SessionHistoryError exception class.

## Lines 17-24
- Starts SessionHistoryService class and sets request timeout.

## Lines 25-32
- Defines async fetch_session_history signature and docstring start.

## Lines 33-40
- Documents args/returns and failure conditions for fetching.

## Lines 41-48
- Builds chat history URL and auth/content headers.

## Lines 49-56
- Logs request, issues HTTP GET, checks status, and parses JSON.

## Lines 57-64
- Validates response, extracts history, logs count, and returns data.

## Lines 65-72
- Handles HTTPStatusError with logged message and custom exception.

## Lines 73-80
- Handles request errors and unexpected errors with logging.

## Lines 81-88
- Starts _validate_response with docstring and data checks.

## Lines 89-96
- Validates presence of data list and raises ValueError otherwise.

## Lines 97-104
- Defines reconstruct_conversation docstring and return description.

## Lines 105-112
- Builds conversation list and iterates messages into role/content pairs.

## Lines 113-120
- Returns conversation or logs errors and returns empty list.

