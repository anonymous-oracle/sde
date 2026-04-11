# n8n_routes.py — line-by-line analysis

## Lines 1-8
- Module docstring for N8N API endpoints.
- Imports APIRouter, Query, Depends, SuccessResponse, auth dependency, and N8N entity types.

## Lines 9-16
- Continues N8N entity imports for workflow and credential responses.
- Defines create_n8n_routes factory.

## Lines 17-24
- Creates router with prefix `/agents/n8n` and tag.
- Retrieves n8n handler from factory.

## Lines 25-32
- Defines POST /register endpoint for workflow registration.
- Delegates to n8n_handler.register_workflow_as_agent.

## Lines 33-40
- Defines POST /connect endpoint with response model and metadata.
- Starts save_user_n8n_credentials handler signature.

## Lines 41-48
- Docstring explains connection test before save and required fields.
- Delegates to create_or_update_credential.

## Lines 49-56
- Defines GET /credentials endpoint for current user.
- get_user_n8n_credentials delegates to get_user_credential.

## Lines 57-64
- Defines PUT /credentials endpoint with update model.
- update_user_n8n_credentials delegates to update_credential.

## Lines 65-72
- Defines DELETE /credentials endpoint with SuccessResponse.
- delete_user_n8n_credentials delegates to delete_credential.

## Lines 73-80
- Defines GET /workflows endpoint with query params.
- list_workflows delegates to n8n_handler.list_workflows.

## Lines 81-88
- Returns router from factory.

## Lines 89-96
- Defines PUT /credentials route and update_user_n8n_credentials signature.

## Lines 97-104
- Docstring lists updatable fields and notes auto connection testing.

## Lines 105-112
- Delegates to update_credential and starts DELETE /credentials route.

## Lines 113-120
- delete_user_n8n_credentials docstring begins with permanence warning.

## Lines 121-128
- Finishes delete docstring and delegates to delete_credential.

## Lines 129-136
- Defines GET /workflows route with active_only/limit query params.

## Lines 137-144
- Docstring describes workflow list and query parameter meanings.

## Lines 145-152
- Docstring lists returned workflow fields and tags.

## Lines 153-158
- Notes user_id extraction, delegates to list_workflows, returns router.
