# nanda_service.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports for Optional/logging and NANDAAdapter.

## Lines 9-16
- Imports NANDA API request/response types and declares NANDAService class.

## Lines 17-24
- Class docstring and __init__ set logger and adapter instance.

## Lines 25-32
- get_all_agents signature with paging/filter parameters.

## Lines 33-40
- get_all_agents docstring describing arguments and return type.

## Lines 41-48
- Starts try block and logs requested filters.

## Lines 49-56
- Builds NANDAAgentsListRequest with defaults and filters.

## Lines 57-64
- Calls adapter.get_agents and starts success handling.

## Lines 65-72
- Logs retrieved count and returns response; exception handling begins.

## Lines 73-80
- Returns error response and starts get_agent_by_id signature.

## Lines 81-88
- get_agent_by_id docstring and argument description.

## Lines 89-96
- Validates agent_id and returns 400 response on missing value.

## Lines 97-104
- Logs fetch and calls adapter.get_agent_by_id.

## Lines 105-112
- Logs success with agent name and returns response.

## Lines 113-120
- Logs errors and returns 500 response for get_agent_by_id failures.

## Lines 121-128
- Begins search_agents signature and docstring.

## Lines 129-136
- Validates query and returns 400 response when missing.

## Lines 137-144
- Sanitizes query length and logs search.

## Lines 145-152
- Calls adapter.search_agents and starts success handling.

## Lines 153-160
- Logs result count and returns response.

## Lines 161-168
- Handles search errors and returns 500 response.

## Lines 169-176
- get_agents_by_category signature and docstring.

## Lines 177-184
- Validates category list and prepares error response.

## Lines 185-192
- Returns invalid category response and logs category fetch.

## Lines 193-200
- Calls adapter.get_agents_by_category and logs success.

## Lines 201-208
- Returns response or error response on exception.

## Lines 209-216
- get_online_agents signature/docstring and logging.

## Lines 217-224
- Calls adapter.get_online_agents and starts success branch.

## Lines 225-232
- Logs online count and returns response.

## Lines 233-240
- Handles online agent errors with 500 response.

## Lines 241-248
- get_agent_facts signature/docstring begins.

## Lines 249-256
- Validates agent_id and returns 400 response if missing.

## Lines 257-264
- Logs facts fetch and calls adapter.get_agent_facts.

## Lines 265-272
- Logs success and returns facts response.

## Lines 273-280
- Handles facts errors with 500 response.

## Lines 281-288
- get_agent_statistics signature/docstring begins.

## Lines 289-296
- Logs statistics start and fetches all agents via adapter.

## Lines 297-304
- Returns failure response if agent fetch fails; extracts agents list.

## Lines 305-312
- Computes total/online/offline counts.

## Lines 313-320
- Builds category breakdown from agents list.

## Lines 321-328
- Builds specialty breakdown and starts stats dict.

## Lines 329-336
- Adds online percentage and categories to stats.

## Lines 337-344
- Computes top specialties, logs, and returns success response.

## Lines 345-352
- Handles statistics errors and returns 500 response.

## Lines 353-360
- health_check signature/docstring and logging.

## Lines 361-368
- Calls adapter.health_check and returns response.

## Lines 369-376
- Handles health check errors with 500 response.

## Lines 377-384
- Starts Messages API section and get_all_messages signature/docstring.

## Lines 385-392
- get_all_messages args for pagination and docstring continuation.

## Lines 393-400
- Logs fetch and builds NANDAMessagesListRequest.

## Lines 401-408
- Calls adapter.get_messages and starts success handling.

## Lines 409-416
- Logs message count and returns response.

## Lines 417-424
- Handles message fetch errors with 500 response.

## Lines 425-432
- get_messages_by_agent signature and docstring start.

## Lines 433-440
- Validates agent_id and prepares error response.

## Lines 441-448
- Logs fetch and calls adapter.get_messages_by_agent.

## Lines 449-456
- Logs count and returns response.

## Lines 457-464
- Handles agent message errors with 500 response.

## Lines 465-472
- get_messages_by_conversation signature/docstring begins.

## Lines 473-480
- Validates conversation_id and prepares error response.

## Lines 481-488
- Logs fetch and calls adapter.get_messages_by_conversation.

## Lines 489-496
- Logs count and returns response.

## Lines 497-504
- Handles conversation message errors with 500 response.

## Lines 505-512
- get_messages_by_type signature/docstring begins.

## Lines 513-520
- Validates message_type against allowed types.

## Lines 521-528
- Returns invalid type response and logs fetch.

## Lines 529-536
- Calls adapter.get_messages_by_type and logs count.

## Lines 537-544
- Returns response or 500 error on exception.

## Lines 545-552
- get_message_statistics signature/docstring begins.

## Lines 553-560
- Logs start and fetches recent messages for analysis.

## Lines 561-568
- Returns failure response or extracts messages list.

## Lines 569-576
- Computes total_messages and message_types breakdown.

## Lines 577-584
- Computes agent_activity and top_active_agents.

## Lines 585-592
- Builds region_activity and stats dict.

## Lines 593-600
- Grabs messages list, computes total_messages, and starts message_types counts.

## Lines 601-608
- Builds message_types counts and begins agent_activity aggregation.

## Lines 609-616
- Completes agent_activity and derives top_agents list.

## Lines 617-624
- Builds region_activity counts for messages.

## Lines 625-632
- Constructs stats dict with totals, types, top agents, regions, and note.

## Lines 633-640
- Logs calculated stats and returns success NANDAApiResponse.

## Lines 641-648
- Logs message statistics errors and returns failure response.

## Lines 649-655
- close method docstring and awaits adapter.close.
