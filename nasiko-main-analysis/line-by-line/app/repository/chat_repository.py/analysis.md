# chat_repository.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports for random, datetime, Optional, and base repo.

## Lines 9-16
- Defines `ChatRepository` and constructor.
- Sets collections for chat sessions and chat history.

## Lines 17-24
- `ensure_indexes` begins; creates indexes on session_id and user_id.

## Lines 25-32
- Adds chat history indexes (session_id, timestamp, compound).
- Logs successful index creation.

## Lines 33-40
- Warns on index errors.
- `_generate_session_title` begins; adjectives list starts.

## Lines 41-48
- Continues adjectives list for session title generation.

## Lines 49-56
- Finishes adjectives list and starts nouns list.

## Lines 57-64
- Continues nouns list entries.

## Lines 65-72
- Finishes nouns list and returns a random adjective+noun title.

## Lines 73-80
- `create_session` signature and parameters start.

## Lines 81-88
- Sets timestamps and title; starts try block and session_document.

## Lines 89-96
- Builds session_document fields; conditionally adds agent_id.

## Lines 97-104
- Adds agent_url if provided; inserts session; prepares response dict.

## Lines 105-112
- Returns created session metadata; logs and raises on error.

## Lines 113-120
- `delete_session` deletes by session_id and user_id; returns boolean.

## Lines 121-128
- Logs and raises on delete error.

## Lines 129-136
- `get_session_history` signature and parameters.

## Lines 137-144
- Starts query and counts total sessions for the user.

## Lines 145-152
- Parses cursor timestamp; sets query window based on direction.

## Lines 153-160
- Handles invalid cursor; executes query with sort and limit+1.

## Lines 161-168
- Determines `has_more` and trims extra item.
- Initializes next/prev cursor variables.

## Lines 169-176
- Computes next/prev cursors when sessions exist and `has_more`.

## Lines 177-184
- Adjusts cursors when a cursor was provided; starts return payload.

## Lines 185-192
- Returns paginated session history with cursors and counts.
- Starts exception handling.

## Lines 193-200
- Logs database error and raises.
- Begins `get_chat_history` signature.

## Lines 201-208
- Sets parameters and starts try block.
- Verifies session exists for user.

## Lines 209-216
- Logs warning and returns None if session not found.
- Initializes query for chat history.

## Lines 217-224
- Parses cursor timestamp and ensures timezone awareness.

## Lines 225-232
- Adds timestamp filter based on direction.
- Handles invalid cursor format and returns None.

## Lines 233-240
- Counts total messages and prepares history query.

## Lines 241-248
- Sorts messages ascending by timestamp and limits to `limit+1`.

## Lines 249-256
- Computes `has_more`, trims list, initializes cursors.

## Lines 257-264
- Sets next/prev cursors when messages exist and `has_more`.

## Lines 265-272
- Adjusts cursors when a cursor was provided; starts return payload.

## Lines 273-280
- Returns paginated chat history payload.
- Logs errors on failure.

## Lines 281-283
- Raises exception after logging.
