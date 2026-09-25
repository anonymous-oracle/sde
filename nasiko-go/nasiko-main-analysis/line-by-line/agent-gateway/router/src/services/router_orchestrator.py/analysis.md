# router_orchestrator.py — line-by-line analysis

## Lines 1-8
- Module docstring, imports logging/AsyncGenerator/typing utilities.

## Lines 9-16
- Imports core services/errors and entity/router helpers.

## Lines 17-24
- Imports router function, truncate_agent_cards, and sets logger.

## Lines 25-32
- Defines RouterOrchestrator and initializes core services.

## Lines 33-40
- Starts process_request signature and pipeline docstring.

## Lines 41-48
- Documents args/yields and starts try/except wrapper.

## Lines 49-56
- Delegates to _handle_route_selection and handles exceptions.

## Lines 57-64
- Starts _handle_route_selection with logging and status response.

## Lines 65-72
- Begins agent card fetch step with registry call.

## Lines 73-80
- Handles empty registry and returns early on no agents.

## Lines 81-88
- Yields success message and handles registry errors.

## Lines 89-96
- Starts truncate_agent_cards step with logging.

## Lines 97-104
- Handles truncation errors and exits route selection.

## Lines 105-112
- Creates vector store and yields routing status.

## Lines 113-120
- Handles vector store errors and exits.

## Lines 121-128
- Fetches session history and reconstructs conversation.

## Lines 129-136
- Yields history retrieved message or handles failure.

## Lines 137-144
- Calls router for AI selection and logs result.

## Lines 145-152
- Extracts agent_name from RouterOutput or dict and yields selection.

## Lines 153-160
- Handles routing errors and exits.

## Lines 161-168
- Resolves agent URL and sends request to selected agent.

## Lines 169-176
- Yields responses from _send_agent_request.

## Lines 177-184
- Handles agent communication errors and yields failure response.

## Lines 185-192
- Starts _send_agent_request and yields "sending" response.

## Lines 193-200
- Sends agent request, extracts response content, logs success.

## Lines 201-208
- Yields agent response or handles AgentClientError.

## Lines 209-216
- Starts _get_agent_url with lookup logic.

## Lines 217-224
- Returns URL if found or logs fallback usage.

## Lines 225-232
- Uses fallback agent or returns None if unavailable.

## Lines 233-240
- Starts _router_response helper and builds RouterResponse JSON.

## Lines 241-248
- Completes router response serialization and newline.

## Lines 249-256
- Starts health_check and builds health status dict.

## Lines 257-264
- Marks components healthy and handles exceptions.

## Lines 265-272
- Sets unhealthy status on error and logs.

## Lines 273-275
- Returns health status dict and ends file.
