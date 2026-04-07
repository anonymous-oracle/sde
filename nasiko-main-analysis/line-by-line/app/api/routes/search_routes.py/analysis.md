# search_routes.py — line-by-line analysis

## Lines 1-8
- Module docstring for autocomplete search endpoints.
- Imports APIRouter, Query, Depends, handler factory, auth dependency, and response types.

## Lines 9-16
- Defines create_search_routes factory and router with prefix `/search`.
- Declares GET /users endpoint with response model and metadata.

## Lines 17-24
- search_users parameters: query with min/max length.
- Adds limit query param and user_id dependency.

## Lines 25-32
- Docstring describes user search features (prefix, case-insensitive, fuzzy).
- Delegates to handlers.search.search_users.

## Lines 33-40
- Declares GET /agents endpoint with response model and metadata.
- search_agents parameters: query and limit, user_id dependency.

## Lines 41-48
- Docstring describes agent search features and ranking.
- Delegates to handlers.search.search_agents.

## Lines 49-56
- Declares POST /index/user endpoint for internal indexing.
- index_user handler delegates to handlers.search.index_user.

## Lines 57-64
- Returns router.
