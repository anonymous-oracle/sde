# auth_client.py — line-by-line analysis

## Lines 1-8
- Module docstring, imports httpx/os/List, and sets AUTH_SERVICE_URL default.

## Lines 9-16
- Defines AuthClient with base_url and timeout initialization.

## Lines 17-24
- get_user_accessible_agents validates token and begins HTTP call.

## Lines 25-32
- Sends GET request with Authorization header and parses response.

## Lines 33-40
- Returns accessible_agents or empty list; handles exceptions safely.

## Lines 41-48
- get_agents_by_owner issues GET to owner permissions endpoint and parses JSON.

## Lines 49-56
- Extracts agent_id list and returns empty list on failure/exception.

## Lines 57-64
- create_agent_permissions POSTs to auth service with owner_id parameter.

## Lines 65-69
- Returns success status based on HTTP code or False on exception.
