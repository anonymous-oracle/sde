# nanda_adapter.py — line-by-line analysis (part 1)

## Lines 1-8
- Module docstring describes NANDA API adapter.
- Imports BaseAdapter and NANDA API response/request models.

## Lines 9-16
- Continues imports of NANDA types for agents and messages.

## Lines 17-24
- Defines NANDAAdapter class and docstring.
- Constructor sets default base_url and calls BaseAdapter.

## Lines 25-32
- Defines health_check; calls GET /api/health.
- Returns success payload on 200.

## Lines 33-40
- On non-200, returns standardized error via _handle_response_error.
- On exception, returns 500 with error message.

## Lines 41-48
- Starts get_agents with request model and docstring.
- Prepares to build query parameters.

## Lines 49-56
- Adds type/limit/page/status/category/search params when present.
- Calls GET /api/agents with params.

## Lines 57-64
- On success, parses JSON and sanitizes unicode.
- Parses into NANDAAgentsResponse model.

## Lines 65-72
- Returns success response with model_dump.
- On non-200, returns standardized error.

## Lines 73-80
- On exception, logs and returns 500 with failure message.
- Starts get_agent_by_id with docstring.

## Lines 81-88
- Calls GET /api/agents/{agent_id}.
- On success, sanitizes JSON and parses into NANDAAgent.

## Lines 89-96
- Wraps into NANDAAgentDetailResponse and returns success response.
- Handles 404 with not found response.

## Lines 97-104
- On other status, uses _handle_response_error.
- Handles exceptions with 500 response.

## Lines 105-112
- Begins get_agents_by_category helper and docstring.
- Builds NANDAAgentsListRequest for category.

## Lines 113-120
- Delegates to get_agents and returns response.

## Continuation
- Remaining methods (search, online, facts, messages) continue in part 2.
