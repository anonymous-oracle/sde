# agent_update_routes.py — line-by-line analysis

## Lines 1-8
- Module docstring for update/rollback/version endpoints.
- Imports FastAPI helpers, handler factory, and request/response types.

## Lines 9-16
- Imports auth dependency and Optional typing.
- Defines create_agent_update_routes factory.

## Lines 17-24
- Creates router with prefix `/agents`.
- Declares PUT /{agent_id}/update endpoint with response model.

## Lines 25-32
- update_agent parameters: agent_id path and optional upload file.
- Includes version strategy form field.

## Lines 33-40
- Adds update_strategy form field.
- Adds cleanup_old flag and description.

## Lines 41-48
- Injects user_id dependency.
- Builds AgentUpdateRequest from form fields.

## Lines 49-56
- Delegates update to handlers.agent_update.update_agent.
- Declares POST /{agent_id}/rollback endpoint.

## Lines 57-64
- rollback_agent accepts AgentRollbackRequest and agent_id.
- Uses user_id dependency and delegates to handler.

## Lines 65-72
- Declares GET /{agent_id}/versions endpoint with response model.
- get_version_history delegates to handler.

## Lines 73-89
- Returns router.
