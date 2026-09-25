# registry_routes.py — line-by-line analysis

## Lines 1-8
- Module docstring for registry routes.
- Imports APIRouter, Path, Depends, Request, auth dependency, handler factory, and types.

## Lines 9-16
- Defines create_registry_routes factory and router with prefix `/registry`.
- Declares POST /registry endpoint metadata.

## Lines 17-24
- create_registry handler delegates to handlers.registry.create_registry.
- Declares GET /registry/user/agents endpoint.

## Lines 25-32
- get_my_agents uses user_id dependency and request.
- Delegates to handlers.registry.get_my_agents.

## Lines 33-40
- Declares GET /registry/user/agents/info endpoint.
- get_my_agents_info delegates to handlers.registry.get_user_agents.

## Lines 41-48
- Declares GET /registry/agent/name/{agent_name} endpoint.
- get_registry_by_name delegates to handlers.registry.get_registry_by_name.

## Lines 49-56
- Declares GET /registry/agent/id/{agent_id} endpoint with auth.
- get_registry_by_agent_id delegates to handler.

## Lines 57-64
- Declares PUT /registry/agent/{agent_name} upsert endpoint.
- Delegates to handlers.registry.upsert_registry_by_name.

## Lines 65-72
- Declares DELETE /registry/agent/{agent_id} endpoint.
- Delegates to handlers.registry.delete_agent_completely.

## Lines 73-80
- Declares PUT /registry/agent/{agent_name}/version/status endpoint.
- Delegates to handlers.registry.update_agent_version_status.

## Lines 81-116
- Returns router.
