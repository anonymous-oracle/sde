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

## Lines 121-128
- Completes agent detail parsing and success response.
- Handles 404 not found and generic errors.

## Lines 129-136
- Logs exceptions for get_agent_by_id and returns 500 response.
- Starts get_agents_by_category definition.

## Lines 137-144
- Docstring for category filter and arguments.
- Builds request and delegates to get_agents.

## Lines 145-152
- Starts search_agents with search_query and limit.
- Delegates to get_agents with search parameter.

## Lines 153-160
- Starts get_online_agents with status filter.
- Delegates to get_agents with status=online.

## Lines 161-168
- Starts get_agent_facts method and docstring.
- Retrieves agent via get_agent_by_id.

## Lines 169-176
- If agent fetch failed, returns response.
- Extracts factsUrl from agent data.

## Lines 177-184
- Returns 404 if factsUrl missing.
- Prepares request to facts URL.

## Lines 185-192
- Calls GET to facts URL; on 200 returns success with data.
- Otherwise returns standardized error.

## Lines 193-200
- Handles exceptions with logged error and 500 response.
- Starts get_messages method and docstring.

## Lines 201-208
- Builds query params from request fields (limit, offset, before/after).

## Lines 209-216
- Adds agent_id, conversation_id, message_type params.
- Calls GET /api/messages.

## Lines 217-224
- On success, parses JSON and sanitizes unicode.
- Handles list response by mapping to NANDAMessage.

## Lines 225-232
- Builds NANDAMessagesResponse with total and has_more.
- Handles wrapped response objects.

## Lines 233-240
- Parses wrapped messages list and builds response with totals.
- Returns success response with model_dump.

## Lines 241-248
- On non-200, returns standardized error.
- Handles exceptions and returns 500 response.

## Lines 249-256
- Starts get_messages_by_agent helper and docstring.
- Builds NANDAMessagesListRequest and delegates.

## Lines 257-264
- Starts get_messages_by_conversation helper and docstring.
- Delegates with conversation_id filter.

## Lines 265-272
- Starts get_messages_by_type helper and docstring.
- Delegates with message_type filter.

## Lines 273-280
- Ends class definition and file.

## Lines 281-288
- Builds messages response totals and starts wrapped-response parsing.

## Lines 289-296
- Maps wrapped messages list and calculates total/has_more flags.

## Lines 297-304
- Returns success response or handles non-200 errors.

## Lines 305-312
- Logs exceptions and returns 500 error response.

## Lines 313-320
- Defines get_messages_by_agent and its docstring.

## Lines 321-328
- Builds list request and delegates to get_messages.

## Lines 329-336
- Defines get_messages_by_conversation with args/docstring.

## Lines 337-344
- Builds conversation request and delegates to get_messages.

## Lines 345-352
- Defines get_messages_by_type with args/docstring.

## Lines 353-359
- Builds type request and delegates to get_messages.
