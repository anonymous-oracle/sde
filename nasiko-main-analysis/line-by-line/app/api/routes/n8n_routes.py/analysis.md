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
