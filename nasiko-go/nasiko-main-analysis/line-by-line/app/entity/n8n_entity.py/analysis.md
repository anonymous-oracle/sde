# n8n_entity.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports for Pydantic, typing, datetime.

## Lines 9-16
- Defines `UserN8NCredentialCreateRequest` with connection_name, n8n_url, api_key.

## Lines 17-24
- Defines `UserN8NCredentialUpdateRequest` and optional connection_name/n8n_url.

## Lines 25-32
- Adds optional api_key and is_active.
- Declares empty `UserN8NCredentialTestRequest` and begins response model.

## Lines 33-40
- `UserN8NCredentialResponse` fields: success, message, user_id, connection_name, n8n_url.

## Lines 41-48
- Adds is_active and timestamps; begins `UserN8NCredentialSingleResponse`.

## Lines 49-56
- SingleResponse fields and starts `UserN8NConnectResponse`.

## Lines 57-64
- ConnectResponse fields; starts `WorkflowSummary` model.

## Lines 65-72
- WorkflowSummary fields (id, name, active, metadata).
- Starts `WorkflowListResponse`.

## Lines 73-80
- WorkflowListResponse fields (list, total_count, connection_name, message).
- Starts `N8nRegisterRequest` with workflow_id.

## Lines 81-88
- Adds optional agent_name and agent_description fields.

## Lines 89-96
- `N8nRegisterResponse` fields: success, message, agent_name, agent_id.

## Lines 97-103
- Adds webhook_url, container_name, upload_id fields.
