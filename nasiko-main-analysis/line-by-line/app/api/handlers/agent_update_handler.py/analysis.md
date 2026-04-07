# agent_update_handler.py — line-by-line analysis

## Lines 1-8
- Module docstring for agent update/rollback handler.
- Imports HTTPException/status/UploadFile, BaseHandler, request/response types.

## Lines 9-16
- Imports AgentVersionInfo and Optional typing.
- Defines AgentUpdateHandler class.

## Lines 17-24
- __init__ stores update service using AgentUpdateService.
- update_agent signature begins.

## Lines 25-32
- Logs update request metadata.
- Validates file presence and filename.

## Lines 33-40
- Enforces .zip extension when file provided.
- Calls update_service.update_agent with request fields.

## Lines 41-48
- On success, builds AgentUpdateResponse with 202 Accepted.
- On failure, builds error response with 400.

## Lines 49-56
- Handles exceptions, logs error, raises 500.
- rollback_agent signature begins.

## Lines 57-64
- Logs rollback request metadata.
- Calls update_service.rollback_agent.

## Lines 65-72
- On success, returns AgentRollbackResponse with 202.
- On failure, returns 400 response.

## Lines 73-80
- Handles rollback errors with 500 response.
- get_version_history signature begins.

## Lines 81-88
- Logs version history lookup.
- Calls update_service.get_version_history.

## Lines 89-96
- On success, transforms versions into AgentVersionInfo list.
- Builds AgentVersionHistoryResponse with 200.

## Lines 97-104
- On missing agent, raises 404.
- Handles errors and raises 500.
