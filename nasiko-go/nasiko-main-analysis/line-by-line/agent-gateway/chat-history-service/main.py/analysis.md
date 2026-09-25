# main.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports FastAPI, Pydantic, typing, logging, datetime.

## Lines 9-16
- Imports Mongo driver/os, configures logging, and initializes app.

## Lines 17-24
- Reads Mongo env vars, creates client/db/collection.

## Lines 25-32
- Defines ChatMessage model fields and defaults.

## Lines 33-40
- Defines ChatLogRequest model and starts startup handler.

## Lines 41-48
- Creates indexes on session_id/timestamp in startup.

## Lines 49-56
- Logs startup success or error, then defines extract_user_message.

## Lines 57-64
- Extracts session_id/params/message and validates user role.

## Lines 65-72
- Iterates text parts and assembles content string.

## Lines 73-80
- Validates content and constructs ChatMessage for user.

## Lines 81-88
- Fills message fields, timestamps, metadata, and handles errors.

## Lines 89-96
- Starts extract_assistant_message and validates session_id.

## Lines 97-104
- Extracts result/artifacts and prepares content parts.

## Lines 105-112
- Iterates artifacts/parts to collect text and build content.

## Lines 113-120
- Validates content and constructs assistant ChatMessage.

## Lines 121-128
- Sets assistant message fields, metadata, and handles errors.

## Lines 129-136
- Defines /log-chat endpoint and starts message extraction.

## Lines 137-144
- Adds user message, extracts assistant message, and appends.

## Lines 145-152
- Inserts messages, logs count, and returns success payload.

## Lines 153-160
- Returns "no messages" response when empty list.

## Lines 161-168
- Handles log-chat errors with HTTPException.

## Lines 169-176
- Defines /chat-history endpoint and builds query cursor.

## Lines 177-184
- Retrieves messages, converts ObjectId to string.

## Lines 185-192
- Returns session data or handles retrieval errors.

## Lines 193-200
- Defines /health endpoint and tests DB connection.

## Lines 201-208
- Returns healthy response or raises 503 on failure.

## Lines 209-216
- Starts __main__ guard and imports uvicorn.

## Lines 217-218
- Runs uvicorn server on port 8002.
