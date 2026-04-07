# chat_history_handler.py — line-by-line analysis

## Lines 1-8
- Imports Optional and FastAPI HTTPException/status.
- Imports BaseHandler and chat entity models.

## Lines 9-16
- Imports ChatHistoryService and defines ChatHistoryHandler.
- __init__ constructs ChatHistoryService.

## Lines 17-24
- create_session signature with user/agent params.
- Calls chat_history_service.create_session.

## Lines 25-32
- Raises 500 if session creation fails.
- Builds SessionResponse with SessionData.

## Lines 33-40
- Handles HTTPException and service errors.
- delete_session signature begins.

## Lines 41-48
- Calls delete_session and returns MessageResponse 204.
- Raises 404 if not found.

## Lines 49-56
- Handles exceptions and service errors.
- get_session_history signature begins.

## Lines 57-64
- Calls service.get_session_history with pagination params.
- Initializes collection and pagination fields.

## Lines 65-72
- Builds SessionHistory list from result messages.
- Populates pagination metadata.

## Lines 73-80
- Returns SessionHistoryResponse with PaginationMetaData.
- Handles exceptions and service errors.

## Lines 81-88
- get_chat_history signature and docstring.
- Calls service.get_chat_history with pagination params.

## Lines 89-96
- Builds ChatHistory list from result messages.
- Populates pagination metadata.

## Lines 97-104
- Returns ChatHistoryResponse.
- Handles exceptions and service errors.
