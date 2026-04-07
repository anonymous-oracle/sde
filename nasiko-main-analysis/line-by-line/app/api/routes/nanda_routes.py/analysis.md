# nanda_routes.py — line-by-line analysis

## Lines 1-8
- Module docstring for NANDA registry routes.
- Imports APIRouter, Path, Query, Optional, handler factory, and response type.

## Lines 9-16
- Defines create_nanda_routes and router with prefix `/nanda`.
- Declares GET /health endpoint.

## Lines 17-24
- nanda_health_check delegates to handlers.nanda.health_check.
- Declares GET /agents with filtering query params.

## Lines 25-32
- get_all_agents query params: limit, page, agent_type.
- Adds status and category filters.

## Lines 33-40
- Delegates get_all_agents to handler with params.
- Declares GET /agents/{agent_id} endpoint.

## Lines 41-48
- get_agent_by_id path param and handler delegation.
- Declares GET /agents/search endpoint.

## Lines 49-56
- search_agents query and limit params.
- Delegates to handlers.nanda.search_agents.

## Lines 57-64
- Declares GET /agents/category/{category} endpoint.
- get_agents_by_category delegates to handler.

## Lines 65-72
- Declares GET /agents/online endpoint.
- get_online_agents delegates to handler.

## Lines 73-80
- Declares GET /agents/{agent_id}/facts endpoint.
- Delegates to handlers.nanda.get_agent_facts.

## Lines 81-88
- Declares GET /statistics endpoint.
- Delegates to handlers.nanda.get_agent_statistics.

## Lines 89-96
- Declares GET /messages endpoint with pagination params.
- Delegates to handlers.nanda.get_all_messages.

## Lines 97-104
- Declares GET /messages/agent/{agent_id} endpoint.
- Delegates to handlers.nanda.get_messages_by_agent.

## Lines 105-112
- Declares GET /messages/conversation/{conversation_id} endpoint.
- Delegates to handlers.nanda.get_messages_by_conversation.

## Lines 113-120
- Declares GET /messages/type/{message_type} endpoint.
- Delegates to handlers.nanda.get_messages_by_type.

## Lines 121-128
- Declares GET /messages/statistics endpoint.
- Delegates to handlers.nanda.get_message_statistics and returns router.
