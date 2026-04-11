# chat_history_routes.py — line-by-line analysis

## Lines 1-8
- Imports Optional and FastAPI helpers.
- Imports auth dependency, handler factory, and chat entities.

## Lines 9-16
- Defines create_chat_history_routes and router prefix `/chat/session`.
- Declares POST endpoint for session creation.

## Lines 17-24
- create_session uses Body default factory and user_id dependency.
- Delegates to handlers.chat_history.create_session.

## Lines 25-32
- Declares DELETE /{session_id} endpoint.
- delete_session delegates to handler.

## Lines 33-40
- Declares GET /list endpoint for session history.
- Defines query params limit/cursor/direction.

## Lines 41-48
- Delegates get_session_history to handler with pagination.
- Declares GET /{session_id} endpoint for chat history.

## Lines 49-56
- Defines query params for chat history pagination.
- Delegates to handlers.chat_history.get_chat_history.

## Lines 57-113
- Returns router.
