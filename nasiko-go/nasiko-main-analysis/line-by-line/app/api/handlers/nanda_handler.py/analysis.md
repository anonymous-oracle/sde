# nanda_handler.py — line-by-line analysis

## Lines 1-8
- Module docstring and initial imports (Optional, HTTPException/Query, BaseHandler).

## Lines 9-16
- Imports NANDAService/NANDAApiResponse and declares NANDAHandler with docstring.

## Lines 17-24
- Initializes NANDA service in __init__; get_all_agents signature begins.

## Lines 25-32
- Defines Query params for limit, page, and agent_type filters.

## Lines 33-40
- Adds status/category Query params, return type, and docstring start.

## Lines 41-48
- Docstring details for args/returns of get_all_agents.

## Lines 49-56
- Ends docstring, enters try, and logs request with extra fields.

## Lines 57-64
- Completes log extras and starts agent_type validation list.

## Lines 65-72
- Enumerates valid agent_type values and prepares 400 on invalid input.

## Lines 73-80
- Raises invalid agent_type; validates status and raises 400 when wrong.

## Lines 81-88
- Calls NANDA service to fetch agents with filters.

## Lines 89-96
- Raises on unsuccessful response, logs success, and returns result.

## Lines 97-104
- Handles HTTPException passthrough and wraps unexpected errors as 500.

## Lines 105-112
- get_agent_by_id signature and docstring start.

## Lines 113-120
- Docstring returns, logs request, and enters try block.

## Lines 121-128
- Validates agent_id and calls service; begins error handling branch.

## Lines 129-136
- Raises 404 or service error; logs success with agent_id.

## Lines 137-144
- Returns response and logs unexpected errors for 500.

## Lines 145-152
- Raises 500 on errors; search_agents signature begins.

## Lines 153-160
- Defines search_agents params and starts docstring.

## Lines 161-168
- Docstring args and return description for search_agents.

## Lines 169-176
- Logs search request and calls service; checks response success.

## Lines 177-184
- Raises on failure; logs success and returns response.

## Lines 185-192
- Handles HTTPException passthrough and wraps generic errors as 500.

## Lines 193-200
- get_agents_by_category signature and docstring start.

## Lines 201-208
- Docstring arguments/returns for category filtering.

## Lines 209-216
- Logs category request and calls service.

## Lines 217-224
- Raises on failure and begins success logging.

## Lines 225-232
- Returns response and handles HTTPException/other errors.

## Lines 233-240
- Logs category errors and starts get_online_agents signature.

## Lines 241-248
- Defines get_online_agents params and docstring.

## Lines 249-256
- Docstring ends, logs request, and enters try.

## Lines 257-264
- Calls service to fetch online agents and checks response.

## Lines 265-272
- Logs success/returns and wraps unexpected errors as 500.

## Lines 273-280
- Raises 500 on errors; get_agent_facts docstring begins.

## Lines 281-288
- Docstring ends and logs get_agent_facts request.

## Lines 289-296
- Validates agent_id and calls get_agent_facts service.

## Lines 297-304
- Handles 404 for facts, raises other errors, and starts success log.

## Lines 305-312
- Returns response and wraps unexpected errors as 500.

## Lines 313-320
- Logs errors for facts; get_agent_statistics signature begins.

## Lines 321-328
- Docstring for statistics and log_info call.

## Lines 329-336
- Calls statistics service and raises on failure.

## Lines 337-344
- Logs success/returns and handles unexpected errors.

## Lines 345-352
- Raises 500 on errors; health_check docstring begins.

## Lines 353-360
- Docstring ends, logs health check, and calls service.

## Lines 361-368
- Raises on failure, logs success/returns, and re-raises HTTPException.

## Lines 369-376
- Logs errors for health check and starts Messages API section.

## Lines 377-384
- get_all_messages signature with limit/offset/before params.

## Lines 385-392
- Adds after param, return type, and docstring start.

## Lines 393-400
- Docstring args and return description for message listing.

## Lines 401-408
- Ends docstring and logs request with pagination extras.

## Lines 409-416
- Calls get_all_messages service with pagination filters.

## Lines 417-424
- Raises on failure, logs success, and returns response.

## Lines 425-432
- Handles HTTPException passthrough and wraps errors as 500.

## Lines 433-440
- get_messages_by_agent signature and docstring start.

## Lines 441-448
- Docstring args/returns for agent message query.

## Lines 449-456
- Logs request and notes validation for agent_id.

## Lines 457-464
- Validates agent_id, calls service, and checks response success.

## Lines 465-472
- Logs success and returns agent message response.

## Lines 473-480
- Handles exceptions for agent message retrieval.

## Lines 481-488
- Raises 500 on errors and starts get_messages_by_conversation signature.

## Lines 489-496
- Docstring for conversation message query begins.

## Lines 497-504
- Docstring ends and logs conversation request.

## Lines 505-512
- Validates conversation_id and raises 400 when missing.

## Lines 513-520
- Calls service and raises on failure for conversation lookup.

## Lines 521-528
- Logs success/returns and re-raises HTTPException.

## Lines 529-536
- Logs errors and raises 500 for conversation failures.

## Lines 537-544
- Completes error handling and starts get_messages_by_type signature.

## Lines 545-552
- Docstring args/returns for message type query.

## Lines 553-560
- Logs request and calls get_messages_by_type service.

## Lines 561-568
- Raises on failure and begins success logging.

## Lines 569-576
- Logs success/returns and starts exception handling.

## Lines 577-584
- Logs errors and raises 500 for message type failures.

## Lines 585-592
- Completes error handling and starts get_message_statistics docstring.

## Lines 593-600
- Docstring ends, logs request, and calls statistics service.

## Lines 601-608
- Raises on failure, logs success, and returns response.

## Lines 609-616
- Handles exceptions for message statistics with 500 errors.

## Lines 617-620
- close method docstring and call to close NANDA service.
