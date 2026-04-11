# observability_routes.py — line-by-line analysis

## Lines 1-8
- Module docstring for Phoenix GraphQL proxy routes.
- Imports APIRouter, HTTPException, Query, Depends, Request, typing.

## Lines 9-16
- Imports handler factory and auth dependency.
- Defines create_observability_routes and router prefix.

## Lines 17-24
- Declares GET /session/list endpoint with start_time query.
- Requires user_id dependency.

## Lines 25-32
- Docstring explains aggregated sessions and filtering.
- Reads Authorization header and enforces presence.

## Lines 33-40
- Delegates to handlers.observability.get_all_sessions.
- Declares GET /session/{session_id} endpoint.

## Lines 41-48
- get_session_details delegates to handler.
- Declares GET /trace/{project_id}/{trace_id} endpoint.

## Lines 49-56
- get_trace_details delegates to handler.
- Declares GET /span/{span_id} endpoint.

## Lines 57-64
- get_span_details delegates to handler.
- Declares GET /agent/{agent_id}/stats endpoint with start_time.

## Lines 65-72
- get_agent_project_stats delegates to handler.
- Returns router.

## Lines 73-80
- Returns trace details and defines span details endpoint signature.

## Lines 81-88
- Span details docstring and handler delegation.

## Lines 89-96
- Defines agent stats endpoint with start_time query and user_id.

## Lines 97-104
- Docstring describes stats args and returned metrics.

## Lines 105-112
- Delegates to get_agent_project_stats and returns router.
