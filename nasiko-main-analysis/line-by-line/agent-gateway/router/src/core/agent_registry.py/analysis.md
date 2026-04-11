# agent_registry.py — line-by-line analysis

## Lines 1-8
- Module docstring, imports logging/typing/httpx, and settings.

## Lines 9-16
- Initializes logger and declares AgentRegistryError exception class.

## Lines 17-24
- Defines AgentRegistry class and __init__ with timeout/cache fields.

## Lines 25-32
- Starts fetch_agent_cards signature and docstring.

## Lines 33-40
- Documents args/returns and error conditions for fetch.

## Lines 41-48
- Checks cache and builds registry URL plus auth headers.

## Lines 49-56
- Logs fetch and starts async HTTP request.

## Lines 57-64
- Parses response JSON, validates, and extracts agent_cards.

## Lines 65-72
- Updates cache timestamp, logs count, and returns cards.

## Lines 73-80
- Handles HTTP status errors with logging and custom exception.

## Lines 81-88
- Handles request errors and unexpected exceptions.

## Lines 89-96
- Validates response contains data list in _validate_response.

## Lines 97-104
- Checks cache validity using timestamps and imports time.

## Lines 105-112
- Compares TTL, clears cache in clear_cache, and logs.

## Lines 113-120
- Starts find_agent_by_name docstring and arguments.

## Lines 121-128
- Iterates agent cards and returns match by name.

## Lines 129-136
- Logs access errors and returns None when missing.

## Lines 137-144
- Starts get_agent_url docstring and argument list.

## Lines 145-152
- Finds agent by name and returns its url field.

## Lines 153-160
- Starts get_fallback_agent docstring describing tuple return.

## Lines 161-168
- Iterates cards, selects first with name+url.

## Lines 169-172
- Returns fallback tuple or None.
