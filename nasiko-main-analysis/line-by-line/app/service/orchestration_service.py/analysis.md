# orchestration_service.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports for logging, redis, and typing Any.

## Lines 9-16
- Imports datetime/settings, declares OrchestrationService, and starts __init__.

## Lines 17-24
- Stores logger/client/stream name and begins connect method.

## Lines 25-32
- connect builds Redis client with host/port/db and timeouts.

## Lines 33-40
- Pings Redis, logs success, or logs error and clears client.

## Lines 41-48
- is_connected checks client and pings Redis, returning True on success.

## Lines 49-56
- Handles ping failure and starts trigger_agent_orchestration signature.

## Lines 57-64
- Defines parameters and begins docstring with args.

## Lines 65-72
- Completes docstring, reconnects if Redis unavailable.

## Lines 73-80
- Logs failure and returns False; enters try and sets base_url default.

## Lines 81-88
- Builds message dict with command, agent_name, agent_path, and base_url.

## Lines 89-96
- Adds timestamp/source and merges additional_data when provided.

## Lines 97-104
- Sends message to Redis stream and logs message_id.

## Lines 105-112
- Returns True or logs error and returns False on exception.

## Lines 113-120
- get_agent_status signature and docstring start.

## Lines 121-128
- Docstring returns, checks connection, and builds status key.

## Lines 129-136
- Reads status hash, handles last_updated, and returns status data.

## Lines 137-144
- Returns None when missing; logs error and returns None on exception.

## Lines 145-152
- set_agent_status signature and docstring with args.

## Lines 153-160
- Docstring returns, checks connection, and starts try block.

## Lines 161-168
- Builds status_data with agent_name/status/last_updated.

## Lines 169-176
- Filters None details, updates hash, and stores via hset.

## Lines 177-184
- Sets key expiration, logs debug, returns True, or logs error.

## Lines 185-192
- Returns False on error; close method closes Redis client and logs.
